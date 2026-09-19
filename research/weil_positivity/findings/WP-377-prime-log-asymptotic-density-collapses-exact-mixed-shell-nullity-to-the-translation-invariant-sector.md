---
id: WP-377
title: Prime-log asymptotic density collapses exact mixed-shell nullity to the translation-invariant sector
branch: weil_positivity
status: supported
kind: cyclotomic-log-radial-prime-log-ergodic-closure-obstruction
claim_strength: exact RH-independent no-go showing that in every strongly continuous unitary log-radial Hilbert topology, the closed span of spectator-prime mixed shells contains the entire non-invariant part of each prime-power shell; any closable positive form making all mixed shells null therefore factors through the translation-invariant sector, which in scalar Fourier realizations is only the zero Mellin trace and again gives Lambda-squared rather than the linear Weil weight
created: 2026-09-19
related: [WP-162, WP-374, WP-375, WP-376]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical cyclotomic identity Phi_nq(x)=Phi_n(x^q)/Phi_n(x) for q prime and q not dividing n
  - prime number theorem consequence p_{k+1}/p_k -> 1, equivalently log p_{k+1}-log p_k -> 0
  - uniform continuity of matrix coefficients of strongly continuous unitary one-parameter groups
  - von Neumann mean ergodic theorem for strongly continuous unitary R-actions
---

# WP-377 — Prime-log asymptotic density collapses exact mixed-shell nullity to the translation-invariant sector

## Claim

`WP-375` and `WP-376` left a precise topological escape: perhaps the cyclotomic log-radial profiles admit a singular, non-Sobolev Hilbert topology in which far translations do not vanish weakly. That escape is not available if the new topology still carries the radial translations as an ordinary strongly continuous unitary one-parameter group.

Let `H` be a Hilbert space containing the canonical log-radial shell profiles

\[
h_n(u)=e^u\rho_n(e^u),
\]

and suppose the translations extend to a strongly continuous unitary representation

\[
U(t):H\to H,
\qquad t\in\mathbb R,
\]

for which the exact cyclotomic relation remains

\[
\boxed{
h_{nq}=(U(\log q)-I)h_n
}
\tag{1}
\]

whenever `q` is prime and `q` does not divide `n`. Let `P_0` denote the orthogonal projection onto the translation-invariant subspace

\[
H^U=\{v\in H:U(t)v=v\ \text{for every }t\in\mathbb R\}.
\tag{2}
\]

Then for every prime power `n=p^a`,

\[
\boxed{
(I-P_0)h_n\in
\overline{\operatorname{span}}^{H}
\{h_{nq}:q\ne p\text{ prime}\}.
}
\tag{3}
\]

Thus the infinite family of mixed spectator shells reconstructs **every non-invariant radial component** of the prime-power shell in *any* strongly continuous unitary radial topology. No absolutely-continuous spectral measure, Sobolev norm, mixing hypothesis, Rajchman hypothesis, or stationarity of the candidate positive form is required.

Consequently, let `D subset H` be a linear domain containing the shell profiles and let `Q` be a nonnegative Hermitian form on `D` that is closable in `H`. If

\[
Q(h_m)=0
\qquad
\text{for every }m\text{ having at least two distinct prime factors},
\tag{4}
\]

then the closure of `Q` identifies every prime-power shell with its invariant projection:

\[
P_0h_{p^a}\in\operatorname{Dom}(\overline Q),
\qquad
\boxed{
\overline Q(P_0h_{p^a})=Q(h_{p^a}).
}
\tag{5}
\]

In particular, if the source-generated radial subspace has no translation-invariant vector, then

\[
Q(h_{p^a})=0
\qquad\text{for every prime power }p^a.
\tag{6}
\]

For a scalar Fourier/spectral realization, the invariant sector is exactly the zero Mellin-frequency atom. Since

\[
\widehat h_n(0)=\int_{\mathbb R}h_n(u)\,du=\Lambda(n),
\tag{7}
\]

any surviving scalar positive form on the shell span again reduces to

\[
Q(h_m,h_n)=c\,\Lambda(m)\Lambda(n),
\qquad c\ge0,
\tag{8}
\]

and hence to `c Lambda(n)^2` on the diagonal. Under the critical half-density normalization `n^{-1/4}`, this is

