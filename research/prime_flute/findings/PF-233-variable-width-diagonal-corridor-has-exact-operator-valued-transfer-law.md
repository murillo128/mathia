# PF-233 — variable-width diagonal corridor has an exact operator-valued transfer law

**Status:** `EXACT-DERIVED + OPERATOR-FACTORIZATION + SINGULAR-VALUE-ENVELOPE + POSITIVE/ROUTE-NARROWING`. PF-231 gives an exact logarithmic rectangle for the complete ultraparallel corridor, while PF-232 separates the actual hypercycle straightening into a reciprocal-prime-small shear and a variable-width diagonal form. The remaining diagonal coefficient does not commute with the Pöschl--Teller operator, so the constant-width scalar mode calculation from PF-228/PF-231 cannot simply be reused mode by mode. Nevertheless the diagonal problem is still **exactly separable after the correct boundary-mass conjugation**.

If

\[
\mathfrak q_a[v]
=\int_0^1\!\int_0^\pi
\left[
 a(\theta)^{-1}|v_X|^2
 +a(\theta)\bigl(|v_\theta|^2+\csc^2\theta\,|v|^2\bigr)
\right]d\theta\,dX,
\]

put `B=M_{a^{-1}}` on `H=L^2((0,\pi),d\theta)` and let `L_a` be the positive operator associated with

