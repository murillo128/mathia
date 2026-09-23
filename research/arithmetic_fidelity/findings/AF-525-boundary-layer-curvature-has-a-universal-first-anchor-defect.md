# AF-525 — Boundary-layer curvature has a universal first anchor defect

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `MATCHED-COMPOSITE-CONTROL` · `MESOSCOPIC-CURVATURE` · `LOWER-ORDER-FIDELITY` · `NO-NOVELTY-CLAIM`

## Claim

Keep the rigid anchored tail-transport family of AF-523. Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=(\log P(s))'',
\]

and for an integer cutoff `A\to\infty` put

\[
L_A=\log A,
\qquad
H_A=\log L_A.
\]

Choose integers `C_A\ge2` satisfying

\[
C_A\to\infty,
\qquad
\frac{C_AH_A}{L_A}\to0,
\tag{1}
\]

and define

\[
Q_A(s)
=
\sum_{p\le A}p^{-s}
+
C_A^{-s}\sum_{p>A}p^{-s}.
\tag{2}
\]

Thus every prime `p\le A` is fixed and every prime `p>A` is moved to the distinct ordinary composite atom `C_Ap`, with coefficient one.

AF-523 proved that throughout the whole boundary layer

\[
0<t\le A^{-1},
\qquad s=1+t,
\tag{3}
\]

the leading relative curvature is blind:

\[
\frac{\kappa_{Q_A}(1+t)}{\kappa_P(1+t)}\to1
\]

uniformly. The first non-zero correction is nevertheless universal and records the retained anchor against the transported tail.

Write

\[
J(t)=\log\frac1t,
\qquad
\eta_A(t)=C_A^{-1-t},
\]

and

\[
B_0(A,t)=\sum_{p\le A}p^{-1-t}.
\]

Define the exact anchor-to-transport defect

\[
D_A(t)
=
\frac{1-\eta_A(t)}{\eta_A(t)}
\frac{B_0(A,t)}{P(1+t)}.
\tag{4}
\]

Then

\[
\boxed{
\sup_{0<t\le1/A}
\left|
\frac{1-\kappa_{Q_A}(1+t)/\kappa_P(1+t)}{D_A(t)}-1
\right|
\longrightarrow0.
}
\tag{5}
\]

Moreover, uniformly on the same boundary layer,

\[
\boxed{
D_A(t)
\sim
\frac{C_AH_A}{J(t)}.
}
\tag{6}
\]

Hence the lower-order curvature profile obeys the explicit law

\[
\boxed{
1-rac{\kappa_{Q_A}(1+t)}{\kappa_P(1+t)}
\sim
\frac{C_A\log\log A}{\log(1/t)}
}
\tag{7}
\]

uniformly for `0<t\le1/A`.

At the endpoint `t=1/A`, this becomes

\[
\boxed{
\frac{\kappa_{Q_A}(1+1/A)}{\kappa_P(1+1/A)}
=
1-rac{C_AH_A}{L_A}
+o\!\left(\frac{C_AH_A}{L_A}\right).
}
\tag{8}
\]

Thus AF-523's leading-order blindness is not blindness to all asymptotic orders. Inside this rigid control family, the first curvature defect recovers the transport scale asymptotically:

\[
C_A
\sim
\frac{J(t)}{H_A}
\left(
1-rac{\kappa_{Q_A}(1+t)}{\kappa_P(1+t)}
\right),
\tag{9}
\]

uniformly throughout the layer. This is recovery of a control-family provenance parameter, not recovery of the full source or of primality in general.

## Derivation

### 1. Exact moment decomposition

Let

\[
M_j^P(1+t)=\sum_p(\log p)^jp^{-1-t},
\qquad
B_j(A,t)=\sum_{p\le A}(\log p)^jp^{-1-t},
\]

for `j=0,1,2`, and write

\[
\rho_j(A,t)=\frac{M_j^{Q_A}(1+t)}{M_j^P(1+t)}.
\]

