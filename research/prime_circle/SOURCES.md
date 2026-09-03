# Prime-circle source anchors

This file records durable literature dependencies used to support or falsify findings in `research/prime_circle/`. It is an anchor list, not a search history.

## Cyclotomic resultants and discriminants

- T. M. Apostol, **Resultants of cyclotomic polynomials**, *Proceedings of the American Mathematical Society* 24 (1970), 457–462. Role: exact resultant support for PC-002/PC-004 and prime-power shell interactions.
- Standard cyclotomic discriminant formula, as used in PC-005. Role: same-shell Vandermonde/self-energy normalization on prime-power rays.

## Potential theory and GCD/Poisson kernels

- B. Gustafsson and V. G. Tkachev, **The Resultant on Compact Riemann Surfaces**, *Communications in Mathematical Physics* 286 (2009), 313–358. DOI: 10.1007/s00220-008-0622-2. arXiv:0710.2326. Role: mutual logarithmic energy as a resultant and renormalized self-energy as discriminant; key novelty correction in PC-006.
- C. Aistleitner, I. Berkes and K. Seip, **GCD sums from Poisson integrals and systems of dilated functions**, *Journal of the European Mathematical Society* 17 (2015), 1517–1546. DOI: 10.4171/JEMS/537. arXiv:1210.0741. Role: classical critical GCD kernel `gcd(m,n)/sqrt(mn)` and its Poisson structure; key novelty correction in PC-006.
- Henry J. Stephen Smith, **On the Value of a Certain Arithmetical Determinant**, *Proceedings of the London Mathematical Society* s1-7 (1875), 208–213. DOI: 10.1112/plms/s1-7.1.208. Role: classical determinant of the GCD matrix, `det(gcd(i,j))=prod phi(k)`; historical prior-art anchor for the boundary-collision GCD form in PC-056.
- Warren P. Johnson, **An LDU Factorization in Elementary Number Theory**, *Mathematics Magazine* 76:5 (2003), 392–394. DOI: 10.1080/0025570X.2003.11953215. Role: modern incidence/LDU presentation of the classical Le Paige factorization `G=L Phi L^T` for the GCD matrix; direct prior-art anchor for the exact Möbius orthogonalization and Hilbert-completion classification in PC-056.

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

## Cyclic symmetry in moduli and Weil–Petersson eigenspaces

- Pierre Lochak, **On arithmetic curves in the moduli spaces of curves**, *Journal of the Institute of Mathematics of Jussieu* 4:3 (2005), 443–508. DOI: 10.1017/S1474748005000101. Role: explicitly identifies the genus-zero roots-of-unity configuration `(0,1,zeta,...,zeta^{r-1},infinity)` as a maximal cyclic special point, gives the standard rational basis of its quadratic-differential cotangent space, diagonalizes the rotation action, and notes that the finite automorphism is an isometry for the Weil–Petersson scalar product; direct prior-art anchor for the character-mode part of PC-040.

## Hyperbolic/de Sitter duality and ideal-circle geometry

- John G. Ratcliffe, **Foundations of Hyperbolic Manifolds**, 3rd ed., Graduate Texts in Mathematics 149, Springer (2019). DOI: 10.1007/978-3-030-31597-9. Role: standard hyperbolic, inversive, Poincaré-disk, and Lorentz-model background for the intrinsic orthogonal-circle construction in PC-031.
- Immanuel Asmus, **Duality between Hyperbolic and de Sitter Geometry**, arXiv:0810.5303v2 [math.DG] (2008). Role: explicit hyperbolic/de Sitter duality in Minkowski space and de Sitter causal geometry; prior-art anchor for the Lorentz-normal formulation in PC-031.
- Maxim Arnold, Dmitry Fuchs, Ivan Izmestiev and Serge Tabachnikov, **Cross-ratio Dynamics on Ideal Polygons**, *International Mathematics Research Notices* 2022:9 (2022), 6770–6853. DOI: 10.1093/imrn/rnaa289. Role: classical projective dynamics of ideal polygons defined by cross-ratio, including the orthogonal-side case; prior-art boundary for attempts to extract a new orthogonal-circle dynamical mechanism in PC-031.
- Robert C. Penner, **The decorated Teichmüller space of punctured surfaces**, *Communications in Mathematical Physics* 113 (1987), 299–339. Role: standard decorated Teichmüller and lambda-length framework in which finite ideal-edge lengths require horocycle decorations; supports the gauge boundary in PC-031.

