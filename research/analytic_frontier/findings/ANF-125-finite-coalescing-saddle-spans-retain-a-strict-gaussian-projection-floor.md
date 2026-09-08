# ANF-125 — finite coalescing saddle spans retain a strict Gaussian projection floor

**Status:** `EXACT-DERIVED + MULTI-PROFILE-OBSTRUCTION + COHERENT-STATE-LIMIT + STRICT-PROJECTION-GAP + FIXED-ARCHITECTURE`. `ANF-123` shows that a low-cost companion to an `ANF-115` interior-saddle packet must itself approach the same saddle on the `A^{-1/2}` scale. `ANF-124` then computes the joint Gaussian limit for one such coalescing family and proves that one wrong coalescing profile cannot be a perfect mirror. The remaining immediate escape was to use several coalescing families and translations at once. For every **fixed, nondegenerate finite** collection, that escape also fails.

After source normalization and the natural rescaling `u=sqrt(A)(alpha-a_0)`, every coalescing packet converges to a canonical Gaussian coherent state. Distinct limiting phase-space points give linearly independent coherent states. Consequently, if the target state is omitted from a fixed finite companion set, its distance from their span is strictly positive. In physical terms, for arbitrary nonnegative integer multiplicities,

\[
\liminf_{A\to\infty}
\frac{E_0\!\left(P_{0,A}\sqcup
\bigsqcup_{j=1}^m w_{j,A}P_{j,A}\right)}
     {E_0(P_{0,A})}
\ge d_*^2>0,
\]

where `d_*^2` is an explicit Schur complement of the limiting Gaussian Gram matrix. The `m=1` case reduces exactly to the `1-rho(kappa)^2` floor of `ANF-124`.

Thus a fixed number of genuinely distinct `A^{-1/2}`-coalescing profiles cannot produce the near-perfect saddle mirror required by the high-efficiency branch of `ANF-120`. Any surviving low-cost completion must become **degenerate** in phase space (a companion approaches the target or several companions coalesce at a finer scale), let the number of profiles grow, or leave the coalescing packet chamber altogether.

## 1. Positive-saddle profiles converge to Gaussian coherent states

Use the exact `ANF-115` packet family with

\[
t_{k,A}=\frac12+A^{-2}3^{-k},
\qquad
n_{0,A}=\lfloor\gamma_0A\rfloor,
\qquad
P_{0,A}:=P_{A,n_{0,A}}.
\]

Write

\[
a_0:=a_{\gamma_0},
\qquad
c_0:=-F_{\gamma_0}''(a_0)
=\frac{1+\pi^2\gamma_0^2}{2\gamma_0}.
\tag{1}
\]

Fix an integer `m>=1`. For `j=1,...,m`, take fixed real parameters `kappa_j,s_j` and sequences

\[
n_{j,A}
=
n_{0,A}+\lfloor\kappa_j\sqrt A\rfloor,
\qquad
\frac{\tau_{j,A}}{\sqrt A}\longrightarrow s_j,
\tag{2}
\]

and put

\[
P_{j,A}:=P_{A,n_{j,A}}+\tau_{j,A}.
\tag{3}
\]

A common real translation of all packets is irrelevant, so the target is taken with `kappa_0=s_0=0`.

Let

\[
E_{j,A}:=E_0(P_{j,A})
\]

and normalize the positive half of the Montgomery--Taylor source Hilbert space by

\[
u_{j,A}(\alpha)
:=
\sqrt{\frac{2}{E_{j,A}}}\,
\mathbf 1_{(0,1)}(\alpha)
J_0(\alpha)^{1/2}S_{P_{j,A}}(\alpha).
\tag{4}
\]

Because every packet is conjugation-invariant and `J_0` is even,

\[
\|u_{j,A}\|_2=1
\tag{5}
\]

exactly.

The phase hidden in the product formula of `ANF-115` is also exact. If

