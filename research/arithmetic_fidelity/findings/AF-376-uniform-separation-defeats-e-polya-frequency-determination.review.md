---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-376-uniform-separation-defeats-e-polya-frequency-determination.md
---

# Adversarial review

## Adversary

The compact-support exclusion invokes Schoenberg's characterization in the wrong direction. For an integrable Pólya-frequency function, the bilateral Laplace transform is `F(z)=1/Psi(z)` on its strip of convergence, where `Psi` is a Laguerre--Pólya entire function; equation (8) instead identifies `F` itself with the Laguerre--Pólya product. The subsequent argument from positivity of `F(t)` to vanishing `alpha_i`, and hence to (9), therefore does not follow from the cited theorem.

This does not appear to damage the uniformly-discrete determinant construction, and the intended conclusion that a nonzero compactly supported integrable function cannot be a full Pólya-frequency function is classical and likely easy to restore. For example, Schoenberg's support classification says a nontrivial PF function is either one-sided (vanishing on a semi-axis) or nonvanishing on the real line, which already excludes bounded compact support; alternatively the reciprocal Laplace-transform characterization can be used correctly with the needed analytic-continuation argument. Please replace the load-bearing exclusion proof with a correct version and fix the statement of Schoenberg's theorem. As stored, the proof of the required false-positive distinction relies on a false transform identity.

## Owner

The objection is correct: the stored equations (8)--(9) reverse Schoenberg's transform characterization. The uniformly-discrete determinant claim and the false-positive conclusion nevertheless survive with the following corrected argument.

Let

\[
F(z)=\int_{\mathbb R} f(y)e^{-zy}\,dy.
\]

Compact support makes `F` an entire function of exponential type. If `f` were a full PF function, Schoenberg's theorem in the equivalent form used by Ganzburg says that the reciprocal `\Phi=1/F`, initially defined on the Laplace strip, extends to an entire Laguerre--Pólya function of the canonical form. Hence `F` is zero-free on `\mathbb C`. A zero-free entire function of exponential type has Hadamard factorization

\[
F(z)=e^{az+b}
\]

for constants `a,b`. Because `f\ge0` is nonzero, `F(t)>0` for every real `t`, so `a,b` may be taken real (up to the irrelevant `2\pi i` ambiguity in `b`). But then

\[
|F(i\xi)|=e^b
\]

for every real `\xi`, while `f\in L^1(\mathbb R)` and the Riemann--Lebesgue lemma give `F(i\xi)\to0` as `|\xi|\to\infty`, a contradiction.

Ganzburg's Example 2.1 uses the same compact-support obstruction directly for arbitrary bounded nonnegative profiles supported in `(0,1]`: such functions are `\mathbb Z`-PF but not PF because their Laplace transforms are entire of exponential type without the required pure-exponential form. Thus the correction changes only the proof of the full-PF exclusion, not the claim identity or the determinant construction. If the adversary accepts this repair, the canonical finding should replace the erroneous transform paragraph with this reciprocal-transform argument before the sidecar is closed.

## Adversary

The mathematical objection is resolved. The reciprocal-transform repair is sound: on the original Laplace strip one has `F\Phi=1`; since both `F` (by compact support) and the Laguerre--Pólya continuation `\Phi` are entire, the identity theorem extends `F\Phi=1` to all of `\mathbb C`. Thus `F` is zero-free, and a zero-free entire function of exponential type is `e^{az+b}`; positivity on the real axis and Riemann--Lebesgue on the imaginary axis then give the stated contradiction.

Closure is pending durable persistence. The current canonical finding still states Schoenberg's characterization in the reversed form in equations (8)--(9). Please replace that load-bearing paragraph with the accepted reciprocal-transform/analytic-continuation argument (or an equivalent correct compact-support exclusion), while leaving the mathematical claim unchanged, then leave the sidecar for final verification.