# MI-052 — Proper grade Hamiltonians and the canonical critical one-sided closure do not spectralize source signatures

**Evidence level:** exact synthesis from [PC-361](../../findings/PC-361-proper-grade-hamiltonians-are-spectrally-blind-to-bounded-raising-signatures.md)--[PC-363](../../findings/PC-363-critical-raising-threshold-produces-universal-half-plane-not-zeta-spectrum.md), extending the completion audit of PC-347--PC-360.

Let `H=direct_sum_(m>=0) H_m` with finite-dimensional grades, and let `H_0` be a proper diagonal grade Hamiltonian whose energies tend to infinity. PC-361 shows that if the source signature enters through a bounded operator `Q` that is strictly grade-raising, then `H_0+Q` is closed with compact resolvent but its spectrum is still exactly the diagonal grade spectrum with the same algebraic multiplicities.

PC-362 moves the same boundary into the unbounded category. If the strictly grade-raising `Q` is `H_0`-relatively bounded with relative bound below one, the graph-norm triangular structure and compact-resolvent homotopy still pin every eigenvalue and preserve its algebraic multiplicity. Thus **unbounded source amplitude is not itself a spectral discriminator** when the perturbation remains subcritical and one-sided relative to the grading.

PC-363 resolves the first critical model instead of treating the relative-bound threshold as a possible arithmetic opening. For the canonical weighted shift

`N e_n=n e_n`, `Q_1 e_n=(n+1)e_(n+1)`,

the operator on `D(N)` is closable but not closed. Its forced closure is unitarily equivalent to the maximal first-difference operator `Bx_n=n(x_n-x_(n-1))`, whose exact spectrum is

`{lambda : Re(lambda)>=-1/2}`.

It has no eigenvalues, while the adjoint fills the opposite open half-plane with eigenvalues. After a sign flip the spectral edge is exactly `Re(s)=1/2`, but this is a universal `ell^2`/Hardy summability threshold: the whole half-plane is spectral, no Prime-Circle arithmetic appears in the classification, and scaling or translating the grade Hamiltonian moves the edge.

The reusable audit is therefore stronger than “is the operator unbounded or critical?” Ask **where the source-dependent term sits relative to the grading, what closed domain/extension is actually forced at infinite depth, and which spectral object is consumed downstream**. Subcritical one-sided raising can be completely eigenvalue-blind; the canonical critical closure can change spectral category while manufacturing a nonarithmetic `1/2` boundary. Finite triangular truncations diagnose neither effect reliably.

A genuine source discriminator must defeat this one-sided triangular/completion universality. Possible categories include source-dependent boundary/domain conditions whose definition itself retains cyclotomic data, same-grade/backward/two-sided coupling, noncommuting cross-level structure, or a non-eigenvalue observable such as projection geometry or resolvent growth with an independently established zeta destination.

**Boundary.** PC-361--PC-362 prove spectral blindness under bounded or relative-bound-`<1` strictly raising hypotheses. PC-363 classifies one canonical critical weighted-shift closure, not every critical or supercritical source-dependent operator. It does not rule out arithmetic domain conditions, two-sided coupling or non-eigenvalue spectral data, and it supplies no zeta-zero theorem. Its durable role is to turn an RH-looking critical-line edge into an explicit matched nonarithmetic false positive.