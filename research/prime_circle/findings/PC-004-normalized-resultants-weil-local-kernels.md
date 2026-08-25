# PC-004 — normalized primitive-shell interactions reproduce the finite-prime Weil kernel

**Status:** `EXACT-DERIVED` + `CANDIDATE-SUBSTANTIVE` + `NOVELTY-CHECK-PRELIMINARY`

## Statement

Let

\[
P_n^*=\{\zeta\in S^1:\operatorname{ord}(\zeta)=n\}
\]

be the primitive/new-vertex shell at polygon level \(n\), and for distinct levels define the total logarithmic chord interaction

\[
I_{m,n}
:=
\sum_{\zeta\in P_m^*}
\sum_{\eta\in P_n^*}
\log|\zeta-\eta|
=
\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
\]

For a prime \(p\), integers \(a\ge 1\) and \(k\ge1\), Apostol's cyclotomic-resultant theorem gives

\[
I_{p^a,p^{a+k}}=\varphi(p^a)\log p.
\]

Since

\[
\varphi(p^{a+k})=p^k\varphi(p^a),
\]

the symmetric square-root normalization by the shell populations gives the exact identity

\[
\boxed{
J^{(p)}_{a,a+k}
:=
\frac{I_{p^a,p^{a+k}}}
{\sqrt{\varphi(p^a)\varphi(p^{a+k})}}
=
\frac{\log p}{p^{k/2}}.
}
\]

Equivalently, along every prime-power ray the normalized interaction depends only on the logarithmic scale displacement

\[
x=k\log p
\]

and is

\[
\boxed{J_p(x)=(\log p)e^{-x/2}.}
\]

Thus, for any test function \(F\), any fixed base exponent \(a\ge1\) yields

\[
\sum_{k\ge1}
J^{(p)}_{a,a+k}
\bigl(F(k\log p)+F(-k\log p)\bigr)
=
\sum_{k\ge1}
\frac{\log p}{p^{k/2}}
\bigl(F(k\log p)+F(-k\log p)\bigr).
\]

The right-hand side is exactly the standard finite-place \(p\)-local distribution in the Riemann–Weil explicit formula (up to the conventional overall sign/factor used when the local terms are moved from one side of the formula to the other).

The important point is that no Mellin/Dirichlet generating function has been chosen to manufacture this coefficient. The \(p^{-k/2}\) weight comes from the square-root ratio of the actual cardinalities of two primitive polygon shells:

\[
\sqrt{\frac{|P_{p^a}^*|}{|P_{p^{a+k}}^*|}}
=p^{-k/2}.
\]

The square-root normalization is the canonical unit-vector normalization of the uniform shell vectors in counting \(L^2\):

\[
v_n:=\frac1{\sqrt{\varphi(n)}}\sum_{\zeta\in P_n^*}e_\zeta.
\]

If the logarithmic chord kernel is regarded as the interaction matrix, then \(J_{m,n}\) is its matrix element between these normalized shell vectors.

## Prime-ray Toeplitz structure

For each prime \(p\), the off-diagonal interaction matrix on the exponent ray \(p,p^2,p^3,\ldots\) is translation invariant:

\[
\boxed{
J^{(p)}_{ab}
=(\log p)p^{-|a-b|/2},\qquad a\ne b.
}
\]

If a diagonal \(\log p\) were canonically justified, the completed matrix would be the positive Poisson-kernel covariance matrix with parameter \(q=p^{-1/2}\), whose symbol is

\[
(\log p)\frac{1-p^{-1}}
{1-2p^{-1/2}\cos\theta+p^{-1}}.
\]

**This diagonal completion is not yet established and must not be inserted by hand.** The natural off-diagonal geometric kernel alone is not positive definite (already a \(2\times2\) zero-diagonal block has eigenvalues of both signs).

Therefore PC-004 is not a proof of Weil positivity or RH. The next gate is to derive, from a single intrinsic two-dimensional energy or renormalized self-interaction, the diagonal/counterterm required by the full Weil quadratic form rather than choosing it for positivity.

