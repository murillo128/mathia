# MI-028 — Post-compression Fourier closure is universal; source-native coupling must occur earlier

**Evidence level:** exact-derived source-specific obstruction from [PC-312](../../findings/PC-312-mixed-conductor-periodic-packet-fails-finite-fourier-self-duality.md), strengthened by the classicalization theorem [PC-313](../../findings/PC-313-finite-fourier-pair-functional-equation-is-universal-hurwitz-duality.md).

PC-311 reduces the direct bilinear mixed-conductor Poisson pairing to one even periodic coefficient `d` of exact period `N=qr`, whose Mellin transform is a finite bundle of ordinary Dirichlet `L(s+t,chi)` functions. PC-312 then proves that the **particular coefficient forced by the canonical Prime-Circle sources** is not a finite-Fourier eigenvector: it vanishes at the nonunit residues `q,r`, while its normalized Fourier dual equals `2/sqrt(N)` there. The scalar packet therefore does not close into a source-native degree-one self-dual functional equation.

PC-313 classifies the minimal vector repair. For every even periodic coefficient, not just the Prime-Circle one, classical Hurwitz duality gives

`Lambda_d(1-s)=Lambda_(F_N d)(s)`

and hence the pair `(Lambda_d,Lambda_(F_N d))` obeys the constant swap matrix. Since `F_N^2=I` on the even subspace, the pair diagonalizes immediately into `d+F_N d` and `d-F_N d`, the universal `+` and `-` finite-Fourier eigensectors.

Thus keeping `(d,F_N d)` **after** periodic scalarization does not restore source-native structure. It merely packages a classical transform available for every even periodic sequence. The apparent matrix functional equation is not a new interaction: its matrix is source-independent and splits back into the manually symmetrized scalar sectors.

The surviving design boundary is therefore earlier than PC-312 suggested. A viable mixed-conductor mechanism must retain information not determined by the already-compressed pair `(d,F_N d)`: for example, a source-forced operation on the separate prime-level fields before cyclic diagonalization, genuinely non-circulant pointed/shell state, nonlinear coupling before scalarization, or a source-dependent matrix/operator whose action is not conjugate to the universal finite-Fourier involution. It still needs an independently justified zero-sensitive destination theorem.

**Boundary.** PC-313 does not rule out vector or operator-valued Prime-Circle structures in general. It rules out only the idea that doubling the already-compressed periodic state by adjoining its Fourier dual is itself a new source mechanism. The loss occurs before that universal closure is applied.