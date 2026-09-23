# MC-481 — Centered Selberg leakage is target-equivalent modulo the envelope

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `CLASSICAL-IDENTITY` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The centered incomplete Selberg-leakage discrepancy isolated in `MC-480` is not an independent exact-to-envelope transfer problem. After the same complete-period mean is removed from every periodic weight, linearity gives an exact identity in which the leakage discrepancy is simply the difference between the already-controlled envelope discrepancy and the original exact hard-mask discrepancy.

Keep the prime-conductor pair-sieve setup of `MC-477`--`MC-480`. Let

\[
K_h(n)=\chi(n+h)\overline{\chi(n)},
\qquad h\not\equiv0\pmod p,
\]

let `W` be square-free with `(W,p)=1`, and let

\[
A=A_{W,h},\qquad \beta=\beta_{W,h},\qquad L=\beta-A
\]

be respectively the exact pair-sieve mask, the current Ramaré--Ruzsa/Bera--Viswanadham Selberg envelope, and its false-positive leakage. For any `W`-periodic weight `F`, define

\[
\overline F:=\frac1W\sum_{b\bmod W}F(b)
\]

and the naturally centered translated-character discrepancy on an interval `I` by

\[
\mathcal D_F(I)
:=
\sum_{n\in I}K_h(n)F(n)
+\frac{|I|}{p}\overline F.
\tag{1}
\]

The centering in `(1)` is canonical for this source frame: the CRT calculation of `MC-480` applies to every `W`-periodic `F` and gives

\[
\frac1{pW}\sum_{n\bmod pW}K_h(n)F(n)
=-\frac{\overline F}{p}.
\tag{2}
\]

Because `L=\beta-A` and both the interval sum and local mean are linear,

\[
\boxed{
\mathcal D_L(I)=\mathcal D_\beta(I)-\mathcal D_A(I).
}
\tag{3}
\]

The quantity called `\mathcal E_{W,h}(I)` in `MC-480` is exactly `\mathcal D_L(I)`. Hence

\[
\boxed{
\mathcal D_A(I)=\mathcal D_\beta(I)-\mathcal E_{W,h}(I).
}
\tag{4}
\]

The envelope term is already cheap in the regime opened by `MC-477`--`MC-478`. For `|I|=H\le p`, `MC-478` gives

\[
\left|\sum_{n\in I}K_h(n)\beta(n)\right|
\ll
\frac{z^2(\log(2z))^5}{G(z)}\sqrt p\log(2p).
\tag{5}
\]

Moreover the zero Fourier mode of the Bera--Viswanadham enveloping expansion is the complete `W`-period mean `\overline\beta`. Their Lemma 3.2, specialized to the current `z_0=2` pair sieve, gives

\[
\overline\beta=w(1)\ll \frac1{G(z)}.
\tag{6}
\]

Combining `(1)`, `(5)` and `(6)` yields

\[
\boxed{
|\mathcal D_\beta(I)|
\ll
\frac{z^2(\log(2z))^5}{G(z)}\sqrt p\log(2p)
+
\frac{H}{pG(z)}.
}
\tag{7}
\]

Therefore any estimate

\[
|\mathcal E_{W,h}(I)|\le B_L
\]

immediately gives

\[
|\mathcal D_A(I)|\le B_\beta+B_L,
\tag{8}
\]

where `B_beta` is the right side of `(7)`. Conversely, any estimate

\[
|\mathcal D_A(I)|\le B_A
\]

gives, by `(3)`,

\[
|\mathcal E_{W,h}(I)|\le B_\beta+B_A.
\tag{9}
\]

Thus once `(7)` is below the desired source budget, a conductor-power estimate for the centered leakage is quantitatively equivalent, up to an already-controlled comparison term, to the conductor-power estimate for the original exact rough×rough discrepancy. Centering removes the forced complete-period mean, but it does **not** turn the Selberg replacement error into a mathematically easier target by itself.

This closes one interpretation of the accepted low-denominator clue: proving smallness of the centered positive leakage as a separate transfer lemma cannot be credited as an independent bridge from the envelope back to the hard mask. A useful continuation must expose additional structure -- for example a signed/factorable exact decomposition, first-exit identity, or cross-component cancellation -- whose proof does more than re-express `\mathcal D_A` through `(3)`.

## 1. The complete-period centering is linear for every sieve-coordinate weight

`MC-480` derived `(2)` for the leakage by observing that `K_h` depends only on the residue modulo `p`, while the leakage depends only on the residue modulo `W`. Nothing in that tensor-product calculation uses positivity or the special formula for `L`.

For every `W`-periodic `F`, CRT gives

\[
\sum_{n\bmod pW}K_h(n)F(n)
=
\left(\sum_{a\bmod p}K_h(a)\right)
\left(\sum_{b\bmod W}F(b)\right).
\]

The classical complete translated-character correlation is `-1` for nonzero shift, so `(2)` follows. In particular the same centering applies simultaneously to `A`, `\beta`, and `L`.

Consequently there is no centering mismatch that could create a new independent error term. Since

\[
\overline L=\overline\beta-\overline A,
\]

substitution into `(1)` proves `(3)` identically.

## 2. The low-denominator envelope discrepancy already has the conductor-sensitive estimate

`MC-478` retained the exact local pair-sieve Fourier factorization long enough to show that the aggregate absolute coefficient mass of the enveloping representation is at most

