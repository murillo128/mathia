# MC-479 — Selberg envelope leakage is order-one on near-cutoff single violations

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `CLASSICAL-IDENTITY` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The signed exact-to-envelope interface left open by `MC-477`--`MC-478` can be sharpened substantially. For the Ramaré--Ruzsa Selberg envelope used by the low-denominator restriction route, the problem is **not** approximation error on genuine pair-sieve survivors: the envelope equals the exact indicator there. The whole replacement error is positive **false-positive leakage**, and that leakage is pointwise order one on an explicit family of residues that violate exactly one sieve condition near the cutoff.

Let the pair sieve have local forbidden set

\[
\mathcal L_r(h)=\{0,-h\}\pmod r,
\qquad
\nu_r(h):=|\mathcal L_r(h)|\in\{1,2\},
\tag{1}
\]

for each active sieve prime `r<z`; the two classes coalesce when `r|h`. Write

\[
A_z(n):=\mathbf 1_{n\bmod r\notin\mathcal L_r(h)\ \forall r<z}
\tag{2}
\]

for the exact pair-sieve indicator. In the Ramaré--Ruzsa notation the Selberg envelope is

\[
\beta_z(n)
=
\left(
\sum_{\substack{d:\ n\bmod d\in\mathcal L_d}}
\Lambda_d
\right)^2,
\qquad
\Lambda_d=\mu(d)\frac{G_d(z)}{G_1(z)},
\tag{3}
\]

with `\Lambda_1=1`; only the squarefree active sieve moduli occur.

Then:

1. **Exact agreement on survivors.** If `A_z(n)=1`, only `d=1` contributes to `(3)`, hence

\[
\boxed{\beta_z(n)=1=A_z(n).}
\tag{4}
\]

Thus

\[
\boxed{\beta_z-A_z=\beta_z\,\mathbf 1_{A_z=0}\ge0.}
\tag{5}
\]

2. **Near-cutoff single violations carry almost full envelope weight.** Suppose `r` is an active prime with

\[
\frac z2<r<z
\tag{6}
\]

and `n` violates the local condition at `r` but satisfies every other active condition below `z`. Then only `d=1,r` contribute to `(3)`. Ramaré--Ruzsa's exact formula

\[
G_d(z)
=
\frac d{|\mathcal L_d|}
\sum_{\substack{d\mid \ell\le z}}
\frac{\mu^2(\ell)|\mathcal L_\ell|}{|\mathcal K_\ell|}
\tag{7}
\]

has only `\ell=r` in the `d=r` sum because `2r>z`. Therefore

\[
G_r(z)=\frac{r}{r-\nu_r(h)},
\tag{8}
\]

and the false-positive envelope value is exactly

\[
\boxed{
\beta_z(n)
=
\left(
1-
\frac{r}{(r-\nu_r(h))G_1(z)}
\right)^2.
}
\tag{9}
\]

For the translated pair sieve, `G_1(z)\gg\log z` uniformly after deleting at most the fixed/isolated primes already removed by the source setup: termwise its local sieve density dominates the ordinary dimension-one Selberg `G`-sum. Since `r/(r-\nu_r)=1+O(1/r)` in `(6)`, `(9)` gives

\[
\boxed{\beta_z(n)=1+O\!\left(\frac1{\log z}\right)}
\tag{10}
\]

uniformly on these single near-cutoff violations. In particular, the majorant is not a pointwise approximation to the hard mask: there are false positives on which `A_z=0` while `\beta_z` tends to `1`.

3. **Even complete-period average leakage is only logarithmically smaller than the survivor mass.** Let

\[
W_z:=\prod_{r<z}r,
\qquad
\Delta_z:=\prod_{r<z}\left(1-\frac{\nu_r(h)}r\right),
\tag{11}
\]

with the products taken over the active sieve primes. Then `\Delta_z` is exactly the density of `A_z=1` modulo `W_z`. For an active `r`, let `E_r` be the residue classes modulo `W_z` that violate the condition at exactly `r` and satisfy every other local condition. Chinese remaindering gives

\[
\frac{|E_r|}{W_z}
=
\Delta_z\frac{\nu_r(h)}{r-\nu_r(h)}.
\tag{12}
\]

The sets `E_r` are disjoint. Combining `(9)` and `(12)` over `z/2<r<z` yields the exact lower bound

