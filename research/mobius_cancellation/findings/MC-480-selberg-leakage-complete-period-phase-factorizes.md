# MC-480 — Selberg leakage complete-period phase factorizes

**Status:** `EXACT-DERIVED` · `CLASSICAL-IDENTITY` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The translated-ratio character phase cannot cancel the Selberg false-positive leakage of `MC-479` on a complete joint period. Once the leakage is viewed as a function of the small-prime sieve coordinate, the same CRT tensor-product mechanism isolated in `MC-472` applies exactly: the complete character factor is `-1`, so the twisted leakage is **minus its total positive mass**.

Let `p` be prime, let `chi` be a nonprincipal character modulo `p`, and let

\[
K_h(n)=\chi(n+h)\overline{\chi(n)},
\qquad h\not\equiv0\pmod p.
\tag{1}
\]

Let `W` be square-free with `(W,p)=1`. Let `A_{W,h}` be the exact two-sided pair-sieve mask and let `beta_{W,h}` be a Selberg envelope built only from the active primes dividing `W`, so both are `W`-periodic. Define the false-positive leakage

\[
L_{W,h}(n):=\beta_{W,h}(n)-A_{W,h}(n).
\tag{2}
\]

For the Ramaré--Ruzsa envelope used in `MC-477`--`MC-479`, `MC-479` proves

\[
L_{W,h}(n)\ge0
\quad\text{and}\quad
L_{W,h}(n)=0\ \text{on every exact survivor}.
\tag{3}
\]

Then the complete joint-period leakage sum factorizes exactly as

\[
\boxed{
\sum_{n\bmod pW}K_h(n)L_{W,h}(n)
=-\sum_{b\bmod W}L_{W,h}(b).
}
\tag{4}
\]

Equivalently, if

\[
\ell_W(h):=\frac1W\sum_{b\bmod W}L_{W,h}(b),
\tag{5}
\]

then

\[
\boxed{
\frac1{pW}\sum_{n\bmod pW}K_h(n)L_{W,h}(n)
=-\frac{\ell_W(h)}p.
}
\tag{6}
\]

Thus the complete-period character coupling does not reduce positive leakage at all beyond the universal translated-ratio mean `-1/p`. In unnormalized form the phase converts the total leakage mass to its negative exactly.

For the same exact mask, `MC-472` gives

\[
\sum_{n\bmod pW}K_h(n)A_{W,h}(n)
=-\sum_{b\bmod W}A_{W,h}(b).
\tag{7}
\]

Hence whenever the survivor mass is nonzero,

\[
\boxed{
\frac{\left|\sum_{n\bmod pW}K_h(n)L_{W,h}(n)\right|}
     {\left|\sum_{n\bmod pW}K_h(n)A_{W,h}(n)\right|}
=
\frac{\sum_{b\bmod W}L_{W,h}(b)}
     {\sum_{b\bmod W}A_{W,h}(b)}.
}
\tag{8}
\]

Specialize now to the active-prime product `W_z` and Selberg envelope of `MC-479`. On the surviving shift channel for which the exact pair sieve is nonempty, `MC-479` proves

\[
\frac{\operatorname{mean}_{W_z}L_{W_z,h}}
     {\operatorname{mean}_{W_z}A_{W_z,h}}
\ge
\frac{\log 2+o(1)}{\log z}.
\tag{9}
\]

Combining `(8)` and `(9)` gives

\[
\boxed{
\frac{\left|\sum_{n\bmod pW_z}K_h(n)L_{W_z,h}(n)\right|}
     {\left|\sum_{n\bmod pW_z}K_h(n)A_{W_z,h}(n)\right|}
\ge
\frac{\log 2+o(1)}{\log z}.
}
\tag{10}
\]

So coupling to `K_h` does **not** turn the known complete-period Selberg leakage into a conductor-power-small error. The only remaining place for a `K_h`-sensitive gain is incomplete-period discrepancy, boundary structure, or a different signed/factorable surrogate.

For an interval `I`, the right centered target is therefore

\[
\mathcal E_{W,h}(I)
:=
\sum_{n\in I}K_h(n)L_{W,h}(n)
+\frac{|I|}{p}\ell_W(h),
\tag{11}
\]

so that

\[
\sum_{n\in I}K_h(n)L_{W,h}(n)
=-\frac{|I|}{p}\ell_W(h)+\mathcal E_{W,h}(I).
\tag{12}
\]

The live restriction-style question is now an estimate for the **centered incomplete leakage discrepancy** `\mathcal E_{W,h}(I)`, not whether complete-period character oscillation suppresses the leakage mass. No estimate for `(11)` is proved here.

## 1. The leakage is a pure sieve-coordinate function

The exact pair-sieve mask depends only on `n mod W`. The Ramaré--Ruzsa Selberg envelope used in this branch is a square of a divisor sum over square-free moduli composed from the same active sieve primes. Every such modulus divides `W`, hence `beta_{W,h}` is also `W`-periodic. Therefore the difference `L_{W,h}` in `(2)` depends only on the `W`-coordinate.

This is the only structural input needed beyond `MC-472`. The argument does not use positivity yet and applies to any `W`-periodic replacement error. Positivity becomes decisive when `(4)` is interpreted: because `L>=0`, the right side has no internal cancellation to recover after the CRT factorization.

## 2. CRT forces exact tensorization

Because `(p,W)=1`, CRT identifies

\[
\mathbb Z/(pW)\mathbb Z
\cong
\mathbb Z/p\mathbb Z\times\mathbb Z/W\mathbb Z.
\tag{13}
\]

Under this identification, `K_h` depends only on the first coordinate and `L_{W,h}` only on the second. Hence

