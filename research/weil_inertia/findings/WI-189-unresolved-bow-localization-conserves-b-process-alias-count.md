# WI-189 — unresolved bow localization conserves aggregate B-process alias count

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding sharpens the stationary-phase obstruction isolated in WI-188 and is deliberately narrower than a bound for the twisted prime covariance itself. It proves that, throughout the local-bow regime in which the classical mean-value theorem is still below arithmetic resolution, shortening the prime-side length cannot make the height chirp globally nonstationary: the number of Poisson/van-der-Corput `B`-process stationary lattice frequencies, summed over the full local shift range, has an asymptotic main term proportional to `U/H^2` in which the Dirichlet length cancels exactly. At a Maynard--Pratt bow of height `H \asymp T^epsilon/log T`, this is polynomially large, `asymp T^(1-2epsilon) log^2 T`, independently of the reciprocal exponent `alpha` at power scale. Thus changing the fixed bow spacing `c` can redistribute stationary aliases between fewer shifts and more aliases per shift, but cannot remove their aggregate power-scale burden before one crosses WI-187's separate mean-value resolution gate.

No cancellation lower bound is asserted: many stationary frequencies can still cancel after arithmetic transforms, and the von-Mangoldt weights may supply additional structure. The conclusion is a route barrier only against the naive escape "shorten `x` until the height chirp becomes uniformly nonstationary".

## 1. The phase and its exact derivative image

Use the source-level local second-moment expansion from WI-188. On a central dyadic prime block `m \in [X,2X]`, the shift-`h` phase in cycles is

\[
f_h(m):=\frac{U}{2\pi}\log\!\left(1+\frac{h}{m}\right),
\qquad U\asymp T,
\tag{1}
\]

with the localizer coupling shifts on the natural scale `h \lesssim X/H`. Its first two derivatives are

\[
f_h'(m)=-\frac{Uh}{2\pi m(m+h)},
\tag{2}
\]

and

\[
f_h''(m)=\frac{Uh(2m+h)}{2\pi m^2(m+h)^2}>0.
\tag{3}
\]

Hence `f_h'` is strictly increasing on `[X,2X]`. Define `nu_h` to be the number of integer derivative levels crossed by this interval, equivalently the number of integers `k` for which there is an `m_k \in (X,2X)` satisfying

\[
f_h'(m_k)=-k.
\tag{4}
\]

These are precisely the stationary frequencies that appear when a one-dimensional Poisson / van-der-Corput `B` process is applied to the smooth phase. Since the number of integers in a real interval differs from its length by `O(1)`, uniformly in `h`,

\[
\nu_h=\Delta_h+O(1),
\tag{5}
\]

where

\[
\begin{aligned}
\Delta_h
&:=|f_h'(X)|-|f_h'(2X)|\\
&=\frac{Uh}{2\pi X^2}
\left(\frac1{1+u}-\frac1{2(2+u)}\right),
\qquad u:=\frac hX\\
&=\frac{Uh}{4\pi X^2}\frac{3+u}{(1+u)(2+u)}.
\end{aligned}
\tag{6}
\]

This is exact. In particular, whenever `h/X=o(1)` uniformly over the shift range,

\[
\boxed{
\Delta_h
=\left(\frac{3}{8\pi}+o(1)\right)\frac{Uh}{X^2}.
}
\tag{7}
\]

The correction to WI-188's original Section 4 is visible here: the per-shift scale is not generally `Theta(h)` at count saturation. It is controlled by

\[
\rho_T h,
\qquad
\rho_T:=\frac{U}{X^2},
\tag{8}
\]

and `rho_T` need only be `T^{o(1)}` when `X=T^{1/2+o(1)}`.

## 2. Summing the full local shift range removes the unknown reciprocal scale

Fix a constant `kappa>0` and put

\[
K_\kappa:=\left\lfloor\kappa\frac{X}{H}\right\rfloor.
\tag{9}
\]

For a standard localizer with `\widehat W(0)\ne0`, continuity gives a fixed neighborhood of zero on which the Fourier weight is nonzero; choosing `kappa` sufficiently small places `1\le h\le K_\kappa` inside that genuinely coupled central shift range. The counting identity below is geometric and does not require any sign assumption on those weights.

Assume

\[
H\to\infty,
\qquad
\frac{X}{H}\to\infty,
\qquad
\frac{U}{HX}\to\infty.
\tag{10}
\]

Then `h/X <= kappa/H=o(1)` uniformly for `h<=K_kappa`, so (7) is uniform. Summing (5)--(7) gives

