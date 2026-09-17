# AF-399 — Regular variation converts physical locality walls into successor-resource laws

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `REGULAR-VARIATION` · `QUANTITATIVE-SAMPLING` · `LOCAL-TO-GLOBAL` · `RESOURCE-TRANSFER` · `NO-NOVELTY-CLAIM`

## Claim

The successor-depth thresholds in AF-396--AF-398 are not intrinsically prime or PF3 constants. They are the index-space image of a fixed **physical locality wall** under an increasing regularly varying sampling source.

Let `(a_n)_{n\ge1}` be a strictly increasing positive sequence with `a_n\to\infty`, put

\[
e_n=\log a_n,
\]

and for a fixed physical reach `h>0` define

\[
H_N(R)=e_{N+R}-e_N
      =\log\frac{a_{N+R}}{a_N},
\tag{1}
\]

and the exact wall count

\[
B_N(h)
=\max\{R\ge0:H_N(R)\le h\}.
\tag{2}
\]

Equivalently, if

\[
A(x)=\#\{n:a_n\le x\},
\]

then the strict monotonicity of `a_n` gives the exact identity

\[
B_N(h)=A(e^h a_N)-N.
\tag{3}
\]

Assume first that `(a_n)` is regularly varying with index `\rho>0`:

\[
\frac{a_{\lfloor \lambda N\rfloor}}{a_N}
\longrightarrow \lambda^\rho
\qquad(N\to\infty)
\tag{4}
\]

for every `\lambda>0`. Then

\[
\boxed{
\frac{B_N(h)}{N}
\longrightarrow
 e^{h/\rho}-1
}
\tag{5}
\]

for every fixed `h>0`.

Thus a fixed physical wall in logarithmic coordinates becomes an asymptotically linear successor budget. Its leading coefficient depends only on the regular-variation exponent `\rho`; the detailed source density enters only at lower orders.

There is a sharp perturbative refinement. Set

\[
\lambda_*=e^{h/\rho}.
\tag{6}
\]

Suppose there is a positive scale `\varepsilon_N\to0`, with `N\varepsilon_N\to\infty`, and a continuous function `\psi` near `\lambda_*` such that, uniformly for `\lambda` in some fixed neighborhood of `\lambda_*`,

\[
\log\frac{a_{\lfloor\lambda N\rfloor}}{a_N}
=
\rho\log\lambda
+\varepsilon_N\psi(\lambda)
+o(\varepsilon_N).
\tag{7}
\]

Then

\[
\boxed{
B_N(h)
=
(\lambda_*-1)N
-
\frac{\lambda_*\psi(\lambda_*)}{\rho}
N\varepsilon_N
+o(N\varepsilon_N)
}.
\tag{8}
\]

Consequently, whenever an independent downstream theorem has a blind/detect wall at physical reach `h`, the first and second successor-depth scales are inherited from the source's regular-variation law rather than from the downstream detector itself.

More precisely, suppose a sampled discriminator obeys the two implications

\[
H_N(R)\le h
\quad\Longrightarrow\quad
\text{blind},
\tag{9}
\]

and

\[
H_N(R)>h+\Delta_N(R)
\quad\Longrightarrow\quad
\text{detect},
\tag{10}
\]

where `\Delta_N(R)` is a physical mesh/error allowance. If `\Delta_N=o(1)` uniformly on first-order threshold blocks, `(5)` gives the sharp first-order transition. If, in the setting of `(7)`,

\[
\Delta_N=o(\varepsilon_N)
\tag{11}
\]

uniformly on second-order threshold blocks, then for

\[
R_N=(\lambda_*-1)N+cN\varepsilon_N+o(N\varepsilon_N)
\tag{12}
\]

the detector is eventually blind when

\[
c< -\frac{\lambda_*\psi(\lambda_*)}{\rho},
\tag{13}
\]

and eventually detecting when

\[
c> -\frac{\lambda_*\psi(\lambda_*)}{\rho}.
\tag{14}
\]

The durable fidelity principle is therefore:

> **Physical reach is the invariant resource seen by a local discriminator; successor depth is a source-dependent coordinate on that resource.**

Regular variation separates these two layers quantitatively. The index `\rho` determines the leading conversion law, while the slowly varying/source-specific factor determines the correction hierarchy.

## First-order derivation

The Uniform Convergence Theorem for regularly varying functions/sequences upgrades `(4)` to locally uniform convergence in `\lambda` on compact subsets of `(0,\infty)`. Fix `\eta>0` small and write

\[
\lambda_- = \lambda_* - \eta,
\qquad
\lambda_+ = \lambda_* + \eta.
\]