\[
c\frac{\Lambda(n)^2}{\sqrt n},
\tag{9}
\]

not the finite Weil coefficient `Lambda(n)/sqrt(n)`.

The remaining radial-topology escape from `WP-376` is therefore much smaller than “use singular spectral data.” **Any strongly continuous unitary radial topology, including arbitrary singular and non-Rajchman scalar spectral measures, collapses exact mixed-shell nullity to its translation-fixed sector.** A genuinely new route must break at least one of those hypotheses or keep the mixed shells active until after a different global assembly.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CYCLOTOMIC-TRANSLATION-COBOUNDARY + PRIME-LOG-SHRINKING-MESH + UNITARY-MATRIX-COEFFICIENT-UNIFORM-CONTINUITY + MEAN-ERGODIC-PROJECTION + ALL-STRONGLY-CONTINUOUS-UNITARY-RADIAL-TOPOLOGIES + CLOSABLE-POSITIVE-RADICAL-RIGIDITY + ZERO-MELLIN-SCALAR-SHARPENING + LAMBDA-SQUARED + MATCHED-SPARSE-SCALE-CONTROL + NO-ZERO-DATA + CLASSICAL-INGREDIENTS + NOT-A-GLOBAL-WEIL-POSITIVITY-PROOF`.

## 1. The source identity supplies the mixed-shell difference vectors

The cyclotomic identity already used in `WP-374`--`WP-376`,

\[
\Phi_{nq}(x)=\frac{\Phi_n(x^q)}{\Phi_n(x)}
\qquad(q\nmid n),
\tag{10}
\]

gives after differentiating the radial potential and passing to `u=log s`

\[
h_{nq}=\tau_{\log q}h_n-h_n.
\tag{11}
\]

The present theorem assumes only that the chosen source-native Hilbert topology extends these translations to the strongly continuous unitary group `U(t)` and preserves (11) as (1). It does **not** assume that `Q` itself is translation invariant.

Fix a prime power `n=p^a` and write

\[
M_n=
\overline{\operatorname{span}}^H
\{(U(\log q)-I)h_n:q\ne p\text{ prime}\}.
\tag{12}
\]

Equation (3) is the statement that the quotient of `h_n` by this mixed-shell closure is precisely its translation-invariant component.

## 2. Prime logarithms have shrinking mesh

List the spectator primes in increasing order as `q_1<q_2<...`. The prime number theorem gives

\[
q_k\sim k\log k,
\tag{13}
\]

and therefore

\[
\frac{q_{k+1}}{q_k}\longrightarrow1.
\tag{14}
\]

Equivalently,

\[
\boxed{
\log q_{k+1}-\log q_k\longrightarrow0.
}
\tag{15}
\]

Deleting the single prime `p` does not affect this limit. This shrinking mesh is the arithmetic input that replaces the weak-escape hypothesis of `WP-375` and `WP-376`.

It is stronger for the present purpose than mere infinitude of spectator primes: every sufficiently large radial time lies arbitrarily close to the logarithm of an actual spectator prime.

## 3. Orthogonality to every mixed shell forces a matrix coefficient to have a limit

Take `g in M_n^perp` and define the matrix coefficient

\[
f_g(t)=\langle U(t)h_n,g\rangle_H.
\tag{16}
\]

By (12), for every spectator prime `q`,

\[
0=\langle (U(\log q)-I)h_n,g\rangle,
\]

so

\[
\boxed{
f_g(\log q)=f_g(0).
}
\tag{17}
\]

Strong continuity and unitarity make `f_g` uniformly continuous on the entire real line. Indeed,

\[
|f_g(t+s)-f_g(t)|
=|\langle U(t)(U(s)-I)h_n,g\rangle|
\le
\|(U(s)-I)h_n\|\,\|g\|,
\tag{18}
\]

and the right-hand side is independent of `t` and tends to zero with `s`.

Now let `t` lie between `log q_k` and `log q_{k+1}`. By (17)--(18),

\[
|f_g(t)-f_g(0)|
\le
\omega_g(\log q_{k+1}-\log q_k),
\tag{19}
\]

where `omega_g(delta)->0` as `delta->0`. Using (15),

\[
\boxed{
f_g(t)\longrightarrow f_g(0)
\qquad(t\to+\infty).
}
\tag{20}
\]

This step is what removes the spectral-type restriction from `WP-376`. A singular continuous Fourier-Stieltjes coefficient need not decay, but if it agrees with its value at zero at **every prime logarithm**, strong continuity plus the shrinking prime-log mesh forces a genuine full-time limit anyway.

## 4. The mean ergodic theorem identifies that limit with the invariant projection

For a strongly continuous unitary `R`-representation, the mean ergodic theorem gives

\[
A_T h_n
:=\frac1T\int_0^T U(t)h_n\,dt
\longrightarrow
P_0h_n
\qquad\text{strongly in }H.
\tag{21}
\]

Taking the inner product with `g`,

\[
\frac1T\int_0^T f_g(t)\,dt
\longrightarrow
\langle P_0h_n,g\rangle.
\tag{22}
\]

But (20) says `f_g(t)` itself converges to `f_g(0)=<h_n,g>`, so its Cesaro mean has the same limit. Hence

\[
\langle h_n,g\rangle
=
\langle P_0h_n,g\rangle,
\tag{23}
\]

or

\[
\langle (I-P_0)h_n,g\rangle=0.
\tag{24}
\]

This holds for every `g in M_n^perp`. Therefore

\[
(I-P_0)h_n\in(M_n^perp)^perp=M_n,
\tag{25}
\]

which proves (3).

The argument is exact and uses neither zeta zeros nor any assumption equivalent to RH. The only arithmetic distribution input is the unconditional shrinking mesh (15).

## 5. Closability pushes the positive form entirely onto the invariant sector

Assume now (4). Positivity gives the form Cauchy--Schwarz inequality, so every mixed shell is radical:

\[
Q(h_m)=0
\quad\Longrightarrow\quad
Q(h_m,z)=0
\quad(z\in D).
\tag{26}
\]

By (3), choose finite linear combinations `y_j` of the mixed shells `h_{nq}` such that

\[
y_j\longrightarrow-(I-P_0)h_n
\qquad\text{in }H.
\tag{27}
\]

Every `y_j` is radical. Set

\[
z_j=h_n+y_j.
\tag{28}
\]

Then

\[
z_j\longrightarrow P_0h_n
\qquad\text{in }H,
\tag{29}
\]

while

\[
Q(z_j-z_k)=0,
\qquad
Q(z_j)=Q(h_n).
\tag{30}
\]

Thus `(z_j)` is Cauchy in the graph norm of the closure of `Q`. Closability implies that its ambient limit `P_0h_n` belongs to `Dom(overline Q)` and that

\[
\overline Q(P_0h_n)=Q(h_n),
\tag{31}
\]

proving (5). If `P_0h_n=0`, the sequential closability criterion applied directly to (28)--(30) gives (6).

So changing the ambient topology can help only by creating a genuine translation-fixed component. Nonzero oscillatory, singular-continuous, pure-point, or otherwise exotic spectral content cannot survive merely because far translates fail to be mixing.

## 6. Scalar spectral topologies still reduce exactly to the zero Mellin trace

Consider an arbitrary scalar translation-invariant spectral Hilbert realization in which translations act as

\[
(U(t)F)(\xi)=e^{it\xi}F(\xi)
\tag{32}
\]

on some positive Borel spectral measure, with the shell profiles in the domain. Strong continuity follows by dominated convergence and does not require the measure to be absolutely continuous, Rajchman, or regular in any stronger sense.

The invariant subspace in (2) is supported at `xi=0`. Therefore, if the spectral measure has no atom at zero, `P_0h_n=0` and every prime-power shell is killed by (6). If it has a scalar zero-frequency atom, then (7) gives

\[
P_0h_n=\Lambda(n)e_0
\tag{33}
\]

up to the fixed normalization of the zero-mode basis vector.

Equation (5) says that the closed positive form on the shell span factors through this one scalar coordinate. Hence by polarization it has the rank-one form (8). The singular/non-Rajchman part of the spectral measure is irrelevant to the surviving arithmetic coefficient: exact mixed-shell nullity forces all of it into the closure of the mixed-shell radical.

This strictly strengthens the spectral boundary in `WP-376`. That finding closed every absolutely-continuous Fourier-weight topology and showed that one nonzero trace atom cannot work. The present argument closes **all** strongly continuous scalar spectral measures at once, including arbitrary collections of nonzero atoms and singular continuous measures with no Fourier decay.

## 7. Matched controls show exactly which hypotheses carry the obstruction

The first control is the zero Mellin trace. If the topology explicitly retains `hat f(0)`, then `P_0` is nonzero and the theorem does not kill the prime-power shell. It instead predicts exactly the known survivor (8). Thus the theorem does not hide the `WP-374`/`WP-376` counterexample; it classifies it as the invariant quotient.

The second control is a sparse artificial scale set. Replace the actual spectator-prime times by

\[
t_k=\frac{2\pi k}{\xi_0},
\qquad \xi_0\ne0,
\tag{34}
\]

and take the one-dimensional nontrivial character `U(t)=e^{i\xi_0 t}`. Then

\[
(U(t_k)-I)h=0
\tag{35}
\]

for every `k`, while the representation has no invariant vector and `h` survives. The difference from the prime case is exactly that the mesh `t_{k+1}-t_k` stays positive. Thus an arbitrary infinite family of spectator scales would not prove (3); the shrinking mesh of **actual prime logarithms** is load-bearing.

The third control is finite truncation. With only finitely many spectator primes, `WP-375` already constructs bounded rank-one positive forms that annihilate the tested mixed shells and retain the chosen prime-power shell. Equation (3) is therefore genuinely an infinite-prime closure theorem.

The fourth control is structural. If the ambient radial action is not unitary/translation-compatible, if it is not strongly continuous, or if mixed shells are allowed nonzero final energy, the proof does not apply. Those are real remaining categories rather than hidden exceptions.

Finally, an invariant sector of multiplicity greater than one is not excluded abstractly. But every surviving component is then **radial-scale invariant** before positivity is evaluated. A candidate using such multiplicity must derive it from additional source geometry and show that it carries the finite--archimedean incidence and linear Weil coefficient; the one-dimensional scalar radial realization has only the net-Mangoldt trace and therefore returns (9).

## 8. Adversarial novelty audit

Every general ingredient in the proof is classical. The cyclotomic recurrence is standard; (15) is an immediate consequence of the prime number theorem; (18) is the elementary uniform-continuity estimate for matrix coefficients of a strongly continuous unitary group; and (21) is the von Neumann mean ergodic theorem. No novelty is claimed for any of those statements.

A bounded literature search found no prior result combining the cyclotomic spectator identity with the shrinking mesh of prime logarithms and the ergodic projection to classify exact Mangoldt-shell nullity in this way. The mathematical novelty claim is therefore only **application-level inside the Mathia construction**: the topology escape left by `WP-376` collapses from arbitrary singular spectral type to the translation-invariant quotient under a much weaker and representation-theoretically natural hypothesis.

This is not classical Weil positivity, a Hilbert--Polya construction, a Sonin/localization criterion, a Connes trace formula, or a zero-defined spectrum. The proof never inserts zeta zeros and does not prove a Weil-positive global form. Conversely, it strengthens a negative result rather than relabeling an RH-equivalent positivity criterion: exact mixed-shell nullity is shown to be incompatible with retaining non-invariant radial information before any zero data enter.

## Consequence for the Weil-positivity search

The ordinary “choose a more singular radial Hilbert topology” continuation is now exhausted as long as radial translations remain a strongly continuous unitary symmetry. The obstruction no longer depends on weak mixing, Riemann--Lebesgue decay, Sobolev regularity, or absolute continuity of spectral measure. Actual prime logarithms sample the radial action with asymptotically vanishing gaps, and that alone is enough to force the quotient onto the invariant sector.

For the scalar radial geometry, the invariant sector is precisely the already-known zero Mellin/net-flux coordinate, so positivity squares `Lambda` and misses the finite Weil coefficient. A surviving route must therefore do something structurally different: keep mixed shells active through an indefinite or global finite--archimedean assembly before final positivity; derive a non-translation-unitary source topology for a geometric reason; introduce extra non-radial invariant multiplicity with genuine arithmetic content; or create the required finite-prime incidence before radial projection.

No Gamma/polar completion or independent global sign theorem is produced here. The result is a decisive negative that removes the remaining singular-spectral version of the exact-nullity radial escape while preserving the zero-mode and sparse-scale controls that show the theorem's boundary exactly.