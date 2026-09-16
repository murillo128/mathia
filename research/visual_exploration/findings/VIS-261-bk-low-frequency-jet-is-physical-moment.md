# VIS-261 — the low-frequency Bogomolny--Keating arithmetic jet is exactly a hierarchy of physical-space moments

## Claim

Use Rodgers' fixed-margin pair-correlation setting from `VIS-260`, and fix a real even admissible weight `omega`. Let `BK_T(alpha)` denote the Bogomolny--Keating prediction in Theorem 1.4 and let `GUE_T(alpha)` denote the matched naive GUE prediction obtained by replacing Rodgers' arithmetic kernel `Q_t(u)` by the sine-kernel term `K_t(u)` discussed immediately after that theorem. Define the arithmetic residual

`R_T(alpha)=BK_T(alpha)-GUE_T(alpha)`.

Writing the prediction difference in physical separation variable `u`, there is a real even integrable kernel `D_T(u)` such that

`R_T(alpha)=int_R D_T(u) exp(i alpha log(T) u) du`.

For every integer `j>=0` for which the corresponding weighted moment is finite,

`R_T^(2j)(0)=(-1)^j log(T)^(2j) M_(2j)(T)`,

where

`M_(2j)(T)=int_R u^(2j) D_T(u) du`.

All odd derivatives vanish. Therefore the first nonzero even Taylor coefficient of the explicit Bogomolny--Keating-minus-GUE prediction is not a new frequency-side object: it is exactly the first nonzero even weighted physical-space moment of the arithmetic kernel difference.

Now take the symmetric sharp cusp-adapted packet from `VIS-259`, supported on `[-b,b]`, annihilating mass, `|alpha|`, and the even moments through order `2m-2`, normalized by

`int alpha^(2m) dnu_b(alpha)=1`,

with optimal total variation

`||nu_b||_TV=E_m^(-1)b^(-2m)`.

If `R_T` is `C^(2m+2)` on `[-b,b]`, then

`int R_T(alpha) dnu_b(alpha)`
` = R_T^(2m)(0)/(2m)! + Rem_(m,T,b)`

and

`|Rem_(m,T,b)|`
` <= [E_m^(-1)b^2/(2m+2)!] sup_(|alpha|<=b)|R_T^(2m+2)(alpha)|`.

Thus the packet does exactly what the support-edge program needs at the prediction level: after the declared nuisance cancellations, it extracts the `2m`-th arithmetic jet with a remainder that gains two powers of bandwidth relative to the sharp packet-conditioning cost.

Combining this with `VIS-260`, the fixed-margin observed zeta statistic can distinguish that arithmetic jet from the matched GUE prediction using Rodgers' theorem only if the retained coefficient dominates **both**

`E_m^(-1)b^2 sup|R_T^(2m+2)|/(2m+2)!`

and

`C T^(-delta) E_m^(-1)b^(-2m)`,

for some fixed `delta<epsilon/2` in the theorem's fixed support margin. For `b=T^(-beta)`, the second term can vanish only in the already established regime `beta<epsilon/(4m)`.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BRIDGED FOURIER REDUCTION + QUANTITATIVE SOURCE-CARRIER GATE + NO-NOVELTY-CLAIM`.

No claim is made here that `M_2(T)`, `M_4(T)`, or any higher moment is nonzero, has a favorable sign, or is large enough to beat the displayed errors. Computing the first nonzero moment is the remaining source-specific question.

## 1. Source, transform, and target representations

The source representation is Rodgers' physical pair-separation variable `u`. In Theorem 1.4 the Bogomolny--Keating prediction is the Fourier transform, in `u`, of the smoothed pair-density kernel containing `Q_t(u)`. Rodgers also records the matched naive GUE prediction obtained by replacing `Q_t(u)` with

`K_t(u)=-(log(t/2pi)/(2pi))^2 K((log(t/2pi)/(2pi))u)`,

where `K(x)=(sin(pi x)/(pi x))^2`.

