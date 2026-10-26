# PF-358 — nearest-neighbor factorization preserves half the constant-fibre correlations without a conditioning bound

**Status:** EXACT-DERIVED + CLASSICAL-CHOLESKY-AND-CAUCHY-METHOD + SHARP-FINITE-MODEL-MULTIPLICITY + ACTUAL-PANT-COMPARISON-OPEN.

PF-357 retains all module-count many constant/high correlations when a diagonal-relative network condition number is controlled. For a **tridiagonal** positive spatial matrix, a different argument retains at least half the correlations without any condition-number, grounding, conductance-contrast, or section-size bound. The price is an explicit comparison between high-mode approximation and transition-mode approximation. Complete sufficiently narrow transition bands satisfy this comparison on comparable large cuff periods.

The fraction one half is asymptotically optimal for this matrix class: nearly singular paired modules can concentrate correlation into one direction per pair, even after arbitrarily weak positive links make the path connected. This is a finite Cauchy corridor-model result. It supplies neither the actual pant comparison nor compatible infinite-section witnesses.

## 1. Exact finite statement

Let `K>0` be a real symmetric tridiagonal `d by d` matrix, `d>=1`. Its off-diagonal entries may have either sign or vanish. Fix `a>0`. On each module `i`, retain `(i,a)` and a finite high-node set `Y_i`, and eliminate a finite transition-node set `T_i`. Nodes are positive and distinct within each module; `a`, `T_i`, and `Y_i` are disjoint there. Nodes may coincide across modules. Empty sets are permitted.

As in PF-355/PF-357, set

\[
M_{(i,x),(j,y)}=\frac{K_{ij}}{x+y},\qquad
M^{/T}=\begin{pmatrix}A&C\\ C^{\mathsf T}&B\end{pmatrix},
\qquad Z=A^{-1/2}CB^{-1/2},
\tag{1}
\]

with retained order `F_a={(i,a):1<=i<=d}`, then `Y`. The full Gram form is strictly positive: vanishing energy forces every finite exponential sum on each module to vanish, and hence all coefficients to vanish. Shorting is exact positive quadratic minimization. For empty `Y`, use the zero map. List singular values decreasingly, padded with zeros to length `d`. Define

\[
Q_i=\prod_{t\in T_i}\left(\frac{a-t}{a+t}\right)^2,
\qquad
P_i=\prod_{b\in Y_i}\left(\frac{a-b}{a+b}\right)^2,
\qquad Q_{d+1}=1,
\qquad r=\min_{1\le i\le d}Q_iQ_{i+1}>0.
\tag{2}
\]

Empty products equal one; set `T_(d+1)=empty` for the endpoint convention. For every nonempty index set `I` containing no consecutive integers,

\[
\boxed{\quad
1-\sigma_{|I|}(Z)^2
\le \frac{2\max_{i\in I}(Q_iP_i)}{r}.
\quad}
\tag{3}
\]

In particular, with `m=ceil(d/2)` and

\[
\varepsilon=\frac{2\max_i(Q_iP_i)}{\min_i(Q_iQ_{i+1})},
\]

one has `1-sigma_m(Z)^2<=epsilon`. If `epsilon<1`, at least `m` singular values are at least `sqrt(1-epsilon)`. A bound at least one is valid but uninformative. The factor two is not claimed optimal; the asymptotic fraction of correlations in the uniform tridiagonal class is sharp in Section 4.

## 2. Local factorization controls the low residual before normalization

Write `D=diag(K_ii)`. A tridiagonal positive matrix has a lower bidiagonal Cholesky factor `K=GG^T`. This follows directly from the recurrence

\[
G_{11}=\sqrt{K_{11}},\qquad
G_{i+1,i}=K_{i+1,i}/G_{ii},\qquad
G_{i+1,i+1}=\sqrt{K_{i+1,i+1}-G_{i+1,i}^2};
\tag{4}
\]

