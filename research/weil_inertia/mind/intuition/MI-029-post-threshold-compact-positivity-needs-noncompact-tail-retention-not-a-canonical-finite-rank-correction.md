# MI-029 — Post-threshold compact positivity needs noncompact tail retention, not a canonical finite-rank correction

**Evidence level:** exact operator-level conclusion from [WI-303](../../findings/WI-303-finite-rank-tail-rank-is-noncanonical.md), using the source-exact tail architecture recorded in [WI-302](../../findings/WI-302-liu-source-exact-certificate-claims-positivity-through-17-16.md). The external `17/16` certificate itself remains pending independent replay.

WI-302 suggested a tempting structural story: once the compact localization passes the `log 8 / 2` threshold where tail-dropping fails, perhaps the positive rank-two correction appearing in Liu's block-Schur certificate is the minimal new invariant. WI-303 rules out that interpretation.

If `S>=0` and `V` spans any finite trial subspace with nonsingular Gram matrix `G=V^*SV`, then

`0 <= S V G^-1 V^* S <= S`.

Thus a positive operator supplies finite-rank Loewner minorants of whatever rank the chosen trial subspace has. In Liu's source-exact decomposition the displayed rank-two term is precisely such an under-filled minorant of the stronger positive tail `C(I-B_band)`. Rank zero, one, two and higher extractions are all structurally available; rank two is a certificate-design choice rather than an invariant of the post-threshold problem.

The source's compact-repair obstruction identifies the genuine boundary. After the simpler localization drops the relevant tail, no fixed compact self-adjoint correction can restore positivity beyond the threshold. Every finite-rank correction is compact, so the rank-two term by itself cannot evade that theorem. The retained source-exact tail operator is instead noncompact because it contains an identity component.

The relevant dichotomy is therefore

**tail dropped + fixed compact repair** versus **source-exact noncompact positive tail retained before finite-dimensional extraction**.

Once the noncompact supplier is present, the finite trial subspace may be optimized for numerical or Schur efficiency without being mistaken for the mathematical mechanism.

This also clarifies what independent replay must test. Removing one rank-one term from the author package may or may not destroy positivity of its specific `N=448` matrix; that is a finite-certificate question. It cannot establish rank-one impossibility as a structural theorem, because the underlying positive tail admits rank-one minorants exactly. Conversely, `T_tail>=tau I` does not by itself prove the package works without the selected vectors.

**Boundary.** WI-303 does not validate Liu's claimed positivity through `17/16`, its coercivity constant, or its analytic transfer. It proves only the operator-structural statement that finite-rank tail rank is noncanonical and that the known post-threshold compact-repair obstruction can only be escaped by retaining noncompact tail information or changing the architecture.