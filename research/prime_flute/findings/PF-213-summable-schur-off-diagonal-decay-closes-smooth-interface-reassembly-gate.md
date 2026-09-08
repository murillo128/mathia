# PF-213 — summable Schur off-diagonal decay closes the smooth-interface reassembly gate

**Status:** `EXACT-DERIVED + ABSTRACT-REASSEMBLY + CONDITIONAL-APPLICATION + POSITIVE/BOUNDARY`. PF-212 closes the local low/high boundary-frequency estimates on every canonical PF-205 thin Fermi seam, but deliberately leaves one global obstruction: the energy-normalized exterior Schur complements from PF-211 may mix boundary data between infinitely many prime modules, so the module-dependent `d_n` coefficient cannot be attached after an arbitrary positive contraction. That remaining requirement can now be stated as an exact quantitative locality condition. If the simultaneous normalized Schur complements have module blocks dominated by one off-diagonal envelope `eta_k` satisfying

\[
\boxed{
\sum_{k\in\mathbb Z}\sqrt{(1+|k|)\eta_k}<\infty,
}
\tag{1}
\]

then all boundary-recoupling families isolated in PF-212 reassemble with the required endpoint classes: every term containing a low boundary projection is globally weak trace class, the high/Dirichlet terms are trace class, and the double-high family is globally weak trace class. In particular any uniform exponential block decay `eta_k\le C\rho^{|k|}`, `0<\rho<1`, is sufficient. Conversely, positivity and contractivity alone are genuinely too weak: there is an explicit positive orthogonal projection that funnels one low mode from every tail module into orthogonal directions of one fixed module, after which multiplication by prime-decaying module weights produces a noncompact operator. Thus the smooth-interface gate is no longer an unspecified reassembly problem. It is enough to prove summable off-diagonal locality such as (1), or an equivalent weighted ideal estimate, for the **actual simultaneous PF normalized Schur complement**. No such geometric decay theorem is proved here, and the independent true-short-collar splice remains open.

## Claim

Index the tail modules by the odd primes `p_n`. Use the PF-205/PF-210/PF-212 scales

\[
d_n\le \frac{D}{p_n},
\qquad
L_n\le A(1+\log p_n),
\qquad
w_n\le \frac{B}{p_n},
\tag{2}
\]

where `L_n` is the module-scale seam length and `w_n` the natural Fermi width. Let the simultaneous boundary energy space split orthogonally as

\[
\mathcal B=\bigoplus_{n\ge n_0}\mathcal B_n,
\tag{3}
\]

and write `Q_n` for the module projections. For each of the two native metrics let `D^{(r)}`, `r\in\{g,h\}`, denote the PF-211 energy-normalized exterior factor. Assume only the already established contraction bound

\[
0\le D^{(r)}\le I
\tag{4}
\]

plus the following **new conditional locality hypothesis**: there is one nonnegative two-sided sequence `eta=(eta_k)_{k\in\mathbb Z}` such that

\[
\boxed{
\|Q_mD^{(r)}Q_n\|\le \eta_{m-n}
\quad\text{for all tail }m,n\text{ and }r\in\{g,h\},
}
\tag{5}
\]

and (1) holds. A finite head and a fixed finite coloring are harmless and may be absorbed into constants.

Let `P_{n,lo}` be the fixed-physical-frequency low projection of PF-211/PF-212. Then

\[
\operatorname{rank}P_{n,lo}\le C(1+L_n)
\le C(1+\log p_n).
\tag{6}
\]

For the high projection `P_{n,hi}=I-P_{n,lo}`, PF-212 gives an energy-normalized Poisson factor `M_{n,hi}` with

\[
s_j(M_{n,hi})
\le
\frac{C L_n}{j+c\kappa L_n},
\tag{7}
\]

and a Dirichlet gradient factor `G_{n,D}` satisfying

\[
\|G_{n,D}\|_{\mathcal S_4}
\le C L_n^{1/4}w_n^{3/4}.
\tag{8}
\]

Finally let the seam coefficient remain on its physical middle module, with

\[
\|F_n\|\le C d_n.
\tag{9}
\]

Under (1)--(9), the PF-212 boundary expansion has the following global consequences.

1. **Every boundary word containing at least one low projection belongs to `\mathcal S_{1,\infty}`.** This includes the one-sided low recouplings and the double-low/mixed low-high terms.
2. **Every high/Dirichlet or Dirichlet/high word belongs to `\mathcal S_1`.**
3. **The double-high boundary word belongs to `\mathcal S_{1,\infty}`.**

Therefore condition (1) is sufficient to remove the global Schur-placement/reassembly hypothesis that remained in PF-212. It is not asserted that the canonical PF Schur complements satisfy (5).

## 1. An infinite weak-`S_1` summation lemma

For a compact operator `T`, write

