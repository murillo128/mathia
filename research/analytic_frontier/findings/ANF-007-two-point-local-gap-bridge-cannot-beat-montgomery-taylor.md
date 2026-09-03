# ANF-007 — two-point local-gap certificates cannot beat Montgomery--Taylor

**Status:** `EXACT-DERIVED + FORMAL-SOURCE-BRIDGE + NEGATIVE/STRUCTURAL-BOUNDARY`. In the exact `n_point_bound` bridge used by `ANF-006`, the `n=2` specialization can never improve the Montgomery--Taylor baseline, no matter how sharply its one-gap certificate is proved or how the pressure denominator and block size are tuned. Since the same bridge has a fully checked improving `n=3` instance, **three consecutive points are the minimal local order at which this local-gap mechanism can add unconditional information.**

## 1. The exact two-point specialization

Let

\[
H:=\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
=0.6725007036794116\ldots
\]

be the Montgomery--Taylor/Anthropic baseline. The formally proved general bridge recorded in `ANF-006` is

\[
\Phi_n(n,c,m,p)
=
\frac{H-(n-1)(m-1)/(pm)}
     {1-c\bigl(m-(n-1)\bigr)/m},
\tag{1}
\]

under `n>=2`, `m>=n`, `p>0`, `c>0`, a finite certificate

\[
c\le F_n(p,g)\qquad(g_i\ge0),
\tag{2}
\]

and the block-cap condition

\[
c\bigl(m-(n-1)\bigr)\le1.
\tag{3}
\]

At `n=2` there is one gap `g>=0`, and the definition of the bridge functional reduces exactly to

\[
F_2(p,g)=\frac gp+2w(g),
\qquad
w(g)=k(g)^2,
\tag{4}
\]

where

\[
k(x)=\frac{K(x)}{K(0)},
\qquad
K(x)=
\frac{\sin(\pi x-1/\sqrt2)}{2\pi x-\sqrt2}
+
\frac{\sin(\pi x+1/\sqrt2)}{2\pi x+\sqrt2}.
\tag{5}
\]

The resulting bound constant is

\[
\Phi_2(c,m,p)
=
\frac{H-(m-1)/(pm)}{1-c(m-1)/m}.
\tag{6}
\]

Because (3) and `m>=2` imply

\[
0\le \frac{c(m-1)}m\le\frac1m<1,
\]

the denominator in (6) is positive. Subtracting `H` gives the exact identity

\[
\boxed{
\Phi_2(c,m,p)-H
=
\frac{m-1}{m}
\frac{cH-1/p}{1-c(m-1)/m}.
}
\tag{7}
\]

Thus a two-point certificate could improve the baseline **if and only if**

\[
pcH>1.
\tag{8}
\]

The rest of the argument shows that the Montgomery--Taylor overlap kernel forbids (8).

## 2. The overlap kernel has a zero before `4/3`

Put

\[
a:=\frac1{\sqrt2}.
\]

At `x=1`, (5) simplifies to

\[
K(1)
=
\sin a\left(
\frac1{2\pi-\sqrt2}-\frac1{2\pi+\sqrt2}
\right)>0.
\tag{9}
\]

At `x=4/3`, both sine terms in (5) are negative. Indeed the elementary bounds

\[
\frac\pi6<a<\frac\pi3
\]

imply

\[
\pi<\frac{4\pi}{3}-a<\frac{3\pi}{2},
\qquad
\frac{3\pi}{2}<\frac{4\pi}{3}+a<2\pi.
\tag{10}
\]

Both denominators in (5) are positive there, hence

\[
K(4/3)<0.
\tag{11}
\]

By continuity, there is therefore some

\[
\boxed{r\in(1,4/3)\quad\text{with}\quad K(r)=0.}
\tag{12}
\]

Consequently `w(r)=0`.

## 3. Every one-gap certificate is too weak to pay its pressure tax

Any valid uniform certificate (2) at `n=2` must hold at the particular gap `g=r`. By (4) and (12),

\[
c\le F_2(p,r)=\frac rp,
\]

so

\[
pcH\le rH.
\tag{13}
\]

Now `H<3/4` exactly. To see this, for `0<a<\pi/2` we have `sin a<a` and

