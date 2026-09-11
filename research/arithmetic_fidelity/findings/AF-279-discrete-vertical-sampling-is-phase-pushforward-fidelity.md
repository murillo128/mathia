# AF-279 — Discrete vertical sampling is phase-pushforward fidelity

**Status:** `CLASSICAL-STRUCTURE`, `LITERATURE+DERIVED`, `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `DISCRETE-SAMPLING`, `ALIASING`, `STABILITY-OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-278 recovers every coefficient of an absolutely convergent Dirichlet series from the full continuous vertical orbit on one fixed line. Replacing that orbit by a regular vertical lattice changes the exact quotient: it folds every source frequency modulo the sampling period.

Let

\[
F(s)=\sum_{n\ge1}a_ne^{-\lambda_ns},
\qquad
0\le \lambda_1<\lambda_2<\cdots,\quad \lambda_n\to\infty,
\]

and fix `c` such that

\[
B_c:=\sum_{n\ge1}|a_n|e^{-c\lambda_n}<\infty.
\]

For `h>0`, retain the bilateral lattice

\[
\mathcal S_h(F)=\bigl(F(c+ikh)\bigr)_{k\in\mathbb Z}.
\]

Write

\[
b_n=a_ne^{-c\lambda_n},
\qquad
z_n=e^{-ih\lambda_n}\in\mathbb T,
\qquad
\mu_F=\sum_{n\ge1}b_n\delta_{z_n}.
\]

Then

\[
F(c+ikh)=\int_{\mathbb T}z^k\,d\mu_F(z),
\]

so Fourier--Stieltjes uniqueness gives

\[
\boxed{
\mathcal S_h(F)=\mathcal S_h(G)
\iff
\mu_F=\mu_G.
}
\]

Thus the complete regular lattice remembers the coefficient law only after pushforward through

\[
\boxed{\lambda\mapsto e^{-ih\lambda}.}
\]

For a common declared frequency system this is equivalent to equality, for every `z\in\mathbb T`, of the absolutely convergent fiber sums

\[
\sum_{n:z_n=z}a_ne^{-c\lambda_n}.
\]

Hence exact coefficient fidelity holds iff the phase map `n\mapsto z_n` is injective. If two frequencies collide, opposite weighted coefficient perturbations inside that fiber are invisible to every sample.

For ordinary Dirichlet series, `\lambda_n=\log n`. Put

\[
q_h=e^{2\pi/h}.
\]

Then `n\ne m` collide iff

\[
h\log(n/m)=2\pi r
\]

for some nonzero integer `r`, equivalently

\[
\frac nm=q_h^r.
\]

Therefore the complete bilateral lattice is coefficient-faithful exactly when

\[
\boxed{
q_h^r\notin\mathbb Q_{>0}
\quad\text{for every }r\in\mathbb Z\setminus\{0\}.
}
\]

The bad spacings form a countable set. For example,

\[
h=\frac{2\pi}{\log2}
\]

makes `n` and `2n` exact aliases for every `n`.

Even when `h` is nonresonant and the infinite lattice is exactly injective, **no fixed finite lattice window has a uniform inverse modulus for an individual coefficient over the unrestricted weighted `\ell^1` source class**. For every target index `N`, every finite `K`, and every `\varepsilon>0`, there are two finite-support ordinary Dirichlet series whose weighted coefficient at `N` differs by an order-one amount, whose weighted `\ell^1` distance is fixed, but whose samples satisfy

\[
\max_{|k|\le K}|F(c+ikh)-G(c+ikh)|<\varepsilon.
\]

So discrete sampling introduces two distinct fidelity questions: exact aliasing of the full infinite channel and conditioning of finite acquisition.

## Exact phase quotient

Absolute convergence implies `\sum_n|b_n|<\infty`, so `\mu_F` is a finite complex Borel measure. For every `k\in\mathbb Z`,

\[
\begin{aligned}
F(c+ikh)
&=\sum_{n\ge1}a_ne^{-c\lambda_n}e^{-ikh\lambda_n}\\
&=\sum_{n\ge1}b_nz_n^k\\
&=\int_{\mathbb T}z^k\,d\mu_F(z).
\end{aligned}
\]

The characters `z\mapsto z^k`, `k\in\mathbb Z`, determine a finite complex measure on the compact abelian group `\mathbb T`. Therefore equality of all bilateral samples is exactly equality of the pushed-forward measures.

