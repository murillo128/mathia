# WI-269 — first-crossing null modes induce a PSD signed-source Laplacian

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-GROUND-STATE-ALGEBRA + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** an exact source-specific necessary condition on any hypothetical first **unrestricted** Suzuki zero mode. It does not prove RH and does not yet force a nonzero prime-lag autocorrelation. Its gain is to replace the cancellation-prone scalar autocorrelation constraints of `WI-253`/`WI-258` by a whole positive-semidefinite family of localized source couplings, with an exact nodal compensation law.
- **Novelty boundary:** the multiplier/ground-state transform algebra is classical, as are finite signed-Laplacian and effective-resistance criteria. Suzuki supplies the localized Weil form and `WI-253` supplies the arbitrary-multiplier source normalization. The Mathia deduction is the exact collapse of that transform to the zeta source `prime atoms + w(h)dh`, its finite PSD signed-Laplacian compressions, and the resulting uncancelled opposite-sign overlap inequality. No priority claim is made.

## Claim

Assume RH is false and let

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\}
\]

be the first global crossing of Suzuki's unrestricted localized Weil ground-state energy, as in `WI-238` and `WI-253`. Choose a normalized real zero mode

\[
\|v\|_2=1,\qquad A_av=0,
\qquad q_a\ge0.
\tag{1}
\]

Extend `v` by zero outside `(-a,a)`. For `h>0` put

\[
\kappa(h)=\frac{e^{-5h/2}}{1-e^{-2h}},
\qquad
w(h)=\kappa(h)-e^{h/2},
\tag{2}
\]

and for a bounded real Lipschitz multiplier `\chi` define

\[
D_\chi(v;h)
:=\int_{\mathbb R}
(\chi(x+h)-\chi(x))^2v(x+h)v(x)\,dx.
\tag{3}
\]

Then every such multiplier satisfies the exact identity

\[
\boxed{
q_a(\chi v)
=
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
D_\chi(v;\log n)
+
\int_0^{2a}w(h)D_\chi(v;h)\,dh
\ge0.
}
\tag{4}
\]

Thus the same signed arithmetic/archimedean source that appears only after center averaging in the scalar flux of `WI-253` is already a **positive-semidefinite multiplier form** before any averaging.

Polarize the right side of (4):

\[
\begin{aligned}
\mathcal B_v(\chi,\psi)
:={}&
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\int (\Delta_{\log n}\chi)(x)(\Delta_{\log n}\psi)(x)
 v(x+\log n)v(x)\,dx\\
&+\int_0^{2a}w(h)
\int (\Delta_h\chi)(x)(\Delta_h\psi)(x)
 v(x+h)v(x)\,dx\,dh,
\end{aligned}
\tag{5}
\]

where `\Delta_h\chi(x)=\chi(x+h)-\chi(x)`. Then

\[
\boxed{\mathcal B_v(\chi,\chi)=q_a(\chi v)\ge0.}
\tag{6}
\]

For any finite real multiplier family `\chi_1,\ldots,\chi_m`, the matrix

\[
L_{ij}:=\mathcal B_v(\chi_i,\chi_j)
\tag{7}
\]

is positive semidefinite. If the multipliers form a partition of unity,

\[
\sum_{j=1}^m\chi_j=1,
\tag{8}
\]

then

\[
\boxed{L\succeq0,\qquad L\mathbf1=0.}
\tag{9}
\]

Hence every finite multiplier partition of a hypothetical first null mode produces a PSD **signed Laplacian compression** of the exact Suzuki source. The entries need not have the Markov sign pattern; `WI-268` proves that ordinary positivity-preserving-semigroup structure is unavailable. What survives is the stronger source-conditioned PSD constraint (9).

There is also an exact nodal consequence. Write

\[
v=v_+-v_-,\qquad v_+,v_-\ge0,
\]

and define the uncancelled opposite-sign overlap

\[
A_-(h)
:=\int_{\{x:v(x+h)v(x)<0\}}
|v(x+h)v(x)|\,dx.
\tag{10}
\]

Then `v_+` and `v_-` lie in the form domain and

\[
\boxed{
q_a(v_+)=q_a(v_-)
=-\left[
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}A_-(\log n)
+
\int_0^{2a}w(h)A_-(h)\,dh
\right]
\ge0.
}
\tag{11}
\]

