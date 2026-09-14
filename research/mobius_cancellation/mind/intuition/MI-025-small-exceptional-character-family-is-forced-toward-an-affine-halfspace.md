# MI-025 — A small exceptional character family is forced toward an affine halfspace

**Evidence level:** exact finite Fourier consequence of [MC-289](../../findings/MC-289-odd-moment-character-bias-from-collision-rich-shells.md) and [MC-290](../../findings/MC-290-odd-moment-exception-set-near-affine-rigidity.md). The statement is an interface theorem for the collision-rich odd shell; it supplies no new character-sum estimate or bound for `M(x)`.

Let `eta=N^2/(2^r sum_s n_s^2)` be the effective occupancy and let `A_lambda` be the generated quadratic-character shell sums. When short odd relations up to weight `t` are absent, MC-289 gives exact odd moments. MC-290 shows how those moments constrain an analytic theorem that controls all but `J` characters.

If for an odd `m<=t` every nonexceptional character obeys

`A_lambda/N >= -delta`,

and `a_lambda=-A_lambda/N` on the exceptional set `E`, then

`1-sum_(lambda in E) a_lambda^m <= delta^(m-2) (1/eta - 1 - sum_(lambda in E) a_lambda^2)`.

Writing `epsilon_m=delta^(m-2)(1/eta-1)`, some exceptional character satisfies

`-A_lambda/N >= ((1-epsilon_m)/J)^(1/m)`.

Thus if `epsilon_m=o(1)` and `log J=o(m)`, one exceptional generated character is `-1` on a `1-o(1)` fraction of the weighted shell. The residual escape is not an arbitrary uncontrolled mode: it is quantitatively close to the exact affine obstruction.

At the natural Geelen-scale occupancy `eta~t 2^-t`, taking `m=t` exposes a sharp one-sided threshold. With one exception and `delta=1/2`, the exceptional character's positive-side shell mass is only `O(t^-2)`; any fixed `delta<1/2` makes the approach to the affine endpoint exponentially stronger.

The reusable interface is therefore: **family cancellation with a small exceptional set converts finite-geometric odd-girth information into near-affine concentration.** Future arithmetic input can attack the size of the exceptional family, the one-sided threshold, the effective occupancy, or the impossibility of such concentration for the actual Legendre shell, rather than trying to control every generated character uniformly.

**Boundary.** The conclusion depends on the exact odd-moment identities and on `eta` not being too small. It does not exclude the affine endpoint, prove a lower bound on `eta`, control conductor, or supply the required exceptional-character theorem.