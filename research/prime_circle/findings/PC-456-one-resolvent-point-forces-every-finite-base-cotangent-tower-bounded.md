# PC-456 — One resolvent point forces every fixed finite-base cotangent tower to be bounded

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. For every fixed nonempty finite base of distinct circle points and every Borel probability on its complete tower, a closed realization of either unchanged cotangent action has nonempty resolvent exactly in the bounded, comparable orbit-`A_2` density class. Its spectrum then equals its Haar spectrum; every closed realization outside that class, if one exists, has spectrum `C`. A matrix resolvent can lose its diagonal endpoint jumps, so the singleton proof does not extend entrywise. A finite polynomial of the resolvent restores the full endpoint jump and supplies the missing test. No closability classification, uniform growing-base estimate, prime discriminator or RH implication is asserted.

## 1. Object and exact dichotomy

Fix distinct angles `0<=theta_a<1`, `1<=a<=r`, with finite `r>=1`, and put
\[
Z=\{e^{2\pi i\theta_a}\},\qquad
X=\{1,\ldots,r\}\times\widehat{\mathbb Z}.
\]
Let `mu` be Haar probability on `Zhat` and `mu_X` its product with uniform base measure. The complete level-`m` preimages of `Z` are
\[
y_{a,t}^{(m)}=e^{2\pi i(\theta_a+t)/m},\qquad t\in\mathbb Z/m\mathbb Z.
\]
Retain the compatible pointwise cylinder matrices
\[
(B_m)_{(a,t),(c,s)}=
\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(\theta_a-\theta_c+t-s)}m,&(a,t)\ne(c,s),\\
0,&(a,t)=(c,s),
\end{cases}
\qquad B_m^+=B_m+J_{rm}/m.
\tag{1}
\]
The probability does not enter these entries. For the Prime-Circle construction, `Z=P_d^*`; arbitrary irrational-angle bases are admissible controls.

Write
\[
H_{ac}=i\cot\pi(\theta_a-\theta_c)\ (a\ne c),\quad H_{aa}=0,
\quad A=H+J_r,\quad
\mathcal B_Z=\bigcup_{\alpha\in\sigma(A)}[\alpha-2,\alpha].
\tag{2}
\]
All finite matrices in (2) are Hermitian. For a positive finite density define the orbit condition, with `Sx=x+1`, by
\[
[w]_{A_2(S)}=\operatorname*{ess\,sup}_{x}\sup_{n\ge1}
\left(\frac1n\sum_{j=0}^{n-1}w(x+j)\right)
\left(\frac1n\sum_{j=0}^{n-1}w(x+j)^{-1}\right)<\infty.
\tag{3}
\]

**Theorem.** For any Borel probability `nu` on `X`, the following are equivalent, for either prescription in (1) separately:

1. A closed operator `T` on `L^2(nu)` contains all cylinder classes, agrees there with that prescription, and has at least one resolvent point.
2. That prescription is well-defined and extends boundedly to `L^2(nu)`.
3. There are densities
   \[
   d\nu(a,x)=\frac1r w_a(x)d\mu(x),\qquad 0<w_a<\infty\ \text{a.e.},
   \quad \frac1r\sum_a\int w_a\,d\mu=1,
   \]
   such that `w_1` satisfies (3) and, for one finite `C`,
   \[
   C^{-1}w_1\le w_a\le Cw_1\quad\text{a.e. for every }a.
   \tag{4}
   \]

When these conditions hold, both actions are bounded, each closed extension is unique, and
\[
\sigma(B^+)=\mathcal B_Z,\qquad
\sigma(B)=\mathcal B_Z\cup\sigma(H).
\tag{5}
\]
If (4), including the density and orbit requirements, fails, **every closed extension of either prescription, if any exists, has empty resolvent**. No existence of such an extension is claimed.

[[research/prime_circle/findings/PC-452-finite-base-cotangent-boundedness-forces-comparable-orbit-weights]] and [[research/prime_circle/findings/PC-453-bounded-cotangent-towers-force-haar-equivalence]] give `2 <-> 3` and (5). [[research/prime_circle/findings/PC-455-one-resolvent-point-forces-singleton-cotangent-tower-boundedness]] proves `1 -> 3` only for a singleton. The new implication here is `1 -> 3` for every fixed finite base, including probabilities with no initially assumed density.

