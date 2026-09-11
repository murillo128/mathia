# AF-279 — Discrete vertical sampling is phase-pushforward fidelity

**Status:** `CLASSICAL-STRUCTURE`, `LITERATURE+DERIVED`, `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `DISCRETE-SAMPLING`, `ALIASING`, `STABILITY-OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-278 recovers every coefficient of an absolutely convergent Dirichlet series from the full continuous vertical orbit on one fixed line. Replacing that orbit by a regular vertical lattice does not merely reduce the number of samples: it changes the exact quotient of the source by folding every frequency modulo the sampling period.

Let

\[
F(s)=\sum_{n\ge1}a_ne^{-\lambda_ns},
\qquad
0\le \lambda_1<\lambda_2<\cdots,\quad \lambda_n\to\infty,
\]

and fix `c` in the absolute-convergence half-plane, so

\[
B_c:=\sum_{n\ge1}|a_n|e^{-c\lambda_n}<\infty.
\]

Fix a sampling step `h>0` and retain the bilateral lattice

\[
\mathcal S_h(F)=\bigl(F(c+ikh)\bigr)_{k\in\mathbb Z}.
\]

Write

\[
b_n:=a_ne^{-c\lambda_n},
\qquad
z_n:=e^{-ih\lambda_n}\in\mathbb T,
\]

and define the finite complex measure

\[
\mu_F:=\sum_{n\ge1}b_n\delta_{z_n}
\]

on the unit circle. Then

\[
F(c+ikh)=\int_{\mathbb T}z^k\,d\mu_F(z).
\]

Therefore the complete lattice channel has the exact classification

\[
\boxed{
\mathcal S_h(F)=\mathcal S_h(G)
\iff
\mu_F=\mu_G.
}
\]

Equivalently, if `F` and `G` use the same declared frequency system, equality of all lattice samples holds exactly when, for every phase `z\in\mathbb T`,

\[
\boxed{
\sum_{n:z_n=z}a_ne^{-c\lambda_n}
=
\sum_{n:z_n=z}a'_ne^{-c\lambda_n}.
}
\]

Thus regular vertical sampling retains the coefficient law only after **pushforward through the wrapped phase map**

\[
\lambda\longmapsto e^{-ih\lambda}.
\]

Three consequences follow.

1. **Exact coefficient fidelity is equivalent to absence of phase collisions.** If `n\mapsto z_n` is injective, the full bilateral lattice determines every `a_n` exactly. If `z_n=z_m` for some `n\ne m`, the two weighted coefficient coordinates are collapsed into one exact fiber and opposite perturbations inside that fiber are invisible to every sample.

2. **For ordinary Dirichlet series the alias condition is arithmetic.** With `\lambda_n=\log n`, put
   \[
   q_h:=e^{2\pi/h}.
   \]
   Then `n\ne m` alias exactly when
   \[
   \frac nm=q_h^r
   \]
   for some nonzero integer `r`. Hence the lattice is coefficient-faithful on the ordinary Dirichlet frequency system iff
   \[
   \boxed{q_h^r\notin\mathbb Q_{>0}\quad\text{for every }r\in\mathbb Z\setminus\{0\}.}
   \]
   The exceptional sampling steps are countable. For example, `h=2\pi/\log 2` makes `n` and `2n` exact aliases for every `n`.

3. **Exact injectivity does not give finite-window stability.** For every ordinary Dirichlet index `N`, every `h>0`, and every finite sample window `|k|\le K`, there are arbitrarily large indices `m` whose wrapped phase is arbitrarily close to that of `N`. Consequently, within a fixed weighted `\ell^1` source budget one can move an order-one weighted coefficient mass from `N` to a remote `m` while making all samples in the fixed window arbitrarily close. Even for a nonresonant `h` with exact infinite-lattice fidelity, no modulus based on a fixed finite lattice window can uniformly recover coefficient `N` over the unrestricted absolutely convergent source class.

The distinction from AF-278 is sharp. Continuous vertical time keeps the real frequencies `\lambda_n` unwrapped and isolates a fixed `\lambda_N` by long-time orthogonality. Regular discrete time replaces them by points of the compact circle. It can remain exactly injective for generic cadence, but remote frequencies necessarily accumulate near every retained phase, so finite-window conditioning is a separate obstruction.

