# PL-341 — Weighted Schur geometry makes the prime block asymptotically half the total PNT mass

**Evidence:** `EXACT-DERIVED + SHARP-PNT-ASYMPTOTIC + DECISIVE-NEGATIVE + PNT-MATCHED-CONTROL`

**Status:** `SHARP-GLOBAL-PRIME-BLOCK-SPECTRUM + SHARP-JUMP-COERCIVITY + SCALAR-COMPENSATION-GAP + NO-RH-CONSEQUENCE`

## Precise claim

Use the fixed-domain notation of `PL-337`--`PL-340` on `I=(-1,1)`. For

\[
h_n(a)=\frac{\log n}{a},
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
W_a=\sum_{\log n<2a}w_n,
\]

set

\[
K_a:=\sum_{\log n<2a}w_n\bigl(S_{h_n(a)}+S_{h_n(a)}^*\bigr),
\qquad
P_a:=-K_a,
\qquad
J_a:=2W_aI-K_a.
\tag{PL341-1}
\]

Thus `P_a=J_a-2W_aI` is the actual prime block and `J_a` is the positive jump sector from `PL-339`.

Then, as `a->infinity`,

\[
\boxed{
\sup\sigma(K_a)=e^a(1+o(1)),
\qquad
\inf\sigma(K_a)=-e^a(1+o(1)).
}
\tag{PL341-2}
\]

Since the weighted Chebyshev sum satisfies

\[
W_a=2e^a(1+o(1)),
\tag{PL341-3}
\]

this is equivalently

\[
\boxed{
\frac{\inf\sigma(P_a)}{W_a}\to-\frac12,
\qquad
\frac{\sup\sigma(P_a)}{W_a}\to+\frac12.
}
\tag{PL341-4}
\]

Consequently the jump sector has the sharp asymptotic spectral edges

\[
\boxed{
\frac{\inf\sigma(J_a)}{W_a}\to\frac32,
\qquad
\frac{\sup\sigma(J_a)}{W_a}\to\frac52.
}
\tag{PL341-5}
\]

This strictly sharpens the channelwise lower bound `J_a>=(1-o(1))W_a I` from `PL-339`. More importantly, it proves that no refinement based only on the accumulated positive jump sector can reach the `2W_a` scalar compensation even asymptotically: there is an unavoidable leading deficit `W_a/2`. The endpoint witnesses of `PL-340` were therefore not merely examples; their `+/-1/2` normalized prime-block scale is the true global spectral scale.

The proof uses only positivity of the von-Mangoldt weights and the prime number theorem. It does not use zeta zeros, analytic continuation, prime-log Kronecker recurrence, or any RH input.

## 1. Outer shifts form one off-diagonal operator

Split

\[
I_-=(-1,0),
\qquad
I_+=(0,1),
\]

and decompose the source into

\[
\mathcal O_a=\{n:e^a\le n<e^{2a},\ \Lambda(n)>0\},
\qquad
\mathcal I_a=\{n:n<e^a,\ \Lambda(n)>0\}.
\tag{PL341-6}
\]

For every `n in O_a`, the lag satisfies `1<=h_n(a)<2`. Hence the zero-exterior compressed translation connects the two half-intervals and has no same-half block. If `T_a:L^2(I_-)->L^2(I_+)` denotes the oriented sum of those outer translations, then

\[
K_a^{\rm out}
=\begin{pmatrix}
0&T_a^*\\
T_a&0
\end{pmatrix},
\qquad
\|K_a^{\rm out}\|=\|T_a\|,
\tag{PL341-7}
\]

and its spectral edges are exactly `+/-||T_a||`.

The inner source is negligible on the outer PNT scale. From `||S_h+S_h^*||<=2`,

\[
\|K_a^{\rm in}\|
\le2\sum_{n<e^a}\frac{\Lambda(n)}{\sqrt n}
=O(e^{a/2+o(a)})
=o(e^a).
\tag{PL341-8}
\]

It therefore remains to determine `||T_a||` sharply.

## 2. A PNT-adapted weighted Schur test gives the upper bound

Let

\[
q_-(y)=e^{-a(1+y)/2},\qquad y\in I_-,
\]

\[
q_+(x)=e^{-a(1-x)/2},\qquad x\in I_+.
\tag{PL341-9}
\]

These are the two endpoint weights already selected by the PNT boundary scaling, now used as Schur weights rather than as fixed test profiles.

Write

\[
\Psi(X):=\sum_{n\le X}\Lambda(n).
\]

For `x in I_+`, the outer shifts that reach `x` have

\[
a\le\log n<a(1+x).
\]

For each such source,

\[
w_n q_-(x-h_n(a))
=rac{\Lambda(n)}{\sqrt n}
 e^{-a(1+x-h_n(a))/2}
=\Lambda(n)e^{-a(1+x)/2}.
\]

