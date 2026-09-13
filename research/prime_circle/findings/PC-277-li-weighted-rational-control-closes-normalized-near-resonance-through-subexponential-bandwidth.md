# PC-277 — Li-weighted rational control closes normalized near-resonance through subexponential bandwidth

**Status:** `DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the moving-bandwidth normalized scalar near-resonance escape left open by PC-274/PC-276.

PC-274 identifies the intrinsic non-collapsing normalization

\[
X_B(x,y):=(B+1)^2D_B(x,y),
\qquad
D_B(x,y):=
\min_{0<\max(|h|,|k|)\le B}
\|hx+ky\|_{\mathbb R/\mathbb Z},
\tag{1}
\]

for which `0<=X_B<=1`. Against the **uniform** rational grid, its elementary transport estimate only forces prime-blindness for `B=o((log q)^{1/3})`. PC-276 then shows, at fixed bandwidth, that the correct smooth baseline is not uniform measure but the exact normalized logarithmic-integral source `lambda_q`: all finite logarithmic corrections are already present before the Prime-Circle geometry acts.

Those two facts combine more strongly if the matched control preserves **both** pieces that matter in the moving-bandwidth problem:

1. the exact smooth `Li` source profile, and
2. the denominator-`q` rational geometry responsible for the eventual exact-resonance transition.

Discretize `lambda_q` onto the denominator-`q` grid. For example, choose a nearest-grid projection

\[
T_q:[2/q,1]\to\{1/q,2/q,\ldots,(q-1)/q\}
\]

with `|T_q(t)-t|<=1/q` and put

\[
\widetilde\lambda_q:=(T_q)_*\lambda_q.
\tag{2}
\]

This is a non-prime rational probability measure with exactly the same denominator as the Prime-Circle source and with the exact `Li` intensity up to mesh error. Let

\[
\widetilde\rho^{\mathrm{Li-grid}}_{q,B}
:=(X_B)_*(\widetilde\lambda_q\otimes\widetilde\lambda_q),
\tag{3}
\]

and let `\widetilde\rho^{prime}_{q,B}` denote the law of `X_B(p/q,r/q)` on the distinct prime pairs used in PC-273--PC-276.

Then there is an absolute `c>0` such that

\[
\boxed{
W_1\!\left(
\widetilde\rho^{\mathrm{prime}}_{q,B},
\widetilde\rho^{\mathrm{Li-grid}}_{q,B}
\right)
\ll
B(B+1)^2
\left(
(\log q)e^{-c\sqrt{\log q}}+
\frac{\log q}{q}
\right)
+
\frac{\log q}{q}.
}
\tag{4}
\]

Consequently, for **every** bandwidth sequence satisfying

\[
\boxed{\log B(q)=o(\sqrt{\log q}),}
\tag{5}
\]

we have

\[
\boxed{
W_1\!\left(
\widetilde\rho^{\mathrm{prime}}_{q,B(q)},
\widetilde\rho^{\mathrm{Li-grid}}_{q,B(q)}
\right)\longrightarrow0.
}
\tag{6}
\]

Thus every fixed power of `log q`, and more generally every bandwidth

\[
B(q)=\exp\!\bigl(o(\sqrt{\log q})\bigr),
\tag{7}
\]

is still unable to turn the intrinsically normalized scalar near-resonance law into a zero-sensitive Prime-Circle statistic at order one. Any discrepancy from the **uniform** grid in this regime can be reproduced by a non-prime rational control carrying only the classical `Li` source profile.

At the opposite endpoint the same rational control also has the correct exact-resonance collapse. Since `D_B(a/q,b/q)` is an integer multiple of `1/q` and the universal Dirichlet bound gives

\[
D_B(a/q,b/q)\le(B+1)^{-2},
\tag{8}
\]

we have

\[
\boxed{
(B+1)^2>q
\quad\Longrightarrow\quad
D_B(a/q,b/q)=0
}
\tag{9}
\]

for **every** denominator-`q` pair, prime or not. Hence both sides of (4) are exactly `delta_0` once `(B+1)^2>q`.

The scalar normalized branch is therefore squeezed from both ends. The genuinely unresolved regime is not “all moving bandwidth”: it is the intermediate rational-microscopic window where `B` grows too quickly for the classical PNT transport bound to survive the `B^2` normalization but has not yet reached the denominator-`q` exact-resonance transition.

## 1. Uniform prime-to-Li transport with a growing Lipschitz constant

PC-276 proves for each fixed Lipschitz test that the normalized prime source `nu_q` differs from the exact normalized `Li` source `lambda_q` by

\[
O_g\!\left((\log q)e^{-c\sqrt{\log q}}\right)
+O_g(\log q/q).
\tag{10}
\]

For the moving-bandwidth application one needs the dependence on the test norm. The same Stieltjes partial-summation proof gives the uniform bounded-Lipschitz form

\[
\boxed{
\left|\int g\,d\nu_q-\int g\,d\lambda_q\right|
\ll
\bigl(\|g\|_\infty+\operatorname{Lip}(g)\bigr)
(\log q)e^{-c\sqrt{\log q}}
+
\|g\|_\infty\frac{\log q}{q}.
}
\tag{11}
\]

One way to see the norm dependence without making any uniform small-`x` claim is to split the Stieltjes integral at `x=q^{1/2}`. The lower interval has normalized mass exponentially smaller than every power of `1/log q`. On `[q^{1/2},q]`, the classical quantitative PNT remainder is uniformly `O(xe^{-c'\sqrt{\log q}})`; integration by parts then contributes one factor of `Lip(g)` and the normalization `pi(q)^{-1}\asymp (log q)/q` produces (11). The omitted endpoint/prime-`2` terms are `O((log q)/q)`.

The grid projection in (2) satisfies directly

\[
W_1(\lambda_q,\widetilde\lambda_q)\le\frac1q.
\tag{12}
\]

Combining (11) with the Kantorovich dual representation of `W_1` therefore gives

\[
\boxed{
W_1(\nu_q,\widetilde\lambda_q)
\ll
(\log q)e^{-c\sqrt{\log q}}
+
\frac{\log q}{q}.
}
\tag{13}
\]

This is the source estimate needed below. No zeta-zero explicit formula is used: it is only the same classical zero-free-region PNT input already used by PC-276.

## 2. The intrinsic normalization costs exactly a cubic bandwidth factor

PC-273 proves

\[
|D_B(x,y)-D_B(x',y')|
\le
B\bigl(|x-x'|+|y-y'|\bigr).
\tag{14}
\]

Therefore

\[
\boxed{
\operatorname{Lip}(X_B)
\le B(B+1)^2
}
\tag{15}
\]

for the `l^1` source metric. Coupling two independent copies of an optimal coupling between `nu_q` and `\widetilde\lambda_q`, pushing through `X_B`, and using (13) gives

\[
W_1\!\left(
(X_B)_*(\nu_q^{\otimes2}),
(X_B)_*(\widetilde\lambda_q^{\otimes2})
\right)
\ll
B(B+1)^2
\left(
(\log q)e^{-c\sqrt{\log q}}+
\frac{\log q}{q}
\right).
\tag{16}
\]

Passing from the prime product law to distinct prime pairs changes a bounded output law by at most the diagonal mass

\[
M_q^{-1}=O(\log q/q),
\tag{17}
\]

which proves (4).

The cubic factor in (4) is not an arithmetic scale. It is simply

\[
\underbrace{B}_{\text{source Lipschitz cost of }D_B}
\times
\underbrace{(B+1)^2}_{\text{intrinsic non-collapse normalization}}.
\tag{18}
\]

Accordingly the `sqrt(log q)` threshold in (5) is not a proposed critical scale either. It is only the point up to which the already-classical de la Vallee-Poussin error wins against this worst-case Lipschitz amplification.

## 3. Why the rationalized Li control is the right matched baseline here

Using continuous `lambda_q` alone would correctly remove the smooth prime-density bias, but it would erase denominator-`q` discreteness. That is harmless at fixed bandwidth and becomes wrong near the exact-resonance scale. Using the uniform denominator-`q` grid alone preserves discreteness but leaves the deterministic `Li` source bias visible; after multiplying by `(B+1)^2`, that smooth bias can be amplified and mistaken for a prime-specific moving-bandwidth effect.

The control `\widetilde\lambda_q` separates these mechanisms. It contains no primes and no explicit-formula oscillation, but it preserves:

- the exact normalized logarithmic-integral source profile to mesh precision `O(1/q)`, and
- the same denominator-`q` rational support as the Prime-Circle source.

Therefore a statistic that cannot distinguish primes from `\widetilde\lambda_q` has not yet accessed a source feature beyond classical smooth prime density plus rational-grid geometry.

Equation (6) shows this throughout every `exp(o(sqrt(log q)))` bandwidth. Equation (9) shows exact agreement again after the denominator transition. Only the intermediate window can possibly distinguish the prime source from this stronger matched control without an additional rescaling or enriched observable.

## 4. Prior-art and novelty audit

No new external theorem is needed. The analytic input in (11) is the same classical quantitative prime number theorem already anchored in PC-273/PC-276 through Montgomery--Vaughan, *Multiplicative Number Theory I: Classical Theory*, Chapter 6. The transport step is the same elementary Wasserstein contraction used in PC-273. The bound (8) is the Dirichlet/pigeonhole estimate already classicalized in PC-271 and reused in PC-274.

The discretization (2) is only a matched-control construction; it is not claimed as new probability or number theory. A targeted novelty audit against the ingredients used here therefore finds no independent new analytic mechanism to claim. The project-local content is the **combined boundary statement**: once the control is required to preserve both the smooth `Li` intensity and the denominator-`q` rational geometry, the normalized scalar Prime-Circle near-resonance law remains classically reproducible far beyond the polylogarithmic window suggested by the prime-versus-uniform-grid estimate.

In particular, neither the appearance of `(B+1)^2`, the cubic Lipschitz loss, nor the surviving intermediate bandwidth window is evidence for RH. Any future positive claim in that window must still be checked against the same Li-weighted rational control before being attributed to zeta-zero information.

No new durable literature dependency is introduced, so `SOURCES.md` is unchanged.

## 5. What this rules out and what survives

The route

\[
\text{prime ordered source}
\longrightarrow
(B+1)^2\Delta_B
\longrightarrow
B=\exp(o(\sqrt{\log q}))
\longrightarrow
\text{order-one zero-sensitive scalar law}
\tag{19}
\]

is closed against the Li-weighted denominator-`q` control.

This includes every fixed bandwidth, every fixed power of `log q`, and every stretched-exponential bandwidth `B=\exp((\log q)^\alpha)` with `alpha<1/2`. It also identifies a false positive to avoid: a prime-versus-uniform-grid discrepancy in the normalized law is not sufficient, because the same discrepancy may already be generated by the smooth `Li` intensity.

The theorem does **not** close:

- the intermediate window in which `log B` is comparable with or larger than `sqrt(log q)` while `(B+1)^2<=q`;
- a further magnification of the Li-centered residual at a scale large enough to expose the classical explicit-formula remainder;
- the minimizing direction `(h,k)` or other signed/vector data discarded by the scalar minimum;
- conditioned source families; or
- genuinely cross-level/nonlocal Prime-Circle observables that are not bounded-Lipschitz functions of one denominator-`q` source pair.

Those are legitimate continuations. But a continuation that merely strengthens the PNT remainder, changes the smooth source approximation, or compares only against the uniform grid remains a classical source-analysis problem rather than a new geometric bridge to RH.

## 6. Falsification and audit tests

The result has direct failure tests.

1. A source test with bounded-Lipschitz norm `K` violating (11) by more than a constant multiple of `K(log q)e^{-c sqrt(log q)}` would falsify the quantitative transport step or the underlying PNT estimate.
2. A point `t` with `|T_q(t)-t|>1/q` would invalidate (12); choosing nearest-grid cells makes this impossible away from harmless endpoints.
3. A pair of source points violating (14) would falsify the exact `B`-Lipschitz estimate already used in PC-273.
4. For a sequence with `log B=o(sqrt(log q))`, a fixed positive lower bound on the Wasserstein distance in (6) would contradict (13)--(16).
5. A denominator-`q` pair with `(B+1)^2>q` and `D_B>0` would contradict (8), because the latter would force `0<D_B<1/q` even though `D_B` is quantized in multiples of `1/q`.
6. A discrepancy in the unresolved intermediate window, or after an additional amplification of the Li-centered residual, is outside the theorem rather than a counterexample.

## 7. Research-line consequence

PC-274 showed that the raw scalar law is prime-blind at every bandwidth but left the intrinsically normalized variable `X_B` as the immediate scalar continuation. PC-276 showed that fixed-bandwidth finite logarithmic centerings are entirely smooth-`Li` source data. PC-277 joins those boundaries without changing the research mandate: **the normalized scalar continuation is still smooth-source/rational-grid data throughout every sub-`exp(sqrt(log q))` bandwidth in the sense of (5), and it collapses exactly once the denominator-scale resonance becomes unavoidable.**

The next serious scalar test is therefore not another polylogarithmic bandwidth or another comparison with the uniform grid. It is the intermediate rational-microscopic window against the Li-weighted denominator-`q` control, or else an enriched observable that retains directional/nonlocal information before scalar compression.