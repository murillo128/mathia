# PC-453 — Bounded cotangent towers force Haar equivalence

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. For every fixed finite base, boundedness of either unchanged complete cotangent-tower action forces the Hilbert-space probability to be equivalent to base-uniform times fiber-Haar measure. No singular component is possible. Together with PC-452 this classifies bounded realizations under **all Borel probabilities**, rather than only probabilities assumed equivalent to Haar. The new step is uniform integrability of cylinder densities, obtained by subgroup averaging and classical reverse Hölder theory. No classification of unbounded closed realizations or RH implication follows.

## 1. Exact object and statement

Let
\[
Z=\{e^{2\pi i\theta_a}:1\le a\le r\},\qquad
0\le\theta_a<1,
\]
be a fixed nonempty finite set of distinct circle points. Its complete level-`m` preimages have coordinates
\[
y_{a,t}^{(m)}=e^{2\pi i(\theta_a+t)/m},\qquad t\in\mathbb Z/m\mathbb Z.
\]
The coherent inverse limit is `X={1,...,r} times Zhat`. Let `mu` denote Haar probability on `Zhat` and `mu_X` the product with uniform base measure. The Prime-Circle case is `Z=P_d^*`; arbitrary distinct angles are matched controls.

On all cylinder functions retain exactly
\[
(T_m)_{(a,t),(c,s)}=
\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(\theta_a-\theta_c+t-s)}m,
 &(a,t)\ne(c,s),\\
0,&(a,t)=(c,s),
\end{cases}
\qquad T_m^+=T_m+J_{rm}/m.
\tag{1}
\]
These are the compatible actions of PC-443 and PC-452. Changing the probability below does not insert quadrature weights into (1).

**Theorem.** For an arbitrary Borel probability `nu` on `X`, the following are equivalent:

1. The unchanged cylinder prescription `T` is well-defined on cylinder classes and extends boundedly to `L^2(nu)`.
2. The same assertion holds for `T^+`.
3. There are positive finite densities
   \[
   d\nu(a,x)=\frac1r w_a(x)d\mu(x),\qquad
   \frac1r\sum_a\int w_a\,d\mu=1,
   \tag{2}
   \]
   such that, with `Sx=x+1`,
   \[
   [w_1]_{A_2(S)}<\infty,\qquad
   C^{-1}w_1\le w_a\le Cw_1\quad\mu\text{-a.e. for every }a
   \tag{3}
   \]
   for some finite `C`. Here
   \[
   [w]_{A_2(S)}=
   \operatorname*{ess\,sup}_x\sup_{n\ge1}
   \left(\frac1n\sum_{j=0}^{n-1}w(x+j)\right)
   \left(\frac1n\sum_{j=0}^{n-1}w(x+j)^{-1}\right).
   \tag{4}
   \]

In particular `nu` is equivalent to `mu_X`. Indeed, for some `epsilon>0`, both `w_a` and `w_a^{-1}` belong to `L^{1+epsilon}(mu)` for every base fiber. This does not force essential upper or lower bounds on the densities.

All bounded realizations have the spectral sets already identified in PC-452. Namely, for
\[
H_{ac}=i\cot\pi(\theta_a-\theta_c)\ (a\ne c),\quad H_{aa}=0,
\qquad A=H+J_r,
\]
and the eigenvalues `lambda_alpha` of `A`,
\[
\sigma(T^+)=\bigcup_\alpha[\lambda_\alpha-2,\lambda_\alpha],
\qquad
\sigma(T)=\sigma(H)\cup\bigcup_\alpha[\lambda_\alpha-2,\lambda_\alpha].
\tag{5}
\]
This is equality of spectral sets, not a self-adjointness or spectral-type assertion.

## 2. Singleton lemma: average the measure before assuming a density

