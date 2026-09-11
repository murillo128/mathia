# WI-240 — The prime-deleted gamma-plus-pole form has unbounded odd negative index

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

WI-239 shows that Suzuki's universal logarithmic core already develops negative inertia as the support radius grows, leaving open the possibility that the *rest* of the non-prime zeta terms — the exact gamma-factor correction and the polar factor `s(s-1)` — might restore coercivity before any prime arithmetic is used. They do not.

Delete only the von Mangoldt sum from Suzuki's exact localized Fourier formula and keep the full gamma multiplier and pole term. Let `Q_arch^a` denote this prime-deleted form on `C_c^\infty(-a,a)`, and define its negative index as the supremum of dimensions of subspaces on which the form is negative definite. Then

\[
\boxed{\forall N\ge 1\ \exists A_N<\infty\ \forall a\ge A_N:\quad
n_-\!\left(Q_{\rm arch}^a\big|_{\rm odd}\right)\ge N.}
\tag{1}
\]

Hence

\[
\boxed{n_-\!\left(Q_{\rm arch}^a\big|_{\rm odd}\right)\longrightarrow\infty
\qquad(a\to\infty).}
\tag{2}
\]

This is an exact source-side obstruction. Even after restoring every non-prime term in Suzuki's Weil form, the odd sector acquires arbitrarily many negative directions. Therefore a localized-Weil route to global positivity/nondegeneracy cannot be powered by the logarithmic singularity, gamma correction, and pole factor alone. If the full zeta form is nonnegative at all radii, the von Mangoldt translation/correlation term must compensate these negative directions. No claim is made that the prime term is sign-definite; the statement is that its signed contribution is indispensable on the relevant directions.

## 1. Exact prime-deleted form

Suzuki's Fourier formula for `v\in H_0^1(-a,a)` is

\[
\begin{aligned}
Q_{B_a}(v)
={}&\frac1{2\pi}\int_{\mathbb R}
\left(\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi\right)
|\widehat v(z)|^2\,dz\\
&-\frac1{2\pi}\int_{\mathbb R}|\widehat v(z)|^2
\sum_{n\le e^{2a}}\frac{2\Lambda(n)}{\sqrt n}\cos(z\log n)\,dz\\
&-\frac1{2\pi}\int_{\mathbb R}\widehat{r_{0,a}''}(z)|\widehat v(z)|^2\,dz,
\end{aligned}
\tag{3}
\]

where

\[
r_0(t)=-4(e^{t/2}+e^{-t/2}-2),
\qquad
r_0''(t)=-(e^{t/2}+e^{-t/2}),
\tag{4}
\]

and `r_{0,a}''=r_0'' 1_{(-2a,2a)}`. This is Suzuki's exact formula, not a small-aperture expansion.

Set

\[
m(z):=\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi
\tag{5}
\]

and delete only the middle von Mangoldt term in (3):

\[
Q_{\rm arch}^a(v)
:=\frac1{2\pi}\int m(z)|\widehat v(z)|^2\,dz
-\frac1{2\pi}\int\widehat{r_{0,a}''}(z)|\widehat v(z)|^2\,dz.
\tag{6}
\]

The label `arch` here means **gamma plus pole, with the von Mangoldt source deleted**. The pole term is kept explicitly so that no positivity is being lost by silently throwing away a non-prime zeta contribution.

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), especially §§2.3--2.5 and equations (2.5)--(2.7): <https://arxiv.org/abs/2606.09096>.

## 2. The pole term is nonpositive on odd test functions

Because `v` is supported in `(-a,a)`, every difference `x-y` lies in `(-2a,2a)` up to a null boundary. Parseval therefore turns the final term in (6) exactly into

\[
P_a(v)
=\iint_{(-a,a)^2}
\left(e^{(x-y)/2}+e^{-(x-y)/2}\right)
 v(y)\overline{v(x)}\,dx\,dy.
\tag{7}
\]

Define

\[
L_\pm(v):=\int_{-a}^{a}v(x)e^{\pm x/2}\,dx.
\tag{8}
\]

Then

\[
P_a(v)=2\operatorname{Re}\bigl(L_-(v)\overline{L_+(v)}\bigr).
\tag{9}
\]

