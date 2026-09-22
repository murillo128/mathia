# FD-265 — Full-grid one-sided escape requires negative triangle saturation

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** canonical full-grid repair / one-sided slack / divisor-smoothed Mertens blocks / exact positive-part decomposition / triangle-saturation escape / physical cushion criterion
- **Depends on:** FD-234, FD-260, FD-261, FD-263, FD-264
- **Classification:** `EXACT-DERIVED + ONE-SIDED-DECOMPOSITION + DIVISOR-CONVOLUTION + POSITIVE-PART-IDENTITY + TRIANGLE-SATURATION-RIGIDITY + PHYSICAL-LIFT-CERTIFICATE + ROUTE-SHARPENING`

## Claim

FD-263 identifies the absolute block-replication ledger for the canonical full-grid repair, while FD-264 shows that its signed band drift collapses to a positive Mertens scale average. The remaining source-side question is genuinely one-sided: how much **negative** repair mass must a positive cushion cover? For the canonical repair this quantity has an exact arithmetic form.

Put

\[
U_N(q):=M(qN)-M((q-1)N),
\qquad
G_N(d):=(\mathbf 1*U_N)(d)=\sum_{q\mid d}U_N(q).
\tag{1}
\]

By FD-234 the canonical real full-grid correction is

\[
\widetilde c_N(d)=-\frac12G_N(d).
\tag{2}
\]

For the complete coefficient band

\[
I_x:=\{d:x<d\le2x\},
\]

define

\[
L_N(x):=\sum_{d\in I_x}|G_N(d)|,
\qquad
S_N(x):=\sum_{d\in I_x}G_N(d).
\tag{3}
\]

Then its exact negative repair demand is

\[
\boxed{
\widetilde R_N^-(x)
:=\sum_{d\in I_x}(-\widetilde c_N(d))_+
=
\frac14\bigl(L_N(x)+S_N(x)\bigr)
=
\frac12\sum_{d\in I_x}(G_N(d))_+.
}
\tag{4}
\]

The signed term in (4) is already the FD-264 probability average. With `\mathcal P_x` defined there,

\[
\boxed{
S_N(x)=x\,\mathcal P_x[M(N\,\cdot)].
}
\tag{5}
\]

Hence

\[
\boxed{
\widetilde R_N^-(x)
=
\frac14
\left(
L_N(x)+x\mathcal P_x[M(N\,\cdot)]
\right).
}
\tag{6}
\]

Let `c_N` be the nearest-integer repair of FD-225. FD-234 gives `c_N=\widetilde c_N+r_N` with `|r_N(d)|\le\tau(d)`. Since the negative-part map is 1-Lipschitz and `\sum_{x<d\le2x}\tau(d)\ll x\log x`, uniformly in `N`,

\[
\boxed{
R_N^-(x)
:=\sum_{d\in I_x}(-c_N(d))_+
=
\frac14
\left(
L_N(x)+x\mathcal P_x[M(N\,\cdot)]
\right)
+O(x\log x).
}
\tag{7}
\]

This turns the current one-sided source problem into an exact sign-bias question for the divisor-smoothed Mertens block field `G_N`. In particular, whenever `L_N(x)\gg x\log x`,

\[
\boxed{
R_N^-(x)=o(L_N(x))
\iff
\frac{S_N(x)}{L_N(x)}\longrightarrow-1.
}
\tag{8}
\]

Thus a large `l^1` field can evade positive-slack demand only by asymptotically saturating the triangle inequality in the **negative** direction: almost all of the `G_N` mass must lie in its negative part. Equivalently, for every fixed `\eta>0`, the triangle gap

\[
S_N(x)\ge-(1-\eta)L_N(x)
\tag{9}
\]

forces

\[
\boxed{
R_N^-(x)
\ge
\frac\eta4L_N(x)-O(x\log x).
}
\tag{10}
\]

This is the missing bridge between the FD-263 absolute population mechanism and the FD-260 positive-cushion ceiling. It separates two independent requirements for a source-side obstruction: block population must first survive divisor convolution strongly enough to make `L_N(x)` large, and the resulting field must then avoid near-total negative sign polarization.

