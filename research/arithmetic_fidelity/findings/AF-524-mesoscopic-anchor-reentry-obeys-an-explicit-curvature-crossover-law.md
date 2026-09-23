# AF-524 — Mesoscopic anchor re-entry obeys an explicit curvature crossover law

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `SOURCE-EXTINCTION` · `OUTWARD-TRANSPORT` · `MATCHED-COMPOSITE-CONTROL` · `MESOSCOPIC-CURVATURE` · `TRANSITION-LAW` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=(\log P(s))'',
\qquad s>1.
\]

For an integer cutoff `A\to\infty`, put

\[
L_A=\log A,
\qquad
H_A=\log L_A,
\]

and choose integers `C_A\ge2` such that

\[
C_A\to\infty,
\qquad
\frac{C_AH_A}{L_A}\to0.
\tag{1}
\]

As in AF-522--AF-523, retain every prime `p\le A` and move every prime `p>A` to the ordinary composite atom `C_Ap`:

\[
Q_A(s)
=
\sum_{p\le A}p^{-s}
+
C_A^{-s}\sum_{p>A}p^{-s}.
\tag{2}
\]

Fix any constant `\alpha>0` and observe this same transported source at

\[
t_A=\exp(-\alpha C_AH_A),
\qquad
s_A=1+t_A.
\tag{3}
\]

Then `(1)` implies

\[
t_A\to0,
\qquad
\frac{t_A}{1/A}\to\infty,
\tag{4}
\]

so these scales lie strictly beyond the whole boundary window `0<t\le1/A` covered by AF-523. Nevertheless the transformed Dirichlet source is still asymptotically extinct:

\[
\boxed{
C_A\frac{Q_A(s_A)}{P(s_A)}
\longrightarrow
1+\frac1\alpha,
}
\tag{5}
\]

and hence `Q_A(s_A)/P(s_A)\to0`.

The first two logarithmic moment participations remain tail-dominated:

\[
\boxed{
C_A\frac{M_j^{Q_A}(s_A)}{M_j^P(s_A)}
\longrightarrow1,
\qquad j=1,2.
}
\tag{6}
\]

But the retained prime prefix now contributes at the same order as the transported tail to the **zeroth** moment. Consequently the curvature has the explicit crossover law

\[
\boxed{
\frac{\kappa_{Q_A}(s_A)}{\kappa_P(s_A)}
\longrightarrow
\frac{\alpha}{1+\alpha}.
}
\tag{7}
\]

Thus the first leading-curvature recovery after AF-523 is controlled not by the geometric cutoff scale `t\asymp1/A`, but by the moment-balance parameter

\[
\frac{\log(1/t)}{C_A\log\log A}.
\tag{8}
\]

At finite nonzero values of `(8)`, the source remains extinct while curvature records the transported tail's share of the surviving zeroth-moment mass. Varying `\alpha` fills every limit in `(0,1)` for the **same asymptotic transport regime**; `\alpha\to\infty` approaches the curvature-blind limit `1` seen uniformly in AF-523.

## Derivation

### 1. The crossover scale is outside the boundary layer but still freezes the retained prefix

Write

\[
J_A=\log\frac1{t_A}=\alpha C_AH_A.
\tag{9}
\]

By `(1)`, `J_A=o(L_A)`, so

\[
\log\frac{t_A}{1/A}=L_A-J_A\to\infty,
\]

which proves the second part of `(4)`.

At the same time

\[
t_AL_A
=\exp(H_A-\alpha C_AH_A)
\to0,
\tag{10}
\]

because `C_A\to\infty`. Hence `p^{-t_A}=1+o(1)` uniformly for `p\le A`. If

\[
B_j(A,t)=\sum_{p\le A}(\log p)^jp^{-1-t},
\qquad j=0,1,2,
\tag{11}
\]

then Mertens' prime estimates and partial summation give

\[
B_0(A,t_A)\sim H_A,
\qquad
B_1(A,t_A)\sim L_A,
\qquad
B_2(A,t_A)\sim\frac12L_A^2.
\tag{12}
\]

The classical prime-zeta expansion at `s=1` and its first two derivatives give

\[
M_0^P(s_A)\sim J_A=\alpha C_AH_A,
\qquad
M_1^P(s_A)\sim t_A^{-1},
\qquad
M_2^P(s_A)\sim t_A^{-2}.
\tag{13}
\]

In particular,

\[
\frac{B_0(A,t_A)}{M_0^P(s_A)}
\sim\frac1{\alpha C_A}.
\tag{14}
\]

