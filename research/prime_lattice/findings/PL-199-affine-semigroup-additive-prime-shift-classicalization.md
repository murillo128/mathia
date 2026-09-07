# PL-199 — Canonical addition turns prime shifts into the classical affine semigroup, whose standard zeta thermodynamics is pole-driven

## Claim

A canonical way to escape the flat commuting-prime-shift obstructions of `PL-197` and `PL-198` is to add ordinary integer translation to multiplication. This does produce a genuinely relational, noncommutative source action, but that action is already classical prior art: it closes exactly to the affine semigroup `N ⋊ N^×` studied by Cuntz and by Laca–Raeburn.

On `ell^2(N_0)` let

\[
S e_k=e_{k+1},\qquad V_n e_k=e_{nk}\quad(n\ge 1).
\]

Then

\[
V_mV_n=V_{mn},\qquad V_nS=S^nV_n,
\]

and unique factorization gives

\[
V_n=\prod_p V_p^{v_p(n)}.
\]

Thus the prime-exponent coordinate shifts, when coupled to the canonical successor `S`, generate the affine maps

\[
k\longmapsto a+mk,
\]

with multiplication law

\[
(a,m)(b,n)=(a+mb,mn).
\]

This is precisely the semidirect-product semigroup `N ⋊ N^×`. Cuntz constructed the associated boundary `C*`-algebra `Q_N` and explicitly described it as the Bost–Connes algebra enriched by one unitary generator corresponding to addition. Laca and Raeburn then showed that the Toeplitz algebra `T(N ⋊ N^×)` is the universal Nica-covariant isometric completion of the affine semigroup and that `Q_N` is its boundary quotient.

The natural KMS dynamics of this classical affine-semigroup completion does not supply a Riemann-critical-line selector. Laca–Raeburn prove that there is a unique `KMS_beta` state for `1 <= beta <= 2`, a phase transition at `beta=2`, and a family of states for `beta>2`; in the extremal low-temperature GNS representations the Liouville operator has eigenvalue `log x` with multiplicity `x`, hence

\[
\operatorname{Tr}(e^{-\beta H})
 =\sum_{x\ge1}x\,x^{-\beta}
 =\zeta(\beta-1)
\]

in its ordinary trace-class region `beta>2`. The authors explicitly associate the phase transition at `beta=2` with the pole of this shifted partition function. The shifted Riemann critical line would instead be `Re(beta)=3/2`; on the real-temperature axis this lies strictly inside the single unique-KMS regime `1 <= beta <= 2` and outside the ordinary trace-class region. Meromorphically replacing the divergent trace there by the continued scalar `zeta(beta-1)` would import analytic continuation rather than derive the zero divisor from the semigroup dynamics.

Therefore the route

\[
\text{prime multiplication}+\text{ordinary successor}
\longrightarrow
\text{affine-semigroup operator algebra/KMS dynamics}
\longrightarrow
\text{RH zero localization}
\]

is not an unexplored relational prime-lattice mechanism. The first arrow is classical and genuinely arithmetic, while the standard second-stage thermodynamic invariant remains controlled by the zeta pole rather than by a mechanism forcing the nontrivial zeros onto `Re(s)=1/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/NEGATIVE-OBSTRUCTION`.

The negative is deliberately restricted to the raw affine-semigroup relations and their standard natural KMS completion. It does not rule out target-relative compressions, different observables, completed trace formulas, or additional Möbius/Weil/Nyman structure inside or around an affine-semigroup algebra.

## 1. Exact affine closure of the prime-coordinate shifts

The prime-exponent representation gives commuting multiplicative isometries

\[
V_p:e_k\mapsto e_{pk},
\]

and therefore

\[
V_n=\prod_pV_p^{v_p(n)}.
\]

Adding the canonical integer successor `S:e_k -> e_(k+1)` introduces a relation which cannot be gauged into independent prime phases:

\[
V_nSe_k=e_{n(k+1)}=e_{nk+n}=S^nV_ne_k.
\]

Consequently

\[
V_nS=S^nV_n.
\]

For `a >= 0` and `m >= 1`, the composite `S^aV_m` acts by

\[
S^aV_me_k=e_{a+mk}.
\]

Using `V_mS^b=S^{mb}V_m`,

\[
(S^aV_m)(S^bV_n)
 =S^{a+mb}V_{mn},
\]

which is exactly the affine-semigroup multiplication

\[
(a,m)(b,n)=(a+mb,mn).
\]

This is a stronger relational structure than the flat prime connection of `PL-197` or the common-intertwiner setup of `PL-198`: the additive generator does not commute with multiplication, and the exponent-lattice directions are tied to a distinguished rational-integer successor operation.

