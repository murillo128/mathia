# WI-273 — positive-tail Hankel norm sharpens gap screening but hits the Carleman wall

## Status

- **Evidence:** `EXACT-DERIVED + SOURCE-SPECIFIC-RIGIDITY + CLASSICAL-CARLEMAN + DECISIVE-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** a strengthening and exact calibration of the one-signed internal-gap route in `WI-270`--`WI-272`. It replaces the scalar positive-tail budget `B(L)` by the actual `L^2` Hankel-operator norm of Suzuki's positive archimedean source, retains only the adjacent collar masses that can participate across the gap, and identifies the sharp zero-gap limit.
- **What it does not claim:** this is not RH, does not show that the hypothetical first null mode is one-signed, and does not by itself exclude arbitrarily narrow screened gaps. The sign-changing branch remains governed by `WI-269` and the accepted signed-source clue.
- **Barrier:** the exact mass-only source-conditioned coefficient tends to `pi/2` as the gap width tends to zero. Therefore merely replacing the Hilbert--Carleman majorant of `WI-270` by the exact positive Suzuki kernel cannot produce a uniform strict improvement in the gapless/narrow-gap limit. Further progress there must use additional structure of the null mode, the full family of cuts, or the distributional null equation rather than only an `L^2` operator norm.

## Claim

Assume the setup of `WI-271` and `WI-272`: RH is false, `a=a_*` is the first unrestricted Suzuki crossing, and `v` is a normalized real one-signed first null mode,

\[
\|v\|_2=1,\qquad A_av=0,\qquad q_a\ge0,\qquad v\ge0\quad\text{a.e.}
\tag{1}
\]

extended by zero outside `(-a,a)`. Let

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\tag{2}
\]

and let

\[
h_0=\log\rho,\qquad \rho^3-\rho-1=0,
\tag{3}
\]

so that `w>0` on `(0,h_0)`, `w(h_0)=0`, and `w<0` on `(h_0,\infty)`.

Suppose `v` has an internal essential-support gap `(\alpha,\beta)` with positive mass on both sides. Put

\[
L=\beta-\alpha>0,
\qquad
M_L=\int_{-a}^{\alpha}v(x)^2dx,
\qquad
M_R=\int_{\beta}^{a}v(x)^2dx,
\tag{4}
\]

and

\[
r_L=\frac{a+\alpha}{2},
\qquad
r_R=\frac{a-\beta}{2}.
\tag{5}
\]

For `0\le L<h_0`, define the positive Hankel kernel on `\mathbb R_+^2`

\[
K_L(u,y)
:=w(L+u+y)\,\mathbf 1_{\{u+y<h_0-L\}},
\tag{6}
\]

and its self-adjoint integral operator

\[
(T_Lf)(u)=\int_0^\infty K_L(u,y)f(y)\,dy,
\qquad
\Theta(L):=\|T_L\|_{L^2(\mathbb R_+)\to L^2(\mathbb R_+)}.
\tag{7}
\]

For `L\ge h_0`, set `\Theta(L)=0`. Also define the only side masses that the positive kernel can see,

\[
\begin{aligned}
m_L^{\rm col}(L)
&:=\int_{\max\{-a,\,\alpha-(h_0-L)\}}^{\alpha}v(x)^2dx,\\
m_R^{\rm col}(L)
&:=\int_{\beta}^{\min\{a,\,\beta+(h_0-L)\}}v(x)^2dx.
\end{aligned}
\tag{8}
\]

Then the exact cross-gap identity of `WI-271`, combined only with the sign of the long-range source, gives the sharper tariff

\[
\boxed{
P_{\alpha,\beta}
\ge
\max\{\lambda_{r_L}M_L,\lambda_{r_R}M_R\}
-\Theta(L)
\sqrt{m_L^{\rm col}(L)m_R^{\rm col}(L)}.
}
\tag{9}
\]

This improves the `WI-272` mass-only estimate because

\[
\boxed{
0\le\Theta(L)\le B(L)
:=\int_L^{h_0}w(h)\,dh
}
\qquad(0<L<h_0),
\tag{10}
\]

while the collar masses in (9) are no larger than `M_L,M_R`.

There is a second explicit bound that is stronger near the sign-change scale. Since `T_L` is Hilbert--Schmidt for every `L>0`, put

\[
H(L):=
\left(
\int_L^{h_0}(h-L)w(h)^2\,dh
\right)^{1/2}.
\tag{11}
\]

Then

\[
\boxed{
\Theta(L)\le
\min\left\{B(L),H(L),\frac\pi2\right\}.
}
\tag{12}
\]

Moreover,

\[
\boxed{
\Theta(L)<\frac\pi2\quad(0<L<h_0),
\qquad
\Theta(0)=\frac\pi2,
\qquad
\lim_{L\downarrow0}\Theta(L)=\frac\pi2.
}
\tag{13}
\]

Thus the strict positive-width improvement degenerates exactly to the Carleman coefficient of `WI-270` as the gap closes.

Under complete prime screening, `P_{\alpha,\beta}=0`, and (9) forces both

\[
\Theta(L)\sqrt{m_L^{\rm col}m_R^{\rm col}}
\ge \lambda_{r_L}M_L,
\qquad
\Theta(L)\sqrt{m_L^{\rm col}m_R^{\rm col}}
\ge \lambda_{r_R}M_R.
\tag{14}
\]

Multiplying yields the local-concentration constraint

\[
\boxed{
\frac{m_L^{\rm col}(L)m_R^{\rm col}(L)}{M_LM_R}
\ge
\frac{\lambda_{r_L}\lambda_{r_R}}{\Theta(L)^2}.
}
\tag{15}
\]

In particular, complete screening is impossible whenever

\[
\boxed{
\Theta(L)<\sqrt{\lambda_{r_L}\lambda_{r_R}}.
}
\tag{16}
\]

The computable sufficient condition obtained by replacing `\Theta(L)` with the right side of (12) strictly strengthens the `B(L)` criterion of `WI-272` on every range where `H(L)<B(L)` or `\pi/2<B(L)`.

Near `h_0`, this strengthening has an exact leading-order size. Writing

\[
c:=-w'(h_0)=\sqrt\rho\,(3+2\rho),
\qquad
\varepsilon=h_0-L,
\tag{17}
\]

one has

\[
B(L)=\frac c2\varepsilon^2+O(\varepsilon^3),
\tag{18}
\]

whereas

\[
\boxed{
H(L)=\frac{c}{2\sqrt3}\varepsilon^2+O(\varepsilon^3).
}
\tag{19}
\]

Thus the elementary Hilbert--Schmidt compression alone reduces the leading positive-tail budget by a factor `1/sqrt(3)` compared with `WI-272` near the sign-change threshold.

## 1. The positive cross-gap source is exactly a Hankel bilinear form

`WI-271` proves, using a Lipschitz transition through the support gap, that the common left/right cut energy is

\[
Q_{\alpha,\beta}
=P_{\alpha,\beta}
+\int_L^{2a}w(h)J_{\alpha,\beta}(h)\,dh
\tag{20}
\]

and firstness gives

\[
Q_{\alpha,\beta}
\ge
\max\{\lambda_{r_L}M_L,\lambda_{r_R}M_R\}.
\tag{21}
\]

Because `v\ge0`, the cross-gap overlap `J_{\alpha,\beta}(h)` is nonnegative. The part of (20) with `h>h_0` is therefore nonpositive, so

\[
Q_{\alpha,\beta}
\le
P_{\alpha,\beta}
+\int_L^{h_0}w(h)J_{\alpha,\beta}(h)\,dh.
\tag{22}
\]

Set

\[
f_L(u)=v(\alpha-u),\qquad
f_R(y)=v(\beta+y)
\qquad(u,y\ge0),
\tag{23}
\]

with zero extension outside the actual side supports. The change of variables

\[
x=\alpha-u,
\qquad
x+h=\beta+y,
\qquad
h=L+u+y
\tag{24}
\]

has unit Jacobian from `(x,h)` to `(u,y)`. Hence the positive term in (22) is exactly

\[
\boxed{
\int_L^{h_0}w(h)J_{\alpha,\beta}(h)\,dh
=
\langle f_R,T_Lf_L\rangle.
}
\tag{25}
\]

The support condition in (6) shows that only `u,y<h_0-L` can contribute, which is precisely the collar restriction in (8). Therefore

\[
\langle f_R,T_Lf_L\rangle
\le
\Theta(L)
\sqrt{m_L^{\rm col}(L)m_R^{\rm col}(L)}.
\tag{26}
\]

Combining (21), (22), and (26) proves (9). No generic convolution majorant has yet been used: `\Theta(L)` is the exact aperture-independent `L^2` operator coefficient of the positive Suzuki cross-gap source.

## 2. Young and Hilbert--Schmidt bounds give two explicit envelopes

Write

\[
k_L(s)=w(L+s)\mathbf1_{(0,h_0-L)}(s).
\tag{27}
\]

Then `T_L` is the Hankel operator with kernel `k_L(u+y)`. Reflection turns it into a one-sided convolution restriction, so the endpoint Young inequality gives

\[
\|T_L\|\le\|k_L\|_1
=\int_0^{h_0-L}w(L+s)ds
=B(L),
\tag{28}
\]

which recovers the coefficient used in `WI-272` but now identifies it as only an upper bound for the true operator norm.

For `L>0`, `k_L` is bounded and compactly supported. Direct integration gives

\[
\begin{aligned}
\|T_L\|_{\rm HS}^2
&=\int_0^\infty\int_0^\infty
k_L(u+y)^2\,du\,dy\\
&=\int_0^{h_0-L}s\,w(L+s)^2ds\\
&=\int_L^{h_0}(h-L)w(h)^2dh.
\end{aligned}
\tag{29}
\]

Thus `\Theta(L)\le H(L)`, proving the second term in (12). This identity is just the standard Hilbert--Schmidt calculation for an integral Hankel kernel; no zeta-specific theorem is hidden in it.

Using `w(h)=c(h_0-h)+O((h_0-h)^2)` from the exact derivative in `WI-272`, with `\varepsilon=h_0-L`, one obtains

\[
H(L)^2
=c^2\int_0^\varepsilon s(\varepsilon-s)^2ds
+O(\varepsilon^5)
=\frac{c^2}{12}\varepsilon^4+O(\varepsilon^5),
\tag{30}
\]

which proves (19). Equation (18) is the `WI-272` tail expansion. Hence

\[
\frac{H(L)}{B(L)}\longrightarrow\frac1{\sqrt3}
\qquad(L\uparrow h_0).
\tag{31}
\]

This is a genuine strengthening of the previously persisted below-`h_0` screening collar.

## 3. The exact source norm has the same sharp zero-gap wall as Carleman

For every `h>0`, `WI-270` established

\[
0<w(h)_+
<\frac1{2h}
\qquad(0<h<h_0).
\tag{32}
\]

Therefore for `s=u+y>0` and every `L\ge0`,

\[
0\le K_L(u,y)
\le\frac1{2(L+s)}
\le\frac1{2s}.
\tag{33}
\]

The last kernel is one half of the classical Carleman operator

\[
(Cf)(u)=\int_0^\infty\frac{f(y)}{u+y}dy,
\tag{34}
\]

whose `L^2(\mathbb R_+)` norm is `\pi`. Consequently

\[
\Theta(L)\le\frac\pi2.
\tag{35}
\]

For every fixed `L>0`, `T_L` is Hilbert--Schmidt and hence compact. Its kernel is nonnegative, so the operator norm can be tested on a nonnegative maximizing eigenfunction. For every nonzero nonnegative `f`, the first inequality in

\[
\langle f,T_Lf\rangle
<\frac12\langle f,Cf\rangle
\le\frac\pi2\|f\|_2^2
\tag{36}
\]

is strict: `L>0` makes `K_L(u,y)<1/(2(u+y))` almost everywhere on every positive-measure product set where `f(u)f(y)>0`, while outside the positive-source triangle the left kernel vanishes. Compactness turns this pointwise strictness into

\[
\boxed{\Theta(L)<\pi/2\qquad(L>0).}
\tag{37}
\]

The case `L=0` is different because the kernel keeps the Carleman singularity. From the exact expansion already used in `WI-272`,

\[
w(h)=\frac1{2h}+O(1)
\qquad(h\downarrow0).
\tag{38}
\]

The upper bound `\Theta(0)\le\pi/2` follows from (33). For the reverse inequality, let `f\in C_c(0,\infty)` be a nonnegative normalized Carleman near-extremizer. Such functions can approximate the Carleman norm because `C_c(0,\infty)` is dense and the positive kernel permits passage to absolute values. Under the unitary dilation

\[
(U_\delta f)(x)=\delta^{-1/2}f(x/\delta),
\tag{39}
\]

the `T_0` quadratic form becomes

\[
\langle U_\delta f,T_0U_\delta f\rangle
=
\iint
f(s)f(t)
\,\delta w(\delta(s+t))
\mathbf1_{\{\delta(s+t)<h_0\}}
\,ds\,dt.
\tag{40}
\]

On the compact support of `f`, (38) gives

\[
\delta w(\delta(s+t))
\longrightarrow\frac1{2(s+t)}.
\tag{41}
\]

Hence the right side of (40) tends to `\frac12\langle f,Cf\rangle`. Taking Carleman near-extremizers proves

\[
\boxed{\Theta(0)=\pi/2.}
\tag{42}
\]

Finally, as `L\downarrow0`, the nonnegative kernels `K_L` increase pointwise to `K_0` because `w` is strictly decreasing on `(0,h_0)` and the support triangle expands. For every fixed nonnegative test function, monotone convergence therefore gives convergence of its quadratic forms. Testing against `T_0` near-extremizers and combining with (35) yields

\[
\boxed{\lim_{L\downarrow0}\Theta(L)=\pi/2.}
\tag{43}
\]

This is the decisive negative part of the finding. The exact Suzuki positive-source kernel is strictly smaller than the Carleman majorant at every fixed positive distance, but the logarithmic diagonal singularity allows arbitrarily concentrated `L^2` profiles to recover the full Carleman norm as the gap closes. There is no uniform coefficient improvement hidden in the replacement `1/(2h) -> w(h)_+` alone.

## 4. Screening now forces adjacent collar concentration

Under complete prime screening, one-signedness gives `P_{\alpha,\beta}=0`. Equation (9) then implies the two inequalities (14). Their product is

\[
\Theta(L)^2m_L^{\rm col}m_R^{\rm col}
\ge
\lambda_{r_L}\lambda_{r_R}M_LM_R,
\tag{44}
\]

which is (15). Since each collar fraction is at most one, (44) immediately gives the necessary condition

\[
\Theta(L)^2\ge\lambda_{r_L}\lambda_{r_R}.
\tag{45}
\]

This retains more geometry than `WI-272`: a screened gap cannot pay the firstness tariff using mass arbitrarily far from its endpoints. The required positive-source payment must be physically present inside the two collars of width `h_0-L` adjacent to the gap. If either collar is depleted, the arithmetic source is forced to cross the gap even when the total side masses are large.

At `L=0`, the collar width is `h_0` and `\Theta(0)=\pi/2`; the mechanism reduces exactly to the sharp Carleman scale of `WI-270`. For every `L>0`, the exact coefficient is strictly smaller and the available collars are strictly shorter. Thus `WI-270`, `WI-271`, and `WI-272` fit into a single operator-norm interpolation:

\[
\text{gapless cut }(\pi/2)
\quad\rightsquigarrow\quad
\text{positive-width Hankel tariff }\Theta(L)
\quad\rightsquigarrow\quad
\text{pure prime tariff }(0)\text{ at }L\ge h_0.
\tag{46}
\]

The interpolation is useful but also exposes the precise remaining obstruction. A mass-only `L^2` estimate cannot generate a strict coefficient gain uniformly down to `L=0`; any such gain would contradict (42)--(43). To rule out the narrow-gap or gapless screened branch one needs information excluding the Carleman concentration sequences for an actual Suzuki null mode—for example regularity/translation constraints from the distributional null equation, compatibility across many cuts, or a source-adapted finite compression that retains more than total/collar `L^2` mass.

## 5. Prior-art and novelty audit

The zeta-specific input remains Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096, current manuscript version August 2026. Suzuki supplies the localized closed Weil form, its self-adjoint operator, and the source decomposition used through `WI-253`, `WI-269`, and `WI-271`. The present finding does not add a claim about Suzuki's operator construction.

The Carleman operator and the norm `\|C\|=\pi` are classical. A modern source is D. R. Yafaev, **Spectral and scattering theory for perturbations of the Carleman operator**, arXiv:1210.5709v2 (2012), which treats the Hankel kernel `1/(t+s)` and records the spectral edge `\pi`. Yafaev's later **Quasi-diagonalization of Hankel operators**, arXiv:1403.3941, is general Hankel-operator background. The Hilbert--Schmidt identity (29), Young bound (28), compactness for `L>0`, and dilation argument at `L=0` are rederived here rather than imported as specialized theorems.

A targeted search for Suzuki/Weil first-crossing arguments combined with Carleman or positive-tail Hankel operator norms located Suzuki's operator paper and general Carleman/Hankel literature, but no source stating the zeta-specific tariff (9), collar constraint (15), or the exact zero-gap calibration (42)--(43). Search absence is audit context only and is not a priority claim.

The new Mathia deduction is therefore not the operator theory itself. It is the identification of the **actual positive Suzuki cross-gap source** as the Hankel operator `T_L`, its insertion into the first-crossing gap identity, and the resulting two-sided conclusion: a strictly stronger positive-width screening criterion together with a sharp proof that the exact-kernel operator-norm route cannot uniformly beat the Carleman wall as `L\downarrow0`.

## Falsification and audit test

The finding is exact and contains no numerical certificate. A falsification should target one of the following load-bearing steps:

1. the change of variables (24) must convert the positive cross-gap integral exactly into the Hankel bilinear form (25), with no missing orientation or factor of two;
2. the kernel support `u+y<h_0-L` must imply precisely the collar masses (8);
3. the operator norm bound (26) must be applied to the same side profiles appearing in the firstness identity, not to unrelated test functions;
4. the Young and Hilbert--Schmidt calculations (28)--(29) must preserve the shift by `L`;
5. the Carleman comparison must use the exact inequality `w(h)_+<1/(2h)` and the classical norm `\pi`;
6. the proof of `\Theta(0)=\pi/2` must retain the unitary dilation factor `\delta`, so that `\delta w(\delta r)\to1/(2r)`;
7. complete screening may set `P_{\alpha,\beta}=0` only because `v\ge0`, exactly as in `WI-270`--`WI-272`.

If these checks hold, the barrier statement is sharp at the level claimed: no argument whose only replacement for the positive archimedean cross-gap term is its unrestricted `L^2` operator norm can gain a uniform constant below `\pi/2` at vanishing gap width.

## Consequence for the research line

The previously suggested escape from the divergent `B(L)` budget in `WI-272`—use the true source-conditioned operator norm—is partly successful and partly closed. It **does** remove the artificial logarithmic divergence, gives the stronger collar-sensitive tariff (9), and improves the near-`h_0` coefficient by at least a factor `1/sqrt(3)` at leading order through (19). But it **does not** solve the narrow-gap limit: the exact coefficient converges to `\pi/2`, the same sharp Carleman constant already present in `WI-270`.

The live one-signed gate is therefore narrower. A proof that complete prime screening is impossible must now exploit a property that Carleman near-extremizers do not satisfy but an actual first Suzuki null mode must satisfy—most plausibly compatibility of many overlapping cuts with the distributional null equation or a stronger source-conditioned finite-partition constraint. Replacing one generic norm bound by another is no longer a credible standalone route to zero defect.