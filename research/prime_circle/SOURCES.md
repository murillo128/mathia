# Prime-circle source anchors

This file records durable literature dependencies used to support or falsify findings in `research/prime_circle/`. It is an anchor list, not a search history.

## Cyclotomic resultants and discriminants

- T. M. Apostol, **Resultants of cyclotomic polynomials**, *Proceedings of the American Mathematical Society* 24 (1970), 457–462. Role: exact resultant support for PC-002/PC-004 and prime-power shell interactions.
- Standard cyclotomic discriminant formula, as used in PC-005. Role: same-shell Vandermonde/self-energy normalization on prime-power rays.

## Potential theory and GCD/Poisson kernels

- B. Gustafsson and V. G. Tkachev, **The Resultant on Compact Riemann Surfaces**, *Communications in Mathematical Physics* 286 (2009), 313–358. DOI: 10.1007/s00220-008-0622-2. arXiv:0710.2326. Role: mutual logarithmic energy as a resultant and renormalized self-energy as discriminant; key novelty correction in PC-006.
- C. Aistleitner, I. Berkes and K. Seip, **GCD sums from Poisson integrals and systems of dilated functions**, *Journal of the European Mathematical Society* 17 (2015), 1517–1546. DOI: 10.4171/JEMS/537. arXiv:1210.0741. Role: classical critical GCD kernel `gcd(m,n)/sqrt(mn)` and its Poisson structure; key novelty correction in PC-006.

## Ramanujan sums and cyclotomic field transforms

- S. Ramanujan, **On certain trigonometrical sums and their applications in the theory of numbers**, *Transactions of the Cambridge Philosophical Society* 22 (1918), 259–276. Role: Ramanujan sums and the arithmetic expansions underlying Fourier decompositions of primitive-root shells.
- G. H. Hardy, **Ramanujan: Twelve Lectures on Subjects Suggested by His Life and Work**, AMS Chelsea reprint (1999). Role: classical account of Ramanujan-sum identities, including the prime-number-theorem boundary identity used in infinite cyclotomic products.
- Hartosh Singh Bal, **Constancy of an Infinite Cyclotomic Product via Ramanujan Sums**, arXiv:2511.16975v2, revised 6 January 2026; also *Integers* 25 (2025), Article A96. Role: defines the normalized cyclotomic factors `hat Phi_n`, derives their Ramanujan-sum logarithmic expansion, and proves the weighted infinite-product identity equivalent to the Dirichlet scale transform used in PC-015. The corrected v2 replaces an invalid infinite-sum interchange while preserving the stated results.

## Standard Dirichlet-series identities

- Classical Euler/Ramanujan Dirichlet-series identities:
  - `sum_{n>=1} mu(n)n^{-s} = 1/zeta(s)` for `Re(s)>1`;
  - `sum_{n>=1} phi(n)n^{-s} = zeta(s-1)/zeta(s)` for `Re(s)>2`;
  - `sum_{n>=1} c_n(m)n^{-s} = sigma_{1-s}(m)/zeta(s)` for `Re(s)>1`.
  Role: identify the reciprocal-zeta and totient factors in PC-015 as classical Möbius/Dirichlet-transform structure rather than new spectral data.

## Fuchsian covers, Selberg factorization, and modular scattering

- A. B. Venkov and P. G. Zograf, **On analogues of the Artin factorization formulas in the spectral theory of automorphic functions connected with induced representations of Fuchsian groups**, *Mathematics of the USSR-Izvestiya* 21:3 (1983), 435–443. DOI: 10.1070/IM1983v021n03ABEH001800. Role: Artin factorization of Selberg zeta functions and automorphic scattering determinants for finite-index Fuchsian subgroups; literature anchor for PC-016/PC-022.
- H. Iwaniec, **Spectral Methods of Automorphic Forms**, 2nd ed., Graduate Studies in Mathematics 53, American Mathematical Society (2002). Role: standard cofinite Fuchsian spectral theory and the modular Eisenstein/scattering coefficient `sqrt(pi) Gamma(s-1/2) zeta(2s-1)/(Gamma(s) zeta(2s))`, used in PC-022 to identify the inherited Riemann-zeta-bearing channel.
- F. Diamond and J. Shurman, **A First Course in Modular Forms**, Graduate Texts in Mathematics 228, Springer (2005). Role: standard modular-curve background for `Gamma(2)`, the modular lambda coordinate, and the identification of the thrice-punctured sphere with the level-two modular curve used in PC-022.
