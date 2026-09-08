# PL-219 — Bost–Connes KMS scalar readouts factor through the diagonal gauge expectation

## Claim

The full noncommutative `C*`-completion of the rational Bost–Connes system does **not** provide an extra scalar equilibrium channel beyond its cyclotomic diagonal. Let

\[
\mathcal A_{BC}=C^*(\mathbb Q/\mathbb Z)\rtimes\mathbb N^\times,
\qquad
\mathcal D=C^*(\mathbb Q/\mathbb Z)\cong C(\widehat{\mathbb Z}).
\]

There is a canonical prime-gauge action of

\[
\mathbb T^{\mathcal P}
\cong \operatorname{Hom}(\mathbb Q_+^\times,\mathbb T)
\]

on `A_BC`, determined by

\[
\gamma_z(e(r))=e(r),
\qquad
\gamma_z(\mu_n)=z(n)\mu_n.
\]

The Bost–Connes time evolution is the one-parameter subgroup

\[
\sigma_t=\gamma_{z(t)},
\qquad
z_p(t)=e^{it\log p}=p^{it}.
\]

Because the prime logarithms have no nontrivial finite integer relation, this one-parameter subgroup is dense in the full prime gauge torus. The fixed-point algebra is exactly the diagonal `D`. Hence Haar averaging over the gauge torus gives a positive unital conditional expectation

\[
E:\mathcal A_{BC}\longrightarrow\mathcal D
\]

and **every Bost–Connes KMS state** `phi` satisfies

\[
\boxed{\phi=\phi\circ E.}
\]

Consequently, for every bounded positive contraction `X in A_BC`,

\[
0\le E(X)\le1,
\qquad
\|E(X)\|\le1,
\qquad
\boxed{\phi(X)=\phi(E(X))}
\]

for every equilibrium state at every positive inverse temperature for which that KMS state exists. In particular, for the unique high-temperature states `phi_beta`, `0<beta<=1`, the entire scalar temperature profile

\[
\beta\longmapsto\phi_\beta(X)
\]

is exactly the profile of the diagonal positive contraction `E(X)`.

This closes the principal bounded-`C*` scalar loophole left explicitly open by `PL-214`: passing from the algebraic Bost–Connes core to arbitrary bounded noncommuting observables cannot restore a new one-point KMS readout near `beta=1/2`. Combined with `PL-218`, which shows that finite-prime diagonal positive contractions already uniformly program arbitrary continuous `[0,1]` profiles on compact intervals inside `(0,1)`, **noncommutativity of the full bounded observable algebra does not rescue scalar-temperature rigidity**.

The result is deliberately restricted to scalar KMS evaluations. It does not diagonalize an operator inside a GNS representation, trivialize a whole time-dependent correlation process, rule out unbounded affiliated operators, or eliminate relative modular/scattering/trace-formula constructions.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. The Bost–Connes time flow is dense in the full prime gauge torus

The standard Bost–Connes presentation used already in `PL-214` has generators `e(r)`, `r in Q/Z`, and multiplicative isometries `mu_n`, with

\[
\sigma_t(e(r))=e(r),
\qquad
\sigma_t(\mu_n)=n^{it}\mu_n.
\]

Unique factorization identifies the group completion of the positive semigroup with

\[
\mathbb Q_+^\times
\cong \mathbb Z^{(\mathcal P)},
\]

so its compact dual is the infinite prime torus

\[
G=\widehat{\mathbb Q_+^\times}\cong\mathbb T^{\mathcal P}.
\]

For `z=(z_p)_p in G`, write

\[
z(n)=\prod_p z_p^{v_p(n)}.
\]

Multiplying every `mu_n` by `z(n)` preserves the Bost–Connes relations because all occurrences of an isometry together with its adjoint have cancelling gauge degree. Thus `gamma_z` is a well-defined continuous action of `G` on `A_BC`.

The physical time evolution is obtained by restricting this action to

\[
z(t)=(p^{it})_p.
\]

To test density, take a continuous character of `G`. Every such character depends on finitely many primes and has the form

\[
\chi_k(z)=\prod_p z_p^{k_p},
\qquad k\in\mathbb Z^{(\mathcal P)}.
\]

If `chi_k` is trivial on the time orbit, then

\[
1=\chi_k(z(t))
=\exp\!\left(it\sum_p k_p\log p\right)
\]

for every real `t`. Therefore

\[
\sum_p k_p\log p=0,
\]

which is equivalent to

\[
\prod_p p^{k_p}=1.
\]

Unique factorization forces every `k_p=0`. By the character criterion for compact abelian groups, no nontrivial character annihilates the time orbit, and hence

\[
\boxed{\overline{\{z(t):t\in\mathbb R\}}=G.}
\]

