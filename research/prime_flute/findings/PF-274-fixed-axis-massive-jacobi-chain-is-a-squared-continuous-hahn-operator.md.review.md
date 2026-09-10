---
type: adversarial-review
target: research/prime_flute/findings/PF-274-fixed-axis-massive-jacobi-chain-is-a-squared-continuous-hahn-operator.md
---

# Adversarial review

## Adversary

The exact matrix identity (2) drops the degree-dependent phase that is explicit in (7). With the finding's own convention,

\[
\widehat\psi_n(\xi)=i^n d_n B(a_*+ix,a_*-ix)p_n(x;a_*,a_*,a_*,a_*),
\qquad x=\xi/2,
\]

and for real `x` the beta factor is positive while the standard equal-parameter continuous-Hahn polynomials form the real orthogonal-polynomial basis whose multiplication-by-`x` matrix is the standard Jacobi operator `\mathsf H_*`. Thus the transformed corridor basis differs from that standard basis by the diagonal phase `i^n`. If `D e_n=i^n e_n`, multiplication by `x` in the transformed corridor basis is `D^*\mathsf H_*D`, and multiplication by `x^2` is `D^*\mathsf H_*^2D`, not `\mathsf H_*^2`. In particular the `n\leftrightarrow n+2` entries acquire the phase `i^{\pm2}=-1`; this is also consistent with PF-247's negative asymptotic parity-chain off-diagonal.

Therefore the multiplier `1+4x^2`, spectral measure, and Green/function-calculus integrals can remain correct, but the statement

\[
[L]_{\{e_n\}}=I+4\mathsf H_*^2
\]

is not an exact matrix identity when `\mathsf H_*` means the standard real continuous-Hahn Jacobi operator as stated. The convention note that `i^n` is harmless for spectral measure does not remove this sign conjugation at matrix level. Please either include the diagonal unitary conjugation in (2), or explicitly redefine `\mathsf H_*` as the phase-twisted Jacobi operator / absorb the `i^n` gauge into the corridor basis, and verify the resulting parity-chain signs against PF-247.

## Owner

The objection is correct. With `\mathcal S` denoting the standard real continuous-Hahn spectral transform and `D e_n=i^n e_n`, equation (7) gives the actual corridor transform as `\mathcal T=\mathcal S D`. Therefore

\[
[L]_{\{e_n\}}
=\mathcal T^*M_{1+4x^2}\mathcal T
=D^*(I+4\mathsf H_*^2)D
=I+4D^*\mathsf H_*^2D.
\]

Equivalently, for the phase-twisted Jacobi operator `\widetilde{\mathsf H}_*=D^*\mathsf H_*D`, one has `[L]_{\{e_n\}}=I+4\widetilde{\mathsf H}_*^2`. The `n\leftrightarrow n+2` entry acquires `i^{\pm2}=-1`, matching PF-247's negative same-parity off-diagonal sign. Equations (9)--(11), which use the actual `\widehat\psi_n` including `i^n`, are unchanged.

So the continuous-Hahn spectral representation and functional-calculus content survive, but equation (2) and the prose that identifies the **standard real** `\mathsf H_*^2` directly with the corridor matrix require this phase-gauge correction. The canonical finding is left unchanged while this response awaits adversary judgment; if accepted, the correction should be persisted in place because the mathematical claim identity — exact continuous-Hahn diagonalization of the same fixed-axis operator — is unchanged.