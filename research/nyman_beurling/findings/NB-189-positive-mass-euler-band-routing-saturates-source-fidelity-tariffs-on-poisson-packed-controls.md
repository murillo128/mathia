# NB-189 — Positive-mass Euler band routing saturates source-fidelity tariffs on Poisson-packed controls

**Date:** 2026-09-17  
**Status:** `DERIVED + MATCHED-CONTROL + SOURCE-FIDELITY + EULER-WIENER + POSITIVE-MASS-BAND-ROUTING + FOURIER-CODE + NB-188-STRESS-TEST`.

`NB-188` narrows the same-frequency Wiener escape to low-fanout routing with square-root source-density gain. The cheapest surviving architecture is therefore a partition of the true Euler-Wiener population into disjoint source bins, each normalized separately. It is not clear a priori whether such a partition can actually preserve the `K^(3/2)` nuclear response required by `NB-178`, or whether the true Euler amplitudes make the surviving representation class empty.

They do not. A completely deterministic contiguous partition in **logarithmic frequency**, using the true von-Mangoldt amplitudes and no frequency-dependent phase tuning at all, already realizes Hadamard-scale nuclear response on a Poisson-packed matched control. The construction uses `K asymp 1/a` disjoint bands from a fixed positive-mass part of the normalized Euler-Wiener source. Each band has unit absolute Wiener budget, the effective fanout is exactly one, and the collective source-density gain is `asymp sqrt K`, exactly the order forced by `NB-188`. Yet on `K` Poisson-separated dipole templates the resulting response matrix is, up to a common row envelope and a rank-one zero-mass correction, an ordinary discrete Fourier matrix.

Thus the `NB-188` tariffs are sharp at the representation level. More importantly, **probe-side Euler source fidelity plus bounded fanout is still not an arithmetic discriminator**: the generic capped-Poisson packing control can already be read at full linear complexity by positive-mass true-amplitude Euler band probes. Any stronger source-specific argument must either charge independent spectral-band access itself, restrict acquisition to what can be generated from the scalar Euler translate family without coefficient-side filtering, or exploit a property of the actual realized Nyman template range that the packed control does not share.

## Setup

Use the normalized Euler-Wiener atoms of `NB-182` and `NB-188`,

\[
\lambda_n:=\log n,
\qquad
M_a(\lambda):=\max\{2,a\lambda\},
\]

\[
\phi_{n,a}(u)
:=
\frac{e^{-iu\lambda_n}}{M_a(\lambda_n)},
\qquad
\alpha_{n,a}
:=
\frac{\Lambda(n)n^{-1-a}M_a(\lambda_n)}{\mathcal W(a)},
\tag{1}
\]

so `alpha_(n,a)>=0`, `sum_n alpha_(n,a)=1`, and each `phi_(n,a)` is unit contractive for

\[
d_a(u,v)=\min\left\{1,\frac{|u-v|}{a}\right\}.
\tag{2}
\]

Fix once and for all

\[
0<r_0<r_1<2
\tag{3}
\]

and a band width `Delta>0` satisfying

\[
\frac{2\pi}{\Delta}<B.
\tag{4}
\]

For sufficiently small `a`, put

\[
K=K(a)
:=
\left\lfloor
\frac{r_1-r_0}{a\Delta}
\right\rfloor,
\qquad
L_k:=\frac{r_0}{a}+k\Delta,
\qquad
0\le k<K,
\tag{5}
\]

and define disjoint logarithmic-frequency bands

\[
S_{k,a}
:=
\{n\ge2:L_k\le\log n<L_k+\Delta\}.
\tag{6}
\]

Because every active channel obeys `a log n<r_1+o(1)<2`, the capped-character cost is exactly

\[
M_a(\lambda_n)=2
\qquad(n\in S_{k,a}).
\tag{7}
\]

Let the normalized source mass of the `k`th band be

\[
\theta_{k,a}
:=
\sum_{n\in S_{k,a}}\alpha_{n,a},
\tag{8}
\]

