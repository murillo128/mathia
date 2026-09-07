# XF-087 — periodic power-sum heat is the exact Volterra trapezoid discretization

**Status:** `EXACT-DERIVED` + `STRUCTURAL/BRIDGE` + `DISCRETE-CONTINUOUS-COMPATIBILITY` + `COLLISION-SAFE`. XF-086 closes the static equal-weight real-divisor gate for every guarded moment vector in the resource regime already used by the Xi-flow architecture. What remained was described as a separate heat-compatibility problem: even if one can realize the source-visible moments by exactly `N` real periodic roots at one time, why should the subsequent periodic heat state have anything to do with the canonical Xi Burgers/Volterra transport of XF-051?

There is an exact answer at the level of the source-visible power sums. The periodic power-sum ODE obtained from the XF-071 log-Vieta system is **precisely the composite trapezoidal-rule semidiscretization in positive frequency of the XF-049/XF-051 Volterra equation**. The two half-weight endpoint samples are not a numerical artifact: together they produce exactly the flat-density damping term already identified in XF-049. Thus the periodic carrier is not an unrelated nonlinear heat model whose compatibility has to be separately engineered. Once its first `K` moments are fixed, their periodic heat evolution is the canonical one-sided Volterra vector field with the continuum convolution replaced by its natural frequency-grid trapezoid rule.

Concretely, write

\[
\Delta:=\frac{2\pi}{L},
\qquad
\xi_m:=m\Delta,
\qquad
a:=\Delta^2,
\qquad
P_m(t):=\sum_{j=1}^N e^{-i\xi_m x_j(t)},
\tag{1}
\]

and set `P_0=N`. For every `1<=m<=N`, the exact periodic heat flow satisfies

\[
\boxed{
P_m'
=\xi_m^2P_m
-\xi_m\,\Delta\!\left[
\frac12P_0P_m
+\sum_{i=1}^{m-1}P_iP_{m-i}
+\frac12P_mP_0
\right].
}
\tag{2}
\]

Compare this with the canonical finite/infinite positive-frequency heat-zero law of XF-049/XF-051,

\[
\boxed{
\partial_t Z(\xi)
=\xi^2Z(\xi)
-\xi\int_0^\xi Z(\eta)Z(\xi-\eta)\,d\eta.
}
\tag{3}
\]

The bracket in `(2)`, multiplied by `Delta`, is exactly the composite trapezoidal rule for the convolution integral in `(3)` on the mesh `0,Delta,...,mDelta`. No approximation enters `(2)`: it is an identity of the exact finite periodic backward heat flow, valid through root collisions and complex-root intervals because it follows from Vieta coefficients.

This changes the live source bridge. XF-085--XF-086 already say that a guarded finite moment state can be realized exactly by a degree-`N` real divisor. XF-087 says that, after that one-time realization, **the first `K` periodic moments have an exact closed heat evolution determined only by those same first `K` moments**, and that evolution is the frequency-grid Volterra scheme for the actual Xi carrier. The remaining dynamic interface is therefore a quantitative continuum-to-grid consistency/stability estimate for the Volterra convolution, including its singular endpoint/background renormalization. It is not a separate nonlinear root-placement or heat-compatibility existence theorem.

## 1. The XF-071 log-Vieta system gives an exact power-sum ODE

XF-071 writes the normalized periodic Vieta polynomial as

\[
E(z,t)=\sum_{k=0}^{N}E_k(t)z^k,
\qquad E_0=1,
\tag{4}
\]

with exact coefficient heat flow

\[
E_k'=-a k(N-k)E_k,
\tag{5}
\]

and formal logarithm

\[
C(z,t)=\log E(z,t)=\sum_{m\ge1}c_m(t)z^m.
\tag{6}
\]

For the XF-070 sign convention

\[
P_m=\sum_{j=1}^{N}e^{-2\pi i m x_j/L},
\tag{7}
\]

Newton's generating identity gives

