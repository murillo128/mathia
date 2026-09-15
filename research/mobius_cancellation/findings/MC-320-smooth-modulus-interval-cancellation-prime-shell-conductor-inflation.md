# MC-320 — Smooth common-modulus interval cancellation is blind to a maximally biased prime shell under conductor inflation

**Status:** `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `NEGATIVE/OBSTRUCTION` · `MATCHED-CONTROL` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-319` isolates a precise remaining analytic gap in the reciprocal endpoint program. At the exact natural source scale, all relevant Legendre characters can be induced to one very smooth common modulus `q=4P`, but the available smooth-modulus Rodosskii estimate controls broad power intervals at harmonic scale much coarser than the one-dyadic-shell signal required by the endpoint.

A tempting next move is to replace the Rodosskii estimate by the much stronger short **integer** character-sum estimates available for smooth moduli and then try to transfer that cancellation to the primes. The following explicit control shows that modulus-level interval cancellation, even at essentially perfect strength, is not by itself the missing information.

Let `R=R(y)` satisfy

\[
R\to\infty,
\qquad
R=O(\log\log y),
\tag{1}
\]

and put

\[
X=y^{1/(2R)},
\qquad
Z=y^{1/R}=X^2.
\tag{2}
\]

For all sufficiently large `y`, choose `2R` distinct odd primes

\[
p_1,\ldots,p_{2R}\in[X,2X]
\tag{3}
\]

and define

\[
P=\prod_{j=1}^{2R}p_j,
\qquad
q=4P.
\tag{4}
\]

Then

\[
y\le P\le y4^R=y(\log y)^{O(1)},
\qquad
P^+(q)\le2X\le Z
\tag{5}
\]

for large `y`. Thus this control has the same first-order common-modulus geometry as the live natural-scale endpoint package: exactly `2R` lower-prime coordinates, a common odd squarefree radical of shell scale up to polylogarithmic slack, and largest source prime below `y^{1/R}`.

Now let `\widetilde\chi_4` be the Dirichlet character modulo `q` induced from the primitive nonprincipal character `\chi_4` modulo `4`:

\[
\widetilde\chi_4(n)
=\chi_4(n)\mathbf 1_{(n,P)=1}.
\tag{6}
\]

Its primitive conductor is only `4`; the factors of `P` inflate the ambient modulus but do not belong to the primitive character. This single distinction is decisive.

First, `\widetilde\chi_4` has extremely strong unweighted interval cancellation. For every real `M` and `H\ge1`, inclusion-exclusion gives

\[
\sum_{M<n\le M+H}\widetilde\chi_4(n)
=
\sum_{d\mid P}\mu(d)\chi_4(d)
\sum_{M/d<m\le(M+H)/d}\chi_4(m).
\tag{7}
\]

Every interval sum of `\chi_4` is bounded absolutely by `2`, because its period has zero total. Hence

\[
\boxed{
\left|\sum_{M<n\le M+H}\widetilde\chi_4(n)\right|
\le2\tau(P)
=2^{2R+1}.
}
\tag{8}
\]

At the critical rank `R\asymp\log\log y`, the right-hand side is only a fixed power of `\log y`. In particular, for every fixed `\alpha>0`,

\[
\sup_{M,\,H\ge y^\alpha}
\frac1H
\left|\sum_{M<n\le M+H}\widetilde\chi_4(n)\right|
\longrightarrow0.
\tag{9}
\]

So the control is uniformly pseudorandom in ordinary integer intervals at every fixed polynomial scale.

Nevertheless it has **maximal** bias on the exact prime shell used by the endpoint program. Let

\[
\mathcal R_y
=\{r:y<r\le2y,\ r\text{ prime},\ r\equiv1\pmod4\}.
\tag{10}
\]

All prime factors of `P` are below `y`, so every `r\in\mathcal R_y` is coprime to `P`; and `\chi_4(r)=1`. Therefore

\[
\boxed{
\widetilde\chi_4(r)=1
\quad\text{for every }r\in\mathcal R_y.
}
\tag{11}
\]

The fixed-modulus prime number theorem in arithmetic progressions then gives

\[
\boxed{
\sum_{r\in\mathcal R_y}
\widetilde\chi_4(r)\log r
=
\frac12y+o(y),
}
\tag{12}
\]

and partial summation gives the harmonic-scale version

\[
\boxed{
\sum_{r\in\mathcal R_y}
\frac{\widetilde\chi_4(r)}r
=
\frac{\log2}{2\log y}
+o\!\left(\frac1{\log y}\right).
}
\tag{13}
\]