the Schur pivots are positive. Let `w_j` be column `j` of `G`. Its support is contained in `{j,j+1}`, or `{d}` at the last column.

For prescribed constant coefficients `u`, and arbitrary transition coefficients, put

\[
v_i(t)=u_i e^{-at}+\sum_{x\in T_i}z_{i,x}e^{-xt}.
\]

The energy is `integral v^T K v = sum_j ||w_j^T v||_2^2` on `(0,infinity)`. Each summand has constant coefficient `w_j^T u` and transition exponents contained in `T_j union T_(j+1)`. Relax its transition coefficients independently of all other summands. The scalar Cauchy distance identity gives

\[
\inf_{(c_x)}\left\|s e^{-at}+\sum_{x\in U}c_xe^{-xt}\right\|_2^2
=\frac{s^2}{2a}\prod_{x\in U}\left(\frac{a-x}{a+x}\right)^2.
\tag{5}
\]

For completeness, (5) follows by iterating

\[
\frac1{x+y}-\frac{2t}{(x+t)(y+t)}
=\frac1{x+y}\frac{x-t}{x+t}\frac{y-t}{y+t},
\]

the one-node Schur identity. Duplicate exponents in a union count only once. Since every factor lies strictly between zero and one, the product for `T_j union T_(j+1)` is at least `Q_j Q_(j+1)`. Including an exponent whose coefficient in `w_j` is zero only enlarges the relaxed space and remains a valid lower bound.

Summing (5), then minimizing the actual shared transition coefficients, therefore proves

\[
\boxed{A\ \ge\ \frac{r}{2a}K.}
\tag{6}
\]

The independent minimizations are a lower bound, not an asserted simultaneous optimizer. This is where nearest-neighbor factorization enters; a general dense Cholesky column would pay transition products from arbitrarily many modules.

Now let `J=diag((-1)^i)`. Tridiagonality gives `K+JKJ=2D`, so `K<=2D`. Comparing the full exponential Gram energies and minimizing over **both** transition and high coefficients yields

\[
E:=A-CB^{-1}C^{\mathsf T}
=M^{/(T\cup Y)}
\ \le\ \frac1a\operatorname{diag}(K_{ii}Q_iP_i).
\tag{7}
\]

Here the reference diagonal metric separates by module, so (5) applies to `T_i union Y_i`. In (6) high coefficients are fixed to zero; in (7) they are minimized. No mixed-block estimate or inverse bound on the transition matrix is used.

If `u` is supported on a nonconsecutive set `I`, then `u^TKu=u^TDu`. Equations (6)–(7) give throughout this `|I|`-dimensional subspace

\[
\frac{u^{\mathsf T}Eu}{u^{\mathsf T}Au}
\le \frac{2\max_{i\in I}(Q_iP_i)}r.
\tag{8}
\]

The increasing generalized eigenvalues of `(E,A)` are `1-sigma_j(Z)^2`, because `A^(-1/2)EA^(-1/2)=I-ZZ^T`. The generalized min-max principle proves (3). Taking odd indices gives `|I|=ceil(d/2)`. These coordinate vectors need not be orthogonal in the shorted metric; min-max uses the dimension of the subspace, not a claim of orthogonality.

## 3. Complete unequal physical bands: a condition independent of the spatial matrix

Use `a=1`, `x=cosh(pi xi)` and `xi=2pi k/L_i`. Choose fixed

\[
0<\kappa_-<\kappa_+<\Omega,
\]

eliminate exactly all positive cosine lattice modes in `(kappa_-,kappa_+)`, and retain all modes in `[kappa_+,Omega]` as `Y_i`. Set

\[
\delta=-\frac2\pi\int_{\kappa_-}^{\kappa_+}
\log\tanh(\pi\xi/2)\,d\xi>0,
\qquad
\gamma=-\frac2\pi\int_{\kappa_+}^{\Omega}
\log\tanh(\pi\xi/2)\,d\xi>0.
\tag{9}
\]

