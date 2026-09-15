# AF-362 — Riesz target recovery is an exponential Picard-moment gate

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-RELATIVE`, `QUANTITATIVE-FIDELITY`, `STABILITY-GATE`, `MOVING-PARAMETER-OBSTRUCTION`, `ZERO-SENSITIVE-SOURCE`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

AF-361 prices recovery of the **entire** endpoint zero-coefficient vector through small-order Riesz smoothing. Its condition number is a worst-case target: it charges for the least transmitted mode even if the downstream observable barely uses that mode. For a declared linear target, the exact recovery price is sharper and is governed by a target-weighted exponential moment.

Retain AF-361's notation. On a finite populated zero band

\[
\mathcal B_{\delta,T}(R_\delta)
=
\{\gamma:T<\gamma\le TR_\delta\},
\]

write

\[
\rho_\gamma=\frac12+i\gamma,
\qquad
M_\delta(\rho)
=
\Gamma(1+\delta)\frac{\Gamma(\rho+1)}{\Gamma(\rho+1+\delta)},
\]

\[
x_\gamma
:=
\delta\log\frac\gamma T,
\qquad
c_{\delta,T}
:=
\Gamma(1+\delta)(iT)^{-\delta},
\]

and let

\[
D_{\delta,T,R_\delta}
:=
\operatorname{diag}\big(M_\delta(\rho_\gamma)\big)_{\gamma\in\mathcal B_{\delta,T}(R_\delta)}.
\tag{1}
\]

Assume RH only for the interpretation of these coordinates as the full critical zero-coefficient channel inherited from AF-358--AF-361. The multiplier estimates below are analytic statements about `(1)` and do not use RH.

Let `a=(a_\gamma)` be a nonzero target vector on the band and define

\[
L_a(z)=\langle a,z\rangle.
\tag{2}
\]

Suppose the available observation is

\[
y=D_{\delta,T,R_\delta}z+\eta,
\qquad
\|\eta\|_2\le\varepsilon.
\tag{3}
\]

Require a recovery rule to be exact on noiseless data for **every** endpoint vector `z`. Then the optimal worst-case error is exactly

\[
\boxed{
\sup_{\|\eta\|_2\le\varepsilon}
\big|\widehat L(Dz+\eta)-L_a(z)\big|
=
\varepsilon\,\|D^{-*}a\|_2.
}
\tag{4}
\]

In fact there is no freedom in the exact recovery rule: because the finite-band diagonal map `D` is invertible, noiseless exactness forces

\[
\widehat L(y)=L_a(D^{-1}y)
=
\langle D^{-*}a,y\rangle
\tag{5}
\]

for every observation vector `y`.

Normalize the target energy into a probability measure on scaled log-frequency,

\[
\mu_{a;\delta,T}
:=
\sum_{\gamma\in\mathcal B_{\delta,T}(R_\delta)}
\frac{|a_\gamma|^2}{\|a\|_2^2}\,\delta_{x_\gamma}.
\tag{6}
\]

AF-361's uniform Gamma-quotient law gives, independently of the upper-band width,

\[
\left|
\frac{M_\delta(\rho_\gamma)}{c_{\delta,T}}
\right|
=
e^{-x_\gamma}
\exp\!\left(O\!\left(\frac\delta T\right)\right).
\tag{7}
\]

Therefore the **exact target-relative recovery modulus** has the asymptotic form

\[
\boxed{
|c_{\delta,T}|\,
\frac{\|D^{-*}a\|_2}{\|a\|_2}
=
\left(
\int e^{2x}\,d\mu_{a;\delta,T}(x)
\right)^{1/2}
\exp\!\left(O\!\left(\frac\delta T\right)\right).
}
\tag{8}
\]

Thus, after quotienting the common lower-edge attenuation, a family of unit-norm targets is uniformly stably recoverable through the Riesz channel **if and only if** its scaled-frequency profiles have uniformly bounded exponential second moment:

\[
\boxed{
\sup_{\delta,T}
\int e^{2x}\,d\mu_{a;\delta,T}(x)<\infty.
}
\tag{9}
\]

The hard bandwidth `v_\delta=\delta\log R_\delta` is therefore only a worst-case proxy. Even when

\[
v_\delta\to\infty,
\tag{10}
\]

a particular target can remain uniformly recoverable if its energy avoids the progressively more attenuated part of the band strongly enough to satisfy `(9)`. Conversely, bounded target recovery forces the sharp tail estimate

\[
\boxed{
\mu_{a;\delta,T}([s,\infty))
\le
C^2e^{-2s}
}
\tag{11}
\]

whenever the left side of `(8)` is at most `C`. If a target retains mass at least `alpha>0` above `x=v_\delta-r`, then

\[
|c_{\delta,T}|\,
\frac{\|D^{-*}a\|_2}{\|a\|_2}
\ge
\sqrt\alpha\,e^{v_\delta-r}
\exp\!\left(O\!\left(\frac\delta T\right)\right),
\tag{12}
\]

so it inherits AF-361's full-band instability up to the declared tail mass.

The absolute noise price remains separate. Since

\[
|c_{\delta,T}|^{-1}
=
\Gamma(1+\delta)^{-1}T^\delta,
\tag{13}
\]

if `u_{\delta,T}=\delta\log T`, then

\[
\boxed{
\frac{\|D^{-*}a\|_2}{\|a\|_2}
=
\exp(u_{\delta,T}+o(1))
\left(
\int e^{2x}\,d\mu_{a;\delta,T}(x)
\right)^{1/2}.
}
\tag{14}
\]

Equation `(14)` is the target-specific refinement of AF-361's two-currency law. The base attenuation `u` charges every target. The differential bandwidth cost is not intrinsically `v`; it is the logarithmic moment

\[
\frac12\log\int e^{2x}\,d\mu_a(x).
\tag{15}
\]

AF-361's factor `e^v` is recovered by taking the supremum over all unit targets, because the maximizing target concentrates on a least-transmitted upper-edge coordinate.

## Derivation

### 1. Exact noisy recovery of one linear target is an adjoint-range problem

For fixed `delta,T,R_delta`, the band contains finitely many zero coordinates and every diagonal entry of `D` is nonzero. Hence `D` is a bijection of the finite coefficient space.

If a recovery map `\widehat L` is exact on noiseless data for every `z`, then for arbitrary `y` one can write `y=Dz` with `z=D^{-1}y`. Therefore exactness already forces `(5)` on the whole observation space; allowing nonlinear estimators cannot improve the deterministic-noise problem without sacrificing noiseless exactness.

For the perturbed observation `(3)`, the error is

\[
\widehat L(Dz+\eta)-L_a(z)
=
\langle D^{-*}a,\eta\rangle.
\tag{16}
\]

Cauchy--Schwarz gives the upper bound in `(4)`, and equality is attained by choosing `eta` in the Riesz-representer direction of `D^{-*}a`. Thus `(4)` is an equality, not a condition-number estimate.

In an infinite-dimensional limit this is the classical adjoint-range/Picard geometry: a bounded exact observation-space representative for `L_a` exists precisely when `a` belongs to `ran(D^*)`, and in a singular basis this becomes reciprocal-singular-value square summability. The finite-band formula here is the exact precursor of that criterion.

### 2. Riesz smoothing turns the Picard weight into an exponential moment

Because `D` is diagonal,

\[
\|D^{-*}a\|_2^2
=
\sum_\gamma
\frac{|a_\gamma|^2}{|M_\delta(\rho_\gamma)|^2}.
\tag{17}
\]

AF-361 gives uniformly for every retained ordinate

\[
\frac{|c_{\delta,T}|^2}
{|M_\delta(\rho_\gamma)|^2}
=
e^{2x_\gamma}
\exp\!\left(O\!\left(\frac\delta T\right)\right).
\tag{18}
\]

The error in `(18)` is uniform because the Gamma-quotient remainder depends on the lower edge `T`, not on the upper endpoint. Multiplying `(17)` by `|c|^2/\|a\|^2` and using `(6)` gives

\[
|c|^2
\frac{\|D^{-*}a\|_2^2}{\|a\|_2^2}
=
\left(
\int e^{2x}\,d\mu_{a;\delta,T}(x)
\right)
\exp\!\left(O\!\left(\frac\delta T\right)\right),
\tag{19}
\]

which proves `(8)`.

The result is stronger than replacing `\|D^{-1}\|` by an average singular value. The probability measure `(6)` is determined by the **declared target functional**, and `(19)` is its exact reciprocal-multiplier energy. Modes irrelevant to the target contribute nothing even when they make the full inverse badly conditioned.

### 3. Exponential target tails, not hard bandwidth, are the sharp normalized gate

If the exponential moment in `(9)` is bounded by `C^2`, Markov's elementary one-sided estimate gives

\[
e^{2s}\mu([s,\infty))
\le
\int_{[s,\infty)}e^{2x}\,d\mu(x)
\le C^2,
\tag{20}
\]

which is `(11)`. Thus a target that remains stable while the physical band expands without bound must progressively suppress its high-`x` energy at least at the exponential scale required by its complete moment, not merely make each individual coefficient small.

Conversely, the exact moment itself is the sufficient condition; no hard support cutoff is required. For example, if a target family is supported in `x<=K` for a fixed `K`, then its normalized recovery cost is at most `e^K(1+o(1))` no matter how far the retained observation band extends. More generally any family satisfying `(9)` has the same property even with unbounded support.

If `mu([v_delta-r,infinity))>=alpha`, then restricting `(19)` to that tail gives `(12)`. Hence targets carrying nonvanishing energy near the moving upper edge recover AF-361's `e^{v_delta}` instability. The full-vector condition number is precisely the supremum of this target-relative modulus over the unit sphere.

### 4. Absolute attenuation and target shape remain independent resources

Equation `(13)` converts normalized observation noise to physical observation noise. Combining it with `(8)` yields `(14)`. A target can therefore pass the differential Picard gate `(9)` and still be unrecoverable against a fixed absolute noise floor if `u=delta log T` diverges.

Conversely, bounded `u` does not rescue a target whose exponential moment diverges. The two resources answer different questions:

- `u` measures whether the whole retained band remains above the absolute observation floor;
- the exponential moment measures whether the particular target asks for information concentrated in strongly attenuated relative modes.

This removes the residual ambiguity in interpreting AF-361's hard-band law: the transformation itself has a worst-case condition number, but **fidelity is target-relative unless the destination genuinely requires the whole vector**.

## Arithmetic-fidelity interpretation

This result closes a live logical gap in the moving-Riesz analysis. AF-361 showed that `delta log R -> infinity` makes full-vector inversion ill-conditioned. That fact alone cannot rule out an RH-facing destination that depends only on a better-conditioned linear functional of the endpoint coefficients. The correct test is `(9)`, together with the absolute factor `(14)`.

The theorem therefore changes what a downstream argument must provide. It is no longer enough to quote either a broad retained band or its worst singular value. One must exhibit the actual source-native target representer `a_{delta,T}`, prove that it is defined independently of the Riesz inverse, and calculate its scaled-frequency measure `(6)`. Only then can one decide whether smoothing has erased the information required by that destination.

This also supplies an exact anti-cheating test. Choosing

\[
a_\gamma=M_\delta(\rho_\gamma)b_\gamma
\]

can make a desired post-Riesz functional artificially well behaved, but it simply bakes the channel multiplier into the target definition. Such a target is not evidence that an independently defined arithmetic discriminator survived. The target profile must come from the source-side arithmetic or from the declared destination observable before its Riesz transport cost is evaluated.

The matched-control conclusion from AF-361 remains unchanged. Equations `(8)`--`(15)` depend only on the universal Riesz multiplier and the chosen target weights on the same frequency coordinates. A matched non-arithmetic coefficient family pays exactly the same transport cost. The theorem can certify preservation of an incoming discriminator, but it cannot create rational-prime specificity.

## Prior art and novelty assessment

No novelty is claimed for adjoint-range recoverability, the Picard criterion, Riesz representation, deterministic optimal recovery of a linear functional, or reciprocal-singular-value weighting.

The closest already-canonical Arithmetic Fidelity precedent is AF-135, which proves in a spectral-Gram setting that target fidelity is controlled by a **whitened target tail** rather than by the ambient condition number and explicitly identifies the resulting discrete-Picard structure. Its prior-art audit records the classical Moore--Penrose, truncated-SVD, and discrete Picard literature, including Per Christian Hansen's 1990 TSVD and discrete-Picard papers.

A fresh literature audit also places `(4)` in the established optimal-recovery/inverse-problem language: classical Picard theory characterizes range membership by reciprocal singular-value square summability, modern inverse-problem surveys treat source/range conditions as the natural stability currency, and the optimal-recovery literature studies linear functionals from indirect noisy observations. Nothing at that abstract operator-theory layer is claimed as new here.

The substantive delta is the **Riesz specialization of that classical target-relative geometry**. AF-361 supplies the uniform moving-band multiplier law, and substituting it into the Picard weight yields the explicit scaled-frequency exponential moment `(8)`. This replaces the hard-band obstruction `e^{v_delta}` by an exact target-dependent criterion and exposes a genuinely larger admissible regime: `v_delta -> infinity` can coexist with bounded normalized target recovery, but only for target families satisfying the exponential-moment gate `(9)`.

## Boundaries and falsification

- The result is exact for linear target functionals and deterministic `ell^2` observation noise. Nonlinear destination observables require their own modulus or a justified linearization; `(8)` must not be silently transferred to them.
- The zero band is finite for each parameter pair. Infinite-band limits are interpreted through families of finite bands. In a genuine infinite-dimensional operator, `a in ran(D^*)` and the corresponding Picard sum are the correct existence conditions.
- The criterion is relative to the coefficient `ell^2` geometry. A different physically justified noise norm changes the dual recovery norm and therefore the target weighting.
- RH is not used in the Gamma-quotient estimate or the diagonal recovery algebra. It is used only when the endpoint coefficient space is identified with all nontrivial zeta zeros on the critical line as in the preceding Riesz findings.
- Bounded normalized cost does not imply bounded absolute cost. The independent factor `T^delta/Gamma(1+delta)` in `(14)` remains.
- A bounded exponential moment does not establish rational-prime specificity. The same target profile on a matched non-arithmetic coefficient family has the same transport modulus.
- An arbitrarily chosen target adapted to `M_delta` can trivialize the transport price. Such a construction is a hidden inverse unless the target is independently forced by the source or destination mathematics.
- The target need not have compact support in scaled frequency. Condition `(9)` is strictly more general; its exponential tail consequence `(11)` is necessary but by itself is weaker than the full moment bound.

A direct falsification would be a family of nonzero targets and Riesz bands for which AF-361's uniform multiplier estimate holds but the ratio in `(8)` fails to approach the exponential moment predicted by `(6)`. Since `(8)` is an algebraic substitution into the exact diagonal dual norm, such a counterexample would have to expose an error in the multiplier normalization or in the declared observation/target geometry.

## Consequences for the research line

The moving-Riesz frontier is now target-specific. The next useful RH-facing theorem cannot stop at full-vector conditioning. It must identify an independently justified arithmetic/destination functional or witness and then prove one of three things:

1. its exponential Picard moment stays bounded while the absolute attenuation budget also remains usable, showing that the required information genuinely survives Riesz transport;
2. its target mass necessarily reaches the moving high-`x` region, forcing the lower bound `(12)` and closing that destination under the declared noise model; or
3. the required destination is nonlinear or relational in a way that cannot be reduced to one linear target, in which case a new target-specific modulus must be derived rather than inferred from the ambient inverse condition number.

This sharpens AF-361's source-native burden without supplying the missing arithmetic target. It is a fidelity gate, not an RH consequence.