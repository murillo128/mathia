# PF-154 — the first-resolvent det2 has no independent zero set

**Status:** `LITERATURE+DERIVED + EXACT-CONDITIONAL + NEGATIVE/BOUNDARY`. PF-147 shows that the still-open global square-resolvent trace-class gate would place the exact prime flute and its exact all-composite shift clone in the Hilbert--Schmidt first-resolvent regime and therefore make a canonical modified Fredholm determinant `det_2` available. The present finding closes the most immediate zeta-like interpretation of that object. For the natural perturbation determinant of the bounded resolvent pair, the exponential regularization in `det_2` never creates zeros: on the resolvent set of the reference operator, its zeros are exactly the ordinary discrete eigenvalues of the numerator bounded resolvent. Thus `det_2` can package relative discrete Laplace spectrum, but it does not supply an additional zero-selection mechanism, resonance divisor, or RH-relevant zero set merely from Hilbert--Schmidt comparability.

## Claim

Let `P_0,P_1 >= 0` be the two self-adjoint Laplacians after one fixed admissible common-Hilbert-space identification, with `P_0` the exact prime-flute Laplacian and `P_1` the exact all-composite shift-clone Laplacian, and put

\[
R_i=(P_i+1)^{-1},\qquad i=0,1.
\tag{1}
\]

Assume only that the first relative resolvent is Hilbert--Schmidt,

\[
\boxed{D:=R_1-R_0\in\mathcal S_2.}
\tag{2}
\]

For the actual prime/shift pair this conclusion is currently conditional: PF-147 derives (2) from the still-open global PF-146 gate

\[
R_1^2-R_0^2\in\mathcal S_1.
\tag{3}
\]

For every `z in rho(R_0)`, define

\[
K(z)=D(R_0-z)^{-1}\in\mathcal S_2
\tag{4}
\]

and the modified perturbation determinant

\[
\boxed{
\Delta_2(z)=\det{}_2\!\left(I+K(z)\right).
}
\tag{5}
\]

Then

\[
\boxed{
\Delta_2(z)=0
\iff
z\in\sigma(R_1),
\qquad z\in\rho(R_0).
}
\tag{6}
\]

Moreover, because `D in S_2` is compact,

\[
\sigma_{\mathrm{ess}}(R_1)=\sigma_{\mathrm{ess}}(R_0).
\tag{7}
\]

Hence every zero in (6) is an isolated finite-multiplicity eigenvalue of `R_1` lying outside the common essential spectrum. For a nonzero zero `z`, this is equivalent under (1) to the ordinary Laplace eigenvalue

\[
\boxed{
\lambda=z^{-1}-1
\in\sigma_{\mathrm{disc}}(P_1).
}
\tag{8}
\]

Therefore the natural first-resolvent `det_2` has **no independent zero divisor** beyond the relative discrete spectrum already present in the chosen Laplacian. Reversing the orientation of the perturbation exchanges the roles of `R_0` and `R_1`; it does not create a new arithmetic set.

## 1. The factorization reduces every zero to ordinary noninvertibility

The elementary relative-resolvent factorization is

\[
I+K(z)
=I+(R_1-R_0)(R_0-z)^{-1}
=(R_1-z)(R_0-z)^{-1}.
\tag{9}
\]

For `K in S_2`, the second regularized Fredholm determinant is

\[
\det{}_2(I+K)
=
\det\!\bigl((I+K)e^{-K}\bigr),
\tag{10}
\]

where `(I+K)e^{-K}-I` is trace class. The exponential `e^{-K}` is boundedly invertible, with inverse `e^K`. The ordinary Fredholm determinant in (10) vanishes exactly when its argument is noninvertible. Consequently

\[
\det{}_2(I+K)=0
\iff
I+K\text{ is noninvertible}.
\tag{11}
\]

The regularizing exponential changes normalization and the logarithmic expansion, but it is everywhere nonvanishing and cannot introduce or remove a Fredholm zero.

Applying (11) to (9), and using invertibility of `(R_0-z)^{-1}`, gives

\[
\Delta_2(z)=0
\iff
R_1-z\text{ is noninvertible},
\tag{12}
\]

which is exactly (6). No prime-gap input enters this step.

## 2. Compactness confines the zero set to ordinary discrete spectrum

Hilbert--Schmidt operators are compact, so (2) implies that `R_1` is a compact perturbation of `R_0`. Weyl stability gives (7). If `z in rho(R_0)`, then `z` is outside `sigma_ess(R_0)` and hence outside `sigma_ess(R_1)`. If (12) holds, self-adjointness of `R_1` therefore forces `z` to be an isolated eigenvalue of finite multiplicity.

This observation is important on the infinite flute. The continuous/essential spectral background is precisely where one might hope that a relative determinant could encode new scattering or resonance data. The bare analytic determinant (5) does not do that: its zeros on its natural domain `rho(R_0)` only register discrete spectral points of `R_1` that the reference resolvent does not already contain.

Under the spectral map `z=(1+lambda)^{-1}`, equation (8) follows for every nonzero zero. Thus the `det_2` zero set is just a reparameterization of an already-existing part of the Laplacian spectrum.

