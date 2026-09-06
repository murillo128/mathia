# PF-191 — exact-area Lambert transport retains the suppressed strong-`L^1` endpoint

**Status:** `EXACT-DERIVED + ENDPOINT-SHARPENING + POSITIVE/BOUNDARY`. PF-179 constructs an exact area-preserving transport between the one-parameter Lambert bodies `Q(a)` and `Q(a+d)` and records only the coarse bound `\int \delta^r=O(d^r)`. That estimate discards where the deformation actually lives. The explicit triangular branch has differential defect

\[
O\!\left(\frac{d}{1+\sinh^2\tau}\right),
\]

while the hyperbolic cross-section where this defect is largest has area density `O(1/\cosh a)`. After refining PF-179's fixed corner Moser patch relative to the common outer translation, the corner contributes only `O(d e^{-2a})`. Consequently the **same exact-area construction can be chosen** with

\[
\int_{Q(a)}\delta^r\,d\mu
+\int_{Q(a+d)}\delta_{\rm inv}^r\,d\mu
\le C_r\frac{d^r}{\cosh a},
\qquad r\ge1.
\]

For the exact prime/shift half-cuffs these strong-`L^1` masses are summable. Thus exact area preservation does not destroy PF-130's hidden Lambert-body endpoint gain. Re-running PF-183's body bookkeeping with this sharper PF-179 estimate also extends the **unweighted assembled-body budget** to `r=1`; on PF-183's disjoint uniformly thick true-short-collar transition slabs, the corresponding inverse-unit-ball weighted body mass is therefore summable at the endpoint as well. This does not prove the missing endpoint conservative splice, a global weighted `L^1` comparison, weak trace class of the full relative resolvent, wave equivalence, or any RH consequence.

## Claim

Use PF-179's Fermi area coordinates

\[
g=\frac{dy^2}{1+y^2}+(1+y^2)d\tau^2,
\qquad d\mu=dy\,d\tau,
\tag{1}
\]

on the ideal Lambert quadrilateral

\[
D_a=\{(\tau,y):\tau\ge0,\ 0\le y\le Y_a(\tau)\}.
\tag{2}
\]

Write

