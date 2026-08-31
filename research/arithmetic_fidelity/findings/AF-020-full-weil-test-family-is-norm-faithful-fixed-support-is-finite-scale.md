# AF-020 — Full Weil test-family data are norm-faithful; fixed log-support is only finite-scale fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let

\[
Q=\{q_j\}_{j\ge1},\qquad 1<q_1\le q_2\le\cdots,\qquad q_j\to\infty,
\]

be a locally finite multiset of generator norms satisfying the Euler-product hypotheses of AF-017, and put

\[
\ell_j=\log q_j.
\]

Define the Weil-weighted prime-power measure on `(0,\infty)` by

\[
\boxed{
\omega_Q
=
\sum_j\sum_{m\ge1}
\ell_j e^{-m\ell_j/2}\,\delta_{m\ell_j}.
}
\]

For a compactly supported smooth test function `F`, write

\[
W_Q(F)=\int_0^\infty F(x)\,d\omega_Q(x).
\]

Then:

1. **The full test-function functional is faithful to the unordered generator-norm multiset.** Knowledge of `W_Q(F)` for every `F\in C_c^\infty(0,\infty)` determines `\omega_Q`, and `\omega_Q` determines `Q` with multiplicity.

2. **A fixed support bound has an exact arithmetic horizon.** For `A>0`, knowledge of `W_Q(F)` for every test supported in `(0,A)` determines exactly the submultiset
   \[
   \boxed{Q_{<e^A}=\{q_j:q_j<e^A\},}
   \]
   and contains no information about generators `q_j\ge e^A`.

3. Consequently, two systems `Q` and `R` have identical bounded-support functionals
   \[
   W_Q(F)=W_R(F)
   \qquad
   \forall F\in C_c^\infty(0,A)
   \]
   if and only if their generator multisets agree below `e^A`.

4. The support-indexed family is therefore a genuine **fidelity filtration**:
   \[
   \mathcal W_A(Q)
   \preceq
   \mathcal W_B(Q)
   \qquad(A<B),
   \]
   where increasing the support radius reveals additional generator norms, and the union over unbounded `A` recovers all of `Q`.

5. In the Guinand--Weil explicit formula, the prime side has precisely this structure, up to the conventional symmetrization `F(x)+F(-x)` and fixed nonzero normalizing factors. Thus a proof regime that restricts the prime-side transform to one fixed compact log-support cannot by itself be globally rational-prime-norm faithful: it is blind to arbitrary changes in generators above its arithmetic horizon. Allowing the complete unbounded test family removes that particular loss.

The conclusion is category-specific. It does **not** say that a zero divisor alone determines the prime-power functional. AF-017 and AF-019 show why: a zero-free analytic factor can preserve the divisor while changing the regular part of the logarithmic derivative. Recovering `W_Q` from a zero-side formula therefore also requires the nonzero-divisor terms of the explicit formula to be fixed or independently controlled.

## Prime-power measure and exact logarithmic derivative

AF-019 gives, in an absolute-convergence half-plane,