and route that band into one probe by

\[
\beta_{k,n}
:=
\frac{\alpha_{n,a}}{\theta_{k,a}}
\mathbf 1_{n\in S_{k,a}},
\qquad
F_{k,a}(u)
:=
\sum_n\beta_{k,n}\phi_{n,a}(u).
\tag{9}
\]

There is no channelwise phase mask in (9): every coefficient is positive. Define

\[
\ell_{k,a}(\sigma)
:=
\frac1q\int F_{k,a}(u)\,d\sigma(u).
\tag{10}
\]

Since `sum_n |beta_(k,n)|=1`, every `ell_(k,a)` is coordinatewise contractive for the `NB-178` capped-transport norm.

## Claim 1: the bands route a fixed positive fraction of the true source at the exact NB-188 tariff

Uniformly for `0<=k<K`, the prime number theorem gives

\[
\boxed{
\theta_{k,a}
=
\frac{2e^{-aL_k}(1-e^{-a\Delta})}
{2+e^{-2}}
+o(a).
}
\tag{11}
\]

Consequently

\[
\theta_{k,a}\asymp a,
\qquad
K\asymp a^{-1},
\tag{12}
\]

and the total normalized Euler-Wiener mass routed by the bands has the positive limit

\[
\boxed{
\sum_{k=0}^{K-1}\theta_{k,a}
\longrightarrow
\Theta_{r_0,r_1}
:=
\frac{2(e^{-r_0}-e^{-r_1})}{2+e^{-2}}
>0.
}
\tag{13}
\]

The bands are disjoint, so in the notation of `NB-188` their effective fanout is exactly

\[
\boxed{
\mathcal F_{\rm eff}=1.
}
\tag{14}
\]

Their source-density gain is

\[
\mathcal G_\alpha^2
=
\frac1K\sum_{k=0}^{K-1}\frac1{\theta_{k,a}}
\asymp
\frac1a
\asymp K,
\tag{15}
\]

hence

\[
\boxed{
\mathcal G_\alpha\asymp\sqrt K.
}
\tag{16}
\]

Thus this elementary band routing lands exactly on the surviving order of magnitude from `NB-188`: positive source mass, bounded fanout, unit absolute Wiener budget per output coordinate, and square-root source-density amplification.

## Claim 2: every band has the same local Fourier envelope

For bounded `u`, define

\[
R_{a,\Delta}(u)
:=
\frac{
\int_0^\Delta e^{-(a+iu)x}\,dx
}{
\int_0^\Delta e^{-ax}\,dx
}.
\tag{17}
\]

Then the PNT gives, uniformly for `0<=k<K` and `|u|<=B`,

\[
\boxed{
F_{k,a}(u)
=
\frac12
e^{-iuL_k}R_{a,\Delta}(u)
+o(1).
}
\tag{18}
\]

Moreover,

\[
R_{a,\Delta}(u)
\longrightarrow
R_{0,\Delta}(u)
:=
 e^{-iu\Delta/2}
\frac{\sin(u\Delta/2)}{u\Delta/2}
\tag{19}
\]

uniformly on `[-B,B]`, with the value at `u=0` interpreted by continuity.

Equation (18) is the key structural fact. After true-amplitude normalization, consecutive fixed-width logarithmic Euler bands are asymptotically the **same local envelope multiplied by consecutive Fourier carriers** `e^(-iu k Delta)`. No prime-phase box hitting or arbitrary coefficient oracle is needed.

## Claim 3: Poisson-packed dipoles turn those bands into a DFT-scale nuclear code

Choose

\[
u_i
:=
\frac{2\pi i}{K\Delta},
\qquad
0\le i<K.
\tag{20}
\]

By (4), all these points lie in `[0,B)` for small `a`. Fix `v=-B` and, for any fixed `X>0`, define zero-mass matched-control templates

