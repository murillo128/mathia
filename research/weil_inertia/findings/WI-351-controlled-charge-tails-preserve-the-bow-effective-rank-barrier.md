# WI-351 — controlled charge tails preserve the bow effective-rank barrier

**Status:** `established`

**Claim type:** `EXACT-DERIVED + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + NON-RH`

**One-line statement:** The finite-charge hypothesis in `WI-350` can be relaxed to infinite `U(1)` charge support with a uniform Sobolev-type charge moment. If
\[
B_s:=\sup_{U\in I}\left(\sum_{q\in\mathbb Z}|q|^{2s}\|P_qF(z_U)\|^2\right)^{1/2}<\infty,
\qquad s>0,
\]
then high charges can be truncated with controlled error and the same bow cell-cover argument gives a finite effective-rank bound. In particular, under the sharp generic height-resolution scaling `L/mu = O(sqrt(r))`, realizing effective rank `r` forces
\[
\frac{B_s}{\mu}=\Omega(r^{s/2}).
\]
Thus merely turning on infinitely many arbitrarily small charge sectors does not evade the `WI-350` obstruction: an escaping equivariant feature must pay quantitatively in angular/charge Sobolev complexity, height resolution, transmission loss, or another excluded hypothesis.

## Why this matters

`WI-350` proved a linear bow rank-resolution obstruction when every centered output vector has at most `D` active `U(1)` charges. Its explicit remaining escape was infinite or rank-growing charge support. Counting active charges cannot control that regime because infinitely many sectors may carry negligible norm.

The result below replaces hard charge count by a soft spectral-tail condition. A uniform weighted charge moment makes the high-charge tail small; truncating at charge `Q` leaves only `2Q+1` one-dimensional character directions per height cell. The finite-dimensional cover of `WI-350` therefore survives with an approximation penalty determined by the tail. This closes the specific escape in which infinitely many charge sectors are present but their weighted energy remains uniformly controlled.

The theorem remains a structural no-go for one witness architecture. It does **not** prove the distinguished off-diagonal cancellation requested by `CLUE-bow-distinguished-twist-offdiagonal-cancellation`, does not characterize the actual arithmetic complexity of a successful source feature, and does not improve the certified simple-critical-zero proportion by itself.

## Setup

Keep the physical bow notation of `WI-348`--`WI-350`. The normalized bow carrier `w_U` is indexed by a height interval `I` of length `H`, its logarithmic source support has width `Delta`, and
\[
z_U=e^{-iUx_c}w_U
\]
satisfies
\[
\|z_U-z_V\|\le \frac{\Delta}{2}|U-V|.
\tag{1}
\]

Let `F` map the phase-saturated source domain into a Hilbert space `K`. Assume:

1. **Strongly continuous `U(1)`-equivariance.** There is a strongly continuous unitary representation `R:S^1 -> U(K)` with
   \[
   F(e^{i\phi}x)=R(e^{i\phi})F(x).
   \tag{2}
   \]
2. **Lipschitz control.**
   \[
   \|F(x)-F(y)\|\le L\|x-y\|.
   \tag{3}
   \]
3. **Transmission floor.**
   \[
   \|F(x)\|\ge\mu>0
   \tag{4}
   \]
   on the relevant source vectors.

By the standard compact-abelian representation decomposition, write
\[
\mathcal K=\widehat\bigoplus_{q\in\mathbb Z}\mathcal K_q,
\qquad
R(e^{i\phi})|_{\mathcal K_q}=e^{iq\phi}I,
\tag{5}
\]
and let `P_q` denote the orthogonal projection onto `K_q`.

For `s>0`, define the homogeneous charge moment along the centered carrier by
\[
B_s:=\sup_{U\in I}
\left(
\sum_{q\in\mathbb Z}|q|^{2s}\|P_qF(z_U)\|^2
\right)^{1/2}.
\tag{6}
\]
The zero-charge term contributes zero and causes no difficulty because only the high-charge tail is estimated below.

For sampled heights `U_1,...,U_m`, put
\[
h_i=\frac{F(w_{U_i})}{\|F(w_{U_i})\|},
\qquad
G=(\langle h_i,h_j\rangle)_{i,j=1}^m.
\]
As in `WI-350`, if `lambda_1 >= ... >= lambda_m >= 0` are the eigenvalues of `G`, define
\[
r_\tau(G):=\min\left\{q:\sum_{j>q}\lambda_j(G)\le\tau m\right\},
\qquad 0<\tau<1.
\tag{7}
\]

