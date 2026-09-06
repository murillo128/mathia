# WI-178 — Lamzouri's exceptional-population slack dominates the simple-real Gram defect

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + STRICT-DISTINCTNESS-IMPROVEMENT + BOOTSTRAP-INTERFACE`.

Lamzouri's finite Hilbert-space proposition and the Alpöge--Furman/Zeta-Lab Gram-defect refinement are not merely parallel ways to prove a simple-critical-zero bound.  The exact slack decomposition of WI-137/WI-170 contains the **entire clipped spectral defect of the Gram matrix of the simple real vectors**, even after the repeated-real and off-real sectors are left uncollapsed.  Consequently, if `G_s` is the Gram matrix of the simple real elements of Lamzouri's finite conjugation-invariant multiset, then

\[
\boxed{
Q-N\ \ge\ O+2M+\operatorname{tr}\Psi(G_s),
}
\tag{A}
\]

where `O` is the multiplicity-weighted non-real population, `M=N-D` is total multiplicity excess, and

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

Thus the Gram defect is not a proof remainder available only for the simple-zero count: it is a source of **coercive budget that must be removed from the off-line/multiplicity reservoir as well**.

At the Montgomery--Taylor profile, inserting the independently kernel-checked four-point source certificate of WI-172 therefore gives the unconditional joint zeta-zero budget

\[
\boxed{
\limsup_{T\to\infty}
\frac{O(T)+2\bigl(N(T)-N_d(T)\bigr)}{N(T)}
\le 1-B_{2330}
=0.32713964116113334049\ldots,
}
\tag{B}
\]

where

\[
B_{2330}
=
\frac{14400000H_{\rm MT}-17240}{14366681}
=0.67286035883886665950\ldots .
\]

In particular, dropping `O(T)` yields the strictly improved unconditional distinct-zero proportion

\[
\boxed{
\liminf_{T\to\infty}\frac{N_d(T)}{N(T)}
\ge
\frac{1+B_{2330}}2
=0.83643017941943332975\ldots .
}
\tag{C}
\]

This improves Lamzouri/Alpöge--Furman's Montgomery--Taylor distinctness constant

\[
\frac{1+H_{\rm MT}}2
=0.83625035183970582286\ldots
\]

by

\[
\frac{B_{2330}-H_{\rm MT}}2
=0.00017982757972750688\ldots .
\]

The numerical gain is secondary.  The structural content is (A): **any future lower bound for the simple-real Gram defect simultaneously sharpens the joint off-line/multiplicity budget**, without treating the uncertified complement as an off-critical population.

## 1. Primary-source and internal interfaces

The primary finite source is Proposition 2.1 of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026).  For a finite nonempty conjugation-invariant multiset `Z`, normalized Hilbert vectors

\[
f_z(u)=\eta(u)e^{-2\pi iuz},
\]

and `Q=\sum_{z,w\in Z}K(z-w)^2`, Lamzouri proves the simple-real and distinct-element inequalities from one Hilbert tensor.

WI-126 verifies that the nested spaces in his proof have the exact dimensions

\[
\dim U=r+k,
\qquad
\dim(V\ominus U)=n,
\qquad
\dim(W\ominus V)=k,
\]

because finite exponentials at distinct complex frequencies are linearly independent and `(f_z,f_{\bar z})\leftrightarrow(g_z,h_z)` is an invertible change of variables.

WI-137 then gives the exact operator slack, and WI-170 rewrites its distinctness part as

\[
\boxed{
Q-N=O+2M+R,
}
\tag{1}
\]

with

\[
R=
\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
+2S_1+E_{\mathbb R}+4H_U+4H_V\ge0.
\tag{2}
\]

Here

\[
S_1=\sum_{x\in R_1}\|P_Uf_x\|^2,
\]

`E_R` is repeated-real multiplicity above two, and `H_U,H_V` are the already defined anti-invariant projection charges.  The new step is to prove

\[
\boxed{R\ge\operatorname{tr}\Psi(G_s).}
\tag{3}
\]

Combining (1) and (3) is exactly (A).

## 2. Compress the full Lamzouri tensor to the simple-real quotient

Put

\[
M_0:=V\ominus U.
\]

For every simple real point `x`, write

\[
a_x=P_Uf_x,
\qquad
b_x=P_{M_0}f_x.
\]

Let

\[
S:=\sum_{x\in R_1} b_x\otimes b_x
\]

be the frame operator on `M_0`.  Since `dim M_0=n` and the images of the `n` simple-real vectors span `M_0`, the vectors `b_x` are linearly independent.  Their Gram matrix

\[
B=(\langle b_x,b_y\rangle)_{x,y\in R_1}
\]

therefore has the same `n` positive eigenvalues as `S`.

The full simple-real Gram matrix is

\[
G_s=(\langle f_x,f_y\rangle)=B+A,
\tag{4}
\]

where

\[
A=(\langle a_x,a_y\rangle)\succeq0,
\qquad
\operatorname{tr}A=S_1.
\tag{5}
\]

Now compress Lamzouri's tensor operator to `M_0`.  Every repeated-real vector and every conjugation-even vector `g_z` lies in `U`, so they disappear.  Only the simple-real frame and the projected odd components remain:

\[
P_{M_0}\mathcal A_F P_{M_0}=S-H,
\tag{6}
\]

where

\[
H:=2\sum_{z\in Z_+}m_z
(P_{M_0}h_z)\otimes(P_{M_0}h_z)\succeq0.
\tag{7}
\]

The target `P_U+P_V` is the identity on `M_0`.  Hence the Hilbert--Schmidt term in (2) dominates the `M_0` diagonal block:

\[
\|\mathcal A_F-(P_U+P_V)\|_{\rm HS}^2
\ge \|S-H-I\|_{\rm HS}^2.
\tag{8}
\]

Furthermore,

\[
\operatorname{tr}H
=2\sum_zm_z\|P_{M_0}h_z\|^2
\le2H_U,
\tag{9}
\]

so `4H_U>=2 tr H`.  Dropping the other nonnegative pieces of (2) gives

\[
\boxed{
R\ge
\|S-H-I\|_{\rm HS}^2
+2\operatorname{tr}H
+2S_1.
}
\tag{10}
\]

This is the uncollapsed exceptional-block interface: the off-line odd sector is allowed to cancel the simple-real frame before any estimate is made, but the amount used for that cancellation is itself charged by `H_U`.

## 3. The optimal PSD cancellation cost is exactly the clipped Gram defect

For every positive-semidefinite operator `S` and every `H>=0`,

\[
\boxed{
\|S-I-H\|_{\rm HS}^2+2\operatorname{tr}H
\ge\operatorname{tr}\Psi(S).
}
\tag{11}
\]

To see this, diagonalize `S`.  In that basis every off-diagonal entry of `H` contributes a nonnegative square, while each diagonal entry `h>=0` has scalar cost

\[
(\lambda-1-h)^2+2h.
\]

Its minimum over `h>=0` is

\[
\begin{cases}
(\lambda-1)^2,&0\le\lambda\le2,\\
2\lambda-3,&\lambda\ge2,
\end{cases}
\]

attained by `h=(\lambda-2)_+`.  Summing proves (11).  This is precisely the same clipped spectral function that appears in the Alpöge--Furman/Zeta-Lab stable rank--trace remainder.

Applying (11) in (10) yields

\[
R\ge\operatorname{tr}\Psi(S)+2S_1
=\operatorname{tr}\Psi(B)+2\operatorname{tr}A.
\tag{12}
\]

It remains only to restore the `U` component of the simple-real vectors.

## 4. Restoring the projected component costs at most `2 S_1`

The scalar function `Psi` is globally `2`-Lipschitz on `[0,\infty)`.  Since `G_s=B+A` with `A>=0`, Weyl monotonicity gives, for ordered eigenvalues,

\[
\lambda_j(G_s)\ge\lambda_j(B),
\qquad
\sum_j\bigl(\lambda_j(G_s)-\lambda_j(B)\bigr)=\operatorname{tr}A.
\]

Therefore

\[
\begin{aligned}
\operatorname{tr}\Psi(G_s)
&\le
\sum_j\left[
\Psi(\lambda_j(B))
+2(\lambda_j(G_s)-\lambda_j(B))
\right]\\
&=
\operatorname{tr}\Psi(B)+2\operatorname{tr}A.
\end{aligned}
\tag{13}
\]

Combining (12) and (13) proves (3), hence the finite joint budget (A).

The exact dimension statement from WI-126 is load-bearing here.  If the projected simple-real vectors could lose rank in `V/U`, zero eigenvalues of their Gram matrix would add an extra `Psi(0)=1` term.  Linear independence rules out that loss exactly.

## 5. Montgomery--Taylor specialization and the new distinctness constant

For the Montgomery--Taylor limiting profile, Lamzouri's unconditional pair-correlation evaluation gives

\[
\frac{Q_T}{N(T)}\longrightarrow 2-H_{\rm MT},
\qquad
H_{\rm MT}
=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\tag{14}
\]

The formally checked Zeta-Lab source used in WI-172 proves, for the actual Montgomery--Taylor overlap kernel, the four-point certificate

\[
(n,c,m,p)=
\left(4,\frac{2330}{10^6},432,2500\right).
\]

Its deterministic block theorem is explicitly a lower bound for the same clipped defect `D(G_B)=tr Psi(G_B)` plus the span pressure.  The formally proved offset averaging then yields

\[
D(G_s)
\ge
\frac{c(432-3)}{432}\,N_0^s
-rac{3(432-1)}{2500\cdot432}\,N
-o(N).
\tag{15}
\]

The usual simple-zero bridge combines (15) with `N_0^s>=H_MT N+D(G_s)-o(N)` and gives WI-172's

\[
\frac{N_0^s}{N}\ge B_{2330}-o(1).
\]

At the lower endpoint `B_{2330}`, (15) supplies exactly

\[
\boxed{
\liminf\frac{D(G_s)}N
\ge B_{2330}-H_{\rm MT}.
}
\tag{16}
\]

Indeed this is the algebra defining the bridge fixed point.  Explicitly,

\[
B_{2330}-H_{\rm MT}
=
\frac{33319H_{\rm MT}-17240}{14366681}
=0.00035965515945501376\ldots>0.
\tag{17}
\]

The hard Montgomery--Taylor profile is reached, as in the existing bridge, through the standard approximating/taper limit; the finite source certificate is stable under the corresponding uniform kernel approximation, with the explicit `delta` error already formalized in Zeta-Lab `S13`.  No wider support, higher prime moment, RH assumption, or conjectural zero statistic is introduced.

Insert (14) and (16) into (A):

\[
\limsup\frac{O+2M}{N}
\le
(1-H_{\rm MT})-(B_{2330}-H_{\rm MT})
=1-B_{2330},
\]

which proves (B).  Since `M=N-N_d`, dropping `O>=0` gives

\[
\limsup\frac{M}{N}\le\frac{1-B_{2330}}2,
\]

and therefore (C).

## 6. Equality, stress tests, and interpretation

The coefficients retain the mandate's separation of the exceptional complement.  A critical-line double has `O=0`, `M=1`; a shallow simple off-line conjugate pair has `O=2`, `M=0`.  Both spend two units in `O+2M`, which is why confluence remains possible.  Higher critical-line multiplicity and repeated off-line zeros cost strictly more through `M`.  The Gram term does **not** identify the remaining exceptional population as off-line; it removes a separate amount of source slack before either exceptional mechanism can spend the residual budget.

Several possible failure modes were checked explicitly:

- The argument does not assume that the exceptional block is positive.  Its negative `h_z` contribution is retained as the arbitrary PSD subtractor `H` in (6)--(11).
- No commutativity between `S` and `H` is assumed.  Off-diagonal entries of `H` only increase the Hilbert--Schmidt objective in an eigenbasis of `S`.
- The projection `f_x -> P_{M_0}f_x` does not lose rank, by the exact exponential linear-independence argument of WI-126.
- Adding the discarded `U` Gram `A` can move eigenvalues in the direction that lowers `Psi`; inequality (13) uses only the global `2`-Lipschitz constant and therefore covers that worst case.
- The result is compatible with the confluence barriers WI-140--WI-173.  It improves a **budget**, not the coefficient-one charge per arbitrarily shallow off-line label.  It therefore does not imply RH or a defect-to-zero iteration by itself.

A useful equality picture also emerges.  To make (A) nearly sharp while `D(G_s)` is extensive, the exceptional odd sector must implement nearly the proximal optimizer `H=(S-2I)_+` on the simple-real quotient, the simple-real `U` projection must nearly saturate the `2`-Lipschitz restoration step, and every other WI-170 remainder must be small.  This is substantially more rigid than the scalar joint budget alone and gives a concrete target for future source-specific exclusion.

## 7. Prior-art and novelty audit

Literature-backed inputs are:

- Lamzouri, arXiv:2609.02882v1, Proposition 2.1 and its unconditional pair-correlation specialization;
- Alpöge--Furman, arXiv:2608.13637, for the finite Weil-form/rank--trace architecture and the original `0.6725/0.8362` theorem;
- Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, *Acta Arith.* 214 (2024), for the unconditional pair-correlation evaluation;
- the classical Weyl eigenvalue monotonicity principle and elementary spectral functional calculus.

The clipped defect `Psi`, pinching, and the `c=2330/10^6` four-point certificate are prior/internal source material already audited in WI-009--WI-020 and formally replayed in WI-172.  No novelty is claimed for those components.

A targeted current-literature search on 6 September 2026 around Lamzouri's Hilbert proof, Gram-defect refinements, four-point source certificates, and distinct-zero bounds found the published/current headline distinctness constant `(1+H_MT)/2=0.8362503518...`, but no statement coupling Lamzouri's exact exceptional-population budget to `tr Psi(G_s)` or the resulting `0.8364301794...` distinctness constant.  Absence from that search is not evidence of priority, and no priority claim is made.

The durable Mathia deduction is the exact bridge (3): **the uncollapsed Lamzouri remainder dominates the clipped Gram defect of the simple real subsystem**.  This transfers any independently justified Gram-defect gain into a simultaneous reduction of off-line mass plus twice multiplicity excess.

## Consequence for the research mandate

The support-one Gram refinements are more useful to the RH-facing program than their simple-zero percentages alone suggest.  They do not merely certify more simple critical zeros; they shrink an explicitly separated exceptional budget:

\[
\boxed{
O+2M+D(G_s)\le Q-N.
}
\]

The next discriminating question is whether the same proximal/equality structure can be made incompatible with the actual zeta source.  In particular, a source theorem showing that an off-line odd sector cannot simultaneously approximate the spectral cancellation `H=(S-2I)_+` across a positive density of simple-real Gram blocks would feed directly into the residual `R`, while WI-173 explains why a depth-only continuous charge cannot do this uniformly.  This is a genuinely uncollapsed exceptional-block target, aligned with the canonical objective rather than another scalar percentage optimization.
