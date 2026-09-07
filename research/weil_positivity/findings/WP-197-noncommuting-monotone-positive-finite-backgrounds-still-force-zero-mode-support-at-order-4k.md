# WP-197 — Noncommuting monotone positive finite backgrounds still force zero-mode support at order `4k`

**Status:** `LITERATURE+DERIVED + EXACT + HIGHER-ORDER-SPECTRAL-SHIFT + NONCOMMUTING-FINITE-DIMENSIONAL + MONOTONE-POSITIVE-PAIR + SPECTRAL-SHIFT-JUMP-ASYMPTOTIC + FULL-WEIL-AUTOCORRELATION-CONE + ZERO-MODE-CLASSIFICATION + DECISIVE-NEGATIVE + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-196` proves that for commuting finite-dimensional positive operators `H>=0` and `V>=0`, full order-`4k` positivity on the real Weil autocorrelation cone forces `HV=0`. It explicitly leaves noncommutativity as a possible escape, because simultaneous diagonalization was used to read the high-frequency Fourier tail from scalar source intervals.

That escape is not real in finite dimension. The exact finite-matrix jump formula for higher-order spectral-shift functions identifies the same source-boundary invariant without assuming `[H,V]=0`: at an eigenvalue `lambda` of `H`, the order-`n` spectral-shift density has a jump equal to a positive odd power of the compressed perturbation `P_lambda V P_lambda` when `n=4k` and `V>=0`. Those positive source jumps generate the same one-sided sine tail that obstructed the commuting case.

Consequently, for every finite-dimensional self-adjoint pair

\[
H\ge0,\qquad V\ge0,
\tag{1}
\]

with no commutativity assumption, and every `n=4k`,

\[
\boxed{
\mathcal R_{4k}(g*\widetilde g;H,V)\ge0
\text{ for every real }g\in C_c^\infty(\mathbb R)
\iff
HV=0.
}
\tag{2}
\]

If `V!=0`, the left side of (2) is in fact strictly positive for every nonzero `g` once `HV=0` holds. Thus **finite-dimensional noncommuting positive-energy coupling does not enlarge the `4k` survivor at all**: full Weil-cone positivity forces the perturbation back onto the zero eigenspace of the background, where the pair becomes commuting automatically and reduces to the universal source-centered carrier of `WP-194`.

## 1. The exact finite-matrix spectral-shift jump is the noncommuting source invariant

For self-adjoint matrices `H,V` and integer `n>=2`, let

\[
\mathcal R_n(f;H,V)
=
\operatorname{Tr}\!\left(
 f(H+V)-\sum_{j=0}^{n-1}\frac1{j!}
 \frac{d^j}{dt^j}f(H+tV)\bigg|_{t=0}
\right).
\tag{3}
\]

Finite-dimensional higher-order spectral-shift theory gives a unique compactly supported `eta_n in L^1(R)` satisfying

\[
\mathcal R_n(f;H,V)
=
\int_{\mathbb R} f^{(n)}(x)\eta_n(x)\,dx.
\tag{4}
\]

The decisive additional input is the exact jump formula of Skripka--Zinchenko for matrix Taylor remainders. If `P_lambda=E_H({lambda})` is the spectral projection of `H` at an eigenvalue `lambda`, then

\[
\boxed{
\eta_n(\lambda^+)-\eta_n(\lambda^-)
=
\frac1{(n-1)!}
\operatorname{Tr}\!\left((P_\lambda V P_\lambda)^{n-1}\right).
}
\tag{5}
\]

Indeed, their finite Borel measure

\[
\omega_r(A_1\times\cdots\times A_r)
=
\operatorname{Tr}\!\left(
 E_H(A_1)V\cdots E_H(A_r)V
\right)
\tag{6}
\]

has atom at `(lambda,...,lambda)` equal, by cyclicity of trace and `P_lambda^2=P_lambda`, to

\[
\omega_r(\{\lambda\}^r)
=
\operatorname{Tr}\!\left((P_\lambda V P_\lambda)^r\right),
\qquad r=n-1.
\tag{7}
\]

No simultaneous eigenbasis for `H` and `V` is involved. Equation (5) is exactly the noncommuting replacement for the scalar source-endpoint value used in `WP-196`.

Now specialize to

\[
n=4k,\qquad r=4k-1.
\tag{8}
\]

Then `r` is odd. If `V>=0`, every compression

\[
A_\lambda=P_\lambda V P_\lambda
\tag{9}
\]

is positive semidefinite, so the source jump

