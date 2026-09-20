# VIS-326 — the first Wang Christoffel split has universal adjacent-coordinate monodromies

## Claim

Keep the maximally fragmented, denominator-`k` renormalized Wang branch of `VIS-325`. Thus

`gcd(u,v)=1`, `u != v`,

`m=max(u,v)`, `n=min(u,v)`, `k=|v-u|>L`, `sigma=sign(v-u)`,

and the renormalized mechanical slope is the reduced rational `d/k`, with the adjacent larger-denominator slope `c/m` satisfying

`d m-c k=sigma`.

Let

`J=floor(m/k)`,

`q=m-Jk`,

`p=c-Jd`.

Since `gcd(m,k)=1` and `k>1`, one has `1<=q<k`, and

`d q-p k=sigma`.

Hence `p/q` is one Farey parent of `d/k`; the complementary fraction

`(d-p)/(k-q)`

is the other parent. At the Christoffel-period level, these are precisely the two parent blocks in the first Farey/standard-word split, up to the usual order/conjugacy convention.

Let the two elementary Wang step vectors from `VIS-325` be

`s_0=(-b,-a)`,

`s_1=(u-b,v-a)`,

and for a block with `q` determinant steps and `p` one-steps define its lattice monodromy

`G(p,q)=p s_1+(q-p)s_0`.

Then the two parent-block monodromies are completely independent of the large Bézout coefficients. They depend only on the Euclidean quotient `J=floor(m/k)` and on the orientation of the center pair.

If `v>u`,

`G(p,q)=(1-J,-J)`,

`G(d-p,k-q)=(J,J+1)`.

If `u>v`,

`G(p,q)=(J,J-1)`,

`G(d-p,k-q)=(-J-1,-J)`.

In either orientation:

- each parent monodromy has consecutive integer coordinates, so it is primitive;
- the two parent monodromies sum to the full period monodromy `(sigma,sigma)` of `VIS-325`;
- their determinant advances against the center `(u,v)` are exactly their block lengths `q` and `k-q`.

At the natural Wang scale `k>L asymp M/log log M`, one has

`J << log log M`.

Thus the first continued-fraction/Christoffel renormalization does not replace the fragmented branch by another direction with coefficients of size `M`: it produces two primitive affine block directions with coordinate increments only `O(log log M)`.

There is, however, one exact sieve-degeneracy boundary. `J=1` if and only if

`m>2n`.

In that case the parent selected by the external Farey neighbour `c/m` is coordinate-stationary:

- for `v>u`, `G(p,q)=(0,-1)`;
- for `u>v`, `G(p,q)=(1,0)`.

So repeated copies of that parent block vary only one prime coordinate. A per-copy dimension-two prime-pair sieve would lose one logarithmic dimension on this block. The complementary parent remains nondegenerate, with monodromy `(1,2)` or `(-2,-1)` respectively.

