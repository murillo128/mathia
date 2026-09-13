# WI-279 — Hilbert cut covariance yields a bottom-Toeplitz reserve but does not break the scalar-profile wall

## Status

- **Evidence:** `EXACT-DERIVED + CLASSICAL-OPERATOR + HILBERT-CUT-COVARIANCE + STRICT-REFINEMENT + DECISIVE-BOUNDARY + PRIOR-ART-AUDITED`.
- **Scope:** strengthens the commensurate cross-cut reserve of `WI-277` by retaining the orientation of the cut vectors in the Hilbert quotient of the first-crossing PSD form instead of replacing each vector by its norm `sqrt(Q_t)`. The resulting coefficient uses the **bottom** eigenvalue of the same finite Toeplitz matrix that appears in `WI-277`.
- **What it does not claim:** this does not prove RH, does not force the reserve above the one-signed archimedean budget `K_+`, does not prove one-signedness of a first null mode, and does not constrain the sign-changing branch by itself. In fact the scalar-profile countermodel of `WI-278` still keeps every reserve proved here below `K_+`.
- **Novelty boundary:** Rayleigh bounds for finite symmetric Toeplitz matrices, principal-submatrix interlacing, and Hilbert-valued tensor extensions are classical. The line-local deduction is the exact signed covariance identity for the first-crossing cut path and its insertion into the commensurate shift optimization. A targeted audit of nilpotent numerical-radius, truncated-Toeplitz, and vector-valued Toeplitz literature found the generic operator machinery but no localized-Weil first-crossing statement of this form. No priority claim is made.

## Claim

Assume RH is false and retain the first unrestricted crossing setup of `WI-253`, `WI-269`, and `WI-276`:

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\},
\qquad q_a\ge0,
\qquad \|v\|_2=1,
\qquad q_a(v)=0,
\tag{1}
\]

with `v` real and extended by zero outside `(-a,a)`. For almost every cut `s`, put

\[
u_s:=v\mathbf 1_{(-a,s)},
\qquad
Q_s:=q_a(u_s),
\qquad
\mathcal S_v:=\int_{\mathbb R}Q_s\,ds,
\tag{2}
\]

where `Q_s=0` outside `[-a,a]`. Let `\mathcal H_q` be the real Hilbert quotient obtained from the PSD form `q_a`, and write

\[
G_s:=[u_s]\in\mathcal H_q.
\tag{3}
\]

Then `||G_s||_q^2=Q_s`. For every `h>0` and every integer `k>=1` with `kh<2a`, define the signed cut covariance

\[
C_k(h):=
\int_{\mathbb R}
\langle G_s,G_{s+kh}\rangle_q\,ds.
\tag{4}
\]

The sliding-window functional satisfies the exact identity

\[
\boxed{
\mathcal F_v(kh/2)=\mathcal S_v-C_k(h).
}
\tag{5}
\]

Now fix `0<r<a`, put `h=2r` and

\[
N:=\left\lceil\frac{2a}{h}\right\rceil
=\left\lceil\frac a r\right\rceil.
\tag{6}
\]

For nonnegative weights `\alpha_k`, supported on indices with `kr<a`, define as in `WI-277`

\[
H_N(\alpha)
:=\frac12\sum_k\alpha_k
\left(J_N^k+(J_N^*)^k\right),
\qquad
\eta_N(\alpha):=\lambda_{\min}(H_N(\alpha)).
\tag{7}
\]

Then

\[
\boxed{
\sum_k\alpha_k C_k(h)
\ge
\eta_N(\alpha)\,\mathcal S_v.
}
\tag{8}
\]

Consequently firstness gives the exact bottom-spectrum reserve

\[
\boxed{
\mathcal S_v
\ge
\frac{
\sum_k\alpha_k\,kr\,\lambda_{kr}
}{
\sum_k\alpha_k-\eta_N(\alpha)
}.
}
\tag{9}
\]

For the same weight vector this is always at least as strong as the top-spectrum reserve of `WI-277`,