## Theorem: soft charge tails imply finite bow effective rank

Assume (1)--(6), with `B_s<infinity`. For an integer `Q>=0` set
\[
T_Q:=\frac{B_s}{(Q+1)^s}.
\tag{8}
\]
If
\[
T_Q<\mu\sqrt\tau,
\tag{9}
\]
then, for `L>0`,
\[
\boxed{
 r_\tau(G)
 \le
 (2Q+1)
 \left(
 1+\frac{H\Delta L}
 {4\left(\mu\sqrt\tau-T_Q\right)}
 \right).
}
\tag{10}
\]
If `L=0`, one may omit the height cover and obtains `r_tau(G)<=2Q+1` whenever (9) holds.

### Proof

Let
\[
P_{\le Q}:=\sum_{|q|\le Q}P_q.
\]
Orthogonality of the charge decomposition gives, uniformly in `U`,
\[
\begin{aligned}
\|(I-P_{\le Q})F(z_U)\|^2
&=\sum_{|q|>Q}\|P_qF(z_U)\|^2\\
&\le (Q+1)^{-2s}
\sum_{|q|>Q}|q|^{2s}\|P_qF(z_U)\|^2\\
&\le T_Q^2.
\end{aligned}
\tag{11}
\]
This is the only new analytic ingredient relative to `WI-350`: weighted charge energy gives an explicit Hilbert-norm Fourier tail.

Fix a height-cover radius `rho>0`. As in `WI-350`, partition `I` into
\[
N\le1+\frac{H\Delta}{4\rho}
\tag{12}
\]
cells and choose a center `V_k` in each cell so that every `U` in that cell satisfies
\[
\|z_U-z_{V_k}\|\le\rho.
\tag{13}
\]
For a center `V_k`, define the truncated charge subspace
\[
C_{k,Q}:=
\operatorname{span}\{P_qF(z_{V_k}):|q|\le Q\}.
\tag{14}
\]
There is at most one vector contributed by each integer character for this fixed center, even if the ambient character eigenspace has higher multiplicity. Hence
\[
\dim C_{k,Q}\le2Q+1.
\tag{15}
\]
Let
\[
W_Q:=C_{1,Q}+\cdots+C_{N,Q},
\qquad
\dim W_Q\le(2Q+1)N.
\tag{16}
\]

Since `w_U=e^{iUx_c}z_U`, equivariance gives
\[
F(w_U)=R(e^{iUx_c})F(z_U).
\tag{17}
\]
For `U` in the cell centered at `V_k`, the truncated comparison vector
\[
R(e^{iUx_c})P_{\le Q}F(z_{V_k})
\]
lies in `C_{k,Q}`: each charge component is merely multiplied by the scalar `e^{iqUx_c}`. By unitarity, (3), (11), and (13),
\[
\begin{aligned}
\operatorname{dist}(F(w_U),W_Q)
&\le
\|F(z_U)-P_{\le Q}F(z_{V_k})\|\\
&\le L\rho+T_Q.
\end{aligned}
\tag{18}
\]
After normalization and use of (4),
\[
\operatorname{dist}(h_U,W_Q)
\le
\frac{L\rho+T_Q}{\mu}.
\tag{19}
\]

Projecting all sampled normalized vectors onto `W_Q` yields a matrix of rank at most `(2Q+1)N`. The same Eckart--Young/singular-value-tail step used in `WI-350` therefore gives
\[
\sum_{j>(2Q+1)N}\lambda_j(G)
\le
m\left(\frac{L\rho+T_Q}{\mu}\right)^2.
\tag{20}
\]
Under (9), choose
\[
\rho=\frac{\mu\sqrt\tau-T_Q}{L}.
\tag{21}
\]
Then the right side of (20) is `tau m`, so `r_tau(G)<=(2Q+1)N`; substitution into (12) proves (10).

If `L=0`, `F(z_U)` is constant on the connected centered carrier. One center suffices, and the same truncation argument gives the stated bound.

## Explicit moment-only corollary

