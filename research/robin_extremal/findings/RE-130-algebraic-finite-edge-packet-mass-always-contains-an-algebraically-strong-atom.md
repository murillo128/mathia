# RE-130 — algebraic finite-edge packet mass always contains an algebraically strong atom

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + ABSOLUTE-PACKET-MASS + MAX-ATOM-INTERPOLATION + RIEMANN-VON-MANGOLDT + DIFFUSE-BRANCH-ELIMINATION + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-129`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix `K>=0`. For a positive-ordinate subedge zero

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\qquad
\gamma>0,
\]

write

\[
a_{\rho,K}(U)
:=e^{-(\Theta-\beta)U}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{U^k(1-\rho)^{k+1}}
\right].
\tag{1}
\]

Define the largest atom and the absolute packet mass by

\[
M_K(U)
:=
\max_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
|a_{\rho,K}(U)|,
\tag{2}
\]

and

\[
\mathfrak A_K(U)
:=
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
|a_{\rho,K}(U)|,
\tag{3}
\]

with zeros counted with multiplicity. The maximum in (2) exists by `RE-129`, and the sum in (3) converges absolutely.

There is a constant `C=C(K,sigma_0,Theta)` such that, whenever `U` is sufficiently large and `0<M_K(U)<=e^-2`,

\[
\boxed{
\mathfrak A_K(U)
\le
C\sqrt{M_K(U)}
\log\frac{e}{M_K(U)}.
}
\tag{4}
\]

Consequently, the maximum atom and the full absolute packet mass have the same algebraic-versus-superalgebraic dichotomy:

\[
\boxed{
M_K(U)=U^{-\omega(1)}
\quad\Longleftrightarrow\quad
\mathfrak A_K(U)=U^{-\omega(1)}.
}
\tag{5}
\]

More quantitatively, for every fixed `B>0` and `c>0`,

\[
\mathfrak A_K(U)\ge cU^{-B}
\tag{6}
\]

forces

\[
\boxed{
M_K(U)
\ge
c'_{B,c,K,\sigma_0,\Theta}
\frac{U^{-2B}}{(\log U)^2}
}
\tag{7}
\]

for all sufficiently large `U`. In particular, for every fixed `eta>0`,

\[
M_K(U)\gg U^{-2B-\eta}.
\tag{8}
\]

Since

\[
\mathcal S_K(U)
=
2\Re\sum_\rho a_{\rho,K}(U)e^{i\gamma U}
\tag{9}
\]

satisfies

\[
|\mathcal S_K(U)|\le2\mathfrak A_K(U),
\tag{10}
\]

an algebraic signed packet value also forces an algebraically strong individual atom. Thus the `RE-124`--`RE-129` **diffuse algebraic cloud is not an independent escape route**: an infinite collection of individually superalgebraic atoms cannot collectively carry algebraic absolute mass, and hence cannot create an algebraic finite-edge residual.

Combining (7)--(8) with `RE-129` gives an exhaustive algebraic-scale dichotomy inside the attained finite-edge packet. If the packet carries algebraic absolute mass, then a dominant algebraically strong atom exists. On an observation window `H=U^(1-theta)`, either the residual has an algebraic excursion of size comparable to that dominant atom, or hiding it forces the inverse-window, logarithmically comparable, cancelling-phase companion of `RE-129`. When the resulting atom exponent is below `K+1`, `RE-123` transfers the excursion branch to actual regular CA states.

## 1. The coefficient family has a summable universal height envelope

The uniform coefficient asymptotic already used in `RE-124`--`RE-129` is

\[
a_{\rho,K}(U)
=
\frac{e^{-(\Theta-\beta)U}}{\rho(1-\rho)}
\left(1+O_K(U^{-1})\right),
\tag{11}
\]

uniformly on the fixed strip. Because `Theta<1`, both `beta` and `1-beta` stay a fixed positive distance from zero. Hence

\[
|\rho(1-\rho)|
=|\rho|\,|1-\rho|
\asymp_{\sigma_0,\Theta}1+\gamma^2,
\tag{12}
\]

and the damping factor never exceeds one. Therefore

\[
\boxed{
|a_{\rho,K}(U)|
\le
\frac{C_K}{1+\gamma^2}
}
\tag{13}
\]

for every sufficiently large `U`, uniformly over every zero in the subedge strip.

The Riemann--von Mangoldt estimate, used here only in its weakest counting form,

\[
N(T)\ll T\log(2+T),
\tag{14}
\]

implies

\[
\sum_{\gamma>T}\frac1{1+\gamma^2}
\ll
\frac{\log(2+T)}{T}
\qquad(T\ge2).
\tag{15}
\]

Indeed, dyadic decomposition gives

\[
\sum_{2^jT<\gamma\le2^{j+1}T}
\frac1{1+\gamma^2}
\ll
\frac{N(2^{j+1}T)}{(2^jT)^2}
\ll
\frac{j+\log(2+T)}{2^jT},
\tag{16}
\]

and summing over `j>=0` proves (15). Multiplicity causes no issue because `N(T)` already counts it.

Equation (15) proves the absolute convergence in (3). More importantly, it prevents an arbitrarily large population of tiny atoms from defeating the maximum coefficient by sheer cardinality.

## 2. Maximum-versus-mass interpolation

Write

\[
M:=M_K(U)
\]

and suppose `0<M<=e^-2`. Set

\[
T:=M^{-1/2}.
\tag{17}
\]

For ordinates `gamma<=T`, maximality gives `|a_(rho,K)(U)|<=M`; hence (14) gives

\[
\sum_{0<\gamma\le T}|a_{\rho,K}(U)|
\le
M N(T)
\ll
M T\log(2+T)
\ll
\sqrt M\log\frac eM.
\tag{18}
\]

For `gamma>T`, use the universal envelope (13) and (15):

\[
\sum_{\gamma>T}|a_{\rho,K}(U)|
\ll
\sum_{\gamma>T}\frac1{1+\gamma^2}
\ll
\frac{\log(2+T)}{T}
\ll
\sqrt M\log\frac eM.
\tag{19}
\]

Adding (18) and (19) proves (4).

This split is sharp enough for the present purpose. The low ordinates can contain at most `O(T log T)` atoms, while the `1/gamma^2` coefficient envelope makes the high-ordinate tail only `O((log T)/T)`. Balancing the two at `T=M^-1/2` leaves no room for a genuinely diffuse algebraic mass with a superalgebraic maximum.

## 3. Algebraic mass forces an algebraic atom

The implication from `mathfrak A_K` to `M_K` in (5) is immediate from (4); the reverse implication uses only `M_K(U)<=mathfrak A_K(U)`. For the quantitative form, suppose (6) holds. If `M` is bounded below by a fixed positive constant, (7) is trivial, so assume `M<=e^-2`.

For a small fixed `D>0`, put

\[
M_0
:=
D\frac{U^{-2B}}{(\log U)^2}.
\tag{20}
\]

For large `U`, the function `sqrt(x) log(e/x)` is increasing on `0<x<=M_0`, and

\[
\sqrt{M_0}\log\frac e{M_0}
\le
C_B\sqrt D\,U^{-B}.
\tag{21}
\]

If `M<=M_0`, (4) and (21) would give

\[
\mathfrak A_K(U)
\le
C C_B\sqrt D\,U^{-B}.
\tag{22}
\]

Choosing `D` so that `C C_B sqrt(D)<c` contradicts (6). This proves (7). Equation (8) follows because `U^eta/(log U)^2->infinity`.

The same conclusion follows from an algebraic signed value: if

\[
|\mathcal S_K(U)|\ge cU^{-B},
\tag{23}
\]

then (10) gives `mathfrak A_K(U)>=cU^-B/2`, so (7) applies.

## 4. The diffuse branch collapses into the strong-atom branch

The cancellation analysis beginning at `RE-124` deliberately separated two possibilities. One was a strong atom hidden by nearby spectral competition. The other was a putative diffuse cloud in which no individual coefficient was algebraically visible but many individually tiny coefficients collectively retained algebraic relevance.

Equation (4) removes the second possibility at the level that matters for the finite-edge residual. If

\[
M_K(U)=U^{-\omega(1)},
\tag{24}
\]

then

\[
\mathfrak A_K(U)=U^{-\omega(1)},
\qquad
\mathcal S_K(U)=U^{-\omega(1)}.
\tag{25}
\]

Thus a superalgebraic maximum does not hide an algebraic amount of unsigned coefficient mass. The full packet is itself superalgebraically negligible.

Conversely, whenever the finite-edge packet has algebraic absolute mass, (7) supplies a dominant algebraically strong atom. Fix `eta>0` and write

\[
A:=2B+\eta.
\tag{26}
\]

Then for large `U`, (8) places the packet in the strong-atom regime of `RE-129`. On any window `H=U^(1-theta)`, either

\[
\sup_{|u-U|\le H}|\mathcal S_K(u)|
>\epsilon_*M_K(U),
\tag{27}
\]

which is already an algebraic continuum excursion, or the opposite inequality holds and `RE-129` forces a distinct companion with inverse-window spacing and cancelling center phase. If `A<K+1`, the excursion alternative is visible on the regular-CA phase mesh by `RE-123`.

The conclusion is therefore not that internal cancellation has disappeared. It is that **all algebraically relevant internal cancellation belongs to the strong-atom geometry already isolated by `RE-124`--`RE-129`**. There is no separate algebraic many-weak-mode regime left to analyze in the attained finite-edge branch.

## 5. Adversarial audit

The main failure modes were checked directly.

First, the infinite zero set cannot invalidate the interpolation: the high-height contribution is controlled by the summable `1/(1+gamma^2)` envelope, not by a finite truncation. Second, no zero-density theorem near `Theta` is used; counting every nontrivial zeta zero only enlarges the relevant sets and the classical bound `N(T)<<T log T` is enough. Third, multiplicities are already included in `N(T)`, so a high-multiplicity ordinate cannot bypass (18)--(19).

Fourth, (4) concerns absolute coefficient mass and does not assume random phases or infer a sign from an unsigned estimate. It only says that algebraic unsigned mass contains an algebraic atom. The signed cancellation problem remains exactly the one handled by `RE-124`--`RE-129`. Fifth, the argument does not require horizontal isolation of the finite edge: `beta` enters only through the damping factor, which is at most one, and the uniform fixed-strip comparison (12).

Finally, the exponent doubling in (7) is kept explicit. The result does not claim that algebraic packet mass of order `U^-B` contains an atom of the same order; the elementary maximum-versus-tail interpolation guarantees the weaker but sufficient `U^-2B/(log U)^2` scale. No stronger exponent is used in the CA transfer.

No material objection survives these checks, so no `.review.md` sidecar is opened.

## 6. Prior-art boundary

The ingredients behind (13)--(19) are classical. Riemann--von Mangoldt gives the zero count, and the resulting absolute summability of weights of order `1/gamma^2` is elementary. The existing Montgomery--Vaughan classical zeta anchor in `SOURCES.md` is sufficient; no new external theorem is load-bearing and no source-list change is required.

A targeted literature audit also checked the neighboring modern zero-geometry direction. Bui--Goldston--Milinovich--Montgomery study small gaps and spacings, and Maynard--Pratt study vertical isolation and zero-density consequences. Those works confirm that close-zero geometry is established prior art, but neither addresses this Robin/CA packet's deterministic maximum-versus-absolute-mass interpolation. Recent work on simplicity and critical-line proportions likewise does not rule out the sparse off-critical configurations relevant under the false-RH finite-edge hypothesis.

No novelty is claimed for `sum (1+gamma^2)^-1<infinity`, for Riemann--von Mangoldt, or for balancing a counting bound against a decaying envelope. The line-specific result is the splice with the exact finite-edge coefficients: **the purported diffuse algebraic escape in the Robin/CA subedge packet collapses into the already-isolated strong-atom branch**.

## 7. Research effect

`RE-124` introduced the strong-atom/diffuse-cloud split because spectral localization starts from one algebraically visible atom. `RE-125`--`RE-129` then made the strong branch progressively rigid but deliberately left the diffuse branch untouched. The summable `1/gamma^2` coefficient geometry shows that this second branch was too pessimistic: algebraic packet mass cannot be assembled from exclusively superalgebraic atoms.

Within the attained finite-edge branch, the live algebraic obstruction is therefore narrower. After `RE-130`, an algebraically relevant packet always enters the strong-atom regime, and persistent hiding reduces to the dominant inverse-window cancelling-pair geometry of `RE-129`. The remaining separate frontiers are the actual exclusion of those off-critical pair configurations, the nonattained-edge branch, and the endpoint `Theta=1`.