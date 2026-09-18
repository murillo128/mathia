# VIS-286 — Wang's large-source diagonal profile linearizes and its arithmetic residual vanishes

## Claim

Keep the exact diagonal source profile isolated in `VIS-282`–`VIS-285`,

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`,

where

`S_D(x)=x^(-2) sum_(2<=n<=x) n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`

and

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3`.

Then, unconditionally as `x->infinity`,

`S_D(x)=log x+o(1)`

and hence

`Q_gamma(x)=log x+o(1)`.

In the physical-source coordinate `x=e^(2*pi*q)`, this becomes

`Q_gamma(e^(2*pi*q))=2*pi*q+o(1)` as `q->infinity`.

Thus the exact prime-power structure exposed at fixed source does not leave a bounded nonzero residual at the escaping-source end after the universal linear profile is removed. More strongly, if `h_T` is any family with uniformly bounded `L^1` norm and

`supp(h_T) subset [Q_T,infinity)`, `Q_T->infinity`,

then

`integral h_T(q)[Q_gamma(e^(2*pi*q))-2*pi*q]dq -> 0`.

So a translating bounded-total-variation packet cannot retain a nontrivial coefficient-scale response from the isolated diagonal arithmetic residual merely by escaping to large source. Any genuine off-compact gain in the complete Wang statistic must come from another sector, a nonuniform remainder, or deliberately growing packet conditioning rather than from a persistent large-`q` residual of `Q_gamma`.

At a prime power `m=p^k`, the jump in the `q`-derivative of the residual is exactly

`-8*pi Lambda(m)^2/m`,

which also tends to zero along escaping source points. The local prime-power kinks therefore flatten in the physical-source coordinate as well as disappearing in the global residual amplitude.

