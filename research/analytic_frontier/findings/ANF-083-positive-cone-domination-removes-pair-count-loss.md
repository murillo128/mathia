# ANF-083 — positive-cone domination removes the pair-count loss from the central-notch complex tube

**Status:** `EXACT-DERIVED + CENTRAL-NOTCH + ALL-CARDINALITY-COMPLEX-TUBE + PAIR-COUNT-FREE + UNBOUNDED-HORIZONTAL-COMPLEXITY + UNBOUNDED-REAL-MULTIPLICITY + STRICT-MONTGOMERY-TAYLOR-IMPROVEMENT`. `ANF-081` closes the affine certificate on every finite real multiset for one fixed central notch, while `ANF-082` lifts that certificate to conjugation-invariant complex multisets only inside a height tube of width `h_p asymp p^{-1/4}` when there are `p` nonreal conjugate pairs. That shrinking width is not intrinsic to the fixed central-notch family. The exact Montgomery--Taylor spatial kernel is entrywise nonnegative, and that extra positive-cone structure controls the whole vertical perturbation relative to the energy of the real-part collapse before any pairwise triangle inequality is taken.

There therefore exist one fixed central-notch spectrum

\[
J_s=J_{\rm MT}-s\phi_\eta\ge0,
\qquad F_s=\widehat J_s,
\]

one fixed constant `q_*>0`, and one fixed height `h_*>0` such that **every finite conjugation-invariant multiset** `W` satisfying

\[
\max_{z\in W}|\operatorname{Im}z|\le h_*
\]

obeys

\[
\boxed{
E_{F_s}(W)\ge q_*\bigl(2N-\sigma(W)\bigr),
}
\tag{1}
\]

where `N=|W|` and `sigma(W)` counts simple real sites, while simultaneously

\[
\boxed{
\frac{C(J_s)}{q_*}<C_{\rm MT}.
}
\tag{2}
\]

The constants are independent of `N`, the number of nonreal pairs, all horizontal positions, collisions, repeated nonreal pairs, and arbitrary real multiplicities. Thus the `p^{-1/4}` loss in `ANF-082` is a phase-blind proof loss for this profile, not a genuine near-real complex obstruction.

## 1. Positive-cone domination gives a relative vertical perturbation bound

Fix the spectrum from `ANF-081` and abbreviate

\[
J_0:=J_{\rm MT},\qquad R_0:=\widehat J_0,
\qquad J_s=J_0-s\phi_\eta.
\]

`ANF-030` gives the special pointwise property

\[
\boxed{R_0(t)\ge0\qquad(t\in\mathbb R),}
\tag{3}
\]

and `ANF-034` gives

\[
0\le\phi_\eta\le J_0.
\]

Hence

\[
\boxed{(1-s)J_0\le J_s\le J_0.}
\tag{4}
\]

For a finite conjugation-invariant multiset `W`, let `X` be its real-part collapse, preserving multiplicity, and put

\[
h:=\max_{z\in W}|\operatorname{Im}z|.
\]

Group all entries by distinct real parts `x_i`. Let `r_i` be the real multiplicity at `x_i`, and let the nonreal pairs centered there have heights `y_{ij}>0` and positive integer pair multiplicities `n_{ij}`. The collapsed multiplicity is

\[
m_i=r_i+2\sum_jn_{ij}.
\tag{5}
\]

For `k>=1` define

\[
a_{i,k}:=2\sum_jn_{ij}y_{ij}^{2k},
\qquad
T_k(\alpha):=\sum_i a_{i,k}e^{-2\pi i\alpha x_i}.
\tag{6}
\]

Since all coefficients are nonnegative,

\[
0\le a_{i,k}\le h^{2k}m_i.
\tag{7}
\]

Write

\[
\|f\|_r^2:=\int_{-1}^{1}J_r(\alpha)|f(\alpha)|^2\,d\alpha,
\qquad r\in\{0,s\}.
\]

Using (3), the quadratic form for `T_k` is coefficientwise monotone on the positive cone:

