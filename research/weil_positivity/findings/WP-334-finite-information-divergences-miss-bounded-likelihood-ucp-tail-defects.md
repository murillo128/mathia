---
id: WP-334
title: Finite information divergences miss bounded-likelihood UCP tail defects while max-divergence detects them
branch: weil_positivity
status: supported
kind: information-topology-ucp-tail-obstruction
claim_strength: exact support-preserving Mangoldt-tail construction showing that an order-one Kadison/Stinespring defect can coexist with mutually absolutely continuous scalar laws whose likelihood ratios are uniformly bounded and whose two-sided Csiszar f-divergences and every fixed finite-order Renyi divergence vanish, while order-infinity Renyi divergence stays bounded away from zero
created: 2026-09-16
related: [WP-023, WP-331, WP-332, WP-333]
prior_art:
  - Imre Csiszar, Information-type measures of difference of probability distributions and indirect observations, Studia Scientiarum Mathematicarum Hungarica 2 (1967), 299-318
  - Tim van Erven and Peter Harremoes, Renyi Divergence and Kullback-Leibler Divergence, IEEE Transactions on Information Theory 60 (2014), no. 7, 3797-3820, DOI 10.1109/TIT.2014.2320500, arXiv:1206.2459
  - Igal Sason and Sergio Verdu, f-Divergence Inequalities, IEEE Transactions on Information Theory 62 (2016), no. 11, 5973-6006, DOI 10.1109/TIT.2016.2603151, arXiv:1508.00335
---

# WP-334 — Finite information divergences miss bounded-likelihood UCP tail defects while max-divergence detects them

## Claim

`WP-333` showed that the exact finite-cutoff UCP rigidity of `WP-332` is nonuniform: on three consecutive points of the intrinsic dyadic prime-power ray, a support-preserving martingale self-map can keep an order-one Kadison defect while its scalar law returns to the Mangoldt source in total variation, every fixed polynomial moment, and every fixed Wasserstein metric. One possible repair was to require a stronger scalar topology, for example relative entropy or another information divergence.

That repair still fails for every ordinary averaged information divergence of fixed finite order.

Fix `s>0` and `epsilon in (0,1)`. At the same finite Mangoldt cutoff and the same dyadic triple used in `WP-333`, let

\[
y_R-h,\qquad y_R,\qquad y_R+h,
\qquad h=\log 2,
\tag{1}
\]

with center mass

\[
r_R=\nu_R(\{y_R\})\longrightarrow0.
\tag{2}
\]

Define the lazy martingale UCP self-map

\[
\Psi_{R,\epsilon}:C(\Sigma_R)\to C(\Sigma_R)
\tag{3}
\]

to be the identity away from `y_R`, while at the center

\[
\Psi_{R,\epsilon}(f)(y_R)
=
\epsilon f(y_R)
+\frac{1-\epsilon}{2}f(y_R-h)
+\frac{1-\epsilon}{2}f(y_R+h).
\tag{4}
\]

For the coordinate `X_R(t)=t`,

\[
\Psi_{R,\epsilon}(X_R)=X_R
\tag{5}
\]

exactly, but its Kadison defect is

\[
Q_{R,\epsilon}
=
\Psi_{R,\epsilon}(X_R^2)
-\Psi_{R,\epsilon}(X_R)^2,
\tag{6}
\]

with

\[
Q_{R,\epsilon}(y_R)
=
(1-\epsilon)(\log2)^2
\tag{7}
\]

and zero elsewhere. Hence

\[
\boxed{
\|Q_{R,\epsilon}\|
=
(1-\epsilon)(\log2)^2
}
\tag{8}
\]

for every cutoff. In Stinespring form the off-diagonal source coupling therefore has norm

\[
\boxed{
\sqrt{1-\epsilon}\,\log2,
}
\tag{9}
\]

again independent of `R`.

Let `nu_R'` be the scalar source law under the transformed state `tau_R o Psi_{R,epsilon}`. Then `nu_R` and `nu_R'` have the **same support** and are mutually absolutely continuous. More strongly, their likelihood ratio

