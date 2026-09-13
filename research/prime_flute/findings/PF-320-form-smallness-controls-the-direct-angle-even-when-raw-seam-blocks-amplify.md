# PF-320 — form smallness controls the direct angle even when raw seam blocks amplify

**Status:** `EXACT-DERIVED + CLASSICAL-BLOCK-FACTORISATION + PERTURBATIVE-ANGLE-STABILITY + POSITIVE/ROUTE-NARROWING`.

PF-319 proves that PF-232's reciprocal-prime form-smallness cannot be pushed directly through an unrelated seam normalizer to control the raw mixed block

\[
L\,Q^{-1/2}(\Lambda_1-\Lambda_0)Q^{-1/2}H.
\]

That obstruction is real for the **raw normalized precision**, but it does not survive the extra diagonal normalization in the actual PF-315/PF-317 direct angle. A positive block form carries its own low/high energy metric, and multiplicative closeness of two positive forms controls their energy-normalized cross angles independently of how anisotropic an external seam metric is.

More precisely, let

\[
M_j=
\begin{pmatrix}
A_j&B_j\\
B_j^*&C_j
\end{pmatrix}>0,
\qquad
T_j:=A_j^{-1/2}B_jC_j^{-1/2},
\qquad j=0,1,
\]

on a finite low/high section. Assume

\[
(1-\varepsilon)M_0\le M_1\le(1+\delta)M_0.
\]

Then `T_0,T_1` are contractions and there are unitaries `U_L,U_H`, acting only inside the low and high sectors, such that

\[
\boxed{
\|U_L^*T_1U_H-T_0\|
\le
2\tau\kappa^2+d(\kappa+1),
}
\]

where

\[
\tau=\max\{\varepsilon,\delta\},
\qquad
\kappa=(1-\varepsilon)^{-1/2},
\qquad
d=\max\!\left\{\kappa-1,\,1-(1+\delta)^{-1/2}\right\}.
\]

For the exact PF-232 constants

\[
\varepsilon=\beta,
\qquad
\delta=\beta+\beta^2,
\qquad
0\le\beta\le\frac12,
\]

this simplifies to

\[
\boxed{
\|U_L^*T_1U_H-T_0\|\le 9\beta.
}
\]

If the low sector has rank `r`, the perturbation therefore has the mean-square bound

\[
\boxed{
\|U_L^*T_1U_H-T_0\|_{\mathcal S_2}^2
\le81r\beta^2.
}
\]

For a canonical prime-flute pant, PF-210 gives `r=O(1+\log P_n)` and PF-232 gives `\beta_n=O(P_n^{-1})`. Thus the hypercycle straightening changes the **local direct angle itself** by at most

\[
\boxed{
O\!\left(\frac{1+\log P_n}{P_n^2}\right)
}
\]

in squared Hilbert--Schmidt mass — exactly the PF-318 endpoint budget. This estimate is independent of the corridor/seam metric mismatch that defeats the raw-block shortcut in PF-319.

There is a second structural point. A sum of positive local pant forms has a global low/high angle that is a contraction sandwich of the orthogonal direct sum of the local angles. Hence one may distribute the identity part of `I+K` among the finitely overlapping pant blocks, estimate each local angle in its **own diagonal energy**, and reassemble without returning to the raw `K_{LH}` block. Common positive finite-pant completion may be left untouched: adding the same positive form to the sheared and shear-deleted corridor preserves PF-232's multiplicative sandwich before taking the DtN minimum.

Consequently the current direct-angle route can be narrowed again. The shear no longer has to be transported through PF-242/PF-255 into the final seam-normalized physical-frequency representation merely to recover reciprocal-prime leakage. A sufficient remaining theorem is an endpoint bound for the **shear-deleted local pant angles**, with the actual seam normalization and the full common finite-pant completion retained. PF-319 remains a correct obstruction to proving the stronger raw `K_{LH}` estimate from form-smallness alone; PF-320 bypasses that stronger target rather than contradicting it.

## 1. Relative positive forms have Lipschitz-stable cross angles

Work first in a finite-dimensional/Galerkin low/high section, exactly as in PF-317. Write

\[
M_j=
\begin{pmatrix}
A_j&B_j\\
B_j^*&C_j
\end{pmatrix}>0.
\tag{1}
\]

