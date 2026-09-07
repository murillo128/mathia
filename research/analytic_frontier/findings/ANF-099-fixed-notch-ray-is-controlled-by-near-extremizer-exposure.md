# ANF-099 — fixed notch ray is controlled by near-extremizer exposure

**Status:** `EXACT-DERIVED + ENVELOPE-REDUCTION + SOURCE-TENSOR-COMPRESSION + FIXED-RAY-CRITERION`. `ANF-086` gives one certified central-notch ray and reduces failure of its fixed amplitude to configurations outside a uniform separable tube. `ANF-097`--`ANF-098` then show that proving such a tube by selecting one separable carrier is genuinely nonconvex. For the narrower question of whether **some positive amplitude on one frozen notch ray** beats Montgomery--Taylor, that full reconstruction is unnecessary. The decision is exactly controlled by one scalar observable of Montgomery--Taylor near-extremizers: the normalized energy exposed by the notch. Moreover `ANF-088` transfers this observable, with an error vanishing as the Montgomery--Taylor excess tends to zero, to its canonical source-generated `2/1/0` equality-signature tensor.

Fix one notch width `eta` and its entire shape before varying amplitude. Write

\[
J_0=J_{\rm MT},\qquad
\phi_\eta(\alpha)=b_\eta(1-|\alpha|/\eta)_+,
\qquad 0\le \phi_\eta\le J_0,
\tag{1}
\]

and, for every nonempty finite conjugation-invariant multiset `W`, put

\[
L(W)=2|W|-\sigma(W),\qquad
S_W(\alpha)=\sum_{z\in W}e^{-2\pi i\alpha z},
\tag{2}
\]

where `sigma` counts simple real sites. Define

\[
r(W)=\frac{\int J_0|S_W|^2}{L(W)},\qquad
e(W)=r(W)-1,\qquad
h_\eta(W)=\frac{\int\phi_\eta|S_W|^2}{L(W)}.
\tag{3}
\]

Lamzouri's Montgomery--Taylor inequality gives `r(W)>=1`, while (1) gives `0<=h_eta(W)<=r(W)`. Set

\[
A_\eta(\varepsilon)
:=\sup_{e(W)\le\varepsilon}h_\eta(W),
\qquad
\beta_\eta
:=\lim_{\varepsilon\downarrow0}A_\eta(\varepsilon).
\tag{4}
\]

The supremum ranges over all finite cardinalities, multiplicities and geometries. Real singleton equality configurations make every set nonempty; `A_eta(epsilon)<=1+epsilon`, and monotonicity in `epsilon` makes the limit well defined with `0<=beta_eta<=1`.

Let `C_0=C_{\rm MT}` and

\[
B_\eta
:=\frac{C(\phi_\eta)}{C_0}
=\frac{b_\eta(1+\eta^2/3)}{C_0}.
\tag{5}
\]

For the frozen ray

\[
J_t=J_0-t\phi_\eta,
\qquad
q_\eta(t):=\inf_W\{r(W)-t h_\eta(W)\},
\qquad
\rho_\eta(t):=\frac{C(J_t)}{C_0}=1-tB_\eta,
\tag{6}
\]

one has the exact criterion

\[
\boxed{
q_\eta'(0+)=-\beta_\eta,
\qquad
\exists\,0<t<\min(1,1/B_\eta):\ q_\eta(t)>\rho_\eta(t)
\iff
\beta_\eta<B_\eta.
}
\tag{7}
\]

Thus `beta_eta` is the complete first-order and existence obstruction for this **one fixed notch direction**. Exact equality configurations alone do not determine it: all nearly active configurations, including sequences of growing cardinality and unbounded geometry, enter the envelope.

## 1. The lower envelope gives the criterion without compactness

Fix `epsilon>0` and split the infimum in (6) into configurations with `e<=epsilon` and `e>epsilon`. On the first class,

\[
r-th\ge1-tA_\eta(\varepsilon).
\tag{8}
\]

On the second, `h<=r` gives, for `0<t<1`,

\[
r-th\ge(1-t)r>(1-t)(1+\varepsilon).
\tag{9}
\]

Consequently

\[
\boxed{
q_\eta(t)\ge
\min\{1-tA_\eta(\varepsilon),(1-t)(1+\varepsilon)\}.
}
\tag{10}
\]

For the opposite direction choose `epsilon_n downarrow0` and configurations `W_n` with

\[
e(W_n)\le\varepsilon_n,
\qquad
h_\eta(W_n)\ge A_\eta(\varepsilon_n)-o(1).
\tag{11}
\]

Then `r(W_n)->1` and `h_eta(W_n)->beta_eta`, so for every fixed `t>0`,

\[
\boxed{q_\eta(t)\le1-t\beta_\eta.}
\tag{12}
\]

No minimizing configuration, compactness, or bounded-cardinality subsequence is used. If `t<=epsilon/(1+epsilon)`, the second branch of (10) is at least one, hence

\[
1-tA_\eta(\varepsilon)\le q_\eta(t)\le1-t\beta_\eta.
\tag{13}
\]

