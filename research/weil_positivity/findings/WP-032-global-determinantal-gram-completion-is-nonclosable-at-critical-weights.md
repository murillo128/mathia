# WP-032 — Global determinantal Gram completion is nonclosable at the critical weights

**Status:** `EXACT-DERIVED + CLASSICAL-PRIOR-ART + DECISIVE-NEGATIVE` for the most direct attempt to globalize the positive Gram/rank mechanism of WP-030 into one closed positive form on the canonical counting Hilbert space of prime places or prime-power events. The finite WP-030 Gram matrices are perfectly positive on every finite support, and their vanishing higher minors admit the standard rank-one determinantal/exterior-algebra interpretation. But after the exact Riemann half-energy attenuation is applied to the **Gram feature amplitude**, the coefficient vector `((log p)/sqrt(p))_p` is not square summable. The resulting positive quadratic form on finitely supported vectors is **not closable**. Hence there is no bounded positive operator, closed positive energy form, or positive-contraction determinantal kernel on the natural `ell^2` place space whose principal minors globally realize the WP-030 selector at the critical weights. Adding an arbitrary archimedean Hilbert sector cannot repair this while keeping the same finite restriction.

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

## 3. Non-summable singleton Gram mass makes the positive form nonclosable

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

## 5. Critical attenuation belongs to the Gram feature amplitude

WP-030 does not read its singleton arithmetic coefficient from the Gram diagonal itself. It reads the positive **top volume**

\[
\sqrt{\det G_{\{p\}}}=\log p.
\]

Therefore, to incorporate the half-energy attenuation while preserving the same WP-030 volume normalization, the criticalized feature amplitude must be

\[
\boxed{
b_p^{(1/2)}=\frac{\log p}{\sqrt p}.}
\tag{14}
\]

The corresponding rank-one Gram kernel is

\[
K_{pq}^{(1/2)}
=b_p^{(1/2)}\overline{b_q^{(1/2)}}
=\frac{(\log p)(\log q)}{\sqrt{pq}},
\tag{15}
\]

with diagonal Gram mass

\[
w_p^{(1/2)}=K_{pp}^{(1/2)}
=|b_p^{(1/2)}|^2
=\frac{(\log p)^2}{p}.
\tag{16}
\]

Its singleton top volume is exactly the desired arithmetic coefficient:

\[
\sqrt{\det K_{\{p\}}^{(1/2)}}
=\sqrt{w_p^{(1/2)}}
=\frac{\log p}{\sqrt p}.
\tag{17}
\]

But

\[
\sum_p w_p^{(1/2)}
=\sum_p\frac{(\log p)^2}{p}
=\infty.
\tag{18}
\]

A minimal proof again needs only Euler's divergence of `sum_p 1/p`: `(log p)^2>=1` for every sufficiently large prime. Hence the positive form associated with (15) is nonclosable by Section 3.

The same conclusion holds on the full prime-power event set

\[
J=\{(p,k):p\text{ prime},\ k\ge1\}
\]

with WP-030-compatible attenuated amplitudes

\[
b_{p,k}^{(1/2)}=\frac{\log p}{p^{k/2}},
\qquad
w_{p,k}^{(1/2)}=|b_{p,k}^{(1/2)}|^2
=\frac{(\log p)^2}{p^k},
\tag{19}
\]

because the `k=1` subseries is exactly (18).

Thus the failure occurs **before** the WP-005 autocorrelation lift and before any gamma/pole completion is discussed.

## 6. The exact WP-030 Gram closability threshold is sigma = 1/2

For a general attenuation exponent `sigma>0`, preserving the WP-030 singleton top-volume convention means using the feature amplitudes

\[
b_p(\sigma)=(\log p)p^{-\sigma}
\]

and therefore

\[
K_{pq}^{(\sigma)}
=b_p(\sigma)\overline{b_q(\sigma)}
=(\log p)(\log q)(pq)^{-\sigma},
\qquad
w_p(\sigma)=\frac{(\log p)^2}{p^{2\sigma}}.
\tag{20}
\]

By Section 3, the rank-one form is closable exactly when its coefficient vector lies in `ell^2(P)`, equivalently when

\[
\sum_p\frac{(\log p)^2}{p^{2\sigma}}<\infty.
\tag{21}
\]

This has the exact boundary

\[
\boxed{\sigma>\frac12.}
\tag{22}
\]

For `sigma>1/2`, convergence follows by comparison with

\[
\sum_{n\ge2}\frac{(\log n)^2}{n^{2\sigma}}<\infty.
\]

At `sigma=1/2`, (21) becomes (18) and diverges; for `sigma<1/2` the terms are larger for all sufficiently large primes. Thus the critical value is exactly the boundary of this WP-030-compatible global rank-one Hilbert realization, not the Euler-product boundary `sigma=1`.

The prime-power family has the same threshold:

\[
\sum_{p,k\ge1}|b_{p,k}(\sigma)|^2
=\sum_{p,k\ge1}\frac{(\log p)^2}{p^{2k\sigma}}.
\tag{23}
\]

The `k=1` terms force divergence for `sigma<=1/2`; for `sigma>1/2`, summing the geometric tail in `k` reduces convergence to the same comparison as in (21).

This boundary is purely operator-theoretic. It uses no zeros, RH, analytic continuation, or Euler-product argument.

## 7. Arbitrary archimedean coupling cannot repair the finite restriction

Suppose one enlarges the Hilbert space to

