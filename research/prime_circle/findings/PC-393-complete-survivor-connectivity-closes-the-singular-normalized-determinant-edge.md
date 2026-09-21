# PC-393 — complete survivor connectivity closes the singular normalized determinant edge

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the singular normalized determinant/pseudodeterminant escape left open by PC-392.

PC-392 proved that the genuinely simultaneous multi-deletion Kron correction cannot produce an extensive normalized log-determinant law at fixed positive spectral gap, but its universal estimate used `(L_ind+lambda I)^{-1} <= lambda^{-1} I` and therefore became inconclusive as `lambda -> 0`, especially at the unregularized pseudodeterminant endpoint. For the intrinsic positive complete inverse-power chord Laplacians of PC-390--PC-392, that apparent singular edge can in fact be closed.

The missing input is geometric rather than spectral: before any deleted-vertex star mesh is added, the surviving boundary already carries a **complete positive chord graph**. On a fixed polynomial primorial window `H=p^u`, every direct survivor edge has conductance at least `c H^{-2 alpha}`. Hence the mean-zero spectral gap of the independent-star baseline is bounded below by `c |S| H^{-2 alpha}`. The gap can shrink polynomially, but not fast enough to compensate for the vanishing `O(log p/p)` rank fraction of the multi-deletion contrast sector.

More precisely, uniformly for every `lambda>=0` (with `lambda=0` interpreted through pseudodeterminants),

\[
0\le
\frac1{|S|}
\log\frac{\det_{\lambda}(L_{\rm red})}
{\det_{\lambda}(L_{\rm ind})}
\le
O_{\alpha,\tau,u}\!\left(\frac{(\log p)^2}{p}\right)
\longrightarrow0,
\tag{1}
\]

where for `lambda>0`, `det_lambda(L):=det(L+lambda I)`, while `det_0(L):=pdet(L)`. Thus **no nonnegative regularization scale, including the exact pseudodeterminant endpoint, can turn the fixed-window thin Kron contrast into a nonzero normalized log-determinant/free-energy density** in this positive complete chord-Laplacian family.

This closes the singular determinant branch left explicitly open by PC-392. It does not rule out unnormalized determinant changes, individual outliers, cross-level evolution of the `k-1` contrast sector, or signed/non-complete operators for which the direct positive edge floor disappears.

## 1. Setup inherited from PC-390--PC-392

Let `S` be the surviving boundary after one primorial sieve/refinement step, with

\[
m:=|S|,
\tag{2}
\]

and let `T` be the simultaneously deleted set, with `k:=|T|`. In the notation of PC-391/PC-392, the true simultaneous Kron reduction and the baseline obtained by summing the independent one-vertex star responses satisfy

\[
L_{\rm red}=L_{\rm ind}+\Delta_T,
\qquad
\Delta_T
=B\left[D^{-1}-(D+K)^{-1}\right]B^\top
=UCU^\top\succeq0.
\tag{3}
\]

PC-391 gives

\[
\operatorname{rank}\Delta_T\le k-1,
\tag{4}
\]

and PC-392 gives, for the normalized regularized inverse-power chord kernel,

\[
\operatorname{tr}\Delta_T\le C_{\alpha,\tau}k.
\tag{5}
\]

Both `L_ind` and `L_red` are weighted graph Laplacians, so

\[
L_{\rm ind}\mathbf1=L_{\rm red}\mathbf1=0,
\qquad
\Delta_T\mathbf1=0.
\tag{6}
\]

The underlying normalized chord conductance is

\[
\kappa_N(d)
=
N^{-2\alpha}
\left[
2\left(
\cosh\frac{\tau}{N}
-\cos\frac{2\pi d}{N}
\right)
\right]^{-\alpha},
\qquad
\alpha>0,\quad\tau\ge0,
\tag{7}
\]

with primorial conductor `N` and a fixed polynomial window

\[
H=p^u,\qquad u>1.
\tag{8}
\]

As in PC-390, `H/N -> 0`, and uniformly for integer separations `1<=d<=H`,

\[
\kappa_N(d)
=
\left(\tau^2+4\pi^2d^2\right)^{-\alpha}(1+o(1)).
\tag{9}
\]

In particular there is a constant `c_{alpha,tau}>0` such that, for all sufficiently large `p`, every direct edge between distinct surviving vertices in the window has weight

\[
\boxed{
\kappa_N(d)\ge c_{\alpha,\tau}H^{-2\alpha}.
}
\tag{10}
\]

The point of (10) is that it is a property of the original prime-circle chord geometry, not an externally imposed regularizer.

## 2. Complete survivor connectivity gives an intrinsic mean-zero spectral floor

Let `L_S` denote the direct weighted Laplacian on the survivor set before adding any independent deleted-vertex star meshes. Because the chord kernel is positive on every pair of distinct survivors, `L_S` is a complete positive weighted graph. The independent-star baseline is

\[
L_{\rm ind}=L_S+M_{\rm star},
\qquad
M_{\rm star}\succeq0,
\tag{11}
\]

where `M_star` is the sum of the one-vertex star-mesh contributions.

