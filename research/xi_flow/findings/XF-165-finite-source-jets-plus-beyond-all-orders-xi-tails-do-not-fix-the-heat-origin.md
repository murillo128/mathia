---
type: negative
research_line: xi_flow
finding_id: XF-165
status: canonical
---

# XF-165 — Finite source jets plus beyond-all-orders Xi tails do not fix the heat origin

**Confidence:** high. The multiplier below is explicit, strictly positive on the real axis and real analytic; it preserves any prescribed finite bank of Xi source jets exactly, agrees with Xi at `+infinity` beyond every fixed theta-exponential scale, and remains dominated by the Xi source. A two-parameter dominated-convergence limit makes its bounded heat orbit approach a negative-time Xi slice, after which Rouché transfers a nonreal zero to `t=0`. The only external Xi fact used is the established Rodgers--Tao bound `Lambda_Xi >= 0`, already anchored in `SOURCES.md`.

## Statement

XF-163 showed that tail invariants which are blind to the Gaussian tilt `rho(u) -> e^{-tau u^2}rho(u)` cannot control the absolute heat origin. XF-164 strengthened this by showing that even beyond-all-orders agreement with the Xi tail does not repair the problem. One apparent escape remained: anchor the heat origin by adding finitely many **gauge-sensitive local source data**, such as `(log Phi)''(0)`, while retaining the exact Xi tail asymptotics.

That escape also fails for every fixed finite amount of local data.

Fix `tau>0`. Let

\[
A=\{a_1,\ldots,a_s\}\subset[0,\infty)
\tag{1}
\]

be any finite set of source locations, and prescribe finite jet orders `J_1,...,J_s`. Choose integers `m_i>=1` such that

\[
2m_i>J_i.
\tag{2}
\]

For `delta>0`, define the even real-analytic notch factors

\[
G_{i,\delta}(u)=
\begin{cases}
\bigl(1-e^{-u^2/\delta^2}\bigr)^{m_i}, & a_i=0,\\[4pt]
\bigl(1-e^{-(u-a_i)^2/\delta^2}\bigr)^{m_i}
\bigl(1-e^{-(u+a_i)^2/\delta^2}\bigr)^{m_i}, & a_i>0,
\end{cases}
\tag{3}
\]

and

\[
G_\delta(u):=\prod_{i=1}^sG_{i,\delta}(u).
\tag{4}
\]

As in XF-164, let

\[
w_R(u):=\exp\!\bigl(-\exp(u^2-R^2)\bigr),
\tag{5}
\]

and set

\[
q_{\tau,\delta,R}(u)
:=\exp\!\bigl(-\tau u^2w_R(u)G_\delta(u)\bigr),
\qquad
\boxed{
\rho_{\tau,\delta,R}(u):=\Phi(u)q_{\tau,\delta,R}(u).
}
\tag{6}
\]

Then:

1. `rho_{tau,delta,R}` is strictly positive and real analytic on the real axis and obeys

\[
e^{-\tau u^2}\Phi(u)
\le \rho_{\tau,\delta,R}(u)
\le \Phi(u).
\tag{7}
\]

Hence every finite positive heat time remains admissible.

2. At every prescribed location `a_i`, the Xi jet is matched **exactly** through the requested order:

\[
\boxed{
\rho_{\tau,\delta,R}^{(j)}(a_i)=\Phi^{(j)}(a_i)
\qquad(0\le j\le J_i).
}
\tag{8}
\]

The same conclusion holds for the logarithmic jets wherever `Phi>0`.

3. For every fixed `delta,R`, every fixed derivative order `j>=0`, and every `c>0`,

\[
\boxed{
 e^{c e^{4u}}
 \frac{d^j}{du^j}
 \bigl(\log\rho_{\tau,\delta,R}(u)-\log\Phi(u)\bigr)
 \longrightarrow0
 \qquad(u\to+\infty).
}
\tag{9}
\]

