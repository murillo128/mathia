# PF-173 — matched central-cut recoupling is trace-summable over the complete short-core family

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + DECISIVE-NEGATIVE/METHOD-BOUNDARY`. PF-172 showed that restoring transmission across one fixed central cut is trace class but has an absolute order-one zero-mode cost that does not shrink with the core length. The missing relative calculation can be done exactly. After matching two collars with core lengths `L` and `L'=e^tL`, the common zero mode cancels, and the **difference of their recoupling corrections is trace class with a quantitative bound `O(|t|L^2)`**. Combined with PF-109 and PF-138, these relative recoupling corrections are trace-summable over the complete tail family of Margulis-short prime-flute cores. Thus neither pinching, short-core multiplicity, nor the central-cut transmission mode can create the remaining global Schatten obstruction. Any failure of the full prime/shift comparison must be body-loaded or genuinely nonlocal: outer collar/body transmission, global Dirichlet-to-Neumann response, localization overlap, or repeated head-tail interaction.

## Claim

Fix `R>0` and use the exact standard collar

\[
C_{L,R}=(-R,R)\times\mathbb S^1,
\qquad
 g_L=dr^2+L^2\cosh^2r\,d\theta^2,
\tag{1}
\]

with Dirichlet conditions at `r=+-R`. Assume the standard collar width is larger than `R`. Let `Delta_L` be the uncut positive Laplacian, and let

\[
\Delta_L^{\rm cut}
=
\Delta_{L,(-R,0)}^D\oplus\Delta_{L,(0,R)}^D
\tag{2}
\]

be obtained by imposing an additional Dirichlet condition at `r=0`. As in PF-172, put

\[
G_L
:=
(\Delta_L+1)^{-1}
-
(\Delta_L^{\rm cut}+1)^{-1}.
\tag{3}
\]

Use the constant-density unitary to place all collars on the common Hilbert space

\[
\mathcal H_R
=L^2((-R,R)\times\mathbb S^1,\cosh r\,dr\,d\theta).
\tag{4}
\]

Let

\[
L'=e^tL,
\qquad |t|\le t_0,
\tag{5}
\]

and assume both collars contain the fixed central slab. Define the **relative recoupling difference**

\[
T_{L,L'}^{(R)}:=G_{L'}-G_L.
\tag{6}
\]

Then

