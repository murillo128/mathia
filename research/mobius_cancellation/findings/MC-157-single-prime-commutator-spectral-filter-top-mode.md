# MC-157 — Single-prime commutator spectral filters have an exact top-mode dichotomy

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical number-state representation and the pulled-back prime commutator from `MC-156`:

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_n=\varepsilon_{pn},
\qquad
D_\mu\varepsilon_n=\mu(n)\varepsilon_n,
\]

\[
B_p:=S_p^*[D_\mu,S_p],
\qquad
B_p\varepsilon_n=b_p(n)\varepsilon_n,
\qquad
b_p(n)=\mu(pn)-\mu(n).
\tag{1}
\]

`MC-156` proves

\[
b_p(n)\in\{-2,-1,0,1,2\}
\tag{2}
\]

and that the complete signed coefficient field is already target-complete. The natural next attempt is therefore to retain only a scalar spectral quotient `g(B_p)` of this five-point alphabet.

For every **odd** function

\[
g:\{-2,-1,0,1,2\}\to\mathbb C,
\qquad g(-t)=-g(t),
\tag{3}
\]

put

\[
a:=g(2),
\qquad
c:=g(1),
\qquad
R_{p,g}(x):=\sum_{n\le x}g(b_p(n)).
\tag{4}
\]

Then the cumulative readout has the exact form

\[
\boxed{
R_{p,g}(x)
=-aM(x)-(a-c)\sum_{j\ge1}M(x/p^j),
}
\tag{5}
\]

where `M(y)=0` for `0\le y<1`, so the sum is finite for every `x`.

Consequently the coefficient of the **unsifted top-scale Mertens mode** is exactly

\[
\boxed{-g(2).}
\tag{6}
\]

This gives a sharp dichotomy for scalar signed spectral filters of one prime commutator:

1. if `g(2)=0`, the filter removes the top Mertens mode, but its entire signed prefix statistic lives on the lower-scale `p`-divisible sector;
2. if `g(2)\ne0`, the unsifted `M(x)` mode survives explicitly, plus only lower dilates.

The two canonical spectral projections make the boundary exact. Define

\[
g_{\rm in}(t)=\frac{4t-t^3}{3},
\qquad
g_{\rm out}(t)=\frac{t^3-t}{3}.
\tag{7}
\]

On the five-point spectrum,

\[
g_{\rm in}(\pm1)=\pm1,
\quad g_{\rm in}(0)=g_{\rm in}(\pm2)=0,
\tag{8}
\]

while

\[
g_{\rm out}(\pm2)=\pm2,
\quad g_{\rm out}(0)=g_{\rm out}(\pm1)=0.
\tag{9}
\]

Thus

\[
I_p:=g_{\rm in}(B_p),
\qquad
O_p:=g_{\rm out}(B_p),
\qquad
B_p=I_p+O_p.
\tag{10}
\]

Their diagonal coefficients are

\[
I_p(n)=-\mu(n)\mathbf 1_{p\mid n},
\qquad
O_p(n)=-2\mu(n)\mathbf 1_{p\nmid n}.
\tag{11}
\]

Writing

\[
J_p(x):=\sum_{n\le x}I_p(n),
\qquad
K_p(x):=\sum_{n\le x}O_p(n),
\tag{12}
\]

one obtains

\[
\boxed{
J_p(x)=\sum_{j\ge1}M(x/p^j),
}
\tag{13}
\]

and

\[
\boxed{
K_p(x)=-2\sum_{j\ge0}M(x/p^j).
}
\tag{14}
\]

The outer band is therefore Mertens-complete by a **two-scale difference**:

\[
\boxed{
M(x)=-\frac12\bigl(K_p(x)-K_p(x/p)\bigr).
}
\tag{15}
\]

For every fixed `\theta>0`,

\[
K_p(x)=O(x^\theta)
\quad\Longleftrightarrow\quad
M(x)=O(x^\theta).
\tag{16}
\]

In contrast, the inner band contains no unsifted term. Under a prior estimate

\[
M(y)=O(y^\beta),
\qquad \beta>0,
\tag{17}
\]

it satisfies

\[
|J_p(x)|
\ll_\beta
\frac{x^\beta}{p^\beta-1}.
\tag{18}
\]

If the prime is allowed to move with the observation scale,

\[
p=x^{\delta+o(1)},
\qquad 0<\delta<1,
\tag{19}
\]

then

\[
J_p(x)=O\!\left(x^{\beta(1-\delta)+o(1)}\right),
\tag{20}
\]

whereas `(15)` remains exact for the corresponding outer filter. The spectral split therefore exhibits the desired intermediate-quotient tradeoff in its cleanest form: **the canonically cheaper signed band is missing the top target, while the band retaining the top target is already Mertens-equivalent.**

This does not rule out every compressed relational statistic. It closes the entire class of scalar functional-calculus filters `g(B_p)` as a source of a free cancellation gain: their signed part either deletes the unsifted mode or keeps it with an explicit coefficient.

