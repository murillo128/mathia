# MC-109 — Critical Hamming cumulative cancellation has a half-shell boundary law

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the exact source-forced Hamming deformation and shell coefficients of `MC-107`--`MC-108`:

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
L:=\log\log N.
\]

Let `K=K_N` be any integer sequence in the previously unresolved turning regime

\[
\alpha_N:=\frac{K-2}{2L}\longrightarrow 1.
\tag{1}
\]

Then the alternating prefix through `K` obeys the same boundary law as the fixed subcritical and supercritical regimes, now uniformly through the critical scale:

\[
\boxed{
\sum_{k=0}^{K}(-1)^k C_{k,N}
\sim
(-1)^K\frac{C_{K,N}}{1+\alpha_N}
\sim
(-1)^K\frac{C_{K,N}}2.
}
\tag{2}
\]

The exact endpoint remains super-logarithmically smaller,

\[
\mathcal Q_N(1)
=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\qquad(A>0\text{ fixed}),
\tag{3}
\]

whereas `MC-107` gives, under `(1)`,

\[
C_{K,N}=N^2(\log N)^{o(1)}
\tag{4}
\]

with the harmless central `1/\sqrt{\log\log N}` factor absorbed in `(\log N)^{o(1)}`. Hence `(3)=o(C_{K,N})`, and the omitted tail is forced to cancel the prefix at the same scale:

\[
\boxed{
\sum_{k>K}(-1)^k C_{k,N}
\sim
-(-1)^K\frac{C_{K,N}}{1+\alpha_N}
\sim
-(-1)^K\frac{C_{K,N}}2.
}
\tag{5}
\]

In the Gaussian central window

\[
\frac{K-2-2L}{\sqrt{2L}}\longrightarrow y\in\mathbb R,
\tag{6}
\]

Stirling's formula and `\mathcal A(1)=36/\pi^4` from `MC-107` sharpen this to

\[
C_{K,N}
\sim
\frac{36J}{\pi^4\sqrt{4\pi L}}
 e^{-y^2/2}N^2,
\qquad
J=\gamma+\gamma_1-\frac12>0,
\tag{7}
\]

and therefore

\[
\sum_{k=0}^{K}(-1)^k C_{k,N}
\sim
(-1)^K
\frac{18J}{\pi^4\sqrt{4\pi L}}
 e^{-y^2/2}N^2.
\tag{8}
\]

Thus the turning point does **not** create a narrow radial escape where the endpoint suddenly becomes visible. Even when adjacent positive shells have comparable size, the alternating cumulative sum is still asymptotically a fixed fraction of the boundary shell. The super-logarithmic endpoint saving must come from cancellation extending beyond every cutoff with `(K-2)/(2\log\log N)\to1`, or from a genuinely non-radial relation.

This result does not estimate `M(N)`, does not improve `(3)`, and does not identify the non-radial/source-specific relation that would explain the endpoint.

## 1. Alternating truncation is an exact coefficient transform

For fixed square-free `b`, put `x=N/b` and, as in `MC-107`, write

\[
m=bd,\qquad n=be,
\]

with `b,d,e` pairwise coprime and square-free. For `0<r,s\le1`, define the total-degree generating polynomial

\[
F_{b,x}^{r,s}(z)
:=
\sum_{\substack{d\le rx,\ e\le sx\\d,e\text{ square-free}\\(d,e)=1,\ (de,b)=1}}
 z^{\omega(d)+\omega(e)}.
\tag{9}
\]

If

\[
F_{b,x}^{r,s}(z)=\sum_{j\ge0}a_j z^j,
\]

then the signed cumulative count has the exact formal-series identity

\[
\sum_{j\le K}(-1)^j a_j
=
(-1)^K[z^K]\frac{F_{b,x}^{r,s}(z)}{1+z}.
\tag{10}
\]

There is one subtlety precisely at the critical saddle `|z|\simeq1`: the rational function in `(10)` has a possible pole at `z=-1`. Remove it exactly by writing

\[
\widetilde F_{b,x}^{r,s}(z)
:=
\frac{F_{b,x}^{r,s}(z)-F_{b,x}^{r,s}(-1)}{1+z},
\tag{11}
\]

