# WP-170 — The archimedean Gamma phase is unimodular but not a passive inner boundary response

**Status:** `EXACT-DERIVED + ARCHIMEDEAN-SCATTERING + SCHUR-INNER-NO-GO + BLASCHKE-OBSTRUCTION + PHASE-SIGN-CHANGE + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-169` identifies an exact piece of information that the positive critical shell Gram of `WP-168` discards. Relative to the canonical Nyman fractional-part factor, the Mathia pointed-shell factor carries the real-place functional-equation phase

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})},
\qquad |R_\infty(\tau)|=1
\quad(\tau\in\mathbb R),
\tag{1}
\]

and

\[
i\frac{d}{d\tau}\log R_\infty(\tau)
=
A_\infty(\tau)
:=\operatorname{Re}\psi\!\left(\frac14+\frac{i\tau}{2}\right)-\log\pi,
\tag{2}
\]

where `A_infty` is exactly the nonconstant archimedean Weil symbol in the normalization used by this research line.

A tempting next step is therefore to try to make `R_infty` itself the scattering/characteristic function of a positive boundary problem. For an ordinary scalar passive realization this would be natural: a Herglotz--Nevanlinna Weyl/DtN function has a Schur characteristic function after a Cayley transform, and a lossless boundary response has inner boundary values. Positivity would then be inherited from the underlying passive geometry rather than inserted into the explicit formula.

That route fails exactly. Although (1) is unimodular on the real axis, its analytic continuation is **not** a Schur/inner function in either causal half-plane orientation. In the upper half-plane its zeros are

\[
\boxed{\tau_n=i\left(2n+\frac12\right),\qquad n=0,1,2,\ldots,}
\tag{3}
\]

and they violate the Blaschke condition:

\[
\sum_{n\ge0}
\frac{\operatorname{Im}\tau_n}{1+|\tau_n|^2}
=
\sum_{n\ge0}
\frac{2n+\tfrac12}{1+(2n+\tfrac12)^2}
=\infty.
\tag{4}
\]

Hence no nonzero bounded analytic function on the upper half-plane can have the zero set (3). In particular `R_infty` is not in the Schur class and cannot be an inner characteristic function there. The inverse orientation has poles at exactly the same upper-half-plane points, so it is not analytic there at all. Swapping upper and lower half-planes exchanges the two statements. Thus neither orientation of the exact Gamma phase is the scalar lossless response of an ordinary positive Herglotz boundary system.

There is an independent boundary manifestation of the same obstruction. Writing

\[
R_\infty(\tau)=e^{i\phi(\tau)},
\tag{5}
\]

with a continuous real phase, (2) gives

\[
\boxed{
\phi'(\tau)
=\log\pi-\operatorname{Re}\psi\!\left(\frac14+\frac{i\tau}{2}\right)
=-A_\infty(\tau).
}
\tag{6}
\]

For `tau>0`, `A_infty` is strictly increasing. Indeed the standard trigamma expansion

\[
\psi'(z)=\sum_{m=0}^{\infty}\frac1{(m+z)^2},
\qquad \operatorname{Re}z>0,
\tag{7}
\]

gives

\[
\frac{d}{d\tau}A_\infty(\tau)
=-\frac12\operatorname{Im}\psi'\!\left(\frac14+\frac{i\tau}{2}\right)
=
\sum_{m=0}^{\infty}
\frac{(m+\tfrac14)(\tau/2)}{igl((m+\tfrac14)^2+(\tau/2)^2\bigr)^2}
>0.
\tag{8}
\]

At the origin,

\[
A_\infty(0)
=\psi\!\left(\frac14\right)-\log\pi
=-\gamma-\frac\pi2-3\log2-\log\pi<0,
\tag{9}
\]

whereas the digamma asymptotic gives

\[
A_\infty(\tau)
=\log\frac{\tau}{2\pi}+O(\tau^{-2})
\longrightarrow+\infty.
\tag{10}
\]

Consequently there is a unique `tau_0>0` at which `A_infty` vanishes (numerically `tau_0≈6.2898359888`), and the scattering phase velocity (6) changes sign there:

\[
\phi'(\tau)>0\quad(0<\tau<\tau_0),
\qquad
\phi'(\tau)<0\quad(\tau>\tau_0).
\tag{11}
\]

For a scalar meromorphic inner function in the upper half-plane, the boundary argument is monotone in the standard orientation: its derivative is a nonnegative sum/distribution of Poisson kernels from its Blaschke zeros plus the nonnegative singular/exponential contribution. Equation (11) therefore also rules out interpreting the exact `WP-169` phase velocity as an ordinary positive time-delay/Clark density. The exact Weil digamma symbol is a signed response, not the boundary density of a scalar inner positive system.

This is a stronger obstruction than merely observing in `WP-169` that taking a logarithmic phase derivative is not a positive Gram operation. Even **before** taking that derivative, the unimodular factor itself fails the analytic passivity test required by the standard scalar Herglotz/Schur route.

## 1. Exact zero and pole geometry

The Gamma function has simple poles at `0,-1,-2,...` and no zeros. The denominator in (1) has a pole when

\[
\frac14+\frac{i\tau}{2}=-n,
\]

which is equivalent to (3). At such a point the numerator is

\[
\Gamma\!\left(n+\frac12\right),
\]

which is finite and nonzero, so every `tau_n` is a simple zero of `R_infty`.

Similarly the numerator has simple poles at

\[
\tau=-i\left(2n+\frac12\right),
\qquad n\ge0.
\tag{12}
\]

Thus `R_infty` is analytic in the open upper half-plane, but its zeros there have linear density and fail (4). The factor `pi^(i tau)` is entire and nonvanishing and therefore cannot alter this zero geometry.

