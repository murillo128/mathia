# PL-263 — Least-eigenvalue shifting can force real Weil-pencil spectra under off-line zero data

## Claim

A finite Hilbert–Pólya construction built from Weil's explicit formula does **not** acquire RH-localizing content merely because one subtracts the algebraically smallest eigenvalue of its Weil matrix and obtains a Hermitian-definite generalized eigenproblem with real spectrum. Yaoming Shi's 2026 finite Prime–Weil construction supplies an exact matched control: in the zero-side model, hypothetical off-critical-line zero pairs give the expected nonreal spectral quartets in the natural **unshifted indefinite interpolation pencil**, while subtracting the least eigenvalue from the same paired matrix creates a positive metric and therefore a **real sign-paired spectrum**. The latter is a different spectral problem and can remain real even when the input zero data violate RH.

Consequently, for the current `prime_lattice` Weil-form program, the RH-sensitive invariant cannot be spectral reality of a ground-state-shifted finite pencil by itself. It must retain information that the scalar shift does not erase: most directly the sign/inertia of the unshifted Weil form, or a prime-to-zero transfer theorem that preserves an RH-sensitive indefinite structure rather than manufacturing positivity before localization is established.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route “subtract the least Weil eigenvalue, form a positive/Hermitian-definite quotient pencil, and use reality of its spectrum as evidence for RH localization.” The finite off-line calculation and the warning that the two pencils are different spectral problems are explicit in Shi, arXiv:2609.04908v1, Sections 7 and 9. The line-specific conclusion is a route restriction, not a novelty claim. This finding does **not** rule out Shi's broader Prime–Weil program, an unshifted construction, or a future theorem that proves the shift itself tends to the RH value with enough uniform control.

## 1. The unshifted zero-side pencil remembers off-line zeros

Use the spectral coordinate

\[
z_\rho=\frac{\rho-\tfrac12}{i}.
\]

RH is equivalent to every `z_rho` being real. A hypothetical symmetric off-line pair at positive ordinate can be written

\[
z_k=\gamma_k+i\eta_k,
\qquad
\overline z_k=\gamma_k-i\eta_k,
\qquad
\gamma_k>0,
\quad 0<\eta_k<\tfrac12.
\]

The corresponding zeta zeros are `1/2-eta_k+i gamma_k` and `1/2+eta_k+i gamma_k`; evenness and conjugation produce the quartet

\[
\{\pm z_k,\pm\overline z_k\}.
\]

Shi forms the paired zero-side real-symmetric matrix

\[
S_{N,L}^{(T,\mathrm{off})}
=
2\sum_{k=1}^{K}
\left(H_L^G(z_k)+H_L^G(\overline z_k)\right).
\]

For distinct quartet points and the dimension-matched choice `N=2K`, Proposition 7.1 gives

\[
\operatorname{In}
\left(S_{2K,L}^{(T,\mathrm{off})}\right)
=(2K,2K,1).
\]

Thus the natural paired off-line matrix is genuinely indefinite. Let `C_{2K,L}` denote the fixed zero-mean contrast matrix and `D_{L,2K}` the diagonal frequency matrix. The unshifted contrast pencil is

\[
G_{2K,L}^{\mathrm{off},0}
=C_{2K,L}^*S_{2K,L}^{(T,\mathrm{off})}C_{2K,L},
\]

\[
K_{2K,L}^{\mathrm{off},0}
=C_{2K,L}^*S_{2K,L}^{(T,\mathrm{off})}
D_{L,2K}C_{2K,L}.
\]

Theorem 7.2 gives the exact determinant identity

\[
\det\!\left(
 wG_{2K,L}^{\mathrm{off},0}
 -K_{2K,L}^{\mathrm{off},0}
\right)
=
\det\!\left(G_{2K,L}^{\mathrm{off},0}\right)
\prod_{k=1}^{K}
(w^2-z_k^2)(w^2-\overline z_k^{\,2}).
\]

Hence its generalized spectrum is exactly

\[
\bigcup_{k=1}^{K}
\{\pm z_k,\pm\overline z_k\}.
\]

This is an exact finite interpolation statement. It is **not** an independent derivation of zeta zeros: the zero parameters are inserted as data. Its value here is adversarial. It provides a mathematically controlled model in which an RH violation has a definite spectral signature before any positivity-enforcing normalization is applied.

## 2. Ground-state shifting destroys that localization test

Starting from the same real-symmetric paired matrix, order its eigenvalues