Let `h_0=\log\rho`, where `\rho^3-\rho-1=0`, so by `WI-268`

\[
w(h)>0\quad(0<h<h_0),
\qquad
w(h)<0\quad(h>h_0).
\tag{12}
\]

Equation (11) therefore gives the source-specific nodal tariff

\[
\boxed{
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}A_-(\log n)
+
\int_0^{h_0}w(h)A_-(h)\,dh
\le
\int_{h_0}^{2a}|w(h)|A_-(h)\,dh.
}
\tag{13}
\]

Every opposite-sign overlap at an active prime-power lag, and every short-range opposite-sign overlap before the archimedean sign change, must therefore be financed by long-range archimedean opposite-sign overlap. Unlike `C_v(h)`, the quantity `A_-(h)` cannot vanish through cancellation between positive and negative overlap regions.

## 1. Exact derivation from the arbitrary-multiplier identity

`WI-253`, equation (14), proves for the unrestricted first crossing that every bounded real Lipschitz multiplier preserving the form domain satisfies

\[
q_a(\chi v)
=\mathcal E_{\chi,\mathrm{mean}}(v)
+
\int_0^{2a}D_\chi(v;h)\,d\nu_a(h),
\tag{14}
\]

where

\[
d\nu_a(h)
=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dh)
-e^{h/2}\,dh
\tag{15}
\]

and

\[
\mathcal E_{\chi,\mathrm{mean}}(v)
=\frac12\sum_{m\ge1}\frac1{b_m}
\iint K_{\alpha_m}(x-y)
(\chi(x)-\chi(y))^2v(x)v(y)\,dx\,dy.
\tag{16}
\]

Here `b_m=m+1/4`, `\alpha_m=2b_m`, and

\[
K_\alpha(h)=\frac\alpha2e^{-\alpha|h|}.
\]

Because the kernels are even, splitting the double integral into the two orientations gives

\[
\mathcal E_{\chi,\mathrm{mean}}(v)
=
\int_0^{2a}
\left[
\sum_{m\ge1}\frac1{b_m}K_{\alpha_m}(h)
\right]D_\chi(v;h)\,dh.
\tag{17}
\]

But

\[
\frac1{b_m}K_{\alpha_m}(h)
=e^{-2b_mh},
\]

so the bracket is exactly

\[
\sum_{m\ge1}e^{-2(m+1/4)h}
=\kappa(h).
\tag{18}
\]

Combining (14)--(18) gives (4) with no estimate. The nonnegativity is simply firstness: at the first global crossing the bottom eigenvalue is zero, so `q_a\ge0`.

This is also the direct nonlocal ground-state-transform algebra. Since `A_av=0`, the weak equation gives

\[
q_a(v,\chi^2v)=0,
\]

and therefore

\[
q_a(\chi v)
=q_a(\chi v)-q_a(v,\chi^2v).
\tag{19}
\]

All multiplication/local potential terms cancel in (19); only squared multiplier differences survive. The unusual feature here is that their edge measure is signed because both `w(h)` and `v(x+h)v(x)` may change sign.

## 2. Finite partitions give PSD signed Laplacians

Polarization of (4) gives (5), and (6) implies positive semidefiniteness of every finite matrix (7). If (8) holds, then `\Delta_h1=0`, hence

\[
\sum_jL_{ij}
=\mathcal B_v(\chi_i,1)=0.
\]

This proves (9).

The statement is stronger than a single autocorrelation inequality but weaker than a Markov/Dirichlet-form theorem. An individual infinitesimal edge in (5) carries signed weight

\[
\left[
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dh)
+w(h)dh
\right]v(x+h)v(x).
\tag{20}
\]

PSD is recovered only after the exact source is integrated against all edge differences generated by the same null mode. This is precisely why `WI-268` does not contradict the result: `WI-268` rules out an unconditional Markov sign pattern for the original form, whereas (9) uses the null equation itself and imposes positivity only on the transformed multiplier family.

This finite compression creates a concrete next interface. Classical signed-graph results characterize when negative Laplacian edges can be absorbed by a positive network in terms of effective resistance or equivalent Schur complements. Those theorems cannot be inserted blindly here—the continuum source, multiplier discretization, and sign of `v(x+h)v(x)` must be preserved—but they provide a precise finite-dimensional language for testing whether the long-range negative part of (20) can be screened without genuine prime overlap.

