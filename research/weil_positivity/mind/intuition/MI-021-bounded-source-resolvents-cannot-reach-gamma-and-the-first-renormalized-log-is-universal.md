# MI-021 — Bounded source resolvents cannot reach Gamma; the first renormalized logarithm is density-universal

**Evidence level:** exact for the bounded-resolvent obstruction and the pole-normalized Mangoldt Herglotz asymptotic in [WP-304](../../findings/WP-304-bounded-source-resolvents-are-too-small-pole-normalized-mangoldt-energy-yields-only-an-oriented-universal-logarithmic-herglotz-tail.md). The Herglotz/Nevanlinna representation, Mertens weighted estimates and digamma asymptotics used there are classical. No Weil-positivity theorem or derivation of the exact Gamma factor is claimed.

WP-303 left a source-forced nonlocal resolvent/boundary transform as one of the few ways to escape singular fixed-source projector motion. WP-304 splits that route by spectral-mass class.

For any self-adjoint source operator `H` and bounded incidence/compression `V`,

`M_V(z)=V^*(H-z)^(-1)V`

is Herglotz, its compressed spectral measure has finite total mass `V^*V`, and

`||M_V(iy)|| <= ||V||^2/y`.

So ordinary bounded source incidence is categorically too small at high energy: it decays and cannot produce the logarithmically growing Gamma/digamma scale. Replacing a spectral cut by a bounded resolvent does not evade the archimedean-growth obstruction.

The pole-normalized positive-energy Mangoldt measure

`mu_+ = sum_(n=p^k) Lambda(n)/(n+1) delta_(log n)`

has instead `mu_+([0,R])=R+O(1)`. Its total mass is infinite but it satisfies the Nevanlinna integrability condition. After the canonical subtraction, the regularized Herglotz transform obeys

`Re m_+(iy)=-log y+O(1)`,

`Im m_+(iy)=pi/2+O(1/y)`.

This crosses the finite-mass barrier, but the leading logarithm is not arithmetic-specific. The proof depends only on cumulative density `R+O(1)`: every positive measure with that density has the same first asymptotic, and Lebesgue measure is an exact matched control. The first logarithm therefore records **spectral density**, not the Riemann Gamma sector.

There is a second gate. The canonical explicit-formula carrier is the even measure `mu_+ + check(mu_+)`. Pairing `+E` and `-E` makes its resolvent response on `iy` purely imaginary, so the real logarithm cancels exactly. The apparently promising log survives only after selecting the positive-energy orientation before evenization.

The useful source question has therefore moved from “can a positive source transform grow like `log y`?” to a more constrained conjunction: what source law forces the one-sided orientation, the infinite-mass renormalization/subtraction, and a **nonuniversal subleading response** carrying the exact Gamma/pole information, while preserving a separate positivity mechanism? A generalized boundary map, scattering object or regularized determinant can lie outside the bounded-resolvent theorem, but it must explain those choices rather than encode the target by representation freedom.

**Boundary.** WP-304 does not rule out unbounded boundary maps, boundary relations, scattering matrices, determinants/log-determinants, domain-changing couplings or genuinely varying noncommuting operators. Nor does it say that every source-native infinite-mass transform is universal. It proves a sharper diagnostic: bounded compression cannot reach the scale, and the first natural infinite-mass escape reaches only a universal oriented logarithm whose real part disappears under canonical evenization.