\[
\ell_a[g]=\int_0^\pi a(\theta)
\left(|g'|^2+\csc^2\theta\,|g|^2\right)d\theta.
\]

With the exact change of boundary variable

\[
y=B^{1/2}v=a^{-1/2}v,
\]

the two-dimensional form becomes

\[
\boxed{
\mathfrak q_a[v]
=\int_0^1
\left(\|y_X\|_H^2+\langle T_a^{1/2}y,T_a^{1/2}y\rangle_H\right)dX,
}
\]

where `T_a` is the positive self-adjoint operator associated with

\[
\tau_a[y]
:=\ell_a[a^{1/2}y].
\]

Thus, writing `K_a=T_a^{1/2}`, the energy Dirichlet-to-Neumann matrix on the **original** pulled-back `d\theta` boundary space is exactly

\[
\boxed{
\Lambda_a
=\mathcal B
K_a
\begin{pmatrix}
\coth K_a&-\operatorname{csch}K_a\\
-\operatorname{csch}K_a&\coth K_a
\end{pmatrix}
\mathcal B,
\qquad
\mathcal B=\operatorname{diag}(B^{1/2},B^{1/2}).
}
\]

No commutation between `a` and `A=-\partial_\theta^2+\csc^2\theta` is used. In particular the diagonal variable width still has an exact cross-block functional calculus after one explicit noncommuting conjugation.

Moreover, if

\[
(1-\eta)s\le a(\theta)\le s,
\qquad
\delta:=\left\|\frac{a'}{2a}\right\|_\infty<\infty,
\]

and

\[
C_\delta:=\max\{2,1+2\delta^2\},
\]

then in quadratic-form order

\[
\boxed{
\frac{(1-\eta)^2}{C_\delta}\,s^2 A
\ \le\ T_a\ \le\
C_\delta\,s^2 A.
}
\]

Since PF-231 gives `spec(A)=\{(m+\alpha)^2:m\ge0\}` with `\alpha=(1+\sqrt5)/2`, this forces the eigenvalues `\lambda_m(T_a)` to satisfy

\[
\frac{(1-\eta)^2}{C_\delta}s^2(m+\alpha)^2
\le
\lambda_m(T_a)
\le
C_\delta s^2(m+\alpha)^2.
\]

Consequently the conjugated cross block

\[
R_a:=K_a\operatorname{csch}K_a
\]

has exactly `O(s^{-1})` channels on every fixed scaled band and exponential decay above it, with constants depending only on uniform bounds for `\eta` and `\delta`. Mapping back to the original `d\theta` trace space multiplies the singular-value scale only by `s^{-1}` up to the same uniform width constants. Therefore the **variable-width diagonal corridor itself does not destroy the PF-228/PF-231 inverse-seam channel envelope**. The unresolved `\sqrt{w_1w_2}/s` dressed gain must now come from the real seam-energy normalizers and subsequent operations, not from noncommutation of the diagonal width coefficient alone.

This does **not** prove the actual PF-205 dressed local block. PF-232's shear is only known to be small in the full positive energy form; that does not yet give an off-diagonal perturbation estimate. The physical hypercycle boundary density, the real seam normalizers, `P/H` projections, and finite one-cusp-pant completion also remain outside the theorem.

## Claim

Let

\[
H=L^2((0,\pi),d\theta),
\qquad
A=-\partial_\theta^2+\csc^2\theta
\]

with the Friedrichs form domain `\mathcal V`. Let `a\in W^{1,\infty}(0,\pi)` be positive and suppose

\[
(1-\eta)s\le a\le s
\tag{1}
\]

for some `s>0` and `0\le\eta<1`. Define `\mathfrak q_a` as above on the fixed strip `(0,1)\times(0,\pi)`, put

\[
B:=M_{a^{-1}},
\tag{2}
\]

and let `L_a` be the operator associated with

\[
\ell_a[g]
=\int_0^\pi a\left(|g'|^2+\csc^2\theta\,|g|^2\right)d\theta.
\tag{3}
\]

Define `T_a` by the closed form

\[
\boxed{
\tau_a[y]
:=\ell_a[B^{-1/2}y]
=\ell_a[a^{1/2}y].
}
\tag{4}
\]

Then:

1. under `y=B^{1/2}v`,
   \[
   \mathfrak q_a[v]
   =\int_0^1\left(\|y_X\|^2+\tau_a[y]\right)dX;
   \tag{5}
   \]
2. if `K_a=T_a^{1/2}`, the energy DtN matrix is, in form sense,
   \[
   \boxed{
   \Lambda_a
   =\mathcal B
   K_a
   \begin{pmatrix}
   \coth K_a&-\operatorname{csch}K_a\\
   -\operatorname{csch}K_a&\coth K_a
   \end{pmatrix}
   \mathcal B,
   }
   \tag{6}
   \]
   where `\mathcal B=diag(B^{1/2},B^{1/2})`;
3. with
   \[
   \delta=\left\|\frac{a'}{2a}\right\|_\infty,
   \qquad
   C_\delta=\max\{2,1+2\delta^2\},
   \tag{7}
   \]
   one has
   \[
   \boxed{
   c_0s^2A\le T_a\le C_0s^2A,
   \qquad
   c_0=\frac{(1-\eta)^2}{C_\delta},
   \quad C_0=C_\delta;
   }
   \tag{8}
   \]
4. if `\kappa_m=m+\alpha`, `\alpha=(1+\sqrt5)/2`, and `\lambda_m(T_a)` is ordered increasingly, then
   \[
   c_0s^2\kappa_m^2
   \le\lambda_m(T_a)\le
   C_0s^2\kappa_m^2;
   \tag{9}
   \]
5. for `F(x)=x/\sinh x`, the positive conjugated cross block
   \[
   R_a=F(K_a)=K_a\operatorname{csch}K_a
   \tag{10}
   \]
   has singular values
   \[
   s_{m+1}(R_a)=F(\sqrt{\lambda_m(T_a)}),
   \tag{11}
   \]
   and therefore
   \[
   \boxed{
   F(\sqrt{C_0}\,s\kappa_m)
   \le s_{m+1}(R_a)
   \le
   F(\sqrt{c_0}\,s\kappa_m).
   }
   \tag{12}
   \]
6. the raw off-diagonal DtN block on the original `d\theta` trace space is
   \[
   C_a=-B^{1/2}R_aB^{1/2},
   \tag{13}
   \]
   and its singular values obey
   \[
   \boxed{
   \frac1s\,s_{m+1}(R_a)
   \le s_{m+1}(C_a)
   \le
   \frac1{(1-\eta)s}\,s_{m+1}(R_a).
   }
   \tag{14}
   \]

For the PF-231/PF-232 hypercycle width

\[
a(\theta)
=s-f_{\rho_1}(\theta)-f_{\rho_2}(\theta),
\qquad
f_\rho(\theta)=\operatorname{arsinh}(\sinh\rho\sin\theta),
\tag{15}
\]

PF-230 gives a uniform tail bound `\eta<1`, and

\[
|a'|\le\sinh\rho_1+\sinh\rho_2.
\tag{16}
\]

For the canonical PF-205 offsets `\sinh\rho_i=w_i=\kappa d_i`, the resulting `\delta` is uniformly bounded on the tail. Hence all constants in (8)--(14) are uniform for the canonical neighboring-cuff family.

## 1. Exact mass conjugation restores product separation

Write the diagonal form as

\[
\mathfrak q_a[v]
=\int_0^1
\left(
\langle Bv_X,v_X\rangle_H+\ell_a[v]
\right)dX.
\tag{17}
\]

Because `B` is independent of `X`, the substitution

\[
y=B^{1/2}v=a^{-1/2}v
\tag{18}
\]

gives

\[
\langle Bv_X,v_X\rangle=\|y_X\|^2
\]

exactly, while the tangential part becomes `\tau_a[y]` by definition. This proves (5). The price for removing the variable transverse mass is not an approximation; it is the new self-adjoint transverse operator `T_a`. All noncommutation between multiplication by `a` and tangential differentiation is retained inside `T_a`.

The boundary traces transform by the same fixed operator:

\[
y_i=B^{1/2}g_i,
\qquad i=0,1.
\tag{19}
\]

For the product form (5), spectral calculus for the positive self-adjoint `T_a` solves

\[
(-\partial_X^2+T_a)y=0
\tag{20}
\]

on the unit interval. Its two-boundary energy matrix is

\[
K_a
\begin{pmatrix}
\coth K_a&-\operatorname{csch}K_a\\
-\operatorname{csch}K_a&\coth K_a
\end{pmatrix}.
\tag{21}
\]

Conjugating the boundary traces back by `B^{1/2}` proves (6) and the exact cross-block identity (13). Thus the variable-width diagonal problem is not merely comparable to a separable model: it is itself an operator-valued one-dimensional product problem.

## 2. The effective transverse operator stays at scale `s^2 A`

Expanding (4), put

\[
c(\theta):=\frac{a'(\theta)}{2a(\theta)}.
\tag{22}
\]

Then

\[
\boxed{
\tau_a[y]
=\int_0^\pi a^2
\left(
|y'+cy|^2+\csc^2\theta\,|y|^2
\right)d\theta.
}
\tag{23}
\]

Let `V=\csc^2\theta\ge1`. Pointwise,

\[
|y'+cy|^2+V|y|^2
\le
2|y'|^2+(1+2\delta^2)V|y|^2
\le C_\delta\left(|y'|^2+V|y|^2\right).
\tag{24}
\]

Conversely,

\[
|y'|^2+V|y|^2
\le
2|y'+cy|^2+(1+2\delta^2)V|y|^2
\le C_\delta\left(|y'+cy|^2+V|y|^2\right).
\tag{25}
\]

Using `(1-\eta)^2s^2\le a^2\le s^2` in (23)--(25) proves (8). The singular endpoint potential is helpful here: it absorbs the bounded zeroth-order term generated by differentiating `a^{1/2}`. No assumption that `a` is close to a constant in derivative norm is needed; only a uniform bound for `a'/a` is required.

Since multiplication by `a^{1/2}` preserves the Friedrichs form domain and `A` has compact resolvent, so does `T_a`. The min--max principle applied to (8), together with PF-231's exact `A` spectrum, gives (9).

## 3. Exact cross-block spectrum and high-mode decay

The scalar function

\[
F(x)=\frac{x}{\sinh x}
\tag{26}
\]

is positive and strictly decreasing for `x>0`. Therefore (9) and functional calculus give (11)--(12).

For every fixed `Z>0`, all modes with

\[
s\kappa_m\le Z
\tag{27}
\]

satisfy

\[
s_{m+1}(R_a)
\ge F(\sqrt{C_0}Z)>0.
\tag{28}
\]

There are `Z/s+O(1)` such modes. Above the scaled band, (12) and the elementary large-`x` behavior of `F` give uniform constants `c,C>0` such that

\[
\boxed{
s_{m+1}(R_a)
\le C(1+s\kappa_m)e^{-cs\kappa_m}.}
\tag{29}
\]

Thus the variable width neither creates a larger channel population than the `1/s` scale nor removes the exponential high-mode suppression present in the constant-width reference, up to uniform multiplicative constants in the scaled frequency.

To return to the original boundary variable, (1) gives

\[
\|B^{1/2}\|\le\frac1{\sqrt{(1-\eta)s}},
\qquad
\|B^{-1/2}\|\le\sqrt s.
\tag{30}
\]

The standard approximation-number inequalities applied to (13) give the upper half of (14). For the lower half, write

\[
R_a=B^{-1/2}(-C_a)B^{-1/2}
\]

and use (30). This proves that the raw variable-width cross block has the same `s^{-1}` amplitude scale as the exact rectangle, with the same `O(s^{-1})` scaled-band population and exponential tail.

## 4. Canonical hypercycle widths satisfy the uniform hypotheses

For (15), PF-231 gives

\[
(1-\eta)s\le a\le s,
\qquad
\eta=\frac{\rho_1+\rho_2}{s},
\tag{31}
\]

and

\[
|f_\rho'|\le\sinh\rho.
\tag{32}
\]

Hence

\[
\delta
\le
\frac{\sinh\rho_1+\sinh\rho_2}
{2(1-\eta)s}.
\tag{33}
\]

For the PF-205 supports, `\sinh\rho_i=w_i=\kappa d_i` exactly. PF-230 supplies `\eta\le\kappa+o(1)<1` after a finite head, while `\rho_i\to0`; consequently `(\sinh\rho_1+\sinh\rho_2)/s` is uniformly bounded. Thus `\delta`, `c_0`, and `C_0` are uniform on the canonical tail.

This conclusion is deliberately weaker than saying `a/s\to1`: the relative width loss can remain order one. The theorem shows that this bounded nonconstant profile is still compatible with the same scaled transverse spectral law after the exact mass conjugation.

## 5. Prior-art and novelty audit

The abstract operator-valued Sturm--Liouville equation `-d^2/dX^2+T` on a Hilbert space is classical. A close operator-theoretic reference is M. Malamud and H. Neidhardt, *Sturm--Liouville boundary value problems with operator potentials and unitary equivalence*, Journal of Differential Equations 252 (2012), 5875--5922, DOI `10.1016/j.jde.2012.02.018`, arXiv `1102.3849`. Variational Dirichlet-to-Neumann operators for nonnegative quadratic forms are treated abstractly by O. Post, *Boundary pairs associated with quadratic forms*, Mathematische Nachrichten 289 (2016), 1052--1099, DOI `10.1002/mana.201500048`, arXiv `1210.4707`. Quadratic-form straightening of variable-width narrow strips is also classical; L. Friedlander and M. Solomyak, *On the Spectrum of the Dirichlet Laplacian in a Narrow Strip*, Israel Journal of Mathematics 170 (2009), 337--354, DOI `10.1007/s11856-009-0032-y`, arXiv `0705.4058`, is representative.

No novelty is claimed for Hilbert-space functional calculus, the product-cylinder DtN formula, form conjugation, the min--max principle, or singular-value ideal inequalities. A structure-directed search did not identify a theorem whose content is the PF-specific statement proved here: the exact PF-231 hypercycle **diagonal** width can be mass-conjugated into a product operator `-\partial_X^2+T_a`, with `T_a\asymp s^2A` uniformly at the canonical prime-flute scales, so its raw cross-DtN block retains the `1/s` channel scale and exponential scaled-frequency envelope despite noncommutation of `a(\theta)` with `A`.

The external literature is methodological/prior-art context; equations (5)--(14) are derived directly from the persisted PF-231/PF-232 form and elementary spectral theory.

## 6. Falsification and boundary checks

1. The theorem concerns the **diagonal variable-width form** `\mathfrak q_a`, not the full PF-232 sheared form. Small relative error of the full positive form does not by itself imply a small error in its off-diagonal DtN block.
2. Formula (6) is on the pulled-back `d\theta` boundary space. The physical hypercycle arclength density from the accepted conformal-rectangle clue is singular at `\theta=0,\pi`; it has not been absorbed into (6).
3. The cross block in (13) is the raw corridor DtN transmission. The actual PF-205 dressed operator normalizes it by two noncommuting seam-energy forms and then participates in Schur inversion. The `\sqrt{w_1w_2}/s` gain is therefore **not** proved here.
4. The proof uses a positive width floor `(1-\eta)s`. It does not apply to the symmetric seam collar itself, whose logarithmic-coordinate width vanishes at the ideal endpoints; the missing two-sided seam-normalizer theorem remains a separate problem.
5. The complete-axis corridor still differs from finite cuff arcs and the one-cusp-pant completion. No artificial endpoint condition from the complete model may be imported into the finite pant.
6. Nothing here proves the physical `P/H` projected estimate, the PF-222 global weak-`S_1` reassembly, wave-operator equivalence, determinant/resonance control, prime/clone separation, or an RH implication.

## Consequences for the research line

PF-231 removed the false constant-Fermi-width obstruction, and PF-232 removed graph shear as an order-one energy perturbation. PF-233 now removes the remaining **diagonal width noncommutation** as a raw transfer obstruction: after exact mass conjugation the variable-width problem has a genuine operator-valued product structure, and its transverse operator stays uniformly at the `s^2A` scale.

The accepted conformal-rectangle clue can therefore be narrowed again. The local target is no longer to discover whether the variable-width diagonal corridor has the right channel count or high-mode decay; it does. The decisive unresolved step is to combine the exact cross block (13) with the **actual PF-205 seam-energy normalizers**, then show that PF-232's reciprocal-prime shear, physical boundary identification/`P/H` projections, and finite-pant completion preserve enough of the resulting `\sqrt{w_nw_{n+1}}/s_n` dressed envelope. A failure must now occur in one of those operations rather than in the diagonal corridor spectrum itself.