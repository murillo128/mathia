# XF-075 — reference-only seam repair uniquely reconstructs the periodized numerator

**Status:** `EXACT-DERIVED` + `CLASSICAL-H-TRANSFORM-ALGEBRA` + `REFERENCE-ONLY-NO-GO` + `STRUCTURAL/OBSTRUCTION`. XF-073 proves that the Gaussian/Appell quotient recovers the Xi heat solution with super-polynomial relative accuracy on a safe interior high-line segment, while XF-074 shows that the same quotient is generically meromorphic on a full period because the periodized Gaussian reference has an exact seam divisor. A natural repair would be to use only that known reference to cancel the seam and recover a global entire exact-heat carrier.

There is a sharp obstruction to that repair. Let `W=W_L` be the periodized Gaussian reference and `V=V_L` any periodized exact backward-heat solution from the same Appell construction. On a zero-free component of `W`, put

\[
R=\frac VW,
\qquad
b=\frac{W_z}{W},
\qquad
\mathcal L_0:=\partial_t+\partial_z^2,
\qquad
\mathcal L_W:=\partial_t+\partial_z^2+2b\partial_z.
\tag{1}
\]

Then `L_0 W=L_0 V=0` and `L_W R=0`. More strongly, multiplication by `W` is the exact intertwiner

\[
\boxed{
\mathcal L_0(Wf)=W\mathcal L_W f.
}
\tag{2}
\]

It is also the **unique nontrivial source-independent multiplicative intertwiner**, up to a scalar depending only on time. Precisely, suppose `A(z,t)` is allowed to depend on the reference but not on `V`, and suppose there is a scalar `lambda(t)` such that

\[
\mathcal L_0(Af)
=
A\mathcal L_W f+\lambda(t)Af
\tag{3}
\]

for every local test function `f`. Then on every connected zero-free component of `W`,

