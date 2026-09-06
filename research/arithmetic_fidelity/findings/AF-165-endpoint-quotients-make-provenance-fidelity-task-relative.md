# AF-165 — Endpoint quotients make provenance fidelity task-relative

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `DECISION-RELATIVE`, `COMPOSITION-LAW`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-164 gives exact sufficient and necessary gates for recovering an entire admissible provenance word from a compressed observation. That whole-word question is sometimes stronger than the downstream mathematics actually needs. If the endpoint consumes only a declared function of provenance, then collisions inside one endpoint class are irrelevant to that target and must not be counted as fidelity failures.

Use the AF-164 setup. Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite alphabet `X`, regarded as the discrete memoryless channel

\[
W(x\mid i)=P_i(x).
\tag{1}
\]

For each `n`, let

\[
\mathcal A_n\subseteq[m]^n,
\qquad
N_n:=|\mathcal A_n|,
\]

and for `a=(a_1,\ldots,a_n)` write

\[
Q_a(x^n)=\prod_{t=1}^nP_{a_t}(x_t).
\tag{2}
\]

Let `A` be uniform on `A_n`, and draw `X^n` from `Q_A`. Now declare an endpoint discriminator

\[
f_n:\mathcal A_n\to\mathcal D_n,
\qquad
D=f_n(A).
\tag{3}
\]

For each endpoint value `d`, put

\[
\mathcal A_{n,d}:=f_n^{-1}(d),
\qquad
M_d(x^n):=\sum_{a\in\mathcal A_{n,d}}Q_a(x^n),
\tag{4}
\]

and define the **endpoint-envelope mass**

\[
C_{f,n}:=\sum_{x^n}\max_{d\in\mathcal D_n}M_d(x^n).
\tag{5}
\]

If `e_{f,n}^*` is the optimal Bayes error for recovering only `D=f_n(A)` from `X^n`, then exactly

\[
\boxed{
\frac{C_{f,n}}{N_n}=1-e_{f,n}^*.
}
\tag{6}
\]

Thus AF-164's normalized Shtarkov mass is the special case `f_n=id`. At the opposite extreme, if `f_n` is constant, then `C_{f,n}=N_n` and the endpoint is perfectly preserved even when the full provenance word is unrecoverable.

More generally, endpoint coarsening is monotone. If

\[
g_n=h_n\circ f_n,
\tag{7}
\]

then

\[
\boxed{
C_n\le C_{f,n}\le C_{g,n}\le N_n,
}
\tag{8}
\]

where `C_n` is AF-164's ordinary Shtarkov mass for whole-provenance decoding. Forgetting distinctions that the endpoint does not consume can only make the declared endpoint easier to recover.

The AF-164 overlap gate also has an exact endpoint-relative refinement. Define the one-use Hellinger/Bhattacharyya affinities

\[
R_{ij}:=\sum_x\sqrt{P_i(x)P_j(x)}.
\tag{9}
\]

Then

\[
\boxed{
e_{f,n}^*
\le
\min\{1,\varepsilon_{f,n}\},
}
\tag{10}
\]

where

\[
\varepsilon_{f,n}
:=
\frac1{N_n}
\sum_{\substack{\{a,b\}\subseteq\mathcal A_n\\f_n(a)\ne f_n(b)}}
\prod_{t=1}^nR_{a_tb_t}.
\tag{11}
\]

Only **cross-endpoint** pairs appear. Arbitrarily large ambiguity among provenance words with the same endpoint value contributes exactly nothing to this sufficient fidelity budget.

There is likewise a task-specific capacity gate. Let

\[
K_n:=|f_n(\mathcal A_n)|,
\]

and let `C_W` be the one-use Shannon capacity of `(1)`, in nats. Since `D=f_n(A)`,

\[
I(D;X^n)\le I(A;X^n)\le n\mathsf C_W.
\tag{12}
\]

Fano's inequality therefore gives, for `K_n>=2`,

\[
\boxed{
H(D)
\le
n\mathsf C_W+\log2+e_{f,n}^*\log K_n.
}
\tag{13}
\]

Because `K_n<=m^n`, reliable endpoint recovery implies the necessary entropy-rate condition

\[
\boxed{
e_{f,n}^*\to0
\quad\Longrightarrow\quad
\limsup_{n\to\infty}\frac{H(D)}n
\le\mathsf C_W.
}
\tag{14}
\]

When the endpoint classes have equal size, `D` is uniform on `K_n` values and `(13)` becomes

