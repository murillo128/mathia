# ANF-106 — gap-free bounded-strip localization reduces fixed-notch exposure to finite physical boxes

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRIP-POSITIVE-OCCUPANCY + GAP-FREE-LOCALIZATION + FINITE-BOX-REDUCTION`. `ANF-099` reduces improvement along a fixed central-notch ray to the strict inequality `beta_eta<B_eta`, while `ANF-105` shows that a near-extremal high-exposure configuration can be localized to one physical component whenever a partition has small aggregate cross interaction in both the Montgomery--Taylor source form and the notch form. The missing bounded-height step was to construct such a partition without assuming empty horizontal gaps or a local density bound. That step is available exactly.

For every fixed height `H` and fixed notch `phi_eta`, a classical bandlimited Poisson minorant can be rescaled so that its real part is uniformly positive on the entire strip `|Im z|<=H`. Applied to the positive-multiplicity point configuration, it gives an `l^2` bound for horizontal cell occupancies in terms of the Montgomery--Taylor source energy. A finite random shift of a coarse grid then makes the **same** physical partition have small total cross budget in both quadratic forms. Consequently, at every fixed height and fixed error scale, any near-extremal configuration with large notch exposure contains a bounded-cardinality, bounded-span physical witness whose bounds are independent of the original cardinality and diameter.

This closes the gap-free bounded-height localization problem. It does **not** prove `beta_eta<B_eta`: the unrestricted envelope still permits height to grow, and even at fixed height the remaining finite-box exposure supremum must be bounded below `B_eta`.

## 1. A strip-positive bandlimited probe controls squared cell occupancy

Fix `H>=0` and one notch

\[
\phi_\eta(\alpha)=b_\eta(1-|\alpha|/\eta)_+,
\qquad 0<\eta<1,
\qquad 0\le\phi_\eta\le J_0:=J_{\rm MT}.
\tag{1}
\]

For a nonempty finite conjugation-invariant multiset `W`, all of whose points satisfy `|Im z|<=H`, retain the notation of `ANF-099`

\[
E_0(W)=\int J_0(\alpha)|S_W(\alpha)|^2\,d\alpha,
\qquad
L(W)=2|W|-\sigma(W),
\tag{2}
\]

\[
e(W)=\frac{E_0(W)}{L(W)}-1,
\qquad
h_\eta(W)=\frac{\int\phi_\eta|S_W|^2}{L(W)}.
\tag{3}
\]

Here `sigma(W)` counts distinct simple real sites. Put

\[
\theta=2^{-1/2},
\qquad a=2H+2,
\qquad j_*:=\frac{\cot^2\theta}{4}.
\tag{4}
\]

By the Montgomery--Taylor factorization in `ANF-087`,

\[
J_0=g*g,
\qquad
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin\theta}
       {\bf1}_{[-1/2,1/2]}(u).
\tag{5}
\]

On its support, `g>=cot(theta)/sqrt(2)`. When `|alpha|<=1/2`, the two translated supports in the convolution overlap on an interval of length at least `1/2`; hence

\[
\boxed{J_0(\alpha)\ge j_*\quad(|\alpha|\le1/2),}
\qquad
\int J_0=1.
\tag{6}
\]

Now define the real entire function

\[
P_a(z)=\frac{1-\cos(\pi z)/\cosh(\pi a)}{z^2+a^2},
\tag{7}
\]

with the apparent poles at `+-ia` removed. Under the Fourier convention

\[
\widehat f(\alpha)=\int_{\mathbb R}f(t)e^{-2\pi i\alpha t}\,dt,
\tag{8}
\]

a direct calculation from the transform of `(t^2+a^2)^{-1}` and the two frequency shifts produced by `cos(pi t)` gives

\[
\boxed{
 p_a(\alpha):=\widehat{P_a}(\alpha)
 =\frac{\pi}{a}
 \frac{\sinh(\pi a(1-2|\alpha|))}{\cosh(\pi a)}
 {\bf1}_{[-1/2,1/2]}(\alpha),
}
\tag{9}
\]

so `0<=p_a<=pi/a` and the cancellation outside `[-1/2,1/2]` is exact.

The load-bearing extra fact is positivity not merely on the real axis but throughout the required complex strip:

\[
\boxed{
\operatorname{Re}P_a(x+iy)
\ge\frac1{5(x^2+a^2)}
\quad(x\in\mathbb R,\ |y|\le H).
}
\tag{10}
\]

To verify it, set `A=x^2+a^2` and `D=(x+iy)^2+a^2`. Since `|y|<=H<a/2`,

\[
\operatorname{Re}D\ge\frac34A,
\qquad |D|\le\frac54A,
\qquad
\operatorname{Re}\frac1D\ge\frac{12}{25A},
\tag{11}
\]

and

\[
\frac{|D|}{\operatorname{Re}D}
\le\frac{a}{\sqrt{a^2-y^2}}<2.
\tag{12}
\]

Also

\[
\frac{|\cos(\pi(x+iy))|}{\cosh(\pi a)}
\le\frac{\cosh(\pi H)}{\cosh(\pi a)}
\le\frac1{\cosh(\pi(a-H))}<\frac14.
\tag{13}
\]

Thus the oscillatory term in (7) has modulus less than one half of `Re(1/D)`, giving `Re P_a>=6/(25A)>1/(5A)`.

Set

\[
F_W(t)=\sum_{z\in W}P_a(t-z).
\tag{14}
\]

Every summand has positive real part for real `t`. Since (9) is compactly supported, inverse Fourier transformation is valid at the finitely many complex shifts and gives

\[
\|F_W\|_2^2
=\int_{-1/2}^{1/2}|p_a(\alpha)S_W(\alpha)|^2\,d\alpha
\le\frac{\pi^2}{a^2j_*}E_0(W).
\tag{15}
\]

Partition the real axis into half-open cells `I_j=[aj,a(j+1))` and let `n_j` count **all entries with multiplicity** whose real part lies in `I_j`. If `t in I_j`, every point of that same cell contributes at least `1/(10a^2)` to `Re F_W(t)`, while all other cells contribute nonnegatively. Integrating `(Re F_W)^2` over the disjoint cells and using (15) yields

\[
\boxed{
\sum_j n_j^2\le C_HE_0(W),
\qquad
C_H:=\frac{100\pi^2a}{j_*}.
}
\tag{16}
\]

This is the missing occupancy estimate. It is derived from the actual source energy; no separation, density, cardinality or span hypothesis has been inserted.

## 2. Both quadratic forms have one summable cell-distance majorant

Let `K=widehat g`. From `ANF-104`, for `|z|>=1`,

\[
|K(z)|\le\kappa\frac{e^{\pi|\operatorname{Im}z|}}{|z|},
\qquad
\kappa:=\frac{1+\sqrt2\pi\cot\theta}{2\pi^2-1}.
\tag{17}
\]

From `ANF-105`,

\[
\widehat{\phi_\eta}(z)
=b_\eta\eta\,\operatorname{sinc}(\eta z)^2,
\qquad
\operatorname{sinc}(u)=\frac{\sin(\pi u)}{\pi u}.
\tag{18}
\]

For points whose real parts lie in two distinct elementary cells at cell distance `d>=1`, define

\[
\begin{aligned}
D_{H,\eta}:=\max\bigg\{&
2\big(e^{4\pi H}+b_\eta\eta e^{4\pi\eta H}\big),\\
&\frac5{a^2}
\left(\kappa^2e^{4\pi H}
+\frac{b_\eta}{\pi^2\eta}e^{4\pi\eta H}\right)
\bigg\}.
\end{aligned}
\tag{19}
\]

Then

\[
\boxed{
|K(z-\bar w)^2|+|\widehat{\phi_\eta}(z-\bar w)|
\le\frac{D_{H,\eta}}{1+d^2}.
}
\tag{20}
\]

For `d=1`, adjacent cells can contain arbitrarily close points, so one uses the direct spectral bounds `|K|^2<=e^{4pi H}` and `|widehat phi_eta|<=b_eta eta e^{4pi eta H}`. For `d>=2`, the horizontal distance exceeds `a(d-1)>=1`, so (17) and the inverse-square bound from (18) apply; the factor five follows from `(1+d^2)/(d-1)^2<=5`. Thus no hidden empty-gap assumption enters (20).

## 3. A shifted coarse grid makes the complete cross budget small

Fix an integer `R>=2`. Group the elementary cells into consecutive blocks of `R` cells. There are exactly `R` shifts of the grouping modulo the elementary grid. Each nonempty block defines a conjugation-invariant component and is complete on every real-part fiber, so the affine denominator is exactly additive as required by `ANF-105`.

For either `psi=J_0` or `psi=phi_eta`, let

\[
\delta_\psi
=\frac2{L(W)}\sum_{i<l}
\left|\operatorname{Re}\int\psi(\alpha)
S_{X_i}(\alpha)\overline{S_{X_l}(\alpha)}\,d\alpha\right|.
\tag{21}
\]

Two elementary cells a distance `d` apart are separated by a uniformly chosen grid shift with probability exactly `min(d/R,1)`. Expand each block cross term into point pairs **before** taking absolute values and apply (20). Averaging over the `R` shifts gives

\[
\mathbb E_{\rm shift}(\delta_0+\delta_\eta)
\le\frac{2D_{H,\eta}}{L(W)}
\sum_{d\ge1}
\frac{\min(d/R,1)}{1+d^2}
\sum_jn_jn_{j+d}.
\tag{22}
\]

Cauchy--Schwarz gives

\[
\sum_jn_jn_{j+d}\le\sum_jn_j^2,
\tag{23}
\]

while a harmonic sum for `d<=R` and an inverse-square tail for `d>R` give

\[
\sum_{d\ge1}
\frac{\min(d/R,1)}{1+d^2}
\le\frac{\log R+2}{R}.
\tag{24}
\]

Combining (16), (22) and (24), at least one shift satisfies the exact gap-free localization bound

\[
\boxed{
\delta_0+\delta_\eta
\le
2D_{H,\eta}C_H(1+e(W))\frac{\log R+2}{R}.
}
\tag{25}
\]

The same shift controls both forms because their nonnegative absolute budgets were added before averaging. The claim is existence of a good shift, not a bound for every fixed grid.

## 4. Bounded-height near-extremizers have finite-resolution physical witnesses

Assume `e(W)<=1` and define

\[
\varepsilon_R
:=4D_{H,\eta}C_H\frac{\log R+2}{R}.
\tag{26}
\]

For the shift from (25), `delta_0+delta_eta<=epsilon_R`. If `e(W)+epsilon_R<=1`, the exact component selector of `ANF-105` supplies a nonempty block `Y` with

\[
\boxed{
e(Y)\le\sqrt{e(W)+\varepsilon_R},
}
\tag{27}
\]

and

\[
\boxed{
h_\eta(Y)
\ge h_\eta(W)
-\sqrt{e(W)+\varepsilon_R}
-e(W)-2\varepsilon_R.
}
\tag{28}
\]

Its horizontal span is at most `aR`. Since it occupies at most `R` elementary cells, applying (16) to `Y` itself and using `L(Y)<=2|Y|` gives

\[
|Y|^2
\le R\sum_jn_j(Y)^2
\le RC_HE_0(Y)
\le2RC_H(1+e(Y))|Y|,
\tag{29}
\]

hence

\[
\boxed{
|Y|\le2C_HR(1+e(Y))\le4C_HR.
}
\tag{30}
\]

The count is total multiplicity, not only the number of distinct centers. For fixed `H`, fixed notch and fixed desired localization error, `R` can be chosen once and (27)--(30) then bound the witness independently of the size or diameter of `W`.

For a precise envelope consequence, let `beta_{eta,H}` denote the `ANF-099` near-extremizer envelope restricted to configurations with `|Im z|<=H`. Let `A^{box}_{H,R}(t)` be the supremum of `h_eta` over actual configurations with excess at most `t`, total cardinality at most `ceil(4C_HR)`, and, after horizontal translation, support contained in

\[
[0,aR]+i[-H,H].
\tag{31}
\]

Whenever `epsilon_R<=1/2`, applying (27)--(30) to a sequence with `e(W)->0` yields

\[
\boxed{
\beta_{\eta,H}
\le
A^{\rm box}_{H,R}(\sqrt{2\varepsilon_R})
+\sqrt{2\varepsilon_R}+3\varepsilon_R.
}
\tag{32}
\]

Thus the bounded-height part of the fatal exposure problem has been converted to finite physical boxes at every finite resolution. A certified bound making the right side of (32) strictly smaller than `B_eta` would exclude all bounded-height near-extremizers at the fatal exposure level.

## 5. Adversarial checks and limits

Several points are load-bearing. First, real-axis nonnegativity of a bandlimited minorant would not suffice: (10) is a separate complex-strip estimate and is what makes every physical point contribute with the same sign to (16). Signed point weights would destroy that argument. Second, one cannot choose a fixed grid and sum pairwise smallness naively; the proof controls the **aggregate** cross budget and only then selects one of the finitely many shifts. Third, the cell partition is by real part, so conjugate pairs and all copies of a real support site remain in one component; this preserves the exact denominator `L=2|W|-sigma` required by `ANF-105`.

The theorem is strictly fixed-height. The constants `D_{H,eta}` grow exponentially with `H`, so one may not interchange `H->infinity` with the near-extremizer limit or identify the unrestricted `beta_eta` with a uniform bounded-height envelope. The source-heavy high-tail mechanism isolated in `ANF-103`--`ANF-104` remains live. Nor does (32) produce one compact feasible set at zero error: the needed `R`, span and cardinality bounds grow as the desired localization error shrinks. Finally, collisions can change `sigma`; any future finite-box certification has to preserve or explicitly stratify real/nonreal and multiplicity types rather than appeal blindly to continuity of the normalized objective.

These controls also give direct falsification tests. A counterexample to the strip sign (10), the Fourier support/normalization (9), the occupancy inequality (16), the adjacent-cell case of (20), the shift probability in (22), or the `ANF-105` denominator additivity would invalidate the reduction. Each has been checked independently here under the declared hypotheses.

## 6. Prior-art boundary and research consequence

The probe (7) is classical rather than a new extremal function. In the normalization of Emanuel Carneiro and Micah B. Milinovich, *On Littlewood's estimate for the modulus of the zeta function on the critical line* (arXiv:2403.17803, Lemma 3),

\[
P_a
=\frac{\cosh(\pi a)+1}{a\cosh(\pi a)}\,m^-_{a,1/2}.
\tag{33}
\]

Their Lemma 3 explicitly reproduces the Poisson-kernel extremals of Carneiro--Chirre--Milinovich, *Bandlimited approximations and estimates for the Riemann zeta-function*, *Publ. Mat.* 63 (2019), 601--661, Lemma 9, DOI `10.5565/PUBLMAT6321906`. The downstream zeta application in the 2024 paper assumes RH, but the extremal-function formula used here does not import that assumption. Plancherel, Cauchy--Schwarz and finite random-grid averaging are likewise classical ingredients.

P.-L. Lions' concentration--compactness principle is the natural classical boundary for the broad idea of eliminating translation/dichotomy escape by localization. No concentration--compactness theorem is used as a black box: (16), (20), (25) and the splice with `ANF-105` are explicit finite estimates specialized to the Montgomery--Taylor source and fixed-notch observable. A targeted search across bandlimited Poisson extremals, large-sieve/concentration language and profile decomposition did not locate this same strip-positive occupancy estimate or the same-partition two-form finite-box reduction. The classification therefore claims only a Mathia-specific derived splice, not novelty of its standard ingredients.

The frontier after this result is sharper. **Within every fixed vertical strip, lack of empty horizontal gaps and arbitrarily large horizontal/cardinality complexity are no longer independent escape routes for `beta_eta`.** They can be localized away at any prescribed finite resolution. The remaining obstruction to `beta_eta<B_eta` is either already visible in the finite physical box problem (32), or uses height escaping to infinity strongly enough to defeat the fixed-strip constants. This cleanly separates the bounded-height certificate problem from the source-heavy endpoint escape studied in `ANF-103`--`ANF-104`.