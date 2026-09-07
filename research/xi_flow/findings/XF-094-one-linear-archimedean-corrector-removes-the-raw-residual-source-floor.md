# XF-094 — one linear archimedean corrector removes the raw residual source floor

**Status:** `EXACT-DERIVED` + `SOURCE-TO-GRID` + `DETERMINISTIC-FLOOR` + `REFERENCE-REFINEMENT`. XF-092 closes the deterministic quadrature problem for the full Polymath reference, while XF-093 shows that fixed-strip quotient accuracy alone does not justify point-sampling the remaining Xi/Polymath residual on the Volterra mesh. There is an independent issue before mesh-scale anti-concentration is even relevant: the **exact** endpoint residual left by the Polymath reference is not small in the guarded source norm.

At `t=0`, throughout the exact prime-free band `0<xi<lambda_2=(log 2)/2`, XF-052 and XF-092 give

\[
\mathcal Z_0(\xi)
=e^\xi+e^{-\xi}-\frac{e^{-\xi}}{1-e^{-4\xi}},
\qquad
\mathcal Z_0^M(\xi)
=-\frac{e^{-\xi}}{4\xi}+\frac12e^{-\xi}+e^\xi.
\]

Hence the raw quotient residual is explicitly

\[
\boxed{
\mathcal R_0(\xi)
:=\mathcal Z_0(\xi)-\mathcal Z_0^M(\xi)
=e^{-\xi}\left(\frac1{4\xi}-\frac12\coth(2\xi)\right).
}
\tag{1}
\]

Its endpoint expansion begins

\[
\boxed{
\mathcal R_0(\xi)
=-\frac{\xi}{3}+\frac{\xi^2}{3}-\frac{7\xi^3}{90}+O(\xi^4).
}
\tag{2}
\]

That linear term is already large enough to produce an order-one XF-086 resource on the interior live block `q<=m<=2q`. With `M=q^2`, `xi_m=m Delta`, `Delta\asymp q^{-3/2}`, and

\[
I_m=\int_{-1}^{1}(\pi m+u)^4|\chi(u)|^2\,du,
\qquad
C_g=\int_{-1}^{1}|\chi(u)|^2\,du,
\]

one has uniformly on that block

\[
\mathcal R_0(\xi_m)
=-\frac{m\Delta}{3}(1+o(1)),
\qquad
I_m=\pi^4C_gm^4(1+o(1)).
\]

Therefore

\[
\boxed{
\mathcal R_{[q,2q]}\bigl((\mathcal R_0(\xi_m))_m\bigr)
=
\frac{127\pi^4C_g}{252}\,q^3\Delta^2(1+o(1))
=\Theta_g(1).
}
\tag{3}
\]

Thus a bridge that simply takes the raw Polymath-subtracted values `Q_m=mathcal R_0(xi_m)` cannot produce the `o(1)` guarded source state required by XF-071. This remains true even with **perfect** sampling, so it is logically distinct from the narrow-spike obstruction in XF-093. It does not reopen XF-085--XF-086: an order-one resource is still `o(J^3)` for `J=q^{1/4}` and is therefore easily equal-weight realizable. The failure is downstream smallness, not static real-divisor existence.

The repair is unexpectedly small. Define the deterministic linear corrector

\[
C(\xi):=-\frac{\xi}{3}
\tag{4}
\]

on a fixed neighborhood of zero, with an arbitrary fixed smooth cutoff below `lambda_2` if a global half-line object is desired, and absorb it into the reference:

\[
\mathcal Z_0^{M,+}:=\mathcal Z_0^M+C.
\]

Then

\[
\boxed{
\mathcal R_0^+(\xi)
:=\mathcal Z_0(\xi)-\mathcal Z_0^{M,+}(\xi)
=\frac{\xi^2}{3}+O(\xi^3).
}
\tag{5}
\]

On the full canonical source band `J<=m<=K`, where `J=q^{1/4}` and `K\asymp q\log\log T`, one has `K Delta ->0`, so `(5)` gives

\[
\boxed{
\mathcal R_{[J,K]}\bigl((\mathcal R_0^+(\xi_m))_m\bigr)
\ll_g
\frac{\Delta^4K^9}{M^2}
=O_g\!\left(q^{-1}(\log\log T)^9\right)
=o(1).
}
\tag{6}
\]

Thus the first regular endpoint coefficient, and no new singular renormalization, is enough to restore the source-size scale required by the guarded periodic transport.

## 1. Exact subtraction below the first prime frequency

XF-052 gives on `0<xi<lambda_2`

\[
B(\xi)
=e^\xi+e^{-\xi}-\frac{e^{-\xi}}{1-e^{-4\xi}}.
\tag{7}
\]

XF-092 gives the exact `t=0` Polymath carrier

\[
\mathcal Z_0^M(\xi)
=-\frac{e^{-\xi}}{4\xi}+\frac12e^{-\xi}+e^\xi.
\tag{8}
\]

Subtracting `(8)` from `(7)` yields

\[
\mathcal R_0(\xi)
=e^{-\xi}
\left[
\frac12+\frac1{4\xi}-\frac1{1-e^{-4\xi}}
\right].
\tag{9}
\]

