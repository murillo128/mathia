# PL-192 — Escaping affine windows have recurrent nonflattening centers beyond the PNT horizon

## Claim

`PL-191` shows that the completely unweighted affine prime-phase carrier is uniformly flat on every fixed positive-width window whose normalized center escapes to infinity **inside** the current short-interval-PNT phase range. That does not extend to arbitrary escaping centers. For the same unweighted carrier, classical Bohr almost periodicity forces arbitrarily large recurrence centers at which a fixed-width window retains a uniform positive amount of mass.

Fix constants

\[
0<a<b<\infty,
\qquad \delta>0,
\]

and specialize the `PL-191` family to the admissible source scale

\[
h_X=X.
\]

Thus

\[
\mathcal P_X=\{q\text{ prime}:aX<q\le bX\},
\qquad M_X=|\mathcal P_X|,
\]

\[
\omega_X(q)=2\log\!\left(1+\frac{X}{q}\right),
\qquad
F_X(u)=\frac1{M_X}\sum_{q\in\mathcal P_X}e^{iu\omega_X(q)}.
\]

For all sufficiently large `X`, there exists a real center `T_X>X` such that

\[
\boxed{
\int_{T_X-\delta/2}^{T_X+\delta/2}|F_X(u)|^2\,du
\ge c_{a,\delta}>0,
}
\]

where `c_(a,delta)` is independent of `X`. In fact one may choose

\[
r_{a,\delta}
=\min\!\left\{\frac\delta2,\frac1{8\log(1+1/a)}\right\}>0
\]

and obtain

\[
\boxed{
|F_X(T_X+v)|\ge\frac12
\qquad (|v|\le r_{a,\delta}),
}
\]

so the integral is at least `r_(a,delta)/2`.

On the other hand, the **same** family satisfies the `PL-191` flattening statement at, for example,

\[
u_X=\log X:
\qquad
\sup_{|v|\le\delta/2}|F_X(\log X+v)|\longrightarrow0.
\]

Hence one and the same canonical matched control has two incompatible escaping-window subsequences:

\[
\boxed{
\text{subresolution escaping centers: flattening,}
\qquad
\text{recurrent superhorizon centers: nonflattening.}
}
\]

Therefore **center escape plus fixed positive width has no coefficient-blind asymptotic content at all once the center is unrestricted**. A target-specific theorem at an escaping phase must use an arithmetically prescribed center, additional coefficient/target structure, or a genuinely different joint/nonlocal observable. The mere fact that the observation window moves to high normalized phase cannot distinguish arithmetic cancellation from generic finite-frequency recurrence.

**Evidence/status:** `CLASSICAL-ALMOST-PERIODICITY + EXACT-DERIVED + DECISIVE-NEGATIVE` for any route

\[
\text{fixed positive affine phase width}
+\text{ arbitrary escaping center}
\longrightarrow
\text{universal scalar flattening/nonflattening law}
\longrightarrow
\text{RH-sensitive meaning}.
\]

No new theorem on almost-periodic functions is claimed. The durable line-specific content is the exact application to the remaining escaping-center branch after `PL-189`--`PL-191`, using the same unweighted rational-prime carrier on both the flat and recurrent sides.

## 1. Each finite prime-band carrier is a Bohr almost-periodic trigonometric polynomial

For fixed `X`, `F_X` is a finite trigonometric polynomial

\[
F_X(u)=\sum_{q\in\mathcal P_X}\frac1{M_X}e^{iu\omega_X(q)}.
\]

Every finite trigonometric polynomial with real frequencies is Bohr uniformly almost periodic. Equivalently, for every `epsilon>0`, its set of `epsilon`-almost periods

\[
E_X(\epsilon)
=
\left\{
\tau\in\mathbb R:
\sup_{u\in\mathbb R}|F_X(u+\tau)-F_X(u)|<\epsilon
\right\}
\]

