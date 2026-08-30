# PC-054 — the cotangent dilation-Gram completion is classical

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-REDIRECTION` + `DECISIVE-NEGATIVE` for treating the nearest known RH/GRH-positive **one-dimensional common-anchor cotangent dilation/Gram construction** as a new prime-circle mechanism. PC-011 identifies the common-anchor chord intercept field with cotangents and already redirects its first multiplicative moments to Dedekind/Vasyunin theory. PC-048–PC-053 then leave genuinely cross-scale Gram/dilation constructions outside their finite-level cotangent no-go results. The present finding audits that explicit escape route: the standard Hilbert-space completion in which rational cotangent sums become entries of a scale Gram matrix is exactly the classical Nyman–Beurling/Vasyunin/Lewis–Zagier territory. In the Lewis–Zagier model the cotangent entries are literally weighted common-anchor chord intercepts, while the critical half-plane is supplied by the external `L^2`/Mellin setup rather than by the circle geometry.

This does **not** prove that every possible multi-level prime-circle Gram operator is classical. It rules out a specific but important novelty claim: taking the one-dimensional anchored cotangent profile, inserting the standard square-wave/fractional-part dilation family and Gram determinant, and then pointing to the resulting RH/GRH criterion as a new geometric bridge.

## 1. Prime-circle chord intercepts are the cotangent atoms

For the regular `q`-gon with common vertex `1`, PC-011 gives the exact supporting-line equation for the chord from `1` to `zeta_q^k`. Its intercept on the vertical diameter is

\[
\boxed{
y_{q,k}=\cot\frac{\pi k}{q}.
}
\]

Thus every finite cotangent value at a rational angle is already a literal scalar observable of the original prime-circle drawing. In particular,

\[
\boxed{
\cot\frac{\pi k}{4n}=y_{4n,k}.
}
\]

This observation is elementary but important for the novelty audit below: when a known RH-related matrix is written as a finite sum of `cot(pi k/q)`, its entries can indeed be realized by the common-anchor chord fan without adding hyperbolic geometry.

The issue is therefore not whether the prime circle can *realize* those cotangent sums. It can. The issue is whether the scale organization that makes them RH-relevant is forced by the prime-circle geometry or is already an external classical construction.

## 2. Lewis–Zagier Gram entries are exact weighted sums of prime-circle chord intercepts

Lewis and Zagier fix the primitive odd character modulo `4`,

\[
\chi_4(k)=
\begin{cases}
(-1)^{(k-1)/2},&k\text{ odd},\\
0,&k\text{ even},
\end{cases}
\]

and a periodic square-wave function `S`. For positive integers `m,n` they define numbers `c_{m,n}` and split them as

\[
\boxed{
c_{m,n}=h_{m,n}+h_{n,m}.}
\]

Their finite cotangent formula is

\[
\boxed{
h_{m,n}
=
\sum_{k=1}^{2n-1}
\chi_4(k)
S\!\left(\frac{km}{n}\right)
\cot\!\left(\frac{\pi k}{4n}\right).}
\]

Substituting the prime-circle intercept identity gives the exact geometric rewriting

\[
\boxed{
h_{m,n}
=
\sum_{k=1}^{2n-1}
\chi_4(k)
S\!\left(\frac{km}{n}\right)
y_{4n,k}.}
\]

Hence `c_{m,n}` is a symmetric cross-scale linear combination of common-anchor chord intercepts from the levels `4m` and `4n`, with a completely explicit arithmetic selection rule. No analogy is involved: the cotangent atoms in the Lewis–Zagier matrices are exactly prime-circle chord-intercept values.

This also exposes the additional structure that is **not** supplied merely by drawing the regular polygons: the modulo-`4` character, the square-wave selector and the particular cross-scale weighting are extra choices.

## 3. The determinant mechanism is a classical dilation Gram problem

Lewis–Zagier also give the integral identity

\[
\boxed{
c_{m,n}
=
\frac{4}{\pi}
\int_0^\infty
S(mt)S(nt)\,\frac{dt}{t^2}.}
\]

Set

\[
G(x)=S(1/x),
\qquad
G_a(x)=G(x/a)=S(a/x),
\qquad 0<a\le1,
\]

as functions in `L^2(0,1)`. For a fixed `N`, let

\[
\mathcal V_N
=
\operatorname{span}\{G_{n/N}:1\le n\le N\}.
\]

Then their Gram matrix satisfies exactly

\[
\boxed{
\left\langle G_{m/N},G_{n/N}\right\rangle
=
\frac{\pi}{4N}\,c_{m,n}.}
\]

Therefore a determinant built from the matrix `(c_{m,n})_{1\le m,n\le N}` is not a new spectral wrapper waiting to be discovered from the prime circle. It is, up to a scalar normalization, the Gram determinant of a classical family of multiplicative dilates.

The corresponding distance of the constant function `xi=1_(0,1]` from `\mathcal V_N` is a ratio of the augmented and unaugmented Gram determinants. Lewis–Zagier prove that the asymptotic behavior of this ratio is equivalent to the zero-free half-plane required by GRH for the relevant odd real Dirichlet `L`-series. This is exactly the sort of cross-level determinant route that remained outside PC-049–PC-053, but it is already established prior art.

## 4. The critical `1/2` comes from the chosen Hilbert/Mellin geometry

The decisive diagnostic is where the complex variable and the critical boundary enter.

For

\[
\mathsf p_s(x)=x^{s-1},
\]

one has

\[
\boxed{
\mathsf p_s\in L^2(0,1)
\iff
\operatorname{Re}s>\frac12.}
\]

Moreover Lewis–Zagier compute the Mellin coefficient

\[
\boxed{
\left\langle \mathsf p_s,G_a\right\rangle
=
\frac{a^s}{s}L(s),}
\]

where `L(s)` is the Dirichlet `L`-series attached to the selected odd character. Thus a zero `L(rho)=0` with `Re(rho)>1/2` produces a vector `p_rho` orthogonal to the entire dilation space, obstructing approximation of `xi`.

This identifies the provenance of the critical line in this construction:

\[
\boxed{
\operatorname{Re}s=\frac12
\text{ is the }L^2(0,1)\text{ integrability boundary of }x^{s-1}.}
\]

The prime-circle chord geometry supplied the cotangent atoms, but it did **not** by itself supply the measure `dx`, the multiplicative dilation representation, the monomials `x^{s-1}`, or the square-wave whose Mellin transform is the chosen `L`-series. Those are precisely the functional-analytic ingredients that make the known criterion work.

Consequently, rediscovering the half-line through this Gram completion would not explain why the original roots-of-unity geometry intrinsically selects `1/2`; it would import the selector from a classical Beurling/Mellin setting.

## 5. Relation to the zeta-specific Vasyunin branch

Lewis–Zagier's theorem is stated for odd real Dirichlet characters, so it must not be silently promoted to a theorem about the Riemann zeta function itself. The zeta-specific nearby route is the classical Nyman–Beurling/Báez-Duarte framework based on dilates of the fractional-part function.

That boundary was already encountered geometrically in PC-011. The first angular moment of the common-anchor cotangent field gives the standard Vasyunin/cotangent sums, and those sums are exactly among the arithmetic forms that occur in the Nyman–Beurling analysis and in the multiplicative autocorrelation of the fractional-part function.

The two prior-art boundaries therefore line up cleanly:

\[
\boxed{
\begin{array}{c}
\text{anchored cotangent moments}\\
\downarrow\\
\text{Vasyunin / Nyman--Beurling for }\zeta
\end{array}
\qquad
\begin{array}{c}
\text{anchored cotangent sums + square-wave dilations}\\
\downarrow\\
\text{Lewis--Zagier Gram determinants for odd }L(s,\chi)
\end{array}}
\]

So cotangent data can certainly participate in genuine RH/GRH criteria. The negative conclusion is about **novelty and provenance**, not relevance: the known successful scale completion is already classical and its spectral parameter is introduced by the dilation/Mellin Hilbert space.

## 6. Why PC-048–PC-053 do not contradict the positive classical criteria

The recent cotangent findings classify intrinsic finite-level and power-map-refinement operators:

- PC-048 reduces the raw old/new shell coefficients at odd squarefree level to fixed `L(0)` / generalized-Bernoulli data;
- PC-049–PC-050 show that canonical fiber pushforward is commuting, invertible and radical-invariant after averaging;
- PC-051–PC-053 show that retaining complete preimage fibers or entire divisor-shell tubes gives only affine spectral inflation of base cotangent data.

Lewis–Zagier do something different. They do **not** take the spectrum of one prime-circle cotangent matrix, nor the power-map fiber pushforward `R H R*`, nor the full preimage-tube operator. They first build a family of scale-dilated functions in an infinite-dimensional Hilbert space and then take their Gram determinants as the number of scales grows.

Therefore their result is not a counterexample to PC-048–PC-053. It is instead the exact prior-art boundary those findings deliberately left open. The audit shows that simply moving from the finite cotangent matrices to the standard dilation Gram completion does not create a new prime-circle program; it moves into an existing one.

## 7. Decisive negative conclusion and surviving frontier

The following route cannot be advertised as a new prime-circle bridge:

\[
\boxed{
\text{common-anchor chord intercepts}
\to
\text{standard cotangent/Vasyunin or square-wave scale weights}
\to
\text{multiplicative dilation Gram matrix}
\to
\text{RH/GRH determinant criterion}.}
\]

At the scalar level it is the classical Vasyunin/Nyman–Beurling family already identified in PC-011; at the explicit Hilbert-Gram level the closest positive cotangent construction is Lewis–Zagier. The fact that their entries can be drawn as prime-circle chord intercept sums is a useful geometric interpretation, but not a new RH mechanism.

A genuinely surviving cross-scale prime-circle route must derive something that is **not** equivalent to selecting one of these known functional-analytic completions. In particular it would need an intrinsically justified multi-level state space, inner product or nonlocal coupling whose complex parameter and critical symmetry arise from the birth/refinement geometry itself rather than from a prechosen square wave, fractional-part function, character, Mellin measure, or `L^2` dilation representation.

This leaves open, among other things:

- a multi-level operator that retains primitive-shell geometry in more than the one-dimensional chord-intercept field;
- nonlinear coupling of several birth labels before any scalar cotangent reduction;
- a cross-level Gram construction whose kernel is forced by the two-dimensional harmonic fields `U_n(z)` rather than by a prescribed fractional-part/square-wave test function;
- and the global primitive-root uniformization/monodromy direction of PC-017.

## 8. Prior-art audit and falsification tests

The principal source is John Lewis and Don Zagier, **Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis**, *Research in the Mathematical Sciences* **6** (2019), Article 4, DOI `10.1007/s40687-018-0159-8`, already anchored in `research/prime_circle/SOURCES.md`. Their paper explicitly provides the finite cotangent formula, the square-wave integral representation, the dilation Gram identity, the Mellin transform `a^s L(s)/s`, and the GRH equivalence. PC-011 records the older Nyman–Beurling/Vasyunin boundary for the Riemann-zeta version of the story.

No novelty claim is made for any of those ingredients. The durable prime-circle result is the exact provenance statement: **the nearest known RH-positive one-dimensional cotangent Gram completion can be represented by common-anchor chord intercepts, but the scale/Hilbert structure that creates the critical half-plane is classical external machinery.**

The classification has direct checks:

1. verify `y_{q,k}=cot(pi k/q)` from the anchored chord equation;
2. substitute `q=4n` into the Lewis–Zagier finite formula and recover `h_{m,n}` as the displayed weighted sum of prime-circle intercepts;
3. verify `c_{m,n}=h_{m,n}+h_{n,m}`;
4. use their integral representation to check `\langle G_{m/N},G_{n/N}\rangle=(pi/(4N))c_{m,n}`;
5. calculate `\int_0^1 |x^{s-1}|^2 dx` and recover the exact boundary `Re(s)>1/2`;
6. Mellin-transform `G_a` and recover `a^sL(s)/s`.

Failure of any of these equalities would invalidate the exact identification. The finding does **not** assert that every possible prime-circle multi-level Gram operator is of Nyman–Beurling/Lewis–Zagier type, nor that a genuinely two-dimensional shell-dependent construction cannot carry new information.