## 2. A resolvent is fixed on every cylinder space

Well-definedness of (1) forces full support of `nu`: a zero-mass input cylinder cannot have a nonzero matrix entry into a positive-mass output cylinder. The nonzero-entry graph of a cotangent matrix on at least three distinct circle points is connected, since the only omitted edges are antipodal pairs. Refine smaller levels to obtain positivity of every cylinder mass. For the augmented action every off-diagonal entry is already nonzero. This is the null-class argument of [[research/prime_circle/findings/PC-446-raw-cotangent-tower-measures-cannot-remove-spectral-bands]], valid for arbitrary distinct-angle bases.

For the character `chi_q(x)=exp(2 pi i q x)`, with rational representative `q in [0,1)`, the exact finite Fourier blocks are
\[
K(q)=D(q)AD(q)^{-1}-2qI_r,\qquad
D(q)=\operatorname{diag}(e^{2\pi i\theta_aq}).
\tag{6}
\]
The augmented prescription uses (6) also at zero. The raw prescription uses `H` at zero and (6) for `q>0`. PC-452, §4, records these pointwise identities; they do not presume weighted Fourier orthogonality.

Every corresponding eigenvector is a nonzero cylinder class by full support. Therefore every closed extension has spectrum containing `mathcal B_Z`, and the raw one also contains `sigma(H)`. Fix `lambda in rho(T)` and let `R=(T-lambda I)^{-1}`. Thus `lambda` lies outside those respective sets. On a level-`m` cylinder, uniqueness of the solution gives
\[
R|_m=(B_m^{(+)}-\lambda I)^{-1}.
\tag{7}
\]
It follows that `R`, and every polynomial in `R`, preserve cylinders and commute there with common fiber translations. No boundedness of those translations in `L^2(nu)` has been assumed.

## 3. Restore the endpoint jump by finite interpolation

Extend (6) smoothly to the **closed** real interval `[0,1]`. The elementary identity
\[
\big(e^{2\pi i(\theta_a-\theta_c)}-1\big)
\big(1+i\cot\pi(\theta_a-\theta_c)\big)=-2
\quad(a\ne c)
\]
gives
\[
K_0:=K(0)=H+J_r,\qquad K_1:=K(1)=H-J_r,
\qquad K_1-K_0=-2J_r.
\tag{8}
\]
In particular both endpoint spectra lie in `mathcal B_Z`.

The inverse's jump need not inherit entrywise nonvanishing. For example, at the base angles `(0,1/4)` and `lambda=i`, direct exact inversion gives
\[
(K_1-iI)^{-1}-(K_0-iI)^{-1}
=\begin{pmatrix}0&0\\-1&0\end{pmatrix}.
\tag{9}
\]
Both diagonal jumps vanish. Compressing the full resolvent is not the same as taking the resolvent of a diagonal compression.

Use instead the scalar polynomial
\[
Q(z)=\det\big(I_r-z(K_0-\lambda I_r)\big)
       \det\big(I_r-z(K_1-\lambda I_r)\big),\qquad
p(z)=\lambda+\frac{1-Q(z)}z.
\tag{10}
\]
Since `Q(0)=1`, `p` is a genuine polynomial of degree at most `2r-1`. For `j=0,1`, the eigenvalues of `(K_j-lambda I)^{-1}` are `(alpha-lambda)^{-1}`, with `alpha in sigma(K_j)`. On each of these, `Q` vanishes and `p((alpha-lambda)^{-1})=alpha`. Hermitian diagonalization, equivalently finite polynomial functional calculus, yields
\[
p\big((K_j-\lambda I)^{-1}\big)=K_j.
\tag{11}
\]
Repeated eigenvalues cause no problem; (10) may include redundant interpolation conditions.