\[
\begin{aligned}
\|T_k\|_0^2
&=\sum_{i,l}a_{i,k}a_{l,k}R_0(x_i-x_l)\\
&\le h^{4k}\sum_{i,l}m_im_lR_0(x_i-x_l)\\
&=h^{4k}\|S_X\|_0^2.
\end{aligned}
\tag{8}
\]

This is the decisive step absent from `ANF-082`: it compares the perturbation coefficients with the collapsed coefficients **inside the same nonnegative spatial Gram form**, instead of replacing every complex pair by a separate absolute-value contribution.

The Fourier--Laplace contribution of one conjugate pair is exact, so

\[
D(\alpha):=S_W(\alpha)-S_X(\alpha)
=\sum_{k\ge1}\frac{(2\pi)^{2k}}{(2k)!}\alpha^{2k}T_k(\alpha).
\tag{9}
\]

For finite `W` the series is uniformly convergent on `[-1,1]`. Since `|alpha|<=1`, multiplication by `alpha^{2k}` is a contraction in either weighted `L^2` norm. Equations (4), (8), and Minkowski therefore give

\[
\begin{aligned}
\|D\|_s
&\le\sum_{k\ge1}\frac{(2\pi)^{2k}}{(2k)!}
       \|\alpha^{2k}T_k\|_s\\
&\le\sum_{k\ge1}\frac{(2\pi)^{2k}}{(2k)!}\|T_k\|_0\\
&\le\bigl(\cosh(2\pi h)-1\bigr)\|S_X\|_0\\
&\le
\boxed{
\frac{\cosh(2\pi h)-1}{\sqrt{1-s}}\,\|S_X\|_s.
}
\end{aligned}
\tag{10}
\]

Unlike the `O(ph^2)` estimate of `ANF-082`, (10) is **relative** and contains neither the number of pairs nor the total cardinality.

## 2. The all-real certificate lifts to one fixed complex tube

Let `q=q_s` be the fixed real-certificate constant from `ANF-081` and put

\[
\rho:=\frac{C(J_s)}{C_{\rm MT}}<q.
\tag{11}
\]

Choose any fixed

\[
\rho<q_*<q
\]

and define

\[
\kappa_*:=1-\sqrt{q_*/q}\in(0,1),
\tag{12}
\]

\[
\boxed{
h_*:=\frac1{2\pi}
\operatorname{arcosh}\!\left(
1+\sqrt{1-s}\,\kappa_*
\right)>0.}
\tag{13}
\]

For `h<=h_*`, equation (10) says

\[
\|S_W-S_X\|_s\le\kappa_*\|S_X\|_s.
\tag{14}
\]

The real-part collapse preserves `N` and cannot create a new simple real site, so

\[
\sigma(X)\le\sigma(W).
\tag{15}
\]

Applying `ANF-081` to `X`,

\[
\|S_X\|_s^2
=E_{F_s}(X)
\ge q\bigl(2N-\sigma(X)\bigr)
\ge q\bigl(2N-\sigma(W)\bigr).
\tag{16}
\]

The reverse triangle inequality and the retained sign `kappa_*<1` now yield

\[
\begin{aligned}
\sqrt{E_{F_s}(W)}
&=\|S_W\|_s\\
&\ge(1-\kappa_*)\|S_X\|_s\\
&\ge\sqrt{q_*\bigl(2N-\sigma(W)\bigr)}.
\end{aligned}
\tag{17}
\]

Squaring gives (1). Equation (2) follows immediately from `q_*>rho`. The same fixed notch therefore has a nonzero open complex neighborhood of the **entire** finite real-multiplicity locus, with no shrinking as the number of conjugate pairs grows.

## 3. Why the `p^{-1/4}` scale disappears

`ANF-082` first bounded the perturbation pointwise by summing `p` pair contributions coherently and only afterward compared that absolute perturbation with the real Hilbert norm. The resulting numerator was `O(ph^2)`, while the universal real norm floor was only `O(sqrt(p))`, forcing `h=O(p^{-1/4})`.