\[
c_m=(-1)^{m-1}\frac{P_m}{m}.
\tag{8}
\]

XF-071 derives the exact triangular Burgers system

\[
c_m'
=-a m(N-m)c_m
+a\sum_{i=1}^{m-1}i(m-i)c_i c_{m-i}.
\tag{9}
\]

Multiply `(9)` by `(-1)^{m-1}m` and use `(8)`. Since

\[
i(m-i)c_i c_{m-i}
=(-1)^mP_iP_{m-i},
\tag{10}
\]

one obtains, with no estimate,

\[
\boxed{
P_m'
=-a m(N-m)P_m
-a m\sum_{i=1}^{m-1}P_iP_{m-i}.
}
\tag{11}
\]

Equivalently,

\[
P_m'
=a m^2P_m
-a m\left(
NP_m+\sum_{i=1}^{m-1}P_iP_{m-i}
\right).
\tag{12}
\]

This formula is valid for `1<=m<=N`, which is more than enough for the Xi source-visible range because XF-083--XF-086 use `K=o(N)`. It is coefficient-level and therefore does not require the roots to remain real or simple after the initial real-divisor realization.

## 2. The nonlinear term is exactly a trapezoidal convolution

For a sequence sampled on the frequency grid `xi_i=i Delta`, define the composite trapezoidal convolution at `xi_m` by

\[
\mathcal T_\Delta(P,P)(\xi_m)
:=
\Delta\left[
\frac12P_0P_m
+\sum_{i=1}^{m-1}P_iP_{m-i}
+\frac12P_mP_0
\right].
\tag{13}
\]

Because `P_0=N`, the two endpoint halves combine to

\[
\mathcal T_\Delta(P,P)(\xi_m)
=\Delta\left[
NP_m+\sum_{i=1}^{m-1}P_iP_{m-i}
\right].
\tag{14}
\]

Using `xi_m=m Delta` and `a=Delta^2`, equation `(12)` becomes exactly

\[
\boxed{
P_m'
=\xi_m^2P_m
-\xi_m\mathcal T_\Delta(P,P)(\xi_m).
}
\tag{15}
\]

Equation `(15)` is the ordinary method-of-lines frequency discretization of `(3)` obtained by replacing the Volterra integral by the composite trapezoidal rule. More strongly, here the discretization is not imposed numerically: it is the algebraic evolution law forced by the exact periodic trigonometric heat carrier.

This explains why the one-sided triangularity of XF-051 and the one-sided triangularity of XF-071 have matched so persistently. They are the continuum and frequency-lattice forms of the same quadratic Volterra law. In particular, for each `m`, both vector fields use only indices/frequencies at or below the target.

## 3. The trapezoid endpoints reproduce the exact flat-density Cauchy clock

The endpoint term in `(14)` is load-bearing. Let

\[
\rho:=\frac NL
\tag{16}
\]

be the mean root density of the periodic carrier. Since `N Delta=2 pi rho`, the linear part of `(15)` is

\[
\xi_m^2P_m-\xi_m\Delta N P_m
=
\boxed{
(\xi_m^2-2\pi\rho\,\xi_m)P_m.
}
\tag{17}
\]

XF-049 independently obtains exactly the multiplier

\[
\lambda_\rho(\xi)=\xi^2-2\pi\rho\xi
\tag{18}
\]

by linearizing the continuous Burgers field about a flat zero density. Thus the diagonal periodic Vieta rate

\[
-a m(N-m)
\tag{19}
\]

is not merely asymptotic to the continuum Cauchy clock: after the frequency identification `xi_m=m Delta`, it is **exactly** the same flat-density multiplier. The two half endpoint weights in the trapezoidal convolution are precisely what supplies the `-2 pi rho xi` background term.

This is a stringent sign and normalization check. Dropping the endpoints would leave the anti-diffusive `+xi^2` term and would fail both XF-049 and the exact Vieta damping. Counting both endpoints at full weight would double the density term and would also be wrong. The half-weight trapezoid is forced exactly.

