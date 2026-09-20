# PL-402 — Singular-series Riesz errors carry a zeta-zero layer that the cubic transition kernel does not annihilate

## Claim

`PL-401` showed that the first cubic-scale average of the continuation-faithful even-gap channel collapses to the **mean** of the Hardy--Littlewood pair singular series. That does **not** mean that linear singular-series averages are intrinsically blind to the zeta zeros. There is direct classical prior art showing the opposite.

Let

\[
\mathfrak S(k)=
\begin{cases}
2C_2\displaystyle\prod_{p\mid k,\ p>2}\frac{p-1}{p-2},&2\mid k,\\
0,&2\nmid k,
\end{cases}
\]

which is the same standard pair singular series used in `PL-401`. Goldston--Suriajaya study its unnormalized Riesz means

\[
S_m(x)=\sum_{k\le x}(x-k)^m\mathfrak S(k)
\qquad(m\ge1)
\]

and the Dirichlet generating function

\[
F(s)=\sum_{k\ge1}\frac{\mathfrak S(k)}{k^s},
\qquad \Re s>1.
\]

They prove the meromorphic continuation

\[
F(s)=
\frac{4C_2}{2^{s+1}+1}
\frac{\zeta(s)\zeta(s+1)}{\zeta(2s+2)}\,\mathcal G(s),
\qquad \Re s>-1,
\tag{1}
\]

with an Euler product `mathcal G` analytic in that region. Hence every nontrivial zeta-zero location `rho` enters the continued singular-series transform at

\[
\boxed{s_\rho=\frac\rho2-1.}
\tag{2}
\]

For their Riesz weights this produces the explicit zero contribution

\[
E_m(x)
 =x^{m-1}\sum_\rho a(\rho)x^{\rho/2}
   +O(x^{m-1+\varepsilon})
\tag{3}
\]

in the precise truncated form of their Theorem 1, and under RH the sharp exponent

\[
E_m(x)\ll_\varepsilon x^{m-3/4+\varepsilon}
\qquad(m\ge2).
\tag{4}
\]

Their unconditional omega argument also gives, for a zero `rho=Theta+i gamma` of multiplicity `m_rho`,

\[
E_m(x)
 =\Omega_\pm\!\left(
   x^{m+\Theta/2-1}
   (\log x)^{m_\rho-1}
  \right).
\tag{5}
\]

After the natural normalization by `x^(m+1)`, a zero therefore contributes at scale

\[
\boxed{x^{\rho/2-2}
 =x^{\beta/2-2}e^{i(\gamma/2)\log x}.}
\tag{6}
\]

Thus the half-line has an exact meaning in this Mellin spectrum: on RH all nontrivial zero modes have common radial exponent

\[
\frac{1/2}{2}-2=-\frac74,
\]

while their ordinates become frequencies `gamma/2` in the logarithmic variable `log x`.

For every fixed `m>=2`, combining Goldston--Suriajaya's RH upper bound with (5) and the zeta functional equation yields the clean corollary

