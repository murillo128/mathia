---
id: CLUE-prime-lattice-quantitative-continuation-pole-tail-variance
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_lattice
based_on:
  - research/mobius_cancellation/findings/MC-525-polynomial-strip-growth-forces-pole-variance-on-every-block.md
  - research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md
  - research/prime_lattice/findings/PL-469-positive-sparse-block-sources-retain-negative-pole-residues.md
  - research/prime_lattice/clues/CLUE-density-one-dyadic-variance-arithmetic-recovery.md
---

# Can quantitative continuation control the pole tail in selected-block prime variance?

## Observation

PL-469 realizes positive bounded integer-supported residue sources with the correct leading masses, negative unit residues at a conjugate off-critical pole pair in every character channel, and complete retained-window variance at most `25X/16`. Its mesh omits `j_k-1,j_k` with `j_k=floor(k log k)`. Neither positivity, the residue sign nor finite pole count repairs recovery on that mesh. The construction supplies no quantitative vertical-growth bound.

MC-525 identifies a substantive extra hypothesis in the signed bounded-coefficient setting. If the only poles of `D(s)` in the closed infinite strip `sigma_0<=Re s<=2` are the simple pair `rho=beta+i gamma`, `bar rho`, with `1/2<sigma_0<beta<1`, `gamma>0`, and the pole-subtracted remainder is holomorphic near the strip and uniformly `O((1+|Im s|)^B)`, then

`V_a(X,H)>=c H^2 X^(2beta-1)`

for every sufficiently large real `X` and integer `1<=H<=h_0 X`. Its two compactly supported mean-zero tests retain both phases of the pole; a Mellin contour shift gives a uniform smaller remainder. Thus a diagonal ceiling at `H=floor X^theta` cannot hold on any unbounded scale set if `beta>1-theta/2`. MC-525 also proves that its MC-524 control necessarily fails the stated strip-growth hypothesis. This does not yet establish the analogous growth diagnosis for PL-469, whose source includes a periodic positive background.

The mechanism is classical smoothed Mellin asymptotics. Its unresolved arithmetic step is not a new contour identity: actual logarithmic derivatives have an infinite pole family, and an isolated zero at finite height is not an isolated pair throughout a strip.

## Research question

For PL-466's actual source

`a_n=Lambda(n) 1_(n=1 mod 5)`,
`D(s)=(1/4) sum_(chi mod 5) -L'(s,chi)/L(s,chi)`,

can a quantitatively controlled contribution from the remaining poles replace MC-525's isolated-pair hypothesis in a centered-variance lower bound? Fix `0<theta<1` and a hypothetical zero `rho=beta+i gamma` with `beta>1-theta/2`, `gamma!=0`. The pole at 1, its deterministic mean profile, all other zero residues and all contour errors must be retained.

For real mean-zero tests `f_i` supported in `(1,2)`, put `S_(X,H)(y)=sum_(y<n<=y+H) a_n`, let `m_(X,H)` be its empirical mean on `[X,2X]`, and define

`L_i(X,H)=(1/H) int_X^(2X) (S_(X,H)(y)-m_(X,H)) f_i(y/X) dy`.

The concrete target is a finite bank with `sum_i |L_i(X,H)|^2 / sum_i ||f_i||_2^2 >= c X^(2beta)` at `H=floor X^theta`. Can the negative residue law and available off-pole logarithmic-derivative bounds force this uniformly on a declared unbounded set of large scales, despite the infinite remaining zero family? Do not assume a rightmost zero, a horizontal gap below it, or a polynomial bound for a holomorphic remainder unless separately justified.

## Why it may matter

PL-466 recovers poles from every dyadic block without quantitative vertical growth. PL-469 defeats a weaker coverage premise even with positivity and sparse poles. A valid additional continuation/tail condition would identify what analytic information an actual-prime recovery argument must use beyond that control. It would not supply the source variance ceiling itself.

This is a separate growth-and-tail test, not a second copy of the accepted `3^k`-mesh question. Any application to that mesh, to the moderate mesh or to Farey-selected scales must state its own coverage conclusion. A lower bound on an unbounded set disjoint from the measured blocks gives no contradiction.

## Decisive test

First calibrate the transfer on a positive periodic residue background plus one conjugate pole pair: retain the periodic counting error and check whether MC-525's mean-zero window identity yields the same floor under a polynomially bounded pole-subtracted remainder. Test PL-469 against the resulting growth hypothesis. Do not substitute bounded coefficients for the actual von Mangoldt source without checking convergence and normalization.

Then write the *actual* smoothed Mellin identity with a finite-height pole packet and its remaining contour/pole contribution explicit. Price the smallest singular value of the packet's mean-zero profile Gram matrix, the test norms and derivative bounds, the contour distance from every pole, and the complete high-height tail. The decisive positive certificate is that the remaining vector has norm strictly below the packet's phase-uniform lower bound on the claimed scales. If packet size or cutoff grows with `X`, these costs must be uniform in that growth; fixed-packet estimates cannot be substituted.

Determine whether the standard arithmetic bounds actually provide that certificate without a zero-free premise. A useful negative outcome is an explicit admissible meromorphic residue-source control satisfying the proposed **quantitative** hypotheses but violating the claimed variance lower bound, or an exact demonstrated loss in this test bank. Lack of a tail estimate alone is an unfinished transfer, not a counterexample to recovery. Sublinear pole counts alone do not bound the magnitude or cancellation of the smoothed pole sum. Audit the classical Mellin converse-mapping and prime-variance converse literature before assigning novelty to any extension.

**Bounded source reading for Prime Lattice:** read exactly `research/mobius_cancellation/findings/MC-525-polynomial-strip-growth-forces-pole-variance-on-every-block.md` for the mean-zero two-test construction, uniform shrinking-window contour shift and exact centered pairing. Include its adjacent `research/mobius_cancellation/findings/MC-525-polynomial-strip-growth-forces-pole-variance-on-every-block.review.md` if present. The inspected revision is `15cde40eeec19402470ed8d4324c3fa609dcac13`; recheck current source and review state. MC-525 contains the required proof in full. This grant is read-only, limited to this test, and permits no other Möbius files or recursive dependency traversal. The other cited mathematical sources are destination-local.

## Evidence boundary

MC-525 establishes only its fixed isolated-pair theorem. PL-469 establishes the positive control on its stated mesh; its growth diagnosis and the proposed infinite-pole transfer remain unproved here. No every-block lower bound for actual primes, sparse-scale zero-free criterion, independent arithmetic estimate, RH/GRH result or external novelty is asserted. The accepted thin-mesh clue and the resolved moderate-mesh control retain their existing dispositions. A theorem needing an isolated rightmost finite pole cluster would be a conditional result, not a resolution for the actual unrestricted zero set.
