---
type: theorem
research_line: xi_flow
finding_id: XF-176
status: canonical
---

# XF-176 — Exact Jacobi plus asymptotic atom matching collapses to the Xi comb

**Evidence classification:** `LITERATURE+DERIVED + EXACT-RIGIDITY + CROSS-INDEX-COUPLING`. An exact real-axis Jacobi law for a sparse positive Gaussian comb upgrades to Fourier self-duality because centered Gaussians and their scale derivatives generate the even Hermite test space. Favorov's 2021 uniqueness theorem for sparse Fourier quasicrystals then turns asymptotic matching of atom positions and masses into exact equality. In Xi Laplace coordinates, `tilde lambda_n-pi n^2=o(n)` and `w_n->1`, together with exact Jacobi reciprocity, force `tilde lambda_n=pi n^2` and `w_n=1` for every `n`. The result is qualitative and exact: it supplies a genuine cross-index modular coupling, but no stability modulus for approximate Jacobi data.

## Statement

Use the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx.
\tag{1}
\]

Let

\[
0<r_1<r_2<\cdots,
\qquad
w_n>0,
\tag{2}
\]

and define the even atomic measure

\[
\boxed{
\rho
:=\delta_0+
\sum_{n\ge1}w_n(\delta_{r_n}+\delta_{-r_n}).
}
\tag{3}
\]

Assume the Xi-tail matching conditions

\[
\boxed{r_n-n\longrightarrow0,}
\qquad
\boxed{w_n\longrightarrow1.}
\tag{4}
\]

For `x>0`, put

\[
\Theta_\rho(x)
:=\langle\rho,e^{-\pi x(\cdot)^2}\rangle
=1+2\sum_{n\ge1}w_n e^{-\pi r_n^2x}.
\tag{5}
\]

Then `(4)` makes `(5)` absolutely convergent for every `x>0`. If the exact Jacobi reciprocity law

\[
\boxed{
\Theta_\rho(x)=x^{-1/2}\Theta_\rho(1/x)
\qquad(x>0)
}
\tag{6}
\]

holds, then

\[
\boxed{\rho=\delta_{\mathbb Z}.}
\tag{7}
\]

Consequently

\[
\boxed{r_n=n,\qquad w_n=1\quad(n\ge1).}
\tag{8}
\]

In the Laplace notation used in XF-166--XF-175, write

\[
\widetilde\lambda_n:=\pi r_n^2,
\qquad
F(x):=\sum_{n\ge1}w_ne^{-\widetilde\lambda_nx}.
\tag{9}
\]

Since `r_n+n~2n`, the position condition in `(4)` is equivalent to

\[
\boxed{
\widetilde\lambda_n-\pi n^2=o(n).
}
\tag{10}
\]

Equivalently, for the XF-175 logarithmic displacement

\[
a_n:=\frac14\log\frac{\widetilde\lambda_n}{\pi n^2},
\tag{11}
\]

one has

\[
\boxed{a_n=o(n^{-1}).}
\tag{12}
\]

Thus an exact Jacobi-positive atomwise deformation cannot hide a tail of nonzero errors at spatial resolution `o(1)`, or at logarithmic Laplace resolution `o(1/n)`, while its masses tend to the Xi masses.

A useful immediate corollary is that **no nontrivial finite atomwise surgery of the Xi theta comb can preserve `(6)`**. A finite surgery agrees exactly with the Xi locations and weights for all sufficiently large `n`, so it satisfies `(4)` and must be trivial by `(7)`.

## 1. Jacobi reciprocity upgrades the Gaussian trace to Fourier self-duality

The conditions `(4)` imply that `rho` is translation bounded. Indeed, for all sufficiently large `n`, `|r_n-n|<1/4`, so the tail support is uniformly separated, and `w_n` is bounded. The finitely many initial atoms do not affect translation boundedness. Hence `rho` is a tempered measure.

Let

\[
g_x(t):=e^{-\pi xt^2}.
\tag{13}
\]

The Gaussian Fourier identity is

\[
\widehat g_x=x^{-1/2}g_{1/x}.
\tag{14}
\]

Therefore `(6)` gives, for every `x>0`,

\[
\begin{aligned}
\langle\widehat\rho,g_x\rangle
&=\langle\rho,\widehat g_x\rangle\\
&=x^{-1/2}\Theta_\rho(1/x)\\
&=\Theta_\rho(x)\\
&=\langle\rho,g_x\rangle.
\end{aligned}
\tag{15}
\]

Set

\[
D:=\widehat\rho-\rho.
\tag{16}
\]