## Inverse-square chord spectra

- F. Calogero and A. M. Perelomov, **Some Diophantine relations involving circular functions of rational angles**, *Linear Algebra and its Applications* 25 (1979), 91–94. Role: classical spectra and trigonometric sums for finite matrices with `sin^{-2}((j-k)pi/n)` entries; primary prior-art anchor for the full regular-polygon inverse-square chord spectrum used in PC-032.

## Generalized Bernoulli special values

- J. Szmidt, J. Urbanowicz and D. Zagier, **Congruences among generalized Bernoulli numbers**, *Acta Arithmetica* 71:3 (1995), 273–278. DOI: 10.4064/aa-71-3-273-278. Role: standard generalized-Bernoulli definition and the exact identity `L(1-m,chi)=-B_{m,chi}/m`; prior-art anchor for the equivalent `L(-1,chi)` form of the pointed inverse-square character spectrum in PC-035.

## Higher even-power trigonometric sums and character weights

- N. Gauthier and P. S. Bruckman, **Sums of the even integral powers of the cosecant and secant**, *The Fibonacci Quarterly* 44:3 (2006), 263–272. DOI: 10.1080/00150517.2006.12428317. Role: differential identities and Mittag-Leffler expansions for all even powers of cosecant/secant; primary prior-art anchor for the analytic ladder used in PC-036.
- M. Beck and M. Halloran, **Finite Trigonometric Character Sums Via Discrete Fourier Analysis**, *International Journal of Number Theory* 6:1 (2010), 51–67. DOI: 10.1142/S1793042110002806. arXiv:0804.0645. Role: finite trigonometric sums weighted by Dirichlet characters as an established discrete-Fourier/class-number framework; prior-art anchor for PC-036.
- Jiahang Liu and Guoce Xin, **Root-of-unity weighted trigonometric power sums: a constant term approach**, arXiv:2607.29130 (2026). Role: current systematic formulas for root-of-unity-weighted powers of cotangent, tangent, cosecant, and secant, including all even powers; modern neighboring prior-art boundary for PC-036.

## Local spectral measures and walk-regularity

- C. D. Godsil and B. D. McKay, **Feasibility conditions for the existence of walk-regular graphs**, *Linear Algebra and its Applications* 30 (1980), 51–61. DOI: 10.1016/0024-3795(80)90180-9. Role: classical equivalence between walk-regularity and equality of vertex-deleted characteristic polynomials, with vertex-transitive graphs as examples; prior-art anchor for the flat pointed local spectral measure and derivative-cofactor mechanism in PC-038.

## Kron reduction and staged Schur elimination

- Florian Dörfler and Francesco Bullo, **Kron Reduction of Graphs With Applications to Electrical Networks**, *IEEE Transactions on Circuits and Systems I: Regular Papers* 60:1 (2013), 150–163. DOI: 10.1109/TCSI.2012.2215780. arXiv:1102.2950. Role: graph-Laplacian Kron reduction as Schur complementation, with algebraic, spectral and resistive properties; primary general prior-art anchor for the divisor-subpolygon reduction in PC-039.
- Douglas E. Crabtree and Emilie V. Haynsworth, **An identity for the Schur complement of a matrix**, *Proceedings of the American Mathematical Society* 22:2 (1969), 364–366. DOI: 10.1090/S0002-9939-1969-0255573-1. Role: classical quotient identity for staged Schur complementation; prior-art anchor for the exact refinement-path independence in PC-039.

## Weil–Petersson homothety under covering constructions

- Carlos A. Serván, **Local rigidity of covering constructions and Weil–Petersson subvarieties of the moduli space of curves**, *International Mathematics Research Notices* 2026:12 (2026). DOI: 10.1093/imrn/rnag121. arXiv:2509.25523. Role: Corollary 6.5 proves for totally marked covering constructions that pullback scales the Weil–Petersson metric by the covering degree, `f^*g_WP = deg(h) g_WP`; direct prior-art anchor for the degree homothety and normalized divisor-refinement transport in PC-041.

## Weil–Petersson curvature and Green/resolvent formulas

