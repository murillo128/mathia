# XF-103 — growing prime bands through q/polylog remain transition-nonidentifying

**Status:** `EXACT-DERIVED` + `GROWING-PRIME-BAND` + `DECISIVE-NEGATIVE` + `TRANSITION-NONIDENTIFIABILITY` + `STRONG-NARROWING`. XF-102 shows that making the first explicit-formula prime atoms visible inside a fixed physical Vieta band still does not identify the periodic transition time. Its explicit boundary was a cutoff fixed independently of the Xi scale. That boundary can be pushed much farther: a physical band may grow almost to `\frac12\log q` while retaining both the exact equal-weight realization margin and enough hidden degree to implant an arbitrary collision time.

Keep the XF-102 scaling

\[
M=q^2,\qquad N=2M,\qquad \Delta^2\asymp q^{-3},\qquad a:=N\Delta\asymp q^{1/2},
\tag{1}
\]

and let `L=L_q\to\infty` satisfy

\[
\boxed{e^L(1+L)=o(q^{1/2}).}
\tag{2}
\]

Set

\[
K:=\left\lfloor\frac{L}{\Delta}\right\rfloor.
\tag{3}
\]

For the same fixed nonnegative bump `\psi` used in XF-102, supported in `[-1,1]`, define the distribution-safe endpoint target

\[
Q_m^{\psi}
:=
B(m\Delta)
-\frac1{2\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right),
\qquad
\lambda_n:=\frac{\log n}{2},
\qquad 1\le m\le K,
\tag{4}
\]

where `B` is the exact archimedean/polar background of XF-052. Then

\[
\boxed{
\frac1N\sum_{m\le K}|Q_m^{\psi}|=o(1),
\qquad
\frac KN=o(1),
}
\tag{5}
\]

and the exact periodic heat trajectory through an equal-weight realization of `(4)` stays in the same vanishing normalized `\ell^1` cone for all `0\le t\le1/2`. Consequently, for **every** fixed `0<\tau\le1/2`, there is another degree-`N` periodic real-divisor control with the identical first-`K` trajectory on the whole modeled heat interval and transition time exactly `\tau`.

Thus the nonidentifiability mechanism of XF-101/102 is not confined to finitely many prime frequencies. It survives a diverging arithmetic band containing a growing number of prime-power atoms.

## 1. The growing endpoint source still costs only `o(N)` raw moment mass

XF-052 gives

\[
B(\xi)=e^\xi+e^{-\xi}-\frac{e^{-\xi}}{1-e^{-4\xi}},
\qquad \xi>0.
\tag{6}
\]

The elementary bound

\[
|B(\xi)|\ll e^\xi+1+\xi^{-1}
\tag{7}
\]

therefore yields

\[
\begin{aligned}
\sum_{m\le K}|B(m\Delta)|
&\ll
\sum_{m\le K}e^{m\Delta}
+K
+\Delta^{-1}\sum_{m\le K}\frac1m\\
&\ll
\Delta^{-1}\bigl(e^L+L+\log(K+1)+1\bigr).
\end{aligned}
\tag{8}
\]

For the atomic sector, compact support of `\psi` means that each prime-power atom contributes to at most three mesh sites. If it contributes to some `m\le K`, then

\[
\lambda_n\le L+\Delta,
\qquad
n\le X:=e^{2(L+\Delta)}.
\tag{9}
\]

No prime number theorem is needed. Using only `\Lambda(n)\le\log n`,

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
\le
\sum_{n\le X}\frac{\log n}{\sqrt n}
\ll
\sqrt X\log X
\ll e^L(1+L),
\tag{10}
\]

and hence

\[
\sum_{m\le K}
\left|
\frac1{2\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right)
\right|
\ll_\psi
\Delta^{-1}e^L(1+L).
\tag{11}
\]

Since `\Delta^{-1}/N\asymp q^{-1/2}`, equations `(8)` and `(11)` give

\[
\frac1N\sum_{m\le K}|Q_m^\psi|
\ll_\psi
q^{-1/2}
\bigl[e^L(1+L)+L+\log(K+1)\bigr]
=o(1).
\tag{12}
\]