\[
J_\lambda
:=
\eta_n(\lambda^+)-\eta_n(\lambda^-)
=
\frac1{r!}\operatorname{Tr}(A_\lambda^r)
\tag{10}
\]

satisfies

\[
\boxed{
J_\lambda\ge0,
\qquad
J_\lambda=0\iff A_\lambda=0.
}
\tag{11}
\]

This is the crucial monotonicity. Noncommutativity changes the interior multiple-operator-integral structure of `eta_n`, but it cannot orient an individual source jump negatively when `V>=0`.

## 2. The jumps force the same one-sided high-frequency sine tail

For matrices, the same finite-dimensional representation underlying (5) makes `eta_n` compactly supported and piecewise absolutely continuous away from the finite set `sigma(H)`. Its distributional derivative can therefore be written

\[
D\eta_n
=q+
\sum_{\lambda\in\sigma(H)}J_\lambda\,\delta_\lambda,
\qquad q\in L^1(\mathbb R).
\tag{12}
\]

Use the Fourier convention

\[
\widehat f(\xi)
=
\int_{\mathbb R}f(x)e^{-i\xi x}\,dx.
\tag{13}
\]

Fourier transformation of (12) gives

\[
i\xi\,\widehat{\eta_n}(\xi)
=
\widehat q(\xi)
+
\sum_{\lambda\in\sigma(H)}J_\lambda e^{-i\lambda\xi}.
\tag{14}
\]

By the Riemann--Lebesgue lemma, `widehat q(xi)=o(1)`. Hence

\[
\widehat{\eta_n}(\xi)
=
\frac1{i\xi}
\sum_{\lambda\in\sigma(H)}J_\lambda e^{-i\lambda\xi}
+o(\xi^{-1}).
\tag{15}
\]

Since `eta_n` is real, the Fourier transform of its even part is the real part of (15):

\[
\boxed{
\widehat{\eta_n^{\rm ev}}(\xi)
=
-\frac1\xi
\sum_{\lambda\in\sigma(H)}J_\lambda\sin(\lambda\xi)
+o(\xi^{-1}).
}
\tag{16}
\]

Equation (16) is the exact noncommuting analogue of the `1/xi` source-boundary asymptotic in `WP-196`. The difference is that the scalar coefficient `v_j^{4k-1}/(4k-1)!` has become the basis-free compression invariant

\[
\frac1{(4k-1)!}
\operatorname{Tr}\!\left((P_\lambda V P_\lambda)^{4k-1}\right).
\tag{17}
\]

## 3. The Weil autocorrelation cone forces every positive-energy source jump off zero to vanish

`WP-193` proves that at order `n=4k`, nonnegativity of the Taylor remainder on **every** real compactly supported smooth autocorrelation is equivalent to

\[
\widehat{\eta_n^{\rm ev}}(\xi)\ge0
\qquad\text{for every }\xi\in\mathbb R.
\tag{18}
\]

Assume now `H>=0` and `V>=0`. The spectrum of `H` lies in `[0,\infty)`. Define the finite sine polynomial

\[
S(\xi)
=
\sum_{\substack{\lambda\in\sigma(H)\\ \lambda>0}}
J_\lambda\sin(\lambda\xi).
\tag{19}
\]

If any `J_lambda>0` at a positive eigenvalue, then `S` is a nonzero finite trigonometric polynomial. Such a polynomial is almost periodic: any value attained with positive margin recurs along arbitrarily large positive arguments. Since `S` is odd and nonzero, there exist `epsilon>0` and a sequence `xi_m->infinity` such that

\[
S(\xi_m)\ge\varepsilon.
\tag{20}
\]

The zero-eigenvalue jump makes no contribution to (19) because `sin(0)=0`. Substituting (20) into (16) gives

\[
\widehat{\eta_n^{\rm ev}}(\xi_m)
=
-\frac{S(\xi_m)}{\xi_m}+o(\xi_m^{-1})<0
\tag{21}
\]

for all sufficiently large `m`, contradicting (18). Therefore

\[
\boxed{
J_\lambda=0
\quad\text{for every }\lambda>0.
}
\tag{22}
\]

By (11),

\[
P_\lambda V P_\lambda=0
\qquad(\lambda>0).
\tag{23}
\]

This already kills noncommuting coupling. If `x in ran P_lambda` and `lambda>0`, then

\[
\langle x,Vx\rangle=0.
\tag{24}
\]

Because `V>=0`, equation (24) implies `V^{1/2}x=0`, hence `Vx=0`. Thus `V` annihilates every positive spectral subspace of `H`, including all possible off-diagonal couplings from those subspaces to `ker H`. Writing `P_0` for the projection onto `ker H`,

