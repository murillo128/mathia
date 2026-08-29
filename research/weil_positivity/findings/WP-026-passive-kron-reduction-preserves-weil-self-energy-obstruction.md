# WP-026 — Passive Kron reduction preserves the self-energy obstruction of the finite Weil comb

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the passive linear Schur/Kron boundary-response route left open by `WP-009`.

## Claim

`WP-009` showed that the exact Prime-Lattice weights

\[
w_n=\frac{\Lambda(n)}{\sqrt n},\qquad a_n=\log n,
\]

can be made into a positive jump energy only by adding a diagonal self-energy that the finite Weil term does not contain:

\[
W_{\rm fin}(f)
=\mathcal E_L(f)-2C_L\|f\|_2^2,
\qquad
C_L=\sum_{a_n<2L}w_n>0.
\tag{1}
\]

That finding explicitly left a **compression / Schur-complement / boundary-response** mechanism open: perhaps hidden positive bulk variables could be integrated out and geometrically generate the needed counterterm.

For ordinary passive linear networks, they cannot.

A finite resistor/Dirichlet network with nonnegative edge conductances and nonnegative shunts has a symmetric loopy Laplacian `Q`: off-diagonal entries are nonpositive and row sums are nonnegative. If the vertices are split into boundary `B` and interior `I`, its exact boundary response is the Schur complement

\[
Q_{\rm red}
=Q_{BB}-Q_{BI}Q_{II}^{-1}Q_{IB}.
\tag{2}
\]

The classical Kron-reduction closure theorem says that `Q_red` is again a symmetric loopy Laplacian. In particular, integrating out arbitrary passive interior geometry preserves the representation

\[
\boxed{
\langle y,Q_{\rm red}y\rangle
=\frac12\sum_{i\ne j}c^{\rm eff}_{ij}|y_i-y_j|^2
 +\sum_i\kappa_i^{\rm eff}|y_i|^2,
\qquad
c^{\rm eff}_{ij},\kappa_i^{\rm eff}\ge0.
}
\tag{3}
\]

For a loopless network `Q_red 1=0`; with passive shunts its row sums are the nonnegative effective shunts.

By contrast, on any finite periodic matched control carrying the same prime-power shifts, the exact finite Weil prime operator is

\[
A_W
=-\sum_{a}w_a(T_a+T_{-a}),
\tag{4}
\]

so the constant mode obeys

\[
\boxed{
A_W\mathbf1=-2C\,\mathbf1,
\qquad C=\sum_a w_a>0.
}
\tag{5}
\]

Equivalently, the passive jump Laplacian

\[
L_{\rm jump}
=\sum_aw_a(2I-T_a-T_{-a})
\tag{6}
\]

satisfies exactly

\[
\boxed{A_W=L_{\rm jump}-2CI.}
\tag{7}
\]

Equation (7) is the finite-network version of (1). The required correction is a **negative shunt / negative killing term**. Because the Schur complement of a passive loopy Laplacian remains inside the same loopy-Laplacian cone, no amount of passive hidden-variable elimination can produce that correction.

Thus the route

```text
Prime-Lattice positive prime-power conductances
    -> add passive hidden bulk / interior variables
    -> Schur or Kron reduction / resistor DtN map
    -> geometrically cancel the diagonal self-energy
    -> exact finite Weil prime form
```

is closed.

This does **not** rule out a genuinely global construction in which the archimedean sector is coupled to the prime sector before positivity is formulated, nor a relative difference of boundary responses with an independently proved order theorem. It rules out the narrower but canonical hope that ordinary passive Schur elimination itself manufactures the signed counterterm missing in `WP-009`.

## 1. Passive boundary response is closed under Schur elimination

Let `Q` be the conductance matrix of a finite connected undirected network. Write

\[
Q_{ij}=-c_{ij}\le0\quad(i\ne j),
\]

and

\[
Q_{ii}=\kappa_i+\sum_{j\ne i}c_{ij},
\qquad c_{ij}=c_{ji}\ge0,\quad\kappa_i\ge0.
\tag{8}
\]

