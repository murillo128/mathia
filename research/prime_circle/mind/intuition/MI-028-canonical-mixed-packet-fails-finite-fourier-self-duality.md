# MI-028 — The complete post-compression finite-Fourier orbit is universal, and the canonical pre-compression product classicalizes to a Mordell--Tornheim bundle

**Evidence level:** exact-derived source-specific obstruction from [PC-312](../../findings/PC-312-mixed-conductor-periodic-packet-fails-finite-fourier-self-duality.md), strengthened by the universal closure theorem [PC-313](../../findings/PC-313-finite-fourier-pair-functional-equation-is-universal-hurwitz-duality.md), the canonical even-sector zero theorem [PC-314](../../findings/PC-314-fourier-symmetrized-canonical-packet-has-off-critical-zeros.md), the orientation-complete closure [PC-315](../../findings/PC-315-oriented-fourier-orbit-eigensectors-have-off-critical-zeros.md), and the canonical nonlinear pre-compression test [PC-316](../../findings/PC-316-pointwise-cross-level-poisson-product-is-mordell-tornheim-l-bundle.md).

PC-311 reduces the direct bilinear mixed-conductor Poisson pairing to one periodic coefficient on `Z/(qr)Z`. Writing the unsymmetrized positive-frequency coefficient as `c`, its even part is `d=c+c^vee` and its orientation-odd part is `e=c-c^vee`. PC-312 proves that the canonical mixed packet is not already a finite-Fourier eigenvector.

PC-313 classifies the minimal even repair. Classical Hurwitz duality universally swaps `d` with `F_N d`, so diagonalization produces the scalar `+1` and `-1` sectors `d+F_N d` and `d-F_N d` for every even periodic coefficient. PC-314 then shows, for the canonical `(q,r)=(5,7)` source, that both sectors lie outside the exceptional `P(s)L(s,chi)` class; Saias--Weingartner therefore forces linearly many zeros in strips strictly inside `Re s>1`.

PC-315 closes the remaining orientation loophole. Since `F_N^2=-I` on odd sequences, the discarded component `e` has the forced scalar eigensectors

`b_(+i)=e-iF_N e`,  `b_(-i)=e+iF_N e`.

For the same canonical `(5,7)` packet, exact unit-class coefficient inequalities show that neither odd sector is of exceptional `P(s)L(s,chi)` form. Both therefore also have infinitely many, indeed positive-density, zeros in suitable strips with `Re s>1`. Together with PC-314, **all four scalar eigensectors `+1,-1,+i,-i` in the complete cyclic Fourier orbit `span{c,F_N c,F_N^2 c,F_N^3 c}` fail RH-like zero confinement for this canonical source**.

PC-316 tests the simplest route that really acts *before* this scalar periodicization. Take the positive-frequency Hardy components from two prime levels, multiply them pointwise, and only then propagate the product by the same Poisson semigroup. This preserves independent source indices `k,l`; the output frequency is `k+l`, and triple Mellinization gives

`Z_(q,r)^(f,g)(s,t,u)=sum_(k,l>=1) a(k)b(l)/(k^s l^t (k+l)^u)`.

So the construction genuinely escapes PC-311's diagonal `k=l` collapse. But periodicity of `a` and `b` decomposes the result into a finite bundle of classical character-weighted Mordell--Tornheim double `L`-functions. Moreover the downstream Poisson step satisfies the exact semigroup identity

`H(x,y,z)=A_(q,f)(x+z,0) B_(r,g)(y+z,0)`, 

so it is a common radial translation rather than a new interaction dynamics. The canonical coefficient-free nonlinear coupling therefore adds analytic variables and retains both indices, but **does not create a new analytic species**.

The design boundary is consequently sharper than “work before compression.” A viable Prime-Circle carrier must retain source-native information outside the complete scalar finite-Fourier orbit **and** avoid immediate reduction of its pre-compression nonlinear structure to a classical multiple-Dirichlet family whose zero theory is not source-selective. If a classical family is the correct output, the missing theorem must be stated honestly as a source-specific zero-selection property of the exact arithmetic bundle rather than inferred from the existence of several Mellin variables.

Pointed/shell-labelled state, more structured nonlinear interactions, or source-dependent matrix/operator geometry remain logically open only when their retained state is not already conjugate to the universal order-four Fourier closure or to a standard multiple-`L` construction, and when an independently justified theorem controls the relevant divisor/signature.

The reusable lesson is that analytic complexity is not automatically new information. Universal transform closure can manufacture scalar symmetries after compression; conversely a nonlinear pre-compression map can preserve more indices yet land exactly in a classical function class. In both cases the audit is the same: identify what source state survives, reduce the resulting analytic object completely, and locate the theorem that actually selects zeros.

**Boundary.** PC-314--PC-315 give a decisive canonical `(5,7)` counterexample to the post-compression scalar finite-Fourier repair. PC-316 classicalizes the canonical pointwise-product/Poisson-propagation coupling but does not prove that its particular Mordell--Tornheim bundle has bad zeros, nor classify every nonlinear mixed-prime construction. Source-dependent operators, different pre-compression nonlinearities, or a separate zero-selection theorem remain open only beyond these exact reductions.