is relatively dense in `R`. In particular `E_X(epsilon)` contains arbitrarily large positive numbers.

Take `epsilon=1/4`. For each sufficiently large `X`, choose

\[
T_X\in E_X(1/4),
\qquad T_X>X.
\]

Then

\[
\boxed{
\sup_{u\in\mathbb R}|F_X(u+T_X)-F_X(u)|<\frac14.
}
\]

The choice `T_X>X` is deliberate. It places the recurrence center safely beyond every phase range `X^(13/15-eta)` covered by `PL-191`, without making any claim about the size of the **first** recurrence time. Almost periodicity guarantees arbitrarily large recurrences but supplies no useful uniform upper bound as the number of prime frequencies grows.

The same conclusion can be phrased as recurrence of the finite-dimensional torus orbit

\[
u\mapsto(e^{iu\omega_X(q)})_{q\in\mathcal P_X};
\]

Kronecker/simultaneous approximation is a classical route to the same fact. No property special to zeta zeros or analytic continuation enters.

## 2. The profile around zero has a uniform coherent core when `h_X=X`

The specialization `h_X=X` is important only because it keeps the local frequencies in a fixed compact interval. For every `q>aX`,

\[
0<\omega_X(q)
=2\log\!\left(1+\frac Xq\right)
\le
\Omega_a:=2\log\!\left(1+\frac1a\right).
\]

Since `F_X(0)=1`, for every real `v`,

\[
|F_X(v)-1|
\le
\frac1{M_X}\sum_{q\in\mathcal P_X}|e^{iv\omega_X(q)}-1|
\le |v|\Omega_a.
\]

Put

\[
r_{a,\delta}
=
\min\!\left\{\frac\delta2,\frac1{4\Omega_a}\right\}
=
\min\!\left\{\frac\delta2,\frac1{8\log(1+1/a)}\right\}.
\]

Then for `|v|<=r_(a,delta)`,

\[
|F_X(v)|\ge\frac34.
\]

Combining this with the `1/4`-almost-period estimate gives

\[
|F_X(T_X+v)|
\ge
|F_X(v)|-|F_X(T_X+v)-F_X(v)|
>\frac12
\]

throughout the same fixed interval. Therefore

\[
\int_{T_X-\delta/2}^{T_X+\delta/2}|F_X(u)|^2du
\ge
\int_{-r_{a,\delta}}^{r_{a,\delta}}\frac14\,dv
=
\frac{r_{a,\delta}}2.
\]

This lower bound is independent of `X`. The recurrent window is not merely failing to converge uniformly to zero at one exceptional point; it carries a fixed positive `L^2` mass on a fixed-width subwindow.

## 3. The same carrier is flat on a different escaping-center sequence

Now keep exactly the same specialization `h_X=X` and take

\[
u_X=\log X.
\]

For every fixed `eta` with `0<eta<13/15`,

\[
\log X\le X^{13/15-\eta}
\]

for all sufficiently large `X`. Also `u_X->infinity`. Therefore `PL-191` applies and gives

\[
\sup_{|v|\le\delta/2}|F_X(\log X+v)|\longrightarrow0.
\]

Consequently

\[
\int_{\log X-\delta/2}^{\log X+\delta/2}|F_X(u)|^2du
\longrightarrow0.
\]

Together with the recurrent centers from the previous section, this proves the stronger matched-control statement:

\[
\lim_{X\to\infty}
\int_{\log X-\delta/2}^{\log X+\delta/2}|F_X(u)|^2du=0,
\]

while for a second sequence `T_X>X`,

\[
\liminf_{X\to\infty}
\int_{T_X-\delta/2}^{T_X+\delta/2}|F_X(u)|^2du
\ge \frac{r_{a,\delta}}2>0.
\]

Thus there is no single asymptotic regime indexed merely by the statement `center -> infinity`. The phase location itself carries essential information once one leaves the theorem-controlled one-point prime-density band.

