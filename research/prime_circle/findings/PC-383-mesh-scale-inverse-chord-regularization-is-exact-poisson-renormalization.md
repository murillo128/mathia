# PC-383 — mesh-scale inverse-chord regularization is exact Poisson renormalization

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the canonical shrinking inverse-chord scalar escape left open by PC-237 and PC-382.

PC-382 proves that every fixed nonzero continuous scalar branch profile becomes asymptotically QMF under high-degree root refinement, but deliberately leaves open conductor-dependent profiles whose variation reaches the inverse-image mesh scale, especially shrinking regularizations of the singular common-anchor chord. For the most canonical such family, the regularized inverse chord,

\[
q_\varepsilon(z)=\bigl(|1-z|^2+\varepsilon^2\bigr)^{-1/2},
\qquad z\in\mathbb T,
\tag{1}
\]

the entire normalized modulus can be classified exactly. After intrinsic `L^2` normalization, its squared weight is a disk Poisson kernel. Root-fiber averaging sends that Poisson kernel to another Poisson kernel by the exact semigroup law

\[
\boxed{E_m P_\rho=P_{\rho^m}.}
\tag{2}
\]

Consequently all singular-value data of the normalized weighted refinement depends on the refinement degree `m` and regularization `epsilon` only through the single dimensionless parameter

\[
\boxed{\tau=2m\,\operatorname{arsinh}(\varepsilon/2).}
\tag{3}
\]

At the exact mesh-scale matching

\[
\varepsilon_{m,\tau}=2\sinh\frac{\tau}{2m},
\tag{4}
\]

the positive operator `T^*T` is **identical for every integer refinement degree**, prime or composite. The surviving order-one defect at `epsilon asymp 1/m` is therefore the classical Poisson profile itself, not a prime-sensitive spectral carrier. The stronger factorization below shows that the normalized operator is an exact QMF isometric embedding followed by one fixed base-side outer Poisson multiplier.

This does not classify every singular scalar weight or the full nonnormal spectrum of the weighted composition operator. It sharply closes the literal regularized inverse-chord modulus branch and identifies the exact boundary any successor must evade.

## 1. The normalized regularized inverse chord is exactly a Poisson kernel

Let normalized Haar measure on the unit circle be `dm`, and define

\[
(V_m f)(z)=f(z^m),\qquad m\ge2.
\tag{5}
\]

For `epsilon>0`, set

\[
S_{m,\varepsilon}=M_{q_\varepsilon}V_m,
\qquad
c_\varepsilon=\int_{\mathbb T}|q_\varepsilon|^2\,dm,
\qquad
T_{m,\varepsilon}=c_\varepsilon^{-1/2}S_{m,\varepsilon}.
\tag{6}
\]

Introduce

\[
\eta=2\operatorname{arsinh}(\varepsilon/2),
\qquad
\rho=e^{-\eta}\in(0,1).
\tag{7}
\]

Because `cosh eta = 1+epsilon^2/2`, for `z=e^{i theta}`,

\[
\begin{aligned}
|1-z|^2+\varepsilon^2
&=2(\cosh\eta-\cos\theta)\\
&=\rho^{-1}|1-\rho z|^2.
\end{aligned}
\tag{8}
\]

Hence

\[
|q_\varepsilon(z)|^2
=\frac{\rho}{|1-\rho z|^2}.
\tag{9}
\]

Using the standard circle integral for the Poisson kernel,

\[
c_\varepsilon
=\frac{\rho}{1-\rho^2}
=\frac1{2\sinh\eta},
\tag{10}
\]

and therefore

\[
\boxed{
\frac{|q_\varepsilon(z)|^2}{c_\varepsilon}
=\frac{1-\rho^2}{|1-\rho z|^2}
=:P_\rho(z).
}
\tag{11}
\]

Thus the geometry-forced regularized inverse chord does not merely resemble harmonic measure: after the canonical normalization already used in PC-380--PC-382, its squared amplitude **is exactly** the Poisson kernel with pole parameter `rho`.

## 2. Root refinement acts by the exact Poisson semigroup law

For the `m`-fold power map, the adjoint of `V_m` is the inverse-image average