Then

\[
Q\mathbf1=(\kappa_i)_i\ge0.
\tag{9}
\]

If the interior Dirichlet block `Q_II` is invertible, minimizing the bulk energy at fixed boundary values gives (2). Dörfler and Bullo's Lemma 2 gives the exact structural closure statement: symmetric loopy, strictly loopy, and loopless Laplacians remain in the corresponding class under Kron reduction. Their proof uses closure of symmetric `M`-matrices under Schur complement.

Consequently `Q_red` still has nonpositive off-diagonal entries and nonnegative row sums. Rewriting its entries as effective conductances and effective shunts gives (3). This is not merely positivity of the Schur complement as a matrix; it is the stronger **passivity / Markov sign structure** needed here.

The same operation is the discrete Dirichlet-to-Neumann map of a resistor network. Curtis and Morrow's classical resistor-network work is a standard boundary-response reference. No novelty is claimed for either Kron reduction or resistor DtN theory.

## 2. The finite Weil prime term lies outside the passive cone

Take a finite abelian translation group `G`, and let `T_a` denote translation by `a`. This gives a finite matched control in which the constant vector belongs to the Hilbert space and every identity can be tested without domain issues.

For a finite set of nonzero shifts with weights `w_a>0`, define the symmetric prime autocorrelation operator (4). Its quadratic form is

\[
\langle f,A_Wf\rangle
=-2\sum_aw_a\operatorname{Re}\langle f,T_af\rangle,
\tag{10}
\]

which is precisely the finite-place sign occurring in `WP-005`/`WP-009`. Since every translation fixes the constant vector,

\[
\langle\mathbf1,A_W\mathbf1\rangle
=-2C\|\mathbf1\|^2<0.
\tag{11}
\]

No loopy Laplacian can have this property: from (3),

\[
\langle\mathbf1,Q_{\rm red}\mathbf1\rangle
=\sum_i\kappa_i^{\rm eff}\ge0.
\tag{12}
\]

For a loopless reduced network the left side of (12) is exactly zero.

The Fourier-symbol version makes the same obstruction explicit. A translation-invariant passive response has symbol

\[
\psi(\chi)
=2\sum_aw_a\bigl(1-\operatorname{Re}\chi(a)\bigr)+\kappa,
\qquad\kappa\ge0,
\tag{13}
\]

whereas the finite Weil prime symbol is

\[
m_W(\chi)
=-2\sum_aw_a\operatorname{Re}\chi(a).
\tag{14}
\]

At the trivial character,

\[
\psi(1)=\kappa\ge0,
\qquad
m_W(1)=-2C<0.
\tag{15}
\]

So the obstruction survives any passive interior complexity; it is visible in the zero mode before one asks about spectra, zeros, or analytic continuation.

## 3. Prime Circle gives an intrinsic Mathia matched control

`PC-039` supplies exactly the kind of nontrivial compression that `WP-009` left open. On the fine regular polygon it starts from the canonical positive inverse-square chord Laplacian

\[
(\mathcal L_nf)_a
=\sum_{b\ne a}\frac{f_a-f_b}{|z_a-z_b|^2},
\]

and for a divisor subpolygon `P_d subset P_n` it integrates out every other vertex by the exact Schur complement

\[
K_{n\to d}
=(\mathcal L_n)_{HH}
-(\mathcal L_n)_{HI}(\mathcal L_n)_{II}^{-1}(\mathcal L_n)_{IH}.
\tag{16}
\]

`PC-039` proves a nontrivial rational harmonic-alias spectrum for this operator and exact path independence under staged divisor refinement. For the present question an even more basic fact is decisive: `mathcal L_n` is a loopless positive graph Laplacian, so by the Kron closure theorem

\[
\boxed{K_{n\to d}\mathbf1=0}
\tag{17}
\]

for every divisor reduction.