## 3. Nodal truncation removes autocorrelation cancellation

The form-domain point in (11) is legitimate. At fixed `a`, the prime/density source perturbation is `L^2`-bounded, so the full localized form has the same form domain as the positive mean form used in `WI-251`/`WI-253`. Each mean-form jump term has kernel representation

\[
\iint K(x-y)|u(x)-u(y)|^2dxdy,
\]

and the normal contraction `u\mapsto u_+` satisfies

\[
|u_+(x)-u_+(y)|\le|u(x)-u(y)|.
\]

Thus `v_+,v_-` belong to the form domain even though no `H^1` regularity or pointwise endpoint values are assumed.

The weak null equation gives

\[
q_a(v,v_+)=q_a(v,v_-)=0.
\tag{21}
\]

Since `v=v_+-v_-`, (21) implies

\[
q_a(v_+)=q_a(v_-)=q_a(v_+,v_-).
\tag{22}
\]

The two parts are nonnegative and have disjoint pointwise support. Polarizing Suzuki's source decomposition, their cross form is

\[
q_a(v_+,v_-)
=-\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\left[
\int v_+(x+\log n)v_-(x)dx
+
\int v_-(x+\log n)v_+(x)dx
\right]
\]

\[
\hspace{28mm}
-\int_0^{2a}w(h)
\left[
\int v_+(x+h)v_-(x)dx
+
\int v_-(x+h)v_+(x)dx
\right]dh.
\tag{23}
\]

The bracket at lag `h` is exactly `A_-(h)`, which proves (11). Since `q_a\ge0`, splitting the continuous term at the unique sign change `h_0` proves (13).

There is a strict firstness refinement whenever one nodal part fits in a proper translated subwindow. If, for example, `v_+` is supported in an interval of radius `r<a`, translation invariance and zero extension give

\[
q_a(v_+)\ge\lambda_r\|v_+\|_2^2>0.
\]

Then (13) strengthens to

\[
\boxed{
\int_{h_0}^{2a}|w(h)|A_-(h)dh
-
\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}A_-(\log n)
-
\int_0^{h_0}w(h)A_-(h)dh
\ge\lambda_r\|v_+\|_2^2.
}
\tag{24}
\]

The analogous statement holds for `v_-`. No strict version is asserted when both nodal parts span the full aperture.

## 4. Relation to the current activity-to-overlap gate

`WI-263`--`WI-265` show that scalar autocorrelation constraints can be screened: positive and negative spatial overlap can cancel inside `C_v(\log n)`. `WI-266` and `WI-267` restore the exact Suzuki equation and prove that simple endpoint screening fails and that every support gap is reached by an active prime translation. They still do not turn translated activity into nonzero autocorrelation.

Equations (4), (9), and (13) expose a stronger intermediate object. Instead of asking immediately for the signed scalar `C_v(\log n)`, one may localize the same null mode by a partition of unity and retain a PSD matrix of source couplings. For a sign-changing mode, the nodal cut already yields a cancellation-free quantity `A_-(\log n)` and an exact tariff against long-range archimedean overlap. For a one-signed mode, (9) remains nontrivial because the edge sign is then exactly the sign of the source itself, so long-range negative archimedean edges must be supported by the short-range/prime positive network.

This does **not** finish the accepted clue. The right side of (13) may be large enough to screen every active prime overlap, and a one-signed null mode makes the nodal inequality trivial. Also, support activity from `WI-267` still does not imply overlap: `v(x)=0` and `v(x+\ell)\ne0` contributes to the pointwise null equation but not to the edge product in (20). The remaining quantitative problem is to show that some finite multiplier compression has a negative effective-resistance/Schur-complement obstruction unless a definite amount of arithmetic overlap is present, or to construct a genuine source-compatible null geometry whose signed Laplacian remains PSD while screening all prime-lag autocorrelations.

## 5. Prior-art and novelty audit

The load-bearing zeta input is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), especially the localized closed form and explicit Weil/source decomposition. `WI-253` already audited the unrestricted density subtraction and arbitrary-multiplier IMS identity against that source. No new claim about Suzuki's operator is made here.

