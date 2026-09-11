# MC-225 — Current multiple-sum Möbius bounds miss the first square-defect shell in the ultra-unbalanced variable regime

**Status:** `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-221`–`MC-224` isolate the active first square-defect shell as a family of selected arithmetic-progression sums

\[
A_d(T)=\sum_{\substack{n\le T\\ n\equiv-P\pmod{d^2}}}
\mu(n)\mathbf 1_{(n,P)=1},
\qquad y<d\le 2y,
\qquad y=c\log X,
\tag{1}
\]

with the required energy scale

\[
W_y(X)=\sum_{d}d|A_d(T)|^2\le X^{1+o(1)}.
\tag{2}
\]

The natural source lift is

\[
n=d^2m-P,
\tag{3}
\]

so after expanding `(2)` one is led to coupled Möbius products whose source variables satisfy quadratic additive relations. This is structurally close to the 2026 theorem of Banks and Shparlinski on multiple sums with the Möbius function. Their framework controls sums of the form

\[
\sum_{f(n_1)+g(n_2)+\wp(n_3)=M}
 u_{n_1}v_{n_2}\,\mu(n_1n_2n_3),
\tag{4}
\]

where `f,g` are injective and `wp` is a bracket polynomial. However, a direct scale audit shows that the theorem does **not** supply the missing first-shell power cancellation. The obstruction is not the quadratic polynomial itself. It is the extreme imbalance between the logarithmic square-root variable `d\asymp\log X` and the source variables of length `X^{1-o(1)}`, together with the selected moving residue retained by `(1)`.

There are two natural ways to place the variables into `(4)`, and each exposes a different failure.

1. If `d` is the polynomial variable, the potentially useful orientation has two long variables `a,b\asymp X` and

\[
a-b-cd^2=0,
\qquad d\asymp y\asymp\log X.
\tag{5}
\]

Banks--Shparlinski Theorem 2.1 requires, in their notation,

\[
\log N\ge (\log\max\{A,B\})^{\varepsilon}
\tag{6}
\]

for some fixed `epsilon>0`. Here `N\asymp y\asymp\log X` while `A,B\asymp X`, so

\[
\log N\asymp\log\log X
=o((\log X)^\varepsilon).
\tag{7}
\]

Thus the useful orientation lies outside the theorem's scale range. Their dedicated one-small-variable application reaches variables as short as

\[
H\ge \exp((\log X)^\varepsilon),
\tag{8}
\]

for fixed positive `epsilon`, still asymptotically much larger than `H\asymp\log X`. Their short-interval Theorem 2.4 does not repair this mismatch: besides its lower bound on the short interval, it requires the other interval lengths to be polynomially bounded in the scale of that short variable, which fails when those lengths are `X^{1-o(1)}` and the short scale is logarithmic.

2. If instead `d` is moved into one of the two weighted injective variables, the hypotheses can be satisfied, but the generic theorem loses the power budget before using any arithmetic. For fixed `c`, take

\[
f(d)=cd^2,
\qquad g(a)=-a,
\qquad \wp(b)=b,
\tag{9}
\]

and let the weight on `d` restrict it to primes in `(y,2y]`. With interval lengths

\[
A\asymp y,
\qquad B\asymp N\asymp X,
\tag{10}
\]

Theorem 2.1 gives, for every fixed `C`, a bound of shape

\[
(A+B)N(\log N)^{-C}
=X^{2-o(1)},
\tag{11}
\]

whereas the theorem's own trivial counting bound is

\[
\min\{A,B\}N\asymp X\log X=X^{1+o(1)}.
\tag{12}
\]

No fixed logarithmic saving in `(11)` overcomes the missing factor `X/log X`. Hence the direct admissible orientation is asymptotically weaker than trivial counting at fixed-power resolution. This is the same exponent-level symptom seen from a different representation in `MC-224`: a generic norm theorem can be very strong in its balanced regime while remaining one full power too coarse for the logarithmic first shell.

The actual square-defect source is narrower still. If one fixes an off-diagonal source difference `h=m_1-m_2`, writes

\[
n_i=d^2m_i-P,
\qquad g=\gcd(n_1,n_2),
\tag{13}
\]

