# PF-355 — one complete constant fibre retains corridor correlation on unequal lattices

**Status:** EXACT-DERIVED + CLASSICAL-SCHUR-CAUCHY-METHOD + UNEQUAL-LATTICE-MODEL-OBSTRUCTION + ACTUAL-PANT-COMPARISON-OPEN.

PF-354 excludes the two complete common-frequency fibres used in PF-353 on actual prime cuffs. That arithmetic obstruction does **not** permit the coupled corridor model's whole low/high angle to vanish: one complete fibre is enough. Every cuff has a constant mode, and its correlation with any one retained high mode, after arbitrary transition elimination, is exactly

\[
\boxed{\rho(\xi)=
\frac{2\sqrt{\cosh(\pi\xi)}}{1+\cosh(\pi\xi)}.}
\tag{1}
\]

Here the low vector may use constants on **all** modules in the finite network. The high mode occurs on just one module; no other module needs to contain its frequency. All normalizations use the same transition-shorted form. A determinant identity also forces the model angle norm towards one when the number of bounded high modes per module diverges.

These statements apply to the precise Gram-valued network model of PF-351--PF-353, including when it is sampled on the actual unequal prime-cuff Fourier lattices. They do not identify that model with the full pant/seam form, prove localization of the low witness, or establish a singular-value multiplicity bound for one infinite surface operator.

## 1. Finite model and one-fibre identity

Let `K` be any real symmetric strictly positive `d by d` matrix. On each module choose a finite set of distinct positive nodes. Different modules may share nodes. For labels `(i,x)` put

\[
M_{(i,x),(j,y)}=\frac{K_{ij}}{x+y}.
\tag{2}
\]

This is strictly positive: its quadratic form is
`integral_0^infinity v(t)^T K v(t) dt`, where
`v_i(t)=sum_x z_(i,x) exp(-xt)`. Vanishing forces each exponential sum to vanish, hence every coefficient to be zero.

Fix `a>0`. Retain the complete fibre

\[
F_a=\{(i,a):1\le i\le d\},
\]

and a nonempty set `Y={(i_j,b_j):1<=j<=r}` with every `b_j != a`. Eliminate any remaining finite set `T`. Transition nodes can be mismatched across modules and can coincide with a retained node on a different module. Since `F_a` is complete, no node in `T` equals `a`. Other retained labels can be omitted from this principal-block calculation without eliminating them.

Write the principal blocks of `S=M^{/T}` as

\[
S_{F_a\cup Y,F_a\cup Y}
=\begin{pmatrix}A&C\\C^{\mathsf T}&B\end{pmatrix}>0,
\qquad
F=\operatorname{diag}_{1\le j\le r}
\frac{b_j-a}{b_j+a}.
\]

Then

\[
\boxed{B-C^{\mathsf T}A^{-1}C=FBF.}
\tag{3}
\]

In particular, the matrix `B` on the right is **already transition-shorted**, not the original high block. Equation (3) does not require a well-conditioned `K`, agreement of the transition sets, a common retained high frequency, or a bound on their cardinalities.

### Proof by reversing the elimination order

Before eliminating `T`, the complete fibre block is `K/(2a)`. Direct multiplication gives, for any remaining labels,

\[
\begin{aligned}
(M^{/F_a})_{(i,x),(j,y)}
&=K_{ij}\left(\frac1{x+y}
-\frac{2a}{(x+a)(y+a)}\right)\\
&=\frac{x-a}{x+a}\,M_{(i,x),(j,y)}\,
\frac{y-a}{y+a}.
\end{aligned}
\tag{4}
\]

Thus eliminating the **whole** fibre gives a scalar diagonal congruence on every remaining label, despite intermodule coupling. The diagonal factors on `T` are nonzero. Consequently shorting `T` from (4) cancels those factors against the inverse transition block and leaves `FBF` on `Y`.

Alternatively, eliminate `T` first and then `F_a`. The result is the left side of (3). The two elimination orders agree: both minimize the same strictly positive quadratic form over all coordinates in `T union F_a`. This proves (3), including empty `T`. It also explains why eliminating only one module's low mode would not suffice.

## 2. Exact correlation and determinant consequences

