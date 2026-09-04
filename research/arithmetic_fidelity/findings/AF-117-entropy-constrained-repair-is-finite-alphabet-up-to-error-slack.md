# AF-117 — Entropy-constrained repair is finite-alphabet repair up to error slack, with a sharp zero-error boundary

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `ENTROPY-CONSTRAINED-REPAIR`, `ZERO-ERROR-BOUNDARY`, `NO-NOVELTY-CLAIM`

## Claim

AF-116 separated three resource budgets that can be confused when a compression needs an auxiliary mark: the number of retained labels, worst-case fixed-length bits, and probability-weighted mean description length. The mean-length regime admits an exact one-shot classification in terms of the Shannon entropy of the repair mark, and it is related to AF-116's finite-alphabet covering complexity by a sharp error-slack principle.

Let `(X,d)` be a metric space with Borel probability measure `mu`, fix `R >= 0`, and let `0 < epsilon < 1`. A **countable deterministic radius-`R` repair mark** consists of a measurable map

\[
m:X\to J
\]

to a finite or countable label set `J`, together with decoder centers `a_j in X`, such that

\[
\mu\{x:d(x,a_{m(x)})>R\}<\varepsilon.
\tag{1}
\]

Write

\[
p_j:=\mu\{m=j\},
\qquad
H_2(p):=\sum_{j:p_j>0}p_j\log_2\frac1{p_j},
\tag{2}
\]

allowing `H_2(p)=+infinity`. Define the **entropy repair cost**

\[
\mathsf E_\mu(R,\varepsilon)
:=
\inf H_2(p),
\tag{3}
\]

where the infimum is over all marks satisfying `(1)`. Define also the **mean prefix-bit repair cost**

\[
\mathsf L_\mu(R,\varepsilon)
:=
\inf \sum_j p_j\ell_j,
\tag{4}
\]

where the infimum is now over admissible marks and binary prefix codes with codeword lengths `ell_j` for the positive-probability labels.

Then:

### 1. Shannon entropy is the exact mean-bit budget up to the unavoidable one-bit integer-length gap

For every `R` and `0<epsilon<1`,

\[
\boxed{
\mathsf E_\mu(R,\varepsilon)
\le
\mathsf L_\mu(R,\varepsilon)
\le
\mathsf E_\mu(R,\varepsilon)+1.
}
\tag{5}
\]

The upper inequality is strict before taking the infimum whenever a finite-entropy nontrivial mark is fixed. In particular,

\[
\boxed{
\mathsf E_\mu(R,\varepsilon)<\infty
\iff
\mathsf L_\mu(R,\varepsilon)<\infty.
}
\tag{6}
\]

Thus, once the allowed side information is a countable variable-length label charged by expected bits, **finite Shannon entropy is the exact finiteness gate**. Merely counting how many labels occur is too strong: infinitely many labels may have finite mean coding cost.

### 2. Finite-alphabet repair implies finite-entropy repair at the same tolerance

Let `N_\mu(R,epsilon)` be AF-116's partial covering number,

\[
N_\mu(R,\varepsilon)
:=
\min\left\{
|C|:
C\subset X\text{ finite},\quad
\mu\!\left(\bigcup_{a\in C}\overline B(a,R)\right)>1-\varepsilon
\right\},
\tag{7}
\]

with value `+infinity` when no finite cover exists. Whenever `N_\mu(R,epsilon)<infinity`,

\[
\boxed{
\mathsf E_\mu(R,\varepsilon)
\le
\log_2 N_\mu(R,\varepsilon).
}
\tag{8}
\]

This is exact at the level of resource classes: an `N`-center partial cover gives a repair mark with at most `N` positive-probability labels, and any such label distribution has entropy at most `log_2 N`.

### 3. Finite entropy forces a finite alphabet after arbitrarily small extra error

Conversely, suppose

\[
\mathsf E_\mu(R,\varepsilon)\le B<\infty.
\tag{9}
\]

For every `delta>0` with `epsilon+delta<1` and every `eta>0`,

\[
\boxed{
N_\mu(R,\varepsilon+\delta)
\le
2^{(B+\eta)/\delta}.
}
\tag{10}
\]

More precisely, the integer on the left is at most the number of labels whose probabilities are at least `2^{-(B+eta)/delta}`, and that number is bounded by the right-hand side.

Therefore finite-alphabet and finite-mean-bit repair have the same **finiteness class at positive tolerance up to arbitrarily small error slack**:

\[
N_\mu(R,\varepsilon)<\infty
\Longrightarrow
\mathsf E_\mu(R,\varepsilon)<\infty,
\tag{11}
\]

while

\[
\mathsf E_\mu(R,\varepsilon)<\infty
\Longrightarrow
N_\mu(R,\varepsilon+\delta)<\infty
\quad\text{for every }\delta>0.
\tag{12}
\]

Thus a finite entropy budget cannot hide an order-one amount of mass in genuinely infinitely many essential labels. It can hide infinitely many **rare** labels, but any fixed additional error tolerance discards all but finitely many of them.

### 4. Exact zero-radius discrete fidelity has a sharper boundary: its entropy is the source entropy itself

The strict-error convention in `(1)` is convenient for AF-116's partial-covering number, so define the exact variant separately. Let

\[
\mathsf E_\mu^{0}(R)
\]

be the infimum in `(3)` over marks with zero excess-radius error, and define `mathsf L_mu^0(R)` analogously.

If `mu` is supported on a finite or countable set of distinct points and `R=0`, exact reconstruction forces different positive-mass atoms to receive different decoder labels. Hence every exact mark has, up to relabeling, the same positive-probability law as `mu`. Therefore

\[
\boxed{
\mathsf E_\mu^{0}(0)=H_2(\mu),
}
\tag{13}
\]

and

\[
\boxed{
H_2(\mu)
\le
\mathsf L_\mu^{0}(0)
\le
H_2(\mu)+1.
}
\tag{14}
\]

For a family of discrete profiles `(mu_i)`, bounded exact mean-bit repair is therefore equivalent to a uniform entropy bound:

\[
\boxed{
\sup_i \mathsf L_{\mu_i}^{0}(0)<\infty
\iff
\sup_i H_2(\mu_i)<\infty.
}
\tag{15}
\]

The additive one-bit coding gap is uniform, so it cannot affect this finiteness classification.

## Derivation

### Kraft--McMillan gives the lower bound in `(5)`

Fix an admissible mark with distribution `p` and a binary prefix code of lengths `(ell_j)`. Prefix codes satisfy Kraft's inequality

\[
K:=\sum_j2^{-\ell_j}\le1.
\tag{16}
\]

For `K>0`, put

\[
q_j:=\frac{2^{-\ell_j}}K.
\tag{17}
\]

Then, with logarithms base two,

\[
\begin{aligned}
D(p\|q)
&=\sum_jp_j\log_2\frac{p_j}{q_j}\\
&=-H_2(p)+\sum_jp_j\ell_j+\log_2 K.
\end{aligned}
\tag{18}
\]

Since relative entropy is nonnegative and `log_2 K<=0`,

\[
\sum_jp_j\ell_j
=
H_2(p)+D(p\|q)-\log_2K
\ge H_2(p).
\tag{19}
\]

Taking the infimum over all admissible marks and codes yields the left inequality of `(5)`.

For the converse, for every positive-probability label choose the Shannon length

\[
\ell_j
=
\left\lceil\log_2\frac1{p_j}\right\rceil.
\tag{20}
\]

Then

\[
\sum_j2^{-\ell_j}
\le
\sum_jp_j
=1,
\tag{21}
\]

so Kraft's inequality admits a binary prefix code with those lengths, and when `H_2(p)<infinity`,

\[
\sum_jp_j\ell_j
< H_2(p)+1
\tag{22}
\]

apart from the trivial one-label case, where both costs are zero. Approximating the infimum in `(3)` and letting the approximation error tend to zero gives the right inequality in `(5)`. If `mathsf E_mu(R,epsilon)=+infinity`, `(19)` forces every admissible mean code length to be infinite, so `(6)` also holds in the extended-value case.

### A finite cover proves `(8)`

Choose a set of `N=N_mu(R,epsilon)` centers whose closed radius-`R` balls cover mass greater than `1-epsilon`. Assign every covered point to one center whose ball contains it and assign the uncovered points arbitrarily to one existing label. The reconstruction error is below `epsilon`, and the mark uses at most `N` positive-probability labels. Therefore

\[
H_2(p)\le\log_2N,
\tag{23}
\]

which proves `(8)`.

### Information-content truncation proves `(10)`

Fix `eta>0`. By `(9)`, choose an admissible mark with

\[
H_2(p)\le B+\eta.
\tag{24}
\]

For a random label `M` with law `p`, define its information content

\[
I(M):=-\log_2p_M.
\tag{25}
\]

Then `I(M)>=0` and

