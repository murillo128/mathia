# PC-345 — full-shell Mellin injectivity has a sharp Gamma-strip threshold

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the first natural exponential-growth escape beyond the tempered full-shell theorem PC-344.

PC-344 proves that the complete scalar Prime-Circle shell family has no hidden tempered null directions beyond the jets supported on zeros of the already explicit zeta factor. The next natural question is whether allowing fixed exponential growth can create additional scalar selectors. The Gamma factor supplies the intrinsic vertical envelope `exp(-pi|t|/2)`, so the relevant residual transform is analytic in a horizontal strip whose critical half-width is `pi/2`.

For the natural residual weighted-`L^2` class below, that threshold is **sharp on every Mellin line `sigma>0`**, not only in the zero-free half-plane. At and above half-width `pi/2`, the complete shell response is injective on ordinary measurable selectors modulo almost-everywhere equality. At every strict smaller width, the nullspace is infinite-dimensional. The threshold is therefore independent of whether the chosen vertical line contains zeta zeros.

This strengthens the negative interpretation. Ordinary function selectors at the full Gamma width do not see the point-supported zeta-zero directions of PC-344 at all; those directions require distributions. Once any fixed amount of the Gamma width is lost, non-zeta Hardy/Blaschke interpolation ghosts appear everywhere, including on zero-free lines.

## 1. Exact shell reduction leaves one apparent `n=1` interpolation mode

Fix

\[
\sigma>0,\qquad \beta:=1-\sigma,
\tag{1}
\]

and retain the exact signed-radial Mellin factorization from PC-179,

\[
\mathcal R_n(\sigma+it)
=U_\sigma(t)A_n(t),
\qquad
U_\sigma(t):=-\Gamma(\sigma+it)\zeta(\sigma+it),
\tag{2}
\]

where

\[
A_n(t)
=\sum_{d\mid n}\mu(n/d)d^{\beta-it}.
\tag{3}
\]

All identities in this finding are understood almost everywhere in `t`. For `0<sigma<1`, the real zeros of `U_sigma` are isolated zeta zeros; at `sigma=1`, `U_1` has the isolated pole at `t=0`; for `sigma>1`, it is finite and nonzero everywhere. Since the selector class below consists of ordinary measurable functions modulo almost-everywhere equality, changing values on this discrete exceptional set has no effect on the class or on any response integral.

For `b>0`, define

\[
\mathcal X_{\sigma,b}
:=\left\{T:\ S(t):=U_\sigma(t)T(t),\quad
 e^{b|t|}S(t)\in L^2(\mathbb R)\right\}.
\tag{4}
\]

This is deliberately a class **after multiplication by the source-forced universal shell factor** `U_sigma`; it is a boundary classification, not a proposal for a new normalized observable. Conversely, every measurable `S` in the weighted space determines an almost-everywhere class `T=S/U_sigma` by dividing off the discrete exceptional set and assigning arbitrary values there.

Since `b>0`, Cauchy--Schwarz gives `S in L^1(R)`. Every shell response is therefore absolutely defined by

\[
L_T(n)
:=\int_{\mathbb R}T(t)\mathcal R_n(\sigma+it)\,dt
=\int_{\mathbb R}S(t)A_n(t)\,dt.
\tag{5}
\]

Use the Fourier convention

\[
f(x):=\widehat S(x)
=\int_{\mathbb R}S(t)e^{-itx}\,dt.
\tag{6}
\]

Then

\[
L_T(n)
=\sum_{d\mid n}\mu(n/d)d^\beta f(\log d).
\tag{7}
\]

Set

\[
g(d):=d^\beta f(\log d).
\tag{8}
\]

Equation (7) is simply

\[
L_T=\mu*g
\tag{9}
\]

on the divisor semigroup. If `L_T(n)=0` for every `n>1`, then

\[
\mu*g=c\varepsilon,
\qquad c=g(1)=f(0),
\tag{10}
\]

where `epsilon` is the Dirichlet-convolution identity. Convolving with the constant-one arithmetic function gives

\[
g(d)=c\qquad(d\ge1),
\tag{11}
\]

hence the exact interpolation law

\[
\boxed{
f(\log d)=c\,d^{-\beta}=c\,d^{\sigma-1}
\qquad(d=1,2,3,\ldots).
}
\tag{12}
\]

Thus

\[
\boxed{
L_T(n)=0\ \forall n>1
\iff
f(\log m)=f(0)m^{\sigma-1}\ \forall m\ge1.
}
\tag{13}
\]

