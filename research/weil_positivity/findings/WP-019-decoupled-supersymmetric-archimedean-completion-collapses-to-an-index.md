# WP-019 — A decoupled supersymmetric archimedean completion collapses to an index

**Status:** `EXACT-DERIVED + CLASSICAL-INDEX-THEORY + DECISIVE-NEGATIVE`. WP-018 leaves a natural global escape: keep its exact Prime-Lattice Boolean supertrace for the finite Mangoldt selector, attach an independent positive/Hodge archimedean complex, and hope that supersymmetric positivity supplies the missing gamma/polar sector. This route fails exactly. For any genuine `Z_2`-graded Hodge/supersymmetric factor whose archimedean observable is a spectral function of its positive Laplacian, all nonzero even/odd modes cancel in supertrace. The factor contributes only an index/Euler characteristic. Consequently a decoupled tensor or direct-sum completion cannot generate the nonconstant archimedean gamma/pole distribution while retaining the WP-018 grading. Recovering the gamma factor requires breaking this cancellation through an ordinary determinant/trace, spectral asymmetry, boundary anomaly, coupling, or another non-Hodge observable; none inherits the desired positivity merely from `Delta >= 0`.

## 1. The live candidate after WP-018

For every Prime-Lattice exponent vector `alpha=v(n)`, WP-018 constructs a canonical backward Boolean cube with grading `Gamma_f` and a positive residual-energy operator

\[
R_\alpha\ge 0,
\]

such that

\[
\boxed{\operatorname{Str}_f R_\alpha
=\operatorname{Tr}(\Gamma_fR_\alpha)
=\Lambda(n).}
\tag{1}
\]

After the intrinsic critical attenuation,

\[
e^{-E(\alpha)/2}\operatorname{Str}_f R_\alpha
=\frac{\Lambda(n)}{\sqrt n}.
\tag{2}
\]

Thus the finite-prime support and normalization problem is solved exactly, but only by an alternating trace. The most economical way to try to make this global is to tensor (or add) an independent archimedean Hodge complex whose Laplacian is positive and whose spectrum is supposed to encode the infinite-place completion.

The question here is deliberately narrow and falsifiable:

> Can the same supersymmetric/Hodge cancellation that makes a positive complex geometrically natural retain the finite Mangoldt supertrace while also exposing a nontrivial archimedean spectrum?

For a decoupled factor the answer is no.

## 2. Exact cancellation theorem for a positive supersymmetric factor

Let

\[
\mathcal H_\infty=\mathcal H_\infty^+\oplus\mathcal H_\infty^-
\]

be a `Z_2`-graded Hilbert space with grading `Gamma_infty`, and let `Q_infty` be an odd self-adjoint operator,

\[
\Gamma_\infty Q_\infty=-Q_\infty\Gamma_\infty.
\]

Put

\[
\Delta_\infty=Q_\infty^2\ge0.
\]

Assume for simplicity that `Delta_infty` has discrete spectrum of finite multiplicity; the same statement holds whenever the relevant graded traces are defined. For every positive eigenvalue `lambda`,

\[
Q_\infty/\sqrt\lambda
\]

is an isomorphism between the even and odd `lambda`-eigenspaces. Hence their contributions cancel in every trace-class spectral multiplier `phi(Delta_infty)`:

\[
\operatorname{Str}_\infty \phi(\Delta_\infty)
=\phi(0)
\left(
\dim\ker\Delta_\infty|_{\mathcal H^+_\infty}
-
\dim\ker\Delta_\infty|_{\mathcal H^-_\infty}
\right).
\tag{3}
\]

Writing the bracket as `ind(Q_infty^+)`,

\[
\boxed{
\operatorname{Str}_\infty \phi(\Delta_\infty)
=\phi(0)\operatorname{ind}(Q_\infty^+).
}
\tag{4}
\]

For `phi(lambda)=e^{-t lambda}` this is the McKean--Singer/Witten-index identity

\[
\boxed{
\operatorname{Str}_\infty e^{-t\Delta_\infty}
=\operatorname{ind}(Q_\infty^+),
\qquad t>0,
}
\tag{5}
\]

so the entire positive nonzero spectrum disappears from the supertrace.

Nothing RH-specific enters this argument. It is the elementary even/odd pairing behind the classical McKean--Singer formula. The original smooth-manifold source is H. P. McKean Jr. and I. M. Singer, *Curvature and the eigenvalues of the Laplacian*, J. Differential Geometry **1** (1967), 43--69, DOI `10.4310/jdg/1214427880`. A finite combinatorial analogue is Oliver Knill, *The McKean--Singer Formula in Graph Theory*, arXiv:`1301.1408`.

