"""One-off transport helper; never included in the graph publication."""
from __future__ import annotations
from pathlib import Path
import collections, hashlib, json, os, re, subprocess, urllib.parse, zipfile

BASE = '2b610652fd76598b46be1d065f4798a20275dfba'
BASE_TREE = '0eba32182851e17d0bcffc5bf06f608f99f7ac40'
EXPECTED_BASE_DELTA = '732d2e2c5b619156943d419c2f760d8f30c3b5a9163dd53cb1f7b6413f54461a'


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def protected_ranges(text):
    ranges = []
    front = re.match(r'\A---\r?\n.*?\r?\n---(?:\r?\n|\Z)', text, re.S)
    if front:
        ranges.append(front.span())
    pos = 0
    fence = None
    start = 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if fence is None and marker:
            fence = marker.group(1)
            start = pos
        elif fence and re.match(r'^\s{0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}\s*$', line):
            ranges.append((start, pos + len(line)))
            fence = None
        elif fence is None and re.match(r'^\s{0,3}(?:#{1,6}\s|>|\|)|^\s*\[\^?[^\]]+\]:|^\*\*(?:Status|Evidence(?:/status)?):', line):
            ranges.append((pos, pos + len(line)))
        pos += len(line)
    if fence:
        ranges.append((start, len(text)))
    patterns = [r'(`+)(?!`)(.*?)\1(?!`)', r'\[\[[^\]\n]+\]\]',
                r'!?\[[^\]\n]*\]\([^\n]*?\)', r'\\\[.*?\\\]', r'\\\(.*?\\\)',
                r'\$\$.*?\$\$', r'(?<![\\$])\$(?!\$)[^\n$]*?\$']
    for pattern in patterns:
        ranges.extend(m.span() for m in re.finditer(pattern, text, re.S))
    return ranges


def apply_wrappers(data, replacements):
    text = data.decode('utf-8')
    protected = protected_ranges(text)
    last = 0
    new_pos = 0
    pieces = []
    audit = []
    for start, end, alias, target in sorted(replacements):
        if start < last or start >= end or text[start:end] != alias:
            raise ValueError('Overlapping or incorrect original reference span')
        if any(start < b and end > a for a, b in protected):
            raise ValueError('Non-prose reference cannot be changed: ' + alias)
        if not target.startswith('research/') or any(c in target for c in '\n|[]'):
            raise ValueError('Not an unambiguous full vault path')
        prefix = text[last:start]
        wrapper = '[[' + target + '|' + alias + ']]'
        pieces.extend([prefix, wrapper])
        new_pos += len(prefix)
        audit.append({'start': new_pos, 'end': new_pos + len(wrapper), 'alias': alias, 'wrapper': wrapper})
        new_pos += len(wrapper)
        last = end
    pieces.append(text[last:])
    changed = ''.join(pieces)
    restored = changed
    for item in reversed(audit):
        a, b = item['start'], item['end']
        assert restored[a:b] == item['wrapper']
        restored = restored[:a] + item['alias'] + restored[b:]
    assert restored.encode('utf-8') == data, 'Exact byte restoration failed'
    return changed.encode('utf-8'), audit


def git(*args, **kw):
    return subprocess.check_output(['git', *args], **kw)


def inventory(ref):
    result = {}
    for record in git('ls-tree', '-r', '-z', ref).split(b'\0'):
        if not record:
            continue
        meta, path = record.split(b'\t', 1)
        mode, kind, sha = meta.decode().split()
        result[path.decode()] = {'mode': mode, 'type': kind, 'sha': sha}
    return result


