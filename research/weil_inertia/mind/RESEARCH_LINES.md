# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Resolve cross-scale incidence inside the rare upper host family, not in the global lower reservoir

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`, `MI-021-complete-screening-promotes-support-avoidance-to-prime-deleted-spectral-criticality`, `MI-022-fixed-finite-prime-power-screening-cannot-buy-prime-deleted-spectral-coercivity`, `MI-023-nearest-prime-width-has-a-lambert-w-spectral-endpoint`.

WI-284 supplies the operator target: complete one-signed screening forces the prime-deleted gamma-plus-pole form to have bottom exactly zero. WI-288 shows that the symmetric two-island screening family is exactly the nearest-prime-power Lambert gap condition, and WI-289 decomposes it into root-scale prime gaps. Prime squares are the unique critical composite layer; all `k>=3` layers are subunit at the root scale.

WI-290 proves that the composite-safe residual has at least `X^(3/8-o(1))` positive-length components on `[X,2X]`. WI-291 supplies the opposite upper-scale sparsity: the ordinary-prime Lambert threshold confines eligible centers to total length `O(X^(3/5+epsilon))` and at most `O(X^(1/10+epsilon)/log X)` giant ordinary-prime gap hosts.

WI-292 localizes these two facts against each other. After enlarging the rare upper hosts by one Lambert radius, elementary spacing of integer powers shows that only

`O_(c,epsilon)(X^(1/10+epsilon))`

composite prime-power neighborhoods can cut them. Consequently the full screened candidate set `F_c(X)=A_c(X) intersect R_c(X)` has at most `O(X^(1/10+epsilon))` connected components, and at most that many positive-length composite-safe components can meet the ordinary-prime safe set at all.

Compared with the global `X^(3/8-o(1))` composite-safe reservoir, only an `X^(-11/40+o(1))` fraction of its positive-length components can even enter an eligible upper host. This is deterministic and requires no cross-scale independence hypothesis. It closes the idea that more global lower safe windows, or a sharper count of them, can force a candidate by abundance.

What remains is much smaller and more arithmetic: determine whether any of the `X^(1/10+o(1))` host-localized candidate pieces actually survive all prime-power cuts infinitely often, or prove that the actual upper/lower prime incidence excludes them. The relevant theorem must work **inside the rare host family**. A cross-scale correlation/avoidance law, null-equation amplitude/sign information, or a different support topology could still close the branch.

## Keep support screening, global reservoir topology, host localization, surviving candidate incidence, null amplitudes and sign geometry separate

WI-290 rigidifies the topology of the global composite-safe reservoir. WI-291 rigidifies the rarity of the ordinary-prime hosts. WI-292 shows that almost all lower safe components are deterministically irrelevant after localization: only `X^(1/10+o(1))` can meet an eligible host.

This is still not an exclusion theorem. A polynomially tiny subfamily can contain infinitely many survivors, and no cross-scale decorrelation has been proved. Many-component supports, sign-changing modes and incomplete screening remain different geometries and must not inherit the two-island reduction without a new proof.