Using

\[
\frac1{1-e^{-4\xi}}
=\frac12+\frac12\coth(2\xi)
\tag{10}
\]

proves `(1)`. The Bernoulli expansion

\[
\coth(2\xi)
=\frac1{2\xi}+\frac{2\xi}{3}-\frac{8\xi^3}{45}+O(\xi^5)
\tag{11}
\]

followed by multiplication by `e^{-xi}` gives `(2)`.

Two cancellations are worth recording. The pole `-1/(4xi)` agrees exactly, as already used in XF-088--XF-092, but the constant term agrees as well: both the exact prime-free background and the Polymath reference have endpoint constant `7/4`. The first mismatch is therefore the deterministic linear coefficient

\[
\boxed{
\frac1{24}-\frac38=-\frac13.
}
\tag{12}
\]

No prime data enter this calculation; the whole live band lies below `lambda_2` for sufficiently large `T` because `K Delta=O((log log T)/(log T))`.

## 2. The linear mismatch has a nonvanishing guarded norm

Let

\[
S_q:=\{m\in\mathbb Z:q\le m\le2q\}.
\tag{13}
\]

For the canonical cutoff `K\asymp q log log T`, one has `S_q subset [J,K]` eventually. Since `m Delta=O(q^{-1/2})` uniformly on `S_q`, equation `(2)` gives

\[
|\mathcal R_0(\xi_m)|^2
=\frac{m^2\Delta^2}{9}(1+o(1)).
\tag{14}
\]

The exact sideband weight satisfies

\[
I_m
=\pi^4C_gm^4(1+O(m^{-1})).
\tag{15}
\]

Using the XF-086 resource definition and `M=q^2`,

\[
\begin{aligned}
\mathcal R_{S_q}(\mathcal R_0)
&=
\frac1{4q^4}
\sum_{m=q}^{2q}
I_m|\mathcal R_0(\xi_m)|^2\\
&=
\frac{\pi^4C_g\Delta^2}{36q^4}
\sum_{m=q}^{2q}m^6(1+o(1)).
\end{aligned}
\tag{16}
\]

Since

\[
\sum_{m=q}^{2q}m^6
=\frac{127}{7}q^7(1+o(1)),
\tag{17}
\]

we obtain `(3)`. In particular, the conclusion needs no exact limiting constant for `q^{3/2}Delta`; the existing two-sided scaling `Delta\asymp q^{-3/2}` already gives a fixed positive lower bound.

A translated-center phase cannot remove this floor. Multiplying `Q_m` by `e^{-i xi_m r}` leaves the XF-086 resource unchanged. Nor can equal-weight realization remove it: XF-085 realizes the prescribed moments exactly, so any real periodic carrier built from the raw samples inherits the same order-one source resource.

This pinpoints the logical mismatch with the desired XF-071 input. XF-060 supplies an `o(1)` derivative-weighted Xi source statistic, whereas the raw Polymath-subtracted continuum samples have a deterministic `Theta(1)` block before any sampling error is considered. Consequently an `o(1)` source interface cannot identify those raw samples directly with the periodic power sums.

## 3. One endpoint coefficient restores `o(1)` source resource

Choose a fixed `xi_0<lambda_2` and a smooth cutoff `kappa` with `kappa=1` on `[0,xi_0]` and support below `lambda_2`. Put

\[
C(\xi)=-\frac13\xi\,\kappa(\xi).
\tag{18}
\]

Because `K Delta ->0`, every live mesh point eventually lies in the region where `kappa=1`. Equation `(2)` then gives the uniform bound

\[
|\mathcal R_0^+(\xi_m)|\ll \xi_m^2,
\qquad J\le m\le K.
\tag{19}
\]

Also `I_m\ll_g m^4`, so

\[
\begin{aligned}
\mathcal R_{[J,K]}(\mathcal R_0^+)
&\ll_g
\frac1{M^2}
\sum_{m=J}^{K}
m^4(m\Delta)^4\\
&\ll_g
\frac{\Delta^4K^9}{M^2}.
\end{aligned}
\tag{20}
\]

At `M=q^2`, `Delta\asymp q^{-3/2}`, `K\asymp q log log T`, this is exactly `(6)`. Since `q\asymp log^2 T`, any fixed power of `log log T` is `o(q)`, and the corrected source resource vanishes.

The exponent is also a useful calibration. Merely improving the residual from `O(xi)` to `O(xi^{1+epsilon})` would already gain a positive power of `q`; the exact cancellation to `O(xi^2)` leaves ample room across the whole `K\asymp q log log T` band.

One may of course absorb the **entire** explicit function `(1)` into a prime-free endpoint reference and make the `t=0` residual vanish identically below `lambda_2`. The point of `(18)` is sharper: the full correction is unnecessary for source-size purposes. Its first nonzero endpoint coefficient alone crosses the `o(1)` threshold.

## 4. The corrector creates no new endpoint counterterm

The linear correction does not disturb the singular renormalization already fixed by XF-088--XF-092. In the notation of XF-092's generic finite-part lemma, the reference has the form

