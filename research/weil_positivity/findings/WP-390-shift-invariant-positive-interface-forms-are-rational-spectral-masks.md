---
id: WP-390
title: Shift-invariant positive interface forms are rational spectral masks
branch: weil_positivity
status: supported
kind: ramanujan-interface-stationary-positive-form-classification
claim_strength: exact RH-independent algebraic classification of shift-invariant positive sesquilinear forms on the periodic-character span underlying WP-389; exact mixed-prime nullity is equivalent to inserting a nonnegative rational-frequency mask supported on prime-power denominators, so stationarity and positivity alone do not force the Weil selector
created: 2026-09-21
related: [WP-039, WP-373, WP-389]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence, CLUE-weil-positivity-mixed-prime-positive-completion-selector-quotient]
prior_art:
  - classical finite Fourier expansion of Ramanujan sums in primitive rational characters
  - classical diagonalization of shift-invariant Hermitian forms in a character eigenbasis
  - Ramanujan-subspace harmonic analysis as adjacent representation-level prior art
---

# WP-390 — Shift-invariant positive interface forms are rational spectral masks

## Claim

`WP-389` identifies the logarithmically normalized integer-interface current of the canonical boundary carrier as

\[
j_m(k)=\frac{c_m(k)}{\sqrt m}
=\frac1{\sqrt m}
\sum_{\substack{1\le a\le m\\(a,m)=1}}
 e^{2\pi iak/m},
\qquad m>1.
\tag{1}
\]

That finding leaves arbitrary non-Markov off-diagonal positive forms as a possible escape from the canonical mean-square Gram. The stationary part of that escape can be classified exactly.

Let

\[
V_{\rm per}:=
\operatorname{span}_{\mathbf C}
\{\chi_r:r\in\mathbf Q/\mathbf Z\},
\qquad
\chi_r(k):=e^{2\pi i r k},
\tag{2}
\]

where only finite linear combinations are allowed, and let the unit shift be

\[
(Sf)(k)=f(k+1).
\tag{3}
\]

If `B` is any Hermitian positive-semidefinite sesquilinear form on `V_per` satisfying

\[
B(Sf,Sg)=B(f,g),
\tag{4}
\]

then there is a uniquely determined arbitrary weight function

\[
w:\mathbf Q/\mathbf Z\longrightarrow [0,\infty)
\tag{5}
\]

such that

\[
\boxed{
B\!\left(\sum_r a_r\chi_r,\sum_r b_r\chi_r\right)
 =\sum_r w(r)a_r\overline{b_r}.
}
\tag{6}
\]

Consequently

\[
\boxed{
B(j_m,j_n)=0\quad(m\ne n),
\qquad
B(j_m,j_m)
 =\frac1m
 \sum_{\substack{1\le a\le m\\(a,m)=1}}
 w(a/m).
}
\tag{7}
\]

Exact nullity of every mixed-prime shell is therefore equivalent to setting `w(r)=0` at every rational frequency whose reduced denominator has at least two distinct prime factors. Conversely, every nonnegative weight supported on denominator `1` and prime-power denominators gives exact mixed-prime nullity.

Thus **every stationary positive form on this algebraic interface domain that performs the desired shell selection carries the prime-power selector explicitly in its rational-frequency weights**. Stationarity plus positivity do not derive that selector from the interface geometry.

## Exact diagonalization

For each rational character,

\[
S\chi_r=e^{2\pi i r}\chi_r.
\tag{8}
\]

Shift invariance therefore gives

\[
B(\chi_r,\chi_s)
 =B(S\chi_r,S\chi_s)
 =e^{2\pi i(r-s)}B(\chi_r,\chi_s).
\tag{9}
\]

If `r\ne s` in `Q/Z`, then the phase in (9) is not `1`, hence

\[
B(\chi_r,\chi_s)=0.
\tag{10}
\]

Positivity gives

\[
w(r):=B(\chi_r,\chi_r)\ge0,
\tag{11}
\]

and finite linearity gives (6). No continuity, closability, Markov property, or kernel representation is used.

For a primitive residue `a mod m`, the rational frequency `a/m` has reduced denominator exactly `m`. Primitive-frequency sets belonging to distinct shell indices are therefore disjoint. Substituting (1) into (6) proves (7).

Now suppose `m` has at least two distinct prime factors and exact mixed-shell nullity is required:

\[
B(j_m,j_m)=0.
\tag{12}
\]

Every summand in (7) is nonnegative, so (12) forces

\[
w(a/m)=0
\quad\text{for every }(a,m)=1.
\tag{13}
\]

Doing this for every mixed-prime `m` proves the necessity of the prime-power-denominator support condition. The converse follows immediately from (7).

## Symmetry does not remove the freedom

One may additionally require denominatorwise symmetry under multiplication by units, so that

