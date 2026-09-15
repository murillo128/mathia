# RE-153 — self-tangent counterexamples force a Pareto Chebyshev-deficit barrier

**Status:** `EXACT-DERIVED + CANONICAL-KERNEL-NORMALIZATION + COUNTEREXAMPLE-AVERAGE-BARRIER + SELECTOR-SCOPE-NARROWING + PRIOR-ART-BOUNDED`. `RE-022` proves that every sufficiently large regular self-tangent Robin counterexample must carry at least `2sqrt(2)` normalized mixed Mertens--Chebyshev mass inside a finite annulus. The weight hidden in that mixed integral has a canonical multiplicative scaling law: after normalizing by its total mass, it converges to the Pareto probability density `(1/2)y^(-3/2) dy` on `y>=1`. Consequently the remaining source obstruction can be stated as a scale-invariant average of the square-root Chebyshev deficit, with sharp limiting threshold `sqrt(2)`.

Fix `0<alpha<3/4` and `A>A_0` as in `RE-022`. For a sufficiently large regular self-tangent colossally abundant state `C`, let `p` be its largest active first-layer prime and put

\[
J_p:=[p+p^\alpha,U_A(p)],
\qquad
D(t):=\frac{t-\vartheta(t)}{\sqrt t}.
\tag{1}
\]

With

