# AF-530 — The full boundary shape has the same sharp conditioning scale as one secant

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CARRIER-SHAPE` · `FINITE-RESOLUTION` · `MINIMAX` · `CONDITIONING` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

AF-529 proved that one finite boundary secant recovers the power-separated anchor exponent in the AF-527 co-tuned control family only at the vanishing signal scale

\[
\delta_A:=\frac{\log A}{A\log\log A}.
\]

Observing the **entire baseline-differenced boundary-layer shape** does not improve that deterministic recovery scale.

Fix a nondegenerate compact interval

\[
K=[\theta_-,\theta_+]\Subset(0,1),
\qquad D:=\theta_+-\theta_->0.
\]

For \(\theta\in K\), set \(B_A(\theta)=\lfloor A^\theta\rfloor\) and choose the co-tuned multipliers \(C_A,\widetilde C_{A,\theta}\) exactly as in AF-527. Write

\[
L_A=\log A,\qquad H_A=\log L_A,
\]

\[
R_{A,\theta}(t)
=
\frac{\widetilde C_{A,\theta}^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A(\theta),t)}{B_0(A,t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t},
\]

and retain the anchored shape

\[
F_{A,\theta}(u)
:=
\log R_{A,\theta}(u/A)-\log R_{A,\theta}(0),
\qquad 0\le u\le1.
\]

Then AF-529 upgrades uniformly over \(K\) to

\[
\boxed{
\sup_{\theta\in K}\sup_{0\le u\le1}
\left|
\frac{F_{A,\theta}(u)}{\delta_A}-u(1-\theta)
\right|
\longrightarrow0.
}
\tag{1}
\]

Hence the complete normalized continuum profile converges to the one-dimensional family \(G_\theta(u)=u(1-\theta)\), and

\[
\boxed{
\sup_{\theta,\eta\in K}
\left|
\frac{\|F_{A,\theta}-F_{A,\eta}\|_\infty}{\delta_A}
-|\theta-\eta|
\right|
\longrightarrow0.
}
\tag{2}
\]

Now observe one unknown profile under deterministic sup-norm error,

\[
Y_A=F_{A,\theta}+e_A,
\qquad
\|e_A\|_\infty\le\varepsilon_A.
\tag{3}
\]

Define

\[
\mathcal R_A(\varepsilon_A)
:=
\inf_{\widehat\theta:C([0,1])\to K}
\sup_{\theta\in K}
\sup_{\|e\|_\infty\le\varepsilon_A}
|\widehat\theta(F_{A,\theta}+e)-\theta|.
\tag{4}
\]

If

\[
\frac{\varepsilon_A}{\delta_A}\longrightarrow c
\qquad(c\in[0,\infty]),
\]

then

\[
\boxed{
\mathcal R_A(\varepsilon_A)
\longrightarrow
\min\!\left(c,\frac D2\right).
}
\tag{5}
\]

Therefore

\[
\boxed{
\text{uniform recovery of }\theta\text{ on }K
\iff
\varepsilon_A=o(\delta_A).
}
\tag{6}
\]

Arbitrarily dense sampling of this full shape channel therefore has the same sharp worst-case noise order as AF-529's endpoint secant. At leading order there is only one retained shape direction, and the endpoint already reads it optimally.

There is also an amplitude-quotient statement. Put

\[
f_{A,\theta}(u)=\log R_{A,\theta}(u/A)
\]

and use the quotient norm on \(C([0,1])/\mathbb R\),

\[
\|[f]\|_q:=\inf_{c\in\mathbb R}\|f-c\|_\infty.
\]

Since \([f_{A,\theta}]=[F_{A,\theta}]\),

\[
\boxed{
\sup_{\theta,\eta\in K}
\left|
\frac{\|[f_{A,\theta}]-[f_{A,\eta}]\|_q}{\delta_A}
-\frac{|\theta-\eta|}{2}
\right|
\longrightarrow0.
}
\tag{7}
\]

Thus forgetting the absolute carrier amplitude does not erase \(\theta\), but it leaves the same vanishing conditioning order \(\delta_A\).

## Derivation

### 1. Compact-uniform form of AF-529

AF-529 gives for each fixed \(\theta\in(0,1)\)

\[
\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}(\log R_{A,\theta})'(t)-(1-\theta)
\right|\to0.
\tag{8}
\]

Its estimates are uniform on \(K\Subset(0,1)\). Indeed,

\[
\log B_A(\theta)=\theta L_A+O(A^{-\theta_-})
\tag{9}
\]

uniformly, and hence

\[
\log\log B_A(\theta)=H_A+\log\theta+o(1)
\tag{10}
\]

uniformly because \(\theta\ge\theta_->0\). The Mertens estimates and elementary moment domination used in AF-529 then give, uniformly for \(\theta\in K\) and \(0\le t\le A^{-1}\),

\[
\frac{H_A}{L_A}\mu_A(t)=1+o(1),
\qquad
\frac{H_A}{L_A}\mu_{B_A(\theta)}(t)=\theta+o(1),
\tag{11}
\]

where

\[
\mu_X(t)
=
\frac{\sum_{p\le X}(\log p)p^{-1-t}}
{\sum_{p\le X}p^{-1-t}}.
\]

The co-tuning also satisfies

\[
\frac{\widetilde C_{A,\theta}}{C_A}=1+O(H_A^{-1})
\tag{12}
\]

uniformly on \(K\): \(\log\theta\) stays bounded and the nearest-integer error remains exponentially smaller than \(H_A^{-1}\). Consequently the multiplier term in AF-529's exact derivative identity is still \(o(L_A/H_A)\) uniformly. Thus

\[
\boxed{
\sup_{\theta\in K}\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}(\log R_{A,\theta})'(t)-(1-\theta)
\right|\to0.
}
\tag{13}
\]

### 2. The entire boundary profile is asymptotically rank one

Integrating (13) from \(0\) to \(u/A\) and multiplying by \(AH_A/L_A=1/\delta_A\) proves (1).

Subtracting the expansions for \(\theta\) and \(\eta\) gives

\[
\frac{F_{A,\theta}(u)-F_{A,\eta}(u)}{\delta_A}
= u(\eta-\theta)+r_A(\theta,\eta,u),
\tag{14}
\]

with

\[
\sup_{\theta,\eta\in K}\sup_{u\in[0,1]}|r_A(\theta,\eta,u)|\to0.
\tag{15}
\]

Since \(\sup_{u\in[0,1]}u=1\), equation (2) follows.

### 3. Endpoint decoding gives the upper minimax bound

Let \(\Pi_K\) be metric projection onto \(K\) and define

\[
\widehat\theta_A(Y)
=
\Pi_K\!\left(1-\frac{Y(1)}{\delta_A}\right).
\tag{16}
\]

By (1), uniformly in \(\theta\in K\),

\[
\frac{F_{A,\theta}(1)}{\delta_A}=1-\theta+o(1).
\]

Because projection onto an interval is nonexpansive,

\[
\sup_{\theta\in K}\sup_{\|e\|_\infty\le\varepsilon_A}
|\widehat\theta_A(F_{A,\theta}+e)-\theta|
\le
\frac{\varepsilon_A}{\delta_A}+o(1).
\tag{17}
\]

The constant midpoint estimator has risk \(D/2\), hence

\[
\limsup_A\mathcal R_A(\varepsilon_A)
\le
\min\!\left(c,\frac D2\right).
\tag{18}
\]

### 4. Overlapping sup-norm balls give the matching lower bound

For \(\theta_0,\theta_1\in K\), if

\[
\|F_{A,\theta_0}-F_{A,\theta_1}\|_\infty\le2\varepsilon_A,
\tag{19}
\]

the midpoint \((F_{A,\theta_0}+F_{A,\theta_1})/2\) is an admissible datum for both parameters. Every decoder therefore incurs worst-case error at least \(|\theta_0-\theta_1|/2\) on that datum.

If \(0<c<\infty\), choose any \(0<d<\min(2c,D)\) and parameters in \(K\) separated by \(d\). Equation (2) gives

\[
\|F_{A,\theta_0}-F_{A,\theta_1}\|_\infty
=
\delta_A(d+o(1))<2\varepsilon_A
\]

for large \(A\), so

\[
\liminf_A\mathcal R_A(\varepsilon_A)\ge d/2.
\]

Letting \(d\uparrow\min(2c,D)\) gives the lower half of (5). For \(c=0\), (17) gives zero risk asymptotically. For \(c=\infty\), take any \(d<D\), use (19) for large \(A\), and let \(d\uparrow D\). This proves (5).

If \(\varepsilon_A=o(\delta_A)\), equation (17) gives uniform consistency. Conversely, if \(\varepsilon_A/\delta_A\not\to0\), a subsequence has \(\varepsilon_A/\delta_A\ge c_0>0\), and the same overlap argument gives a fixed positive minimax error on that subsequence. This proves (6).

### 5. Quotienting amplitude changes the constant, not the scale

For every real continuous \(h\),

\[
\|[h]\|_q
=
\inf_c\|h-c\|_\infty
=
\frac12(\max h-\min h).
\tag{20}
\]

The normalized difference in (14) converges uniformly to \(u(\eta-\theta)\), whose range has length \(|\eta-\theta|\). Continuity of the quotient norm under ambient sup-norm perturbations gives (7).

This is the appropriate statement after completely forgetting the zero-jet amplitude. It does not identify quotient-noise constants with the anchored observation model in (3).

## Prior-art / novelty audit

The minimax mechanism is classical optimal-recovery and inverse-stability mathematics. In particular:

- Charles A. Micchelli, T. J. Rivlin, and S. Winograd, **“The optimal recovery of smooth functions,”** *Numerische Mathematik* 26 (1976), 191–200, gives classical worst-case lower bounds for recovery from finite information.
- Charles A. Micchelli and T. J. Rivlin, **“A Survey of Optimal Recovery,”** in *Optimal Estimation in Approximation Theory* (1977), DOI `10.1007/978-1-4684-2388-4_1`, is classical prior art for worst-case optimal recovery.
- David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *Annals of Statistics* 22(1), 238–270 (1994), DOI `10.1214/aos/1176325367`, explicitly relates estimation difficulty to a modulus of continuity and connects minimax estimation to optimal recovery.
- Mahmood Ettehad and Simon Foucart, **“Instances of Computational Optimal Recovery: Dealing with Observation Errors,”** *SIAM/ASA Journal on Uncertainty Quantification* 9(4), 1438–1456 (2021), DOI `10.1137/20M1328476`, treats worst-case optimal recovery with inaccurate observations.
- Heinz W. Engl, Martin Hanke, and Andreas Neubauer, ***Regularization of Inverse Problems***, Mathematics and Its Applications 375, Springer/Kluwer (1996), DOI `10.1007/978-94-009-1740-8`, provides standard inverse-problem language for instability and regularization.

No novelty is claimed for overlapping deterministic noise balls, two-point minimax lower bounds, quotient norms, or the principle that inverse stability is controlled by a modulus of continuity.

The durable Arithmetic Fidelity content is the exact specialization to the AF-527 control family: AF-529's finite-window law is uniform over compact anchor-exponent families, the **whole** normalized carrier shape collapses to \(u(1-\theta)\), and its deterministic minimax recovery scale is exactly \(\log A/(A\log\log A)\). Thus denser access to the same boundary-shape observable does not restore a stronger fidelity margin.

## Boundaries and falsification audit

1. **Anchored shape, not raw amplitude.** Equations (1)--(6) concern \(F_{A,\theta}(u)=f_{A,\theta}(u)-f_{A,\theta}(0)\). AF-527 only shows that the static amplitude mismatch is super-algebraically small in \(H_A\); that can still be much larger than \(\delta_A\). No claim is made that the unquotiented raw profile lacks additional information.

2. **Amplitude quotient has a different noise geometry.** Equation (7) identifies quotient separation. If observation error is measured directly in quotient norm, minimax constants differ. Only the asymptotic order is shared.

3. **Deterministic adversarial sup-norm noise.** Independent stochastic errors at many samples may average down and define a different experiment. Correlated, integral, derivative, Sobolev, or probabilistic noise requires separate analysis.

4. **Compact exponent family.** The uniform result assumes \(K\Subset(0,1)\). Regimes with \(\theta=\theta_A\to0\) or \(1\) can have different asymptotics.

5. **Anchor exponent, not rational-prime identity.** The recovered target is \(\theta\). The proof uses Mertens-type moments and does not distinguish rational primes from matched generalized-prime systems with the same moment laws.

6. **Exact carrier ratio, not curvature-defect ratio.** The theorem remains upstream of the curvature-to-carrier approximation. A corresponding derivative/profile theorem for the normalized curvature defect needs separate error control.

7. **No universal minimal-lift claim.** The full declared shape channel being asymptotically rank one does not prove that the endpoint or first derivative is minimal among all possible representations.

8. **Target-relative conditioning.** The scale \(\delta_A\) is the margin for order-one recovery of \(\theta\). Distinguishing parameters whose separation itself tends to zero is a different decision problem.

## Consequence

AF-527--AF-530 separate four fidelity layers for one matched-control family. Scalar amplitude can collide beyond every algebraic order in \(1/\log\log A\); one infinitesimal relational derivative recovers the coarse anchor exponent; a physical finite secant carries it only at scale \(\delta_A\); and the complete anchored boundary shape does not improve the deterministic conditioning order.

The resulting principle is stronger than an injectivity test: **after a lift restores a discriminator, inspect the dimension and modulus of the retained shape family.** Here the normalized family is asymptotically rank one, so a conditioning improvement must come from another scale, another observable, extra source-derived structure, or another noise geometry—not from denser sampling of the same boundary shape.