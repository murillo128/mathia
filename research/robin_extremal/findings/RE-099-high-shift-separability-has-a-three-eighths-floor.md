# RE-099 — high-shift separability has a three-eighths floor

**Status:** `EXACT-DERIVED + NEGATIVE/METHOD-OBSTRUCTION + DEFORMED-QUADRATIC-SPARSE-HOSTS + FOURTH-MOMENT-HIGH-SHIFTS + POINTWISE-KERNEL-SEPARABILITY + THREE-EIGHTHS-FLOOR + SHIFTED-ENERGY-QUANTIFICATION + PRIOR-ART-AUDITED`.

`RE-098` splits the fourth-moment route for the residual mixed first/depth-two Robin channel into a near-resonant block, already controlled in the useful interval

\[
\frac{69-16\sqrt3}{121}<\vartheta<\frac{73}{200},
\]

and a nonresonant block involving the deformed-quadratic phase kernel

\[
S_X(\Omega)
=\sum_{n\asymp X^{1/2}}e^{i\Omega\log x(n)},
\qquad
x(n)=\eta_1^{-1}(\eta_2(n)).
\]

That finding left open whether sufficiently strong pointwise cancellation in `S_X(\Omega)` might by itself finish the high-shift block, with shifted four-zero information merely an alternative resource. It cannot, within the natural **separable absolute-value architecture** that bounds the phase kernel pointwise and then pays for the zero quartets only through their total count. At the critical real-part slab `sigma=1/2`, even the unrealistically favorable bound `|S_X(\Omega)|=X^{o(1)}` for every high shift leaves the condition

\[
\boxed{\vartheta>\frac38.}
\]

This is already outside the Robin host window `vartheta<73/200`, since

\[
\frac38-\frac{73}{200}=\frac1{100}.
\]

Thus pointwise exponential-sum technology alone cannot close the present route. A successful fourth-moment proof must obtain a genuine saving in the effective high-shift quartet mass, or retain enough joint oscillation between the quartet shift and the sample kernel that the two objects are never separated by absolute values. Quantitatively, even under ideal pointwise kernel control, reaching some `vartheta<73/200` requires a high-shift quartet saving strictly larger than `T^(8/127)` relative to the unstructured `T^4` count.

## 1. The separable high-shift architecture

Keep the notation of `RE-098`:

\[
M=X^{1/2},
\qquad
H=X^\vartheta,
\qquad
T=\frac XH(\log X)^3
 =X^{1-\vartheta+o(1)}.
\tag{1}
\]

After the explicit-formula reduction and a `1/log X` real-part decomposition, a slab beginning at `sigma` contributes

\[
X^{4\sigma-4+o(1)}
\sum_{\rho_1,\ldots,\rho_4}
S_X(\gamma_1+\gamma_2-\gamma_3-\gamma_4),
\tag{2}
\]

up to the harmless conjugations and coefficient majorants already absorbed in the model bound of `RE-098`. Write

\[
\Omega=\gamma_1+\gamma_2-\gamma_3-\gamma_4.
\]

The near-resonant region `|Omega|<=1` is not at issue here: `RE-098` controls it by the Heath-Brown four-zero energy estimate and obtains the threshold `0.341216...`.

Consider instead a high-shift region in which one estimates the kernel pointwise,

\[
|S_X(\Omega)|\le K_{\rm hi}(X,T),
\tag{3}
\]

and then discards all additive information among the zeros, bounding the number of admissible quartets only by the fourth power of the ordinary zero count. This gives, at the critical slab `sigma=1/2`,

\[
\mathcal B_{\rm hi}(1/2)
\ll
X^{-2+o(1)}
K_{\rm hi}(X,T)
N(1/2,T)^4.
\tag{4}
\]

The Riemann--von Mangoldt count gives

\[
N(1/2,T)=T^{1+o(1)},
\tag{5}
\]

so if

\[
K_{\rm hi}(X,T)\ll X^{\kappa+o(1)},
\qquad \kappa\ge0,
\tag{6}
\]

then