def derive(TREE, ORIGINAL):
    changes = {}
    findings = collections.defaultdict(list)
    for p in TREE:
        if re.fullmatch(r'research/[^/]+/findings/[^/]+\.md', p) and not p.endswith('.review.md'):
            findings[p.split('/')[1]].append(p)

    def put(path, data):
        if isinstance(data, str):
            data = data.encode()
        if data != ORIGINAL.get(path):
            changes[path] = data

    def text(path):
        return changes.get(path, ORIGINAL[path]).decode()

    titles = {}
    for line, files in sorted(findings.items()):
        slug = line.replace('_', '-')
        hub = f'research/{line}/graph/{slug}.md'
        old = ORIGINAL[hub].decode()
        title = re.search(r'^# (.+?) research graph\s*$', old, re.M)[1]
        titles[line] = title
        membership = f'research/{line}/graph/{slug}-membership.md'
        rendered = f'---\nid: RG-{slug}-membership\ntype: research-graph-membership\nscope: {line}\nderived: true\n---\n\n# {title} structural membership\n\n[[{hub[:-3]}|{title} research graph]]\n\nThis stable projection inventories every current canonical {title} finding. Links assert line ownership only, not dependence, support, chronology, novelty, or endorsement. The source of membership is the current findings tree, not a curator window.\n\n'
        for p in sorted(files):
            label = re.match(r'[A-Z]+-\d+', Path(p).name)[0]
            rendered += f'- [[{p[:-3]}|{label}]]\n'
        put(membership, rendered)
        link = f'[[{membership[:-3]}|{title} structural membership]]'
        pattern = r'<!-- structural-membership:start -->\n.*?\n<!-- structural-membership:end -->'
        if re.search(pattern, old, re.S):
            new, n = re.subn(pattern, '## Canonical finding membership (structural)\n\n' + link, old, flags=re.S)
            assert n == 1
        elif f'research/{line}/graph/current-window-' in old:
            new, n = re.subn(r'\[\[research/' + re.escape(line) + r'/graph/current-window-[^|\]]+\|Current curator-window membership\]\]', link, old)
            assert n == 1
        else:
            assert link in old
            new = old
        assert new.count(f'[[{membership[:-3]}|') == 1
        put(hub, new)

    retired = sorted(p for p in TREE if '/graph/' in p and p.endswith('.md') and re.match(r'(?:current-(?:frontier|window)-|frontier-membership)', Path(p).name))
    retired += ['research/prime_flute/graph/relations/legacy-pf015-collision-and-duplicate.md', 'research/prime_circle/graph/relations/legacy-pc015-id-collision.md']
    for p in retired:
        put(p, None)
    global_path = 'research/graph/global.md'
    old = text(global_path)
    new = re.sub(r'^- \[\[research/graph/frontier-membership(?:-tail)?\|[^\]]+\]\]\n', '', old, flags=re.M)
    assert new != old
    put(global_path, new)

    mi_path = 'research/graph/intuition-membership.md'
    mi = sorted(p for p in TREE if re.fullmatch(r'research/(?:[^/]+/)?mind/intuition/MI-[^/]+\.md', p))
    mi_groups = collections.defaultdict(list)
    for p in mi:
        mi_groups['global' if p.startswith('research/mind/') else p.split('/')[1]].append(p)
    body = '<!-- intuition-membership:start -->\n## Current durable intuitions\n'
    for line in ['global'] + sorted(set(mi_groups) - {'global'}):
        body += '\n### ' + ('Global' if line == 'global' else titles[line]) + '\n'
        body += ''.join(f'- [[{p[:-3]}]]\n' for p in mi_groups[line])
    body += '<!-- intuition-membership:end -->'
    new, n = re.subn(r'<!-- intuition-membership:start -->.*?<!-- intuition-membership:end -->', body, ORIGINAL[mi_path].decode(), flags=re.S)
    assert n == 1
    put(mi_path, new)

    redirects = {
        'research/graph/README.md': ('research/graph/atlas/index', 'research/graph/atlas/riemann-atlas'),
        'research/graph/atlas/territories/RA-G1-cyclotomic-ramanujan-divisor-harmonic.md': ('research/prior_art/graph/index', 'research/prior_art/graph/prior-art'),
        'research/graph/atlas/territories/RA-F2-farey-riesz-cycle-criteria.md': ('research/prior_art/graph/index', 'research/prior_art/graph/prior-art'),
        'research/graph/atlas/territories/RA-E1a-instantiated-automorphic-trace.md': ('research/prior_art/graph/index', 'research/prior_art/graph/prior-art'),
    }
    for p, (a, b) in redirects.items():
        assert b + '.md' in TREE
        old = text(p)
        assert a in old
        new = old.replace(a, b)
        if p.endswith('README.md'):
            new = new.replace("that line's `graph/index.md`", "that line's semantically named hub, `research/<line>/graph/<line-name>.md`")
        put(p, new)
    p = 'research/arithmetic_fidelity/graph/relations/stable-fidelity-distance-to-collision.md'
    old = text(p)
    paras = old.split('\n\n')
    removed = [q for q in paras if 'AF-058-near-isometric-renorming-can-destroy-safe-lift-existence' in q]
    assert len(removed) == 1 and removed[0].startswith('[[research/arithmetic_fidelity/findings/AF-058-')
    assert not any(p.startswith('research/arithmetic_fidelity/findings/AF-058-') for p in TREE)
    put(p, '\n\n'.join(q for q in paras if q not in removed))

    # Only these human-reviewed source relations, never automatic similarity links.
    plan = {237: [235, 236], 238: [235, 237], 239: [238], 240: [239, 238], 241: [240], 242: [240],
            243: [240, 241, 242, 238, 239], 244: [243, 238, 237], 245: [243, 244], 246: [236, 243],
            247: [243, 244, 245, 246, 238], 248: [247, 243], 249: [248, 247, 243], 250: [248, 249, 247, 243],
            251: [247, 248, 250], 252: [251, 247]}
    pf = {int(re.match(r'PF-(\d+)', Path(p).name)[1]): p for p in findings['prime_flute']}
    audit = {}
    for src, targets in plan.items():
        p = pf[src]
        original = ORIGINAL[p]
        t = original.decode()
        masks = protected_ranges(t)
        replacements = []
        for dst in targets:
            target = pf[dst]
            alias = f'PF-{dst:03d}'
            assert p != target
            for q in [p, target]:
                assert q[:-3] + '.review.md' not in TREE
            existing = {x.split('|')[0].split('#')[0] for x in re.findall(r'\[\[([^\]\n]+)\]\]', t)}
            if target[:-3] in existing or Path(target).stem in existing:
                continue
            m = next((m for m in re.finditer(r'\b' + re.escape(alias) + r'\b', t) if not any(m.start() < b and m.end() > a for a, b in masks)), None)
            if (src, dst) == (248, 243):
                anchor = t.index('The critical edge therefore does **not** by itself kill PF-243')
                m = re.search(r'\bPF-243\b', t[anchor:])
                assert m is not None
                pos = anchor + m.start()
                m = next(x for x in re.finditer(r'\bPF-243\b', t) if x.start() == pos)
            assert m is not None
            replacements.append((m.start(), m.end(), alias, target[:-3]))
        new, records = apply_wrappers(original, replacements)
        assert len(records) == len(replacements)
        put(p, new)
        audit[p] = {'before_sha': blob_sha(original), 'after_sha': blob_sha(new), 'wrappers': records}
    return changes, audit, retired


