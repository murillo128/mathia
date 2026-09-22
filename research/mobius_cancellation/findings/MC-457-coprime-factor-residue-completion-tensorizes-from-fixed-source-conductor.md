# MC-457 — Coprime factor-residue completion tensorizes from the fixed source conductor

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CRT-TENSORIZATION` · `FACTOR-RESIDUE-COMPLETION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-456` shows how Pascadi/Yang-type dispersion can make internal factors analytically visible when those factors are themselves parts of the arithmetic-progression modulus before completion. The most direct attempt to imitate that mechanism in the present fixed-conductor source frame is to **refuse to recombine one internal sieve factor**, keep its divisibility condition as a separate congruence modulus, and complete the translated character sum while that factor is still explicit.

For the complete part of the source sum, this does not break the quotient. The reason is exact CRT tensorization.

Let `q,r>=1` satisfy `(q,r)=1`, and let `F:Z->C` be `q`-periodic. For every residue `c (mod r)`,

\[
\boxed{
\sum_{\substack{t\bmod qr\\t\equiv c\pmod r}}F(t)
=
\sum_{x\bmod q}F(x).
}
\tag{1}
\]

Equivalently, for additive factor frequencies `a (mod r)`,

\[
\boxed{
\sum_{t\bmod qr}F(t)e(at/r)
=
\begin{cases}
r\displaystyle\sum_{x\bmod q}F(x),&a\equiv0\pmod r,\\
0,&a\not\equiv0\pmod r.
\end{cases}
}
\tag{2}
\]

Thus every nonzero Fourier mode introduced solely to remember the separate factor congruence vanishes on a complete mixed `q r` block. The surviving zero mode is exactly the original complete source average; it contains no factor-specific oscillation.

For the primitive translated-character kernel

\[
F_h(t):=\chi(t+h)\overline{\chi(t)},
\tag{3}
\]

`MC-413` gives

\[
\sum_{x\bmod q}F_h(x)=c_q(h).
\tag{4}
\]

Hence, whenever `(r,q)=1`,

\[
\boxed{
\sum_{\substack{t\bmod qr\\t\equiv c\pmod r}}
\chi(t+h)\overline{\chi(t)}
=c_q(h),
}
\tag{5}
\]

independently of `r` and `c`. The same holds after any affine reparametrization `t=t_0+bj` with `(b,q)=1`: a block of `q` consecutive selected samples traverses all source residues modulo `q`, so its complete contribution is again `c_q(h)`.

This applies directly to a pre-recombined well-factorable divisor component. On the squarefree upper-sieve support relevant to `MC-409`--`MC-456`, every contributing divisor factor is coprime to the primitive source conductor because `(de,q)>1` makes the shifted kernel vanish. If one internal factor is left as a separate congruence after the other compatible divisor constraints are solved, its independent part is therefore a modulus `r` coprime to `q`. Parameterizing that residue class produces a `q`-periodic translated source sequence, and `(1)`--`(5)` show that complete source blocks forget the separate factor exactly.

For an incomplete interval containing `J=Bq+s` selected samples, `0<=s<q`, the same argument gives

\[
\boxed{
B\,c_q(h)+E,
\qquad |E|\le s<q.
}
\tag{6}
\]

Consequently the only factor-specific dependence created by this **sequential congruence / partial-completion** maneuver lies in the incomplete boundary term. Merely preserving a factor as a separate coprime progression modulus before completion does not reproduce the Pascadi/Yang quotient-breaking mechanism in the complete bulk.

This is stronger than simply collapsing the internal factors to their product and invoking `MC-413`: it checks the most obvious alternative ordering explicitly. Even when a factor congruence is Fourier-detected before multiplication collapse, the mixed transform is a tensor product of a `q`-periodic source factor and an `r`-residue factor, so the nontrivial `r`-frequencies are exact null modes on complete blocks.

The result does **not** rule out incomplete factor-specific dispersion. A surviving transfer must exploit the incomplete mixed blocks collectively, or create a non-product arithmetic relation before completion so that the source phase and the factor modulus no longer live on independent CRT coordinates. No improved character-sum estimate, Möbius bound, zero-free region, or RH consequence follows.

## 1. CRT tensorization lemma

Because `(q,r)=1`, reduction modulo `q` and modulo `r` gives a bijection

\[
\mathbf Z/(qr)\mathbf Z
\cong
\mathbf Z/q\mathbf Z\times\mathbf Z/r\mathbf Z.
\tag{7}
\]

Fixing `t=c (mod r)` leaves exactly one representative modulo `qr` for every residue `x (mod q)`. Since `F(t)` depends only on the first CRT coordinate, summing over that fibre proves `(1)` immediately.

For `(2)`, under the same CRT bijection the factor `e(at/r)` depends only on the second coordinate. Therefore

\[
\sum_{t\bmod qr}F(t)e(at/r)
=
\left(\sum_{x\bmod q}F(x)\right)
\left(\sum_{y\bmod r}e(ay/r)\right),
\tag{8}
\]

and additive orthogonality gives `(2)`.

The point for the current branch is not the elementary identity itself but its interpretation. Introducing additive characters to keep a coefficient factor `r` separate does create formal dual labels `a (mod r)`, yet all `a!=0` labels are orthogonal to the complete fixed-conductor source block. They are not the reciprocal/Kloosterman modes of `MC-456`; before truncation they are a tensor factor that cancels exactly.

## 2. Application to translated primitive-character correlations

Take `F=F_h` from `(3)`. It is `q`-periodic. For primitive `chi`, the finite Fourier/Gauss transform gives the classical autocorrelation identity

\[
\sum_{x\bmod q}\chi(x+h)\overline{\chi(x)}=c_q(h),
\tag{9}
\]

already derived and audited in `MC-413`. Substitution into `(1)` yields `(5)`.

The result is invariant under the affine progressions that arise after solving some of the sieve congruences. If

\[
n=n_0+b(c+rj),
\qquad (br,q)=1,
\tag{10}
\]

then as `j` runs through `q` consecutive values, `n (mod q)` runs through every source residue exactly once. Hence

\[
\sum_{j=J}^{J+q-1}
\chi(n_0+b(c+rj)+h)
\overline{\chi(n_0+b(c+rj))}
=c_q(h).
\tag{11}
\]

No internal-factor label survives in the complete source oscillation. Different factor representatives can still alter coefficient weights, interval endpoints, compatibility conditions, or the number of complete blocks; those are outer arithmetic data, not new complete source phases.

## 3. Why sequential factor congruences do not yet imitate Pascadi/Yang

For one well-factorable component, write a squarefree product divisor as

\[
d=r_1r_2,
\qquad (r_1,r_2)=1,
\tag{12}
\]

and similarly on the second copy. A natural pre-quotient tactic is to solve all but the `r_1` congruence and leave

\[
t\equiv c_{r_1}\pmod{r_1}
\tag{13}
\]

visible while transforming the source variable. Since every surviving sieve divisor is coprime to `q`, the independent part of `r_1` is coprime to the source conductor. Equations `(1)`--`(6)` then apply to the resulting periodic source sequence.

In additive Fourier language, detecting `(13)` contributes modes `e(a(t-c_{r_1})/r_1)`. A complete transform over the natural mixed period `q r_1` kills every `a!=0` mode by `(2)`. Keeping `r_1` separate has therefore not created a complete oscillatory kernel that varies inside the multiplication fibre `r_1r_2=d`.

This is structurally different from the Pascadi/Yang setting audited in `MC-456`. There the factor blocks are parts of the **same progression modulus that constrains the arithmetic source variables**. Dispersion duplicates different modulus blocks and completion produces reciprocal phases in which those blocks occupy asymmetric numerator/denominator roles. The resulting transformed kernel is not a tensor product of an external periodic source factor and an independent residue mask.

Here the primitive character conductor is external and coprime to the sieve factors. If the only new operation is to retain a factor as an extra congruence mask and then fully complete, CRT separates the two modulus systems before any reciprocal interaction can arise.

## 4. The surviving incomplete boundary

Let the selected arithmetic progression contain `J` samples after the factor congruence is imposed. Writing `J=Bq+s`, `0<=s<q`, partition the sample index into `B` full source periods plus one final block. Equation `(11)` evaluates every full period and yields `(6)`.

Thus factor-specific starting residues and the order in which coprime factor congruences were imposed can affect only:

- the number `B` of complete source blocks through interval geometry;
- the final incomplete translated-character sum of fewer than `q` selected samples;
- outer coefficient and compatibility data.

The second item is the only place where the separate factor residue can remain inside the source oscillation. It is not automatically small: in the large-conductor regime the entire useful interval may be shorter than one source period. This finding therefore does not close the accepted clue. It moves its transfer test one step further: **full completion after merely exposing a coprime factor congruence is a dead end; any genuine factor-specific gain must live before that tensorization or in collective control of the incomplete tails.**

A quantitative continuation must keep those tails coupled across factor representatives and show that the resulting diagonal/off-diagonal budget beats the product-level occupancy tariff. Bounding each tail independently by a standard short-character estimate and then summing absolutely would return to the already classified source-cost problem.

## 5. Prior art and novelty boundary

The mathematics used in `(1)`--`(2)` is the Chinese remainder theorem and finite additive-character orthogonality. The periodic/Fourier framework is classical; NIST DLMF §27.10 records finite Fourier expansions of periodic arithmetic functions and the separable Gauss transform of primitive Dirichlet characters, including the finite Fourier expansion used throughout `MC-411`--`MC-413` (https://dlmf.nist.gov/27.10). No novelty is claimed for these identities.

The primitive-character autocorrelation `(9)` is the Ramanujan-sum identity already audited in `MC-413`. The current contribution is a frontier-specific ordering check: it proves that **keeping one internal coprime sieve factor as a separate residue modulus before complete source Fourier analysis still tensorizes**, so this simplest pre-product implementation of the factor-specific transfer criterion from `MC-456` does not work in the complete bulk.

The comparison with current well-factorable dispersion prior art remains exactly the one in `MC-456`: Alexandru Pascadi, *On the exponents of distribution of primes and smooth numbers*, arXiv:2505.00653, and Zhiyuan Yang, *Convolution-type Bombieri-Vinogradov theorem with well-factorable Weights, and its applications*, arXiv:2608.13299. Their theorems establish that factor-specific quotient breaking can be analytically useful when factor blocks participate in progression-modulus geometry; they do not contradict the CRT tensorization above for an independent fixed character conductor.

A targeted literature search on 22 September 2026 found the CRT/Fourier ingredients as standard and the Pascadi/Yang architecture as the closest modern comparison, but no theorem that converts an independent coprime sieve-factor residue mask attached to a fixed primitive-character correlation into a complete factor-specific source phase. No novelty claim is made from that absence.

## Boundaries and falsification tests

- **Coprimality is load-bearing.** The tensorization uses `(q,r)=1`. In the present shifted sieve kernel this is exactly the surviving regime because a sieve divisor sharing a source-conductor prime makes one character factor vanish. A future representation in which a useful internal modulus genuinely shares source-conductor primes would fall outside this statement and must first avoid that vanishing mechanism.
- **Only the complete bulk is classified.** Incomplete mixed blocks retain nonzero factor-frequency modes. Their collective estimation remains live.
- **Outer interval geometry can depend on the factor representative.** The theorem does not call that dependence fake; it says it is not complete source-phase occupancy. Any gain from endpoint geometry must be quantified separately.
- **Sequential congruence ordering may still matter before completion.** A dispersion/Cauchy/reciprocity step applied while several incomplete factor-conditioned families are coupled is not covered if it creates a kernel that is no longer a tensor product of a `q`-periodic source function and an independent residue mask.
- **No claim covers a shared or variable arithmetic modulus.** Pascadi/Yang lie outside the no-go because their factor blocks occur inside the progression modulus itself and survive dispersion into reciprocal phases.
- **No individual short-sum saving is asserted.** Equation `(6)` gives only an exact complete/incomplete decomposition; it does not improve Burgess, q-vdC, or any incomplete character estimate.
- **No zeta input is used.** The argument is finite CRT/Fourier algebra and does not use analytic continuation, zero-free regions, or RH.

## Consequence for the research line

`MC-454` proved that merely exposing internal factor tuples does not increase source occupancy; `MC-455` proved that standard source-only `q`-vdC preserves the product quotient; `MC-456` then identified successful modern prior art in which factor blocks really do enter distinct modulus roles before dispersion. The present calculation tests the most immediate transfer of that idea back to the Möbius source frame and finds an exact obstruction: **an internal factor used only as an additional coprime residue modulus is CRT-independent of the fixed primitive-character conductor, so complete source analysis annihilates its nonzero factor modes.**

The accepted factor-specific-dispersion clue should therefore narrow again. The next live calculation is not to split another divisor congruence and fully complete it. It is to keep the incomplete factor-conditioned families coupled through the first dispersion/Cauchy/reciprocity step and ask whether that operation creates a genuinely non-tensor kernel before completion. If it does not, the fixed external conductor is becoming a structural no-go for the Pascadi/Yang transfer; if it does, the resulting incomplete mixed kernel and its true diagonal become the next quantitative object.