\[
(E_mg)(z)
=(V_m^*M_gV_m)(z)
=\frac1m\sum_{w^m=z}g(w).
\tag{12}
\]

The circle Poisson kernel has the absolutely convergent Fourier expansion

\[
P_\rho(w)=\sum_{k\in\mathbb Z}\rho^{|k|}w^k.
\tag{13}
\]

Averaging over the `m` roots of `z` kills every Fourier frequency not divisible by `m`; for `k=m\ell` the average is `z^ell`. Therefore

\[
\begin{aligned}
E_mP_\rho(z)
&=\sum_{\ell\in\mathbb Z}\rho^{m|\ell|}z^\ell\\
&=P_{\rho^m}(z).
\end{aligned}
\tag{14}
\]

Combining (11)--(14) gives the exact positive operator

\[
\boxed{
T_{m,\varepsilon}^*T_{m,\varepsilon}
=M_{P_{\rho^m}}.
}
\tag{15}
\]

Since `rho^m=e^{-m eta}`, define

\[
\tau=m\eta
=2m\operatorname{arsinh}(\varepsilon/2).
\tag{16}
\]

Then

\[
\boxed{
T_{m,\varepsilon}^*T_{m,\varepsilon}
=M_{P_{e^{-\tau}}}.
}
\tag{17}
\]

No primality assumption appears. For the normalized modulus, the pair `(m,epsilon)` has collapsed exactly to one real scale parameter `tau`.

The extrema of the Poisson kernel occur at `z=-1` and `z=1`:

\[
\min_{\mathbb T}P_{e^{-\tau}}
=\tanh\frac\tau2,
\qquad
\max_{\mathbb T}P_{e^{-\tau}}
=\coth\frac\tau2.
\tag{18}
\]

Thus the minimum modulus, operator norm and condition number are

\[
\boxed{
\alpha(T_{m,\varepsilon})^2=\tanh\frac\tau2,
\qquad
\|T_{m,\varepsilon}\|^2=\coth\frac\tau2,
\qquad
\kappa(T_{m,\varepsilon})=\coth\frac\tau2.
}
\tag{19}
\]

The last equality uses `kappa=||T||/alpha(T)`. These quantities are exactly degree-blind once `tau` is fixed.

## 3. The shrinking-regularization phase diagram is one-dimensional

Equation (17) gives a sharp classification of the open shrinking-profile boundary in PC-382.

### Pre-mesh singularity: `tau_m -> infinity`

For small `epsilon`, `eta=epsilon+O(epsilon^3)`, so `tau_m -> infinity` includes every regime `m epsilon_m -> infinity`. Then

\[
e^{-\tau_m}\to0,
\qquad
\|P_{e^{-\tau_m}}-1\|_\infty\to0,
\tag{20}
\]

and hence

\[
T_{m,\varepsilon_m}^*T_{m,\varepsilon_m}\to I
\quad\text{in operator norm}.
\tag{21}
\]

This extends the PC-382 collapse beyond fixed continuous profiles: the weight may itself become singular at the anchor, provided its regularization scale remains asymptotically wider than the inverse-image mesh.

### Exact mesh scale: `tau_m -> a in (0,infinity)`

When `epsilon_m asymp 1/m`, an order-one defect survives. But (17) identifies it completely:

\[
T_{m,\varepsilon_m}^*T_{m,\varepsilon_m}
\longrightarrow M_{P_{e^{-a}}}
\tag{22}
\]

whenever `tau_m -> a`. More strongly, choosing the exact matching (4) gives

\[
\boxed{
T_{m,\varepsilon_{m,\tau}}^*T_{m,\varepsilon_{m,\tau}}
=M_{P_{e^{-\tau}}}
\quad\text{for every }m\ge2.
}
\tag{23}
\]

Thus a prime degree `p` and any composite control degree `m` with the same `tau` have identical positive operator, singular-value function, norm, minimum modulus and condition number. The first scale at which the regularized singularity defeats PC-382's asymptotic QMF collapse is therefore **exactly universal**, not arithmetically selective.

### Sub-mesh singularity: `tau_m -> 0`

When `m epsilon_m ->0`, the normalized profile concentrates at the anchor:

\[
P_{e^{-\tau_m}}\,dm\rightharpoonup\delta_1.
\tag{24}
\]

At the same time

\[
\min P_{e^{-\tau_m}}\sim\frac{\tau_m}{2},
\qquad
\max P_{e^{-\tau_m}}\sim\frac{2}{\tau_m},
\qquad
\kappa(T_{m,\varepsilon_m})\sim\frac{2}{\tau_m}.
\tag{25}
\]

The scalar channel becomes singularly ill-conditioned rather than approaching a new stable bounded operator. This is the same qualitative endpoint warning already visible in PC-237 for singular functional calculus, now obtained directly at finite refinement degree for the geometry-forced regularization.

## 4. Exact outer/QMF factorization isolates all surviving modulus data on the base

The collapse in (17) is stronger than a calculation of `T^*T`. Let

\[
a_\rho(z)=\frac{\sqrt{1-\rho^2}}{1-\rho z},
\qquad |a_\rho(z)|^2=P_\rho(z),
\tag{26}
\]

and define the finite filter

\[
h_{m,\rho}(z)
=
\sqrt{\frac{1-\rho^2}{1-\rho^{2m}}}
\sum_{j=0}^{m-1}\rho^jz^j.
\tag{27}
\]

The geometric-series identity gives exactly

\[
\boxed{
a_\rho(z)
=h_{m,\rho}(z)\,a_{\rho^m}(z^m).}
\tag{28}
\]

Moreover, `|h_{m,rho}|^2` has Fourier bandwidth at most `m-1`; root-fiber averaging kills every nonconstant mode, while

\[
\|h_{m,\rho}\|_2^2
=\frac{1-\rho^2}{1-\rho^{2m}}
\sum_{j=0}^{m-1}\rho^{2j}
=1.
\tag{29}
\]

Hence

\[
E_m|h_{m,\rho}|^2=1,
\tag{30}
\]

so `M_{h_{m,rho}}V_m` is an exact QMF isometry in the same sense as PC-380--PC-381.

The normalized geometric weight in `T` is `sqrt(P_rho)=|a_rho|`. Put

\[
u_\rho(z)=\frac{|a_\rho(z)|}{a_\rho(z)},
\qquad |u_\rho(z)|=1,
\tag{31}
\]

and

\[
W_{m,\rho}:=M_{u_\rho h_{m,\rho}}V_m.
\tag{32}
\]

Equations (28)--(31) imply

\[
\boxed{
T_{m,\varepsilon}
=W_{m,\rho}\,M_{a_{\rho^m}},
\qquad
W_{m,\rho}^*W_{m,\rho}=I.
}
\tag{33}
\]

At exact mesh matching `rho=e^{-tau/m}`,

\[
\boxed{
T_{m,\tau}
=W_{m,\tau}\,M_{a_{e^{-\tau}}}.
}
\tag{34}
\]

All non-isometric modulus data is therefore carried by one fixed base-side outer multiplier `a_{e^{-tau}}`; dependence on the refinement degree is pushed into an exact QMF isometric embedding. This is a stricter structural statement than merely saying that the singular values happen to match.

It also makes the matched composite control intrinsic: the same factorization holds for every integer covering degree. Nothing in the regularized inverse-chord scalar modulus marks rational primes.

## 5. Spectral consequences and the boundary not proved here

For every finite `tau>0`, (18) makes `T` bounded below. The same right-inverse/infinite-defect argument used in PC-382 therefore yields

\[
\boxed{
\sqrt{\tanh(\tau/2)}\,\overline{\mathbb D}
\subseteq
\sigma(T_{m,\varepsilon}^*)
\subseteq
\sqrt{\coth(\tau/2)}\,\overline{\mathbb D}.
}
\tag{35}
\]

Every point strictly inside the smaller disk is an adjoint eigenvalue of infinite multiplicity. At matched `tau`, both spectral bounds are independent of `m`.

Equation (35) is deliberately **not** promoted to a full spectral-equivalence statement. The isometric factor `W_{m,rho}` in (33) still depends on `m`, and the nonnormal spectrum in the annulus between the two displayed disks is not classified here. Equality of `T^*T`, singular-value data, and the base modulus factor does not by itself imply unitary equivalence of the full weighted composition operators.

