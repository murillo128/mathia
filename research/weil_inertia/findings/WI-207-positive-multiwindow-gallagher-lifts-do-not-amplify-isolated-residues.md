# WI-207 — positive multiwindow Gallagher lifts do not amplify isolated residues

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

WI-205 shows that the explicit-formula residue of a bounded near-line zero packet is polynomially sub-diagonal in the exact Gallagher source norm, and WI-206 shows that optimizing one scalar physical window cannot repair that loss. WI-206 deliberately left a coupled multiwindow observable outside its conclusion. A substantial part of that apparent escape can also be closed exactly: **any finite collection of linear windows combined by an arbitrary positive-semidefinite quadratic form has the same residue-to-prime-diagonal visibility bound, with no dependence on the number of channels.**

The reason is not a loose channelwise Cauchy--Schwarz estimate. A PSD cross-channel coupling factors through one Hilbert norm. After that factorization, the packet residue is a single Hilbert-valued linear functional and its natural von-Mangoldt square diagonal is the matching Hilbert energy. The same Riesz/Cauchy--Schwarz quotient from WI-206 reappears exactly. The argument is dimension-free, so the number of windows and the PSD coupling may depend on `X`, on the distinguished twist, and even on the hypothetical target packet.

At the bow scale `L=X/H`, for a packet of total multiplicity `M_F` with maximal horizontal depth `delta_*`, every such positive multiwindow lift satisfies

\[
\boxed{
\frac{\text{packet residue energy}}
     {\text{its prime-square diagonal}}
\le
(1+o(1))
M_F^2 X^{2\delta_*}
\frac{1}{H\log X}.
}
\tag{1}
\]

Thus in the source-compatible normalized-depth regime `delta_* log T=O(1)`, `X=T^{1/2+o(1)}`, `H=T^vartheta/log T`, a bounded packet contributes only

\[
\boxed{M_F^2T^{-\vartheta+o(1)}}
\tag{2}
\]

of the diagonal, exactly as for one box window. Coherent positive cross-channel interference does not buy a factor of the channel count. A multiwindow architecture can evade this finding only by leaving the positive same-translation quadratic class—for example through a genuinely sign-indefinite or nonlinear joint statistic, a nonlocal cross-translation form whose positivity uses arithmetic structure rather than a fixed PSD channel matrix, or a different source relation. The unresolved distinguished-twist covariance in `CLUE-bow-distinguished-twist-offdiagonal-cancellation.md` therefore remains open.

## 1. Exact PSD multiwindow reduction to one Hilbert-valued profile

Fix `X`, a physical span `L=o(X)`, a twist `U`, and `J>=1`. Let

\[
v(t)=\bigl(v_1(t),\ldots,v_J(t)\bigr)^T
\tag{3}
\]

be a vector of complex piecewise-`C^1` or bounded-variation profiles supported in `[0,1]`. The individual weighted prime sums are

\[
S_j(x)
:=\sum_n\Lambda(n)n^{-iU}
  v_j\!\left(\frac{n-x}{L}\right),
\qquad X\le x\le2X-L.
\tag{4}
\]

Write `S(x)=(S_1(x),...,S_J(x))^T`. Let

\[
Q=Q^*\succeq0
\tag{5}
\]

be any positive-semidefinite channel coupling. The coupled source energy is

\[
\mathcal E_Q
:=\int_X^{2X-L} S(x)^*Q S(x)\,dx.
\tag{6}
\]

Factor

\[
Q=B^*B
\tag{7}
\]

and define the Hilbert-valued effective profile

\[
V(t):=Bv(t).
\tag{8}
\]

Then pointwise in `x`,

\[
S(x)^*QS(x)
=\left\|
\sum_n\Lambda(n)n^{-iU}
V\!\left(\frac{n-x}{L}\right)
\right\|_2^2.
\tag{9}
\]

Equation (9) is exact. In particular, off-diagonal channel terms in `Q` are not discarded or bounded separately: all coherent PSD mixing has already been retained inside the norm. Rank deficiency, complex channel phases and arbitrarily ill-conditioned positive couplings cause no difficulty because only `V=Bv` survives.

