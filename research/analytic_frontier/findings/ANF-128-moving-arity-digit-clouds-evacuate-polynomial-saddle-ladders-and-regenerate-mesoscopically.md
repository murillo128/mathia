# ANF-128 — moving-arity digit clouds evacuate polynomial saddle ladders and regenerate mesoscopically

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + EXPONENTIAL-TRANSLATION-CLOUD + MOVING-ARITY + POLYNOMIAL-DEPTH-SADDLE-LADDER + MESOSCOPIC-TRANSPORT + FIXED-NOTCH-DARK + CASCADE-GATE`. `ANF-126` makes subexponential growing mirrors excisable, while `ANF-127` shows that any positive exponential unsigned-budget rate can cancel one saddle and regenerate source in a second chamber. The remaining question is how much of an exponential cancellation cascade can be excluded by tracking progressively more spectral chambers. The construction below shows that even a polynomial-depth **arithmetic ladder** of natural Gaussian checkpoints can be evacuated by one moving-arity digit layer while essentially all coherent source growth is regenerated in a nearby mesoscopic chamber. It does not claim invisibility to an arbitrary polynomially chosen checkpoint set.

Fix an `ANF-115` packet family with interior saddle `a=a_gamma`. For exponents `lambda>0` and `sigma>=0` satisfying

\[
\boxed{2\lambda+\sigma<\frac12,}
\tag{1}
\]

and for every prescribed exponential unsigned-budget rate `rho>0`, there is an explicit positive cloud of translated copies with

\[
\frac1A\log\mathcal U_A\to\rho
\]

that simultaneously suppresses `A^{sigma+o(1)}` pairwise disjoint natural Gaussian chambers arranged in an arithmetic ladder, spread across a spectral interval of length `Theta(A^{-lambda})`, by `exp(-kappa A+o(A))`, while a coherent chamber at distance `Theta(A^{-lambda})` from the original saddle carries source energy `exp((2rho+o(1))A)` relative to one packet. The suppression exponent is

\[
\boxed{
\kappa_{\lambda,\sigma,\rho}
=
\frac{2\rho}{\lambda+\sigma}
\left(\frac12-2\lambda-\sigma\right)>0.
}
\tag{2}
\]

Within this repeated moving-arity geometric-sum family, the line `2 lambda + sigma = 1/2` is sharp on the `A`-exponential scale. In the one-root-depth case `sigma=0`, this gives an internal quarter-power frontier: a single layer can transport its coherent reservoir by `A^{-lambda}` while exponentially evacuating the original natural Gaussian saddle chamber exactly when `lambda<1/4`. This is a sharp boundary for the explicit digit construction, **not** a universal `A^{-1/4}` obstruction for arbitrary physical clouds.

## 1. Moving arity creates a mesoscopic root ladder

Fix `gamma>0` and let

\[
P_A:=P_{A,\lfloor\gamma A\rfloor}
\]

be the `ANF-115` packet. Write

\[
E_A:=E_0(P_A),
\qquad
a:=a_\gamma\in(0,1),
\qquad
F(\alpha):=F_\gamma(\alpha),
\qquad
f:=F(a),
\tag{3}
\]

where `F'(a)=0` and `F''(a)<0`. Choose `lambda>0`, `sigma>=0` satisfying (1), put

\[
\theta:=\lambda+\sigma<\frac12,
\tag{4}
\]

and choose integers

\[
q_A=A^{\theta+o(1)},
\qquad
s_A=A^{\sigma+o(1)},
\qquad
1\le s_A<\frac{q_A}{2}.
\tag{5}
\]

For `sigma=0` one may take `s_A=1`. Define

\[
\beta_A:=\frac{a}{1-2s_A/q_A},
\qquad
d_A:=\frac1{\beta_A}=\frac{1-2s_A/q_A}{a}.
\tag{6}
\]

Since `s_A/q_A=A^{-lambda+o(1)}`, we have `beta_A<1` for large `A` and

