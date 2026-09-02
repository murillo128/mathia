# MI-005 — Scale-doubling identities are exponent-neutral unless retained boundary data add new cancellation

**Evidence level:** supported by the exact Huxley--Watt specializations and generalized-product controls; one fixed-radius analytic-norm finding remains under open adversarial review and is not load-bearing here

## Core intuition

Nonlinear identities that relate scale `N` to `N^2` can look like amplification mechanisms, especially when they generate bilinear or higher-degree Möbius forms. The audited Huxley--Watt family shows a harder boundary: after the exact coarse modes are exposed, the power exponent transported by the identity is neutral. Higher algebraic degree, finite jet expansion, or collapsing to generalized Möbius coefficients does not create a better cancellation exponent by itself.

What can still matter is the **retained signed boundary-face information** before those products are scalarized or collapsed. Any gain must come from an estimate on that new carrier, not from the scale-doubling algebra alone.

## Strongest justified principle

MC-020 specializes Huxley--Watt scale doubling to the harmonic coefficient `H(N)=sum_{n<=N}mu(n)/n` and shows that the apparent nonlinear recursion contains a rank-one coarse mode whose critical control is already RH-equivalent.

MC-021 isolates an exact centered bounded endpoint kernel and a signed quadratic form `B(N)`. This is a genuine new algebraic carrier, but a bound on `B(N)` alone does not close the recursion because lower-scale harmonic and auxiliary terms remain.

MC-022 shows why pointwise kernel resemblance is insufficient. The difference between the harmonic endpoint kernel and Watt's classical sawtooth contains a quadratic form whose correction carries an RH-equivalent coarse quantity. Smallness of the kernel at most points does not imply a cheap arithmetic bilinear form.

MC-023 differentiates the analytic family at the harmonic point and obtains an infinite triangular jet hierarchy rather than finite closure. MC-025 shows that passing to higher-degree product identities remains exponent-neutral: the output power is a convex combination of input exponents, so symmetric inputs reproduce the same exponent. MC-026 gives the corresponding collapse control: replacing the cutoff-face structure by unrestricted generalized Möbius convolutions preserves the same zero boundary and therefore supplies no automatic gain.

## What remains possible

A viable scale-transfer mechanism must retain information discarded by the scalar coarse mode or unrestricted product collapse. Candidate structures include signed cutoff-face incidence, genuinely asymmetric auxiliary factors with independently proved cancellation, or a multiscale coupling whose norm does not project directly onto an RH-equivalent lower-order statistic.

The decisive test is quantitative: after expressing every coarse/Riesz component explicitly, does the remaining signed boundary term admit a source theorem that improves the exponent? If not, changing polynomial degree or taking more derivatives is only a repackaging.

## Status / novelty

Huxley identities, harmonic sums, Euler--Maclaurin/Watt kernels, generalized Möbius convolutions, and exponent interpolation are classical or direct. The synthesis is the structural no-amplification rule for this family: **algebraic nonlinearity is not cancellation amplification unless a new retained boundary variable receives an independent estimate**.

## Falsification criterion

Produce a Huxley--Watt-type identity whose audited coarse terms are controlled at exponent `theta` but whose exact retained boundary term forces an output exponent strictly below `theta` from an independent arithmetic theorem. A formal higher-degree or finite-jet rearrangement without such a source estimate does not falsify the principle.

## Lean-formalizable core

- Exact harmonic endpoint identity.
- Bilinear centered-kernel decomposition.
- Triangular jet hierarchy.
- Convex-combination exponent transport for higher product degree.
- Generalized Möbius product collapse.