\[
\boxed{
1-e_{f,n}^*
\le
\min\left\{
1,
\frac{n\mathsf C_W+\log2}{\log K_n}
\right\}.
}
\tag{15}
\]

Hence if

\[
\frac1n\log K_n\longrightarrow R_f>\mathsf C_W,
\tag{16}
\]

then

\[
\boxed{
\limsup_{n\to\infty}(1-e_{f,n}^*)
\le
\frac{\mathsf C_W}{R_f}<1.
}
\tag{17}
\]

The decisive change from AF-164 is that the necessary rate is the complexity of the **endpoint quotient**, not the number of hidden provenance words. Whole-provenance capacity can be exponentially insufficient while the downstream discriminator is recovered exactly.

## Derivation

### Endpoint decoding is Bayes classification of the quotient experiment

Let

\[
n_d:=|\mathcal A_{n,d}|,
\qquad
\pi_d:=\frac{n_d}{N_n},
\qquad
\bar Q_d:=\frac1{n_d}M_d.
\tag{18}
\]

Then `pi_d` is the prior probability of endpoint value `d` and `bar Q_d` is the conditional law of `X^n` given `D=d`. The Bayes success probability is therefore

\[
\begin{aligned}
1-e_{f,n}^*
&=
\sum_{x^n}\max_d\pi_d\bar Q_d(x^n)\\
&=
\frac1{N_n}
\sum_{x^n}\max_dM_d(x^n)\\
&=
\frac{C_{f,n}}{N_n},
\end{aligned}
\tag{19}
\]

which proves `(6)`.

If `f_n=id`, every class contains one word and `M_a=Q_a`, so `(5)` is exactly AF-164's Shtarkov mass `C_n`. If `f_n` is constant, the sole aggregate likelihood is

\[
M_*(x^n)=\sum_aQ_a(x^n),
\]

whose total mass is `N_n`; hence `C_{f,n}=N_n`.

For `(8)`, if `g=h\circ f`, each `g`-aggregate is a sum of `f`-aggregates:

\[
M_c^{(g)}(x^n)
=
\sum_{d:h(d)=c}M_d^{(f)}(x^n).
\tag{20}
\]

Pointwise,

\[
\max_cM_c^{(g)}(x^n)
\ge
\max_dM_d^{(f)}(x^n),
\]

so summing proves `C_g>=C_f`. The two endpoint cases above give the outer bounds.

### Only cross-endpoint overlap can cause endpoint classification error

For nonnegative numbers `(r_d)`,

\[
\sum_dr_d-\max_dr_d
\le
\sum_{d<e}\sqrt{r_dr_e}.
\tag{21}
\]

Applying `(21)` pointwise to

\[
r_d=M_d(x^n)
\]

and summing gives

\[
e_{f,n}^*
\le
\frac1{N_n}
\sum_{d<e}
\sum_{x^n}\sqrt{M_d(x^n)M_e(x^n)}.
\tag{22}
\]

Equivalently, this first bound is

\[
e_{f,n}^*
\le
\sum_{d<e}
\sqrt{\pi_d\pi_e}\,
\operatorname{Aff}(\bar Q_d,\bar Q_e),
\tag{23}
\]

where

\[
\operatorname{Aff}(P,Q):=\sum_x\sqrt{P(x)Q(x)}.
\]

To reduce `(22)` to the underlying provenance words, use

\[
\sqrt{
\left(\sum_{a\in\mathcal A_{n,d}}Q_a\right)
\left(\sum_{b\in\mathcal A_{n,e}}Q_b\right)
}
\le
\sum_{a\in\mathcal A_{n,d}}
\sum_{b\in\mathcal A_{n,e}}
\sqrt{Q_aQ_b}.
\tag{24}
\]

For product laws,

\[
\sum_{x^n}\sqrt{Q_a(x^n)Q_b(x^n)}
=
\prod_{t=1}^nR_{a_tb_t}.
\tag{25}
\]

Substituting `(24)--(25)` into `(22)` proves `(10)--(11)`.

If

\[
\rho:=\max_{i\ne j}R_{ij}<1,
\]

then AF-164's Hamming estimate yields the useful corollary

\[
\varepsilon_{f,n}
\le
\frac1{N_n}
\sum_{\substack{\{a,b\}\subseteq\mathcal A_n\\f_n(a)\ne f_n(b)}}
\rho^{d_H(a,b)}.
\tag{26}
\]

The distance geometry that matters is therefore the distance **between endpoint classes**. Dense clusters inside one class may be completely harmless.

### Capacity applies to endpoint entropy, not hidden-source cardinality

The Markov relation

