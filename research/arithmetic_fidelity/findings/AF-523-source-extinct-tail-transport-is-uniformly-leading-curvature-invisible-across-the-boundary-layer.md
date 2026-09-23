# AF-523 — Source-extinct tail transport is uniformly leading-curvature invisible across the boundary layer

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `SOURCE-EXTINCTION` · `MULTI-SCALE` · `OUTWARD-TRANSPORT` · `MATCHED-COMPOSITE-CONTROL` · `MESOSCOPIC-CURVATURE` · `NEGATIVE/OBSTRUCTION` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=(\log P(s))'',
\qquad s>1.
\]

For an integer cutoff `A\to\infty`, write

\[
L_A=\log A,
\qquad
H_A=\log L_A.
\]

Choose integers `C_A\ge2` satisfying

\[
C_A\longrightarrow\infty,
\qquad
\frac{C_AH_A}{L_A}\longrightarrow0.
\tag{1}
\]

Retain every prime `p\le A` and move every prime `p>A` to the ordinary composite atom `C_Ap`. Thus

\[
Q_A(s)
=
\sum_{p\le A}p^{-s}
+
C_A^{-s}\sum_{p>A}p^{-s}.
\tag{2}
\]

Every moved atom is distinct, composite, strictly larger than its source prime, and has coefficient one.

Then throughout the entire moving boundary layer

\[
0<t\le \frac1A,
\qquad s=1+t,
\tag{3}
\]

the transformed source becomes uniformly negligible in Dirichlet value while its leading logarithmic-curvature profile becomes uniformly indistinguishable from the prime source:

\[
\boxed{
\sup_{0<t\le1/A}
\frac{Q_A(1+t)}{P(1+t)}
\longrightarrow0,
}
\tag{4}
\]

but

\[
\boxed{
\sup_{0<t\le1/A}
\left|
\frac{\kappa_{Q_A}(1+t)}{\kappa_P(1+t)}-1
\right|
\longrightarrow0.
}
\tag{5}
\]

More precisely, if

\[
\eta_A(t)=C_A^{-1-t},
\]

and `M_j^S(1+t)` denotes the `j`th raw logarithmic moment of a positive Dirichlet source `S`, then for `j=0,1,2`,

\[
\boxed{
\sup_{0<t\le1/A}
\left|
\frac{M_j^{Q_A}(1+t)}{\eta_A(t)M_j^P(1+t)}-1
\right|
\longrightarrow0.
}
\tag{6}
\]

Since `\eta_A(t)\sim C_A^{-1}\to0` uniformly on `(0,1/A]`, equation `(6)` gives `(4)`. Equation `(5)` follows because all three normalized moment participations collapse to the same vanishing factor, so the exact three-moment curvature formula from AF-521 cancels that common factor.

A concrete admissible choice is

\[
C_A=\left\lfloor\sqrt{\frac{L_A}{H_A}}\right\rfloor,
\tag{7}
\]

the endpoint-`\lambda=1` family already used at the single scale `t=1/A` in AF-522. AF-523 shows that its invisibility is not a one-point accident: it persists simultaneously over a continuum of boundary scales.

Consequently, observing scalar log-curvature at any finite collection of scales `t_{A,k}\le1/A`, or even observing its complete leading relative profile over the whole interval `(0,1/A]`, does not recover the lost prime provenance within this control class. Multi-scale observation only becomes potentially stronger if it leaves this boundary layer, retains lower-order information, or enriches the observable beyond normalized scalar curvature.

## Derivation

### 1. Uniform reference-source asymptotics

Put

\[
J(t)=\log\frac1t.
\]

For `0<t\le1/A`, one has `J(t)\ge L_A`. The classical prime-zeta expansion at `s=1` and its first two derivatives give uniformly in this range

\[
M_0^P(1+t)=P(1+t)=J(t)+O(1),
\tag{8}
\]

