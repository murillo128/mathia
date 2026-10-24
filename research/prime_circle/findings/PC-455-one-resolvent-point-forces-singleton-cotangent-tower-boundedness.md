# PC-455 — One resolvent point forces singleton cotangent-tower boundedness

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. For the unchanged complete singleton cotangent tower, any closed realization on any Borel probability with a nonempty resolvent is already the bounded orbit-`A_2` realization. Consequently every closed realization has spectrum either `[-1,1]` or the whole complex plane. The new implication starts from one bounded inverse, not a bound on the raw action. It uses the nonvanishing jump of the inverse sawtooth multiplier and classical weighted singular-integral testing. It supplies no prime discriminator, classification of closability, or RH implication.

## 1. Object and spectral dichotomy

Fix a singleton base `z_0=exp(2 pi i theta)` and its complete power-map preimages
\[
y_t^{(m)}=e^{2\pi i(\theta+t)/m},\qquad t\in\mathbb Z/m\mathbb Z.
\]
The coherent lift space is `X=Zhat`, with Haar probability `mu`. On the algebra of all cylinder functions keep the compatible matrices
\[
(B_m)_{ts}=\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(t-s)}m,&t\ne s,\\
0,&t=s,
\end{cases}
\qquad B_m^+=B_m+J_m/m.
\tag{1}
\]
Changing the probability does not change these entries. The Prime-Circle singleton is `P_2^*={-1}`; every other singleton, including an irrational-angle control, has the same differences in (1).

Let `nu` be any Borel probability on `X`. For either prescription separately, the following are equivalent:

1. There exists a closed operator `T` on `L^2(nu)`, containing all cylinder classes with the action (1), for which `rho(T)` is nonempty.
2. The cylinder prescription is well-defined and extends boundedly to `L^2(nu)`.
3. `nu=w mu`, where `0<w<infinity` almost everywhere, `integral w dmu=1`, and
   \[
   [w]_{A_2(S)}:=\operatorname*{ess\,sup}_{x\in X}\sup_{n\ge1}
   \left(\frac1n\sum_{j=0}^{n-1}w(x+j)\right)
   \left(\frac1n\sum_{j=0}^{n-1}w(x+j)^{-1}\right)<\infty,
   \quad Sx=x+1.
   \tag{2}
   \]

These conditions hold for both prescriptions simultaneously. When they hold, their respective closed extensions are unique, everywhere defined and bounded, and each has spectrum `[-1,1]`. If (3) fails, **every closed extension, if any exists, has empty resolvent and spectrum `C`**. No existence of a closed extension is asserted in this second case.

[[research/prime_circle/findings/PC-451-cotangent-tower-boundedness-is-exactly-orbit-a2]] and [[research/prime_circle/findings/PC-453-bounded-cotangent-towers-force-haar-equivalence]] establish the bounded-action classification, and [[research/prime_circle/findings/PC-450-bounded-weighted-cotangent-towers-retain-the-haar-band]] supplies the exact band spectrum. The substantive new implication is `1 -> 3`. It extends the explicit empty-resolvent family of [[research/prime_circle/findings/PC-449-equivalent-power-weights-give-cotangent-towers-empty-resolvent]] to every singleton probability outside the bounded class, conditional only on existence of a closed extension.

## 2. A hypothetical resolvent fixes a bounded cylinder multiplier

Existence of `T` implies full support of `nu`. Indeed a cylinder of zero mass represents the zero vector, so its indicator must have zero image on every positive-mass cylinder. The nonzero-entry graph of `B_m` is connected for `m>=3`: only opposite vertices can have a zero off-diagonal cotangent, and these omissions do not disconnect the graph. The augmented graph has every off-diagonal entry nonzero. Thus the zero-mass vertices cannot be separated from the positive-mass ones; refining the smaller levels proves that every residue cylinder has positive mass. This is the singleton null-class argument of PC-446.

For `q=j/m` represented in `[0,1)`, the characters satisfy
\[
B\chi_q=b(q)\chi_q,\qquad
b(0)=0,\quad b(q)=1-2q\ (q>0),\qquad
B^+\chi_q=(1-2q)\chi_q.
\tag{3}
\]
All characters have norm one under `nu`. Their eigenvalues are dense in `[-1,1]`, so closedness of the spectrum of `T` forces any `lambda in rho(T)` to lie outside that band.

