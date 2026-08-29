# Literature anchors for the prime-flute notes

This is a compact **source map**, not a new Riemann corpus. It records the external theorems used by `FINDINGS.md` and the points that still need primary-source auditing before they are promoted to theorem-level project evidence.

Do not copy full source text here. Preserve only bibliographic/provenance information and the exact role the source plays in our deductions.

## S1 — zero-twist tight flutes

**A. Arredondo, C. Morales, C. Ramírez Maluendas**, *Parabolicity of zero-twist tight flute surfaces and uniformization of the Loch Ness monster*, arXiv:2108.12487; Lobachevskii Journal of Mathematics 43 (2022), DOI: 10.1134/S1995080222040035.

- https://arxiv.org/abs/2108.12487
- https://doi.org/10.1134/S1995080222040035

Used for:

- construction of a torsion-free Fuchsian group from an increasing positive endpoint sequence;
- identification of the resulting convex core as a zero-twist tight flute;
- first-kind/parabolic criteria in terms of divergence of the endpoint-spacing series.

Relevant findings: PF-001 (geometric setup), PF-012.

**Audit note.** Our explicit matrix identities in PF-004 should be checked independently even if the generator convention is taken from this construction, because sign/orientation conventions can differ.

## S2 — type/parabolicity via Fenchel-Nielsen data

**A. Basmajian, H. Hakobyan, D. Šarić**, *The type problem for Riemann surfaces via Fenchel-Nielsen parameters*, Proceedings of the London Mathematical Society 125 (2022), 568–625; arXiv:2011.03166. DOI: 10.1112/plms.12465.

- https://arxiv.org/abs/2011.03166
- https://doi.org/10.1112/plms.12465

Used for:

- parabolicity criteria for zero-twist flutes in terms of cuff/Fenchel-Nielsen parameters;
- background for why some scalar cuff sums detect conformal type while remaining too coarse for fine prime-gap arithmetic.

Relevant findings: PF-001, PF-002, PF-012.

## S3 — shear coordinates / quasisymmetry

**D. Šarić**, *Shears for quasisymmetric maps*, arXiv:2004.04575.

- https://arxiv.org/abs/2004.04575

Used for:

- the standard interpretation of fan shears as logarithms of ratios of adjacent horocyclic intervals/cross-ratios;
- quasisymmetric control through shear data.

Relevant finding: PF-003.

## S4 — ratios and isolated clusters of consecutive prime gaps

**J. Pintz**, *On the ratio of consecutive gaps between primes*, arXiv:1406.2658.

- https://arxiv.org/abs/1406.2658

Verified uses:

- consecutive prime-gap ratios are arbitrarily small and arbitrarily large;
- Theorem 2/proof gives, for arbitrary fixed `k0`, infinitely many bounded clusters of at least `k0` consecutive primes surrounded on both sides by growing prime-free intervals of Erdős-Rankin scale.

Relevant findings: PF-003, PF-007.

**Important wording discipline.** The exact theorem statement should be quoted/paraphrased from the source when imported into a formal research artifact. `LEAN_CANDIDATES.md` currently uses mnemonic interfaces only.

## S5 — one small gap between two large neighboring gaps

A Goldston–Pintz–Yıldırım/Pintz result is recorded in the literature in the form

```text
limsup min(d_{n-1}, d_{n+1}) /
       (d_n (log n)^c) = infinity,

c = 1/632.
```

This statement was independently located during the exploration as Theorem 7.6 in an ICM proceedings exposition by Pintz.

Used for:

- the arithmetic input in PF-005, turning the exact PF-004 cross-ratio formula into a sequence of closed hyperbolic elements with translation length tending to zero.

Relevant finding: PF-005.

**SOURCE AUDIT REQUIRED.** Before this is used as a frozen theorem dependency or Lean import, pin the primary paper and exact indexing convention for `d_n`. The secondary proceedings statement is enough for the research ledger but not for a final formal dependency.