\[
D=f_n(A)\longleftarrow A\longrightarrow X^n
\]

gives the first inequality in `(12)` by data processing. AF-164 already proves

\[
I(A;X^n)\le n\mathsf C_W
\]

for an arbitrary codebook distribution induced by uniform `A`, because the coordinates of `A` may be dependent while the channel remains memoryless conditional on `A`.

Fano gives

\[
H(D\mid X^n)
\le
h(e_{f,n}^*)+e_{f,n}^*\log(K_n-1)
\le
\log2+e_{f,n}^*\log K_n.
\tag{27}
\]

Since

\[
H(D)=I(D;X^n)+H(D\mid X^n),
\]

combining `(12)` and `(27)` proves `(13)`. Because `K_n<=N_n<=m^n`, `e_{f,n}^*\log K_n/n` tends to zero whenever `e_{f,n}^*\to0`, giving `(14)`.

If the fibers of `f_n` have equal cardinality, uniform `A` makes `D` uniform and `H(D)=\log K_n`. Rearranging `(13)` proves `(15)`, and `(17)` follows from `(16)`.

The converse is deliberately one-sided. A small endpoint entropy or a rate below capacity does **not** prove recoverability. The cross-class overlap geometry in `(10)--(11)`, or another direct reconstruction argument, is still needed for an achievability claim.

## Decisive matched control: exact endpoint fidelity with exponentially lost provenance

Take one-use provenance symbols

\[
i=(u,v)\in\{0,1\}^2
\]

and let the retained output be

\[
Y=(u,z),
\qquad
z=v\oplus N,
\tag{28}
\]

where `N` is Bernoulli with

\[
0<p:=\mathbb P(N=1)<\frac12.
\]

Thus the first bit is transmitted noiselessly while the second passes through a binary symmetric channel. The four one-use laws `P_{u,v}` are distinct.

Use the full Cartesian codebook

\[
\mathcal A_n=(\{0,1\}^2)^n
\]

with the uniform prior. Whole provenance is

\[
A=(U^n,V^n).
\]

The optimal decoder observes `U^n` exactly and chooses `V^n=Z^n`. Therefore

\[
\boxed{
1-e_n^*=(1-p)^n\longrightarrow0.
}
\tag{29}
\]

So AF-164's whole-provenance fidelity vanishes exponentially. The same conclusion is visible from the one-use capacity. With natural logarithms,

\[
\mathsf C_W
=2\log2-h(p)
<2\log2,
\tag{30}
\]

where

\[
h(p)=-p\log p-(1-p)\log(1-p).
\]

The full provenance rate is `2 log 2`, strictly above capacity.

Now declare the endpoint

\[
f_n(U^n,V^n)=U^n.
\tag{31}
\]

This endpoint is literally present as the first coordinate of the retained observation, so

\[
\boxed{
e_{f,n}^*=0,
\qquad
C_{f,n}=N_n
\quad\text{for every }n.
}
\tag{32}
\]

The overlap test sees the same fact exactly. If two provenance words have different endpoint values `U^n`, then at some coordinate their `u` bits differ. The corresponding one-use laws have disjoint support in the first output coordinate, so that factor in `(11)` is zero. Hence

\[
\boxed{
\varepsilon_{f,n}=0
}
\tag{33}
\]

although words inside each fixed-`U^n` class remain exponentially numerous and can be highly confusable through the noisy `V` coordinates.

This kills the inference

\[
\text{whole provenance is above capacity}
\Longrightarrow
\text{the downstream discriminator is lost}.
\]

The implication is valid only when the downstream discriminator separates the provenance alternatives whose recovery was declared.

## Arithmetic/analytic stress test: the divisor quotient

AF-017 gives a concrete arithmetic version of the same logical distinction. Exact Euler-product value data recover the unordered generator-norm multiset under the stated hypotheses, but Grosswald--Schnitzer modified Euler products can change those generator norms while preserving the complete zero/pole divisor in `Re(s)>0`.

If the declared endpoint is **only the meromorphic divisor**, those modified norm systems lie inside one endpoint class. Their different prime-norm provenance does not by itself refute fidelity to that divisor: the endpoint quotient intentionally identifies them.

If instead the claimed endpoint is the ordinary rational-prime norm system, Euler coefficients, von Mangoldt data, or another discriminator that separates the Grosswald--Schnitzer controls, then the same-divisor compression places different endpoint values on the same retained observation and is genuinely non-faithful for that target.