and restricts to nonzero Möbius terms, then `d\nmid n_i`, so `d\nmid g`; because `g\mid n_1-n_2=d^2h`, one has `g\mid h`. Writing `n_1=ga`, `n_2=gb`, square-freeness gives

\[
(a,b)=1,
\qquad (g,ab)=1,
\qquad a-b=\frac hg d^2,
\tag{14}
\]

and

\[
\mu(n_1)\mu(n_2)=\mu(ab)=-\mu(abd)
\tag{15}
\]

because `d` is prime and coprime to `ab`. This produces exactly the product-Möbius sign occurring in `(4)`. But the selected source coordinate also imposes

\[
gb\equiv-P\pmod{d^2},
\qquad	ext{equivalently}\qquad
b\equiv-Pg^{-1}\pmod{d^2},
\tag{16}
\]

in addition to the quadratic difference relation. A signed bound for the relaxed equation `(14)` cannot simply be restricted to `(16)`: cancellation on the discarded residue classes may be essential.

Therefore the recent multiple-sum theory is unusually close to the active Mathia source mechanism, but it lands on the wrong side of the exact bottleneck. To affect `(2)`, an adaptation would have to retain useful cancellation when the quadratic coupling variable has only logarithmic length, or find a source-specific factorization/rebalancing that avoids the loss `(11)` **while still preserving the selected residue `(16)`**. None of those upgrades follows from the published theorem.

No improved bound for `W_y(X)`, `A_d(T)`, `M(X)`, or the zeta zero set is claimed.

## 1. Exact source dictionary behind the quadratic relation

The source representation `(3)` is forced by the selected congruence in `(1)`. Since `d>y`, one has `(d,P)=1`; therefore

\[
(d^2m-P,P)=1\iff(m,P)=1.
\tag{17}
\]

Consequently the first-shell coordinate may be written directly as a Möbius sum along the affine source polynomial `d^2m-P`, with a roughness condition on `m`. Squaring it produces pairs

\[
(d^2m_1-P,\ d^2m_2-P)
\tag{18}
\]

whose difference is exactly `d^2(m_1-m_2)`.

For a nonzero pair contribution both integers are square-free. Let `g` be their gcd. The congruence `n_i\equiv-P mod d` and `(d,P)=1` implies `d\nmid g`. Hence `g|h`, and division by the exact gcd produces `(14)` with all common square-free factors removed. The sign identity `(15)` is then exact, not heuristic: the common factor contributes twice and cancels from the Möbius parity, while adjoining the prime `d` flips the remaining sign once.

This is the precise reason Banks--Shparlinski is relevant prior art rather than a merely verbal analogy. After gcd stripping, the off-diagonal source really does expose a product Möbius weight on variables satisfying an additive equation with the quadratic polynomial `d^2`. The extra selected congruence `(16)` and extreme variable scales are what prevent a black-box application.

## 2. Why changing the variable placement does not solve the scale problem

Banks--Shparlinski's Theorem 2.1 has two features that matter here. First, the polynomial may be an ordinary polynomial of any fixed complexity, so `cd^2` is admissible. Second, only the first two variables carry arbitrary bounded weights, while the third variable is the argument of the polynomial and enters the Möbius product directly.

Putting `d` in the third slot is analytically natural because then the theorem's output would be proportional to the short `d`-length. But the scale separation `(7)` violates the theorem's long-interval hypothesis. This is not a cosmetic endpoint issue: Section 7.6 of the paper explicitly identifies `H=1` as a Chowla-type boundary and obtains nontrivial estimates only when the small third variable grows at least like `exp((log X)^epsilon)`.

Putting `d` in the first slot avoids that hypothesis because `f(d)=cd^2` is allowed to be injective and the long `b` variable can occupy the polynomial slot. But the theorem then measures the two weighted intervals through `(A+B)`, not through their minimum. When `A\asymp\log X` and `B\asymp X`, that replacement is precisely a lost factor of order `X/log X` compared with the trivial number of solutions. Arbitrarily strong fixed logarithmic savings cannot compensate for it.