The last step uses `(2)` and `\log K=O(\log q+\log(1+L))`. Also

\[
\frac KN\asymp\frac{L}{N\Delta}=\frac La=o(1).
\tag{13}
\]

Thus the sufficient cone of XF-085 holds eventually with a fixed margin, say `\kappa=1/2`, and `N\ge C_\kappa K`. There is an exact degree-`N` equal-weight unit-circle carrier whose first `K` power sums are `(4)`.

The estimate is deliberately insensitive to prime clustering. The triangle inequality and the compact mesh support charge each atom only `O(1)` times, so no spacing hypothesis between neighboring prime-power frequencies enters.

## 2. The small normalized moment cone remains forward-invariant for growing `L`

Let `P_m(t)` be the first `K` power sums of this exact periodic heat trajectory and put

\[
u_m(t):=\frac{P_m(t)}N,
\qquad
\xi_m:=m\Delta,
\tag{14}
\]

with

\[
S(t):=\sum_{m\le K}|u_m(t)|,
\qquad
D(t):=\sum_{m\le K}\xi_m|u_m(t)|.
\tag{15}
\]

The exact triangular equation of XF-087, in the normalization used by XF-102, is

\[
\dot u_m
=
\xi_m(\xi_m-a)u_m
-a\xi_m\sum_{i=1}^{m-1}u_i u_{m-i}.
\tag{16}
\]

Exactly as in XF-102 but now using only `\xi_m\le L`, its upper Dini derivative obeys

\[
\boxed{
D^+S
\le
\left[-(a-L)+2aS\right]D.
}
\tag{17}
\]

Equation `(12)` gives `S(0)=o(1)`, while `(2)` implies `L/a\to0`. For large `q`, throughout the barrier region `S\le1/8`,

\[
-(a-L)+2aS
\le -\frac34a+L
\le -\frac12a.
\tag{18}
\]

A first-exit argument therefore gives

\[
\boxed{
S(t)\le S(0)=o(1)
\qquad(0\le t\le1/2).
}
\tag{19}
\]

So the fixed-band invariance of XF-102 is actually a growing-band statement as long as the physical cutoff remains `o(a)` and the initial raw moment mass stays subcritical. Condition `(2)` guarantees both at once.

## 3. Arbitrary transition times remain exactly implantable

Fix any

\[
0<\tau\le\frac12,
\tag{20}
\]

and set

\[
R:=K+1,
\qquad
n:=N-2R.
\tag{21}
\]

Because `K=o(N)`, one has `n\sim N` and `n/K\to\infty`. By `(19)`,

\[
\sum_{m\le K}|P_m(\tau)|=N S(\tau)=o(N)=o(n).
\tag{22}
\]

XF-085 can therefore be applied again with exactly `n` unit-circle nodes to realize the target prefix `P_m(\tau)`, `1\le m\le K`, on a degree-`n` polynomial `A_\tau`. Choose a phase `\phi` avoiding the finite root set of `A_\tau` and multiply by the XF-101 collision crystal

\[
C_\phi(w):=(w^R-e^{i\phi})^2.
\tag{23}
\]

The crystal has degree `2R`, has `R` exact double roots on the unit circle, and contributes zero to every power sum of order `1\le m<R`; in particular it does not change any of the first `K` moments. The product

\[
F_\tau(w):=A_\tau(w)C_\phi(w)
\tag{24}
\]

therefore has degree exactly `N`, agrees with the original carrier on the complete visible prefix at time `\tau`, and has the same collision configuration used in XF-101. The collision normal form and backward real-zero-preserver argument already established there give

\[
\boxed{\Lambda_{\rm per}(F_\tau)=\tau.}
\tag{25}
\]

Because the first `K` equations are autonomous and triangular, equality of the prefix at `t=\tau` forces equality of the complete first-`K` trajectory on the whole common interval of existence. Hence the same growing prime-enriched Vieta history is compatible with **every** positive transition time in `(0,1/2]`.

## 4. A concrete band sees all prime powers through `q/(log q)^4`

Take