Fix such a `lambda`, and set `L=||(T-lambda)^{-1}||`. For every level-`m` cylinder `h`, the finite matrix inverse supplies a cylinder solution of `(T-lambda)u=h`. Uniqueness forces
\[
R_\lambda h:=(T-\lambda)^{-1}h
  =(B_m^{(+)}-\lambda I)^{-1}h.
\tag{4}
\]
Thus `R_lambda` maps cylinders to cylinders, commutes there with every translation `R_h f(x)=f(x+h)`, and obeys
\[
\|R_\lambda f\|_{L^2(\nu)}\le L\|f\|_{L^2(\nu)}.
\tag{5}
\]
The superscript `(+)` means either convention throughout. No Fourier expansion in the unknown weighted Hilbert space is assumed: (3)--(4) are finite cylinder identities.

## 3. The inverse symbol retains a nonzero two-sided tail

Define the smooth function on the **closed** interval
\[
r_\lambda(q)=\frac1{1-2q-\lambda},\qquad
a_d=\int_0^1 r_\lambda(q)e^{2\pi i d q}\,dq\quad(d\in\mathbb Z).
\tag{6}
\]
The endpoints are unequal:
\[
\Delta_\lambda=r_\lambda(1)-r_\lambda(0)
=\frac{2}{\lambda^2-1}\ne0,
\qquad c_\lambda=\frac{\Delta_\lambda}{2\pi i}.
\tag{7}
\]
Twice integrating by parts, for every nonzero integer `d`, gives
\[
\left|a_d-\frac{c_\lambda}{d}\right|
\le\frac{E_\lambda}{d^2},\qquad
E_\lambda:=\frac{|r'_\lambda(1)|+|r'_\lambda(0)|+
                       \int_0^1|r''_\lambda(q)|\,dq}{4\pi^2}<\infty.
\tag{8}
\]
Choose an integer `N>=1` with `N>=2 E_lambda/|c_lambda|`. For `|d|>=N`,
\[
\operatorname{Re}\left(
\frac{\overline{c_\lambda}}{|c_\lambda|}\operatorname{sgn}(d)a_d\right)
\ge\frac{|c_\lambda|}{2|d|}.
\tag{9}
\]
The phase is fixed on each direction. This treats arbitrary complex `lambda`; positivity or reality of the full inverse kernel is not required.

At finite level `M`, the entry at displacement `d=t-s` is
\[
k_M^{(+)}(d)=\frac1M\sum_{j=0}^{M-1}
  \frac{e^{2\pi i j d/M}}{b^{(+)}(j/M)-\lambda}.
\tag{10}
\]
For each fixed integer `d`, Riemann sums give `k_M^{(+)}(d) -> a_d`. In the unaugmented case the single altered `j=0` value changes (10) by
\[
\frac1M\left(-\frac1\lambda-\frac1{1-\lambda}\right),
\tag{11}
\]
which tends to zero. In particular an endpoint modification does not remove (7). We will take this limit only on fixed finite blocks, never uniformly over a growing block or over `lambda` approaching the band.

## 4. Average the measure, then test separated blocks

Set `G_m=ker(X -> Z/mZ)` and average the original probability over that subgroup:
\[
\nu_m=\nu*\mu_{G_m}=w_m\mu,
\qquad w_m(x)=m\nu(x+G_m)>0.
\tag{12}
\]
Each `w_m` is a positive finite periodic array, with Haar mean one. Apply (5) to translated cylinder functions and average over `h in G_m`. The pointwise commutation from (4), followed by Fubini, gives
\[
\|R_\lambda f\|_{L^2(\nu_m)}\le L\|f\|_{L^2(\nu_m)}.
\tag{13}
\]
This step does not presume that translations are bounded on `L^2(nu)`, or that `nu` has a density. Only cylinder functions are translated before averaging their inequalities.

Write `W_m(t)=w_m(t mod m)` on the integers. Fix `m`, `n>=1` and an arbitrary integer `a`. Put `D=N+2` and take
\[
I=\{a,\ldots,a+n-1\},\qquad
J=\{a+Dn,\ldots,a+(D+1)n-1\}.
\tag{14}
\]
For `s in I,t in J`, one has `N<=t-s<=(D+1)n`. Consequently (9) gives a fixed-phase lower bound `kappa/n` for every `a_(t-s)`, where
\[
\kappa=\frac{|c_\lambda|}{2(D+1)}>0.
\tag{15}
\]
In the reverse direction the opposite phase gives the same bound.

