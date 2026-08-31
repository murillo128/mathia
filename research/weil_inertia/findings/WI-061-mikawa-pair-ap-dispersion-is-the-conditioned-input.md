# WI-061 — Mikawa pair-AP dispersion is the missing conditioned input, not yet the cross-conductor splice

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It materially narrows the arithmetic bottleneck isolated by WI-057--WI-060. A targeted primary-source audit found that Hiroshi Mikawa's 1992 theorem is not merely ordinary prime distribution in arithmetic progressions: it is a Bombieri--Vinogradov theorem for the **twin-prime correlation itself inside residue classes**, and its proof exposes a modulus-weighted `L^2` pair-error square function before the final Cauchy--Schwarz step. That is exactly the type of residue-conditioned pair input that WI-057 said ordinary MRT does not supply.

The remaining obstruction is now more specific. Mikawa controls each conditioning modulus, and collectively controls a `q`-weighted square sum over moduli, but the Yang `W`-local main has Fourier mass spread over very many squarefree conductors. The exact-support decomposition from WI-058 converts Mikawa's theorem into a good **per-conductor** bound with only a divisor-type factor `<=6^omega(d)`. What is still missing is a cross-conductor square-function/martingale assembly that combines those bounds without reverting to the Wiener/triangle-inequality loss ruled out by WI-060, together with the moving-interval and exact local-main splice. Thus the live task is no longer "invent a residue-conditioned prime-pair theorem"; it is "splice an existing conditioned pair-dispersion theorem through the `W`-local conductor geometry without losing orthogonality."

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

This is the main theorem of H. Mikawa, *On prime twins in arithmetic progressions*, Tsukuba J. Math. 16:2 (1992), 377--387, DOI `10.21099/tkbjm/1496161970`. Primary open-access source: https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf . The zbMATH review independently states the same `Q=x^(1/2) log^{-B(A)} x` extension of the Maier--Pomerance mean-value theorem: https://portal.mardi4nfdi.de/wiki/Item%3AQ2367079 .

The even-shift notation is not silently identified with the Yang shift family here. For prime-pair correlations, odd shifts are locally killed apart from the prime `2`; the exact `p=2`/collision booking in the Yang source remains part of the splice audit below.

## 2. The proof contains the square-function interface, not only the final `L^1` theorem

The important point for WI-060 is on p. 379 of Mikawa's paper. Before the final theorem is obtained, Mikawa applies Cauchy in the form

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

He then bounds the second factor by the dispersion quantity `mathcal D(x;q,a)` built from the `W,V,U` terms of §§2--5, and proves

\[
x\mathcal L
\sum_{q\le Q}\max_{(a,q)=1}\mathcal D(x;q,a)
\ll_A x^4\mathcal L^{-2A},
\qquad \mathcal L=\log x,
\tag{7}
\]

in the range (5). Consequently, after the harmless renaming of the arbitrary logarithmic exponent, the proof supplies the derived square-function consequence

\[
\boxed{
\sum_{q\le Q}q\max_{(a,q)=1}
\sum_{0<2k\le x}|E(x;q,a,2k)|^2
\ll_A x^3(\log x)^{-A}
}
\tag{8}
\]

for every fixed `A>0` and a corresponding `B(A)`.

Equation (8) is not a new theorem claim: it is the nonnegative second factor displayed explicitly in Mikawa's proof and dominated there by his admissible dispersion quantity. The exact source chain is p. 379, equations (2.3)--(2.5) plus the displayed Cauchy inequality. This is precisely why the paper is more relevant to WI-060 than a citation to the final `L^1` statement alone would suggest.

## 3. This directly changes the interpretation of WI-057

WI-057 proved an information-theoretic obstruction: ordinary unconditioned MRT pair-correlation control cannot bound a covariance after multiplication by a `W`-local periodic mode. A periodic quotient component can be invisible to the unconditioned pair sum while remaining leading after local conditioning. The finding therefore demanded one of three genuinely stronger interfaces, the first being a **residue-conditioned/twisted pair theorem**.

