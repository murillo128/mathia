# WP-016 — Prime-Lattice Hodge positivity cancels out of the arithmetic supertrace

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the canonical ordinary Hodge/cohomology route on the Prime-Lattice exponent cutoff. The underlying number-theoretic complexes, their Mertens/Liouville Euler characteristics, wedge-of-spheres homotopy type, and shifted-complex Laplacian integrality are classical. The Hodge pairing argument below is standard finite-dimensional supersymmetry. The durable conclusion is project-specific: the canonical Prime-Lattice cohomology does possess an independent positive Laplacian, but the grading needed to recover its RH-sensitive arithmetic invariant cancels every positive nonzero Hodge mode, while ordinary positive traces are dominated by order-`X` harmonic mass and ordinary cup-product intersection data are trivial.

## 1. The canonical exponent cutoff really does supply a positive geometric operator

For `X>=1`, write

\[
M_X=\left\{\alpha\in\mathbb N_0^{(\mathbb P)}:\sum_p\alpha_p\log p\le\log X\right\}.
\]

Its square-free sector

\[
\Delta_X=M_X\cap\{0,1\}^{(\mathbb P)}
\]

is exactly Anders Björner's simplicial complex of square-free integers at most `X`, under `alpha=v(n)`. The full exponent down-set is likewise Björner's multicomplex of all integers at most `X`.

This is therefore not merely an analogy: Prime Lattice already has a canonical finite cochain complex. On the reduced simplicial cochains of `Delta_X`, choose any positive degreewise Hermitian inner products and form

\[
D=d+d^*,\qquad L=D^2=dd^*+d^*d.
\]

Each degree block

\[
L_k\ge0
\]

is positive semidefinite for the elementary geometric reason

\[
\langle\omega,L_k\omega\rangle
=\|d\omega\|^2+\|d^*\omega\|^2\ge0.
\]

So this route passes an important gate that many earlier candidates failed: the sign is an independent Hodge theorem and does not use RH, zeta zeros, or analytic continuation.

Björner's exact arithmetic identification is

\[
\boxed{\widetilde\chi(\Delta_X)=-M(X),}
\]

where `M(X)=sum_{n<=X} mu(n)`, and hence the classical Mertens criterion gives

\[
RH\iff M(X)=O_\varepsilon(X^{1/2+\varepsilon}).
\]

The question for this branch is therefore sharp: can the genuine positivity of `L` force the RH-sensitive alternating cancellation?

It cannot in the ordinary Hodge channel.

## 2. Every positive nonzero Hodge mode cancels from the graded arithmetic observable

Split the reduced cochain space by parity,

\[
\mathcal H=\mathcal H^+\oplus\mathcal H^-,
\]

where `+` is even degree and `-` is odd degree. The Hodge-Dirac operator `D` is odd and commutes with `L=D^2`.

Let `E_lambda^+` and `E_lambda^-` be the even and odd eigenspaces of `L` at an eigenvalue `lambda>0`. Since

\[
D^2=\lambda I
\]

on their direct sum, `D` gives an isomorphism

\[
D:E_\lambda^+\overset{\sim}{\longrightarrow}E_\lambda^-,
\qquad
D^{-1}=\lambda^{-1}D.
\]

Thus every positive eigenvalue occurs with identical even and odd multiplicity.

Consequently, for **any** scalar spectral function `F` defined on the finite spectrum,

\[
\begin{aligned}
\operatorname{Str}F(L)
&:=\operatorname{Tr}_{\mathcal H^+}F(L)
 -\operatorname{Tr}_{\mathcal H^-}F(L)\\
&=F(0)\bigl(\dim\ker L|_{\mathcal H^+}-\dim\ker L|_{\mathcal H^-}\bigr)\\
&=F(0)\,\widetilde\chi(\Delta_X)\\
&=\boxed{-F(0)M(X)}.
\end{aligned}
\]

The familiar heat identity is only one specialization:

\[
\operatorname{Str}e^{-tL}=-M(X),\qquad t>0.
\]

The same collapse holds for resolvents, completely monotone functions, spectral cutoffs, or any other degree-independent functional calculus. If `F(0)=0`, the supertrace is identically zero and loses the arithmetic invariant. If `F(0)\ne0`, the supertrace retains exactly the same Mertens cancellation, multiplied by a scalar.

This is the decisive obstruction: **the channel that knows the RH-sensitive arithmetic is precisely the channel in which all independently positive nonzero Hodge spectrum cancels identically.** The positive spectrum cannot explain the sign or size of `M(X)` because it is absent from the graded observable.

## 3. Changing the positive metric cannot repair the obstruction

