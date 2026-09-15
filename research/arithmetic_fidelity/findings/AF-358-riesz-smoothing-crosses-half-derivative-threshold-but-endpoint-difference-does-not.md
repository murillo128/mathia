# AF-358 — Riesz smoothing crosses the half-derivative threshold but endpoint comparison does not

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

Retain AF-356's logarithmically normalized Riesz family

\[
E_\delta(y)
:=
e^{-y/2}\mathcal R_\delta[\Lambda-1](e^y),
\qquad
b_\delta(\rho)
:=
B(\rho,1+\delta)
=
\frac{\Gamma(\rho)\Gamma(1+\delta)}
{\Gamma(\rho+1+\delta)}.
\tag{1}
\]

Assume RH. Group repeated nontrivial zeros by distinct positive ordinates `gamma`, with multiplicity `m_gamma`, and write

\[
\rho_\gamma=\frac12+i\gamma.
\tag{2}
\]

The nontrivial-zero Fourier coefficients of `E_delta` are

\[
\widehat E_\delta(\gamma)
=-m_\gamma b_\delta(\rho_\gamma),
\qquad
\widehat E_0(\gamma)
=-\frac{m_\gamma}{\rho_\gamma}.
\tag{3}
\]

For a zero-frequency Fourier profile `F`, define the weighted Fourier--Besicovitch Sobolev energy

\[
\|F\|_{H^s_{B,\zeta}}^2
:=
2\sum_{\gamma>0}
(1+\gamma^2)^s
|\widehat F(\gamma)|^2.
\tag{4}
\]

At `s=0` this is exactly the nontrivial-zero contribution to AF-356's `B^2` seminorm. The subscript `zeta` emphasizes that `(4)` is the Hilbert scale on the actual zeta-zero frequency set rather than a claim about an arbitrary almost-periodic spectrum.

Then the Riesz order supplies an **exact amount of quadratic spectral regularity**:

\[
\boxed{
\|E_\delta\|_{H^s_{B,\zeta}}<\infty
\quad\Longleftrightarrow\quad
s<\frac12+\delta
}
\qquad(\delta\ge0),
\tag{5}
\]

where only the nontrivial-zero profile is meant in `(5)`.

But for every fixed `delta>0`, comparison with the endpoint has the **endpoint threshold, independent of the smoothing order**:

\[
\boxed{
\|E_\delta-E_0\|_{H^s_{B,\zeta}}<\infty
\quad\Longleftrightarrow\quad
s<\frac12.
}
\tag{6}
\]

Moreover, for every fixed `s<1/2`,

\[
\boxed{
\|E_\delta-E_0\|_{H^s_{B,\zeta}}
=O_s(\delta)
\qquad(\delta\downarrow0).
}
\tag{7}
\]

Thus AF-356's `B^2` continuity extends through every **strictly subcritical** quadratic Sobolev weight, but stops exactly at the half-derivative boundary.

This boundary is also the natural absolute-convergence threshold for the zeta-zero spectrum. Since the Riemann--von Mangoldt law gives `N(T)=O(T log T)`, Cauchy--Schwarz implies

\[
H^s_{B,\zeta}\subset \ell^1(\{\gamma\})
\qquad(s>1/2),
\tag{8}
\]

in the sense that any coefficient family with finite `(4)` is absolutely summable over the distinct zero ordinates. Consequently every fixed positive Riesz order has enough spectral regularity to cross this generic uniform-convergence gate: choose

\[
\frac12<s<\frac12+\delta.
\tag{9}
\]

The endpoint difference never crosses it, because `(6)` fails already at `s=1/2`.

So there is no ordinary **quadratic Sobolev upgrade** that turns AF-356's stable `B^2` comparison into a uniform endpoint comparison. The obstruction is not merely that `s=0` was too weak: every weighted `ell^2` scale of this form remains subcritical for `E_delta-E_0`. Any successful uniform moving-order estimate must exploit information not captured by these quadratic zero-mode energies, such as phase cancellation, maximal/tail control, short-interval coupling, or another source-native structure of the kind left open by AF-357.

## Derivation

### 1. A fixed Riesz order gains exactly `delta` derivatives on the zero spectrum

The classical Gamma-ratio asymptotic gives, for fixed `delta>=0`,

\[
\frac{\Gamma(\rho)}{\Gamma(\rho+1+\delta)}
=
\rho^{-1-\delta}\left(1+O_\delta(|\rho|^{-1})\right),
\qquad |\rho|\to\infty
\tag{10}
\]

in the vertical sector containing `rho_gamma`. Hence

\[
|b_\delta(\rho_\gamma)|
\asymp_\delta
(1+\gamma)^{-1-\delta}
\tag{11}
\]

for all sufficiently large `gamma`.

Let `m_gamma` be the zero multiplicity. The standard multiplicity bound gives