If `z_n` is unique, its atom mass is `b_n`, hence `a_n=e^{c\lambda_n}b_n`. If `z_n=z_m`, replace

\[
b_n\mapsto b_n+\delta,
\qquad
b_m\mapsto b_m-\delta.
\]

The pushed-forward measure and every lattice sample remain unchanged. This identifies the full kernel rather than merely producing one counterexample.

The bilateral qualification is deliberate. For arbitrary complex measures, nonnegative Fourier indices alone are analytic moments and do not carry the same elementary measure-uniqueness guarantee. A one-sided sample channel therefore needs its own source-category audit.

## Ordinary Dirichlet resonance is an arithmetic sampling condition

With `\lambda_n=\log n`, collision is equivalent to

\[
e^{-ih\log n}=e^{-ih\log m}
\iff
h\log(n/m)\in2\pi\mathbb Z.
\]

Thus the exceptional spacings are exactly the positive members of the countable set

\[
\left\{
\frac{2\pi r}{\log(n/m)}:
 n,m\in\mathbb N,\ n\ne m,\ r\in\mathbb Z\setminus\{0\}
\right\}.
\]

Outside that set, every wrapped phase is distinct and the full coefficient sequence is exactly recoverable from the bilateral lattice. At a resonant spacing, the loss is an arithmetic quotient of coefficient coordinates before any later spectral, positive, or asymptotic operation is applied.

This is the analytic-value analogue of AF-029: an infinite lattice family can be either faithful or exactly aliased depending on whether the induced phase representation separates the source.

## Remote phase recurrence destroys fixed-window recovery

Fix an ordinary Dirichlet index `N` and set

\[
q=e^{2\pi/h}>1.
\]

For large integers `j`, choose `m_j` nearest to `Nq^j`. Then

\[
\frac{m_j}{Nq^j}\to1,
\]

so

\[
h\log(m_j/N)=2\pi j+o(1).
\]

Consequently

\[
e^{-ih\log m_j}\to e^{-ih\log N}.
\]

No equidistribution theorem is needed: every target phase is approached by remote ordinary-Dirichlet frequencies simply by approximating the geometric progression `Nq^j` with integers.

Now take weighted coefficient perturbations

\[
\Delta b_N=1,
\qquad
\Delta b_{m_j}=-1.
\]

Their weighted `\ell^1` norm is exactly two, while the sample difference is

\[
\Delta S_j(k)=z_N^k-z_{m_j}^k.
\]

For each fixed `K`,

\[
\max_{|k|\le K}|\Delta S_j(k)|\to0.
\]

In original coefficients the same perturbation is

\[
\Delta a_N=N^c,
\qquad
\Delta a_{m_j}=-m_j^c,
\]

and still has weighted absolute-convergence norm

\[
\sum_n|\Delta a_n|n^{-c}=2.
\]

Scaling gives any desired fixed target displacement. Hence finite windows cannot uniformly recover a fixed coefficient on this source ball, even when the complete infinite sample map is injective.

This is a product-topology / finite-acquisition obstruction, not a claim about every norm on the full infinite sequence. An `\ell^\infty` norm over all `k\in\mathbb Z`, for example, may detect differences invisible on every preassigned finite window.

## Prime-coordinate consequence and limit

For a degree-one Euler family

\[
Z_\alpha(s)=\prod_p(1-\alpha_pp^{-s})^{-1}
=\sum_{n\ge1}f_\alpha(n)n^{-s},
\]

one has `f_\alpha(p)=\alpha_p`. Therefore a nonresonant complete bilateral lattice determines the full Dirichlet coefficient law and hence every local prime parameter.

This is exact prime-coordinate fidelity, but it reconstructs essentially the whole source and uses infinitely many observations. The finite-window obstruction shows that countability is not a sufficient compression budget: broader source coordinates require an ever-growing observation horizon because wrapped logarithmic frequencies accumulate.

Conversely, a phase collision proves nonfaithfulness on the unrestricted Dirichlet coefficient class. It does **not** automatically construct two degree-one Euler systems with identical lattice values, because multiplicativity couples many coefficients. Any Euler-category collision requires a separate construction.

## Prior art and novelty assessment

The ingredients are classical; no broad sampling theorem is claimed as new.