This formulation also absorbs several windows with different offsets or widths so long as they lie inside one common physical span `L`: choose the common normalized coordinate `t=(n-x)/L` and encode each translated/rescaled window as one component of `v(t)`. Zeros between the component supports cost nothing. Thus the theorem concerns the total physical footprint, not merely identical copies of one profile.

## 2. The packet residue obeys a dimension-free Riesz bound

Let `F` be a finite packet of zeta zeros, counted with multiplicity, and put

\[
M_F:=\sum_{\rho\in F}m_\rho,
\qquad
\delta_*:=\max_{\rho=\beta+i\gamma\in F}
\left(\beta-\frac12\right).
\tag{10}
\]

Applying the standard logarithmic-derivative explicit formula componentwise to (4), the contribution of `F` to the effective Hilbert-valued source is

\[
R_F(x)
=-L\sum_{\rho\in F}m_\rho
\int_0^1
V(t)(x+Lt)^{\rho-iU-1}\,dt.
\tag{11}
\]

The same formula underlies WI-205--WI-206; vectorization changes only the codomain. Since `X<=x+Lt<=2X` and the relevant near-line regime has `beta<1`, the triangle inequality followed by the Hilbert norm gives

\[
\|R_F(x)\|_2
\le
M_F L X^{-1/2+\delta_*}
\int_0^1\|V(t)\|_2\,dt.
\tag{12}
\]

Integrating over an interval of length at most `X`,

\[
\int_X^{2X-L}\|R_F(x)\|_2^2dx
\le
M_F^2L^2X^{2\delta_*}
\left(\int_0^1\|V(t)\|_2dt\right)^2.
\tag{13}
\]

Now use Cauchy--Schwarz on the unit physical profile interval:

\[
\left(\int_0^1\|V(t)\|_2dt\right)^2
\le
\int_0^1\|V(t)\|_2^2dt.
\tag{14}
\]

Therefore

\[
\boxed{
\int_X^{2X-L}\|R_F(x)\|_2^2dx
\le
M_F^2L^2X^{2\delta_*}\|V\|_{L^2([0,1];\mathbf C^J)}^2.
}
\tag{15}
\]

Nothing in (12)--(15) depends on `J`. The profiles and `Q` may be selected after specifying `X`, `U` and the target packet; the estimate already grants that oracle adaptivity. In the one-zero case the Riesz optimizer has one fixed Hilbert direction multiplied by the scalar matched profile `(x+Lt)^{\bar\rho+iU-1}`. Hence a truly multichannel direction does not even improve the sharp local linear-functional norm: the optimal response is rank one in channel space.

## 3. The natural prime-square diagonal carries exactly the same Hilbert norm

The diagonal part of (6) is

\[
D_Q(X,L)
:=\int_X^{2X-L}
\sum_n\Lambda(n)^2
v\!\left(\frac{n-x}{L}\right)^*
Q
v\!\left(\frac{n-x}{L}\right)
\,dx.
\tag{16}
\]

By (8),

\[
D_Q(X,L)
=\int_X^{2X-L}
\sum_n\Lambda(n)^2
\left\|V\!\left(\frac{n-x}{L}\right)\right\|_2^2dx.
\tag{17}
\]

For every integer `n` in the macroscopic interior

\[
X+L\le n\le2X-L,
\tag{18}
\]

the substitution `x=n-Lt`, `0<=t<=1`, stays entirely inside the integration interval. Hence its contribution is exactly

\[
\int_X^{2X-L}
\left\|V\!\left(\frac{n-x}{L}\right)\right\|_2^2dx
=L\|V\|_2^2.
\tag{19}
\]

All omitted boundary terms in (17) are nonnegative. The classical second von-Mangoldt moment

\[
\sum_{n\le Y}\Lambda(n)^2\sim Y\log Y
\tag{20}
\]

therefore yields, because `L=o(X)`,