This is the new regime relative to AF-523: after multiplication by the tail factor `C_A^{-1}`, the retained zeroth moment is no longer negligible.

### 2. Zeroth-moment balance gives the extinction constant

Let

\[
d_A=\log C_A,
\qquad
\eta_A=C_A^{-1-t_A}.
\tag{15}
\]

Since `t_Ad_A\to0`,

\[
\eta_A\sim C_A^{-1}.
\tag{16}
\]

The zeroth moment satisfies exactly

\[
M_0^{Q_A}
=B_0+\eta_A(M_0^P-B_0).
\tag{17}
\]

Using `(14)`--`(16)`,

\[
\frac{M_0^{Q_A}}{M_0^P}
=\frac1{\alpha C_A}(1+o(1))
+\frac1{C_A}(1+o(1)),
\tag{18}
\]

which is `(5)`.

Equivalently, at this scale

\[
B_0(A,t_A)\sim H_A,
\qquad
\eta_AM_0^P(s_A)\sim\alpha H_A.
\tag{19}
\]

The retained prefix and transported tail therefore survive in zeroth-moment proportions `1:(\alpha)` even though their total participation relative to the original source still tends to zero.

### 3. The first two moments remain transported-tail dominated

Transport by `C_A` shifts each moved logarithmic coordinate by `d_A`. Therefore

\[
M_1^{Q_A}
=B_1+\eta_A\bigl[(M_1^P-B_1)+d_A(M_0^P-B_0)\bigr],
\tag{20}
\]

and

\[
\begin{aligned}
M_2^{Q_A}
={}&B_2+\eta_A\bigl[(M_2^P-B_2)
+2d_A(M_1^P-B_1)\\
&\hspace{35mm}+d_A^2(M_0^P-B_0)\bigr].
\end{aligned}
\tag{21}
\]

The prefix is negligible relative to the transported first moment because

\[
\frac{B_1/M_1^P}{\eta_A}
=O(C_At_AL_A)
=o(1).
\tag{22}
\]

Indeed `t_A=L_A^{-\alpha C_A}`, so the power `L_A^{-\alpha C_A}` beats the factors `C_A L_A`. Likewise

\[
\frac{B_2/M_2^P}{\eta_A}
=O(C_At_A^2L_A^2)
=o(1).
\tag{23}
\]

The support-shift terms are also lower order:

\[
\frac{d_AM_0^P}{M_1^P}
=O(d_At_AJ_A)=o(1),
\tag{24}
\]

\[
\frac{d_AM_1^P}{M_2^P}=O(d_At_A)=o(1),
\qquad
\frac{d_A^2M_0^P}{M_2^P}
=O(d_A^2t_A^2J_A)=o(1).
\tag{25}
\]

Substitution into `(20)`--`(21)` gives

\[
\frac{M_1^{Q_A}}{M_1^P}
=\eta_A(1+o(1)),
\qquad
\frac{M_2^{Q_A}}{M_2^P}
=\eta_A(1+o(1)),
\tag{26}
\]

which proves `(6)`.

### 4. Curvature reads the zeroth-moment mixture

Set

\[
\rho_j(A)=\frac{M_j^{Q_A}(s_A)}{M_j^P(s_A)},
\qquad j=0,1,2.
\tag{27}
\]

Equations `(5)`--`(6)` yield

\[
C_A\rho_0\to1+\frac1\alpha,
\qquad
C_A\rho_1\to1,
\qquad
C_A\rho_2\to1.
\tag{28}
\]

For the prime source,

\[
r_A:=
\frac{(M_1^P(s_A))^2}
{M_0^P(s_A)M_2^P(s_A)}
\sim\frac1{J_A}
\to0.
\tag{29}
\]

The exact three-moment identity used in AF-521--AF-523 is

\[
\frac{\kappa_{Q_A}(s_A)}{\kappa_P(s_A)}
=
\frac{
\rho_2/\rho_0-r_A(\rho_1/\rho_0)^2
}{1-r_A}.
\tag{30}
\]

By `(28)`,

\[
\frac{\rho_2}{\rho_0}\to\frac{\alpha}{1+\alpha},
\qquad
\frac{\rho_1}{\rho_0}\to\frac{\alpha}{1+\alpha},
\tag{31}
\]

while `(29)` kills the squared-mean correction. Equation `(30)` therefore gives `(7)`.

The crossover is structurally simple: the first two moments still see only the dilated tail, but the zeroth moment sees both the fixed anchor and the tail. Leading curvature is therefore exactly the tail fraction of the zeroth-moment mixture.

