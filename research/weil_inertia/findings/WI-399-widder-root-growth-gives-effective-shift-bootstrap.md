# WI-399 — Widder root growth gives an exact effective-shift defect bootstrap

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SHARP-STRUCTURAL-BARRIER + PRIOR-ART-REDIRECT + BOOTSTRAP-INTERFACE`.

**Parent findings:** WI-393, WI-395, WI-398.

## Claim

A recent non-peer-reviewed preprint of Zeraoulia Rafik introduces a fixed-height high-order Widder hierarchy for

\[
G(x)=\xi\!\left(\frac12+\sqrt x\right),
\qquad
F_\xi(x)=2\frac{G'(x)}{G(x)},
\]

and proves an RH-equivalent prime-side root-growth criterion. This is materially different from the density-normalized moving-carrier interfaces of WI-393--WI-398: a single off-critical zero already produces an exponentially growing high-order mode at a suitable fixed height.

The preprint also proves, by an optimized absolute-convergence contour shift, that for every fixed `T>=2`

\[
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}
\le
\mathcal M(T)
:=
\frac{2}{1+\sqrt{1-T^{-2}}}.
\tag{1}
\]

The exact synthesis below identifies why that bound cannot itself start an RH proof. For a hypothetical zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad 0<|\delta|<\frac12,
\]

put

\[
w_\rho=(\gamma-i\delta)^2
\]

and define its one-zero Widder root amplification at scale `T` by

\[
R_{\delta,\gamma}(T)
:=
4T^2\frac{|w_\rho|}{|T^2+w_\rho|^2}.
\tag{2}
\]

Then for every `T>=2`

\[
\boxed{
\mathcal M(T)
=
\sup_{|\delta|<1/2}\sup_{\gamma>0} R_{\delta,\gamma}(T).
}
\tag{3}
\]

More strongly, if

\[
M(\sigma):=
\frac{2}{1+\sqrt{1-4\sigma^2}},
\qquad 0\le\sigma<\frac12,
\tag{4}
\]

then

\[
\boxed{
R_{\delta,\gamma}(T)
\le M(|\delta|/T)
< M(1/(2T))=\mathcal M(T).
}
\tag{5}
\]

The first inequality is sharp for every fixed depth `|delta|`: the maximizing ordinate is explicit. Thus the optimized **absolute** prime-side root bound is exactly the strip-edge envelope of the **single-zero** signal. The same rational saddle appears on both sides; the agreement is not merely an asymptotic exponent comparison.

There is also an exact conditional bootstrap interface. Fix `0<=a<1/2`. Suppose one could prove, for every sufficiently large fixed `T`, the stronger signed-prime estimate

\[
\boxed{
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}
\le M(a/T).
}
\tag{6}
\]

Then every sufficiently high nontrivial zero would satisfy

\[
\boxed{
|\Re\rho-1/2|\le a.
}
\tag{7}
\]

Hence a genuine reduction of the effective contour width from `1/2` to `a` yields exactly the corresponding zero-free horizontal strip. At the endpoint `a=1/2`, (6) is precisely the absolute-convergence bound (1), so it yields only the already-known critical strip. At `a=0`, (6) becomes the RH root threshold `1`.

This is a credible defect-to-zero *interface*, not yet a bootstrap theorem: no mechanism is presently known that turns the narrower zero strip (7) back into a still smaller effective prime width. What it does prove is that the recent Widder hierarchy has the right individual-defect sensitivity, while also locating a sharp arithmetic gate: further progress requires signed cancellation/analytic continuation that beats the absolute-convergence width `1/2`.

No improved simple-critical-zero proportion and no proof of RH is claimed.

## 1. Primary-source interface: an individual off-line zero is visible

The primary source is Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026. It is explicitly non-peer-reviewed.

The source uses the genus-zero product for `G`. For a zero `rho=1/2+delta+i gamma`, the reflected parameter is

\[
w_\rho=-(\delta+i\gamma)^2=(\gamma-i\delta)^2.
\tag{8}
\]

Critical-line zeros have `delta=0`, hence `w_rho>0`; an off-line functional-equation pair gives nonreal conjugate reflected parameters.

For fixed `T`, Proposition A1 of the preprint defines

\[
\mathcal R(T)
:=
4T^2\max_\rho
\left|
\frac{w_\rho}{(T^2+w_\rho)^2}
\right|
\tag{9}
\]

and proves

\[
\limsup_{m\to\infty}
|T^2A'_m(T^2)|^{1/m}
=\mathcal R(T).
\tag{10}
\]

Under RH, `mathcal R(T)<=1` for every `T`; if RH is false, it exceeds one on a nonempty open interval. Lemma A1 gives the exact explicit-formula relation

\[
2T^2A'_m(T^2)=\mathcal H_m(T)-\mathcal P_m(T),
\qquad
\sup_m|\mathcal H_m(T)|<\infty,
\tag{11}
\]

and Theorem A2 concludes

\[
\boxed{
\mathrm{RH}
\iff
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}\le1
\quad\text{for every fixed }T\ge2.
}
\tag{12}
\]

Thus, unlike a density-only statistic, this hierarchy cannot hide a finite or zero-density collection of off-line zeros: any one of them creates a fixed-`T` root rate greater than one after suitable tuning. Corollary A2 makes this even more explicit by choosing

\[
T_\rho=\sqrt{\gamma^2+\delta^2},
\qquad
z_\rho=\frac{\gamma^2}{\gamma^2+\delta^2},
\]

for which the corresponding normalized zero factor is

\[
R_{\delta,\gamma}(T_\rho)=z_\rho^{-1}
=1+\frac{\delta^2}{\gamma^2}>1.
\tag{13}
\]

This individual-defect sensitivity is the main reason the preprint materially redirects the line despite not improving Mathia's current simple-critical-zero percentage.

## 2. Exact kernel identity: the prime saddle is the zero saddle

Set

\[
y=\frac\gamma T,
\qquad
\sigma=\frac{|\delta|}{T}.
\tag{14}
\]

Since

\[
|w_\rho|=\gamma^2+\delta^2
=T^2(y^2+\sigma^2)
\]

and

\[
|T^2+w_\rho|^2
=T^4\left[(1+y^2-\sigma^2)^2+4y^2\sigma^2\right],
\]

equation (2) becomes the exact rational identity

\[
\boxed{
R_{\delta,\gamma}(T)
=
\frac{4(y^2+\sigma^2)}
{(1+y^2-\sigma^2)^2+4y^2\sigma^2}.
}
\tag{15}
\]

But the right-hand side is **exactly** the shifted beta-kernel factor called `mathcal R_sigma(y)` in Lemma 5 and Proposition A2 of Rafik's preprint. The source independently maximizes that function while estimating the shifted Fourier kernel and obtains

\[
\sup_{y\in\mathbb R}\mathcal R_\sigma(y)
=M(\sigma)
=\frac{2}{1+\sqrt{1-4\sigma^2}}.
\tag{16}
\]

For the zeta application `T>=2` and `|delta|<1/2`, so `sigma<1/4`, safely inside the range of the source's saddle calculation. Equations (15)--(16) prove the first inequality in (5). The function `M(sigma)` is strictly increasing for `sigma>0`, and the critical strip gives

\[
\sigma=\frac{|\delta|}{T}<\frac1{2T},
\]

which proves the strict second inequality in (5).

Conversely, for every fixed `sigma<1/4`, the source's maximizer is real and positive, with

\[
y_\sigma^2+\sigma^2=\sqrt{1-4\sigma^2}.
\tag{17}
\]

Therefore the first inequality in (5) is sharp as a geometric one-zero envelope. Sending `|delta|` upward to the open strip edge `1/2` yields

\[
\sup_{|\delta|<1/2,\gamma>0}R_{\delta,\gamma}(T)
=M(1/(2T))
=\mathcal M(T),
\]

which proves (3).

The significance is not that the actual zeta zero set attains this supremum. It need not. The point is sharper: Proposition A2's optimized absolute prime estimate and the most adverse single-zero geometry are controlled by the **same extremal rational function**. Any argument that only retains this absolute shifted-kernel norm is already saturated at the boundary allowed by the critical strip.

## 3. Effective-shift theorem

Assume (6) for a fixed `a<1/2`, and suppose for contradiction that there is a sufficiently high zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad |\delta|>a.
\]

Write

\[
r:=\gamma^2+\delta^2.
\]

Choose `T` by

\[
\boxed{
T^2=2\delta^2+\sqrt{r^2+4\delta^4}.
}
\tag{18}
\]

For a nontrivial zeta zero this `T` is certainly larger than two once the ordinate is in the asserted sufficiently-high range. Equation (18) is equivalent to

\[
\frac{r}{T^2}
=
\sqrt{1-rac{4\delta^2}{T^2}},
\tag{19}
\]

which is precisely the saddle condition (17) with `sigma=|delta|/T` and `y=gamma/T`. Hence this one zero contributes

\[
R_{\delta,\gamma}(T)=M(|\delta|/T).
\tag{20}
\]

Because `|delta|>a` and `M` is strictly increasing,

\[
R_{\delta,\gamma}(T)>M(a/T)>1.
\tag{21}
\]

Therefore the global zero-side spectral radius in (9) satisfies

\[
\mathcal R(T)>M(a/T)>1.
\tag{22}
\]

Equation (11) now transfers this root rate to the prime side without any uniqueness hypothesis. Indeed, if

\[
\limsup|T^2A'_m(T^2)|^{1/m}=\mathcal R(T)>1
\]

and `mathcal H_m(T)` is bounded, then

\[
\boxed{
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}
=\mathcal R(T).
}
\tag{23}
\]

The upper bound follows from the triangle inequality in (11), and the reverse inequality follows along a subsequence attaining the limsup because the bounded `mathcal H_m(T)` has root rate at most one. Equations (22)--(23) contradict (6). This proves (7).

Thus `a` has a literal interpretation as an **effective horizontal width** purchased by the prime-side estimate. The existing no-cancellation contour argument has effective width `a=1/2`; a source theorem with any fixed `a<1/2` would already prove a strictly narrower zero strip, and `a=0` would prove RH.

## 4. Quadratic-coefficient form of the same gate

For fixed `a`,

\[
M(a/T)
=1+\frac{a^2}{T^2}+O_a(T^{-4}).
\tag{24}
\]

Consequently the absolute-convergence endpoint has

\[
\mathcal M(T)
=1+\frac{1}{4T^2}+O(T^{-4}),
\tag{25}
\]

and the coefficient `1/4` is exactly the square of the critical-strip half-width.

A weaker asymptotic source theorem can therefore still have geometric content. If, for some fixed `c<1/4`, one proves uniformly for all sufficiently large fixed `T`

\[
\limsup_{m\to\infty}|\mathcal P_m(T)|^{1/m}
\le
1+\frac{c+o(1)}{T^2},
\tag{26}
\]

then any fixed-depth family of zeros with

\[
|\delta|>\sqrt c+\varepsilon
\]

is excluded at sufficiently large ordinate by tuning `T` to the saddle (18). This is the asymptotic version of the exact effective-width theorem.

This does **not** rule out zeros whose horizontal depth tends to zero. In particular, merely improving the coefficient from `1/4` to a positive `c` is a strict zero-free-strip advance, not RH. Reaching all the way to root threshold one, or producing an iterative theorem that forces the effective width to contract repeatedly, remains necessary for defect elimination.

## 5. Relationship to WI-393--WI-398

WI-393--WI-398 identify a square-root-prime obstruction for moving-carrier Weil tests. Jutila zero density then shows that the density-normalized horizontal signal of scalar and matrix Fourier observables is suppressed near the critical line; positive-density detection requires a growing arithmetic budget or collapsing spectral margin.

The Widder hierarchy avoids that particular weakness. It does not average the exceptional population before detecting it. High order `m` exponentially amplifies the phase of one nonreal reflected parameter, so even one off-line pair produces `mathcal R(T)>1` at a suitable fixed `T`. This is exactly the type of finite/zero-density sensitivity demanded by the canonical RH objective.

The price is that the arithmetic obstruction reappears in a sharper form. The shifted beta-kernel needed to control the prime functional has the same saddle (15) as the one-zero defect itself. Absolute convergence of

\[
\sum_{n\ge2}\Lambda(n)n^{-1/2-a}
\]

requires `a>1/2`; letting `a` decrease to its endpoint produces precisely the strip-edge factor `M(1/(2T))`. Thus the `1/2` boundary is not an accidental constant in the proof: it is simultaneously the Dirichlet-series absolute-convergence threshold and the maximal horizontal depth permitted to a zeta zero.

This gives a cleaner target than simply increasing the Widder order. A useful theorem must beat the endpoint **arithmetically**, through signed prime cancellation or controlled analytic continuation of `-zeta'/zeta`, enough to replace the effective width `1/2` by a smaller width. The exact theorem above then converts that arithmetic gain directly into horizontal zero exclusion.

