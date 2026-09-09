# AF-225 — fixed-resolution prime-tail marks carry asymptotically full source identity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `QUANTITATIVE-FIDELITY`, `MARK-COMPLEXITY`, `ZERO-ERROR-COLORING`, `CHROMATIC-ENTROPY`, `NO-NOVELTY-CLAIM`

## Claim

AF-224 reduces any uniformly separated, uniformly resolvable marked translation repair to a proper coloring of the source proximity graph at some fixed source scale. That lower bound is exact at the combinatorial level, and on the rational-prime log-log source it is asymptotically as expensive as retaining the source identity itself.

Let `S` be a finite subset of `R` and let `r>0`. Define the proximity graph

\[
G_r(S):\qquad s\sim t
\iff
0<|s-t|\le r,
\tag{1}
\]

and the maximal local multiplicity

\[
M_S(r):=\max_{x\in\mathbb R}\#\bigl(S\cap[x,x+r]\bigr).
\tag{2}
\]

Define the minimum number of proximity marks by

\[
K_r(S)
:=
\min_{\lambda:S\to A}
|\lambda(S)|,
\tag{3}
\]

where the minimum is over marks satisfying

\[
\lambda(s)=\lambda(t),\ s\ne t
\quad\Longrightarrow\quad
|s-t|>r.
\tag{4}
\]

Then

\[
\boxed{K_r(S)=\chi(G_r(S))=M_S(r).}
\tag{5}
\]

Thus AF-224's local-density lower bound has no hidden graph-coloring slack: for a one-dimensional source, maximal occupancy of an `r`-window is exactly the minimum alphabet size required merely to avoid same-mark confusability at scale `r`.

Now specialize to the rational-prime log-log source truncated at `Q`:

\[
S_Q
:=
\{-\log\log p:p\le Q,\ p\text{ prime}\},
\qquad
n_Q:=|S_Q|=\pi(Q).
\tag{6}
\]

Fix `r>0` and put

\[
a:=e^{-r}\in(0,1).
\tag{7}
\]

All primes in the power interval

\[
Q^a<p\le Q
\tag{8}
\]

map into one source interval of length `r`. Hence they form a clique in `G_r(S_Q)`, so

\[
K_r(S_Q)
\ge
\pi(Q)-\pi(Q^a).
\tag{9}
\]

By the prime number theorem,

\[
\frac{\pi(Q^a)}{\pi(Q)}
\sim
\frac{1}{a}Q^{a-1}
\longrightarrow0.
\tag{10}
\]

Since trivially `K_r(S_Q)\le\pi(Q)`, one obtains

\[
\boxed{
K_r(S_Q)
\sim
\pi(Q)
\sim
\frac{Q}{\log Q}.
}
\tag{11}
\]

Equivalently, any proximity mark at a fixed nonzero source resolution uses asymptotically one distinct mark per prime in cardinality scale. A fixed-length encoding of the used mark alphabet therefore requires

\[
\boxed{
\log_2 K_r(S_Q)
=
\log_2 Q-\log_2\log Q+o(1),
}
\tag{12}
\]

which is the same asymptotic fixed-length cost as indexing the prime source itself.

The conclusion is stronger under the uniform distribution on primes up to `Q`. Let `P_Q` be uniform on `{p:p\le Q, p prime}` and let `\lambda_Q` be any proper proximity mark satisfying `(4)` on `S_Q`. Then there is a decoder from the mark alone whose prime-identification error is at most

\[
\delta_Q
:=
\frac{\pi(Q^a)}{\pi(Q)}
\longrightarrow0.
\tag{13}
\]

Moreover, with entropy in natural logarithms,

\[
\boxed{
H(\lambda_Q(-\log\log P_Q))
=
\log\pi(Q)-o(1).
}
\tag{14}
\]

Thus, under the natural uniform finite-cutoff source, a mark capable of repairing the fixed-resolution AF-224 confusability does not merely need an unbounded alphabet: it asymptotically carries the full prime-source identity, both in one-shot alphabet size and in entropy. In this category, growing provenance is therefore not a genuinely cheaper compression repair.

