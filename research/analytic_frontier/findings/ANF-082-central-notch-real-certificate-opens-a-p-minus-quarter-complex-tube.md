# ANF-082 — central-notch real certificate opens a p-minus-quarter complex tube

**Status:** `EXACT-DERIVED + CENTRAL-NOTCH + ALL-REAL-CERTIFICATE-LIFT + GENERAL-CONJUGATION-INVARIANT-COMPLEX-TUBE + UNBOUNDED-HORIZONTAL-COMPLEXITY + UNBOUNDED-REAL-MULTIPLICITY + P-MINUS-QUARTER-HEIGHT-EXCLUSION + STRICT-MONTGOMERY-TAYLOR-IMPROVEMENT`. `ANF-081` proves that one fixed central-notch spectrum beats Montgomery--Taylor while satisfying the affine counting inequality for every finite real multiset, with no restriction on support size or multiplicity. The remaining obstruction is therefore genuinely non-real. The real certificate has a quantitative open neighborhood in the full complex configuration space: if a conjugation-invariant multiset contains `p` nonreal conjugate pairs and every nonreal point has height at most an explicit `h_p>0`, then the same fixed spectrum still satisfies an affine certificate that strictly beats Montgomery--Taylor. The tube is uniform in all horizontal positions, all real multiplicities, and total cardinality, and its elementary worst-case width satisfies `h_p asymp p^{-1/4}`.

This is not a small-cardinality statement. Earlier complex reductions such as `ANF-035`--`ANF-072` use special one-pair, common-fiber, or low-cardinality geometry. Here the only inputs are the full real-multiplicity theorem `ANF-081`, positive spectral energy, and the exact Fourier--Laplace structure factor of conjugate pairs.

## 1. Preserve part of the real normalization margin

Fix the central-notch parameters supplied by `ANF-081` and write

\[
J:=J_s\ge0,
\qquad
F:=\widehat J,
\qquad
q:=q_s\in(0,1).
\tag{1}
\]

For every finite real multiset `X`, with cardinality `N(X)` and number of simple sites `sigma(X)`, `ANF-081` proves

\[
\boxed{
E_F(X)\ge q\bigl(2N(X)-\sigma(X)\bigr).
}
\tag{2}
\]

It also proves the strict objective inequality

\[
\frac{C(J)}q<C_{\rm MT}.
\tag{3}
\]

Put

\[
\rho:=\frac{C(J)}{C_{\rm MT}},
\qquad
\mu:=\int_{-1}^{1}J(\alpha)\,d\alpha=F(0)>0.
\tag{4}
\]

Then `rho<q`. Choose any fixed

\[
\boxed{
q_*\in(\rho,q),
}
\tag{5}
\]

for example `q_*=(q+rho)/2`, and define

\[
\delta:=\sqrt q-\sqrt{q_*}>0.
\tag{6}
\]

The retained normalization still improves Montgomery--Taylor:

\[
\boxed{
\frac{C(J)}{q_*}<C_{\rm MT},
\qquad
2-\frac{C(J)}{q_*}>2-C_{\rm MT}.
}
\tag{7}
\]

The gap `delta` is the Hilbert-norm budget available for moving points away from the real axis.

## 2. Every real-part collapse has a norm floor in the correct affine variable

Let `W` be any finite conjugation-invariant multiset. Write

\[
N:=|W|,
\qquad
\sigma:=\sigma(W),
\qquad
M:=2N-\sigma.
\tag{8}
\]

Let `p` be the number of nonreal conjugate pairs counted with multiplicity, so `W` has exactly `2p` nonreal entries. Let `R(W)` be the real-part collapse obtained by replacing every `x+iy,x-iy` by two copies of `x`.

The collapse preserves cardinality and cannot create a new simple real point from a nonreal pair. It can instead destroy an existing simple point if the pair collapses onto its support. Therefore

\[
\boxed{
\sigma(R(W))\le\sigma(W)=\sigma.
}
\tag{9}
\]

Applying (2) to `R(W)` gives

