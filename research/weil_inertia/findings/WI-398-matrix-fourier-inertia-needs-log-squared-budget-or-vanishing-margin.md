# WI-398 — matrix Fourier inertia needs a log-squared source budget or vanishing spectral margin

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + QUANTITATIVE-STRUCTURAL-BARRIER + PRIOR-ART-AUDITED`.

**Parent findings:** WI-236, WI-395, WI-397. Related matrix barriers: WI-139, WI-154, WI-321.

## Claim

WI-395 proves a sharp scalar strip-contraction inequality in the square-root-prime Fourier norm, and WI-397 combines it with Jutila's uniform near-critical-line zero-density theorem to show that the density-normalized horizontal signal of any scalar Fourier-Stieltjes detector with bounded absolute prime budget is `O(log^{-2} T)`. WI-236 identifies a different but complementary obstruction: finite inertia already detects finite RH failure exactly, while an infinite sparse escape can survive only through collapse of the spectral margin at zero.

These two obstructions fit together in a dimension-free matrix statement. Passing from a scalar Fourier detector to an arbitrarily large Hermitian matrix-valued Fourier detector does **not** remove the quadratic-log budget barrier if the source side is still controlled by weighted operator total variation. Instead, every positive-density inertia change must be paid for either by a source budget of order `log^2 T` or by a corresponding collapse of the reference spectral margin.

Let `M_T` be a countably additive `M_{d_T}(C)`-valued Borel measure of finite total variation, where the matrix dimension `d_T` may grow arbitrarily with `T`. Write `|M_T|` for its total-variation measure in operator norm and define

\[
B_T:=\int_{\mathbb R}e^{|u|/2}\,d|M_T|(u)<\infty,
\tag{1}
\]

\[
H_T(z):=\int_{\mathbb R}e^{iuz}\,dM_T(u),
\qquad |\Im z|\le\frac12.
\tag{2}
\]

For real `gamma` and `0<=delta<1/2`, put

\[
\Delta_\delta H_T(\gamma)
:=H_T(\gamma+i\delta)+H_T(\gamma-i\delta)-2H_T(\gamma).
\tag{3}
\]

Let `q(delta)` be the sharp scalar contraction factor of WI-395,

\[
q(0)=0,
\]

and, for `0<delta<1/2`,

\[
q(\delta)=
\left(\frac{1-2\delta}{1+2\delta}\right)^{\frac1{2\delta}-1}
\left(\frac{4\delta}{1+2\delta}\right)^2.
\tag{4}
\]

Then the scalar inequality amplifies exactly to operator norm:

\[
\boxed{
\|\Delta_\delta H_T(\gamma)\|_{\rm op}
\le q(\delta) B_T.
}
\tag{5}
\]

The constant `q(delta)` is still sharp in the matrix class, independently of `d_T`: scalar sharpness embeds into any matrix dimension by multiplying a scalar extremizer by a rank-one Hermitian projection.

Now impose the Hermitian reflection symmetry

\[
M_T(-E)=M_T(E)^*
\tag{6}
\]

for every Borel set `E`. Then `H_T(x)` is Hermitian for real `x`, while

\[
H_T(\gamma+i\delta)^*=H_T(\gamma-i\delta).
\tag{7}
\]

For each right-half off-critical zero occurrence

\[
\rho=\frac12+\delta_\rho+i\gamma_\rho,
\qquad
T<\gamma_\rho\le2T,
\qquad
0<\delta_\rho<\frac12,
\]

let `K_\rho=K_\rho^*` be any Hermitian background independent of whether the mirror pair is kept off the line or projected to the line, and define

\[
A_\rho^0:=K_\rho+2H_T(\gamma_\rho),
\tag{8}
\]

\[
A_\rho:=K_\rho
+H_T(\gamma_\rho+i\delta_\rho)
+H_T(\gamma_\rho-i\delta_\rho).
\tag{9}
\]

Both matrices are Hermitian and

\[
A_\rho-A_\rho^0
=\Delta_{\delta_\rho}H_T(\gamma_\rho).
\tag{10}
\]

Define the reference spectral margin

\[
g_\rho:=\operatorname{dist}(0,\operatorname{spec}A_\rho^0).
\tag{11}
\]

If the inertia changes under the horizontal displacement,

\[
\operatorname{In}(A_\rho)\ne\operatorname{In}(A_\rho^0),
\tag{12}
\]

then Weyl spectral stability gives the exact necessary condition

\[
\boxed{
g_\rho\le
\|\Delta_{\delta_\rho}H_T(\gamma_\rho)\|_{\rm op}
\le q(\delta_\rho)B_T.}
\tag{13}
\]

Let `C_T` be any multiset of right-half off-critical occurrences for which (12) holds, and put

\[
N_T:=N(2T)-N(T),
\qquad
L_T:=\log(T/2\pi).
\]

WI-397 proves, from Jutila's uniform zero-density theorem and the sharp WI-395 contraction factor,

\[
\frac1{N_T}
\sum_{\rho\in E_T^+}q(\delta_\rho)
\ll \frac1{L_T^2},
\tag{14}
\]

where `E_T^+` is the full multiset of right-half off-critical zero occurrences in the dyadic height window. Summing (13) over `C_T` therefore yields

\[
\boxed{
\frac1{N_T}
\sum_{\rho\in C_T} g_\rho
\ll \frac{B_T}{L_T^2}.}
\tag{15}
\]

Consequently, for every `eta>0`,

\[
\boxed{
\frac1{N_T}
\#\{\rho\in C_T:g_\rho\ge\eta\}
\ll \frac{B_T}{\eta L_T^2}.}
\tag{16}
\]

In particular, if `|C_T|>=cN_T` for some fixed `c>0`, then

\[
\frac1{|C_T|}\sum_{\rho\in C_T}g_\rho
\ll_c \frac{B_T}{L_T^2}.
\tag{17}
\]

Thus a positive-density matrix-inertia detector with `B_T=o(L_T^2)` can succeed only on blocks whose critical-projection reference matrices become spectrally singular. With bounded `B_T`, positive-density detection forces average reference margin `O(L_T^{-2})`; by Markov, a positive fraction of the detected blocks has margin on that same scale. Conversely, if a positive-density target family has a uniform reference gap `g_\rho>=eta>0`, then any detector in this class that changes its inertia on that family must satisfy

\[
\boxed{B_T\gg_{c,\eta}L_T^2.}
\tag{18}
\]

No RH conclusion and no improved simple-critical-zero proportion is claimed. The result is a quantitative no-go theorem for a specific but broad matrix escape: arbitrary matrix dimension and coherent cross-channel interference do not help when horizontal information is generated by one matrix Fourier-Stieltjes observable and the prime side is controlled by its componentwise absolute square-root-weighted operator variation.

## 1. Operator-valued strip contraction is dimension-free

From (2), exactly as in the scalar calculation,

\[
\Delta_\delta H_T(\gamma)
=2\int_{\mathbb R}
e^{iu\gamma}\bigl(\cosh(\delta u)-1\bigr)\,dM_T(u).
\tag{19}
\]

The defining variation inequality for a finite-dimensional Banach-valued measure gives

\[
\begin{aligned}
\|\Delta_\delta H_T(\gamma)\|_{\rm op}
&\le
\int_{\mathbb R}
2\bigl(\cosh(\delta|u|)-1\bigr)\,d|M_T|(u)\\
&\le
\sup_{D\ge0}
\left[2(\cosh(\delta D)-1)e^{-D/2}\right]
\int e^{|u|/2}\,d|M_T|(u).
\end{aligned}
\tag{20}
\]

WI-395 computes the scalar supremum in brackets exactly as `q(delta)`, proving (5). No scalar compression, positivity, commutativity, or fixed matrix dimension is used: the proof is simply the triangle inequality in the operator norm after passing to total variation.

Sharpness is equally direct. Let `P` be any rank-one Hermitian projection and let `mu_delta` be a scalar symmetric two-frequency measure attaining the WI-395 extremum at

\[
D_*(\delta)=
\frac1\delta
\log\frac{1+2\delta}{1-2\delta}.
\]

Taking

\[
dM_T(u)=P\,d\mu_\delta(u)
\]

reduces both sides of (5) to the scalar equality case on the range of `P`. Hence no dimension-dependent improvement of `q(delta)` is possible from the weighted operator-variation budget alone.

This boundary differs from WI-154 and WI-321. WI-154 closes pointwise-PSD matrix one-delta kernels by quadratic compression to the sharp scalar CCLM extremizer, while WI-321 closes positive Hilbert-valued channelization of a scalar Weil semibound. Equation (5) requires neither pointwise positivity nor a positive channel metric; it allows a fully signed/noncommuting matrix Fourier measure. What it assumes instead is that the source cost is controlled by absolute operator variation before any arithmetic cancellation.

## 2. Hermitian symmetry makes horizontal displacement an inertia perturbation

Condition (6) is the natural Fourier symmetry for a Hermitian real-axis observable. Indeed, changing variables `u->-u` in the adjoint integral gives

\[
H_T(z)=H_T(\overline z)^*.
\tag{21}
\]

Equations (7)--(10) follow immediately. The background `K_\rho` is deliberately arbitrary: any Hermitian part of a proposed finite matrix certificate that is unchanged by horizontally projecting the given mirror pair can be included there. Thus the argument is not tied to a particular choice of Gram basis or to Lamzouri's tensor representation.

If `g_\rho>0` and

\[
\|A_\rho-A_\rho^0\|_{\rm op}<g_\rho,
\]

then Weyl's Hermitian eigenvalue perturbation inequality keeps every ordered eigenvalue of `A_\rho` on the same side of zero as the corresponding eigenvalue of `A_\rho^0`. Hence the positive and negative indices are unchanged. Taking the contrapositive proves the first inequality in (13); if `g_\rho=0`, it is trivial.

The key point is that inertia can only amplify a tiny horizontal Fourier perturbation if the reference matrix is already close to singular. This is precisely the spectral-margin escape identified abstractly in WI-236, now with a quantitative source-side scale attached to it.

## 3. Jutila prices the total available margin crossing

The remaining input is already audited in WI-397. Jutila's uniform near-critical-line zero-density estimate implies an exponentially decaying tail for the normalized depth

\[
Y_\rho=\delta_\rho L_T,
\]

out to a slowly growing `O(log L_T)` window. Combining that tail with

\[
q(\delta)=\frac{16}{e^2}\delta^2+O(\delta^3)
\]

near the critical line and the trivial boundedness `q(delta)<1` yields (14). The rate `L_T^{-2}` is the strongest consequence available from those two interfaces alone: WI-397 exhibits an abstract Jutila-compatible positive-density population at fixed normalized depth `Y_0`, for which the mean of `q(delta)` is itself of order `L_T^{-2}`.

Since `C_T` is a submultiset of `E_T^+`, (13) and (14) give

\[
\sum_{\rho\in C_T}g_\rho
\le
B_T\sum_{\rho\in E_T^+}q(\delta_\rho)
\ll
N_T\frac{B_T}{L_T^2},
\]

which is (15). Equations (16)--(18) are immediate consequences.

There is a useful stronger reading of (15). Suppose `|C_T|>=cN_T`. Then at least half of `C_T` must satisfy

\[
g_\rho\ll_c \frac{B_T}{L_T^2},
\tag{22}
\]

since otherwise the sum of the margins would exceed (15). More generally, any proposed distributional lower bound on the reference margins converts directly into a lower bound on the source budget required for positive-density inertia sensitivity.

This is not yet a defect-to-zero bootstrap. It is instead a **margin-or-budget dichotomy**: if one can independently rule out the `O(B_T/L_T^2)` near-null reference sector for a zeta-specific matrix family, then the same source budget can no longer support positive-density off-line inertia changes. That gives a precise next interface for combining source-side arithmetic with the spectral geometry of WI-236/WI-139.

## 4. Scope and failure modes

The theorem should not be read as saying that all matrix Weil-form methods have a `log^2 T` barrier. Several routes remain genuinely outside its hypotheses.

First, the actual signed prime polynomial may be much smaller than the componentwise absolute weighted operator variation `B_T`. WI-395 already identifies this as the scalar escape, and the same caveat is load-bearing here. A theorem exploiting arithmetic cancellation before taking operator variation can have a different budget.

Second, a global matrix may couple many zeros nonlocally rather than decompose into blocks whose off-line-versus-projected difference is one common Fourier mirror perturbation of the form (10). The result applies only once such a blockwise perturbation representation has been justified.

Third, nonlinear statistics, determinant identities, Schur complements, or source-dependent test selection can preserve information not represented by a single linear matrix Fourier-Stieltjes observable. Likewise, a source norm intrinsically adapted to an indefinite signature may not dominate `B_T`.

Fourth, the theorem gives no lower bound on `g_\rho` for Bombieri, Lamzouri, or another concrete zeta matrix. WI-236 explicitly warns that zero spectral margin is the unresolved infinite-dimensional escape. The present result quantifies how fast that margin must collapse **if** a Fourier-generated bounded-budget detector is to change inertia on positive density; it does not close the escape by itself.

Finally, the use of Jutila is occurrence-weighted and unconditional, but it does not identify the uncertified complement as an off-line population. Multiple critical-line zeros and proof slack remain separate categories, as required by the research mandate.

## 5. Prior art and novelty audit

The ingredients are classical or already established in this line. The total-variation estimate for Banach/operator-valued measures is standard vector-measure integration. Weyl's perturbation inequality for Hermitian matrices,

\[
|\lambda_j(A+E)-\lambda_j(A)|\le\|E\|_{\rm op},
\]

and the consequent stability of inertia under perturbations smaller than the distance of the reference spectrum from zero are classical matrix analysis; see, for example, Rajendra Bhatia, *Perturbation Bounds for Matrix Eigenvalues*, especially the treatment of spectral variation of Hermitian matrices. The zeta-specific density input and its required uniformity in the near-line displacement were already checked against the primary/literature chain in WI-397.

A targeted literature search around operator-valued Fourier-Stieltjes transforms, matrix-valued Hermitian Fourier analysis, spectral-variation/inertia perturbation, and zeta explicit-formula matrices found standard operator-valued Fourier and Weyl--Titchmarsh theory but no result matching the present combined statement. Those neighboring sources are not load-bearing: the proof of (5) is the elementary vector-measure variation inequality, and the inertia step is standard Weyl stability.

The Mathia-corpus deduplication is more important here. WI-154 treats pointwise-PSD support-one matrix kernels and therefore a different positivity cone. WI-321 treats positive Hilbert-channel lifts of a scalar semibound. WI-139 gives orientation rigidity for Lamzouri's negative eigenspace near saturation. WI-236 identifies zero spectral margin as the abstract escape from finite-inertia completeness but gives no source-side rate. WI-395 gives the sharp scalar horizontal contraction, and WI-397 derives the `L_T^{-2}` average contraction from Jutila. None of those statements yields the dimension-free implication (15)--(18) for matrix Fourier inertia detectors.

The new line-local deduction is therefore the combination: **operator-valued Fourier variation preserves the sharp scalar strip contraction, and Weyl stability converts Jutila's `L_T^{-2}` horizontal budget into an `L_T^{-2}` spectral-margin budget for every positive-density inertia change.** This is a novelty statement about the Mathia research corpus, not an external priority claim.

## Research consequence

Matrix dimension by itself is not an escape from the scalar horizontal observability barrier. If a proposed matrix certificate is generated by Fourier-Stieltjes channels whose true source cost is controlled by weighted absolute operator variation, then arbitrarily many channels still face the same sharp `q(delta)` contraction. Jutila then forces the total margin that those channels can cross at positive density to be only `O(B_T/L_T^2)`.

This sharpens the surviving program after WI-236 and WI-397. A useful next theorem must do at least one of two things: obtain a zeta-specific lower bound on the relevant reference spectral margins, thereby turning (15) into a contradiction for bounded/subquadratic-log source cost, or exhibit genuinely signed arithmetic cancellation/nonlinear matrix structure whose source budget is not measured by `B_T`. Merely enlarging a bounded-budget scalar Fourier observable into a larger coherent matrix does not address the obstruction.