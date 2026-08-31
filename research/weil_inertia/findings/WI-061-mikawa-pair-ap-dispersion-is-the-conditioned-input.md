# WI-061 — Mikawa pair-AP dispersion is the missing conditioned input, not yet the cross-conductor splice

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It materially narrows the arithmetic bottleneck isolated by WI-057--WI-060. Hiroshi Mikawa's 1992 theorem is a Bombieri--Vinogradov theorem for the **twin-prime correlation itself inside residue classes**, and its proof exposes a modulus-weighted `L^2` pair-error square function before the final Cauchy--Schwarz step. That is the residue-conditioned pair input that WI-057 showed ordinary MRT does not supply.

The remaining obstruction is more specific. Mikawa controls each conditioning modulus and collectively controls a `q`-weighted square sum over moduli, while the Yang `W`-local main has Fourier mass spread over very many squarefree conductors. The exact-support decomposition from WI-058 converts Mikawa's theorem into a good **per-conductor** bound with only a divisor-type factor `<=6^omega(d)`, provided the residue bookkeeping is done by exact Parseval before any residue maximum. What is still missing is a cross-conductor square-function/martingale assembly that combines those bounds without reverting to the Wiener/triangle-inequality loss ruled out by WI-060, together with the moving-interval and exact local-main splice.

## 1. Exact Mikawa theorem

Mikawa fixes coprime positive integers `q,a` and, for nonzero integer `k`, defines

\[
\Psi(x;q,a,2k)
=
\sum_{\substack{0<m,n\le x\\m-n=2k\\n\equiv a\pmod q}}
\Lambda(m)\Lambda(n).
\tag{1}
\]

When `(a+2k,q)=1`, the expected main term is

\[
H(x;q,2k)
=
\mathfrak S
\prod_{\substack{p\mid qk\\p>2}}
\frac{p-1}{p-2}
\frac{x-|2k|}{\varphi(q)},
\qquad
\mathfrak S
=2\prod_{p>2}\left(1-\frac1{(p-1)^2}\right),
\tag{2}
\]

and he sets

\[
E(x;q,a,2k)
=
\begin{cases}
\Psi(x;q,a,2k)-H(x;q,2k),&(a+2k,q)=1,\\
\Psi(x;q,a,2k),&(a+2k,q)>1.
\end{cases}
\tag{3}
\]

His theorem states that for every `A>0` there is `B=B(A)>0` such that

\[
\boxed{
\sum_{q\le Q}
\max_{(a,q)=1}
\sum_{0<2k\le x}
|E(x;q,a,2k)|
\ll_A x^2(\log x)^{-A}
}
\tag{4}
\]

uniformly for

\[
\boxed{Q\le x^{1/2}(\log x)^{-B}.}
\tag{5}
\]

This is the main theorem of H. Mikawa, *On prime twins in arithmetic progressions*, *Tsukuba J. Math.* 16:2 (1992), 377--387, DOI `10.21099/tkbjm/1496161970`; primary open-access source: https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf . The even-shift notation is not silently identified with the Yang shift family: the exact `p=2`/collision booking remains part of the splice audit below.

## 2. Mikawa's proof contains the required square-function interface

On p. 379, before the final `L^1` theorem is obtained, Mikawa applies Cauchy in the form

\[
\begin{aligned}
&\left(
\sum_{q\le Q}\max_{(a,q)=1}
\sum_{0<2k\le x}|E(x;q,a,2k)|
\right)^2\\
&\qquad\le
\left(
\sum_{q\le Q}\frac1q\sum_{0<2k\le x}1
\right)
\left(
\sum_{q\le Q}q\max_{(a,q)=1}
\sum_{0<2k\le x}|E(x;q,a,2k)|^2
\right).
\end{aligned}
\tag{6}
\]

He bounds the second factor by his dispersion quantity `mathcal D(x;q,a)` and proves, with `mathcal L=log x`, an estimate of the form

\[
x\mathcal L
\sum_{q\le Q}\max_{(a,q)=1}\mathcal D(x;q,a)
\ll_A x^4\mathcal L^{-2A}
\tag{7}
\]

in the range (5). After harmlessly renaming the arbitrary logarithmic exponent, the proof therefore supplies

\[
\boxed{
\sum_{q\le Q}q\max_{(a,q)=1}
\sum_{0<2k\le x}|E(x;q,a,2k)|^2
\ll_A x^3(\log x)^{-A}
}
\tag{8}
\]

for every fixed `A>0` and a corresponding `B(A)`.

Equation (8) is a derived consequence of the nonnegative second factor displayed and controlled in Mikawa's proof, not a new theorem attributed to him. The exact source chain is p. 379, equations (2.3)--(2.5) plus the displayed Cauchy inequality.

## 3. Prior-art redirection relative to WI-057

