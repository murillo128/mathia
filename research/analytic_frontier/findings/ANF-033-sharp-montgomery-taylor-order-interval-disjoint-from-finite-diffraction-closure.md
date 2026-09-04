# ANF-033 — the sharp Montgomery--Taylor order interval is disjoint from the finite-diffraction closure

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + CONVEX-CLOSURE-SEPARATION + DECISIVE-NEGATIVE + STRUCTURAL-BOUNDARY`. `ANF-020` reduces the remaining finite-real scalar Montgomery--Taylor ceiling to the existence of one measure in the weak-* convex diffraction closure `K` dominated by

\[
\nu_{\rm MT}
=
a_{\rm MT}\delta_0+a_{\rm MT}|\alpha|\,d\alpha,
\qquad
a_{\rm MT}=C_{\rm MT}^{-1}.
\]

`ANF-030` supplies the exact sharp test `J_MT`, with strictly positive band profile `J_MT>0` on `(-1,1)` and nonnegative spatial transform `R_MT`; `ANF-031`--`ANF-032` turn its zero-set rigidity into fixed-scale local two-point sparsification. The two loopholes left in `ANF-032` can both be closed. An elementary compact-transform Fejer-kernel majorant controls the low-frequency mass of the sparse survivor, while the same positive sharp energy controls the spectral effect of deleting the exceptional `o(n)` points.

The result is

\[
\boxed{
K\cap\{\mu:0\le\mu\le\nu_{\rm MT}\}
=
\varnothing.
}
\tag{1}
\]

By the exact duality of `ANF-020`, the sharp finite-real stability inequality is therefore false: there exists a continuous even `J>=0` supported in `[-1,1]` such that

\[
\boxed{
q_{\rm real}(J)
>
\frac{C(J)}{C_{\rm MT}},
\qquad\text{equivalently}\qquad
\frac{C(J)}{q_{\rm real}(J)}<C_{\rm MT}.
}
\tag{2}
\]

This is an existential separation result, not yet an explicit scalar kernel and not yet a new unconditional zeta-zero proportion. It proves that **finite real configurations do not impose the Montgomery--Taylor ceiling**. Any scalar route must now be tested against the genuinely complex/conjugation-invariant configurations and the full zeta-side affine inequality rather than being discarded at the real stability stage.

## 1. Any dominated element of `K` would have to equal the sharp budget exactly

Retain the notation of `ANF-020` and `ANF-030`. For a finite real configuration `X` with `n=|X|`,

\[
\mu_X(d\alpha)
=
\frac1n
\left|
\sum_{x\in X}e^{-2\pi i\alpha x}
\right|^2d\alpha,
\]

and the sharp Montgomery--Taylor energy is

\[
\int J_{\rm MT}\,d\mu_X
=
1+\Delta(X),
\qquad
\Delta(X)
=
\frac2n\sum_{x<y}R_{\rm MT}(x-y)
\ge0.
\tag{3}
\]

Because `K` is the weak-* closed convex hull of the `mu_X` and `J_MT in C_0((-1,1))`, (3) passes to the closure:

\[
\boxed{
\int J_{\rm MT}\,d\mu\ge1
\qquad(\mu\in K).
}
\tag{4}
\]

On the other hand `ANF-030` gives the exact calibration

\[
\int J_{\rm MT}\,d\nu_{\rm MT}=1.
\tag{5}
\]

Suppose `mu in K` and `0<=mu<=nu_MT`. Equations (4)--(5) force equality, so for the positive measure `tau=nu_MT-mu`,

\[
\int J_{\rm MT}\,d\tau=0.
\tag{6}
\]

The band profile is strictly positive at every point of `(-1,1)`. Therefore a nonzero positive Radon measure on that open interval cannot have zero `J_MT` integral: every point of its support lies in a compact neighborhood on which `J_MT` has a positive minimum. Hence `tau=0` and

\[
\boxed{\mu=\nu_{\rm MT}.}
\tag{7}
\]

Thus the whole order-interval problem reduces to the single membership question `nu_MT in K`.

## 2. Fixed-scale sharp energy removes almost all three-point clusters

Fix `L>0`. `ANF-032` defines

\[
\kappa_L
=
\min_{\substack{a,b\ge0\\a+b\le L}}
\left[
R_{\rm MT}(a)+R_{\rm MT}(b)+R_{\rm MT}(a+b)
\right]
>0.
\tag{8}
\]

For every finite configuration `X`, one may delete a subset `E` and retain `Y=X\setminus E` so that every interval of length strictly less than `L/2` contains at most two points of `Y`, while

\[
\varepsilon(X)
:=
\frac{|E|}{|X|}
\le
\frac{2\Delta(X)}{\kappa_L}.
\tag{9}
\]

For a finite convex combination

\[
\lambda=\sum_r w_r\mu_{X_r},
\qquad
\sum_r w_r=1,
\]

write

\[
\overline\Delta
=
\sum_r w_r\Delta(X_r)
=
\int J_{\rm MT}\,d\lambda-1,
\qquad
\overline\varepsilon
=
\sum_r w_r\varepsilon(X_r).
\]

Then

\[
\boxed{
\overline\varepsilon
\le
\frac{2\overline\Delta}{\kappa_L}.
}
\tag{10}
\]

No quantitative lower bound on `kappa_L` as `L->infinity` will be needed. The limit order below is: fix `L`, approximate the sharp face arbitrarily well so that `overlineDelta->0`, and only afterwards let `L` grow.

## 3. Sharp energy also controls the spectral cost of deleting the exceptional points

The second loophole in `ANF-032` was that deleting `o(n)` points need not be small for diffraction because a small coherent subset can interfere with the survivor. At the sharp face, however, the positive `J_MT` energy controls exactly that interference.

Fix an even function

\[
\phi\in C_c((-\eta,\eta)),
\qquad
0\le\phi\le1,
\qquad
\phi(0)=1,
\tag{11}
\]

with `0<eta<1`. Since `J_MT>0` on the compact support of `phi`, there is a finite constant `C_phi` such that

\[
\phi\le C_\phi J_{\rm MT}.
\tag{12}
\]

For one decomposition `X=Y sqcup E`, with `n=|X|`, use the original normalization and define

\[
\widetilde\mu_Y(d\alpha)
=
\frac1n
\left|\sum_{y\in Y}e^{-2\pi i\alpha y}\right|^2d\alpha,
\qquad
\widetilde\mu_E(d\alpha)
=
\frac1n
\left|\sum_{e\in E}e^{-2\pi i\alpha e}\right|^2d\alpha.
\tag{13}
\]

Put

\[
A_Y=\int J_{\rm MT}\,d\widetilde\mu_Y,
\qquad
B_E=\int J_{\rm MT}\,d\widetilde\mu_E.
\]

Because `R_MT>=0`, the pair sums internal to `Y` and `E` are sub-sums of the total positive pair energy in (3). Therefore

\[
A_Y\le1+\Delta(X),
\qquad
B_E\le\varepsilon(X)+\Delta(X).
\tag{14}
\]

Writing the exponential sum of `X` as `S_X=S_Y+S_E`, equations (12)--(14) and Cauchy--Schwarz give

\[
\begin{aligned}
\left|
\int\phi\,d\mu_X
-
\int\phi\,d\widetilde\mu_Y
\right|
&\le
C_\phi
\left(
2\sqrt{A_YB_E}+B_E
\right)\\
&\le
C_\phi
\left[
2\sqrt{(1+\Delta(X))(\varepsilon(X)+\Delta(X))}
+\varepsilon(X)+\Delta(X)
\right].
\end{aligned}
\tag{15}
\]

Average (15) over a convex combination and apply Cauchy--Schwarz once more. With

\[
\widetilde\lambda
=
\sum_r w_r\widetilde\mu_{Y_r},
\]

one obtains

\[
\boxed{
\left|
\int\phi\,d\lambda
-
\int\phi\,d\widetilde\lambda
\right|
\le
C_\phi
\left[
2\sqrt{(1+\overline\Delta)(\overline\varepsilon+\overline\Delta)}
+\overline\varepsilon+\overline\Delta
\right].
}
\tag{16}
\]

For fixed `L`, (10) shows that the right side tends to zero with `overlineDelta`. Thus a vanishing exceptional particle fraction is spectrally harmless for every fixed compact interior test once the same configurations are approaching the sharp `J_MT` face.

## 4. Local two-point sparsity forces vanishing central mass by an elementary band majorant

Let

\[
Y=\{y_1<y_2<\cdots<y_m\}
\]

satisfy the conclusion of `ANF-032`: every interval of length `<L/2` contains at most two points. Then

\[
y_{j+2}-y_j\ge L/2.
\tag{17}
\]

Consequently the odd-indexed and even-indexed subsequences are each `delta`-separated with

\[
\delta\ge L/2.
\tag{18}
\]

A self-contained Fourier majorant gives the only large-sieve input needed here. For `H>0` put

\[
K_H(\alpha)
=
H\left(
\frac{\sin(\pi H\alpha)}{\pi H\alpha}
\right)^2.
\tag{19}
\]

Then `K_H>=0`, `int K_H=1`, and in the present Fourier convention

\[
\widehat K_H(x)
=
\left(1-\frac{|x|}{H}\right)_+,
\]

so its transform is supported in `[-H,H]`. Define the absolute constant

\[
c_0
:=
\int_{-1}^{1}
\left(
\frac{\sin(\pi u)}{\pi u}
\right)^2du
>0.
\tag{20}
\]

For `0<H<delta`, set `r=1/H` and

\[
W_{\eta,H}
:=
c_0^{-1}
\left(
\mathbf 1_{[-\eta-r,\eta+r]}*K_H
\right).
\]

If `|alpha|<=eta`, the convolution interval contains the whole kernel window `[-r,r]`, hence `W_{\eta,H}(alpha)>=1`. Moreover

\[
\int W_{\eta,H}
=
\frac{2(\eta+r)}{c_0},
\]

while `widehat W_{\eta,H}` is supported in `[-H,H]`. Therefore, for every finite `delta`-separated set `Z`, all off-diagonal Fourier terms vanish and

\[
\begin{aligned}
\int_{-\eta}^{\eta}
\left|
\sum_{z\in Z}e^{-2\pi i\alpha z}
\right|^2d\alpha
&\le
\int W_{\eta,H}(\alpha)
\left|
\sum_{z\in Z}e^{-2\pi i\alpha z}
\right|^2d\alpha\\
&=
|Z|\int W_{\eta,H}.
\end{aligned}
\]

Taking `H=delta/2` gives the explicit estimate

\[
\boxed{
\int_{-\eta}^{\eta}
\left|
\sum_{z\in Z}e^{-2\pi i\alpha z}
\right|^2d\alpha
\le
\frac{2}{c_0}
\left(
\eta+\frac{2}{\delta}
\right)|Z|.
}
\tag{21}
\]

Apply (21) to the two parity subsequences and use

\[
|S_{\rm odd}+S_{\rm even}|^2
\le
2|S_{\rm odd}|^2+2|S_{\rm even}|^2.
\]

Together with (18),

\[
\int_{-\eta}^{\eta}|S_Y(\alpha)|^2d\alpha
\le
\frac{4}{c_0}
\left(
\eta+\frac4L
\right)|Y|.
\tag{22}
\]

After dividing by the original cardinality `n>=|Y|`,

\[
\boxed{
\widetilde\mu_Y((-\eta,\eta))
\le
\frac{4}{c_0}
\left(
\eta+\frac4L
\right).
}
\tag{23}
\]

In particular, because `0<=phi<=1` and `supp(phi) subset (-eta,eta)`, the same upper bound holds for `int phi d tilde_mu_Y`.

The argument is deterministic and finite. It uses no stationarity, Palm representation, density limit, separated-frequency theorem, or assumption about how the surviving points are distributed beyond the local two-point packing law.

## 5. The sharp budget cannot lie in `K`

Assume for contradiction that `nu_MT in K`, which by Section 1 is the only possible dominated witness.

Fix `L>0` and the bump `phi` from (11). By the definition of `K`, for every tolerance there is a finite convex combination `lambda` of finite-configuration diffraction measures simultaneously approximating `nu_MT` on the two tests `J_MT` and `phi`. Since every component has sharp energy at least one and `nu_MT` has sharp energy exactly one, these approximants can be chosen so that

\[
\overline\Delta
=
\int J_{\rm MT}\,d\lambda-1
\longrightarrow0
\tag{24}
\]

while

\[
\int\phi\,d\lambda
\longrightarrow
\int\phi\,d\nu_{\rm MT}.
\tag{25}
\]

For each component apply the `ANF-032` deletion at this fixed `L`. Equations (10) and (16) imply

\[
\int\phi\,d\lambda
-
\int\phi\,d\widetilde\lambda
\longrightarrow0.
\tag{26}
\]

Equation (23), averaged over the components, gives uniformly

\[
\int\phi\,d\widetilde\lambda
\le
\frac4{c_0}
\left(
\eta+\frac4L
\right).
\tag{27}
\]

Passing through (25)--(27),

\[
\int\phi\,d\nu_{\rm MT}
\le
\frac4{c_0}
\left(
\eta+\frac4L
\right).
\tag{28}
\]

Now `L` was arbitrary. Letting `L->infinity` yields

\[
\boxed{
\int\phi\,d\nu_{\rm MT}
\le
\frac{4\eta}{c_0}.
}
\tag{29}
\]

But the atom at the origin gives, because `phi(0)=1`,

\[
\int\phi\,d\nu_{\rm MT}
\ge
a_{\rm MT}.
\tag{30}
\]

Choose any `eta<c_0 a_MT/4`. Equations (29)--(30) contradict each other. Therefore

\[
\boxed{\nu_{\rm MT}\notin K.}
\tag{31}
\]

Together with (7), this proves the disjointness (1).

The order of limits is load-bearing. For each fixed `L`, `kappa_L` is merely positive, so weak-* approximation can force `overlineDelta` small enough to eliminate the exceptional fraction. Only after that approximation limit is taken is `L` sent to infinity. The deterioration of `kappa_L` at large scale therefore cannot rescue the witness.

## 6. Consequence: the sharp finite-real stability ceiling is false

`ANF-020` proves the exact alternative

\[
\left[
q_{\rm real}(J)
\le
\frac{C(J)}{C_{\rm MT}}
\ \text{for every continuous even }J\ge0
\right]
\quad\Longleftrightarrow\quad
K\cap\{0\le\mu\le\nu_{\rm MT}\}\ne\varnothing.
\tag{32}
\]

Negating (32) with (1) gives (2). Using `ANF-018`,

\[
q_{\rm real}(J)
=
\widehat J(0)-2B_{\rm stab}(\widehat J),
\]

so the same separating spectrum satisfies

\[
\boxed{
B_{\rm stab}(\widehat J)
<
\frac12
\left(
\widehat J(0)-\frac{C(J)}{C_{\rm MT}}
\right).
}
\tag{33}
\]

Thus the sharp stability inequality posed in `CLUE-semidefinite-pair-correlation-horizontal-lift.md` is refuted existentially. The separator supplied by convex separation is not explicit, so this finding does not yet provide a kernel ready for the next conjugation-invariant complex test.

This distinction matters for the zeta application. `ANF-017` already separates the finite-real test from the full universal affine inequality over conjugation-invariant complex multisets. Equation (2) says there exists a scalar positive-band shape that survives **all finite real configurations at once**. It does not say that the same shape survives vertically displaced conjugate pairs, nor that the BGSST/Lamzouri counting bridge produces a stronger unconditional simple-critical-zero proportion. Those are now the correct next scalar gates.

## 7. Prior art, novelty boundary, and decisive audit

No new external theorem is load-bearing. The central-mass estimate in Section 4 is proved directly from the elementary Fejer kernel identity `widehat K_H=(1-|x|/H)_+`; it is included in full precisely so that no large-sieve citation is needed. The sharp band test remains the Carneiro--Chandee--Littmann--Milinovich / Montgomery--Taylor extremizer already anchored for `ANF-030`, while `ANF-031`--`ANF-032` provide the Mathia-derived additive zero-set and local packing inputs. `SOURCES.md` therefore does not change.

A targeted search of the existing diffraction/hyperuniform realizability literature already recorded for `ANF-020`, together with standard separated-frequency/large-sieve literature, did not locate this particular combination proving disjointness of the Montgomery--Taylor order interval from the finite-diffraction convex closure. The proof here is self-contained relative to the canonical findings just cited, and no publication-level novelty claim is made.

The proof has four short failure tests:

1. If `J_MT` were allowed to vanish inside the open band, equality in its energy would not force a dominated witness to equal `nu_MT`; strict interior positivity from `ANF-030` is essential.
2. If `R_MT` changed sign, the deleted-set bounds (14) would fail; its nonnegativity is essential.
3. If the `ANF-032` survivor were not a union of finitely many separated subsequences with separation growing like `L`, the compact-transform majorant would not force the central mass to `O(eta)+o_L(1)`.
4. The conclusion is only the finite-real scalar separation encoded by `K`. Any claim of an improved unconditional zeta proportion before the complex/conjugation-invariant gate would overstate what has been proved.

These checks leave (1), (2), and (33) as exact consequences of the current canonical inputs plus the elementary Fourier calculation in Section 4.
