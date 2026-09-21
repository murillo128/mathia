# AF-465 — Uniform doubling is not a Hilbert-fidelity certificate

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-GEOMETRY`, `QUANTITATIVE-FIDELITY`, `NONLINEAR-TARGET`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-464 gives a clean metric obstruction to uniformly stable Hilbert recovery: if an admissible source family contains Hamming cubes of growing dimension with uniformly controlled source distortion, then every uniformly Lipschitz Hilbert-valued encoder has deteriorating inverse conditioning.

The converse fails strongly. **Excluding growing low-distortion Hamming cubes is not sufficient to certify uniform Hilbert fidelity.**

There is a classical family of finite weighted Laakso graphs `(L_n,d_n)` such that:

1. the family is uniformly doubling;
2. consequently it cannot contain Hamming cubes `Q_k=({0,1}^k,d_H)` of unbounded dimension with a distortion bound independent of `k`;
3. nevertheless its Euclidean/Hilbert distortion is unbounded:

\[
\sup_n c_2(L_n)=\infty,
\qquad
c_2(X)
=
\inf_f
\operatorname{Lip}(f)\,
\operatorname{Lip}(f^{-1}|_{f(X)}).
\tag{1}
\]

Thus the Hamming-cube certificate in AF-464 is a sufficient witness of Hilbert-fidelity failure, not a complete characterization of it. A thin or cube-poor arithmetic source can evade that particular certificate while still carrying other metric obstructions that force arbitrarily bad Hilbert conditioning.

## Why uniform doubling excludes uniformly distorted growing Hamming cubes

Let a metric space `X` have doubling constant at most `D`: every ball of radius `r` is coverable by at most `D` balls of radius `r/2`.

Suppose a metric space `S` admits a `K`-bi-Lipschitz embedding `f:S->X`. After rescaling the target metric, write

\[
d_S(x,y)
\le
d_X(fx,fy)
\le Kd_S(x,y).
\tag{2}
\]

Fix a source ball `B_S(x,r)`. Its image lies in `B_X(fx,Kr)`. Iterate the doubling cover until the target covering radius is at most `r/4`. This takes

\[
m=\left\lceil\log_2(4K)\right\rceil
\tag{3}
\]

steps and produces at most `D^m` target balls. For every nonempty target ball choose one image point as a center. Any two image points in the same target ball are at target distance at most `r/2`; by the lower inequality in `(2)` their source preimages are at distance at most `r/2`. Hence

\[
\lambda(S)
\le
D^{\lceil\log_2(4K)\rceil},
\tag{4}
\]

where `lambda(S)` denotes the doubling constant. In particular, a fixed-distortion subspace of a uniformly doubling family is uniformly doubling.

The Hamming cubes are not uniformly doubling. For example, set

\[
r_k=\lfloor k/4\rfloor,
\qquad
s_k=\lfloor k/8\rfloor.
\]

The ball around `0` of Hamming radius `r_k` has cardinality

\[
\sum_{j\le r_k}\binom{k}{j},
\]

whereas every Hamming ball of radius `s_k` has at most

\[
\sum_{j\le s_k}\binom{k}{j}
\]

points. Therefore any cover of the former by radius-`s_k` balls requires at least the quotient of these two volumes. Standard binomial-entropy asymptotics give

\[
\frac{\sum_{j\le k/4}\binom{k}{j}}
     {\sum_{j\le k/8}\binom{k}{j}}
=
\exp(c k+o(k))
\tag{5}
\]

for

\[
c=\bigl(H(1/4)-H(1/8)\bigr)\log 2>0,
\]

with `H` the binary entropy. Hence `lambda(Q_k)->infinity` exponentially. Combining this with `(4)`, no uniformly doubling family can contain `Q_k` for unbounded `k` with one common bi-Lipschitz distortion bound.

The weighted Laakso graph family is uniformly doubling, so it is automatically **AF-464-cube-poor** in precisely this bounded-distortion sense.

## Laakso graphs nevertheless have unbounded Hilbert distortion

The weighted Laakso graphs are a nested family of finite metric graphs whose isometric union is the infinite Laakso graph `L_omega`. Ostrovska and Ostrovskii record both the uniform doubling property of the finite family and the classical nonembeddability of `L_omega` into Banach spaces with the Radon–Nikodym property. Hilbert spaces have the Radon–Nikodym property.

For completeness, the infinite-space obstruction implies `(1)` directly. Suppose instead that

\[
\sup_n c_2(L_n)<\infty.
\]

Then for some fixed `K` and every `n` there is a Hilbert space `H_n` and, after rescaling and translating the embedding,

\[
d_n(x,y)
\le
\|f_n(x)-f_n(y)\|_{H_n}
\le
K d_n(x,y)
\qquad (x,y\in L_n),
\tag{6}
\]

with a common basepoint sent to `0`.

Take a nonprincipal ultraproduct `H_U` of the Hilbert spaces `H_n`. An ultraproduct of Hilbert spaces is again Hilbert. For each `x in L_omega`, the point belongs to every sufficiently large `L_n`; the sequence `f_n(x)` is then uniformly bounded because of `(6)`. Sending `x` to its ultraproduct class gives

\[
d_{L_\omega}(x,y)
\le
\|F(x)-F(y)\|_{H_U}
\le
K d_{L_\omega}(x,y).
\tag{7}
\]

This would be a bi-Lipschitz embedding of `L_omega` into a Hilbert space, contradicting the Radon–Nikodym nonembeddability theorem. Therefore the finite Hilbert distortions must diverge.

This gives the desired separation:

\[
\boxed{
\text{uniformly doubling / no uniform growing Hamming cubes}
\;\not\Rightarrow\;
\text{uniform Hilbert fidelity}.
}
\tag{8}
\]

## Strict relation to AF-464

AF-464 proves a source certificate of the form

\[
\text{large Hamming cubes}
\Longrightarrow
\text{Hilbert distortion blow-up}.
\]

AF-465 proves that the reverse diagnostic is invalid:

\[
\text{no large uniformly distorted Hamming cubes}
\centernot\Longrightarrow
\text{bounded Hilbert distortion}.
\]

So the escape route identified at the end of AF-464 — restrict the source enough to remove the paired-mixture cubes — is only a **necessary escape from that proof**, not a positive recovery theorem. The source can remain globally incompatible with Hilbert geometry for reasons not witnessed by those cubes.

This distinction matters for the Arithmetic Fidelity program. A negative certificate and its absence are not symmetric pieces of evidence. Removing one obstruction never establishes faithfulness unless a positive theorem controls the whole admissible source geometry.

## Source-metric boundary: snowflaking can repair the obstruction

The failure is genuinely metric rather than merely set-theoretic. Assouad's embedding theorem, in the dimension-independent form of Naor and Neiman, states that for every fixed doubling bound `D` and every `epsilon in (0,1/2)`, there are `N=N(D)` and `C=C(D,epsilon)` such that every `D`-doubling metric space `(X,d)` has a bi-Lipschitz embedding

\[
(X,d^{1-\varepsilon})\hookrightarrow\mathbb R^N
\]

with distortion at most `C`.

Thus the same uniformly doubling Laakso family that has unbounded Hilbert distortion in its original shortest-path metric becomes uniformly Euclidean-embeddable after the controlled snowflake transformation `d -> d^(1-epsilon)`.

This sharpens another AF-464 boundary: **changing the source metric can be a real escape**, but it must be justified by the downstream problem. A snowflaked representation has not preserved the original quantitative notion of source separation; it has replaced it with another one.

## Prior art and novelty audit

The metric geometry used here is classical. **No novelty is claimed for Laakso graphs, doubling metrics, their Hilbert nonembeddability, superreflexivity test families, or Assouad snowflake embeddings.**

- Sofiya Ostrovska and Mikhail I. Ostrovskii, **“Nonexistence of embeddings with uniformly bounded distortions of Laakso graphs into diamond graphs,”** *Discrete Mathematics* 340(2), 9–17 (2017), DOI `10.1016/j.disc.2016.08.003`, arXiv:`1512.06439`. The paper records the weighted Laakso family as uniformly doubling, places it among classical graph families with poor Hilbert embeddability, and recalls the nonembedding of the infinite Laakso union into Banach spaces with the Radon–Nikodym property.
- Mikhail I. Ostrovskii, **“On metric characterizations of the Radon–Nikodým and related properties of Banach spaces,”** *Journal of Topology and Analysis* 6(3), 441–464 (2014), DOI `10.1142/S1793525314500186`, arXiv:`1302.5968`. This supplies the broader metric-test-space / Radon–Nikodym context including Laakso-type spaces.
- Assaf Naor and Ofer Neiman, **“Assouad's theorem with dimension independent of the snowflaking,”** *Revista Matemática Iberoamericana* 28(4), 1123–1142 (2012), DOI `10.4171/RMI/706`. This gives the uniform finite-dimensional Euclidean embedding of `(X,d^(1-epsilon))` for doubling `X`, with dimension depending only on the doubling constant.
- S. J. Dilworth, Denka Kutzarova, and Svetozar Stankov, **“Metric embeddings of Laakso graphs into Banach spaces,”** *Banach Journal of Mathematical Analysis* 16, article 60 (2022), DOI `10.1007/s43037-022-00212-7`, arXiv:`2203.08229`. They show, in particular, the very different behavior of Laakso graphs in non-superreflexive targets, including uniformly bounded distortion into `L_1`.

The Arithmetic Fidelity contribution is only the audit consequence: AF-464's Hamming-cube witness is not a completeness criterion for stable Hilbert recovery. The classical Laakso family closes that possible inference cleanly and forces a positive source-geometry certificate before “cube-poor” can be interpreted as “faithful.”

## Boundary and falsification audit

- **This is a family-level conditioning obstruction.** Every individual finite Laakso graph embeds into some finite-dimensional Euclidean space with finite distortion. The obstruction is the absence of one distortion bound valid as complexity grows.
- **Uniform doubling is not being claimed to imply Hilbert failure.** Many uniformly doubling spaces embed well into Hilbert space. Laakso graphs show only that uniform doubling is insufficient as a positive certificate.
- **Absence of Hamming cubes remains useful negative information.** It proves that AF-464's specific cube witness cannot fire with uniform constants; it does not classify all possible metric obstructions.
- **The snowflake theorem changes the metric.** It is not recovery of the original shortest-path geometry and cannot be imported into an arithmetic problem unless the downstream discriminator is stable under that metric change.
- **Target category remains load-bearing.** Laakso graphs can have uniformly bounded distortion in important non-superreflexive/type-1 targets even while Hilbert distortion diverges. This is consistent with AF-464's type-1 boundary.
- **No completeness claim is made for the replacement languages.** Markov convexity, thick families of geodesics, superreflexivity test spaces, and related Ribe-program invariants are candidate audit tools for obstructions beyond cubes, not asserted here to classify Arithmetic Fidelity sources.
- **No direct prime or RH theorem follows.** The result constrains what would count as a valid positive source-geometry argument in a later arithmetic specialization.

## Arithmetic-fidelity consequence

Suppose a prime-derived admissible source family is shown to avoid the paired-mixture cubes used in AF-464, or more generally to have bounded doubling complexity. That fact alone does **not** justify a uniformly stable Hilbert-valued representation. The Laakso example shows that a source can be uniformly doubling and cube-poor while every Hilbert representation still develops arbitrarily bad pairwise conditioning.

Accordingly, a prime-facing “thin source” rescue now needs a positive theorem at the metric actually consumed downstream: for example a direct uniform bi-Lipschitz embedding/recovery bound, a structural invariant known to imply such a bound in the declared target category, or a different target/metric for which the required fidelity can be proved. Merely showing that the AF-464 obstruction is absent is no longer enough.

This makes the remaining escape route more precise: **the task is not to delete known bad substructures one at a time, but to identify a positive geometric property that survives the intended compression and quantitatively controls recovery.**