For arbitrarily large multiples `M` of `m`, these two blocks embed as disjoint residue blocks modulo `M`. Their level-`M` weights for `nu_m` are exactly `W_m(t)`, including when the blocks cross residue zero. Test (13) on the level-`M` function `f=1_I/W_m`. Restrict the output norm to `J` and cancel the common normalization `1/M`. Taking `M -> infinity` through multiples of `m` in these finite sums yields
\[
\sum_{t\in J}\left|\sum_{s\in I}\frac{a_{t-s}}{W_m(s)}\right|^2W_m(t)
\le L^2\sum_{s\in I}W_m(s)^{-1}.
\tag{16}
\]
For an integer interval `E`, write `W_E=sum_E W_m` and `V_E=sum_E W_m^{-1}`. The phase bound and (16) imply
\[
W_J V_I\le\frac{L^2n^2}{\kappa^2}.
\]
Interchanging the two blocks gives `W_I V_J<=L^2 n^2/kappa^2`. Since `W_J V_J>=n^2` by Cauchy--Schwarz,
\[
\boxed{\frac{W_I V_I}{n^2}\le K:=\frac{L^4}{\kappa^4}.}
\tag{17}
\]
This holds for **every** `m,n,a`, with the same finite `K`. The separation multiplier `D` depends on `lambda` but not on the block length or the marginal. Short intervals are included by separating them farther; no small-distance coefficient is assumed nonzero.

## 5. Recover the original measure and close the implication

Here (17) supplies exactly the finite-marginal input to the compactness argument in PC-453, §§3--4. For completeness, its required steps are as follows. On the real line define the one-periodic step weight
\[
v_m(u)=W_m(\lfloor mu\rfloor).
\]
For intervals of length at least `1/m`, enlarging to full mesh cells costs at most a factor three in length and gives `[v_m]_(A_2(R))<=9K`. A shorter interval meets at most two cells. For their values `a,b` and relative length `eta`, its product of averages is
\[
1+\eta(1-\eta)(a/b+b/a-2)
\le (a+b)(a^{-1}+b^{-1})/4\le K.
\]
Thus the same real-line bound holds at every scale, also for `v_m^{-1}`. Taking `n=m` in (17) gives `integral w_m^{-1} dmu<=K`. The classical reverse Hölder theorem now gives a common `epsilon>0`, depending only on `K`, such that
\[
\|w_m\|_{L^{1+\epsilon}(\mu)}\le2,
\qquad
\|w_m^{-1}\|_{L^{1+\epsilon}(\mu)}\le2K.
\tag{18}
\]
The source is Hytönen--Pérez, Proposition 2.2 and Theorem 2.3, as detailed in PC-453. This application uses equality of the real-line and profinite finite-array moments, not an identification of their topologies.

The functions `w_(k!)` form a nonnegative mean-one martingale on Haar space directly from addition of cylinder masses. Equation (18) makes it uniformly integrable, so it converges almost everywhere and in `L^1(mu)` to a finite `w`. For every residue cylinder `E`, its integrals eventually equal `nu(E)`; the limit therefore gives `nu=w mu` on the generating cylinder algebra and hence on all Borel sets. Fatou's lemma applied to the reciprocal bound proves `w>0` almost everywhere. This excludes every singular component without assuming absolute continuity in (12).

Remove all integer translates of the null set where martingale convergence fails. For each remaining `x`, pass to the limit in (17) along the finite lists `w_(k!)(x+j)`, whose limits are positive and finite. This proves (2). The weighted ergodic Hilbert-transform theorem, via PC-451, gives boundedness of both cylinder prescriptions. It applies to Haar-preserving ergodic translation `S` on the nonatomic probability space `X`, with the positive integrable density just obtained. Thus `1 -> 3` is proved.

Conversely (3) gives boundedness by PC-451 and therefore a closed realization with nonempty resolvent. PC-450 constructs its inverses outside `[-1,1]` using bounded interval-character projections, and PC-451 supplies the reciprocal integrability needed for the unaugmented constant-mode correction. Their spectra are exactly that band.

Finally, the graph closure of a bounded operator restricted to a dense cylinder algebra is its whole graph. Any closed extension containing that restriction contains this whole graph, already defined on the entire Hilbert space, and hence equals the bounded operator. This proves uniqueness and the dichotomy for **every** closed extension. No assumption that cylinders are a core for an initially proposed unbounded extension was used.

