# PC-222 — common-anchor Mangoldt weighting selects only prime-primary axes

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most canonical sector-weighting repair left open by PC-221: use the **common-anchor von Mangoldt observable itself** to weight exact-order conductor sectors before they are summed or eliminated.

This source-forced scalar weighting does not recover the mixed-conductor information lost by the unweighted resolution of the identity. On the exact-order decomposition of `H_n=L^2(Z/nZ)`, the anchor observable

\[
\mathcal A_n:=\sum_{d\mid n}\Lambda(d)P_d
\]

has support only on the prime-power exact-order axes. More strongly, **every scalar functional calculus of this observable** has the exact form

\[
\boxed{
f(\mathcal A_n)
=f(0)I+
\sum_{p\mid n}
\bigl(f(\log p)-f(0)\bigr)
\left(\sum_{a=1}^{v_p(n)}P_{p^a}\right).
}
\tag{1}
\]

Thus no weight depending only on the common-anchor scalar `Lambda(d)` can distinguish two mixed-prime conductor sectors: every such sector has eigenvalue `0` and receives the same weight `f(0)`.

For squarefree mixed `N`, which is the live transverse branch of PC-214/PC-215, this becomes even sharper. The weighted lower-conductor response equals the unweighted PC-221 response plus corrections through **single-prime exact-order channels only**. With the cyclotomic coefficient mask `M=M_{g_N}`, direct Mangoldt weighting gives

\[
\boxed{
P_NM\mathcal A_NMP_N
=\sum_{p\mid N}(\log p)\,L_{N,p}^*L_{N,p},
\qquad
L_{N,p}:=P_pMP_N.
}
\tag{2}
\]

Each `L_{N,p}` has rank `p-1`, and in fact has flat nonzero singular spectrum:

\[
\boxed{
L_{N,p}L_{N,p}^*=\alpha_{N,p}I_{E_p},
\qquad
L_{N,p}^*L_{N,p}=\alpha_{N,p}\Pi_{N,p},
}
\tag{3}
\]

where `Pi_{N,p}` is an orthogonal projection of rank `p-1`. Hence the direct source-forced repair is a weighted sum of prime-axis projections, not a bulk mixed-conductor operator. For primorial-type levels its rank is negligible compared with `dim E_N=phi(N)`.

This is a decisive boundary, not a new RH mechanism. It closes **scalar common-anchor weighting** as a way to make the full lower-conductor sum of PC-221 arithmetically rich. It does **not** close repeated mask-mediated words that move between different prime axes, nor the noncommuting principal-angle geometry of the projections `Pi_{N,p}`; those remain genuinely different tests.

## 1. Exact-order setting and the anchor conductor operator

Use the exact-order orthogonal decomposition already isolated in PC-066 and used throughout PC-220/PC-221:

\[
\mathcal H_n
=\bigoplus_{d\mid n}E_d,
\qquad
I=\sum_{d\mid n}P_d,
\tag{4}
\]

where `P_d` projects onto the Fourier characters of exact additive order `d`.

The common anchored vertex gives the exact Prime-Circle identity of PC-001,

\[
\log\Phi_d(1)=\Lambda(d).
\tag{5}
\]

If this intrinsic scalar is used as the conductor-sector weight, the canonical operator is therefore

\[
\boxed{
\mathcal A_n
:=\sum_{d\mid n}\Lambda(d)P_d.
}
\tag{6}
\]

No external divisor ordering or spectral parameter has been inserted: `mathcal A_n` is simply the diagonal operator whose value on the exact-order sector `E_d` is the scalar already measured at the common anchor.

Let `p^e || n`. Since

\[
\Lambda(d)\ne0
\iff d=p^a,
\qquad
\Lambda(p^a)=\log p,
\tag{7}
\]

(6) immediately becomes

\[
\boxed{
\mathcal A_n
=\sum_{p\mid n}(\log p)
\sum_{a=1}^{v_p(n)}P_{p^a}.
}
\tag{8}
\]

Define the `p`-primary exact-order projection

\[
R_{p^e}:=\sum_{a=0}^{e}P_{p^a}.
\tag{9}
\]

Then

\[
\boxed{
\mathcal A_n
=\sum_{p^e\parallel n}(\log p)(R_{p^e}-P_1).
}
\tag{10}
\]