\[
\boxed{
D_Q(X,L)
\ge
(1-o(1))XL\log X\,\|V\|_2^2.
}
\tag{21}
\]

The important uniformity point is that no weighted prime number theorem depending on the profiles is needed. The full profile norm factors out **exactly** in (19), before the macroscopic prime-square sum is evaluated. Thus (21) remains valid for arbitrarily many channels and for `X`-dependent profiles and PSD matrices, provided the common physical span remains `o(X)`.

Combining (15) and (21) gives the dimension-free visibility quotient

\[
\boxed{
\frac{
\int_X^{2X-L}\|R_F(x)\|_2^2dx
}{D_Q(X,L)}
\le
(1+o(1))
M_F^2X^{2\delta_*}
\frac{L}{X\log X}.
}
\tag{22}
\]

Equation (22) is the multiwindow analogue of WI-206 equation (13), but its shape factor has disappeared completely: all channel geometry has been absorbed into one common Hilbert norm and cancels between signal and diagonal.

## 4. Bow-scale consequence and mesoscopic-packet threshold

At the exact Gallagher bow scale of WI-195,

\[
L=K=\frac XH,
\tag{23}
\]

(22) becomes (1):

\[
\frac{\text{packet residue energy}}
     {\text{prime-square diagonal}}
\le
(1+o(1))
\frac{M_F^2X^{2\delta_*}}{H\log X}.
\tag{24}
\]

Under the source-compatible normalization

\[
X=T^{1/2+o(1)},
\qquad
H=\frac{T^\vartheta}{\log T},
\qquad
\delta_*\log T=O(1),
\tag{25}
\]

one has `X^(2 delta_*)=T^{o(1)}` up to a bounded factor, so

\[
\boxed{
\frac{\text{packet residue energy}}
     {\text{diagonal}}
\ll
M_F^2T^{-\vartheta+o(1)}.
}
\tag{26}
\]

Consequently a positive multiwindow lift still needs, at a minimum,

\[
M_F\gtrsim T^{\vartheta/2-o(1)}
\tag{27}
\]

before the packet's own residues can be diagonal-sized. Increasing the number of windows cannot lower this threshold. The only way to gain within the same positive linear architecture is to enlarge the **physical span** `L`, not the channel dimension. Repeating the argument after placing several offset windows inside a common span `W=o(X)` simply replaces `L` by `W`; the packet-to-diagonal quotient is at most

\[
(1+o(1))M_F^2X^{2\delta_*}\frac{W}{X\log X}.
\tag{28}
\]

For bounded normalized-depth packets, diagonal visibility would require a span of order `X log X`, beyond one dyadic source block. This is the same physical-support obstruction found in WI-206, now unaffected by coherent positive multi-channel packaging.

## 5. Stress tests and exact boundary

Several plausible loopholes do not change the conclusion.

If `Q` is diagonal, (22) says that summing many independently weighted Gallagher energies has no channel-count bonus. If `Q` has large off-diagonal entries, the factorization `Q=B^*B` retains their coherent interference exactly rather than bounding it termwise. If `Q` is singular, both target response and diagonal are projected onto the same surviving subspace. If `J=J(X)` grows, the proof is unchanged because all estimates are Hilbert-space inequalities with no dimension constant. If the profiles and `Q` are tuned to the distinguished `U` or to the hypothetical off-line packet, the same bound still applies.

What is load-bearing is **positive quadratic scalarization at each common translation**. A Hermitian matrix `Q` with a genuine negative direction cannot be factored as in (7), so a sign-indefinite cross-window statistic lies outside the theorem. Such a form would need a separate zero-side or source-side argument proving that its total contribution is controlled despite the negative channel directions; positivity of the final numerical value on one arithmetic sequence is not enough to import (22).

The theorem also does not cover a nonlocal operator coupling different translations `x` whose positivity and diagonal structure are not reducible to a fixed channel PSD form, nonlinear statistics of several window outputs, prime-adaptive weights that alter the macroscopic diagonal, or a second independent explicit-formula/source relation. Those are genuine changes of architecture rather than more channels inside the same one.