Walter Rudin, ***Fourier Analysis on Groups***, Wiley-Interscience (1962; later Wiley Classics editions), is a standard source for Fourier--Stieltjes transforms of finite measures on locally compact abelian groups and their uniqueness. The measure classification above is a direct instance of that theorem.

The folding `\lambda\mapsto e^{-ih\lambda}` is the elementary aliasing mechanism of uniform sampling. In the almost-periodic/nonharmonic setting, Daniel Lindblad, Christian Frey, Laura Junge, Graham Ashcroft, and Niklas Andersson, **“Minimizing Aliasing in Multiple Frequency Harmonic Balance Computations,”** *Journal of Scientific Computing* 91 (2022), article 65, DOI `10.1007/s10915-022-01776-0`, explicitly study aliasing and conditioning for discrete sampling of arbitrary frequency sets and contrast uniform sampling with condition-aware sampling strategies.

Markus Petz, Gerlind Plonka, and Nadiia Derevianko, **“Exact reconstruction of sparse non-harmonic signals from their Fourier coefficients,”** *Sampling Theory, Signal Processing, and Data Analysis* 19 (2021), article 7, DOI `10.1007/s43670-021-00007-1`, is neighboring finite-mode reconstruction prior art. AF-279 is not a Prony-type reconstruction algorithm; it treats an absolutely summable infinite coefficient law as a finite complex measure after phase wrapping.

AF-029 already classifies a lattice-induced cosine quotient for compactly supported measure observables, while AF-278 gives the contrasting continuous-time Dirichlet channel before wrapping. A targeted search did not locate the exact synthesis of the ordinary-Dirichlet rational-power resonance criterion with the remote-index finite-window instability as a named theorem. This is not an exhaustive novelty proof; the contribution is the Arithmetic Fidelity classification and resource accounting built from classical harmonic analysis.

## Boundaries and failure modes

- Absolute convergence on `Re(s)=c` is assumed so the pushed-forward measure has finite total variation.
- Exact recovery uses every bilateral sample `k\in\mathbb Z`; one-sided sampling needs a separate audit.
- The frequency system is known. The theorem recovers amplitudes on declared frequencies, not unknown frequencies jointly with amplitudes.
- Nonresonance gives exact injectivity but not a finite-window inverse modulus on the unrestricted weighted `\ell^1` source ball. Sparsity, separation, positivity, multiplicativity, coefficient decay, or other compactness assumptions can change that problem.
- The remote recurrence argument is specific to ordinary frequencies `\log n`; for a general frequency sequence, the exact quotient still holds but wrapped accumulation must be analyzed separately.
- General Dirichlet collisions do not automatically lie in narrower Euler or arithmetic-control categories.
- No analytic continuation, critical-strip estimate, zero-location theorem, functional equation, or RH implication follows from the sampling classification.

## Decisive audit test

When an RH carrier replaces continuous analytic observation by regular samples, first compute the induced phase map

\[
\lambda\mapsto e^{-ih\lambda}.
\]

Then separate four questions: its exact fibers on the declared source category; whether extra structure splits those fibers; whether target coordinates are sufficiently isolated in wrapped phase to admit a finite-window inverse modulus; and which resource must grow to resolve near-aliases—window length, cadence diversity, nonuniform sampling, precision, source constraints, or an independent arithmetic rigidity theorem.

An infinite list of regular samples is not automatically equivalent to the continuous orbit it came from. **Acquisition geometry itself is a compression.**

## Consequence for the research line

AF-275--AF-279 now separate four acquisition geometries for the same prime-breadth problem. Finite values and finite jets leave exact far-prime fibers. Escaping real-depth samples recover the source while paying depth-dependent precision. Continuous vertical Bohr means recover it at fixed real part by paying unbounded phase-time breadth. Regular vertical sampling adds a wrapped-phase quotient: generic cadence remains exactly faithful on ordinary Dirichlet coefficients, resonant cadence creates exact arithmetic aliases, and even nonresonant cadence has no fixed-window recovery modulus because remote logarithmic frequencies recur arbitrarily close after wrapping.

The useful principle is therefore stronger than “infinite observations recover the source”: continuous versus discrete acquisition, cadence, sidedness, horizon, and source category determine different quotient fibers and different stability costs, and those costs must be priced before assigning arithmetic meaning to a downstream representation.