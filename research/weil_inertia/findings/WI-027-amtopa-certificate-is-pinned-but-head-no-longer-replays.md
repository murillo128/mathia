# WI-027 — AMTOPA's `0.6734164909` certificate is publicly pinned, but current HEAD no longer replays it

**Status:** `PRIOR-ART-AUDIT + COMPUTATIONAL-CERTIFICATE + NEEDS-INDEPENDENT-REPLAY`. AMTOPA's public `zeta-exact-pressure` repository contains a genuine historical computer-assisted certificate trace for its research-draft candidate

\[
\frac{N_0^s(T,2T)}{N(T,2T)}\gtrsim 0.6734164909,
\]

including a successful GitHub Actions run at the exact source commit recorded by the candidate, freshly generated interval tables, a successful hardened branch-and-bound at the advertised target, and a content-addressed uploaded artifact. This is materially stronger evidence than an unsupported numerical headline. It is **not**, however, an independently reproduced theorem: the repository itself labels the result a research-draft candidate and records `independent_reproduction: false`; the current repository tip cannot replay the local certificate because a later fail-closed rewrite disables the convexity/tangent accelerator. The current-HEAD failure does not refute the historical certificate, because the successful run is pinned to the earlier code and the earlier convexity lower-bound construction is mathematically monotone in the required direction. The correct Mathia state is therefore **historical computational certificate requiring independent replay and analytic-bridge audit**, not `ESTABLISHED`, but also not `REFUTED`.

## 1. Exact primary claim and provenance

The primary repository `AMTOPA/zeta-exact-pressure` describes its headline as a **"current interval-certified research-draft record"**, explicitly says that it is not a peer-reviewed theorem, and gives the exact-pressure inputs

\[
B=\frac{93}{23000},
\qquad
F(g_1,\ldots,g_6)\ge \frac{79107}{10^7},
\]

for a seven-point/six-gap local functional built from a 17-term analytic window. Its conservative scalar-Gram assembly chooses `m=145` and records

\[
\boxed{0.67341649097149929495003553310749\ldots},
\]

with advertised safe floor

\[
\boxed{0.6734164909}.
\tag{1}
\]

The root `candidate.json`, dated 2026-08-12, pins the local certificate to

```text
source_commit = b3b7784ed0089c3c2197d740aaae1a424d142e44
workflow_run_id = 31610179703
artifact_id = 9147378469
artifact_digest_sha256 = 871532c739d5a9e8de770cf00675381ea4fd9c81f212d8e46f86403a27a34dc1
```

and records `independent_reproduction: false`.

This provenance can be checked against GitHub itself. Actions run `31610179703`, started 2026-08-12 15:03 UTC, checked out exactly `b3b7784ed0089c3c2197d740aaae1a424d142e44`, regenerated the full interval tables at grid `4000` and precision `50`, and produced the six SHA-256 streams recorded in the candidate. The decisive verifier output in the public job log is

```text
target=0.0079106999999999997 table_cells=64954 required_cells=64922
initial_boxes=64 accelerated=true components=2,2,2,2,2,2
VERIFIED=true nodes=3768186 pruned=1884125 splits=1884061
convex=2030240 tangent=936616 max_depth=74
```

The workflow then uploaded an eight-file artifact whose GitHub-computed digest is exactly the digest stored in `candidate.json`. Thus there is a concrete public execution trace tying the claimed finite inequality to a particular source revision and table set; it is not merely a copied status flag.

## 2. Independent audit: all tables replay, current HEAD does not

A later independent audit in `teal-sea/zeta-lab`, `hunts/amtopa_ceiling/`, pinned AMTOPA's then-current tip at

```text
7253fdcab9366af45b8c8caf44e408c0af44a1a7
```

and rebuilt the six interval tables. Its recorded hashes match AMTOPA's `candidate.json` byte for byte. However, running the **current-tip** verifier on those tables reaches a terminal grid cell with

```text
lower = 0.0079105811209911128
```

against target `0.0079107`, a deficit of about

\[
1.18879\times10^{-7},
\]

and reports `convex=0`, so the tangent pruner never runs. The audit therefore correctly states that a reviewer cloning the repository at the current tip obtains `INCONCLUSIVE`, not `VERIFIED`.

This is a reproducibility defect in the current repository state, but it must not be conflated with a falsification of the historical certificate. The primary candidate is explicitly pinned to the earlier source commit, and the public Actions log confirms that the earlier code did return `VERIFIED` on freshly generated tables.

## 3. The HEAD regression is fail-closed, not a discovered false acceptance

The code difference explains the discrepancy. At the successful source commit `b3b7784`, the Hessian lower-bound contribution of a pair with exact nonnegative coefficient `p` and a lower bound `s` for the kernel second derivative is inserted as the **thin** interval

```cpp
const double scalar = s >= 0
    ? down(p.lower * s)
    : down(p.upper * s);
const Interval term = point(static_cast<long double>(scalar));
```

and the resulting lower-bound Hessian is checked by interval LDL.

At tip `7253fdca`, the same step was changed to

```cpp
const Interval curvature = mul(
    p.exact,
    {static_cast<long double>(sec),
     std::numeric_limits<long double>::infinity()});
```