- Scott A. Wolpert, **Chern forms and the Riemann tensor for the moduli space of curves**, *Inventiones Mathematicae* 85 (1986), 119–145. DOI: 10.1007/BF01388794. Role: primary classical source for the Weil–Petersson Riemann tensor expressed through the hyperbolic Green/resolvent operator; analytic prior-art anchor for PC-042.
- Lin Weng, **Omega-admissible theory. II. Deligne pairings over moduli spaces of punctured Riemann surfaces**, *Mathematische Annalen* 320 (2001), 239–283. DOI: 10.1007/s002080100194. Role: Appendix explicitly extends the Wolpert curvature-tensor formula to punctured Teichmüller spaces and writes the associated spectral/resolvent decomposition; punctured-surface anchor for PC-042.

## Cotangent character coordinates, matrices, and GRH boundaries

- Kurt Girstmair, **Cotangent power sums and character coordinates**, *Integers* 25 (2025), Article A63. arXiv:2504.08330. Role: treats `i cot(pi k/n)` as a cyclotomic Galois orbit and expresses character-weighted cotangent data through character coordinates, Gauss sums, and generalized Bernoulli numbers; closest direct prior-art anchor for the fixed `L(0)` / Bernoulli content in PC-045.
- Wiktor Ejsmont and Franz Lehner, **The Trace Method for Cotangent Sums**, *Journal of Combinatorial Theory, Series A* 177 (2021), Article 105324. DOI: 10.1016/j.jcta.2020.105324. arXiv:2002.06052. Role: realizes cotangent values as spectra of finite self-adjoint matrices and derives trace/power-sum consequences, including even-zeta approximations; neighboring finite-matrix prior art for PC-045.
- Liwen Gao and Xuejun Guo, **Trigonometric determinants via special values of Dirichlet L-functions**, *Linear and Multilinear Algebra* 74:7 (2026), 916–933. DOI: 10.1080/03081087.2026.2654025. arXiv:2512.18581. Role: current spectral treatment of cotangent/tangent/cosecant/sine determinants in terms of Dirichlet `L`-values and Gauss sums; modern novelty boundary for PC-045.
- Matthias Beck, **Dedekind cotangent sums**, *Acta Arithmetica* 109:2 (2003), 109–130. DOI: 10.4064/aa109-2-1. arXiv:math/0112077. Role: generalized cotangent sums, reciprocity laws, and Petersson–Knopp identities; prior-art boundary for interpreting the prime-refinement cotangent distribution relation in PC-049 as a new scale law.
- L. Alayne Parson, **Dedekind sums and Hecke operators**, *Mathematical Proceedings of the Cambridge Philosophical Society* 88:1 (1980), 11–14. DOI: 10.1017/S0305004100057315. Role: classical Hecke-operator origin and direct treatment of Petersson–Knopp-type scale identities; prior-art boundary for interpreting the commuting prime-step actions in PC-049 as a new Hecke mechanism.
- John Lewis and Don Zagier, **Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis**, *Research in the Mathematical Sciences* 6 (2019), Article 4. DOI: 10.1007/s40687-018-0159-8. Role: proves that an asymptotic determinant property of a different cross-scale family of rational-cotangent matrices is equivalent to GRH for an odd Dirichlet `L`-series, via Gram/dilation and Beurling-type functional analysis; critical boundary showing that PC-045/PC-049 rule out only intrinsic finite-level/fiber-pushforward cotangent routes, not cotangent-based RH criteria in general.

## Hardy spaces of Dirichlet series and multiplier thresholds

- Håkan Hedenmalm, Peter Lindqvist and Kristian Seip, **A Hilbert space of Dirichlet series and systems of dilated functions in `L^2(0,1)`**, *Duke Mathematical Journal* 86:1 (1997), 1–37. DOI: 10.1215/S0012-7094-97-08601-4. Role: introduces the Hilbert space of Dirichlet series with square-summable coefficients, its infinite-polydisk/character-space model, and identifies its multiplier algebra with bounded Dirichlet-series functions on the right half-plane; primary functional-analytic prior-art anchor for the infinite Möbius-basis threshold classification in PC-055.
- Tomás Fernández Vidal, Daniel Galicer and Pablo Sevilla-Peris, **Multipliers for Hardy spaces of Dirichlet series**, *Annales de l'Institut Fourier* 75:2 (2025), 541–577. DOI: 10.5802/aif.3658. Role: modern multiplier theory for Hardy spaces of Dirichlet series, including norm and spectral properties of multiplication operators and the infinite-variable holomorphic model; neighboring prior-art context for PC-055.

## Solenoid spectral triples and proper length functions

