# PF-295 — canonical seam ratios close the fixed-axis parameter escape

**Status:** `EXACT-DERIVED + CANONICAL-SCALE-CLOSURE + UNIFORM-FRACTIONAL-REGULARITY + NEGATIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-294-fixed-axis-robin-source-is-uniformly-half-sobolev-for-bounded-seam-ratio|PF-294]] leaves one explicit parameter loophole: its uniform `H^{1/2}` estimate for a fixed normalized Robin source row assumes that the seam-to-corridor ratio `r=w/s` stays bounded. For an abstract family that is a real limitation. For the **canonical PF-205/PF-230 prime-flute geometry**, however, the limitation is automatically satisfied.

PF-205 fixes the signed Fermi-area seam halfwidths `w_j=\kappa d_j`, while PF-230 uses the actual neighboring-cuff distance `s_n` and the corresponding normal offsets `\rho_j=\operatorname{arsinh}w_j`. Its exact geometric calibration proves

\[
\frac{\rho_n+\rho_{n+1}}{s_n}\le \kappa+o(1)<1
\]

for fixed sufficiently small `\kappa<1/4`. Since `w_j=\sinh\rho_j=\rho_j(1+o(1))`, both canonical ratios `w_n/s_n` and `w_{n+1}/s_n` are therefore uniformly bounded on the tail. Through the PF-234/PF-235/PF-258 dictionary these are exactly the `r=w/s` parameters entering PF-294's fixed-axis Robin source.

Consequently, for every fixed source row, **the canonical pant tail has a uniform physical-axis `H^{1/2}` bound for the normalized fixed-axis source**. The unbounded-`w/s` escape listed after PF-294 is not available to the actual PF-205 trimmed geometry. Together with PF-255/PF-256, this also rules out the already-controlled hypercycle/density/corridor transports as the place where that fixed source suddenly loses every positive Sobolev margin.

This still does not identify PF-290's complete mixed Riesz representative with one fixed-axis source column. The live roughness mechanisms are now genuinely downstream: mixed/global Schur reassembly of the kind warned about by PF-279, neighboring-cell coupling, source-row proliferation or nonuniform superposition, support migration/end completion, or another normalization effect not contained in the canonical fixed-axis factor.

## Claim

Use the canonical PF-205 seam widths

\[
w_j=\kappa d_j,
\qquad
\rho_j:=\operatorname{arsinh}w_j,
\tag{1}
\]

with the same fixed sufficiently small `\kappa<1/4` as in PF-230. Let `s_n` be the common-perpendicular distance between the two finite cuff axes of the `n`th one-cusp pant, so PF-230 gives

\[
s_n=\frac{h_n+h_{n+1}}2
\tag{2}
\]

and, after a finite head,

\[
\boxed{
\frac{\rho_n+\rho_{n+1}}{s_n}
\le \kappa+o(1)<1.
}
\tag{3}
\]

Then:

1. the signed Fermi-area seam ratios satisfy
   \[
   \boxed{
   \frac{w_n+w_{n+1}}{s_n}
   \le \kappa+o(1),
   }
   \tag{4}
   \]
   and hence there are `N<\infty` and `r_*<\infty` such that
   \[
   \boxed{
   \max\left\{\frac{w_n}{s_n},\frac{w_{n+1}}{s_n}\right\}
   \le r_*
   \qquad(n\ge N);
   }
   \tag{5}
   \]
2. in the PF-234/PF-235/PF-258 fixed-axis symmetric seam model, the parameter in PF-294 is exactly
   \[
   r_{n,j}=\frac{w_j}{s_n},
   \qquad j\in\{n,n+1\};
   \tag{6}
   \]
3. for every fixed parity/source row `i` and every `0\le\sigma\le1/2`, PF-294 therefore yields
   \[
   \boxed{
   \sup_{n\ge N}\ \max_{j\in\{n,n+1\}}
   \left\|
   U^*y_{s_n,r_{n,j}}^{(i)}
   \right\|_{H^\sigma(\mathbb R_\tau)}
   <\infty,
   }
   \tag{7}
   \]
   where `U` is PF-247's exact complete-axis compactification and `y_{s,r}^{(i)}` is PF-294's normalized fixed-axis Robin source;
4. the canonical PF-205 seam shrinkage cannot therefore be used to realize PF-292's required loss of **every** positive Sobolev bound for this fixed-axis source component. The same remains true after the already-controlled PF-255/PF-256 geometric transports, in the sense recorded in PF-293: those transports preserve positive graph/Sobolev regularity already present with a uniform bound.

The conclusion is asymptotic and fixed-row. It does not assert a uniform bound for arbitrary source-row superpositions or for PF-290's complete mixed response `G_{n,r}`.

## 1. PF-230 already bounds the canonical `w/s` ratio

PF-230 works with the actual trimmed central corridor. The PF-205 artificial boundaries are offset from the two cuff axes by

\[
\rho_j=\operatorname{arsinh}w_j,
\qquad
w_j=\kappa d_j,
\tag{8}
\]

and its equation (8) is precisely (3). Because `d_j\to0`, one has `w_j\to0` and hence `\rho_j\to0`. The elementary expansion

\[
\sinh\rho=\rho+O(\rho^3)
\tag{9}
\]

therefore gives, uniformly for the two adjacent seams,

\[
w_j=\rho_j(1+o(1)).
\tag{10}
\]

Adding the two relations and dividing by `s_n` turns (3) into (4). Positivity then gives (5) immediately. For example, one may choose any fixed `r_*>\kappa` after moving far enough into the tail; the finite head is irrelevant to every PF-290/PF-292 asymptotic obstruction.

There is also a coarser arithmetic reading already visible in PF-228: `w_n\asymp P_n^{-1}` while `s_n\asymp(g_n+g_{n+1})/P_n`, so the ratio is of inverse-gap type rather than a new growing scale. The proof above is preferable because PF-230 gives the required comparison directly in the actual trimmed hyperbolic geometry.

## 2. The ratio is the same one used by the fixed-axis Robin edge

PF-234 identifies the actual PF-205 symmetric seam normalizer with the flat fixed-axis multiplier `M\tanh(wM)` up to a quadratic `1+O(w^2)` form error on the **same signed Fermi-area halfwidth `w`**. PF-235 carries that seam normalizer into the complete-axis compactification. PF-258 then writes the relative fixed-axis edge using the actual corridor scale `s` as

\[
\mathcal R^0_{s,r}
=s^{-1}A^{-1/4}f_{rs}(L)A^{-1/4},
\qquad
w=rs.
\tag{11}
\]

Thus there is no hidden change of scale between PF-230 and PF-294: on the `n`th canonical pant face, `s=s_n`, `w=w_j`, and the abstract PF-294 parameter is exactly (6).

This dictionary is the load-bearing point. Without it, one could not use a geometric bound on the trimmed corridor to close an operator-theoretic parameter loophole. With it, PF-294 applies uniformly along the canonical tail.

## 3. PF-294 becomes a canonical-tail theorem

PF-294 proves, for every fixed row `i` and every finite `r_*`,

\[
\sup_{s>0,\,0<r\le r_*}
\|U^*y_{s,r}^{(i)}\|_{H^\sigma}
<\infty,
\qquad 0\le\sigma\le\frac12.
\tag{12}
\]

Insert (5)--(6) into (12). This gives (7) with no additional estimate and no dependence on the shrinking pant scale `s_n`.

PF-293 already records that the exact PF-255 hypercycle half-density transport and the PF-256 variable-corridor graph equivalence preserve the positive graph regularity of a source family when its source norm is uniformly controlled. Equation (7) supplies precisely that missing uniform control for the canonical fixed-axis component at every fixed row. Therefore the known coordinate/density/corridor changes do not reopen the frequency-escape loophole that PF-294 closed.

For the PF-292 fixed-window test one may spend any strict fraction `0<\sigma<1/2` of this margin, so endpoint trace/restriction conventions at `\sigma=1/2` are not load-bearing. The remaining question is whether the **complete** normalized mixed response introduces a new rough factor after the fixed-axis source has been propagated and reassembled.

## 4. What is actually left for the local heavy-angle obstruction

Before PF-295, the accepted heavy-angle clue still listed an unbounded seam ratio as one possible way to defeat PF-294. That possibility is now closed for the canonical PF-205 trimming. A positive PF-290 shorting deficit can no longer be explained by saying only that the seam shrinks in a parameter regime outside PF-294's theorem.

A surviving local obstruction must instead exhibit a concrete downstream mechanism. The main live candidates are:

- PF-279-type Schur reservoir amplification or another genuinely mixed/global reassembly effect;
- neighboring-cell coupling that creates fine tangential structure absent from one isolated fixed-axis source;
- a source-row population whose relevant indices grow with the pant index, so the fixed-row constants in PF-294 are insufficient;
- support migration or end completion that escapes the PF-291/PF-292 fixed-window model;
- an additional normalization whose parameter growth is not the canonical `w_j/s_n` ratio.

These are mathematically different failure modes. None is supplied merely by the PF-205 seam scale.

## Prior art and novelty audit

No new general theorem in hyperbolic geometry or Sobolev theory is claimed. The pair-of-pants/right-angled-hexagon geometry underlying PF-230 is classical; standard references such as Peter Buser, *Geometry and Spectra of Compact Riemann Surfaces*, develop the hyperbolic polygon and pants machinery. The small-argument relation `\sinh\rho\sim\rho` is elementary. PF-294's fractional-regularity estimate is already a persisted project theorem.

The project-specific contribution is the **scale identification across existing Prime-Flute results**: PF-230's canonical trimmed-corridor bound controls exactly the `r=w/s` parameter left open by PF-294, via the PF-234/PF-235/PF-258 fixed-axis dictionary. The result is therefore a route-closing corollary for the canonical construction, not a novelty claim about hyperbolic pants or Robin operators in general.

## Boundaries and falsification

1. **Fixed source row.** PF-294's constant depends on `i`. PF-295 does not control a family whose source-row index or number of coherently combined rows grows with `n`.
2. **Component theorem.** The complete PF-290 Riesz representative may contain mixed/global Schur pieces not factored through one fixed-axis source column. PF-279 makes this a serious surviving possibility.
3. **Canonical trimming.** The conclusion uses the PF-205 width `w_j=\kappa d_j`. A different noncanonical seam normalization could have another ratio, but it would require a new geometric/operator justification rather than being attributed to the canonical flute.
4. **Tail statement.** The finite head is irrelevant to the asymptotic compactness/noncompactness tests. No uniform constant over an arbitrarily reparametrized finite head is needed.
5. **No weak-trace conclusion.** Removing this frequency-escape mechanism does not prove that the full heavy extension angle is compact, let alone in `\mathcal S_{1,\infty}`. It only closes one candidate source of PF-292 roughness.

The finding would fail if PF-230's `w_j,\rho_j,s_n` are not the same canonical seam/corridor scales entering the PF-234/PF-235/PF-258 relative edge, or if PF-294's `r=w/s` dictionary is being applied to a different normalization. Those identifications are explicit in the cited findings. A genuine counterexample would therefore have to locate a distinct physical scale in the complete mixed response, not make the canonical ratio diverge.

## Consequence for the research line

The immediate heavy-angle task should no longer spend effort asking whether the canonical seam ratio escapes every bounded set. It does not. The useful question is now sharper: after factoring the canonically uniform fixed-axis source and the PF-255/PF-256 transports, **which exact residual operator, if any, destroys the positive Sobolev margin of the complete normalized response?**

If no such residual rough factor exists, PF-292 kills the local PF-290 noncompactness witness and the line returns to PF-287's global heavy-range essential-orthogonality/counting problem. If one does exist, it must now be exhibited as a genuinely mixed/reassembled mechanism rather than inherited from canonical seam shrinkage.