\[
\begin{aligned}
\sum_{h\le K_\kappa}\nu_h
&=\left(\frac{3}{8\pi}+o(1)\right)
\frac{U}{X^2}\sum_{h\le K_\kappa}h
+O(K_\kappa)\\
&=\left(\frac{3}{16\pi}+o(1)\right)
\frac{U}{X^2}K_\kappa^2
+O(K_\kappa).
\end{aligned}
\tag{11}
\]

The last error is negligible relative to the main term precisely because

\[
\frac{(U/X^2)K_\kappa^2}{K_\kappa}
\asymp\frac{U}{HX}\to\infty.
\tag{12}
\]

Using `K_kappa=(kappa+o(1))X/H`, the prime-side length cancels **exactly at main-term scale**:

\[
\boxed{
\sum_{h\le K_\kappa}\nu_h
=\left(\frac{3\kappa^2}{16\pi}+o(1)\right)
\frac{U}{H^2}.
}
\tag{13}
\]

This is the structural point. Replacing `X` by a shorter length decreases the number of active shifts linearly, `K\asymp X/H`, but increases the derivative sweep at a given shift quadratically through `rho_T=U/X^2`; after summing the linear-in-`h` sweeps, the two effects cancel.

The same computation gives a stronger distributional statement than a bare total count. For every fixed `0<a<b<=kappa`, uniformly for

\[
a\frac XH\le h\le b\frac XH,
\tag{14}
\]

one has

\[
\Delta_h\asymp\frac{U}{HX},
\tag{15}
\]

so whenever `U/(HX)->infinity`, a positive proportion of the relevant shifts individually cross an unbounded number of integer derivative levels. The aggregate asymptotic in (13) is therefore not generated by a vanishingly small exceptional set of shifts.

## 3. Specialization to source-compatible Maynard--Pratt bows

For the bow family in WI-184--WI-188, let the right-half population be `T^epsilon`, with fixed `0<epsilon<1/2`, ordinate spacing `c/log T`, and reciprocal prime-side exponent

\[
\alpha=\frac{2\pi}{c},
\qquad
X=T^\alpha.
\tag{16}
\]

The bow height is

\[
H=\left(c+o(1)\right)\frac{T^\epsilon}{\log T}.
\tag{17}
\]

Source compatibility gives `alpha<=1/2+o(1)` through WI-184. Consider exactly the side of WI-187's dichotomy on which the classical localized mean-value theorem is **not** yet asymptotic, namely

\[
\epsilon\le\alpha
\tag{18}
\]

at exponent level. Then

\[
\frac XH
= T^{\alpha-\epsilon+o(1)}\log T\to\infty,
\tag{19}
\]

including the boundary `epsilon=alpha`, and

\[
\frac{U}{HX}
=T^{1-\epsilon-\alpha+o(1)}\log T\to\infty.
\tag{20}
\]

Indeed `epsilon<=alpha<=1/2` implies `1-epsilon-alpha>=1-2alpha>=0`, and the only possible exponent-zero endpoint would require `epsilon=alpha=1/2`, excluded by the fixed `epsilon<1/2` bow regime. Thus all hypotheses of (13) hold throughout the unresolved source-compatible regime.

Substituting (17) into (13) gives

\[
\boxed{
\sum_{h\le K_\kappa}\nu_h
\asymp
T^{1-2\epsilon}(\log T)^2,
}
\tag{21}
\]

with an explicit leading factor `(3 kappa^2/(16 pi)+o(1)) U/H^2`. For fixed `c`, changing `c` changes only the constant through `H`; it does **not** improve the power of `T`. Equivalently, changing the reciprocal exponent `alpha=2pi/c` while remaining on the unresolved side of (18) merely redistributes a polynomial stationary-frequency budget between the number of shifts and the number of aliases per shift.

At count saturation, WI-184 supplies only

\[
c=4\pi+o(1),
\qquad
\alpha=\frac12+o(1),
\tag{22}
\]

with no rate strong enough to assert `X=sqrt(T)(1+o(1))`. Formula (13) is specifically robust to that missing rate: `X` has disappeared. Therefore the adversarial scale objection to WI-188 invalidates its original `Theta(h)` **per-shift** wording, but does not remove the aggregate stationary-lattice obstruction. At the count-saturating bow, for every fixed `epsilon<1/2`,

\[
\boxed{
\sum_{h\le K_\kappa}\nu_h
= T^{1-2\epsilon+o(1)}(\log T)^2,
}
\tag{23}
\]

up to the fixed geometric constant coming from `U/T`, `c`, and `kappa`.

## 4. Combined with WI-187, fixed-spacing retuning has no free chirp escape

WI-187 established the black-box local mean-value gate

