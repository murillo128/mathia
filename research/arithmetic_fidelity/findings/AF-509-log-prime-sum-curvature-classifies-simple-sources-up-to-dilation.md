# AF-509 — Log-prime-sum curvature classifies simple sources up to dilation

## Status

`LITERATURE+DERIVED` · `EXACT-DERIVED` · `ARITHMETIC-FIDELITY` · `QUOTIENT-CLASSIFICATION` · `DIRICHLET-SOURCE` · `GIBBS-VARIANCE` · `SOURCE-ANCHOR` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
Q=\{q_1<q_2<\cdots\},\qquad 1<q_1,\qquad q_n\to\infty,
\]

be a simple locally finite positive source whose prime/Dirichlet sum

\[
P_Q(s)=\sum_{n\ge1}q_n^{-s}
\]

converges absolutely on a real half-line `s>\sigma_0`. Define the log-curvature profile

\[
\kappa_Q(s):=\frac{d^2}{ds^2}\log P_Q(s).
\tag{1}
\]

For every such source, normalize the exponentially tilted weights

\[
\mu_{Q,s}(q_n)=\frac{q_n^{-s}}{P_Q(s)}.
\tag{2}
\]

Then

\[
\boxed{
\kappa_Q(s)=\operatorname{Var}_{\mu_{Q,s}}(\log q).
}
\tag{3}
\]

More importantly, on the class of **simple unit-weight sources**, the complete curvature profile forgets exactly one structural degree of freedom: common multiplicative scale.

If `Q` and `R` have a common absolute-convergence half-line, then the following are equivalent:

\[
\boxed{
\kappa_Q(s)=\kappa_R(s)
\text{ on one nonempty open interval}
\iff
R=cQ:=\{cq:q\in Q\}
\text{ for some }c>0.
}
\tag{4}
\]

Thus

\[
Q\longmapsto \kappa_Q(\cdot)
\]

is an exact quotient by global dilation, not a generic many-source compression.

The missing scale can be restored by one natural scalar. For example,

\[
m_Q:=\lim_{s\to\infty}-\frac{d}{ds}\log P_Q(s)=\log q_1,
\tag{5}
\]

so the enriched observation `(\kappa_Q,m_Q)` recovers `Q` exactly.

There is also an arithmetic way to eliminate the same gauge without recording a numerical anchor. If both sources consist of ordinary positive integers and are **primitive** in the sense

\[
\gcd\{q:q\in Q\}=\gcd\{r:r\in R\}=1,
\tag{6}
\]

then `(4)` forces `c=1`, hence `Q=R`. In particular, if `\mathbb P` is the rational-prime source, then among primitive simple integer sources,

\[
\boxed{
\kappa_R=\kappa_{\mathbb P}
\text{ on any open interval in }(1,\infty)
\Longrightarrow
R=\mathbb P.
}
\tag{7}
\]

This supplies a concrete Arithmetic Fidelity example in which a substantial compression—discarding the level and slope of `\log P_Q`—still preserves the complete source modulo a one-dimensional gauge, while a natural arithmetic source restriction pins that gauge.

## Derivation

### 1. The curvature is the tilted log-norm variance

Absolute convergence on `s>\sigma_0` permits termwise differentiation there. Put `X(q)=\log q`. Then

\[
P_Q'(s)=-\sum_q X(q)q^{-s},
\qquad
P_Q''(s)=\sum_q X(q)^2q^{-s}.
\]

Therefore

\[
\begin{aligned}
(\log P_Q)'(s)
&=-\mathbb E_{\mu_{Q,s}}X,\\
(\log P_Q)''(s)
&=\mathbb E_{\mu_{Q,s}}X^2-
  \big(\mathbb E_{\mu_{Q,s}}X\big)^2,
\end{aligned}
\]

which is `(3)`. This is the standard cumulant/exponential-tilting identity: the second derivative of a log-Laplace transform is the variance in the associated natural exponential family.

A common dilation `q\mapsto cq` translates every log norm by the same constant `\log c`. At the Dirichlet-sum level,

\[
P_{cQ}(s)=c^{-s}P_Q(s),
\tag{8}
\]

so

\[
\log P_{cQ}(s)=\log P_Q(s)-s\log c
\]

and hence

\[
\boxed{\kappa_{cQ}(s)=\kappa_Q(s).}
\tag{9}
\]

The invariance therefore has both a probabilistic meaning—variance ignores translation—and an exact analytic meaning—two derivatives erase the affine scale term.

### 2. Equal curvature leaves only an affine log-Laplace ambiguity

Assume `\kappa_Q=\kappa_R` on a nonempty open interval `I` inside the common convergence half-line. Then

\[
\frac{d^2}{ds^2}
\big(\log P_R(s)-\log P_Q(s)\big)=0
\qquad(s\in I).
\]

Hence there are real constants `a,b` such that

\[
\log P_R(s)-\log P_Q(s)=a+bs
\qquad(s\in I),
\]

or

\[
P_R(s)=e^a e^{bs}P_Q(s).
\tag{10}
\]