Thus this genuinely nonlocal Mathia-native boundary response cannot generate the negative constant-mode correction in (5). Its failure is not caused by the special rational alias formula of `PC-039`; it follows from passivity before that spectrum is computed.

This is a useful matched control because the geometry is substantially richer than the direct translation energy of `WP-009`: fine vertices really are integrated out and effective long-range couplings are created. Nevertheless Schur elimination does not leave the passive cone.

## 4. Why a relative subtraction is a different problem

One can of course form

\[
Q_{\rm rel}=Q_1-Q_0
\tag{18}
\]

from two positive boundary responses and arrange cancellation of row sums or self-energies. But (18) is no longer a passive-network DtN map in general. A difference of positive semidefinite loopy Laplacians need not be positive semidefinite and need not be an `M`-matrix.

This is exactly the structural issue already encountered for relative DtN/scattering in `WP-015`: subtraction can expose the arithmetic signal, but the original geometric sign theorem does not pass automatically to the relative object.

A relative escape remains legitimate only if Mathia forces an additional theorem such as

\[
Q_1\succeq Q_0
\tag{19}
\]

on the relevant test space, or supplies a grading/cohomological pairing whose sign is independently controlled. Equation (19) cannot be inferred from passive Schur reduction alone.

Similarly, one could attempt a singular infinite-volume limit in which positive self-energies diverge and are subtracted by renormalization. `WP-009` already shows that the Prime-Lattice constant `C_L` diverges with the window. Such a subtraction may define a meaningful relative object, but its canonicity and sign would be new mathematical content; it is not generated by the finite passive Kron theorem.

## 5. Matched control and novelty audit

Nothing in the obstruction uses primality. Replace the prime powers by arbitrary positive shifts `a_j` and positive conductances `w_j`. Equations (6)--(15) remain true. Therefore passive Schur/Kron positivity is **too universal** to distinguish the Riemann system from a free weighted shift system or a generalized-prime control.

The general theorem is classical:

- Florian Dörfler and Francesco Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60 (2013), no. 1, 150--163, DOI `10.1109/TCSI.2012.2215780`, arXiv: `1102.2950`. Lemma 2 proves structural closure of loopy/strictly-loopy/loopless Laplacians under Kron reduction.
- Edward B. Curtis and James A. Morrow, *The Dirichlet to Neumann Map for a Resistor Network*, SIAM Journal on Applied Mathematics 51 (1991), no. 4, 1011--1029, DOI `10.1137/0151051`. Classical discrete boundary-response framework for resistor networks.

No novelty is claimed for these results. The durable Mathia-specific consequence is the combination with `WP-009` and `PC-039`: **the most canonical positive Schur-compression mechanism cannot create the negative self-energy counterterm required to turn the exact Prime-Lattice conductances into the finite Weil prime form.**

## 6. Boundary of the no-go

This finding rules out only passive linear Schur/Kron elimination as the source of the missing sign. It does not rule out:

- a global bulk in which finite and archimedean degrees of freedom are coupled before any local-to-global decomposition is read off;
- a relative boundary response with a separately proved Loewner-order theorem;
- signed or indefinite bulk variables followed by a nontrivial positive quotient theorem;
- a grading/supertrace, cohomological, or intersection pairing outside the Markov/resistor cone;
- singular or unbounded compressions whose limit is not a finite passive Schur complement.

These are exactly the kinds of extra structures that would have to supply new mathematics rather than merely hide the subtraction in eliminated passive variables.

## 7. Exact falsification tests

The stated no-go is falsified by any one of the following:

1. a finite passive loopy Laplacian whose Schur complement has a negative row sum;
2. a passive Kron-reduced boundary form equal to (4) with some `w_a>0`;
3. a `PC-039` divisor reduction for which `K_{n->d} 1 != 0`;
4. a proof that a relative difference such as (18) inherits positivity solely from passivity, without any additional ordering hypothesis.

Items 1--3 contradict the structural closure theorem and the exact constant-mode calculation. Item 4 would supply precisely the extra sign theorem that the present finding says is absent from ordinary Kron reduction.