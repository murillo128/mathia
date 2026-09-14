# NB-116 — Selberg density upgrades the high-zero Burnol tail to inverse height

**Status:** `EXACT-DERIVED + SELBERG-ZERO-DENSITY + HORIZONTAL-FIRST-MOMENT + ARBITRARY-HIGH-ZERO-PACKET + GLOBAL-BLASCHKE-TAIL + NB-115-THRESHOLD-SHARPENING + REPRESENTATION-AUDIT`.

`NB-114` shows that every right-half zeta zero `rho=beta+i gamma` contributes only

\[
\delta_\rho
=\frac{2\beta-1}{\beta^2+\gamma^2}
\]

to the elementary Burnol/Blaschke defect budget, but then bounds `delta_rho` by `1/gamma^2` and counts all zeros. That loses the factor `2 beta-1` exactly where zero-density information is strongest. Keeping that factor and integrating a Selberg zero-density estimate removes the logarithm from the entire high-zero tail.

Let

\[
A(T)
:=
\sum_{\substack{\zeta(\rho)=0\\0<\gamma\le T\\\beta>1/2}}
\left(\beta-\frac12\right),
\tag{1}
\]

with multiplicity. Then

\[
\boxed{A(T)\ll T.}
\tag{2}
\]

Consequently

\[
\boxed{
\sum_{\substack{\zeta(\rho)=0\\\beta>1/2\\|\gamma|\ge G}}
\frac{2\beta-1}{\beta^2+\gamma^2}
\ll \frac1G.
}
\tag{3}
\]

Thus every finite packet `F` of actual right-half zeros with `|Im rho|>=G`, with arbitrary ordinate spread and multiplicity, satisfies

\[
\boxed{
\tau(F)
:=1-|B_F(1)|^2
\ll \frac1G.
}
\tag{4}
\]

The full right-half Blaschke tail above height `G` obeys the same bound. This improves the `O(log G/G)` global tail estimate in `NB-114` and, unlike the earlier fixed-ratio shell estimate, does not depend on packet cardinality.

Combined with the exact compression theorem of `NB-115`, `(4)` has a finite-section consequence. If a packet above height `G` captures a fixed fraction `c>0` of the truncated target in the integer-cell section `E_R`, then at least half of that finite target projection must flow through compression eigenmodes with

\[
\boxed{
0<\lambda
\ll_c
\frac1G+\frac1R.
}
\tag{5}
\]

In particular, when `R/G -> infinity`, any order-one finite high-zero target access must use target-bearing cell-compression modes of retention `O_c(1/G)`. The remaining escape after `NB-115` is therefore one logarithm narrower than the raw zero-counting argument suggests.

## 1. Selberg density controls the first horizontal moment of right-half zeros

Let

\[
N_>(\sigma,T)
:=
\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,\ 0<\gamma\le T,\ \beta>\sigma\},
\tag{6}
\]

counted with multiplicity. Selberg's near-critical zero-density theorem gives

\[
N_>(\sigma,T)
\ll
T^{1-\frac14(\sigma-1/2)}\log T.
\tag{7}
\]

For the argument below only uniformity on a fixed compact strip, say `1/2<=sigma<=3/4`, is needed. Simonič's explicit Selberg-type estimate supplies such uniformity; no optimization of the constant `1/4` is relevant here.

By layer cake,

\[
\begin{aligned}
A(T)
&=
\sum_{\substack{0<\gamma\le T\\\beta>1/2}}
\int_0^{\beta-1/2}du\\
&=
\int_0^{1/2}
N_>\!\left(\frac12+u,T\right)du.
\end{aligned}
\tag{8}
\]

Split at `u_0=1/4`. On `0<=u<=1/4`, `(7)` yields

\[
\begin{aligned}
\int_0^{1/4}
N_>\!\left(\frac12+u,T\right)du
&\ll
T\log T
\int_0^{1/4}T^{-u/4}\,du\\
&=
4T\left(1-T^{-1/16}\right)
\ll T.
\end{aligned}
\tag{9}
\]

For `1/4<=u<=1/2`, monotonicity in `sigma` gives

\[
N_>\!\left(\frac12+u,T\right)
\le N_>\!\left(\frac34,T\right)
\ll T^{15/16}\log T=o(T).
\tag{10}
\]

The interval has fixed length, so `(8)`--`(10)` prove `(2)`.

This is the representation-level point missed by the raw `N(T)` count: the Burnol factor does not charge each off-critical zero equally. It charges its horizontal displacement from the critical line, and zero density controls exactly the first moment of that displacement.

## 2. The horizontal first moment gives an inverse-height Blaschke tail

For a positive-ordinate right-half zero write

\[
a_\rho:=\beta-\frac12>0.
\tag{11}
\]

Then

\[
\delta_\rho
=\frac{2a_\rho}{\beta^2+\gamma^2}
\le \frac{2a_\rho}{\gamma^2}.
\tag{12}
\]

Decompose the positive tail dyadically. By `(2)`, for every `k>=0`,

\[
\sum_{\substack{2^kG\le\gamma<2^{k+1}G\\\beta>1/2}}
a_\rho
\le A(2^{k+1}G)
\ll 2^kG.
\tag{13}
\]

Therefore

\[
\begin{aligned}
\sum_{\substack{\gamma\ge G\\\beta>1/2}}
\delta_\rho
&\le
2\sum_{k\ge0}
\frac{1}{(2^kG)^2}
\sum_{\substack{2^kG\le\gamma<2^{k+1}G\\\beta>1/2}}
a_\rho\\
&\ll
\frac1G\sum_{k\ge0}2^{-k}
\ll \frac1G.
\end{aligned}
\tag{14}
\]

