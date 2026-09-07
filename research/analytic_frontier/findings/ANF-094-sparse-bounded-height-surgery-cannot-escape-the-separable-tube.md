# ANF-094 — sparse bounded-height surgery cannot escape the separable tube

**Status:** `EXACT-DERIVED + DESTINATION-NORMALIZATION + SPARSE-SURGERY + SEPARABLE-CONE + ALL-CARDINALITIES + DECISIVE-SCREENING`. `ANF-092`--`ANF-093` show that a vanishing-density finite-difference block can retain exponentially bad source-to-destination conditioning even inside an exactly separable Montgomery--Taylor near-extremizer. The generalized-eigenvector witness in `ANF-093`, however, is a signed coefficient direction rather than an actual multiset deformation. The first nonlinearization attempt is therefore to modify the physical conjugate pairs carried by that sparse block. The relative destination normalization of `ANF-086` imposes a strong obstruction: **any surgery affecting only `m=o(sqrt(N))` conjugate pairs and keeping all edited heights bounded remains asymptotically inside the protected separable tube, regardless of how badly conditioned the signed linearized direction is.**

Fix the central-notch data of `ANF-086`, with

\[
J_s\ge0,
\qquad
\|f\|_s^2:=\int_{-1}^{1}J_s(\alpha)|f(\alpha)|^2\,d\alpha,
\qquad
q_s>0,
\tag{1}
\]

and define the fixed finite constant

\[
M_s:=\left(\int_{-1}^{1}J_s(\alpha)\,d\alpha\right)^{1/2}.
\tag{2}
\]

Let `P` be any all-nonreal product multiset covered by `ANF-085`, of total cardinality `N`. Form a conjugation-invariant multiset `W` from `P` by replacing at most `m` labelled conjugate pairs. An original pair and its replacement may have arbitrary real centers, and both heights are only required to lie in `[0,H]`; height zero is allowed and means a double real site. No separation, distinctness, or collision restriction is imposed.

Then `P` is an admissible comparator in the definition of `d_sep(W)`, and

\[
\boxed{
 d_{\rm sep}(W)
 \le
 K_s\,\frac{m}{\sqrt N}\,\cosh(2\pi H),
 \qquad
 K_s:=\frac{2\sqrt2\,M_s}{\sqrt{q_s}}.
}
\tag{3}
\]

Consequently, for any sequence of such surgeries,

\[
\boxed{
 m_N\cosh(2\pi H_N)=o(\sqrt N)
 \quad\Longrightarrow\quad
 d_{\rm sep}(W_N)\longrightarrow0.
}
\tag{4}
\]

In particular, no sequence satisfying (4) can defeat the fixed central-notch certificate of `ANF-086`, whose fatal configurations require `d_sep>=kappa_crit>0`.

## 1. One edited conjugate pair has a uniform destination-norm budget

Write the structure factor of one conjugate pair at real center `x` and height `y>=0` as

\[
B_{x,y}(\alpha)
:=e^{-2\pi i\alpha(x+iy)}+e^{-2\pi i\alpha(x-iy)}
=2e^{-2\pi i\alpha x}\cosh(2\pi\alpha y).
\tag{5}
\]

For `|alpha|<=1` and `0<=y<=H`,

\[
|B_{x,y}(\alpha)|\le2\cosh(2\pi H).
\tag{6}
\]

Hence replacing `(x,y)` by any `(x',y')` with `0<=y'<=H` costs pointwise at most

\[
|B_{x',y'}(\alpha)-B_{x,y}(\alpha)|
\le4\cosh(2\pi H).
\tag{7}
\]

After at most `m` pair replacements, the triangle inequality gives

\[
|S_W(\alpha)-S_P(\alpha)|
\le4m\cosh(2\pi H)
\tag{8}
\]

throughout the support of `J_s`. Therefore

\[
\boxed{
\|S_W-S_P\|_s
\le4M_s m\cosh(2\pi H).
}
\tag{9}
\]

This estimate is deliberately worst-case. It does not ask the edited pairs to be separated or incoherent, so no Gram bound or square-root cancellation is hidden in the argument.

## 2. The separable carrier contributes a square-root-cardinality denominator

Because `P` is all nonreal, it has no simple real sites. Thus

\[
L(P)=2N.
\tag{10}
\]

The all-height separable theorem `ANF-085`, in the normalization used by `ANF-086`, gives

\[
\|S_P\|_s^2
=E_{F_s}(P)
\ge q_sL(P)
=2q_sN.
\tag{11}
\]

The surgery preserves total cardinality. Every replacement at height zero contributes a double real site, never a simple real site; collisions can only increase multiplicity. Hence `sigma(W)=0` as well, and the original product carrier `P` satisfies the comparison conditions defining `Sep(W)`.

Therefore

\[
\begin{aligned}
d_{\rm sep}(W)
&\le\delta_s(W\mid P)\\
&=\frac{\|S_W-S_P\|_s}{\|S_P\|_s}\\
&\le
\frac{4M_sm\cosh(2\pi H)}{\sqrt{2q_sN}},
\end{aligned}
\tag{12}
\]

which is exactly (3).

The scale `m/sqrt(N)` is the relevant unconditional sparsity threshold for this argument. Without extra geometric assumptions one cannot replace the triangle bound in (8) by uniform square-root cancellation: edited pair contributions may be made highly coherent by collisions or near-collisions. The point is that the `ANF-092` conditioning block is already much sparser than this worst-case threshold.