Divide by `t` after subtracting one, send `t downarrow0`, and then `epsilon downarrow0`. This proves the derivative in (7).

The same two inequalities give the global existence equivalence. If `beta_eta>=B_eta`, then (12) implies

\[
q_\eta(t)\le1-t\beta_\eta\le1-tB_\eta=\rho_\eta(t)
\tag{14}
\]

for every positive admissible amplitude, including the equality case `beta_eta=B_eta`. Conversely, if `beta_eta<B_eta`, choose `a` with `beta_eta<a<B_eta` and then `epsilon>0` so that `A_eta(epsilon)<=a`. Any sufficiently small positive `t`, for instance

\[
0<t\le
\min\left\{
\frac{\varepsilon}{2(1+\varepsilon)},
\frac1{2(1+B_\eta)}
\right\},
\tag{15}
\]

makes the second branch in (10) exceed one and gives

\[
q_\eta(t)\ge1-ta>1-tB_\eta=\rho_\eta(t)>0.
\tag{16}
\]

This is precisely the strict affine normalization improvement along the frozen ray.

## 2. The projection-tax tensor carries exactly the needed observable

Use the Montgomery--Taylor factorization from `ANF-087`. With `g` there, `eta_MT=sqrt(g)` and `J_0=g*g`, define on `[-1/2,1/2]^2`

\[
\mathcal F_W(u,v)
=\eta_{\rm MT}(u)\eta_{\rm MT}(v)S_W(u+v).
\tag{17}
\]

Let `mathcal T_W` be the **adapted** equality-signature tensor of `ANF-088`, not an arbitrary tensor with the same ranks. That finding gives

\[
\|\mathcal F_W-\mathcal T_W\|_2^2
\le e(W)L(W).
\tag{18}
\]

It also gives `D_U=r_0+k`, `D_V-D_U=n`, where `r_0` is the number of distinct repeated real sites, `k` the number of distinct nonreal conjugate pairs and `n` the number of simple real sites. Hence

\[
\|\mathcal T_W\|_2^2
=4D_U+(D_V-D_U)
=4(r_0+k)+n
\le L(W),
\tag{19}
\]

because repeated real multiplicities are at least two and nonreal-pair multiplicities are at least one.

Define the multiplication operator `M_eta` by

\[
m_\eta(u,v)
:=\sqrt{\frac{\phi_\eta(u+v)}{J_0(u+v)}},
\tag{20}
\]

setting it to zero on the null set where numerator and denominator both vanish. Since `0<=phi_eta<=J_0`, `M_eta` is a contraction. Changing variables by `alpha=u+v` and using `g*g=J_0` gives the exact observable identity

\[
\boxed{
h_\eta(W)=
\frac{\|M_\eta\mathcal F_W\|_2^2}{L(W)}.}
\tag{21}
\]

Put

\[
\Theta_\eta(W)
:=\frac{\|M_\eta\mathcal T_W\|_2^2}{L(W)}.
\tag{22}
\]

From (18), contraction, and (19),

\[
\boxed{
|\sqrt{h_\eta(W)}-\sqrt{\Theta_\eta(W)}|
\le\sqrt{e(W)},
}
\tag{23}
\]

and, after expanding the squared norm around `mathcal T_W`,

\[
\boxed{
|h_\eta(W)-\Theta_\eta(W)|
\le2\sqrt{e(W)}+e(W).
}
\tag{24}
\]

The error is uniform over cardinality, multiplicity and height. Therefore

\[
\boxed{
\beta_\eta
=
\lim_{\varepsilon\downarrow0}
\sup_{e(W)\le\varepsilon}\Theta_\eta(W).
}
\tag{25}
\]

This replaces a nonlinear configuration-reconstruction problem by a scalar concentration question on the **physical source-generated** tensors already singled out by the exact projection-tax identity.

A finite positive target is now explicit. If for one `epsilon>0`

\[
\sup_{e(W)\le\varepsilon}\Theta_\eta(W)
+2\sqrt\varepsilon+\varepsilon
<B_\eta,
\tag{26}
\]

then `beta_eta<B_eta`, so (7) produces a smaller improving amplitude on the same frozen ray. Conversely, an actual physical sequence with

\[
e(W_n)\to0,
\qquad
\liminf_{n\to\infty}\Theta_\eta(W_n)\ge B_\eta
\tag{27}
\]

forces `beta_eta>=B_eta` and kills every positive admissible amplitude on that ray.

## 3. Observable control is strictly weaker than separable reconstruction

The reduction also quantifies how much of the stronger `ANF-086` program is unnecessary for the fixed-ray existence question. Freeze one already certified amplitude `s_0` and separable floor `q_0` from `ANF-086`, so

\[
q_0>1-s_0B_\eta.
\tag{28}
\]

Suppose only the qualitative all-sequence statement were known:

\[
e(W_n)\to0
\quad\Longrightarrow\quad
d_{\rm sep}^{(s_0)}(W_n)\to0.
\tag{29}
\]

Applying the `ANF-086` perturbative floor to approximate maximizers in (4) would give

