# WP-032 — Global determinantal Gram completion is nonclosable at the critical weights

**Status:** `EXACT-DERIVED + CLASSICAL-PRIOR-ART + DECISIVE-NEGATIVE` for the most direct attempt to globalize the positive Gram/rank mechanism of WP-030 into one closed positive form on the canonical counting Hilbert space of prime places or prime-power events. The finite WP-030 Gram matrices are perfectly positive on every finite support, and their vanishing higher minors admit the standard rank-one determinantal/exterior-algebra interpretation. But the exact Riemann weights force a non-square-summable rank-one coefficient vector. The resulting positive quadratic form on finitely supported vectors is **not closable**. Hence there is no bounded positive operator, closed positive energy form, or positive-contraction determinantal kernel on the natural `ell^2` place space whose principal minors globally realize the WP-030 selector at the critical weights. Adding an arbitrary archimedean Hilbert sector cannot repair this while keeping the same finite restriction.

## 1. The finite WP-030 matrices are compatible with one formal rank-one kernel

For a finite prime support `S`, WP-030 constructs the positive Gram matrix

\[
G_S=(a_pa_q)_{p,q\in S},
\qquad a_p=\log p,
\tag{1}
\]

so that

\[
\sqrt{\det G_S}
=
\begin{cases}
\log p,&S=\{p\},\\
0,&|S|\ge2.
\end{cases}
\tag{2}
\]

These finite matrices are mutually compatible under principal compression. Formally they are the finite principal minors of

\[
K^{\rm raw}_{pq}=a_pa_q.
\tag{3}
\]

Thus there is an obvious candidate global geometry on the canonical degree-one space

\[
H_{\rm fin}=\ell^2(\mathbb P):
\qquad
q_{\rm raw}(x)
=\left|\sum_p (\log p)x_p\right|^2,
\qquad x\in c_{00}(\mathbb P).
\tag{4}
\]

Every finite restriction is positive and has exactly the WP-030 rank-one structure. The question is whether (4) is the restriction of a legitimate closed positive form on `ell^2(P)`.

It is not.

## 2. General rank-one lemma from vanishing two-point Gram determinants

The obstruction does not depend on the exact phases in (3).

Let `J` be a countable index set and let `q` be a positive semidefinite Hermitian form on `c_00(J)`. Write

\[
K_{ij}=q(e_i,e_j),
\qquad
w_i=K_{ii}>0.
\tag{5}
\]

Assume that every two-point principal Gram determinant vanishes:

\[
\det
\begin{pmatrix}
w_i&K_{ij}\\
K_{ji}&w_j
\end{pmatrix}
=0
\qquad(i\ne j).
\tag{6}
\]

Positivity gives Cauchy--Schwarz,

\[
|K_{ij}|^2\le w_iw_j,
\]

and (6) is equality for every pair. In the pre-Hilbert space obtained by quotienting the radical of `q`, equality in Cauchy--Schwarz implies that all basis classes are collinear. Therefore there are phases `zeta_i`, `|zeta_i|=1`, such that on `c_00(J)`

\[
\boxed{
q(x)=|L(x)|^2,
\qquad
L(x)=\sum_{i\in J}\zeta_i\sqrt{w_i}\,x_i.
}
\tag{7}
\]

So the vanishing higher-minor support rule does not merely suggest rank one: **positivity plus the two-point zeros force rank one.**

This is the operator-theoretic core of the determinantal interpretation of WP-030.

## 3. Non-summable singleton mass makes the positive form nonclosable

Suppose

\[
\sum_{i\in J}w_i=\infty.
\tag{8}
\]

Then the coefficient vector

\[
c_i=\zeta_i\sqrt{w_i}
\]

is not in `ell^2(J)`, so `L` in (7) is an unbounded linear functional on the dense subspace `c_00(J)`.

This already rules out a bounded rank-one operator, but the failure is stronger: the positive quadratic form itself is not closable.

Because `L` is unbounded, for every integer `m>=1` there is a finitely supported vector `y_m` with

\[
|L(y_m)|>m\|y_m\|_2.
\]

After rescaling and adjusting phase, choose `x_m in c_00(J)` such that

\[
L(x_m)=1,
\qquad
\|x_m\|_2<\frac1m.
\tag{9}
\]

Then

\[
x_m\to0\quad\text{in }\ell^2(J),
\]

while

\[
q(x_m-x_n)
=|L(x_m)-L(x_n)|^2
=0
\tag{10}
\]

for every `m,n`, but

\[
q(x_m)=1.
\tag{11}
\]

Equations (9)--(11) violate the defining closability criterion for a positive quadratic form. Hence

\[
\boxed{
\sum_i w_i=\infty
\quad\Longrightarrow\quad
q\text{ is not closable on }\ell^2(J).
}
\tag{12}
\]

