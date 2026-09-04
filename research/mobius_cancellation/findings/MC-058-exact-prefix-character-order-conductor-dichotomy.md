# MC-058 — Higher-order exact-prefix characters pay a super-sixth-power conductor cost

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `PRIOR-ART-CORRECTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `X>=2`. Let `q>X` be prime and let `chi` be a nonprincipal Dirichlet character modulo `q` satisfying

\[
\chi(p)=-1
\qquad\text{for every prime }p\le X.
\tag{1}
\]

Then the square-free-supported comparator

\[
f(n)=\mu(n)^2\chi(n)
\]

agrees exactly with Möbius throughout the observed prefix:

\[
f(n)=\mu(n)
\qquad(1\le n\le X).
\tag{2}
\]

If `chi` is quadratic, `MC-057` already gives the eventually quadratic conductor floor `q>3X^2`, with the stronger `q>4X^2+1` in the `q≡5 (mod 8)` branch used by `MC-055`.

If instead `chi` has order strictly larger than `2`, the conductor cost is much stronger. The value `-1` in `(1)` forces `ord(chi)` to be even. Put

\[
\psi=\chi^2,
\qquad
k=\operatorname{ord}(\psi)=\frac{\operatorname{ord}(\chi)}2>1.
\tag{3}
\]

Then `psi` is a nonprincipal character modulo the same prime `q` and

\[
\boxed{\psi(n)=1\qquad(1\le n\le X).}
\tag{4}
\]

Its kernel is exactly the subgroup of `k`-th powers in `(Z/qZ)^*`. Hence the least `k`-th power non-residue `g(q,k)` satisfies

\[
\boxed{g(q,k)>X.}
\tag{5}
\]

The classical Burgess least-power-nonresidue theorem, recorded in `MC-S34`, states uniformly for `k>1` dividing `q-1` that

\[
g(q,k)\ll_\varepsilon q^{1/(4\sqrt e)+\varepsilon}.
\tag{6}
\]

Consequently, for every fixed `delta>0`,

\[
\boxed{
q\gg_\delta X^{4\sqrt e-\delta}
}
\qquad
\left(4\sqrt e\approx6.594885\right).
\tag{7}
\]

Treviño's explicit theorem in the same source gives an unconditional finite-threshold version: for every prime `q>=10^4732` and every `k>1` dividing `q-1`,

\[
g(q,k)\le q^{1/6},
\]

so any higher-order exact-prefix interpolant in that range obeys

\[
\boxed{q>X^6.}
\tag{8}
\]

Thus replacing the quadratic characters of `MC-055` by higher-order complex Dirichlet characters does not relax the moving-comparator complexity barrier. Once exact agreement with the Möbius prime signs is imposed, squaring the character exposes a classical least-power-nonresidue obstruction and forces a conductor far beyond the observation scale.

No estimate for `M(X)` follows. This is a complexity obstruction for one exact-prefix interpolation class, assembled from classical character theory and Burgess prior art.

## 1. Exact Möbius-prefix agreement does not require quadraticity

Take any `n<=X`. Since `q>X`, the integer `n` is coprime to the conductor. If `n` is not square-free, both `f(n)` and `mu(n)` vanish. If

\[
n=p_1\cdots p_r
\]

is square-free, every `p_j<=X`, so `(1)` and complete multiplicativity give

\[
\chi(n)=\prod_{j=1}^r\chi(p_j)=(-1)^r=\mu(n).
\]

Since `mu(n)^2=1` on square-free integers, `(2)` follows.

The finite-prefix phenomenon isolated in `MC-055` is therefore not intrinsically quadratic: any Dirichlet character that takes the value `-1` on all observed primes produces the same exact local comparator. What changes with character order is the arithmetic price of sustaining that prefix.

## 2. Higher character order turns the observed prefix into a principal prefix

Let `r=ord(chi)>2`. Because `chi(p)=-1` for at least the prime `2`, the image of `chi` contains an element of order two. Hence `r` is even. The squared character `psi=chi^2` has order

\[
k=r/\gcd(r,2)=r/2>1,
\]

so it is nonprincipal. Since the modulus is prime, every nonprincipal character modulo `q` is primitive.

For every observed prime,

\[
\psi(p)=\chi(p)^2=1.
\]

Complete multiplicativity then gives `(4)` for every integer `n<=X`.

This is the key asymmetry with the quadratic case. If `ord(chi)=2`, squaring makes `chi^2` principal globally and no nonprincipal least-nonresidue theorem remains. For every higher even order, however, squaring removes the Möbius sign on the observed prefix while leaving a genuinely nonprincipal character globally.

## 3. The kernel of `psi` is the `k`-th-power subgroup

The multiplicative group

\[
G=(\mathbb Z/q\mathbb Z)^*
\]

is cyclic of order `q-1`. A character of exact order `k` has kernel of index `k`, hence of size `(q-1)/k`.

Because `k|q-1`, the subgroup of `k`-th powers

\[
G^k=\{a^k:a\in G\}
\]

also has size `(q-1)/k`. A cyclic group has a unique subgroup of each divisor order, so

\[
\ker\psi=G^k.
\tag{9}
\]

Therefore an integer `m` coprime to `q` is a `k`-th power residue exactly when `psi(m)=1`. Equation `(4)` says every positive integer through `X` is a `k`-th power residue. By definition of the least `k`-th power non-residue, `(5)` follows.

This step is exact and contains no analytic estimate, no zeta information, and no probabilistic interpretation.

## 4. Burgess converts the principal prefix into a conductor floor

Treviño's `MC-S34` summarizes the classical unconditional Burgess result for the least `k`-th power non-residue, uniformly over `k>1` dividing `q-1`:

\[
g(q,k)\ll_\varepsilon q^{a+\varepsilon},
\qquad
a=\frac1{4\sqrt e}.
\]

Combining this with `(5)` gives

\[
X < g(q,k)\ll_\varepsilon q^{a+\varepsilon}.
\tag{10}
\]

Fix `delta>0`. Choose `epsilon>0` small enough that

\[
\frac1{a+\varepsilon}>4\sqrt e-\frac\delta2.
\]

Equation `(10)` gives

\[
q\gg_\varepsilon X^{1/(a+\varepsilon)}.
\]

After weakening the exponent slightly to absorb the fixed implied constant for sufficiently large `X`, this yields `(7)`; enlarging the constant handles the remaining finite range. Thus the useful invariant statement is

\[
q\gg_\delta X^{4\sqrt e-\delta}
\qquad(\delta>0).
\]

The same source provides the explicit all-order theorem

\[
g(q,k)\le q^{1/6}
\qquad(q\ge10^{4732}),
\]

which combined with `(5)` proves `(8)` without asymptotic implied constants.

## 5. Why direct Burgess summation misses part of the obstruction

There is a simpler but weaker argument. Since `psi(n)=1` throughout `[1,X]`,

\[
\sum_{n\le X}\psi(n)=X.
\]

Applying the ordinary Burgess character-sum estimate exactly as in `MC-056` would force only

\[
q\gg_\delta X^{4-\delta}.
\]

The least-power-nonresidue theorem is stronger because its classical proof does more than test the raw initial sum: Burgess's character-sum input is combined with multiplicative/smooth-number amplification. The resulting threshold `1/(4sqrt(e))` replaces the raw `1/4` barrier.

For this exact-prefix problem, that distinction matters. The observed condition is not merely a large character sum; it says the entire initial multiplicative semigroup generated by the small primes lies in one character kernel. Least-power-nonresidue theory is therefore the natural prior art, and the direct `X^{4-o(1)}` character-sum estimate understates the conductor cost.

## 6. Order dichotomy for prime-conductor exact-prefix characters

The current exact-prefix character frontier now separates cleanly by order.

For order `2`, the squared character becomes principal, so the least-nonresidue route above disappears. `MC-057` instead exploits the opposite fact that every observed prime is a quadratic **nonresidue** for `chi`; least-prime-quadratic-residue and class-number results then force a quadratic conductor floor.

For order greater than `2`, squaring leaves a nonprincipal character and turns every observed prime into a **residue** for `psi`. This puts the whole observed integer prefix inside a proper power-residue subgroup and triggers `(7)`.

Thus complex/higher-order phase freedom does not supply a cheap escape from the quadratic matched control. It changes which classical obstruction detects the interpolation, and in the higher-order case the currently available unconditional exponent is substantially stronger.

## 7. Prior art and novelty boundary

The analytic estimate in this finding is classical prior art. `MC-S34` is Enrique Treviño, *The Burgess inequality and the least k-th power non-residue*, International Journal of Number Theory 11 (2015), 1653–1678, DOI `10.1142/S1793042115400163`, arXiv `1412.3062`. Its introduction records the Burgess bound `(6)` for general `k`, and Theorem 3 gives the explicit `p^(1/6)` result for every `k>1` dividing `p-1`; Remark 2 states that the method reaches every exponent above `1/(4sqrt(e))`.

The older smooth-number amplification behind least power nonresidues goes back through Burgess and Norton; Norton's monograph *Numbers with Small Prime Factors, and the Least kth Power Non-Residue*, Memoirs AMS 106 (1971), is direct historical prior art for that mechanism.

A targeted search for Dirichlet characters prescribed to equal `-1` on an initial prime set found the expected neighboring finite-interpolation and character-correlation discussions, while the least-power-nonresidue literature already supplies the decisive global restriction after squaring. No standalone novelty claim is justified. The Mathia-specific contribution is the exact reduction from a higher-order Möbius-prefix comparator to that classical least-power-nonresidue boundary and the resulting order dichotomy with `MC-057`.

## 8. Boundary and surviving route

This finding does not prove that higher-order exact-prefix characters exist with conductors near the lower bound, nor does it rule out all scale-dependent multiplicative comparators. It says that **if** a prime-conductor Dirichlet character reproduces the Möbius sign at every observed prime, then higher character order cannot make the certificate low-complexity.

The result also does not transfer the conductor lower bound into a lower bound for the true comparator partial sum; it constrains the arithmetic resource required to manufacture exact local agreement.

A surviving character-based comparator strategy would therefore have to relax at least one load-bearing feature: exact agreement at every prime through `X`, prime-conductor Dirichlet-character structure, or dependence on a single character kernel. Approximate or weighted agreement remains logically open, but any such relaxation must be audited against the earlier pretentiousness, boundary-zero, and uniformity obstructions rather than treated as an automatic escape.