- Carla Farsi, Therese Landry, Nadia S. Larsen and Judith A. Packer, **Spectral triples for noncommutative solenoids and a Wiener’s lemma**, *Journal of Noncommutative Geometry* 18:4 (2024), 1415–1452. DOI: 10.4171/JNCG/557. arXiv:2212.07470. Role: constructs finitely summable solenoid spectral triples from bounded-doubling/proper length functions; its explicit `\mathbb Z[1/p]` length combines archimedean absolute value with a `p`-adic size term, providing the neighboring prior-art boundary for PC-068’s conclusion that compact resolvent needs an additional arithmetic proper scale.

## Unitary time operators and additive covariance

- Daiju Funakawa, Yasumichi Matsuzawa, Itaru Sasaki, Akito Suzuki and Noriaki Teranishi, **Time operators for quantum walks**, *Letters in Mathematical Physics* 110:9 (2020), 2471–2490. DOI: 10.1007/s11005-020-01299-5. arXiv:1901.10665. Role: established unitary time-operator/strong additive commutation framework, including self-adjoint discrete-spectrum examples for discrete-time quantum walks; prior-art boundary for PC-070, whose obstruction comes from the fixed mode and infinite bilateral-orbit multiplicity of the Prime-Circle solenoid dilation rather than from additive covariance in general.

## Rational/projective heights and primitive lattice zeta

- Stephen Hoel Schanuel, **Heights in number fields**, *Bulletin de la Société Mathématique de France* 107 (1979), 433–449. DOI: 10.24033/bsmf.1905. Role: classical bounded-height counting on projective space; prior-art anchor for the standard rational/projective height used in PC-074.
- Gabriel A. Dill, **On the frequency of height values**, *Research in Number Theory* 7, article 33 (2021). DOI: 10.1007/s40993-021-00261-1. Role: explicitly notes that Euler's phi function already appears when counting rational numbers of fixed height; direct prior-art anchor for the `4 phi(n)` shell multiplicity in PC-074.
- Paul Epstein, **Zur Theorie allgemeiner Zetafunktionen**, *Mathematische Annalen* 56 (1903), 615–644. DOI: 10.1007/BF01444309. Role: classical positive-definite quadratic-form lattice zeta functions and their functional equations; prior-art anchor for the quadratic/projective-height control in PC-074.
- Werner Georg Nowak, **Primitive lattice points in rational ellipses and related arithmetic functions**, *Monatshefte für Mathematik* 106 (1988), 57–63. DOI: 10.1007/BF01501488. Role: RH-sensitive error terms for primitive lattice-point counts in quadratic regions; prior-art boundary showing that visible-lattice/projective-height RH phenomena are established arithmetic rather than a new Prime-Circle spectral mechanism.

## Hilbert and Hankel operator spectra

- Wilhelm Magnus, **On the Spectrum of Hilbert's Matrix**, *American Journal of Mathematics* 72:4 (1950), 699–704. DOI: 10.2307/2372284. Role: classical spectrum `[0,pi]` and absence of eigenvalues for the Hilbert matrix; primary spectral anchor for the universal model in PC-075.
- Marvin Rosenblum, **On the Hilbert matrix. I**, *Proceedings of the American Mathematical Society* 9:1 (1958), 137–140, and **On the Hilbert matrix. II**, *Proceedings of the American Mathematical Society* 9:4 (1958), 581–584. Role: explicit diagonalization/spectral representation of generalized Hilbert matrices and the multiplicity-one absolutely continuous channel used in PC-075.
- Alexander Pushnitski and Dmitri Yafaev, **Spectral and scattering theory of self-adjoint Hankel operators with piecewise continuous symbols**, *Journal of Operator Theory* 74:2 (2015), 417–455. DOI: 10.7900/jot.2014aug11.2052. arXiv:1408.2361. Role: multichannel Hankel scattering theory in which symbol jumps generate absolutely continuous bands; direct prior-art boundary for the oscillatory Hilbert channels isolated in PC-075.
- Noboru Ushiroya, **Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums**, *Journal of Integer Sequences* 21 (2018), Article 18.2.6. arXiv:1803.02970. Role: finite Fourier spectral analysis of Ramanujan-sum matrices; neighboring prior art for the finite channel matrix `C_n` in PC-075.
- Ole Fredrik Brevig, Karl-Mikael Perfekt, Kristian Seip, Aristomenis G. Siskakis and Dragan Vukotic, **The multiplicative Hilbert matrix**, *Advances in Mathematics* 302 (2016), 410–432. DOI: 10.1016/j.aim.2016.07.019. Role: zeta/Dirichlet-series-adjacent multiplicative Hankel operator with the same classical continuous band `[0,pi]`; novelty warning for interpreting a Hilbert/Hankel band as an RH mechanism in PC-075.
- Aurelian Gheondea and Raimund J. Ober, **A trace formula for Hankel operators**, *Proceedings of the American Mathematical Society* 127:7 (1999), 2007–2012. DOI: 10.1090/S0002-9939-99-04669-9. Role: general trace-class Hankel trace formula reducing the trace to one half of a symbol endpoint difference; neighboring prior-art anchor for PC-076's collapse of the first Hardy/Hilbert relative trace to the antipodal cyclotomic endpoint values.

