# RE-236 — Full-arc contraction eliminates the inverse-center exception

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER-DRIFT + SUPER-BROAD-CORRIDOR + WIENER-COST + SYMMETRIC-ARC-GEOMETRY + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-220, RE-235.

RE-235 proves that a super-broad complex single-center negative-binomial predictor cannot keep a bounded normalized Wiener rate on a fixed positive arc, and more generally that bounded rate forces an exponentially thin observed arc when

\[
|a|\sin\alpha\ge1.
\]

It leaves `|a| sin(alpha)<1` as a separate inverse-center boundary because its coarse phase estimate loses the radial margin needed to control the exact DC normalizer there.

That exception is not genuine. The two endpoint contraction inequalities on the **symmetric** arc already imply a uniform DC margin at every center scale. No hypothesis comparing `alpha` with `1/|a|` is needed.

Let

\[
a=\rho e^{i\varphi},
\qquad \rho\ge1,
\qquad 0<\alpha<\frac\pi2,
\]

and assume full-arc contraction

\[
\max_{|\theta|\le\alpha}
\left|1-\frac{e^{-i\theta}}a\right|<1.
\tag{1}
\]

Set

\[
q:=\left|1-\frac1a\right|.
\tag{2}
\]

Then

\[
\boxed{
1-q>
\frac{\sin\alpha}{\sqrt3\,\rho}.
}
\tag{3}
\]

Consequently, for the exact normalized truncated negative-binomial predictor

\[
Q_{m,N,a}(z)
:=z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)},
\tag{4}
\]

with `Q(1) != 0`, define

\[
\tau:=\frac{N}{m\rho}.
\tag{5}
\]

Whenever `tau>=2`, the exact normalized Wiener norm satisfies

\[
\boxed{
\|F_{m,N,a}\|_A
>
e^{-2}
\left(\frac{\sin\alpha}{\sqrt3}\right)^m
\tau^{m-1}
\left(1+\frac1\rho\right)^N.
}
\tag{6}
\]

Hence

\[
\boxed{
\frac1m\log\|F_{m,N,a}\|_A
>
\tau\log2
+\left(1-\frac1m\right)\log\tau
+\log\frac{\sin\alpha}{\sqrt3}
-\frac2m.
}
\tag{7}
\]

The super-broad conclusion of RE-235 therefore holds for **every contracting symmetric arc**, including the former inverse-center layer. In particular, if

\[
\rho_m\to\infty,
\qquad
\tau_m=\frac{N_m}{m\rho_m}\to\infty,
\qquad
\inf_m\alpha_m>0,
\]

then

\[
\boxed{
\frac1m\log\|F_m\|_A\to\infty,
\qquad
\frac{\log\|F_m\|_A}{m\alpha_m}\to\infty.
}
\tag{8}
\]

More generally, if for some finite `C`

\[
\frac{\log\|F_m\|_A}{m\alpha_m}\le C,
\tag{9}
\]

then every sufficiently large contracting super-broad member obeys

\[
\boxed{
\sin\alpha_m
<
\sqrt3\,e^{2/m+C\alpha_m}
\tau_m^{-(1-1/m)}2^{-\tau_m}.
}
\tag{10}
\]

Thus the one-center super-broad frontier no longer splits into an ordinary arc and an inverse-center layer. Under contraction, **bounded normalized Wiener rate always forces the arc to be exponentially thin in the super-broad load**. The only surviving scale-dependent possibility inside this argument is therefore the genuinely coupled exponentially thin-arc limit itself.

## 1. Endpoint contraction gives more phase information than `cos(phi)>=sin(alpha)`

The endpoint cases of (1) are

\[
\left|1-\frac{e^{-i\alpha}}a\right|<1,
\qquad
\left|1-\frac{e^{i\alpha}}a\right|<1.
\tag{11}
\]

Equivalently,

\[
\cos(\varphi+\alpha)>\frac1{2\rho},
\qquad
\cos(\varphi-\alpha)>\frac1{2\rho}.
\tag{12}
\]

Put

\[
\beta:=\arccos\frac1{2\rho}.
\tag{13}
\]

Because `rho>=1`,

