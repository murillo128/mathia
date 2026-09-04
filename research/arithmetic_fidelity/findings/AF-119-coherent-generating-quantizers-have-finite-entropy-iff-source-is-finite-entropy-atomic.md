# AF-119 — Coherent generating quantizers have finite entropy iff the source is finite-entropy atomic

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `STRUCTURAL-CLASSIFICATION`, `COHERENT-MULTISCALE-ENTROPY`, `ATOMICITY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-118 identified a coherence gap: separately optimized finite-tolerance codebooks do not automatically assemble into one exact mark. The gap closes sharply once the retained descriptions are required to form one nested hierarchy that eventually generates the full source information.

Let `(X, B, mu)` be a standard Borel probability space. Let

\[
\mathcal P_1 \preceq \mathcal P_2 \preceq \cdots
\tag{1}
\]

be finite or countable measurable partitions, where `P_{n+1}` refines `P_n`, and put

\[
\mathcal F_n:=\sigma(\mathcal P_n).
\tag{2}
\]

Assume the hierarchy is **exactly generating** modulo `mu`:

\[
\sigma\!\left(\bigcup_{n\ge1}\mathcal F_n\right)
=
\mathcal B
\qquad (\bmod\ \mu).
\tag{3}
\]

Write

\[
H_\mu(\mathcal P)
:=
-\sum_{A\in\mathcal P}\mu(A)\log_2\mu(A)
\in[0,\infty].
\tag{4}
\]

Then the following classification holds.

### 1. Every coherent generating hierarchy converges to the same terminal entropy

Define the entropy of the full measured source by

\[
H^\star(\mu)
:=
\sup_{\mathcal Q}
H_\mu(\mathcal Q),
\tag{5}
\]

where the supremum is over finite measurable partitions `Q` of `X`. Then

\[
\boxed{
H_\mu(\mathcal P_n)\uparrow H^\star(\mu).
}
\tag{6}
\]

Thus the limiting entropy budget is not a property of a clever choice of nested codebook. Once the hierarchy genuinely generates the source, its terminal entropy is forced by the measure class itself.

For standard alphabets this is the partition form of the classical general-alphabet quantization theorem: asymptotically generating quantizers recover the full entropy.

### 2. Finite terminal entropy is equivalent to finite-entropy atomicity

Let the positive-mass atoms of `mu` have masses

\[
p_1,p_2,\ldots,
\qquad
\sum_j p_j\le1.
\tag{7}
\]

Then

\[
\boxed{
H^\star(\mu)<\infty
}
\tag{8}
\]

holds if and only if `mu` is purely countably atomic and

\[
\boxed{
H_2(p):=\sum_j p_j\log_2\frac1{p_j}<\infty.
}
\tag{9}
\]

In that case

\[
\boxed{
H^\star(\mu)=H_2(p).
}
\tag{10}
\]

If `mu` has any nonatomic component of positive mass, then

\[
\boxed{
H^\star(\mu)=+\infty.
}
\tag{11}
\]

If `mu` is purely atomic but its atom law has infinite Shannon entropy, the same conclusion holds.

Combining `(6)` with `(8)`--`(11)` gives the exact coherence gate:

\[
\boxed{
\sup_n H_\mu(\mathcal P_n)<\infty
\iff
\mu\text{ is purely atomic with finite atom entropy.}
}
\tag{12}
\]

### 3. The classification is sharp in both directions

If `mu` is purely atomic with finite entropy, enumerate its atoms as `(x_j)` and take

\[
\mathcal P_n
=
\bigl\{
\{x_1\},\ldots,\{x_n\},
X\setminus\{x_1,\ldots,x_n\}
\bigr\}.
\tag{13}
\]

This is a nested generating hierarchy modulo `mu`, and

\[
H_\mu(\mathcal P_n)\uparrow H_2(p)<\infty.
\tag{14}
\]

Conversely, if a nested hierarchy generates a source with a nonatomic component, its entropies must diverge even when **every individual tolerance scale** admits a finite codebook.

### 4. The cumulative innovation budget is the same obstruction

Whenever the displayed entropies are finite, refinement gives the chain rule

\[
H_\mu(\mathcal P_n)
=
H_\mu(\mathcal P_1)
+
\sum_{k=2}^{n}
H_\mu(\mathcal P_k\mid\mathcal P_{k-1}).
\tag{15}
\]

Therefore the total new information inserted by an exact coherent refinement tower is finite exactly in the finite-entropy atomic regime:

\[
\boxed{
\sum_{k\ge2}
H_\mu(\mathcal P_k\mid\mathcal P_{k-1})<\infty
\iff
H^\star(\mu)<\infty,
}
\tag{16}
\]

provided `H_mu(P_1)<infinity`; if an earlier stage already has infinite entropy, the obstruction is immediate.

This separates two notions that AF-116--AF-118 had to keep distinct:

- **pointwise repair complexity:** how many descriptions suffice at one declared tolerance;
- **coherent exact description complexity:** how much information one nested family must accumulate to identify the source in the limit.

The first may be finite at every positive tolerance while the second is infinite.

## Derivation

### Refinement gives monotonicity

If `P_{n+1}` refines `P_n`, then the cell label of `P_n` is a deterministic function of the finer label. Hence

\[
H_\mu(\mathcal P_n)
\le
H_\mu(\mathcal P_{n+1}),
\tag{17}
\]

including the extended-value case.

### A generating hierarchy reaches every finite observable

Fix a finite measurable partition

\[
\mathcal Q=\{Q_1,\ldots,Q_m\}.
\tag{18}
\]

Because the sigma-fields `F_n` increase to `B` modulo `mu`, martingale convergence gives

\[
\mathbb E[1_{Q_j}\mid\mathcal F_n]
\longrightarrow
1_{Q_j}
\quad\text{in }L^1
\qquad (j=1,\ldots,m).
\tag{19}
\]

Equivalently, the conditional uncertainty about the finite label `Q(X)` vanishes:

\[
H_\mu(\mathcal Q\mid\mathcal F_n)\longrightarrow0.
\tag{20}
\]

Therefore

\[
I(\mathcal Q;\mathcal F_n)
=
H_\mu(\mathcal Q)
-
H_\mu(\mathcal Q\mid\mathcal F_n)
\longrightarrow
H_\mu(\mathcal Q).
\tag{21}
\]

Since `F_n=sigma(P_n)`,

\[
I(\mathcal Q;\mathcal F_n)
\le
H_\mu(\mathcal P_n).
\tag{22}
\]

Taking `n -> infinity` and then the supremum over finite `Q` yields

\[
H^\star(\mu)
\le
\sup_n H_\mu(\mathcal P_n).
\tag{23}
\]

For the reverse inequality, the entropy of a countable partition is the supremum of the entropies of its finite coarsenings. Every such coarsening is one of the finite measurable partitions allowed in `(5)`, so

\[
H_\mu(\mathcal P_n)\le H^\star(\mu)
\tag{24}
\]

for every `n`. Equations `(23)` and `(24)` prove `(6)`.

This is also exactly the standard-alphabet quantizer theorem in Robert Gray's general-alphabet information theory: an asymptotically generating sequence of quantizers has entropy converging to the general-alphabet entropy.

### Purely atomic sources reduce to the atom law

Suppose the atoms `(x_j)` carry all mass, with probabilities `(p_j)`. Any finite measurable partition is a deterministic function of the atom index `J`, so data processing gives

\[
H_\mu(\mathcal Q)\le H_2(p).
\tag{25}
\]

The partitions in `(13)` have entropy

\[
-\sum_{j=1}^{n}p_j\log_2p_j
-
r_n\log_2r_n,
\qquad
r_n:=\sum_{j>n}p_j.
\tag{26}
\]

As `n -> infinity`, the first term tends monotonically to `H_2(p)` and `-r_n log_2 r_n -> 0`. Thus

\[
H^\star(\mu)=H_2(p),
\tag{27}
\]

with equality also in the extended sense when the atom entropy diverges.

### Any nonatomic mass forces infinite terminal entropy

Suppose the nonatomic component has mass `alpha>0`. A nonatomic finite measure can be divided into `m` measurable pieces of equal mass `alpha/m`. Put those pieces into separate cells and place the remaining mass `1-alpha` in one additional cell. The resulting finite partition has entropy

\[
h_2(\alpha)+\alpha\log_2m,
\tag{28}
\]

where `h_2` is binary entropy. Letting `m -> infinity` proves

\[
H^\star(\mu)=+\infty.
\tag{29}
\]

This proof also gives a useful adversarial control: a compact interval with an absolutely continuous probability measure has finite covering number at every fixed positive geometric tolerance, but every exactly generating coherent hierarchy has unbounded entropy.

## Geometric sufficient condition for exact generation

The hypothesis `(3)` is measure-theoretic. A common geometric sufficient condition is available when `X` is a separable metric standard Borel space and each `P_n` is countable.

If there is a full-measure set `X_0` such that the hierarchy separates every two distinct points of `X_0`, then the generated countable sigma-field is the full Borel sigma-field on `X_0`. In particular, it is enough that for every `x in X_0`,

\[
\operatorname{diam}\mathcal P_n(x)\longrightarrow0,
\tag{30}
\]

where `P_n(x)` is the cell containing `x`.

Thus a genuinely shrinking nested geometric quantizer is subject to `(12)`: bounded cumulative Shannon information is possible only when the measured source is effectively a finite-entropy countable atomic object.

## Boundary with AF-116--AF-118

AF-116's partial covering number `N_mu(R,epsilon)` optimizes a new finite center set separately at each tolerance. AF-117 shows that a fixed positive error budget can discard sufficiently rare labels, and AF-118 shows that for **one fixed countable mark law** the integrated logarithmic tolerance-rank curve is finite exactly when that mark has finite entropy.

The present result supplies the missing coherence theorem for **nested exact quantizers**. It shows that coherence is not a technical bookkeeping condition: for a nonatomic source it changes the resource class completely. Even if

\[
N_\mu(R,\varepsilon)<\infty
\tag{31}
\]

at every positive tolerance, no nested sequence that asymptotically identifies all source points can have uniformly bounded entropy.

Therefore one must not infer a finite exact side-information budget from scale-by-scale covering bounds alone. A proposed multiscale repair has only three honest options:

1. terminate in a countable atomic discriminator with finite entropy;
2. remain approximate and state the allowed distortion/error rather than claim exact recovery;
3. pay an unbounded refinement budget and analyze its **growth rate** rather than its nonexistent finite terminal entropy.

The third regime is where Rényi information dimension, rate-distortion, metric entropy, and related asymptotic theories become the relevant classical language.

## Falsification and audit tests

The classification depends on exact generation, not merely on refinement. It is falsified as an application if the hierarchy retains only a proper sub-sigma-field: then `(6)` computes the entropy of that retained factor rather than the full source.

Likewise, arbitrary nonnested codebooks do not satisfy the theorem. They remain under the AF-118 coherence warning unless an additional construction turns them into a common generating filtration without increasing the declared resource beyond what the application can pay.

The result also concerns Shannon entropy of the partition labels. A continuous mark carried as a real number is not a finite-entropy discrete code merely because it is one scalar coordinate; its finite-precision description belongs to a distortion/rate or information-dimension problem.

Finally, bounded entropy of a **particular discriminator** can survive on a nonatomic ambient source if the hierarchy only needs to generate the sigma-field of that discriminator. The correct object in `(12)` is always the terminal retained/discriminator factor actually claimed to be reconstructed, not an irrelevant richer ambient space.

## Prior art and novelty assessment

The central convergence theorem is classical, and **no standalone theorem-level novelty is claimed**.

- Robert M. Gray, ***Entropy and Information Theory***, Springer-Verlag (1990), corrected first-edition PDF revised 2023; 2nd ed. Springer (2011), §5.5. Lemma 5.5.1 defines general-alphabet information/entropy through finite quantizers, and Lemma 5.5.5 states that quantizers whose partitions asymptotically generate a standard alphabet recover the full entropy in the limit. This is direct prior art for `(6)`.
- Peter Walters, ***An Introduction to Ergodic Theory***, Graduate Texts in Mathematics 79, Springer (1982), Chapter 4. Role: classical measurable-partition, conditional-entropy, refinement, and generating-partition framework underlying `(17)` and `(15)`.
- Alfréd Rényi, **“On the dimension and entropy of probability distributions,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10, 193–215 (1959), DOI `10.1007/BF02063299`. Role: classical passage from fine quantization entropy to information dimension when exact finite discrete entropy is unavailable.
- Yihong Wu and Sergio Verdú, **“Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression,”** *IEEE Transactions on Information Theory* 56(8), 3721–3748 (2010), DOI `10.1109/TIT.2010.2050803`. Role: modern operational boundary showing that analog/non-discrete sources move naturally to asymptotic almost-lossless compression and information-dimension rates under regularity constraints rather than a finite exact discrete-entropy budget.

The atomic/nonatomic dichotomy in `(8)`--`(11)` is an elementary consequence of the classical entropy-of-a-probability-space definition: finite partitions can split any positive nonatomic mass into arbitrarily many equal-probability cells, while on a purely atomic source every partition is a coarsening of the atom identity.

The Arithmetic Fidelity value is therefore organizational but exact: AF-118's coherence caveat becomes a hard **atomicity gate**. Pointwise cheap repairs across all tolerances do not assemble into a finite-information exact mark unless the terminal discriminator itself is a finite-entropy atomic object. For non-atomic terminal structure, the mathematically meaningful question is no longer whether exact marking has finite entropy, but how its required information diverges with resolution.

## Consequences for the research line

This closes the most immediate gap left by AF-118. Future multiscale constructions should not compare a separately optimized tolerance-cover curve directly with one-shot Shannon entropy. They must first identify the terminal discriminator factor and decide whether it is atomic.

For arithmetic applications this is potentially useful because many desired discriminators are discrete even when their geometric or spectral carriers are continuous. A continuum carrier is not automatically fatal: the relevant question is whether the **prime-specific factor that must survive** is a countable finite-entropy object and whether the proposed compression supplies a coherent filtration that converges to that factor without also retaining the entire continuous ambient state.

Conversely, if a proposed RH route requires exact recovery of a genuinely nonatomic phase, boundary profile, spectral measure, or other continuous provenance object from increasingly fine marks, finite expected side-information cannot be the escape hatch. One must instead prove an approximate/stable theorem at declared resolution or quantify an asymptotic information rate.