\[
\epsilon>\alpha=\frac{2\pi}{c}.
\tag{24}
\]

If (24) fails, (21) shows that shortening the prime-side length by taking a different fixed source-compatible spacing does not make the full local shift family nonstationary: a polynomial aggregate of stationary lattice frequencies survives. If (24) holds, the classical mean-value theorem becomes arithmetically resolved, but WI-187's Riemann--von Mangoldt bookkeeping then forces the selected mirror-closed bow to occupy less than `2epsilon+o(1)` of the local zero count and leaves more than `1-2epsilon-o(1)` as an excess count reservoir.

Thus fixed-`c` retuning has a sharper two-sided constraint:

\[
\boxed{
\begin{array}{ll}
\epsilon\le\alpha:&
\text{the local prime covariance remains below black-box resolution and carries }\asymp U/H^2\text{ stationary aliases};\\[1mm]
\epsilon>\alpha:&
\text{black-box resolution is bought only after a positive/large complementary zero-count reservoir appears.}
\end{array}}
\tag{25}
\]

This does not combine the two alternatives into an RH proof; the reservoir in the second line can contain multiplicity, critical-line zeros, other off-line pairs, or a mixture. It does close a weaker proposed escape from WI-188: **one cannot remove the stationary-lattice obstruction merely by shortening the reciprocal prime length while staying in the unresolved bow regime.**

## 5. Prior-art audit and evidence boundary

The analytic mechanism behind (4)--(7) is classical. The van-der-Corput `B` process / truncated Poisson formula transforms a smooth exponential sum into a dual sum over integer frequencies lying in the image of the phase derivative, with one stationary point for each such frequency under monotonicity/curvature hypotheses. Standard sources include S. W. Graham and G. Kolesnik, *Van der Corput's Method of Exponential Sums*, Cambridge University Press, 1991. A recent explicit formulation is Natasha Dhiman, Habiba Kadiri and Emily Quesada-Herrera, **Explicit Exponential Sum Estimates and Approximate Functional Equations for the Zeta Function**, arXiv:2609.00537v1 (1 Sep 2026), which develops an explicit truncated-Poisson `B` process for zeta applications. No new B-process theorem is claimed here.

The phase family itself has close established neighbors in moment problems. Berke Topacogullari, **The fourth moment of individual Dirichlet L-functions on the critical line**, *Mathematische Zeitschrift* 298 (2021), 577--624, DOI `10.1007/s00209-020-02610-9`, reduces a load-bearing shifted convolution to sums containing an oscillatory factor `e(alpha h/n)` over `n` and `h`. That is the first-order local model of `e((U/2pi) log(1+h/m))`; Topacogullari's coefficients and theorem surface are different and are not imported as a bound for the present von-Mangoldt covariance. Conrey--Keating's shifted-convolution work, already audited in WI-188, is another neighboring architecture.

A targeted search for the exact aggregate cancellation (13) in this bow/local-form-factor setting did not locate it. This is **not** evidence of priority. The durable new Mathia delta is the elementary but load-bearing synthesis of the exact WI-188 phase with the full localized shift range and the WI-187 resolution gate, yielding the `U/H^2` cancellation of the prime-side length.

The finding deliberately makes no inference from the *number* of stationary frequencies to the size or sign of the weighted shifted-prime covariance. Such an inference would be false without additional arithmetic information. Vaughan/Heath-Brown decompositions, a Poisson/Kuznetsov/delta-method transform, cancellation among dual stationary terms, or cancellation across `h` can all evade a crude alias count. The result also assumes a fixed-scale localizer and the Maynard--Pratt fixed-`epsilon` local-height regime; a `T`-dependent localizer/support shrinkage would have to pay its own uncertainty/localization cost and is not ruled out here.

## 6. Research consequence

WI-188's surviving source-specific target should now be stated in a rate-robust form. The count-saturating bow does not give `Theta(h)` stationary aliases for each shift without extra control on how fast `c->4pi`. Instead, the exact per-shift scale is `(U/X^2)h`, while the **aggregate** over the natural local shift family is asymptotically `(3 kappa^2/(16pi))U/H^2` and therefore remains polynomially large at every fixed `epsilon<1/2`.

The next viable arithmetic move is consequently not another choice of the fixed bow spacing or reciprocal prime length. It must exploit cancellation *inside* the B-process dual family or across shifts, use the special von-Mangoldt coefficients through a source-specific bilinear/spectral theorem, or couple the selected bow to the compulsory excess reservoir with an independently controlled signed invariant. That keeps the research objective aligned with the canonical mandate: the obstruction is being pushed back toward a genuinely source-controlled defect-elimination mechanism rather than another percentage-only optimization.