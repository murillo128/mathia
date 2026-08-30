# WI-044 — isolated locked covariance can cancel under exact cell centering

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CORRECTION + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** invalidate the narrow information-theoretic statement of WI-043: marginal interval control of two shifted-pair error processes does not bound their isolated locked covariance. It does narrow the consequence that should be drawn from that statement. A large isolated covariance need not survive in the full Yang dispersion quantity

\[
D=S_1-2S_2+S_3=\sum_j(A_j-MT_j)^2.
\]

An exact same-base model in the public lock geometry has uniformly bounded marginal pair discrepancy and an `Omega(L^2)` sum of locked-covariance pieces, while the fully centered cell dispersion is **exactly zero**. The missing covariance is canceled by the other centered terms because the deterministic cell main captures the shared local mode.

Accordingly, the next evidence-changing obligation in the Yang--Yang one-sided fourth-moment audit is not to prove an absolute bound for the covariance `C_k` isolated in WI-043. It is to reconstruct the **fully centered shift-first identity**, with the exact local singular-series main retained through `S1-2S2+S3`, and determine whether any genuinely joint residual remains after that cancellation. Only such a residual would require a new bilinear/four-point theorem.

## 1. Source interface being corrected

The pinned public source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

For fixed `b1,b2,j`, the source defines the cell mass

\[
A_{b_2,j}
=\sum_m\Lambda(m)\Lambda(n),
\qquad
b_1n-b_2m=j,
\tag{1}
\]

and its deterministic Montgomery--Hardy--Littlewood cell main `MT`. The exact dispersion is

\[
D=\sum_{b_2,j}(A_{b_2,j}-MT_{b_2,j})^2
=S_1-2S_2+S_3.
\tag{2}
\]

The public `scripts/t2_swaps.py` expands `S1` by imposing the same lock on two copies. With

\[
g=(b_1,b_2),\qquad r=b_1/g,\qquad q=b_2/g,
\tag{3}
\]

one has exactly

\[
m'=m-rk,\qquad n'=n-qk.
\tag{4}
\]

WI-043 then centered each shifted pair separately and isolated a term of the form

\[
C_k
=\sum_n B_{qk}(n)
\sum_{m\in I_k(n)}B_{rk}(m).
\tag{5}
\]

Its same-base alternating model proves correctly that marginal maximal discrepancy does not control (5). What remained untested was whether (5), **after this particular pairwise centering**, is itself a residual that the full cell dispersion must estimate absolutely.

The source explicitly claims that its welding layer uses an "exact factorization of main terms" before the remaining major/minor-arc estimates. That claim is not publicly written out at theorem level and remains an audit gate under WI-037/WI-042. The point here is narrower: one cannot rule such a cancellation out merely because (5) is large.

Primary source:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/t2_swaps.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex, subsection `Covered zone, middle band, bridge and aggregation`.

## 2. Exact local-mode model

Fix `0<eta<1` and define one positive bounded base sequence

\[
a_x=1+\eta(-1)^x.
\tag{6}
\]

For any integer shift `h`, its pair product is

\[
P_h(x):=a_xa_{x-h}.
\tag{7}
\]

Its exact parity mean is

\[
\mu_h:=1+\eta^2(-1)^h.
\tag{8}
\]

Hence the centered pair error

\[
B_h(x):=P_h(x)-\mu_h
\tag{9}
\]

is

\[
\boxed{
B_h(x)=
\begin{cases}
2\eta(-1)^x,&h\ \text{even},\\
0,&h\ \text{odd}.
\end{cases}}
\tag{10}
\]

In particular every ordinary interval has uniformly bounded marginal discrepancy:

\[
\boxed{
\sup_I\left|\sum_{x\in I}B_h(x)\right|\le2\eta
}
\tag{11}
\]

for every `h`. Thus this is at least as strong a marginal cancellation model as the one used in WI-043.

## 3. A fixed lock is centered perfectly

Now take the simplest exact public lock geometry `b1=b2=1`, so

\[
n=m+j.
\tag{12}
\]

Let the admissible `m`-window be any interval `W` of even cardinality `L`. Define the cell mass

\[
A_j:=\sum_{m\in W}a_ma_{m+j}.
\tag{13}
\]

If `j` is even then

