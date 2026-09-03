# PC-144 — gap-two average remainder has exact Mertens rate

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-SIEVE-BOUNDARY`. PC-142 isolates the gap-two top band of the primitive-shell inverse-square chord Laplacian, and PC-143 proves that along primorials its spectral projector converges to the gap-two matching projector in normalized Frobenius average while failing to converge in operator norm. The proof of PC-143 deliberately gives no useful convergence rate for the average statement.

That missing scale can be extracted exactly. If
\[
N_x=\prod_{p\le x}p,
\qquad
L_x=A_x+R_x,
\qquad
A_x=\beta_{N_x}P_x,
\]
with `P_x` the gap-two matching projection of rank `E_x`, then
\[
T_x:=\frac{\operatorname{tr}(P_xR_xP_x)}{E_xN_x^2}
\]
satisfies
\[
\boxed{
(\log x)T_x\longrightarrow C_{\rm gap}>0.
}
\]
The constant is an absolutely convergent conditional reduced-residue singular-series average, given explicitly below. Hence the mean remainder energy seen from the canonical matching space is not merely `o(N_x^2)`: it is exactly of order `N_x^2/log x`. Equivalently it is asymptotic to a fixed positive multiple of the primorial totient density `phi(N_x)/N_x`.

This sharpens the density-one localization boundary of PC-143 but does not produce a new RH mechanism. The `1/log x` scale is forced by the ordinary Mertens product after conditioning a third primitive vertex on an existing gap-two primitive pair.

## 1. Orient the exact gap-two matching

For `x>=3`, every gap-two primitive edge has a unique orientation
\[
\{a,a+2\},
\qquad
a\equiv5\pmod6,
\]
because `a` and `a+2` must be the two nonzero residue classes modulo `3`. Let `M_x^+` be the set of these starts and `M_x^-:=M_x^++2` the set of corresponding endpoints. Both have cardinality `E_x`, and the matched vertex set is their disjoint union.

For a signed offset `h`, let `r_x^+(h)` be the fraction of `a in M_x^+` for which `a+h` is again primitive, with the graph-self offset `h=0` and the deleted matching partner `h=2` assigned value zero. Define `r_x^-(h)` analogously from `M_x^-`, deleting its partner at `h=-2`.

CRT gives an exact local formula. Parity forces `h` even. Modulo `3`, a start `a congruent 2` remains primitive after translation precisely when
\[
h\not\equiv1\pmod3.
\]
For every prime `p>=5`, conditioning on the pair `a,a+2` leaves `p-2` possible classes for `a`. The extra condition that `a+h` be nonzero removes one more class unless it collides with one already excluded, which happens exactly when
\[
p\mid h(h-2).
\]
Therefore, for `h notin {0,2}` represented as a signed integer modulo `N_x`,
\[
\boxed{
r_x^+(h)
=
\mathbf 1_{\{2\mid h,\ h\not\equiv1\ (3)\}}
\prod_{\substack{5\le p\le x\\p\nmid h(h-2)}}
\frac{p-3}{p-2}.
}
\tag{1}
\]
Reflection gives
\[
\boxed{r_x^-(h)=r_x^+(-h).}
\tag{2}
\]
Thus the third-vertex survival factor is exact finite CRT data; no prime-tuple conjecture is being used.

## 2. Conditioning one more primitive vertex costs exactly one Mertens factor

Put
\[
Q_x:=\prod_{5\le p\le x}\frac{p-3}{p-2}.
\tag{3}
\]
For a fixed admissible offset `h`, equation (1) becomes, once `x` exceeds all prime divisors of `h(h-2)`,
\[
r_x^+(h)
=
Q_x
\prod_{\substack{p\ge5\\p\mid h(h-2)}}
\frac{p-2}{p-3}.
\tag{4}
\]
The universal product `Q_x` is an ordinary Mertens factor times an absolutely convergent Euler correction, because
\[
\frac{(p-3)/(p-2)}{1-1/p}
=
\frac{p(p-3)}{(p-2)(p-1)}
=
1-\frac{2}{(p-2)(p-1)}.
\tag{5}
\]
Hence
\[
\boxed{
Q_x\sim\frac{\kappa}{\log x},
\qquad
\kappa
:=3e^{-\gamma}
\prod_{p\ge5}
\frac{p(p-3)}{(p-2)(p-1)}>0.
}
\tag{6}
\]
The factor `3` removes the `p=2,3` factors from the usual Mertens product.

Define the finite offset correction
\[
S(h)
:=
\prod_{\substack{p\ge5\\p\mid h(h-2)}}
\frac{p-2}{p-3}.
\tag{7}
\]
Then for every fixed `h notin {0,2}`,
\[
\boxed{
(\log x)r_x^+(h)
\longrightarrow
\kappa\,
\mathbf 1_{\{2\mid h,\ h\not\equiv1\ (3)\}}S(h).
}
\tag{8}
\]
This identifies the exact arithmetic scale hidden behind the qualitative `r_x(h)->0` statement in PC-143.

## 3. The inverse-square kernel makes the conditional singular series summable

PC-143 proves the exact trace identity
\[
T_x
=
\sum_{h\ne0}
\frac{w_h(N_x)}{N_x^2}\,r_x(h),
\qquad
w_h(N):=\frac1{4\sin^2(\pi h/N)},
\tag{9}
\]
where `r_x=(r_x^++r_x^-)/2` and offsets are taken symmetrically modulo `N_x`. Since `w_h=w_{-h}` and (2) holds, the orientation average disappears after summation:
\[
\boxed{
T_x
=
\sum_h
\frac{w_h(N_x)}{N_x^2}\,r_x^+(h),
}
\tag{10}
\]
with the self and deleted-partner terms understood to be zero.

For every fixed nonzero integer `h`,
\[
\frac{w_h(N_x)}{N_x^2}
\longrightarrow
\frac1{4\pi^2h^2}.
\tag{11}
\]
PC-143 also supplies the uniform estimate
\[
0\le\frac{w_h(N)}{N^2}
\le\frac1{16d_N(h)^2},
\tag{12}
\]
where `d_N(h)` is the symmetric cyclic distance.

The extra arithmetic factor remains summable against `1/h^2`. Indeed, for every `epsilon>0`,
\[
S(h)\ll_\epsilon |h(h-2)|^\epsilon,
\tag{13}
\]
because each local factor is `1+O(1/p)` and, after absorbing finitely many small primes into the constant, it is bounded by `p^epsilon`. Choosing `epsilon<1/2` makes `S(h)/h^2` summable. Mertens' product theorem also makes `(log x)Q_x` uniformly bounded for large `x`, so equations (4), (12), and (13) provide an `x`-independent summable majorant.

Dominated convergence may therefore be applied to (10). The exact limit is
\[
\boxed{
C_{\rm gap}
=
\frac{\kappa}{4\pi^2}
\sum_{\substack{h\in\mathbb Z\\h\equiv0,2\ (6)\\h\ne0,2}}
\frac1{h^2}
\prod_{\substack{p\ge5\\p\mid h(h-2)}}
\frac{p-2}{p-3},
}
\tag{14}
\]
and
\[
\boxed{
T_x\sim\frac{C_{\rm gap}}{\log x}.
}
\tag{15}
\]
The series in (14) is absolutely convergent by (13), and it is strictly positive; for example `h=6` already contributes a positive term. A direct numerical evaluation gives `C_gap` about `7.14 x 10^-3`, used only as a control and not in the proof.

Since
\[
\frac{\varphi(N_x)}{N_x}
\sim\frac{e^{-\gamma}}{\log x},
\]
there is also the intrinsic primorial form
\[
\boxed{
\frac{T_x}{\varphi(N_x)/N_x}
\longrightarrow e^\gamma C_{\rm gap}.
}
\tag{16}
\]
Thus the average residual coupling of the isolated matching band is asymptotically linear in the ordinary reduced-residue density.

## 4. Consequence for the isolated top-band projector

Let `Q_x^top` be the rank-`E_x` top-band spectral projection of PC-142. PC-143 derives
\[
\frac1{E_x}\|(I-Q_x^{\rm top})P_x\|_F^2
\le
\frac{\rho_{N_x}}{(\beta_{N_x}-\rho_{N_x})^2}
\frac{\operatorname{tr}(P_xR_xP_x)}{E_x},
\tag{17}
\]
where `rho_N=O(N^2)` and `beta_N-rho_N>=c_6N^2` with `c_6>0`. Combining (15) with (17) gives the quantitative refinement
\[
\boxed{
1-\frac1{E_x}\operatorname{tr}(P_xQ_x^{\rm top})
=O\!\left(\frac1{\log x}\right).
}
\tag{18}
\]
No matching lower bound follows from this argument, so (18) is deliberately only an upper rate for the projector deficit. The exact asymptotic proved here is for the compressed remainder energy `T_x`.

The mean Rayleigh correction on the canonical matching space is correspondingly
\[
\boxed{
\frac1{E_x}\operatorname{tr}(P_xL_xP_x)
=
\beta_{N_x}
+
\left(C_{\rm gap}+o(1)\right)
\frac{N_x^2}{\log x}.
}
\tag{19}
\]
PC-143's operator-norm obstruction remains untouched: sparse CRT-constructible directions still force a positive liminf for `||P_x-Q_x^top||`. Equations (18) and that obstruction sharpen the two-scale picture: density-average mismatch decays on a classical sieve scale, while worst-direction mismatch remains macroscopic.

## 5. Prior-art and RH audit

Every number-theoretic ingredient in the asymptotic scale is classical. The passage from (3) to (6) is Mertens' product theorem plus an absolutely convergent Euler factor. The local factors in (1) are finite CRT counts for a three-point reduced-residue pattern conditioned on a two-point pattern. Reduced-residue tuples are a classical sieve subject; nearby general literature already cited in PC-143 includes H. L. Montgomery and R. C. Vaughan, **On the distribution of reduced residues**, *Annals of Mathematics* 123 (1986), 311--333, DOI `10.2307/1971274`, and Farzad Aryan, **The distribution of k-tuples of reduced residues**, *Mathematika* 61 (2015), 72--88, DOI `10.1112/S0025579314000151`.

Directed searches across reduced-residue tuple distributions, conditional singular-series products, primorial Mertens factors, and weighted short-gap statistics did not expose the exact spectral statistic (14)--(19). That absence is not evidence of historical priority. No novelty is claimed for Mertens, CRT tuple counts, or singular-series corrections separately; the durable contribution is the exact rate they force for the canonical PC-142/143 Prime-Circle top-band remainder.

The result is therefore primarily a classicalization boundary. The matching eigenspace's average residual interaction is not carrying a new zeta-zero scale: it is controlled by the same `1/log x` reduced-residue thinning that appears before any analytic continuation or critical-line structure enters. There is no new spectral parameter, functional equation, gamma factor, zeta-zero divisor, or critical-line involution here.

What remains outside the result is correspondingly narrower: sparse exceptional directions from PC-143, finer internal spacing inside the isolated top band, and genuinely cross-level transport of those exceptional directions. Those require more than the density-average third-vertex statistic classified here.

## 6. Falsification surface

1. For every fixed signed offset `h`, exact CRT enumeration of oriented matched starts must agree with (1). In particular, after conditioning on `a,a+2`, every prime `p>=5` contributes `(p-3)/(p-2)` unless `p|h(h-2)`.
2. The factorization (5) must give the Mertens asymptotic (6); the residual Euler product converges absolutely because its local deviation from `1` is `O(p^-2)`.
3. Direct finite evaluation of (9) gives `T_x` approximately `0.00359616, 0.00309850, 0.00276961, 0.00252455, 0.00235876` for `N_x=30,210,2310,30030,510510` respectively. The scaled values `(log x)T_x` must approach the constant in (14), numerically about `0.00714`.
4. The exact asymptotic claim is only (15). Equation (18) is an upper bound inherited through the PC-143 Sylvester estimate and must not be promoted to `Theta(1/log x)` without a separate lower bound.
5. PC-143's positive operator-norm liminf remains compatible with (15)--(18): a vanishing fraction of exceptional directions can carry order-`N_x^2` couplings while contributing only Mertens-scale average mass.
6. Any revision of the PC-142 isolated-band count or PC-143 trace identity would require re-auditing the corresponding projector consequence, but the CRT/Mertens asymptotic for the oriented third-vertex statistic can be checked independently.
