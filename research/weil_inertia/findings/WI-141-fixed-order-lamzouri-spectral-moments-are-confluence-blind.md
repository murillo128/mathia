# WI-141 — fixed-order Lamzouri spectral moments are confluence-blind

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. WI-138 shows that Lamzouri's self-adjoint tensor operator counts each distinct off-line conjugate pair by one negative eigenvalue, while WI-140 shows that the complete finite Lamzouri deficit can nevertheless tend to zero when a simple off-line pair conflues to a critical-line double. The same confluence kills a substantially broader rescue route: **every fixed finite package of continuous spectral statistics of the Lamzouri operator is asymptotically blind to this replacement**.

For one simple off-line pair `x +/- i y`, the Lamzouri operator has the exact two-point spectrum

\[
\boxed{\lambda_+(y)=2(1+t(y)),\qquad \lambda_-(y)=-2t(y),}
\]

where

\[
t(y)=\int_{\mathbb R}\eta(u)^2\sinh^2(2\pi u y)\,du
=4\pi^2\mu_2y^2+O(y^4),
\qquad
\mu_2=\int u^2\eta(u)^2\,du>0.
\]

The collapsed real double, padded by the disappearing odd direction, has spectrum `(2,0)`. Hence for every fixed integer `r >= 1`,

\[
\boxed{
\operatorname{tr}(\mathcal A_y^r)
=2^r\bigl((1+t)^r+(-t)^r\bigr)
=2^r+O_r(y^2),
}
\]

with `tr A_y = 2` exactly. More strongly, as operators on Lamzouri's common ambient Hilbert space,

\[
\boxed{\|\mathcal A_y-\mathcal A_0\|_{S_p}=O(y^2)}
\qquad(1\le p\le\infty).
\]

Thus fixed trace moments, Schatten norms, characteristic-polynomial coefficients after zero padding, and every other locally continuous finite-dimensional spectral functional converge to their real-double values, even though the negative index is exactly one for every `y>0` and zero at `y=0`. Rank, inertia, determinant sign, and similarly discontinuous/singular quantities can still distinguish the pair; what they do **not** supply is a positive quantitative gap.

Consequently, adding any fixed number of ordinary higher trace moments of the Lamzouri tensor to the existing `trace + Hilbert--Schmidt` information cannot by itself produce a universal positive charge per off-line pair. A density-scale version follows by combining the exact one-pair estimate with the WI-140 block construction: for every fixed moment order `R`, one may choose the horizontal depths tending to zero rapidly enough that a positive-density simple off-line population and its real-double collapse have the same normalized moments `tr(A^r)/N` up to `o(1)` simultaneously for all `1 <= r <= R`, while the off-line configuration still has a positive-density negative index. Any successful moment/minor/determinant bootstrap must therefore introduce a **singular or source-specific scale** -- for example a divided-difference normalization, a resolvent scale shrinking toward zero, a proved lower bound on horizontal depth, or an interaction theorem that prevents simultaneous confluence in actual zeta configurations. Merely knowing more fixed continuous moments is not enough.

This is an abstract Lamzouri/inertia barrier, not a zeta counterexample and not a barrier to higher moments for the separate task of improving the critical Gram certificate. Actual zeta zeros obey density/correlation/arithmetic constraints absent from the dilute WI-140 near-extremizers; a genuinely new arithmetic observable can still rule those configurations out.

## 1. Exact pair spectrum

Use Lamzouri's setup from Proposition 2.1 of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1. Normalize

\[
\int_{\mathbb R}\eta(u)^2\,du=1,
\]

and fix a simple conjugate pair

\[
z=x+iy,\qquad \bar z=x-iy,\qquad y>0.
\]

Write

\[
f(u)=\eta(u)e^{-2\pi iux},
\]

so that Lamzouri's even/odd vectors are

\[
g_y(u)=f(u)\cosh(2\pi uy),
\qquad
h_y(u)=-i f(u)\sinh(2\pi uy).
\tag{1}
\]

Because `eta^2` is even and `cosh(2 pi u y)sinh(2 pi u y)` is odd,

\[
\langle g_y,h_y\rangle=0.
\tag{2}
\]

Set

\[
t(y):=\|h_y\|^2.
\tag{3}
\]