## 6. Prior art and novelty boundary

The finite Stieltjes/Widder framework is classical. Lennart Bondesson and Thomas Simon, *Stieltjes functions of finite order and hyperbolic monotonicity*, Trans. Amer. Math. Soc. 370 (2018), 8279--8314, arXiv:`1604.05267`, develops the finite Stieltjes classes and Widder derivative conditions used by Rafik. Recent 2026 preprints of Nicholas G. Polson develop related Thorin/GGC, Stieltjes, reciprocal-xi, and zero-measure formulations of RH. Those works make clear that Stieltjes/Thorin positivity for xi is not itself a new mechanism.

Rafik's 17 September 2026 preprint is the direct prior art for the beta--Widder hierarchy used here. In particular, Proposition A1 gives the zero-side spectral radius, Theorem A2 gives the prime root-growth RH criterion, Proposition A2 gives the optimized absolute bound (1), the generating-function appendix identifies the inaccessible terminal annulus, and Corollary A2 gives the real pole associated with an individual off-critical zero. Those statements are attributed to the preprint and are not claimed by Mathia.

The additional Mathia deduction is the exact identification (15): the shifted-prime `L^1` saddle function in Rafik's Lemma 5 is literally the normalized one-zero amplification function after `y=gamma/T`, `sigma=|delta|/T`. This yields the sharp strip-envelope identity (3) and the effective-shift implication (6)--(7). A prior-art search across Widder/Stieltjes xi criteria, recent Thorin formulations, and the source preprint located no explicit statement of this exact width-to-depth theorem. That search absence is **not** a priority claim.

