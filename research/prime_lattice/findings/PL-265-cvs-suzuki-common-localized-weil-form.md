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
\log q\le2a
\quad\Longleftrightarrow\quad
q\le e^{2a}=c.
\]

Consequently, on the corresponding finite Galerkin test family, the CvS matrix evaluates the restriction of the same unshifted Weil quadratic form represented in the continuum by Suzuki's self-adjoint operator `A_a`. No Schur complement, spectral shift, or extra sign-comparison constant is needed merely to pass from the accumulated multi-edge source to the localized Weil form.

This resolves the clue's **bridge-construction question** by prior art and exact parameter matching. It does **not** solve the RH-facing sign problem. The remaining burden is to prove the unshifted localized form nonnegative, or to control a genuinely new limit/invariant that forces that sign.

## 1. The multiplicative and additive localizations are the same window

Connes--Consani--Moscovici formulate the semilocal construction on

\[
[\lambda^{-1},\lambda]
\]

with prime cutoff

\[
x=\lambda^2.
\]

Suzuki explicitly reformulates their closed localized Weil form on

\[
[-a,a],\qquad a=\log\lambda,
\]

and denotes it by `Q_W^a`, with canonical lower-bounded self-adjoint representative `A_a` satisfying

\[
Q_W^a(v)=\langle A_a v,v\rangle.
\]

Therefore

\[
x=\lambda^2=e^{2a}.
\]

This is exactly the cutoff denoted `c` in the finite CvS path used in `PL-264`. If that path uses additive length `L=log c`, then `L=2a`, so its interval `[-L/2,L/2]` is Suzuki's `[-a,a]`. This is the ordinary logarithmic change of variables between the multiplicative semilocal interval and the additive support interval of the completed Weil form, not a heuristic matching of scales.

## 2. The prime-power source cutoff also agrees exactly

Suzuki's continuous screw function contains the arithmetic term

\[
\sum_{n\le e^{|t|}}
\frac{\Lambda(n)}{\sqrt n}\bigl(|t|-\log n\bigr).
\]

For `x,y in [-a,a]`, the difference variable satisfies `|x-y|<=2a`, so no arithmetic atom with `n>e^{2a}` can enter the localized operator. Since `Lambda(n)` is supported on prime powers, the complete non-archimedean source is

\[
\{q=p^r:q\le e^{2a}\}
=
\{r e_p:r\log p\le2a\}
\]

in prime-exponent coordinates.

That is exactly the accumulated edge set of `PL-264` at cutoff `c=e^{2a}`. The local rank-one shocks isolated there are event-by-event singular increments of a source path whose fully accumulated value at `L=2a` is already the localized Weil form. The many-edge coupling and pole/archimedean completion are not a second object awaiting a bridge; they are ingredients of the target form itself.

Endpoint conventions (`<` versus `<=`) can depend on whether one uses smooth compact support or the closed form at the boundary. They do not change the parameter identity or source horizon.

## 3. What is exact at finite Galerkin level

The CvS finite matrix is obtained by evaluating the completed real-even distribution on a finite Fourier/Galerkin family. After the standard logarithmic/unitary identification,

\[
v^*Q_N(c)v
=
Q_W^a(f_v),
\qquad c=e^{2a},
\]

for the associated finite test function `f_v`. A negative direction of the finite matrix is therefore a negative direction of the same unshifted Weil form, and conversely within that Galerkin subspace.

One should **not** strengthen this to a literal operator identity

\[
Q_N(c)=P_NA_aP_N
\]

without fixing domains and form realizations. `A_a` is the self-adjoint representative of the closed continuum form, while `Q_N(c)` is a finite form compression. Equality of quadratic-form values on the identified test subspace is the safe exact statement.

`PL-261` supplies the relevant completeness theorem for the Connes--Consani Laurent core: at every fixed semilocal scale, the lowest finite-compression eigenvalues converge downward to the lower bound of the closed form. Thus no further bridge is needed for existential finite detection of a negative continuum direction.

## 4. Crossing information: corrected boundary

Suzuki proves that the lowest spectral value `lambda_a` of `A_a` is continuous in `a`, is positive for sufficiently small `a`, and becomes negative at some finite `a` if RH fails.

`PL-266` sharpens the moving-radius consequence and corrects the stronger boundary previously stated here. Suzuki's Corollary 1.2 identifies `lambda_a` with the infimum of the same global Weil Rayleigh quotient over the nested classes `C_c^infty(-a,a)`. Hence

\[
0<a<b\quad\Longrightarrow\quad\lambda_b\le\lambda_a.
\]

For the nested Laurent compressions `mu_N(a)` of `PL-261`, one has pointwise

\[
\mu_N(a)\ge\lambda_a,
\qquad
\mu_N(a)\downarrow\lambda_a.
\]

If RH is false and

\[
a_-:=\inf\{a>0:\lambda_a<0\},
\qquad
a_N:=\inf\{a>0:\mu_N(a)<0\},
\]

