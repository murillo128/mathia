# PC-072 — eventually outward scalar dilation covariance cannot have compact resolvent

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the natural non-bijective/coercive scalar-covariance escape left open by PC-071 on the compatible Prime-Circle solenoid.

## Claim

PC-064 identifies the compatible all-level Prime-Circle refinement with the arithmetic solenoid

\[
\Sigma_{\mathbb Q}\cong\widehat{\mathbb Q},
\qquad
L^2(\Sigma_{\mathbb Q})
=\overline{\operatorname{span}}\{\chi_q:q\in\mathbb Q\},
\]

and PC-069--PC-071 study the Haar-Koopman dilation unitary

\[
V_m\chi_q=\chi_{mq},\qquad m\ge2.
\]

PC-071 rules out every scalar homeomorphic law

\[
V_m^*HV_m=\Phi(H)
\]

for a self-adjoint compact-resolvent `H`, but explicitly leaves non-bijective scalar laws outside its theorem. The most natural repair is to use a non-bijective **coercive** law, for example a polynomial such as `\Phi(x)=x^2`, hoping that repeated dilation drives spectral energy rapidly outward.

That repair also fails.

Let `\Phi:\mathbb R\to\mathbb R` be a finite-valued real Borel function satisfying the eventual outward condition

\[
\boxed{
\exists R<\infty:\quad |x|>R\Longrightarrow |\Phi(x)|>|x|.
}
\]

Then there is no self-adjoint compact-resolvent operator `H` on either

\[
L^2_0(\Sigma_{\mathbb Q})=\mathbf1^\perp
\]

or the full `L^2(\Sigma_{\mathbb Q})` satisfying, as an equality of self-adjoint operators,

\[
\boxed{V_m^*HV_m=\Phi(H).}
\]

In particular, **every real polynomial `P` of degree at least two is excluded**, because its leading term gives `|P(x)|>|x|` outside a compact interval.

The mechanism is different from PC-071. Injectivity of `\Phi` is not assumed, so one cannot transport an eigenvector uniquely backward. Instead unitary equivalence forces every eigenvalue to have at least one spectral preimage. Eventual outward growth makes every infinite backward chain bounded. Compact resolvent then forces that chain to repeat, hence every eigenvalue is periodic under `\Phi`. Periodic eigenspaces form finite-dimensional `V_m`-invariant subspaces, which the Prime-Circle solenoid dilation has only in the constant mode. The infinite-dimensional representation therefore cannot be spanned.

Thus making the scalar law more nonlinear and more coercive does not rescue an ordinary Hilbert--Pólya operator while retaining the intrinsic two-sided solenoid dilation. A surviving non-bijective scalar law must fail this outward-tail condition in an essential way, or the construction must leave scalar functional calculus altogether.

## 1. Forward spectral transport does not require injectivity

Assume

\[
V_m^*HV_m=\Phi(H).
\]

Multiplying on the left by `V_m` gives

\[
HV_m=V_m\Phi(H).
\]

If `H\psi=\lambda\psi`, then Borel functional calculus gives

\[
\Phi(H)\psi=\Phi(\lambda)\psi,
\]

and therefore

\[
\boxed{
H(V_m\psi)=\Phi(\lambda)V_m\psi.
}
\]

Hence every eigenvalue is sent to another eigenvalue:

\[
\boxed{
\lambda\in\operatorname{Spec}_p(H)
\Longrightarrow
\Phi(\lambda)\in\operatorname{Spec}_p(H).
}
\]

For non-injective `\Phi`, however, `V_m^{-1}` need not send an `H`-eigenvector to a single eigenspace. It may land in the direct sum of several eigenspaces having the same `\Phi`-value. This is precisely why PC-071's homeomorphism argument cannot simply be reused.

The correct replacement is to work with existence of spectral preimages rather than a unique backward orbit.

## 2. Unitary equivalence forces a spectral predecessor for every eigenvalue

Because `V_m^*HV_m` is unitarily equivalent to `H`, the operators `H` and `\Phi(H)` have the same point spectrum with the same finite multiplicities.