The operator `P=p(R)` is bounded; write `L=||P||`. Its smooth interior matrix symbol is
\[
F(q)=p\big((K(q)-\lambda I)^{-1}\big),\qquad 0\le q\le1.
\]
The inverse exists throughout this closed interval because its spectral sets are contained in `mathcal B_Z`. Equations (8)--(11) give the universal **entrywise** jump
\[
\boxed{F(1)-F(0)=-2J_r.}
\tag{12}
\]
This recovers only the endpoint values. In general `F(q)!=K(q)` in the interior, and no identity `p(R)=T` is asserted. The polynomial is a proof device inside the algebra of a hypothetical bounded inverse, not an additional geometric operator chosen to construct a spectrum.

For every pair `a,c` put
\[
a_d^{ac}=\int_0^1F_{ac}(q)e^{2\pi i d q}\,dq.
\]
Two integrations by parts give, for nonzero integer `d`,
\[
\left|a_d^{ac}-\frac{i}{\pi d}\right|\le\frac{E}{d^2},\qquad
E=\max_{a,c}\frac{|F'_{ac}(1)|+|F'_{ac}(0)|+
                  \int_0^1|F''_{ac}(q)|\,dq}{4\pi^2}<\infty.
\tag{13}
\]
Choose an integer `N>=max(1,2 pi E)`. Then simultaneously for every entry and both signs,
\[
\operatorname{Re}\big(-i\,\operatorname{sgn}(d)a_d^{ac}\big)
\ge\frac1{2\pi|d|}\qquad(|d|\ge N).
\tag{14}
\]
The constants may depend on the fixed base and the chosen resolvent point.

At level `M`, the entries of `P` are the discrete Fourier sums of `F(j/M)`. For the raw prescription only the zero-frequency matrix is replaced, by `p((H-lambda I)^{-1})`. This changes each spatial entry by a fixed matrix entry divided by `M`. Consequently, at every fixed integer displacement `d`, for either convention,
\[
P_{M;(a,t),(c,s)}\longrightarrow a_d^{ac},\qquad d=t-s,
\tag{15}
\]
by ordinary Riemann sums. No uniform growing-block limit is used.

## 4. All finite marginals satisfy orbit A2

Average `nu` over common translations by `G_m=ker(Zhat -> Z/mZ)`. This gives
\[
d\nu_m(a,x)=\frac1r w_{a,m}(x)d\mu(x),\qquad
w_{a,m}(x)=rm\,\nu\big(\{a\}\times(x+G_m)\big)>0.
\tag{16}
\]
Apply `||Pf||_nu<=L||f||_nu` to translated cylinders and average the inequalities over `G_m`. The cylinder commutation noted after (7) gives
\[
\|Pf\|_{L^2(\nu_m)}\le L\|f\|_{L^2(\nu_m)}.
\tag{17}
\]
This operation uses translations of finite functions before averaging; it does not assume absolute continuity of `nu` or bounded translation operators on its Hilbert space.

Extend each array periodically to the integers, `W_{a,m}(t)=w_{a,m}(t mod m)`. Fix a fiber `a`, length `n>=1` and starting integer `b`. Set `D=N+2` and
\[
I=\{b,\ldots,b+n-1\},\qquad
J=\{b+Dn,\ldots,b+(D+1)n-1\},\qquad
\kappa=\frac1{2\pi(D+1)}.
\]
All positive displacements from `I` to `J` satisfy (14), with lower bound `kappa/n`; the reverse direction has the opposite fixed phase. Embed these **fixed** blocks at levels `M` tending to infinity through multiples of `m`. Test (17) on `1_I/W_{a,m}` in fiber `a`, retain outputs only in the same fiber on `J`, cancel the common normalization `1/(rM)`, and use (15). With `W_E=sum_E W_{a,m}` and `V_E=sum_E W_{a,m}^{-1}`, the result is
\[
W_JV_I\le L^2n^2/\kappa^2,
\qquad W_IV_J\le L^2n^2/\kappa^2.
\]
Cauchy--Schwarz gives `W_JV_J>=n^2`. Multiplying and cancelling proves
\[
\boxed{\frac{W_IV_I}{n^2}\le K:=L^4/\kappa^4}
\quad\text{for every }a,m,b,n.
\tag{18}
\]
This includes all short intervals and intervals longer than a period.