This distinction matters for RH-facing arguments. A same-divisor generalized-prime control does not automatically refute a theorem whose conclusion depends only on that divisor. It does refute any stronger claim that the divisor alone recovers or certifies the ordinary rational-prime source. Therefore the endpoint equivalence relation has to be declared **before** using a provenance collision as a no-go theorem.

## Prior art and novelty assessment

The underlying principle is classical: preserving a specified decision/function can require strictly less information than reconstructing the entire source.

- Alon Orlitsky and James R. Roche, **“Coding for Computing,”** *IEEE Transactions on Information Theory* 47(3), 903--917 (2001), DOI `10.1109/18.915643`, develops function-specific compression and characteristic-graph entropy rather than requiring complete source reconstruction. This source is already anchored in `SOURCES.md` for AF-001 and AF-011.
- AF-127--AF-129 already place recovery deficiency relative to declared decision/witness classes, and AF-155 shows that Shtarkov-mass contraction itself is one restricted Bayes decision defect. The general slogan that fidelity is task-relative is therefore not new here.
- AF-164 already audits the Shannon/Fano capacity and Hellinger/Bhattacharyya ingredients used above for whole-provenance codebooks. Equations `(10)--(17)` are their endpoint-quotient specialization and extension, not a new coding theorem.

The Arithmetic Fidelity contribution is the exact **placement of the quotient inside the provenance-codebook gate**. AF-164 counts all admissible identity patterns because its declared task is whole-word recovery. AF-165 shows how that gate changes when the downstream theorem consumes only `f_n(A)`: the envelope aggregates likelihoods inside endpoint classes, the sufficient collision budget drops every within-class pair, and the converse uses endpoint entropy/cardinality rather than hidden provenance cardinality. The matched control `(28)--(33)` proves that this distinction can change the fidelity verdict from exponentially bad to exact.

No novelty is claimed for Bayes classification, Fano's inequality, data processing, function computation, or Bhattacharyya-type error bounds.

## Boundary conditions and falsification checks

- The source prior in the main codebook formulation is uniform on `A_n`. Unequal priors have the same quotient-experiment interpretation after weighting the aggregates, but the formulas must use those weights rather than raw class counts.
- `f_n` must represent a mathematically declared downstream discriminator. Choosing it after seeing a collision merely to merge inconvenient controls is not a legitimate repair.
- Endpoint fidelity is only as strong as the endpoint. Recovering a coarse `f_n(A)` says nothing about provenance distinctions that `f_n` deliberately discards.
- Conversely, failure of whole-provenance recovery is not an obstruction unless the downstream theorem actually needs those distinctions.
- The cross-pair quantity `epsilon_{f,n}` is sufficient, not necessary. Large or nonvanishing pairwise affinity budgets do not prove endpoint failure because the union-style bound can be loose.
- The capacity/entropy gate is necessary, not sufficient. A low-rate endpoint may still be unrecoverable because the channel collapses exactly the endpoint classes that need separation.
- The memoryless product law `(2)` is essential to the factorization in `(25)` and to the one-use capacity bound. Arithmetic applications must derive their actual composition law rather than import an i.i.d. provenance model by analogy.
- The Grosswald--Schnitzer stress test distinguishes a divisor-only endpoint from a rational-prime-source endpoint. It does not say that a proof of RH must reconstruct the prime norms from its final zero data, nor that every zero-based mechanism is invalid.

## Decisive audit test

Before applying a provenance or capacity obstruction to a concrete compression chain:

1. state the downstream discriminator `f` whose recovery the mathematical conclusion genuinely requires;
2. quotient the admissible controls by equality of that discriminator;
3. test only collisions that cross the resulting endpoint classes;
4. use endpoint entropy/rate, not hidden-source cardinality, in any capacity converse;
5. separately prove that the chosen endpoint is strong enough for the intended arithmetic or analytic conclusion.

A whole-provenance no-go is decisive only when the endpoint is injective on the relevant provenance class or when an independent theorem shows that complete provenance recovery is necessary.

## Consequence for the line

The current provenance frontier should no longer ask only how many hidden identities can recombine. It should first ask **which equivalence classes of those identities the endpoint actually consumes**.

The correct source audit is therefore two-stage: classify the admissible provenance codebook, then quotient it by the declared downstream discriminator. Whole-source complexity remains the conservative upper requirement, but endpoint-relative cross-class geometry and endpoint entropy are the relevant fidelity gates for a specific theorem.

For arithmetic applications, this prevents two opposite mistakes: demanding recovery of irrelevant source provenance and, conversely, declaring a coarse endpoint faithful when the intended RH mechanism secretly needs finer rational-prime structure than that endpoint retains.