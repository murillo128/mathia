# PF-315 — sequential physical-band elimination factorizes the full angle defect

**Status:** `EXACT-DERIVED + CLASSICAL-SCHUR-QUOTIENT + PHYSICAL-ANGLE-FACTORIZATION + POSITIVE/ROUTE-NARROWING`.

PF-281 identifies the actual physical target as the energy-normalized `P/H` cross form. PF-311 then refines the physical-low side into cuff constants `C` and retained nonconstant physical-low modes `L`, shorts `L`, and isolates the conditional constant/high angle

\[
T_H=S_L^{-1/2}E_{LH}R_H^{-1/2}.
\]

PF-312--PF-314 analyze what can and cannot be amplified around that conditional block. One representation question remained implicit: **how does this post-low angle sit inside the original PF-281 physical `P/H` angle?** The answer is exact and removes an arbitrary source map from this stage of the problem.

On every finite canonical section, let the PF-311 positive boundary form be

\[
\mathcal A=
\begin{pmatrix}
H&B_L&B_H\\
B_L^*&J_{LL}&J_{LH}\\
B_H^*&J_{HL}&J_{HH}
\end{pmatrix}>0
\tag{1}
\]

on `C\oplus L\oplus H`, where the full physical-low space is `P=C\oplus L`. Put

\[
A_P=
\begin{pmatrix}
H&B_L\\
B_L^*&J_{LL}
\end{pmatrix},
\qquad
Q=\binom{B_H}{J_{LH}},
\tag{2}
\]

and define the full PF-281 angle

\[
T_{P/H}:=A_P^{-1/2}QJ_{HH}^{-1/2}.
\tag{3}
\]

After shorting `L`, keep PF-311's blocks

\[
S_L=H-B_LJ_{LL}^{-1}B_L^*,
\tag{4}
\]

\[
E_{LH}=B_H-B_LJ_{LL}^{-1}J_{LH},
\tag{5}
\]

\[
R_H=J_{HH}-J_{HL}J_{LL}^{-1}J_{LH},
\tag{6}
\]

and introduce the **direct low/high angle**

\[
Z_{LH}:=J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}
\tag{7}
\]

and the residual source map

\[
V_H:=R_H^{1/2}J_{HH}^{-1/2}.
\tag{8}
\]

Then there is a unitary change of coordinates `U_P` on the physical-low energy space such that

\[
\boxed{
U_PT_{P/H}
=
\binom{T_HV_H}{Z_{LH}}.
}
\tag{9}
\]

Moreover

\[
\boxed{
V_H^*V_H=I-Z_{LH}^*Z_{LH},
}
\tag{10}
\]

and therefore the full physical angle has the exact nested-defect identity

\[
\boxed{
I-T_{P/H}^*T_{P/H}
=
V_H^*(I-T_H^*T_H)V_H.
}
\tag{11}
\]

Equivalently, for every physical-high energy coordinate `x`,

\[
\boxed{
\|T_{P/H}x\|^2
=
\|Z_{LH}x\|^2+
\|T_HV_Hx\|^2,
}
\tag{12}
\]

and

\[
\boxed{
\|x\|^2-\|T_{P/H}x\|^2
=
\|(I-T_H^*T_H)^{1/2}V_Hx\|^2.
}
\tag{13}
\]

The representation consequence is important. The actual physical-high input does **not** feed the post-low angle `T_H` through an arbitrary source map. It reaches that conditional channel through the canonical residual map `V_H`, whose Gram is exactly the defect of the direct `L/H` angle. If `V_H` suppresses a direction strongly, then `Z_{LH}` is already nearly isometric on that direction and the same direction is already large in the full physical `P/H` angle. Conversely, if the direct `L/H` angle has a uniform gap from one, then `V_H` is uniformly invertible and cannot hide bad singular-value behavior of `T_H`.