\[
\boxed{
T_{L,L'}^{(R)}\in\mathcal S_1,
\qquad
\|T_{L,L'}^{(R)}\|_{\mathcal S_1}
\le C_{R,t_0}|t|L^2.
}
\tag{7}
\]

Moreover, the angular zero-mode block vanishes exactly:

\[
\boxed{P_0T_{L,L'}^{(R)}P_0=0.}
\tag{8}
\]

This is strictly stronger than estimating the two absolute recoupling operators separately. PF-172 gives

\[
\|G_L\|_1\ge c_R>0
\tag{9}
\]

uniformly as `L->0`, while (7) tends to zero whenever the **relative** logarithmic length defect tends to zero with `L` bounded.

For the exact prime flute and its all-composite shift clone, let `S` be the complete tail family of Margulis-short canonical cores from PF-138. For `eta in S`, let `L_eta` and `L_{eta,+}` be the matched prime/shift lengths, and set

\[
t_\eta=\log(L_{\eta,+}/L_\eta).
\tag{10}
\]

After discarding a finite head, choose one fixed

\[
0<R<\operatorname{arsinh}1
\tag{11}
\]

so that every prime and matched shift short collar contains the fixed central slab. Then

\[
\boxed{
\bigoplus_{\eta\in\mathcal S}
T_{L_\eta,L_{\eta,+}}^{(R)}
\in\mathcal S_1,
}
\tag{12}
\]

and the trace norm of the tail tends to zero as the left prime label tends to infinity.

Equation (12) is an orthogonal **central-collar model statement**. It does not identify the outer Dirichlet boundaries with the actual full-surface collar/body interfaces and does not prove that the full uncut prime/shift first relative resolvent is trace class. PF-112 forbids that latter conclusion for the genuinely non-isometric two-dimensional pair.

## 1. Fourier and parity reduction isolate one scalar boundary channel

On the `m`th angular Fourier mode, write

\[
q=\frac{2\pi|m|}{L},
\qquad
W(r)=\operatorname{sech}^2r.
\tag{13}
\]

The radial operator on `(-R,R)` is

\[
H_q
=
H_0+q^2W,
\qquad
H_0
=-\frac1{\cosh r}\partial_r(\cosh r\,\partial_r).
\tag{14}
\]

The potential and the outer boundary conditions are reflection symmetric. On the half interval `(0,R)`, let `K_q^N` denote (14) with Neumann condition at `0` and Dirichlet at `R`, and let `K_q^D` use Dirichlet conditions at both ends. Set

\[
R_N(q)=(K_q^N+1)^{-1},
\qquad
R_D(q)=(K_q^D+1)^{-1},
\qquad
D(q)=R_N(q)-R_D(q).
\tag{15}
\]

The uncut full collar splits into an even channel with the `N-D` half-interval problem and an odd channel with the `D-D` problem. The centrally cut collar gives two copies of the `D-D` problem. After the symmetric/antisymmetric identification, the `m`th block of `G_L` is therefore unitarily equivalent to

\[
D(q)\oplus0.
\tag{16}
\]

The operator `D(q)` is positive. It also has rank at most one: for any forcing term, the difference between the Neumann and Dirichlet resolvent solutions solves the homogeneous second-order equation and vanishes at `R`; that solution space is one-dimensional. Hence

\[
\|D(q)\|_1=\|D(q)\|.
\tag{17}
\]

For `m=0`, `q=0` independently of `L`. Equation (16) immediately gives the exact cancellation (8). This is the same zero mode that produced PF-172's non-decaying **absolute** recoupling cost; subtraction removes it before any trace norm is taken.

## 2. A nonzero Fourier mode has a relative trace bound `O(|t|q^{-2})`

Put

\[
c_R=\operatorname{sech}^2R>0.
\tag{18}
\]

For either boundary condition `B in {N,D}` and `q>0`,

\[
K_q^B+1\ge 1+c_Rq^2,
\tag{19}
\]

so

\[
\|R_B(q)\|
\le(1+c_Rq^2)^{-1}.
\tag{20}
\]

Using positivity, rank one, and (20),

\[
\|D(q)\|_1
\le
\|R_N(q)\|+\|R_D(q)\|
\le C_Rq^{-2}
\tag{21}
\]

through the nonzero collar modes; the harmless small-`q` regime can be absorbed into the constant on any fixed admitted collar range.

For `L'=e^tL`, the corresponding Fourier parameter is

\[
q'=e^{-t}q.
\tag{22}
\]

Let

\[
V=(q'^2-q^2)W.
\tag{23}
\]

For `|t|<=t_0`,

\[
\|V\|_\infty
\le C_{t_0}|t|q^2,
\qquad
q'\asymp_{t_0}q.
\tag{24}
\]

The two resolvent identities give

\[
R_B(q')-R_B(q)
=-R_B(q')VR_B(q).
\tag{25}
\]

Subtracting the `N` and `D` versions **before taking a trace norm** yields the useful factorization

\[
\boxed{
D(q')-D(q)
=-D(q')VR_N(q)
-R_D(q')VD(q).
}
\tag{26}
\]

Each term in (26) contains a rank-one trace-class factor. Equations (20)--(24) therefore imply

\[
\begin{aligned}
\|D(q')-D(q)\|_1
&\le
\|D(q')\|_1\|V\|\|R_N(q)\|
+
\|R_D(q')\|\|V\|\|D(q)\|_1\\
&\le
C_{R,t_0}|t|q^{-2}.
\end{aligned}
\tag{27}
\]

This is the cancellation PF-172 left open in its exact local model. Separate bounds on `D(q')` and `D(q)` would retain their absolute trace budgets; the algebraic subtraction (26) exposes the small source/clone parameter before the ideal norm.

## 3. Summing the Fourier modes crosses the trace endpoint

By (8), only `m!=0` contributes. For those modes,

\[
q^{-2}
=\frac{L^2}{4\pi^2m^2}.
\tag{28}
\]

The Fourier blocks are orthogonal, so (27) gives

\[
\begin{aligned}
\|T_{L,L'}^{(R)}\|_1
&=
\sum_{m\ne0}
\|D(q_m')-D(q_m)\|_1\\
&\le
C_{R,t_0}|t|L^2
\sum_{m\ne0}\frac1{m^2}\\
&\le C'_{R,t_0}|t|L^2.
\end{aligned}
\tag{29}
\]

This proves (7).

There is no conflict with PF-112 or PF-127. The **metric** first relative resolvent

\[
(\Delta_{L'}+1)^{-1}-(\Delta_L+1)^{-1}
\tag{30}
\]

has a nonzero two-dimensional interior principal symbol and is not trace class when `L'!=L`. In (6), that interior contribution is subtracted once more through the corresponding centrally cut relative resolvent. What remains is a boundary-transmission difference with only one scalar channel per Fourier mode, and its source/clone zero mode cancels exactly.

## 4. The complete Margulis-short central-cut family is trace-summable

PF-138 proves that every sufficiently far Margulis-short closed geodesic is a canonical consecutive-block separator. If its left exterior prime label is `P`, the number of such short separators obeys

\[
N(P)=O(P^\theta),
\qquad
\theta=0.525.
\tag{31}
\]

PF-109 gives uniformly on the same family

\[
|t_\eta|
=
\left|
\log\frac{L_{\eta,+}}{L_\eta}
\right|
=O(P^{-3}).
\tag{32}
\]

Every core in the family satisfies

\[
L_\eta\le\mu_*=2\operatorname{arsinh}1.
\tag{33}
\]

The shift length is asymptotically multiplicatively equal, so after removing finitely many head terms both surfaces admit the same fixed central radius (11). Applying (29) and then (31)--(33),

\[
\begin{aligned}
\sum_{\eta\in\mathcal S}
\|T_\eta^{(R)}\|_1
&\le
C_R
\sum_{P\ {\rm prime}}
N(P)P^{-3}\\
&\le
C_R'
\sum_{P\ {\rm prime}}
P^{\theta-3}\\
&<\infty.
\end{aligned}
\tag{34}
\]

because `theta-3=-2.475<-1`. The collars are mutually disjoint in the Margulis-short family, so their model Hilbert spaces form an orthogonal direct sum. Equation (34) proves (12), and the same convergent majorant makes the trace norm of the omitted tail tend to zero.

This is stronger than the `S_r`, `r>1`, conclusion required for the local metric blocks in PF-171: **once source and clone central-cut transmission are subtracted first, this particular interface family is already `S_1`.**

## 5. Prior art and novelty audit

No general boundary-calculus novelty is claimed. PF-172 already audits the classical fact that finite smooth boundary-condition changes in dimension two have trace-class first-resolvent differences, with Behrndt--Langer--Lotoreichik and Grubb as primary anchors. The half-interval rank-one statement used here is the elementary one-dimensional version of the same Krein-resolvent principle and is also proved directly by the one-dimensional range argument above.

Likewise, the resolvent identity, Fourier decomposition, rank-one ideal estimate, and direct-sum trace criterion are standard. A directed check of the mixed-boundary/Krein literature finds the expected general boundary-condition singular-value theory, not a theorem whose content is the matched prime/shift estimate (29) or the complete short-core composition (34).

The Mathia-specific content is therefore the exact conjunction

\[
\boxed{
\text{PF-172 zero-mode identification}
+
\text{source/clone subtraction before norms}
+
\text{PF-109 }O(P^{-3})\text{ matching}
+
\text{PF-138 complete short-core count}
\Longrightarrow
\text{central-cut relative recoupling is globally }\mathcal S_1.
}
\tag{35}
\]

This is a method boundary for the prime-flute operator program, not a new general theorem about elliptic boundary problems.

## 6. Adversarial controls and falsification core

A later review can audit the result through the following finite chain.

1. Check the parity decomposition of the exact symmetric collar: the uncut even sector is `N-D`, the uncut odd sector is `D-D`, while the centrally cut problem gives two `D-D` sectors.
2. Verify that the difference between the half-interval `N-D` and `D-D` resolvents has one-dimensional range and is positive, so its trace norm equals its operator norm.
3. Use `sech^2r>=sech^2R` to obtain the nonzero-mode resolvent bound (20) and then (21).
4. Verify the exact resolvent subtraction (26); this is where the relative source/clone cancellation enters.
5. Check `|q'^2-q^2|<=C|t|q^2` and derive (27).
6. Verify that the `m=0` recoupling operator is independent of `L`, hence cancels exactly in (6).
7. Sum `m^-2` to obtain (29).
8. Apply PF-109 only at the prime/shift specialization and PF-138 only for completeness/counting of the short-core family.
9. Keep the outer Dirichlet boundaries in the statement. Do not replace (12) by a claim about the actual full-surface Dirichlet-to-Neumann or scattering operator.
10. Do not infer global first-resolvent trace class: PF-112 remains the exact local obstruction for the uncut non-isometric metric pair.

A refutation must break the parity/rank-one reduction, the algebraic identity (26), the quantitative mode estimate, PF-109's uniform logarithmic matching, or PF-138's complete short-core count. Failure of a later body-loaded assembly theorem would not refute PF-173; it would locate the remaining global obstruction outside the central-cut model.

## Research consequence

The accepted sharp-Schatten question is now narrower than after PF-172. PF-171 already shows that the complete **central metric** short-collar family lies in every `S_r`, `r>1`. PF-173 now shows that if those collars are additionally cut through their shrinking cores, the complete **relative recoupling correction** is even trace class after prime/shift cancellation.

Therefore the remaining uncut operator problem cannot be blamed on an accumulation of common central transmission zero modes or on the number of short collars. The live calculation is the body-loaded one: place prime and clone in one common outer interface calculus, retain the actual complementary-body Dirichlet-to-Neumann/Poisson operators, subtract source and clone before taking Schatten norms, and decide whether those nonlocal terms preserve the `S_r`, `r>1`, threshold or create the first genuine global obstruction.
