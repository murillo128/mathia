# WI-295 — exact digamma bathtub gives an explicit screened support floor

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-BATHTUB + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed, completely screened** first-crossing branch of `WI-281`--`WI-294`. This finding sharpens the qualitative support-measure floor in `WI-294` by retaining Suzuki's exact gamma multiplier instead of replacing it by a coarse logarithmic lower bound. It also turns the same estimate into an amplitude tariff for widely separated pieces of a hypothetical many-component support.
- **Result:** if `v>=0` is a normalized first-crossing null mode and every active prime-power autocorrelation is screened, then its positivity support `E={v>0}` must satisfy an exact universal lower bound

  \[
  |E|>\mu_*,
  \]

  where `\mu_*` is the unique positive zero of the explicit monotone function `\mathcal H` in (6). Numerically, for orientation only,

  \[
  \mu_*\approx 0.17604298731884824.
  \]

  Together with the exact `|E|<=log 2` packing bound of `WI-281`, complete one-signed screening therefore confines the support measure to a nontrivial compact interval rather than merely requiring it to be nonzero.
- **Novelty boundary:** Suzuki supplies the gamma-plus-pole decomposition. `WI-287` already introduced the Fourier `L^infinity` cap and a bathtub rearrangement after replacing the exact gamma multiplier by `log(1+|z|)-C`; `WI-294` used that coarse version to deduce an unspecified absolute support floor for the actual nonnegative null vector. The new line-local deduction is to prove that Suzuki's **exact** multiplier is even and strictly increasing in `|z|`, apply the bathtub principle directly to it, identify the unique exact support threshold, and feed the resulting gamma bound back into the positive pole factorization. No priority claim is made.

## Claim

Let `a>0` be a Suzuki first crossing and let

\[
0\ne v\ge0,
\qquad
\|v\|_2=1,
\qquad
A_av=0,
\qquad
q_a(v)=0,
\tag{1}
\]

be a real first null mode, extended by zero outside `(-a,a)`. Assume complete screening of every active prime-power autocorrelation. Put

\[
E:=\{x\in(-a,a):v(x)>0\},
\qquad
\mu:=|E|.
\tag{2}
\]

By `WI-284` and `WI-294`, complete screening removes the discrete prime source on this vector and leaves

\[
q_{\rm arch}^a(v)=G(v)+P_a(v)=0,
\tag{3}
\]

where

\[
G(v)
=\frac1{2\pi}\int_{\mathbb R}
 m(z)|\widehat v(z)|^2\,dz,
\qquad
m(z):=
\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi,
\tag{4}
\]

and

\[
P_a(v)
=2L_-(v)L_+(v),
\qquad
L_\pm(v):=\int_{-a}^{a}v(x)e^{\pm x/2}\,dx.
\tag{5}
\]

For `\mu>0` define the exact gamma bathtub profile

\[
\boxed{
\mathcal H(\mu)
:=
\frac{\mu}{2\pi}
\int_{-\pi/\mu}^{\pi/\mu}
\left[
\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi
\right]dz.
}
\tag{6}
\]

Then `\mathcal H` is continuous and strictly decreasing on `(0,\infty)`, with

\[
\lim_{\mu\downarrow0}\mathcal H(\mu)=+\infty,
\qquad
\lim_{\mu\to\infty}\mathcal H(\mu)
=m(0)<0.
\tag{7}
\]

Hence there is a unique `\mu_*>0` such that

\[
\boxed{\mathcal H(\mu_*)=0.}
\tag{8}
\]

Every normalized function supported on a measurable set of measure `\mu` obeys

\[
\boxed{
G(v)\ge \mathcal H(\mu).
}
\tag{9}
\]

For a nonzero compactly supported `v`, the inequality is in fact strict. Since `v>=0` is nonzero, both factors in (5) are strictly positive, so (3) gives

\[
G(v)=-P_a(v)<0.
\tag{10}
\]

Combining (8)--(10) yields the exact support floor

\[
\boxed{
\mu=|E|>\mu_*.
}
\tag{11}
\]

The power-of-two screening argument of `WI-281` independently gives

\[
\mu\le L:=\log2.
\tag{12}
\]

Therefore every one-signed completely screened first null mode must satisfy

