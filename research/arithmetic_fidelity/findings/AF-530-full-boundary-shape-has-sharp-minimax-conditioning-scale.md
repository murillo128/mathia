# AF-530 — The full boundary shape has the same sharp conditioning scale as one secant

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CARRIER-SHAPE` · `FINITE-RESOLUTION` · `MINIMAX` · `CONDITIONING` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

AF-529 proved that a single finite boundary secant recovers the power-separated anchor exponent in the AF-527 co-tuned control family only at the vanishing signal scale

\[
\delta_A:=\frac{\log A}{A\log\log A}.
\]

That two-sample result leaves open whether observing the **entire boundary-layer shape** can improve the deterministic recovery scale. It cannot, for the baseline-differenced carrier-shape channel considered here.

Fix a nondegenerate compact interval

\[
K=[\theta_-,\theta_+]\Subset(0,1),
\qquad D:=\theta_+-\theta_->0.
\]

For every \(\theta\in K\), let

\[
B_A(\theta)=\lfloor A^\theta\rfloor
\]

and choose the co-tuned multipliers \(C_A,\widetilde C_{A,\theta}\) exactly as in AF-527, with

\[
L_A=\log A,\qquad H_A=\log L_A.
\]

Let

\[
R_{A,\theta}(t)
=
\frac{\widetilde C_{A,\theta}^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A(\theta),t)}{B_0(A,t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t},
\]

and retain the complete anchored shape on the physical boundary layer,

\[
F_{A,\theta}(u)
:=
\log R_{A,\theta}(u/A)-\log R_{A,\theta}(0),
\qquad 0\le u\le1.
\]

Then AF-529 strengthens uniformly in \(\theta\in K\) to

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

Thus, after the only normalization that prevents the signal from vanishing, the entire continuum profile converges to the one-dimensional affine family

\[
G_\theta(u)=u(1-\theta).
\]

In particular,

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

Now observe one unknown profile through deterministic sup-norm error:

\[
Y_A=F_{A,\theta}+e_A,
\qquad
\|e_A\|_\infty\le\varepsilon_A.
\tag{3}
\]

Define the worst-case minimax risk

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
\qquad\text{for }c\in[0,\infty],
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

Consequently,

\[
\boxed{
\text{uniform recovery of }\theta\text{ on }K
\quad\Longleftrightarrow\quad
\varepsilon_A=o(\delta_A).
}
\tag{6}
\]

So arbitrarily dense sampling of the complete anchored carrier shape does **not** improve the deterministic noise order obtained from AF-529's single endpoint secant. At leading order the profile contains only one scalar direction, and the endpoint already reads that direction optimally.

There is also an intrinsic amplitude-quotient formulation. Put

\[
f_{A,\theta}(u)=\log R_{A,\theta}(u/A)
\]

and pass to the quotient Banach space

\[
C([0,1])/\mathbb R
\]

that forgets additive amplitude constants, with quotient norm

\[
\|[f]\|_q:=\inf_{c\in\mathbb R}\|f-c\|_\infty.
\]

Since \([f_{A,\theta}]=[F_{A,\theta}]\), equation (1) gives

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

Thus forgetting the absolute carrier amplitude does not erase the anchor exponent, but it leaves the same vanishing conditioning order \(\delta_A\); only the constant changes with the observation geometry.

## Derivation

### 1. AF-529 is uniform on compact anchor-exponent families

AF-529 proves, for each fixed \(\theta\in(0,1)\),

\[
\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}(\log R_{A,\theta})'(t)-(1-\theta)
\right|
\to0.
\tag{8}
\]

Every estimate in that proof is uniform when \(\theta\) ranges over a compact \(K\Subset(0,1)\).

Indeed, if \(\theta\in K\), then uniformly

\[
\log B_A(\theta)
=
\theta L_A+O(A^{-\theta_-}),
\tag{9}
\]

and hence

\[
\log\log B_A(\theta)
=
H_A+\log\theta+o(1).
\tag{10}
\]

Because \(\theta\ge\theta_->0\), the Mertens errors used in AF-529 satisfy uniformly

\[
B_0(B_A(\theta),t)
=
\log\log B_A(\theta)+B_1
+O(L_A^{-1})+O(L_A/A),
\tag{11}
\]

for \(0\le t\le A^{-1}\). Likewise, with

\[
M_1(X,t)=\sum_{p\le X}(\log p)p^{-1-t},
\qquad
\mu_X(t)=\frac{M_1(X,t)}{B_0(X,t)},
\]

the elementary moment bounds in AF-529 give

\[
\sup_{\theta\in K}\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}\mu_{B_A(\theta)}(t)-\theta
\right|
\to0.
\tag{12}
\]

The \(X=A\) term is independent of \(\theta\) and satisfies

\[
\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}\mu_A(t)-1
\right|
\to0.
\tag{13}
\]

For the multiplier contribution, AF-527's co-tuning gives

\[
\frac{\widetilde C_{A,\theta}}{C_A}
=
1+O(H_A^{-1})
\tag{14}
\]

uniformly on \(K\), because \(\log\theta\) is bounded there and nearest-integer rounding is exponentially smaller than \(H_A^{-1}\). The derivative term therefore remains

\[
\sup_{\theta\in K}\sup_{0\le t\le A^{-1}}
\frac{H_A}{L_A}
|g_t(\widetilde C_{A,\theta})-g_t(C_A)|
\to0,
\tag{15}
\]

with

\[
g_t(C)=\frac{C^{1+t}\log C}{C^{1+t}-1}.
\]

Combining (12)--(15) in AF-529's exact logarithmic-derivative identity proves the compact-uniform version of (8):

\[
\sup_{\theta\in K}\sup_{0\le t\le A^{-1}}
\left|
\frac{H_A}{L_A}(\log R_{A,\theta})'(t)-(1-\theta)
\right|
\to0.
\tag{16}
\]

### 2. Integration gives a rank-one limiting shape family

For \(0\le u\le1\),

\[
F_{A,\theta}(u)
=
\int_0^{u/A}(\log R_{A,\theta})'(t)\,dt.
\]

Multiply by \(AH_A/L_A=1/\delta_A\). The uniform estimate (16) then gives (1).

For \(\theta,\eta\in K\), subtract the two expansions in (1):

\[
\frac{F_{A,\theta}(u)-F_{A,\eta}(u)}{\delta_A}
=
u(\eta-\theta)+r_A(\theta,\eta,u),
\tag{17}
\]

where the symbol on the right is \(u(\eta-\theta)\) and

\[
\sup_{\theta,\eta\in K}\sup_{u\in[0,1]}|r_A(\theta,\eta,u)|\to0.
\tag{18}
\]

Therefore

\[
\frac{\|F_{A,\theta}-F_{A,\eta}\|_\infty}{\delta_A}
=|\theta-\eta|+o(1)
\]

uniformly, because \(\sup_{0\le u\le1}u=1\). This proves (2).

The occurrence of \(\nu\) in (17) is only typographical notation for the profile variable \(u\); no additional parameter is introduced.

### 3. Endpoint decoding supplies the minimax upper bound

Let \(\Pi_K\) denote metric projection onto the interval \(K\), and define

\[
\widehat\theta_A(Y)
=
\Pi_K\!\left(1-\frac{Y(1)}{\delta_A}\right).
\tag{19}
\]

By (1), uniformly in \(\theta\in K\),

\[
\frac{F_{A,\theta}(1)}{\delta_A}
=1-\theta+o(1).
\]

Since projection onto an interval is nonexpansive,

\[
\sup_{\theta\in K}\sup_{\|e\|_\infty\le\varepsilon_A}
|\widehat\theta_A(F_{A,\theta}+e)-\theta|
\le
\frac{\varepsilon_A}{\delta_A}+o(1).
\tag{20}
\]

The constant estimator \((\theta_-+\theta_+)/2\) has worst-case error \(D/2\). Hence

\[
\limsup_A\mathcal R_A(\varepsilon_A)
\le
\min\!\left(c,\frac D2\right)
\tag{21}
\]

whenever \(\varepsilon_A/\delta_A\to c\), including \(c=\infty\) in the obvious extended sense.

Thus the complete continuum profile cannot improve the order achieved by reading only its terminal secant.

### 4. Overlapping noise balls give the matching lower bound

Fix two parameters \(\theta_0,\theta_1\in K\). If

\[
\|F_{A,\theta_0}-F_{A,\theta_1}\|_\infty
\le2\varepsilon_A,
\tag{22}
\]

then the midpoint profile

\[
Y_A=\frac12(F_{A,\theta_0}+F_{A,\theta_1})
\]

lies in both admissible noise balls. No decoder receiving \(Y_A\) can distinguish which parameter generated it, so its worst-case error on that datum is at least

\[
\frac{|\theta_0-\theta_1|}{2}.
\tag{23}
\]

Suppose first \(0<c<\infty\). For any

\[
0<d<\min(2c,D),
\]

choose \(\theta_0,\theta_1\in K\) with \(|\theta_0-\theta_1|=d\). Equation (2) gives

\[
\|F_{A,\theta_0}-F_{A,\theta_1}\|_\infty
=
\delta_A(d+o(1))
<2\varepsilon_A
\]

for all sufficiently large \(A\). Hence

\[
\liminf_A\mathcal R_A(\varepsilon_A)\ge d/2.
\]

Letting \(d\uparrow\min(2c,D)\) yields

\[
\liminf_A\mathcal R_A(\varepsilon_A)
\ge
\min\!\left(c,\frac D2\right).
\tag{24}
\]

For \(c=0\), the lower bound is trivial and (20) gives convergence to zero. For \(c=\infty\), take any \(d<D\); equation (22) eventually holds and then let \(d\uparrow D\). Combining with (21) proves (5).

Equation (6) is immediate: \(\varepsilon_A=o(\delta_A)\) is sufficient by (20), while if it fails there is a subsequence with \(\varepsilon_A/\delta_A\ge c_0>0\), and the same two-point overlap argument gives a fixed positive minimax error on that subsequence.

### 5. Quotienting amplitude keeps the same order

Because subtracting \(f(0)\) changes only the additive constant,

\[
[f_{A,\theta}]=[F_{A,\theta}].
\]

For a real continuous function \(h\),

\[
\|[h]\|_q
=
\inf_c\|h-c\|_\infty
=
\frac12\bigl(\max h-\min h\bigr).
\tag{25}
\]

The normalized difference in (17) converges uniformly to

\[
u(\eta-\theta),
\]

whose range has length \(|\eta-\theta|\). Quotient norms are 1-Lipschitz with respect to the ambient sup norm, so (18) immediately gives (7).

Thus the scalar zero-jet may be discarded completely while the relational shape still retains \(\theta\); however, the retained separation remains only order \(\delta_A\).

## Prior-art / novelty audit

The minimax mechanism in (22)--(24) is classical optimal-recovery reasoning, not a new general theorem. Micchelli, Rivlin, and Winograd studied worst-case recovery bounds from finite information in the 1970s, and the Micchelli--Rivlin survey organized the broader optimal-recovery framework. Donoho later made the modulus-of-continuity viewpoint explicit in statistical estimation and connected it to optimal recovery. Modern work such as Ettehad--Foucart treats worst-case recovery from inaccurate observations directly.

No novelty is claimed for overlapping deterministic noise balls, minimax two-point lower bounds, quotient norms, or the principle that inverse stability is governed by a modulus of continuity.

The durable Arithmetic Fidelity content is the **exact specialization to the AF-527 co-tuned arithmetic control family**: AF-529's finite-window expansion is uniform over compact anchor exponents, the whole continuum carrier shape collapses after normalization to the one-dimensional family \(u(1-\theta)\), and therefore the complete profile has the same sharp deterministic recovery scale \(\log A/(A\log\log A)\) as one endpoint secant. More samples do not improve the minimax order because there is no additional leading shape direction to average against adversarial sup-norm error.

## Boundaries and falsification audit

1. **Anchored shape, not the raw amplitude profile.** Equations (1)--(6) concern \(F_{A,\theta}(u)=f_{A,\theta}(u)-f_{A,\theta}(0)\). AF-527's static amplitude mismatch is only known to be super-algebraically small in \(H_A\), which is still much larger than \(\delta_A\) on the relevant scale. The theorem therefore does not claim that the unquotiented raw profile has no additional information.

2. **Amplitude quotient has its own noise geometry.** Equation (7) identifies exact quotient separation. If observation error is itself measured in the quotient norm, endpoint differencing can double the ambient error and the minimax constant changes. The theorem claims equality of the asymptotic **order**, not invariance of constants across observation models.

3. **Deterministic adversarial sup-norm noise only.** Independent stochastic errors at many sample points may average down and define a different experiment. Correlated, integral, derivative, or Sobolev noise geometries likewise require separate analysis.

4. **Compact exponent families away from 0 and 1.** The compactness of \(K\Subset(0,1)\) makes the AF-529 asymptotics uniform. Letting \(\theta\) approach 0 or 1 with \(A\) can create new boundary regimes.

5. **Anchor exponent, not rational-prime identity.** As in AF-528/AF-529, the recovered parameter is \(\theta\). The proof uses Mertens-type prime moments and does not separate rational primes from generalized-prime systems sharing the same moment laws.

6. **Exact carrier ratio, not normalized curvature defect.** The result still concerns the AF-527 carrier ratio before the curvature-to-carrier approximation. Uniform derivative control for the curvature-defect ratio would be an additional theorem.

7. **No minimal-lift theorem.** The full profile being asymptotically rank one does not prove that the first derivative or endpoint secant is minimal among every admissible representation. It proves only that within this declared boundary-shape channel, the complete continuum observation does not improve the deterministic noise order.

8. **The scale is target-relative.** The normalization \(\delta_A\) is forced by recovery of an order-one change in \(\theta\). A weaker target, such as distinguishing exponents separated by a vanishing amount, has a correspondingly different decision scale.

## Consequence

AF-527, AF-528, AF-529, and AF-530 now separate four distinct fidelity questions for the same matched-control family:

- scalar amplitude can collide beyond every algebraic order in \(1/\log\log A\);
- an infinitesimal relational derivative recovers the coarse anchor exponent;
- a physical finite secant carries that exponent only at the vanishing scale \(\delta_A\);
- retaining the entire anchored boundary shape does not improve the worst-case deterministic conditioning order.

The lesson is sharper than injective versus non-injective recovery. **Once a lift restores a discriminator, one must still ask whether the whole retained observation class contains additional stable directions.** Here it does not at leading order: the normalized profile is asymptotically rank one. Any genuine conditioning improvement must therefore come from a different scale, a different observable, extra source-derived structure, or a different noise geometry rather than denser sampling of the same boundary shape.