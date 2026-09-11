# WI-241 — On odd tests the pole cancels the PNT main density, leaving a bounded resolvent plus prime discrepancy

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

WI-240 shows that the gamma-plus-pole part of Suzuki's localized Weil form has unbounded negative index in the odd sector, so any all-radius positivity mechanism must use the von Mangoldt translation term. A sharper decomposition shows that **the bulk prime density itself is not the missing compensation**. On odd test functions, replacing the discrete von Mangoldt measure by its Prime Number Theorem main density cancels the polar term exactly up to a bounded positive convolution operator. The resulting mean-density model still has unbounded odd negative index.

Consequently, in this source-side formulation the genuinely load-bearing arithmetic object is the **signed discrepancy of the von Mangoldt measure from density one**, tested against localized autocorrelations. In particular, if the full zeta Weil form is nonnegative on odd tests, that discrepancy must supply a uniform negative charge on every fixed finite-dimensional family of slowly varying odd dilates.

This is an exact operator identity in Suzuki's normalization. It does not assume RH and it does not assert a new form of the Prime Number Theorem.

## 1. Suzuki's exact odd-sector decomposition

For `v\in C_c^\infty(-a,a)`, extend `v` by zero to the real line and define the real autocorrelation

\[
C_v(h):=\operatorname{Re}\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx,
\qquad h\ge0.
\tag{1}
\]

Then `C_v(h)=0` for `h\ge2a`. Suzuki's exact Fourier/translation formula gives the von Mangoldt part of the localized Weil form as

\[
Q_\Lambda^a(v)
=-2\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}\,C_v(\log n).
\tag{2}
\]

The non-prime Fourier multiplier is

\[
m(z)=\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi,
\tag{3}
\]

and the factor `s(s-1)` contributes the polar term isolated in WI-240. For odd `v`, if

\[
L_\pm(v):=\int_{-a}^{a}v(x)e^{\pm x/2}\,dx,
\tag{4}
\]

then `L_-(v)=-L_+(v)` and the exact polar contribution is

\[
Q_{\rm pole}^a(v)=-2|L_+(v)|^2.
\tag{5}
\]

Thus on odd functions Suzuki's formula may be written

\[
Q_W^a(v)=Q_\gamma(v)+Q_{\rm pole}^a(v)+Q_\Lambda^a(v),
\tag{6}
\]

where

\[
Q_\gamma(v)
=\frac1{2\pi}\int_{\mathbb R}m(z)|\widehat v(z)|^2\,dz.
\tag{7}
\]

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), especially equations (2.5)--(2.7) and the exact translation formula preceding (2.5): <https://arxiv.org/abs/2606.09096>.

## 2. Replace the von Mangoldt atoms by their PNT main density

Define the continuum main-density analogue of (2) by

\[
Q_1^a(v)
:=-2\int_1^\infty x^{-1/2}C_v(\log x)\,dx.
\tag{8}
\]

Because `C_v(h)=0` for `h\ge2a`, the upper limit is effectively `e^{2a}`. With `x=e^h`,

\[
Q_1^a(v)
=-2\int_0^\infty e^{h/2}C_v(h)\,dh.
\tag{9}
\]

This is the quadratic-form replacement corresponding to the classical main term

\[
\psi(X)=\sum_{n\le X}\Lambda(n)\sim X.
\tag{10}
\]

The relevance of density one is not heuristic: the `X` main term in the explicit formula is the contribution of the pole of `\zeta(s)` at `s=1`. The next calculation shows that, in the odd localized quadratic form, this continuum source and Suzuki's explicit polar factor are algebraically paired.

## 3. Exact pole--density cancellation

Let

\[
A_v(h):=\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx.
\tag{11}
\]

Fubini gives the exact bilateral Laplace factorization

\[
\begin{aligned}
\int_{\mathbb R}e^{h/2}A_v(h)\,dh
&=\left(\int_{\mathbb R}v(u)e^{u/2}\,du\right)
  \overline{\left(\int_{\mathbb R}v(x)e^{-x/2}\,dx\right)}\\
&=L_+(v)\overline{L_-(v)}.
\end{aligned}
\tag{12}
\]

For odd `v`, `L_-=-L_+`, hence the right-hand side is `-|L_+|^2`. Also `A_v(-h)=\overline{A_v(h)}`, so taking real parts in (12) yields

\[
\int_0^\infty\left(e^{h/2}+e^{-h/2}\right)C_v(h)\,dh
=-|L_+(v)|^2.
\tag{13}
\]

Combining (5), (9), and (13) gives

\[
\boxed{
Q_{\rm pole}^a(v)+Q_1^a(v)
=2\int_0^\infty e^{-h/2}C_v(h)\,dh.
}
\tag{14}
\]

The right-hand side is the quadratic form of the positive kernel `e^{-|x-y|/2}`:

\[
\boxed{
R(v):=\iint_{\mathbb R^2}e^{-|x-y|/2}v(y)\overline{v(x)}\,dx\,dy
=Q_{\rm pole}^a(v)+Q_1^a(v).
}
\tag{15}
\]

