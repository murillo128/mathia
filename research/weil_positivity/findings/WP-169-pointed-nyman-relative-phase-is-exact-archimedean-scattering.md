# WP-169 — Pointed/Nyman relative phase is exactly the archimedean scattering factor, but its sign is not Gram positivity

**Status:** `EXACT-DERIVED + ARCHIMEDEAN-PHASE-BRIDGE + POSITIVE-MATRIX-GRAM + FUNCTIONAL-EQUATION + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + MATCHED-CONTROLS`.

`WP-168` identifies the critical pointed-Dirichlet shell limit with a stationary positive Gram kernel whose spectral density is

\[
\frac{|\zeta(\tfrac12+i\tau)|^2}{\tfrac14+\tau^2}.
\]

That scalar Gram loses the phase of `zeta`, and `WP-168` therefore concludes correctly that the Gram itself does not generate the Gamma/polar part of the Weil explicit formula. There is, however, a sharper statement about the **phase that was discarded**.

Let

\[
a(x)=H_{\lfloor x\rfloor}-\log x-\gamma,
\qquad
h(x)=\{1/x\},
\]

and put

\[
b(y)=e^{y/2}a(e^y),
\qquad
c(y)=e^{y/2}h(e^y).
\tag{1}
\]

Here `b` is the Mathia-native scaling profile derived in `WP-168`, while `c` is the classical Nyman--Müntz fractional-part control used there to identify the same scalar autocorrelation. Their Mellin transforms give, with the Fourier convention of `WP-168`,

\[
\widehat b(\tau)
=-\frac{\zeta(\tfrac12+i\tau)}{\tfrac12-i\tau},
\qquad
\widehat c(\tau)
=-\frac{\zeta(\tfrac12-i\tau)}{\tfrac12-i\tau}.
\tag{2}
\]

The Riemann functional equation therefore gives the **exact relative phase**

\[
\boxed{
\widehat b(\tau)=R_\infty(\tau)\widehat c(\tau),
}
\tag{3}
\]

where

\[
\boxed{
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})},
\qquad |R_\infty(\tau)|=1.
}
\tag{4}
\]

Thus the two spectral factors with the same modulus are not related by an arbitrary phase: for this canonical Nyman comparator their phase difference is exactly the real-place Gamma/scattering factor. If `S_\infty` denotes the Fourier multiplier with symbol `R_\infty`, then

\[
\boxed{b=S_\infty c}
\tag{5}
\]

and `S_infty` is unitary on `L^2(R)`.

More strongly, the logarithmic derivative of this phase is **exactly the nonconstant archimedean Weil symbol in the normalization already used in `WP-005`**:

\[
\boxed{
i\,\frac{d}{d\tau}\log R_\infty(\tau)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{i\tau}{2}\right)-\log\pi.
}
\tag{6}
\]

So the Gamma/digamma profile that appeared structurally but without a sign theorem in `WP-074` reappears here in a second, independent way: it is the phase velocity between the Mathia pointed-shell scaling factor and the Nyman fractional-part factor.

This is a genuine structural bridge, but it is **not** the sought Weil positivity mechanism. The bridge classicalizes to the standard real-place Fourier/co-Poisson scattering factor, and extracting (6) from the unitary phase is a signed logarithmic-derivative operation, not a consequence of positivity. The scalar Gram in `WP-168` still sees only `|zeta|^2`; the positive two-channel Gram of `(b,c)` is rank one at every frequency and is positive for the tautological reason that it is an outer product. No Gamma phase, finite-prime term, or polar term is forced by that positivity.

The result therefore sharpens the frontier rather than solving it:

\[
\boxed{
\text{Mathia pointed half-density}
\;\xrightarrow{\text{relative phase vs. Nyman control}}\;
\text{exact real-place scattering/Gamma factor},
}
\]

but

\[
\boxed{
\text{positive Gram data}
\not\Rightarrow
\text{canonical selection of that phase or Weil sign}.
}
\]

A successful continuation must make an equivalent phase/boundary operator intrinsic to the **same source geometry** that carries the finite arithmetic data, before positive scalarization. Merely recognizing the Gamma factor after choosing the classical Nyman spectral factor does not meet that gate.

## 1. Exact phase quotient

`WP-168` proves, for `0<Re(s)<1`,

\[
A(s):=\int_0^\infty a(x)x^{s-1}\,dx
=-\frac{\zeta(1-s)}{s},
\tag{7}
\]

while the classical fractional-part identity is

\[
H(s):=\int_0^\infty h(x)x^{s-1}\,dx
=-\frac{\zeta(s)}{s}.
\tag{8}
\]

Since the half-density change of variables `x=e^y` sends the critical Mellin line to ordinary Fourier transform, taking

\[
s=\frac12-i\tau
\tag{9}
\]

gives (2).

The symmetric functional equation