Both sides extend holomorphically to their common absolute-convergence half-plane, so the identity theorem extends `(10)` throughout that half-plane. Set

\[
c=e^{-b}>0.
\]

Using `(8)`, equation `(10)` becomes

\[
P_R(s)=e^a P_{cQ}(s).
\tag{11}
\]

Thus the only ambiguity left by the curvature before using the unit-weight source structure is a translation of the log-support together with a common positive rescaling of the underlying counting measure.

### 3. Simple unit weights kill the common mass factor

Write `R=\{r_1<r_2<\cdots\}` and `cQ=\{cq_1<cq_2<\cdots\}`. Take `(11)` along real `s\to\infty`.

The smallest exponent dominates each positive Dirichlet sum:

\[
P_R(s)=r_1^{-s}(1+o(1)),
\qquad
P_{cQ}(s)=(cq_1)^{-s}(1+o(1)).
\tag{12}
\]

Equality `(11)` first forces the exponential rates to agree,

\[
r_1=cq_1.
\tag{13}
\]

After `(13)`, dividing by the common leading exponential and taking the limit forces its coefficient to agree. Both sources have unit coefficient at their first simple atom, so

\[
e^a=1.
\tag{14}
\]

Equation `(11)` is therefore the exact equality

\[
P_R=P_{cQ}.
\tag{15}
\]

The standard uniqueness argument for positive discrete generalized Dirichlet sums, already used in AF-017, now gives equality of supports. Equivalently, subtract the common first term from `(15)` and repeat the leading-exponent argument inductively. Hence

\[
R=cQ,
\]

proving the forward implication in `(4)`. The reverse implication is exactly `(9)`.

This identifies the whole fiber of the compression, not merely a sufficient family of collisions.

### 4. One scalar restores exact recovery

From `(12)`,

\[
\log P_Q(s)=-s\log q_1+o(s)
\]

and differentiation of the tilted mean gives the sharper standard limit

\[
-(\log P_Q)'(s)
=\mathbb E_{\mu_{Q,s}}\log q
\longrightarrow\log q_1.
\tag{16}
\]

Under dilation,

\[
m_{cQ}=m_Q+\log c.
\tag{17}
\]

Therefore two sources with the same `\kappa` and the same `m` have `R=cQ` by `(4)` and then `c=1` by `(17)`. So `(\kappa,m)` is faithful on the simple unit-weight source class.

This is a genuine lift rather than a restatement of the full function: `\kappa` has discarded two affine integration constants of `\log P`, but the unit-mass structure already eliminates the constant-amplitude freedom, leaving only one global support-translation parameter. One scalar source anchor is exactly sufficient to pin that remaining orbit.

### 5. Primitive integer support pins the scale structurally

Suppose `Q,R\subset\mathbb Z_{\ge2}` are primitive and `R=cQ`. Since `cq\in\mathbb Z` for any fixed `q\in Q`, `c` is rational. Write `c=a/b` in lowest terms with positive integers `a,b`.

Because `cq` is an integer for every `q\in Q`, the denominator `b` divides every element of `Q`. Primitivity of `Q` therefore forces `b=1`, so `c=a` is a positive integer. But then

\[
\gcd(R)=a\,\gcd(Q)=a.
\]

Primitivity of `R` forces `a=1`. Hence

\[
\boxed{c=1.}
\tag{18}
\]

The rational primes satisfy the primitive condition because `\gcd(2,3)=1`. This proves `(7)`.

The point is not that integrality magically follows from the curvature. It does not. The point is category-sensitive: **once exact primitive integer support is an independently justified source constraint, the only collision left by the curvature quotient is inadmissible.**

## Matched controls and relation to the current prime-provenance frontier

The unrestricted source category has an exact matched control for every `c>0`, `c\ne1`:

\[
Q\ne cQ,
\qquad
\kappa_Q=\kappa_{cQ}.
\tag{19}
\]

For the rational primes this gives, for example, `\mathbb P` and `\sqrt2\,\mathbb P`. They have identical tilted log-norm variance profiles despite different generator norms. Therefore `\kappa` alone is not rational-prime faithful in the unrestricted Beurling/real-norm category.

But `(4)` says that there are **no other** collisions among simple unit-weight sources. This is substantially different from the finite-sample situation of AF-484. There, any finite family of exact prime-zeta values can be preserved by nonintegral density-matched Beurling controls through an infinite-dimensional deformation. Here an exact curvature profile on one open interval is analytic infinite data, and its entire fiber collapses to the one-dimensional dilation orbit.

The two results are therefore compatible and mark a useful information boundary:

\[
\text{finitely many exact prime-zeta samples}
\quad\text{leave large source freedom},
\]

whereas

\[
\text{the full log-curvature profile on an open interval}
\quad\text{leaves only global scale}.
\]

No claim is made that finitely many curvature values, finitely many derivatives, or noisy curvature samples have the same rigidity. Those are separate conditioning/finite-information questions.

AF-368 and AF-369 also remain load bearing. Scalar counting proximity, even at arbitrarily small `O(\log x)` error, does not supply primitive integer support. Conversely, AF-369 shows another category in which exact integer-supported structure plus one scalar normalization restores the rational-prime discriminator. AF-509 gives a different realization of the same broader lesson: **the fidelity of an analytic compression and the rigidity of the admitted source class must be audited jointly.**

