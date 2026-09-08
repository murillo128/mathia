# AF-204 — Weighted Euler localization exactly calibrates varying-profile transfer

**Status:** `EXACT-DERIVED`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-RECOVERY`, `SOURCE-LOCALIZATION`, `ARITHMETIC-CONTROL`, `NO-NOVELTY-CLAIM`

## Claim

AF-201 identifies weak Peano-carrier concentration as the exact finite-band transfer topology when the quartic source profile `Q` stays two-sided bounded. AF-203 gives the stronger sufficient varying-profile gate `Q^2 W_1 -> 0`. The remaining varying-profile question has an exact answer at the level of the full fixed-band Euler transform.

Fix

\[
x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and write

\[
F_s(u)=-\log(1-e^{-su}),
\qquad
s=\sigma+i\tau,
\qquad |\tau|\le T,
\]

\[
g_\tau(u):=F_{\sigma+i\tau}^{(4)}(u).
\]

For a five-node quartic minimal-support control `nu=mu_+-mu_-` from AF-199, let

\[
\delta:=W_1(\mu_+,\mu_-)>0,
\qquad
Q:=\frac{\int u^4\,d\nu(u)}{\delta^4}>0,
\]

and let `beta` be its normalized positive Peano B-spline carrier. As in AF-201,

\[
E(\tau)
:=\frac1{\delta^4}\int F_{\sigma+i\tau}(u)\,d\nu(u)
=
\frac{Q}{24}\int g_\tau(v)\,d\beta(v).
\tag{1}
\]

Define the real-axis endpoint defect

\[
\Lambda_\sigma(\beta)
:=
1-
\frac{1}{g_0(x)}\int g_0(v)\,d\beta(v),
\qquad
 g_0(v)=F_\sigma^{(4)}(v)>0.
\tag{2}
\]

There is a finite constant `C=C(x,sigma,T)` such that every probability carrier `beta` supported on `[x,infinity)` satisfies

\[
\boxed{
\frac{g_0(x)}{24}\,Q\Lambda_\sigma(\beta)
\le
\sup_{|\tau|\le T}
\left|
E(\tau)-\frac{Q}{24}g_\tau(x)
\right|
\le
\frac{C g_0(x)}{24}\,Q\Lambda_\sigma(\beta).
}
\tag{3}
\]

The lower bound is exact at `tau=0`. Consequently, for an arbitrary sequence in which `Q_n` may vary without an a priori upper bound,

\[
\boxed{
\sup_{|\tau|\le T}
\left|
E_n(\tau)-\frac{Q_n}{24}g_\tau(x)
\right|
\longrightarrow0
\quad\Longleftrightarrow\quad
Q_n\Lambda_\sigma(\beta_n)\longrightarrow0.
}
\tag{4}
\]

Thus the intrinsic varying-profile resource is not weak localization alone and not the stronger first-moment quantity used in AF-200. It is **localization defect weighted by the surviving source profile**.

For the five-node quartic minimal-support source class this condition has an equally simple source-side form. Let

\[
D:=u_4-x
\]

be the anchored knot diameter. Then, for every sequence in this class,

\[
\boxed{
Q_n\Lambda_\sigma(\beta_n)\to0
\quad\Longleftrightarrow\quad
Q_nD_n\to0.
}
\tag{5}
\]

Hence the exact fixed-band varying-profile transfer gate is

\[
\boxed{Q_nD_n\to0.}
\tag{6}
\]

AF-203's condition `Q_n^2 delta_n -> 0` remains a useful purely profile/transport sufficient criterion because

\[
D_n\le3Q_n\delta_n
\quad\Longrightarrow\quad
Q_nD_n\le3Q_n^2\delta_n.
\tag{7}
\]

It is therefore a sufficient surrogate for the exact gate `(6)`, not the intrinsic transfer condition.

## Derivation

### 1. The real Euler defect dominates the whole fixed vertical band

AF-201 proves that

\[
g_0(v)=\sigma^4\sum_{k\ge1}k^3e^{-k\sigma v}
\]

is positive and strictly decreasing on `[x,infinity)`. Put

\[
h(v):=g_0(x)-g_0(v).
\tag{8}
\]

Then `h(x)=0`, `h(v)>0` for `v>x`, and

\[
g_0(x)\Lambda_\sigma(\beta)=\int h(v)\,d\beta(v).
\tag{9}
\]

AF-201 also establishes finite band constants

\[
M:=\sup_{v\ge x,\ |\tau|\le T}|g_\tau(v)|<\infty,
\qquad
L:=\sup_{v\ge x,\ |\tau|\le T}|g_\tau'(v)|<\infty.
\tag{10}
\]

On the compact interval `[x,x+1]`, strict negativity of `g_0'` gives