## 3. Tensoring WP-018 with such a factor erases the archimedean spectrum

For a finite graded operator `A_f` and a trace-class archimedean multiplier,

\[
\operatorname{Str}_{f\widehat\otimes\infty}
\bigl(A_f\otimes\phi(\Delta_\infty)\bigr)
=
\operatorname{Str}_f(A_f)
\operatorname{Str}_\infty\phi(\Delta_\infty).
\tag{6}
\]

Taking `A_f=R_alpha` and using (1) and (4),

\[
\boxed{
\operatorname{Str}
\bigl(R_\alpha\otimes\phi(\Delta_\infty)\bigr)
=
\Lambda(n)\,\phi(0)\,\operatorname{ind}(Q_\infty^+).
}
\tag{7}
\]

The archimedean factor can therefore only:

- multiply the finite Mangoldt selector by a constant index;
- reverse it if the index is negative;
- or annihilate it if the index is zero.

It cannot produce any dependence on the positive spectrum of `Delta_infty`.

This is incompatible with the completed zeta logarithmic derivative. With

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

one has

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
+\frac{\zeta'}{\zeta}(s).
\tag{8}
\]

The infinite-place and polar contribution in (8) is a nonconstant function of `s`; in the Weil explicit formula it becomes a nontrivial archimedean/polar distribution on the test function. An index scalar cannot reproduce it.

The same obstruction applies to a decoupled direct sum of supersymmetric complexes: the supertrace is additive, but each independent Hodge spectral block contributes only its zero-mode index under a spectral multiplier. Taking more such blocks gives more constants, not the digamma/pole kernel.

## 4. Matched control: arbitrary positive spectra have the same supertrace

The information loss can be made completely explicit. Choose any sequence

\[
0<\lambda_1\le\lambda_2\le\cdots
\]

with sufficient growth for the heat operator to be trace class. Let the even space contain one zero mode `h_0` plus vectors `e_j`, let the odd space contain vectors `o_j`, and define an odd self-adjoint `Q` by pairing

\[
Qe_j=\sqrt{\lambda_j}\,o_j,
\qquad
Qo_j=\sqrt{\lambda_j}\,e_j,
\qquad
Qh_0=0.
\]

Then

\[
\operatorname{Str}e^{-tQ^2}=1
\tag{9}
\]

for every `t>0`, independently of the entire sequence `{lambda_j}`.

Thus a harmonic-oscillator-like spacing, an exponential spacing such as `lambda_j=2^j`, and an arbitrarily perturbed paired spectrum are **matched controls** for the proposed supersymmetric completion: the positive Hodge supertrace cannot distinguish them.

That is fatal for an argument in which the actual archimedean spectral spacing is supposed to force the `Gamma` factor. The sign theorem has erased precisely the data that would have to distinguish the correct infinite place from a fake one.

## 5. The gamma factor is visible to an ordinary determinant, not to the Hodge supertrace

There is a useful control showing that the missing information is real rather than nonexistent. For the one-sided number operator

\[
N_a e_m=(m+a)e_m,
\qquad m=0,1,2,\ldots,
\]

its spectral zeta function is the Hurwitz zeta function

\[
\zeta_{N_a}(z)=\sum_{m\ge0}(m+a)^{-z}=\zeta(z,a).
\]

The classical identity

\[
\zeta'(0,a)=\log\Gamma(a)-\frac12\log(2\pi)
\tag{10}
\]

therefore gives

\[
\log\det_\zeta N_a
=-\log\Gamma(a)+\frac12\log(2\pi).
\tag{11}
\]

So an oscillator/number-operator spectrum can indeed encode `Gamma`. Equation (10) is formula 25.11.18 of the NIST Digital Library of Mathematical Functions.

But if the same positive spectrum is placed in a genuine supersymmetric pair, its nonzero even and odd levels cancel from the **supertrace** by (3). Conversely, if one uses the ordinary trace or ordinary zeta determinant so that the spectrum survives, the WP-018 finite selector is still an alternating supertrace. A mixed functional such as

\[
\operatorname{Str}_f\otimes\operatorname{Tr}_\infty
\tag{12}
\]

is not a positive functional on positive operators, because the first factor is not positive. Already on a one-edge Boolean cube, a positive diagonal matrix `diag(a,b)` has supertrace `a-b` of either sign.