\[
m_\gamma\ll\log(2+\gamma),
\tag{12}
\]

while trivially

\[
m_\gamma^2\ge m_\gamma.
\tag{13}
\]

On a dyadic shell `T<gamma<=2T`, Riemann--von Mangoldt gives

\[
\sum_{T<\gamma\le2T}m_\gamma
=N(2T)-N(T)
\asymp T\log T.
\tag{14}
\]

For the upper bound in `(5)`, `(11)`--`(14)` give

\[
\begin{aligned}
\sum_{T<\gamma\le2T}
 m_\gamma^2(1+\gamma^2)^s
 |b_\delta(\rho_\gamma)|^2
&\ll_\delta
T^{2s-2-2\delta}
(\log T)
\sum_{T<\gamma\le2T}m_\gamma\\
&\ll_\delta
T^{2s-1-2\delta}(\log T)^2.
\end{aligned}
\tag{15}
\]

The dyadic series converges whenever `2s-1-2delta<0`, namely `s<1/2+delta`.

For the reverse implication, `(11)`, `(13)`, and `(14)` give

\[
\sum_{T<\gamma\le2T}
 m_\gamma^2(1+\gamma^2)^s
 |b_\delta(\rho_\gamma)|^2
\gg_\delta
T^{2s-1-2\delta}\log T.
\tag{16}
\]

At `s=1/2+delta` the shell contribution already grows like `log T`; above it grows polynomially. Hence the series diverges and `(5)` is exact.

### 2. Every fixed positive smoothing order has endpoint-like high-frequency difference

For fixed `delta>0`, `(10)` gives

\[
\rho\,b_\delta(\rho)
=
\Gamma(1+\delta)\rho^{-\delta}
\left(1+O_\delta(|\rho|^{-1})\right)
\longrightarrow0
\tag{17}
\]

along the zero ordinates. Therefore

\[
b_\delta(\rho)-\frac1\rho
=
-\frac1\rho\left(1+o(1)\right),
\tag{18}
\]

so

\[
\left|
b_\delta(\rho_\gamma)-\frac1{\rho_\gamma}
\right|
\asymp_\delta
\frac1{1+\gamma}
\tag{19}
\]

at high frequency. Repeating `(15)`--`(16)` with exponent `delta=0` proves the divergence half of `(6)` for every `s>=1/2`.

For the subcritical upper bound, AF-356 already derived uniformly for `0<=delta<=1`

\[
\left|
b_\delta(\rho_\gamma)-\frac1{\rho_\gamma}
\right|
\ll
\delta\,
\frac{\log(2+\gamma)}{1+\gamma}.
\tag{20}
\]

Using `(12)` and `(14)`, the dyadic contribution to the squared `H^s_{B,zeta}` norm is therefore

\[
\ll
\delta^2
T^{2s-1}(\log T)^4.
\tag{21}
\]

This is summable for every fixed `s<1/2`, proving both the upper half of `(6)` and `(7)`.

### 3. Why `s=1/2` is the uniform-convergence gate for this frequency set

For any coefficient family `a_gamma`, Cauchy--Schwarz gives

\[
\sum_{\gamma>0}|a_\gamma|
\le
\left(
\sum_{\gamma>0}(1+\gamma^2)^s|a_\gamma|^2
\right)^{1/2}
\left(
\sum_{\gamma>0}(1+\gamma^2)^{-s}
\right)^{1/2}.
\tag{22}
\]

The second factor is finite for `s>1/2`: the number of distinct ordinates in `[T,2T]` is at most `N(2T)-N(T)=O(T log T)`, so its dyadic shell is

\[
O\!\left(T^{1-2s}\log T\right).
\tag{23}
\]

Thus `(8)` follows directly, without needing a generic embedding theorem for arbitrary almost-periodic spectra. In particular, `(5)` shows that every `delta>0` admits some `s>1/2` and hence an absolutely convergent nontrivial-zero Fourier series.

The comparison profile behaves differently. By `(6)`, its weighted square energy diverges at the exact threshold needed for this Cauchy--Schwarz passage. This is a structural explanation for AF-356's metric split: positive Riesz smoothing makes each fixed profile regular enough for a uniform zero-series representation, but **the operation of removing that smoothing leaves an endpoint-sized high-frequency tail no matter how small the fixed positive order is**.

## Arithmetic-fidelity interpretation

AF-356 showed that `delta -> 0` is Lipschitz in ordinary `B^2`; AF-357 showed that scalar partial-sum and jump envelopes still permit worst-case endpoint loss of order `min{1,delta log X}`. The present result identifies the spectral regularity boundary between those facts.

