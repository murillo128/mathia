# MC-325 — Sparse even-layer averaging saturates the quartic source floor

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint partition and common lower-prime source package used in `MC-301`, `MC-323`, and `MC-324`. Let

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\qquad R\to\infty,
\tag{1}
\]

with exact endpoint profile

\[
x_{\lambda_I}
=(-1)^{|I|}\left(1-\frac{2|I|}{R}\right),
\qquad
\lambda_I:=\sum_{i\in I}\lambda_i.
\tag{2}
\]

Fix common lower-prime product representatives

\[
V_i\subseteq U
\qquad(1\le i\le R),
\tag{3}
\]

and put

\[
P:=\prod_{p\in U}p.
\tag{4}
\]

Let `r=r(R)` be any even integer sequence satisfying

\[
2\le r=o(\sqrt R).
\tag{5}
\]

For every `r`-subset `I\subseteq[R]`, define the package representative

\[
V_I:=\mathop{\triangle}_{i\in I}V_i,
\qquad
m_I:=\prod_{p\in V_I}p.
\tag{6}
\]

Then the straightforward extension of the `MC-324` pair argument to the full Hamming layer `|I|=r` **cannot improve the quartic common-source exponent**. More precisely, for every fixed `\delta\in(0,2)`, the varying-modulus prime Halász--Montgomery obstruction of `MC-323` gives

\[
\log P
\ge
\left(\frac{2-\delta}{1/2+\binom r2/R}\right)
\left(1-O_\delta\!\left(\binom Rr^{-1}\right)\right)
\log y,
\tag{7}
\]

for all sufficiently large `y` along the endpoint regime. Consequently,

\[
\boxed{
\liminf_{y\to\infty}\frac{\log P}{\log y}\ge4.
}
\tag{8}
\]

But the coefficient `1/2` in `(7)` is asymptotically **best possible for any universal columnwise incidence bound on these sparse even layers**:

\[
\boxed{
\sup_{0\le a\le R}
\frac{B_{R,r}(a)}{\binom Rr}
=\frac12+o(1),
}
\tag{9}
\]

where

\[
B_{R,r}(a)
:=
\sum_{\substack{0\le j\le r\\ j\ \mathrm{odd}}}
\binom aj\binom{R-a}{r-j}
\tag{10}
\]

counts the `r`-subsets meeting a fixed `a`-element source column in odd parity.

Thus **all sparse even endpoint layers have the same asymptotic source-mass ceiling under this proof architecture**. Increasing from pairs to `4`-modes, `6`-modes, or any even `r=o(\sqrt R)` supplies vastly more fixed-bias characters, but each source coordinate participates in asymptotically one half of the layer, so the extra character count cancels from the averaged conductor inequality. The quadratic individual-conductor horizon from `MC-323` and the asymptotic one-half parity-incidence ceiling multiply to the same quartic package floor already obtained from pairs in `MC-324`.

This is a no-go for a **specific higher-layer amplification mechanism**, not for higher endpoint modes in general. To beat exponent `4`, a future argument must use information not reducible to independent lower bounds for individual mode conductors plus a universal single-layer column-incidence count. No estimate for `M(x)` follows.

## 1. Every sparse even layer retains fixed shell bias

For `|I|=r`, equation `(2)` gives

\[
x_{\lambda_I}
=1-\frac{2r}{R},
\tag{11}
\]

because `r` is even. Under `(5)`, `r/R\to0`, so for all sufficiently large `R`,

\[
|x_{\lambda_I}|\ge\frac12
\qquad
\text{for every }I\in\binom{[R]}r.
\tag{12}
\]

Distinct `r`-subsets give distinct functionals. Indeed, if `\lambda_I=\lambda_J`, independence of `\lambda_1,\ldots,\lambda_R` gives `I=J`.

The source-character dictionary audited in `MC-301` applies to every nonzero selected shell functional: a minimizing lower-prime representative gives a distinct primitive real Dirichlet character of odd squarefree, hence cubefree, conductor `\mathcal Q(\lambda_I)`, and its normalized prime-shell average is exactly `x_{\lambda_I}`.

Apply equation `(8)` of `MC-323` with fixed threshold `\tau=1/2`. For every fixed `\delta\in(0,2)`, only `O_\delta(1)` distinct fixed-bias characters can have conductor at most `y^{2-\delta}`. Hence

\[
\boxed{
\#\left\{
I\in\binom{[R]}r:
\mathcal Q(\lambda_I)\le y^{2-\delta}
\right\}
=O_\delta(1).
}
\tag{13}
\]

The chosen package representative `(6)` need not minimize conductor, but

\[
\mathcal Q(\lambda_I)\le m_I.
\tag{14}
\]

Therefore all but `O_\delta(1)` members of the layer obey

\[
\boxed{m_I>y^{2-\delta}.}
\tag{15}
\]

This is exactly the analytic input used for pairs in `MC-324`; the only new question is how efficiently one source coordinate can serve an entire higher Hamming layer.

## 2. Higher-layer source incidence is a Krawtchouk parity slice

