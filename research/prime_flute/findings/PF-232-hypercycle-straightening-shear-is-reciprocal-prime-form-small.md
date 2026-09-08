# PF-232 — hypercycle straightening shear is reciprocal-prime form-small

**Status:** `EXACT-DERIVED + FORM-COMPARISON + POSITIVE/ROUTE-NARROWING`. PF-231 puts the neighboring ultraparallel corridor into exact logarithmic coordinates and then straightens the PF-205 inward hypercycle boundaries onto the fixed strip `(0,1) x (0,pi)`. In that formula the coefficient `b_s/a_s` can stay order one, so PF-231 correctly refused to call the transformed operator a small coefficient perturbation. The full quadratic form has a sharper normalization, however: after measuring transverse and tangential derivatives in their natural thin-strip energy scales, the cross term is controlled by `b_s` itself, not by `b_s/a_s`.

For the actual PF-205 offsets, `b_s` is uniformly at most the seam Fermi-area halfwidth. More precisely, if the two inward hyperbolic distances are `rho_1,rho_2`, put

\[
w_i:=\sinh\rho_i,
\qquad
\beta:=\max(w_1,w_2).
\]

Then the exact PF-231 straightened form differs from its variable-width diagonal part by only a relative `O(beta)` form error. In the canonical prime-flute family `rho_i=arsinh(w_i)` with `w_i=kappa d_i=O(P_i^{-1})`, so this geometric shear error is **reciprocal-prime small**, even on the critical tangential band of scale `1/s`. The only geometric deformation that can remain order one in relative form size is the width loss `(rho_1+rho_2)/s`, which is already the seam-to-corridor scale controlled in PF-205/PF-230.

This does **not** prove PF-228's normalized `w/s` dressed cross-block estimate. Loewner comparison of the full two-boundary energy DtN form does not compare its off-diagonal block, does not commute with the real seam normalizers, and does not settle the finite-pant completion or the physical `P/H` projections. The result instead removes one candidate obstruction: the apparent order-one `b_s/a_s` coupling created by graph straightening is not an order-one perturbation in the natural energy metric.

## Claim

Let

\[
f_i(\theta)
:=\operatorname{arsinh}(\sinh\rho_i\,\sin\theta),
\qquad
0<\theta<\pi,
\]

and suppose

\[
0<\rho_1+\rho_2<s.
\]

As in PF-231, define

\[
a(\theta):=s-f_1(\theta)-f_2(\theta),
\qquad
x=f_1(\theta)+a(\theta)X,
\qquad 0<X<1,
\]

and

\[
b(X,\theta):=f_1'(\theta)+a'(\theta)X.
\]

On the fixed strip let

\[
\mathfrak q_{\rm hyp}[v]
:=\int_0^1\!\int_0^\pi
\left[
 a^{-1}|v_X|^2
 +a\left|v_\theta-\frac ba v_X\right|^2
 +a\csc^2\theta\,|v|^2
\right]d\theta\,dX
\tag{1}
\]

be the exact shifted hyperbolic form from PF-231. Define its diagonal variable-width comparison

\[
\mathfrak q_{\rm diag}[v]
:=\int_0^1\!\int_0^\pi
\left[
 a^{-1}|v_X|^2
 +a|v_\theta|^2
 +a\csc^2\theta\,|v|^2
\right]d\theta\,dX,
\tag{2}
\]

and the untrimmed constant-width logarithmic rectangle form

\[
\mathfrak q_{\rm rect}[v]
:=\int_0^1\!\int_0^\pi
\left[
 s^{-1}|v_X|^2
 +s|v_\theta|^2
 +s\csc^2\theta\,|v|^2
\right]d\theta\,dX.
\tag{3}
\]

Put

\[
\beta:=\max(\sinh\rho_1,\sinh\rho_2),
\qquad
\eta:=\frac{\rho_1+\rho_2}{s}.
\tag{4}
\]

If `beta<1`, then on the common finite-energy form domain,

\[
\boxed{
(1-\beta)\,\mathfrak q_{\rm diag}
\le
\mathfrak q_{\rm hyp}
\le
(1+\beta+\beta^2)\,\mathfrak q_{\rm diag}.
}
\tag{5}
\]

Moreover

\[
\boxed{
(1-\eta)\,\mathfrak q_{\rm rect}
\le
\mathfrak q_{\rm diag}
\le
\frac1{1-\eta}\,\mathfrak q_{\rm rect}.
}
\tag{6}
\]

Consequently

\[
\boxed{
(1-\beta)(1-\eta)\,\mathfrak q_{\rm rect}
\le
\mathfrak q_{\rm hyp}
\le
\frac{1+\beta+\beta^2}{1-\eta}\,\mathfrak q_{\rm rect}.
}
\tag{7}
\]

