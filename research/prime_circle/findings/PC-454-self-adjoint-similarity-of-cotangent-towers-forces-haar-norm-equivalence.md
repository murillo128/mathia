# PC-454 — Self-adjoint similarity of cotangent towers forces Haar norm equivalence

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. Among all bounded unchanged complete cotangent-tower realizations over a fixed finite base, bounded similarity to a self-adjoint operator is possible exactly when the measure has a density bounded above and below relative to canonical Haar probability. The augmented singleton has an exact optimal similarity constant, recovered from integer translations inside its exponential group. Orbit `A_2` boundedness and an unchanged real spectral band do not suffice. This is a specialization of classical similarity and weighted translation theory, not a prime discriminator or an RH implication.

## 1. Object and theorem

Fix distinct angles `0<=theta_a<1`, `1<=a<=r`, with `r` finite and nonzero. The complete level-`m` preimages of their circle points have coordinates
\[
y_{a,t}^{(m)}=e^{2\pi i(\theta_a+t)/m},\qquad t\in\mathbb Z/m\mathbb Z.
\]
Their coherent inverse limit is `X={1,...,r} times Zhat`, with canonical probability `mu_X` equal to uniform base measure times Haar probability `mu` on `Zhat`. The primitive-shell case is `Z=P_d^*`; irrational-angle bases are matched controls.

Keep the unchanged compatible cylinder action
\[
(T_m)_{(a,t),(c,s)}=
\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(\theta_a-\theta_c+t-s)}m,&(a,t)\ne(c,s),\\
0,&(a,t)=(c,s),
\end{cases}
\qquad T_m^+=T_m+J_{rm}/m.
\tag{1}
\]
Here `J_k` is the `k` by `k` all-ones matrix. Changing the Hilbert-space probability does not insert weights into (1).

Let `nu` be a Borel probability for which either action is well-defined on cylinder classes and extends boundedly to `L^2(nu)`. PC-453 proves that both extend boundedly and
\[
d\nu(a,x)=\frac1r w_a(x)d\mu(x),\qquad
0<w_a<\infty\quad\text{a.e.},
\tag{2}
\]
where the finitely many densities are uniformly comparable and a reference density `w=w_1` is orbit `A_2` for `x -> x+1`.

**Theorem.** The following are equivalent:

1. `T` is boundedly similar to a self-adjoint operator.
2. `T^+` is boundedly similar to a self-adjoint operator.
3. There are constants `0<c<=C<infinity` such that `c<=w_a<=C` almost everywhere for every `a`.
4. `sup_{t in R} ||exp(itT)|| < infinity`.
5. `sup_{t in R} ||exp(itT^+)|| < infinity`.

Similarity permits an arbitrary bounded invertible intertwiner, not just a multiplication operator or a prescribed change of density. Consequently no other bounded positive invertible Hilbert metric can evade condition 3. In that condition the identity map to the Haar space already supplies a similarity to the original Haar action.

For the singleton write `B_w^+=T^+`, put `H_w=L^2(Zhat,w mu)`, normalize `integral w dmu=1`, and define
\[
c_w=\operatorname*{ess\,inf}w,\qquad C_w=\operatorname*{ess\,sup}w,
\]
\[
\kappa_{\mathrm{sa}}(B_w^+)
=\inf\{\|L\|\|L^{-1}\|:LB_w^+L^{-1}\text{ is self-adjoint}\}.
\]
The infimum over an empty set is infinity. Then, with extended-real values,
\[
\boxed{
\kappa_{\mathrm{sa}}(B_w^+)
=\sup_{t\in\mathbb R}\|e^{itB_w^+}\|
=\sup_{n\in\mathbb Z}\|e^{\pi i nB_w^+}\|
=\sqrt{C_w/c_w}.}
\tag{3}
\]
The right side is infinite if `c_w=0` or `C_w=infinity`. No sharp constant is asserted here for the unaugmented or multiple-base action.

## 2. The exponential contains the entire integer translation group

On the singleton, for `q=j/m in [0,1)` put `chi_q(x)=exp(2 pi i j(x mod m)/m)`. These characters satisfy
\[
B_w^+\chi_q=(1-2q)\chi_q.
\tag{4}
\]
Their finite span is the dense cylinder algebra. Define `R_k f(x)=f(x+k)`. For every integer `n`, (4) gives on cylinders
\[
e^{\pi i nB_w^+}\chi_q
=(-1)^n e^{-2\pi i nq}\chi_q,
\qquad
\boxed{e^{\pi i nB_w^+}=(-1)^nR_{-n}.}
\tag{5}
\]
The equality extends to the weighted space. Indeed orbit `A_2` at two consecutive points bounds both `w(x+1)/w(x)` and its reciprocal; iteration makes each integer translation bounded. Equivalently, the bounded exponential in (5) gives its unique bounded extension from cylinders. Translation on measurable functions agrees with that extension by density and equivalence of the measures.