First take `r=1`. The base angle cancels from (1), leaving the scalar actions
\[
(B_m)_{ts}=\frac{i}{m}\cot\frac{\pi(t-s)}m\quad(t\ne s),
\qquad (B_m)_{tt}=0,\qquad B_m^+=B_m+J_m/m.
\tag{6}
\]
Suppose either action is bounded by `L` on cylinder functions in `L^2(nu)`. PC-446's null-class argument forces full support: at every level with at least three points the nonzero cotangent-entry graph is connected, and a zero-mass input cylinder would otherwise have a nonzero output on a positive-mass cylinder. Refining the smaller levels proves positivity of every cylinder mass. The augmented kernel has no off-diagonal zeros and obeys the same conclusion.

Set
\[
G_m=\ker(\widehat{\mathbb Z}\longrightarrow\mathbb Z/m\mathbb Z),
\qquad \nu_m=\nu*\mu_{G_m},
\tag{7}
\]
where `mu_Gm` is normalized Haar measure on that closed subgroup. Directly on cosets,
\[
d\nu_m=w_m\,d\mu,\qquad
w_m(x)=m\nu(x+G_m)>0,
\qquad \int w_m\,d\mu=1.
\tag{8}
\]
Each `w_m` has finitely many positive values. Neither (7) nor (8) assumes that `nu` has a density.

For `h in Zhat`, write `R_h f(x)=f(x+h)`. The cylinder matrices (6) are circulant, so either raw action commutes pointwise with `R_h` on cylinders. Apply its norm inequality to `R_h f` and average over `h in G_m`. Fubini gives
\[
\int |B^{(+)}f|^2\,d\nu_m
\le L^2\int |f|^2\,d\nu_m.
\tag{9}
\]
All integrands are bounded cylinder functions. No translation is being assumed bounded on `L^2(nu)`, and the individual translated measures need not equal `nu`. The averaging takes place in the inequality on pointwise cylinder functions, before extension. Their density in `L^2(nu_m)` now gives a bounded realization with the **same** bound `L`.

PC-451 applies to the equivalent probability (8). Its nonmaximal necessity estimate yields, uniformly in `m`,
\[
[w_m]_{A_2(S)}\le K:=(6\pi)^4L^4.
\tag{10}
\]
Its use here is not circular: absolute continuity of `nu_m` follows directly from subgroup averaging, while absolute continuity of the original `nu` is still to be proved. The finite two-block proof of (10) does not require a maximal-transform hypothesis.

## 3. Uniform reverse Hölder control of finite marginals

Write `W_m(t)=m nu(t+G_m)`, extended periodically to all integers. Since `w_m` is constant on each positive-Haar-mass residue cylinder, (10) is the actual finite-array statement
\[
\left(\frac1n\sum_{j=0}^{n-1}W_m(t+j)\right)
\left(\frac1n\sum_{j=0}^{n-1}W_m(t+j)^{-1}\right)\le K
\tag{11}
\]
for every integer `t` and every `n>=1`, including intervals longer than a period. In particular
\[
\frac1m\sum_{t=0}^{m-1}W_m(t)=1,
\qquad \frac1m\sum_{t=0}^{m-1}W_m(t)^{-1}\le K.
\tag{12}
\]

Define the positive, one-periodic step weight on the real line
\[
v_m(u)=W_m(\lfloor mu\rfloor).
\tag{13}
\]
Its ordinary real-line Muckenhoupt characteristic satisfies
\[
[v_m]_{A_2(\mathbb R)}\le9K.
\tag{14}
\]
Here is the passage from discrete intervals, including the small-interval boundary. If an interval `I` has length at least `1/m`, enlarge it to the union `J` of all mesh cells it meets. Then `|J|<=|I|+2/m<=3|I|`. Positivity bounds the two integrals on `I` by those on `J`, and (11) on the consecutive full cells gives (14). If `|I|<1/m`, it meets at most two cells. For their values `a,b` and relative length `theta`, the product of averages is
\[
1+\theta(1-\theta)(a/b+b/a-2)
\le\frac{(a+b)(a^{-1}+b^{-1})}{4}\le K.
\tag{15}
\]
The one-cell case gives one. The reciprocal weight has the same `A_2` characteristic.

