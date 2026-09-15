# MI-024 — The critical Mangoldt logarithmic end blocks the classical infinity Schur step

**Evidence level:** exact source-asymptotic and Herglotz-sign obstruction from [WP-310](../../findings/WP-310-classical-moment-schur-reduction-cannot-start-on-the-critical-mangoldt-herglotz-source.md), using the classical Nevanlinna moment-Schur framework cited there

The function-level Schur/Nevanlinna route left open after scalar gauge rigidity has a hard entrance condition at infinity. The classical real-line moment Schur step starts from a positive finite-mass Cauchy response

`n(z)=-s_0/z+o(1/z)`, with `0<s_0<infinity`,

so that `-s_0/n(z)` cancels the leading `z` in the first transform.

The canonical reflected critical Mangoldt source is in a different Herglotz class. Its positive measure has asymptotic density one and infinite total mass, while its regularized response satisfies

`m_-(iy)=L(y)+iQ(y)`,

`L(y)=log y-B+A_0/y^2+o(y^-2)`, `Q(y)=pi/2+C_+/y+o(y^-1)`.

Thus `|m_-(iy)|~log y`, not `O(1/y)`. This is not only a mismatch with the moment-Schur hypotheses. Formally inserting the source into the first step with any fixed finite `s_0>0` and real `c`,

`S_(s_0,c)(z)=-s_0/m_-(z)-z+c`,

gives

`Im S_(s_0,c)(iy)=s_0 Q(y)/(L(y)^2+Q(y)^2)-y<0`

for all sufficiently large `y`. The transform actively leaves the Herglotz class.

Finite cutoffs are a matched control: every truncated positive measure has finite moments and admits the classical Schur algorithm exactly, but its zeroth moment grows like the cutoff and diverges in the critical limit. Normalizing the cutoff changes the already-fixed arithmetic normalization. Subtracting the unit-density background makes the remainder finite but signed, so positivity is no longer supplied by the source measure.

Fixed projective preprocessing also does not repair the asymptotic class. An affine recoding preserves the logarithmic end, while a compactifying Möbius map produces only `O(1/log y)` after subtracting its finite boundary limit, still much larger than `1/y`. WP-309 already prevents a holomorphically varying automorphism family from adding further scalar freedom.

The reusable boundary is precise: **the classical source-moment Schur reduction at infinity is closed for the canonical critical Mangoldt Herglotz source.** Surviving Schur/compression routes must introduce genuinely new structure—a finite-reference interpolation transform, a separately derived cutoff/renormalization law, an operator-valued/generalized resolvent construction, or another positive realization not equivalent to the finite-moment infinity step.