The same inequalities hold for the corresponding **energy DtN quadratic forms** on the common pulled-back `theta` boundary trace space: for fixed boundary data, take the infimum of (5)--(7) over all extensions with that trace.

For the canonical PF-205 neighboring seam supports,

\[
\rho_j=\operatorname{arsinh}w_j,
\qquad
w_j=\kappa d_j,
\qquad
d_j=P_j^{-1}(1+o(1)),
\tag{8}
\]

so

\[
\boxed{\beta_n=O(P_n^{-1})\to0.}
\tag{9}
\]

PF-230 gives simultaneously

\[
\boxed{\eta_n\le\kappa+o(1)<1}
\tag{10}
\]

for the fixed sufficiently small PF-205 `kappa`. Thus the graph **tilt/shear** becomes asymptotically negligible in relative energy form, while the graph **width loss** remains uniformly controlled but need not converge to zero.

## 1. The normalized shear coefficient is `b`, not `b/a`

Differentiate the exact hypercycle graph:

\[
f_i'(\theta)
=\frac{\sinh\rho_i\cos\theta}
{\sqrt{1+\sinh^2\rho_i\sin^2\theta}}.
\tag{11}
\]

Since `a'=-f_1'-f_2'`, the PF-231 coefficient has the exact convex-combination form

\[
\boxed{
b=(1-X)f_1'-Xf_2'.}
\tag{12}
\]

Hence

\[
\boxed{
|b(X,\theta)|
\le
\max(\sinh\rho_1,\sinh\rho_2)
=\beta.
}
\tag{13}
\]

The potentially misleading quantity `b/a` appears because `X` is dimensionless while the physical transverse derivative has scale `1/a`. To compare energies, set

\[
P:=a^{-1/2}v_X,
\qquad
Q:=a^{1/2}v_\theta.
\tag{14}
\]

Then the complete gradient part of (1) is exactly

\[
\boxed{
|P|^2+|Q-bP|^2.
}
\tag{15}
\]

Thus the dimensionless relative coupling in the anisotropic energy norm is `b`. The ratio `b/a` by itself is not the perturbation parameter.

For complex-valued `P,Q`, equation (15) gives

\[
|P|^2+|Q-bP|^2
=(1+b^2)|P|^2+|Q|^2-2b\operatorname{Re}(P\overline Q).
\tag{16}
\]

Using `2|P||Q|<=|P|^2+|Q|^2` and `|b|<=beta`,

\[
(1-\beta)(|P|^2+|Q|^2)
\le
|P|^2+|Q-bP|^2
\le
(1+\beta+\beta^2)(|P|^2+|Q|^2).
\tag{17}
\]

The potential term in (1)--(2) is identical and nonnegative, so integration proves (5).

This estimate is uniform over all tangential frequencies. In particular, it does not deteriorate on the critical `theta` frequency scale `m=O(1/s)` singled out by PF-231: the thin-strip weights in (14) put transverse and critical tangential derivatives on the same energy scale before the `beta` coupling is measured.

## 2. Width variation is a separate bounded deformation

PF-231 proves

\[
(1-\eta)s\le a(\theta)\le s.
\tag{18}
\]

Therefore

\[
\frac1s\le\frac1a\le\frac1{(1-\eta)s},
\qquad
(1-\eta)s\le a\le s.
\tag{19}
\]

Applying these bounds separately to the transverse, tangential, and positive potential terms gives (6), and combining (5) with (6) gives (7).

The distinction matters. The hypercycle slope is controlled by the absolute seam width `w_i=sinh rho_i`, whereas the width deformation is controlled by the ratio `(rho_1+rho_2)/s`. For prime-flute scales these are respectively reciprocal-prime small and uniformly bounded seam-to-corridor data. Treating both effects as the single coefficient `b/a=O(1)` hides that separation.

## 3. Variational transfer to the full energy DtN form

Fix boundary traces `(g_0,g_1)` at `X=0,1` in the common finite-energy trace domain. Write

\[
\lambda_{\rm hyp}[g_0,g_1]
:=\inf_{\operatorname{Tr}v=(g_0,g_1)}\mathfrak q_{\rm hyp}[v],
\tag{20}
\]

and define `lambda_diag`, `lambda_rect` analogously. Since (5)--(7) hold for **every** admissible extension with the same trace, taking infima preserves the inequalities. In particular,

\[
(1-\beta)\lambda_{\rm diag}
\le\lambda_{\rm hyp}
\le(1+\beta+\beta^2)\lambda_{\rm diag},
\tag{21}
\]

with the analogous rectangle comparison from (7).

This is a statement about the full positive two-boundary energy form in the common `dtheta` trace representation. It does not imply entrywise or off-diagonal monotonicity for a `2 x 2` block operator, and it does not allow square roots of noncommuting seam forms to be cancelled. Those are exactly the distinctions required by the conformal-rectangle clue.

