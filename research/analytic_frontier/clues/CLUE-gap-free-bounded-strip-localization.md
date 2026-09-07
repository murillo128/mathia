---
id: CLUE-analytic-frontier-gap-free-bounded-strip-localization
type: research-clue
status: resolved
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-087-montgomery-taylor-equality-is-a-two-site-real-zero-set-packing.md
  - research/analytic_frontier/findings/ANF-099-fixed-notch-ray-is-controlled-by-near-extremizer-exposure.md
  - research/analytic_frontier/findings/ANF-104-remote-source-heavy-tails-require-core-tail-endpoint-coupling.md
  - research/analytic_frontier/findings/ANF-105-endpoint-decoupled-profile-splitting-cannot-raise-fixed-notch-exposure.md
---

# Can a positive strip probe localize bounded-height near-extremizers without empty horizontal gaps?

## Observation

ANF-105 extracts a near-extremal high-exposure component when a physical partition has small aggregate interactions in both the Montgomery--Taylor source norm and the fixed-notch observable. Its endpoint/gap criterion supplies one sufficient condition, but does not construct such a partition for a configuration with no large empty horizontal gaps. Assuming a local occupancy bound before making the cut would leave a new unproved physical hypothesis.

There is a candidate way to supply both missing pieces for every fixed height strip. A rescaled classical bandlimited Poisson minorant has positive real part throughout a narrower strip. Applied to the actual positive-multiplicity configuration, it bounds the sum of squared horizontal cell occupancies by the source energy. Averaging a coarse grid over its finitely many shifts can then make the complete cross budget small, even when adjacent occupied cells touch. ANF-105 supplies the final component selection.

## Research question

Fix `H>=0` and one notch `phi_eta(alpha)=b_eta(1-|alpha|/eta)_+`, with `0<eta<1`, `b_eta>0` and `0<=phi_eta<=J_0=J_MT`. Retain ANF-099's conventions
\[
E_0(W)=\int J_0|S_W|^2,\quad
L(W)=2|W|-\sigma(W),\quad
e(W)=E_0(W)/L(W)-1,\quad
h_\eta(W)=\int\phi_\eta|S_W|^2/L(W),
\]
where `sigma` counts simple real sites and all multisets are nonempty, finite and conjugation-invariant. Every point, including multiplicities, must satisfy `|Im z|<=H`.

Independently audit the following gap-free localization claim. There are explicit constants depending only on `H` and the fixed notch such that, for every integer `R>=2`, a partition into horizontal blocks of width `(2H+2)R` satisfies
\[
\boxed{\delta_0+\delta_\eta
 \le 2D_{H,\eta}C_H(1+e(W))\,\frac{\log R+2}{R}.}
\tag{1}
\]
Here the two `delta` quantities are exactly ANF-105's normalized sums of absolute component cross terms, on the **same partition**. No point separation, local density, cardinality, or total span bound is assumed.

The stronger consequence to check is an explicit finite-resolution witness reduction: a bounded-height global near-extremizer with large notch exposure contains a component whose excess and exposure errors are controlled by (1), and whose horizontal span **and total multiplicity** have bounds independent of the original configuration's size. The proof and all constants below are proposed for checking, not asserted as independently accepted evidence.

## Why it may matter

This would replace ANF-105's conditional decoupling input by a constructed partition throughout the bounded-height class, including linearly dense or highly clustered configurations without empty gaps. The new source input is a derived squared-occupancy estimate, not a restatement that cross terms should be small.

For fixed height and fixed error tolerance, a high-exposure obstruction would have a bounded-size, bounded-span witness. This creates a precise finite-variable certificate target; it does not promise that the deliberately coarse bounds make numerical verification feasible. It also does not control height growing without bound, interchange height and near-extremality limits, or prove the strict exposure inequality required by ANF-099.

## Decisive test

**Derive local occupancy from a probe positive on the whole strip.** Write
\[
\theta=2^{-1/2},\qquad a=2H+2,\qquad
j_*=\frac{\cot^2\theta}{4}.
\]
ANF-087 gives `J_0=g*g`, where
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin\theta}
       {\bf1}_{[-1/2,1/2]}(u).