\[
\boxed{A(z,t)=c(t)W(z,t),\qquad \lambda(t)=\frac{c'(t)}{c(t)}.}
\tag{4}
\]

Consequently, when `f=R=V/W`,

\[
\boxed{AR=c(t)V.}
\tag{5}
\]

After removing the harmless time-dependent scalar, the only universal multiplicative repair that restores exact backward heat simply reconstructs the original periodized numerator. If exact backward heat is required with no scalar zeroth-order gauge, then `c` is constant.

There is an equally sharp additive obstruction. XF-074 supplies two exact matched controls at a frozen time: `u=1`, for which `R=1` and every reference seam singularity cancels, and a zero-free Fourier heat mode for which the same reference seam points are genuine poles of `R`. Therefore no additive principal-part correction depending only on `W` can make the quotient holomorphic for both controls. Any meromorphic seam subtraction that works beyond the special `u=1` control must use **source-dependent seam data** (equivalently, the numerator jets that determine the Laurent principal parts).

Thus there is no reference-only global repair that simultaneously keeps the relative quotient normalization and restores the exact entire heat structure required by the XF-067--XF-071 Vieta transport. The live Gaussian route is narrower than XF-074 left it: remain center-local, obtain new Xi control at the seam and subtract source-dependent principal parts, or use an approximate/nonmultiplicative finite surrogate with an explicit conditioning and truncation budget. A fixed theta/reference correction by itself cannot supply the missing global carrier.

## 1. Exact quotient conjugation

Because `W` and `V` solve backward heat,

\[
W_t=-W_{zz},
\qquad
V_t=-V_{zz}.
\tag{6}
\]

On `W\ne0`, write `V=WR`. Expanding `(WR)_t+(WR)_{zz}=0` gives

\[
W\left(R_t+R_{zz}\right)+2W_zR_z=0,
\]

hence

\[
\boxed{
R_t=-R_{zz}-2\frac{W_z}{W}R_z.
}
\tag{7}
\]

This is the forced quotient equation already used in XF-073. But the same expansion with an arbitrary `f` gives the stronger operator identity (2):

\[
\begin{aligned}
\mathcal L_0(Wf)
&=(W_t+W_{zz})f
 +W(f_t+f_{zz})+2W_zf_z\\
&=W\left(f_t+f_{zz}+2\frac{W_z}{W}f_z\right).
\end{aligned}
\tag{8}
\]

No zero information about `V` enters. The identity is purely the gauge/`h`-transform algebra of two solutions of the same parabolic operator.

For a general multiplier `A`, the corresponding expansion is

\[
\boxed{
\mathcal L_0(Af)-A\mathcal L_W f
=
(\mathcal L_0A)f
+2\left(A_z-Ab\right)f_z.
}
\tag{9}
\]

Equation (9) is the decisive comparison because the target Vieta carrier needs exact heat evolution, not merely pointwise cancellation of a known divisor.

## 2. Uniqueness of a universal multiplicative heat repair

Assume (3). Comparing the independent coefficients of `f` and `f_z` in (9) yields

\[
A_z=Ab=A\frac{W_z}{W},
\qquad
\mathcal L_0A=\lambda(t)A.
\tag{10}
\]

The first identity gives

\[
\partial_z\left(\frac AW\right)=0,
\]

so on each connected zero-free component

\[
A=c(t)W.
\tag{11}
\]

Substituting into the second identity and using `L_0W=0`,

\[
\mathcal L_0(cW)=c'(t)W=\lambda(t)c(t)W.
\tag{12}
\]

This proves (4). If `A` is required to extend holomorphically across the reference divisor, the identity extends by analytic continuation: there is no second entire reference-only multiplier hiding behind the seam.

Allowing the scalar `lambda(t)` is important. Multiplying an entire heat carrier by a nonzero time-dependent scalar does not change its zero divisor or normalized Vieta coordinates. Even with that harmless freedom, (5) shows that the quotient cannot be converted into a different exact carrier by a universal multiplier. The only possibility is the numerator `V` itself, up to normalization.

This is stronger than the elementary statement that multiplying `R` by `W` removes its poles. It says that **preserving the exact heat operator forces that choice**. Any other reference-only multiplier necessarily leaves a first-derivative defect, introduces a spatial potential, or both, and therefore exits the exact diagonal Vieta dynamics used in XF-067--XF-071.

## 3. A fixed additive theta correction cannot cancel generic seam poles

A second possible repair is additive: keep the quotient but subtract a fixed meromorphic principal part built from the known theta reference. XF-074 already contains a matched control that rules this out source-independently.

At any frozen time `t_0`, the reference has the seam-zero family

\[
z_{r,n}
=\left(r+\frac12\right)L
+i(2n+1)\frac{\pi v(t_0)}L.
\tag{13}
\]

For the exact heat datum `u\equiv1`, periodization gives `V=W`, hence

\[
R_0\equiv1.
\tag{14}
\]

For the zero-free Fourier heat mode used in XF-074, with

\[
\omega_0=\frac{\pi h(t_0)}L,
\]

the transformed numerator is a vertical translate of `W` and is nonzero at every point (13). Therefore

\[
R_{\omega_0}
=
e^{-\omega_0^2\sigma^2/2}
\frac{W(z-i\omega_0\sigma^2,t_0)}{W(z,t_0)}
\tag{15}
\]

has a genuine pole at every exhibited seam zero.

Suppose a correction `P_W(z,t_0)`, depending only on the reference, made `R-P_W` holomorphic through those seam points for every exact heat datum. Applying this first to (14) forces `P_W` itself to be holomorphic there. Applying the same correction to (15) then leaves its genuine pole untouched, a contradiction. Hence

\[
\boxed{
\text{no source-independent additive seam subtraction can holomorphize all quotient data.}
}
\tag{16}
\]

At a simple reference zero `zeta`, the required principal coefficient would be `V(zeta)/W_z(zeta)`; at a higher-order zero the corresponding Laurent coefficients depend on further numerator jets. The exact order is not needed for (16). What matters is that the principal part is **data-dependent**. XF-073 deliberately controls Xi only on the safe interior contour, so it presently supplies none of this seam information.

## 4. Consequence for the Gaussian-to-Vieta bridge

XF-074 left three honest possibilities: stay center-local, work meromorphically with explicit seam control, or construct a finite entire surrogate with its auxiliary divisor neutralized. XF-075 separates what can be done using the known reference alone from what requires genuinely new source information.

A universal multiplicative repair that preserves exact heat evolution is exhausted by `W` and returns `V`. This reinstates the unnormalized Gaussian/Appell numerator; it does not turn the relatively normalized quotient into a new global zero carrier. A universal additive repair is impossible because the seam principal parts vary with the heat datum. Therefore the phrase "neutralize the reference divisor" cannot mean applying a fixed theta correction after division.

The meromorphic route remains logically possible, but it now has an explicit source obligation: control the actual Xi numerator at the reference seam strongly enough to estimate and transport its principal parts in the destination norm. That is outside the domain of XF-073, whose strength comes precisely from staying a horizontal distance `L/4` away from the seam. A finite entire trigonometric surrogate also remains possible because it may be approximate, nonmultiplicative, or source-dependent; XF-075 only says that such a construction must expose and pay for those departures rather than obtaining them for free from the reference.

For the current program this makes the center-local destination route the only branch that can proceed using **only** the source information already established in XF-073. It does not prove that the local route closes, and it does not show that the two source-dependent global alternatives are impossible.

## 5. Prior-art boundary

The operator algebra in (2) is classical `h`-transform/gauge structure: Doob's `h`-transform conjugates a linear Markov/heat generator by multiplication with a harmonic or space-time harmonic reference, producing a logarithmic-derivative drift. A primary classical anchor is J. L. Doob, **Conditional brownian motion and the boundary limits of harmonic functions**, *Bulletin de la Société Mathématique de France* 85 (1957), 431--458, DOI `10.24033/bsmf.1494`. The present proof does not rely on positivity or a probabilistic interpretation; `W` is complex-holomorphic and has zeros, so all statements are made componentwise away from its divisor and then extended only where analytically justified.

No novelty is claimed for the `h`-transform identity or for the theta divisor of XF-074. The line-specific delta is the architectural consequence obtained by combining that classical conjugation algebra with the exact Gaussian seam control: **reference-only multiplicative heat repair is unique and undoes the quotient, while reference-only additive pole subtraction fails on matched exact heat data**. A targeted search did not locate this specific Gaussian-Xi-to-periodic-Vieta no-go as a stated result.

Because the argument is self-contained and the Doob citation is used only to delimit the classical prior-art class rather than as a load-bearing theorem, no new `SOURCES.md` dependency is required.

## 6. Audit tests and evidence boundary

There are four direct checks. First, `A=W` must make the defect in (9) vanish identically; it does by `L_0W=0` and `W_z-Wb=0`. Second, allowing `A=c(t)W` must produce only the scalar defect `c'(t)Wf`; equation (12) gives exactly that. Third, the additive no-go must preserve the cancellation control `u=1`: it does, and that control is what forces any universal additive correction to be holomorphic at the seam before the pole-producing Fourier mode is tested. Fourth, none of the argument may use reality or simplicity of Xi zeros; it does not.

The scope is deliberately narrow. XF-075 does not rule out source-dependent multipliers or principal-part subtraction, nonlinear transformations of `R`, center-local weighted estimates, or finite approximate trigonometric surrogates. It also does not claim that the entire periodized numerator `V` is useless; it says only that multiplying the quotient by a universal reference correction cannot produce a **different** exact-heat carrier while retaining the quotient normalization. Finally, this is an interface obstruction, not a bound on the de Bruijn--Newman constant and not a consequence for RH.