Most importantly, (22) is only an upper bound on the contribution of the **selected zero packet's own explicit-formula residues**. It does not estimate the full `Lambda-Lambda^sharp` covariance at the distinguished bow twist and does not preclude arithmetic cancellation of that full covariance. Thus `WI-195` and the accepted `CLUE-bow-distinguished-twist-offdiagonal-cancellation.md` remain live. The result only says that the full covariance cannot be forced to be large by hiding a bounded target packet in an arbitrarily rich PSD collection of local linear windows.

## 6. Prior-art and novelty audit

Weighted Gallagher/Selberg mean-square methods are classical. Giovanni Coppola and Maurizio Laporta, **A generalization of Gallagher's lemma for exponential sums**, *Siauliai Mathematical Seminar* 10:18 (2015), 29--47, arXiv:1411.1739, develops scalar weighted Gallagher inequalities, self-convolution smoothing and comparisons between window choices. WI-206 already uses that literature to classify scalar window optimization as prior art rather than a new analytic device.

The factorization `Q=B^*B`, the Hilbert-valued Cauchy--Schwarz/Riesz bound and the matched-filter interpretation are elementary Hilbert-space facts. No novelty is claimed for them. The closely related line-local WI-144 proves a different positive-Hilbert collapse on the **zero-side Lamzouri kernel**: coherent vector features and PSD Frobenius energies cannot manufacture the signed Fourier tail needed by the CGdL transplant. WI-207 is not that statement transplanted verbatim. Its object is the **prime-side explicit-formula residue-to-diagonal quotient** at the source-fixed Gallagher scale, and its conclusion is the dimension-free power loss (22)--(26).

A targeted literature search around vector/matrix-valued Gallagher inequalities, multiple weighted Selberg integrals, Hilbert-valued Dirichlet-polynomial mean squares and multichannel matched filtering located the classical scalar weighted-Gallagher literature and the generic Hilbert/matched-filter principle, but no zeta result establishing the specific packet-versus-von-Mangoldt-diagonal bound (22) for arbitrary PSD multiwindow coupling. Absence from that search is not evidence of priority. The durable Mathia contribution is the exact closure of the positive multiwindow loophole left open by WI-206, together with the dimension-free packet threshold (27).

## 7. Research consequence

The current bow program should not spend further cycles increasing the number of ordinary local windows, tuning their phases, or optimizing a fixed PSD covariance matrix in the hope that coherent positive channel interference will make one bounded normalized-depth off-line packet visible. That entire class pays the same `T^{-vartheta+o(1)}` visibility factor as the original box.

This narrows the surviving source-side choices. A useful multi-observable escape must introduce information that the Hilbert quotient in (22) does not preserve: a rigorously controlled sign-indefinite cross-channel form, genuinely nonlocal translation coupling, a nonlinear statistic, a second independent source identity, or arithmetic structure forcing a mesoscopic packet rather than an isolated exception. Independently, the direct `WI-195` route remains to prove or rule out source-specific signed off-diagonal cancellation at the distinguished twist.

## Classification

- **Classical identity:** PSD quadratic forms factor through a Hilbert norm; Hilbert-valued Riesz/Cauchy--Schwarz gives (12)--(15); `sum_{n<=Y} Lambda(n)^2 ~ Y log Y` gives the macroscopic prime-square normalization.
- **Literature-backed context:** weighted Gallagher/Selberg windowing and smoothing are established prior art; WI-195 supplies the exact bow `L^2` source interface and WI-205--WI-206 supply the scalar residue comparison being extended.
- **Exact deduction:** equations (9), (15), (21) and the dimension-free quotient (22), including arbitrary finite `X`-dependent channel count and PSD coupling.
- **Decisive barrier:** positive same-translation multiwindow quadratic lifts cannot amplify a bounded normalized-depth packet to diagonal scale.
- **Not claimed:** a bound for the full distinguished-twist covariance, impossibility of sign-indefinite/nonlinear/nonlocal multi-observable methods, a new simple-zero proportion, or any direct elimination of off-critical zeros.