Haar invariance and change of variables give the exact norm
\[
\|R_{-n}\|_{H_w\to H_w}^2
=\operatorname*{ess\,sup}_x\frac{w(x+n)}{w(x)}.
\tag{6}
\]
For example, the upper bound is immediate after writing the squared output norm as `integral |f(x)|^2 w(x+n) dmu(x)`. Indicators of sets on which the ratio approaches its essential supremum give the lower bound. This also proves the extended-value version before boundedness is known.

Translation by one is ergodic on Haar `Zhat`: on its complete Haar character basis, the eigenvalue `exp(2 pi i q)` equals one only at `q=0`. This ergodicity sharpens (6) to
\[
\sup_{n\in\mathbb Z}\operatorname*{ess\,sup}_x
\frac{w(x+n)}{w(x)}=C_w/c_w.
\tag{7}
\]
To prove the lower bound, choose positive thresholds `ell>c_w` and `h<C_w` for which the low set `{w<ell}` and high set `{w>h}` have positive measure. The union of all integer translates of the high set has full measure by ergodicity. Hence some translate intersects the low set in positive measure, and on that intersection `w(x+n)/w(x)>h/ell`. Let `h` increase and `ell` decrease to their essential endpoints. The argument also gives arbitrarily large ratios when either endpoint is infinite or zero. Constant weights give equality directly. The upper bound when both endpoints are finite is immediate.

This step uses measurable ergodicity, not an assumption that a continuous positive weight attains extrema or that topologically dense integer orbits sample a measurable weight uniformly.

## 3. Optimal similarity and the constant-mode exception

If `LB_w^+L^{-1}=A=A*`, then
\[
\|e^{itB_w^+}\|=\|L^{-1}e^{itA}L\|
\le\|L^{-1}\|\|L\|\qquad(t\in\mathbb R).
\tag{8}
\]
Equations (5)--(7) therefore force `kappa_sa>=sqrt(C_w/c_w)`, without assumptions on the form of `L` or on a chosen eigenbasis.

Conversely, if `0<c_w<=C_w<infinity`, the identity `J:H_w -> L^2(mu)` has
\[
\|J\|=c_w^{-1/2},\qquad \|J^{-1}\|=C_w^{1/2},
\]
and intertwines `B_w^+` with its bounded self-adjoint Haar realization. If similarity is required within one Hilbert space, compose `J` with the unitary `L^2(mu) -> H_w`, `f -> w^{-1/2}f`. This has the same condition number and transports the Haar self-adjoint operator to `H_w`. It proves the matching upper bound for all real times and for the infimum, completing (3).

For the unaugmented singleton, let
\[
P_0f=\left(\int f\,d\mu\right)\mathbf1,\qquad N=\ker P_0.
\tag{9}
\]
The orbit `A_2` classification gives `integral w^{-1} dmu<infinity`, so `P_0` is bounded. It commutes with the two actions, and
\[
B_w=B_w^+-P_0,
\qquad
e^{itB_w^+}=e^{itB_w}\bigl(I+(e^{it}-1)P_0\bigr).
\tag{10}
\]
The second factor and its inverse are uniformly bounded in real `t`. Thus the two exponential groups are uniformly bounded simultaneously. In particular the unaugmented endpoint `b(0)=0`, and its degeneracy with `q=1/2`, cannot invalidate the qualitative similarity obstruction. Applying (5) directly to the unaugmented action would be incorrect.

## 4. Finite-base reduction preserves the obstruction

Use the reference density `w=w_1`; multiplying it by a positive constant changes none of the operator norms or density ratios, so its integral need not be normalized. PC-452 proves that equivalence of norms from cross-fiber comparability, followed by a bounded invertible phase-multiplier conjugation, transforms `T^+` into
\[
\mathcal C^+=(A-I_r)\otimes I+I_r\otimes B_w^+
\quad\text{on }\mathbb C^r\otimes H_w,
\tag{11}
\]
where
\[
H_{ac}=i\cot\pi(\theta_a-\theta_c)\ (a\ne c),\quad H_{aa}=0,
\qquad A=H+J_r.
\]
Both `H` and `A` are finite Hermitian matrices. Explicitly the phase multiplier on fiber `a` sends `chi_q` to `exp(2 pi i theta_a q)chi_q`; PC-452 proves boundedness of it and its inverse using the orbit-weight interval calculus. No unbounded formal Fourier change of basis is being used.

The commuting tensor factors in (11) give
\[
e^{it\mathcal C^+}=e^{it(A-I_r)}\otimes e^{itB_w^+},
\qquad
\|e^{it\mathcal C^+}\|=\|e^{itB_w^+}\|.
\tag{12}
\]
Fixed bounded similarities preserve whether a group is uniformly bounded. Equations (3) and (12) therefore make condition 5 equivalent to bounds above and below for `w`; comparability makes that equivalent to condition 3 for every fiber.