\[
a_ma_{m+j}=a_m^2
=1+\eta^2+2\eta(-1)^m,
\]

whose alternating term sums to zero on an even interval. If `j` is odd then

\[
a_ma_{m+j}=1-\eta^2
\]

pointwise. Therefore in both cases

\[
\boxed{
A_j=L\bigl(1+\eta^2(-1)^j\bigr)=L\mu_j.
}
\tag{14}
\]

Choose the deterministic cell main to be exactly this local mean,

\[
MT_j:=L\mu_j.
\tag{15}
\]

Then the complete centered cell dispersion vanishes:

\[
\boxed{(A_j-MT_j)^2=0.}
\tag{16}
\]

This is the finite analogue of what a correct singular-series main is designed to do: absorb deterministic congruence modes before the analytic error is estimated.

## 4. The WI-043 covariance is nevertheless macroscopic

Expand `A_j^2` by the difference

\[
k=m-m'.
\tag{17}
\]

For `|k|<L`, the overlap `W\cap(W+k)` contains `L-|k|` terms. In the `b1=b2=1` lock, both shifted pairs have the same shift `k`, so the isolated pair-centered covariance is

\[
C_{j,k}
:=\sum_{m\in W\cap(W+k)}
B_k(m)B_k(m+j).
\tag{18}
\]

By (10), `C_{j,k}=0` for odd `k`. For even `k`,

\[
B_k(m)B_k(m+j)
=4\eta^2(-1)^{m+m+j}
=4\eta^2(-1)^j,
\]

and hence

\[
\boxed{
C_{j,k}
=4\eta^2(-1)^j(L-|k|)
\qquad(k\ \text{even}).
}
\tag{19}
\]

For even `j` every nonzero term in (19) is positive. If `L=2M`, summing over all even `k` with `|k|<L` gives

\[
\sum_{k\ \mathrm{even}}(L-|k|)=\frac{L^2}{2},
\]

so

\[
\boxed{
\sum_{k\ \mathrm{even}} C_{j,k}
=2\eta^2L^2.
}
\tag{20}
\]

Thus the isolated locked covariance is quadratic in the cell length even though every marginal discrepancy is `O(1)` and the **fully centered cell error is exactly zero** by (16).

There is no contradiction. Equations (16) and (20) force the remaining terms generated by the pairwise centering of the exact `S1-2S2+S3` identity to cancel the large covariance exactly. In this model, taking an absolute value of (18) before those terms are recombined destroys the cancellation that makes the original dispersion small.

## 5. The phenomenon is a local-factor issue, not a special numerical accident

The mode `(-1)^x=e(x/2)` is the simplest local congruence mode. In prime correlations, parity and the other `p`-adic restrictions are precisely what the Hardy--Littlewood singular series records. The Yang cell main is not a product of two unconditioned scalar means inserted after the swap; it is indexed by the original lock `j` through `S_{b1,b2}(j)`, and `S3` contains the corresponding second local moment `E2(b1,b2)`.

This does **not** prove that the Yang main-factorization sentence is correct. It proves that a proof audit must preserve that local conditioning long enough to decide the question. Centering the two shifted pairs separately by `S(rk)` and `S(qk)`, then demanding that the resulting covariance be small in absolute value, can manufacture a false proof obligation by moving a deterministic joint local factor into the "error".

The same warning persists for general odd reduced coefficients. If `b1,b2` are odd, then `r,q` in (3) are odd. On an even structured shift `k`, both pair shifts remain even, and the lock fixes the relative parity of `m` and `n`. Thus the common frequency `1/2` remains phase-locked through the exact Diophantine cell. This is precisely the kind of mode that must be allocated to the joint local main before one asks for analytic decorrelation.

## 6. Consequence for WI-041--WI-043

Three earlier conclusions remain valid but their roles are now sharper.

- **WI-041:** maximal interval `L^2` derived from MRT handles moving endpoints, but its possible progression-wise strengthening is still only marginal information.
- **WI-042:** the public `g1_ledger.py` uses the forbidden global family Cauchy and therefore does not supply the printed shift-only proof.
- **WI-043:** marginal maximal discrepancy does not control the isolated covariance (5). Equation (20) confirms that statement in an even stronger way.

What must be narrowed is the inference from WI-043 to the full theorem. The implication