\[
\beta_A-a=2aA^{-\lambda+o(1)}.
\tag{7}
\]

Let

\[
D_q(x):=\sum_{v=0}^{q-1}e^{-2\pi i v x}.
\tag{8}
\]

For each integer `r` with `s_A<=r<=2s_A`, introduce

\[
a_{r,A}:=\beta_A\left(1-\frac r{q_A}\right).
\tag{9}
\]

Then

\[
a_{r,A}d_A=1-\frac r{q_A},
\qquad
D_{q_A}(a_{r,A}d_A)=0,
\tag{10}
\]

and the original saddle is the last root in this ladder:

\[
a_{2s_A,A}=a.
\tag{11}
\]

There are `s_A+1=A^{sigma+o(1)}` centers. Their adjacent spacing is

\[
a_{r,A}-a_{r+1,A}
=\frac{\beta_A}{q_A}
=A^{-(\lambda+\sigma)+o(1)},
\tag{12}
\]

while the full ladder has diameter

\[
a_{s_A,A}-a
=\Theta\!\left(\frac{s_A}{q_A}\right)
=\Theta(A^{-\lambda}).
\tag{13}
\]

Because `theta<1/2`, the spacing (12) is much larger than the natural Gaussian width `A^{-1/2}`. Fixed-width Gaussian chambers around all these roots are therefore pairwise disjoint even though the whole ladder contracts mesoscopically toward `a`.

## 2. A positive physical cloud realizes the repeated digit exactly

Fix `rho>0` and let

\[
h_A:=\left\lfloor\frac{\rho A}{\log q_A}\right\rfloor.
\tag{14}
\]

Choose positive spacings

\[
d_{\ell,A}=d_A+O(A^{-10}),
\qquad 1\le\ell\le h_A,
\tag{15}
\]

so that every translated physical point below is distinct. As in `ANF-127`, this can be done inductively: after finitely many earlier digits have been fixed, every possible new collision excludes only finitely many values of the next spacing, so an arbitrarily small interval around `d_A` contains an admissible value.

For `v=(v_1,...,v_{h_A})` with `0<=v_ell<q_A`, set

\[
\tau_v:=\sum_{\ell=1}^{h_A}v_\ell d_{\ell,A}
\]

and form

\[
T_A
:=
\bigsqcup_{v\in\{0,\ldots,q_A-1\}^{h_A}}
(P_A+\tau_v).
\tag{16}
\]

Its number of copies and unsigned Hilbert budget satisfy

\[
R_A=q_A^{h_A}
=\exp((\rho+o(1))A),
\qquad
\mathcal U_A=R_A,
\qquad
\frac1A\log\mathcal U_A\to\rho.
\tag{17}
\]

The horizontal span is only polynomial,

\[
\operatorname{span}_x(T_A)
=O(h_Aq_A)
=A^{1+\theta+o(1)},
\tag{18}
\]

and translation gives the exact modulation factorization

\[
S_{T_A}(\alpha)
=p_A(\alpha)S_{P_A}(\alpha),
\qquad
p_A(\alpha)
=
\prod_{\ell=1}^{h_A}
D_{q_A}(\alpha d_{\ell,A}).
\tag{19}
\]

No signed coefficients, abstract Hilbert vectors, or nonphysical weights enter the construction.

## 3. Every Gaussian chamber in the arithmetic ladder is exponentially evacuated

The geometric sum has the closed form

\[
D_q(x)
=e^{-\pi i(q-1)x}\frac{\sin(\pi qx)}{\sin(\pi x)}.
\tag{20}
\]

At the root `x_r=1-r/q`,

\[
|D_q'(x_r)|
=
\frac{\pi q}{\sin(\pi r/q)}
=(1+o(1))\frac{q^2}{r}
\tag{21}
\]

uniformly for `s_A<=r<=2s_A`, because `s_A/q_A=A^{-lambda+o(1)}->0`.

Fix `S>0` and let

