# PF-357 — network conditioning bounds every constant-fibre correlation defect

**Status:** EXACT-DERIVED + CLASSICAL-SHORTING-AND-MINMAX + CONDITIONAL-MODEL-MULTIPLICITY + ACTUAL-PANT-COMPARISON-OPEN.

PF-356 permits the retained-constant angle of an unequal-lattice corridor network to concentrate in one direction when its positive network metric degenerates. The amount of degeneration matters. Every squared canonical-correlation defect is within a factor equal to a diagonal-relative network condition number of an explicit **per-module scalar product**, independently of the number, mismatch, or conditioning of the eliminated transition modes.

For complete bounded high strips these scalar products decay exponentially in the cuff periods. Hence a network condition number subexponential in the minimum period forces **all module-count many correlations** to approach one. Grounded paths satisfy an explicit sufficient condition involving their length and conductance contrast. This is a finite corridor-model theorem; it does not establish that condition, a residual-scale form comparison, or an infinite-operator conclusion for the prime flute.

## 1. Finite spectral comparison

Let `K>0` be a real symmetric `d by d` matrix. Choose a positive diagonal matrix `D=diag(d_i)` and constants

\[
0<\alpha\le\beta,\qquad \alpha D\le K\le\beta D,
\qquad \kappa_D=\beta/\alpha.
\tag{1}
\]

The inequalities are in quadratic-form order. Fix a node `a>0`. On module `i`, retain its constant-fibre label `(i,a)`, a finite high set `Y_i`, and a finite eliminated set `T_i`. All nodes are positive, distinct **within each module**, and `a`, `Y_i`, `T_i` are disjoint there. Nodes on different modules may coincide; no shared nonconstant node is required. Empty sets are allowed.

On these labels use PF-355's exact corridor coefficient form

\[
(M_K)_{(i,x),(j,y)}=\frac{K_{ij}}{x+y}.
\tag{2}
\]

Write `F_a={(i,a):1<=i<=d}`, `Y=union_i ({i} times Y_i)` and similarly `T`. Short exactly `T` and define

\[
S_K=M_K^{/T}=\begin{pmatrix}A&C\\ C^{\mathsf T}&B\end{pmatrix},
\qquad Z=A^{-1/2}CB^{-1/2},
\tag{3}
\]

with retained order `F_a,Y`. For empty `Y`, interpret `Z` as the zero map. List its singular values in decreasing order, padding with zeros to length `d` if `|Y|<d`. Put

\[
P_i=\prod_{b\in Y_i}\left(\frac{b-a}{b+a}\right)^2,
\qquad P_{(1)}\le\cdots\le P_{(d)},
\tag{4}
\]

where an empty product is one. Then

\[
\boxed{\quad
\kappa_D^{-1}P_{(j)}
\le 1-\sigma_j(Z)^2
\le\kappa_D P_{(j)},\qquad 1\le j\le d.
\quad}
\tag{5}
\]

In particular, for `0<rho<1`,

\[
\#\{j:\sigma_j(Z)\ge\rho\}
\ \ge\ \#\{i:\kappa_D P_i\le1-\rho^2\}.
\tag{6}
\]

The condition number belongs to the `d by d` spatial matrix relative to a **diagonal** metric. It is not the condition number of the large sampled Gram matrix or of its transition block. Taking `D=I` always works; a better diagonal scaling can improve the bound. Arbitrary nondiagonal comparison metrics would lose the scalar decomposition used below.

## 2. Proof: compare the two residual minimizations

For coefficient vectors `z` define `v_i(t)=sum_x z_(i,x) exp(-xt)`. Then

\[
z^{\mathsf T}M_Kz=\int_0^\infty v(t)^{\mathsf T}Kv(t)\,dt,
\qquad \alpha M_D\le M_K\le\beta M_D.
\tag{7}
\]

These Gram matrices are strictly positive: a zero integral forces every finite exponential sum on each module to vanish. Distinctness within each module then forces every coefficient to be zero.

For any positive block matrix, its Schur quadratic form is the minimum over the eliminated coefficients. Therefore (7) survives both shorting operations needed here:

\[
\alpha A_D\le A\le\beta A_D,
\qquad
\alpha E_D\le E\le\beta E_D,
\tag{8}
\]

where `A_D` is the `F_a` principal block after eliminating `T` from `M_D`, and

\[
E=A-CB^{-1}C^{\mathsf T}=M_K^{/(T\cup Y)},
\qquad E_D=M_D^{/(T\cup Y)}.
\tag{9}
\]

For `A`, the high coefficients are fixed to zero; for `E`, they are minimized as well. Keeping this distinction is essential. Successive shorting equals simultaneous minimization, so (9) is exact.

The diagonal spatial metric separates the modules. The one-node Cauchy identity

\[
\frac1{x+y}-\frac{2t}{(x+t)(y+t)}
=\frac1{x+y}\frac{x-t}{x+t}\frac{y-t}{y+t}
\tag{10}
\]