Positivity gives the standard contraction factorization

\[
B_j=A_j^{1/2}T_jC_j^{1/2},
\qquad
\|T_j\|\le1.
\tag{2}
\]

Assume

\[
(1-\varepsilon)M_0\le M_1\le(1+\delta)M_0,
\qquad 0\le\varepsilon<1,\quad\delta\ge0.
\tag{3}
\]

Normalize by the **diagonal blocks of `M_0`**, not by an external metric:

\[
S=\operatorname{diag}(A_0^{-1/2},C_0^{-1/2}).
\tag{4}
\]

Then

\[
\widehat M_0=SM_0S
=
\begin{pmatrix}
I&T_0\\
T_0^*&I
\end{pmatrix},
\tag{5}
\]

while

\[
\widehat M_1=SM_1S
=
\begin{pmatrix}
A&B\\
B^*&C
\end{pmatrix}
\tag{6}
\]

satisfies the same sandwich

\[
(1-\varepsilon)\widehat M_0
\le\widehat M_1
\le(1+\delta)\widehat M_0.
\tag{7}
\]

Since `\|T_0\|\le1`,

\[
\|\widehat M_0\|\le2.
\tag{8}
\]

Put `\Delta=\widehat M_1-\widehat M_0` and `\tau=\max\{\varepsilon,\delta\}`. From (7), for every unit vector `x`,

\[
|\langle x,\Delta x\rangle|
\le\tau\langle x,\widehat M_0x\rangle
\le2\tau,
\]

hence

\[
\boxed{\|\Delta\|\le2\tau.}
\tag{9}
\]

In particular

\[
\|B-T_0\|\le2\tau.
\tag{10}
\]

Compressing (7) to the diagonal sectors gives

\[
(1-\varepsilon)I\le A,C\le(1+\delta)I.
\tag{11}
\]

Set

\[
\kappa=(1-\varepsilon)^{-1/2},
\qquad
d=\max\!\left\{\kappa-1,\,1-(1+\delta)^{-1/2}\right\}.
\tag{12}
\]

Then

\[
\|A^{-1/2}\|,\|C^{-1/2}\|\le\kappa,
\qquad
\|A^{-1/2}-I\|,\|C^{-1/2}-I\|\le d.
\tag{13}
\]

Define the angle of `\widehat M_1` by

\[
\widehat T_1=A^{-1/2}BC^{-1/2}.
\tag{14}
\]

Equations (10)--(13) give

\[
\begin{aligned}
\|\widehat T_1-T_0\|
&\le
\|A^{-1/2}(B-T_0)C^{-1/2}\|\\
&\quad+\|(A^{-1/2}-I)T_0C^{-1/2}\|
+\|T_0(C^{-1/2}-I)\|\\
&\le2\tau\kappa^2+d(\kappa+1).
\end{aligned}
\tag{15}
\]

The normalization in (4) changes the angle only by left/right unitaries. Indeed, with

\[
U_L=A_1^{1/2}A_0^{-1/2}A^{-1/2},
\qquad
U_H=C_1^{1/2}C_0^{-1/2}C^{-1/2},
\tag{16}
\]

direct multiplication shows `U_L,U_H` are unitary and

\[
\boxed{\widehat T_1=U_L^*T_1U_H.}
\tag{17}
\]

This proves the general bound.

For PF-232 take

\[
\varepsilon=\beta,
\qquad
\delta=\beta+\beta^2.
\tag{18}
\]

If `\beta\le1/2`, then

\[
\tau\le\frac32\beta,
\qquad
\kappa^2\le2,
\qquad
\kappa\le\sqrt2,
\qquad
d\le\beta.
\tag{19}
\]

Substitution into (15) gives the convenient uniform estimate

\[
\boxed{
\|U_L^*T_1U_H-T_0\|\le9\beta.
}
\tag{20}
\]

If the low target has dimension `r`, the difference in (20) has rank at most `r`, hence

\[
\boxed{
\|U_L^*T_1U_H-T_0\|_{\mathcal S_2}^2
\le81r\beta^2.
}
\tag{21}
\]

The argument is uniform in the finite section. It therefore supplies the same finite-section-compatible bound used throughout PF-311/PF-317/PF-318; no unbounded raw cross operator is required.

