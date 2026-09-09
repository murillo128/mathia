# PF-248 — parity-Jacobi tail is trace class but first-moment critical

**Status:** `EXACT-DERIVED + TRACE-CLASS-RELATIVE-JACOBI + FIRST-MOMENT-CRITICAL + HALF-LINE-SQUARE-ROOT-CALIBRATION + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes|PF-247]] identifies the fixed-axis relative operator

\[
J=A^{-1/2}LA^{-1/2}
\]

as two half-line parity Jacobi chains with coefficients tending to diagonal `1/2` and off-diagonal `-1/4`. The proposed local clue `CLUE-critical-jacobi-square-root-decay-window.md` then asks whether the critical zero edge still leaves enough algebraic mode locality to reach PF-243's strict `R>1` separated Robin-Poisson threshold.

Two exact calculations sharpen that question substantially.

First, the PF-247 coefficients approach the constant Jacobi operator at order `j^{-2}`, with the entire `j^{-1}` term cancelling. Consequently the relative Jacobi perturbation is not merely compact: it is **trace class**. However, its first weighted moment diverges, so the usual first-moment Jacobi/Jost scattering regime does not apply directly. The tail sits at an inverse-square threshold.

Second, the constant **half-line** model is better than the bilateral Toeplitz calibration in the clue. The Dirichlet image term cancels the leading `n^{-2}` square-root coefficient in every fixed output row, leaving exact `n^{-3}` decay. Thus a fixed output row of the free square root tolerates input weight `K^R` for every

\[
R<\frac52,
\]

not merely `R<3/2`. The critical edge therefore does **not** by itself kill [[research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing|PF-243]]'s required supercritical window. What remains is a sharper and genuinely nontrivial stability problem: whether this half-line cancellation and enough weighted matrix decay survive PF-247's specific `O(j^{-2})` first-moment-critical variable Jacobi tail, the full-output norm required by PF-243, and then the actual `T_a`/hypercycle perturbations.

## 1. Exact coefficient tail from PF-247

Use PF-247's notation

\[
\alpha=\frac{1+\sqrt5}{2},\qquad \kappa_n=n+\alpha,
\]

and its exact formulas (19)--(27) for the normalized relative coefficients `a_n,b_n`. Direct expansion at infinity gives

\[
\boxed{
a_n=-\frac14+\frac{1}{16n^2}
-\frac{3+\sqrt5}{16n^3}+O(n^{-4}),
}
\tag{1}
\]

and

\[
\boxed{
b_n=\frac12+\frac{5}{8n^2}
-\frac{5(1+\sqrt5)}{8n^3}+O(n^{-4}).
}
\tag{2}
\]

In particular, the `n^{-1}` coefficients vanish exactly in both entries.

For parity `\varepsilon\in\{0,1\}`, identify the chain index by `n=2j+\varepsilon`. Then

\[
\boxed{
a_j^{(\varepsilon)}=-\frac14+\frac{1}{64j^2}+O(j^{-3}),
\qquad
b_j^{(\varepsilon)}=\frac12+\frac{5}{32j^2}+O(j^{-3}).
}
\tag{3}
\]

The error constants may depend on parity, but the displayed leading terms do not.

Let `J_0` be the constant half-line Jacobi matrix with diagonal `1/2` and off-diagonal `-1/4`. In each parity block,

\[
J_\varepsilon-J_0
\]

is the sum of a diagonal operator with entries `b_j^{(\varepsilon)}-1/2` and two weighted shifts with coefficients `a_j^{(\varepsilon)}+1/4`. Equation (3) places each coefficient sequence in `\ell^1`, hence

\[
\boxed{J_\varepsilon-J_0\in\mathcal S_1.}
\tag{4}
\]

Equivalently, after the harmless alternating sign normalization used in PF-247, the same trace-class statement holds relative to the constant chain with off-diagonal `+1/4`. Thus PF-247's compactness statement can be strengthened to trace class at the fixed-axis relative-Jacobi level.

## 2. The first weighted moment nevertheless diverges

Equation (3) also gives, for either parity,

\[
j\left(
\left|a_j^{(\varepsilon)}+\frac14\right|
+\left|b_j^{(\varepsilon)}-\frac12\right|
\right)
=
\frac{11}{64}\frac1j+O(j^{-2}).
\tag{5}
\]

Therefore

\[
\boxed{
\sum_{j\ge1}j\left(
\left|a_j^{(\varepsilon)}+\frac14\right|
+\left|b_j^{(\varepsilon)}-\frac12\right|
\right)=\infty.
}
\tag{6}
\]

This distinction matters. Gerald Teschl's standard whole-line Jacobi scattering hypothesis H.10.1 in *Jacobi Operators and Completely Integrable Nonlinear Lattices*, Chapter 10, assumes the corresponding **first weighted moment** is summable; under that hypothesis Theorem 10.2 constructs Jost solutions. After the elementary sign/affine normalization taking our constant chain to the usual free Jacobi normalization, (6) still diverges. Hence that first-moment Jost machinery cannot simply be invoked to transfer free edge behavior to the PF-247 chain.

Reference:

- Gerald Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices*, AMS Mathematical Surveys and Monographs 72 (2000), Chapter 10, Hypothesis H.10.1 and Theorem 10.2: https://www.mat.univie.ac.at/~gerald/ftp/book-jac/jacop.pdf

The `j^{-2}` tail also has a useful **formal** zero-edge diagnostic. Insert `u_j\sim j^\sigma` into the zero-energy recurrence and retain only the `j^{\sigma-2}` balance from (3). One obtains

\[
-\frac14\sigma(\sigma-1)
+2\left(\frac1{64}\right)+\frac5{32}=0,
\]

or

\[
\boxed{\sigma\in\left\{-\frac12,\frac32\right\}.}
\tag{7}
\]

The formal subordinate branch `j^{-1/2}` is exactly borderline for `\ell^2`. Equation (7) is **not** asserted as an asymptotic theorem for actual solutions: proving such threshold asymptotics would require a discrete regular-singular/Levinson argument with its hypotheses checked. Its role here is only to expose why the `j^{-2}` perturbation is a critical scale rather than a harmless rapidly decaying correction.

## 3. Exact free half-line square-root kernel

The proposed clue first used the bilateral constant model. The half-line model relevant to each PF-247 parity chain has an additional boundary cancellation that can be computed exactly.

On `\ell^2(\mathbb N_0)`, let

\[
(J_0u)_j=-\frac14u_{j-1}+\frac12u_j-\frac14u_{j+1},
\qquad u_{-1}=0.
\tag{8}
\]

The discrete sine transform diagonalizes `J_0` with multiplier

\[
\lambda(t)=\frac12-\frac12\cos t=\sin^2\frac t2,
\qquad 0<t<\pi.
\tag{9}
\]

Therefore `J_0^{1/2}` has multiplier `\sin(t/2)`. Put

\[
c_k:=\frac1\pi\int_0^\pi \sin\frac t2\cos(kt)\,dt.
\tag{10}
\]

Elementary integration gives

\[
\boxed{
c_0=\frac2\pi,
\qquad
c_k=-\frac{2}{\pi(4k^2-1)}\quad(k\ge1).
}
\tag{11}
\]

Using `2\sin((m+1)t)\sin((n+1)t)=\cos((m-n)t)-\cos((m+n+2)t)`, the half-line kernel is

\[
\boxed{
\langle e_m,J_0^{1/2}e_n\rangle
=c_{|m-n|}-c_{m+n+2}.
}
\tag{12}
\]

The first term in (12) is the bilateral Toeplitz tail used in the clue. The second is the Dirichlet image term. For fixed `m` and `n\to\infty`, their `n^{-2}` pieces cancel and

\[
\boxed{
\langle e_m,J_0^{1/2}e_n\rangle
=-\frac{2(m+1)}{\pi n^3}+O_m(n^{-4}).
}
\tag{13}
\]

Consequently, for every fixed output mode `m`,

\[
\sum_{n\ge0}(1+n)^{2R}
\left|\langle e_m,J_0^{1/2}e_n\rangle\right|^2<\infty
\quad\Longleftrightarrow\quad
R<\frac52.
\tag{14}
\]

Since the PF-247 corridor mode weight satisfies `K\asymp n` on either parity chain, the same exponent threshold holds for the fixed-row model up to harmless constants.

The `k^{-2}` bilateral square-root tail is the classical `s=1/2` discrete-fractional scale. A representative reference is Ó. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea, J. L. Varona, *Nonlocal discrete diffusion equations and the fractional discrete Laplacian, regularity and applications*, Advances in Mathematics 330 (2018), 688--738, DOI `10.1016/j.aim.2018.03.023`, arXiv:1608.08913. Equation (12), including the half-line image cancellation, is derived directly here from the sine transform; no general fractional-Laplacian theorem is imported.

## 4. What this proves — and what it does not

The exact free half-line calculation corrects the exponent budget of the proposed clue. The bilateral fixed-row estimate gave only `R<3/2`; after imposing the actual half-line boundary, the image term improves the fixed-row threshold to

\[
\boxed{1<R<\frac52,}
\tag{15}
\]

so there is ample room above PF-243's strict `R>1` requirement **in the constant half-line calibration**.

At the same time, (3)--(7) explain why this cannot yet be promoted to the desired Robin-Poisson theorem. The actual PF-247 chain is trace-class-close to `J_0`, but the perturbation is exactly outside the first-moment regime that would make threshold scattering/Jost transfer routine. Trace-class closeness alone does not preserve weighted matrix-element decay of a non-Lipschitz edge function such as `\lambda^{1/2}`.

Moreover PF-243 needs a separated source-to-**full-output-energy** estimate, not one fixed row of `J^{1/2}`. The scalar factor entering the actual normalized Robin-Poisson map has not yet been identified as literally `J^{1/2}`; PF-233's `K_a=T_a^{1/2}` replacement and PF-235's width-dependent hypercycle/axis coordinate defect remain separate perturbations. Thus (14)--(15) are a calibration of the available exponent margin, not the missing theorem.

The surviving local target is now precise:

> prove or disprove that the specific first-moment-critical `O(j^{-2})` PF-247 Jacobi perturbation preserves enough **half-line weighted functional-calculus decay**, after the full-output summation and the actual Robin scalar factor are inserted, to retain at least one exponent `R>1`.

If that fails already for the fixed-axis variable Jacobi chain, the present functional-calculus route can be closed before spending effort on `T_a` or the geometric coordinate defect. If it succeeds, the free-model margin in (15) quantifies how much decay those later perturbations are allowed to consume.

## 5. Prior-art and novelty audit

The general ingredients are classical:

- asymptotically free Jacobi matrices, first-moment scattering hypotheses, and Jost solutions are standard; Teschl's Chapter 10 is used above only to identify a familiar theorem whose weighted hypothesis our exact tail does **not** satisfy;
- the `|k|^{-2}` kernel scale for a square root of the one-dimensional discrete Laplacian is classical fractional-discrete-Laplacian behavior, as in Ciaurri--Roncal--Stinga--Torrea--Varona;
- the half-line kernel (12) is an elementary sine-transform/method-of-images calculation and is not claimed as a new general theorem.

The project-specific content is the exact continuation of PF-247: its particular compactified-axis/corridor relative coefficients have a cancelled `1/n` term, a nonzero `1/n^2` tail, and hence land simultaneously in trace class and outside the first weighted moment. Combining that exact tail with the half-line square-root calibration changes the live PF-243 question from vague "functional-calculus decay" to a threshold-stability problem with an explicit exponent reserve.

No novelty is claimed for Jacobi scattering theory, fractional discrete Laplacians, trace-class perturbation theory, or half-line Fourier analysis. No spectral statement about zeta zeros or RH follows.

## 6. Falsification and reproducibility checks

1. **Coefficient algebra.** Substitute PF-247 equations (19)--(27) and `\alpha=(1+\sqrt5)/2` into a symbolic series expansion. The invariant diagnostics are
   \[
   n^2(a_n+1/4)\to1/16,
   \qquad
   n^2(b_n-1/2)\to5/8.
   \]
   Any nonzero `1/n` term would invalidate the trace-class/critical classification above.
2. **Trace class versus first moment.** On a Jacobi band, `\ell^1` diagonal/off-diagonal coefficient differences give a trace-class difference by summing the corresponding rank-one matrix entries. Equation (5) independently forces the weighted `\ell^1` divergence.
3. **Half-line kernel.** Equation (12) follows directly from the sine transform and product-to-sum identity. For fixed `m`, expanding the two rational terms in (11) gives the nonzero leading coefficient in (13); therefore the endpoint `R=5/2` itself diverges logarithmically in the squared weighted row.
4. **Formal threshold exponent only.** Equation (7) is not evidence for actual solution asymptotics, a resonance, or absence of point spectrum. Any later use of those exponents must first supply a valid discrete asymptotic theorem or direct proof.
5. **No automatic perturbative transfer.** `J-J_0\in\mathcal S_1` is weaker than the weighted kernel estimate PF-243 needs. A counterexample showing that the actual `O(j^{-2})` tail destroys (13)-type cancellation would refute the positive transfer while leaving (1)--(14) intact.
6. **No full Robin estimate yet.** Full-output accumulation, the exact Robin scalar factor, `T_a`, the hypercycle coordinate map, physical `P/H` recoupling, finite-pant completion, neighboring-module extension, global weak-`S_1` reassembly, and every RH-level bridge remain open.
