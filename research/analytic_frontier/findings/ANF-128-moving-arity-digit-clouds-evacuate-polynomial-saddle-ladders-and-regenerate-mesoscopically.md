# ANF-128 — moving-arity digit clouds evacuate polynomial saddle ladders and regenerate mesoscopically

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + EXPONENTIAL-TRANSLATION-CLOUD + MOVING-ARITY + POLYNOMIAL-DEPTH-SADDLE-LADDER + MESOSCOPIC-TRANSPORT + FIXED-NOTCH-DARK + CASCADE-GATE`. `ANF-126` makes subexponential growing mirrors excisable, while `ANF-127` shows that any positive exponential unsigned-budget rate can cancel one saddle and regenerate source in a second chamber. The remaining question is whether an exponential cancellation cascade can be closed by monitoring progressively more spectral chambers. The answer is already negative for any fixed or polynomially sparse chamber checkpoint scheme of the natural Gaussian width: one moving-arity digit layer can erase a polynomial-depth ladder of such chambers and regenerate essentially all of its coherent source growth in a nearby mesoscopic chamber.

Fix an `ANF-115` packet family with interior saddle `a=a_gamma`. For exponents `lambda>0` and `sigma>=0` satisfying

\[
\boxed{2\lambda+\sigma<\frac12,}
\tag{1}
\]

and for every prescribed exponential unsigned-budget rate `rho>0`, there is an explicit positive cloud of translated copies with

\[
\frac1A\log\mathcal U_A\to\rho
\]

that simultaneously suppresses `A^{sigma+o(1)}` pairwise disjoint natural Gaussian chambers, spread across a spectral interval of length `Theta(A^{-lambda})`, by `exp(-kappa A+o(A))`, while a coherent chamber at distance `Theta(A^{-lambda})` from the original saddle carries source energy `exp((2rho+o(1))A)` relative to one packet. The suppression exponent is

\[
\boxed{
\kappa_{\lambda,\sigma,\rho}
=
\frac{2\rho}{\lambda+\sigma}
\left(\frac12-2\lambda-\sigma\right)>0.
}
\tag{2}
\]

Within this repeated moving-arity geometric-sum family, the line `2 lambda + sigma = 1/2` is sharp on the `A`-exponential scale. In the one-checkpoint-depth case `sigma=0`, this gives an internal quarter-power frontier: a single layer can transport its coherent reservoir by `A^{-lambda}` while exponentially evacuating the original natural Gaussian saddle chamber exactly when `lambda<1/4`. This is a sharp boundary for the explicit digit construction, **not** a universal `A^{-1/4}` obstruction for arbitrary physical clouds.

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

For `sigma=0` one may simply take `s_A=1`. Define

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

and the original saddle is the final root in this ladder:

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

Because `theta<1/2`, the spacing (12) is much larger than the natural Gaussian width `A^{-1/2}`. Thus fixed-width Gaussian chambers around all these roots are pairwise disjoint, even though the entire ladder contracts mesoscopically toward `a`.

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

so that every translated physical point below is distinct. As in `ANF-127`, such spacings can be chosen inductively: after finitely many earlier digits have been fixed, every new collision excludes only finitely many values of the next spacing, so an arbitrarily small interval around `d_A` contains an admissible value.

For `v=(v_1,...,v_{h_A})` with `0<=v_ell<q_A`, set

\[
\tau_v:=\sum_{\ell=1}^{h_A}v_\ell d_{\ell,A}
\]

and form the positive physical cloud

\[
T_A
:=
\bigsqcup_{v\in\{0,\ldots,q_A-1\}^{h_A}}
(P_A+\tau_v).
\tag{16}
\]

Its number of copies is

\[
R_A=q_A^{h_A}
=\exp((\rho+o(1))A).
\tag{17}
\]

Consequently its unsigned Hilbert budget in the sense used in `ANF-123`--`ANF-127` is

\[
\mathcal U_A=R_A,
\qquad
\frac1A\log\mathcal U_A\to\rho.
\tag{18}
\]

The horizontal span is only polynomial:

\[
\operatorname{span}_x(T_A)
=O(h_Aq_A)
=A^{1+\theta+o(1)}.
\tag{19}
\]

Most importantly, translation gives the exact modulation factorization

\[
S_{T_A}(\alpha)
=p_A(\alpha)S_{P_A}(\alpha),
\qquad
p_A(\alpha)
=
\prod_{\ell=1}^{h_A}
D_{q_A}(\alpha d_{\ell,A}).
\tag{20}
\]

No signed coefficients, abstract Hilbert vectors, or nonphysical weights enter the construction.

## 3. Every natural Gaussian chamber in the ladder is exponentially evacuated

The geometric sum has the closed form

\[
D_q(x)
=e^{-\pi i(q-1)x}\frac{\sin(\pi qx)}{\sin(\pi x)}.
\tag{21}
\]

At the root `x_r=1-r/q`,

\[
|D_q'(x_r)|
=
\frac{\pi q}{\sin(\pi r/q)}
=(1+o(1))\frac{q^2}{r}
\tag{22}
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
\tag{23}
\]

The conditions `q_A=o(sqrt A)` and (15) imply that throughout these chambers the numerator in (21) stays in its linear regime and the denominator remains comparable to `r/q_A`. Hence, uniformly in `r`, `ell`, and `alpha in B_{r,A}(S)`,

\[
|D_{q_A}(\alpha d_{\ell,A})|
\le
C_S\frac{q_A^2}{s_A\sqrt A}.
\tag{24}
\]

Combining (20) and (24),

\[
\sup_{\alpha\in B_{r,A}(S)}|p_A(\alpha)|^2
\le
\left(
C_S\frac{q_A^4}{s_A^2A}
\right)^{h_A}.
\tag{25}
\]

Now

\[
4\log q_A-2\log s_A-\log A
=
(4\lambda+2\sigma-1+o(1))\log A.
\tag{26}
\]

Using `h_A/A=(rho+o(1))/log q_A` gives

\[
\frac1A
\log
\sup_{B_{r,A}(S)}|p_A|^2
\le
-\kappa_{\lambda,\sigma,\rho}+o(1),
\tag{27}
\]

with `kappa` exactly as in (2). Therefore

\[
\boxed{
\sup_{s_A\le r\le2s_A}
\frac{E_{B_{r,A}(S)}(T_A)}{E_A}
\le
\exp\bigl(-(\kappa_{\lambda,\sigma,\rho}+o(1))A\bigr).
}
\tag{28}
\]

Since there are only `A^{sigma+o(1)}` disjoint chambers, the same exponential rate holds for their union. Thus one digit layer does not merely kill a finite phase jet or a single saddle value: it evacuates a polynomial-depth sequence of full natural Gaussian chambers across a mesoscopic interval.

The phase line is also sharp for this construction. At the original saddle `a=a_{2s_A,A}`, take a fixed off-center Gaussian subwindow

\[
\alpha=a+\frac u{\sqrt A},
\qquad
u_0\le |u|\le\nu_1,
\tag{29}
\]

with `0<nu_0<nu_1` fixed. The reverse form of the same small-angle estimate gives

\[
|D_{q_A}(\alpha d_{\ell,A})|
\asymp
\frac{q_A^2}{s_A\sqrt A}
\tag{30}
\]

uniformly there. `ANF-118` gives a nonvanishing Gaussian fraction of the base packet energy on such a subwindow. Hence the exponent in (27) is attained up to `o(A)`. If `2lambda+sigma>1/2`, the same family exponentially *amplifies* rather than evacuates that saddle chamber; equality is the critical subexponential boundary. This sharpness statement is internal to the repeated `D_q` architecture.

## 4. The evacuated ladder regenerates at one nearby coherent chamber

At `beta_A`, every nominal digit is exactly coherent:

\[
\beta_Ad_A=1,
\qquad
|D_{q_A}(\beta_Ad_A)|=q_A.
\tag{31}
\]

Take a much narrower chamber

\[
C_A
:=
\left\{
\alpha:
\bigl||\alpha|-\beta_A\bigr|
\le A^{-2}
\right\}.
\tag{32}
\]

The perturbation (15), the width in (32), and `q_A=A^{theta+o(1)}` with `theta<1/2` imply

\[
|D_{q_A}(\alpha d_{\ell,A})|
=q_A\exp(-o(1))
\tag{33}
\]

uniformly on `C_A`. Thus

\[
|p_A(\alpha)|^2
=R_A^2\exp(-o(A)).
\tag{34}
\]

Meanwhile `beta_A-a=Theta(A^{-lambda})`. Taylor expansion at the strict saddle gives the moving large-deviation cost

\[
I_A
:=
f-F(\beta_A)
=\Theta(A^{-2\lambda})
=o(1).
\tag{35}
\]

The polynomial chamber width in (32) contributes only `o(A)` to the logarithm. The `ANF-115` Laplace envelope therefore yields

\[
\frac1A
\log
\frac{E_{C_A}(P_A)}{E_A}
\to0.
\tag{36}
\]

Combining (17), (34), and (36),

\[
\boxed{
\frac1A
\log
\frac{E_{C_A}(T_A)}{E_A}
\longrightarrow2\rho.
}
\tag{37}
\]

The trivial pointwise bound `|p_A|<=R_A` gives the matching global upper bound `E_0(T_A)<=R_A^2E_A`. Hence in fact

\[
\boxed{
\frac1A
\log
\frac{E_0(T_A)}{E_A}
\longrightarrow2\rho.
}
\tag{38}
\]

The cloud therefore asymptotically saturates its full coherent square-growth rate after evading all the ladder checkpoints. The source has not been destroyed; it has been transported a mesoscopic distance into a chamber deliberately omitted from the root ladder.

## 5. The same cloud can remain exponentially dark to any fixed central notch

Fix a central notch radius `eta<a`. Because the `ANF-115` exponent has a strict saddle at `a`,

\[
\Delta_\eta
:=
f-\sup_{|\alpha|\le\eta}F(\alpha)
>0.
\tag{39}
\]

Using `|p_A|<=R_A` everywhere and the base-packet Laplace bound gives

\[
\frac{E_\eta(T_A)}{E_A}
\le
\exp\bigl((2\rho-\Delta_\eta+o(1))A\bigr).
\tag{40}
\]

Therefore, if the prescribed exponential budget rate is chosen so that

\[
2\rho<\Delta_\eta,
\tag{41}
\]

then

\[
\boxed{
E_\eta(T_A)/E_A
\le e^{-c_\eta A}
}
\tag{42}
\]

for some `c_eta>0`, even though (38) says the global source energy is growing at rate `e^{2rho A}`. Thus a polynomial ladder of off-notch chamber tests does not force leakage back into the fixed central notch. This is the feature directly relevant to the exposure gate in `ANF-099`--`ANF-121`.

## 6. Adversarial checks and the new cascade gate

Several possible overclaims are excluded by construction.

First, (38) means `T_A` is **not** itself a bounded-mass Montgomery--Taylor near-extremizer; its regenerated reservoir is exponentially oversized. `ANF-128` therefore does not close `ANF-099` in either direction. A fatal completion would still need another cancellation layer that removes the coherent chamber near `beta_A` while preserving the required affine/source normalization.

Second, the quarter-power statement at `sigma=0` is not asserted as a universal transport law. It is the exact exponential phase boundary of the repeated moving-arity geometric-sum architecture, derived from the root slope `q^2/r` and the number of repeated digits. Other exponential clouds could have a different tradeoff.

Third, the polynomial ladder is genuinely stronger than a fixed finite set of checkpoints. Its cardinality tends to infinity and its chambers are separated by much more than their Gaussian width. Nevertheless it still samples only a vanishing part of the continuum between `a` and `beta_A`. The coherent endpoint can sit immediately beyond the final root and recover the full square-growth exponent.

The new positive gate is therefore more global than the one left by `ANF-127`. A proof cannot close the exponential branch merely by iterating finitely many, or polynomially many sparsely placed, mesoscopic saddle chambers. It needs a conservation/coercivity statement that controls the **continuum of log-amplitude or source budget across the transport interval**, or it must show that cancelling the final coherent maximum necessarily pays an unrecoverable affine, source, or notch-exposure cost. The obstruction is now an explicit cascade geometry rather than a generic warning that a second chamber may appear.

## 7. Prior-art boundary

Finite geometric sums, their equally spaced root grids, and products of such trigonometric factors are classical; nearby languages include Dirichlet kernels, comb-filter nulls, and generalized Riesz products. The load-bearing step here is not an external theorem about those objects. It is the repo-specific coupling of their moving root lattice with the `ANF-115` Laplace saddle, the Montgomery--Taylor unsigned source budget, and a growing number of repeated physical translation digits.

A targeted audit found no source whose theorem supplies the tradeoff

\[
2\lambda+\sigma<\frac12
\]

or the simultaneous conclusions (28), (37), and (40) for this physical packet model. The derivation above uses only elementary geometric-sum estimates plus already-established `ANF-115`/`ANF-118` packet asymptotics. No new external result is load-bearing, so `research/analytic_frontier/SOURCES.md` requires no change.

## 8. Implication for the frontier

`ANF-126` closes all subexponential unsigned budgets. `ANF-127` proves that a positive exponential rate can escape one chamber. `ANF-128` shows that, after entering that exponential regime, a single physical layer can already hide from a polynomial-depth sequence of natural Gaussian chamber checks while transporting essentially its entire coherent source exponent by a mesoscopic distance and remaining dark to a fixed central notch.

The next meaningful question is no longer how many discrete saddle chambers to add. It is whether there is a **continuum transport inequality** for physical exponential sums that forces a nonrecoverable cost when source mass is repeatedly cancelled and regenerated between nearby chambers. Absent such a law, the exponential-cascade branch remains a genuine obstruction to turning the fixed-notch exposure mechanism into a universal near-extremizer theorem.