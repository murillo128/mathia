# AF-061 — Source `\ell^r` geometry shifts the fixed-base safe-lift critical exponent to `r`

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `1\le r<\infty`, equip

\[
X_r=\mathbb R^2
\]

with the `\ell^r` metric, and fix the symmetric two-point target

\[
S_a=\{(-a,0),(a,0)\},
\qquad a>0.
\tag{1}
\]

For `1\le p<\infty`, use the AF-057 product refinement

\[
Y_{p,r}=X_r\times\mathbb R,
\qquad
C(x)=(x,0),
\]

with

\[
D_{p,r}((x,h),(x',h'))
=
\left(\|x-x'\|_r^p+|h-h'|^p\right)^{1/p}.
\tag{2}
\]

At the midpoint base `m=0`, define the powered far-field defect

\[
\Delta_{p,r}
=
\sup_{x\in X_r}
\left(
 d_r(x,S_a)^p-\|x\|_r^p
\right).
\tag{3}
\]

Then:

1. **The exact critical exponent is the source exponent `r`.** One has
   \[
   \boxed{
   \Delta_{p,r}
   =
   \begin{cases}
   a^p, & 1\le p\le r,\\[1mm]
   +\infty, & p>r.
   \end{cases}
   }
   \tag{4}
   \]
   Consequently, by AF-057,
   \[
   \boxed{
   (0,h)\in\mathcal E_C(S_a)
   \iff
   |h|\ge a
   \qquad(1\le p\le r),
   }
   \tag{5}
   \]
   whereas for `p>r` no finite vertical lift exists above the midpoint.

2. **The max-product endpoint also fails.** If
   \[
   D_{\infty,r}((x,h),(x',h'))
   =
   \max\{\|x-x'\|_r,|h-h'|\},
   \tag{6}
   \]
   then no finite `(0,h)` is safe.

3. **A general power-gap amplification principle explains the obstruction.** Let `(X,d)` be any metric space, let `S\subseteq X` be nonempty, let `m\in X`, and suppose that for some `\rho\ge1`, `c>0`, and a sequence `x_n` with
   \[
   d(x_n,m)\to\infty
   \]
   one has
   \[
   d(x_n,S)^\rho-d(x_n,m)^\rho\ge c
   \qquad\forall n.
   \tag{7}
   \]
   Then for every `p>\rho`,
   \[
   \boxed{
   \sup_x\left(d(x,S)^p-d(x,m)^p\right)=+\infty.
   }
   \tag{8}
   \]
   Thus an order-one far-field gap at power `\rho` becomes an unbounded defect after any super-`\rho` powering.

4. **The Euclidean `p=2` transition of AF-057 and AF-059 is therefore not universal.** It is exactly the `r=2` member of (4). For `r=1`, every product exponent `p>1` already fails at the midpoint; for larger finite `r`, the same two-point target remains finitely liftable through all `p\le r`.

5. **Even with the product exponent frozen at `p=2`, an arbitrarily small source renorming can cross the fixed-base existence boundary.** For `1\le r<2`, on the common vector space `\mathbb R^2`,
   \[
   \|z\|_2
   \le
   \|z\|_r
   \le
   K_r\|z\|_2,
   \qquad
   K_r=2^{\frac1r-\frac12},
   \tag{9}
   \]
   and `K_r\downarrow1` as `r\uparrow2`. The corresponding `p=2` product metrics satisfy
   \[
   D_{2,2}\le D_{2,r}\le K_rD_{2,2}.
   \tag{10}
   \]
   Nevertheless, at `r=2` finite midpoint lifts exist, while for every `r<2` equation (4) gives `2>r` and hence no finite midpoint lift. Therefore for every `\varepsilon>0` there is a source norm and product metric globally `(1+\varepsilon)`-bi-Lipschitz close to the Euclidean one for which the same fixed-base lift statement has the opposite truth value.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{the safe-lift critical exponent is not attached to the target alone;}\\
\text{it is set by the interaction between powering and the source's far-field geometry.}
\end{array}
}
\tag{11}
\]

This sharpens the representation warning in AF-057--AF-060. A threshold observed in one metric presentation cannot be promoted to an intrinsic fidelity law until the source metric category, not merely the target and the refinement syntax, has been fixed.

## Derivation

### Exact `\ell^r` distance to the symmetric target

Write `x=(u,v)`. Since the two target points differ only in the first coordinate,

\[
\begin{aligned}
 d_r(x,S_a)^r
 &=
 |v|^r+
 \min\{|u-a|^r,|u+a|^r\}\\
 &=
 |v|^r+\bigl||u|-a\bigr|^r.
\end{aligned}
\tag{12}
\]

For nonnegative `s,t`, one has `|s-t|\le\max\{s,t\}`, hence

\[
|s-t|^r\le s^r+t^r.
\tag{13}
\]

Applying this to `s=|u|`, `t=a` gives

