# ANF-095 — Montgomery--Taylor pair norm sharpens sparse surgery to a matched log-log threshold

**Status:** `EXACT-DERIVED + SPARSE-SURGERY + ENDPOINT-SHARP + LOGLOG-THRESHOLD + NEAR-EXTREMIZER-GATE + QUOTIENT-FRONTIER`. `ANF-094` proves that changing only `m` conjugate pairs of an `N`-point separable carrier cannot leave the protected destination tube while `m cosh(2 pi H)=o(sqrt N)`. That estimate deliberately uses only a uniform pointwise bound and therefore loses the endpoint geometry of the fixed Montgomery--Taylor spectrum. Restoring that geometry gives an exact pair norm and an additional inverse-height factor. On the diluted conditioning family of `ANF-092/093`, the necessary escape scale moves from `(log n)/(4 pi)` to the sharply matched scale `(log n+2 log log n)/(4 pi)+O(1)`. Below that scale the modified block can still be made Montgomery--Taylor near-extremal, so the exact projection taxes of `ANF-088` cannot close the sparse route earlier.

Retain the fixed central-notch spectrum from `ANF-081`,

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad 0\le J_s\le J_{\rm MT},
\qquad q_s>0,
\tag{1}
\]

and the Montgomery--Taylor factor from `ANF-087`,

\[
K(z)=
\frac{\cos(\pi z)-\sqrt2\,\pi z\cot(2^{-1/2})\sin(\pi z)}
     {1-2\pi^2z^2}.
\tag{2}
\]

Let `P` be an all-nonreal separable product multiset of total cardinality `N`, and let `W` be obtained by replacing at most `m` labelled conjugate pairs of `P`. The old and new pair centers may be arbitrary and may collide; assume only that every old and new height has absolute value at most `H`. Then

\[
\boxed{
 d_{\rm sep}(W)
 \le
 \frac{2m}{\sqrt{q_sN}}
 \sqrt{1+K(2iH)^2}.
}
\tag{3}
\]

Equivalently, with the dimensionless sparse-height budget

\[
\boxed{
\Xi_{m,N}(H)
:=
\frac{m^2}{N}\bigl(1+K(2iH)^2\bigr),
}
\tag{4}
\]

one has

\[
\boxed{
 d_{\rm sep}(W)\le \frac{2}{\sqrt{q_s}}\sqrt{\Xi_{m,N}(H)}.
}
\tag{5}
\]

The same quantity controls the largest possible Montgomery--Taylor energy of an arbitrary block of `m` conjugate pairs with heights at most `H`:

\[
\boxed{
E_{\rm MT}(B)
\le
2m^2\bigl(1+K(2iH)^2\bigr)
=2N\Xi_{m,N}(H).
}
\tag{6}
\]

Thus `Xi` is not merely a perturbative bookkeeping parameter. It is the common scale at which a sparse block becomes visible in the destination norm and macroscopic in the Montgomery--Taylor source energy.

## 1. The exact norm of one conjugate pair

For a pair at horizontal center `x` and height `y>=0`, write

\[
B_{x,y}(\alpha)
:=e^{-2\pi i\alpha(x+iy)}+e^{-2\pi i\alpha(x-iy)}
=2e^{-2\pi i\alpha x}\cosh(2\pi\alpha y).
\tag{7}
\]

Because `J_MT` is the Fourier transform of `K^2`, the Montgomery--Taylor norm of this pair is exactly its two-point energy:

\[
\boxed{
\|B_{x,y}\|_{\rm MT}^2
=2+2K(2iy)^2.
}
\tag{8}
\]

The horizontal center disappears because it contributes only a unit-modulus phase. Since `J_s<=J_MT`,

\[
\|B_{x,y}\|_s
\le
\sqrt{2+2K(2iy)^2}.
\tag{9}
\]

Moreover `K(2iy)` is positive and increasing for `y>=0`. Indeed, with the positive even density `g` from `ANF-087`,

\[
K(2iy)
=\int_{-1/2}^{1/2}g(u)e^{4\pi uy}\,du
=\int_{-1/2}^{1/2}g(u)\cosh(4\pi uy)\,du.
\tag{10}
\]

If one pair is replaced by another pair whose two heights are bounded by `H`, the triangle inequality and (9) give a cost at most

\[
2\sqrt{2+2K(2iH)^2}.
\tag{11}
\]

Summing over at most `m` edits yields

\[
\|S_W-S_P\|_s
\le
2m\sqrt{2+2K(2iH)^2}.
\tag{12}
\]

Because `P` is all-nonreal and separable, `ANF-085` gives

\[
\|S_P\|_s^2\ge2q_sN.
\tag{13}
\]

