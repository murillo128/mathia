# PC-343 — full-shell Mellin-measure kernel is exactly zeta-zero support

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the arbitrary finite-measure scalar Mellin escape left beyond PC-339--PC-342 when one requires the full shell response rather than only mixed-semiprime nulls.

PC-339--PC-341 show that mixed-semiprime nulls collapse a finite-measure selector when the induced prime-log interpolation function has enough control on the full Gamma strip `|Im z|<pi/2`; PC-342 records that arbitrary analytic survivors outside that growth class do exist. The full Prime-Circle shell family is much more rigid. Divisor inversion turns all-shell nulls into zeros at **every** `log m`, not merely at prime logarithms. The resulting zero set is too dense for the boundary growth supplied by any finite Mellin-frequency measure.

Fix `sigma>0` and a finite complex Borel measure `T` on the frequency line. With PC-179 notation,

\[
\mathcal R_n(s)
=-\Gamma(s)\zeta(s)
 n^{1-s}\prod_{p\mid n}(1-p^{s-1})
=:U(s)A_n(s),
\tag{1}
\]

define

\[
L_{\sigma,T}(n)
:=\int_{\mathbb R}\mathcal R_n(\sigma+it)\,dT(t).
\tag{2}
\]

Let

\[
Z_\sigma:=\{t\in\mathbb R:\zeta(\sigma+it)=0\}.
\tag{3}
\]

Then the exact finite-measure nullspace is

\[
\boxed{
\begin{aligned}
\sigma\ne1:\quad
&L_{\sigma,T}(n)=0\ \forall n>1
\iff \operatorname{supp}T\subseteq Z_\sigma,\\
\sigma=1:\quad
&L_{1,T}(n)=0\ \forall n>1
\iff T=0.
\end{aligned}}
\tag{4}
\]

In particular, for `sigma>1` the full shell transform is injective on finite measures. In the critical strip its only null directions are measures supported on ordinates of the **already present universal zeta factor**. At the exceptional endpoint line `sigma=1`, pole cancellation removes even that nullspace.

A useful corollary is the exact uniqueness of the classical Mangoldt selector:

\[
\boxed{
L_{1,T}(n)=c\Lambda(n)\quad\forall n>1
\Longrightarrow
T=c\delta_0.
}
\tag{5}
\]

Thus an arbitrary finite global Mellin measure, even one violating every boundary-moment hypothesis of PC-339/PC-340 and lying outside the bounded-characteristic hypothesis of PC-341, cannot reproduce the complete Prime-Circle Mangoldt response by a second non-endpoint construction.

## 1. Divisor inversion upgrades prime-log interpolation to all integer logarithms

The cyclotomic factor has the equivalent divisor form

\[
A_n(s)=\sum_{d\mid n}\mu(n/d)d^{1-s}.
\tag{6}
\]

Ordinary divisor inversion therefore gives, for every integer `m>=2`,

\[
\sum_{d\mid m}A_d(s)=m^{1-s},
\qquad
\boxed{
\sum_{\substack{d\mid m\\d>1}}A_d(s)=m^{1-s}-1.
}
\tag{7}
\]

Put

\[
\beta:=1-\sigma,
\qquad
V_\sigma(t):=(\beta-it)U(\sigma+it).
\tag{8}
\]

When `sigma=1`, the apparent singularity at `t=0` is removable: since `U(s)=-Gamma(s)zeta(s)` has residue `-1` at `s=1`,

\[
V_1(0)=1.
\tag{9}
\]

For complex `z`, define

\[
\Psi_z(t)
:=
\frac{e^{(\beta-it)z}-1}{\beta-it},
\tag{10}
\]

with the removable value `Psi_z(0)=z` in the sole case `beta=t=0`, and set

\[
F_T(z):=\int_{\mathbb R}V_\sigma(t)\Psi_z(t)\,dT(t).
\tag{11}
\]

For real `z=log m`, equations (7)--(11) give exactly

\[
\boxed{
F_T(\log m)
=
\sum_{\substack{d\mid m\\d>1}}L_{\sigma,T}(d).
}
\tag{12}
\]

Hence all-shell nulls force

\[
\boxed{F_T(\log m)=0\qquad(m=2,3,4,\ldots).}
\tag{13}
\]

This is the extra rigidity absent from the semiprime-only problem: the zero set is the logarithm of **all** positive integers.

## 2. Gamma decay gives only polynomial boundary blow-up for every finite measure

For fixed `sigma>0`, Stirling's formula for `Gamma(s)` together with any standard polynomial vertical-line bound for `zeta(s)` gives constants `C,B` such that

\[
|V_\sigma(t)|
\le C(1+|t|)^B e^{-\pi|t|/2}
\qquad(t\in\mathbb R).
\tag{14}
\]

At `sigma=1`, the factor `1-s` in (8) has already removed the zeta pole, so the same estimate holds globally.

