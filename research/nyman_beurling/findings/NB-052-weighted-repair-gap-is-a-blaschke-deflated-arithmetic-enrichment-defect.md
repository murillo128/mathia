# NB-052 — weighted repair gap is a Blaschke-deflated arithmetic enrichment defect

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + PRIOR-ART-CLASSICALIZATION + FINITE-DEBLASCHKE-IDENTITY + TWO-SCALE-REPAIR-NORMAL-FORM`. `NB-050` identifies the recursively repaired weighted-skeleton slack with the finite target-enrichment gap

\[
\widetilde d_{M,N}^2-d_N^2
=
\frac{d_K^2-\delta_{M,N}^2}{M},
\qquad
K=\left\lfloor\frac NM\right\rfloor,
\tag{1}
\]

between the reciprocal-integer section `V_K` and the denser continuous-parameter grid

\[
\mathcal C_{M,N}
=
\operatorname{span}\{\rho_{M/n}:M<n\le N\}.
\tag{2}
\]

`NB-051` then shows that, when `M -> infinity` and `N/M -> infinity`, the numerator tends to the closure-level target gap

\[
\Delta_*=d_{\mathrm{nat}}^2-d_{\mathrm{cont}}^2.
\tag{3}
\]

The present result gives that quantity, and already every finite numerator in (1), an exact Hardy-space normal form. Burnol's classical Blaschke factorization removes the common off-critical-zero obstruction from **both** finite spaces. After that common factor is divided out, the `NB-050` numerator is exactly a difference of ordinary target distances between two deflated arithmetic subspaces. Consequently the rigid Blaschke zero floor cancels from the weighted repair comparison at every finite `(M,N)`.

Let

\[
\mathcal H^2:=H^2(\Re s>1/2),
\qquad
k_1(s):=\frac1s,
\tag{4}
\]

with the Mellin normalization used by Burnol. Let `B` be the Blaschke product over the zeros `rho` of `zeta` with `Re rho>1/2`, normalized so that `B(1)>0`. Burnol proves that the Mellin transform of the full continuous Nyman closure is exactly

\[
B\mathcal H^2,
\tag{5}
\]

and that

\[
P_{B\mathcal H^2}k_1
=
B(1)\frac{B(s)}s.
\tag{6}
\]

In particular

\[
\boxed{
d_{\mathrm{cont}}^2=1-B(1)^2,
}
\tag{7}
\]

with

\[
B(1)^2
=
\prod_{\substack{\zeta(\rho)=0\\\Re\rho>1/2}}
\left|\frac{1-\rho}{\rho}\right|^{2m_\rho}.
\tag{8}
\]

For `0<theta<1`, put

\[
\psi_\theta(s)
:=
\widehat{\rho_\theta}(s)
=
\frac{\theta-\theta^s}{s}\zeta(s),
\qquad
\phi_\theta(s):=\frac{\psi_\theta(s)}{B(s)}.
\tag{9}
\]

Define the deflated finite spaces

\[
\mathcal A_K
:=
\operatorname{span}\{\phi_{1/j}:2\le j\le K\},
\tag{10}
\]

and

\[
\mathcal D_{M,N}
:=
\operatorname{span}\{\phi_{M/n}:M<n\le N\}.
\tag{11}
\]

Because `V_K subseteq C_(M,N)`, one has `A_K subseteq D_(M,N)`. Then the exact finite identity is

\[
\boxed{
d_K^2-\delta_{M,N}^2
=
B(1)^2
\left(
\operatorname{dist}(k_1,\mathcal A_K)^2
-
\operatorname{dist}(k_1,\mathcal D_{M,N})^2
\right).
}
\tag{12}
\]

Combining (12) with `NB-050` yields

\[
\boxed{
M\bigl(\widetilde d_{M,N}^2-d_N^2\bigr)
=
B(1)^2
\left(
\operatorname{dist}(k_1,\mathcal A_K)^2
-
\operatorname{dist}(k_1,\mathcal D_{M,N})^2
\right).
}
\tag{13}
\]

Thus the weighted repair does **not** compare two copies of the rigid zero obstruction. That component is common and cancels identically. What remains is an arithmetic enrichment defect after common inner-factor removal.

## 1. Burnol splits the common zero obstruction orthogonally

Burnol's Mellin formula is

\[
\widehat{\rho_\theta}(s)
=
\frac{\theta-\theta^s}{s}\zeta(s).
\tag{14}
\]

His Beurling--Lax argument identifies the closed continuous Nyman space with `B H^2` and gives (6). Set

\[
g(s):=\frac{B(1)}s,
\qquad
u:=k_1-Bg.
\tag{15}
\]

Equation (6) is exactly the statement

\[
\nu\perp B\mathcal H^2.
\tag{16}
\]

Multiplication by the inner function `B` is an isometry on `H^2`, and `||k_1||=1`. Hence

\[
\|\nu\|^2
=1-\|Bg\|^2
=1-B(1)^2
=d_{\mathrm{cont}}^2.
\tag{17}
\]

Now let `E` be any closed subspace of `H^2`. Since `BE subseteq B H^2`, for every `a in E`,

\[
\begin{aligned}
\|k_1-Ba\|^2
&=\|\nu+B(g-a)\|^2\\
&=\|\nu\|^2+\|g-a\|^2.
\end{aligned}
\tag{18}
\]

Taking the infimum gives the general exact identity

\[
\boxed{
\operatorname{dist}(k_1,BE)^2
=
d_{\mathrm{cont}}^2
+
\operatorname{dist}(g,E)^2.
}
\tag{19}
\]

This is the only Hilbert-space mechanism needed below. It is classical inner-factor projection geometry, not a new Nyman theorem.

## 2. The finite `NB-050` enrichment loses the rigid term exactly

The Mellin image of the discrete section `V_K` is

\[
B\mathcal A_K,
\tag{20}
\]

while the Mellin image of the finite continuous grid `C_(M,N)` is

\[
B\mathcal D_{M,N}.
\tag{21}
\]

Applying (19) twice gives

\[
d_K^2
=
d_{\mathrm{cont}}^2
+
\operatorname{dist}(g,\mathcal A_K)^2,
\tag{22}
\]

and

\[
\delta_{M,N}^2
=
d_{\mathrm{cont}}^2
+
\operatorname{dist}(g,\mathcal D_{M,N})^2.
\tag{23}
\]

Subtracting cancels `d_cont^2` exactly:

\[
\boxed{
d_K^2-\delta_{M,N}^2
=
\operatorname{dist}(g,\mathcal A_K)^2
-
\operatorname{dist}(g,\mathcal D_{M,N})^2.
}
\tag{24}
\]

Since `g=B(1) k_1` and the spaces are linear, (24) is precisely (12).

This finite cancellation is useful conceptually. `NB-051` introduced `Delta_*` as a difference between two target projections. Burnol's factorization shows that the portion forced solely by zeros to the right of the critical line is **identical on both sides of that comparison**. The weighted repair slack measures only how much better the denser deflated grid captures the remaining Hardy target than the deflated reciprocal-integer grid.

The same factorization can be written using Burnol's outer factor

\[
O(s):=
\frac{s-1}{s}\frac{\zeta(s)}{B(s)}.
\tag{25}
\]

Then

\[
\phi_\theta(s)
=
O(s)\frac{\theta-\theta^s}{s-1}.
\tag{26}
\]

For the natural family,

\[
\mathcal A_{\mathrm{nat}}
:=
\overline{\operatorname{span}}
\{\phi_{1/j}:j\ge2\}
=
\overline{\operatorname{span}}
\left\{
O(s)\frac{j^{-1}-j^{-s}}{s-1}:j\ge2
\right\}.
\tag{27}
\]

Equation (27) should not be read as making the problem zero-free or source-computable: `O` itself contains the deflation by `B`. It only isolates which factor is common to the continuous and natural target problems.

## 3. `Delta_*` is exactly the infinite deflated arithmetic defect

Define

\[
\delta_{\mathrm{def}}
:=
\operatorname{dist}(k_1,\mathcal A_{\mathrm{nat}}).
\tag{28}
\]

Applying (19) to the natural closure gives

\[
d_{\mathrm{nat}}^2
=
d_{\mathrm{cont}}^2
+B(1)^2\delta_{\mathrm{def}}^2.
\tag{29}
\]

Therefore

\[
\boxed{
\Delta_*
=d_{\mathrm{nat}}^2-d_{\mathrm{cont}}^2
=B(1)^2\delta_{\mathrm{def}}^2.
}
\tag{30}
\]

Equivalently,

\[
\boxed{
d_{\mathrm{nat}}^2
=
1-B(1)^2
+B(1)^2\delta_{\mathrm{def}}^2.
}
\tag{31}
\]

Now take any two-scale sequence from `NB-051`,

\[
M_r\to\infty,
\qquad
N_r/M_r\to\infty.
\tag{32}
\]

That finding proves

\[
M_r\bigl(\widetilde d_{M_r,N_r}^2-d_{N_r}^2\bigr)
\longrightarrow
\Delta_*.
\tag{33}
\]

Substituting (30) gives the sharpened repair normal form

\[
\boxed{
M_r\bigl(\widetilde d_{M_r,N_r}^2-d_{N_r}^2\bigr)
\longrightarrow
B(1)^2\delta_{\mathrm{def}}^2.
}
\tag{34}
\]

There is also a direct deflated reading of the `NB-051` convergence. Since `K_r -> infinity`,

\[
\operatorname{dist}(k_1,\mathcal A_{K_r})
\longrightarrow
\delta_{\mathrm{def}},
\tag{35}
\]

while the sampled spaces `D_(M_r,N_r)` become dense enough in `H^2` for the particular target `k_1` that

\[
\operatorname{dist}(k_1,\mathcal D_{M_r,N_r})
\longrightarrow0.
\tag{36}
\]

Equations (12), (35), and (36) recover (30) from the finite enrichment identity. The apparent continuous-versus-natural target gap is therefore the asymptotic residual of the reciprocal-integer family **after the common Blaschke obstruction has been divided out**.

Two cautions are essential. First,

\[
\Delta_*=0
\tag{37}
\]

does not by itself imply RH. If off-critical zeros exist, it remains logically possible that `delta_def=0`; the deflated natural family could be dense for the target while `B(1)<1`. Second, the identity does not make `delta_def` a cheap arithmetic observable. Constructing the deflated family explicitly requires the same Blaschke factor carrying the off-critical zeros unless another source-side formula bypasses it.

## 4. Prior-art boundary and consequence for the live bridge

The common inner-factor mechanism is classical. Jean-François Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis* (Contemporary Mathematics 287, 2001; arXiv:math/9910055), proves (5)--(8) and the projection formula (6). Those statements are load-bearing prior art and are not claimed as Mathia discoveries.

A particularly close contemporary boundary is T. A. Ziad, *A Gram-Spectral Autopsy of the BNBD Inversion Problem* (Zenodo preprint, 18 May 2026, DOI `10.5281/zenodo.20277868`). That work explicitly advertises an orthogonal split of the finite BNBD inversion problem into a rigid Blaschke skeleton and an arithmetic Gram projection defect with zero cross-term. Accordingly, **the de-Blaschke orthogonal splitting itself and the interpretation of the remainder as an arithmetic projection defect are not claimed new here**.

The line-local mathematical delta is narrower: `NB-050` independently produced the weighted-tail finite-grid repair identity, and `NB-051` independently produced its two-scale limit `Delta_*`. Equations (12)--(13) identify the exact finite weighted-repair numerator with a **deflated enrichment gain**, while (34) identifies the `NB-051` first-order repair limit with the infinite deflated arithmetic defect. This classicalizes part of the previous interpretation and removes one tempting but false direction: the repair limit is not an additional zero-obstruction beyond Burnol's Blaschke factor.

The surviving source-to-target question is consequently sharper. A useful theorem must control

\[
\delta_{\mathrm{def}}
\quad\text{or its finite difference}\quad
\operatorname{dist}(k_1,\mathcal A_K)^2
-
\operatorname{dist}(k_1,\mathcal D_{M,N})^2
\tag{38}
\]

from source-visible data without assuming `B`, the full target projection, `d_N`, or an equivalent RH-sensitive oracle as input. The localized directional signal from `NB-045`--`NB-049` remains potentially relevant, but it now has to constrain a specifically **Blaschke-deflated arithmetic occupation defect**, not an opaque continuous-versus-natural projection gap.

This is a stricter target than merely proving another continuous-grid convergence theorem. Conversely, a proof that the deflated defect cannot be accessed without reconstructing `B` or equivalent target information would close the present repair route more decisively. No such positive or negative source bridge is proved here.