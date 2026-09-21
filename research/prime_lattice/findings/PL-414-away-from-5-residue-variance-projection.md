# PL-414 — Away-from-5 de-aliasing is an exact finite residue-class / Fourier projection of the prime-pair source

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + SOURCE-BRIDGE + FINITE-FOURIER-PROJECTION`.

**Parent findings:** `PL-406`, `PL-407`, `PL-412`, `PL-413`.

## Claim

`PL-412` repairs the endpoint Mellin criterion by deleting the unique dangerous local coordinate `p=5`, and `PL-413` shows that this deletion is exactly the standard singular-series operation “away from 5.” The remaining question there was whether that repaired model source has a natural actual-prime realization rather than being only a manipulated Euler factor.

For prime pairs it does. Let

\[
\beta_5(h)
:=\frac{1-\nu_5(h)/5}{(1-1/5)^2},
\qquad
\nu_5(h)=\begin{cases}1,&5\mid h,\\2,&5\nmid h,\end{cases}
\tag{1}
\]

be the ordinary `p=5` Hardy--Littlewood local factor, and write

\[
\mathfrak S^{(5)}(h):=\frac{\mathfrak S(h)}{\beta_5(h)},
\qquad
g_5(h):=\beta_5(h)^{-1}.
\tag{2}
\]

Then

\[
g_5(h)=
\begin{cases}
4/5,&5\mid h,\\
16/15,&5\nmid h.
\end{cases}
\tag{3}
\]

If

\[
C_X(h):=\sum_{n\le X}\Lambda(n)\Lambda(n+h),
\tag{4}
\]

then `g_5(h)C_X(h)` is, up to the negligible terms in which one of the two prime powers is a power of `5`, exactly a normalized average of the pair correlations in the admissible residue classes modulo `5`. More precisely, put

\[
\mathcal A_5(h)
:=\{a\in\mathbb Z/5\mathbb Z:\ a\ne0,\ a+h\ne0\},
\qquad
|\mathcal A_5(h)|=5-\nu_5(h),
\tag{5}
\]

and

\[
C_{X,a}^{(5)}(h)
:=\sum_{\substack{n\le X\\ n\equiv a\pmod5}}
\Lambda(n)\Lambda(n+h).
\tag{6}
\]

Uniformly for `1<=h<=X`,

\[
\boxed{
 g_5(h)C_X(h)
 =\frac{16}{5|\mathcal A_5(h)|}
 \sum_{a\in\mathcal A_5(h)}C_{X,a}^{(5)}(h)
 +O((\log X)^2).
}
\tag{7}
\]

At the Hardy--Littlewood local-density level, each individual admissible residue class has the same away-from-5 main term

\[
C_{X,a}^{(5)}(h)
\sim \frac{5X}{16}\,\mathfrak S^{(5)}(h),
\qquad a\in\mathcal A_5(h),
\tag{8}
\]

so (7) has main term `X mathfrak S^(5)(h)`. Thus the `p=5` repair is not an arbitrary correction on the model side: it is the local-density normalization obtained by conditioning the actual pair on an admissible residue class modulo `5`.

There is a second exact consequence. The multiplier `g_5` is only a finite `Z/5Z` Fourier projector:

\[
\boxed{
 g_5(h)
 =\frac{76}{75}
 -\frac4{75}\sum_{j=1}^{4}e(jh/5),
 \qquad e(x):=e^{2\pi i x}.
}
\tag{9}
\]

Hence the away-from-5 cubic source-replacement error from `PL-406`--`PL-407` is a fixed linear combination of **five** ordinary/twisted quadratic prime-variance sectors. The deletion of the dangerous `p=5` Euler coordinate therefore introduces no new infinite-dimensional analytic obstruction; it replaces the untwisted variance target by a finite vector of mod-5 twisted variance targets. If those five sectors satisfy the same LPZ-shaped power-saving bound, the threshold curve of `PL-407` is unchanged.

This advances the source bridge but does not prove it at the required precision. Existing almost-all prime-correlation and short-interval uniformity theorems handle fixed periodic/arithmetic-progression structure at logarithmic or qualitative precision, whereas the `PL-404` zero layer still requires the power-small signed remainder calibrated in `PL-407`.

## 1. Exact residue-class identity

For a pair `(n,n+h)` with both von Mangoldt weights nonzero, failure to belong to one of the classes in `mathcal A_5(h)` can occur only when `n` or `n+h` is a power of `5`. There are `O(log X)` such powers up to `2X`, and each exceptional product is `O(log X)`. Therefore

\[
C_X(h)
=\sum_{a\in\mathcal A_5(h)}C_{X,a}^{(5)}(h)
+O((\log X)^2)
\tag{10}
\]

uniformly for `1<=h<=X`.

From (1),

\[
\beta_5(h)
=\frac{5(5-\nu_5(h))}{16}
=\frac{5|\mathcal A_5(h)|}{16}.
\tag{11}
\]

Multiplying (10) by `g_5=beta_5^{-1}` proves (7). Since `g_5` is bounded between `4/5` and `16/15`, the exceptional term remains `O((log X)^2)`.

This is an exact identity about the actual prime-power-supported von Mangoldt sequence. No Hardy--Littlewood conjecture or zeta continuation is used in (7).

## 2. Why an admissible residue class has the away-from-5 local factor

Fix `a in mathcal A_5(h)` and write `n=5m+a`. The two affine forms are

\[
L_1(m)=5m+a,
\qquad
L_2(m)=5m+a+h.
\tag{12}
\]

For every prime `ell ne 5`, multiplication by `5` is invertible modulo `ell`, so the local factor of this pair of forms is exactly the usual `beta_ell(h)`. At `ell=5`, both forms are nonzero constants because `a` is admissible. Thus their local von Mangoldt weights are each `5/4`, and the local factor in the `m` variable is

\[
\left(\frac54\right)^2=\frac{25}{16}.
\tag{13}
\]

The `m` interval has length `X/5+O(1)`. Therefore the Hardy--Littlewood prediction for (6) is

\[
\frac X5\cdot\frac{25}{16}
\prod_{\ell\ne5}\beta_\ell(h)
=\frac{5X}{16}\mathfrak S^{(5)}(h),
\tag{14}
\]

which proves the local-density statement (8). Summing (14) over the `5-nu_5(h)` admissible classes restores

\[
\frac{5(5-\nu_5(h))}{16}\mathfrak S^{(5)}(h)
=\mathfrak S(h),
\tag{15}
\]

as it must.

This calculation is standard Hardy--Littlewood local-factor algebra. Kuperberg's arithmetic-progression singular-series formalism packages exactly this operation by deleting local factors at primes dividing the progression modulus. No general novelty is claimed for (12)--(15); the line-specific point is that the unique `p=5` de-aliasing required by `PL-412` lands on this standard arithmetic conditioning without any extra choice.

## 3. Exact finite Fourier decomposition

Equation (3) can be written

\[
g_5(h)
=\frac{16}{15}-\frac4{15}\,1_{5\mid h}.
\tag{16}
\]

Using finite Fourier orthogonality

\[
1_{5\mid h}=\frac15\sum_{j=0}^{4}e(jh/5)
\tag{17}
\]

gives (9).

Let `f:Z->C` have finite support and

\[
C_f(h)=\sum_n f(n)\overline{f(n+h)}.
\tag{18}
\]

For the even cubic kernel `K_eta` from `PL-406`, define

\[
Q^{(5)}_{\eta,H}(f)
:=\sum_{h\in\mathbb Z}
K_\eta(h/H)g_5(h)C_f(h).
\tag{19}
\]

Put

\[
f_j(n):=f(n)e(-jn/5),\qquad 1\le j\le4.
\tag{20}
\]

Then

\[
C_{f_j}(h)=e(jh/5)C_f(h),
\tag{21}
\]

so (9) gives the exact identity

\[
\boxed{
Q^{(5)}_{\eta,H}(f)
=\frac{76}{75}Q_{\eta,H}(f)
-\frac4{75}\sum_{j=1}^{4}Q_{\eta,H}(f_j).
}
\tag{22}
\]

Every term on the right is an ordinary quadratic Fourier statistic of the form already treated in `PL-406`. If

\[
F_j(\alpha)=\sum_n f_j(n)e(n\alpha),
\tag{23}
\]

then `F_j(alpha)=F(alpha-j/5)`, so (22) merely samples the same additive prime spectrum in the five rational frequency sectors `0,1/5,...,4/5`.

Likewise, the triangular representation of `PL-406` gives

\[
Q_{\eta,H}(f_j)
=\frac1H\int_0^\infty
K_\eta''(t)T_{f_j}(Ht)\,dt,
\tag{24}
\]

where for integer `L`

\[
T_{f_j}(L)
=\sum_x\left|\sum_{r=1}^{L}f(x+r)e(-jr/5)\right|^2.
\tag{25}
\]

Thus deleting the `p=5` local source coordinate becomes a finite family of short-interval second moments with additive mod-5 twists. It does **not** produce a new Euler-product continuation problem on the actual-prime side.

## 4. Quantitative consequence for the PL-407 threshold

Let

\[
\Delta C_X(h)=C_X(h)-X\mathfrak S(h)
\tag{26}
\]

with the same source-relative boundary conventions as `PL-406`--`PL-407`. Since `mathfrak S^(5)=g_5 mathfrak S`, the away-from-5 remainder is exactly

\[
\Delta C_X^{(5)}(h)
:=g_5(h)C_X(h)-X\mathfrak S^{(5)}(h)
=g_5(h)\Delta C_X(h).
\tag{27}
\]

Consequently its cubic weighted error is the same fixed combination (22), now applied linearly to the source-subtracted correlation. Define the five triangular remainders

\[
\Delta T_{X,j}(L)
:=\sum_{h\in\mathbb Z}(L-|h|)_+
 e(jh/5)\Delta C_X(h),
\qquad 0\le j\le4.
\tag{28}
\]

If, uniformly in the effective support of `K_eta''`,

\[
|\Delta T_{X,j}(L)|
\ll
XL\left(\frac LX\right)^\mu(\log X)^B
\qquad (j=0,1,2,3,4),
\tag{29}
\]

then the finite coefficients in (9) and the argument of `PL-407` give

\[
|\mathcal E_\eta^{(5)}(X,H)|
\ll_{\eta,\mu}
H^{-1}\left(\frac HX\right)^\mu(\log X)^B.
\tag{30}
\]

For `H=X^theta`, the sufficient source-replacement condition is therefore still

\[
\boxed{
\mu>\frac{3\theta}{4(1-\theta)}.
}
\tag{31}
\]

In particular the square-root calibration boundary remains `theta=2/5`.

There is an important asymmetry in this statement. A bound only for the untwisted sector `j=0` does **not** imply (30); the four rational-frequency sectors are additional arithmetic data. Conversely, because there are only four of them and the modulus is fixed, no loss in the power exponent occurs if a theorem controls them uniformly. The `p=5` repair therefore changes the **vector of variance observables**, not the required exponent curve.

The exceptional power-of-5 term in (7) is harmless on the same polynomial windows already used in `PL-406`: after the `1/(XH)` cubic normalization and summation over `O(H)` effective lags it contributes `O((log X)^2/X)`, which is `o(H^{-7/4})` whenever `H=o(X^{4/7}/(log X)^{8/7})` up to harmless logarithmic refinements.

## 5. Representation assessment

The source-side operation of `PL-413`,

\[
\mathfrak S(h)\longmapsto\mathfrak S^{(5)}(h)=g_5(h)\mathfrak S(h),
\tag{32}
\]

has two exact actual-prime representations:

- residue representation: multiply the full pair correlation by `g_5`, equivalently take the normalized mean over admissible residue classes modulo `5`, up to the explicit power-of-5 exceptional set in (7);
- Fourier representation: decompose `g_5` into the five characters of `Z/5Z`, giving (22)--(25).

The maps preserve the lag, cubic kernel, fixed-modulus local conditioning, and the source-subtracted error scale. The Fourier map is invertible as the ordinary finite Fourier transform on residue data, but the scalar away-from-5 projection by itself loses the four complementary residue-sector combinations. No analytic continuation is used in this representation step.

What is gained is a concrete actual-prime target for the repaired model. What is **not** gained is the missing power-saving theorem: the five twisted variances still have to be controlled at the `PL-407` precision.

## 6. Prior-art / novelty audit

The following literature was checked against the claim.

- **Vivian Z. Kuperberg**, “Sums of singular series along arithmetic progressions and with smooth weights,” *International Journal of Number Theory* **21**(1) (2025), 53--74, DOI `10.1142/S1793042125500046`, arXiv:2301.06095. Kuperberg explicitly studies singular series constrained to residue classes modulo `r` and introduces the singular series with primes dividing `r` removed. This is direct prior art for the arithmetic meaning of `mathfrak S^(5)` and for the fact that residue incidences control the fixed-modulus correction.
- **Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, Joni Teräväinen**, “Higher uniformity of arithmetic functions in short intervals II. Almost all intervals,” *Inventiones Mathematicae* **244** (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, arXiv:2411.05770. The paper proves almost-all Hardy--Littlewood correlations in polynomial shift ranges and its discorrelation machinery is explicitly uniform over arithmetic progressions / rational periodic components of bounded complexity. It shows that a fixed modulus such as `5` is structurally routine for current prime-uniformity methods, but the available savings remain qualitative or arbitrary fixed powers of `log X` at the relevant correlation stage, not the power precision in (29).
- The standard local-factor identity `beta_p=(1-nu_p/p)(1-1/p)^(-2)` and finite Fourier orthogonality on `Z/5Z` are classical. No novelty is claimed for those facts or for generic residue-class decompositions.

Targeted searches found no prior source making the **line-specific combination** used here: the unique `p=5` cancellation repair from `PL-412`, its away-from-5 endpoint conditioning from `PL-413`, and the exact reduction of the resulting actual-prime cubic source error to five rational-frequency variance sectors with the unchanged `PL-407` exponent threshold. The durable claim is therefore this bridge/reduction, not a new theorem about prime pairs in arithmetic progressions.

## 7. Boundary and falsification audit

- **Equation (7) is exact up to an explicit prime-power exception; equation (8) is a local-density / Hardy--Littlewood statement.** They must not be conflated. The present finding does not prove the fixed-shift prime-pair asymptotic.
- **No formal Euler-product continuation is used.** The only continuation-sensitive statement remains the model Mellin criterion already isolated in `PL-412`. Equations (7), (9), and (22) are finite arithmetic/Fourier identities.
- **Fixed modulus does not supply the required precision.** Existing prime-correlation uniformity with rational periodic weights does not imply (29) with positive `mu`. The target remains a much finer signed variance theorem or a direct explicit-formula evaluation of the tested functional.
- **Componentwise control is sufficient, not necessary.** Cancellation among the five Fourier sectors in (22) could beat the bound obtained by estimating each `Delta T_{X,j}` separately. Thus (31) is the inherited threshold of the absolute/componentwise route, not a universal barrier.
- **The projection is rational-prime specific only through the previously isolated aliasing at `p=5`.** A formally identical finite Fourier decomposition exists for deleting any fixed prime local factor. What is special here is that `PL-412` proved that `p=5` is the unique rational-prime coordinate capable of the relevant endpoint pole cancellation; the finite-modulus harmonic algebra itself is generic.
- **Beurling/generalized-prime control.** The residue-class interpretation uses the ordinary congruence ring modulo the rational prime `5`; a generic multiplicative generalized-prime system need not possess this additive finite quotient. This is genuine rational-prime arithmetic structure, although it still does not force RH without the missing variance estimate.

## Consequence for the line

The mismatch left by `PL-413` is narrower than it appeared. The repaired away-from-5 source already has a canonical actual-prime observable: normalize the pair correlation by the admissible mod-5 local density, or equivalently average it over admissible residue classes. On the harmonic side this is only a five-sector Fourier projection, so the repair is fully compatible with the `PL-406` short-interval-variance bridge and does not alter the `PL-407` power-saving exponent curve.

The live arithmetic target is now precise: control the **five source-subtracted mod-5 twisted short-interval variance sectors**, or their specific signed combination (22), at `o(H^-7/4)` after normalization. Another generic singular-series manipulation or another untwisted almost-all-shift theorem will not close the bridge.