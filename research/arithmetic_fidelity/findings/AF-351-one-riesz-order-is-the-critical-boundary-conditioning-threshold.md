# AF-351 — one Riesz order is the critical boundary-conditioning threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `TARGET-METRIC-CALIBRATION`, `BOUNDARY-CLARIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
c_n:=\Lambda(n)-1
\]

and, for a fixed integer `r>=0`,

\[
\mathcal R_r[c](X)
:=
\sum_{n\le X}c_n\left(1-\frac nX\right)^r.
\tag{1}
\]

AF-350 proves that an `O(X^theta)` bound for this profile excludes zeta zeros in `Re(s)>theta`. At the critical boundary `theta=1/2`, the smoothing order matters in a sharper way:

\[
\boxed{
\text{for every fixed integer }r\ge1,
\qquad
\mathrm{RH}
\iff
\mathcal R_r[\Lambda-1](X)=O_r(X^{1/2}).
}
\tag{2}
\]

The unsmoothed case is qualitatively different. Since

\[
\mathcal R_0[\Lambda-1](X)
=
\psi(X)-\lfloor X\rfloor,
\tag{3}
\]

Hardy--Littlewood's classical oscillation theorem gives, in particular,

\[
\boxed{
\mathcal R_0[\Lambda-1](X)\ne O(X^{1/2}).
}
\tag{4}
\]

Indeed the classical lower oscillation is larger by an unbounded `log log log X` factor along suitable sequences.

Thus the first Riesz smoothing order crosses an exact boundary-conditioning threshold. Order zero retains the critical zero modes with coefficients of size about `1/|gamma|`, whose accumulated boundary oscillation prevents an `O(sqrt(X))` readout. Every order `r>=1` inserts one additional inverse power of the zero height; the zero-mode coefficients become absolutely summable, so under RH the normalized critical profile is bounded while AF-350 guarantees that the same bound still detects every zero to the right of the critical line.

This is not a new RH criterion. It is a fidelity statement about a compression stage: **one order of smoothing improves the conditioning of the boundary zero signal without moving or erasing the RH discriminator.**

## Derivation

### 1. The reverse implication is already forced by AF-350

AF-350 shows for every fixed integer `r>=0` that

\[
\mathcal R_r[\Lambda-1](X)=O(X^\theta)
\quad\Longrightarrow\quad
\zeta(s)\ne0\qquad(\Re s>\theta).
\tag{5}
\]

Taking `theta=1/2`, an `O(X^{1/2})` bound gives no nontrivial zero to the right of the critical line. The functional equation reflects every nontrivial zero `rho` to `1-rho`, so a zero to the left would force one to the right. Therefore

\[
\mathcal R_r[\Lambda-1](X)=O(X^{1/2})
\quad\Longrightarrow\quad
\mathrm{RH}
\tag{6}
\]

for every fixed `r>=0`.

The issue left open by AF-350 was the converse at the boundary.

### 2. Under RH, one smoothing order makes the zero expansion absolutely summable

For integer `r>=1`, the classical Hardy--Littlewood Riesz explicit formula may be written, with the finite/trivial-pole terms collected into a bounded remainder, as

\[
\mathcal R_r[\Lambda](X)
=
\frac{X}{r+1}
-
\sum_\rho m_\rho B(\rho,r+1)X^\rho
+
O_r(1),
\qquad X\ge2,
\tag{7}
\]

where the sum is over distinct nontrivial zeros, `m_rho` is multiplicity, and

\[
B(s,r+1)
=
\frac{r!}{s(s+1)\cdots(s+r)}.
\tag{8}
\]

AF-348 gives for dense unit mass

\[
\mathcal R_r[1](X)=\frac{X}{r+1}+O_r(1).
\tag{9}
\]

Subtracting `(9)` from `(7)` yields

\[
\mathcal R_r[\Lambda-1](X)
=
-
\sum_\rho m_\rho B(\rho,r+1)X^\rho
+
O_r(1).
\tag{10}
\]