Since `(cosh(pi xi)-1)/(cosh(pi xi)+1)=tanh^2(pi xi/2)`, bounded-variation Riemann sums give

\[
Q_i=\exp(-\delta L_i+O(1)),\qquad
P_i=\exp(-\gamma L_i+O(1)).
\tag{10}
\]

The constants depend only on the fixed band endpoints, uniformly over modules, periods tending to infinity and their number. Endpoint rounding changes only boundedly many bounded summands.

For `L_min=min_i L_i` and `L_max=max_i L_i`, (2)–(3) imply

\[
1-\sigma_{\lceil d/2\rceil}(Z)^2
\le C\exp\big(2\delta L_{\max}-(\delta+\gamma)L_{\min}\big).
\tag{11}
\]

Thus, along any sequence of these finite models,

\[
\boxed{\quad
(\delta+\gamma)L_{\min}-2\delta L_{\max}\longrightarrow+\infty
\quad\Longrightarrow\quad
\sigma_{\lceil d/2\rceil}(Z)\longrightarrow1.
\quad}
\tag{12}
\]

The section size and every positive tridiagonal `K` may vary arbitrarily. If `L_max<=R L_min` for fixed `R>=1`, it suffices that `gamma>(2R-1)delta`. Such fixed bands exist: hold `kappa_->0` and `Omega>kappa_-` fixed and let `kappa_+` approach `kappa_-` from above. Then `delta -> 0` while `gamma` tends to a positive number. Choose one sufficiently small **positive** width and keep it fixed as periods grow.

This differs materially from PF-357: arbitrarily small grounding and exponentially bad conductance contrast cannot defeat the fraction in (12). The gain is obtained by retaining only half the spatial directions and paying a transition approximation cost explicitly. No quantitative frequency separation is required, and coincident transition nodes only improve the lower estimate (6). Positive Fourier normalization is a diagonal congruence and leaves the canonical correlations unchanged. Sines decouple in this even-weight cosine model.

The sufficient band condition is not a necessary threshold. If it fails, (11) does not decide the angle. Additional transition nodes are covered by (3) with their actual products, but not by the particular rate (10).

## 4. Why no larger universal fraction follows for tridiagonal matrices

Partition `d` modules into pairs and, if needed, one singleton. On each pair use

\[
K_\tau^{\rm pair}=\begin{pmatrix}1+\tau&-1\\-1&1+\tau\end{pmatrix},
\qquad \tau>0,
\tag{13}
\]

and put scalar `1` on a singleton. Their direct sum is positive and tridiagonal. Give all modules complete unequal physical bands with pairwise irrational period ratios, comparable periods tending to infinity, and endpoints satisfying (12).

For each **fixed finite pair**, PF-356 applies with `v=(1,-1)`: all nonconstant scalar nodes on the two modules are distinct. As `tau -> 0`, its first squared correlation tends to `1-P_1P_2`, while its second tends to zero. The reason is that the limiting transition and high scalar Gram blocks remain invertible, the mixed block has rank one, and the low normalization grows only as `O(tau^(-1/2))`; the unnormalized mixed-block remainder is `O(tau)`, giving an `O(sqrt(tau))` second correlation. The exact complete-fibre determinant then identifies the surviving value. A singleton has squared correlation `1-P_i` by scalar shorting.

Along growing finite models, choose positive `tau` only after each model's complete node sets are fixed, small enough that all extra paired correlations are at most `1/n`. Products `P_i` tend to zero by (10). Direct sums therefore have exactly `ceil(d/2)` correlations tending uniformly to one, with all the others tending uniformly to zero. There is no asserted uniform quantitative choice of `tau` in terms of the lattice spacing.