\[
V=P_0VP_0.
\tag{25}
\]

Consequently

\[
\boxed{HV=VH=0.}
\tag{26}
\]

The necessity direction of (2) is therefore independent of commutativity: commutativity emerges as a consequence of the full cone order.

## 4. Converse: zero-mode support reduces exactly to the universal centered carrier

If `HV=0`, self-adjointness also gives `VH=0`. Relative to

\[
\mathcal H=\ker H\oplus(\ker H)^\perp,
\tag{27}
\]

the pair decomposes as

\[
H=0\oplus H_+,
\qquad
V=V_0\oplus0.
\tag{28}
\]

The second block has zero perturbation and contributes no Taylor remainder. The first block is exactly the source-centered pair of `WP-194`. Hence for every `k>=1`,

\[
\mathcal R_{4k}(g*\widetilde g;H,V)
=
\mathcal R_{4k}(g*\widetilde g;0,V_0)
\ge0,
\tag{29}
\]

with strict inequality for every nonzero real `g in C_c^infty(R)` whenever `V!=0`.

This proves the converse and completes the exact classification (2).

A useful corollary is immediate:

\[
\boxed{
H>0,\ V\ge0,\ V\ne0
\quad\Longrightarrow\quad
\text{the bare order-`4k` remainder fails the full Weil cone.}
}
\tag{30}
\]

A strictly positive finite background has no zero mode on which a nontrivial positive perturbation can survive.

## 5. Exact noncommuting two-dimensional control

The obstruction is visible in the smallest noncommuting positive pair. Let `a>0`, `b!=0`,

\[
H=
\begin{pmatrix}
0&0\\
0&a
\end{pmatrix},
\qquad
V=
\begin{pmatrix}
1&b\\
b&b^2
\end{pmatrix}
=
\begin{pmatrix}1\\ b\end{pmatrix}
\begin{pmatrix}1&b\end{pmatrix}.
\tag{31}
\]

Then `H>=0`, `V>=0`, and `[H,V]!=0`. At the positive source eigenvalue `a`,

\[
P_aVP_a=b^2 P_a,
\tag{32}
\]

so for `r=4k-1`,

\[
J_a
=
\frac{b^{2r}}{r!}>0.
\tag{33}
\]

Therefore

\[
\widehat{\eta_{4k}^{\rm ev}}(\xi)
=
-\frac{b^{2(4k-1)}}{(4k-1)!\,\xi}
\sin(a\xi)
+o(\xi^{-1}),
\tag{34}
\]

and the multiplier is negative along an infinite sequence with `sin(a xi)` bounded away from zero on the positive side.

This control is useful because the noncommuting coupling can be arbitrarily small. As `b->0`, the bad `1/xi` coefficient becomes tiny and the first visible sign failure can move far into the Fourier tail, but the universal full-cone statement still fails for every `b!=0`. Finite numerical windows could therefore give a false impression that weak noncommutativity repairs the sign.

## 6. Aggressive falsification and exact scope

**Monotone positivity of `V` is load-bearing.** For a general signed self-adjoint perturbation, the odd compression traces in (10) can have either sign and source jumps can cancel. The theorem does not classify signed/intersection-type perturbations.

**The half-line condition on `H` is load-bearing.** `WP-195` gives explicit sign-indefinite source spectra whose positive and negative locations combine into a nonnegative Fourier multiplier. The proof above uses that every nonzero source frequency has the same orientation `lambda>0` while every jump weight is nonnegative.

**Finite dimensionality is load-bearing.** The proof uses finitely many source jumps and recurrence of a finite trigonometric polynomial. Infinite discrete spectra require summability strong enough to control the jump series uniformly, while continuous background spectrum can replace the atomic source boundary by a genuinely different object. No infinite-dimensional or continuous-spectrum classification is claimed.

**The bare Taylor remainder is load-bearing.** A source-forced counterterm, nonlocal transform, finite--archimedean coupling, or different completed functional can alter the Fourier tail. Such a construction must prove positivity for the assembled object; it cannot inherit the sign merely by citing higher-order spectral-shift positivity.

**The order `4k` is essential to the surviving category.** Orders `4k+2` were already excluded universally by the broad-dilation parity obstruction in `WP-193`. The present result says that the first parity class not killed there also collapses to zero-mode support under finite monotone positive geometry, even without commutativity.