Put
\[
b_s:=\frac{B_s}{\mu}
\]
and choose
\[
K:=\max\left\{1,
\left\lceil
\left(\frac{2b_s}{\sqrt\tau}\right)^{1/s}
\right\rceil
\right\},
\qquad Q=K-1.
\tag{22}
\]
Then
\[
\frac{T_Q}{\mu}=\frac{b_s}{K^s}\le\frac{\sqrt\tau}{2},
\tag{23}
\]
while
\[
2Q+1=2K-1
\le
1+2\left(\frac{2b_s}{\sqrt\tau}\right)^{1/s}.
\tag{24}
\]
Taking `rho=mu sqrt(tau)/(2L)` in the proof gives the convenient bound
\[
\boxed{
 r_\tau(G)
 \le
 \left[
 1+2\left(\frac{2B_s}{\mu\sqrt\tau}\right)^{1/s}
 \right]
 \left[
 1+\frac{H\Delta L}{2\mu\sqrt\tau}
 \right].
}
\tag{25}
\]
For `s=1`,
\[
\boxed{
 r_\tau(G)
 \le
 \left(1+\frac{4B_1}{\mu\sqrt\tau}\right)
 \left(1+\frac{H\Delta L}{2\mu\sqrt\tau}\right).
}
\tag{26}
\]
For a strongly continuous circle representation, `B_1` is the norm of the infinitesimal phase generator applied to the centered output, uniformly along the carrier, whenever those vectors lie in the generator domain. Thus (26) has the concrete interpretation that controlled angular derivative energy and controlled height resolution jointly bound bow effective rank.

## Consequence under the sharp generic height scaling

Suppose `H Delta <= 1`, write `r=r_tau(G)`, and assume the generic `WI-349` height-resolution scale
\[
\frac L\mu\le C\sqrt r.
\tag{27}
\]
Combining (25) and (27) gives
\[
1+2\left(\frac{2b_s}{\sqrt\tau}\right)^{1/s}
\ge
\frac{r}{1+C\sqrt r/(2\sqrt\tau)}.
\tag{28}
\]
Hence
\[
\boxed{
\frac{B_s}{\mu}
\ge
\frac{\sqrt\tau}{2}
\left[
\frac12\left(
\frac{r}{1+C\sqrt r/(2\sqrt\tau)}-1
\right)
\right]_+^s.
}
\tag{29}
\]
In particular, as `r -> infinity`,
\[
\boxed{
\frac{B_s}{\mu}
\ge
\left(\frac{\tau^{(s+1)/2}}{2C^s}+o(1)\right)r^{s/2}.
}
\tag{30}
\]
For the first charge moment,
\[
\boxed{
\frac{B_1}{\mu}
\ge
\left(\frac{\tau}{2C}+o(1)\right)\sqrt r.
}
\tag{31}
\]
Therefore the infinite-charge escape left open by `WI-350` is not free. At the already-sharp generic `L/mu=O(sqrt(r))` height cost, a successful equivariant construction must develop unbounded weighted phase frequency: every positive charge-Sobolev moment satisfying the theorem scales at least as `r^(s/2)`.

## Equality, sharpness, and what is actually being charged

The theorem does not claim that the powers in (25) or (30) are globally sharp. Three separate relaxations occur: the high-charge tail is bounded only by its weighted second moment, the height interval is covered independently of the charge distribution, and the low-rank approximation step retains only total squared projection error. Correlations between height and charge could improve the constants or the exponents for a narrower feature class.

What *is* exact is the logical obstruction: bounded `B_s/mu`, bounded `H Delta`, and the `O(sqrt(r))` height-resolution law cannot coexist with unbounded effective rank. Infinite formal support is irrelevant if its weighted tail decays uniformly fast enough.

Conversely, (30) does not rule out a natural arithmetic witness whose charge moment genuinely diverges at the required rate. Such divergence may be precisely how distinguished arithmetic information escapes the generic geometric obstruction. The finding therefore converts an unconstrained escape (`infinitely many charges`) into a quantitative structural requirement (`growing weighted charge energy`).

## Relation to nearby findings

