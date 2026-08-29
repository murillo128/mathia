# WP-018 — Local Boolean energy supertrace recovers von Mangoldt, but the selector is not a positive form

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + NEGATIVE/OBSTRUCTION`. The exact selector below is the classical identity `Lambda = mu * log` written intrinsically on the Prime-Lattice exponent cone. The Mathia-specific value is that it resolves the support problem left open by WP-017 without an explicit axis projector or the `N^{-1}` normalization of WP-004: every exponent vector carries a canonical backward Boolean cube, and the graded trace of its positive residual-energy operator is exactly `Lambda(n)`. The decisive limitation is equally exact: the prime-power selector is produced by an **alternating supertrace**, not by positivity. Ordinary positive traces lose the selector, the construction has no archimedean/polar sector, and the same mechanism works for arbitrary weighted free commutative monoids and Beurling generalized primes.

## 1. Every exponent vector has a canonical backward Boolean cube

Let

\[
\alpha=v(n)=(v_p(n))_p\in\mathbb N_0^{(\mathbb P)},\qquad n\ge2,
\]

with support

\[
S(\alpha)=\{p:\alpha_p>0\},\qquad r=|S(\alpha)|,
\]

and intrinsic Prime-Lattice energy

\[
E(\alpha)=\sum_p\alpha_p\log p=\log n.
\]

For every subset `T subseteq S(alpha)`, write

\[
\mathbf 1_T=\sum_{p\in T}e_p.
\]

Because every coordinate in the support is at least one, all vectors

\[
\alpha-\mathbf 1_T
\]

remain in the exponent cone. Hence `alpha` canonically determines the finite backward Boolean cube

\[
C_\alpha=\{\alpha-\mathbf 1_T:T\subseteq S(\alpha)\}.
\]

No CW realization, metric choice, prime-power list, or analytic continuation is needed for this cube: it is forced by the coordinatewise order on the exponent lattice.

Put a one-dimensional basis vector `e_T` at each vertex and grade by parity of `|T|`:

\[
\mathcal H_\alpha
=\bigoplus_{T\subseteq S(\alpha)}\mathbb C e_T,
\qquad
\Gamma e_T=(-1)^{|T|}e_T.
\]

Define the residual-energy operator

\[
R_\alpha e_T
=E(\alpha-\mathbf 1_T)e_T.
\]

Since `E>=0` on the exponent cone,

\[
\boxed{R_\alpha\ge0.}
\]

Thus the full exponent lattice really does supply a canonical finite positive operator at every integer, including every proper prime power. This escapes the event-support obstruction of the square-free persistence object in WP-017.

## 2. Its supertrace is exactly the von Mangoldt function

The graded trace is

\[
\operatorname{Str}R_\alpha
=\sum_{T\subseteq S(\alpha)}(-1)^{|T|}
E(\alpha-\mathbf 1_T).
\tag{1}
\]

Using linearity of the logarithmic energy,

\[
E(\alpha-\mathbf 1_T)
=E(\alpha)-\sum_{p\in T}\log p.
\]

The constant contribution to (1) is

\[
E(\alpha)\sum_T(-1)^{|T|}
=E(\alpha)(1-1)^r=0.
\]

For a fixed `p in S(alpha)`,

\[
\sum_{T\ni p}(-1)^{|T|}
=-(1-1)^{r-1}.
\]

Therefore

\[
\operatorname{Str}R_\alpha
=\begin{cases}
\log p,&r=1,\\
0,&r\ge2.
\end{cases}
\tag{2}
\]

But `r=1` means precisely `n=p^k` for some `k>=1`. Hence

\[
\boxed{\operatorname{Str}R_{v(n)}=\Lambda(n).}
\tag{3}
\]

This also explains exactly why the exponent multiplicity `k` disappears. On the prime ray `alpha=k e_p`, the Boolean cube is only the edge

\[
k e_p\longleftrightarrow (k-1)e_p,
\]

and

\[
E(k e_p)-E((k-1)e_p)=\log p.
\]

So WP-004's division by occupation number `N^{-1}` is not the only intrinsic way to remove the factor `k`: the local backward finite difference removes it automatically.

Equivalently, if `tau_{-e_p}` denotes the backward coordinate shift wherever defined, then

\[
\boxed{
\left(\prod_{p\mid n}(I-\tau_{-e_p})\right)E(v(n))
=\Lambda(n).
}
\tag{4}
\]

For support size at least two this is a mixed finite difference of an affine-linear function and therefore vanishes. For support size one it is the first difference `log p`.

In divisor notation, (1) is exactly the classical Möbius-inversion identity

\[
\Lambda(n)
=\sum_{d\mid n}\mu(d)\log\frac nd
=(\mu*\log)(n),
\]

because square-free divisors `d` of `n` correspond to subsets of `S(alpha)` and `mu(d)=(-1)^{|T|}`. No novelty is claimed for this arithmetic identity.

## 3. Critical attenuation reproduces the entire WP-004 finite measure

Multiplying (3) by the intrinsic critical attenuation gives

\[
e^{-E(\alpha)/2}\operatorname{Str}R_\alpha
=\frac{\Lambda(n)}{\sqrt n}.
\tag{5}
\]

Hence the finite positive-location distribution can be written without an explicit axis projection as

\[
\boxed{
\sum_{\alpha\ne0}
 e^{-E(\alpha)/2}
 \operatorname{Str}R_\alpha\,
 \delta_{E(\alpha)}
=
\sum_p\sum_{k\ge1}
(\log p)p^{-k/2}\delta_{k\log p}.
}
\tag{6}
\]

Equation (6) is exactly the finite coefficient measure isolated in WP-004. It therefore answers one concrete question left open by WP-017: **retaining the full exponent multiplicity does admit a canonical local incidence operation that has events at every integer yet kills all non-prime-powers and normalizes every `p^k` to `log p`.**

The price is that the selector is graded.

## 4. The arithmetic selector is not supplied by positivity

Although every `R_alpha` is positive, the functional used in (3) is

\[
\operatorname{Str}R_\alpha
=\operatorname{Tr}(\Gamma R_\alpha),
\]

and `Gamma` has both signs as soon as the cube has an edge. A supertrace is not a positive functional on positive operators. Already on a one-dimensional Boolean cube, for a generic positive diagonal operator

\[
D=\operatorname{diag}(a,b),\qquad a,b\ge0,
\]

one has

\[
\operatorname{Str}D=a-b,
\]

which may be positive, zero, or negative.

The nonnegativity of (3) therefore does **not** follow from the theorem `R_alpha>=0`. It follows from the special affine and coordinate-monotone form of `E`: along a single occupied coordinate the backward energy drop is `log p>0`, while all higher mixed differences vanish.

Replacing supertrace by the ordinary positive trace destroys the Mangoldt support. Directly,

\[
\operatorname{Tr}R_\alpha
=2^rE(\alpha)-2^{r-1}\sum_{p\in S(\alpha)}\log p,
\tag{7}
\]

which is positive for generic composites and, on `n=p^k`, equals

\[
(2k-1)\log p,
\]

not `log p`.

Thus the exact prime-power selector sits in the same structural tension seen elsewhere in this branch: **positivity is available before grading, while the arithmetic cancellation appears only after introducing signs.** Here, however, the cancellation is local and completely explicit rather than the global Hodge-index cancellation of WP-016.

## 5. Matched controls show that the mechanism is finite-place and universal

Replace the rational primes by abstract generators `q_j` carrying arbitrary positive weights `a_j>0`, and define

\[
E_a(\alpha)=\sum_j\alpha_j a_j.
\]

The identical Boolean calculation gives

\[
\operatorname{Str}R^a_\alpha
=\begin{cases}
a_j,&\operatorname{supp}(\alpha)=\{j\},\\
0,&|\operatorname{supp}(\alpha)|\ge2.
\end{cases}
\tag{8}
\]

So the sign/cancellation theorem does not distinguish rational primes from a generic weighted free commutative monoid. In particular it survives verbatim for Beurling generalized-prime exponent systems, where the same axis selector gives the generalized von Mangoldt function.

This is a decisive matched control. The Boolean supertrace is a canonical way to extract **generator powers** from free exponent geometry, not a mechanism that knows the global arithmetic completion of `Q`. The Beurling controls already used in WP-004 can have the same finite selector while their zeta functions possess zeros far to the right of `1/2`.

## 6. No archimedean or polar term is generated

The entire construction of `C_alpha`, `R_alpha`, and `Gamma` lives in the nonnegative finite-prime exponent cone. It has no distinguished infinite-place degree of freedom, no product-formula constraint, and no source for the gamma or pole terms of the completed explicit formula.

One could append such terms externally, but then their sign and normalization would not follow from the Boolean energy supertrace. Prior findings already show why the obvious completions are insufficient: bare Tate self-duality is indefinite (WP-008), direct positive Hankel completion leaves the positive-measure cone (WP-013), and ordinary arithmetic-surface fiber intersection kills the prime axes (WP-011).

Therefore (6) is a stronger finite-place realization than a mere support observation, but it still does not assemble a global Weil-positive form.

## 7. Relation to WP-016 and WP-017

WP-016 found a genuine positive Hodge Laplacian on the square-free Björner complex, but all positive nonzero Hodge modes cancel from the graded arithmetic supertrace. WP-017 then showed that square-free persistence cannot repair the finite Weil support because there are no events at proper prime powers.

The full exponent lattice now resolves the latter problem in a precise way:

```text
full exponent vector alpha
    -> canonical backward Boolean cube C_alpha
    -> positive residual-energy operator R_alpha
    -> alternating supertrace
    -> Lambda(n)
    -> critical attenuation Lambda(n)/sqrt(n).
