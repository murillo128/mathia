# WI-013 — explicit witnesses uniformly cap the entire n-point pressure bridge below 0.676553

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the specific pressure-certificate/sliding-window family formalized as `Zeta23Ext.PalomarV2.n_point_bound` / `Zeta23Ext.Bridge.n_point_bound`. The conservative all-`n` ceiling below is derived directly from the formally stated bridge, the exact Montgomery--Taylor kernel at integer arguments, and an explicit period-37 witness word. No finite certificate floor, optimization run, or interval-arithmetic table is assumed. This does **not** bound genuinely different global Gram/Fenchel/Bellman assemblies such as WI-011--WI-012.

## 1. Exact bridge input

Let

\[
H:=H_{\rm MT}
=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
=0.6725007036794116457\ldots.
\]

The public `teal-sea/zeta-lab` Lean bridge states, for `n >= 2`, `m >= n`, `p > 0`, `c > 0`, a uniform local certificate

\[
F_n(g;p)\ge c\qquad(g_i\ge0),
\]

and the cap

\[
c\bigl(m-(n-1)\bigr)\le1,
\]

that the resulting asymptotic simple-critical-zero proportion is

\[
\Phi_n(c,m,p)
=
\frac{
H-\dfrac{(n-1)(m-1)}{pm}
}{
1-\dfrac{c(m-(n-1))}{m}
}.
\tag{1}
\]

This is the exact theorem contract in `lean/bridge/V2Challenge.lean`; `V2Solution.lean` proves the advertised statements from the sorry-free development, and the three-/four-point bridge was independently rebuilt in the Palomar registration recorded by the repository. The argument below uses only (1), its stated cap, and the definition of `F_n`.

Write

\[
k=n-1,
\qquad
F_n(g;p)=\frac{S(g)}p+W_n(g),
\qquad
S(g)=\sum_{i=1}^{k}g_i.
\tag{2}
\]

Here

\[
W_n(g)
=
\sum_{s=1}^{k}
\frac{2}{n-s}
\sum_{i=1}^{n-s}
 w\!\left(g_i+\cdots+g_{i+s-1}\right),
\tag{3}
\]

where `w(x)=k_MT(x)^2` is the squared normalized Montgomery--Taylor overlap kernel.

## 2. Reconstructing the witness leg directly from the formal bridge

Assume first `k >= 2`, equivalently `n >= 3`. Put

\[
d=m-k\ge1.
\]

After multiplying numerator and denominator of (1) by `m`, regard

\[
f(d)
=
\frac{H(k+d)-k(k+d-1)/p}{k+d(1-c)}.
\tag{4}
\]

If `Phi_n <= H` there is nothing to prove. In the positive-gain branch `f(d)>H`, direct subtraction gives

\[
Hcd>\frac{k(k+d-1)}p.
\tag{5}
\]

On the other hand

\[
f'(d)
\text{ has the sign of }
Hcp-1-c(k-1).
\tag{6}
\]

Condition (5), together with `d <= 1/c`, is stronger than positivity of (6). Hence in the only branch relevant to an improvement over `H`, `f` is increasing in `d`. We may therefore enlarge `d` to the largest integer allowed by the bridge cap,

\[
q=\left\lfloor\frac1c\right\rfloor,
\qquad
M=k+q.
\tag{7}
\]

At this cap `cq <= 1`, so the denominator in (4) is at least `M-1`; the numerator is positive in the positive-gain branch. Thus

\[
\Phi_n
\le
H+\frac{H}{M-1}-\frac{k}{p}.
\tag{8}
\]

Since `q >= 1/c-1`, for `k >= 2`,

\[
M-1=k+q-1
\ge k-2+\frac1c,
\]

and therefore

\[
\boxed{
\Phi_n\le H+Hc-\frac{k}{p}.
}
\tag{9}
\]

Now evaluate the assumed certificate at **any** explicit nonnegative gap vector `g`. From (2),

\[
c\le W_n(g)+\frac{S(g)}p.
\]

Substitution into (9) gives

\[
\Phi_n
\le
H+H W_n(g)+\frac{H S(g)-k}{p}.
\tag{10}
\]

Consequently every witness satisfying

\[
S(g)\le\frac{k}{H}
\tag{11}
\]

forces the exact pressure-independent ceiling

\[
\boxed{
\Phi_n\le H\bigl(1+W_n(g)\bigr).
}
\tag{12}
\]

This is the load-bearing reduction. A closely related witness leg appears in the later `zeta-lab/hunts/family_wall` analysis; the derivation above is independent and pins it line-by-line to the exact formal bridge hypotheses.

## 3. Exact integer values of the Montgomery--Taylor kernel

The bridge defines

\[
K(x)=\int_{-1/2}^{1/2}
\cos(\sqrt2\,t)\cos(2\pi x t)\,dt,
\qquad
k_{\rm MT}(x)=\frac{K(x)}{K(0)}.
\]

