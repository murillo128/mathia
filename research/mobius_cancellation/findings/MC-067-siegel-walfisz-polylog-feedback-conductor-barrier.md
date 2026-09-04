# MC-067 — Siegel–Walfisz excludes every polylogarithmic conductor from the positive signed-feedback bootstrap

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the square-free quadratic comparator of `MC-066`. Let `q` be an odd prime,

\[
\chi(n)=\left(\frac{n}{q}\right),
\qquad
f_\chi(n)=\mu(n)^2\chi(n),
\qquad
h_\chi=1*f_\chi,
\]

and recall the exact local coefficients

\[
h_\chi(p^a)=
\begin{cases}
0,&\chi(p)=-1,\\
2,&\chi(p)=+1,\\
1,&p=q,
\end{cases}
\qquad a\ge1.
\tag{1}
\]

For `0<theta<1`, define the positive feedback budget

\[
R_\theta(X;\chi)
:=
\sum_{2\le d\le X}\frac{h_\chi(d)}{d^\theta}.
\tag{2}
\]

Fix `B>0` and `eta>0`. Uniformly for prime conductors

\[
q\le (\log X)^B
\tag{3}
\]

and exponents

\[
0<\theta\le 1-\eta,
\tag{4}
\]

the Siegel–Walfisz theorem implies, for all sufficiently large `X` depending on `B` and `eta`,

\[
\boxed{
R_\theta(X;\chi)
\gg_B
\frac{X^{1-\theta}}{\log X}
\ge
\frac{X^\eta}{\log X}.
}
\tag{5}
\]

In particular,

\[
\boxed{R_\theta(X;\chi)>1}
\tag{6}
\]

throughout the whole polylogarithmic-conductor regime once `X` is large enough. Therefore the positive-kernel triangle bootstrap isolated in `MC-066`, which requires `R_theta(X;chi)<1`, cannot use a conductor bounded by any fixed power of `log X` at any exponent separated from `1`.

Equivalently, if a sequence of moving quadratic characters closes that bootstrap at a fixed `theta<1` for arbitrarily large `X`, then its conductors must eventually satisfy

\[
\boxed{
q(X)>(\log X)^B
\quad\text{for every fixed }B>0.
}
\tag{7}
\]

So the phrase "genuinely moving" in `MC-066` can be sharpened: the conductor must be **super-polylogarithmic**, not merely unbounded.

Coupling this with the classical Munsch/Burgess comparator certificate from `MC-064`--`MC-066` produces a narrow asymptotic corridor. If one tries to certify a near-critical family

\[
|F_\chi(X)|=X^{1/2+o(1)}
\]

using only the displayed Munsch bound

\[
|F_\chi(X)|
\ll
X^{1/2}q^{3/16}(\log X)(\log q)^{1/2},
\tag{8}
\]

then that certificate requires

\[
q=X^{o(1)}.
\tag{9}
\]

Thus a near-critical implementation of this exact architecture can live only in the intermediate regime

\[
\boxed{
(\log X)^{\omega(1)}<q<X^{o(1)}.
}
\tag{10}
\]

Equation `(10)` is a **method-specific search corridor**, not an existence statement. It says that the two classical sides of the same proposed bootstrap squeeze the conductor from opposite directions: Siegel–Walfisz kills every fixed polylogarithmic scale through the feedback term, while the Munsch/Burgess certificate becomes non-critical when the conductor has a fixed positive power of `X`.

No new estimate for `M(X)` is claimed.

## 1. Split primes already force a large positive feedback term

For every prime `p!=q` with `chi(p)=+1`, equation `(1)` gives

\[
h_\chi(p)=2.
\]

Since every term of `R_theta` is nonnegative,

\[
R_\theta(X;\chi)
\ge
2\sum_{\substack{p\le X\\ \chi(p)=+1}}p^{-\theta}.
\tag{11}
\]

The obstruction therefore needs only a lower bound for quadratic-residue primes in one terminal interval. It does not require an Euler-product approximation for the full kernel, estimates for composite `d`, or any inversion of the recurrence in `MC-066`.

Put

\[
\vartheta_+(x;\chi)
:=
\sum_{\substack{p\le x\\ \chi(p)=+1}}\log p.
\tag{12}
\]