Equation `(13)` is exactly the scale that `MC-319` identified as decisive for a one-dyadic-shell endpoint character. Thus a character can simultaneously have polylogarithmically bounded sums on **every ordinary interval** and a maximal `1/\log y` harmonic signal on the restricted prime shell.

This is not a counterexample to the endpoint source-character problem, because `\widetilde\chi_4` has primitive conductor `4` rather than a high-cost lower-prime conductor. It is a sharper no-go against a specific analytic escape:

\[
\boxed{
\text{common-modulus smoothness + unweighted interval cancellation}
\not\Rightarrow
\text{dyadic prime-shell cancellation}
}
\tag{14}
\]

when primitive conductor/source provenance is discarded.

Accordingly, the residual route after `MC-319` must retain at least one genuinely prime-sensitive or provenance-sensitive datum: the primitive conductor of the endpoint character, its actual lower-prime source representation, a family relation among the primitive characters, or direct control of a `\Lambda`/prime-weighted sum. Replacing the Rodosskii estimate by a black-box theorem for `\sum\chi(n)` over smooth common moduli cannot by itself close the endpoint.

No estimate for `M(x)` follows.

## 1. A source-scale-matched inflated modulus exists

Under `(1)`,

\[
\log X=\frac{\log y}{2R}\longrightarrow\infty.
\tag{15}
\]

The prime number theorem implies

\[
\pi(2X)-\pi(X)\sim\frac{X}{\log X},
\tag{16}
\]

and the right-hand side dominates `R` overwhelmingly in the regime `(1)`. Hence `(3)` is possible for all sufficiently large `y`.

Multiplying the lower and upper bounds in `(3)` gives

\[
X^{2R}\le P\le(2X)^{2R},
\]

which is precisely the first part of `(5)`. Since `R=O(\log\log y)`,

\[
4^R=(\log y)^{O(1)}.
\tag{17}
\]

Also `X\to\infty`, so eventually `2X\le X^2=Z`. Thus the ambient modulus does not escape the natural source-scale regime merely by hiding a huge prime factor or by using more than `2R` lower-prime coordinates.

The control is intentionally sharper than a generic primorial inflation. It matches the live endpoint package in the two coarse quantities that drove `MC-314` and `MC-319`: source count `n=2R` and largest source prime `Z\le y^{1/R}`. What it does **not** match is the provenance of the character itself.

## 2. Inclusion-exclusion proves interval cancellation without any zero-free theorem

Because `P` is odd and squarefree,

\[
\mathbf1_{(n,P)=1}
=\sum_{d\mid(n,P)}\mu(d).
\tag{18}
\]

Insert `(18)` into `(6)` and interchange the finite sums. If `d\mid P`, then `d` is odd and complete multiplicativity of `\chi_4` gives

\[
\chi_4(dm)=\chi_4(d)\chi_4(m).
\tag{19}
\]

This yields `(7)` exactly.

The values of `\chi_4` over any four consecutive integers sum to zero, so every interval sum is bounded by an absolute constant; `2` is sufficient. Since `P` has exactly `2R` prime factors,

\[
\tau(P)=2^{2R},
\]

and `(8)` follows.

This is stronger for the present comparator than what is needed from the smooth-modulus literature. Klurman--Mangerel--Teräväinen, *Multiplicative functions in short arithmetic progressions* (PLMS 127 (2023), Lemma 10.1; source `MC-S45`), prove for a general nonprincipal character modulo a sufficiently smooth `q` the much deeper estimate

\[
\left|\sum_{M<n\le M+N}\chi(n)\right|
\ll
N\exp\!\left(-\frac14\sqrt{\log N}\right)
\tag{20}
\]

once `P^+(q)\le N^{0.001}` and `N\ge q^{C/\log\log q}`. The family `(4)` also eventually satisfies those hypotheses for every `N\ge y^\alpha` with fixed `\alpha>0`. But `(8)` shows that no quantitative sharpening of `(20)` at the level of ordinary interval discrepancy can repair the information loss exposed here: the control already has far stronger interval cancellation and still has `(11)`--`(13)`.

## 3. The prime restriction sees information that interval discrepancy forgot

The mechanism is elementary but diagnostic. The induced character is periodic modulo the large common modulus `q`, yet its primitive arithmetic content is just `\chi_4`. The factor

\[
\mathbf1_{(n,P)=1}
\tag{21}
\]

removes integers divisible by the inflated lower-prime package. Inclusion-exclusion then cancels ordinary interval sums using only the zero-mean period of `\chi_4`.