With Suzuki's Fourier convention,

\[
R(v)
=\frac1{2\pi}\int_{\mathbb R}
\frac{|\widehat v(z)|^2}{z^2+1/4}\,dz.
\tag{16}
\]

Therefore

\[
\boxed{0\le R(v)\le4\|v\|_2^2.}
\tag{17}
\]

This is the central cancellation. The individually large continuum-prime and polar pieces do not add to a large coercive term; on odd tests they collapse exactly to a bounded positive resolvent.

## 4. The exact remaining arithmetic is the von Mangoldt discrepancy

Define

\[
\Delta_\Lambda^a(v)
:=\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}C_v(\log n)
-\int_1^{e^{2a}}x^{-1/2}C_v(\log x)\,dx.
\tag{18}
\]

Since `C_v` vanishes beyond `2a`, the cutoff is intrinsic to the test and may be omitted from either expression without changing its value. Subtracting (8) from (2) and using (15) gives the exact odd-sector identity

\[
\boxed{
Q_W^a(v)=Q_\gamma(v)+R(v)-2\Delta_\Lambda^a(v),
\qquad v\ \text{odd}.
}
\tag{19}
\]

Equivalently, the explicit pole and the **density-one** part of the prime-power source have already been accounted for by the bounded positive operator `R`; everything arithmetic beyond that main density enters through `\Delta_\Lambda^a`.

In Stieltjes notation, (18) is simply a smoothed Prime Number Theorem remainder:

\[
\Delta_\Lambda^a(v)
=\int_1^{e^{2a}}x^{-1/2}C_v(\log x)\,d\bigl(\psi(x)-x\bigr),
\tag{20}
\]

with endpoint conventions immaterial after the standard half-jump interpretation, or by reading (18) itself as the definition. Thus the source-side endgame has been reduced from an undifferentiated "prime compensation" problem to a signed PNT-discrepancy problem for a special autocorrelation family.

## 5. The density-one model still has unbounded odd negative index

Set

\[
Q_{\rm mean}^a(v):=Q_\gamma(v)+R(v).
\tag{21}
\]

By (7) and (16), this is the Fourier-multiplier form

\[
Q_{\rm mean}^a(v)
=\frac1{2\pi}\int_{\mathbb R}M(z)|\widehat v(z)|^2\,dz,
\qquad
M(z):=m(z)+\frac1{z^2+1/4}.
\tag{22}
\]

At zero frequency,

\[
\begin{aligned}
M(0)
&=\psi(1/4)-\log\pi+4\\
&=4-\gamma-\frac\pi2-3\log2-\log\pi\\
&=-1.3721834192256655\ldots<0.
\end{aligned}
\tag{23}
\]

The negativity is elementary and does not depend on the decimal: for example `\gamma>1/2`, `\pi/2>3/2`, `3\log2>2`, and `\log\pi>0` already force the sum subtracted from `4` to exceed `4`.

Now fix any finite-dimensional odd subspace

\[
F\subset C_c^\infty(-1,1)
\tag{24}
\]

and use the unitary dilation

\[
(U_a\phi)(x)=a^{-1/2}\phi(x/a).
\tag{25}
\]

Then

\[
Q_{\rm mean}^a(U_a\phi)
=\frac1{2\pi}\int_{\mathbb R}M(u/a)|\widehat\phi(u)|^2\,du.
\tag{26}
\]

The digamma multiplier has only logarithmic growth and the rational resolvent multiplier is bounded. Since Fourier transforms of elements of `F` are Schwartz, dominated convergence gives, uniformly on the unit sphere of `F`,

\[
\boxed{
U_a^*Q_{\rm mean}^aU_a\big|_F
\longrightarrow M(0)I_F.
}
\tag{27}
\]

Because `M(0)<0`, every prescribed finite-dimensional odd `F` becomes a negative subspace for sufficiently large `a`. Hence

\[
\boxed{
\forall N\ge1\ \exists A_N<\infty\ \forall a\ge A_N:\quad
n_-\!\left(Q_{\rm mean}^a\big|_{\rm odd}\right)\ge N.
}
\tag{28}
\]

So even the PNT main density, combined exactly with the pole and the complete gamma factor, does not restore odd-sector coercivity.

## 6. Necessary discrepancy charge under Weil positivity

Equation (19) makes the remaining source requirement quantitative. Suppose the actual localized Weil form is nonnegative on odd functions. For a unit vector `\phi\in F`,

\[
0\le Q_W^a(U_a\phi)
=Q_{\rm mean}^a(U_a\phi)-2\Delta_\Lambda^a(U_a\phi).
\tag{29}
\]

Therefore

\[
\Delta_\Lambda^a(U_a\phi)
\le\frac12 Q_{\rm mean}^a(U_a\phi).
\tag{30}
\]

Using (27), for every `\varepsilon>0` and every fixed finite-dimensional odd `F`, all sufficiently large `a` must satisfy uniformly on its unit sphere