The summands in (10) have mutually orthogonal ranges. Consequently

\[
\boxed{
\operatorname{rank}\mathcal A_n
=\sum_{p^e\parallel n}\sum_{a=1}^{e}\varphi(p^a)
=\sum_{p^e\parallel n}(p^e-1).
}
\tag{11}
\]

Thus the exact common-anchor signal is already sparse in conductor space: it occupies only the prime-primary coordinate axes and vanishes on every exact-order sector involving at least two distinct primes.

## 2. Position-space kernel is a sum of prime-primary congruence blocks

The standard coordinate matrix of an exact-order projector is

\[
(P_d)_{x,y}=\frac1n c_d(x-y),
\tag{12}
\]

with `c_d` the Ramanujan sum. The elementary prime-power identity

\[
\sum_{a=0}^{e}c_{p^a}(t)
=p^e\,\mathbf 1_{p^e\mid t}
\tag{13}
\]

therefore gives

\[
\sum_{a=1}^{e}c_{p^a}(t)
=p^e\,\mathbf 1_{p^e\mid t}-1.
\tag{14}
\]

Substituting into (8),

\[
\boxed{
(\mathcal A_n)_{x,y}
=\frac1n
\sum_{p^e\parallel n}
(\log p)
\left(
p^e\mathbf 1_{x\equiv y\pmod{p^e}}-1
\right).
}
\tag{15}
\]

So even before Fourier diagonalization the anchor-derived operator is not a hidden mixed-prime kernel. It is an additive superposition of prime-primary congruence blocks. The geometry has supplied the coefficients `log p`, but it has not created interactions involving two or more prime coordinates at once.

As exact controls, (11) gives

\[
\operatorname{rank}\mathcal A_{12}=5,
\qquad
\operatorname{rank}\mathcal A_{18}=9,
\qquad
\operatorname{rank}\mathcal A_{30}=7,
\qquad
\operatorname{rank}\mathcal A_{60}=9.
\tag{16}
\]

Direct construction from the Ramanujan projector matrices agrees with (15) in these cases.

## 3. Any scalar function of the anchor signal has the same collapse

The obstruction is not limited to linear Mangoldt weighting. The spectrum of `mathcal A_n` is contained in

\[
\{0\}\cup\{\log p:p\mid n\}.
\tag{17}
\]

Every mixed-prime sector `E_d` lies in the `0` eigenspace, while every `E_{p^a}` for a fixed prime `p` lies in the same `log p` eigenspace. Therefore, for **any** scalar function `f` defined on (17), spectral calculus gives exactly (1):

\[
 f(\mathcal A_n)
=f(0)I+
\sum_{p\mid n}
\bigl(f(\log p)-f(0)\bigr)
\sum_{a=1}^{v_p(n)}P_{p^a}.
\tag{18}
\]

This proves a stronger no-go than merely observing that `Lambda(d)` vanishes on mixed conductors. No polynomial, analytic function, resolvent, heat kernel, exponential, threshold, or other scalar functional calculus of the common-anchor observable can separate mixed exact-order sectors. All of them are identical on the entire mixed-conductor subspace.

For a squarefree mixed level

\[
N=\prod_{p\mid N}p,
\qquad \omega(N)\ge2,
\tag{19}
\]

we have simply

\[
\boxed{
\mathcal A_N=\sum_{p\mid N}(\log p)P_p,
}
\tag{20}
\]

and

\[
\boxed{
f(\mathcal A_N)
=f(0)I+
\sum_{p\mid N}
\bigl(f(\log p)-f(0)\bigr)P_p.
}
\tag{21}
\]

This is exactly the regime where PC-214/PC-215 found growing mixed-prime transverse locality, so the mismatch is structural: the live mixed-coordinate geometry sits in sectors on which the anchor scalar is identically zero.

## 4. Weighted lower-conductor paths reduce to PC-221 plus prime axes

Let

\[
P:=P_N,
\qquad
Q:=I-P_N
\tag{22}
\]

for squarefree mixed `N`. PC-221 showed that an **unweighted** complete sum over lower exact-order conductors collapses because `Q` is just the sum of all proper-sector projectors.

The most direct source-forced repair is to weight those sectors by a scalar function of the common-anchor value. Define

