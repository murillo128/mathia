# MI-060 — Cube-poorness does not certify Hilbert fidelity

**Evidence level:** supported classical-structure synthesis from [AF-465](../../findings/AF-465-uniform-doubling-is-not-a-hilbert-fidelity-certificate.md), read against the sufficient Hamming-cube obstruction AF-464. The Laakso/doubling and snowflake-embedding ingredients are classical; no claim is made that an arithmetic source is Laakso-like.

AF-464 gives a negative witness: if a source family contains growing Hamming cubes with uniformly controlled source distortion, then a fixed upper-Lipschitz budget cannot give complexity-uniform bi-Lipschitz recovery into Hilbert. AF-465 shows that the converse diagnostic is false.

There are finite weighted Laakso graphs `(L_n,d_n)` with one uniform doubling bound and hence no Hamming cubes of unbounded dimension with one common distortion bound, but

`sup_n c_2(L_n) = infinity`.

Thus **removing the AF-464 cube witness removes only that proof of failure; it does not supply a positive Hilbert-fidelity certificate**. A physical arithmetic source that needs pairwise recovery in Hilbert must satisfy a positive quantitative statement in the metric actually consumed downstream—for example a uniform bi-Lipschitz embedding/recovery bound, or another invariant whose hypotheses genuinely imply such a bound for the declared target. “Thin”, “doubling”, or “cube-poor” alone is insufficient.

The source metric is load-bearing. For a fixed doubling bound and fixed `epsilon in (0,1/2)`, Assouad/Naor--Neiman gives uniform finite-dimensional Euclidean embeddability after snowflaking `d -> d^(1-epsilon)`. This is a real escape from the original Hilbert obstruction only after changing the quantitative notion of source separation, so the downstream argument must justify that metric replacement rather than silently inherit fidelity in `d`.

**Boundary.** AF-465 does not say every uniformly doubling family has bad Hilbert distortion, does not place Laakso geometry inside a prime-derived source, and does not classify all non-Hilbert obstructions. The conclusion is target- and metric-relative; type-1/non-superreflexive targets can behave differently.