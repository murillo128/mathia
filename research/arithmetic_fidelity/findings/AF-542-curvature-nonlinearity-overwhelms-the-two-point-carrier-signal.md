# AF-542 — Curvature nonlinearity overwhelms the two-point carrier signal

## Status

`EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CURVATURE-COMPRESSION` · `FINITE-RESOLUTION` · `CONDITIONING` · `REPRESENTATION-TRANSFER` · `NO-NOVELTY-CLAIM`

## Claim

AF-541 proved that a weighted two-point contrast of the **exact anchor carrier** recovers a power-separated cutoff exponent while cancelling arbitrary tail-multiplier drift. That recovery does **not** survive passage to the actual normalized-curvature defect, even in the much smaller subfamily where the two sources use the same AF-525-admissible multiplier.

Fix `0<\theta<1`, put

\[
B_A=\lfloor A^\theta\rfloor,
\qquad
L_A=\log A,
\qquad
H_A=\log L_A,
\qquad
h_A=A^{-1},
\]

and choose integers `C_A\ge2` such that

\[
C_A\to\infty,
\qquad
\frac{C_AH_A}{L_A}\to0.
\tag{1}
\]

For `X\in\{A,B_A\}`, let

\[
Q_{X,C_A}(s)
=
\sum_{p\le X}p^{-s}
+
C_A^{-s}\sum_{p>X}p^{-s},
\]

and write

\[
\Delta_{X,C_A}(t)
=
1-
\frac{\kappa_{Q_{X,C_A}}(1+t)}{\kappa_P(1+t)}
\]

for the actual normalized-curvature defect. Its AF-525 carrier is