\[
\boxed{
\Delta_\Lambda^a(U_a\phi)
\le\frac{M(0)+\varepsilon}{2}
=-0.6860917096\ldots+\frac\varepsilon2.
}
\tag{31}
\]

Thus positivity cannot be supplied merely by the fact that `\psi(x)\sim x`. It requires a **signed deficit relative to the density-one autocorrelation integral**, of fixed order after the exponentially large pole/main-density pieces have cancelled.

This should not be misread as an unconditional inequality for `\Delta_\Lambda`: (31) is a necessary consequence of odd Weil positivity. Its research value is to identify exactly what an arithmetic proof must establish if it tries to close the localized source-side route.

## 7. Why coarse prime bounds cannot close the route

Before (14), the polar term and the density-one prime term may each be exponentially large on slowly varying dilates. Bounding them separately by absolute values loses their exact cancellation. The same is true of a black-box operator-norm estimate for the discrete prime translation sum: it measures the total von Mangoldt mass rather than the discrepancy from its pole-induced main density.

The useful quantity is therefore not

\[
\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n},
\tag{32}
\]

but the signed functional (18), or an equivalent representation in terms of `\psi(x)-x`. Any proposed source-side coercivity argument that only inserts the Prime Number Theorem main term and then controls the remainder by a relative `o(1)` estimate is structurally too coarse: the main term has already cancelled the pole at the operator level, while the surviving target in (31) is an absolute order-one signed effect on normalized dilates.

This does **not** prove that standard PNT error bounds are formally incapable of every possible estimate of (18); special cancellation from the autocorrelation weight could still be exploited. The barrier is narrower and exact: separate size estimates for the pole and total prime mass discard the quantity that decides the sign after cancellation.

## 8. Prior-art audit and novelty boundary

The load-bearing ingredients divide as follows.

- **Literature-backed exact input:** Suzuki supplies the localized translation formula (2), the gamma multiplier (3), and the polar factor used in (5). WI-240 already audited their signs against arXiv:2606.09096.
- **Classical explicit-formula input:** the interpretation `\psi(x)=x+(\text{fluctuation})` and the fact that the `x` term corresponds to the pole at `s=1` are classical von Mangoldt/Riemann explicit-formula structure. No novelty is claimed for subtracting the Prime Number Theorem main term as an arithmetic device.
- **Mathia deduction:** equations (12)--(19) identify the exact odd-sector operator cancellation, (22)--(28) show that the resulting density-one model still has unbounded odd negative index, and (31) isolates the fixed-order signed discrepancy charge required by positivity.

A targeted prior-art search around Weil quadratic forms, `\psi(x)-x`, von Mangoldt density-one subtraction, and Suzuki's localized operator found the classical explicit-formula decomposition and Suzuki's exact form, but did not locate this specific odd autocorrelation/resolvent identity or its negative-index consequence. Search absence is not a priority claim.

## 9. Stress tests and boundaries

1. **Oddness is load-bearing.** The factorization (12) holds generally, but the cancellation (14) uses `L_-=-L_+`. The finding makes no corresponding full-space identity with the same sign.
2. **No asymptotic substitution is used in (14) or (19).** `Q_1` is a deliberately defined density-one comparison form. The difference between the actual primes and this comparison is retained exactly as `\Delta_\Lambda`.
3. **The cutoff is exact.** Because `v` is supported in `(-a,a)`, `C_v(h)=0` for `h\ge2a`; writing sums/integrals up to `e^{2a}` or to infinity is equivalent.
4. **The resolvent is positive but bounded.** It contributes at most `4\|v\|^2`, and its low-frequency value `4` is not enough to overturn the negative gamma value `m(0)`.
5. **Equation (31) is conditional on odd Weil positivity.** It is a necessary target for an RH proof through this route, not a new unconditional prime-discrepancy theorem.
6. **Normalization matters.** The constant `M(0)` and the kernel `e^{-|x-y|/2}` are tied to Suzuki's Fourier convention and the `s(s-1)` normalization of the completed zeta function.
7. **This does not improve the bulk simple-zero percentage.** It addresses the README mandate's defect-elimination endgame by sharpening which source information must prevent finite-radius degeneration.

## Consequence for the research line

WI-240 said that the prime term is indispensable. WI-241 makes that statement substantially sharper:

\[
\boxed{
\text{the mean prime density is not enough; the compensating information lives in the signed }\Lambda-1\text{ discrepancy.}
}
\tag{33}
\]

The live finite-radius problem should therefore be formulated directly in terms of the operator generated by (18), rather than by the total prime translation sum. A promising next test is to integrate (18) by parts against `\psi(x)-x` and determine whether known unconditional one-sided information, explicit-formula identities, or a first-crossing zero-mode equation constrain this autocorrelation-weighted discrepancy strongly enough to supply (31). Conversely, a barrier showing that all available PNT-error estimates are too weak after the exact pole cancellation would close another broad source-side route cleanly.