Also `sigma(P)=0<=sigma(W)`, so `P` belongs to the comparison class defining `d_sep(W)` in `ANF-086`. Dividing (12) by (13) proves (3)--(5). No separation, Gram conditioning, or sign assumption in physical space is used.

For an arbitrary block `B` of `m` conjugate pairs at centers `x_j` and heights `|y_j|<=H`, pointwise

\[
|S_B(\alpha)|
\le2m\cosh(2\pi|\alpha|H).
\tag{14}
\]

Integrating against `J_MT` and using (8) proves (6).

## 2. The inverse-height factor is exact, not an artifact

Putting `z=2iy` into (2) gives the closed form

\[
\boxed{
K(2iy)
=
\frac{
\cosh(2\pi y)
+2\sqrt2\,\pi y\cot(2^{-1/2})\sinh(2\pi y)
}{1+8\pi^2y^2}.
}
\tag{15}
\]

Hence

\[
\boxed{
K(2iy)
=
\frac{\cot(2^{-1/2})}{4\sqrt2\,\pi}
\frac{e^{2\pi y}}{y}
\left(1+O\!\left(\frac1y\right)\right)
}
\qquad(y\to\infty).
\tag{16}
\]

Consequently, for `H>=1`,

\[
\boxed{
 d_{\rm sep}(W)
 \le
 C_s\frac{m}{\sqrt N}\frac{e^{2\pi H}}{H}
}
\tag{17}
\]

for a constant depending only on the fixed notch.

This gains a full factor `H^{-1}` over the pointwise `cosh(2 pi H)` bound of `ANF-094`. The gain is genuine destination geometry. The notch `phi_eta` is supported in `[-eta,eta]` with `eta<1`, so

\[
\|B_{x,y}\|_s^2
=
2+2K(2iy)^2
-s\int_{-\eta}^{\eta}\phi_\eta(\alpha)
 4\cosh^2(2\pi\alpha y)\,d\alpha.
\tag{18}
\]

The subtracted term is `O(e^{4 pi eta y})`, whereas (16) gives

\[
K(2iy)^2
\asymp \frac{e^{4\pi y}}{y^2}.
\tag{19}
\]

Therefore

\[
\boxed{
\|B_{x,y}\|_s^2
\sim2K(2iy)^2
\asymp\frac{e^{4\pi y}}{y^2}.
}
\tag{20}
\]

So the `e^{2 pi H}/H` scale cannot be removed by a better estimate for one high pair. It is the true endpoint-Laplace scale of the central-notch destination norm.

## 3. The diluted conditioning family moves to a log-plus-two-log-log threshold

Apply (5) to the exact sparse-dilution scaling of `ANF-092/093`. There the carrier has

\[
N_n=2(n^3+n+1),
\qquad
m_n=n+1.
\tag{21}
\]

If a surgery on that `m_n`-pair block were to reach the fatal threshold of `ANF-086`,

\[
d_{\rm sep}(W_n)\ge\kappa_{\rm crit}>0,
\tag{22}
\]

then (5) forces

\[
\Xi_{m_n,N_n}(H_n)
\ge\frac{q_s\kappa_{\rm crit}^2}{4}.
\tag{23}
\]

Using (16) and `m_n^2/N_n\asymp n^{-1}` gives

\[
\frac{e^{4\pi H_n}}{nH_n^2}\gg_s1.
\tag{24}
\]

In particular

\[
\boxed{
4\pi H_n
\ge
\log n+2\log\log n+O_s(1),
}
\tag{25}
\]

or equivalently

\[
\boxed{
H_n
\ge
\frac{\log n}{4\pi}
+
\frac{\log\log n}{2\pi}
+O_s(1).
}
\tag{26}
\]

This strictly sharpens the necessary height `H_n>=(log n)/(4 pi)+O_s(1)` from `ANF-094`. The missing `2 log log n` came from treating the compactly supported spectrum as if it had nonzero mass right at its endpoint; in reality the exact Montgomery--Taylor pair norm carries the inverse-height factor in (16).

## 4. The same threshold is where sparse dilution stops making the source cost negligible

The new threshold is not merely a stronger screening estimate. It matches the source-energy transition.

Return to the construction of `ANF-092`. Let `q_n=n^3`, let `mathcal H_n` be its high-zero padding comb of `q_n` real centers, and let

\[
C_n=\{0,d,2d,\ldots,nd\},
\qquad m_n=n+1.
\tag{27}
\]

Keep the padding pairs at the collapsing height `y_n=r^{n/8}`, but lift only the `C_n` pairs to a new common height `Y_n`. Denote the resulting conjugation-invariant multiset by `W_n^{(Y)}`. The low padding block alone satisfies

