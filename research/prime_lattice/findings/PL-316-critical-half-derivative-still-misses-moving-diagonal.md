# PL-316 — Critical zero-extension `H^{1/2}` still misses the moving Green diagonal

**Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE/ROUTE-NARROWING`

**Status:** `H00-HALF-INSUFFICIENT + ARBITRARILY-SMALL-CRITICAL-NORM + ACTUAL-BRANCH-TAIL-CONTROL-OPEN`

## Precise claim

The sparse moving-diagonal mismatch constructed in `PL-314` and strengthened in `PL-315` can be chosen so that its physical pullback, extended by zero outside `(-1,1)`, lies in the critical zero-extension Sobolev class `H^{1/2}(R)`. Its `H^{1/2}(R)` norm can moreover be made arbitrarily small, while along the selected scales `s_n -> 0` the normalized Green transfer still has the same order-one lower bound from `PL-315`.

More precisely, fix `r>0` and the `PL-315` bump family

\[
m(Q)=\sum_{n\ge1}s_n\chi\!\left(\frac{s_nQ-r}{\delta_n}\right),
\qquad
Q>0,
\tag{PL316-1}
\]

with pairwise disjoint supports, `delta_n<min{r/4,1/2}`, summable `delta_n`, and the strengthened scale choice

\[
s_n\le \frac{\varepsilon 2^{-n-2}}{1+\|\chi'\|_{L^1}},
\qquad
s_n\le2^{-n}\delta_n^n.
\tag{PL316-2}
\]

Let

\[
Q(x)=-\log\frac{1-x}{2},
\qquad
f(x)=m(Q(x)),\quad -1<x<1,
\tag{PL316-3}
\]

and let `Ef` denote the zero extension of `f` to `R`. Then

\[
\boxed{Ef\in H^{1/2}(\mathbb R).}
\tag{PL316-4}
\]

By decreasing the admissible `s_n` further, while keeping the fixed `delta_n` and the Green-mass lower bounds used in `PL-315`, one may impose

\[
\boxed{\|Ef\|_{H^{1/2}(\mathbb R)}<\eta}
\tag{PL316-5}
\]

for any prescribed `eta>0`. Nevertheless the same fixed mismatch satisfies, along those same selected scales,

\[
\boxed{
\mathcal A_{s_n}[m](r)\ge \frac34e^{-2r},
}
\tag{PL316-6}
\]

while the rank-one candidate `e^{-r}\int_0^\infty m(Q)dQ` can be kept below `e^{-2r}/4` by the original choice of the summable `delta_n`.

Thus **critical zero-extension half-derivative regularity does not imply the moving-tail suppression needed by `PL-314`**. In particular, membership in the Lions--Magenes-type critical zero-extension class does not force `Qm(Q)->0` and does not justify the rank-one corner reduction.

## 1. Exact critical Gagliardo kernel in logarithmic endpoint coordinates

Write

\[
x(Q)=1-2e^{-Q},
\qquad
\frac{dx}{dQ}=2e^{-Q}.
\]

For `Q,P>0`,

\[
|x(Q)-x(P)|=2|e^{-Q}-e^{-P}|,
\]

hence the interior critical Gagliardo measure transforms exactly as

\[
\frac{dx\,dy}{|x-y|^2}
=
\frac{e^{-Q-P}}{(e^{-Q}-e^{-P})^2}\,dQ\,dP
=
\frac{dQ\,dP}{4\sinh^2((Q-P)/2)}.
\tag{PL316-7}
\]

Since `sinh(|h|/2)>=|h|/2`,

\[
\frac1{4\sinh^2(h/2)}\le\frac1{h^2}.
\tag{PL316-8}
\]

Therefore

\[
[f]_{H^{1/2}(-1,1)}
\le [m]_{\dot H^{1/2}(\mathbb R_Q)},
\tag{PL316-9}
\]

where `m` is extended by zero to `Q<0`; the first bump can be placed away from `Q=0`, as in `PL-315`.

For a single packet

\[
m_n(Q)=s_n\chi\!\left(\frac{Q-Q_n}{L_n}\right),
\qquad
Q_n=\frac r{s_n},
\qquad
L_n=\frac{\delta_n}{s_n},
\tag{PL316-10}
\]

the one-dimensional critical scaling is exact:

\[
[m_n]_{\dot H^{1/2}(\mathbb R)}
=s_n[\chi]_{\dot H^{1/2}(\mathbb R)}.
\tag{PL316-11}
\]

The seminorm is a Hilbert seminorm, so

\[
[m]_{\dot H^{1/2}}
\le [\chi]_{\dot H^{1/2}}\sum_ns_n<\infty.
\tag{PL316-12}
\]

The same estimate shows that this interior contribution can be made arbitrarily small because the Green-mass selection permits each `s_n` to be decreased after `delta_n` is fixed.

The ordinary logarithmic `L^2` mass is also finite:

\[
\|m_n\|_{L^2(dQ)}^2
=s_n\delta_n\|\chi\|_2^2,
\qquad
\|m\|_2^2
=\|\chi\|_2^2\sum_ns_n\delta_n<\infty.
\tag{PL316-13}
\]

## 2. The zero-extension boundary terms are exactly controlled

The critical endpoint is delicate because interior `H^{1/2}` alone does not guarantee that extension by zero remains in `H^{1/2}(R)`. Here the exterior interactions can be evaluated directly.

At the right endpoint,

\[
\int_{1}^{\infty}\frac{dz}{(z-x)^2}=\frac1{1-x},
\]

and the logarithmic coordinate gives

\[
\int_{-1}^{1}\frac{|f(x)|^2}{1-x}\,dx
=
\int_0^\infty |m(Q)|^2\,dQ<\infty.
\tag{PL316-14}
\]

At the left endpoint,

\[
\int_{-\infty}^{-1}\frac{dz}{(x-z)^2}=\frac1{1+x},
\]

so

\[
\int_{-1}^{1}\frac{|f(x)|^2}{1+x}\,dx
=
\int_0^\infty
|m(Q)|^2\frac{e^{-Q}}{1-e^{-Q}}\,dQ.
\tag{PL316-15}
\]

Because the supports start at some `Q_0>0`, the last weight is uniformly bounded on the support and (PL316-13) controls it. Finally,

\[
\|f\|_{L^2(-1,1)}^2
=2\int_0^\infty e^{-Q}|m(Q)|^2\,dQ<\infty.
\tag{PL316-16}
\]

Equations (PL316-9), (PL316-14), (PL316-15), and (PL316-16) prove (PL316-4) directly from the Gagliardo definition, without relying on an abstract extension theorem. They also give the quantitative estimate

\[
\|Ef\|_{H^{1/2}(\mathbb R)}
\le C_{Q_0,\chi}\left(
\sum_ns_n+\Bigl(\sum_ns_n\delta_n\Bigr)^{1/2}
\right),
\tag{PL316-17}
\]

up to an inessential equivalent-norm constant. Since the recursive Green-mass choice admits arbitrarily small `s_n`, (PL316-5) follows.

## 3. Why the moving-diagonal obstruction is unchanged

Nothing in the preceding regularity verification changes the selection argument of `PL-315`. For each fixed `delta_n`, weak convergence of the stretched Green measures permits choosing `s_n` arbitrarily small while retaining

\[
\mu_{s_n,r}
\bigl((r-\delta_n/2,r+\delta_n/2)\bigr)
\ge\frac34e^{-2r}.
\tag{PL316-18}
\]

On that interval the `n`-th packet obeys `m(q/s_n)>=s_n`. The normalization in

\[
\mathcal A_s[m](r)
=\frac1s\int m(q/s)\,d\mu_{s,r}(q)
\]

therefore cancels the packet height `s_n` and gives (PL316-6), independently of how small `s_n` is. At the packet center,

\[
Q_n m(Q_n)=\frac r{s_n}s_n=r,
\tag{PL316-19}
\]

so the mismatch still violates the sufficient `PL-314` condition `Qm(Q)->0` at exactly the sparse moving locations sampled by the Green atom.

The critical Sobolev norm is scale invariant under packet compression, but it is proportional to the packet amplitude `s_n`. This is the mechanism behind the counterexample: moving observation at `Q~1/s` amplifies an `H^{1/2}`-small packet by the reciprocal factor `1/s`.

## Prior-art and novelty audit

The critical zero-extension phenomenon itself is classical. The Lions--Magenes space `H_{00}^{1/2}` is standard; for example, Corentin Audiard, *Annales de l'Institut Fourier* **69** (2019), 31--80, DOI `10.5802/aif.3238`, recalls that ordinary zero extension fails at the half derivative in general and that the Lions--Magenes norm adds the boundary Hardy term `\int |u(x)|^2/d(x,\Omega^c) dx`. This is prior art, not a Mathia discovery.

A targeted literature check for critical zero-extension Sobolev regularity combined with moving-diagonal small-order fractional Green limits did not locate a theorem covering the line-specific construction. Search absence is not treated as evidence of broad novelty. The durable mathematical delta is narrower and exact: applying the classical critical Gagliardo/Hardy structure to the already-persisted `PL-315` packets shows that **the same moving-diagonal obstruction survives the endpoint class that `PL-315` had left open**.

## Adversarial controls and boundaries

1. This is a counterexample to **generic** critical `H^{1/2}` or `H_{00}^{1/2}` control as a sufficient moving-tail hypothesis. It does not show that the actual completed-Weil mismatch belongs to this class, nor that its source equation permits such sparse packets.
2. The result does not address any supercritical class `H^{1/2+eta}`, a critical Besov/Dini refinement, monotonicity, one-sided variation, an asymptotic expansion, or another source-structured condition that suppresses `m(r/s)/s`.
3. The proof does not infer zero-extension regularity from interior `H^{1/2}`. It explicitly computes both exterior Gagliardo interactions; this is necessary at the critical exponent.
4. No necessity claim is made for `Qm(Q)->0`. `PL-314` proves it is sufficient, while the present result only shows that critical zero-extension Sobolev control does not imply it.
5. The arbitrary-small-norm statement does not assert uniform failure at a fixed externally prescribed sequence of scales. The sequence `s_n` is part of the counterexample construction and is chosen recursively using the fixed-neighborhood Green-mass limit, exactly as in `PL-314`--`PL-315`.

## Consequence for the research line

`PL-315` left the half-derivative endpoint as the last obvious generic Sobolev shortcut below source-specific boundary analysis. `PL-316` closes that shortcut. The corner reduction cannot be justified by upgrading the present global/all-log regularity merely to critical zero-extension `H^{1/2}`.

The surviving targets are therefore genuinely stronger or structurally different: prove from the completed-Weil eigen-equation a tail law such as `Qm(Q)->0` or `m(Q)=o(1/Q)`, obtain a direct bound on the moving samples `m(r/s)/s`, derive monotone/one-sided or asymptotic endpoint structure, or establish a supercritical/critical-refined estimate that rules out scale-invariant sparse saturation. Only after such a source-specific moving-tail gate is proved does the rank-one endpoint moment from `PL-313` become a stable arithmetic matching parameter.
