---
id: WP-337
title: Approximate barycentric preservation needs bias times propagation control
branch: weil_positivity
status: supported
kind: approximate-ucp-propagation-rigidity-boundary
claim_strength: exact sharp rowwise variance bound for finite commutative Markov/UCP self-maps with nonzero source-coordinate bias; the intrinsic dyadic Mangoldt ray realizes a one-sided long-jump family whose channel norm, two-sided max-divergence, and absolute coordinate bias all vanish while its Kadison defect stays order one, proving that the WP-336 bidirectional-product criterion is nonuniform under merely asymptotic barycentric preservation
created: 2026-09-16
related: [WP-332, WP-333, WP-334, WP-335, WP-336]
prior_art:
  - Rajendra Bhatia and Chandler Davis, A Better Bound on the Variance, The American Mathematical Monthly 107 (2000), no. 4, 353-357, DOI 10.1080/00029890.2000.12005203
  - Richard V. Kadison, A Generalized Schwarz Inequality and Algebraic Invariants for Operator Algebras, Annals of Mathematics 56 (1952), 494-503, DOI 10.2307/1969657
  - W. Forrest Stinespring, Positive Functions on C*-Algebras, Proceedings of the American Mathematical Society 6 (1955), 211-216, DOI 10.1090/S0002-9939-1955-0069403-4
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
---

# WP-337 — Approximate barycentric preservation needs bias times propagation control

## Claim

`WP-336` gave the sharp stability law for a commutative Markov/UCP readout that preserves the real source coordinate exactly. If the row at `x` moves mass `epsilon_x` and reaches distances `L_-(x)` and `L_+(x)` on the two sides, exact barycentric preservation implies

\[
0\le K(x)\le \varepsilon_x L_-(x)L_+(x),
\]

where `K=Psi(X^2)-Psi(X)^2` is the Kadison defect. This made **bidirectional** propagation the exact price of an order-one defect under small channel norm.

That conclusion is not stable under merely asymptotic preservation of the source coordinate. The missing term can be computed sharply.

Let `Sigma` be a finite subset of the real line, `X(t)=t`, and

\[
\Psi:C(\Sigma)\to C(\Sigma)
\]

be a Markov/UCP self-map with transition law `P_x` at `x`. Define

\[
\varepsilon_x:=1-P_x(\{x\}),
\qquad
\beta_x:=\Psi(X)(x)-x,
\]

and

\[
L_-(x):=x-\min\operatorname{supp}P_x,
\qquad
L_+(x):=\max\operatorname{supp}P_x-x.
\]

Then the Kadison defect

\[
K:=\Psi(X^2)-\Psi(X)^2\ge0
\]

satisfies the sharp pointwise inequality

\[
\boxed{
K(x)
\le
\varepsilon_xL_-(x)L_+(x)
+\beta_x\bigl(L_+(x)-L_-(x)\bigr)
-\beta_x^2.
}
\tag{1}
\]

Equality holds whenever, conditional on leaving `x`, the transition is supported at the two propagation endpoints. In particular, one-sided endpoint jumps are equality cases.

Since

\[
\|\Psi-I\|=2\sup_x\varepsilon_x,
\tag{2}
\]

(1) implies the uniform stability estimate

\[
\boxed{
\|K\|
\le
\frac12\|\Psi-I\|B(\Psi,X)
+\|\Psi(X)-X\|\,A(\Psi,X),
}
\tag{3}
\]

with

\[
B(\Psi,X):=\sup_xL_-(x)L_+(x),
\qquad
A(\Psi,X):=\sup_x|L_+(x)-L_-(x)|.
\tag{4}
\]

Thus approximate multiplicative-domain rigidity follows if **both** scale-corrected errors vanish,

\[
\|\Psi_R-I\|B_R\to0,
\qquad
\|\Psi_R(X_R)-X_R\|A_R\to0.
\tag{5}
\]

The second condition is essential. On the intrinsic dyadic prime-power ray there is a support-preserving UCP family for which

\[
\|\Psi_R-I\|\to0,
\qquad
\|\Psi_R(X_R)-X_R\|\to0,
\tag{6}
\]

and even both max-divergences between the transformed and original scalar Mangoldt laws tend to zero, while

\[
\boxed{
\|K_R\|\to(\log2)^2.
}
\tag{7}
\]

