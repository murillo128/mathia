# NB-248 — Squaring the Ford-edge logarithmic derivative hits the pole-critical L2 endpoint

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + METHOD-BOUNDARY + FIRST-ORDER-EDGE-L2-OBSTRUCTION + MATCHED-PACKET-BUDGET-SHARP + NB-237/NB-247-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-237` rewrites the critical Ford current as a bounded first-order area pairing against the normalized logarithmic derivative `R^{-1} zeta'/zeta`. `NB-247` then shows that the live source theorem may be reduced to a hard Ford-window second moment of that current. The most direct way to combine those two statements would be to insert the `NB-237` area formula into the second moment and apply Cauchy--Schwarz to `zeta'/zeta` before dealing with the carrier.

That route is not available. In the Ford-scaled two-dimensional edge coordinates, every zero produces a Cauchy pole. The normalized pole is locally in `L^p` exactly for `p<2`, while `p=2` is logarithmically divergent. More precisely, if an edge weight is nonzero at a zero, then the weighted local `L^2` norm of `R^{-1} zeta'/zeta` is infinite. If the pole is excised at normalized radius `epsilon`, the contribution is `asymp J^{-1} log(1/epsilon)` per simple zero. For a carrier-compatible packet with `Theta(J)` simple zeros, the summed coefficient of that logarithmic divergence is order one, so regularization offers **no decay in `J`**.

The subcritical exponents do not provide a hidden escape. For every fixed `1 <= p < 2`, one pole contributes `asymp J^{-1}` to the `p`-th power of the normalized `L^p` mass, so summing the absolute local pole budgets over a `Theta(J)` matched packet stays order one. Hölder below the critical exponent can therefore recover at most the existing absolute population scale; at `p=2`, where one might hope for a Hilbert-space gain, the pole singularity ceases to be square-integrable.

The correct order of operations is consequently the one already suggested by `NB-243`: **pair the divisor first, then square the resulting finite current**. Squaring the area integrand itself is singular; squaring the already-integrated current produces a two-copy kernel whose `1/r` singularities are separately locally integrable and is representation-equivalent to the depth-marked carrier pair energy. Thus the hard-window theorem left by `NB-247` cannot be obtained by a black-box local `L^2` estimate for the first-order logarithmic-derivative field. Any successful first-order route must preserve the signed pole pairing, or pass directly to a bilinear/two-point observable before taking absolute values.

## 1. Put the `NB-237` edge current in frozen-center form

Retain the Ford variables used in `NB-237`--`NB-247`:

\[
Q=\log(10+|t_0|),
\qquad
R=Q^{2/3}(\log Q)^{1/3},
\qquad
X=YR,
\qquad
J=\frac RH,
\tag{1}
\]

with `Y` bounded above and below by positive constants and, in the conservative transition regime,

\[
1\ll J\le \log Q.
\tag{2}
\]

Freeze `X,H,J` and the horizontal Ford cutoff at the selected center `t_0`, exactly as in `NB-246`--`NB-247`, but allow the observation center `t` to move in the Ford box. Write

\[
\sigma(d)
:=1-\frac{\log J+d}{X},
\qquad
s_t(d,\tau)
:=\sigma(d)+i\left(t+\frac\tau H\right).
\tag{3}
\]

The first-order divisor identity of `NB-237` gives the frozen critical current in the form

