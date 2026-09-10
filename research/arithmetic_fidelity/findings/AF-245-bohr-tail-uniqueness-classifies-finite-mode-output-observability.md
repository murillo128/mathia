# AF-245 — Bohr tail uniqueness classifies finite-mode output observability

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `RH-SUFFICIENT-QUOTIENT`, `OUTPUT-SAMPLING`, `BOHR-OBSERVABILITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-244 used thickness of a retained index set only to guarantee that every nonzero finite unit-circle exponential mode remains detectably nonzero along infinitely many retained indices. The exact topological object controlling that stronger positive-amplitude observability is the tail closure of the sampling set in the Bohr compactification of the integers.

Let `b\mathbb Z` be the Bohr compactification of the discrete group `\mathbb Z`, with canonical dense embedding

\[
\iota:\mathbb Z\longrightarrow b\mathbb Z.
\]

For an unbounded set `S\subset\mathbb N`, define its **tail Bohr limit set**

\[
K_S
:=
\bigcap_{N\ge1}
\overline{\iota(S\cap[N,\infty))}^{\,b\mathbb Z}.
\tag{1}
\]

For every finite unit-circle exponential polynomial

\[
F(n)=\sum_{j=1}^m c_j u_j^n,
\qquad |u_j|=1,
\tag{2}
\]

let `\chi_{u_j}` denote the continuous character of `b\mathbb Z` extending `n\mapsto u_j^n`, and put

\[
\widetilde F(x)=\sum_{j=1}^m c_j\chi_{u_j}(x).
\tag{3}
\]

Then

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}|F(n)|
=
\max_{x\in K_S}|\widetilde F(x)|.
}
\tag{4}
\]

Consequently the following are equivalent:

1. every nonzero finite unit-circle exponential polynomial satisfies
   \[
   \limsup_{\substack{n\to\infty\\n\in S}}|F(n)|>0;
   \tag{5}
   \]
2. no nonzero trigonometric polynomial on `b\mathbb Z` vanishes identically on `K_S`;
3. `K_S` is a uniqueness set for trigonometric polynomials on `b\mathbb Z`.

Call this property **finite-mode tail observability**.

If `S` has finite-mode tail observability and

\[
a_n=q^nF(n)+r_n,
\qquad q>1,
\qquad
\limsup_{n\to\infty}|r_n|^{1/n}<q,
\tag{6}
\]

with nonzero `F` of the form `(2)`, then

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}|a_n|^{1/n}=q.
}
\tag{7}
\]

In particular, every Bohr-dense `S\subset\mathbb N` has finite-mode tail observability, and the Li-coefficient consequence of AF-244 sharpens to

> **For every Bohr-dense set `S\subset\mathbb N`, RH is equivalent to**
> \[
> \boxed{
> \limsup_{\substack{n\to\infty\\n\in S}}|\lambda_n|^{1/n}\le1.
> }
> \tag{8}
> \]

This genuinely enlarges the sampling geometries covered by AF-244: every thick subset of `\mathbb N` is Bohr-dense, but there exist Bohr-dense subsets of `\mathbb N` that have natural density zero and are not thick.

The result remains an **output-sampling theorem**. It does not lower the source depth or cancellation budget required to form a high-index Li coefficient.

## Why it matters

AF-244 showed that output density is not the relevant resource for preserving the off-critical Li root discriminator. Equation `(4)` identifies a more intrinsic retained-state object: the asymptotic location of the surviving indices in the compact phase space seen simultaneously by all characters of `\mathbb Z`.

The distinction is structural. Thickness works because it forces enough recurrence to hit every finite phase pattern, but consecutive blocks are not essential. A highly sparse, non-thick set can still be complete for all finite phase modes if its Bohr tail geometry is sufficiently rich. Conversely, a set with substantial ordinary density can fail immediately if it aliases a periodic phase sector; the even integers, for example, miss the mode `1-(-1)^n` completely.

Thus the retained fraction of coordinates and the retained **phase geometry** are separate compression variables. For the finite dominant modes governing off-RH Li root growth, the second is the load-bearing one.

## Derivation / evidence

### 1. Tail limsup is exactly a maximum on the tail Bohr limit set

For each `N`, write

\[
K_N:=\overline{\iota(S\cap[N,\infty))}^{\,b\mathbb Z}.
\tag{9}
\]

Because `S` is unbounded, each `K_N` is nonempty and compact, and the family is nested:

\[
K_{N+1}\subseteq K_N.
\tag{10}
\]

The universal property of the Bohr compactification extends each character `n\mapsto u^n` continuously to `b\mathbb Z`, so `(3)` is continuous and agrees with `F` on the embedded integers. Hence

\[
\sup_{\substack{n\in S\\n\ge N}}|F(n)|
=
\max_{x\in K_N}|\widetilde F(x)|.
\tag{11}
\]

Let the right-hand side be `M_N`. The sequence `M_N` decreases to a limit `M`. Choose a maximizing point `x_N\in K_N`. Compactness of `K_1` gives a convergent subnet. Its limit lies in every fixed `K_{N_0}`, because eventually the subnet indices satisfy `N\ge N_0`; hence it lies in

\[
K_S=\bigcap_NK_N.
\]

Continuity of `\widetilde F` gives a point of `K_S` at which `|\widetilde F|=M`. The reverse inequality is immediate from `K_S\subseteq K_N`. Therefore

\[
M=\max_{K_S}|\widetilde F|.
\tag{12}
\]

But `M` is exactly the decreasing limit of the tail suprema on the left of `(11)`, which is the restricted limsup. This proves `(4)`.

A finite linear combination of distinct characters that vanishes on all of `b\mathbb Z` also vanishes on the dense copy of `\mathbb Z`; the usual finite Vandermonde argument then forces every coefficient to vanish. Thus `(4)` gives the equivalence `(5)` with trigonometric-polynomial uniqueness on `K_S`.

### 2. Positive-amplitude observability preserves an exponential root discriminator

Assume `(6)` and finite-mode tail observability. By `(5)` there is a constant `C>0` and an unbounded sequence `n_k\in S` such that

\[
|F(n_k)|\ge C.
\tag{13}
\]

Choose `\eta` with

\[
\limsup |r_n|^{1/n}<\eta<q.
\tag{14}
\]

Eventually `|r_n|\le\eta^n`, so along the indices in `(13)`,

\[
|a_{n_k}|
\ge Cq^{n_k}-\eta^{n_k}
\ge \frac C2q^{n_k}
\tag{15}
\]

for all large `k`. This gives the lower root-rate bound `q`. Since every finite exponential polynomial is bounded and the remainder has smaller root rate, the upper bound is also `q`, proving `(7)`.

This condition is deliberately stronger than the logically minimal root-rate requirement. If `F(n)` tends to zero along `S` only subexponentially, `(7)` may still hold even though `(5)` fails. Therefore **Bohr uniqueness exactly classifies positive-amplitude finite-mode observability, not all possible root-rate-preserving sampling sets**.

### 3. Bohr density makes every tail fully observable

Suppose `S\subset\mathbb N` is dense in the Bohr topology. The compact group `b\mathbb Z` is infinite and has no isolated points. Removing finitely many points from a dense subset therefore leaves a dense subset: for any nonempty open `U`, the set `U` cannot be finite, so `U` minus the removed finite set is still a nonempty open set and must meet the original dense set.

Hence every tail `S\cap[N,\infty)` is Bohr-dense and

\[
K_N=b\mathbb Z,
\qquad
K_S=b\mathbb Z.
\tag{16}
\]

No nonzero trigonometric polynomial vanishes identically on `b\mathbb Z`, so every Bohr-dense sampling set has finite-mode tail observability.

### 4. Thickness is a sufficient route to Bohr density, but not a necessary one

Every nonempty Bohr-open subset of `\mathbb Z` is syndetic. For completeness, this follows directly from compactness. A Bohr neighborhood of zero contains the pullback of a sufficiently small open neighborhood `V` of the identity in `b\mathbb Z`. The integer translates of `V` cover the compact group because `\iota(\mathbb Z)` is dense, and compactness reduces this to finitely many translates. Pulling back to `\mathbb Z` gives bounded gaps.

A thick set meets every syndetic set. Indeed, if finitely many translates of `B` cover `\mathbb Z`, thickness supplies a translate of the corresponding finite set inside `S`, and one of those points lies in `B`. Therefore a thick `S` meets every nonempty Bohr-open set and is Bohr-dense. Its tails are again thick, so `(16)` follows as well.

The converse fails strongly. Kahane and Katznelson prove that if positive integers are selected independently with probabilities `\varpi_n` satisfying

\[
n\varpi_n\longrightarrow\infty,
\tag{17}
\]

then the resulting random set is almost surely dense in the Bohr group.

Take, for example,

\[
\varpi_n=\frac{\log(n+1)}{n+1}.
\tag{18}
\]

Then `(17)` holds. On the other hand,

\[
\sum_{n\ge1}\varpi_n\varpi_{n+1}<\infty.
\tag{19}
\]

By the first Borel--Cantelli lemma, almost surely only finitely many adjacent pairs `n,n+1` are both retained. Such a realization cannot contain arbitrarily long intervals, so it is not thick.

It also has natural density zero. If `A_N` is the number of retained integers up to `N`, then

\[
\mathbb E A_N
=
\sum_{n\le N}\varpi_n
=O((\log N)^2).
\tag{20}
\]

Markov's inequality on `N=2^k` gives a summable bound for

\[
\Pr(A_{2^k}\ge\varepsilon 2^k),
\]

so Borel--Cantelli gives `A_{2^k}/2^k\to0` almost surely; monotonicity between dyadic scales then gives `A_N/N\to0`. Thus with probability one the same random set is simultaneously Bohr-dense, density zero, and non-thick.

This proves that Bohr density strictly enlarges the thick sufficient class used in AF-244.

### 5. Periodic aliasing is an immediate necessary diagnostic

Finite-mode observability imposes much more than ordinary density. Suppose that for some modulus `q\ge2`, all sufficiently large elements of `S` lie in a proper residue subset

\[
R\subsetneq\mathbb Z/q\mathbb Z.
\tag{21}
\]

Let `\omega=e^{2\pi i/q}` and define the nonzero polynomial

\[
P(z)=\prod_{r\in R}(z-\omega^r).
\tag{22}
\]

Then

\[
F(n):=P(\omega^n)
\tag{23}
\]

is a finite unit-circle exponential polynomial and vanishes on every sufficiently large `n\in S`. Hence `(5)` fails.

Therefore every finite-mode observable sampling set must visit **every residue class modulo every `q` infinitely often**. This condition is only a necessary periodic test, not a sufficient replacement for the full Bohr uniqueness condition, because irrational character combinations can impose additional phase constraints.

## Li-coefficient consequence

AF-244 already establishes the exact analytic bridge needed here. If RH is false, the nearest poles inside the unit disk of

\[
\frac d{dz}\log\xi\!\left(\frac1{1-z}\right)
=
\sum_{n\ge1}\lambda_n z^{n-1}
\tag{24}
\]

produce

\[
\lambda_n=q^nF(n)+r_n,
\qquad q>1,
\qquad \limsup|r_n|^{1/n}<q,
\tag{25}
\]

with a fixed nonzero finite unit-circle exponential mode `F`. Equation `(7)` therefore gives restricted root rate `q>1` on every finite-mode observable set, in particular every Bohr-dense `S`.

Under RH, the same generating function is holomorphic on the open unit disk, so the unrestricted Li root rate is at most one and every subsequence inherits that upper bound. This proves `(8)`.

The representation map has been audited in both directions relevant to the conclusion: the Bohr compactification changes only how the finite phase mode is represented, while `(4)` exactly identifies the retained tail readout; the separate AF-244 analytic bridge is what converts that finite-mode observability statement into an RH discriminator. Bohr density by itself says nothing about zeta zeros without that bridge.

## Prior-art audit

The Bohr compactification, extension of characters, trigonometric-polynomial/almost-periodic viewpoint, and Bohr-topological density are classical harmonic analysis. No novelty is claimed for those structures or for the compactness argument behind `(4)`.

Kenneth Kunen and Walter Rudin, **“Lacunarity and the Bohr topology,”** *Mathematical Proceedings of the Cambridge Philosophical Society* 126(1), 117--137 (1999), DOI `10.1017/S030500419800317X`, explicitly construct a set in `\mathbb Z` that is `\Lambda(p)` for every finite `p` and is dense in `\mathbb Z^#`. This is strong prior art that Bohr density can coexist with severe classical sparsity.