Mikawa supplies exactly such an interface for the actual von Mangoldt pair. The correlation in (1) is conditioned on `n=a mod q`, its main term contains the local factors at primes dividing `q`, the theorem is uniform in the residue through `max_a`, and the modulus reaches square-root scale. In particular, the modulus range itself is not the obstacle for the effective `W`-local conductors isolated by WI-058--WI-060: every subpolynomial conductor `d=X^{o(1)}` is eventually far below `x^(1/2) log^{-B}x` on any fixed positive-power physical scale.

Thus the durable correction to the prior-art map is

\[
\boxed{
\text{ordinary MRT is insufficient, but a classical conditioned pair theorem already exists.}
}
\tag{9}
\]

This does not contradict WI-042. WI-042 asked for the much stronger **four-index global Yang cell square norm** after the public `g1_ledger.py` has already performed across-family Cauchy. Mikawa does not prove that cell theorem. What changes is the repair strategy before that forbidden global square is taken.

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

Let `E_d(a,h_2)` denote the Mikawa residue-class pair error for the second prime pair, after the exact main-term identification required in §6 below, and let

\[
T_{d,b}(h_2)
=
\sum_{a\bmod d}E_d(a,h_2)e(ab/d).
\tag{12}
\]

Parseval gives

\[
\sum_{b\bmod d}|T_{d,b}(h_2)|^2
=d\sum_{a\bmod d}|E_d(a,h_2)|^2
\le d^2\max_a|E_d(a,h_2)|^2.
\tag{13}
\]

For the exact-conductor contribution

\[
C_d(k)
=
\sum_{\operatorname{cond}(b/d)=d}
\widehat G_{h_1(k)}(b/d)\,T_{d,b}(h_2(k)),
\tag{14}
\]

Cauchy and (10)--(13) give pointwise

\[
|C_d(k)|^2
\le
B_d(h_1(k))d^2
\max_a|E_d(a,h_2(k))|^2.
\tag{15}
\]

The local factor multiplying Mikawa's natural `d * error^2` weight is only divisor-like. Indeed, for every odd active prime,

\[
pv_p(h_1)
\le
\begin{cases}
3/2,&p\mid h_1,\\
6,&p\nmid h_1,
\end{cases}
\tag{16}
\]

because `2p/(p-2)<=6` for `p>=3`. Hence

\[
\boxed{dB_d(h_1)\le6^{\omega(d)}.}
\tag{17}
\]

If the Yang structured map `k -> h_2(k)` is injective on a booked subfamily, restricting Mikawa's nonnegative shift square sum to that subfamily yields

\[
\boxed{
\sum_k|C_d(k)|^2
\le
6^{\omega(d)}
\left[
 d\max_a\sum_{h_2}|E_d(a,h_2)|^2
\right].
}
\tag{18}
\]

The bracket is exactly the modulus-weighted quantity controlled collectively by (8). Thus the feared physical conductor `d` itself cancels against the `1/d` scale of the exact-support local Fourier energy; the per-conductor price is `6^omega(d)`, not `d`.

This is a line-specific exact deduction from Mikawa plus WI-058. It is also the main reason this prior art materially redirects the program.

## 5. Why this still does not black-box close WI-060

Equation (18) controls one exact conductor, and summing its **squares** over conductors can use Mikawa's modulus sum after a suitable `omega(d)` truncation. The Yang covariance, however, contains the scalar sum

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

Applying triangle inequality or generic Cauchy across conductors reintroduces the huge conductor-family entropy/Wiener loss diagnosed in WI-060. This is not cosmetic: WI-059 shows that truncating to a fixed polylogarithmic conductor misses positive `W`-local `L^2` mass, while WI-060 shows that the retained family can have super-polylogarithmic `ell^1` complexity.

Therefore Mikawa removes the **single-conductor arithmetic theorem** as the missing ingredient but leaves the exact Hilbert-space assembly problem