The result also does not classify:

- inverse powers `(|1-z|^2+epsilon^2)^{-alpha/2}` with `alpha != 1`, for which the normalized squared weight is no longer a Poisson kernel;
- asymmetric or phase-sensitive singular regularizations not determined by the common-anchor chord magnitude;
- source- or shell-dependent weights coupled before the root-fiber average;
- nonlinear, matrix-valued, tensor, or genuinely cross-level operators;
- a separate mechanism that extracts arithmetic information from nonnormal phase data left inside the QMF embedding.

Those are real exclusions. PC-383 closes the canonical literal inverse-chord **scalar modulus** branch, not every possible mesh-scale singular construction.

## 6. Prior-art and novelty audit

Every abstract analytic ingredient above is classical.

Sheldon Axler, Paul Bourdon and Wade Ramey, **Harmonic Function Theory**, 2nd ed., Graduate Texts in Mathematics 137, Springer (2001), gives the standard disk Poisson kernel, its Fourier expansion and harmonic-measure interpretation. The identity (14) is then the elementary roots-of-unity Fourier selector applied to that classical kernel.

Ola Bratteli, David E. Evans and Palle E. T. Jorgensen, **Compactly supported wavelets and representations of the Cuntz relations**, *Applied and Computational Harmonic Analysis* 8:2 (2000), 166--196, DOI `10.1006/acha.2000.0283`, develops the quadrature-mirror-filter/Cuntz-isometry framework in which constant inverse-fiber energy gives an isometric weighted composition operator. That is the operator-theoretic class containing (30)--(34).

Xianghong Chen and Hans Volkmer, **On transfer operators on the circle with trigonometric weights**, *Journal of Fractal Geometry* 5:4 (2018), 351--386, DOI `10.4171/JFG/64`, studies circle transfer operators of the same power-map/preimage-average form, including sine and cosine power weights. It is direct neighboring prior art for treating root-fiber weighted dynamics as classical transfer-operator theory rather than a new spectral species.

No historical novelty is claimed for Poisson kernels, the semigroup relation, QMF filters, outer factors, or weighted composition operators. The durable Prime-Circle contribution is the exact identification forced by the line's own singular common-anchor geometry: **the canonical shrinking inverse-chord regularization lands exactly inside this classical Poisson/QMF package**, with a one-parameter renormalization `tau` and an exact prime/composite matched control.

A directed search around Poisson kernels, circle transfer operators, QMF/Cuntz weighted composition, and root-of-unity fiber averaging found no basis for treating this specialization as an existing RH criterion. More importantly, the derivation itself produces no zeta factor, gamma factor, functional-equation symmetry, zero divisor, or distinguished real part `1/2`.

## 7. Consequence for the Prime-Circle frontier

The most direct singular continuation of the PC-380--PC-382 weighted-refinement branch now has an exact boundary:

\[
\text{regularized inverse anchor chord}
\longrightarrow
\text{mesh-scale shrinking}
\longrightarrow
\text{normalized weighted refinement}
\longrightarrow
\text{Poisson/QMF renormalization}.
\tag{36}
\]

Above the mesh scale the normalized operator returns to the universal isometric regime. At the mesh scale an order-one defect survives, but it is exactly the prime-blind Poisson kernel and can be factored onto the base through a universal outer multiplier. Below the mesh scale the scalar channel becomes singularly concentrated and ill-conditioned.

Therefore **shrinking the canonical inverse-chord regularization to `epsilon asymp 1/m` does not rescue a prime-sensitive scalar modulus or singular-value spectrum**. A successor in this branch must show mathematically what survives beyond this Poisson renormalization: a different singular exponent with genuinely new normalized structure, phase/nonnormal data that is not reducible to the QMF embedding, conductor/source dependence before scalarization, or nonlinear/cross-level geometry. Merely making the anchor singular at the inverse-image mesh scale is no longer sufficient.

The finding should be revised if the normalization in (10)--(11) is inconsistent with the canonical weighted-refinement normalization, if the root-fiber identity (14) fails under the stated power-map convention, or if a matched prime/composite pair at equal `tau` has different `T^*T`. Any of those would directly falsify the exact classification.