\[
S=\sinh a,
\qquad A=\cosh a,
\qquad a'=a+d,
\qquad
\lambda=\frac{\sinh a'}{\sinh a},
\tag{3}
\]

with `a` in the PF-179 tail and `0<=d<=d_0`. Then PF-179's area-preserving transport may be chosen so that for every fixed `r>=1`,

\[
\boxed{
E_r(a,d):=
\int_{Q(a)}
\delta_{g_a,F^*g_{a'}}^r\,d\mu_a
+
\int_{Q(a')}
\delta_{g_{a'},(F^{-1})^*g_a}^r\,d\mu_{a'}
\le
C_r\frac{d^r}{\cosh a}.
}
\tag{4}
\]

Here `delta` is the same multiplicative metric-deviation scalar used in PF-174/PF-175/PF-179. The density part is exactly zero because `F` preserves area.

For the exact prime/shift half-cuffs

\[
a_n^+=a_n+d_n,
\qquad d_n=O(p_n^{-1}),
\tag{5}
\]

one therefore has

\[
\boxed{
\sum_n E_1(a_n,d_n)<\infty.
}
\tag{6}
\]

Let `F_body` denote the exact-area PF-179--PF-182 assembled body comparison used in PF-183, before insertion of the PF-138 true-short-collar gauges. Then the endpoint version of PF-183's unweighted body estimate holds:

\[
\boxed{
\int_X\delta_{\rm body}\,d\mu_X
+
\int_{X_+}\delta_{\rm body}^{+}\,d\mu_{X_+}
<\infty.
}
\tag{7}
\]

Consequently, on PF-183's disjoint uniformly thick transition slabs `T_\eta`, where the inverse-unit-ball weights satisfy `W_X,W_{X_+}<=C`,

\[
\boxed{
\sum_\eta\int_{T_\eta}W_X\delta_{\rm body}\,d\mu_X
+
\sum_\eta\int_{T_\eta^+}W_{X_+}\delta_{\rm body}^{+}\,d\mu_{X_+}
<\infty.
}
\tag{8}
\]

Equation (8) extends only PF-183's **energy accounting** to the endpoint. It does not establish an `r=1` version of PF-183's still-conditional local conservative splice lemma.

## 1. The finite triangular branch has a decaying differential defect

On PF-179's finite branch the exact area-preserving map is

\[
\tau'=\psi(\tau)=\operatorname{arsinh}(\lambda\sinh\tau),
\qquad
y'=\frac{y}{\psi'(\tau)}.
\tag{9}
\]

Put

\[
p=\psi'(\tau),
\qquad q=(\log p)' .
\tag{10}
\]

PF-179 gives the exact identities

\[
p^2
=
\frac{\lambda^2(1+\sinh^2\tau)}
{1+\lambda^2\sinh^2\tau},
\tag{11}
\]

and

\[
q
=
\frac{(1-\lambda^2)\tanh\tau}
{1+\lambda^2\sinh^2\tau}.
\tag{12}
\]

Hence, with

\[
e:=p^2-1,
\]

one has exactly

\[
\boxed{
e
=
\frac{\lambda^2-1}
{1+\lambda^2\sinh^2\tau},
\qquad |q|\le e.}
\tag{13}
\]

The pointwise `O(d)` estimate in PF-179 kept only the supremum of (13). The denominator is the endpoint gain.

Pulling back (1) under (9) gives the exact metric

\[
\boxed{
F^*g
=
\frac{(dy-yq\,d\tau)^2}{p^2+y^2}
+(p^2+y^2)d\tau^2.
}
\tag{14}
\]

Let `M=1+y^2` and use the source orthonormal coframe

\[
\alpha=\frac{dy}{\sqrt M},
\qquad
\beta=\sqrt M\,d\tau.
\tag{15}
\]

Relative to `(alpha,beta)`, equation (14) has matrix

\[
\begin{pmatrix}
\dfrac{M}{M+e}
&-\dfrac{yq}{M+e}\\[3mm]
-\dfrac{yq}{M+e}
&\dfrac{M+e}{M}
+\dfrac{y^2q^2}{M(M+e)}
\end{pmatrix}.
\tag{16}
\]

The Lambert width is uniformly bounded on the PF-179 tail, so `M` remains in one fixed compact interval. Since `e=O(d)` and `|q|<=e`, the relative metric eigenvalues lie in

\[
1+O(e).
\tag{17}
\]

The Güneysu--Thalmaier deviation is a smooth monotone function of the absolute logarithms of those eigenvalues on a fixed quasi-isometry range. Therefore

\[
\boxed{
\delta_{g,F^*g}(\tau,y)
\le
C\frac{\lambda^2-1}
{1+\lambda^2\sinh^2\tau}.}
\tag{18}
\]

No density term has to be added: the Jacobian in the area coordinates is exactly one.

## 2. Exact cross-section integration produces `1/cosh(a)`

On the finite branch PF-179 gives

\[
Y_a(\tau)
=
\frac{\cosh\tau}
{\sqrt{S^2-\sinh^2\tau}}.
\tag{19}
\]

For bounded `d`,

\[
0\le\lambda^2-1\le C d.
\tag{20}
\]

Using (18), integrating first in `y`, and extending the positive integral from the actual finite-branch cutoff to `0<=\sinh\tau<=S`, one obtains for every `r>=1`

\[
\begin{aligned}
I_r^{\rm fin}
&\le
C_r d^r
\int
\frac{Y_a(\tau)}{(1+\sinh^2\tau)^r}\,d\tau\\
&\le
C_r d^r
\int_0^S
\frac{dz}
{\sqrt{S^2-z^2}(1+z^2)^r}.
\end{aligned}
\tag{21}
\]

Since `r>=1`, the last integral is bounded by its `r=1` value. With `z=S\sin\theta`,

\[
\begin{aligned}
\int_0^S
\frac{dz}
{\sqrt{S^2-z^2}(1+z^2)}
&=
\int_0^{\pi/2}
\frac{d\theta}{1+S^2\sin^2\theta}\\
&=
\frac{\pi}{2\sqrt{1+S^2}}
=
\frac{\pi}{2\cosh a}.
\end{aligned}
\tag{22}
\]

Thus

\[
\boxed{I_r^{\rm fin}\le C_r d^r/\cosh a.}
\tag{23}
\]

This is the exact-area analogue of PF-130's hidden effective-area gain. The two maps are different: PF-130 used the earlier non-area-preserving Lambert comparison, whereas (23) comes directly from PF-179's exact-area triangular transport.

## 3. The corner correction can be measured relative to an isometry

PF-179's outer branch is the exact isometry

\[
J_\epsilon(\tau,y)=(\tau+\epsilon,y),
\qquad
\epsilon=\log\frac{\cosh a'}{\cosh a}.
\tag{24}
\]

The original PF-179 proof estimated the fixed corner patch relative to the identity and therefore retained only an `O(d)` differential bound. At the endpoint this is unnecessarily coarse: the relevant reference map on that patch is `J_epsilon`, not the identity.

PF-179 already proves

\[
|\beta-\epsilon|\le C d e^{-2a},
\qquad
\beta=\log\lambda,
\tag{25}
\]

and, on every fixed recentered corner interval `|\tau-T_a|<=r_0`,

\[
\psi(\tau)-\tau-\beta=O(d e^{-2a}).
\tag{26}
\]

Equation (13) gives on the same interval

\[
|p-1|+|q|=O(d e^{-2a}),
\tag{27}
\]

because `T_a=a+O(1)`. Hence the complete finite-branch germ (9), including its differential and its upper-boundary trace, differs from the outer isometry `J_epsilon` by

\[
\boxed{O(d e^{-2a})}
\tag{28}
\]

in a fixed recentered `C^1` chart. PF-179's corner-mass identity likewise gives

\[
|M_c(a')-M_c(a)|=O(d e^{-2a}).
\tag{29}
\]

After composing the target corner patch with `J_epsilon^{-1}`, the source and target patches, their prescribed boundary germs, and their corner locations are therefore `O(d e^{-2a})`-close in one fixed bounded-geometry model. The same fixed-domain extension and relative Moser argument already used in PF-179 can consequently be run at that **actual** scale. The preliminary extension has differential

\[
I+O(d e^{-2a}),
\]

its Jacobian is `1+O(d e^{-2a})`, and the compactly supported mean-zero primitive/divergence solution has the same scale. The correcting Moser flow is therefore `I+O(d e^{-2a})` in `C^1`.

Composing back with the exact isometry `J_epsilon` gives an exact-area corner map with metric deviation

\[
\delta_{\rm corner}=O(d e^{-2a})
\tag{30}
\]

on a patch of uniformly bounded area. Thus

\[
\boxed{
I_r^{\rm corner}
\le C_r d^r e^{-2ar}
\le C_r\frac{d^r}{\cosh a}.}
\tag{31}
\]

The outer branch contributes zero because it is isometric. Combining (23) and (31) proves the source half of (4).

Because `F` is exactly area preserving, change of variables preserves the integral, and the relative logarithmic metric eigenvalues for the inverse are the negatives of those for the forward map. The same deviation bound therefore holds on the target side, proving (4) after changing the constant.

## 4. The exact prime/shift family crosses the strong-`L^1` endpoint

For the exact shift clone, PF-107 gives

\[
d_n=O(p_n^{-1}),
\qquad
\sum_n d_n^2<\infty.
\tag{32}
\]

PF-114 gives the exact collar conversion

\[
\frac1{\sinh a_n}=\sinh\frac{h_n}{2},
\qquad
\sum_n h_n^2<\infty.
\tag{33}
\]

Since `cosh a_n>=sinh a_n` and `h_n->0`,

\[
\frac1{\cosh a_n}
\le
\frac1{\sinh a_n}
\le C h_n
\tag{34}
\]

on the tail. Cauchy--Schwarz therefore gives

\[
\sum_n\frac{d_n}{\cosh a_n}
\le
C
\left(\sum_n d_n^2\right)^{1/2}
\left(\sum_n h_n^2\right)^{1/2}
<\infty.
\tag{35}
\]

Equations (4) and (35) prove (6), including the reflected Lambert pieces at only fixed multiplicity.

This strengthens PF-179 without contradicting it. PF-179's `O(d^r)` bound is correct but uses only the uniform bilipschitz estimate; PF-191 retains the spatial decay already present in PF-179's explicit derivative.

## 5. PF-183's body accounting now reaches `r=1`

PF-183 proves its assembled-body estimate by adding four modules. Its only non-endpoint input was PF-179's coarse Lambert-body estimate `O(d_n^r)`, whose sum was used only for `r>1`. The other modules already cross the endpoint: PF-180's split synchronization has summable strong-`L^1` cost, while PF-181's cusp handoff and PF-182's decomposition-cuff smoothing have finite two-sided weighted `L^1` cost and therefore finite unweighted `L^1` cost.

Replacing PF-179's coarse input by (6) lets the same assembly argument be run at `r=1`, proving (7). No new composition or counting theorem is needed.

PF-183 then uses only two facts on the true-short-collar transition slabs `T_eta`: the slabs are pairwise disjoint and their inverse-unit-ball weights are uniformly bounded above. Applying that exact argument to the now-integrable endpoint body defect gives (8).

Therefore the multiplicity reduction itself is not an `r>1` phenomenon. What remains exponent-sensitive is the **local conservative splice theorem**. An endpoint extension would require a uniform estimate of the schematic form

\[
E_1(\operatorname{splice}_\eta;T_\eta)
\le
C\left(E_1^{\rm body}(T_\eta)+|t_\eta|\right)
\tag{36}
\]

on the normalized marked annulus, together with the corresponding inverse/target estimate. PF-183--PF-188 do not establish (36).

## 6. Prior art and novelty audit

No novelty is claimed for hyperbolic Lambert quadrilaterals, triangular mass transport, Moser's volume-form method, elementary elliptic integrals, or the use of an isometry as the reference map for a local perturbation. Vuorinen--Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings*, Ann. Acad. Sci. Fenn. Math. 38 (2013), 433--453, DOI `10.5186/aasfm.2013.3845`, studies sharp hyperbolic-distance and quasiconformal behavior of Lambert quadrilaterals but does not supply this exact-area integrated defect estimate.

The fixed-domain relative Moser ingredient and its bounded-geometry use were already audited in PF-179; PF-191 changes only the quantitative scale fed into that construction. A fresh structure-based search for area-preserving hyperbolic Lambert transports and integrated distortion found the same general Lambert/quasiconformal literature but no theorem giving (4) or the prime/shift summation (6). Search absence is not treated as a novelty theorem.

The durable project-specific delta is the exact integration of PF-179's already-persisted transport: exact area preservation and PF-130-style strong-`L^1` localization are compatible on the Lambert bodies. The consequent extension of PF-183's **unweighted body/slab accounting** to `r=1` is likewise a consequence of persisted Mathia modules, not a claimed new theorem about arbitrary hyperbolic surfaces.

## 7. Audit and falsification boundary

A later adversary can check PF-191 through the following finite chain:

1. import PF-179's area coordinates, triangular map (9), outer isometry, corner identities, and fixed-domain Moser setup;
2. verify (11)--(13) and then compute the pullback metric (14) directly;
3. express (14) in the source orthonormal coframe and verify matrix (16), including the off-diagonal `q` term;
4. use `|q|<=e`, bounded Lambert width, and the fixed quasi-isometry range to justify the pointwise deviation bound (18);
5. integrate the exact finite-branch width, substitute `z=sinh tau`, and verify the standard identity (22);
6. on the corner, factor out PF-179's exact outer translation and check that the remaining boundary/domain data are `O(d e^{-2a})` rather than merely `O(d)`; rerun the same fixed-domain extension/Moser estimate at that scale;
7. use exact area preservation to transfer the forward bound to the inverse/target side;
8. insert PF-107 and PF-114 and verify the Cauchy--Schwarz summation (35);
9. re-run only PF-183's existing body-module bookkeeping and disjoint-thick-slab estimate to obtain (7)--(8);
10. do **not** infer a global weighted `L^1` metric comparison away from the thick slabs, an endpoint conservative splice, `S_{1,infinity}` for the uncut resolvent, trace class, wave completeness, determinant control, or arithmetic separation.

A refutation would need to break the exact pullback calculation, the `1/cosh(a)` integral, the refined corner scale after factoring the outer isometry, the established prime/mesh square-summability, or PF-183's persisted module bookkeeping. Failure of the still-open local endpoint splice or weak-Schatten reassembly would not refute PF-191; those are the next gates isolated by the result.