\[
N_T(\sigma)=\#\{j:s_j(T)>\sigma\},
\qquad
q(T)=\sup_{\sigma>0}\sigma N_T(\sigma).
\tag{10}
\]

Suppose compact operators `T_alpha` satisfy

\[
q(T_\alpha)\le q_\alpha
\quad\text{and}\quad
\sum_\alpha \sqrt{q_\alpha}<\infty.
\tag{11}
\]

Then

\[
\boxed{
\sum_\alpha T_\alpha\in\mathcal S_{1,\infty},
\qquad
q\!\left(\sum_\alpha T_\alpha\right)
\le
\left(\sum_\alpha\sqrt{q_\alpha}\right)^2.
}
\tag{12}
\]

Indeed, for a finite subfamily put `A=\sum_\alpha\sqrt{q_\alpha}` and allocate the threshold

\[
\sigma_\alpha
=\sigma\frac{\sqrt{q_\alpha}}{A}.
\tag{13}
\]

The repeated Fan counting inequality gives

\[
N_{\sum T_\alpha}(\sigma)
\le
\sum_\alpha N_{T_\alpha}(\sigma_\alpha)
\le
\frac{A^2}{\sigma}.
\tag{14}
\]

Also `\|T_\alpha\|\le q(T_\alpha)\le q_\alpha`, and (11) implies `\sum q_\alpha<\infty`; hence the infinite sum converges in operator norm. Passing (14) to the norm limit proves (12). This is the device that lets infinitely many off-diagonal bands replace PF-199/PF-210's fixed finite coloring without paying an infinite weak-ideal triangle loss.

## 2. One global mixing: prime-density counting survives each offset

First consider a low-frequency word with one global Schur factor. Suppress bounded Poisson/gradient contractions and write its essential block form as

\[
T=WDP_{lo},
\tag{15}
\]

where `W=\bigoplus_m W_m` is module diagonal with `\|W_m\|\le C/p_m`. Decompose by module offset,

\[
T=\sum_{k\in\mathbb Z}T^{(k)},
\qquad
T^{(k)}
=\sum_n W_{n+k}Q_{n+k}DQ_nP_{n,lo}.
\tag{16}
\]

For fixed `k`, source modules `n` and target modules `n+k` are both orthogonal, so `T^{(k)}` is a literal two-sided block direct sum. Its `n`th block has

\[
\|T_n^{(k)}\|
\le
\frac{C\eta_k}{p_{n+k}},
\qquad
\operatorname{rank}T_n^{(k)}
\le C(1+\log p_n).
\tag{17}
\]

For `k\ge0`, monotonicity gives `\log p_n\le\log p_{n+k}`. For `k=-j<0`, iterated Bertrand gives

\[
p_{m+j}<2^j p_m,
\qquad
\log p_{m+j}\le\log p_m+j\log2.
\tag{18}
\]

At singular-value threshold `sigma`, only target modules with

\[
p_m\le C\eta_k/\sigma
\tag{19}
\]

can contribute. Summing the rank bound before discarding the threshold information and using the same elementary Chebyshev estimate `vartheta(X)=O(X)` as PF-210 gives

\[
\boxed{
N_{T^{(k)}}(\sigma)
\le
\frac{C(1+|k|)\eta_k}{\sigma},
\qquad
q(T^{(k)})\le C(1+|k|)\eta_k.
}
\tag{20}
\]

Condition (1) and the summation lemma now imply `T\in\mathcal S_{1,\infty}`. The adjoint orientation is identical.

The important point is that the global Schur factor need not preserve modules exactly. It may mix infinitely many of them, provided the off-diagonal bands decay fast enough in the precise square-root summability currency (1).

## 3. Two global mixings: every low-containing boundary word remains weak trace class

A double-boundary word has a physical middle module carrying the coefficient. After fixing offsets

\[
b=m-n,
\qquad
a=\ell-m,
\tag{21}
\]

its schematic low-containing block is

\[
T_n^{(a,b)}:
\mathcal H_n\longrightarrow\mathcal K_{\ell},
\qquad
\|T_n^{(a,b)}\|
\le
C\frac{\eta_a\eta_b}{p_m},
\tag{22}
\]

and the presence of at least one low projection makes its rank at most

\[
C(1+\log p_n)
\quad\text{or}\quad
C(1+\log p_\ell).
\tag{23}
\]

For fixed `(a,b)` the source and target modules again form a two-sided direct sum. Iterated Bertrand compares the shifted prime indices, so either version of (23) is bounded by

\[
C(1+\log p_m+|a|+|b|).
\tag{24}
\]

Repeating the threshold count gives

\[
\boxed{
q(T^{(a,b)})
\le
C(1+|a|+|b|)\eta_a\eta_b.
}
\tag{25}
\]

Because

