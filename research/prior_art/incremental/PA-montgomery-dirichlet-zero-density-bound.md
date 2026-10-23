---
id: PA-montgomery-dirichlet-zero-density-bound
type: prior-art
canonical_name: Montgomery's Dirichlet zero-density bound
aliases:
  - Montgomery Theorem 12.1 zero-density estimate
kind: zero-density-bound
topics:
  - dirichlet-l-functions
  - zero-density
---

# Montgomery's Dirichlet zero-density bound

## What it is

For the nontrivial-zero count with multiplicity, the classical estimate is
\[
\sum_{\chi\bmod q}N(\sigma,T,\chi)
\ll(qT)^{3(1-\sigma)/(2-\sigma)}(\log(qT))^9,
\qquad \tfrac12\le\sigma\le\tfrac45,
\quad q\ge1,\ T\ge2.
\]
Dickinson's introduction displays this bound and attributes it to Montgomery's Theorem 12.1. At fixed modulus and fixed \(\sigma>1/2\), it gives \(o(T)\); monotonicity covers larger \(\sigma\). Martin–Ng's introduction separately records the resulting almost-everywhere nonvanishing on each fixed off-critical vertical progression.

## Relation to RH / Mathia research

[[research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss|PL-466]], equations (15)–(20), uses this sparsity twice: against a periodic mean factor's full progression of poles, then against a nonzero polynomial residue sequence left by its finite Fourier filter. The empirical variance premise is separate and unproved.

## Known scope and limits

Sublinear counting allows isolated off-critical zeros. It proves neither GRH nor PL-466's variance hypothesis. No critical-line sparsity or uniform limit as \(\sigma\downarrow1/2\) follows. Imprimitive Euler-factor zeros on \(\Re s=0\) are outside the stated application.

## Related prior art

[[research/prior_art/zero-density-method|Zero-density method]] is the broader proof-method object; this note identifies the specific quantitative theorem used by PL-466.

## Evidence and provenance

- H. L. Montgomery, *Topics in Multiplicative Number Theory*, Lecture Notes in Mathematics 227 (1971), Chapter 12, Theorem 12.1, [DOI](https://doi.org/10.1007/BFb0060851); attribution and formula checked through Dickinson's statement below.
- George Dickinson, *Zeros of Dirichlet L-functions near the critical line*, [arXiv:2211.06264v1, p. 1](https://arxiv.org/pdf/2211.06264v1), introduction immediately before Theorem 1.1. The cited Montgomery estimate is distinct from Dickinson's new theorem.
- Greg Martin and Nathan Ng, *Nonzero values of Dirichlet L-functions in vertical arithmetic progressions*, [author manuscript, p. 1](https://www.cs.uleth.ca/~nathanng/RESEARCH/NVDVAP.pdf), introduction after Theorem 1.1; [DOI](https://doi.org/10.1142/S1793042113500140).
- Persisted lookup trigger: `research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md`, Sections 3–4 and prior-art comparison, at `1c8eebb3d027d21e8a59029af8ff249b456f499d`.
