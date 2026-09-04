# MC-049 — Global Liouville pretentiousness turns comparator power cancellation into a zeta zero-free condition

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
f:\mathbb N\to[-1,1]
\]

be completely multiplicative, let

\[
S_f(x)=\sum_{n\le x}f(n),
\qquad
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s},
\]

and suppose that for some fixed

\[
0<\delta<\frac12
\]

one has

\[
S_f(x)\ll x^{1-\delta}.
\tag{1}
\]

Write `lambda` for the Liouville function. Under `(1)`, the following two conditions are equivalent:

\[
\boxed{
F(1)=0
\quad\Longleftrightarrow\quad
\sum_p\frac{1+f(p)}p<\infty.
}
\tag{2}
\]

The right-hand condition is exactly finite **global ordinary pretentious distance** from Liouville, because `lambda(p)=-1` and `f(p)` is real:

\[
\mathbb D(f,\lambda;\infty)^2
=
\sum_p\frac{1-\operatorname{Re}(f(p)\overline{\lambda(p)})}{p}
=
\sum_p\frac{1+f(p)}p.
\tag{3}
\]

The forward implication in `(2)` is established prior art: Aymone's Theorem 1.1 (`MC-S33`) proves that `(1)` together with `F(1)=0` forces `f` to be Liouville-pretentious, and in fact proves the much stronger weighted prime estimate

\[
\sum_{p\le x}(1+f(p))\log p
\ll_\varepsilon x^{1-\delta+\varepsilon}.
\tag{4}
\]

The reverse implication in `(2)` is elementary. If the ordinary global Liouville distance is finite, then the Euler-product ratio between `F` and the Liouville Dirichlet series has a finite positive limit at `s=1`. Since

\[
\sum_{n\ge1}\frac{\lambda(n)}{n^s}
=
\frac{\zeta(2s)}{\zeta(s)}
\to0
\qquad(s\to1^+),
\tag{5}
\]

and `(1)` makes `F` analytic at `s=1`, it follows that `F(1)=0`.

Combining `(2)` with the second conclusion of Aymone's theorem gives the line-specific obstruction:

\[
\boxed{
S_f(x)\ll x^{1-\delta}
\ \,\text{and}\ 
\mathbb D(f,\lambda;\infty)<\infty
\quad\Longrightarrow\quad
\zeta(s)\ne0
\ \text{for}\ \operatorname{Re}s>1-\delta.
}
\tag{6}
\]

Thus a fixed real completely multiplicative comparator cannot simultaneously be globally Liouville-pretentious and enjoy an independently proved power saving without that power saving already forcing a matching zero-free half-plane for the Riemann zeta function.

In particular, if one could produce a fixed such comparator satisfying

\[
S_f(x)=O_\varepsilon(x^{1/2+\varepsilon})
\qquad\text{for every }\varepsilon>0
\tag{7}
\]

while retaining finite global ordinary distance from Liouville, then RH would follow. For every `eta in (0,1/2)`, apply `(6)` with `delta=1/2-eta` using the `x^(1/2+eta)` instance of `(7)`; zeta is then zero-free in `Re(s)>1/2+eta`. Letting `eta` tend to zero excludes every zero with real part greater than `1/2`, and the functional-equation symmetry gives RH.

This is not a new RH criterion or a new zero-free theorem. The zero-free implication is Aymone's theorem. The durable point for the current research line is that the hypothesis `F(1)=0` appearing in that theorem is **not an independent hidden analytic condition** once one proposes a power-cancellative comparator that is globally ordinarily pretentious to Liouville: the ordinary prime-harmonic relation itself forces the zero at `1`.

## 1. Power cancellation makes the comparator Dirichlet series regular at `s=1`

From `(1)` and partial summation,

\[
F(s)=s\int_1^\infty S_f(x)x^{-s-1}\,dx
\tag{8}
\]

in the half-plane

\[
\operatorname{Re}s>1-\delta.
\]

Hence `F` is analytic there, in particular at `s=1`. This point matters because the argument below first identifies the limit of `F(s)` along the real axis as `s->1+`; `(8)` guarantees that this limit is the actual analytic value `F(1)` rather than merely a boundary value of an Euler product.

No information about zeros of zeta has entered at this stage.

## 2. Global Liouville pretentiousness forces `F(1)=0`

For real `sigma>1`, complete multiplicativity gives

\[
F(\sigma)
=
\prod_p\left(1-\frac{f(p)}{p^\sigma}\right)^{-1},
\tag{9}
\]

