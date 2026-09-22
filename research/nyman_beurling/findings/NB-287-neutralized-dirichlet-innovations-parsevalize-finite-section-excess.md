# NB-287 — neutralized Dirichlet innovations Parsevalize finite-section excess

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-282, NB-284, NB-285, NB-286
- **Classification:** `EXACT-DERIVED + FIRST-FREE-JET-COST + FINITE-SECTION-GRAM + NULLSPACE-INNOVATION + ORTHONORMAL-DECOMPOSITION + TARGET-AWARE + MOVING-PACKET-CONDITIONING + ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-286` expresses the genuine finite-section penalty as a dynamic sum of target-aligned rank-one Gram gains. The same quantity has a stronger source-space description: after the first surjective section, every genuinely new Dirichlet direction generates one canonical **sample-null innovation**, these innovations are mutually orthonormal and complete the interpolation nullspace, and the whole finite-section excess is exactly the Parseval tail of the current minimum-norm interpolant on those innovations.

Fix a zero packet `Z` and retain the quotient-source Hilbert space, first-free sampling map and nested finite sections from `NB-285`:

\[
\mathcal H=\mathcal H_Z^\infty,
\qquad
L:\mathcal H\to\mathbb C^N,
\qquad
V_r\subseteq V_{r+1},
\qquad
K_r=LP_rL^*.
\]

Work beyond a section `r_0` on which `L|_(V_(r_0))` is already onto, as supplied by `NB-282`. Put

\[
D_r:=V_r\cap\ker L,
\qquad
R_r:=P_rL^*K_r^{-1}.
\]

Thus `R_r` is the optimal right inverse from `NB-285`. Whenever the next integer contributes a genuinely new normalized source direction

\[
\psi_{r+1}\in V_{r+1}\ominus V_r,
\qquad
\|\psi_{r+1}\|=1,
\]

set

\[
v_{r+1}:=L\psi_{r+1},
\qquad
\ell_r:=v_{r+1}^*K_r^{-1}v_{r+1},
\]

and define the **neutralized Dirichlet innovation**

\[
\boxed{
q_{r+1}
:=
\frac{
\psi_{r+1}-R_rv_{r+1}
}{
\sqrt{1+\ell_r}
}.
}
\tag{1}
\]

Then

\[
\boxed{
Lq_{r+1}=0,
\qquad
\|q_{r+1}\|=1,
\qquad
D_{r+1}=D_r\oplus\operatorname{span}\{q_{r+1}\}.
}
\tag{2}
\]

Consequently the `q_(r+1)` produced by successive genuine enrichments are mutually orthonormal. Moreover,

\[
\boxed{
\overline{\bigcup_{r\ge r_0}D_r}=\ker L,
}
\tag{3}
\]

so, after adjoining an orthonormal basis of the already-present finite space `D_(r_0)`, the neutralized innovations form an orthonormal basis of the full interpolation nullspace.

Let

\[
h_r:=R_ry=P_rL^*K_r^{-1}y
\]

be the finite minimum-norm interpolant of the prescribed first-free datum `y`, and let `h_infty` be the corresponding minimum-norm interpolant in `H`. The one-step update is not merely a Sherman--Morrison identity in data space. It is the source-space orthogonal projection

\[
\boxed{
h_{r+1}
=
h_r-\langle h_r,q_{r+1}\rangle q_{r+1}.
}
\tag{4}
\]

Its squared coefficient is exactly the `NB-286` target-aligned leverage gain:

\[
\boxed{
|\langle h_r,q_{r+1}\rangle|^2
=
\frac{
|v_{r+1}^*K_r^{-1}y|^2
}{
1+v_{r+1}^*K_r^{-1}v_{r+1}
}
=
\mathcal C_r-\mathcal C_{r+1}.
}
\tag{5}
\]

Because the `q`'s are orthonormal, the apparently dynamic tail of `NB-286` is actually a static Parseval expansion. For every feasible `M>=r_0`,

\[
\boxed{
h_M-h_\infty
=
\sum_{r\ge M}
\langle h_M,q_{r+1}\rangle q_{r+1},
}
\tag{6}
\]

where zero/redundant enrichment steps are simply omitted, and

\[
\boxed{
\mathfrak A_M
=
\|h_M-h_\infty\|^2
=
\sum_{r\ge M}
|\langle h_M,q_{r+1}\rangle|^2.
}
\tag{7}
\]

Furthermore

\[
\langle h_M,q_{r+1}\rangle
=
\langle h_r,q_{r+1}\rangle
\qquad(r\ge M),
\tag{8}
\]

