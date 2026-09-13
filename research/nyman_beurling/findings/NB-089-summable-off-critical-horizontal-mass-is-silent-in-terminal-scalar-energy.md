# NB-089 — summable off-critical horizontal mass is silent in terminal scalar energy

**Status:** `EXACT-DERIVED + CONDITIONAL-ACTUAL-NYMAN-SOURCE + INFINITE-BLASCHKE + SUMMABLE-HORIZONTAL-ZERO-MASS + TERMINAL-SCALAR-SILENCE + NEGATIVE-METHOD-BOUNDARY`.

`NB-088` proves that every **fixed finite** off-critical Blaschke divisor is asymptotically invisible to the dyadic scalar sibling-energy channel of `NB-087`. The remaining scalar possibility was therefore genuinely collective: perhaps an infinite Blaschke product could accumulate enough finite-prefix delay to make

\[
\sum_{j\in\mathcal P_{R,2}} |\eta_{j,R}^{(2)}|^2
\]

diverge even though every finite subproduct contributes only `O(R^-1)` total squared distortion.

There is a sharp infinite-product obstruction to that hope. Let `Z_+` be the multiset, with multiplicity, of zeta zeros `rho` with `Re rho>1/2`, and put

\[
\lambda_\rho:=\rho-\frac12,
\qquad
a_\rho:=\Re\lambda_\rho=\Re\rho-\frac12>0.
\]

Assume the total horizontal off-critical mass is finite,

\[
\boxed{
A:=\sum_{\rho\in Z_+} a_\rho<\infty.
}
\tag{1}
\]

Then the **full infinite** off-critical Blaschke factor is still silent in the `NB-087` dyadic scalar channel. Uniformly for terminal windows `j+1\le X\le2j`,

\[
\boxed{
\|J_XD_j\|^2
=1-\frac1X+O_A(j^{-1}),
\qquad
0\le\Lambda_{j,X}(B)\ll_A j^{-1}.
}
\tag{2}
\]

Consequently, uniformly for `j in mathcal P_(R,2)`,

\[
\boxed{
\eta_{j,R}^{(2)}=O_A(R^{-1}),
\qquad
\sum_{j\in\mathcal P_{R,2}}
|\eta_{j,R}^{(2)}|^2
=O_A(R^{-1})\longrightarrow0.
}
\tag{3}
\]

Thus the scalar branching obstruction does not merely fail for finitely many off-critical zeros. It also fails for an infinite off-critical zero set whose **unweighted horizontal displacement from the critical line is summable**. A divergent `NB-087` scalar obstruction can therefore exist only outside (1). In particular, merely proving that the Burnol inner factor is infinite cannot make this channel RH-decisive.

## 1. Summable horizontal mass makes the unnormalized Blaschke product absolutely convergent inside the half-plane

Use the shifted coordinate `z=s-1/2`. For one right-half zero write, as in `NB-088`,

\[
b_\lambda(z)=\frac{z-\lambda}{z+\overline\lambda},
\qquad a=\Re\lambda\in(0,1/2).
\tag{4}
\]

For every compact set `K` in the open right half-plane, `Re z>=delta_K>0`, and

\[
|1-b_\lambda(z)|
=
\frac{2a}{|z+\overline\lambda|}
\le
\frac{2a}{\delta_K}.
\tag{5}
\]

Hence assumption (1) makes

\[
B_*(z):=\prod_{\rho\in Z_+} b_{\lambda_\rho}(z)
\tag{6}
\]

converge normally on compact subsets without needing height-dependent phase normalizers. `B_*` differs from Burnol's inner factor `B` by at most a unimodular constant, which is irrelevant to every norm and delay-energy statement below. This is much stronger than the ordinary half-plane Blaschke convergence required merely to define `B`: the point of (1) is that it controls the product by the **unweighted** horizontal mass.

Let `F` be a finite submultiset of `Z_+`, let `A_F=sum_(rho in F) a_rho`, and divide the raw innovation by the corresponding finite product. We now obtain estimates depending on `A_F` rather than on the number of factors. That is the step which survives `|F| -> infinity`.

## 2. Finite-horizon inverse factors cost only their horizontal mass