\[
F(\xi)=-\frac c\xi+d\log\xi+b(\xi).
\tag{21}
\]

Replacing `b` by `b+C` preserves all hypotheses

\[
|(b+C)'(\xi)|\ll1+|\log\xi|,
\qquad
|(b+C)''(\xi)|\ll\xi^{-1},
\tag{22}
\]

and leaves the pole coefficient `c=1/4` and logarithmic coefficient `d=-t/8` untouched. Therefore the same frozen counterterm

\[
\boxed{
\frac14\log\Delta\,\delta_0
}
\tag{23}
\]

renormalizes the corrected reference. The generic XF-092 quadrature estimate remains

\[
|E^{M,+}_{t,m}-E^S_{t,m}|
\ll
\Delta(1+\xi_mL_\Delta^2),
\tag{24}
\]

up to a changed fixed constant, and hence has the same `o(1)` guarded-resource consequence. The repair is therefore not paid for by a second mesh-dependent normalization.

What remains is a **dynamic reference choice**, not a source-size or singular-quadrature problem. A positive-time corrected reference must transport the deterministic linear background, or an equivalent prime-free correction, consistently on continuum and periodic sides. A frozen cutoff corrector merely changes the deterministic forcing and stays within the same finite-part quadrature class; proving the resulting forced residual comparison over the required heat interval is still a separate stability step.

## 5. Relation to XF-093

XF-093 remains valid: an arbitrarily small high-line quotient can hide a narrow Fourier spike aligned with one Volterra node, so fixed-strip accuracy alone cannot control raw nodal samples. The present finding identifies a prior obstruction for the **actual endpoint source**. Even if every sample were known exactly and no spectral spike existed, the vector `(mathcal R_0(xi_m))` would still have the nonzero floor `(3)`.

Accordingly, the sufficient target proposed at the end of XF-093 — an `o(1)` cell-Sobolev bound for the raw Polymath-subtracted residual — cannot hold on the canonical live band at `t=0`. The correct target is the **deterministically corrected residual**, for example `(5)`, or a source-faithful reference that contains the same linear endpoint coefficient. Mesh-scale anti-concentration should be proved only after this deterministic floor has been quotiented.

This distinction matters because the two repairs address different failure modes. The linear corrector removes a broad, completely explicit endpoint profile. A sampling theorem prevents narrow spectral concentration. Neither substitutes for the other.

## 6. Stress tests and falsification boundary

**Prime-free scope.** The exact formula `(1)` uses XF-052 and is asserted only below `lambda_2`. That is enough because `K Delta ->0`. No claim is made that the Polymath residual has the same elementary formula across the prime-power atoms.

**No static obstruction.** Equation `(3)` is intentionally not presented as a failure of XF-085--XF-086. Since `Theta(1)=o(J^3)`, the raw residual moments remain deep inside the equal-weight realization cone. The obstruction is precisely that XF-071 needs `o(1)` normalized guarded energy for the source-to-destination smallness argument.

**No new singularity.** The corrector is `O(xi)` and can be compactly supported. It cannot change the pole residue, the positive-time logarithmic cusp, or the frozen endpoint delta. Any derivation that introduces a new `log Delta` term solely from `(18)` is inconsistent with the generic XF-092 finite-part lemma.

**Scale check.** On `m\asymp q`, the exact weights are order one while `mathcal R_0(xi_m)\asymp q^{-1/2}`. There are `Theta(q)` such modes, producing the order-one total in `(3)`. After linear correction the samples become `O(q^{-1})`; the same block then contributes `O(q^{-1})`, consistent with `(6)`.

**Not a transition theorem.** Removing the deterministic source floor does not show that a positive `Lambda` transition creates guarded destination mass. That independent coercivity gate remains unchanged.

## 7. Prior-art boundary and consequence for `xi_flow`

The external ingredients behind the two carriers are already anchored in the line: the classical explicit formula/Euler-product decomposition used by XF-052 and the Polymath15 reference used by XF-089--XF-092. A targeted search around the Polymath reference, the Fourier explicit formula, and de Bruijn--Newman logarithmic-derivative transport found the expected source literature but no statement of the Mathia-specific guarded resource calculation `(3)` or the one-coefficient repair `(6)`. No new external theorem is load-bearing, so `SOURCES.md` does not change.

The live source bridge is now more precise. The full Polymath reference is sufficiently accurate for singular quadrature, but it is **not normalized finely enough to be the small-source reference for the guarded Vieta state**. Its residual contains a deterministic linear archimedean mode whose aggregate resource is macroscopic. Absorbing `-xi/3` into the reference removes that floor with no new counterterm and leaves an `o(1)` endpoint source state. Only after this correction should the XF-093 mesh-scale sampling gate be attacked.

The remaining sequence is therefore: transport a deterministic corrected reference through the continuum/grid comparison; establish mesh-scale control for the corrected Xi-specific residual rather than the raw Polymath residual; realize the resulting finite moments by XF-085--XF-086; use XF-087/XF-071 for the guarded periodic evolution; and separately prove the positive-transition destination lower bound. The new result removes a hidden normalization mismatch in the first of those steps without changing the later gates.