# WP-146 — Critical resultant kernel is conditionally indefinite on a mixed-prime three-chain

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + CRITICAL-HALF-DENSITY + CONDITIONAL-SIGN-FAILURE + MATCHED-EQUAL-WEIGHT-CONTROL + GLOBAL-COMPLETION-OBSTRUCTION + PRIOR-ART-AUDITED` for the direct Schoenberg/centered-quotient continuation of the zero-order Prime-Circle resultant kernel.

`WP-145` showed that differentiating the logarithmic cyclotomic resultant into its canonical positive Hessian destroys the prime-power support and `log p` amplitudes that matter for the finite Weil term. A natural escape is to keep the zero-order resultant kernel intact and ask for positivity only after quotienting the constant direction, as in conditionally positive/negative kernels, centered Gram constructions, and intersection-style forms.

That escape already fails on three exact-order Prime-Circle shells. The normalized resultant kernel retains the desired critical amplitudes on each prime-power edge, but two different prime labels joined in series force an indefinite quadratic form on the mean-zero subspace. The failure survives every additive row-plus-column gauge and every later global augmentation that leaves this finite kernel as a principal block with the ordinary total-zero constraint. Thus simple centering cannot be the missing sign theorem: any surviving route must alter or couple the finite arithmetic data before conditional positivity is invoked.

## 1. Preserve the zero-order arithmetic kernel instead of differentiating it

For distinct positive integers `m,n`, define the normalized zero-order resultant kernel

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}},
\qquad J_{m,m}=0.
\tag{1}
\]

By Apostol's cyclotomic-resultant theorem, if `n/m=p^k` with prime `p`, then

\[
|\operatorname{Res}(\Phi_m,\Phi_n)|=p^{\varphi(m)},
\tag{2}
\]

and if `n/m` is not a prime power the absolute resultant is `1`. On an interior prime-power step, where `p\mid m` and hence

\[
\varphi(mp^k)=p^k\varphi(m),
\tag{3}
\]

(1) therefore gives exactly

\[
\boxed{
J_{m,mp^k}=\frac{\log p}{p^{k/2}}.
}
\tag{4}
\]

Unlike the positive Hessian in `WP-145`, the zero-order kernel has both the sparse prime-power support and the critical half-density amplitude required by the finite Weil contribution.

The question is whether this arithmetic kernel might already have a geometric sign after removing the trivial constant direction. For a finite restriction `J_F`, conditional negative definiteness would require

\[
a^T J_F a\le0
\qquad\text{whenever}\qquad \sum_i a_i=0,
\tag{5}
\]

while conditional positive definiteness reverses the inequality. In the negative-type case the centered kernel `-P J_F P` is positive semidefinite on the mean-zero subspace, with `P` the orthogonal projection off constants. This is the canonical Schoenberg/centered-Gram route that preserves the zero-order arithmetic values before applying a sign theorem.

## 2. The exact arithmetic witness is the chain 6 → 12 → 36

Take the three exact-order shells

\[
m_0=6,
\qquad m_1=12=6\cdot2,
\qquad m_2=36=12\cdot3.
\tag{6}
\]

Both adjacent ratios are prime, and both are interior steps because `2\mid6` and `3\mid12`. Equation (4) gives

\[
x:=J_{6,12}=\frac{\log2}{\sqrt2},
\qquad
y:=J_{12,36}=\frac{\log3}{\sqrt3}.
\tag{7}
\]

The endpoint ratio is `36/6=6`, which is not a prime power, so Apostol's theorem gives

\[
J_{6,36}=0.
\tag{8}
\]

Thus the exact restriction is the weighted path

\[
\boxed{
J_F=
\begin{pmatrix}
0&x&0\\
x&0&y\\
0&y&0
\end{pmatrix}.
}
\tag{9}
\]

The two arithmetically forced edge weights are unequal. In fact `3^4=81>32=2^5`, so

\[
\frac{\log3}{\log2}>\frac54>
\sqrt{\frac32},
\tag{10}
\]

and hence

\[
y=\frac{\log3}{\sqrt3}>
\frac{\log2}{\sqrt2}=x>0.
\tag{11}
\]

This gives a finite witness involving only exact Prime-Circle resultant data; no zero locations, fitted kernel, regularization, or archimedean term has been inserted.

## 3. Unequal prime labels force both conditional signs to fail

Write an arbitrary mean-zero vector on the three nodes as

\[
a=(s,t,-s-t).
\tag{12}
\]

For the general weighted path

\[
R_{x,y}=
\begin{pmatrix}
0&x&0\\
x&0&y\\
0&y&0
\end{pmatrix},
\tag{13}
\]

direct expansion gives

\[
\boxed{
a^T R_{x,y}a
=2\bigl[(x-y)st-y t^2\bigr].
}
\tag{14}
\]

As a quadratic form in `(s,t)`, the determinant of the associated symmetric `2×2` matrix is

\[
-\frac{(x-y)^2}{4}<0
\qquad (x\ne y).
\tag{15}
\]

Therefore the restriction to the mean-zero plane is indefinite. Both possible conditional signs fail explicitly:

- with `a=(1,-1,0)`,
  \[
  a^T J_F a=-2x<0,
  \tag{16}
  \]
  so `J_F` is not conditionally positive definite;
- because `y>x`, set `t=1` and `s=-2y/(y-x)`. Then
  \[
  a^T J_F a=2y>0,
  \tag{17}
  \]
  so `J_F` is not conditionally negative definite.

Hence

\[
\boxed{
J_F\text{ is neither CPD nor CND on }\mathbf1^\perp.
}
\tag{18}
\]

Equivalently, neither `P J_F P` nor `-P J_F P` is positive semidefinite on the centered quotient. The desired critical arithmetic amplitudes have survived intact, but their mixed-prime assembly has no Schoenberg sign.

## 4. Matched control: the graph shape is not the obstruction

The same three-node path with equal positive edge weights passes the negative-type test. If `x=y=w>0`, equation (14) collapses to

\[
a^T R_{w,w}a=-2w t^2\le0
\qquad\text{for every }a\perp\mathbf1.
\tag{19}
\]

Thus an equal-weight path is conditionally negative semidefinite. The failure in (18) is not caused merely by using three nodes, a path graph, sparse support, or centering. It is triggered by the **unequal prime-dependent critical amplitudes** forced by the cyclotomic resultant.

This is the relevant matched control for the Mathia route: replacing the arithmetic labels by a geometrically homogeneous clone repairs the conditional sign, while restoring the exact `log p/\sqrt p` labels destroys it.

## 5. Centering gauges and a later separate global sector cannot repair the witness

Conditional kernels are unchanged on the mean-zero subspace by additive row-plus-column gauges. If

\[
G_{ij}=u_i+u_j,
\tag{20}
\]
then for every `a` with `\sum_i a_i=0`,

\[
a^TGa
=2\left(\sum_i a_i\right)
\left(\sum_i u_i a_i\right)=0.
\tag{21}
\]

Equivalently,

\[
P(J_F+G)P=PJ_FP.
\tag{22}
\]

So constants, separate shell self-energies represented by row/column potentials, or a change of centering gauge cannot fix (18). This statement deliberately does **not** cover an arbitrary diagonal completion `d_i\delta_{ij}`; such a term changes the quadratic form rather than its gauge class and is a genuinely different completion problem, already constrained globally by `WP-096`/`WP-097`.

Nor can one append an independent archimedean or pole sector *afterward* while leaving `J_F` as an unchanged principal block and retaining the ordinary total-zero conditional-sign domain. Either witness from (16)--(17), extended by zeros in the new coordinates, still has total sum zero and retains the same wrong sign. Therefore every CPD/CND global kernel must already have CPD/CND restrictions on this finite triple.

This does not rule out a global construction in which the real place, pole sector, cohomological quotient, or cross-prime correspondence modifies the finite block **before** the sign theorem, or in which the admissible test space is coupled by a nontrivial global constraint. It rules out the direct sequence

\[
\boxed{
\text{exact zero-order resultant coefficients}
\longrightarrow
\text{ordinary centering / negative-type quotient}
\longrightarrow
\text{PSD geometry}
}
\tag{23}
\]

even before the missing archimedean terms are addressed.

## 6. Relation to existing Mathia obstructions and prior art

This is distinct from the two closest earlier failures. `WP-052` showed that interpreting the Prime-Circle resultant as an Arakelov principal-divisor intersection does not produce a new global class with the required sign. `WP-145` kept the actual collision geometry but moved to the independently positive second variation, thereby losing prime-power support and `log p`. The present witness keeps the **zero-order** resultant and its exact critical amplitudes, and falsifies the simpler possibility that positivity appears merely after quotienting constants.

The arithmetic input is classical: T. M. Apostol, *Resultants of cyclotomic polynomials*, Proc. Amer. Math. Soc. **24** (1970), 457–462, gives the prime-power support used in (2). Conditional negative type and its connection with positive-definite/centered Gram kernels are classical Schoenberg theory; see I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. **44** (1938), 522–536. No novelty is claimed for either theorem.

A bounded prior-art audit using combinations of `cyclotomic resultant`, `conditionally negative definite`, `conditionally positive definite`, `negative type`, and `Schoenberg` did not locate a direct treatment of the normalized cyclotomic-resultant kernel (1) with the exact mixed-prime witness (6). The novelty claim is therefore deliberately narrow: the exact three-shell obstruction (18), its arithmetic matched control (19), and the consequence for the current Mathia zero-order-resultant positivity route.

## 7. Consequence for the Weil-positivity search

`WP-145` left open the possibility that arithmetic cancellation should be preserved before positivity rather than differentiated away. `WP-146` narrows that opening: **preserving the zero-order resultant is necessary for this route but ordinary conditional positivity is still too weak a global mechanism.** The first mixed-prime chain with unequal critical labels already carries both signs after centering.

A viable continuation must therefore introduce non-separable cross-prime or finite--archimedean structure before the positivity theorem, while preserving the exact prime-power selector. Examples not ruled out here include a canonical non-additive completion, a genuinely coupled cohomological/intersection quotient, or a boundary construction whose admissible subspace is forced globally rather than by ordinary mean-zero centering. Any such mechanism must explain independently why its added structure is canonical and why matched non-arithmetic controls do not reproduce the same output.