The identity `cosh^2-sinh^2=1` gives

\[
\|g_y\|^2=1+t(y).
\tag{4}
\]

For a simple pair, WI-137's self-adjoint tensor operator is exactly

\[
\mathcal A_y=2(g_y\otimes g_y-h_y\otimes h_y).
\tag{5}
\]

Since the two rank-one directions in (5) are orthogonal, its nonzero eigenvalues are

\[
\boxed{
2\|g_y\|^2=2(1+t),
\qquad
-2\|h_y\|^2=-2t.
}
\tag{6}
\]

This recovers WI-140's isolated-pair calculation and WI-138's exact negative index without perturbation theory.

At `y=0`, `g_0=f` and `h_0=0`. The pair has conflued to a real point of multiplicity two and

\[
\mathcal A_0=2f\otimes f.
\tag{7}
\]

If the disappearing odd direction is retained as a zero direction for comparison, the spectra are therefore

\[
\operatorname{spec}(\mathcal A_y)=\{2(1+t),-2t\},
\qquad
\operatorname{spec}(\mathcal A_0)=\{2,0\}.
\tag{8}
\]

Compact support of `eta` permits termwise Taylor expansion:

\[
\boxed{
t(y)=4\pi^2\mu_2y^2+O(y^4),}
\qquad
\mu_2:=\int u^2\eta(u)^2\,du>0.
\tag{9}
\]

Thus the negative eigenvalue is topologically persistent for every `y>0` but its magnitude is only quadratic in the horizontal displacement.

## 2. The whole operator converges quadratically, not only its eigenvalues

The spectral calculation is enough for trace moments, but the stronger operator statement clarifies the boundary of every continuous finite-dimensional refinement.

On the compact support of `eta`,

\[
\cosh(2\pi uy)-1=O(y^2),
\qquad
\sinh(2\pi uy)=O(y),
\]

uniformly in `u`. Hence

\[
\|g_y-f\|_2=O(y^2),
\qquad
\|h_y\|_2=O(y).
\tag{10}
\]

For every Schatten norm, a rank-one operator satisfies

\[
\|a\otimes b\|_{S_p}=\|a\|\,\|b\|.
\tag{11}
\]

Using

\[
g_y\otimes g_y-f\otimes f
=(g_y-f)\otimes g_y+f\otimes(g_y-f),
\]

(10)--(11) give

\[
\|g_y\otimes g_y-f\otimes f\|_{S_p}=O(y^2),
\qquad
\|h_y\otimes h_y\|_{S_p}=O(y^2).
\]

Equation (5) therefore yields the uniform finite-rank estimate

\[
\boxed{
\|\mathcal A_y-\mathcal A_0\|_{S_p}=O(y^2)
\quad\text{for every }1\le p\le\infty.
}
\tag{12}
\]

This is the precise topological obstruction. Any functional that is locally continuous in one of these equivalent finite-rank matrix topologies must converge to its real-double value. A locally Lipschitz functional does so at `O(y^2)`.

The discontinuous exceptions are exactly the sort already exposed by WI-138. For every `y>0`, the padded two-dimensional inertia is `(1,1,0)` and the rank is two; at `y=0` the inertia is `(1,0,1)` and the rank is one. Continuity of the matrix does not imply continuity of inertia at an eigenvalue crossing zero.

## 3. Every fixed trace-moment package collapses explicitly

From (6), for every integer `r>=1`,

\[
\boxed{
M_r(y):=\operatorname{tr}(\mathcal A_y^r)
=2^r\left((1+t)^r+(-t)^r\right).
}
\tag{13}
\]

For `r=1`,

\[
M_1(y)=2
\tag{14}
\]

exactly. This is the one-pair instance of Lamzouri's global identity `tr A_F=N`.

For every fixed `r>=2`, (9) and (13) give

\[
\boxed{
M_r(y)-M_r(0)=O_r(t)=O_r(y^2).
}
\tag{15}
\]

For example,

\[
M_2(y)-4=8t+8t^2,
\tag{16}
\]

which is exactly the simple-pair Lamzouri deficit of WI-140, while

\[
M_3(y)-8=24t+24t^2.
\tag{17}
\]

So the third moment does not open a count gap that the second moment missed: it vanishes on precisely the same quadratic confluence scale. The same is true for every fixed higher order.

