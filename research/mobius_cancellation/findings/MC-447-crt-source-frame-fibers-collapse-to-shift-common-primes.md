# MC-447 — CRT source-frame fibers collapse to shift-common-prime degeneracies

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-INGREDIENTS` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the restricted-frame branch isolated by `MC-446`. Let `q>=2`, let `h` be a nonzero shift with `(h,q)=1`, and let `d,e` be squarefree sieve divisors satisfying

\[
(de,q)=1,
\qquad
(d,e)\mid h.
\tag{1}
\]

Put

\[
L=[d,e],
\tag{2}
\]

and let `r` be the canonical integer `0<=r<L` solving

\[
r\equiv0\pmod e,
\qquad
r\equiv-h\pmod d.
\tag{3}
\]

As in `MC-413`, attach the incomplete-character frame

\[
F_h(d,e)=(u,a),
\qquad
u\equiv rL^{-1}\pmod q,
\qquad
a\equiv hL^{-1}\pmod q.
\tag{4}
\]

Assume the separated-modulus range

\[
d,e\le D,
\qquad D^2<q.
\tag{5}
\]

Then the frame `(u,a)` determines `(L,r)` uniquely. Moreover, once `(L,r)` is fixed, every ambiguity in recovering `(d,e)` comes only from primes dividing both `L` and the shift `h`:

\[
\boxed{
\#F_h^{-1}(u,a)
\le 3^{\omega((L,h))}.
}
\tag{6}
\]

If additionally `L<=D`, so every divisor of `L` lies inside the sieve support, the bound is exact:

\[
\boxed{
\#F_h^{-1}(u,a)=3^{\omega((L,h))}.
}
\tag{7}
\]

In particular, if the shift is coprime to the sifting support `P(z)` and `d,e|P(z)`, then `(L,h)=1` and

\[
\boxed{F_h\text{ is injective on the supported compatible divisor pairs.}}
\tag{8}
\]

For fixed `L`, the distinct frame starts `u` are indexed only by the primes of `L` not dividing `h`. When `L<=D`, their number is exactly

\[
\boxed{
2^{\omega(L/(L,h))}.
}
\tag{9}
\]

Thus the two easiest escape mechanisms left open after `MC-446` do not supply hidden averaging in the natural separated regime:

1. grouping by the constrained shift `a=hL^{-1}` is merely grouping by the lcm `L`, because `a` determines `L` uniquely;
2. frame collisions are absent when `(h,P(z))=1`, and in general are confined to the elementary `3`-way assignment ambiguity at primes common to `L` and `h`.

For prime `q>=5`, a single fixed-`a` slice cannot even meet the full-box Cauchy occupancy threshold of `MC-446`. Indeed its support has size at most `2^{\omega(L)}<q-1`, whereas the exact prime-modulus threshold from `MC-446` is at least `q-1` for every `1<=H<=q`.

This does **not** rule out a sharper restricted-frame second moment. It rules out obtaining that gain merely from lcm fibres, pair collisions, or from treating `a=hL^{-1}` as an additional free averaging coordinate. The remaining live mechanisms must use cancellation in the actual divisor weights, restricted Fourier/dispersion geometry of the distinct `u`-frames, modulus factorization, or a regime where `(5)` fails in a quantitatively useful way.

No new estimate for an incomplete character sum, `M(x)`, or a twisted Mertens sum follows.

## 1. The frame recovers the lcm and the canonical CRT residue

Because `(h,q)=1`, the coordinate `a` in `(4)` is a unit modulo `q`. Hence

\[
L\equiv h a^{-1}\pmod q.
\tag{10}
\]

The support condition `(5)` gives

\[
1\le L\le de\le D^2<q.
\tag{11}
\]

Therefore the residue class in `(10)` has exactly one possible representative in the allowed range: the frame determines the integer `L` itself.

Once `L` is known,

\[
r\equiv uL\pmod q.
\tag{12}
\]

The canonical choice `0<=r<L<q` again makes this representative unique. Thus any two divisor pairs producing the same frame must first produce the same exact pair `(L,r)`.

This already shows that fixing or grouping the shift coordinate `a` in the regime `(5)` does not average over multiple lcm scales. It simply selects one `L`.

## 2. Prime-by-prime reconstruction of `(d,e)`

Fix an admissible `(L,r)` and a prime `p|L`. Since `d,e` are squarefree and `[d,e]=L`, the prime `p` occurs in at least one of `d,e`.

If `p` does not divide `h`, then `p` cannot divide both `r` and `r+h`. The congruences `(3)` therefore force exactly one of two possibilities:

\[
\begin{array}{lll}
p\mid r     &\Longrightarrow& p\mid e,\ p\nmid d,\\
p\mid r+h   &\Longrightarrow& p\mid d,\ p\nmid e.
\end{array}
\tag{13}
\]

For an admissible frame one of these alternatives must occur, because `p` has to occur in `d` or `e`. Hence every prime `p|L` with `p\nmid h` has a **unique** side assignment.

Now suppose `p|h`. Since `p` must lie in at least one of `d,e`, either congruence in `(3)` forces

\[
r\equiv0\pmod p,
\tag{14}
\]

and then also `r+h=0 (mod p)`. Conversely, once `(14)` holds, the local congruences do not distinguish among

\[
p\mid d,\ p\nmid e;
\qquad
p\nmid d,\ p\mid e;
\qquad
p\mid d,\ p\mid e.
\tag{15}
\]

All three choices preserve the same `L` and `r`; the third is allowed precisely because the common prime divides `h`, so `(d,e)|h` remains satisfied.

The choices at distinct primes are independent. Therefore there are at most three pair assignments for each prime of `(L,h)`, proving `(6)`. If `L<=D`, none of the resulting divisors can leave the support range, so every local assignment in `(15)` is admissible and `(7)` follows.

The same argument counts distinct residues rather than pair preimages. Primes in `(L,h)` do not change `r` at all, while every prime in `L/(L,h)` has the binary `d`-side versus `e`-side choice in `(13)`. Hence, when `L<=D`, the number of distinct `(L,r)` and therefore distinct `u` values above one fixed `a` is exactly `(9)`.

## 3. Coprime shifts are the completely injective case

Suppose the sieve divisors are supported on the squarefree sifting product `P(z)` and

\[
(h,P(z))=1.
\tag{16}
\]

Then every supported lcm `L` is coprime to `h`. Equation `(6)` becomes

\[
\#F_h^{-1}(u,a)\le1,
\tag{17}
\]

which proves `(8)`. The compatibility condition `(d,e)|h` simultaneously forces `(d,e)=1`, so for `L<=D` the divisor pairs above `L` are simply the ordered coprime factorizations `L=de`. Each prime factor of `L` chooses one side, giving `2^{omega(L)}` different pairs, and the injectivity result says they give `2^{omega(L)}` different `u`-frames rather than a high-multiplicity fibre.

Equivalently, after multiplying the CRT residue by `-h^{-1}` modulo `L`, these starts are the classical CRT idempotents: for the coprime factorization `L=de`,

\[
x\equiv1\pmod d,
\qquad
x\equiv0\pmod e,
\tag{18}
\]

so `x^2=x (mod L)`. The apparent source-frame multiplicity is therefore the familiar Boolean choice of CRT components, embedded into the conductor coordinate; it is not an additional arithmetic dimension created by the q-vdC step.

## 4. Consequence for the `MC-446` occupancy route

Let `q=p>=5` be prime. For weights supported on one fixed `a`, the effective occupancy from `MC-446` satisfies

\[
R_{\mathrm{eff}}(W)\le |\operatorname{supp}W|
\le 2^{\omega(L/(L,h))}
\le 2^{\omega(L)}.
\tag{19}
\]

Because `L<q`, one has

\[
2^{\omega(L)}<q-1
\tag{20}
\]

for `q>=5` (the only equality case `2^{omega(L)}=L` for squarefree `L>1` is `L=2`, which is still `<q-1`). On the other hand the exact squarefree-prime specialization of the ambient threshold `(11)` in `MC-446` is

\[
\frac{(q-1)^2}{H}+\frac{H-1}{H}
=1+\frac{q(q-2)}H
\ge q-1,
\qquad 1\le H\le q.
\tag{21}
\]

Therefore a fixed-`a` source slice cannot make the **existing full-box Cauchy estimate** beat the pointwise `H||W||_1` bound. Merely grouping the divisor pairs by `a=hL^{-1}` does not evade the occupancy obstruction.

The qualifier is essential: `(21)` is the tariff of the full `(u,a)` moment. A new restricted moment over the arithmetic `u`-set could have a much smaller diagonal/off-diagonal cost and is not bounded by this argument. The present calculation identifies what such a theorem must actually exploit: not pair multiplicity, but cancellation or Fourier structure among a set of distinct CRT-idempotent frames.

## 5. Prior art and novelty boundary

The algebra in this finding is elementary Chinese-remainder theory. The correspondence between coprime factorizations of a squarefree modulus and idempotents of `Z/LZ` is a standard CRT consequence: under the product-ring decomposition, an idempotent chooses `0` or `1` independently in each prime component. The reconstruction in `(13)`--`(15)` is the same local algebra with the additional shift-common-prime degeneracy required by `(d,e)|h`.

A targeted audit on 21 September 2026 found the standard CRT/idempotent correspondence and the established incomplete-character/dispersion literature already recorded around `MC-413` and `MC-446`, but no reason to treat `(6)`--`(9)` as an independent number-theory theorem. No novelty is claimed for CRT idempotents, their Boolean count, or elementary fibre reconstruction.

The durable Mathia result is narrower: when the exact `MC-413` source-frame coordinates are inserted, two proposed ways of beating the `MC-446` ambient occupancy barrier can be classified completely in the separated-modulus regime. The constrained shift coordinate is just an injective lcm label, and frame collisions disappear for shifts coprime to the sieve support.

## Boundaries and falsification tests

- **The separated-modulus hypothesis is load-bearing.** If `D^2>=q`, distinct lcm values may be congruent modulo `q`, and `a` need not recover the integer `L`. Such wraparound fibres are not covered by `(6)` and remain a possible, though highly structured, regime to test.
- **The shift must be a unit modulo `q` for the lcm recovery step.** If `(h,q)>1`, the coordinate `a=hL^{-1}` is not invertible and can identify more lcm residues. This is separate from the shift-common-prime ambiguity inside `L`.
- **Squarefree sieve support is used in the local three-way classification.** Prime powers require valuation-level bookkeeping rather than the `d/e/both` alternatives in `(15)`.
- **The exact fibre count `(7)` assumes `L<=D`.** For `D<L<=D^2`, some reassigned pairs can violate `d,e<=D`; the universal upper bound `(6)` remains valid.
- **Injectivity is not cancellation.** Distinct source frames may still have a favorable restricted second moment or weighted dispersion relation. The result only says collisions/fibres do not provide that gain in the coprime-shift separated regime.
- **A fixed-`a` ambient-Cauchy failure is not a restricted-moment no-go.** The next analytic target remains a second moment or bilinear form evaluated on the actual CRT-idempotent set with the well-factorable weights inserted before Cauchy.
- **No RH or zero-free information enters.** The proof is finite CRT algebra plus the exact occupancy formula already proved in `MC-446`.

## Consequence for the research line

`MC-446` left fibres/collisions, grouping by `a=hL^{-1}`, outer coefficient cancellation, restricted Fourier geometry, and modulus factorization as concrete ways the arithmetic source-frame image might outperform generic ambient averaging. The first two are now sharply restricted.

In the common regime `(h,P(z))=1` and `D^2<q`, the divisor-pair map has no frame collisions at all, and fixing `a` is exactly fixing `L`. Even when the shift shares sieve primes, all same-frame multiplicity is explained by the elementary three-way assignment at those common primes. Therefore the next useful calculation should not search for hidden fibre multiplicity. It should compute a genuinely **restricted weighted second moment on the distinct CRT-idempotent `u`-set**, or exploit coefficient cancellation/modulus factorization before the source frames are scalarized.