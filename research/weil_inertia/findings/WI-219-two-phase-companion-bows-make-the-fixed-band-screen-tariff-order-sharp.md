# WI-219 — two-phase companion bows make the fixed-band screen tariff order-sharp

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + CLASSICAL-IDENTITY`.

WI-218 proves that a screen which makes the selected Maynard--Pratt bow residue subdiagonal throughout a fixed power-scale band must spend a positive-density number of exponential channels: `n(T) \gg M`. The natural next hope is that the same fixed-band observable might force a *superlinear* screen cost, which could turn the rank tariff into a contradiction without first solving the source-localization problem.

That hope is false at the level of the current bow-plus-screen interface. There is an explicit symmetry-respecting companion screen with only `Theta(M)` additional off-line functional-equation pairs, at the **same bounded normalized horizontal depth as the bow**, whose residual is uniformly `O(1)` before the `1/M` bow normalization on an entire fixed neighborhood of any reciprocal harmonic. After normalization and the exact WI-218 box operator, its selected Gallagher energy is `O(1/M)` of the raw-prime diagonal on every fixed-multiplicative subslab of that band.

Thus the `Omega(M)` complexity in WI-218 is order-sharp. No argument which sees only the finite bow profile, functional-equation/conjugation symmetry, critical-strip admissibility, and the fixed-band selected Gallagher energy can upgrade the screen tariff to `omega(M)`. The remaining leverage must come from information deliberately absent from this interface: local Riemann--von Mangoldt count/localization, source-specific `Lambda-Lambda^sharp` structure, or another invariant coupling the companion screen to fresh arithmetic cost.

The explicit companion is **not** a zeta-zero counterexample. It is co-localized with the bow and grossly exceeds the local zero-count budget in the count-saturating `2<d<3` regime. That failure is the point: the analytic fixed-band rank interface has reached its asymptotic ceiling, and the next theorem must consume the local-count/source constraint rather than ask the same interface for a larger rank constant.

## 1. Equal-depth bow and a symmetry-safe companion

Retain the WI-214--WI-218 normalization. Let `M=2p+1` be odd and

\[
D_M(t)
:=\sum_{j=-p}^{p}e^{2\pi ijt}
=\frac{\sin(\pi Mt)}{\sin(\pi t)}.
\tag{1}
\]

For fixed normalized horizontal depth `h>0`, the equal-depth functional-equation-symmetrized bow is

\[
B_M(t):=2\cosh(ht)D_M(t).
\tag{2}
\]

Fix a positive reciprocal harmonic `k<d`, and choose a fixed

\[
0<\sigma<\min\!\left(\frac12,k,d-k\right).
\tag{3}
\]

Define the two-phase companion screen

\[
\boxed{
S_M(t)
:=2\cosh(ht)D_M(t)
\left(
 e^{2\pi i t/(3k)}+e^{-2\pi i t/(3k)}
\right).
}
\tag{4}
\]

Expanding `D_M`, (4) is exactly the sum of the `2M` functional-equation pairs

\[
2\cosh(ht)e^{2\pi i(j+1/(3k))t},
\qquad
2\cosh(ht)e^{2\pi i(j-1/(3k))t},
\qquad -p\le j\le p.
\tag{5}
\]

Every pair has the same radial parameter `h` as the selected bow. The phase set is exactly closed under frequency negation, because

\[
-(j+1/(3k))=(-j)-1/(3k),
\]

and likewise with the signs exchanged. Thus the positive-height packet is already closed under the conjugation reflection used in WI-214, while the factor `2 cosh(ht)` supplies the same-ordinate functional-equation mirror. No free complex coefficients or negative multiplicities are being introduced.

At the center harmonic,

\[
e^{2\pi i/3}+e^{-2\pi i/3}=-1,
\]

so

\[
\boxed{S_M(k)=-B_M(k).}
\tag{6}
\]

The issue is whether this cancellation survives the entire fixed band rather than only the center. It does, with a much stronger uniform bound than is needed.

## 2. The residual is uniformly bounded on the whole fixed band

Put

\[
P_k(t):=1+2\cos\!\left(\frac{2\pi t}{3k}\right).
\tag{7}
\]

Then

\[
R_M(t):=B_M(t)+S_M(t)
=2\cosh(ht)D_M(t)P_k(t).
\tag{8}
\]

Since `P_k(k)=0` and

\[
|P_k'(t)|\le \frac{4\pi}{3k},
\]

the mean-value theorem gives, for `|t-k|<=sigma`,

\[
|P_k(t)|
\le \frac{4\pi}{3k}|t-k|.
\tag{9}
\]

Write `delta=t-k`. Because `k` is an integer and `|delta|<1/2`, the Dirichlet-kernel formula gives

\[
|D_M(k+\delta)|
=\frac{|\sin(\pi M\delta)|}{|\sin(\pi\delta)|}
\le \min\!\left(M,\frac1{2|\delta|}\right),
\tag{10}
\]

where `|sin(pi delta)|>=2|delta|` on `|delta|<=1/2`. Combining (9)--(10), with the value at `delta=0` obtained by continuity,

\[
|D_M(t)P_k(t)|\le\frac{2\pi}{3k}.
\tag{11}
\]

Therefore

\[
\boxed{
\sup_{|t-k|\le\sigma}|R_M(t)|
\le
\frac{4\pi}{3k}\cosh\!\bigl(h(k+\sigma)\bigr),
}
\tag{12}
\]

uniformly in `M`.

This is the key sharpness mechanism. The bow itself has height `Theta(M)` in its natural `1/M` neighborhood of `k`. The companion phase factor has a simple zero at exactly that peak, so its `O(|t-k|)` defect cancels the `O(1/|t-k|)` Dirichlet shoulder. Away from the peak the Dirichlet kernel is already `O(1)`. The whole fixed band therefore costs only a bounded residual, not merely a small relative error at one reciprocal sample.

The construction is elementary finite Fourier algebra. The only classical input is the Dirichlet-kernel identity (1); the phase filter (7) and the uniform estimate (12) are exact deductions here.

## 3. The exact WI-218 source box remains subdiagonal

Return to the natural coordinate

\[
s=M(t-k)
\tag{13}
\]

and divide by the bow population. Define

\[
r_M(s):=\frac1M R_M\!\left(k+\frac{s}{M}\right).
\tag{14}
\]

Equation (12) gives

\[
\boxed{
|r_M(s)|\ll_{h,k,\sigma}\frac1M
}
\tag{15}
\]

uniformly for `|s|<=sigma M`.

WI-218 removes the harmless outer exponential tilt and works with the exact unit-box operator

\[
(K_{\eta_M}f)(s)
:=\int_0^1e^{\eta_M v}f(s+v)\,dv,
\qquad
\eta_M=\frac{\log T}{2dM}.
\tag{16}
\]

On any slightly smaller fixed band, so that `[s,s+1]` stays inside `|s|<=sigma M`, (15) implies directly

\[
\boxed{
|K_{\eta_M}r_M(s)|
\ll_{h,k,\sigma}\frac1M.
}
\tag{17}
\]

Hence on the whole fixed band

\[
\int |K_{\eta_M}r_M(s)|^2ds
=O_{h,k,\sigma}(M^{-1}),
\tag{18}
\]

and on every fixed-multiplicative subslab, whose natural-coordinate length is

\[
Q\asymp\frac{M}{\log T},
\]

one has

\[
\boxed{
\int_{\text{subslab}}|K_{\eta_M}r_M(s)|^2ds
=O\!\left(\frac1{M\log T}\right).
}
\tag{19}
\]

The exact physical dictionary in WI-217--WI-218 multiplies such a normalized subslab integral by a factor `asymp log T` when it is divided by the matching raw-prime Gallagher diagonal. Therefore (19) gives

\[
\boxed{
\frac{\text{selected bow+screen Gallagher energy}}
{\text{raw-prime Gallagher diagonal}}
=O(M^{-1})=o(1)
}
\tag{20}
\]

on **every** fixed-multiplicative subslab contained in the chosen power-scale band.

Thus this is not another discrete reciprocal-sample screen of the WI-211--WI-212 type, nor merely the natural `1/M` continuum screen of WI-214. It passes the stronger fixed-band source test that generated the positive-density lower tariff in WI-218.

## 4. Complexity and critical-strip cost

The screen (5) uses exactly `2M` additional off-line functional-equation pairs. In the exponential-channel bookkeeping of WI-214--WI-218, each such pair contributes its two radial exponentials, so the effective channel rank is at most

\[
\boxed{n=4M.}
\tag{21}
\]

No attempt is made to optimize the constant `4`. The asymptotic conclusion is what matters: a `Theta(M)` screen exists. Since WI-218 proves that a fixed fractional rank deficit below `cM` leaves a positive selected residue on some slab, the lower and upper constructions now match in order:

\[
\boxed{
\text{fixed power-scale band screening complexity}=\Theta(M)
}
\tag{22}
\]

within the free bow-plus-exponential-screen interface.

The radial cost is also minimal in the relevant sense. WI-214's source dictionary converts a fixed radial parameter `a` into

\[
\beta=\frac12+\frac{da}{\log T}.
\tag{23}
\]

Here `a=h` for both the bow and the companion. Consequently every added pair lies at

\[
\boxed{
\beta_{\rm scr}=\frac12+\frac{dh}{\log T},
}
\tag{24}
\]

which is strictly inside the critical strip for all sufficiently large `T` and has the same bounded normalized horizontal depth as the original bow. The matching `Theta(M)` upper screen therefore does not need the logarithmically deep phase-filter layers used by the sparse WI-214 construction.

This cleanly interpolates the existing barriers. Sparse or polylogarithmic screens can handle only narrow natural neighborhoods and must pay radial depth; once a full fixed exponent band is demanded, WI-218 forces positive-density complexity, and the present companion shows that positive-density complexity can pay the whole bill while staying near the critical line.

## 5. Why this is not a zeta countermodel: local count rejects the companion

The screen phases in (5) differ from the bow phases only by the fixed offsets `+/-1/(3k)`. Under the source dictionary their ordinate offsets differ from the original bow by only `O(1/log T)`, so the companion occupies the same `Theta(M/log T)` positive-height interval up to an `O(1/log T)` boundary enlargement.

The original symmetrized bow already contributes `2M+O(1)` positive-height zero labels: `M` right-half labels and their compulsory same-ordinate mirrors. The screen contributes another `4M` positive-height labels because its `2M` functional-equation pairs contain two zeros each. Thus the co-localized configuration uses

\[
\boxed{6M+O(1)}
\tag{25}
\]

positive-height zero labels.

By WI-210, Riemann--von Mangoldt supplies only

\[
(d+o(1))M
\tag{26}
\]

labels on the corresponding bow interval. In the principal two-harmonic regime `2<d<3`, and indeed for every fixed `d<6`, the explicit companion cannot be an actual local zeta-zero configuration.

This is not a defect in the sharpness result. It identifies exactly which information is missing from the free screen interface. WI-218's linear-algebra argument cannot know that its `Theta(M)` channels would have to be paid for by zero labels in a locally count-limited interval. The present screen proves that **without consuming that localization/count fact, no superlinear rank theorem is available from the fixed-band profile itself.**

A remote screen remains a logically different possibility: moving the companion phases by `Theta(M)` or more changes their natural `1/M` peak profile and the simple cancellation (12), so the displayed construction does not show that remote zeta zeros can realize the same effect. Establishing or excluding such transport is precisely the surviving localization/source problem already isolated by WI-218 and `MI-014`.

## 6. Prior-art, novelty, and falsification audit

The finite geometric-series/Dirichlet-kernel identity is classical Fourier analysis. A targeted prior-art search around shifted Dirichlet kernels, phase-filter cancellation, and exponential screens found the standard frequency-shift and Dirichlet-kernel identities, but no zeta-specific statement that the two conjugation-closed shifts `+/-1/(3k)` make the WI-218 fixed-band screen tariff order-sharp. Absence from that search is not used as a priority claim.

The nearby Mathia results are genuinely different. WI-211--WI-212 screen finitely many reciprocal samples. WI-214 uses a growing but zero-density screen to flatten two natural `1/M` continuum windows. WI-215--WI-217 prove that widening the observation increases the required rank, culminating in `M/log T` on one fixed-multiplicative slab. WI-218 stacks `Theta(log T)` such slabs and obtains the `Omega(M)` positive-density tariff. The new exact deduction is the matching symmetry-safe `O(M)` upper construction (4)--(20) on that same fixed-band observable.

The finding would fail if any of the following were wrong: the expansion (5) into functional-equation pairs, the conjugation closure of the two shifted phase sets, the simple-zero estimate (9) for the phase filter, the Dirichlet bound (10), or the WI-217--WI-218 conversion from normalized box energy to the raw-prime diagonal. No unproved zeta theorem or numerical certificate enters.

The boundary is equally important. This result does **not** assert that zeta has the companion zeros, that the full `Lambda-Lambda^sharp` source term can be screened, or that remote zeros can evade local count. It proves only that the current fixed-band bow-plus-screen interface cannot demand more than linear screen complexity, even after functional-equation/conjugation symmetry and near-line critical-strip admissibility are enforced.

## Research consequence

Do not spend further cycles trying to strengthen WI-218 from `Omega(M)` to `omega(M)` using only more translation-nullspace bookkeeping or the same fixed-band selected-residue norm. The linear tariff is already order-sharp.

The RH-facing gate is now narrower: **convert the linear screen tariff into an actual local zero-count charge, or prove that transporting a `Theta(M)` companion screen outside the bow interval necessarily pays a source-energy/radial penalty.** The explicit companion above shows why that extra theorem must use information beyond the current profile/rank interface.