The classical real-line reverse Hölder theorem gives an exponent `epsilon=epsilon(K)>0`, independent of `m`, such that
\[
\left(\int_0^1 v_m^{1+\epsilon}\right)^{1/(1+\epsilon)}\le2,
\qquad
\left(\int_0^1 v_m^{-(1+\epsilon)}\right)^{1/(1+\epsilon)}\le2K.
\tag{16}
\]
For a precise source, Hytönen--Pérez, Proposition 2.2 and Theorem 2.3, bound the reverse Hölder exponent using the weight characteristic. Their exponential `A_infinity` characteristic is at most the `A_2` characteristic by Jensen; Proposition 2.2 controls the Fujii--Wilson characteristic, and Theorem 2.3 supplies the factor two. A smaller common exponent may be used for both reciprocal weights by monotonicity of normalized `L^p` norms. Applying the theorem on `[0,1]`, with (12), proves (16).

The integrals in (16) are exactly the corresponding profinite integrals of `w_m` and its reciprocal, because each residue class has Haar mass `1/m`. The real-line interpolation is used only to prove these uniform finite-array moment bounds; it is not an identification of the profinite topology with the circle.

## 4. Recovering the measure and excluding every singular component

Take the cofinal generating sequence `m_k=k!`. The finite-density functions `w_{m_k}` form a nonnegative mean-one martingale on Haar space, even before `nu` is known to be absolutely continuous. Indeed, if `m` divides `n`, the masses of the `n/m` finer cylinders add to the mass of the coarser one, so
\[
\mathbb E_\mu(w_n\mid\mathcal F_m)=w_m.
\tag{17}
\]
The first bound in (16) implies uniform integrability. The martingale therefore converges almost everywhere and in `L^1(mu)` to a finite `w>=0`, with `integral w=1`.

For every residue cylinder `E`, at all sufficiently fine factorial levels,
\[
\int_E w_{m_k}\,d\mu=\nu(E).
\]
Passing to the `L^1` limit gives `integral_E w dmu=nu(E)`. These cylinders generate the Borel sigma-algebra, so uniqueness of finite measures gives
\[
\boxed{\nu=w\mu.}
\tag{18}
\]
This is the step that excludes both a purely singular probability and an arbitrary nonzero singular component mixed with an absolutely continuous part.

The reciprocal bound in (16) and Fatou's lemma give
\[
\int w^{-(1+\epsilon)}d\mu\le(2K)^{1+\epsilon},
\tag{19}
\]
with the convention that the integrand is infinite where `w=0`. Thus `w>0` almost everywhere, and (18) is equivalence, not only absolute continuity. The first moment bound similarly gives `||w||_{1+epsilon}<=2`. PC-451 now applies to the original probability and yields `w in A_2(S)`, simultaneous boundedness of both actions and spectral set `[-1,1]`.

## 5. Fixed finite bases

For general `r`, PC-446's support argument again applies to (1). Thus
\[
s_a=\nu(\{a\}\times\widehat{\mathbb Z})>0,
\qquad
\tau_a(E)=s_a^{-1}\nu(\{a\}\times E)
\tag{20}
\]
defines a full-support probability on each fiber. The coordinate projection onto that fiber is orthogonal in `L^2(nu)`. Compressing the bounded full action gives exactly (6) on `L^2(tau_a)`, with norm at most `L`; normalizing the fiber mass does not change this norm bound.

The singleton lemma proves `tau_a=rho_a mu` with `rho_a>0` almost everywhere. Hence (2) holds with `w_a=r s_a rho_a`. Each `rho_a` and its reciprocal has the common higher-integrability exponent obtained above. Since there are finitely many strictly positive `s_a`, the asserted higher integrability of every `w_a` and reciprocal follows as well, without claiming constants uniform in the fiber masses.