For every `x` with `x^\top\mathbf1=0`, (10) and the complete-graph identity give

\[
\begin{aligned}
x^\top L_Sx
&=\sum_{a<b}w_{ab}(x_a-x_b)^2\\
&\ge c_{\alpha,\tau}H^{-2\alpha}
\sum_{a<b}(x_a-x_b)^2\\
&=c_{\alpha,\tau}mH^{-2\alpha}\|x\|_2^2.
\end{aligned}
\tag{12}
\]

Therefore

\[
\boxed{
\lambda_2(L_{\rm ind})
\ge\lambda_2(L_S)
\ge c_{\alpha,\tau}mH^{-2\alpha}.
}
\tag{13}
\]

This is the key estimate missed by the full-space `lambda^{-1}` bound in PC-392. The only exact zero mode is the common constant vector, and the multi-deletion correction annihilates that same vector by (6). Thus the determinant contrast never needs to probe the singular constant direction.

## 3. The determinant ratio lives entirely on the mean-zero subspace

Write `\mathcal H_0:=\mathbf1^\perp`. Both Laplacians preserve `\mathcal H_0` and are strictly positive there. For `lambda>0`, the constant mode contributes the same scalar eigenvalue `lambda` to numerator and denominator, so it cancels exactly:

\[
\frac{\det(L_{\rm red}+\lambda I_m)}
{\det(L_{\rm ind}+\lambda I_m)}
=
\frac{\det_{\mathcal H_0}(L_{\rm red}+\lambda I)}
{\det_{\mathcal H_0}(L_{\rm ind}+\lambda I)}.
\tag{14}
\]

At `lambda=0`, because `L_ind` and `L_red` are connected Laplacians with the same one-dimensional kernel,

\[
\frac{\operatorname{pdet}L_{\rm red}}
{\operatorname{pdet}L_{\rm ind}}
=
\frac{\det_{\mathcal H_0}L_{\rm red}}
{\det_{\mathcal H_0}L_{\rm ind}}.
\tag{15}
\]

For every `lambda>=0`, define on `\mathcal H_0`

\[
X_\lambda
:=
\left(L_{\rm ind}|_{\mathcal H_0}+\lambda I\right)^{-1/2}
\Delta_T|_{\mathcal H_0}
\left(L_{\rm ind}|_{\mathcal H_0}+\lambda I\right)^{-1/2}
\succeq0.
\tag{16}
\]

Then both (14) and (15) are summarized by

\[
\boxed{
R_p(\lambda)
:=
\frac{\det_{\lambda}(L_{\rm red})}
{\det_{\lambda}(L_{\rm ind})}
=
\det_{\mathcal H_0}(I+X_\lambda),
\qquad \lambda\ge0.
}
\tag{17}
\]

Using the factorization `\Delta_T=UCU^\top`, the endpoint can also be written by the matrix determinant lemma as

\[
\boxed{
\frac{\operatorname{pdet}L_{\rm red}}
{\operatorname{pdet}L_{\rm ind}}
=
\det\!\left(
I_k+C^{1/2}U^\top L_{\rm ind}^{+}U C^{1/2}
\right),
}
\tag{18}
\]

where `L_ind^+` is the Moore--Penrose inverse. Equation (18) makes explicit that the unregularized determinant correction still lives on at most the `k-1` deleted-vertex contrast directions; passing to a pseudodeterminant creates no extra spectral dimensions.

## 4. Uniform control down to the exact pseudodeterminant endpoint

By (4),

\[
\operatorname{rank}X_\lambda\le k-1.
\tag{19}
\]

Because `\Delta_T\succeq0`, its operator norm is bounded by its trace. Combining (5) and (13), uniformly for all `lambda>=0`,

\[
\begin{aligned}
\|X_\lambda\|
&\le
\frac{\|\Delta_T\|}
{\lambda_2(L_{\rm ind})+\lambda}\\
&\le
\frac{C_{\alpha,\tau}k}
{c_{\alpha,\tau}mH^{-2\alpha}}\\
&\le C'_{\alpha,\tau}\frac{k}{m}H^{2\alpha}.
\end{aligned}
\tag{20}
\]

If `\mu_1,...,\mu_r` are the nonzero eigenvalues of `X_lambda`, with `r<=k-1`, then

\[
\begin{aligned}
0
&\le\frac1m\log R_p(\lambda)\\
&=\frac1m\sum_{j=1}^{r}\log(1+\mu_j)\\
&\le\frac{k}{m}
\log\!\left(
1+C'_{\alpha,\tau}\frac{k}{m}H^{2\alpha}
\right).
\end{aligned}
\tag{21}
\]

PC-391 established on every fixed polynomial window that

\[
\frac{k}{m}
=O\!\left(\frac{\log p}{p}\right).
\tag{22}
\]

With `H=p^u` and fixed `alpha,u`,

\[
\log\!\left(
1+C'\frac{k}{m}H^{2\alpha}
\right)
=O_{\alpha,u}(\log p).
\tag{23}
\]

Therefore