\[
X_{n,A}:=\sum_{k=1}^n t_{k,A},
\]

then on the positive saddle neighborhood

\[
S_{P_{A,n}}(\alpha)
=
2^{n+1}\cosh\!\left(\frac{A\alpha}{2}\right)
e^{-\pi i\alpha X_{n,A}}
\prod_{k=1}^n\cos(\pi\alpha t_{k,A}),
\tag{6}
\]

and a translation by `tau` adds the factor `e^{-2 pi i alpha tau}`. Moreover,

\[
\frac{X_{n_{j,A},A}-X_{n_{0,A},A}}{\sqrt A}
\longrightarrow\frac{\kappa_j}{2}.
\tag{7}
\]

The saddle itself moves by

\[
\sqrt A\,(a_{\gamma_0+\kappa_j/\sqrt A}-a_0)
\longrightarrow
\mu_j,
\qquad
\mu_j
:=
a_{\gamma_0}'\kappa_j
=
-\frac{\kappa_j}{c_0\gamma_0}.
\tag{8}
\]

After the unitary rescaling `u=sqrt(A)(alpha-a_0)`, removal of the common rapidly oscillating phase of the base packet, and one harmless constant phase for each `j`, the elementary Laplace expansion used in `ANF-124` strengthens to `L^2(R)` convergence

\[
u_{j,A}\longrightarrow \psi_{\mu_j,\nu_j},
\tag{9}
\]

where

\[
\nu_j
:=
\pi\left(\frac{\kappa_j}{2}+2s_j\right)
\tag{10}
\]

and

\[
\boxed{
\psi_{\mu,\nu}(u)
=
\left(\frac{c_0}{2\pi}\right)^{1/4}
\exp\!\left[-\frac{c_0}{4}(u-\mu)^2\right]
\exp\!\left[-i\nu\left(u-\frac{\mu}{2}\right)\right].
}
\tag{11}
\]

Indeed, the squared amplitudes converge to the Gaussian density with mean `mu_j` and variance `1/c_0`; strict concavity gives a uniform Gaussian majorant outside every fixed rescaled window, while (6)--(8) give the displayed linear phase on compact `u`-sets. Dominated convergence then gives (9).

The limiting inner product is therefore