This is exactly the same prime-log Kronecker mechanism that appears elsewhere in the line, but here its consequence is a **negative rigidity statement**: time invariance already implies invariance under every independent prime phase.

## 2. Gauge averaging lands exactly on the cyclotomic diagonal

Let `H_BC` denote the dense algebraic core from `PL-214`. It has the standard coprime monomial basis

\[
x_{m,n,r}=\mu_m e(r)\mu_n^*,
\qquad (m,n)=1.
\]

The gauge action gives

\[
\gamma_z(x_{m,n,r})
=z(m/n)x_{m,n,r}.
\]

Average over normalized Haar measure on `G`:

\[
E(a)=\int_G\gamma_z(a)\,dz.
\]

This is a positive unital contractive conditional expectation onto the gauge fixed-point algebra. For a basis monomial,

\[
E(x_{m,n,r})=0
\]

unless the gauge degree `m/n` is trivial. Because the basis is coprime, `m/n=1` forces `m=n=1`; the surviving monomial is simply `e(r)`. Therefore

\[
E(H_{BC})\subset\operatorname{span}\{e(r):r\in\mathbb Q/\mathbb Z\}.
\]

Conversely every `e(r)` is fixed. Since `H_BC` is norm dense, `E` is contractive, and the span of the `e(r)` is dense in `D`, it follows that

\[
\boxed{\mathcal A_{BC}^{G}=\mathcal D.}
\]

The density from the previous section also gives

\[
\mathcal A_{BC}^{\sigma}=\mathcal A_{BC}^{G}=\mathcal D.
\]

Thus there is no hidden bounded zero-energy sector in the completion beyond the diagonal. The possible accumulation of rational log-frequencies near zero does not enlarge the fixed-point algebra: the full compact gauge action supplies a bounded projection onto the exact zero grade.

## 3. Every KMS state factors through the same diagonal expectation

A KMS state for a `C*`-dynamical system is invariant under its time evolution. Hence, for every Bost–Connes KMS state `phi`,

\[
\phi\circ\sigma_t=\phi
\qquad(t\in\mathbb R).
\]

For fixed `a in A_BC`, the function

\[
z\longmapsto\phi(\gamma_z(a))
\]

is continuous on `G`. Since the physical time orbit is dense in `G` and the function is constant on that orbit, it is constant on all of `G`. Therefore `phi` is fully gauge invariant:

\[
\phi\circ\gamma_z=\phi
\qquad(z\in G).
\]

Averaging gives

\[
\phi(E(a))
=\int_G\phi(\gamma_z(a))\,dz
=\phi(a),
\]

so

\[
\boxed{\phi=\phi\circ E.}
\]

This argument is independent of the phase transition and therefore applies to every KMS state, including the low-temperature extremal states. That does **not** mean the low-temperature `1/zeta(beta)` normalization disappears: it already lives in the restriction of those states to the diagonal `D`. The theorem removes off-diagonal bounded observables as an *additional scalar channel*; it does not remove arithmetic already present in the diagonal state itself.

For `0<beta<=1` there is a unique state `phi_beta`, so the same fixed expectation `E`, independent of `beta`, satisfies

\[
\boxed{
\phi_\beta(X)=\phi_\beta(E(X))
\quad\text{for every }X\in\mathcal A_{BC},\ 0<\beta\le1.
}
\]

If `X` is positive or a positive contraction, positivity and contractivity of `E` preserve those constraints exactly. Thus a source-forced claim based only on the scalar graph `beta -> phi_beta(X)` cannot use noncommutativity to escape the diagonal matched controls.

## 4. Relation to `PL-214` and `PL-218`

`PL-214` proved directly on the algebraic core that KMS invariance kills every nonzero signed prime-lattice grade, and therefore every fixed finite algebraic correlation is a finite Dirichlet polynomial in `beta`. It explicitly left the full `C*`-completion open because a norm limit may contain infinitely many grades and need not retain the finite-polynomial form.

The present finding closes exactly the **scalar bounded-observable** part of that loophole. It does not claim that `phi_beta(X)` for arbitrary `X in A_BC` is a finite Dirichlet polynomial. Instead it proves the stronger structural reduction

\[
X\longmapsto E(X)\in\mathcal D
\]

before taking the KMS expectation. Infinite norm limits may have complicated temperature dependence, but that dependence is already realizable by a diagonal continuous observable.

`PL-218` then supplies the relevant adversarial control near the Riemann half. On every compact interval

\[
0<a<b<1,
\]

finite-prime diagonal positive contractions can uniformly approximate any prescribed continuous `[0,1]` scalar temperature profile. Consequently the conjunction

\[
\text{full bounded Bost--Connes algebra}
+\text{noncommutativity}
+\text{positivity}
+\text{norm-one budget}
+\text{special scalar behavior near }\beta=1/2
\]

