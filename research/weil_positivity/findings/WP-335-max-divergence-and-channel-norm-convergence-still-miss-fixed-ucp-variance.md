---
id: WP-335
title: Max-divergence and channel-norm convergence still miss fixed UCP variance for the unbounded Mangoldt coordinate
branch: weil_positivity
status: supported
kind: ucp-unbounded-observable-stability-obstruction
claim_strength: exact support-preserving martingale UCP construction on the intrinsic dyadic prime-power ray for which both order-infinity Renyi divergences of the scalar source laws tend to zero and the Markov readout converges to the identity in operator norm, while the Kadison defect of the logarithmic source coordinate has constant norm
created: 2026-09-16
related: [WP-332, WP-333, WP-334]
prior_art:
  - Richard V. Kadison, A Generalized Schwarz Inequality and Algebraic Invariants for Operator Algebras, Annals of Mathematics 56 (1952), 494-503, DOI 10.2307/1969657
  - W. Forrest Stinespring, Positive Functions on C*-Algebras, Proceedings of the American Mathematical Society 6 (1955), 211-216, DOI 10.1090/S0002-9939-1955-0069403-4
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
  - Tim van Erven and Peter Harremoes, Renyi Divergence and Kullback-Leibler Divergence, IEEE Transactions on Information Theory 60 (2014), 3797-3820, DOI 10.1109/TIT.2014.2320500, arXiv:1206.2459
  - Volker Strassen, The Existence of Probability Measures with Given Marginals, Annals of Mathematical Statistics 36 (1965), 423-439, DOI 10.1214/aoms/1177700153
---

# WP-335 — Max-divergence and channel-norm convergence still miss fixed UCP variance for the unbounded Mangoldt coordinate

## Claim

`WP-334` showed that the support-preserving UCP tail escape survives every fixed finite-order information divergence, while its particular fixed-laziness construction is detected by order-infinity Renyi divergence. That leaves a natural possible repair: require the transformed scalar law to converge to the Mangoldt law in **both** max-divergence directions, i.e. require its likelihood ratio to converge uniformly to one.

That repair is still insufficient for the logarithmic source observable.

Fix `s>0`, put `h=log 2`, and use the finite pole-normalized Mangoldt source of `WP-333`--`WP-334`. On the dyadic ray write

\[
y_j=jh,\qquad
w_{j,R}=\nu_R(\{y_j\})
\propto \frac{h\,2^{-js}}{2^j+1}.
\tag{1}
\]

Let

\[
k_R=\left\lfloor\frac{R}{h}\right\rfloor,
\qquad j_R=k_R-1,
\qquad a_R=\left\lfloor\frac{j_R}{2}\right\rfloor.
\tag{2}
\]

For large `R`, `a_R>=2`, and the three intrinsic support points

\[
y_{j_R-a_R},\qquad y_{j_R},\qquad y_{j_R+1}
\tag{3}
\]

all lie inside the cutoff. Define a Markov/UCP self-map `Psi_R:C(Sigma_R)->C(Sigma_R)` to be the identity away from `y_{j_R}` and, at the center, set

\[
\Psi_R(f)(y_{j_R})
=
\frac{1}{a_R(a_R+1)}f(y_{j_R-a_R})
+\left(1-\frac1{a_R}\right)f(y_{j_R})
+\frac{1}{a_R+1}f(y_{j_R+1}).
\tag{4}
\]

The transition probabilities sum to one and their displacement has zero mean. Hence for the logarithmic coordinate `X_R(t)=t`,

\[
\boxed{\Psi_R(X_R)=X_R.}
\tag{5}
\]

Nevertheless the Kadison defect

\[
Q_R:=\Psi_R(X_R^2)-X_R^2\ge0
\tag{6}
\]

is supported at the modified center and satisfies

\[
\boxed{Q_R(y_{j_R})=(\log2)^2,\qquad \|Q_R\|=(\log2)^2}
\tag{7}
\]

for every sufficiently large cutoff. Thus the associated Stinespring off-diagonal source coupling has constant norm `log 2`.

At the same time, if `nu_R'=nu_R Psi_R` denotes the transformed scalar law, then