while

\[
L_\lambda(\sigma)
:=
\sum_{n\ge1}\frac{\lambda(n)}{n^\sigma}
=
\prod_p\left(1+\frac1{p^\sigma}\right)^{-1}
=
\frac{\zeta(2\sigma)}{\zeta(\sigma)}.
\tag{10}
\]

Therefore

\[
\frac{F(\sigma)}{L_\lambda(\sigma)}
=
\prod_p
\frac{1+p^{-\sigma}}
     {1-f(p)p^{-\sigma}}.
\tag{11}
\]

At `sigma=1`, each local factor is at least `1` because `-1<=f(p)<=1`, and

\[
\log\frac{1+p^{-1}}{1-f(p)p^{-1}}
=
\frac{1+f(p)}p+O\!\left(\frac1{p^2}\right),
\tag{12}
\]

uniformly in the allowed values of `f(p)`. If the right side of `(3)` is finite, the logarithms in `(12)` are summable. Consequently `(11)` has a finite strictly positive limit

\[
0<R_f<\infty
\qquad(\sigma\to1^+).
\tag{13}
\]

The classical pole of zeta at `1` gives

\[
L_\lambda(\sigma)=\frac{\zeta(2\sigma)}{\zeta(\sigma)}\to0.
\tag{14}
\]

Equations `(11)`--`(14)` imply

\[
F(\sigma)\to R_f\cdot0=0.
\]

By the analyticity from Section 1,

\[
F(1)=0.
\tag{15}
\]

This implication uses only the global ordinary Liouville-pretentious prime sum and the independently assumed power saving. It does not use RH, a zero-free region, analytic continuation of `1/zeta` into the critical strip, or the stronger power-aware pretentious quantities of `MC-047`--`MC-048`.

## 3. Aymone upgrades the same hypotheses to a zero-free region

Aymone (`MC-S33`) proves that a completely multiplicative `f:N->[-1,1]` satisfying `(1)` and `(15)` obeys `(4)` and, crucially,

\[
\zeta(s)\ne0
\qquad
(\operatorname{Re}s>1-\delta).
\tag{16}
\]

The source proof is structurally important for this line. Setting `h=1*f`, the local coefficients

\[
h(p^m)=1+f(p)+\cdots+f(p)^m
\]

are nonnegative. The product `H(s)=zeta(s)F(s)` is analytic past `1` because `F(1)=0` cancels the zeta pole. Landau's theorem for Dirichlet series with nonnegative coefficients then converts analyticity into convergence, giving strong control of the Euler factors. A square-free-supported companion series is used to conclude that `1/zeta(s)` is analytic throughout `Re(s)>1-delta`.

That is an established literature mechanism, not a new derivation here. The new bookkeeping consequence is only that the apparently separate source hypothesis `F(1)=0` is automatic for the comparator class described by `(1)` and `(3)`.

The same theorem proves the forward implication in `(2)`: `F(1)=0` plus `(1)` forces the prime sum in `(3)` to converge. Hence within this power-cancellative completely multiplicative real class, the analytic zero at `1` and global ordinary Liouville pretentiousness are equivalent interfaces to the same zero-free obstruction.

## 4. Cancellation alone is not enough: a character control

The Liouville-proximity condition is substantive. Let `chi` be a fixed nonprincipal real Dirichlet character. It is completely multiplicative with values in `{-1,0,1}`, and periodicity gives

\[
\sum_{n\le x}\chi(n)=O(1)
\tag{17}
\]

for fixed modulus. Thus it has far stronger summatory cancellation than required by `(1)` for every `delta<1`.

Nevertheless its Dirichlet series satisfies

\[
F(1)=L(1,\chi)\ne0.
\tag{18}
\]

Therefore `(2)` forces

\[
\sum_p\frac{1+\chi(p)}p=\infty.
\tag{19}
\]

So one cannot drop the Liouville-pretentious hypothesis and conclude a zeta zero-free region merely from the existence of an unrelated completely multiplicative function with excellent partial sums. This matched control prevents the finding from degenerating into the false statement that any independent power-cancellative comparator carries RH information.

There is a second important boundary. Möbius and the exact-support comparators `mu^2 g` used elsewhere in this line are multiplicative but **not completely multiplicative**, because they vanish on prime squares. Aymone's theorem does not apply to that class. The obstruction therefore narrows a comparator route; it does not collapse the full multiplicative-search space.