There are exactly `(q-1)/2` reduced residue classes modulo the prime `q` on which the quadratic character equals `+1`. The Siegel–Walfisz theorem in `MC-S15` gives, for every fixed power `C>0`, uniformly for `q<=(log x)^C` and every reduced residue class `a mod q`,

\[
\vartheta(x;q,a)
=
\frac{x}{q-1}
+O_C\!\left(xe^{-c\sqrt{\log x}}\right),
\tag{13}
\]

with the usual ineffective threshold coming from Siegel's theorem. Summing `(13)` over the `(q-1)/2` split classes yields

\[
\vartheta_+(x;\chi)
=
\frac{x}{2}
+O_C\!\left(qx e^{-c\sqrt{\log x}}\right)
=
\frac{x}{2}+o_C(x)
\tag{14}
\]

uniformly when `q<=(log x)^C`.

If `(3)` holds at `X`, then for large `X` it also lies inside a Siegel–Walfisz range at `X/2` after increasing the fixed logarithmic exponent, for example from `B` to `B+1`. Hence `(14)` at `X` and `X/2` gives

\[
\sum_{\substack{X/2<p\le X\\ \chi(p)=+1}}\log p
=
\frac{X}{4}+o_B(X).
\tag{15}
\]

For all sufficiently large `X`, the left side is at least `X/5`. Since every prime in the interval has `log p<=log X`,

\[
\#\{X/2<p\le X:\chi(p)=+1\}
\ge
\frac{X}{5\log X}.
\tag{16}
\]

Every such prime also satisfies `p^{-theta}>=X^{-theta}`. Inserting `(16)` into `(11)` gives the explicit asymptotic lower bound

\[
R_\theta(X;\chi)
\ge
\frac{2}{5}\frac{X^{1-\theta}}{\log X},
\tag{17}
\]

once `X` is large enough. Under `(4)`, this is at least `(2/5)X^eta/log X`, proving `(5)`--`(6)`.

The key point is that the obstruction comes from **terminal split primes**. A small conductor has already entered the uniform prime-distribution regime by the time the feedback is evaluated at scale `X`, so the split-prime population cannot remain sparse enough for a positive `p^{-theta}` kernel to be contractive.

## 2. Why this is stronger than the fixed-character observation in MC-066

`MC-066` already noted that a fixed nonprincipal quadratic character cannot keep `R_theta(X;chi)` bounded for `theta<1`, because split primes occupy positive-density residue classes asymptotically. That statement by itself leaves open conductors that grow slowly with `X`: the asymptotic threshold for a different character at every scale could in principle move faster than the observation point.

Siegel–Walfisz is exactly the uniformity needed to close that loophole for

\[
q\le(\log X)^B
\]

with arbitrary fixed `B`. Equation `(17)` is uniform across every prime conductor in that range. Therefore neither a fixed character, a logarithmically growing conductor, nor any fixed polylogarithmic conductor can satisfy the positive-feedback contraction required by `(9)` of `MC-066`.

This does not extend automatically to `q=X^delta`. Siegel–Walfisz is deliberately a polylogarithmic-modulus theorem, and possible exceptional-zero effects are part of why uniform prime distribution at polynomially growing moduli is a different problem. The surviving corridor in `(10)` is therefore not an artifact to be erased by silently extrapolating `(13)` beyond its valid range.

## 3. The Munsch side supplies the opposite pressure near the critical exponent

For prime `q`, `MC-S38` gives

\[
|F_\chi(X)|
\ll
X^{1/2}q^{3/16}(\log X)(\log q)^{1/2}.
\tag{18}
\]

At a fixed target `theta=1/2+epsilon`, this displayed theorem can certify

\[
|F_\chi(X)|\le X^{\theta+o(1)}
\]

only in the conductor range

\[
q\le X^{16\varepsilon/3+o(1)}.
\tag{19}
\]

For a near-critical target whose excess exponent tends to zero, the same certificate therefore requires `q=X^{o(1)}`. Equation `(7)` simultaneously requires `q` to dominate every fixed power of `log X` if the positive feedback is to contract. This gives `(10)`.

The word "requires" here is certificate-specific. A conductor larger than `(19)` might have an unusually small true squarefree character sum; Munsch's upper bound would simply no longer certify it at the desired exponent. Likewise a different squarefree-character theorem with better conductor dependence would alter the upper side of the corridor.