Connected paths give the same sharpness control. For each fixed model, add positive conductances between neighboring pairs, i.e. positive multiples of `(e_i-e_(i+1))(e_i-e_(i+1))^T`. This preserves positivity and tridiagonality and makes all neighboring links nonzero. At a fixed positive `tau`, the finite Gram, inverse and canonical-correlation maps are continuous. Choose these finitely many conductances sufficiently small that every singular value changes by at most `1/n`. All conductances remain positive. Thus connectedness alone does not improve the uniform asymptotic fraction.

This control establishes optimality within the stated finite matrix class, not realizability by actual prime-flute conductances. Retaining additional nonconstant low modes can increase the singular count; the upper sharpness example concerns only the constant-fibre/high-strip angle.

## 5. Consequences and boundaries

- **Locality now has a proved finite-model effect.** PF-356's dense growing-dimensional rank-one metric cannot be used to suppress all but one correlation in a tridiagonal network satisfying (12). It can suppress one direction per pair, showing exactly why a full-module count still needs more information.
- **Constants stay retained.** All module constants are low variables. Eliminating them, imposing a mean-zero split, or changing the shorted form is a different problem.
- **The comparison uses the whole transition block.** It does not freeze neighboring transitions or import a local Dirichlet witness after further relaxation. Factorwise relaxation in (6) already allows more freedom than the actual coupled transition minimization.
- **Finite spatial sparsity is not spatial localization after completion.** Low coefficient vectors can be chosen in a parity subspace, but their energy-normalized representatives and minimizing transition extensions need not be localized. Attaching reservoirs or passing to an infinite section requires a compatible comparison.
- **No actual-PDE result follows.** The true pant/seam form still needs two-sided comparison at the much smaller shorted residual scale. Tridiagonal adjacency of the actual geometric problem does not identify its frequency kernel with (1). Prime and nonprime periods obey the same model theorem.
- **No global ideal or RH claim.** Even growing finite multiplicity does not prove noncompactness of a single completed infinite operator without identifying compatible compressions. No scattering, zeta-zero, or RH consequence is established.

## 6. Prior art and verification

Bidiagonal Cholesky factorization is classical; see Charles F. Van Loan, *Introduction to Scientific Computing: A Matrix-Vector Approach Using MATLAB*, second edition, Section 7.3.2, p. 258 ([Cornell-hosted chapter](https://www.cs.cornell.edu/courses/cs4210/2014fa/CVLBook/chap7.pdf)). Formula (4) verifies precisely the locality used here. Positive variational shorting and the scalar Cauchy/Müntz distance product are the classical sources in S31: Li–Mathias, *Extremal Characterizations of the Schur Complement and Resulting Inequalities*, and Almira, [*Müntz Type Theorems I*](https://www.maths.tcd.ie/EMIS/journals/SAT/papers/10/10.pdf), Section 2.1, pp. 154–155. The sign-conjugation identity and independent-set min-max argument are proved directly above.

Structure-directed literature searches covered tridiagonal Cholesky, bipartite normalized spectra, positive Schur minimization, Cauchy/Müntz residual products and canonical correlations of structured matrices. No novelty is claimed for those ingredients or for a new general angle theorem. The derived addition is the conductance-independent bound (3), its complete-band consequence (12), and the matching paired-network multiplicity control. None supplies the missing surface comparison.

Supplementary standard-library Python `Fraction` checks used `d=1,...,5`, diagonal matrices, path Laplacians plus grounding `10^(-24)`, and grounded paths with conductances cycling through `10^(-8),1,10^8`. Transition sets were empty, the shared node `3`, or one unequal node `3+i/11` (zero-based `i`). Each high set contained `b+i/q` for `(b,q)=(5,13),(7,17),(9,19),(11,23),(13,29),(15,31)`. All 45 cases exactly verified positivity of the elimination pivots, (6), (7), and positivity of the parity compression of `epsilon A-E`. These check degenerating metrics, shared/unequal nodes, normalization and the min-max certificate. They are finite algebra checks, not numerical evidence for the actual surface or a substitute for the arbitrary finite proof. Scratch remains outside Git; no Lean verification or independent adversarial approval is claimed.