\]
The overlap of the two intervals has length at least `1/2` when `|alpha|<=1/2`, and `g>=cot(theta)/sqrt(2)` on its interval. Hence
\[
J_0(\alpha)\ge j_*\quad (|\alpha|\le1/2),\qquad \int J_0=1.
\tag{2}
\]

Consider the real entire function
\[
P_a(z)=\frac{1-\cos(\pi z)/\cosh(\pi a)}{z^2+a^2}.
\tag{3}
\]
Both apparent poles are removable. With Fourier convention
`widehat f(alpha)=integral f(t) exp(-2 pi i alpha t) dt`, its transform is
\[
p_a(\alpha)=
 \frac{\pi}{a}\,
 \frac{\sinh(\pi a(1-2|\alpha|))}{\cosh(\pi a)}
 {\bf1}_{[-1/2,1/2]}(\alpha),\qquad
0\le p_a\le\pi/a.
\tag{4}
\]
One can verify (4) directly from the transform of `(t^2+a^2)^(-1)` and the two frequency shifts from `cos(pi t)`. The cancellation outside `[-1/2,1/2]` is exact. Inverse Fourier transformation extends to all complex arguments.

The additional property needed here is not real-axis nonnegativity alone, but
\[
\boxed{\operatorname{Re}P_a(x+iy)\ge
       \frac1{5(x^2+a^2)}
       \quad(x\in\mathbb R,\ |y|\le H).}
\tag{5}
\]
For a direct check put `A=x^2+a^2` and `D=(x+iy)^2+a^2`. Since `|y|<=a/2`,
\[
\operatorname{Re}D\ge3A/4,\quad |D|\le5A/4,\quad
\operatorname{Re}(1/D)\ge12/(25A),\quad
\frac{|D|}{\operatorname{Re}D}
 \le\frac{a}{\sqrt{a^2-y^2}}<2.
\]
Moreover
\[
\frac{|\cos(\pi(x+iy))|}{\cosh(\pi a)}
 \le\frac{\cosh(\pi H)}{\cosh(\pi a)}
 \le\frac1{\cosh(\pi(a-H))}<\frac14.
\]
Thus the oscillatory correction in (3) has modulus at most half the real part of `1/D`. This gives `Re P_a>=6/(25A)>=1/(5A)`.

For the actual configuration set `F_W(t)=sum_(z in W) P_a(t-z)`. Equation (5) ensures every summand has positive real part on the real axis. Equation (4), Plancherel and (2) yield
\[
\|F_W\|_{L^2(\mathbb R)}^2
 =\int_{-1/2}^{1/2}|p_a(\alpha)S_W(\alpha)|^2d\alpha
 \le\frac{\pi^2}{a^2j_*}E_0(W).
\tag{6}
\]
The identity follows from the explicit inverse transform and finite summation; no complex shift of an infinite contour is being assumed.

Let `n_j` count all entries of `W` whose real parts lie in the half-open cell
`I_j=[aj,a(j+1))`. For every `t in I_j`, its own cell contributes at least
`n_j/(10a^2)` to `Re F_W(t)`, and all other cells contribute nonnegatively. Integrating over the disjoint cells in (6) gives
\[
\boxed{\sum_jn_j^2\le C_HE_0(W),\qquad
       C_H=\frac{100\pi^2a}{j_*}.}
\tag{7}
\]
This is the step that replaces an assumed density/occupancy condition. Positive multiplicities are essential; no sign is being asserted for the original complex Montgomery--Taylor cross terms.

