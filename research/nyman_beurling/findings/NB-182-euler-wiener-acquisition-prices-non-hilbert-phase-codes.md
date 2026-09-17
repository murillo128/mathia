# NB-182 — Euler-Wiener acquisition prices non-Hilbert phase codes

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-FIDELITY-BOUNDARY + WIENER-DIRICHLET + NON-HILBERT-ACQUISITION + NUCLEAR-TARIFF + NB-181-REFINEMENT`.

`NB-181` proves that bounded Hilbert acquisition of the actual-amplitude Euler feature map cannot recover a growing Hadamard-scale coordinatewise certificate. It also leaves an exact escape: the genuine scalar Euler readout uses the phase vector `(e^{-it log n})_n`, which is not in `ell^2`; its convergence comes instead from the absolute Dirichlet-series structure in `Re s>1`.

That non-Hilbert escape can itself be priced. The actual logarithmic derivative belongs, at every exterior width `a>0`, to an absolutely convergent Euler/Dirichlet algebra. After normalizing each Euler character by its capped-Poisson Lipschitz cost, the whole scalar source is a **convex combination** of unit capped-transport characters. Vertical translation, and more generally Fourier--Stieltjes mixing of vertical translations, changes only their phases. This gives a trace-norm factorization that is independent of Hilbert square summability.

The consequence is sharp at the representation level. Unit total-variation mixtures of the genuine scalar Euler translates still certify at most order-one `NB-178` complexity. A dense `N x N` phase code with singular values on the `sqrt N` scale requires RMS **Wiener acquisition gain** of order `sqrt N`. Thus the true Euler scalar readout is outside the bounded Hilbert dual, but it is not free: its natural non-Hilbert coherent acquisition has its own quantitative tariff.

Combining this tariff with the high-ordinate capped-Poisson bound of `NB-167` produces a new scale comparison. The absolute Euler acquisition budget is `asymp 1/a`, whereas the uniform high-ordinate source norm is only

\[
H_T=\min\left\{a^{-1},\frac{\log T}{\log\log T}\right\}.
\]

The ratio is `asymp 1/(aH_T)`. Matching the full generic Poisson packing dimension `N asymp 1/a` at fixed-fraction Hadamard strength therefore requires

\[
 aH_T^2=O(1).
\]

In the one-line-capped regime this leaves only the narrower window

\[
 a\lesssim \left(\frac{\log\log T}{\log T}\right)^2
\]

for a full packing-rank code under the uniform source normalization. Above that square crossover, a successful code would have to exploit additional height-specific cancellation beyond the already known uniform one-line bound.

## Claim

Fix `0<a<=1` and write

\[
\lambda_n:=\log n,
\qquad
c_{n,a}:=\frac{\Lambda(n)}{n^{1+a}}.
\]

For `lambda>=0` define the capped-character cost

\[
M_a(\lambda):=\max\{2,a\lambda\},
\tag{1}
\]

and the **Euler-Wiener acquisition budget**

\[
\mathcal W(a)
:=
\sum_{n\ge2}c_{n,a}M_a(\lambda_n).
\tag{2}
\]

Then

\[
\boxed{
\mathcal W(a)\asymp a^{-1}
\qquad(0<a\le1).
}
\tag{3}
\]

Let

\[
d_a(u,v):=\min\left\{1,\frac{|u-v|}{a}\right\},
\]

and let `mathsf D_a` be the corresponding Jordan transport norm on zero-mass finite signed measures. For every real height `t`, put

\[
K_{a,t}(u)
:=-\frac{\zeta'}{\zeta}(1+a+i(t+u)).
\tag{4}
\]

Absolute convergence gives

\[
K_{a,t}(u)
=
\sum_{n\ge2}c_{n,a}e^{-i(t+u)\lambda_n}.
\tag{5}
\]

The normalized scalar translate

\[
\Psi_{a,t}(u)
:=
\frac{K_{a,t}(u)}{\mathcal W(a)}
\tag{6}
\]

is `d_a`-contractive:

\[
\boxed{
|\Psi_{a,t}(u)-\Psi_{a,t}(v)|
\le d_a(u,v).
}
\tag{7}
\]

More generally, for a finite complex Borel measure `mu` on the height variable define the Fourier--Stieltjes acquisition

\[
\Psi_{a,\mu}(u)
:=
\int \Psi_{a,t}(u)\,d\mu(t).
\tag{8}
\]

Then

\[
|\Psi_{a,\mu}(u)-\Psi_{a,\mu}(v)|
\le \|\mu\|_{TV}d_a(u,v).
\tag{9}
\]

Now choose `N` zero-mass templates `nu_1,...,nu_N` with

\[
\mathsf D_a(\nu_i)\le qX,
\tag{10}
\]

and choose `K` acquisitions `mu_1,...,mu_K`. Let

\[
A_{ik}
:=
\frac1q\int \Psi_{a,\mu_k}(u)\,d\nu_i(u),
\tag{11}
\]

\[
Q:=
\left(
\sum_{k=1}^K\|\mu_k\|_{TV}^2
\right)^{1/2},
\qquad
G:=\frac Q{\sqrt K}.
\tag{12}
\]

Then

\[
\boxed{
\|A\|_*
\le
X\sqrt N\,Q
=
X\sqrt{NK}\,G.
}
\tag{13}
\]

If every acquisition has `||mu_k||_TV<=1`, then the probes in (11) are individually capped-transport contractive and the coordinatewise certificate of `NB-178` obeys, with `r=min{N,K}`,

\[
\boxed{
\frac{
\left(
\|A\|_*-
\epsilon\sqrt{NKr}
\right)_+^2
}{NK}
\le
\left(XG-\epsilon\sqrt r\right)_+^2
\le
\left(X-\epsilon\sqrt r\right)_+^2.
}
\tag{14}
\]

In particular, at zero tolerance this entire unit-TV non-Hilbert acquisition class certifies at most `X^2`, independently of `N` and `K`.

There is also a gain tariff with no unit-TV assumption. If `N=K` and

\[
s_j(A)\ge\alpha\sqrt N,
\qquad 1\le j\le N,
\tag{15}
\]

then necessarily

\[
\boxed{
G\ge\frac{\alpha\sqrt N}{X}.
}
\tag{16}
\]

Thus a dense rank-`N` code cannot be synthesized from the genuine scalar Euler translate family at bounded RMS Fourier--Stieltjes acquisition cost.

## Derivation

### 1. Each Euler character has an exact capped-transport cost

For `h=|u-v|`,

\[
|e^{-i\lambda u}-e^{-i\lambda v}|
\le\min\{2,\lambda h\}.
\]

If `h>=a`, division by `M_a(lambda)>=2` gives a bound by one. If `h<a`, using `M_a(lambda)>=a lambda` gives a bound by `h/a`. Hence

\[
\boxed{
\left|
\frac{e^{-i\lambda u}-e^{-i\lambda v}}
{M_a(\lambda)}
\right|
\le d_a(u,v).
}
\tag{17}
\]

Define

\[
\alpha_{n,a}
:=
\frac{c_{n,a}M_a(\lambda_n)}{\mathcal W(a)}.
\tag{18}
\]

The coefficients are positive and sum to one. Equation (5) therefore becomes

\[
\boxed{
\Psi_{a,t}(u)
=
\sum_{n\ge2}
\alpha_{n,a}
\frac{e^{-i(t+u)\lambda_n}}{M_a(\lambda_n)}.
}
\tag{19}
\]

So the normalized actual Euler kernel is literally a convex combination of unit `d_a`-Lipschitz characters. Equations (7) and (9) follow immediately.

This is the non-Hilbert analogue missing from `NB-181`: no `ell^2` phase vector is introduced. The source is controlled by the `ell^1`/Wiener mass of its absolutely convergent Euler coefficients after charging each frequency its correct capped-Lipschitz cost.

### 2. The Euler-Wiener budget is exactly inverse-width scale

Put

\[
L(a)
:=
\sum_{n\ge2}\frac{\Lambda(n)}{n^{1+a}}
=-\frac{\zeta'}{\zeta}(1+a),
\]

and

\[
J(a)
:=
\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+a}}
=-L'(a).
\]

The Laurent expansion at the pole of `zeta` gives

\[
L(a)=a^{-1}+O(1),
\qquad
J(a)=a^{-2}+O(1)
\qquad(a\downarrow0).
\tag{20}
\]

Since

\[
2\le M_a(\lambda)\le2+a\lambda,
\]

we have

\[
2L(a)
\le
\mathcal W(a)
\le
2L(a)+aJ(a).
\tag{21}
\]

Equations (20)--(21), together with continuity on every compact subinterval of `(0,1]`, prove (3).

The scale `1/a` is therefore not an arbitrary norm choice. It is the absolute Euler exposure required to synthesize the scalar logarithmic derivative while respecting one Poisson-width capped-transport geometry.

### 3. Fourier--Stieltjes acquisition has a nuclear factorization

For each template and Euler frequency set

\[
b_{i,n}
:=
\frac1q
\int
\frac{e^{-iu\lambda_n}}
{M_a(\lambda_n)}
\,d\nu_i(u).
\tag{22}
\]

By (17) and capped Kantorovich--Rubinstein duality,

\[
|b_{i,n}|\le X.
\tag{23}
\]

Let

\[
b_n:=(b_{1,n},\ldots,b_{N,n})^T,
\qquad
h_n:=
\bigl(
\widehat\mu_1(\lambda_n),\ldots,
\widehat\mu_K(\lambda_n)
\bigr)^T,
\]

with `hat mu(lambda)=int e^{-it lambda} dmu(t)`. Then

\[
\|b_n\|_2\le X\sqrt N,
\qquad
\|h_n\|_2\le Q.
\tag{24}
\]

Using (19), the response matrix factors as the absolutely convergent rank-one sum

\[
A
=
\sum_{n\ge2}
\alpha_{n,a}
 b_n h_n^T.
\tag{25}
\]

The nuclear norm of a rank-one matrix is the product of the Euclidean norms of its two vectors. Since the `alpha_n` are positive and sum to one,

\[
\|A\|_*
\le
\sum_n
\alpha_{n,a}
\|b_n\|_2\|h_n\|_2
\le
X\sqrt N\,Q,
\]

which proves (13). Equation (14) is then the `NB-178` coordinatewise certificate, while (15) implies `||A||_*>=alpha N^(3/2)` and comparison with (13) proves (16).

The important point is that this bound covers the exact phase acquisition that escaped `NB-181`: a genuine height evaluation is `mu=delta_t`, so its acquisition cost in (12) is exactly one. Arbitrary finite mixtures of heights are included as well.

## High-ordinate arithmetic cancellation becomes an explicit acquisition gain

The absolute Euler budget is intentionally source-blind about cancellation between frequencies. The high-ordinate zeta source does better. Let

\[
H_T
:=
\min\left\{\frac1a,\frac{\log T}{\log\log T}\right\}.
\tag{26}
\]

For fixed support radius `B`, `NB-167` gives a constant `C_B` such that, for all sufficiently large `T`, every `t in [T,2T]` satisfies

\[
|K_{a,t}(u)-K_{a,t}(v)|
\le
C_B H_T d_a(u,v),
\qquad |u|,|v|\le B.
\tag{27}
\]

Hence the directly source-normalized probes

\[
\ell_t^{src}(\sigma)
:=
\frac1{qC_BH_T}
\int K_{a,t}(u)\,d\sigma(u)
\tag{28}
\]

are coordinatewise contractive. In the acquisition class above they are exactly

\[
\ell_t^{src}
=
\kappa_T\,\ell_{\delta_t}^{W},
\qquad
\kappa_T
:=
\frac{\mathcal W(a)}{C_BH_T}
\asymp_B
\frac1{aH_T},
\tag{29}
\]

where `ell^W` denotes the `mathcal W(a)`-normalized source probe.

Thus the uniform one-line cancellation has a precise representation meaning: it buys an acquisition gain `kappa_T` over the absolute-convergence/Wiener baseline. Applying (13) with `mu_k=kappa_T delta_{t_k}` gives, for any heights `t_1,...,t_K in [T,2T]`,

\[
\boxed{
\|A^{src}\|_*
\le
\kappa_T X\sqrt{NK}.
}
\tag{30}
\]

If `N=K` and the source-normalized response has all singular values at least `cX sqrt N` for some fixed `c>0`, then

\[
\boxed{
N\ll_{B,c}\kappa_T^2
\asymp_B
\frac1{a^2H_T^2}.
}
\tag{31}
\]

This is a conditioning tariff, not an assertion that `kappa_T` is the largest possible gain at every individual height. Equation (27) supplies a uniform source-safe normalization. If a selected set of heights admits much smaller actual capped-Lipschitz norm, it may support larger gains, but those gains are additional height-specific arithmetic cancellation and must be paid explicitly in (16).

## Comparison with the generic Poisson packing

`NB-179` shows that bare capped-Poisson geometry supports a synthetic Hadamard code at dimension

\[
N_{pack}\asymp_B a^{-1}
\tag{32}
\]

with singular values a fixed fraction of `X sqrt(N_pack)`. For the actual Euler translate family under the uniform source normalization (28) to match that full geometric packing rank, (31)--(32) force

\[
\boxed{
aH_T^2\ll_B1.}
\tag{33}
\]

This exposes a square crossover that was invisible in `NB-181`.

If

\[
a\le\frac{\log\log T}{\log T},
\]

then `H_T=log T/log log T`, and (33) becomes

\[
\boxed{
 a
\ll_B
\left(\frac{\log\log T}{\log T}\right)^2.
}
\tag{34}
\]

Therefore throughout the intermediate boundary layer

\[
\left(\frac{\log\log T}{\log T}\right)^2
\ll a
\le
\frac{\log\log T}{\log T},
\]

the uniform high-ordinate Euler acquisition cannot realize a full Poisson-packing-rank Hadamard response. Any such response must exploit additional height-specific cancellation beyond the uniform one-line control.

In the complementary regime `H_T=1/a`, one has `kappa_T=Theta_B(1)`. Hence a growing `N asymp1/a` full packing code is again excluded under the source-safe normalization as `a->0`.

The theorem does **not** close the thinner region `aH_T^2=O(1)`. In particular, once `a` is at or below the square one-line scale, the absolute Euler acquisition budget is large enough that the present nuclear argument no longer separates actual source translates from generic packing at full rank.

## Self-adversarial audit

The new tariff concerns a restricted but source-natural acquisition architecture: vertical translates of the actual absolutely convergent Euler series and their finite Fourier--Stieltjes mixtures. It does not upper-bound the primal quantity `mathfrak L_T(epsilon)` and does not rule out other nonlinear or non-translation-based source probes.

The Wiener budget `mathcal W(a)` deliberately absolute-values the Euler channels. It therefore discards the arithmetic cancellation that makes the high-ordinate logarithmic derivative much smaller than `1/a`. The factor `kappa_T` records exactly how much of that cancellation is being used as acquisition gain; it should not be interpreted as computational cost or as a lower bound for the true pointwise norm of `zeta'/zeta`.

