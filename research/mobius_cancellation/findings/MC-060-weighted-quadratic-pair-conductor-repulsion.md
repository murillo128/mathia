# MC-060 — Two weighted approximate quadratic prefixes cannot both have subquadratic conductor

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `X>=2`. Let `q_1 != q_2` be odd primes larger than `X`, and let

\[
\chi_i(n)=\left(\frac{n}{q_i}\right)
\qquad(i=1,2)
\]

be their primitive quadratic characters. Measure approximate agreement with the Möbius prime sign by

\[
A_X(\chi_i)
:=
\sum_{p\le X}\frac{|1+\chi_i(p)|}{p-1}.
\tag{1}
\]

Suppose that for some fixed `eta in (0,1]`,

\[
\boxed{
A_X(\chi_1)+A_X(\chi_2)\le 1-\eta.
}
\tag{2}
\]

Put

\[
Q=q_1q_2,
\qquad
\psi=\chi_1\chi_2.
\tag{3}
\]

Then `psi` is a primitive nonprincipal quadratic character modulo the square-free conductor `Q`, and its initial character sum has a fixed linear component:

\[
\boxed{
\left|\sum_{n\le X}\psi(n)\right|\ge \eta X.
}
\tag{4}
\]

Consequently the classical Burgess character-sum estimate gives, for every fixed `delta>0`,

\[
\boxed{
q_1q_2\gg_{\eta,\delta}X^{4-\delta}.
}
\tag{5}
\]

In particular, if both approximate interpolants satisfy the common bound

\[
A_X(\chi_i)\le c<\frac12,
\tag{6}
\]

then, with `eta=1-2c`, every distinct pair obeys `(5)`. Therefore for every fixed `epsilon>0` and sufficiently large `X`, **at most one** member of such a family can have conductor

\[
q_i\le X^{2-\varepsilon}.
\tag{7}
\]

This closes the most direct weighted-approximate analogue of the pairwise exact-prefix escape in `MC-056`. Exact agreement is not load-bearing for the near-quartic **pairwise** conductor barrier: a fixed generator-weighted phase budget already forces the quotient/product character to remain principal-like on a positive fraction of the whole integer prefix.

No estimate for `M(X)` follows. The result is an unconditional complexity obstruction for a specific moving quadratic-character comparator class.

## 1. Two approximate Möbius prime laws make the product character approximately principal

For every prime `p<=X`, both characters have modulus one because `q_i>X`. The elementary identity

\[
1-\chi_1(p)\chi_2(p)
=
(1+\chi_1(p))-\chi_1(p)(1+\chi_2(p))
\]

gives

\[
|1-\psi(p)|
\le
|1+\chi_1(p)|+|1+\chi_2(p)|.
\tag{8}
\]

Define the principal-phase defect

\[
B_X(\psi)
:=
\sum_{p\le X}\frac{|1-\psi(p)|}{p-1}.
\tag{9}
\]

Equations `(1)`, `(2)`, and `(8)` imply

\[
\boxed{B_X(\psi)\le1-\eta.}
\tag{10}
\]

This is the quadratic pairwise counterpart of the squared-phase defect in `MC-059`. There, a single higher-order character can be squared without becoming principal; here a single quadratic character cannot be treated that way, but the product of **two distinct** quadratic characters is again nonprincipal and removes their common Möbius sign approximately.

The distinction is essential. If `q_1=q_2`, then `psi=chi_1^2` is principal away from the conductor and Burgess supplies no obstruction. The theorem constrains the coexistence of two distinct approximate certificates.

## 2. The prime defect controls the whole integer prefix

For any integer `n<=X`, write

\[
n=\prod_p p^{v_p(n)}.
\]

Since neither conductor prime can divide such an `n`, every factor `psi(p)` appearing below has modulus one. Repeated use of

\[
|1-zw|\le |1-z|+|1-w|
\qquad(|z|=|w|=1)
\]

gives

\[
|1-\psi(n)|
\le
\sum_p v_p(n)|1-\psi(p)|.
\tag{11}
\]

Summing over `n<=X` and exchanging finite sums yields

