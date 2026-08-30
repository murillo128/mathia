# WI-043 — maximal pair discrepancy does not control the locked four-point covariance

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + NEEDS-AUDIT`. This finding does **not** refute the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes a stronger repair route left open by WI-037--WI-042: even granting the maximal-over-interval Matomäki--Radziwiłł--Tao pair-discrepancy control derived in WI-041, the exact Yang dispersion swap contains a genuinely **joint locked covariance** of two shifted-pair error processes. Uniformly tiny interval discrepancy for each marginal process, even when both arise from the same positive bounded base sequence, does not control that covariance. A concrete period-two model in the exact `b1=b2=1` strip geometry has `O(1)` maximal discrepancy for every relevant pair process but an `Omega(Y)` locked covariance.

Accordingly, a valid shift-first repair of the public Yang welding step must use information beyond the marginal MRT norm: an exact source-specific cancellation that removes the covariance, a joint/bilinear shifted-prime estimate, a suitable higher-uniformity/Fourier statement with the power-sized coefficients actually present, or another theorem that controls the coupled pair-error product. Merely reorganizing the public swap and then applying WI-041 separately to the two pair families cannot close the analytic bridge.

## 1. Exact locked product in the public dispersion swap

The pinned source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

For fixed `b1,b2`, the public `scripts/t2_swaps.py` defines

\[
A(b_2,j)
=\sum_m \Lambda(m)\Lambda(n),
\qquad
n=\frac{b_2m+j}{b_1},
\qquad
0<|j|\le J,
\tag{1}
\]

with the appropriate interval restrictions. Expanding the square and imposing equality of the two offsets gives

\[
b_1(n-n')=b_2(m-m').
\tag{2}
\]

Writing

\[
g=(b_1,b_2),
\qquad
r=b_1/g,
\qquad
q=b_2/g,
\tag{3}
\]

the code parameterizes (2) exactly by

\[
m'=m-rk,
\qquad
n'=n-qk.
\tag{4}
\]

Thus the `S1` term in the exact identity

\[
D=S_1-2S_2+S_3
\tag{5}
\]

contains, for each structured shift `k`, the locked four-prime sum

\[
S_{1,k}
=
\sum_n
\Lambda(n)\Lambda(n-qk)
\,w_k(n),
\tag{6}
\]

where the same public paper identifies the welding weight as

\[
\boxed{
 w_k(n)
 =\sum_{m\in I_k(n)}
 \Lambda(m)\Lambda(m-rk).
}
\tag{7}
\]

The interval `I_k(n)` is the moving intersection imposed by the original `m` window, the translated `m-rk` window, and the strip `0<|b_1n-b_2m|\le J`; WI-041 checked that it is a union of at most two intervals. Equations (6)--(7) are therefore not a generic weighted prime sum inserted by hand: they are the exact algebraic content of the public swap.

Primary source:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/t2_swaps.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex, subsection `Covered zone, middle band, bridge and aggregation`.

## 2. Exact centering exposes the missing covariance

For a nonzero shift `h`, abbreviate

\[
P_h(x):=\Lambda(x)\Lambda(x-h),
\qquad
\mu_h:=\mathfrak S(h),
\qquad
B_h(x):=P_h(x)-\mu_h.
\tag{8}
\]

Ignoring only the harmless smooth/window-length normalizations for the moment, (7) decomposes identically as

\[
w_k(n)
=
\mu_{rk}|I_k(n)|+E_{rk,k}(n),
\tag{9}
\]

where

\[
E_{rk,k}(n)
:=\sum_{m\in I_k(n)} B_{rk}(m).
\tag{10}
\]

Substitute

\[
P_{qk}(n)=\mu_{qk}+B_{qk}(n)
\tag{11}
\]

into (6). One obtains the exact four-term decomposition

\[
\begin{aligned}
S_{1,k}
={}&
\mu_{qk}\mu_{rk}\sum_n |I_k(n)| \\
&+\mu_{rk}\sum_n |I_k(n)|B_{qk}(n) \\
&+\mu_{qk}\sum_n E_{rk,k}(n) \\
&+\boxed{\sum_n B_{qk}(n)E_{rk,k}(n)}.
\end{aligned}
\tag{12}
\]

The first line is the factorized Hardy--Littlewood main. The next two lines are **marginal** discrepancy terms: with the slow geometry made explicit, maximal interval/prefix estimates of the WI-041 type are the natural input for them. The boxed term

\[
\boxed{
C_k:=\sum_n B_{qk}(n)
\sum_{m\in I_k(n)}B_{rk}(m)
}
\tag{13}
\]

is different. It is a covariance between two shifted-pair error processes coupled by the strip geometry. It is the exact point at which knowing every marginal interval discrepancy is not the same as knowing the locked four-point correlation.

This distinction is independent of the `S2` and `S3` bookkeeping. Those terms subtract the deterministic singular-series pieces from the cell square. They do not turn (13) into a marginal two-point error theorem; in the exact dispersion identity, (13) is precisely part of the off-diagonal fluctuation that the welding layer must control.

## 3. Maximal pair discrepancy is information-theoretically insufficient

WI-041 derives from MRT a maximal norm of the form

\[
M_Y(h)
:=
\sup_{I\subset[Y,2Y]}
\left|\sum_{x\in I} B_h(x)\right|,
\tag{14}
\]

with an averaged estimate

\[
\sum_h M_Y(h)^2
\ll_A HY^2(\log Y)^{-A}.
\tag{15}
\]

Even a dramatically stronger pointwise hypothesis

\[
M_Y(h)=O(1)
\tag{16}
\]

for both shifts in (13) does **not** imply `C_k=o(Y)`.

The obstruction can be realized by one positive bounded base sequence, so it is not an artifact of choosing two unrelated adversarial error arrays.

Fix `0<eta<1` and put

\[
a_x=1+\eta(-1)^x>0.
\tag{17}
\]

For every even shift `h`, the pair product is

\[
a_xa_{x-h}
=(1+\eta(-1)^x)^2
=1+\eta^2+2\eta(-1)^x.
\tag{18}
\]

Center at its exact parity mean

\[
\mu_h^{\rm toy}=1+\eta^2,
\qquad
B_h^{\rm toy}(x)=2\eta(-1)^x.
\tag{19}
\]

For **every** integer interval `I`,

\[
\boxed{
\left|\sum_{x\in I}B_h^{\rm toy}(x)\right|
\le2\eta.
}
\tag{20}
\]

Thus this toy process satisfies a maximal interval-discrepancy bound much stronger than the logarithmically saving statement available from MRT.

## 4. The obstruction occurs in the exact `b1=b2=1` Yang strip

Now specialize the swap geometry to

\[
b_1=b_2=1,
\qquad r=q=1,
\tag{21}
\]

and take an **even** structured shift `k`. Away from the outer interval boundaries, the public condition `0<|b_1n-b_2m|\le J` becomes exactly

\[
I_J(n)=\{m:1\le|m-n|\le J\}.
\tag{22}
\]

Choose `J` odd. From (19),

\[
\begin{aligned}
E_h^{\rm toy}(n)
&:=\sum_{m\in I_J(n)}B_h^{\rm toy}(m)\\
&=2\eta\sum_{s=1}^{J}
\left((-1)^{n-s}+(-1)^{n+s}\right)\\
&=4\eta(-1)^n\sum_{s=1}^{J}(-1)^s\\
&=-4\eta(-1)^n.
\end{aligned}
\tag{23}
\]

Therefore the locked covariance is

\[
\begin{aligned}
C_k^{\rm toy}
&=\sum_n B_k^{\rm toy}(n)E_k^{\rm toy}(n)\\
&=-8\eta^2\,Y+O_{J,\eta}(1)
\end{aligned}
\tag{24}
\]

on an interior block of length `Y`. In particular,

\[
\boxed{
M_Y(k)\le2\eta
\quad\text{while}\quad
|C_k^{\rm toy}|\asymp Y.
}
\tag{25}
\]

The diagonal deletion `j=0` is important here rather than an inconvenience: (22) is exactly the off-diagonal strip used by the public code. For odd `J`, the symmetric neighbors retain the parity mode instead of averaging it away. Boundary truncations affect only `O(J)` sites and hence only the `O_{J,eta}(1)` term when `J` is fixed relative to this finite information test.

Equation (25) proves the needed no-go. There is no abstract inequality that turns marginal maximal interval discrepancy for the two pair processes into a sublinear bound for the locked covariance (13).

## 5. Why this is stronger than the earlier welding barriers

The previous findings close progressively weaker shortcuts.

- **WI-037:** pointwise divisor-boundedness of the welding coefficient cannot preserve minor-arc cancellation.
- **WI-041:** the moving interval itself is not fatal; MRT can be maximalized over interval endpoints, but sparse progressions may lose `sqrt(r)` if treated separately.
- **WI-042:** the public `g1_ledger.py` takes an across-family Cauchy--Schwarz, exactly the route the paper says is over budget; the desired shift-only consumer is not written out publicly.

The present result asks the most favorable question left after those findings: suppose the missing shift-first regrouping is supplied and suppose the moving windows are controlled by the full maximal MRT norm of WI-041. Is that marginal information now enough?

The answer is still **no**. The exact expansion (12) leaves the joint term (13), and the same-base-sequence model (17)--(25) shows that this term can be macroscopic while all marginal interval deviations are uniformly bounded.

Hence the remaining proof obligation is not merely to move Cauchy--Schwarz to the correct index. It must explain why the actual von Mangoldt pair-error processes do not exhibit a coherent locked mode of the type exposed by (25).

## 6. What kind of new input would close the covariance

A valid repair may still exist, but it must furnish genuinely joint information. Sufficient mechanisms include, for example:

1. **Exact cancellation before estimation.** A source-specific algebraic identity involving the full `S1-2S2+S3` combination that cancels (13) after the actual kernel/block weights are restored.
2. **A bilinear shifted-prime theorem.** A bound directly for the locked covariance (13), averaged over the structured `(r,q,k)` family with the Yang normalization.
3. **Fourier/higher-uniformity decorrelation.** A theorem excluding common coherent modes of the two centered pair processes at the power-sized reduced coefficients that occur in the middle band. WI-039--WI-040 already show why fixed-coefficient transference cannot simply be quoted here.
4. **A source-specific spectral projection.** If the exact strip/kernel weights annihilate the dangerous common modes, that annihilation must be proved quantitatively and uniformly rather than inferred from marginal MRT cancellation.

What is now ruled out is the chain

\[
\boxed{
\text{exact swap}
+\text{maximal marginal MRT for each pair family}
\Longrightarrow
\text{locked four-point factorization}
}
\tag{26}
\]

without an additional joint ingredient.

## 7. Prior-art and novelty audit

The primary literature input remains Matomäki--Radziwiłł--Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. LMS 118 (2019), 284--350, arXiv:1707.01315. Their Theorem 1.3(i) controls individual shifted-prime correlations for almost all shifts; WI-041 derives the maximal-interval `L^2` variant. It does not state a theorem for the locked covariance (13).

The general principle behind the counterexample is classical: cancellation of each of two sequences against intervals or low-complexity test functions does not by itself bound their mutual correlation. Alternating sequences are the elementary model, while more sophisticated versions are expressed through Fourier or Gowers-uniformity norms and generalized von Neumann inequalities. No novelty is claimed for that principle, the parity construction, Cauchy--Schwarz, or the decomposition of a product around its means.

The Mathia contribution recorded here is specific to the Yang proof interface:

- derive the exact centered decomposition (12) from the public `S1` swap and the printed welding weight;
- identify the boxed covariance (13) as the piece not covered by the marginal maximal MRT theorem;
- realize a macroscopic obstruction using a **single positive bounded base sequence** in the exact `b1=b2=1`, `j!=0` strip geometry of the public code;
- thereby sharpen the analytic repair target from “write the shift-only consumer” to “supply a joint theorem or exact cancellation for the locked pair-error covariance.”

No claim of priority is made for this organization or for the toy model. A bounded prior-art audit found no published theorem in the cited Yang/MRT chain that supplies the missing joint covariance estimate.

## 8. Decisive verification / falsification gate

Narrow or retire this finding if the public Yang chain supplies one of the following.

1. An exact weighted `S1-2S2+S3` identity in which (13) cancels before any estimate, including all kernel, block, boundary, and singular-series terms.
2. A stated primary theorem controlling (13), or its exact weighted analogue, in the full `8/33` middle-band parameter range with the power-sized reduced coefficients present in the source.
3. A proof that the Yang strip/kernel annihilates every common coherent mode allowed by marginal MRT, strong enough to invalidate the same-geometry test (17)--(25) once the actual admissible weights are imposed.

The elementary model is **not** a model of the primes and therefore cannot falsify such a source-specific theorem. Its role is logical: it proves that no conclusion about (13) can be obtained from the marginal maximal-discrepancy information alone.

## 9. Consequence for `weil_inertia`

The one-sided fourth-moment route remains a high-value candidate because WI-028 shows that only a coarse remainder bound is needed to beat Mathia's current unconditional theorem, and WI-030--WI-035 have already converted many deterministic and major-arc pieces into exact or literature-backed statements. The remaining uncertainty is now more sharply localized:

\[
\boxed{
\text{MRT marginal pair control}
\;\not\supset\;
\text{locked four-point covariance control}.
}
\tag{27}
\]

Accordingly, further work should not spend cycles improving endpoint maximalization, generic divisor envelopes, or the existing global-cell Cauchy ledger. The shortest evidence-changing target is the actual **joint** arithmetic object (13): either derive a Yang-specific cancellation/joint estimate for it, or show that controlling it requires a four-point input beyond the published MRT theorem. The latter would turn the present information barrier into a theorem-level obstruction to the advertised one-sided route rather than merely to its current public write-out.