## 3. This closes a zeta-like route but not a Hilbert--Polya route

PF-147 correctly identified `det_2` as a canonical second-order perturbation object once the first relative resolvent lies in `S_2`. What PF-154 rules out is the stronger interpretation

```text
Hilbert--Schmidt relative resolvent
    -> modified Fredholm determinant det2
    -> new arithmetic zero divisor
    -> candidate Riemann-zero selector.
```

The middle arrow does not create new zeros. Any arithmetic significance of `Delta_2`'s zeros would have to come from the **actual discrete Laplace spectrum of the numerator surface**. In particular, if one wanted a Hilbert--Polya mechanism in which prime-flute eigenvalues themselves encode Riemann zeros, PF-154 says nothing against it; `det_2` would merely repackage those eigenvalues.

The all-composite control makes the boundary sharper. With the orientation used above, the zeros are discrete eigenvalues of the all-composite clone `P_1`, not a prime-specific set selected by regularization. Reversing the determinant gives the prime spectrum instead. The determinant construction itself therefore has no primality-selecting content.

## 4. Resonances and boundary values require genuinely additional structure

Equation (6) is a statement on the natural analytic domain `rho(R_0)`. It must not be promoted to a claim about resonances or a meromorphic continuation through continuous spectrum.

Gesztesy--Pushnitski--Simon [S18], already used in PF-147, emphasize that even for Hilbert--Schmidt self-adjoint pairs the modified determinant

\[
\det{}_2((A-z)(B-z)^{-1})
\tag{13}
\]

need not possess the nontangential boundary values required for an ordinary on-spectrum phase. Thus `S_2` membership alone gives neither a canonical scattering determinant nor a continued resonance divisor. PF-148 reaches ordinary Krein/Birman--Krein scattering by the **different** trace-class square-resolvent route, and PF-153 shows that higher even resolvent powers do not generate independent first-order phases.

A future resonance result would therefore need extra geometry or weighted-resolvent/meromorphic-continuation estimates beyond PF-147. If such a continuation existed, its poles and zeros could carry information not covered by PF-154; they would not be consequences of `det_2` regularization alone.

## 5. Prior-art / novelty audit

No novelty is claimed for the abstract determinant theory. For `K in S_2`, the definition (10), the Fredholm zero/invertibility criterion, compactness of Schatten perturbations, and Weyl stability of essential spectrum are classical. The Koplienko/modified-determinant framework and its boundary-value limitations are recorded in Gesztesy--Pushnitski--Simon [S18]. Directed searches around Hilbert--Schmidt perturbation determinants, regularized Fredholm determinants, Koplienko spectral shift, and product/zero formulas found the zero criterion as standard regularized-determinant theory rather than a new spectral theorem.

The project-specific content is the negative specialization to the exact prime-flute control hierarchy:

\[
\boxed{
R_1-R_0\in\mathcal S_2
\Longrightarrow
\Delta_2\text{ exists, but }
Z(\Delta_2)\cap\rho(R_0)
=\sigma_{\mathrm{disc}}(R_1)\cap\rho(R_0).
}
\tag{14}
\]

This is a durable boundary because PF-147 explicitly opened `det_2` as the natural object at the expected first-resolvent Schatten endpoint. PF-154 records that availability of the object must not be mistaken for a new zeta-like selector.

## 6. Stress tests and falsification core

A later adversary can check PF-154 through the following chain:

1. verify that the only operator hypothesis needed for the determinant statement is (2), while its application to the full prime/shift surfaces remains conditional through PF-147/PF-146;
2. check the exact factorization (9);
3. use the standard definition (10) and invertibility of `e^{-K}` to prove (11);
4. combine (9)--(11) to obtain (6);
5. use `S_2 subset K` and Weyl's theorem to obtain (7), then self-adjointness to identify every zero in `rho(R_0)` with discrete spectrum;
6. map nonzero `R_1` eigenvalues back to `P_1` by (8);
7. do **not** infer absence of a meromorphic continuation, equality of resonance sets, absence of prime-specific discrete eigenvalues, or failure of every possible Hilbert--Polya mechanism.

A refutation would require failure of one of these standard Fredholm facts for the displayed `S_2` perturbation or a mismatch between the common-Hilbert-space pair in PF-147 and the factorization above. Producing interesting prime-flute discrete eigenvalues would not refute PF-154; it would show that the information was already in the Laplacian spectrum rather than created by the modified determinant.

## Research consequence

The conditional operator route now separates cleanly into two genuinely different questions. The trace-class squared-resolvent gate can still yield a canonical relative scattering phase through PF-148, and the Hilbert--Schmidt first-resolvent endpoint can still yield a Koplienko/`det_2` object through PF-147. But **the zeros of that direct `det_2` are not a new spectral invariant layered on top of the Laplacian**: on its natural domain they are exactly relative discrete eigenvalues. Any surviving determinant-based RH mechanism must therefore come from substantive Laplace spectral structure or from an independently justified continuation/scattering construction, not from the regularization itself.