## S6 — Baker-Harman-Pintz short intervals

**R. C. Baker, G. Harman, J. Pintz**, *The Difference Between Consecutive Primes, II*, Proceedings of the London Mathematical Society 83 (2001), 532–562. DOI: 10.1112/S0024611501012690.

- https://doi.org/10.1112/S0024611501012690

Used for:

- the unconditional exponent `0.525`, equivalently the existence of a prime in `[x, x+x^0.525]` for sufficiently large `x`;
- a convenient unconditional bound implying convergence of sums such as `sum (g_n/p_n)^2` in our application.

Relevant findings: PF-001, PF-002.

## S7 — small eigenvalues under hyperbolic degeneration

**M. Burger**, *Asymptotics of small eigenvalues of Riemann surfaces*, Bulletin of the American Mathematical Society 18 (1988).

- https://www.ams.org/journals/bull/1988-18-01/S0273-0979-1988-15576-5/S0273-0979-1988-15576-5.pdf

Used for:

- degeneration of small Laplace eigenvalues to a weighted graph when separating geodesics are pinched;
- graph vertices weighted by component areas and edges by total lengths of separating geodesics;
- the normalization `lambda_j(surface) / lambda_j(graph) -> 1/pi` in Burger's theorem.

Relevant finding: PF-014.

**Scope warning.** Burger's theorem concerns controlled degenerating families. It does not directly prove that the one fixed infinite prime-flute is globally equivalent to an infinite graph.

## S8 — cyclotomic/trigonometric degree fact

For odd `n`, a standard cyclotomic calculation gives

```text
[Q(tan(pi/n)) : Q] = phi(n),
```

and hence for an odd prime `p`,

```text
[Q(cot(pi/p)) : Q] = p-1.
```

A concrete derivation/reference located during the exploration is in University of Groningen lecture notes on advanced algebraic structures, in the section treating tangent values and cyclotomic fields.

Used for:

- the unbounded algebraic-degree step in PF-010.

Relevant finding: PF-010.

**SOURCE AUDIT REQUIRED.** Prefer replacing the lecture-note pointer with a standard cyclotomic-field theorem already available in mathlib or a primary algebra reference when formalization starts. The mathematical step itself is standard; the current issue is provenance quality, not plausibility.

## S9 — classical prime zeta identity

The classical prime zeta function

```text
P(s) = sum_p p^(-s)
```

satisfies, in its initial domain and by continuation through the usual logarithmic relation,

```text
P(s) = sum_{k>=1} mu(k)/k * log(zeta(k s)).
```

Used for:

- interpreting PF-011: once the one-dimensional spine zeta is reduced to prime zeta plus a holomorphic term, its Riemann-zero singularity structure is inherited from an already classical arithmetic object rather than created by new surface spectral dynamics.

Relevant finding: PF-011.

**SOURCE AUDIT REQUIRED.** Pin a standard prime-zeta reference before this identity is used in a publication-level claim. It is not needed for the first Lean milestone.

## S10 — sources still to pin for lower-priority negative branches

The following branches were useful for exploration but should not be promoted until their source hypotheses are checked precisely:

- Patterson-Sullivan uniqueness/divergence-type hypotheses behind the strongest form of PF-012;
- exact modular primitive-Hecke double-coset normalization used in the historical PF-009 derivation;
- finite-type Selberg/Ruelle convergence hypotheses used for comparison in PF-006;
- the precise spectral-convergence theorem required by PF-008.

These omissions are intentional. `FINDINGS.md` marks the affected claims as negative background or `NEEDS-AUDIT` rather than pretending the sourcing is complete.

## S11 — asymptotically isometric infinite-type structures

**F. Yaşar**, *Infinite-dimensional Teichmüller spaces*, arXiv:2104.00289 (2021).

- https://arxiv.org/abs/2104.00289

Used for:

- prior-art context for asymptotically isometric / asymptotic length-spectrum equivalence on infinite-type hyperbolic surfaces;
- checking whether the uniform tail equivalence in PF-105 is already an instance of a standard Fenchel-Nielsen theorem.