\[
W_{f,N}^{<}
:=\sum_{\substack{d\mid N\\d<N}}
f(\Lambda(d))P_d.
\tag{23}
\]

Since `Lambda(N)=0` and only the prime divisors have nonzero Mangoldt value among proper squarefree divisors, (21) gives the exact decomposition

\[
\boxed{
W_{f,N}^{<}
=f(0)Q+
\sum_{p\mid N}
\bigl(f(\log p)-f(0)\bigr)P_p.
}
\tag{24}
\]

Hence for arbitrary multiplication masks `M_u,M_v` on the same finite circle,

\[
\boxed{
\begin{aligned}
P_NM_uW_{f,N}^{<}M_vP_N
={}&f(0)P_NM_uQM_vP_N\\
&+\sum_{p\mid N}
\bigl(f(\log p)-f(0)\bigr)
P_NM_uP_pM_vP_N.
\end{aligned}
}
\tag{25}
\]

The first term is exactly the unweighted all-lower-sector response classified by PC-221. The entire correction allowed by a scalar function of the anchor observable consists of **single-prime channels**.

For direct von Mangoldt weighting, `f(t)=t`, the unweighted term disappears and

\[
\boxed{
P_NM_u\mathcal A_NM_vP_N
=\sum_{p\mid N}(\log p)
P_NM_uP_pM_vP_N.
}
\tag{26}
\]

Thus the canonical anchor weight does not reveal the mixed conductor lattice hidden by the unweighted sum. It removes that lattice almost completely and keeps only its one-prime coordinate axes.

## 5. With the cyclotomic mask, each surviving prime channel is a flat partial isometry

Specialize now to the source-derived normalized cyclotomic coefficient mask of PC-212/PC-220/PC-221,

\[
M=M_{g_N},
\qquad
\widehat g_N(k)
=\frac{\Phi_N(\zeta_N^{-k})}{\sqrt{Nh_N}},
\tag{27}
\]

for which PC-221 proved

\[
\widehat g_N(k)=0
\iff k\in U(N).
\tag{28}
\]

For each prime `p|N`, put

\[
L_{N,p}:=P_pMP_N:E_N\to E_p.
\tag{29}
\]

In Fourier coordinates, with output frequency `alpha` of exact order `p` and input frequency `beta in U(N)`,

\[
(L_{N,p})_{\alpha,\beta}
=\widehat g_N(\alpha-\beta).
\tag{30}
\]

Use the CRT decomposition of `Z/NZ`. A frequency of exact order `p` has nonzero `p`-coordinate and zero coordinates at every `q|N`, `q!=p`; a unit frequency has every prime coordinate nonzero. Therefore all `q!=p` coordinates of `alpha-beta` are automatically nonzero, while its `p`-coordinate vanishes exactly when

\[
\alpha_p=\beta_p.
\tag{31}
\]

By (28), (30) is nonzero **exactly** in case (31). Consequently:

- distinct output rows `alpha` have disjoint supports in the unit-frequency input set, because they impose different values of `beta_p`;
- after fixing `alpha_p=beta_p`, the remaining differences run once through the exact-order `N/p` frequencies, independently of the chosen nonzero value of `alpha_p`.

The rows are therefore pairwise orthogonal and have identical norm. This proves (3), with

\[
\boxed{
\alpha_{N,p}
=\frac1{Nh_N}
\sum_{u\in U(N/p)}
\left|\Phi_N(\zeta_{N/p}^{u})\right|^2
>0.
}
\tag{32}
\]

Equivalently, there is an orthogonal projection `Pi_{N,p}` on `E_N`, of rank `p-1`, such that

\[
L_{N,p}^*L_{N,p}=\alpha_{N,p}\Pi_{N,p}.
\tag{33}
\]

The direct common-anchor response (2) therefore has the completely explicit structural form

\[
\boxed{
S_N:=P_NM\mathcal A_NMP_N
=\sum_{p\mid N}
(\log p)\alpha_{N,p}\Pi_{N,p}.
}
\tag{34}
\]

In particular,

\[
\boxed{
\operatorname{rank}S_N
\le
\sum_{p\mid N}(p-1).
}
\tag{35}
\]

For comparison,

\[
\dim E_N=\varphi(N)=\prod_{p\mid N}(p-1).
\tag{36}
\]

For the first few mixed controls,