\[
\boxed{
\mu_*<|E|\le\log2.
}
\tag{13}
\]

A non-load-bearing high-precision numerical evaluation gives

\[
\mu_*\approx0.17604298731884824,
\qquad
\frac{\mu_*}{\log2}\approx0.2539763448.
\tag{14}
\]

Thus complete screening cannot be realized by a positivity set using an arbitrarily small fraction of the `log 2` selector budget.

The same argument also bounds Suzuki's positive pole coupling. From (3), (9), and (10),

\[
\boxed{
0<P_a(v)<-\mathcal H(\mu).
}
\tag{15}
\]

Using `\mu\le\log2` and monotonicity of `\mathcal H`,

\[
\boxed{
P_a(v)<C_2,
\qquad
C_2:=-\mathcal H(\log2).
}
\tag{16}
\]

For orientation only,

\[
C_2\approx1.4978867223836473.
\tag{17}
\]

Finally let `A,B\subset E` be measurable sets such that

\[
y-x\ge R\ge0
\qquad(x\in A,\ y\in B)
\tag{18}
\]

up to null sets, and write

\[
M_1(A):=\int_Av(x)dx,
\qquad
M_1(B):=\int_Bv(x)dx.
\tag{19}
\]

Then the pole factorization gives the separated-mass tariff

\[
\boxed{
M_1(A)M_1(B)
<
\frac{-\mathcal H(\mu)}{4\cosh(R/2)}
\le
\frac{C_2}{4\cosh(R/2)}.
}
\tag{20}
\]

Thus widely separated components are permitted only if their `L^1` amplitudes become exponentially unbalanced. This is an amplitude restriction on the live many-component branch that is invisible to support topology alone.

## 1. Suzuki's exact gamma multiplier is radially monotone

The multiplier `m` in (4) is even because the digamma function respects complex conjugation away from its poles. To prove strict monotonicity, let

\[
b_n=n+\frac14,
\qquad
y=\frac z2.
\tag{21}
\]

For `z>0`, the absolutely convergent trigamma series gives

\[
\psi'\!\left(\frac14+iy\right)
=\sum_{n\ge0}\frac1{(b_n+iy)^2}.
\tag{22}
\]

Differentiating the real part with respect to `z`,

\[
\begin{aligned}
 m'(z)
&=\operatorname{Re}
\left[
\frac i2
\psi'\!\left(\frac14+\frac{iz}{2}\right)
\right]\\
&=
\sum_{n\ge0}
\frac{b_ny}{(b_n^2+y^2)^2}
>0.
\end{aligned}
\tag{23}
\]

Hence `m(z)` is strictly increasing for `z>0` and is therefore a strictly increasing function of `|z|`.

This is the only special-function monotonicity needed below. No numerical property of the digamma function is used in the proof.

## 2. Direct bathtub minimization of the exact multiplier

Because `v` is supported on a set of measure `\mu`, Cauchy--Schwarz gives

\[
|\widehat v(z)|
\le\|v\|_1
\le\sqrt\mu\,\|v\|_2
=\sqrt\mu.
\tag{24}
\]

Parseval gives

\[
\frac1{2\pi}\int_{\mathbb R}|\widehat v(z)|^2dz=1.
\tag{25}
\]

Therefore

\[
p_v(z):=\frac{|\widehat v(z)|^2}{2\pi}
\tag{26}
\]

is a probability density satisfying the exact cap

\[
0\le p_v(z)\le c_\mu:=\frac\mu{2\pi}.
\tag{27}
\]

Let

\[
A_\mu:=\frac\pi\mu,
\qquad
p_*(z):=c_\mu\,\mathbf1_{[-A_\mu,A_\mu]}(z).
\tag{28}
\]

Then `p_*` also has total mass one. Since `m` is even and strictly increasing in `|z|`, the elementary bathtub comparison is exact:

\[
\int m(z)p_v(z)dz
\ge
\int m(z)p_*(z)dz.
\tag{29}
\]

For completeness, subtract `m(A_\mu)` from the integrand. On `|z|<A_\mu`, both

\[
m(z)-m(A_\mu)\le0,
\qquad
p_v(z)-c_\mu\le0,
\]

so their product is nonnegative. Outside that interval, both