For every positive integer `j`, product-to-sum gives exactly

\[
\boxed{
k_{\rm MT}(j)=\frac{(-1)^{j+1}}{2\pi^2j^2-1},}
\qquad
\boxed{
w(j)=\frac1{(2\pi^2j^2-1)^2}.}
\tag{13}
\]

Write `w_j=w(j)`. Two elementary consequences used below are

\[
w_j\le\frac{w_1}{j^4}\qquad(j\ge1),
\tag{14}
\]

because `2 pi^2 j^2-1 >= j^2(2 pi^2-1)`, and

\[
w_2<\frac{w_1}{16},
\tag{15}
\]

because `8 pi^2-1 > 4(2 pi^2-1)`.

## 4. One explicit word works for every n >= 3

Use the period-37 sequence already identified in the `zeta-lab` family-wall audit,

\[
\boxed{
g_i
=1+\left\lfloor\frac{18i}{37}\right\rfloor
 -\left\lfloor\frac{18(i-1)}{37}\right\rfloor.}
\tag{16}
\]

Every `g_i` is `1` or `2`. In its first `k` entries, the number of twos is exactly

\[
r_k=\left\lfloor\frac{18k}{37}\right\rfloor,
\]

so

\[
S_k=k+r_k\le\frac{55}{37}k.
\tag{17}
\]

The required comparison with `1/H` can be proved without trusting a decimal. Set `x=1/sqrt(2)`. Alternating Taylor bounds at `0<x<1` give

\[
\cos x
\ge1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}
=\frac{4379}{5760},
\]

and

\[
\frac{\sin x}{x}
\le1-\frac{x^2}{6}+\frac{x^4}{120}
=\frac{147}{160}.
\]

Hence

\[
\cos x-\frac{91}{110}\frac{\sin x}{x}
\ge
\frac{59}{316800}>0,
\]

so

\[
x\cot x>\frac{91}{110},
\qquad
\boxed{H<\frac{37}{55}.}
\tag{18}
\]

Since `H>0`, (17)--(18) imply `S_k < k/H` for every `k`.

For `k=2` (that is, `n=3`), the prefix is `(1,1)` and (3) gives exactly

\[
W_3=2w_1+2w_2.
\tag{19}
\]

For every `k >= 3`, at least one quarter of the first `k` gaps are twos. Indeed this is direct for `k=3,4`, while for `k>=5`,

\[
\left\lfloor\frac{18k}{37}\right\rfloor
\ge\frac{18k}{37}-1
\ge\frac{k}{4}.
\tag{20}
\]

Therefore the scale-one contribution to (3) is at most

\[
\frac32w_1+\frac12w_2.
\]

At every scale `s>=2`, each window sum is an integer at least `s`, and (13) is decreasing on positive integers. The entire scale contributes at most `2w_s`. Thus

\[
W_n(g)
\le
\frac32w_1+\frac52w_2
+2\sum_{s\ge3}w_s.
\tag{21}
\]

Using (14)--(15) and the elementary tail estimate

\[
\sum_{s\ge3}\frac1{s^4}
\le\frac1{3^4}+\int_3^\infty x^{-4}\,dx
=\frac2{81},
\]

we get

\[
W_n(g)
<
\left(\frac32+\frac5{32}+\frac4{81}\right)w_1
=
\frac{4421}{2592}w_1
<2w_1
<2w_1+2w_2.
\tag{22}
\]

Combining (12), (19), and (22), **every admissible instance with `n>=3`** satisfies

\[
\Phi_n
\le
H\left(1+2w_1+2w_2\right).
\tag{23}
\]

## 5. The n = 2 endpoint is below the same ceiling

The parametric Lean theorem starts at `n=2`, so this endpoint must be checked separately rather than hidden in the `k>=2` argument.

Put

\[
a=2w_1,
\qquad
b=2w_2,
\qquad
x=1/p.
\]

The one-gap witness `g_1=1` gives `c <= a+x`. Writing `q=m-1`, the exact bridge is

\[
\Phi_2
=\frac{H(q+1)-qx}{1+q(1-c)}.
\tag{24}
\]

If `Phi_2 <= H`, again there is nothing to prove. Otherwise

\[
Hc>x,
\tag{25}
\]

and (24) is increasing in `q`. The cap gives `q <= floor(1/c)`, so at `Q=floor(1/c)`,

\[
\Phi_2
\le H+\frac{H}{Q}-x
\le\frac{H}{1-c}-x
\le\frac{H}{1-a-x}-x.
\tag{26}
\]

The earlier exact bound `H<37/55<7/10`, together with `pi>3`, gives `a<2/17^2<1/100`. From (25) and `c<=a+x`,

\[
x<\frac{Ha}{1-H}<\frac7{300}.
\]

Hence `(1-a-x)(1-a) > (29/30)(99/100) > H`, which algebraically implies from (26)

\[
\Phi_2<\frac{H}{1-a}.
\tag{27}
\]

