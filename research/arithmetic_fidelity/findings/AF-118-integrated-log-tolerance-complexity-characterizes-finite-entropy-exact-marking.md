# AF-118 — Integrated log tolerance complexity characterizes finite-entropy exact marking

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `LOG-RANK-COMPLEXITY`, `ENTROPY-FINITENESS-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-116 introduced tolerance-dependent covering complexity and AF-117 showed that a countable exact repair mark has finite expected prefix-bit cost exactly when its label law has finite Shannon entropy. Those results leave a quantitative gap: knowing that every fixed positive tolerance is finitely coverable does not say how the required alphabet grows as the tolerance tends to zero.

For a **fixed** countable mark law, that entire tolerance curve has an exact rank representation, and its logarithmic area is the correct finiteness statistic.

Let

\[
p_1\ge p_2\ge\cdots>0,
\qquad
\sum_{j\ge1}p_j=1,
\tag{1}
\]

be the positive masses of a finite or countable mark, rearranged in nonincreasing order. Write

\[
F_k:=\sum_{j=1}^k p_j,
\qquad F_0:=0,
\tag{2}
\]

and for `0<epsilon<1` define the **tolerance rank complexity**

\[
K_p(\varepsilon)
:=
\min\{k\ge1:F_k>1-\varepsilon\}.
\tag{3}
\]

Equivalently, `K_p(epsilon)` is the smallest number of most-probable labels that retain mass strictly greater than `1-epsilon`.

Let `J` be the rank random variable with

\[
\mathbb P(J=j)=p_j.
\tag{4}
\]

Then:

### 1. The whole tolerance curve has an exact log-rank area

For every finite or countable probability law `(p_j)`,

\[
\boxed{
\int_0^1 \log_2 K_p(\varepsilon)\,d\varepsilon
=
\mathbb E[\log_2 J]
=
\sum_{j\ge1}p_j\log_2 j.
}
\tag{5}
\]

The strict inequality in `(3)` changes only boundary points of the tolerance intervals and therefore does not affect the integral.

Define

\[
\mathsf A(p)
:=
\int_0^1\log_2K_p(\varepsilon)\,d\varepsilon.
\tag{6}
\]

This quantity is the expected logarithm of the optimal probability rank, i.e. the logarithm of the geometric-mean guess rank.

### 2. Shannon entropy and log-rank area have exactly the same finiteness class

For every sorted countable law,

\[
\boxed{
\mathsf A(p)\le H_2(p),
}
\tag{7}
\]

where

\[
H_2(p)=\sum_jp_j\log_2\frac1{p_j}.
\tag{8}
\]

Conversely, there is a universal constant `C<infinity` such that

\[
\boxed{
H_2(p)
\le
\mathsf A(p)
+2\log_2\!\bigl(1+\mathsf A(p)\bigr)
+C.
}
\tag{9}
\]

Consequently,

\[
\boxed{
H_2(p)<\infty
\iff
\int_0^1\log_2K_p(\varepsilon)\,d\varepsilon<\infty.
}
\tag{10}
\]

Thus AF-117's exact finite-mean-bit gate can be read directly from the **entire** tolerance-complexity profile of one coherent mark. It is not enough that `K_p(epsilon)` be finite for each fixed positive `epsilon`; its logarithm must be integrable as `epsilon` decreases to zero.

### 3. The equivalence is uniform over families

For a family `(p^{(i)})`, put

\[
A_*:=\sup_i\mathsf A(p^{(i)}).
\tag{11}
\]

Then

\[
\boxed{
\sup_i H_2(p^{(i)})<\infty
\iff
A_*<\infty.
}
\tag{12}
\]

More quantitatively,

\[
A_*
\le
\sup_iH_2(p^{(i)}),
\tag{13}
\]

and when `A_*<infinity`,

\[
\sup_iH_2(p^{(i)})
\le
A_*+2\log_2(1+A_*)+C.
\tag{14}
\]

Combining AF-117 with `(12)`, a family of exact discrete marks has uniformly bounded mean prefix-bit cost if and only if the integrated logarithm of its tolerance rank complexity is uniformly bounded.

### 4. Pointwise tolerance bounds have a sharp integrability boundary

Equation `(10)` turns growth of `K_p(epsilon)` near zero into an exact entropy test.

If for sufficiently small `epsilon`,

\[
\log K_p(\varepsilon)
\le C_0\varepsilon^{-\beta}
\qquad\text{with }\beta<1,
\tag{15}
\]

then `H_2(p)<infinity`. In particular, polynomial growth of `K_p(\varepsilon)` in `1/epsilon`, or even stretched-exponential growth `\exp(O(\varepsilon^{-\beta}))` with `beta<1`, is compatible with finite exact mean information.

Conversely, if for all sufficiently small `epsilon`,

\[
\log K_p(\varepsilon)
\ge c_0\varepsilon^{-1},
\tag{16}
\]

then `H_2(p)=+infinity`.

The exponent `1` is therefore the natural pointwise power threshold for the logarithmic tolerance curve, with the exact boundary determined by integrability rather than by one asymptotic exponent alone.

## Derivation

### The quantile cells prove the exact identity `(5)`

From `(3)`, `K_p(epsilon)=j` precisely when

\[
F_{j-1}\le1-\varepsilon<F_j.
\tag{17}
\]

Equivalently,

\[
1-F_j<\varepsilon\le1-F_{j-1}.
\tag{18}
\]

This interval has Lebesgue length

\[
F_j-F_{j-1}=p_j.
\tag{19}
\]

Therefore

\[
\begin{aligned}
\int_0^1\log_2K_p(\varepsilon)\,d\varepsilon
&=
\sum_{j\ge1}p_j\log_2j\\
&=
\mathbb E[\log_2J],
\end{aligned}
\tag{20}
\]

with monotone convergence covering the infinite-support case.

### Sorted mass gives the lower entropy bound `(7)`

Because `(p_j)` is nonincreasing,

\[
jp_j
\le
\sum_{r=1}^jp_r
\le1,
\tag{21}
\]

so

\[
p_j\le\frac1j.
\tag{22}
\]

Hence

\[
\log_2j
\le
\log_2\frac1{p_j},
\tag{23}
\]

and averaging `(23)` against `p_j` proves `(7)`.

### A universal integer code proves the converse finiteness bound

The finite-support harmonic prior `q_j\propto1/j` cannot be normalized on all positive integers. To obtain a support-independent bound, define

\[
q_j
:=
\frac1Z\frac1{j(1+\log_2j)^2},
\qquad
Z:=\sum_{j\ge1}\frac1{j(1+\log_2j)^2}.
\tag{24}
\]

The integral test gives `Z<infinity`, so `(q_j)` is a probability distribution with full support. Choose Shannon code lengths

\[
\ell_j
:=
\left\lceil\log_2\frac1{q_j}\right\rceil.
\tag{25}
\]

Since `2^{-ell_j}<=q_j`, Kraft's inequality holds and a binary prefix code with these lengths exists. Its expected length under `p` satisfies

\[
\begin{aligned}
\mathbb E_p[\ell_J]
&<
\log_2Z
+\mathbb E_p[\log_2J]\\
&\quad
+2\mathbb E_p[\log_2(1+\log_2J)]
+1.
\end{aligned}
\tag{26}
\]

The function `x -> log_2(1+x)` is concave for `x>=0`, so Jensen's inequality and `(5)` give

\[
\mathbb E_p[\log_2(1+\log_2J)]
\le
\log_2(1+\mathsf A(p)).
\tag{27}
\]

The noiseless source-coding lower bound says that Shannon entropy does not exceed the mean length of any binary prefix code. Thus

\[
H_2(p)
\le
\mathsf A(p)
+2\log_2(1+\mathsf A(p))
+\log_2Z+1.
\tag{28}
\]

Equation `(9)` follows with the universal constant

\[
C:=\log_2Z+1.
\tag{29}
\]

The same bound applied pointwise to a family proves `(12)`--`(14)`.

## Exact controls and boundary examples

### AF-116's dyadic hierarchy lies safely inside the finite-entropy regime

For the limiting dyadic level law

\[
p_j=2^{-j},
\qquad j\ge1,
\tag{30}
\]

the omitted tail after the first `k` labels is exactly `2^{-k}`. Therefore

\[
K_p(\varepsilon)
\asymp
\log_2\frac1\varepsilon
\qquad(\varepsilon\downarrow0).
\tag{31}
\]

Hence

\[
\log K_p(\varepsilon)
=O\!\left(\log\log\frac1\varepsilon\right),
\tag{32}
\]

which is integrable at zero. This recovers, from the tolerance curve alone, AF-116/AF-117's conclusion that the exact scale label can have finite entropy and finite mean coding cost despite requiring infinitely many possible labels.

### AF-117's heavy-tail example sits on the nonintegrable boundary

AF-117 used masses proportional to

\[
p_j\asymp\frac1{j(\log j)^2}.
\tag{33}
\]

Their tail satisfies

\[
\sum_{j>K}p_j
\asymp
\frac1{\log K}.
\tag{34}
\]

Solving `(34)` for the number of labels needed to leave error `epsilon` gives

\[
K_p(\varepsilon)
=\exp\!\left(\Theta\!\left(\frac1\varepsilon\right)\right),
\tag{35}
\]

and therefore

\[
\log K_p(\varepsilon)
=\Theta\!\left(\frac1\varepsilon\right).
\tag{36}
\]

The integral in `(10)` diverges logarithmically. This is exactly the divergence AF-117 found directly from

\[
p_j\log\frac1{p_j}
\asymp
\frac1{j\log j}.
\tag{37}
\]

Thus the earlier example is not merely an isolated heavy-tail construction: it realizes the natural nonintegrable tolerance-growth boundary.

### AF-117's pointwise Markov bound is deliberately too coarse to decide exact entropy

AF-117 proved that entropy at most `B` implies, after extra error `delta`, a finite alphabet bounded roughly by

\[
K(\delta)\lesssim2^{B/\delta}.
\tag{38}
\]

Taking logarithms gives the borderline envelope `B/delta`, whose integral diverges. There is no contradiction: Markov's inequality controls each tolerance separately and discards the dependence between different tolerance levels.

Equation `(5)` retains that dependence because all tolerances are generated by one common ranked law. The exact entropy budget is therefore encoded in the **area under the full log-rank curve**, not in the worst universal pointwise consequence of a finite entropy bound.

## Critical coherence boundary

The identity `(5)` applies to one fixed mark distribution, not to an independently reoptimized cover at every tolerance.

AF-116's geometric quantity

\[
N_\mu(R,\varepsilon)
\tag{39}
\]

allows the set of reproduction centers to change with `epsilon`. AF-117's entropy repair cost similarly takes an infimum over admissible marks at the declared tolerance. In a general metric repair problem, the optimal codebooks for two tolerances need not be nested or arise from one common countable mark.

Therefore one must **not** replace `K_p(epsilon)` by `N_mu(R,epsilon)` in `(5)` and call the resulting integral an entropy without an additional coherence theorem.

To use the present result after a geometric or spectral compression, one needs either:

- one source-forced countable mark whose label probabilities are fixed across tolerance levels; or
- a theorem producing a coherent nested family of codebooks/partitions from which a single mark law can be reconstructed.

Without such coherence, integrating separately optimized covering numbers can understate the information required by any one admissible repair.

This is a new audit gate for multiscale constructions: **tolerance-wise cheap repairs do not automatically assemble into one cheap exact mark.**

## Prior art and novelty assessment

The ingredients are classical and **no standalone theorem-level novelty is claimed**.

- Claude E. Shannon, **“A Mathematical Theory of Communication,”** *Bell System Technical Journal* 27 (1948), 379–423 and 623–656. Role: Shannon entropy and the noiseless source-coding lower bound underlying `(28)`.
- Peter Elias, **“Universal Codeword Sets and Representations of the Integers,”** *IEEE Transactions on Information Theory* 21(2), 194–203 (1975), DOI `10.1109/TIT.1975.1055349`. Role: classical universal prefix coding of positive integers with logarithmic-plus-lower-order code lengths; direct prior-art boundary for the support-independent integer-code argument in `(24)`--`(28)`.
- Erdal Arıkan, **“An Inequality on Guessing and Its Application to Sequential Decoding,”** *IEEE Transactions on Information Theory* 42(1), 99–105 (1996), DOI `10.1109/18.481781`. Role: foundational probability-ordered guessing framework and moment/Rényi-entropy inequalities; the rank variable `J` is the optimal guess number for a source sorted by decreasing mass.
- Olivier Rioul, **“Variations on a Theme by Massey,”** *IEEE Transactions on Information Theory* 68(5), 2813–2828 (2022), DOI `10.1109/TIT.2022.3141264`. Role: modern entropy-versus-guessing inequalities and the mature information-theoretic context for bounding discrete entropy from rank/moment information.
- Julien Béguinot, Olivier Rioul, Loïc Masure, François-Xavier Standaert, Wei Cheng, and Sylvain Guilley, **“Scalable Information Theoretic Evaluation of the Rank Statistics in Side-Channel Attacks,”** *IACR Transactions on Cryptographic Hardware and Embedded Systems* 2026(1), 53–81 (2026), DOI `10.46586/tches.v2026.i1.53-81`. Role: direct recent prior art for **log-guessing entropy** `E[log rank]`, geometric-mean rank, marginal guesswork, and finite-support information-theoretic bounds connecting rank statistics to Shannon information.

For finite support of size `M`, the classical comparison is sharper than the universal infinite-alphabet bound. With the harmonic distribution

\[
q_j=\frac1{jH_M},
\qquad
H_M=\sum_{j=1}^M\frac1j,
\tag{40}
\]

Gibbs' inequality gives

\[
\mathsf A(p)
\le H_2(p)
\le
\mathsf A(p)+\log_2H_M.
\tag{41}
\]

This is exactly the finite-rank language developed in the modern log-guessing literature. The support-independent bound `(9)` replaces the divergent harmonic normalization by a universal integer code and is used here only to classify **finiteness on countably infinite or unbounded supports**.

The Arithmetic Fidelity contribution is organizational rather than a novelty claim: AF-116 and AF-117 had separated label cardinality, tolerance complexity, and expected-bit cost but had not yet identified the exact global functional of the tolerance curve that decides the zero-error entropy boundary. Equation `(5)` supplies that bridge and exposes the additional coherence requirement when one tries to infer exact side-information cost from independently optimized multiscale covers.

## Consequence for the active frontier

The multiscale budget hierarchy can now be stated more sharply.

A source-natural exact mark may require infinitely many labels and may have `K(epsilon)->infinity` as `epsilon->0` without violating a bounded mean-information budget. The decisive quantity is not the pointwise divergence of `K`, nor finiteness of `K(epsilon)` at every fixed tolerance, but

\[
\boxed{
\int_0^1\log_2K_p(\varepsilon)\,d\varepsilon.
}
\tag{42}
\]

For a coherent mark, finiteness of `(42)` is equivalent to finite entropy and hence, by AF-117, to finite mean prefix-bit exact repair. For a family of source instances, a uniform bound on `(42)` is equivalent to a uniform entropy budget.

For RH-facing applications this creates a concrete two-stage obligation. First, identify a **single source-forced relational or multiscale mark** and prove that its tolerance-rank curve has bounded integrated logarithm. Second, test that same mark against matched Beurling/generalized-prime or other non-prime controls. A collection of separately optimized low-complexity approximations at each tolerance does not satisfy the first gate unless they assemble coherently into one admissible mark.

The next useful advance should therefore not be another abstract distinction between cardinality and entropy. It should establish, for a concrete Mathia compression, whether its surviving scale/provenance data admit a coherent mark whose integrated log tolerance complexity is bounded and whose retained structure still distinguishes the intended arithmetic source from matched controls.