Jean-Pierre Kahane and Yitzhak Katznelson, **“Entiers aléatoires, ensembles de Sidon, densité dans le groupe de Bohr et ensembles d'analyticité,”** *Comptes Rendus Mathématique* 345(1), 21--24 (2007), DOI `10.1016/j.crma.2007.06.001`, prove the random-selection density statement used in `(17)`. The non-thickness and zero-density consequences for the concrete choice `(18)` are derived above from elementary probability bounds.

The Li/Keiper generating-function and off-RH finite dominant-mode input is not reproved as new mathematics here; it is imported from AF-244, whose source audit includes Keiper, Bombieri--Lagarias, and Voros.

A targeted search for Li/Keiper criteria formulated on Bohr-dense subsequences, Bohr uniqueness sets of Li output indices, and closely equivalent sparse root-rate formulations did not locate the exact synthesis `(8)`. This is not an exhaustive novelty proof. The present contribution should therefore be read narrowly: **classical Bohr uniqueness machinery gives an exact state space for the positive-amplitude observability question left open by AF-244, and this yields a new-to-this-corpus sparse Li sampling criterion covering non-thick zero-density sets.**

## Boundaries / caveats

**Bohr uniqueness is exact for `(5)`, not necessary for every root-rate decoder.** A sampling set could approach the zero set of a mode with amplitude tending to zero subexponentially and still preserve the `n`th-root rate. Quantitative root-rate fidelity beyond positive-amplitude observability requires a rate-sensitive refinement of the tail Bohr geometry.