WI-057 showed an information-theoretic obstruction: ordinary unconditioned MRT pair-correlation control cannot bound a covariance after multiplication by a `W`-local periodic mode. Mikawa supplies the missing stronger interface for the actual von Mangoldt pair: the correlation is conditioned on `n=a mod q`, the main contains the local factors at primes dividing `q`, the theorem is uniform over reduced residues, and the modulus reaches square-root scale.

Thus the durable correction to the prior-art map is

\[
\boxed{
\text{ordinary MRT is insufficient, but a classical conditioned pair theorem already exists.}
}
\tag{9}
\]

This does not contradict WI-042. WI-042 concerns the much stronger four-index global Yang cell square norm after an across-family Cauchy step; Mikawa does not prove that cell theorem. The change is to the repair strategy **before** that global square is taken.

## 4. Exact compatibility with one `W`-local Fourier conductor

WI-058 gives the exact-support Fourier energy of the normalized `W`-local pair main. For an odd squarefree conductor `d` supported on active local primes, write

\[
B_d(h_1)
=
\sum_{\operatorname{cond}(\xi)=d}
|\widehat G_{h_1}(\xi)|^2
=
\prod_{p\mid d}v_p(h_1),
\tag{10}
\]

where

\[
v_p(h_1)=
\begin{cases}
1/(p-1),&p\mid h_1,\\
2/(p-2),&p\nmid h_1.
\end{cases}
\tag{11}
\]

Mikawa's square-function maximum is over reduced residues only, so the Fourier bookkeeping must **not** take a residue maximum pointwise and then sum over shifts. Extend the error to all residues by

\[
\widetilde E_d(a,h)
=
\begin{cases}
E(x;d,a,h),&(a,d)=1,\\
\Psi(x;d,a,h),&(a,d)>1,
\end{cases}
\tag{12}
\]

where the second line is not attributed to Mikawa: it is simply the actual von-Mangoldt pair count with no coprime-residue Hardy--Littlewood main subtracted. Let

\[
\widetilde T_{d,b}(h)
=
\sum_{a\bmod d}\widetilde E_d(a,h)e(ab/d).
\tag{13}
\]

For the exact-conductor contribution

\[
C_d(k)
=
\sum_{\operatorname{cond}(b/d)=d}
\widehat G_{h_1(k)}(b/d)\,\widetilde T_{d,b}(h_2(k)),
\tag{14}
\]

Cauchy followed by **exact Parseval before any residue maximum** gives

\[
\begin{aligned}
|C_d(k)|^2
&\le B_d(h_1(k))
   \sum_{b\bmod d}|\widetilde T_{d,b}(h_2(k))|^2\\
&=B_d(h_1(k))\,d
  \sum_{a\bmod d}|\widetilde E_d(a,h_2(k))|^2.
\end{aligned}
\tag{15}
\]

For every odd active prime,

\[
pv_p(h_1)
\le
\begin{cases}
3/2,&p\mid h_1,\\
6,&p\nmid h_1,
\end{cases}
\tag{16}
\]

so

\[
\boxed{dB_d(h_1)\le6^{\omega(d)}.}
\tag{17}
\]

Assume, as in the booked Yang subfamily, that `k -> h_2(k)` is injective into Mikawa's shift range. Summing (15) before taking any residue maximum yields

\[
\sum_k|C_d(k)|^2
\le 6^{\omega(d)}
\sum_{h_2}\sum_{a\bmod d}|\widetilde E_d(a,h_2)|^2.
\]

Define

\[
M_d:=\max_{(a,d)=1}
\sum_{0<2k\le x}|E(x;d,a,2k)|^2.
\]

The reduced residues compare to Mikawa in the correct order:

\[
\sum_{(a,d)=1}\sum_{h_2}|E(x;d,a,h_2)|^2
\le \varphi(d)M_d\le dM_d.
\]

For the non-reduced classes there is a deterministic prime-power bound. If `Lambda(n) != 0` and `(n,d)>1`, then `n=p^r` for some prime `p|d`. Hence, for each fixed admissible shift `h`, nonnegativity gives

\[
\begin{aligned}
\sum_{(a,d)>1}|\Psi(x;d,a,h)|^2
&\le
\left(\sum_{(a,d)>1}\Psi(x;d,a,h)\right)^2\\
&\le
\left((\log x)\sum_{p\mid d}\sum_{r:p^r\le x}\log p\right)^2\\
&\le \omega(d)^2(\log x)^4.
\end{aligned}
\]

There are at most `x` shifts in the relevant prefix range, so

\[
\sum_{h_2}\sum_{(a,d)>1}|\Psi(x;d,a,h_2)|^2
\le x\,\omega(d)^2(\log x)^4.
\]

