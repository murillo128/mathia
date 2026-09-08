# AF-201 — Weak Peano-carrier concentration is the exact bounded-profile Euler transfer gate

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-CONTROL`, `SOURCE-LOCALIZATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-199 represents every five-node minimal-support quartic moment-flat control by a positive normalized Peano B-spline carrier, while AF-200 bounds the error of replacing the carrier average by the left-endpoint derivative using the first moment of that carrier. The first-moment condition is sufficient, but it is stronger than the topology actually seen by a fixed finite Euler band.

Fix

\[
x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and let

\[
F_s(u)=-\log(1-e^{-su}),\qquad s=\sigma+i\tau,
\qquad |\tau|\le T.
\tag{1}
\]

For each index `n`, let

\[
\nu_n=\mu_{n,+}-\mu_{n,-}
\]

be an AF-199 quartic minimal-support control on five ordered knots

\[
x=u_{0,n}<u_{1,n}<\cdots<u_{4,n},
\]

with moments through degree three equal and

\[
\delta_n:=W_1(\mu_{n,+},\mu_{n,-})>0.
\]

Let

\[
\beta_n(dv):=B_n(v)\,dv
\]

be its normalized Peano B-spline probability carrier and define the positive homogeneous source profile

\[
Q_n:=\frac{\int u^4\,d\nu_n(u)}{\delta_n^4}>0.
\tag{2}
\]

Then AF-199 gives the exact identity

\[
\boxed{
E_n(\tau)
:=\frac1{\delta_n^4}\int F_{\sigma+i\tau}(u)\,d\nu_n(u)
=
\frac{Q_n}{24}
\int g_\tau(v)\,d\beta_n(v),
}
\tag{3}
\]

where

\[
g_\tau(v):=F_{\sigma+i\tau}^{(4)}(v).
\tag{4}
\]

On the fixed half-plane edge and finite band, set

\[
M:=\sup_{v\ge x,\ |\tau|\le T}|g_\tau(v)|<\infty,
\qquad
L:=\sup_{v\ge x,\ |\tau|\le T}|g_\tau'(v)|<\infty.
\tag{5}
\]

Then every carrier satisfies the sharper uniform transfer bound

\[
\boxed{
\sup_{|\tau|\le T}
\left|
E_n(\tau)-\frac{Q_n}{24}g_\tau(x)
\right|
\le
\frac{Q_n}{24}
\int \min\{2M,L(v-x)\}\,d\beta_n(v).
}
\tag{6}
\]

Thus no first moment is intrinsically required: the finite-band Euler family sees the carrier through a bounded localization gauge.

There is an exact one-scalar localization diagnostic internal to the real Euler kernel. Since

\[
g_0(v)
=F_\sigma^{(4)}(v)
=\sigma^4\sum_{k\ge1}k^3e^{-k\sigma v}
\tag{7}
\]

is positive and strictly decreasing on `[x,\infty)`, define

\[
\boxed{
\Lambda_\sigma(\beta)
:=
1-
\frac{1}{g_0(x)}\int g_0(v)\,d\beta(v)
\in[0,1].
}
\tag{8}
\]

For every `r>0`, writing

\[
c_r
:=
1-\frac{g_0(x+r)}{g_0(x)}>0,
\tag{9}
\]

one has the exact tail control

\[
\boxed{
\beta([x+r,\infty))
\le
\frac{\Lambda_\sigma(\beta)}{c_r}.
}
\tag{10}
\]

Consequently, for any sequence of Peano carriers supported on `[x,\infty)`,

\[
\boxed{
\Lambda_\sigma(\beta_n)\to0
\quad\Longleftrightarrow\quad
\beta_n\Rightarrow\delta_x
}
\tag{11}
\]

where `=>` denotes weak convergence of probability measures.

Combining `(6)` and `(10)` gives, for every fixed `r>0`,

\[
\boxed{
\sup_{|\tau|\le T}
\left|
E_n(\tau)-\frac{Q_n}{24}g_\tau(x)
\right|
\le
\frac{Q_n}{24}
\left(
Lr+
2M\frac{\Lambda_\sigma(\beta_n)}{c_r}
\right).
}
\tag{12}
\]

This identifies the exact bounded-profile localization topology. If

\[
\sup_nQ_n<\infty
\tag{13}
\]

and

\[
\beta_n\Rightarrow\delta_x,
\tag{14}
\]

then

\[
\boxed{
\sup_{|\tau|\le T}
\left|
E_n(\tau)-\frac{Q_n}{24}g_\tau(x)
\right|
\longrightarrow0.
}
\tag{15}
\]

Conversely, if

\[
\inf_nQ_n>0
\tag{16}
\]

and `(15)` holds, then `(14)` must hold. Indeed, at the real point `\tau=0`,

\[
\boxed{
\frac{Q_n}{24}g_0(x)\Lambda_\sigma(\beta_n)
=
\frac{Q_n}{24}g_0(x)-E_n(0),
}
\tag{17}
\]

and the right-hand side is nonnegative. Thus a positive lower profile bound forces `\Lambda_\sigma(\beta_n)\to0`, hence weak concentration by `(11)`.

Therefore, on any source class with

\[
0<q_-\le Q_n\le q_+<\infty,
\tag{18}
\]

**weak convergence of the Peano carrier to the fixed endpoint is equivalent to uniform finite-band transfer from the full Euler transform to its homogeneous quartic endpoint model.**

The scalar fixed-band objective inherits the same sufficient transfer. If

\[
D_{T,n}:=\sup_{|\tau|\le T}
\left|\int F_{\sigma+i\tau}\,d\nu_n\right|,
\qquad
M_4(x):=\sup_{|\tau|\le T}|g_\tau(x)|,
\]

then `(15)` implies

\[
\boxed{
\left|
\frac{D_{T,n}}{\delta_n^4}
-
\frac{Q_n}{24}M_4(x)
\right|
\longrightarrow0.
}
\tag{19}
\]

No converse is claimed from the scalar supremum alone, because equality of supremum norms need not identify the whole band profile.

## Derivation

### 1. The exact Peano representation isolates the only approximation step

For `m=4`, AF-199 gives

\[
\int f(u)\,d\nu_n(u)
=
\frac{\int u^4\,d\nu_n(u)}{24}
\int f^{(4)}(v)\,d\beta_n(v).
\tag{20}
\]

Substituting `f=F_s` and `(2)` yields `(3)` exactly. The question is therefore not whether a Taylor formula exists, but when the positive probability average of `g_\tau` over `\beta_n` can be replaced uniformly by its value at the anchored endpoint `x`.

The series

\[
F_s(u)=\sum_{k\ge1}\frac{e^{-ksu}}k
\tag{21}
\]

converges absolutely for `u\ge x>0` and `\Re s=\sigma>0`. Termwise differentiation gives

\[
g_\tau(u)=s^4\sum_{k\ge1}k^3e^{-ksu},
\qquad
 g_\tau'(u)=-s^5\sum_{k\ge1}k^4e^{-ksu}.
\tag{22}
\]

Since `|s|` is bounded on the finite vertical band, the exponentially convergent majorants at `u=x` prove `(5)`.

For every `v\ge x`, the mean-value estimate and the uniform bound give simultaneously

\[
|g_\tau(v)-g_\tau(x)|\le L(v-x),
\qquad
|g_\tau(v)-g_\tau(x)|\le2M.
\tag{23}
\]

Integrating the minimum of the two bounds against the positive probability measure `\beta_n` and using `(3)` proves `(6)`.

### 2. One real Euler derivative detects endpoint weak concentration

At `\tau=0`, `(22)` becomes `(7)`. Every term is positive and strictly decreasing, and

\[
g_0'(v)
=-\sigma^5\sum_{k\ge1}k^4e^{-k\sigma v}<0.
\tag{24}
\]

Thus `g_0(x)` is the unique maximum of `g_0` on the common support half-line `[x,\infty)`. For any probability measure `\beta` on that half-line,

\[
\begin{aligned}
g_0(x)-\int g_0\,d\beta
&=
\int\bigl(g_0(x)-g_0(v)\bigr)\,d\beta(v)\\
&\ge
\bigl(g_0(x)-g_0(x+r)\bigr)
\beta([x+r,\infty)).
\end{aligned}
\tag{25}
\]

Dividing by `g_0(x)` gives `(10)`.

If `\Lambda_\sigma(\beta_n)\to0`, `(10)` shows that for every `r>0` the mass outside `[x,x+r)` tends to zero. This is exactly convergence in probability to the constant `x`, hence weak convergence to `\delta_x`. Conversely, weak convergence to `\delta_x` implies convergence of the integral of the bounded continuous function `g_0/g_0(x)` to `1`, which is `(8)` tending to zero. This proves `(11)`.

### 3. Weak concentration is enough for the whole finite band

Split the bounded gauge in `(6)` at `x+r`. On `[x,x+r)`, it is at most `Lr`; on the tail it is at most `2M`. Equation `(10)` then gives `(12)`.

Assume `(13)` and `(14)`. By `(11)`, `\Lambda_\sigma(\beta_n)\to0`. Given `\varepsilon>0`, first choose `r>0` so that `q_+Lr/24<\varepsilon/2`, then use `(12)` and `(9)` to choose `n` large enough that the tail term is below `\varepsilon/2`. This proves `(15)`.

For the reverse implication under `(16)`, evaluate the transfer error at `\tau=0`. Equation `(3)` and definition `(8)` give `(17)`. Since `Q_n\ge q_->0`, uniform transfer forces `\Lambda_\sigma(\beta_n)\to0`, and `(11)` again gives weak concentration.

Finally, the elementary inequality

\[
\left|
\sup_\tau|a_\tau|-\sup_\tau|b_\tau|
\right|
\le
\sup_\tau|a_\tau-b_\tau|
\tag{26}
\]

applied to `(15)` proves `(19)`.

## Consequence for the localization frontier

AF-200's first-moment estimate used

\[
\sup_\tau
\left|
\int g_\tau\,d\beta-g_\tau(x)
\right|
\le
L\,W_1(\beta,\delta_x).
\tag{27}
\]

That remains useful, but `(6)`--`(12)` show that it is not the intrinsic finite-band topology. The Euler derivative family is uniformly bounded as well as uniformly Lipschitz, so far-away carrier mass is penalized only by its mass once it leaves the local Lipschitz scale. For bounded `Q`, **weak endpoint concentration is enough even when the first carrier moment is not controlled**.

This changes the live localization question. One should not search for the strongest convenient equicoercive moment condition and mistake it for necessity. The observation-side transfer problem is already classified on bounded `Q` profiles by `(11)`--`(18)`. What remains is source-side: identify a natural condition on unrestricted five-knot controls, or on sublevel sets of the full Euler objective, that forces both a finite upper `Q` budget and weak Peano concentration. AF-200 shows that `W_1(\mu_+,\mu_-)` alone does neither: its mass-escape family can keep the source separation fixed while the full Euler objective collapses and the homogeneous profile becomes irrelevant.

The lower bound in `(18)` is needed only for the converse. If `Q_n\to0`, the endpoint model itself vanishes and uniform transform agreement can occur without localizing the carrier. This is another reason to state localization together with the retained source profile rather than as an absolute property of the compression.

## Prior art and novelty assessment

The Peano B-spline representation is classical and was already audited in AF-199 against Carl de Boor, **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46–69, including the Peano-kernel/divided-difference bridge.

Weak convergence of probability measures through bounded continuous test functions, and its metrization by bounded-Lipschitz/Fortet-Mourier type distances on metric spaces, are standard probability theory; see Patrick Billingsley, ***Convergence of Probability Measures***, 2nd ed., Wiley (1999), Chapter 1, DOI `10.1002/9780470316962`, and the classical weak-topology literature. The implication from weak convergence to uniform control of this particular finite-band family is also an elementary specialization of uniformly bounded equicontinuous test-family arguments.

No novelty is claimed for weak convergence, tightness, bounded-Lipschitz metrics, Peano kernels, or the fact that a bounded strictly maximized test function can detect concentration at its unique maximizer. The durable Arithmetic Fidelity result is the exact specialization to the AF quartic Euler carrier: the real-axis fourth derivative supplies the explicit scalar defect `(8)` and tail certificate `(10)`, while `(12)` makes that same defect sufficient for uniform complex-band transfer under a declared `Q` budget. This replaces AF-200's stronger first-moment gate by the exact weak-localization topology for bounded homogeneous profiles.

## Boundaries and falsification checks

- The common left endpoint `x` and support restriction `\operatorname{supp}\beta_n\subset[x,\infty)` are essential to the one-scalar converse. If carrier mass may lie on both sides of `x`, the average of one strictly monotone test can equal its value at `x` by compensation without concentration.
- `\sigma>0` and finite `T` are essential to the uniform bounded/Lipschitz constants in `(5)`. Growing vertical bandwidth is a different problem and may require stronger localization.
- The upper `Q` bound is essential for weak concentration alone to imply the weighted transfer `(15)`. The lower `Q` bound is essential only for the reverse implication.
- Equation `(19)` is one-way. Agreement of the scalar supremum objective does not by itself imply agreement of the full band transform.
- Weak carrier concentration is weaker than first-moment convergence in the ambient probability-measure space. This finding does not claim that every such weakly concentrating probability sequence is realizable by five-knot Peano splines, nor that the two notions are strictly separated inside the exact five-knot source class.
- The theorem does not prove compactness of full-Euler minimizers, boundedness of their `Q` profiles, convergence to the homogeneous knot optimizer, rational-prime specificity, or any RH consequence.

## Decisive next test

The remaining source-class question is now precise: characterize the five-knot projective sublevel geometry for which low full-Euler discrepancy forces a bounded `Q` profile and `\Lambda_\sigma(\beta)\to0`. A positive result would turn `(18)` into the missing Gamma/minimizer-transfer gate; a counterexample with bounded `Q` but nonlocalizing Peano carriers and anomalously small full objective would show that still more source information is required.