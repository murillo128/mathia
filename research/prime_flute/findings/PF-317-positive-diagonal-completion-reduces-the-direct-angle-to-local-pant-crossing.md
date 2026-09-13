# PF-317 — positive diagonal completion reduces the direct `L/H` angle to local pant crossing

**Status:** `EXACT-DERIVED + CLASSICAL-CONTRACTION-SANDWICH + PRIME-DENSITY-REDUCTION + POSITIVE/ROUTE-NARROWING`.

PF-315/PF-316 isolate the direct retained-low/high angle

\[
Z_{LH}=J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}
\]

as one of the two independent weak-`S_1` gates for the full physical `P/H` angle. The accepted direct-angle clue asks for a uniform low/high singular-value estimate through the shrinking-collar family. At first sight that looks like a global pseudodifferential/reassembly problem for the complete boundary precision `J`.

The simultaneous seam normalization from PF-214 gives a sharper reduction. In the boundary-energy coordinates used by PF-280/PF-281, the positive precision is

\[
I+K,
\qquad
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\]

where `Q` is the disjoint union of the canonical PF-205 seam strips and `E` is the disjoint union of the one-cusp pant cores. The strip DtN form `\Lambda_Q` is exactly translation invariant in the physical cuff coordinate, so the fixed physical Fourier split commutes with the seam normalization. On every finite PF-311 section, after separating cuff constants `C` from retained nonconstant low modes `L` and physical high modes `H`, the direct nonconstant blocks therefore satisfy

\[
J_{LL}=I_L+K_{LL},
\qquad
J_{LH}=K_{LH},
\qquad
J_{HH}=I_H+K_{HH}.
\]

Consequently

\[
\boxed{
Z_{LH}
=(I_L+K_{LL})^{-1/2}
K_{LH}
(I_H+K_{HH})^{-1/2}.
}
\]

Both diagonal factors are contractions. Hence every singular value of the actual direct angle is bounded by the corresponding singular value of the **seam-energy-normalized pant cross form**:

\[
\boxed{
s_j(Z_{LH})\le s_j(K_{LH}).
}
\]

Same-sector pant energy can only help this sufficient estimate; it does not have to be inverted or localized first.

PF-214 now becomes decisive in a different way. Its normalized exterior precision `K` is exactly block Jacobi in the cuff-module index. Therefore `K_{LH}` is the sum of only three module offsets, and for each fixed offset its local blocks are orthogonal on both source and target sides. Since the retained physical-low space on one module has only `O(1+\log P_n)` dimensions, PF-210 implies the following concrete endpoint criterion:

\[
\boxed{
\|L_{n+r} K H_n\|\le \frac{C}{P_n}
\quad(r=-1,0,1)
\quad\Longrightarrow\quad
Z_{LH}\in\mathcal S_{1,\infty}.
}
\]

Thus the direct-angle route does **not** require a global weak-`S_1` theorem for the full DtN remainder if these three local mixed-frequency pant blocks admit the reciprocal-prime norm bound. The module reassembly and prime-density counting are already automatic.

There is also no shrinking-strip normalization loss hidden in this criterion. PF-234's pointwise comparison of the hyperbolic and flat shifted strip energies holds for every extension, not only equal traces on the two strip faces. Minimizing it for arbitrary two-sided boundary data gives a full two-boundary DtN comparison

\[
(1+w^2)^{-1}\Lambda^0_{L,w}
\le_{\rm form}
\Lambda^{\rm hyp}_{L,w}
\le_{\rm form}
(1+w^2)\Lambda^0_{L,w}.
\]

The flat shifted strip form is completely explicit in physical Fourier modes. For `\mu=\sqrt{1+\xi^2}` its two-face DtN matrix is

\[
\boxed{
\Lambda^0_{L,w}(\xi)
=\mu
\begin{pmatrix}
\coth(2\mu w)&-\operatorname{csch}(2\mu w)\\
-\operatorname{csch}(2\mu w)&\coth(2\mu w)
\end{pmatrix},
}
\]

with symmetric/antisymmetric eigenvalues `\mu\tanh(\mu w)` and `\mu\coth(\mu w)`. Replacing the actual strip energy by this flat model changes a locally normalized pant block by at most

\[
\sqrt{1+w_m^2}\sqrt{1+w_n^2}
=1+O(P_n^{-2})
\]