The construction uses only a **one-sided** long backward jump, so

\[
B_R=0
\tag{8}
\]

identically. Its entire fixed defect is carried by the new bias-times-asymmetry term in (1).

Therefore the sharp `WP-336` bidirectional-propagation criterion cannot be extended by replacing exact barycentric preservation with the unweighted requirement `||Psi_R(X_R)-X_R||->0`. Once exact preservation is relaxed, a vanishing first-moment bias can be amplified by a diverging one-sided propagation radius into an order-one second-moment defect.

This is again a negative boundary theorem, not a Weil-positivity mechanism. The same construction works on generic equally spaced geometric tails. Its value is to close the explicit approximate-barycenter loophole left by `WP-336` and identify the additional moving-scale quantity that any surviving UCP route must control.

**Classification:** `EXACT-DERIVED + LITERATURE-BACKED + SHARP-BOUNDARY + UCP-READOUT + APPROXIMATE-MARTINGALE + BIAS-PROPAGATION + ONE-SIDED-TAIL + MAX-DIVERGENCE + MATCHED-CONTROL + DECISIVE-NEGATIVE + NOT-WEIL-POSITIVITY`.

## 1. Exact biased variance bound

Fix `x` and let

\[
Z=t-x
\]

under `P_x`. Then

\[
\mathbb E Z=\beta_x,
\qquad
K(x)=\operatorname{Var}(Z).
\tag{9}
\]

If `epsilon_x=0`, then `Z=0`, `beta_x=0`, and (1) is trivial. Assume `epsilon_x>0` and condition on the event `Z!=0`. Let `W` denote the conditional displacement. Its mean is

\[
\mu_x:=\mathbb E W=\frac{\beta_x}{\varepsilon_x},
\tag{10}
\]

and its support lies in

\[
-L_-(x)\le W\le L_+(x).
\tag{11}
\]

The Bhatia--Davis variance inequality gives

\[
\operatorname{Var}(W)
\le
\bigl(L_+(x)-\mu_x\bigr)
\bigl(\mu_x+L_-(x)\bigr).
\tag{12}
\]

Equivalently,

\[
\mathbb E W^2
\le
L_-(x)L_+(x)
+\mu_x\bigl(L_+(x)-L_-(x)\bigr).
\tag{13}
\]

Because `Z` equals zero with probability `1-epsilon_x` and equals `W` with probability `epsilon_x`,

\[
\begin{aligned}
K(x)
&=\mathbb E Z^2-(\mathbb EZ)^2\\
&=\varepsilon_x\mathbb EW^2-\beta_x^2\\
&\le
\varepsilon_xL_-(x)L_+(x)
+\beta_x\bigl(L_+(x)-L_-(x)\bigr)
-\beta_x^2.
\end{aligned}
\tag{14}
\]

This proves (1).

The estimate is sharp because Bhatia--Davis is sharp for distributions supported on the two endpoints. The equality condition is exactly the geometry relevant here: after the stationary atom at `x` is removed, all transported mass may sit at the extreme accessible displacements.

When `beta_x=0`, (14) reduces to the `WP-336` law

\[
K(x)\le\varepsilon_xL_-(x)L_+(x).
\tag{15}
\]

So `WP-336` is the exact zero-bias face of the more general inequality rather than a generic continuity statement around that face.

## 2. The global stability modulus acquires a bias-propagation term

Dropping the favorable term `-beta_x^2` and bounding the signed asymmetry term by absolute value gives

\[
K(x)
\le
\varepsilon_xL_-(x)L_+(x)
+|\beta_x|\,|L_+(x)-L_-(x)|.
\tag{16}
\]

For a Markov kernel on `C(Sigma)`, the same row total-variation calculation as in `WP-336` gives

\[
\|\Psi-I\|=2\sup_x\varepsilon_x.
\tag{17}
\]

Taking suprema in (16) proves (3).

This separates two genuinely different resources. The first term prices random off-diagonal escape under exact barycentric cancellation. The second prices deterministic first-moment drift against **propagation asymmetry**. A small absolute drift is harmless only when the geometry prevents it from being levered by an increasingly long one-sided displacement.

The sufficient asymptotic condition is therefore not merely

\[
\|\Psi_R-I\|\to0,
\qquad
\|\Psi_R(X_R)-X_R\|\to0.
\tag{18}
\]