## 6. Prior art, consequences and limits

The nondegenerate-kernel method is classical. Atencia and Martín-Reyes, *The maximal ergodic Hilbert transform with weights*, **Pacific J. Math. 108** (1983), 257--263, [Theorem 1.2 and pp. 258--260](https://msp.org/pjm/1983/108-2/pjm-v108-n2-p01-s.pdf), provide the orbit-weight theorem and separated-block testing background. Here the test starts from the **inverse** symbol, with a complex phase and a large-distance tail, rather than from boundedness of the cotangent action.

David Cruz-Uribe and John-Oliver MacLellan, *Necessary conditions for two-weight inequalities for singular integral operators*, **Studia Math. 261** (2021), 187--205, DOI [10.4064/sm200430-12-3](https://doi.org/10.4064/sm200430-12-3), [author manuscript, Introduction and §3](https://arxiv.org/pdf/2004.08988), place such lower-kernel tests and averaging arguments in classical nondegeneracy theory. Their Euclidean two-measure hypotheses are not imported as a profinite theorem; (12)--(17) prove the needed version directly.

Tuomas Hytönen and Carlos Pérez, *Sharp weighted bounds involving A_infinity*, **Analysis & PDE 6** (2013), 777--818, [Proposition 2.2 and Theorem 2.3](https://msp.org/apde/2013/6-4/apde-v6-n4-p02-s.pdf), supply the uniform reverse Hölder input to (18). No new weight theorem is claimed. The bounded prior-art audit covered nondegenerate singular integrals, weighted ergodic Hilbert transforms, multiplier endpoint jumps and empty-resolvent realizations. It does not establish historical novelty of the resulting specialization.

The exact local delta is removal of the possibility of an **unbounded singleton realization with a useful nonempty resolvent**. PC-449 gave a particular empty-resolvent family; PC-451 and PC-453 classified bounded realizations but explicitly left unbounded closed extensions outside their conclusions. The jump (7) connects those two regimes: one resolvent bound already enforces the same orbit regularity. PC-454's stricter criterion for self-adjoint similarity remains distinct; bounded orbit-`A_2` realizations need not be similar to self-adjoint ones.

The result is identical for a nonarithmetic singleton base. It cannot select rational-prime birth or a critical line. It does not classify which measures outside (2) admit a closure, whether such a closure has other closed extensions, or the spectral types within `C`. It does not cover multiple or growing bases, changed kernels, incomplete fibers, half-density compensation, or domains omitting cylinder functions. In particular one cannot replace the scalar inverse in (6) by a matrix inverse without rechecking its entrywise nondegeneracy.

## 7. Validation and decisive audit

This is an analytic, literature-backed proof, not a Lean verification. Standard-library Python independently inverted the direct finite matrices for `m in {3,4,5,8,13,17}`, `lambda in {i,2,-2,1+0.75i,-0.4+i}`, and both endpoint conventions. All **60** cases agreed with (10) to maximum entry error below `2.1e-15`.

For the same five parameters, Simpson quadrature at 16,384 and 32,768 panels checked (8)--(9) at the ten signed displacements `d=±N,±(N+1),±2N,±3N,±5N`. Here `E_lambda` was enlarged by replacing `integral |r''|` by `8 dist(lambda,[-1,1])^{-3}`, giving `N=4,5,5,6,4`. Across **50** checks the largest remainder divided by its asserted bound was below `0.235`; the smallest projected coefficient divided by the lower bound in (9) exceeded `1.84`. The two quadratures differed by less than `6.4e-13`. For positive `d=N`, finite sums at `M=4096,16384` approached (6) for all five parameters. These are finite sign/normalization diagnostics; they do not prove the all-parameter tail bound, singular-measure exclusion or spectral dichotomy.

The decisive analytic checks are the nonzero endpoint jump, opposite phases for opposite block directions, subgroup averaging **before** assuming a density, holding the test blocks fixed during the refinement limit, and uniform integrability before identifying the limiting probability. A closed unchanged-action singleton realization outside the orbit-`A_2` equivalent class with even one resolvent point would falsify the theorem. Dense real eigenvalues alone are insufficient; the contradiction comes from the forced inverse and the uniform two-block estimates.
