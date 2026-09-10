---
type: negative
research_line: xi_flow
finding_id: XF-160
status: canonical
---

# XF-160 — positive Fourier sources retain maximal-contact blindness with asymptotically prescribed transition gaps

**Confidence:** high for the finite periodic source class proved below. The construction is exact at every finite degree, the transition locations converge to the prescribed values, and its observation difference is exactly the same maximal-contact packet as XF-141/XF-159 up to sign. This does **not** show that the Riemann Xi kernel itself realizes the control: it only proves that nonnegativity of the Fourier-side source, by itself, cannot exclude the maximal-contact blind direction.

## Statement

XF-159 leaves one principal escape from the maximal-contact obstruction: an Xi-specific source theorem could rule out the adversarial packet before target-side conditioning becomes relevant. The most immediate such source property is positivity. In the de Bruijn--Newman representation

\[
H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\]

the Riemann kernel is positive for `u>=0`; indeed each summand can be written

\[
\pi n^2 e^{5u}
\bigl(2\pi n^2e^{4u}-3\bigr)e^{-\pi n^2e^{4u}}>0.
\tag{1}
\]

Thus, after even extension, every Xi heat slice is the Fourier transform of a nonnegative even source measure. The maximal-contact family of XF-141 was not presented in that source form because its centered low-frequency coefficients have the opposite sign from its edge carrier.

That sign defect can be removed **without changing the matched-pair observation difference**. Let

\[
N=2M,\qquad r=M-1,
\tag{2}
\]

and define the folded-binomial weights

\[
p_0:=\frac{\binom{2r}{r}}{4^r},\qquad
p_j:=\frac{2\binom{2r}{r-j}}{4^r}\quad(1\le j\le r).
\tag{3}
\]

They satisfy

\[
p_j=\frac{|c_j|}{H_r},\qquad
\sum_{j=0}^r p_j=1,
\tag{4}
\]

for the XF-141 barycentric packet. Put

\[
\begin{aligned}
B_r(w,s)
:=&\ 2p_0e^{-aM^2s}w^M\\
&+\sum_{j=1}^r p_j e^{-a(M^2-j^2)s}
\bigl(w^{M-j}+w^{M+j}\bigr),
\end{aligned}
\tag{5}
\]

so that the canonical XF-141 maximal-contact family is exactly

\[
E^-_\lambda(w,s)=1+w^{2M}-\lambda B_r(w,s).
\tag{6}
\]

Define instead the **positive-spectrum companion family**

\[
\boxed{
E^+_\lambda(w,s)=1+w^{2M}+\lambda B_r(w,s),
\qquad 0<\lambda\le1.
}
\tag{7}
\]

For every fixed `rho>=0`, retain the same XF-141 amplitude

\[
\lambda_{r,\rho}
:=\mathcal A_r(-\rho)^{-1},
\qquad
\mathcal A_r(s)
:=\sum_{j=0}^r p_j e^{-a(M^2-j^2)s}.
\tag{8}
\]

Then the following three statements hold.

First, after the harmless centered scalar normalization

\[
\mathcal H^+_\lambda(\theta,s)
:=e^{aM^2s}e^{-iM\theta}E^+_\lambda(e^{i\theta},s),
\tag{9}
\]

`mathcal H^+_lambda` solves the backward heat equation

\[
\partial_s\mathcal H^+_\lambda
=-a\,\partial_\theta^2\mathcal H^+_\lambda
\tag{10}
\]

and is the Fourier transform of an even **nonnegative finite measure** at every time. Explicitly,

\[
\begin{aligned}
\mathcal H^+_\lambda(\theta,s)
=&\ 2e^{aM^2s}\cos(M\theta)+2\lambda p_0\\
&+2\lambda\sum_{j=1}^r p_j e^{aj^2s}\cos(j\theta),
\end{aligned}
\tag{11}
\]

