# PC-083 — cyclically separated Hardy traces converge without Abel regularization

**Status:** `EXACT-DERIVED` + `NOVELTY-CORRECTION` + `PRIOR-ART-REDIRECTION`. This finding corrects one convergence/novelty interpretation in PC-082 while leaving its exact higher-trace formulas and its proof that higher relative Hardy data exceed pairwise resultants intact. No theorem-level historical novelty is claimed.

PC-082 represented cyclically separated root-channel traces by a radial/Abel limit and described that prescription as essential because the corresponding critical cone series is not absolutely convergent. The absolute-convergence statement is correct, but the stronger conclusion is not: **for every cyclically separated root word, the natural finite Hardy sections already converge ordinarily to the same trace.** Abel damping is therefore a convenient summability proof and an order-safe representation, not a necessary renormalization of this sector.

More precisely, let

\[
(\mathcal H_\alpha)_{jk}
=\frac{\alpha^{j+k+1}}{j+k+1},
\qquad j,k\ge0,
\qquad |\alpha|=1,
\]

and take roots `alpha_1,...,alpha_k` with cyclic indices and

\[
\boxed{\alpha_i\alpha_{i+1}\neq1\quad\text{for every }i.}
\]

If `P_N` denotes the orthogonal projection onto `span{e_0,...,e_N}`, then

\[
\boxed{
\lim_{N\to\infty}
\operatorname{Tr}
\bigl(P_N\mathcal H_{\alpha_1}P_N\cdots
      P_N\mathcal H_{\alpha_k}P_N\bigr)
=
\operatorname{Tr}
\bigl(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k}\bigr).
}
\]

The common value is exactly the PC-082 cube period

\[
\boxed{
\left(\prod_{i=1}^k\alpha_i\right)
\int_{[0,1]^k}
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-\alpha_i\alpha_{i+1}x_ix_{i+1}}.
}
\]

The associated multiple series remains **conditionally** rather than absolutely convergent. The correction is therefore not that the criticality disappears; it is that the cyclotomic oscillation supplied intrinsically by distinct primitive roots is already sufficient to define the trace by ordinary operator finite sections.

## 1. Exact finite-section formula

Write cyclic indices modulo `k` and set

\[
A=\prod_{i=1}^k\alpha_i,
\qquad
\delta_i=\alpha_{i-1}\alpha_i.
\]

The cyclic-separation hypothesis is exactly

\[
\boxed{\delta_i\neq1\quad\text{for every }i.}
\]

Expanding the trace of the finite compressed word gives

\[
S_N
:=
\operatorname{Tr}
\bigl(P_N\mathcal H_{\alpha_1}P_N\cdots
      P_N\mathcal H_{\alpha_k}P_N\bigr)
=
\sum_{0\le j_1,\ldots,j_k\le N}
\prod_{i=1}^k
\frac{\alpha_i^{j_i+j_{i+1}+1}}
{j_i+j_{i+1}+1}.
\]

Every `j_i` occurs once with `alpha_{i-1}` and once with `alpha_i`, so

\[
\prod_{i=1}^k\alpha_i^{j_i+j_{i+1}+1}
=
A\prod_{i=1}^k\delta_i^{j_i}.
\]

Using

\[
\frac1{j_i+j_{i+1}+1}
=
\int_0^1x_i^{j_i+j_{i+1}}\,dx_i
\]

and noting that `j_i` occurs in the factors `x_{i-1}` and `x_i`, the finite sum factorizes exactly:

\[
\boxed{
S_N
=
A\int_{[0,1]^k}
\prod_{i=1}^k
\left(
\sum_{j=0}^N
(\delta_i x_{i-1}x_i)^j
\right)
\,dx_1\cdots dx_k.
}
\]

Equivalently,

\[
\boxed{
S_N
=
A\int_{[0,1]^k}
\prod_{i=1}^k
\frac{1-(\delta_i x_{i-1}x_i)^{N+1}}
{1-\delta_i x_{i-1}x_i}
\,dx_1\cdots dx_k.
}
\]

Thus the ordinary finite-section approximation has an exact elementary integral formula; no radial parameter has been introduced.

## 2. Cyclic separation gives a uniform Dirichlet bound

For a fixed unit complex number `delta != 1`, define

\[
c_\delta
=
\min_{0\le t\le1}|1-\delta t|.
\]

Because the compact radial segment `{delta t:0<=t<=1}` does not contain `1`,

\[
\boxed{c_\delta>0.}
\]

Hence every partial geometric sum satisfies the uniform bound

\[
\left|
\sum_{j=0}^N(\delta t)^j
\right|
=
\left|
\frac{1-(\delta t)^{N+1}}{1-\delta t}
\right|
\le
\frac2{c_\delta},
\qquad 0\le t\le1,
\]

independently of `N`.

For almost every point of `[0,1]^k`, each product `x_{i-1}x_i` is strictly smaller than `1`. Therefore

\[
(\delta_i x_{i-1}x_i)^{N+1}\longrightarrow0
\]

for every `i` outside a measure-zero union of boundary faces. The integrand in the exact finite-section formula is bounded by the integrable constant

