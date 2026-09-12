# MI-005 — Stable tails are global continuation phenomena constrained by source branching and persistent far Gram mass

**Evidence level:** supported by the causal/stable-tail theorems NB-063--NB-066, finite Schur characterization NB-067, boundary-chain control NB-068, and source-specific branching restrictions NB-069--NB-070; no bounded certificate for the actual Nyman source is yet proved.

NB-066--NB-067 show that a hypothetical persistent Nyman target is a global continuation problem. Its finite traces are natural, but the least compatible future norm diverges; finite normalized Schur complements converge to that continuation cost and therefore provide a source-only certificate.

NB-068 proves that canonical one-cell memory is not a substitute. A nearest-neighbor scalar chain can have `Gamma_R=0` at every step and still carry a stable boundary mode with divergent continuation cost. NB-069 then adds the exact source covariance missing from that control: integer-dilation branching sends each coarse innovation isometrically to a normalized consecutive block of finer innovations, inducing exact Gram block-renormalization identities. Under uniform norm bounds, fixed finite-band nonorthogonality is incompatible with that branching law.

NB-070 closes the obvious rapidly decaying long-range escape as well. For branching factor `m` and `q=m^r`, every coarse correlation obeys the exact descendant-block mass inequality

`sum_(k in I_i^q) sum_(l in I_j^q) |G_kl| >= q |G_ij|`.

If

`omega(L)=sup_k sum_(|l-k|>=L) |G_kl|`,

then uniformly bounded exact-branching innovations satisfy

`omega(L)->0  =>  G_ij=0 for i!=j`.

Equivalently, every nonorthogonal source in this class has `lim_(L->infty) omega(L)>0`: an order-one amount of aggregate absolute Gram mass must persist arbitrarily far from the diagonal. A matched obstruction cannot be repaired by replacing the forbidden tridiagonal chain with a uniformly summable polynomially/exponentially decaying tail.

This still does not settle the stable tail. The branching identities and Schur complements retain signs/phases, while `omega(L)` uses absolute mass. Large forced far mass may cancel in block averages, and poor Schur conditioning need not be read from one row-tail statistic. The remaining theorem is therefore **signed**: combine positive-semidefiniteness and exact block renormalization with the NB-067 finite Schur certificates, rather than approximate the canonical Gram matrix by a localized one.

The reusable distinction is now five-way: one-cell memory can vanish, global continuation can remain expensive, source branching can exclude cheap finite-band controls, branching can force persistent far absolute mass in every nonorthogonal bounded control, and the signed finite Schur geometry still decides whether that mass sustains a stable tail.

**Boundary.** NB-070 does not prove the actual Nyman stable tail is zero, bound the Schur certificates, or exclude nonorthogonal mechanisms with persistent far mass or unbounded innovation norms.