so `(7)` is term-by-term the telescoping expansion from `NB-286`, but with the changing inverse Gram metric removed from the final representation.

Equivalently, if `h_r` is nonzero, the fractional gain of `NB-286` has the direct source-space angle formula

\[
\boxed{
\alpha_r
=
\frac{\mathcal C_r-\mathcal C_{r+1}}{\mathcal C_r}
=
\left|
\left\langle
\frac{h_r}{\|h_r\|},q_{r+1}
\right\rangle
\right|^2.
}
\tag{9}
\]

Thus the two factors in the whitened formula

\[
\cos^2\theta_r\frac{\ell_r}{1+\ell_r}
\]

are exactly the squared cosine with one canonical source-space direction after sample neutralization. Large raw leverage and target alignment are not two independent mechanisms; together they measure how much of the current minimum-norm source lies in the **newly unlocked interpolation-null direction**.

This identifies a sharper moving-packet target. A persistent finite-section obstruction requires nonvanishing Parseval mass of the finite minimum-norm source in future exact sample-null Dirichlet relations. Conversely, to make the genuine finite-section excess vanish it is enough to prove that this future null-innovation tail is asymptotically invisible to `h_(M_X)`.

---

## 1. Neutralizing the new atom creates the unique new null direction

For `r>=r_0`, let

\[
L_r:=L|_{V_r}.
\]

Surjectivity gives

\[
K_r=L_rL_r^*\succ0,
\]

and the finite minimum-norm right inverse is

\[
R_r=L_r^*(L_rL_r^*)^{-1}=P_rL^*K_r^{-1}.
\tag{10}
\]

It satisfies

\[
L R_r=I_{\mathbb C^N}
\tag{11}
\]

and

\[
R_r^*R_r=K_r^{-1}.
\tag{12}
\]

Suppose `V_(r+1)` gains one new dimension and choose unit

\[
\psi_{r+1}\perp V_r.
\]

Its first-free sample vector is `v_(r+1)=L psi_(r+1)`. The old section can reproduce exactly those samples with minimum norm `R_r v_(r+1)`. Therefore

\[
L\bigl(\psi_{r+1}-R_rv_{r+1}\bigr)=0.
\tag{13}
\]

Because `R_rv_(r+1)` belongs to `V_r` and `psi_(r+1)` is orthogonal to `V_r`,

\[
\begin{aligned}
\|\psi_{r+1}-R_rv_{r+1}\|^2
&=1+\|R_rv_{r+1}\|^2\\
&=1+v_{r+1}^*K_r^{-1}v_{r+1}\\
&=1+\ell_r.
\end{aligned}
\tag{14}
\]

This proves the first two assertions of `(2)`.

Now

\[
D_r=\ker L_r.
\]

Since `L_r` is onto,

\[
\operatorname{ran}L_r^*=D_r^\perp\cap V_r.
\tag{15}
\]

The repair `R_rv_(r+1)` lies in this range, while `psi_(r+1)` is orthogonal to all of `V_r`. Hence the numerator in `(1)` is orthogonal to `D_r`, and therefore

\[
q_{r+1}\perp D_r.
\tag{16}
\]

Surjectivity persists after enrichment. Since the domain dimension increases by one while the rank stays `N`, the kernel dimension also increases by one. We have already produced one nonzero vector in the new kernel orthogonal to the old kernel, so

\[
D_{r+1}=D_r\oplus\operatorname{span}\{q_{r+1}\}.
\tag{17}
\]

If the next integer adds no new source direction, then `V_(r+1)=V_r`, `D_(r+1)=D_r`, and there is no innovation to add. All subsequent statements are understood along the genuine-enrichment subsequence.

Equation `(17)` immediately implies pairwise orthogonality: every earlier innovation belongs to `D_r`, whereas the next `q_(r+1)` is orthogonal to `D_r`.

The span in `(1)` is canonical even though the phase of `psi_(r+1)` is not. Replacing `psi_(r+1)` by a unimodular multiple changes `v_(r+1)`, its optimal repair, and `q_(r+1)` by the same phase. Thus the one-dimensional null innovation itself is independent of that convention.

---

## 2. The finite nullspaces exhaust the full interpolation nullspace

By definition of the infinite quotient-source space,

\[
\overline{\bigcup_rV_r}=\mathcal H.
\tag{18}
\]

Density of `V_r` in `H` alone does not automatically imply density of `D_r=V_r cap ker L` in `ker L`; the interpolation constraint has to be repaired. Here the finite surjectivity from `NB-282` supplies exactly the needed bounded correction.

Fix one surjective section `r_0` and its bounded right inverse `R_(r_0)`. Let `z in ker L`. Choose `x_j in V_(r_j)` with