\[
\boxed{
 d_r(x,S_a)^r
 \le
 \|x\|_r^r+a^r.
 }
\tag{14}
\]

The bound is exact at the midpoint `x=0`.

### Subcritical and critical powers

Assume `1\le p\le r` and put

\[
q=\frac pr\in(0,1].
\]

The map `t\mapsto t^q` is subadditive on `\mathbb R_+`, so from (14),

\[
\begin{aligned}
 d_r(x,S_a)^p
 &\le
 \left(\|x\|_r^r+a^r\right)^{p/r}\\
 &\le
 \|x\|_r^p+a^p.
\end{aligned}
\tag{15}
\]

Therefore every term in (3) is at most `a^p`. At `x=0`,

\[
d_r(0,S_a)^p-0=a^p,
\tag{16}
\]

so the supremum is exactly `a^p`. This proves the finite branch of (4), and AF-057's exact product criterion immediately gives (5).

At `p=r`, no concavity slack is used: equation (14) itself is precisely the required powered-distance estimate. The equality case therefore identifies the transition point without an asymptotic argument.

### Supercritical powers diverge at infinity

For `p>r`, inspect the perpendicular ray

\[
x_t=(0,t),
\qquad t>0.
\]

Equation (12) gives

\[
d_r(x_t,S_a)^r=t^r+a^r,
\qquad
\|x_t\|_r=t.
\tag{17}
\]

Hence the powered defect on this ray is

\[
(t^r+a^r)^{p/r}-t^p.
\tag{18}
\]

Let `\alpha=p/r>1`. By the mean-value theorem applied to `s\mapsto s^\alpha`, for some `\xi_t\in(t^r,t^r+a^r)`,

\[
(t^r+a^r)^\alpha-(t^r)^\alpha
=
\alpha a^r\xi_t^{\alpha-1}.
\tag{19}
\]

Because `\alpha-1>0`, the right-hand side tends to `+\infty`. Thus `\Delta_{p,r}=+\infty`, proving the supercritical branch of (4).

The same calculation exhibits the asymptotic scale

\[
(t^r+a^r)^{p/r}-t^p
\sim
\frac pr a^r t^{p-r}.
\tag{20}
\]

The exponent `p-r` makes explicit why the transition occurs at `p=r`.

### General power-gap amplification

For (7)--(8), put

\[
b_n=d(x_n,m)^\rho\to\infty,
\qquad
\alpha=\frac p\rho>1.
\]

Then

\[
d(x_n,S)^p-d(x_n,m)^p
\ge
(b_n+c)^\alpha-b_n^\alpha.
\tag{21}
\]

Again by the mean-value theorem,

\[
(b_n+c)^\alpha-b_n^\alpha
=
\alpha c\eta_n^{\alpha-1}
\]

for some `\eta_n\in(b_n,b_n+c)`. Since `\eta_n\to\infty`, the right-hand side diverges. This proves (8).

For the `\ell^r` two-point model, (17) gives the stronger exact relation

\[
d_r(x_t,S_a)^r-d_r(x_t,0)^r=a^r
\qquad\forall t,
\tag{22}
\]

so the general lemma applies with `\rho=r` and `c=a^r`. The supercritical obstruction is therefore not an isolated coordinate trick: it is the canonical amplification of a persistent lower-power far-field gap.

### Max-product failure

For a finite height `h`, choose `t>|h|`. Then

\[
D_{\infty,r}(C(x_t),(0,h))=t,
\tag{23}
\]

while

\[
d_r(x_t,S_a)=(t^r+a^r)^{1/r}>t.
\tag{24}
\]

Thus the safe inequality fails for every finite `h`.

### Near-isometric source renorming at fixed product power

For `1\le r<2`, standard finite-dimensional norm comparison gives (9). Consequently

\[
\begin{aligned}
D_{2,r}((x,h),(x',h'))^2
&=\|x-x'\|_r^2+|h-h'|^2\\
&\le K_r^2\|x-x'\|_2^2+|h-h'|^2\\
&\le K_r^2D_{2,2}((x,h),(x',h'))^2,
\end{aligned}
\]

while the lower inequality follows from `\|z\|_2\le\|z\|_r`. This proves (10).

At the Euclidean endpoint `r=2`, equation (4) gives `\Delta_{2,2}=a^2`, hence the midpoint fiber contains all heights `|h|\ge a`. For every `r<2`, the same product power is supercritical and the defect is infinite. Since `K_r\to1`, the flip occurs under arbitrarily small multiplicative distortion.

Unlike AF-060, this comparison deliberately changes the **source metric** together with the ambient product metric. It therefore establishes a different instability: even when the refinement rule and its exponent are held fixed, the source representation itself can move the system across the far-field threshold.

## Exact controls

### AF-057 is recovered exactly at `r=2`

Putting `r=2` in (12)--(20) reproduces the AF-057 two-point Euclidean theorem:

\[
\Delta_{p,2}=a^p
\quad(1\le p\le2),
\qquad
\Delta_{p,2}=+\infty
\quad(p>2).
\tag{25}
\]