Having now proved equivalence to `mu_X`, invoke PC-452: its same-lift off-diagonal entry tests force the densities to be uniformly comparable, and its singleton classification supplies (3). Conversely (2)--(3) imply boundedness of both actions by that finding's bounded phase-multiplier conjugation. Its separate treatment of the constant block proves (5). No spectral equality is being inferred merely from dense cylinder eigenvalues.

## 6. Prior art, controls and limits

The load-bearing external input is Tuomas Hytönen and Carlos Pérez, *Sharp weighted bounds involving A_infinity*, **Analysis & PDE 6** (2013), 777--818, [Proposition 2.2 and Theorem 2.3, pp. 785--786](https://msp.org/apde/2013/6-4/apde-v6-n4-p02-s.pdf), DOI `10.2140/apde.2013.6.777`. This is established reverse Hölder/self-improvement theory; no new weight theorem is claimed. The application needs one common exponent controlled by (14), not just a separate positive exponent for every finite weight.

The existing orbit classification rests on Atencia and Martín-Reyes, *The maximal ergodic Hilbert transform with weights*, **Pacific J. Math. 108** (1983), 257--263, [Theorem 1.2](https://msp.org/pjm/1983/108-2/pjm-v108-n2-p01-s.pdf). That theorem starts with a density. It does not by itself justify assuming a density for the arbitrary probability in this finding; (7)--(19) provide that missing passage. Averaging measures, finite-weight interpolation and uniform-integrability martingale convergence are classical tools. The prior-art search covered weighted ergodic Hilbert transforms, singular measures and reverse Hölder self-improvement; it supplies no historical novelty claim for their combination.

The precise line-local delta is **necessity of Haar equivalence for every bounded unchanged-action realization**, closing the singular-probability boundary explicitly left by [[research/prime_circle/findings/PC-451-cotangent-tower-boundedness-is-exactly-orbit-a2]] and [[research/prime_circle/findings/PC-452-finite-base-cotangent-boundedness-forces-comparable-orbit-weights]]. Unlike [[research/prime_circle/findings/PC-448-haar-admixture-does-not-close-rigid-cotangent-towers]], it requires no character-rigidity sequence, but concludes absence of a bounded realization rather than nonclosability.

All steps apply to an irrational-angle singleton and every finite distinct-angle base under the same cotangent rule. The result is therefore a control-blind obstruction to changing this fixed action by changing only the Hilbert-space probability. Finite base geometry still determines the band endpoints in (5); different bases need not have the same endpoints. No prime-birth discriminator, zeta-zero exclusion, critical-line selection or arithmetic coercivity is supplied.

Full support alone remains only the well-definedness gate. Failure of Haar equivalence here does **not** imply nonclosability, empty resolvent or absence of an unbounded closed extension. Conversely unbounded densities can satisfy (3), as PC-450 shows. Changed kernels, half-density compensation, restricted domains discarding cylinders, incomplete fibers and growing-base limits remain outside the theorem. There is no uniform growing-base estimate hidden in (3) or (5).

## 7. Validation and decisive audit

The proof is analytic and literature-backed, not formally verified. Its decisive dependencies are the exact covariance of the unchanged scalar cylinder action in (9), the uniform nonmaximal bound (10), the passage from **all integer intervals** to real intervals in (14), and a reverse Hölder exponent independent of the refinement level. Equation (17) is proved from finite masses, rather than assuming an unknown Radon--Nikodym derivative. Uniform integrability is used before identifying the limiting measure; almost-everywhere martingale convergence alone would lose singular mass. The reciprocal estimate is then used separately to exclude a zero-density region.

A singular full-support probability supporting either bounded raw action would falsify the theorem. A family of finite marginals satisfying (9) with one bound but lacking the common moment control (16) would falsify its key compactness step. Neither weak convergence of measures nor equality of the spectra of finite regularizations is used as a substitute for that step.