## 3. The `ANF-092`--`ANF-093` bad block cannot be nonlinearized at bounded height

For the near-extremizing product family of `ANF-092`,

\[
X_n=C_n\cup H_n,
\qquad
|C_n|=n+1,
\qquad
|H_n|=n^3,
\tag{13}
\]

and

\[
P_n=X_n+i\{-y_n,+y_n\},
\qquad
y_n=r^{n/8}.
\tag{14}
\]

Its total cardinality is

\[
N_n=2(n^3+n+1).
\tag{15}
\]

The exponentially bad Rayleigh direction in `ANF-093` is supported entirely on the `n+1` pairs above `C_n`. Consider **any actual multiset surgery on all of those pairs**, not merely the binomial signed direction: move their real centers arbitrarily, change their heights arbitrarily, allow collisions, and leave the `n^3` padding pairs untouched. If all old and new edited heights are at most `H_n`, then (3) gives

\[
\boxed{
 d_{\rm sep}(W_n)
 =O_s\!\left(
 n^{-1/2}\cosh(2\pi H_n)
 \right).
}
\tag{16}
\]

Thus every bounded-height surgery satisfies

\[
d_{\rm sep}(W_n)\to0.
\tag{17}
\]

More generally, for every fixed `epsilon>0`,

\[
H_n\le
\left(\frac1{4\pi}-\epsilon\right)\log n
\tag{18}
\]

still gives

\[
d_{\rm sep}(W_n)=O_s(n^{-2\pi\epsilon})\to0.
\tag{19}
\]

So the exponential generalized-eigenvalue blow-up of `ANF-093` cannot be converted into a fatal nonlinear geometry merely by assigning bounded, shrinking, or even moderately growing physical heights to its sparse conditioning block. The relative Hilbert normalization sees that block as vanishing mass against the `Theta(n^3)` safe carrier.

## 4. A genuine sparse-block escape must pay logarithmic height

Retain the fatal-distance threshold from `ANF-086`,

\[
\kappa_{\rm crit}>0.
\tag{20}
\]

If a surgery of the form above were to satisfy

\[
d_{\rm sep}(W)\ge\kappa_{\rm crit},
\tag{21}
\]

then (3) forces

\[
\boxed{
\cosh(2\pi H)
\ge
\frac{\kappa_{\rm crit}\sqrt N}{K_s m}.
}
\tag{22}
\]

Whenever the right side exceeds one,

\[
\boxed{
H
\ge
\frac1{2\pi}
\operatorname{arcosh}\!\left(
\frac{\kappa_{\rm crit}\sqrt N}{K_s m}
\right).
}
\tag{23}
\]

For the exact `ANF-092` scaling `N_n=2(n^3+n+1)` and `m_n=n+1`, equation (23) becomes

\[
\boxed{
H_n\ge\frac{\log n}{4\pi}+O_s(1).
}
\tag{24}
\]

This is only a **necessary** condition for turning the sparse block into a fatal configuration, not a construction. It nevertheless changes the live search region sharply. The source-window pathology from `ANF-093` lives at the exponentially small common height `y_n=r^{n/8}`; any actual sparse-block deformation that remains on comparable or bounded heights is screened before source conditioning matters. To threaten the central-notch certificate through that same vanishing-density block, one must simultaneously exploit vertical Fourier--Laplace amplification strong enough to overcome the `sqrt(N)` destination normalization.

## 5. Adversarial boundary and prior art

The proof does not use Montgomery--Taylor near-extremality of `W`; it is a pure destination-side screening theorem. That is stronger for the stated class, but also marks the boundary. The result does not control surgeries affecting `Omega(sqrt(N))` pairs, nor sparse surgeries whose heights reach the logarithmic scale in (23). Those are precisely the regimes where the crude coherent triangle bound no longer places the configuration inside the `ANF-086` tube.

It also does not claim that logarithmic height is sufficient for an obstruction. A candidate reaching (23) must still satisfy the independent Montgomery--Taylor near-extremizer gate, and the same large Fourier--Laplace factors that enlarge the destination defect may make that source condition difficult. Establishing compatibility or incompatibility of those two requirements is the next substantive test.

The norm estimate (9) is elementary Hilbert-space perturbation theory, and no novelty is claimed for triangle-inequality stability itself. A targeted prior-art check of frame perturbations, sparse nonharmonic exponential sums, and finite exponential-sum stability found only the classical neighboring perturbation/reconstruction framework, not the line-specific `m cosh(2 pi H)/sqrt(N)` screening consequence obtained by combining a sparse pair edit with the all-height separable energy floor of `ANF-085` and the normalized cone distance of `ANF-086`. No external theorem is load-bearing, so `SOURCES.md` is unchanged.

## Research consequence

`ANF-093` proves that even the exact Lamzouri source quotient leaves exponentially bad signed cross-window directions on the safe near-extremal cone. `ANF-094` shows why that linear pathology is not yet a nonlinear obstruction: **the specific bad block has too little physical mass to escape the normalized separable tube at bounded height.** The surviving route is now two-parameter rather than purely condition-number driven. A genuine counterfamily built from sparse conditioning must combine vanishing support fraction with at least logarithmic vertical amplification while preserving Montgomery--Taylor near-extremality. The next decisive calculation should test whether that logarithmic-height requirement is compatible with the exact projection-tax identity of `ANF-088`; if it is not, the sparse-conditioning escape closes entirely.