\[
\prod_{i=1}^k\frac2{c_{\delta_i}}.
\]

Dominated convergence now gives

\[
\boxed{
\lim_{N\to\infty}S_N
=
A\int_{[0,1]^k}
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-\delta_i x_{i-1}x_i}.
}
\]

Relabeling `i` converts `delta_i=alpha_{i-1}alpha_i` into the PC-082 form `alpha_i alpha_{i+1}`. PC-082 independently proved that the same integral is the ordinary trace of the boundary operator product. Hence the finite-section limit equals the trace.

The proof works without change for rectangular cutoffs `0<=j_i<=N_i` with every `N_i -> infinity`: each coordinate contributes its own uniformly bounded finite geometric sum. Thus the root-channel series has genuine Pringsheim/rectangular convergence, not merely Abel summability.

## 3. The shell-level cyclic traces inherit ordinary convergence

Recall

\[
\Gamma_n
=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha.
\]

If shell orders `n_1,...,n_k` are cyclically adjacent and distinct, then for every root choice

\[
\alpha_i\in P_{n_i}^*
\]

we have `alpha_i alpha_{i+1} != 1`: equality would imply `alpha_{i+1}=alpha_i^{-1}`, forcing the two roots to have the same exact order.

There are only finitely many primitive roots in each shell, so the root-channel limit may be summed term by term. Consequently

\[
\boxed{
\lim_{N\to\infty}
\operatorname{Tr}
\bigl(P_N\Gamma_{n_1}P_N\cdots
      P_N\Gamma_{n_k}P_N\bigr)
=
\operatorname{Tr}
\bigl(\Gamma_{n_1}\cdots\Gamma_{n_k}\bigr)
}
\]

for every cyclically separated shell word covered by Sections 2--4 of PC-082.

This is an intrinsic operator cutoff: `P_N` is simply the first `N+1` Hardy modes. The higher trace therefore does not depend for its existence on choosing an external radial regularizer.

## 4. Criticality survives: the convergence is not absolute

For a fixed root word, the absolute value of each series term is

\[
\prod_{i=1}^k\frac1{j_i+j_{i+1}+1}.
\]

On the dyadic block

\[
R\le j_i<2R
\qquad\text{for every }i,
\]

there are `R^k` lattice points and every denominator factor is at most `4R+1`. Hence the absolute mass of each such block is bounded below by a positive constant independent of `R`:

\[
\sum_{R\le j_i<2R}
\prod_{i=1}^k\frac1{j_i+j_{i+1}+1}
\ge
\frac{R^k}{(4R+1)^k}.
\]

Taking disjoint dyadic blocks proves

\[
\boxed{
\sum_{j_1,\ldots,j_k\ge0}
\left|
\prod_{i=1}^k
\frac{\alpha_i^{j_i+j_{i+1}+1}}
{j_i+j_{i+1}+1}
\right|
=\infty.
}
\]

Thus PC-082 was correct to identify the cycle sums as sitting at critical homogeneity. What changes is the role of the root-of-unity characters: because **every coordinate character is nontrivial under cyclic separation**, their bounded geometric partial sums already provide enough multidimensional Dirichlet cancellation for ordinary rectangular convergence.

## 5. Abel damping agrees with, rather than defines, the separated trace

PC-082 used

\[
\mathcal H_{\alpha,r}=rR_r\mathcal H_\alpha R_r,
\qquad 0<r<1,
\]

and proved that radial traces converge to the boundary operator trace as `r -> 1^-`. The present result shows that, in the cyclically separated sector,

\[
\boxed{
\text{finite Hardy sections}
\;=\;\text{ordinary conditional sum}
\;=\;\text{PC-082 cube integral}
\;=\;\text{Abel boundary value}
\;=\;\text{operator trace}.
}
\]

So the word `Abel` should be read there as a safe summation convention, not as evidence of a new renormalized arithmetic object.

For the `k=3` triangle-cone coordinates of PC-082, this distinction matters. The linear change from `(i,j,k)` to `(r,s,t)` sends a Hardy box cutoff to a particular expanding polytope in the strict triangle cone. Because the transformed series is not absolutely convergent, an unspecified reordering of triangle lattice points need not be equivalent. The **operator finite-section ordering** is canonical and convergent; arbitrary cone reorderings remain unjustified.

## 6. Pairwise control recovers PC-080 without radial limits

At `k=2`, let `delta=alpha beta != 1`. The theorem gives directly

\[
\lim_{N\to\infty}
\operatorname{Tr}
(P_N\mathcal H_\alpha P_N\mathcal H_\beta P_N)
=
\delta\int_0^1\int_0^1
\frac{dx\,dy}{(1-\delta xy)^2}.
\]

The elementary integral is

\[
-\operatorname{Log}(1-\delta),
\]

which is exactly the root-channel trace used in PC-080. Summing complete primitive shells therefore recovers

\[
\operatorname{Tr}(\Gamma_m\Gamma_n)
=-\log|\operatorname{Res}(\Phi_m,\Phi_n)|
\]