## Derivation

### 1. The one-dimensional proximity graph has exact coloring cost `M_S(r)`

Every subset of `S` contained in an interval of length `r` is a clique of `G_r(S)`. Therefore

\[
\chi(G_r(S))\ge M_S(r).
\tag{15}
\]

For the reverse inequality, order the source points increasingly:

\[
s_1<s_2<\cdots<s_n.
\tag{16}
\]

Color greedily in this order using a palette of `M_S(r)` colors. When `s_i` is reached, every earlier neighbor lies in

\[
[s_i-r,s_i),
\tag{17}
\]

so those earlier neighbors together with `s_i` lie in one interval of length `r`. There are therefore at most `M_S(r)-1` earlier neighbors. At most that many colors are forbidden, and one of the `M_S(r)` colors remains available.

Hence

\[
\chi(G_r(S))\le M_S(r),
\tag{18}
\]

which proves `(5)`.

Equivalently, represent `s\in S` by the unit-length-at-scale-`r` interval `[s,s+r]`. Two such intervals intersect exactly when the source points are at distance at most `r`, so `G_r(S)` is a unit interval graph. Equality of clique and chromatic number is the classical perfectness of interval graphs; the greedy proof above records the exact specialization needed here without importing stronger graph theory.

### 2. A fixed log-log window near `Q` contains almost every prime below `Q`

Let

\[
v(x):=-\log\log x.
\tag{19}
\]

For `Q^a<p\le Q`, one has

\[
a\log Q<\log p\le\log Q.
\tag{20}
\]

Taking logarithms and using `\log a=-r` gives

\[
\log\log Q-r
<
\log\log p
\le
\log\log Q,
\tag{21}
\]

hence

\[
v(Q)
\le
v(p)
<
v(Q)+r.
\tag{22}
\]

Therefore the source points associated with all primes in `(Q^a,Q]` lie in one `r`-window and form a clique. This proves `(9)`.

The prime number theorem gives

\[
\pi(Q)
\sim
\frac{Q}{\log Q},
\qquad
\pi(Q^a)
\sim
\frac{Q^a}{a\log Q},
\tag{23}
\]

so `(10)` follows. Because `a<1`, the omitted lower-prime population is an asymptotically vanishing fraction of all primes below `Q`. Combining the clique lower bound with the trivial upper bound by one color per source point proves `(11)` and `(12)`.

This is the scale effect hidden by the qualitative statement `N_{S_P}(r)=infinity` in AF-224. A fixed additive window in the coordinate `-log log p` corresponds to the enormous multiplicative interval `(Q^{e^{-r}},Q]` in the prime variable. As `Q` grows, that one proximity clique contains a fraction tending to one of the entire truncated source.

### 3. The same giant clique forces near-full mark entropy

Let

\[
C_Q:=\{p:Q^a<p\le Q,\ p\text{ prime}\},
\tag{24}
\]

and let

\[
m_Q:=\pi(Q^a),
\qquad
n_Q:=\pi(Q),
\qquad
\delta_Q:=m_Q/n_Q.
\tag{25}
\]

Because `C_Q` is a clique, every proper mark `\lambda_Q` is injective on `C_Q`.

Construct a decoder `D_Q` from marks to primes as follows. For each mark used by `C_Q`, map that mark to its unique prime in `C_Q`; define the decoder arbitrarily on marks not used by `C_Q`. Whenever `P_Q\in C_Q`, this decoder is correct. Therefore

\[
\Pr\bigl[D_Q(\lambda_Q(v(P_Q)))\ne P_Q\bigr]
\le
\delta_Q,
\tag{26}
\]

which tends to zero by `(10)`.

For the entropy statement, let `B_Q` indicate whether `P_Q\in C_Q`. Since `P_Q` is uniform on the `n_Q` primes,

