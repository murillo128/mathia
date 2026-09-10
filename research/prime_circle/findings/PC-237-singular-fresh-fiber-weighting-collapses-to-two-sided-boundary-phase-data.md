# PC-237 — singular fresh-fiber weighting collapses to two-sided boundary phase data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the singular / inverse-chord fixed-base fresh-fiber escape left explicitly open by PC-236. At fixed coarse conductor `N`, PC-227 produces normalized shifted Cauchy packets on `ell^2(Z)`, while PC-235 identifies the intrinsic fresh coordinate `z^N` with the bilateral shift `S`. The present result classifies the most natural singular scalar functional calculus of that same coordinate.

For every normalized packet

\[
g_\sigma(j)=\frac{\sin(\pi\sigma)}{\pi}\frac1{j+\sigma},
\qquad 0<\sigma<1,
\]

the spectral measure of `S` is **exactly normalized Haar measure on the circle**, independent of `sigma`. Consequently a possibly unbounded Borel multiplier `V(S)` is defined on `g_sigma` exactly when `V in L^2(T)`. In particular,

\[
|1-S|^{-\alpha}g_\sigma\in\ell^2(\mathbb Z)
\quad\Longleftrightarrow\quad
\alpha<\frac12.
\]

Thus the intrinsic inverse chord (`alpha=1`) and inverse-square chord (`alpha=2`) do not act on the limiting source packet without regularization. For the natural symmetric regularization, every supercritical or critical power `alpha>=1/2` concentrates at the two one-sided approaches to the anchor and the normalized packet Gram kernel converges to

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\langle h_{\sigma,\varepsilon},h_{\tau,\varepsilon}\rangle
=
\cos\!\bigl(\pi(\tau-\sigma)\bigr).
}
\]

This kernel has rank at most two. Hence singular scalar weighting of one fixed-base fresh coordinate does not open an expanding spectral carrier: below threshold it is ordinary measurable functional calculus of the bilateral shift, while at and above threshold its canonical geometric regularization reduces, per packet sector, to two elementary boundary phases. Fixed finite direct sums of packet sectors therefore remain finite-dimensional at the endpoint. No zeta zero divisor, completed functional equation, or distinguished real part `1/2` is produced.

## 1. The PC-227 packet is an exact fractional discrete-Hilbert translate

The partial-fraction identity

\[
\sum_{j\in\mathbb Z}\frac1{(j+\sigma)^2}
=\pi^2\csc^2(\pi\sigma)
\tag{1}
\]

shows immediately that `||g_sigma||_2=1`.

De Carli and Shaikh Samad study the one-parameter family

\[
(T_t a)_m
=
\frac{\sin(\pi t)}{\pi}
\sum_{n\in\mathbb Z}\frac{a_n}{m-n+t},
\qquad t\notin\mathbb Z,
\tag{2}
\]

with the integer values continued as signed translations. They prove that `{T_t}_{t in R}` is a strongly continuous one-parameter group of isometries on `ell^2(Z)` whose infinitesimal generator is the discrete Hilbert transform up to the factor `pi`. Taking `a=delta_0` gives the exact identification

\[
\boxed{g_\sigma=T_\sigma\delta_0.}
\tag{3}
\]

With the PC-235 convention

\[
(Sf)(j)=f(j+1),
\tag{4}
\]

the integer continuation of (2) gives

\[
T_1=-S.
\tag{5}
\]

Because the `T_t` form an abelian group, `T_sigma` commutes with `S`. Since `T_sigma` is surjective and norm preserving, it is unitary. Therefore for every `k in Z`,

\[
\begin{aligned}
\langle g_\sigma,S^kg_\sigma\rangle
&=\langle T_\sigma\delta_0,S^kT_\sigma\delta_0\rangle\\
&=\langle\delta_0,S^k\delta_0\rangle\\
&=\delta_{k0}.
\end{aligned}
\tag{6}
\]

The Fourier coefficients in (6) determine the spectral measure uniquely, so

\[
\boxed{d\mu_{g_\sigma}(z)=dm(z),}
\tag{7}
\]

where `m` is normalized Haar probability on `T`. This is exact for every `0<sigma<1`; it is not an asymptotic statement and contains no primality hypothesis.

## 2. Exact domain test for arbitrary singular scalar multipliers

Let `V:T->C` be Borel measurable and let `V(S)` be the possibly unbounded operator given by the spectral theorem for the bilateral shift. Equation (7) gives

\[
\boxed{
g_\sigma\in\operatorname{Dom}(V(S))
\iff
\int_{\mathbb T}|V(z)|^2\,dm(z)<\infty,
}
\tag{8}
\]

and, whenever this holds,

\[
\boxed{
\|V(S)g_\sigma\|_2^2
=
\int_{\mathbb T}|V(z)|^2\,dm(z).
}
\tag{9}
\]

Both the domain and the norm are independent of the cyclotomic packet shift `sigma`. Thus allowing an unbounded functional calculus does not by itself expose a new packet-dependent spectral invariant.

For the geometry-forced inverse-chord powers