## 4. Canonical prime-flute scale

PF-205 chooses the signed Fermi-area seam halfwidth

\[
w_j=\kappa d_j,
\qquad
d_j=P_j^{-1}(1+o(1)).
\tag{22}
\]

The corresponding hyperbolic normal offset is `rho_j=arsinh w_j`, so

\[
\sinh\rho_j=w_j
\tag{23}
\]

**exactly**. Equations (4), (13), and (22) therefore yield

\[
\beta_n
=\max(w_n,w_{n+1})
=O(P_n^{-1}).
\tag{24}
\]

No prime-gap lower bound beyond the canonical setup is needed for this shear estimate. The gap data enter instead through `s_n` and hence through `eta_n`. PF-230 already proves the uniform tail bound (10).

Thus the coordinate shear introduced by the actual hypercycle trimming cannot supply a persistent order-one loss in the energy form. Any failure of PF-228's dressed `w/s` mechanism must come from a finer operation than this bulk form coupling: the variable-width diagonal problem itself, the actual seam-energy normalizers, finite pant/cusp completion, physical frequency projections, or global Schur reassembly.

## 5. Prior-art and novelty audit

Straightening variable-width thin domains and estimating the resulting quadratic forms is classical. A close standard reference remains Leonid Friedlander and Michael Solomyak, *On the Spectrum of the Dirichlet Laplacian in a Narrow Strip*, Israel Journal of Mathematics 170 (2009), 337--354, arXiv `0705.4058`, which treats variable-width narrow strips by quadratic-form methods. Variational definitions of Dirichlet-to-Neumann operators from nonnegative quadratic forms are likewise standard; Olaf Post, *Boundary pairs associated with quadratic forms*, Mathematische Nachrichten 289 (2016), 1052--1099, arXiv `1210.4707`, is representative abstract prior art.

No novelty is claimed for domain straightening, the inequality `2|P||Q|<=|P|^2+|Q|^2`, or the Dirichlet variational principle. A structure-directed search did not identify a theorem whose content is the PF-specific conclusion recorded here: for the exact PF-231 logarithmic hypercycle graphs coming from the PF-205 seam supports, the normalized shear parameter is exactly bounded by `max(sinh rho_i)=max(w_i)=O(P_i^{-1})`, while the independent width deformation is controlled by `(rho_1+rho_2)/s`. The durable value is this project-specific scale separation and the resulting removal of one purported order-one obstruction.

No external theorem is imported into the proof of (5)--(10); the literature above is novelty/methodological context only.

## 6. Falsification and boundary checks

1. The comparison is for the **energy form** in the pulled-back `theta` representation. Physical arclength on the hypercycles carries a nontrivial density, so no physical-`L^2` singular-value conclusion follows merely from (21).
2. The bound `beta<1` is harmless on the canonical tail because `beta_n=O(P_n^{-1})`, but (5) is not asserted with a positive lower constant for arbitrary large offsets.
3. The width comparison requires `eta<1`; PF-230 supplies this only after the canonical finite head.
4. `lambda_hyp` and `lambda_rect` are full positive two-boundary forms. Loewner comparability does **not** imply a comparable off-diagonal block after matrix inversion or after normalization by noncommuting seam forms.
5. The actual PF-205 seam-energy operator has not been proved two-sided comparable to the symmetric flat normalizer used in PF-228. The trial upper bound in the conformal-rectangle clue is not enough for that step.
6. The complete-axis logarithmic corridor still differs from the finite one-cusp pant module at its end completion, and the physical `P/H` projections are not diagonal in the Pöschl--Teller basis.
7. Nothing here proves weak `S_1` membership of the global reciprocal-prime Schur commutator, nested-cut weak-trace reassembly, wave-operator equivalence, determinant/resonance control, prime/clone separation, or any RH implication beyond what earlier findings already establish.

## Consequences for the research line

PF-231 localized the smooth-route problem to the hypercycle trim, boundary normalizers, projections, and global reassembly. PF-232 sharpens that localization: **hypercycle tilt is not the dangerous part of the trim**. After the exact fixed-domain normalization, its relative form size is `O(w_n)=O(P_n^{-1})`, not order one. The apparent order-one `b_s/a_s` coefficient was a coordinate-scale warning, not a lower bound on relative energy mixing.

The next local gate should therefore keep the variable-width diagonal form `q_diag` and the real PF-205 boundary-energy forms intact, and ask whether their normalized two-boundary Schur transfer retains PF-228's `sqrt(w_n w_{n+1})/s_n` amplitude with the required high-mode envelope. A failure now has to be exhibited in the boundary normalizer, width-dependent off-diagonal transfer, physical projection, or pant completion—not attributed generically to graph-straightening shear. Only after that one-cut estimate is settled does PF-222's nested weak-trace reassembly become the independent global gate.