\[
1+|a|+|b|
\le(1+|a|)(1+|b|),
\tag{26}
\]

condition (1) implies

\[
\sum_{a,b}\sqrt{q(T^{(a,b)})}<\infty.
\tag{27}
\]

Equation (12) therefore proves weak trace class for every low-containing two-sided boundary word. This replaces exact module support by summably decaying module transport.

## 4. High/Dirichlet words are still strongly trace summable

For one high boundary factor mixed from module `n` into the physical coefficient/Dirichlet module `m`, put `k=m-n`. PF-212's Schatten-Hölder calculation, with the additional Schur block norm `eta_k`, gives

\[
\|T_{m,n}\|_1
\le
C\eta_k\,d_m\,L_n^{3/4}L_m^{1/4}w_m^{3/4}.
\tag{28}
\]

By (2) and iterated Bertrand,

\[
L_n\le C(1+\log p_m+|k|),
\tag{29}
\]

so for each fixed offset

\[
\sum_m\|T_{m,m-k}\|_1
\le
C(1+|k|)\eta_k
\sum_m\frac{1+\log p_m}{p_m^{7/4}}
<\infty.
\tag{30}
\]

Condition (1) implies `\sum_k(1+|k|)\eta_k<\infty`, because the terms `\sqrt{(1+|k|)\eta_k}` are summable. Hence summing (30) over all offsets proves

\[
\boxed{T_{hi/D},T_{D/hi}\in\mathcal S_1.}
\tag{31}
\]

Thus global module mixing does not reopen the thin-aspect-ratio gate once it has summable off-diagonal decay.

## 5. Double-high words keep PF-212's weak endpoint

The only non-finite-rank boundary word without a Dirichlet factor is the double-high term. Fix offsets `(a,b)` as in (21), so `m=n+b` and `ell=m+a`. PF-212's high Poisson singular-value envelope and the product inequality give

\[
s_{2j-1}(T_n^{(a,b)})
\le
\frac{C\eta_a\eta_b\,d_mL_\ell L_n}
{(j+c\kappa L_\ell)(j+c\kappa L_n)}.
\tag{32}
\]

In particular the top singular value is `O(eta_a eta_b/p_m)`, so a block can contribute at threshold `sigma` only when

\[
p_m\le X:=C\eta_a\eta_b/\sigma.
\tag{33}
\]

Dropping the positive frequency offsets in the denominator of (32) gives the counting bound

\[
N_{T_n^{(a,b)}}(\sigma)
\le
C\sqrt{
\frac{\eta_a\eta_bL_\ell L_n}{p_m\sigma}}
.
\tag{34}
\]

Again `L_n,L_\ell\le C(1+\log p_m+|a|+|b|)`. The Chebyshev estimate used in PF-210/PF-212 and partial summation give

\[
\sum_{p\le X}\frac{1+\log p+s}{\sqrt p}
\le C(1+s)\sqrt X,
\qquad s=|a|+|b|.
\tag{35}
\]

Summing (34) over the two-sided direct sum at fixed offsets therefore yields

\[
\boxed{
q(T^{(a,b)})
\le
C(1+|a|+|b|)\eta_a\eta_b.
}
\tag{36}
\]

The same square-root summation (27) and lemma (12) prove that the complete double-high family is in `\mathcal S_{1,\infty}`. Hence the three local classes in PF-212 survive an infinite global Schur coupling whenever (1) holds.

## 6. Positivity alone can destroy even compactness

PF-211 already gives a finite-dimensional warning that `0\le D\le I` does not preserve a small aligned product. The global reassembly problem admits a sharper exact falsifier.

Let

\[
\mathcal B=\mathcal B_0\oplus\bigoplus_{n\ge1}\mathcal B_n.
\tag{37}
\]

Choose orthonormal vectors `e_n\in\mathcal B_n` and an orthonormal sequence `f_n\in\mathcal B_0`. Let `P` project onto the closed span of the `e_n`, so there is only **one low source mode per tail module**. Put

\[
v_n=\frac{e_n+f_n}{\sqrt2}
\tag{38}
\]

and let `D` be the orthogonal projection onto the closed span of the mutually orthonormal `v_n`. Then

\[
0\le D\le I.
\tag{39}
\]

Let `W` be module diagonal with

\[
W|_{\mathcal B_0}=w_0I,
\qquad
W|_{\mathcal B_n}=w_nI,
\qquad
w_0>0,
\qquad
w_n\to0,
\tag{40}
\]

and one may take `w_n=1/p_n`. Directly,

\[
WDP e_n
=
\frac12(w_ne_n+w_0f_n).
\tag{41}
\]

These images are mutually orthogonal and satisfy

\[
\|WDP e_n\|\ge\frac{w_0}{2}.
\tag{42}
\]

Therefore

\[
\boxed{WDP\text{ is not compact}.}
\tag{43}
\]