Thus the current physical-angle problem has a sharp dichotomy. Either the direct retained-low/high channel `Z_{LH}` already carries the obstruction, or the conditional post-low channel must be estimated through `T_HV_H`; there is no third operator-norm source-amplification mechanism between them. This does not prove compactness or weak trace class, because singular-value counting for both components remains open.

## Claim

Fix a finite PF-205/PF-311 boundary-response section with decomposition `C\oplus L\oplus H` and matrix (1). Let `A_P,Q,T_{P/H},S_L,E_{LH},R_H,T_H,Z_{LH},V_H` be defined by (2)--(8), with

\[
T_H=S_L^{-1/2}E_{LH}R_H^{-1/2}.
\tag{14}
\]

Then:

1. `T_{P/H}`, `T_H`, and `Z_{LH}` are contractions, strictly so on every finite strictly positive section;
2. there is a unitary `U_P:C\oplus L\to C\oplus L` in the corresponding energy coordinates such that (9) holds;
3. `V_H` is a contraction satisfying (10);
4. the full defect satisfies (11), hence the norm identities (12)--(13);
5. `Z_{LH}` and `T_HV_H` are literal orthogonal-row compressions of `T_{P/H}` after the unitary `U_P`, so for every singular index `j`,
   \[
   \boxed{
   s_j(Z_{LH})\le s_j(T_{P/H}),
   \qquad
   s_j(T_HV_H)\le s_j(T_{P/H}).
   }
   \tag{15}
   \]
6. if for some `\delta>0`
   \[
   Z_{LH}^*Z_{LH}\le(1-\delta^2)I,
   \tag{16}
   \]
   then
   \[
   V_H^*V_H\ge\delta^2I
   \tag{17}
   \]
   and hence
   \[
   \boxed{
   \delta\,s_j(T_H)
   \le s_j(T_HV_H)
   \le s_j(T_H)
   \qquad(j\ge1).
   }
   \tag{18}
   \]
   In particular, under a uniform direct-channel gap, compactness or membership in any two-sided symmetric operator ideal is equivalent for `T_H` and `T_HV_H` up to fixed constants;
7. whenever the finite sections converge to bounded operators in a common limiting realization, one has the exact compactness reduction
   \[
   \boxed{
   T_{P/H}\text{ compact}
   \iff
   Z_{LH}\text{ compact and }T_HV_H\text{ compact}.
   }
   \tag{19}
   \]
   More generally, the same two components are the only ones that need to be controlled in a two-sided symmetric ideal, with the usual finite-block-column quasi-triangle estimate.

A particularly cheap noncompactness test follows from (12): if a normalized weakly-null high-sector sequence `x_n` satisfies

\[
\|Z_{LH}x_n\|\longrightarrow1,
\tag{20}
\]

then automatically

\[
\|T_{P/H}x_n\|\longrightarrow1,
\tag{21}
\]

so the full physical angle cannot be compact. Thus suppression of the conditional channel by `V_H` cannot rescue a direction on which the direct low/high channel itself saturates.

## 1. Block elimination identifies the actual residual input map

The physical-low diagonal block has the exact block-LDU factorization

\[
A_P=L_P
\begin{pmatrix}
S_L&0\\
0&J_{LL}
\end{pmatrix}
L_P^*,
\qquad
L_P=
\begin{pmatrix}
I&B_LJ_{LL}^{-1}\\
0&I
\end{pmatrix}.
\tag{22}
\]

The same triangular factor transforms the physical `P/H` cross block:

\[
Q
=L_P\binom{E_{LH}}{J_{LH}}.
\tag{23}
\]

Let

\[
D_P:=\operatorname{diag}(S_L,J_{LL})
\tag{24}
\]

and define

\[
U_P:=D_P^{1/2}L_P^*A_P^{-1/2}.
\tag{25}
\]

Using (22),

\[
U_P^*U_P
=A_P^{-1/2}L_PD_PL_P^*A_P^{-1/2}
=I,
\tag{26}
\]

so `U_P` is unitary in the finite section. Equations (3), (23), and (25) give