For `sigma>1`, Riemann--Lebesgue immediately forces `c=0`, which was enough for the zero-free control. For `0<sigma<=1`, the sampled values in (12) are bounded or decaying, so Riemann--Lebesgue does **not** remove this apparent missing-`n=1` mode. The critical-width argument must kill it analytically rather than assume it away.

## 2. The residual envelope is exactly a Hardy strip

For `z=x+iy` with `|y|<b`, equation (6) continues holomorphically as

\[
f(z)=\int_{\mathbb R}S(t)e^{-itz}\,dt.
\tag{14}
\]

Plancherel gives

\[
\int_{\mathbb R}|f(x+iy)|^2\,dx
=2\pi\int_{\mathbb R}|S(t)|^2e^{2ty}\,dt.
\tag{15}
\]

Consequently

\[
\boxed{
e^{b|t|}S(t)\in L^2(\mathbb R)
\iff
f\in H^2(S_b),
\qquad
S_b:=\{z:|\operatorname{Im}z|<b\},
}
\tag{16}
\]

with equivalent norms.

Map `S_b` conformally to the disk by

\[
w=\phi_b(z)
:=\tanh\!\left(\frac{\pi z}{4b}\right).
\tag{17}
\]

The logarithmic integer samples become

\[
w_m
=\phi_b(\log m)
=\frac{m^\alpha-1}{m^\alpha+1},
\qquad
\alpha:=\frac{\pi}{2b},
\tag{18}
\]

so

\[
1-w_m=\frac{2}{m^\alpha+1}.
\tag{19}
\]

The convergence or divergence of this single Blaschke sum is the sharp width boundary.

## 3. The full Gamma width kills the nonzero interpolation mode for every `sigma>0`

Take first

\[
b=\frac\pi2.
\tag{20}
\]

Let `f in H^2(S_b)` satisfy the null interpolation law (12), put `c=f(0)`, and define

\[
G(z):=e^{\beta z}f(z)-c.
\tag{21}
\]

Then

\[
\boxed{G(\log m)=0\qquad(m=1,2,3,\ldots).}
\tag{22}
\]

Although `G` need not itself belong to `H^2`, it has far too little boundary growth to support this zero set unless it vanishes identically. To see this directly, fix `a<b` and write

\[
\delta:=b-a.
\tag{23}
\]

The standard point-evaluation estimate for a Hardy strip follows from the subharmonic mean-value inequality on a disk of radius comparable to `delta`:

\[
\sup_{|y|\le a,\ x\in\mathbb R}|f(x+iy)|
\le C\delta^{-1/2}\|f\|_{H^2(S_b)}.
\tag{24}
\]

Choose an integer `M>2|beta|+2` and remove the harmless real-direction exponential by

\[
H(z):=
\frac{G(z)}{(2\cosh(z/2))^M}.
\tag{25}
\]

For `|Im z|<=pi/2`,

\[
|2\cosh(z/2)|^2
=2(\cosh(\operatorname{Re}z)+\cos(\operatorname{Im}z))
\ge2\cosh(\operatorname{Re}z),
\tag{26}
\]

so the denominator dominates `e^{M|Re z|/2}` uniformly up to the critical strip. Equations (24)--(26) give

\[
H\in H^\infty(S_a),
\qquad
\boxed{
\log\|H\|_{H^\infty(S_a)}
=O\!\left(\log\frac1\delta\right)
}
\tag{27}
\]

as `a` tends to `pi/2`.

If `H` were nonzero, choose a fixed real `x_0<0` with `H(x_0)!=0`. Under the strip-to-disk map for `S_a`, put

\[
\alpha_a:=\frac{\pi}{2a}>1.
\tag{28}
\]

The zeros `log m` map to `(m^{alpha_a}-1)/(m^{alpha_a}+1)`. The standard bounded-analytic zero-factor estimate used in PC-343 therefore gives

\[
\log\|H\|_{H^\infty(S_a)}
\ge
\log|H(x_0)|
+2e^{\alpha_a x_0}\bigl(\zeta(\alpha_a)-1\bigr).
\tag{29}
\]

As `a` approaches `pi/2`,

\[
\alpha_a-1\sim\frac{2\delta}{\pi},
\qquad
\zeta(\alpha_a)\sim\frac1{\alpha_a-1},
\tag{30}
\]

so (29) forces a lower bound of order `1/delta` for the logarithm of the norm, contradicting the merely logarithmic upper bound (27). Hence

\[
H\equiv0,
\qquad
G\equiv0.
\tag{31}
\]

