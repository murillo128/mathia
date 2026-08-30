# WP-045 — radial Schur elimination loses the boundary Weil birth term

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the shell-blind Schur/Feshbach escape left open by `WP-044`. The cross-radius Prime-Circle Gram kernel remains positive under ordinary block Schur elimination, so this is a genuine sign-preserving nonlinear operation rather than another subtraction. Nevertheless, under the comparable boundary scaling in which `WP-044` isolates the radial common mode, eliminating even one radial channel removes the finite Prime-Circle birth operator `C` from the leading boundary response. The Schur limit is a universal positive scalar kernel in the radial variables tensored with the shell identity; the Weil-signed finite-prime operator survives only inside a vanishing resolvent correction. Thus a shell-blind finite-dimensional Feshbach/conditional-covariance construction cannot isolate `C` while inheriting positivity from the original radial Gram family.

This does **not** rule out shell-dependent elimination, a singular cutoff-dependent rescaling that magnifies subleading terms, an infinite-dimensional nonseparable finite--archimedean sector, a nonlinear determinant/intersection pairing, or another construction whose sign theorem is not merely Schur positivity. Those remain genuine escapes because they break the shell-blind common-mode structure used below.

## 1. Start from the positive cross-radius Prime-Circle Gram

On a fixed finite primitive-shell space `E`, `WP-036` and `WP-044` give

\[
\widehat G_x
=\sum_{r\ge1}\frac{x^r}{r}u_ru_r^*\succeq0,
\qquad 0<x<1,
\tag{1}
\]

and the canonical polarization

\[
\widehat G_{x,y}
:=\widehat G_{\sqrt{xy}}
=\sum_{r\ge1}\frac{(xy)^{r/2}}r u_ru_r^*.
\tag{2}
\]

Hence, for any finitely many radii `x_1,...,x_k`, the block Gram operator

\[
\mathbb K_X
=\left[\widehat G_{\sqrt{x_ix_j}}\right]_{i,j=1}^k
\succeq0
\tag{3}
\]

on `C^k tensor E` is positive semidefinite.

`WP-044` showed that **linear** radial contrasts cannot remove the universal collision divergence without simultaneously removing the arithmetic finite part. A natural nonlinear escape is therefore to integrate out radial channels by Schur complement/Feshbach reduction. Because Schur complementation of a positive block operator is again positive when the eliminated block is invertible, this route carries an independent sign theorem automatically.

The question is whether that sign-preserving nonlinear elimination can retain the Prime-Circle birth operator `C`.

## 2. Comparable boundary scaling has one common shell operator in every radial block

Take

\[
x_i(\varepsilon)
=1-c_i\varepsilon+o(\varepsilon),
\qquad c_i>0,
\qquad \varepsilon\downarrow0.
\tag{4}
\]

Then

\[
1-\sqrt{x_i x_j}
=\frac{c_i+c_j}{2}\varepsilon+o(\varepsilon).
\tag{5}
\]

Let

\[
L_\varepsilon=-\log\varepsilon,
\qquad
B_{ij}:=-\log\frac{c_i+c_j}{2}.
\tag{6}
\]

Using the fixed-shell boundary expansion of `WP-034`/`WP-044`, each cross block satisfies in operator norm on `E`

\[
\boxed{
\widehat G_{\sqrt{x_i x_j}}
=
X_\varepsilon+B_{ij}I_E+o(1),
\qquad
X_\varepsilon:=L_\varepsilon I_E+C.
}
\tag{7}
\]

Thus the same shell operator `X_epsilon` appears in **every** radial block. The divergent scalar identity and the arithmetic operator are already fused before any Schur reduction:

\[
X_\varepsilon
=L_\varepsilon I_E+C.
\tag{8}
\]

Since `E` is fixed and finite dimensional, `C` is bounded. Therefore, for every fixed `k`, the diagonal block

\[
\widehat G_{x_k}
=X_\varepsilon+B_{kk}I_E+o(1)
\tag{9}
\]

is strictly positive and invertible for all sufficiently small `epsilon`, with

\[
\left\|\widehat G_{x_k}^{-1}\right\|=O(L_\varepsilon^{-1}).
\tag{10}
\]

## 3. Eliminating one radial channel cancels the common shell operator

Eliminate radial channel `k`. For retained indices `i,j != k`, define the Schur/Feshbach response

\[
\mathcal S^{(k)}_{ij}(\varepsilon)
:=
\widehat G_{\sqrt{x_i x_j}}
-
\widehat G_{\sqrt{x_i x_k}}
\widehat G_{x_k}^{-1}
\widehat G_{\sqrt{x_k x_j}}.
\tag{11}
\]

Because the parent block matrix (3) is positive, the reduced block matrix

\[
\mathcal S^{(k)}(\varepsilon)
=\left[\mathcal S^{(k)}_{ij}(\varepsilon)\right]_{i,j\ne k}
\succeq0.
\tag{12}
\]

Now ignore only the `o(1)` remainders in (7) for one algebraic step and write