## 5. Cross-fiber comparability and recovery of the probability

The same tail tests the interaction between different fibers. Fix displacement `d=N`. In (17) use a single input cylinder `(c,t)` and keep the single output cylinder `(a,t+N)` at levels `M` tending through multiples of `m`. By (14)--(15),
\[
|a_N^{ac}|^2W_{a,m}(t+N)\le L^2W_{c,m}(t),\qquad
W_{a,m}(t+N)\le4\pi^2N^2L^2W_{c,m}(t).
\tag{19}
\]
Within fiber `a`, the interval `[t,t+N]` in (18) contains the product `W_{a,m}(t)/W_{a,m}(t+N)` among its positive terms. Hence
\[
W_{a,m}(t)\le K(N+1)^2W_{a,m}(t+N).
\]
Combining with (19), and then interchanging the fiber labels, yields
\[
C_0^{-1}W_{c,m}(t)\le W_{a,m}(t)\le C_0W_{c,m}(t),
\qquad C_0=4\pi^2N^2L^2K(N+1)^2,
\tag{20}
\]
uniformly in all marginals. Thus comparability has been derived before assuming a density, rather than inferred from separate orbit bounds.

For completeness, the measure-recovery step of PC-453 applies to (18) as follows. Let `alpha_a=r nu({a} times Zhat)>0`, the mean of `w_{a,m}`. The normalized arrays `w_{a,m}/alpha_a` have mean one and satisfy (18) unchanged. Their one-periodic real step interpolations
\[
v_{a,m}(u)=W_{a,m}(\lfloor mu\rfloor)/\alpha_a
\]
have ordinary real-line `A_2` characteristic at most `9K`: an interval at least one cell long is enlarged by a length factor at most three; a shorter interval meets at most two cells, whose worst weighted-average product is their two-cell `A_2` product. The reciprocal has the same characteristic. Taking an entire period in (18) bounds its mean by `K`.

The classical uniform reverse Hölder theorem therefore gives one `epsilon(K)>0` such that
\[
\|w_{a,m}/\alpha_a\|_{1+\epsilon}\le2,\qquad
\|\alpha_a/w_{a,m}\|_{1+\epsilon}\le2K.
\tag{21}
\]
These are also the profinite norms, since both spaces give equal mass to the array cells. Hytönen--Pérez, Proposition 2.2 and Theorem 2.3, supplies this step, exactly as in PC-453, §§3--4.

Along the factorial partitions, the normalized densities form mean-one martingales on Haar space by addition of cylinder masses. The first bound in (21) gives uniform integrability, hence almost-everywhere and `L^1` convergence. Their cylinder integrals recover the original fiber measures, so `nu` has the densities `w_a` in the theorem. Fatou applied to the second bound excludes zero-density regions. In particular no singular component can remain. Pass (18) and (20) to the limit, removing the countable union of integer translates of the exceptional null sets. The finite lists of positive convergent values give (3) and (4).

PC-452 now gives boundedness of both original actions and their spectra (5). This proves `1 -> 3`. Conversely boundedness gives a closed realization with nonempty resolvent. The closure of a bounded operator restricted to the dense cylinder algebra is its whole graph, already defined on the entire Hilbert space. Every closed extension containing that graph equals it. This proves uniqueness and the dichotomy for **all** closed extensions, without assuming cylinders were a core for the initially proposed `T`.

## 6. Prior art and mathematical delta

