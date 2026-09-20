# VIS-330 — Wang real-axis power saving forces a zeta zero-free half-plane

## Claim

Let Wang's symmetric squared-von-Mangoldt source profile be

`S(x)=x^(-2) sum_(n<=x) n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`

as in `VIS-292`, and put

`R(x)=S(x)-log x`.

Suppose that for some fixed `delta>0`,

`R(x)=O(x^(-delta))`

as `x->infinity`. Then the Riemann zeta function has no nontrivial zero `rho` with

`Re(rho)>max(1/2,1-delta)`.

Consequently:

- if `0<delta<1/2`, this pointwise power saving already forces the fixed zero-free half-plane `Re(s)>1-delta`;
- if `delta>=1/2`, it forces the absence of every nontrivial zero with `Re(s)>1/2`, and hence RH by the functional-equation symmetry.

Thus a fixed-power improvement of Wang's real-axis source remainder is not a cheap strengthening of the Korobov--Vinogradov envelope. Every exponent `delta>0` purchases a fixed zeta zero-free strip, and the square-root exponent reaches the RH boundary.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-MELLIN-PRINCIPLE + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

This is a one-way implication. It does not prove a converse from a zero-free half-plane to the stated remainder, does not produce any new zero-free region, and does not show that all subpower improvements over `VIS-291` are RH-equivalent.

## 1. Tail Mellin transform of the real-axis remainder

Write

`D(s)=sum_(n>=2) Lambda(n)^2 n^(-s)`.

`VIS-292` gives, initially for `0<Re(w)<2`,

`integral_0^infinity S(x)x^(-w-1) dx = [4/(4-w^2)] D(1+w)`.

For `0<x<1`, every integer `n>=2` lies in the second branch of the source profile, so exactly

`S(x)=C x^2`,

where

`C=sum_(n>=2) Lambda(n)^2/n^3=D(3)`.

Hence

`integral_0^1 S(x)x^(-w-1)dx = C/(2-w)`

for `Re(w)<2`. Also, for `Re(w)>0`,

`integral_1^infinity (log x)x^(-w-1)dx = 1/w^2`.

Therefore the tail transform

`F(w)=integral_1^infinity R(x)x^(-w-1)dx`

satisfies, initially on `0<Re(w)<2`,

`F(w) = [4/(4-w^2)]D(1+w) - C/(2-w) - 1/w^2`.

The terms subtracted here are explicit endpoint/main-term contributions. They do not depend on the nontrivial zeta zero divisor.

## 2. A power remainder makes the tail transform holomorphic farther left

If

`R(x)=O(x^(-delta))`,

then for every compact subset of `Re(w)>-delta`, the defining integral for `F(w)` converges absolutely and locally uniformly. Standard Mellin-transform theory therefore makes `F` holomorphic throughout

`Re(w)>-delta`.

This is only the elementary fundamental-strip direction: decay of the original function enlarges the half-plane in which its Mellin integral is holomorphic. No converse mapping theorem is used.

On the other hand, `VIS-293` gives a meromorphic continuation of `D(s)` to `Re(s)>1/2`, with

`D(s)=(log zeta)''(s)+A(s)`

and `A` holomorphic there. Thus the right-hand side of the identity for `F(w)` is meromorphic for

`Re(w)>-1/2`.

Because the two expressions agree on the nonempty open strip `0<Re(w)<2`, analytic continuation identifies them on their common continuation domain.

## 3. Off-line zeros become forbidden poles

Let `rho` be a nontrivial zeta zero with `Re(rho)>1/2`, and set

`w_rho=rho-1`.

By `VIS-293`, `D(1+w)` has a double pole at `w=w_rho`. The Wang multiplier

`4/(4-w^2)`

is nonzero at every such point: a nontrivial zero has `-1<Re(w_rho)<0`, so `w_rho` is not `+/-2`. The explicit terms `C/(2-w)` and `1/w^2` are also holomorphic at `w_rho`; the only possible singularity of `1/w^2` is `w=0`, corresponding to the pole `s=1`, not to a nontrivial zero.

Therefore the meromorphic continuation of the right-hand side has an uncancelled double pole at every `w_rho` with `Re(rho)>1/2`.

But the assumed real-axis bound makes `F` holomorphic whenever

`Re(w_rho)=Re(rho)-1>-delta`,

i.e. whenever

`Re(rho)>1-delta`.

Such a pole is impossible. Hence there are no nontrivial zeros in

`Re(rho)>max(1/2,1-delta)`.

For `delta>=1/2`, this excludes every zero to the right of the critical line. The functional equation reflects any zero to the left of `1/2` to one to the right, so all nontrivial zeros must then lie on `Re(s)=1/2`.

## 4. Prior art and evidence boundary

The only general transform input is the classical fact that a Mellin integral is analytic in its fundamental strip and that stronger endpoint decay enlarges that strip. A standard reference is Philippe Flajolet, Xavier Gourdon, and Philippe Dumas, **Mellin Transforms and Asymptotics: Harmonic Sums**, *Theoretical Computer Science* 144 (1995), 3--58, DOI `10.1016/0304-3975(95)00002-E`, especially the discussion of fundamental strips and Mellin mapping principles. The zeta-specific pole divisor used here is the already-persisted `VIS-293` reduction.

No novelty is claimed for Mellin fundamental strips, the general relation between remainder decay and zero-free regions, or zeta functional-equation symmetry. The Mathia-specific content is the exact pricing of a proposed **Wang source-profile** power saving through the source Mellin identity and the pole divisor established in `VIS-293`.

The implication is deliberately one-sided. A zero-free region alone need not yield `R(x)=O(x^(-delta))` without suitable growth and inversion estimates. Nor does this result classify stretched-exponential, logarithmic, or other subpower improvements, which can enlarge the useful real-axis envelope without creating a fixed Mellin half-plane.

## Dependencies

- `VIS-291`: current unconditional Korobov--Vinogradov-scale envelope for the fixed-power Wang source branch.
- `VIS-292`: exact Wang Green/Mellin identity and nonvanishing smoothing multiplier.
- `VIS-293`: exact first-half-plane pole divisor of the squared-von-Mangoldt source transform.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose real-axis source route is narrowed here.

## Research consequence

The accepted Wang clue can now separate two regimes cleanly. A **fixed power** real-axis gain `O(x^(-delta))` is already a zero-free-half-plane theorem; at `delta>=1/2` it is RH-equivalent in the one-way sense above. Such a hypothesis must therefore be priced explicitly rather than described as a modest source-specific improvement.

The genuinely cheaper unresolved search space is narrower: subpower improvements to the current Korobov--Vinogradov-scale remainder, or a fixed-power gain accompanied by an explicit proof of the corresponding fixed zero-free strip, must still be propagated through Wang's source, gamma, localization, cross-term and moving-upper budget. Whether any such weaker gain is quantitatively sufficient at the natural window remains open.