The algebraic ancestor of (19) is the classical ground-state representation/Doob-transform mechanism. A directly relevant nonlocal reference is Rupert L. Frank and Robert Seiringer, **Non-linear ground state representations and sharp Hardy inequalities**, *Journal of Functional Analysis* 255 (2008), 3407--3430, DOI `10.1016/j.jfa.2008.05.015`, arXiv:0803.0503. Their theory establishes nonlocal ground-state representations in positive-kernel settings. The present zeta specialization differs in the load-bearing point that the transformed edge weight (20) is signed.

For the finite compression (9), classical signed-Laplacian prior art includes Daniel Zelazo and Mathias Bürger, **On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance**, arXiv:1408.2187, and Wei Chen et al., **Characterizing the positive semidefiniteness of signed Laplacians via Effective Resistances**, 2016 IEEE CDC, DOI `10.1109/CDC.2016.7798396`. These works supply neighboring finite-dimensional criteria; they do not state the zeta-specific transform (4), the nodal tariff (13), or a continuum-to-finite discretization theorem sufficient for RH.

A targeted search around Suzuki's localized Weil operator, nonlocal ground-state representations, signed Laplacians, effective resistance, and zeta null modes found the classical ingredients above but no statement of (4), (9), or (13) for the localized Weil source. Search absence is audit context only and is not treated as a priority claim.

## 6. Stress tests and failure modes

1. **Factor check.** In `WI-253` the mean IMS term has a prefactor `1/2`; splitting the even double integral into positive and negative lags contributes the compensating factor `2`. Therefore its one-sided kernel is exactly `kappa(h)`, not `kappa(h)/2` or `2kappa(h)`.
2. **Prime sign.** Suzuki's prime translations enter the quadratic form with negative cross coefficient. In the ground-state difference (19) this becomes the positive atomic coefficient in (4); for opposite nodal signs the cross form reverses it again, giving the negative prime term in (23).
3. **Archimedean sign.** The continuous transformed weight is `w=kappa-e^{h/2}`. `WI-268` independently checks its unique sign change and the equivalent original-form cross kernel `-w`.
4. **No hidden smoothness of the zero mode.** Multiplication in (4) uses bounded Lipschitz multipliers on the closed form domain as already justified in `WI-253`. The positive/negative-part statement uses normal contraction of the positive mean-form domain plus boundedness of the finite-radius source perturbation; it does not assume `v in H_0^1`.
5. **First crossing is essential.** The identity before the final inequality follows from the null equation, but PSD of `mathcal B_v` uses `q_a>=0`. A zero eigenvector at a later crossing need not produce a PSD signed Laplacian.
6. **No ordinary Markov inference.** PSD of the transformed multiplier form does not restore positivity preservation of the original semigroup. Individual transformed edge weights can be negative, consistently with `WI-268`.
7. **Nodal law may be vacuous.** If `v` is one-signed then `A_-=0`. If `v` changes sign only at long separations, (13) can also be weak. The finding is a structural constraint, not an overlap lower bound.
8. **Effective resistance is a next test, not an imported theorem.** A finite partition may approximate or compress the continuum source, but no error-free discretization or resistance contradiction is asserted here.

## Falsification and audit test

The finding is exact. A refutation must identify a failure in at least one of the following load-bearing steps: the unrestricted arbitrary-multiplier identity of `WI-253`; the even-kernel collapse (17)--(18); the first-crossing implication `q_a>=0`; the form-domain stability under positive/negative parts; the cross-form sign/factor in (23); or the sign change of `w` proved independently in `WI-268`.

A direct finite-dimensional sanity check is useful: if a PSD quadratic form has a null vector `v` and one writes `v=v_+-v_-`, then `q(v_+)=q(v_-)=q(v_+,v_-)>=0`. Equation (23) is exactly the Suzuki-source evaluation of this elementary identity.

## Research consequence

The accepted first-crossing program now has a source-specific object between support propagation and scalar autocorrelation: the PSD signed-source Laplacian (9). The next high-value test is to choose finite multiplier partitions adapted to support/nodal components and ask whether the negative long-range archimedean edges can satisfy the signed-Laplacian PSD/effective-resistance conditions while all prime-lag overlaps remain screened. A positive obstruction would turn `WI-267` activity into quantitative overlap; a source-compatible PSD screening construction would decisively close this route.
