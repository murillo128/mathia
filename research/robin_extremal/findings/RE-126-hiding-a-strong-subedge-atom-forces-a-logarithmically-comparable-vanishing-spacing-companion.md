# RE-126 — hiding a strong subedge atom forces a logarithmically comparable vanishing-spacing companion

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SPECTRAL-LOCALIZATION + LOCAL-ZERO-COUNT + ZERO-PAIR-NECESSITY + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-125`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix `K>=0`, `A>0`, and `0<eta<1`. For a positive-ordinate subedge zero

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\qquad
\gamma>0,
\]

write, as in `RE-124`--`RE-125`,

\[
a_{\rho,K}(u)
:=
 e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right],
\tag{1}
\]

and

\[
\mathcal S_K(u)
=
2\Re
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
 a_{\rho,K}(u)e^{i\gamma u}.
\tag{2}
\]

Let `rho_0=beta_0+i gamma_0` satisfy

\[
|a_{\rho_0,K}(U)|\ge cU^{-A}
\tag{3}
\]

for a fixed `c>0`, and let `c_*>0` be the inner-radius constant from `RE-125`. Define the reciprocal annulus

\[
\mathcal A_\eta(\rho_0;U)
:=
\left\{
\rho\ne\rho_0:
\sigma_0\le\Re\rho<\Theta,
\ \Im\rho>0,
\ \frac{c_*}{U}<|\Im\rho-\gamma_0|\le U^{-1+\eta}
\right\}.
\tag{4}
\]

Then there are constants `epsilon_*>0`, `c_1>0`, and `U_0` depending only on the fixed parameters such that, whenever `U>=U_0` and the strong atom is hidden on the `RE-125` observation window in the sense that

\[
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
\le
\epsilon_*|a_{\rho_0,K}(U)|,
\tag{5}
\]

there exists a **distinct-ordinate companion zero**

\[
\rho_1=\beta_1+i\gamma_1
\in\mathcal A_\eta(\rho_0;U)
\tag{6}
\]

such that

\[
\boxed{
|a_{\rho_1,K}(U)|
\ge
c_1\frac{|a_{\rho_0,K}(U)|}{\log U}
\gg
\frac{U^{-A}}{\log U}.
}
\tag{7}
\]

In particular, for every fixed `epsilon>0`,

\[
|a_{\rho_1,K}(U)|\gg_{\epsilon}U^{-A-\epsilon}
\tag{8}
\]

for all sufficiently large `U`. Thus the annular mass required by `RE-125` cannot be spread over polynomially or exponentially many individually negligible neighbors: a hidden strong atom forces at least one logarithmically comparable algebraically strong companion.

Moreover,

\[
\boxed{
\Theta-\beta_1
\le
\frac{A\log U+\log\log U+O(1)}{U},
\qquad
\gamma_1\ll_A U^{A/2},
}
\tag{9}
\]

and

\[
\boxed{
\frac{c_*}{U}
<
|\gamma_1-\gamma_0|
\le
U^{-1+\eta}.
}
\tag{10}
\]

Along any unbounded sequence of hidden strong atoms, the target ordinates tend to infinity and the conventional local-spacing normalization satisfies

\[
\boxed{
|\gamma_1-\gamma_0|\,\log(2+\gamma_0)
\longrightarrow 0.
}
\tag{11}
\]

Hence the strong-atom branch of the finite-edge obstruction requires not merely annular coefficient mass but an actual pair of algebraically strong near-edge zeros whose ordinate separation is vanishingly small relative to the usual `1/log gamma` zero-spacing scale. The pair need not be consecutive, and (7)--(11) are necessary conditions for hiding the target, not sufficient cancellation criteria.

When `A<K+1`, failure of (6)--(7) forces the continuum excursion supplied by `RE-125`, and `RE-123` transfers that excursion to actual regular CA states. The separate diffuse-cloud branch, in which no individual atom satisfies (3), remains open.

## 1. The RE-125 annulus contains only `O(log U)` zeros

The single-atom estimate already proved in `RE-124` gives, uniformly for every atom satisfying (3),

\[
\Theta-\beta_0\ll_A\frac{\log U}{U},
\qquad
\gamma_0\ll_A U^{A/2}.
\tag{12}
\]

Because `eta<1`, for large `U` the annulus (4) lies inside the unit ordinate window

\[
|\gamma-\gamma_0|<1.
\tag{13}
\]

The classical Riemann--von Mangoldt formula

\[
N(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+O(\log(2+T))
\tag{14}
\]

therefore gives, with zeros counted with multiplicity,

\[
\#\mathcal A_\eta(\rho_0;U)
\le
N(\gamma_0+1)-N(\max\{0,\gamma_0-1\})
\ll
\log(2+\gamma_0)
\ll_A
\log U.
\tag{15}
\]

No zero-density theorem and no lower bound for zero gaps is used. The estimate counts **all** nontrivial zeros in the unit window, so it remains an upper bound after restricting to the subedge strip in (4).

## 2. Comparable annular mass collapses to one strong companion

`RE-125` proves that there is a constant `C` such that

\[
|a_{\rho_0,K}(U)|
\le
C\left[
\sup_{|u-U|\le U^{1-\eta/2}}|\mathcal S_K(u)|
+
\sum_{\rho\in\mathcal A_\eta(\rho_0;U)}
|a_{\rho,K}(U)|
\right]
+o(U^{-A}).
\tag{16}
\]

Choose `epsilon_*>0` so that `C epsilon_*<1/4`. Since (3) makes `o(U^-A)=o(|a_{rho_0,K}(U)|)`, for sufficiently large `U`, (5) and (16) imply

\[
\sum_{\rho\in\mathcal A_\eta(\rho_0;U)}
|a_{\rho,K}(U)|
\ge
c_2|a_{\rho_0,K}(U)|
\tag{17}
\]

for a fixed `c_2>0`.

Combining (15) and (17), one member of the annulus must satisfy

\[
|a_{\rho_1,K}(U)|
\gg
\frac{|a_{\rho_0,K}(U)|}{\log U},
\tag{18}
\]

which is (7). The lower radius in (4) makes `gamma_1!=gamma_0`, so this is a genuinely distinct ordinate rather than multiplicity of the target zero. Equation (8) follows from `log U=o(U^epsilon)` for every fixed `epsilon>0`.

The coefficient comparability from `RE-124`,

\[
|a_{\rho,K}(U)|
\asymp_K
\frac{e^{-(\Theta-\beta)U}}{1+\gamma^2},
\tag{19}
\]

then gives the horizontal part of (9): from (7),

\[
e^{-(\Theta-\beta_1)U}
\gg
\frac{U^{-A}}{\log U},
\]

and hence

\[
\Theta-\beta_1
\le
\frac{A\log U+\log\log U+O(1)}{U}.
\tag{20}
\]

For the ordinate, (10) and (12) give directly

\[
\gamma_1
=
\gamma_0+O(U^{-1+\eta})
\ll_A U^{A/2}.
\tag{21}
\]

Thus the companion is not merely nearby: it lies in the same shrinking horizontal edge layer and at the same polynomial height scale as the target.

## 3. The forced pair has vanishing normalized spacing

From (10), (12), and fixed `eta<1`,

\[
|\gamma_1-\gamma_0|\log(2+\gamma_0)
\ll_A
U^{-1+\eta}\log U
=o(1),
\tag{22}
\]

which proves (11).

For an unbounded sequence `U_j`, the target ordinates cannot remain bounded. Indeed, a bounded ordinate range contains only finitely many zeta zeros. Every fixed subedge zero has `Theta-beta>0`, so its coefficient in (1) decays exponentially in `U` and eventually violates (3). Consequently `gamma_0(U_j)->infinity` along any such hidden strong-atom sequence.

The factor `log gamma` is the standard normalization associated with the local mean zero-spacing scale `1/log gamma`. Therefore (22) is a genuine small-spacing requirement. It is stronger than merely asking for two zeros in the same bounded ordinate interval, but it does **not** say that the pair is consecutive or that such pairs are impossible.

The statement also respects the non-uniformity in `eta`: for every fixed `eta>0`, hiding forces some companion in the corresponding annulus. The companion may depend on `eta`; no claim of one zero satisfying a uniform `U^{-1+o(1)}` bound is made.

## 4. Consequence for the CA frontier

Suppose (3) holds with `A<K+1`. If no companion satisfying (7) exists in the annulus (4), then (15) makes the total annular mass `o(|a_{rho_0,K}(U)|)` after any fixed logarithmic improvement strong enough to contradict (17). More directly, the contrapositive of (7) says that the hidden-packet condition (5) cannot hold. Hence

\[
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
\gg U^{-A}.
\tag{23}
\]

`RE-123` then supplies regular CA phases that sample this excursion with superalgebraic accuracy, producing actual CA residuals of the same order.

This separates the remaining finite-edge obstruction more sharply. In the strong-atom regime, cancellation now requires a **near-edge, algebraically strong, distinct-ordinate doublet at vanishing normalized spacing**. The old possibility that the necessary annular mass might be smeared across a huge number of individually tiny local atoms is excluded by the elementary local zero count. The genuinely diffuse branch remains different: it is still possible in principle that the total algebraic residual is assembled from many globally distributed atoms none of which reaches the threshold (3).

## 5. Representation and adversarial audit

No new source coordinate is introduced. The proof uses only the same signed subedge packet of `RE-121`--`RE-125`, the strong-atom location already derived in `RE-124`, the annular mass necessity of `RE-125`, and the classical zero-counting function `N(T)`.

The main adversarial checks are as follows.

First, the zero count is used only as an upper bound. The `O(log T)` error in the Riemann--von Mangoldt formula is fully sufficient to deduce an `O(log T)` count in a fixed-length interval; no false unit-interval asymptotic is assumed.

Second, multiplicity cannot fake the companion. Zeros at the same ordinate lie inside the reinforcing inner ball of `RE-125`, whereas (4) starts at the strictly positive radius `c_*/U`.

Third, (17) is an absolute-mass statement. Pigeonholing it proves the existence of a large companion coefficient but does not claim that this companion by itself cancels the target. Additional annular atoms may still be required for the correct phase geometry.

Fourth, the result does not turn the diffuse-cloud branch into a strong atom. It begins with the explicit hypothesis (3); a packet made from individually smaller coefficients remains outside the theorem.

Fifth, the normalized-gap conclusion is asymptotic only along an unbounded hidden-atom sequence. The discreteness of zeta zeros and exponential damping of every fixed subedge zero justify the required escape of `gamma_0` to infinity.

Sixth, the theorem keeps `eta>0` fixed. Constants from `RE-125` are allowed to deteriorate as `eta->0`, so no uniform exact `O(1/U)` companion theorem is inferred.

A separate adversarial pass over the local zero count, multiplicity, pigeonhole step, coefficient-to-edge conversion, normalized spacing, and CA transfer found no material objection, so no `.review.md` sidecar is opened.

## 6. Prior-art boundary

The only new classical input is the Riemann--von Mangoldt zero count, used through the weak unit-window consequence `N(T+1)-N(T-1)=O(log T)`. This is standard zeta-function theory and is covered by the classical Montgomery--Vaughan source already anchored in `SOURCES.md`; no new bibliography dependency is required.

The nearest modern neighbors in the targeted prior-art audit are the literature on unusually small zero spacings and Maynard--Pratt's work on half-isolated zeros. Bui--Goldston--Milinovich--Montgomery, *Small gaps and small spacings between zeta zeros* (Acta Arithmetica 210 (2023), 133--153, DOI `10.4064/aa220731-15-2`), studies small spacings and distinct zeros, with its principal positive-density statements under RH. Maynard--Pratt, *Half-isolated zeros and zero-density estimates* (arXiv:2206.11729), develops zero detectors sensitive to vertical isolation.

Those results prevent any broad novelty claim about small zero spacing or vertical isolation themselves. `RE-126` makes only the line-specific splice: **if the finite-edge Robin/CA packet hides one algebraically strong subedge atom, then the `RE-125` annular mass plus the local zeta zero count force a second logarithmically comparable near-edge atom at vanishing normalized ordinate separation**. A targeted search found no prior theorem asserting this necessary pair geometry for the Robin/CA finite-edge residual.

## 7. Research effect

`RE-125` left the strong-atom obstruction as reciprocal-annular coefficient mass. `RE-126` turns that mass condition into a pairwise geometric one. At the relevant polynomial heights there are only logarithmically many zeta zeros available in the annulus, so the packet cannot hide a strong target using a locally diffuse sea of arbitrarily weak neighbors.

The next strong-atom question is therefore concrete: can an attained off-critical edge support infinitely many pairs of near-edge zeros with algebraically strong coefficients and normalized ordinate gaps tending to zero, with the phase relation needed to suppress the Robin residual? Existing small-gap theory does not rule this out in the required off-line, nonconsecutive setting. In parallel, the genuinely diffuse global packet remains a separate obstruction and still requires a different argument.