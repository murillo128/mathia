# WP-029 — Even commutator energies radialize, but positive one-sided parts retain Boolean orientation

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the square/modulus/even-functional-calculus repair of the non-`Q`-invariant Boolean Mangoldt insertion from WP-018/WP-020, together with the ordinary full-trace and Boolean-supertrace readouts of arbitrary scalar spectral functions. The stronger statement that *every* positive spectral function of the single commutator becomes radial is false: the positive part `(C_alpha)_+` is a canonical counterexample and retains the oriented Boolean edge operator. Thus positivity alone does not erase incidence information, but the standard positive commutator energies do, and the two canonical global scalar readouts still fail to recover `Lambda`.

## 1. Exact Boolean commutator

For an exponent vector

\[
\alpha=v(n),
\qquad
S=\{p:\alpha_p>0\},
\qquad
r=|S|,
\]

identify the backward Boolean cube with

\[
\mathcal H_\alpha\cong\Lambda^*\mathbb C^r.
\]

Let `epsilon_p` be exterior multiplication, `iota_p=epsilon_p^*` contraction, and

\[
N_p=\epsilon_p\iota_p,
\qquad
a_p=\log p.
\]

The canonical Boolean Hodge supercharge and the WP-018 residual-energy insertion are

\[
Q_\alpha=\sum_{p\in S}(\epsilon_p+\iota_p),
\tag{1}
\]

and

\[
R_\alpha=E(\alpha)I-\sum_{p\in S}a_pN_p.
\tag{2}
\]

The successful arithmetic readout remains

\[
\operatorname{Str}R_\alpha=\Lambda(n),
\tag{3}
\]

while `[R_alpha,Q_alpha]` is nonzero. Using

\[
[N_p,\epsilon_p]=\epsilon_p,
\qquad
[N_p,\iota_p]=-\iota_p,
\]

define the self-adjoint commutator

\[
C_\alpha:=i[R_\alpha,Q_\alpha]
=\sum_{p\in S}a_p\gamma_p,
\qquad
\gamma_p:=i(\iota_p-\epsilon_p).
\tag{4}
\]

The canonical anticommutation relations give

\[
\gamma_p^2=I,
\qquad
\gamma_p\gamma_q+\gamma_q\gamma_p=0
\quad(p\ne q).
\tag{5}
\]

Hence

\[
\boxed{C_\alpha^2=A(n)^2I},
\qquad
A(n):=\left(\sum_{p\mid n}(\log p)^2\right)^{1/2}.
\tag{6}
\]

For every `n>1`, the spectrum of `C_alpha` is `{+A(n),-A(n)}` with equal multiplicities `2^{r-1}`.

## 2. What really radializes: even positive energy

Equation (6) gives immediately

\[
|C_\alpha|=A(n)I,
\qquad
C_\alpha^*C_\alpha=A(n)^2I.
\tag{7}
\]

More generally, if `f` is even on `{+/-A(n)}`, then

\[
f(C_\alpha)=f(A(n))I.
\tag{8}
\]

Thus every standard even positive commutator energy — square/carré-du-champ, modulus, positive even powers, heat functions of `C_alpha^2`, resolvents of `C_alpha^2`, and completely monotone functions of `C_alpha^2` — factors only through the Euclidean radius `A(n)`.

That loses the Boolean inclusion-exclusion selecting prime powers. For a prime power,

\[
A(p^k)=\log p=\Lambda(p^k),
\]

but already

\[
A(6)=\sqrt{(\log2)^2+(\log3)^2}>0,
\qquad
\Lambda(6)=0.
\tag{9}
\]

So the canonical positive **energy** attached to the commutator is unconditional but arithmetically too coarse.

## 3. Positivity alone does not imply radialization

The two-point spectrum also classifies arbitrary scalar spectral functions exactly. For any scalar `f`,

\[
f(C_\alpha)
=u_f(A)I+v_f(A)C_\alpha,
\tag{10}
\]

where

\[
u_f(A)=\frac{f(A)+f(-A)}2,
\qquad
v_f(A)=\frac{f(A)-f(-A)}{2A}.
\tag{11}
\]

If `f>=0` on the spectrum, then `f(C_alpha)` is positive, but the coefficient `v_f(A)` need not vanish. The canonical counterexample is

\[
f(t)=t_+:=\max(t,0),
\]

for which

\[
\boxed{
(C_\alpha)_+
=\frac{A(n)I+C_\alpha}{2}\succeq0.
}
\tag{12}
\]

Whenever `r>=2`, this operator is not scalar. Its off-diagonal part is `C_alpha/2`, so it still contains the oriented Boolean edge differential and the individual weights `log p`.

Therefore the implication

\[
\text{positive spectral functional calculus}
\Longrightarrow
\text{radial/scalar observable}
\]

is false. What radializes automatically is the **even** functional calculus, equivalently functions of `C_alpha^2`.

This boundary matters: an incidence-sensitive compression, boundary functional, or globally coupled use of `(C_alpha)_+` is not excluded by the Clifford identity alone.

## 4. The canonical scalar readouts still fail

Although a general positive `f(C_alpha)` can retain oriented incidence information internally, the two most intrinsic scalar readouts do not recover the Mangoldt selector.

Because `C_alpha` is odd for the Boolean parity grading `Gamma`,

\[
\operatorname{Tr}(\Gamma)=0,
\qquad
\operatorname{Tr}(\Gamma C_\alpha)=0.
\]

Combining this with (10) yields

\[
\boxed{
\operatorname{Str}f(C_\alpha)=0
}
\tag{13}
\]