\[
-\frac{Z_Q'(s)}{Z_Q(s)}
=
\sum_j\sum_{m\ge1}
\ell_j e^{-sm\ell_j}.
\]

If

\[
\mu_Q
=
\sum_j\sum_{m\ge1}\ell_j\,\delta_{m\ell_j},
\]

then this is simply the Laplace transform

\[
-\frac{Z_Q'(s)}{Z_Q(s)}
=
\int_0^\infty e^{-sx}\,d\mu_Q(x).
\]

The measure used in the symmetric Weil formula is the fixed reweighting

\[
d\omega_Q(x)=e^{-x/2}\,d\mu_Q(x).
\]

Because `e^{-x/2}` is known and nowhere zero, multiplication by this weight is invertible and cannot itself lose support or multiplicity information.

Local finiteness of `Q` implies local finiteness of both `\mu_Q` and `\omega_Q`: on a bounded interval `0<x\le A`, only finitely many generators satisfy `\ell_j\le A`, and for each such generator only finitely many multiples `m\ell_j\le A` occur.

Thus `\omega_Q` is a locally finite positive atomic measure and defines a distribution by test-function pairing.

## Full test-family recovery

A locally finite measure is determined by its action on `C_c^\infty(0,\infty)`. Therefore equality

\[
W_Q(F)=W_R(F)
\qquad
\forall F\in C_c^\infty(0,\infty)
\]

implies

\[
\omega_Q=\omega_R.
\]

It remains to check that prime-power collisions such as

\[
\log 4=2\log 2
\]

do not prevent recovery of the underlying generator multiset.

Remove the known Weil damping and, for `x>0`, define

\[
b_Q(x)
=
\frac{e^{x/2}\omega_Q(\{x\})}{x}.
\]

Let

\[
n_Q(y)=\#\{j:\ell_j=y\}
\]

be the multiplicity of `y` as a generator logarithm. At an atom `x`, every contribution is of the form `x=m\ell_j`, so

\[
\begin{aligned}
b_Q(x)
&=
\frac1x
\sum_{m\ge1\,:\,x/m\in\{\ell_j\}}
\frac{x}{m}\,n_Q(x/m)\\
&=
\boxed{
\sum_{m\ge1}\frac{1}{m}n_Q(x/m).
}
\end{aligned}
\]

The coefficient sequence `1/m` has Dirichlet inverse `\mu(m)/m`, where `\mu` is the ordinary Möbius function. Hence dilation-Möbius inversion gives

\[
\boxed{
n_Q(x)
=
\sum_{m\ge1}\frac{\mu(m)}{m}\,b_Q(x/m).
}
\]

For each fixed `x` this sum is finite: if `\ell_1` is the smallest generator logarithm, then `b_Q(x/m)=0` once `x/m<\ell_1`.

Indeed, substituting the expression for `b_Q` yields

\[
\sum_{m,k\ge1}
\frac{\mu(m)}{mk}
 n_Q\!\left(\frac{x}{mk}\right)
=
\sum_{r\ge1}
\frac{n_Q(x/r)}{r}
\sum_{m\mid r}\mu(m)
=n_Q(x).
\]

Therefore the complete prime-power measure recovers every generator logarithm and its multiplicity, even when different prime powers land on the same point. Exponentiating recovers `Q`.

This is the distributional analogue of AF-017's recovery from the exact Euler product and AF-019's recovery from the exact logarithmic derivative.

## Fixed support gives exact finite-scale fidelity

Fix `A>0` and retain only

\[
\mathcal W_A(Q)
=
\{W_Q(F):F\in C_c^\infty(0,A)\}.
\]

This determines exactly the restriction

\[
\omega_Q\big|_{(0,A)}.
\]

For every `x<A`, the Möbius reconstruction of `n_Q(x)` uses only values

\[
b_Q(x/m),
\qquad
x/m\le x<A.
\]

Thus the restricted measure reconstructs all generator logarithms `\ell_j<A`, equivalently all norms

\[
q_j<e^A.
\]

Conversely, a generator with `\ell_j\ge A` contributes atoms only at

\[
m\ell_j\ge A,
\qquad m\ge1,
\]

so it contributes nothing to any test supported in `(0,A)`. One may therefore alter, insert, delete, or rearrange arbitrarily many generators above `e^A` without changing `\mathcal W_A` at all, subject only to the ambient local-finiteness/convergence assumptions.

Hence

\[
\boxed{
\mathcal W_A(Q)=\mathcal W_A(R)
\iff
Q_{<e^A}=R_{<e^A}
\text{ as multisets}.
}
\]

This is stronger than the vague statement that compact support sees only finitely many prime powers. The bounded-support destination has a complete mathematical classification: it is faithful to the generator system **below one explicit norm horizon and completely blind above it**.

## Placement inside the Guinand--Weil explicit formula

In a standard symmetric form of the explicit formula, the prime contribution contains terms of the shape

\[
\sum_{p}\sum_{m\ge1}
(\log p)p^{-m/2}
\bigl(F(m\log p)+F(-m\log p)\bigr),
\]

with the remaining side consisting of zero, pole, and archimedean terms according to the chosen normalization.

The positive-log part is exactly the functional of `\omega_{\mathbb P}` above. Evenness or the displayed symmetrization does not create a new loss on the positive half-line: compactly supported smooth functions away from zero can be extended to admissible even tests, and the prime-power support is bounded away from zero because the smallest generator is larger than one.

If `F` is restricted to support in `(-A,A)`, then only prime powers satisfying

\[
m\log p<A
\iff
p^m<e^A
\]

can appear. The theorem above shows that the complete family of all such tests still recovers every base prime `p<e^A`, despite prime-power collisions, but no prime `p\ge e^A`.

This gives a precise Arithmetic Fidelity interpretation of the familiar Fourier-support restrictions used in explicit-formula arguments: a fixed support restriction is not only an analytic limitation on which sums can be estimated. It is an **exact truncation of the prime-norm discriminator at a corresponding logarithmic scale**.

When the support parameter itself grows without bound and every compact region is eventually probed, this particular obstruction disappears because the distributional functional determines the whole prime-power measure.

## Relation to zero-side and residue-only compressions

It is essential not to identify the full test-family functional with the zero divisor.

AF-019 separated

\[
\text{exact logarithmic derivative}
\longrightarrow
\text{principal parts/divisor}
\]

and showed that the latter discards the holomorphic logarithmic derivative of a zero-free factor. The Guinand--Weil formula is derived from the exact logarithmic derivative together with contour motion, functional-equation/gamma data, and boundary/decay conditions. Its full distributional identity can therefore retain information that a residue list alone does not.

Accordingly, the implication

\[
\text{all prime-side test pairings}
\Longrightarrow Q
\]

proved here must not be reversed into

\[
\text{zero divisor}
\Longrightarrow Q
\]

without additional hypotheses. Grosswald--Schnitzer remain a direct counterexample at the divisor layer.

If a route claims that its zero-side representation determines the full prime-side functional, the fidelity burden is to prove that the archimedean, normalization, boundary, and zero-free regular terms are fixed in the declared category. AF-018 gives one example of such rigidity for completed order-one entire functions with a common reflection symmetry and normalization; AF-019 gives another at the exact-log-derivative layer.

## Prior art and novelty assessment

The ingredients are classical.

- A. P. Guinand, **“A Summation Formula in the Theory of Prime Numbers,”** *Proceedings of the London Mathematical Society* s2-50 (1948), 107--119, DOI `10.1112/plms/s2-50.2.107`, is classical test-function explicit-formula prior art.
- André Weil, **“Sur les ‘formules explicites’ de la théorie des nombres premiers,”** *Comm. Sém. Math. Univ. Lund*, Tome Supplémentaire (1952), 252--265, is the foundational general explicit-formula reference in which prime powers and zeros are paired through transform-related test functions.
- H.-J. Besenfelder, **“Die Weilsche ‘Explizite Formel’ und temperierte Distributionen,”** *Journal für die reine und angewandte Mathematik* 293/294 (1977), 228--257, is direct prior art for treating Weil's explicit formula distributionally.
- H. Iwaniec, W. Luo, and P. Sarnak, **“Low lying zeros of families of L-functions,”** *Publications Mathématiques de l'IHÉS* 91 (2000), 55--131, DOI `10.1007/BF02698741`, is a standard modern example of explicit-formula arguments whose arithmetic reach is controlled by Fourier-support restrictions.

No novelty is claimed for the Guinand--Weil formula, distributional uniqueness, compact-support truncation, or Möbius inversion in isolation. The Arithmetic Fidelity contribution is the **exact category classification** obtained by combining them with AF-017/AF-019: the full prime-side test distribution is norm-faithful, whereas a fixed log-support class is faithful exactly up to `e^A` and has an arbitrarily large same-destination fiber above that horizon.

This is a fidelity theorem and obstruction, not a new explicit formula and not evidence for RH.

## Boundaries and failure modes

- The theorem inherits AF-017's locally finite generator multiset and exact Euler-factor setting. More general local factors with independent coefficients require a separate identifiability theorem.
- The weight `e^{-x/2}` is harmless only because it is known and nowhere zero. Unknown or vanishing local weights can introduce additional fibers.
- The support statement uses the complete family of tests in `C_c^\infty(0,A)`, not one test, finitely many moments, or a finite-dimensional test subspace. Those coarser destinations may lose information even below `e^A`.
- The threshold is strict because tests are supported in `(0,A)`. A convention that includes the boundary must audit atoms exactly at `x=A` separately.
- Equality of prime-side distributions does not recover labels, prime order, additive structure of the integers, splitting provenance, or any richer upstream arithmetic relation beyond the unordered norm multiset.
- A fixed-support zero statistic can contain other arithmetic information through family averaging, conductors, gamma factors, coefficients, or an independently supplied model. The no-go here is specifically against recovering generator norms that never enter the retained prime-side support.
- The full explicit formula contains archimedean and normalization terms. Equality of zero locations alone does not imply equality of the full test functional unless those other terms are fixed by independent hypotheses.
- No claim here constrains the location, multiplicity, or simplicity of zeta zeros.

## Decisive audit test

For any explicit-formula, trace-formula, density, or positivity route that imposes a support restriction:

1. identify the exact log-variable tested on the arithmetic side and its normalization;
2. translate the allowed support into the corresponding generator-norm horizon;
3. determine whether the route has the **whole** test family inside that support or only a smaller finite/positive/quadratic cone;
4. construct a matched control that agrees on all generators below the horizon and changes them above it;
5. verify whether any independently retained boundary, normalization, archimedean, or operator data distinguish that control;
6. only then claim global rational-prime specificity.

If no additional retained datum sees beyond the fixed support horizon, the route cannot be globally norm-faithful. If the support family grows without bound, that particular objection no longer applies and the next compression layer must be audited instead.

## Consequence for the line

Treat test-function support as a **fidelity scale**, not merely an analytic convenience.

The arithmetic chain is now refined to

\[
\boxed{
Q
\longrightarrow
Z_Q
\longrightarrow
-Z_Q'/Z_Q
\longrightarrow
\omega_Q
\longrightarrow
\mathcal W_A(Q).
}
\]

Under the stated hypotheses, the first four layers are faithful to the unordered norm multiset. The last layer is faithful exactly below `e^A` and forgets everything above it.

This supplies a reusable audit for support-limited explicit-formula and positivity arguments: before asking whether a later global operation can select rational primes, first check whether the allowed test class ever received the prime-norm information at the scales the claimed discriminator requires.