# WI-182 — confluence near-extremizers kill every extensive source-only proximal-mismatch charge

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + ROUTE-SPECIFIC-BARRIER`. The source-structured correction proposed in `CLUE-source-structured-proximal-mismatch-below-clipping` has a valid exact square-completion interpretation, but it cannot by itself supply an extensive positive charge at the Montgomery--Taylor population scale. The existing WI-140 mixed confluence near-extremizers already force the normalized source-specific mismatch to zero while preserving any prescribed simple-real fraction and the corresponding scalar pair budget.

More precisely, let `R` be the exact Lamzouri remainder from WI-170, let `G_s` be the full simple-real Gram, let `e=D-n=r+2k` be the number of distinct exceptional elements, and let the actual source correction in full-Gram coordinates be

\[
Z=A+\widetilde C\succeq0,
\qquad \operatorname{rank} Z\le e,
\]

with `A` the conjugation-even projection Gram and `\widetilde C` the transported conjugation-odd correction from the clue. Put

\[
Y=(G_s-2I)_+,
\qquad
Y_-=(2I-G_s)_+,
\]

and

\[
\Gamma_e
:=\|Z-Y\|_{\rm HS}^2-\mathcal T_e(G_s)
 +2\operatorname{tr}(Y_-Z).
\tag{1}
\]

Then

\[
\boxed{0\le \Gamma_e\le R.}
\tag{A}
\]

Consequently, for every target simple-real fraction `s in [0,1]`, WI-140 supplies finite Lamzouri multisets with

\[
\frac nN\to s,
\qquad
\frac QN\to 2-s,
\qquad
\frac RN\to0,
\]

whose entire complementary population is simple and off the real axis. Along the same configurations,

\[
\boxed{\frac{\Gamma_e}{N}\to0.}
\tag{B}
\]

Taking `s=H_MT` reproduces the ideal Montgomery--Taylor scalar budget `Q/N -> C_MT=2-H_MT` while a positive-density exceptional population remains simple and off-line and the proposed source-specific mismatch contributes no positive limiting density. Therefore no theorem using only Lamzouri's finite source geometry, the current scalar pair budget, and population bookkeeping can prove

\[
\Gamma_e\ge cN
\]

with any fixed `c>0` at the target density, nor any lower bound `Gamma_e/N >= phi(1-n/N)` with `phi(1-H_MT)>0` on that abstract source class.

This does **not** rule out a mismatch lower bound after adding a genuinely stronger hypothesis that excludes WI-140's dilute confluence family, such as local-density/separation information, an additional independently controlled correlation observable, or a source-evaluable mixed moment. The result closes the proposed mismatch as a free gain from the already retained source geometry; it does not close every strengthened mismatch mechanism.

## 1. Exact square completion and the source-specific remainder

Use the finite Hilbert-space notation of Lamzouri's Proposition 2.1 as reconstructed in WI-179--WI-181. Let `F : C^n -> M_0` synthesize the projected simple-real vectors `b_x`, so

\[
B=F^*F,
\qquad
S=FF^*,
\qquad
U=FB^{-1/2}:\mathbb C^n\to M_0.
\tag{2}
\]

Finite exponential independence gives `B>0`, so `U` is unitary onto `M_0`:

\[
U^*U=B^{-1/2}F^*FB^{-1/2}=I.
\tag{3}
\]

No quantitative conditioning estimate for `B^{-1/2}` is used below. Let

\[
G_s=B+A,
\qquad
A\succeq0,
\tag{4}
\]

where `A` is the Gram of the simple-real projections into Lamzouri's exceptional-even space, and let `C\succeq0` be the actual conjugation-odd correction on `M_0`. Transport it by the unitary polar factor,

\[
\widetilde C=U^*CU,
\qquad
Z=A+\widetilde C\succeq0.
\tag{5}
\]

The source ranks satisfy

\[
\operatorname{rank}A\le r+k,
\qquad
\operatorname{rank}\widetilde C=\operatorname{rank}C\le k,
\]

hence

\[
\boxed{\operatorname{rank}Z\le r+2k=e=D-n.}
\tag{6}
\]

The pre-minimization source inequality in the clue, equivalently the WI-179 remainder before the two rank relaxations are forgotten, is

\[
R\ge
\|G_s-I-Z\|_{\rm HS}^2+2\operatorname{tr}Z.
\tag{7}
\]

For a Hermitian `G_s`, split `G_s-2I=Y-Y_-` into its positive and negative parts. Since `YY_-=0`, direct expansion gives

\[
\boxed{
\|G_s-I-Z\|_{\rm HS}^2+2\operatorname{tr}Z
=
\operatorname{tr}\Psi(G_s)
+\|Z-Y\|_{\rm HS}^2
+2\operatorname{tr}(Y_-Z).
}
\tag{8}
\]

Here

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

The last trace in (8) is nonnegative because `Y_-` and `Z` are PSD. Since `rank Z<=e`, the Frobenius Eckart--Young theorem applied to `Y\succeq0` gives

\[
\|Z-Y\|_{\rm HS}^2\ge
\mathcal T_e(G_s)
:=\sum_{j>e}(\mu_j(G_s)-2)_+^2.
\tag{9}
\]

Thus the quantity in (1) is nonnegative and (8) becomes the exact decomposition

\[
\boxed{
\|G_s-I-Z\|_{\rm HS}^2+2\operatorname{tr}Z
=
\operatorname{tr}\Psi(G_s)
+\mathcal T_e(G_s)
+\Gamma_e.
}
\tag{10}
\]

Combining (7) and (10), and using nonnegativity of `tr Psi` and `T_e`, proves (A):

\[
R\ge
\operatorname{tr}\Psi(G_s)+\mathcal T_e(G_s)+\Gamma_e
\ge\Gamma_e\ge0.
\tag{11}
\]

This domination is the decisive point. It avoids any attempt to estimate `A`, `C`, or `B^{-1/2}` separately: every source-specific mismatch charge of the form proposed by the clue is already trapped below the complete remainder `R`.

## 2. WI-140 supplies the required positive-density source near-extremizers

WI-140 constructs mixed finite Lamzouri configurations from two asymptotic local blocks:

- isolated simple real singleton blocks, with `(N,n,Q)=(1,1,1)` and zero finite deficit;
- simple off-line conjugate-pair blocks whose horizontal depth tends to zero, with `(N,n,Q)=(2,0,4+o(1))` and finite deficit tending to zero.

The real centers of all blocks are separated so that cross-block kernel contributions vanish by the Riemann--Lebesgue lemma. For integer sequences `a_j,b_j`, the resulting finite multisets have

\[
N_j=a_j+2b_j,
\qquad
n_j=a_j,
\qquad
Q_j=a_j+4b_j+o(N_j).
\tag{12}
\]

Hence, for any prescribed `s in [0,1]`, choosing

\[
\frac{a_j}{a_j+2b_j}\to s
\]

gives

\[
\boxed{
\frac{n_j}{N_j}\to s,
\qquad
\frac{Q_j}{N_j}\to2-s.
}
\tag{13}
\]

All labels are simple. The `a_j` singleton labels are real and the remaining `2b_j` labels occur in non-real conjugate pairs, so

\[
M_j=0,
\qquad
O_j=2b_j=N_j-n_j.
\tag{14}
\]

WI-170's exact population identity is

\[
Q-N=O+2M+R.
\tag{15}
\]

Substituting (14) yields

\[
R_j
=Q_j-N_j-O_j
=Q_j-2N_j+n_j.
\tag{16}
\]

The right side is exactly WI-140's complete finite deficit `Delta_j`. Its mixed construction gives

\[
\boxed{\frac{R_j}{N_j}=\frac{\Delta_j}{N_j}\to0.}
\tag{17}
\]

Now apply (A) to every member of the sequence:

\[
0\le\frac{\Gamma_{e_j}}{N_j}
\le\frac{R_j}{N_j}
\to0.
\tag{18}
\]

This proves (B). No numerical quadrature, approximate polar decomposition, or assumption about the eigenvalue-2 threshold is involved.

At the Montgomery--Taylor target choose

\[
s=H_{\rm MT}
=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\tag{19}
\]

Then

\[
\frac{Q_j}{N_j}\to
2-H_{\rm MT}
=rac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=C_{\rm MT},
\tag{20}
\]

while

\[
\frac{O_j}{N_j}\to1-H_{\rm MT}>0,
\qquad
\frac{\Gamma_{e_j}}{N_j}\to0.
\tag{21}
\]

Thus this is not the isolated-pair objection explicitly anticipated in the clue: the exceptional population has a prescribed positive limiting density and the scalar pair budget is the same limiting one used in the Montgomery--Taylor application.

## 3. What the barrier does and does not close

Suppose one seeks a source-only lower bound at fixed limiting simple-real fraction `s`, of the form

\[
\Gamma_e\ge c(s)N-o(N)
\tag{22}
\]

with `c(s)>0`. Equations (13), (18) contradict (22) on the finite Lamzouri source class for every `s` for which the WI-140 mixed construction is used. In particular `c(H_MT)>0` is impossible while retaining only the source conditions already present in Proposition 2.1 plus the single scalar `Q/N -> C_MT` constraint.

The same argument applies to any nonnegative refinement `J` satisfying

\[
0\le J\le R
\tag{23}
\]

on the finite source class: WI-140 forces `J/N->0` on its mixed near-extremizers. This explains why changing coordinates from the quotient correction to the full-Gram proximal optimizer cannot by itself evade the confluence barrier. A new nonnegative decomposition of the *same* remainder may identify useful geometry, but it cannot create an extensive tax on a family where the entire remainder is already subextensive.

The boundary is equally important. WI-140 deliberately uses a dilute sequence in Lamzouri's rescaled ordinate coordinate. It is not asserted to model the local density, spacing distribution, or full family of correlations of actual zeta zeros. Therefore (22) could become possible after adding a source theorem that quantitatively excludes this dilution or confluence geometry. Examples include an independently established local-density/separation constraint, another support-admissible correlation observable not reducible to the scalar `Q`, or a mixed even/odd moment with a zeta-side evaluation. Such an input would be genuinely new arithmetic/source information, not a free consequence of the present finite Hilbert geometry.

Critical-line multiplicity also remains distinct. The counterexample above can be chosen with **no repeated real points at all**: its full complementary population is simple and off-line. Thus the obstruction is not caused by silently replacing off-line pairs by real doubles, even though confluence to doubles is the local mechanism that makes each pair block cheap.

No unconditional zeta-zero percentage changes in this finding.

## 4. Primary sources, prior art, and novelty boundary

The primary external source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), especially Proposition 2.1 and Section 3. Lamzouri defines the finite exponential-feature Hilbert space used here; his unconditional zeta application takes a real even `eta in C_c^infty((-1/2,1/2))`, so `K=widehat{eta^2}` and the corresponding real pair-correlation profile has support in `[-1,1]`. His Lemma 3.2 gives

\[
C_{\rm MT}=
\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=1.3274992963206\ldots.
\]

The unconditional support-one pair-correlation input is the Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh theorem cited by Lamzouri; the confluence and dilute-block construction used here is the already persisted WI-140 result. The low-rank Frobenius approximation step is the classical Eckart--Young theorem already audited in WI-179. Riemann--Lebesgue is used only inside WI-140's block separation, not as a new external assumption here.

A targeted current-literature audit found Lamzouri's September 2026 preprint and no external treatment of the source-specific proximal mismatch `Gamma_e`, its polar-coordinate formulation, or the implication (A)--(B). This is not a priority claim. The line-specific mathematical delta is the exact observation that the newly proposed `Gamma_e` is bounded above by the already controlled complete remainder and is therefore annihilated, at positive exceptional density and the correct scalar Montgomery--Taylor normalization, by WI-140's existing confluence near-extremizers.

The strongest safe conclusion is therefore:

\[
\boxed{
\text{source-structured proximal mismatch alone is not an extensive bootstrap resource.}
}
\]

A surviving version must state the extra density, correlation, overlap, or arithmetic hypothesis that excludes the WI-140 family and must prove that this hypothesis is actually available for zeta zeros.