so every Fourier mass is nonnegative. Hence this family lies in the natural finite periodic analogue of the nonnegative-source class containing the Xi deformation.

Second, if `Lambda_per^+(lambda)` denotes the periodic all-real-root threshold of `(7)`, then for every fixed `rho>=0`,

\[
\boxed{
\Lambda_{\rm per}^+(1)\longrightarrow0,
\qquad
\Lambda_{\rm per}^+(\lambda_{r,\rho})\longrightarrow-\rho.
}
\tag{12}
\]

For `rho>0` the transition gap therefore satisfies

\[
\boxed{
\Lambda_{\rm per}^+(1)
-
\Lambda_{\rm per}^+(\lambda_{r,\rho})
\longrightarrow\rho.
}
\tag{13}
\]

Third, the entire pairwise spacetime difference is unchanged up to sign:

\[
\boxed{
E^+_1-E^+_{\lambda_{r,\rho}}
=-\bigl(E^-_1-E^-_{\lambda_{r,\rho}}\bigr).
}
\tag{14}
\]

Consequently **every pointwise, multipoint, full-future and full-field blindness estimate of XF-146--XF-159 that depends only on the matched-pair difference transfers verbatim to this positive-spectrum family**. In particular, on any moving observation domain `K_N` inside the XF-159 blind phase with margin

\[
\delta_N:=-\sup_{(S,D)\in K_N}\Gamma(S,D)>0,
\tag{15}
\]

the corresponding raw fields satisfy

\[
\boxed{
\|\mathcal F^+_{1,N}
-\mathcal F^+_{\lambda_{r,\rho},N}\|_\infty
\le
16(1-\lambda_{r,\rho})e^{-N\delta_N}.
}
\tag{16}
\]

For fixed `rho>0`, any Lipschitz decoder on this positive-source control class that recovers `Lambda_per` from such a field must therefore have, for all sufficiently large `N`,

\[
\boxed{
L_N\ge\frac{\rho}{32}e^{N\delta_N}.
}
\tag{17}
\]

Thus positivity of the Fourier-side heat source is not the missing Xi rigidity. Any successful source-side exclusion of the maximal-contact direction must use finer information about the **specific spectral profile** of `Phi`, or another Xi-specific identity not shared by arbitrary nonnegative source measures.

## 1. The folded barycentric packet is a positive heat kernel after changing only the common sign

From the exact absolute-weight identity in XF-141,

\[
\sum_{j=0}^r|\omega_j|=\frac{4^r}{(2r)!},
\]

one obtains `(3)` directly. The resulting trigonometric generating function is

\[
\boxed{
p_0+\sum_{j=1}^r p_j\cos(j\theta)
=\cos^{2r}\!\left(\frac\theta2\right).
}
\tag{18}
\]

Indeed, `(18)` is simply the centered binomial expansion of
`(e^{i\theta/2}+e^{-i\theta/2})^(2r)/4^r`.

Equation `(11)` follows by centering `(7)` and multiplying by `e^(aM^2s)`. Its Fourier coefficients are

\[
q_{\pm M}(s)=e^{aM^2s},\qquad
q_0(s)=2\lambda p_0,
\qquad
q_{\pm j}(s)=\lambda p_j e^{aj^2s}>0.
\tag{19}
\]

Therefore

\[
\mathcal H^+_\lambda(\theta,s)
=\sum_{j=-M}^M q_j(0)e^{aj^2s}e^{ij\theta},
\tag{20}
\]

which is exactly a finite nonnegative even spectral measure subjected to the Gaussian Fourier multiplier of backward heat. Positive-definiteness can be checked directly, without invoking Bochner: for arbitrary complex `zeta_l` and angles `theta_l`,

\[
\sum_{\ell,m}\zeta_\ell\overline{\zeta_m}
\mathcal H^+_\lambda(\theta_\ell-\theta_m,s)
=
\sum_j q_j(0)e^{aj^2s}
\left|\sum_\ell\zeta_\ell e^{ij\theta_\ell}\right|^2
\ge0.
\tag{21}
\]

