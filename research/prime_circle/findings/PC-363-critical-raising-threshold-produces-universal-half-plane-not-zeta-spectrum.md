# PC-363 — critical raising threshold produces a universal half-plane, not a zeta spectrum

- **Finding ID:** `PC-363`
- **Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE`
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact critical-domain / nonnormal-spectrum classification
- **Scope:** resolves the critical `c=1` weighted-shift boundary deliberately left open by PC-362. At the first coefficient where the grade-raising perturbation is no longer subcritical relative to the canonical number operator, the natural closed extension loses the discrete grade spectrum completely and acquires an entire half-plane. The apparent `1/2` boundary is forced by the ambient `ell^2`/Hardy norm and sign convention, not by Prime-Circle arithmetic.
- **RH relevance:** high as a negative control. After a sign flip the spectral edge is exactly `Re(s)=1/2`, so this construction can superficially manufacture the Riemann critical line. The exact calculation shows why that coincidence is not an RH mechanism: every point on one side of the line is spectral, no zeta zero is selected, the operator contains no arithmetic data, and scaling or shifting the grade Hamiltonian moves the edge. A critical-line boundary obtained only from this completion/domain transition is therefore a functional-analytic wrapper rather than evidence for RH.

## Claim

PC-362 studies

\[
N e_n=n e_n,
\qquad
Q_c e_n=c(n+1)e_{n+1}
\]

on `ell^2(N_0)`, with common domain `D(N)`. It proves the grade spectrum for `0<c<1`, and shows that for `c>1` the closed operator `N+Q_c` has no eigenvectors. The borderline `c=1` was intentionally not classified.

At that critical value,

\[
H_1=N+Q_1=N(I+S)
\tag{1}
\]

on `D(N)`, where `S e_n=e_{n+1}`. The operator in (1) is closable but not closed. Its closure `A` is unitarily equivalent to the maximal first-difference operator

\[
(Bx)_n=n(x_n-x_{n-1}),
\qquad x_{-1}=0,
\tag{2}
\]

with

\[
\mathcal D(B)
=
\left\{x\in\ell^2:
(n(x_n-x_{n-1}))_{n\ge0}\in\ell^2
\right\}.
\tag{3}
\]

The exact spectrum is

\[
\boxed{
\sigma(A)=\sigma(B)=
\{\lambda\in\mathbb C:\operatorname{Re}\lambda\ge-\tfrac12\}.
}
\tag{4}
\]

Moreover,

\[
\boxed{\sigma_p(B)=\varnothing,}
\tag{5}
\]

while

\[
\boxed{
\sigma_p(B^*)=
\{\mu\in\mathbb C:\operatorname{Re}\mu>-\tfrac12\}.
}
\tag{6}
\]

Hence the open half-plane in (4) is residual spectrum and its boundary is continuous spectrum. Equivalently,

\[
\boxed{
\sigma(-A)=
\{s\in\mathbb C:\operatorname{Re}s\le\tfrac12\}.
}
\tag{7}
\]

So the critical weighted-shift repair can produce a literal spectral boundary at `Re(s)=1/2`, but it produces the **whole half-plane**, not the nontrivial zeros of `zeta`.

## 1. The critical operator is not closed on `D(N)`

Let

\[
Ue_n=(-1)^n e_n.
\]

Then `U` is unitary, commutes with `N`, and `USU=-S`. Thus

\[
U H_1 U
=
N(I-S)
=:B_0
\tag{8}
\]

on `D(N)`, with coordinate formula (2).

The criticality is already visible in the vector

\[
x_n=\frac{1}{n+1}.
\]

After the harmless alternating conjugation has been applied, `x` belongs to `ell^2` but not to `D(N)`, whereas

\[
n(x_n-x_{n-1})
=-\frac{1}{n+1}
\qquad(n\ge1)
\tag{9}
\]

belongs to `ell^2`. Smooth finite cutoffs of `x` converge to `x` both in `ell^2` and in the graph image of (2). Therefore `B_0`, and hence `H_1`, is not closed on `D(N)`.

This is exactly the domain transition that the strict relative-bound `<1` argument of PC-362 avoids.

## 2. The closure is the maximal first-difference operator

Let `B` be (2)--(3). It is closed by coordinatewise passage to limits.

It remains to show that finite sequences are a graph core. For `M>1`, choose a cutoff `chi^(M)_n` satisfying

\[
\chi_n^{(M)}=1\quad(n\le M),
\qquad
\chi_n^{(M)}=0\quad(n\ge M^2),
\]

and interpolate linearly in `log n` on `[M,M^2]`. Then

\[
\sup_n n|\chi_n^{(M)}-\chi_{n-1}^{(M)}|
\le \frac{C}{\log M}.
\tag{10}
\]

For `x in D(B)`, put `x^(M)_n=chi^(M)_n x_n`. These vectors have finite support and

\[
B(\chi^{(M)}x)_n
=
\chi_n^{(M)}(Bx)_n
+n(\chi_n^{(M)}-\chi_{n-1}^{(M)})x_{n-1}.
\tag{11}
\]

The first term converges to `Bx` by tail convergence in `ell^2`; the second has norm at most

\[
\frac{C}{\log M}\|x\|_2.
\tag{12}
\]

Therefore

\[
x^{(M)}\to x,
\qquad
Bx^{(M)}\to Bx.
\]

Since finite sequences lie in `D(N)`, this proves

\[
\boxed{\overline{B_0}=B,}
\qquad
\boxed{\overline{H_1}=U B U.}
\tag{13}
\]

The closure is forced; it is not an arbitrary spectral completion added after the fact.

## 3. A sharp numerical-range identity fixes the half-plane edge

For a finite sequence `x`, direct expansion gives

\[
2\operatorname{Re}\langle Bx,x\rangle
=
\sum_{n\ge1}n|x_n-x_{n-1}|^2
-\|x\|_2^2.
\tag{14}
\]

By the graph-core result, (14) extends to `D(B)`. Consequently

\[
\boxed{
\operatorname{Re}\langle Bx,x\rangle
\ge
-\frac12\|x\|_2^2.
}
\tag{15}
\]

For every `lambda` with

\[
\operatorname{Re}\lambda<-\frac12,
\]

one therefore has

\[
\|(B-\lambda)x\|_2
\ge
\left(-\frac12-\operatorname{Re}\lambda\right)\|x\|_2.
\tag{16}
\]

So `B-lambda` is injective with closed range. The remaining question is whether that range is all of `ell^2`.

## 4. The adjoint fills the opposite open half-plane with eigenvalues

Because finite sequences are a core, the adjoint is the maximal backward first-difference operator

\[
(B^*y)_n
=n y_n-(n+1)y_{n+1},
\tag{17}
\]

on the domain where the right-hand side belongs to `ell^2`.

Solving

\[
B^*y=\overline\lambda\,y
\]

gives

\[
y_{n+1}
=
\frac{n-\overline\lambda}{n+1}y_n.
\tag{18}
\]

For `lambda` not a nonnegative integer,

\[
y_n
=
\frac{\Gamma(n-\overline\lambda)}
{\Gamma(-\overline\lambda)\,n!}
y_0,
\tag{19}
\]

and hence

\[
|y_n|\asymp n^{-\operatorname{Re}\lambda-1}.
\tag{20}
\]

For nonnegative integral `lambda`, the recurrence terminates and gives a finite-support vector. Thus in all cases

\[
\ker(B^*-\overline\lambda)\ne0
\quad\Longleftrightarrow\quad
\operatorname{Re}\lambda>-\frac12.
\tag{21}
\]

If `Re(lambda)<-1/2`, (21) says the closed range from (16) is also dense, hence surjective. Therefore

\[
\{\operatorname{Re}\lambda<-\tfrac12\}
\subset\rho(B).
\tag{22}
\]

Conversely, (21) places every point of the opposite open half-plane in the spectrum of `B`. Since the spectrum of a closed operator is closed, its boundary line is spectral as well. This proves (4).

The same recurrence also shows that `B` itself has no eigenvalues. If `lambda != 0`, the zeroth coordinate forces `x_0=0`; for nonintegral `lambda` the recurrence then forces every coordinate to vanish, while at a positive integer `m` a newly free `x_m` produces a tail growing like `n^m` and therefore cannot lie in `ell^2`. For `lambda=0`, the recurrence gives a constant tail, again not in `ell^2`. This proves (5).

## 5. Why the `1/2` is not the Riemann critical line

Equation (7) is visually dangerous: after changing the generator sign, the boundary of the spectrum is exactly

\[
\operatorname{Re}s=\frac12.
\]

But every ingredient exposing that `1/2` is non-arithmetic:

1. the critical coefficient `c=1` is the equality point between the shift growth and the chosen number-operator normalization;
2. the exponent `1/2` comes from square summability of the universal adjoint solution `n^{-s-1}`;
3. the open half-plane, not a discrete set, is already spectrum;
4. no `Phi_n`, Ramanujan sum, von Mangoldt weight, shell resultant, old/new coupling, or other Prime-Circle datum occurs in (4);
5. multiplying the grade Hamiltonian by a positive scalar rescales the half-plane edge, and adding a scalar translates it.

Thus the line is not an invariant extracted from roots-of-unity geometry. It is the Hilbert-space growth boundary of a critical triangular completion.

In particular, the route

\[
\text{Prime-Circle all-depth signature}
\longrightarrow
\text{critical one-sided grade shift}
\longrightarrow
\text{spectral edge at }1/2
\longrightarrow
\text{RH mechanism}
\]

is closed. The third arrow is real; the fourth is not.

## 6. What survives PC-362--PC-363

The ordinary-spectrum frontier is now sharper. Subcritical strictly raising perturbations are eigenvalue-blind by PC-362. At the canonical critical model, the closed-domain limit is not a refined arithmetic spectrum but a universal half-plane. Supercritical one-sided shifts can lose point spectrum entirely, again without selecting arithmetic data.

A surviving RH-facing operator therefore needs more than tuning the growth of a one-sided raising term against the grade Hamiltonian. It must introduce a geometry-forced structure that changes the spectral set nontrivially: for example same-grade/backward/two-sided coupling, cross-level noncommutativity, a source-dependent domain condition that itself carries exact cyclotomic data, or a non-eigenvalue observable whose zeta relation survives a matched control. Merely obtaining a `1/2` boundary from the completion is now an explicit false positive.

## Prior-art and novelty audit

No novelty is claimed for the functional-analytic technology. The operator becomes, under the standard Hardy-space identification `ell^2(N_0) ~= H^2(D)` and the alternating unitary, a first-order differential operator of the classical weighted-composition-generator form

\[
Bf(z)=z(1-z)f'(z)-z f(z).
\tag{23}
\]

Generators `G f' + g f` on Hardy and related analytic-function spaces are an established theory. E. A. Gallardo-Gutiérrez, A. G. Siskakis and D. Yakubovich, **Generators of C0-semigroups of weighted composition operators**, arXiv:2110.05247 (accepted in *Israel Journal of Mathematics*), prove a general generator characterization for operators of precisely this differential form on classical Hardy spaces and neighboring spaces. Earlier composition-semigroup spectral theory goes back at least to A. G. Siskakis, **On a class of composition semigroups in Hardy spaces**, *Journal of Mathematical Analysis and Applications* 127 (1987), 122--135, DOI `10.1016/0022-247X(87)90144-2`. Current work continues to classify spectra of infinitesimal generators on Hardy/Bergman-type spaces; this is not a new operator-theory category.

The numerical-range estimate, adjoint-range argument, maximal/minimal first-difference closure, and gamma-ratio asymptotics are likewise standard functional-analysis tools. Searches around the exact bidiagonal matrix, its Hardy differential symbol, Cesàro/Hardy operators, and weighted-composition generators did not identify a source stating exactly (4) for this normalization; that absence is **not** a novelty claim.

The line-local contribution is narrower and negative: it resolves the exact critical control left by PC-362 and demonstrates that the most tempting `1/2` produced by the all-depth one-sided spectralization is universal completion geometry. It cannot by itself be evidence for the Riemann critical line.