\[
E_{\rm MT}(\mathcal H_n+i\{-y_n,+y_n\})
=4q_n(1+o(1))
\tag{28}
\]

by the high-zero-comb estimate and the same small-height argument as `ANF-092`.

For the lifted `m_n`-pair block, (6) gives

\[
E_{\rm MT}(C_n+i\{-Y_n,+Y_n\})
\le
2m_n^2\bigl(1+K(2iY_n)^2\bigr).
\tag{29}
\]

Hence whenever

\[
\boxed{
\frac{e^{4\pi Y_n}}{nY_n^2}\longrightarrow0,
}
\tag{30}
\]

the lifted block has energy `o(q_n)`. Minkowski's inequality in `L^2(J_MT)` then gives

\[
E_{\rm MT}(W_n^{(Y)})
\le
\left(
\sqrt{4q_n(1+o(1))}+o(\sqrt{q_n})
\right)^2
=4q_n(1+o(1)).
\tag{31}
\]

Since `W_n^{(Y)}` has `q_n+m_n` conjugate pairs and no real sites,

\[
L(W_n^{(Y)})=4(q_n+m_n)=4q_n(1+o(1)).
\tag{32}
\]

Lamzouri's lower bound supplies the reverse inequality, so

\[
\boxed{
\frac{\Delta(W_n^{(Y)})}{L(W_n^{(Y)})}\longrightarrow0.
}
\tag{33}
\]

For example, every fixed `epsilon>0` permits

\[
\boxed{
4\pi Y_n
=
\log n+(2-\epsilon)\log\log n,
}
\tag{34}
\]

and still (33) holds. By `ANF-088`, all terms in the exact projection-tax decomposition are then `o(L)` as well.

Thus the source and destination thresholds meet to within `O(1)` in height. Below

\[
4\pi H=\log n+2\log\log n-O(1),
\tag{35}
\]

the sparse block can remain source-negligible and the destination surgery is automatically screened. At the fatal scale, `Xi=Theta(1)`: the edited block is simultaneously capable of carrying macroscopic destination norm and macroscopic Montgomery--Taylor energy. The next obstruction cannot be obtained by pushing the old height estimate or by citing the projection tax alone; it has to analyze whether that **critical `Xi=Theta(1)` block can use source cancellation/quotient geometry to remain globally near-extremal while staying a fixed distance from every separable carrier**.

## 5. Adversarial checks and evidence boundary

The estimate (3) survives arbitrary horizontal motion of the edited pairs because each pair norm is translation invariant in spectral space. It also allows collisions and repeated pairs; the factor `m` in the triangle inequality is therefore unavoidable at this level, since coincident edits can add coherently. The asymptotic (16) was checked directly from the exact rational-trigonometric formula (2), and independently follows from endpoint Laplace asymptotics for the positive density `g`.

The near-extremal construction in Section 4 does not use cancellation between the lifted block and the padding. It uses only the upper bound (29), the already proved near-extremality of the padding, Minkowski, and Lamzouri's global floor. Thus (33) is robust to the detailed horizontal geometry of the lifted block as long as its cardinality and height obey (30).

The result does **not** prove that a critical `Xi=Theta(1)` surgery has `d_sep` bounded below, nor that such a surgery can remain Montgomery--Taylor near-extremal. Equation (5) is an upper bound on the distance to one explicit separable comparator, not a lower bound on the intrinsic infimum. Likewise (6) is an upper bound on block energy. The critical transition remains the genuine unresolved case.

A targeted prior-art check against Lamzouri's current Hilbert-space proof, the Montgomery--Taylor/Carneiro--Chandee--Littmann--Milinovich extremal-kernel literature, and standard complex-exponential/frame perturbation results did not identify a result giving the line-specific sparse-surgery parameter (4), the exact destination pair scale (20), or the matched threshold (25). The only load-bearing external ingredients are already anchored in `SOURCES.md`; the new argument is an exact consequence of the fixed Mathia notch, the explicit Montgomery--Taylor factor, and the internal separable-floor results. `SOURCES.md` is therefore unchanged.

## Research consequence

`ANF-094` left open whether the logarithmic height needed to make a sparse bad block visible could coexist with Montgomery--Taylor near-extremality. The answer is now scale-sharp: the crude logarithmic threshold was too early by `2 log log n` in the exponent. Up to that corrected boundary, near-extremality and the exact projection-tax identity are fully compatible, but the destination defect is still forced to zero. A genuinely dangerous sparse-conditioning mechanism must live at the matched transition `Xi=Theta(1)`, where its nonseparable destination mass and its source-energy budget are both macroscopic. The next useful theorem should therefore attack this critical block directly in the **destination-quotiented** geometry, rather than strengthen raw or source-only conditioning estimates.