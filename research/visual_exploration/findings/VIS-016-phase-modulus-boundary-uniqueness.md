# VIS-016 — zero set plus boundary modulus determines the disk field up to global phase

## Claim

Let `F` be holomorphic on a neighborhood of the closed disk `|w|<=R`, with no zero on `|w|=R`. Suppose the interior zeros, with multiplicity, are known.

Then the interior zero multiset together with the boundary modulus

`theta -> |F(R exp(i theta))|`

determines `F` throughout `|w|<R` **up to multiplication by one unimodular constant**.

Equivalently, if `F_1` and `F_2` are holomorphic on a neighborhood of the same closed disk, have exactly the same zeros in the disk with the same multiplicities, have no boundary zeros, and satisfy

`|F_1(Re^{i theta})| = |F_2(Re^{i theta})|`

for every `theta`, then there is a real constant `alpha` such that

`F_1(w) = exp(i alpha) F_2(w)`

throughout the disk.

After the common zero factors are removed, the phase is therefore not an independent visual or multiscale channel. If `Q` is the resulting zero-free factor and

`log Q = u + i v`

is a holomorphic logarithm, then `v` is the harmonic conjugate of `u=log|Q|`, unique up to an additive constant. On every concentric circle `|w|=r<R`, with Fourier coefficients

`u_n(r) = (1/(2 pi)) int u(r e^{i theta}) e^{-i n theta} d theta`

and similarly `v_n(r)`, one has for every `n>=1`

`v_n(r) = -i u_n(r)`,

while the negative modes are the conjugates and only the zeroth phase mode remains free.

**Evidence/status:** `CLASSICAL-COMPLEX-ANALYSIS + EXACT-DERIVED + DECISIVE-NEGATIVE/BASELINE`.

No novelty is claimed for the maximum-modulus principle, holomorphic logarithms, harmonic conjugates, or boundary phase retrieval in this regular disk setting. The durable Mathia consequence is that adding phase to the concentric-shell program does not evade the source-plus-boundary information closure established in `VIS-013`–`VIS-015`.

## Exact uniqueness proof

Assume `F_1` and `F_2` satisfy the hypotheses. Their quotient

`h = F_1/F_2`

has removable singularities at the common interior zeros because the multiplicities agree. After those cancellations, `h` is holomorphic and zero-free on a neighborhood of the closed disk.

On the boundary,

`|h| = 1`.

The maximum-modulus principle applied to `h` gives `|h|<=1` in the disk. Since `h` has no zeros, `1/h` is holomorphic there; applying the same principle to `1/h` gives `|h|>=1`. Hence `|h|=1` everywhere in the disk.

A nonconstant holomorphic map has open image, whereas the unit circle has empty interior. Therefore `h` is constant, and the boundary modulus forces that constant to have modulus one:

`h = exp(i alpha)`.

This proves the claim directly, without a numerical or visual assumption.

## Harmonic-conjugate shell form

Let the zeros of `F` in the disk be `a_j` with multiplicities `m_j`, and factor them explicitly, for example locally as

`P(w) = product_j (1-w/a_j)^{m_j}`

after separating any zero at the center in the usual way. The quotient

`Q(w)=F(w)/P(w)`

is zero-free on the disk, so on the simply connected disk it has a holomorphic logarithm

`g(w)=log Q(w)=sum_{n>=0} b_n w^n`.

Writing `g=u+i v`, the real and imaginary parts are harmonic conjugates. On `w=r e^{i theta}`,

`u_n(r) = (b_n/2) r^n`,
`v_n(r) = (b_n/(2i)) r^n = -i u_n(r)`

for `n>=1`.

Thus a boundary shell of `log|Q|` fixes every nonconstant phase mode on that shell and, through the same `r^n` analytic scaling, fixes the phase on every smaller concentric shell. The remaining degree of freedom is exactly one additive phase constant, corresponding to the unimodular factor in the uniqueness theorem.

This is stronger than saying that phase and log modulus often look correlated. In the zero-free quotient they are the two conjugate components of one holomorphic logarithm.

## Combination with the Poisson–Jensen closure

`VIS-015` decomposes the complete concentric circular `log|F|` field into:

1. explicit Green/logarithmic potentials of the interior zeros, carrying their radial and angular configuration; and
2. a zero-free harmonic background determined by one boundary shell.