\[
\varepsilon_1^{\mathrm{off}}
\le \varepsilon_2^{\mathrm{off}}
\le\cdots
\le\varepsilon_{2N+1}^{\mathrm{off}}
\]

and define

\[
W_{N,L}^{\mathrm{off}}
=
S_{N,L}^{(T,\mathrm{off})}
-
\varepsilon_1^{\mathrm{off}} I.
\]

By construction,

\[
W_{N,L}^{\mathrm{off}}\succeq0.
\]

On the same zero-mean contrast space set

\[
G_{N,L}^{\mathrm{off}}
=C_{N,L}^*W_{N,L}^{\mathrm{off}}C_{N,L},
\qquad
K_{N,L}^{\mathrm{off}}
=C_{N,L}^*W_{N,L}^{\mathrm{off}}D_{L,N}C_{N,L}.
\]

The scalar shift preserves the divided-difference/rank-two commutator identity, so `K_{N,L}^{off}` is real symmetric. Under the explicit hypotheses that the least eigenvalue is simple and

\[
G_{N,L}^{\mathrm{off}}\succ0,
\]

Shi's Theorem 9.1 states that

\[
K_{N,L}^{\mathrm{off}}y
=
\mu G_{N,L}^{\mathrm{off}}y
\]

is a Hermitian-definite pencil. Therefore **all generalized eigenvalues are real**. With the centrosymmetry/parity hypotheses its spectrum is additionally sign-paired.

The crucial logical point is that this reality is automatic from the newly created positive metric. In the dimension-matched off-line model, Shi compares the two constructions explicitly: the unshifted pencil has inertia `(2K,2K)` and reconstructs the nonreal quartets, whereas the shifted pencil is positive definite and hence real. Unless the least eigenvalue is already zero and the two metrics coincide, the pencils are different and need not be similar. In particular there is no universal operation sending the quartet to the radial values

\[
\pm\sqrt{\gamma_k^2+\eta_k^2}.
\]

The shifted real numbers depend on the complete paired matrix. Thus the implication

\[
\text{shifted finite pencil has real spectrum}
\quad\Longrightarrow\quad
\text{input zeros lie on the critical line}
\]

is false even in the exact zero-side model designed to reproduce the divisor.

## 3. Prime-lattice interpretation

Shi's arithmetic matrices are genuinely inside the `prime_lattice` mandate rather than an unrelated matrix model. The Riemann explicit formula contains the finite-window non-archimedean term

\[
\sum_p\sum_{r\ge1}
\frac{\log p}{p^{r/2}}
\bigl(F(r\log p)+F(-r\log p)\bigr),
\]

with only finitely many prime powers surviving for compact logarithmic support. In exponent coordinates those locations are exactly the axis rays

\[
r e_p,
\qquad
\log(p^r)
=
\langle r e_p,(\log q)_q\rangle
=r\log p.
\]

So the arithmetic input uses the same prime-power skeleton isolated in `PL-013` and the finite Weil compressions of `PL-259`–`PL-261`. No mixed-support exponent vector creates the positive metric in Section 9: positivity is obtained globally by subtracting the algebraically smallest eigenvalue from the assembled real-symmetric matrix.

That distinction matters. The unshifted Weil form has an RH-equivalent sign interpretation, and `PL-259` shows that its finite inertia already detects a positive proportion of critical-line simple zeros unconditionally. `PL-261` sharpens detectability further: every RH failure gives a negative direction in some finite semilocal compression. A least-eigenvalue shift deliberately removes exactly this negative-direction information before the generalized spectral problem is solved.

Therefore the finite Prime–Weil spectral program and the current source-side positivity program should not be conflated. The former may still approximate zero ordinates after an appropriate transfer theorem; the latter needs arithmetic control that proves the original Weil metric has the required sign. **Created positivity is not evidence for source-side Weil positivity.**

## 4. The remaining transfer problem is the nontrivial part

Shi carefully separates exact finite algebra from the missing analytic limit. For fixed test functions and uniformly norm-bounded families, simultaneous prime-power and zero-tail truncations are controlled. Under RH, an exact finite-zero interpolation vector is a trial state for the arithmetic matrix and yields

\[
\lambda_{\min}(S_{N,N})\longrightarrow0.
\]

But this is conditional and controls only a distinguished direction. Recovering the individual zero ordinates from the **prime-side** matrices requires a moving-dimension relative perturbation theorem for the entire generalized pencil, including lower bounds or preconditioned estimates for the compressed metric and exclusion of spectral pollution. Shi explicitly lists this as the central unresolved transfer problem.