Keep the terminal relative horizon

\[
L:=\log2.
\]

`NB-088` writes the raw innovation, after shifting its support origin to `log j`, as

\[
y_j(u)=
\begin{cases}
\sqrt j\,e^{-u/2},&0\le u<\delta_j,\\[1mm]
-j^{-1/2}e^{-u/2},&\delta_j\le u\le L,
\end{cases}
\qquad
\delta_j=\log(1+1/j).
\tag{7}
\]

Its `L^1` mass is small even though its first spike has height `sqrt j`:

\[
\|y_j\|_{L^1(0,L)}
\le
\sqrt j\,\delta_j+Lj^{-1/2}
\ll_L j^{-1/2}.
\tag{8}
\]

For a single factor, finite-horizon division by `b_lambda` is the causal Volterra operator already derived in `NB-088`,

\[
(T_\lambda f)(u)
=f(u)+2a\int_0^u e^{\lambda(u-v)}f(v)\,dv.
\tag{9}
\]

Because `a<1/2` and `0<=v<=u<=L`,

\[
|e^{\lambda(u-v)}|\le e^{L/2}.
\]

Put `C_L=2Le^(L/2)`. Fubini then gives the uniform `L^1` estimate

\[
\boxed{
\|T_\lambda f\|_1
\le
(1+C_La)\|f\|_1.
}
\tag{10}
\]

The increment also satisfies

\[
\boxed{
\|(T_\lambda-I)f\|_\infty
\le
2e^{L/2}a\|f\|_1.
}
\tag{11}
\]

For a finite product `F={lambda_1,...,lambda_m}`, set

\[
f_0=y_j,
\qquad
f_n=T_{\lambda_n}f_{n-1}.
\]

Iterating (10),

\[
\|f_n\|_1
\le
\exp(C_LA_F)\|y_j\|_1.
\tag{12}
\]

Telescoping (11) and using (12),

\[
\begin{aligned}
\|f_m-y_j\|_\infty
&\le
2e^{L/2}
\sum_{n=1}^m
 a_n\|f_{n-1}\|_1\\
&\le
2e^{L/2}A_F e^{C_LA_F}\|y_j\|_1\\
&\ll_{A_F}j^{-1/2}.
\end{aligned}
\tag{13}
\]

The crucial feature is that the constant depends on the **sum of the real parts** `A_F`, not on `m` and not on the imaginary heights of the zeros.

## 3. The terminal norm estimate survives the infinite product

Let `r_{j,F}=f_m-y_j`. For every sub-horizon `0<=L_X=log(X/j)<=L`, equations (8) and (13) imply

\[
\begin{aligned}
\left|
\|f_m\|_{L^2(0,L_X)}^2
-
\|y_j\|_{L^2(0,L_X)}^2
\right|
&\le
2\|r_{j,F}\|_\infty\|y_j\|_1
+L\|r_{j,F}\|_\infty^2\\
&\ll_{A_F}j^{-1}.
\end{aligned}
\tag{14}
\]

Under (1), all finite partial products have `A_F<=A`, so the constant in (14) is uniform along an exhaustion of `Z_+`. The normal convergence from (5)--(6) makes the tail inner products tend to `1` on compact subsets of the half-plane. Equivalently, the partially deflated Hardy vectors converge strongly, up to the harmless fixed unimodular normalization, to the fully deflated innovation `D_j`. Passing to the finite Paley--Wiener horizon in (14) is therefore legitimate.

`NB-088` gives the exact raw terminal norm

\[
\|J_X\widetilde D_j\|^2=1-\frac1X
\tag{15}
\]

and the exact causal decomposition

\[
\|J_XD_j\|^2
=1-\frac1X+\Lambda_{j,X}(B),
\qquad
\Lambda_{j,X}(B)\ge0.
\tag{16}
\]

The infinite-product limit of (14) together with (15)--(16) proves

\[
0\le\Lambda_{j,X}(B)\ll_A j^{-1},
\tag{17}
\]

uniformly throughout `j+1<=X<=2j`. This proves (2).

The strong-limit step is not an inverse-bound assertion for `1/B` on the whole Hardy space. It uses only the actual divisible innovation and the tail of its own convergent inner product. The Volterra estimates are confined to the fixed causal horizon `log 2`.