The lower side is tied instead to the positive feedback architecture itself. Any replacement theorem that still closes `MC-066` by demanding `R_theta<1` must confront `(17)` in the Siegel–Walfisz range.

## 4. Prior art and novelty boundary

The analytic input is classical. `MC-S15` anchors Montgomery and Vaughan, *Multiplicative Number Theory I: Classical Theory*, Chapters 4 and 11. Chapter 11 proves the Siegel–Walfisz theorem and its corresponding uniform estimates for `vartheta(x;q,a)` and `pi(x;q,a)` for `q<=(log x)^A`. No novelty is claimed for `(13)`--`(16)`, for the equidistribution of split prime residue classes, or for the fact that the theorem is ineffective at its uniform threshold.

`MC-S38` is Munsch's classical squarefree-character estimate and supplies `(18)`. The local identity `h_chi(p)=2` on split primes and the feedback recurrence are already persisted in `MC-066`.

The retained line-specific content is the coupling of these two classical boundaries to the exact feedback carrier: uniform split-prime equidistribution turns the qualitative "moving character" escape of `MC-066` into the quantitative super-polylogarithmic lower bound `(7)`, and the Munsch certificate supplies the opposite near-critical subpolynomial pressure `(9)`. This is stored as a derived obstruction and search-space reduction, not as a new theorem of analytic number theory.

A targeted prior-art check around small prime quadratic residues, prime character sums, and uniform primes in arithmetic progressions found the expected Burgess/Linnik/Siegel–Walfisz literature. Those results do not justify extending `(17)` to general polynomial conductors. Conversely, least-prime-residue results alone are weaker than the terminal population estimate needed here; the useful input is uniform distribution of a positive proportion of split primes once the modulus is polylogarithmic in the observation scale.

## 5. Boundaries and falsification tests

The conclusion is deliberately restricted to the positive-kernel triangle bootstrap of `MC-066`.

- `R_theta` is nonnegative, so the prime-only lower bound `(11)` is exact and cannot be repaired by cancellation among composite kernel coefficients. But a future argument that preserves the signs of the terms `h_chi(d) M(X/d)` instead of bounding them by `R_theta` lies outside this obstruction.
- The uniform statement uses `theta<=1-eta`. It says nothing when `theta` approaches `1` so quickly that `X^(1-theta)/log X` stays bounded. This boundary is irrelevant to the intended Mertens/RH exponents near `1/2` but is mathematically real.
- The threshold inherited from Siegel–Walfisz is ineffective. Equation `(5)` is asymptotic and is not a finite numerical exclusion for a specified `X` and `q`.
- The conductor is prime and the character is the quadratic comparator used by `MC-064`--`MC-066`. The same argument extends to fixed-index character value classes when the relevant residue classes are uniformly equidistributed, but that generalization is not needed here.
- Equation `(10)` is not a proof that useful conductors in the intermediate corridor exist. It is the intersection of two necessary search conditions for this specific classical certificate package.
- No zero-free theorem for the Riemann zeta function, no RH-equivalent Mertens estimate, and no continuation of `1/zeta(s)` enters the derivation.

A counterexample to the exact claim would need a sequence of prime moduli `q<=(log X)^B` for which the split-prime terminal interval violates the Siegel–Walfisz consequence `(15)`, or a failure of the local identity `h_chi(p)=2` on split primes. The classical theorem and the coefficient identity exclude those possibilities.

## Consequence for the active frontier

The simplest signed quadratic-comparator escape is now squeezed more sharply. Moving the conductor below the prefix did remove the specific `X/q` absolute-fidelity floor of `MC-065`, but moving it **too far down** makes the positive feedback kernel noncontractive for a different reason: by the terminal scale, Siegel–Walfisz has forced roughly half the primes into the split classes, and their `p^{-theta}` mass alone already diverges polynomially.

A surviving near-critical character bootstrap must therefore either operate with conductors in the genuinely intermediate super-polylogarithmic/subpolynomial regime, obtain a comparator theorem stronger than the Munsch/Burgess certificate, or exploit signed cancellation among the feedback terms so that `R_theta<1` is no longer the closure mechanism. Merely choosing a very small moving conductor cannot close the gap.