The shell `(10)` performs a very different operation. It first restricts to primes and then to the `1 mod 4` class. Every selected prime automatically avoids the lower-prime factors of `P`, and the mod-4 restriction freezes the primitive character to the value `+1`. The same character therefore looks maximally balanced to the integer-interval observable `(8)` and maximally unbalanced to the shell-prime observable `(11)`.

This is a concrete representation-loss example inside the exact scale of the live branch. The common modulus `q` remembers which integers are removed by divisibility, but an unweighted interval norm does not remember whether the surviving sign pattern is concentrated on primes in one residue class.

## 4. Relation to the MC-319 barrier

`MC-319` used the exact endpoint package to obtain a very smooth common modulus and then applied the KMT/Chang zero-free machinery to the relevant character family. The remaining failure was resolution: the Rodosskii estimate controls a broad power interval, whereas the endpoint needs one dyadic prime shell at harmonic scale `1/\log y`.

The present control rules out one superficially natural repair. KMT Lemma 10.1 and the Graham--Ringrose/Chang smooth-modulus character-sum technology behind it concern ordinary character sums. Even if such an estimate is made extremely strong, `(8)`--`(13)` show that **modulus-level interval cancellation is the wrong observable** unless an additional theorem converts primitive source information into prime-weighted cancellation.

The distinction between ambient modulus and primitive conductor is therefore load-bearing. The endpoint characters in `MC-296`--`MC-319` arise from actual lower-prime Legendre source products; their primitive conductors carry source cost. The comparator deliberately erases that provenance by inducing a conductor-`4` character to the same type of large smooth modulus. A successful continuation must exploit the feature that this comparator lacks rather than only improving a theorem that treats both as characters modulo the same `q`.

## 5. Prior art and novelty boundary

No new character-sum theorem is claimed. Equation `(7)` is ordinary Möbius inclusion-exclusion, and the bounded partial sums of `\chi_4` are immediate from periodicity. Equations `(12)`--`(13)` are the classical prime number theorem/Mertens asymptotic in the fixed progression `1 mod 4`.

The smooth-modulus comparison `(20)` is Klurman, Mangerel and Teräväinen, source `MC-S45`; their Lemma 10.1 is explicitly uniform over nonprincipal characters modulo `q` and does not require the character to be primitive. Their paper uses smooth-conductor character-sum and zero-free machinery from Graham--Ringrose, Chang and related work.

A targeted literature audit on 16 September 2026 found the ingredients separately but no need for a novelty claim: the durable result is the Mathia-specific matched-control composition showing exactly which datum must survive the transition from the common smooth modulus to the dyadic prime shell. **No standalone novelty claim is made.**

## Boundaries and falsification tests

- **The comparator is imprimitive by design.** Its primitive conductor is `4`. It does not refute a theorem that genuinely uses the high primitive conductors/source costs of the endpoint characters.
- **The match is at common-modulus/source-package scale, not character provenance.** Equations `(3)`--`(5)` match `n=2R`, shell-scale radical size up to polylogarithmic slack, and the natural largest-source-prime cap. The selected `p_j` do not generate the primitive character.
- **The `1 mod 4` shell restriction is essential to maximality.** Without it, `\chi_4` changes sign across prime residue classes. This is precisely why a prime-sensitive theorem must retain the actual shell projector rather than infer from unweighted intervals.
- **The result does not show that KMT Lemma 10.1 is useless.** It remains valuable inside arguments that combine interval cancellation with additional primitive-conductor, convolution, or prime-sensitive structure. What fails is using the interval estimate as the decisive endpoint discriminator by itself.
- **No contradiction with MC-319 is claimed.** The endpoint characters there have different primitive provenance. This finding narrows the residual theorem surface; it does not settle the arithmetic endpoint.
- **No statement about Möbius partial sums follows.** The result is local to the character/Frobenius realizability branch.

## Consequence for the research line

The analytic frontier after `MC-319` is now sharper. The missing theorem cannot merely say that characters modulo the smooth common `q` have small sums on short or long integer intervals: an explicit `2R`-source, natural-scale inflated-modulus control satisfies a much stronger property while retaining a maximal shell-prime signal of the exact required size.

The next useful discriminator must therefore be **primitive-source aware and prime sensitive**. A concrete target is a dyadic estimate for

\[
\sum_{y<p\le2y}\chi(p)\log p
\quad\text{or}\quad
\sum_{y<p\le2y}\frac{\chi(p)}p
\tag{22}
\]

that uses the primitive conductor/source-cost spectrum of the actual endpoint characters (possibly collectively), not just the smoothness of an ambient common modulus. This is the feature the conductor-inflation control cannot fake.