Hence

\[
\sum_n w_n q_-(x-h_n(a))
=e^{-a(1+x)/2}
\bigl(\Psi(e^{a(1+x)})-\Psi(e^a-)\bigr).
\tag{PL341-10}
\]

After division by `q_+(x)`, this is at most

\[
e^{-ax}\Psi(e^{a(1+x)}).
\tag{PL341-11}
\]

If

\[
\varepsilon_a:=
\sup_{X\ge e^a}
\left|\frac{\Psi(X)}{X}-1\right|,
\]

then the prime number theorem gives `varepsilon_a->0`, and therefore

\[
\sum_n w_n q_-(x-h_n(a))
\le(1+\varepsilon_a)e^a q_+(x).
\tag{PL341-12}
\]

The adjoint estimate is identical. For `y in I_-`, the admissible outer shifts obey `a<=log n<a(1-y)` and

\[
\sum_n w_n q_+(y+h_n(a))
\le(1+\varepsilon_a)e^a q_-(y).
\tag{PL341-13}
\]

The weighted Schur argument works directly for this finite sum of partial translations. Pointwise Cauchy--Schwarz with the first inequality, followed by integration, change of variables in each translated term, and the second inequality, gives

\[
\boxed{
\|T_a\|\le(1+\varepsilon_a)e^a
=e^a(1+o(1)).
}
\tag{PL341-14}
\]

No pair-correlation or short-interval prime estimate is used. The square-root weight `n^{-1/2}` is exactly what makes the exponential Schur factors cancel to the unweighted Chebyshev staircase `Psi`.

## 3. The same endpoint weights saturate the Schur bound

Normalize the two endpoint weights:

\[
f_a(y)=\left(\frac{a}{1-e^{-a}}\right)^{1/2}q_-(y),
\qquad
g_a(x)=\left(\frac{a}{1-e^{-a}}\right)^{1/2}q_+(x).
\tag{PL341-15}
\]

Then `||f_a||_2=||g_a||_2=1`. For one outer lag `h=log n/a`, put

\[
\delta_n=2a-\log n\in(0,a].
\]

The overlap of the translated endpoint layers has physical length `delta_n/a`, and the product of the two exponential profiles is constant on that overlap. A direct change of variables gives

\[
\langle g_a,S_{h_n(a)}f_a\rangle
=rac{\delta_n e^{-\delta_n/2}}{1-e^{-a}}.
\tag{PL341-16}
\]

Multiplication by `w_n=Lambda(n)e^{-a}e^{delta_n/2}` cancels the profile factor, so

\[
\langle g_a,T_af_a\rangle
=rac{e^{-a}}{1-e^{-a}}
\sum_{e^a\le n<e^{2a}}
\Lambda(n)(2a-\log n).
\tag{PL341-17}
\]

The remaining sum has a one-line PNT asymptotic. In Stieltjes form,

\[
\sum_{e^a\le n<e^{2a}}
\Lambda(n)(2a-\log n)
=
\int_{e^a}^{e^{2a}}
\log\!\left(\frac{e^{2a}}{t}\right)d\Psi(t).
\]

Integration by parts yields

\[
-a\Psi(e^a)
+
\int_{e^a}^{e^{2a}}\frac{\Psi(t)}{t}\,dt
=e^{2a}(1+o(1)),
\tag{PL341-18}
\]

because `Psi(t)=t(1+o(1))` uniformly for `t>=e^a` while `ae^a=o(e^{2a})`. Thus

\[
\langle g_a,T_af_a\rangle=e^a(1+o(1)),
\]

and hence

\[
\boxed{
\|T_a\|\ge e^a(1+o(1)).
}
\tag{PL341-19}
\]

Together with (PL341-14),

\[
\boxed{\|T_a\|=e^a(1+o(1)).}
\tag{PL341-20}
\]

The endpoint exponential pair therefore asymptotically saturates the global weighted Schur bound.

## 4. Sharp spectral edges of the prime and jump sectors

From (PL341-7),

\[
\sup\sigma(K_a^{\rm out})=\|T_a\|,
\qquad
\inf\sigma(K_a^{\rm out})=-\|T_a\|.
\]

The inner perturbation has norm `o(e^a)` by (PL341-8), so the variational principle gives

\[
\sup\sigma(K_a)=e^a(1+o(1)),
\qquad
\inf\sigma(K_a)=-e^a(1+o(1)),
\]

which is (PL341-2).

Classical partial summation from `Psi(x)~x` gives

\[
W_a
=\sum_{n<e^{2a}}\frac{\Lambda(n)}{\sqrt n}
=2e^a(1+o(1)).
\tag{PL341-21}
\]

Since `P_a=-K_a`, (PL341-4) follows. Since `J_a=2W_aI-K_a`,

