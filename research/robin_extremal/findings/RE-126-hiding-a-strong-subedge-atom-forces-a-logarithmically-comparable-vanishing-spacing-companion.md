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

for fixed `c>0`, and let `c_*>0` be the inner-radius constant from `RE-125`. Define

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

Then there are constants `epsilon_*>0`, `c_1>0`, and `U_0` depending only on the fixed parameters such that, whenever `U>=U_0` and

\[
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
\le
\epsilon_*|a_{\rho_0,K}(U)|,
\tag{5}
\]

there exists a zero

\[
\rho_1=\beta_1+i\gamma_1
\in\mathcal A_\eta(\rho_0;U)
\tag{6}
\]

with

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

Consequently, for every fixed `epsilon>0`,

\[
|a_{\rho_1,K}(U)|\gg_\epsilon U^{-A-\epsilon},
\tag{8}
\]

while

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

Thus the comparable annular mass required by `RE-125` cannot be hidden in an arbitrarily large population of individually negligible local modes. A hidden strong atom forces a **distinct-ordinate, logarithmically comparable, algebraically strong companion** in the same shrinking horizontal edge layer.

Along any unbounded sequence of hidden strong atoms, the target ordinates tend to infinity and

\[
\boxed{
|\gamma_1-\gamma_0|\log(2+\gamma_0)\longrightarrow0.
}
\tag{11}
\]

Hence the strong-atom branch requires an actual near-edge zero pair whose separation is vanishingly small relative to the conventional local `1/log gamma` spacing scale. The pair need not be consecutive, and the theorem gives a necessary condition for cancellation, not a sufficient one.

When `A<K+1`, absence of such a companion forces the continuum excursion supplied by `RE-125`, which `RE-123` transfers to actual regular CA states. The separate diffuse-cloud branch, where no individual atom satisfies (3), remains open.

## 1. Only logarithmically many zeros can occupy the annulus

The single-atom estimate already proved in `RE-124` gives

\[
\Theta-\beta_0\ll_A\frac{\log U}{U},
\qquad
\gamma_0\ll_A U^{A/2}.
\tag{12}
\]

Because `eta<1`, the annulus (4) is contained, for large `U`, in `|gamma-gamma_0|<1`. The classical Riemann--von Mangoldt formula

\[
N(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+O(\log(2+T))
\tag{13}
\]

therefore implies, with zeros counted with multiplicity,

\[
\boxed{
\#\mathcal A_\eta(\rho_0;U)
\ll
\log(2+\gamma_0)
\ll_A
\log U.
}
\tag{14}
\]

This uses only a fixed-window upper bound. No unit-interval asymptotic, zero-density theorem, pair-correlation statement, or lower gap bound is assumed. Counting all nontrivial zeros only enlarges the subedge annulus and therefore gives a valid upper bound for (4).

## 2. The RE-125 mass condition forces one strong companion

`RE-125` gives

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
\tag{15}
\]

Choose `epsilon_*>0` with `C epsilon_*<1/4`. Because (3) turns the final term into `o(|a_{rho_0,K}(U)|)`, the hidden-packet hypothesis (5) implies

\[
\sum_{\rho\in\mathcal A_\eta(\rho_0;U)}
|a_{\rho,K}(U)|
\ge
c_2|a_{\rho_0,K}(U)|
\tag{16}
\]

for some fixed `c_2>0` and all sufficiently large `U`. Pigeonholing (16) through the cardinality bound (14) gives (7). The lower radius `c_*/U` in (4) guarantees `gamma_1!=gamma_0`, so multiplicity of the target cannot serve as this companion.

The coefficient comparability from `RE-124`,

\[
|a_{\rho,K}(U)|
\asymp_K
\frac{e^{-(\Theta-\beta)U}}{1+\gamma^2},
\tag{17}
\]

turns (7) into the horizontal estimate in (9): since the denominator is at least one,

\[
e^{-(\Theta-\beta_1)U}
\gg
\frac{U^{-A}}{\log U},
\]

hence

\[
\Theta-\beta_1
\le
\frac{A\log U+\log\log U+O(1)}{U}.
\tag{18}
\]

The ordinate estimate follows even more directly from (10) and the target bound in (12): `gamma_1=gamma_0+o(1)<<_A U^(A/2)`. Thus target and companion occupy the same polynomial-height edge layer.

## 3. The pair is asymptotically much closer than the normalized spacing scale

Equations (10) and (12) give

\[
|\gamma_1-\gamma_0|\log(2+\gamma_0)
\ll_A
U^{-1+\eta}\log U
=o(1),
\tag{19}
\]