and iteration give

\[
(A_D)_{ii}=\frac{d_i}{2a}
\prod_{t\in T_i}\left(\frac{a-t}{a+t}\right)^2>0,
\qquad E_D=A_D\operatorname{diag}(P_i).
\tag{11}
\]

Thus all transition products cancel from the scalar generalized eigenvalues. For every nonzero real vector `u`, (8) gives

\[
\kappa_D^{-1}\frac{u^{\mathsf T}E_Du}{u^{\mathsf T}A_Du}
\le\frac{u^{\mathsf T}Eu}{u^{\mathsf T}Au}
\le\kappa_D\frac{u^{\mathsf T}E_Du}{u^{\mathsf T}A_Du}.
\tag{12}
\]

Apply the generalized Courant--Fischer principle in the same coefficient space. The increasing eigenvalues of the reference quotient are `P_(j)`. Those of the middle quotient are the increasing eigenvalues of

\[
A^{-1/2}EA^{-1/2}=I_d-ZZ^{\mathsf T},
\]

namely `1-sigma_j(Z)^2` with the stated decreasing singular-value order. This proves (5) and (6). No comparison of the mixed blocks alone, no inverse estimate for the transition matrix, and no small perturbation assumption is needed.

If `K=D` then `kappa_D=1` and (5) is equality for every `j`. The exact decoupled identity is classical Cauchy Gram algebra; (5) is its quadratic-form comparison consequence, not a new general principal-angle theorem.

## 3. Complete physical high strips give an exponential budget

Use the cosine realization `a=1`, `b=cosh(pi xi)` and physical frequencies `xi=2pi k/L_i`. Fix

\[
0<\kappa_-<\kappa_+<\Omega.
\]

On each module eliminate every transition frequency in `(kappa_-,kappa_+)`, and take `Y_i` to consist of exactly the positive cosine modes in `[kappa_+,Omega]`. Arbitrary additional transition nodes outside the retained sets are also allowed. Since

\[
\frac{\cosh(\pi\xi)-1}{\cosh(\pi\xi)+1}
=\tanh^2(\pi\xi/2),
\]

we obtain

\[
\log P_i
=4\sum_{\kappa_+\le 2\pi k/L_i\le\Omega}
\log\tanh\frac{\pi^2k}{L_i}
=-\gamma L_i+O(1),
\tag{13}
\]

where

\[
\gamma=-\frac2\pi\int_{\kappa_+}^{\Omega}
\log\tanh(\pi\xi/2)\,d\xi>0.
\tag{14}
\]

The `O(1)` is uniform in `i` and in the module count for fixed strip endpoints: the summand as a function of `xi` is smooth with bounded variation on this closed interval, so the lattice Riemann-sum error is bounded independently of `L_i` as the periods grow. Endpoint rounding changes at most two bounded terms. Thus constants depending only on the strip give

\[
c_*e^{-\gamma L_i}\le P_i\le C_*e^{-\gamma L_i}.
\tag{15}
\]

Let `L_min=min_i L_i` along any sequence of finite networks. From (5),

\[
1-\sigma_d(Z)^2\le C_*\kappa_D e^{-\gamma L_{\min}}.
\tag{16}
\]

Consequently `log(kappa_D)-gamma L_min -> -infinity` forces every one of the `d` correlations to tend to one, uniformly even when `d` grows. Every module then has high modes, so the padding convention causes no difficulty. Unequal or rationally independent cuff periods cause no loss, and transition cardinality does not enter this criterion.

Conversely, if `d>=2` and `sigma_2(Z)<=epsilon<1`, then

\[
\kappa_D\ge\frac{1-\epsilon^2}{P_{(2)}}
\ge C_*^{-1}(1-\epsilon^2)e^{\gamma L_{\min}}.
\tag{17}
\]

Thus PF-356's concentration to one direction on growing complete high strips requires at least exponential deterioration of **every valid diagonal-relative comparison ratio**. This is a necessary condition, not a converse or a sharp transition law. The condition may still be met by that countercontrol's freely chosen small parameter.

## 4. A concrete growing nearest-neighbor regime

For a path with `d` internal vertices and Dirichlet endpoint values `u_0=u_(d+1)=0`, let

\[
u^{\mathsf T}Ku=\sum_{i=0}^d c_i|u_{i+1}-u_i|^2,
\qquad 0<c_{\min}\le c_i\le c_{\max}.
\tag{18}
\]

Comparison with the unit-conductance Dirichlet path `K_0` gives
`c_min K_0 <= K <= c_max K_0`. The sine vectors have eigenvalues
`4 sin^2(j pi/(2(d+1)))`, `1<=j<=d`, for `K_0`; substitution in the tridiagonal recurrence verifies this formula. Hence (1) with `D=I` can be chosen so that

\[
\kappa_I\le\frac{c_{\max}}{c_{\min}}
\csc^2\frac\pi{2(d+1)}
\le\frac{c_{\max}}{c_{\min}}(d+1)^2.
\tag{19}
\]