Therefore

\[
f(z)=c e^{-\beta z}=c e^{(\sigma-1)z}.
\tag{32}
\]

No nonzero function of the form (32) belongs to `H^2(S_{pi/2})`: for `sigma>1` its square integral diverges as `x->+infinity`, for `0<sigma<1` it diverges as `x->-infinity`, and for `sigma=1` a nonzero constant is not square-integrable. Thus `c=0`, `f=0`, and Fourier injectivity gives `S=0`. Since `U_sigma` is nonzero almost everywhere, `T=0` as an almost-everywhere class.

We have proved

\[
\boxed{
\ker\left(T\mapsto(L_T(n))_{n>1}\right)
\cap\mathcal X_{\sigma,\pi/2}
=\{0\}
\qquad(\sigma>0).
}
\tag{33}
\]

The same conclusion holds for every `b>pi/2` by the inclusion `X_{sigma,b} subset X_{sigma,pi/2}`.

## 4. Every narrower strip has an infinite-dimensional kernel on every Mellin line

Now let

\[
0<b<\frac\pi2.
\tag{34}
\]

Then `alpha=pi/(2b)>1`, and (19) gives

\[
\sum_{m\ge1}(1-w_m)
=\sum_{m\ge1}\frac{2}{m^\alpha+1}
<\infty.
\tag{35}
\]

Thus `{w_m}` is a Blaschke sequence. There is a nonzero bounded analytic Blaschke product `B_b` on `S_b` whose zeros contain every `log m`. Choose `R>b` and put

\[
q_R(z):=\frac1{z^2+R^2}.
\tag{36}
\]

Then `q_R in H^2(S_b)`, and

\[
f_b(z):=B_b(z)q_R(z)
\tag{37}
\]

is a nonzero member of `H^2(S_b)` satisfying

\[
f_b(\log m)=0\qquad(m\ge1).
\tag{38}
\]

By (16), `f_b` is the Fourier transform of a nonzero `S_b(t)` with

\[
e^{b|t|}S_b(t)\in L^2(\mathbb R).
\tag{39}
\]

For **any** `sigma>0`, define `T_b=S_b/U_sigma` away from the discrete zero/pole set of `U_sigma` and assign arbitrary values on that set. Then `T_b` is a nonzero almost-everywhere class in `X_{sigma,b}`. Since `f_b(0)=0`, equation (13) holds with `c=0`, and therefore

\[
\boxed{
L_{T_b}(n)=0\qquad\forall n>1.
}
\tag{40}
\]

The kernel is infinite-dimensional. For distinct real `a_j`, the functions

\[
f_{b,a_j}(z):=e^{-ia_jz}f_b(z)
\tag{41}
\]

remain in `H^2(S_b)`, retain all zeros `log m`, and are linearly independent. Consequently

\[
\boxed{
\dim\ker\left(T\mapsto(L_T(n))_{n>1}\right)
\cap\mathcal X_{\sigma,b}
=\infty
\qquad(\sigma>0,\ 0<b<\pi/2).
}
\tag{42}
\]

Combining (33) and (42), the threshold is exact and independent of the Mellin line:

\[
\boxed{
\begin{array}{ll}
b\ge\pi/2:&\text{full-shell injectivity for every }\sigma>0,\\[2mm]
0<b<\pi/2:&\text{infinite-dimensional full-shell kernel for every }\sigma>0.
\end{array}}
\tag{43}
\]

## 5. Zeta zeros and Hardy ghosts live in different selector categories

The extension from `sigma>1` to the whole Mellin half-plane clarifies what the previous scalar nullspace results are actually measuring.

PC-344 works in `S'(R)`. On a line through a zeta zero, delta distributions and their allowed derivatives can be killed by multiplication with the universal factor `U_sigma`; those are the zeta-zero jets. The present class consists instead of ordinary functions modulo almost-everywhere equality. A discrete set of ordinates has measure zero, so point-supported information disappears. This is why (33) remains injective even if `Re(s)=sigma` passes through nontrivial zeta zeros.

Conversely, the subcritical nulls in (42) require no zeta zeros at all. Taking `sigma>1` still provides the decisive matched control: the same infinite-dimensional kernel exists in a half-plane where zeta is zero-free. Taking `sigma=1/2` changes nothing about the Hardy threshold. Thus neither side of (43) detects the critical line; the transition is caused solely by the density of the logarithmic sampling set relative to the Gamma strip.