Consequently `F_T` is holomorphic on the full open Gamma strip

\[
S_{\pi/2}=\{z:|\operatorname{Im}z|<\pi/2\}.
\tag{15}
\]

Indeed, for every `a<pi/2`, the integral representation

\[
\Psi_z(t)=\int_0^z e^{(\beta-it)w}\,dw
\tag{16}
\]

gives

\[
|F_T(z)|
\le
\|T\|\,|z|e^{|\beta||\operatorname{Re}z|}
K_\sigma(a),
\qquad
K_\sigma(a):=
\sup_t e^{a|t|}|V_\sigma(t)|.
\tag{17}
\]

Writing

\[
\delta:=\frac\pi2-a,
\tag{18}
\]

equation (14) implies, for some finite exponent `N_sigma`,

\[
\boxed{K_\sigma(a)=O_\sigma(\delta^{-N_\sigma}).}
\tag{19}
\]

Choose an integer `M>2|beta|+2` and remove the harmless real-direction growth by

\[
H(z):=
\frac{F_T(z)}{(2\cosh(z/2))^M}.
\tag{20}
\]

The denominator has no zero in `|Im z|<=pi/2`, and the quotient of the elementary factor in (17) by `(2cosh(z/2))^M` is uniformly bounded there. Thus

\[
H\in H^\infty(S_a)
\qquad(a<\pi/2)
\tag{21}
\]

and, crucially,

\[
\boxed{
\log\|H\|_{H^\infty(S_a)}
=O_\sigma\!\left(\log\frac1\delta\right)
\quad(a\uparrow\pi/2).
}
\tag{22}
\]

No exponential moment of `T` is assumed. The Gamma factor itself is enough to force this merely polynomial approach to the strip boundary.

## 3. Zeros at every `log m` force essential-exponential boundary growth

Assume for contradiction that `H` is nonzero. Choose one fixed real `x_0<0` with `H(x_0) != 0`. For `a<pi/2`, map `S_a` to the disk by

\[
\phi_a(z)=\tanh\!\left(\frac{\pi z}{4a}\right),
\qquad
\alpha:=\frac{\pi}{2a}>1.
\tag{23}
\]

The zeros `z_m=log m` become

\[
\phi_a(\log m)
=\frac{m^\alpha-1}{m^\alpha+1}.
\tag{24}
\]

Because `alpha>1`, they form a Blaschke sequence in every strictly narrower strip. Applying the standard bounded-analytic zero-factor inequality at the point `x_0` gives

\[
\log\|H\|_{H^\infty(S_a)}
\ge
\log|H(x_0)|
+
\sum_{m=2}^\infty
\log\coth\!\left(
\frac{\alpha(\log m-x_0)}2
\right).
\tag{25}
\]

For `0<y<1`,

\[
\log\frac{1+y}{1-y}\ge2y.
\tag{26}
\]

Taking `y=e^{\alpha x_0}m^{-\alpha}` in (25) therefore yields

\[
\boxed{
\log\|H\|_{H^\infty(S_a)}
\ge
\log|H(x_0)|
+2e^{\alpha x_0}\bigl(\zeta(\alpha)-1\bigr).
}
\tag{27}
\]

As `a` tends to `pi/2`,

\[
\alpha-1\sim\frac{2\delta}{\pi},
\qquad
\zeta(\alpha)\sim\frac1{\alpha-1},
\tag{28}
\]

so (27) forces

\[
\boxed{
\log\|H\|_{H^\infty(S_a)}
\ge
\frac{\pi e^{x_0}+o(1)}{\delta}.
}
\tag{29}
\]

Thus any nonzero survivor with all integer-log zeros must have **essential-exponential** norm blow-up `exp(c/delta)` as the Gamma boundary is approached. Equation (22) allows only polynomial blow-up. The two bounds are incompatible, hence

\[
\boxed{F_T\equiv0.}
\tag{30}
\]

This is stronger than the prime-log situation of PC-341. Prime logs contribute the prime-zeta divergence `sum_p p^{-alpha} ~ log(1/(alpha-1))`, whereas all integer logs contribute `zeta(alpha) ~ 1/(alpha-1)`. The full shell family therefore upgrades a polynomial lower blow-up to an essential-exponential one.

## 4. Fourier uniqueness leaves exactly the inherited zeta-zero support

Differentiate (11). For real `x`,

\[
F_T'(x)
=e^{\beta x}
\int_{\mathbb R}
e^{-itx}V_\sigma(t)\,dT(t).
\tag{31}
\]

Since `F_T=0`, the Fourier transform of the finite measure

\[
d\eta(t):=V_\sigma(t)\,dT(t)
\tag{32}
\]

vanishes identically. Fourier uniqueness gives `eta=0`. Hence `T` is supported on the real zero set of `V_sigma`.

If `sigma!=1`, the factor `beta-it` never vanishes for real `t`, `Gamma` has no zeros, and therefore

