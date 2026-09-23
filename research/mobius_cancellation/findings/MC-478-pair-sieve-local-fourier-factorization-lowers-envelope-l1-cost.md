# MC-478 — Pair-sieve local Fourier factorization lowers envelope ℓ¹ cost

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-477` bounded the low-denominator enveloping-sieve coefficient mass by discarding the pair-sieve local Fourier structure and using only Bera--Viswanadham's final generic pointwise estimate

\[
|w(a/q)|\ll \frac{1}{G(z)\sqrt q}.
\]

That loses one full power of the sieve cutoff under absolute recombination. In the translated pair sieve, the stronger intermediate estimate in the proof of their Lemma 3.2 combines with exact Chinese-remainder factorization of the local forbidden-residue Fourier transform to give

\[
\boxed{
\sum_{\substack{q\le z^2\\q\mid P(2,z)}}
\sum_{a\bmod q}^{*}|w(a/q)|
\ll
\frac{z^2(\log(2z))^5}{G(z)}.
}
\tag{1}
\]

Here the implied constant is uniform in the surviving pair-sieve shift `h`. Consequently, in the prime-conductor source frame of `MC-477`, where

\[
S_{q,a}(I)=\sum_{n\in I}K_h(n)e(an/q),
\qquad
|S_{q,a}(I)|\ll \sqrt p\log(2p),
\]

one obtains the sharper envelope estimate

\[
\boxed{
\left|\sum_{n\in I}K_h(n)\beta(n)\right|
\ll
\frac{z^2(\log(2z))^5}{G(z)}
\sqrt p\log(2p).
}
\tag{2}
\]

Thus the simplest coefficientwise conductor-sensitive route requires, up to logarithms,

\[
z^2\sqrt p\ll H
\tag{3}
\]

rather than the `z^3\sqrt p\ll H` condition obtained in `MC-477` by summing the generic `q^{-1/2}` coefficient bound over all reduced rational frequencies.

The gain is entirely representation-specific. It comes from summing the **actual pair-sieve local Fourier factors before replacing them by the generic `q^{-1/2}` envelope**. It is not a cancellation theorem for the exact rough×rough indicator, and it does not settle the signed replacement error between that indicator and the enveloping weight.

## 1. Use the intermediate coefficient bound rather than its generic corollary

Bera--Viswanadham's Lemma 3.1 writes the enveloping-sieve coefficient at a reduced rational frequency `a/q` in terms of the normalized Fourier transform of the allowed residue set `K_q`. In the proof of Lemma 3.2 they first obtain, for squarefree `q` supported on the sieve primes,

\[
|w(a/q)|
\ll
\frac{3^{\omega(q)}}{G(z)}
\left|
\frac1{|K_q|}\sum_{b\in K_q} e(ab/q)
\right|,
\tag{4}
\]

before replacing the normalized local Fourier factor by a generic pointwise upper bound that yields the published `q^{-1/2}` estimate.

For the translated pair sieve, the forbidden residues modulo a sieve prime `r` are

\[
\mathcal L_r(h)=\{0,-h\}\pmod r.
\tag{5}
\]

If `r\nmid h`, the two residues are distinct and `|K_r|=r-2`; if `r\mid h`, they coincide and `|K_r|=r-1`. Once the parity-degenerate odd shifts are removed as in `MC-472`, the `r=2` factor is always of the second type.

Because `q` is squarefree, the Chinese remainder theorem gives

\[
K_q\cong\prod_{r\mid q}K_r.
\]

For a reduced `a (mod q)`, the additive character also factors into nonzero local frequencies `a_r (mod r)`. Therefore

\[
\left|
\frac1{|K_q|}\sum_{b\in K_q} e(ab/q)
\right|
=
\prod_{r\mid q} A_r(a_r;h),
\tag{6}
\]

where

\[
A_r(c;h)=
\begin{cases}
\displaystyle
\frac{|1+e(-ch/r)|}{r-2},& r\nmid h,\\[1.1ex]
\displaystyle
\frac1{r-1},& r\mid h.
\end{cases}
\tag{7}
\]

Indeed, at nonzero local frequency the complete sum over `Z/rZ` vanishes, so the sum over the allowed set is minus the contribution of the one or two excluded residues.

## 2. The reduced-frequency ℓ¹ mass factorizes and each local factor is at most two

Summing `(6)` over reduced residues modulo `q` factorizes exactly:

\[
\sum_{a\bmod q}^{*}
\left|
\frac1{|K_q|}\sum_{b\in K_q} e(ab/q)
\right|
=
\prod_{r\mid q} L_r(h),
\tag{8}
\]

with

\[
L_r(h)=
\begin{cases}
1,&r\mid h,\\[0.8ex]
\displaystyle
\frac{1}{r-2}
\sum_{c=1}^{r-1}|1+e(c/r)|,&r\nmid h.
\end{cases}
\tag{9}
\]

For an odd prime `r` in the second case,

\[
\sum_{c=1}^{r-1}|1+e(c/r)|
=2\left(\csc\frac{\pi}{2r}-1\right),
\tag{10}
\]

hence

\[
L_r(h)
=
\frac{2\left(\csc(\pi/(2r))-1\right)}{r-2}
\le 2.
\tag{11}
\]

A short elementary proof of the last inequality is enough. Since `\pi/(2r)\le\pi/6` for `r\ge3`, concavity of sine on `[0,\pi/6]` gives

\[
\sin\frac{\pi}{2r}\ge\frac{3}{2r}\ge\frac1{r-1}.
\]

Thus `\csc(\pi/(2r))\le r-1`, which is exactly `(11)`. In the first case of `(9)` the local mass is identically one. The surviving `r=2` factor also has mass one.

Combining `(4)`, `(8)` and `(11)` therefore gives the fixed-denominator aggregate bound

\[
\boxed{
\sum_{a\bmod q}^{*}|w(a/q)|
\ll
\frac{6^{\omega(q)}}{G(z)}.
}
\tag{12}
\]

This is qualitatively different from summing the generic pointwise bound `G(z)^{-1}q^{-1/2}` over `\varphi(q)` frequencies. The local pair-sieve transform pays only a bounded factor per prime after the reduced frequencies are aggregated.

## 3. Summing denominators costs `z²` times polylogarithms

Put `Q=z^2`. Since the admissible denominators in the enveloping sieve are squarefree,

\[
6^{\omega(q)}=\tau_6(q),
\]

where `\tau_6` is the ordered six-fold divisor function. Hence

\[
\sum_{\substack{q\le Q\\q\mid P(2,z)}}6^{\omega(q)}
\le
\sum_{q\le Q}\tau_6(q)
\ll Q(\log(2Q))^5.
\tag{13}
\]

The last bound is elementary: `\sum_{n\le Q}\tau_6(n)` counts ordered products `d_1\cdots d_6\le Q`; summing first over `d_6` gives at most

\[
Q\left(\sum_{d\le Q}\frac1d\right)^5
\ll Q(\log(2Q))^5.
\]

Substituting `Q=z^2` into `(12)` proves `(1)`. Combining `(1)` with the denominator-independent completion estimate from `MC-477` proves `(2)`.

Relative to the natural enveloping-sieve mass scale `H/G(z)`, the right side of `(2)` is strictly smaller whenever

\[
z^2(\log(2z))^5\sqrt p\log(2p)=o(H),
\tag{14}
\]

which yields the coarse window `(3)` after suppressing logarithms.

## 4. What this improves, and what it does not

The `z^3/G(z)` coefficient mass in `MC-477` was explicitly labeled a crude upper bound rather than a barrier. Equation `(1)` demonstrates that it is indeed not the right pair-sieve aggregate scale: using the same enveloping representation and the same termwise character estimate, but retaining the exact local Fourier product one step longer, saves a full power of `z` up to logarithms.

This does **not** show that `z^2(\log z)^5/G(z)` is sharp. The factor `3^{\omega(q)}` in `(4)` came from the general enveloping-sieve coefficient argument, and the coefficients may have further signed or arithmetic structure that an absolute-value estimate still discards. Equation `(1)` is therefore an improved constructive upper bound, not a lower bound on every possible recombination.

More importantly, the original base component remains

\[
\sum_{n\in I}K_h(n)A_{W,h}(n),
\qquad
A_{W,h}(n)=\mathbf1_{(n(n+h),W)=1},
\]

not the enveloping-weight sum in `(2)`. Pointwise majorization `A\le\beta` still does not control a complex signed sum. No argument above bounds

\[
\sum_{n\in I}K_h(n)(A_{W,h}(n)-\beta(n)).
\tag{15}
\]

Thus the remaining decisive restriction-style question is more concentrated than after `MC-477`: **can the exact-to-envelope signed replacement be controlled below the conductor-saving budget, or can the envelope enter a positive quadratic form that retains the `K_h` gain?** Further coefficient cancellation is useful but is no longer the only unresolved half of the low-denominator route.

## Prior art and novelty boundary

Tanmoy Bera and G. K. Viswanadham, *Restriction estimates with sifted integers*, arXiv:2512.21640v3 (revised 13 May 2026), Lemmas 3.1--3.2, provide the enveloping-sieve coefficient formula and the intermediate estimate `(4)`. Their construction is based on the Ramaré--Ruzsa enveloping sieve from Olivier Ramaré and Imre Z. Ruzsa, *Additive properties of dense subsets of sifted sequences*, Journal de Théorie des Nombres de Bordeaux 13 (2001), 559--581.

The Chinese-remainder factorization, the explicit Fourier transform of the complement of one or two residue classes, and the divisor-function mean bound used above are elementary/classical. A targeted audit found no basis for a novelty claim for any of those ingredients. The durable line-specific advance is the accounting statement: **for the exact translated pair-sieve local model, the intermediate enveloping-sieve Fourier formula has aggregate absolute mass at most `z^2 polylog(z)/G(z)`, rather than the `z^3/G(z)` obtained by first collapsing to the generic `q^{-1/2}` pointwise estimate.**

No new restriction theorem, character-sum theorem, or sieve majorant is claimed.

## Boundaries and falsification tests

- **Reduced local frequencies are essential.** The factorization `(8)` uses `(a,q)=1`, so every local frequency is nonzero. That is exactly the frequency set in the enveloping expansion used by Bera--Viswanadham.
- **Squarefree denominators are essential to the simple product.** They are built into the relevant `q\mid P(2,z)` support. A different enveloping representation with prime powers requires a separate local calculation.
- **Parity degeneration remains isolated.** Once `2|W`, odd `h` has no rough×rough survivors. The surviving even-shift local factor at `2` has mass one.
- **The bound is uniform in prime divisors of `h`.** Such primes only reduce the local mass from at most two to exactly one.
- **The logarithmic exponent is not asserted sharp.** It comes from the coarse domination by `\tau_6`; retaining the actual local constants can improve logarithmic factors but is not needed for the present power-of-`z` separation.
- **The result is still an ℓ¹ recombination.** It preserves the conductor-sensitive mode estimate but takes absolute values across the low-denominator family. Structured cancellation among `w(a/q)` may improve it further.
- **No signed replacement theorem is proved.** Equation `(15)` remains uncontrolled.
- **No Möbius, Mertens, zero-free-region, or RH consequence follows.** This is a sharper estimate inside one staged sieve component.

## Consequence for the research line

The low-denominator restriction-style route survives another test and becomes quantitatively cheaper. `MC-477` showed that each rational frequency couples to the translated-ratio character phase for `O(\sqrt p\log p)` independently of its denominator. The present result shows that the pair-sieve local Fourier geometry can aggregate those frequencies for only `z^2` times polylogarithms, rather than the previous crude `z^3` cost.

Accordingly, the main rough×rough bottleneck is no longer the mere cardinality of the low-denominator frequency family. The sharp unresolved interface is the signed passage from the exact pair-sieve indicator to the enveloping representation, together with any remaining source-budget constraints after `(14)` is inserted into the full staged architecture. If that replacement can be controlled without losing the conductor gain, the route has genuinely escaped the full-primorial obstructions of `MC-473`--`MC-475`; if not, the representation remains analytically compressed but unusable for the exact base component.