which is a polynomial. Then

\[
\sum_{j\le K}(-1)^j a_j
=
F_{b,x}^{r,s}(-1)
+(-1)^K[z^K]\widetilde F_{b,x}^{r,s}(z).
\tag{12}
\]

The first term is an unconditional prime-number-theorem-scale remainder, not a new critical contribution. Indeed on square-free support `(-1)^{\omega(n)}=\mu(n)`, and the same finite-prime-exclusion specialization of the Landau--Selberg--Delange theorem used below gives, for every fixed `A`,

\[
F_{b,x}^{r,s}(-1)
\ll_A \frac{x^2}{(\log x)^A}
\tag{13}
\]

uniformly for the polylogarithmic `b`, `r`, and `s` ranges used later. This is the standard negative-integer phenomenon: the Landau--Selberg--Delange main coefficients vanish because the reciprocal gamma factor vanishes. No RH-scale zero-free region is being assumed.

## 2. Coprimality inversion gives a one-variable complex-parameter model

For square-free `c`, set

\[
B_z^{(c)}(X)
:=
\sum_{\substack{n\le X\\n\text{ square-free}\\(n,c)=1}}
 z^{\omega(n)}.
\tag{14}
\]

Exactly as in the accepted coprimality-inversion repair persisted in `MC-107`, Möbius inversion of `(d,e)=1` gives

\[
F_{b,x}^{r,s}(z)
=
\sum_{\substack{q\ge1\\q\text{ square-free}\\(q,b)=1}}
\mu(q)z^{2\omega(q)}
B_z^{(bq)}(rx/q)
B_z^{(bq)}(sx/q).
\tag{15}
\]

Koukoulopoulos's Landau--Selberg--Delange theorem, specialized to the multiplicative function

\[
1_{(n,c)=1}\mu(n)^2z^{\omega(n)},
\]

gives on every fixed complex `z`-compact

\[
B_z^{(c)}(X)
=
X(\log X)^{z-1}\frac{G_c(z)}{\Gamma(z)}
+O\!\left(X(\log X)^{\Re z-2}\right),
\tag{16}
\]

with the finite-prime exclusion factor

\[
G_c(z)=G(z)\prod_{p\mid c}(1+z/p)^{-1}.
\tag{17}
\]

For `c` of fixed polylogarithmic size the derivatives of the finite Euler correction contribute only powers of `\log\log N`; these are negligible compared with the full `1/\log N` saving in `(16)`. Truncating the `q`-sum at a fixed small power of `\log N` is also harmless: the normalized tail is dominated by the convergent majorant `C^{\omega(q)}/q^2` already used in `MC-107`, while the far `q` range has the same crude `O(x^{3/2+o(1)})` bound.

Consequently, uniformly for `z` in a fixed neighborhood of the unit saddle circle and for `r,s` down to a sufficiently small fixed negative power of `\log N`, `(15)` has the form

\[
F_{b,x}^{r,s}(z)
=
rs\frac{x^2}{(\log x)^2}
 e^{\lambda_x z}
 z^2 A_b(z)
+E_{b,x}^{r,s}(z),
\qquad
\lambda_x:=2\log\log x,
\tag{18}
\]

where

\[
A_b(z)
:=
\frac{H_b(1,1;z,z)}{\Gamma(1+z)^2}
\tag{19}
\]

is the same analytic arithmetic factor that underlies the proportional shell law in `MC-107`, and the error in `(18)` has at least one fixed extra power of `1/\log N` compared with the leading family, up to powers of `\log\log N`.

This is not a new multivariable Selberg--Delange invocation. Equation `(15)` reduces the needed complex-parameter rectangle estimate to a summable superposition of the same one-variable theorem used in the repaired `MC-107` argument.

## 3. The apparent pole at `-1` is killed by the gamma zero

The main term in `(18)` can be divided by `1+z` without introducing a critical singularity. Since

\[
\frac1{\Gamma(1+z)^2}
\]

has a zero of order two at `z=-1`, the function

\[
\boxed{
\frac{A_b(z)}{1+z}
=
\frac{H_b(1,1;z,z)}{(1+z)\Gamma(1+z)^2}
}
\tag{20}
\]