## Fidelity and matched-control audit

The control class is the same rigid one as AF-523:

- every prime `p\le A` is retained;
- every prime `p>A` moves strictly outward to the distinct ordinary composite `C_Ap`;
- every coefficient stays equal to one;
- no deletion, collision, signed weight, noninteger norm, or inward transport is used.

Equation `(7)` shows that leaving the AF-523 boundary layer **does** restore leading-order discrimination, but only when the observation reaches a scale where the retained provenance-bearing anchor enters a visible moment layer at the same order as the transported tail. The discrimination is quantitative rather than all-or-nothing: the curvature limit is the moment-participation ratio `\alpha/(1+\alpha)`.

This also sharpens the failure mechanism. The decisive variable is not geometric distance from the cutoff by itself. The relevant threshold is whether

\[
\log(1/t)
\]

is large or small compared with `C_AH_A`, because that comparison determines whether the prefix contribution `H_A` is negligible, comparable to, or dominant over the transported-tail zeroth moment `C_A^{-1}\log(1/t)`.

## Representation audit

AF-523 established that the complete leading relative curvature profile is blind throughout `0<t\le1/A`. AF-524 changes only the observation scale and keeps the source transformation fixed. The resulting transition therefore isolates the missing representation feature: **cross-moment participation mismatch**.

When all visible moments inherit the same tail factor, curvature cancels that factor. At `(3)`, the zeroth moment stops inheriting it while the first two moments still do. Curvature becomes informative precisely because its numerator and denominator no longer descend through the same asymptotic gauge.

This is a concrete instance of the line's general fidelity question: a compression regains discriminating power when an otherwise forgotten marked component re-enters one of the layers compared by the observable, even though the underlying source remains globally negligible relative to the reference.

## Prior art and novelty assessment

No novelty is claimed for the analytic ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is the classical source for the prime-zeta singularity at `s=1`; the moment scales in `(13)` are standard consequences of that expansion and differentiation.
- Mertens' prime estimates, together with partial summation, give the retained-prefix asymptotics in `(12)`.
- AF-521 gives the exact three-moment curvature identity `(30)`.
- AF-522 gives the analogous continuum of curvature limits when the observation scale is fixed at `t=1/A` and the transport factor itself is tuned.
- AF-523 proves uniform curvature blindness for the present transport regime throughout `0<t\le1/A`.

A focused literature search for truncated prime-zeta tail dilation, cutoff-dependent Dirichlet transport, Mellin/dilation crossover laws, and logarithmic-curvature variants recovered the standard prime-zeta, Mertens, Mellin, and log-partition ingredients but no direct theorem matching `(5)`--`(8)`. The present result is therefore stored as an exact derived crossover law inside the Arithmetic Fidelity control family with `NO-NOVELTY-CLAIM`, not as a claim of external theorem novelty.

## Boundaries and failure modes

1. **Fixed positive crossover parameter.** The theorem is stated for fixed `\alpha>0`. Taking `\alpha` itself to zero or infinity with `A` requires checking the corresponding uniform error terms; AF-523 already supplies the relevant `\alpha=\infty` boundary regime uniformly on `t\le1/A`.
2. **Leading relative curvature only.** Lower-order curvature terms may discriminate earlier or encode additional transport information.
3. **The transport family still changes with `A`.** This is an asymptotic conditioning/classification result, not an exact quotient theorem for one fixed source.
4. **Positive simple sources.** Signed or complex coefficients can introduce cancellations absent from this moment argument.
5. **The retained-prefix geometry matters.** A different anchor size or a nonuniform transport changes the balance scale by changing the zeroth-moment competition.
6. **No RH consequence follows.** The result identifies when one scalar compression regains provenance sensitivity; it does not establish a prime-specific operator, sign mechanism, or implication for the zero set of `\zeta`.

## Research consequence

AF-523 left the first live escape explicitly outside its boundary layer: inspect scales `t\gg1/A` where the retained prefix can re-enter. AF-524 resolves the leading-order version of that question for the same rigid controls. The first nontrivial transition occurs when

\[
\log(1/t)\asymp C_A\log\log A,
\]

not when `t\asymp1/A`. At that scale source extinction persists, but leading curvature recovers a continuum of discrimination because the provenance-bearing prefix contributes to the zeroth moment while remaining negligible in the first two.

The next unresolved question is therefore lower-order and structural rather than merely another scale search: determine whether the subleading curvature defect inside the AF-523 blind region carries a stable transport/provenance invariant, or whether a richer observable is required to expose participation mismatch before the zeroth-moment crossover.