\[
\begin{aligned}
\sum_{n\le X}|1-\psi(n)|
&\le
\sum_{p\le X}|1-\psi(p)|
\sum_{n\le X}v_p(n)\\
&=
\sum_{p\le X}|1-\psi(p)|
\sum_{j\ge1}\left\lfloor\frac{X}{p^j}\right\rfloor\\
&\le
X\sum_{p\le X}\frac{|1-\psi(p)|}{p-1}.
\end{aligned}
\tag{12}
\]

Together with `(10)`,

\[
\boxed{
\sum_{n\le X}|1-\psi(n)|\le(1-\eta)X.
}
\tag{13}
\]

The weight `1/(p-1)` is therefore not an arbitrary substitute for the usual pretentious weight `1/p`: it is exactly the elementary upper bound for how many prime-generator occurrences must be propagated when one lifts prime-phase discrepancies to all factorizations in the prefix.

## 3. A fixed residual principal component forces a large character sum

Write

\[
\sum_{n\le X}\psi(n)
=
X-
\sum_{n\le X}(1-\psi(n)).
\]

The reverse triangle inequality and `(13)` give

\[
\begin{aligned}
\left|\sum_{n\le X}\psi(n)\right|
&\ge
X-
\sum_{n\le X}|1-\psi(n)|\\
&\ge
\eta X,
\end{aligned}
\]

which proves `(4)`.

This step does not assume that either character agrees exactly with Möbius on any prime. Many mismatches are allowed, provided their generator-weighted total remains below the fixed threshold in `(2)`. It is likewise distribution-free: no independence of prime values, no random-character heuristic, and no statement about the density of mismatches is used.

Condition `(2)` is sufficient, not necessary. Once the total defect reaches one, this particular `L^1` transfer no longer guarantees a linear product-character sum; cancellations among the defects may still leave one, but a different argument would be required.

## 4. Burgess turns pairwise phase coherence into a conductor product floor

Because `q_1` and `q_2` are distinct primes, their primitive quadratic characters have coprime conductors. Their product `psi` is therefore primitive modulo

\[
Q=q_1q_2
\]

and nonprincipal. The modulus is square-free, hence cubefree, so the arbitrary-fixed-parameter Burgess estimate anchored by `MC-S34` applies:

\[
\left|\sum_{n\le X}\psi(n)\right|
\ll_{r,\varepsilon}
X^{1-1/r}
Q^{(r+1)/(4r^2)+\varepsilon}
\tag{14}
\]

for every fixed integer `r>=1` and every `epsilon>0`.

Combining `(4)` and `(14)` gives

\[
\eta X^{1/r}
\ll_{r,\varepsilon}
Q^{(r+1)/(4r^2)+\varepsilon}.
\tag{15}
\]

For fixed `r`, taking the Burgess epsilon arbitrarily small makes the resulting exponent of `X` in the conductor lower bound arbitrarily close to

\[
\frac{4r}{r+1}.
\]

Given `delta>0`, choose `r` sufficiently large that this exceeds `4-delta/2`, and then choose the Burgess epsilon sufficiently small to absorb the remaining exponent loss. The fixed factor `eta` is absorbed into the implied constant. This proves `(5)`.

Under `(6)`, equation `(2)` holds with `eta=1-2c>0`, so the pairwise bound is uniform for the class. If two distinct conductors both satisfied `(7)`, then

\[
q_1q_2\le X^{4-2\varepsilon},
\]

contradicting `(5)` with any `delta<2epsilon` for large `X`. Hence the at-most-one conclusion follows.

## 5. Relation to MC-056, MC-057, and MC-059

`MC-056` proved the exact pairwise version: when both quadratic characters equal `-1` on every prime through `X`, their product is identically `1` on every integer through `X`, so Burgess gives the same near-quartic product-conductor exponent. The present result shows that the exact prefix can be replaced by a quantitative weighted neighborhood of the Möbius prime law without changing that exponent.

For **exact** prime-quadratic interpolants, `MC-057` is stronger: classical least-prime-quadratic-residue theory already forces each individual conductor to exceed a constant multiple of `X^2`. The present theorem is useful precisely where that least-residue argument disappears—approximate interpolation may contain small quadratic residues, so there need not be a residue-free initial prime interval.