\[
m_0:=\min_{x\le w\le x+1}(-g_0'(w))>0.
\tag{11}
\]

For `x<=v<=x+1`, the mean-value estimates give

\[
|g_\tau(v)-g_\tau(x)|\le L(v-x),
\]

while

\[
h(v)=\int_x^v(-g_0'(w))\,dw\ge m_0(v-x).
\]

Therefore

\[
|g_\tau(v)-g_\tau(x)|
\le \frac{L}{m_0}h(v).
\tag{12}
\]

For `v>=x+1`, one instead has

\[
|g_\tau(v)-g_\tau(x)|\le2M
\]

and

\[
h(v)\ge h(x+1)>0,
\]

so

\[
|g_\tau(v)-g_\tau(x)|
\le
\frac{2M}{h(x+1)}h(v).
\tag{13}
\]

Thus with

\[
C:=\max\left\{
\frac{L}{m_0},
\frac{2M}{h(x+1)}
\right\}<\infty,
\tag{14}
\]

one has the pointwise domination

\[
\boxed{
|g_\tau(v)-g_\tau(x)|\le C h(v)
\qquad(v\ge x,\ |\tau|\le T).
}
\tag{15}
\]

This is the load-bearing step. The single positive real-axis defect is not merely a detector of weak concentration: on a fixed band it quantitatively dominates every complex fourth-derivative discrepancy in the family.

### 2. Weighted defect is necessary and sufficient

Using `(1)`, positivity of `beta`, `(15)`, and `(9)`,

\[
\begin{aligned}
\sup_{|\tau|\le T}
\left|
E(\tau)-\frac{Q}{24}g_\tau(x)
\right|
&\le
\frac{Q}{24}
\int
\sup_{|\tau|\le T}|g_\tau(v)-g_\tau(x)|
\,d\beta(v)\\
&\le
\frac{CQ}{24}\int h(v)\,d\beta(v)\\
&=
\frac{Cg_0(x)}{24}Q\Lambda_\sigma(\beta).
\end{aligned}
\tag{16}
\]

At `tau=0`, monotonicity makes the endpoint discrepancy nonnegative and AF-201's exact identity gives

\[
\frac{Q}{24}g_0(x)-E(0)
=
\frac{g_0(x)}{24}Q\Lambda_\sigma(\beta).
\tag{17}
\]

Since the band supremum is at least its value at `tau=0`, `(16)` and `(17)` prove the two-sided calibration `(3)`, hence the equivalence `(4)`.

This removes the bounded-profile hypothesis from the transfer characterization. The role of an upper bound on `Q` in AF-201 was only to let unweighted weak localization imply weighted localization. Once the defect is multiplied by `Q`, no separate profile bound is required.

### 3. In the quartic minimal-support class the weighted defect is exactly weighted diameter

AF-202 proves, for order `m=4`,

\[
\frac1{16}c(D/2)
\le
\Lambda_\sigma(\beta)
\le
c(D),
\qquad
c(r):=1-\frac{g_0(x+r)}{g_0(x)}.
\tag{18}
\]

The function `c` satisfies

\[
c(0)=0,
\qquad
c'(0)=-\frac{g_0'(x)}{g_0(x)}>0.
\tag{19}
\]

Hence there exist `D_0>0` and constants `a,b>0`, depending only on `x` and `sigma`, such that

\[
\boxed{
aD\le\Lambda_\sigma(\beta)\le bD
\qquad(0<D\le D_0).
}
\tag{20}
\]

To use this local comparison in both directions, first note that the source profile is uniformly bounded away from zero in this class. Since `mu_+` and `mu_-` are probabilities supported in an interval of diameter `D`,

\[
\delta=W_1(\mu_+,\mu_-)\le D.
\tag{21}
\]

AF-203 gives

\[
D\le3Q\delta.
\tag{22}
\]

Because `D>0`, `(21)` and `(22)` imply the universal lower bound

\[
\boxed{Q\ge\frac13.}
\tag{23}
\]

Now suppose `Q_n Lambda_sigma(beta_n)->0`. By `(23)`, `Lambda_sigma(beta_n)->0`; AF-202 then gives `D_n->0`. For all sufficiently large `n`, the lower half of `(20)` gives

\[
Q_nD_n\le a^{-1}Q_n\Lambda_\sigma(\beta_n)\to0.
\tag{24}
\]

Conversely, if `Q_nD_n->0`, `(23)` implies `D_n->0`; the upper half of `(20)` gives

\[
Q_n\Lambda_\sigma(\beta_n)
\le bQ_nD_n\to0.
\tag{25}
\]

This proves `(5)` and `(6)`.

## Consequence for the quartic localization frontier

The source/observation hierarchy is now exact for the full fixed-band profile:

- `D->0` is the unweighted localization topology forced by AF-202;
- bounded `Q` turns that topology into transfer, as AF-201 states;
- when `Q` varies, the exact condition is `QD->0`;
- `Q^2 delta->0` is a convenient sufficient condition supplied by AF-203 because it forces `QD->0`.

This also sharpens the interpretation of AF-200. Its mass-escape family fails because physical localization is absent, but a different varying-profile sequence could fail even with `D->0` if the surviving quartic profile grows quickly enough that `QD` does not vanish. The retained source amplitude and the localization scale must be declared together.

The remaining accepted clue question is therefore no longer the abstract transfer topology. It is whether a mathematically natural constrained source class or full-Euler optimization problem forces `QD->0` together with whatever projective compactness is needed to transfer optimizer identity. AF-200 already rules this out for unrestricted normalized full-Euler sublevels. Moreover, AF-201's warning remains: convergence of the scalar band supremum alone does not imply convergence of the entire band profile, so a minimizer theorem needs an additional argument rather than following automatically from `(4)`.

## Prior art and novelty assessment

The positive-measure mechanism behind `(15)`--`(17)` is classical in spirit. Korovkin-type approximation theory studies when positive linear operators or positive Radon-measure averages are controlled by a small family of test functions, and quantitative versions bound approximation errors by test-function defects and moduli of continuity. A standard broad reference is Francesco Altomare and Michele Campiti, *Korovkin-type Approximation Theory and Its Applications*, de Gruyter (1994), DOI `10.1515/9783110884586`; see also Francesco Altomare and Sabrina Diomede, “Positive operators and approximation in function spaces on completely regular spaces,” *International Journal of Mathematics and Mathematical Sciences* (2003), DOI `10.1155/S0161171203301206`, which explicitly treats positive operators represented by Borel measures.

AF-201 already audits weak convergence and the Peano-carrier representation against classical probability and spline/divided-difference theory. No novelty is claimed for positive linear functionals, weak concentration, Korovkin-type testing, modulus-of-continuity estimates, or the elementary fact that a strictly peaked positive test function can control mass away from its maximizer.

The durable result here is the exact specialization to the Arithmetic Fidelity Euler carrier: the one real fourth-derivative defect quantitatively calibrates the whole fixed complex band after multiplication by the surviving quartic profile, and the five-knot source geometry converts that weighted defect exactly into the asymptotic source condition `QD->0`. This closes the varying-profile transfer gate without claiming a new general approximation theory.

## Boundaries and falsification checks

- The full-band calibration fixes `x>0`, `sigma>0`, and finite `T`. Growing bandwidth, movement toward `sigma=0`, or a moving anchor can change the constants and requires a separate uniformity analysis.
- The upper bound uses positivity of the normalized Peano carrier and its support in `[x,infinity)`. A signed carrier or two-sided support around the anchor need not be controlled by the same one-sided real defect.
- Equation `(4)` concerns convergence of the **full band profile**. It does not claim that convergence of the scalar objective `sup_|tau| |E(tau)|` is sufficient for `Q Lambda->0`.
- The source equivalence `(5)` uses the fixed-order five-node minimal-support quartic class through AF-202 and AF-203. The observation-side calibration `(3)` is more general, but `QD` is not asserted to be the correct source variable for arbitrary carriers or higher/growing cancellation order.
- The universal bound `Q>=1/3` is only a corollary of the nonsharp AF-203 coercivity certificate and `delta<=D`; no sharp lower profile constant is claimed.
- The theorem does not establish compactness or existence of full-Euler minimizers, convergence to the homogeneous knot optimizer, rational-prime specificity, zero selection, or any RH implication.