The example does not model the geometry of the PF exterior. It proves the narrower point required by the gate: **prime-decaying local weights, logarithmic or even rank-one low sectors, and positivity of the global Schur contraction do not by themselves prevent infinitely many tail modes from being transported into a fixed non-decaying module.** Some quantitative locality, weighted boundedness, or equivalent reassembly structure is mathematically necessary.

## 7. Prior art and novelty audit

No novelty is claimed for weak Schatten ideals, Fan/Ky-Fan counting, direct-sum singular-value counting, Bertrand's postulate, Chebyshev's estimate `vartheta(X)=O(X)`, Schatten Hölder, or elementary block-matrix decompositions. The square-root threshold allocation in (13)--(14) is an elementary way to sum infinitely many weak-`S_1` bands when their endpoint constants have summable square roots.

There is classical prior art for **exponential decay of inverses of banded matrices**. Stephen Demko, William F. Moss and Philip W. Smith, *Decay rates for inverses of band matrices*, Mathematics of Computation **43** (1984), 491--499, DOI `10.1090/S0025-5718-1984-0758197-9`, prove exponential inverse-entry decay with rates controlled by spectral data, including positive-definite cases. Later work extends such decay estimates to tridiagonal and other banded settings. That literature is relevant as a mechanism by which a local, uniformly conditioned precision operator can acquire a decaying inverse.

It does **not** prove (5) for the prime flute. The PF normalized factor

\[
D=\Lambda_Q^{1/2}(\Lambda_Q+\Lambda_E)^{-1}\Lambda_Q^{1/2}
\tag{44}
\]

contains a global exterior Dirichlet-to-Neumann operator; no finding establishes that its module representation is banded, uniformly conditioned in the sense needed by inverse-decay theorems, or even that its off-diagonal blocks decay. Invoking Demko without first proving such a local precision structure would simply rename the missing gate.

The durable project-specific deduction is instead conditional and exact: **any module-decay envelope satisfying (1) is already strong enough to preserve PF-210/PF-212's prime-density weak endpoint through the simultaneous Schur coupling, while positivity alone can fail compactness.** This turns the current global reassembly problem into a falsifiable operator-locality target.

## 8. Falsification and boundary checks

A later adversary can test PF-213 through the following points.

1. The module decomposition in (3) must be the actual simultaneous PF seam decomposition used by the Krein/DtN identity, not a basis chosen after diagonalizing `D`.
2. The off-diagonal estimate (5) must hold uniformly on the tail for the source and target normalized Schur factors. A qualitative statement that `D` is bounded, positive, pseudolocal, or geometrically local is not enough.
3. The coefficient `F_m` must remain attached to its physical middle module. Commuting the prime-decaying weight through the global Schur factor is not permitted.
4. The low rank must stay on the module spectral scale `O(1+\log p_n)` from PF-210/PF-211. Cell-scale rank `O(L_n/w_n)` is still outside this argument.
5. The high singular-value envelope must be the actual PF-212 bound on the canonical thin Fermi strip. If the simultaneous global cut changes that local geometry, (7)--(8) must be revalidated.
6. The summability condition (1), or a quantitatively equivalent weighted ideal estimate, is essential to this proof. Merely showing `\eta_k\to0` does not justify the infinite weak-ideal sum.
7. The positive-contraction example (37)--(43) is an abstract obstruction, not evidence that the PF Schur complement actually has long-range funneling.
8. Nothing here proves the unsmoothed PF-204 cotangent-transport endpoint, the PF-183 true-short-collar splice, wave-operator completeness, a determinant, prime/clone separation, or any RH consequence.

A decisive positive continuation is now concrete: construct the **simultaneous** PF-205 seam cut, write its normalized exterior Schur block matrix in the physical module decomposition, and prove either (5) with an envelope satisfying (1), a finite-range/fixed-color special case, or another weighted estimate that implies the same offset bounds (20), (25), and (36). A decisive negative continuation is equally concrete: exhibit a geometrically forced family of off-diagonal blocks whose transport violates every such summable endpoint budget.

## Consequences for the research line

PF-210 showed that prime density makes module-scale low modes cheaper than absolute weak-mass summation suggests. PF-211 showed that exterior energy normalization removes norm amplification but not cross-module mixing. PF-212 closed the local high-frequency/aspect-ratio estimates and left that mixing as the last smooth-interface boundary gate. PF-213 now supplies the missing abstract bridge: **summably decaying Schur transport is enough, and unrestricted positive transport is not.**

Accordingly, another local cylinder estimate is not the next task on the smooth branch. The remaining decomposition-interface question is a global locality theorem for the actual normalized exterior boundary operator. If that theorem yields (1), the PF-212 boundary reassembly closes; the separate true-short-collar endpoint must still be settled before the full first relative resolvent can be placed in weak trace class.