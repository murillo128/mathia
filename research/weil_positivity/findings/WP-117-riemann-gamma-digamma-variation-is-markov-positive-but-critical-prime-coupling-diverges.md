# WP-117 — Riemann Gamma digamma variation is Markov-positive but critical prime coupling diverges

**Status:** `EXACT-DERIVED + CLASSICAL-CONSEQUENCE + MARKOV-POSITIVE + PRIME-CIRCLE-BRIDGE + DECISIVE-CRITICAL-OBSTRUCTION + MATCHED-CONTROL + PRIOR-ART-AUDITED` for the attempt to turn the intrinsically selected Prime-Circle `q=2` Gamma channel into the positive archimedean part of a single global Weil geometry.

`WP-036` shows that the exact Prime-Circle radial Mellin response contains `psi(s/q)` on every full-root diagonal, while `WP-048` independently selects `q=2` from the anchored reflection/cycle geometry and therefore identifies the Riemann `psi(s/2)` channel without choosing `2` merely because the target Gamma factor is known. The remaining question is whether the Gamma response itself carries an independent positivity theorem after the affine extraction that prevented the positive-real theorem of `WP-036` from transferring directly.

It does. For every `a>0`, the vertical digamma variation

\[
h_a(u):=\operatorname{Re}\psi(a+iu)-\psi(a)
\tag{1}
\]

is a continuous conditionally negative-definite function on `R`, with an explicit symmetric Lévy measure. In particular, on the Riemann critical line the normalized real Gamma logarithmic-derivative variation

\[
H_\infty(t)
:=\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\psi\!\left(\frac14\right)
\tag{2}
\]

is exactly a Lévy--Dirichlet/Markov symbol. Its associated quadratic form is nonnegative for the ordinary geometric reason that it is a jump energy; RH and zeta zeros do not enter.

This is a genuine improvement over merely observing a digamma inside a positive-real response. However, the same exact symbol cannot be used as a scalar Kronecker energy on an exact critical Prime-Lattice/prime-torus completion: `WP-115` applies verbatim and forces infinite prime-axis energy. Thus Mathia now contains a canonical independently positive archimedean response, but the direct scalar gluing of that response to the critical finite-prime carrier is impossible. Any surviving global route must couple the finite and infinite places nonseparably, change the observable/domain, or leave the scalar Markov/Dirichlet class before the final positivity theorem.

This finding does **not** prove Weil positivity or RH. It does not supply the additive/polar global terms, and it does not claim that conditional negative definiteness of the digamma variation is historically new. The special-function identity and Lévy--Khintchine theorem are classical; the Mathia-specific content is the exact bridge from the independently selected Prime-Circle `q=2` channel to this Markov-positive symbol together with the matched critical exclusion from `WP-115`.

## 1. The vertical digamma variation has a positive Lévy representation

For `Re z>0`, NIST DLMF §5.9(ii), Eq. 5.9.12 gives the classical integral representation

\[
\psi(z)
=
\int_0^\infty
\left(
\frac{e^{-x}}{x}
-
\frac{e^{-zx}}{1-e^{-x}}
\right)dx.
\tag{3}
\]

Fix `a>0` and subtract the value at `z=a`. Taking real parts at `z=a+iu` gives exactly

\[
\boxed{
h_a(u)
=
\int_0^\infty
(1-\cos ux)
\frac{e^{-ax}}{1-e^{-x}}\,dx.
}
\tag{4}
\]

Define the symmetric measure on `R\setminus\{0\}`

\[
\boxed{
\nu_a(dy)
=
\frac12
\frac{e^{-a|y|}}{1-e^{-|y|}}\,dy.
}
\tag{5}
\]

Then (4) becomes

\[
\boxed{
h_a(u)
=
\int_{\mathbb R}
(1-\cos uy)\,\nu_a(dy).
}
\tag{6}
\]

This is an honest Lévy measure. Near zero,

\[
\frac12\frac{e^{-a|y|}}{1-e^{-|y|}}
\sim \frac1{2|y|},
\tag{7}
\]

so

\[
\int_{|y|<1}y^2\,\nu_a(dy)<\infty,
\tag{8}
\]

while the tail decays exponentially because `a>0`. Hence

\[
\int_{\mathbb R}(1\wedge y^2)\,\nu_a(dy)<\infty.
\tag{9}
\]

By the classical symmetric Lévy--Khintchine/Schoenberg characterization, (6) proves

\[
\boxed{
h_a\text{ is even, continuous, nonnegative, nontrivial, and conditionally negative definite.}}
\tag{10}
\]

No analytic continuation of zeta, zero data, RH assumption, or fitted spectral kernel is used in this sign theorem.

## 2. The positivity is an actual jump Dirichlet energy

Let `f` be a Schwartz function on `R` and use a unitary Fourier transform. The nonnegative multiplier `h_a` defines

