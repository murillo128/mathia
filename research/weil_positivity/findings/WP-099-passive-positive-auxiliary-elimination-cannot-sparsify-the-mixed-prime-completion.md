# WP-099 — Passive positive auxiliary elimination cannot sparsify the mixed-prime completion

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PASSIVE-REDUCTION + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-097` shows that the exact critical one-prime Weil moments can coexist with ordinary positivity and finite diagonal mass only because the positive prime-torus carrier contains mixed-prime Fourier terms. `WP-098` then proves that a positive/unital map on the same prime-torus algebra cannot erase those mixed modes while retaining the prime-coordinate unitaries, but leaves open an enlarged finite--archimedean architecture in which the prime observables first become strict contractions or interact with a non-scalar global sector.

There is a further exact obstruction to the most geometric version of that escape. Attaching an arbitrary positive auxiliary sector and then **eliminating it passively by energy minimization, Schur complement, or shorting cannot turn a finite-mass `WP-097` completion into the sparse Weil carrier**. The reason is order-theoretic and survives arbitrary auxiliary dimension: passive elimination produces a positive form dominated by the original finite form, whereas `WP-096` proves that sparse one-prime Weil support requires a diagonal that grows without bound as more primes are admitted.

More strongly, if the passive reduction preserves the original diagonal normalization exactly, then it cannot change **any** matrix coefficient at all. Thus a boundary-response/Dirichlet-principle route cannot keep the finite self-energy fixed while using an auxiliary archimedean sector to cancel the mixed-prime correlations that pay for positivity.

## 1. Prime-torus normal form and the passive-order hypothesis

Work in the multiplicative `B`-coordinates of `WP-096`. For `C>=C_*`, let `R_C` be the positive multiplicative Toeplitz form supplied by the `WP-097` product completion,

\[
R_C(\varepsilon_a,\varepsilon_b)
=\varphi_C(a/b),
\tag{1}
\]

with

\[
\varphi_C(1)=C,
\qquad
\varphi_C(p^k)
=-\frac{\log p}{p^{|k|/2}}
\quad(k\ne0),
\tag{2}
\]

and, for a reduced rational supported on a finite prime set `F`,

\[
\varphi_C\!\left(\prod_{p\in F}p^{k_p}\right)
=(-1)^{|F|}C^{1-|F|}
\prod_{p\in F}(\log p)p^{-|k_p|/2}.
\tag{3}
\]

In particular every multiplicative basis vector has the same diagonal energy,

\[
R_C(\varepsilon_m,\varepsilon_m)=C.
\tag{4}
\]

Now let `S` be any nonnegative Hermitian form on the same algebraic core satisfying the quadratic-form order

\[
\boxed{0\le S\le R_C.}
\tag{5}
\]

This is exactly the order relation produced by passive elimination from a larger positive energy. Indeed, suppose `Q` is a nonnegative Hermitian form on a finite sector plus an arbitrary auxiliary space `K`, with

\[
Q(x\oplus0,x\oplus0)=R_C(x,x).
\tag{6}
\]

Whenever the Dirichlet/shorted response

\[
S(x,x)=\inf_{y\in K}Q(x\oplus y,x\oplus y)
\tag{7}
\]

defines the candidate quadratic form, positivity gives the left inequality in (5), while choosing `y=0` gives the right inequality. In the usual block-operator case

\[
Q=
\begin{pmatrix}
R_C&B\\
B^*&D
\end{pmatrix}\succeq0,
\tag{8}
\]

with invertible positive `D`, (7) is the Schur complement

\[
S=R_C-BD^{-1}B^*\succeq0,
\tag{9}
\]

so (5) is explicit. General shorted-operator/form constructions preserve the same order even when the auxiliary sector is infinite-dimensional.

Thus the theorem below does not assume a particular archimedean Hilbert space, a finite rank coupling, a Stinespring representation, or refinement coherence. It uses only the defining passivity property of energy minimization.

## 2. Exact theorem: a dominated positive sparse output needs more diagonal than the input has

Assume that `S` is still an exact-cover-covariant candidate, so in the `WP-096` normal form it is multiplicative Toeplitz:

\[
S(\varepsilon_a,\varepsilon_b)=\psi(a/b).
\tag{10}
\]

Suppose one asks the passive reduction to produce the exact sparse finite-Weil support,

\[
\psi(p^k)
=-\frac{\log p}{p^{|k|/2}}
\qquad(k\ne0),
\tag{11}
\]

while

\[
\psi(r)=0
\tag{12}
\]

whenever the reduced rational `r` involves at least two distinct primes. Put

\[
C_S:=\psi(1).
\tag{13}
\]

Evaluating (5) on any basis vector gives immediately

\[
\boxed{C_S\le C.}
\tag{14}
\]

But `WP-096` proves, purely from positivity of the sparse multiplicative Toeplitz kernel, that on every finite prime set `P`,

\[
\boxed{
C_S\ge D(P)
:=2\sum_{p\in P}\frac{\log p}{\sqrt p-1}.
}
\tag{15}
\]

Since `D(P)` diverges along prime exhaustion,

\[
\boxed{
\text{finite }C
+0\le S\le R_C
+\text{exact sparse Weil rays}
\quad\Longrightarrow\quad
\text{contradiction}.
}
\tag{16}
\]

Equivalently, for every fixed finite input normalization `C`, choose `P` with `D(P)>C`. No passive positive reduction of the `WP-097` carrier can have the requested sparse restriction on that prime set, because it would have to satisfy simultaneously

\[
D(P)\le C_S\le C<D(P).
\tag{17}
\]

The obstruction is therefore not that an auxiliary sector is too small. The direction of the energy inequality is wrong: **sparsifying the positive completion requires more diagonal positivity budget, while passive elimination can only decrease the effective energy.**

## 3. Sharp two-prime failure at the minimal positive completion

At the sharp `WP-097` normalization

\[
C=C_*
=\frac{2\log2}{\sqrt2-1}
=:c_2,
\tag{18}
\]

the obstruction appears already on two prime coordinates. For `P={2,3}`,

\[
D(\{2,3\})
=c_2+c_3
=C_*+\frac{2\log3}{\sqrt3-1}
>C_*.
\tag{19}
\]

Hence every dominated positive form satisfies `C_S<=C_*`, while every positive sparse carrier with the exact `2`- and `3`-prime rays requires

\[
C_S\ge C_*+c_3.
\tag{20}
\]

So the minimal positive product completion cannot be converted into the sparse carrier by **any** positive Schur complement or shorted response even in the first nontrivial two-prime test. This is the passive-reduction analogue of the explicit two-coordinate failure of the Fourier/ANOVA projector in `WP-098`, but the mechanisms are different: `WP-098` says the desired same-algebra projector is not order preserving; here the reduction is order preserving and fails because it moves in the wrong order direction.

## 4. Diagonal-preserving passivity is completely rigid

There is a stronger local statement that does not use the divergent lower bound.

Suppose a positive reduction satisfies (5) and preserves the diagonal normalization,

\[
S(\varepsilon_m,\varepsilon_m)=C
\qquad\text{for every }m.
\tag{21}
\]

Then the difference

\[
E:=R_C-S
\tag{22}
\]

is a nonnegative Hermitian form with

\[
E(\varepsilon_m,\varepsilon_m)=0.
\tag{23}
\]

Cauchy--Schwarz for a nonnegative form gives

\[
|E(\varepsilon_m,x)|^2
\le E(\varepsilon_m,\varepsilon_m)E(x,x)=0,
\tag{24}
\]

so every basis vector lies in the nullspace of `E`. Hence

\[
\boxed{E=0\quad\text{and therefore}\quad S=R_C.}
\tag{25}
\]

Thus a passive auxiliary sector cannot alter even one mixed-prime coefficient while keeping all finite diagonal norms unchanged. In particular, on distinct primes `p,q`, the `WP-097` coefficient

\[
R_C(\varepsilon_p,\varepsilon_q)
=\varphi_C(p/q)
=\frac{(\log p)(\log q)}{C\sqrt{pq}}
\tag{26}
\]

cannot be changed to zero by a diagonal-preserving shorting. This is a Gram-geometric rigidity: subtracting a positive form without shortening any generating vector leaves all their mutual inner products unchanged.

## 5. Why strict contractions and arbitrary auxiliary dimension do not rescue passive reduction

`WP-098` correctly leaves open the possibility that an enlarged positive map compresses the coordinate unitaries to strict contractions, thereby escaping the multiplicative-domain theorem. The present obstruction is orthogonal to that issue.

A dilation or global auxiliary sector may be arbitrarily large and may indeed turn prime observables into strict contractions. If the proposed geometric sign theorem is nevertheless a **passive bulk-energy theorem** whose finite response is obtained by minimizing over the auxiliary variables, the resulting form still satisfies (5). No multiplicative-domain equality is used. Equations (14)--(17) then apply as soon as the reduced finite form is claimed to be the exact sparse cover-covariant Weil carrier.

The same is true for a positive scalar readout after an arbitrary positive auxiliary factorization. If

\[
C(\mathbb T^P)\xrightarrow{\Phi}B\xrightarrow{\omega}\mathbb C
\tag{27}
\]

has `Phi` positive and `omega` a positive functional, then `omega circ Phi` is again a positive functional on `C(T^P)`. Riesz--Markov turns it into a positive measure, and the `WP-096` sparse lower bound applies directly. Thus operator-valued intermediate positivity does not help if the last finite selector is still an ordinary positive scalar state.

These two observations close the natural inherited-positivity interpretations of “attach a global sector and then read out the finite selector”: positive scalarization and passive energy minimization both return to the positive cone already classified by `WP-096`.

## 6. Matched free-generator control

Nothing in the order argument is special to rational primes. Replace them by free multiplicative generators `g`, prescribe one-generator sparse moments

\[
\psi(g^k)=-a_g r_g^{|k|},
\qquad a_g>0,
\quad 0<r_g<1,
\tag{28}
\]

and set all mixed-generator coefficients to zero. The same finite-torus Fourier calculation used in `WP-096` gives the necessary positive diagonal

\[
C_S\ge
2\sum_{g\in F}\frac{a_gr_g}{1-r_g}
\tag{29}
\]

for every finite generator set `F`.

Therefore any finite-mass positive mixed completion whose passive reduction is dominated by the input has exactly the same obstruction whenever the right-hand side of (29) diverges. The rational-prime specialization

\[
a_p=\log p,
\qquad
r_p=p^{-1/2}
\tag{30}
\]

returns (15). This is a structural statement about positive Gram completion and passive reduction, not evidence that the rational primes themselves force RH.

## 7. Prior-art and novelty audit

The abstract operator theory is classical.

- The fact that minimizing a nonnegative block quadratic form produces a nonnegative Schur-complement/shorted form dominated by the original boundary block is standard linear and operator theory.
- W. N. Anderson, Jr. and G. E. Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics **28** (1975), 60--71, DOI `10.1137/0128007`, develops the shorted operator of a positive operator as the maximal positive operator below it with range in a prescribed subspace, including its network interpretation.
- Riesz--Markov representation of positive functionals on `C(X)` and Bochner representation of positive-definite functions on discrete abelian groups are classical; `WP-096` already uses the latter to classify the exact-cover-positive cone.
- Stinespring dilation and multiplicative-domain rigidity are not needed for the main theorem. Their role remains the distinct same-algebra obstruction recorded in `WP-098`.

No theorem-level novelty is claimed for Schur complements, shorted operators, positive-map composition, or Riesz/Bochner representation. The Mathia-specific result is the exact collision between that classical positivity order and the `WP-096`/`WP-097` prime-torus boundary:

\[
\boxed{
\text{mixed-prime finite-mass positive completion}
\xrightarrow{\text{passive positive elimination}}
\text{dominated positive response}
\not=\text{sparse Weil carrier}.
}
\tag{31}
\]

This materially narrows the explicit finite--archimedean escape left by `WP-098` without claiming that all enlarged global architectures have been ruled out.

## 8. Scope boundary and falsification surface

The result is intentionally narrower than the full research objective.

**A genuinely nonseparable global form remains open.** If the finite and archimedean pieces are never separated into a positive sparse finite response, but only acquire the explicit-formula decomposition after evaluating one assembled global quadratic form, then (5) need not describe the mechanism. This is now the principal surviving route.

**Changing the zero-auxiliary finite block remains open.** Equation (6) assumes that setting the auxiliary/global variable to zero recovers the `WP-097` positive completion. A geometry in which the global sector changes the finite block even at the level of the admissible state space, boundary condition, domain, or quotient is outside the theorem.

**Non-passive or relative reductions remain open.** A difference of positive forms, an indefinite off-diagonal matrix coefficient, a supertrace, or another relative construction need not satisfy `0<=S<=R_C`. Such a mechanism cannot inherit its sign from passive minimization and needs a separate global positivity theorem.

**Nonlinear readouts remain open.** Determinants, capacities, ranks, nonlinear quotient norms, or other scalar invariants are not automatically ordered as in (5). They must be audited separately and cannot borrow the present sign theorem.

**Diverging cutoff-dependent diagonal is not forbidden algebraically.** On each finite prime set a sparse positive carrier exists once its diagonal reaches `D(P)`. What is ruled out is obtaining an all-prime finite-mass carrier by passively eliminating a fixed finite-mass completion. A proposed renormalized infinite diagonal must derive its subtraction and final sign independently rather than hide the divergence.

A falsification under the stated hypotheses would require a nonnegative exact-cover-covariant form `S` with exact sparse coefficients, finite diagonal `C_S`, and `0<=S<=R_C` for some finite `C`. Equations (14)--(15) make such an example impossible once `P` is chosen with `D(P)>C`. A construction that violates domination, changes the finite block before reduction, retains mixed modes through the final global pairing, or changes the domain/topology lies outside the theorem rather than falsifying it.

## Research consequence

The mixed-prime completion of `WP-097` cannot be treated as a positive finite subsystem to which one simply attaches a passive archimedean bath and then integrates/minimizes the bath away. If the auxiliary sector is eliminated by a genuine positive Dirichlet principle, its boundary response has **less**, not more, positivity budget than the mixed completion, while exact sparse Weil support requires an unboundedly larger diagonal budget.

The live finite--archimedean route is therefore forced to be more strongly global:

\[
\boxed{
\text{do not isolate a sparse positive finite carrier after the global coupling.}
}
\]

A survivor must retain the mixed-prime sector until the final assembled pairing, change the finite observable/domain structure through the global geometry itself, or use a non-passive/relative/nonlinear mechanism with an independent sign theorem. Merely enlarging the Hilbert space or replacing prime-coordinate unitaries by strict contractions is not enough when the final reduction is a passive positive boundary response.