is analytic there (indeed it still has at least a simple zero). Thus the pole in the elementary cumulative kernel `1/(1+z)` is absent from the Landau--Selberg--Delange main family. The only pole residue of the exact finite polynomial is the genuine arithmetic remainder `(13)`, already super-logarithmically small.

This cancellation is the technical reason the saddle argument survives exactly as `\alpha_N\to1` from either side. It is not legitimate simply to insert `1/(1+z)` into a Cauchy integral and ignore `z=-1`; the subtraction `(11)` and the gamma zero `(20)` are both required.

## 4. The Sathe--Selberg saddle multiplies the critical coefficient by `1/(1+alpha)`

The proof of Koukoulopoulos's Theorem 16.2 gives the quantitative Sathe--Selberg coefficient extraction directly from a complex-parameter Landau--Selberg--Delange expansion. In his notation, for `k\le C\log\log x` the relative error is

\[
1+O_C\!\left(\frac{k}{(\log\log x)^2}\right),
\tag{21}
\]

and the saddle is the positive real point `k/\log\log x`. The same Cauchy calculation applies to any analytic multiplier with bounded derivatives on the relevant compact set.

Apply that calculation to the two analytic multipliers in `(18)`:

\[
z^2A_b(z)
\qquad\text{and}\qquad
z^2\frac{A_b(z)}{1+z}.
\]

With

\[
n:=K-2,
\qquad
\alpha_{b,N}:=\frac{n}{\lambda_x},
\]

and `\alpha_{b,N}\to1`, the leading exact-degree rectangle coefficient is

\[
[z^K]\,e^{\lambda_x z}z^2A_b(z)
\sim
A_b(\alpha_{b,N})
\frac{\lambda_x^n}{n!},
\tag{22}
\]

whereas the cumulative coefficient is

\[
[z^K]\,e^{\lambda_x z}z^2\frac{A_b(z)}{1+z}
\sim
\frac{A_b(\alpha_{b,N})}{1+\alpha_{b,N}}
\frac{\lambda_x^n}{n!}.
\tag{23}
\]

Thus the signed cumulative rectangle count is asymptotically `(-1)^K/(1+\alpha_{b,N})` times its degree-`K` boundary mass. For `b` below any fixed power of `\log N`,

\[
\lambda_x=2\log\log(N/b)=2L+o(1),
\]

so `\alpha_{b,N}=\alpha_N+o(1)` uniformly in the retained `b` range.

The error terms from `(18)` are much smaller than the critical coefficient scale. Under `(1)`, `MC-107` gives a shell of size `N^2(\log N)^{-o(1)}`; every fixed extra factor `1/\log N` therefore beats the whole `\alpha_N\to1` regime, not merely the Gaussian subwindow.

## 5. The sawtooth kernel and common-factor sum preserve the same ratio

It remains to pass from rectangle counts to the actual source kernel

\[
f(u,v)=z\!\left(\frac1{uv}\right).
\tag{24}
\]

The argument is the quantitative version of the one already used in `MC-107`. Choose a small fixed `eta>0` and discard the coordinate strips `u<(\log N)^{-\eta}` or `v<(\log N)^{-\eta}`. Their absolute pair mass is `O(N^2/(\log N)^\eta)`, which is `o(C_{K,N})` under `(1)`. On the remaining square, the discontinuity hyperbolas `uv=1/q` have only polynomial-in-`\log N` combinatorial complexity. The rectangle error inherited from `(18)` carries a full fixed power of `1/\log N`, so a sufficiently fine polylogarithmic partition still leaves `o(C_{K,N})` total error. The limiting integral is therefore the same

\[
J=\int_0^1\!\int_0^1 z\!\left(\frac1{uv}\right)du\,dv
=\gamma+\gamma_1-\frac12.
\tag{25}
\]

Likewise truncate the common factor at `b\le(\log N)^\eta`. The omitted absolute pair mass is

\[
\ll N^2\sum_{b>(\log N)^\eta}\frac1{b^2}
\ll \frac{N^2}{(\log N)^\eta}
=o(C_{K,N}).
\tag{26}
\]

For the retained `b`, `(23)` is uniform. Summing the same Euler factors as in `MC-107` therefore gives