For the physical FD-226 scale-adapted reservoir architecture, write

\[
\Lambda_N:=\frac{N}{D\log N}
\]

for its natural occupancy scale, take `x\asymp D`, and let `p_N(d)>=0` be any physical cushion whose normalized profile satisfies the FD-260 hypotheses. FD-261 gives

\[
\sum_{d\in I_x}p_N(d)
\ll
\Lambda_Nx^{2-\beta},
\qquad
\beta=\log_2\frac32.
\tag{11}
\]

If `p_N` pointwise lifts the canonical rounded repair, then `p_N(d)\ge(-c_N(d))_+`, so (7) yields the necessary arithmetic condition

\[
\boxed{
\sum_{d\in I_x}(G_N(d))_+
\ll
\Lambda_Nx^{2-\beta}+x\log x.
}
\tag{12}
\]

Equivalently,

\[
\boxed{
L_N(x)+x\mathcal P_x[M(N\,\cdot)]
\ll
\Lambda_Nx^{2-\beta}+x\log x.
}
\tag{13}
\]

Therefore a lower bound on the **positive divisor-smoothed block mass**, not merely on raw block amplitudes, their population, the total variation `L_N`, or the signed band drift, is the exact arithmetic certificate that can contradict the current general nonnegative cushion theorem.

## 1. The negative part is exactly the positive part of the divisor-smoothed block field

Equation (2) is the exact real inversion already isolated in FD-234. Coordinatewise,

\[
(-\widetilde c_N(d))_+
=
\frac12(G_N(d))_+.
\tag{14}
\]

For every real number `z`,

\[
z_+=\frac{|z|+z}{2}.
\]

Summing (14) over `I_x` therefore gives

\[
\begin{aligned}
\widetilde R_N^-(x)
&=\frac12\sum_{d\in I_x}(G_N(d))_+\\
&=\frac14\sum_{d\in I_x}\bigl(|G_N(d)|+G_N(d)\bigr)\\
&=\frac14\bigl(L_N(x)+S_N(x)\bigr),
\end{aligned}
\]

which proves (4).

This identity is elementary, but it changes the live object. FD-263 bounds `\sum|\widetilde c_N(d)|=L_N(x)/2` by a block-replication norm. FD-264 controls `\sum\widetilde c_N(d)=-S_N(x)/2` by a positive scale average. The physical cushion does not see either statistic separately: its minimum pointwise load is their precise one-sided combination (4).

There is a symmetric identity for the positive part of the repair,

\[
\sum_{d\in I_x}(\widetilde c_N(d))_+
=
\frac14\bigl(L_N(x)-S_N(x)\bigr).
\tag{15}
\]

Thus `S_N/L_N` is exactly the sign-polarization coordinate of the full-grid correction. No probabilistic or average-sign assumption is needed.

## 2. FD-264 identifies the sign bias with a positive Mertens scale average

For the real repair, the full-grid residual is identically zero:

\[
M(mN)+2(\mathscr A\widetilde c_N)(m)=0.
\]

Set `R_N=0` in FD-264's exact signed-band identity. It gives

\[
\sum_{d\in I_x}\widetilde c_N(d)
=-\frac{x}{2}\mathcal P_x[M(N\,\cdot)].
\tag{16}
\]

On the other hand, (2) gives

\[
\sum_{d\in I_x}\widetilde c_N(d)
=-\frac12S_N(x).
\tag{17}
\]

Comparing (16) and (17) proves (5), and substitution into (4) proves (6).

The averaging operator is positive and normalized. If

\[
\pi_x(q)=\frac{w_x(q)}x,
\qquad
w_x(q)=m_x(q)-m_x(q+1),
\]

then `\pi_x(q)>=0` and `\sum_q\pi_x(q)=1`. Hence

\[
|S_N(x)|
=x\left|\mathcal P_x[M(N\,\cdot)]\right|
\le L_N(x),
\tag{18}
\]