## Prior art and novelty assessment

The mathematical ingredients are classical, and no novelty is claimed for them.

- The identity `d^2\log L/ds^2 = \operatorname{Var}_s(X)` is standard cumulant / natural-exponential-family theory. The *Encyclopedia of Mathematics* article **“Natural exponential family of probability distributions”** records the Hessian/variance relation for the cumulant transform and the classical fact that variance data determine the associated natural exponential family. Standard Esscher/exponential-tilting treatments give the same identity directly.
- G. H. Hardy and Marcel Riesz, ***The General Theory of Dirichlet's Series***, Cambridge Tracts in Mathematics and Mathematical Physics 18 (1915), is the classical background for generalized Dirichlet series and uniqueness in a half-plane of convergence. Modern accounts use the same frequency-series framework.
- David V. Widder, ***The Laplace Transform***, Princeton University Press (1941), is a classical source for Laplace-transform representation and uniqueness. The present discrete unit-mass proof needs only the elementary leading-exponent argument.
- AF-017 already established inside Arithmetic Fidelity that an exact positive prime Dirichlet/Laplace sum determines its locally finite generator-norm multiset. The present proof reuses that uniqueness boundary after identifying exactly which affine information the curvature has removed.

The durable Arithmetic Fidelity delta is the **exact fiber classification for this particular compression** and its arithmetic specialization. Instead of saying only that a second derivative loses affine information, `(4)` proves that, on simple unit-weight Dirichlet sources, it loses *nothing else*: equal tilted-variance profiles are exactly common dilations. Equation `(18)` then shows that primitive integer support removes that sole gauge and makes the curvature profile rational-prime faithful relative to that source class.

This should be read as a classical log-Laplace/exponential-family mechanism applied to the prime-provenance problem, not as a new theorem in probability, generalized Dirichlet series, or analytic number theory.

## Boundaries and failure modes

- **Simple unit weights are load bearing.** For a general positive discrete measure, equality of log-Laplace curvature determines the measure only up to support translation and an overall positive mass factor. Repeated atoms or arbitrary weights can retain the `e^a` ambiguity in `(11)`. The unit coefficient at each simple source atom is what forces `e^a=1`.
- **The observation is an exact profile, not finite data.** Equality on one open interval suffices by analyticity, but equality at finitely many points does not. AF-484 is therefore not contradicted, and no finite-sample or noisy recovery theorem is claimed.
- **The source-class anchor is real information.** Primitive integer support is not derivable from `\kappa`. It is an independent admissibility restriction. Dropping it immediately restores the dilation controls `(19)`.
- **Integrality without primitivity is insufficient.** If `Q` is integer valued, then integer dilations such as `2Q` remain integer valued and have the same curvature. The gcd normalization, or another independently justified scale anchor, is essential.
- **The result uses the prime/Dirichlet sum, not the meromorphic zero divisor.** Nothing here shows that `\kappa_Q` can be reconstructed from zeros alone, nor does it evade the same-divisor controls of AF-017 or AF-369.
- **No analytic continuation is needed.** All claims live in a common absolute-convergence half-plane. The open-interval identity is propagated only inside that domain.
- **Conditioning is unresolved.** Exact quotient rigidity can coexist with severe instability when `\kappa` is known approximately or only on a bounded finite grid. Quantitative inverse stability requires a separate theorem.
- **No RH consequence follows.** The theorem concerns source provenance. It neither constrains Riemann-zero locations nor supplies a route from the curvature profile to the critical line.

## Decisive audit test

For any proposed matched control against the full profile `\kappa_Q`, first check the declared source category.

If the sources are simple unit-weight generalized primes and the profiles agree on an open interval, the control must be a common dilation. A purported non-dilation control would contradict `(4)` and should be rejected or traced to a violated hypothesis such as weights, multiplicities, finite sampling, or approximate equality.

If the target is specifically the rational-prime source and the admissible controls are primitive integer sources, the dilation fiber is already trivial by `(18)`. Conversely, in an unrestricted real-norm category, a common dilation is an immediate exact falsifier of rational-prime identity from `\kappa` alone.

## Consequence for the research line

AF-509 supplies an exact positive model of the line's central question: a nontrivial compression can forget a visible source feature without destroying every source discriminator. The second derivative of `\log P_Q` removes absolute log-origin and function normalization, yet the simple-source category forces the remaining fiber to be precisely one dilation orbit.

For the current prime-provenance frontier this gives a sharp three-layer separation. Finite prime-zeta samples are too weak by AF-484; the full tilted-variance profile is strong enough to recover a simple source modulo scale; and primitive integer support pins that scale and therefore distinguishes the rational primes exactly within that declared class.

The next quantitative question is no longer whether full curvature is exactly faithful modulo dilation—it is—but how much of that profile can be discarded or corrupted before non-dilation controls reappear, and whether any such finite/noisy regime remains compatible with a natural arithmetic source gate.