# MC-226 — Quantitative polynomial Möbius uniformity still misses the selected first-shell source slice

**Status:** `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-221`–`MC-225` reduce the current first square-defect bottleneck to selected Möbius sums

\[
A_d(T)
=
\sum_{\substack{r\le X/d^2\\(r,P)=1}}
\mu(d^2r-P)
\quad\text{up to the exact lower endpoint,}
\qquad
P=\prod_{p\le y}p,
\qquad
y=c\log X,
\tag{1}
\]

for primes `d\asymp y`, together with the diagonal-scale energy target

\[
W_y(X)
:=
\sum_{y<d\le2y\atop d\ \mathrm{prime}}
 d\,|A_d(T)|^2
\le X^{1+o(1)}.
\tag{2}
\]

A particularly close piece of current prior art is Matthiesen--Teräväinen--Wang, *Quantitative asymptotics for polynomial patterns in the primes*, Mathematika 72 (2026), e70103, DOI `10.1112/mtk.70103`, first published 12 May 2026. Their Theorems 1.2 and 1.3 prove arbitrary fixed powers of logarithmic cancellation for Möbius products along polynomial progressions, including one-dimensional estimates after averaging the remaining translation parameter.

That theorem does **not** supply `(2)`, for three independent and quantitatively visible reasons.

### 1. The useful one-dimensional estimate is averaged over the translation, while the square-defect source selects one translation

For fixed integral polynomials `P_1,...,P_k` of maximal degree `D`, their Theorem 1.3(1) gives, under its dominant-degree-difference hypothesis, a bound of the form

\[
\frac1{N^{D+1}}
\sum_{n\le N^D}
\left|
\sum_{m\le N}
\prod_{j=1}^k\mu(n+P_j(m))
\right|
\ll_A (\log N)^{-A},
\tag{3}
\]

and the companion estimate with the roles of `m` and `n` averaged in the opposite order. Thus the theorem gives strong **average** control over translations `n`, but does not give a uniform estimate for a prescribed translation.

Already for a single first-shell coordinate one may use the even extension of Möbius and write

\[
\mu(d^2r-P)=\mu(P-d^2r).
\tag{4}
\]

Taking the polynomial `Q_d(r)=-d^2r`, the Mathia source is the specific translation

\[
n=P,
\tag{5}
\]

not a generic or averaged `n`. Since `P=X^{c+o(1)}` with `c<1/2` while the natural `r`-length is `N\asymp X/d^2=X^{1-o(1)}`, this selected translation lies well inside the range over which an almost-all theorem could average. But `(3)` gives no reason that this highly structured primorial translation is not one of the exceptional slices.

Markov's inequality can convert `(3)` into a small exceptional **set** of translations after choosing a threshold, but it cannot certify the one predetermined translation `(5)`. This is exactly the source-selection issue isolated independently in `MC-224` and `MC-225`: averaging a family is not enough when the arithmetic construction chooses one distinguished coordinate before the estimate is applied.

### 2. Even a typical-slice logarithmic gain is far above the required power scale

There is a second obstruction before exceptional translations are considered. For `k=1`, `(3)` says on average that a length-`N` Möbius polynomial sum has size at most

\[
\frac{N}{(\log N)^A}
\tag{6}
\]

at any fixed requested logarithmic power. For the first shell, `N\asymp X/d^2=X^{1-o(1)}`. Hence `(6)` is still

\[
X^{1-o(1)},
\tag{7}
\]

whereas the first-shell energy `(2)` requires square-root-scale signed balance: `MC-221` calibrates the needed relative parity bias as `X^{-1/2+o(1)}` across an unsigned population of size `X^{1-o(1)}`.

No fixed logarithmic saving can bridge that fixed-power gap:

\[
(\log X)^{-A}=X^{-o(1)},
\tag{8}
\]

while the missing amplitude is of order `X^{-1/2+o(1)}`. Thus even an oracle assertion that the selected translation `(5)` behaved like a typical translation at the theorem's stated strength would still not prove `(2)`.

This is a theorem-strength issue, not a criticism of the result. Matthiesen--Teräväinen--Wang explicitly obtain arbitrary powers of logarithm, matching the natural Siegel--Walfisz scale of their problem. The Mathia first shell asks for a different power budget.