where the last inequality is also just the triangle inequality for `S_N`. The one-sided escape in (8) is therefore an **extremal** regime: the signed sum must come within `o(L_N)` of the most negative value allowed by triangle inequality.

This is substantially more specific than saying that within-band cancellation might defeat an `l^1` lower bound. If `L_N` is large but the repair needs little positive slack, the divisor-smoothed field cannot merely oscillate; it must become almost entirely nonpositive in `l^1` mass.

## 3. Rounding changes the one-sided objective only by `O(x log x)`

FD-234 writes the integer repair as

\[
c_N=\widetilde c_N+r_N,
\qquad
|r_N(d)|\le\tau(d).
\tag{19}
\]

Since `z\mapsto z^-` is 1-Lipschitz,

\[
\left|
(-c_N(d))_+-(-\widetilde c_N(d))_+
\right|
\le|r_N(d)|.
\tag{20}
\]

Summing over `I_x` and using the elementary divisor-sum estimate

\[
\sum_{x<d\le2x}\tau(d)\ll x\log x
\tag{21}
\]

proves (7).

Now assume `L_N(x)/(x\log x)\to\infty` along a family. Dividing (7) by `L_N(x)` gives

\[
\frac{R_N^-(x)}{L_N(x)}
=
\frac14\left(1+\frac{S_N(x)}{L_N(x)}\right)+o(1).
\tag{22}
\]

Because `-1<=S_N/L_N<=1`, equation (8) follows immediately. Likewise (9) inserted into (7) proves (10).

So nearest-integer parity cannot provide the remaining escape. At any scale where the divisor-smoothed block variation dominates the elementary rounding budget, vanishing relative negative demand is equivalent to negative triangle saturation of the real arithmetic field itself.

## 4. Relation to the FD-263 replication ledger

The absolute field `L_N` is itself controlled by the exact replication kernel. From (1), triangle inequality and exchange of the divisor/multiple sums give

\[
\boxed{
L_N(x)
\le
\sum_{q\le2x}|U_N(q)|m_x(q),
}
\tag{23}
\]

which is exactly twice the real-repair version of the FD-263 `l^1` upper ledger.

Equation (23) need not be close to equality: different divisor blocks can cancel inside a given `G_N(d)`. Therefore the amplitude-density condition isolated by FD-263 is only the first of two source hurdles. A successful lower-bound route must establish enough **post-convolution variation** `L_N`, not merely enough raw weighted variation on the right side of (23).

Even that is not sufficient by itself. Equation (4) says that a large `L_N` translates to large negative slack only if the sign bias stays away from `-1`. The precise two-stage source problem is therefore:

1. prove that enough Mertens block variation survives the divisor convolution `U_N -> G_N`;
2. prove that the surviving field does not asymptotically align with the nonpositive cone on the deep coefficient band.

This is strictly sharper than searching for a dense family of large `|U_N(q)|`. Such a family may disappear through divisor-sum cancellation, or it may produce a large `G_N` that is almost entirely negative and therefore costs almost no negative repair mass.

Conversely, any uniform triangle gap as in (9) converts an `l^1` lower bound for `G_N` into a one-sided lower bound with no further loss in the depth exponent. Thus the sign problem and the amplitude-density problem are now cleanly separated.

## 5. Physical cushion consequence and phase calibration

Let `p_N` be a nonnegative cushion lifting the rounded canonical repair pointwise,

\[
c_N(d)+p_N(d)\ge0.
\]

Then

\[
p_N(d)\ge(-c_N(d))_+
\]

and hence

\[
R_N^-(x)\le\sum_{d\in I_x}p_N(d).
\tag{24}
\]

Under the FD-260 hypotheses in the FD-226 physical normalization, equation (11) applies. Combining (24) with (7) gives (12)--(13), with harmless absolute constants.

This provides a direct falsification target for physical liftability. If on some unbounded family one proves

