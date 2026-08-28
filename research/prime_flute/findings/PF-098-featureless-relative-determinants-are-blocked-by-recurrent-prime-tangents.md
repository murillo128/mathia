# PF-098 — recurrent prime tangents block standard relative determinants against featureless controls

**Status:** `DECISIVE-NEGATIVE` for the standard Müller/Borthwick--Judge--Perry relative-zeta route when the reference flute is a smooth/density-matched control whose geometry at infinity omits recurrent prime tangents; `EXACT-GEOMETRIC + OPERATOR-THEORETIC`.

## Claim

A natural response to the failure of the absolute Selberg/Laplacian determinant is to compare the prime-flute with a featureless reference surface: for example the exact orthogonal-circle flute obtained from a smooth prime-number-theorem sampling sequence `q_n` with

\[
q_n\sim p_n,
\qquad
\frac{q_{n+1}-q_n}{q_n-q_{n-1}}\to1,
\]

or the simpler integer control used in PF-088.

This does **not** produce a standard relative determinant. The obstruction is stronger than divergence of a particular Euler product: the two Laplacians are not a trace-class perturbation in the relative heat sense required by the classical relative-zeta formalism.

More generally, let `X_0` be any marked control flute whose pointed geometric limit set at infinity omits one recurrent isolated prime tangent `Y_H` supplied by PF-034/PF-046. Then there exists `t_0>0` such that, after the canonical pants marking identifies the two `L^2` spaces,

\[
\boxed{
 e^{-t_0\Delta_{X_{\rm prime}}}
 -Ue^{-t_0\Delta_{X_0}}U^{-1}
 \notin \mathcal S_1.
}
\]

Consequently the standard relative heat trace

\[
\operatorname{Tr}
\left(e^{-t\Delta_{X_{\rm prime}}}
-Ue^{-t\Delta_{X_0}}U^{-1}\right)
\]

is not available for all `t>0`, and the usual relative zeta/determinant construction cannot be applied to this pair.

The mathematical mechanism is a **tangent-hull mismatch at infinity**: a local spectral defect that recurs infinitely often with nonvanishing size cannot become trace class merely because the occurrences have zero density.

## 1. The distinguished cuffs already show an order-one mismatch at infinitely many escaping blocks

PF-046 gives, for every sufficiently large prescribed `B`, a fixed finite prime pattern

\[
H_B=\{\eta_1<\cdots<\eta_r\}
\]

which occurs infinitely often as an isolated block of consecutive primes. For its first two internal gaps

\[
d_1=\eta_2-\eta_1,
\qquad
d_2=\eta_3-\eta_2,
\]

one may force

\[
\boxed{
\frac{d_1}{d_2}<\frac1{B-1}.
}
\]

At an occurrence near prime scale `P`, the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

hence

\[
\boxed{
\ell_1(P)-\ell_2(P)
\longrightarrow
2\log\frac{d_2}{d_1}
>2\log(B-1).
}
\tag{1}
\]

The same exact orthogonal-circle block has the canonical short separator

\[
\boxed{
\sinh^2\frac{L_B}{4}=\frac{d_1}{d_2},
\qquad
L_B\to0\quad(B\to\infty).
}
\tag{2}
\]

Thus the extreme cuff contrast is not merely an arithmetic label. It survives as a genuine primitive hyperbolic length in the pointed tangent `Y_{H_B}`.

Now compare this with a density-matched smooth control `q_n` whose consecutive spacings are locally regular. For every fixed window,

\[
\frac{q_{n+k+1}-q_{n+k}}{q_{n+1}-q_n}\to1.
\]

After the same affine/Möbius normalization used to take prime tangents, the control windows therefore converge to the regular equal-spacing orthogonal-circle model. Its relevant local cross-ratios stay in a compact subset of `(0,\infty)`, so the corresponding primitive separator lengths are bounded away from zero.

Choosing `B` sufficiently large gives

\[
\boxed{
L_B<\frac12\,\operatorname{syst}_{\rm loc}(Y_0),
}
\tag{3}
\]

where `Y_0` denotes the regular pointed control model and `syst_loc` means the shortest primitive closed geodesic visible in the fixed marked core under consideration.

The mismatch in (1)--(3) occurs at **infinitely many disjoint locations escaping to infinity** in the same prime-flute.

## 2. A local heat observable distinguishes the two pointed limits

Let `K` be a compact core of `Y_{H_B}` containing the short separator from (2), and choose a smooth cutoff

\[
0\le\chi\le1
\]

