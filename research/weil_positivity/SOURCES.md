# Weil-positivity literature anchors

This file records only durable literature dependencies for canonical findings in `research/weil_positivity/findings/`. It is not a search log.

## Classical explicit formula and positivity target

- **André Weil**, *Sur les “formules explicites” de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952), 252–265. Original explicit-formula positivity framework underlying Weil's criterion. Mathia's retained summary is [`research/prior_art/weil-positivity-criterion.md`](../prior_art/weil-positivity-criterion.md).
- **Enrico Bombieri**, *Remarks on Weil's quadratic functional in the theory of prime numbers. I*, Atti Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. 11 (2000), no. 3, 183–233. Modern treatment of Weil's quadratic functional and its positivity formulation.

## Uniformization and geometric positivity

- **Peter G. Zograf and Leon A. Takhtadzhyan**, *On Liouville's equation, accessory parameters, and the geometry of Teichmüller space for Riemann surfaces of genus 0*, Mathematics of the USSR-Sbornik 60 (1988), no. 1, 143–161. DOI: `10.1070/SM1988v060n01ABEH003160`. Constructs a Weil–Petersson potential from the hyperbolic/Liouville metric and identifies it as a generating function for the Fuchsian accessory parameters. This is the classical geometric-positivity anchor for auditing whether the PC-017 projective-connection defect can yield a Weil-type positive energy.

## Local and semilocal trace structure

- **Jean-François Burnol**, *Scattering on the p-adic field and a trace formula*, International Mathematics Research Notices 2000, no. 2, 57–70. DOI: `10.1155/S1073792800000040`; arXiv: `math/9901051`. Gives a nonarchimedean scattering model in which a nonnegative time-delay spectral function coexists with the local Weil explicit formula only after an odd/even grading, as a **supertrace**. This is a key prior-art warning against identifying each finite-place Weil contribution with an ordinary positive local energy.
- **Alain Connes and Caterina Consani**, *Weil positivity and trace formula, the archimedean place*, Selecta Mathematica (N.S.) 27 (2021), Paper 77. DOI: `10.1007/s00029-021-00689-4`; arXiv: `2006.13771`. Locates an archimedean source of positivity in a compressed scaling action on the orthogonal complement of cutoff projections; the mechanism is operator/compression based rather than a bare positive kernel equal termwise to the explicit formula.
- **Alain Connes**, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv: `2602.04022` (2026). Current survey and research perspective on restricted Weil quadratic forms and semilocal adele-class spaces. In the semilocal geometry, prime contributions are encoded by periodic orbits while the relevant positivity is a property of the assembled Weil quadratic form.

## Prime-lattice and generalized-prime controls

- **Håkan Hedenmalm, Peter Lindqvist, and Kristian Seip**, *A Hilbert space of Dirichlet series and systems of dilated functions in L²(0,1)*, Duke Mathematical Journal 86 (1997), no. 1, 1–37. DOI: `10.1215/S0012-7094-97-08601-4`; arXiv: `math/9512211`. Classical Hardy-Hilbert/Bohr realization in which square-summable Dirichlet coefficients become the `H²` geometry of the infinite prime polydisc/character space. This anchors the exponent-basis operator setup used in WP-004.
- **Harold G. Diamond, Hugh L. Montgomery, and Ulrike M. A. Vorhauer**, *Beurling primes with large oscillation*, Mathematische Annalen 334 (2006), no. 1, 1–36. DOI: `10.1007/s00208-005-0638-2`. Constructs a Beurling generalized-prime system with generalized-integer counting `N_B(x)=κx+O(x^θ)`, `1/2<θ<1`, while its zeta function has infinitely many zeros on a curve `σ=1-a/log t`. WP-004 uses this as a matched control showing that prime-exponent positivity plus a `1/2` Hilbert boundary does not force global RH/Weil positivity.
- **Szilárd Gy. Révész**, *The Carlson-type zero-density theorem for the Beurling ζ function*, Journal of the London Mathematical Society 111 (2025), no. 3, e70110. DOI: `10.1112/jlms.70110`. Records the standard Beurling generalized von Mangoldt function — `log|p|` on generalized prime powers and zero otherwise — and its logarithmic-derivative role. This is the literature anchor for the generalized-prime version of the WP-004 axis calculation.
- **Titus W. Hilberdink and Michel L. Lapidus**, *Beurling zeta functions, generalised primes, and fractal membranes*, Acta Applicandae Mathematicae 94 (2006), no. 1, 21–48. DOI: `10.1007/s10440-006-9063-0`; arXiv: `math/0410270`. Studies arbitrary generalized-prime systems and characterizes additional hypotheses under which analytic continuation and suitable generalized functional equations exist, underscoring that Euler/prime-exponent structure alone does not supply the Riemann archimedean completion.

## Global geometric comparison

- **Alain Connes, Caterina Consani, and Matilde Marcolli**, *The Weil proof and the geometry of the adeles class space*, in *Algebra, Arithmetic, and Geometry*, Vol. I, Progress in Mathematics 269, Birkhäuser (2009/2010), 339–405; arXiv: `math/0703392`. Formulates the explicit formula as a Lefschetz-type trace on a global cohomological object and makes the positivity of the resulting trace pairing the number-field analogue to be explained. This is close prior art for any proposed Mathia global quotient/cohomology/compression mechanism.
