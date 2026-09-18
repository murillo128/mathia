# VIS-293 — Wang's squared-von-Mangoldt source has the zeta zero divisor in its first continuation half-plane

## Claim

Let

`D(s)=sum_(n>=2) Lambda(n)^2 n^(-s)`

for `Re(s)>1`, the Dirichlet transform of the weighted source measure in `VIS-292`, and let

`P(s)=sum_p p^(-s)`

be the prime zeta function. Then, initially for `Re(s)>1`,

`D(s)=sum_(k>=1) P''(k s)`.

Using the classical Möbius inversion

`P(z)=sum_(m>=1) [mu(m)/m] log zeta(m z)`,

differentiation twice and regrouping give

`D(s)=sum_(r>=1) c(r) (log zeta)''(r s)`,

where

`c(r)=sum_(m|r) mu(m)m = product_(p|r)(1-p)`.

Consequently

`D(s)=(log zeta)''(s)+A(s)`,

where

`A(s)=sum_(r>=2) c(r)(log zeta)''(r s)`

is holomorphic throughout the open half-plane `Re(s)>1/2`.

Therefore the meromorphic continuation of `D` to `Re(s)>1/2` has exactly the same singularities there as `(log zeta)''(s)`: a double pole with principal part `+(s-1)^(-2)` at `s=1`, and for every nontrivial zeta zero `rho` of multiplicity `m_rho` with `Re(rho)>1/2`, a double pole with principal part

`-m_rho (s-rho)^(-2)`.

In particular,

`D(s)-1/(s-1)^2`

is holomorphic on `Re(s)>1/2` **if and only if RH holds**.

Combined with `VIS-292`, the continued Mellin-side quantity

`[4/(4-w^2)] D(1+w)`

inherits every off-critical zeta zero as a double pole at `w=rho-1`; the symmetric Wang kernel does not cancel these poles because its multiplier has no zeros there.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PRIME-ZETA CONTINUATION + RH-EQUIVALENT REFORMULATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not prove RH, a sharper real-axis bound for `S(x)-log x`, or a new continuation theorem for the prime zeta function. It identifies the exact analytic burden hidden inside the source-specific branch left open by `VIS-292`.

## 1. Exact prime-zeta decomposition

Since `Lambda(p^k)=log p`, absolute convergence for `Re(s)>1` gives

`D(s)`
` = sum_p sum_(k>=1) (log p)^2 p^(-k s)`
` = sum_(k>=1) P''(k s)`.

For the prime zeta function, Euler's product and Möbius inversion give

`P(z)=sum_(m>=1) [mu(m)/m] log zeta(m z)`

in the initial half-plane of absolute convergence. Differentiating twice with respect to `z`,

`P''(z)=sum_(m>=1) mu(m)m (log zeta)''(m z)`.

Hence

`D(s)=sum_(k,m>=1) mu(m)m (log zeta)''(m k s)`.

Writing `r=mk` and summing over divisors `m|r`,

`D(s)=sum_(r>=1) c(r)(log zeta)''(r s)`

with

`c(r)=sum_(m|r) mu(m)m`.

The divisor sum is multiplicative, and on a prime power only `m=1,p` contribute, so

`c(r)=product_(p|r)(1-p)`.

No asymptotic input is used in this identity.

## 2. Only the `r=1` term can be singular for `Re(s)>1/2`

Fix a compact subset of `Re(s)>1/2`; then `Re(s)>=1/2+delta` for some `delta>0`. For every `r>=2`,

`Re(r s)>=1+2 delta`.

Thus `zeta(r s)` is holomorphic, nonzero and finite there. Moreover

`(log zeta)''(z)=sum_(n>=2) Lambda(n) log n n^(-z)`

absolutely for `Re(z)>1`. Since `|c(r)|<=r` and the latter Dirichlet series decays exponentially in `r` uniformly on the compact set, the series

`A(s)=sum_(r>=2)c(r)(log zeta)''(r s)`

converges normally there. Hence `A` is holomorphic on all of `Re(s)>1/2`.