Thus the present result does not contradict or replace that finding; it identifies which part of its threshold came from Euclidean source geometry.

### The `r=1` endpoint kills every nonlinear power

For the `\ell^1` source,

\[
d_1((0,t),S_a)=t+a,
\]

so every `p>1` produces

\[
(t+a)^p-t^p\to+\infty.
\]

Only `p=1` remains finite, exactly as (4) predicts. This rules out an interpretation in which `2` is privileged merely because the lift adds one extra coordinate.

### Global safe-envelope existence remains trivial

For every `r` and `p`, the source embedding is isometric for its declared source metric, so AF-054 and AF-060 still give

\[
C(S_a)\subseteq\mathcal E_C(S_a).
\tag{26}
\]

The theorem concerns only the distinguished midpoint fiber. It does not claim that the global safe envelope disappears.

### The source-renorming comparison changes exactly what it says

In (9)--(10), the underlying points, target coordinates, base point, vertical coordinate, and product exponent are fixed, but the source norm changes from `\ell^2` to `\ell^r`. Therefore this is not a counterexample to invariance under harmless coordinate relabeling. It shows that metric data which are bi-Lipschitz close but not isometric can change an exact constant-`1` fidelity condition.

## Prior art and novelty assessment

The ingredients are classical and no novelty is claimed for `\ell^p` norm comparison, uniform convexity, coapproximation, or the elementary power inequalities used above.

- Olof Hanner, **“On the Uniform Convexity of `L^p` and `\ell^p`,”** *Arkiv för Matematik* 3(3), 239–244 (1956), DOI `10.1007/BF02589410`. Role: classical `L^p/\ell^p` geometry and exponent-sensitive norm structure; neighboring background rather than a source of the exact safe-lift formula.
- V. Westphal, **“Cosuns in `l_p(n)`, `1\le p<\infty`,”** *Journal of Approximation Theory* 54 (1988), 287–305. Role: direct classical evidence that coapproximation geometry depends materially on the ambient `p`-norm even in finite dimensions; already part of the AF-057 audit.
- T. D. Narang and S. P. Singh, **“Best Coapproximation in Metric Linear Spaces,”** *Tamkang Journal of Mathematics* 30(4), 241–252 (1999), DOI `10.5556/j.tkjm.30.1999.4198`. Role: established metric-dependent coapproximation framework; prevents treating metric sensitivity of safe/coapproximation-type sets as a new paradigm.

A targeted literature search across finite-dimensional `\ell^p` coapproximation, metric coapproximation, and classical `L^p/\ell^p` geometry found strong prior art for **norm-dependent approximation geometry**, but did not identify the exact AF-057 powered far-field quantity (3) or the formula (4) as a standard named theorem. That absence is not used as evidence of novelty. The durable contribution here is a Mathia-specific structural classification and falsification control: it proves exactly that the Euclidean critical exponent was representation-dependent and isolates the persistent lower-power far-field gap that causes the phase transition.

## Boundaries and failure modes

- Equation (4) is specific to the symmetric two-point target in `\mathbb R^2` with the `\ell^r` source norm and the exact AF-057 `\ell^p` product refinement. It does not classify arbitrary Banach spaces, arbitrary finite targets, or nonlinear refinements.
- The power-gap lemma (7)--(8) is a one-way obstruction. It proves super-`\rho` divergence from a persistent `\rho`-power gap; it does not prove finiteness for `p\le\rho` without an independent global upper bound such as (14).
- The near-isometric comparison changes the source metric as well as the ambient product metric. AF-060 remains the stronger statement when the source metric must stay exactly fixed.
- Exact safe-lift inequalities use constant `1`; bi-Lipschitz equivalence need not preserve them. The instability therefore does not contradict topological or coarse geometric equivalence.
- The theorem is about fixed-base/fiber-constrained existence. Global safe-envelope nonemptiness remains automatic by (26).
- Nothing here distinguishes rational primes or implies RH. Its role is to determine which parts of a proposed discriminator are intrinsic before arithmetic specialization.

## Consequence for the Arithmetic Fidelity frontier

AF-057 discovered a `p=2` phase transition for a two-point Euclidean source, AF-059 extended the Euclidean classification to compact targets, and AF-060 showed that the resulting fixed-base existence can be unstable under near-isometric ambient renorming. Equation (4) now shows that the value `2` itself was not intrinsic: it was the source exponent.

The next reusable quantity is therefore not a preferred product exponent but the **far-field contact order** between the target-distance function and the base-distance function. Equation (7) supplies an exact obstruction test: once a positive gap survives at some power `\rho` along an escaping family, every higher powered compression amplifies that residual into infinite repair cost.

For future arithmetic or geometric applications, a proposed lift should therefore declare and justify the metric/asymptotic category strongly enough to control this contact order. Otherwise a threshold or recovery statement may describe the chosen representation rather than a property of the discriminator being transported.