\[
\nu_i
:=
qX(\delta_{u_i}-\delta_v).
\tag{21}
\]

For sufficiently small `a`, `|u_i-v|>a`, so

\[
\mathsf D_a(\nu_i)=qX.
\tag{22}
\]

Let

\[
A_{ik}
:=
\ell_{k,a}(\nu_i)
=
X\bigl(F_{k,a}(u_i)-F_{k,a}(v)\bigr).
\tag{23}
\]

First ignore the common reference value `F_(k,a)(v)` and write

\[
E_{ik}:=XF_{k,a}(u_i).
\tag{24}
\]

Equations (5), (18) and (20) give

\[
E_{ik}
=
\frac X2
R_{a,\Delta}(u_i)
 e^{-iu_i r_0/a}
 e^{-2\pi iik/K}
+o(X)
\tag{25}
\]

uniformly in `i,k`. Thus, up to an entrywise `o(X)` error, `E` is a diagonal row multiplier times the unnormalized `K x K` discrete Fourier matrix. Its main-term singular values are

\[
\frac{X\sqrt K}{2}
|R_{a,\Delta}(u_i)|,
\qquad 0\le i<K.
\tag{26}
\]

Since

\[
\frac{u_i\Delta}{2}=\frac{\pi i}{K},
\]

the Riemann sum in (19) yields

\[
\frac1K\sum_{i=0}^{K-1}
|R_{a,\Delta}(u_i)|
\longrightarrow
\int_0^1
\frac{\sin(\pi x)}{\pi x}\,dx
=
\frac{\operatorname{Si}(\pi)}{\pi}.
\tag{27}
\]

Therefore

\[
\boxed{
\|E\|_*
=
\left(
\frac{\operatorname{Si}(\pi)}{2\pi}
+o(1)
\right)
XK^{3/2}.
}
\tag{28}
\]

The zero-mass correction is only rank one. Indeed,

\[
A
=
E-X\mathbf 1 c^T,
\qquad
c_k:=F_{k,a}(v).
\tag{29}
\]

Because every active atom has modulus `1/2` and every coefficient row in (9) is a probability vector,

\[
|c_k|\le\frac12.
\]

Hence

\[
\|X\mathbf 1c^T\|_*
\le
\frac X2 K
=o(XK^{3/2}).
\tag{30}
\]

Combining (28)--(30) gives the matched-control response

\[
\boxed{
\|A\|_*
\ge
\left(
\frac{\operatorname{Si}(\pi)}{2\pi}
-o(1)
\right)
XK^{3/2}.
}
\tag{31}
\]

The constant `Si(pi)/(2 pi)` is about `0.295`; only its positivity matters.

Consequently, if a synthetic adaptive family has realized range containing the templates (21), the coordinatewise certificate `NB-178` gives, for every fixed

\[
0\le\epsilon<rac{\operatorname{Si}(\pi)}{2\pi}X,
\]

\[
\boxed{
\mathfrak L_T(\epsilon)
\ge
K
\left(
\frac{\operatorname{Si}(\pi)}{2\pi}X
-
\epsilon
-o(1)
\right)^2.
}
\tag{32}
\]

Thus true-amplitude Euler bands recover **linear Poisson-scale source complexity** on the same kind of non-arithmetic packed control that stress-tested `NB-178` in `NB-179`.

## Derivation of the PNT band profile

Write

\[
S_a(L,u)
:=
\sum_{L\le\log n<L+\Delta}
\frac{\Lambda(n)}{n^{1+a+iu}}.
\tag{33}
\]

The prime number theorem in the form

\[
\psi(x)=x+o(x)
\]

implies, uniformly for `L>=r_0/a` and `|u|<=B`,

\[
\boxed{
S_a(L,u)
=
\int_L^{L+\Delta}e^{-(a+iu)x}\,dx
+o(1).
}
\tag{34}
\]

To see the uniformity, write `psi(x)=x+E(x)` with

