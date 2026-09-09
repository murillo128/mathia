# PL-240 — Quadratic reciprocity gives canonical mixed-prime support geometry, but it is the classical Rédei 4-rank matrix and opens a quadratic L-family

## Claim

A genuinely source-forced, nonlocal relation between different prime-coordinate directions already exists on every finite square-free support: **quadratic reciprocity organizes the selected primes into the classical Rédei matrix** of a quadratic field.

Let

`S={p_1,...,p_t}`

be distinct odd rational primes and put

`d_i=p_i^*=(-1)^((p_i-1)/2)p_i`,

`D_S=product_(i=1)^t d_i`.

Then every `d_i` is a prime discriminant and `D_S` is a fundamental discriminant. The square-free exponent-lattice vertex

`alpha_S=sum_(p in S) e_p`

therefore canonically determines the quadratic field

`K_S=Q(sqrt(D_S))`.

For this field, Rédei's matrix `R_S in M_t(F_2)` is built from quadratic Hilbert/Kronecker symbols between the ramified prime directions. In the convention recorded by Li--Yu,

`(R_S)_(ij)=lambda((p_i,D_S)_(p_j))`,

where `lambda:{+1,-1}->F_2` sends `+1` to `0` and `-1` to `1`. For `i!=j`, this coincides with the additive quadratic-residue symbol

`lambda((d_j/p_i))`.

The Hilbert-symbol product formula forces every row sum to vanish, so `R_S 1=0`. Rédei's theorem gives the exact arithmetic meaning of the remaining nullity:

`rank_4 Cl^+(K_S)=t-1-rank_(F_2)(R_S)=dim_(F_2) ker(R_S)-1`.

Thus the exponent lattice does possess a canonical **mixed-prime incidence geometry** that is richer than prime order, `log p`, fixed congruence colors, or a fixed Galois quotient: its zero modes are precisely the 4-rank of the narrow class group of the support-dependent quadratic field.

This is nevertheless a prior-art redirect rather than a zeta spectral mechanism. After transposing the off-diagonal matrix, row `i` consists of samples of the primitive quadratic Dirichlet character

`chi_(d_i)(q)=(d_i/q)`

at the other support primes. Its natural scalar analytic completion is therefore the quadratic Dirichlet `L`-function `L(s,chi_(d_i))`, not the Riemann zeta function. As the support changes, so do the characters, conductors, and quadratic fields. Pairwise quadratic reciprocity therefore escapes the *fixed-modulus/fixed-Galois* scalarizations of `PL-114`--`PL-116`, but it escapes into a classical **family of quadratic L-functions and class groups**, not into a new zeta-specific operator.