\[
\frac{
\sum_k\alpha_k\,kr\lambda_{kr}
}{
\sum_k\alpha_k+\rho_N(\alpha)
},
\qquad
\rho_N(\alpha)=\lambda_{\max}(H_N(\alpha)),
\tag{10}
\]

because `H_N(alpha)` is a real symmetric nonnegative matrix and therefore

\[
-\eta_N(\alpha)\le\rho_N(\alpha).
\tag{11}
\]

The improvement can be strict. For `N=3` and `alpha_1=alpha_2=1`,

\[
H_3
=\frac12
\begin{pmatrix}
0&1&1\\
1&0&1\\
1&1&0
\end{pmatrix},
\qquad
\operatorname{spec}(H_3)=\{1,-1/2,-1/2\}.
\tag{12}
\]

Thus the Hilbert-cut reserve has denominator `5/2`, whereas the scalar norm-profile reserve of `WI-277` has denominator `3`:

\[
\boxed{
\mathcal S_v
\ge
\frac{r\lambda_r+2r\lambda_{2r}}{5/2}
>
\frac{r\lambda_r+2r\lambda_{2r}}{3}.
}
\tag{13}
\]

This strict gain is genuine information retained by the common oriented cut path, not a better estimate for the nonnegative scalar profile `sqrt(Q)`.

## 1. The cut path gives an exact signed covariance identity

The quotient-vector notation does not require an additional pointwise regularity assumption on `v`. `WI-276` already proves that the sharp cut pieces are form-admissible for almost every cut by smooth approximation. For fixed `h` and finitely many `k`, intersect those full-measure sets.

For such an `s`,

\[
u_{s+kh}-u_s
=v\mathbf1_{(s,s+kh)}.
\tag{14}
\]

Hence in `H_q`,

\[
[v\mathbf1_{(s,s+kh)}]
=G_{s+kh}-G_s,
\]

and therefore

\[
q_a\!\left(v\mathbf1_{(s,s+kh)}\right)
=Q_s+Q_{s+kh}
-2\langle G_s,G_{s+kh}\rangle_q.
\tag{15}
\]

The covariance is integrable because Cauchy--Schwarz gives

\[
|\langle G_s,G_{s+kh}\rangle_q|
\le\frac12(Q_s+Q_{s+kh}),
\tag{16}
\]

and `Q` is integrable. The exact sliding-window identity used in `WI-253` and `WI-276` is

\[
\int_{\mathbb R}
q_a\!\left(v\mathbf1_{(s,s+kh)}\right)ds
=2\mathcal F_v(kh/2).
\tag{17}
\]

Integrating (15), using translation invariance of `\int Q_s ds`, and comparing with (17) gives

\[
2\mathcal F_v(kh/2)
=2\mathcal S_v-2C_k(h),
\]

which proves (5).

This identifies exactly where `WI-276` lost information. Its triangle inequality replaced the signed inner product in (15) by

\[
|\langle G_s,G_{s+h}\rangle_q|
\le\sqrt{Q_sQ_{s+h}},
\]

then retained only the scalar norm profile `sqrt(Q)`. Equation (5) keeps the orientation and sign of all cut-vector covariances.

## 2. Commensurate shifts are controlled by the bottom Toeplitz eigenvalue

Fix `h=2r`. Decompose the real line into translation fibers modulo `h`. On almost every fiber, the points lying in `(-a,a)` form one consecutive chain of length at most

\[
N=\left\lceil\frac{2a}{h}\right\rceil.
\]

For one chain write its cut vectors as

\[
g=(g_0,\ldots,g_{n-1}),
\qquad g_j\in\mathcal H_q,
\qquad n\le N.
\tag{18}
\]

Zero-pad the chain to length `N`. The weighted covariance on that fiber is exactly

\[
\sum_k\alpha_k\sum_j
\langle g_j,g_{j+k}\rangle_q
=
\left\langle
 g,(H_N(\alpha)\otimes I_{\mathcal H_q})g
\right\rangle.
\tag{19}
\]

The tensor product has the same finite scalar spectral bounds, hence