\[
\cos a>1-\frac{a^2}{2}=\frac34.
\]

Hence

\[
a\cot a=\frac{a\cos a}{\sin a}>\cos a>\frac34,
\]

and therefore

\[
H=\frac32-a\cot a<\frac34.
\tag{14}
\]

Combining (12)--(14),

\[
\boxed{pcH\le rH<\frac43\cdot\frac34=1.}
\tag{15}
\]

This is the strict opposite of the necessary-and-sufficient improvement condition (8). Substitution into (7) yields

\[
\boxed{\Phi_2(c,m,p)<H}
\tag{16}
\]

for every admissible positive two-point certificate, every pressure denominator `p`, and every allowed block size `m`.

The obstruction is not numerical optimization. It comes from an actual zero of the overlap kernel occurring early enough that the best possible one-gap lower bound cannot compensate for the linear pressure cost introduced by the block argument.

## 4. Three points are therefore the minimal improving local order

The same formal bridge has an unconditional `n=3` theorem. The `teal-sea/zeta-lab` three-point development proves inside Lean the certificate

\[
F_3(3000,g_1,g_2)\ge\frac{1345}{10^6}
\qquad(g_1,g_2\ge0),
\]

and its `n_point_bound` instance gives

\[
\Phi_3
=0.67273733450380945\ldots
>H.
\tag{17}
\]

The three-point functional contains

\[
\frac{g_1+g_2}{p}+w(g_1)+w(g_2)+2w(g_1+g_2),
\tag{18}
\]

so the first successful local certificate uses the compatibility of **two adjacent gaps and their sum**. A one-gap statistic can sit exactly at a kernel zero and defeats any attempted gain; two adjacent gaps cannot in general place `g_1`, `g_2`, and `g_1+g_2` simultaneously at the relevant kernel zeros, which is precisely the extra finite-configuration information exploited by the proved three-point certificate.

Thus, within this bridge, the first genuinely useful configuration-level information is not merely “adjacency” of a pair. It is the additive consistency constraint already present in a triple of consecutive zeros.

## 5. Prior art and novelty boundary

The Montgomery--Taylor overlap kernel, Ainta's three-/seven-point mechanism, and the parametric `n_point_bound` theorem are prior art/formal-source material already anchored in `SOURCES.md` and `ANF-006`. The public `zeta-lab` bridge explicitly permits every `n>=2`, but its documented examples begin with the improving three-point case; the inspected Ainta and bridge materials do not state the two-point no-go above.

No publication-level novelty claim is made for the elementary inequalities (9)--(15). The durable Mathia contribution is the **exact structural classification relative to the current local-gap branch**: the formally available `n=2` case is provably incapable of beating the baseline, whereas the fully checked `n=3` case does beat it. That turns “local configuration information helps” into the sharper statement that order three is the minimal successful local order for this specific support-one bridge.

## 6. Falsification and boundaries

The claim is scoped to the `n_point_bound` architecture and the Montgomery--Taylor overlap kernel `w=k^2`. A different analytic window, a different block deduction, a signed/coboundary local functional, or a method not paying the pressure term in (4) is outside the theorem.

The no-go would fail if either the bridge's `n=2` specialization were not actually (4)--(6), or if the kernel had no zero below `4/3`. The first follows directly from the formal definitions of `F` and `Phi_n`; the second follows from the exact sign change (9)--(11), without numerical root finding.

The theorem also does not say that every useful higher-order certificate must exploit the particular spectral defect used by Ainta. It isolates only the **minimal point count** at which this bridge can improve `H`.

## 7. Consequences for `analytic_frontier`

`ANF-006` showed that local ordered configuration processing can escape the global pair-moment ceiling. The present result identifies the first nontrivial rung of that escape:

\[
\text{one gap / two points: impossible to improve}
\quad<\quad
\text{two compatible gaps / three points: proved improvement}.
\]

So the configuration-level branch should not spend effort optimizing two-point or isolated-gap certificates inside this architecture. The smallest meaningful finite object is a triple, and the load-bearing new information is already the additive relation among its three pair distances. Higher-point work should therefore be judged by what additional compatibility or memory it preserves beyond this three-point constraint, rather than by point count alone.