Because

\[
\lambda_-^\rho<e^h<\lambda_+^\rho,
\]

local uniformity gives, for all sufficiently large `N`,

\[
a_{\lfloor\lambda_-N\rfloor}<e^h a_N
<a_{\lfloor\lambda_+N\rfloor}.
\tag{15}
\]

By monotonicity and the definition `(2)`,

\[
\lambda_-N-N+O(1)
\le B_N(h)
\le
\lambda_+N-N+O(1).
\tag{16}
\]

Letting `\eta\downarrow0` proves `(5)`.

Equivalently, the counting function `A` is an asymptotic inverse of the sampling sequence. Classical inversion theory for regular variation says that the inverse of an index-`\rho` regularly varying function has index `1/\rho`; `(5)` is the fixed-multiplicative-level specialization of that fact.

## Second-order transfer

Under `(7)`, first-order regular variation already gives

\[
\frac{N+B_N(h)}{N}\to\lambda_*.
\tag{17}
\]

Write a trial threshold in the form

\[
\lambda_N(t)=\lambda_*+t\varepsilon_N.
\tag{18}
\]

Uniformity in `(7)`, continuity of `\psi`, and Taylor expansion of `\log\lambda` at `\lambda_*` give, uniformly for bounded `t`,

\[
\begin{aligned}
\log\frac{a_{\lfloor\lambda_N(t)N\rfloor}}{a_N}-h
&=
\rho\left(
\log\lambda_N(t)-\log\lambda_*
\right)
+\varepsilon_N\psi(\lambda_N(t))
+o(\varepsilon_N)\\
&=
\varepsilon_N
\left(
\frac{\rho t}{\lambda_*}
+\psi(\lambda_*)
\right)
+o(\varepsilon_N).
\end{aligned}
\tag{19}
\]

Hence the sign changes at

\[
t_*
=-\frac{\lambda_*\psi(\lambda_*)}{\rho}.
\tag{20}
\]

For every fixed `\delta>0`, `(19)` is negative at `t=t_*-\delta` and positive at `t=t_*+\delta` for all sufficiently large `N`. Monotonicity brackets the exact crossing index between those two trial indices. Since `N\varepsilon_N\to\infty`, integer rounding contributes only

\[
O(1)=o(N\varepsilon_N),
\]

and letting `\delta\downarrow0` proves `(8)`.

This derivation is simply an implicit inversion of a second-order regular-variation expansion. No new regular-variation theorem is claimed.

## Detector composition law

The same expansion explains exactly when a physical locality theorem transfers to index depth. For `(12)`, put

\[
\lambda_N
=1+\frac{R_N}{N}
=\lambda_*+c\varepsilon_N+o(\varepsilon_N).
\]

Then `(19)` gives

\[
H_N(R_N)-h
=
\varepsilon_N
\left(
\frac{\rho c}{\lambda_*}
+\psi(\lambda_*)
\right)
+o(\varepsilon_N).
\tag{21}
\]

If `c<t_*`, the right-hand side is eventually negative, so `(9)` applies. If `c>t_*`, it is eventually a positive constant multiple of `\varepsilon_N`; under `(11)` it eventually exceeds the detector allowance `\Delta_N`, so `(10)` applies.

This separates three logically different resources that can otherwise be conflated:

1. the **geometric/discriminator wall** `h`, fixed in the intrinsic coordinate;
2. the **source-density conversion** from physical reach to index breadth, governed by regular variation;
3. the **sampling mesh or detector margin** `\Delta_N`, which decides whether the positive physical excess is actually resolvable.

Only the first belongs to the local detector. The lower-order coefficients in the successor budget can come entirely from the second layer.

## Rational-prime specialization

Take

\[
a_n=p_n,
\qquad
\rho=1.
\]

The prime number theorem gives

\[
p_n=nL(n),
\qquad
L(n)\sim\log n,
\]

so `p_n` is regularly varying of index one. For fixed `\lambda` in a compact neighborhood of `e`, the standard `n`th-prime expansion gives

\[
\log\frac{p_{\lfloor\lambda N\rfloor}}{p_N}
=
\log\lambda
+
\frac{\log\lambda}{\log N}
+o\!\left(\frac1{\log N}\right)
\tag{22}
\]

uniformly there. Thus for the AF-395/AF-397 physical wall `h=1`,

\[
\lambda_*=e,
\qquad
\varepsilon_N=\frac1{\log N},
\qquad
\psi(\lambda)=\log\lambda.
\]

Equation `(8)` becomes

