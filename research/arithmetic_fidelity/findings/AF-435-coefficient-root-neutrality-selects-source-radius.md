# AF-435 — Coefficient-root neutrality selects the source radius

## Status

`CLASSICAL-IDENTITY` · `EXACT-DERIVED` · `ARITHMETIC-FIDELITY` · `SOURCE-SELECTOR` · `RECIPROCAL-ORDER-SCALE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(z)=\sum_{j\ge0} a_j z^j
\]

be a non-polynomial analytic germ at the origin with finite nonzero Taylor radius `R(f)`. For every positive scale constant `c`, define the source-only coefficient-root response

\[
\Gamma_f(c)
:=
\limsup_{j\to\infty}|a_jc^j|^{1/j}.
\tag{1}
\]

Then the classical Cauchy--Hadamard formula gives the exact identity

\[
\boxed{\Gamma_f(c)=\frac{c}{R(f)}.}
\tag{2}
\]

Consequently the source radius is the unique positive **coefficient-root-neutral** scale:

\[
\boxed{
\Gamma_f(c)=1
\iff
c=R(f).
}
\tag{3}
\]

Equivalently,

\[
R(f)
=
\sup\{c>0:\Gamma_f(c)\le1\}
=
\inf\{c>0:\Gamma_f(c)\ge1\}.
\tag{4}
\]

Thus this selector is not obtained by asking which `c` behaves well downstream. It is the unique source scale separating exponential decay from exponential amplification of the Taylor-coefficient sequence after multiplication by the reciprocal-order scale constant.

For the Arithmetic Fidelity left-tail source

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}x\right),
\]

AF-433--AF-434 identify the nearest singularity radius

\[
R(h)=2\pi
\]

and the exact even coefficients

\[
[x^{2k}]h(x)
=
\frac{(-1)^k\zeta(2k)}{k(2\pi)^{2k}}.
\tag{5}
\]

Therefore

\[
\left|[x^{2k}]h(x)\,c^{2k}\right|^{1/(2k)}
=
\frac{c}{2\pi}
\left(\frac{\zeta(2k)}k\right)^{1/(2k)}
\longrightarrow
\frac{c}{2\pi},
\tag{6}
\]

so coefficient-root neutrality selects exactly

\[
\boxed{c=2\pi=r_1.}
\tag{7}
\]

This closes the source-admissibility gate of `CLUE-linear-derivative-shift-full-tail` for the natural admissible class of coefficient-root-critical selectors. Since the determinant amplitude is

\[
a=\left(\frac{c}{2\pi}\right)^2,
\]

the source-selected value is `a=1`. AF-426 then applies with `m=1` and proves that complete adjacent-packet cancellation cannot occur on that exact-square fiber. Hence the source selector survives, while the current packet-cancellation route does not.

## 1. Cauchy--Hadamard gives the selector exactly

For `c>0`,

\[
|a_jc^j|^{1/j}=c|a_j|^{1/j}.
\]

Taking the limsup and using

\[
\limsup_{j\to\infty}|a_j|^{1/j}=\frac1{R(f)}
\]

gives `(2)` immediately. No regularity of the coefficient sequence beyond the finite nonzero radius is needed; sparse zero coefficients are harmless because the statement uses a limsup.

Equation `(2)` produces a sharp trichotomy intrinsic to the source germ and the chosen source coordinate:

\[
c<R(f)\Rightarrow\Gamma_f(c)<1,
\qquad
c=R(f)\Rightarrow\Gamma_f(c)=1,
\qquad
c>R(f)\Rightarrow\Gamma_f(c)>1.
\tag{8}
\]

The value `1` is not an externally tuned threshold: it is the neutral root rate between exponential contraction and exponential expansion. This removes the `\kappa R` ambiguity left open by similarity-equivariance alone in AF-433. Multiples `c=\kappa R` remain similarity-covariant, but only `\kappa=1` is root-neutral.

The construction also has the expected dilation covariance. If

\[
f_\lambda(z)=f(z/\lambda),
\qquad \lambda>0,
\]

then `R(f_\lambda)=\lambda R(f)` and

\[
\Gamma_{f_\lambda}(c)=\frac{c}{\lambda R(f)}.
\tag{9}
\]

Hence the neutral selector scales as `S(f_\lambda)=\lambda S(f)`.

## 2. Specialization to the Bernoulli source

AF-434 gives the canonical product expansion

\[
\frac{1-e^{-x}}x
=e^{-x/2}\prod_{j\ge1}
\left(1+\frac{x^2}{(2\pi j)^2}\right),
\]

and therefore

\[
h(x)
=
\frac x2+
\sum_{k\ge1}
\frac{(-1)^k\zeta(2k)}{k(2\pi)^{2k}}x^{2k}.
\tag{10}
\]

The singularity ladder is `\{2\pi i j:j\in\mathbb Z\setminus\{0\}\}`, so the nearest shell has radius `r_1=2\pi`. Independently, `(6)` shows that the same value is the exact coefficient-root transition. Since

\[
\zeta(2k)^{1/(2k)}\to1,
\qquad
k^{-1/(2k)}\to1,
\]

all farther-shell aggregate information in `\zeta(2k)` is subexponential at this root scale. The source radius, rather than a downstream packet feature, fixes the neutral constant.

This source-side mechanism is different from the shell/packet transport rejected in AF-434. No source-shell label is carried through Cauchy--Binet. Instead, the complete coefficient sequence determines a single critical scale before the target partition decomposition is introduced.

## 3. Consequence for the reciprocal-order determinant route

The live clue asked for a principled selector for the reciprocal-order family

\[
x_n(c)=\frac cn
\]

that could be fixed without inspecting packet cancellation or exceptional-set membership. The coefficient-root criterion supplies such an admissible class: select the unique `c` for which the source Taylor coefficients are exponentially neutral under multiplication by `c^j`.

For `h`, this gives `c=2\pi`. AF-417's normalized fixed-excess law uses the corresponding amplitude

\[
a=\frac{c^2}{4\pi^2},
\]

so the selected amplitude is exactly `a=1`, the `m=1` square fiber. AF-426 proves on every exact-square fiber that the unique asymptotically admissible integer depth still leaves

\[
Q_{n,m}\longrightarrow
\frac{4m^2e^{2m}}{(2m-1)^2\zeta(2m)}>1.
\tag{11}
\]

In particular, at `m=1`, complete adjacent-packet cancellation is impossible. AF-426 deliberately does not infer exponential divergence there because the tied packet rate is only `\Lambda_1=1`; the conclusion here is correspondingly narrow: the present cancellation mechanism is closed at the source-selected probe, not that the entire determinant hierarchy has been classified.

## Prior-art and novelty audit

Equation `(2)` is exactly the classical Cauchy--Hadamard radius formula rewritten after multiplying the Taylor coefficients by `c^j`. The Encyclopedia of Mathematics, *Cauchy-Hadamard theorem*, records

\[
R^{-1}=\limsup |a_j|^{1/j}
\]

and the associated convergence/divergence boundary; the theorem goes back to Cauchy and Hadamard. See <https://encyclopediaofmath.org/wiki/Cauchy-Hadamard_theorem>. Arithmetic Fidelity already used the same classical radius principle in AF-235, so no novelty is claimed for the root test, the radius formula, or the fact that a nearest analytic obstruction determines the Taylor radius.

The Mathia-specific result is only the application to the open provenance gate left by AF-433--AF-434: coefficient-root neutrality defines a source-only admissible selector class, that class has the unique selector `c=R(h)=2\pi`, and the resulting downstream amplitude can then be audited independently using AF-426.

## Boundaries and falsification checks

- Coefficient-root neutrality is one principled admissible selector class, not a theorem that every possible notion of canonical reciprocal-order probe must choose `R(f)`.
- The selector is canonical relative to the fixed source coordinate. A nonlinear reparameterization of the source may change Taylor radii and is not covered by the dilation covariance `(9)`.
- `\Gamma_f(R)=1` does not assert convergence of the Taylor series on `|z|=R`; boundary convergence is intentionally irrelevant to the selector.
- The criterion acts on the scale constant `c` through high-order source coefficients. It must not be confused with evaluating `h(c/n)` alone, which lies near the regular point `0` for every fixed `c` as `n\to\infty`.
- AF-434 remains in force: this result does not transport a shell index into a packet index and does not recover shell-resolved provenance after coefficient aggregation.
- AF-426 closes complete adjacent-packet cancellation at `a=1`, but does not by itself rule out every other full-determinant mechanism, an enriched shell-resolved representation, or a different independently justified source selector class.
- No statement about the rational-prime discriminator, the Riemann zero set, or RH follows from `(1)`--`(11)`.

## Consequence for the research line

The accepted full-tail clue no longer needs a freely chosen amplitude. Within the source-native coefficient-root-critical class, the reciprocal-order constant is fixed before any target calculation as `c=2\pi`, hence `a=1`. Combining that source result with AF-426 yields a clean provenance-first negative test: the canonical root-neutral probe reaches an exact square, but the integer derivative source still cannot cancel the adjacent complete packets.

A future continuation of this determinant branch must therefore change something substantive rather than retune `c`: either justify a different source-side admissibility notion independently, introduce a representation that retains shell-resolved provenance before aggregation, or investigate a target mechanism not requiring the adjacent-packet cancellation already excluded at the selected scale.