## 2. Common positive completion cannot spoil the sandwich

PF-232 derives its comparison on the straightened neighboring-cuff corridor. Let `c_0,c_1` be the shear-deleted and actual corridor bulk forms and let `r\ge0` denote **any common positive remainder** of the pant construction: cusp-side completion, another unchanged geometric region, or an auxiliary positive term. If

\[
(1-\beta)c_0\le c_1\le(1+\beta+\beta^2)c_0,
\tag{22}
\]

then trivially

\[
(1-\beta)(r+c_0)
\le r+c_1
\le(1+\beta+\beta^2)(r+c_0).
\tag{23}
\]

Taking the variational infimum over all interior extensions with a fixed external boundary trace preserves the order, so the corresponding full local DtN forms obey the same inequality. Congruence by **any fixed positive seam form `Q`** preserves it again. Finally, adding the same positive block-diagonal identity share `W` gives

\[
(1-\beta)M_0\le M_1\le(1+\beta+\beta^2)M_0,
\tag{24}
\]

for

\[
M_j=W+Q^{-1/2}\Lambda_jQ^{-1/2}.
\tag{25}
\]

Thus the angle estimate (20) is insensitive to the exact seam/corridor scale mismatch and to any common finite-pant completion. Those features still matter for the **reference angle `T_0`**, but they cannot amplify the shear correction beyond `O(\beta)` once the cross term is measured in the local diagonal energies of `M_j`.

This is precisely where PF-319's countermodel stops applying. PF-319 shows that

\[
Q^{-1/2}(\Lambda_1-\Lambda_0)Q^{-1/2}
\]

may be large even when `\Lambda_1` and `\Lambda_0` are relatively close. Equation (20) does not bound that raw operator. It bounds the intrinsic correlation operator after the **same form's own diagonal blocks** have been divided out.

## 3. Positive local forms reassemble by contraction sandwich

Let a finite section of the direct nonconstant boundary problem have positive local contributions

\[
M_e=
\begin{pmatrix}
A_e&B_e\\
B_e^*&C_e
\end{pmatrix}\ge0,
\qquad
M=\sum_eM_e
=
\begin{pmatrix}
A&B\\
B^*&C
\end{pmatrix}.
\tag{26}
\]

Use the standard positive-block factorization

\[
B_e=A_e^{1/2}T_eC_e^{1/2},
\qquad \|T_e\|\le1.
\tag{27}
\]

On the supports of `A,C`, define

\[
X_Lx=\bigoplus_e A_e^{1/2}A^{-1/2}x,
\qquad
X_Hy=\bigoplus_e C_e^{1/2}C^{-1/2}y.
\tag{28}
\]

Then

\[
X_L^*X_L=I,
\qquad
X_H^*X_H=I,
\tag{29}
\]

and the global angle is exactly

\[
\boxed{
A^{-1/2}BC^{-1/2}
=X_L^*\left(\bigoplus_eT_e\right)X_H.
}
\tag{30}
\]

Therefore every two-sided symmetric ideal estimate for the orthogonal direct sum of the local angles passes to the global angle. This is the correct localization principle for positive forms: localize **after intrinsic diagonal normalization**, rather than asking the raw externally normalized cross block to be small.

For `I+K` in PF-317, choose any nonnegative block-diagonal partition of the identity among the finitely incident pant blocks, `I=\sum_eW_e`, with each `W_e` commuting with the physical `L/H` split, and put

\[
M_e=W_e+K_e.
\tag{31}
\]

Then (30) applies and the sum is exactly the global direct precision. Different harmless choices of the positive identity partition change the local reference angles but not the validity of the contraction-sandwich implication.

## 4. The PF-232 shear already fits the PF-318 mean-square budget at angle level

Apply the previous sections to one canonical local pant contribution. Let `T_{0,n}` be the local physical `L/H` angle for the **shear-deleted** straightened corridor, retaining the actual seam normalization and all common positive pant completion, and let `T_{1,n}` be the corresponding actual hypercycle-straightened angle.

PF-232 gives, on the tail,

\[
\beta_n\le\frac{C}{P_n}.
\tag{32}
\]

PF-210/PF-317 give for every one of the finitely many neighboring low targets

