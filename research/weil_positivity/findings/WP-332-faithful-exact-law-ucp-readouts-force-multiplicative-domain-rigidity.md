---
id: WP-332
title: Faithful exact-law UCP readouts force the source observable into the multiplicative domain
branch: weil_positivity
status: supported
kind: ucp-readout-multiplicative-domain-obstruction
claim_strength: exact C*-algebraic obstruction extending WP-331 from conditional expectations to arbitrary unital completely positive readouts; exact scalar-law preservation under a faithful output state forces zero Kadison defect, multiplicative-domain rigidity, and vanishing Stinespring off-diagonal coupling for the source observable
created: 2026-09-16
related: [WP-329, WP-330, WP-331]
prior_art:
  - Richard V. Kadison, A Generalized Schwarz Inequality and Algebraic Invariants for Operator Algebras, Annals of Mathematics 56 (1952), 494-503, DOI 10.2307/1969657
  - W. Forrest Stinespring, Positive Functions on C*-Algebras, Proceedings of the American Mathematical Society 6 (1955), 211-216, DOI 10.1090/S0002-9939-1955-0069403-4
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
---

# WP-332 — Faithful exact-law UCP readouts force the source observable into the multiplicative domain

## Claim

`WP-331` showed that a conditional-expectation enrichment cannot simultaneously preserve the exact scalar source law and expose a new centered positive variance to the same faithful scalar state: the conditional variance must vanish. That finding left a natural escape in which the source is recovered by a more general positive compression/readout rather than by a conditional expectation.

For the canonical unital completely positive version of that escape, the same obstruction becomes stronger and more geometric.

Let `A` and `B` be unital `C*`-algebras, let

\[
\Phi:A\to B
\tag{1}
\]

be unital completely positive, let `tau` be a faithful state on `B`, and put

\[
\phi=\tau\circ\Phi.
\tag{2}
\]

For a self-adjoint `X in A`, write

\[
b=\Phi(X)\in B_{\rm sa}.
\tag{3}
\]

If the scalar law of `X` under `phi` is the same as the scalar law of `b` under `tau`, then already equality of the second moments forces

\[
\Phi(X^2)=\Phi(X)^2=b^2.
\tag{4}
\]

Consequently `X` lies in the multiplicative domain of `Phi`. Hence, for every `Z in A`,

\[
\Phi(XZ)=b\Phi(Z),
\qquad
\Phi(ZX)=\Phi(Z)b,
\tag{5}
\]

and therefore

\[
\Phi(f(X))=f(b)
\tag{6}
\]

for every continuous `f` on the spectrum of `X`.

Equivalently, in any Stinespring representation

\[
\Phi(a)=V^*\pi(a)V,
\qquad V^*V=I,
\tag{7}
\]

the source observable has no off-diagonal coupling between the compressed space and its dilation complement:

\[
(I-VV^*)\pi(X)V=0.
\tag{8}
\]

Because `pi(X)` is self-adjoint, `Ran(V)` is a reducing subspace for `pi(X)`.

Thus

\[
\boxed{
\text{exact scalar source law}
+\text{ faithful UCP readout}
+\text{ source coordinate }b=\Phi(X)
\Longrightarrow
\text{multiplicative-domain rigidity and zero source-observable boundary coupling}.
}
\tag{9}
\]

At every finite Mangoldt cutoff the canonical source state is faithful, so replacing the conditional expectation in `WP-331` by an arbitrary UCP compression does not create a hidden finite--archimedean coupling while preserving the same source law in the same observable. A surviving compression/boundary route must change the observable or response before this exact-law readout, change the scalar law, use a nonfaithful/null sector, or leave the UCP-compression architecture.

**Classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE + UCP-READOUT + KADISON-SCHWARZ + MULTIPLICATIVE-DOMAIN + STINESPRING-COMPRESSION + FAITHFUL-STATE + MATCHED-CONTROL + NOT-WEIL-POSITIVITY`.

## Evidence class

The operator-algebra theorem used here is classical. Kadison--Schwarz positivity, Stinespring dilation, and Choi's multiplicative-domain equality criterion are not claimed as new. The Mathia-specific result is their application to the precise escape left by `WP-331`: a general UCP readout cannot preserve the exact finite arithmetic law of the same compressed mean while using off-diagonal dilation coupling of that observable to carry new source-visible geometry.

No zeta zeros, RH assumption, analytic continuation, prime-number asymptotic, numerical fit, or regularization enters. The arithmetic specialization uses only the finite Mangoldt source already fixed in `WP-329`--`WP-331`.

## 1. The Kadison defect is positive

Since `Phi` is unital and completely positive, the Kadison--Schwarz inequality gives

\[
\Phi(X)^2\le \Phi(X^2)
\tag{10}
\]

for self-adjoint `X`. Define the positive defect

\[
D_\Phi(X)
:=
\Phi(X^2)-\Phi(X)^2
\ge0.
\tag{11}
\]

If `X` under `phi=tau circ Phi` and `b=Phi(X)` under `tau` have the same scalar law, then their second moments agree:

\[
\tau(\Phi(X^2))
=
\phi(X^2)
=
\tau(b^2)
=
\tau(\Phi(X)^2).
\tag{12}
\]

Therefore

\[
\tau(D_\Phi(X))=0.
\tag{13}
\]

Faithfulness of `tau` on the positive cone of `B` forces

\[
D_\Phi(X)=0,
\tag{14}
\]

which proves (4).

Only the second-moment part of exact law preservation is needed. Higher scalar moments play no role in forcing the rigidity.

## 2. Equality forces multiplicative-domain rigidity

For a unital completely positive map, Choi's multiplicative-domain theorem says that an element `a` satisfying

\[
\Phi(a^*a)=\Phi(a)^*\Phi(a),
\qquad
\Phi(aa^*)=\Phi(a)\Phi(a)^*
\tag{15}
\]

belongs to the multiplicative domain of `Phi`. Since `X=X^*`, equation (14) supplies both equalities in (15) at once. Hence

\[
X\in\operatorname{MD}(\Phi).
\tag{16}
\]

The defining consequence is exactly (5). Because the multiplicative domain is a `C*`-subalgebra, it contains `C^*(X,1)`, and the restriction

\[
\Phi|_{C^*(X,1)}
\tag{17}
\]

is a unital `*`-homomorphism. Continuous functional calculus then gives (6).

This is stronger than matching scalar moments. Every `Phi`-visible mixed product containing the source observable factors through the deterministic image `b`. The readout has no hidden covariance of `X` left to use as a new arithmetic coupling.

## 3. Stinespring geometry makes the missing coupling explicit

Take a Stinespring dilation (7) and put

\[
P=VV^*.
\tag{18}
\]

Using `V^*V=I`, the Kadison defect has the exact factorization

\[
\begin{aligned}
D_\Phi(X)
&=V^*\pi(X)^2V
 -V^*\pi(X)V\,V^*\pi(X)V\\
&=V^*\pi(X)(I-P)\pi(X)V\\
&=\bigl((I-P)\pi(X)V\bigr)^*
   \bigl((I-P)\pi(X)V\bigr).
\end{aligned}
\tag{19}
\]

Thus (14) is equivalent to

\[
(I-P)\pi(X)V=0.
\tag{20}
\]

So `pi(X)` maps `Ran(V)` into itself. Since `pi(X)` is self-adjoint, invariance implies that `Ran(V)` is reducing, and therefore

\[
(I-P)\pi(X)P=0,
\qquad
P\pi(X)(I-P)=0.
\tag{21}
\]

Equation (21) is the geometric content of the finding. If a UCP compression is supposed to recover the exact source law from the compressed mean of the same self-adjoint observable, faithfulness kills precisely the off-diagonal block that could have coupled that source observable to a new dilation/boundary sector.

The dilation may still contain a large orthogonal complement and other operators may couple to it. What disappears is specifically the coupling carried by `X` under the readout being used to preserve its source law. The result is therefore a structural restriction, not a claim that the whole ambient algebra is trivial.

## 4. Exact finite-cutoff Mangoldt application

Use the finite support from `WP-329`--`WP-331`:

\[
\Sigma_R
=
\{\log n:n=p^k,\ \log n\le R\},
\tag{22}
\]

and let `nu_{s,R}` be the normalized positive Mangoldt weight on `Sigma_R`. Put

\[
B_R=C(\Sigma_R),
\qquad
b_R(x)=x,
\qquad
\tau_{s,R}(f)=\int_{\Sigma_R}f(x)\,d\nu_{s,R}(x).
\tag{23}
\]

Every point of `Sigma_R` has strictly positive `nu_{s,R}` mass. Hence `tau_{s,R}` is faithful on the finite-dimensional commutative `C*`-algebra `B_R`.

Now allow **any** unital completely positive readout

\[
\Phi_R:A_R\to B_R
\tag{24}
\]

and any self-adjoint `X_R in A_R` satisfying

\[
\Phi_R(X_R)=b_R.
\tag{25}
\]

If the scalar law of `X_R` under `tau_{s,R} circ Phi_R` is required to remain exactly `nu_{s,R}`, then the theorem gives

\[
X_R\in\operatorname{MD}(\Phi_R)
\tag{26}
\]

and every Stinespring dilation of `Phi_R` satisfies

\[
(I-P_R)\pi_R(X_R)P_R=0.
\tag{27}
\]

So the conditional-expectation hypothesis in `WP-331` was not the load-bearing source of rigidity. The obstruction survives arbitrary UCP compressions: exact faithful law preservation itself forces the source observable into the noiseless/multiplicative sector of the readout.

This closes a genuine portion of `WP-331`'s suggested “compression” escape. Simply replacing `E` by a more general positive compression cannot make the same exact Mangoldt observable interact with an auxiliary archimedean sector while keeping its scalar law unchanged.

## 5. Matched controls show that the rigidity is not arithmetic

Replace `nu_{s,R}` by any probability measure `mu` on the same finite support with strictly positive mass at every point. The state

\[
\tau_\mu(f)=\int f\,d\mu
\tag{28}
\]

is still faithful. For any UCP `Phi_R` and any self-adjoint `X_R` with `Phi_R(X_R)=b_R`, exact preservation of the scalar law of `b_R` under `tau_mu` again implies

\[
X_R\in\operatorname{MD}(\Phi_R).
\tag{29}
\]

The theorem therefore does not recognize Mangoldt weighting, prime-power support, the critical half-density, or a Gamma factor. It is a matched-control obstruction to a proposed architecture, not an arithmetic positivity mechanism.

This distinction matters for the `weil_positivity` mandate. A positive UCP/compression theorem that reaches (29) for the Mangoldt source but also for arbitrary positive control weights cannot by itself explain the global Weil sign. Arithmetic selectivity must enter in a structure not erased by the multiplicative-domain collapse.

## 6. Adversarial boundary and exact escape routes

The obstruction has deliberately narrow hypotheses.

**Nonfaithful output state.** If `tau` is not faithful, the positive Kadison defect may be nonzero while lying in a `tau`-null positive sector. This is the UCP analogue of the null-ideal loophole already exhibited explicitly in `WP-330`; it is not a new selective mechanism by itself.

**Changed scalar law.** If the enriched observable is allowed to change its scalar second moment, then `tau(D_Phi(X))` may be positive and off-diagonal Stinespring coupling can survive. A viable construction must then derive the desired finite and archimedean Weil terms from the changed response rather than claim exact preservation of the old source law.

**Different source observable.** The theorem assumes that the arithmetic coordinate is the compressed mean `b=Phi(X)` of the same self-adjoint observable whose law is preserved. A source recovered from a derivative, resolvent, transfer function, boundary Weyl function, nonlinear response, joint observable, or another operator is outside the claim unless that new observable itself satisfies the hypotheses.

**Non-UCP or signed response.** Indefinite pairings, supertraces, signed boundary forms, and nonlinear Schur/Feshbach responses are not UCP readouts and are not ruled out here. Their sign must be established separately; leaving the UCP category does not automatically supply Weil positivity.

**Couplings through other operators.** Equation (21) kills the off-diagonal Stinespring block of `X`, not every possible interaction in `A`. A multivariable construction may still couple another operator to the dilation complement. To matter, that coupling must be source-forced, survive matched controls, and generate the finite plus archimedean/global Weil structure before positivity is read off.

These boundaries prevent a false global no-go. In particular, the finding does not rule out Connes-style compressed scaling constructions, source-derived boundary triples, or a genuinely joint finite--archimedean form whose arithmetic source is not the unchanged scalar law of one compressed mean.

## 7. Prior-art and novelty audit

Kadison's generalized Schwarz inequality, Stinespring dilation, and Choi's multiplicative-domain criterion are classical operator-algebra results. The factorization (19) is the standard compression form of the Kadison defect. No theorem-level novelty is claimed for those facts.

The durable delta is the exact Mathia application. `WP-331` proved collapse for conditional expectations by decomposing `X=E(X)+Y`. The present result removes idempotence, bimodularity, and the inclusion of the base algebra from the hypothesis: an arbitrary UCP readout with a faithful output state is already rigid once it preserves the scalar law of its own compressed self-adjoint mean. In Stinespring language, the prospective hidden boundary coupling is exactly the positive Schwarz defect and must vanish.

A bounded literature audit found this operator-algebra mechanism to be standard and found no basis for presenting (9) as a new general theorem. Its research value is instead falsificatory: it closes the most direct UCP-compression repair of the live operator-valued route after `WP-331` while exposing the precise assumptions a genuinely different boundary response must break.

This mechanism is distinct from classical Weil positivity, Hilbert--Polya, Frobenius/cohomological positivity, Connes trace formulas, and intersection-form programs. It obtains no zero form and proves no RH-equivalent positivity statement; it only shows why one proposed way of hiding new positive geometry behind an exact arithmetic readout is impossible.

## 8. Consequence for the surviving Weil-positivity frontier

The operator-valued sequence `WP-329`--`WP-332` now separates four increasingly strong but still insufficient architectures:

1. deterministic amalgamated divisibility can store all arithmetic in the scalar state (`WP-329`);
2. nonzero operator-valued noise is still vacuous if scalarization kills its ideal (`WP-330`);
3. making the scalar state faithful while preserving the exact law collapses conditional-expectation noise (`WP-331`);
4. replacing that conditional expectation by an arbitrary UCP compression still collapses the source observable into the multiplicative domain (this finding).

The next nontrivial escape therefore cannot be merely “use a more general positive compression.” It must change what is being read out or how the finite and archimedean pieces interact before scalarization. A serious candidate should supply a source-derived multivariable or energy-dependent boundary response, a joint finite--archimedean operator whose arithmetic is not confined to one preserved scalar law, or another non-UCP geometric pairing with its own independent sign theorem.

That surviving problem is still exactly the README mandate: derive the completed Weil orientation from intrinsic geometry rather than insert it into the readout. `WP-332` does not solve that problem, but it removes a broad natural class of faithful exact-law compression repairs from the viable search space.