Consequently the source-compatible per-conductor estimate is

\[
\boxed{
\sum_k|C_d(k)|^2
\le
6^{\omega(d)}
\left[
 dM_d+x\,\omega(d)^2(\log x)^4
\right].
}
\tag{18}
\]

The first bracketed term is exactly the modulus-weighted square function appearing in (8). The second is a separately booked non-coprime prime-power error, not a new arithmetic hypothesis. It is negligible even after the modulus sum: for every fixed `\varepsilon>0`,

\[
6^{\omega(d)}\omega(d)^2\ll_\varepsilon d^\varepsilon,
\]

and therefore, for `Q<=x^(1/2)(log x)^(-B)`, its total contribution is

\[
\ll_\varepsilon x(\log x)^4Q^{1+\varepsilon}
=o_A\!\left(x^3(\log x)^{-A}\right)
\]

for every fixed `A` after increasing `x`. Thus the physical conductor still cancels against the exact-support Fourier energy: the Mikawa-controlled term pays only the divisor-type factor `6^omega(d)`, while the non-reduced residues are harmless at this scale.

## 5. Why this still does not black-box close WI-060

Equation (18) controls one exact conductor, but the Yang covariance contains the scalar sum

\[
C(k)=\sum_{d\mid W}C_d(k).
\tag{19}
\]

There is no automatic implication

\[
\sum_k\left|\sum_dC_d(k)\right|^2
\ll (\log X)^{O(1)}
\sum_d\sum_k|C_d(k)|^2.
\tag{20}
\]

Generic triangle inequality or Cauchy across conductors reintroduces the conductor-family entropy/Wiener loss diagnosed in WI-060. WI-059 shows that truncating to a fixed polylogarithmic conductor misses positive `W`-local `L^2` mass, while WI-060 shows that the retained family can have super-polylogarithmic `ell^1` complexity.

Therefore Mikawa removes the **single-conductor arithmetic theorem** as the missing ingredient but leaves the Hilbert-space assembly problem

\[
\boxed{
\text{Mikawa pair-AP }L^2
+\text{ orthogonal `W` conductor geometry}
\stackrel{?}{\Longrightarrow}
\text{cross-conductor covariance }o(1).
}
\tag{21}
\]

A plausible positive route is a martingale/Carleson or large-sieve inequality that preserves orthogonality of exact-support local components before the scalar conductor sum is formed. A decisive negative route would show that any such assembly necessarily incurs a loss too large for Mikawa's arbitrary fixed logarithmic savings. The factor `6^omega(d)` is not by itself the main obstruction: after truncating `omega(d)` at `C log log X`, it is only a fixed power of `log X`, while the far spectral tail can be treated by the Bernoulli/Chernoff bookkeeping already isolated in WI-058--WI-060. This observation is a program guide, not a completed proof of (20).

## 6. Three load-bearing splice gates remain

Even a solution of (20) would not yet certify the Yang one-sided fourth moment.

**Local-main normalization.** Mikawa's reduced-residue error subtracts the Hardy--Littlewood pair main (2), while the Yang welding decomposition uses the exact `W`-local pair main and WI-049's full four-form local factorization. One must prove that the **reduced-residue** main splices to that deterministic local main with only already-booked `o(1)` terms, including primes dividing the conditioning conductor or either shift and the `p=2` parity factor. The non-reduced classes are no longer silently absorbed into this identification: they are the explicit prime-power error in (18), whose negligibility must remain valid after the final source normalization.

**Translated and moving intervals.** Mikawa states a prefix theorem with both primes `<=x`. A single translated pair interval can be written as a difference of prefix pair counts after intersecting the shifted physical intervals, but the Yang endpoints move with the cell and shift. A maximal-over-endpoints version, a dyadic interval decomposition with a proved boundary budget, or a direct short-interval pair-AP theorem is still needed. Maurizio Laporta's *A short intervals result for 2n-twin primes in arithmetic progressions* is nearby prior art, but its exact theorem surface is not consumed here without a separate reconstruction.

**Two-leg locked geometry.** Mikawa conditions one prime pair modulo one auxiliary modulus. The Yang covariance locks two pair shifts through the same `k` and then averages over two prime-power bases. Equation (18) can be restricted to an injective booked shift subfamily, but the second base, Mertens weights, source Jacobians, collisions, boundary strip, and the non-reduced booking must still be propagated with the exact normalization of WI-033/WI-046--WI-050.

## 7. Adjacent multiplet prior art does not remove those gates

Koichi Kawada, *The prime k-tuplets in arithmetic progressions*, *Tsukuba J. Math.* 17 (1993), 43--57, proves an averaged arithmetic-progression asymptotic for fixed linear coefficients in a short physical interval, with a modulus range of the shape

\[
Q\le yx^{-1/2}(\log x)^{-B}
\tag{22}
\]