The important point is not that positive-definite trigonometric polynomials are new; they are classical. It is that the **same folded-binomial packet responsible for maximal-contact blindness can sit inside this source-positive class once the common carrier sign is changed**.

## 2. The positive companion is already all-real at the prescribed comparison time

Write

\[
G^+_\lambda(\theta,s)
:=e^{-iM\theta}E^+_\lambda(e^{i\theta},s).
\tag{22}
\]

At the `2M` carrier extrema

\[
\theta_k=\frac{k\pi}{M},\qquad 0\le k<2M,
\tag{23}
\]

we have

\[
G^+_\lambda(\theta_k,s)
=2(-1)^k
+2\lambda\sum_{j=0}^r
p_j e^{-a(M^2-j^2)s}\cos(j\theta_k).
\tag{24}
\]

If

\[
\lambda\mathcal A_r(s)\le1,
\tag{25}
\]

then the signs in `(24)` alternate strictly. For even `k`, equality with zero would require every cosine in the lower bound to equal `-1`, impossible because the `j=0` term has cosine `1`. For odd `k`, equality would require every cosine in the upper bound to equal `1`, impossible because `p_1>0` and `cos(k\pi/M)<1` for odd `k` in the stated range.

Hence there is a distinct unit-circle zero in every interval between consecutive `theta_k`. Since `E^+_lambda` has degree `2M`, these are all its zeros and all are simple. Because `mathcal A_r(s)` is strictly decreasing in `s`, the definition `(8)` gives

\[
\lambda_{r,\rho}\mathcal A_r(s)\le1
\quad\text{for every }s\ge-\rho.
\tag{26}
\]

Therefore

\[
\boxed{
\Lambda_{\rm per}^+(\lambda_{r,\rho})\le-\rho,
}
\tag{27}
\]

including `rho=0`, where `lambda_(r,0)=1` and hence `Lambda_per^+(1)<=0`.

The strict sign argument at equality is useful: unlike a loose perturbative criterion, it proves that the positive companion still has all `2M` roots simple on the unit circle at the comparison slice itself. Its actual first collision occurs slightly earlier.

## 3. Fixed additional backward time destroys every unit-circle zero

It remains to show that the transition cannot occur a fixed amount earlier than `-rho`. For `tau>=0`, define

\[
K_r(\theta,\tau)
:=p_0+\sum_{j=1}^r p_j e^{-aj^2\tau}\cos(j\theta).
\tag{28}
\]

By `(18)`, `K_r(theta,0)=cos^(2r)(theta/2)>=0`, and `(28)` is its ordinary **forward** periodic heat evolution. Let `P_tau` be the normalized periodic heat kernel with Fourier multiplier `e^(-aj^2 tau)`. For every fixed `tau>0`, `P_tau` is continuous and strictly positive on the circle, so

\[
m_\tau:=\min_\theta P_\tau(\theta)>0.
\tag{29}
\]

Convolution with `(18)` gives

\[
\boxed{
K_r(\theta,\tau)\ge m_\tau p_0.
}
\tag{30}
\]

No degree-dependent lower bound on `m_tau` is needed. Since the central binomial coefficient is the largest among the `2r+1` coefficients summing to `4^r`,

\[
\boxed{
p_0=\frac{\binom{2r}{r}}{4^r}
\ge\frac1{2r+1}.
}
\tag{31}
\]

Now fix `epsilon>0` and put `s=-(rho+epsilon)`. From `(8)` and `(28)`,

\[
\lambda_{r,\rho}
=\frac{e^{-aM^2\rho}}{K_r(0,\rho)},
\qquad
0<K_r(0,\rho)\le1.
\tag{32}
\]

Therefore

