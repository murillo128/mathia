# Prime-lattice research notes

This directory preserves high-signal findings from the **prime-exponent / Bohr-geometry** research line so they can be reused later by Mathia, independent review, and formalization.

The intrinsic arithmetic object is the unique-factorization exponent vector

```text
n = product_p p^{v_p(n)}
v(n) = (v_2(n), v_3(n), v_5(n), ...)
```

with finite support. Multiplication becomes vector addition, primes are coordinate basis directions, and square-free integers are the finite-support vertices of the infinite `{0,1}` hypercube. The logarithmic size is the linear functional

```text
log n = sum_p v_p(n) log p.
```

Under the classical Bohr correspondence, a Dirichlet series becomes a power series in prime coordinates. The one-complex-dimensional curve relevant to ordinary Dirichlet series is

```text
s = sigma + i t  ->  z(s) = (p^{-s})_p
                     = (p^{-sigma} e^{-i t log p})_p,
```

so vertical translation is a Kronecker-type flow with frequencies `log p`.

## Research stance

The exponent-vector representation, the square-free Boolean hypercube, the Euler-product factorization, classical Möbius inversion, and the classical Bohr lift are **baseline prior art**, not Mathia discoveries. A durable finding in this branch must add a precise consequence, obstruction, boundary condition, or prior-art redirect that materially changes what a geometric or spectral RH mechanism could be.

In particular, identities that hold only in `Re(s) > 1` must not be silently promoted into statements about the critical strip. Analytic continuation is a genuine boundary in the problem, not a coordinate change that can be ignored.

## Evidence labels

- **EXACT-DERIVED** — exact consequence derived from the explicit prime-lattice/Bohr setup.
- **LITERATURE+DERIVED** — a published theorem or standard construction plus a derived consequence for this research line.
- **CLASSICAL-IDENTITY** — exact structure already present in the literature; retained when its prior-art status materially redirects the investigation.
- **NEGATIVE/OBSTRUCTION** — rules out or sharply narrows a natural mechanism.
- **DECISIVE-NEGATIVE** — decisively kills a specifically stated route under its stated hypotheses.
- **CONJECTURAL** / **NEEDS-AUDIT** — reserved for claims that remain unproved or insufficiently sourced.

These labels describe provenance and certainty, not importance.

## Files

- [`findings/`](findings/) — canonical `PL-NNN-*` finding notes and source of truth for durable research evidence.
- [`SOURCES.md`](SOURCES.md) — literature anchors used by the stored findings.
- [`graph/index.md`](graph/index.md) — derived navigation and relation view; it is not a source of mathematical truth.

The separate Mathia mind process owns `mind/` synthesis; this evidence branch does not maintain intuitions, research lines, project status, or chronological logs.

## Durable high-level picture

The investigation has established a useful separation:

```text
standard infinite-polydisk / Bohr-Hardy geometry
    -> naturally singles out Re(s) = 1/2 as the ell^2 point-evaluation boundary,
       robust across the classical H^p scale

standard H^2 reproducing kernel
    -> remains entirely in the zero-free half-plane and cannot encode nontrivial zeros by kernel orthogonality

ambient prime torus + log-prime frequencies alone
    -> too flexible: Helson twists can have radically different zero/pole and continuation behavior

bare prime Kronecker flow on Haar L^2(T^infinity)
    -> characters are exact eigenmodes with frequencies log q, q in Q_{>0}
    -> pure-point spectral type; ergodic/uniquely ergodic but not weakly mixing
    -> cannot by itself supply a decay-of-correlations or resonance mechanism for the Riemann zero divisor

Tanaka ergodic-Hardy prime-torus extension
    -> for every u>1/2, zeta/Mobius coefficient functions are outer in finite H^q on T^infinity
    -> Haar-a.e. prime-phase twist is analytic and zero-free in Re(s)>1/2
    -> typical twists occur as compact-uniform limits of vertical zeta shifts
    -> the distinguished zeta identity orbit is wholly inside the exceptional Haar-null set because of the pole at 1
    -> Haar typicality and ordinary ergodic averages therefore cannot alone decide RH; weak zeta moments require deleting a density-zero set

adelic completion of the valuation lattice (Tate)
    -> A_f^×/Zhat^× is the signed finite-support valuation lattice direct_sum_p Z; positive integer exponent vectors are its nonnegative cone
    -> log n is minus the finite idelic log-norm and is balanced exactly by the archimedean place through the global product formula
    -> additive Fourier transform on the full adele ring plus multiplicative Mellin integration sends chi to chi^vee=chi^(-1)|.|
    -> for chi=eta|.|^s with eta unitary, chi^vee=conj(chi) exactly on Re(s)=1/2, so the critical line is the unitary/Hermitian self-dual axis
    -> genuine continuation and the functional equation require this adelic/additive/archimedean structure, which is absent from the bare prime torus

Bagchi function-space dynamics
    -> RH is exactly equivalent to strong recurrence of the distinguished zeta function under vertical translation

randomized critical Bohr boundary
    -> exists rigorously as a generalized-function / Gaussian-multiplicative-chaos limit,
       but is not an ordinary function or even a local Borel measure from which pointwise zeros can be read

canonical prime-flow generator A = sum_p (log p) N_p
    -> diagonalizes the lattice exactly; exp(-sigma A) is Schatten S_q iff q sigma > 1
    -> Re(s)=1/2 is its Hilbert-Schmidt boundary, while zeta(s) is an ordinary trace only for Re(s)>1

one-particle prime operator T_s = diag(p^{-s})
    -> becomes Hilbert-Schmidt exactly for Re(s)>1/2, so the standard det_2 exists there
    -> det_2(I-T_s) = exp(-sum_{k>=2} P(k s)/k) is holomorphic and zero-free
    -> the regularization removes the k=1 prime-zeta term, the only Euler-log term that can carry zeta-zero singularities in that half-plane

canonical multiplicative Hilbert / Helson operator
    -> matrix 1/(sqrt(m n) log(m n)) couples lattice energies through E(m)+E(n)
    -> is a genuine small Hankel operator on the infinite torus with zeta kernel
    -> has no eigenvalues and spectrum [0,pi], refined to purely absolutely continuous multiplicity one
    -> its kernel samples zeta only in Re(s+w)>1; the boundary spectral singularity is the pole at 1 / Carleman kernel, not the critical zero divisor

Möbius orientation of the square-free hypercube
    -> already feeds the Nyman-Beurling / Bagchi Hardy closure program
    -> exact Möbius cancellation plus the known H^2 bridge proves the canonical approximation only for Re(s)>1;
       entering the critical strip requires genuinely stronger analytic control
```

Thus the bare prime-exponent lattice and infinite torus are not, by themselves, a zero mechanism for the Riemann zeta function. Several natural refinements are already rigorous prior art: the raw prime Kronecker rotation has a completely pure-point rational-log Koopman spectrum and no mixing; Tanaka already builds an ergodic-Hardy critical-strip extension on the prime torus but simultaneously shows that the actual zeta orbit is a Haar-null exception to its generic zero-free theory; Tate’s adelic harmonic analysis identifies the valuation lattice as only a quotient/skeleton of the finite ideles, makes `log n` the finite idelic norm coordinate balanced by the archimedean place, and gives a genuine additive-Fourier/Poisson mechanism whose unitary self-dual axis is exactly `Re(s)=1/2`; Bagchi recurrence gives an exact RH-level dynamical target for the distinguished function; Saksman–Webb give a stochastic critical boundary; the canonical `log n` generator gives a clean Schatten/trace hierarchy; standard Hilbert–Schmidt regularization of the one-particle prime determinant is zero-free and pushes zero-sensitive information into the removed prime-zeta counterterm; the canonical non-diagonal multiplicative Hilbert operator has a completely continuous Hilbert/Carleman-type spectrum despite its zeta kernel; and Möbius-weighted Hardy approximation gives a precise zero-free criterion. In every case the remaining RH difficulty is not the exponent-vector encoding or even why `1/2` is the natural symmetry axis, but additional arithmetic/analytic structure capable of forcing the deterministic Riemann zero divisor to concentrate on that axis through the critical strip.