Let `\lambda` be an eigenvalue of `H`. Then `\lambda` is also an eigenvalue of `\Phi(H)`. Since `H` has compact resolvent, it has a complete orthogonal eigenbasis and `\Phi(H)` acts on the `H`-eigenspace `E_\mu(H)` by the scalar `\Phi(\mu)`. Thus

\[
E_\lambda(\Phi(H))
=
\bigoplus_{\substack{\mu\in\operatorname{Spec}_p(H)\\\Phi(\mu)=\lambda}}
E_\mu(H).
\]

The left side is nonzero, so at least one term on the right exists. Therefore

\[
\boxed{
\forall\lambda\in\operatorname{Spec}_p(H),\quad
\exists\mu\in\operatorname{Spec}_p(H):\ \Phi(\mu)=\lambda.
}
\]

Starting from any eigenvalue `\lambda_0`, choose recursively

\[
\Phi(\lambda_{-j})=\lambda_{-(j-1)},
\qquad j\ge1.
\]

This gives an infinite backward spectral chain even when `\Phi` folds many eigenvalues together.

There is also an exact multiplicity identity,

\[
\dim E_\lambda(H)
=
\sum_{\substack{\mu\in\operatorname{Spec}_p(H)\\\Phi(\mu)=\lambda}}
\dim E_\mu(H),
\]

although the contradiction below needs only existence of one predecessor.

## 3. Eventual outward growth traps every backward spectral chain

Fix `\lambda_0` and a backward chain as above. Let

\[
M=\max\{R,|\lambda_0|\}.
\]

Suppose for contradiction that some `\lambda_{-j}` satisfies

\[
|\lambda_{-j}|>M.
\]

Then `|\lambda_{-j}|>R`, so the outward condition gives

\[
|\lambda_{-(j-1)}|
=|\Phi(\lambda_{-j})|
>|\lambda_{-j}|.
\]

The new value is still outside `[-R,R]`, so the inequality can be iterated forward along the chosen chain. After `j` steps,

\[
|\lambda_0|>|\lambda_{-j}|>M\ge|\lambda_0|,
\]

which is impossible.

Hence every backward chain obeys the exact bound

\[
\boxed{
|\lambda_{-j}|\le \max\{R,|\lambda_0|\}
\qquad(j\ge0).
}
\]

This is the key obstruction. A superlinear or otherwise outward scalar law may look coercive in forward time, but two-sided unitary covariance forces spectral predecessors in the opposite direction, and those predecessors are trapped in one compact interval.

## 4. Compact resolvent turns bounded backward chains into periodic cycles

A self-adjoint compact-resolvent operator has only finitely many eigenvalues in every bounded real interval. The backward chain from Section 3 is infinite but remains in `[-M,M]`. Therefore it cannot consist of infinitely many distinct values.

There exist `a>b\ge0` such that

\[
\lambda_{-a}=\lambda_{-b}.
\]

Set `r=a-b>0`. Applying `\Phi^r` to `\lambda_{-a}` returns the same value, so `\lambda_{-a}` is periodic. Since `\lambda_0` is a forward iterate of `\lambda_{-a}`, it lies on the same finite cycle. Thus the starting eigenvalue was itself periodic:

\[
\boxed{
\forall\lambda\in\operatorname{Spec}_p(H),\quad
\exists r\ge1:\ \Phi^r(\lambda)=\lambda.
}
\]

So eventual outward covariance plus compact resolvent does not merely constrain the spectrum. It forces **every** eigenvalue into a finite `\Phi`-cycle.

## 5. Every spectral cycle gives a forbidden finite-dimensional dilation-invariant subspace

Let

\[
\lambda_0\mapsto\lambda_1\mapsto\cdots
\mapsto\lambda_{r-1}\mapsto\lambda_0
\]

be a cycle of distinct eigenvalues. Section 1 gives

\[
V_m E_{\lambda_j}(H)
\subseteq E_{\lambda_{j+1}}(H)
\]

with indices modulo `r`. Since `V_m` is unitary,

\[
\dim E_{\lambda_j}(H)
\le
\dim E_{\lambda_{j+1}}(H).
\]

Going once around the cycle forces equality at every step. Hence all inclusions are onto:

\[
\boxed{
V_m E_{\lambda_j}(H)
=E_{\lambda_{j+1}}(H).
}
\]