\[
\mathbb E I(M)=H_2(p)\le B+\eta.
\tag{26}
\]

Markov's inequality gives

\[
\mathbb P\!\left\{
I(M)>\frac{B+\eta}{\delta}
\right\}
\le\delta.
\tag{27}
\]

Let

\[
A:=\left\{
j:p_j\ge2^{-(B+\eta)/\delta}
\right\}.
\tag{28}
\]

Equation `(27)` says `P(M in A)>=1-delta`. Since the probabilities in `A` sum to at most one,

\[
|A|\le2^{(B+\eta)/\delta}.
\tag{29}
\]

The original repair succeeds on a set of mass greater than `1-epsilon`. Intersecting that success set with `{M in A}` leaves mass strictly greater than `1-epsilon-delta`. Every point in that intersection lies in one of the radius-`R` balls centered at `(a_j)_{j in A}`. These finitely many centers therefore certify `(10)`.

This argument is deliberately one-shot. It does not invoke asymptotic block coding, typical sequences, or a rate-distortion limit; the only probabilistic input is the mean self-information of the actual repair-label law.

## Exact controls and separation examples

### AF-116's geometric spectral profile has bounded entropy exactly where its mean mark cost stays bounded

AF-116 used the normalized spectral-level law

\[
w_{n,\ell}
=
\frac{2^{-\ell}}{1-2^{-n}},
\qquad
1\le\ell\le n.
\tag{30}
\]

Its entropy is exactly

\[
\begin{aligned}
H_2(w_n)
&=
\sum_{\ell=1}^n
w_{n,\ell}\log_2\frac1{w_{n,\ell}}\\
&=
\frac{\sum_{\ell=1}^n\ell2^{-\ell}}{1-2^{-n}}
+\log_2(1-2^{-n})\\
&=
2-\frac{n}{2^n-1}
+\log_2(1-2^{-n})
\longrightarrow2.
\end{aligned}
\tag{31}
\]

AF-116's unary code `1^{ell-1}0` had expected length

\[
2-\frac{n}{2^n-1}<2.
\tag{32}
\]

Thus the bounded mean description length in that example is not an artifact of a specially chosen unary code. It is forced by the bounded Shannon entropy of the resource-weighted scale law, and `(5)` shows that no prefix code can improve the mean cost below entropy.

At the same time the exact label cardinality is `n`, and every fixed finite label alphabet fails when arbitrarily small error is demanded uniformly. This is the precise separation between support/cardinality complexity and probability-weighted mean information.

### Every positive tolerance may have uniformly finite cardinality while exact mean-bit cost diverges

The error slack in `(10)` cannot be removed uniformly at `epsilon=0`.

Take the discrete metric on the countable set `{3,4,5,...}` and, for `n>=3`, define

\[
a_j:=\frac1{j(\log j)^2},
\qquad
S_n:=\sum_{j=3}^na_j,
\qquad
p_j^{(n)}:=\frac{a_j}{S_n}
\quad(3\le j\le n).
\tag{33}
\]

The series `sum_{j>=3} a_j` converges. Hence for every fixed `epsilon>0` there is a finite `K(epsilon)` such that

\[
\sum_{j>K(\varepsilon)}a_j
<\varepsilon a_3.
\tag{34}
\]

Since `S_n>=a_3`, for all `n>K(epsilon)`,

\[
\sum_{j>K(\varepsilon)}p_j^{(n)}<\varepsilon.
\tag{35}
\]

Therefore, at zero radius,

\[
\boxed{
\sup_n N_{p^{(n)}}(0,\varepsilon)<\infty
\quad\text{for every fixed }\varepsilon>0.
}
\tag{36}
\]

So every positive error tolerance is uniformly repairable by a finite alphabet.

But

\[
H_2(p^{(n)})
=
\log_2S_n
+
\frac1{S_n}
\sum_{j=3}^n
 a_j\log_2\frac1{a_j}.
\tag{37}
\]

The normalizing factors `S_n` converge to a finite positive limit, while

\[
a_j\log\frac1{a_j}
\sim
\frac1{j\log j}.
\tag{38}
\]

The series in `(38)` diverges. Consequently

\[
\boxed{
H_2(p^{(n)})\to\infty,
\qquad
\mathsf L_{p^{(n)}}^0(0)\to\infty.
}
\tag{39}
\]

This is the sharp nonuniform boundary left open by AF-116: **finite complexity at every fixed positive tolerance does not imply bounded exact average-bit complexity as the tolerance tends to zero**. Rare labels may be individually negligible at every prescribed error level while their cumulative exact self-information diverges.