then

\[
a_N\downarrow a_-.
\]

Thus **uniform-in-`a` convergence is not needed merely to recover the onset of strict negativity**: the variational restriction prevents a false early crossing, and pointwise convergence at any fixed radius to the right of `a_-` eventually detects negativity. Suzuki's continuity gives `lambda_{a_-}=0`.

Important moving-radius problems remain. The argument does not exclude a zero plateau, so it does not necessarily locate the earliest radius with `lambda_a=0`; it gives no rate for `a_N-a_-`, no moving eigenvector convergence, and no locally uniform transform control on the expanding strip. The last problem is precisely the stronger stability gate isolated in `PL-262`. Nor does the threshold conclusion transfer automatically to an unrelated truncation lacking the restriction inequality and fixed-radius cofinal convergence.

## 5. Matched-control and sign audit

The common-form identity does not create an RH mechanism. Replacing the von-Mangoldt weights by another finite source while retaining the same support geometry and one-edge templates still produces a localized real distribution, finite Galerkin forms, and a continuum form. What changes is the global signed arithmetic content, not the existence of the representation bridge.

This sharpens `PL-264`: the universal one-edge jet is too weak, and accumulating those edges does not become RH-informative merely because the result is rewritten in Suzuki's screw-function coordinates. The RH-sensitive assertion remains the sign of the **specific completed zeta Weil form**, or a source-forced consequence strong enough to imply that sign.

Schematically,

\[
\text{CvS accumulated source path}
\quad=\quad
\text{finite/Galerkin representation of }Q_W^a
\quad\leftrightarrow\quad
A_a,
\]

where the equal sign denotes equality of the identified quadratic form and the last arrow passage to its canonical self-adjoint representative.

## 6. Analytic-continuation boundary

No Euler product is continued into the critical strip. The common object is the **completed Weil quadratic form**, whose pole, archimedean place, functional equation, and zero divisor have already entered through the explicit formula.

The finite prime cutoff comes from support: localization to `[-a,a]` places the autocorrelation/difference variable in `[-2a,2a]`, so only `q<=e^{2a}` contributes. Suzuki's formula for `g(t)` displays the same cutoff directly. The parameter match therefore survives analytic continuation because it concerns the completed explicit-formula distribution, not a formal Euler-product truncation outside `Re(s)>1`.

## 7. Prior-art and novelty audit

The decisive literature anchors are already registered in `research/prime_lattice/SOURCES.md`:

- source 56, **Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2**. Suzuki unifies the localized Weil results of Yoshida, Bombieri, Connes--Consani, and Connes--Consani--Moscovici; rewrites the multiplicative interval with `a=log lambda`; identifies `Q_W^a` with the closed localized form represented by `A_a`; and gives the screw kernel with arithmetic horizon `n<=exp(|t|)`.
- source 28, **Connes--Consani--Moscovici, “Zeta spectral triples”**, for the semilocal normalization `[lambda^-1,lambda]` and prime horizon `x=lambda^2`.
- source 27, **Connes--Consani, “Spectral triples and zeta-cycles”**, for the fixed-scale Laurent form core used in `PL-261` and `PL-266`.

`PL-264` stores the finite CvS path and its exact von-Mangoldt edge increments. Combining these established pieces yields

\[
c=x=\lambda^2=e^{2a},\qquad L=\log c=2a.
\]

This parameter synthesis is immediate once the notations are aligned and is **not claimed as a new theorem**. The durable result remains the prior-art redirect: the local clue treated CvS accumulation and Suzuki localization as potentially distinct objects requiring a bridge, but they are two realizations of the same completed localized Weil form.

`PL-266` adds an elementary variational sharpening of the crossing boundary. No new literature source is needed for either result.

## 8. Falsification and remaining live target

The bridge claim would be materially falsified or narrowed if the CCM prime horizon at multiplicative radius `lambda` were not `lambda^2`, Suzuki's `a` were not `log lambda`, the CvS path of `PL-264` used a different completed distribution, or the finite matrix quadratic values failed to equal the restricted Weil quadratic form on their defining test family. The cited constructions exclude these possibilities under the stated normalizations.

The line no longer needs an abstract transform from CvS to Suzuki, nor a uniform-in-radius theorem merely to prevent drift of the first **strict-negative** Laurent-core threshold. What remains genuinely RH-facing is sharper: derive nonnegativity from source arithmetic not already equivalent to Weil positivity; understand whether a zero plateau can occur if earliest degeneracy matters; obtain quantitative threshold/eigenvector control; solve the expanding-window transform stability problem of `PL-262`; or produce a source invariant of the accumulated prime-power path that fails matched non-zeta controls and forces the unshifted Weil orientation.

The clue `CLUE-localized-weil-multi-edge-bridge` remains resolved as a bridge-construction question. Its deeper motivation—the missing reason the exact zeta source should have the correct global sign—remains open.
