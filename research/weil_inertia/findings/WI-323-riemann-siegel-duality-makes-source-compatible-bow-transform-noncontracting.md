# WI-323 — Riemann--Siegel duality makes the source-compatible bow transform noncontracting

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

WI-194 showed that, at the count-saturating bow scale `A\asymp X^2`, the joint logarithmic phase

\[
\phi(m,n)=A\log\frac nm,
\qquad A:=\frac{U}{2\pi},
\]

is self-dual under the two-dimensional stationary map. WI-322 then sharpened the source normalization: every source-compatible symmetrized Maynard--Pratt bow has reciprocal prime length

\[
X_*\le \sqrt{\frac{U}{2\pi}}\,(1+o(1))
=\sqrt A\,(1+o(1)),
\]

not merely `T^(1/2+o(1))`. Combining those two facts closes a natural remaining escape more strongly than either finding separately.

The direct logarithmic Poisson/B-process transform is not merely self-dual at exact count saturation. For **every source-compatible bow**, its natural dual length is

\[
\boxed{Y_*:=\frac A{X_*}\ge X_*(1-o(1)).}
\]

Thus it cannot shorten the arithmetic source by a power. At exact local count saturation it is asymptotically self-dual; if the bow spacing is larger and the reciprocal source length is shorter, the direct dual is longer. Moreover the multiplicative localization and the square-root Dirichlet normalization are exactly preserved by the stationary map: `p/q=n/m`, and the stationary Hessian sends `1/\sqrt{mn}` exactly to `1/\sqrt{pq}`. The geometric transform therefore supplies neither a hidden bandwidth contraction nor a hidden normalized amplitude gain.

This is a barrier only to using the **direct approximate-functional-equation / joint logarithmic stationary transform as a compression mechanism**. It is not an estimate for the prime-weighted covariance and does not resolve the accepted distinguished-twist clue. Arithmetic cancellation in the transformed coefficients, a genuinely different source decomposition, spectral input, or another source-fixed invariant can still succeed. No unconditional simple-critical-zero proportion changes here.

## 1. Exact normalized self-duality of the logarithmic kernel

Retain the central source variables of WI-188 and WI-194. Put

\[
A:=\frac{U}{2\pi},
\qquad
\phi(m,n):=A\log\frac nm,
\qquad
m,n>0.
\tag{1}
\]

For a two-dimensional Poisson/stationary term with dual frequencies `(-p,q)`, `p,q>0`, the critical equations are

\[
\frac A m=p,
\qquad
\frac A n=q.
\tag{2}
\]

Hence

\[
\boxed{m=\frac A p,\qquad n=\frac A q.}
\tag{3}
\]

When `n>m`, one has `p>q`. Evaluating the Legendre phase gives the WI-194 identity

\[
\phi(m,n)+pm-qn
=A\log\frac pq.
\tag{4}
\]

There is, however, a stronger exact invariance that is useful for the localized bow problem. Equation (3) gives

\[
\boxed{\frac pq=\frac nm.}
\tag{5}
\]

Therefore every multiplicative localizer depending only on the logarithmic ratio is transported without any change of its dimensionless argument. In particular, for the triangular localization used in WI-195,

\[
\boxed{
H\log\frac pq
=H\log\frac nm.
}
\tag{6}
\]

The source bandwidth `|H log(n/m)|\le1` is exactly the same dual bandwidth `|H log(p/q)|\le1`. This is stronger than saying that two diagonal strips have comparable widths at one scale: the **relative multiplicative geometry is identical pointwise under the stationary map**.

The square-root source normalization is also exactly self-dual. The Hessian is

\[
\nabla^2\phi(m,n)
=
\begin{pmatrix}
A/m^2&0\\
0&-A/n^2
\end{pmatrix},
\qquad
\left|\det\nabla^2\phi(m,n)\right|
=\frac{A^2}{m^2n^2}.
\tag{7}
\]

Thus the leading two-dimensional stationary Jacobian is

\[
\left|\det\nabla^2\phi\right|^{-1/2}
=\frac{mn}{A}.
\tag{8}
\]

Multiplying by the geometric factor in the BGSTB prime square gives

\[
\frac1{\sqrt{mn}}
\left|\det\nabla^2\phi\right|^{-1/2}
=
\frac{\sqrt{mn}}A.
\tag{9}
\]

But (3) also gives `pq=A^2/(mn)`, hence

\[
\boxed{
\frac{\sqrt{mn}}A=\frac1{\sqrt{pq}}.
}
\tag{10}
\]

So, at the geometric stationary-phase level, the normalized kernel