Both `rho` and `widehat rho` are even tempered distributions, so `D` is even, and `(15)` says

\[
D(g_x)=0
\qquad(x>0).
\tag{17}
\]

The map `x -> g_x` is smooth with values in the Schwartz space. Differentiating `(17)` `k` times at `x=1` yields

\[
D\!\left(t^{2k}e^{-\pi t^2}\right)=0
\qquad(k\ge0).
\tag{18}
\]

The even Hermite functions are polynomial multiples of `e^{-pi t^2}` with even polynomial, hence lie in the span in `(18)`; conversely their finite span is dense in the even Schwartz space. Since `D` is even, it also annihilates every odd test function. Continuity on the Schwartz space therefore gives

\[
\boxed{\widehat\rho=\rho}
\tag{19}
\]

as tempered distributions, hence as measures.

This step is important for the source interpretation. A scalar Jacobi identity tested only on the one-parameter Gaussian family looks weaker than a full Poisson summation law, but for an **even tempered atomic comb** it already determines the full Fourier eigenmeasure because scaling derivatives recover the complete even Hermite test basis.

## 2. Favorov asymptotic uniqueness collapses the deformation

A sparse Fourier quasicrystal, in Favorov's terminology, is a discrete tempered measure with uniformly bounded local support multiplicity whose Fourier transform is an atomic measure with tempered total variation. The measure `rho` satisfies these conditions: `(4)` gives uniform tail separation and bounded masses, while `(19)` identifies its Fourier transform with itself.

The standard integer comb

\[
\delta_{\mathbb Z}=\sum_{m\in\mathbb Z}\delta_m
\tag{20}
\]

is also a sparse Fourier quasicrystal and is self-dual under `(1)` by Poisson summation.

Favorov's Theorem 1 states that two sparse Fourier quasicrystals coincide if their support points can be numbered so that the matched locations approach one another and the corresponding masses also approach one another. Apply it to `rho` and `delta_Z`, numbering the positive and negative atoms in matched pairs:

\[
r_n\leftrightarrow n,
\qquad
-r_n\leftrightarrow -n,
\qquad
0\leftrightarrow0.
\tag{21}
\]

The two convergence hypotheses are exactly `(4)`. Hence Favorov gives

\[
\rho=\delta_{\mathbb Z},
\tag{22}
\]

which proves `(7)--(8)`.

The load-bearing external theorem here is therefore not Hamburger rigidity from XF-168. Hamburger assumes the exact square support and then fixes its coefficients. Favorov works one level earlier: once exact Jacobi has been converted to Fourier self-duality, **asymptotically matching support and masses already force the entire comb exactly**, including every finite and remote defect.

## 3. The Xi scale dictionary exposes the rigidity threshold

The atomwise source analysis of XF-175 uses Laplace positions `tilde lambda_n` rather than spatial comb positions. From `(9)`,

\[
\widetilde\lambda_n-\pi n^2
=\pi(r_n-n)(r_n+n).
\tag{23}
\]

Under `r_n~n`, equation `(23)` shows precisely

\[
r_n-n=o(1)
\quad\Longleftrightarrow\quad
\widetilde\lambda_n-\pi n^2=o(n).
\tag{24}
\]

Also

\[
r_n=n e^{2a_n},
\tag{25}
\]

so `(24)` is equivalent to `a_n=o(1/n)`.

This is qualitatively different from the direct source norm of XF-175. There, bounded-factor changes of atoms near `pi n^2` are Gaussian-invisible like `e^{-c pi n^2}` on every fixed transform strip. Here, exact Jacobi reciprocity supplies a nonlocal cross-index condition: if the same deformation converges to Xi at the much finer spatial scale `r_n-n=o(1)` and the masses converge to one, **no nonzero tail defect exists at all**.

The theorem is therefore a genuine answer to one branch of XF-175's next gate. Exact modular coupling can prevent independent high-index atom motion even though the direct Xi source transform is exponentially insensitive to it. The coupling is global rather than energetic: it turns asymptotic agreement at infinity into exact equality everywhere.

## 4. Stress tests and boundary conditions

### Common scale mixtures do not satisfy the asymptotic-matching hypothesis

The positive scale-mixture controls of XF-167 and XF-169 are not counterexamples. A nontrivial common spatial dilation sends integer positions to `e^{2a}n`, whose displacement from `n` is of order `n`, not `o(1)`. Symmetric mixtures contain several such lattices. Thus those exact-Jacobi controls lie outside `(4)` exactly where they should.

### XF-175's Gaussian blindness is not contradicted