def validate(TREE, ORIGINAL, changes, audit, retired):
    post = dict(ORIGINAL)
    for p, data in changes.items():
        assert '/graph/' in p or p in audit, ('path gate', p)
        if data is None:
            post.pop(p)
        else:
            post[p] = data
    paths = set(TREE) - set(retired) | set(post)
    stems = collections.defaultdict(list)
    for p in paths:
        if p.endswith('.md'):
            stems[Path(p).stem].append(p)

    def links(data):
        return re.findall(r'\[\[([^\]\n]+)\]\]', data.decode())

    def resolve(target, source):
        t = urllib.parse.unquote(target).split('|', 1)[0].split('#', 1)[0].strip()
        if not t:
            return source
        for c in [t, t + '.md', str(Path(source).parent / t), str(Path(source).parent / (t + '.md'))]:
            if c in paths:
                return c
        matches = stems[Path(t).stem]
        return matches[0] if len(matches) == 1 else None

    groups = collections.defaultdict(set)
    for p in paths:
        if re.fullmatch(r'research/[^/]+/findings/[^/]+\.md', p) and not p.endswith('.review.md'):
            groups[p.split('/')[1]].add(p)
    for line, expected in groups.items():
        slug = line.replace('_', '-')
        m = f'research/{line}/graph/{slug}-membership.md'
        hub = f'research/{line}/graph/{slug}.md'
        actual = [resolve(t, m) for t in links(post[m]) if '/findings/' in t]
        assert set(actual) == expected and len(actual) == len(expected)
        assert hub in [resolve(t, m) for t in links(post[m])]
        assert [resolve(t, hub) for t in links(post[hub])].count(m) == 1
        assert '<!-- structural-membership:start -->' not in post[hub].decode()
    mi = {p for p in paths if re.fullmatch(r'research/(?:[^/]+/)?mind/intuition/MI-[^/]+\.md', p)}
    m = 'research/graph/intuition-membership.md'
    actual = [resolve(t, m) for t in links(post[m]) if '/MI-' in t]
    assert set(actual) == mi and len(actual) == len(mi)
    pa = {p for p in paths if re.fullmatch(r'research/prior_art/(?:[^/]+\.md|incremental/.+\.md)', p) and Path(p).name not in ('README.md', 'COVERAGE.md')}
    m = 'research/prior_art/graph/prior-art-membership.md'
    assert {resolve(t, m) for t in links(post[m]) if '/graph/' not in t} == pa
    for p, data in post.items():
        if p.endswith('.md') and '/graph/' in p:
            for t in links(data):
                assert resolve(t, p), ('unresolved graph link', p, t)
    for p, record in audit.items():
        assert blob_sha(ORIGINAL[p]) == record['before_sha']
        assert blob_sha(post[p]) == record['after_sha']
        text = post[p].decode()
        for x in reversed(record['wrappers']):
            a, b = x['start'], x['end']
            assert text[a:b] == x['wrapper']
            target = x['wrapper'][2:-2].split('|')[0] + '.md'
            assert target in paths and target != p
            assert p[:-3] + '.review.md' not in paths and target[:-3] + '.review.md' not in paths
            text = text[:a] + x['alias'] + text[b:]
        assert text.encode() == ORIGINAL[p]
    for p in changes:
        if p.startswith('research/graph/atlas/'):
            assert post[p].replace(b'research/prior_art/graph/prior-art|', b'research/prior_art/graph/index|') == ORIGINAL[p]
    assert not any(p.startswith('research/graph/atlas/telemetry/') for p in changes)
    assert '.obsidian/graph.json' not in changes
    return {'research_lines': len(groups), 'canonical_findings': sum(map(len, groups.values())),
            'durable_intuitions': len(mi), 'prior_art_nodes': len(pa), 'changed_files': len(changes),
            'temporary_membership_nodes_removed': len(retired) - 2, 'obsolete_collision_notes_removed': 2,
            'source_files_reference_only': len(audit), 'new_direct_links': sum(len(a['wrappers']) for a in audit.values()),
            'graph_owned_unresolved_wikilinks': 0, 'reference_byte_restoration': 'PASS',
            'canonical_membership': 'PASS', 'atlas_states_and_masses': 'UNCHANGED',
            'telemetry': 'UNCHANGED', 'default_graph_configuration': 'UNCHANGED'}