For each source prime `p\in U`, define its generator-column support

\[
S_p:=\{i\in[R]:p\in V_i\},
\qquad
a_p:=|S_p|.
\tag{16}
\]

By the symmetric-difference definition `(6)`,

\[
p\in V_I
\quad\Longleftrightarrow\quad
|I\cap S_p|\ \text{is odd}.
\tag{17}
\]

Thus the number of `r`-subsets whose package representative contains `p` is exactly `B_{R,r}(a_p)` from `(10)`. Summing the logarithmic package costs gives the exact identity

\[
\boxed{
\sum_{I\in\binom{[R]}r}\log m_I
=
\sum_{p\in U} B_{R,r}(a_p)\log p.
}
\tag{18}
\]

The same count is the standard binary Krawtchouk slice. If

\[
K_r(a;R)
:=
\sum_{j=0}^r(-1)^j
\binom aj\binom{R-a}{r-j},
\tag{19}
\]

then Vandermonde's identity separates even and odd intersections to give

\[
\boxed{
B_{R,r}(a)
=
\frac12\left(\binom Rr-K_r(a;R)\right).
}
\tag{20}
\]

No new coding polynomial is being introduced here. Krawtchouk polynomials are classical eigenfunctions of the binary Hamming association scheme; the point is that the exact Mathia source-package incidence lands on this classical parity statistic.

For `r=2`, `(18)` reduces to the weighted Plotkin identity of `MC-324`, because

\[
B_{R,2}(a)=a(R-a).
\tag{21}
\]

## 3. Sparse even layers are asymptotically half-balanced

The decisive bound can be proved without asymptotic Krawtchouk theory.

Fix a column support `S\subseteq[R]` of size `a`, and put

\[
\theta:=\frac aR.
\tag{22}
\]

First sample `r` indices independently and uniformly from `[R]`, with replacement. The probability that an odd number of sampled indices lies in `S` is

\[
q_r(\theta)
=
\frac{1-(1-2\theta)^r}{2}.
\tag{23}
\]

Because `r` is even,

\[
(1-2\theta)^r\ge0,
\]

and therefore

\[
q_r(\theta)\le\frac12.
\tag{24}
\]

Let `E` be the event that the independent sample contains a repeated index. By the union bound,

\[
\Pr(E)
\le
\frac{\binom r2}{R}.
\tag{25}
\]

Conditioned on `E^c`, the underlying unordered set is uniform in `\binom{[R]}r`. If `A` is the odd-intersection event, then

\[
\left|
\Pr(A)-\Pr(A\mid E^c)
\right|
\le\Pr(E).
\tag{26}
\]

Since

\[
\Pr(A\mid E^c)
=
\frac{B_{R,r}(a)}{\binom Rr},
\tag{27}
\]

we obtain the uniform bound

\[
\boxed{
\frac{B_{R,r}(a)}{\binom Rr}
\le
\frac12+\frac{\binom r2}{R}
\qquad(0\le a\le R).
}
\tag{28}
\]

Under `(5)`,

\[
\varepsilon_R:=\frac{\binom r2}{R}=o(1).
\tag{29}
\]

The constant `1/2` is sharp at this scale. Take `a=\lfloor R/2\rfloor`. If `R` is even then the with-replacement parity probability in `(23)` is exactly `1/2`. If `R` is odd, `|1-2\theta|=1/R`, so for even `r`,

\[
q_r(\theta)
=
\frac12-\frac1{2R^r}.
\tag{30}
\]

Using `(26)` in the opposite direction gives

\[
\frac{B_{R,r}(\lfloor R/2\rfloor)}{\binom Rr}
\ge
\frac12-rac1{2R^r}-\varepsilon_R.
\tag{31}
\]

Together `(28)` and `(31)` prove `(9)`.

Thus a source coordinate whose incidence column is approximately balanced already occupies asymptotically the maximum possible fraction of every sparse **even** Hamming layer. Adding more even modes increases both the total conductor demand and the total available coordinate-incidence capacity by the same binomial factor.

## 4. Conductor summation reproduces, but cannot improve, exponent four

Let

\[
N_r:=\binom Rr.
\tag{32}
\]

From `(18)` and `(28)`,

\[
\sum_{I\in\binom{[R]}r}\log m_I
\le
\left(\frac12+\varepsilon_R\right)
N_r\log P.
\tag{33}
\]

On the other hand, `(15)` gives

\[
\sum_{I\in\binom{[R]}r}\log m_I
>
\left(N_r-O_\delta(1)\right)
(2-\delta)\log y.
\tag{34}
\]

Combining `(33)` and `(34)` yields `(7)`:

\[
\frac{\log P}{\log y}
>
\frac{2-\delta}{1/2+\varepsilon_R}
\left(1-O_\delta(N_r^{-1})\right).
\tag{35}
\]

Since `R\to\infty`, `r\ge2`, and `(5)` holds, one has `N_r\to\infty` and `\varepsilon_R\to0`. Therefore for each fixed `\delta>0`,

