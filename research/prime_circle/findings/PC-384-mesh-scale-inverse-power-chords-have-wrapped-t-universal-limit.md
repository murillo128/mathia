# PC-384 — mesh-scale inverse-power chords have a wrapped-t universal limit

**Status:** `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the fixed positive inverse-power extension of the shrinking common-anchor chord branch left open by PC-383.

PC-383 classifies the regularized inverse chord itself. Its exact mesh-scale modulus is a Poisson kernel, independent of whether the refinement degree is prime or composite. A natural escape is to change the singularity rather than the scale: replace the inverse chord by an arbitrary fixed positive inverse power and ask whether a different exponent produces a degree-sensitive order-one defect.

It does not. There is a sharp analytic threshold at squared-weight exponent `alpha=1/2`, but neither side carries arithmetic information. Below and at the threshold the normalized fiber energy becomes asymptotically QMF. Above it, an order-one profile survives, but the profile is the classical wrapped Student-t family; it depends only on the singularity exponent and the dimensionless mesh parameter, not on primality or factorization of the refinement degree. The Poisson kernel of PC-383 is exactly its `alpha=1` member.

Thus the whole family of fixed positive inverse powers of the regularized common-anchor chord is degree-blind at exact mesh scale after the intrinsic `L^2` normalization used in PC-380--PC-383. Changing the scalar singular exponent does not rescue the prime-sensitive modulus branch.

## 1. Fixed inverse-power family at the inverse-image mesh scale

Let normalized Haar measure on the unit circle be `dm`, let

\[
(V_m f)(z)=f(z^m),
\qquad
(E_m g)(z)=\frac1m\sum_{w^m=z}g(w),
\tag{1}
\]

and fix `alpha>0` and `tau>0`. Write

\[
\eta_m=\frac{\tau}{m},
\qquad
\varepsilon_m=2\sinh\frac{\eta_m}{2}.
\tag{2}
\]

The regularized inverse-power chord amplitude is

\[
q_{\alpha,m}(e^{i\theta})
=\bigl(2(\cosh\eta_m-\cos\theta)\bigr)^{-\alpha/2}
=\bigl(|1-e^{i\theta}|^2+\varepsilon_m^2\bigr)^{-\alpha/2}.
\tag{3}
\]

Its squared weight and normalization are

\[
g_{\alpha,m}(\theta)
=|q_{\alpha,m}(e^{i\theta})|^2
=\bigl(2(\cosh(\tau/m)-\cos\theta)\bigr)^{-\alpha},
\tag{4}
\]

\[
c_{\alpha,m}
=\int_{\mathbb T}g_{\alpha,m}\,dm.
\tag{5}
\]

For

\[
S_{m,\alpha,\tau}=M_{q_{\alpha,m}}V_m,
\qquad
T_{m,\alpha,\tau}=c_{\alpha,m}^{-1/2}S_{m,\alpha,\tau},
\tag{6}
\]

the positive operator is exactly

\[
T_{m,\alpha,\tau}^*T_{m,\alpha,\tau}
=M_{A_{m,\alpha,\tau}},
\qquad
A_{m,\alpha,\tau}
=\frac{E_m g_{\alpha,m}}{c_{\alpha,m}}.
\tag{7}
\]

The question is therefore whether the normalized root-fiber energy `A_(m,alpha,tau)` retains any arithmetic dependence on the integer degree `m` as `m` grows through prime or composite values.

## 2. There is a sharp threshold at `alpha=1/2`

The answer is a three-regime asymptotic classification.

### Subcritical singularity: `0<alpha<1/2`

At zero regularization the boundary singularity

\[
\bigl(2(1-\cos\theta)\bigr)^{-\alpha}
\asymp |\theta|^{-2\alpha}
\tag{8}
\]

is integrable. Consequently

\[
c_{\alpha,m}\longrightarrow
c_{\alpha,0}
:=\frac1{2\pi}\int_{-\pi}^{\pi}
\bigl(2(1-\cos\theta)\bigr)^{-\alpha}\,d\theta
\in(0,\infty).
\tag{9}
\]

The shifted root samples form a Riemann sum away from the anchor. In a shrinking anchor neighborhood, the largest possible single contribution after the `1/m` fiber normalization is

\[
O\!\left(\frac{m^{2\alpha}}m\right)
=O(m^{2\alpha-1})=o(1).
\tag{10}
\]

Splitting the circle into that neighborhood and its smooth complement gives, uniformly in the base angle,

\[
E_m g_{\alpha,m}=c_{\alpha,0}+o(1).
\tag{11}
\]

Hence

\[
\boxed{
\|A_{m,\alpha,\tau}-1\|_\infty\to0,
\qquad 0<\alpha<\tfrac12.
}
\tag{12}
\]

The mesh-scale singularity is too weak to survive normalized fiber averaging.

### Critical singularity: `alpha=1/2`

At the borderline, both the circle integral and the root sum have the same logarithmic divergence. Uniformly in the base angle,

\[
c_{1/2,m}=\frac1\pi\log m+O(1),
\tag{13}
\]

\[
E_m g_{1/2,m}=\frac1\pi\log m+O(1).
\tag{14}
\]

The `O(1)` terms can depend on `tau` and on the base angle but remain uniformly bounded for fixed `tau>0`. Therefore

\[
\boxed{
\|A_{m,1/2,\tau}-1\|_\infty
=O\!\left(\frac1{\log m}\right)
\to0.
}
\tag{15}
\]

Even the critical inverse-power singularity returns asymptotically to the QMF/isometric limit.

### Supercritical singularity: `alpha>1/2`

Now the mesh-scale anchor neighborhood dominates both numerator and normalization. Put `z=e^{ix}` with `x in [-pi,pi]` and reindex the `m` inverse images symmetrically around the anchor. For each fixed integer `k`,

\[
m^2\,2\!\left(
\cosh\frac\tau m
-
\cos\frac{x+2\pi k}{m}
\right)
\longrightarrow
\tau^2+(x+2\pi k)^2.
\tag{16}
\]

The elementary lower bound for `sin u/u` on the represented half-circle gives a summable majorant of the form

\[
C_{\alpha,\tau}(1+k^2)^{-\alpha},
\tag{17}
\]

and this is summable precisely in the present regime `alpha>1/2`. Dominated convergence therefore yields uniformly in `x`,

\[
\boxed{
m^{1-2\alpha}
(E_m g_{\alpha,m})(e^{ix})
\longrightarrow
\sum_{k\in\mathbb Z}
\frac1{\bigl((x+2\pi k)^2+\tau^2\bigr)^\alpha}.
}
\tag{18}
\]

The same local rescaling in the Haar integral gives

\[
\boxed{
m^{1-2\alpha}c_{\alpha,m}
\longrightarrow
C_{\alpha,\tau}
:=\frac1{2\pi}\int_{\mathbb R}(u^2+\tau^2)^{-\alpha}\,du
=\frac{\Gamma(\alpha-\tfrac12)}{2\sqrt\pi\,\Gamma(\alpha)}
\tau^{1-2\alpha}.
}
\tag{19}
\]

Thus

\[
\boxed{
\|A_{m,\alpha,\tau}-W_{\alpha,\tau}\|_\infty\to0,
\qquad \alpha>\tfrac12,
}
\tag{20}
\]

where the universal mean-one limit is

\[
\boxed{
W_{\alpha,\tau}(x)
=
\frac{
\displaystyle\sum_{k\in\mathbb Z}
\bigl((x+2\pi k)^2+\tau^2\bigr)^{-\alpha}}
{
\displaystyle
\frac{\Gamma(\alpha-\tfrac12)}{2\sqrt\pi\,\Gamma(\alpha)}
\tau^{1-2\alpha}}
.}
\tag{21}
\]

In operator language,

\[
\boxed{
T_{m,\alpha,\tau}^*T_{m,\alpha,\tau}
\longrightarrow M_{W_{\alpha,\tau}}
\quad\text{in operator norm}.
}
\tag{22}
\]

The limit contains `alpha` and `tau`, but no residue of whether the refinement degree was prime, a prime power, squarefree composite, or otherwise factored.

## 3. The surviving profile is the classical wrapped Student-t family

Set

\[
\nu=\alpha-\frac12>0.
\tag{23}
\]

Poisson summation applied to `(u^2+tau^2)^(-alpha)` gives the Fourier expansion

\[
W_{\alpha,\tau}(x)
=1+2\sum_{n\ge1}b_n(\alpha,\tau)\cos(nx),
\tag{24}
\]

with

\[
\boxed{
b_n(\alpha,\tau)
=
\frac{2^{1-\nu}}{\Gamma(\nu)}
(n\tau)^\nu K_\nu(n\tau),
\qquad n\ge1,
}
\tag{25}
\]

where `K_nu` is the modified Bessel function of the second kind.

This is not a new prime-circle spectral family. Up to the factor `2pi` converting a probability density to a mean-one circle function, (21) is exactly the density obtained by wrapping a centered Student-t random variable. Indeed a Student-t law with

\[
d=2\alpha-1,
\qquad
s=\frac\tau{\sqrt d}
\tag{26}
\]

has real-line density proportional to `(u^2+tau^2)^(-alpha)`; periodizing it modulo `2pi` gives (21). Pewsey, Lewis and Jones study precisely this wrapped-t family and record its modified-Bessel trigonometric moments. Gaunt gives a direct derivation of the Student-t characteristic function in the same modified-Bessel form.

The PC-383 profile appears as the exact classical special case `alpha=1`. Then `nu=1/2` and

\[
K_{1/2}(y)=\sqrt{\frac\pi{2y}}e^{-y},
\tag{27}
\]

so

\[
b_n(1,\tau)=e^{-n\tau}.
\tag{28}
\]

Therefore

\[
W_{1,\tau}(x)
=1+2\sum_{n\ge1}e^{-n\tau}\cos(nx)
=P_{e^{-\tau}}(e^{ix}),
\tag{29}
\]

exactly recovering the Poisson renormalization of PC-383 rather than producing a competing mechanism.

## 4. Matched nonprime controls falsify arithmetic selectivity

The classification is independent of any arithmetic property of `m`. Fix `alpha>0` and `tau>0`, and let `p_j` be any sequence of prime degrees tending to infinity while `n_j` is any sequence of composite degrees tending to infinity. With the same intrinsic mesh matching

\[
\varepsilon_m=2\sinh\frac\tau{2m},
\tag{30}
\]

both sequences have the same normalized positive-operator limit:

\[
T_{p_j,\alpha,\tau}^*T_{p_j,\alpha,\tau}
-
T_{n_j,\alpha,\tau}^*T_{n_j,\alpha,\tau}
\longrightarrow0
\tag{31}
\]

in the sense that each multiplier converges uniformly to the same function: `1` for `alpha<=1/2`, and `W_(alpha,tau)` for `alpha>1/2`.

Thus no order-one statistic of the singular values, minimum modulus, condition profile, or any continuous functional of `T^*T` can distinguish prime from matched composite refinement in this family. The phase transition at `alpha=1/2` is analytic -- the integrability threshold of the local real-line singularity -- rather than arithmetic.

This is stronger than merely observing another classical kernel. It closes the direct loophole left by PC-383: **varying the fixed positive inverse-power exponent does not turn the mesh-scale common-anchor modulus into a prime-sensitive carrier.** The only nontrivial supercritical limits are classical wrapped-t profiles.

## 5. Boundary of the negative result

This finding is deliberately limited to fixed `alpha>0`, positive scalar inverse-power chord weights, exact mesh matching `eta_m=tau/m`, and the positive operator `T^*T`. It does **not** classify the full nonnormal phase spectrum of `T`, exponent sequences `alpha_m`, sign/phase-changing weights, nonlinear or tensor observables, cross-level nonseparable couplings, or source-dependent operators.

It also does not classify genuinely submesh regularization. In the subcritical regime `alpha<1/2`, a much smaller cutoff can make a single anchor sample compete with the `1/m` fiber normalization; at `alpha=1/2` the corresponding threshold carries logarithmic corrections. Those are different scaling problems and should not be declared closed by (12)--(22).

For the canonical exact-mesh question, however, the boundary is now sharp: scalar inverse-power strengthening either washes out (`alpha<=1/2`) or converges to a universal wrapped-t multiplier (`alpha>1/2`). Any prime-circle mechanism surviving this branch must obtain arithmetic selectivity from structure beyond this normalized scalar fiber energy.

## Literature / novelty audit

- Arthur Pewsey, Toby Lewis, M. C. Jones, **“The Wrapped t Family of Circular Distributions,”** *Australian & New Zealand Journal of Statistics* 49(1), 79--91 (2007), DOI: https://doi.org/10.1111/j.1467-842X.2006.00465.x. This is the direct prior-art anchor for the periodized Student-t family and its modified-Bessel trigonometric moments.
- Robert E. Gaunt, **“A simple proof of the characteristic function of Student’s t-distribution,”** *Communications in Statistics -- Theory and Methods* 50(14), 3380--3383 (2021), DOI: https://doi.org/10.1080/03610926.2019.1702695. This anchors the classical modified-Bessel characteristic-function formula underlying (25).
- The remaining ingredients in the limit derivation -- root-fiber averaging, local mesh rescaling, Poisson summation, and the standard beta/gamma integral in (19) -- are classical analysis. The line-specific content is the classification of how this classical family arises from the prime-circle common-anchor refinement and the matched-prime/composite falsification.

## Consequence for the RH objective

No zeta zero, functional equation, critical-line symmetry, explicit-formula oscillation, or arithmetic spectral discriminator appears in this fixed inverse-power mesh-scale family. The nontrivial limit for `alpha>1/2` is already a classical circular probability kernel, while the weaker singularities converge to the identity. Accordingly, this branch does not supply a new bridge from the intrinsic prime-circle geometry to RH; it supplies a sharp no-go boundary for one of the last scalar singular repairs left by PC-382 and PC-383.