\[
\frac\pi3\le\beta<\frac\pi2.
\]

After choosing the phase representative compatible with (12), both endpoint angles lie in the same interval `(-beta,beta)`. Therefore

\[
|\varphi|+\alpha<\beta.
\tag{14}
\]

Since cosine decreases on `[0,pi]`,

\[
\begin{aligned}
\cos\varphi
&>\cos(\beta-\alpha)\\
&=\frac{\cos\alpha}{2\rho}
+\sqrt{1-\frac1{4\rho^2}}\,\sin\alpha.
\end{aligned}
\tag{15}
\]

This retains the small but load-bearing offset `1/(2rho)` that is lost if one keeps only the rough cone estimate `cos(phi)>=sin(alpha)`.

## 2. The exact cone geometry yields a uniform DC radial margin

From (2),

\[
q^2
=1-\frac{2\cos\varphi}{\rho}+\frac1{\rho^2}.
\tag{16}
\]

Using (15),

\[
\begin{aligned}
1-q^2
&=\frac{2\cos\varphi}{\rho}-\frac1{\rho^2}\\
&>
\frac{\sin\alpha}{\rho}
\left(
2\sqrt{1-\frac1{4\rho^2}}
-\frac{\tan(\alpha/2)}{\rho}
\right).
\end{aligned}
\tag{17}
\]

Equation (14) implies `alpha<beta`, so

\[
\tan\frac\alpha2<\tan\frac\beta2.
\]

Using

\[
\tan\frac\beta2
=
\frac{\sin\beta}{1+\cos\beta}
=
\frac{\sqrt{1-1/(4\rho^2)}}{1+1/(2\rho)},
\]

the bracket in (17) is strictly larger than

\[
\frac{\sqrt{4\rho^2-1}}{\rho+1/2}.
\tag{18}
\]

For `rho>=1`,

\[
\frac{\sqrt{4\rho^2-1}}{\rho+1/2}
\ge\frac2{\sqrt3},
\tag{19}
\]

because after squaring (19) is equivalent to

\[
(2\rho+1)(\rho-1)\ge0.
\]

Therefore

\[
1-q^2>
\frac{2}{\sqrt3}
\frac{\sin\alpha}{\rho}.
\tag{20}
\]

Contraction at `theta=0` gives `q<1`, hence `1+q<2`. Dividing (20) by `1+q` proves the announced uniform margin

\[
1-q>
\frac{\sin\alpha}{\sqrt3\,\rho}.
\]

The point is not the constant `1/sqrt(3)`. The structural fact is that **symmetric endpoint contraction already contributes one full factor `sin(alpha)/rho` even when `rho sin(alpha)<1`**.

## 3. The RE-235 coefficient argument then loses its inverse-center hypothesis

Define

\[
S_{m,N}(s)
:=
\sum_{k=0}^{N}
\binom{m+k-1}{k}s^k.
\tag{21}
\]

RE-220 gives the exact phase-independent Wiener identity

\[
\|Q_{m,N,a}\|_A
=
\rho^{-m}
S_{m,N}\!\left(1+\frac1\rho\right).
\tag{22}
\]

At DC, triangle inequality and the full negative-binomial series give

\[
|Q_{m,N,a}(1)|
\le
\rho^{-m}S_{m,N}(q)
\le
\rho^{-m}(1-q)^{-m}.
\tag{23}
\]

Therefore

\[
\|F_{m,N,a}\|_A
\ge
(1-q)^m
S_{m,N}\!\left(1+\frac1\rho\right).
\tag{24}
\]

The terminal-block estimate of RE-235 is independent of `alpha`. For completeness, put

\[
s:=1+\frac1\rho,
\qquad
w_k:=\binom{m+k-1}{k}s^k,
\qquad
L:=\lfloor\rho\rfloor.
\]

If `tau>=2`, then `N=m rho tau>=2m rho`, and for `N-L<=k<=N`,

\[
\frac{w_{k-1}}{w_k}
=
\frac{k}{(m+k-1)s}
\ge
\left(1+\frac1\rho\right)^{-2}.
\]

Hence every one of the last `L+1>rho` terms is at least `e^{-2}w_N`, so