The positive-order channel does not lose high-frequency information arbitrarily: it damps a zero ordinate `gamma` by an additional factor `gamma^{-delta}` and thereby buys exactly `delta` units of the weighted quadratic regularity `(4)`. But endpoint comparison cancels that gain asymmetrically. At frequencies `gamma >> exp(1/delta)`, the smoothed coefficient is negligible relative to `1/rho_gamma`, so the difference has the same high-frequency order as the endpoint itself.

That makes the endpoint obstruction a **moving-bandwidth problem**, not simply a lack of mean-square control. For small `delta`, the smoothing looks endpoint-like through an enormous but finite frequency range and only wins beyond a scale exponential in `1/delta`; AF-357 found the same exponential scale in physical/logarithmic lag through the Beta kernel. The two descriptions are compatible views of the same singular limit.

What remains open is therefore narrower. A source-native estimate can still beat this obstruction by exploiting arithmetic phase relations or cross-scale cancellation not visible in `(4)`. But strengthening AF-356 by inserting finitely many powers of frequency into the same quadratic spectral energy cannot reach uniform endpoint fidelity: the exact half-derivative threshold `(6)` blocks that route.

## Boundaries and falsification

- The result is conditional on RH, because the normalized nontrivial-zero terms become real Fourier frequencies only after `Re(rho)=1/2`.
- Statements `(5)`--`(7)` concern the nontrivial-zero Fourier--Besicovitch profile. The elementary pole/trivial-zero/floor corrections suppressed in AF-356 have zero `B^2` contribution there; no new pointwise claim about those terms is inferred from the seminorm alone.
- The `H^s_{B,zeta}` notation is defined by `(4)` for this finding. It is a Fourier-weighted Hilbert scale on the zeta-zero spectrum, not an assertion that every convention for Sobolev--Besicovitch spaces has identical notation or embedding hypotheses.
- Failure at `s=1/2` does **not** prove that every possible uniform or maximal estimate fails. It rules out the ordinary route that obtains uniformity from this family of weighted quadratic Fourier energies. Phase-sensitive, nonlinear, maximal, short-interval, or arithmetic-specific estimates remain possible.
- The proof groups multiplicities explicitly. No simplicity or linear-independence hypothesis for zero ordinates is used.
- The exact threshold uses only fixed `delta` in the Gamma-ratio asymptotic. It does not by itself give a sharp two-parameter norm law when `delta=delta(T)` varies simultaneously with frequency.

A direct falsification would be either a failure of the coefficient asymptotic `(11)` on the RH zero line or a zero-count/multiplicity law contradicting the dyadic estimates `(14)`--`(16)`. Both inputs are classical. A narrower audit is to check that an alternative proposed quadratic norm genuinely contains information beyond a monotone reweighting of the coefficients in `(4)`; otherwise `(6)` applies after the corresponding exponent conversion.

## Source / prior-art audit

The functional-analytic setting is established prior art. R. Iannacci, A. M. Bersani, G. Dell'Acqua, and P. Santucci, **“Embedding Theorems for Sobolev-Besicovitch Spaces of Almost Periodic Functions,”** *Zeitschrift für Analysis und ihre Anwendungen* **17** (1998), no. 2, 443--457, DOI `10.4171/ZAA/832`, develops Sobolev-type embedding theory for Sobolev--Besicovitch almost-periodic spaces. This finding does not claim to introduce that theory; `(4)` is an explicit zero-spectrum specialization and `(22)` gives the only embedding step actually needed here.

The Gamma-ratio asymptotic in `(10)` is standard; NIST DLMF §5.11(iii), especially Eqs. 5.11.12--5.11.13, records `Gamma(z+a)/Gamma(z+b) ~ z^(a-b)` with its asymptotic expansion in sectors away from the negative real axis. Riemann--von Mangoldt zero counting and the bound `m_gamma=O(log gamma)` are classical; see E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford (1986), Chapter 9. R. R. Hall, **“On the Zeros of the Riemann Zeta-Function,”** *J. London Math. Soc.* **59** (1999), 65--75, DOI `10.1112/S0024610798006942`, also explicitly recalls both the zero-count formula and the standard `O(log|gamma|)` multiplicity bound.

The Riesz/Beta zero coefficient and the `B^2` endpoint representation are inherited from AF-356, whose audit points to classical Riesz/Hardy--Riesz theory, Wintner's prime-number-theorem remainder distribution, and the modern `B^2` almost-periodic framework of Akbary--Ng--Shahabi.

A targeted search over Sobolev--Besicovitch embeddings, Riesz means of the von Mangoldt function, and zeta-zero almost-periodic expansions did not locate the exact thresholds `(5)`--`(7)` stated for this Riesz endpoint family. Absence from that search is not evidence of novelty. The durable contribution claimed here is narrower: combining the classical Gamma decay and zero-density law with AF-356's coefficient identity exposes an exact Mathia-relevant regularity barrier and rules out a natural quadratic-Sobolev repair of the moving endpoint problem.