for `m != n` by direct finite Hardy sections as well. This is a consistency check on normalization and on the finite-section proof.

## 7. Prior-art and novelty correction

The correction moves the novelty boundary but does not prove a full classical reduction.

1. Terasoma's 2004 rational-cone theorem, already anchored in `SOURCES.md`, assumes **absolute convergence** for the general cyclotomic conical zeta value that it reduces to the cyclotomic multiple-zeta span. The present critical series fails that hypothesis, so PC-082 was right not to invoke Terasoma's reduction theorem directly.
2. At the same time, cyclotomic multiple-zeta theory itself classically allows boundary exponent `1` when a terminal root-of-unity character is nontrivial. The bounded-geometric-sum mechanism above is the multidimensional analogue of that familiar Dirichlet cancellation. Thus conditional convergence generated by nontrivial cyclotomic characters is not, by itself, a novel phenomenon.
3. Guo--Paycha--Zhang's conical-zeta and renormalized-conical-zeta frameworks remain close prior art, but **renormalization is not required merely to define the cyclically separated Hardy traces**. Any comparison with their renormalized values should therefore be posed only after a specific cone reordering or singular character degeneration is introduced.
4. A targeted novelty search around cyclotomic conical zeta values, conditional root-of-unity character sums, and conical regularization found the established frameworks above but no authoritative source stating this exact finite-Hardy-section identity. Absence of that specialization is not treated as historical novelty.

Accordingly, PC-082's robust new internal content remains that higher trace-class Hardy interactions carry more information than pairwise resultants. The part that must be downgraded is the suggestion that the cyclically separated values owe their existence to a special Hardy Abel **regularization**.

## 8. Boundary: repeated-shell words are not covered

The hypothesis `delta_i != 1` for every coordinate is sharp for this proof. If a cyclic word has adjacent roots with

\[
\alpha_{i-1}\alpha_i=1,
\]

then

\[
\sum_{j=0}^N(\alpha_{i-1}\alpha_i t)^j
=
\sum_{j=0}^N t^j
\]

has no uniform bound as `t -> 1`. Dominated convergence fails at exactly the Hilbert singular channel.

This is relevant to PC-082's control

\[
\operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)>0.
\]

That repeated-shell word was explicitly outside the cyclic root-separation formula because the wrap-around `3 -> 3` can contain reciprocal primitive roots. The present result does **not** classicalize or give ordinary multiple-series convergence for that larger repeated-shell sector. Operator trace-class arguments may still define such traces even when some individual root-channel expansions require a stronger summation prescription.

Thus the surviving relative Hardy frontier splits cleanly:

\[
\boxed{
\begin{array}{ll}
\text{cyclically separated root/shell words}
&\to\text{ordinary conditionally convergent cone periods},\\[3pt]
\text{words with reciprocal same-shell channels}
&\to\text{possible genuine boundary/regularization issue}.
\end{array}}
\]

## 9. RH relevance

This correction does not create a new bridge to the Riemann zeros. It removes one possible source of apparent special structure. For cyclically separated finite words, the Hardy regulator is not supplying an intrinsic complex spectral parameter, a functional equation, a gamma factor, or a critical-line symmetry; it is merely one method of reaching a conditionally convergent value already selected by finite Hardy sections.

The next meaningful novelty question for this branch is therefore narrower than the one stated at the end of PC-082: determine whether these **ordinary conditionally convergent cyclotomic cone periods**, with their operator-induced ordering, reduce by legitimate cone subdivision/iterated-integral identities to established cyclotomic multiple-polylogarithm values. Only the reciprocal-channel/repeated-shell sector still has a genuine regularization issue at finite trace order.

An infinite-shell or cross-level deformation would still need to derive its analytic parameter from Prime-Circle geometry rather than inserting exponents by hand.

## Falsification surface

The correction has six direct audit points.

1. In the finite trace expansion, `j_i` must carry the phase `delta_i^{j_i}` with `delta_i=alpha_{i-1}alpha_i`.
2. Cyclic separation must imply `delta_i != 1` for every coordinate.
3. The integral identity must factor the finite rectangular sum into the product of finite geometric sums shown above.
4. For every nontrivial unit `delta`, `min_{0<=t<=1}|1-delta t|` must be strictly positive, giving an `N`-independent bound.
5. Dominated convergence must reproduce exactly the PC-082 cube period and hence its already-established operator trace.
6. Absolute convergence must still fail on dyadic boxes, so the result may not be upgraded to an order-independent absolutely convergent conical zeta value.

Failure of points 1--5 invalidates the ordinary-convergence theorem. Failure of point 6 would alter the prior-art classification but not the finite-section limit itself.

## Research consequence

PC-082 should now be read with one precise correction:

\[
\boxed{
\text{for cyclically separated Hardy words, Abel summation is sufficient but not necessary.}
}
\]

Their higher traces are canonical **ordinary conditional finite-section limits**. The higher relative sector still exceeds pairwise cyclotomic resultants, but its separated part is closer to classical cyclotomic Dirichlet/conical summation than PC-082's regularization language suggested.