# WI-170 — Lamzouri's distinctness slack is an exact off-line/multiplicity budget

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE`. Lamzouri's Proposition 2.1 contains two headline inequalities driven by the same pair-correlation quantity `Q`: one for simple real elements and one for all distinct elements. WI-126--WI-140 have so far used the first inequality to expose horizontal transversality, exact tensor inertia, and the off-line confluence barrier. Recombining the complete WI-137 slack with the elementary population identities shows that the second inequality has a sharper interpretation than its published scalar statement: its entire slack contains the **full multiplicity-weighted off-real population with coefficient one**, and the remaining terms are exactly nonnegative.

If `D` is the number of distinct elements of Lamzouri's finite conjugation-invariant multiset, `M:=N-D` is total multiplicity excess, and

\[
O:=2\sum_{z\in Z_+}m_z
\]

is the number of non-real labels counted with multiplicity, then

\[
\boxed{
Q-N-O-2M
=
\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
+2S_1+E_{\mathbb R}+4H_U+4H_V
\ge0.
}
\tag{A}
\]

Equivalently,

\[
\boxed{
Q-3N+2D
=O+
\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
+2S_1+E_{\mathbb R}+4H_U+4H_V,
}
\tag{B}
\]

so Lamzouri's distinctness lower bound strengthens finitely to

\[
\boxed{
D\ge \frac{3N-Q+O}{2}.
}
\tag{C}
\]

The joint budget

\[
\boxed{O+2M\le Q-N}
\tag{D}
\]

separates the two principal exceptional populations in exactly the way requested by the Weil-inertia mandate: `O` is off-critical mass after the zeta specialization, while `M` is multiplicity excess and includes critical-line multiples as well as repeated off-line zeros. The coefficients in (D) are individually sharp in Lamzouri's abstract finite class. A real double saturates the multiplicity coefficient `2` exactly; a simple off-real conjugate pair approaching the real axis asymptotically saturates the off-real coefficient `1`. Thus the second headline inequality does contain a discontinuous count charge that the first slack lacks, but **it does not supply an independent bootstrap reservoir**: the same `Q-N` budget can be spent at the same leading cost either on critical-line doubles or on arbitrarily shallow simple off-line pairs. Any RH-facing improvement must add source information that forbids this exchange, rather than merely combining Lamzouri's two published inequalities.

No unconditional simple-critical-zero proportion changes in this finding.

## 1. Primary-source contract

The primary source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1. For a finite nonempty conjugation-invariant multiset `Z`, with `N=|Z|` counted with multiplicity and

\[
Q:=\sum_{z,s\in Z}K(z-s)^2,
\]

Lamzouri proves both

\[
n\ge2N-Q
\tag{1}
\]

for the number `n` of simple real elements, and

\[
D\ge\frac{3N-Q}{2}
\tag{2}
\]

for the number `D` of distinct elements. His zeta application evaluates the same `Q` by the unconditional pair-correlation theorem of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh and obtains the Montgomery--Taylor constants `0.672500703679...` and `0.836250351839...` respectively.

WI-126 reconstructs Lamzouri's nested spaces `U subset V subset W`, and WI-137 packages the complete slack in (1) as an exact operator identity. Write `R_1` for the simple real points, `R_2` for the distinct repeated real points, and `Z_+` for one representative of each non-real conjugate pair. Put

\[
r:=|R_2|,\qquad k:=|Z_+|,
\]

and let the multiplicities be `m_x>=2` on `R_2` and `m_z>=1` on `Z_+`. Then

\[
N=n+\sum_{x\in R_2}m_x+2\sum_{z\in Z_+}m_z,
\qquad
D=n+r+2k.
\tag{3}
\]

The exact WI-137 identity is

\[
\boxed{
Q-(2N-n)
=
\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
+2S_1+2E_{\mathbb R}+4E_{\mathbb C}+4H_U+4H_V,
}
\tag{4}
\]

where

\[
E_{\mathbb R}:=\sum_{x\in R_2}(m_x-2),
\qquad
E_{\mathbb C}:=\sum_{z\in Z_+}(m_z-1),
\tag{5}
\]

and `S_1,H_U,H_V` are the nonnegative source/projection charges defined in WI-126--WI-137. All terms on the right of (4) are nonnegative.

The literature-backed claims in this section are Lamzouri's two finite inequalities and their pair-correlation application. Identity (4) is the already persisted exact Mathia reconstruction. Equations (A)--(D) below are new algebraic consequences of that reconstruction; they are not attributed to Lamzouri.

## 2. Population bookkeeping eliminates the off-line multiplicity excess exactly

Define the total multiplicity excess

\[
M:=N-D.
\tag{6}
\]

Using (3)--(5),

\[
\boxed{
M=r+E_{\mathbb R}+2E_{\mathbb C}.
}
\tag{7}
\]

The multiplicity-weighted non-real population is

\[
\boxed{
O:=2\sum_{z\in Z_+}m_z=2k+2E_{\mathbb C}.
}
\tag{8}
\]

Also

\[
N-n=2r+E_{\mathbb R}+O.
\tag{9}
\]

Start from the left side of (A) and insert the simple-real deficit from (4):

\[
\begin{aligned}
Q-N-O-2M
&=[Q-(2N-n)]+(N-n)-O-2M\\
&=[Q-(2N-n)]-E_{\mathbb R}-4E_{\mathbb C},
\end{aligned}
\tag{10}
\]

where the last equality is exactly (7)--(9). Substituting (4) cancels all of the off-line multiplicity-excess term and one copy of the repeated-real excess:

\[
\begin{aligned}
Q-N-O-2M
&=\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2\\
&\quad+2S_1+E_{\mathbb R}+4H_U+4H_V.
\end{aligned}
\tag{11}
\]

This is (A). No inequality has been used in (10)--(11); it is an exact identity.

Since `M=N-D`, (11) is equivalently

\[
Q-3N+2D-O
=
\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
+2S_1+E_{\mathbb R}+4H_U+4H_V,
\tag{12}
\]

which is (B). Dropping the nonnegative right side gives (C) and (D).

The cancellation of `E_C` is load-bearing. An off-real pair of multiplicity `m` is not charged once as a distinct pair: its `2m` labels enter `O`, while its repeated copies also enter `2M`. Thus (D) automatically assigns the stronger cost appropriate to repeated off-line zeros without mixing them with repeated real zeros.

## 3. Exact separation of the exceptional populations

Equation (A) has a useful interpretation unavailable from the two headline percentages viewed separately. The pair-correlation surplus `Q-N` is partitioned into

\[
\boxed{
Q-N
=O+2M+R,
}
\tag{13}
\]

with

\[
R:=
\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
+2S_1+E_{\mathbb R}+4H_U+4H_V
\ge0.
\tag{14}
\]

The three pieces have different meanings.

- `O` is exactly the non-real population counted with multiplicity. Under Lamzouri's zeta rescaling this is the off-critical zero mass in the height window, not an uncertified residue inferred from a proportion theorem.
- `2M` is twice the total multiplicity excess `N-D`; it charges repeated critical-line zeros and repeated off-line zeros according to their actual multiplicity.
- `R` is genuine source/operator slack: Hilbert--Schmidt mismatch from the canonical `2/1/0` target, simple-real leakage into `U`, real multiplicity above two, and the two horizontal transversality charges.

This is precisely why the uncertified complement must not be called an off-line population. The same scalar budget can be occupied by two qualitatively different zero types, and (13) keeps those types explicit before any bound is taken.

WI-138 gives the complementary exact inertia statement

\[
n_-(\mathcal A_F)=k,
\tag{15}
\]

which counts distinct off-line conjugate pairs rather than multiplicity-weighted labels. Equations (8), (13), and (15) therefore separate both notions: `k` is a sign/inertia count, while `O` is the multiplicity-weighted off-line mass. Repeated off-line zeros increase `O` and `M` without changing the negative index.

## 4. Zeta-scale consequence is a joint budget, not a new percentage

For Lamzouri's zeta multiset at height `T`, let `O(T)` denote the number of off-critical zeros in the window, counted with multiplicity, and let

\[
M(T):=N(T)-N_d(T)
\]

be total multiplicity excess. For each fixed admissible test function, (D) gives the finite inequality

\[
O(T)+2M(T)\le Q_T-N(T).
\tag{16}
\]

Lamzouri's unconditional pair-correlation evaluation and the Montgomery--Taylor limiting family give

\[
\limsup_{T\to\infty}
\frac{O(T)+2M(T)}{N(T)}
\le
1-C_0,
\tag{17}
\]

with

\[
C_0=
\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
=0.672500703679\ldots.
\]

Hence

\[
\boxed{
\limsup_{T\to\infty}
\frac{O(T)+2\bigl(N(T)-N_d(T)\bigr)}{N(T)}
\le0.327499296320\ldots.
}
\tag{18}
\]

Taking `O>=0` recovers the `83.625...%` distinctness theorem. Taking `M>=0` gives the corresponding upper budget for off-line labels. The point is not either marginal bound; it is the **joint tradeoff**. A configuration carrying positive off-line mass has strictly less room for multiplicity excess, and conversely.

This does not improve WI-036's stronger simple-critical proportion. The analytic right side in (18) is still the Montgomery--Taylor `Q` budget, and (18) admits the same leading exceptional mechanisms that make the simple-real inequality sharp. No claim is made that the actual zeta zeros approach equality in (18).

## 5. The coefficients `1` and `2` are individually sharp

The two canonical controls from the existing line show that neither coefficient in (D) can be increased universally while retaining the same right side `Q-N`.

First take one real point of multiplicity two. WI-126 records

\[
N=2,\qquad D=1,\qquad M=1,\qquad O=0,\qquad Q=4.
\]

Thus

\[
O+2M=2=Q-N,
\tag{19}
\]

and every term in `R` vanishes. Any universal replacement of the coefficient `2` on `M` by a larger constant already fails on this exact critical-line-double equality configuration.

Next take the isolated simple non-real conjugate pair of WI-140. Put

\[
t(y):=\|h_y\|^2>0.
\]

Then

\[
N=2,\qquad D=2,\qquad M=0,\qquad O=2,
\]

and WI-140 computes

\[
Q-4=8t+8t^2,
\qquad t(y)\to0
\quad(y\to0).
\tag{20}
\]

Therefore

\[
Q-N=2+8t+8t^2\longrightarrow2=O.
\tag{21}
\]

For any fixed `a>1`, the putative universal strengthening `aO+2M<=Q-N` fails for all sufficiently shallow non-real pairs. Thus the coefficient `1` on off-real labels is also sharp.

These controls are stronger than a numerical observation. They show that the same pair-correlation budget has two coefficientwise optimal ways to approach saturation: a real double uses the multiplicity axis, while an arbitrarily shallow simple off-line pair uses the off-line axis. The discontinuous population change at confluence is absorbed by the distinctness slack rather than producing a contradiction.

## 6. Why the distinctness theorem does not bootstrap the simple-real theorem

At first sight the second inequality in Lamzouri's Proposition 2.1 looks promising for the RH-facing objective because, unlike the first horizontal remainder, (B) contains a hard count term `O` that does not vanish when a non-real pair approaches the real axis. Equation (13) shows exactly why this does not close the gap.

The count term is paid from `Q-N`, not from the near-equality deficit `Q-(2N-n)` used by the simple-real theorem. Even an all-real, all-simple configuration has `D=N`, `M=O=0` and therefore leaves the macroscopic residual

\[
Q-N\sim(1-C_0)N
\tag{22}
\]

in the distinctness budget. There is no source reason for that reservoir to be `o(N)`. Consequently the fact that every off-line label costs one unit in (13) does not force the off-line mass to vanish.

More sharply, the two controls (19)--(21) show that merely taking positive affine combinations of Lamzouri's two headline inequalities cannot create an autonomous anti-confluence charge. The real-double and shallow-off-line axes already saturate the two exchange rates permitted by the common `Q` budget. To distinguish them one needs information not present in those two scalar consequences of the same second moment: for example a source inequality controlling the residual `R`, a statistic that couples horizontal location to multiplicity, or genuinely new higher-correlation/support information.

This is a barrier, not a statement that Lamzouri's distinctness inequality is redundant. Equation (13) is useful structural bookkeeping and may become coercive if another theorem independently controls `M`, `R`, or a component of `O`. What is closed is the idea that the published distinctness percentage by itself supplies the missing count discontinuity needed to upgrade WI-140 into a defect-to-zero argument.

## 7. Prior-art and novelty audit

Lamzouri's Proposition 2.1 explicitly proves the two literature-backed finite inequalities (1)--(2), and the Alpöge--Furman theorem gives the same `67.25...%` simple-critical and `83.625...%` distinct constants through the matrix-inertia route. The classical multiplicity literature represented in this line by Conrey--Ghosh--Gonek supplies related integrality/counting inequalities. None of those inputs is treated as new here.

The internal precursors are WI-126's exact population/slack bookkeeping, WI-137's complete Hilbert--Schmidt identity, WI-138's exact negative-index count, and WI-140's one-pair confluence control. A targeted external search around Lamzouri's September 2026 preprint, the Alpöge--Furman distinctness result, off-line mass, and the expressions `Q-3N+2D` / `Q-N` located the separate headline bounds but no statement of the exact joint identity (A), the strengthened finite inequality (C), or the coefficientwise-sharp budget (D). Absence from that search is not evidence of priority, and no priority claim is made.

The durable Mathia deduction is the exact recombination: **Lamzouri's distinctness slack equals the full off-real label population plus an explicit nonnegative source/operator residual, and the resulting off-line/multiplicity exchange rates are already sharp on the canonical confluence controls.**

## 8. Research consequence

The exceptional complement now has an additional exact ledger. At the Lamzouri finite level,

\[
Q-N=\underbrace{O}_{\text{off-real labels}}
+\underbrace{2M}_{\text{multiplicity excess}}
+\underbrace{R}_{\text{operator/source slack}}.
\]

This does not identify the uncertified fraction with off-line zeros; it proves the opposite structural lesson. Critical-line doubles and shallow simple off-line pairs are two distinct ways of spending the same second-moment budget at their sharp leading exchange rates. Higher multiplicity and nontrivial source geometry create additional cost through `M` and `R`, but the two canonical mechanisms remain compatible with saturation.

A surviving defect-to-zero mechanism must therefore break this exchange. A decisive next input would be an independent zeta theorem forcing a positive lower bound for `R` whenever `O` is positive, or a relation preventing the `O`-axis confluence control from coexisting with the actual zero statistics. Without such information, combining the simple-real and distinctness inequalities from the same `Q` cannot iterate the present defect to zero.