## Exact quotient by Fourier--Stieltjes uniqueness

Absolute convergence gives

\[
\sum_n|b_n|<\infty,
\]

so `\mu_F` is a finite complex Borel measure. For every integer `k`,

\[
\begin{aligned}
F(c+ikh)
&=\sum_{n\ge1}a_ne^{-c\lambda_n}e^{-ikh\lambda_n}\\
&=\sum_{n\ge1}b_nz_n^k\\
&=\int_{\mathbb T}z^k\,d\mu_F(z).
\end{aligned}
\]

The characters `z\mapsto z^k`, `k\in\mathbb Z`, form the Fourier characters of the compact abelian group `\mathbb T`. A finite complex measure is uniquely determined by all of its Fourier--Stieltjes coefficients. Hence equality of the complete bilateral sample sequences is equivalent to equality of the pushforward measures.

For a fixed declared frequency sequence, the mass of `\mu_F` at `z` is exactly

\[
\mu_F(\{z\})
=
\sum_{n:z_n=z}b_n,
\]

where the fiber sum converges absolutely. This proves the phase-fiber formula in the claim.

If every fiber is a singleton, `b_n` is recovered as the atom mass at `z_n`, and then

\[
a_n=e^{c\lambda_n}b_n.
\]

If instead `z_n=z_m`, choose any `\delta\ne0` and alter only

\[
b_n\mapsto b_n+\delta,
\qquad
b_m\mapsto b_m-\delta.
\]

The measure `\mu_F`, hence every lattice sample, is unchanged. The failure is therefore exact aliasing, not numerical error or insufficiently long observation.

The bilateral qualification matters for general complex coefficients. Nonnegative Fourier indices alone are analytic moments and do not, for arbitrary complex measures on `\mathbb T`, have the same elementary uniqueness property. The theorem here deliberately prices the complete two-sided lattice rather than silently importing additional positivity or Hardy-space assumptions.

## Ordinary Dirichlet frequencies: the resonance set is countable

For `\lambda_n=\log n`, a collision means

\[
e^{-ih\log n}=e^{-ih\log m}.
\]

This is equivalent to

\[
h\log(n/m)=2\pi r
\]

for some `r\in\mathbb Z\setminus\{0\}`. Exponentiating gives

\[
\frac nm=e^{2\pi r/h}=q_h^r.
\]

Thus a collision exists iff a nontrivial integral power of `q_h` is a positive rational. Equivalently the exceptional spacings are contained exactly in the countable set

\[
\left\{
\frac{2\pi r}{\log(n/m)}:
 n,m\in\mathbb N,\ n\ne m,\ r\in\mathbb Z\setminus\{0\},\
\frac{r}{\log(n/m)}>0
\right\}.
\]

For every `h` outside this set, the wrapped phases are pairwise distinct and the complete bilateral lattice recovers the entire ordinary Dirichlet coefficient sequence.

At the resonant spacing

\[
h=\frac{2\pi}{\log 2},
\]

one has

\[
e^{-ih\log(2n)}
=e^{-ih\log n}e^{-i2\pi}
=e^{-ih\log n}
\]

for every `n`. The quotient therefore folds each `n` together with its dyadic multiples. More generally, whenever `q_h^r=u/v\in\mathbb Q_{>0}`, frequencies whose indices differ by the rational scale `u/v` collide whenever both indices are integral.

This is the direct analytic-value analogue of AF-029's lattice-observable quotient: the retained family is infinite, yet its exact information content is controlled by whether its generated phase representation separates source coordinates.

## Remote phase recurrence destroys fixed-window recovery

Exact nonaliasing is only a zero-error statement for the **entire** lattice. Its finite-window inverse is not uniformly stable on the unrestricted absolutely convergent source class.

Fix an ordinary Dirichlet index `N` and let

\[
q=e^{2\pi/h}>1.
\]

For each large integer `j`, choose an integer `m_j` nearest to `Nq^j`. Then

\[
\frac{m_j}{Nq^j}\to1,
\]

and therefore

\[
\begin{aligned}
h\log(m_j/N)
&=h\log q^j+h\log\!\left(\frac{m_j}{Nq^j}\right)\\
&=2\pi j+o(1).
\end{aligned}
\]