## 4. Why this materially strengthens the boundary of `PL-191`

`PL-191` correctly treats `X^(13/15-o(1))` as a theorem-technology horizon inherited from the current short-interval prime number theorem. It leaves larger centers untreated rather than interpreting lack of control as arithmetic evidence.

The present finding adds a qualitatively different fact: **an unrestricted all-center extension of its flattening conclusion is actually false**, not merely unavailable by current methods. At sufficiently large specially recurrent centers, classical almost periodicity forces the unweighted finite prime-band carrier back near its low-frequency profile.

This does not promote the numerical exponent `13/15` into a sharp transition. Almost periodicity does not locate the first recurrence on a useful scale, and no assertion is made that nonflattening begins immediately beyond `X^(13/15)`. The comparison is only:

- inside the current polynomial resolution band, `PL-191` supplies a concrete escaping sequence such as `log X` with uniform flattening;
- with no upper restriction on the center, Bohr recurrence supplies another escaping sequence, which may be extremely large, with uniform nonflattening on a fixed subwindow.

Accordingly, “go to higher phase” is not itself an escape from the PNT universality results. A proposed high-phase statistic must specify **which** high phases are selected and why that selection is canonical/arithmetic rather than an almost-periodic recurrence artifact.

## 5. Relation to earlier prime-lattice recurrence and aliasing results

The mechanism is classical and several earlier findings already record nearby forms of recurrence, but none makes the present moving-window matched-control comparison.

- `PL-011` identifies the bare prime Kronecker flow as pure-point and almost periodic. The current `F_X` is a finite scalar matrix coefficient of exactly that general type; this is the main internal prior-art anchor for the recurrence step.
- `PL-067` shows that, after completed explicit-formula centering and second scaling, a zero-frequency series is uniformly almost periodic under RH and therefore generically has no limit. That is a zero-divisor signal already downstream of analytic continuation. Here the recurrence occurs **before** any zeta-zero input, in the ordinary finite prime-band carrier, and is used as a matched control.
- `PL-071` shows adaptive finite-horizon prime-character resonances are Diophantine-universal, while `PL-167` shows growing signed prime-log families create unresolved finite-height aliases. Those are frequency-selection statements on the dual prime lattice. The present result instead keeps the entire unweighted positive prime band fixed for each `X` and translates its scalar observation window by an almost period.
- `PL-191` is the immediate predecessor: it establishes genuine high-phase flattening in a large but bounded frequency range. The new point is that the same carrier must recur at sufficiently remote centers, so the escaping-center branch cannot be assigned a universal limit once the upper phase restriction is removed.

Thus this finding is not a new recurrence theorem. It closes a specific loophole created by the current affine-window trichotomy.

## Prior art and novelty audit

The analytic input is classical Bohr almost-periodicity. A finite generalized trigonometric polynomial is Bohr uniformly almost periodic, and the defining equivalent property is that every `epsilon>0` has a relatively dense set of uniform `epsilon`-almost periods. The compact-group/Kronecker version of this fact is already represented in the line literature ledger by Peter Walters, *An Introduction to Ergodic Theory* (Springer GTM 79, 1982), the general anchor for `PL-011`. Modern surveys and the Encyclopedia of Mathematics state the same Bohr characterization explicitly.

No external novelty is claimed for the recurrence theorem, for simultaneous approximation, or for the elementary coherent-core estimate. A targeted audit around Bohr almost periods, Kronecker approximation, finite trigonometric polynomials, and prime-frequency rotations found only this classical mechanism, not an arithmetic theorem that would attach zero-sensitive meaning to the recurrent centers.

The repository novelty audit compared the closest recurrence/aliasing findings `PL-011`, `PL-067`, `PL-071`, `PL-162`, and `PL-167`. They establish the general recurrence background, zero-ordinate phase recurrence, or finite-horizon aliasing, but do not combine that mechanism with the exact `PL-191` macroscopic prime-band carrier to produce two contradictory escaping-window asymptotics for the same matched control. The durable result is therefore the route restriction, not a claim of new harmonic analysis.