**The criterion is universal over fixed finite modes.** It does not cover infinitely many co-dominant frequencies, continuous spectral mass, or a mode family whose dimension grows with `n`.

**Output compression remains distinct from source compression.** Even a zero-density Bohr-dense set can require arbitrarily large Li indices. AF-238--AF-243 show that forming those coefficients from truncated source data can still destroy or fabricate the relevant cancellation. AF-245 does not evade that obstruction.

**Bohr density is sufficient, not the minimal topological condition.** The exact positive-amplitude condition is trigonometric-polynomial uniqueness of `K_S`; a proper closed subset of `b\mathbb Z` may still be a uniqueness set. Replacing Bohr density by the precise geometry of such proper uniqueness sets is a legitimate refinement, but it is not needed for `(8)`.

**Periodic completeness is only a first audit.** Visiting every residue class modulo every integer rules out finite-order-character aliases but does not control irrational characters or their finite combinations.

## Consequence

AF-244's local-window condition can now be replaced by a clean hierarchy:

\[
\text{thick sampling}
\Longrightarrow
\text{Bohr-dense sampling}
\Longrightarrow
\text{finite-mode tail observability}
\Longrightarrow
\text{Li off-RH root-rate preservation}.
\tag{26}
\]

The first implication is strict, and the second need not be an equivalence because proper trigonometric-polynomial uniqueness sets may exist. The important conceptual change is that **sampling fidelity is governed by the geometry seen by the discriminator's phase family, not by ordinary cardinal density or adjacency structure**.

The remaining output-side problem is quantitative rather than merely topological: characterize sampling sets for which every relevant finite mode avoids its zero set at a subexponential rate, which would identify the exact boundary for `n`th-root fidelity rather than the stronger positive-amplitude condition proved here. Separately, the harder RH-facing bottleneck remains source access: finding a compression that forms enough globally cancelled Li information without paying essentially linear source depth.