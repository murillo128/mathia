---
type: adversarial-review
target: research/weil_inertia/findings/WI-061-mikawa-pair-ap-dispersion-is-the-conditioned-input.md
---

# Adversarial review

## Adversary

Equation (18) is not justified by the displayed pointwise estimate (15). After (13) is relaxed to

\[
|C_d(k)|^2\le B_d(h_1(k))d^2\max_a |E_d(a,h_2(k))|^2,
\]

summing over an injective shift family yields a term proportional to

\[
\sum_{h_2}\max_a |E_d(a,h_2)|^2,
\]

whereas the Mikawa square-function input quoted in (8) controls

\[
\max_a\sum_{h_2}|E_d(a,h_2)|^2.
\]

The first quantity cannot in general be bounded by the second, so the stated transition from (15) to (18) interchanges `sum` and `max` in the wrong direction.

The intended per-conductor estimate appears repairable, but only by retaining exact Parseval before taking the residue-class maximum. Cauchy with (10) and the equality in (13) gives

\[
|C_d(k)|^2
\le B_d(h_1(k))\,d\sum_a |E_d(a,h_2(k))|^2.
\]

Using the uniform bound `dB_d(h_1)\le 6^{\omega(d)}`, then summing over the injective `h_2` family, gives

\[
\sum_k|C_d(k)|^2
\le 6^{\omega(d)}\sum_a\sum_{h_2}|E_d(a,h_2)|^2,
\]

which can be compared to Mikawa only after the exact admissible residue set is checked; for the coprime residue classes in the quoted theorem one would use at most `\varphi(d)` copies of `\max_a\sum_{h_2}|E_d(a,h_2)|^2`, hence at most the displayed `d` factor. The non-coprime residue conventions and local-main bookings in (12) must also be compatible with that step rather than silently absorbed.

Please either persist this corrected Parseval-before-maximum route, including the exact residue-domain bookkeeping, or provide another argument that legitimately fixes the same maximizing residue across all shifts. Until then, the claim that (18) is an exact deduction from Mikawa plus WI-058 has a material proof gap.

## Owner

The objection to the displayed `(15) -> (18)` transition is correct: taking the residue maximum pointwise and then summing the shifts loses the order of `max` and `sum`. The per-conductor conclusion survives by keeping Parseval exact until after the shift sum, but the residue-domain convention must be made explicit and the present equation (18) should not be persisted unchanged.

Mikawa's source fixes `(a,d)=1` from the outset. For the Fourier bookkeeping, extend the pair error to all residues by

\[
\widetilde E_d(a,h)=
\begin{cases}
E(x;d,a,h),&(a,d)=1,\\
\Psi(x;d,a,h),&(a,d)>1,
\end{cases}
\tag{R1}
\]

where the second line is not attributed to Mikawa: it is simply the actual von-Mangoldt pair count with no coprime-residue Hardy--Littlewood main subtracted. Let `\widetilde T_{d,b}` be its full additive Fourier transform. With the conventions of (10)--(14), Cauchy followed by exact Parseval gives

\[
\begin{aligned}
|C_d(k)|^2
&\le B_d(h_1(k))
   \sum_{b\bmod d}|\widetilde T_{d,b}(h_2(k))|^2\\
&=B_d(h_1(k))\,d
  \sum_{a\bmod d}|\widetilde E_d(a,h_2(k))|^2.
\end{aligned}
\tag{R2}
\]

Thus, for a booked subfamily on which `k -> h_2(k)` is injective into Mikawa's shift range, (17) gives

\[
\sum_k|C_d(k)|^2
\le 6^{\omega(d)}
\sum_{h_2}\sum_{a\bmod d}|\widetilde E_d(a,h_2)|^2.
\tag{R3}
\]

Put

\[
M_d:=\max_{(a,d)=1}
\sum_{0<2k\le x}|E(x;d,a,2k)|^2.
\]

The reduced residues now compare to Mikawa in the correct order:

\[
\sum_{(a,d)=1}\sum_{h_2}|E(x;d,a,h_2)|^2
\le \varphi(d)M_d
\le dM_d.
\tag{R4}
\]

There is also a deterministic bound for the non-reduced classes. Since `\Lambda(n)\ne0` and `(n,d)>1` force `n=p^r` for some prime `p|d`, for every fixed admissible shift `h`

\[
\begin{aligned}
\sum_{(a,d)>1}|\Psi(x;d,a,h)|^2
&\le
\left(
\sum_{(a,d)>1}\Psi(x;d,a,h)
\right)^2\\
&\le
\left(
(\log x)
\sum_{p\mid d}\sum_{r:p^r\le x}\log p
\right)^2\\
&\le \omega(d)^2(\log x)^4.
\end{aligned}
\tag{R5}
\]

The first inequality uses nonnegativity. Summing over at most `x` shifts yields

\[
\sum_{h_2}\sum_{(a,d)>1}|\Psi(x;d,a,h_2)|^2
\le x\,\omega(d)^2(\log x)^4.
\tag{R6}
\]

Consequently the source-compatible per-conductor statement is

\[
\boxed{
\sum_k|C_d(k)|^2
\le
6^{\omega(d)}
\left[
 dM_d+x\,\omega(d)^2(\log x)^4
\right].
}
\tag{R7}
\]

The first bracketed term is exactly the modulus-weighted square function occurring in the Mikawa input. The second is a prime-power/non-reduced-residue booking, not a new arithmetic hypothesis. It is negligible even after the modulus sum: for every fixed `\varepsilon>0`, `6^{\omega(d)}\omega(d)^2\ll_\varepsilon d^\varepsilon`, so for `Q\le x^{1/2}(\log x)^{-B}` its total contribution is

\[
\ll_\varepsilon x(\log x)^4Q^{1+\varepsilon}
=o_A\!\left(x^3(\log x)^{-A}\right)
\]

for every fixed `A` after increasing `x`.

Thus the review does not restore the original literal equation (18); it repairs the mathematical claim behind it. The physical conductor still cancels against the exact-support Fourier energy, leaving the same divisor-type `6^{\omega(d)}` price on the Mikawa-controlled term, while the non-coprime residue classes contribute only a separately negligible prime-power error. The cross-conductor assembly, translated/moving-interval splice, exact local-main matching, parity/collision booking, and two-leg locked geometry remain open exactly as stated in §§5--6. If the adversary accepts this as the same claim identity, the canonical finding should be updated in place to replace (12)--(18)'s ambiguous residue convention and incorrect max/sum step by (R1)--(R7).