The continuation problem in this first half-plane therefore collapses exactly to the single term `(log zeta)''(s)`.

## 3. Pole divisor and the RH equivalence

Near `s=1`, write

`zeta(s)=(s-1)^(-1) h(s)`

with `h(1)!=0`. Then

`(log zeta)''(s)=1/(s-1)^2 + holomorphic`.

Near a nontrivial zero `rho` of multiplicity `m_rho`, write

`zeta(s)=(s-rho)^(m_rho) g(s)`

with `g(rho)!=0`. Then

`(log zeta)''(s)=-m_rho/(s-rho)^2 + holomorphic`.

Because `A` is holomorphic, none of these poles can be cancelled by the `r>=2` source terms. Thus after removing the pole at `1`, `D` is holomorphic in the open half-plane `Re(s)>1/2` exactly when zeta has no zeros there.

The functional equation pairs every nontrivial zero with real part below `1/2` with one above `1/2`. Therefore absence of zeros in `Re(s)>1/2` is equivalent to all nontrivial zeros lying on `Re(s)=1/2`, i.e. RH.

This equivalence is a reformulation, not an independent attack on RH.

## 4. Consequence for Wang's smoothing

`VIS-292` gives, initially for `0<Re(w)<2`,

`M[S](w)=[4/(4-w^2)]D(1+w)`.

The rational multiplier has no zero in the continuation region relevant here. Hence a zeta zero `rho` with `Re(rho)>1/2` produces a double pole of the continued Mellin-side expression at

`w=rho-1`,

with `Re(w)>-1/2`.

So Wang's symmetric smoothing preserves the first-half-plane zero divisor analytically. The source is not merely "prime-sensitive": its first nontrivial continuation half-plane already contains an RH-equivalent holomorphy condition.

This sharply limits what counts as a useful source-specific escape. Proving directly that the normalized source transform has no poles in `Re(s)>1/2` would simply prove RH in different coordinates. A weaker real-axis estimate for `S(x)-log x` may still be useful, but it must be assessed by what continuation or zero-free region it actually implies rather than being treated as free extra cancellation supplied by the Wang source.

## 5. Prior art and evidence boundary

The prime-zeta Möbius inversion and its continuation/singularity mechanism are classical; see Carl-Erik Fröberg, **On the Prime Zeta Function**, *BIT Numerical Mathematics* 8 (1968), 187–202, DOI `10.1007/BF01933420`. Standard zeta zero symmetry and the equivalence between zero-freeness of `Re(s)>1/2` and RH are already anchored in this line's `SOURCES.md` through DLMF §25.10.

No novelty is claimed for prime-zeta continuation, Möbius inversion, or the RH equivalence. The Mathia-specific result is the exact reduction of **Wang's particular squared-von-Mangoldt source transform** to `(log zeta)''` plus a holomorphic remainder in the first continuation half-plane, and the resulting negative control on proposed source-specific analytic gains.

The result does not show that every improvement over the Korobov–Vinogradov real-axis envelope proves RH. It does not derive a converse Tauberian theorem for a particular remainder scale, control a moving source boundary, or establish an asymptotic secondary term for `S(x)`. Those require separate arguments.

## Dependencies

- `VIS-291`: gives the strongest standard unconditional fixed-power PNT envelope currently propagated through Wang's complete error budget.
- `VIS-292`: identifies the nonvanishing Green/Mellin multiplier and leaves the analytic structure of `D(s)` as the separate next question.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose deeper fixed-power branch is narrowed here.

## Research consequence

The fixed-power source branch no longer has an uncosted "study `D(s)`" escape. In the first continuation half-plane, `D` differs from `(log zeta)''` only by a holomorphic term, so its off-line singularities are exactly the zeta off-line zeros. Any proposed analytic continuation or pole-exclusion argument for this source must be priced against that RH-equivalent burden.

The remaining nontrivial possibilities are narrower: derive a genuinely useful **real-axis** source estimate and state precisely what zero-free information it entails, or leave the compact fixed-power regime and study a moving source boundary where the existing uniform theorem no longer applies. Those are separate research questions and are not pursued in this invocation.