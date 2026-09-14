# PF-336 — relative polar transport removes the normalized-insertion envelope

**Status:** `LITERATURE+DERIVED + RELATIVE-POLAR-PERTURBATION + HILBERT-SCHMIDT-COMMUTATOR-TRANSFER + CONDITION-NUMBER-FREE + POSITIVE/ROUTE-SHARPENING`.

PF-335 transfers physical-translation locality from the normalized pant insertion

\[
K=Q^{-1/2}\Lambda_{LL}Q^{-1/2}\ge0
\]

to the completed whitening map

\[
F=\bigl(Q^{1/2}(I+K)Q^{1/2}\bigr)^{1/2}Q^{-1/2},
\]

but its estimate for `F` carries the factor `\sqrt{1+\|K\|}`. Consequently PF-335 lists a uniform operator envelope `\sup_n\|K_n\|<\infty` as a load-bearing hypothesis before translation locality can be passed to the completed polar rotation from PF-330--PF-331.

That envelope is **not needed for the polar rotation itself**. The extra factor comes from controlling the nonunitary whitening map `F` before extracting its polar factor. If one instead applies relative perturbation theory directly to the unitary polar factor, the positive completion `I+K\ge I` supplies all of the inverse control required by the multiplicative perturbation.

Precisely, let

\[
H=I+K,\qquad S=H^{1/2},\qquad
A_0=Q^{1/2}HQ^{1/2},
\]

and write the right polar decomposition from PF-330--PF-331 as

\[
F=US,
\qquad
U=A_0^{1/2}Q^{-1/2}S^{-1}.
\]

For every unitary `V` commuting with `Q`, on every finite PF section,

\[
\boxed{
\|[U,V]\|_{\mathcal S_2}
\le \frac1{\sqrt2}\,\|[K,V]\|_{\mathcal S_2}.
}
\tag{1}
\]

The constant is independent of `\|K\|`, the retained dimension, the smallest seam eigenvalue, and the condition number of `Q`. Likewise, if `X=X^*` and `[X,Q]=0`,

\[
\boxed{
\|[U,X]\|_{\mathcal S_2}
\le \frac1{\sqrt2}\,\|[K,X]\|_{\mathcal S_2}.
}
\tag{2}
\]

For the PF-325 physical translations `\tau_t`, equation (1) therefore gives directly

\[
\boxed{
\|[U_n,\tau_t]\|_{\mathcal S_2}
\le \frac1{\sqrt2}
\left\|
Q_{L,n}^{-1/2}[\Lambda_{LL,n},\tau_t]Q_{L,n}^{-1/2}
\right\|_{\mathcal S_2}.
}
\tag{3}
\]

Hence the translation branch no longer needs the separate hypothesis `\sup_n\|K_n\|<\infty`:

\[
\boxed{
\sup_{t\in I_n}\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1)
\Longrightarrow
\sup_{t\in I_n}\|[U_n,\tau_t]\|=o(1).
}
\tag{4}
\]

The implication uses only `\|T\|\le\|T\|_{\mathcal S_2}` after (3). This removes one of the two explicit operator-theoretic gates left by PF-335. The remaining translation-side theorem is the geometric/PDE estimate for the **normalized pant insertion commutator itself**. As before, translation compatibility alone does not supply concentration of a completed reference packet, and spatial cutoffs do not commute with `Q`; the stronger fixed-window route remains separate.

## 1. The completed polar rotation is the adjoint polar factor of a graded product

The useful representation is not the polar decomposition of `F` itself. Put

\[
B:=SQ^{1/2}.
\tag{5}
\]

Then

\[
B^*B
=Q^{1/2}S^2Q^{1/2}
=Q^{1/2}HQ^{1/2}
=A_0.
\tag{6}
\]

Thus the polar decomposition of `B` is

\[
B=W A_0^{1/2},
\qquad
W=SQ^{1/2}A_0^{-1/2}.
\tag{7}
\]

Its unitary factor is exactly the adjoint of the PF-330/PF-331 completed rotation. Indeed,

\[
\begin{aligned}
W^*S
&=A_0^{-1/2}Q^{1/2}S^2\\
&=A_0^{-1/2}Q^{1/2}H\\
&=A_0^{-1/2}A_0Q^{-1/2}\\
&=A_0^{1/2}Q^{-1/2}=F.
\end{aligned}
\tag{8}
\]

Since `F=US` is the right polar decomposition and `S>0`, uniqueness gives

\[
\boxed{U=W^*.}
\tag{9}
\]

This representation exposes the correct relative perturbation variable. The potentially badly conditioned seam factor sits on the **right** of `S` in `B=SQ^{1/2}` and will not be inverted in the perturbation estimate.

## 2. Translation conjugation becomes a left multiplicative perturbation

Let `V` be unitary with `[V,Q]=0` and define

\[
H_1=VHV^*,\qquad S_1=H_1^{1/2}=VSV^*.
\tag{10}
\]

The translated graded product is