\[
\liminf_{y\to\infty}\frac{\log P}{\log y}
\ge4-2\delta.
\tag{36}
\]

Letting the fixed `\delta` tend to zero proves `(8)`.

Equation `(9)` explains why this route stops there. Suppose one tries to improve `(33)` using only a universal inequality

\[
B_{R,r}(a)\le c_{R,r}\binom Rr
\qquad\text{for every }a.
\tag{37}
\]

Then necessarily

\[
c_{R,r}\ge\frac12-o(1).
\tag{38}
\]

At the same time `MC-323` supplies only the near-quadratic individual-conductor lower scale `y^{2-o(1)}`. Consequently the best asymptotic exponent obtainable by combining those two ingredients is

\[
\frac{2}{1/2}=4.
\tag{39}
\]

The pair layer of `MC-324` already reaches this exponent. Sparse higher even layers therefore provide **no exponent gain** under independent-conductor summation plus unrestricted columnwise parity counting, even though the number of available fixed-bias modes grows from `\binom R2` to `\binom Rr`.

## 5. Prior art and novelty boundary

The analytic conductor input is exactly `MC-323`, based on Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143–149, DOI `10.4064/aa106-2-4`, Theorem 3. In its varying-modulus clause, characters of possibly different moduli `q\le Q` are handled by replacing the single-modulus parameter by `Q^2`; for cubefree moduli the Burgess parameter may be chosen arbitrarily. No strengthening of that theorem is asserted here.

The parity polynomial `(19)` is the standard binary Krawtchouk polynomial from the Hamming association scheme. A broad coding-theory reference is Philippe Delsarte and Vladimir I. Levenshtein, *Association schemes and coding theory*, IEEE Transactions on Information Theory **44** (1998), 2477–2504, DOI `10.1109/18.720545`. No novelty is claimed for Krawtchouk polynomials, their intersection interpretation, or identity `(20)`.

There is also established higher-order Plotkin literature. Hsuan-Yin Lin, Stefan M. Moser and Po-Ning Chen, *Weak Flip Codes and their Optimality on the Binary Erasure Channel*, IEEE Transactions on Information Theory **64** (2018), 5191–5218, DOI `10.1109/TIT.2018.2834924`, introduces `r`-wise Hamming distance and generalized `r`-wise Plotkin bounds through a columnwise codebook analysis. That statistic is not identical to the XOR-parity slice `B_{R,r}(a)` used here, so it is adjacent prior art rather than the theorem invoked in `(28)`.

A targeted literature search on 16 September 2026 found the Krawtchouk/Hamming-scheme parity machinery, generalized higher-order Plotkin bounds, and Schlage-Puchta character-family estimates separately, but no source asserting the present composition for reciprocal-endpoint source packages. **No standalone novelty claim is made.** The durable contribution is the exact obstruction: the most direct attempt to exploit the endpoint's higher even Fourier layers cannot amplify the quartic source exponent because sparse even column parity is asymptotically half-balanced.

## Boundaries and falsification tests

- **This is a proof-architecture ceiling, not a universal source-cost upper bound.** The result says that the combination “individual conductor floor from `MC-323` + sum one Hamming layer + universal per-column incidence bound” cannot asymptotically produce an exponent above `4`. It does not prove that the true source radical can be as small as `y^{4+o(1)}`.
- **Even parity is load-bearing.** For odd `r`, the with-replacement probability `(23)` can approach `1` as `\theta\to1`; there is no universal one-half ceiling. Odd layers require a different analysis and cannot be declared useless from this finding.
- **Sparsity is load-bearing.** The coupling error in `(28)` is `O(r^2/R)`. Dense layers with `r` comparable to `\sqrt R` or larger are not controlled sharply enough by this argument; exact Krawtchouk asymptotics may matter there.
- **The complete endpoint profile is load-bearing.** Equation `(11)` gives a fixed nonzero bias uniformly across the chosen layer. A perturbed endpoint can lose this property before the incidence argument begins.
- **The primitive-character dictionary is load-bearing.** The use of `MC-323` requires the distinct cubefree primitive source characters established for these selected shell functionals. A different source representation must re-establish the analytic hypotheses.
- **A structural restriction on source columns could beat the universal ceiling.** Equation `(9)` is attained by nearly balanced columns. If arithmetic forces every admissible `a_p/R` into a region where the parity probability is uniformly below `1/2`, then the denominator in `(35)` can improve. No such restriction is proved here.
- **Cross-character information remains a genuine escape.** Covariances, joint conductor constraints, determinant/energy inequalities, or another theorem controlling many modes simultaneously may use information discarded by summing independent lower bounds `(15)`.
- **A stronger analytic conductor horizon remains a genuine escape.** Replacing the exponent `2-o(1)` supplied by `MC-323` with a larger forced individual-conductor exponent would raise `(39)` proportionally.
- **No Möbius estimate is asserted.** As in `MC-324`, the reciprocal endpoint remains a conditional source geometry; this result narrows one amplification route and gives no bound for the actual Mertens function.