\[
\begin{aligned}
E_F(R(W))
&\ge q\bigl(2N-\sigma(R(W))\bigr)\\
&\ge qM.
\end{aligned}
\tag{10}
\]

Since `J>=0`, energy is the squared Hilbert norm of the structure factor,

\[
E_F(Z)
=
\int_{-1}^{1}J(\alpha)|S_Z(\alpha)|^2\,d\alpha,
\qquad
S_Z(\alpha)=\sum_{z\in Z}e^{-2\pi i\alpha z}.
\tag{11}
\]

Thus (10) is equivalently

\[
\boxed{
\|S_{R(W)}\|_{L^2(J)}\ge\sqrt{qM}.
}
\tag{12}
\]

There is also a purely combinatorial lower bound on `M` in terms of the complex mass. If `r=N-2p` is the number of real entries counted with multiplicity, then `sigma<=r`, whence

\[
M=2N-\sigma
\ge2N-r
=N+2p
=r+4p
\ge4p.
\tag{13}
\]

Hence

\[
\boxed{
\sqrt M\ge2\sqrt p.
}
\tag{14}
\]

No support separation or multiplicity hypothesis is used here.

## 3. Moving `p` conjugate pairs changes the structure factor by a controlled Hilbert vector

Assume now `p>=1` and put

\[
h:=\max_{z\in W}|\operatorname{Im}z|.
\tag{15}
\]

List the nonreal pairs, with multiplicity, as

\[
x_j+iy_j,\quad x_j-iy_j,
\qquad
1\le j\le p,
\qquad
0<y_j\le h.
\tag{16}
\]

At a real frequency `alpha`, the contribution of the `j`-th pair to `S_W-S_{R(W)}` is exactly

\[
2e^{-2\pi i\alpha x_j}
\bigl(\cosh(2\pi\alpha y_j)-1\bigr).
\tag{17}
\]

Therefore, with

\[
D(\alpha):=S_W(\alpha)-S_{R(W)}(\alpha),
\tag{18}
\]

support in `|alpha|<=1` gives the pointwise bound

\[
\boxed{
|D(\alpha)|
\le
2p\bigl(\cosh(2\pi h)-1\bigr).
}
\tag{19}
\]

After integration against `J`,

\[
\boxed{
\|D\|_{L^2(J)}
\le
2p\bigl(\cosh(2\pi h)-1\bigr)\sqrt\mu.
}
\tag{20}
\]

This estimate is deliberately phase-blind. All `p` pair perturbations are allowed to align coherently at every frequency; any horizontal cancellation can only improve it.

## 4. An explicit all-cardinality complex height tube

Define

\[
\boxed{
h_p:=
\frac1{2\pi}
\operatorname{arcosh}\!\left(
1+\frac{\delta}{\sqrt{\mu p}}
\right).
}
\tag{21}
\]

If `h<=h_p`, then (20) gives

\[
\|D\|_{L^2(J)}
\le2\delta\sqrt p
\le\delta\sqrt M,
\tag{22}
\]

where the last inequality is (14). The reverse triangle inequality in `L^2(J)` and (12) now yield

\[
\begin{aligned}
\sqrt{E_F(W)}
&=\|S_{R(W)}+D\|_{L^2(J)}\\
&\ge\|S_{R(W)}\|_{L^2(J)}-\|D\|_{L^2(J)}\\
&\ge(\sqrt q-\delta)\sqrt M\\
&=\sqrt{q_*M}.
\end{aligned}
\tag{23}
\]

Squaring proves

\[
\boxed{
E_F(W)\ge q_*\bigl(2N-\sigma(W)\bigr).
}
\tag{24}
\]

Equivalently,

\[
\boxed{
\sigma(W)
\ge
2N-q_*^{-1}E_F(W).
}
\tag{25}
\]

Together with (7), this gives the promised statement: **the fixed central-notch spectrum from `ANF-081` beats Montgomery--Taylor on every finite conjugation-invariant multiset whose `p` nonreal pairs lie in the tube `|Im z|<=h_p`.** There is no bound on the number of real sites, their occupancies, their horizontal geometry, pair collisions, or the horizontal positions of the complex pairs.