The characteristic polynomial on the padded two-dimensional space is equally explicit:

\[
\boxed{
\chi_y(\lambda)
=(\lambda-2(1+t))(\lambda+2t)
=\lambda^2-2\lambda-4t(1+t).
}
\tag{18}
\]

At the double endpoint,

\[
\chi_0(\lambda)=\lambda(\lambda-2).
\tag{19}
\]

Thus every coefficient converges, and the determinant satisfies

\[
\det\mathcal A_y=-4t(1+t)
=-16\pi^2\mu_2y^2+O(y^4).
\tag{20}
\]

Its **sign** distinguishes the off-line pair from the padded double for every nonzero `y`, but its magnitude has no uniform lower bound. A determinant argument therefore needs a new lower bound or a singular normalization; the bare nonvanishing statement does not charge pair count.

The same continuity applies to any fixed principal minor of a compression `P A_y P` when the finite-rank projection `P` is chosen independently of `y`: the matrix entries converge by (12), and determinants are polynomial in those entries. A basis or compression that itself divides by the collapsing odd direction is intentionally outside this statement.

## 4. Fixed finite moment information cannot rescue pair count

A universal count charge from finitely many continuous moments would require a positive separation between the off-line and double moment vectors. Equation (15) rules that out already for one pair.

More explicitly, fix `R`. The moment map

\[
\mathcal M_R(y)
:=\bigl(M_1(y),\ldots,M_R(y)\bigr)
\]

satisfies

\[
\boxed{
\mathcal M_R(y)\longrightarrow\mathcal M_R(0)
\qquad(y\to0^+),
}
\tag{21}
\]

while

\[
n_-(\mathcal A_y)=1,
\qquad
n_-(\mathcal A_0)=0.
\tag{22}
\]

Therefore there is no continuous function of `M_1,...,M_R` that vanishes on the double endpoint yet is bounded below by a positive constant on every simple off-line pair. The same statement holds for any finite family of locally continuous spectral functionals of `A_y`.

This is stronger than the WI-140 statement `inf Delta=0` at fixed pair count. WI-140 kills a charge extracted from the **existing finite deficit**. Equations (12)--(22) show that supplying finitely many additional ordinary spectral moments or continuous finite matrix invariants does not repair that defect: their data vector itself converges to the double data vector.

There is also a density-scale version inside Lamzouri's abstract finite class. Start from the WI-140 mixed construction with `a` isolated simple-real blocks and `b` simple off-line pair blocks. Replace each pair by its collapsed real double to obtain a comparison configuration with the same total multiplicity. Let `N=a+2b`, and give every off-line pair a common depth `y_N`.

For small `y_N`, the triangle inequality applied blockwise to (12) gives

\[
\|\mathcal A_{\rm off}-\mathcal A_{\rm dbl}\|_{S_1}
\ll b y_N^2\ll Ny_N^2.
\tag{23}
\]

Both operator norms are `O(N)` without any spacing assumption. The telescoping identity

\[
A^r-B^r
=\sum_{j=0}^{r-1}A^j(A-B)B^{r-1-j}
\]

therefore gives

\[
\left|\operatorname{tr}(\mathcal A_{\rm off}^r)
-\operatorname{tr}(\mathcal A_{\rm dbl}^r)\right|
\ll_r N^r y_N^2.
\tag{24}
\]

Choose, for example, `y_N=N^{-(R+1)}`. Then simultaneously for every `1<=r<=R`,

\[
\boxed{
\frac1N\left|\operatorname{tr}(\mathcal A_{\rm off}^r)
-\operatorname{tr}(\mathcal A_{\rm dbl}^r)\right|
\longrightarrow0.
}
\tag{25}
\]

The center separations in WI-140 may independently be taken large enough that the complete Lamzouri deficit per zero also tends to zero. Hence for any prescribed limiting simple-real fraction `s in [0,1]` and any fixed `R`, the abstract finite class contains a near-sharp sequence in which the entire complementary fraction is simple and off-line, the negative index has positive density when `s<1`, and the first `R` normalized tensor moments are asymptotically indistinguishable from those of the corresponding real-double collapse.