\[
B_1=S_1Q^{1/2}
=V(SQ^{1/2})V^*
=VBV^*.
\tag{11}
\]

If `W_1` is its unitary polar factor, equivariance of polar decomposition gives

\[
W_1=VWV^*.
\tag{12}
\]

At the same time, `B_1` is a **purely relative left perturbation** of `B`:

\[
B_1=(S_1S^{-1})B=D_1^*B,
\qquad
D_1=S^{-1}S_1.
\tag{13}
\]

There is no right perturbation. This is exactly the setting of Ren-Cang Li's relative unitary-polar theorem: for full-column-rank matrices `B` and `\widetilde B=D_1^*BD_2`, the Frobenius change of the unitary polar factor is controlled by the distances of `D_1,D_2` and their inverses from the identity, with no dependence on the singular values of `B`.

For the square full-rank specialization `D_2=I` used here, Li's Theorem 1 gives

\[
\boxed{
\|W_1-W\|_{\mathcal S_2}
\le
\left(
\|D_1-I\|_{\mathcal S_2}^2
+
\|I-D_1^{-1}\|_{\mathcal S_2}^2
\right)^{1/2}.
}
\tag{14}
\]

The source is R.-C. Li, *Relative perturbation bounds for the unitary polar factor*, BIT Numerical Mathematics **37** (1997), 67--75, DOI `10.1007/BF02510173`; the same theorem appears as Theorem 1 in LAPACK Working Note 83, UT-CS-94-251 (revised January 1996), `https://www.netlib.org/lapack/lawnspdf/lawn83.pdf`.

The important point for the present application is not merely continuity of the polar decomposition. Equation (14) is a **relative multiplicative** bound, which is why the smallest singular value of `B` and the condition of `Q` disappear.

## 3. Positive completion controls both relative perturbation factors with constant one

Because

\[
H=I+K\ge I,
\qquad
H_1=VH V^*\ge I,
\]

one has

\[
S\ge I,\qquad S_1\ge I,
\qquad
\|S^{-1}\|,\|S_1^{-1}\|\le1.
\tag{15}
\]

From (13),

\[
D_1-I=S^{-1}(S_1-S),
\tag{16}
\]

while

\[
I-D_1^{-1}
=I-S_1^{-1}S
=S_1^{-1}(S_1-S).
\tag{17}
\]

Therefore

\[
\boxed{
\|D_1-I\|_{\mathcal S_2}
\le\|S_1-S\|_{\mathcal S_2},
\qquad
\|I-D_1^{-1}\|_{\mathcal S_2}
\le\|S_1-S\|_{\mathcal S_2}.
}
\tag{18}
\]

No upper bound on `S` or `K` appears.

The square-root difference is also uniformly contractive in this positive-completion regime. Let

\[
Y=S_1-S.
\]

Since `S_1^2-S^2=H_1-H`,

\[
S_1Y+YS=H_1-H.
\tag{19}
\]

Diagonalize `S_1` on the left and `S` on the right. Every matrix coefficient of the Sylvester map in (19) is multiplied by `s_{1,i}+s_j\ge2`. Hence

\[
\boxed{
\|S_1-S\|_{\mathcal S_2}
\le\frac12\|H_1-H\|_{\mathcal S_2}.
}
\tag{20}
\]

But

\[
H_1-H=VKV^*-K=(VK-KV)V^*,
\tag{21}
\]

so unitary invariance gives

\[
\|H_1-H\|_{\mathcal S_2}
=\|[K,V]\|_{\mathcal S_2}.
\tag{22}
\]

Combining (14), (18), and (20)--(22),

\[
\|W_1-W\|_{\mathcal S_2}
\le\sqrt2\|S_1-S\|_{\mathcal S_2}
\le\frac1{\sqrt2}\|[K,V]\|_{\mathcal S_2}.
\tag{23}
\]

Finally, (9) and (12) imply

\[
\|W_1-W\|_{\mathcal S_2}
=\|VU^*V^*-U^*\|_{\mathcal S_2}
=\|[U,V]\|_{\mathcal S_2},
\]

which proves (1).

For a bounded self-adjoint `X` commuting with `Q`, apply (1) to `V_t=e^{itX}`, divide by `|t|`, and let `t\to0` in the finite-dimensional section. This gives (2).

## 4. Prime-Flute consequence: PF-335's envelope is an artifact of stopping at `F`

PF-335 proves the useful but stronger intermediate estimate

\[
\|[F,V]\|_{\mathcal S_2}
\le
\frac{\sqrt{1+\|K\|}}{\sqrt2}
\|[K,V]\|_{\mathcal S_2}.
\tag{24}
\]

That estimate remains correct. It says the **nonunitary whitening map** can carry the size of its positive factor `S=(I+K)^{1/2}`. But the packet accounting in PF-330 and the locality reduction in PF-331 ultimately require the unitary polar rotation `U`, not a uniform bound on the full nonunitary `F`.

