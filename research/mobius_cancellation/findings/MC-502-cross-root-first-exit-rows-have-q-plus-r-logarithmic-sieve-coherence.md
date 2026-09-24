# MC-502 — Cross-root first-exit rows have q+r logarithmic sieve coherence

**Status:** `EXACT-DERIVED` · `CLASSICAL-LOCAL-DENSITY+DERIVED-APPLICATION` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-495` reduces the still-live incomplete repeated-residue cross-root branch to a nonnegative source weight against one conductor phase. One possible source of a nonuniform conductor weight is the exact lower-prime hard mask carried by a plus-root first-exit row and a minus-root first-exit row. For one pair of distinct active source primes, however, the **complete auxiliary-sieve overlap of those two hard masks has only logarithmic coherence**.

Let `q<r` be distinct active first-exit primes, with the same fixed small-prime exclusions as in `MC-471`--`MC-495`. Use the native first-exit coordinates

\[
n=qm
\qquad\text{for the plus root},
\tag{1}
\]

and

\[
n+h=rm
\qquad\text{for the minus root}.
\tag{2}
\]

For an active lower prime `ell<q`, with `ell` distinct from `q,r`, the plus row excludes

\[
m\equiv 0,-hq^{-1}\pmod\ell,
\tag{3}
\]

while the minus row excludes

\[
m\equiv 0,hr^{-1}\pmod\ell.
\tag{4}
\]

Hence their common lower-prime mask has the three candidate forbidden roots

\[
0,\qquad -hq^{-1},\qquad hr^{-1}\pmod\ell.
\tag{5}
\]

The two shifted roots collide exactly when

\[
-hq^{-1}\equiv hr^{-1}\pmod\ell
\iff
\ell\mid h(q+r).
\tag{6}
\]

Thus, away from primes dividing the fixed shift `h`, the cross-root collision invariant is **`q+r`**, in exact sign-sensitive contrast with the same-root `q-r` invariant of `MC-491`.

For every nondegenerate active common lower prime, the local forbidden-count function is

\[
\boxed{
\nu_\ell^{+-}(q,r)=
\begin{cases}
1,&\ell\mid h,\\
2,&\ell\nmid h\ \text{and}\ \ell\mid q+r,\\
3,&\ell\nmid h(q+r).
\end{cases}}
\tag{7}
\]

If a small active prime has `nu_ell^{+-}=ell`, the joint local support is empty and the overlap bound below is trivial; equivalently such finite degeneracies may be kept in the line's fixed-exclusion set.

Let `d_q` and `d_r` be the complete-period densities of the individual plus and minus lower-prime masks, and let `e_{q,r}^{+-}` be the complete-period density of their joint mask on a common auxiliary-sieve period. Define the normalized sieve coherence

\[
\rho_{\rm sieve}^{+-}(q,r)
:=
\frac{e_{q,r}^{+-}}{\sqrt{d_qd_r}}.
\tag{8}
\]

Then the exact CRT product and Mertens' product theorem give

\[
\boxed{
\rho_{\rm sieve}^{+-}(q,r)
\ll_{h,\mathcal E}
\frac1{\log r}
\prod_{\substack{\ell\mid(q+r)\\ \ell<q\\ \ell\ \mathrm{active}}}
\left(1-\frac1\ell\right)^{-1}}
\tag{9}
\]

and therefore

\[
\boxed{
\rho_{\rm sieve}^{+-}(q,r)
\ll_{h,\mathcal E}
\frac1{\log r}\,
\frac{q+r}{\varphi(q+r)}.}
\tag{10}
\]

Here `mathcal E` denotes the finite fixed exclusions/degenerate local factors. In polynomial source-prime ranges this is at most the familiar logarithmic enhancement

\[
\rho_{\rm sieve}^{+-}(q,r)
\ll_{h,\mathcal E,C}
\frac{\log\log p}{\log p}
\qquad(q,r\le p^C),
\tag{11}
\]

up to the usual harmless interpretation for bounded arguments.

So the complete-period lower-prime hard mask cannot by itself turn one cross-root pair into an order-one coherent object through a conductor-power mechanism. Any larger incomplete cross-root bias left by `MC-495` must come from **endpoint/conductor-profile alignment, genuinely q-dependent signed or complex source coefficients, or another structure that is destroyed by complete auxiliary-sieve averaging**. No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Exact cross-root collision law

For the plus first-exit root `q|n`, write `n=qm`. At a lower active prime `ell<q`, the residual pair-sieve condition excludes `ell|n` and `ell|n+h`. Since `q` is invertible modulo `ell`, these are exactly

\[
m\equiv0,
\qquad
m\equiv-hq^{-1}
\pmod\ell.
\tag{12}
\]

For the minus root `r|n+h`, write `n+h=rm`, hence `n=rm-h`. At an active prime `ell<r`, the corresponding exclusions are

\[
m\equiv0,
\qquad
m\equiv hr^{-1}
\pmod\ell.
\tag{13}
\]

On the common range `ell<q`, the union is `(5)`. The two nonzero candidate roots coincide precisely when

\[
-hq^{-1}=hr^{-1}\pmod\ell.
\]

Multiplying by `qr` gives

\[
h(q+r)\equiv0\pmod\ell,
\tag{14}
\]

which proves `(6)` and `(7)`. Equivalently, the common-core admissibility is the local nonvanishing of the cubic polynomial

\[
f_{q,r}(m)=m(qm+h)(rm-h),
\tag{15}
\]

whose three roots modulo a common lower prime are exactly `(5)`. The discriminant/collision content relevant here is therefore carried by the fixed factor `h` and the sign-sensitive source combination `q+r`.

This is not a new polynomial-sieve identity. The content for the present line is that the exact **first-exit plus/minus specialization** selects `q+r`; the plus/plus specialization in `MC-491` selects `q-r`. The difference is forced by the native root orientation, not chosen as a convenient coordinate.

## 2. Exact complete-period normalized overlap

Because the masks are products of residue exclusions, their complete-period densities factor over active auxiliary primes by CRT, exactly as in `MC-472` and `MC-491`.

For a common lower prime `ell<q`:

- if `ell|h`, each row excludes only the common class `0`, so the normalized local factor is `1`;
- if `ell\nmid h` and `ell|q+r`, both two-class masks exclude the same pair of classes, so the normalized local factor is again `1`;
- otherwise the individual rows each have local density `1-2/ell`, while the joint mask excludes three classes and has local density `1-3/ell`.

Thus every generic common-prime factor is

\[
\frac{1-3/\ell}{1-2/\ell}
=
\frac{\ell-3}{\ell-2}
\le
1-\frac1\ell.
\tag{16}
\]

For the one-sided tail `q\le\ell<r`, only the minus row is still sifted. In the normalized overlap its local factor is

\[
\sqrt{1-\frac1\ell}
\quad(\ell|h),
\tag{17}
\]

or

\[
\sqrt{1-\frac2\ell}
\le
1-\frac1\ell
\quad(\ell\nmid h).
\tag{18}
\]

The finitely many prime divisors of fixed `h`, fixed exclusions, and small degenerate factors are absorbed into a constant. Consequently the product of all generic active factors below `r` is bounded by a Mertens product, except that each collision prime dividing `q+r` in the common range removes one expected factor `1-1/ell`. This yields

\[
\rho_{\rm sieve}^{+-}(q,r)
\ll_{h,\mathcal E}
\prod_{\substack{\ell<r\\ \ell\ \mathrm{active}}}
\left(1-\frac1\ell\right)
\prod_{\substack{\ell\mid(q+r)\\ \ell<q\\ \ell\ \mathrm{active}}}
\left(1-\frac1\ell\right)^{-1}.
\tag{19}
\]

Mertens gives the first factor as `O(1/log r)` after the fixed exclusions are restored. The second product is at most

\[
\prod_{\ell\mid(q+r)}
\left(1-\frac1\ell\right)^{-1}
=
\frac{q+r}{\varphi(q+r)},
\tag{20}
\]

proving `(9)`--`(10)`. If desired, the fixed `h` dependence can be displayed symmetrically by replacing the final totient ratio by `|h(q+r)|/phi(|h(q+r)|)` rather than absorbing the prime divisors of `h` into the constant.

## 3. What the q+r invariant does and does not buy

The collision set can noticeably raise a particular pair overlap relative to the generic product when `q+r` is unusually smooth, but the increase is only the multiplicative totient factor in `(10)`. Standard maximal-order control of `n/phi(n)` makes this logarithmic in polynomial ranges; it is not a conductor power.

This rules out one tempting interpretation of the live lower-prime hard-mask route. The exact pair-sieve geometry **does** remember the source labels `q,r`: it remembers them through divisibility of `q+r`. But complete-period pairwise coherence prices that memory only through the small set of prime divisors of `q+r`. The hard mask is therefore not behaving like an arbitrary q-dependent phase code capable of supplying many nearly independent conductor directions.

The result does not imply that the full source weight `W(m)=A(m)B(m)` in `MC-495` has small correlation with the conductor phase. The physical first-exit rows are incomplete and have q-dependent endpoints. A truncation may sample the local mask very nonuniformly modulo the conductor even when the complete auxiliary-sieve period has small normalized overlap. That endpoint-sensitive correlation is precisely the part erased by the averaging used here and remains live.

Likewise, the theorem is pairwise. It does not assert a spectral bound for the entire matrix indexed by all plus/minus source primes. A collective argument would still have to account for dependencies among the additive invariants `q+r`; this finding only shows that each complete-period pair receives at most logarithmic/totient enhancement from the lower-prime hard-mask collision pattern.

## 4. Representation audit

### Source-to-representation map

The source objects are exact first-exit rows in the original integer variable `n`. On a plus root `q|n`, the forced affine coordinate is `m=n/q`. On a minus root `r|n+h`, the forced coordinate is `m=(n+h)/r`. In the incomplete repeated-residue decomposition of `MC-495`, the two row families are zero-extended to the same integer `m`-domain before their cross term is formed. Expanding the nonnegative amplitudes `A(m)B(m)` pairwise therefore exposes exactly the product of one plus hard mask and one minus hard mask analyzed above.

### Preserved structure

The affine maps preserve, prime by prime, the exact lower-prime divisibility exclusions. On common lower primes they preserve all three forbidden residue classes and hence the exact collision condition `ell|h(q+r)`. No density approximation is made before `(7)`.

### Information intentionally forgotten

Passing to complete auxiliary-sieve densities forgets the physical interval endpoints, the conductor phase `R_a(m)` of `MC-495`, source coefficients, and the ordering of admissible `m` within the period. The common-core polynomial `(15)` also omits the one-sided primes `q<=ell<r`; these are restored explicitly by the tail factors `(17)`--`(18)` in the full normalized product.

Therefore `(9)` is an obstruction only to a **complete-period hard-mask-coherence** mechanism. It cannot be reused as an incomplete weighted-character estimate without an additional transfer theorem.

### Degeneracies and fibres

Primes dividing `h` collapse both shifted roots to zero. Small primes can saturate the residue space and make the joint support empty. Fixed excluded primes are absent by construction. All are finite/local effects handled explicitly or absorbed into `mathcal E`.

The map

\[
(q,r)\longmapsto
\{\ell:\ell\mid q+r\}
\tag{21}
\]

is highly many-to-one. The `q+r` collision pattern is therefore a compressed invariant, not an injective encoding of source-prime identity. No reconstruction claim is made.

### Canonicality and control representation

The signs in `(3)`--`(4)` are forced by the two native roots `q|n` and `r|n+h`; no arbitrary section or gauge chooses `q+r`. Repeating the same derivation for two same-root rows produces the `q-r` collision law already proved in `MC-491`. That same-root control is the simplest quotient/reparameterization comparator and verifies that `q+r` is genuine root-orientation data rather than notation.

## 5. Prior-art and novelty boundary

The general ingredients are classical. CRT factorization of sifted-set densities, local root counts of polynomial congruences, singular-series products, Mertens products, and higher-dimensional sieve language are established mathematics. `MC-472` already records the corresponding complete-period factorization boundary for this line, and `MC-484` records that the residual first-exit pair sieve is generically dimension two. No novelty is claimed for those tools or for viewing `(15)` through polynomial-sieve local densities.

The derived contribution is narrower: for the exact Mathia first-exit cross-root pair left unresolved by `MC-495`, the lower-prime mask has the explicit sign-sensitive collision law `ell|h(q+r)` and therefore the complete-period normalized overlap satisfies the logarithmic/totient ceiling `(9)`--`(10)`. A targeted prior-art audit found the expected classical local-density and higher-dimensional-sieve machinery, not a reason to promote this specialization to a new general sieve theorem.

Accordingly the result is classified `CLASSICAL-LOCAL-DENSITY+DERIVED-APPLICATION` and `NO-NOVELTY-CLAIM`.

## Boundaries and falsification tests

- **Complete auxiliary-sieve averaging is essential.** The result does not estimate the incomplete conductor-projected weight of `MC-495`.
- **Pairwise, not collective.** No operator-norm or many-row cancellation statement follows from the pairwise coherence bound alone.
- **Fixed-shift regime.** Constants may depend on the fixed integer shift `h`; if `h` is allowed to grow, its totient factors must be retained explicitly.
- **Exact local support.** If a small local factor has empty support, the corresponding pair is absent and the bound is trivial; it must not be regularized into a positive density.
- **No arbitrary replacement of masks.** Smooth or independent random masks do not preserve the collision arithmetic and are only controls, not proofs about the source-derived weight.
- **No hidden RH input.** The derivation uses finite congruence algebra, CRT factorization, Mertens' theorem, and elementary totient bounds; it does not use `1/zeta(s)` in the critical strip, a zero-free region, or an RH-equivalent estimate.

## Consequence for the live branch

`MC-495` left two genuine escape resources: a source-derived incomplete weight that correlates with the conductor phase, or a q-dependent signed/complex coefficient introduced before nonnegative aggregation. This finding narrows the first resource further. The **complete-period lower-prime hard mask alone** carries only `q+r` divisor coherence and pays at least the logarithmic ceiling `(10)`.

The next useful test is therefore endpoint-sensitive rather than another complete sieve-density calculation: derive how truncation of the exact first-exit rows projects the `q+r`-structured hard mask onto conductor residues and whether that centered profile can correlate with

\[
R_a(m)=\chi\!\left(1-\frac{h^2}{a^2m^2}\right)
\]

at a scale larger than the complete-period contribution after all source-width and reconstruction tariffs are restored. Alternatively, exhibit a genuinely q-dependent pre-aggregation sign/phase. Without one of those two mechanisms, the cross-root lower-prime mask has no conductor-power resource at the complete-period level.