It follows that

\[
z_{m_j}=e^{-ih\log m_j}\longrightarrow e^{-ih\log N}=z_N.
\]

This recurrence is elementary and holds for every `h>0`; no equidistribution theorem is needed.

Now compare two finite-support weighted coefficient laws whose difference is

\[
\Delta b_N=1,
\qquad
\Delta b_{m_j}=-1.
\]

Their difference in the sampled channel is

\[
\Delta S_j(k)=z_N^k-z_{m_j}^k.
\]

For every fixed `K`,

\[
\max_{|k|\le K}|\Delta S_j(k)|\to0,
\]

while the target weighted coefficient displacement at `N` remains exactly one and the weighted source `\ell^1` norm of the perturbation remains exactly two.

Equivalently, in the original coefficients one may take

\[
\Delta a_N=e^{c\log N}=N^c,
\qquad
\Delta a_{m_j}=-m_j^c,
\]

so that the perturbation still has fixed weighted absolute-convergence norm

\[
\sum_n|\Delta a_n|n^{-c}=2.
\]

Scaling this pair gives any desired fixed displacement at `a_N` while preserving a bounded weighted source budget.

Hence for every finite `K` and every `\varepsilon>0` there exist two absolutely convergent finite-support Dirichlet series with a fixed nonzero coefficient difference at `N` but

\[
\max_{|k|\le K}
|F(c+ikh)-G(c+ikh)|<\varepsilon.
\]

So no finite-window inverse modulus exists on this source class. In topological language, when the sample sequence is given the product topology of coordinatewise observation, extraction of an individual atom mass is discontinuous even when the full lattice map is injective.

This does **not** imply instability in every norm on the full infinite sample sequence. For example, an `\ell^\infty` discrepancy over all `k\in\mathbb Z` can see phase differences that every fixed window misses. The obstruction is specifically that increasing source breadth can hide behind arbitrarily remote sample indices; exact infinite-lattice fidelity cannot be priced as finite observation merely because the retained set is countable.

## Prime-coordinate consequence and its limit

For a degree-one Euler family

\[
Z_\alpha(s)=\prod_p(1-\alpha_pp^{-s})^{-1}
=\sum_{n\ge1}f_\alpha(n)n^{-s},
\]

one has `f_\alpha(p)=\alpha_p`. Therefore, whenever the chosen spacing `h` is nonresonant on the ordinary Dirichlet frequency system, the complete bilateral lattice determines the whole Dirichlet coefficient law and hence every local prime parameter `\alpha_p`.

This is a positive exact-fidelity statement, but it reconstructs essentially the full source and still uses infinitely many observations. The fixed-window obstruction shows that countability alone is not a meaningful compression budget: to recover ever broader prime coordinates from regular vertical samples, one must permit the observation horizon to grow and confront increasingly close wrapped phases.

Conversely, an exact phase collision proves nonfaithfulness on the unrestricted Dirichlet coefficient class. It does **not** automatically produce two degree-one Euler systems with identical lattice values, because Euler multiplicativity couples many coefficients. Any stronger collision claim inside a narrower Euler category requires a separate construction respecting that category.

## Prior art and novelty assessment

The harmonic-analysis ingredients are classical and no broad sampling novelty is claimed.

- Walter Rudin, ***Fourier Analysis on Groups***, Wiley-Interscience (1962; Wiley Classics editions later), is a standard source for Fourier--Stieltjes transforms of finite measures on locally compact abelian groups and their uniqueness. The equivalence between the complete integer moment sequence of `\mu_F` and the measure itself is an instance of that classical uniqueness theorem.
- The restriction of an exponential mode `e^{-it\lambda}` to the lattice `t=kh` replaces `\lambda` by its class modulo `2\pi/h`; this is the elementary aliasing mechanism of uniform sampling. In the almost-periodic/nonharmonic setting, Harmonic Balance literature explicitly distinguishes arbitrary-frequency almost-periodic Fourier analysis from uniform discrete transforms and uses oversampling/nonuniform sampling to mitigate aliasing and conditioning; see T. Breiten and M. Hanke, **“Minimizing Aliasing in Multiple Frequency Harmonic Balance Computations,”** *Journal of Scientific Computing* 92 (2022), article 18, DOI `10.1007/s10915-022-01776-0`.
- Markus Petz, Gerlind Plonka, and Nadiia Derevianko, **“Exact reconstruction of sparse non-harmonic signals from their Fourier coefficients,”** *Sampling Theory, Signal Processing, and Data Analysis* 19 (2021), article 7, DOI `10.1007/s43670-021-00007-1`, is neighboring finite-mode reconstruction prior art. The present result is not a new Prony-type algorithm; it treats an absolutely summable infinite coefficient law as a finite complex measure after phase wrapping.
- AF-029 already gives the line's finite-measure analogue for a lattice of cosine-modulated Weil tests: the complete lattice factors through an explicit phase/cosine quotient, and fidelity is exactly support-level separation by that quotient. AF-278 gives the contrasting continuous-time Dirichlet channel before phase wrapping.