\[
B_N(1)
=
(e-1)N
-e\frac{N}{\log N}
+o\!\left(\frac{N}{\log N}\right),
\tag{23}
\]

which is exactly the second-order wall isolated in AF-397.

The Baker--Harman--Pintz prime-gap input used in AF-380/AF-395/AF-397 gives the corresponding prime-log mesh

\[
\Delta_N
=O(p_N^{-19/40})
=o(1/\log N),
\tag{24}
\]

so the generic detector transfer `(13)`--`(14)` applies at this scale. Writing

\[
R_N=(e-1)N-\alpha\frac{N}{\log N}
\]

means `c=-\alpha`; the threshold `c=-e` is precisely AF-397's split `\alpha=e`.

AF-398 is the next iteration of the same mechanism. Its

\[
+e\frac{N\log\log N}{\log^2N}
\]

term comes from refining the convergence profile in `(22)` one order further. It is therefore a **source-density correction to the representation map**, not a new PF3 constant. Further prime asymptotic terms can continue to refine the successor coordinate without changing the underlying physical locality wall at all.

## Prior-art and novelty audit

N. H. Bingham, C. M. Goldie, and J. L. Teugels, ***Regular Variation***, Cambridge University Press (1987), DOI `10.1017/CBO9780511721434`, is the standard reference for Karamata regular variation, the Uniform Convergence Theorem, asymptotic inversion, de Haan theory, and applications to analytic number theory. The first-order step `(5)` is a direct specialization of this classical theory.

Laurens de Haan and Ulrich Stadtmüller, **“Generalized Regular Variation of Second Order,”** *Journal of the Australian Mathematical Society Series A* **61** (1996), 381--395, develop the standard second-order framework in which an auxiliary scale controls the convergence error of a regularly varying law. The hypothesis `(7)` is deliberately written as the local uniform expansion actually needed here rather than claiming a new version of their general theory.

The rational-prime specialization uses the same classical `n`th-prime asymptotics already audited in AF-397/AF-398 and the same Baker--Harman--Pintz mesh estimate already audited in AF-380.

**No novelty is claimed for regular variation, its inversion theory, second-order regular variation, or the prime asymptotic expansion.** The durable Arithmetic Fidelity contribution is the decomposition `(9)`--`(14)`: it identifies exactly which part of a sampled locality threshold belongs to the downstream discriminator and which part is merely the source-dependent coordinate conversion needed to preserve that discriminator after compression to successor labels.

## Boundaries and falsification

The assumption `\rho>0` is essential to the linear successor law `(5)`. Purely slowly varying sources (`\rho=0`) can require superlinear or otherwise nonmultiplicative index breadth to cross a fixed physical log wall; `(5)` does not cover them.

The wall `h` is fixed. If `h=h_N` moves with `N`, ordinary compact-uniform regular variation may be insufficient and a separate moving-scale theorem is required.

The second-order formula requires the uniform expansion `(7)` and `N\varepsilon_N\to\infty`. Pointwise second-order information alone does not justify inserting a moving `\lambda_N` into the expansion, and if `N\varepsilon_N` stays bounded then integer granularity competes with the claimed correction.

The detector conclusion is conditional on `(9)`--`(10)`. Regular variation converts resources; it does not manufacture a locality theorem. Likewise, second-order detection requires the physical mesh/error allowance to satisfy `(11)`. A detector whose required margin is of the same order as `\varepsilon_N` can shift or blur the index threshold.

The result concerns monotone sampling sequences in logarithmic physical coordinates. A nonmonotone source, a different intrinsic coordinate, or a compression whose discriminator depends on more than physical span can have a different resource law.

No RH consequence is established. In the prime PF3 example the theorem explains the representation cost of reaching an already-known curvature-topology violation; it does not prove any RH-equivalent positivity statement.

## Consequences

AF-396--AF-398 now separate cleanly into a detector theorem and a source theorem. The AF-395 profile supplies a physical PF3 topology wall; prime-log mesh control makes that wall observable; regular variation and its correction hierarchy convert the wall into successor-label breadth.

This prevents future work from over-interpreting coefficients such as `e-1`, `-e`, or the later log-log term as geometry of total positivity. The first coefficient is determined by the regular-variation index and wall position; lower-order coefficients encode convergence of the source-density law.

For Arithmetic Fidelity more generally, this gives a reusable audit rule for compressions that replace a physically meaningful coordinate by rank, index, shell number, refinement depth, or another combinatorial label: **first identify the invariant physical wall, then prove the source-dependent conversion law, and only then interpret a combinatorial threshold.** A threshold that changes under a different source with the same downstream local geometry is representation cost, not discriminator structure.