**This still does not generate arithmetic.** When the classification succeeds, the survivor is `H=0` on the support of `V`, and `WP-194` shows that arbitrary nonarithmetic spectra of `V` work equally well. There is still no Mangoldt selector, Gamma factor, polar/global term, or source-specific finite--archimedean incidence.

## 7. Prior art and novelty boundary

The higher-order spectral-shift framework is classical/current operator theory. The exact finite-dimensional facts used above are particularly well documented in:

- Anna Skripka and Maxim Zinchenko, *Stability and uniqueness properties of Taylor approximations of matrix functions*, Linear Algebra and its Applications **582** (2019), 218--236, DOI `10.1016/j.laa.2019.07.037`. Their Theorem 2.1 records the unique compactly supported matrix spectral-shift function, Theorem 2.6 gives the finite spectral-measure representation, and Proposition 2.9 gives exactly the jump formula used in (5).

The matrix spectral-shift function, its jump formula, multiple-operator-integral measure, and finite-dimensional regularity are therefore **prior art**. No novelty is claimed for them. Likewise, Fourier asymptotics of a compactly supported piecewise absolutely continuous function from its jumps, linear independence/almost-periodicity of finite trigonometric polynomials, and the positivity implication `PVP=0 => VP=0` for `V>=0` are standard ingredients.

A targeted search around higher-order spectral shift, matrix Taylor remainders, positive perturbations, Fourier-positive/positive-definite spectral-shift densities, and noncommuting positive matrices found the established trace/jump machinery and recent even-order density-positivity results, but did not expose an independent theorem with the branch-specific conclusion (2). Absence of a wording match is not treated as standalone novelty. The durable Mathia result is the **combination** of the classical jump theorem with the exact `WP-193` Weil-autocorrelation Fourier gate, yielding a noncommutative extension of the `WP-196` zero-mode classification.

## 8. Consequence for `weil_positivity`

`WP-196` left four obvious ways to escape its commuting positive-energy classification: noncommutativity, infinite-dimensionality, sign-indefinite/intersection-type geometry, or replacing the bare `4k` Taylor remainder by a different assembled functional. The first of those is now closed in finite dimension:

\[
\boxed{
H\ge0,\ V\ge0,\ \dim\mathcal H<\infty
\quad+\quad
\text{full order-`4k` Weil-cone positivity}
\quad\Longrightarrow\quad
\operatorname{ran}V\subseteq\ker H,
}
\tag{35}
\]

**without any assumption on `[H,V]`.**

This matters for the geometric search because merely introducing matrix-valued finite--archimedean mixing before the higher-order trace does not rescue a monotone positive-energy interpretation. If both the background and the added structure remain positive operators on a finite internal space, the source jumps remember every positive background eigenspace touched by the perturbation and the Weil cone detects that contact in the Fourier tail.

A surviving higher-order route must therefore use a genuinely different category: an infinite/continuous source geometry with new convergence control, a sign-indefinite form with an independent index/Hodge-type theorem, or a completed nonlocal functional whose finite and archimedean pieces are coupled before the sign is taken. Any such route still has to derive the actual finite-prime, Gamma, and polar/global terms from the same source-native object and survive the universal nonarithmetic controls of `WP-194` and `WP-195`.

## Dependencies

- `research/weil_positivity/findings/WP-193-higher-order-spectral-shift-positivity-has-a-mod-four-weil-autocorrelation-gate.md`
- `research/weil_positivity/findings/WP-194-source-centered-4k-taylor-remainders-are-weil-cone-positive-and-scalar-centering-is-rigid.md`
- `research/weil_positivity/findings/WP-195-positive-definite-background-spectra-preserve-4k-weil-cone-positivity-off-center.md`
- `research/weil_positivity/findings/WP-196-monotone-positive-commuting-backgrounds-force-zero-mode-support-for-4k-weil-cone-positivity.md`

## Bottom line

For finite-dimensional positive operators `H>=0` and `V>=0`, noncommutativity does not enlarge the order-`4k` Weil-positive Taylor-remainder class. Classical higher-order spectral-shift theory gives a positive source jump at every positive eigenvalue of `H` touched by `V`; those jumps force an oscillatory `1/xi` Fourier tail, while `WP-193` requires the even spectral-shift Fourier multiplier to be nonnegative everywhere. Hence full Weil-autocorrelation positivity holds **exactly when `HV=0`**.

The only monotone positive finite survivor is therefore the zero-mode carrier already shown in `WP-194` to be universal and nonarithmetic. A source-specific Weil bridge must leave finite monotone positive Taylor-remainder geometry more radically than by adding noncommuting matrix coupling.