After averaging in `t` exactly as in the theorem and multiplying by the fixed weight `omega(u)`, define `D_T(u)` to be the resulting Bogomolny--Keating-minus-GUE kernel. Rodgers defines `Q_t` continuously at `u=0`; `K_t` is even and regular there. With a real even `omega`, `D_T` is real and even.

The transformed representation is frequency `alpha`:

`R_T(alpha)=int D_T(u) e(alpha log(T)u/(2pi)) du`
`          =int D_T(u) exp(i alpha log(T)u) du`,

using Rodgers' convention `e(x)=exp(2pi i x)`.

The target-relevant representation is only the low-frequency jet seen by a compact signed packet. Passing from `D_T` to finitely many derivatives of `R_T` preserves the corresponding weighted moments exactly, but forgets the rest of the physical-space shape. Different arithmetic kernels can share the same finite moment list, so a finite jet is a carrier test, not a reconstruction of the full Bogomolny--Keating correction.

## 2. Fourier differentiation turns the source coefficient into a moment

Because the fixed smooth weight has rapidly decaying physical-space tails and Rodgers' prediction is integrable against it, differentiation under the integral is legitimate whenever the displayed weighted moment is finite. For any integer `k>=0`,

`R_T^(k)(alpha)`
` = (i log T)^k int u^k D_T(u) exp(i alpha log(T)u) du`.

At `alpha=0`, evenness of `D_T` kills every odd moment. Hence

`R_T^(2j)(0)`
` = (i log T)^(2j) int u^(2j)D_T(u)du`
` = (-1)^j log(T)^(2j) M_(2j)(T)`.

Equivalently, the coefficient of `alpha^(2j)` is

`A_(2j)(T)`
` = (-1)^j log(T)^(2j) M_(2j)(T)/(2j)!`.

This is the exact dictionary that was missing after `VIS-260`. The vague task "compute the first surviving Bogomolny--Keating frequency coefficient" is reduced to the concrete source-side task "compute the first nonzero even weighted moment of `D_T`".

The reduction does not make that moment easy. `D_T` contains the difference between Rodgers' explicit arithmetic `Q_t` and the GUE sine-kernel prediction, including the zeta, prime-sum, and Euler-product terms recorded in Theorem 1.3. The point is only that there is now a unique physical-space scalar to compute at each candidate order.

## 3. A sharp packet extracts one jet and pays only a two-order Taylor remainder

Use the symmetric extremal packet guaranteed by `VIS-259`. Symmetry is harmless because `R_T` is even: replacing any packet by its reflection average leaves its pairing with `R_T` unchanged and cannot increase total variation.

Taylor-expand `R_T` on `[-b,b]` through order `2m`. The packet annihilates the constant and all preceding even powers, while odd powers pair to zero by symmetry. Its normalized `2m`-th moment is one. Therefore

`int R_T dnu_b = R_T^(2m)(0)/(2m)! + int r_(2m+2)(alpha)dnu_b(alpha)`.

Taylor's remainder gives

`|r_(2m+2)(alpha)|`
` <= |alpha|^(2m+2) sup_(|x|<=b)|R_T^(2m+2)(x)|/(2m+2)!`.

Since `|alpha|<=b`,

`int |alpha|^(2m+2)d|nu_b|(alpha)`
` <= b^(2m+2)||nu_b||_TV`
` = E_m^(-1)b^2`.

This proves the claimed remainder bound.

An entirely physical-space sufficient bound follows from the same Fourier formula:

`sup_(|alpha|<=b)|R_T^(2m+2)(alpha)|`
` <= log(T)^(2m+2) int |u|^(2m+2)|D_T(u)|du`.

Thus the Taylor truncation is quantitatively controlled once the next absolute physical moment is controlled. In particular, choosing a shrinking `b` is useful only if this source-side moment growth does not erase the nominal `b^2` gain.

## 4. Composition with Rodgers' theorem gives the complete fixed-margin calibration gate