**Obtain a summable cell-distance majorant.** Let
\[
K(z)=\widehat g(z),\qquad
\kappa=\frac{1+\sqrt2\pi\cot\theta}{2\pi^2-1}.
\]
ANF-104 gives `|K(z)|<=kappa exp(pi |Im z|)/|z|` for `|z|>=1`. ANF-105 gives
\[
\widehat{\phi_\eta}(z)=b_\eta\eta\,\operatorname{sinc}(\eta z)^2,
\qquad \operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
\]
For points in distinct elementary cells a distance `d=|j-l|>=1` apart, the following explicit choice suffices:
\[
\begin{split}
D_{H,\eta}:=\max\bigg\{&
2\big(e^{4\pi H}+b_\eta\eta e^{4\pi\eta H}\big),\\
&\frac5{a^2}
 \left(\kappa^2e^{4\pi H}
       +\frac{b_\eta}{\pi^2\eta}e^{4\pi\eta H}\right)
\bigg\}.
\end{split}
\tag{8}
\]
Indeed
\[
|K(z-\bar w)^2|+
|\widehat{\phi_\eta}(z-\bar w)|
 \le \frac{D_{H,\eta}}{1+d^2}.
\tag{9}
\]
When `d=1`, use the elementary spectral bounds `e^(4 pi H)` and
`b_eta eta exp(4 pi eta H)`; adjacent cells can contain arbitrarily close points, so the remote bound is not applicable there. When `d>=2`, the horizontal distance is at least `a(d-1)>=1`, and the inverse-square bounds apply. The factor five in (8) follows from
`(1+d^2)/(d-1)^2<=5`. This handles near-boundary pairs without inserting a hidden empty gap.

**Select a grid shift after bounding the whole cross budget.** For an integer `R>=2`, group elementary cells into consecutive groups of `R` cells. There are `R` possible integer shifts of this grouping. Each induced nonempty component `X_i` contains complete real-part fibers, so
\[
L(W)=\sum_iL(X_i)
\]
holds exactly. For each shift use ANF-105's definitions
\[
\delta_\psi=
 \frac2{L(W)}\sum_{i<l}
 \left|\operatorname{Re}\int\psi S_{X_i}\overline{S_{X_l}}\right|,
 \qquad \psi=J_0,\phi_\eta.
\tag{10}
\]
A pair of elementary cells at distance `d` is separated by a uniformly chosen shift with probability `min(d/R,1)`. Expand the block cross terms before taking pairwise absolute bounds in (9). Then
\[
\mathbb E_{\rm shift}(\delta_0+\delta_\eta)
 \le\frac{2D_{H,\eta}}{L(W)}
 \sum_{d\ge1}\frac{\min(d/R,1)}{1+d^2}
                 \sum_j n_jn_{j+d}.
\tag{11}
\]
Cauchy--Schwarz gives `sum_j n_j n_(j+d)<=sum_j n_j^2`. Also
\[
\sum_{d\ge1}\frac{\min(d/R,1)}{1+d^2}
 \le\frac{\log R+2}{R}.
\tag{12}
\]
Use the harmonic sum for `d<=R` and an inverse-square integral for `d>R`. Substituting (7) proves the expectation bound (1); at least one of the finitely many shifts is no worse than its average. The same shift controls both observables because their nonnegative budgets were added before averaging.

This is a total-interaction estimate, not an assertion that individually small pair interactions may be summed without a cardinality cost. It does not assert the bound for every shift.

**Splice into the physical profile selector and bound the witness size.** For `e(W)<=1`, define
\[
\varepsilon_R:=
4D_{H,\eta}C_H\,\frac{\log R+2}{R}.
\tag{13}
\]
Choose the shift just constructed, so `delta_0+delta_eta<=epsilon_R`. If
`e(W)+epsilon_R<=1`, ANF-105's component lemma gives one nonempty block `Y` with
\[
\boxed{e(Y)\le\sqrt{e(W)+\varepsilon_R},}
\tag{14}
\]
\[
\boxed{h_\eta(Y)\ge h_\eta(W)
 -\sqrt{e(W)+\varepsilon_R}-e(W)-2\varepsilon_R.}
\tag{15}
\]
Its horizontal span is at most `aR`, its height bound remains `H`, and no change to the notch or source spectrum has occurred.

The block has at most `R` elementary cells. Apply (7) to `Y` itself and use
`L(Y)<=2|Y|`:
\[
|Y|^2\le R\sum_jn_j(Y)^2
 \le RC_HE_0(Y)
 \le2RC_H(1+e(Y))|Y|.
\]
Therefore
\[
\boxed{|Y|\le2C_HR(1+e(Y))\le4C_HR.}
\tag{16}
\]
The count includes all multiplicities, not just distinct centers. Neither (14)--(16) contains the original `|W|` or its diameter.

