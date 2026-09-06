# WI-180 — the full simple-real Gram tail is screened by at most the distinct exceptional count

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-INTERFACE + ROUTE-SPECIFIC-BARRIER`. WI-179 proves that Lamzouri's off-line odd sector can remove the quadratic supercritical penalty in at most one projected quotient mode per distinct off-line conjugate pair. Its extra term is naturally written on the projected simple-real frame `S`, and WI-179 correctly warns that the same-index tail cannot simply be replaced by a tail of the full simple-real Gram `G_s` because `G_s=B+A` with `A\succeq0`.

Keeping one more exact source fact resolves that observability problem with a controlled index shift. The projection Gram `A` has rank at most `r+k`, where `r` is the number of distinct repeated-real points and `k` the number of distinct off-line conjugate pairs. Rank-perturbation interlacing therefore transfers the WI-179 tail back to the full Gram after paying at most `r+k` additional spectral slots. Since

\[
D-n=r+2k
\]

is exactly the number of **distinct exceptional elements** of Lamzouri's finite multiset, the resulting finite budget is

\[
\boxed{
Q-N\ge
O+2M+\operatorname{tr}\Psi(G_s)
+\mathcal T_{D-n}(G_s),
}
\tag{A}
\]

where `D` is the total number of distinct elements, `n` is the number of simple real elements, `O` is the multiplicity-weighted non-real population, `M=N-D`, and

\[
\mathcal T_e(G_s)
:=\sum_{j>e}(\mu_j-2)_+^2
\tag{B}
\]

for the decreasing eigenvalues `mu_j` of `G_s`. Thus **each distinct exceptional element can screen at most one full-Gram supercritical mode in the rank-only relaxation**. A repeated-real point supplies one screening dimension through `U`; a simple off-line conjugate pair supplies two, one through its conjugation-even direction in `U` and one through the odd rank-one proximal correction.

No unconditional simple-critical-zero percentage changes here. The result makes the WI-179 bootstrap interface source-observable: a lower bound on the supercritical spectral tail of the actual simple-real Montgomery--Taylor Gram can now be inserted directly, without first controlling the projected quotient Gram.

## 1. Exact source interface

Use the notation of WI-170, WI-178, and WI-179 for Lamzouri's finite conjugation-invariant multiset. Let

\[
r:=|R_2|,
\qquad
k:=|Z_+|,
\]

where `R_2` is the set of distinct repeated real points and `Z_+` contains one representative of each distinct non-real conjugate pair. If `R_1` is the set of simple real points, then

\[
n:=|R_1|,
\qquad
D=n+r+2k.
\tag{1}
\]

Lamzouri's nested spaces satisfy

\[
\dim U=r+k,
\qquad
M_0:=V\ominus U,
\qquad
\dim M_0=n.
\tag{2}
\]

For each simple real point `x`, write

\[
a_x=P_Uf_x,
\qquad
b_x=P_{M_0}f_x.
\tag{3}
\]

Let `B` be the Gram matrix of the `b_x`, and let

\[
A=(\langle a_x,a_y\rangle)_{x,y\in R_1}.
\tag{4}
\]

The full simple-real Gram is

\[
\boxed{G_s=B+A,\qquad A\succeq0.}
\tag{5}
\]

Because every `a_x` lies in the `(r+k)`-dimensional space `U`,

\[
\boxed{d:=\operatorname{rank}A\le r+k.}
\tag{6}
\]

The frame operator `S=\sum b_x\otimes b_x` on `M_0` has the same positive eigenvalues as `B`. WI-179 proves

\[
\boxed{
Q-N\ge
O+2M+\operatorname{tr}\Psi(G_s)+\mathcal T_k(B),
}
\tag{7}
\]

where

\[
\mathcal T_k(B)
=\sum_{j>k}(\lambda_j(B)-2)_+^2.
\tag{8}
\]

The only new question is how much of (8) survives when one replaces the projected Gram `B` by the directly source-visible full Gram `G_s`.

## 2. Rank-`d` positive perturbation transfers the tail with exactly `d` lost slots

Let

\[
\lambda_1\ge\cdots\ge\lambda_n
\]

be the eigenvalues of `B`, and

\[
\mu_1\ge\cdots\ge\mu_n
\]

those of `G_s=B+A`. Since `A\succeq0` has rank `d`, the classical rank-perturbation interlacing inequality gives

\[
\boxed{
\mu_{j+d}\le\lambda_j\le\mu_j
\qquad(1\le j\le n-d).
}
\tag{9}
\]

No commutativity between `A` and `B` is required. One way to see the left inequality is the min--max principle restricted to `\ker A`, whose codimension is `d`; equivalently, a rank-`d` positive perturbation can increase the eigenvalue counting function above any threshold by at most `d`.

The function

\[
\phi(t):=(t-2)_+^2
\tag{10}
\]

is nondecreasing. Therefore, for every integer `k>=0`,

\[
\begin{aligned}
\mathcal T_k(B)
&=\sum_{j>k}\phi(\lambda_j)\\
&\ge\sum_{j=k+1}^{n-d}\phi(\lambda_j)\\
&\ge\sum_{j=k+1}^{n-d}\phi(\mu_{j+d})\\
&=\boxed{\mathcal T_{k+d}(G_s)}.
\end{aligned}
\tag{11}
\]

Here and below `\mathcal T_e=0` when `e>=n`. The shift by `d` is the exact price of forgetting which full-Gram modes were created or raised by the low-rank projection component `A`.

Using (6),

\[
k+d\le k+r+k=r+2k=D-n.
\tag{12}
\]

Since `e\mapsto\mathcal T_e(G_s)` is decreasing,

\[
\boxed{
\mathcal T_k(B)
\ge
\mathcal T_{D-n}(G_s).
}
\tag{13}
\]

Substitution into (7) proves the full-Gram budget (A).

## 3. The spectral screening budget equals the distinct exceptional population

Equation (13) has a direct geometric interpretation. Before the proximal minimization, the full simple-real Gram can lose supercritical spectral information in two places.

First, passing from `G_s` to the quotient Gram `B` subtracts the PSD matrix `A`; its rank is at most `r+k`. Each distinct repeated-real point contributes at most one dimension to `U`, and each distinct off-line pair contributes at most one conjugation-even dimension. Second, WI-179 allows the projected odd correction to cancel at most `k` further supercritical modes, one per distinct off-line pair. The total rank-only screening capacity is therefore

\[
(r+k)+k=r+2k=D-n.
\tag{14}
\]

This is exactly the number of distinct elements that are not simple and real. Multiplicity does not buy additional spectral slots: extra copies increase the scalar `O` and `M` charges in (A), but they do not increase `r` or `k`.

For `epsilon>0`, define the full-Gram supercritical count

\[
q_\epsilon(G_s)
:=\#\{j:\mu_j\ge2+\epsilon\}.
\tag{15}
\]

Then (B) gives

\[
\boxed{
\mathcal T_{D-n}(G_s)
\ge
\bigl(q_\epsilon(G_s)-(D-n)\bigr)_+\epsilon^2.
}
\tag{16}
\]

Hence (A) implies

\[
\boxed{
Q-N\ge
O+2M+\operatorname{tr}\Psi(G_s)
+igl(q_\epsilon(G_s)-(D-n)\bigr)_+\epsilon^2.
}
\tag{17}
\]

If only the multiplicity-weighted populations are retained, WI-170 gives

\[
M=r+E_{\mathbb R}+2E_{\mathbb C},
\qquad
O=2k+2E_{\mathbb C},
\]

and therefore

\[
D-n=r+2k\le M+O.
\tag{18}
\]

A weaker but population-only corollary is consequently

\[
\boxed{
Q-N\ge
O+2M+\operatorname{tr}\Psi(G_s)
+\mathcal T_{M+O}(G_s).
}
\tag{19}
\]

The exact cutoff `D-n` is preferable when distinct exceptional counts are available.

## 4. A moment-ratio criterion for activating the bootstrap term

The full-Gram formulation exposes a precise spectral statistic that would make the new term positive. Put

\[
Y:=(G_s-2I)_+,
\qquad
L_2:=\operatorname{tr}Y^2,
\qquad
L_4:=\operatorname{tr}Y^4.
\tag{20}
\]

If `y_1>=...>=y_n>=0` are the eigenvalues of `Y`, then

\[
L_2=\sum_j y_j^2,
\qquad
L_4=\sum_j y_j^4,
\qquad
\mathcal T_e(G_s)=\sum_{j>e}y_j^2.
\]

Cauchy--Schwarz on the first `e` terms gives

\[
\sum_{j\le e}y_j^2
\le
\sqrt{e\sum_{j\le e}y_j^4}
\le\sqrt{eL_4}.
\]

Thus for every `e`,

\[
\boxed{
\mathcal T_e(G_s)
\ge
\max\{0,\,L_2-\sqrt{eL_4}\}.
}
\tag{21}
\]

When `L_4>0`, define the supercritical participation ratio

\[
\rho:=\frac{L_2^2}{L_4}.
\tag{22}
\]

Then

\[
\boxed{
\rho>e
\quad\Longrightarrow\quad
\mathcal T_e(G_s)
\ge
L_2\left(1-\sqrt{\frac e\rho}\right)>0.
}
\tag{23}
\]

This is not a new matrix-analysis principle; it is the elementary Schatten-moment/Cauchy--Schwarz rank bound written in the exact variable needed by (A). Its role is diagnostic. The missing source input is no longer an unspecified ``stronger spectral estimate'': one sufficient route is to prove that the supercritical excess of the actual simple-real Gram has effective multiplicity `rho` larger than the distinct exceptional count.

A source estimate for ordinary pair energy or `tr Psi(G_s)` does not supply (22), because those quantities also charge subcritical eigenvalues. Higher spectral moments can help only if they control the **positive part above 2** or another invariant that forces its effective rank.

## 5. Scalar Gram defect alone cannot activate the new tail

The shift to the full Gram does not make the existing scalar Gram-defect lower bounds self-bootstrapping. WI-015 gives an exact Montgomery--Taylor integer-gap control that already lives in the genuine translation-kernel geometry. On every finite section its Gram eigenvalues satisfy

\[
1-\frac4{17}<\mu_j<1+\frac4{17}=\frac{21}{17}<2.
\tag{24}
\]

Consequently

\[
(G_s-2I)_+=0,
\qquad
q_\epsilon(G_s)=0,
\qquad
\mathcal T_e(G_s)=0
\tag{25}
\]

for every `epsilon>0` and every cutoff `e`, even though the exact Gram defect is positive and extensive and equals its pair energy on this control:

\[
\operatorname{tr}\Psi(G_s)
=\operatorname{tr}(G_s-I)^2.
\tag{26}
\]

Thus no argument that first compresses the simple-real source to the single scalar `tr Psi(G_s)`, even while retaining generic PSD consistency and the exact Montgomery--Taylor placement used by WI-015, can infer a positive value of the WI-180 tail. The source must retain information that excludes the subcritical spectral control before scalarization.

WI-020 supplies a complementary abstract warning. At fixed Frobenius energy above the clipping threshold, the sharp minimum of `tr Psi` is realized by a one-spike spectrum. Scalar energy therefore naturally permits concentration of supercriticality into very few modes rather than forcing the extensive mode multiplicity required by (17). The new bootstrap is genuinely a **spectral-shape** mechanism, not another use of the same scalar defect.

This does not refute the route. The WI-015 periodic control is not asserted to be the actual zeta zero process, and additional zeta-specific spacing/correlation information may exclude it. It does show that such additional information is logically necessary for this branch.

## 6. Sharpness and boundary conditions

The two rank losses used above are individually sharp at the level of the relaxed matrix problem. A rank-`d` positive perturbation can raise exactly `d` eigenvalues across a fixed threshold, so the shift by `d` in (11) cannot be reduced by generic interlacing. WI-179 likewise proves that, in its relaxed PSD proximal minimization, a rank-`k` odd correction can cancel the `k` largest supercritical excess modes exactly. Therefore the combined cutoff `k+d`, and hence the worst-case source bound `D-n`, cannot be improved using only the two rank facts.

Several stronger-looking statements are **not** justified:

- one cannot replace `\mathcal T_{D-n}(G_s)` by `\mathcal T_k(G_s)` without controlling the projection Gram `A`;
- a large value of `tr Psi(G_s)` does not imply `q_epsilon(G_s)>D-n`, by (24)--(26);
- the result does not identify the uncertified complement as off-line zeros: `D-n` includes distinct repeated-real points as well as both members of each off-line pair;
- if `D-n>=n`, the new tail is identically zero, so the inequality by itself has no bootstrap force;
- no claim is made that the moment ratio (22) is currently accessible from support-one pair correlation or from the existing four-point certificate.

The gain can be stronger when source geometry gives `rank A<r+k` or when the projected odd correction has rank smaller than `k`. Those are additional source constraints, not consequences of the present rank algebra.

## 7. Prior-art and novelty audit

The finite zeta/Hilbert-space source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1. The exact population, Gram-defect, and proximal-rank interfaces used here are the Mathia findings WI-170, WI-178, and WI-179. The full-Gram Montgomery--Taylor subcritical control is WI-015, and the scalar trace--energy extremizer is WI-020.

Rank-`d` Hermitian interlacing, eigenvalue counting under finite-rank perturbations, and the Cauchy--Schwarz moment/rank inequality are classical matrix-analysis facts. No novelty is claimed for any of them. A targeted audit of Lamzouri's current preprint, the local WI-170--WI-179 chain, and standard finite-rank interlacing literature found the projected-tail caveat of WI-179 but not the source-specific composition

\[
\operatorname{rank}A\le r+k,
\qquad
\operatorname{rank}C\le k
\quad\Longrightarrow\quad
\text{full-Gram screening cutoff }r+2k=D-n.
\]

Absence from that bounded audit is not a priority claim. The durable line-specific content is the exact transfer (A)/(13), its interpretation as one full-Gram spectral screening slot per distinct exceptional element, and the identification of a supercritical effective-rank statistic as a sufficient bootstrap input.

## 8. Consequence for the research line

WI-179 left a concrete but awkward target: prove many supercritical eigenvalues for the **projected** simple-real quotient `S`, whose geometry depends on the unknown exceptional subspace `U`. The present interlacing step removes that obstacle. It is enough to work with the full simple-real Montgomery--Taylor Gram `G_s`, at the unavoidable cost of allowing every distinct exceptional element one screening slot.

The RH-facing question is therefore sharper:

\[
\boxed{
\text{Can a source theorem force the supercritical excess of }G_s
\text{ to have effective rank exceeding }D-n?
}
\]

If yes, (21)--(23) create positive residual budget after **all** rank-allowed exceptional screening, which feeds back against the exceptional population in (A). If not, and source-compatible near-extremizers can keep all supercritical excess inside at most `D-n` modes—or avoid the threshold entirely as in WI-015—then the WI-179 rank coupling cannot bootstrap to zero defect without genuinely new information.

This is a structural advance rather than a percentage result: it moves the new nonlinear exceptional-block constraint onto the actual full Gram object already used by the Montgomery--Taylor/four-point machinery, while simultaneously proving that the existing scalar defect certificate is insufficient to activate it.