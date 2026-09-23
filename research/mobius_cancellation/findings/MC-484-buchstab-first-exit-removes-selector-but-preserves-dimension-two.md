# MC-484 — Buchstab first exit removes the bracket selector but preserves the dimension-two pair sieve

**Status:** `CLASSICAL-IDENTITY` · `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-483` isolates the exact selector obstruction created by replacing the hard pair-sieve mask with an upper/lower bracket. That selector is **not** an unavoidable feature of the hard mask itself. A direct Buchstab first-exit decomposition eliminates it pointwise and retains an explicit prime factor. The price is equally exact: every first-exit branch is again a translated **dimension-two pair-sieve problem**, now on a shorter interval and with a moving arithmetic shift.

Let `P(t)` be the product of the active sieve primes below `t` in the current pair-sieve channel, with the same fixed exclusions as in `MC-471`--`MC-483`, and put

\[
F_h(n):=n(n+h),
\qquad
A_t(n):=\mathbf 1_{(F_h(n),P(t))=1}.
\tag{1}
\]

For `2<=w<=z`, the pointwise Buchstab identity is

\[
\boxed{
A_z(n)
=
A_w(n)
-
\sum_{\substack{w\le q<z\\ q\ \mathrm{active\ prime}}}
\mathbf 1_{q\mid F_h(n)}A_q(n).
}
\tag{2}
\]

The proof is just the uniqueness of the least active prime divisor of `F_h(n)` in `[w,z)`. Thus `(2)` is an **exact signed decomposition of the hard mask**, not a majorant/minorant and not a re-encoding through the bracket selector `theta` of `MC-483`.

Multiplying by the translated-ratio character phase

\[
K_h(n):=\chi(n+h)\overline{\chi(n)}
\tag{3}
\]

and summing over a source interval `I` gives

\[
\boxed{
\sum_{n\in I}K_h(n)A_z(n)
=
\sum_{n\in I}K_h(n)A_w(n)
-
\sum_{w\le q<z} T_q(I),
}
\tag{4}
\]

where

\[
T_q(I):=
\sum_{\substack{n\in I\\q\mid F_h(n)}}
K_h(n)A_q(n).
\tag{5}
\]

The important specialization is that `T_q` remains in the same structural family. Let

\[
R_q(h):=\{a\pmod q:a(a+h)\equiv0\pmod q\}.
\tag{6}
\]

For `q\nmid h`, `R_q(h)={0,-h}`; for `q\mid h` the two roots coincide. Parameterize one root branch by `n=a+qm`. Because `q` is distinct from the conductor prime `p`, if `\bar q_p` denotes the inverse of `q` modulo `p`, then

\[
K_h(a+qm)
=
\chi\!\left(m+(a+h)\bar q_p\right)
\overline{\chi\!\left(m+a\bar q_p\right)}.
\tag{7}
\]

After translating `m`, this is the same translated-ratio phase with separation

\[
\delta_{q,p}\equiv h\bar q_p\pmod p.
\tag{8}
\]

The roughness mask has the same closure property. Since `q` is invertible modulo `P(q)`, there is a unique CRT class `\delta_q (mod P(q))` satisfying

\[
q\delta_q\equiv h\pmod{P(q)}.
\tag{9}
\]

For a fixed root `a`, translation by the CRT class `a q^{-1}` modulo `P(q)` gives

\[
A_q(a+qm)
=
\mathbf 1_{(m(m+\delta_q),P(q))=1}
\tag{10}
\]

up to the harmless sign change `\delta_q -> -\delta_q` on the second root branch. Consequently every summand in `(5)` is, after an affine reparameterization, a translated-ratio character sum on an interval of length `H/q+O(1)` against another exact pair-sieve mask with cutoff `q`.

So Buchstab first exit does exactly what the accepted clue asked for at the algebraic level: it exposes a signed factor variable `q` **before** coefficientwise absolute values and removes the artificial upper/lower selector. But it does **not** reduce the sifting dimension or supply the conductor-power cancellation. The live problem becomes a bilinear/dispersion problem in the first-exit prime `q` and the shortened source variable `m`.

## 1. Exact proof of the first-exit identity

If `A_w(n)=0`, some active prime below `w` divides `F_h(n)`. Then `A_q(n)=0` for every `q>=w`, so both sides of `(2)` vanish.

Assume `A_w(n)=1`. If `A_z(n)=1`, no active prime in `[w,z)` divides `F_h(n)`, so the sum in `(2)` is empty. If `A_z(n)=0`, let `q` be the least active prime in `[w,z)` dividing `F_h(n)`. By minimality, `(F_h(n),P(q))=1`, hence `A_q(n)=1`. Every larger prime divisor `q'>q` has `A_{q'}(n)=0` because `q|P(q')`. Therefore exactly one term of the sum equals one. This proves `(2)` pointwise.