For a concrete envelope test, let `beta_(eta,H)` be ANF-099's near-extremizer envelope restricted to `|Im z|<=H`. Define `A_box_(H,R)(t)` as the supremum of `h_eta` over actual configurations of excess at most `t`, total cardinality at most `ceil(4C_HR)`, and, after horizontal translation, lying in
`[0,aR]+i[-H,H]`. If `epsilon_R<=1/2`, then every sufficiently near-extremal sequence has `e(W)<=epsilon_R`. Equations (14)--(16) give
\[
\boxed{\beta_{\eta,H}\le
 A^{\rm box}_{H,R}\!\left(\sqrt{2\varepsilon_R}\right)
 +\sqrt{2\varepsilon_R}+3\varepsilon_R.}
\tag{17}
\]
A rigorous upper bound making the right side smaller than `B_eta` would exclude bounded-height near-extremizers at the fatal exposure level. Equation (17) is a proposed finite-resolution reduction, **not** that upper bound. The box may contain very many variables because the constants are conservative.

For validation, first check the strip sign (5), the Fourier normalization (4)--(6), cell counts including multiplicities, and the adjacent-cell case in (9). Next check the exact shift probability and the factors of two in (10)--(11), and verify that the selected component has the true simple-real-site denominator. A counterexample to any of these statements under the declared hypotheses is a decisive rejection of this handoff. If they pass, the next substantive task is a certified bound on (17)'s physical finite-box exposure or a sharper localization constant, not simply restating the existence of a cut.

## Evidence boundary

This is a proposed analytical handoff for independent Research Watch validation, not a canonical finding or a formal proof artifact. The supplied derivation aims to establish occupancy control and gap-free localization at fixed height; it does not establish `beta_eta<B_eta`, a bound on the finite-box supremum, an improved unconditional zero proportion, or RH. The all-configuration source floor and the ANF-105 selection lemma remain named dependencies.

The probe itself is classical. In the notation of Lemma 3 of Emanuel Carneiro and Micah B. Milinovich, *On Littlewood's estimate for the modulus of the zeta function on the critical line*, arXiv:2403.17803v1 (2024), it is exactly
\[
P_a=\frac{\cosh(\pi a)+1}{a\cosh(\pi a)}\,m^-_{a,1/2}.
\]
That lemma reproduces the Poisson extremal functions of Carneiro--Chirre--Milinovich, *Bandlimited approximations and estimates for the Riemann zeta-function*, Publ. Mat. 63 (2019), 601--661, Lemma 9. Their approximation formula requires no RH; **none of the RH-conditional zeta estimates in the 2024 paper is imported here**. No novelty is claimed for the Poisson minorant, its Fourier transform, Plancherel, finite random-grid averaging or Cauchy--Schwarz. The proposed Mathia contribution is their strip-positive occupancy application and its quantitative splice into the two-observable physical profile lemma.

P.-L. Lions, *The concentration-compactness principle in the calculus of variations. The locally compact case, part 1*, Ann. Inst. H. Poincare Anal. Non Lineaire 1(2) (1984), 109--145, is a conceptual prior-art boundary for profile localization and escape. No compactness theorem from that paper is used to skip the explicit physical estimates above.

Several distinctions must survive review. A real-axis nonnegative or positive-definite function need not have positive real part on a complex strip; (5) is a separate load-bearing proof. Signed coefficients would invalidate (7). A fixed unlucky grid may repeatedly cut closely spaced pairs, so only existence of a good shift is asserted. Spectral positivity does not justify deleting negative source cross terms. Source-negligible counting tails and source-negligible energy tails are not interchangeable.

Finally, `H` is fixed before sending `R` to infinity, and (8) grows exponentially with `H`. The unrestricted envelope allows height to grow along near-extremizers, so it must not be replaced without proof by `sup_H beta_(eta,H)`. Nor do (16)--(17) supply one compact set for the zero-error limit: the witness bound grows as the desired localization error shrinks. Collisions change `sigma`, so any finite-box verification must preserve the real/nonreal and multiplicity strata instead of assuming continuity of the affine denominator. The unbounded-height source-heavy mechanism in ANF-103--ANF-104 remains open.

## Research disposition

Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-106-gap-free-bounded-strip-localization-reduces-fixed-notch-exposure-to-finite-physical-boxes.md]]
