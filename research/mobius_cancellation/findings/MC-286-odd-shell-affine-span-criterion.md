# MC-286 — Odd shell rows are exactly an affine-span problem

**Status:** `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the projected shell setup of `MC-285`. Identify each occupied sign pattern in `{±1}^d` with a vector in `F_2^d` by writing

\[
v_p(r)=(-1)^{w_p(r)},
\qquad
w_U(r)=(w_p(r))_{p\in U}\in\mathbf F_2^d.
\]

Let

\[
S=\{w_U(r):r\in\mathcal R_y\}\subset\mathbf F_2^d
\]

be the set of distinct occupied projected cells, and let `n_s` be the shell multiplicity of `s∈S`.

There exists an odd-cardinality set of **distinct shell primes** whose projected product is the all-positive endpoint if and only if

\[
0\in\operatorname{aff}_{\mathbf F_2}(S).
\]

Equivalently, there is no nonzero linear functional `λ∈(F_2^d)^*` such that

\[
\lambda(s)=1
\qquad\text{for every }s\in S.
\]

Thus the affine-hyperplane obstruction exhibited in `MC-285` is not merely one possible obstruction: at the support level it is the **only** obstruction to an odd projected endpoint row.

For a prescribed odd shell weight `t`, the exact multiplicity condition is the following. Such a row exists if and only if there is an odd-cardinality zero-sum subset `B⊂S` with `|B|≤t` and

\[
P_B:=\sum_{s\in S}\left\lfloor\frac{n_s-1_B(s)}2\right\rfloor
\ge \frac{t-|B|}{2}.
\]

The set `B` is the odd parity nucleus; all remaining selected primes can be added in equal-pattern pairs.

## Support-level equivalence

An odd-cardinality zero-sum subset `B⊂S` is exactly an affine representation of the origin over `F_2`. Indeed, its indicator coefficients satisfy

\[
\sum_{s\in S}1_B(s)=1,
\qquad
\sum_{s\in S}1_B(s)s=0
\]

in `F_2`. Conversely, any affine representation of `0` has coefficients in `{0,1}` whose support has odd cardinality and sums to zero.

This proves

\[
\exists\ B\subset S:\ |B|\text{ odd},\ \sum_{s\in B}s=0
\quad\Longleftrightarrow\quad
0\in\operatorname{aff}(S).
\]

For the dual formulation, if `0` does not lie in the affine hull, write that hull as `a+V` with `a∉V`. Linear algebra over `F_2` gives a functional `λ` vanishing on `V` and satisfying `λ(a)=1`; hence `λ=1` on all of `S`. The converse is immediate because a functional equal to `1` on all generators is also `1` on their affine hull and therefore excludes the origin.

A minimal odd zero-sum subset is a circuit of the associated binary vector matroid: any proper zero-sum subset would leave either itself or its complement as a smaller odd zero-sum subset. Consequently one may always choose such a nucleus with

\[
|B|\le d+1.
\]

This last statement also follows directly by choosing an affinely independent subfamily spanning the origin.

## Exact prescribed-weight criterion

Suppose a shell row selects `m_s` primes from cell `s`, with `0≤m_s≤n_s`. Its projected sum is determined only by the parity support

\[
B=\{s:m_s\equiv1\pmod2\}.
\]

When `t=\sum_s m_s` is odd, `|B|` is odd. The endpoint condition is precisely

\[
\sum_{s\in B}s=0.
\]

After reserving one selected prime in each cell of `B`, every remaining selected prime must occur in same-cell pairs. Cell `s` supplies at most

\[
\left\lfloor\frac{n_s-1_B(s)}2\right\rfloor
\]

such pairs. Therefore a row of exact size `t` exists exactly when the total pair capacity is at least `(t-|B|)/2`, which proves the stated necessary-and-sufficient criterion.

This separates two issues that were conflated at the end of `MC-285`: **support geometry** decides whether any odd endpoint row can exist, while **cell multiplicities** decide which prescribed odd cardinalities can be reached once an odd nucleus exists.

## A coarse finite-size sufficient condition

Let

\[
N=\sum_{s\in S}n_s,
\qquad K=|S|,
\qquad k=|B|.
\]

Before reserving the nucleus, the shell contains at least `(N-K)/2` disjoint same-cell pairs. Reserving one prime from each of the `k` nucleus cells destroys at most one available pair per cell, so

\[
P_B\ge \frac{N-K}{2}-k.
\]

Hence the exact capacity condition certainly holds whenever

\[
N-K\ge t+k.
\]

Since a minimal odd nucleus can be chosen with `k≤d+1`, the support condition `0∈aff(S)` together with

\[
N-K\ge t+d+1
\]

is a simple sufficient finite criterion for an odd endpoint row of size `t`. This bound is intentionally conservative; unlike the formula for `P_B`, it is not claimed to be necessary.

## Product-character translation

For a nonempty coordinate subset `J⊂U`, let `λ_J` be its indicator functional and define the corresponding product of quadratic signs by

\[
\chi_J(r)=\prod_{p\in J}\left(\frac p r\right)
          =(-1)^{\lambda_J(w_U(r))}.
\]

The affine obstruction `λ_J(s)=1` for every occupied pattern is therefore exactly the statement

\[
\chi_J(r)=-1
\qquad\text{for every }r\in\mathcal R_y.
\]

Consequently

\[
0\in\operatorname{aff}(S)
\]

is equivalent to the following source-native condition: for every nonzero coordinate functional, or equivalently every nonempty generated product-character direction, **some shell prime has product sign `+1`**.

This is strictly weaker as a finite pattern requirement than the full Boolean pattern realization used in `MC-284`. Full realization certainly implies the criterion, but one all-positive cell, one three-cell odd relation, or any other odd zero-sum nucleus already suffices. The reduction does not by itself prove that the weaker requirement is analytically easier uniformly as `d` and the conductors grow.

## Relation to the existing frontier

`MC-285` proved that even shell weights need only equal-cell pairing and isolated affine concentration as the obstruction that survives for odd weights. The present result closes the finite-combinatorial side of that parity split: affine concentration is exactly the support-level obstruction, and the multiplicity formula above gives the exact extra condition for a prescribed odd weight.

`MC-284` remains a valid sufficient route because realizing every Boolean pattern forces `0∈S`. It is, however, stronger than necessary for the odd-row Christoffel obstruction. Future arithmetic work can target the weaker dual statement that no nontrivial product-character direction stays identically negative throughout the shell, or can directly force a bounded odd zero-sum nucleus.

For the endpoint-normalized empirical Christoffel problem of `MC-281`, any such odd row again evaluates the supported polynomial at its endpoint value `1`, so the same one-row energy obstruction applies. What remains is arithmetic: prove the required affine-span/nonconstancy statement in a support and conductor regime large enough to matter.

## Prior-art and novelty audit

The equivalence between absence of odd circuits and affine structure is classical binary-matroid theory. A standard formulation is that a loopless binary matroid is affine if and only if it has no odd circuit; the same mechanism appears throughout the literature on affine/bipartite binary matroids. See, for example, James Oxley and Kristen Wetzler, *The binary matroids whose only odd circuits are triangles*, Advances in Applied Mathematics 76 (2016), 34–38, DOI `10.1016/j.aam.2016.01.006`, and standard matroid-theory treatments of affine binary matroids.

No novelty is claimed for that finite-geometric equivalence. The useful research contribution here is its exact specialization to the parity obstruction left open by `MC-285`, the necessary-and-sufficient occupancy formula for a prescribed odd shell size, and the translation of the obstruction into constant-negative generated quadratic-character directions. Those statements refine the current Mathia frontier; they are not a new theorem about Möbius summatory cancellation or RH.

## Boundaries

- This does not improve any unconditional bound for `M(x)` and does not prove or imply RH.
- `0∈aff(S)` is necessary and sufficient for existence of **some** odd projected endpoint row, not by itself for a row of every prescribed odd size.
- The `P_B` condition is the exact fixed-size criterion; `N-K≥t+d+1` is only a convenient sufficient bound.
- Full pattern realization remains useful for stronger objectives; the claim here is only that it is unnecessary for existence of one odd endpoint row.
- Rephrasing the dual obstruction as product-character nonconstancy does not supply the required character estimate. In particular, exponentially many generated directions may still make a uniform arithmetic proof difficult.
- The matroid terminology is prior art. The line-specific content is the shell/occupancy/character specialization and the resulting narrowing of the live frontier.

## Decisive test and next frontier

For any proposed odd-weight endpoint-normalized empirical-energy `<1` certificate, form the occupied projected pattern set `S` on the coordinates actually used by the certificate.

If `0∈aff(S)` and the exact pair-capacity inequality holds for the target odd weight `t`, the certificate is killed by an explicit projected endpoint row. Therefore the next source-native arithmetic question is sharply reduced to whether the actual quadratic-character shell can sustain

\[
\chi_J(r)=-1\quad\text{for all shell primes }r
\]

for some nontrivial generated product character `χ_J` in the growing-support regime, or whether available prime-character estimates can rule out every such affine obstruction before the Christoffel support size becomes too large.