\[
w(a/m)=\omega_m
\qquad ((a,m)=1).
\tag{14}
\]

Then

\[
\boxed{
B(j_m,j_m)=\frac{\varphi(m)}m\,\omega_m.
}
\tag{15}
\]

The sequence `omega_m>=0` is still arbitrary. Indeed, for any desired nonnegative shell-energy profile `E_m`, choosing

\[
\omega_m=\frac{m}{\varphi(m)}E_m
\tag{16}
\]

realizes `B(j_m,j_m)=E_m`. In particular, imposing Galois/unit symmetry within each primitive denominator does not derive either prime-power support or the desired prime-power magnitudes.

The canonical mean-square form of `WP-389` is the control `w(r)=1`. Equation (15) then reduces to

\[
B(j_m,j_m)=\frac{\varphi(m)}m,
\tag{17}
\]

which is strictly positive on mixed shells and, on `m=p^e`, equals `1-1/p` independently of the exponent. The canonical stationary choice therefore does not contain the Weil selector.

## Hilbert completion and a stronger regularity boundary

The obstruction is not repaired merely by passing to the canonical Besicovitch mean-square completion. In the orthonormal character coordinates, any bounded nonnegative `w` defines a bounded positive diagonal form. In particular the discontinuous mask

\[
w(r)=
\begin{cases}
1,&\text{if the reduced denominator of }r\text{ is a prime power},\\
0,&\text{if it has at least two distinct prime factors},
\end{cases}
\tag{18}
\]

is bounded and gives exact mixed-shell nullity. Hilbert-space boundedness or closedness alone therefore does not make the selector intrinsic; it merely permits the programmed spectral projection.

A substantially stronger geometric regularity does change the conclusion. If the weights in (5) are restrictions of a continuous nonnegative function `W` on the usual circle frequency space, then exact mixed-prime nullity forces `W` to vanish on all rational frequencies of mixed-prime reduced denominator. That set is dense in the circle, so continuity forces

\[
W\equiv0.
\tag{19}
\]

Hence a nonzero exact selector in the stationary interface sector must be spectrally discontinuous, or must obtain its arithmetic support from additional structure rather than ordinary continuous frequency geometry. This is the periodic-interface analogue of the continuity obstruction in `WP-373`, but it is not needed for the algebraic classification above.

## Consequence for the Weil-positivity mandate

`WP-389` showed that the first canonical interface energy classicalizes to Ramanujan orthogonality and leaves mixed shells positive. The present classification closes a larger stationary class: replacing that mean-square energy by an arbitrary positive, possibly highly nonlocal and non-Markov, **shift-invariant** form does not create a hidden geometric prime-power selector. The shift action already diagonalizes the form in rational characters, after which exact mixed-shell deletion is precisely a choice of arithmetic spectral weights.

This does not rule out the live routes identified by the current research state. A nonstationary off-diagonal form could couple rational characters before this diagonalization; a finite-`q` prelimit construction could contain structure lost in the limiting interface; and a finite--archimedean coupling could make selection or positivity emerge only after global assembly. Nor does this finding derive the linear Weil coefficients or a global sign theorem.

What it does rule out is a specific source-free move: **stationary positivity on the `WP-389` interface cannot be presented as an intrinsic explanation of prime-power support unless the rational-frequency weights themselves are independently forced by the source geometry.**

## Novelty audit

The ingredients are classical: Ramanujan's primitive-character expansion gives (1), and shift invariance diagonalizes a Hermitian form in a simple character eigenbasis. The research contribution here is the exact application to the `WP-389` boundary carrier and the resulting equivalence between mixed-prime nullity and a prime-power-denominator rational spectral mask.

This is distinct from `WP-039`, which constrains translation-invariant **Markov/Dirichlet** energies via conditionally negative-definite symbols, and from `WP-373`, which treats continuous scalar multipliers on the common prime-log line. No broad novelty claim is made for the abstract harmonic-analysis lemma itself.

A bounded prior-art audit of the classical Ramanujan/periodic harmonic-analysis surface and adjacent Ramanujan-subspace literature found the representation ingredients but no source-native Weil-positivity mechanism that forces the mask classified here. The conclusion should therefore be read as a new structural closure inside this research line, not as a claim of a new general theorem in harmonic analysis.

## Limits

- `B` is required to be shift-invariant on the periodic-character interface domain. Nonstationary forms are outside the theorem.
- Positivity may be degenerate; the proof explicitly allows zero weights.
- No topological hypothesis is needed for the algebraic classification because all vectors in `V_per` are finite sums.
- The continuity corollary concerns the ordinary circle topology and is an additional regularity assumption, not a consequence of stationarity.
- Exact mixed-shell nullity addresses arithmetic support only. It does not supply the finite Weil coefficient, the archimedean term, or global Weil positivity.
- Nothing here assumes RH or identifies zeros as a self-adjoint spectrum.
