# MC-512 — Pair-phase participation factorizes the MC-511 collision gate

**Evidence:** `EXACT-DERIVED · FRONTIER-ADVANCE · CLASSICAL-COLLISION-DIVERSITY+DERIVED-SPECIALIZATION · PRIOR-ART-AUDITED · NO-GENERAL-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-511` reduces the same-relative-state contribution to the physical collision second moment to one effective participation quantity,

\[
R_*=
\frac{W^2}{\sum_{u,t} b_u(t)^2},
\]

where (u) ranges over ordered source pairs, (b_u(t)\ge0) is the exact pair-resolved contribution to conductor coordinate (t\in\mathbf F_p), and

\[
W=\sum_{u,t}b_u(t)>0.
\]

That scalar mixes two logically different resources: how many source pairs carry material mass, and how broadly each material pair spreads its own mass across conductor phase. They separate exactly.

For every pair with positive mass define

\[
w_u:=\sum_t b_u(t),
\qquad
\alpha_u:=\frac{w_u}{W},
\qquad
\pi_u(t):=\frac{b_u(t)}{w_u}.
\]

Define the effective pair participation

\[
R_{\rm pair}
:=
\frac{1}{\sum_u\alpha_u^2}
=
\frac{W^2}{\sum_u w_u^2},
\tag{1}
\]

and the within-pair effective phase support

\[
S_u
:=
\frac{1}{\sum_t\pi_u(t)^2}
=
\frac{w_u^2}{\sum_t b_u(t)^2}.
\tag{2}
\]

Thus (1\le S_u\le p). Weight the pairs by their squared mass,

\[
\lambda_u
:=
\frac{\alpha_u^2}{\sum_v\alpha_v^2},
\qquad
\sum_u\lambda_u=1,
\tag{3}
\]

and let

\[
S_{\rm phase}
:=
\left(
\sum_u\frac{\lambda_u}{S_u}
\right)^{-1}.
\tag{4}
\]

Then the `MC-511` participation factorizes exactly:

\[
\boxed{
R_*=R_{\rm pair}\,S_{\rm phase}.
}
\tag{5}
\]

In particular,

\[
1\le S_{\rm phase}\le p,
\qquad
R_{\rm pair}\le R_*\le pR_{\rm pair}.
\tag{6}
\]

If every material pair has (S_u\ge s), then (S_{\rm phase}\ge s) and therefore (R_*\ge sR_{\rm pair}). The weighting in ((4)) is essential: diffuse phase support on tiny pair-mass tails does not inflate the effective participation seen by the collision energy.

If (L) bounds every exact relative-state fibre, the `MC-511` gate

\[
R_*\ge pL
\tag{7}
\]

is therefore equivalent to

\[
\boxed{
R_{\rm pair}S_{\rm phase}\ge pL.
}
\tag{8}
\]

This yields three exact regimes before any cross-state collision estimate is attempted:

1. If (R_{\rm pair}<L), then ((7)) is impossible even at maximal within-pair spread (S_{\rm phase}=p).
2. If (R_{\rm pair}\ge pL), then ((7)) is automatic even at minimal within-pair spread (S_{\rm phase}=1).
3. If (L\le R_{\rm pair}<pL), then ((7)) holds exactly when
   [
   S_{\rm phase}\ge\frac{pL}{R_{\rm pair}}.
   \tag{9}
   ]

Equivalently, the normalized same-state tariff itself factorizes as

\[
\boxed{
\frac{pL}{R_*}
=
\frac{L}{R_{\rm pair}}
\frac{p}{S_{\rm phase}}.
}
\tag{10}
\]

Thus the next source audit no longer has to treat a small (R_*) as one opaque failure. It can determine whether the bottleneck is **between-pair concentration**, **within-pair phase concentration**, or both.

This is a diagnostic factorization, not a cancellation theorem. It proves no lower bound for either factor, no estimate for the cross-state collision mass, and no new bound for (M(x)).

## 1. Exact derivation

From the definitions,

\[
\sum_{u,t}b_u(t)^2
=
\sum_u w_u^2\sum_t\pi_u(t)^2
=
\sum_u\frac{w_u^2}{S_u}.
\tag{11}
\]

After dividing by (W^2),

\[
\frac{1}{R_*}
=
\sum_u\frac{\alpha_u^2}{S_u}.
\tag{12}
\]

But

\[
\sum_u\alpha_u^2=\frac1{R_{\rm pair}},
\]

and by ((3)),

\[
\sum_u\frac{\alpha_u^2}{S_u}
=
\left(\sum_u\alpha_u^2\right)
\left(\sum_u\frac{\lambda_u}{S_u}\right)
=
\frac1{R_{\rm pair}S_{\rm phase}}.
\tag{13}
\]

Inverting gives ((5)).

Because every probability law on (p) residues satisfies

\[
\frac1p\le\sum_t\pi_u(t)^2\le1,
\]

one has (1\le S_u\le p). A weighted harmonic mean of numbers in ([1,p]) remains in ([1,p]), proving ((6)). Equations ((7))--((10)) are then immediate algebra.

No independence assumption, random model, equidistribution theorem, smoothing, or asymptotic estimate enters the factorization.

## 2. Substitution into the localized relative-state tariff

In the localized setting of `MC-510`, write

\[
B=H(2Q+H),
\qquad
N_z=pM_z.
\]

That finding gives the exact-state fibre upper bound

\[
L\le L_z
=
1+
2\left\lfloor\frac{B}{pM_z}\right\rfloor
\left(
1+\left\lfloor\frac{H}{p\min I}\right\rfloor
\right).
\tag{14}
\]

Combining `MC-511` with ((5)) gives the source-resolved certificate