\[
L_R=\frac{d\nu_R'}{d\nu_R}
\tag{10}
\]

is trapped between positive constants depending only on `s` and `epsilon`, not on `R`:

\[
\boxed{
\epsilon\le L_R\le 1+(1-\epsilon)2^s.
}
\tag{11}
\]

Nevertheless, for every finite-valued continuous convex `f:(0,infinity)->R` with `f(1)=0`,

\[
D_f(\nu_R'\|\nu_R)=O_f(r_R)\to0,
\qquad
D_f(\nu_R\|\nu_R')=O_f(r_R)\to0.
\tag{12}
\]

Thus KL in **both** directions, chi-square, squared Hellinger, Jensen-Shannon, total variation, and every other ordinary Csiszar `f`-divergence with finite values on positive compact intervals all miss the order-one operator defect.

The same sharpens for Renyi divergence. For every fixed finite order `alpha in (0,infinity)`,

\[
D_\alpha(\nu_R'\|\nu_R)\to0,
\qquad
D_\alpha(\nu_R\|\nu_R')\to0.
\tag{13}
\]

At order infinity the behavior changes:

\[
D_\infty(\nu_R\|\nu_R')
=
\log\frac1\epsilon,
\tag{14}
\]

while

\[
D_\infty(\nu_R'\|\nu_R)
\longrightarrow
\log\!\left(1+(1-\epsilon)2^s\right)>0.
\tag{15}
\]

So the same intrinsic UCP tail escape produces a clean topology threshold:

\[
\boxed{
\text{all fixed finite averaged information divergences vanish}
\quad\text{but}\quad
D_\infty\text{ remains order one}.
}
\tag{16}
\]

Consequently the scalar topology needed to globalize `WP-332` cannot merely be "stronger than total variation" in an averaged information-theoretic sense. It must control the likelihood ratio **uniformly on rare atoms** (an `L^infinity`/max-divergence type condition), beat the vanishing faithfulness modulus from `WP-333`, or control the UCP map/operator geometry directly.

This is a negative boundary result, not a Weil-positivity mechanism. The construction is generic on any equally spaced tail whose neighboring masses are uniformly comparable. Its value is to rule out a broad and natural attempted repair of the live UCP route.

**Classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE + UCP-READOUT + INFORMATION-DIVERGENCE + BOUNDED-LIKELIHOOD + RENYI-THRESHOLD + MOVING-TAIL + MATCHED-CONTROL + NOT-WEIL-POSITIVITY`.

## Evidence class

The operator part is the explicit commutative UCP construction of `WP-333` with one added laziness parameter `epsilon`. The information-divergence estimates are finite-sum identities and uniform likelihood-ratio bounds. No zero data, RH assumption, prime-number theorem, analytic continuation, numerical fit, or regularization enters.

Csiszar `f`-divergences and Renyi divergences are classical. No theorem-level novelty is claimed for their definitions, continuity on bounded likelihood-ratio classes, or the fact that order-infinity Renyi divergence is a max-likelihood-ratio quantity. The Mathia-specific delta is the exact placement of those standard information topologies around the intrinsic Mangoldt-tail UCP counterexample: even **two-sided relative-entropy-strength convergence with mutual absolute continuity and uniformly bounded density ratios** does not recover the order-one operator defect.

## 1. The lazy intrinsic martingale keeps the source coordinate but not its square

Use the finite pole-normalized Mangoldt source from `WP-333`,

\[
a_n=\frac{\Lambda(n)}{n+1}n^{-s},
\qquad
\nu_R(\{\log n\})=\frac{a_n}{Z_R},
\qquad s>0.
\tag{17}
\]

Let `j_R` be the moving dyadic index from that finding and set

\[
y_R=j_R\log2,
\qquad h=\log2.
\tag{18}
\]

For all sufficiently large `R`, the points `y_R-h`, `y_R`, and `y_R+h` lie in the exact finite source support. Equation (4) is a Markov operator, hence a unital completely positive map because the algebra is commutative.

The barycentric identity

\[
\epsilon y_R
+\frac{1-\epsilon}{2}(y_R-h)
+\frac{1-\epsilon}{2}(y_R+h)
=
y_R
\tag{19}
\]

proves (5). For the square,

\[
\begin{aligned}
\Psi_{R,\epsilon}(X_R^2)(y_R)
&=
\epsilon y_R^2
+\frac{1-\epsilon}{2}(y_R-h)^2
+\frac{1-\epsilon}{2}(y_R+h)^2\\
&=
y_R^2+(1-\epsilon)h^2.
\end{aligned}
\tag{20}
\]

This gives (7)-(8). The Stinespring factorization used in `WP-332`--`WP-333`,

\[
Q_{R,\epsilon}
=
\bigl((I-P_R)\pi_R(X_R)V_R\bigr)^*
\bigl((I-P_R)\pi_R(X_R)V_R\bigr),
\tag{21}
\]

then gives (9).

The map itself also stays a fixed distance from the identity. Taking a sup-norm-one function equal to `1` at `y_R` and `-1` at the two neighbors yields

\[
\|(\Psi_{R,\epsilon}-I)f_R\|_\infty
=2(1-\epsilon),
\tag{22}
\]

and the reverse inequality follows from the norm of the three-point signed averaging functional. Thus

\[
\boxed{
\|\Psi_{R,\epsilon}-I\|=2(1-\epsilon).
}
\tag{23}
\]

There is no hidden convergence at the map level.

## 2. The transformed law remains uniformly equivalent to the source law

Write

\[
w_-=\nu_R(\{y_R-h\}),
\qquad
r_R=\nu_R(\{y_R\}),
\qquad
w_+=\nu_R(\{y_R+h\}).
\tag{24}
\]

Only these three masses change:

\[
\begin{aligned}
\nu_R'(y_R)&=\epsilon r_R,\\
\nu_R'(y_R-h)&=w_-+\frac{1-\epsilon}{2}r_R,\\
\nu_R'(y_R+h)&=w_++\frac{1-\epsilon}{2}r_R.
\end{aligned}
\tag{25}
\]

For the dyadic weights (17),

\[
\frac{r_R}{w_-}
=
2^{-s}\frac{2^{j_R-1}+1}{2^{j_R}+1},
\tag{26}
\]

and

\[
\frac{r_R}{w_+}
=
2^s\frac{2^{j_R+1}+1}{2^{j_R}+1}.
\tag{27}
\]

For every `j_R>=1`,

\[
2^{-(s+1)}
<
\frac{r_R}{w_-}
\le
\frac23\,2^{-s},
\tag{28}
\]

while

\[
\frac{r_R}{w_+}<2^{s+1}.
\tag{29}
\]

Therefore

\[
w_-\le 2^{s+1}r_R,
\qquad
w_+\le 2^{-s}r_R,
\tag{30}
\]

where the second bound is deliberately nonsharp but uniform.

The likelihood ratio is

\[
L_R=
\begin{cases}
\epsilon,& y=y_R,\\[2mm]
1+\dfrac{1-\epsilon}{2}\dfrac{r_R}{w_-},& y=y_R-h,\\[3mm]
1+\dfrac{1-\epsilon}{2}\dfrac{r_R}{w_+},& y=y_R+h,\\[3mm]
1,& \text{otherwise}.
\end{cases}
\tag{31}
\]

Equations (28)-(29) imply (11). In particular both `L_R` and `L_R^{-1}` are uniformly bounded:

\[
\epsilon\le L_R\le C_{s,\epsilon},
\qquad
C_{s,\epsilon}:=1+(1-\epsilon)2^s,
\tag{32}
\]

and hence

\[
C_{s,\epsilon}^{-1}
\le
\frac{d\nu_R}{d\nu_R'}
\le
\epsilon^{-1}.
\tag{33}
\]

This removes two possible objections to `WP-333`: no support point disappears, and the escape does not rely on a likelihood ratio blowing up on the moving tail.

## 3. Every ordinary two-sided f-divergence still vanishes

Let `f:(0,infinity)->R` be continuous and convex with `f(1)=0`. The Csiszar divergence is

\[
D_f(P\|Q)
=
\int f\!\left(\frac{dP}{dQ}\right)dQ.
\tag{34}
\]

Since `L_R=1` outside the three affected atoms,

\[
D_f(\nu_R'\|\nu_R)
=
\sum_{\{y_R-h,y_R,y_R+h\}}
\nu_R(y)\,f(L_R(y)).
\tag{35}
\]

By (30), the total original mass of those atoms is at most

\[
(1+2^{s+1}+2^{-s})r_R.
\tag{36}
\]

By (32), `L_R` lies in the fixed compact interval `[epsilon,C_{s,epsilon}]`, so

\[
M_f
:=
\sup_{\epsilon\le t\le C_{s,\epsilon}}|f(t)|
<\infty.
\tag{37}
\]

Hence

\[
0\le D_f(\nu_R'\|\nu_R)
\le
M_f(1+2^{s+1}+2^{-s})r_R
\longrightarrow0.
\tag{38}
\]

For the reverse direction, use (33). The transformed mass of the same three atoms is at most `C_{s,epsilon}` times their original mass, and `1/L_R` lies in the compact interval `[C_{s,epsilon}^{-1},epsilon^{-1}]`. Therefore another finite constant `M_f'` gives

\[
0\le D_f(\nu_R\|\nu_R')
\le
M_f' C_{s,\epsilon}(1+2^{s+1}+2^{-s})r_R
\longrightarrow0.
\tag{39}
\]

Thus the failure is not a one-sided KL pathology. Mutual absolute continuity and bounded likelihood ratios allow every standard finite `f`-divergence to ignore an order-one positive operator defect when that defect moves onto a source atom of vanishing mass.

This differs from `WP-023`. There the information divergence was taken along the prime-torus Poisson parameter family and its critical limit lost the Weil coefficients through Fisher/pole geometry. Here the probability laws themselves are asymptotically indistinguishable by the whole `f`-divergence class even though the underlying UCP source coupling does **not** converge.

## 4. Every fixed finite Renyi order vanishes

For `alpha in (0,infinity)`, `alpha != 1`, write

\[
D_\alpha(P\|Q)
=
\frac{1}{\alpha-1}
\log
\int
\left(\frac{dP}{dQ}\right)^\alpha dQ.
\tag{40}
\]

With `P=nu_R'`, `Q=nu_R`, the integral differs from `1` only on the three affected atoms:

\[
\int L_R^\alpha\,d\nu_R
=
1+
\sum_{\{y_R-h,y_R,y_R+h\}}
\nu_R(y)\bigl(L_R(y)^\alpha-1\bigr).
\tag{41}
\]

Because `L_R` remains in the fixed compact interval (32), the summand factor is uniformly bounded for every fixed finite `alpha`. Equation (36) therefore gives

\[
\int L_R^\alpha\,d\nu_R
=
1+O_{\alpha,s,\epsilon}(r_R),
\tag{42}
\]

hence

\[
D_\alpha(\nu_R'\|\nu_R)
=
O_{\alpha,s,\epsilon}(r_R)
\longrightarrow0.
\tag{43}
\]

The reverse direction is identical using (33). At `alpha=1` this is already covered by KL in (38)-(39), and at `alpha=0` both order-zero divergences vanish exactly because the supports coincide.

Therefore every fixed finite Renyi order sees the two scalar laws converge even though (8), (9), and (23) remain order one.

## 5. Order infinity is the sharp scalar threshold for this escape

The order-infinity Renyi divergence is the max-likelihood ratio,

\[
D_\infty(P\|Q)
=
\log \left\|\frac{dP}{dQ}\right\|_\infty.
\tag{44}
\]

For the reverse direction, the minimum likelihood ratio in (31) is exactly `epsilon`, so

\[
\boxed{
D_\infty(\nu_R\|\nu_R')
=
\log(1/\epsilon)
}
\tag{45}
\]

for every sufficiently large `R`.

In the forward direction the largest ratio is attained at the upper dyadic neighbor for large `R`. From (27),

\[
\frac{r_R}{w_+}
\longrightarrow 2^{s+1},
\tag{46}
\]

and therefore

\[
\boxed{
D_\infty(\nu_R'\|\nu_R)
\longrightarrow
\log\!\left(1+(1-\epsilon)2^s\right).
}
\tag{47}
\]

The scalar distinction is thus not "weak metrics versus information metrics." It is **averaged versus uniform relative control**. Every fixed finite information order averages the discrepancy against an atom whose source mass tends to zero. `D_infinity`, by contrast, records the worst relative change independently of that atom's mass and therefore does not forget the moving defect.

This matches the faithfulness-modulus inequality of `WP-333`. There one needs scalar Kadison defect `o(m_R)` to force sup-norm defect to zero. Here the same boundary reappears probabilistically: only a topology that refuses to discount arbitrarily light source atoms can prevent the UCP escape.

## 6. Matched controls and falsification boundary

Nothing in the information-divergence argument is arithmetically selective. The same construction works on any family of probability measures containing a moving three-point arithmetic progression

\[
x_R-h,\ x_R,\ x_R+h
\tag{48}
\]

whose center mass tends to zero and whose two neighboring masses remain comparable to it by cutoff-independent constants. The lazy barycentric Markov row then fixes the coordinate, retains an order-one conditional variance `(1-epsilon)h^2`, and changes every finite averaged information divergence by only the total mass of those three atoms.

The dyadic Mangoldt ray matters only because it supplies such a triple **intrinsically**, with exact logarithmic spacing and explicit local mass ratios. Hence (16) is a matched-control obstruction, not a source-selective sign theorem.

Several escape routes remain genuinely outside the claim.

1. A scalar topology controlling `||dnu_R'/dnu_R-1||_infinity` or `D_infinity` can detect this counterexample. Such a condition must itself be derived canonically from the proposed geometry; imposing it only because weaker topologies fail is not a Weil mechanism.
2. Direct norm/cb-norm control of the UCP maps can exclude the example because (23) stays order one.
3. A source-derived positive form may use another observable or a joint finite--archimedean response rather than infer operator geometry from convergence of one scalar law.
4. An arithmetic theorem could supply a uniform lower bound or relative-faithfulness estimate on precisely the sector carrying the Kadison defect. `WP-333` shows that the raw Mangoldt cutoff state does not supply such a bound by itself.
5. A topology whose order grows with the cutoff can approach max-divergence. The present claim is only for each **fixed** finite order; allowing `alpha=alpha_R->infinity` changes the hypothesis and must be audited quantitatively.

A falsification of the claimed threshold would require a standard finite-valued `f`-divergence or fixed finite Renyi order for which (38), (39), or (43) does not vanish under the explicit likelihood ratios (31). Since the ratios stay in a fixed positive compact interval and only `O(r_R)` total mass is modified, such a counterexample would contradict the displayed finite-sum bounds.

## 7. Prior-art and novelty audit

Csiszar's `f`-divergence framework and Renyi divergence are classical. Van Erven--Harremoes gives a modern systematic account of finite-order and order-infinity Renyi divergence, including the KL limit at order one. Sason--Verdu studies `f`-divergence and Renyi bounds under bounded relative information, including reverse-Pinsker-type control. Thus the implication "bounded likelihood ratios + vanishing rare-event mass/TV implies vanishing fixed finite information divergences" is firmly classical; the bounds above are direct finite-sum instances, not a new information-theory theorem.

The UCP/Kadison/Stinespring side is likewise classical and was already audited in `WP-332`--`WP-333`. The lazy Markov kernel in (4) is a standard martingale-kernel modification, not a new probabilistic object.

The durable research delta is narrower and Mathia-specific: the support-preserving counterexample of `WP-333` can be strengthened so that **both** scalar laws remain uniformly equivalent, all two-sided finite information divergences vanish, yet the positive operator defect and Stinespring coupling remain fixed. This closes the natural suggestion that KL, chi-square, Hellinger, finite Renyi order, or another ordinary information divergence might supply the missing uniformity needed to pass from finite faithful UCP rigidity to a global theorem.

The mechanism is not classical Weil positivity, Frobenius/cohomology, Hilbert--Polya, Connes trace geometry, Sonin localization, or an intersection-form theorem. It proves no RH-equivalent positivity and imports no zero data. It only narrows which convergence/interface structures could possibly transport an independently positive Mathia geometry to the global Weil criterion.

## Consequence for the research line

After `WP-333`, the live operator-valued question was whether a stronger scalar convergence notion could prevent thin-tail coupling from evading exact finite-cutoff rigidity. `WP-334` gives a sharp negative answer for the broad information-theoretic class:

\[
\boxed{
\text{upgrading TV / moments / fixed Wasserstein convergence}
\ \text{to all fixed finite }f\text{/Renyi information tests}
\ \text{still does not control the Kadison/Stinespring defect}.
}
\tag{49}
\]

For this intrinsic tail escape, max-divergence or an equivalent uniform likelihood-ratio condition is the first scalar information scale that remains nonvanishing. The surviving frontier is therefore narrower: a useful global positivity bridge must either derive such uniform relative control from the source itself, work in a genuinely stronger map/operator topology, change the observable/readout architecture, or produce a source-selective sign theorem in which the moving operator coupling remains visible before scalar averaging.

Simply replacing weak scalar convergence by a conventional finite information divergence is no longer an open repair.