If `v` is odd, the change of variable `x\mapsto-x` gives `L_-(v)=-L_+(v)`. Hence

\[
\boxed{P_a(v)=-2|L_+(v)|^2\le0\qquad(v\ \text{odd}).}
\tag{10}
\]

Thus the complete pole contribution cannot repair a negative gamma direction in the odd sector; it only lowers the form further. This sign is the main reason to use the odd sector. It is also structurally relevant because Yoshida's odd-test positivity criterion already suffices to imply RH.

## 3. Large support freezes the gamma symbol at a negative value

The exact value at frequency zero is

\[
\begin{aligned}
m(0)
&=\psi(1/4)-\log\pi\\
&=-\gamma-\frac\pi2-3\log2-\log\pi<0.
\end{aligned}
\tag{11}
\]

Fix any finite-dimensional subspace

\[
F\subset C_c^\infty(-1,1)
\tag{12}
\]

consisting of odd functions, and put `N=dim F`. For `a\ge1`, use the unitary dilation

\[
(U_a\phi)(x)=a^{-1/2}\phi(x/a),
\qquad U_aF\subset C_c^\infty(-a,a).
\tag{13}
\]

With Suzuki's Fourier convention,

\[
\widehat{U_a\phi}(z)=a^{1/2}\widehat\phi(az).
\tag{14}
\]

Therefore the gamma part of (6) is

\[
G_a(U_a\phi)
=\frac1{2\pi}\int_{\mathbb R}m(u/a)|\widehat\phi(u)|^2\,du.
\tag{15}
\]

For every fixed pair `\phi,\psi\in F`, the associated sesquilinear matrix entry converges to `m(0)\langle\phi,\psi\rangle`. Indeed, the standard digamma asymptotic on the vertical line `\operatorname{Re}s=1/4` gives

\[
|m(t)|\le C\bigl(1+\log(2+|t|)\bigr),
\tag{16}
\]

while Fourier transforms of elements of `C_c^\infty` are Schwartz. Dominated convergence applies. Since `F` is finite dimensional, entrywise convergence is norm convergence of the compressed Hermitian forms:

\[
\boxed{U_a^*G_aU_a\big|_F\longrightarrow m(0)I_F.}
\tag{17}
\]

Because `m(0)<0`, there is `A(F)` such that for every `a\ge A(F)`,

\[
G_a(U_a\phi)<0
\qquad(0\ne\phi\in F).
\tag{18}
\]

No asymptotic eigenvalue formula is used here; only the exact multiplier (5), dilation, and finite-dimensional uniform convergence.

## 4. Arbitrarily large odd negative subspaces

Every vector in `U_aF` is odd. Combining (10) and (18), for all sufficiently large `a`,

\[
Q_{\rm arch}^a(U_a\phi)
=G_a(U_a\phi)+P_a(U_a\phi)<0
\qquad(0\ne\phi\in F).
\tag{19}
\]

So `U_aF` is an `N`-dimensional negative subspace. Since `N` was arbitrary, (1)--(2) follow.

There is also a monotonicity interpretation. The prime-deleted expression is the same global gamma-plus-pole quadratic functional restricted to nested support classes. Zero extension therefore preserves its value, so its negative index is nondecreasing with `a`. The scaling argument proves that this monotone index is unbounded.

The proof deliberately avoids asserting that (6) has any special standalone arithmetic meaning beyond being the exact non-prime part of Suzuki's decomposition. Negative index is defined at the quadratic-form level, so no separate self-adjointness theorem for the artificially prime-deleted operator is required.

## 5. Consequence for the localized-Weil program

WI-239 left two possible sources of rescue beyond the logarithmic core: the exact archimedean/polar correction and the prime-power term. Equation (2) removes the first possibility in a strong sense. The non-prime sector does not merely retain one accidental negative mode; its odd negative index diverges.

Writing the full form schematically as

\[
Q_W^a=Q_{\rm arch}^a-Q_{\rm prime}^a,
\tag{20}
\]

if `Q_W^a\ge0` on all odd vectors, then on every negative subspace supplied above the signed prime functional must satisfy