\[
\boxed{
\mathcal B_{\rm hi}(1/2)
\ll
X^{-2+\kappa+4(1-\vartheta)+o(1)}
=
X^{2+\kappa-4\vartheta+o(1)}.
}
\tag{7}
\]

This is a statement about what the **separable estimate proves**, not a lower bound for the true fourth moment. The point is precisely to identify which information is destroyed when the shift and the phase kernel are separated.

## 2. Even perfect pointwise phase cancellation stops at `3/8`

The bad-host set has trivial size `M=X^(1/2)`. To obtain the fixed power saving required by `RE-095`, the exponent in (7) must be strictly below `1/2`. Hence every estimate of the form (3)--(6) needs

\[
2+\kappa-4\vartheta<\frac12,
\]

or equivalently

\[
\boxed{
\vartheta>rac38+\frac\kappa4.
}
\tag{8}
\]

The best conceivable case in this information class is `kappa=0`: grant a uniform bounded/subpower kernel for **every** high shift. Equation (8) still demands

\[
\boxed{\vartheta>\frac38=0.375.}
\tag{9}
\]

But the Robin splice of `RE-095` needs some

\[
\vartheta<\frac{73}{200}=0.365.
\tag{10}
\]

The two intervals are disjoint by exactly `1/100` at their endpoints. Therefore no improvement in a conventional pointwise estimate for `S_X` can by itself bridge the present Robin window once the zero quartets have been replaced by their unstructured total count.

The conclusion becomes still more restrictive for familiar cancellation scales. If the pointwise kernel is parameterized by

\[
K_{\rm hi}\ll M^\lambda=X^{\lambda/2+o(1)},
\tag{11}
\]

then (8) reads

\[
\vartheta>\frac38+\frac\lambda8.
\tag{12}
\]

For example, square-root cancellation relative to the `M` sample terms (`lambda=1/2`) would still require `vartheta>7/16`. Thus the obstruction is not a complaint that current exponent-pair technology is quantitatively weak; it survives after granting pointwise cancellation far stronger than one should expect uniformly.

## 3. The minimum shifted-quartet saving can be quantified exactly

Suppose the high-shift quartet factor is not paid by the full `T^4`, but an argument supplies an effective absolute-mass bound

\[
Q_{\rm hi}(T)\ll T^{4-\eta+o(1)},
\qquad \eta\ge0,
\tag{13}
\]

while the pointwise kernel satisfies (6). The analogue of (7) is

\[
\mathcal B_{\rm hi}(1/2)
\ll
X^{-2+\kappa+(4-\eta)(1-\vartheta)+o(1)}.
\tag{14}
\]

There exists some `vartheta<73/200` for which (14) beats `X^(1/2)` by a fixed power only if the limiting inequality at `vartheta=73/200` is strict:

\[
-2+\kappa+(4-\eta)\frac{127}{200}<\frac12.
\tag{15}
\]

Solving gives the exact necessary threshold within this separable model,

\[
\boxed{
\eta>rac{8+200\kappa}{127}.
}
\tag{16}
\]

In particular, even with the idealized subpower kernel `kappa=0`, one needs

\[
\boxed{
\eta>\frac8{127}=0.0629921259\ldots .
}
\tag{17}
\]

Conversely, in this exponent bookkeeping, any fixed `eta>8/127` together with `kappa=0` leaves room to choose `vartheta` sufficiently close to but below `73/200` and obtain a polynomial host saving. Thus `8/127` is not merely a rough indication: it is the exact power gap between the unstructured high-shift quartet count and the present Robin target under ideal pointwise phase control.

If the kernel costs `M^lambda`, then `kappa=lambda/2` and (16) becomes

\[
\eta>\frac{8+100\lambda}{127}.
\tag{18}
\]

This makes explicit how pointwise phase cancellation and shifted-energy information can trade against one another, while showing that the shifted side can never be removed completely.

## 4. Bazzanella's fourth-moment split places the obstruction in the high-shift branch

The closest primary precedent remains Danilo Bazzanella, *Prime Numbers in Intervals Starting at a Fixed Power of the Integers* (J. Aust. Math. Soc. **87** (2009), 83--99, DOI `10.1017/S1446788709000020`), already anchored in `SOURCES.md`. Its fourth-moment proof makes essentially the same structural split visible.

