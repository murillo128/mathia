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
- L. Tóth, **Sums of products of Ramanujan sums**, *Annali dell'Università di Ferrara* 58 (2012), 183–197. DOI: 10.1007/s11565-011-0143-3. arXiv:1104.1906. Role: classical multiplicativity and product/correlation identities for products of Ramanujan sums; prior-art anchor for the same-index Fourier nonlinearities classified in PC-024.

## Standard Dirichlet-series identities

- Classical Euler/Ramanujan Dirichlet-series identities:
  - `sum_{n>=1} mu(n)n^{-s} = 1/zeta(s)` for `Re(s)>1`;
  - `sum_{n>=1} mu(n)^2 n^{-s} = zeta(s)/zeta(2s)` for `Re(s)>1`;
  - `sum_{n>=1} phi(n)n^{-s} = zeta(s-1)/zeta(s)` for `Re(s)>2`;
  - `sum_{n>=1} c_n(m)n^{-s} = sigma_{1-s}(m)/zeta(s)` for `Re(s)>1`.
  Role: identify the reciprocal-zeta, squarefree, and totient factors in PC-015/PC-024 as classical Möbius/Ramanujan Dirichlet-transform structure rather than new spectral data.

## Multiplicative characters, log-sine transforms, and class-number determinants

- H. L. Montgomery and R. C. Vaughan, **The Bateman–Chowla functions**, *The Ramanujan Journal* 70, article 33 (2026). DOI: 10.1007/s11139-026-01410-9. Role: explicit modern statement of the classical primitive-character formulas expressing `L(1,chi)` through Gauss sums and log-sine/weighted residue sums; prior-art anchor for the multiplicative anchored-chord spectrum in PC-025.
- Q. Yang, N. Wang and S. Kanemitsu, **Determinant expression for the class number of an abelian number field**, *Kyushu Journal of Mathematics* 77 (2023), 237–254. DOI: 10.2206/kyushujm.77.237. Role: finite-abelian-group characters and convolution maps as the basis of discrete Fourier/Dedekind determinant formulas, including the log-sine even part and cyclotomic class-number setting; prior-art anchor showing the determinant version of PC-025 is classical.

## Cyclotomic units and projective cross-ratios

- Lawrence C. Washington, **Introduction to Cyclotomic Fields**, 2nd ed., Graduate Texts in Mathematics 83, Springer (1997). DOI: 10.1007/978-1-4612-1934-7. Role: standard reference for cyclotomic/circular units, including generators built from ratios `(1-zeta^a)/(1-zeta)` and their regulator/class-number context; prior-art anchor for PC-026.
- Warren Sinnott, **On the Stickelberger ideal and the circular units of a cyclotomic field**, *Annals of Mathematics* 108 (1978), 107–134. DOI: 10.2307/1970932. Role: classical circular-unit framework and finite-index/class-number structure; supports the classification in PC-026 that prime-level cross-ratios remain inside the classical cyclotomic-unit package.

## Fuchsian covers, Selberg factorization, and modular scattering

- A. B. Venkov and P. G. Zograf, **On analogues of the Artin factorization formulas in the spectral theory of automorphic functions connected with induced representations of Fuchsian groups**, *Mathematics of the USSR-Izvestiya* 21:3 (1983), 435–443. DOI: 10.1070/IM1983v021n03ABEH001800. Role: Artin factorization of Selberg zeta functions and automorphic scattering determinants for finite-index Fuchsian subgroups; literature anchor for PC-016/PC-022/PC-023.
- K. Fedosova and A. Pohl, **Meromorphic continuation of Selberg zeta functions with twists having non-expanding cusp monodromy**, *Selecta Mathematica* 26, article 9 (2020). DOI: 10.1007/s00029-019-0534-3. Role: explicit twisted Selberg Euler product for finite-dimensional twists, including unitary characters, and modern statement/generalization of Venkov–Zograf factorization; supports the regrouping used in PC-023.
- H. Iwaniec, **Spectral Methods of Automorphic Forms**, 2nd ed., Graduate Studies in Mathematics 53, American Mathematical Society (2002). Role: standard cofinite Fuchsian spectral theory and the modular Eisenstein/scattering coefficient `sqrt(pi) Gamma(s-1/2) zeta(2s-1)/(Gamma(s) zeta(2s))`, used in PC-022 to identify the inherited Riemann-zeta-bearing channel.
- F. Diamond and J. Shurman, **A First Course in Modular Forms**, Graduate Texts in Mathematics 228, Springer (2005). Role: standard modular-curve background for `Gamma(2)`, the modular lambda coordinate, and the identification of the thrice-punctured sphere with the level-two modular curve used in PC-022.

## Fuchsian accessory parameters and Liouville/Weil-Petersson geometry

- Irwin Kra, **Accessory Parameters for Punctured Spheres**, *Transactions of the American Mathematical Society* 313:2 (1989), 589–617. DOI: 10.1090/S0002-9947-1989-0958896-0. Role: classical Fuchsian uniformizing connections and accessory parameters for punctured spheres, including their real-analytic dependence on moduli and behavior under degenerations; background for PC-017/PC-028.
- P. G. Zograf and L. A. Takhtajan, **On Liouville's equation, accessory parameters, and the geometry of Teichmüller space for Riemann surfaces of genus 0**, *Mathematics of the USSR-Sbornik* 60:1 (1988), 143–161. DOI: 10.1070/SM1988v060n01ABEH003160. Role: accessory parameters as derivatives of the classical Liouville action and the Weil-Petersson geometry of punctured spheres; primary prior-art anchor for the nonlinear uniformization direction of PC-017 and the symmetry restriction in PC-028.
- L. A. Takhtajan and P. G. Zograf, **Hyperbolic 2-spheres with conical singularities, accessory parameters and Kähler metrics on `M_{0,n}`**, *Transactions of the American Mathematical Society* 355:5 (2003), 1857–1867. DOI: 10.1090/S0002-9947-02-03243-9. arXiv:math/0112170. Role: Liouville action as a generating function for accessory parameters and Kähler-potential interpretation on moduli; supports the surviving collective Liouville/Weil-Petersson branch after PC-028.