\[
\frac1{\sqrt{mn}}
\widehat W\!\left(H\log\frac nm\right)
 e\!\left(A\log\frac nm\right)
\tag{11}
\]

returns to the same square-root normalization, the same multiplicative localizer, and the same logarithmic phase in the dual variables `(p,q)`, apart from the standard stationary-phase convention/signature factor. The Hessian has one positive and one negative direction, so there is no source of a power saving in that universal factor.

Equations (5), (6), and (10) are algebraic identities. They do **not** assert that raw `\Lambda(m)\Lambda(n)` can be passed through stationary phase as a smooth amplitude. Any rigorous arithmetic transform must first justify the treatment of those coefficients. Their role here is to identify what the direct phase geometry can and cannot contribute once such a transformation is legitimate.

## 2. Exact Riemann--Siegel scale makes the direct dual noncontracting

Let `X_*` be the reciprocal prime length forced by a source-compatible symmetrized bow. WI-322 proves, using the exact local Riemann--von Mangoldt density rather than only exponent-level counting,

\[
\boxed{
X_*\le \sqrt A\,(1+o(1)),
\qquad A=\frac{U}{2\pi}.
}
\tag{12}
\]

Define the scale ratio

\[
\lambda_T:=\frac{A}{X_*^2}.
\tag{13}
\]

Then

\[
\boxed{\lambda_T\ge1-o(1).}
\tag{14}
\]

If `m,n\asymp X_*`, equation (3) places the stationary dual variables at the central scale

\[
Y_*:=\frac A{X_*}
=\lambda_TX_*.
\tag{15}
\]

Consequently

\[
\boxed{
\frac{Y_*}{X_*}=\lambda_T\ge1-o(1).
}
\tag{16}
\]

There are two regimes. At exact local count saturation, `X_*\sim\sqrt A` and `Y_*\sim X_*`: the transform is asymptotically self-dual. If the bow spacing exceeds the count-minimal value enough to make `X_*` smaller than `\sqrt A`, then `\lambda_T>1` at the corresponding scale and **the direct dual length is larger than the source length**. Moving deeper onto the short side of the Riemann--Siegel point therefore cannot buy a shorter dual Dirichlet object by applying the same logarithmic transform.

This is exactly the length reciprocity in the classical approximate functional equation. In the standard notation for `\zeta(\sigma+it)`, one chooses truncation lengths `x,y` with

\[
\boxed{2\pi xy=t.}
\tag{17}
\]

Thus `xy=t/(2\pi)` and the fixed point is `x=y=\sqrt{t/(2\pi)}`. DLMF §25.9.1 states this classical approximate functional equation and cites Titchmarsh, *The Theory of the Riemann Zeta-function*, equation (4.12.4), p. 79. Hardy--Littlewood's 1923 paper is the classical source of the approximate-functional-equation method. Equation (15) is therefore not a new functional equation: the new line-local consequence is that WI-322 places the bow source **on or below that fixed point**, so the classical duality points in the noncontracting direction.

## 3. The localized diagonal strip cannot shrink under the same transform

The exact ratio identity (5) already proves preservation of the relative bandwidth. It is also useful to spell out the additive scale. From (3),

\[
\boxed{
p-q
=A\left(\frac1m-\frac1n\right)
=\frac{A(n-m)}{mn}.}
\tag{18}
\]

Dividing by either dual coordinate gives two exact relative identities:

\[
\boxed{
\frac{p-q}{q}=\frac{n-m}{m},
\qquad
\frac{p-q}{p}=\frac{n-m}{n}.
}
\tag{19}
\]

Suppose the source localizer restricts a dyadic block `m,n\asymp X_*` to relative width `O(1/H)`, equivalently to the natural additive width

\[
K_*:=\frac{X_*}{H}.
\tag{20}
\]

The dual central scale is `Y_*=\lambda_TX_*`, while (19) keeps the relative width `O(1/H)`. Its natural additive width is therefore

\[
\boxed{
K_*^\vee:=\frac{Y_*}{H}
=\lambda_TK_*.
}
\tag{21}
\]

By (14), this is not asymptotically smaller than the source width by any fixed power. At exact self-duality it is the same scale; on the short side it is longer.

The same bookkeeping can be phrased as a phase-space count. A source dyadic diagonal strip has `\asymp X_*K_*=X_*^2/H` lattice cells at the scale level. The dual strip has

\[
\asymp Y_*K_*^\vee
=\frac{Y_*^2}{H}
=\lambda_T^2\frac{X_*^2}{H}.
\tag{22}
\]