\[
M_1^P(1+t)=\frac1t+O(1),
\qquad
M_2^P(1+t)=\frac1{t^2}+O(1).
\tag{9}
\]

Hence

\[
r(t):=
\frac{(M_1^P(1+t))^2}
{M_0^P(1+t)M_2^P(1+t)}
=
\frac1{J(t)}(1+o(1)),
\tag{10}
\]

uniformly on `(0,1/A]`; in particular

\[
\sup_{0<t\le1/A}r(t)=O(L_A^{-1}).
\tag{11}
\]

For the retained prefix define

\[
B_j(A,t)=
\sum_{p\le A}(\log p)^jp^{-1-t},
\qquad j=0,1,2.
\tag{12}
\]

Because `t\log p\le L_A/A=o(1)` uniformly for `p\le A`, Mertens' prime estimates and partial summation give uniformly on `(0,1/A]`

\[
B_0(A,t)=H_A+O(1),
\tag{13}
\]

\[
B_1(A,t)=L_A+o(L_A),
\tag{14}
\]

and

\[
B_2(A,t)=\frac12L_A^2+o(L_A^2).
\tag{15}
\]

The exact constants in `(14)`--`(15)` are not essential below; what matters is that the retained prefix moments grow only polylogarithmically while the full first and second moments have scales `t^{-1}` and `t^{-2}`.

### 2. The retained anchor is uniformly smaller than the transported tail

Let

\[
d_A=\log C_A,
\qquad
\eta_A(t)=C_A^{-1-t}.
\tag{16}
\]

Condition `(1)` implies eventually `C_A<L_A/H_A`, so `d_A=O(H_A)`. Since `t\le1/A`,

\[
td_A=O(H_A/A)=o(1),
\]

and therefore

\[
\eta_A(t)=C_A^{-1}(1+o(1))
\tag{17}
\]

uniformly throughout `(0,1/A]`.

For the zeroth moment, equation `(2)` gives exactly

\[
M_0^{Q_A}
=B_0+\eta_A(M_0^P-B_0).
\tag{18}
\]

By `(8)`, `(13)`, and `J(t)\ge L_A`,

\[
\frac{B_0}{M_0^P}
=O\!\left(\frac{H_A}{J(t)}\right)
=O\!\left(\frac{H_A}{L_A}\right).
\tag{19}
\]

Relative to the transported-tail factor, `(1)` and `(17)` give

\[
\frac{B_0/M_0^P}{\eta_A(t)}
=O\!\left(\frac{C_AH_A}{L_A}\right)
=o(1)
\tag{20}
\]

uniformly. Thus

\[
\frac{M_0^{Q_A}}{M_0^P}
=\eta_A(t)(1+o(1)).
\tag{21}
\]

This is already stronger than pointwise source extinction: the fixed prime anchor is negligible compared with the dilated tail everywhere in the whole boundary layer.

### 3. The same factor controls the first two logarithmic moments

Transporting `p` to `C_Ap` shifts its logarithmic coordinate by `d_A`. Hence the first two moments are exactly

\[
M_1^{Q_A}
=B_1+\eta_A\bigl[(M_1^P-B_1)+d_A(M_0^P-B_0)\bigr],
\tag{22}
\]

and

\[
\begin{aligned}
M_2^{Q_A}
={}&B_2+\eta_A\bigl[(M_2^P-B_2)
+2d_A(M_1^P-B_1)\\
&\hspace{34mm}+d_A^2(M_0^P-B_0)\bigr].
\end{aligned}
\tag{23}
\]

For the first moment, equations `(9)` and `(14)` give

\[
\frac{B_1}{M_1^P}=O(tL_A)
\le O(L_A/A).
\tag{24}
\]

Since `\eta_A\gg H_A/L_A`,

\[
\frac{B_1/M_1^P}{\eta_A}
=O\!\left(\frac{C_AL_A}{A}\right)
=o(1);
\tag{25}
\]