\[
x_j\to z,
\qquad
r_j\to\infty.
\]

Continuity of `L` gives

\[
Lx_j\to Lz=0.
\]

For `r_j>=r_0`, define

\[
z_j:=x_j-R_{r_0}Lx_j.
\tag{19}
\]

Since `R_(r_0)Lx_j` lies in `V_(r_0) subseteq V_(r_j)`, we have `z_j in V_(r_j)`. Moreover

\[
Lz_j=Lx_j-LR_{r_0}Lx_j=0,
\]

so `z_j in D_(r_j)`. Finally,

\[
\|z_j-z\|
\le
\|x_j-z\|
+
\|R_{r_0}\|\,\|Lx_j\|
\longrightarrow0.
\tag{20}
\]

This proves `(3)`.

Combining `(3)` with the orthogonal one-dimensional growth `(17)` gives, for every feasible `M>=r_0`,

\[
\boxed{
\ker L
=
D_M
\oplus
\overline{\operatorname{span}}
\{q_{r+1}:r\ge M\}.
}
\tag{21}
\]

This is the completeness step that turns the one-step rank-one algebra into a full Parseval identity rather than merely another telescoping formula.

---

## 3. Minimum-norm interpolation is successive removal of null innovations

The finite minimum-norm interpolant

\[
h_r=R_ry
\tag{22}
\]

is feasible and orthogonal to the finite kernel:

\[
Lh_r=y,
\qquad
h_r\perp D_r.
\tag{23}
\]

Because `h_r` is also a feasible vector in `V_(r+1)`, the entire next feasible affine space is

\[
\{h\in V_{r+1}:Lh=y\}
=h_r+D_{r+1}.
\tag{24}
\]

Using `(17)` and `(23)`, any point in `(24)` can be written uniquely as

\[
h_r+d+tq_{r+1},
\qquad
d\in D_r.
\]

The three relevant components satisfy

\[
h_r\perp D_r,
\qquad
q_{r+1}\perp D_r.
\]

Minimizing the norm first kills `d`, and minimizing in the remaining one-dimensional direction subtracts the projection of `h_r` onto `q_(r+1)`. Therefore

\[
h_{r+1}
=h_r-\langle h_r,q_{r+1}\rangle q_{r+1},
\]

which is `(4)`. Pythagoras gives

\[
\boxed{
\mathcal C_r-\mathcal C_{r+1}
=
\|h_r\|^2-\|h_{r+1}\|^2
=
|\langle h_r,q_{r+1}\rangle|^2.
}
\tag{25}
\]

To identify this with `NB-286`, use `h_r=R_ry`. Since `psi_(r+1) perp V_r`,

\[
\langle h_r,\psi_{r+1}\rangle=0.
\tag{26}
\]

Also, by `(12)`,

\[
\bigl|\langle h_r,R_rv_{r+1}\rangle\bigr|
=
\bigl|v_{r+1}^*K_r^{-1}y\bigr|.
\tag{27}
\]

Dividing by the normalization in `(14)` gives

\[
|\langle h_r,q_{r+1}\rangle|^2
=
\frac{|v_{r+1}^*K_r^{-1}y|^2}
{1+v_{r+1}^*K_r^{-1}v_{r+1}},
\tag{28}
\]

proving `(5)` and `(9)`.

The meaning of the denominator in `NB-286` is now transparent. A new atom first has its already-reproducible sample component removed by the old optimal right inverse. The remaining exact-sample-null vector has norm `sqrt(1+ell_r)`, and normalization converts it into the unit direction `q_(r+1)`. The target-aware gain is just the squared projection onto that direction.

---

## 4. The dynamic leverage tail is a static Parseval tail

Fix `M>=r_0`. Iterating `(4)` gives, for `R>M`,

\[
h_R
=
h_M-
\sum_{r=M}^{R-1}
\langle h_r,q_{r+1}\rangle q_{r+1}.
\tag{29}
\]

The innovation vectors are mutually orthonormal. More is true: the coefficient in `(29)` can be frozen at the initial section. Indeed the previous updates from `h_M` to `h_r` are linear combinations of

\[
q_{M+1},\ldots,q_r,
\]

all orthogonal to `q_(r+1)`. Hence

\[
\boxed{
\langle h_r,q_{r+1}\rangle
=
\langle h_M,q_{r+1}\rangle.
}
\tag{30}
\]

Thus

\[
h_R
=
h_M-
\sum_{r=M}^{R-1}
\langle h_M,q_{r+1}\rangle q_{r+1}.
\tag{31}
\]

The infinite minimum-norm interpolant `h_infty` has the same samples as `h_M`, so