\[
\boxed{
D_\infty(\nu_R'\|\nu_R)\to0,
\qquad
D_\infty(\nu_R\|\nu_R')\to0.
}
\tag{8}
\]

Equivalently, the likelihood ratio converges to one uniformly on the entire finite support. Even more strongly,

\[
\boxed{\|\Psi_R-I\|_{C(\Sigma_R)\to C(\Sigma_R)}=\frac{2}{a_R}\to0.}
\tag{9}
\]

So neither two-sided max-divergence convergence of the scalar law nor ordinary operator-norm convergence of the Markov readout is enough to globalize the exact multiplicative-domain rigidity of `WP-332` for the **moving unbounded source coordinate**.

The loophole is not hidden likelihood mass. It is a vanishing transition probability multiplied by a growing jump length. The map becomes uniformly close to the identity on the unit ball of bounded functions, but the cutoff-dependent observable `X_R` has `||X_R||~R`; a probability of order `1/a_R^2` sent a distance of order `a_R` contributes order one to the conditional second moment.

This is a negative boundary result, not a Weil-positivity mechanism. The same construction works on generic one-sided geometric tails with an equally spaced coordinate. Its Mathia-specific value is to close the max-divergence repair suggested by `WP-334` and to identify the missing ingredient more sharply: a viable global rigidity theorem must control the source observable in an **energy/graph-norm or moment-weighted topology**, not merely the scalar likelihood ratio or the channel on bounded observables.

**Classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE + UCP-READOUT + MAX-DIVERGENCE + CHANNEL-NORM-CONVERGENCE + UNBOUNDED-OBSERVABLE + MARTINGALE-TAIL + MATCHED-CONTROL + NOT-WEIL-POSITIVITY`.

## 1. The intrinsic asymmetric martingale step

Abbreviate `j=j_R` and `a=a_R`. The three nonzero transition probabilities in (4) are

\[
p_-:=\frac1{a(a+1)},\qquad
p_0:=1-\frac1a,\qquad
p_+:=\frac1{a+1}.
\tag{10}
\]

They satisfy

\[
p_-+p_0+p_+=1
\tag{11}
\]

and, in lattice units,

\[
-a p_-+p_+=0.
\tag{12}
\]

Equation (12) is exactly the martingale/barycentric condition. Since the displacements in physical log-coordinate are `-ah` and `+h`, it proves (5).

The conditional variance at the modified point is

\[
\begin{aligned}
Q_R(y_j)
&=p_-(ah)^2+p_+h^2\\
&=h^2\left(\frac{a}{a+1}+\frac1{a+1}\right)\\
&=h^2.
\end{aligned}
\tag{13}
\]

Every other row is deterministic, so the defect vanishes elsewhere. This proves (7). By the Stinespring factorization already used in `WP-332`--`WP-334`,

\[
Q_R=
\bigl((I-P_R)\pi_R(X_R)V_R\bigr)^*
\bigl((I-P_R)\pi_R(X_R)V_R\bigr),
\tag{14}
\]

hence

\[
\|(I-P_R)\pi_R(X_R)V_R\|=h.
\tag{15}
\]

The asymmetry is load-bearing. A symmetric jump of growing radius would have to deposit too much relative mass onto the exponentially lighter forward tail. Here the long jump goes backward toward a much heavier atom with probability `O(a^{-2})`, while the compensating one-step forward jump has probability only `O(a^{-1})`.

## 2. The scalar likelihood ratio converges uniformly to one

Only the center and its two targets change under the transformed state. Let

\[
L_R=\frac{d\nu_R'}{d\nu_R}.
\tag{16}
\]

At the center,

\[
L_R(y_j)=1-\frac1a.
\tag{17}
\]

At the backward target,

\[
L_R(y_{j-a})
=1+\frac1{a(a+1)}\frac{w_{j,R}}{w_{j-a,R}},
\tag{18}
\]

and at the forward target,

\[
L_R(y_{j+1})
=1+\frac1{a+1}\frac{w_{j,R}}{w_{j+1,R}}.
\tag{19}
\]

All remaining values equal one. From (1), normalization cancels in ratios and

\[
\frac{w_{j,R}}{w_{j-a,R}}
=2^{-as}\frac{2^{j-a}+1}{2^j+1}
\le 2^{-as},
\tag{20}
\]

while

\[
\frac{w_{j,R}}{w_{j+1,R}}
=2^s\frac{2^{j+1}+1}{2^j+1}
<2^{s+1}.
\tag{21}
\]

Therefore

\[
1-\frac1a
\le L_R
\le
1+\frac{2^{s+1}}{a+1}
\tag{22}
\]

throughout the support. Since `a_R->infinity`,

\[
\|L_R-1\|_\infty=O_s(a_R^{-1})\to0.
\tag{23}
\]

For mutually absolutely continuous discrete laws, order-infinity Renyi divergence is the logarithm of the maximal likelihood ratio. Thus

\[
D_\infty(\nu_R'\|\nu_R)
\le
\log\left(1+\frac{2^{s+1}}{a_R+1}\right)
\to0,
\tag{24}
\]

and

\[
D_\infty(\nu_R\|\nu_R')
\le
-\log\left(1-\frac1{a_R}\right)
\to0.
\tag{25}
\]

This strictly strengthens the scalar convergence in `WP-334`: once the likelihood ratios converge uniformly to one, every fixed finite-order Renyi divergence and every ordinary continuous `f`-divergence also vanishes.

## 3. The readout itself converges uniformly on bounded functions

Only one row of `Psi_R-I` is nonzero. At that row the signed measure is

\[
p_-\delta_{y_{j-a}}+p_+\delta_{y_{j+1}}-(p_-+p_+)\delta_{y_j}.
\tag{26}
\]

Its total variation norm is

\[
2(p_-+p_+)=\frac2a.
\tag{27}
\]

The norm is attained by a sup-norm-one function taking value `+1` at the two target points and `-1` at the center. Hence (9) is exact.

This removes another possible repair of `WP-333`: one cannot rescue cutoff-uniform source rigidity merely by requiring the finite Markov/UCP readouts themselves to approach the identity in ordinary operator norm.

There is no contradiction with continuity theorems for channels or Stinespring dilations. The quantity being tested here is not a fixed bounded observable as `R` changes. The logarithmic coordinate grows with the cutoff,

\[
\|X_R\|\asymp R,
\tag{28}
\]

and its square grows like `R^2`. Small channel error on the unit ball can therefore coexist with a nonvanishing error on this moving unbounded-energy observable.

## 4. The second-moment scalar error is still exponentially invisible

Because `Q_R` is supported only at `y_j`,

\[
\tau_R(Q_R)=w_{j,R}h^2.
\tag{29}
\]

Here `j=k_R-1`, so the same elementary dyadic estimate as in `WP-333` gives

\[
w_{j,R}\le C_s e^{-(s+1)R}
\tag{30}
\]

up to an `s`-dependent constant. Thus the scalar second-moment discrepancy tends to zero exponentially while the operator defect remains exactly `h^2`.

This sharpens the conditioning statement of `WP-333`. The problem is not only that the faithful state gives tiny weight to the tail. Even after imposing a likelihood-ratio error that is **uniformly small at every atom**, the conditional variance can remain fixed because the transition geometry uses increasing displacement.

## 5. Matched control and falsification

The construction does not use prime selectivity. Consider any equally spaced ray `x_j=jh` carrying positive weights with a uniformly bounded one-step forward ratio

\[
\sup_j \frac{w_j}{w_{j+1}}<\infty
\tag{31}
\]

and with enough points to the left. Choose `a_j->infinity`, `a_j<j`, and use exactly the probabilities (10) from `x_j` to `x_{j-a_j}`, `x_j`, and `x_{j+1}`. Then the coordinate is fixed, the conditional variance is `h^2`, the channel norm distance is `2/a_j`, and the forward-target likelihood perturbation is `O(1/a_j)`. If in addition the backward target is not exponentially lighter than the center—in particular for any geometrically decreasing tail—it also has vanishing relative perturbation.

So the mechanism is generic. It does **not** distinguish Mangoldt support, produce the Gamma term, create the pole counterterms, or orient the Weil explicit formula. It is valuable only as a falsifier of an attempted global rigidity principle.

The strongest direct falsifier of this finding would be an overlooked support or cutoff violation. There is none: by construction `j_R+1=k_R` lies at or below the cutoff, while `j_R-a_R>=1` for large `R`; all three points are genuine powers of the same prime `2` and hence belong to the exact finite Mangoldt support.

## 6. Prior-art and novelty audit

Kadison--Schwarz positivity, multiplicative domains, Stinespring dilation, martingale kernels, and order-infinity Renyi divergence are classical. `WP-333` already anchored the martingale-coupling perspective, and `WP-334` already anchored the fact that `D_infinity` is a maximum likelihood-ratio quantity. No theorem-level novelty is claimed for any of those ingredients.

The searched prior-art surface also contains continuity theorems for Stinespring dilations and energy-constrained channel metrics. Those results do not state the false implication ruled out here—namely that convergence of channels on bounded observables or convergence of a scalar likelihood ratio controls the Kadison defect of a cutoff-dependent observable whose norm diverges. Rather, they reinforce the correct redirect: once observables are unbounded or their energy scale grows, the topology must include the relevant energy/moment control.

The Mathia-specific delta is therefore narrow but substantive: on the **intrinsic dyadic prime-power support of the canonical Mangoldt source**, an explicit source-preserving UCP self-map closes the max-divergence loophole left by `WP-334` while keeping the exact source coordinate and a fixed Stinespring coupling.

## 7. Consequence for the Weil-positivity search

The stability boundary is now sharper:

\[
\text{finite faithful exact law}
\Longrightarrow
\text{multiplicative-domain rigidity}
\tag{32}
\]

at each cutoff, but none of the following asymptotic conditions alone globalizes it for the logarithmic source coordinate:

\[
\text{TV / finite moments / fixed Wasserstein}
\quad\text{(`WP-333`),}
\tag{33}
\]

\[
\text{finite-order information divergences}
\quad\text{(`WP-334`),}
\tag{34}
\]

or even

\[
\text{two-sided }D_\infty\to0
+\text{ ordinary channel-norm convergence}
\quad\text{(this finding).}
\tag{35}
\]

A future obstruction or positive construction must therefore control the **moving observable together with the map**. Natural candidates are an energy-constrained/channel graph norm, a uniform quadratic-form estimate on the source domain, or a source-forced Dirichlet/variance bound that sees displacement cost before scalarization. Merely strengthening the probability-law metric is not enough.

This still does not provide the missing global Weil-positive geometry. It removes a tempting analytic shortcut and leaves a more precise target: any intrinsic finite-to-infinite UCP architecture must prove positivity in a topology strong enough to control the unbounded logarithmic arithmetic coordinate and simultaneously generate the archimedean/global terms.