\[
\sup_{x\ge e^{r_0/a}}
\frac{|E(x)|}{x}
\longrightarrow0.
\]

Stieltjes integration by parts on the fixed multiplicative interval `[e^L,e^(L+Delta)]` bounds both endpoint terms and the integral involving `E(x)` by this supremum times a constant depending only on `B` and `Delta`. This proves (34) without any short-interval prime theorem: the arithmetic intervals have fixed multiplicative ratio `e^Delta`.

At `u=0`, (34) gives

\[
S_a(L_k,0)
=
e^{-aL_k}
\frac{1-e^{-a\Delta}}a
+o(1).
\tag{35}
\]

Since `M_a=2` on the bands and `a mathcal W(a)->2+e^(-2)` by `NB-187`, equations (8) and (35) give (11). Summing the resulting geometric progression proves (13).

Likewise, (7)--(9) make the global Wiener normalization cancel inside each band:

\[
F_{k,a}(u)
=
\frac12
\frac{S_a(L_k,u)}{S_a(L_k,0)}.
\tag{36}
\]

Dividing (34) at `u` by (34) at zero yields (18). The denominator in (35) is uniformly bounded away from zero before the global `a` normalization, so the ratio error remains `o(1)` uniformly in `k` and bounded `u`.

Finally, the entrywise `o(1)` error in (25) contributes `o(K^(3/2))` to the nuclear norm: its Frobenius norm is `o(K)`, and rank at most `K` converts this to nuclear norm `o(K^(3/2))`. Hence the DFT main term controls (28) at the exact scale needed.

## What this resolves after NB-188

`NB-188` proves that a Hadamard-scale response in the same-frequency Wiener class cannot come from bounded source-relative rephasing or broad fanout. The balanced partition architecture was left as the extremal representation that pays both tariffs sharply, but its ability to carry an actual code was open.

The construction above shows that this surviving corner is nonempty in a particularly rigid form:

- the routing uses **disjoint contiguous log-frequency bands**, so fanout is one;
- it uses a fixed positive fraction of the true normalized Euler-Wiener mass;
- every coefficient is the actual positive Euler-Wiener coefficient followed only by the required per-band normalization;
- there is no channelwise phase choice, randomized mask, Kronecker recurrence or selection of exceptional primes;
- the resulting probes nevertheless produce `Theta(K^(3/2))` nuclear response on a Poisson-packed matched control.

Thus neither the square-root density tariff nor bounded fanout is by itself a no-go mechanism. They are the exact price of converting the scalar positive Euler source into `K asymp1/a` separately normalized spectral bands, and that price is sufficient to reconstruct a full Fourier code in the ambient capped-Poisson geometry.

This sharpens the interpretation of `NB-187` as well. A positive construction does not need to isolate only `K` individual prime channels from the exponentially large Euler population. It can aggregate that population into `K` macroscopic logarithmic bands, each carrying mass `Theta(a)`, and recover `K` effective Fourier coordinates. The exponential channel-cardinality mismatch disappears once the weak channels are grouped before normalization.

## Representation and generality audit

**Generality audited.** The DFT diagonalization, Riemann-sum limit and the fact that fixed-width frequency blocks become modulated copies of one envelope are generic Fourier facts. The same construction would work for any positive Dirichlet source whose coefficient-counting measure has a smooth nonzero limiting density on the scaled logarithmic coordinate. No novelty is claimed for frequency blocking or Fourier matrices.

The arithmetic-specific input is the exact Euler-Wiener atomic decomposition of `NB-182`, the scaled source law of `NB-187`, and the PNT statement that the von-Mangoldt mass in every fixed multiplicative band is asymptotic to Lebesgue mass in logarithmic coordinates. Those facts make (9) a true-amplitude Euler construction rather than a synthetic Fourier basis inserted by hand.

The matched-control boundary is equally important. The templates (21) are synthetic zero-mass dipoles. This finding does **not** prove that the actual realized Nyman sampler range contains these templates, approximates them, or can coordinate them independently. It therefore does not prove that the true Nyman complexity grows like `1/a`, nor does it imply logarithmic Euler rescue or RH.

