# AF-526 — First curvature defect sees only log-log anchor scale

## Status

`EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `MATCHED-COMPOSITE-CONTROL` · `MESOSCOPIC-CURVATURE` · `LOWER-ORDER-FIDELITY` · `NO-NOVELTY-CLAIM`

## Claim

AF-525 showed that, for one rigid anchored outward tail transport, the first nonzero boundary-layer curvature defect recovers the transport scale once the anchor cutoff is known. Across a broader class in which the anchor cutoff itself may vary, that first defect does not recover the cutoff at its natural asymptotic order. It sees the cutoff only through its logarithmic Mertens mass `log log A`.

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=(\log P(s))'',
\]

and let `A\to\infty` be integer cutoffs. Put

\[
L_A=\log A,
\qquad
H_A=\log L_A.
\]

Choose integers `C_A\ge2` such that

\[
C_A\to\infty,
\qquad
\frac{C_AH_A}{L_A}\to0.
\tag{1}
\]

Let `B_A` be another integer cutoff satisfying

\[
B_A\to\infty,
\qquad
B_A\le A,
\tag{2}
\]

write

\[
L_B=\log B_A,
\qquad
H_B=\log L_B,
\]

and assume the same transport scale is admissible at the second cutoff:

\[
\frac{C_AH_B}{L_B}\to0.
\tag{3}
\]

Define two positive unit-weight sources

\[
Q_A^{(A)}(s)
=
\sum_{p\le A}p^{-s}
+
C_A^{-s}\sum_{p>A}p^{-s},
\tag{4}
\]

and

\[
Q_A^{(B)}(s)
=
\sum_{p\le B_A}p^{-s}
+
C_A^{-s}\sum_{p>B_A}p^{-s}.
\tag{5}
\]

Thus the two controls use exactly the same outward multiplicative transport `p\mapsto C_Ap`; they differ only in where the retained prime anchor ends.

For `0<t\le1/A`, define their normalized curvature defects

\[
\Delta_A^{(A)}(t)
=
1-
\frac{\kappa_{Q_A^{(A)}}(1+t)}{\kappa_P(1+t)},
\]

\[
\Delta_A^{(B)}(t)
=
1-
\frac{\kappa_{Q_A^{(B)}}(1+t)}{\kappa_P(1+t)}.
\tag{6}
\]

If

\[
\frac{H_B}{H_A}\longrightarrow\rho
\qquad (0\le\rho\le1),
\tag{7}
\]

then

\[
\boxed{
\sup_{0<t\le1/A}
\left|
\frac{\Delta_A^{(B)}(t)}{\Delta_A^{(A)}(t)}-\rho
\right|
\longrightarrow0.
}
\tag{8}
\]

In particular, for every fixed `\theta\in(0,1)`, take

\[
B_A=\lfloor A^\theta\rfloor.
\tag{9}
\]

Then `(3)` follows from `(1)` and

\[
H_B
=
\log\log B_A
=
H_A+\log\theta+o(1),
\tag{10}
\]

so `H_B/H_A\to1`. Hence

\[
\boxed{
\sup_{0<t\le1/A}
\left|
\frac{\Delta_A^{(B)}(t)}{\Delta_A^{(A)}(t)}-1
\right|
\longrightarrow0.
}
\tag{11}
\]

The two source families are nevertheless provenance-distinct: `B_A/A\to0`, and for all sufficiently large `A` there are primes in `(B_A,A]`, which are retained in `(4)` but transported to composites in `(5)`. Therefore even a power-separated change of anchor cutoff is invisible to the **first nonzero normalized boundary-layer curvature correction** at relative asymptotic order.

Equivalently, AF-525's recovery formula for `C_A` is conditional on knowing the anchor normalization `H_A`. Once the anchor cutoff is itself part of the unknown source provenance, the first defect identifies only its leading log-log mass, not the cutoff scale.

## Derivation

### 1. Both transports fall under AF-525 on the common window

Condition `(1)` is exactly the source-extinct boundary-layer regime of AF-525 for cutoff `A`. Conditions `(2)`--`(3)` give the same regime for cutoff `B_A` with the same integer dilation `C_A`.

AF-525 applies to `Q_A^{(A)}` on

\[
0<t\le1/A
\]

and to `Q_A^{(B)}` on the larger window

\[
0<t\le1/B_A.
\]

Since `B_A\le A`, the first window is contained in the second. We may therefore compare both curvature defects uniformly on the common observed layer

\[
W_A=(0,1/A].
\tag{12}
\]

Put

\[
\eta_A(t)=C_A^{-1-t},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t}.
\]

The exact AF-525 anchor-to-transport carrier at cutoff `X` is

\[
D_X(t)
=
\frac{1-\eta_A(t)}{\eta_A(t)}
\frac{B_0(X,t)}{P(1+t)}.
\tag{13}
\]

Because both controls use the same `C_A`, the factors involving `\eta_A` and `P(1+t)` cancel exactly when the two carriers are compared:

\[
\boxed{
\frac{D_{B_A}(t)}{D_A(t)}
=
\frac{B_0(B_A,t)}{B_0(A,t)}.
}
\tag{14}
\]

Thus varying the anchor cutoff is seen at first order only through the retained zeroth logarithmic moment.

### 2. The retained zeroth moment compresses the cutoff to log-log scale

The uniform Mertens estimate used in AF-525 gives, on the appropriate boundary layer,

\[
B_0(X,t)=\log\log X+O(1).
\tag{15}
\]

For `X=A` this holds uniformly on `W_A`. For `X=B_A` it holds uniformly on `0<t\le1/B_A`, hence also on `W_A`. Since `H_A,H_B\to\infty`, `(14)`--`(15)` imply

\[
\sup_{t\in W_A}
\left|
\frac{D_{B_A}(t)}{D_A(t)}
-
\frac{H_B}{H_A}
\right|
\longrightarrow0.
\tag{16}
\]

Under `(7)`, therefore,

\[
\frac{D_{B_A}(t)}{D_A(t)}\to\rho
\]

uniformly on the common layer.

### 3. Curvature carries exactly the same first-order collapse

AF-525 proves, for each admissible anchored family,

\[
\frac{\Delta_X(t)}{D_X(t)}\to1
\tag{17}
\]

uniformly over its full boundary layer. Applying `(17)` at `X=A` and `X=B_A`, then restricting both to `W_A`, gives

\[
\frac{\Delta_A^{(B)}(t)}{\Delta_A^{(A)}(t)}
=
\frac{\Delta_A^{(B)}(t)}{D_{B_A}(t)}
\frac{D_{B_A}(t)}{D_A(t)}
\frac{D_A(t)}{\Delta_A^{(A)}(t)}.
\tag{18}
\]

The first and third factors tend uniformly to one; the middle factor tends uniformly to `\rho` by `(16)`. This proves `(8)`.

For the fixed-power choice `(9)`,

\[
\log B_A=\theta\log A+o(\log A),
\]

so `(10)` follows. Moreover

\[
\frac{C_AH_B}{L_B}
\sim
\frac1\theta
\frac{C_AH_A}{L_A}
\to0,
\]

which verifies `(3)` automatically. Therefore `(11)` is an immediate corollary.

### 4. The collision is not source equality

For fixed `\theta\in(0,1)`, the interval `(B_A,A]` contains primes for all sufficiently large `A` by the prime number theorem. Any such prime `p` contributes the atom `p` to `Q_A^{(A)}` but contributes the distinct composite atom `C_Ap` to `Q_A^{(B)}`. Hence the source measures are different even though their first curvature defects have ratio tending uniformly to one on `W_A`.

The result is therefore an asymptotic representation collision, not an equality of sources or of complete curvature profiles.

## Fidelity and matched-control audit

The matched controls remain unusually rigid. Both sources have positive unit coefficients; both begin from the same rational-prime support; both retain an initial prime segment exactly; both move the remaining primes only outward to distinct ordinary composite atoms; both use the same multiplier `C_A`; and both are observed on the same boundary layer. The only changed provenance datum is the anchor cutoff.

AF-525's first correction is carried by the retained zeroth-moment prefix `B_0(X,t)`. AF-526 shows that this carrier itself is a compression: at the relevant boundary scale it remembers `X` only through the slowly varying quantity `log log X`. Consequently, cutoffs separated by a fixed power have the same first-order carrier even though their retained prime sets differ on an asymptotically enormous interval.

This closes one natural interpretation of AF-525. The first defect is genuinely informative inside a family where `A` is known and only `C_A` is unknown, but it is not a source-specific provenance marker once the anchor boundary is allowed to vary. A lower-order discriminator must therefore retain more than the leading Mertens mass of the anchor if it is to distinguish such controls.

## Representation audit

The source class is the positive unit-weight anchored tail-transport family with variable cutoff. The observed representation is the first nonzero asymptotic jet of the scalar normalized curvature profile on the common shrinking layer `W_A`.

At this resolution the map from source provenance to observation factors through

\[
X\longmapsto B_0(X,t)\sim\log\log X.
\]

Equation `(8)` makes the resulting equivalence explicit: two admissible anchor sequences whose log-log masses have asymptotic ratio `\rho` have first curvature defects with the same ratio `\rho`. In particular, the `\rho=1` class contains every fixed-power cutoff `A^\theta`, `0<\theta<1`.

This does not contradict AF-509--AF-510, which concern exact recovery from the complete curvature profile of fixed simple sources up to global dilation. Nor does it contradict AF-525, whose recovery of `C_A` divides by the externally known `H_A`. The lost datum here is precisely the unknown anchor provenance after truncating the observation to its first boundary-layer curvature correction.

## Prior art and novelty assessment

No novelty is claimed for the analytic ingredients. The proof uses only AF-525, the same classical prime-zeta/Mertens estimates already audited there, the prime number theorem to certify that the two retained supports are eventually distinct, and the elementary slowly varying identity

\[
\frac{\log\log(A^\theta)}{\log\log A}\to1
\qquad (0<\theta<1).
\]

The language of slowly varying functions is classical regular-variation theory; the present use does not claim a new theorem in that literature. The Arithmetic-Fidelity contribution is the matched-control interpretation: the first lower-order curvature carrier established in AF-525 factors through a slowly varying anchor statistic, so it cannot identify the anchor cutoff at power-scale resolution.

A literature check around positive Dirichlet-series log-convexity and the prime-zeta singularity found the standard analytic background, but no reason to reinterpret this direct AF-525 consequence as an independent classical theorem. It should therefore be treated as an exact derived obstruction inside the current source model, not as a novelty claim about prime-zeta analysis.

## Boundaries

- Equation `(8)` concerns the **first** nonzero boundary-layer curvature defect. It does not assert equality of higher asymptotic corrections or of full curvature profiles.
- The common observation window is `0<t\le1/A`; changing the window can expose additional information.
- The two transports use the same multiplier `C_A`. Allowing different multipliers creates further confounding, but that larger classification is not needed for this obstruction.
- The result identifies a failure of anchor-cutoff recovery, not a failure of exact prime-source recovery from unrestricted data.
- For `\rho<1`, condition `(3)` is an independent admissibility requirement; it must not be inferred from `(1)` without information on the growth of `B_A`.
- The fixed-power collision `(9)` is the clean unconditional specialization within the AF-525 regime: there `(3)` follows directly from `(1)`.
