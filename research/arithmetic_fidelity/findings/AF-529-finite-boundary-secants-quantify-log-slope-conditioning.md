# AF-529 — Finite boundary secants quantify log-slope conditioning

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CARRIER-SHAPE` · `FINITE-RESOLUTION` · `CONDITIONING` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

Keep the co-tuned anchored outward-tail controls and exact carrier ratio of AF-527/AF-528. Thus, for fixed \(\theta\in(0,1)\),

\[
B_A=\lfloor A^\theta\rfloor,
\qquad
L_A=\log A,
\qquad
H_A=\log L_A,
\]

with \(C_A,\widetilde C_A\) chosen exactly as in AF-527, and

\[
R_A(t)
=
\frac{\widetilde C_A^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A,t)}{B_0(A,t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t}.
\]

AF-528 proved the infinitesimal recovery law

\[
\frac{H_A}{L_A}(\log R_A)'(0)\longrightarrow1-\theta.
\]

The same law is uniform across the full AF-527 physical boundary layer \(0\le t\le A^{-1}\):

\[
\boxed{
\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}(\log R_A)'(t)-(1-\theta)
\right|
\longrightarrow0.
}
\tag{1}
\]

Consequently, for

\[
F_A(u)=\log R_A(u/A)-\log R_A(0),
\qquad 0\le u\le1,
\]

one has the uniform finite-window law

\[
\boxed{
\sup_{0\le u\le1}
\left|
\frac{A H_A}{L_A}F_A(u)-u(1-\theta)
\right|
\longrightarrow0.
}
\tag{2}
\]

In particular,

\[
\log\frac{R_A(1/A)}{R_A(0)}
=
(1-\theta)\frac{L_A}{A H_A}
+o\!\left(\frac{L_A}{A H_A}\right).
\tag{3}
\]

Thus AF-528's derivative lift is **asymptotically identifiable but severely conditioned at finite boundary resolution**. The order-\(L_A/H_A\) infinitesimal slope becomes only an order

\[
\boxed{\frac{\log A}{A\log\log A}}
\]

relative log-change across the entire natural window of width \(1/A\).

For the direct two-sample observation of \(\log R_A(0)\) and \(\log R_A(u/A)\), fixed \(u>0\), additive observation errors bounded by \(\varepsilon_A\) give the estimator

\[
\widehat\theta_A
=
1-
\frac{A H_A}{uL_A}
\bigl(Y_A(u/A)-Y_A(0)\bigr),
\tag{4}
\]

with

\[
|\widehat\theta_A-\theta|
\le o(1)
+
\frac{2A H_A}{uL_A}\,\varepsilon_A.
\tag{5}
\]

Hence

\[
\varepsilon_A=o\!\left(\frac{L_A}{A H_A}\right)
\tag{6}
\]

is sufficient for consistent recovery through this finite secant channel. Conversely, at this two-sample observation level, bounded adversarial errors on the same scale as \(L_A/(A H_A)\) can mask an order-one change in \(\theta\). This is a conditioning statement for the declared observable, not a minimax impossibility theorem for every possible lift of the full carrier family.

## Derivation

### 1. Exact logarithmic derivative

Define

\[
M_1(X,t)=\sum_{p\le X}(\log p)p^{-1-t},
\qquad
\mu_X(t)=\frac{M_1(X,t)}{B_0(X,t)}.
\]

Also set

\[
g_t(C)
=
\partial_t\log(C^{1+t}-1)
=
\frac{C^{1+t}\log C}{C^{1+t}-1}.
\]

Exact differentiation of the finite expression for \(R_A\) gives

\[
(\log R_A)'(t)
=
 g_t(\widetilde C_A)-g_t(C_A)
+
\mu_A(t)-\mu_{B_A}(t).
\tag{7}
\]

The sign in the prime-moment term comes from

\[
\partial_t\log B_0(X,t)=-\mu_X(t).
\]

Thus the finite-resolution question reduces to uniform control of the multiplier term and of the first logarithmic prime moments on \(0\le t\le A^{-1}\).

### 2. The prime-moment term is uniform on the shrinking window

Write

\[
S(X)=B_0(X,0)=\sum_{p\le X}\frac1p,
\qquad
M_1(X)=M_1(X,0).
\]

The classical Mertens estimates used in AF-528 are

\[
S(X)=\log\log X+B_1+O(1/\log X),
\tag{8}
\]

and

\[
M_1(X)=\log X+O(1).
\tag{9}
\]

For \(0\le t\le A^{-1}\), the elementary inequality \(0\le1-e^{-y}\le y\) gives

\[
0\le S(X)-B_0(X,t)
\le tM_1(X)
\tag{10}
\]

for \(X\le A\). Therefore

\[
B_0(X,t)=S(X)+O\!\left(\frac{\log X}{A}\right)
\tag{11}
\]

uniformly on the window.

For the numerator, let

\[
M_2(X)=\sum_{p\le X}\frac{(\log p)^2}{p}.
\]

Since \(\log p\le\log X\), equation (9) already gives the sufficient bound

\[
M_2(X)\le (\log X)M_1(X)=O((\log X)^2).
\tag{12}
\]

Again using \(1-e^{-y}\le y\),

\[
0\le M_1(X)-M_1(X,t)
\le tM_2(X)
=O\!\left(\frac{(\log X)^2}{A}\right).
\tag{13}
\]

For \(X=A\), equations (8)--(13) imply uniformly for \(0\le t\le A^{-1}\),

\[
\frac{H_A}{L_A}\mu_A(t)\longrightarrow1.
\tag{14}
\]

For \(X=B_A\), use

\[
L_B=\theta L_A+o(1),
\qquad
H_B=H_A+\log\theta+o(1),
\tag{15}
\]

and the same estimates, noting that the observation width is still \(A^{-1}\), which is smaller than the natural \(B_A^{-1}\) scale. Hence uniformly on the same window,

\[
\frac{H_A}{L_A}\mu_{B_A}(t)\longrightarrow\theta.
\tag{16}
\]

Subtracting (16) from (14),

\[
\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}
\bigl(\mu_A(t)-\mu_{B_A}(t)\bigr)
-(1-\theta)
\right|
\to0.
\tag{17}
\]

No short-interval prime theorem is used here. The window is in the exponent variable \(t\), while the prime cutoff remains the full interval \(p\le X\); the uniformity follows from elementary moment domination once the classical Mertens sums are known.

### 3. Co-tuned multipliers remain negligible uniformly

The multiplier derivative has the exact form

\[
g_t(C)=\frac{\log C}{1-C^{-(1+t)}}.
\tag{18}
\]

For \(t\ge0\), uniformly,

\[
g_t(C)=\log C+O\!\left(\frac{\log C}{C}\right).
\tag{19}
\]

AF-527's tuning gives

\[
\frac{\widetilde C_A}{C_A}=1+O(H_A^{-1}),
\qquad
C_A,\widetilde C_A\asymp e^{\sqrt{H_A}}.
\tag{20}
\]

Consequently

\[
\sup_{0\le t\le A^{-1}}
|g_t(\widetilde C_A)-g_t(C_A)|
=O(H_A^{-1}),
\tag{21}
\]

and therefore

\[
\sup_{0\le t\le A^{-1}}
\frac{H_A}{L_A}
|g_t(\widetilde C_A)-g_t(C_A)|
=O(L_A^{-1})\to0.
\tag{22}
\]

Combining (7), (17), and (22) proves (1).

### 4. Integrating the uniform slope gives the finite-window law

For \(0\le u\le1\),

\[
F_A(u)
=
\int_0^{u/A}(\log R_A)'(t)\,dt.
\tag{23}
\]

Equation (1) is uniform over the integration interval, so multiplying (23) by \(A H_A/L_A\) gives (2). Taking \(u=1\) gives (3).

Because the right side of (3) tends to zero,

\[
\frac{R_A(1/A)}{R_A(0)}-1
=
(1-\theta)\frac{L_A}{A H_A}
+o\!\left(\frac{L_A}{A H_A}\right).
\tag{24}
\]

Thus the same parameter that is order-one after derivative renormalization is encoded by a vanishing relative endpoint change in the raw finite-window carrier.

### 5. Direct noise amplification

Let

\[
Y_A(0)=\log R_A(0)+e_0,
\qquad
Y_A(u/A)=\log R_A(u/A)+e_u,
\]

with \(|e_0|,|e_u|\le\varepsilon_A\). Substituting these observations into (4) and using (2) yields

\[
\widehat\theta_A-\theta
=o(1)
-
\frac{A H_A}{uL_A}(e_u-e_0),
\]

which proves (5) and the sufficient resolution condition (6).

The amplification factor \(A H_A/L_A\) is exactly the reciprocal of the finite-window signal scale. This is the finite-resolution cost hidden by the normalized derivative statement of AF-528.

## Fidelity / representation audit

AF-527 and AF-528 separate two different notions of survival. AF-527 shows that scalar amplitude asymptotics can lose the power-separated anchor provenance to every fixed algebraic order in \(1/H_A\). AF-528 shows that an exact infinitesimal shape derivative restores \(\theta\). AF-529 shows that this recovered information survives on the non-infinitesimal physical window, but only with a vanishing margin of order \(L_A/(A H_A)\).

This matters because injectivity and conditioning are distinct fidelity resources. The lifted representation is asymptotically injective in the coarse parameter \(\theta\), yet the inverse map through a finite secant has condition scale \(A H_A/L_A\to\infty\). A property can therefore survive a compression in the exact zero-error sense while becoming arbitrarily fragile under finite-resolution observation.

The baseline subtraction in \(F_A(u)\) is essential to the statement. AF-527 proves that the static co-tuned amplitude mismatch is super-algebraically small in \(H_A\), but that scale is still vastly coarser than \(L_A/(A H_A)\). The finite-shape signal is revealed by comparing the same carrier at two nearby boundary parameters, not by treating \(R_A(0)\) as exactly one.

## Boundaries

1. **Exact carrier ratio, not curvature-defect ratio.** As in AF-528, the theorem concerns the exact carrier ratio \(R_A\). No derivative or finite-window transfer to the normalized curvature-defect ratio is claimed.

2. **Two-sample conditioning, not universal impossibility.** Equation (6) is sufficient for the explicit secant decoder and the scale is sharp for that baseline-differenced two-point channel under bounded adversarial observation error. It does not rule out another representation or a richer multi-sample/full-function observation with better conditioning.

3. **Anchor exponent, not prime identity.** The recovered parameter is \(\theta\). The proof uses only Mertens-type prime moments and is expected to have analogues for matched generalized-prime systems with the same moment laws. No rational-prime discriminator or RH consequence follows.

4. **The natural window is crucial.** The severe factor \(A\) comes from observing only \(0\le t\le A^{-1}\). A wider exact-carrier window could carry a larger secant signal, but it would no longer be the AF-527 boundary layer whose curvature comparison motivated the lift.

5. **No stochastic noise model is assumed.** The bound in (5) is deterministic. Statistical averaging can improve effective precision under additional independent-noise assumptions, but those assumptions are extra structure and are not part of this finding.

6. **No minimal-lift claim.** A first derivative and its finite secant suffice for this coarse provenance parameter. The result does not prove that this is the least-dimensional or best-conditioned lift available.

## Prior-art / source audit

The arithmetic inputs are classical Mertens estimates. Terence Tao's expository account, *Mertens' theorems* (2013), records in particular

\[
\sum_{p\le x}\frac{\log p}{p}=\log x+O(1),
\qquad
\sum_{p\le x}\frac1p=\log\log x+O(1),
\]

and AF-527/AF-528 already use the refined reciprocal-prime constant/error form. Source: https://terrytao.wordpress.com/2013/12/11/mertens-theorems/ .

The instability of numerical differentiation under noisy function values is also classical; for example, Rick Chartrand, *Numerical Differentiation of Noisy, Nonsmooth Data*, ISRN Applied Mathematics 2011, DOI 10.5402/2011/164564, explicitly treats differentiation as an ill-conditioned/noise-amplifying inverse operation. That general principle is prior art and is not claimed as new here.

A targeted literature search did not identify a standard theorem matching the specific AF-527 co-tuned prime-carrier family, the uniform boundary-layer limit (1), or the resulting scale \(\log A/(A\log\log A)\). No novelty claim is made on that basis. The durable Mathia contribution is the exact specialization that converts AF-528's qualitative finite-resolution warning into a proved asymptotic conditioning law for this representation.

## Consequence

AF-528's one-derivative lift does not remove the fidelity problem; it changes its category. Exact identifiability of the anchor exponent is restored, but finite-resolution robustness deteriorates at the explicit rate

\[
\frac{A\log\log A}{\log A}.
\]

For Arithmetic Fidelity, this is a concrete separation between **survival of information** and **stable survival of information**. Future lift claims should therefore track not only whether provenance is recoverable in principle, but also the margin by which matched controls remain distinguishable on the observation scale actually available.