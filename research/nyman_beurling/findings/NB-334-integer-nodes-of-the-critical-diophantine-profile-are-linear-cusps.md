# NB-334 — Integer nodes of the critical Diophantine profile are linear cusps

- **Date:** 2026-09-28
- **Status:** proved
- **Research line:** nyman_beurling
- **Depends on:** NB-332
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + CRITICAL-SQUARE-SCALE + DIOPHANTINE-PROFILE + INTEGER-NODE-LOCAL-ASYMPTOTIC + LINEAR-CUSP + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Let

\[
\mathfrak D(x)
:=
\sum_{k=1}^{\infty}
\frac{\|kx\|_{\mathbb Z}^{\,2}}{k^2},
\tag{1}
\]

where \(\|y\|_{\mathbb Z}\) is the distance from \(y\) to the nearest integer. Then

\[
\boxed{
\mathfrak D(h)
=
(\log 2)\,|h|+O(h^2)
}
\qquad(h\to0).
\tag{2}
\]

In particular, the critical exact-lattice profile of NB-332,

\[
\Phi(\delta)
=
-\frac{\mathfrak D(\delta)}{4\delta},
\qquad
\delta>0,
\tag{3}
\]

has a linear cusp at every positive integer. For every fixed \(L\in\mathbb N\),

\[
\boxed{
\Phi(L+\varepsilon)
=
-\frac{\log2}{4L}\,|\varepsilon|
+
O(\varepsilon^2)
}
\qquad(\varepsilon\to0).
\tag{4}
\]

Thus the integer zeros isolated by NB-332 are not flat zeros of the limiting adjacent-channel profile. A fixed nonzero perturbation of the limiting critical aspect ratio away from \(L\) restores the leading adjacent coefficient linearly in the distance to the node.

The statement is deliberately about the already-established limiting profile. It does not interchange the limits \(q\to\infty\) and \(\varepsilon\to0\), and therefore does not by itself control a coupled sequence \(d_q/q=L+\varepsilon_q\) with \(\varepsilon_q\to0\).

## 1. Rescale the series to one bounded-variation Riemann sum

For \(t>0\), define

\[
f(t):=\frac{\|t\|_{\mathbb Z}^{\,2}}{t^2},
\tag{5}
\]

and set \(f(0)=1\). This extension is continuous because
\(\|t\|_{\mathbb Z}=t\) on \(0\le t\le1/2\), so \(f=1\) there.

For \(h>0\),

\[
\mathfrak D(h)
=
h^2\sum_{k\ge1}f(kh)
=
h\left(
h\sum_{k\ge1}f(kh)
\right).
\tag{6}
\]