\[
\boxed{
\frac{pC_{\rm same}}{W^2}
\le
\frac{pL_z}{R_{\rm pair}S_{\rm phase}}.
}
\tag{15}
\]

In the common regime (H<p\min I),

\[
L_z
\le
1+\frac{2B}{pM_z},
\]

so

\[
\boxed{
\frac{pC_{\rm same}}{W^2}
\le
\frac{p}{R_{\rm pair}S_{\rm phase}}
+
\frac{2B}{M_zR_{\rm pair}S_{\rm phase}}.
}
\tag{16}
\]

Equation ((16)) refines the `MC-511` audit without changing its mathematics. The primorial depth (M_z) controls exact-state recurrence, while (R_{\rm pair}) and (S_{\rm phase}) measure two independent ways the physical source can fail to realize the large (R_*) needed to make that recurrence collision-irrelevant.

For a dyadic source block (I=[Q,2Q]), (B=3Q^2), so the sufficient condition becomes

\[
R_{\rm pair}S_{\rm phase}\gg p,
\qquad
M_zR_{\rm pair}S_{\rm phase}\gg Q^2.
\tag{17}
\]

The product in ((17)) is still (R_*); the gain is diagnostic rather than numerical. It identifies which factor a source-specific theorem must actually control.

## 3. Consequence for the accepted localized-cross-state clue

The accepted clue previously asked for a direct lower bound on (R_*) before attacking the cross-state pushforward. Equation ((5)) turns that into two separate, representation-faithful questions.

First estimate the effective pair population (R_{\rm pair}) from the exact reconstruction weights. A large raw count of ordered pairs is irrelevant if most mass sits on a few pairs. If (R_{\rm pair}<L_z), the `MC-511` gate cannot be reached by phase spreading alone, so attempting a cross-state argument under that gate is premature.

If instead (R_{\rm pair}\ge pL_z), no within-pair phase theorem is needed for the gate: same-state recurrence is already priced out at the natural conductor collision scale. The live object is immediately the many-to-one map from distinct relative states to the physical coordinate (t=x+j).

Only in the intermediate range

\[
L_z\le R_{\rm pair}<pL_z
\]

does the detailed physical phase spread matter. There the exact target is ((9)): prove enough weighted harmonic phase support (S_{\rm phase}), with the square-mass weights (lambda_u), rather than prove a visually broad support statement for typical or unweighted pairs.

This prevents two false positives. Many source pairs do not help if their reconstruction mass is concentrated, and highly diffuse low-mass pairs do not help if the collision energy is carried by concentrated heavy pairs.

## 4. Prior art and novelty boundary

The single-level quantity

\[
\left(\sum_i p_i^2\right)^{-1}
\]

is classical. Hill's diversity numbers place the inverse-Simpson quantity in a continuum of effective-number measures, and Jost emphasizes the interpretation of transformed Simpson/Gini-Simpson quantities as effective numbers. Those references are recorded as `MC-S57` and `MC-S58`.

No novelty is claimed for inverse participation ratios, Simpson collision probability, Hill numbers, harmonic means, or the elementary regrouping in ((11))--((13)). In particular, ((5)) should not be described as a general Shannon-style or Rényi-style chain rule: the conditional weighting here is the specific squared pair-mass escort (lambda_u\propto\alpha_u^2) forced by the collision second moment.

The Mathia-specific contribution is the exact specialization to the `MC-511` pair-resolved first-exit collision gate. It converts the opaque condition (R_*\ge pL) into the three-regime source audit ((8))--((10)), separating source-pair mass participation from within-pair conductor-phase participation without changing the physical measure.

## Representation audit

The factorization is performed **before** pair provenance is discarded. It uses the same nonnegative (b_u(t)) admitted by `MC-511) and introduces no completed period, uniform start model, random source, or surrogate mask.

The decomposition also preserves the collision weighting exactly. The relevant phase average is not an ordinary average of the (S_u), but the harmonic mean under squared pair masses. This is precisely the weighting produced by the original quadratic energy and prevents low-weight diffuse pairs from manufacturing a large effective support.

## Boundaries and falsification tests

- **Positive pair mass.** Pairs with (w_u=0) are omitted. They contribute neither to (W) nor to the collision energy.
- **Nonnegative pair-resolved branch.** The probability/support interpretation needs (b_u(t)\ge0). A signed or complex pre-aggregation remains a separate escape.
- **Raw cardinality is insufficient.** The number of source pairs can be large while (R_{\rm pair}) stays (O(1)).
- **Raw phase support is insufficient.** A pair can visit many residues while one residue carries nearly all of its mass, leaving (S_u) small.
- **Typical-pair spread is insufficient.** Because (S_{\rm phase}) uses squared pair-mass weights, a small set of heavy concentrated pairs can dominate it.
- **The factorization does not control (C_{\rm cross}).** Passing ((8)) only says same-state recurrence cannot carry the relevant collision budget; distinct states may still collide strongly after the physical pushforward.
- **The fibre tariff remains an upper bound.** Replacing the true fibre size by (L_z) is conservative.
- **No global Möbius conclusion.** There is no new estimate for (M(x)), no zero-free region, and no RH consequence.

## Consequence

The first unresolved quantitative step after `MC-511` is now bifurcated cleanly. Measure the exact reconstruction mass across source pairs through (R_{\rm pair}), and measure the collision-weighted within-pair conductor spread through (S_{\rm phase}). Their product is exactly the old (R_*), but the factorization identifies which resource is absent and gives a sharp three-regime gate against the relative-state fibre tariff.

Only after that gate is passed should the nonnegative branch spend effort proving a cross-state anti-diagonal dispersion theorem. If the gate fails because (R_{\rm pair}<L_z), no possible within-pair phase spread can rescue it; if (R_{\rm pair}\ge pL_z), the phase-spread audit can be skipped entirely.