## 4. Exact first-`K` moment realization is already an exact closed periodic heat state

The main consequence concerns the static carrier theorem of XF-085--XF-086. Suppose at time `t_0` one constructs exactly `N` unit-circle nodes with prescribed moments

\[
P_m(t_0)=Q_m,
\qquad 1\le m\le K<N.
\tag{20}
\]

The particular positions of those roots, their ordering, repeated nodes, and every moment above `K` may vary among different realizations. Nevertheless equation `(11)` is triangular in `m`. Hence two degree-`N` periodic carriers with the same prefix `(P_1,...,P_K)` at `t_0` satisfy

\[
\boxed{
P_m^{(1)}(t)=P_m^{(2)}(t),
\qquad 1\le m\le K,
}
\tag{21}
\]

for every common heat time for which the coefficient flow is considered. This follows simply by uniqueness of the finite triangular polynomial ODE; root labels and reality play no role.

Therefore the equal-weight realization supplied by XF-085 is stronger dynamically than a one-slice existence statement might suggest. Once it reproduces the first `K` moments, it automatically determines **the** periodic first-`K` heat trajectory associated with that prefix. There is no additional choice of high modes or hidden root geometry capable of changing the guarded low-frequency evolution.

This does not yet identify that trajectory with Xi. The actual continuum law `(3)` evaluates a genuine integral over every intermediate frequency, whereas `(15)` uses only the grid samples. But the discrepancy is now isolated to one explicit operation: continuum Volterra convolution versus its trapezoidal quadrature.

## 5. Smooth continuum fields give the expected consistency estimate

For calibration only, suppose `Z` is an ordinary `C^2` function on `[0,xi_m]` and define

\[
f_m(\eta):=Z(\eta)Z(\xi_m-\eta).
\tag{22}
\]

The elementary composite trapezoidal error bound gives

\[
\left|
\mathcal T_\Delta f_m
-\int_0^{\xi_m}f_m(\eta)\,d\eta
\right|
\le
\frac{\xi_m\Delta^2}{12}
\|f_m''\|_{L^\infty(0,\xi_m)}.
\tag{23}
\]

Consequently the mismatch between the discrete and continuum Volterra vector fields at the grid mode is bounded by

\[
\boxed{
|\operatorname{Err}_m|
\le
\frac{\xi_m^2\Delta^2}{12}
\|f_m''\|_{L^\infty(0,\xi_m)}.
}
\tag{24}
\]

On the current Xi scaling,

\[
L\asymp\log^3T,
\qquad
\Delta\asymp\log^{-3}T,
\qquad
K=O(\log^2T\,\log\log T),
\tag{25}
\]

so

\[
\xi_K=K\Delta
=O\!\left(\frac{\log\log T}{\log T}\right)
\longrightarrow0.
\tag{26}
\]

Thus an ordinary uniformly smooth renormalized convolution profile would leave enormous consistency margin. Equation `(24)` is not used as an Xi theorem, however. XF-051 emphasizes that the actual positive-frequency Xi carrier is a distribution with a singular endpoint at `xi=0`; a naive `C^2` bound across that endpoint is unavailable and would simply assume away the difficult part.

The value of `(23)`--`(24)` is to identify the precise pathology that can still defeat the bridge: after the deterministic density/archimedean background is separated in a source-faithful way, the residual endpoint regularity must be strong enough for the trapezoidal convolution error to be small in the guarded `X(B)` resource. If that fails, the leading quadrature defect gives a concrete obstruction rather than an unspecified periodic-localization error.

## 6. Stress tests

**First mode.** For `m=1`, the interior convolution sum is empty and `(11)` gives

\[
P_1'=-a(N-1)P_1.
\tag{27}
\]

The trapezoidal form gives `xi_1^2-aNP_1/P_1=a-aN`, exactly the same rate. This is also the `k=1` Vieta eigenvalue of XF-067.