For `p=0`, equation (25) is already `ANF-081` with the stronger constant `q`; no height condition is needed.

## 5. The exclusion width decays only as `p^{-1/4}`

The explicit tube has a simple large-`p` scale. Since

\[
\operatorname{arcosh}(1+x)\sim\sqrt{2x}
\qquad(x\downarrow0),
\]

(21) gives

\[
\boxed{
h_p
\sim
\frac{\sqrt\delta}
{\sqrt2\,\pi\,\mu^{1/4}}
\,p^{-1/4}.
}
\tag{26}
\]

Thus any sequence of affine counterexamples for this fixed central notch with `p` nonreal pairs must satisfy

\[
\max|\operatorname{Im}z|>h_p.
\tag{27}
\]

In particular, for every fixed `p` there is a strictly positive height neighborhood of the full real-multiplicity boundary containing no counterexample, uniformly over arbitrary horizontal complexity. If `p` grows, a counterexample cannot approach the real axis faster than the explicit `p^{-1/4}` scale supplied by this worst-case estimate.

The exponent `1/4` is **not claimed sharp**. It comes from combining a coherent `O(ph^2)` structure-factor perturbation with the universal affine mass floor `M>=4p`, whose Hilbert norm is only `O(sqrt p)`. A cancellation-sensitive or moment-weighted estimate could enlarge the tube.

## 6. Adversarial audit and evidence boundary

The argument has five load-bearing points. First, `ANF-081` is applied only to the real multiset `R(W)`, exactly within its proved scope. Second, the simple-point comparison has the favorable direction `sigma(R(W))<=sigma(W)` even when collapsed pairs collide with existing real supports. Third, (17) is the exact Fourier--Laplace contribution of a conjugate pair; the hyperbolic growth is not linearized. Fourth, all phase information is discarded only through the triangle inequality, so repeated horizontal centers and coherent pair multiplicities are covered rather than excluded. Fifth, the objective payment is explicit: `q_*` is chosen strictly above `C(J)/C_MT`, so the tube retains a strict Montgomery--Taylor improvement instead of merely preserving nonnegativity.

Several edge cases are automatic. A pair occurring with multiplicity `k` is counted as `k` conjugate pairs and is covered by the same estimate. Arbitrarily large real occupancies remain covered because they enter only through the real theorem `ANF-081`. If many complex pairs share a horizontal coordinate, (19) already assumes the worst possible coherent addition. If the collapse removes simple real points, (10) only strengthens.

The analytic ingredients beyond the line-local findings are classical: positive compact-spectrum Fourier energy as an `L^2(J)` norm and Hilbert-space triangle inequalities. The Fourier--Laplace strip framework is already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides, while the pair-correlation/Hilbert framework is already anchored through Lamzouri, BGSST, and Carneiro--Chandee--Littmann--Milinovich. A targeted literature check did not identify a theorem supplying this Mathia-specific affine lift from the all-real certificate, so no new load-bearing source entry is required and no publication-level novelty claim is made.

This finding does **not** prove the full complex affine certificate, a better unconditional zeta-zero proportion, or RH. Configurations with heights above `h_p` remain open, and the tube shrinks with the number of nonreal pairs. Its role is to remove an entire all-cardinality boundary layer: after `ANF-081`, a complex obstruction cannot emerge by an arbitrarily small vertical perturbation of a dangerous real multiset without paying a quantitative height cost.

## 7. Next decisive test

The next useful reduction should attack the dependence on `p` or the complementary height region. One route is to retain horizontal phase information in (17) and replace the coherent `p` loss by a structure-factor or Gram estimate tied to the real energy floor; any gain from `p` toward `sqrt p` would widen the protected tube substantially. The complementary route is a large-height coercivity estimate exploiting the same nonnegative compact spectrum, so that for each `p` all possible counterexamples are compactified into an explicit intermediate-height region. Either improvement would turn the current local openness of the all-real certificate into a substantially more global complex-screening theorem.