Together with (16), this proves the sufficient condition

\[
\boxed{\quad
\frac{c_{\max}}{c_{\min}}(d+1)^2
 e^{-\gamma L_{\min}}\longrightarrow0
\quad\Longrightarrow\quad \sigma_d(Z)\longrightarrow1.
\quad}
\tag{20}
\]

For bounded conductance contrast, `log d=o(L_min)` is one admissible growing-module regime. This supplies a multiplicity theorem with unequal complete lattices for a specified class of local networks. It does **not** prove that locality alone is sufficient: unbounded conductance contrast or vanishing effective grounding can make (20) fail. In particular, Dirichlet grounding at the two ends has not been identified with the reservoir response of the infinite flute.

## 5. Evidence boundary and controls

- **The retained constants are essential to this proof.** All `d` labels in `F_a` remain low variables. A mean-zero split or further elimination of these constants is outside the theorem.
- **Missing high coverage is visible.** A module with empty `Y_i` has `P_i=1`; (5) gives no small defect there. A large total high-mode count on other modules does not replace the per-module products.
- **No unconditioned multiplicity claim.** With no bound on `kappa_D`, (16) can be vacuous. PF-356 remains a valid countercontrol; (17) prices the extra degeneration needed rather than ruling it out.
- **Enlargement and further shorting differ.** Adding retained low/high variables preserves these singular-value lower bounds by isometric compression in the same shorted metric, as in PF-353. Eliminating more retained variables, changing the form, or attaching reservoirs requires a new comparison.
- **The model is universal.** The proof uses positive spatial coupling and the Cauchy kernel, and works on nonprime periods. Sampling prime-cuff lengths does not establish the actual pant/seam form sandwich at the residual scale. PF-346's warning about small raw errors remains in force.
- **Finite multiplicity is not an infinite-operator theorem.** The vectors may depend on the whole finite network, and the finite Dirichlet models need not be compressions of one completed infinite angle. No compactness/noncompactness, Schatten class, scattering, zeta-zero or RH consequence follows here.

The changed research test is quantitative: compare spatial conditioning with the explicit rate (14), rather than infer multiplicity from positivity or infer its failure from a freely degenerate metric. For the actual surface the outstanding step remains a justified network/pant comparison and compatible finite-section passage; (20) does not supply either.

## 6. Prior art and validation

Positive Schur minimization and monotonicity are classical; see Li and Mathias, [*Extremal Characterizations of the Schur Complement and Resulting Inequalities*](https://doi.org/10.1137/S0036144599337290), SIAM Review 42 (2000), 233–246, and S24. Norm-equivalent inner-product angle bounds are also classical: Lin and Sinnamon, [*The Generalized Wielandt Inequality in Inner Product Spaces*](https://arxiv.org/abs/1201.6294), Theorems 2.4 and 2.6 (S25). Equation (12) uses the elementary residual/min-max route directly.

The scalar product (11) is the Cauchy Gram-distance identity appearing in the classical Müntz proof; Almira, [*Müntz Type Theorems I*](https://www.maths.tcd.ie/EMIS/journals/SAT/papers/10/10.pdf), Surveys in Approximation Theory 3 (2007), 152–194, Section 2.1, pp. 154–155. The change of variables `x=exp(-t)` sends `exp(-a t)` isometrically to `x^(a-1/2)` in `L^2(0,1)`, recovering the same factors. No infinite Müntz density theorem is imported.

Structure-directed searches covered Schur extremal inequalities, principal angles under equivalent metrics, Cauchy residual products and Müntz Gram distances. No historical novelty is claimed for the component methods or their general combination. The derived addition to PF-355/PF-356 is the **ordered, modulewise defect comparison uniform in transition elimination**, its complete-lattice rate, and the resulting explicit growing-path multiplicity regime. It resolves the conditioned finite-model question, not the actual surface question.

Supplementary standard-library Python `Fraction` checks covered 36 cases: `d=1,2,3,4`; diagonal, weighted Dirichlet-path, and rank-one-plus-positive-grounding network matrices; and empty, one-node, or two-node transition sets per module. With zero-based `i`, transition nodes were `2+i/7` and, when present, `3+i/11`; high nodes were `5+i/3,7+i/13`, with a separate one-node case omitting the final module's high set. Diagonal scaling used entries `((i+2)/2)^2`. The path conductances were `1+(i mod 3)/2`; rank-one vectors were `(-1)^i(i+1)/d`, with grounding `1/7` or `10^(-6)`.

All cases had strictly positive Gram pivots and exactly satisfied both elimination orders, (11), the two Loewner sandwiches (8), and the extreme generalized-defect bounds. Diagonal networks reproduced equality of the scalar defect products. These exact finite checks audit algebra and boundary conventions; the full ordered statement follows from (12) and min-max. Scratch computation is not part of the repository. No Lean verification or independent adversarial approval is claimed.