For the lower-shift part, Bazzanella uses Kusmin--Landau to obtain a kernel of the form

\[
|S(\Omega)|
\ll
\frac{N^{1/\alpha}}{1+|\Omega|}
\]

through the range `1<=|Omega|<=const*N^(1/alpha)`. The reciprocal shift weight can then be combined with Heath-Brown's four-zero convolution estimate; this is the analogue of **keeping additive-energy information coupled to the shift** rather than replacing all quartets by `N(sigma,T)^4`.

For larger shifts, the paper switches to an exponent-pair pointwise estimate for the sample sum and pays a fourth power of the ordinary zero count. That is exactly the separable architecture abstracted in (3)--(7). `RE-099` does not claim that Bazzanella's theorem contains the Robin-specific `3/8` obstruction: the new point is that after inserting the `RE-095` target and the `RE-098` normalization, even an ideal pointwise replacement for the exponent-pair bound leaves the high-shift branch outside the required interval.

This also explains why sharpening ordinary zero-density estimates off the critical line is not, by itself, the missing ingredient. The floor (9) is already forced by the critical slab, where the total number of zeta zeros up to height `T` is `T^(1+o(1))`. What is missing is information about **how four such ordinates populate translated sum-difference windows**, or an estimate that never destroys the oscillation associated with that translated difference.

## 5. Stress tests and evidence boundary

The first stress test is intentionally overpowered: set `K_hi=X^o(1)`. If the obstruction disappeared under such a hypothesis, it would merely diagnose weak exponential-sum technology. It does not disappear; (9) remains. This proves that pointwise phase cancellation is not the sole resource required by the present fourth-moment architecture.

The second stress test is conceptual. Equations (7)--(18) are **upper-bound method barriers**, not assertions that the actual high-shift contribution has size `T^4` or that the fourth moment cannot be smaller. A signed treatment of the quartet sum, a bilinear/large-sieve estimate coupling `Omega` directly to `S_X(Omega)`, or a shifted-additive-energy theorem can all evade the obstruction. Such an argument would use information explicitly discarded in passing to (4). Therefore this finding does not rule out the fourth-moment route; it rules out only the strategy "prove a better pointwise phase bound and combine it with unstructured quartet counting."

The third stress test is the exact quadratic sample `x(n)=n^2/2`. The same bookkeeping gives the same `3/8` floor for the separable high-shift branch. Hence the obstruction is not a special defect of the CA logarithmic deformation. The deformation matters for proving the eventual coupled estimate, but the need for such coupling is already present in the quadratic control.

No new external theorem is load-bearing beyond the Bazzanella source already recorded in `SOURCES.md`; the remaining exponent calculation is internal to the `RE-095`--`RE-098` framework. No priority claim is made for the general principle that fourth-moment estimates benefit from additive-energy information.

## 6. Research consequence

`RE-098` left three possibilities phrased symmetrically: improve the nonresonant kernel, improve shifted four-zero information, or combine both. `RE-099` removes the first as a standalone route. Within the direct fourth-moment program, the next theorem must retain **joint shifted structure**.

A quantitatively sufficient target can now be stated sharply. In the most optimistic pointwise-kernel regime, prove an effective high-shift quartet saving

\[
Q_{\rm hi}(T)\ll T^{4-\eta+o(1)}
\qquad\text{for some}\qquad
\boxed{\eta>\frac8{127}},
\]

uniformly in the critical beta slab and in the shift ranges relevant to `T=X^(1-vartheta+o(1))`; or prove a weighted estimate for

\[
\sum_{\rho_1,\ldots,\rho_4}
S_X(\gamma_1+\gamma_2-\gamma_3-\gamma_4)
\]

that achieves the same exponent without factoring into a pointwise kernel and an absolute quartet count. The second formulation is likely the more faithful one: it asks directly for the shifted four-zero/oscillatory-kernel coupling that `RE-098` identified, and `RE-099` now shows is not optional.