\[
\boxed{
\text{Mikawa pair-AP }L^2
+\text{ orthogonal `W` conductor geometry}
\stackrel{?}{\Longrightarrow}
\text{cross-conductor covariance }o(1).
}
\tag{21}
\]

A credible positive route is a martingale/Carleson or large-sieve inequality that preserves orthogonality of the exact-support local components before the scalar conductor sum is formed. A decisive negative route would show that any such assembly necessarily incurs an `X^{o(1)}` loss too large for Mikawa's fixed-power logarithmic savings.

The factor `6^omega(d)` in (18) is not by itself the main obstruction. One may truncate `omega(d)` at `J=C log log X`; then `6^J` is only a fixed power of `log X`, absorbable by choosing the arbitrary logarithmic exponent in (8) larger, while the omitted `W`-spectral tail is far beyond the mean support size `asymp log log w` and can be made tiny by elementary Bernoulli/Chernoff bookkeeping. The hard part is the **number and coherence of the remaining conductors**, not the divisor factor on one conductor. This truncation observation is a program guide, not a completed bound for (19).

## 6. Three load-bearing splice gates remain

Even a solution of (20) would not yet certify the Yang one-sided fourth moment. Three source-specific interfaces must be checked rather than inferred.

**Local-main normalization.** Mikawa subtracts the Hardy--Littlewood pair main (2) in each residue class. The Yang welding decomposition uses the exact `W`-local pair main and WI-049's full four-form local factorization. One must prove that the residue-class main subtracted in (12) splices to that deterministic local main with only already-booked `o(1)` terms. Primes dividing the conditioning conductor, either shift, and the `p=2` parity factor must be handled explicitly.

**Translated and moving intervals.** Mikawa states a prefix theorem with both primes `<=x`. A single translated pair interval can be written as a difference of two prefix pair counts after intersecting the two shifted physical intervals, but the Yang endpoints move with the cell and shift. A maximal-over-endpoints version, dyadic interval decomposition with a proved boundary budget, or a direct short-interval pair-AP theorem is needed before the whole source family can be inserted. The nearby literature includes Maurizio Laporta, *A short intervals result for 2n-twin primes in arithmetic progressions*, Tsukuba J. Math. 23 (1999), 201--214, but its exact theorem surface was not reconstructed in this pass and is therefore not used as evidence here.

**Two-leg locked geometry.** Mikawa conditions one prime pair modulo one auxiliary modulus. The Yang covariance locks two pair shifts through the same `k` and then averages over the two prime-power bases. Equation (18) is useful precisely because the nonnegative shift square sum may be restricted to a structured subset, but the second base, Mertens weights, source Jacobians, collisions and boundary strip must still be propagated with the exact normalization of WI-033/WI-046--WI-050.

## 7. Adjacent multiplet prior art does not remove those gates

Koichi Kawada, *The prime k-tuplets in arithmetic progressions*, Tsukuba J. Math. 17 (1993), 43--57, is directly adjacent prior art. Its Theorem 2 proves, for fixed linear coefficients and a short physical interval `y`, an averaged arithmetic-progression asymptotic for prime `k`-tuplets with

\[
Q\le yx^{-1/2}(\log x)^{-B},
\tag{22}
\]

and `y>x^(2/3) log^C x`; primary source: https://tsukuba.repo.nii.ac.jp/record/15690/files/3.pdf . This confirms that prime-multiplet AP dispersion is a classical research surface rather than a new Yang-specific concept.

It is not a black-box solution for the live four-form system. Kawada fixes the linear coefficients `a_j` and averages over intercept parameters, whereas the Yang reduced coefficients themselves range through power-sized prime bases. This is the same growing-coefficient distinction that made Bienvenu useful only in the fixed-polylog regime in WI-050. No growing-coefficient conclusion is imported from Kawada.

## 8. Consequence for the live clue and the research priority

The prior chain WI-057--WI-060 had reduced the source problem to one of three possibilities: invent a residue-conditioned pair theorem, prove cross-mode cancellation, or prove the localized covariance directly. Mikawa eliminates the first item as an invention task. The revised shortest credible chain is

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

