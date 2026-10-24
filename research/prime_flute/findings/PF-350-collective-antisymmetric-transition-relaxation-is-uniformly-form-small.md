# PF-350 — collective antisymmetric transition relaxation is uniformly form-small

**Status:** EXACT-DERIVED + UNIFORM-COUPLED-FINITE-SECTION-COMPARISON + GLOBAL-SYMMETRIC-TRANSITION-ANGLE-OPEN.

PF-349 controls face-parity relaxation on one cuff with every other cuff held at zero. The same small-width control extends to **all antisymmetric transition variables in an arbitrarily long coupled tail section**, before or after all symmetric transition variables are eliminated. No bound on neighboring gap ratios, inverse transition conditioning, or the number of modules is needed. The proof uses pant-by-pant positivity to control the collective complementary block; it does not assume that the two global parity diagonal blocks coincide.

This reduces the global transition test for symmetric retained witnesses to symmetric face transmission. It does not transfer PF-349's local correlation to that global symmetric sector, and it does not prove compactness or noncompactness of the completed angle.

## Object and uniform comparison

Use PF-205's natural simultaneous seam strips, PF-214's exact pant-core assembly, and the positive shift `Delta+1`. Work in a finite interval of tail cuff modules `I subset {m,m+1,...}`, with traces outside `I` fixed to zero. Include the bordering pants with zero data at their other cuff. Let

\[
M=Q+\Lambda_E>0,
\qquad \phi_n^{\rm left}=(u_n+v_n)/\sqrt2,
\quad \phi_n^{\rm right}=(u_n-v_n)/\sqrt2.
\tag{1}
\]

Here `u` is symmetric and `v` antisymmetric **across the two faces of each strip**, not across neighboring pants. All Fourier bases use the common zero-twist physical cuff coordinate and its period `L_n`.

Fix `kappa>0` and `0<eta<=1`. Let `T_n` contain all sine and cosine modes with positive physical frequency in `(kappa,kappa+eta)`, and write `T_+` and `T_-` for their symmetric and antisymmetric face copies on all modules in `I`. The real dimension is

\[
r_n=\dim T_n=\eta L_n/\pi+O(1).
\tag{2}
\]

Choose any finite collection `R` of symmetric nontransition Fourier modes and include all of `T_+`. There is no common upper-frequency bound on `R`. Every antisymmetric nontransition coefficient remains zero. On `R op T_+ op T_-`, write the actual pant form and seam form as

\[
\Lambda_E=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}\ge0,
\qquad Q=\begin{pmatrix}Q_+&0\\0&Q_-\end{pmatrix},
\qquad H=A+Q_+.
\tag{3}
\]

The first slot is `R op T_+`, the second `T_-`. These can have different dimensions. Define two forms on exactly the same retained space `R`:

\[
S_{\rm sym}=H^{/T_+},\qquad
S_{\rm full}=M^{/(T_+\oplus T_-)}.
\tag{4}
\]

The first allows symmetric transition transmission through the **entire section**, with antisymmetric data zero. The second frees both parities throughout that section. Both include sine and cosine transition data.

There are constants `C_kappa` and `epsilon_m -> 0`, independent of the section size and the retained Fourier cutoff, such that

\[
\boxed{(1+b_{m,\eta})^{-1}S_{\rm sym}
\le S_{\rm full}\le S_{\rm sym},
\qquad b_{m,\eta}\le C_\kappa\eta+\epsilon_m.}
\tag{5}
\]

The same comparison holds before shorting `T_+`. This is relative control at the actual shorted energy scale, even when those energies are very small. For fixed small positive width the error is bounded by a small constant; it is not asserted to tend to zero with `m` alone.

## 1. A collective pant block is bounded by its local diagonal blocks

PF-214 gives the exact positive assembly

\[
\Lambda_E[\phi]=\sum_j E_j(\phi_j^{\rm right},\phi_{j+1}^{\rm left}),
\tag{6}
\]

where each `E_j` is the positive shifted pant DtN form. For any positive two-slot form, Cauchy--Schwarz implies

\[
E_j(a,b)\le2E_j(a,0)+2E_j(0,b).
\tag{7}
\]

Apply (7) with `u=0` in (1) and sum. If `C_nn` is the diagonal module block of the actual collective antisymmetric pant matrix `C`, then