There is also an acquisition boundary. The probes use coefficient-side **band selection**. They are much more structured than the arbitrary masks permitted by `NB-188`, but they are not generated by a unit-TV mixture of scalar vertical translates; `NB-182` already rules out that bounded-gain class. Operationally, the new resource is access to `K` independently normalized spectral projections of the Euler Dirichlet series. Treating those projections as free would be an oracle if the only physical source observable were the scalar function `-zeta'/zeta(1+a+it)`. The theorem says precisely that this is now the resource that must be charged or derived.

## Prior-art audit

Focused searches were made for Nyman--Beurling frequency-band decompositions, Littlewood--Paley/block decompositions of Dirichlet series, logarithmic-frequency projections of the zeta logarithmic derivative, and Fourier/Vandermonde sampling of Dirichlet polynomials. Frequency blocking, Littlewood--Paley theory for Hardy spaces of Dirichlet series, and Fourier analysis of Dirichlet polynomials are classical neighboring technologies; recent work on Littlewood--Paley formulas for Dirichlet-series Hardy spaces and on large values of Dirichlet polynomials confirms that this surrounding representation is standard.

No source located in this pass states the line-specific claim proved here: that a fixed positive fraction of the **NB-182 Euler-Wiener acquisition measure**, divided into `K asymp1/a` contiguous logarithmic bands and normalized bandwise, saturates the `NB-188` density/fanout tariffs and yields a `K^(3/2)` DFT-scale response on Poisson-packed matched controls. No new external theorem is load-bearing beyond the PNT consequences already anchored in `SOURCES.md`, so `SOURCES.md` is unchanged.

## Self-review

The strongest possible overclaim would be to call (31) a source-faithful Nyman certificate. It is not. The **probes** are source-faithful within the declared same-frequency Euler-Wiener model; the **templates** are matched synthetic controls. `NB-178` only turns the matrix into a lower bound for `mathfrak L_T` when those templates belong to the realized range. Equation (32) is therefore explicitly conditional on the synthetic range containing (21).

A second overclaim would be to regard the band probes as free observations of zeta. The construction assumes coefficient-side access to disjoint logarithmic blocks. Recovering `K` such blocks from only scalar vertical samples may itself require a large inversion window, large total variation, or another resource. None of those costs is estimated here. The finding instead identifies **independent spectral-band access** as the next acquisition currency that a genuine source argument must price.

The use of the region `r_1<2` is a convenience that makes `M_a(lambda)=2` exactly and produces the clean factor `1/2`. Bands in the `a lambda>2` region have a slowly varying capped-character normalization and should give the same qualitative Fourier-block mechanism after carrying that envelope through the calculation. No claim about the optimal constant or maximal source fraction is intended.

The DFT code is nuclear rather than uniformly Hadamard in every singular direction: the sinc envelope makes some edge singular values small. That is sufficient for `NB-178`, whose certificate uses the nuclear norm. The positive average in (27) is the exact reason the response still has `Theta(K^(3/2))` mass.

## Research consequence

The post-`NB-188` frontier should no longer ask only whether bounded-fanout aggregation of exponentially many true Euler channels can preserve growing phase complexity. **It can, at the representation level, by contiguous band routing.** The sharper discriminator is whether those `K asymp1/a` independently normalized Euler bands can be obtained from the actual scalar source with affordable acquisition cost, and whether the actual realized Nyman template range responds to them with comparable nuclear mass after the generic Poisson packing mechanism is matched out.

A negative next step should therefore target the band-selection operator itself: prove a lower bound for synthesizing `K` disjoint normalized log-frequency projections from scalar vertical translates or from whatever source observables are declared admissible. A positive next step should instead derive such a multiband acquisition from genuine zeta data and test its response on actual Nyman templates rather than synthetic dipoles.