XF-175 permits arbitrary matched atomwise motion without imposing exact Jacobi on the deformed comb. Its conclusion is an absolute transform-stability statement, not a modular-admissibility theorem. XF-176 says that a tail deformation which is both asymptotically Xi at the scale `(24)` **and** exactly Jacobi cannot be one of those independent perturbations unless it is zero.

### Relative spectral accuracy alone is weaker than the theorem

The condition

\[
\widetilde\lambda_n/(\pi n^2)\to1
\tag{26}
\]

only gives `r_n/n->1`; it does not imply `r_n-n->0`. For example, a bounded nonzero spatial displacement already has relative Laplace error `O(1/n)` while failing the Favorov matching condition. XF-176 therefore does not justify replacing `(10)` by mere relative convergence. The absolute `o(n)` Laplace scale is load-bearing in the present reduction.

### Mass matching and exact Jacobi are also load-bearing

Favorov's theorem requires the matched masses to converge, so `w_n->1` is not cosmetic. Likewise, `(6)` is used exactly to obtain `(19)`. A small Jacobi defect gives only an approximate Gaussian self-duality statement; no quantitative version of Favorov's uniqueness theorem is supplied here. The finding must not be read as a stability theorem.

### Uniform sparsity is not an extra hidden axiom

The quasicrystal theorem needs sparsity, but in this application it follows from `(4)`: eventually each `r_n` lies in a disjoint fixed neighborhood of the corresponding integer. Thus the only substantive source hypotheses beyond exact Jacobi are the asymptotic location and mass matching themselves.

## Prior-art and novelty audit

The decisive prior-art hit is Serhii Yu. Favorov, *Uniqueness theorems for Fourier quasicrystals and temperate distributions with discrete support*, Proceedings of the American Mathematical Society 149:10 (2021), 4431--4440, DOI `10.1090/proc/15546`. Its Theorem 1 states exactly the asymptotic uniqueness principle used in Section 2: two sparse Fourier quasicrystals with matched support locations and masses tending to one another coincide.

The broader Fourier-quasicrystal literature classifies uniformly discrete support/spectrum measures in terms of periodic Dirac-comb structure, but that classification is not needed for the proof. Favorov's asymptotic theorem is sharper for the present matched-Xi question.

No novelty is claimed for Favorov's theorem, Poisson summation, Gaussian Fourier self-duality, or Hermite completeness. The line-specific derived content is the bridge `(6) => (19)` for the theta atom comb, the verification that the XF-175 matched deformation lands in Favorov's sparse class under `(4)`, and the scale translation `(24)--(25)`. Together these turn the qualitative cross-index-coupling request left by XF-175 into an exact rigidity theorem.

## Relation to prior findings

XF-168 proves Hamburger rigidity after the support has already been fixed to `pi n^2`: exact Jacobi then fixes all weights. XF-169--XF-174 show that common positive scale mixing survives many source-side classifiers but carries a quantitative zero-resolution cost. XF-175 leaves the common-scale gauge, constructs an explicit atomwise strip budget, and shows that remote independent atom errors are exponentially invisible to every fixed finite-height transform test.

XF-176 does not reverse the Gaussian-blindness estimate. Instead it identifies a different source-faithful mechanism that the independent controls of XF-175 intentionally dropped: exact Jacobi, when combined with asymptotic Xi matching, promotes the Gaussian trace to a self-dual Fourier quasicrystal, and asymptotic quasicrystal uniqueness then forbids the entire deformation.

## Consequence for `xi_flow`

The cross-index question after XF-175 now has a precise qualitative answer in one regime:

\[
\boxed{
\text{exact Jacobi}
+
\bigl(\widetilde\lambda_n-\pi n^2=o(n)\bigr)
+
(w_n\to1)
\Longrightarrow
\text{exact Xi theta comb}.
}
\tag{27}
\]

Do not spend further passes looking for an exact-Jacobi counterexample with atomwise errors satisfying `(10)` and masses tending to one; Favorov rigidity rules it out once the Gaussian trace is upgraded to self-duality.

The remaining useful gate is **quantitative**. One needs either a stability version that converts an approximate Jacobi/self-duality defect plus finite-scale atom matching into a controlled distance from `delta_Z`, or a theorem that weakens `(10)` while retaining enough positivity/modular structure to force a visible low-spectral defect. Only such a quantitative bridge could be compared with the finite-height zero margins or transition-scale quantities needed for an upper bound on the de Bruijn--Newman threshold. XF-176 is source rigidity, not transition coercivity, and it does not by itself advance `Lambda<=0`.