- `WI-347` is the one-charge endpoint.
- `WI-350` treats finite active charge dimension `D`; choosing a hard cutoff with no tail recovers the same mechanism with `D<=2Q+1`.
- `WI-349` shows that the generic phase-sensitive bow covering cost `L/mu=Theta(sqrt(r))` is achievable without a charge-complexity restriction. Equations (29)--(31) show what an equivariant feature must additionally pay if it remains in that height-resolution regime.
- The accepted distinguished-twist clue remains unresolved. This theorem narrows the admissible witness class but supplies no signed covariance or arithmetic cancellation by itself.

## Prior-art audit

The audit covered compact-group/Peter--Weyl decomposition, Fourier/Sobolev tail estimates on the circle, low-rank approximation/singular-value tails, and repository searches for previous `weil_inertia` results involving charge moments, angular Sobolev norms, Fourier tails, or generator norms.

The ingredients are classical. For `S^1`, irreducible continuous unitary representations are integer characters; the orthogonal decomposition (5) is the compact-abelian specialization of Peter--Weyl/Pontryagin theory. Equation (11) is the elementary weighted-Fourier-tail estimate underlying the standard Fourier characterization of Sobolev regularity. Equation (20) is the same classical Eckart--Young low-rank approximation step already used in `WI-350`.

No source located in this audit states the bow-specific combination (10), (25), or the growth consequence (30). That negative search is **not** a priority claim. The durable novelty assertion is only local: the preceding `WI` findings inspected in this pass stop at a hard active-charge count and do not contain the weighted-tail extension.

## Sources and provenance

- *Encyclopedia of Mathematics*, “Peter-Weyl theorem”, https://encyclopediaofmath.org/wiki/Peter-Weyl_theorem. Role: classical compact-group representation decomposition; for the circle, the irreducibles are the integer characters used in (5).
- *Encyclopedia of Mathematics*, “Pontryagin duality”, https://encyclopediaofmath.org/wiki/Pontryagin_duality. Role: standard character-group description for locally compact abelian groups; the dual of `S^1` is the integer charge lattice.
- C. Eckart and G. Young, “The Approximation of One Matrix by Another of Lower Rank”, *Psychometrika* **1** (1936), 211--218, DOI `10.1007/BF02288367`. Role: classical low-rank approximation principle behind (20).
- `WI-348`--`WI-350` are the direct local provenance for the physical bow metric, the generic phase-sensitive covering law and its sharpness, and the finite-charge effective-rank obstruction.

No external theorem beyond these classical mechanisms is required for the weighted tail inequality (11); it follows directly from definition (6) and orthogonality of the charge projections.

## Evidence state

**Classification:** `EXACT-DERIVED + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + NON-RH`.

The result is an exact Hilbert-space deduction from the stated bow geometry, equivariance, transmission floor, and charge-moment hypothesis. It uses no numerical experiment, zeta correlation conjecture, wider-support explicit formula, or external finite certificate. Its arithmetic relevance is conditional only in the ordinary sense that a future bow witness would have to satisfy the hypotheses before the obstruction applies.

## Failure modes and falsification boundary

The conclusion may be evaded by any of the explicit escape mechanisms: `B_s/mu` may grow at the required rate or faster; `L/mu` may grow faster than the generic square-root law; the transmission floor may collapse; `H Delta` may grow; the map may fail `U(1)` equivariance or strong continuity; the feature may depend explicitly on height; or the successful mechanism may not be representable by a PSD Gram feature at all.

The theorem would be falsified by an example satisfying (1)--(6) and (9) whose Gram tail violates (10). Because the proof reduces to orthogonal charge truncation, a one-dimensional height cover, and the singular-value tail variational principle, those are the three load-bearing steps to audit.

## Consequence for the research line

`WI-350` left “infinite charge support” as a qualitative escape. This finding shows that the relevant quantity is not support cardinality but **weighted charge energy**. At the generic sharp bow resolution scale, useful equivariant features must become increasingly oscillatory in the phase variable, quantitatively at least as in (30).

That redirects the source-specific question. Instead of asking only whether a distinguished-twist observable has finitely or infinitely many charges, one should ask whether the arithmetic construction supplies a uniform bound on an angular generator/Sobolev norm. Such a bound would extend the no-go barrier to the infinite-support case; failure of such a bound would identify the necessary phase-frequency growth that any successful distinguished covariance must exploit.