still does not constitute an RH mechanism. A viable proposal must use information not captured by a one-point KMS scalar readout.

## 5. Adversarial boundaries

**A whole time-dependent correlation process is not reduced to one fixed diagonal observable.** For fixed bounded `X_1,...,X_k` and fixed real times `t_1,...,t_k`, the product

\[
Y=\sigma_{t_1}(X_1)\cdots\sigma_{t_k}(X_k)
\]

is one element of `A_BC`, so

\[
\phi_\beta(Y)=\phi_\beta(E(Y)).
\]

But `E(Y)` depends on the inputs and the times. The theorem does not say that the full function of all time variables is generated by one time-independent diagonal observable, nor does it trivialize its Fourier spectrum.

**GNS operator spectra remain outside the claim.** The statement concerns scalar state evaluation. A non-diagonal operator can have nontrivial spectrum, commutators, scattering data, or modular behavior in a KMS representation even though its one-point expectation equals that of its gauge average.

**Unbounded affiliated observables remain outside the claim.** Haar averaging is used on the bounded `C*`-algebra. An unbounded operator or quadratic form requires a separate domain and integrability analysis.

**No analytic continuation is performed.** The factorization is a real-temperature KMS identity. It neither continues `zeta(beta)` through `beta=1` nor imports an Euler product into the critical strip.

**The result is not rational-prime specific enough to support RH.** The density argument uses only that the energy labels have no nontrivial finite integer relation. A generic free multiplicative system with rationally independent energies has the same dense one-parameter subgroup and the same gauge-diagonalization mechanism. The ordinary primes satisfy the hypothesis canonically by unique factorization, but the conclusion itself therefore fails the line's Beurling/generic-control discrimination test.

**A genuinely source-forced relation may still survive outside scalar expectation.** The result does not close the current line-level requirement from `mind/RESEARCH_LINES.md`: a canonical relation among prime channels could still appear in operator-valued correlations, modular data, an infinite trace/positivity identity, a completed adelic construction, or another object that is not collapsed by `phi=phi o E`.

## 6. Prior art and novelty audit

The algebra, relations, time evolution, and KMS framework are classical Bost–Connes theory, already recorded as source 5 in `research/prime_lattice/SOURCES.md`:

- Jean-Benoît Bost and Alain Connes, “Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,” *Selecta Mathematica, New Series* **1** (1995), 411–457. DOI `10.1007/BF01589495`.

The extra steps used here are standard compact-group/KMS machinery: construct the gauge action from the free multiplicative grading, use unique factorization to prove density of the physical one-parameter subgroup, Haar-average onto the fixed algebra, and use time invariance of KMS states. A targeted prior-art audit around KMS states for dense one-parameter subgroups of gauge actions found this density-to-gauge-invariance argument as established operator-algebra technique in related graph `C*`-dynamical systems. No novelty is claimed for that mechanism.

The durable line-specific contribution is instead the **closure of an explicit research loophole**. `PL-214` left arbitrary bounded norm limits outside its finite algebraic calculation; `PL-219` proves that, at the level of scalar equilibrium evaluation, every such norm limit is exactly replaceable by a diagonal observable. That negative conclusion is what is being stored.

## Falsification / audit tests

The finding would be materially falsified or require narrowing if any of the following failed:

1. the standard Bost–Connes relations did not admit the full character gauge action `gamma_z(mu_n)=z(n)mu_n`;
2. the prime-log time subgroup were not dense in that gauge torus;
3. the gauge fixed-point algebra contained a bounded element outside `C^*(Q/Z)`;
4. a Bost–Connes KMS state failed to be invariant under the physical time evolution;
5. Haar averaging failed to be a positive unital conditional expectation onto the gauge fixed-point algebra; or
6. a bounded positive contraction `X` had a scalar KMS value different from the diagonal contraction `E(X)`.

Each point is independently checkable from the classical presentation plus standard compact-group `C*` dynamics. None depends on RH.

## Consequence for the research line

The surviving Bost–Connes program is narrower than after `PL-218`. It is no longer enough to move from finite diagonal observables to arbitrary bounded **non-diagonal** observables and inspect their one-point equilibrium values. The prime-log dynamics is dense in the full phase torus, so equilibrium scalarization automatically erases every nonzero gauge grade.

A meaningful next mechanism must therefore live in structure that the KMS scalar expectation does not quotient out: a source-forced relation visible in operator-valued or multi-time data, a canonical unbounded/global object with controlled continuation, a relative modular or scattering invariant with non-programmable arithmetic compatibility, or a completed trace/positivity formula. Merely choosing a more sophisticated bounded Bost–Connes observable and plotting `beta -> phi_beta(X)` near `1/2` is now a closed route.