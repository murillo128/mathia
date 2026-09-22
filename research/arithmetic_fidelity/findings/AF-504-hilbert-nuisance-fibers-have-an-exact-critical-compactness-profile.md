# AF-504 — Hilbert nuisance fibers have an exact critical compactness profile

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NUISANCE-QUOTIENT`, `HILBERT-GEOMETRY`, `MEASURE-OF-NONCOMPACTNESS`, `CRITICAL-CONTACT`, `MINIMAL-LIFT`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-503 proves that a fully saturated infinite-dimensional nuisance fiber forces raw noncompactness at every radius strictly above the asymptotic separation threshold, but its Banach-space lower bound vanishes at the exact critical radius. In Hilbert observation geometry the equality case can be resolved exactly: orthogonality makes the nuisance radius collapse at precisely the rate left over after quotient separation.

Let `H` be a Hilbert space, let `V subset H` be a closed linear subspace, let

\[
\pi:H\to Q:=H/V
\]

be the quotient map, let `C subset H` be nonempty, and put `D:=\overline C`. Assume the closed source is fully nuisance-saturated,

\[
\boxed{D+V=D.}
\]

Fix `s in H`, and define

\[
m_T:=\inf_{t\ge T}\operatorname{dist}_H(ts,D),
\qquad
\lambda:=\lim_{T\to\infty}m_T
=\liminf_{t\to\infty}\operatorname{dist}_H(ts,D).
\]

For a fixed radius `R`, write

\[
\alpha_T(R):=\chi_H\bigl(E^0_{T,R}(C,s)\bigr),
\qquad
\beta_T(R):=\chi_Q\bigl(E^V_{T,R}(C,s)\bigr),
\]

using the raw and quotient-visible tail sets of AF-500--AF-503. Set

\[
r_T(R):=\sqrt{(R^2-m_T^2)_+}.
\]

Then for every `T,R`,

\[
\boxed{
\beta_T(R)
\le
\alpha_T(R)
\le
\sqrt{\beta_T(R)^2+r_T(R)^2}.
}
\]

If `V` is infinite-dimensional, the nuisance fiber itself also gives

\[
\boxed{
\alpha_T(R)\ge r_T(R),
}
\]

hence

\[
\boxed{
\max\{\beta_T(R),r_T(R)\}
\le
\alpha_T(R)
\le
\sqrt{\beta_T(R)^2+r_T(R)^2}.
}
\]

Passing to the decreasing tails gives, for finite `lambda` and every `R>=lambda`,

\[
\boxed{
\nu_C^V(s;R)
\le
\nu_C^0(s;R)
\le
\sqrt{\nu_C^V(s;R)^2+R^2-\lambda^2}.
}
\]

When `V` is infinite-dimensional this sharpens to

\[
\boxed{
\max\left\{
\nu_C^V(s;R),
\sqrt{R^2-\lambda^2}
\right\}
\le
\nu_C^0(s;R)
\le
\sqrt{\nu_C^V(s;R)^2+R^2-\lambda^2}.
}
\]

The critical radius is therefore special. At `R=lambda` the nuisance term vanishes and the two tail defects agree **exactly**, with no finite-dimensionality assumption:

\[
\boxed{
\nu_C^0(s;\lambda)
=
\nu_C^V(s;\lambda).
}
\]

Thus quotient-tail compactness at the exact threshold lifts back to the saturated Hilbert source even when the nuisance space is infinite-dimensional:

\[
\boxed{
\nu_C^V(s;\lambda)=0
\iff
\nu_C^0(s;\lambda)=0.
}
\]

By contrast, if `V` is infinite-dimensional and the quotient-visible tail is compact at some `R>lambda`, then the raw defect is not merely positive; it is exactly

\[
\boxed{
\nu_C^0(s;R)=\sqrt{R^2-\lambda^2}.
}
\]

For `R<lambda`, both tail sets are eventually empty and both defects vanish. Consequently a quotient-compact saturated Hilbert model has a genuine square-root phase transition: no raw compactness defect below or at the critical radius, followed immediately by the fiber defect `sqrt(R^2-lambda^2)` above it.

This resolves the compactness part of AF-503's exact-radius boundary in Hilbert geometry. It does **not** remove the separate contact/attainment gate: a compact critical tail can still be empty, so actual equality contacts or a distance-defined threshold still require the existence/attainment conditions isolated in AF-499--AF-500.

## Orthogonal bundle identity

Because `V` is closed,

\[
H=V^\perp\oplus V.
\]

Let

\[
J:Q\to V^\perp
\]

be the canonical isometric section: `J(pi(x))=P_{V^\perp}x`. The Hilbert quotient norm is therefore

\[
\|q\|_Q=\|J(q)\|_H.
\]

Saturation gives

\[
D_V:=\overline{\pi(C)}=\pi(D).
\]

For each quotient residual `q in E^V_{T,R}`, choose `t>=T` and `d in D` with

\[
q=\pi(d-ts).
\]

Writing

\[
d-ts=J(q)+v_0,
\qquad v_0\in V,
\]

saturation permits replacing `d` by `d-v_0`. Hence `J(q)` itself is an admissible raw residual at the same time. Adding any further `v in V` remains inside `D-ts`. Orthogonality then gives the exact fiber description

\[
\boxed{
E^0_{T,R}
=
\left\{
J(q)+v:
q\in E^V_{T,R},\ v\in V,
\ \|v\|^2\le R^2-\|q\|_Q^2
\right\}.
}
\]

Thus the quotient-visible residual `q` carries a nuisance ball of radius

\[
\rho_R(q):=\sqrt{R^2-\|q\|_Q^2}.
\]

This is the Hilbert refinement of AF-503's translated-ball argument. The relevant fiber radius is not merely the radial slack `R-||q||`; Pythagoras converts the same slack into the larger orthogonal radius `sqrt(R^2-||q||^2)`.

## Finite-tail noncompactness bounds

The lower bound

\[
\beta_T(R)\le\alpha_T(R)
\]

follows because `pi` is `1`-Lipschitz and maps the raw tail onto the quotient tail under saturation and Hilbert proximinality.

For the upper bound, every `q in E^V_{T,R}` satisfies

\[
\|q\|_Q\ge m_T,
\]

so every nuisance fiber in the orthogonal bundle has radius at most

\[
r_T(R)=\sqrt{(R^2-m_T^2)_+}.
\]

Fix `epsilon>0`. Cover `E^V_{T,R}` by finitely many quotient balls of radius `beta_T(R)+epsilon`, with centers `q_1,...,q_N`, and lift their centers to `J(q_j) in V^perp`. If

\[
x=J(q)+v\in E^0_{T,R}
\]

and `q` belongs to the ball centered at `q_j`, orthogonality gives

\[
\begin{aligned}
\|x-J(q_j)\|_H^2
&=\|J(q-q_j)\|_H^2+\|v\|_H^2\\
&< (\beta_T(R)+\varepsilon)^2+r_T(R)^2.
\end{aligned}
\]

Hence

\[
\alpha_T(R)
\le
\sqrt{\beta_T(R)^2+r_T(R)^2}.
\]

Now assume `V` is infinite-dimensional. Since `m_T` is the infimum of the norms of the quotient residuals occurring after time `T`, for every `epsilon>0` with `m_T+epsilon<R` there is a `q in E^V_{T,R}` with

\[
\|q\|_Q<m_T+\varepsilon.
\]

The raw tail then contains the entire infinite-dimensional nuisance ball

\[
J(q)+
\sqrt{R^2-\|q\|_Q^2}\,\overline B_V.
\]

As used in AF-503, the Hausdorff measure of noncompactness of a radius-`a` ball in an infinite-dimensional closed subspace, even when measured in the ambient Hilbert space, is exactly `a`. Letting `epsilon downarrow 0` yields

\[
\alpha_T(R)\ge r_T(R).
\]

These arguments also show why finite-dimensional and infinite-dimensional nuisance spaces separate only in the lower bound. Orthogonal lifting always controls how much extra noncompactness can appear, but a bounded fiber contributes a positive Hausdorff defect only when it is itself infinite-dimensional.

## Tail limit and the critical-radius cancellation

The numbers `m_T` increase to `lambda`, while `alpha_T(R)` and `beta_T(R)` decrease to the raw and quotient tail profiles. Therefore, for every fixed `R>=lambda`,

\[
r_T(R)\longrightarrow\sqrt{R^2-\lambda^2}.
\]

Passing to the limit in the finite-tail inequalities gives the claimed asymptotic bounds.

At the exact radius `R=lambda`,

\[
r_T(\lambda)
=\sqrt{\lambda^2-m_T^2}
\longrightarrow0.
\]

Therefore

\[
\nu_C^V(s;\lambda)
\le
\nu_C^0(s;\lambda)
\le
\nu_C^V(s;\lambda),
\]

which proves exact equality. The infinite-dimensional nuisance directions become asymptotically harmless **only because the critical truncation forces their allowable radius to collapse to zero**. No compactness of the full nuisance ball is being recovered.

This distinguishes two logically different statements:

- at `R=lambda`, the truncation itself squeezes the nuisance fibers to vanishing radius, so raw and quotient noncompactness coincide;
- at every fixed `R>lambda`, the allowed nuisance radius converges to the positive number `sqrt(R^2-lambda^2)`, so an infinite-dimensional saturated fiber necessarily survives as raw noncompactness.

If the quotient-visible tail is compact at such an `R>lambda`, the upper and lower bounds meet and give the exact square-root formula.

## Sharp model

Take

\[
H=\mathbb R\oplus_2 V,
\qquad
D=\mathbb N\times V,
\qquad
s=(1,0),
\]

with infinite-dimensional Hilbert `V`. Then `lambda=0` and the quotient tail at every finite radius is eventually the singleton `{0}`, hence has zero Hausdorff noncompactness. At integer times the raw tail contains

\[
\{0\}\times\overline B_V(0,R),
\]

so

\[
\nu_C^0(s;R)=R
=\sqrt{R^2-\lambda^2}.
\]

This attains the formula. More generally, replacing the first-coordinate source by a saturated source whose quotient asymptotic separation is a prescribed `lambda>0` gives the same Pythagorean fiber radius `sqrt(R^2-lambda^2)` whenever the quotient-visible tail is compact.

## Prior-art and novelty audit

No broad novelty is claimed for orthogonal projection, Hilbert quotients, or Hausdorff measures of noncompactness. The ingredients are classical and already anchored by the local source audit used in AF-501--AF-503:

- the projection theorem for closed subspaces of Hilbert space gives `H=V^perp direct-sum V`, unique minimum-norm coset representatives, and the quotient isometry with `V^perp`;
- R. R. Akhmerov, M. I. Kamenskii, A. S. Potapov, A. E. Rodkina, and B. N. Sadovskii, *Measures of Noncompactness and Condensing Operators*, Birkhauser (1992), supplies the standard Hausdorff-measure-of-noncompactness machinery;
- Tomasz Zajac, **“The Concept of Measures of Noncompactness in Banach Spaces,”** *Symmetry* 17(8), 1248 (2025), DOI `10.3390/sym17081248`, records in particular the radius of an infinite-dimensional ball as its Hausdorff noncompactness;
- Robert E. Megginson, *An Introduction to Banach Space Theory*, Springer (1998), DOI `10.1007/978-1-4612-0603-3`, supplies standard closed-subspace and quotient-space background.

A targeted literature search found the expected classical projection and measure-of-noncompactness ingredients but no reason to treat the line-specific tail formula as a named general theorem. The durable Arithmetic Fidelity contribution is the exact composition of those ingredients with the AF-500--AF-503 nuisance-tail object: **in a saturated Hilbert model, raw and quotient Hausdorff noncompactness coincide exactly at the asymptotic separation radius, while an infinite-dimensional nuisance fiber contributes the sharp square-root defect immediately above that radius.**

## Falsification and boundary audit

- Full saturation of the closed source `D` is essential for the exact orthogonal bundle identity. Without it, the minimum-norm representative of a quotient residual need not be an admissible source residual.
- Hilbert geometry is essential for the Pythagorean square-root profile. A general Banach norm has no orthogonal decomposition with `||a+v||^2=||a||^2+||v||^2`; AF-503's weaker universal bound remains the safe statement there.
- Infinite dimensionality of `V` is needed only for the positive fiber lower bound above threshold. The critical identity `nu^0(lambda)=nu^V(lambda)` holds for arbitrary closed `V`.
- The result concerns Hausdorff noncompactness of radius-truncated tails. Another compactness defect can have a different value on an infinite-dimensional ball and therefore a different quantitative profile.
- Critical compactness does not imply critical contact. The radius-`lambda` tail may be empty for arbitrarily large `T` even though `lambda` is the liminf distance. Actual-contact and distance-attainment statements still require the separate gates from AF-499--AF-500.
- A quotient-visible defect `nu_C^V(s;R)>0` can coexist with the nuisance fiber defect. The bounds need not meet away from the quotient-compact regime; no additive Pythagorean identity for arbitrary noncompact quotient sets is claimed.
- The theorem does not recover discarded nuisance coordinates as information. It quantifies when those coordinates are geometrically harmless for the specific compactness test and when restoring them necessarily destroys compactness.