A targeted search for the exact ordinary-Dirichlet statement “bilateral regular vertical samples classify coefficients by the phase pushforward `n\mapsto n^{-ih}` together with the rational-power resonance criterion and the fixed-window remote-index instability” did not locate that synthesis as a named theorem. This is not an exhaustive novelty proof. The contribution should therefore be read narrowly as a category-specific Arithmetic Fidelity classification assembled from classical Fourier uniqueness and aliasing.

## Boundaries and failure modes

- Absolute convergence on `Re(s)=c` is assumed so that `\mu_F` has finite total variation and all rearrangements are immediate.
- Exact recovery uses every bilateral sample `k\in\mathbb Z`. A one-sided lattice requires a separate analytic-moment audit for the declared source category.
- The frequency system `\{\lambda_n\}` is known. The theorem recovers coefficient mass on declared frequencies; it does not jointly estimate unknown frequencies.
- Nonresonance gives exact injectivity but no finite-window modulus on the unrestricted weighted `\ell^1` source ball. Additional sparsity, separation, coefficient decay, positivity, multiplicativity, or another compactness constraint can change that stability problem and must be priced explicitly.
- The remote-phase recurrence uses ordinary frequencies `\log n`. For a general frequency sequence the exact quotient theorem still holds, but phase accumulation and its rate depend on the wrapped frequency geometry.
- An exact collision in the general Dirichlet category does not by itself yield a collision in a narrower Euler, positive, or arithmetic-control class.
- No analytic continuation, zero-location theorem, functional equation, critical-strip estimate, or RH consequence follows from the sampling classification.

## Decisive audit test

When a proposed RH carrier replaces a continuous or nonuniform analytic observation by regular samples, compute the induced compact phase map before interpreting the samples:

\[
\lambda\mapsto e^{-ih\lambda}.
\]

Then ask, in order:

1. What are its exact fibers on the declared source category?
2. Does the retained two-sided sample family determine only the phase pushforward, or does extra structure split those fibers?
3. Even if the phase map is injective, are relevant source coordinates isolated in the wrapped spectrum strongly enough to give a finite-window inverse modulus?
4. What resource must grow to resolve remote near-aliases: window length, nonuniform sampling, multiple cadences, precision, source constraints, or an independent arithmetic rigidity theorem?

An infinite list of regular samples is not automatically equivalent to the continuous orbit it came from. Sampling can introduce a new quotient before any later spectral, positive, or asymptotic compression is applied.

## Consequence for the research line

AF-275--AF-279 now separate four acquisition geometries for the same broad prime-breadth problem. Finite values and finite jets leave exact far-prime fibers. Escaping real-depth samples recover the source with severe depth-dependent precision. Continuous vertical Bohr means recover it at fixed real part by paying unbounded phase-time breadth. A regular vertical lattice introduces an additional wrapped-phase quotient: generic cadence remains exactly faithful on ordinary Dirichlet coefficients, resonant cadence creates exact arithmetic aliases, and even nonresonant cadence has no fixed-window recovery modulus because remote logarithmic frequencies recur arbitrarily close after wrapping.

The resulting fidelity principle is sharper than “infinite observations recover the source.” **Acquisition geometry itself is a compression.** Continuous time, discrete time, cadence, sidedness, horizon, and source-category constraints determine different quotient fibers and different stability costs. Any RH-facing claim that retains sampled analytic data must price those choices before attributing arithmetic meaning to the downstream representation.