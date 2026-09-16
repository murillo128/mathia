# MI-028 — The complete post-compression finite-Fourier orbit is universal and its canonical scalar sectors need not have RH-like zeros

**Evidence level:** exact-derived source-specific obstruction from [PC-312](../../findings/PC-312-mixed-conductor-periodic-packet-fails-finite-fourier-self-duality.md), strengthened by the universal closure theorem [PC-313](../../findings/PC-313-finite-fourier-pair-functional-equation-is-universal-hurwitz-duality.md), the canonical even-sector zero theorem [PC-314](../../findings/PC-314-fourier-symmetrized-canonical-packet-has-off-critical-zeros.md), and the orientation-complete closure [PC-315](../../findings/PC-315-oriented-fourier-orbit-eigensectors-have-off-critical-zeros.md).

PC-311 reduces the direct bilinear mixed-conductor Poisson pairing to one periodic coefficient on `Z/(qr)Z`. Writing the unsymmetrized positive-frequency coefficient as `c`, its even part is `d=c+c^vee` and its orientation-odd part is `e=c-c^vee`. PC-312 proves that the canonical mixed packet is not already a finite-Fourier eigenvector.

PC-313 classifies the minimal even repair. Classical Hurwitz duality universally swaps `d` with `F_N d`, so diagonalization produces the scalar `+1` and `-1` sectors `d+F_N d` and `d-F_N d` for every even periodic coefficient. PC-314 then shows, for the canonical `(q,r)=(5,7)` source, that both sectors lie outside the exceptional `P(s)L(s,chi)` class; Saias--Weingartner therefore forces linearly many zeros in strips strictly inside `Re s>1`.

PC-315 closes the remaining orientation loophole. Since `F_N^2=-I` on odd sequences, the discarded component `e` has the forced scalar eigensectors

`b_(+i)=e-iF_N e`,  `b_(-i)=e+iF_N e`.

For the same canonical `(5,7)` packet, exact unit-class coefficient inequalities show that neither odd sector is of exceptional `P(s)L(s,chi)` form. Both therefore also have infinitely many, indeed positive-density, zeros in suitable strips with `Re s>1`. Together with PC-314, **all four scalar eigensectors `+1,-1,+i,-i` in the complete cyclic Fourier orbit `span{c,F_N c,F_N^2 c,F_N^3 c}` fail RH-like zero confinement for this canonical source**.

The surviving design boundary is consequently stronger than preserving chirality or adjoining another transform-generated component. A viable Prime-Circle carrier must retain source-native information not determined by the complete finite-Fourier orbit of the already periodicized packet, or act before that scalar periodicization, and it must provide an independently justified zero-selecting theorem. Pointed/shell-labelled state, nonlinear coupling between still-separated prime-level indices, or a genuinely source-dependent matrix/operator remain logically open only when they are not conjugate to this universal order-four Fourier closure and their divisor control is separately proved.

The reusable lesson is that an exact Riemann-type functional equation is a symmetry statement, not a zero-confinement mechanism. Universal transform closure can manufacture all parity/orientation scalar symmetries after information has already been compressed, while the actual canonical source instance can still have abundant zeros even in the half-plane of absolute convergence.

**Boundary.** PC-314--PC-315 give a decisive canonical `(5,7)` counterexample to the post-compression scalar finite-Fourier repair; they do not classify every mixed prime pair. They do not rule out pre-compression nonlinear structure, source-dependent operator geometry outside the finite-Fourier orbit, or a separate theorem that genuinely selects zeros. Nor do they say anything negative about the individual classical Dirichlet `L`-components before those components are recombined into the periodic scalar sectors.
