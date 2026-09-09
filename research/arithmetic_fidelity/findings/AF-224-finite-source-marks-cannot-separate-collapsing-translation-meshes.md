# AF-224 — finite source marks cannot separate collapsing translation meshes

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `QUANTITATIVE-FIDELITY`, `MARKED-TRANSLATION-GATE`, `ZERO-ERROR-COLORING-BRIDGE`, `COORDINATE-RIGIDITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-221--AF-223 show that the rational-prime log-log tail cannot be spread by an exact or well-conditioned approximate reparameterization while preserving one faithful translation-difference profile. AF-223 leaves source-specific side information as one explicit escape. A **fixed finite source mark** does not provide that escape if the marked representation still shares one continuous sample coordinate.

Let `V` be a real normed space, `(Z,d_Z)` a metric space, `S\subset\mathbb R` a source set, and `A` a finite set of source marks. Let

\[
\lambda:S\to A,
\qquad
\Phi:\mathbb R\to V,
\qquad
\Psi:S\to V,
\qquad
f:\mathbb R\to Z,
\tag{1}
\]

with `\Phi` continuous at `0`. For each used mark `a\in A`, let

\[
F_a:V\to Z
\tag{2}
\]

be a mark-specific decoder. Suppose that, for some `\varepsilon\ge0`,

\[
\boxed{
 d_Z\!\left(
 F_{\lambda(v)}(\Phi(u)-\Psi(v)),
 f(u-v)
 \right)
 \le\varepsilon
 \qquad(u\in\mathbb R,\ v\in S).
}
\tag{3}
\]

For each used mark `a`, define its realized hidden states

\[
\mathcal R_a
:=
\{\Phi(u)-\Psi(v):u\in\mathbb R,\ v\in S,\lambda(v)=a\}
\tag{4}
\]

and its realized inverse-resolution modulus

\[
\omega_a(r)
:=
\sup\{\|x-y\|:
 x,y\in\mathcal R_a,
 d_Z(F_a(x),F_a(y))\le r\}.
\tag{5}
\]

Put

\[
\eta:=\max_{a\in\lambda(S)}\omega_a(2\varepsilon),
\tag{6}
\]

and assume `\eta<\infty`. Finally define the anchored sample modulus

\[
\Omega_0(r)
:=
\sup_{|h|\le r}\|\Phi(h)-\Phi(0)\|.
\tag{7}
\]

Continuity of `\Phi` at zero gives `\Omega_0(r)\to0` as `r\downarrow0`.

Then every same-mark pair satisfies the exact quantitative constraint

\[
\boxed{
\lambda(v)=\lambda(w)
\quad\Longrightarrow\quad
\|\Psi(v)-\Psi(w)\|
\le
\Omega_0(|v-w|)+\eta.
}
\tag{8}
\]

Consequently, suppose the hidden source coordinates are uniformly separated by some `c_*>\eta`:

\[
\|\Psi(v)-\Psi(w)\|\ge c_*
\qquad(v\ne w).
\tag{9}
\]

For any `r>0` such that

\[
\Omega_0(r)+\eta<c_*,
\tag{10}
\]

no two distinct source points at distance at most `r` may carry the same mark. If

\[
N_S(r)
:=
\sup_{x\in\mathbb R}
\#\big(S\cap[x,x+r]\big)
\in\mathbb N\cup\{\infty\},
\tag{11}
\]

then necessarily

\[
\boxed{
|A|\ge N_S(r).
}
\tag{12}
\]

Equivalently, the mark map is a proper coloring of the source proximity graph whose edges join pairs with `0<|v-w|\le r`. The local source density is therefore a lower bound on the required mark alphabet.

For the rational-prime Euler source

\[
S_{\mathbb P}
:=
\{v_p=-\log\log p:p\text{ prime}\},
\tag{13}
\]

one has

\[
\boxed{
N_{S_{\mathbb P}}(r)=\infty
\qquad\text{for every }r>0.
}
\tag{14}
\]

Hence no **fixed finite** mark alphabet can make `\Psi(S_{\mathbb P})` uniformly separated when `(3)` is uniformly well conditioned with `c_*>\eta`.

Two useful specializations are immediate.

1. In the exact case `\varepsilon=0`, if each `F_a` is injective on `\mathcal R_a`, then `\eta=0`. A finite source mark cannot turn the collapsing prime log-log mesh into a uniformly separated hidden source while retaining the marked translation representation `(3)`.

2. If every mark-specific decoder has the common lower-Lipschitz bound

\[
d_Z(F_a(x),F_a(y))\ge m\|x-y\|
\qquad(x,y\in\mathcal R_a)
\tag{15}
\]

for some `m>0`, then

\[
\eta\le\frac{2\varepsilon}{m}.
\tag{16}
\]

Therefore any finite-mark representation with uniform hidden separation `c_*>0` must satisfy the error floor

\[
\boxed{
\varepsilon\ge\frac{m c_*}{2}.
}
\tag{17}
\]

unless another hypothesis is abandoned.

Thus the simplest side-information escape from AF-223 is itself rigid: **a bounded mark alphabet cannot desingularize an arbitrarily dense source tail while preserving one shared continuous sample coordinate and uniformly resolvable marked translation decoders.** A marked rescue must pay through growing mark complexity, deteriorating inverse conditioning, nonvanishing error, a mark-dependent sample geometry, or departure from the translation-difference category.

## Derivation

### 1. Equal marks let two source points be compared at exactly the same target argument

Take distinct `v,w\in S` with

\[
\lambda(v)=\lambda(w)=a.
\tag{18}
\]

The key point is that full translation covariance in `(3)` lets us align their target arguments while keeping the sample coordinates near the fixed anchor `0`.

Use the sample value `u=0` for source point `v`, and use

\[
u'=w-v
\tag{19}
\]

for source point `w`. Then

\[
u-v=-v,
\qquad
u'-w=(w-v)-w=-v.
\tag{20}
\]

Thus both marked decoder outputs approximate the **same** target value `f(-v)`:

\[
d_Z(F_a(\Phi(0)-\Psi(v)),f(-v))\le\varepsilon,
\tag{21}
\]

\[
d_Z(F_a(\Phi(w-v)-\Psi(w)),f(-v))\le\varepsilon.
\tag{22}
\]

The triangle inequality gives

\[
d_Z\!\left(
F_a(\Phi(0)-\Psi(v)),
F_a(\Phi(w-v)-\Psi(w))
\right)
\le2\varepsilon.
\tag{23}
\]

Both hidden states lie in `\mathcal R_a`. By `(5)--(6)`,

\[
\|\Phi(0)-\Psi(v)-\Phi(w-v)+\Psi(w)\|
\le\eta.
\tag{24}
\]

Rearranging and applying the triangle inequality yields

\[
\|\Psi(v)-\Psi(w)\|
\le
\|\Phi(0)-\Phi(w-v)\|+\eta
\le
\Omega_0(|v-w|)+\eta,
\tag{25}
\]

which is `(8)`.

This anchored comparison is stronger than applying AF-223 separately inside every mark class. It requires neither density of the difference set inside a class nor a global Hyers-Ulam argument. The only sample regularity used is continuity at one common anchor.

### 2. Uniform hidden separation turns the mark into a graph coloring

Assume `(9)` and choose `r` satisfying `(10)`. If two distinct points `v,w` obey

\[
|v-w|\le r,
\tag{26}
\]

then `(8)` would give, whenever they had the same mark,

\[
\|\Psi(v)-\Psi(w)\|
\le\Omega_0(r)+\eta
<c_*,
\tag{27}
\]

contradicting `(9)`. Therefore every pair at source distance at most `r` must receive different marks.

Define the proximity graph `G_r(S)` with vertex set `S` and an edge between distinct `v,w` whenever `|v-w|\le r`. The mark map `\lambda` is a proper coloring of this graph. Every subset of `S` contained in one interval `[x,x+r]` is a clique, so it needs pairwise distinct marks. Taking the supremum over `x` gives `(12)` directly.

No graph-theoretic perfection theorem is needed for this lower bound. The coloring language is useful because it identifies exactly what finite side information is doing: it partitions the source into classes that must avoid the confusable small-distance pairs forced by the translation representation.

### 3. Vanishing one-dimensional mesh makes every fixed proximity scale have unbounded local multiplicity

Let

\[
s_1>s_2>\cdots,
\qquad
s_n\to-\infty,
\tag{28}
\]

and suppose its consecutive mesh collapses:

\[
s_n-s_{n+1}\longrightarrow0.
\tag{29}
\]

Then, for every fixed `r>0`,

\[
N_S(r)=\infty
\tag{30}
\]

for `S=\{s_n:n\ge1\}`. Indeed, fix an arbitrary integer `M\ge1`. Choose `n` so far in the tail that

\[
s_j-s_{j+1}<\frac rM
\qquad(n\le j<n+M).
\tag{31}
\]

Then

\[
s_n-s_{n+M}
=
\sum_{j=n}^{n+M-1}(s_j-s_{j+1})
<r.
\tag{32}
\]

Thus the interval `[s_{n+M},s_n]` of length below `r` contains `M+1` source points. Since `M` was arbitrary, `(30)` follows.

This is the exact combinatorial obstruction behind the finite-mark failure. Pigeonhole alone already says that any block of `|A|+1` such points contains a same-mark pair; `(12)` packages the statement as a scale-dependent side-information lower bound.

### 4. The rational-prime log-log source has collapsing mesh

Write the rational primes as

\[
p_1<p_2<\cdots
\tag{33}
\]

and set

\[
s_n=v_{p_n}:=-\log\log p_n.
\tag{34}
\]

Then `s_n\downarrow-\infty`. If `p_n<p_{n+1}` are consecutive primes, Bertrand's postulate gives

\[
p_{n+1}<2p_n.
\tag{35}
\]

Hence

\[
\begin{aligned}
0<s_n-s_{n+1}
&=
\log\frac{\log p_{n+1}}{\log p_n}\\
&<
\log\!\left(1+\frac{\log2}{\log p_n}\right)
\longrightarrow0.
\end{aligned}
\tag{36}
\]

Applying the previous step proves `(14)`.

The prime input is deliberately weak. No prime number theorem or prime-gap conjecture is needed. The same marked-translation obstruction applies to every ordered source with vanishing mesh.

### 5. Quantitative decoder conditioning gives the error floor

Assume `(15)`. Whenever two realized states of the same mark have output distance at most `2\varepsilon`, the lower-Lipschitz inequality gives

\[
\|x-y\|
\le\frac{2\varepsilon}{m}.
\tag{37}
\]

Therefore `(16)` holds. If a finite-mark prime-tail representation also had `c_*>2\varepsilon/m`, continuity at zero would provide an `r>0` such that

\[
\Omega_0(r)+\frac{2\varepsilon}{m}<c_*.
\tag{38}
\]

But `(14)` and `(12)` would then require infinitely many marks, contradicting finiteness of `A`. Thus every such finite-mark representation must have

\[
c_*\le\frac{2\varepsilon}{m},
\tag{39}
\]

which is equivalent to `(17)`.

This should be interpreted as a conditioning tradeoff, not as a universal approximation lower bound. A decoder can evade `(17)` by becoming poorly conditioned on the realized fibers, and a representation can evade it by dropping uniform hidden separation. Both are genuine changes in the fidelity resource being claimed.

## Relation to the current Arithmetic Fidelity frontier

AF-221 rules out nonlinear scalar coordinate stretching inside an exact faithful translation profile. AF-222 shows that a vector-valued hidden coordinate still collapses to one affine direction when the retained profile is injective on realized states. AF-223 makes that rigidity stable under approximate observation whenever the decoder has a finite inverse-resolution modulus.

AF-224 addresses the first explicit escape left by AF-223: source-specific side information. The result does **not** claim that marks are useless. It says that a *fixed finite* mark can only color finitely many local confusability classes, while the rational-prime log-log tail develops arbitrarily large source cliques at every fixed continuity scale. Finite marking therefore cannot create a uniform source-separation resource inside the same marked translation category.

This sharpens the next admissibility question. A source mark intended to rescue prime-tail conditioning now needs a declared complexity law. Its alphabet must grow with the local source multiplicity, or its expected/entropy cost must be analyzed under a nonuniform source distribution. Merely saying that the construction is "marked" is no longer enough to evade the translation-mesh obstruction.

The result also connects naturally to the broader Arithmetic Fidelity distinction between exact information and useful conditioning. A mark may retain source identity set-theoretically while still failing to provide a uniformly resolvable geometric coordinate. Here the obstruction is quantified by the three resources visible in `(8)`: sample continuity scale, decoder inverse resolution, and mark alphabet complexity.

## Exact controls and boundaries

### The theorem constrains finite marks, not arbitrary side information

A countably infinite or scale-growing mark alphabet can color the proximity graph. AF-224 does not determine whether such a mark has finite entropy, finite expected description length, or any intrinsic arithmetic meaning. Those are separate resource questions; a growing alphabet is not automatically disqualified.

### The shared sample coordinate is load bearing

All marks use the same `\Phi`. If the sample representation itself becomes mark dependent, say `\Phi_a(u)`, the anchored comparison `(21)--(25)` no longer produces one common modulus. That is a different marked category and requires its own fidelity audit.

### Uniform inverse resolution is load bearing

The quantity `\eta` is a maximum over the finitely many used marks. If one mark-specific decoder develops arbitrarily large realized fibers at output scale `2\varepsilon`, same-target output agreement no longer forces nearby hidden states. Such ill-conditioning is an allowed escape, but it explicitly gives up the claimed stable fidelity.

### Uniform hidden separation is the target resource being ruled out

The theorem does not say that a finite mark cannot preserve any arithmetic predicate or finite discriminator. It says that it cannot turn a source whose local multiplicity diverges at every fixed scale into a uniformly separated hidden source under `(3)`. A proposed RH mechanism that needs a different retained property must state and test that property directly.

### The mark may be viewed as an explicit component of the hidden state

If the actual retained state is `(\Phi(u)-\Psi(v),\lambda(v))` and the decoder is one map `F(x,a)`, set `F_a(x):=F(x,a)`. Same-mark pairs still obey `(8)`. Giving different marks an arbitrary positive metric separation does not help because the obstruction always selects a pair with the **same** mark.

### Full translation covariance is essential

Equation `(3)` is required for every real `u`. The anchor choice `u=0`, `u'=w-v` uses this freedom. A finite sampled matrix, one-sided sample domain, or source-dependent sample window may avoid the argument. Such a model no longer inherits AF-224 automatically.

