# WI-426 — Positive multiscale Kunik line energy is either cubically blind or singular

**Status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

**Parents:** [WI-424](./WI-424-kunik-boundary-flux-is-a-poisson-defect-counter.md), [WI-425](./WI-425-fixed-safe-lines-are-cubically-blind-to-shallow-boundary-flux.md), [WI-410](./WI-410-carleman-summation-removes-bsy-height-decay-only-by-giving-up-finite-source-budget.md).

## Claim

WI-425 leaves open whether replacing one or finitely many fixed interior lines by a positive continuum of lines can recover the reciprocal-depth Kunik boundary charge. For the natural diagonal `L^2` multiscale energy, there is an exact dichotomy: **as long as all sampled lines stay a fixed positive distance from the critical boundary, every finite one-zero budget remains cubically blind to a shallow defect; if the continuum is instead allowed to sweep with positive density through every possible defect depth, its `L^2` energy is already infinite as soon as one off-critical zero exists.**

For one right-half zero

\[
\rho=\frac12+d+i\gamma,
\qquad 0<d<\frac12,
\]

write

\[
g_{a;d,\gamma}(t)
:=\frac{B_\rho'}{B_\rho}\!\left(\frac12+a+it\right)
=\frac1{a-d+i(t-\gamma)}-\frac1{a+d+i(t-\gamma)}.
\tag{1}
\]

For every `a>0`, `a\ne d`, the line energy is exactly

\[
\boxed{
\|g_{a;d,\gamma}\|_2^2
=
\frac{4\pi d^2}
{|a-d|(a+d)(|a-d|+a+d)}
=
\begin{cases}
\displaystyle \frac{2\pi d}{d^2-a^2},&0<a<d,\\[2mm]
\displaystyle \frac{2\pi d^2}{a(a^2-d^2)},&a>d.
\end{cases}
}
\tag{2}
\]

The boundary limit `a=0` is the WI-424 tariff

\[
\|g_{0;d,\gamma}\|_2^2=\frac{2\pi}{d}.
\tag{3}
\]

Now fix a genuinely safe displacement `a_0>0`, let `\mu` be any positive Borel measure supported on `[a_0,\infty)`, and restrict to `0<d<a_0`. Define

\[
Q_\mu(d)
:=\int_{[a_0,\infty)}
\|g_{a;d,\gamma}\|_2^2\,d\mu(a),
\qquad
M_3(\mu):=\int_{[a_0,\infty)}a^{-3}\,d\mu(a).
\tag{4}
\]

Then

\[
\boxed{
Q_\mu(d)
=2\pi d^2
\int_{[a_0,\infty)}
\frac{a^{-3}}
{1-d^2/a^2}\,d\mu(a).
}
\tag{5}
\]

Hence there are only two possibilities.

If `M_3(\mu)<\infty`, then

\[
2\pi d^2M_3(\mu)
\le Q_\mu(d)
\le
\frac{2\pi d^2M_3(\mu)}{1-d^2/a_0^2},
\tag{6}
\]

so

\[
\boxed{
Q_\mu(d)\sim 2\pi M_3(\mu)d^2
\qquad(d\downarrow0).
}
\tag{7}
\]

In particular,

\[
\frac{\|g_{0;d,\gamma}\|_2^2}{Q_\mu(d)}
\ge
\frac{1-d^2/a_0^2}{M_3(\mu)d^3}
\longrightarrow\infty.
\tag{8}
\]

Thus **no positive weighted continuum of safe-line `L^2` energies which is finite on a one-zero factor can dominate the reciprocal-depth boundary energy uniformly in `d`**. Finite collections, countable weighted collections and ordinary integrals over every Euler-product-safe line are all special cases.

If instead `M_3(\mu)=\infty`, equation (5) gives

\[
\boxed{Q_\mu(d)=\infty\quad\text{for every }0<d<a_0.}
\tag{9}
\]

So making the safe-line weight large enough to escape the cubic loss does not create a stronger finite arithmetic budget: it makes the proposed energy infinite already for a single defect.

There is a complementary singularity if one lets the line continuum enter the possible zero region. From (2), as `a\to d` from either side,

\[
\boxed{
\|g_{a;d,\gamma}\|_2^2
\sim\frac{\pi}{|a-d|}.
}
\tag{10}
\]

Consequently, if `w(a)` is locally bounded below by a positive constant near `d`,

\[
\int w(a)\|g_{a;d,\gamma}\|_2^2\,da=\infty.
\tag{11}
\]

For Kunik's full Blaschke product the same conclusion is local and cannot be removed by cancellation: at a zero of multiplicity `m`,

\[
\frac{B'}B(z)=\frac{m}{z-\rho}+H(z)
\tag{12}
\]

with `H` holomorphic near `\rho`, so `|B'/B|^2` has the nonintegrable planar singularity `m^2/|z-\rho|^2`. Therefore, for any continuous weight `w>0` on `(0,1/2)`, the improper strip energy

\[
\mathcal A_w(B)
:=
\int_0^{1/2}w(a)
\int_{\mathbb R}
\left|
\frac{B'}B\!\left(\frac12+a+it\right)
\right|^2dt\,da
\tag{13}
\]

satisfies

\[
\boxed{
\mathcal A_w(B)<\infty
\quad\Longleftrightarrow\quad
B\equiv1
\quad\Longleftrightarrow\quad
\text{RH}.
}
\tag{14}
\]

The last equivalence uses Kunik's factorization, where `B` contains precisely the zeta zeros with `Re rho>1/2`; the functional equation supplies a right-half partner for every off-critical zero. Equation (14) is an exact criterion but not a new route to RH: the perfect coercivity comes from integrating the logarithmic derivative through its unknown poles. An independent proof that (13) is finite would already have excluded the defect it is supposed to detect.

This closes the most direct positive-diagonal multiscale repair of WI-425. A useful Kunik bridge cannot be obtained merely by replacing finitely many safe vertical-line norms with a positive weighted continuum of the same norms.

## 1. Exact line-energy calculation

Put `u=t-\gamma`. From (1),

\[
|g_{a;d,\gamma}(t)|^2
=
\frac{4d^2}
{(u^2+(a-d)^2)(u^2+(a+d)^2)}.
\tag{15}
\]

For positive `A,C`,

\[
\int_{\mathbb R}
\frac{du}{(u^2+A^2)(u^2+C^2)}
=
\frac{\pi}{AC(A+C)}.
\tag{16}
\]

Taking `A=|a-d|` and `C=a+d` proves the first expression in (2). If `a>d`, then `A+C=2a`; if `a<d`, then `A+C=2d`, which gives the two branches displayed there. The lower branch tends to `2\pi/d` as `a\downarrow0`, independently checking (3), and either branch gives (10) at `a=d`.

For `a\ge a_0>d`, rewrite the second branch as

\[
\|g_{a;d,\gamma}\|_2^2
=2\pi d^2a^{-3}
\frac1{1-d^2/a^2}.
\tag{17}
\]

Because

\[
1\le\frac1{1-d^2/a^2}
\le\frac1{1-d^2/a_0^2},
\tag{18}
\]

integration against the positive measure `\mu` gives (5)--(6). When `M_3(\mu)<\infty`, (7) follows either from the squeeze in (6) or dominated convergence. When `M_3(\mu)=\infty`, the left inequality in (18) proves (9) directly. No smoothness, discreteness or finite total mass assumption on `\mu` is needed.

The frequency picture explains the third inverse moment. For `a>d`, under the convention `\widehat f(\xi)=\int f(t)e^{-it\xi}dt`,

\[
\widehat{g_{a;d,\gamma}}(\xi)
=4\pi e^{-a\xi}\sinh(d\xi)
 e^{-i\gamma\xi}\mathbf 1_{\xi>0}.
\tag{19}
\]

A line at displacement `a` exponentially suppresses frequencies above scale `1/a`. For a shallow defect `d\ll a`, the surviving range sees `\sinh(d\xi)\sim d\xi`, hence squared energy of order `d^2/a^3`. By contrast, the boundary profile in WI-424 contains frequencies out to scale `1/d` and has energy `2\pi/d`. The cubic conditioning loss is therefore the exact cost of analytic continuation across the missing high-frequency range, not an artefact of choosing finitely many lines.

## 2. Why sweeping through all depths is not a finite workaround

Equation (10) already shows the one-factor obstruction. For the full product, let `\rho` be an isolated right-half zero of multiplicity `m`. In a disk containing no other zero,

\[
B(z)=(z-\rho)^mF(z),
\qquad F(\rho)\ne0,
\]

so (12) holds with `H=F'/F` holomorphic. Shrinking the disk if necessary, `H` is bounded there, and on a still smaller punctured disk

\[
\left|\frac{B'}B(z)\right|
\ge \frac{m}{2|z-\rho|}.
\tag{20}
\]

Therefore

\[
\iint
\left|\frac{B'}B(z)\right|^2dA(z)
\ge
\frac{m^2}{4}
\int_0^r\frac{dr'}{r'}
=\infty.
\tag{21}
\]

A continuous positive depth weight changes this by only a bounded positive factor locally, proving the non-RH direction of (14). Under RH there are no right-half zeros, Kunik's Blaschke product is the empty product `B\equiv1`, and the energy is zero. Thus the multiscale strip norm crossing the entire possible defect region is not merely expensive; its finiteness is exactly a zero-free assertion.

This is the same structural warning as WI-423 in a different representation. WI-423 shows that demanding an absolutely continuous exact planar Riesz source already removes the atomic defect. Here the source remains Kunik's legitimate Blaschke product, but integrating the **logarithmic derivative** in planar `L^2` across its possible zero set makes the norm itself singular. The obstruction is local and survives any global rearrangement of the remaining zeros.

## 3. Prior art and novelty audit

No priority claim is made for the analytic ingredients.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829, gives the half-plane Poisson--Schwarz/Blaschke factorization used in WI-423--WI-425. Its equations (1.2)--(1.4) identify the right-half zeta-zero Blaschke factor whose logarithmic derivative is used here.
- The fact that a logarithmic derivative has a simple pole with residue equal to the multiplicity at each zero is classical complex analysis. The local `L^2(dA)` divergence in (21) is the elementary two-dimensional integral of that pole.
- There is extensive prior art on Hardy/Bergman regularity of derivatives of inner and Blaschke functions, including P. R. Ahern and D. N. Clark, *On inner functions with H^p derivative* (Michigan Math. J. 21 (1974), 115--127), P. R. Ahern, *The mean modulus and the derivative of an inner function* (Indiana Univ. Math. J. 28 (1979), 311--347), and later weighted Bergman work. Janne Heittokangas, *Growth estimates for logarithmic derivatives of Blaschke products and of functions in the Nevanlinna class* (Kodai Math. J. 30 (2007), 263--279, DOI `10.2996/kmj/1183475517`), is direct neighboring literature on Blaschke logarithmic derivatives. These are context for derivative/logarithmic-derivative regularity, not sources for the zeta-specific safe-line portfolio claim.
- Repository-local comparison was made against WI-410, WI-421--WI-425. WI-425 proves the exact conditioning law for one or finitely many fixed lines but explicitly leaves a continuum/multiscale norm as a possible escape. The new mathematical delta is the arbitrary-positive-measure dichotomy (5)--(9), together with the observation (10)--(14) that extending a positive `L^2` line continuum through all possible defect depths makes finiteness itself RH-equivalent. No claim is made that these elementary consequences have not appeared elsewhere.

A literature search located the classical inner-function derivative/Bergman theory and logarithmic-derivative growth estimates above, but did not locate a zeta-specific result packaging this exact safe-continuum versus pole-singularity dichotomy. Absence from that search is not used as evidence of priority.

## 4. Stress tests, boundaries and falsification

1. **Only positive diagonal line energies are excluded.** The argument applies to `Q_\mu=\int\|g_a\|_2^2d\mu(a)` with `\mu\ge0`. It does not exclude signed cross-scale combinations, non-diagonal quadratic forms in `(a,a')`, or cancellation performed before taking the norm.

2. **Renormalized pole subtraction is outside the claim.** One can remove the divergence in (21) by subtracting principal parts or puncturing neighborhoods of zeros. If the subtraction/punctures are chosen from the unknown zero set, that is oracle information; an independently defined zeta-specific renormalization could still be useful and would be genuinely new input.

3. **Depth-adaptive scales are not ruled out if selected independently.** WI-425 already shows that `a=cd` has bounded condition number. This finding says that a target-independent positive safe-line portfolio cannot obtain that scaling at finite cost, while a continuum that blindly crosses every possible `d` becomes singular. An arithmetic mechanism which independently predicts the needed depth scale is not excluded.

4. **The result is `L^2`-specific.** WI-424 makes `L^2` especially natural because its boundary energy has the exact reciprocal-depth diagonal charge. Other `L^p`, Lorentz, maximal or nonlinear functionals require separate analysis.

5. **No zero is constructed and RH is not proved.** Equation (14) is a taut-but-exact norm criterion: its reverse direction is difficult precisely because proving finiteness would already prove zero-freeness. It is used here as a no-go diagnostic for a proof interface, not as evidence that the criterion can be established arithmetically.

The finding is falsified if one exhibits a positive Borel measure supported a fixed distance `a_0>0` from the boundary such that `Q_\mu(d)` is finite for every one-zero factor yet dominates `c/d` uniformly as `d\downarrow0`; equations (5)--(9) rule this out exactly. The broader strategic conclusion would be falsified by a genuinely non-diagonal or zeta-specific multiscale estimate that avoids both sides of this dichotomy.

## Consequence for the research line

The most literal multiscale repair proposed after WI-425 is now closed. There is no useful middle regime for positive diagonal `L^2` line portfolios:

- staying in any fixed safe half-strip and keeping a finite one-zero source budget preserves the same `d^2` signal versus `1/d` boundary-energy mismatch, with exact cubic ratio;
- weighting those safe lines strongly enough to defeat the mismatch makes the budget infinite for every defect;
- moving a positive continuum through the possible defect depths creates a logarithmic pole divergence, so finiteness of the resulting strip energy is already RH-equivalent.

A viable Kunik defect-to-zero mechanism must therefore change the interface, not merely densify the sampling of safe lines. The remaining live options include non-diagonal/signed scale couplings with independently controlled cancellation, an independently defined renormalization, or a zeta-specific arithmetic identity that couples safe-line data to the unknown defect scale without first recovering the zero locations themselves.