\[
m(z)-m(A_\mu)\ge0,
\qquad
p_v(z)\ge0,
\]

so the product is again nonnegative. The total-mass equality removes the constant `m(A_\mu)`. This proves (29), and (29) is precisely (9).

This also identifies the exact extremizer of the **density-cap relaxation**: it is the centered saturated box `p_*`. The statement is deliberately about the relaxation, not about actual Fourier power spectra of compactly supported functions.

For the actual compactly supported `v`, equality cannot occur. Equality in the bathtub step would force `|\widehat v|^2` to vanish almost everywhere outside a bounded interval. But compact support makes `\widehat v` an entire function; vanishing on a real interval would force `\widehat v\equiv0`, contrary to `\|v\|_2=1`. Thus (9) is strict for the present null vector, which accounts for the strict inequalities in (11), (15), and (20).

## 3. The exact threshold is unique

Put

\[
A:=\frac\pi\mu,
\qquad
F(A):=\frac1A\int_0^A m(z)dz.
\tag{30}
\]

Then

\[
\mathcal H(\mu)=F(\pi/\mu).
\tag{31}
\]

Since `m` is strictly increasing,

\[
F'(A)
=
\frac{m(A)-F(A)}A
>0.
\tag{32}
\]

Thus `\mathcal H` is strictly decreasing in `\mu`.

At the large-support end,

\[
\lim_{\mu\to\infty}\mathcal H(\mu)
=m(0)
=\psi\!\left(\frac14\right)-\log\pi
<0.
\tag{33}
\]

At the small-support end the standard digamma asymptotic on the fixed vertical line `Re s=1/4` gives

\[
m(z)=\log|z|-\log(2\pi)+o(1)
\qquad(|z|\to\infty).
\tag{34}
\]

Averaging (34) over `[0,A]` yields

\[
F(A)=\log A-1-\log(2\pi)+o(1)
\to+\infty.
\tag{35}
\]

Equations (31)--(35) prove existence and uniqueness of `\mu_*` in (8).

The numerical value in (14) is not load-bearing. The theorem uses the exact root characterization (8); a future interval-arithmetic formalization can enclose `\mu_*` if a certified decimal is useful.

## 4. Positive pole coupling converts the gamma floor into an amplitude tariff

For real nonnegative `v`, the pole term can be symmetrized as

\[
\begin{aligned}
P_a(v)
&=2L_-(v)L_+(v)\\
&=2\iint_{(-a,a)^2}
 v(x)v(y)\cosh\!\left(\frac{y-x}{2}\right)dxdy.
\end{aligned}
\tag{36}
\]

The first equality is Suzuki's exact pole factorization, and the second follows by averaging the exponential kernel with its transpose.

Because the kernel in (36) is positive, retain only the cross terms `A\times B` and `B\times A`. Under (18),

\[
P_a(v)
\ge
4\cosh(R/2)
M_1(A)M_1(B).
\tag{37}
\]

Combining (37) with (15) proves the first inequality in (20). The second follows from `\mu\le\log2` and the monotonicity of `\mathcal H`.

This is stronger than the support statement alone in exactly the direction left open by `WI-282`--`WI-294`. Tiny remote satellites can preserve full aperture while barely changing support-based variational bounds. Equation (20) shows that the actual null vector pays for such remote pieces in the exponentially weighted pole coupling: two separated pieces cannot both retain fixed `L^1` amplitude as their separation grows.

It does not yet turn that tariff into an `L^2` contradiction. Without additional regularity or amplitude control, a set of positive measure may carry arbitrarily small `L^1` mass while another region carries the normalized `L^2` mass. That is the remaining quantitative gap.

## 5. Relation to the current one-signed screening frontier

`WI-281` proves `|E|<=log2` from the power-of-two subfamily and then uses rearrangement to reduce the positive source budget. `WI-282`--`WI-283` show that support packing and support domination alone still admit full-span many-component relaxations. `WI-284` promotes complete screening to the exact prime-deleted null identity. `WI-286`--`WI-293` deliberately relax the actual null vector to unrestricted signed vectors on candidate supports, while `WI-294` restores one-signedness and observes that the positive pole forces `G(v)<0`; a coarse logarithmic gamma estimate then yields some unspecified `\mu_0>0`.

