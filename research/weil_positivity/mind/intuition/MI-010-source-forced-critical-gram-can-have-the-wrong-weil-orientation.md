# MI-010 — The source-forced critical Gram has the wrong Weil orientation, and post-formation positive weighting cannot repair it faithfully

**Evidence level:** exact Bost--Connes critical Gram, essential-spectrum obstruction, singular-trace classification, and faithful-metric congruence boundary through WP-230

## Core intuition

Matching the critical half-density, prime logarithmic scale, and a canonical positive source geometry is still not enough for Weil positivity. The sign theorem depends on orientation, and the current Bost--Connes finite-prime defect has the wrong orientation in a way stable under several natural post-processing categories.

The newest evidence closes two especially tempting repairs. Scalar singular traces cannot preserve the full critical source information, and a faithful positive metric inserted around the already-formed defect cannot change its sign. A viable completion must therefore alter the **relation that forms the defect**, not merely change how the same defect is measured afterward.

## Strongest justified principle

WP-216--WP-218 identify the source-forced critical Gram and its Weil-oriented defect. On each prime axis the defect is Toeplitz with a sign-changing continuous symbol, so its negative essential spectrum survives every compact/relatively compact self-adjoint correction. Finite baths and compact boundary repairs cannot orient the same bulk.

WP-227--WP-229 analyze the exact critical amplitudes and their positive square. The decreasing singular values satisfy `mu_n(A)~sqrt(log n/n)` for the linear carrier and `mu_n(B)~log n/n` for the quadratic bath. Orthogonal doubling then shows that **every** finite positive singular trace on the linear carrier vanishes. Squaring moves into a singularly traceable class, but the repeated-prime-power sector is trace class and every finite singular trace agrees with the prime-only block. Scalar singular-trace geometry therefore faces an exact fork: preserve the linear amplitudes and get no finite nonzero trace, or square to a traceable object that forgets the higher prime-power selector.

WP-230 closes faithful positive congruence more generally. For arbitrary positive self-adjoint `G`, possibly unbounded, the form `<G^{1/2}x,W_FG^{1/2}x>` is nonnegative exactly when the compression of `W_F` to the closure of `Ran G^{1/2}` is nonnegative. If `G` is faithful that range is dense, so both strict signs of the original defect survive. If `G` is nonfaithful, all sign-changing power comes from support selection rather than the positive weights inside the support.

## Program consequence

The next completion must change category **before or during formation of the sign-bearing relation**: a genuinely nontracial/operator-valued modular correspondence, asymmetric left/right spatial operation, noncongruential completely positive construction, active finite--archimedean incidence, distributional pairing, or another source-forced operation that changes the essential orientation while retaining the full Mangoldt tower.

Any support restriction must be derived independently from source geometry; otherwise it is the same sign-programming freedom already exposed by earlier quotient controls.

## Counterevidence / boundary

The results do not rule out asymmetric/noncongruential operations, operator-valued modular structures, unbounded domain-sensitive constructions that are not positive congruences of the same defect, or finite--archimedean coupling formed before scalarization. WP-230 classifies metric reweighting of the fixed defect, not every modular mechanism.

## Epistemic status

**Exact wrong-orientation obstruction with exhaustive scalar singular-trace and faithful positive-metric no-gos; a pre-scalarization relational sign-producing operation remains open.**

## Falsification criterion

Refute the prime-axis essential-spectrum calculation, produce a finite nonzero singular trace on the exact linear carrier contrary to WP-229, or find a faithful positive `G` making the WP-230 congruence nonnegative. A positive continuation should instead derive a source-forced operation that changes the defect itself and survives completed finite-prime/archimedean readout.