For `J>=2`, both coordinates of both parent monodromies are nonzero and coprime. The first Christoffel split therefore has no common-step-content obstruction to using repeated parent blocks as two-affine-form sieve directions. What remains is to prove that sufficiently many useful copies occur inside the observed subperiod segment and to control the corresponding resultants/local factors; neither follows from the representation alone.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-CHRISTOFFEL-FACTORIZATION + REPRESENTATION-REDUCTION + SIEVE-DEGENERACY-CLASSIFICATION + NO-NOVELTY-CLAIM`.

No prime-count estimate, repeated-block sieve theorem, continued-fraction occupancy theorem, Wang natural-window theorem, or stronger RH criterion is claimed.

## 1. The external Farey neighbour selects an exact parent

From `VIS-325`, the two slopes satisfy

`d m-c k=sigma`.

Euclidean division gives

`m=Jk+q`, `1<=q<k`.

The strict remainder follows because

`gcd(m,k)=gcd(max(u,v),|u-v|)=gcd(u,v)=1`,

and `k>1` in the regime `L<k`.

Substituting `m=Jk+q` into the determinant-one identity gives

`d(Jk+q)-c k=sigma`,

hence

`d q-(c-Jd)k=sigma`.

With `p=c-Jd`,

`d q-pk=sigma`.

The inequalities `0<=p<=q` follow directly from

`p=(qd-sigma)/k`

and `0<d<k`; the endpoint values correspond to the usual `0/1` or `1/1` Farey parent. Thus `p/q` is a reduced Farey neighbour of `d/k` with smaller denominator. The complementary numerator-denominator pair

`(d-p,k-q)`

has the opposite determinant and is the other Farey parent. Their mediant is exactly `d/k`.

This makes the first continued-fraction step intrinsic to the Wang center geometry: its parent denominator is not an arbitrary approximant but the Euclidean remainder

`q=m mod k`.

## 2. A general Farey-parent block has an exact Wang displacement

A block with `q` determinant increments and `p` one-steps has net lattice displacement

`G(p,q)`
` =p s_1+(q-p)s_0`
` =(p u-q b, p v-q a)`.

Two identities are immediate and useful independently of the special parent chosen above.

First,

`v G_1-u G_2=q(ua-vb)=q`,

because `au-bv=1`. Thus the determinant-coordinate advance of a block is exactly its word length `q`, as it must be geometrically.

Second,

`G_2-G_1`
` =p(v-u)-q(a-b)`.

Using the orientation-dependent definition of `d` from `VIS-325`, this becomes

`G_2-G_1=sigma(pk-qd)`.

For a Farey parent, `|pk-qd|=1`; therefore its two monodromy coordinates differ by exactly one. In particular

`gcd(G_1,G_2)=1`.

This primitivity is Mathia-relevant because repeated copies of one parent block, when they occur, place corresponding internal offsets on affine progressions whose two step coefficients have no common factor. It does not by itself guarantee two-prime density: the repeat count, contents of the translated forms, and their resultant still matter.

## 3. The selected parent collapses to the Euclidean quotient

For the parent selected by `m=Jk+q`, the determinant relation is

`pk-qd=-sigma`.

The explicit Bézout identities of `VIS-325` give the unified displacement formula

`G(p,q)`
` =(((-sigma)u+sigma q)/k, ((-sigma)v+sigma q)/k)`
` =sigma((q-u)/k,(q-v)/k)`.

Now use `q=m-Jk`.

If `v>u`, then `m=v`, `u=v-k`, and

`(q-u)/k=1-J`,

`(q-v)/k=-J`.

Hence

`G(p,q)=(1-J,-J)`.

If `u>v`, then `m=u`, `v=u-k`, and multiplication by `sigma=-1` gives

`G(p,q)=(J,J-1)`.

The complementary parent block fills the rest of the denominator-`k` period. Since `VIS-325` proves that the full period monodromy is `(sigma,sigma)`, subtraction gives

`(J,J+1)`

when `v>u`, and

`(-J-1,-J)`

when `u>v`.

So the first Christoffel split has a universal lattice image: after all large parameters and Bézout coefficients cancel, only the single Euclidean quotient `J` remains.

## 4. The hard Wang regime makes the parent directions small

In the unresolved regime of `VIS-324`--`VIS-325`,

`k>L`.

At the natural Wang scale,

`L asymp M/log log M`,

while `m<=2M`. Therefore

`J=floor(m/k) << log log M`.

Every coordinate in the two parent monodromies from Section 3 is consequently `O(log log M)`.

This is a genuine representation gain. The original branch lives at prime coordinates of size `M`, and the first denominator-`k` period has length `k=M^(1-o(1))` in the difficult regime. Yet the two first-level Christoffel parent blocks translate corresponding points by primitive consecutive-coordinate vectors of only logarithmic-iterated size.

A large partial quotient or another mechanism that yields many consecutive copies of one such parent block would therefore create a classical affine-sieve direction with small step coefficients. The present result deliberately stops before asserting that the observed Wang subperiod actually contains enough such copies.

## 5. Exact coordinate-stationary boundary

The quotient `J` equals one exactly when

`k<=m<2k`.

Since `k=m-n`, the strict upper inequality is equivalent to

`m>2n`.

(The equality `m=2n` is impossible for coprime `u,v>1`.)

For `J=1`, Section 3 gives

`G(p,q)=(0,-1)` when `v>u`,

and

`G(p,q)=(1,0)` when `u>v`.

This is not merely a small-coefficient case. Along repeated copies of that parent block, one prime coordinate is exactly frozen. If the frozen coordinate is composite, the corresponding prime-pair fibre is empty; if it is prime, only the other coordinate still has to be prime. Thus a sieve performed only in the copy index has dimension one on that fibre and cannot be credited with the generic two powers of logarithmic saving.

The complementary parent is still nondegenerate:

`(1,2)` for `v>u`,

`(-2,-1)` for `u>v`.

Therefore `J=1` does not kill continued-fraction renormalization, but it does kill a naive rule saying that every repeated Christoffel parent block automatically provides a dimension-two sieve variable.

For `J>=2`, both coordinates of both parent vectors are nonzero and consecutive, hence coprime. This removes the step-content degeneracy but leaves the ordinary two-form arithmetic conductor and the available repetition length to be controlled.

## Prior-art and novelty boundary

Farey parents, Christoffel words, rational mechanical words, standard-word factorizations, and their continued-fraction recursion are classical. The relevant prior-art boundary is already recorded in `VIS-325`, including Jean-Pierre Borel and Christophe Reutenauer, **On Christoffel classes**, *RAIRO - Theoretical Informatics and Applications* 40:1 (2006), 15--27, DOI `10.1051/ita:2005038`, and Jean Berstel, Aaron Lauve, Christophe Reutenauer, Franco Saliola, **Combinatorics on Words: Christoffel Words and Repetitions in Words**, CRM Monograph Series 27, American Mathematical Society, DOI `10.1090/crmm/027`.

The use of a dimension-two upper-bound sieve for two nonproportional affine forms is likewise classical and is already anchored in `VIS-324` through Iwaniec--Kowalski and Friedlander--Iwaniec. No new theorem about Christoffel factorization or Selberg sieve is claimed.

The Mathia-specific content is the exact specialization to the Wang Bézout path: the larger-denominator neighbour `c/m` selects the Euclidean parent `q=m mod k`; both first Christoffel parent blocks have universal monodromies depending only on `floor(m/k)`; those vectors are automatically primitive; and the only coordinate-stationary first-parent case is the explicit center-ratio regime `m>2n`.

## Boundaries and falsification

This result classifies the **first** Christoffel/Farey split. It does not assert that a useful parent block repeats many times inside the observed determinant window. A cyclic conjugate of the period may intersect the standard factorization unfavourably, and later continued-fraction levels can have different repetition structure.

Primitivity of a block translation is not prime pseudorandomness. Even with nonzero coprime step coefficients, a two-affine-form sieve carries a resultant/local-factor conductor depending on the internal offset of the block. That conductor and its aggregate behavior are not bounded here.

The `J=1` axis case is a warning about **per-copy** sieving, not a proof of excessive Wang occupancy. Sieve dimension may be recovered by averaging over internal block offsets, by using the complementary parent, or by a later coefficient-weighted argument.

The `O(log log M)` monodromy bound uses the natural hard-regime scale `k>L asymp M/log log M`. The exact formulas for the parent vectors do not require that asymptotic specialization.

Falsify the exact claim by producing an admissible `VIS-325` branch for which `q=m mod k` is not a Farey-parent denominator of `d/k`, one of the displayed parent monodromies fails, the two monodromies do not sum to `(sigma,sigma)`, their coordinate difference is not one in absolute value, or `J=1` occurs outside the stated center-ratio regime.

## Dependencies

- `VIS-319`: canonical unimodular Bézout coordinates preserving the two prime-coordinate exclusions.
- `VIS-321`: fixed-gate mechanical-path representation.
- `VIS-322`: center-gap Farey-neighbour identities and diagonal period direction.
- `VIS-324`: closure of polynomially long first-level runs and isolation of the near-maximal center-gap sieve frontier.
- `VIS-325`: denominator-`k` mechanical renormalization and full-period monodromy `(sigma,sigma)`.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the natural-window occupancy frontier.

## Research consequence

The vague "try continued fractions" branch from `VIS-325` now has a concrete first gate. Inspect the Euclidean quotient

`J=floor(m/k)`

and the two parent lengths

`q=m mod k`, `k-q`.

For `J>=2`, any genuinely repeated first-parent packet moves corresponding prime-coordinate positions along primitive nonzero consecutive-step affine directions of size `O(log log M)` in the hard natural regime. The next theorem should quantify the repeat multiplicity actually visible in the subperiod window and then control the two-form resultants/local factors across internal offsets.

For `J=1`, do not apply a dimension-two sieve blindly to the externally selected parent copies: that block has an axis monodromy and only one varying prime coordinate. Either use the complementary parent, average across internal offsets to recover the second arithmetic dimension, or move to a later continued-fraction/energy representation.

This is the natural stopping boundary for the present invocation. The next independent question is no longer what the first Christoffel directions are, but whether their visible repetition and resultant structure are strong enough to meet the `VIS-316` taper-weighted occupancy target.