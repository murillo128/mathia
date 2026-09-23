# AF-514 — Weighted tail transport destroys the curvature provenance margin

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-OBSTRUCTION` · `DIRICHLET-SOURCE` · `WEIGHTED-TAIL-TRANSPORT` · `GLOBAL-RELATIVE-PROFILE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa(s)=\frac{d^2}{ds^2}\log P(s),
\qquad s>1,
\]

be the rational-prime Dirichlet sum and its log-curvature. For a cutoff `A\ge3`, move every prime `p>A` outward to an integer

\[
q_p=p+h_p,
\qquad 0\le h_p\le p,
\]

and assume the `q_p` are pairwise distinct. Keep all primes `p\le A` fixed, and write

\[
R_A
=
\{p\in\mathbb P:p\le A\}
\cup
\{q_p:p\in\mathbb P,\ p>A\}.
\tag{1}
\]

Define the weighted transport budget

\[
B_A
:=
\sum_{p>A}
\frac{h_p(1+\log^2 p)}{p^2}.
\tag{2}
\]

Whenever `B_A\to0` along a family of such controls, the complete relative-curvature profile remains asymptotically indistinguishable from the prime profile:

\[
\boxed{
\sup_{s>1}
\frac{|\kappa_{R_A}(s)-\kappa(s)|}{\kappa(s)}
\le C B_A
}
\tag{3}
\]

for all sufficiently large `A`, with `C` independent of `A` for the declared family. Consequently,

\[
\boxed{
\sup_{s>1}
|\log\kappa_{R_A}(s)-\log\kappa(s)|
\longrightarrow0.
}
\tag{4}
\]

Thus AF-513 is not a peculiarity of a fixed additive shift. The same full-domain curvature topology is blind to a whole weighted class of cofinite tail transports whose individual displacements may vary with the generator and may tend to infinity.

A concrete arithmetic corollary is especially sharp. Fix any `0<\alpha<1` and, for odd primes, put

\[
h_\alpha(p)
=
2\left\lfloor\frac{p^\alpha}{2}\right\rfloor+1,
\qquad
q_p=p+h_\alpha(p).
\tag{5}
\]

For sufficiently large `A`, every `q_p` with `p>A` is an even composite integer, the map `p\mapsto q_p` is strictly increasing, and

\[
h_\alpha(p)\asymp p^\alpha\to\infty.
\]

Nevertheless

\[
B_A
\ll_\alpha
A^{\alpha-1}(1+\log^2 A),
\tag{6}
\]

so

\[
\boxed{
\sup_{s>1}
\frac{|\kappa_{R_A}(s)-\kappa(s)|}{\kappa(s)}
\ll_\alpha
A^{\alpha-1}(1+\log^2 A)
\longrightarrow0.
}
\tag{7}
\]

Hence an entire cofinite prime tail can be replaced by **composite generators at unbounded sublinear distance** while preserving the complete log-curvature profile arbitrarily well in the same global relative topology used by AF-511--AF-513.

## Derivation

Write

\[
P_A(s)=\sum_{q\in R_A}q^{-s},
\qquad
D_A(s)=P_A(s)-P(s),
\qquad
\eta_A(s)=\frac{D_A(s)}{P(s)}.
\tag{8}
\]

Then

\[
P_A=P(1+\eta_A)
\]

and

\[
\kappa_{R_A}-\kappa
=
\frac{d^2}{ds^2}\log(1+\eta_A).
\tag{9}
\]

The proof follows the boundary/right-half-line split of AF-512 and AF-513, but the fixed shift is replaced by the transport budget `(2)`.

### 1. The transport budget controls the first two source derivatives near `s=1`

For `j=0,1,2`, set

\[
f_{j,s}(x)=\partial_s^j x^{-s}=(-\log x)^j x^{-s}.
\]

Fix `0<\delta<1/2`. If `1<s\le1+\delta` and `x\in[p,q_p]\subset[p,2p]`, then

\[
|\partial_x f_{j,s}(x)|
\le
C_{\delta,j}(1+\log^2p)p^{-2}.
\tag{10}
\]

The mean-value theorem therefore gives

\[
|f_{j,s}(q_p)-f_{j,s}(p)|
\le
C_{\delta,j}
\frac{h_p(1+\log^2p)}{p^2}.
\tag{11}
\]

Summing over the transported tail yields the uniform estimate

\[
\boxed{
|D_A^{(j)}(s)|\le C_\delta B_A,
\qquad
1<s\le1+\delta,
\quad j=0,1,2.
}
\tag{12}
\]

No prime-counting theorem enters `(12)`: it is a direct generator-space transport estimate.

### 2. The convergence boundary still dilutes the transported tail