Put `d_A=\log C_A`. The exact transported-moment identities from AF-523 are

\[
\rho_0
=
\eta_A+(1-\eta_A)u_0,
\qquad
u_j:=\frac{B_j}{M_j^P},
\tag{10}
\]

\[
\rho_1
=
\eta_A+(1-\eta_A)u_1
+
\eta_A d_A\frac{M_0^P}{M_1^P}(1-u_0),
\tag{11}
\]

and

\[
\rho_2
=
\eta_A+(1-\eta_A)u_2
+2\eta_A d_A\frac{M_1^P}{M_2^P}(1-u_1)
+\eta_A d_A^2\frac{M_0^P}{M_2^P}(1-u_0).
\tag{12}
\]

Equation `(4)` is exactly

\[
D_A(t)=\frac{1-\eta_A}{\eta_A}u_0,
\]

so `(10)` is the exact factorization

\[
\boxed{
\rho_0=\eta_A(1+D_A).
}
\tag{13}
\]

This identifies the candidate lower-order variable without approximation: it is the retained zeroth-moment anchor divided by the transported-tail normalization.

### 2. Size of the anchor defect

For `0<t\le1/A`, AF-523 established the uniform estimates

\[
P(1+t)=J(t)+O(1),
\tag{14}
\]

\[
B_0(A,t)=H_A+O(1),
\tag{15}
\]

and, from `(1)`,

\[
\eta_A(t)=C_A^{-1}(1+o(1))
\tag{16}
\]

uniformly. Since `J(t)\ge L_A\to\infty` and `H_A\to\infty`, equations `(14)`--`(16)` give

\[
D_A(t)
=
\frac{C_AH_A}{J(t)}(1+o(1))
\tag{17}
\]

uniformly, proving `(6)`. In particular

\[
0<D_A(t)\le(1+o(1))\frac{C_AH_A}{L_A}=o(1)
\tag{18}
\]

uniformly.

### 3. The first and second moments have smaller relative defects

Define `E_{1,A}` and `E_{2,A}` by

\[
\rho_1=\eta_A(1+E_{1,A}),
\qquad
\rho_2=\eta_A(1+E_{2,A}).
\tag{19}
\]

From `(11)`--`(12)`,

\[
E_{1,A}
=
\frac{1-\eta_A}{\eta_A}u_1
+d_A\frac{M_0^P}{M_1^P}(1-u_0),
\tag{20}
\]

and

\[
E_{2,A}
=
\frac{1-\eta_A}{\eta_A}u_2
+2d_A\frac{M_1^P}{M_2^P}(1-u_1)
+d_A^2\frac{M_0^P}{M_2^P}(1-u_0).
\tag{21}
\]

The same uniform prime-zeta and Mertens estimates used in AF-523 give

\[
M_1^P(1+t)\sim t^{-1},
\qquad
M_2^P(1+t)\sim t^{-2},
\tag{22}
\]

\[
B_1(A,t)\sim L_A,
\qquad
B_2(A,t)\sim\frac12L_A^2.
\tag{23}
\]

For the prefix term in `(20)`, division by `D_A` cancels the transport factor exactly, leaving

\[
\frac{u_1}{u_0}
=O\!\left(
\frac{tJ(t)L_A}{H_A}
\right).
\tag{24}
\]

For sufficiently large `A`, `tJ(t)` increases on `(0,1/A]`, so

\[
\sup_{0<t\le1/A}
\frac{u_1}{u_0}
=O\!\left(\frac{L_A^2}{AH_A}\right)
=o(1).
\tag{25}
\]

The support-shift term in `(20)`, again relative to `D_A`, is

\[
O\!\left(
\frac{d_A}{C_A}
\frac{tJ(t)^2}{H_A}
\right).
\tag{26}
\]

Since `(\log C_A)/C_A` is bounded and `tJ(t)^2` is eventually increasing on the layer,