This leaves open a non-black-box use of the authors' proof architecture. A decomposition that genuinely balances the long variables, a dispersion step that gains from the selected residue, or another source factorization might change the ledger. The present finding rules out only the direct theorem-level import.

## 3. Prior art and novelty audit

The primary source is William D. Banks and Igor E. Shparlinski, *Multiple sums with the Möbius function*, Quarterly Journal of Mathematics 77 (2026), no. 1, 109–127, DOI `10.1093/qmath/haaf049`; accessible preprint arXiv:2506.08787.

Their Theorem 2.1 proves the general long-interval bound `(4)` under the scale condition summarized in `(6)`. Theorem 2.4 treats a short third interval but retains polynomial comparability requirements among the other lengths. Section 7.6 studies the model with one small variable, states that the `H=1` case remains a Chowla-type problem, and records the unconditional range `H>=exp((log N)^epsilon)` up to notation. The paper also emphasizes that binary analogues remain out of reach. These are literature facts; no novelty is claimed for the Banks--Shparlinski theorem or its limitations.

The contribution here is only the line-specific dictionary and power audit: equations `(13)`--`(16)` identify the first square-defect off-diagonal source with a selected-residue subfamily of the same product-Möbius/additive-polynomial architecture, and `(7)`/`(11)` show that both direct variable placements miss the Mathia scale for complementary reasons. A targeted search for Möbius multiple sums, square-modulus arithmetic progressions, and current short-variable results found no theorem that removes both losses at the logarithmic first-shell scale.

This finding also sharpens the relationship to `MC-209` and `MC-224`. `MC-209` already identifies the off-diagonal shell as an aggregated shifted-Möbius problem, while `MC-224` rules out coefficient-uniform large-sieve averaging at the required power. Banks--Shparlinski supplies a modern source-coupled alternative to inspect; the present audit shows that its current theorem is not yet the missing signed family estimate.

## 4. Boundaries and falsification tests

- The decomposition `(13)`--`(16)` applies only to nonzero Möbius pair terms; zero terms disappear from the energy expansion and therefore require no gcd sign identity.
- The exact gcd `g` may vary with the pair. The scale discussion is already decisive on the `g=1` sector, where the long variables remain of size `X^{1-o(1)}`; no claim is made that every large-`g` subrange violates the same numerical hypothesis.
- The relaxed Banks--Shparlinski sum does not impose `(16)`. A bound for the relaxed signed sum does not bound the selected subfamily by monotonicity, because there is no positivity.
- Equation `(11)` is a direct application-scale estimate, not a lower bound for the theorem or for every possible use of its proof. Rebalancing or additional factorization could in principle create a genuinely different application.
- The theorem allows a quadratic polynomial unconditionally; the obstruction here must not be misstated as a degree-two or bracket-polynomial barrier.
- The Section 7.6 threshold is a theorem range, not an impossibility theorem below that range. The point is that current prior art does not reach `H\asymp\log X`, not that no future method can.
- No inference from the paper to RH is made. Its conditional refinements under zero-free hypotheses are prior-art context only and are not imported into the first-shell argument.

The scale audit is falsified if Theorem 2.1 actually permits `N\asymp\log X` together with `A,B\asymp X` under its stated fixed-`epsilon` hypothesis, or if the admissible placement `(9)` yields a fixed-power improvement over the trivial `O(X\log X)` solution count. The source dictionary is falsified by any nonzero Möbius pair for which exact gcd stripping fails to give `(14)`--`(16)`.

## Consequence for the active frontier

The first-shell frontier is now more specific than “find a bilinear estimate.” A current theorem designed precisely for Möbius weights on additive polynomial relations already exists, but its useful range stops before the logarithmic coupling variable that the square-defect geometry forces. Moving that variable into an admissible weighted slot restores the hypotheses only by losing the same full power that `MC-224` could not afford.

The next source-coupled attack should therefore be judged against a sharper requirement: it must produce a **nontrivial estimate in an ultra-unbalanced quadratic relation with `d\asymp\log X`, while retaining or exploiting the selected residue `-P mod d^2`**. A result that handles only balanced three-variable sums, only a relaxed all-residue relation, or only logarithmic savings after replacing the short interval by the long one has not crossed the first-shell bottleneck.