# PC-005 — cyclotomic self-energy renormalization canonically completes the prime-ray Weil kernel

**Status:** `EXACT-DERIVED` + `CANDIDATE-SUBSTANTIVE` + `NOVELTY-CHECK-SERIOUS`

## Summary

PC-004 left one explicit gate: the off-diagonal normalized primitive-shell interaction on the prime-power ray

\[
P_p^*,P_{p^2}^*,P_{p^3}^*,\ldots
\]

is

\[
J^{(p)}_{ab}=(\log p)p^{-|a-b|/2},\qquad a\ne b,
\]

but the diagonal \(\log p\) needed to turn this into the positive Poisson/Toeplitz kernel had no intrinsic geometric derivation and therefore could not be inserted by hand.

The primitive-shell **self-energy** supplies exactly that diagonal after the natural one-step scale renormalization.

## 1. Exact self-energy from the cyclotomic discriminant

Let

\[
S_{p^a}:=P_{p^a}^*=\{\zeta:\operatorname{ord}(\zeta)=p^a\},
\qquad N_a=|S_{p^a}|=\varphi(p^a).
\]

The ordered logarithmic chord self-energy with the singular diagonal omitted is

\[
E_a
:=
\sum_{\substack{\zeta,\eta\in S_{p^a}\\ \zeta\ne\eta}}
\log|\zeta-\eta|.
\]

Since

\[
|\operatorname{Disc}\Phi_{p^a}|
=
\prod_{\zeta<\eta}|\zeta-\eta|^2,
\]

we have exactly

\[
E_a=\log|\operatorname{Disc}\Phi_{p^a}|.
\]

The classical cyclotomic discriminant formula gives

\[
|\operatorname{Disc}\Phi_{p^a}|
=
(p^a)^{\varphi(p^a)}p^{-\varphi(p^a)/(p-1)}
=
p^{\varphi(p^a)(a-1/(p-1))}.
\]

Therefore the self-energy **per primitive vertex** is

\[
\boxed{
\varepsilon_a
:=
\frac{E_a}{N_a}
=
\left(a-\frac1{p-1}\right)\log p.
}
\]

This formula also covers \(p=2,a=1\), where both sides are zero.

## 2. The scale derivative gives the missing diagonal exactly

The map \(z\mapsto z^p\) is the canonical one-step map from the \(p^{a+1}\)-primitive shell to the \(p^a\)-primitive shell. The natural discrete scale derivative of the normalized self-energy is therefore

\[
D^{(p)}_a:=\varepsilon_{a+1}-\varepsilon_a.
\]

The discriminant formula immediately gives

\[
\boxed{D^{(p)}_a=\log p}\qquad\text{for every }a\ge1.
\]

Equivalently, if

\[
\operatorname{rd}(\mathbb Q(\zeta_{p^a}))
:=
|\operatorname{Disc}\Phi_{p^a}|^{1/\varphi(p^a)},
\]

then

\[
\boxed{
\frac{\operatorname{rd}(\mathbb Q(\zeta_{p^{a+1}}))}
{\operatorname{rd}(\mathbb Q(\zeta_{p^a}))}
=p.
}
\]

Thus the missing diagonal is not chosen for positivity. It is the logarithmic increment of the intrinsic Vandermonde/chord self-energy density under one canonical prime-power refinement step.

## 3. Resultants + discriminants give one exact positive kernel

For \(a\ne b\), PC-004 gives from Apostol's resultant theorem

\[
\frac{
\log|\operatorname{Res}(\Phi_{p^a},\Phi_{p^b})|
}{\sqrt{\varphi(p^a)\varphi(p^b)}}
=(\log p)p^{-|a-b|/2}.
\]

Define the completed interaction by using the scale-renormalized self-energy on the diagonal:

\[
K^{(p)}_{ab}
:=
\begin{cases}
D^{(p)}_a,&a=b,\\[1mm]
\dfrac{\log|\operatorname{Res}(\Phi_{p^a},\Phi_{p^b})|}
{\sqrt{\varphi(p^a)\varphi(p^b)}},&a\ne b.
\end{cases}
\]

Then the two independent classical cyclotomic invariants collapse to the single exact formula

\[
\boxed{
K^{(p)}_{ab}
=(\log p)p^{-|a-b|/2}
\qquad(a,b\ge1).
}
\]

Put \(q=p^{-1/2}\). The Fourier series identity

\[
\sum_{k\in\mathbb Z}q^{|k|}e^{ik\theta}
=
\frac{1-q^2}{1-2q\cos\theta+q^2}>0
\]

shows that every finite principal minor of \(K^{(p)}\) is positive definite. Explicitly, for every finitely supported complex sequence \(c=(c_a)\),