A natural response is to weight the cochains geometrically, for example by the intrinsic Prime-Lattice energies `log p`, hoping that a weighted Hodge Laplacian will insert the missing arithmetic scale.

Let the degreewise inner products be changed arbitrarily while remaining positive definite. The adjoints and nonzero spectra of `L_k` may change substantially. But finite-dimensional Hodge theory still gives

\[
\ker L_k\cong\widetilde H^k(\Delta_X;\mathbb C),
\]

and the same `D`-pairing argument still matches every positive even eigenmode with an odd one. Therefore

\[
\boxed{\operatorname{Str}F(L)=-F(0)M(X)}
\]

is invariant under every such positive metric choice.

So inserting `log p`, edge lengths, conductances, or other positive weights **only through the Hodge metric** cannot convert the Mertens reformulation into a new Weil positivity mechanism. To change the graded arithmetic observable one must change something more structural: the differential/complex, introduce a non-supersymmetric insertion, couple different cutoffs, or pass to a genuinely relative/adelic object.

## 4. Ordinary positive traces are quantitatively too large

Perhaps one should forget the supertrace and use the ordinary positive trace of `F(L)` instead. Björner's Betti asymptotics show why positivity alone is then far too weak.

For the square-free complex,

\[
\sum_k\beta_k(\Delta_X)
=\frac{2X}{\pi^2}+O(X^\theta),
\qquad \theta>\frac{17}{54},
\]

and the even and odd Betti masses are separately asymptotic to `X/pi^2`.

For any nonnegative spectral function with `F(0)>0`,

\[
\operatorname{Tr}F(L)
\ge F(0)\sum_k\beta_k(\Delta_X)
=\frac{2F(0)}{\pi^2}X+o(X).
\]

Thus the most immediate positivity inequality

\[
|\operatorname{Str}F(L)|\le\operatorname{Tr}F(L)
\]

only bounds the Mertens cancellation on the natural **linear** scale. RH requires essentially the square-root scale.

The difficulty is therefore visible already in the zero modes: there are order-`X` positive-dimensional harmonic sectors of each parity, and RH asks for cancellation between their dimensions down to `X^{1/2+epsilon}`. Positivity of each sector provides no mechanism comparing the two extensive masses.

This also gives a matched-control test. The Hodge inequality and positive-mode pairing hold for any finite graded Hilbert complex, arithmetic or not. The prime-specific information enters only through the kernel dimensions. Hence the positivity theorem itself is not an arithmetic selector.

## 5. Ordinary cohomological intersection does not provide the missing sign either

Björner proves that `Delta_X` has the homotopy type of a wedge of spheres. The full multicomplex CW realization is likewise homotopy equivalent to a wedge of spheres.

For a wedge of spheres, cup products between positive-degree reduced cohomology classes vanish. Hence the canonical ordinary cohomology ring does not supply a nontrivial product pairing of the form

\[
H^k\times H^{d-k}\longrightarrow H^d\longrightarrow\mathbb C
\]

from which a Hodge-index or intersection-sign theorem analogous to the function-field proof could be extracted. Nor is `Delta_X` in general a closed oriented manifold carrying a canonical Poincare-duality fundamental class.

This matters because `WP-011` left open a global correspondence/cohomological mechanism after showing that vertical arithmetic-surface fibers lie in the intersection radical. The most literal cohomology supplied by the exponent lattice does not fill that gap: it has large homology but essentially no ordinary positive-degree cup-product intersection algebra.

This statement does **not** rule out a new relative, sheaf, adelic, persistent, twisted, or correspondence cohomology. It rules out obtaining the missing Weil-type intersection form for free from the canonical Björner complex and its ordinary cohomology.

## 6. The arithmetic observable is Mertens/Liouville, not the Weil local-to-global decomposition

There is a second structural mismatch. The canonical Euler/Hodge grading weights integer cells by

\[
\mu(n)
\]

in the square-free complex, or by `(-1)^{Omega(n)}` in the full multicomplex. The finite side of the Riemann-Weil explicit formula instead uses

\[
\frac{\Lambda(p^r)}{p^{r/2}}
\]

on every prime power, together with an archimedean gamma contribution and pole terms.

Thus the Hodge construction reaches RH through the already-known Mertens/Liouville equivalence, not through a place-matched Weil pairing. It supplies no intrinsic archimedean or polar sector, and no test-function-dependent family whose finite coefficients are the `WP-004` Mangoldt weights.

This is not a semantic distinction. The research target is a geometry whose **own positivity** explains the assembled Weil form. Here the geometry is positive, but its RH-sensitive graded invariant is merely another classical RH-equivalent cancellation problem, and the positive part of the spectrum cancels before that invariant is evaluated.

## 7. Adversarial escape tests

