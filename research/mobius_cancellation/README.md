# Möbius Cancellation

## Research mandate

### Primary object

The line studies cancellation in the Möbius function

\[
\mu(n)\in\{-1,0,1\},
\qquad
M(x)=\sum_{n\le x}\mu(n),
\]

and in closely related multiplicative-function observables that can expose why local or averaged randomness does, or does not, propagate to global square-root-scale cancellation. The intrinsic arithmetic structure includes multiplicativity, square-free support, sign, correlations, short-interval sums, Dirichlet-polynomial representations, and the reciprocal-zeta relation in domains where it is legitimately available.

The line treats the RH-equivalent scale

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\]

as a target boundary to explain, not as an assumption or as a license to import zero-free continuation implicitly.

### Objective

Determine whether known or newly derived structure in Möbius cancellation can constrain the global growth of `M(x)` beyond currently available unconditional bounds, or isolate a precise obstruction that explains why strong local, averaged, correlation, or non-pretentious cancellation fails to reach the RH scale.

A successful mechanism should connect independently controlled arithmetic information to a genuinely stronger global cancellation statement, or prove a reusable no-go showing that a broad class of local/statistical information is insufficient. Merely restating an RH-equivalent Möbius criterion, rewriting `1/zeta(s)`, or describing Möbius as random does not count as progress.

### Priority questions

Study in particular:

- the exact local-to-global gap between cancellation in almost all short intervals and bounds for the full summatory function `M(x)`;
- Halász-type mean-value theory and pretentious distance as structural explanations of when multiplicative functions can sustain large partial sums;
- whether quantitative non-pretentiousness of Möbius at multiple scales can be converted into stronger deterministic control of `M(x)`;
- which correlation bounds, Chowla-type information, logarithmic averages, higher-order correlations, or Fourier-uniformity statements would actually imply improved global exponents, and which provably do not;
- decompositions of Möbius sums through Dirichlet polynomials, identities extracting prime factors, bilinear forms, Type I/II structures, or related analytic mechanisms, with explicit accounting of the step that loses the square-root scale;
- extremal or near-extremal sign/correlation patterns compatible with currently known local cancellation results but still capable of producing anomalously large `M(x)`;
- whether an off-critical zero would force a detectable and quantitatively rigid signature in Möbius partial sums, correlations, scale interactions, or multiplicative pretentiousness beyond the tautological explicit-formula implication;
- comparisons with Liouville and other multiplicative functions to separate genuinely Möbius-specific information from generic multiplicative cancellation;
- Beurling/generalized-prime or randomized multiplicative models as controls for determining which mechanisms depend on the exact rational-prime system;
- possible bootstrap inequalities in which a weak global bound improves the local/correlation input strongly enough to feed back into a strictly better global bound.

### Scope and exclusions

This line owns arithmetic cancellation mechanisms centered on Möbius and closely related multiplicative functions. It does not own new geometric encodings of the primes, generic infinite-torus/Bohr representations, or general theories of information loss under compression.

Do not count the classical identity `1/zeta(s)=sum mu(n)n^{-s}` in its half-plane of absolute convergence, the standard RH-equivalent bound for `M(x)`, or a contour argument that assumes the required zero-free continuation as a new mechanism.

Do not promote probabilistic or random-walk heuristics for Möbius to evidence without an exact theorem connecting the model to the deterministic arithmetic function. Strong cancellation in almost all short intervals, logarithmic averages, or averaged correlations must not be silently upgraded to uniform global cancellation.

The disproved Mertens conjecture `|M(x)| < sqrt(x)` is a negative prior-art boundary, not a target strengthening to recover by heuristic argument.

### Line-specific falsification controls

For candidate mechanisms, test specifically whether:

- the claimed implication survives explicit constructions where strong local or averaged cancellation coexists with large exceptional global partial sums;
- the input controls exceptional intervals strongly enough for the proposed summation or chaining argument, rather than only almost-all behavior;
- a purported correlation gain is genuinely independent of mean-value information already encoded by Halász-type estimates;
- logarithmic averaging, smoothing, or truncation has erased exactly the rare coherent contribution that could dominate `M(x)`;
- the argument distinguishes Möbius from Liouville, generic non-pretentious multiplicative functions, random multiplicative functions, and suitably matched Beurling/generalized-prime systems;
- a use of `1/zeta(s)`, Perron inversion, or contour shifting has imported the desired zero-free region or RH-scale estimate circularly;
- an apparent square-root law is stable under removal of finite-range numerics and does not rely on random-walk independence that multiplicativity does not supply;
- any proposed bootstrap has a strict quantitative gain after all exceptional sets, logarithmic losses, smoothing errors, and scale transitions are included.

### Prior-art domains

- Möbius and Mertens summatory-function bounds and RH-equivalent criteria;
- Halász mean-value theory for multiplicative functions;
- Granville-Soundararajan pretentious multiplicative-function theory;
- Matomäki-Radziwiłł theory of multiplicative functions in short intervals and subsequent refinements;
- Chowla-type correlations, logarithmically averaged correlations, and Fourier uniformity of Möbius/Liouville;
- Dirichlet-polynomial, bilinear-form, Vaughan/Ramaré-type decompositions and related analytic-number-theory techniques;
- zero-free regions, zero-density results, Perron/Mellin methods, and explicit formulas only where their dependence on zero information is audited explicitly;
- random multiplicative functions and probabilistic models as adversarial comparators rather than substitutes for arithmetic proof;
- Beurling/generalized-prime systems and generalized Möbius functions as controls for rational-prime specificity.

### Relationship to other lines

`prime_lattice` studies the exponent-vector/Bohr/harmonic representation of multiplicative arithmetic; this line may use consequences from that language only when they produce concrete cancellation information for Möbius, and it does not own the ambient infinite-torus representation itself.

`arithmetic_fidelity` is complementary and transversal: its general results may help determine whether averaging, correlation summaries, smoothing, or spectralization have discarded the discriminator needed for global Möbius cancellation. Möbius Cancellation remains responsible for proving the arithmetic hypotheses and consequences in the concrete setting.

`weil_inertia` and `weil_positivity` approach zero location through explicit-formula forms, inertia, or positivity. A Möbius result may provide an independent arithmetic constraint on possible zero configurations, but this line does not inherit their matrix or positivity objectives.

`prime_circle` and `prime_flute` are geometrically distinct. Any future bridge must identify a proved shared arithmetic mechanism rather than treating geometric resemblance as evidence.