`VIS-260` already propagates Rodgers' uniform theorem error through the same optimally conditioned packet:

`|int [P_T(alpha)-BK_T(alpha)]dnu_b(alpha)|`
` <= C T^(-delta)E_m^(-1)b^(-2m)`.

Subtracting the matched GUE prediction and inserting the present Taylor reduction gives, schematically but with each error term separately controlled,

`int [P_T-GUE_T]dnu_b`
` = A_(2m)(T) + TaylorRem + RodgersRem`.

Therefore a rigorous positive fixed-margin carrier requires

`|A_(2m)(T)|`
` >> E_m^(-1)b^2 sup|R_T^(2m+2)|`

and

`|A_(2m)(T)|`
` >> T^(-delta)E_m^(-1)b^(-2m)`.

The factorial constants above may of course be retained when comparing exact scales. This criterion separates three logically distinct questions that had previously been mixed together: whether the arithmetic prediction has a nonzero carrier, whether the low-frequency packet isolates it accurately, and whether the theorem transfers the actual zeta statistic to that prediction accurately enough.

For a power-law packet `b=T^(-beta)`, `VIS-260` gives the necessary certified theorem-transfer range `beta<epsilon/(4m)` for fixed margin `epsilon`. The present result adds the independent Taylor-resolution gate. Neither gate addresses the moving-edge or four-level covariance obstruction.

## 5. Prior art and novelty boundary

Rodgers' Theorem 1.4 and the formulas immediately surrounding it are the external source for the prediction being transformed:

Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, DOI `10.1093/qmath/has024`, arXiv `1203.3275`.

The identity between derivatives of a Fourier transform at the origin and weighted moments of its source is standard Fourier calculus, as is Taylor remainder control. No novelty is claimed for either fact. The substantive Mathia contribution here is only their exact composition with the already-persisted support-edge representation and the sharp packet capacity of `VIS-259`, yielding a source-carrier test in the same normalization used by `VIS-260`.

This finding does not claim that the Bogomolny--Keating-minus-GUE moment hierarchy is new, nor that its first nonzero member has not been computed elsewhere. Candidate-specific novelty is deliberately not asserted: the next step must first derive the relevant `M_(2j)(T)` from the explicit `Q_t-K_t` kernel and then audit any resulting asymptotic against the analytic-number-theory literature.

## 6. Boundaries and falsification

The reduction is fixed-margin and two-level because its rigorous transfer input is `VIS-260`. It does not supply the moving-support uniformity excluded there, and it does not repair the four-level covariance requirement of `VIS-139`--`VIS-141`.

The packet must be normalized and cancelled before looking at confirmation data. Changing `m`, `b`, `omega`, or the matched null after seeing a favorable residual would invalidate the pre-registration logic of the accepted support-edge clue.

A nonzero formal derivative is not enough. Kill a candidate order if the corresponding `M_(2m)(T)` vanishes, is wholly explained by the matched null/calibration, or is asymptotically no larger than either the Taylor remainder or the propagated Rodgers error. If the first few moments vanish, do not climb to higher `m` merely because `VIS-259` guarantees a packet: the higher source carrier must be independently motivated and derived first.

No untouched confirmation-zero data are used.

## Research consequence

The next source-side calculation is now sharply specified. Start with the quadratic branch `m=1` and compute

`M_2(T)=int u^2 D_T(u)du`

from Rodgers' explicit `Q_t-K_t` kernel for one fixed predeclared even weight `omega`. If that moment gives a nonzero asymptotic coefficient that beats both the `VIS-261` Taylor remainder and the `VIS-260` theorem-transfer term for an admissible `b=T^(-beta)`, the restricted-support branch has its first rigorously calibrated arithmetic carrier.

If `M_2(T)` vanishes or is too small, the quartic branch is admissible only after computing `M_4(T)` independently and checking the corresponding `m=2` gates. Do not optimize higher packet orders before the source moments justify them.