Finite polynomial reconstruction of matrix functions is classical: Nicholas J. Higham, *Functions of Matrices: Theory and Computation*, SIAM (2008), §1.2.2, [author's bibliographic record](https://eprints.maths.manchester.ac.uk/1067/). Equation (10) gives the particular polynomial explicitly, so no interpolation theorem is being used without its hypotheses.

Nondegenerate-kernel testing and averaging are also classical; see David Cruz-Uribe and John-Oliver MacLellan, *Necessary conditions for two-weight inequalities for singular integral operators*, **Studia Math. 261** (2021), 187--205, [author manuscript, Introduction and §3](https://arxiv.org/pdf/2004.08988). Its Euclidean measure hypotheses are not a profinite theorem; (16)--(20) provide the required finite-array argument directly. Atencia--Martín-Reyes, *The maximal ergodic Hilbert transform with weights*, **Pacific J. Math. 108** (1983), 257--263, [Theorem 1.2](https://msp.org/pjm/1983/108-2/pjm-v108-n2-p01-s.pdf), supplies the orbit-weight sufficiency already incorporated into PC-452. Hytönen--Pérez, *Sharp weighted bounds involving A_infinity*, **Analysis & PDE 6** (2013), 777--818, [Proposition 2.2 and Theorem 2.3](https://msp.org/apde/2013/6-4/apde-v6-n4-p02-s.pdf), supplies the uniform exponent in (21).

The bounded novelty audit covered weighted ergodic/discrete Hilbert transforms, matrix functional calculus, nondegenerate-kernel necessity and weighted cotangent resolvents. No new general interpolation or weight theorem, or historical priority, is claimed. The line-local delta is the removal of the **entire fixed finite-base unbounded/nonempty-resolvent possibility**, including noncomparable fiber densities and arbitrary singular probabilities. The new bridge beyond the singleton result is (10)--(12): a finite polynomial restores every endpoint entry despite the actual cancellation (9). The cross-fiber estimate (20) is indispensable; separate scalar orbit tests alone do not yield boundedness of the full tower.

This is not a new prime-specific coupling. The same argument applies to every distinct-angle finite base, with that base's own band endpoints. Different base geometries need not have identical spectra. The conclusion concerns spectral sets, not self-adjointness, spectral type, a Riesz basis or similarity to a self-adjoint operator.

## 7. Boundaries and decisive audit

The base is fixed and finite. The degree in (10), derivative bound in (13), polynomial operator norm, tail threshold and density constants may deteriorate with the number or separation of base points and with `lambda`. No uniform limit as the base grows follows. Changed kernels, incomplete fibers, half-density-compensated actions and domains omitting cylinder functions remain outside the theorem. Outside (4), the result is conditional on a closed extension existing and does not classify closability or closed extensions with empty resolvent.

The decisive checks are the raw zero-mode correction in (15), endpoint recovery without claiming interior recovery, two-sided complex phases in (14), common-translation averaging before assuming densities, fixed blocks during `M -> infinity`, both cross-fiber directions, and uniform integrability before measure identification. A closed unchanged-action finite-base realization outside (4) with even one resolvent point would falsify the result. Dense eigenbands alone would not exclude such an example; the polynomial-tail and weight arguments do.

## 8. Validation

The proof is analytic and literature-backed, not Lean-verified. Separate standard-library Python diagnostics checked **126** direct finite matrices: bases `P_2^*`, `P_3^*`, `P_5^*`, angles `{0,1/4}`, `{0,1/2}`, and the two irrational-angle sets `{sqrt(2),sqrt(3)} mod 1` and `{sqrt(2),sqrt(3),sqrt(5)} mod 1`; levels `m=1,3,5`; parameters `lambda=i,2i,-1+i`; and both conventions. Direct Gauss--Jordan inversion followed by polynomial matrix evaluation agreed with the assembled Fourier blocks to maximum entry error below `1.9e-13`. Endpoint reconstruction (11) had maximum entry error below `7.7e-14`. The antipodal base includes a repeated eigenvalue across the two endpoints, testing the redundant-factor case of (10).

For (9), the polynomial from (10) is exactly
\[
p(z)=-3i+12z+16iz^2-8z^3.
\]
The raw inverse jump has zero diagonals, while its polynomial restores `-2J_2`. Composite Simpson quadrature with 4,096 and 8,192 panels checked all four Fourier entries at `d=+-16,+-32,+-64`: the **24** projected coefficients divided by the leading value `1/(pi |d|)` lay between `0.9781` and `1.0270`. The two quadratures differed by less than `2.5e-9`. These are finite normalization/cancellation diagnostics, not proofs of the uniform tail estimate, density recovery or infinite spectral dichotomy. Equations (10)--(21) supply those analytic steps.