\[
-Q_{\rm prime}^a(v)\ge -Q_{\rm arch}^a(v)>0.
\tag{21}
\]

This is a necessary compensation condition, not a claim that `-Q_{\rm prime}^a` is globally positive. The useful next object is therefore not another universal coercivity estimate for the archimedean operator. It is the structured action of the finitely many shifts `\log n\le2a` on these slowly varying odd negative directions, and whether the exact von Mangoldt weights can supply the required compensation at every scale.

This changes the source-side endgame from

`first crossing + non-prime coercivity -> contradiction`

to a genuinely arithmetic question:

`growing non-prime negative subspace + von Mangoldt shift correlations -> can compensation persist for every radius?`

That is within the canonical `weil_inertia` objective because it asks whether a source-justified defect/inertia mechanism can exclude every exceptional off-critical zero rather than merely improve a density proportion.

## 6. Prior-art and novelty audit

The provenance separates cleanly.

1. **Literature-backed exact input.** Suzuki supplies the localized Weil form, the exact Fourier decomposition (3), the gamma multiplier (5), and the pole term (4). Yoshida's odd-sector positivity implication is reported and rederived in Suzuki's framework.
2. **Recent numerical context, not proof input.** Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Junghoon Shin and Minseo Kim, **A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion**, arXiv:2607.24830 (2026), numerically studies Suzuki's operator. Its "prime-free regime" is the genuine small-aperture window `2a<log 2`; it does not analyze the artificial large-`a` prime-deleted form in (6), and its numerical positivity near the first prime threshold does not conflict with (1).
3. **Mathia deduction.** The odd pole identity (10) plus the low-frequency dilation limit (17) gives the unbounded negative-index conclusion (1). Targeted searches for equivalent statements about a prime-deleted Suzuki/Weil form, an archimedean odd negative-index divergence, or a theorem that the non-prime sector alone is coercive did not locate this consequence. Search absence is not asserted as priority.

Neighboring work on finite Guinand--Weil truncations and archimedean-tail certification concerns a different cutoff/Galerkin object and does not provide or contradict (1). In particular, positivity of an omitted high-frequency archimedean *tail* is distinct from the sign of the low-frequency gamma symbol `m(0)` exploited here.

## 7. Stress tests and boundaries

- **Fourier sign:** (10) depends on the minus sign in Suzuki's third term and on `r_0''=-(e^{t/2}+e^{-t/2})`. Reversing either sign destroys the argument; both are explicit in Suzuki's formula.
- **Oddness:** the pole term is indefinite on the full space. The theorem claims divergence in the odd sector, where the factorization is exact and nonpositive.
- **Large support, not the physical prime-free window:** for the actual zeta form the prime term is absent only when `2a<log2`. The theorem intentionally deletes primes at large `a` to test whether the remaining structure can be coercive. It does not claim that the actual zeta operator ever enters a large prime-free regime.
- **No RH assumption:** (1) is a property of the explicitly defined prime-deleted form. It neither assumes nor proves RH.
- **No sign claim for primes:** the von Mangoldt term is not declared positive. Only the necessity of its compensating signed action follows conditionally from full Weil positivity.
- **Uniformity:** the passage from pointwise multiplier convergence to an `N`-dimensional negative subspace uses finite-dimensional norm convergence, not pointwise convergence over an infinite unit sphere.

A decisive audit is therefore short: verify Suzuki's signs in (3)--(4), verify the odd factorization (9)--(10), and verify the finite-dimensional dominated-convergence step (15)--(18). These three checks imply (1) directly.

## 8. Research consequence

The pure-core no-go of WI-239 can now be strengthened to a prime-necessity statement:

\[
\boxed{\text{gamma factor + pole factor alone cannot control the localized odd inertia at large support.}}
\tag{22}
\]

The live source-side question is now quantitatively sharper: on the explicit slowly varying odd subspaces `U_aF`, how large and how coherent is the von Mangoldt translation form, and can its compensation be connected to the zero-side first-crossing defect of WI-238? A failure of compensation on even one first-crossing-compatible direction would produce the desired contradiction; a universal compensation identity would instead expose the exact arithmetic mechanism still missing from the line.