Equation (31) is a necessary condition for a dense code in the declared source normalization, not a sufficient construction. Paying the required gain does not produce orthogonal phase directions. Conversely, exceptional heights may have much smaller local source norm than the uniform `C_BH_T` bound and can therefore pay more gain. A future positive-density argument would have to control how often such exceptional acquisition gains occur.

The full-packing comparison uses the same capped-Poisson amplitude `X` on both sides and asks for singular values that are a fixed fraction of the maximal `X sqrt N` scale. It does not claim that the synthetic `NB-179` dipoles are realized by Nyman samplers.

Nothing here removes the sparse-height escape, the ultra-thin limitation inherited from the stationary mean-square theorem, or the final gap back to global Nyman--Beurling approximation. The result only narrows the post-`NB-181` representation question: moving from `ell^2` to the obvious absolutely convergent non-Hilbert source class does not make coherent phase acquisition free.

## Representation and prior-art audit

The generic representation is classical. Absolutely convergent Dirichlet series form a Wiener--Dirichlet algebra; the literature on that algebra includes Bayart, Finet, Li and Queffélec, *Composition operators on the Wiener-Dirichlet algebra* (arXiv:0904.2527), and related work on Banach algebras of Dirichlet series. Fourier--Stieltjes transforms of finite measures and the triangle inequality for nuclear norms are likewise standard background.