supported in a slightly larger core. PF-064/PF-094 provide exactly the locality needed here: along isolated occurrences `P_m`, the exterior collars diverge, finite propagation gives convergence of the localized wave kernels to the tangent wave kernel, and the primitive singularity at time `L_B` survives.

For the smooth control, the corresponding marked cores converge instead to `Y_0`. By (3), its localized wave trace has no primitive singularity at `L_B`.

Therefore the two localized spectral measures cannot be equal. Equivalently, their Laplace transforms cannot agree for every positive time. Hence there exists

\[
t_0>0
\]

such that

\[
\boxed{
 a_H(t_0)
 :=\operatorname{Tr}\bigl(\chi e^{-t_0\Delta_{Y_{H_B}}}\chi\bigr)
 \ne
 a_0(t_0)
 :=\operatorname{Tr}\bigl(\chi_0 e^{-t_0\Delta_{Y_0}}\chi_0\bigr).
}
\tag{4}
\]

This implication uses no global trace formula. Equality of the localized heat traces for every `t>0` would imply equality of the corresponding localized spectral measures by uniqueness of the Laplace transform; their cosine transforms would then give identical localized wave distributions, contradicting the short primitive orbit present only on the prime tangent.

Let `\chi_m` be the transplanted cutoff on the `m`-th isolated occurrence. The supports can be chosen pairwise disjoint. Pointed heat-kernel convergence then gives

\[
\operatorname{Tr}\bigl(\chi_m e^{-t_0\Delta_{X_{\rm prime}}}\chi_m\bigr)
\longrightarrow a_H(t_0),
\tag{5}
\]

whereas the marked control gives

\[
\operatorname{Tr}\bigl(\chi_m Ue^{-t_0\Delta_{X_0}}U^{-1}\chi_m\bigr)
\longrightarrow a_0(t_0).
\tag{6}
\]

Thus the localized relative heat traces converge to the nonzero constant

\[
\boxed{
c_H(t_0):=a_H(t_0)-a_0(t_0)\ne0.}
\tag{7}
\]

## 3. Infinitely repeated nonzero local trace blocks are incompatible with trace class

Set

\[
T_{t_0}
=e^{-t_0\Delta_{X_{\rm prime}}}
-Ue^{-t_0\Delta_{X_0}}U^{-1}.
\]

Suppose, for contradiction, that `T_{t_0}` were trace class.

Because the cutoffs have pairwise disjoint supports, for every finite `N` and phases `\varepsilon_m` with `|\varepsilon_m|=1`,

\[
B_N:=\sum_{m=1}^N\varepsilon_m\chi_m^2
\]

satisfies

\[
\|B_N\|\le1.
\]

Choose `\varepsilon_m` to align the phases of

\[
\operatorname{Tr}(\chi_mT_{t_0}\chi_m).
\]

Cyclicity of the trace gives

\[
\sum_{m=1}^N
\left|
\operatorname{Tr}(\chi_mT_{t_0}\chi_m)
\right|
=
|\operatorname{Tr}(B_NT_{t_0})|
\le
\|T_{t_0}\|_{\mathcal S_1}.
\tag{8}
\]

But (5)--(7) imply

\[
\left|
\operatorname{Tr}(\chi_mT_{t_0}\chi_m)
\right|
\longrightarrow |c_H(t_0)|>0.
\]

The left side of (8) therefore grows linearly in `N`, a contradiction. Hence

\[
\boxed{T_{t_0}\notin\mathcal S_1.}
\tag{9}
\]

This is the central obstruction. Notice that the recurrence frequency is irrelevant: **infinitely many** asymptotically identical defects are enough. PF-068 showed that a fixed pattern has zero area density; PF-098 shows that zero density is still far too large for trace-class relative spectral theory when the amplitude of each defect does not decay.

## 4. Consequence for relative zeta functions, determinants and scattering

Müller's relative-zeta construction for noncompact operators starts from a pair `(A,A_0)` for which the relative heat operator

\[
e^{-tA}-e^{-tA_0}
\]

is trace class, together with the required small- and large-time asymptotics. The relative zeta function is obtained by Mellin transforming its trace. Borthwick--Judge--Perry use this architecture for infinite-area surfaces that are hyperbolic near infinity under controlled conformal perturbations, obtaining relative determinants whose divisors encode eigenvalues and resonances.

Equation (9) fails before any analytic continuation question arises. Therefore a smooth/PNT/integer control whose tangent hull omits recurrent prime tangents cannot serve as the reference in that standard architecture.

The same obstruction also rules out any ordinary Birman--Krein/relative-scattering setup that assumes a trace-class resolvent/heat perturbation of such a featureless reference. It does **not** rule out a new renormalized trace which explicitly subtracts each recurrent tangent sector; that would be a different construction and would need a canonical geometric prescription.

