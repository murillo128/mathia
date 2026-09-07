# ANF-088 — Montgomery--Taylor excess is an exact projection tax

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + NEAR-EQUALITY-RIGIDITY + PROJECTION-TAX + HILBERT-SCHMIDT-STABILITY`. `ANF-087` classifies the exact Montgomery--Taylor equality set and records Lamzouri's adapted-basis deficit identity. Keeping all projection terms in Lamzouri's first-range calculation and using the strict interior positivity of the exact Montgomery--Taylor factor gives a stronger quantitative statement: the adapted dimensions are always saturated, and the whole excess is exactly the sum of a canonical tensor-distance term, discrete multiplicity taxes, simple-real projection leakage, nonreal antisymmetric projection leakage, and the negative final-range tail.

For every nonempty finite conjugation-invariant multiset `W`, retain the notation of `ANF-087`:

\[
E_{\rm MT}(W)=\sum_{z,w\in W}K(z-w)^2,
\qquad
L(W)=2|W|-\sigma(W),
\qquad
\Delta(W):=E_{\rm MT}(W)-L(W)\ge0.
\tag{1}
\]

Let `R_1` be the distinct simple real sites, `R_2` the distinct real sites of multiplicity at least two, choose one representative from each distinct nonreal conjugate pair, and write

\[
n:=|R_1|,
\qquad r:=|R_2|,
\qquad k:=\#\{\text{nonreal conjugate pairs}\}.
\tag{2}
\]

With Lamzouri's functions

\[
f_z(u)=\eta_{\rm MT}(u)e^{-2\pi iuz},
\qquad
g_z=\frac{f_z+f_{\bar z}}2,
\qquad
h_z=\frac{f_z-f_{\bar z}}{2i},
\tag{3}
\]

let `U subset V subset mathcal W` and the adapted orthonormal basis `psi_j` be as in `ANF-087`, and put

\[
\Psi_j(u,v)=\psi_j(u)\psi_j(v),
\qquad
\alpha_j=\langle\mathcal F,\Psi_j\rangle,
\qquad
\mathcal F(u,v)=\sum_{z\in W}f_z(u)f_z(v).
\tag{4}
\]

Then the exact Montgomery--Taylor profile satisfies

\[
\boxed{
D_U=r+k,
\qquad
D_V=n+r+k,
\qquad
D_W=n+r+2k.
}
\tag{5}
\]

Define the canonical equality-signature tensor

\[
\mathcal T_W
:=2\sum_{j\le D_U}\Psi_j
+\sum_{D_U<j\le D_V}\Psi_j.
\tag{6}
\]

The excess has the exact decomposition

\[
\boxed{
\begin{aligned}
\Delta(W)
={}&\|\mathcal F-\mathcal T_W\|_2^2\\
&+2\sum_{x\in R_1}\|P_Uf_x\|_2^2
+2\sum_{x\in R_2}(m_x-2)\\
&+4\sum_z(m_z-1)
+4\sum_zm_z\,\|(I-P_U)h_z\|_2^2\\
&+2\sum_{j>D_V}(-\alpha_j).
\end{aligned}}
\tag{7}
\]

Every term on the right is nonnegative. In particular,

\[
\boxed{
\|\mathcal F-\mathcal T_W\|_2\le\sqrt{\Delta(W)},
\qquad
\sum_zm_z\,\operatorname{dist}(h_z,U)^2\le\frac{\Delta(W)}4,
}
\tag{8}
\]

and

\[
\boxed{
\sum_{x\in R_1}\|P_Uf_x\|_2^2\le\frac{\Delta(W)}2,
\qquad
2\sum_{x\in R_2}(m_x-2)+4\sum_z(m_z-1)\le\Delta(W).
}
\tag{9}
\]

Thus a Montgomery--Taylor near-extremizer is not merely close in the scalar energy. Its Hilbert tensor is close to the exact `2/1/0` equality signature; simple-real modes are nearly orthogonal to the repeated/nonreal symmetric span; and every antisymmetric nonreal mode is forced close to that span. The only way a genuinely complex sequence can approach equality is therefore through quantitative ill-conditioning of a finite exponential system.

## 1. The adapted dimensions are identically saturated

For the exact extremizer,

\[
\eta_{\rm MT}(u)>0
\qquad(-1/2<u<1/2).
\tag{10}
\]

After division by `eta_MT`, every `f_w` becomes the exponential `e^{-2 pi iuw}`. Finite exponentials with distinct complex frequencies are linearly independent on any open real interval: differentiating a finite relation at one interior point gives a Vandermonde system.

Consider first the generators of `U`. A relation

\[
\sum_{x\in R_2}a_xf_x+
\sum_z b_zg_z=0
\tag{11}
\]

expands, after division by `eta_MT`, into a relation among the distinct frequencies `x`, `z`, and `bar z`. The coefficients of `z` and `bar z` are both `b_z/2`, hence exponential independence forces every `a_x` and `b_z` to vanish. Therefore the `r+k` displayed generators of `U` are independent and

\[
D_U=r+k.
\tag{12}
\]

Adding the `n` distinct simple-real exponentials preserves independence, so

\[
D_V=n+r+k.
\tag{13}
\]

Finally, for each nonreal pair the change of variables

\[
(f_z,f_{\bar z})
\longleftrightarrow
(g_z,h_z)
\tag{14}
\]

is invertible. Hence adjoining all `h_z` gives the full family of distinct frequencies, proving

\[
D_W=n+r+2k.
\tag{15}
\]

In particular the integer dimension defect `n-(D_V-D_U)` in `ANF-087` vanishes **for every configuration**, not merely when `Delta<1`. Likewise there is no hidden rank-loss term `r+k-D_U`: near equality can only make the relevant Gram matrices badly conditioned, never exactly singular.

## 2. The first-range slack is itself an exact geometric tax

Write

\[
A_U:=\sum_{j\le D_U}\alpha_j.
\tag{16}
\]

Lamzouri's coefficient formula, Parseval on the vectors already lying in `U`, and orthogonal projection for the remaining vectors give

\[
\begin{aligned}
A_U
={}&\sum_{x\in R_1}\|P_Uf_x\|_2^2
+\sum_{x\in R_2}m_x\\
&+2\sum_zm_z
\left(\|g_z\|_2^2-\|P_Uh_z\|_2^2\right).
\end{aligned}
\tag{17}
\]

This is the corrected exact version of the first-range expression: the simple-real projection term is nonnegative and may be discarded for Lamzouri's inequality, but it cannot be omitted from an equality sign away from the endpoint.

Lamzouri's norm identity is

\[
\|g_z\|_2^2-\|h_z\|_2^2=1.
\tag{18}
\]

Since

\[
\|g_z\|_2^2-\|P_Uh_z\|_2^2
=1+\|(I-P_U)h_z\|_2^2,
\tag{19}
\]

and `D_U=r+k`, subtracting `2D_U` from (17) yields the exact nonnegative identity

\[
\boxed{
\begin{aligned}
A_U-2D_U
={}&\sum_{x\in R_1}\|P_Uf_x\|_2^2
+\sum_{x\in R_2}(m_x-2)\\
&+2\sum_z(m_z-1)
+2\sum_zm_z\,\|(I-P_U)h_z\|_2^2.
\end{aligned}}
\tag{20}
\]

This separates four distinct mechanisms that Lamzouri's lower bound deliberately merges: simple-real leakage into `U`, excess multiplicity at repeated real sites, excess multiplicity of nonreal pairs, and failure of antisymmetric nonreal directions to lie in `U`.

## 3. Completing the Bessel squares gives the canonical tensor distance

`ANF-087` gives the exact adapted-basis deficit identity

\[
\begin{aligned}
\Delta
={}&\mathcal B
+\sum_{j\le D_U}(\alpha_j-2)^2
+2(A_U-2D_U)\\
&+\sum_{D_U<j\le D_V}(\alpha_j-1)^2
+\sum_{j>D_V}(\alpha_j^2-2\alpha_j),
\end{aligned}
\tag{21}
\]

where the dimension defect has disappeared by (5),

\[
\mathcal B
=\|\mathcal F\|_2^2-
\sum_{j=1}^{D_W}\alpha_j^2,
\tag{22}
\]

and Lamzouri's final-range sign gives `alpha_j<=0` for `j>D_V`.

Because the `Psi_j` are orthonormal and `alpha_j=<mathcal F,Psi_j>`, the definition (6) gives exactly

\[
\begin{aligned}
\|\mathcal F-\mathcal T_W\|_2^2
={}&\mathcal B
+\sum_{j\le D_U}(\alpha_j-2)^2\\
&+\sum_{D_U<j\le D_V}(\alpha_j-1)^2
+\sum_{j>D_V}\alpha_j^2.
\end{aligned}
\tag{23}
\]

Subtracting (23) from (21) therefore leaves only

\[
\Delta
=\|\mathcal F-\mathcal T_W\|_2^2
+2(A_U-2D_U)
+2\sum_{j>D_V}(-\alpha_j).
\tag{24}
\]

Substitution of (20) is precisely (7). No estimate is used in this final step.

A useful side consequence is

\[
\sum_{j>D_V}|\alpha_j|\le\frac{\Delta}2,
\qquad
\sum_{j>D_V}\alpha_j^2\le\Delta,
\tag{25}
\]

so the negative spectral tail is controlled simultaneously in `l^1` and `l^2`.

## 4. Small excess freezes the discrete multiplicity defects

The multiplicity terms in (7) are integer-valued after their displayed coefficients. Consequently

\[
\Delta<2
\quad\Longrightarrow\quad
m_x=2\ \text{for every }x\in R_2,
\qquad
m_z=1\ \text{for every nonreal pair}.
\tag{26}
\]

More generally, if `Delta<=epsilon L(W)`, then

\[
\sum_{x\in R_2}(m_x-2)
+2\sum_z(m_z-1)
\le\frac{\epsilon}{2}L(W).
\tag{27}
\]

Thus relative near-extremality allows multiplicity defects only on an `O(epsilon)` fraction of the available affine budget. The remaining complex obstruction is continuous rather than combinatorial: the antisymmetric directions must have small Schur complements against `U`.

Indeed, choose any ordered generator basis `u_1,...,u_{r+k}` of `U` and let `G_U` be its Gram matrix. Equation (12) makes `G_U` positive definite. For each nonreal representative `z`, standard Gram geometry gives

\[
\boxed{
\operatorname{dist}(h_z,U)^2
=
\frac{\det G(u_1,\ldots,u_{r+k},h_z)}{\det G_U}.
}
\tag{28}
\]

Hence the nonreal projection tax in (7) is exactly a sum of Gram/Schur-complement defects. There is no algebraic rank-loss loophole: a near-extremizing complex family must instead drive these positive determinants anomalously small relative to the conditioning of its base Gram matrices.

## 5. Consequence for the `ANF-086` frontier

`ANF-086` shows that any configuration defeating the fixed central-notch certificate must satisfy two simultaneous conditions: it lies a fixed positive destination-Hilbert distance from every compatible separable carrier, and it is Montgomery--Taylor near-extremal. `ANF-087` identifies the exact endpoint. Equation (7) now identifies what a hypothetical near-endpoint counterexample has to do internally.

If `Delta(W_j)->0`, then automatically

\[
\|\mathcal F_j-\mathcal T_{W_j}\|_2\to0,
\qquad
\sum_zm_z\operatorname{dist}(h_z,U_j)^2\to0,
\qquad
\sum_{x\in R_1}\|P_{U_j}f_x\|_2^2\to0,
\tag{29}
\]

with all multiplicities eventually canonical whenever the excess is absolutely below two. Thus the surviving all-cardinality gate is no longer an unspecified stability problem for Lamzouri's inequality. It is a **conditioning-to-geometry problem**: determine whether the projection-collapse regime in (29), together with the canonical `2/1/0` tensor signature, forces `d_sep(W_j)->0`, or construct a growing family whose exponential Gram systems become sufficiently ill-conditioned that (29) holds while `d_sep` stays bounded below.

This formulation also explains why generic finite-dimensional compactness is insufficient. Classical Ingham/Riesz-sequence inequalities give quantitative lower frame bounds when frequencies obey suitable separation hypotheses; conversely, the nonharmonic Fourier literature explicitly treats the loss of conditioning when frequency gaps collapse. Those theories are the correct neighboring tools for separated subclasses, but the current Mathia gate permits growing cardinality, unbounded geometry, and no uniform separation hypothesis.

## 6. Prior art, audit, and evidence boundary

The load-bearing external input remains Lamzouri's Proposition 2.1 and its nested-space/Bessel proof, already anchored in `research/analytic_frontier/SOURCES.md`. The only additional ingredients are elementary Hilbert-space projection identities, Gram determinants, and linear independence of finite exponentials on an interval. A targeted prior-art search for quantitative nonharmonic-Fourier stability confirms that Ingham/Riesz-sequence theory is the mature neighboring framework under frequency-separation assumptions; no such separation theorem is imported into (5)--(29), so no new source anchor is required.

The audit has three important boundaries. First, (5) uses the strict positivity of the **exact** Montgomery--Taylor `eta_MT` on an open interval; for a generic compactly supported factor with interior zeros, the dimension argument must be rechecked. Second, (7) is basis-adapted: `mathcal T_W` depends on the nested spaces generated by `W` and is not asserted to be the tensor of an actual separable multiset. Converting its Hilbert closeness into the `J_s`-destination distance `d_sep` is precisely the unresolved step. Third, small **relative** excess `Delta/L` does not imply the absolute threshold `Delta<2` when cardinality grows, so (26) cannot be applied indiscriminately in the thermodynamic regime; the averaged bound (27) is the correct statement there.

The result does not prove the central-notch inequality for all complex multisets, improve the zeta proportion, or establish a uniform near-extremizer modulus. Its durable effect is to replace the abstract Montgomery--Taylor near-equality gate by an exact positive decomposition whose only genuinely complex term is a finite-exponential projection/conditioning defect.