\[
Y_\varepsilon:=X_\varepsilon+B_{kk}I_E.
\tag{13}
\]

Since every displayed block is a scalar affine function of the same operator `X_epsilon`, the blocks commute and the following identity is exact:

\[
\begin{aligned}
&(X_\varepsilon+B_{ij}I)
-(X_\varepsilon+B_{ik}I)
(X_\varepsilon+B_{kk}I)^{-1}
(X_\varepsilon+B_{kj}I)
\\[1mm]
&\quad=
D^{(k)}_{ij}I
-
\alpha_i\alpha_j
Y_\varepsilon^{-1},
\end{aligned}
\tag{14}
\]

where

\[
\boxed{
D^{(k)}_{ij}
=B_{ij}-B_{ik}-B_{kj}+B_{kk}
}
\tag{15}
\]

and

\[
\alpha_i=B_{ik}-B_{kk}.
\tag{16}
\]

The cancellation in (14) is the key point: the entire common operator `X_epsilon`, including `C`, disappears from the leading term. It survives only inside the inverse `Y_epsilon^{-1}`.

Restoring the `o(1)` terms in (7) does not change the boundary conclusion. The cross blocks have norm `O(L_epsilon)`, the eliminated inverse has norm `O(1/L_epsilon)`, and the resolvent perturbation caused by the diagonal `o(1)` term is `o(1/L_epsilon^2)`. Consequently every error introduced in (11) is `o(1)`, and (10) makes the resolvent term in (14) itself `O(1/L_epsilon)`. Hence

\[
\boxed{
\mathcal S^{(k)}_{ij}(\varepsilon)
=D^{(k)}_{ij}I_E+o(1).
}
\tag{17}
\]

Therefore

\[
\boxed{
\mathcal S^{(k)}(\varepsilon)
\longrightarrow
D^{(k)}\otimes I_E
}
\tag{18}
\]

in operator norm on every fixed finite shell box.

The finite arithmetic operator `C` is absent from the Schur boundary response.

## 4. The limiting radial kernel is positive and completely universal

The limit in (18) is not merely shell-scalar; its positivity can be seen directly.

Using (6),

\[
D^{(k)}_{ij}
=
-\log\frac{c_i+c_j}{2}
+\log\frac{c_i+c_k}{2}
+\log\frac{c_k+c_j}{2}
-\log c_k.
\tag{19}
\]

The elementary logarithm integral gives

\[
\boxed{
D^{(k)}_{ij}
=
\int_0^\infty
\frac{
(e^{-c_it/2}-e^{-c_kt/2})
(e^{-c_jt/2}-e^{-c_kt/2})
}{t}\,dt.
}
\tag{20}
\]

Thus `D^(k)` is a Gram matrix of radial difference features and

\[
D^{(k)}\succeq0.
\tag{21}
\]

The convergence of (20) is elementary: the numerator is `O(t^2)` at zero and decays exponentially at infinity.

So Schur elimination does preserve positivity, exactly as hoped. What it preserves in the boundary limit is the universal radial conditional-covariance kernel (20), not the arithmetic birth form.

Nothing in (19)--(21) knows about primes, Ramanujan shells, von Mangoldt weights, or the Riemann Gamma factor.

## 5. The two-radius case makes the loss completely explicit

Keep one radius with scale constant `c` and eliminate one with scale constant `d`. Then (18) becomes the scalar-shell limit

\[
\boxed{
\mathcal S_{c\mid d}(\varepsilon)
\longrightarrow
\log\frac{(c+d)^2}{4cd}\,I_E
\succeq0.
}
\tag{22}
\]

This is exactly the same arithmetic--geometric-mean scalar that appears in the two-radius secant energy of `WP-044`, but it now arises from a genuine nonlinear Schur/Feshbach operation.

For the idealized boundary model with the `o(1)` term deleted, equation (14) is more informative. Put

\[
b_c=-\log c,
\quad
b_d=-\log d,
\quad
b_{cd}=-\log\frac{c+d}{2}.
\]

Then

\[
\boxed{
\mathcal S^{\rm ideal}_{c\mid d}
=
\log\frac{(c+d)^2}{4cd}\,I_E
-
\left(\log\frac{2d}{c+d}\right)^2
\bigl(L_\varepsilon I_E+C+b_dI_E\bigr)^{-1}.
}
\tag{23}
\]

Thus even before taking the limit, `C` is no longer an additive finite part. It has been pushed into a resolvent multiplied by a term vanishing like `1/log(1/epsilon)`.

Equation (23) is **not** used to claim a controlled first subleading expansion of the exact Prime-Circle Schur response: the known boundary remainder is only `o(1)` and can dominate `1/L_epsilon`. It is instead an exact diagnostic of the common-mode model. To recover `C` from such a subleading resolvent in the true geometry would require new quantitative asymptotics plus a singular subtraction/rescaling. The ordinary Schur sign theorem does not provide positivity for that renormalized extraction.

## 6. Why this is different from the linear contrast obstruction

`WP-044` proved that a fixed zero-sum radial contrast annihilates `C` because the collision term and `C` share the radial tensor factor `J`.

