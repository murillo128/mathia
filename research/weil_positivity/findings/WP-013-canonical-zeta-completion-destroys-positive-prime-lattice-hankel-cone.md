# WP-013 — canonical zeta completion destroys the positive Prime-Lattice Hankel cone

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct Hankel/Laplace/moment completion of the positive Prime-Lattice axis measure. This does **not** rule out non-Hankel compressions, relative/cohomological quotients, intersection forms, boundary-response constructions, or other mechanisms in which positivity appears only after a genuinely different global operation.

## 1. Claim

`WP-004` gives the exact positive Prime-Lattice measure

\[
\mu_{1/2}
=
\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}
=
\sum_p\sum_{k\ge1}(\log p)p^{-k/2}\,\delta_{k\log p}.
\tag{1}
\]

Unlike the passive-jump energy tested in `WP-009`, this infinite measure has a completely natural positive **Laplace/Hankel** realization. For `u>1/2`,

\[
h_{\rm fin}(u)
:=\int_0^\infty e^{-ut}\,d\mu_{1/2}(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{n^{u+1/2}}
=-\frac{\zeta'}{\zeta}\!\left(\frac12+u\right).
\tag{2}
\]

Hence, on `x,y>1/4`,

\[
\boxed{
K_{\rm fin}(x,y)=h_{\rm fin}(x+y)
}
\tag{3}
\]

is a positive-semidefinite Hankel kernel. This positivity is exact, independent of RH, and uses the Prime-Lattice weights without inserting any zero data.

However, the canonical first step toward the global zeta completion already leaves the positive Hankel cone. Removing the pole at `s=1` forces

\[
h_{\rm pole}(u)
:=h_{\rm fin}(u)-\frac1{u-1/2},
\tag{4}
\]

and the Laurent expansion at `s=1` gives

\[
\boxed{
\lim_{u\downarrow1/2}h_{\rm pole}(u)=-\gamma<0.
}
\tag{5}
\]

Therefore the Hankel kernel `h_pole(x+y)` has negative diagonal for `x>1/4` sufficiently close to `1/4`, so it cannot be positive semidefinite.

Adding the full canonical archimedean and polar completion does not rescue the same-sign Hankel route. With

\[
\xi(s)
=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and

\[
h_\xi(u)
:=-\frac{\xi'}{\xi}\!\left(\frac12+u\right),
\tag{6}
\]

the finite-prime component retains the positive sign of (2), but Stirling's formula gives

\[
\boxed{
h_\xi(u)
=-\frac12\log\frac{u+1/2}{2\pi}+O(u^{-1})
\longrightarrow-\infty.
}
\tag{7}
\]

Thus `h_xi(x+y)` also has negative diagonal for all sufficiently large `x`. Flipping the overall sign would make the large-parameter archimedean behavior positive, but would simultaneously flip every Prime-Lattice atom in (1) to a negative coefficient.

Consequently the direct route

```text
WP-004 positive axis measure
    -> Laplace transform / positive Hankel kernel
    -> canonical pole + gamma completion
    -> global Weil positivity
```

fails exactly: **the finite object lies inside the positive moment cone, while the canonical global completion exits that cone.**

## 2. The finite Prime-Lattice Hankel kernel is genuinely positive

Fix finitely many `x_1,...,x_N>1/4` and coefficients `c_1,...,c_N`. From (1)--(3),

\[
\begin{aligned}
\sum_{i,j}c_i\overline{c_j}K_{\rm fin}(x_i,x_j)
&=\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
\left|\sum_i c_i n^{-x_i}\right|^2\\
&\ge0.
\end{aligned}
\tag{8}
\]

The sum converges because `2 min_i x_i>1/2`, equivalently the resulting Dirichlet exponent is strictly larger than `1`.

So this is not a formal positivity obtained by analytic continuation. It lives entirely in the ordinary Euler-product half-plane after the critical `n^{-1/2}` weighting has been absorbed into the intrinsic measure (1).

The same statement can be expressed as complete monotonicity. For every integer `m>=0`,

\[
(-1)^m h_{\rm fin}^{(m)}(u)
=
\sum_{n\ge2}
\frac{\Lambda(n)(\log n)^m}{n^{u+1/2}}
>0,
\qquad u>\frac12.
\tag{9}
\]

Thus the Prime-Lattice finite factor gives a particularly rigid positive object: a Laplace moment kernel, not merely a positive diagonal operator.

This is the natural escape from the large-jump obstruction of `WP-009`. The same measure that cannot be a Lévy jump measure at the critical weight becomes perfectly finite after Laplace damping.

## 3. The zeta pole subtraction has the wrong sign for moment positivity

Write `s=1+epsilon`. The Laurent expansion

\[
\zeta(1+\varepsilon)
=\frac1\varepsilon+\gamma+O(\varepsilon)
\]

implies

\[
-\frac{\zeta'}{\zeta}(1+\varepsilon)
=\frac1\varepsilon-\gamma+O(\varepsilon).
\tag{10}
\]

Since `epsilon=u-1/2`, equations (4)--(5) follow immediately.

The subtraction itself also has a clean measure meaning:

\[
\frac1{u-1/2}
=
\int_0^\infty e^{-ut}e^{t/2}\,dt,
\qquad u>\frac12.
\tag{11}
\]

Therefore the pole cancellation transforms the positive atomic measure (1) into the signed formal measure

\[
\mu_{1/2}-e^{t/2}dt.
\tag{12}
\]

The sign failure is not hidden in a delicate operator-domain issue: equation (5) already makes the one-by-one principal minor negative. Any positive-semidefinite kernel must satisfy `K(x,x)>=0`, and `h_pole(2x)<0` for `x` sufficiently close to `1/4`.

This is also not cured by declaring the pole term a harmless renormalization. The subtraction in (4) is precisely the canonical pole cancellation that occurs when `-zeta'/zeta` is inserted into the completed logarithmic derivative. Omitting it means that the object is still the finite Euler factor rather than the completed zeta object.

## 4. The gamma completion forces a second, asymptotic sign obstruction

Differentiate the completed function:

\[
-\frac{\xi'}{\xi}(s)
=
-\frac1s
-\frac1{s-1}
+\frac12\log\pi
-\frac12\psi(s/2)
-\frac{\zeta'}{\zeta}(s),
\tag{13}
\]

where `psi=Gamma'/Gamma`.

For real `s->+infinity`, the Euler series gives `zeta'(s)/zeta(s)=O(2^{-s} log 2)`, while the classical digamma asymptotic is

\[
\psi(s/2)=\log(s/2)-\frac1s+O(s^{-2}).
\tag{14}
\]

Substitution into (13) yields

\[
-\frac{\xi'}{\xi}(s)
=-\frac12\log\frac{s}{2\pi}+O(s^{-1}),
\tag{15}
\]

which is (7).

Hence no positive Hankel kernel can be obtained by simply replacing `h_fin` by the canonical completed logarithmic derivative while preserving the sign of the finite Prime-Lattice atoms. A finite additive constant cannot repair the problem because the negative drift in (15) is logarithmically unbounded.

An arbitrary extra function could of course force the diagonal positive, but that would no longer be the canonical zeta completion and would fail this research line's no-hand-picked-counterterm gate unless independently forced by a larger geometry.

## 5. Matched generalized-prime control

The finite Hankel positivity uses only two ingredients:

1. nonnegative generalized von Mangoldt weights on generalized prime powers;
2. convergence of the associated Dirichlet series in an Euler-product half-plane.

Therefore the construction extends verbatim to Beurling generalized-prime systems in their absolute-convergence region:

\[
K_{\mathcal P}(x,y)
=
\sum_q \Lambda_{\mathcal P}(q)
q^{-1/2-x-y}
\ge_{\rm PSD}0.
\tag{16}
\]

The Diamond--Montgomery--Vorhauer control already used in `WP-004` has a generalized-integer counting law of the expected linear scale but a zeta function with infinitely many zeros approaching `Re(s)=1`. Thus finite Hankel positivity is not a hidden arithmetic selector for the Riemann system; it is another universal consequence of positive Euler weights.

What distinguishes ordinary `Q` is the canonical gamma/pole completion. Equations (5) and (7) show that **the very structure that makes the object global and `Q`-specific destroys the direct moment positivity**.

This control is important because it prevents the positive kernel (3) from being mistaken for a new route to RH merely because it contains the exact critical `Lambda/sqrt(n)` weights.

## 6. Relation to earlier Weil-positivity findings

This obstruction is different from the earlier failures.

- `WP-004` supplied the positive atomic Prime-Lattice measure itself.
- `WP-005` showed that the exact Weil autocorrelation lift turns those atoms into an indefinite translation/cosine operator.
- `WP-009` showed that interpreting the atoms as passive jump conductances gives infinite energy on every nonzero compactly supported Weil test.
- The present finding uses a different operation: exponential damping converts the same infinite measure into a well-defined **positive Hankel moment kernel**. That route survives both of those local objections, but it then fails at the canonical global completion.

Thus there is a genuine new pinch:

\[
\boxed{
\text{Prime-Lattice finite weights}
\xrightarrow{\text{Laplace/Hankel}}
\text{unconditional positivity}
\xrightarrow{\text{pole + gamma completion}}
\text{sign failure}.
}
\tag{17}
\]

The missing global mechanism cannot be just a moment completion of the finite measure.

## 7. Prior art and novelty assessment

No novelty is claimed for the general Hankel/Laplace theorem, the Euler logarithmic derivative, the Laurent expansion at `s=1`, or Stirling's formula.

Pushnitski and Treil's modern positive-Hankel framework states explicitly that a Hankel operator with kernel `h(t+s)` is positive semidefinite exactly when the kernel function is the Laplace transform of a positive measure (under the corresponding operator hypotheses). Equation (8) is the elementary finite-Gram version needed here and does not depend on invoking the full operator theorem.

The nearby zeta literature also already contains global Hankel/moment formulations whose positivity is equivalent to RH; Suzuki's screw-function work is one such retained boundary in this corpus. Those results do not supply an independent sign theorem for the present construction.

The Mathia-specific contribution is therefore a **no-go synthesis**, not a new Hankel theorem: the intrinsic WP-004 axis measure produces a bona fide positive moment kernel, but the exact pole cancellation and the completed gamma factor required by the Riemann zeta function force that same-sign Hankel family out of the positive cone.

## 8. Audit / falsification core

The decisive checks are finite and explicit:

1. verify from `WP-004` that the axis measure is (1);
2. for `u>1/2`, expand `-zeta'/zeta(1/2+u)` into its absolutely convergent von-Mangoldt series and obtain (2);
3. expand the quadratic form to obtain the Gram identity (8);
4. use `zeta(1+epsilon)=epsilon^{-1}+gamma+O(epsilon)` to derive (10) and the negative limit (5);
5. differentiate the standard definition of `xi(s)` to obtain (13);
6. insert the digamma asymptotic to obtain the negative divergence (15).

A counterexample to the stated no-go must therefore change the structure materially. It would have to produce a canonical global operation that is **not** the direct sum-variable Hankel completion `h(x+y)` of the WP-004 measure, or derive additional terms from a larger geometry in a way that changes the positivity theorem before comparison with the completed explicit formula.

## 9. Consequence for the research line

The finding removes another apparently promising universal-positive route. The Prime-Lattice finite measure is rich enough to generate more than a diagonal positive operator: it generates an entire positive moment kernel. But the completed zeta data do not remain in that cone.

The surviving target is therefore narrower. A successful construction must let the archimedean/polar sector interact with the finite-prime sector through a **nontrivial compression, quotient, grading, boundary response, relative determinant, cohomological/intersection pairing, or comparable global operation** whose positivity is proved independently. Merely Laplace-transforming the exact finite weights and then appending the standard completion cannot supply Weil positivity.