`MC-059` closes the corresponding higher-order approximate route for a **single** character. There `chi^2` remains nonprincipal and a weighted squared-phase defect directly triggers Burgess. Quadratic characters are the exceptional order because squaring destroys the character. The pair construction here supplies the missing replacement: two distinct quadratic approximate certificates produce a nonprincipal product character and inherit the same generator-to-prefix transfer.

The resulting order picture is therefore sharper than after `MC-059`:

- higher-order prime characters with small weighted Möbius-phase defect are individually forced into `q=X^{4-o(1)}` conductor;
- quadratic characters evade that one-object squaring argument, but two distinct certificates in the same fixed weighted neighborhood cannot both lie below the `X^{2-o(1)}` conductor scale;
- one isolated approximate quadratic certificate remains logically possible and is **not** ruled out by this finding.

That last survivor is the correct boundary. Promoting the pairwise obstruction into an individual approximate-quadratic conductor theorem would require genuinely new input.

## 6. Prior art and novelty boundary

The analytic engine is classical Burgess theory, already anchored by `MC-S34` (Treviño's modern statement). The conceptual fact that multiplicative functions close to a common target have a product/quotient close to the principal function is standard pretentious-number-theory language; `MC-S5` supplies the line's existing modern pretentious-distance anchor. Large-character-sum and character-repulsion literature likewise studies the rigidity of nonprincipal characters that remain principal-like for long ranges.

The proof above does not claim a new character-sum theorem. The prime-to-integer inequality `(12)` is the same elementary multiplicative telescoping mechanism used in `MC-059`, now applied to the product of two quadratic certificates; Burgess then supplies the global complexity obstruction. A targeted audit around pairs of close Dirichlet characters, pretentious repulsion, and large character sums found this established surrounding mechanism and no basis for a standalone novelty claim.

The retained Mathia-specific value is the exact specialization to the approximate Möbius-prefix comparator frontier left open by `MC-057` and `MC-059`, together with the explicit `1/(p-1)` generator budget and the resulting at-most-one low-conductor falsification rule.

## 7. Boundaries and falsification tests

The conclusion is deliberately narrow.

- It requires **two distinct** prime-conductor quadratic characters. It does not constrain a single approximate quadratic certificate.
- It assumes both conductors exceed `X`, so no conductor zero occurs inside the observed prefix and the comparison really is between unit-modulus prime phases.
- The defect threshold must leave a fixed gap below one. If `A_X(chi_1)+A_X(chi_2)` approaches or exceeds one, the present `L^1` argument supplies no linear character-sum lower bound.
- The result constrains conductor complexity, not the partial sums of `mu^2 chi_i` and not `M(X)` itself.
- The `X^{4-o(1)}` product exponent comes from direct Burgess and is not asserted sharp. Exact agreement permits the stronger individual least-residue information of `MC-057`.
- A family may still contain one exceptionally low-conductor approximate quadratic certificate at a given scale. Showing that such a certificate cannot persist coherently across scales is a separate problem.

The claim is falsified if the product of distinct primitive quadratic characters of prime conductors fails to be primitive/nonprincipal modulo `q_1q_2`, if `(12)` fails under the stated unit-modulus prefix hypotheses, or if the cubefree Burgess estimate cannot be applied with arbitrary fixed `r`. These are all explicit, auditable steps.

## Consequence for the active frontier

The moving-character escape is now narrowed on both sides of the order dichotomy. Higher-order approximate certificates already pay a near-quartic individual conductor cost (`MC-059`); quadratic approximate certificates can avoid that one-object argument, but a fixed weighted Möbius neighborhood contains **at most one** subquadratic prime-conductor certificate at each sufficiently large observation scale.

A surviving quadratic-comparator bootstrap must therefore exploit the identity and evolution of that one possible certificate, not merely the existence of many interchangeable local fits. The next nontrivial question is whether a single approximate quadratic character can remain sufficiently close to the Möbius prime law over a long nested range of scales while retaining conductor dependence strong enough to give useful cancellation at those same scales. Any such proposal must still pass the uniformity and global-boundary obstructions of `MC-049`–`MC-055`; pairwise replacement alone no longer supplies an escape.