**Degree two.** For `N=2`, `P_1'=-aP_1` while

\[
P_2'=-2aP_1^2.
\tag{28}
\]

Newton's identity `P_2=E_1^2-2E_2`, together with `E_1'=-aE_1` and `E_2'=0`, gives `(28)` directly.

**Arithmetic lattice.** For equally spaced periodic roots, `P_m=0` for `1<=m<N`. Equation `(11)` then keeps every such mode zero, as required by stationarity of the lattice modulo the common heat normalization.

**Translation covariance.** Translating every root by `b` multiplies `P_m` by `e^{-i xi_m b}`. Every term in `(15)` acquires the same phase because `xi_i+xi_{m-i}=xi_m`, matching the translation covariance of XF-049.

**Collisions and complex roots.** The derivation uses the coefficient identity `(9)`, not the real-simple particle ODE. Therefore `(11)`--`(15)` continue through the discriminant exactly as XF-067--XF-071 do.

**No aliasing in the live band.** The statement is restricted to `m<=N`. The Xi architecture uses `K=o(N)`, so the entire source/destination band lies strictly inside this nonwrapped triangular sector. Nothing here asserts an unrestricted convolution law for arbitrarily high periodic power sums.

## 7. Consequence for the live Xi bridge

After XF-087, the phrase “make the realized real divisor heat-compatible” should not be treated as a third independent existence problem. The local architecture can be decomposed more sharply:

1. extract a finite target moment state from the actual Xi Gaussian/reference description with controlled guarded resource;
2. realize that state exactly by `N` equal-weight unit-circle roots using XF-085--XF-086;
3. compare the actual continuum Volterra flow `(3)` with the exact periodic trapezoidal flow `(15)` on the guarded frequency grid, allowing XF-071 to quotient the unresolved infrared completion;
4. separately prove that a hypothetical positive-`Lambda` transition forces nontrivial mass in the same destination resource.

Step 2 already fixes the periodic first-`K` heat trajectory; no further nonlinear root matching is needed. Step 3 is the genuine remaining dynamic interface. Its hard feature is precisely the endpoint/background structure identified by XF-051, not generic root collisions, high-mode dependence, or arbitrary periodic heat dynamics.

This also suggests a cleaner falsification target. A negative result should exhibit an Xi-compatible endpoint/background profile for which the trapezoidal convolution defect stays order one in the guarded band despite `Delta -> 0`, or prove that the source-to-grid sampling needed to define the target moments is unstable at the available relative precision. Generic counterexamples that merely choose different high periodic moments cannot affect the first `K` trajectory by `(21)`.

## 8. Prior-art and novelty boundary

The ingredients are classical separately. Backward heat on trigonometric polynomials and the unitary-polynomial viewpoint are represented in the line's existing Kabluchko anchor. Cole--Hopf/Burgers pole dynamics and the one-sided Volterra representation are classical structures already calibrated in XF-049 and XF-051. Composite trapezoidal quadrature and its `C^2` error estimate are standard numerical analysis; the line already contains a trapezoidal/Euler--Maclaurin anchor for a different lattice-to-continuum step.

A targeted literature search found the expected Burgers pole-decomposition, Calogero--Moser/Sutherland, trigonometric heat-flow, and numerical Burgers literatures, but did not identify a source used here for the exact finite identity `(15)` as the bridge between the periodic Vieta state and the Xi positive-frequency Volterra carrier. No broad novelty claim is made for the classical components or for the trapezoidal scheme itself.

The durable Mathia delta is the exact **interface identification**: the nonlinear periodic power-sum heat flow already derived internally is not merely analogous to the Xi Burgers carrier; mode by mode below the degree barrier it is its composite-trapezoid frequency discretization, with the endpoint weights reproducing exactly the known flat-density Cauchy damping. This converts an open qualitative heat-compatibility obligation into one explicit quantitative continuum-to-grid stability estimate matched to the existing guarded resource.
