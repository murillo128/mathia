---
id: WP-276
title: Trace-class source surgery cannot manufacture the pole continuum
branch: weil_positivity
status: supported
kind: source-side-perturbative-spectral-type-obstruction
claim_strength: exact RH-independent no-go for trace-class and trace-class-resolvent self-adjoint repairs of a purely singular arithmetic source
created: 2026-09-13
related: [WP-188, WP-256, WP-273, WP-274, WP-275]
---

# WP-276 — Trace-class source surgery cannot manufacture the pole continuum

## Claim

`WP-275` shows that an exact bounded time intertwiner cannot carry Mathia's natural pure-point arithmetic dynamics into the nonzero absolutely continuous continuum appearing in the pole-completed normalization of `WP-273`. One apparent escape is to change the source dynamics first: add a finite-dimensional boundary sector, couple it to the arithmetic Hamiltonian, and hope that a self-adjoint perturbation turns the source into a mixed operator with the required continuous channel before positivity is imposed.

There is an exact perturbative boundary on that escape.

Let `A` be a self-adjoint arithmetic/source operator with no absolutely continuous spectrum,

\[
\mathcal H_{\rm ac}(A)=\{0\}.
\tag{1}
\]

Allow an auxiliary self-adjoint sector `K` which is itself wholly singular; finite-dimensional boundary variables are the main case. Set

\[
A_0=A\oplus K,
\qquad
\mathcal H_{\rm ac}(A_0)=\{0\}.
\tag{2}
\]

If `B` is obtained from `A_0` by a self-adjoint trace-class perturbation,

\[
B=A_0+V,
\qquad
V=V^*\in\mathcal S_1,
\tag{3}
\]

then Kato–Rosenblum gives unitary equivalence of the absolutely continuous parts. Hence

\[
\boxed{
\mathcal H_{\rm ac}(B)=\{0\}.
}
\tag{4}
\]

The same conclusion survives domain-changing or boundary-condition constructions whenever the self-adjoint operators are trace-class resolvent comparable: if, for one non-real `z`,

\[
(A_0-z)^{-1}-(B-z)^{-1}\in\mathcal S_1,
\tag{5}
\]

then Birman's extension of the trace-class scattering theorem gives complete wave operators and therefore unitary equivalence of the absolutely continuous parts. Again (4) follows.

Thus **finite-rank, trace-class, and trace-class-resolvent source-side surgery cannot manufacture the nonzero absolutely continuous carrier required by the `WP-273`/`WP-275` pole-completed model from a source whose spectral type is initially pure point or otherwise wholly singular.**

This is not a no-go against every mixed finite–archimedean construction. If an infinite-dimensional absolutely continuous archimedean sector is already present before the coupling, trace-class coupling may produce nontrivial scattering while preserving that a.c. sector. In that surviving architecture, however, the continuum has been supplied at zeroth order; it has not been generated from the arithmetic source by a small positive/boundary correction. The research burden then moves to deriving that a.c. archimedean sector intrinsically and proving that its coupling to the finite-prime source yields the Weil sign independently of the target formula.

## 1. Source-side setup after `WP-275`

The source-native Fock/prime-power dynamics isolated earlier in this line is pure point. In the simplest form relevant here one has eigenvectors

\[
A e_{p^k}=k\log p\,e_{p^k},
\tag{6}
\]

or the equivalent pure-point multiplication model on the arithmetic measure used in `WP-273`–`WP-275`. The exact atom weights do not matter for the present theorem; only the absence of an a.c. component matters.

On the other side, `WP-273`'s pole normalization produces a genuine continuum carrier. In the unitary normalization used in `WP-275` it is

\[
\mathcal H_{\rm pole}=L^2(\mathbb R,dx),
\qquad
(M_x g)(x)=xg(x),
\tag{7}
\]

whose spectral type is absolutely continuous. A self-adjoint source deformation intended to create a nonzero channel unitarily equivalent to a part of (7) must therefore acquire nonzero absolutely continuous spectrum.

`WP-275` already rules out the most rigid way of doing this: leave the source operator unchanged and use a bounded exact intertwiner from its pure-point representation to (7). The remaining natural perturbative proposal is instead