Crossing from `b=pi/2` to `b=pi/2-delta` permits the residual selector to compensate roughly `e^{delta|t|}` of the Gamma decay, modulo polynomial factors. An arbitrarily small fixed exponential allowance is enough to create invisible scalar selectors.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. Hardy-space zero sets are governed by the Blaschke condition; bilateral Fourier/Laplace transforms with exponential `L^2` weights give Hardy spaces on strips through Paley--Wiener theory; point evaluation on a smaller Hardy strip follows from the elementary subharmonic mean-value estimate. Zen Harper, *Laplace transform representations and Paley-Wiener theorems for functions on vertical strips*, Documenta Mathematica 15 (2010), 235--254, DOI `10.4171/DM/296`, is a direct neighboring strip-transform reference. The zero-factor estimate at the critical boundary is the same standard Blaschke machinery already audited in PC-341 and PC-343.

A directed novelty check against Hardy-strip uniqueness sets, `{log n}` Blaschke interpolation, Müntz/exponential completeness, weighted Fourier uniqueness, and Gamma-weighted Mellin interpolation found the expected broad classical frameworks rather than an independent RH mechanism matching (43). No historical novelty is claimed for Paley--Wiener, Blaschke products, the point-evaluation estimate, or the convergence test `sum m^{-alpha}`.

The durable Prime-Circle delta is the exact combination forced by the shell divisor algebra. Full-shell nullity does **not** initially give zeros at every `log m` on lines `sigma<=1`; it gives the nonhomogeneous interpolation law (12). The critical Gamma width is nevertheless rigid enough to force the only analytic continuation of those samples to be the forbidden exponential `c e^{(sigma-1)z}`, which cannot lie in the Hardy strip unless `c=0`. Below the critical width, homogeneous Blaschke ghosts exist and work for every `sigma`.

No new `SOURCES.md` entry is needed: the load-bearing external machinery is the same classical Hardy/Paley--Wiener/Blaschke theory already used by the preceding scalar-Mellin findings.

## 7. Consequence for the Prime-Circle frontier

The first fixed-exponential enlargement beyond tempered selectors has now been classified throughout the original Mellin half-plane. There is no special recovery of injectivity, noninjectivity, or zero-sensitive structure on `Re(s)=1/2`: ordinary function selectors are injective at the full Gamma width on **all** vertical lines and acquire non-arithmetic interpolation ghosts on **all** vertical lines as soon as that width is narrowed.

This makes progressively larger scalar Mellin selector spaces an even weaker route toward an RH mechanism than the zero-free control alone suggested. The zeta-zero directions of PC-344 belong specifically to point-supported distributional structure; the exponential-growth ghosts of PC-345 belong to Hardy interpolation. Neither supplies a source-derived reason for the Riemann divisor or for the critical line.

A surviving continuation therefore needs structure outside this residual scalar-function classification: shell-dependent operators, nonlinear observables, matrix-valued/noncommuting carriers, or genuinely cross-shell/cross-level geometry before scalar Mellin evaluation. Merely moving the same scalar selector between vertical lines or weakening its exponential envelope cannot create the missing zero-sensitive mechanism.

## Audit / falsification tests

A counterexample to (43) is either (i) a nonzero `T in X_{sigma,pi/2}` for some `sigma>0` annihilating every shell, or (ii) a strict subcritical width `0<b<pi/2` and some `sigma>0` for which no nonzero full-shell null exists.

The load-bearing checkpoints are:

1. divisor convolution must give exactly the interpolation law `f(log m)=f(0)m^{sigma-1}` rather than silently setting the missing `n=1` mode to zero;
2. the weighted-`L^2` residual condition must be equivalent to `H^2` control on `|Im z|<b`;
3. at `b=pi/2`, the transformed difference `G(z)=e^{(1-sigma)z}f(z)-f(0)` must have only polynomial boundary-norm blow-up after the zero-free `cosh` normalization, while its integer-log zeros demand `exp(c/delta)` blow-up unless `G=0`;
4. the resulting exponential `f(z)=f(0)e^{(sigma-1)z}` must fail `H^2` unless `f(0)=0`;
5. for `b<pi/2`, the logarithmic samples must satisfy the Blaschke condition and produce a genuine nonzero `H^2` function vanishing at all `log m`;
6. the discrete zeros or pole of `U_sigma` must be irrelevant to ordinary almost-everywhere selector classes, so division by `U_sigma` off that set genuinely produces the subcritical examples on every vertical line.

Failure of any one of these checkpoints would destroy the claimed all-line sharp threshold. Within the stated residual function class, all six are exact.