\[
V_\alpha(z)=|1-z|^{-\alpha},
\tag{10}
\]

local integrability at `z=1` gives the sharp threshold

\[
\boxed{
g_\sigma\in\operatorname{Dom}(|1-S|^{-\alpha})
\iff
\alpha<\frac12.
}
\tag{11}
\]

For `0<=alpha<1/2`, the norm can be evaluated exactly:

\[
\begin{aligned}
\| |1-S|^{-\alpha}g_\sigma\|_2^2
&=\frac1{2\pi}\int_0^{2\pi}
(2|\sin(\theta/2)|)^{-2\alpha}\,d\theta\\
&=\boxed{\frac{\Gamma(1-2\alpha)}{\Gamma(1-\alpha)^2}}.
\end{aligned}
\tag{12}
\]

At `alpha=1/2` the divergence is logarithmic; for `alpha>1/2` it is a power divergence. In particular the literal inverse chord and inverse-square chord are outside the Hilbert-space domain on the PC-227 packet limit.

This already closes one naive continuation of PC-236: replacing a continuous chord observable by its reciprocal does not produce a new self-adjoint spectral object on the source state. One must specify a regularization or a different domain.

## 3. The canonical symmetric regularization has only two boundary phases

The domain failure in (11) leaves a natural question: can the diverging singularity itself, after normalization, retain nontrivial cyclotomic information? Use the geometry-preserving symmetric regularization

\[
V_{\alpha,\varepsilon}(e^{i\theta})
=
\bigl(4\sin^2(\theta/2)+\varepsilon^2\bigr)^{-\alpha/2},
\qquad \varepsilon>0.
\tag{13}
\]

For each `epsilon`, this is bounded and PC-236 applies. The exact Fourier representation of (3), with the convention in which `S` is multiplication by `e^{-i theta}`, is

\[
\boxed{
\widehat g_\sigma(\theta)
=e^{i\sigma(\pi-\theta)},
\qquad 0<\theta<2\pi.
}
\tag{14}
\]

Its modulus is one, another direct expression of the Haar spectral measure.

For `alpha>=1/2`, put

\[
h_{\sigma,\varepsilon}
=
\frac{V_{\alpha,\varepsilon}(S)g_\sigma}
{\|V_{\alpha,\varepsilon}(S)g_\sigma\|_2}.
\tag{15}
\]

Then

\[
\langle h_{\sigma,\varepsilon},h_{\tau,\varepsilon}\rangle
=
\frac{\int_0^{2\pi}
W_{\alpha,\varepsilon}(\theta)
 e^{i(\tau-\sigma)(\pi-\theta)}\,d\theta}
{\int_0^{2\pi}W_{\alpha,\varepsilon}(\theta)\,d\theta},
\tag{16}
\]

where

\[
W_{\alpha,\varepsilon}(\theta)
=\bigl(4\sin^2(\theta/2)+\varepsilon^2\bigr)^{-\alpha}.
\tag{17}
\]

As `epsilon->0`, the normalized weight in (16) concentrates at `z=1`. In the interval representation this point has two one-sided approaches, `theta->0+` and `theta->2pi-`. Symmetry of (17) gives asymptotically equal mass to the two sides. The phase in (16) tends respectively to

\[
e^{i\pi(\tau-\sigma)}
\quad\hbox{and}\quad
e^{-i\pi(\tau-\sigma)}.
\tag{18}
\]

Therefore

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\langle h_{\sigma,\varepsilon},h_{\tau,\varepsilon}\rangle
=\frac12e^{i\pi(\tau-\sigma)}
 +\frac12e^{-i\pi(\tau-\sigma)}
=\cos\bigl(\pi(\tau-\sigma)\bigr).
}
\tag{19}
\]

The critical case `alpha=1/2` is included: although concentration is only logarithmic, every fixed arc away from the anchor carries a vanishing fraction of the total divergent mass.

The limiting kernel factors as

\[
\cos\bigl(\pi(\tau-\sigma)\bigr)
=
\cos(\pi\sigma)\cos(\pi\tau)
+
\sin(\pi\sigma)\sin(\pi\tau),
\tag{20}
\]

so every finite Gram matrix built from these normalized singular packets has rank at most two. Equivalently, the entire endpoint packet label reduces to the universal real two-vector

\[
\boxed{v_\sigma=(\cos\pi\sigma,\sin\pi\sigma).}
\tag{21}
\]

There is generally **no strong `ell^2` limit** for the individual vectors `h_{sigma,epsilon}`. Their spectral probability density converges weakly to point mass at `z=1`, while any vector in this cyclic bilateral-shift representation has spectral measure absolutely continuous with respect to Haar measure. Equation (19) is therefore a singular boundary Gram limit, not a newly produced eigenvector in the original Hilbert space.

## 4. What happens to the full fixed-base packet sector

PC-227 does not contain only one packet in isolation. A fixed exact-order source column is a finite orthogonal direct sum of packet components

\[
C_r g_{\sigma_r},
\tag{22}
\]

