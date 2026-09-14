# AF-344 — power-supported backgrounds trade sign density for amplitude

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-COUNTEREXAMPLE`, `NO-NOVELTY-CLAIM`

## Claim

AF-342 proves that reducing the ordered sign variation of the prime-layer residual requires prime-scale exceptional behavior in a general background, and AF-343 shows that fixed nonnegative periodic or more generally syndetic positive-composite backgrounds cannot supply that escape. The remaining live possibility is a fixed non-syndetic background with long zero gaps.

That escape is real, and it can be realized by an extremely simple prime-independent family. For every fixed integer `k>=2`, define

\[
b_k(n):=
\begin{cases}
 k m^{k-1},& n=m^k\text{ for an integer }m>=2,\\
 0,&\text{otherwise}.
\end{cases}
\tag{1}
\]

Let the prime layer from AF-341 be

\[
a(n):=\begin{cases}\log p,&n=p\text{ prime},\\0,&\text{otherwise},\end{cases}
\qquad
h_k(n):=a(n)-b_k(n).
\tag{2}
\]

Then the following three statements hold simultaneously.

### 1. The background is pole-normalized and zero-pole-blind

For `Re(s)>1`,

\[
B_k(s):=\sum_{n>=2} b_k(n)n^{-s}
=k\sum_{m>=2}m^{k-1-ks}
=\boxed{k\bigl(\zeta(ks-k+1)-1\bigr)}.
\tag{3}
\]

Hence `B_k` extends meromorphically to the whole plane with exactly one pole, at `s=1`, and

\[
\operatorname*{Res}_{s=1}B_k(s)=1.
\tag{4}
\]

It is therefore holomorphic at every nontrivial zeta zero.

If `A(s)=\sum_p(\log p)p^{-s}` denotes the meromorphic prime-layer transform from AF-341 and

\[
H_k(s):=A(s)-B_k(s),
\tag{5}
\]

then the pole at `s=1` cancels, every zeta zero `rho` with `Re(rho)>1/2` remains a pole of residue minus its multiplicity, and

\[
\boxed{\mathrm{RH}\iff H_k\text{ is holomorphic on }\Re(s)>\tfrac12.}
\tag{6}
\]

Thus `b_k` preserves exactly the same right-half-plane RH pole discriminator used in AF-341--AF-343 without depending on prime locations or on the zero divisor.

### 2. The residual has sub-prime-scale ordered sign variation

Every nonzero coefficient of `h_k` is either

- positive at a prime, where `h_k(p)=\log p`, or
- negative at a perfect `k`-th power `m^k`, where `h_k(m^k)=-k m^{k-1}`.

These supports are disjoint for `k>=2` and `m>=2`. Under the AF-216 convention that zero coefficients are deleted before sign changes are counted, let

\[
N_k(P,B):=\#\{m>=2:P\le m^k\le BP\}.
\tag{7}
\]

Each negative entry can participate in at most two sign changes in the zero-deleted sequence, so for every fixed `B>1`,

\[
V\bigl(h_k(P),\ldots,h_k(\lfloor BP\rfloor)\bigr)
\le 2N_k(P,B).
\tag{8}
\]

Moreover,

\[
N_k(P,B)
=\bigl(B^{1/k}-1\bigr)P^{1/k}+O_k(1),
\tag{9}
\]

and therefore

\[
\boxed{
V\bigl(h_k(P),\ldots,h_k(\lfloor BP\rfloor)\bigr)
=O_{k,B}(P^{1/k})
=o\!\left(\frac{P}{\log P}\right).
}
\tag{10}
\]

For every fixed `k`, this beats the `Theta(P/log P)` variation of the uniformly centered prime layer. Taking larger fixed `k` makes the polynomial exponent `1/k` arbitrarily small.

### 3. The saved sign density reappears as coefficient amplitude

The baseline has only about `x^{1/k}` nonzero sites up to `x`, but its coefficients on those sites have size about `x^{1-1/k}`. More precisely, elementary power-sum asymptotics give

\[
\sum_{n\le x} b_k(n)
=k\sum_{2\le m\le x^{1/k}}m^{k-1}
=x+O_k\bigl(x^{1-1/k}\bigr),
\tag{11}
\]

and on every fixed multiplicative window,

\[
\sum_{P\le n\le BP}b_k(n)
=(B-1)P+O_{k,B}\bigl(P^{1-1/k}\bigr).
\tag{12}
\]

At the same time,

\[
\#\operatorname{supp}(b_k)\cap[P,BP]=\Theta_{k,B}(P^{1/k}),
\qquad
\max_{P\le n\le BP} b_k(n)=\Theta_{k,B}(P^{1-1/k}).
\tag{13}
\]

So this family does not make the unit-residue main term disappear. It concentrates order-`P` background mass onto a sparse set of composite sites. The sign-count resource drops because most composite coefficients become exactly zero, while the missing density is paid for by growing amplitude.

The durable conclusion is therefore a counterexample to treating ordered sign variation, exceptional-site cardinality, or description length as interchangeable source-complexity currencies:

\[
\boxed{
\text{sparse support + growing amplitude can preserve the RH pole discriminator while collapsing sign variation.}
}
\tag{14}
\]

A fixed algebraic rule as simple as “weighted perfect `k`-th powers” is enough. No prime-scale list of exceptional locations is required.

## Derivation

### 1. Exact Dirichlet transform and residue

For `Re(s)>1`, substitute `n=m^k` into the Dirichlet series of `(1)`:

\[
\begin{aligned}
B_k(s)
&=\sum_{m>=2}k m^{k-1}(m^k)^{-s}\\
&=k\sum_{m>=2}m^{-(ks-k+1)}\\
&=k\bigl(\zeta(ks-k+1)-1\bigr).
\end{aligned}
\tag{15}
\]

The Riemann zeta function is meromorphic on `C` with only a simple pole at `1` of residue `1`. Therefore the affine pullback in `(15)` has a pole only when

\[
ks-k+1=1,
\]

namely at `s=1`. Since

\[
\zeta(1+k(s-1))
=\frac{1}{k(s-1)}+O(1),
\tag{16}
\]

multiplication by `k` gives residue `1`, proving `(4)`.

AF-341 proves that `A` is meromorphic on `Re(s)>1/2`, has residue `+1` at `1`, and residue `-m_rho` at every zeta zero `rho` in that half-plane. Equation `(4)` cancels the first pole, while `B_k` is holomorphic at every `rho!=1`. This proves `(6)` exactly as in the analytic specialization of AF-342.

### 2. Sign changes are controlled by the sparse negative support

For `k>=2`, no integer `m^k` with `m>=2` is prime. Thus the nonzero signs of `h_k` are exactly `+` on ordinary primes and `-` on perfect `k`-th powers. All remaining integers contribute zeros and disappear under the line's sign-variation convention.

In any finite `+/-` sequence containing `N_-` negative entries, the number of sign changes is at most twice the number of negative runs, hence at most `2N_-`. Applying this with the negative sites in `[P,BP]` gives `(8)`.

The count `(9)` follows directly from

\[
P^{1/k}\le m\le (BP)^{1/k}.
\]

Combining `(8)` and `(9)` proves `(10)`. No statement that the upper bound is sharp is needed. A matching lower bound would require information about primes between successive `k`-th powers and is deliberately not asserted.

### 3. Sparse mass and amplitude are exactly balanced

Write `M=\lfloor x^{1/k}\rfloor`. The elementary estimate

\[
\sum_{m\le M}m^{k-1}=\frac{M^k}{k}+O_k(M^{k-1})
\tag{17}
\]

gives

\[
k\sum_{2\le m\le M}m^{k-1}=M^k+O_k(M^{k-1})=x+O_k(x^{1-1/k}),
\tag{18}
\]

which is `(11)`. Subtracting the same estimate at `P` and `BP` gives `(12)`. The support and amplitude estimates in `(13)` are immediate from the definition.

This is the source-side conservation law exposed by the example: decreasing the density of negative witnesses from order `P` to order `P^{1/k}` forces their individual scale to grow to order `P^{1-1/k}` if the baseline is still to carry unit average mass and cancel the pole at `1`.

## Relation to AF-342 and AF-343

AF-342's exceptional-set lower bound is not contradicted. For `b_k`, one has `b_k(p)=0<log p` at every prime, so there are no prime-height exceptions. Instead almost every prime-adjacent composite satisfies `b_k(m)=0`, hence belongs to AF-342's set `C_b` because that theorem counts `b(m)<=0`. The exceptional set is prime-scale even though the baseline itself has a short fixed formula and only `O(P^{1/k})` nonzero sites in a multiplicative window.

This realizes exactly the boundary already stated in AF-342: exceptional-site cardinality is not a description-length lower bound. Here the large `C_b` is generated by the generic zero value rather than by a stored list of prime-adjacent composites.

AF-343 is also respected. Its syndetic positive-composite witness hypothesis fails maximally: the positive support of `b_k` is the perfect `k`-th powers, whose gaps are unbounded. What AF-343 left as an escape is therefore not merely formal. A fixed, nonnegative, nonperiodic, zero-pole-blind background with unbounded witness gaps can preserve the RH discriminator and reduce the residual sign variation below prime scale.

The price is not hidden prime provenance. It is **amplitude concentration**. This redirects the frontier from “can a non-syndetic baseline exist?” to “which source regularity or downstream theorem controls the joint support-density/amplitude tradeoff rather than sign count alone?”

## Exact controls and boundaries

### This is not an RH proof or a new RH criterion

Equation `(6)` is the same classical right-half-plane pole discriminator already isolated in AF-341 and abstracted in AF-342. The new content is the resource counterexample: that discriminator can coexist with a residual whose ordered sign variation is only `O(P^{1/k})`.

### The baseline has unbounded coefficients

The construction intentionally spends amplitude. Any theorem that requires a uniformly bounded background, bounded local mass, an `ell^p` budget, bounded dynamic range, or another amplitude regularity can exclude this example. AF-344 proves that such a retained resource is necessary if ordered sign variation is intended to stand in for a broader notion of source simplicity.

### Zero deletion is load-bearing

The collapse in `(10)` uses the established AF-216 convention that zero coefficients are deleted before counting ordered sign changes. If zero runs themselves carry a cost, or if the downstream observation theorem prices support gaps, the resource accounting changes. This is not a defect in the calculation; it identifies another piece of source structure that the sign statistic forgets.

### The exponent `1/k` is an upper-bound scale, not a claimed optimum

For fixed `k`, `(10)` is enough to prove sub-prime-scale sign variation. No lower bound of order `P^{1/k}` is asserted. In particular, proving that every interval between consecutive `k`-th powers contains a prime would be a separate and generally unavailable number-theoretic input.

### Large fixed `k` is not one universal background

Each `k` defines a different fixed baseline. The family shows that no positive polynomial lower exponent is forced uniformly over this simple class, but it does not produce a single baseline with polylogarithmic or bounded sign variation.

### Analytic fidelity does not imply downstream usability

`H_k` retains the zero-pole discriminator, but AF-344 does not show that an AF-216/AF-338-style observation theorem remains effective for the large negative amplitudes, sparse support, or zero runs of `h_k`. The result removes ordered sign variation by itself as a sufficient proxy for the missing source regularity; it does not supply the replacement regularity theorem.

## Prior art and novelty assessment

No novelty claim is made for the analytic ingredients.

- NIST Digital Library of Mathematical Functions, §25.2 records the classical Dirichlet-series definition of `zeta(s)` for `Re(s)>1` and its meromorphic continuation with a unique simple pole at `s=1` of residue `1`. Substitution of the affine argument `ks-k+1` gives `(15)` immediately.
- Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., remains the standard source used in AF-341 for the logarithmic derivative, zero-pole structure, and functional-equation symmetry underlying `(6)`.
- Perfect `k`-th powers and power-sum asymptotics are classical; `(9)` and `(17)` are elementary consequences of their defining parametrization and integral/Euler-Maclaurin estimates.

A targeted literature search did not identify a standard theorem organized around this particular comparison between perfect-power background sparsity, pole cancellation, RH pole fidelity, and ordered sign variation. That search failure is not evidence of novelty. The constituent identities are elementary/classical, and the result is classified as an exact Arithmetic Fidelity resource-accounting counterexample rather than a new analytic-number-theory theorem.

## Consequence for Arithmetic Fidelity

AF-342--AF-343 had narrowed the source recoding problem to a non-syndetic or genuinely multiscale background. AF-344 resolves the existence side decisively: such a background can be fixed, prime-independent, and algebraically trivial.

The important change is conceptual. **Ordered sign variation is not conserved under fidelity-preserving recoding once sparse high-amplitude backgrounds are allowed.** A source representation can retain the RH right-half-plane pole discriminator while making sign count arbitrarily low in polynomial exponent, without encoding the prime locations into the baseline.

The next useful theorem must therefore price at least one resource that AF-344 spends and the sign count ignores: coefficient amplitude/dynamic range, support-gap geometry, local mass concentration, or a joint norm that couples these to sign variation. Otherwise the source-complexity obstruction can always be shifted into a sparse weighted background rather than genuinely removed.