Assume RH. Then every nontrivial zero has

\[
\rho=\frac12+i\gamma.
\tag{11}
\]

For large `|gamma|`,

\[
|B(\rho,r+1)|
\ll_r
|\gamma|^{-r-1}.
\tag{12}
\]

The Riemann--von Mangoldt zero count gives

\[
N(T)=O(T\log T).
\tag{13}
\]

Hence a dyadic decomposition gives

\[
\sum_\rho m_\rho |B(\rho,r+1)|
<\infty
\qquad(r\ge1),
\tag{14}
\]

because the zeros with `2^j<|gamma|<=2^{j+1}` contribute at most

\[
O_r\!\left(j\,2^{-jr}\right).
\tag{15}
\]

Therefore the zero sum in `(10)` converges absolutely and uniformly after division by `X^{1/2}`. Under RH,

\[
\left|
\sum_\rho m_\rho B(\rho,r+1)X^\rho
\right|
\le
X^{1/2}
\sum_\rho m_\rho |B(\rho,r+1)|
=
O_r(X^{1/2}).
\tag{16}
\]

Together with `(10)`, this proves

\[
\mathrm{RH}
\quad\Longrightarrow\quad
\mathcal R_r[\Lambda-1](X)=O_r(X^{1/2})
\qquad(r\ge1).
\tag{17}
\]

Combining `(17)` with `(6)` proves the equivalence `(2)`.

### 3. The same calculation exposes the conditioning mechanism

Under RH, divide `(10)` by `X^{1/2}` and write `t=log X`. Then for `r>=1`,

\[
X^{-1/2}\mathcal R_r[\Lambda-1](X)
=
F_r(t)+o(1),
\tag{18}
\]

where

\[
F_r(t)
:=-
\sum_\rho
m_\rho B(\rho,r+1)e^{i\gamma t}.
\tag{19}
\]

By `(14)`, `(19)` is an absolutely and uniformly convergent Fourier series. Pairing conjugate zeros makes `F_r` real-valued. In particular it is a bounded uniformly almost-periodic function of logarithmic scale.

The relevant change from `r=0` to `r=1` is therefore not that smoothing removes the critical zero modes. Their frequencies `gamma` survive exactly. What changes is the conditioning of their amplitudes:

\[
B(\rho,1)=\frac1\rho
\asymp \frac1{|\gamma|},
\qquad
B(\rho,2)=\frac1{\rho(\rho+1)}
\asymp \frac1{|\gamma|^2}.
\tag{20}
\]

Since zero density is of order `T log T`, the first sequence is not absolutely summable while the second is. One smoothing order therefore converts a conditionally accumulated boundary signal into an absolutely summable one without changing the zero locations carried by that signal.

This gives an exact instance of the distinction emphasized by AF-349--AF-350:

\[
\boxed{
\text{better destination conditioning}
\ne
\text{loss of the target discriminator}.
}
\tag{21}
\]

### 4. Order zero cannot satisfy the same sharp boundary norm

For `r=0`, equation `(3)` gives

\[
\mathcal R_0[\Lambda-1](X)
=
\psi(X)-X+O(1).
\tag{22}
\]

Hardy and Littlewood proved the classical oscillation lower bound

\[
\psi(X)-X
=
\Omega_\pm\!\left(
X^{1/2}\log\log\log X
\right)
\tag{23}
\]

in the usual asymptotic sense. The `O(1)` floor correction is negligible, so `(23)` implies `(4)`.

This does not conflict with the usual RH prime-number-theorem error estimate. Under RH one has, classically,

\[
\psi(X)-X
=
O\!\left(X^{1/2}\log^2 X\right),
\tag{24}
\]

and therefore `O_epsilon(X^{1/2+epsilon})` for every positive `epsilon`. The exact `O(X^{1/2})` boundary norm is simply too strong before smoothing; the zero modes collectively force a slowly growing excess.