It is the scale-aware pair (5). This is the direct analogue, for approximate barycentric preservation, of the channel-error-times-propagation correction isolated by `WP-336`.

## 3. Intrinsic dyadic Mangoldt counterexample

Use the finite pole-normalized Mangoldt source from `WP-333`--`WP-336`. Fix `s>0`, put

\[
h=\log2,
\qquad
y_j=jh,
\]

and along the dyadic prime-power ray write

\[
w_{j,R}=\nu_R(\{y_j\})
\propto
\frac{h\,2^{-js}}{2^j+1}.
\tag{19}
\]

Let

\[
k_R=\left\lfloor\frac{R}{h}\right\rfloor,
\qquad
j_R=k_R-1,
\qquad
a_R=\left\lfloor\frac{j_R}{2}\right\rfloor.
\tag{20}
\]

For sufficiently large `R`, both `y_{j_R}` and `y_{j_R-a_R}` belong to the intrinsic cutoff support and `a_R->infinity`.

Define `Psi_R` to be the identity at every source point except `y_{j_R}`. At that row set

\[
\Psi_R(f)(y_{j_R})
=
\left(1-\frac1{a_R^2}\right)f(y_{j_R})
+\frac1{a_R^2}f(y_{j_R-a_R}).
\tag{21}
\]

This is a support-preserving Markov/UCP self-map. The only nonzero displacement is the backward jump

\[
-a_Rh.
\tag{22}
\]

Hence

\[
\varepsilon_R=\frac1{a_R^2},
\qquad
L_{-,R}=a_Rh,
\qquad
L_{+,R}=0.
\tag{23}
\]

In particular the bidirectional product from `WP-336` vanishes exactly:

\[
L_{-,R}L_{+,R}=0.
\tag{24}
\]

The source-coordinate bias at the modified row is

\[
\beta_R
=-\frac{h}{a_R},
\tag{25}
\]

so

\[
\boxed{
\|\Psi_R(X_R)-X_R\|=\frac{h}{a_R}\to0.
}
\tag{26}
\]

The channel itself converges still faster:

\[
\boxed{
\|\Psi_R-I\|=\frac2{a_R^2}\to0.
}
\tag{27}
\]

Nevertheless the Kadison defect is the variance of a two-point law with displacements `0` and `-a_Rh`:

\[
\begin{aligned}
K_R(y_{j_R})
&=
\frac1{a_R^2}
\left(1-\frac1{a_R^2}\right)
(a_Rh)^2\\
&=
\left(1-\frac1{a_R^2}\right)h^2.
\end{aligned}
\tag{28}
\]

Every other row is deterministic. Therefore

\[
\boxed{
\|K_R\|
=
\left(1-\frac1{a_R^2}\right)(\log2)^2
\longrightarrow
(\log2)^2.
}
\tag{29}
\]

The pointwise sharp bound (1) is an equality here. Indeed,

\[
\varepsilon_RL_{-,R}L_{+,R}=0,
\]

while

\[
\beta_R(L_{+,R}-L_{-,R})-\beta_R^2
=
h^2-\frac{h^2}{a_R^2},
\tag{30}
\]

exactly reproducing (28).

Thus the new term is not a proof artifact. It is the entire defect in a canonical one-sided intrinsic example.

## 4. Even two-sided max-divergence still converges

Let

\[
\nu_R'=
u_R\Psi_R
\]

be the transformed scalar source law and let

