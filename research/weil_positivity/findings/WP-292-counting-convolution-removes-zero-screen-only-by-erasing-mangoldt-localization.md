---
id: WP-292
title: Counting convolution removes the zero screen only by erasing Mangoldt localization
branch: weil_positivity
status: supported
kind: signed-source-convolution-tradeoff
claim_strength: exact unconditional tempered category descent after canonical counting convolution, with exact recovery restoring the RH-equivalent Mangoldt obstruction
created: 2026-09-14
related: [WP-269, WP-270, WP-278, WP-285, WP-286, WP-290, WP-291]
prior_art:
  - classical Dirichlet-convolution identity 1 * Lambda = log and Mobius inversion Lambda = mu * log
  - G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, Section 17.7
  - T. M. Apostol, Introduction to Analytic Number Theory, arithmetic functions and Dirichlet convolution
  - Szilard Gy. Revesz, The Carlson-type zero-density theorem for the Beurling zeta function, JLMS 111 (2025), e70110
---

# WP-292 — Counting convolution removes the zero screen only by erasing Mangoldt localization

## Claim

`WP-290` and `WP-291` show that every **finite source-native dilation-difference hierarchy applied directly to the critical Mangoldt half-density** remains trapped at an RH-equivalent category gate. The zeta pole can be killed without zero data, but any nontrivial zero off the critical line survives as a pole of the logarithmic derivative, and the resulting signed source is tempered if and only if RH.

There is a canonical way to evade that zero screen **unconditionally** before taking the dilation differences. It is also a decisive matched control, because the escape works by converting the prime-power carrier into the all-integer logarithmic carrier.

Define on the positive logarithmic half-line

\[
\mu_\Lambda
:=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n},
\qquad
\nu
:=\sum_{m\ge1}\frac1{\sqrt m}\,\delta_{\log m}.
\tag{1}
\]

Their additive convolution is locally finite and satisfies the exact identity

\[
\boxed{
\nu*\mu_\Lambda
=\omega
:=\sum_{N\ge2}\frac{\log N}{\sqrt N}\,\delta_{\log N}.
}
\tag{2}
\]

Indeed, the coefficient at `log N` is

\[
\frac1{\sqrt N}\sum_{d\mid N}\Lambda(d)
=\frac{\log N}{\sqrt N}.
\tag{3}
\]

Equivalently, for `Re s>1/2`,