Finally

\[
\frac1{1-a}\le1+a+b
\tag{28}
\]

is elementary. With `X=pi^2`, `A=2X-1`, `B=8X-1`, (28) is equivalent to

\[
A^2(A^2-2)-2B^2>0.
\]

The left side is

\[
P(X)=16X^4-32X^3-112X^2+32X-3.
\]

Since `X>9`, `P(9)=72861>0`, and

\[
P'(X)=32(2X^3-3X^2-7X+1)>0
\qquad(X\ge9),
\]

(28) follows. Thus the same ceiling also covers `n=2`.

## 6. Uniform all-n obstruction

Equations (23) and (27)--(28) prove the single exact statement

\[
\boxed{
\forall n\ge2,
\qquad
\Phi_n(c,m,p)
\le
C_{\rm press},
}
\tag{29}
\]

for every admissible certificate and every admissible `c,m,p` in the present formal bridge, where

\[
\boxed{
C_{\rm press}
:=
H\left(
1+rac{2}{(2\pi^2-1)^2}
 +\frac{2}{(8\pi^2-1)^2}
\right)
=0.6765522097515686554\ldots.
}
\tag{30}
\]

So **no local certificate whatsoever, at any finite point count, can make this specific n-point pressure/sliding-window bridge certify more than about 67.6553% simple critical zeros.** The obstruction is not certificate quality: an explicit admissible configuration defeats the bridge before one asks how well `F_n` can actually be minimized.

This materially strengthens WI-010. WI-010 proved that the gain of the same bridge is `O(1/n)` and hence returns to `H` as `n -> infinity`; (29) closes the remaining logical loophole that a moderate finite `n` might produce an arbitrarily large jump.

## 7. Prior art and novelty audit

No novelty is claimed for the **witness-leg idea** or the period-37 word. `teal-sea/zeta-lab/hunts/family_wall/` independently developed the same style of pressure cancellation, found the explicit word (16), and reports the stronger numerical family ceiling

\[
\sup_n\Phi_n\le0.675142509660254.
\]

That upstream result is extremely relevant prior art and materially redirects this line. However, its own `RESULTS.md` says explicitly that the family-wall result is not a proof or machine-checked theorem, and lists as a remaining load-bearing item the need to check the cap/bridge assumptions against `n_point_bound` line by line. Its adversarial audit also found and repaired two incorrect inequality steps in an earlier version of the chain.

WI-013 therefore does **not** promote `0.675142509660254` to established evidence. Instead it gives a weaker but self-contained exact ceiling, checks the bridge contract directly against `V2Challenge.lean`, reconstructs the positive-gain/cap argument independently, and uses only elementary inequalities after importing the explicit prior-art word. The stronger upstream number remains a valuable target for formal audit.

The exact ceiling (30) is also much narrower in scope than claims that all Montgomery--Taylor Gram methods have a universal thermodynamic ceiling. It applies only to the present `Phi_n` pressure bridge. A global Fenchel witness, capacitated matching, Bellman/subaction certificate, multi-profile construction, or new arithmetic input can evade (29) by changing the global assembly itself.

## 8. Adversarial checks and falsification test

The main ways this result could fail are concrete.

1. **Bridge mismatch.** Equation (1), the cap, or the definition of `F_n` would have to differ from the actual formal theorem. They were checked against the public `V2Challenge.lean` statement corresponding to the proved development.
2. **Positive-branch monotonicity.** A counterexample would require `Phi_n>H` while the derivative sign in (6) is nonpositive. Equation (5) plus `d<=1/c` rules this out directly.
3. **Witness infeasibility.** The period-37 prefixes would need `S_k>k/H`. Equations (17)--(18) prove the opposite without decimal numerics.
4. **Kernel-energy error.** The integer formula (13) follows by a one-line product-to-sum integral. Equations (14)--(22) are monotone positive-term upper bounds; no cancellation or floating-point sign is used.
5. **Endpoint escape.** `n=2` is handled separately in §5 and is strictly below the same constant.

A decisive machine audit would formalize (29) as a theorem parameterized by the already formal `n_point_bound`, proving only the elementary integer-kernel and witness inequalities above. No prime-side analytic theorem needs to be added.

## 9. Research consequence

The route

\[
\boxed{
\text{same }n\text{-point pressure bridge}
+\text{arbitrarily strong finite certificate}
\Longrightarrow
\text{large new simple-zero fraction}
}
\]

is closed uniformly, not merely asymptotically. Within this bridge the absolute conservative ceiling is `0.6765522097...`; upstream prior art suggests the true family ceiling is lower still.

This strengthens the strategic conclusion of WI-010 and supports the architectural move already isolated in WI-011--WI-012: further progress inside bandwidth one should spend effort on **changing the global assembly of Gram defect**, not on making the same pressure certificate larger or increasing its point count. The barrier says nothing against that global-dual route, and it also does not touch support-greater-than-one arithmetic mechanisms.