The conclusion does not depend on treating the concrete `ell^2(N_0)` representation as the universal Toeplitz representation. The exact algebraic point is only that the canonical generators close to `N ⋊ N^×`. Laca–Raeburn's universal Nica-covariant Toeplitz completion and Cuntz's boundary quotient are established operator-algebraic completions of that same affine semigroup.

## 2. The category exit is classical prior art

Joachim Cuntz, *C*-algebras associated with the `ax+b`-semigroup over `N`* (2008), constructs a `C*`-algebra naturally associated with this semigroup. The published abstract states that it can be obtained from the Bost–Connes algebra by adding one unitary generator corresponding to addition; its stabilization is described by a crossed product involving the finite adeles of `Q` and the rational affine group.

Marcelo Laca and Iain Raeburn, *Phase transition on the Toeplitz algebra of the affine semigroup over the natural numbers* (2010), prove that

\[
(Q\rtimes Q_+^*,\;N\rtimes N^\times)
\]

is quasi-lattice ordered, that `T(N ⋊ N^×)` is universal for Nica-covariant isometric representations, and that Cuntz's `Q_N` is the boundary quotient. Their natural dynamics fixes the additive generator and assigns the multiplicative generators their logarithmic energies, so the prime weights `log p` remain present in exactly the same sense as in the Bost–Connes/log-Hamiltonian picture of `PL-024`.

This makes the novelty boundary unusually sharp. `PL-024` classicalized the relation `[H,V_p]=(log p)V_p`; the present finding classicalizes the next obvious noncommutative repair, namely coupling those multiplicative directions to ordinary addition itself. The latter is not merely another scalar phase or commuting prime shift: it is the canonical rational-integer semiring relation, and it was already promoted to a full operator-algebraic dynamical system in the classical literature.

## 3. The standard thermodynamic singularity is still a pole boundary

Laca–Raeburn compute the KMS states of the natural dynamics for all inverse temperatures. Their main phase diagram is:

- no KMS states for `beta<1`;
- a unique KMS state for every `1 <= beta <= 2`;
- a phase transition at `beta=2`;
- for `beta>2`, KMS states parametrized by probability measures on the circle;
- the `beta=1` state factors through the quotient `Q_N`.

For an extremal `KMS_infinity` state, the dynamics is implemented in the corresponding GNS representation by a Liouville operator whose eigenvalues are `log x`, each with multiplicity `x`. Hence the ordinary Gibbs trace is

\[
\operatorname{Tr}(e^{-\beta H})
 =\sum_{x\ge1}x^{1-\beta}
 =\zeta(\beta-1),
\]

which converges exactly for `beta>2`. Laca–Raeburn explicitly call this the partition function and associate the finite-temperature phase transition with its pole at `beta=2`.

This is the correct analytic-continuation boundary for the present audit. The identity above is an ordinary operator trace only in the trace-class half-line `beta>2`. The meromorphic function `zeta(beta-1)` of course continues elsewhere, but at `beta=3/2` the operator trace diverges. The KMS state nevertheless exists there because KMS theory is not the same thing as analytic continuation of the Gibbs trace.

The formal shift of the Riemann critical line is

\[
\operatorname{Re}(\beta-1)=\tfrac12
\quad\Longleftrightarrow\quad
\operatorname{Re}\beta=\tfrac32.
\]

On the physical real axis, `beta=3/2` lies inside the same unique-KMS phase as every other `beta` in `[1,2]`; the published phase diagram has no transition or symmetry change there comparable to the pole-driven transition at `beta=2`. Thus the natural affine-semigroup thermodynamics does not turn the critical line into an intrinsic equilibrium boundary.

## 4. Why this is a stronger control than generic Beurling or flat-gauge objections

The affine relation is genuinely specific to ordinary integers. A generic Beurling prime system preserves a free multiplicative exponent monoid but does not automatically come with a discrete successor operation closed inside its generalized integers and satisfying

\[
V_nS=S^nV_n.
\]

So this negative cannot be dismissed as another deformation showing that the prime-lattice geometry is universal. It tests a canonical piece of rational-integer structure that generic free prime systems lack.

That specificity is exactly why the prior-art redirect matters. Even after adding ordinary addition — enough to escape the fully commuting/gauge-flat prime-shift category — the most standard operator-algebraic dynamical completion is already known, and its basic zeta-sensitive thermal invariant is organized around the pole of a shifted zeta function. Rational-integer specificity alone therefore does not produce the missing zero-localization principle.

## 5. Prior art and novelty audit

Primary anchors:

1. **Joachim Cuntz**, “C*-algebras associated with the `ax+b`-semigroup over `N`,” in *K-Theory and Noncommutative Geometry*, EMS Series of Congress Reports, European Mathematical Society, 2008, pp. 201–215. DOI: https://doi.org/10.4171/060-1/8.
   - Establishes the arithmetic `ax+b` `C*`-algebra `Q_N`; the published abstract explicitly relates it to Bost–Connes by adjoining a unitary addition generator and describes the finite-adelic crossed-product picture.