\[
\frac1{W_z}
\sum_{n\bmod W_z}(\beta_z(n)-A_z(n))
\ge
\Delta_z
\sum_{z/2<r<z}
\frac{\nu_r(h)}{r-\nu_r(h)}
\left(
1-
\frac{r}{(r-\nu_r(h))G_1(z)}
\right)^2.
\tag{13}
\]

Since `\nu_r(h)\ge1`, Mertens' theorem for reciprocal primes on the dyadic interval gives, after deleting at most the isolated source-conductor prime,

\[
\sum_{z/2<r<z}
\frac{\nu_r(h)}{r-\nu_r(h)}
\ge
\frac{\log 2+o(1)}{\log z}.
\tag{14}
\]

Together with `(10)`, this gives

\[
\boxed{
\frac{\operatorname{mean}_{W_z}(\beta_z-A_z)}
     {\operatorname{mean}_{W_z}A_z}
\ge
\frac{\log 2+o(1)}{\log z}.
}
\tag{15}
\]

So even on the natural complete local period, the positive leakage is at best logarithmically smaller than the exact survivor mass solely from this explicit one-violation family. It cannot supply a fixed conductor-power saving by a phase-blind `L^1` or `L^\infty` replacement when the sieve cutoff is in the polynomial source regime.

The consequence for the live twisted sum is exact. With

\[
K_h(n)=\chi(n+h)\overline{\chi(n)},
\]

one has

\[
\sum_{n\in I}K_h(n)A_z(n)
=
\sum_{n\in I}K_h(n)\beta_z(n)
-
\sum_{n\in I}K_h(n)(\beta_z(n)-A_z(n)).
\tag{16}
\]

`MC-478` controls the first term through the low-denominator Fourier representation. The second term is now identified as a positive false-positive leakage weight that is **not small pointwise and is not power-small relative to the survivor mass even on a complete sieve period**. Therefore the remaining exact-to-envelope step cannot succeed by showing that `\beta_z-A_z` is a small unsigned error. It must obtain cancellation of `K_h` **against the leakage set itself**, retain a genuinely signed/factorable decomposition of that leakage, or replace the envelope by a different object with a stronger signed matching property.

No estimate for that twisted leakage term is proved here.

## 1. Why the envelope is exactly one on the hard support

Ramaré--Ruzsa construct the enveloping sieve as the square `(3)`. Their bordering sets are multiplicative: for squarefree `d`, membership `n mod d in L_d` means that `n` hits the forbidden local set at every prime divisor of `d`.

If `A_z(n)=1`, no active prime below `z` is bad. Hence no `d>1` can occur in the inner sum of `(3)`. The only remaining term is `d=1`, and the Selberg normalization gives

\[
\Lambda_1=\mu(1)G_1(z)/G_1(z)=1.
\]

This proves `(4)` and `(5)`. This exact-on-survivors property is standard Selberg-envelope prior art; it is not a new sieve theorem.

It changes the live interpretation, however. The phrase "signed approximation error" can suggest that the envelope differs slightly from the hard mask everywhere. It does not. The interior survivor set is matched exactly. The unresolved interface consists entirely of the extra residue classes admitted by the positive majorant.

## 2. One bad prime above `z/2` leaves no room for a second Selberg divisor

Assume `E_r` with `z/2<r<z`. Because all other local constraints are satisfied, the only squarefree `d` for which `n mod d in L_d` are `1` and `r`. Thus

\[
\beta_z(n)=(1+\Lambda_r)^2
=
\left(1-\frac{G_r(z)}{G_1(z)}\right)^2.
\tag{17}
\]

Equation `(7)` is the Ramaré--Ruzsa `G_d` formula. When `d=r>z/2`, a multiple `\ell` of `r` with `\ell\le z` must equal `r`. Since

\[
|\mathcal L_r|=\nu_r,
\qquad
|\mathcal K_r|=r-\nu_r,
\]

substitution into `(7)` proves `(8)` and hence `(9)`.

For a pair sieve, every active prime excludes at least one residue, so its local weight

\[
\frac{\nu_r}{r-\nu_r}
\]

dominates the ordinary dimension-one Selberg local weight `1/(r-1)`. Consequently the corresponding `G_1(z)` dominates, up to deletion of the finite/isolated primes already excluded by the source normalization, the classical sum

\[
\sum_{d\le z}\frac{\mu^2(d)}{\varphi(d)}\gg\log z.
\tag{18}
\]

This is enough for `(10)`; no dimension-two asymptotic or singular-series uniformity in `h` is needed.

## 3. The complete-period lower bound is an adversarial control, not a source-interval theorem