Thus the two required jobs pull in opposite directions in the decoupled construction:

```text
finite Prime-Lattice selector:
    needs grading / cancellation -> sees Lambda(n)

archimedean Gamma spectrum:
    needs nonzero spectral levels -> ordinary trace/determinant sees them

supersymmetric Hodge supertrace:
    cancels those nonzero archimedean levels -> only index remains
```

## 6. Prior art and novelty audit

No index-theoretic novelty is claimed. The cancellation in (3)--(5) is the classical McKean--Singer/Witten-index mechanism, and the Hurwitz-zeta/Gamma identity in (10) is classical.

The Mathia-specific result is the incompatibility with the exact finite selector of WP-018. That finding makes a decoupled supersymmetric completion unusually tempting because both sides appear to admit positive spectral/Hodge operators. The exact calculation above shows that **the grading that exposes `Lambda` cannot simply be extended by an independent positive supersymmetric infinite-place factor and still retain its nonzero spectrum.**

This does not supersede the established cohomological/trace-formula prior art. Connes--Consani's archimedean Weil-positivity mechanism uses compression of the scaling action rather than a bare Hodge supertrace, and Connes--Consani--Marcolli use a global cohomological/quotient construction. Deninger-style determinant/Lefschetz programs likewise retain dynamical spectral data through regularized determinants and flow actions. Those are outside the no-go precisely because they are not a decoupled spectral function of a positive supersymmetric Laplacian.

## 7. Boundary of the obstruction

This finding rules out the following specific family:

\[
\boxed{
\text{WP-018 Boolean grading}
\;\widehat\otimes\;
\text{independent positive Hodge/supersymmetric archimedean factor}
\;\xrightarrow{\operatorname{Str}}\;
\text{global Weil completion}.
}
\]

It does **not** rule out:

- a genuinely coupled finite/archimedean differential or superconnection;
- boundary conditions whose eta/spectral-asymmetry term survives supersymmetric pairing;
- a relative determinant or anomaly forced canonically by the geometry;
- a noncommutative compression or quotient such as the established adelic prior art;
- an intersection/cohomological pairing whose positivity theorem is not merely `Delta>=0` plus supertrace;
- an archimedean operator that is not a spectral function of the supersymmetric Laplacian.

These escapes are real, but each must supply a new sign theorem. Once the construction intentionally prevents the supersymmetric cancellation in (3), positivity no longer follows from the ordinary Hodge statement alone.

## 8. Falsification and audit tests

Withdraw or narrow this finding if any of the following fails:

1. for every positive eigenvalue of `Delta=Q^2`, the odd operator `Q/sqrt(lambda)` pairs the even and odd eigenspaces;
2. therefore (3) holds for every spectral multiplier whose graded trace exists;
3. tensor-product supertrace factorizes as in (6);
4. applying (3) to WP-018 gives (7), so all positive archimedean eigenvalues disappear;
5. the completed zeta logarithmic derivative has the nonconstant gamma/polar term in (8);
6. a one-sided arithmetic spectrum retains `Gamma` through the ordinary zeta determinant by (10)--(11);
7. replacing the finite supertrace by an ordinary positive trace destroys the exact Mangoldt selector, as proved already in WP-018.

Items 1--7 are exact and independent of RH. The only scope condition is structural: the archimedean completion is decoupled and its claimed sign comes from an ordinary supersymmetric/Hodge positive Laplacian.

## 9. Consequence for the research line

WP-018 remains a useful exact finite-place construction, but its most straightforward cohomological completion is now closed. The surviving global route must do more than tensor a Boolean Möbius grading with an independent archimedean Hodge theory.

A successful Mathia-native mechanism must make the **same coupled object** do three jobs without circularity:

1. retain the local incidence cancellation that normalizes every `p^k` to `log p`;
2. retain nonzero infinite-place spectral data strongly enough to generate the gamma and polar terms;
3. derive final nonnegativity from a theorem stronger than the universal supersymmetric cancellation that would otherwise erase those data.

This points specifically toward coupled boundary/cohomological, relative/anomalous, compression, or intersection mechanisms rather than a product of independently positive local complexes.

## Internal dependencies

- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-008-tate-adelic-fourier-self-duality-is-indefinite.md`
- `research/weil_positivity/findings/WP-012-prime-lattice-frobenius-shifts-are-fixed-point-free-bost-connes-skeleton.md`
- `research/weil_positivity/findings/WP-015-prime-flute-dtn-positivity-does-not-survive-critical-scattering-continuation.md`