\[
\sum_{k=0}^{K}(-1)^k C_{k,N}
\sim
(-1)^K
J\,\frac{\mathcal A(\alpha_N)}{1+\alpha_N}
\frac{N^2}{(\log N)^2}
\frac{(2L)^{K-2}}{(K-2)!}.
\tag{27}
\]

Comparing `(27)` with the proportional shell formula of `MC-107` proves `(2)`. Equation `(5)` follows by subtracting `(27)` from the exact endpoint `(3)`.

## Prior art and novelty boundary

The analytic ingredients are classical. Dimitris Koukoulopoulos, *The Distribution of Prime Numbers*, Graduate Studies in Mathematics 203, AMS (2019), Theorem 16.2, gives the Sathe--Selberg coefficient asymptotic uniformly for `k\le C\log\log x` with the explicit relative error `O_C(k/(\log\log x)^2)`; its proof is precisely the Cauchy saddle calculation used in `(22)`--`(23)`. The author's preliminary version is available at `https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf`. Chapter 13 supplies the Landau--Selberg--Delange expansion used in `(16)`, including the negative-integer gamma-zero mechanism behind `(13)`.

Modern mod-Poisson formulations of Selberg--Delange, for example Maximilian Janisch, *Probabilistic interpretation of the Selberg--Delange Method in analytic number theory*, arXiv:2501.17535 (2025), provide adjacent language for precise prime-factor large deviations. They do not supply the present source-specific coprime-pair sawtooth kernel or the Hamming cumulative identity.

A targeted search for Sathe--Selberg parity truncations, alternating cumulative prime-factor counts, `(-1)^{\omega}` cutoffs, and mod-Poisson parity tails did not identify `(2)` or `(27)` as a standard named result. The transform `(10)`, the saddle method, and the gamma-zero cancellation are classical mechanisms. **No novelty claim is made.** The durable delta is their exact application to the already-derived Möbius Hamming source: the previously open `\alpha_N\to1` radial regime obeys a boundary-shell obstruction rather than an endpoint-scale collapse.

## Boundaries and falsification tests

- The result concerns direct **radial cumulative truncation** of the exact Hamming deformation. It does not rule out non-radial, cross-shell, or source-coupled identities that use information lost by the degree projection.
- The subtraction `(11)` is essential. Any derivation that moves a Cauchy contour through `|z|=1` while ignoring the exact `z=-1` residue is incomplete.
- The smallness of `(13)` is unconditional prime-number-theorem-scale information. Replacing it by an RH-strength Mertens estimate would be circular and is unnecessary here.
- The complex-parameter estimate `(18)` must retain the finite-prime exclusion and coprimality Euler factors. Dropping them changes the arithmetic constant, exactly as the adversarial repair of `MC-107` established.
- The polylogarithmic axis, partition, `q`, and `b` truncations are justified only because `\alpha_N\to1` leaves the boundary shell at `N^2(\log N)^{-o(1)}` scale. This finding does not claim the same quantitative argument uniformly for arbitrary fixed `\alpha` far from `1`; those regimes are already handled separately by `MC-107` and `MC-108`.
- Equation `(8)` requires the bounded Gaussian scaling `(6)`. The general half-shell law `(2)` requires only `(1)`.
- The endpoint `(3)` remains an externally known unconditional estimate for this exact deformation, not a new consequence of the saddle calculation. No improved bound for the Mertens function follows.

## Consequence for the research line

`MC-107` showed a last-shell-sized cancellation debt for every fixed proportional cutoff below the `2\log\log N` peak, and `MC-108` showed the analogous law for every fixed proportional cutoff above it. The only radial ambiguity left between those results was a moving cutoff with proportional parameter tending to `1`.

That ambiguity is now removed. The entire critical regime `(K-2)/(2\log\log N)\to1` still carries a boundary-shell-sized signed prefix, asymptotically one half of `C_K` at the peak. A purely radial explanation of the hard endpoint therefore cannot be obtained by tuning the truncation to the Sathe--Selberg turning scale. The surviving question is sharper: find a genuinely non-radial/source-specific relation, or a global signed coupling across the full Hamming degree range, whose cancellation is not reducible to direct radial truncation.