## 1. The five-point commutator alphabet separates divisibility and sign

From `MC-156`, there are exactly three cases:

\[
b_p(n)=
\begin{cases}
0,&\mu(n)=0,\\
-2\mu(n),&\mu(n)\ne0\text{ and }p\nmid n,\\
-\mu(n),&\mu(n)\ne0\text{ and }p\mid n.
\end{cases}
\tag{21}
\]

Hence an odd spectral function needs only its two positive values `a=g(2)` and `c=g(1)`. Equation `(21)` gives

\[
g(b_p(n))=
\begin{cases}
0,&\mu(n)=0,\\
-a\mu(n),&p\nmid n,\\
-c\mu(n),&p\mid n.
\end{cases}
\tag{22}
\]

Let

\[
A_p(x):=\sum_{\substack{n\le x\\p\mid n}}\mu(n).
\tag{23}
\]

Then

\[
R_{p,g}(x)
=-a\bigl(M(x)-A_p(x)\bigr)-cA_p(x)
=-aM(x)+(a-c)A_p(x).
\tag{24}
\]

It remains only to identify the `p`-divisible signed mass.

## 2. The p-divisible signed mass is an exact lower-dilation tail

Define

\[
F_p(x):=\sum_{n\le x}\mu(pn).
\tag{25}
\]

Splitting the summation according to `p\mid n` and using square-free support gives

\[
F_p(x)=-M(x)+F_p(x/p).
\tag{26}
\]

Indeed, if `p\nmid n`, then `\mu(pn)=-\mu(n)`, while for `p\mid n` the nonzero terms in `\mu(n)` are precisely shifted into the next `p`-divisible layer of the recurrence. Iterating `(26)` terminates after finitely many steps:

\[
F_p(x)=-\sum_{j\ge0}M(x/p^j).
\tag{27}
\]

Because

\[
A_p(x)=F_p(x/p),
\tag{28}
\]

we get

\[
\boxed{
A_p(x)=-\sum_{j\ge1}M(x/p^j).
}
\tag{29}
\]

Substituting `(29)` into `(24)` proves `(5)`.

This identity is entirely discrete. It uses neither `1/\zeta(s)`, Perron inversion, contour shifting, analytic continuation, nor a zero-free region.

## 3. Canonical inner and outer spectral filters realize the two extremes

The polynomials in `(7)` are the Lagrange spectral selectors for the two nonzero magnitude bands of `B_p`. Direct evaluation gives `(8)` and `(9)` and also

\[
g_{\rm in}(t)+g_{\rm out}(t)=t.
\tag{30}
\]

Therefore `(10)` is an exact operator decomposition.

For the inner filter, `a=0`, `c=1`, so `(5)` becomes `(13)`. This part keeps Möbius sign, but only on the `p`-divisible shell. Its apparent cheapness is precisely the loss of the unsifted layer, not a new estimate for that layer.

For the outer filter, `a=2`, `c=0`, so `(5)` becomes `(14)`. Applying `(14)` once at `x` and once at `x/p` cancels every lower-dilation term and leaves

\[
K_p(x)-K_p(x/p)=-2M(x),
\tag{31}
\]

which proves `(15)`.

Thus neither half of the most canonical signed spectral quotient gives the hoped-for intermediate carrier:

- the inner half is structurally cheaper because it has removed the top mode;
- the outer half retains the top mode and recovers it exactly by one dilation difference.

The split is not a statement about numerical size alone. It identifies which arithmetic layer each spectral band actually retains.

## 4. Quantitative exponent consequences

Assume `(17)` with constant `C`. From `(13)`,

\[
|J_p(x)|
\le Cx^\beta\sum_{j\ge1}p^{-j\beta}
=\frac{C x^\beta}{p^\beta-1},
\tag{32}
\]

which is `(18)`. For fixed `p`, this is a genuine lower-scale identity but only a constant-factor saving at the same exponent. A polynomial exponent saving appears only for a moving prime family as in `(19)`, yielding `(20)`.

For the outer filter, `(14)` gives

\[
|K_p(x)|
\le \frac{2C}{1-p^{-\beta}}x^\beta.
\tag{33}
\]

Conversely, if `|K_p(y)|\le D y^\beta`, then `(15)` gives

\[
|M(x)|
\le \frac D2\left(x^\beta+(x/p)^\beta\right)
\le \frac D2(1+p^{-\beta})x^\beta.
\tag{34}
\]

This proves `(16)`. In particular, the RH-scale family

\[
K_p(x)=O_\varepsilon(x^{1/2+\varepsilon})
\tag{35}
\]

is no easier than the standard Mertens criterion: `(15)` converts it back to that criterion with no loss of exponent.

## 5. General scalar functional calculus: even part is support, odd part obeys the top-mode rule

Any scalar function `h` on the spectrum `(2)` splits uniquely into even and odd parts. The even part depends only on

\[
|b_p(n)|\in\{0,1,2\},
\tag{36}
\]