Thus the perturbation remains invisible beyond every fixed Xi theta-tail scale exactly as in XF-164.

4. Fix the finite jet bank `(1)--(2)` and `tau`. Along any choice `delta_n->0`, `R_n->infinity`, the associated heat transforms

\[
\mathcal H_t^{(n)}(z)
:=\int_0^\infty e^{tu^2}
\rho_{\tau,\delta_n,R_n}(u)\cos(zu)\,du
\tag{10}
\]

satisfy

\[
\boxed{
\mathcal H_t^{(n)}(z)\longrightarrow H_{t-\tau}(z)
}
\tag{11}
\]

locally uniformly for real `t` and complex `z` on every compact spacetime set.

5. Since `Lambda_Xi>=0`, `H_{-tau}` has a nonreal zero. Therefore, for all sufficiently small `delta` and sufficiently large `R` along the above limit,

\[
\boxed{
\mathcal H_0^{(\tau,\delta,R)}
\text{ has a nonreal zero,}
}
\tag{12}
\]

while `(7)--(9)` still hold.

Consequently **no criterion consisting of an arbitrarily accurate asymptotic Xi tail plus any fixed finite collection of exact local source jets can force the distinguished `t=0` slice to be real-rooted**. The source datum that fixes the Xi heat origin must be genuinely global/infinite-dimensional, or an exact identity that couples separated source scales in a way finite local interpolation cannot preserve.

## 1. Analytic notches preserve any prescribed finite source-jet bank

For real `u`, every factor in `(3)` lies in `[0,1)`, so

\[
0\le G_\delta(u)\le1,
\qquad
0<w_R(u)<1.
\tag{13}
\]

This gives

\[
-\tau u^2
\le -\tau u^2w_R(u)G_\delta(u)\le0,
\tag{14}
\]

and hence `(7)`. The factors in `(3)` are real analytic and the product is even; therefore the multiplier in `(6)` preserves the usual even real source symmetry as well as positivity.

Now fix a prescribed point `a_i>0`. Near `u=a_i`,

\[
1-e^{-(u-a_i)^2/\delta^2}
=\frac{(u-a_i)^2}{\delta^2}
+O((u-a_i)^4),
\tag{15}
\]

so

\[
G_\delta(u)=O((u-a_i)^{2m_i}).
\tag{16}
\]

The remaining factors, including the paired `-a_i` notch, are analytic and bounded there. Since `u^2w_R(u)` is analytic,

\[
\log q_{\tau,\delta,R}(u)
=O((u-a_i)^{2m_i}),
\tag{17}
\]

and therefore

\[
q_{\tau,\delta,R}(u)=1+O((u-a_i)^{2m_i}).
\tag{18}
\]

Because `2m_i>J_i`, multiplying by `Phi` proves `(8)`.

At `a_i=0`, the extra factor `u^2` in `(6)` only improves the order: the zero in `(3)` gives

\[
\log q_{\tau,\delta,R}(u)=O(u^{2m_i+2}).
\tag{19}
\]

Thus `(8)` also holds there. Since `Phi` is positive on the real source axis, equality of the multiplicative jet implies equality of the corresponding finite logarithmic jet as well.

The important quantifier is finite-but-arbitrary: for every finite set of locations and every finite list of requested orders, one first fixes suitable `m_i` and then constructs the source. This does **not** produce one non-Xi analytic source agreeing with the complete infinite jet at a point; analytic identity would forbid that.

## 2. The notches disappear in measure while the soft tail splice remains invisible

For each fixed real `u` not belonging to the finite set `A` or its reflected copy, as `delta->0`,

\[
G_\delta(u)\longrightarrow1.
\tag{20}
\]

At the finitely many notched points the limit differs, but those points have Lebesgue measure zero. For every fixed `u`, as `R->infinity`,

\[
w_R(u)\longrightarrow1.
\tag{21}
\]