### Degree-dependent spectral weights

Using different functions `F_k(L_k)` in different degrees can prevent positive-mode cancellation. But that is no longer the canonical supertrace of one Hodge functional calculus. The degree dependence must itself be derived geometrically and then shown to reproduce the Mangoldt, archimedean, and pole terms. Choosing it to force those terms would be an inserted kernel.

### Analytic or Reidemeister torsion

Torsion uses degree-weighted determinants of nonzero Laplacian spectrum and therefore lies outside the `Str F(L)` collapse. It is not ruled out as an invariant. But it is a determinant/spectral package rather than a positive quadratic form, and no canonical bridge from the Björner torsion data to the Weil local-to-global coefficients is supplied here. Under this branch's gate, merely obtaining another determinant is insufficient.

### Weighted Laplacians

Positive cochain weights can change nonzero eigenvalues but not the cohomological index or the positive-mode parity cancellation. They therefore do not rescue the direct Hodge-supertrace route.

### Morse complexes and intersection numbers

Oliver Knill developed a closely related prime-divisibility Morse complex in which the Mertens function is again Euler characteristic and the Morse cohomology is equivalent to the simplicial cohomology. Stable/unstable intersection numbers define the differential, but equivalence to the same cohomology does not create a new ordinary intersection ring or a sign theorem for the Mertens cancellation.

### Cross-level or relative constructions

A complex coupling several `X`, a mapping cone, persistence module, sheaf, or adelic relative complex can evade this result because it changes the object before positivity is taken. Such a construction remains live only if its extra structure is forced by Mathia and produces both the finite Mangoldt and archimedean/global terms without importing RH.

## 8. Prior art and novelty audit

The relevant ingredients are already classical or established prior art.

- Anders Björner's 2011 paper constructs exactly the square-free divisibility complex and the all-integer multicomplex, identifies their Euler characteristics with the Mertens and summatory Liouville functions, proves the RH growth equivalence, and proves wedge-of-spheres homotopy types.
- Duval and Reiner prove that shifted simplicial complexes have integral ordinary combinatorial Laplacian spectra; Björner's square-free complex is shifted.
- Oliver Knill's 2016 `On Primes, Graphs and Cohomology` gives a closely related discrete Morse/cohomological realization of the natural numbers, again with Mertens as Euler characteristic, and explicitly discusses computing the cohomology through kernels of Hodge Laplacians while leaving deeper spectral significance speculative.
- Positive Hodge Laplacians, harmonic-representative Hodge theory, and cancellation of positive even/odd modes in a graded Hodge-Dirac complex are standard finite-dimensional mathematics.

No theorem-level novelty is claimed for these ingredients or for the abstract identity `Str F(D^2)=F(0) index(D^+)`.

The durable contribution is the **Mathia-specific no-go synthesis**: the most canonical cohomology currently intrinsic to Prime Lattice does have unconditional positivity, but the RH-sensitive arithmetic survives only as an index/Euler-characteristic cancellation after that positive spectrum has canceled, and the ordinary cohomology ring supplies no Hodge-index-like intersection form.

## 9. Falsification criterion and research consequence

This finding should be withdrawn or narrowed if any of the following fails:

1. `Delta_X` is the square-free Prime-Lattice energy cutoff and has `widetilde chi(Delta_X)=-M(X)`;
2. its ordinary Hodge Laplacian is positive and has harmonic spaces isomorphic to reduced cohomology;
3. `D` pairs the even and odd eigenspaces at every `lambda>0`;
4. therefore `Str F(L)=F(0) widetilde chi(Delta_X)` for arbitrary degree-independent spectral `F`;
5. Björner's total Betti number is order `X`, with even and odd parity masses each order `X`;
6. the wedge-of-spheres homotopy type makes all positive-degree reduced cup products vanish.

Under these exact facts, the direct route

```text
Prime-Lattice exponent complex
    -> positive ordinary Hodge Laplacian
    -> graded trace / ordinary intersection
    -> global Weil positivity
```

is closed.

The surviving cohomological target is substantially narrower: Mathia would need to force a **different global complex or correspondence** whose sign theorem is not the universal positivity of `d d^*+d^* d`, whose pairing has nontrivial arithmetic intersection content, and whose single local-to-global structure produces both the `Lambda(p^r)/sqrt(p^r)` finite terms and the archimedean/pole counterterms. Simply putting a positive Hodge metric on the canonical exponent cell complex cannot do it.

## Internal dependencies

- `research/prime_lattice/findings/PL-022-bjorner-exponent-cell-complex-hodge-obstruction.md`
- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-011-prime-lattice-whole-fibers-are-null-for-arithmetic-surface-intersection.md`