\[
\sup_{0<t\le1/A}(26)
=O\!\left(\frac{L_A^2}{AH_A}\right)
=o(1).
\tag{27}
\]

Therefore

\[
\boxed{E_{1,A}=o(D_A)}
\tag{28}
\]

uniformly.

For `(21)`, the prefix contribution satisfies

\[
\frac{u_2}{u_0}
=O\!\left(
\frac{t^2J(t)L_A^2}{H_A}
\right)
\le
O\!\left(\frac{L_A^3}{A^2H_A}\right)
=o(1).
\tag{29}
\]

The linear support-shift contribution divided by `D_A` is

\[
O\!\left(
\frac{d_A}{C_A}
\frac{tJ(t)}{H_A}
\right)
\le
O\!\left(\frac{L_A}{AH_A}\right)
=o(1),
\tag{30}
\]

and the quadratic shift contribution divided by `D_A` is

\[
O\!\left(
\frac{d_A^2}{C_A}
\frac{t^2J(t)^2}{H_A}
\right)
\le
O\!\left(\frac{L_A^2}{A^2H_A}\right)
=o(1),
\tag{31}
\]

because `(\log C)^2/C` is bounded for `C\ge2`. Hence

\[
\boxed{E_{2,A}=o(D_A)}
\tag{32}
\]

uniformly.

Equations `(13)`, `(19)`, `(28)`, and `(32)` isolate the asymmetry that leading-order AF-523 deliberately erased:

\[
\rho_0=\eta_A(1+D_A),
\qquad
\rho_1=\eta_A(1+o(D_A)),
\qquad
\rho_2=\eta_A(1+o(D_A)).
\tag{33}
\]

The retained prefix first appears at relative order `D_A` in the zeroth moment, while its effects on the first two moments are strictly smaller throughout the full boundary layer.

### 4. Curvature converts that mismatch into the first visible defect

For the prime reference source define

\[
r(t)=
\frac{(M_1^P(1+t))^2}
{M_0^P(1+t)M_2^P(1+t)}.
\]

AF-523 gives

\[
\sup_{0<t\le1/A}r(t)=O(L_A^{-1})=o(1).
\tag{34}
\]

The exact three-moment identity from AF-521 is

\[
\frac{\kappa_{Q_A}}{\kappa_P}
=
\frac{
\rho_2/\rho_0-r(t)(\rho_1/\rho_0)^2
}{1-r(t)}.
\tag{35}
\]

Using `(33)` and `D_A=o(1)` uniformly,

\[
\frac{\rho_2}{\rho_0}
=1-D_A+o(D_A),
\tag{36}
\]

and

\[
\left(\frac{\rho_1}{\rho_0}\right)^2
=1-2D_A+o(D_A).
\tag{37}
\]

Substitution into `(35)` gives

\[
\frac{\kappa_{Q_A}}{\kappa_P}
=
1-
\frac{1-2r(t)}{1-r(t)}D_A
+o(D_A).
\tag{38}
\]

Equation `(34)` makes the prefactor tend uniformly to one. Therefore

\[
\frac{\kappa_{Q_A}}{\kappa_P}
=1-D_A+o(D_A)
\tag{39}
\]

uniformly, proving `(5)`. Combining `(39)` with `(17)` gives `(7)` and the endpoint formula `(8)`.

## Fidelity and matched-control audit

The matched control is unchanged from AF-523: fixed primes below the cutoff, distinct ordinary composite targets above it, outward motion only, and unit coefficients. No extra marker has been added to the source and no arbitrary weight has been used to expose the transport.

The result sharpens the meaning of AF-523. At leading relative order the three moment participations share the common factor `\eta_A`, so curvature cancels it and the entire boundary profile looks prime-like. At the next order they do not remain equal: the retained prefix enters `\rho_0` at order `D_A` while its first- and second-moment effects are `o(D_A)`. Curvature is therefore sensitive precisely to the first **cross-moment participation mismatch**.