\[
B_{r,A}(S)
:=
\left\{
\alpha:
\bigl||\alpha|-a_{r,A}\bigr|
\le\frac S{\sqrt A}
\right\}.
\tag{22}
\]

The conditions `q_A=o(sqrt A)` and (15) keep the numerator in (20) in its linear regime and the denominator comparable to `r/q_A`. Uniformly in `r`, `ell`, and `alpha in B_{r,A}(S)`,

\[
|D_{q_A}(\alpha d_{\ell,A})|
\le
C_S\frac{q_A^2}{s_A\sqrt A}.
\tag{23}
\]

Hence

\[
\sup_{\alpha\in B_{r,A}(S)}|p_A(\alpha)|^2
\le
\left(
C_S\frac{q_A^4}{s_A^2A}
\right)^{h_A}.
\tag{24}
\]

Since

\[
4\log q_A-2\log s_A-\log A
=
(4\lambda+2\sigma-1+o(1))\log A,
\tag{25}
\]

and `h_A/A=(rho+o(1))/log q_A`, we obtain

\[
\frac1A
\log
\sup_{B_{r,A}(S)}|p_A|^2
\le
-\kappa_{\lambda,\sigma,\rho}+o(1).
\tag{26}
\]

Therefore

\[
\boxed{
\sup_{s_A\le r\le2s_A}
\frac{E_{B_{r,A}(S)}(T_A)}{E_A}
\le
\exp\bigl(-(\kappa_{\lambda,\sigma,\rho}+o(1))A\bigr).
}
\tag{27}
\]

There are only `A^{sigma+o(1)}` pairwise disjoint chambers, so their union has the same exponential suppression rate. Thus one layer can evacuate a polynomial-depth root lattice of complete natural Gaussian chambers across a mesoscopic interval.

The phase line is sharp for this digit family. At the original saddle `a=a_{2s_A,A}`, take a fixed off-center Gaussian subwindow

\[
\alpha=a+\frac u{\sqrt A},
\qquad
0<\nu_0\le |u|\le\nu_1.
\tag{28}
\]

The reverse small-angle estimate gives

\[
|D_{q_A}(\alpha d_{\ell,A})|
\asymp
\frac{q_A^2}{s_A\sqrt A}
\tag{29}
\]

uniformly there, and `ANF-118` supplies a nonvanishing Gaussian fraction of the base packet energy on such a subwindow. Thus (26) is attained up to `o(A)`. If `2lambda+sigma>1/2`, this repeated-digit family exponentially amplifies rather than evacuates the saddle chamber; equality is the critical subexponential boundary. This is an internal sharpness statement for the explicit architecture only.

## 4. The evacuated ladder regenerates at one nearby coherent chamber

At `beta_A`, every nominal digit is coherent:

\[
\beta_Ad_A=1,
\qquad
|D_{q_A}(\beta_Ad_A)|=q_A.
\tag{30}
\]

Take

\[
C_A
:=
\left\{
\alpha:
\bigl||\alpha|-\beta_A\bigr|
\le A^{-2}
\right\}.
\tag{31}
\]

The perturbation (15), the width in (31), and `q_A=A^{theta+o(1)}` with `theta<1/2` imply

\[
|D_{q_A}(\alpha d_{\ell,A})|
=q_A\exp(-o(1))
\tag{32}
\]

uniformly on `C_A`. Consequently

\[
|p_A(\alpha)|^2
=R_A^2\exp(-o(A)).
\tag{33}
\]

Since `beta_A-a=Theta(A^{-lambda})`, Taylor expansion at the strict saddle gives

\[
I_A:=f-F(\beta_A)=\Theta(A^{-2\lambda})=o(1).
\tag{34}
\]

The polynomial width of `C_A` changes only subexponential factors in the `ANF-115` Laplace envelope, so

\[
\frac1A
\log
\frac{E_{C_A}(P_A)}{E_A}
\to0.
\tag{35}
\]