\[
\boxed{
\sup_{\lambda\ge0}
\frac1m\log R_p(\lambda)
=
O_{\alpha,\tau,u}\!\left(\frac{(\log p)^2}{p}\right)
\longrightarrow0.
}
\tag{24}
\]

The supremum includes `lambda=0` through (15)--(17). No condition such as `lambda_p >> (log p)/p` remains.

For `1<u<=2`, PC-391 already gives eventually `k=1`, hence `\Delta_T=0` exactly and (24) is trivial. The new content is the genuine multi-deletion range `u>2`, where `k` can diverge but its contrast sector remains too sparse to overcome the polynomial intrinsic conditioning supplied by the complete survivor graph.

## 5. Why PC-392's apparent threshold was not intrinsic

PC-392 used the valid but deliberately crude full-space estimate

\[
(L_{\rm ind}+\lambda I)^{-1}\preceq\lambda^{-1}I,
\tag{25}
\]

which must diverge as `lambda -> 0` because it includes the constant zero mode. The present calculation shows that this divergence is irrelevant to the contrast determinant: `\Delta_T\mathbf1=0`, so the constant mode cancels before any estimate is required.

On the only subspace that contributes, the inverse is controlled instead by the intrinsic gap (13). That gap is allowed to close as fast as a fixed power of the window size, but such polynomial growth contributes only `O(log p)` per exceptional contrast eigenvalue after taking a logarithm. Since the number of exceptional directions is only an `O(log p/p)` fraction of the survivor space, their total normalized logarithmic contribution still vanishes.

Thus the `(log p)/p` threshold in PC-392 was a boundary of that universal `lambda^{-1}` estimate, not a genuine spectral transition of this positive complete chord geometry.

## 6. Prior-art / novelty audit

The abstract graph identities are classical. Kron reduction is Schur complementation of graph Laplacians; the line's existing source anchor is Florian Dörfler and Francesco Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60:1 (2013), 150--163, DOI `10.1109/TCSI.2012.2215780`, arXiv `1102.2950`. Restricting a connected Laplacian to `1^perp`, using its Moore--Penrose inverse, and expressing spanning-tree/pseudodeterminant quantities through determinant identities are likewise standard spectral-graph linear algebra. No novelty is claimed for those ingredients.

The prime-circle-specific derived statement is the asymptotic combination of four facts forced by this line: the rank-`k-1` contrast factorization of PC-391, the `O(k)` trace bound of PC-392, the complete-survivor edge floor `w_min >= cH^{-2alpha}` from the intrinsic chord kernel, and the primorial deletion-density estimate `k/m=O(log p/p)`. Together they imply the uniform all-`lambda` bound (24), including the exact pseudodeterminant endpoint.

This is therefore a **classicalization/no-go result**, not a new graph determinant theorem, zeta criterion, or Hilbert--Pólya construction. It rules out one natural amplification strategy inside the specified positive complete chord-Laplacian model; it does not elevate the determinant formalism itself into arithmetic evidence.

## 7. Audit and falsification checks

The finite-dimensional core can be checked without asymptotics. For any positive complete survivor graph and any simultaneous deleted set, form `L_ind`, `L_red`, and `Delta_T`. Verify `Delta_T 1=0`, restrict both Laplacians to `1^perp`, and check (17) at positive `lambda` and (18) at `lambda=0`. The lower bound (13) can be independently checked by comparing the direct survivor Laplacian against the constant-weight complete graph with weight `w_min`.

The asymptotic conclusion can fail only if one of its geometry-specific hypotheses fails: the direct survivor graph is not complete/positive, the minimum edge weight becomes super-polynomially small in the fixed polynomial window, the contrast trace ceases to be `O(k)`, or the deletion rank fraction no longer obeys `O(log p/p)`. None occurs for the normalized positive inverse-power chord kernel and primorial window treated in PC-390--PC-392.

The conclusion is intentionally normalized. Equation (24) does **not** show that the unnormalized determinant or pseudodeterminant ratio tends to one; its logarithm may still grow like `O(k log p)`. Nor does it exclude individual outlier eigenvalues, cross-level transport/evolution of the `k-1` contrast subspace, or signed/indefinite/non-complete operators where the Loewner and edge-floor arguments are unavailable.

Nothing in this result supplies a zeta zero, functional-equation symmetry, critical-line selector, or new spectral operator for RH.

## Consequence for the research line

The singular determinant escape left by PC-392 is closed for the intrinsic positive complete inverse-power chord-Laplacian/Kron family. The multi-deletion contrast sector is not only a vanishing fraction of the survivor space; complete survivor connectivity prevents its generalized eigenvalues from becoming exponentially large enough to compensate for that sparsity in a normalized logarithmic determinant.

Accordingly, this branch should not spend further effort on choosing smaller nonnegative scalar regularizations or on the exact pseudodeterminant as a way to recover an extensive arithmetic carrier. Any remaining value of the contrast sector must instead be sought in **unnormalized exceptional data, individual outliers, cross-level dynamics, nonlinear observables, or operators whose sign/support structure genuinely leaves the positive complete-graph regime**. Those possibilities remain hypotheses to audit, not evidence of an RH mechanism.