\[
\mathcal E_a(f)
:=
\int_{\mathbb R}h_a(\xi)|\widehat f(\xi)|^2\,d\xi.
\tag{11}
\]

Using (6), Tonelli, and Plancherel,

\[
\begin{aligned}
\mathcal E_a(f)
&=
\int_{\mathbb R}\nu_a(dy)
\int_{\mathbb R}(1-\cos(\xi y))|\widehat f(\xi)|^2\,d\xi\\
&=
\boxed{
\frac12
\int_{\mathbb R}
\|f(\cdot+y)-f(\cdot)\|_2^2\,\nu_a(dy)
}\ge0.
\end{aligned}
\tag{12}
\]

Thus the sign does not come from declaring the Gamma term positive by analogy. It is the standard nonnegativity of a symmetric jump energy. This is exactly the sort of independent geometric/Markov theorem sought by the research mandate, although at this stage it covers only a normalized archimedean response rather than the global Weil form.

The general `a>0` family is also an adversarial control: the CND mechanism is not Riemann-specific. Arithmetic specificity must come from an independent reason to select the Riemann value `a=1/4`, not from (10) alone.

## 3. Prime Circle intrinsically selects the Riemann member of the family

For the real Gamma factor

\[
\Gamma_{\mathbb R}(s)
:=\pi^{-s/2}\Gamma(s/2),
\tag{13}
\]

write

\[
A_\infty(s)
:=\frac{d}{ds}\log\Gamma_{\mathbb R}(s)
=-\frac12\log\pi+\frac12\psi(s/2).
\tag{14}
\]

On the critical line `s=1/2+it`, subtraction at `t=0` removes the fixed scalar term and gives

\[
\boxed{
2\left[
\operatorname{Re}A_\infty\!\left(\frac12+it\right)
-A_\infty\!\left(\frac12\right)
\right]
=H_\infty(t)
=h_{1/4}(t/2).
}
\tag{15}
\]

Therefore (10) immediately implies that the normalized critical-line Gamma response is CND.

This specialization is not merely target matching inside Mathia. `WP-036` derives for every full-root level `q`

\[
\psi(s/q)
=\frac{s}{q}\mathcal M_{q,q}(s)-\gamma-\frac qs,
\tag{16}
\]

and originally left the choice `q=2` arbitrary. `WP-048` closes that selector gap: the anchored circle's unique orientation-reversing isometry has fixed locus `\mu_2`, and the compatible cycle Laplacian independently has its unique maximal nontrivial mode at order two. The same `q` labels the singular root set of the full-root radial field. Thus Prime Circle selects the `q=2` channel before the Riemann Gamma target is consulted, and (15) identifies the resulting vertical variation with the specific member `h_{1/4}(t/2)` of the classical CND family.

## 4. The Riemann Gamma symbol has an explicit symmetric jump geometry

Rescaling (4) with `a=1/4` gives

\[
\boxed{
H_\infty(t)
=2\int_0^\infty
(1-\cos ty)
\frac{e^{-y/2}}{1-e^{-2y}}\,dy.
}
\tag{17}
\]

Equivalently,

\[
\boxed{
H_\infty(t)
=
\int_{\mathbb R}(1-\cos ty)\,\nu_\infty(dy),
\qquad
\nu_\infty(dy)
=
\frac{e^{-|y|/2}}{1-e^{-2|y|}}\,dy.
}
\tag{18}
\]

The corresponding positive form is therefore

\[
\boxed{
\mathcal E_\infty(f)
=
\frac12\int_{\mathbb R}
\|f(\cdot+y)-f(\cdot)\|_2^2\,\nu_\infty(dy)
\ge0.
}
\tag{19}
\]

This is stronger than the statement from `WP-036` that the unrenormalized Mellin family is positive-real. The affine extraction leading to `psi(s/2)` does destroy that particular positive-real argument, but after restriction to the critical vertical line and normalization at `t=0`, the Gamma variation acquires a different independent positivity mechanism: it is the symbol of a symmetric Lévy--Dirichlet form.

## 5. Direct scalar gluing to the critical finite carrier is impossible

The tempting next step is to use the same canonical symbol as a positive scalar energy on the multiplicative Kronecker generator `X` of the Prime-Lattice/prime-torus completion,

\[
A_\infty^{\rm tor}
:=H_\infty(X).
\tag{20}
\]

On a prime-axis character `e_p`, the Kronecker frequency is

\[
E(e_p)=\log p.
\tag{21}
\]

For an exact critical finite positive completion of total mass `C`, the mandatory first prime-coordinate moment has magnitude

\[
|\widehat\eta(e_p)|
=\frac{\log p}{C\sqrt p}.
\tag{22}
\]

Since `H_infty` is a nontrivial continuous CND function with `H_infty(0)=0`, it lies exactly in the class treated by `WP-115`. Retaining only the compulsory prime-axis harmonics therefore gives