For `T`, the same conjugation and the bounded topological direct decomposition
\[
\mathbb C^r\otimes H_w
=(\mathbb C^r\otimes\operatorname{ran}P_0)
\mathbin{\dotplus}(\mathbb C^r\otimes N)
\tag{13}
\]
give the finite block `H` on the first summand and the restriction of (11) on the second. This is PC-452's separate constant-block calculation. Its exponential group is uniformly bounded exactly when `exp(it B_w^+|_N)` is uniformly bounded: the other factors are finite Hermitian exponentials. Adding back the scalar constant eigenvalue `1`, with the bounded projections `P_0` and `I-P_0`, shows this is equivalent to uniform boundedness of the full singleton group. Thus condition 4 is also equivalent to condition 3.

Self-adjoint similarity for either full action implies the corresponding uniform bound by (8). Conversely condition 3 makes the identity to `L^2(mu_X)` boundedly invertible and intertwines the action with its self-adjoint Haar realization, as in PC-444. This proves all five equivalences. No separation of overlapping base bands or simplicity of their eigenvalues is required.

## 5. Prior art and the mathematical consequence

Béla Sz.-Nagy, *On uniformly bounded linear transformations in Hilbert space*, **Acta Sci. Math. (Szeged) 11** (1947), 152--157, [Theorems I--II, pp. 152--153](https://acta.bibl.u-szeged.hu/38563/1/math_011_fasc_003.pdf), proves the classical unitarizability of uniformly bounded groups. The necessity (8) is elementary; this finding proves sufficiency by the explicit Haar identification, without invoking an abstract unitarization theorem. The exact optimal constant (3) uses the tower's translation identity and ergodicity, not the general theorem's bound.

Earl Berkson and T. A. Gillespie, *Spectral decompositions, ergodic averages, and the Hilbert transform*, **Studia Math. 144** (2001), 39--61, [Introduction, p. 40](https://www.impan.pl/shop/en/publication/transaction/download/product/90253), DOI `10.4064/sm144-1-2`, explicitly distinguishes spectral decomposability from power boundedness, including Hilbert-space examples. Accordingly the separation between bounded ordered spectral projections and a uniformly bounded group is classical operator theory. The present formulas give that distinction for the actual cotangent tower and its admitted weights. Weighted Fourier/Riesz-basis theory is a second classical viewpoint; failure of a particular eigenfamily alone is not used to exclude arbitrary similarities here. No historical novelty is claimed.

The exact local inputs are [[research/prime_circle/findings/PC-450-bounded-weighted-cotangent-towers-retain-the-haar-band]], [[research/prime_circle/findings/PC-451-cotangent-tower-boundedness-is-exactly-orbit-a2]], [[research/prime_circle/findings/PC-452-finite-base-cotangent-boundedness-forces-comparable-orbit-weights]], and [[research/prime_circle/findings/PC-453-bounded-cotangent-towers-force-haar-equivalence]]. PC-444 supplied bounded-density sufficiency; the present necessity excludes **every** bounded self-adjoint similarity outside that regime. The scalar quantitative statement additionally proves optimality of the Haar norm comparison.

In particular PC-450's unbounded orbit `A_1` densities give bounded raw operators with spectrum `[-1,1]` whose exponential groups have unbounded norm supremum and which are not similar to any self-adjoint operator. Its densities `(1-epsilon)+epsilon w` have the same obstruction for every `0<epsilon<=1` while converging to Haar in total variation as `epsilon` tends to zero. The obstruction therefore concerns the uniform metric, not spectral-set equality or total-variation proximity. Bounded nonconstant densities do admit similarity, while PC-444 says the unchanged action itself is symmetric only at Haar.

All arguments work for arbitrary distinct nonarithmetic base angles. They do not recover prime birth, move zeta zeros, or select a critical line. This closes the bounded-metric repair of the classified fixed-base weighted towers. It does not address unbounded intertwiners, changed cylinder prescriptions, unbounded closed realizations, incomplete fibers, or growing-base limits.

## 6. Validation and decisive audit

The proof is analytic and is not Lean-verified. Standard-library Python independently exponentiated the direct finite singleton cotangent matrices by scaling, Taylor summation and squaring. The **49 cases** `m in {1,2,3,4,5,8,13}`, `n=-3,...,3` checked (5) with maximum entry error below `3.6e-15` and the constant-mode correction (10) below `3.7e-15`. For each level, the three positive profiles `1`, `1+((7t+3) mod 11)`, and its reciprocal gave **21 exact rational checks** of the finite version of (7). Weighted squared-column norms of the exponential agreed with (6) to error below `2.7e-14`. These diagnostics check signs, endpoints and finite normalization; they do not establish the infinite essential-supremum or similarity assertion.

The decisive analytic checks are ergodicity in (7), boundedness of each phase multiplier before (11), and retaining the topological constant/mean-zero decomposition in (13). Sampling only even integers in (5) would lose the sharp conclusion: a nonconstant positive density depending only on parity has `||R_{-2n}||=1` despite `C_w/c_w>1`. A bounded unchanged realization with an essentially unbounded density or reciprocal and a bounded self-adjoint similarity would falsify the theorem. For the augmented singleton, any similarity with condition number strictly less than `sqrt(C_w/c_w)` would already contradict the full signed-translation subgroup. Equality of real spectra alone is never used as evidence for similarity.
