# AF-164 — Provenance codebooks obey a decoding-capacity gate

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `COMPOSITION-LAW`, `STRUCTURAL-RIGIDITY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-161--AF-163 show that whole-family recovery complexity depends strongly on how hidden alternative identity is allowed to recombine across coordinates: full Cartesian recombination gives exponential tensor growth, one shared identity stays bounded, and a block partition interpolates through the number of independently recombinable blocks.

The partition model is not the natural endpoint of that classification. An arbitrary provenance constraint is more cleanly represented by a **codebook of admissible identity patterns**, and then two classical coding quantities give complementary fidelity gates: a pair-overlap enumerator is a sufficient condition for whole-provenance survival, while Shannon channel capacity is a necessary rate condition.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite alphabet `X`, with the distinct laws `P_i` regarded as the output laws of a discrete memoryless channel

\[
W(x\mid i)=P_i(x).
\tag{1}
\]

For each `n`, let

\[
\mathcal A_n\subseteq[m]^n
\]

be a nonempty set of admissible provenance words. A word `a=(a_1,\ldots,a_n)` determines the product law

\[
Q_a(x^n)=\prod_{t=1}^n P_{a_t}(x_t).
\tag{2}
\]

Write

\[
N_n:=|\mathcal A_n|,
\qquad
\mathcal E(\mathcal A_n):=(Q_a)_{a\in\mathcal A_n},
\tag{3}
\]

and let `C_n`, `Lambda_n`, and `G_n=Lambda_n/C_n` be respectively the Shtarkov mass, AF-159/AF-160 barycentric domination radius, and convex-hull penalty of this constrained experiment.

If `A` is uniform on `A_n`, `X^n` is drawn from `Q_A`, and `e_n^*` is the optimal whole-word classification error, then exactly

\[
\boxed{
C_n=N_n(1-e_n^*).
}
\tag{4}
\]

Thus the normalized Shtarkov mass is not merely a source-complexity surrogate in this model:

\[
\boxed{
\frac{C_n}{N_n}=1-e_n^*
}
\tag{5}
\]

is the optimal probability that the retained observations still identify the complete admissible provenance word under the uniform prior.

Define the one-coordinate Hellinger/Bhattacharyya affinity matrix

\[
R_{ij}:=\sum_{x\in X}\sqrt{P_i(x)P_j(x)},
\qquad R_{ii}=1,
\tag{6}
\]

and the normalized codebook collision budget

\[
\varepsilon_n
:=
\frac1{N_n}
\sum_{\{a,b\}\subseteq\mathcal A_n,\ a\ne b}
\prod_{t=1}^n R_{a_tb_t}.
\tag{7}
\]

Then

\[
\boxed{
e_n^*\le \min\{1,\varepsilon_n\}.
}
\tag{8}
\]

Consequently, whenever `epsilon_n<1`,

\[
\boxed{
N_n(1-\varepsilon_n)
\le C_n\le\Lambda_n\le N_n,
}
\tag{9}
\]

and therefore

\[
\boxed{
1\le G_n\le\frac1{1-\varepsilon_n}.
}
\tag{10}
\]

In particular,

\[
\varepsilon_n\to0
\quad\Longrightarrow\quad
\frac{C_n}{N_n}\to1,
\quad
\frac{\Lambda_n}{N_n}\to1,
\quad
G_n\to1.
\tag{11}
\]

So an admissible provenance family whose codewords become collectively distinguishable has a very simple asymptotic recovery-complexity scale: the barycentric domination radius approaches the **number of admissible provenance identities**, and the extra convex-hull mismatch disappears.

This sufficient gate has a direct code-geometric form. If

\[
\rho:=\max_{i\ne j}R_{ij}<1,
\tag{12}
\]

then for Hamming distance `d_H`,

\[
\prod_{t=1}^nR_{a_tb_t}
\le
\rho^{d_H(a,b)}.
\tag{13}
\]

Hence the distance enumerator of the provenance codebook controls whole-identity fidelity. Cardinality alone is not enough: two sets of the same size can have completely different overlap geometry.

There is also a converse rate gate. Let

\[
\mathsf C_W
:=
\max_{\pi\in\Delta_m}I_\pi(I;X)
\tag{14}
\]

be the Shannon capacity of the one-coordinate channel `(1)`, measured in nats. For every codebook with `N_n>=2`, Fano's inequality and memorylessness give

\[
\boxed{
\frac{C_n}{N_n}
=1-e_n^*
\le
\min\left\{
1,
\frac{n\mathsf C_W+\log2}{\log N_n}
\right\}.
}
\tag{15}
\]

Therefore, if the provenance rate converges,

\[
\frac1n\log N_n\longrightarrow R>\mathsf C_W,
\tag{16}
\]

then

\[
\boxed{
\limsup_{n\to\infty}\frac{C_n}{N_n}
\le
\frac{\mathsf C_W}{R}<1.
}
\tag{17}
\]

The vanishing-collision regime `(11)` is consequently impossible above the channel's discrimination capacity.

The structural conclusion is sharper than AF-163's block-count language. **Coherent provenance is useful only relative to the number and geometry of admissible identity patterns that the retained local channel can actually distinguish.** A provenance constraint should therefore be audited as a code: its pattern count gives the required whole-family scale, its overlap geometry gives a sufficient recovery test, and the local channel capacity gives a necessary asymptotic rate gate.

## Derivation

### Shtarkov mass is whole-provenance MAP success

For a uniform prior on `A_n`, maximum a posteriori decoding is maximum-likelihood decoding. Its success probability is

\[
\begin{aligned}
1-e_n^*
&=
\sum_{x^n}
\max_{a\in\mathcal A_n}
\frac1{N_n}Q_a(x^n)\\
&=
\frac1{N_n}
\sum_{x^n}\max_{a\in\mathcal A_n}Q_a(x^n)\\
&=
\frac{C_n}{N_n},
\end{aligned}
\tag{18}
\]

which proves `(4)--(5)`. This identity is valid for any finite experiment; the provenance codebook merely gives it a concrete source interpretation.

Distinct codewords give distinct product laws under the standing assumption that the base `P_i` are distinct: a product law determines each one-coordinate marginal, so equality `Q_a=Q_b` forces `P_{a_t}=P_{b_t}` and hence `a_t=b_t` for every coordinate.

### Pair affinities give a sufficient collective-separation bound

For any nonnegative numbers `(r_a)_{a\in\mathcal A_n}`, choose one index attaining their maximum. Then

\[
\sum_a r_a-\max_a r_a
\le
\sum_{a<b}\min(r_a,r_b)
\le
\sum_{a<b}\sqrt{r_ar_b}.
\tag{19}
\]

Apply `(19)` pointwise with `r_a=Q_a(x^n)` and sum over `x^n`. Since every `Q_a` is a probability law,

\[
N_n-C_n
\le
\sum_{a<b}
\sum_{x^n}\sqrt{Q_a(x^n)Q_b(x^n)}.
\tag{20}
\]

The product structure makes every pair affinity factor exactly:

\[
\sum_{x^n}\sqrt{Q_a(x^n)Q_b(x^n)}
=
\prod_{t=1}^nR_{a_tb_t}.
\tag{21}
\]

Dividing `(20)` by `N_n` and using `(5)` proves `(8)`.

AF-160 gives the universal lower bound `C_n<=Lambda_n`. The uniform barycenter of the `N_n` codeword laws gives `Lambda_n<=N_n`, since every member is pointwise at most `N_n` times that barycenter. Combining these bounds with `(8)` proves `(9)--(11)`.

If `a_t=b_t`, the corresponding factor in `(21)` is one; if they differ, it is at most `rho`. Equation `(13)` follows immediately.

### Shannon capacity bounds the rate at which provenance can remain identifiable

Let the random codeword `A=(A_1,\ldots,A_n)` be uniform on `A_n`. Its coordinates may be arbitrarily dependent because the codebook may impose any global provenance relation. Conditional on `A`, however, the outputs are independent and `X_t` depends only on `A_t` through the same one-use channel `W`.

Therefore

\[
\begin{aligned}
I(A;X^n)
&=H(X^n)-H(X^n\mid A)\\
&\le
\sum_{t=1}^nH(X_t)
-
\sum_{t=1}^nH(X_t\mid A_t)\\
&=
\sum_{t=1}^nI(A_t;X_t)\\
&\le
n\mathsf C_W.
\end{aligned}
\tag{22}
\]

Fano's inequality for estimating the uniform `N_n`-valued variable `A` from `X^n` gives

\[
H(A\mid X^n)
\le
h(e_n^*)+e_n^*\log(N_n-1),
\tag{23}
\]

where `h` is binary entropy in nats. Since `H(A)=log N_n`, `h(e)<=log2`, and `log(N_n-1)<=log N_n`,

\[
\log N_n
\le
I(A;X^n)+\log2+e_n^*\log N_n.
\tag{24}
\]

Using `(22)` and rearranging proves `(15)`. Equation `(17)` follows directly from `(16)`.

This converse is deliberately a statement about `C_n/N_n`, equivalently whole-provenance decision survival. It does **not** imply an analogous upper bound for `Lambda_n/N_n`: AF-160's convex-hull penalty may still separate `Lambda_n` from the Shtarkov mass when the codebook is not reliably decodable.

## Provenance controls

### One shared identity

For AF-162's diagonal family

\[
\mathcal A_n=\{(i,\ldots,i):i\in[m]\},
\]

one has `N_n=m` and

\[
\varepsilon_n
=
\frac1m\sum_{i<j}R_{ij}^n
\longrightarrow0.
\tag{25}
\]

Thus `(11)` recovers the qualitative AF-162 conclusion `C_n,Lambda_n->m` and `G_n->1`. The provenance rate is zero, so there is no capacity obstruction.

### Full Cartesian recombination

For

\[
\mathcal A_n=[m]^n,
\]

`N_n=m^n` and the provenance rate is `log m`. Unless the one-use channel can transmit the input identity perfectly, `C_W<log m`, so `(17)` prevents whole-provenance success from tending to one. AF-161 is stronger for the exact barycentric radius in this special product case: it gives exact multiplicative growth rather than only the coding converse.

### Blockwise provenance

AF-163's partition model is the codebook in which one label is constant inside each block and labels may vary independently between blocks. For block sizes `r_1,\ldots,r_k`, its cardinality is `N=m^k`.

Put

\[
S_r:=\sum_{i,j=1}^mR_{ij}^r
=m+2\sum_{i<j}R_{ij}^r.
\tag{26}
\]

Because block affinities factor, the sum over all **ordered** pairs of admissible block-label words equals `prod_j S_{r_j}`. Removing the diagonal and dividing by two gives the exact codebook collision budget

\[
\boxed{
\varepsilon
=
\frac12
\left[
\prod_{j=1}^k
\left(
1+\frac2m\sum_{i<\ell}R_{i\ell}^{r_j}
\right)
-1
\right].
}
\tag{27}
\]

If `rho=max_{i!=j}R_ij`, then each factor is at most

\[
1+(m-1)\rho^{r_j}.
\tag{28}
\]

Hence AF-163's long-coherent-block condition

\[
\sum_j\rho^{r_j}\to0
\tag{29}
\]

implies `epsilon->0`. The earlier disappearance of the hull penalty is therefore accompanied by a direct decision interpretation: the admissible block-provenance word itself becomes asymptotically decodable. This identifies AF-163's partition theorem as one structured codebook regime rather than a separate provenance principle.

## Arithmetic/analytic stress test

Use the two-member local family already audited in AF-157--AF-163,

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right).
\tag{30}
\]

Its Hellinger affinity is

\[
R_{12}
=
\frac{9+2\sqrt2}{7\sqrt3}<1.
\tag{31}
\]

For the shared-identity codebook with two words, `(25)` tends to zero and the complete hidden identity becomes recoverable, agreeing with AF-162.

For the full Cartesian codebook `A_n={1,2}^n`, AF-161 gives the exact Shtarkov mass

\[
C_n=\left(\frac{25}{21}\right)^n,
\qquad
N_n=2^n,
\tag{32}
\]

so

\[
\boxed{
1-e_n^*
=
\frac{C_n}{N_n}
=
\left(\frac{25}{42}\right)^n
\longrightarrow0.
}
\tag{33}
\]

The two one-coordinate output laws both have full support, so observing `X` cannot determine the binary input label with zero conditional uncertainty. Hence the one-use channel capacity is strictly below `log2`, consistent with the positive-rate converse `(17)`.

This is still only a local arithmetic-derived channel model. It does not assert that a global Euler product, a family of rational primes, or any RH-facing representation literally forms a memoryless provenance code. The test isolates the proof obligation: before applying a local recovery modulus globally, derive the actual admissible identity patterns and the channel/compression law that transports them.

## Prior-art and novelty audit

No novelty is claimed for the coding-theory ingredients.

- Claude E. Shannon, **“A Mathematical Theory of Communication,”** *Bell System Technical Journal* 27 (1948), 379–423 and 623–656, DOI `10.1002/j.1538-7305.1948.tb01338.x` and `10.1002/j.1538-7305.1948.tb00917.x`, is the foundational source for discrete memoryless channel capacity and the coding theorem.
- Robert M. Fano, ***Transmission of Information: A Statistical Theory of Communication***, MIT Press/Wiley (1961), is the classical source for the error/conditional-entropy inequality used in `(23)--(24)` and for discrete-channel coding theory.
- Robert G. Gallager, **“A Simple Derivation of the Coding Theorem and Some Applications,”** *IEEE Transactions on Information Theory* 11(1), 3–18 (1965), DOI `10.1109/TIT.1965.1053730`, is direct classical prior art for block-code error bounds on discrete memoryless channels and the rate-versus-capacity distinction.
- Yu. M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175–186 (English translation, 1987), is the classical NML/minimax-regret source behind the Shtarkov mass used in AF-149--AF-163.
- Neri Merhav, **“On the Minimum Description Length Principle for Sources with Piecewise Constant Parameters,”** *IEEE Transactions on Information Theory* 39(6), 1962–1967 (1993), DOI `10.1109/18.265504`, is direct prior art for source models with parameter identity shared within segments and changing between segments; it already classicalizes the partition/change-point provenance model used in AF-163.
- The Bhattacharyya/Hellinger and classical hypothesis-testing literature already cited in AF-162 supplies the pair-affinity overlap bound underlying `(19)--(21)`.

Thus arbitrary constrained codebooks, MAP decoding, channel capacity, Fano converses, pairwise Bhattacharyya bounds, and NML/Shtarkov quantities are all established mathematics. The durable result here is an internal **dictionary and gate** for Arithmetic Fidelity: an admissible provenance relation is a codebook; `C/N` is exact whole-provenance decision survival; its affinity enumerator supplies a sufficient collective-separation test; and the retained local channel capacity supplies a necessary provenance-rate condition. This turns AF-163's call for a more general compatibility law into a precise theorem without claiming a new coding theorem.

## Boundaries and counterarguments

1. **Capacity is necessary, not sufficient.** A rate below `C_W` does not make an arbitrary predetermined codebook reliably decodable. Its geometry still matters. Equation `(8)` gives one explicit sufficient test, but it is not necessary and can be loose.

2. **The Fano gate controls Shtarkov/decision survival, not the full barycentric radius.** Above capacity, `(17)` forces `C_n/N_n` away from one but does not by itself force `Lambda_n/N_n` away from one or determine the hull penalty. These are distinct source-complexity axes.

3. **Whole-provenance recovery may be stronger than the destination requires.** A downstream RH-facing observable may consume only a quotient or witness class of the hidden pattern. Then `A_n` should first be quotiented by the actual decision target rather than paying to decode irrelevant identity coordinates.

4. **Memoryless product structure is a real hypothesis.** Equations `(21)--(22)` use conditional product laws. An arithmetic source with global analytic coupling, overlapping constraints, or non-product observations needs its own analogue; naming its admissible states a codebook does not import this theorem automatically.

5. **Uniform-prior decision survival is the normalization in `(4)`.** Other priors or weighted arithmetic alternatives lead to weighted envelope/decision quantities. They may be more natural in a concrete application and require a separately stated calibration.

6. **Pairwise distinct base laws are used only to keep provenance labels honest.** If some `P_i` coincide, quotient those labels first. Otherwise raw codebook cardinality counts identities that the retained channel never distinguished even at one coordinate.

## Research consequence

AF-163's next-step question can now be sharpened. For a proposed arithmetic local-to-global compression, do not ask only how many coordinates or blocks it has. Identify the actual admissible provenance family `A_n`, quotient away distinctions the endpoint does not consume, and then compare three scales:

\[
\log|\mathcal A_n|,
\qquad
\text{codebook overlap/interaction geometry},
\qquad
n\mathsf C_W.
\]

If the effective provenance rate exceeds the retained channel's capacity, full identity cannot survive asymptotically. If the normalized affinity collision budget vanishes, the entire admissible provenance family does survive and `Lambda_n` asymptotically collapses to the raw pattern count with no extra hull penalty. Between those regimes, the source-specific compatibility structure rather than a generic partition or Cartesian model must determine the useful recovery law.