The transition at `r=1` is consequently real: the same arithmetic singularities that force the `r=0` boundary accumulation become absolutely summable after one Riesz factor.

## Prior art and novelty assessment

No novelty claim is made for the constituent analytic-number-theory statements.

- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41, 119--196 (1916), DOI `10.1007/BF02422942`, is direct classical prior art for the Riesz explicit formula used in `(7)` and for the large oscillation of `psi(x)-x` used in `(23)`. AF-350 already audited their equations (2.251)--(2.252) as the relevant zero-sensitive Riesz formula.
- E. C. Titchmarsh, revised by D. R. Heath-Brown, ***The Theory of the Riemann Zeta-function***, 2nd ed., Clarendon Press, Oxford (1986), is the standard source for the Riemann--von Mangoldt zero-count asymptotic and the explicit-formula machinery underlying `(13)`.
- NIST DLMF §25.10 records the classical zero distribution and points to Titchmarsh §4.17 for the zero-count framework.

The Arithmetic Fidelity contribution is the organization of these classical facts into a **sharp conditioning threshold for one declared compression**. AF-350 established that every fixed Riesz order preserves poles strictly above the error line. AF-351 adds that the first positive smoothing order is exactly enough to make the critical-line zero amplitudes absolutely summable, so the sharp `sqrt(X)` terminal norm becomes RH-equivalent even though the same norm is impossible at order zero.

## Boundaries and failure modes

### This does not make RH easier

Equation `(2)` is an equivalence. Proving the `O(sqrt(X))` bound for the prime source at any fixed `r>=1` is therefore already as strong as proving RH. Smoothing supplies boundary conditioning, not a shortcut around the arithmetic difficulty.

### The threshold concerns the sharp critical `C^0` norm

The statement does not say that `r=0` loses zero information. AF-350 shows the opposite: even order zero preserves every pole strictly to the right of its declared error exponent. The distinction here is only whether the exact boundary-scale norm `O(X^{1/2})` is compatible with the accumulated critical zero modes.

### Fixed finite order is essential

The constants may depend on `r`. No assertion is made for a smoothing order growing with `X`, for fractional orders near zero, or for a different kernel whose transform has a different high-frequency decay law.

### Absolute summability is a sufficient conditioning mechanism, not source recovery

Even for `r>=1`, the bounded normalized profile does not recover the coefficients `Lambda(n)-1`, prime support, prime gaps, or local sign geometry. AF-349 already shows that coefficient recovery requires a much stronger destination metric. AF-351 concerns only the RH zero discriminator encoded in the boundary Fourier modes.

### The critical line itself is allowed

The `O(X^{1/2})` bound does not remove poles on `Re(s)=1/2`; AF-350's Mellin argument only forces holomorphy strictly to the right. That is exactly why the bound can be compatible with RH while still retaining the critical zeros as the bounded oscillatory profile `(19)`.

## Consequence for Arithmetic Fidelity

AF-348 showed that finite Riesz smoothing can make radically different sparse and dense sources bounded-error indistinguishable. AF-349 located that loss in the weak destination metric rather than in the full transform. AF-350 then showed that the same weak error exponent still preserves Dirichlet singularities above its boundary.

AF-351 now identifies a complementary positive role for compression: **a transformation can discard difficult source-local structure and simultaneously improve the conditioning of the target-relevant global signal.** Here one Riesz order suppresses the high-zero tail from `1/|gamma|` to `1/|gamma|^2`, enough for absolute summability, while every zero's frequency and the off-critical singularity obstruction remain intact.

For the line's broader program this gives a more precise design rule. The useful question is not whether a compression preserves all arithmetic structure, nor even whether it monotonically loses information. One should ask whether it kills nuisance directions faster than it attenuates the target discriminator. In this model, `r=1` is the first order at which that trade is favorable in the sharp critical boundary norm.