The line-specific content is the combination proved here: charge each actual Euler coefficient by the capped-Poisson character cost `max(2,a log n)`, identify the resulting source budget as `Theta(1/a)`, factor the full family of vertical zeta-logarithmic-derivative acquisitions through a convex rank-one mixture, and compare that tariff with both the `NB-167` high-ordinate norm `H_T` and the exact Poisson packing dimension from `NB-179`.

A focused search over Wiener--Dirichlet algebras, absolutely convergent zeta logarithmic derivatives, Fourier--Stieltjes acquisitions and Nyman--Beurling approximation located the standard surrounding ingredients but not this capped-transport/nuclear-capacity comparison. That absence is not used as novelty evidence. No external theorem is load-bearing: the Euler expansion, pole asymptotics, character contraction and nuclear factorization needed above are proved directly. `research/nyman_beurling/SOURCES.md` therefore remains unchanged.

## Evidence ledger

**Internal load-bearing dependencies:** `NB-167` for the uniform high-ordinate capped-Poisson source norm; `NB-178` for the coordinatewise nuclear certificate; `NB-179` for the exact generic Poisson-packing control; `NB-181` for the bounded-Hilbert acquisition boundary being refined.

**External load-bearing dependencies:** none.

**Context-only prior art consulted:** classical Wiener--Dirichlet/absolutely convergent Dirichlet-series Banach algebras and Fourier--Stieltjes measure algebras.

## Frontier moved

`NB-181` leaves the genuine Euler scalar sum outside its Hilbert tariff. `NB-182` shows that this escape has a natural finite non-Hilbert budget: after capped-character normalization, the scalar Euler source is an `ell^1` convex mixture, and dense phase-code response requires RMS Fourier--Stieltjes acquisition gain `Omega(sqrt N)`.

The next sharp question is therefore not merely to choose a Banach space larger than `ell^2`. It is to determine whether **height-specific arithmetic cancellation can make the capped-Lipschitz norm of the actual Euler translate anomalously smaller than the uniform `H_T` scale on enough heights to pay the missing acquisition gain**, especially in the surviving square-boundary window `aH_T^2=O(1)`. A negative distributional theorem for that gain would turn the present representation tariff into a genuine source-persistence obstruction; a positive construction would finally identify arithmetic coherence unavailable to the generic Poisson packing.