\[
\begin{array}{c|c|c}
N & \sum_{p\mid N}(p-1) & \varphi(N)\\ \hline
30 & 7 & 8\\
210 & 13 & 48\\
2310 & 23 & 480
\end{array}
\tag{37}
\]

and the ratio in (35)--(36) tends rapidly to zero along primorial levels. Thus the source-forced scalar weighting does not turn the growing `omega(N)-1` mixed-coordinate locality of PC-215 into a bulk operator on the primitive sector.

Equation (34) should not be overread. The projections `Pi_{N,p}` need not commute for different primes. Exact finite checks already show nonzero commutators at squarefree levels such as `N=105`. Their mutual principal-angle geometry can therefore still carry genuinely collective information even though each individual channel is flat.

## 6. Prior-art and novelty audit

The ingredients responsible for the collapse are classical.

The exact-period decomposition (4) and Ramanujan projectors are standard finite Fourier/Ramanujan-subspace theory and are already anchored for PC-066 and PC-221. The support and values of `Lambda(d)` in (7) are the elementary von Mangoldt prime-power identity already realized geometrically by PC-001. Equations (13)--(15) are standard Ramanujan-sum divisor identities. Scalar functional calculus of an orthogonal spectral resolution is elementary operator theory.

A directed literature search around von-Mangoldt-weighted Ramanujan sums, exact-period/Ramanujan subspaces, cyclotomic exact-order projectors, and Bost--Connes-type conductor dynamics found the expected classical surroundings: Ramanujan subspaces decompose finite signals by exact divisor periods, while arithmetic diagonal dynamics on cyclotomic data is already a well-developed theme. No source located the exact project-specific combination (24)--(34). That absence is **not** evidence of novelty: the central classification follows immediately once the source-derived anchor value is combined with the standard exact-order projectors.

The decisive matched control is stronger than a bibliography search. Replace `Lambda(d)` by any scalar observable `w(d)=f(Lambda(d))`. Then every mixed-prime conductor still receives exactly the same value `f(0)`, and (18), (24), and (25) remain valid. Hence the obstruction is caused by the information content of the common-anchor scalar itself, not by the special choice of a particular operator wrapper.

Conversely, assigning independent weights to mixed conductors by hand would evade this theorem but would also abandon the source-forced premise. A weight such as an arbitrary `h(d)` can encode as much divisor information as desired; PC-066 already explains why such a diagonal conductor multiplier is not an intrinsic RH mechanism merely because it can be written spectrally.

Nothing in (1)--(35) creates a spectral variable tied to zeta zeros, a gamma factor, an `s <-> 1-s` symmetry, or a critical-line constraint. The result is therefore a **classicalization and boundary theorem**, not progress toward RH by itself.

## 7. Consequence for the live frontier

PC-221 left one immediate repair deliberately open: if summing every lower conductor with equal weight is only insertion of the identity, perhaps the original Prime-Circle geometry supplies a canonical nonuniform sector weight. PC-001 supplies exactly one obvious scalar candidate, `Lambda(d)` at the common anchor.

PC-222 shows that this candidate is too compressed. Any scalar use of that anchor signal has only the spectral values `0` and `log p`; it can distinguish prime-primary axes but **cannot distinguish mixed-prime conductor sectors at all**. In the squarefree transverse branch, the direct cyclotomic-mask response is only the sum (34) of rank-`p-1` prime-channel projections.

The surviving question is correspondingly narrower and more structural. A successful collective mechanism cannot obtain rich mixed-conductor weights from scalar functional calculus of the common-anchor potential. It must instead use information that exists **before** that scalar collapse: for example repeated mask-mediated transitions between distinct prime axes, noncommuting words or principal-angle invariants of the `Pi_{N,p}`, genuinely cross-level composition, or another intrinsically geometric observable that already couples multiple prime coordinates.

In particular, PC-222 does **not** assert that

\[
P_NM\mathcal A_NM\mathcal A_NMP_N
\]

or longer alternating words are trivial. Those operators can move from one prime axis to another through `M`, and (34) does not diagonalize their relative geometry. The exact boundary is only the scalar-sector-weighting repair itself: **common-anchor Mangoldt data can select the prime axes, but it cannot by itself supply the mixed-conductor dynamics that PC-215 indicates would be needed.**