Equation (8) changes the order of operations. The positive coefficients generated by all vertical moments are dominated coefficientwise by the collapsed multiplicity vector, and `R_MT>=0` makes the whole Montgomery--Taylor quadratic form monotone under that domination. Consequently every even vertical moment is paid relative to `||S_X||_0`, and the complete hyperbolic series resums to the scalar factor `cosh(2pi h)-1`. No cardinality estimate is needed at any stage.

This is genuinely special to the Montgomery--Taylor base kernel. Spectral nonnegativity alone gives positive definiteness but does **not** make a quadratic form monotone under coefficientwise domination. For example, take `J_0=1/2` on `[-1,1]`, so `R_0(t)=sinc(2t)`. At sites `0,3/4`, `R_0(3/4)=-2/(3pi)`. With nonnegative vectors `a=(10,0)<=m=(10,1)`,

\[
E(a)=100,
\qquad
E(m)=101-\frac{40}{3\pi}<100.
\tag{18}
\]

Thus (8) really uses the explicit square representation of `R_MT` from `ANF-030`, not merely Bochner positivity.

## 4. Adversarial audit and failure modes

The proof has six load-bearing checks. The factor two in (6) is forced by the two members of each conjugate pair and exactly matches the Taylor expansion in (9). Grouping repeated centers before applying (8) covers pair collisions and arbitrary integer multiplicities rather than assuming distinct horizontal sites. The coefficientwise comparison is legal only because all `a_{i,k}`, `m_i`, and all entries `R_0(x_i-x_l)` are nonnegative. The direction of the norm comparison in the last line of (10) follows from `J_s>=(1-s)J_0`. The real theorem is used only on the real multiset `X`. Finally, `kappa_*<1` is retained before squaring the reverse-triangle lower bound.

Uniform convergence causes no hidden interchange problem: for finite `W` and finite `h`, the conjugate-pair cosh series converges uniformly on the compact frequency interval, so the finite weighted measure `J_s(alpha)dalpha` admits the displayed Minkowski limit. No small-height Taylor truncation is used.

The result does not prove monotonicity of energy under arbitrary vertical motion; it proves a controlled relative perturbation bound inside the fixed strip `|Im z|<=h_*`. Nor does it show that `widehat J_s` is pointwise nonnegative. The argument deliberately moves to the unperturbed norm for the positive-cone comparison and uses only spectral comparability to return to `J_s`.

## 5. Prior art and evidence boundary

The ingredients are classical at the appropriate level. Carneiro--Chandee--Littmann--Milinovich supply the Montgomery--Taylor extremal Hilbert-space framework whose exact extremizer is used in `ANF-030`. Buescu--Paixão--Symeonides give the classical Fourier--Laplace/positive-definite strip representation relevant to complex translations. Positive-cone monotonicity for a quadratic form with entrywise nonnegative kernel and Hilbert-space triangle inequalities are elementary. A targeted search of positive-definite-kernel, Fourier--Laplace, and pair-correlation literature did not identify a theorem that supplies the specific relative estimate (10) or its affine splice (11)--(17). No theorem-level novelty is claimed for the classical ingredients, and no new `SOURCES.md` entry is needed because the load-bearing literature anchors are already present.

The result remains an auxiliary certificate inside the Mathia/BGSST-style affine program. It does **not** prove a full complex affine certificate, a new unconditional proportion of critical zeros, a zero-free strip for zeta, or RH. Configurations with `max|Im z|>h_*` remain open.

## 6. Consequence for the live frontier

The near-real multi-pair escape route left by `ANF-082` is closed for the fixed central-notch profile: increasing the number of conjugate pairs cannot force the admissible complex tube back onto the real axis. Any remaining counterexample must leave one fixed positive-width strip around the real-multiplicity locus.

The next decisive question is therefore the **complementary-height problem**. A useful positive result would give large-height coercivity or another global comparison that pushes all possible counterexamples back into the protected strip. A useful negative result would exhibit a genuinely positive-height configuration violating the affine certificate. Either outcome now tests real complex geometry rather than an artifact of coherent pair counting.
