# VIS-412 — Wang dyadic shells are Bohr-orthogonal, so intrinsic Bargmann cycles vanish

## Claim

Use the near-ratio Wang decomposition from `VIS-313`. For dyadic `M`, let

`F_M(T)=sum_(lambda in Lambda_M) B_lambda exp(-i lambda T)`

be the contribution with

`M < max(q,r) <= 2M`, `0<|log(q/r)|<log 2`,

where `lambda=log(q/r)` and the near-band pair `(q,r)` has distinct prime bases.

Then distinct dyadic shells have disjoint frequency supports:

`M != N  =>  Lambda_M intersect Lambda_N = emptyset`.

With the canonical Bohr mean inner product

`<f,g>_B = lim_(V->infinity) V^(-1) integral_0^V conjugate(f(T)) g(T) dT`,

one therefore has the exact orthogonality relation

`<F_M,F_N>_B = 0` for `M != N`.

Consequently, for any finite family of distinct Wang dyadic shells, the frame graph of `VIS-411` has no edges. Every Bargmann cycle product involving distinct shells is zero, so its phase is **undefined rather than a nontrivial holonomy**. The canonical intrinsic Bohr geometry of these Wang shells therefore cannot supply the source-forced cross-shell cycle phase left open by `VIS-411`.

This is a representation-specific negative result. If the same shells are restricted to a finite interval, tapered, or embedded into another non-orthogonal Hilbert representation, their pairwise overlaps need not vanish. Those finite-window overlaps are real data, but they are window/kernel couplings rather than intrinsic Bohr Gram entries and require their own source-specificity and stability tests.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-BOHR/PARSEVAL-ORTHOGONALITY + REPRESENTATION-BOUNDARY + NO-NOVELTY-CLAIM`.

## 1. The dyadic shell supports are exactly disjoint

`VIS-313` proves that every strict near-band frequency comes from prime powers with distinct base primes. Hence `q` and `r` are coprime, and the reduced rational ratio `q/r` uniquely determines the oriented pair `(q,r)`.

The dyadic shell label is then determined by that pair through `max(q,r)`. With the usual disjoint dyadic intervals

`M < max(q,r) <= 2M`,

one oriented pair belongs to exactly one shell. Therefore one frequency cannot occur in two distinct shell supports. The reverse frequency `-lambda`, coming from `(r,q)`, has the same value of `max(q,r)` and remains in the same shell.

Thus

`Lambda_M intersect Lambda_N = emptyset`

for distinct dyadic shell labels `M,N`.

This step is specific to the cross-base near band. It uses exactly the uniqueness mechanism already established in `VIS-313`; it would fail for a shell construction in which the same grouped frequency is deliberately copied across labels.

## 2. Bohr mean orthogonality kills every cross-shell Gram edge

For two distinct real frequencies `lambda != mu`, direct integration gives

`V^(-1) integral_0^V exp(i(lambda-mu)T) dT -> 0`

as `V->infinity`.

Each fixed dyadic shell is a finite exponential polynomial, because only finitely many prime powers satisfy `max(q,r)<=2M`. Expanding the Bohr inner product term by term therefore gives

`<F_M,F_N>_B`
` = sum_(lambda in Lambda_M) sum_(mu in Lambda_N)`
`   conjugate(B_lambda) B_mu <exp(-i lambda T),exp(-i mu T)>_B`.

When `M != N`, disjoint support implies `lambda != mu` for every pair in the double sum, so every term is zero and

`<F_M,F_N>_B=0`.

No cancellation estimate is involved. The result is exact orthogonality in the intrinsic mean-square geometry of the almost-periodic exponential representation.

For the normalized rays used in projective geometry, the conclusion is unchanged whenever `F_M` and `F_N` are nonzero: their normalized overlap is still zero.

## 3. The Bargmann frame graph is edgeless

`VIS-411` shows that after quotienting independent shell phases, phase-sensitive relational information is carried by closed products of nonzero Gram entries. An edge `{M,N}` exists only when

`G_(MN)=<F_M,F_N> != 0`.

For the Wang dyadic shells in Bohr geometry, every off-diagonal Gram entry vanishes. Hence the frame graph is a discrete set of vertices with no cross-shell edge and therefore no cycle.

For three distinct shells, for example,

`Delta_(MNP)=<F_M,F_N>_B <F_N,F_P>_B <F_P,F_M>_B = 0`.

It is important not to assign phase zero to this product. Its argument is undefined because the complex number itself vanishes. There is therefore no hidden projective phase to extract from a finer visualization of the same intrinsic Gram geometry.

This closes one specific escape route from the information-loss controls in `VIS-409`--`VIS-411`: **the canonical Wang dyadic-shell Bohr Hilbert structure does not force nontrivial Bargmann holonomy between distinct shells.**

## 4. Finite windows create nonzero overlap by sinc leakage

The obstruction above does not say that finite-window cross-shell plots must be blank. Replace the Bohr mean by the normalized interval inner product on `[T0,T0+V]`. For two pure frequencies and `Delta=mu-lambda`,

`V^(-1) integral_(T0)^(T0+V) exp(i Delta T) dT`
` = exp(i Delta (T0+V/2)) sinc(Delta V/2)`,

where `sinc(z)=sin(z)/z`.

Thus distinct frequencies acquire nonzero overlap whenever the sinc factor is nonzero. Summing over shell coefficients produces a finite-window Gram entry depending on

- the shell coefficient arithmetic;
- the cross-shell frequency spacings;
- the window width `V`;
- the window center `T0`;
- and any taper or kernel used instead of the sharp interval.

Such an overlap can still be mathematically useful. What this finding rules out is calling its phase an **intrinsic Bohr shell holonomy**. A finite-window cycle must instead survive explicit perturbations of window center, width, and taper, and must discriminate the arithmetic source from matched controls preserving the relevant shell energies/frequency geometry, before it can support a source-specific claim.

In particular, a nonzero finite-window Bargmann product does not contradict the zero Bohr product: the two constructions use different Hilbert geometries.

## 5. Prior art and novelty boundary

The load-bearing orthogonality is classical almost-periodic Fourier theory. A. S. Besicovitch, **Almost Periodic Functions**, Cambridge University Press (1932), develops generalized Fourier expansions and the Parseval/Riesz-Fischer mean-square theory for almost-periodic functions. The original generalized almost-periodic framework is also in A. S. Besicovitch, **On Generalized Almost Periodic Functions**, *Proceedings of the London Mathematical Society* s2-25 (1926), 495--512, DOI `10.1112/plms/s2-25.1.495`.

For the present finite exponential polynomials, however, no deep theorem is needed: orthogonality follows directly from the displayed elementary mean integral. The almost-periodic literature supplies the canonical Hilbert-space interpretation and confirms that this is standard Parseval geometry rather than a new analytic theorem.

The projective-cycle side is already classicalized by `VIS-411`, which records the finite-frame/Bargmann invariant literature, including Chien and Waldron, **A Characterization of Projective Unitary Equivalence of Finite Frames and Applications**, *SIAM Journal on Discrete Mathematics* 30:2 (2016), 976--994, DOI `10.1137/15M1042140`.

No novelty is claimed for Bohr orthogonality, Parseval theory, orthogonal frame components, or the fact that a Bargmann product containing a zero overlap vanishes. The Mathia-specific contribution is the exact specialization to the Wang dyadic ratio shells of `VIS-313` and the resulting closure of the intrinsic cycle-holonomy question opened by `VIS-411`.

## 6. Boundaries and falsification

This finding applies to the `VIS-313` strict near-band dyadic shell family equipped with the Bohr mean inner product. It does not prove that every conceivable Wang-derived shell family is orthogonal, and it does not apply automatically to logarithmic-coordinate `L^2` profiles, finite-window embeddings, tapered packets, cross-Wigner constructions, or deliberately overlapping shell decompositions.

It also does not say finite-window overlaps contain no arithmetic information. Their coefficients and frequency spacings are source-derived. The negative statement is narrower: nonzero finite-window cycles are not invariants of the canonical infinite-horizon Bohr Gram geometry.

Falsify the core claim by exhibiting a nonzero near-band grouped frequency that belongs to two distinct `VIS-313` dyadic shells, or by finding a distinct-frequency exponential pair with nonzero Bohr mean inner product. Either would break the orthogonality argument. A useful extension rather than a falsification would be a different, explicitly justified non-orthogonal source geometry whose gauge-invariant cycles remain stable under its natural controls.

## Dependencies

- `VIS-313`: unique cross-base near-band ratios and dyadic Wang shell decomposition.
- `VIS-410`: distinction between faithful multi-shell coherence and representation-induced/scalarized information loss.
- `VIS-411`: independent shell phase gauge and Bargmann cycle invariants.

## Research consequence

For the current Wang construction, the next positive cross-shell direction should **not** search for a Bargmann phase in the intrinsic Bohr Gram matrix: there are no cross-shell edges there to carry one.

A genuinely new source-derived relational mechanism must therefore change at least one ingredient in a mathematically explicit way: use a non-orthogonal packetization with a principled source meaning, study a finite-window/tapered cycle and prove stability plus arithmetic discrimination, or identify a different gauge-invariant multilinear coupling not reduced to the Bohr pairwise Gram graph. Merely rendering the same orthogonal shell family with a richer phase-space visualization cannot create the missing relation.