\[
h_M-h_\infty\in\ker L.
\tag{32}
\]

Both `h_M` and `h_infty` are orthogonal to `D_M`: the first by finite minimum-norm interpolation, the second because `h_infty perp ker L`. Therefore

\[
h_M-h_\infty
\in
\ker L\ominus D_M.
\tag{33}
\]

By `(21)`, the right-hand side is exactly the closed span of the future innovations. Taking Fourier coefficients against `q_(r+1)` and using `h_infty perp ker L` gives

\[
\langle h_M-h_\infty,q_{r+1}\rangle
=
\langle h_M,q_{r+1}\rangle.
\tag{34}
\]

Parseval in `(21)` proves `(6)` and `(7)` directly. In particular,

\[
\boxed{
\mathfrak A_M
=
\sum_{r\ge M}
\frac{|v_{r+1}^*K_r^{-1}y|^2}
{1+v_{r+1}^*K_r^{-1}v_{r+1}}
=
\sum_{r\ge M}|\langle h_M,q_{r+1}\rangle|^2.
}
\tag{35}
\]

So the exact `NB-286` series has no hidden interaction between different future enrichments even in source space. Its changing inverse metrics are the coordinates needed to construct an orthonormal basis of the future interpolation nullspace one direction at a time.

There is also a compact geometric form. Since `h_M-h_infty` is precisely the orthogonal projection of `h_M` onto `ker L`,

\[
\boxed{
\mathfrak A_M
=
\|P_{\ker L}h_M\|^2,
\qquad
\frac{\mathfrak A_M}{\mathcal C_M}
=
\frac{\|P_{\ker L}h_M\|^2}{\|h_M\|^2}.
}
\tag{36}
\]

The first equality was already implicit in the minimum-norm geometry of `NB-285`; the new content is the explicit orthonormal resolution of that projection by legal one-Dirichlet-step neutralizations.

---

## 5. Consequence for the moving Ford regime

For a moving family `(Z_X,M_X)`, let `q_(X,r+1)` denote the neutralized innovations constructed inside the packet-dependent quotient-source space. Equation `(7)` gives the exact criterion

\[
\boxed{
\mathfrak A_{M_X}(Z_X)
=
\sum_{r\ge M_X}
|\langle h_{X,M_X},q_{X,r+1}\rangle|^2.
}
\tag{37}
\]

Therefore a sufficient condition for the genuine finite-section penalty to vanish is

\[
\sum_{r\ge M_X}
|\langle h_{X,M_X},q_{X,r+1}\rangle|^2
\longrightarrow0.
\tag{38}
\]

Conversely, an order-one floor

\[
\mathfrak A_{M_X}(Z_X)\ge\eta>0
\tag{39}
\]

forces at least `eta` of squared correlation mass between the finite minimum-norm source and the future exact-sample-null innovations.

For a relative floor, `(36)` is even sharper:

\[
\frac{\mathfrak A_{M_X}}{\mathcal C_{M_X}}
\ge\delta
\quad\Longleftrightarrow\quad
\sum_{r\ge M_X}
\left|
\left\langle
\frac{h_{X,M_X}}{\|h_{X,M_X}\|},q_{X,r+1}
\right\rangle
\right|^2
\ge\delta.
\tag{40}
\]

This removes the need to reason separately about a small eigenvalue of `K_r`, a large leverage `ell_r`, and an alignment angle in data space. Those quantities remain useful for calculating a one-step update, but the obstruction itself is simply the future-nullspace Fourier mass of the current source.

The arithmetic object is also more explicit than a generic kernel projection. The numerator of `(1)` is

\[
\psi_{r+1}-R_rL\psi_{r+1}.
\tag{41}
\]

It is an exact relation between one newly admitted orthogonalized Dirichlet source direction and the **minimum-norm old-section source with identical first-free samples**. Thus future progress is controlled only by sample-invisible source relations. Any arithmetic estimate aimed at the remaining finite-section obstruction should therefore target the correlations

\[
\langle h_{M},q_{r+1}\rangle,
\tag{42}
\]

or structured blocks of them, rather than raw future Gram mass or `lambda_min(K_r)` in isolation.

This is a route narrowing, not an RH implication. No estimate of `(42)` for actual Ford-coupled packets is proved here.

---

## 6. Adversarial checks

### The innovations are not assumed orthogonal; they are proved orthogonal

The key point is `(17)`. Each new `q_(r+1)` lies in `D_(r+1)` and is orthogonal to the entire previous kernel `D_r`. Since all earlier innovations lie in `D_r`, pairwise orthogonality follows. It is not inferred from the rank-one Gram updates alone.