Let `c_j` denote column `j` of `C`. Taking a diagonal entry of (3) yields

\[
\boxed{
\frac{c_j^{\mathsf T}A^{-1}c_j}{B_{jj}}
=1-\left(\frac{b_j-a}{b_j+a}\right)^2
=\frac{4ab_j}{(a+b_j)^2}.}
\tag{5}
\]

The square root is the maximum absolute correlation between the one high coordinate `j` and an arbitrary vector in `F_a`, in the `S` inner product. A maximizing low vector is proportional to `A^{-1}c_j`. It need not be localized on module `i_j`, and its coefficients need not be uniformly bounded in the unshorted coordinate metric.

For the entire selected block set

\[
Z=A^{-1/2}CB^{-1/2},\qquad p=\min(d,r).
\]

Strict positivity gives `||Z||<1`. Taking determinants in (3) gives

\[
\boxed{
\prod_{k=1}^{p}(1-\sigma_k(Z)^2)
=\det(I_r-Z^{\mathsf T}Z)
=\prod_{j=1}^{r}\left(\frac{b_j-a}{b_j+a}\right)^2.}
\tag{6}
\]

Zero singular values are included where needed. Hence

\[
\boxed{
\|Z\|^2\ge
1-\left[\prod_{j=1}^{r}
\left(\frac{b_j-a}{b_j+a}\right)^2\right]^{1/p}.}
\tag{7}
\]

Indeed each of the `p` factors on the left of (6) is at least `1-||Z||^2`. When `a<b_j<=R`, put `q=(R-a)/(R+a)<1`. Equation (7) implies `||Z||^2>=1-q^(2r/p)`. Thus `r/d -> infinity` forces `||Z|| -> 1`, irrespective of transition mismatch or degeneration of the positive matrix `K`.

If `F_a` is contained in a larger retained low space and `Y` in a larger retained high space, their normalized angle is an isometric compression of the full normalized angle. For example the low inclusion is `S_LL^(1/2) J_a A^(-1/2)`. The norm lower bounds therefore transfer to these **enlarged retained spaces**. Further shorting retained variables is a different operation.

Neither (5) nor (6) supplies `d` uniformly large singular values. The high test vectors are not orthogonal in the shorted `B` metric, and a determinant deficit can concentrate in few singular directions. PF-353's stronger full-fibre multiplicity statement used its additional common-frequency hypothesis.

## 3. Unequal physical lattices, including the prime-cuff periods

PF-346's normalized cosine kernel is

\[
k_x(t)=\frac{\cos(\pi^{-1}\operatorname{arcosh}(x)t)}
{\sqrt{\pi(x+1)}},\qquad
\langle k_x,k_y\rangle_{L^2(\operatorname{sech}t\,dt)}
=\frac1{x+y},\qquad x,y\ge1.
\tag{8}
\]

On module `i`, sample `x=cosh(pi xi)` at the nonnegative physical cosine frequencies `xi=2pi k/L_i`. There is exactly one constant node `a=1` per module. Its weighted norm is positive; it has no connection with the excluded prime endpoint `p=2`. Ordinary physical Fourier normalization changes (2) by an invertible diagonal congruence and does not change the canonical correlations.

Fix `0<kappa_-<kappa_+`. Eliminate every sampled transition frequency in `(kappa_-,kappa_+)`, on every module, retaining the constants as low variables. For any module choose

\[
\xi_i=\frac{2\pi}{L_i}
\left\lceil\frac{\kappa_+L_i}{2\pi}\right\rceil
\in[\kappa_+,\kappa_++2\pi/L_i).
\tag{9}
\]

This is an actual high lattice mode. Substitution of `a=1`, `b=cosh(pi xi_i)` in (5) proves (1) for that high coordinate and the complete constant low space. Along large periods it converges to the positive number `rho(kappa_+)`. Even exact rational independence of every pair of periods causes no difficulty: no nonzero frequency is required on two modules.

There is a stronger whole-model norm consequence. Fix a high strip `[kappa_+,Omega]` with `Omega>kappa_+`. The number of its modes on module `i` is

\[
r_i=\frac{\Omega-\kappa_+}{2\pi}L_i+O(1).
\tag{10}
\]