\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)
=
\pi^{-(1-s)/2}\Gamma((1-s)/2)\zeta(1-s)
\tag{10}
\]

implies

\[
\frac{\zeta(1-s)}{\zeta(s)}
=
\pi^{1/2-s}
\frac{\Gamma(s/2)}{\Gamma((1-s)/2)}.
\tag{11}
\]

Equation (11) is an identity of meromorphic functions, so no division-by-zero assumption is needed: the quotient on the left extends through zeta zeros by the Gamma expression on the right. Substituting (9) gives exactly (4).

Because the numerator and denominator Gamma values in (4) are complex conjugates and `|pi^(i tau)|=1`,

\[
|R_\infty(\tau)|=1
\tag{12}
\]

for every real `tau`. Hence `S_infty` is a unitary translation-invariant operator and (5) follows from Plancherel.

No Riemann-hypothesis assumption or zero data enter this derivation.

## 2. The archimedean digamma symbol is the phase velocity

Differentiate (4):

\[
\frac{d}{d\tau}\log R_\infty(\tau)
=
i\log\pi
-\frac{i}{2}\psi\!\left(\frac14-\frac{i\tau}{2}\right)
-\frac{i}{2}\psi\!\left(\frac14+\frac{i\tau}{2}\right).
\tag{13}
\]

For real `tau`, the two digamma values are conjugates. Therefore

\[
\frac{d}{d\tau}\log R_\infty(\tau)
=i\left[
\log\pi
-
\operatorname{Re}\psi\!\left(\frac14+\frac{i\tau}{2}\right)
\right],
\tag{14}
\]

which proves (6).

The right side of (6) is exactly the nonconstant archimedean multiplier displayed in `WP-005` for the centered Riemann explicit formula. This is not merely the statement that a Gamma function appears somewhere in the construction: the **same frequency-dependent function** is recovered with its normalization and sign from the derivative of the relative phase.

There is also a useful internal control. `WP-074` derives the Riemann digamma shape from a relative resolvent of the independently forced half-integer Hardy number operator `L=N+1/2`. The present derivation reaches the same profile from the critical shell scaling limit. The agreement is evidence that the half-density geometry is consistently touching the real-place functional-equation structure. It is not evidence of a new positivity theorem, because both readouts remain signed relative responses.

## 3. Why the positive two-channel Gram still does not give the sign

Consider the stationary matrix Gram of the pair `(b,c)`,

\[
K_{ij}(t)=\langle f_i,f_j(\cdot-t)\rangle,
\qquad (f_1,f_2)=(b,c).
\tag{15}
\]

Using `bhat=R_infty chat`, its spectral density is, up to the Fourier normalization,

\[
\boxed{
\frac{|\zeta(\tfrac12-i\tau)|^2}{\tfrac14+\tau^2}
\begin{pmatrix}
1 & \overline{R_\infty(\tau)}\\
R_\infty(\tau) & 1
\end{pmatrix}.
}
\tag{16}
\]

The matrix in (16) has eigenvalues `0` and `2` for every `tau`. Its positivity is therefore automatic and its determinant vanishes identically. For any fixed coefficients `alpha,beta`, the positive scalar compression has density

\[
\frac{|\zeta(\tfrac12-i\tau)|^2}{\tfrac14+\tau^2}
\left|\alpha R_\infty(\tau)+\beta\right|^2
\ge0.
\tag{17}
\]

Equation (17) can display the Gamma phase inside a modulus square, but it cannot turn the signed function (6) into a positivity consequence. To extract (6) one differentiates a phase logarithm. That operation is neither a positive compression nor a positive quadratic readout.

Moreover every measure in (16)--(17) remains absolutely continuous. Thus this finite channel augmentation stays inside the same-space multiplier class whose spectral-type mismatch with an exact positive Weil realization is already recorded in `WP-005` and in the Shoeib--Torky multiplier obstruction. The new phase identification does not escape that no-go.

## 4. Phase-gauge falsification: the Gram does not select `R_infty`

The strongest adversarial control is that the scalar Gram of `WP-168` cannot determine the phase used above.

Let `theta(tau)` be any measurable real function and define another spectral factor by

\[
\widehat c_\theta(\tau)
=e^{i\theta(\tau)}\widehat c(\tau).
\tag{18}
\]

Then

\[
|\widehat c_\theta(\tau)|=|\widehat c(\tau)|=|\widehat b(\tau)|,
\tag{19}
\]

so `c_theta` has **exactly the same stationary autocorrelation** as `c` and `b`. But its relative phase to `b` is

\[
R_\infty(\tau)e^{-i\theta(\tau)},
\tag{20}
\]

whose logarithmic derivative can be changed arbitrarily by `theta'` whenever that derivative is meaningful.