\[
S_{m,N}(s)
\ge
e^{-2}\rho
\binom{m+N-1}{N}s^N.
\tag{25}
\]

Also

\[
\binom{m+N-1}{N}
\ge
\left(\frac Nm\right)^{m-1}
=(\rho\tau)^{m-1}.
\tag{26}
\]

Substitute (3), (25), and (26) into (24). The radial powers cancel exactly:

\[
\begin{aligned}
\|F\|_A
&>
e^{-2}\rho
\left(\frac{\sin\alpha}{\sqrt3\,\rho}\right)^m
(\rho\tau)^{m-1}
\left(1+\frac1\rho\right)^N\\
&=
e^{-2}
\left(\frac{\sin\alpha}{\sqrt3}\right)^m
\tau^{m-1}
\left(1+\frac1\rho\right)^N.
\end{aligned}
\]

This proves (6). Finally,

\[
\rho\log\left(1+\frac1\rho\right)\ge\log2
\qquad(\rho\ge1),
\]

so `N/m=rho tau` gives (7), and solving (7) under (9) gives (10).

## 4. What changes in the single-center boundary map

RE-235 correctly identified two ways in which its particular estimate could fail to give a contradiction for scale-dependent arcs: the coarse inverse-center layer `rho sin(alpha)<1`, and arcs exponentially small in `tau`. The first was a proof artifact. Equations (14)--(20) use the full symmetric endpoint cone and recover the missing radial factor with no comparison between `rho` and `alpha`.

The second possibility remains real at the level of the present bound. If `alpha` is itself of order `2^{-tau}` or smaller, the negative term `log sin(alpha)` in (7) can balance the positive `tau log 2` term. This finding therefore does **not** claim a complete impossibility theorem for every shrinking-arc single-center sequence.

The resulting classification is sharper:

\[
\boxed{
\text{contracting super-broad one-center + bounded normalized rate}
\Longrightarrow
\sin\alpha\lesssim \tau^{-1}2^{-\tau}
}
\]

up to the explicit finite-`m` factors in (10), with no separate inverse-center branch.

This remains a representation obstruction, not a universal theorem about all separated predictors. The global interval remains

\[
1\le C_{\rm sep}\le5.996390.
\]

Multi-center/minimax predictors, rational predictors, other polynomial bases, and noncontracting representations remain untouched. The surviving exponentially thin-arc scaling also remains open inside the present single-center architecture.

## 5. Prior-art and falsification audit

The negative-binomial coefficient array, its generating function, and incomplete-beta reformulations are classical. The approximation-theory and superoscillation literature already recorded for this line provides the broad context for paying coefficient norm to reproduce forbidden frequencies. A fresh structural search for truncated negative-binomial Wiener-norm bounds and complex-center arc estimates did not reveal a directly matching theorem for the phase-margin inequality (3) or its use in the normalized super-broad bound (6).

No external theorem is load-bearing here. The new input is elementary Euclidean geometry of the two contraction endpoints, followed by the exact coefficient identity already persisted in RE-220 and the finite terminal-block estimate reconstructed above. No `SOURCES.md` update is therefore required.

The falsification boundary is precise. Symmetry of the observed arc is essential to (14); contraction only at `theta=0` does not force the same phase margin. The theorem is stated for `rho>=1`, which is automatic eventually in the large-center regimes it is meant to close. It also retains the contraction hypothesis and the single-center truncated negative-binomial representation.

A direct numerical stress test over random feasible endpoint phases and center radii was used only as a private check before publication; the stored claim does not depend on it.

## Research consequence

The inverse-center layer left by RE-235 is closed: it does not represent a distinct cheap complex-center geometry. Once the full symmetric contraction condition is used, every super-broad single-center family with bounded normalized Wiener rate is forced into the same exponentially thin destination regime, regardless of how `alpha` compares with `1/rho`.

This removes one artificial branch from the one-center frontier. Continuing the architecture now means confronting only the genuinely coupled exponentially thin-arc limit, while a route intended to improve the live `C_sep<=5.996390` bound still has stronger reason to change global approximation geometry rather than tune another center-scale relation.