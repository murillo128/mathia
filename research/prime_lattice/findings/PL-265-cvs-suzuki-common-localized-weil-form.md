# PL-265 — CvS and Suzuki already represent the same localized Weil form

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PRIOR-ART-REDIRECT + CLUE-RESOLUTION`

## Claim

The bridge proposed in `CLUE-localized-weil-multi-edge-bridge` is **not a missing transform between two different arithmetic objects**. At the quadratic-form level, the finite Connes--van Suijlekom/Connes--Consani--Moscovici truncation and Suzuki's localized screw-function operator are representations of the same completed localized Weil form, with the exact parameter identification

\[
\lambda=e^a,\qquad c=\lambda^2=e^{2a},\qquad L=\log c=2a.
\]

Here `a` is Suzuki's additive support radius, `lambda` is the multiplicative semilocal radius used by Connes--Consani--Moscovici, `c` is the prime-power cutoff used by the finite CvS path, and `L` is the diameter of the additive support window. Thus

\[
[-L/2,L/2]=[-a,a],
\]

and both constructions use exactly the von-Mangoldt atoms with

\[
\log q\le 2a
\quad\Longleftrightarrow\quad
q\le e^{2a}=c.
\]

Consequently, on the corresponding finite Galerkin test family, the CvS matrix is already the restriction of the same unshifted Weil quadratic form represented in the continuum by Suzuki's self-adjoint operator `A_a`. No Schur complement, spectral shift, or extra sign-comparison constant is needed merely to pass from the accumulated multi-edge source to the localized Weil form.

This resolves the clue's **bridge-construction question** by prior art and exact parameter matching. It does **not** solve the RH-facing sign problem. The remaining burden is to prove the unshifted localized form nonnegative, or to control a genuinely new limit/invariant that forces that sign. Finite-dimensional tracking of the *location* of the first radius at which the ground state crosses zero also requires quantitative control beyond the form identity.

## 1. The multiplicative and additive localizations are the same window

Connes--Consani--Moscovici formulate the semilocal construction on

\[
[\lambda^{-1},\lambda]
\]

with the prime cutoff

\[
x=\lambda^2.
\]

Suzuki explicitly reformulates their closed localized Weil form on the additive interval

\[
[-a,a],\qquad a=\log\lambda,
\]

and denotes it by `Q_W^a`. He records the canonical lower-bounded self-adjoint representative `A_a` through

\[
Q_W^a(v)=\langle A_a v,v\rangle.
\]

Therefore the multiplicative cutoff becomes

\[
x=\lambda^2=e^{2a}.
\]

This is exactly the cutoff denoted `c` in the finite CvS path used in `PL-264`. Equivalently, if that path uses additive length

\[
L=\log c,
\]

then

\[
L=2a,
\]

so the CvS Hilbert interval `[-L/2,L/2]` is literally Suzuki's `[-a,a]`.

The identity is not a heuristic matching of scales. It is the ordinary logarithmic change of variables between the multiplicative semilocal interval and the additive support interval of the completed Weil form.

## 2. The prime-power source cutoff also agrees exactly

The same relation follows directly from Suzuki's screw kernel, independently of notation. His continuous function `g(t)` contains the arithmetic term

\[
\sum_{n\le e^{|t|}}
\frac{\Lambda(n)}{\sqrt n}\bigl(|t|-\log n\bigr).
\]

When the localized kernel is evaluated on `x,y in [-a,a]`, every difference satisfies

\[
|x-y|\le 2a.
\]

Hence no arithmetic atom with

\[
n>e^{2a}
\]

can enter the localized operator. Since `Lambda(n)` is supported on prime powers, its complete non-archimedean source is exactly

\[
\{q=p^r:q\le e^{2a}\}.
\]

In prime-exponent coordinates this is

\[
\{r e_p:r\log p\le 2a\}.
\]

That is the same accumulated edge set in `PL-264` at CvS cutoff `c=e^{2a}`. The local rank-one shocks isolated there are therefore the event-by-event singular increments of a source path whose **fully accumulated value at `L=2a` is already the localized Weil form**. The many-edge coupling and the pole/archimedean completion are not a second object awaiting a bridge; they are the source decomposition of the target form itself.

Endpoint conventions (`<` versus `<=`) depend on whether one works with compactly supported smooth test functions or the closed form at the boundary. They do not alter the parameter identity or the source horizon.

## 3. What is exact at finite Galerkin level

The CvS finite matrix is obtained by evaluating the real even distribution defining the truncated Weil quadratic form on a finite Fourier/Galerkin family. Therefore, after the standard logarithmic/unitary identification of the interval, its quadratic value has the form

\[
v^*Q_N(c)v
=
Q_W^a(f_v),
\qquad c=e^{2a},
\]

for the associated finite test function `f_v`.

This is the strongest sign comparison the clue could ask for on that common finite family: the comparison constant is exactly one. A negative direction of the finite matrix is a negative direction of the same unshifted Weil form, and conversely within that Galerkin subspace. There is no need to manufacture positivity by replacing the form with a shifted pencil; `PL-263` remains the control showing why such shifting would destroy the RH-sensitive orientation.

One should **not** strengthen this statement to the literal operator equality

\[
Q_N(c)=P_N A_a P_N
\]

without specifying domains and the chosen form realization. `A_a` is the Friedrichs/self-adjoint representative of the closed continuum form, whereas `Q_N(c)` is a finite form compression. The safe exact statement is equality of quadratic-form values on the identified finite test subspace.

`PL-261` already supplies the relevant completeness theorem for the Connes--Consani Laurent core: at fixed semilocal scale, the lowest finite-compression eigenvalues converge downward to the lower bound of the closed form. Thus no additional bridge is needed to ensure existential detection of a negative continuum direction either.

## 4. The first-crossing problem is not automatically finite-dimensional

Suzuki proves that the lowest spectral value `lambda_a` of `A_a` is continuous in `a`, is positive for sufficiently small `a`, and becomes negative for some finite `a` if RH fails. Hence a failure of RH produces a finite degeneracy/crossing radius in the **continuum localized family**.

The common-form identification preserves this information at the source level, but it does not by itself prove that a fixed finite Galerkin dimension locates the same crossing radius, nor that the finite crossing radii converge uniformly as `N` grows. Pointwise form-core convergence at each fixed radius is weaker than the uniform-in-`a` estimate needed to track the first crossing without drift.

This is the precise residue of the clue's phrase "first-crossing information." The transform/comparison part is already classicalized; a quantitative moving-radius Galerkin theorem would be a separate result. Likewise, `PL-262` remains the relevant warning for any subsequent passage that tries to turn expanding-window Hilbert-space control into locally uniform analytic information in the strip.

## 5. Matched-control and sign audit

The common-form identity does not create an RH mechanism. If the von-Mangoldt weights are replaced by another finite set of source weights while the same support geometry and one-edge rank-one jets are retained, the same construction still produces a localized real distribution, a Galerkin form, and a corresponding continuum form. What changes is the global signed arithmetic content, not the existence of the bridge.

This sharpens the lesson of `PL-264`: the universal one-edge jet is too weak, and accumulating those edges does not become informative merely because one rewrites the accumulated object in Suzuki's screw-function coordinates. The only RH-sensitive statement is still the sign of the **specific completed zeta Weil form** (or a source-forced consequence strong enough to imply that sign).

Thus the bridge is useful organizationally but mathematically neutral with respect to RH:

\[
\text{CvS accumulated source path}
\quad=\quad
\text{finite/Galerkin representation of }Q_W^a
\quad\leftrightarrow\quad
A_a,
\]

where the equal sign means equality of the identified quadratic form and the final arrow means passage to its canonical self-adjoint representative, not equality of finite and infinite operators.

## 6. Analytic-continuation boundary

No Euler product is continued into the critical strip in this argument. The common object is the **completed Weil quadratic form**, whose pole, archimedean place, functional equation, and zero divisor have already been incorporated through the explicit formula.

The finite prime cutoff arises from support: localizing to `[-a,a]` makes the autocorrelation/difference variable live in `[-2a,2a]`, so only `q<=e^{2a}` can contribute. Suzuki's formula for `g(t)` displays the same cutoff directly. The parameter match therefore survives analytic continuation because it is a statement about the completed explicit-formula distribution, not about truncating the Euler product outside `Re(s)>1`.

## 7. Prior-art and novelty audit

The decisive literature anchor is already source 56 in `research/prime_lattice/SOURCES.md`:

- **Masatoshi Suzuki**, “Weil's quadratic form via the screw function,” arXiv:`2606.09096v2` (revised 17 August 2026). Suzuki states that his framework unifies the localized Weil results of Yoshida, Bombieri, Connes--Consani, and Connes--Consani--Moscovici; explicitly rewrites the latter's multiplicative interval using `a=log lambda`; identifies `Q_W^a` with the closed localized form represented by `A_a`; and gives the screw kernel whose arithmetic sum is cut off by `n<=exp(|t|)`.

Source 28 in the same registry, **Connes--Consani--Moscovici, “Zeta spectral triples”**, supplies the complementary semilocal normalization: the construction on `[lambda^{-1},lambda]` uses Euler-prime data through `x=lambda^2`.

`PL-264` already stores and audits the finite CvS path and its exact von-Mangoldt edge increments. Combining these established pieces yields

\[
c=x=\lambda^2=e^{2a},\qquad L=\log c=2a.
\]

The parameter synthesis is immediate once the notations are placed side by side and is **not claimed as a new theorem**. The durable result is a prior-art redirect: the local clue treated the CvS accumulation and Suzuki localization as potentially different objects requiring a new source-defined bridge, but the literature shows that they are two realizations of the same localized completed Weil form.

No additional literature entry is required for this finding because the two external anchors that establish the identification are already registered as sources 28 and 56.

## 8. Falsification and remaining live target

This finding would be materially falsified or narrowed by any of the following:

1. the CCM prime horizon at multiplicative radius `lambda` were not `lambda^2`;
2. Suzuki's variable `a` were not the logarithmic radius `log lambda`;
3. the CvS path in `PL-264` used a different completed distribution rather than the same truncated Weil distribution;
4. the finite matrix quadratic values failed to equal the restricted Weil quadratic form on their defining Galerkin family.

The cited constructions and the stored derivation of `PL-264` exclude these possibilities under the stated normalizations.

What remains open is substantially sharper. The line no longer needs to search for an abstract multi-edge transform from CvS to Suzuki. It needs a **source-forced sign theorem or a quantitative crossing/limit theorem** for the common unshifted form. A useful successor must therefore do at least one of the following: derive nonnegativity from arithmetic structure not already equivalent to Weil positivity; obtain quantitative uniform control of finite Galerkin ground states as `a` and `N` vary; or produce a new invariant of the accumulated prime-power path that is not preserved by matched non-zeta source controls and that forces the unshifted Weil orientation.

The clue `CLUE-localized-weil-multi-edge-bridge` is therefore resolved as a bridge-construction question, while its deeper motivation—the missing reason the exact zeta source should have the correct global sign—remains the central RH-facing problem.