The source's separate Schur--triple computer-assisted simple-zero value `0.672625773769468...` is below the current established Mathia bound and is not imported as progress. The present finding uses only the analytic fixed-`T` Widder/explicit-formula interfaces stated above; the preprint's non-peer-reviewed status is retained in the evidence label.

## Decisive audit tests

The finding reduces to four exact checks:

1. verify the reflected-zero coordinate `w_rho=(gamma-i delta)^2` and the source's Proposition A1 normalization `4T^2|w/(T^2+w)^2|`;
2. substitute `y=gamma/T`, `sigma=|delta|/T` and verify that the result is exactly the source's shifted beta-kernel factor `mathcal R_sigma(y)`;
3. verify its one-variable maximum (16), including strict monotonicity of `M(sigma)` and the endpoint identity `M(1/(2T))=mathcal M(T)`;
4. for the effective-shift implication, verify that (18) enforces the saddle condition and that boundedness of `mathcal H_m(T)` transfers every zero-side root rate strictly above one to the same prime-side root rate.

Failure of any of these four interfaces invalidates the new synthesis. No numerical certificate is involved.

## Research consequence

This materially redirects the individual-defect program. The Widder hierarchy supplies an exact detector that does not lose finite or zero-density off-line exceptions, so it escapes the specific population-averaging obstruction behind WI-396--WI-398. But it also comes with a sharp no-go: the optimized absolute prime estimate is exactly the critical-strip one-zero envelope and therefore cannot narrow the strip at all.

The live arithmetic target is now precise. Prove a signed prime root-growth estimate with an effective width `a<1/2`; that would immediately give a stricter zero-free strip. Better still, find a source theorem in which the resulting narrower strip feeds back into a smaller effective width and iterates toward `a=0`. Without such signed cancellation or feedback, the new hierarchy is an RH-equivalent detector rather than an RH proof.