\[
\boxed{
|C_k|\ \text{large}
\Longrightarrow
\text{full Yang welding remainder large}
}
\tag{21}
\]

is false without first proving that the local-main and cross terms cannot cancel it. The model (6)--(20) gives an exact counterexample to (21).

Therefore a new four-point or higher-uniformity theorem is **not yet logically forced** by WI-043. It becomes necessary only if the full source-specific centering leaves a genuinely joint residual after all deterministic local factors have been removed.

## 7. Revised shortest proof obligation

The efficient audit target is now the exact combination, not an isolated summand:

\[
\boxed{
S_1-2S_2+S_3
\longrightarrow
\text{joint local main}
+\text{fully centered shift residual}.
}
\tag{22}
\]

A valid repair of the Yang one-sided route should provide all of the following in one chain.

1. Write the `S1` shift-first expansion with the actual cell/kernel/block weights.
2. Insert the same local factors used by `MT_{b2,j}` and `E2(b1,b2)`, rather than centering the two pair processes independently by scalar twin means.
3. Combine `S1-2S2+S3` **before** any absolute value or Cauchy--Schwarz that could destroy local-factor cancellation.
4. Identify the residual after this exact recombination.
5. Only then match that residual to MRT, a weighted/anisotropic refinement, a genuinely joint prime theorem, or an exact zero identity.

If the recombination cancels the analogue of (5), WI-043 remains only an information-theoretic warning about a bad decomposition. If a non-canceling joint term survives with the Yang normalization, that residual -- not (5) in isolation -- is the correct theorem obligation.

## 8. Prior-art and novelty audit

No novelty is claimed for parity, periodic sequences, autocorrelation identities, centering, or the principle that Hardy--Littlewood singular series encode local congruence obstructions. Likewise no novelty is claimed for the exact algebra `D=S1-2S2+S3` or for the Yang local-density factors.

The literature-backed arithmetic boundary remains Matomäki--Radziwiłł--Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges* (Proc. LMS 118 (2019), 284--350, arXiv:1707.01315): it supplies marginal shifted-prime information, not the unpublished Yang welding factorization. The newer higher-uniformity results audited in WI-039 remain relevant only if a genuinely joint residual survives the exact centering.

The durable exact deduction recorded here is specific to the current Mathia audit: the same positive bounded model used to motivate the WI-043 covariance obstruction can be centered at the **cell level** so that the original dispersion is exactly zero while the isolated covariance has size `Theta(L^2)`. Hence the covariance-alone obstruction is not invariant under the algebraically natural choice of main term and cannot be promoted to a theorem-level barrier for the full Yang route without the recombination test (22).

A bounded prior-art check found the classical local-factor/singular-series interpretation and modern Gowers formulations of joint prime-pattern uniformity, but no need for a new external theorem is established by this finding. Absence of a matching formulation is not a priority claim.

## 9. Decisive verification / falsification gate

Reject or narrow this finding if any of the following fails.

1. Verify (14) directly for both parities of `j` and even `L`.
2. Verify the pair-error formula (10) and the overlap count leading to (19)--(20).
3. Expand the finite identity `(A_j-MT_j)^2` and confirm that its zero value forces exact cancellation of the large covariance contribution when all pairwise-centering terms are retained.
4. Reconstruct the Yang cell main and check that its local factors are indeed introduced before the claimed welding estimate; this finding does not assume that their subsequent factorization is valid.
5. Do not infer from the toy model that the actual prime residual cancels. The conclusion is only that **isolated `C_k` is not a logically sufficient obstruction**.
6. Promote a joint four-point theorem to a necessary input only after an exact source-level recombination shows a non-canceling joint residual with the actual weights and normalization.

## 10. Consequence for `weil_inertia`

The one-sided fourth-moment candidate remains unproved for the reasons already isolated in WI-037 and WI-042. WI-043 still closes the shortcut "marginal maximal MRT controls every centered product term separately." What changes is the research priority: before spending effort on a new four-prime theorem, first test whether the public claim of **exact main-term factorization** removes the locked covariance once `S1`, `S2`, and `S3` are centered coherently at the cell level.

This is a cheaper and more decisive fork. Exact cancellation would materially reopen the Yang route using mostly existing two-point technology; failure of cancellation would expose the true residual joint object and justify the stronger arithmetic machinery that WI-043 had only conditionally motivated.