\[
\sum_{n\bmod pW}K_h(n)L_{W,h}(n)
=
\left(\sum_{a\bmod p}K_h(a)\right)
\left(\sum_{b\bmod W}L_{W,h}(b)\right).
\tag{14}
\]

`MC-472` derives the classical complete correlation

\[
\sum_{a\bmod p}\chi(a+h)\overline{\chi(a)}=-1
\tag{15}
\]

for `h not congruent to 0 mod p`, by the bijection `a -> 1+h/a` from the nonzero contributing residues to `F_p^times\setminus{1}`. Substitution into `(14)` proves `(4)`.

The same calculation applied to `A_{W,h}` is precisely the complete-period factorization already stored in `MC-472`, giving `(7)` and then `(8)`.

## 3. The current Selberg leakage inherits the logarithmic lower bound unchanged

`MC-479` identifies explicit false-positive residue classes that violate exactly one active sieve prime `r` with `z/2<r<z`. On those classes the exact mask is zero while the envelope weight is

\[
1+O(1/\log z).
\tag{16}
\]

Summing these disjoint classes over one complete sieve period yields `(9)`. Equation `(4)` shows that completing also in the conductor coordinate does not decorrelate them from `K_h`: the conductor coordinate contributes exactly the scalar `-1`.

This is stronger than saying that a triangle inequality loses phase. There is no hidden complete-period phase saving being discarded by the triangle inequality; on the full CRT product the exact twisted leakage already has magnitude equal to the positive leakage mass.

The relative statement `(10)` should be used only when the exact pair-sieve survivor mass is nonzero. In particular, when `2|W_z` and `h` is odd, `MC-472` shows that the rough×rough pair-sieve channel vanishes identically, so the ratio in `(10)` is not the relevant object. The live channel is the nonempty survivor case, including the even-shift branch when `z>2`.

## 4. Consequence for incomplete intervals

A source interval generally sees only a small part of the enormous joint period `pW_z`. Therefore `(4)` does not itself give a source-scale lower bound. It instead determines what must be subtracted before asking for cancellation.

The natural decomposition is `(12)`. Any proposed conductor-sensitive treatment of Selberg leakage must now explain why the centered incomplete discrepancy `\mathcal E_{W,h}(I)` is small after all source-length, shift, Fejér, endpoint, normalization, and depth costs are charged. A proof that merely completes to `pW_z`, averages over full CRT fibers, or invokes orthogonality of the conductor character cannot provide that gain: the complete block is already fixed by `(4)`.

This leaves three materially different possibilities:

- exploit genuinely incomplete character/sieve discrepancy before complete-period tensorization;
- find a signed or factorable surrogate whose replacement error retains cancellative structure in the `W`-coordinate rather than the positive leakage of `(3)`;
- abandon this base-channel transfer and seek the needed signed information in first-exit boundary, nonempty rough-block, or pre-positive cross-component terms.

No one of these possibilities is established by this finding.

## 5. Prior art and novelty boundary

The character identity `(15)` and the CRT tensor-product argument are classical and were already audited in `MC-472`; this finding does not claim a new character-sum theorem. The Selberg-envelope construction and exact-on-survivors property are classical and were audited in `MC-479` against Ramaré--Ruzsa and the Bera--Viswanadham restriction framework.

A targeted literature check on 23 September 2026 also found Yixiu Xiao and Hongze Li, *Selberg sieve weights and sign changes of Kloosterman sums. I. Uniform asymptotics for shifted weights*, arXiv `2609.24248`, and Part II, arXiv `2609.24255`. Those papers provide close modern prior art for retaining shifted Selberg-weight structure in an oscillatory problem, but their oscillatory object is Kloosterman and their theorems do not supply the incomplete translated-ratio character estimate `(11)`. No theorem transfer or novelty claim is made here.

The durable contribution is only the **candidate-specific composition** of the already established facts `MC-472` and `MC-479`: the exact current leakage is a pure sieve-coordinate function, so complete-period coupling to the translated-ratio phase reproduces its positive mass rather than cancelling it. This closes complete-period phase cancellation as an escape for the accepted low-denominator envelope route.

## Boundaries and falsification tests

- **`h not congruent to 0 mod p` is essential.** The complete character factor is not `-1` at zero shift.
- **`(p,W)=1` is essential for the tensor product.** The current source setup removes the conductor prime from the sieve coordinate exactly as in `MC-472`.
- **The envelope must be `W`-periodic.** This holds for the current active-prime Selberg envelope; a replacement using genuinely conductor-coupled coefficients would require a fresh analysis.
- **Complete-period factorization is not a short-interval lower bound.** Large cancellation in `(11)` remains possible and is precisely the unresolved question.
- **The relative logarithmic lower bound requires nonzero survivor mass.** Odd-shift parity-vanishing cases are handled separately by `MC-472`.
- **A signed surrogate is not ruled out.** Equation `(4)` diagnoses the current positive Selberg leakage, not every possible exact-to-surrogate transfer.
- **No Möbius, Mertens, zero-free-region, or RH consequence follows.** This is a structural obstruction inside one candidate representation.

## Consequence for the research line

The accepted low-denominator restriction clue should no longer ask whether simply coupling `K_h` to the positive Selberg leakage creates cancellation on average. On every complete joint CRT block, it does the opposite: the twisted leakage has exactly the magnitude of the leakage mass.

The decisive object is now the centered incomplete discrepancy `(11)`. A positive continuation must prove a strict conductor-power estimate for that quantity, or replace the positive envelope by a signed/factorable surrogate with an independently proved matching theorem. If neither survives full source-budget accounting, the Selberg-envelope transfer for the empty-vector base component is closed.