\[
\sum_{d\in I_x}(G_N(d))_+
\ge
N^{\theta-o(1)}D^{\alpha-o(1)},
\qquad x\asymp D,
\tag{25}
\]

then FD-261's phase comparison applies to this **actual minimum slack demand**. At the same arithmetic amplitude scale as the first switched row, the general FD-260 depletion becomes decisive at or before the first-row boundary only if

\[
\boxed{
\alpha>2-\beta
=1.4150374992\ldots .
}
\tag{26}
\]

Nothing in the present finding proves (25). Its contribution is to identify exactly what must satisfy such a lower bound. A theorem only about signed band drift cannot do it by FD-264. A theorem only about raw block population does not do it by (23). A theorem about `L_N` does it once one additionally rules out negative triangle saturation.

The alternative FD-259 route remains qualitatively different. If the physical positive cushion were known to have nonnegative Möbius increments, its capacity ceiling is inverse-linear and a merely linear-depth source demand is already exponent-critical. FD-265 neither proves nor assumes that extra cone condition.

## 6. Finite audit

The identities were checked independently at the same finite point used in FD-263--FD-264: `N=100`, `x=16`. Computing the Möbius function and Mertens prefixes directly through `3200` gives

\[
L_{100}(16)=117,
\qquad
S_{100}(16)=-3.
\]

Therefore the exact real repair has

\[
\widetilde R_{100}^-(16)
=\frac{117-3}{4}
=28.5,
\tag{27}
\]

and positive repair mass `30`. The FD-264 scale-average audit gives exactly

\[
\sum_qw_{16}(q)M(100q)=-3,
\]

matching (5).

For the nearest-integer target with ties rounded to even, direct inversion gives

\[
R_{100}^-(16)=26,
\qquad
\sum_{16<d\le32}|c_d|=57,
\qquad
\sum_{16<d\le32}c_d=5.
\]

The one-sided rounding shift is therefore `2.5`, well inside the uniform divisor-sum allowance in (7). The finite computation is only an endpoint and sign-convention audit; none of the proof depends on the numerical example.

## 7. Prior-art boundary and consequence

A targeted literature search around positive parts of divisor/Dirichlet convolutions, short-interval Möbius block sums, Mertens block increments, and `l^1` divisor-sum transforms found the standard Dirichlet-convolution framework and neighboring short-interval Möbius literature, but no result matching the repository-specific identity (6), its triangle-saturation equivalence (8), or the physical FD-260 consequence (12). No external theorem is load-bearing here: the proof uses the exact local identities already established in FD-234 and FD-264 plus the elementary positive/negative-part formula and divisor-sum bound. `SOURCES.md` therefore needs no update.

The result is an exact reduction, not the missing arithmetic lower bound. It does not prove that `L_N` is large, does not prove a uniform triangle gap, and does not improve a Mertens estimate. It also applies specifically to the canonical full-grid repair modulo the capacity-negligible nearest-integer perturbation of FD-234; switched-only repairs with materially different full-grid residuals remain a separate route.

The main consequence is that the source-side problem is now sharper than “prove large within-band variation.” The relevant arithmetic field is explicitly

\[
G_N=\mathbf1*\bigl(M(N\,\cdot)-M(N(\,\cdot-1))\bigr),
\]

and its positive part is, up to the factor `1/2` and the negligible rounding budget, the literal minimum positive slack required by the canonical repair. Large variation fails to create an obstruction only in the extremal regime where `G_N` nearly saturates the negative triangle inequality.

**Verdict.** The canonical full-grid positivity bottleneck has an exact one-sided arithmetic objective. After divisor smoothing of the consecutive Mertens blocks, the required negative repair mass is one half of the positive `l^1` mass of that field, and its imbalance is exactly the positive Mertens scale average from FD-264. Therefore the surviving amplitude-density route has two precise obligations: retain enough variation through divisor convolution and prevent near-complete negative sign polarization. Any future source theorem that establishes both, at depth exponent above the FD-261 threshold, yields a genuine physical cushion obstruction; neither raw block population nor signed band drift alone can do so.