Conjugation gives the same estimate for negative ordinates, proving `(3)`.

For a finite packet `F`, put

\[
S_F:=\sum_{\rho\in F}\delta_\rho.
\tag{15}
\]

The exact elementary comparison from `NB-114` is

\[
1-e^{-S_F}
\le
\tau(F)
=1-\prod_{\rho\in F}(1-\delta_\rho)
\le
S_F.
\tag{16}
\]

Equations `(3)` and `(16)` prove `(4)`. Exhausting the full right-half tail by finite packets also proves convergence of the corresponding Blaschke products and the same `O(1/G)` bound for their total target mass. Since the whole tail budget is `O(1/G)`, `(16)` also gives `tau=S+O(G^{-2})` whenever the full tail is viewed as the monotone limit of finite packets.

The bound is stronger than a shell count in two ways. It permits arbitrarily many ordinates and arbitrarily large relative height spread, and it does not mention packet rank. Collecting more actual high zeros cannot recover the logarithm lost in `NB-114`.

## 3. `NB-115` then forces an inverse-height compression collapse

Use the notation of `NB-115`. For a finite packet `F`, let `K_F` be its finite Burnol model space, let `Q_R` be the integer-cell projection onto `E_R`, and let

\[
H_{F,R}=A^*Q_RA
\tag{17}
\]

be the compression Gram in any orthonormal coordinates of `K_F`. If the compressed span captures a fixed fraction `c` of the truncated target, `NB-115` proves that at least half of that target projection lies in eigenmodes satisfying

\[
0<\lambda\le
\Lambda_{F,R,c}
:=
\frac{2\left(\sqrt{\tau(F)}+R^{-1/2}\right)^2}
     {c(1-1/R)}.
\tag{18}
\]

For `R>=2`, `(4)` and `(x+y)^2<=2x^2+2y^2` give

\[
\Lambda_{F,R,c}
\ll_c
\frac1G+\frac1R,
\tag{19}
\]

which is `(5)`.

The distinction from `NB-115` is material. There the actual-zeta corollary used only `d=O(G log G)` in a fixed-ratio shell and therefore obtained `lambda=O(log G/G+1/R)`. Equation `(19)` is uniform over **every finite actual right-half packet supported above `G`**, regardless of rank and shell width. For sections with `R/G -> infinity`, the source-specific near-kernel scale is `1/G`, not `log G/G`.

This still does not rule out the finite escape. A cell-compression mode with retention `O(1/G)` can in principle amplify a continuum target vector of norm `O(G^{-1/2})` to order-one finite target access. The theorem identifies a stricter necessary scale; it does not provide a source-specific lower bound on that retention.

## 4. Representation audit and matched controls

The observable is the Burnol target mass, not raw zero count and not canonical Gram conditioning. Its exact per-zero coordinate is `delta_rho`, whose numerator is the horizontal displacement `2 beta-1`. Conjugation is an exact symmetry, packet cardinality and shell width are nuisance coordinates, and relative-ordinate shear affects conditioning but not the product formula `(16)`.

The kill test is therefore to ask whether `(3)` follows already from the Riemann--von Mangoldt count used in `NB-114`. It does not. An abstract symmetric zero multiset with `Theta(G log G)` centers in `[G,2G]`, all at a fixed horizontal displacement `beta-1/2=Theta(1)`, is compatible with the raw total-count scale and has Burnol defect `Theta(log G/G)`. The logarithm disappears only after imposing horizontal zero density.

Conversely, the `1/G` order is not improvable from Selberg's estimate alone. A matched density profile can place `Theta(G log G)` centers in `[G,2G]` at displacement `a=Theta(1/log G)`. Their horizontal first moment is `Theta(G)`, compatible with `(7)`, while their summed Burnol defect is `Theta(1/G)`. Thus the new scale is the natural endpoint of the present source input; a smaller tail would require stronger information than this zero-density envelope.

This representation audit also prevents a false interpretation. Equation `(2)` does **not** say there are only `O(T)` off-critical zeros. There may still be `Theta(T log T)` of them extremely close to the critical line. The theorem uses precisely the fact that such zeros then carry proportionally smaller Burnol target weight.

## 5. Prior-art boundary and remaining frontier

Selberg's zero-density theorem is classical. A modern explicit source is Aleksander Simonič, *Explicit zero density estimate for the Riemann zeta-function near the critical line*, J. Math. Anal. Appl. 491 (2020), 124303, DOI `10.1016/j.jmaa.2020.124303`, which records Selberg's estimate and gives a uniform explicit version near the critical line. Burnol's model-space projection formula is already load-bearing in `SOURCES.md`. No novelty is claimed for either theorem.

A targeted prior-art search did not identify a Nyman--Beurling result that combines the horizontal first moment implied by Selberg density with Burnol's per-zero Blaschke factor to obtain the global `O(1/G)` right-half target tail. The line-local contribution is this synthesis and its consequence `(19)` for the finite integer-cell compression mechanism isolated by `NB-115`.

The frontier is correspondingly narrower. Raw rank supply, wider packets, and the total `O(G log G)` zero count can no longer explain order-one finite target access. Any surviving high-zero mechanism must produce target-weighted eigenmodes of the actual integer-cell compression at retention scale `O(1/G+1/R)`, or exploit a representation outside the `NB-115` finite Burnol compression model. The next useful theorem should therefore attack the target spectral weight of `H_{F,R}` below the inverse-height scale, rather than further refining packet cardinality.