Relevant finding: PF-105.

**Scope warning.** Yaşar's Fenchel-Nielsen characterization of `T^0_ls(H_0)` is stated under an **upper-bounded base surface** hypothesis. The prime-flute's distinguished cuffs tend to infinity, so PF-105 does not invoke that theorem. Its `O(P^-2)` cross-ratio/separator bounds and `ell^1` fan-shear defect are derived directly from the exact endpoint law.

## S12 — bounded ideal triangulations and quasiconformal length distortion

**D. Šarić, C. Whitney**, *Bounded ideal triangulations of infinite Riemann surfaces*, Journal of the London Mathematical Society 112 (2025), e70276. DOI: 10.1112/jlms.70276; arXiv:2502.05590.

- https://arxiv.org/abs/2502.05590
- https://doi.org/10.1112/jlms.70276

**H. Shiga**, *On the hyperbolic length and quasiconformal mappings*, Complex Variables, Theory and Application 50 (2005), 123–130. DOI: 10.1080/02781070412331328206.

- https://doi.org/10.1080/02781070412331328206

Used for:

- Whitney--Šarić Proposition 4.2: a surface carrying their bounded ideal triangulation is quasiconformal to a zero-shear representative whose covering group is a subgroup of `PSL_2(Z)`;
- the classical Wolpert inequality `K^-1 ell_X(c) <= ell_Y(f_*(c)) <= K ell_X(c)` for a `K`-quasiconformal map, stated by Shiga for hyperbolic Riemann surfaces;
- PF-110's literature-derived obstruction: a torsion-free subgroup of `PSL_2(Z)` has hyperbolic traces of absolute value at least `3`, hence a positive closed-geodesic length floor, and quasiconformal length distortion transfers positive systole back to every surface with a bounded ideal triangulation.

Relevant finding: PF-110; relevant local clue: `CLUE-affine-composite-clone-relative-operator-class.md`.

**Novelty discipline.** The modular trace floor and quasiconformal length inequality are classical, and Whitney--Šarić supply the substantive structural theorem. PF-110 does not claim a new general triangulation theorem; it records the immediate corollary and uses it to close the previously proposed bounded-triangulation route for the zero-systole prime flute.

## S13 — pair-of-pants marked-length comparison

**W. P. Thurston**, *Minimal stretch maps between hyperbolic surfaces*, preprint, arXiv:math/9801039 (1998).

- https://arxiv.org/abs/math/9801039

Used for:

- Lemma 3.4 (`Shrinking at the waist`): for two marked hyperbolic pair-of-pants structures, any nonperipheral fundamental-group element whose marked geodesic length increases has ratio strictly below the largest corresponding boundary-length ratio;
- PF-111's two-direction specialization, after approximating the common cusp by equal positive boundary length, which turns PF-107's summable relative cuff defect into a summable sequence of uniform distortions for the entire marked closed-geodesic spectrum of each individual tight pant.

Relevant finding: PF-111; relevant local clue: `CLUE-affine-composite-clone-relative-operator-class.md`.

**Scope warning.** PF-111 is pant-local. Thurston's lemma does not by itself control closed geodesics that traverse several pants, produce an equivariant global comparison, or imply any relative Laplacian/operator-ideal statement.

## Provenance policy for future additions

For each future finding, record separately:

```text
1. exact custom statement we derived;
2. finite algebra/computation that can be independently checked;
3. external theorem(s) it imports;
4. exact hypotheses of those theorems;
5. whether the bridge is proved, conjectural, or still needs audit;
6. whether a Lean formalization can isolate the custom finite core.
```

A negative result is worth preserving when it rules out a plausible conceptual bridge. For Mathia, those failed bridges are training/evaluation material for recognizing telescoping, universality, imported structure, non-uniform hyperbolicity, and mismatched spectral analogies—not merely historical clutter.