Choose all these modes as `Y`, so `r=sum_i r_i` and `R=cosh(pi Omega)`. If the minimum period in a sequence of finite sections tends to infinity, then `r/d -> infinity`. Equation (7) forces the norm of the model's retained constant/high angle, and hence of its enlarged retained low/high angle, to tend to one. This statement allows the number of modules, their positive network matrix and all their transition sets to vary.

Including sine transition modes in this even-weight network model does not change the cosine argument: all cosine/sine cross integrals vanish, also across modules. Actual seam face-parity variables and non-corridor pant terms are not represented by (2).

## 4. Controls and the remaining geometric boundary

- **The complete low fibre is essential.** With independent modules `K=I`, retaining only the constant on module 1 and a high mode on module 2 gives zero correlation, even after eliminating transition nodes on both modules. The theorem retains all module constants.
- **A mean-zero or post-constant sector is different.** If the intended low space excludes constants or has already shorted them out, (1) is not its witness. The result applies to the retained-constant split explicitly used here and in the transition clue.
- **Strict grounding is essential to this formulation.** `K>0` makes all inverses legitimate. Arbitrarily small positive grounding is allowed; substituting a singular ungrounded network is not justified by the finite identities.
- **Nonprime controls give the same answer.** The proof works for arbitrary positive cuff periods, including composite endpoint controls. It detects Cauchy network structure, not primality.
- **Normalization remains the PDE gate.** PF-346 already shows that a positive error small at the raw corridor scale can change a normalized shorted angle. This finding proves no comparison between (2) and the actual coupled pant/seam form at the residual energy scale.
- **No infinite-operator conclusion is inferred from a finite norm.** The maximizing constant vector can spread over the entire section. No separated-module witness, compatible infinite-section limit, compactness/noncompactness, Schatten threshold, scattering statement, zeta-zero relation or RH consequence is established.

The precise change to the live question is that **unequal lattices alone cannot erase the whole retained-constant angle of this exact network model**. Approximate shared nonzero modes are unnecessary for that model norm obstruction. The actual-surface question still requires the completed pant/seam comparison and, for an operator-ideal conclusion, localization or singular-value multiplicity after normalization.

## 5. Prior art and verification

The scalar factor in (4) is the classical Cauchy Schur identity already used in PF-346. Commutation of finite positive shorting follows directly from quadratic minimization. Gohberg, Kailath and Olshevsky, [*Fast Gaussian Elimination with Partial Pivoting for Matrices with Displacement Structure*](https://www2.math.uconn.edu/~olshevsky/papers/geppdsam.pdf), Lemma 1.1 and equations (1.3)--(1.4), provide the broader classical preservation of Cauchy-like displacement structure. Forrester and Zhang, [*Parametrising correlation matrices*](https://arxiv.org/abs/1812.07685), equations (2.6)--(2.7), give the standard normalized Schur/partial-correlation interpretation. These sources are S23; neither is invoked as a prime-flute PDE theorem.

The result is an exact specialization of classical algebra, not a new general Schur or interpolation theorem. Its addition to PF-353 is the **one complete fibre versus arbitrary unequal retained nodes** identity (3), with its determinant consequence and its use of the universal constant modes to avoid PF-354's nonzero-frequency obstruction. Searches by Cauchy Schur complements, canonical correlations, displacement generators and Blaschke/kernel interpolation confirmed the classical structural setting; no historical novelty is claimed for this finite identity.

Supplementary standard-library Python `Fraction` checks used `d=1,2,3`, `a=1`, and the path Laplacian plus `tau I` with `tau=1,1/7,1/1000`, both unchanged and conjugated by alternating signs. On zero-based module `i`, transition nodes were `2+i/7` and `3+i/11`, or the transition set was empty. Retained high labels were `(i,5+i/3)` for every module, plus `(0,7)` and `(d-1,8)`. All 36 cases had positive elimination pivots and satisfied (3), (5), (6), and the independent elimination-order calculation exactly. The incomplete-fibre control above was checked with `K=I_2`, low label `(0,1)`, high label `(1,5)`, and transition labels `(0,2),(1,3)`; its mixed block vanished exactly. These are consistency checks, not substitutes for the arbitrary finite proof (4). No Lean proof or independent adversarial approval is claimed.