Hence along `delta_n->0`, `R_n->infinity`,

\[
q_{\tau,\delta_n,R_n}(u)
\longrightarrow e^{-\tau u^2}
\tag{22}
\]

for almost every `u>=0`.

At the opposite end, for fixed `delta,R`,

\[
\log\rho_{\tau,\delta,R}(u)-\log\Phi(u)
=-\tau u^2e^{-e^{u^2-R^2}}G_\delta(u).
\tag{23}
\]

The factors `G_delta` and all their fixed-order derivatives grow at most polynomially times ordinary Gaussian exponentials and in fact approach `1` with Gaussian errors. Differentiating `w_R` contributes finite sums of powers of `u` and `e^{u^2-R^2}`, always multiplied by `e^{-e^{u^2-R^2}}`. Therefore, for every fixed `j`, the logarithm of the absolute value of the `j`th derivative in `(23)` is bounded above by

\[
-e^{u^2-R^2}+O_j(u^2).
\tag{24}
\]

Since `e^{u^2-R^2}` dominates `e^{4u}` as `u->infinity`, `(9)` follows for every fixed `c>0`.

Thus the construction independently hides the perturbation at the two places a finite descriptor might inspect: it is exactly flat to prescribed finite orders at finitely many source points, while it is beyond-all-fixed-theta-scales small in the far tail. The change is forced into the unsampled mesoscopic source region.

## 3. The bounded heat orbit still converges to the negative-time Xi slice

Let `I` be a compact real interval of heat times and `K` a compact subset of `C`. Put

\[
T:=\max I,
\qquad
Y:=\max_{z\in K}|\operatorname{Im}z|.
\tag{25}
\]

By `(7)`, both `q_{tau,delta,R}` and `e^{-tau u^2}` lie between zero and one. Hence for `t in I`, `z in K`,

\[
\begin{aligned}
&\left|e^{tu^2}\Phi(u)
\bigl(q_{\tau,\delta,R}(u)-e^{-\tau u^2}\bigr)
\cos(zu)\right|\\
&\hspace{3em}\le
2\Phi(u)e^{Tu^2+Yu}.
\end{aligned}
\tag{26}
\]

The right side is integrable because the Xi source has double-exponential decay; equivalently, XF-162 already established all finite positive quadratic moments. Combining the almost-everywhere convergence `(22)` with dominated convergence yields

\[
\sup_{t\in I}\sup_{z\in K}
\left|
\mathcal H_t^{(n)}(z)-H_{t-\tau}(z)
\right|
\longrightarrow0.
\tag{27}
\]

The finite exact jet constraints therefore cost nothing at the level of bounded-spacetime heat-orbit approximation: their transition layers can be squeezed into sets of vanishing measure while the transform sees only their vanishing integral contribution.

This point is stronger than merely defeating `(log Phi)''(0)`. Any **finite-dimensional local sampling scheme on the source**, with arbitrarily high but finite derivative order at finitely many fixed real locations, can be made exactly Xi while the transform converges to a time-shifted Xi orbit.

## 4. A nonreal zero survives all finite local anchors

Fix `tau>0`. The established Rodgers--Tao lower bound gives

\[
-\tau<\Lambda_{\rm Xi}.
\tag{28}
\]

By the defining de Bruijn--Newman dichotomy, `H_{-tau}` has at least one nonreal zero `z_tau`. Choose a closed disk `D_tau` around such a zero whose closure misses the real axis and whose boundary contains no zero of `H_{-tau}`. Then

\[
m_\tau:=\min_{z\in\partial D_\tau}|H_{-\tau}(z)|>0.
\tag{29}
\]

Apply `(27)` at `t=0` and `K=partial D_tau`. For all sufficiently large `n`,

\[
\sup_{z\in\partial D_\tau}
|\mathcal H_0^{(n)}(z)-H_{-\tau}(z)|<m_\tau.
\tag{30}
\]