\[
A_{\rm source}
\longrightarrow
A_{\rm completed}
\longrightarrow
\mathcal H_{\rm pole},
\tag{8}
\]

where the first arrow is supposed to be a canonical finite-dimensional boundary correction, positive finite-rank coupling, trace-class energy correction, or closely related self-adjoint extension. Equations (3)–(5) show that this whole small-perturbation class fails before the second arrow can exist as an a.c. spectral channel.

## 2. Kato–Rosenblum kills additive trace-class manufacture of the continuum

For self-adjoint operators `A_0` and `B=A_0+V` with self-adjoint `V` trace class, the Kato–Rosenblum theorem says that the wave operators

\[
W_\pm(B,A_0)
\tag{9}
\]

exist and are complete. Equivalently, the restrictions of `A_0` and `B` to their absolutely continuous subspaces are unitarily equivalent.

Under (2), the a.c. part of `A_0` is the zero operator on the zero space. Completeness therefore forces

\[
P_{\rm ac}(B)=0.
\tag{10}
\]

No information about the arithmetic eigenvalue locations, prime weights, RH, the explicit formula, or positivity is used. In particular, making the perturbation positive does not help:

\[
V\ge0,
\qquad
V\in\mathcal S_1
\tag{11}
\]

still implies (10). Such a `V` may provide an attractive independent operator inequality, but it cannot simultaneously create the a.c. geometric channel to which that sign theorem would need to couple.

Finite-rank corrections are included automatically because

\[
\operatorname{rank}V<\infty
\quad\Longrightarrow\quad
V\in\mathcal S_1.
\tag{12}
\]

Hence adding finitely many boundary coordinates and coupling them to the source by a bounded finite-rank block is not merely too small quantitatively: it is exactly incapable of changing the spectral type in the required direction.

The theorem does not assert that the full spectral measure is unchanged. Trace-class perturbations can alter eigenvalues and singular spectrum substantially. What is invariant is precisely the part relevant to the `WP-273` target: the absolutely continuous component.

## 3. Domain-changing boundary conditions do not evade the obstruction when their resolvents differ by trace class

A boundary construction need not have the additive form (3). Two self-adjoint extensions of the same symmetric operator may have different domains, so `B-A_0` is not even a bounded operator. The correct invariant in that setting is the resolvent.

Birman's trace-class-resolvent theorem states that if

\[
(A_0-z)^{-1}-(B-z)^{-1}\in\mathcal S_1
\tag{13}
\]

for one non-real `z`, then the wave operators for `A_0` and `B` exist and are complete. Therefore their a.c. parts are again unitarily equivalent. With (2), this gives (10).

This matters for the geometric language of the present research line. A proposal such as

- attach finitely many archimedean boundary coordinates;
- impose a new self-adjoint matching condition;
- obtain a finite-rank Krein resolvent correction;
- read positivity from the resulting extension,

cannot manufacture the required pole continuum if the uncoupled operator has no a.c. part. Finite-rank resolvent corrections are trace class and lie exactly inside (13).

So the obstruction is not an artifact of insisting on a common operator domain. It covers the standard finite-deficiency-index boundary-condition mechanism as soon as the extensions are trace-class resolvent comparable.

## 4. A finite boundary sector cannot act as a hidden source of continuum

Let `F` be finite-dimensional and let

\[
A_0=A\oplus K_F
\tag{14}
\]

for any self-adjoint matrix `K_F`. Then `A_0` still has no a.c. spectrum. If a completed operator on `\mathcal H_A\oplus F` differs from (14) by a finite-rank or trace-class self-adjoint coupling, (10) follows.

The same statement holds if `F` is replaced by an infinite-dimensional but wholly singular self-adjoint auxiliary. What matters is

\[
\mathcal H_{\rm ac}(A)\oplus\mathcal H_{\rm ac}(K)=0.
\tag{15}
\]

Thus a discrete ``archimedean correction'' appended to the arithmetic source cannot, by any trace-class coupling, become the Lebesgue-type boundary sector required in the pole-completed Krein picture.