**Evidence/status:** `LITERATURE+DERIVED + PRIME-NUMBER-THEOREM SPECIALIZATION + SOURCE-ESCAPE NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new prime-number theorem, new estimate for Wang's complete pair statistic, moving-packet asymptotic, off-critical-strip gain, or RH implication is claimed.

## 1. The squared von Mangoldt mass has a two-term classical asymptotic

Put

`B(x)=sum_(n<=x) Lambda(n)^2`.

The prime powers with exponent at least two contribute only `o(x)`. Indeed their total contribution is bounded by the primes up to `sqrt(x)` and smaller higher-power ranges, hence is `O(sqrt(x) log x)` at the precision needed here.

For the prime contribution, partial summation gives

`sum_(p<=x) (log p)^2 = theta(x) log x - integral_2^x theta(t)/t dt`,

where `theta(x)=sum_(p<=x) log p`.

The classical zero-free-region form of the prime number theorem gives, in particular,

`theta(x)=x+o(x/log x)`.

Substitution yields

`sum_(p<=x) (log p)^2 = x log x - x + o(x)`.

Therefore

`B(x)=x log x-x+o(x)`.

Only this standard consequence of the prime number theorem is needed below. The stronger classical de la Vallee Poussin error is far more than sufficient.

## 2. The two halves of `S_D` have opposite constant terms

Write

`S_D(x)=A_-(x)+A_+(x)`,

with

`A_-(x)=x^(-2) sum_(n<=x) n Lambda(n)^2`

and

`A_+(x)=x^2 sum_(n>x) Lambda(n)^2/n^3`.

Partial summation against `B` gives

`sum_(n<=x) n Lambda(n)^2 = x B(x)-integral_1^x B(t)dt`.

Using `B(t)=t log t-t+o(t)`, one obtains

`x B(x)=x^2 log x-x^2+o(x^2)`

and

`integral_1^x B(t)dt = (1/2)x^2 log x-(3/4)x^2+o(x^2)`.

Hence

`A_-(x)=(1/2)log x-1/4+o(1)`.

For the tail, Stieltjes partial summation gives

`sum_(n>x) Lambda(n)^2/n^3 = -B(x)/x^3 + 3 integral_x^infinity B(t)/t^4 dt`.

The same asymptotic for `B` yields

`A_+(x)=(1/2)log x+1/4+o(1)`.

The constants cancel exactly, leaving

`S_D(x)=log x+o(1)`.

This sharpens the `log x+O(1)` form sufficient for Wang's growing-source theorem, but it uses no information beyond the classical prime number theorem applied to Wang's explicit coefficient sequence.

The added term in `Q_gamma` satisfies `C_Lambda/x^2=o(1)`, so

`Q_gamma(x)-log x -> 0`.

## 3. Escaping packets cannot preserve the isolated residual at bounded total variation

Set

`R_infty(q)=Q_gamma(e^(2*pi*q))-2*pi*q`.

The preceding calculation is exactly the statement

`R_infty(q)->0` as `q->infinity`.

Let a packet family satisfy `sup_T ||h_T||_1 <= M` and `supp(h_T) subset [Q_T,infinity)` with `Q_T->infinity`. Then

`|integral h_T(q)R_infty(q)dq|`
` <= M sup_(q>=Q_T)|R_infty(q)|`
` -> 0`.

No smoothness, fixed width, or fixed packet shape is needed for this conclusion. Bounded total variation and escape of the entire support suffice.

This statement concerns only the already isolated diagonal profile. It does **not** justify substituting a growing source into the compact-source pair-statistic asymptotics of `VIS-283`–`VIS-284`. In Wang's complete formula, the localization error, mean-value remainder, other source sectors, and the allowed range `x<=T^lambda` must be tracked jointly with the chosen growth law `x=x(T)`.

Thus a large-`q` plot or packet response that grows approximately linearly is not, by itself, an arithmetic discovery: `2*pi*q` is the forced asymptotic baseline. A residual signal is meaningful only after that baseline and the moving-source error budget have both been charged.

## 4. The prime-power kinks flatten under source escape

`VIS-282` proved that at each prime power `m`,

`S_D'(m+)-S_D'(m-)=-4 Lambda(m)^2/m^2`.

The smooth terms `log x` and `C_Lambda/x^2` do not change this jump. Under `x=e^(2*pi*q)`, the chain rule therefore gives the jump in the `q` derivative of either `Q_gamma(e^(2*pi*q))` or its residual after subtracting `2*pi*q` as

`2*pi*m[-4 Lambda(m)^2/m^2] = -8*pi Lambda(m)^2/m`.

Since `Lambda(p^k)^2=(log p)^2` and `(log p)^2/p^k -> 0`, the kink amplitude vanishes along the escaping prime-power sequence. The fixed-source arithmetic texture survives exactly at each finite source point but becomes asymptotically flat in this coordinate.

This derivative observation is a consequence of the stronger value asymptotic, not an independent route to a source threshold.

## 5. Prior art and novelty boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), defines

`a_n(x)=Lambda(n)n^(-1/2) min(n/x,x/n)`

and records the global estimate `sum a_n(x)^2=log x+O(1)` used in his short-interval pair-correlation argument. `VIS-282` retained the exact square sum instead of collapsing it to that bound.

The only additional input here is classical prime-distribution theory. The prime number theorem in Chebyshev-function form, together with its standard zero-free-region error, implies the two-term asymptotic for `B(x)` used above; see for example A. Ivić, **The Riemann Zeta-Function**, Wiley (1985), Chapter 12, or the standard prime-number-theorem references collected in NIST DLMF §25.16(i).

The conclusion `S_D(x)=log x+o(1)` is therefore treated as a direct classical specialization of Wang's explicit coefficients, not as a new analytic-number-theory theorem. A targeted literature check found no need for an additional mechanism beyond this standard partial-summation argument.

## 6. Boundaries and falsification

The asymptotic `Q_gamma(x)=log x+o(1)` is an `x->infinity` statement about the isolated source profile. It does not provide a rate uniform in a simultaneously growing `T`, nor does it control Wang's complete field-energy or pair-statistic error when `x=x(T)`.

The bounded-packet consequence fails if `||h_T||_1` is allowed to grow rapidly enough to amplify the vanishing residual. Such growth is precisely packet conditioning and must be charged separately, just as in the fixed-interior localization obstruction of `VIS-284`.

Likewise, subtracting the linear `2*pi*q` baseline does not remove or estimate other Wang sectors. A genuine new large-source mechanism would survive after the exact baseline subtraction **and** after all source-dependent theorem errors and normalization factors are shown small in the same growth regime.

No confirmation-zero data, numerical fitting, or visual salience is used.

## Dependencies

- `VIS-282`: exact formula for `S_D(x)` and prime-power derivative jumps.
- `VIS-283`: identifies `Q_gamma(x)=S_D(x)+C_Lambda/x^2` as the surviving fixed-source diagonal profile after signed recombination.
- `VIS-284`: bounded packet projection and the total-variation cost of fixed-interior localization.
- `VIS-285`: exact regularity of `Q_gamma` at the opposite source boundary `q=0`.

## Research consequence

The two obvious singularities of the **isolated diagonal source observable** are now closed. `VIS-285` shows that `Q_gamma` is analytic and quadratic at `q=0`; the present result shows that at `q->infinity` it is only the universal linear profile `2*pi*q` plus a vanishing residual.

The accepted packet-localization clue is therefore narrowed again. Any surviving source-boundary or off-compact mechanism must live in the complete moving-source Wang asymptotic — for example in a quantitatively nonuniform remainder, another source sector, or a singular packet normalization — rather than in a hidden endpoint amplification of `Q_gamma` itself. Deriving that coupled moving-source budget is a separate thread.