## 5. Why the projective-prime reference behaves differently

PF-087 found a trace-class object in `Re s>1/4`, but it compares

\[
x_n^E=\pi\cot\frac{\pi}{p_n}
\qquad\text{with}\qquad
x_n^0=p_n.
\]

Crucially, both sides are sampled at the **same primes**. They therefore share the full finite projective gap/tangent hull. Their difference is the finite-scale nonprojectivity of the endpoint map, beginning with the Schwarzian defect

\[
S\!\left(\pi\cot\frac{\pi}{p}\right)=\frac{2\pi^2}{p^4}
\]

from PF-082. That defect decays along the end, which is precisely the kind of behavior compatible with trace-class direct-channel comparison.

PF-088 then showed that the `Re s=1/4` boundary of that direct operator is already present for integer sampling, so the exponent itself is universal one-dimensional propagation rather than prime arithmetic.

This exposes a useful no-go tension:

\[
\boxed{
\begin{array}{c}
\text{featureless reference}\;\Rightarrow\;
\text{keeps prime-gap contrast but misses recurrent tangent hull}\;\Rightarrow\;
\text{not relative trace class},\\[1mm]
\text{prime-indexed projective reference}\;\Rightarrow\;
\text{matches tangent hull and admits a decaying direct defect}\;\Rightarrow\;
\text{subtracts the projective gap geometry itself}.
\end{array}}
\tag{10}
\]

Thus one cannot obtain a standard natural determinant merely by choosing a smooth null model and hoping that prime-gap fluctuations appear as a trace-class perturbation.

## 6. Exact geometry and interior/exterior duality

The obstruction is not an artifact of the cuff asymptotic. The short tangent separator is computed from the exact orthogonal-circle cross-ratio, and the localized wave/heat distinction is intrinsic to the resulting hyperbolic surface.

The asymptotic

\[
\ell_n\sim2\log\frac{4p_n}{g_n}
\]

is used only to translate the exact modulus into the distinguished-cuff language, as in (1).

All decisive data -- cross-ratios, primitive separator lengths, Laplacian heat kernels and pointed tangent geometry -- are preserved under ambient Möbius conjugacy. The interior/exterior inversion therefore carries the same tangent-hull mismatch and the same trace-class obstruction.

## 7. Prior-art / novelty audit

Known ingredients, not claimed as new:

- Werner Müller's relative zeta functions and determinants for noncompact self-adjoint elliptic operators, based on trace-class relative heat operators;
- Borthwick--Judge--Perry's relative determinants for controlled perturbations of infinite-area hyperbolic surfaces;
- the general principle that compact/trace-class perturbations cannot carry a nonvanishing family of identical defects escaping to infinity;
- right-limit/limit-operator descriptions of essential behavior, e.g. Last--Simon for Schrödinger/Jacobi/CMV operators and later graph/limit-operator work;
- uniqueness of the Laplace transform of a positive spectral measure and local wave-trace detection of closed geodesics.

Directed searches for relative determinants or scattering determinants on tight flutes and infinitely generated Fuchsian groups did not locate a theorem treating the present geometry. Existing tight-flute literature concentrates primarily on type/parabolicity and Fenchel--Nielsen criteria; standard hyperbolic determinant/scattering results assume geometrically finite or controlled asymptotic structures absent here.

The potentially new content is the program-specific composition

\[
\boxed{
\text{Pintz/Maynard recurrent isolated prime patterns}
\to
\text{exact recurrent hyperbolic tangents with nondecaying cuff contrast}
\to
\text{nonzero localized heat defect repeated at infinity}
\to
\text{failure of standard relative trace class against a smooth control}.
}
\]

The abstract operator principle is not new; the decisive point is that the exact prime-flute arithmetic supplies the recurrent order-one defects needed to trigger it.

## 8. Scope of the negative result

PF-098 does **not** say that every relative spectral object is impossible. It rules out the most natural standard route in which one compares the prime-flute to a featureless smooth/density-matched reference and then applies ordinary relative heat/resolvent trace theory.

A viable relative object would have to do something stronger than a single background subtraction. In particular it would have to retain or explicitly renormalize the entire recurrent tangent hull rather than treating prime-gap fluctuations as a decaying perturbation of a regular end.

This is consistent with PF-097: an individual tangent is primality-blind, but **which tangent types recur, and where they recur along the single infinite prime-flute, is precisely the information that prevents the prime geometry from becoming a trace-class perturbation of a featureless reference.**