with cyclotomic amplitudes `C_r` and shifts `sigma_r`, the number of sectors depending only on the fixed coarse conductor `N`.

Equation (7) applies to every component. Consequently the domain threshold (11) is unchanged for the full column whenever at least one component is nonzero. Under the normalized singular regularization, each orthogonal packet copy contributes at most the two boundary phases (21). Thus a fixed finite direct sum remains bounded by a finite-dimensional endpoint carrier depending on `N`; its dimension does not grow with the fresh prime `q`.

The amplitudes `C_r` can affect the finite direct-sum weighting, but they do not alter the universal threshold or create new fresh-fiber spectral support. The result therefore does not erase the cyclotomic source data already present in PC-227; it shows that **singular scalar weighting of the one fresh coordinate does not amplify that data into a new growing operator species**.

## 5. Stress tests and falsification controls

The key collapse is prime-blind. Equations (3), (6), (8), and (19) hold for every real `sigma in (0,1)`, including completely non-arithmetic shifts. The source packet's cyclotomic origin is therefore not responsible for either the Haar measure, the `alpha=1/2` threshold, or the two boundary phases.

The threshold is also not an artifact of one finite Fourier truncation. It is the exact spectral-theorem domain criterion for the limiting bilateral shift. Regularizations below threshold converge in the ordinary `ell^2` functional calculus; at and above threshold the chosen natural symmetric chord regularization leaves only the endpoint phases (18).

The rank-two statement is deliberately **not** upgraded to a claim that the normalized vectors become collinear. The two one-sided limits at the same circle point carry different fractional-shift phases. They agree only in special packet differences. This is why the correct universal endpoint carrier is two-dimensional rather than rank one.

The result does not classify arbitrary singular finite-`q` constructions. A profile whose shape depends on `q` at the mesh scale can couple to the exact cyclic lattice before the PC-227 limit and need not be approximated by the fixed limiting multiplier used here. Nor does the argument cover simultaneous `N,q->infinity`, operators coupling coarse and fresh coordinates before packet separation, old/new mode mixing that is not a scalar function of `z^N`, several genuinely noncommuting refinement coordinates, or global uniformization/accessory data.

These exclusions are material. PC-237 closes the fixed-base **single-fresh-coordinate scalar singular functional-calculus branch**, especially the direct inverse-chord powers suggested by the open boundary of PC-236. It is not a no-go theorem for every non-equicontinuous or singular Prime-Circle mechanism.

## 6. Prior art and novelty audit

The abstract Cauchy-packet operator structure is classical. Laura De Carli and Gohin Shaikh Samad, **One-parameter Groups of Operators and Discrete Hilbert Transforms**, *Canadian Mathematical Bulletin* 59:3 (2016), 497–507, DOI `10.4153/CMB-2016-028-7`, arXiv `1506.03362`, define exactly the group (2), including signed shifts at integer parameter, and prove its `ell^2` isometry/group properties. Thus the identification (3) places the normalized PC-227 packet directly inside established discrete-Hilbert-transform theory rather than creating a new family of vectors.

The remaining ingredients are standard spectral/Fourier analysis: spectral measures of the bilateral shift, measurable functional calculus, the beta/gamma evaluation of the circle integral in (12), and boundary concentration of the singular weight. Fisher--Hartwig literature provides a much broader classical context for power singularities on the unit circle, but no Toeplitz determinant theorem is needed for the present argument.

No historical novelty is claimed for the one-parameter Hilbert group, Haar spectral measure technology, the `L^2` integrability threshold, or the elementary cosine kernel. The project-specific durable content is the exact bridge from the source-forced PC-227 packet to that classical group and the resulting sharp obstruction: **the most direct singular/inverse-chord escape from PC-236 either remains ordinary bilateral-shift functional calculus or degenerates, after canonical normalization, to two one-sided boundary phases.**

A directed search around discrete Hilbert transforms, shifted Cauchy kernels, singular circle multipliers, and unitary shift functional calculus found no evidence that this project-specific identification yields a known RH criterion. More importantly, the calculation itself supplies no zeta factor or zero condition. It should therefore be recorded as a classicalization/boundary result, not as a candidate RH mechanism.

## 7. Consequence for the live Prime-Circle frontier

The route

\[
\boxed{
\text{PC-227 fixed-base Cauchy packet}
\longrightarrow
|1-z^N|^{-\alpha}
\longrightarrow
\text{singular scalar fresh-fiber spectrum}
\longrightarrow
\text{new RH-facing carrier}
}
\]

is now sharply restricted. For `alpha<1/2` the multiplier is an ordinary `L^2` spectral function with packet-independent norm. For `alpha>=1/2` it is not defined on the source packet without regularization, and the natural symmetric geometric regularization has only the two elementary boundary phases in (19).

The surviving frontier must therefore exploit a feature that occurs **before** this one-coordinate scalarization: genuine `q`-scale finite-mesh interaction, simultaneous coarse/fresh growth, a coupled coarse/fresh or old/new operator, multiple noncommuting refinement coordinates, or the global uniformization/accessory sector. Merely making the same fresh-fiber scalar observable singular is not enough.