The argument is independent of sieve dimension and independent of the character phase. Multiplication by any coefficient sequence and summation preserves the identity, giving `(4)` without an information-loss step.

## 2. Reparameterization preserves the pair-sieve family

Take a root `a in R_q(h)` and write `n=a+qm`. For every active prime `r<q`, multiplication by `q^{-1}` modulo `r` is a bijection. The two forbidden residue classes for `n` modulo `r` therefore become two affine residue classes for `m`, separated by

\[
\delta_{q,r}\equiv hq^{-1}\pmod r.
\tag{11}
\]

The classes `(\delta_{q,r})_{r<q}` assemble by CRT into `(9)`. Thus the lower-prime condition is again the exclusion of the two classes `0` and `-\delta_q` modulo each generic `r<q`, with the usual collapse to one class when `r|\delta_q`. This is exactly the same local-density pattern as the original pair sieve:

\[
\nu_{\delta_q}(r)
=
\begin{cases}
1,&r\mid\delta_q,\\
2,&r\nmid\delta_q.
\end{cases}
\tag{12}
\]

In particular, the Buchstab step has not secretly converted the problem to a dimension-one linear sieve. It has moved the cutoff from `z` to `q`, shortened the interval by `q`, and made the shift depend on `q`, while retaining the generic two-residue local geometry.

The phase behaves compatibly by `(7)`--`(8)`: after a translation of the shortened interval, it is again a ratio of two translates of the same primitive character, with separation `h q^{-1}` modulo the conductor. The same first-exit prime therefore controls **both** the sieve shift and the character shift. That coupled dependence is the new resource preserved by `(4)`.

## 3. Why the identity alone does not buy a power saving

The pointwise decomposition is lossless, but triangle bounding its new prime branches immediately destroys the resource it exposed. Since `F_h(n)=0 mod q` has at most two residue classes modulo an active prime `q`,

\[
|T_q(I)|
\le
2\left(\frac{H}{q}+1\right).
\tag{13}
\]

Therefore a purely absolute treatment of the first-exit sum gives only the harmonic/endpoint scale

\[
\sum_{w\le q<z}|T_q(I)|
\ll
H\sum_{w\le q<z}\frac1q
+\pi(z),
\tag{14}
\]

with no fixed conductor power saved. Equation `(14)` is not asserted to be sharp; it marks the exact failure mode. The first-exit representation is useful only if the `q` variable is kept coupled to the inner translated-ratio phase and pair-sieve condition through a bilinear, dispersion, reciprocity, or comparable estimate.

This is materially different from `MC-482`--`MC-483`. There the transfer loss appears **before** the analytic estimate because positive bracketing leaves an uncontrolled selector. Here there is no selector: the hard mask itself supplies the signed decomposition. The unresolved cost is analytic cancellation across a moving family of exact lower-cutoff pair-sieve sums.

## 4. The tempting Iwaniec bilinear-remainder transfer has a dimension gate

There is important nearby prior art, but it cannot be imported as a black box.

Henryk Iwaniec's paper *A new form of the error term in the linear sieve*, Acta Arithmetica 37 (1980), 307--320, DOI `10.4064/aa-37-1-307-320`, is precisely a classical source for reorganizing **linear-sieve** remainder terms into factorable/bilinear structure. Jacek Pomykała's *Bilinear form of the remainder term in the Rosser-Iwaniec sieve of dimension kappa in (1/2,1)*, Acta Arithmetica 52 (1989), 293--306, DOI `10.4064/aa-52-3-293-306`, explicitly extends that bilinear-remainder viewpoint only through the stated subunit dimension range.

The current hard mask has generic sieve dimension `kappa=2`, as `(12)` makes explicit. Higher-dimensional sieve theory treats `kappa>1` as a separate regime; Harold Diamond, Heini Halberstam and William Galway's *A Higher-Dimensional Sieve Method* (Cambridge Tracts in Mathematics 177, 2008, DOI `10.1017/CBO9780511542909`) develops that regime separately, with the twin-prime/two-residue pattern as the standard dimension-two example. Recent work such as Runbo Li, *A note on variants of Buchstab's identity*, arXiv:`2504.07974` (2025), likewise studies Buchstab-type iterations specifically for `kappa>1`.

