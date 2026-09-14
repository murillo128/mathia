# AF-340 — constant-background zero isolation forces growing sign complexity

**Status:** `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `SOURCE-COMPLEXITY-GATE`, `ZERO-SENSITIVE-SOURCE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-339 shows that the pole-cancelled discrepancy `Lambda(n)-1` retains the zeta zero divisor but has ordered sign variation of order `P/log P` on every fixed multiplicative window `[P,AP]`. That result should not be overread as saying that **zero sensitivity itself** requires a complicated signed source: the uncentered Mangoldt source `Lambda(n)` is one-sided.

The exact obstruction is sharper. Within the natural one-parameter family obtained by subtracting a constant background,

\[
d_n^{(c)}:=\Lambda(n)-c,
\qquad n\ge2,
\qquad c\in\mathbb R,
\tag{1}
\]

the two desired resources split at a sharp boundary.

For `Re(s)>1`,

\[
\boxed{
H_c(s):=\sum_{n\ge2}d_n^{(c)}n^{-s}
=-\frac{\zeta'(s)}{\zeta(s)}-c\bigl(\zeta(s)-1\bigr).
}
\tag{2}
\]

If `rho` is any zero of `zeta` of multiplicity `m`, then

\[
\boxed{
\operatorname*{Res}_{s=\rho}H_c(s)=-m
}
\tag{3}
\]

for **every** real `c`. Thus the whole family retains the zero divisor as poles with the same residues.

At the pole of zeta,

\[
\boxed{
\operatorname*{Res}_{s=1}H_c(s)=1-c.
}
\tag{4}
\]

Hence the main pole is removed **if and only if**

\[
\boxed{c=1.}
\tag{5}
\]

On the source side, using the AF-216 convention that zero coefficients are deleted before sign changes are counted:

- if `c<=0`, then
  \[
  \boxed{V(d_L^{(c)},\ldots,d_U^{(c)})=0}
  \tag{6}
  \]
  for every finite interval after deleting zero coefficients;
- if `c>0`, then for every fixed `A>1`, as `P->infinity`,
  \[
  \boxed{
  V\bigl(d_P^{(c)},\ldots,d_{\lfloor AP\rfloor}^{(c)}\bigr)
  =\bigl(2(A-1)+o(1)\bigr)\frac{P}{\log P}.
  }
  \tag{7}
  \]

Therefore this complete constant-background family has a sharp tradeoff:

\[
\boxed{
\begin{array}{c}
\text{bounded ordered sign complexity}\[2pt]
(c\le0)
\end{array}
\quad\Longrightarrow\quad
\text{the pole at }1\text{ survives},
}
\tag{8}
\]

while the unique member that removes that pole, `c=1`, necessarily lies in the growing-sign-complexity regime.

Equivalently, **zero-divisor sensitivity is cheap in this family; isolating the zero-sensitive fluctuation from the zeta main pole by a constant background is what spends an unbounded ordered sign budget.** No choice of constant background gives both pole cancellation at `s=1` and a source sign order bounded independently of an escaping multiplicative window.

## Derivation

### 1. Every constant background preserves the zeta-zero poles

The classical logarithmic-derivative identity gives, for `Re(s)>1`,

\[
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\tag{9}
\]

and

\[
\zeta(s)-1=\sum_{n\ge2}n^{-s}.
\tag{10}
\]

Subtracting `c` times `(10)` from `(9)` proves `(2)`.

If `rho` is a zero of multiplicity `m`, write

\[
\zeta(s)=(s-\rho)^m g(s),
\qquad g(\rho)\ne0.
\]

Then

\[
-\frac{\zeta'(s)}{\zeta(s)}
=-\frac{m}{s-\rho}-\frac{g'(s)}{g(s)},
\tag{11}
\]

whereas `-c(zeta(s)-1)` is holomorphic at `rho`. This proves `(3)`.

Near `s=1`,

\[
\zeta(s)=\frac1{s-1}+\gamma+O(s-1)
\]

and therefore

\[
-\frac{\zeta'(s)}{\zeta(s)}
=\frac1{s-1}-\gamma+O(s-1).
\tag{12}
\]

The second term in `(2)` has residue `-c`, so `(4)` and `(5)` follow.

### 2. The one-sided branch is exactly `c<=0`

Because `Lambda(n)>=0` for every integer `n`, if `c<0` then

\[
d_n^{(c)}=\Lambda(n)+|c|>0
\]

for every `n`. Thus the ordered sign variation is zero.

At `c=0`, the nonzero coefficients are exactly the prime powers and all of them are positive. AF-216 deletes zero coefficients before counting sign changes, so the variation is again zero. This proves `(6)`.

Notice what this does and does not mean. The source `Lambda(n)` is genuinely zero-sensitive through `-zeta'/zeta`, but it also retains the pole at `1`. It therefore disproves any stronger claim that zero sensitivity alone forces source oscillation.

### 3. Every positive background creates prime-scale sign oscillation

Fix `c>0` and `A>1`. For all sufficiently large rational primes `p`,

\[
d_p^{(c)}=\log p-c>0.
\tag{13}
\]

Every non-prime-power integer has coefficient `-c<0`. Thus every sufficiently large odd prime in `[P,AP]` is a positive site surrounded by negative even neighbors, except when one adjacent even integer is itself a positive power of `2`. In a fixed multiplicative window there are only `O_A(1)` powers of `2`, so endpoint effects and these exceptional adjacent pairs remove only `O_A(1)` of the two sign-changing edges contributed by the primes. Hence

\[
V\bigl(d_P^{(c)},\ldots,d_{\lfloor AP\rfloor}^{(c)}\bigr)
\ge
2\bigl(\pi(AP)-\pi(P)\bigr)-O_{A,c}(1).
\tag{14}
\]

For the opposite bound, every sign change is incident to a positive coefficient. Positive coefficients can occur only at prime powers `p^k` with `log p>c`. The number of such sites in `[P,AP]` is at most

\[
\pi(AP)-\pi(P)+O_A(\sqrt P\log P),
\tag{15}
\]

because all powers with `k>=2` contribute only `O_A(\sqrt P\log P)` sites. Each positive site is incident to at most two sign-changing edges, so

\[
V\bigl(d_P^{(c)},\ldots,d_{\lfloor AP\rfloor}^{(c)}\bigr)
\le
2\bigl(\pi(AP)-\pi(P)\bigr)+O_A(\sqrt P\log P).
\tag{16}
\]

The prime number theorem on the fixed multiplicative interval gives

\[
\pi(AP)-\pi(P)
=\bigl(A-1+o(1)\bigr)\frac{P}{\log P},
\tag{17}
\]

and `(14)`--`(17)` prove `(7)`.

If `c=log p_0` for a fixed prime `p_0`, the coefficients at powers of `p_0` vanish. Deleting those zero coefficients changes only a lower-order set and does not affect `(7)`.

## Consequence for the AF-216 / AF-338 route

AF-216 proves that a nonzero signed source with at most `r-1` ordered sign changes cannot annihilate `r` equally spaced first-harmonic Dirichlet samples. AF-338 transfers a fixed requested sign order to the full Euler-log kernel on sufficiently remote integer windows under the sufficient depth condition `sigma>r-1`.

AF-340 shows that the apparent source-side shortcut `use Lambda itself because it has no sign changes` pays for that simplicity by retaining the dominant pole at `s=1`. Conversely, every positive constant subtraction produces a sign budget growing on prime scale, and the **only** subtraction that exactly cancels the pole is the AF-339 source `Lambda-1`.

This does not prove that pole cancellation is logically necessary for every RH-facing representation. It proves a narrower no-go statement: **constant-background centering cannot simultaneously buy a pole-free zero-sensitive destination and bounded ordered source complexity.** A successful recoding of the AF-339 source must therefore be genuinely more structured than changing the constant baseline.

The remaining live alternatives are correspondingly sharper:

- use a nonconstant or multiscale background whose subtraction lowers effective source complexity while preserving recoverable zero-divisor information;
- group or transform the centered source in a way that reduces the complexity consumed by the observation theorem without hiding the original source in the lift;
- prove a growing-order observation theorem with joint source-scale control; or
- replace ordered sign variation by a different finite-certifiable source invariant.

## Exact controls and boundaries

### This is a classification only of constant backgrounds

A varying baseline `b_n`, block average, cumulative transform, wavelet-like recoding, summation-by-parts representation, or nonlinear grouping can have a completely different sign geometry. AF-340 does not rule out those mechanisms.

What it rules out is the simplest affine repair

\[
\Lambda(n)\longmapsto\Lambda(n)-c
\]

with fixed `c`.

### Pole removal is not itself RH relevance

Cancelling the pole at `1` makes the retained singularities cleaner, but it does not distinguish critical-line zeros from off-line zeros, force positivity, or prove RH. Equation `(5)` is a representation-level isolation statement, not a theorem that every useful RH route must remove the pole.

### The `c<=0` branch is sign-simple for a trivial reason

For `c<0` every coefficient is positive; for `c=0` every nonzero coefficient is positive. This is not a discovered arithmetic regularity. Its value is as a matched control showing exactly which additional operation creates the oscillation seen in AF-339.

### The positive-background asymptotic is insensitive to finitely many threshold primes

For fixed `c>0`, whether a small prime power has coefficient positive, zero, or negative affects only lower-order terms. The main sign-variation scale comes from ordinary primes near `P`, for which `log p>c` automatically once `P` is large.

### AF-338 remains fixed-order

As in AF-339, `(7)` cannot be substituted into AF-338's sufficient condition to assert a necessary sampling depth of order `P/log P`. AF-338's constants and threshold depend on fixed `r`; no growing-order uniform theorem has been proved.

## Prior art and novelty assessment

No novelty claim is made for the constituent number theory.

- The von Mangoldt identity `-zeta'/zeta=sum Lambda(n)n^{-s}` for `Re(s)>1` is classical. The *Encyclopedia of Mathematics* entry **“Mangoldt function”** records both the definition of `Lambda` and this Dirichlet-series identity; Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., is a standard primary reference for the analytic continuation and zero/pole structure used here.
- The prime number theorem and the fact that higher prime powers are lower-order in prime-power counting are classical. The *Encyclopedia of Mathematics* entry **“Chebyshev function”** records `psi(x)=sum_{n<=x}Lambda(n)` and its prime-power decomposition.
- A targeted search for the fixed family `Lambda(n)-c`, its ordered sign changes, and the simultaneous cancellation of the zeta pole did not identify a standard theorem organized as `(4)`--`(8)`. That absence is not used as a novelty claim: the classification follows directly from classical identities, the definition of `Lambda`, and the prime number theorem.

The durable Arithmetic Fidelity contribution is the **resource separation**. AF-339's obstruction is not caused by remembering the zero divisor. The source becomes oscillatory when a positive background is subtracted, and exact cancellation of the zeta pole uniquely selects the centered member `c=1`. This identifies what the next compression must improve rather than merely restating that the raw centered coefficients oscillate.

## Consequence for Arithmetic Fidelity

The source-side problem now has a clean matched-control boundary:

\[
\text{Lambda source: sign-simple + zero-sensitive + main pole retained},
\]

whereas

\[
\text{Lambda-1 source: main pole removed + zero-sensitive + growing sign complexity}.
\]

Within constant-background recodings there is no third option that combines the favorable sides. The next useful compression question is therefore not whether one can tune the baseline, but whether a **structured nonconstant recoding can remove or quarantine the main term while making the residual zero-sensitive discriminator cheaper for the downstream observation theorem**.