This does not assert that actual zeta zeros can realize the dilute centers or the rapidly shrinking horizontal depths. It isolates exactly which missing source-specific theorem would be needed to prevent the construction.

## 5. What escapes the no-go

The obstruction applies to a **fixed finite package of continuous matrix observables** at a scale that remains regular as `y->0`. Several routes therefore remain logically open, but each must pay for information absent from ordinary fixed moments.

First, inertia and rank are discontinuous at the confluent endpoint and already distinguish the two populations exactly by WI-138. WI-140 shows why sign information alone is not quantitative: the new negative eigenvalue may have arbitrarily small magnitude.

Second, singular normalizations can retain the missing horizontal direction. WI-132 divides the odd vector by `y` and obtains the confluent divided difference

\[
\frac{h_{x+iy}}y\longrightarrow -2\pi i u\,\eta(u)e^{-2\pi iux}.
\]

That is precisely the type of operation excluded from the continuity statement above. It removes the unavoidable `y` factor, but the actual Lamzouri slack still contains the square-depth weight `y^2`, and WI-133--WI-136 show that the normalized quotient can itself screen.

Third, a resolvent or log-determinant evaluated on a spectral scale tending to zero could amplify the near-zero negative cloud. Such an observable is not uniformly continuous at the confluent matrix and would require a new arithmetic or analytic evaluation before it can be used in the zeta problem. Bare determinant nonvanishing, by (20), is insufficient.

Fourth, a source-specific theorem may simply forbid extensive confluence. A lower bound on a positive-density set of normalized horizontal depths, a density/correlation theorem coupling those depths to vertical spacing, or another arithmetic statistic that changes at order one under the off-line-to-double replacement would evade the abstract construction.

Finally, this finding says nothing against higher trace moments used on the **critical Gram side** to improve the already-certified simple-critical proportion. Those moments may still constrain positive Gram geometry or recover rank/trace slack. The no-go concerns the different task of converting Lamzouri's exact negative **index** into a quantitative off-line **count charge** when the associated negative eigenvalues are allowed to confluence to zero.

## 6. Prior art and novelty audit

The primary zeta source is Lamzouri's arXiv:2609.02882v1, Proposition 2.1 and its Hilbert-space proof. WI-137 identifies the associated self-adjoint tensor operator and the complete Hilbert--Schmidt slack; WI-138 identifies its inertia by Sylvester congruence; WI-140 supplies the exact simple-pair confluence and the fixed-count/dilute near-extremizer obstruction. Those are the source-side inputs used here.

Continuity of Hermitian spectra and of polynomial spectral functions under matrix perturbation is classical matrix analysis; no novelty is claimed for it. Standard references include Kato's *Perturbation Theory for Linear Operators* and modern expositions such as Benjamin Texier, *Basic matrix perturbation theory*, Enseign. Math. 64 (2018), 249--263, which treats continuity of finite-dimensional spectra and coalescing eigenvalues. Likewise, continuity of determinants/principal minors is elementary polynomial algebra.

The targeted Mathia audit found no earlier `weil_inertia` finding that closes the **fixed higher-moment rescue** in this form. WI-140 proves only that the already-exposed Lamzouri deficit can have zero infimum at fixed off-line pair count; WI-132--WI-136 explore singular divided-difference/Schur normalizations rather than ordinary continuous moment data. The durable additional content here is the exact all-`r` formula (13), the Schatten convergence (12), and the density-scale consequence (25), which together show that finitely many additional fixed-order Lamzouri tensor moments remain asymptotically indistinguishable from the real-double endpoint.

This is not a priority claim. It is a specialization of classical perturbation continuity to the new Lamzouri operator, coupled to the exact zero-type interpretation supplied by WI-138--WI-140.

## 7. Research consequence

The complement-characterization program should not spend arithmetic effort evaluating a third, fourth, or any other **fixed finite number of ordinary Lamzouri tensor trace moments** merely in the hope that negative index will then acquire a uniform cost. Simple-pair confluence makes every such fixed moment package converge to the critical-double package.

The next useful observable must retain information that is discontinuous or singular at confluence, or it must import a genuinely zeta-specific constraint preventing the horizontal depth from collapsing on a density-scale population. This narrows the live bootstrap interface from "more spectral data" to "spectral data with a confluence-sensitive scale or new arithmetic coupling."