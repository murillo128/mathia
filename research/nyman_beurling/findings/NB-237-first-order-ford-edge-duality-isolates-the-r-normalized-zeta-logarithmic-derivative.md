# NB-237 — First-order Ford edge duality isolates the R-normalized zeta logarithmic derivative

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + FIRST-ORDER-EDGE-DUALITY + R-NORMALIZED-LOG-DERIVATIVE + CARRIER-POLE-RESONANCE + NB-236-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-236` rewrites the critical Ford layer as a bounded-mass Poincaré–Lelong edge pairing against `log|zeta|`. That representation proves that horizontal depth localization itself is cheap, but leaves a second-order potential kernel whose useful cancellation is not yet explicit.

The same smooth Ford cutoff has a first-order distributional representation through `zeta'/zeta`. For the exact carrier, the `L^1` mass of the first-order edge kernel is not merely bounded: it is

\[
O\!\left(\frac1R\right).
\]

After the Ford change of variables, the unresolved coefficient is therefore a microlocal signed average of the naturally normalized current

\[
\frac1R\frac{\zeta'}{\zeta}(s).
\]

This does **not** by itself give decay. The matched critical packets from `NB-231` are exactly resonant with the carrier frequency: a pole spacing of order `1/R` becomes a spacing of one integer number of carrier periods. Hence generic high-frequency or Riemann–Lebesgue reasoning cannot make the first-order pairing small. The representation sharpens the next source-side target to a cancellation theorem for the `R`-normalized logarithmic derivative that excludes this carrier-locked pole geometry.

## 1. The Ford-localized zero sum has a first-order exact formula

Retain the notation of `NB-228`--`NB-236`:

\[
Q=\log(10+|t|),
\qquad
R=Q^{2/3}(\log Q)^{1/3},
\qquad
Y=\frac XR,
\]

and

\[
J:=\frac RH\to\infty.
\tag{1}
\]

Fix `r>0`, put

\[
\sigma_X=1+\frac rX,
\qquad
s_X=\sigma_X+it,
\]

and let

\[
F(z)=\int_0^1\phi(y)e^{izy}\,dy,
\qquad
0\ne\phi\in C_c^\infty((0,1)).
\tag{2}
\]

As in `NB-236`, define the holomorphic carrier

\[
K_{X,H}(s)
:=e^{X(s-s_X)}F\!\left(-iH(s-s_X)\right)
\tag{3}
\]

and the Ford-depth coordinate

\[
d(s):=X(1-\Re s)-\log J.
\tag{4}
\]

For a fixed real cutoff `chi in C_c^infty(R)`, equal to one on the target critical layer, set

\[
\Psi(s):=K_{X,H}(s)\chi(d(s)).
\tag{5}
\]

For a meromorphic function `f`, distributionally,

\[
\bar\partial\!\left(\frac{f'}f\right)
=
\pi\sum_{f(\rho)=0}m(\rho)\delta_\rho
-
\pi\sum_{f(p)=\infty}n(p)\delta_p.
\tag{6}
\]

Pairing (6) with `Psi` gives

\[
\sum_\rho m(\rho)\Psi(\rho)
-
\sum_p n(p)\Psi(p)
=
-\frac1\pi
\int_{\mathbb C}
\frac{f'}f(s)\,\bar\partial\Psi(s)\,dA(s).
\tag{7}
\]

Take `f=zeta`. For all sufficiently large `J`, the fixed support of `chi` excludes the pole at `1`, because `d(1)=-log J`, and excludes all trivial zeros because their Ford depth tends to `+infinity`. Thus only the nontrivial zeros in the selected depth layer remain.

Since `K_{X,H}` is holomorphic and

\[
\bar\partial d=-\frac X2,
\]

we have the exact identity

\[
\bar\partial\Psi(s)
=-\frac X2K_{X,H}(s)\chi'(d(s)).
\tag{8}
\]

Substituting (8) into (7) yields

\[
\boxed{
\sum_\rho m(\rho)\Psi(\rho)
=
\frac{X}{2\pi}
\int_{\mathbb C}
\frac{\zeta'}{\zeta}(s)
K_{X,H}(s)\chi'(d(s))\,dA(s).
}
\tag{9}
\]

Equation (9) is the first-order counterpart of the Poincaré–Lelong formula in `NB-236`. It is representation-equivalent at the distributional level, but exposes a different quantitative normalization.

## 2. The first-order edge tariff is exactly `1/R`

Introduce the scaled coordinates

\[
\tau:=H(\Im s-t),
\qquad
 d:=X(1-\Re s)-\log J.
\tag{10}
\]

Then

\[
s(d,\tau)
=
1-\frac{\log J+d}{X}
+i\left(t+\frac\tau H\right)
\tag{11}
\]

and

\[
K_{X,H}(s(d,\tau))
=
\frac{e^{-r-d}}J
\,e^{i(X/H)\tau}
F\!\left(
\tau+i\frac{\log J+d+r}{YJ}
\right).
\tag{12}
\]

Because `X/H=YJ`, define

\[
\eta_{d,J}:=\frac{\log J+d+r}{YJ}.
\tag{13}
\]

On the fixed support of `chi'`, `eta_{d,J}->0` uniformly. The Jacobian is

\[
dA(s)=\frac1{XH}\,dd\,d\tau.
\tag{14}
\]

Using (12)--(14), (9) becomes

\[
\boxed{
\sum_\rho m(\rho)\Psi(\rho)
=
\frac{e^{-r}}{2\pi R}
\int_{\mathbb R^2}
\frac{\zeta'}{\zeta}(s(d,\tau))
\,e^{-d}\chi'(d)
\,e^{iYJ\tau}
F(\tau+i\eta_{d,J})
\,dd\,d\tau.
}
\tag{15}
\]

The cancellation of scales is exact:

\[
\frac X2
\times
\frac1J
\times
\frac1{XH}
=
\frac1{2JH}
=
\frac1{2R}.
\tag{16}
\]

Since `F` is uniformly Schwartz in `tau` under the vanishing imaginary displacement (13),

\[
\boxed{
\left\|
\frac{X}{2\pi}K_{X,H}(s)\chi'(d(s))
\right\|_{L^1(dA)}
\ll_{\phi,\chi,r,Y}
\frac1R.
}
\tag{17}
\]

Thus the first-order edge representation naturally tests `zeta'/zeta` at scale `R`, not scale `1`. A black-box absolute-value estimate would have to show that the relevant local average of `|zeta'/zeta|` is `o(R)` to obtain `o(1)`. Such a statement cannot hold uniformly near the very poles whose residues encode the critical zeros.

The singularity causes no distributional integrability problem: near a zero `rho`,

\[
\frac{\zeta'}{\zeta}(s)
=
\frac{m(\rho)}{s-\rho}+O(1),
\]

and `1/|s-rho|` is locally integrable with respect to planar area. Equation (9) is therefore a genuine first-order area pairing, not a principal-value fiction around each zero.

## 3. A matched critical packet is exactly resonant with the carrier

The small prefactor `1/R` in (15) might suggest integrating by parts in `tau` or invoking high-frequency cancellation from

\[
e^{iYJ\tau}.
\]

The adversarial packets already constructed in `NB-231` show why this is not available generically.

Take a critical-depth packet with

\[
d_j=d_0=O(1)
\]

and ordinates

\[
\gamma_j
=t+\frac{2\pi qj+\theta}{X},
\qquad
1\le j\le M,
\qquad
M\asymp J,
\tag{18}
\]

where `q>=1` is a fixed integer and the packet occupies only a fixed small fraction of the carrier window. In the scaled ordinate coordinate,

\[
\tau_j=H(\gamma_j-t),
\]

so consecutive poles are separated by

\[
\Delta\tau
=
\frac{2\pi qH}{X}
=
\frac{2\pi q}{YJ}.
\tag{19}
\]

But the oscillatory factor in (15) has frequency `YJ`. Hence its phase increment from one pole to the next is

\[
\boxed{
(YJ)\Delta\tau=2\pi q.
}
\tag{20}
\]

The pole lattice is therefore exactly phase-locked to the carrier. All `M asymp J` residues can contribute with the same carrier phase. At the zero-sum level, each critical zero has coefficient of size `asymp 1/J`, so such a packet contributes order one, exactly as in `NB-231`.

Equation (20) gives the same obstruction on the logarithmic-derivative side. The local poles of `zeta'/zeta` produce Fourier content at the carrier frequency itself. The fact that this frequency tends to infinity does not imply Riemann–Lebesgue cancellation because the function being sampled changes with the frequency and can place its poles at the matching lattice scale `1/R`.

Thus the `1/R` tariff in (17) is not a hidden free gain. It is the normalization at which a critical coherent pole packet has order-one mass.

## 4. What this changes after `NB-236`

`NB-236` left the source-side frontier as a signed bounded-mass pairing of `log|zeta|` on the two Ford edges. Equation (15) turns the same object into a first-order current whose normalization is explicit:

\[
\boxed{
\text{critical Ford coefficient}
\quad\Longleftrightarrow\quad
\text{microlocal pairing with }
R^{-1}\frac{\zeta'}{\zeta}.
}
\tag{21}
\]

The first-order form has two advantages. First, the horizontal cutoff only differentiates once, and its complete kernel mass is `O(1/R)`. Second, the obstruction is now visible as a pole-spacing problem: a theorem strong enough to make (15) `o(1)` must rule out or decorrelate logarithmic-derivative mass that is synchronized with the carrier lattice.

This also rules out a tempting but circular route. A pointwise upper bound for `zeta'/zeta` away from zeros can be strong, but deleting small neighborhoods of the poles discards precisely the residues that reconstruct the zero coefficient. Conversely, estimating those neighborhoods absolutely returns the population tariffs of `NB-230`--`NB-234`. The useful input has to preserve signed information across the poles.

A plausible target is therefore a deterministic microlocal estimate of the form

\[
\frac1R
\int_{\mathbb R^2}
\frac{\zeta'}{\zeta}(s(d,\tau))
W_J(d,\tau)e^{iYJ\tau}
\,dd\,d\tau
=o(1),
\tag{22}
\]

for the specific smooth edge weights generated by (15), or an equivalent zero-statistical statement that excludes carrier-locked depth-phase packets. Generic mean values that average over `t` or forget the depth mark are not enough for the deterministic blockwise application pursued here.

## 5. Prior-art and representation audit

The identity (6) is classical complex analysis: it is the distributional logarithmic-derivative form of the argument principle/Cauchy–Pompeiu machinery. No novelty is claimed for replacing a zero divisor by `f'/f`, nor for the local pole expansion of `zeta'/zeta`.

A targeted prior-art search also found the recent preprint by Najnudel and Nikeghbali, *Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes transforms* (arXiv:2609.15862, September 2026). It makes explicit a closely related viewpoint: normalized logarithmic derivatives are Stieltjes transforms of local zero configurations. Their arithmetic result concerns random heights on the critical line and a `log T` normalization (under a horizontal-collapse hypothesis for the direct logarithmic-derivative comparison). It does not provide the deterministic, near-`1`, Ford-depth-localized, carrier-frequency estimate (22). It is therefore relevant prior art for the representation, not a load-bearing input to the derivation above.

The project-specific content is narrower: the exact Ford carrier (3), the depth cutoff (4), the scale identity `JH=R`, and the resonance (20). Those ingredients turn a generic Cauchy–Pompeiu representation into the `R^{-1}` microlocal current in (15) and identify the matched-packet obstruction at exactly the same scale. No new external theorem is needed for these calculations, so `SOURCES.md` does not require a new durable dependency.

## 6. Adversarial review and scope

Several possible overclaims were checked.

First, (9) is distributional. `zeta'/zeta` is not bounded near zeros, but its simple-pole singularities are locally area-integrable, while the carrier is Schwartz in the ordinate direction. Second, the pole at `1` and the trivial zeros disappear only after `J` is sufficiently large relative to the fixed support of `chi`; this is an asymptotic statement, not an identity for arbitrary finite parameters.

Third, the `O(1/R)` kernel mass in (17) is only a normalization calculation. It does **not** imply that the pairing is small, because `zeta'/zeta` can be of size `R` or larger on the corresponding microscopic pole scale. Fourth, (20) constructs an admissible matched spectral control, not a claim that the actual zeta zeros form such a packet. Its role is adversarial: any proposed theorem based only on generic oscillation of the carrier must also exclude this exact resonance.

Finally, the finding remains source-side. It does not prove a new bound for the optimal Nyman–Beurling distance and does not establish the missing bridge from an optimal approximant to vanishing of the critical Ford coefficient.

Subject to those limits, the durable conclusion is that the unresolved Ford transition can be represented without a growing localization tariff as a **first-order `R`-normalized logarithmic-derivative current**, but this normalization is sharp against coherent critical packets. The next non-circular source-side input should therefore control the joint pole geometry seen by (22), rather than rely on high-frequency cancellation of the carrier in isolation.