\[
\boxed{0\le C\le2\bigoplus_{n\in I}C_{nn}.}
\tag{8}
\]

In particular the intermodule terms have not been discarded: their full contribution is bounded by (8). Each `C_nn` is one half the sum of the two adjacent pant self-responses compressed to `T_n`. The signs in the antisymmetric identification do not change a self-response. There is no claim that `C=A` globally.

Put

\[
D_n=L_n^{-1}(s_{n-1}^{-1}+s_n^{-1}),
\qquad s_j=(h_j+h_{j+1})/2.
\tag{9}
\]

PF-344's bounded-frequency trial gives each normalized cosine self-energy at most `C_K(D_n+1)`, with `K=kappa+1`. The identical upper bound holds for a normalized sine: in the raywise linear extension use `|sin(xi t)|<=1` and `|(sin(xi t))'|<=K`; its transverse integral against `sech(t)` is bounded, and the remaining chart energy has the same `O_K(1)` estimate. No reflection decoupling or invariance of an individual Fourier mode is assumed. Thus positivity gives

\[
\|C_{nn}\|\le\operatorname{Tr}C_{nn}
\le C_Kr_n(D_n+1).
\tag{10}
\]

This estimate controls every combination in the growing band through its trace, not just its individual matrix entries.

## 2. The actual seam dominates the entire antisymmetric transition block

The strip reflection makes `Q` exactly diagonal in face parity. PF-317's hyperbolic/flat form comparison and `z coth(z)>=1` give, for every transition frequency,

\[
Q_{-,n}\ge\frac{1}{w_n(1+w_n^2)}I.
\tag{11}
\]

Combining (8)--(11) yields

\[
\boxed{C\le b_{m,\eta} Q_-,\quad
b_{m,\eta}:=2C_K\sup_{n\ge m}
w_n(1+w_n^2)r_n(D_n+1).}
\tag{12}
\]

The supremum is over the tail geometry, so the bound is independent of which finite interval is selected. The known natural scales give

\[
w_n\asymp P_n^{-1},\quad L_n\to\infty,\quad L_n=O(\log P_n),
\quad h_n\asymp g_n/P_n,\quad g_n\ge2,
\]
\[
s_{n-1},s_n\ge h_n/2,
\qquad w_n(s_{n-1}^{-1}+s_n^{-1})\le C.
\tag{13}
\]

Here `P_n,g_n` use PF-205's cuff indexing; the last inequality needs no ratio of adjacent gaps. By (2),

\[
w_nr_n(D_n+1)
\le C(\eta+L_n^{-1})+Cw_n(\eta L_n+1).
\tag{14}
\]

For `0<eta<=1`, the supremum of the non-`eta` terms tends to zero as `m -> infinity`, proving the bound for `b` in (5). Unlike PF-348's two-sided Gram comparison, this step needs no Baker--Harman--Pintz growth exponent. It uses only (13) and the existing uniform upper trial.

## 3. Relative control survives all symmetric transition elimination

The needed block inequality holds without equal diagonal blocks, without commutativity, and even when the pant block `C` is singular. Let `P=[[A,B],[B*,C]]>=0`, `Q_->0`, and `C<=b Q_-`, for `b>0`. Put `V=C+Q_-` and `delta=b/(1+b)`. Then `C<=delta V`. Positivity of `P` gives

\[
|\langle x,By\rangle|^2\le A[x]C[y].
\tag{15}
\]

For \(y=V^{-1}B^*x\), write \(e=\langle x,BV^{-1}B^*x\rangle=V[y]\ge0\). Equation (15) implies `e^2<=delta A[x]e`, hence

\[
0\le BV^{-1}B^*\le\delta A.
\tag{16}
\]

As `Q_+>=0`, shorting all of `T_-` gives

\[
F=H-BV^{-1}B^*,\qquad
\boxed{(1+b)^{-1}H\le F\le H.}
\tag{17}
\]

If `b=0`, positivity forces `B=0` and the conclusion is equality. Finally, shorting a fixed subspace is monotone and homogeneous because it is the minimum over that subspace. Short `T_+` in (17). Sequential and simultaneous minima agree, so `F^{/T_+}=S_full` and (5) follows. This argument never bounds `H_TT^{-1}` and remains valid after arbitrarily ill-conditioned symmetric shorting.

## What this does and does not say about the angle

For retained symmetric low/high vectors `u,v`, set

\[
\rho_S(u,v)=\frac{|S[u,v]|}{\sqrt{S[u]S[v]}}.
\]

Set `delta=b_(m,eta)/(1+b_(m,eta))`. Equation (5) implies `0<=S_sym-S_full<=delta S_sym`. Cauchy--Schwarz for that positive difference, the reverse triangle inequality, and `S_full[u]<=S_sym[u]` give

\[
\boxed{\rho_{S_{\rm full}}(u,v)
\ge\max\{0,\rho_{S_{\rm sym}}(u,v)-\delta\}.}
\tag{18}
\]

Thus any sufficiently large normalized witness established **after global symmetric transition shorting** survives the full parity relaxation with the explicit loss in (18). Both denominators are energies from the same respective globally shorted form.

PF-349 supplies a witness only with other cuffs fixed to zero. It supplies no lower bound for `rho_(S_sym)` in (18). Neighboring symmetric transition traces can still follow one another through the pant corridors. Equation (5) neither controls that relaxation nor transfers compactness between the two normalized cross operators: a fixed `O(eta)` form error need not be compact. A positive compactness theorem would also have to control retained antisymmetric nontransition modes, which are fixed to zero here. No infinite-section operator domain, singular-value counting theorem, or finite-head relaxation has been established here.

## Prior art, checks, and significance

The block Cauchy--Schwarz inequality is classical; see Moslehian, Kian and Xu, *Positivity of 2 x 2 block matrices of operators*, Banach J. Math. Anal. 13 (2019), 726–743, [arXiv:1904.08680](https://arxiv.org/abs/1904.08680), Proposition 5.14 and Theorem 5.11. Positive shorting is the classical Anderson--Trapp framework, [DOI](https://doi.org/10.1137/0128007), already S24. Equations (7) and (15)--(17) are elementary consequences, proved here; no new matrix theorem is claimed. PF-214 already places the pant assembly in classical domain-decomposition theory.

The line-specific addition is the **collective** estimate (12): positive two-boundary pant assembly turns the natural seam penalty and narrow-band dimension count into a relative bound uniform in an arbitrarily long interacting section. PF-349's single-module equal-diagonal decomposition does not itself supply that global bound. The result includes all tangential modes in the transition interval and arbitrary retained symmetric Fourier cutoffs; it removes the need to analyze antisymmetric transition propagation separately before attacking the unresolved symmetric propagation.

Supplementary exact `Fraction` arithmetic checked 18 coupled-chain controls: `2,3,4` modules, `1,2` coordinates per face, and `b in {1/100,1/5,1}`. For each chain, construct each adjacent two-face pant block as `10^(2j-2) R_j^t R_j`, with `j=0,...,modules-2`, rectangular `R_j` of size `(2r-1) x 2r`, entries drawn from `{-2,-1,0,1,2}` using `Random(350)`. Assemble on opposite faces of successive modules and transform to rational parity coordinates `left=u+v`, `right=u-v`. Add `10^(-12)I` to the symmetric block and take the antisymmetric seam on module `n` to be `[(2 Tr C_nn+1)/b]I`. Exact positive-semidefinite elimination checked (8), (12), (17), the shorted sandwich retaining the first and last symmetric coordinates, and equality of sequential/simultaneous shorting. Three scalar controls `P=[[1,1],[1,1]]`, `Q_+=0`, `Q_-=1/b` attain equality in the lower bound (17). These checks validate finite algebra, not the pant PDE or its constants; the proof is independent of them.

The load-bearing geometric checks are the actual two-boundary pant support, the single-mode self-energy upper trial, and the actual hyperbolic antisymmetric seam lower bound. A larger seam width, a transition band reaching unbounded physical frequencies, or extra long-range form couplings require a new estimate. Nonprime flutes satisfying the same scales and trials satisfy the same comparison. There is no prime-specific invariant, relative scattering theorem, or RH implication.

For the active transition clue, the remaining narrow-band test is now the globally coupled **symmetric** transition form, with the quantitative full-parity comparison already available. The local Dirichlet correlation and that global form remain different objects.
