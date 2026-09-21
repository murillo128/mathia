# PL-415 — The away-from-5 source repair diagonalizes into a signed Dirichlet-character variance supertrace

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + SOURCE-BRIDGE + SPECTRAL-REDIRECT`.

**Parent findings:** `PL-407`, `PL-412`, `PL-413`, `PL-414`.

## Claim

`PL-414` realizes the unique `p=5` endpoint repair as a finite additive Fourier projection over the five frequencies `j/5`. There is a second exact diagonalization which is better matched to the spectral/zero side: on the unit group modulo `5`, the same inverse local factor is a signed combination of the four multiplicative Dirichlet characters.

Let `chi` run over the four Dirichlet characters modulo `5`, extended by zero on multiples of `5`, and let `chi_0` be the principal character. For `5\nmid nm`, character orthogonality gives

\[
\sum_{\chi\bmod 5}\chi(n)\overline{\chi(m)}
=4\,1_{n\equiv m\pmod 5}.
\tag{1}
\]

Since the away-from-5 multiplier from `PL-414` is

\[
g_5(h)=\beta_5(h)^{-1}
=\begin{cases}
4/5,&5\mid h,\\
16/15,&5\nmid h,
\end{cases}
\tag{2}
\]

(1) implies the exact unit-group identity

\[
\boxed{
 g_5(m-n)
 =\chi_0(n)\overline{\chi_0(m)}
 -\frac1{15}\sum_{\substack{\chi\bmod5\\\chi\ne\chi_0}}
 \chi(n)\overline{\chi(m)}
 }
\qquad (5\nmid nm).
\tag{3}
\]

Thus the local repair is not only a five-sector additive Fourier projector. It is also the rational virtual character

\[
\boxed{
 g_5(a/b)
 =\chi_0(a/b)-\frac1{15}\sum_{\chi\ne\chi_0}\chi(a/b)
 =\frac1{15}\bigl(16\,\mathbf 1-\chi_{\mathrm{reg}}\bigr)(a/b)
 }
\tag{4}
\]

on `(Z/5Z)^times`. The negative coefficient is essential: this is a signed virtual-character decomposition, not a positive representation.

For the actual prime-pair source, define

\[
C_{X,\chi}(h)
:=\sum_{n\le X}
\Lambda(n)\chi(n)\Lambda(n+h)\overline{\chi(n+h)}.
\tag{5}
\]

Because `Lambda(n)` is nonzero on a multiple of `5` only when `n` is a power of `5`, (3) yields uniformly for `1\le h\le X`

\[
\boxed{
 g_5(h)C_X(h)
 =C_{X,\chi_0}(h)
 -\frac1{15}\sum_{\chi\ne\chi_0}C_{X,\chi}(h)
 +O((\log X)^2).
 }
\tag{6}
\]

The same decomposition also diagonalizes the Hardy--Littlewood source term. Consequently the source-subtracted away-from-5 cubic observable can be expressed, up to the explicit power-of-5 error, as one fixed signed combination of Dirichlet-character short-interval variances. Modulo complex conjugation there are only **three distinct real variance sectors**: the principal character, the quadratic character, and one quartic character. Therefore the five separate additive-sector bounds stated in `PL-414` are a convenient sufficient condition but are not the intrinsic target. The actual bridge only requires control of one signed character superposition, so cancellation between the Dirichlet-`L` sectors remains available.

This also identifies a new guardrail. The nonprincipal sectors are precisely degree-one primitive Dirichlet-`L` variance problems. Standard zero-pair routes to such power-saving variances are tied to zero statistics of `L(s,chi)` and are commonly formulated under GRH. Proving the three sectors independently through that machinery would therefore import arithmetic hypotheses stronger than RH for `zeta` alone. A viable unconditional route should instead exploit the fixed signed combination in (6), or prove its variance estimate directly, rather than silently assume separate critical-line control for the auxiliary Dirichlet `L`-functions.

## 1. Exact character diagonalization of the local factor

For units `n,m mod 5`, put `r=n m^{-1}`. The four characters form the complete dual of the cyclic group `(Z/5Z)^times`. Hence

\[
\sum_{\chi\bmod5}\chi(r)
=\begin{cases}4,&r=1,\\0,&r\ne1.\end{cases}
\tag{7}
\]

Subtracting the principal character gives

\[
\sum_{\chi\ne\chi_0}\chi(n)\overline{\chi(m)}
=\begin{cases}3,&n\equiv m\pmod5,\\-1,&n\not\equiv m\pmod5.\end{cases}
\tag{8}
\]

The right side of (3) is therefore `1-3/15=4/5` in the first case and `1+1/15=16/15` in the second, proving (3).

There is a useful general control. For an odd prime `p`, the inverse Hardy--Littlewood local pair factor on units has the same form

\[
g_p(m-n)
=\chi_0(n)\overline{\chi_0(m)}
-\frac1{p(p-2)}
\sum_{\chi\ne\chi_0\bmod p}
\chi(n)\overline{\chi(m)}.
\tag{9}
\]

Indeed the two local values are `(p-1)/p` when `p\mid(m-n)` and `(p-1)^2/[p(p-2)]` otherwise, while the nonprincipal character sum is `p-2` or `-1`. Equation (3) is the `p=5` specialization. This control shows that the coefficient `1/15` is forced by the standard local-density algebra; it is not tuned to the cubic kernel.

## 2. The actual-prime correlation identity

For a term in `C_X(h)=sum_{n<=X}Lambda(n)Lambda(n+h)`, if both `n` and `n+h` are coprime to `5`, equation (3) applies termwise. If one is not coprime to `5`, its von Mangoldt weight can be nonzero only when that integer is `5^k`. There are `O(log X)` such powers in the relevant range, and each pair contributes `O((log X)^2)` in total under the same estimate used in `PL-414`. Hence (6).

This is an exact finite-group identity for the actual prime-power-supported source. No Hardy--Littlewood asymptotic, RH, GRH, Euler-product continuation, or zero statistic is used to obtain it.

The additive decomposition of `PL-414` and the multiplicative decomposition (6) preserve different structure. The additive basis diagonalizes translation on `Z/5Z`; the multiplicative basis diagonalizes the unit-group action and is the one naturally attached to Dirichlet `L`-functions. Neither representation creates new information. The gain is that the second representation exposes exactly which spectral channels the repaired source couples to.

## 3. The Hardy--Littlewood source diagonalizes in the same basis

Write

\[
\mathfrak S^{(5)}(h)=g_5(h)\mathfrak S(h)
\tag{10}
\]

for the singular series with the `p=5` factor removed, as in `PL-413`--`PL-414`. For a character `chi mod 5`, define the local character correlation

\[
A_\chi(h)
:=\sum_{a\bmod5}\chi(a)\overline{\chi(a+h)}.
\tag{11}
\]

The fixed-residue Hardy--Littlewood calculation in `PL-414` gives the corresponding character-weighted model source

\[
M_{X,\chi}(h)
:=\frac{5X}{16}\,\mathfrak S^{(5)}(h)A_\chi(h).
\tag{12}
\]

For the principal character,

\[
A_{\chi_0}(h)
=\begin{cases}4,&5\mid h,\\3,&5\nmid h,\end{cases}
\tag{13}
\]

while for every nonprincipal character

\[
A_\chi(h)
=\begin{cases}4,&5\mid h,\\-1,&5\nmid h.\end{cases}
\tag{14}
\]

The second identity is the standard complete shifted character autocorrelation. Therefore

\[
\boxed{
 M_{X,\chi_0}(h)
 -\frac1{15}\sum_{\chi\ne\chi_0}M_{X,\chi}(h)
 =X\mathfrak S^{(5)}(h).
 }
\tag{15}
\]

For `5|h`, the bracket in units of `(5X/16)S^(5)` is `4-12/15=16/5`; for `5\nmid h` it is `3+3/15=16/5`. Thus the exact character identity is compatible with the source subtraction, not merely with the raw correlation.

Define

\[
\Delta C_{X,\chi}(h)
:=C_{X,\chi}(h)-M_{X,\chi}(h)
\tag{16}
\]

and

\[
\Delta C_X^{(5)}(h)
:=g_5(h)C_X(h)-X\mathfrak S^{(5)}(h).
\tag{17}
\]

Then (6) and (15) give

\[
\boxed{
\Delta C_X^{(5)}(h)
=\Delta C_{X,\chi_0}(h)
-\frac1{15}\sum_{\chi\ne\chi_0}\Delta C_{X,\chi}(h)
+O((\log X)^2).
}
\tag{18}
\]

The same source conventions and diagonal projection as `PL-406`--`PL-414` are understood here.

## 4. Only three distinct real short-interval variance sectors remain

For integer `L`, let

\[
\Delta T_{X,\chi}(L)
:=\sum_{h\in\mathbb Z}(L-|h|)_+\Delta C_{X,\chi}(h).
\tag{19}
\]

Equivalently, before source subtraction, the triangular term is the short-interval second moment

\[
T_{X,\chi}(L)
=\sum_x\left|\sum_{r=1}^{L}\Lambda(x+r)\chi(x+r)\right|^2
\tag{20}
\]

up to the same finite-support boundary convention as `PL-406`. This is precisely the natural short-interval variance observable attached to the logarithmic-derivative coefficients of `L(s,chi)`.

The character group modulo `5` consists of `chi_0`, one real quadratic character `chi_2`, and a conjugate pair of quartic characters `chi_4, overline{chi_4}`. Since the coefficients in (20) are conjugated when `chi_4` is replaced by `overline{chi_4}`,

\[
T_{X,\chi_4}(L)=T_{X,\overline{\chi_4}}(L),
\tag{21}
\]

and the model terms obey the same equality. Hence

\[
\boxed{
\Delta T_X^{(5)}(L)
=\Delta T_{X,\chi_0}(L)
-\frac1{15}\Delta T_{X,\chi_2}(L)
-\frac2{15}\Delta T_{X,\chi_4}(L)
+E_5(X,L),
}
\tag{22}
\]

where the exceptional power-of-5 contribution satisfies the crude bound

\[
E_5(X,L)=O(L^2(\log X)^2).
\tag{23}
\]

For every fixed `mu<1` and polynomial short-interval scale `L=X^theta`, `theta<1`, (23) is polynomially smaller than an `XL(L/X)^mu` target, apart from harmless logarithms. In particular it is harmless throughout the square-root calibration regime `mu=1/2` considered in `PL-407`.

Equation (22) sharpens the quantitative target left by `PL-414`. It is sufficient, but not necessary, to prove the `PL-407` power bound separately in all five additive sectors, or even separately in the three character sectors. The intrinsic condition is only

\[
\left|
\Delta T_{X,\chi_0}(L)
-\frac1{15}\Delta T_{X,\chi_2}(L)
-\frac2{15}\Delta T_{X,\chi_4}(L)
\right|
\ll
XL\left(\frac LX\right)^\mu(\log X)^B.
\tag{24}
\]

If (24) holds uniformly on the effective support of the cubic kernel, the derivation of `PL-407` is unchanged and gives

\[
|\mathcal E_\eta^{(5)}(X,H)|
\ll
H^{-1}(H/X)^\mu(\log X)^B,
\tag{25}
\]

so for `H=X^theta` the sufficient threshold remains

\[
\mu>\frac{3\theta}{4(1-\theta)}.
\tag{26}
\]

The important change is conceptual: (24) permits cancellation between the three `L`-channels that separate absolute-value estimates discard.

## 5. Spectral meaning and the GRH guardrail

For the principal character modulo `5`,

\[
L(s,\chi_0)=\zeta(s)(1-5^{-s}).
\tag{27}
\]

The extra zeros of the deleted Euler factor lie on `Re(s)=0`, so its nontrivial zeros in the open critical strip are exactly the Riemann-zeta zeros. The principal sector is therefore the original zeta channel with the `p=5` local coordinate removed.

Every nonprincipal character modulo the prime `5` is primitive. Its logarithmic derivative has coefficients

\[
-\frac{L'}{L}(s,\chi)
=\sum_{n\ge1}\frac{\Lambda(n)\chi(n)}{n^s},
\qquad \Re s>1,
\tag{28}
\]

which are exactly the coefficients appearing in (20). Thus the two nonprincipal real sectors in (22) are genuine degree-one Dirichlet-`L` short-interval variance sectors, not merely formal residue twists.

This places the repaired source inside established prior art. Yildirim studied pair correlations of zeros of Dirichlet `L`-functions and their implications for primes in arithmetic progressions. Bui--Keating--Smith give a general Selberg-class framework relating power-sensitive short-interval variances of logarithmic-derivative coefficients to pair correlation of zeros; their zero-side theorems are formulated under GRH. Current work of Kandhil--Languasco--Moree likewise assumes GRH together with Dirichlet-`L` pair correlation to obtain strong prime-distribution consequences in arithmetic progressions.

The conclusion is a guardrail, not an impossibility theorem. One may not argue that the nonprincipal terms in (22) are harmless merely because their modulus is fixed. Proving each term by the standard zero-pair route can import GRH or comparable information for auxiliary Dirichlet `L`-functions, which is not supplied by RH for `zeta`. Conversely, equation (22) shows that the Mathia source does **not** require the individual terms to satisfy the desired power bound. A direct estimate of their fixed signed superposition could exploit cancellation and avoid proving three separate spectral conjectures.

## 6. Prior-art and novelty audit

The finite-character orthogonality in (1), the shifted character sum in (14), the relation between primes in arithmetic progressions and Dirichlet `L`-functions, and the short-interval-variance/pair-correlation correspondence are all classical or established structures. No novelty is claimed for those ingredients.

The main literature anchors checked are:

- **C. Yalcin Yildirim**, “The pair correlation of zeros of Dirichlet L-functions and primes in arithmetic progressions,” *Manuscripta Mathematica* **72** (1991), 325--334. DOI `10.1007/BF02568283`. It is direct prior art for using pair correlations of Dirichlet-`L` zeros to control prime arithmetic-progression statistics.
- **H. M. Bui, J. P. Keating, D. J. Smith**, “On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class,” *Journal of the London Mathematical Society* **94** (2016), 161--185, DOI `10.1112/jlms/jdw030`, arXiv:1506.03741. It gives the relevant degree-one short-interval variance / zero-pair framework and makes the GRH dependence of the zero-side transfer explicit.
- **Neelam Kandhil, Alessandro Languasco, Pieter Moree**, “Pair correlation of zeros of Dirichlet L-functions: a possible path towards the conjectures of Chowla, Elliott-Halberstam and Montgomery,” *Mathematische Annalen* **394** (2026), article 43, DOI `10.1007/s00208-026-03383-y`. It is a current guardrail showing that strong prime-distribution consequences from Dirichlet-`L` pair correlation remain coupled to GRH-type input.

Targeted repository and literature searches found no exact prior occurrence of the line-specific identity (6)/(22) as the diagonalization of the `PL-412`--`PL-414` **inverse `p=5` local factor inside the cubic source bridge**. The safe contribution is therefore narrow: an exact representation of the already-fixed Mathia observable and a reduction of its five additive sufficient sectors to one signed combination of three distinct Dirichlet-character variance sectors. It is not a new theorem about character sums, Dirichlet `L`-functions, Hardy--Littlewood, or pair correlation.

## 7. Adversarial audit

1. **The character transform does not improve an error estimate by itself.** Equations (6), (18), and (22) are exact changes of representation. Without a new bound on the signed combination, the `H^{-7/4}` source-replacement gate from `PL-407` remains open.

2. **Three separate bounds are still overkill.** Applying the triangle inequality to (22) recovers a sufficient condition but destroys the only new opportunity exposed here: cancellation between the principal, quadratic, and quartic sectors. Future work should test the combined statistic before estimating its components independently.

3. **Auxiliary GRH cannot be smuggled in.** The standard pair-correlation transfer for the nonprincipal Dirichlet `L`-functions is commonly formulated under GRH. Such an input would be stronger than the target RH statement for `zeta` and cannot serve as an unconditional proof of the bridge.

4. **The principal character is not literally zeta at the local level.** It deletes the `p=5` Euler factor as in (27). This changes boundary/local data but not the nontrivial zero divisor in `0<Re(s)<1`; the distinction must nevertheless be preserved in source formulas.

5. **The power-of-5 exception is explicit rather than absent.** Character extension by zero removes terms in which one endpoint is divisible by `5`, whereas `g_5 C_X` still contains prime-power terms `5^k`. Their contribution is the controlled error in (6) and (23), not an exact equality without remainder for the raw von Mangoldt source.

6. **No claim is made that Dirichlet-`L` zeros cancel spectrally in (22).** The signed variance identity is on the prime/source side. Turning it into a zero-side cancellation with enough precision would require a matched explicit-formula or variance-transfer theorem for the combined observable.

## Consequence for the line

`PL-414` left a five-component fixed-modulus variance target. The multiplicative character basis shows that this was not minimal. The away-from-5 source repair is intrinsically the rational virtual-character supertrace

\[
\chi_0-\frac1{15}(\chi_2+\chi_4+\overline{\chi_4}),
\tag{29}
\]

so the actual arithmetic target is the single signed variance combination (24). This is simultaneously better and more restrictive: it opens a cancellation route unavailable to componentwise estimates, but it also shows that naive spectral reduction immediately couples the zeta channel to genuine Dirichlet-`L` zero statistics.

The next useful pass should therefore ask whether the **combined** mod-5 character variance admits a direct power saving stronger than its components, or whether its explicit-formula zero side contains a structural cancellation forced by the coefficients `1,-1/15,-2/15`. Treating the three sectors independently should be used only as a control, because that route risks replacing the original RH problem by auxiliary GRH assumptions.