This sharpens an earlier recurring failure mode in the line. Several finite-dimensional archimedean repairs failed because of rank, signature, or inability to reproduce the Gamma carrier. Here the reason is independent of those details: **even before asking for the correct Gamma density, a trace-class perturbative completion of a wholly singular source cannot create any a.c. density at all.**

## 5. Matched control: a pre-existing a.c. archimedean sector survives

The decisive control is to start instead from

\[
A_0=A_{\rm arithmetic}\oplus A_\infty,
\qquad
\mathcal H_{\rm ac}(A_\infty)\ne0.
\tag{16}
\]

Then Kato–Rosenblum gives

\[
B_{\rm ac}\simeq (A_\infty)_{\rm ac}
\tag{17}
\]

for any trace-class self-adjoint coupling `B-A_0`. This does **not** trivialize the coupling. Discrete states can interact with the continuum, scattering data can be nontrivial, and a boundary response can change. The theorem says only that the a.c. channel was already present and its unitary equivalence class cannot be created or destroyed by the trace-class perturbation.

This is a genuine surviving route and prevents overreading the no-go. A Mathia-native construction could in principle produce an intrinsic infinite-dimensional archimedean continuum first and then couple the prime sector to it. To satisfy the research mandate it would still need to explain, without inserting the explicit formula by hand,

\[
\text{why this continuum, why the Gamma/pole normalization, why the finite-prime coupling, and why the final sign.}
\tag{18}
\]

`WP-188` already shows that one particularly classical version of this surviving picture fails on the target side: the exact Gamma phase is too large at infinity to be an ordinary trace-class Birman–Krein scattering determinant. The present finding is different. `WP-188` assumes an a.c. scattering setting and obstructs the exact Gamma determinant there; `WP-276` acts one step earlier and says that a trace-class perturbation of a wholly singular arithmetic source cannot create the a.c. setting in the first place.

## 6. The trace-class boundary is real, not a generic compactness no-go

The theorem should not be extended from `\mathcal S_1` to all compact or Hilbert–Schmidt perturbations. Classical Weyl–von Neumann theory, sharpened by Kuroda, shows that the Kato–Rosenblum trace-class threshold is essentially optimal among trace ideals: for ideals strictly larger than trace class, spectral type can change drastically. In particular, a self-adjoint operator can be changed to one with pure-point spectrum by a Hilbert–Schmidt perturbation; reversing the comparison gives examples where an `\mathcal S_2` perturbation takes a pure-point operator to one with continuous spectrum.

Therefore the durable conclusion is not

\[
\text{``small/compact corrections can never change spectral type.''}
\]

It is the sharper statement

\[
\boxed{
\text{a source-side spectral-type change required after `WP-275` must leave the trace-class / trace-class-resolvent regime,}
}
\tag{19}
\]

unless an a.c. sector is supplied independently at zeroth order.

The sharpness control is important methodologically. It exposes an actual analytic-category boundary rather than converting the failure of one construction into a vague impossibility claim.

## 7. Adversarial falsification and scope

The following attacks do not refute the claim because they leave its hypotheses.

1. **Use a Hilbert–Schmidt but non-trace-class coupling.** This is outside the theorem and is a legitimate escape. Such a candidate would need its own domain, spectral-type, and positivity analysis.

2. **Start with an intrinsic a.c. archimedean operator.** Also outside the manufacture claim. Equation (17) explicitly preserves this possibility.

3. **Use a nonlinear or nonunitary transform rather than a self-adjoint perturbation.** Kato–Rosenblum does not apply. Such a transform must still explain why the resulting positive form is geometrically canonical and not an inverse realization of the target, the failure already isolated in `WP-274`.

4. **Use an unbounded coupling whose resolvent difference is not trace class.** Again outside the theorem. This is precisely one of the nonperturbative categories left open by (19).

5. **Produce only a continuous scalar boundary function, not an a.c. spectral channel.** The theorem is about self-adjoint spectral type. A continuous response function can be generated in other ways, but it does not by itself realize the `L^2(\mathbb R,dx)` carrier of the `WP-273`/`WP-275` positivity problem.

6. **Create singular continuous spectrum.** This is not enough. Kato–Rosenblum permits changes in the singular part, but the target channel under discussion is absolutely continuous.