\[
\inf\sigma(J_a)
=2W_a-\sup\sigma(K_a),
\qquad
\sup\sigma(J_a)
=2W_a-\inf\sigma(K_a),
\]

and (PL341-5) follows as well.

Thus the exact leading asymptotic is

\[
J_a\in
\left[\left(\frac32-o(1)\right)W_a,
      \left(\frac52+o(1)\right)W_a\right]
\]

at the level of spectral edges, while

\[
P_a\in
\left[-\left(\frac12+o(1)\right)W_a,
       \left(\frac12+o(1)\right)W_a\right]
\]

with both endpoint ratios attained asymptotically.

## 5. Adversarial audit and matched controls

**No hidden zero input.** The only arithmetic theorem used is `Psi(x)~x`. The argument stays entirely on the geometric/source side of the explicit formula and does not continue an Euler product or invoke the zero divisor.

**No illicit kernel-density step.** The outer operator is a finite sum of partial translations, not an integral operator with a Lebesgue density. The Schur estimate is applied in its discrete-kernel form and can be verified directly by pointwise Cauchy--Schwarz and change of variables. No atomic-to-continuum norm convergence is assumed; this is important because `PL-052`--`PL-053` show that such norm convergence is false.

**No conflict with the Kronecker norm defect.** `PL-052` shows that the atomic boundary operator does not converge in norm to its rank-one PNT strong limit. Equation (PL341-20) determines the norm of the raw outer block without asserting norm convergence to that rank-one operator. A family can keep high-frequency recurrent directions while its norm has the same leading value as the strong-limit model.

**Boundary normalization is load-bearing.** The factor `n^{-1/2}` in the Weil source is exactly matched by the half-exponential Schur weights. Replacing the source by a different power changes the natural endpoint weights and the scale. The result is therefore specific to the square-root-normalized Weil source, though not to the rational primes among systems sharing its PNT law.

**Matched generalized-prime control.** The proof uses only a positive atomic source measure with cumulative Chebyshev mass `Psi(X)=X(1+o(1))`. A Beurling/generalized-prime system satisfying the corresponding PNT reproduces the same leading `1/2`, `3/2`, and `5/2` constants. These constants are therefore PNT-universal geometry, not rational-prime RH rigidity.

**Endpoint choices and threshold atoms.** Whether the inequalities at `log n=a` or `log n=2a` are strict changes at most isolated source atoms and does not affect any displayed asymptotic. At `h=2` the compressed shift is zero; at `h=1` it is still purely off-diagonal up to null endpoints.

## 6. Prior-art and novelty assessment

The weighted Schur test is classical, the prime number theorem is classical, and the path/translation representation is already part of `PL-337`--`PL-339`. A targeted search around compressed translations, finite-interval Wiener--Hopf operators, von-Mangoldt Hankel operators, and Weil-form source blocks did not locate a published theorem stating the asymptotic spectral edges (PL341-2)--(PL341-5) for this localized prime block. Search absence is not treated as evidence of broad novelty.

The durable line-specific delta is exact and narrower: the PNT-adapted Schur weights close the factor-two gap left by `PL-339` and prove that the `PL-340` endpoint `+/-W_a/2` witnesses are asymptotically globally extremal. No new external source is required beyond the literature already registered for the localized Weil form and the classical PNT.

## Consequence for `prime_lattice`

The accumulated positive jump sector is stronger than `PL-339` could certify, but not strong enough in the only way that would matter for removing the prime sign problem:

\[
\boxed{
\inf\sigma(J_a)
=\left(\frac32+o(1)\right)W_a
<2W_a.
}
\]

Therefore the scalar compensation leaves a sharp negative prime-block edge

\[
\boxed{
\inf\sigma(P_a)
=-\left(\frac12+o(1)\right)W_a.
}
\]

This closes the route of obtaining asymptotic source positivity by sharpening channelwise jump coercivity alone. Any RH-facing sign mechanism must use information absent from this PNT-universal block estimate: the pole/archimedean completion, a source-selected branch constraint, a genuinely rational-prime relation, or another global coupling that changes which directions are admissible or energetically relevant. In particular, further improvements of the separate positive-jump lower bound cannot bridge the compensation gap, because the exact aggregate spectral edge is now fixed.

## Dependencies

- `PL-337`: exact decomposition of each prime-power source term as a positive jump plus scalar compensation.
- `PL-339`: exact compressed-shift path spectra, the first global PNT-scale jump coercivity bound, and the notation used here.
- `PL-340`: endpoint-layer witnesses at normalized prime-block scale `+/-1/2`; the present result proves their leading scale is globally sharp.
- `PL-051`--`PL-053`: PNT boundary model and high-frequency norm-defect controls, used only to audit topology and ensure no norm-convergence assumption is being smuggled into the Schur proof.
- Classical prime number theorem `Psi(x)~x` and Stieltjes partial summation, already within the line's prior-art surface.
