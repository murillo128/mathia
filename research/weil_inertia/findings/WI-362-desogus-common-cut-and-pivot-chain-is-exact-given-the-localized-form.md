# WI-362 — Desogus's common-cut and inherited-pivot chain is exact given the localized one-cell form

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIMARY-SOURCE-INDEPENDENT-ANALYTIC-AUDIT + PARTIAL-GATE-VALIDATION + NON-ESTABLISHED-RH`.

## Claim

The common-complement/no-double-spend part of Marco Desogus's Gate II argument in **The Three Gates: A Rooted-Operator Approach to Weil Positivity** (`arXiv:2609.20367v1`, 17 Sep 2026) survives an independent analytic reconstruction **once the exact normalized one-cell form used by the paper is granted**. In particular, the chain

\[
\text{coherent source capacity}
\;\longrightarrow\;
\text{one common ground/transverse short}
\;\longrightarrow\;
\text{one-defect ground lower model}
\;\longrightarrow\;
\text{inherited-pivot surplus}
\]

can be derived without allocating the same Cauchy--Carleman reserve twice.

This materially narrows the first two audit gates in WI-361. The source-capacity/common-infimum subgate is not where an immediate contradiction appears: the source-source terms exactly replace the portions of a one-source complement charge occupied by other source intervals, while the later baseline/residual split keeps the slot-ground and within-slot transverse budgets in one and the same variational short. Monotonicity of that same short then transfers the one-defect lower form to the exact inherited pivot.

The result is deliberately narrower than the preprint's main theorem. This audit does **not** independently establish the upstream identification of the normalized cell form with the complete zeta Weil operator at every step, the later common-cut/fold intertwining on the exact harmonic vector, the `Y=7` interval base, the finite MASTER sweeps, the aligned-penalty analytic tail, or RH. Those remain separate load-bearing gates.

## 1. Exact source-capacity reconstruction

The normalized one-cell boundary/collar form used by the preprint is

\[
\mathfrak b[u]
=
\frac14\iint_{(0,1)^2}
\frac{|u(x)-u(y)|^2}{|x-y|}\,dx\,dy
-
\frac12\int_0^1\log(x(1-x))|u(x)|^2\,dx.
\tag{1}
\]

Consider pairwise disjoint source intervals

\[
I_\nu=(a_\nu,a_\nu+\varepsilon)\Subset(0,1)
\]

of one common length, with prescribed mean-zero data `f_ν`. The nontrivial issue is that minimizing each source against an independent complement would reuse the same positive complement reserve. The paper instead keeps one common extension `u` and proves the estimate before taking any infimum.

The two-source inequality needed for that accounting is exact. After rescaling two slots to `(0,1)` and writing their separation as `D>=1`, define

\[
E_D(f,g)=\int_0^1\!\!\int_0^1
\frac{|f(s)-g(t)|^2}{D+t-s}\,ds\,dt,
\qquad
c_D=\log\frac{D+1}{D}.
\tag{2}
\]

For mean-zero `f,g`, the Laplace representation

\[
\frac1{D+t-s}
=
\int_0^\infty e^{-Du}e^{us}e^{-ut}\,du
\]

reduces the mixed kernel to a product of two mean-zero Laplace increments. Weighted Cauchy--Schwarz, followed by AM--GM, gives

\[
E_D(f,g)\ge c_D\bigl(\|f\|_2^2+\|g\|_2^2\bigr).
\tag{3}
\]

The scaling back to intervals of length `ε` is consistent: the pair energy acquires one factor `ε`, exactly as do the physical `L^2` norms, so no extra power of `ε` is lost.

For one source `I_ν`, the internal difference energy contributes at least

\[
\frac12\|f_\nu\|_2^2.
\tag{4}
\]

The free region to the left and right supplies the one-source logarithmic complement charges. Whenever a piece of that nominal complement is occupied by another source interval `I_μ`, (3) supplies exactly the missing charge from both sides:

\[
\frac12c_{\nu\mu}
\bigl(\|f_\nu\|_2^2+\|f_\mu\|_2^2\bigr),
\qquad
c_{\nu\mu}
=
\log\frac{a_\mu+\varepsilon-a_\nu}{a_\mu-a_\nu}.
\tag{5}
\]

Thus the source-free pieces and each source-source pair reconstruct, for every source separately, the full complement charge

\[
\frac12
\left[
\log\frac{a_\nu+\varepsilon}{\varepsilon}
+
\log\frac{1-a_\nu}{\varepsilon}
\right]
\|f_\nu\|_2^2.
\tag{6}
\]

The endpoint potential contributes

\[
-\frac12
\log\bigl((a_\nu+\varepsilon)(1-a_\nu)\bigr)
\|f_\nu\|_2^2,
\tag{7}
\]

which cancels all dependence on `a_ν`. Combining (4), (6), and (7) yields

\[
\boxed{
\mathfrak b[u]
\ge
\left(\log\frac1\varepsilon+\frac12\right)
\sum_\nu\|f_\nu\|_2^2.
}
\tag{8}
\]

Crucially, (8) holds for **every one common extension** `u`. Taking one infimum over the actual common complement therefore gives the simultaneous short; there is no step in which separate source minimizers are added.

For the true arithmetic source intervals in a fixed parent cell `C_m`, the logarithmic normalization gives common length

\[
\varepsilon_{k,m}=\frac{w_k}{w_m},
\qquad
w_j=\log(1+1/j),
\tag{9}
\]

and distinct `n` give disjoint intervals. Different parent cells are orthogonal. Hence this local common-extension statement applies parent by parent without identifying distinct physical source intervals.

## 2. Free source means do not reopen double spending

The later MASTER argument needs the slot-ground component and the within-slot mean-zero component simultaneously. The paper handles this by the exact split

\[
\mathfrak b=\mathfrak l_0+\mathfrak r,
\qquad
\mathfrak r\ge0,
\tag{10}
\]

where

\[
L_0
=
\beta_0 I-\frac12|\mathbf1\rangle\langle\mathbf1|,
\qquad
\beta_0=\log2+\frac12.
\tag{11}
\]

The residual estimate may be reconstructed with arbitrary source means. Writing `f_{ν,0}` for the mean-zero part on each source slot, one gets

\[
\mathfrak r[u]
\ge
\sum_\nu
\left(
\log\frac1{2\varepsilon}-\Delta_\nu
\right)
\|f_{\nu,0}\|_2^2,
\tag{12}
\]

with

\[
\Delta_\nu
=
\frac12\sum_{\mu\ne\nu}\delta_{D_{\nu\mu}},
\qquad
\delta_D
=
\log\frac{D+1}{D}-\frac1{D+1}.
\tag{13}
\]

The universal constant used by the paper is independently transparent. Since ordered disjoint equal slots satisfy `D_{νμ}>=|ν-μ|` and `δ_D` decreases,

\[
\Delta_\nu
\le
\sum_{j\ge1}\delta_j.
\]

But the series telescopes against the harmonic numbers:

\[
\sum_{j=1}^{N}\delta_j
=
\log(N+1)-H_{N+1}+1
\longrightarrow
1-\gamma
=0.422784335\ldots
<0.422785=:d_0.
\tag{14}
\]

So the residual bound with free means is valid with the printed rational decimal safety constant.

Now take the **same** common-complement infimum. The residual term in (12) depends only on prescribed source data and therefore passes unchanged through that infimum. The exact short of `L_0` contributes the slot-ground matrix `D^{(0)}_{k,m}` and contributes `β_0 I` on the orthogonal within-slot mean-zero sector. Hence, in one operation,

\[
\boxed{
\mathfrak C^{\rm short}_{k,m}
\succeq
D^{(0)}_{k,m}|_{\mathcal G_m}
\oplus
\bigoplus_n
\left(
\frac12+\log\frac1{\varepsilon_{k,m}}-d_0
\right)Q_{k,n}.
}
\tag{15}
\]

This is the relevant no-double-spend fact. The ground budget comes from `l_0`; the extra transverse capacity comes from the disjoint residual `r`; both are established before a single common infimum. They are not two lower bounds separately extracted from the same reserve and then added afterwards.

## 3. The one-defect lower model transfers to the exact inherited pivot

The exact short of the baseline operator (11) over the complement of the union of `M` equal slots is elementary rank-one Schur algebra. In the normalized slot-ground basis it is

\[
D^{(0)}_{k,m}
=
\beta_0 I-q_{k,m}|u_m\rangle\langle u_m|,
\qquad
q_{k,m}
=
\frac{\beta_0\varepsilon_{k,m}}
{2\log2+M_m\varepsilon_{k,m}},
\tag{16}
\]

and, because the occupied length `M_m ε_{k,m}` is at most one,

\[
0\le q_{k,m}M_m\le\frac12.
\tag{17}
\]

No separate theorem about operator shorts is needed for the order transfer used next. If two quadratic forms satisfy `Q(x,y)>=Q_0(x,y)` for every extension variable `y`, then for every prescribed `x`

\[
\inf_y Q(x,y)
\ge
\inf_y Q_0(x,y).
\tag{18}
\]

Thus the pointwise lower-form order `b>=l_0` survives the same common-complement short. A further short of the mismatch space also preserves it by the identical variational argument. Consequently the surviving exact inherited-line pivot satisfies

\[
\boxed{
P^{\rm ex}_{k,m}\ge\Pi_m^{(0)}>0.
}
\tag{19}
\]

The actual and reference inherited source vectors are collinear,

\[
r_m=\theta_{k,m}r_m^0,
\qquad 0<\theta_{k,m}<1,
\tag{20}
\]

so (19) produces the exact comparator surplus

\[
\mathscr S^{\rm ex}_{k,m}[r_m^0]
-
\mathscr S^{\rm ex}_{k,m}[r_m]
\ge
\Pi_m^{(0)}C_m
(\varepsilon_{k,m}^2-\kappa_{k,m})
>0.
\tag{21}
\]

This establishes the inherited-pivot lower bound from the same common-cut metric; it does not introduce an independent positive reserve after the source short.

## 4. The printed mixed constant and response-placement algebra check out

The numerical-looking coefficient `189/250` in the next local step is actually backed by a comfortable analytic margin. With the notation of the preprint, Sherman--Morrison gives

\[
\frac{\rho_m}{\Pi_m^{(0)}}
=
\frac{q^2a^2h}{\beta_0N}.
\]

Using `q<=1/(2M)`, `N>=log 2`, and `v=h/M` gives

\[
\frac{\rho_m}{\Pi_m^{(0)}}
\le
\frac{v(1-v)}{4\beta_0\log2}
\le
\frac{v}{4\beta_0\log2}.
\tag{22}
\]

Popoviciu's inequality on the values `sqrt(n)` in one parent class yields

\[
v
\le
\frac14
\left(\sqrt{1+\frac1m}-1\right)^2.
\tag{23}
\]

For an active parent `k>=2m+1`, so `w_k<w_m/2`; the monotonicity used by the paper then gives

\[
1-\theta_{k,m}^2
>
\tanh^2(w_m/4).
\]

Combining this with `w_m<=log2` gives

\[
\frac{\rho_m}{\Pi_m^{(0)}}
<
c_*(1-\theta_{k,m}^2),
\qquad
c_*
=
\frac{3+2\sqrt2}
{16(\log2+\tfrac12)\log2}
=0.4404655103\ldots
<\frac{189}{250}.
\tag{24}
\]

The later homogeneous Young estimate needs the slightly different comparison

\[
\frac53c_*=0.7341091839\ldots
<\frac{189}{250}=0.756,
\tag{25}
\]

which also holds with margin. Cauchy--Schwarz in the inverse mismatch metric then gives the advertised positive `2x2` mixed block.

The response-placement identity itself is also exact **once one is on the surviving inherited line**. If the reduced quadratic is

\[
P^{\rm ex}|a|^2-2\operatorname{Re}(\bar a\,\omega)+\text{rest},
\]

its Schur minimizer satisfies `P^{ex}a=ω`; the source-coupling contribution is therefore precisely the negative metric energy `-P^{ex}|a|^2`. Because `r_m=θr_m^0` in that same one-dimensional metric, the comparator term in (21) is a decomposition of this very debit, not an unrelated positive term added later.

Finally, splitting

\[
A_m=(1-\theta^2)\Pi_m^{(0)}
=\frac35A_m+\frac25A_m
\]

and applying Young separately to the perpendicular and aligned forcing gives exactly

\[
-\left(\frac{439}{250}\chi_m+\frac52W_{k,m}\right)|\gamma|^2.
\tag{26}
\]

Thus the local constants and homogeneity used after the inherited-pivot step do not expose an algebraic failure.

## 5. What this audit closes and what remains open

This finding validates the following **internal analytic subchain** of the recent preprint:

- the mean-zero pair capacity and its scaling to true equal-length source intervals;
- reconstruction of missing one-source complement charge by source-source interactions;
- use of one common complement rather than independent source minimizers;
- the exact baseline/residual split and the residual constant `d_0`;
- simultaneous slot-ground and within-slot transverse lower forms under the same short;
- the exact rank-one baseline short and the variational transfer to the exact inherited pivot;
- the rational parent coefficient and local mixed/aligned Young algebra;
- the one-dimensional response-placement identity once the exact inherited line has already been reached.

It does **not** validate the full RH chain. In particular, this pass has not independently replayed or established:

1. the complete upstream derivation that places every routed zeta source and every noncompact/exterior contribution into the normalized cell form (1) with exactly the stated normalization;
2. the global same-vector/common-cut/fold intertwining of Lemma 8.4 and the complete term identification in Theorem 8.5;
3. the strict transverse-reserve finite computations used around Theorem 6.55;
4. the interval-certified `Y=7` base endpoint;
5. the finite MASTER sweeps through the stated cutoff or the aligned-penalty analytic tail;
6. the end-to-end induction and hence the claimed RH conclusion.

Accordingly, WI-361 remains correctly classified as a candidate RH proof requiring independent audit and certificate replay. The important update is narrower: **a generic objection that the coherent source estimate necessarily double-counts the complement reserve does not survive reconstruction.** Any decisive failure must now be sought upstream in the exact transport/normalization, downstream in the same-vector fold assembly, or in the computer-assisted certificates and analytic tails.

## 6. Prior art and novelty assessment

All source-capacity, one-defect, inherited-pivot, MASTER mixed-block, and response-placement mechanisms audited here are claims of Desogus's 17 Sep 2026 preprint, not Mathia inventions. Mathia makes no priority claim for them. The contribution of this finding is an independent derivation and evidence-status refinement relative to WI-361: it separates an analytically checkable common-cut/pivot subchain that survives from the still-unverified global transport, fold, and certificate gates.

No new theorem about zeta zeros or RH is claimed here. The established evidence base remains unchanged until the remaining gates are independently closed.

## Sources

- Marco Desogus, **The Three Gates: A Rooted-Operator Approach to Weil Positivity**, arXiv:2609.20367v1 (17 Sep 2026), especially §§5, 6.8--6.9, 6.14.4--6.14.6 and §8: https://arxiv.org/abs/2609.20367
- `research/weil_inertia/findings/WI-361-desogus-source-exact-cofinal-rooted-schur-induction.md` for the prior primary-source audit and the explicit audit gates this finding narrows.