on adjacent canonical tail modules. Therefore the remaining direct-channel theorem can be attacked in an explicit flat seam-energy normalization without invoking a uniform fixed-domain pseudodifferential calculus on collapsing collars.

PF-215 does not contradict this reduction. Its diverging normalized adjacent hopping is witnessed by **constant-to-constant** pant data, whereas `Z_{LH}` uses nonconstant retained low modes against physical high modes. PF-215 rules out a uniform bound on the complete neighboring block `Q_{n+1}KQ_n`; it does not rule out a reciprocal-prime bound on the much narrower mixed-frequency block `L_{n+1}KH_n` (or the two other allowed offsets). That mixed-frequency estimate is now the local PDE gate.

## Claim

Work first on a finite canonical simultaneous-cut section so that all energy spaces and Galerkin blocks are finite dimensional. Let

\[
\mathcal B=\mathcal C\oplus\mathcal L\oplus\mathcal H
\]

be the PF-311 physical decomposition into cuff constants, retained nonconstant physical-low modes, and physical-high modes. Let

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0
\tag{1}
\]

be PF-214's seam-energy-normalized exterior precision on the same section, and let

\[
\mathcal J:=I+K.
\tag{2}
\]

Because every PF-205 strip metric is independent of the tangential cuff coordinate, `\Lambda_Q` commutes with the physical Fourier projections. Restricting (2) to `\mathcal L\oplus\mathcal H` gives

\[
J_{LL}=I_L+K_{LL},
\qquad
J_{LH}=K_{LH},
\qquad
J_{HH}=I_H+K_{HH}.
\tag{3}
\]

Define the PF-315 direct angle

\[
Z_{LH}:=J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}.
\tag{4}
\]

Then:

1. `I_L+K_{LL}\ge I_L` and `I_H+K_{HH}\ge I_H`, so
   \[
   \|(I_L+K_{LL})^{-1/2}\|\le1,
   \qquad
   \|(I_H+K_{HH})^{-1/2}\|\le1;
   \tag{5}
   \]
2. one has the exact factorization
   \[
   \boxed{
   Z_{LH}
   =(I_L+K_{LL})^{-1/2}
   K_{LH}
   (I_H+K_{HH})^{-1/2};
   }
   \tag{6}
   \]
3. therefore, whenever `K_{LH}` is compact on a finite-section-compatible limiting realization,
   \[
   \boxed{
   s_j(Z_{LH})\le s_j(K_{LH})
   \qquad(j\ge1),
   }
   \tag{7}
   \]
   and the same implication holds for every two-sided symmetric ideal, in particular
   \[
   \boxed{
   K_{LH}\in\mathcal S_{1,\infty}
   \Longrightarrow
   Z_{LH}\in\mathcal S_{1,\infty}.
   }
   \tag{8}
   \]

No upper comparison between the full diagonal precision and the seam energy is required. Equation (7) uses only positivity of the added same-sector blocks.

### Exact three-offset localization of `K_{LH}`

Let `Q_n` denote PF-214's cuff-module projection, and set

\[
L_n:=LQ_n,
\qquad
H_n:=HQ_n.
\tag{9}
\]

PF-214 proves at form level

\[
Q_mKQ_n=0
\qquad(|m-n|>1).
\tag{10}
\]

Hence

\[
\boxed{
K_{LH}
=\sum_{r=-1}^{1}B^{(r)},
\qquad
B^{(r)}:=\sum_n L_{n+r}KH_n.
}
\tag{11}
\]

For fixed `r`, the source spaces `H_n\mathcal B` are mutually orthogonal and the target spaces `L_{n+r}\mathcal B` are mutually orthogonal. Thus, whenever the local form blocks extend boundedly,

\[
B^{(r)}=\bigoplus_n B_n^{(r)},
\qquad
B_n^{(r)}:=L_{n+r}KH_n
\tag{12}
\]

is a literal two-sided orthogonal direct sum.

At fixed physical cutoff `\kappa`, elementary Fourier counting on the one-dimensional artificial boundary gives

\[
\operatorname{rank}B_n^{(r)}
\le \dim L_{n+r}\mathcal B
\le C_\kappa(1+L_{n+r}),
\tag{13}
\]

where `L_m` here denotes the total relevant boundary length of module `m`. The prime-flute cuff law gives

\[
L_m=O(1+\log P_m).
\tag{14}
\]