## 5. Relation to the existing pretentious frontier

`MC-003` showed that Möbius and Liouville already share the critical `1/2` transfer threshold through their exact square convolution, so Liouville itself is not an easier RH-scale comparator. `MC-045`--`MC-046` then constructed scale-dependent exact-support multiplicative perturbations that ordinary one-scale pretentious distance fails to detect, while `MC-047` showed that Jung--Lemke Oliver's strong power-aware carrier does detect those perturbations at the correct target normalization. `MC-048` quantified why the older prime-only beta-pretentious Cauchy transfer overpays the same terminal-prime mass.

The present result addresses a different residual question left after that chain: could one avoid the strong transfer metric altogether by finding a **fixed completely multiplicative function** whose power cancellation is independently tractable and which is merely globally close to Liouville in the ordinary `1/p` pretentious metric?

Within the real bounded class, the answer is negative in a precise sense. If the global ordinary distance is finite, the power-saving estimate itself makes `F(1)` well-defined and the Euler ratio forces it to vanish; Aymone then turns the proposed comparator estimate directly into a zeta zero-free region of the same exponent. At the RH scale, the comparator estimate is therefore already an RH-level theorem.

This does not contradict `MC-045`: its `nu_X` is a scale-dependent family rather than one fixed completely multiplicative function, and it is not completely multiplicative because of the Möbius square-free factor. Nor does it say ordinary pretentious distance can transfer pointwise power cancellation between arbitrary fixed multiplicative functions. It says something weaker but strategically decisive: in this particular completely multiplicative Liouville-like class, **existence of the independently power-cancellative comparator already constrains zeta zeros**, so the hoped-for easier object cannot be certified without paying the zero-free burden somewhere in the proof.

## 6. Prior art and novelty boundary

Theorem 1.1 of Aymone (`MC-S33`) is the decisive source. It sharpens an earlier theorem of Koukoulopoulos on completely multiplicative functions small on average and proves both the weighted prime discrepancy `(4)` and the zero-free consequence `(16)`. No novelty is claimed for those statements, for Landau's nonnegative-coefficient mechanism, or for the relation `L_lambda(s)=zeta(2s)/zeta(s)`.

Venturini (`MC-S17`) is adjacent prior art for the broader principle that analyticity and a zero at `1` of a bounded completely multiplicative Dirichlet series can force zeta nonvanishing. `MC-008` already used that literature to distinguish zero-divisor fidelity from absolute convolution inversion in a different, non-completely-multiplicative comparator.

A targeted literature check also found Koukoulopoulos's 2013 predecessor and the later Koukoulopoulos--Soundararajan structural theory of multiplicative functions with small partial sums. These reinforce that the small-average/pretentiousness direction is established analytic-number-theory territory. Accordingly, the finding is stored as a `CLASSICAL-MECHANISM` plus an exact line-specific corollary, with **no standalone novelty claim**.

The only derived addition is the reverse half of `(2)`: under `(1)`, finite global ordinary distance to Liouville makes the Euler ratio `(11)` finite and nonzero at `1`, hence forces `F(1)=0`. Together with Aymone's theorem, this identifies the source's analytic hypothesis and global Liouville pretentiousness as equivalent conditions in the power-cancellative class.

## 7. Consequence for the next comparator search

After `MC-048`, a surviving pretentious-style route was to find an arithmetic comparator with independently controlled cancellation and a relation to Möbius/Liouville that does not carry the RH burden unchanged. This finding rules out one broad version of that idea:

> a fixed real completely multiplicative comparator with power cancellation and finite global ordinary Liouville distance is not independently cheaper at the corresponding exponent; its existence already forces the matching zeta zero-free region.

A genuinely different comparator route must therefore violate at least one essential input of the obstruction or add structure not represented by comparator partial sums alone. Plausible remaining categories include multiplicative-but-not-completely-multiplicative square-free-supported objects, complex-valued comparators outside Aymone's real class, signed convolution/bilinear mechanisms that do not rely on a single comparator summatory estimate, or relations that are local/multiscale rather than finite global ordinary Liouville distance.

The useful falsification test is now explicit: whenever a proposed fixed completely multiplicative real comparator is claimed to be both Liouville-like and easier to cancel, first ask whether its prime values make `sum_p (1+f(p))/p` finite. If yes, any exponent `1-delta` proved for its summatory function already certifies zeta zero-freeness in `Re(s)>1-delta`; the comparator has relocated the target rather than weakened it.