Rouché's theorem gives the same number of zeros, counted with multiplicity, inside `D_tau`; hence `mathcal H_0^(n)` has a nonreal zero. No simplicity assumption on `z_tau` is needed.

Because every member of the sequence was constructed with the exact jet identities `(8)` and the tail property `(9)`, this proves `(12)` without weakening either source constraint.

## Relation to prior findings

XF-162 found a genuine Xi-specific discriminator for the then-current maximal-contact controls: the normalized theta-tail hazard. XF-163 showed that the hazard cannot locate the absolute transition because Gaussian source tilting translates the heat origin while preserving the tail jet. XF-164 then showed that replacing that finite tail jet by arbitrarily detailed asymptotic tail information still does not suffice.

XF-165 closes the most immediate local repair of that negative result. Gauge-sensitive quantities such as `(log Phi)''(0)` do detect the literal Gaussian tilt, but **any finite collection of such local quantities can be pinned exactly to its Xi value by analytic notches of vanishing width**. At the same time the transform remains arbitrarily close, on every bounded spacetime window, to the shifted Xi orbit.

The durable obstruction is therefore no longer merely `tail-only`. It is **finite-dimensional source summarization**: separated finite local jets plus arbitrarily strong asymptotic tail agreement still leave enough mesoscopic freedom to move the observed zero geometry.

## Prior-art and novelty audit

The de Bruijn--Newman heat deformation and the Rodgers--Tao theorem `Lambda_Xi>=0` are classical and already anchored in `SOURCES.md`; Rouché stability and analytic interpolation by functions with prescribed finite-order zeros are standard complex-analysis ingredients. A targeted literature search for Xi-kernel perturbations preserving prescribed finite source jets together with beyond-all-orders tail agreement did not locate a theorem stating the specific conclusion above. Recent work on shape properties of the Xi kernel, including log-concavity, studies exact global inequalities of the true kernel rather than this finite-jet perturbative non-identifiability problem.

The derived contribution here is narrow: the explicit notch-times-soft-splice construction `(3)--(6)`, its simultaneous exact finite-jet and beyond-all-orders tail preservation, and the resulting Rouché transfer of negative-time Xi zero geometry. No newly found external theorem is load-bearing, so `SOURCES.md` requires no update.

## Falsification boundary

This finding does **not** preserve an infinite Taylor jet of Xi at any point. For a real-analytic source, equality of a complete analytic germ would determine the source on the connected domain. It also does not preserve an exact open-interval identity with Xi in the tail, for the same identity-theorem reason.

It does **not** show that every finite-dimensional functional of the source is noncoercive. The construction directly covers finitely many pointwise derivative jets plus asymptotic tail data; nonlocal functionals such as exact moments or modular transforms may couple the transition layers and could detect the perturbation.

It also does not assign or compute a de Bruijn--Newman constant for the modified source. The proved target statement is only the existence of a nonreal zero at the distinguished `t=0` slice, inherited by locally uniform convergence from `H_{-tau}`.

Finally, this is not a construction of a second theta kernel and does not challenge any exact identity of the actual Xi source. Its role is to falsify a class of candidate proof strategies that try to compress the necessary source rigidity into finitely many local anchors plus arbitrarily accurate tail asymptotics.

## Consequence for `xi_flow`

The next source-side gate should require a constraint that cannot be satisfied by finite local interpolation. The most promising logical forms are an **exact global theta/modular identity**, an infinite coupled coefficient law, or a nonlocal transform identity tying the mesoscopic mass directly to both the core and the tail. Such a candidate must fail on the Gaussian tilt of XF-163, the tail splice of XF-164, and the finite-jet notched splice `(6)`.

Conversely, adding more point samples, more derivatives at fixed source locations, or more asymptotic tail coefficients is now a provably non-closing direction as long as their number remains fixed. The next gate is to identify and test one genuinely global Xi identity against these counterexamples rather than further enriching a finite descriptor.