The bold arrow is now the highest-value mathematical target. Re-running ordinary MRT, first-order BDH, or mode-by-mode fixed-log estimates would repeat routes already closed by WI-057/WI-060. Conversely, proving (20) with a fixed logarithmic loss would materially change the status of the Yang one-sided fourth-moment candidate because the per-conductor arithmetic input is already classical and reaches much farther in modulus than the `W` spectrum requires.

## 9. Prior-art / novelty audit

Primary and authoritative sources checked in this pass:

- H. Mikawa, **On prime twins in arithmetic progressions**, *Tsukuba Journal of Mathematics* 16:2 (1992), 377--387, DOI `10.21099/tkbjm/1496161970`; open PDF https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf . Load-bearing source for (1)--(8), especially p. 379 for the modulus-weighted square factor.
- zbMATH review of Mikawa, https://portal.mardi4nfdi.de/wiki/Item%3AQ2367079 . Independent bibliographic confirmation of the theorem and square-root modulus range.
- Koichi Kawada, **The prime k-tuplets in arithmetic progressions**, *Tsukuba Journal of Mathematics* 17:1 (1993), 43--57; open PDF https://tsukuba.repo.nii.ac.jp/record/15690/files/3.pdf . Adjacent multiplet-AP prior art; not consumed as a growing-coefficient theorem.
- Natalie Evans, **Correlations of almost primes**, *Math. Proc. Cambridge Philos. Soc.* 174 (2023), 301--344, DOI `10.1017/S0305004122000251`. Modern contextual source locating Mikawa in the average prime-correlation literature; not load-bearing for the new deduction.
- Maurizio Laporta, **A short intervals result for 2n-twin primes in arithmetic progressions**, *Tsukuba Journal of Mathematics* 23 (1999), 201--214. Identified as the closest short-interval follow-up; exact hypotheses not used until separately audited.

No novelty is claimed for Mikawa's theorem, Linnik dispersion, Cauchy--Schwarz, Parseval, or prime-tuple AP distribution. The line-specific deductions are the exact alignment (10)--(18) with WI-058's conductor energy and the resulting identification of **cross-conductor assembly**, rather than absence of a conditioned pair theorem, as the remaining spectral obstruction. A targeted audit did not locate this specific Yang/`W`-local splice in the cited literature; that absence is not used as a priority claim.

## 10. Decisive promotion / falsification tests

Promote this route toward a theorem only after all of the following are proved with the source normalization.

1. **Main-term identity:** identify Mikawa's residue-class Hardy--Littlewood main with the exact `W`-local/full four-form main used after WI-049, including `p=2`, non-coprime residues and collision bookings.
2. **Maximal interval transfer:** prove a pair-AP analogue adequate for all moving Yang physical intervals with no power loss that destroys (8), either from Mikawa's proof, Laporta/related short-interval prior art, or a fresh dyadic maximalization.
3. **Cross-conductor square function:** prove an inequality of the form (20) with at most a fixed logarithmic loss, or an equivalent martingale/large-sieve estimate that combines the exact-support conductor pieces before triangle inequality.
4. **Locked-shift bookkeeping:** show that restricting Mikawa's shift square sum to `h_2=qk` and integrating the first/second base Mertens weights preserves an `o(1)` normalized remainder over the full source support after the already-separated boundary strip.
5. **End-to-end remainder gate:** insert the resulting welding bound into the certified deterministic core and compare with the `R(1)<0.0380702829...` threshold from WI-028 before making any new simple-zero claim.

Narrow or withdraw the redirection if Mikawa's displayed second factor cannot be made uniform for the exact translated residue-class errors needed by Yang, or if the cross-conductor family necessarily forces the same super-polylogarithmic Wiener loss as WI-060. Either outcome would be substantive: the first would close this prior-art splice, while the second would establish a more precise barrier for the entire `W`-local square-function route.