```

But it also identifies the remaining obstruction more sharply. The finite Mangoldt selector itself is an **incidence/Möbius grading effect**. It is not the ordinary trace of a positive energy, nor a positive Hodge pairing. Any global cohomological construction that uses this selector must therefore explain why the required grading and the archimedean/polar completion together produce a positive Weil quadratic form by an independent theorem.

This is materially narrower than the escape left by WP-017: the missing finite selector no longer needs to be guessed, but its exact canonical form already carries alternation.

## 8. Prior art and novelty audit

No theorem-level novelty is claimed.

- `Lambda = mu * log` is a classical Möbius-inversion identity.
- The sign `(-1)^{|T|}` on a Boolean interval is the classical Möbius function of the subset/divisibility lattice.
- Björner's number-theoretic complexes and multicomplexes already organize the same exponent/divisibility poset topologically, as recorded for WP-016 and WP-017.
- The generalized-prime von Mangoldt selector is standard and is already anchored in this branch by Révész.

The durable Mathia-specific result is the **exact local operator packaging and its no-go consequence**: the full exponent geometry does canonically solve WP-017's prime-power support/normalization problem, but it does so through a supertrace of positive local energies. Consequently, it does not supply the sought positive quadratic functional and does not remove the need for genuinely global structure.

## 9. Falsification and boundary tests

Withdraw or narrow this finding if any of the following fails:

1. every `alpha` has the backward Boolean cube `alpha-1_T` for `T subseteq supp(alpha)` inside `N_0^(P)`;
2. the residual energies `E(alpha-1_T)` are nonnegative;
3. the alternating sum in (1) is `log p` for support size one and zero for support size at least two;
4. therefore the sum equals `Lambda(n)` for every `n>=2`;
5. the same calculation works for arbitrary positive generator weights and hence is not specific to rational primes;
6. ordinary trace (7) is nonzero on generic composites and fails the prime-power normalization;
7. no archimedean or pole datum is present in the construction itself.

All seven statements are finite and exact. They require neither RH nor analytic continuation.

This finding does **not** rule out a graded global geometry. A supertrace can participate in a successful trace formula when a separate geometric theorem controls the assembled sign. What is ruled out is treating the positivity of the local operators `R_alpha` as if it automatically made their Mangoldt supertrace a positive form. The surviving route must derive the grading, the infinite-place completion, and the final nonnegativity from one larger Mathia-native structure.

## Internal dependencies

- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-016-prime-lattice-hodge-positivity-cancels-out-of-the-arithmetic-supertrace.md`
- `research/weil_positivity/findings/WP-017-squarefree-persistence-has-no-prime-power-events.md`
- `research/prime_lattice/findings/PL-008-mobius-hardy-zero-free-bridge.md`
- `research/prime_lattice/findings/PL-022-bjorner-exponent-cell-complex-hodge-obstruction.md`