for every scalar spectral function `f` and every `r>=1`. Thus restoring the Boolean supertrace annihilates the entire spectral functional calculus of the single commutator instead of giving `Lambda(n)`.

The ordinary full trace is

\[
\boxed{
\operatorname{Tr}f(C_\alpha)
=2^{r-1}\bigl(f(A(n))+f(-A(n))\bigr).
}
\tag{14}
\]

It depends only on `r` and `A(n)`. In particular, an ordinary positive trace of `(C_alpha)_+` equals

\[
2^{r-1}A(n),
\]

which is strictly positive on every multi-prime composite and therefore does not have Mangoldt support.

There is also a basis-level version of the same limitation. Since `C_alpha` has zero diagonal in the Boolean vertex basis,

\[
\langle e_T,f(C_\alpha)e_T\rangle=u_f(A(n))
\tag{15}
\]

for every vertex `T`. Hence all diagonal positive energies are radial even when the full positive operator is not.

The remaining live possibility would have to use the **off-diagonal incidence data** in a canonical positive pairing/compression before collapsing to a scalar.

## 5. Critical attenuation does not repair the even-energy route

The finite Weil coefficient requires the scalar attenuation

\[
e^{-E(\alpha)/2}=n^{-1/2}.
\]

Applied to the canonical positive commutator modulus,

\[
n^{-1/2}|C_\alpha|
=\frac{A(n)}{\sqrt n}I\ge0,
\tag{16}
\]

but the support defect remains:

\[
\frac{A(6)}{\sqrt6}>0,
\qquad
\frac{\Lambda(6)}{\sqrt6}=0.
\tag{17}
\]

Thus the critical half-weight is not the missing selector. The successful cancellation still lives in the signed Boolean readout (3).

Multiplying `R_alpha` by a positive scalar function of `C_alpha^2` and then taking a supertrace merely rescales `Lambda(n)`; the arithmetic information still comes from the signed insertion `R_alpha` and its supertrace, not from the positive commutator energy.

## 6. Matched generalized-prime control

Nothing above uses a special theorem about rational primes. Replace the edge weights `log p` by arbitrary positive numbers `a_j` on a free commutative monoid. Then

\[
C=\sum_j a_j\gamma_j,
\qquad
C^2=\left(\sum_j a_j^2\right)I,
\tag{18}
\]

and all conclusions (7)--(15) persist.

Therefore the positive even-energy theorem is a universal Clifford/Fock-space fact and is too generic to encode RH-specific arithmetic by itself. The fact that `(C)_+` retains orientation is equally universal; it supplies a surviving information channel, not yet an arithmetic sign theorem.

## 7. Prior-art and novelty audit

No novelty is claimed for the CAR/exterior-algebra realization, Clifford identity, positive/negative spectral parts, or the decomposition (10). These are standard finite-dimensional functional-calculus facts.

The Mathia-specific content is the exact classification of what happens to the **particular Boolean commutator forced by WP-018/WP-020**:

```text
successful signed Mangoldt insertion R_alpha
    -> weighted Boolean commutator C_alpha
    -> even positive energy |C_alpha| or C_alpha^2
         => exact radial collapse A(n), wrong support
    -> general positive spectral part such as (C_alpha)_+
         => orientation survives internally
         => full trace is radial and supertrace is zero
```

So the durable negative result is not a no-go for every positive function of the commutator. It is the sharper statement that the standard energy repair and the standard scalar readouts cannot convert the Boolean Mangoldt cancellation into an independent positive scalar theorem.

## 8. Boundary of the obstruction

This finding does **not** rule out:

- an incidence-sensitive compression or boundary functional of `(C_alpha)_+` whose positivity is canonical and whose scalar output has Mangoldt support;
- a globally coupled finite/archimedean operator formed before any even squaring/modulus operation;
- higher multilinear expressions using several distinct commutators;
- a relative, APS/eta, transgression, or trace-defect construction whose sign follows from an independent theorem;
- a global differential in which `R_alpha` is only the finite shadow and the archimedean/polar terms arise from the same object.

Any such route must still pass two tests that the single-commutator energy fails: it must preserve the oriented Boolean inclusion-exclusion long enough to kill multi-prime composites, and its final nonnegativity must come from geometry rather than from re-inserting the Mangoldt selector or Weil functional by hand.

## 9. Falsification criterion and consequence

The exact claims to audit are:

1. equations (1)--(6) for the Boolean commutator;
2. even functional calculus gives the scalar collapse (8);
3. `(C_alpha)_+=(A I+C_alpha)/2` is positive and non-scalar whenever the commutator is nonzero;
4. every scalar spectral function has the form (10);
5. its Boolean supertrace vanishes as in (13);
6. its full trace is the radial quantity (14);
7. every Boolean-vertex diagonal matrix element is radial as in (15).

All are finite-dimensional algebra and can be checked on the first two-prime cube `n=p^a q^b`.

The research consequence is a narrower but more reliable fork than the discarded blanket radialization claim. **Global coupling need only occur before the commutator is reduced to an even energy or a radial scalar readout; positivity itself does not yet force loss of orientation.** The live target is therefore an incidence-sensitive positive compression/readout whose sign is structural and whose finite scalar shadow is exactly the Mangoldt/Weil weight rather than merely `A(n)`.

## Internal dependencies

- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-020-q-invariant-coupled-hodge-insertions-still-collapse-to-index.md`
- `research/weil_positivity/findings/WP-016-prime-lattice-hodge-positivity-cancels-out-of-the-arithmetic-supertrace.md`