\[
\boxed{
\mathcal R_{t_0}(t)
=
\frac{e^{-r}}{2\pi R}
\int_{\mathbb R^2}
\frac{\zeta'}{\zeta}\!\left(s_t(d,\tau)\right)
W_J(d,\tau)\,dd\,d\tau,
}
\tag{4}
\]

where

\[
W_J(d,\tau)
:=
 e^{-d}\chi'(d)
 e^{iYJ\tau}
 F\!\left(\tau+i\eta_{d,J}\right),
\qquad
\eta_{d,J}
:=\frac{\log J+d+r}{YJ}.
\tag{5}
\]

The support of `chi'` is fixed in `d`, and `F` is uniformly Schwartz in the real `tau` direction. Thus `W_J` has bounded `L^q(dd d tau)` norms for every fixed `1<=q<=infinity`, uniformly in the allowed Ford regime. Equation (4) is finite because the simple-pole singularities of `zeta'/zeta` are locally area-integrable.

The question is whether the hard-window target of `NB-247`,

\[
I_A(t_0)
:=
H\int_{t_0-A/H}^{t_0+A/H}
|\mathcal R_{t_0}(t)|^2\,dt,
\tag{6}
\]

can be controlled by taking an `L^2` norm of the logarithmic derivative inside (4). The local pole geometry shows that it cannot.

## 2. The Ford-normalized pole is exactly critical for planar `L^2`

Let

\[
\rho=\beta+i\gamma
\]

be a nontrivial zero of multiplicity `m=m(rho)`, and for the current center `t` define its Ford coordinates

\[
d_\rho:=X(1-\beta)-\log J,
\qquad
\tau_\rho:=H(\gamma-t).
\tag{7}
\]

Then

\[
s_t(d,\tau)-\rho
=
-\frac{d-d_\rho}{X}
+i\frac{\tau-\tau_\rho}{H}.
\tag{8}
\]

Since `X=YR` and `H=R/J`,

\[
\boxed{
R\bigl(s_t(d,\tau)-\rho\bigr)
=
-\frac{d-d_\rho}{Y}
+iJ(\tau-\tau_\rho).
}
\tag{9}
\]

Near the zero, write

\[
\frac{\zeta'}{\zeta}(s)
=
\frac{m}{s-\rho}+g_\rho(s),
\tag{10}
\]

where `g_rho` is holomorphic in a puncture-free neighborhood of `rho`. Hence

\[
\frac1R\frac{\zeta'}{\zeta}(s_t(d,\tau))
=
\frac{m}{-(d-d_\rho)/Y+iJ(\tau-\tau_\rho)}
+\frac1R g_\rho(s_t(d,\tau)).
\tag{11}
\]

Introduce the isotropic pole coordinates

\[
x:=\frac{d-d_\rho}{Y},
\qquad
y:=J(\tau-\tau_\rho).
\tag{12}
\]

Their Jacobian is

\[
dd\,d\tau
=
\frac YJ\,dx\,dy.
\tag{13}
\]

For any fixed small disk `x^2+y^2<c^2`, the singular contribution to the `p`-th power of the normalized local norm is therefore

\[
\frac YJ m^p
\int_{x^2+y^2<c^2}
(x^2+y^2)^{-p/2}\,dx\,dy.
\tag{14}
\]

The radial integral is

\[
2\pi\int_0^c r^{1-p}\,dr.
\tag{15}
\]

Hence

\[
\boxed{
R^{-1}\frac{\zeta'}{\zeta}
\text{ is locally }L^p(dd\,d\tau)
\iff p<2.
}
\tag{16}
\]

At the Hilbert exponent,

\[
2\pi\int_0^c\frac{dr}{r}=+\infty.
\tag{17}
\]

Consequently, whenever

\[
W_J(d_\rho,\tau_\rho)\ne0,
\tag{18}
\]

one has

\[
\boxed{
\int
\left|
\frac1R\frac{\zeta'}{\zeta}(s_t(d,\tau))
\right|^2
|W_J(d,\tau)|\,dd\,d\tau
=+\infty
}
\tag{19}
\]

over every sufficiently small neighborhood of that pole.

Thus the naive Cauchy--Schwarz step

\[
\left|
\int R^{-1}\frac{\zeta'}{\zeta}W_J
\right|^2
\le
\left(\int |R^{-1}\zeta'/\zeta|^2|W_J|\right)
\left(\int |W_J|\right)
\tag{20}
\]

is not merely quantitatively weak: its first factor is undefined as a finite quantity in the presence of an edge zero.

This is a genuine uniform obstruction. A fixed smooth transition `chi'` cannot assume that its support contains no zeta zero at any selected height. Moving the transition to avoid one known pole would make the source cutoff depend on the unknown divisor and would also have to be repeated uniformly as the selected height changes.

## 3. Excising the poles exposes the missing logarithmic endpoint

The divergence in (18) is only logarithmic, so one might try to excise microscopic pole neighborhoods and pass to a limit. The scaling shows exactly what that buys.

Remove the normalized ellipse

\[
\mathcal E_\varepsilon(\rho)
:=
\left\{
\left(\frac{d-d_\rho}{Y}\right)^2
+
J^2(\tau-\tau_\rho)^2
<\varepsilon^2
\right\}.
\tag{21}
\]

For a simple zero, the coefficient of the logarithmic divergence is universal. As `epsilon->0`, the annulus `epsilon<sqrt(x^2+y^2)<c` contributes

\[
\boxed{
\frac{2\pi Y}{J}
\log\frac1\varepsilon
+O_{\rho,J,c}(J^{-1})
}
\tag{22}
\]

to the squared local mass of `R^{-1}zeta'/zeta`; the holomorphic part and the cross term cannot change the coefficient of `log(1/epsilon)`. Multiplicity `m` multiplies that coefficient by `m^2`. No uniform claim is made about the displayed remainder as the zero configuration itself varies.

Now insert only the **population scale** of the matched Ford geometry of `NB-231`. A carrier-compatible packet has

\[
M\asymp J
\tag{23}
\]

zeros whose scaled vertical separation is

\[
\Delta\tau
\asymp\frac1J.
\tag{24}
\]

In the `y=J tau` coordinate the pole centers are separated by a fixed positive amount, so the logarithmic coefficients from disjoint sufficiently small pole annuli add. Their total coefficient is

\[
\boxed{
\frac{1}{J}\sum_{j=1}^{M}m(\rho_j)^2
\asymp 1
}
\tag{25}
\]

for a simple matched packet. Thus an `L^2` regularization has **no asymptotic `J` gain in its singular coefficient**: sending the exclusion radius to zero produces an order-one multiple of `log(1/epsilon)`, not a quantity suppressed by carrier width.

A contour displacement has the same structural price. Moving the first-order edge a normalized distance `epsilon` away from a pole regularizes its local square only by cutting off this logarithmic singularity. If the displacement crosses the divisor, the omitted residues are precisely the zero terms whose cancellation the Ford current is supposed to control. Thus regularization cannot silently turn (4) into a harmless `L^2` field estimate.

## 4. Subcritical `L^p` is finite but has no matched-packet gain

One could instead apply Holder with an exponent below the singular endpoint. Equation (14) shows why that also fails to create the missing decay from population information alone.

For every fixed

\[
1\le p<2,
\]

the singular part of one simple pole contributes

\[
\asymp_p\frac1J
\tag{26}
\]

to the `p`-th power of its local normalized pole budget on a fixed disk in `(x,y)`. Summing those **absolute local pole costs** over an allowed packet with `M asymp J` gives

\[
\boxed{
\frac1J\sum_{j=1}^{M}m(\rho_j)^p
\asymp_p1
}
\tag{27}
\]

for simple poles. Hence replacing the exact signed field by subcritical local `L^p` costs can recover at most an order-one estimate from the existing population information; there is no hidden negative power of `J`. The conjugate exponent `q=p/(p-1)` sees a uniformly bounded norm of the smooth edge weight `W_J`, so a Holder argument based only on those absolute pole budgets is compatible with

\[
|\mathcal R_{t_0}(t)|=O_p(1),
\tag{28}
\]

which is exactly the scale already permitted by the coherent packet. The constant in the radial integral deteriorates like `(2-p)^{-1}` as `p` approaches `2`, so drifting toward the endpoint does not by itself manufacture a vanishing factor.

This gives a sharp functional-analytic picture:

\[
\begin{array}{ccl}
p<2&:&\text{finite, but matched packets keep order-one mass},\\
p=2&:&\text{logarithmically divergent at every visible pole},\\
p>2&:&\text{power divergent at every visible pole}.
\end{array}
\tag{29}
\]

The hoped-for Hilbert-space gain sits exactly at the exponent where the first-order divisor field stops belonging to the space.

## 5. Squaring after divisor pairing is finite and preserves the right two-point object

The obstruction concerns the **order of operations**, not the existence of a second moment for the Ford current itself. Equation (4) is finite because a Cauchy pole is locally `L^1` in two dimensions. Therefore one may first perform the signed area pairing and only then square:

\[
|\mathcal R_{t_0}(t)|^2
=
\frac{e^{-2r}}{4\pi^2R^2}
\iiiint
Z_t(d,\tau)\overline{Z_t(d',\tau')}
W_J(d,\tau)\overline{W_J(d',\tau')}
\,dd\,d\tau\,dd'\,d\tau',
\tag{30}
\]

where

\[
Z_t(d,\tau)
:=
\frac{\zeta'}{\zeta}(s_t(d,\tau)).
\tag{31}
\]

Near a pair of poles, the singularity in (30) is a product of two separate `1/r` factors. Each is locally area-integrable, so the four-dimensional product is locally integrable. The hard center mean (6) can therefore be inserted **after** this bilinearization without creating the `L^2` pole divergence of (18).

At the divisor level, this is exactly the same structural operation as `NB-243`: first use the residues to form the finite depth-marked current, then take its squared modulus. Expanding the resulting current gives the carrier pair phase

\[
e^{iX(\gamma_j-\gamma_k)}
\tag{32}
\]

rather than the divergent local square of a single Cauchy pole.

Thus `NB-237` and `NB-247` fit together only through a **bilinear/two-copy first-order representation**, not through a one-copy area `L^2` norm. Any useful estimate on the logarithmic-derivative side must retain the cancellation between poles until after the pairing, or equivalently control a genuine two-point object. Taking absolute squares too early destroys exactly the residue structure one needs.

## 6. Prior-art boundary

The local integrability threshold of a simple Cauchy pole is classical complex analysis; no novelty is claimed for the elementary fact that `1/z` lies locally in planar `L^p` precisely for `p<2`. The line-local content is the Ford scaling (9)--(12), which puts the desired hard-window second moment exactly at that critical exponent, and the Ford-scaled pole budgets (21)--(27), which show that regularization or movement below the endpoint recovers no asymptotic carrier-width gain.

Two literature checks reinforce the boundary without being load-bearing. Fan Ge, *Mean values of the logarithmic derivative of the Riemann zeta-function near the critical line*, Mathematika 69 (2023), 562--572, DOI `10.1112/mtk.12194`, [arXiv:2211.08571](https://arxiv.org/abs/2211.08571), studies moments only after evaluating `zeta'/zeta` at a positive horizontal offset from the zero line; the displayed asymptotics become singular as that offset tends to zero. Najnudel and Nikeghbali, *Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes transforms*, [arXiv:2609.15862](https://arxiv.org/abs/2609.15862) (14 September 2026), identify Cauchy/Stieltjes behavior for normalized logarithmic derivatives, again emphasizing the heavy-tailed pole geometry rather than a square-integrable field. Neither theorem supplies the deterministic Ford-window estimate required here.

No external theorem is needed for (8)--(32), so `SOURCES.md` does not acquire a new durable dependency.

## 7. Adversarial review and falsification boundary

Several limits matter.

First, (18) is conditional on the edge weight being nonzero at the pole. A particular selected center can have no zero in the support of `chi'`, in which case its local logarithmic derivative is smooth there and an `L^2` estimate is formally possible. The result is a **uniform method boundary**: the source theorem cannot rely on that accident because the existing zero information does not exclude visible edge zeros uniformly.

Second, this does not rule out all mean-square methods for `zeta'/zeta`. One may evaluate on a contour kept a controlled positive distance from every pole, use a renormalized principal object, or form a bilinear correlation before taking absolute values. What is excluded is the black-box step that inserts the exact first-order edge formula and then estimates the same-area variable by ordinary `L^2`/Cauchy--Schwarz.

Third, the matched packet used in (24)--(26) is an adversarial spectral control compatible with the previously audited population scales; it is not a claim that actual zeta zeros realize that geometry. Its role is to show sharpness of the available information: subcritical Holder norms do not distinguish the dangerous packet from an allowed source configuration.

Fourth, the finding remains source-side. It does not prove the hard-window mean (6), and it does not supply the independent bridge from Nyman--Beurling approximation distance to the Ford current.

A decisive falsification of the method-boundary claim would be a uniform inequality deriving the exact current from a one-copy weighted planar `L^2` norm of `R^{-1}zeta'/zeta` on the same edge while allowing the weight to be nonzero at a zero. Equation (18) rules this out at the level of the norm itself. A successful theorem must modify the representation or the order in which pairing and squaring occur.

## Conclusion

The local second-moment target of `NB-247` should **not** be attacked by first turning the `NB-237` representation into a local planar `L^2` problem for `zeta'/zeta`. Ford scaling makes a visible zero look like

\[
\frac1{-(d-d_\rho)/Y+iJ(\tau-\tau_\rho)},
\]

which is exactly at the non-square-integrable Cauchy endpoint. Excising the poles leaves a logarithmic cost with no `J`-decay for a `Theta(J)` matched packet, while every fixed `p<2` remains only order one.

The viable first-order route is therefore narrower: **retain the signed divisor pairing and bilinearize only afterwards**. That returns the depth-marked two-point carrier object already isolated by `NB-243` and now required in hard-window form by `NB-247`. The missing theorem is genuinely a pole-correlation theorem, not an ordinary local `L^2` bound for the logarithmic-derivative field.