\[
\left\langle
 g,(H_N(\alpha)\otimes I)g
\right\rangle
\ge
\eta_N(\alpha)
\sum_j\|g_j\|_q^2.
\tag{20}
\]

Integrating over the fiber parameter is legitimate by (16). The left side becomes `sum alpha_k C_k(h)` and the right side becomes `eta_N(alpha) S_v`, proving (8).

No Hilbert-valued measurability theorem beyond the existing scalar cut identities is load-bearing here: for each finite family of shifts, all quantities can be defined and integrated through the measurable scalar forms `Q_s` and `q_a(v 1_(s,s+kh))` using the polarization identity (15). The Hilbert quotient is a convenient exact representation of those scalar quantities.

## 3. Firstness converts covariance into source reserve

At the first global crossing, every smaller window remains strictly positive at the bottom. Thus for every active `k`,

\[
\mathcal F_v(kr)\ge kr\lambda_{kr}.
\tag{21}
\]

Using (5), multiplying by `alpha_k`, and summing gives

\[
\sum_k\alpha_k kr\lambda_{kr}
\le
\left(\sum_k\alpha_k\right)\mathcal S_v
-
\sum_k\alpha_k C_k(h).
\tag{22}
\]

Insert (8):

\[
\sum_k\alpha_k kr\lambda_{kr}
\le
\left(\sum_k\alpha_k-\eta_N(\alpha)\right)\mathcal S_v.
\tag{23}
\]

Since `H_N(alpha)` has zero diagonal and is nonzero when some active `alpha_k>0`, its trace is zero and `eta_N(alpha)<0`; hence the denominator is positive. This proves (9).

For comparison with `WI-277`, `H_N(alpha)` has nonnegative entries. Perron--Frobenius, or simply the standard spectral-radius bound for a real symmetric nonnegative matrix, gives `|lambda|<=rho_N(alpha)` for every eigenvalue. In particular (11) holds, proving pointwise dominance of (9) over (10). Equality occurs for the one-shift/bipartite case; odd-cycle compatibility can make the inequality strict, as (12)--(13) show.

## 4. The bottom-spectrum coefficient is sharp for abstract PSD cut geometry

The improvement over `WI-277` should not be mistaken for an endlessly improvable generic PSD coefficient. For any fixed `H_N(alpha)`, choose a real eigenvector

\[
b=(b_0,\ldots,b_{N-1})
\]

for `eta_N(alpha)` and a unit vector `xi` in a one-dimensional real Hilbert space. On a positive-measure set of full-length fibers set

\[
G_j=b_j\xi.
\tag{24}
\]

Then (19)--(20) is an equality. Moreover this profile can be realized by an abstract null partition: set the consecutive increment vectors

\[
d_0=b_0\xi,
\quad
d_j=(b_j-b_{j-1})\xi\ (1\le j\le N-1),
\quad
d_N=-b_{N-1}\xi.
\tag{25}
\]

Their sum is zero, so their Gram form is PSD and the total vector is null, while the cumulative cut vectors are exactly `b_j xi`. Thus the bottom-eigenvalue constant cannot be universally improved from PSD null-partition geometry alone.

For the concrete three-vertex example, `b=(1,-1,0)` has Rayleigh quotient `-1/2` for (12). The corresponding increments `(1,-2,1,0)` already give the rank-one finite null-partition model noted in the clue that led to this finding.

This sharpness is only for the abstract PSD cut geometry. It does **not** assert that the extremizer satisfies Suzuki's exact source equation or is realized by a zeta first null mode.

## 5. WI-278 still blocks a scalar-profile budget crossing

The strict refinement does not reopen the scalar spectral-profile route closed by `WI-278`. That finding constructs an admissible first-crossing profile `tilde lambda` at `a=1` satisfying every scalar profile constraint used there and

\[
M:=\sup_{0<x<1}x\widetilde\lambda(x)
<\frac1{20}<K_+.
\tag{26}
\]

For any base radius and any nonnegative commensurate weights,

\[
\sum_k\alpha_k kr\widetilde\lambda(kr)
\le
M\sum_k\alpha_k.
\tag{27}
\]

Because `eta_N(alpha)<=0`,