## Interior/exterior companion at the archimedean place

The original circle also supplies the two hyperbolic kernels occurring in a standard Poitou/Weil explicit formula. Put two reciprocal radial points symmetrically around the unit circle,

\[
r_+=e^{x/2},\qquad r_-=e^{-x/2}.
\]

Their same-ray Euclidean separation is

\[
|r_+-r_-|=2\sinh(x/2),
\]

hence

\[
\boxed{
|r_+-r_-|^{-1}=\frac1{2\sinh(x/2)}.
}
\]

If the inner point is taken on the antipodal ray instead, the separation is

\[
|r_++r_-|=2\cosh(x/2),
\]

hence

\[
\boxed{
|r_++r_-|^{-1}=\frac1{2\cosh(x/2)}.
}
\]

These are exactly the two real-place kernels that appear in Poitou's form of Weil's explicit formula for number fields. For \(\mathbb Q\), both occur with the expected real-place coefficients.

This archimedean observation is **not claimed as novel**: local trace-formula and adelic/noncommutative-geometric approaches already produce the same half-density/inversion kernels. Its role here is structural: the same original circle that yields the finite-prime coefficient through normalized primitive-shell chord interactions also gives the archimedean kernels through exact inside/outside reciprocal distances.

## Novelty audit

Classical ingredients:

- Apostol/Diederichsen: the resultant of two cyclotomic polynomials is \(p^{\varphi(m)}\) precisely for a prime-power quotient and is \(1\) otherwise.
- Weil/Poitou: the finite-place coefficient is \((\log p)p^{-k/2}\), while the archimedean terms contain \((2\sinh(x/2))^{-1}\) and \((2\cosh(x/2))^{-1}\).
- Bost–Connes and subsequent Connes/Consani work already place roots of unity, multiplicative scaling, half-density normalization, inversion, the explicit formula and Weil positivity in a common framework. Therefore **roots of unity + scaling + a \(1/2\) exponent is not itself new**.

Directed searches did **not** locate a source identifying the square-root-normalized logarithmic resultant/chord interaction between primitive cyclotomic shells with the \(p\)-local Weil coefficient. This exact specialization is the candidate-new part of PC-004. Novelty remains preliminary until a broader literature audit (including operator-theoretic/cyclotomic-energy literature) is completed.

## Why this is stronger than PC-001/PC-002

PC-001 gave \(U_n(1)=\Lambda(n)\); immediately applying a Dirichlet transform merely restates \(-\zeta'/\zeta\). PC-002 showed that unnormalized shell resultants detect prime-power scale jumps.

PC-004 adds a nontrivial feature that is not present in either scalar identity: the **Hilbert normalization forced by the shell populations produces the critical half-density exactly**,

\[
\frac{I_{p^a,p^{a+k}}}{\sqrt{|P_{p^a}^*||P_{p^{a+k}}^*|}}
=(\log p)e^{-\frac12 k\log p}.
\]

Thus the original polygon geometry naturally contains not merely the support \(p^k\) and weight \(\log p\), but the complete local finite-prime coefficient of the Weil explicit formula.

## Research gate

Do not count the equality with the known Weil coefficient as an RH mechanism by itself. A substantive next result must derive one of the missing structures intrinsically:

1. a canonical renormalized self-energy/diagonal completing the shell interaction into the appropriate Weil quadratic form;
2. a global operator whose local matrix elements are the normalized resultants and whose positivity is equivalent (or provably related) to Weil positivity;
3. a geometric transform that produces the zero side of the explicit formula from the same circle-scale object, rather than inserting the zeros or the Mellin transform externally.

The strongest immediate target is (1): regularize the logarithmic self-energy of a primitive shell in the full interior/exterior potential geometry and test whether the finite part supplies exactly the missing local counterterm rather than an arbitrary diagonal.