\[
\boxed{
\mathrm{RH}
\iff
\frac{E_m(x)}{x^{m+1}}
 =O_\varepsilon(x^{-7/4+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\tag{7}
\]

This is prior-art arithmetic, not a new RH criterion claimed by this line. Its significance here is that it identifies exactly what `PL-401`'s first-moment collapse discarded: the zero-sensitive information lives in a **subleading Mellin layer of the same singular series**, not necessarily in a nonlinear statistic or in an actual `Lambda(r)Lambda(r+d)` error.

There is moreover a direct compatibility with the cubic transition phase. Put

\[
H=r^{1/3},
\qquad
a=\frac\pi6,
\qquad
g(u)=\frac{\sin(a u^3)}{u},
\tag{8}
\]

with `g(0)=0`. The leading even-gap term of `PL-401` is

\[
-\frac{1}{\sqrt2\,\pi H}
\sum_d \mathfrak S(d)\,g(d/H)
\tag{9}
\]

on the cubic window, modulo the cutoffs and transition errors specified there. The oscillatory Mellin transform of the ideal full cubic kernel is exact for

\[
-2<\Re s<4:
\]

\[
\boxed{
\widehat g(s)
 =\int_0^\infty u^{s-1}g(u)\,du
 =\frac13
   a^{-(s-1)/3}
   \Gamma\!\left(\frac{s-1}{3}\right)
   \sin\!\left(\frac{\pi(s-1)}6\right).
}
\tag{10}
\]

At every nontrivial zeta-zero location `s_rho=rho/2-1`, the imaginary part is nonzero. Since Gamma has no zeros and the sine factor in (10) vanishes only at the real points `s=1+6k`,

\[
\boxed{\widehat g(s_\rho)\ne0}
\tag{11}
\]

for every nontrivial zero `rho`. Therefore the **cubic phase itself does not annihilate the zeta-zero pole locations in Mellin space**. Any cancellation of an individual residue would have to come from the arithmetic factor in (1), not from the continuation kernel discovered in `PL-401`.

Two consistency checks are especially sharp:

\[
\widehat g(1)=\frac\pi6,
\tag{12}
\]

which is exactly the universal Gallagher mass computed in `PL-401`, and

\[
\widehat g(0)
 =\frac12\left(\frac\pi6\right)^{1/3}\Gamma(2/3)\ne0.
\tag{13}
\]

Since the generating function `F(s)` itself has residue `-1/2` at `s=0`, a rigorously regularized cubic Mellin average has a deterministic `H^-1` layer before the zero layer. On RH the latter begins at `H^-7/4`. This ordering is crucial because the transition approximation currently available in `PL-401` is only accurate at aggregate order `H^-1` on a fixed cubic annulus. The zero-sensitive layer is therefore **real but still below the present continuation error floor**.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + ROUTE-REOPENING + SCALE-OBSTRUCTION`.

The literature component is the Goldston--Suriajaya continuation and Riesz explicit formula. Equations (6), (7), and the cubic-kernel Mellin calculation (10)--(13) are derived here. No novelty is claimed for Mellin inversion, Riesz means, or the zero-sensitive singular-series mechanism itself.

## 1. The classical singular-series transform already contains the zero divisor

Goldston--Suriajaya's factorization (1) is the decisive prior-art redirect. The denominator

\[
\zeta(2s+2)
\]

moves a zeta zero `rho` to `s=rho/2-1`. This is not a formal continuation of the Hardy--Littlewood Euler product. The Dirichlet series for `F(s)` is first defined in `Re(s)>1`, and their theorem gives a meromorphic continuation of the resulting function into `Re(s)>-1`.

The Riesz weight contributes the Mellin factor

\[
\frac{m!}{s(s+1)\cdots(s+m)},
\]

so contour shifting turns the poles at `s_rho` into residues proportional to

\[
x^{m+s_\rho}
 =x^{m-1+\rho/2}.
\]

This is exactly the exponent in their explicit formula. The pole at `s=1` gives the mean term `x^(m+1)/(m+1)`, while the singularity at `s=0` together with the Riesz Mellin factor gives the familiar `x^m log x` correction.

Normalize by `x^(m+1)`. Then the zero contribution is (6). If RH holds, `beta=1/2` and every such mode has modulus `x^-7/4`; the remaining `x^(i gamma/2)` is a pure oscillation in `log x`. Conversely, if RH is false, the functional equation produces a zero with `Theta>1/2`. Goldston--Suriajaya's omega bound (5) then gives a normalized contribution of size

\[
x^{\Theta/2-2}(\log x)^{m_\rho-1},
\]

which is larger by the fixed power

\[
x^{(\Theta-1/2)/2}
\]

than the RH scale. Choosing `epsilon<(Theta-1/2)/2` contradicts the right side of (7). This proves the derived equivalence (7).

The result is stronger evidence for a meaningful Mellin/spectral interpretation than the first-moment use of the singular series in `PL-401`, but it is not Hilbert--Polya: the zeros are poles of an already continued arithmetic transform, not eigenvalues of a self-adjoint operator.

## 2. The cubic transition kernel has the right Mellin fingerprint

At the cubic scale `H=r^(1/3)`, the even-gap coefficient from `PL-401` is

\[
\Re P_{r,d}
 =-\frac{1+o(1)}{\sqrt2\,\pi d}
   \sin\!\left(\frac{\pi d^3}{6r}\right).
\]

Writing `d=Hu` gives exactly

\[
\Re P_{r,d}
 \sim
 -\frac1{\sqrt2\,\pi H}g(u).
\]

The transform (10) follows by the substitution `t=a u^3`:

\[
\begin{aligned}
\widehat g(s)
&=\int_0^\infty u^{s-2}\sin(a u^3)\,du\\
&=\frac13a^{-(s-1)/3}
  \int_0^\infty
  t^{(s-1)/3-1}\sin t\,dt.
\end{aligned}
\]

Using the standard oscillatory sine Mellin integral gives (10), initially on its ordinary convergence strip and then throughout `-2<Re(s)<4` by the same oscillatory interpretation. Near zero, `g(u)=a u^2+O(u^8)`, which gives the lower boundary `Re(s)>-2`; at infinity the cubic oscillation gives the upper boundary.

At `s=1`, the apparent `Gamma(0) sin(0)` singularity is removable and

\[
\widehat g(1)
 =\frac13\lim_{z\to0}\Gamma(z)\sin(\pi z/2)
 =\frac\pi6.
\]

This recovers the integral used in `PL-401`:

\[
\int_0^\infty\frac{\sin(\pi u^3/6)}u\,du=\frac\pi6.
\]

At `s=0`, the recurrence `Gamma(2/3)=(-1/3)Gamma(-1/3)` yields (13). Hence neither the average pole at `s=1` nor the first lower arithmetic singularity at `s=0` is suppressed by the cubic phase.

Most importantly, for

\[
s_\rho=\frac\rho2-1
\]

one has `-1<Re(s_rho)<-1/2` and `Im(s_rho)=gamma/2 != 0`. The zero set of the sine factor in (10) is real, while Gamma has no zeros. Equation (11) follows immediately. In this precise sense, the cubic continuation kernel is **spectrally compatible** with the classical zeta-zero layer of the pair singular series.

## 3. Why the zero layer is below the present PL-401 error floor

The compatibility in Section 2 is not yet a theorem transferring the Goldston--Suriajaya explicit formula to the exact continuation statistic of `PL-401`. The scale comparison shows exactly what is missing.

On a fixed cubic annulus

\[
\delta H\le d\le C H,
\qquad H=r^{1/3},
\]

`PL-401` currently has the pointwise approximation

\[
P_{r,d}
 =P^{(0)}_{r,d}
 +O\!\left(
   d^{-2}+r^{-1}+d^3r^{-2}
  \right).
\tag{14}
\]

Across `Theta(H)` gaps, the three error terms aggregate respectively as

\[
O(H^{-1}),\qquad O(H^{-2}),\qquad O(H^{-2}),
\tag{15}
\]

using only the first-moment control of `mathfrak S(d)`. The dominant `H^-1` error comes from the next `1/d` correction in the transition factors.

That is not an accidental mismatch. The arithmetic Mellin transform itself has a singularity at `s=0`, and (13) says the cubic kernel sees it. A regularized cubic average should therefore contain an `H^-1` deterministic arithmetic term before any nontrivial-zero term. On RH the zero layer is only

\[
H^{-7/4+i\gamma/2}.
\tag{16}
\]

Thus the present continuation expansion stops **three quarters of a power too early** to resolve the RH-sensitive layer. Merely subtracting the universal `pi/6` mean from `PL-401` is insufficient.

A genuine transfer theorem would have to expand and renormalize the continuation kernel through every contribution larger than `H^-7/4`, including the aggregate `H^-1` term, and leave a remainder `o(H^-7/4+epsilon)` at the desired scale. This is now a quantitative target rather than the vague instruction to “look at fluctuations beyond Gallagher's mean.”

## 4. Regularization boundary for the ideal cubic weight

There is one analytic subtlety that must not be hidden. The ideal kernel

\[
g(u)=\frac{\sin(a u^3)}u
\]

has only `1/u` amplitude decay. Its Mellin transform is well defined as an oscillatory integral, but on an initial line `Re(s)>1` its vertical Gamma decay is exactly canceled by the exponential growth of the sine factor. One cannot therefore justify the full discrete identity

\[
\frac1H\sum_{d\ge1}\mathfrak S(d)g(d/H)
 \stackrel{?}{=}
 \frac1{2\pi i}
 \int F(s)\widehat g(s)H^{s-1}\,ds
\tag{17}
\]

by a naive absolutely convergent Mellin inversion on that line.

This is a technical, not conceptual, obstruction. A smooth compact cutoff or Abel factor at `d/H` makes the initial Mellin inversion absolute and permits the standard contour machinery. For such regularizations, the zero poles remain at the same `s_rho`; their residues are multiplied by the Mellin transform of the chosen weight. The exact calculation (11) shows that in the limit toward the ideal cubic phase there is no structural zero imposed by the phase itself at any nontrivial `s_rho`.

The hard finite window of `PL-401` is another possible regularization, but its endpoint and uniform transition errors have to be tracked if one wants a theorem at the `H^-7/4` scale. This finding does **not** claim that (17), without a regulator, is already justified.

## 5. Prior-art and novelty audit

The main literature anchor is:

- **D. A. Goldston, Ade Irma Suriajaya**, “A singular series average and the zeros of the Riemann zeta-function,” *Acta Arithmetica* **200** (2021), 71--90, DOI `10.4064/aa200821-24-2`, arXiv:2007.16099. Their Lemma 2.1 is the continuation (1); Theorems 1--2 give the zero explicit formula and RH upper bound; Theorems 4--5 and equation (6.1) give the oscillation/omega obstruction from off-line or multiple zeros.

The journal abstract explicitly states that the Riesz-mean error term is expressible through the zeta zeros. The paper also explains that the Cesaro/Riesz singular-series average arises naturally from prime short-interval variance, tying this prior art to the same pair-correlation neighborhood already encountered in `PL-077` and `PL-401`.

A targeted search for the specific cubic weight `sin(pi u^3/6)/u`, cubic transition phases, and singular-series Mellin averages did not locate a source combining this exact kernel with the Goldston--Suriajaya transform. No novelty claim is made for generic smooth-weight Mellin summation. The only line-specific derived content is the compatibility calculation (10)--(13), the RH-equivalent normalized exponent (7), and the scale comparison with the actual `PL-401` continuation error.

The earlier conclusion of `PL-401` remains correct at leading order: Gallagher first-moment averaging sees only the universal mass. What changes is the interpretation of the residual. It is no longer justified to treat “linear singular-series averaging” itself as exhausted. Classical prior art proves that sufficiently resolved subleading Riesz errors already carry the zero divisor.

## 6. Adversarial controls

Several failure modes are excluded explicitly.

1. **No Euler-product continuation shortcut.** Equation (1) is a theorem about the meromorphic continuation of the singular-series Dirichlet generating function. The zero poles are not obtained by formally evaluating an Euler product outside absolute convergence.
2. **No claim that every residue is individually nonzero.** Equation (11) says only that the cubic **weight factor** does not vanish at `s_rho`. Arithmetic numerator factors in (1), zero multiplicities, or residue interactions remain separate issues. Goldston--Suriajaya's omega theorem supplies the robust global off-line obstruction.
3. **No replacement of actual prime-pair errors by the singular series.** The singular series is the Hardy--Littlewood local-density model. A theorem for `Lambda(r)Lambda(r+d)` with the same continuation weight would require additional averaged prime-pair input.
4. **No Hilbert--Polya claim.** The frequencies `gamma/2` in `log H` come from residues of a meromorphically continued arithmetic transform; they are not the point spectrum of a self-adjoint operator.
5. **No hidden RH assumption in the pole map.** The continuation (1), explicit formula of Theorem 1, and omega estimate (5) are unconditional. RH enters only when all `beta` are set equal to `1/2` for the upper bound (4).
6. **The half exponent is not inserted by hand.** The map `s_rho=rho/2-1` is forced by the denominator `zeta(2s+2)`. The normalized error exponent `-7/4` is exactly the image of `beta=1/2` under `beta/2-2`.
7. **The cubic transfer is not yet below its own error.** Any numerical or asymptotic claim to see zero ordinates directly in the present `PL-401` statistic before removing the `H^-1` layer would be below the justified resolution and must be rejected.

## Consequence for the line

The next continuation-faithful pair test is now sharply specified. The question is no longer merely whether arithmetic fluctuations of `mathfrak S(d)` survive the cubic phase. Classical theory says that the singular series has a zero-sensitive Mellin layer, and the exact cubic kernel has nonzero Mellin response at every nontrivial zero location.

The missing bridge is quantitative:

\[
\boxed{
\text{continue the PL-401 cubic expansion past the }H^{-1}
\text{ layer and control the aggregate remainder at }H^{-7/4+\varepsilon}.
}
\]

If that bridge can be made rigorous, the resulting centered statistic should be compared against the classical pole pattern

\[
H^{\rho/2-2}
 =H^{\beta/2-2}e^{i(\gamma/2)\log H}.
\]

Failure to recover this pattern would falsify the proposed transfer from the singular-series model to the continuation kernel; success would still not prove RH, but it would turn the current cubic branch into a concrete continuation-faithful detector of the same zero layer that Riesz singular-series means already encode.