## Cyclotomic conical zeta values and critical cone regularization

- Tomohide Terasoma, **Rational convex cones and cyclotomic multiple zeta values**, arXiv:math/0410306 (2004). Role: defines rational-cone zeta values with finite-order characters and proves that the absolutely convergent values lie in the cyclotomic multiple-zeta-value span; closest classical boundary for the root-of-unity cycle-cone periods in PC-082. Its absolute-convergence hypothesis is essential and does not directly cover the critical Abel traces there.
- Li Guo, Sylvie Paycha and Bin Zhang, **Conical zeta values and their double subdivision relations**, *Advances in Mathematics* 252 (2014), 343–381. DOI: 10.1016/j.aim.2013.10.022. arXiv:1301.3370. Role: conical zeta values as geometric multiple-zeta generalizations and cone-subdivision analogues of shuffle/quasi-shuffle relations; neighboring prior art for the triangle/cycle-cone organization in PC-082.
- Li Guo, Sylvie Paycha and Bin Zhang, **Renormalised conical zeta values**, arXiv:1602.04190 (2016). Role: algebraic-Birkhoff renormalization of conical zeta values at poles; novelty-warning boundary for PC-082's critical non-absolutely-convergent cone traces. PC-082 does not identify its Hardy radial/Abel prescription with this renormalization.

## Hochschild deformations and associative Nijenhuis products

- Murray Gerstenhaber, **On the deformation of rings and algebras**, *Annals of Mathematics* 79 (1964), 59–103. DOI: 10.2307/1970484. Role: classical Hochschild-cohomological deformation theory, including trivial deformations induced by changes of variables; primary prior-art anchor for PC-088's classification of the cotangent Leibniz defect as a coboundary/gauge deformation.
- José F. Cariñena, Janusz Grabowski and Giuseppe Marmo, **Quantum Bi-Hamiltonian Systems**, *International Journal of Modern Physics A* 15 (2000), 4797–4810. DOI: 10.1142/S0217751X00001954. arXiv:math-ph/0610011. Role: associative Nijenhuis operators and the derived product `N(a)b + aN(b) - N(ab)`; direct prior-art anchor for the operator-derived bilinear product tested in PC-088.
- Tomasz Brzeziński and James Papworth, **Affine Nijenhuis Operators and Hochschild Cohomology of Trusses**, *SIGMA* 19 (2023), 056. DOI: 10.3842/SIGMA.2023.056. arXiv:2303.12880. Role: modern explicit treatment of Nijenhuis products and their associativity obstruction in Hochschild-cohomological terms; supporting novelty boundary for PC-088.

## Hermite cotangent product identities

- Warren P. Johnson, **Trigonometric Identities à la Hermite**, *The American Mathematical Monthly* 117:4 (2010), 311–327. DOI: 10.4169/000298910X480784. Role: gives Hermite's arbitrary-valence product-to-sum cotangent identity and a partial-fraction derivation; direct classical prior-art anchor for the hidden-shell star reduction and finite multileg tree boundary in PC-094.

## Cyclotomic multiple polylogarithms and hyperlogarithmic reduction

- A. B. Goncharov, **Multiple polylogarithms, cyclotomy and modular complexes**, *Mathematical Research Letters* 5 (1998), 497–516. DOI: 10.4310/MRL.1998.v5.n4.a7. Role: iterated-integral continuation and special-value theory of multiple polylogarithms at roots of unity; primary period-class anchor for PC-100/PC-102.
- Jianqiang Zhao, **A Note on Colored Tornheim's Double Series**, *Integers* 10:6 (2010), 879–882. DOI: 10.1515/integ.2010.059. arXiv:0907.5106. Role: explicit reduction of colored double Tornheim series to double polylogarithm values at roots of unity; direct prior-art anchor for the weight-three `S(X,Y)` building block in PC-102.
- Erik Panzer, **Algorithms for the symbolic integration of hyperlogarithms with applications to Feynman integrals**, *Computer Physics Communications* 188 (2015), 148–166. DOI: 10.1016/j.cpc.2014.10.019. arXiv:1403.3385. Role: standard hyperlogarithmic integration and alphabet/linear-reducibility framework for rational functions times hyperlogarithms; prior-art anchor for the quartic reduction in PC-102.