Modulo `W_z`, all local conditions are independent under the Chinese remainder theorem. The survivor density is exactly `\Delta_z`. Requiring the forbidden condition at one specified prime `r` while requiring allowed conditions at every other active prime gives `(12)`.

Summing the nonnegative leakage over the disjoint `E_r` yields `(13)`. The lower bound `(14)` uses only `\nu_r\ge1` and the classical reciprocal-prime mass between `z/2` and `z`; a single omitted conductor prime changes the sum by only `O(1/z)`.

This calculation must not be misread as a lower bound on every actual source interval `I`. The complete sieve period `W_z` is enormous compared with the short source intervals in the staged architecture, and leakage can fluctuate locally. Equation `(15)` is instead a **matched falsification control** for any method that treats `\beta_z-A_z` as intrinsically small merely because `\beta_z` is a good sieve majorant. Globally in the local residue model, the explicit near-cutoff false positives already force only logarithmic relative accuracy.

The stronger pointwise obstruction `(9)`--`(10)` needs no averaging at all: CRT supplies residue classes with exactly one near-cutoff violation, and on those classes the envelope/hard-mask discrepancy is asymptotically order one.

## 4. Prior art and novelty boundary

Olivier Ramaré and Imre Z. Ruzsa, *Additive properties of dense subsets of sifted sequences*, Journal de Théorie des Nombres de Bordeaux 13 (2001), 559--581, DOI `10.5802/jtnb.338`, Section 4.2, equations (4.2.1)--(4.2.4), give the enveloping-sieve square `(3)`, the Selberg weights, the exact `G_d` expression `(7)`, and the majorization of the sifted characteristic function.

Olivier Ramaré, *Notes on restriction theory in the primes*, Section 4, equation (8), states the same basic Selberg construction in the ordinary rough-number case and explicitly notes that the square is nonnegative and takes the value `1` at integers with no prime factors in the sieving range. Tanmoy Bera and G. K. Viswanadham, *Restriction estimates with sifted integers*, arXiv:2512.21640v3 (revised 13 May 2026), Section 3, imports the Ramaré--Ruzsa envelope used in `MC-477`--`MC-478`.

The exact-on-survivors property, Selberg weights, CRT densities, and Mertens reciprocal-prime estimate are classical. A targeted literature audit on 23 September 2026 found no basis for a novelty claim. The durable Mathia contribution is only the **candidate-specific negative accounting**: for the exact translated pair-sieve envelope currently under consideration, a single forbidden prime in the upper half of the cutoff already makes the unsigned exact-to-envelope error order one pointwise and only logarithmically smaller than the survivor mass on the complete local period.

## Boundaries and falsification tests

- **This does not bound the twisted leakage.** The phase `K_h` may cancel strongly on the false-positive set. That is now the live question.
- **Complete-period density is not short-interval density.** Equation `(15)` is an adversarial control against phase-blind small-error arguments, not a lower bound for every source interval.
- **The result concerns the Ramaré--Ruzsa/Bera--Viswanadham Selberg envelope used in `MC-477`--`MC-478`.** A different signed surrogate or a differently truncated/factorable sieve may have a different leakage profile.
- **Near-cutoff primes are essential to the simple exact formula.** For `r<=z/2`, several multiples enter `G_r(z)` and `(8)` no longer holds.
- **The local forbidden set must be nonempty.** In the translated pair sieve it always is; primes dividing `h` reduce `\nu_r` from two to one but do not remove the obstruction.
- **The omitted conductor prime is harmless only for this local-period control.** A construction that deletes a positive-density family of sieve primes would require a fresh reciprocal-prime calculation.
- **No claim is made that the lower bound `(15)` is sharp.** Other false-positive configurations can only increase the nonnegative leakage mean.
- **No Möbius, Mertens, zero-free-region, or RH consequence follows.** This is a structural obstruction inside one candidate source-kernel representation.

## Consequence for the research line

The low-denominator envelope survives as a cheap representation of `\beta_z`, but the simplest route from `\beta_z` back to the exact hard mask is now closed. The missing term in `MC-478` is not a small approximation remainder: it is a genuine positive leakage population containing order-one near-cutoff false positives.

Accordingly, the accepted restriction-style clue should no longer ask whether unsigned envelope accuracy can pay the conductor budget. It cannot in the relevant sense. The next decisive test is narrower: **can the translated-ratio phase `K_h` obtain conductor-sensitive cancellation on the Selberg leakage set itself, or can a signed/factorable replacement preserve the low-denominator gain while suppressing that leakage before coefficient-blind closure?**