### Density of the finite source spaces is not silently transferred to their kernels

That transfer can fail for arbitrary constrained dense families. Equation `(19)` uses one fixed finite right inverse, available because `NB-282` gives eventual surjectivity, to repair approximants into `ker L`. This is the load-bearing step behind completeness `(3)`.

### No inverse Gram is used before surjectivity

All formulas involving `K_r^{-1}` start only after `r_0`, where `L|_(V_r)` is onto. Earlier sections can be handled with pseudoinverses, but they are irrelevant to the tail criterion and are not used in the proof.

### Redundant integer additions cause no artificial basis vector

If `V_(r+1)=V_r`, there is no one-dimensional enrichment and no `q_(r+1)`. The theorem indexes only genuine source-space increments. This preserves the exact finite-section problem rather than assigning leverage to a duplicated generator.

### The result is invariant under the phase choice of the new orthogonalized atom

Changing `psi_(r+1)` by a unit scalar changes `q_(r+1)` by the same scalar, leaving its span and every squared correlation invariant. The construction is therefore not an artifact of a Gram--Schmidt phase convention.

### The Parseval identity does not assume RH or source completeness beyond the declared quotient space

`H` is the closed quotient-source space already defined in `NB-284/285`. The proof uses density of the finite sections **in that space by definition**; it does not identify `H` with ambient `H^2`, `C_ZH^2`, or any RH-equivalent closure. The full kernel in `(3)` means `ker(L:H->C^N)`, not the kernel of ambient Hardy evaluation.

### A large nullspace tail is not by itself a lower bound

The future innovations are an orthonormal basis of the available null directions, but only their correlations with the specific `h_M` matter. A large or complicated future nullspace can be completely irrelevant if `h_M` is nearly orthogonal to it. This preserves the target-aware warning of `NB-001` and `NB-286`.

---

## 7. Prior-art audit and novelty boundary

The generic linear-algebra ingredients are classical. Recursive pseudoinverse/least-squares updates under appended columns belong to the Greville tradition; for a modern account see Ruben Staub and Stephan N. Steinmann, *Efficient recursive least squares solver for rank-deficient matrices*, Applied Mathematics and Computation 399 (2021), 125996, DOI `10.1016/j.amc.2021.125996`. Minimum-norm solutions being orthogonal to the constraint kernel and Gram--Schmidt/Parseval decompositions are standard Hilbert-space facts. No novelty is claimed for those statements in isolation.

A fresh search for Nyman--Beurling work combining recursive pseudoinverse/nullspace innovations with first-free zero interpolation did not locate this formulation. The closest recent Gram-focused work found was Hugh Carvill, *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing*, arXiv:2510.18132 (2025), which studies decay and compressibility of BN generator Gram entries rather than target-aware first-free interpolation or the neutralized null innovations `(1)`. Alouges--Darses--Hillion, *Polynomial approximations in a generalized Nyman--Beurling criterion*, J. Théor. Nombres Bordeaux 34 (2022), 767--785, studies approximation and special Gram structures, again not this sequential first-free nullspace resolution.

The line-local contribution claimed here is therefore deliberately narrow: starting from the exact `NB-285/286` first-free quotient-source problem, identify each legal Dirichlet enrichment with the canonical sample-neutralized direction `(1)`, prove those directions form the orthogonal innovation decomposition `(21)` of the source interpolation kernel, and convert the dynamic target-aligned leverage series into the static Parseval identity `(35)`.

The proof is self-contained once `NB-282`, `NB-284`, `NB-285` and `NB-286` are admitted. The external items above delimit generic prior art but are not load-bearing dependencies, so no new `SOURCES.md` anchor is required.

---

## 8. Research disposition

This finding sharpens rather than closes the finite-section branch. `NB-286` left the next arithmetic task in the data-space quantities

\[
v_{r+1}^*K_r^{-1}v_{r+1}
\quad\text{and}\quad
v_{r+1}^*K_r^{-1}y.
\]

`NB-287` shows that their target-relevant combination is exactly one Fourier coefficient against a canonical unit vector in the source interpolation kernel. The remaining Ford-coupled question can therefore be stated without a changing inverse Gram metric:

\[
\boxed{
\text{control the future Parseval mass }
\sum_{r\ge M_X}
|\langle h_{X,M_X},q_{X,r+1}\rangle|^2.
}
\tag{43}
\]

A useful next step would have to exploit arithmetic structure of the neutralized Dirichlet relations `q_(X,r+1)` strongly enough to estimate `(43)` uniformly in the moving zero packet. Merely proving Gram decay, large/small leverage, or generic conditioning bounds does not settle that target-aware tail.