\[
1-s_0\beta_\eta
=\lim_n\{r(W_n)-s_0h_\eta(W_n)\}
\ge q_0,
\tag{30}
\]

hence

\[
\boxed{
\beta_\eta\le\frac{1-q_0}{s_0}<B_\eta.
}
\tag{31}
\]

Thus no quantitative rate in a separable-stability theorem is needed merely to prove that **some** smaller notch amplitude improves the Montgomery--Taylor normalization. More importantly, (26) may be weaker still because it asks only for one contracted tensor observable, not a nearby physical product carrier.

This does not make the nonconvex selection problem of `ANF-097`--`ANF-098` irrelevant to stronger goals. It remains load-bearing if one wants geometric classification or the original fixed-amplitude tube. The present result only removes that stronger burden from the existence decision along one preselected scalar ray.

## 4. Two controls prevent false compactness and rank arguments

Exact equality cases do not determine `beta_eta`. As an abstract scalar control, take admissible pairs

\[
(r,h)=(1,1/4),
\qquad
(r,h)=(1+1/n^2,3/4),\quad n\ge1.
\tag{32}
\]

They satisfy the only scalar constraints `r>=1` and `0<=h<=r`. The exact minimizer has notch exposure `1/4`, but `beta=3/4` and the lower envelope is `q(t)=1-3t/4`. With objective slope `B=1/2`, exact-equality inspection would predict the wrong sign. This is not a physical counterexample; it shows why the finite equality classification in `ANF-087` cannot replace the all-cardinality near-extremizer envelope.

Nor can one discard the fact that `mathcal T_W` is generated by an actual exponential configuration. Let

\[
\psi_j(u)=e^{2\pi iju},\qquad1\le j\le m,
\tag{33}
\]

be orthonormal on `[-1/2,1/2]`, and form the abstract equality-signature tensor

\[
T_m(u,v)=2\sum_{j=1}^m\psi_j(u)\psi_j(v),
\qquad L_m=4m.
\tag{34}
\]

Then

\[
\frac{\|M_\eta T_m\|_2^2}{4m}
=
\frac1m\int_{-1}^{1}(1-|\alpha|)
\frac{\phi_\eta(\alpha)}{J_0(\alpha)}
\left|\sum_{j=1}^me^{2\pi ij\alpha}\right|^2d\alpha.
\tag{35}
\]

For fixed `eta<1`, the Fejer approximate identity gives

\[
\frac{\|M_\eta T_m\|_2^2}{4m}
\longrightarrow\frac{b_\eta}{J_0(0)}.
\tag{36}
\]

For sufficiently small fixed `eta`, this exceeds `B_eta`, because

\[
\frac{b_\eta/J_0(0)}{B_\eta}
=
\frac{C_0}{J_0(0)(1+\eta^2/3)}>1
\tag{37}
\]

and `C_0=J_0(0)+\int|\alpha|J_0(\alpha)d\alpha>J_0(0)`. Thus the abstract `2/1/0` signature and its norm budget alone cannot prove (26). The relation between the adapted subspaces and the physical exponential source must be retained.

## 5. Prior-art boundary and evidence limit

The value-function part of (7) belongs to classical envelope/sensitivity analysis. Milgrom and Segal, *Envelope Theorems for Arbitrary Choice Sets*, Econometrica 70(2) (2002), 583--601, DOI `10.1111/1468-0262.00296`, is the closest general prior-art boundary found for derivatives of optimized values over unrestricted choice sets. No theorem from that paper is load-bearing here: (10)--(16) are a complete elementary proof specialized to this affine family, including nonattainment and nearly active configurations. The contraction estimate and Fejer approximate-identity control are likewise classical. The line-specific mathematical content is the exact splice of this envelope to the Montgomery--Taylor affine normalization and to the canonical `ANF-088` source tensor.

No literature result found supplies the physical inequality `beta_eta<B_eta`, and this finding does **not** claim it. It also does not give a physical counterexample with `beta_eta>=B_eta`, certify the original amplitude from `ANF-086`, improve an unconditional zero proportion by itself, or prove RH. Moving `eta` with `t`, optimizing the notch after inspecting configurations, or restricting to a fixed cardinality changes the problem. Because all load-bearing inputs are already canonical in this line and the new argument is derived directly, `SOURCES.md` is unchanged.

## Research consequence

For one frozen central-notch direction, the live gate is no longer the full nonconvex problem of selecting a good separable carrier. It is the scalar physical concentration inequality

\[
\boxed{\beta_\eta<B_\eta,}
\tag{38}
\]

or its negation by an actual near-extremizing sequence. Equation (25) identifies the exact source-side quantity to attack: the central-notch exposure of the canonical `ANF-088` tensors. A proof of the uniform finite-`epsilon` bound (26) closes the entire ray positively; a physical sequence satisfying (27) closes it negatively. Arbitrary equality-signature tensors and exact equality cases are insufficient controls, so the next argument must use the fact that the adapted tensor is generated by a genuine positive conjugation-invariant exponential multiset.