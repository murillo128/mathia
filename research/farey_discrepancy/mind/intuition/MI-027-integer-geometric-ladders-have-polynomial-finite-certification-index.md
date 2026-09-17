# MI-027 — Integer separation makes geometric orbit rigidity finitely certifiable

**Evidence level:** exact synthesis from [FD-172](../../findings/FD-172-dyadic-midpoint-rigidity-on-bounded-squarefree-multiplicative-sources.md) through [FD-174](../../findings/FD-174-integer-geometric-midpoint-ladders-have-explicit-finite-scale-certification.md).

FD-173 turns sparse midpoint target-rigidity into a prime-power orbit-hitting condition: every odd prime must place some power inside one observed half-annulus. For a fixed integer geometric ladder `{B^k}`, qualitative irrational-rotation recurrence guarantees eventual hitting but gives no finite source-scale certificate.

FD-174 makes that recurrence effective without importing deep Diophantine approximation. The observed logarithmic window has fixed width `log_B 2`. A Dirichlet pigeonhole step first compresses the recurrence problem to a denominator `q<=Q_B=floor(log_2 B)+1`. Once `q` is bounded in terms of `B`, a very small return would compare two distinct integers `p^q` and `B^m`; their separation by at least one forces a quantitative lower bound on the return distance.

The combination yields an explicit hit

`p^j in (B^k/2,B^k]`

with `j=O_B(p^Q_B)` and `k=O_B(p^Q_B log p)`. Consequently the first

`K_B(X)=O_B(X^Q_B log X)`

geometric midpoint samples certify every prime coordinate through source scale `X`. Uniform midpoint error at those samples gives a uniform prime-defect bound and hence coefficient control on the squarefree prefix.

The reusable mechanism is not merely equidistribution. It is **bounded-denominator recurrence followed by arithmetic separation**: first reduce an infinite recurrence question to finitely many low-denominator comparisons, then use discreteness of the source to prevent arbitrarily fine near-collisions. That turns exact infinite-horizon rigidity into a finite certification theorem.

**Boundary.** The bound is deliberately crude and special to integer geometric bases and the bounded squarefree multiplicative source class. It does not identify the optimal first-hit growth, weaken multiplicativity/nonnegativity, or supply the Franel--Landau destination estimate.