\[
H=\ell^2(J)\oplus H_\infty
\]

and seeks a closed positive quadratic form `Q` whose restriction to finitely supported pure finite-place vectors is the rank-one form (7) with the exact critical WP-030-compatible amplitudes.

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
\tag{24}
\]

For bounded positive operators the statement is even more immediate: compression to the finite-place closed subspace would give a bounded positive operator there, which Section 3 forbids.

This is stronger than the direct rank count in WP-030 Section 5. The archimedean sector may now have arbitrary dimension and arbitrary coupling. It still cannot make a nonclosable finite Gram restriction into a closed positive geometry.

## 8. Determinantal-process prior art explains what the finite selector really is

For a discrete determinantal process with kernel `K`, the `r`-point correlation on a finite set `S` is the principal minor

\[
\rho(S)=\det K_S.
\tag{25}
\]

Rank-one determinantal kernels therefore have exactly the qualitative support pattern seen in WP-030: singleton minors may be positive, while every minor of order at least two vanishes. In matroid language this is the rank-one case.

Russell Lyons' classical treatment of determinantal probability measures develops precisely this positive-contraction/principal-minor and exterior-algebra framework:

- Russell Lyons, *Determinantal probability measures*, Publications Mathématiques de l'IHÉS **98** (2003), 167--212, DOI `10.1007/s10240-003-0016-0`.

So the finite determinant mechanism of WP-030 has a standard probabilistic/combinatorial home. The Mathia-specific issue is not positivity of the finite minors; it is whether the exact arithmetic amplitudes define a legitimate **global** positive kernel.

They do not on the natural counting space. A determinantal probability kernel must in particular be a bounded positive contraction. A finite rank-one cutoff with diagonal Gram masses `w_i=|b_i|^2` has unique nonzero eigenvalue

\[
\lambda=\sum_i w_i.
\tag{26}
\]

At the critical WP-030 scale, (18) forces `lambda -> infinity` as the cutoff grows. Renormalizing by `lambda` restores a probability kernel but changes the Gram diagonal to `w_i/lambda` and the singleton top-volume amplitude to `|b_i|/sqrt(lambda)`, so it no longer realizes the exact Weil coefficient scale.

The DPP comparison is therefore a prior-art redirect, not a new positivity route.

## 9. Matched controls

The proof uses only:

1. a countable collection of generator/event labels;
2. positive singleton Gram masses `w_i`;
3. vanishing two-point Gram determinants;
4. divergence of `sum_i w_i`.

It applies unchanged to any generalized-prime or weighted free-monoid system with non-square-summable critical feature amplitudes. Conversely, if `sum_i w_i<infinity`, the rank-one form

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

A normalization distinction is also essential. WP-033 studies the **stronger separate modeling assumption** that `log p/sqrt(p)` itself is a quadratic-form value on a unit prime-event state. That diagonal-mass model is not the same as preserving WP-030, where `log p/sqrt(p)` is the square root of a singleton Gram determinant and the corresponding diagonal mass is `(log p)^2/p`. WP-032's exact threshold statement is only about this WP-030-compatible top-volume normalization.

## 11. Falsification tests and research consequence

The claim is falsified if any of the following fails:

1. vanishing every positive `2 x 2` Gram determinant forces equality in Cauchy--Schwarz and hence one-dimensional Gram span;
2. this gives the representation (7) on finitely supported vectors;
3. `sum_i w_i=infinity` makes the coefficient functional `L` unbounded on `ell^2(J)`;
4. the normalized sequence in (9) violates the closability criterion exactly as in (10)--(11);
5. preserving the WP-030 top-volume normalization at exponent `sigma` gives feature amplitudes `b_p(sigma)=(log p)p^{-sigma}` and diagonal Gram masses `(log p)^2 p^{-2sigma}`;
6. `sum_p (log p)^2/p` diverges, while `sum_p (log p)^2/p^{2 sigma}` converges for every `sigma>1/2`;
7. the full prime-power squared-amplitude series has the same threshold because its `k=1` subseries is decisive and the `k>=2` tail is geometric;
8. any global closed positive form agreeing with this finite restriction would inherit the same nonclosability witness on vectors with zero archimedean component;
9. a rank-one determinantal positive-contraction kernel cannot retain exact critical singleton Gram masses whose total sum diverges.

All nine tests are elementary or classical and require no RH assumption, zero data, analytic continuation, or numerical experiment.

The research consequence is a global gate on the promising WP-030 route:

\[
\boxed{
\text{finite positive Gram minors}
\not\Rightarrow
\text{one global closed positive Gram geometry at the critical weights}.
}
\]

The successful local rank/volume selector must remain **support dependent** or undergo a genuine change of Hilbert representation before globalization. Simply declaring the compatible finite Gram matrices to be one infinite positive kernel — even with arbitrary later archimedean coupling — is not mathematically available on the canonical Prime-Lattice counting Hilbert space at `sigma=1/2`.

## Internal dependencies

- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-009-prime-lattice-weil-weights-fail-passive-jump-energy.md`
- `research/weil_positivity/findings/WP-030-incidence-gram-volume-recovers-von-mangoldt-positively-but-is-a-rank-test.md`
- `research/weil_positivity/findings/WP-031-place-additive-positive-quadratic-readouts-cannot-select-prime-powers.md`
- `research/weil_positivity/findings/WP-033-stable-hilbert-renorming-cannot-rescue-critical-mangoldt-gram-selector.md`