\[
\sum_k\alpha_k-\eta_N(\alpha)
\ge
\sum_k\alpha_k.
\tag{28}
\]

Therefore every bottom-spectrum reserve proved here obeys

\[
\boxed{
R_{\rm bottom}
\le M
<\frac1{20}<K_+.
}
\tag{29}
\]

So the Hilbert cut orientation is **genuinely stronger information than the scalar norm-profile relaxation for a fixed actual profile**, but the presently certified scalar constraints on `lambda_r` still do not force the stronger reserve to cross the one-signed archimedean budget. The distinction is important: `WI-278` did not show that restoring cut orientation was algebraically useless; (13) proves that it is useful. It showed that no reserve whose numerator is controlled only by the current scalar profile data can force the desired crossing, and (27)--(29) now extend that wall to the bottom-spectrum family.

## Prior art and novelty audit

- `WI-276` already anchors Uffe Haagerup and Pierre de la Harpe, **The numerical radius of a nilpotent operator on a Hilbert space**, *Proc. Amer. Math. Soc.* 115 (1992), 371--379, DOI `10.1090/S0002-9939-1992-1072339-6`. Its theorem is an arbitrary-Hilbert-space one-shift result and supplies the classical operator-theory background for the original cross-cut reserve.
- `WI-277` already audits the finite/truncated Toeplitz side, including Gorkin--Partington and related finite-shift literature. The Rayleigh lower bound, zero-padding/interlacing, and tensoring by an identity used in (19)--(20) are classical finite spectral theory; no new general Toeplitz theorem is claimed here.
- A fresh targeted search for Hilbert/vector-valued truncated shifts, matrix-valued truncated Toeplitz operators, polynomial numerical radii, and signed covariance bounds located generic vector-valued operator frameworks but no source coupling the **bottom** finite-Toeplitz spectrum to Suzuki's first-crossing cut path. Search absence is novelty-audit context only and is not a priority claim.
- The Mathia-specific content is (5), (8)--(9), their strict comparison with `WI-277`, and the exact compatibility with the `WI-278` profile wall.

## Audit and falsification tests

The exact claim can be killed by any of the following:

1. show that the a.e. sharp cuts used in `WI-276` cannot be polarized simultaneously for a fixed finite family of shifts, invalidating (15);
2. find a factor-of-two error between the sliding-window identity (17) and the covariance identity (5);
3. exhibit a translation fiber with more than `ceil(2a/h)` active cut vectors or a missing cross term in (19);
4. find a symmetric nonnegative `H_N(alpha)` with `-lambda_min>lambda_max`, contradicting the spectral-radius comparison;
5. construct weights for the `WI-278` profile that violate the elementary bound (27)--(29).

All five tests are finite or reduce to identities already used in `WI-253`, `WI-276`, and `WI-277`. No numerical quadrature or conjectural zero statistic is used.

## Research consequence

The independent-review clue that motivated this test is **supported but narrowed**. Restoring the Hilbert cut path recovers real information lost by `sqrt(Q)` and gives a uniformly no-worse, sometimes strictly stronger, multishift reserve. The scalar support-only top-spectrum coefficient of `WI-277` was therefore not the end of generic first-crossing PSD geometry.

However, the resulting family still cannot cross `K_+` from the currently certified scalar `lambda_r` information because the `WI-278` counterprofile survives it verbatim through (27)--(29). The next RH-facing step must therefore use information not reducible to the scalar bottom-eigenvalue profile: the exact Suzuki signed-source multiplier form of `WI-269`, source-specific noncommensurate cut compatibility, null-mode nodal/shape information, or archimedean sign geometry.

## Formalization disposition

The finite Toeplitz inequality itself is a routine tensor/Rayleigh statement and would not verify the load-bearing analytic bridge. Conversely, formalizing the full statement would require representing the a.e. sharp-cut family, the form quotient, scalar polarization, and the fiber/Fubini passage that are not currently present in the `WI-276` finite PSD formalization. At this stage that is not a bounded Lean handoff relative to the theorem's role, so no automatic formalization issue is opened.