\[
H(P_Q)=\log n_Q.
\tag{27}
\]

Conditioned on `B_Q=1`, the pair `(\lambda_Q(v(P_Q)),B_Q)` determines `P_Q` exactly because the marking is injective on the clique. Conditioned on `B_Q=0`, there are at most `m_Q` possible primes. Thus

\[
H(P_Q\mid\lambda_Q(v(P_Q)))
\le
h(\delta_Q)+\delta_Q\log m_Q,
\tag{28}
\]

where `h` is the binary entropy in nats.

Because `\lambda_Q` is deterministic,

\[
H(\lambda_Q(v(P_Q)))
=
I(P_Q;\lambda_Q(v(P_Q)))
=
H(P_Q)-H(P_Q\mid\lambda_Q(v(P_Q))).
\tag{29}
\]

The prime-number-theorem estimate `(10)` gives

\[
\delta_Q\log m_Q
=
O\!\left(Q^{a-1}\log Q\right)
\longrightarrow0,
\tag{30}
\]

and `h(\delta_Q)\to0`. Therefore

\[
H(\lambda_Q(v(P_Q)))
\ge
\log n_Q-o(1).
\tag{31}
\]

The opposite inequality `H(\lambda_Q(v(P_Q)))\le\log n_Q` is automatic for a deterministic function of an `n_Q`-point source. This proves `(14)`.

The entropy conclusion is not merely a reformulation of the alphabet lower bound. A large alphabet can in general have very small entropy under a skewed source. Here the giant clique occupies probability `1-o(1)` under the uniform prime cutoff, so almost all of the source mass must also be separated by distinct marks.

## Application of AF-224

AF-224 assumes a marked translation representation with common sample coordinate `Phi`, mark-specific decoders, uniform approximation error `epsilon`, realized inverse-resolution defect `eta`, and a desired hidden source separation `c_*>eta`. Once one chooses any fixed `r>0` satisfying

\[
\Omega_0(r)+\eta<c_*,
\tag{32}
\]

AF-224 proves that every pair of distinct source points at distance at most `r` must receive different marks.

Therefore `(11)--(14)` apply to every finite prime cutoff of such a representation. If the same representation is intended uniformly along the prime tail, then the number of distinct marks actually used below `Q` must satisfy

\[
|\lambda(S_Q)|\ge(1-o(1))\pi(Q),
\tag{33}
\]

and, under the uniform cutoff distribution, the mark itself has entropy

\[
H(\lambda(v(P_Q)))=H(P_Q)-o(1).
\tag{34}
\]

This closes the simplest growing-alphabet escape left open by AF-224. At fixed source resolution and uniform conditioning, the mark asymptotically becomes a source identifier rather than a compressed structural lift.

## Exact controls and boundaries

### Fixed source resolution is load bearing

The theorem fixes `r>0`. If the admissible same-mark exclusion radius shrinks with `Q`, the clique `(Q^{e^{-r}},Q]` can occupy a smaller fraction of the prime cutoff. Quantifying that regime requires a declared scale law; sufficiently short moving intervals eventually require prime-distribution input stronger than the bare fixed-`r` prime number theorem.

In AF-224 language, such a shrinking `r` corresponds to allowing the separation margin, sample continuity modulus, approximation error, or inverse conditioning to deteriorate with source scale. That is a genuine fidelity cost, not a contradiction of AF-225.

### The entropy statement uses the uniform prime cutoff

The cardinality result `(11)` is distribution free. The near-full entropy statement `(14)` uses the uniform law on primes up to `Q`. A deliberately concentrated source distribution can assign negligible probability to the giant clique and have much smaller mark entropy. Any claimed low expected description cost must therefore state the source law rather than infer it from alphabet growth alone.

### Proper coloring is necessary, not sufficient, for the full representation

Equation `(5)` solves only the combinatorial marking problem produced by AF-224. A proper coloring does not construct `Phi`, `Psi`, the marked decoders, or a well-conditioned recovery. The actual marked translation representation may require strictly more side information than `K_r(S)`.