\[
\boxed{
L_q:=\frac12\log q-2\log\log q.
}
\tag{26}
\]

Then

\[
e^{L_q}=\frac{q^{1/2}}{(\log q)^2},
\qquad
q^{-1/2}e^{L_q}(1+L_q)=O((\log q)^{-1}),
\tag{27}
\]

so `(2)` holds. The corresponding prefix has

\[
K\asymp \frac{q^{3/2}\log q}{2}=o(q^2)=o(N)
\tag{28}
\]

up to the fixed constants implicit in the Xi mesh relation. More importantly, every prime-power atom with

\[
\lambda_n\le L_q-\Delta
\tag{29}
\]

lies fully inside the visible mesh band. Equivalently,

\[
n\le e^{2(L_q-\Delta)}
=(1+o(1))\frac{q}{(\log q)^4}.
\tag{30}
\]

Thus one may expose **all prime-power source atoms through an arithmetically growing range of order `q/(log q)^4`** and still leave the periodic transition time completely nonidentifiable from the entire autonomous low-moment history.

This is substantially stronger than merely observing the first prime `2`: the number and physical span of source atoms both diverge.

## 5. Stress tests and evidence boundary

The statement is intentionally finite-periodic and interface-level. It does **not** prove a Xi-to-periodic shadow theorem on frequencies of order `L_q`; XF-100 already explains why the earlier low-band shadow estimate cannot simply be extrapolated to prime scale. The theorem instead says that even if a redesigned, distribution-safe source extractor legally supplies all the moments `(4)`, that information is still insufficient to identify transition time after it is compressed into an autonomous sublinear Vieta prefix.

The condition `(2)` is sufficient, not asserted sharp. The crude arithmetic estimate `(10)` deliberately uses only `\Lambda(n)\le\log n`; sharper Chebyshev/PNT information would improve the quantitative frontier, but no such refinement is needed for the present obstruction. In particular, this finding does not claim that the mechanism survives once the normalized raw source mass stops being `o(1)`, nor that `L\sim\frac12\log q` is an exact saturation threshold.

Individual mesh samples near prime atoms may be as large as `O(\Delta^{-1})`; this is harmless for the exact equal-weight theorem because XF-085 requires a global raw `\ell^1/N` margin rather than pointwise smallness of each moment. Likewise, the growing number of constrained modes does not threaten the collision reserve while `K=o(N)`: the hidden factor `(23)` still occupies only `o(N)` degree.

## 6. Prior-art and novelty boundary

The load-bearing external ingredients are unchanged. The explicit-formula prime-power frequencies and coefficients are already anchored in `SOURCES.md` through Guinand--Weil; the exact prescribed-node equal-weight quadrature theorem is already anchored there through Gilboa--Peled; and the real-zero-preserver/collision ingredients used by XF-101 are already part of the line's established source chain. The new step is the elementary growing-band budget `(8)`--`(13)` and its combination with the exact forward-invariant `\ell^1` cone and collision crystal.

A targeted search across de Bruijn--Newman heat flow, Chebyshev-type quadrature, power-sum/Vieta representations, and root-of-unity collision constructions did not surface a result asserting this specific growing-prime-band transition nonidentifiability. No new literature dependency is introduced, so `SOURCES.md` does not need an update.

## 7. Consequence for `xi_flow`

XF-100 showed that the original guarded shadow is prime-blind. XF-102 then showed that crossing the first prime frequency is insufficient. The present finding removes a much larger rescue class:

\[
\boxed{
\text{diverging prime band}
+\text{sublinear autonomous Vieta prefix}
+\text{vanishing raw }\ell^1/N
\;\not\Rightarrow\;
\text{transition identifiability}.
}
\tag{31}
\]

The next viable interface must therefore break at least one of the structural properties used by the implant: it must force enough source mass or enough constrained degree to consume the hidden collision reserve, impose a genuinely non-prefix/global Xi constraint, or use an observable whose dynamics do not close autonomously on the visible low modes. Merely widening the prefix to a growing collection of prime-power frequencies—even through `q/(\log q)^4` in the explicit construction above—does not cross that information barrier.