# WP-136 — Repeated-prime full-chord continuous positive spectral traces are extensive

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + POSITIVE-FORM + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION` for fixed continuous nonnegative spectral traces of the complete repeated-prime full-chord fiber spectrum classified by `PC-156`.

`WP-135` proved that the canonical coarse sector of the normalized full primitive-shell inverse-square chord energy is reducing under repeated-prime refinement, so Schur/Feshbach elimination and fixed positive functional calculus followed by coarse compression are exactly stationary. It deliberately left open a different escape: perhaps a positive scalar observable of the **entire fine spectrum**, including every nonzero deck character, can see the repeated prime-power depth. `PC-156` makes that route explicit enough to test.

The result is negative for the natural continuous positive class. Let

\[
A_N:=N^{-2}L_N^{\rm int}
\]

and fix a coarse modulus `d`. For every refinement factor `m` satisfying

\[
\operatorname{rad}(m)\mid\operatorname{rad}(d),
\tag{1}
\]

`PC-156` gives

\[
A_{dm}
\cong
\bigoplus_{k=0}^{m-1}
D_{m,k}\,\mathcal P_d(k/m)\,D_{m,k}^{-1},
\tag{2}
\]

where the `D_{m,k}` are unitary diagonal conjugations and

\[
\mathcal P_d(t)
=
\frac1{d^2}
\left(
L_d^{\rm int}
+\frac t2 C_d
-\frac{t^2}{2}I
\right),
\qquad 0\le t\le1.
\tag{3}
\]

Thus repeated-prime refinement does not create a new family of positive operators: it samples one fixed finite-dimensional Hermitian quadratic pencil on an increasingly fine rational grid.

Let `Phi` be any **fixed continuous scalar function** that is nonnegative on a compact interval containing

\[
\bigcup_{0\le t\le1}\sigma(\mathcal P_d(t)).
\]

Then `Phi(\mathcal P_d(t))\succeq0`. Define

\[
h_\Phi(t):=\operatorname{Tr}\Phi(\mathcal P_d(t))\ge0,
\qquad
S_\Phi(m):=\operatorname{Tr}\Phi(A_{dm}).
\tag{4}
\]

Equations (2)--(3) imply the exact sampling identity

\[
\boxed{
S_\Phi(m)
=
\sum_{k=0}^{m-1}h_\Phi(k/m).
}
\tag{5}
\]

Since `h_Phi` is continuous and nonnegative, ordinary Riemann sums give

\[
\frac{S_\Phi(m)}m
\longrightarrow
I_\Phi
:=
\int_0^1h_\Phi(t)\,dt
\ge0.
\tag{6}
\]

There are only two possibilities:

\[
\boxed{
I_\Phi=0
\Longrightarrow
h_\Phi\equiv0
\Longrightarrow
S_\Phi(m)=0\ \text{for every }m,
}
\tag{7}
\]

or

\[
\boxed{
I_\Phi>0
\Longrightarrow
S_\Phi(m)=I_\Phi m+o(m).
}
\tag{8}
\]

Hence every fixed continuous nonnegative full-fiber spectral trace is either identically zero or **extensive in the deck multiplicity**. It cannot directly generate a nonzero depth-independent prime-power birth.

## 1. Prime-power matched control

Take a fixed prime `p`, choose `d=p^a`, and refine by `m=p^r`. Then `dm=p^{a+r}`, whereas the arithmetic shell weight remains

\[
\Lambda(p^{a+r})=\log p
\qquad(r\ge0).
\tag{9}
\]

If `I_Phi>0`, (8) gives

\[
S_\Phi(p^{r+1})-S_\Phi(p^r)
=
I_\Phi(p-1)p^r+o(p^r),
\tag{10}
\]

which grows exponentially in the depth parameter rather than staying equal to `log p`. If instead one divides by the deck multiplicity, then

\[
\frac{S_\Phi(p^r)}{p^r}\longrightarrow I_\Phi,
\tag{11}
\]

so consecutive normalized shell increments tend to zero. The zero-density case `I_Phi=0` gives no shell signal at all.

This is a matched control on the exact arithmetic direction that matters here: the geometric refinement repeatedly deepens the same already-present prime while the von Mangoldt coefficient is unchanged.

## 2. Exact identity-trace check

The simplest genuinely positive spectral observable already exhibits the obstruction without an asymptotic theorem. Since `A_{dm}\succeq0`, take

\[
\Phi(x)=x.
\]

Write `q=phi(d)`. `PC-156` gives

\[
\operatorname{Tr}C_d=q,
\tag{12}
\]

and therefore from (3)

\[
\operatorname{Tr}\mathcal P_d(t)
=
\operatorname{Tr}A_d
+
\frac{q}{2d^2}(t-t^2).
\tag{13}
\]

Using

\[
\sum_{k=0}^{m-1}
\left(
\frac{k}{m}-\frac{k^2}{m^2}
\right)
=
\frac{m^2-1}{6m},
\tag{14}
\]

one obtains the exact finite formula

\[
\boxed{
\operatorname{Tr}A_{dm}
=
m\operatorname{Tr}A_d
+
\frac{q(m^2-1)}{12md^2}
=
m\left(\operatorname{Tr}A_d+\frac{q}{12d^2}\right)
-
\frac{q}{12d^2m}.
}
\tag{15}
\]

Thus even before taking a limit, the raw positive trace has the form `alpha*m-beta/m`. Along `m=p^r` its shell increment is not a depth-independent `log p`. This exact identity is a useful sanity check that the Riemann-sum obstruction is describing the actual full-chord spectrum rather than an artefact of a loose estimate.

## 3. The theorem extends to fixed continuous positive block readouts

The scalar-functional-calculus presentation is not essential. Let

\[
B_d:[0,1]\to M_q(\mathbb C)
\]

be any fixed continuous field with `B_d(t)\succeq0`, canonically constructed from the fiber pencil but independent of the refinement depth. The full uniform deck trace

\[
S_B(m)
:=
\sum_{k=0}^{m-1}\operatorname{Tr}B_d(k/m)
\tag{16}
\]

obeys the same dichotomy because `t\mapsto\operatorname{Tr}B_d(t)` is continuous and nonnegative:

\[
S_B(m)=0\ \text{for all }m
\quad\text{or}\quad
S_B(m)=m\int_0^1\operatorname{Tr}B_d(t)\,dt+o(m).
\tag{17}
\]

So the obstruction is not peculiar to choosing a particular `Phi`; it is the combination of **fixed continuous positive fiber data plus uniform tracing over the complete cyclic deck spectrum**.

## 4. Adversarial controls

Several apparent escapes do not contradict the claim.

First, applying a logarithm **after** the positive trace can manufacture the desired scale: if `S(p^r)\sim I p^r`, then

\[
\log S(p^{r+1})-\log S(p^r)\longrightarrow\log p.
\tag{18}
\]

But this is a nonlinear scalarization, not a positive quadratic form or positive operator trace. Indeed, `log(dim U(p^{a+r}))` already contains a `log p` increment for the same cardinality reason, with no arithmetic Weil mechanism. Such a post-processing therefore cannot count as an intrinsic positive derivation of the Mangoldt term.

Second, determinants, pseudodeterminants and `Tr log` are outside the theorem because they are nonlinear or singular at zero. This exclusion is material rather than cosmetic: `WP-043` already showed that a cycle-Laplacian shell log-determinant can recover `log p`. That route fails this branch for a different reason—the spectral positivity is not the Weil pairing—so the present result must not be strengthened into a no-go for all nonlinear fine-spectrum observables.

Third, subtracting the extensive bulk,

\[
S_\Phi(m)-mI_\Phi,
\tag{19}
\]

can expose subextensive corrections, but the subtraction destroys the raw positive trace. It is not an admissible rescue unless a separate Mathia-native geometric theorem canonically supplies the counterterm while preserving the required global sign. An arbitrary renormalization would violate the branch mandate.

Fourth, allowing an `m`-dependent `Phi_m`, deck weights chosen after seeing `m`, or a narrowing window around a selected character can evade the Riemann-sum conclusion. Those choices would need an intrinsic geometric derivation and an independent sign theorem; otherwise they are hand-picked kernels in a different notation.

Finally, singular endpoint-supported positive measures are not covered. Earlier repeated-prime controls, especially `WP-083`, already warn that arithmetic information can hide at singular endpoints after a homogeneous positive bulk has flattened. The present theorem therefore leaves that genuinely different possibility open.

## 5. Consequence for the Weil-positivity search

Combining `WP-135` with the present result closes two complementary natural uses of the exact `PC-156` repeated-prime fibers:

- the `k=0` coarse sector and every Schur/Feshbach feedback from the other sectors are exactly stationary;
- a fixed continuous positive trace over **all** sectors is zero or extensive.

Thus the complete repeated-prime full-chord spectrum does not recover the prime-power Mangoldt tower through either canonical coarse positive response or fixed continuous positive whole-spectrum trace. The obstruction is structural: refinement merely densifies the sampling grid of a fixed finite-dimensional pencil.

This does **not** eliminate a distinguished nonzero deck character selected intrinsically by new geometry, refinement-dependent concentration with a canonical boundary theorem, rectangular operators retaining several conductor levels at once, nonlinear cross-sector interactions, genuinely new-prime fibers, singular spectral scalarizations, or finite--archimedean coupling performed before the deck symmetry is imposed. Any such survivor still has to produce both the finite and archimedean/global terms and obtain nonnegativity independently of RH or inserted zero data.

## 6. Prior-art and novelty audit

The analytic step in (5)--(8) is deliberately not claimed as new: sampling a fixed continuous band function on finer cyclic/Floquet grids and passing to its Riemann-sum density is classical elementary spectral analysis. `WP-104` already found an analogous extensive-density obstruction for a different positive cover-trace construction.

The branch-specific advance is narrower. `PC-156` supplies an **exact Mathia-native quadratic fiber pencil** for repeated-prime full-chord refinement, and `WP-135` explicitly left scalar observables of the complete fine spectrum open. Equations (5)--(17) close the fixed continuous nonnegative trace part of that escape, with the prime-power tower as a matched arithmetic control. `WP-043` is retained as the adverse comparison showing why singular/nonlinear log-determinant readouts must remain outside the claim.

No zero data, zeta determinant, RH-equivalent Weil functional, or hand-picked kernel enters the proof. Positivity is intrinsic to the chosen nonnegative functional calculus; its failure is that this positivity scales in the wrong way.

## 7. Status

This is a **substantive negative finding**. It eliminates fixed continuous nonnegative whole-fiber/full-spectrum trace readouts as a repeated-prime Mangoldt mechanism for the exact `PC-156` full-chord pencil. It does not eliminate singular or nonlinear scalarizations, canonically distinguished/refinement-dependent deck sectors, multi-level operators, cross-sector interactions, new-prime fibers, or finite--archimedean coupling before symmetry reduction.

### Internal evidence

- [WP-135](WP-135-repeated-prime-full-chord-feshbach-self-energy-is-zero.md)
- [WP-104](WP-104-cover-dirichlet-log-jensen-positivity-has-extensive-harmonic-trace-density.md)
- [WP-083](WP-083-homogeneous-cover-jensen-positivity-is-flat-and-mangoldt-support-needs-a-singular-endpoint.md)
- [WP-043](WP-043-cycle-laplacian-shell-logdet-recovers-mangoldt-but-spectral-positivity-is-the-wrong-pairing.md)
- [PC-156](../../prime_circle/findings/PC-156-repeated-prime-full-chord-fibers-collapse-to-a-fixed-quadratic-pencil.md)
