# VIS-033 — complete xi-field visualizations collapse to the zero divisor

## Claim

Let `F` and `G` be nonzero entire functions of order at most one with the same zeros, counted with multiplicity. Suppose both satisfy the same Riemann-type reflection symmetry

`F(s)=F(1-s)` and `G(s)=G(1-s)`.

Then `F/G` is constant. Consequently, if one nonzero normalization value is also fixed, then `F=G` identically.

Applied to the Riemann xi function,

`xi(s) = (1/2)s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)`,

which is entire of order one and satisfies `xi(s)=xi(1-s)`, the complete nontrivial zero divisor together with the standard normalization determines the **entire complex xi field**. Equivalently, for

`Xi(z)=xi(1/2+i z)`,

the complete zero divisor, evenness `Xi(z)=Xi(-z)`, and one normalization determine `Xi` everywhere.

Therefore any exact visualization or statistic that is a deterministic functional of the complete xi field — domain coloring, modulus or phase portraits, level sets, Hardy/critical-line traces after known deterministic factors, derivatives and critical points, or another exact full-field rendering — is not an independent information channel once the complete xi zero divisor and normalization are already retained.

**Evidence/status:** `CLASSICAL-HADAMARD-FACTORIZATION + EXACT-DERIVED + DECISIVE-NEGATIVE/INFORMATION-QUOTIENT`.

No novelty is claimed for Hadamard factorization or uniqueness of entire functions from their canonical product. The Mathia contribution is the explicit information-accounting consequence for the canonical visual-atlas program.

## 1. Hadamard factorization leaves only an exponential quotient

For an entire function of order at most one, Hadamard factorization writes the function as a canonical product over its zeros multiplied by an exponential of a polynomial of degree at most one.

Because `F` and `G` have exactly the same zero divisor, choose the same canonical product `P(s)` for both. Then

`F(s)=exp(a_F s+b_F) P(s)`,

`G(s)=exp(a_G s+b_G) P(s)`.

Hence

`H(s)=F(s)/G(s)=exp(a s+b)`

with `a=a_F-a_G` and `b=b_F-b_G`.

This step is global. Unlike the disk result in `VIS-016`, no boundary-modulus data are supplied: finite-order growth plus the complete zero divisor has already reduced the remaining ambiguity to one affine exponential factor.

## 2. Reflection symmetry kills the exponential slope

The two functional equations imply

`H(s)=H(1-s)`.

Substituting the exponential form gives

`exp(a s+b)=exp(a(1-s)+b)`

for every complex `s`, so

`exp(a(2s-1))=1`

identically. Differentiating with respect to `s` forces `a=0`. Thus `H` is constant.

One nonzero normalization value fixes that constant. In particular, the standard xi normalization fixes the remaining scalar, so the complete zero divisor determines the complete xi field.

The same argument is especially transparent in the centered coordinate. If `F_c(z)=F(1/2+i z)` and `G_c(z)=G(1/2+i z)`, their quotient has the form `exp(alpha z+beta)` while both centered functions are even. Evenness of the quotient forces `alpha=0`.

No Riemann-Hypothesis assumption enters this argument. Off-critical-line zeros, if they exist, are simply part of the complete divisor.

## 3. Consequence for the canonical visual atlas

The accepted canonical-atlas clue proposed separating visual representations into mathematically independent families before treating agreement across panels as corroboration. At the level of **complete exact data**, the Hadamard uniqueness result makes that quotient much coarser than panel taxonomy suggests.

Once the complete xi zero divisor and normalization are retained, the following are deterministic re-renderings of one underlying object rather than independent evidence families:

- complete complex-plane value/domain-coloring portraits of `xi` or `Xi`;
- complete modulus, log-modulus, phase, phase-gradient, and level-set portraits;
- critical-line traces obtained from the same field, including `Xi(t)` and Hardy-type real traces after known deterministic factors;
- derivative fields, critical points, Taylor jets, and contour winding extracted from the reconstructed entire field;
- any exact transform or plot computed deterministically from the complete reconstructed `xi`/`zeta` field and fixed elementary factors.

This does **not** make those views visually redundant. They can expose different geometric features to a human or model and remain valuable search instruments. The negative result is epistemic: persistence of a feature across several such complete views is not independent mathematical evidence because all of them are recoverable from the same complete divisor.