## 4. Dyadic parent-versus-children distortion remains microscopic

For `j in mathcal P_(R,2)`, `NB-088` gives the exact identity

\[
\eta_{j,R}^{(2)}
=
\frac{
2\Lambda_{j,R/2}(B)
-\Lambda_{2j,R}(B)
-\Lambda_{2j+1,R}(B)
-2/R
}{
2(1-1/R)
+\Lambda_{2j,R}(B)
+\Lambda_{2j+1,R}(B)
}.
\tag{18}
\]

All three indices are comparable to `R`, so (17) makes the three delay energies `O_A(R^-1)`. The denominator in (18) is bounded below by `2(1-1/R)`, and therefore

\[
|\eta_{j,R}^{(2)}|\ll_A R^{-1}
\tag{19}
\]

uniformly over the complete terminal parents. Since

\[
|\mathcal P_{R,2}|=R/4+O(1),
\]

we obtain

\[
\sum_{j\in\mathcal P_{R,2}}
|\eta_{j,R}^{(2)}|^2
\ll_A R^{-1}\to0.
\tag{20}
\]

Thus even a genuinely infinite inner defect can lie asymptotically on the same scalar visible-energy manifold as the RH branch.

## 5. Consequence for the scalar radial strategy

`NB-087` supplies only the one-sided entropy lower bound

\[
\mathfrak S_{R,2}
\ge
\sum_{j\in\mathcal P_{R,2}}|\eta_{j,R}^{(2)}|^2.
\tag{21}
\]

As in `NB-088`, equation (20) does **not** prove bounded radial charge or successful prediction. Sibling contrasts, cross-block correlations, earlier indices and the positive radial floors of `NB-085` remain available carriers of the off-critical inner factor.

What changes is the falsification boundary for the scalar average direction. A strategy trying to force divergence through `eta` must now exclude the entire false-RH-compatible regime

\[
\sum_{\Re\rho>1/2}
\left(\Re\rho-\frac12\right)<\infty.
\tag{22}
\]

That regime includes the finite-zero controls of `NB-088` but is strictly larger: it permits infinitely many off-critical zeros approaching the critical line fast enough in total horizontal displacement. Current zero-density information does not turn `B neq 1` into the negation of (22). Therefore **infinitude of the Blaschke defect is not the collective estimate the scalar route needs**.

A positive continuation of the scalar route must obtain genuinely non-summable horizontal inner mass, or a stronger quantity that forces non-summable parent/child delay imbalance despite (17). Otherwise the line should move to the matrix directions deliberately discarded by `NB-087`.

## 6. Prior-art and adversarial boundary

Burnol's Nyman-space result remains the source of the off-critical inner factor and its zero product; no novelty is claimed for that factorization or for standard half-plane Blaschke convergence. Kondratyuk's Carleman--Nevanlinna analysis (*Computational Methods and Function Theory* 4 (2005), 391--403, DOI `10.1007/BF03321076`) independently singles out the total horizontal displacement `sum |Re rho-1/2|` in a summation formula for `log|zeta|` on the critical line. That is a prior-art boundary for the arithmetic quantity in (1), not for the terminal Nyman consequence (2)--(3). The literature audit did not locate the finite-horizon Volterra estimate by total horizontal mass or its dyadic sibling-energy consequence. No priority claim is made.

The main stress tests are explicit in the theorem. First, (1) is a **conditional** hypothesis and is not asserted for the actual zeta zero set under false RH. The ordinary Blaschke condition has height weights and is substantially weaker. Second, the proof never sums a bound once per zero with a degree-dependent constant; equations (10)--(13) convert the whole finite product to an exponential in the bounded total mass `A_F`, which is what permits the infinite limit. Third, high imaginary parts do not enter the operator norm adversely because only `|e^{lambda(u-v)}|=e^{a(u-v)}` is used on a fixed horizon. Fourth, (20) says only that this compulsory scalar lower bound vanishes; it does not say that the full determinant entropy or Nyman distance vanishes. Finally, divergence of (22) is only a necessary escape from this obstruction, not a sufficient condition for scalar entropy divergence.