\[
\begin{aligned}
G^+_{\lambda_{r,\rho}}
(\theta,-\rho-\epsilon)
=&\ 2\cos(M\theta)\\
&+2\frac{e^{aM^2\epsilon}}
{K_r(0,\rho)}
K_r(\theta,\rho+\epsilon).
\end{aligned}
\tag{33}
\]

Using `(30)`--`(32)`, uniformly in `theta`,

\[
G^+_{\lambda_{r,\rho}}
(\theta,-\rho-\epsilon)
\ge
-2
+2e^{aM^2\epsilon}
\frac{m_{\rho+\epsilon}}{2r+1}.
\tag{34}
\]

The second term tends to `+infinity` because `r=M-1`. Hence `(34)` is strictly positive for all `theta` at sufficiently large degree. At that slice the polynomial has **no unit-circle zero at all**, so in particular it is not in the all-real phase. Consequently

\[
-\rho-\epsilon
<
\Lambda_{\rm per}^+(\lambda_{r,\rho})
\le
-\rho
\tag{35}
\]

for every fixed `epsilon>0` and all sufficiently large `N`. This proves the second limit in `(12)`. Taking `rho=0` gives

\[
-\epsilon<\Lambda_{\rm per}^+(1)\le0,
\tag{36}
\]

which proves the first limit and hence `(13)`.

This argument deliberately does not claim an exact finite-`N` transition location. It gives the amount needed for the matched-control obstruction: a target separation converging to any prescribed fixed `rho`.

## 4. The complete blind field is identical in magnitude to the canonical maximal-contact pair

The sign change from `(6)` to `(7)` alters each individual zero trajectory, but it leaves the pairwise perturbation exactly unchanged in modulus:

\[
E^+_1-E^+_\lambda=(1-\lambda)B_r,
\qquad
E^-_1-E^-_\lambda=-(1-\lambda)B_r.
\tag{37}
\]

This identity holds as a polynomial identity for every complex `w` and every real heat time. Therefore, with the same complex observation coordinate used in XF-146--XF-159,

\[
R^+_\lambda(z,s)
:=E^+_\lambda\!\left(-e^{-2\pi iz/L},s\right),
\tag{38}
\]

we have

\[
\boxed{
|R^+_1(z,s)-R^+_\lambda(z,s)|
=
|R^-_1(z,s)-R^-_\lambda(z,s)|
}
\tag{39}
\]

pointwise on the whole complex spacetime plane.

Thus no new visibility calculation is required. The root-spacing real-tube bound of XF-146, the infinite-jet and shallow-collar bounds of XF-151, the exact outward/inward exponents of XF-156/XF-158, the multipoint budget of XF-157, and the continuum/Lipschitz theorem of XF-159 all apply to the positive companion pair with precisely the same input gap. Only the target value changes from an exact finite-degree gap `rho` to a gap converging to `rho`.

For a fixed `rho>0`, `(13)` makes that distinction irrelevant to stable inversion. Once `N` is large enough that the target gap is at least `rho/2`, XF-159 and `(39)` yield `(16)`--`(17)`.

There is a small geometric difference if one insists on recentering coordinates at the **actual** first collision of the positive companion rather than keeping the canonical packet coordinate: its first collision need not occur at the XF-141 carrier point. This does not affect `(39)` or any observation theorem stated in the fixed coordinate. A source-local theorem that recenters dynamically at the collision must account for that translation separately; translation merely adds the corresponding linear phase to the positive spectral measure and does not destroy its origin from a nonnegative source.

## 5. What source information is still missing

The result rules out a tempting but insufficient source-side repair. The Xi kernel has a positive Fourier-side density, but the canonical blindness mechanism is not an artifact of allowing signed source measures: **finite nonnegative source measures already support the same exponentially hidden packet together with an asymptotically fixed transition-time separation.**