\[
D_{X,C_A}(t)
=
\frac{(C_A^{1+t}-1)B_0(X,t)}{P(1+t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t}.
\]

Define the exact-carrier and actual-curvature ratios

\[
R_A(t)=\frac{D_{B_A,C_A}(t)}{D_{A,C_A}(t)},
\qquad
\widehat R_A(t)=\frac{\Delta_{B_A,C_A}(t)}{\Delta_{A,C_A}(t)}.
\tag{2}
\]

Both ratios extend continuously to `t=0`, and their quotient tends there to one. At the endpoint `h_A=1/A`, however,

\[
\boxed{
\log \widehat R_A(h_A)-\log R_A(h_A)
=
(-\log\theta)\frac{C_A-1}{L_A}\,(1+o(1)).
}
\tag{3}
\]

Thus the actual-curvature representation adds a deterministic nonlinear correction of order `C_A/L_A`. AF-541's weighted two-point carrier signal has the much smaller order

\[
\frac{L_A}{A H_A}.
\]

Indeed, with

\[
Q_hf=f(h)-(1+h)f(0),
\]

AF-541 gives

\[
\frac{H_A}{h_AL_A}Q_{h_A}\log R_A\to1-\theta,
\]

whereas `(3)` and equality of the `t=0` correction imply

\[
\boxed{
\frac{H_A}{h_AL_A}Q_{h_A}\log \widehat R_A
=
1-\theta
+(-\log\theta)\frac{A(C_A-1)H_A}{L_A^2}(1+o(1))
\longrightarrow+\infty.
}
\tag{4}
\]

Therefore the minimal two-sample annihilator discovered for the exact carrier is **not representation-stable** under the actual curvature compression. The obstruction is not tail-multiplier drift: the same multiplier is used in numerator and denominator. It is the first nonlinear correction in the map from the AF-525 carrier to curvature itself.

This closes the direct AF-541-to-curvature transfer route at its natural endpoint resolution. Any successful curvature-level recovery must either remove this nonlinear defect before forming the two-point contrast, retain enough additional information to estimate it, or work at a different asymptotic scale/representation.

## Derivation

### 1. Exact curvature defect as a nonlinear function of the carrier

Use the notation of AF-525. For a cutoff `X`, write

\[
\rho_0=\eta(1+D_X),
\qquad
\rho_1=\eta(1+E_{1,X}),
\qquad
\rho_2=\eta(1+E_{2,X}),
\]

where

\[
\eta=C_A^{-1-t},
\qquad
D_X=D_{X,C_A}(t),
\]

and let

\[
r(t)=\frac{(M_1^P(1+t))^2}{M_0^P(1+t)M_2^P(1+t)}.
\]

AF-525's exact three-moment identity gives

\[
\frac{\kappa_{Q_{X,C_A}}}{\kappa_P}
=
\frac{(1+E_{2,X})/(1+D_X)
-r(t)(1+E_{1,X})^2/(1+D_X)^2}
{1-r(t)}.
\]

Consequently the exact relative carrier error

\[
q_X(t):=\frac{\Delta_{X,C_A}(t)}{D_X(t)}
\]

is

\[
q_X
=
\frac{
(1-2r)+(1-r)D_X
-(1+D_X)E_{2,X}/D_X
+2rE_{1,X}/D_X
+rE_{1,X}^2/D_X
}
{(1-r)(1+D_X)^2}.
\tag{5}
\]

If the `E`-terms are temporarily suppressed, define

\[
F(D,r)
=
\frac{(1-2r)+(1-r)D}{(1-r)(1+D)^2}.
\tag{6}
\]

As `(D,r)\to(0,0)`,

\[
\partial_DF(D,r)=-1+o(1).
\tag{7}
\]

The key point is that AF-525's statement `q_X\to1` hides a first nonlinear correction of size `-D_X`. That correction is harmless for value-level carrier equivalence but can dominate a much smaller transverse shape signal.

### 2. On the common endpoint, the non-carrier moment terms are smaller than the cutoff difference

Evaluate at `t=h_A=1/A`. For both `X=A` and `X=B_A`, the AF-525 estimates restricted to this common window give

\[
r(h_A)=O(L_A^{-1}),
\qquad
D_X(h_A)=O\!\left(\frac{C_AH_A}{L_A}\right)=o(1),
\tag{8}
\]

and

\[
\frac{E_{1,X}(h_A)}{D_X(h_A)}
=O\!\left(\frac{L_A^2}{AH_A}\right),
\tag{9}
\]

\[
\frac{E_{2,X}(h_A)}{D_X(h_A)}
=O\!\left(\frac{L_A}{AH_A}
+rac{L_A^3}{A^2H_A}\right).
\tag{10}
\]

The quadratic `E_{1,X}` term in `(5)` is smaller still. Hence the total contribution of the `E`-terms to `q_X(h_A)` is

\[
O\!\left(\frac{L_A}{AH_A}ight).
\tag{11}
\]

This is the AF-541 finite-shape scale. It will be negligible compared with the cutoff-dependent nonlinear carrier correction below.

### 3. The two cutoff carriers differ by `C_A/L_A`, not by the AF-541 shape scale

Because the multiplier and prime-zeta factors are common,

\[
D_{A,C_A}(h_A)-D_{B_A,C_A}(h_A)
=
\frac{C_A^{1+h_A}-1}{P(1+h_A)}
\sum_{B_A<p\le A}p^{-1-h_A}.
\tag{12}
\]

The same Mertens estimates already audited in AF-525 and AF-541 give

\[
P(1+h_A)=L_A+O(1),
\tag{13}
\]

and, since `p^{-1/A}=1+o(1)` uniformly for `p\le A`,

\[
\sum_{B_A<p\le A}p^{-1-h_A}
=-\log\theta+o(1).
\tag{14}
\]

Condition `(1)` implies `\log C_A=O(H_A)` and therefore

\[
C_A^{1+h_A}-1=(C_A-1)(1+o(1)).
\tag{15}
\]

Combining `(12)`--`(15)`,

\[
\boxed{
D_A(h_A)-D_B(h_A)
=
(-\log\theta)\frac{C_A-1}{L_A}(1+o(1)).
}
\tag{16}
\]

The error scale in `(11)` is negligible relative to `(16)` because

\[
\frac{L_A/(AH_A)}{(C_A-1)/L_A}
=
O\!\left(\frac{L_A^2}{A H_A(C_A-1)}\right)
\to0.
\tag{17}
\]

### 4. The common curvature background cancels but the nonlinear carrier correction does not

Equation `(5)` can be written as

\[
q_X(h_A)=F(D_X(h_A),r(h_A))
+O\!\left(\frac{L_A}{AH_A}\right).
\tag{18}
\]

The `r`-dependence is identical for the two sources. By the mean-value theorem, `(7)`, `(8)`, and `(16)`,

\[
q_{B_A}(h_A)-q_A(h_A)
=
D_A(h_A)-D_B(h_A)
+o\!\left(\frac{C_A}{L_A}\right).
\tag{19}
\]

Moreover `q_A(h_A),q_{B_A}(h_A)\to1`, so logarithmization preserves the first difference:

\[
\log q_{B_A}(h_A)-\log q_A(h_A)
=
D_A(h_A)-D_B(h_A)
+o\!left(\frac{C_A}{L_A}\right).
\tag{20}
\]

For each fixed `A`, direct use of the prime-zeta singularity as `t\downarrow0` gives

\[
q_A(t)\to1,
\qquad
q_{B_A}(t)\to1.
\tag{21}
\]

Thus `\widehat R_A/R_A=q_{B_A}/q_A` extends continuously to `t=0` with value one. Equations `(16)` and `(20)` prove `(3)`. Because the correction at `t=0` is exactly zero, it passes unchanged through the AF-541 functional `Q_{h_A}`, and `(4)` follows.

## Fidelity and matched-control audit

This is a stronger falsifier than changing the tail multiplier. The two sources use the **same** `C_A`, the same positive unit coefficients, the same rational-prime source, the same outward multiplicative transport, and the same observed boundary layer. Their only provenance difference is the retained cutoff `A` versus `A^\theta`.

At carrier level, the weighted two-point observable succeeds because the cutoff information lives in the transverse variation of `B_0(X,t)` and the multiplier nuisance can be annihilated. Curvature adds another compression after that carrier has been formed. Its first nonlinear term depends on the carrier amplitude itself. Since the two cutoffs have carrier amplitudes differing by order `C_A/L_A`, that post-compression term is much larger than the order `L_A/(AH_A)` transverse signal.

The failure is therefore a direct example of the line's composition principle: a discriminator can survive one representation and still be destroyed by a later nonlinear compression whose nominal approximation error is small in absolute or relative terms but large compared with the discriminator scale.

Matched generalized-prime or non-prime systems remain relevant controls for any later arithmetic interpretation, but they are not needed to produce this obstruction. The loss already occurs inside the rigid prime-derived control family.

## Representation audit

The source-to-observation chain is

\[
\text{anchored source}
\longrightarrow
D_{X,C}(t)
\longrightarrow
\Delta_{X,C}(t)
\longrightarrow
Q_h\log\frac{\Delta_B}{\Delta_A}.
\]

AF-541 established fidelity of the final two-point functional when applied after the **first** arrow. AF-542 shows that fidelity is not compositional under the **second** arrow at the required resolution.

The issue is not that AF-525 was wrong: its uniform statement

\[
\Delta_{X,C}(t)=D_{X,C}(t)(1+o(1))
\]

is sufficient for first-order value asymptotics. It is simply too coarse for a downstream statistic whose target lives at scale `L_A/(AH_A)`. Here the structured `o(1)` contains a cutoff-dependent term of order `D_X`, and the difference of those terms across the two sources is order `C_A/L_A`.

Thus a value-level asymptotic equivalence cannot be pushed through an increasingly ill-conditioned relational observable without controlling the approximation error in the observable's own transverse seminorm.

## Prior-art / novelty audit

No novelty is claimed for the analytic-number-theory ingredients, Taylor expansion of a nonlinear observation map, finite-difference conditioning, or the general fact that small value errors can be amplified by derivative-like contrasts.

The prime-zeta and Mertens estimates are the same classical inputs already sourced and audited in AF-525, AF-529, and AF-541. AF-541 also records standard prior art on nuisance projection/reference differencing, divided differences and finite-difference weights, and numerical differentiation of noisy data (Cox--Reid; Hu--Leus; de Boor; Fornberg; Chartrand). A targeted literature check again located the generic numerical-differentiation/finite-difference stability literature rather than an arithmetic theorem corresponding to `(3)`--`(4)`.

The durable Arithmetic Fidelity result is the exact source-specific scale comparison: the first nonlinear curvature correction creates a cutoff-dependent discrepancy `\asymp C_A/L_A`, while the carrier discriminator exposed by the two-point annihilator is only `\asymp L_A/(AH_A)`. This is retained as a no-go theorem for this representation chain, not as a claim of a new general theorem about numerical differentiation.

## Boundaries

- The result closes the direct AF-541 weighted two-point transfer to the **raw normalized-curvature defect** at `h=1/A`. It does not rule out a curvature-level observable that explicitly subtracts or estimates the nonlinear carrier correction.
- The theorem uses a common AF-525-admissible multiplier. It therefore disproves representation stability without needing arbitrary multiplier drift, but it does not classify all unequal-multiplier curvature ratios.
- The divergence in `(4)` is a conditioning statement for this normalization, not a divergence of the curvature defects themselves; each defect remains asymptotically small.
- The target remains only the coarse cutoff exponent `\theta`. No statement here identifies rational primes, zeta zeros, or RH.
- The proof uses the endpoint `h=1/A`, which maximizes AF-541's deterministic noise budget. Smaller separations do not repair the fundamental scale mismatch without a separate cancellation of the nonlinear curvature term.

## Consequence

The next useful question is no longer whether the AF-541 carrier contrast can be transferred by invoking AF-525's value-level equivalence; it cannot. A viable curvature route must construct a **curvature-native renormalization or relational lift** that removes the order-`D` nonlinear observation term before trying to read the much smaller cutoff-shape signal. More generally, Arithmetic Fidelity should measure approximation errors after applying the same transverse functional used by the discriminator, not only in the upstream value norm.