Therefore the Gamma phase in (4) is not selected by the positive Gram kernel. It is selected only after one makes the additional choice of the classical fractional-part/Nyman spectral factor `c`, whose Mellin transform is (8). This is precisely the distinction required by the branch mandate: a comparator that reveals the known archimedean factor is not yet an intrinsic geometric structure that **forces** it.

This control also explains why `WP-168` and the present finding are compatible. `WP-168` says the scalar Gram produces no Gamma term; the present result says the Gamma factor lives in a relative spectral phase that the scalar Gram has erased.

## 5. All-degree control and absence of finite--archimedean incidence

The Mathia profile `b` was obtained in `WP-168` from the full-root controls

\[
F_N(z)=\log\frac{1-z^N}{1-z}
\tag{21}
\]

for arbitrary degrees `N`, not only primes or prime powers. The phase relation (3)--(6) is derived after taking that same all-degree scaling limit. Consequently the Gamma/scattering factor appears **before** any use of Mangoldt support.

This kills the tempting interpretation that (6) is already the sought finite--archimedean coupling. It is a real-place phase relation attached to the universal coefficient-lattice scaling profile. It does not distinguish the prime specialization from the matched composite controls, it does not generate the finite Mangoldt comb, and it produces no polar finite-rank term.

Thus the current accepted finite--archimedean-incidence clue remains open. What this finding adds is a sharper discriminator: seeing the exact Gamma factor is not enough. A candidate must show why the same source geometry that retains the **signed finite arithmetic selector** canonically chooses and couples to the real-place phase, rather than obtaining the latter from a separate Nyman/Fourier comparator.

## 6. Prior art and novelty audit

No novelty is claimed for the Riemann functional equation, its Gamma factor, or its interpretation as a scale-invariant Fourier scattering multiplier.

- Riemann's functional equation gives (10)--(11); Tate's thesis places such local Gamma factors inside the adelic Fourier-functional-equation framework.
- Jean-François Burnol, *On Fourier and Zeta(s)*, Forum Mathematicum 16 (2004), 789--840, DOI `10.1515/form.2004.16.6.789`, studies the Fourier/zeta interaction and identifies the functional-equation `chi(s)` as the Mellin spectral multiplier of the scale-invariant Fourier transform. With the orientation used here, `R_infty` is the inverse of that standard `chi` factor on the critical line.
- Jean-François Burnol, *Entrelacement de co-Poisson*, Annales de l'Institut Fourier 57 (2007), no. 2, 525--602, DOI `10.5802/aif.2268`, develops the co-Poisson intertwining viewpoint for precisely these Fourier/L-function functional equations.
- The same-space positive-multiplier obstruction relevant to Section 3 is already recorded in `WP-005` and `research/weil_positivity/SOURCES.md`; no new general multiplier theorem is claimed here.

The Mathia-specific content is the exact identification

\[
\text{WP-168 native profile }b
\quad = \quad
\text{real-place scattering unitary}
\;\times\;
\text{Nyman fractional-part profile }c,
\tag{22}
\]

followed by the observation that the archimedean Weil digamma symbol is its phase velocity (6), together with the phase-gauge and all-degree controls showing why this does not yet supply intrinsic Weil positivity.

This is a **prior-art classicalization with a new local bridge**, not a claim that Mathia has discovered the functional equation or its scattering interpretation.

## Dependencies

- `research/weil_positivity/findings/WP-005-prime-lattice-axis-positivity-does-not-survive-weil-autocorrelation-lift.md`
- `research/weil_positivity/findings/WP-010-nyman-totality-projection-positivity-is-tautological.md`
- `research/weil_positivity/findings/WP-074-pointed-cover-inverse-scale-defect-has-positive-log-degree-trace-but-poisson-weil-lift-is-indefinite.md`
- `research/weil_positivity/findings/WP-168-critical-pointed-dirichlet-scaling-limit-is-a-nyman-mellin-gram-kernel.md`
- `research/weil_positivity/SOURCES.md` — Tate, Nyman--Beurling, and same-space multiplier anchors.

## Bottom line

The phase discarded by the `WP-168` positive Gram is mathematically meaningful. Relative to the canonical Nyman fractional-part factor, it is exactly

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(1/4-i\tau/2)}{\Gamma(1/4+i\tau/2)},
\]

and its logarithmic phase derivative is exactly the Riemann archimedean digamma multiplier. This is the cleanest finite-to-archimedean structural contact yet exposed by the critical pointed-shell scaling route.

But the contact does not pass the research mandate's sign gate. The Nyman factor is an additional classical spectral-factor choice not selected by the positive Gram; the two-channel Gram remains a tautological rank-one modulus-square object; the logarithmic derivative that produces the archimedean term is signed; the same construction occurs for all degrees; and no polar or finite-prime coupling is created. A successful Mathia mechanism must therefore make an equivalent real-place phase/boundary operator intrinsic **before** Gram scalarization and couple it to the finite arithmetic selector in one geometry whose positivity has an independent theorem.