under his stated lower bound on `y`. This confirms that prime-multiplet AP dispersion is classical prior art, but it is not a black-box solution for the live four-form system: Yang's reduced coefficients themselves range through power-sized prime bases, whereas Kawada fixes the linear coefficients. No growing-coefficient conclusion is imported from that theorem.

## 8. Consequence for the live research priority

The chain WI-057--WI-060 reduced the source problem to residue-conditioned pair control, cross-mode cancellation, or a direct localized covariance estimate. Mikawa eliminates the first item as an invention task. The shortest credible chain is now

\[
\boxed{
\begin{array}{c}
\text{exact `W`-local support decomposition (WI-058)}\\
\downarrow\\
\text{Mikawa residue-conditioned pair dispersion, conductor by conductor}\\
\downarrow\\
\textbf{cross-conductor square-function / martingale assembly}\\
\downarrow\\
\text{moving-interval + exact local-main splice}\\
\downarrow\\
\text{locked two-leg Mertens aggregation}.
\end{array}}
\tag{23}
\]

The bold arrow is the highest-value unresolved mathematical target. Re-running ordinary MRT, first-order BDH, or mode-by-mode fixed-log estimates repeats routes already closed by WI-057/WI-060.

## 9. Prior-art / novelty audit

Primary and authoritative anchors:

- H. Mikawa, **On prime twins in arithmetic progressions**, *Tsukuba Journal of Mathematics* 16:2 (1992), 377--387, DOI `10.21099/tkbjm/1496161970`; primary source https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf . Load-bearing for (1)--(8), especially p. 379 for the modulus-weighted square factor.
- zbMATH review of Mikawa, https://portal.mardi4nfdi.de/wiki/Item%3AQ2367079 . Independent bibliographic confirmation of the theorem and square-root modulus range.
- Koichi Kawada, **The prime k-tuplets in arithmetic progressions**, *Tsukuba Journal of Mathematics* 17:1 (1993), 43--57; primary source https://tsukuba.repo.nii.ac.jp/record/15690/files/3.pdf . Adjacent multiplet-AP prior art, not consumed as a growing-coefficient theorem.
- Natalie Evans, **Correlations of almost primes**, *Math. Proc. Cambridge Philos. Soc.* 174 (2023), 301--344, DOI `10.1017/S0305004122000251`. Context for Mikawa in the average prime-correlation literature.
- Maurizio Laporta, **A short intervals result for 2n-twin primes in arithmetic progressions**, *Tsukuba Journal of Mathematics* 23 (1999), 201--214. Closest short-interval follow-up identified here; exact hypotheses are not used as evidence until separately audited.

No novelty is claimed for Mikawa's theorem, Linnik dispersion, Cauchy--Schwarz, Parseval, or prime-tuple AP distribution. The line-specific deduction is the source-compatible alignment (10)--(18) with WI-058's conductor energy, including the explicit reduced/non-reduced residue split, and the resulting identification of **cross-conductor assembly**, rather than absence of a conditioned pair theorem, as the remaining spectral obstruction. No priority claim is made from failure to locate this exact Yang/`W`-local splice in the cited literature.

## 10. Decisive promotion / falsification tests

Promote this route toward a theorem only after all of the following are proved with the source normalization.

1. **Main-term identity:** identify Mikawa's reduced-residue Hardy--Littlewood main with the exact `W`-local/full four-form main used after WI-049, including `p=2`, conductor/shift local factors and collisions; separately verify that the non-reduced prime-power booking of (18) remains negligible after this normalization.
2. **Maximal interval transfer:** prove a pair-AP analogue adequate for all moving Yang physical intervals with no power loss that destroys (8), either from Mikawa's proof, Laporta/related short-interval prior art, or a fresh dyadic maximalization.
3. **Cross-conductor square function:** prove an inequality of the form (20) with at most a fixed logarithmic loss, or an equivalent martingale/large-sieve estimate combining exact-support conductor pieces before triangle inequality.
4. **Locked-shift bookkeeping:** show that restricting Mikawa's shift square sum to the Yang booked shift family and integrating the two base Mertens weights preserves an `o(1)` normalized remainder over the full source support after the already-separated boundary strip.
5. **End-to-end remainder gate:** insert the resulting welding bound into the certified deterministic core and compare with the `R(1)<0.0380702829...` threshold from WI-028 before making any new simple-zero claim.

Narrow or withdraw the redirection if Mikawa's displayed square-function factor cannot be made uniform for the translated residue-class errors needed by Yang, or if the cross-conductor family necessarily forces the same super-polylogarithmic Wiener loss as WI-060. Either outcome would be substantive: the first closes this prior-art splice, while the second establishes a sharper barrier for the entire `W`-local square-function route.