2. **Marcelo Laca, Iain Raeburn**, “Phase transition on the Toeplitz algebra of the affine semigroup over the natural numbers,” *Advances in Mathematics* **225**(2) (2010), 643–688. DOI: https://doi.org/10.1016/j.aim.2010.03.007. arXiv: https://arxiv.org/abs/0907.3760.
   - Establishes the quasi-lattice order, the universal Nica-covariant Toeplitz algebra, the boundary quotient `Q_N`, the natural dynamics, the complete KMS phase diagram, and the partition function `zeta(beta-1)` with phase transition at `beta=2`.

No novelty is claimed for the affine semigroup, its `C*`-algebras, the covariance relation, or the KMS theorem. The derived contribution to this research line is the identification that the exact category exit suggested by the post-`PL-198` frontier — add a canonical noncommuting integer relation to the prime shifts — lands immediately in this established theory, together with the analytic observation that its standard thermal transition is at the shifted zeta pole rather than at the shifted critical line.

A mechanism search around `ax+b`, `N ⋊ N^×`, Cuntz/Laca–Raeburn, zeta zeros, and RH did not produce a theorem in these primary affine-semigroup sources that derives zero localization from the raw semigroup relations or natural KMS dynamics alone. This is recorded only as a novelty boundary, not as a theorem that no other observable on these algebras could ever be RH-sensitive.

## 6. Boundary conditions and counterarguments

### The affine algebra is not being dismissed as arithmetically empty

It is substantially richer than the bare prime lattice: addition and multiplication interact noncommutatively, Cuntz's completion reaches finite-adèlic geometry, and the Toeplitz system has a nontrivial KMS phase structure. The negative concerns only the claim that this canonical enrichment itself supplies the missing Riemann-zero localization mechanism.

### `Q_N` and the Toeplitz algebra must not be conflated

In Cuntz's boundary quotient the addition generator is unitary. In the Laca–Raeburn Toeplitz algebra it is represented by an isometry, and `Q_N` is a boundary quotient. The concrete unilateral successor on `ell^2(N_0)` is used above only to derive the affine semigroup law, not to identify that concrete representation with `Q_N`.

### KMS continuation is not scalar analytic continuation

The existence of a `KMS_(3/2)` state does not make the divergent operator trace equal to the analytically continued number `zeta(1/2)`. Any construction that uses zeros of continued `zeta(beta-1)` below `beta=2` must exhibit an additional operator, boundary value, determinant, scattering object, or trace formula which genuinely survives there.

### Additional target-relative structure remains open

A compression tied to the Nyman target, a Möbius/parity observable, Weil positivity, an adelic trace formula, a nontrivial quotient modulo an ideal, or another completed mechanism can change the problem. Such a construction would no longer be a consequence of the raw affine-semigroup relations and must be audited on its own. The finding therefore narrows, rather than closes, the search for relational prime-shift actions.

## 7. Decisive audit tests

This finding should be withdrawn or materially narrowed if any of the following occurs:

1. the exact relation `V_nS=S^nV_n` fails to generate the affine semigroup law `(a,m)(b,n)=(a+mb,mn)` for the stated canonical operators;
2. `T(N ⋊ N^×)` is not the Laca–Raeburn universal Nica-covariant Toeplitz algebra or `Q_N` is not its stated boundary quotient;
3. the natural Laca–Raeburn dynamics has a distinct phase transition or symmetry-localization phenomenon at `beta=3/2` comparable to the one at `beta=2`;
4. the ordinary Liouville Gibbs trace in the cited extremal GNS representations is trace class at `beta<=2`, contrary to `sum_x x^(1-beta)`;
5. an established theorem derives Riemann-zero localization from the raw affine-semigroup relations and this natural KMS mechanism without importing an RH-equivalent target, analytically continued zeta divisor, or additional completed trace/positivity structure.

The first four tests are exact or directly covered by the cited literature. The fifth is the novelty boundary for future work.

## Consequence for the research line

The post-`PL-198` instruction to seek a genuinely relational prime-shift action remains correct, but **ordinary integer addition is no longer an unclassified escape**. Its canonical relation with multiplication is precisely the classical arithmetic `ax+b` semigroup, and its standard operator-algebraic thermodynamics singles out the shifted pole boundary `beta=2`, not the shifted critical line `Re(beta)=3/2`.

A surviving relational construction must therefore add a load-bearing ingredient beyond

\[
V_p\text{ prime shifts},\qquad S\text{ successor},\qquad V_pS=S^pV_p.
\]

In particular, the next useful mechanism must explain how a target-sensitive cancellation, completed Fourier/Weil structure, nontrivial compression, or other arithmetic observable couples to this rational-integer semiring relation in a way that cannot be reduced to the already-classical affine-semigroup KMS system.