This is an exact obstruction, not a failure of a particular regularization.

## 4. The raw WP-030 Gram kernel already fails globally

For the direct global kernel (3),

\[
w_p=(\log p)^2.
\]

Thus

\[
\sum_p w_p=\sum_p(\log p)^2=\infty,
\]

so the formal global version of the WP-030 Gram family is nonclosable on the canonical degree-one Hilbert space `ell^2(P)`.

Equivalently, the formal incidence map

\[
B^*:c_{00}(\mathbb P)\to\mathbb C,
\qquad
B^*x=\sum_p(\log p)x_p
\tag{13}
\]

is not closable. Therefore the finite positive operators `G_S=B_SB_S^*` do **not** arise as compressions of one closed global rank-one incidence operator on the natural counting Hilbert space.

This distinction is invisible if one studies only finite supports: every finite matrix is perfectly positive, yet the compatible infinite family has no closed positive-form completion.

## 5. Criticalizing the singleton weights does not help

One might try to build the half-energy attenuation into the positive Gram feature itself rather than multiply the WP-030 determinant afterward.

For the prime events `p`, the desired singleton coefficient is

\[
w_p^{(1/2)}
=\frac{\log p}{\sqrt p}.
\tag{14}
\]

The unique rank-one positive Gram pattern with these diagonals and vanishing two-point determinants has, up to phases,

\[
K_{pq}^{(1/2)}
=\sqrt{w_p^{(1/2)}w_q^{(1/2)}}.
\tag{15}
\]

But

\[
\sum_p\frac{\log p}{\sqrt p}=\infty.
\tag{16}
\]

A minimal proof needs only Euler's divergence of `sum_p 1/p`: for every prime `p>=3`,

\[
\frac{\log p}{\sqrt p}\ge\frac1p.
\]

Therefore the form associated with (15) is again nonclosable by Section 3.

The same conclusion holds on the full prime-power event set

\[
J=\{(p,k):p\text{ prime},\ k\ge1\}
\]

with exact finite Weil weights

\[
w_{p,k}=\frac{\log p}{p^{k/2}},
\tag{17}
\]

because the `k=1` subseries already gives (16).

Thus the failure occurs **before** the WP-005 autocorrelation lift and before any gamma/pole completion is discussed.

## 6. The exact threshold is the Euler convergence half-plane

The obstruction identifies a useful analytic boundary rather than merely saying that `1/2` is bad.

For

\[
w_p(\sigma)=\frac{\log p}{p^\sigma},
\qquad \sigma>0,
\tag{18}
\]

a global rank-one positive form with singleton masses `w_p(sigma)` is closable on the counting `ell^2(P)` exactly when

\[
\sum_p w_p(\sigma)<\infty.
\tag{19}
\]

The prime sum in (19) converges for `sigma>1` and diverges for `sigma<=1`. Likewise

\[
\sum_{p,k\ge1}\frac{\log p}{p^{k\sigma}}
\]

converges exactly in the Euler-product half-plane `sigma>1`.

Hence the rank-one Gram geometry has the same qualitative boundary repeatedly encountered elsewhere in this research line:

\[
\boxed{
\text{honest global positive rank-one kernel}
\quad\text{for }\sigma>1,
\qquad
\text{nonclosable at }\sigma=\tfrac12.
}
\tag{20}
\]

This does not use zeros or RH. It is simply the operator-domain cost of retaining the exact positive prime masses globally.

## 7. Arbitrary archimedean coupling cannot repair the finite restriction

Suppose one enlarges the Hilbert space to

\[
H=\ell^2(J)\oplus H_\infty
\]

and seeks a closed positive quadratic form `Q` whose restriction to finitely supported pure finite-place vectors is the rank-one form (7) with the exact critical weights.

The sequence `(x_m,0)` from Section 3 still satisfies

\[
(x_m,0)\to0,
\qquad
Q((x_m-x_n,0))=0,
\qquad
Q((x_m,0))=1.
\]

That contradicts closability of the global form `Q` itself.

Therefore

\[
\boxed{
\text{no closed positive finite--archimedean form can contain this nonclosable finite restriction.}
}
\tag{21}
\]

For bounded positive operators the statement is even more immediate: compression to the finite-place closed subspace would give a bounded positive operator there, which Section 3 forbids.

This is stronger than the direct rank count in WP-030 Section 5. The archimedean sector may now have arbitrary dimension and arbitrary coupling. It still cannot make a nonclosable finite Gram restriction into a closed positive geometry.

## 8. Determinantal-process prior art explains what the finite selector really is

For a discrete determinantal process with kernel `K`, the `r`-point correlation on a finite set `S` is the principal minor

\[
\rho(S)=\det K_S.
\tag{22}
\]