def run():
    parent = git('rev-parse', 'HEAD', text=True).strip()
    assert git('rev-parse', BASE + '^{tree}', text=True).strip() == BASE_TREE
    baseline_tree = inventory(BASE)
    baseline = {p: git('show', BASE + ':' + p) for p in baseline_tree if p.endswith('.md')}
    baseline_changes, _, _ = derive(baseline_tree, baseline)
    signature = json.dumps({p: None if d is None else blob_sha(d) for p, d in baseline_changes.items()}, sort_keys=True, separators=(',', ':'))
    assert hashlib.sha256(signature.encode()).hexdigest() == EXPECTED_BASE_DELTA, 'Not the locally reviewed migration'
    TREE = inventory(parent)
    changed = set(git('diff', '--name-only', BASE, parent, text=True).splitlines())
    guarded = {p for p in changed if '/graph/' in p or p.startswith('.agents/') or p.startswith('.obsidian/') or re.match(r'research/prime_flute/findings/PF-(23[5-9]|24[0-9]|25[0-2])-', p)}
    assert not guarded, ('changed reviewed inputs', sorted(guarded))
    ORIGINAL = {p: Path(p).read_bytes() for p in TREE if p.endswith('.md')}
    for p, d in ORIGINAL.items():
        assert blob_sha(d) == TREE[p]['sha']
    changes, audit, retired = derive(TREE, ORIGINAL)
    report = validate(TREE, ORIGINAL, changes, audit, retired)
    pattern = re.compile(r'(?<![\w-])(?:' + '|'.join(re.escape(Path(p).stem) for p in sorted(retired, key=lambda p: -len(Path(p).stem))) + r')(?![\w-])')
    scanned = 0
    for p, e in TREE.items():
        if p in retired or e['mode'] not in ('100644', '100755'):
            continue
        data = changes.get(p)
        if data is None:
            data = Path(p).read_bytes()
        try:
            t = data.decode('utf-8')
        except UnicodeDecodeError:
            continue
        if '\0' in t:
            continue
        scanned += 1
        if not pattern.search(t):
            continue
        for n, line in enumerate(t.splitlines(), 1):
            if not pattern.search(line):
                continue
            if p == '.agents/skills/mathia-research-graph-curator/SKILL.md' and '`frontier-membership*`' in line:
                continue
            raise AssertionError(('retired incoming reference', p, n, line))
    for p, data in changes.items():
        if data is not None and p not in TREE:
            assert not pattern.search(data.decode()), p
    report.update({'source_revision': parent, 'reviewed_baseline': BASE, 'text_files_audited': scanned, 'remaining_concrete_retired_references': 0})
    for p, data in changes.items():
        dest = Path(p)
        if data is None:
            dest.unlink()
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
    git('add', '--', *sorted(changes))
    assert set(git('diff', '--cached', '--name-only', text=True).splitlines()) == set(changes)
    git('diff', '--cached', '--check')
    tree = git('write-tree', text=True).strip()
    message = ('research(graph): replace temporal stars with stable research topology\n\n'
               'Replace 25 temporal membership nodes across 13 research lines; remove\n'
               'two obsolete ID-collision projections, and repair stale derived links.\n'
               'Rebuild all canonical finding/intuition memberships from the current tree.\n'
               'Restore 40 explicit Prime Flute reference links in 16 source notes;\n'
               'reversing the approved wrappers preserves every original byte.\n\n'
               'Audit all tracked UTF-8 text for retired references; zero unresolved\n'
               'graph-owned wikilinks. Source claims/status, prior art, graph settings,\n'
               'Atlas states/masses and telemetry are unchanged.\n\n'
               f'Parent: {parent}\n'
               f'Canonical findings: {report["canonical_findings"]}; intuitions: {report["durable_intuitions"]}; prior art: {report["prior_art_nodes"]}.\n'
               'Temporary audit workflow/helper are not part of this commit.\n')
    env = dict(os.environ, GIT_AUTHOR_NAME='github-actions[bot]', GIT_AUTHOR_EMAIL='41898282+github-actions[bot]@users.noreply.github.com', GIT_COMMITTER_NAME='github-actions[bot]', GIT_COMMITTER_EMAIL='41898282+github-actions[bot]@users.noreply.github.com')
    commit = git('commit-tree', tree, '-p', parent, input=message.encode(), env=env).decode().strip()
    assert git('rev-parse', commit + '^', text=True).strip() == parent
    branch = 'codex/graph-topology-candidate-' + os.environ['GITHUB_RUN_ID']
    git('push', 'origin', commit + ':refs/heads/' + branch)
    report.update({'candidate_commit': commit, 'candidate_tree': tree, 'candidate_branch': branch})
    out = Path(os.environ['RUNNER_TEMP']) / 'graph-candidate'
    out.mkdir(exist_ok=True)
    (out / 'validation-report.json').write_text(json.dumps(report, indent=2) + '\n')
    (out / 'changes.json').write_text(json.dumps({p: None if d is None else blob_sha(d) for p, d in changes.items()}, indent=2) + '\n')
    (out / 'wrapper-audit.json').write_text(json.dumps(audit, indent=2) + '\n')
    with zipfile.ZipFile(out / 'changed-files.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for p, data in changes.items():
            if data is not None:
                z.writestr(p, data)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    run()