\[
\begin{aligned}
U_PT_{P/H}
&=D_P^{-1/2}
\binom{E_{LH}}{J_{LH}}J_{HH}^{-1/2}\\
&=
\binom{
S_L^{-1/2}E_{LH}J_{HH}^{-1/2}
}{
J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}
}.
\end{aligned}
\tag{27}

By definition of `T_H` and `V_H`,

\[
S_L^{-1/2}E_{LH}J_{HH}^{-1/2}
=T_HR_H^{1/2}J_{HH}^{-1/2}
=T_HV_H,
\tag{28}
\]

while the lower block in (27) is exactly `Z_{LH}`. This proves (9).

This calculation is the representation step missing after PF-314. No additional source is chosen. `V_H` is forced by the same sequential elimination that defines PF-311's conditional angle.

## 2. The source Gram is exactly the direct-channel defect

From (6)--(8),

\[
\begin{aligned}
V_H^*V_H
&=J_{HH}^{-1/2}R_HJ_{HH}^{-1/2}\\
&=I-
J_{HH}^{-1/2}J_{HL}J_{LL}^{-1}J_{LH}J_{HH}^{-1/2}\\
&=I-Z_{LH}^*Z_{LH}.
\end{aligned}
\tag{29}

This proves (10). Substituting (9) into `T_{P/H}^*T_{P/H}` gives

\[
T_{P/H}^*T_{P/H}
=V_H^*T_H^*T_HV_H+Z_{LH}^*Z_{LH}.
\tag{30}
\]

Using (29),

\[
\begin{aligned}
I-T_{P/H}^*T_{P/H}
&=V_H^*V_H-V_H^*T_H^*T_HV_H\\
&=V_H^*(I-T_H^*T_H)V_H,
\end{aligned}
\tag{31}
\]

which is (11). Equations (12)--(13) are its quadratic-form version.

There is a useful interpretation in the language of PF-313--PF-314. `V_H` is already a defect-scale residual source map, but its defect is the **preceding direct low/high channel** `Z_{LH}`, not an independently postulated weight. Sequential shorting therefore determines both the conditional angle and the exact source through which the full physical high input reaches it.

## 3. A uniform direct-channel gap makes the conditional angle visible

Equation (16) and (10) give

\[
\delta^2I\le V_H^*V_H\le I.
\tag{32}
\]

Thus `V_H` is invertible onto its range with

\[
\|V_H\|\le1,
\qquad
\|V_H^{-1}\|\le\delta^{-1}.
\tag{33}
\]

The ideal inequality `s_j(AB)\le\|B\|s_j(A)` gives the upper bound in (18), while

\[
T_H=(T_HV_H)V_H^{-1}
\]

gives the lower bound. Hence under a uniform direct `L/H` gap the post-low angle cannot be made compact, weak-trace, or small merely by saying that its physical source is restricted: the actual source map is uniformly reversible in energy coordinates.

If no such gap exists, the failure is itself physical information. A sequence on which `V_H` becomes small has, by (10), a correspondingly large direct `L/H` correlation. Equation (12) shows that this channel already contributes to the full PF-281 angle before the conditional constant/high conversion is considered.

This replaces an ambiguous choice between “source avoidance” and “angle saturation” by an exact two-channel bookkeeping identity.

## 4. Consequence for compactness and weak-trace work

After the unitary `U_P`, the full physical angle is the block column `(T_HV_H,Z_{LH})^T`. Therefore each component is a compression of the full angle, giving (15). Conversely a block column of two compact operators is compact, proving (19) whenever the limiting operators are defined in a common realization.

For the weak-trace target, the same structure gives the correct objects to count. One may estimate `Z_{LH}` and `T_HV_H` separately and then use the finite block-column quasi-triangle inequality in `\mathcal S_{1,\infty}`. Estimating `T_H` alone is stronger than necessary when `Z_{LH}` has no uniform gap, because `V_H` may suppress some conditional directions. But that suppression is never free: the same directions are then close to saturation in `Z_{LH}`.

Thus the next source-weighted or counting argument should be attached to the actual factor `T_HV_H` or to `Z_{LH}`, not to a free-standing Green/source model. This is exactly the representation discipline demanded by the accepted source-weighted-return clue.

## 5. Prior art and novelty audit

The matrix algebra is classical. The factorization (22) is the standard block-LDU/Schur-complement factorization, and the compatibility of sequential Schur complements is the Crabtree--Haynsworth quotient formula. F. Zhang, *A Matrix Identity on the Schur Complement*, Linear and Multilinear Algebra **52** (2004), 367--373, DOI `10.1080/03081080310001645172`, gives a direct modern treatment of this quotient identity. T. Ando, *Generalized Schur complements*, Linear Algebra and its Applications **27** (1979), 173--186, DOI `10.1016/0024-3795(79)90040-5`, proves the corresponding commutativity/quotient rules in a generalized shorted-operator framework.

The identities (9)--(13) are therefore not claimed as new matrix theory. They are a normalized rewriting of that classical sequential elimination, closely analogous to conditioning/partial-correlation factorizations for positive covariance matrices. The project-specific content is the placement of the quotient identity at the exact PF-281/PF-311 physical split: it identifies the actual source map into the post-low angle and shows that any attenuation there is paid for by the direct physical `L/H` channel. A structure-directed literature search found the classical Schur/conditioning framework but no prime-flute-specific result establishing this placement or its consequence for the current weak-trace route.

## 6. Boundaries and falsification tests

1. **Finite sections are exact.** Equations (9)--(13) hold for every finite strictly positive canonical section. Passing to the infinite boundary form requires the same closed-form and convergence controls already required by PF-281/PF-311.
2. **`Z_{LH}` is energy normalized.** It is not the raw block `J_{LH}`. Any physical conclusion must retain both diagonal energies in (7).
3. **`V_H` is the canonical residual input only for this sequential split.** A later geometric coefficient map or target reconstruction can introduce additional factors; the theorem does not declare all source/reassembly maps harmless.
4. **No uniform gap is asserted.** Equation (18) is conditional on (16). If the gap fails, the theorem redirects attention to the direct physical channel `Z_{LH}` rather than assuming a hidden source loss.
5. **No weak-trace theorem is proved.** The exact factorization changes what must be counted, but it supplies no singular-value asymptotic for `Z_{LH}` or `T_HV_H`.
6. **No cancellation claim.** Signed target reassembly can still alter a later observable even when the physical angle is large.
7. **No arithmetic discrimination.** The algebra is universal. Prime-flute content lies in the canonical physical-band decomposition and in whatever tail estimates are eventually proved for the two actual components.

A direct numerical audit is immediate: generate any positive three-block matrix in the PF-311 ordering, compute both sides of (9) after the unitary (25), and verify (10)--(13). The decisive project audit is geometric/operator-theoretic: estimate `Z_{LH}` and `T_HV_H` on the canonical tail and determine which component carries the heavy PF-287 range.

## Consequence for the research line

PF-314 left the physical source representation as the immediate gate before another Green estimate. PF-315 resolves one substantial part of that representation **for the actual PF-281 physical angle**: after the nonconstant physical-low variables are isolated, the physical-high source reaching the conditional PF-311 angle is canonically `V_H=R_H^{1/2}J_{HH}^{-1/2}`, and its Gram is exactly the defect of the direct `L/H` angle.

The next investigation should therefore branch on the real two-channel dichotomy. First test the direct energy-normalized `Z_{LH}` on the canonical tail. If it has a heavy/noncompact source-reached range, the full physical obstruction is already present there. If it has a uniform gap, `V_H` is uniformly invertible and the singular-value problem transfers back to `T_H` with no hidden source escape. If it is neither uniformly gapped nor itself decisively heavy, estimate the coupled pair `Z_{LH}` and `T_HV_H` directly; a free-standing diagonal Green norm is not the right next observable.