Rank-one determinantal kernels therefore have exactly the qualitative support pattern seen in WP-030: singleton minors may be positive, while every minor of order at least two vanishes. In matroid language this is the rank-one case.

Russell Lyons' classical treatment of determinantal probability measures develops precisely this positive-contraction/principal-minor and exterior-algebra framework:

- Russell Lyons, *Determinantal probability measures*, Publications Mathématiques de l'IHÉS **98** (2003), 167--212, DOI `10.1007/s10240-003-0016-0`.

So the finite determinant mechanism of WP-030 has a standard probabilistic/combinatorial home. The Mathia-specific issue is not positivity of the finite minors; it is whether the exact arithmetic weights define a legitimate **global** positive kernel.

They do not on the natural counting space. A determinantal probability kernel must in particular be a bounded positive contraction. A finite rank-one cutoff with diagonal weights `w_i` has unique nonzero eigenvalue

\[
\lambda=\sum_i w_i.
\tag{23}
\]

As the cutoff grows, the exact critical mass in (16) forces `lambda -> infinity`. Renormalizing by `lambda` restores a probability kernel but changes every arithmetic weight to `w_i/lambda`, so it no longer realizes the exact Weil coefficient scale.

The DPP comparison is therefore a prior-art redirect, not a new positivity route.

## 9. Matched controls

The proof uses only:

1. a countable collection of generator/event labels;
2. positive singleton masses `w_i`;
3. vanishing two-point Gram determinants;
4. divergence of `sum_i w_i`.

It applies unchanged to any generalized-prime or weighted free-monoid system with non-summable critical singleton masses. Conversely, if `sum_i w_i<infinity`, the rank-one form

\[
q(x)=\left|\sum_i\sqrt{w_i}x_i\right|^2
\]

is bounded and perfectly legitimate.

Thus WP-032 is an **operator-category obstruction**, not evidence specific to the rational primes. Its value is to locate exactly where the local positive determinant geometry ceases to define a global Hilbert object.

## 10. Boundary of the obstruction

WP-032 does **not** rule out:

- the support-dependent finite Gram family of WP-030 itself;
- performing a nonlinear determinant, rank, or exterior operation separately on each finite exponent support before entering any global Hilbert space;
- changing the finite-place base measure or Hilbert norm so that the coefficient vector becomes square summable, provided the resulting bridge back to the Weil test-function normalization is derived rather than inserted;
- a genuinely non-Hilbert or distributional global object for which closed positive quadratic-form theory is not the relevant category;
- an indefinite or graded intermediate geometry whose final assembled form is positive by a separate theorem;
- an infinite-dimensional compression/localization that changes the finite-place representation before the critical weights are interpreted as one Gram kernel;
- a global construction that does not encode Mangoldt support through vanishing principal minors of one positive kernel.

It also does not replace WP-005 or WP-009. Even a hypothetical way around the present domain obstruction would still have to explain why the exact finite coefficients enter the Weil autocorrelation with the required sign and how the archimedean/polar sector creates global positivity.

## 11. Falsification tests and research consequence

The claim is falsified if any of the following fails:

1. vanishing every positive `2 x 2` Gram determinant forces equality in Cauchy--Schwarz and hence one-dimensional Gram span;
2. this gives the representation (7) on finitely supported vectors;
3. `sum_i w_i=infinity` makes the coefficient functional `L` unbounded on `ell^2(J)`;
4. the normalized sequence in (9) violates the closability criterion exactly as in (10)--(11);
5. `sum_p (log p)/sqrt(p)=infinity`;
6. the full prime-power critical series also diverges because it contains the `k=1` subseries;
7. any global closed positive form agreeing with this finite restriction would inherit the same nonclosability witness on vectors with zero archimedean component;
8. a rank-one determinantal positive-contraction kernel cannot retain exact singleton masses whose total sum diverges.

All eight tests are elementary or classical and require no RH assumption, zero data, analytic continuation, or numerical experiment.

The research consequence is a new global gate on the promising WP-030 route:

\[
\boxed{
\text{finite positive Gram minors}
\not\Rightarrow
\text{one global closed positive Gram geometry at the critical weights}.
}
\]

The successful local rank/volume selector must remain **support dependent** or undergo a genuine change of Hilbert representation before globalization. Simply declaring the compatible finite Gram matrices to be one infinite positive kernel — even with arbitrary later archimedean coupling — is not mathematically available on the canonical Prime-Lattice counting Hilbert space.

## Internal dependencies

- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-009-prime-lattice-weil-weights-fail-passive-jump-energy.md`
- `research/weil_positivity/findings/WP-030-incidence-gram-volume-recovers-von-mangoldt-positively-but-is-a-rank-test.md`
- `research/weil_positivity/findings/WP-031-place-additive-positive-quadratic-readouts-cannot-select-prime-powers.md`