\[
\boxed{
\sum_p
H_\infty(\log p)
\frac{(\log p)^2}{C^2p}
=+\infty.
}
\tag{23}
\]

Thus the same Markov positivity that makes the archimedean channel canonical cannot be used as a finite scalar Kronecker energy at the critical normalization. The obstruction is not a defect of this particular jump measure; `WP-115` proves it for every nontrivial symmetric continuous CND scalar symbol.

As a transparent asymptotic check, the classical digamma asymptotic gives

\[
H_\infty(t)=\log|t|+O(1)
\qquad(|t|\to\infty),
\tag{24}
\]

so along prime axes

\[
H_\infty(\log p)
=\log\log p+O(1).
\tag{25}
\]

The critical summand is therefore of order

\[
\frac{(\log p)^2\log\log p}{p},
\tag{26}
\]

consistent with the general divergence theorem. In particular, no spurious extra factor `log p` is being hidden in the Gamma asymptotic.

## 6. The off-critical control is finite

Replace the critical first-harmonic amplitudes by the matched off-critical family

\[
|\widehat\eta_\sigma(e_p)|
\asymp
\frac{\log p}{p^\sigma},
\qquad \sigma>\frac12.
\tag{27}
\]

Then the one-prime contribution for the same symbol is bounded by a constant multiple of

\[
\sum_p
\frac{(\log p)^2(1+\log\log p)}{p^{2\sigma}},
\tag{28}
\]

which converges for every `sigma>1/2`. Hence the divergence in (23) occurs precisely at the arithmetic critical normalization relevant to the Weil carrier; it is not merely an ultraviolet failure of the Gamma jump form in every weighted realization.

This matched control also aligns with `WP-115`: its no-go is critical, not a claim that the CND symbol itself is ill-defined or non-geometric.

## 7. Falsification and prior-art boundary

Several stronger interpretations fail.

First, (19) is only the normalized `t`-dependent Gamma variation. The fixed `-\tfrac12\log\pi` contribution, the normalization at `t=0`, and the polar/global terms of the completed zeta explicit formula are not generated by the Lévy measure (18). Adding them by hand would violate the branch mandate.

Second, the `a>0` derivation shows that CND positivity is a generic special-function consequence of the classical digamma integral, not an arithmetic theorem specific to zeta. The Mathia-specific fact is that `WP-036` plus `WP-048` reaches the Riemann `a=1/4` member through an independently selected Prime-Circle channel.

Third, the construction contains no zeta zeros. It is therefore distinct from the RH-equivalent infinitely-divisible completed-zeta law audited in `SOURCES.md` (Nakamura--Suzuki), whose Lévy measure under RH is supported on zero ordinates. Here the positivity is unconditional but only archimedean, and the attempt to globalize it by the simplest scalar finite coupling is killed by (23).

Fourth, this does not evade classical Weil positivity by renaming its kernel. Equations (4)--(12) identify a standard Lévy--Dirichlet form before any Weil test functional is inserted. Conversely, no claim is made that this form already equals the Weil quadratic functional.

The bounded literature audit found the ingredients in standard sources: the digamma integral is NIST DLMF §5.9(ii), Eq. 5.9.12 (`https://dlmf.nist.gov/5.9.E12`), and the CND/Lévy--Khintchine implication is standard Lévy-process theory, for which `research/weil_positivity/SOURCES.md` already records Schilling's *An Introduction to Lévy and Feller Processes*. Searches for the exact phrase/classification of `Re psi(a+it)-psi(a)` as a conditionally negative-definite function did not expose a clear direct prior-art statement. That absence is **not** evidence of historical novelty; the derivation is an immediate classical consequence of (3).

## 8. Consequence for the Weil-positivity search

The surviving architecture is now narrower but more informative. Prime Circle supplies a canonical `q=2` archimedean channel; after the correct critical-line normalization, that channel has its **own** RH-independent positivity theorem, namely the jump Dirichlet energy (19). This answers one important part of the branch question more positively than `WP-036` did.

But the direct global scalar route

\[
\text{Prime-Circle Gamma symbol}
\longrightarrow
H_\infty(X)
\longrightarrow
\text{critical positive prime-torus energy}
\tag{29}
\]

is decisively impossible by `WP-115`. A viable global Weil geometry must therefore do something structurally different before positivity is taken: for example a nonseparable finite--archimedean coupling, matrix/graded or boundary pairing, quotient/compression with an independent sign theorem, or a non-Markov band-pass architecture whose distinguished scale is itself produced geometrically. `WP-116` shows why inserting such a scale arbitrarily is not an acceptable scale-free repair.

The key boundary is therefore:

\[
\boxed{
\text{intrinsic Prime-Circle Gamma response}
+\text{ independent Markov positivity}
\quad\text{exists,}
\qquad
\text{direct critical scalar gluing}
\quad\text{does not.}
}
\tag{30}
\]