indeed `C_A=o(L_A/H_A)` makes the right side `o(L_A^2/(AH_A))`.

The support-shift term is also uniformly negligible relative to the main transported first moment because

\[
\frac{d_AM_0^P}{M_1^P}
=O\bigl(d_AtJ(t)\bigr).
\tag{26}
\]

For `0<t\le1/A`, the function `t\log(1/t)` is increasing for all sufficiently large `A`, so

\[
\sup_{0<t\le1/A}d_AtJ(t)
=O\!\left(\frac{H_AL_A}{A}\right)
=o(1).
\tag{27}
\]

Equations `(22)`, `(24)`--`(27)` therefore yield

\[
\frac{M_1^{Q_A}}{M_1^P}
=\eta_A(t)(1+o(1))
\tag{28}
\]

uniformly.

For the second moment,

\[
\frac{B_2}{M_2^P}=O(t^2L_A^2)
\le O(L_A^2/A^2)
=o(\eta_A),
\tag{29}
\]

while the two support-shift corrections satisfy

\[
\frac{d_AM_1^P}{M_2^P}=O(d_At)
=O(H_A/A)=o(1),
\tag{30}
\]

and

\[
\frac{d_A^2M_0^P}{M_2^P}
=O\bigl(d_A^2t^2J(t)\bigr)
=O\!\left(\frac{H_A^2L_A}{A^2}\right)
=o(1)
\tag{31}
\]

uniformly. Substitution into `(23)` gives

\[
\frac{M_2^{Q_A}}{M_2^P}
=\eta_A(t)(1+o(1))
\tag{32}
\]

uniformly. Equations `(21)`, `(28)`, and `(32)` prove `(6)`.

### 4. Common extinction is an asymptotic dilation gauge

Set

\[
\rho_j(A,t)=
\frac{M_j^{Q_A}(1+t)}{M_j^P(1+t)},
\qquad j=0,1,2.
\]

AF-521 gives the exact identity

\[
\frac{\kappa_{Q_A}(1+t)}{\kappa_P(1+t)}
=
\frac{
\rho_2/\rho_0-r(t)(\rho_1/\rho_0)^2
}{1-r(t)}.
\tag{33}
\]

By `(6)`,

\[
\frac{\rho_1}{\rho_0}\to1,
\qquad
\frac{\rho_2}{\rho_0}\to1
\tag{34}
\]

uniformly, while `(11)` gives `r(t)\to0` uniformly. Equation `(33)` therefore proves `(5)`.

The mechanism is the moving-boundary analogue of AF-509's exact dilation gauge. A global dilation satisfies

\[
P_{cQ}(s)=c^{-s}P_Q(s)
\]

and therefore leaves log-curvature exactly unchanged. Here the retained prime prefix prevents `(2)` from being an exact global dilation. But condition `(1)` makes that anchor uniformly negligible compared with the transported tail throughout `(0,1/A]`; all first three moment layers therefore inherit the same factor `C_A^{-s}` asymptotically. Curvature cancels the factor and becomes uniformly gauge-blind at leading relative order.

## Fidelity and matched-control audit

The control is deliberately rigid. It uses no arbitrary weights, support collisions, noninteger norms, inward motion, or deletion:

- all primes `p\le A` remain fixed;
- all primes `p>A` move strictly outward to `C_Ap`;
- every target is an ordinary composite integer;
- moved targets are pairwise distinct;
- every coefficient remains exactly one.

Nevertheless the whole normalized boundary-curvature profile in `(5)` cannot distinguish this source from the rational-prime source while `(4)` says their zeroth Dirichlet participation differs maximally in the limit.

This closes the most immediate multi-scale escape left by AF-522. The one-point endpoint `\lambda=1` extends to a continuum of simultaneous observation scales, so taking more scalar-curvature samples inside the same moving boundary layer does not restore provenance.