No update to `research/prime_lattice/SOURCES.md` is required: the classical compact-rotation/Kronecker anchor used here is already entry 22 and already supports the relevant recurrence background.

## Analytic-continuation and falsification controls

No Euler product, Dirichlet series, or analytically continued zeta identity appears in the proof. Every `F_X` is a finite prime sum. This is intentionally a **negative control**: the recurrent nonflattening cannot be evidence for RH because it occurs without zeta zeros or continuation.

The effect is also non-arithmetic in the required Beurling/Helson sense. Any finite real frequency list with a uniformly coherent low-frequency profile gives a trigonometric polynomial with arbitrarily large approximate periods. Rational-prime arithmetic supplies the particular frequencies, but does not supply the recurrence principle. Hence a construction that reads arithmetic significance directly from a recurrent high-phase window fails the line's matched-control gate.

The exact falsification points are elementary:

1. for fixed `X`, `F_X` must fail to be a finite trigonometric polynomial;
2. such a polynomial must fail to have arbitrarily large `1/4`-almost periods;
3. with `h_X=X`, some prime-band frequency must exceed `Omega_a=2 log(1+1/a)`;
4. the estimate `|F_X(v)-1|<=|v|Omega_a` must fail;
5. or `PL-191` must fail for the explicit flat center `u_X=log X`.

None of these points depends on an unproved statement about zeta zeros.

## Adversarial boundaries

This is a strong scalar matched-control obstruction, but its scope should not be enlarged.

- The recurrence centers `T_X` are chosen **after** the finite frequency set is known and may grow extraordinarily fast with `X`. No useful upper bound for `T_X` is proved. Therefore this does not obstruct a theorem for a separately prescribed center sequence lying in a quantified intermediate or super-polynomial range.
- The choice `h_X=X` is one admissible matched control. It is sufficient to disprove any coefficient-blind universal law for arbitrary source growth and arbitrary escaping centers. The argument is not claimed uniformly for all `h_X`; when `h_X/X` grows without bound, the local frequency diameter itself grows and the simple fixed-width coherent-core lower bound need not remain uniform.
- The result does not say that a hard target such as `mu(q+h)` or `lambda(q+h)` shares these recurrence centers. A target-dependent theorem may remain genuinely arithmetic if its coefficients prevent the matched-control reduction.
- The result concerns one scalar affine Fourier carrier. Joint prime-coordinate data, matrix-valued observables, completed Weil/Nyman couplings, nonlinear target-relative operators, and other nonlocal structures are not reduced to this argument.
- No claim is made that `13/15` is optimal or intrinsic. It remains the current short-interval-PNT resolution exponent; recurrence only proves that complete all-center flattening is impossible eventually.
- A recurrence center selected by an explicit arithmetic rule could still be meaningful. The negative result applies when “large phase” or “escaping center” itself is treated as the source of rigidity.

## Consequence for the research line

The scalar affine-window branch now has a complete qualitative warning that was missing after `PL-191`. Bounded-center positive-width flattening is rigid (`PL-189`); shrinking windows reduce to pointwise readout (`PL-190`); subresolution escaping positive-width windows can be generically flat (`PL-191`); and unrestricted escaping centers necessarily include generic almost-periodic returns with fixed positive local mass (`PL-192`).

Therefore the next scalar candidate cannot be justified by window geometry alone on **either** side of the current PNT horizon. It must provide a canonical arithmetic prescription for the observation center and a target-specific estimate at that center, or else leave the scalar one-measure affine reduction through a genuinely joint, nonlocal, completed, or parity-tail-sensitive coupling. High phase without such extra structure is ambiguous between ordinary PNT dephasing and ordinary Bohr recurrence.