The finite-dimensional space

\[
\mathcal K_\lambda
=
\bigoplus_{j=0}^{r-1}E_{\lambda_j}(H)
\]

is therefore `V_m`-invariant.

PC-069 proves the representation-theoretic fact specific to the compatible Prime-Circle solenoid:

\[
\boxed{
\text{every finite-dimensional }V_m\text{-invariant subspace is contained in }
\mathbb C\mathbf1.
}
\]

On `L^2_0(\Sigma_{\mathbb Q})` there is no nonzero such subspace at all, so even one eigenvalue is impossible. On the full `L^2`, every spectral cycle would have to lie in the one-dimensional constant sector. But the eigenspaces of a compact-resolvent self-adjoint operator form a complete basis of the whole infinite-dimensional Hilbert space. They cannot all lie in `\mathbb C\mathbf1`.

Therefore no such `H` exists.

## 6. Polynomial and superlinear scalar repairs are all covered

Let

\[
P(x)=a_dx^d+\cdots+a_0,
\qquad a_d\ne0,
\qquad d\ge2.
\]

Then

\[
\frac{|P(x)|}{|x|}
\sim |a_d|\,|x|^{d-1}
\longrightarrow\infty
\qquad(|x|\to\infty).
\]

Hence there is `R` such that

\[
|P(x)|>|x|
\qquad(|x|>R).
\]

PC-072 therefore yields the clean corollary

\[
\boxed{
V_m^*HV_m=P(H),\quad \deg P\ge2
\Longrightarrow
H\text{ cannot have compact resolvent}.}
\]

This includes the most obvious non-bijective choices `P(x)=x^2`, `x^2+c`, higher even powers, and all odd/even real polynomials of degree at least two, regardless of the number of real branches or critical points.

The theorem is broader than polynomial dynamics: any real Borel law whose tails strictly increase absolute value is excluded. Continuity, monotonicity and injectivity are not used.

## 7. Why this is not already PC-071 and why the boundary is real

PC-071 handles real homeomorphisms. Its proof can move eigenspaces bijectively along `\Phi`-orbits and classify increasing/decreasing homeomorphic dynamics. None of that works for a folding map such as `x^2`, because `V_m^{-1}` may mix several preimage eigenspaces.

PC-072 supplies a different invariant: **existence of backward spectral predecessors plus compactness**. It therefore closes a genuinely new class that PC-071 explicitly left open.

The outward hypothesis is also substantive rather than cosmetic. The bilateral-shift number-operator model used as a control in PC-069/PC-070 has

\[
S^*NS=N+I
\]

on `\ell^2(\mathbb Z)`. The law `\Phi(x)=x+1` fails the outward condition on the negative tail, where

\[
|x+1|<|x|
\qquad(x\ll0).
\]

Its backward orbit escapes to `-\infty` instead of being trapped, so the present proof correctly does not exclude that compact-resolvent bilateral model. PC-070 needs additional Prime-Circle orbit-multiplicity structure to rule out additive covariance on the full solenoid.

Thus PC-072 should not be generalized to arbitrary non-bijective or arbitrary Borel scalar laws without a separate argument.

## 8. Prior-art and novelty audit

No historical novelty is claimed for the abstract ingredients.

- Borel functional calculus and unitary equivalence of self-adjoint operators are standard spectral theory; the same background already underlies PC-069--PC-071.
- A self-adjoint compact-resolvent operator has pure discrete spectrum, finite-dimensional eigenspaces and finitely many eigenvalues in every bounded interval; again this is standard functional analysis.
- The fact that a polynomial of degree at least two expands absolute value outside a sufficiently large compact interval is elementary polynomial dynamics.
- PC-069 already supplies the project-specific representation fact that the solenoid dilation `V_m` has no finite-dimensional invariant subspace outside the constant mode.

Targeted literature searches for exact relations of the form `U^*HU=\Phi(H)` or `U^*HU=P(H)` with compact resolvent found standard literature on spectral/functional calculus and unitary equivalence, but did not locate this exact universal-arithmetic-solenoid obstruction. That absence is not a novelty proof.

