# PF-189 — the complete short-collar central sector is weak trace class at the sharp endpoint

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-171 proves that the orthogonal Dirichlet direct sum of all fixed-central Margulis-short prime/shift collar blocks belongs to every Schatten class `S_r`, `r>1`, but not to `S_1`. That leaves open whether the intersection over all `r>1` hides a worse-than-critical endpoint. It does not. The same separated-variable model gives a uniform weak-trace estimate for each matched collar,

\[
\|A_\eta\|_{\mathcal S_{1,\infty}}^{\#}
\le C_R |t_\eta|L_\eta,
\]

where `t_eta=log(L_eta^+/L_eta)` and `||.||^#` is the singular-value counting quasi-norm. PF-109 and PF-138 then make these weak-endpoint masses absolutely summable over the complete short family. Consequently the full decoupled central sector lies in `S_{1,infinity}` while PF-171 keeps it outside `S_1`. Thus the short-collar sector reaches the canonical two-dimensional critical ideal exactly; any global first-relative-resolvent behavior worse than weak trace class must be created by body/interface/uncut assembly, not by the complete collapsing central family.

## Claim

Use the notation and one fixed central half-width `R>0` of PF-169/PF-171. For every Margulis-short core `eta`, let

\[
A_\eta
=(\Delta_{\eta,+,R}^D+1)^{-1}
-(\Delta_{\eta,R}^D+1)^{-1},
\qquad
L_\eta=\ell(\eta),
\qquad
t_\eta=\log\frac{L_\eta^+}{L_\eta}.
\tag{1}
\]

For a compact operator `T`, write

\[
N_T(\sigma):=\#\{j:s_j(T)>\sigma\},
\qquad
\|T\|_{1,\infty}^{\#}:=
\sup_{\sigma>0}\sigma N_T(\sigma).
\tag{2}
\]

This is an equivalent weak-Schatten `S_{1,infinity}` quasi-norm. There is a constant `C_R` on the canonical tail such that

\[
\boxed{
\|A_\eta\|_{1,\infty}^{\#}
\le C_R |t_\eta|L_\eta.
}
\tag{3}
\]

After absorbing the finite exceptional head into the constant, the complete Dirichlet-decoupled central operator

\[
A_{\rm thin}^D:=\bigoplus_{\eta\in\mathcal S}A_\eta
\tag{4}
\]

satisfies

\[
\boxed{
A_{\rm thin}^D\in\mathcal S_{1,\infty}.
}
\tag{5}
\]

If `S_{>=Q}` is the PF-171 tail whose left exterior prime label is at least `Q`, and `theta=0.525` is the PF-138 counting exponent, then

\[
\boxed{
\left\|
\bigoplus_{\eta\in\mathcal S_{\ge Q}}A_\eta
\right\|_{1,\infty}^{\#}
\le C_R Q^{\theta-2}
=C_R Q^{-1.475}.
}
\tag{6}
\]

Together with PF-171,

\[
\boxed{
A_{\rm thin}^D
\in\mathcal S_{1,\infty}\setminus\mathcal S_1.
}
\tag{7}
\]

Equations (5)--(7) concern only the orthogonal fixed-central Dirichlet model. They do not imply weak-trace membership of the uncut full-surface relative resolvent.

## 1. One Fourier block has the critical counting bound

PF-127 places both matched collar Laplacians on the common measure and decomposes them into angular Fourier modes. For `m in Z`,

\[
H_{m,L}
=H_0+\frac{(2\pi m)^2}{L^2}\operatorname{sech}^2r,
\tag{8}
\]

on the fixed interval `[-R,R]` with Dirichlet boundary. The `m=0` block is independent of `L`, so its relative resolvent is exactly zero.

For `m ne 0`, put

\[
R_{m,L}:=(H_{m,L}+1)^{-1}.
\tag{9}
\]

PF-127's fixed-interval min-max estimate gives, uniformly in the collapsing length,

\[
s_k(R_{m,L})
\le
\frac{C_R}{k^2+(m/L)^2},
\qquad k\ge1.
\tag{10}
\]

For `L^+=e^tL` with bounded `|t|`, the centrifugal-potential difference satisfies

\[
\|V_m\|_\infty
\le C_R|t|(m/L)^2,
\qquad
\|R_{m,L}\|
\le C_R(L/|m|)^2.
\tag{11}
\]

Hence

\[
\|V_mR_{m,L}\|
\le C_R|t|.
\tag{12}
\]

The resolvent identity

\[
A_m=R_{m,L^+}V_mR_{m,L}
\tag{13}
\]

and the ideal singular-value inequality `s_k(BC)<=||C||s_k(B)` now give the stronger pointwise estimate behind PF-127's `S_r` sum:

\[
\boxed{
s_k(A_m)
\le
\frac{C_R|t|}{k^2+(m/L)^2}
\qquad(m\ne0).
}
\tag{14}
\]

No interpolation in the Schatten exponent is used here.

## 2. Elliptic lattice counting produces exactly one power of `L`

Fix `sigma>0` and put

\[
\Lambda^2:=\frac{C_R|t|}{\sigma}.
\tag{15}
\]

Equation (14) shows that a singular value from Fourier mode `m ne 0` and radial index `k>=1` can exceed `sigma` only if

\[
k^2+(m/L)^2<\Lambda^2.
\tag{16}
\]

There are at most `2 L Lambda` possible nonzero integers `m`, and for each such `m` at most `Lambda` possible radial indices. If `L Lambda<1` there is no nonzero angular mode at all, so the same bound remains valid. Therefore

\[
N_{A_{L,L^+}^{(R)}}(\sigma)
\le
2L\Lambda^2
\le
\frac{C_R|t|L}{\sigma}.
\tag{17}
\]

Taking the supremum of `sigma N(sigma)` proves (3).

The factor `L` has a simple phase-space meaning. The critical two-dimensional `j^{-1}` tail is still present for every nontrivial collar, but the angular-frequency lattice has spacing `1/L`; as the core pinches, fewer transverse modes lie below a fixed frequency threshold. Collapse therefore suppresses the **coefficient** of the weak-trace tail without changing its critical exponent.

This is compatible with PF-112/PF-127: when `t ne 0`, a compactly supported localization still has nonzero order-`-2` principal symbol and `c/j` singular-value asymptotics, so trace class remains impossible even though the weak endpoint coefficient tends to zero with `L`.

## 3. The complete short family has summable weak-endpoint mass

For an orthogonal direct sum, the singular-value counting functions add exactly:

\[
N_{\oplus_\eta A_\eta}(\sigma)
=
\sum_\eta N_{A_\eta}(\sigma).
\tag{18}
\]

Thus (3) implies

\[
\left\|\bigoplus_{\eta\in E}A_\eta\right\|_{1,\infty}^{\#}
\le
C_R\sum_{\eta\in E}|t_\eta|L_\eta
\tag{19}
\]

for every subfamily `E` of the canonical tail.

PF-138 gives `L_eta<=mu_*` and at most

\[
N(P)=O(P^\theta),
\qquad\theta=0.525,
\tag{20}
\]

short canonical separators with left exterior prime label `P`. PF-109 gives uniformly on that entire family

\[
|t_\eta|=O(P^{-3}).
\tag{21}
\]

Consequently

\[
\sum_{\eta\in\mathcal S_{\rm tail}}|t_\eta|L_\eta
\le
C\sum_{P\ {\rm prime}}P^{\theta-3}
<\infty.
\tag{22}
\]

The finite head contributes a finite weak-Schatten constant by the ordinary compact local pseudodifferential theory already audited in PF-112. Equations (18)--(22) prove (5).

Restricting to `P>=Q` and bounding the prime sum by the integer sum gives

\[
\sum_{P\ge Q}P^{\theta-3}
\le C Q^{\theta-2},
\tag{23}
\]

which proves the vanishing weak-endpoint tail estimate (6).

## 4. The endpoint is genuinely weak, not trace class

PF-171 already proves that the complete central direct sum is not trace class. The reason is local and survives the stronger upper bound above: PF-005 supplies pinching canonical blocks and PF-170 makes the matched shift length nontrivial there, while PF-127/PF-112 give the critical `c/j` singular-value tail for every such genuinely changed collar.

If `A_thin^D` were trace class, compression to one nontrivial collar summand would be trace class, contradicting that local asymptotic. Therefore (7) follows.

The combination

\[
\boxed{
\text{weak }S_1\text{ globally on the decoupled thin sector}
\quad+\quad
\text{not }S_1\text{ even locally}
}
\tag{24}
\]

is sharper than merely recording membership in every `S_r`, `r>1`: it identifies the natural critical ideal in which the whole short-collar central family lives.

## 5. Consequence for the sharp-Schatten program

PF-171 already says that no exponent `r>1` is lost in the complete central thin sector. PF-189 strengthens that boundary conclusion. Even at the critical exponent, the entire decoupled sector has controlled weak-trace mass, with a tail tending to zero as `Q^{-1.475}`.

Therefore a future failure of weak `S_1` for the **uncut** first relative resolvent cannot be attributed to the mere presence, pinching, or multiplicity of the canonical Margulis-short cores. It would have to be generated by a channel absent from the orthogonal central model: body metric defect, collar/body transmission, cutoff commutators, or nonlocal reassembly.

Conversely, (5) does not solve the accepted `S_r`, `r>1`, clue. Weak `S_1` is not trace class and does not by itself provide the trace-class perturbation theory required for ordinary spectral shift, Fredholm determinants, or Kato--Rosenblum. The current geometric splice gate PF-183--PF-188 therefore remains live.

## 6. Prior art and novelty audit

No novelty is claimed for weak Schatten ideals or for the fact that order `-d` classical pseudodifferential operators naturally sit at the weak-trace endpoint. PF-112 already audits the relevant Birman--Solomyak singular-value Weyl law and the Kalton--Lord--Potapov--Sukochev/Connes weak-trace context, and PF-127 already derives the separated hyperbolic-collar resolvent estimates used here.

No additional external theorem is imported in PF-189. The new step is the direct lattice-counting consequence of PF-127's modewise model, followed by PF-138's complete-family multiplicity bound and PF-109's uniform `P^{-3}` matching. A directed search around weak-trace resolvent differences on degenerating hyperbolic collars found the general critical pseudodifferential and degeneration literature but no source supplying this project-specific uniform `|t|L` weak bound together with the complete prime/shift short-family summation. Search absence is not treated as a novelty theorem.

## 7. Audit / falsification core

A later adversary can check PF-189 through the following finite chain:

1. use PF-169/PF-171 to fix one central width `R` for the complete short family;
2. repeat PF-127's common-measure Fourier decomposition and verify exact cancellation of `m=0`;
3. use the fixed-interval eigenvalue bound to obtain (10) for the target resolvent as well as the source;
4. combine the exact centrifugal-potential difference with the source resolvent operator norm to verify (12);
5. apply the singular-value ideal inequality to obtain the pointwise mode estimate (14);
6. count integer pairs satisfying (16) and verify the uniform `C|t|L/sigma` counting bound (17), including the regime `L Lambda<1` where no nonzero angular mode contributes;
7. add counting functions for the orthogonal direct sum, insert PF-109 and PF-138, and sum `P^{theta-3}` to obtain (5)--(6);
8. use PF-171/PF-112 for non-`S_1`; do not infer trace-class consequences from weak `S_1`;
9. preserve the decoupling boundary: no claim about the uncut full-surface relative resolvent is made until body/interface/transmission terms are controlled.

A refutation would need to break the modewise singular-value bound, the elliptic lattice count, PF-109's uniform length matching, PF-138's complete short-core count, or the exact orthogonal direct-sum counting identity. Failure of the later global splice does not refute PF-189; it would identify precisely the noncentral mechanism excluded from this endpoint calculation.