The upper-half-plane Blaschke condition is necessary for the zero set of every bounded analytic nonzero function. Since the summand in (4) is asymptotic to `1/(2n)`, the condition fails logarithmically. Hence the boundary identity `|R_infty|=1` does **not** mean that `R_infty` is inner: it hides unbounded analytic growth in the half-plane.

This distinction matters for the Mathia program because ordinary positive boundary realizations do not merely require a unitary multiplier on the boundary. Their analytic continuation is constrained by passivity. If `M(z)` is a scalar Herglotz--Nevanlinna function, for example, then an appropriate Cayley transform

\[
S(z)=\frac{M(z)-i}{M(z)+i}
\tag{13}
\]

is Schur. A lossless realization has unimodular boundary values, hence an inner `S`. Equation (4) proves that the exact `R_infty` from `WP-169` cannot be such an `S`.

## 2. The sign-changing phase velocity is the same failure on the boundary

Equation (8) gives more than an asymptotic sign check: it proves strict monotonicity of the exact Weil archimedean symbol on the positive axis. Combining (9) and (10) gives a unique sign crossing. Therefore neither a constant phase gauge nor reversing the scattering orientation turns the raw phase derivative into a globally nonnegative density; reversing orientation simply reverses both signs.

A pure translation/delay factor `exp(i a tau)` does not cure the analytic obstruction either. It changes the boundary phase velocity by the constant `a` but leaves all zeros (3) unchanged, so the Blaschke failure persists. Likewise multiplying by a finite Blaschke/rational passive factor cannot remove the non-Blaschke zero sequence: multiplication only adds admissible zeros, while cancellation would require poles at (3), which a Schur factor cannot supply in its analytic half-plane.

Thus the no-go is not a normalization accident. To turn the real-place phase into a genuinely passive characteristic function one would have to change the analytic object by an **infinite, nontrivial compensating structure**, not by a scalar gauge, orientation choice, finite-dimensional boundary attachment, or ordinary delay.

## 3. Matched controls

Three controls delimit the claim.

First, the scalar Gram of `WP-168` remains positive and stationary because it keeps only `|zeta|^2`. Nothing here contradicts that positivity. The present obstruction concerns exactly the extra phase datum exposed by `WP-169`.

Second, Jean-François Burnol's local scattering work is an important prior-art comparison. At nonarchimedean places, nonnegative time-delay data can occur, while the local Weil distribution is recovered only with an additional grading/supertrace structure. The present calculation shows that the raw real-place Gamma factor does not even provide an ordinary scalar positive time-delay density globally. It therefore cannot be promoted to the desired Weil sign merely by copying the simplest passive-scattering interpretation.

Third, the conclusion is specific to **scalar passive/Herglotz boundary realization of the exact phase**. It does not rule out a genuinely matrix-valued, indefinite-to-positive, compressed, domain-changing, or nonseparable finite--archimedean geometry in which the final positive theorem appears only after coupling. Such an escape must, however, alter the analytic category before scalarization; it cannot claim that the already identified unimodular `R_infty` is itself the positive boundary response.

## 4. Prior-art and novelty audit

No novelty is claimed for the Gamma poles, the Blaschke condition, Herglotz/Schur Cayley transforms, or the Riemann--Siegel phase behavior. These are classical complex/function-theoretic facts. Standard references include John B. Garnett, *Bounded Analytic Functions* (Springer GTM 236, 2007) for Blaschke/inner theory and the NIST DLMF, Chapter 5, for Gamma/digamma/polygamma identities and asymptotics.

The relevant number-theoretic scattering boundary remains the literature already anchored for `WP-169`: Jean-François Burnol, *On Fourier and Zeta(s)* (Forum Math. 16, 2004) and *Entrelacement de co-Poisson* (Ann. Inst. Fourier 57, 2007). Burnol's *Scattering on the p-adic field and a trace formula* (IMRN 2000) is the matched positive-time-delay control already recorded in `research/weil_positivity/SOURCES.md`.

The Mathia-specific substantive content is the no-go obtained by applying those classical positivity constraints to the **exact source-derived phase isolated by `WP-169`**:

\[
\boxed{
\text{pointed critical phase }R_\infty
+\text{ scalar passive boundary positivity}
\not\Rightarrow
\text{Weil positivity},
}
\tag{14}
\]

for the stronger reason that `R_infty` itself is not a Schur/inner passive response.

## 5. Research consequence

The live architecture in `research/weil_positivity/mind/RESEARCH_LINES.md` asks for a real-place phase/boundary operator intrinsic to the same source geometry that retains signed finite-prime information, coupled before positive scalarization. `WP-169` supplied the exact phase shape but not its intrinsic selection. The present result adds another necessary condition: **even if that phase were made intrinsic, ordinary scalar passive boundary positivity would still not be the missing sign theorem.**

A viable continuation must therefore do at least one of the following before the final positive readout: couple finite and archimedean channels nonseparably so that the scalar `R_infty` is no longer the characteristic function being tested; pass to a matrix/operator-valued response with a new coercivity theorem; use a compression/domain change whose positivity is not equivalent to scalar Schur passivity; or discover a source-forced infinite compensating structure whose contribution is simultaneously the missing finite/polar data rather than an inserted regularization.

The last possibility is especially constrained by the branch mandate. Because the zero sequence (3) requires an infinite compensation, any proposed repair must explain from the same Mathia geometry why that compensation also carries the finite-prime and polar terms. Appending an arbitrary infinite inner/outer factor merely to restore passivity would be another hand-picked regularization and does not pass the substantive gate.