\[
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\qquad
w_p(t):=\sqrt p\log p\,\sqrt t\,(-h'(t)),
\tag{2}
\]

define

\[
Z_p:=\int_{J_p}w_p(t)\,dt,
\qquad
\nu_p(dt):=\frac{w_p(t)}{Z_p}\mathbf 1_{J_p}(t)\,dt.
\tag{3}
\]

Then `nu_p` is a probability measure for all sufficiently large `p`, and

\[
\boxed{Z_p=2+o(1).}
\tag{4}
\]

Under the multiplicative coordinate `y=t/p`, the push-forward of `nu_p` converges weakly to

\[
\boxed{
\nu_\infty(dy)=\frac12 y^{-3/2}\mathbf 1_{[1,\infty)}(y)\,dy.
}
\tag{5}
\]

Equivalently, for every fixed `B>1`,

\[
\boxed{
\nu_p\bigl([p,Bp]\cap J_p\bigr)
\longrightarrow 1-B^{-1/2},
\qquad
\nu_p\bigl([Bp,U_A(p)]\bigr)
\longrightarrow B^{-1/2}.
}
\tag{6}
\]

In particular the limiting median of the height kernel is `4p`: asymptotically half of the normalized weight lies below `4p` and half above it. By contrast, every additive selector window `[p,p+p^alpha]`, `alpha<1`, carries only `o(1)` of this normalized mass.

Most importantly, along every unbounded sequence of regular self-tangent Robin counterexamples,

\[
\boxed{
\int_{J_p}D(t)\,d\nu_p(t)
\ge \sqrt2-o(1).
}
\tag{7}
\]

Thus a fixed-margin estimate

\[
\int_{J_p}\frac{t-\vartheta(t)}{\sqrt t}\,d\nu_p(t)
\le \sqrt2-\eta
\tag{8}
\]

for some `eta>0` on all sufficiently large eligible self-tangent CA frontier primes would exclude counterexamples on that family. This is an averaged source criterion, not a pointwise Chebyshev bound: the relevant average is forced by the exact Robin kernel itself.

## 1. The Mertens derivative has a universal multiplicative kernel

Write

\[
a(t):=-\log(1-t^{-1}).
\]

Direct differentiation gives

\[
\boxed{
-h'(t)
=
\frac1{t(t-1)\log t}
+
\frac{a(t)}{t(\log t)^2}
>0.
}
\tag{9}
\]

Hence `w_p(t)>0`. Put `t=py`. For every fixed `y>=1`, (9) gives

\[
p\,w_p(py)
\longrightarrow y^{-3/2}.
\tag{10}
\]

Indeed the first term in (9) contributes

\[
\frac{\log p}{\log(py)}
\frac{p}{py-1}\,y^{-1/2}
\longrightarrow y^{-3/2},
\tag{11}
\]

while the second is `O(y^(-3/2)/log p)` for fixed `y`. The same elementary bounds

\[
\frac1t\le a(t)\le\frac1{t-1}
\tag{12}
\]

show, uniformly for `p` sufficiently large and all `y>=1`,

\[
0<p\,w_p(py)\ll y^{-3/2}.
\tag{13}
\]

Since `y^(-3/2)` is integrable on `[1,infinity)`, dominated convergence yields

\[
\int_p^\infty w_p(t)\,dt
=
\int_1^\infty p\,w_p(py)\,dy
\longrightarrow
\int_1^\infty y^{-3/2}\,dy
=2.
\tag{14}
\]

The lower part omitted from `J_p` has length `p^alpha` and `w_p(t)\ll1/p` for `t\asymp p`, so

\[
\int_p^{p+p^\alpha}w_p(t)\,dt
=O(p^{\alpha-1})=o(1).
\tag{15}
\]

For the upper tail, (13) gives the uniform estimate

\[
\int_U^\infty w_p(t)\,dt
\ll \sqrt{\frac pU},
\qquad U\ge p.
\tag{16}
\]

Because `U_A(p)/p -> infinity`, (14)--(16) prove (4).

The same dominated-convergence argument on `[1,B]`, followed by (16), proves weak convergence (5). Integrating the limiting density explicitly gives (6): its tail is `P(Y>=B)=B^(-1/2)`. The appearance of a Pareto law is therefore not a probabilistic model imposed on the primes; it is the deterministic scaling limit of the derivative kernel already present in the exact Mertens splice.

## 2. The deterministic Mertens tax disappears at this scale

`RE-022` uses

\[
I(t)
=
(\vartheta(t)-t)h'(t)-\bigl(h(t)-k(t)\bigr),
\qquad
k(t)=\frac1{t\log t}.
\tag{17}
\]

Since

\[
h(t)-k(t)
=
\frac{-\log(1-t^{-1})-t^{-1}}{\log t},
\tag{18}
\]

the elementary expansion, or the convergent positive series for `-log(1-x)-x`, gives for `t>=2`

\[
0<h(t)-k(t)\ll\frac1{t^2\log t}.
\tag{19}
\]

Therefore the complete normalized tax above `p` obeys

\[
0\le
\sqrt p\log p
\int_p^\infty (h(t)-k(t))\,dt
\ll p^{-1/2}.
\tag{20}
\]

In particular, writing

\[
\tau_p
:=
\sqrt p\log p
\int_{J_p}(h(t)-k(t))\,dt,
\tag{21}
\]

we have

\[
\boxed{0\le\tau_p=o(1).}
\tag{22}
\]

Thus at the first Robin scale the deterministic correction does not alter the normalized source threshold.

## 3. RE-022 becomes a probability-average obstruction

By definition of `D(t)`,

\[
\vartheta(t)-t=-\sqrt t\,D(t).
\tag{23}
\]

Because `h'(t)<0`, equations (2) and (23) give the exact identity

\[
\sqrt p\log p\,(\vartheta(t)-t)h'(t)
=D(t)w_p(t).
\tag{24}
\]

Integrating (17) over `J_p` therefore yields

\[
\boxed{
\sqrt p\log p\int_{J_p}I(t)\,dt
=
Z_p\int_{J_p}D(t)\,d\nu_p(t)-\tau_p.
}
\tag{25}
\]

For every unbounded sequence of regular self-tangent Robin counterexamples, `RE-022` proves

\[
\liminf
\sqrt p\log p\int_{J_p}I(t)\,dt
\ge2\sqrt2.
\tag{26}
\]

Combining (4), (22), (25), and (26) gives

\[
2\int_{J_p}D(t)\,d\nu_p(t)
\ge2\sqrt2-o(1),
\]

which is exactly (7).

This reformulation also keeps the quantifiers honest. It does not claim that `D(t)>=sqrt(2)` pointwise, nor that the endpoint `D(p)` determines the height. A counterexample may pay the required average with uneven positive and negative Chebyshev excursions. What is forced is the single signed average under the canonical measure (3).

## 4. The selector is local, while the height kernel is multiplicatively broad

The accepted clue `CLUE-clean-peak-selector-height-coupling` asks whether the CA selector can control the same signed prime-error source that determines Robin height. `RE-022` already proves that every additive window `[p,p+p^alpha]`, `alpha<3/4`, is negligible for the first normalized height. Equations (5)--(6) make the scale mismatch quantitative and intrinsic to the kernel.

For example,

\[
\nu_p([p,4p]\cap J_p)\to\frac12,
\qquad
\nu_p([4p,U_A(p)])\to\frac12.
\tag{27}
\]

More generally a fixed multiplicative cutoff `Bp` always leaves asymptotic mass `B^(-1/2)` in the future tail. Hence endpoint information or a sublinear additive selector neighborhood can affect only a vanishing fraction of the probability measure relevant to (7). Any successful selector-to-height implication must propagate arithmetic information over multiplicative scales, or exploit cancellation/correlation between those scales; local endpoint control alone cannot cover the canonical height weight.

This is a sharper obstruction than merely saying that the Euler product depends on historical primes. The exact history seen after self-tangent cancellation has a universal asymptotic geometry: on `t/p` it is Pareto with shape parameter `1/2`.

## 5. What this does and does not advance

Equation (7) gives a concrete source-side target that is weaker in form than a pointwise square-root Chebyshev inequality: it asks only for a signed average along the CA-selected frontier primes. It also removes the deterministic `(h-k)` term from the first-order problem and fixes the normalization constant exactly. A proof of (8) with a fixed margin on the relevant selected family would therefore close this particular counterexample channel without separately controlling every `theta(t)-t` in the annulus.

The finding does **not** provide such an unconditional estimate. Standard unconditional PNT remainders are far too large at the square-root normalization on the full annulus, and `RE-009` already warns that global one-sided control of the mixed race is RH-strength. The remaining opportunity is source-specific: exploit the self-tangent CA host to control the Pareto-weighted average (7), rather than trying to infer an entire historical sign from the endpoint selector.

A targeted prior-art scan over Robin/CA criteria, Mertens-product formulations, and Chebyshev-error treatments did not locate this specific normalized-kernel/Pareto formulation. No external theorem is load-bearing here: (4)--(7) follow from elementary calculus plus the already-canonical `RE-022` finite-annulus threshold, so no new `SOURCES.md` anchor is required.

## Research consequence

The unresolved selector-height coupling can now be phrased without the auxiliary Mertens kernels. For eligible self-tangent frontier primes `p`, define the canonical probability measure `nu_p` by (3). The counterexample side requires

\[
\boxed{
\mathbb E_{\nu_p}
\left[\frac{t-\vartheta(t)}{\sqrt t}\right]
\ge\sqrt2-o(1),
}
\tag{28}
\]

while `nu_p`, on multiplicative scale, converges to a fixed Pareto law with median `4p` and tail `B^(-1/2)`. The next useful theorem should therefore control this **selected multiplicative average** directly, or prove a propagation mechanism from CA event geometry into it. Improving only the additive neighborhood of `p` cannot by itself capture a nonvanishing portion of the limiting height kernel.