No canonical passage from the finite `F_2` Rédei nullity to the Riemann zero divisor, Weil positivity, or analytic continuation of `zeta` is supplied by this construction. A real or Hermitian lift of `R_S` can of course be diagonalized over `C`, but its real spectrum would then be a property of the chosen lift; the invariant selected by genus theory is the `F_2` rank/nullity above.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE-BOUNDARY + NO-NOVELTY-CLAIM`, decisive only against treating pairwise quadratic-residue incidence on a finite prime support as a new zeta-specific spectral mechanism.

## Exact support-dependent construction

The use of the starred primes is important. For an odd prime `p`,

`p^*=p` if `p=1 mod 4`,

and

`p^*=-p` if `p=3 mod 4`.

Hence `p^*=1 mod 4`, and a product of distinct prime discriminants is again a fundamental discriminant. The field `K_S` is therefore determined canonically by the square-free support `S`; there is no auxiliary modulus chosen independently of the lattice point.

Let `T={p_1,...,p_t}` be the finite ramified-prime set of `K_S/Q`. Li--Yu rederive the classical Rédei theorem from the Chevalley--Gras formula and define

`R_S=(lambda((p_i,D_S)_(p_j)))_(1<=i,j<=t)`.

Here `( , )_(p_j)` is the quadratic Hilbert symbol at `p_j`. The product formula for Hilbert symbols gives

`sum_j (R_S)_(ij)=0 in F_2`

for each `i`. For `i!=j`, Li--Yu identify the entry with

`lambda((d_j/p_i))`,

where `(d_j/p_i)` is the Kronecker/Legendre symbol. Consequently the matrix records a genuine pairwise arithmetic relation between different prime-coordinate directions.

Their stated Rédei theorem is

`rank_4 Cl^+(K_S)=t-1-rank_(F_2)(R_S)`.

With

`rank_4 Cl^+(K_S):=dim_(F_2)(Cl^+(K_S)[4]/Cl^+(K_S)[2])`,

this says exactly that the forced one-dimensional kernel coming from the row-sum relation is the trivial mode, while every additional null direction measures 4-torsion in the narrow class group.

This is much stronger arithmetically than inventing an adjacency matrix from labels after the fact: the matrix is a standard genus-theoretic invariant of the quadratic field canonically attached to the chosen support.

## Why this really escapes the earlier fixed-label obstructions

`PL-114` closes pair kernels obtained from a **fixed** finite congruence modulus: a finite character table diagonalizes them into scalar Dirichlet `L`-channels. `PL-115` and `PL-116` analogously close canonical central pair observables inside a **fixed** finite or profinite Galois source: harmonic analysis again decomposes them into scalar Artin channels.

The Rédei construction is not of that form. If one adds or removes a prime direction, both

`D_S`

and

`K_S=Q(sqrt(D_S))`

change. Moreover the residue symbol in one row naturally has conductor tied to that row prime. There is therefore no single fixed finite character table or fixed finite Galois extension through which all supports factor.

This is a real escape from those no-go hypotheses. It also uses more than the abstract order type excluded by `PL-237` or the one-dimensional consecutive log gaps of `PL-239`: an entry couples two actual rational-prime labels through a reciprocity law.

The escape, however, is classical genus theory. It demonstrates that “source-dependent mixed-prime relation” is a nonempty design class, but it does not by itself identify an RH mechanism inside that class.

## The natural analytic channel is quadratic `L`, not `zeta`

The Rédei matrix itself is finite and algebraic; no analytic continuation is needed to define it or to prove the 4-rank identity. To ask what analytic object is naturally generated by one pairwise-residue row, transpose the off-diagonal convention. Rank and nullity are unchanged by transposition, while for fixed `i` the off-diagonal entries become samples

`lambda(chi_(d_i)(p_j))`,

where

`chi_(d_i)(n)=(d_i/n)`

is the primitive real quadratic Dirichlet character of conductor `|d_i|=p_i`.

For `Re(s)>1`, and only using absolute Euler convergence,

`L(s,chi_(d_i))=product_q (1-chi_(d_i)(q)q^(-s))^(-1)`

and

`log L(s,chi_(d_i))=sum_q sum_(k>=1) chi_(d_i)(q)^k/(k q^(ks))`.

Thus extending the finite row from the selected primes to its canonical full prime sampling produces an ordinary quadratic Dirichlet `L`-function. The classical meromorphic/entire continuation and functional equation of that `L`-function are additional global analytic theorems; they are **not** consequences of the finite Rédei matrix or of the exponent-lattice embedding.

As `p_i` varies, the conductor varies. Hence the analytic closure of the pairwise reciprocity data is naturally a growing quadratic `L`-family. Its common critical symmetry line is `Re(s)=1/2`, but that is the standard Dirichlet functional-equation symmetry, not a mechanism selecting the Riemann zeros or proving their localization.

This distinction prevents an illegal shortcut: the finite `F_2` matrix contains exact residue data, but one cannot replace that finite data by an analytically continued `L`-function and then attribute the continuation or its zeros back to the matrix without proving a new bridge.

## Prior-art and novelty audit

The support-level matrix and the 4-rank identity are classical Rédei/Reichardt genus theory. Li--Yu provide a modern peer-reviewed derivation with an explicit Hilbert-symbol matrix and the exact formula

`rank_4 Cl^+(K)^+=t-1-rank R`

(in their notation, for the narrow class group of a quadratic field). Peter Stevenhagen's modern treatment of Rédei reciprocity goes further: higher Rédei symbols govern 8-rank phenomena and are controlled by Frobenius conditions on the prime divisors of the discriminant. Therefore even replacing pairwise Legendre symbols by the first natural higher reciprocity invariant is established arithmetic prior art and must not be presented as a new lattice construction.

A targeted search for Rédei-matrix spectral formulations found classical graph/tournament interpretations and extensive class-group applications, but no theorem making the ordinary Rédei matrix a zeta-specific Hilbert--Pólya operator or deriving Riemann-zero localization from its spectrum. Absence from that search is **not** treated as evidence of nonexistence; the durable claim here is only the positive prior-art identification and the exact analytic-channel reduction above.

This finding therefore makes no novelty claim for the matrix, the rank formula, quadratic reciprocity, or the quadratic `L`-family. Its contribution to this research line is the boundary identification: the most canonical obvious mixed-prime relation that survives the previous fixed-label controls is already a well-developed support-dependent arithmetic theory, and its first analytic completion branches away from the principal zeta channel.

## Adversarial controls and failure modes

**Rational-prime specificity survives.** Unlike generic order/log matched controls, Legendre/Kronecker symbols use the residue-field arithmetic of the actual rational primes. This finding does not dismiss them as programmable labels.

**The fixed-modulus control does not apply verbatim.** The row conductor and the field vary with the support. The conclusion is therefore not “`PL-114` already proves scalarization”; it is the more limited statement that the resulting non-fixed structure is classical and naturally family-valued.

**Real eigenvalues of an auxiliary lift prove nothing about RH.** The native Rédei matrix is over `F_2`, and its canonical arithmetic invariant in the quoted theorem is rank/nullity. Choosing signs `+/-1`, symmetrizing, or embedding into a Hermitian matrix creates a real spectrum by linear algebra unless a separate theorem shows that this lift controls a zeta trace/determinant or Weil form.

**Family averages are not ruled out.** Moments or averages of quadratic `L`-functions can contain zeta factors after character orthogonality. This finding does not claim that support-dependent reciprocity can never influence the principal zeta channel indirectly. It says that such an averaging/trace bridge would be new required structure; it is absent from the bare pairwise Rédei construction.

**Higher reciprocity is not automatically an escape.** Rédei's trilinear symbol and governing-field theory already encode higher `2`-power class-group information. A proposed trilinear or higher support tensor must be audited against that literature before being treated as new, and it must still explain why its analytic output is zeta-specific rather than another family invariant.

## Consequences for `prime_lattice`

`PL-239` left “a source-forced global relation among several prime coordinates” as a viable escape from local log-gap geometry. `PL-240` shows that this design requirement is mathematically meaningful: quadratic reciprocity supplies exactly such a relation, and its nullspace even has a canonical global arithmetic interpretation.

But it also removes the most immediate version of that escape from the novelty frontier. Future work should not spend passes rediscovering pairwise Legendre-symbol adjacency, Rédei matrices, or their direct `F_2` spectralization. Those objects should instead be used as a **matched arithmetic control** for any proposed mixed-prime mechanism.

A surviving mechanism must do at least one thing that the Rédei construction does not: couple the support-dependent reciprocity data canonically to the principal `zeta` channel, produce a trace/determinant whose continuation is derived rather than inserted, interact with the archimedean/functional-equation side of the explicit formula, or establish a positivity/duality statement strong enough to distinguish Riemann zeros from the surrounding quadratic `L`-family.

The next useful question is therefore narrower than “find any relation between prime directions”: it is whether there is a **source-forced mixed-prime relation with a proved principal-channel coupling** rather than merely a classical family-valued reciprocity invariant.

## Sources

- Jianing Li, Chia-Fu Yu, “The Chevalley–Gras formula over global fields,” *Journal de Théorie des Nombres de Bordeaux* **32**(2) (2020), 525–543. DOI: https://doi.org/10.5802/jtnb.1133. Example 2.6 gives the Rédei matrix via Hilbert symbols, identifies the off-diagonal Kronecker-symbol entries, notes the row-sum relation from the Hilbert product formula, and states `rank_4 Cl^+(K)=t-1-rank R`.
- Peter Stevenhagen, “Rédei reciprocity, governing fields and negative Pell,” *Mathematical Proceedings of the Cambridge Philosophical Society* **172**(3) (2022), 627–654. DOI: https://doi.org/10.1017/S0305004121000335. Modern source for Rédei reciprocity, higher Rédei symbols, governing fields, and their role in 8-ranks of narrow class groups.
- J. S. Milne, *Class Field Theory*, version 4.03 (2020), Chapter VIII, §5. https://www.jmilne.org/math/CourseNotes/CFT.pdf. Existing `prime_lattice` anchor for Hilbert symbols and the global product formula used as the reciprocity background.