The durable contribution is therefore the **Prime-Circle frontier closure** obtained by combining standard functional calculus with the already-derived two-sided dilation representation:

\[
\boxed{
\text{compatible solenoid dilation}
+\text{ eventually outward scalar covariance}
+\text{ ordinary compact resolvent}
\quad\text{are incompatible}.}
\]

This is a negative research result, not a claim that the underlying functional-analytic lemmas are new.

## 9. Boundary of the obstruction

PC-072 rules out non-bijective scalar laws only when their tails are eventually outward in absolute value. It does **not** rule out:

- a non-bijective scalar law with a translation-like or otherwise non-outward tail, whose backward spectral chains can escape every compact set;
- a spectrum-specific discontinuous law whose tail behavior is not coercive, although such a proposal remains subject to the arbitrary-spectral-wrapper control in the Prime-Circle mandate;
- an operator-valued or matrix covariance in which `V_m^*HV_m` is not a scalar function of `H`;
- a one-sided semigroup/isometry representation instead of the two-sided solenoid automorphism;
- a semifinite spectral triple or another framework not requiring ordinary compact resolvent;
- symmetry breaking by the common anchor, primitive/old decomposition, embedded chord data or cross-level geometry before passage to the abstract solenoid;
- nonlinear determinant/transfer data that are not functional calculus of one self-adjoint operator;
- or the global primitive-root uniformization/accessory branch of PC-017.

The narrowed scalar frontier is now sharp: after PC-071 and PC-072, a surviving regular-looking scalar law cannot merely be a homeomorphic reparametrization **or** a coercive folding/superlinear repair. It would need a genuinely different tail geometry, and Prime Circle would still have to derive that law before spectralization rather than choose it to manufacture desired zeta behavior.

## 10. Exact audit tests

The finding has direct falsifiers.

1. From `V_m^*HV_m=\Phi(H)`, verify that `H(V_m\psi)=\Phi(\lambda)V_m\psi` whenever `H\psi=\lambda\psi`.
2. Use compact-resolvent diagonalization of `H` to verify
   \[
   E_\lambda(\Phi(H))
   =\bigoplus_{\Phi(\mu)=\lambda}E_\mu(H).
   \]
3. Use unitary equivalence of `H` and `\Phi(H)` to prove that every `H`-eigenvalue has at least one spectral predecessor.
4. Starting from any predecessor chain, verify that `|\Phi(x)|>|x|` outside `[-R,R]` forces the bound `|\lambda_{-j}|\le\max(R,|\lambda_0|)`.
5. Use compact resolvent to show that the bounded infinite chain repeats, and check that repetition implies the original eigenvalue is periodic under `\Phi`.
6. For a finite spectral cycle, verify the cyclic dimension inequalities and conclude that the direct sum of its eigenspaces is finite-dimensional and `V_m`-invariant.
7. Apply the PC-069 invariant-subspace theorem to obtain the contradiction on both mean-zero and full `L^2`.
8. For any real polynomial of degree at least two, verify eventual outward growth explicitly.
9. Test the boundary law `\Phi(x)=x+1` on the bilateral number-operator model and confirm that it fails the outward hypothesis exactly on one tail.

Failure of any of items 1--8 would invalidate the obstruction. Item 9 prevents the theorem from being silently overextended to scalar laws whose backward spectral dynamics can escape to infinity.

## Consequence for the Prime-Circle program

PC-071 left non-bijective scalar covariance as the most immediate scalar escape from the homeomorphism no-go. The obvious way to exploit that freedom was to choose a folding or superlinear law whose forward dynamics becomes more coercive than an affine dilation.

PC-072 closes that entire natural class:

\[
\boxed{
V_m^*HV_m=\Phi(H),
\qquad
|\Phi(x)|>|x|\text{ for }|x|\gg1
\quad\Longrightarrow\quad
H\text{ cannot be an ordinary compact-resolvent Prime-Circle Hamiltonian}.}
\]

The reason is structurally useful: **forward coercivity becomes backward spectral trapping under a two-sided unitary refinement symmetry**. The remaining search should therefore prioritize mechanisms that leave one-variable scalar covariance altogether, or that derive a genuinely asymmetric/non-outward law from embedded Prime-Circle geometry before the solenoid quotient.