The result does **not** contradict AF-509. AF-509 concerns exact equality of complete curvature profiles on a fixed open interval for two fixed sources. AF-523 concerns a sequence of changing sources and a shrinking boundary window, with only leading relative asymptotic equality. Exact finite-`A` profiles can still differ, and lower-order information can still distinguish them.

## Representation audit

The mathematical carrier remains scalar logarithmic curvature, equivalently variance of `\log x` under exponential tilting. The new point is not another representation of the source but a uniform failure mode for a proposed enrichment of the observation protocol.

AF-522 showed that one moving scale is insufficient in the extinction regime. AF-523 tests the natural repair "observe many nearby scales" and shows that the repair fails at leading order over an entire continuum when the tail transport approaches the dilation gauge faster than the retained anchor contributes.

Thus the relevant distinction is not merely one-scale versus multi-scale. It is whether the observation family crosses a region in which different moment layers have genuinely different participation profiles. If all visible moment layers share one asymptotic factor, a continuum of scales can still carry only gauge information.

## Prior art and novelty assessment

No novelty is claimed for the analytic-number-theory or exponential-family ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is the classical reference for the prime-zeta singularity at `s=1`; the expansion of `P(1+t)` and its differentiated moment scales used in `(8)`--`(10)` are standard consequences.
- Mertens' prime estimates and partial summation give the prefix asymptotics `(13)`--`(15)`.
- AF-509 establishes the exact global-dilation curvature gauge for simple unit-weight Dirichlet sources.
- AF-521 supplies the exact three-moment curvature identity `(33)`.
- AF-522 constructs the same anchored outward control at the single scale `t=1/A` and identifies the endpoint regime in which curvature tends to the prime value despite source extinction.

A focused literature search located the standard prime-zeta boundary expansion, Mertens prime sums, and ordinary log-partition/variance interpretation, but did not identify a standard theorem formulated as the uniform boundary-layer statement `(4)`--`(6)` for anchored prime-to-composite tail dilation. The result is therefore recorded as an exact internal no-go refinement with `NO-NOVELTY-CLAIM`, not as an external theorem-novelty claim.

## Boundaries and failure modes

1. **Leading relative curvature only.** Equation `(5)` is a relative asymptotic statement. Exact curvature values, absolute differences, or sufficiently precise lower-order terms may retain distinguishing information.
2. **The observation window is one-sided and moving.** The theorem covers `0<t\le1/A`. Scales with `t\gg1/A`, for which the retained prefix can dominate the natural exponential-tilting region, are not covered.
3. **The tail factor must dominate the anchor while still vanishing.** Condition `(1)` is exactly the useful regime `H_A/L_A\ll C_A^{-1}\ll1`. AF-522 shows different curvature limits when the transported-tail factor is only comparable to the anchor share.
4. **Positive simple sources only.** Signed or complex coefficients can create cancellations absent from the moment comparison above.
5. **The control changes with `A`.** This is a conditioning/no-go result for moving source families, not an exact quotient classification for one fixed arithmetic source.
6. **Scalar curvature remains the tested carrier.** Richer marked, relational, operator-valued, or provenance-sensitive observables are not ruled out.
7. **No RH consequence follows.** The theorem classifies a compression failure mode and supplies a matched arithmetic control; it is not evidence for the Riemann hypothesis.

## Research consequence

AF-522 left open whether multi-scale or whole-profile observation could couple the extinction-regime moment ratios strongly enough to recover provenance. AF-523 gives a decisive negative answer for the first natural version of that escape: **throughout the full boundary layer `1<s\le1+1/A`, a rigid anchored prime-to-composite transport can make its source participation vanish while matching the prime log-curvature uniformly at leading relative order.**

The remaining multi-scale frontier must therefore leave at least one of the mechanisms behind `(6)`. Productive next tests are: observe scales `t\gg1/A` where the retained anchor re-enters, retain lower-order curvature information instead of only the leading relative profile, or use a richer observable whose visible layers do not all acquire the same asymptotic dilation factor.