\[
\{t:V_\sigma(t)=0\}
=Z_\sigma.
\tag{33}
\]

Conversely, a measure supported on `Z_sigma` annihilates every shell because the common factor `zeta(s)` in (1) vanishes there. This proves the first line of (4).

If `sigma=1`, equation (9), the absence of Gamma zeros, and the classical zero-free theorem `zeta(1+it)!=0` for real `t!=0` show that `V_1` has no real zero at all. Thus `eta=0` implies `T=0`, proving the second line of (4).

Finally, PC-179 gives

\[
\mathcal R_n(1)=\Lambda(n).
\tag{34}
\]

So if `L_{1,T}=c Lambda`, then `T-c delta_0` lies in the trivial nullspace (4), proving (5).

## 5. Prior-art and novelty audit

Every external analytic ingredient is classical. The bounded-function zero-factor/Blaschke step is the same disk theory audited in PC-341; W. K. Hayman, **Identity Theorems for Functions of Bounded Characteristic**, *Journal of the London Mathematical Society* 58 (1998), 127--140, DOI `10.1112/S0024610798006334`, is an explicit nearby reference for the canonical factorization and Blaschke zero condition. Stirling decay for Gamma, polynomial vertical-line bounds for zeta, the pole and zero-free line at `Re(s)=1`, and uniqueness of Fourier transforms of finite measures are standard classical analysis/analytic-number-theory inputs.

A directed search against Blaschke uniqueness for logarithms of integers, Müntz/exponential completeness, Fourier-Stieltjes measure uniqueness, and Gamma-weighted interpolation did not locate an independent RH mechanism matching (4). Neighboring completeness theories such as Müntz--Szász and exponential-system completeness are broader classical approximation frameworks, not evidence that the Prime-Circle nullspace classification itself is historically new. No novelty claim is made for those ingredients.

The line-local delta is the combination forced by the exact cyclotomic divisor family: **all shell responses convert to the zero set `{log 2, log 3, ...}`, whose boundary-growth demand is exponentially stronger than the Gamma-weighted transform of any finite measure can supply.** This leaves the universal zeta factor as the only possible all-shell nullspace in the critical strip.

That statement must not be promoted as an independent RH criterion. For `0<sigma<1`, saying that the map `T -> (L_{sigma,T}(n))_{n>1}` is noninjective exactly when the vertical line contains a zeta zero is a faithful kernel classification, but its noninjective directions are precisely atoms/measures on zeros of the zeta factor already explicit in (1). It is therefore an inherited reformulation, not a new spectral explanation of the zeros.

## 6. Consequences and boundary

This closes a specific loophole left by PC-339--PC-342: **arbitrarily bad critical-boundary behavior of a finite scalar Mellin measure cannot create a second exact all-shell Mangoldt selector.** At `sigma=1`, the endpoint distribution `delta_0` is not merely one solution; it is the unique finite-measure solution.

The quantifier strengthening is essential. PC-343 does **not** say that semiprime nulls alone determine an arbitrary finite measure without the growth hypotheses of PC-339--PC-341. Prime-log zeros have only logarithmic Blaschke divergence at the critical width, and PC-342 correctly leaves faster-growth survivors outside those theorems. Here the decisive input is the response on every shell, which supplies every integer logarithm through (12).

The theorem also does not classify infinite-order distributions, non-measure functionals, shell-dependent symbols, nonlinear operations, matrix-valued/noncommuting carriers, or genuinely cross-shell/cross-level geometry before scalar Mellin evaluation. Those remain outside the finite scalar-measure nullspace result.

For the RH objective, the conclusion is negative but useful: taking the complete family of scalar signed-radial Mellin responses does retain enough information to determine a finite measure modulo the **known common zeta zeros**, but it does not manufacture new zero-sensitive structure beyond that universal factor.

## Audit / falsification tests

The claim can be falsified by any finite complex measure `T` not supported on `Z_sigma` (or any nonzero `T` when `sigma=1`) for which all `L_{sigma,T}(n)` vanish. Equations (7)--(33) exclude such an example.

The load-bearing checkpoints are:

1. divisor inversion must give exactly (7), hence all integer-log zeros (13);
2. the source multiplier `V_sigma` must have only Gamma-critical exponential decay times polynomial growth, yielding the polynomial boundary bound (22);
3. the disk Blaschke product estimate must give (25), and the full integer zero set must force the `zeta(alpha)` lower bound (27);
4. the asymptotics in (28) must turn that lower bound into `exp(c/delta)`, contradicting (22);
5. after `F_T=0`, Fourier uniqueness must reduce the kernel exactly to the zero set of `V_sigma`, with the removable endpoint value (9) handled before invoking the zero-free line.

The theorem is intentionally not stated with only semiprime controls; dropping the all-shell hypothesis removes the `zeta(alpha)` divergence and returns to the genuinely open faster-growth regime isolated by PC-341/PC-342.