## Toeplitz determinants, unitary characteristic polynomials, and Fisher–Hartwig roots

- Daniel Bump and Alex Gamburd, **On the averages of characteristic polynomials from classical groups**, *Communications in Mathematical Physics* 265:1 (2006), 227–274. DOI: 10.1007/s00220-006-1503-1. arXiv:math-ph/0502043. Role: exact unitary/classical-group averages of products and ratios of characteristic polynomials via Weyl/Littlewood identities; classical finite-section framework underlying the CUE/Christoffel kernel representation in PC-121.
- Percy Deift, Alexander Its and Igor Krasovsky, **Asymptotics of Toeplitz, Hankel, and Toeplitz+Hankel determinants with Fisher–Hartwig singularities**, *Annals of Mathematics* 174:2 (2011), 1243–1299. DOI: 10.4007/annals.2011.174.2.12. arXiv:0905.0443. Role: general Fisher–Hartwig asymptotics for root singularities on the unit circle; prior-art anchor showing that the `N^{phi(n)}/|disc Phi_n|` leading scale in PC-121 is classical Toeplitz asymptotic structure.
- Estelle L. Basor and Peter J. Forrester, **Formulas for the Evaluation of Toeplitz Determinants with Rational Generating Functions**, *Mathematische Nachrichten* 170 (1994), 5–18. DOI: 10.1002/mana.19941700102. Role: classical exact determinant formulas for rationally generated Toeplitz matrices; nearby exact-evaluation prior art for the polynomial cyclotomic symbols classified in PC-121.

## Schemmel totients and reduced-residue pair counts

- Nittiya Pabhapote and Vichian Laohakosol, **Combinatorial Aspects of the Generalized Euler's Totient**, *International Journal of Mathematics and Mathematical Sciences* 2010, Article 648165. DOI: 10.1155/2010/648165. Role: classical multiplicative Schemmel/generalized-totient counts for simultaneous coprimality; prior-art anchor for the uniform `S_2(m)=m prod_{p|m}(1-2/p)` gap-two refinement fiber in PC-148.

## Prime-pair singular-series averages and zeta zeros

- D. A. Goldston and Ade Irma Suriajaya, **A singular series average and the zeros of the Riemann zeta-function**, *Acta Arithmetica* 200 (2021), 71–90. DOI: 10.4064/aa200821-24-2. arXiv:2007.16099. Role: equation (2.2) gives exactly the Hardy--Littlewood prime-pair singular-series Dirichlet generating function used in PC-151, with meromorphic continuation through `zeta(s) zeta(s+1) / zeta(2s+2)` and explicit zero-dependent Riesz-mean residues; primary prior-art anchor showing that the zeta-zero sensitivity of the full-chord spectral Mellin displacement is inherited classical singular-series structure rather than a new Prime-Circle zero mechanism.

## Linked-cluster and forest expansions

- Abdelmalek Abdesselam and Vincent Rivasseau, **Trees, forests and jungles: a botanical garden for cluster expansions**, in *Constructive Physics*, Lecture Notes in Physics 446, Springer (1995), 7–36. DOI: 10.1007/3-540-59190-7_20. arXiv:hep-th/9409094. Role: classical Brydges--Kennedy forest interpolation and linked-cluster tree expansions; prior-art anchor for the spanning-tree majorant and connected induced-subset log-determinant clusters in PC-154.

## Bloch time-reversal symmetry

- Gianluca Panati, **Triviality of Bloch and Bloch-Dirac bundles**, *Annales Henri Poincaré* 8:5 (2007), 995–1011. DOI: 10.1007/s00023-007-0326-8. arXiv:math-ph/0601034. Role: standard periodic Bloch setting in which time-reversal symmetry pairs opposite quasimomenta; prior-art anchor for PC-159's classification of the exact `t <-> 1-t` Prime-Circle pencil symmetry as ordinary Bloch reality/time reversal rather than zeta-specific arithmetic structure.