This is a limited recovery theorem. Within the rigid family `(2)`, the lower-order defect asymptotically identifies `C_A` through `(9)`. It does not prove that curvature identifies an arbitrary transported source, and it does not recover rational-prime provenance against unrestricted controls. Different controls could still be engineered to share the same first defect.

## Representation audit

The source object is the simple positive unit-weight Dirichlet support. The target representation is the scalar normalized curvature profile `\kappa_{Q_A}/\kappa_P`. The task is not full source reconstruction; it is recovery of the tail-transport provenance parameter inside the declared matched-control family.

AF-523 established non-injectivity at **leading asymptotic order** on this task: every admissible `C_A` satisfying `(1)` maps to the same limiting profile `1`. AF-525 refines the target representation by retaining one lower asymptotic order, not by adding an external marker. The resulting first defect separates transport scales because the quotient that killed the common factor `\eta_A` no longer kills the unequal correction in `\rho_0`.

The exact carrier `(4)` is therefore preferable to vague language about "information returning." What survives is a specific quotient coordinate: retained zeroth-moment participation relative to transported-tail normalization. Equations `(28)` and `(32)` show why that coordinate is the unique first-order mismatch among the first three moment layers in this regime.

## Prior art and novelty assessment

No novelty is claimed for the analytic-number-theory ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is the classical reference for the logarithmic singularity of `P(s)` at `s=1`.
- The local expansion `P(1+t)=\log(1/t)+\text{regular part}` and its differentiated moment expansions are standard. A recent explicit treatment is Artur Kawalec, **“On the series expansion of the prime zeta function about s=1 and its coefficients,”** arXiv:`2603.21535` (2026), which also records the higher logarithmic prime sums underlying `(22)`--`(23)`.
- Mertens' prime estimates and partial summation give the prefix asymptotics used in `(15)` and `(23)`.
- AF-521 supplies the exact three-moment curvature identity `(35)`; AF-523 supplies the same control family and the uniform leading-order blindness; AF-524 identifies the complementary mesoscopic crossover after the retained zeroth moment re-enters at leading order.

A focused search for truncated-prime-zeta boundary asymptotics, anchored tail dilations, and lower-order logarithmic-curvature defects located the standard prime-zeta and Mertens ingredients but no theorem matching `(5)`--`(7)` for this transported control family. The result is therefore stored as an exact internal refinement with `NO-NOVELTY-CLAIM`, not as a claim of new external mathematics.

## Boundaries and failure modes

1. **Rigid transport family.** Recovery of `C_A` in `(9)` is conditional on the uniform tail map `p\mapsto C_Ap`. A broader transport can introduce additional first-order moment defects.
2. **Relative reference observable.** The result uses `\kappa_{Q_A}/\kappa_P`; it does not say that an observer lacking the prime reference can infer `C_A` from `\kappa_{Q_A}` alone.
3. **First lower order only.** Controls with the same `D_A(t)` profile can remain indistinguishable at this order. Full provenance would require either higher asymptotic orders or another observable.
4. **Boundary-layer regime.** The hypothesis `C_AH_A/L_A\to0` is essential for `D_A=o(1)`. AF-524 describes the crossover once the anchor reaches leading order outside this regime/scale balance.
5. **No RH consequence.** The theorem concerns task-relative fidelity of a compression on a matched control class. It supplies no direct implication for zeta zeros or the Riemann hypothesis.

## Research consequence

AF-523's suggested escape "retain lower-order information" works in the strongest possible sense for this rigid family: the very first curvature correction is already nonzero, has a uniform profile, and asymptotically recovers the tail-dilation scale.

The next useful test is therefore not another expansion of the same uniform dilation. It is to broaden the outward transport class and ask whether the first defect remains a one-coordinate anchor law or whether multiple independent transport statistics enter. A positive universality theorem would identify a genuine compression invariant; a counterexample with the same `D_A` but different provenance would delimit exactly how much this lower-order recovery buys.