so it sees square-free support and whether `p` divides the square-free state, but not the Möbius orientation. Such even readouts are therefore unsuitable by themselves for first-order signed Mertens cancellation; this is the same support/orientation distinction that already appears throughout `MC-138`–`MC-155`.

The odd part is exhausted by `(5)`: after prefix aggregation, all of its signed arithmetic information enters through only two pieces, the unsifted `M(x)` mode with coefficient `-g(2)` and the lower-dilation tail with coefficient `-(g(2)-g(1))`.

Therefore `(6)` is a fast kill test for every proposed scalar spectral filter of `B_p`. If a construction chooses `g(2)=0` to remove target leakage, it must explain how lower dilates alone regenerate a genuinely stronger top-scale estimate without simply undoing that quotient. If it keeps `g(2)\ne0`, it must show a new cancellation mechanism involving the explicit top mode rather than treating the filtered statistic as independently cheaper by construction.

## Prior art and novelty assessment

The Bost–Connes semigroup representation, its canonical isometries, and the relevant operator-algebraic setting are established prior art already audited in `MC-138`–`MC-156`. The weighted-shift commutator calculation `(1)` and the exact five-point coefficient classification `(21)` are persisted in `MC-149` and `MC-156`. Polynomial functional calculus on a finite spectrum and the local multiplicative rules for `\mu` are elementary classical tools.

A targeted literature search for Bost–Connes/prime-semigroup commutators combined with Möbius spectral projections or cumulative spectral-band identities recovered the standard Bost–Connes/operator-algebra setting but did not locate `(5)`–`(15)` as a named theorem. That absence is **not** used as evidence of novelty. The present result is an exact line-level synthesis of already-audited source structure with elementary finite spectral calculus, so no novelty claim is made.

The substantive delta relative to `MC-156` is not a new ambient operator. `MC-156` showed that the complete signed coefficient table overshoots by reconstructing `D_\mu` pointwise. The present result classifies the most immediate lossy alternative — scalar functional calculus before prefix aggregation — and proves exactly where the top Mertens mode goes.

There is a close structural analogy with `MC-090`, where a gcd-sieve split of the Huxley–Watt carrier makes one component lower-scale while the retained component keeps the unsifted top mode. The objects and derivations are different: `MC-090` is a divisor-sieve decomposition of a bilinear sawtooth form, while `(5)` is a complete finite-spectrum classification of one prime commutator. The recurrence of the same top-mode tradeoff is therefore evidence for a line-level obstruction pattern, not a claim that the two constructions are identical.

## Boundaries and falsification tests

- **Scalar functional calculus only.** The theorem classifies `g(B_p)` for a single commutator followed by ordinary prefix aggregation. Joint noncommutative words in several primes, matrix-valued filters, non-scalar conditional expectations, or relational statistics coupling different states are outside `(5)`.
- **Odd filters carry the cancellation statement.** Even filters may be useful as support controls but cannot by themselves distinguish the sign of `\mu(n)`.
- **A fixed prime does not improve an exponent in the inner band.** Equation `(18)` is a lower-scale/constant-factor reduction for fixed `p`; the exponent saving `(20)` requires a moving prime family and must not be quoted otherwise.
- **The outer-band equivalence is exact and unconditional.** No zero information enters `(15)`. A counterexample to `(15)` would refute the derivation directly.
- **No RH progress is claimed.** The theorem says which filtered readouts are cheaper or target-complete; it supplies no new bound for the surviving top mode.
- **Moving-prime use changes the family, not the algebra.** Each `p` is already a canonical prime isometry, but choosing `p=p(x)` is a scale-dependent readout and any future mechanism must justify uniformity across that family.
- **Relational compression remains live.** A quotient that mixes inner and outer bands before scalarization, couples different primes/scales, or retains a source-forced signed relation without reconstructing the pointwise coefficient table can evade this theorem. It still has to survive the existing biased/support-matched controls and prove an anchored Mertens transfer.

The decisive falsification test is finite: evaluate any proposed scalar spectral function on the five values `{-2,-1,0,1,2}`. Its odd part must satisfy `(5)`. A single admissible spectral filter whose cumulative signed readout cannot be written in that form would refute the classification.

## Consequence for the research line

The immediate post-`MC-156` question was whether a natural lossy spectral quotient of one signed commutator could sit between cancellation-blind scalar norms and the target-complete coefficient table. For **scalar functional calculus**, the answer is now exact and negative.

The canonical spectral split shows both failure modes simultaneously: the `|b|=1` band can become polynomially cheaper along moving primes only because it omits the unsifted top mode, while the `|b|=2` band recovers `M(x)` by the two-scale identity `(15)`. More generally, `g(2)` is the top-mode coefficient for every odd scalar spectral filter.

A surviving semigroup route must therefore leave this one-variable spectral quotient class. The next admissible carrier must use a genuinely relational signed coupling — across bands, primes, scales, or states — whose compression is demonstrably weaker than pointwise recovery and whose quantitative transfer to `M(x)` does not simply preserve the unsifted target with nonzero coefficient.