Thus the equality `K_r=M_S(r)` shows that AF-224's coloring lower bound is sharp as a coloring bound, not that every optimal coloring lifts to a valid analytic representation.

### The result is coordinate/category specific

The giant-clique asymptotic is a consequence of the source coordinate `v_p=-log log p` and the fixed-resolution translation category. A different source coordinate, mark-dependent sample geometry, nontranslation relation, or downstream objective that does not require uniform hidden separation lies outside the hypotheses and needs its own fidelity audit.

### Near-full identity cost is not rational-prime specificity

The theorem says that repairing this generic metric crowding by marks is almost as expensive as retaining prime identity. It does not show that the retained marks encode a specifically arithmetic invariant, nor that source identity itself survives a later RH-relevant compression. A useful arithmetic lift still needs an independently justified structural role downstream.

## Prior art and novelty assessment

The graph-theoretic part is classical. D. R. Fulkerson and O. A. Gross, **“Incidence Matrices and Interval Graphs,”** *Pacific Journal of Mathematics* **15**(3), 835--855 (1965), DOI `10.2140/pjm.1965.15.835`, is foundational interval-graph literature. Proximity graphs of points on a line are unit interval graphs, and equality of clique and chromatic number for interval graphs is standard; `(15)--(18)` is only the elementary greedy specialization needed here.

The zero-error and entropy languages are also established. H. S. Witsenhausen, **“The Zero-Error Side Information Problem and Chromatic Numbers,”** *IEEE Transactions on Information Theory* **22**(5), 592--593 (1976), DOI `10.1109/TIT.1976.1055607`, supplies the classical coloring interpretation of zero-error side information. Noga Alon and Alon Orlitsky, **“Source Coding and Graph Entropies,”** *IEEE Transactions on Information Theory* **42**(5), 1329--1339 (1996), DOI `10.1109/18.532875`, develops chromatic and graph entropy for source coding. Jean Cardinal, Samuel Fiorini, and Gwenaël Joret, **“Minimum Entropy Coloring,”** *Journal of Combinatorial Optimization* **16**(4), 361--377 (2008), DOI `10.1007/s10878-008-9152-2`, studies the minimum-entropy coloring problem directly, including interval graphs.

The arithmetic asymptotic uses only the classical prime number theorem `pi(x)~x/log x`, in the form established by Hadamard and de la Vallée-Poussin and recorded in standard analytic-number-theory references.

No novelty is claimed for interval-graph perfection, chromatic entropy, or the prime number theorem. A targeted prior-art check found these ingredients as mature theories. The durable Arithmetic Fidelity result is the exact category-specific consequence obtained by combining AF-224's marked-translation confusability radius with the crowding geometry of `-log log p`: **at any fixed positive fidelity radius, the admissible side mark separates a `1-o(1)` fraction of the entire truncated prime source and therefore carries asymptotically full source identity.** Absence of a located source for this exact specialization is not a novelty claim.

## Consequence for the research line

AF-224 left growing mark complexity and nonuniform information cost as possible escapes from the failure of fixed finite marks. AF-225 sharply narrows both at fixed fidelity radius. The required alphabet grows as `(1-o(1))pi(Q)`, and under a uniform prime cutoff the mark entropy differs from the full source entropy by `o(1)`.

Therefore a provenance-based repair inside the same uniformly conditioned translation category cannot claim meaningful compression merely because the mark alphabet is allowed to grow. To remain nontrivial, the next escape must change a load-bearing resource: let the effective source resolution shrink with scale, exploit a justified nonuniform source law, introduce mark-dependent geometry, abandon uniform hidden separation, or leave the translation-difference category.

This is a stronger minimal-lift audit than the qualitative statement that infinitely many marks are necessary. At fixed resolution, the lift is asymptotically a hidden copy of source identity under the most natural finite-cutoff distribution, exactly the tautological-recovery failure mode that the Arithmetic Fidelity mandate is intended to expose.