Put `s=1+t`, `L(t)=\log(1/t)`, and `g=\log P`. AF-512 records, after shrinking `\delta` if necessary,

\[
P(1+t)\asymp L(t),
\qquad
|g'(1+t)|\ll\frac1{tL(t)},
\qquad
\kappa(1+t)\asymp\frac1{t^2L(t)}.
\tag{13}
\]

As in AF-513,

\[
\eta_A'
=\frac1P(D_A'-g'D_A)
\tag{14}
\]

and

\[
\eta_A''
=
\frac1P
\left[
D_A''-2g'D_A'
+\big((g')^2-\kappa\big)D_A
\right].
\tag{15}
\]

Substituting `(12)` into the same estimates used in AF-513 gives

\[
\sup_{1<s\le1+\delta}
\frac{|\eta_A''(s)|}{\kappa(s)}
\le C_\delta B_A,
\tag{16}
\]

\[
\sup_{1<s\le1+\delta}
\frac{|\eta_A'(s)|^2}{\kappa(s)}
\le C_\delta B_A^2,
\tag{17}
\]

and `\sup_{1<s\le1+\delta}|\eta_A(s)|\to0` whenever `B_A\to0`.

For sufficiently large `A`, `|\eta_A|\le1/2`, so

\[
\frac{d^2}{ds^2}\log(1+\eta_A)
=
\frac{\eta_A''}{1+\eta_A}
-
\frac{(\eta_A')^2}{(1+\eta_A)^2}
\tag{18}
\]

implies

\[
\boxed{
\sup_{1<s\le1+\delta}
\frac{|\kappa_{R_A}(s)-\kappa(s)|}{\kappa(s)}
\le C_\delta B_A.
}
\tag{19}
\]

Thus the boundary divergence does not price the total amount of tail displacement; it sees only the summable weighted transport cost `(2)`.

### 3. The right half-line is smaller by an additional power of the cutoff

Set `\sigma=1+\delta`. For `s\ge\sigma`, retain the extra factor `p^{-(s-1)}` in `(10)`. Since `p>A`,

\[
|D_A^{(j)}(s)|
\le
C_\sigma(s+1)
B_A A^{-(s-1)},
\qquad j=0,1,2.
\tag{20}
\]

The retained prime prefix contains `2,3`, so `P(s)\ge2^{-s}`. AF-511 supplies the fixed-pair curvature lower envelope

\[
\kappa(s)\ge c_\sigma\left(\frac23\right)^s,
\qquad s\ge\sigma.
\tag{21}
\]

On `[\sigma,\infty)`, `g'` and `\kappa` are bounded. Equations `(14)`--`(15)` and `(20)` therefore imply, up to a fixed polynomial factor in `s`,

\[
|\eta_A^{(j)}(s)|
\le
C_\sigma B_A A
(s+1)\left(\frac2A\right)^s,
\qquad j=0,1,2.
\tag{22}
\]

Combining `(18)`, `(21)`, and `(22)` gives

\[
\frac{|\kappa_{R_A}(s)-\kappa(s)|}{\kappa(s)}
\le
C_\sigma B_A A
(s+1)^2\left(\frac3A\right)^s
	ag{23}
\]

for large `A`; the quadratic term in `B_A` is absorbed once `B_A\le1`. For sufficiently large `A`, the supremum of the right side over `s\ge\sigma` is attained up to a constant at the left endpoint, hence

\[
\boxed{
\sup_{s\ge1+\delta}
\frac{|\kappa_{R_A}(s)-\kappa(s)|}{\kappa(s)}
\le
C_\delta B_A A^{-\delta}.
}
\tag{24}
\]

Together, `(19)` and `(24)` prove `(3)`. Once the relative error is below `1/2`, positivity and `|\log(1+x)|\le2|x|` give `(4)`.

### 4. Sublinear composite transports have vanishing budget

For `(5)`, `h_\alpha(p)` is odd and nondecreasing in `p`. Every transported odd prime therefore lands on an even integer, and `p\mapsto p+h_\alpha(p)` is strictly increasing. Since `\alpha<1`, eventually `h_\alpha(p)\le p`, so the preceding theorem applies.

Moreover,

\[
B_A
\le
C_\alpha
\sum_{n>A}
\frac{n^\alpha(1+\log^2n)}{n^2}
\ll_\alpha
A^{\alpha-1}(1+\log^2 A),
\tag{25}
\]

by integral comparison. This proves `(6)`--`(7)` without using any unproved information about prime gaps or prime density.

## Fidelity and matched-control audit

AF-513 showed that replacing every remote prime by `p+h` for one fixed `h` is invisible in the full relative-curvature topology. The present result identifies the actual sufficient condition behind that example: **weighted generator transport**, not bounded displacement.

The composite family `(5)` preserves the important admissibility properties of the earlier controls:

- it is an ordinary positive-integer, simple, unit-weight source;
- it retains the complete prime prefix below `A`, including the scale anchor `2`;
- every generator in the moved cofinite tail is composite;
- the moved tail is infinite for every cutoff;
- the displacement tends to infinity rather than remaining bounded;
- the full relative-curvature and log-curvature profiles still converge uniformly to the prime profiles.

This removes a natural escape from AF-513: requiring the adversarial tail to drift farther and farther from the primes does not by itself restore a positive provenance margin. The curvature topology discounts a displacement of size `h_p` roughly by `h_p p^{-2}(1+\log^2p)` near its most sensitive boundary.

The comparison is not stronger than AF-513 in every respect. Fixed `h=1` also gives bounded counting-function discrepancy, whereas `(5)` allows an unbounded sublinear displacement. The new conclusion is specifically that **unbounded geometric separation of the tail generators is compatible with vanishing curvature separation**.

As before, this is a stability obstruction rather than an exact collision. AF-509/AF-510 exact injectivity and inversion remain intact; the inverse is simply not uniformly stable for rational-prime provenance in this topology along the declared transport class.

## Representation audit

The tested representation is again

\[
\|Q-\mathbb P\|_{\mathrm{rel}\,\kappa}
=
\sup_{s>1}
\frac{|\kappa_Q(s)-\kappa_{\mathbb P}(s)|}
{\kappa_{\mathbb P}(s)},
\tag{26}
\]

with the associated log-curvature metric. The result does not say that every source representation forgets sublinear tail transport. An atom-indexed pullback metric, arithmetic incidence data, parity, factorization marks, congruence information, or another source-aware observable separates the controls immediately.

The reusable statement is narrower and representation-aware: a natural full-profile compression can be exactly injective while its inverse has zero provenance margin along a quantitatively large support-transport class. The transport budget `(2)` exposes which remote perturbations this particular compression systematically discounts.

## Prior art and novelty assessment

No novelty is claimed for the analytic ingredients. The proof uses the same classical prime-zeta boundary behavior and elementary support-perturbation estimates already audited for AF-511--AF-513. The relevant source anchors recorded there remain the applicable literature basis, including Fröberg's classical prime-zeta analysis and the inverse-Laplace/Prony stability literature.

A focused literature check also finds extensive arithmetic work on shifted primes and generalized/Beurling prime systems. That literature studies arithmetic functions, factorization, counting, zero behavior, or general inverse-transform stability; it does not supply the Mathia-specific claim that the full prime-zeta log-curvature relative topology admits the weighted transport criterion `(2)`--`(3)`. Because `(3)` itself follows by an elementary extension of AF-513, this finding is deliberately classified `NO-NOVELTY-CLAIM`: its value is the stronger obstruction and the explicit composite control family, not a claim of a new general transform theorem.

## Boundaries and failure modes

1. **Outward comparable transport is assumed.** The proof uses `p\le q_p\le2p`. Large inward moves, superlinear moves, collisions, or arbitrary reordering require separate estimates.
2. **The budget is sufficient, not claimed necessary.** Failure of `B_A\to0` does not imply curvature distinguishability.
3. **The topology remains representation-dependent.** Stronger source-aware metrics can price the same transport directly.
4. **No RH consequence follows from the controls alone.** They falsify robust recovery of rational-prime provenance from this curvature carrier; they do not show that the transported source has the same zeta zeros or an RH-equivalent property.
5. **The sublinear exponent is a convenient unconditional family.** The theorem itself is the weighted criterion `(2)`; other displacement laws may also satisfy it.
6. **No exact collision is produced.** The controls approach the prime curvature profile but do not equal it, so AF-509/AF-510 exact recovery is unaffected.

## Consequence for the line

The live frontier moves one level deeper. AF-511 ruled out positive margin against one remote replacement; AF-512 showed that using the full convergence domain does not repair it; AF-513 extended the collapse to a cofinite fixed-shift tail; AF-514 now shows that bounded tail displacement was not the cause.

Any repair based solely on the same unweighted relative-curvature profile must confront the weighted transport class `(2)`. A plausible next discriminator must therefore **price remote generators more strongly or retain arithmetic incidence not visible to this carrier**: for example an atom-indexed/source-pullback topology, a source-scale-adaptive observation, or an independent additive/congruence/factorization relation. Merely moving the observation window toward `s=1`, or demanding that the adversarial tail move an unbounded distance in the original generator coordinate, cannot create a positive rational-prime provenance wall.