which is (11).

The target ordinates must escape to infinity along any unbounded sequence `U_j` satisfying (3). Otherwise they would range over a compact region containing only finitely many zeta zeros. Every fixed subedge zero has `Theta-beta>0`, so its coefficient in (1) decays exponentially in `U` and eventually becomes smaller than `U^-A`, contradicting (3).

The quantifiers in `eta` remain exactly those of `RE-125`: for every fixed `eta>0`, a hidden atom forces some companion in the corresponding annulus. That companion may depend on `eta`. No uniform exact `O(1/U)` companion theorem is claimed.

## 4. CA consequence and surviving obstruction

The theorem has a quantitative contrapositive. If every zero in (4) has coefficient smaller than the threshold `c_1|a_{rho_0,K}(U)|/log U` fixed above, then (5) cannot hold. Therefore

\[
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
\gg
|a_{\rho_0,K}(U)|
\gg U^{-A}.
\tag{20}
\]

When `A<K+1`, the superalgebraically fine regular-CA phase mesh from `RE-123` samples this continuum excursion at the same algebraic scale. Hence a strong target without a logarithmically comparable annular companion produces an actual CA residual excursion.

The strong-atom branch is therefore much narrower than after `RE-125`: cancellation requires at least one near-edge companion of almost the same algebraic strength and with vanishing normalized ordinate spacing. What remains genuinely different is the diffuse branch, where the full packet has algebraic size but no single coefficient reaches the strong-atom threshold (3).

## 5. Representation and adversarial audit

No new source coordinate is introduced. The proof uses the same signed subedge packet of `RE-121`--`RE-125`, the single-atom location estimate from `RE-124`, the annular mass necessity from `RE-125`, and the classical zero-counting function `N(T)`.

The main adversarial checks are these. The Riemann--von Mangoldt formula is used only for the upper bound (14), so its `O(log T)` remainder is sufficient; no false fixed-window asymptotic is needed. Multiplicity cannot fake the companion because equal ordinates lie inside the reinforcing inner ball excluded from (4). Pigeonholing absolute mass proves only that a large companion exists; it does not assert that this companion alone supplies the cancelling phase. The argument starts from an individually strong atom and therefore does not collapse the separate diffuse-cloud branch. Finally, constants may deteriorate as `eta->0`, so (10) is not silently upgraded to a uniform exact reciprocal-gap theorem.

A separate adversarial pass over the local zero count, multiplicity, pigeonhole step, coefficient-to-edge conversion, normalized spacing, and CA transfer found no material objection, so no `.review.md` sidecar is opened.

## 6. Prior-art boundary

The only classical input newly used in the derivation is the Riemann--von Mangoldt zero count, through the weak consequence that a bounded ordinate interval contains `O(log T)` zeros near height `T`. The existing Montgomery--Vaughan classical zeta reference in `SOURCES.md` is sufficient for this standard input, so no new bibliography anchor is needed.

The nearest modern neighbors found in the targeted audit are Bui--Goldston--Milinovich--Montgomery, *Small gaps and small spacings between zeta zeros* (Acta Arithmetica **210** (2023), 133--153, DOI `10.4064/aa220731-15-2`), and Maynard--Pratt, *Half-isolated zeros and zero-density estimates* (arXiv:2206.11729). They establish that small-spacing and vertical-isolation questions are established prior-art domains; they do not provide this Robin/CA implication. In particular, the forced pair here may be off the critical line and need not be consecutive.

The claim specific to this line is the splice of `RE-125`'s annular mass requirement with the local zeta zero count: **hiding one algebraically strong finite-edge atom forces a second logarithmically comparable near-edge atom at vanishing normalized ordinate separation**. The targeted audit found no prior theorem asserting this necessary pair geometry for the finite-edge Robin/CA residual.

## 7. Research effect

`RE-125` left the strong-atom obstruction as reciprocal-annular coefficient mass. `RE-126` turns that mass condition into a pairwise zero-geometry requirement. At the polynomial heights forced by algebraic visibility there are only logarithmically many zeros available locally, so the needed mass cannot be diluted among a huge number of tiny nearby coefficients.

The next strong-atom question is now concrete: whether an attained off-critical edge can support infinitely many algebraically strong near-edge pairs with normalized ordinate gaps tending to zero and with the phase relation needed to suppress the Robin residual. Existing spacing results do not rule out that off-line, nonconsecutive configuration. The genuinely diffuse global packet remains a separate obstruction and requires a different argument.