Adjacent prime labels are comparable after a finite head, so the exact PF-210 counting theorem applies. If

\[
\boxed{
\|B_n^{(r)}\|
\le \frac{C}{P_n}
\qquad
(r=-1,0,1)
}
\tag{15}
\]

uniformly in the finite geometric/Galerkin section, then

\[
B^{(r)}\in\mathcal S_{1,\infty}
\qquad(r=-1,0,1),
\tag{16}
\]

and therefore, by the finite-sum weak-ideal inequality,

\[
\boxed{
K_{LH}\in\mathcal S_{1,\infty}
\quad\text{and hence}\quad
Z_{LH}\in\mathcal S_{1,\infty}.
}
\tag{17}
\]

Equivalently the singular counting function obeys

\[
\boxed{
N_{Z_{LH}}(a)\le \frac{C'}{a}
}
\tag{18}
\]

with a constant independent of the canonical truncation.

The condition (15) is sufficient, not asserted necessary. A finer local singular-value estimate could also close (18) even if a block norm decays more slowly.

## 1. Same-sector positive completion is harmless for this sufficient direction

Equation (6) is the entire algebraic point. Write

\[
A_L=(I_L+K_{LL})^{-1/2},
\qquad
A_H=(I_H+K_{HH})^{-1/2}.
\]

By positivity these are contractions, and

\[
Z_{LH}=A_LK_{LH}A_H.
\]

The standard two-sided singular-value inequality gives

\[
s_j(A_LK_{LH}A_H)
\le \|A_L\|\,s_j(K_{LH})\,\|A_H\|
\le s_j(K_{LH}).
\]

This is a classical contraction sandwich, not a new operator-theory theorem. Its value here is representational: the difficult square roots in the **actual** diagonal blocks never need to be expanded, localized, or approximated to obtain a sufficient direct-angle estimate. Their only role in (6) is contractive.

This is stronger for the present purpose than trying first to prove a two-sided comparison `J\asymp J_0`. Such a comparison would spend effort controlling diagonal pant reservoirs that can only improve the upper singular-value bound in (7).

## 2. The simultaneous cut makes reassembly finite before any PDE estimate

PF-214's block-Jacobi identity is a support theorem, not a decay theorem. The complement of all seam strips is a disjoint chain of pant cores; each pant core touches only two consecutive cuff modules. Conjugation by `\Lambda_Q^{-1/2}` preserves module support because `\Lambda_Q` is module diagonal. That proves (10).

Taking an `L/H` corner cannot enlarge support. Splitting by the offset `r=m-n` therefore gives exactly the three families in (11). For each fixed offset, no additional coloring is needed: each source module and each target module occurs once. The only global arithmetic input is then PF-210's threshold count on the low target rank.

This point matters because the accepted direct-angle clue originally asked for a global truncation-independent singular-value law after local modeling. For this channel, **global placement is already solved by topology** once the local mixed blocks themselves are bounded at the correct reciprocal-prime scale. The unresolved theorem is local in one pant plus its two adjacent seam-energy normalizers.

## 3. PF-234 extends from the symmetric branch to the full two-face strip form

PF-234 proves for every extension `u` on the Fermi-area rectangle `(-w,w)\times(\mathbb R/L\mathbb Z)` that

\[
(1+w^2)^{-1}\mathfrak e_w^0[u]
\le
\mathfrak e_w^{\rm hyp}[u]
\le
(1+w^2)\mathfrak e_w^0[u].
\tag{19}
\]

PF-234 only needed to record the equal-trace symmetric branch. But (19) holds before boundary data are specialized. For arbitrary two-face traces `\phi=(\phi_-,\phi_+)`, take the infimum over all extensions with those traces. This gives the full DtN-form comparison

\[
\boxed{
(1+w^2)^{-1}\Lambda^0_{L,w}
\le_{\rm form}
\Lambda^{\rm hyp}_{L,w}
\le_{\rm form}
(1+w^2)\Lambda^0_{L,w}.
}
\tag{20}
\]

For a Fourier mode `e^{i\xi s}`, put `\mu=\sqrt{1+\xi^2}`. Solving the one-dimensional flat equation on `(-w,w)` gives

\[
\boxed{
\Lambda^0_{L,w}(\xi)
=\frac{\mu}{\sinh(2\mu w)}
\begin{pmatrix}
\cosh(2\mu w)&-1\\
-1&\cosh(2\mu w)
\end{pmatrix}.
}
\tag{21}
\]

Its symmetric and antisymmetric face eigenvalues are respectively

\[
\mu\tanh(\mu w),
\qquad
\mu\coth(\mu w).
\tag{22}
\]

Let `\widetilde B_{mn}` be the pant `L/H` cross form normalized by the flat strip energies on its source and target modules, and `B_{mn}` the same cross form normalized by the actual hyperbolic strip energies. Form order in (20) yields contraction/factorization maps with

\[
\boxed{
\|B_{mn}\|
\le
\sqrt{1+w_m^2}\sqrt{1+w_n^2}
\,\|\widetilde B_{mn}\|.
}
\tag{23}
\]

The same inequality holds singular-value by singular-value whenever the flat-normalized block is compact. On the canonical PF-205 tail

\[
w_n=O(P_n^{-1}),
\tag{24}
\]

so for `|m-n|\le1`,

\[
\sqrt{1+w_m^2}\sqrt{1+w_n^2}
=1+O(P_n^{-2}).
\tag{25}
\]

Therefore a proof of

\[
\boxed{
\|\widetilde B_{n+r,n}\|
\le \frac{C}{P_n},
\qquad r=-1,0,1,
}
\tag{26}
\]

in the explicit flat shifted-strip normalization is already enough for (15)--(18). The collapsing physical strip does not introduce an additional normalization constant.

## 4. Why PF-215's divergent hopping does not settle the mixed block

PF-215 proves

\[
\|Q_{n+1}KQ_n\|
\gtrsim
\frac{P_n^{1.475}}{\log P_n}
\]

when the full adjacent block has a bounded realization. The witness is the symmetric **constant** strip mode: opposite constant values across the thin pant corridor cost `\gtrsim s_n^{-1}` exterior energy while the strip energy of a constant symmetric trace is tiny.

That witness lies in the `C/C` channel removed before `Z_{LH}` is formed. It gives no lower bound on

\[
L_{n+r}KH_n.
\]

Conversely, PF-215 means one must not try to prove (26) by bounding the complete pant block first; that larger statement is false. The required estimate must exploit actual frequency separation between retained nonconstant low modes and physical high modes.

This is compatible with PF-212/PF-255: the seam model itself is exactly Fourier diagonal, and the prime-dependent hypercycle transport has a two-derivative high-to-low barrier. Those facts make (26) plausible as a sharply targeted PDE estimate, but they do not prove it for the finite pant completion.

## Prior-art and novelty audit

The singular-value contraction sandwich in (7) is standard operator-ideal algebra; it is closely aligned with classical Douglas-type factorization/order arguments, and no novelty is claimed for it. The flat two-face DtN matrix (21) is elementary separation of variables. PF-210's prime-density threshold count and PF-214's block-Jacobi support are already established project results.

The fixed-geometry DtN literature recorded in the accepted direct-angle clue remains relevant background for attacking a local block, but it is not needed to justify the reduction above. In particular, a generic fixed-domain pseudodifferential remainder theorem would be a much stronger and less scale-transparent input than (26).

The project-specific new content is the combination of the existing structures: the PF-315 direct angle is contractively dominated by the seam-normalized exterior `L/H` cross form; PF-214 makes that form exactly three-offset local; PF-210 turns a reciprocal-prime local norm bound plus logarithmic low rank into the full weak-`S_1` endpoint; and PF-234 removes any extra loss from replacing the actual shrinking strip energy by an explicit flat model. No claim is made that the remaining local pant estimate (26) is known in the literature or proved here.

## Consequence for the research line

The direct-angle frontier is now narrower than the accepted clue originally stated. A successful positive argument need not build a global principal/remainder calculus for `J`, control same-sector Schur reservoirs, or prove a separate global reassembly theorem. It is enough to prove the **three local flat-seam-normalized mixed-frequency bounds** (26), or another local singular-value estimate strong enough to imply PF-210's threshold count.

The next decisive calculation should therefore be performed on one actual one-cusp pant core with its two PF-205 artificial boundaries. Normalize its `L/H` cross form by the explicit flat shifted-strip matrix (21), keep the fixed physical cutoff, and determine whether the three allowed module offsets have norm `O(P_n^{-1})`. PF-215 says the corresponding all-frequency block is enormous, so any positive proof must visibly use low/high frequency separation rather than absolute pant-energy size.