It does not follow that the actual Xi source can realize this family. The controls use degree-dependent discrete measures with a specially engineered folded-binomial low-frequency cloud and an edge carrier. The actual source is the specific continuous density `Phi(u)du`, with its exact theta-series shape, superexponential tails, arithmetic normalization and any additional regularity those imply. Moreover, the two matched controls use different source measures; they do not match the complete known Xi source globally. A theorem allowed to inspect that full source can of course distinguish them.

This is exactly the remaining distinction that a useful source theorem must exploit. Positivity or positive-definiteness by itself is now too weak. The next decisive test is to identify a **quantitative spectral-shape constraint actually proved for the Xi kernel** and determine whether it survives the scaling/periodization needed by the destination while excluding the folded-binomial-plus-edge profile. Candidate properties must be checked rather than assumed: recent work on total positivity of the de Bruijn--Newman kernel shows that even natural strengthenings of positivity can fail at finite order.

## Prior-art and novelty audit

The broad source class is classical. C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. 61 (1976), 245--251, DOI `10.1090/S0002-9939-1976-0434982-5`, explicitly studies Gaussian deformations of Fourier transforms of even nonnegative finite measures. Bochner/Herglotz identifies nonnegative spectral measures with positive-definite functions; `(21)` proves the only direction needed here directly. None of that is claimed as new.

A directed modern audit also found Wojciech Michalowski, *On the Polya Frequency Order of the de Bruijn--Newman Kernel: Certified Failure at Order Five*, arXiv:2602.20313v2 (20 July 2026). It certifies that the classical kernel `Phi(|u|)` is not `PF_5`; the revised version explicitly withdraws stronger global claims while retaining the finite `PF_5` counterexample. This is not load-bearing for XF-160, but it is a useful warning that one cannot silently upgrade the known nonnegative source to an arbitrary total-positivity hypothesis.

The Mathia-specific contribution here is the exact sign-companion construction `(7)`, the transition squeeze `(35)`, and the identity `(39)` showing that the complete maximal-contact blind field survives inside a nonnegative Fourier-source class. No audited source supplied this combination or the resulting conditioning obstruction. Since no external theorem is required for the proof and the existing de Bruijn--Newman/Newman--Wu source anchors already cover the classical nonnegative-measure framework, `SOURCES.md` is unchanged.

## Falsification boundary

The strongest possible misreading would be to call `(7)` an Xi surrogate. It is not. It shares positivity of the Fourier source and exact backward-heat evolution, but not the actual Xi spectral density, prime structure, continuous support, global normalization, or high-height asymptotics. The conclusion is only that **source positivity alone cannot be the hypothesis that removes XF-159's matched control**.

The transition comparison is asymptotic in degree. At finite `N`, `Lambda_per^+(1)` need not equal `0`, and `Lambda_per^+(lambda_(r,rho))` need not equal `-rho`; `(35)`--`(36)` are the claimed bounds. Likewise, `(39)` transfers observation differences, not individual fields or zero locations.

The positivity statement concerns the centered heat solution after multiplication by the nonvanishing scalar `e^(aM^2s)`, which does not change zeros. Spatial recentering of a collision introduces a linear Fourier phase, as it does for a translated Xi slice; the underlying source measure remains nonnegative before translation.

No claim about `Lambda` for the actual Riemann Xi function follows.

## Consequence for `xi_flow`

XF-159 pushed the frontier to source realizability. XF-160 removes the weakest obvious source-side exclusion: the maximal-contact obstruction survives the same **nonnegative Fourier-source geometry** that underlies the de Bruijn--Newman deformation. Future work should therefore stop treating positivity or positive-definiteness as a plausible discriminator by itself.

The live source gate is narrower and more arithmetic/quantitative: use the actual shape of `Phi`, an explicit-formula consequence, a rigorously available spectral regularity condition, or another Xi-specific identity to rule out the folded-binomial-plus-edge direction after the exact destination normalization. Conversely, if that profile can be approximated while preserving one of those stronger source constraints, the conditioning obstruction becomes correspondingly harder to evade.