Hence the direct transform does not geometrically compress the active family; at the self-dual point it preserves its scale, and for `\lambda_T>1` the dual stationary region expands. The exact Jacobian in (7)--(10) simultaneously shows that this expansion is not accompanied by a new normalized square-root weight that would constitute a hidden power saving. Cancellation can of course occur among the dual arithmetic coefficients, but that is additional arithmetic information, not phase-space compression.

This strengthens WI-194 in two ways. WI-194 assumed the count-saturating scale `A\asymp X^2` and concluded only comparability of the source and dual strips and order-one stationary amplitude. Equations (5), (10), and (19) give exact normalized invariance, while WI-322 promotes the scale statement from the count-saturating case to **every source-compatible bow** and fixes the direction of any imbalance.

## 4. What route is closed, and what remains open

The finding closes the following weak strategy:

\[
\text{source-compatible bow at reciprocal length }X_*
\;\longrightarrow\;
\text{direct logarithmic AFE/Poisson/B transform}
\;\longrightarrow\;
\text{a shorter arithmetic object that black-box estimates can resolve}.
\tag{23}
\]

The last implication is unavailable. The exact source count places `X_*` on or below the Riemann--Siegel fixed point, and the direct dual length is `A/X_*\ge X_*(1-o(1))`; the relative multiplicative bandwidth and normalized square-root kernel are unchanged.

This does **not** say that an approximate functional equation is useless in a future proof. It may expose arithmetic coefficients with additional cancellation, allow a nontrivial bilinear decomposition, interact with a spectral transform, or be one step in a method whose gain comes from arithmetic rather than geometry. Nor does it say that the transformed covariance is large. The conclusion is specifically that **duality itself is not the missing contraction**.

The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` therefore remains open. WI-195 reduces its source-fixed square to a positive multiplicative short-interval `L^2` norm; WI-196 shows that generic positivity and twist averaging cannot forbid a distinguished dip; WI-197 shows that the published MRSTT Type-II transfer misses the required norm even after unrealistically strong pointwise input. The present finding adds that one cannot escape those norm barriers simply by sending the source across the classical Riemann--Siegel duality and hoping the arithmetic length becomes shorter.

The required advance still has to enter through information absent from (1)--(22): signed source-specific cancellation in the von-Mangoldt coefficients, a genuinely stronger localized second-moment/dispersion theorem, a new source-fixed observable with incompatible near-null directions, or another exact decomposition/inertia mechanism.

## 5. Prior-art and novelty audit

The reciprocal-length law (17) and the self-dual length `\sqrt{t/(2\pi)}` are classical. A primary historical anchor is G. H. Hardy and J. E. Littlewood, **The Approximate Functional Equation in the Theory of the Zeta-Function, with Applications to the Divisor-Problems of Dirichlet and Piltz**, *Proceedings of the London Mathematical Society* s2-21 (1923), 39--74, DOI `10.1112/plms/s2-21.1.39`. A modern authoritative statement is NIST DLMF §25.9.1, which gives the approximate functional equation under `2\pi xy=t` and cites E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed. (1986), equation (4.12.4), p. 79.

The logarithmic stationary geometry is also not new. WI-191 already identifies the one-dimensional bow B-process phase exactly with Atkinson's classical phase, and WI-194 derives the joint map `(m,n)=(A/p,A/q)` and the logarithmic-ratio self-duality at the count-saturating scale. WI-322 supplies the new input used here: exact Riemann--von Mangoldt normalization forces `X_*` to the short side of the same Riemann--Siegel fixed point.

A bounded prior-art audit found the classical approximate-functional-equation and Atkinson/B-process frameworks, but no source was located whose theorem surface states the specific line-local conclusion obtained by combining them with the source-compatible bow count: exact preservation of the multiplicative localizer and square-root stationary normalization together with one-sided noncontraction for every source-compatible bow. This absence is **not evidence of priority**, and no priority claim is made. The durable contribution is the exact synthesis and its route-closing consequence inside the present Weil-inertia program.

## Research consequence

The bow arithmetic problem is now more sharply separated from its geometric transform. The count constraint fixes the source on the noncontracting side of Riemann--Siegel duality; the direct stationary map preserves the normalized logarithmic kernel exactly. Therefore another pass through approximate-functional-equation or joint B-process geometry cannot, by itself, convert the distinguished source square into an easier shorter-length problem.

Future work on the accepted bow clue should test the **arithmetic coefficient transform**, not the phase transform: what signed structure survives after a legitimate decomposition of the `\Lambda(m)\Lambda(n)` weights, whether the dual fiber coefficients possess cancellation unavailable to arbitrary coefficients, or whether a second source-fixed observable rules out the common near-null direction. Any proposed gain that uses only the reciprocal length, logarithmic phase, Hessian, or triangular multiplicative bandwidth has already been accounted for by the exact self-duality above.