The present finding closes the constant-loss in that last step. The exact multiplier itself supplies the optimal centered bathtub profile under the Fourier `L^infinity` cap, so no auxiliary global lower bound

\[
m(z)\ge\log(1+|z|)-C
\]

is needed. The support floor is therefore no longer merely existential: it is pinned to the unique special-function threshold (8), and the same calculation gives the pole/cross-component tariff (20).

There is also a useful no-go boundary. The centered saturated density in §2 is the exact optimizer of the information retained by

\[
\operatorname{supp}(v)\text{ has measure }\mu,
\qquad
\|v\|_2=1
\]

through the sole Fourier cap (27). Therefore a stronger universal gamma lower bound cannot come from rearranging the same cap more cleverly. Any improvement past `\mathcal H(\mu)` must use additional structure of actual Fourier transforms, the `log 2` selector geometry, firstness/null-equation constraints, or further prime lags.

## 6. Prior-art and provenance audit

The load-bearing operator identity is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), already source-audited in `WI-238`, `WI-240`, and `SOURCES.md`. The gamma multiplier (4) is the classical archimedean term in Weil's explicit formula; the pole factorization (5) is the exact finite-aperture form recorded in `WI-240`.

The Fourier `L^infinity` cap (24)--(27) and the use of a bathtub rearrangement are already internal prior art in `WI-287`. That finding first replaced the exact multiplier by a coarse `log(1+|z|)-C_\Gamma` lower bound because its purpose was the asymptotic two-island Lambert-`W` balance. `WI-294` then reused the resulting `log(1/\mu)-C_0` estimate for the actual nonnegative null vector. The present result is not a claim that the bathtub principle is new; it retains the exact digamma multiplier and proves the monotonicity needed to run the rearrangement without the lossy comparison function.

A targeted literature search around Suzuki's localized Weil form, nonnegative/support-restricted null vectors, Fourier-support uncertainty, and direct rearrangement of the digamma archimedean multiplier located Suzuki's operator paper and standard explicit-formula treatments, but no source giving the threshold (8) or the separated-mass consequence (20). Search absence is recorded only as novelty-audit context and is not used as mathematical evidence or as a priority claim.

## 7. Stress tests and limits

- **One-signedness is load-bearing for the floor.** The bathtub bound (9) holds for arbitrary supported `v`, but the implication `G(v)<0` uses `P_a(v)>0`, which can fail for sign-changing vectors.
- **Complete screening is load-bearing.** It is what gives `q_{\rm arch}^a(v)=0`; surviving prime terms can alter the gamma/pole balance.
- **The decimal in (14) is not a certified input.** The exact theorem is (8) and (11). The displayed decimal is only numerical orientation.
- **`\mu_*` need not be the true optimal support floor for actual null modes.** It is the exact threshold obtained from the sharp pointwise Fourier cap and the exact gamma multiplier. Analyticity, selector geometry, the null equation, and firstness may force a larger floor.
- **The pole tariff is in `L^1`, not `L^2`.** Remote components can still evade (20) by carrying very small amplitude. A future closure needs a source-specific mechanism converting the existing cutwise `L^2` reserves into enough `L^1` mass, or a direct Fourier/null-equation argument that forbids such vanishing satellites.
- **No statement about the current simple-critical-zero proportion changes.** This is a structural constraint on the exceptional/off-line route toward the ultimate RH objective.

## Research consequence

The live one-signed complete-screening branch now has two simultaneous quantitative constraints:

\[
\boxed{
\mu_*<|\{v>0\}|\le\log2
}
\tag{38}
\]

and, for any two positivity pieces separated by `R`,

\[
\boxed{
\left(\int_Av\right)
\left(\int_Bv\right)
\ll e^{-R/2}
}
\tag{39}
\]

with the exact constant given in (20). Thus the surviving many-component geometry cannot be merely a distance-avoiding set of positive total measure: any full-span construction must also become strongly amplitude-hierarchical across large separations. The next useful bridge is to combine this exponential `L^1` hierarchy with the cutwise firstness reserves of `WI-270`--`WI-280` or with the exact Suzuki null equation, aiming to show that a normalized null mode cannot maintain the required `L^2` mass while all remote `L^1` interactions decay at the pole-imposed rate.