### 3. The off-diagonal source lies outside the direct fixed-polynomial theorem in either natural orientation

Expanding `(2)` gives the two-point source from `MC-209`,

\[
\mu(d^2r-P)\mu(d^2(r+h)-P).
\tag{9}
\]

There are two natural ways to compare `(9)` with the polynomial-pattern theorem.

**Freeze `d` and average in `r`.** The two polynomials are parallel linear forms

\[
P_1(r)=d^2r,
\qquad
P_2(r)=d^2(r+h).
\tag{10}
\]

Their difference is constant. Therefore for `k=2` they fail the hypothesis of Theorems 1.2/1.3(1) that one polynomial differ from the other in the full maximal degree. The paper explicitly allows some constant-difference pairs only when another polynomial supplies the required dominant degree; the bare two-point parallel pair `(10)` has no such third direction.

**Freeze `r,h` and average in `d`.** Then

\[
P_1(d)=r d^2,
\qquad
P_2(d)=(r+h)d^2,
\tag{11}
\]

and the degree-two difference condition is satisfied when `h\ne0`. But now the active averaging range is only

\[
N\asymp d\asymp y\asymp\log X,
\tag{12}
\]

while a typical coefficient is

\[
r\asymp \frac{X}{d^2}=X^{1-o(1)}.
\tag{13}
\]

The quantitative generalized von Neumann estimate used by the paper, Proposition 3.1, requires its leading coefficient `c_k` to satisfy

\[
|c_k|\le N^\eta
\tag{14}
\]

for a sufficiently small fixed `eta>0` depending on the degree. Equations `(12)`--`(13)` violate `(14)` by a fixed-power margin: every fixed power of `N\asymp\log X` is only `X^{o(1)}`.

So the variable orientation that makes the polynomial differences nondegenerate moves the source into a coefficient regime outside the theorem's quantitative engine. The orientation with long variable length keeps coefficients tame but turns the relevant two-point forms into parallel constant-difference forms and still leaves the translation `P` selected rather than averaged.

These two failures are complementary and mirror the variable-placement obstruction found for Banks--Shparlinski in `MC-225`.

## 1. Exact prior-art statement used here

Matthiesen, Teräväinen and Wang prove for fixed `k,D` and fixed integer polynomials `P_1,...,P_k` satisfying the stated dominant-degree condition that

\[
\left|
\frac1{N^{D+1}}
\sum_{n\le N^D}
\sum_{m\le N}
\prod_{j=1}^k\mu(n+P_j(m))
\right|
\ll_A (\log N)^{-A}
\tag{15}
\]

for every fixed `A>0`; Theorem 1.3(1) strengthens this to the two `L^1` one-dimensional-average estimates represented by `(3)`. Their Proposition 3.1 is more flexible than the fixed-polynomial headline statement and permits coefficients varying with `N`, but only inside the polynomial-size condition `(14)` together with comparable leading coefficients at maximal degree.

The distinction matters here. A superficial comparison might say that `(9)` is simply a quadratic polynomial Möbius correlation and therefore falls under the 2026 theorem. The scale audit shows why this is false: the square-defect source simultaneously requires a logarithmic quadratic variable, an `X^{1-o(1)}` coefficient/companion variable, and one primorial-selected translation.

The paper's result is therefore genuine adjacent prior art and not a black-box solution of the first shell.

## 2. Relation to the current first-shell frontier

`MC-224` showed that coefficient-uniform additive large-sieve control forgets the source-selected direction and remains at energy `X^{2-o(1)}`. `MC-225` showed that the current Banks--Shparlinski multiple-Möbius theorem either excludes the logarithmic polynomial variable or loses a full power when the variables are rearranged.

The present audit closes a different apparent escape. Modern Gowers-uniformity methods now give quantitative nonlinear polynomial Möbius cancellation, but their strongest directly stated conclusion is still logarithmic and averaged/fixed-complexity in exactly the coordinates where the square-defect source is singular.

The common obstruction can now be stated more sharply:

> the missing theorem must control a **source-selected, ultra-unbalanced polynomial Möbius slice at fixed-power strength**, not merely establish generic polynomial pseudorandomness after averaging the translation or keeping all polynomial coefficients within the averaging scale.

This does not imply that Gowers methods are irrelevant. An adaptation that exploits the exact lift `n+P=d^2r`, allows coefficients of size `X^{1-o(1)}` while the `d`-variable has logarithmic length, and controls the predetermined primorial translation could constitute genuinely new information not covered by this finding.

## 3. Prior-art and novelty boundary

Primary source:

Lilian Matthiesen, Joni Teräväinen and Mengdi Wang, *Quantitative asymptotics for polynomial patterns in the primes*, Mathematika 72 (2026), issue 3, e70103, DOI `10.1112/mtk.70103`; arXiv:2405.12190. The journal version was first published 12 May 2026.

Theorem 1.2 is the quantitative Möbius polynomial-pattern theorem. Theorem 1.3(1) is the one-dimensional `L^1` averaged strengthening. Proposition 3.1 supplies the coefficient-dependent generalized von Neumann interface and explicitly assumes `|c_k|\le N^eta` for sufficiently small `eta` in terms of the degree. All of those statements are literature facts; no novelty is claimed for them.

The durable Mathia contribution is only the source-specific applicability audit `(4)`--`(14)`: it identifies three distinct losses that prevent the 2026 theorem from supplying `MC-221`'s first-shell power budget. A targeted search of current nonlinear polynomial Möbius results found no published theorem in this family that simultaneously removes the selected-translation, power-saving and ultra-unbalanced-coefficient losses.

## 4. Boundaries and falsification tests

- The finding does not claim that the polynomials in the square-defect source are outside all Gowers-uniformity technology. It states only that the published theorem and its displayed quantitative engine do not give the needed bound directly.
- The fixed-polynomial wording of Theorems 1.2/1.3 is not used as the sole obstruction. Proposition 3.1 explicitly allows some coefficient growth, and `(14)` is the quantitative condition used for the ultra-unbalanced comparison.
- Equation `(3)` is an averaged bound, not a statement that an exceptional primorial translation actually exists. The obstruction is lack of certification of the predetermined translation, not evidence that it is bad.
- The logarithmic-saving comparison `(6)`--`(8)` is an exponent-budget statement. Allowing `A` to be any **fixed** constant never creates a fixed power of `X`; no claim is made about a theorem uniform in `A` growing with `X`.
- The parallel-form failure `(10)` concerns the two-point `k=2` use of Theorem 1.2/1.3(1). The theorem can allow some constant-difference pairs in larger collections when another full-degree difference satisfies its hypothesis.
- The original first-shell sum also contains the roughness restriction `(r,P)=1` and precise endpoints. Those extra structures are not used to manufacture the obstruction above; a successful adaptation would still have to preserve them.
- No conclusion about RH, GRH, or the actual size of `W_y(X)` follows from this prior-art audit.

The finding is falsified as a theorem-level audit if the published 2026 result contains a uniform corollary for a predetermined translation `n=P`, with coefficients in `(11)` of size `(13)` when `N\asymp\log X`, and with a fixed-power saving sufficient to reduce `(2)` to `X^{1+o(1)}`. None of those three properties is present in the cited statements.

## Consequence for the active frontier

Two of the strongest recent nonlinear Möbius technologies now sit immediately next to the first square-defect source: Banks--Shparlinski multiple sums (`MC-225`) and Matthiesen--Teräväinen--Wang polynomial-pattern uniformity (this finding). Both permit genuine nonlinear Möbius cancellation, yet both miss the same active regime from different directions.

The next useful attack should therefore preserve all three load-bearing features simultaneously:

1. the selected primorial source coordinate `-P mod d^2` or its exact lift `n+P=d^2r`;
2. the ultra-unbalanced scale `d\asymp\log X` against source variables of length `X^{1-o(1)}`;
3. fixed-power rather than merely logarithmic cancellation.

A theorem that averages away the source translation, requires all polynomial coefficients to live at the logarithmic variable scale, or supplies only `(log X)^{-A}` relative cancellation has not yet crossed the first-shell bottleneck.