\[
L_R=\frac{d\nu_R'}{d\nu_R}.
\]

Only the center and backward target change. At the center,

\[
L_R(y_{j_R})=1-\frac1{a_R^2}.
\tag{31}
\]

At the backward target,

\[
L_R(y_{j_R-a_R})
=
1+rac1{a_R^2}
\frac{w_{j_R,R}}{w_{j_R-a_R,R}}.
\tag{32}
\]

From (19), normalization cancels and

\[
\frac{w_{j,R}}{w_{j-a,R}}
=
2^{-as}
\frac{2^{j-a}+1}{2^j+1}
\le
2^{-as}.
\tag{33}
\]

Therefore

\[
1-\frac1{a_R^2}
\le
L_R
\le
1+rac{2^{-a_Rs}}{a_R^2}
\tag{34}
\]

throughout the support. Consequently

\[
D_\infty(\nu_R'\|\nu_R)
\le
\log\left(1+\frac{2^{-a_Rs}}{a_R^2}\right)
\to0,
\tag{35}
\]

and

\[
D_\infty(\nu_R\|\nu_R')
\le
-\log\left(1-\frac1{a_R^2}\right)
\to0.
\tag{36}
\]

So the counterexample simultaneously has uniform likelihood-ratio convergence, bounded-channel convergence, and absolute source-coordinate convergence. The surviving defect is not due to a hidden scalar tail discrepancy; it is exactly the product of a vanishing coordinate bias with a diverging one-sided propagation radius.

## 5. Matched control and falsification

Nothing in the mechanism is prime-selective. On any equally spaced ray `x_j=jh`, choose a moving index `j`, a backward distance `a_j->infinity` with `a_j<j`, and replace one row by

\[
(1-a_j^{-2})\delta_{x_j}
+a_j^{-2}\delta_{x_{j-a_j}}.
\tag{37}
\]

Then

\[
\|\Psi_j-I\|=2a_j^{-2},
\qquad
\|\Psi_j(X)-X\|=h/a_j,
\]

while

\[
\|K_j\|=(1-a_j^{-2})h^2.
\]

If the scalar weights decrease at least geometrically along the ray, the two-sided max-divergences also vanish exactly as in (35)--(36). Thus a generalized-prime or entirely non-arithmetic matched control reproduces the whole phenomenon.

Several attempted repairs are therefore falsified:

- **absolute approximate barycentricity:** `||Psi_R(X_R)-X_R||->0` is insufficient;
- **ordinary channel convergence:** `||Psi_R-I||->0` remains insufficient;
- **uniform scalar likelihood convergence:** both max-divergences can vanish;
- **the exact-martingale propagation product:** `sup L_-L_+` can vanish identically while the defect stays fixed.

The surviving repair is scale-aware: the coordinate bias itself must be controlled after multiplication by propagation asymmetry, or one must directly control an equivalent first/second-moment graph norm.

## 6. Prior-art and novelty audit

The probabilistic inequality behind (1) is classical. Bhatia--Davis bounds the variance of a bounded real random variable by the distances from its mean to the two support endpoints. Conditioning on the off-diagonal part and then applying the elementary law of total variance gives (1). No novelty is claimed for Bhatia--Davis, Kadison--Schwarz, Stinespring dilation, multiplicative-domain theory, or the fact that commutative UCP maps are Markov kernels.

A bounded literature search around refined Bhatia--Davis inequalities and approximate multiplicative-domain/Kadison-defect control found the standard variance and operator-algebra mechanisms, but no arithmetic-specific theorem corresponding to the moving Mangoldt-tail scaling considered here. The repository-level delta is narrower: `WP-336` left approximate barycentric preservation outside its theorem, and (1) identifies the exact additional bias-propagation term; the intrinsic dyadic source then realizes a sharp one-sided escape in which **all three unweighted errors**—channel norm, max-divergence, and coordinate bias—vanish while the Kadison defect stays fixed.

This is therefore `LITERATURE+DERIVED`, not a claim of a new variance theorem.

## 7. Consequence for the Weil-positivity search

The UCP route now has a more precise stability boundary. For the same moving logarithmic source coordinate, it is not enough that a candidate readout become asymptotically identity and asymptotically barycentric in ordinary norm. The relevant modulus must pay both

\[
\text{escape probability}\times\text{bidirectional propagation}
\]

and

\[
\text{coordinate bias}\times\text{propagation asymmetry}.
\]

A fixed positive defect can hide at the critical scale of either term. Exact barycentricity suppresses the second channel and recovers `WP-336`; approximate barycentricity reopens a one-sided nonlocal escape unless its bias is weighted by the distance over which it is transported.

This still does not produce the finite-prime/archimedean decomposition or the global Weil sign required by the research mandate. Instead it removes another soft route to obtaining a nontrivial positive coupling from asymptotic source fidelity alone. A viable geometric mechanism must now either control the actual first- and second-moment propagation scales, use an exact source law strong enough to force the multiplicative domain, leave the commutative Markov/UCP category, or expose a genuinely source-selective coupling that the generic tail construction cannot fake.

No zero data, RH assumption, analytic continuation, hand-picked Weil kernel, or regularization enters the argument.