Conversely, a genuine counterexample within the stated class would be decisive: one would need self-adjoint `A_0,B` with `A_{0,ac}=0`, either `B-A_0 in S_1` or trace-class resolvent difference, and `B_ac != 0`. That would contradict the classical trace-class scattering theorem itself, not merely this Mathia application.

## 8. Prior-art and novelty audit

The operator theorem is classical and is **not** a Mathia discovery.

- The Kato–Rosenblum theorem gives existence and completeness of wave operators for self-adjoint trace-class perturbations and hence unitary equivalence of the a.c. parts.
- Birman's extension gives the same a.c. equivalence when the resolvent difference is trace class; this is the relevant form for domain-changing and boundary-condition comparisons.
- Weyl–von Neumann/Kuroda results show why trace class is the meaningful threshold: trace ideals strictly larger than `S_1` do not preserve the a.c. spectral type in this way.

An audit-friendly modern source is Barry Simon, *Tosio Kato's work on non-relativistic quantum mechanics: part 2*, Bulletin of Mathematical Sciences (2018), DOI `10.1007/s13373-018-0121-5`, especially the discussion of the Kato–Rosenblum theorem and Birman's trace-class-resolvent extension.

The local Mathia novelty audit also matters. `WP-188` already invokes trace-class scattering, but for a different target-side obstruction: an existing a.c. scattering pair cannot have the exact Gamma carrier as an ordinary `L^1` Birman–Krein determinant. `WP-275` uses pure-point versus a.c. type to kill a bounded exact intertwiner, but explicitly leaves a source-side spectral-type change as an escape. No earlier finding in this branch was found to apply Kato–Rosenblum to close the **trace-class source-deformation** portion of that escape.

Accordingly the durable delta is not a new scattering theorem. It is the branch-specific classification

\[
\boxed{
\text{`WP-275`'s ``change spectral type first'' escape cannot be implemented by trace-class or trace-class-resolvent self-adjoint source surgery.}
}
\tag{20}
\]

That is a strict narrowing of the allowed architecture and survives the matched controls above.

## 9. Consequence for the `weil_positivity` frontier

The source-first frontier now has a more exact hierarchy.

`WP-273` requires a genuinely global/nonlocal mechanism because finite-box positivity cannot certify the pole-completed sign. `WP-274` excludes target-supplied inverse Clark/canonical realizations as independent evidence. `WP-275` says a direct bounded exact pure-point-to-a.c. time intertwiner is zero. `WP-276` now shows that **one cannot evade that spectral mismatch by a finite-rank or trace-class self-adjoint repair of the source, including the standard trace-class-resolvent boundary-extension regime.**

A surviving Mathia-native mechanism must therefore do at least one of two substantially stronger things:

\[
\begin{aligned}
&\text{(A) derive an intrinsic infinite-dimensional a.c. archimedean sector before coupling,}\\
&\text{or}\\
&\text{(B) perform a genuinely non-trace-class/nonperturbative spectral-type change.}
\end{aligned}
\tag{21}
\]

Neither route is close to a proof of Weil positivity. Route (A) must still explain why the finite-prime and Gamma/pole pieces are forced by one geometry and why their coupled form is nonnegative. Route (B) must establish self-adjointness/closability, the new spectral type, and an independent positivity theorem without using the target zero data or an arbitrary regularization.

The finding is therefore negative but substantive: it turns the vague instruction "change spectral type before positivity" left by `WP-275` into an operator-ideal boundary with an exact theorem, a matched surviving control, and a falsifiable next architectural test.

## Conclusion

A purely arithmetic or otherwise wholly singular Mathia source cannot acquire the nonzero absolutely continuous pole carrier through finite-dimensional boundary augmentation followed by finite-rank, trace-class, or trace-class-resolvent self-adjoint coupling. Kato–Rosenblum/Birman invariance forces the a.c. part to remain zero.

The route is not globally closed. What remains is more specific: **either the archimedean continuum must be intrinsic from the beginning, or the source must undergo a genuinely non-trace-class spectral-type change before any geometric positivity theorem can bridge it to the pole-completed Weil form.**