Thus the classical bilinear nature of the **linear** Rosser-Iwaniec remainder is strong evidence that a factor-retaining architecture is mathematically natural, but it is not a theorem about `(4)`. A valid transfer to this line must either:

1. prove a dimension-two analogue compatible with the exact density `(12)` and the moving character shift `(8)`;
2. decompose `(4)` into genuine dimension-one pieces without losing the coupling or reintroducing exponential branch multiplicity; or
3. derive a different bilinear/dispersion identity directly for the `q,m` family.

The targeted prior-art audit found the classical linear/subunit bilinear-remainder theorems and modern higher-dimensional Buchstab/sieve frameworks, but no basis for treating the needed dimension-two, character-coupled estimate as already supplied by those results. This is a boundary statement, not a novelty claim or a literature-completeness claim.

## 5. Consequence for the accepted q-vdC clue

The first alternative in the clue -- find an exact signed/factorable representation before scalarization -- is now partially resolved. **An exact selector-free signed representation exists:** Buchstab first exit `(2)`--`(5)`.

What remains is no longer the algebraic existence question. The decisive empty-vector test is whether the moving family

\[
\sum_{w\le q<z}
\sum_{m\in I_{q,a}}
K_{\delta_{q,p}}(m)
\mathbf 1_{(m(m\pm\delta_q),P(q))=1}
\tag{15}
\]

admits a conductor-sensitive bilinear/dispersion estimate after summing over the one or two root branches `a in R_q(h)`, with all source weights and endpoint tariffs retained. A proof must exploit the coupled `q` dependence before taking absolute values. Merely invoking the factorability of a classical linear-sieve remainder, or applying a bound independently to every `q`, does not pass the dimension and recombination gates above.

Equation `(15)` also gives a clean falsification target. If no estimate stronger than the absolute budget `(14)` survives after the exact source coefficients and q-vdC weights are restored, then Buchstab iteration is only a lossless change of coordinates and the route should move to the separately retained nonempty/boundary or cross-component channels. Conversely, a genuine power gain for `(15)` would evade both the positive-bracket selector obstruction of `MC-483` and the full-primorial spectral explosion of `MC-473`--`MC-475`.

## Prior art and novelty boundary

- Buchstab's identity and its iteration in sieve theory are classical. No novelty is claimed for `(2)` as a sieve identity.
- Iwaniec's 1980 factorable/bilinear linear-sieve remainder and Pomykała's 1989 subunit-dimensional extension are established prior art; they motivate but do not prove the needed dimension-two estimate.
- Higher-dimensional sieve theory and Buchstab variants for `kappa>1` are established subjects. No novelty is claimed for recognizing the pair-sieve density as dimension two.
- The Mathia-specific content is the exact **source-frame audit**: specializing first exit to the hard mask left by `MC-483`, proving the simultaneous reparameterizations `(7)`--`(12)`, and locating the remaining proof obligation as the coupled moving-shift bilinear family `(15)` rather than an uncontrolled bracket selector.

## Boundaries and falsification tests

- **No conductor-power estimate is proved.** Equation `(4)` is exact bookkeeping; `(14)` shows that absolute recombination is not enough.
- **No dimension-two bilinear sieve theorem is claimed.** Any use of Iwaniec/Pomykała must match the actual sieve dimension and hypotheses rather than transfer the word "bilinear" by analogy.
- **The moving shifts are load-bearing.** Replacing `delta_q` or `delta_{q,p}` by a fixed generic shift discards precisely the common `q` dependence exposed by first exit.
- **The residual hard mask remains exact.** Replacing `A_q` by a positive envelope reopens the `MC-479`--`MC-483` transfer issues unless a new signed theorem is supplied.
- **Iterating Buchstab is not automatically progress.** Each further step introduces another ordered prime variable; a useful iteration must terminate in ranges with an independently controlled analytic estimate rather than merely expanding the tree.
- **Root collisions must be retained.** When a sieve prime divides the current shift, the two forbidden classes merge; all dimension and density estimates must account for those exceptional primes exactly.

## Consequence for the research line

The bracket-selector obstruction is now separated from the hard-mask problem. Positive upper/lower replacement loses the selector; exact Buchstab first exit retains the missing factor without a selector, but preserves the dimension-two pair sieve and converts the frontier into a moving-prime bilinear problem.

The next useful advance is therefore a theorem or obstruction for `(15)`: either a conductor-sensitive dimension-two bilinear/dispersion estimate that keeps the first-exit prime coupled to the translated-ratio phase, or a proof that the available source geometry forces any such recombination back to the known harmonic/endpoint tariffs. No improved bound for `M(x)`, no zero-free region, and no RH consequence follows from this finding.