\[
\ll \frac{z^2(\log(2z))^5}{G(z)}.
\]

Each rational mode couples to `K_h` for `O(\sqrt p\log p)` independently of its denominator, which is `(5)`.

It remains only to price the deterministic mean added by the canonical centering. The enveloping expansion is periodic with period dividing the active-prime product `W`; therefore its average over `W` is precisely its zero rational Fourier coefficient. Bera--Viswanadham's Lemma 3.2 bounds that coefficient by `O(G(z)^{-1})` when `z_0=2`. This proves `(6)` and hence `(7)`.

The second term `H/(pG(z))` is not a new conductor obstruction in the intended source range `H\le p`: it is at most the natural sifted mass scale `H/G(z)` by the additional factor `1/p`. Whether `(7)` is sufficiently small in the full staged architecture still depends on the source parameters already tracked by `MC-478`; no stronger admissible range is asserted here.

## 3. Why the centered leakage is not a separate transfer resource

The exact identity `(3)` has a two-sided consequence. Suppose a proposed argument controls `\mathcal E=\mathcal D_L` at a scale that is genuinely smaller than the target rough×rough mass. Then `(4)` immediately controls `\mathcal D_A`, because `\mathcal D_\beta` is already priced by `(7)`. The proposed leakage theorem has therefore solved the original exact discrepancy up to a known cheap term.

Conversely, if one somehow controls the exact discrepancy first, `(3)` controls the centered leakage at the same scale, again up to `(7)`. There is no one-way approximation principle here analogous to an unsigned majorant inequality. The two centered quantities differ by the controlled envelope term.

This is stronger than the negative result of `MC-479`, which said that `\beta-A` is not small in unsigned mass, and different from `MC-480`, which said that complete-period character oscillation does not cancel that mass. Those findings left open the possibility that subtracting the complete mean might expose an easier incomplete leakage discrepancy. Equation `(3)` shows that **centering alone cannot create such an independent simplification**.

The statement does not prove that every method for estimating `\mathcal E` must be hard. It says that any successful estimate is already, mathematically, a solution of the exact base-channel discrepancy once `(7)` is inserted. If the proof of `\mathcal E` uses a new signed decomposition or structural theorem, that new theorem may still be the desired mechanism; its value comes from that extra structure, not from interpreting `L` as a small replacement error.

## 4. Prior art and novelty boundary

The Ramaré--Ruzsa enveloping sieve and its rational Fourier representation are classical prior art. Bera and Viswanadham, *Restriction estimates with sifted integers*, arXiv `2512.21640v3` (revised 13 May 2026), Section 3 and Lemma 3.2, provide the low-denominator expansion and the coefficient estimate used for `(6)`; the same source explicitly attributes the construction to Ramaré--Ruzsa. `MC-477`--`MC-479` already audited this literature in the present pair-sieve specialization.

Green and Tao's *Restriction theory of the Selberg sieve, with applications* (J. Théorie des Nombres de Bordeaux 18 (2006), 147--182) is broader prior art for using Selberg majorants to control arithmetic exponential sums. No theorem from that paper supplies the present translated-ratio character estimate, and no novelty claim is made here.

The complete character correlation, CRT tensorization, Fourier zero-mode interpretation, and linear identity `(3)` are elementary/classical. A targeted literature check found no basis for a novelty claim. The durable contribution is only the candidate-specific accounting consequence: after `MC-478` has made the envelope discrepancy cheap, the newly isolated centered leakage discrepancy of `MC-480` is algebraically target-equivalent to the original exact hard-mask discrepancy rather than an independent exact-to-envelope approximation step.

## Boundaries and falsification tests

- **The identity `(3)` is exact; the cheapness of `\mathcal D_\beta` is conditional on the existing `MC-478` source frame.** A different conductor, interval regime, or envelope must re-price its own comparison term.
- **`h\not\equiv0\pmod p` and `(W,p)=1` remain essential** for the canonical centering `(2)` used by this branch.
- **`H\le p` is used in the `MC-478` interval completion estimate.** Longer intervals require separating complete conductor blocks before applying `(7)`.
- **No lower bound for `\mathcal E` or `\mathcal D_A` is proved.** Target-equivalence is an accounting identity, not a hardness theorem.
- **Signed/factorable replacements are not ruled out.** A replacement that exposes a new exact structure can still be useful, but its success must be credited to that structure rather than to small centered leakage.
- **Boundary, nonempty-component and cross-component channels remain separate.** Equation `(3)` concerns the current empty-vector hard-mask/envelope pair.
- **No Möbius, Mertens, zero-free-region, or RH consequence follows.** This closes one proof architecture inside the staged source-kernel route.

## Consequence for the research line

The accepted restriction-style clue should no longer treat a conductor-power bound for the centered Selberg leakage as a cheaper transfer subproblem. In the regime where the low-denominator envelope is already controlled, such a bound is the original exact rough×rough discrepancy modulo the known envelope term.

The surviving ways forward are therefore narrower: derive a genuinely signed/factorable exact surrogate whose new structure yields the needed cancellation; exploit first-exit/nonempty-component information not present in the base positive leakage; or retain cross-component interference before positive closure. Merely centering the current false-positive leakage and trying to prove it small is now closed as an independent mechanism.