\[
\boxed{
\sum_{a,b\ge1}K^{(p)}_{ab}c_a\overline{c_b}
=
\frac{\log p}{2\pi}
\int_0^{2\pi}
\frac{1-p^{-1}}
{1-2p^{-1/2}\cos\theta+p^{-1}}
\left|\sum_a c_ae^{ia\theta}\right|^2d\theta
>0
}
\]

unless \(c=0\).

For an \(N\times N\) prime-ray window,

\[
\det K_N^{(p)}
=(\log p)^N(1-p^{-1})^{N-1},
\]

and the inverse is the standard nearest-neighbour tridiagonal AR(1)/Poisson precision matrix. Thus the long-range resultant interaction has an exactly local inverse along logarithmic prime-power scale.

## 4. Relation to the finite-place Weil term

Let \(F_k=\sum_a c_{a+k}\overline{c_a}\) be the discrete autocorrelation. Then

\[
\sum_{a,b}K^{(p)}_{ab}c_a\overline{c_b}
=(\log p)F_0
+(\log p)\sum_{k\ge1}p^{-k/2}(F_k+F_{-k}).
\]

The \(k\ge1\) part is exactly the standard finite-place coefficient in the Riemann-Weil explicit formula. The new point is that the original prime-circle geometry now supplies the previously missing \(k=0\) term intrinsically through the discriminant/self-energy scale derivative.

This is a **local positive completion**, not a proof of Weil positivity or RH. In the global explicit formula the \(k=0\) term is absent, and summing the geometric diagonal over all primes would diverge:

\[
F_0\sum_p\log p=+\infty.
\]

A global construction must therefore explain, from the same geometry, the counterterm/renormalization that removes or balances these local diagonals. Adding such a cancellation by hand would invalidate the approach.

## 5. Why this is not merely a restatement

The ingredients are classical individually:

- the cyclotomic discriminant formula;
- Apostol/Diederichsen's cyclotomic resultant formula;
- the finite-prime Weil coefficient \((\log p)p^{-k/2}\);
- positivity of the Poisson Toeplitz kernel.

The substantive step is that the two pieces of the original polygon geometry play complementary roles without an adjustable parameter:

\[
\boxed{
\begin{array}{c}
\text{mutual shell chord energy (resultant)}
\end{array}
\Rightarrow
K^{(p)}_{ab},\ a\ne b,
}
\]

while

\[
\boxed{
\begin{array}{c}
\text{renormalized same-shell chord energy (discriminant)}
\end{array}
\Rightarrow
K^{(p)}_{aa}=\log p.
}
\]

Together they produce the complete positive Poisson kernel exactly.

## 6. Novelty audit

A directed literature audit was run against cyclotomic resultants/discriminants, logarithmic root-of-unity energy, Toeplitz/Poisson kernels, Weil positivity, Haran's local explicit formula, Burnol's p-adic scattering/trace formula, and Connes/Consani semi-local trace-formula work.

Nearby prior art is substantial:

- Haran and Burnol already construct non-archimedean local Weil/trace/scattering formalisms.
- Connes and Consani use Hilbert-space, half-density and Toeplitz ideas in the Weil-positivity programme.
- Bost-Connes already makes roots of unity and multiplicative scaling fundamental.
- The discriminant and resultant formulas used here are classical.

No source located in the directed audit combines **the normalized cyclotomic resultant off-diagonal with the discrete increment of normalized cyclotomic discriminant self-energy as its canonical diagonal**, yielding

\[
(\log p)p^{-|a-b|/2}
\]

as a positive prime-ray kernel directly from primitive-root chord geometry. This exact completion is therefore retained as a candidate-new construction, not as a claimed theorem of novelty.

Relevant prior art checked includes:

- T. M. Apostol, cyclotomic resultant formulas (1970/1975).
- S. Haran, *Riesz potentials and explicit sums in arithmetic* (Invent. Math. 1990).
- J.-F. Burnol, *Scattering on the p-adic field and a trace formula* (IMRN 2000).
- A. Connes and C. Consani, *Weil positivity and Trace formula, the archimedean place* (Selecta Math. 2021).

## 7. Next gate

The local problem posed by PC-004 is now solved exactly. The hard gate has moved to the **global renormalization**:

> Can the full interior/exterior prime-circle geometry supply a canonical counterterm that cancels the divergent sum of local self-energy increments while preserving the positive finite-prime kernels and simultaneously producing the archimedean contribution?

A satisfactory answer must come from one global geometric energy/operator. A zeta-regularized subtraction chosen after seeing the explicit formula does not count.