\[
\boxed{
\Gamma(z,z')
=
\exp\!\left[
-\frac{c_0}{8}(\mu-\mu')^2
-\frac{(\nu-\nu')^2}{2c_0}
\right]
\exp\!\left[
\frac{i}{2}(\mu\nu'-\mu'\nu)
\right],
}
\tag{12}
\]

for `z=(mu,nu)` and `z'=(mu',nu')`. Its modulus reproduces exactly the two penalties of `ANF-124`:

\[
|\Gamma(z_r,z_s)|
=
\exp\!\left[
-\frac{f''(\gamma_0)}8(\kappa_r-\kappa_s)^2
-\frac{\pi^2}{2c_0}
\left(
\frac{\kappa_r-\kappa_s}{2}
+2(s_r-s_s)
\right)^2
\right].
\tag{13}
\]

Thus the pairwise computation of `ANF-124` is the two-point shadow of a full finite Gaussian Gram geometry.

## 2. Distinct limiting phase-space points have a strictly positive Gram determinant

Set

\[
z_j:=(\mu_j,\nu_j)\in\mathbb R^2,
\qquad
z_0=(0,0).
\tag{14}
\]

Assume that `z_1,...,z_m` are pairwise distinct and that no `z_j` equals `z_0`. Then the `m+1` states

\[
\psi_{z_0},\psi_{z_1},\ldots,\psi_{z_m}
\]

are linearly independent.

This needs no external coherent-state theorem. From (11),

\[
\psi_{\mu,\nu}(u)
=
C_{\mu,\nu}\,
e^{-c_0u^2/4}
e^{\lambda_{\mu,\nu}u},
\qquad
\lambda_{\mu,\nu}
=
\frac{c_0\mu}{2}-i\nu,
\tag{15}
\]

with `C_{mu,nu}!=0`. Distinct phase-space points give distinct complex numbers `lambda`. A linear relation among the states would therefore give a finite exponential polynomial

\[
\sum_{j=0}^m d_j e^{\lambda_j u}=0
\tag{16}
\]

for every real `u`. Differentiating (16) at zero for orders `0,...,m` yields a Vandermonde system with nonzero determinant, so every `d_j` vanishes.

Hence the coherent-state Gram matrix

\[
\mathcal G
:=
\bigl[\Gamma(z_r,z_s)\bigr]_{0\le r,s\le m}
\tag{17}
\]

is strictly positive definite. Let

\[
G
:=
\bigl[\Gamma(z_r,z_s)\bigr]_{1\le r,s\le m},
\qquad
g
:=
\bigl(\Gamma(z_1,z_0),\ldots,\Gamma(z_m,z_0)\bigr)^T.
\tag{18}
\]

The squared distance from the target state to the complex span of the companions is the Schur complement

\[
\boxed{
d_*^2
:=
1-g^*G^{-1}g
=
\frac{\det\mathcal G}{\det G}
>0.
}
\tag{19}
\]

This is the exact finite-profile obstruction.

There is also a useful uniform version. Fix `m`, a compact phase-space ball `|z|<=R`, and `delta>0`. On the compact set of configurations satisfying

\[
|z_j-z_0|\ge\delta,
\qquad
|z_j-z_k|\ge\delta
\quad(j\ne k),
\tag{20}
\]

the continuous quantity in (19) has a positive minimum,

\[
d_*^2\ge c(m,R,\delta)>0.
\tag{21}
\]

So the floor cannot disappear along a nondegenerate compact family of fixed finite architectures.

## 3. Arbitrary physical multiplicities cannot beat the projection floor

Let `w_{j,A}` be arbitrary nonnegative integers and form the physical multiset

\[
V_A
:=
P_{0,A}
\sqcup
\bigsqcup_{j=1}^m w_{j,A}P_{j,A}.
\tag{22}
\]

On the positive half source Hilbert space, (4) gives the exact identity

\[
\frac{E_0(V_A)}{E_{0,A}}
=
\left\|
u_{0,A}
+
\sum_{j=1}^m
b_{j,A}u_{j,A}
\right\|_2^2,
\qquad
b_{j,A}
:=
w_{j,A}\sqrt{\frac{E_{j,A}}{E_{0,A}}},
\tag{23}
\]

where `E_{0,A}=E_0(P_{0,A})`. The negative half contributes the conjugate norm and is already accounted for by the normalization in (4).

Now relax the physical coefficients `b_{j,A}>=0` to arbitrary complex scalars. Use the same harmless per-vector phase gauges as in Section 1; diagonal rephasing changes neither the companion span nor the projection distance. If `G_A` and `g_A` are the resulting finite-`A` companion Gram matrix and target-correlation vector, (9) gives

\[
G_A\longrightarrow G,
\qquad
g_A\longrightarrow g.
\tag{24}
\]

Since `G` is positive definite, `G_A` is uniformly invertible for large `A`, and the exact finite-dimensional projection formula yields

\[
\inf_{c\in\mathbb C^m}
\left\|
u_{0,A}+\sum_{j=1}^m c_j u_{j,A}\right\|_2^2
=
1-g_A^*G_A^{-1}g_A
\longrightarrow d_*^2.
\tag{25}
\]

Every physical choice in (23) lies inside this relaxed problem. Therefore

\[
\boxed{
\liminf_{A\to\infty}
\frac{E_0(V_A)}{E_0(P_{0,A})}
\ge d_*^2>0.
}
\tag{26}
\]

The multiplicities may depend on `A` arbitrarily; there is no bounded-coefficient hypothesis. Possible coefficient blowup cannot exploit the `o(1)` in the Gaussian approximation because the companion Gram matrix remains uniformly well-conditioned.

For `m=1`, (19) is

\[
d_*^2=1-|\Gamma(z_1,z_0)|^2.
\tag{27}
\]

Optimizing the translation slope with `s_1=-kappa_1/4` gives

\[
|\Gamma(z_1,z_0)|
=
\exp\!\left[
-\frac{\kappa_1^2}
{4\gamma_0(1+\pi^2\gamma_0^2)}
\right]
=
\rho(\kappa_1),
\tag{28}
\]

so (26) becomes exactly the `1-rho(kappa)^2` floor of `ANF-124`.

The obstruction is also genuinely local to the saddle. If `E_0(V_A)=O(E_{0,A})`, uniform invertibility of `G_A` bounds the normalized coefficient vector in (23). Hence for any `S_A->infinity` sufficiently slowly, Gaussian concentration in (9) gives

\[
\frac{E_{B_A(S_A)}(V_A)}{E_{0,A}}
\ge d_*^2-o(1),
\qquad
B_A(S_A)
=
\left\{
\alpha:
\bigl||\alpha|-a_0\bigr|
\le\frac{S_A}{\sqrt A}
\right\}.
\tag{29}
\]

For every fixed notch `0<eta<a_0`, this entire residual is eventually off-notch. Thus a fixed nondegenerate coalescing span cannot hide its projection defect in the central efficient region.

## 4. What this closes, and the precise remaining escape

`ANF-124` left open whether several coalescing profiles could cooperate even though one wrong profile has a strict coherence gap. Equation (26) closes that chamber for every fixed number of companions whose limiting phase-space points remain distinct from one another and from the target. The obstruction is stronger than positivity of the physical coefficients: it survives after granting the adversary arbitrary complex coefficients.

This is exactly the regime relevant to the near-perfect mirroring branch of `ANF-120`. A sequence whose fixed-notch exposure approaches the source efficiency ceiling forces the off-notch saddle aggregate toward zero source norm. A fixed nondegenerate finite coalescing architecture cannot do that because (29) leaves a positive fraction of the target packet's source mass in the saddle window.

The adversarial boundary is important. The proof does **not** cover configurations in which a companion phase-space point approaches `z_0`, several companion points coalesce so that `G` becomes singular, or the number `m=m_A` grows. Those are not technical omissions. If points coalesce while coefficients grow, difference quotients can generate Hermite-type derivative states; if a point approaches `z_0`, the projection distance necessarily tends to zero; and the exact nesting identity of `ANF-124` realizes a coalescing `kappa sqrt(A)` packet by `2^{Theta(sqrt(A))}` translations of the base packet. Thus the remaining chamber is a genuine **degenerate/growing coherent-state span** problem rather than another fixed finite Gram calculation.

The prior-art audit finds the Gaussian geometry itself to be classical. V. Bargmann, *On a Hilbert space of analytic functions and an associated integral transform, Part I*, Comm. Pure Appl. Math. **14** (1961), 187--214, is the classical analytic-function/Fock-space anchor; finite linear independence of distinct canonical coherent states is standard in that setting. The broader linear-independence problem for arbitrary time-frequency shifts is the HRT conjecture, but the Gaussian case used here reduces directly to the exponential-polynomial/Vandermonde argument (15)--(16). No external theorem is load-bearing in the proof above. The Mathia-specific content is the exact identification (8)--(13) of coalescing `ANF-115` physical packets with that coherent-state geometry and the resulting Montgomery--Taylor source floor (26).

The next useful gate is therefore not another fixed `m` extension. It is to resolve one of the two genuinely new limits: either derive the tangent/Hermite Gram law for **degenerating** coalescing profiles and test whether positivity/excision still kills those jets, or obtain a quantitative lower bound for **growing** coherent-state spans strong enough to compete with the exact exponential nesting architecture.