## 4. Where genuinely different visual information can still live

The result shifts the useful notion of visual independence from a change of rendering to a change of **information retained**.

Potentially discriminating families must deliberately be lossy, partial, truncated, noisy, localized, differently conditioned, or externally matched. Examples include finite zero windows versus finite prime sums, sparse samples versus complete boundary data, low-frequency projections versus local spacing statistics, or matched null ensembles preserving selected lower-order information while destroying higher-order organization.

Two such views can be meaningfully different because neither need determine the complete xi field. Their residuals, approximation errors, or information losses may therefore carry distinct structure even though the exact infinite objects from which they descend are globally linked.

This also clarifies prime-versus-zero pictures. A complete exact zeta field is fixed once xi is fixed, because the gamma/polynomial completion factors are known. Thus an exact prime-side object deterministically recovered from the full zeta function is not independent at the complete-data level. A **finite prime truncation versus finite zero truncation** can nevertheless be a useful two-channel experiment because the truncations discard information differently; the hybrid Euler–Hadamard literature in `VIS-010` is precisely the kind of scale-dependent accounting required there.

## 5. Relation to the earlier local closure results

`VIS-013`–`VIS-015` show that complete concentric `log|F|` shell data decompose into zero sources plus harmonic boundary information. `VIS-016` then proves that, on one regular disk, the interior zero multiset plus full boundary modulus determines the holomorphic field up to a unimodular constant. `VIS-017` glues those local phase constants across connected overlapping disks, and `VIS-018` reduces contour phase winding to divisor count.

The present result is different in scope and in what data it needs. It does not use a boundary shell or an overlapping cover. For the global order-one xi function, the **complete divisor plus growth class and reflection symmetry** already determines the entire field up to one scalar, and standard normalization removes that scalar.

Thus the canonical-atlas independence quotient closes globally: changing from zeros to a complete exact field portrait does not add a new information carrier.

## Prior art and novelty assessment

The Encyclopedia of Mathematics entry **Riemann xi-function** records the classical facts used here: `xi` is a real entire function of order one, satisfies `xi(s)=xi(1-s)`, and has a Hadamard canonical product over its zeros. It cites the standard treatments of Edwards and Titchmarsh. Stable locator: `https://encyclopediaofmath.org/wiki/Riemann_xi-function`.

The abstract uniqueness lemma is an immediate specialization of the classical Hadamard factorization theorem: two finite-order entire functions with the same divisor have canonical factorizations differing only by the exponential polynomial allowed by their growth order. The reflection symmetry then removes the linear term by the elementary quotient argument above.

Accordingly, no new entire-function theorem or new property of `xi` is claimed. The durable result is the visual-research boundary: **complete exact xi-field views cannot provide independent corroboration beyond the complete xi divisor**.

## Boundary conditions and falsification

The conclusion requires the **complete** zero divisor, including multiplicities, and the correct finite-order/growth class. A finite zero window does not determine the complete field. Truncated canonical products can have material tail error, and two different reconstruction schemes can expose different numerical artifacts.

The result also assumes the exact reflection symmetry when removing the residual linear exponential factor. For a generic order-one entire function without that symmetry, the zero divisor alone leaves an `exp(a s+b)` ambiguity unless other normalization/growth data fix it.

A single scalar normalization is required after reflection. Without it, multiplication by a nonzero constant preserves both the zero divisor and the functional equation.

The finding does not say that two lossy measurements have equal information, that finite visualizations are statistically redundant, or that human perceptual usefulness is the same across renderings. It says only that at the complete exact analytic level they descend from one reconstructible field.

A falsification would require an order-at-most-one pair with the same complete zero divisor and the same reflection symmetry whose quotient is nonconstant, contradicting the Hadamard quotient form or the symmetry calculation.

## Research consequence

The accepted canonical-atlas clue should no longer search for "independent" families merely by changing complete representations of `xi`. The useful atlas is instead an **information-loss atlas**: each baseline should document what it discards, truncates, averages, conditions on, or replaces by a matched control.

Cross-view persistence becomes potentially meaningful only after this information quotient is explicit. A feature seen in domain coloring, modulus contours, and a critical-line trace is not three votes when all three are reconstructed from the same complete divisor. A feature surviving two deliberately non-equivalent partial channels can still generate a clue, provided the missing-information map and decisive control are stated precisely.