The useful point is that \(f\) has finite total variation on \([0,\infty)\). Put
\(d(t)=\|t\|_{\mathbb Z}\). Away from the harmless integer and half-integer
corners, \(d\) is differentiable with \(|d'(t)|=1\), and for \(t\ge1/2\),

\[
|f'(t)|
=
\left|
\frac{2d(t)d'(t)}{t^2}
-
\frac{2d(t)^2}{t^3}
\right|
\le
\frac1{t^2}
+
\frac1{2t^3},
\tag{7}
\]

because \(0\le d(t)\le1/2\). The right-hand side is integrable on
\([1/2,\infty)\), while \(f\) is constant on \([0,1/2]\). Hence

\[
V:=\operatorname{Var}_{[0,\infty)}(f)<\infty.
\tag{8}
\]

This gives a direct global Riemann-sum error. On each cell
\([(k-1)h,kh]\),

\[
\left|
h f(kh)-\int_{(k-1)h}^{kh}f(t)\,dt
\right|
\le
h\,\operatorname{Var}_{[(k-1)h,kh]}(f).
\tag{9}
\]

Summing the cell variations,

\[
\left|
h\sum_{k\ge1}f(kh)
-
\int_0^\infty f(t)\,dt
\right|
\le
Vh.
\tag{10}
\]

Therefore

\[
\mathfrak D(h)
=
h I+O(h^2),
\qquad
I:=
\int_0^\infty
\frac{\|t\|_{\mathbb Z}^{\,2}}{t^2}\,dt.
\tag{11}
\]

This step is the reason a termwise small-\(h\) expansion is unnecessary and, in
fact, misleading: the number of terms with \(kh=O(1)\) grows like \(1/h\).

## 2. The continuum coefficient is exactly \(\log 2\)

The integral in (11) can be evaluated cell by cell. On
\([n,n+1/2]\),

\[
\|t\|_{\mathbb Z}=t-n,
\]

while on \([n+1/2,n+1]\),

\[
\|t\|_{\mathbb Z}=n+1-t.
\]

For \(n\ge0\), direct integration gives

\[
\begin{aligned}
I_n
&:=
\int_n^{n+1}
\frac{\|t\|_{\mathbb Z}^{\,2}}{t^2}\,dt\\
&=
2
+
2n\log n
-
2(n+1)\log(n+1)
+
2\log\!\left(n+\frac12\right),
\end{aligned}
\tag{12}
\]

with \(0\log0:=0\). Hence

\[
\begin{aligned}
\sum_{n=0}^{N-1}I_n
&=
2N
-
2N\log N
+
2\sum_{n=0}^{N-1}\log\!\left(n+\frac12\right)\\
&=
2N
-
2N\log N
+
2\log\Gamma\!\left(N+\frac12\right)
-
2\log\Gamma\!\left(\frac12\right).
\end{aligned}
\tag{13}
\]

Stirling's formula and \(\Gamma(1/2)=\sqrt\pi\) give

\[
\log\Gamma\!\left(N+\frac12\right)
=
N\log N-N+\frac12\log(2\pi)+O(N^{-1}),
\tag{14}
\]

so (13) tends to

\[
\boxed{I=\log2}.
\tag{15}
\]

Combining (11) and (15) proves (2) for \(h>0\). Since
\(\mathfrak D(-h)=\mathfrak D(h)\), the same formula holds from both sides.

## 3. The integer zeros are cusps

The defining series is exactly one-periodic:

\[
\mathfrak D(x+L)=\mathfrak D(x)
\qquad(L\in\mathbb Z),
\tag{16}
\]

because \(kL\) is an integer for every \(k\). Therefore, for any fixed positive
integer \(L\),

\[
\mathfrak D(L+\varepsilon)
=
\mathfrak D(\varepsilon)
=
(\log2)|\varepsilon|+O(\varepsilon^2).
\tag{17}
\]

Substituting into (3) and using

\[
\frac1{L+\varepsilon}
=
\frac1L+O(\varepsilon)
\tag{18}
\]

yields (4). Equivalently, the one-sided slopes exist and satisfy

\[
\Phi'_-(L)=\frac{\log2}{4L},
\qquad
\Phi'_+(L)=-\frac{\log2}{4L}.
\tag{19}
\]

The node is therefore a downward linear cusp. The exact adjacent-channel
cancellation at \(\delta=L\) is destroyed at first order by displacement of the
limiting aspect ratio.

## 4. Boundary and adversarial checks

Several distinctions are load-bearing.

First, (2) is not obtained by replacing
\(\|kh\|_{\mathbb Z}\) with \(k|h|\) term by term. Such a replacement is valid
only before the nearest-integer folds and would produce a divergent term count.
The bounded-variation Riemann-sum argument controls all folds simultaneously and
gives the required \(O(h^2)\) remainder.

Second, periodicity is used only after the local expansion at zero is proved.
There is no assumption that \(\mathfrak D\) is differentiable at the integer
nodes; (19) shows precisely that it is not.

Third, NB-332 proves the \(q\to\infty\) critical profile for a fixed limiting
ratio \(\delta\). Combining that theorem with (4) is valid when one first fixes a
noninteger \(\delta=L+\varepsilon\) and then lets \(q\to\infty\). It does not
supply a uniform estimate when \(\varepsilon=\varepsilon_q\to0\). Resolving that
coupled boundary layer requires a two-parameter remainder estimate for the
finite-\(q\) coefficient.

Fourth, this result concerns displacement of the macroscopic ratio \(\delta\).
It does not contradict NB-333's separate off-lattice observation that, at the
exact integer ratio, moving through the bounded remainder phase leaves this same
adjacent channel at zero to leading order.

The closest audited classical literature concerns the multiplicative
autocorrelation of the fractional-part function. Báez-Duarte, Balazard,
Landreau and Saias study
\(A(\lambda)=\int_0^\infty\{t\}\{\lambda t\}t^{-2}\,dt\) and establish singular
local behavior at rational arguments; Balazard and Martin subsequently analyze
its differentiability through Bernoulli/divisor-series and continued-fraction
structure. That literature makes rational cusps in nearby fractional-part
objects unsurprising, but the proof above uses neither autocorrelation theorem
nor differentiability criterion. A targeted audit did not identify the exact
series (1) together with coefficient (15) as a stated theorem. No bibliographic
novelty is claimed.

Audit anchors:

- L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias,
  *Étude de l'autocorrélation multiplicative de la fonction partie
  fractionnaire*, Ramanujan J. 9 (2005), 215–240,
  DOI 10.1007/s11139-005-0834-4; arXiv:math/0306251.
- M. Balazard, B. Martin,
  *Sur l'autocorrélation multiplicative de la fonction partie fractionnaire et
  une fonction définie par J. R. Wilton*, arXiv:1305.4395.

No external result is load-bearing for (2)--(4), so SOURCES.md requires no new
dependency entry.

## Research consequence

NB-332 left positive integers as the exact zeros of the critical
Diophantine adjacent profile. This finding determines their local geometry:
they are isolated linear cusps with universal numerator coefficient \(\log2\),
not flat cancellation plateaux. Therefore every sufficiently small but fixed
nonzero displacement of the limiting critical aspect ratio restores an adjacent
coefficient of size

\[
\frac{\log2}{4L}|\varepsilon|+O(\varepsilon^2).
\tag{20}
\]

The remaining source-side question is sharper than simply asking whether the
integer node is stable. At fixed aspect ratio it is not stable under ratio
displacement, while NB-333 shows bounded remainder phase at the exact integer
ratio is still invisible to this channel. The unresolved regime is the coupled
boundary layer \(d_q/q=L+\varepsilon_q\), \(\varepsilon_q\to0\), together with
optimization over other admissible witnesses. A useful next theorem must compare
the linear cusp scale against the finite-\(q\) error rather than infer uniformity
from the pointwise profile.

The result remains source-side. It gives no target-occupation estimate, no
finite-section distance bound, and no RH implication by itself.
