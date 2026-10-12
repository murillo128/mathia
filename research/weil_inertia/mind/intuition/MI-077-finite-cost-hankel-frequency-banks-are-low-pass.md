# MI-077 — Finite-cost Hankel frequency banks compress to a shallow-blind low-pass multiplier

**Evidence level:** exact source-grounded synthesis from [WI-438](../../findings/WI-438-shallow-hankel-coercivity-requires-scale-matched-boundary-oscillation.md) and [WI-441](../../findings/WI-441-finite-cost-hankel-frequency-banks-are-shallow-blind.md).

Let `H_omega=P_- M_(exp(-i omega t))|H_+` for `omega>0`, with a positive source-fixed frequency measure `mu`. The positive quadratic bank is
`Q_mu(u)=int ||H_omega u||_2^2 dmu(omega)=int_0^infty W_mu(xi)|u_hat(xi)|^2 dxi`,
where `W_mu(xi)=mu((xi,infty))` is nonincreasing. Thus an arbitrarily large **positive** family of shifted noncompact Hankel operators has only a *single low-pass multiplier* as its quadratic observable.

For the normalized shallow Kunik Hardy packet `u_(r,gamma)`,
`Q_mu(u_(r,gamma))=F_mu(r)=int (1-exp(-2r omega)) dmu(omega)`,
independent of `gamma`. If `F_mu(r_0)<infinity` at one positive scale, equivalently `int min(1,omega)dmu(omega)<infinity`, then dominated convergence gives `F_mu(r)->0` as `r->0`, uniformly in the zero ordinate. Any bounded non-diagonal mixing has quadratic response bounded by `||B||F_mu(r)` and vanishes too. A depth-adapted tone `omega~1/r` can remain sensitive, but integrating all such tones with finite fixed packet cost cannot.

The negative result concerns positive fixed pure-frequency banks and bounded output operations, not arbitrary rough Hankel symbols or an operator with a justified depth-dependent unbounded renormalization. The specific remaining requirement is a source-fixed coupling whose **packet-scale** response stays nonzero without spending infinite energy or reading the hypothetical zero depth.