Combining (17), (33), and (35),

\[
\boxed{
\frac1A
\log
\frac{E_{C_A}(T_A)}{E_A}
\longrightarrow2\rho.
}
\tag{36}
\]

The trivial pointwise bound `|p_A|<=R_A` gives `E_0(T_A)<=R_A^2E_A`, hence the matching global rate

\[
\boxed{
\frac1A
\log
\frac{E_0(T_A)}{E_A}
\longrightarrow2\rho.
}
\tag{37}
\]

The source has therefore not been destroyed by the ladder of roots; it has been transported a mesoscopic distance into the deliberately coherent endpoint chamber, where the cloud asymptotically saturates its square-growth exponent.

## 5. The same cloud can remain exponentially dark to a fixed central notch

Fix `eta<a`. Because the `ANF-115` exponent has a strict saddle at `a`, define

\[
\Delta_\eta
:=
f-\sup_{|\alpha|\le\eta}F(\alpha)>0.
\tag{38}
\]

Using `|p_A|<=R_A` everywhere and the base-packet Laplace bound,

\[
\frac{E_\eta(T_A)}{E_A}
\le
\exp\bigl((2\rho-\Delta_\eta+o(1))A\bigr).
\tag{39}
\]

Thus whenever

\[
2\rho<\Delta_\eta,
\tag{40}
\]

the complete cloud is exponentially negligible for that fixed central notch even while its global source norm grows at rate `e^{2rho A}` in the endpoint chamber. A mesoscopic root ladder therefore does not by itself force regenerated source back into the fixed-notch window relevant to `ANF-099`--`ANF-121`.

## 6. Adversarial checks and the new cascade gate

The construction does **not** produce a bounded-mass Montgomery--Taylor near-extremizer: (37) says the regenerated endpoint reservoir is exponentially oversized. A fatal completion would still need another cancellation layer that removes that coherent chamber while preserving the affine/source normalization. Nor does the construction defeat an arbitrary polynomially chosen set of spectral checkpoints; the simultaneous zeros lie on the explicit arithmetic ladder (9).

What is established is enough to rule out a weaker proof strategy. Tracking only a fixed finite chamber family is already inadequate after `ANF-127`, and merely replacing it by the particular increasingly dense arithmetic ladder above still does not close the exponential branch: `A^{sigma+o(1)}` separated Gaussian chambers can all be dark while a nearby omitted chamber carries essentially the full coherent exponent. Closing **arbitrary** adaptive or polynomial checkpoint schemes would require a separate argument and is not claimed here.

The positive gate suggested by the calculation is more global: a continuum transport/coercivity law for the log-amplitude or source budget across the interval from `a` to `beta_A`, or a theorem that cancelling the final coherent maximum necessarily incurs an unrecoverable affine, source, or notch-exposure cost. The obstruction is now an explicit mesoscopic cascade geometry rather than only the existence of a second chamber.

## 7. Prior-art boundary and implication

Finite geometric sums, equally spaced root grids, and products of trigonometric factors are classical; nearby languages include Dirichlet kernels, comb-filter nulls, and generalized Riesz products. No external theorem is load-bearing here. The new calculation couples the moving root lattice with the already-established `ANF-115`/`ANF-118` packet asymptotics and the Montgomery--Taylor unsigned source budget to produce the explicit phase condition (1), suppression rate (2), regenerated endpoint rate (36), and fixed-notch estimate (39).

A targeted audit found no source supplying this packet-specific tradeoff, so `research/analytic_frontier/SOURCES.md` requires no change. The frontier is now sharper: `ANF-126` closes subexponential unsigned budgets; `ANF-127` opens the exponential branch by transporting one saddle; `ANF-128` shows that one exponential physical layer can already hide that transport from a polynomial-depth arithmetic ladder of natural Gaussian checks. The next substantive step is to test whether a genuinely continuum source-transport inequality survives these digit products and can prevent repeated cancellation/regeneration from returning to bounded mass.