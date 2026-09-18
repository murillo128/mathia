# RE-197 — Subcritical growing jets collapse the full real Euler ray superlogarithmically

**Status:** `EXACT-DERIVED + GROWING-EULER-JET-MATCHING + FULL-REAL-EULER-RAY + SUPERLOGARITHMIC-SUPPRESSION + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-186-RE-196-SPLICE + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-186, RE-196.

`RE-196` proves that every *fixed* number of exactly matched Euler boundary jets makes the complete real Euler profile smaller than the selector debt by the corresponding fixed power of `log p`, but it deliberately leaves the growing-depth regime open because the centered transport constants were not tracked uniformly in `K`. `RE-186` supplies exactly the missing geometry: its repair uses a fixed logarithmic interpolation window, advances in exponentially small logarithmic microsteps, and has an explicit geometric residual recurrence.

Combining those two structures yields a genuinely growing precision theorem.

Let

\[
L:=\log p,
\qquad
K=K(p)\ge1,
\qquad
K\log\log p=o(L),
\tag{1}
\]

and let `Q_{p,K}` be the ordinary-prime `{0,1,2}` matched control constructed by `RE-186`. Write

\[
D_Q(s)
:=
\sum_q (m_Q(q)-1)[-\log(1-q^{-s})]
\]

and

\[
d_p\asymp\frac1{\sqrt p\log p}
\]

for the canonical selector debt. Then there is an absolute constant `C>1` such that

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\le
 d_p\left(\frac{C}{\log p}\right)^{K+1}
 +d_p\,p^{-1/2+o(1)}.
}
\tag{2}
\]

The `o(1)` is uniform along every family satisfying (1). In particular, if also `K(p)\to\infty`, then

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\le
 d_p\exp\!\left(-(1-o(1))K\log\log p\right).
}
\tag{3}
\]

At the same time all conclusions of `RE-186` remain in force: `Q_{p,K}` is supported on ordinary primes, has multiplicities only in `{0,1,2}`, matches every Euler boundary derivative through order `K` exactly, obeys every fixed Korobov--Vinogradov source envelope, and still carries the order-one normalized Robin transient at `8p` before any repair appears.

Thus the stable non-rigidity statement on the **entire positive real Euler axis** is no longer confined to fixed log-power precision. Throughout the whole subcritical depth already realized by `RE-186`, increasing the number of matched jets buys essentially one additional factor `1/log p` per jet, even though `K` itself tends to infinity.

For example, if `K=(\log p)^\alpha` with any fixed `0<\alpha<1`, then

\[
\sup_{s\ge1}|D_Q(s)|
\le
 d_p\exp\!\left(-(1+o(1))(\log p)^\alpha\log\log p\right).
\tag{4}
\]

This closes the growing-depth precision question below `K\asymp \log p/\log\log p`; it does **not** close the larger constructive region of `RE-188`, nor the high-order saturation regime of `RE-189`.

## 1. The full-ray Taylor bound is uniform in growing order

Put

\[
r:=K+1,
\qquad
c_q:=m_Q(q)-1,
\qquad
F(u):=p^uD_Q(1+u),
\qquad u\ge0.
\tag{5}
\]

The exact Euler expansion is

\[
F(u)
=
\sum_q c_q
\sum_{m\ge1}\frac{q^{-m}}m
\exp[-u\lambda_{m,q}],
\qquad
\lambda_{m,q}:=m\log q-L.
\tag{6}
\]

Every modified prime satisfies `q>=2p`, so `lambda_{m,q}>0`. Because `RE-186` matches `D_Q^{(j)}(1+)=0` for `0<=j<=K`, the Leibniz rule gives

\[
F^{(j)}(0)=0,
\qquad 0\le j\le K.
\tag{7}
\]

Define the absolute normalized `r`-th rate moment

\[
\mathfrak M_r
:=
\sum_q|c_q|
\sum_{m\ge1}\frac{q^{-m}}m\lambda_{m,q}^r.
\tag{8}
\]

Once `\mathfrak M_r<\infty`, Taylor's theorem with integral remainder gives

\[
|F(u)|
\le
\frac{\mathfrak M_r}{r!}u^r,
\tag{9}
\]

because the extra factors `e^{-u\lambda_{m,q}}` can only decrease the absolute `r`-th derivative. Therefore

\[
\sup_{u\ge0}|D_Q(1+u)|
\le
\frac{\mathfrak M_r}{r!}
\left(\frac r{eL}\right)^r.
\tag{10}
\]

Stirling gives the convenient uniform form

\[
\boxed{
\frac1{r!}
\left(\frac r{eL}\right)^r
\asymp
\frac1{\sqrt r\,L^r}.
}
\tag{11}
\]

So the entire problem is reduced to tracking one growing centered rate moment of the `RE-186` source.

## 2. The microstep repair has exponentially bounded first-harmonic transport

Use the exact `RE-186` scales

\[
h=e^{-a_0V(p)/8},
\qquad
x_n=16p\,e^{nh}.
\tag{12}
\]

Its generation-`n` repair is supported inside the fixed logarithmic window

\[
\log(q/x_n)\in[0,1+o(1)],
\tag{13}
\]

so

\[
\log(q/p)\le C+nh
\tag{14}
\]

with an absolute `C`. Let `M_n` be the exact Chebyshev-coordinate residual from `RE-186`. That finding proves

\[
M_0\le C_0^K d_p
\tag{15}
\]

and

\[
M_n
\ll
3^{-n}M_0
+
K^2\sum_{a<n}
\frac{3^{-(n-1-a)}}{x_a}.
\tag{16}
\]

It also proves that the total absolute `H`-mass edited in generation `n` is `O(KM_n)`. Since `H(q)\asymp q^{-1}` on the whole repair, the first-harmonic contribution to (8) is bounded by

\[
\mathfrak M_r^{(1)}
\ll
 d_p C^r
+
K\sum_{n\ge0}M_n(C+nh)^r.
\tag{17}
\]

The geometric part of (16) is harmless at growing order. The elementary estimate

\[
\sum_{n\ge0}3^{-n}(C+nh)^r
\le C_1^r\bigl(1+h^rr!\bigr)
\tag{18}
\]

and

\[
hr
=
K e^{-a_0V(p)/8}(1+o(1))
=o(1)
\tag{19}
\]

show that this part contributes at most

\[
d_p C_2^K.
\tag{20}
\]

For the rounding floor in (16), interchange the two generation sums. A second elementary exponential-moment estimate gives

\[
\sum_{a\ge0}rac{(C+ah)^r}{x_a}
\ll
\frac{C_3^r r!}{ph}.
\tag{21}
\]

Hence

\[
\boxed{
\mathfrak M_r^{(1)}
\ll
 d_p C_4^K
+
\frac{K^3C_4^r r!}{ph}.
}
\tag{22}
\]

This estimate also proves a point not stated in `RE-186`: although that finding only needed absolute convergence through derivative order `K`, the normalized derivative of order `K+1` needed here is absolutely summable as well.

Now use (1). We have

\[
h^{-1}=p^{o(1)},
\qquad
r\log r=o(L).
\tag{23}
\]

Insert (22) into (10). The selector-propagated part gives

\[
\ll
 d_p\left(\frac C L\right)^r,
\tag{24}
\]

while the quantization floor gives

\[
\ll
\frac{p^{-1+o(1)}K^3C^r r!}{\sqrt r\,L^r}
=
 p^{-1+o(1)}
\left(\frac{Cr}{L}\right)^r
\ll p^{-1+o(1)}.
\tag{25}
\]

Since

\[
p^{-1+o(1)}
=d_p\,p^{-1/2+o(1)},
\tag{26}
\]

up to the absorbed logarithmic factor, (24)--(25) already have the form claimed in (2).

## 3. Exact prime powers stay below the same floor

It remains to justify that the modes `m>=2` in (8) do not reintroduce a growing-order loss. Because `r=o(L)`, uniformly for every modified `q>=2p`,

\[
\frac{(m+1)^{r-1}q^{-(m+1)}}{m^{r-1}q^{-m}}
\le
\frac{e^{r/2}}q
=o(1)
\qquad(m\ge2).
\tag{27}
\]

Thus the prime-power series is uniformly dominated by its first term:

\[
\sum_{m\ge2}m^{r-1}q^{-m}
\ll
2^rq^{-2}.
\tag{28}
\]

Since `lambda_{m,q}<=m log q`,

\[
\sum_{m\ge2}
\frac{q^{-m}}m\lambda_{m,q}^r
\ll
2^r\frac{(\log q)^r}{q^2}.
\tag{29}
\]

For `log q>r`, the function `(log q)^r/q` is decreasing. All modified primes satisfy that inequality for sufficiently large `p`, so

\[
\mathfrak M_r^{(\ge2)}
\ll
\frac{2^rL^r}{p}
\sum_q\frac{|c_q|}{q}.
\tag{30}
\]

The same recurrence (16), now with no moment weight, yields

\[
\sum_q\frac{|c_q|}{q}
\ll
C_5^Kd_p+rac{K^3}{ph}.
\tag{31}
\]

Combining (30), (31), and (11), and using again `K\log\log p=o(L)`, gives a full-ray prime-power contribution

\[
\ll
 d_p p^{-1+o(1)}+p^{-2+o(1)}.
\tag{32}
\]

This is smaller than the second term of (2). Equations (22) and (30) also establish `\mathfrak M_r<\infty`, completing the justification of the Taylor step.

## 4. The precision gain is superlogarithmic throughout the subcritical region

Equation (2) is stronger than merely saying that the real Euler profile tends to zero. It gives a quantitative modulus tied to the matched depth. If `K\to\infty`, then

\[
\left(\frac C{\log p}\right)^{K+1}
=
\exp\!\left(-(1-o(1))K\log\log p\right).
\tag{33}
\]

Condition (1) implies

\[
K\log\log p=o(\log p),
\]

so the `p^{-1/2+o(1)}` floor in (2) is asymptotically much smaller than (33). This proves (3).

The important distinction from `RE-188` is that the present theorem uses the **fixed-width** `RE-186` geometry. That is precisely why the `(K+1)`st centered transport moment costs only `C^K` rather than roughly `(CK)^K`. Once `K` grows beyond the fixed-window prime-power regime, `RE-188` widens the shell reservoir linearly in `K`; the same full-ray argument then pays that width in the first uncontrolled centered moment. Nothing here proves comparable suppression through the full `RE-188` depth

\[
K=o\!\left((\log p)^{5/3}(\log\log p)^{1/3}\right).
\]

Nor does (3) conflict with `RE-189`: its high-order normalized jets near `K\asymp(\log p)^2` lie far beyond (1) and enter a different saturation mechanism.

## Representation audit

The useful representation is the normalized Laplace coordinate already exposed by `RE-196`,

\[
F(u)=p^uD_Q(1+u).
\]

What changes here is not the Taylor argument but the source geometry inserted into its first omitted coefficient. In the `RE-186` microstep construction, each repair generation occupies a **fixed** centered logarithmic window while its residual mass contracts geometrically. The growing-order transport moment therefore sees `C^K`, not an uncontrolled `K`-dependent spatial radius. Quantization creates an exponentially decaying spatial tail; its `r`-th moment contributes an `r!`, but the selector factor `p^{-u}` converts that term into `(r/\log p)^r/p`, which remains negligible throughout (1).

This is still a stable-information theorem, not exact source identification. `RE-174` remains valid: exact values on a sufficiently rich unbounded temperature set determine the source. Here the complete real profile is nonzero but becomes superlogarithmically smaller than the Robin-relevant selector debt while the destination coordinate remains macroscopically changed.

The result is also source-specific. Generic moment matching for Laplace transforms and the severe ill-posedness of Laplace inversion are classical. The new quantitative ingredient is that the ordinary-prime bounded-multiplicity repair from `RE-186` simultaneously supplies exact growing jet annihilation, a fixed centered spatial window, a geometric residual recurrence, and enough prime-shell fidelity to keep the Robin transient alive.

## Adversarial self-review

**Does (2) silently assume absolute convergence of the `(K+1)`st derivative, which `RE-186` did not state?** No. Equations (17)--(22) and (27)--(32) prove absolute summability of the exact normalized rate moment `\mathfrak M_{K+1}`. This is an additional consequence of the `RE-186` recurrence, not an imported assumption.

**Could the enormous number `h^{-1}` of microstep generations destroy the growing moment?** It appears only in the quantization floor as `1/h=p^{o(1)}`. The selector-propagated mass contracts geometrically in generation number before the baseline can move a macroscopic logarithmic distance. For the floor term, summing `e^{-nh}(C+nh)^r` produces `h^{-1}r!`; condition (1) makes both factors subexponential in `p` at the required scale.

**Is the prime-power estimate uniform in growing `K`?** Yes only in the stated subcritical region. Equation (27) uses `r=o(log p)`, which follows from (1). The stronger condition (1) is already required by `RE-186` to make its fixed-width exact shell matrix approximate the Chebyshev frame.

**Does the theorem include the arbitrary reciprocal-variation padding of `RE-195`--`RE-196`?** No. For fixed `K`, that padding is uniformly harmless, but its derivative bounds were not tracked uniformly when `K` grows and its terminal support may depend on the prescribed variation. The present theorem deliberately uses the canonical `RE-186` matched control and proves a growing-depth full-ray near-null direction without claiming arbitrary unsigned variation at the same time.

**Can (2) be pushed directly through the full depth of `RE-188`?** Not by the same estimate. `RE-188` uses logarithmic repair width `W\asymp K`; the first omitted centered moment can therefore cost roughly `K^{K+1}` before the real-ray Taylor factor is applied. A different representation or a signed cancellation estimate for that omitted moment would be needed to retain superlogarithmic suppression once `K` approaches or exceeds `log p`.

**Does observing complex temperatures change the conclusion?** Potentially. As in `RE-196`, the proof uses positivity of the real damping rates `lambda_{m,q}`. Vertical phases probe the logarithmic support oscillatory rather than monotonically, so no complex-strip stability claim is made.

## Prior-art audit

The general inverse-problem backdrop is classical: finite moment regularization of Laplace inversion and the severe instability of recovering a source from Laplace data are well established in the moment-problem literature. Targeted searches around Laplace inversion with finite moments found, among others, Dung--Huy--Quan--Trong (2006), *A Hausdorff-like moment problem and the inversion of the Laplace transform*, and modern work on the ill-posed Hausdorff moment problem. None supplies the line-specific estimate (2), and no external theorem from that literature is used in the proof.

The load-bearing inputs are internal: exact Euler resummation and the microstep shell recurrence of `RE-186`, together with the normalized real-ray Taylor mechanism of `RE-196`. The remaining estimates are elementary exponential moments, Stirling, and monotonicity. No new external dependency is introduced, so `SOURCES.md` is unchanged.

## Consequence for the research line

The scalar real-Euler frontier is now narrower than after `RE-196`. A fixed log-power precision theorem cannot help, and neither can any precision schedule of the form

\[
\varepsilon_p
\gg
\exp[-(1-o(1))K(p)\log\log p]
\]

for some growing `K` satisfying (1): an honest ordinary-prime `{0,1,2}` source can remain inside that full-ray tolerance while retaining an order-one Robin transient.

The unresolved scalar region begins only when one of the ingredients above fails: growing jet depth at or beyond `log p/log log p`, the wider `RE-188` construction where the first omitted moment pays a growing spatial radius, the high-order saturation region of `RE-189`, or genuinely complex/nonlocal observables. A future coercive invariant must therefore measure signed source structure that survives these matched near-null directions rather than raw spectral span, raw reciprocal variation, or any fixed real-axis precision scale.