This prevents the opposite overclaim: `PL-263` does not say that the prime-side shifted matrices converge to a real spectrum under an actual RH violation. No such moving-dimension theorem is available. The exact off-line zero-side model proves the narrower and sufficient falsification statement: **spectral reality after positivity-enforcing shift is logically insensitive to off-line input and hence cannot itself be the localization mechanism.** Any successful prime-side construction must use additional information that is not a generic consequence of making the metric positive.

## 5. Novelty and prior-art audit

The principal finite facts are prior art from Yaoming Shi, *Construction of Finite Hilbert--Pólya Matrices from Weil's Explicit Formula*, arXiv:2609.04908v1 (submitted 4 September 2026). In particular:

- Sections 7.1–7.2 prove the indefinite inertia and exact reconstruction of hypothetical off-line quartets.
- Section 9 proves that least-eigenvalue shifting creates a positive Hermitian-definite pencil with real sign-paired spectrum and explicitly warns that it is a different spectral problem.
- Section 1.5 and Section 6.1 isolate the still-missing moving-dimension relative prime-to-zero transfer theorem.

Shi credits an earlier finite real-spectrum ground-state quotient to Sören Lemke as a communicated construction; the current literature search did not locate an independent public theorem by Lemke that changes the route restriction above. More broadly, the generic observation that Hermitian-definite pencils have real spectrum is standard linear algebra and is not claimed as new.

This finding is not a duplicate of `PL-257`. `PL-257` rules out the generic inference from a canonical self-adjoint dilation generator to RH when zeta zeros enter only through scattering/resonance data. Here the obstruction is finite and sharper: **the very normalization used to manufacture a positive Weil metric can make the quotient spectrum real when the supplied zero divisor is explicitly off-line.** It is also complementary to `PL-259` and `PL-261`, which retain the unshifted Weil sign/inertia as the RH-sensitive quantity.

No credible literature located in this pass supplies an arithmetic theorem turning the positivity-enforcing shift itself into an RH-localizing invariant. The source paper instead makes the distinction explicit, so `PL-263` is stored as a prior-art redirect rather than as a discovery.

## 6. Falsification gate for future finite Weil spectra

A future finite-dimensional Hilbert–Pólya claim based on a Weil matrix should be stress-tested against the following matched control before spectral reality is treated as evidence:

1. Feed the corresponding zero-side finite model a symmetric off-critical quartet `±(gamma+i eta), ±(gamma-i eta)` with `eta != 0`.
2. Verify that the **unshifted** construction retains a nonreal or indefinite RH-sensitive signature.
3. Apply every proposed ground-state subtraction, quotient, whitening, or positive-metric normalization.
4. Ask whether the claimed spectral property now holds automatically from positivity/Hermiticity even though the input remains off-line.

If it does, that property is not an RH-localizing invariant. A route survives this finding only if it proves something additional—such as nonnegativity of the unshifted arithmetic Weil form, convergence of the shift to the correct unshifted value with sign control, a determinant identity that preserves the original divisor, or a relative transfer theorem whose hypotheses themselves exclude the off-line control.

## Consequence for the research line

The live frontier remains the one isolated by `PL-259`–`PL-261`: **source-side sign control of the unshifted Weil core**. The new paper gives a useful negative gate for an adjacent spectral shortcut. Real eigenvalues obtained only after subtracting `lambda_min` must not be counted as progress toward RH localization, because the same mechanism survives an exact hypothetical off-line zero model.

The safe directional rule is therefore:

\[
\boxed{
\text{preserve/test unshifted Weil sign or inertia before spectral normalization.}
}
\]

A finite spectral construction becomes relevant to the target only when the arithmetic prime-power side supplies the missing sign, or when a rigorous prime-to-zero transfer preserves an invariant that fails for the off-line quartet control.

## Sources

- Yaoming Shi, “Construction of Finite Hilbert--Pólya Matrices from Weil's Explicit Formula,” arXiv:2609.04908v1 [math.GM], submitted 4 September 2026. https://arxiv.org/abs/2609.04908. Main source for the finite Prime–Weil construction, the exact off-line interpolation quartet, the least-eigenvalue-shifted positive pencil, and the unresolved relative transfer problem.
- Levent Alpöge and Ralph Furman, “More than two thirds of the zeta zeros are simple and on the critical line,” arXiv:2608.13637v2 [math.NT], 2026. Comparison anchor for the unshifted finite-Weil inertia method in `PL-259`.
- André Weil, “Sur les ‘formules explicites’ de la théorie des nombres premiers,” 1952. Classical source for the explicit-formula quadratic form underlying the prime-power axis-ray interpretation.