\[
r_n:=\dim L_n\le C_\kappa(1+\log P_n).
\tag{33}
\]

Hence (21) yields unitaries within the local physical low/high sectors such that

\[
\boxed{
\|U_{L,n}^*T_{1,n}U_{H,n}-T_{0,n}\|_{\mathcal S_2}^2
\le
C\frac{1+\log P_n}{P_n^2}.
}
\tag{34}
\]

The unitaries do not alter singular values, rank, or any symmetric-ideal membership. PF-318's threshold-counting argument therefore applies to the direct sum of these **shear-error angles** across the canonical tail; finite pant incidence and the three neighboring offsets only multiply the constant. In particular the shear-error family is weak trace class at exactly the budget already known to be sufficient for the direct endpoint.

Equation (34) is stronger for the present purpose than PF-242's raw Pöschl--Teller cut locality: it is stated in the intrinsic low/high angle metric itself and needs no conversion from corridor energy to seam energy. PF-242/PF-255 remain useful structural information, but they are no longer required merely to prevent the PF-232 shear from breaking the direct-angle endpoint.

## 5. Remaining direct-angle gate

PF-320 does **not** prove the full direct angle is weak trace class. By (30) and (34), a sufficient remaining target is now:

> prove a weak-`S_1`-compatible singular-value envelope for the orthogonal direct sum of the **shear-deleted local pant angles** `T_{0,n}`, using the actual seam form and retaining the full common finite-pant completion.

Once that reference family is in `\mathcal S_{1,\infty}`, adding the local shear-error family from (34) keeps the direct angle in `\mathcal S_{1,\infty}`, and the contraction sandwich (30) passes the estimate to the global direct angle.

This is a genuine reduction of the live PDE problem. The shear no longer needs a same-seam-metric raw `K_{LH}` estimate. The remaining nontrivial ingredients are the shear-deleted variable-width/diagonal corridor, its physical-frequency relation to the actual seam energy, and the finite one-cusp-pant completion. PF-233/PF-238 already constrain the first two at the transfer level, but no current finding proves the required local physical `L/H` angle envelope with completion.

The independent conditional post-low angle `T_H` from PF-315/PF-316 is unchanged by this finding.

## Prior-art and novelty audit

The abstract ingredients are classical operator theory, not a claimed new general theorem. Positivity of a `2x2` block operator matrix is equivalent to factorization of the off-diagonal block through a contraction; this is standard Douglas-factorization/positive-block machinery. See R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proc. Amer. Math. Soc. **17** (1966), 413--415, DOI `10.1090/S0002-9939-1966-0203464-1`. Modern block-operator treatments use the same contraction factorization.

The project-specific content is the quantitative use of multiplicative PF-232 form control **at the intrinsic direct-angle level**, the observation that arbitrary common positive pant completion preserves the sandwich, and the PF-210/PF-318 prime-scale consequence (34). No novelty is claimed for Douglas factorization or for elementary perturbation estimates of positive block matrices.

The closest stored results are PF-239 and PF-319. PF-239 applies operator monotonicity to the full normalized resolvent and gets `O(\beta_n)` control for low-touch inverse errors; it does not address the PF-315/PF-317 direct angle. PF-319 correctly proves failure of transferring form-smallness to a raw block normalized by another metric. PF-320 identifies why the actual angle is better behaved: its own diagonal energies absorb exactly the anisotropy that PF-319's raw-block countermodel can amplify.

## Falsification and boundary conditions

The proof depends on **multiplicative order of the whole local positive form**. An additive error bound in an unrelated norm is not enough. The same seam normalizer and the same common completion must be used on both sides before the comparison.

The local-to-global implication (30) is one-way: a good global angle does not force every chosen local angle to be good. PF-320 therefore supplies a sufficient localization route, not a necessary characterization.

The `9\beta` constant is deliberately nonsharp. Only the uniform `O(\beta)` scale matters. If future work finds a local regime with `\beta` not below `1/2`, that finite head is handled separately; the canonical tail has `\beta_n=O(P_n^{-1})`.

Finally, PF-320 does not establish the weak-`S_1` bound for the shear-deleted local pant-angle family and makes no claim about the separate conditional angle `T_H`, scattering, determinants, zeta zeros, or RH.