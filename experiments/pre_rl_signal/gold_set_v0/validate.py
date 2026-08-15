from __future__ import annotations
import json
from public_fixtures import build_public
from private_truth import build_private

EXPECTED_CONTEXTS={"factual","procedural","structural","sterile","wrong"}

def main() -> None:
    public=build_public(); private=build_private()
    assert public['version']==private['version']=='gold-set-v0'
    situations=public['situations']; answers=private['answers']
    assert len(situations)==20
    ids={s['id'] for s in situations}; assert len(ids)==20
    total=0
    by_id={s['id']:s for s in situations}
    for s in situations:
        sid=s['id']; total += len(s['hidden_tasks'])
        assert set(s['contexts'])==EXPECTED_CONTEXTS
        src=s['shuffled_structural_from']; assert src in ids and src != sid
        assert by_id[src]['cluster'] != s['cluster']
        public_text=json.dumps(s).lower()
        assert 'ground_truth' not in public_text and 'correct_answer' not in public_text
        assert {t['id'] for t in s['hidden_tasks']} == set(answers[sid])
    assert total==80
    print('validated 20 situations / 80 hidden tasks')

if __name__=='__main__': main()