Equation (1) shows that passing through (24) is unnecessarily expensive for the translation branch. The large positive amplitude in `S` is exactly the component discarded by polar extraction, and relative polar perturbation sees only the multiplicative mismatch between `S_1` and `S`. Because both are bounded below by the identity, that mismatch is controlled by the square-root Sylvester equation with no upper envelope.

For the canonical Prime-Flute finite low section,

\[
K_n
=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2},
\]

and PF-325 gives `[Q_{L,n},\tau_t]=0`. Therefore (3) is uniform in retained rank and seam condition. The obstruction-side translation gate can now be stated without the first PF-335 hypothesis:

\[
\boxed{
\sup_{t\in I_n}
\left\|
Q_{L,n}^{-1/2}
[\Lambda_{LL,n},\tau_t]
Q_{L,n}^{-1/2}
\right\|_{\mathcal S_2}
=o(1).
}
\tag{25}
\]

If (25) holds, then the completed polar rotation is translation-compatible in operator norm on the same critical interval. What remains is to prove (25) from the actual one-cusp-pant/core DtN geometry and to supply a sufficiently concentrated completed reference profile, or instead prove the stronger fixed-window locality needed to avoid the reference-profile step.

## Prior-art and novelty audit

The abstract mechanism in this finding is **classical**, not a new polar-decomposition theorem. Li's 1997 result was designed precisely to remove smallest-singular-value dependence for multiplicative perturbations `\widetilde B=D_1^*BD_2`; later work on unitary, subunitary, generalized, and weighted polar factors extends the same perturbation program. The present proof uses only the square full-rank Frobenius specialization of Li's Theorem 1 together with the elementary Sylvester estimate (20).

A targeted audit found the expected surrounding literature: R.-C. Li, *New perturbation bounds for the unitary polar factor*, SIAM J. Matrix Anal. Appl. 16 (1995), 327--332; W. Li and W. Sun, *Perturbation bounds of unitary and subunitary polar factors*, SIAM J. Matrix Anal. Appl. 23 (2002), 1183--1193; W. Li and W. Sun, *New perturbation bounds for unitary polar factors*, SIAM J. Matrix Anal. Appl. 25 (2003), 362--372; and weighted extensions such as H. Yang and H. Li, *Perturbation bounds for weighted polar decomposition in the weighted unitarily invariant norm*, Numer. Linear Algebra Appl. 15 (2008), 685--700.

No novelty is claimed for those matrix perturbation estimates. The project-specific contribution is the exact identification

\[
U^*=\operatorname{polar}(\sqrt{I+K}\,Q^{1/2})
\]

and the observation that physical translation conjugation is a one-sided relative perturbation whose two multiplicative errors are both absorbed by `I+K\ge I`. That specialization removes the `\sup\|K_n\|` envelope from the **actual Prime-Flute polar transport gate**, even though the envelope remains present in PF-335's stronger estimate for `F` itself.

The Li theorem is used at the finite-section level exactly within its full-rank matrix hypotheses. No infinite-dimensional extension of Li's theorem is asserted here.

## Boundaries and adversarial checks

1. **The normalized pant commutator is still the hard theorem.** Equation (25) is a reduction, not an estimate for the actual DtN block.
2. **Translation locality still does not imply spatial concentration.** `\tau_t` commutes with `Q`; a fixed physical cutoff generally does not. PF-331's cutoff route remains unresolved.
3. **No uniform bound on `K_n` is proved or needed for (3).** PF-336 removes that hypothesis only from the polar-translation transfer. Other arguments that need `F_n` itself, its positive factor, or an operator envelope for the normalized pant response are unaffected.
4. **Finite sections are essential to the stated imported theorem.** Passing the resulting packet/locality statement to an infinite boundary realization still requires the compatible limit already present in PF-329--PF-335.
5. **The constant `1/\sqrt2` is sufficient, not asserted sharp.** Sharpening the matrix constant has no current effect on the endpoint logic.
6. **The direct upper-bound route is unchanged.** PF-317--PF-321 may still close the weak-`S_1` endpoint by local angle estimates without using this obstruction-side translation argument.
7. **No completed correlation lower bound is proved.** The PF-324 finite-boundary/escaping-boundary arithmetic regimes still need to be tested after locality and concentration are established.
8. **No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication follows.**

## Consequence for the research line

PF-335 left two translation-side operator hypotheses: a uniform envelope for `K_n` and a Hilbert--Schmidt translation-commutator estimate. PF-336 removes the first one at the level that actually rotates the critical packets. The clean remaining transport statement is now

\[
\sup_{t\in I_n}\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1)
\quad\Longrightarrow\quad
\sup_{t\in I_n}\|[U_n,\tau_t]\|=o(1),
\]

with no retained-rank, seam-conditioning, or `\|K_n\|` loss. The next substantive obstruction-side target is therefore geometric/PDE control of the normalized pant insertion commutator (25), followed by concentration of one completed reference profile. There is no remaining reason to prove a separate uniform operator envelope merely to transport physical translations through the completed polar factor.