The present calculation addresses a different escape. Schur/Feshbach reduction is nonlinear:

\[
A-BD^{-1}B^*.
\]

It can generate effective interactions that are not obtainable from a fixed linear contrast, and in many geometric problems it is exactly the canonical way positive bulk energy induces a positive boundary response.

Nevertheless, equations (14)--(18) show that the nonlinear elimination still cannot separate the two common-mode components. Algebraically, the large common operator `X_epsilon=L_epsilon I+C` cancels between the direct block and the conditioned block before the boundary limit is taken. The surviving leading response is the radial second-difference kernel `D^(k)`.

This is also distinct from `WP-026`. There the no-go used closure of passive resistor/Markov Laplacians under Kron reduction and a negative constant-mode self-energy obstruction. Here the parent object is a **positive Gram covariance kernel**, not a loopy Laplacian, and no row-sum or `M`-matrix argument is used. The obstruction is the Prime-Circle boundary common-mode factorization itself.

## 7. Finite-prime and archimedean consequences

`WP-036` remains the strongest same-parent bridge: the positive radial family has a Mellin diagonal containing the Riemann `psi(s/2)` scale, while its boundary finite part contains the Prime-Circle birth operator with interior coefficients

\[
-\frac{\Lambda(p^m)}{\sqrt{p^m}}.
\tag{24}
\]

The Schur construction might therefore have served as the missing positive coupling: add radial/archimedean channels, integrate some of them out, and hope the effective positive response keeps the finite arithmetic term while removing the collision background.

Equation (18) rules out that mechanism for **shell-blind finite radial elimination under comparable boundary scaling**. The effective positive boundary response is

\[
D^{(k)}\otimes I_E,
\tag{25}
\]

so it contains neither the finite birth matrix nor an interaction capable of marrying that matrix to the `q=2` Mellin/digamma channel.

The surviving design requirement is therefore stronger than after `WP-044`: a successful Feshbach/boundary construction must be nonseparable in radial and shell variables **before** elimination, or must use a singular limit whose renormalized sign is proved independently. Merely promoting finite radial contrasts to ordinary positive Schur elimination does not cross the boundary.

## 8. Matched controls and novelty audit

The Schur-complement positivity used in (12) is classical finite-dimensional Hilbert-space geometry; no novelty is claimed for it. `WP-026` already audits Schur/Kron boundary response as standard machinery in a different passive-network cone.

The Mathia-specific statement is the exact cancellation identity (14) combined with the Prime-Circle boundary expansion (7). The mechanism is **too universal** to encode Riemann arithmetic: replace `C` by an arbitrary bounded self-adjoint operator on any finite-dimensional shell space and the same conclusion (18) holds. The limit depends only on the radial approach constants `c_i`.

This matched control is decisive for the claimed scope. Any interpretation of (18) as specifically prime-geometric would fail, because primality never enters the Schur cancellation once the common-mode asymptotic has been established.

The result also does not reproduce Connes--Consani/Sonin localization or a cohomological intersection form. Those mechanisms change the relevant space or pairing before positivity is read off. Here the operation stays entirely inside the existing Prime-Circle radial Gram family and therefore cannot claim novelty by analogy to those prior-art programs.

## 9. Boundary of the no-go

The finding is deliberately narrower than a general impossibility theorem for positive compression.

It rules out:

- fixed finite collections of comparable boundary radii;
- the canonical cross-radius polarization of `WP-044`;
- shell-blind elimination of one radial channel by ordinary positive Schur/Feshbach reduction;
- iterating that idea as a proposed way to make the **leading** effective boundary response retain `C`.

It does **not** rule out:

- a Schur map whose radial elimination depends nontrivially on the arithmetic shell/conductor;
- an infinite-dimensional radial/archimedean sector with genuinely nonseparable shell coupling;
- an unbounded or cutoff-dependent transform that magnifies subleading terms;
- proving a sharper exact remainder expansion and then finding a new independently positive renormalized response;
- determinant, intersection, grading, cohomological, or relative-order constructions not reducible to the Schur response above.

The fixed-shell hypothesis is essential. Equation (7) is a fixed finite-box boundary asymptotic and this finding does not exchange the boundary limit with a cofinal shell cutoff.

## 10. Exact falsification tests

The claim can be killed by any one of the following:

1. for fixed finite shell space and comparable radii, a direct calculation of (11) with a non-scalar shell-dependent `O(1)` limit;
2. failure of the algebraic identity (14) for commuting common blocks `X+B_ij I`;
3. a radial matrix `D^(k)` from (15) with a negative quadratic direction, contradicting the Gram representation (20);
4. an ordinary shell-blind Schur elimination whose leading finite boundary term retains a nonzero multiple of `C` while the universal collision term is removed;
5. a proof that the singular subtraction/rescaling needed to expose the vanishing resolvent correction in the exact geometry inherits positivity from Schur complementation alone.

Items 1--4 contradict the exact fixed-box derivation. Item 5 would supply precisely the additional sign theorem that this finding leaves open rather than assumes.