### Entropy is a budget, not a provenance certificate

The entropy of a label law records the average amount of noiseless side information needed to name that label. It does not say that the label is intrinsic, canonical, source-natural, or sufficient for the discriminator of interest.

Two unrelated constructions can have the same label distribution and therefore the same entropy. A rational-prime-derived object and a matched Beurling/generalized-prime control can likewise have identical scale-label entropies. Passing `(5)` or `(15)` is therefore only a **resource feasibility** result. Arithmetic fidelity still requires the retained mark itself to be forced by the source and to distinguish the matched controls at the same information layer.

### Mean-bit, worst-case-bit, and exact-cardinality categories must not be interchanged

A countable prefix code can have finite mean length but unbounded worst-case length. Conversely, a finite alphabet automatically bounds both support cardinality and worst-case fixed-length cost. The three statements

- finitely many labels;
- bounded worst-case bits;
- bounded expected bits

are therefore different admissibility categories, even though `(10)` shows that finite expected bits collapse to a finite effective alphabet after allowing a fixed extra error probability.

A downstream RH mechanism must declare which category its retained structure genuinely supports before a witness is chosen. Otherwise a proof can appear to repair a compression merely by silently changing the side-information budget.

## Prior art and novelty assessment

The coding-theoretic mathematics used here is classical, and **no theorem-level novelty is claimed**.

- Claude E. Shannon, **“A Mathematical Theory of Communication,”** *Bell System Technical Journal* 27 (1948), 379–423 and 623–656. Role: foundational source-coding entropy and variable-length coding framework; establishes entropy as the fundamental average description-rate quantity.
- Brockway McMillan, **“Two inequalities implied by unique decipherability,”** *IRE Transactions on Information Theory* 2(4), 115–116 (1956), DOI `10.1109/TIT.1956.1056818`. Role: classical extension of Kraft's inequality to uniquely decipherable codes; supports the lower-bound side of `(5)` beyond prefix codes.
- Claude E. Shannon, **“Coding Theorems for a Discrete Source With a Fidelity Criterion,”** *IRE National Convention Record*, part 4 (1959), 142–163. Role: foundational rate-distortion/fidelity-criterion framework, showing that lossy representation must be audited jointly with an explicit fidelity tolerance and rate budget.
- Philip A. Chou, Tom Lookabaugh, and Robert M. Gray, **“Entropy-Constrained Vector Quantization,”** *IEEE Transactions on Acoustics, Speech, and Signal Processing* 37(1), 31–42 (1989), DOI `10.1109/29.17498`. Role: direct mature prior art for quantizers optimized under an entropy/variable-rate constraint rather than a fixed codebook-rate constraint.

Equations `(5)` and `(13)`–`(15)` are direct one-shot specializations of classical noiseless source coding. The implication `(10)` is the elementary information-content truncation of a finite-entropy label law, and the heavy-tail control `(33)`–`(39)` is an explicit boundary example. The Arithmetic Fidelity value is not a new coding theorem: it is the exact placement of these classical distinctions immediately after AF-115/AF-116's multiscale compression hierarchy, so that a proposed repair must name its admissible resource category before “infinitely many retained scales” is treated as either fatal or harmless.

## Consequence for the active frontier

AF-115 classified the **number of persistent geometric scales** needed to retain almost all resource mass. AF-116 showed that unbounded exact scale cardinality need not imply large average side information. The present result closes that ambiguity at the next budget layer:

\[
\boxed{
\text{finite expected prefix-bit repair}
\iff
\text{finite entropy repair},
}
\tag{40}
\]

and finite entropy can always be truncated to a finite alphabet after an arbitrarily small increase in error tolerance.

The genuinely harder boundary is therefore not “finite versus infinitely many labels” by itself. It is whether the application requires **exact** retention as tolerance tends to zero, and whether the source-forced label distribution has uniformly bounded entropy in that regime. The heavy-tail family proves that all fixed positive-tolerance covering tests can pass while exact mean-bit fidelity still diverges.

For RH-facing applications, any trace/determinant/spectral repair that invokes an infinite marked hierarchy should now be audited in this order: identify the source-natural mark, specify the permitted error/fidelity regime, compute or bound its resource-weighted entropy rather than only its support size, and then compare the same mark against matched non-prime controls. Only after those gates pass can bounded mean information be interpreted as preservation of the arithmetic discriminator rather than merely cheap coding of a non-arithmetic scale profile.