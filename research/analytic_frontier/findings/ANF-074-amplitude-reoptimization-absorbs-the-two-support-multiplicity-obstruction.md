# ANF-074 — amplitude reoptimization absorbs the two-support multiplicity obstruction

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY-REDUCTION + AMPLITUDE-REOPTIMIZATION + CENTRAL-NOTCH-SURVIVOR + THREE-SUPPORT-FRONTIER`. `ANF-073` shows that the minimum-elementary-slack normalization of the central-notch kernel fails on the real four-point multiset `{0,0,t,t}` as soon as the kernel is negative at a Montgomery--Taylor zero. That failure is genuine at the fixed normalization, but it does **not** kill the underlying central-notch shape after the spectral amplitude is reoptimized. In fact, positivity of the notch spectrum implies something stronger: among all real multisets supported on at most two distinct sites and having no simple points, the equal double/double pattern is already the strongest affine test. The entire two-support multiplicity class therefore reduces to the `D_2` gate isolated in `ANF-073`, and every sufficiently small central notch in the full width range that already survives `ANF-046` passes that gate with strict Montgomery--Taylor room.

Consequently the real-multiplicity continuation requested by `ANF-073` begins at **three distinct support sites**. Unequal multiplicities on two sites cannot repair the four-point obstruction into a shape-level no-go.

## 1. Equal doubles dominate every two-site no-simple multiplicity pattern

Let `F=widehat J` with `J>=0`, put

\[
d:=F(0),
\]

and fix a real `t` with

\[
f:=F(t).
\]

Since `J>=0`, the two-by-two translation Gram matrix

\[
\begin{pmatrix}d&f\\f&d\end{pmatrix}
\]

is positive semidefinite. Hence

\[
\boxed{d\ge0,\qquad f\ge-d.}
\tag{1}
\]

Take a real multiset consisting of `p>=2` copies of `0` and `q>=2` copies of `t`. It has no simple elements. Its ordered energy is

\[
E_{p,q}(t)=d(p^2+q^2)+2pqf,
\tag{2}
\]

so any universal affine certificate

\[
s(Z)\ge A|Z|-E_F(Z)
\]

must obey

\[
A\le \frac{E_{p,q}(t)}{p+q}.
\tag{3}
\]

For the equal-double pattern `p=q=2`, the right side is

\[
2(d+f).
\tag{4}
\]

Subtracting the corresponding numerator for a general pair gives

\[
\begin{aligned}
E_{p,q}(t)-2(d+f)(p+q)
={}&d\bigl[p(p-2)+q(q-2)\bigr]\\
&+2f\bigl[pq-p-q\bigr].
\end{aligned}
\tag{5}
\]

Write `f=-d+g` with `g>=0` by (1). Then (5) becomes the exact sum

\[
\boxed{
E_{p,q}(t)-2(d+f)(p+q)
=d(p-q)^2+2g(pq-p-q).
}
\tag{6}
\]

For `p,q>=2`, one has `pq-p-q=(p-1)(q-1)-1>=0`. Therefore

\[
\boxed{
\frac{E_{p,q}(t)}{p+q}\ge2(d+F(t))
\qquad(p,q\ge2).
}
\tag{7}
\]

Thus no unequal finite multiplicity on two real support sites gives a smaller admissible intercept than `{0,0,t,t}`. The one-support class is similarly minimized by a double point, since `p` coincident copies give `A<=pd` and `p>=2`.

This is a finite-multiplicity statement, not the large-multiplicity copositivity limit of `ANF-005`: the exact integer bookkeeping shows that for positive-spectrum kernels all one- and two-support no-simple real multisets are exhausted by the double-point and equal-double tests.

## 2. The two-support class is exactly the `D_2` normalization gate

For an unscaled shape define

\[
m_{\mathbb R}(F):=\inf_{t\in\mathbb R}F(t),
\qquad
D_2(F):=d+2m_{\mathbb R}(F).
\tag{8}
\]

As derived in `ANF-073`, after scaling `F` by an amplitude `lambda>0` the singleton and equal-double constraints force

\[
\lambda M(F)+\delta_\lambda
\ge
\lambda M(F)+\max\{0,1-\lambda D_2(F)\}.
\tag{9}
\]

When `D_2>0` and `0<=M<D_2`, the right side is minimized at `lambda=D_2^{-1}` and equals

\[
\boxed{\frac{M(F)}{D_2(F)}.}
\tag{10}
\]

Equation (7) shows that, for every positive-spectrum shape, adding *all* two-support no-simple multiplicity patterns leaves (9)--(10) unchanged. There is no hidden stronger `(p,q)` branch behind `ANF-073`.

## 3. Every objective-surviving narrow central notch passes this gate

Use the central-notch notation of `ANF-046`,

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
\beta:=s b_\eta>0,
\]

and

\[
F_s=\widehat J_s,
\qquad
\delta_s=\beta\eta.
\tag{11}
\]

The exact diagonal and pair functional are

\[
d_s=1-\beta\eta,
\tag{12}
\]

and

\[
M(F_s)
=m_{\rm MT}-\beta a(\eta),
\qquad
a(\eta):=1-\eta+\frac{\eta^2}{3}.
\tag{13}
\]

Moreover `R_MT>=0` and the removed sinc-square satisfies `0<=Phi_eta<=b_eta eta`, so `ANF-046` gives the global spatial bound

\[
F_s(t)\ge-\beta\eta
\qquad(t\in\mathbb R).
\tag{14}
\]

Hence

\[
m_{\mathbb R}(F_s)\ge-\beta\eta
\]

and therefore

\[
\boxed{
D_2(F_s)\ge1-3\beta\eta.
}
\tag{15}
\]

Choose `s>0` sufficiently small that `M(F_s)>=0` and `3\beta\eta<1`; this costs nothing in the `ANF-034` separator, whose admissible ray contains arbitrarily small positive `s`. Then

\[
\frac{M(F_s)}{D_2(F_s)}
\le
\frac{m_{\rm MT}-\beta a(\eta)}{1-3\beta\eta}.
\tag{16}
\]

The decisive comparison is exact. Subtract the right side of (16) from `m_MT`:

\[
\boxed{
m_{\rm MT}
-
\frac{m_{\rm MT}-\beta a(\eta)}{1-3\beta\eta}
=
\frac{\beta\,[a(\eta)-3m_{\rm MT}\eta]}{1-3\beta\eta}.
}
\tag{17}
\]

Now use precisely the width range already isolated in `ANF-046`,

\[
0<\eta<3-\sqrt6.
\tag{18}
\]

That condition is equivalent to

\[
a(\eta)-\eta
=1-2\eta+\frac{\eta^2}{3}>0.
\tag{19}
\]

Also the exact Montgomery--Taylor constant satisfies `m_MT<1/3`. Therefore

\[
\boxed{
a(\eta)-3m_{\rm MT}\eta
=
[a(\eta)-\eta]+(1-3m_{\rm MT})\eta
>0.
}
\tag{20}
\]

Equations (16)--(20) prove

\[
\boxed{
\frac{M(F_s)}{D_2(F_s)}<m_{\rm MT}
}
\tag{21}
\]

for every width in the full `ANF-046` objective-surviving interval and all sufficiently small positive amplitudes on the notch ray.

This is stronger than merely checking the explicit `ANF-034` separator widths. `ANF-073` showed that those widths in fact obey `eta<1/5`; the present argument needs only the much larger interval (18). The two-support multiplicity normalization is therefore not close to closing the notch shape.

## 4. Why this does not contradict the fixed-normalization falsifier

`ANF-073` evaluates the unscaled candidate at its minimum elementary slack `delta_s=beta eta` and finds an exact negative slack on `{0,0,z_1,z_1}`. Nothing here reverses that statement. At the original amplitude, the true two-support multiplicity constraint demands more slack than `delta_s` because `F_s(z_1)<0`.

The distinction is that the affine optimization is allowed to rescale the whole spectral shape. The two-support envelope crosses its zero-slack branch at `lambda=D_2(F_s)^{-1}`. Equation (21) says that the corresponding pair-functional cost remains strictly below the Montgomery--Taylor threshold. Thus the fixed intercept dies, while the **shape ray** survives this entire finite multiplicity class.

The worst-case lower bound (15) deliberately forgets where the true minimum of `F_s` occurs. Any sharper lower bound on `m_R(F_s)` only increases `D_2` and improves (21). Determining the exact spatial minimum is therefore unnecessary for deciding the two-support gate.

## 5. Boundary of the result and next decisive test

The conclusion is limited but sharp: every real multiset whose support has at most two distinct sites is now accounted for, including arbitrary finite multiplicities. This does **not** control multisets on three or more distinct real sites. Positive semidefiniteness of the translation Gram does not make their finite-multiplicity affine normalization automatically reducible to pairwise tests, because a nonuniform occupation vector can exploit cancellations among three or more feature vectors even when every two-by-two principal Gram is harmless.

Accordingly, the real-multiplicity branch exposed by `ANF-073` starts at three support sites. The cheapest next gate is to minimize

\[
\frac{\sum_{i,j}k_i k_jF_s(x_i-x_j)}{\sum_i k_i}
\]

over three distinct real sites and integers `k_i>=2`, jointly with the simple-support constraints and amplitude normalization. A proof that the minimum is still generated by uniform doubles would reduce the problem back to the finite-real stability floor of `ANF-017`--`ANF-018`; a certified nonuniform three-site pattern below that envelope would identify the first genuinely new multiplicity obstruction.

## 6. Prior art and evidence boundary

No new external theorem is load-bearing. The positive-type Gram inequality used in (1) is the same Fourier-square structure already canonicalized in `ANF-017`, `ANF-018`, and `ANF-035`; the amplitude objective and `D_2` gate are canonical in `ANF-005` and `ANF-073`. A targeted check of the current positive-type pair-potential/stability literature and current zeta pair-correlation work found the expected general stability and Gram frameworks but no result needed for the elementary finite-integer reduction (6) or the notch comparison (17)--(21). No publication-level novelty claim is made, and `SOURCES.md` needs no new load-bearing anchor.

The result does not restore the failed minimum-slack intercept of `ANF-073`, prove the full real-multiplicity envelope, establish a universal affine certificate, improve the unconditional zeta-zero proportion, or imply RH. It only proves that the first newly exposed multiplicity obstruction is absorbed by amplitude reoptimization throughout the already viable narrow-notch width regime, and that any stronger real-multiplicity falsifier must involve at least three distinct support sites.