\[
\mathcal L\nu(s)=\zeta(s+1/2),
\qquad
\mathcal L\mu_\Lambda(s)=-\frac{\zeta'}{\zeta}(s+1/2),
\tag{4}
\]

and therefore

\[
\boxed{
\mathcal L\omega(s)=-\zeta'(s+1/2).
}
\tag{5}
\]

The multiplication by `zeta` has removed **all poles coming from nontrivial zeros**, not by knowing where the zeros are but by undoing the logarithmic derivative. What remains is the double pole at `s=1/2` inherited from the pole of `zeta` at `1`.

For any integer `q>=2`, let

\[
\Delta_q:=I-\sqrt q\,S_{\log q}.
\tag{6}
\]

Then two source-native dilation coboundaries remove that double pole and give an ordinary tempered distribution **without RH**:

\[
\boxed{
T_q:=\Delta_q^2\omega\in\mathcal S'(\mathbb R)
\qquad\text{unconditionally}.
}
\tag{7}
\]

Its Laplace transform is

\[
\mathcal L T_q(s)
=\bigl(1-q^{1/2-s}\bigr)^2\bigl(-\zeta'(s+1/2)\bigr),
\tag{8}
\]

so the order-two zero at `s=1/2` cancels the only pole of `zeta'`, while there are no zero-divisor poles left to screen the half-plane.

This is a genuine source-native signed category descent left open by `WP-291`, but it **does not advance toward Weil positivity**. The price of unconditional admissibility is exact loss of Mangoldt localization: the intermediate carrier (2) can be constructed from the ordinary integers with no prime-power selector at all. Moreover, exact recovery of the Mangoldt carrier is Möbius inversion, and applying that inverse to `T_q` returns exactly the RH-equivalent object already closed by `WP-291`.

Thus the tradeoff is exact:

\[
\boxed{
\text{unconditional category descent}
\quad\Longleftrightarrow\quad
\text{erase the logarithmic-derivative / prime-power localization},
}
\tag{9}
\]

within this canonical convolution route. Restoring that localization restores the zero screen and the RH-equivalent category gate.

**Classification:** `EXACT-DERIVED + SOURCE-NATIVE-DIRICHLET-CONVOLUTION + ZERO-INDEPENDENT-ZERO-SCREEN-REMOVAL + UNCONDITIONAL-TEMPERED-DESCENT + PRIME-POWER-LOCALIZATION-ERASURE + SIGNED-CANCELLATION + BOTH-JORDAN-PARTS-NONTEMPERED + MOBIUS-INVERSE-RESTORES-RH-GATE + GENERALIZED-PRIME-MATCHED-CONTROL + CLASSICAL-ARITHMETIC-IDENTITY + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The convolution is canonical and exact

The operation in (2) is not fitted to zeta zeros. In logarithmic coordinates, multiplication of integers becomes addition, so additive convolution of the two atomic measures is precisely Dirichlet convolution of their arithmetic coefficients. For every `N`, only finitely many divisor pairs `mn=N` contribute, hence the convolution is well-defined as a locally finite measure before any global growth condition is imposed.

At `log N`,

\[
\begin{aligned}
(\nu*\mu_\Lambda)(\{\log N\})
&=\sum_{mn=N}\frac1{\sqrt m}\frac{\Lambda(n)}{\sqrt n}\\
&=\frac1{\sqrt N}\sum_{n\mid N}\Lambda(n)\\
&=\frac{\log N}{\sqrt N}.
\end{aligned}
\tag{10}
\]

The last equality is the classical identity

\[
\mathbf 1*\Lambda=\log.
\tag{11}
\]

The transform calculation (4)--(5) says the same thing analytically:

\[
\zeta(s+1/2)
\left(-\frac{\zeta'}{\zeta}(s+1/2)\right)
=-\zeta'(s+1/2).
\tag{12}
\]

This matters because it identifies exactly how the nontrivial-zero poles disappear. No cancellation between individual zero modes is being engineered. The entire zero divisor ceases to appear because the source has been moved from a logarithmic derivative to an ordinary derivative.

That is already a warning for the Weil objective. The explicit-formula finite term is prime-power localized precisely because it comes from `-zeta'/zeta`, not from `-zeta'`. Equation (12) removes the analytic obstruction by removing the same structural feature that supplies the required finite-prime support.

## 2. Two dilation coboundaries give unconditional temperedness

The transform argument makes the required order transparent: `-zeta'(s+1/2)` has a double pole at `s=1/2`, so one factor `1-q^(1/2-s)` is insufficient while two factors have the correct zero order. A direct real-space proof avoids using any converse transform theorem.

Let

\[
W(X):=\sum_{2\le n\le X}\frac{\log n}{\sqrt n}.
\tag{13}
\]

Elementary Euler summation gives a constant `C` such that

\[
W(X)
=2\sqrt X\log X-4\sqrt X+C
+O\!\left(\frac{\log X}{\sqrt X}\right).
\tag{14}
\]

The cumulative function of `T_q` is, for sufficiently large `X`,

\[
D_q^{(2)}(X)
=W(X)-2\sqrt q\,W(X/q)+q\,W(X/q^2).
\tag{15}
\]

Substituting (14), the `sqrt(X) log X` terms cancel, the `sqrt(X) log q` terms cancel, and the `sqrt(X)` terms cancel. Hence

\[
\boxed{
D_q^{(2)}(X)
=C(1-\sqrt q)^2
+O_q\!\left(\frac{\log X}{\sqrt X}\right).
}
\tag{16}
\]

In particular the cumulative function is bounded. The locally finite signed measure `T_q` is therefore the distributional derivative of a bounded function and defines a tempered distribution. No prime-number theorem, zero-free region, or RH input is used.

The first difference does not have this property. From (14),

\[
W(X)-\sqrt q\,W(X/q)
=2\sqrt X\log q+O_q(1),
\tag{17}
\]

which still has exponential growth in the logarithmic coordinate. Thus the order-two cancellation is not decorative: it matches exactly the order of the pole of `zeta'` at `1`.

This sharply contrasts with `WP-290`--`WP-291`. There, every finite product of the same dilation coboundaries leaves poles from off-critical zeros because the carrier remains `-zeta'/zeta`. Here two factors suffice unconditionally only because convolution by `nu` has already removed the denominator `zeta`.

## 3. The descent remains irreducibly signed

Unconditional temperedness does not turn (7) into a positive-energy construction. Both Jordan channels still have exponential mass.

The coefficient of `T_q` at `log N` is

\[
c_q(N)
=\frac{1}{\sqrt N}
\left[
\log N
-2q\,\mathbf 1_{q\mid N}\log(N/q)
+q^2\,\mathbf 1_{q^2\mid N}\log(N/q^2)
\right].
\tag{18}
\]

For every prime `p` not dividing `q`,

\[
c_q(p)=\frac{\log p}{\sqrt p}>0.
\tag{19}
\]

Hence, by the prime number theorem and partial summation,

\[
(T_q)_+([0,\log X])
\ge
\sum_{\substack{p\le X\\p\nmid q}}
\frac{\log p}{\sqrt p}
\sim2\sqrt X.
\tag{20}
\]

For the negative channel, take `N=qp` with `p` prime and `p\nmid q`. Then the `q^2` term vanishes and

\[
c_q(qp)
=\frac{\log q+(1-2q)\log p}{\sqrt{qp}},
\tag{21}
\]

which is negative for all sufficiently large `p`. Its magnitude is asymptotic to

\[
\frac{2q-1}{\sqrt q}\frac{\log p}{\sqrt p}.
\tag{22}
\]

Therefore `(T_q)_-` also has square-root cumulative growth, hence exponential growth in logarithmic coordinate. Neither Jordan part is tempered even though their signed difference is.

So the new unconditional category descent does not repair the sign-order obstruction of `WP-290`. It strengthens it: even after the zero screen has been removed algebraically, the admissible object exists only through cancellation between two individually inadmissible positive channels.

## 4. Exact recovery of prime support restores the RH-equivalent gate

The classical Dirichlet inverse of the constant-one arithmetic function is the Möbius function. Define the formal/local inverse half-density

\[
\eta
:=\sum_{m\ge1}\frac{\mu_{\rm Mob}(m)}{\sqrt m}\,\delta_{\log m}.
\tag{23}
\]

Coefficientwise convolution is locally finite and gives

\[
\eta*\nu=\delta_0,
\qquad
\eta*\omega=\mu_\Lambda.
\tag{24}
\]

Equivalently, on the initial convergence half-plane,

\[
\mathcal L\eta(s)=\frac1{\zeta(s+1/2)}.
\tag{25}
\]

Because convolution by `eta` commutes coefficientwise with the integer translation operators,

\[
\boxed{
\eta*T_q
=\Delta_q^2\mu_\Lambda.
}
\tag{26}
\]

But `WP-291` proves for every finite product of source-native dilation coboundaries, including the repeated pair `(q,q)`, that

\[
\boxed{
\Delta_q^2\mu_\Lambda\in\mathcal S'(\mathbb R)
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{27}
\]

Thus the Möbius inverse that exactly restores the prime-power-localized source also restores the zero-divisor obstruction. The transform identity is explicit:

\[
\frac1{\zeta(s+1/2)}
\bigl(1-q^{1/2-s}\bigr)^2
\bigl(-\zeta'(s+1/2)\bigr)
=
\bigl(1-q^{1/2-s}\bigr)^2
\left(-\frac{\zeta'}{\zeta}(s+1/2)\right).
\tag{28}
\]

This is the decisive tradeoff. Convolution by the counting carrier makes the signed source unconditionally admissible because it removes `1/zeta` from the logarithmic derivative. Exact arithmetic deconvolution puts `1/zeta` back and recovers precisely the RH-equivalent finite-difference hierarchy already classified.

No claim is needed about whether `eta` itself is tempered in some weaker or conditional sense. Equation (26) is a coefficientwise identity on compact support, while (27) shows that **its exact recovery action is not an unconditional category-preserving operation on this source**.

## 5. Matched controls show that the escape is arithmetic-blind

The output carrier `omega` has a direct definition that does not mention primes:

\[
\omega
=\sum_{N\ge2}\frac{\log N}{\sqrt N}\delta_{\log N}.
\tag{29}
\]

Therefore every subsequent statement in Sections 2--3 can be reproduced by starting from the ordinary integer set and never constructing `Lambda` at all. The disappearance of the zero screen is not evidence that a hidden Riemann-specific geometry has been found; it is exactly what should happen after the prime-power logarithmic derivative has been replaced by the derivative of the all-integer counting series.

The same algebraic collapse persists in the standard generalized-prime comparison class. For a free Beurling generalized-prime monoid with generalized von Mangoldt function `Lambda_G`, unique factorization gives

\[
\sum_{d\mid g}\Lambda_G(d)=\log|g|.
\tag{30}
\]

Thus convolution of the generalized counting half-density with its generalized Mangoldt half-density again produces the all-generalized-integer logarithmic carrier. The mechanism is therefore an Euler-monoid identity, not a selector of the Riemann global sign. Révész's 2025 treatment records the generalized von Mangoldt/logarithmic-derivative structure used for this matched control.

This separates the present mechanism from a genuine solution to the branch mandate. A useful global geometry may certainly use a signed source coupling, but if its only category improvement is the convolution (2), then any sign theorem proved after that step applies equally to the all-integer or generalized-prime control unless additional source-forced structure reintroduces arithmetic specificity. If that additional structure exactly reconstructs `Lambda`, (26)--(28) show that the RH-equivalent zero screen returns.

## 6. Prior-art and novelty audit

The arithmetic identities used here are classical. The divisor-sum formula `sum_{d|n} Lambda(d)=log n`, its Möbius inverse, multiplication of Dirichlet series by Dirichlet convolution, and `-zeta'(s)=sum log(n)n^{-s}` are standard analytic number theory; no novelty is claimed for them. Hardy--Wright and Apostol are standard references, while Révész supplies the directly relevant generalized-prime logarithmic-derivative setting.

The branch-level contribution is the **exact placement of those classical identities inside the current Mathia obstruction hierarchy**. `WP-290`--`WP-291` establish that finite source-dilation differences cannot make the Mangoldt carrier unconditionally tempered. Equations (2), (7), and (26) identify the first canonical zero-independent way around that gate and show algebraically why it is not progress toward the Weil target: it first destroys the logarithmic-derivative localization, and exact restoration returns the closed RH-equivalent problem.

This also differs from the growing-window control of `WP-285`. There the zero field is suppressed asymptotically by a generic long-memory average under a favorable RH assumption. Here no RH assumption and no growing observation window are needed. The cancellation is finite and exact after a canonical arithmetic convolution, but precisely for that reason its loss of prime localization can be identified coefficient by coefficient.

No independent positivity theorem appears. No Gamma or polar term is generated, no Weil quadratic identity is matched, and no geometric pairing is shown nonnegative. The result is a source-processing classification, not an RH criterion or a new number-theoretic identity.

## Consequence

The live signed-coupling question after `WP-291` is now narrower. **Unconditional category descent is possible**, so one cannot argue that every zero-independent signed preprocessing must remain RH-equivalent. But the canonical successful preprocessing found here works by passing from

\[
-\frac{\zeta'}{\zeta}
\quad\text{to}\quad
-\zeta',
\tag{31}
\]

which removes the same prime-power localization needed by the finite Weil term.

A genuinely useful next construction must therefore satisfy both of the following before any positivity theorem is counted:

1. produce an unconditional globally admissible signed carrier without importing zero data or assuming RH; and
2. retain a source-forced arithmetic distinction stronger than the all-integer identity `1*Lambda=log`, so that the finite-prime Weil coefficients can still be recovered **without applying an inverse operation that restores the `1/zeta` zero screen**.

Any candidate that smooths by the counting carrier and then invokes Möbius deconvolution has merely traversed the exact loop (2) -> (26) and returned to `WP-291`. Any candidate that stops after the smoothing has a tempered object, but no longer has the finite-prime Weil source it was supposed to explain.

## Evidence boundary

`WP-292` does **not** prove that every infinite-dimensional, adelic, cohomological, or geometric signed coupling must erase Mangoldt localization. It classifies one particularly canonical route: convolution by the critical all-integer counting half-density followed by finite source-native dilation differences.

It also does not claim that Möbius inversion is globally ill-defined in every generalized-function category. The exact claim is narrower: its coefficientwise action restores `Delta_q^2 mu_Lambda`, whose temperedness is RH-equivalent by `WP-291`. Hence Möbius recovery cannot serve as an unconditional category-preserving return map for this construction.

Finally, bounded cumulative growth of `T_q` supplies only tempered distributional hostability. It does not supply positivity, a Weil pairing, the archimedean Gamma term, the polar normalization, or a sign theorem. Those remain separate obligations under the canonical research mandate.