### Collapsing mesh, not primality, drives the negative theorem

Primes enter only through `(36)`. The positive obstruction applies to every source sequence with vanishing consecutive spacing. Rational-prime specificity would have to enter through an additional source law or relational structure beyond this generic metric crowding.

## Prior art and novelty assessment

The coloring language is classical zero-error information theory. H. S. Witsenhausen, **“The Zero-Error Side Information Problem and Chromatic Numbers,”** *IEEE Transactions on Information Theory* **22**(5), 592--593 (1976), DOI `10.1109/TIT.1976.1055607`, identifies a zero-error side-information problem with graph coloring in the nontrivial information pattern. Noga Alon and Alon Orlitsky, **“Source Coding and Graph Entropies,”** *IEEE Transactions on Information Theory* **42**(5), 1329--1339 (1996), DOI `10.1109/18.532875`, develops the corresponding chromatic/graph-entropy language for one-shot and repeated source coding.

AF-224 is not presented as a new graph-coloring theorem. The proximity graph, clique lower bound, and finite-pigeonhole step are elementary. The neighboring zero-error literature is used to classify the side mark correctly as a coloring resource rather than to claim a new coding principle.

The analytic ingredient is also elementary: continuity of the shared sample coordinate at one anchor converts a small source displacement into a small hidden sample displacement. The prime-tail input is the classical Bertrand bound already used in AF-221--AF-223; Ramanujan's 1919 proof of Bertrand's postulate is more than sufficient for `(36)`.

A targeted literature search located the classical zero-error/chromatic and graph-entropy frameworks but did not identify a source needed for the specific marked translation inequality `(8)` or its rational-prime log-log specialization. Absence of a located reference is not evidence of novelty. The durable contribution is therefore conservative: **an exact category-specific reduction of the finite-mark escape to a source-density coloring bound**, assembled from elementary continuity, inverse-resolution, and classical zero-error coloring ideas.

## Consequence for the research line

The translation-rigidity branch now has a clearer escape hierarchy. Scalar nonlinear stretching is closed by AF-221; unused vector dimension is closed by AF-222; stable approximate stretching is closed by AF-223; and fixed finite source marking is closed by AF-224 whenever the intended repair is uniform hidden separation with well-conditioned marked decoders.

The remaining marked escape is no longer qualitative. It must expose a real new resource: **growing provenance complexity versus source scale**, nonuniform information cost, mark-dependent geometry, or a nontranslation relation. For a prime-facing construction, the next useful question is therefore not whether a mark can be attached, but whether its required complexity is intrinsically arithmetic and survives the downstream compression more cheaply than carrying the discarded source identity itself.