The present finding shows that, once those same zero factors are known, the phase of the zero-free background is already determined by its log modulus up to one constant. The zero factors themselves also determine their own argument/winding contribution.

Therefore, under the regular disk hypotheses, the data

`interior zero multiset + boundary modulus`

determine the entire complex holomorphic field in the disk up to one global phase. Adding domain-coloring hue, unwrapped phase, phase-gradient texture, or phase shells to the same disk does not create an additional information carrier after the zero set and boundary modulus have been retained.

This does **not** make phase plots useless. They can be excellent representations of winding, zeros, critical points, or branch structure. The point is narrower: after the exact zero and boundary-modulus information has already been counted, phase is not an independent residual.

## Visual check

The retained artifact

`research/visual_exploration/visualizations/phase-logmod-conjugacy.md`

illustrates the harmonic-conjugate relation on a local shell around the numerically tabulated 100th critical-line zeta zero.

For the illustration only, set

`rho_100 = 1/2 + i gamma_100`,
`gamma_100 = 236.5242296658162058...`

and evaluate the zero-normalized field

`H(w)=xi(rho_100+w)/(xi'(rho_100) w)`.

On the shell `r=0.8`, 1024 angular samples were used to form

`u(theta)=log|H(r e^{i theta})|`

and a continuous, mean-centered numerical phase `v(theta)`. The phase reconstructed from `u` by the circular Hilbert-transform Fourier multiplier `-i sign(n)` agrees with the directly sampled phase to floating-point accuracy.

Across ten sampled radii from `0.15` through `1.0`, using 512 angular samples per shell, the largest absolute reconstruction discrepancy was `8.88e-16`. At `r=0.8`, the largest residual in the positive-mode identity `v_n=-i u_n` over modes `1..12` was `2.12e-17`.

These numbers are **only a numerical integrity illustration** of the classical theorem. They are not a certified zero-free region for `xi`, not evidence about off-critical-line zeros, and not part of the proof.

## Research consequence

The accepted multiscale clue had left phase or another intrinsic field as a possible escape from the complete concentric `log|xi|` closure. Phase itself is now closed under the same information accounting.

A future visual candidate must therefore retain information not already reconstructible from

`zero configuration + boundary modulus + one global phase`.

For a single regular disk around one center, merely replacing modulus by phase, combining the two as domain coloring, plotting phase gradients, or following phase across nested shells cannot supply a new invariant after this quotient.

The live directions become sharper: relations among several centers that are not reducible to the same underlying zero coordinates, statistics of the zero configuration against genuinely matched point-process controls, or observables carrying information not determined by the holomorphic function's zero set and one boundary modulus.

## Prior art and novelty assessment

The proof is elementary classical complex analysis. John B. Conway's *Functions of One Complex Variable I*, 2nd edition, contains the maximum-modulus theorem and the harmonic-function/harmonic-conjugate machinery used here. The disk Fourier relation is the standard conjugate-harmonic/Hilbert-transform relation for real and imaginary parts of a holomorphic function.

Hardy-space inner/outer factorization gives a broader boundary-value framework, but that machinery is not needed under the present stronger assumption that the functions extend holomorphically across the boundary and that the complete interior zero multiset is supplied.

`VIS-016` therefore claims no new theorem of phase retrieval or complex analysis. Its contribution is the exact negative-control specialization for Mathia's current visual program: **phase does not survive as an independent concentric-disk information channel once the zero set and boundary modulus have been quotiented.**

## Boundary conditions and falsification

The theorem assumes the compared functions have the same complete zero multiset in the disk, including multiplicities, and no zeros on the boundary. It also uses full boundary modulus, not finitely many samples.

The regularity across the closed disk matters. In rough Hardy-space boundary settings, singular inner factors can be zero-free and unimodular almost everywhere on the boundary, so boundary modulus plus ordinary interior zeros need not capture all inner data without additional hypotheses. That is outside this finding's regular disk claim.

Likewise, phaseless data on sparse curves or discrete samples constitute a genuine phase-retrieval problem and are not covered by the full-boundary theorem.

The finding does not say that cross-center phase relations, critical-point data, derivatives, or non-holomorphic observables are redundant. It says only that within one regular simply connected disk, once the complete zero set and boundary modulus are retained, the holomorphic field itself is fixed up to a single global phase.