before the same style of interval LDL test. The lower endpoint is still a valid curvature lower bound, but the new `+infinity` upper endpoints make the interval matrix so wide that Schur-complement subtraction can drive later pivot lower endpoints to `-infinity`; the positive-definite gate consequently ceases to certify boxes that the earlier lower-matrix test could certify.

The earlier thin construction is sound for the intended implication. Each pair contributes a scalar multiple of the all-ones block `J_[i,j)` on its covered gaps, and

\[
J_{[i,j)}\succeq0.
\]

If `c_p(g)>=\underline c_p` throughout a box, then

\[
\sum_p c_p(g)J_p
\succeq
\sum_p \underline c_p J_p.
\tag{2}
\]

Therefore positive definiteness of the rounded-down scalar lower matrix on the right is sufficient for convexity of the true Hessian. The later change is conservative in the acceptance direction: it can turn a previously certifiable box into `INCONCLUSIVE`, but this code inspection provides no mechanism by which it would expose a false positive from the earlier lower-matrix argument.

This agrees with `zeta-lab`'s adversarial diagnosis: the regression is **fail-closed**. Their current-tip failure is evidence against *present-day replayability*, not evidence that (1) is numerically false.

## 4. What is and is not established

The evidence tiers should be kept separate.

**Primary computational evidence.** The exact historical source revision, workflow run, generated-table hashes, verifier statistics, artifact ID and artifact digest are public and mutually consistent. This supports the statement that AMTOPA did run the advertised finite certificate successfully on 2026-08-12 at the pinned code revision.

**Independent partial reproduction.** `teal-sea/zeta-lab` independently regenerated all six interval tables and obtained the same byte streams, and it independently diagnosed the later verifier regression. It did **not** convert the AMTOPA headline into an independently reproduced theorem; its public state explicitly treats figures above the internally Lean-proved four-point result as certificate-dependent claims.

**Remaining gates.** The primary `candidate.json` itself says `independent_reproduction: false`. A durable promotion would require at least (i) an independent end-to-end replay at the pinned historical commit or an equivalent corrected verifier, and (ii) an independent audit of the analytic bridge that transports the finite local inequality, the custom window constant, and exact pressure ledger into the asymptotic zeta-zero proportion. Neither gate is supplied merely by the successful original Actions run.

Accordingly Mathia must not cite `0.6734164909` as an established unconditional theorem. Conversely, it should not classify the number as refuted solely because AMTOPA's later HEAD cannot reproduce the old run.

## 5. Relevance to `weil_inertia`

If its remaining gates survive audit, AMTOPA is directly relevant to the support-one program pursued here: it changes the admissible analytic window and local pressure geometry rather than asking for support greater than one or new prime-side moments. Its claimed `0.6734164909` is well above Mathia's presently established four-point improvements but still below the certified period-33 obstruction `0.67361` of WI-019 for the deliberately narrower **single-profile Montgomery--Taylor collapsed interface**. There is therefore no contradiction with WI-019: AMTOPA is not using that exact fixed Montgomery--Taylor profile.

The practical redirection is precise. Before investing research effort in numerically overtaking `0.6734164909`, the higher-value prior-art task is to decide whether this existing candidate closes end to end:

1. replay the `b3b7784` certificate independently from freshly generated tables and compare hashes/output;
2. audit the exact-pressure global assembly and multiplicity bookkeeping against the Alpöge--Furman/Gram-defect contracts already reconstructed in WI-009--WI-026;
3. only if those pass should `0.6734164909` become the benchmark that new support-one improvements must beat.

## 6. Prior-art and novelty assessment

No mathematical novelty is claimed for the AMTOPA construction or for the `zeta-lab` audit. This finding is a provenance/evidence audit of a very recent public research claim. The additional Mathia contribution is the evidence classification above: the public historical Actions trace materially strengthens the candidate relative to an unaudited headline, while the current-tip failure is a conservative replay regression and therefore does not by itself invalidate the pinned certificate.

**Primary sources:**

- `AMTOPA/zeta-exact-pressure`, `README.md`, `candidate.json`, source commit `b3b7784ed0089c3c2197d740aaae1a424d142e44`, GitHub Actions run `31610179703`, 12 Aug 2026.
- `AMTOPA/zeta-exact-pressure`, tip `7253fdcab9366af45b8c8caf44e408c0af44a1a7`, `src/verify_local_tables.cpp`.
- `teal-sea/zeta-lab`, `hunts/amtopa_ceiling/RESULTS.md`, independent table/current-tip reproducibility audit, current public revision inspected 30 Aug 2026.

## 7. Decisive promotion/falsification test

The next evidence-changing test is **not** another floating optimization. Check out exactly `b3b7784ed0089c3c2197d740aaae1a424d142e44` in an independent environment, regenerate the full six tables, verify all six hashes, compile the historical hardened verifier with `-ffp-contract=off`, and demand

```text
VERIFIED=true
nodes=3768186
convex=2030240
tangent=936616
```

at target `79107/10000000`, or an independently justified equivalent certificate. A mismatch would materially downgrade the candidate. A matching independent replay would close the finite-computation gate but would still leave the analytic bridge for separate audit before theorem-level promotion.