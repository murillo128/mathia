# WI-148 — full scalar universality forces Fourier positivity for every fixed superexponentially integrable profile

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-145 showed that a universal Lamzouri-form scalar inequality cannot carry a genuine eventually negative outer Fourier tail. WI-146 showed that the complete one- and two-point tests do not force Fourier positivity: a negative intermediate band can be protected by a smaller positive repair farther out. WI-147 then proved that the **full** universal finite inequality detects every negative band when the Fourier profile is continuous and compactly supported.

The compact-support hypothesis in WI-147 is not essential for a fixed regular scalar profile. Let `phi : R -> R` be continuous, real-even, normalized by

\[
\int_{\mathbb R}\phi(t)\,dt=1,
\tag{1}
\]

and assume it has absolute exponential moments of every order,

\[
\boxed{
\int_{\mathbb R}|\phi(t)|e^{c|t|}\,dt<\infty
\qquad\text{for every }c>0.
}
\tag{2}
\]

Define the entire Fourier--Laplace transform

\[
H(z):=\int_{\mathbb R}\phi(t)e^{-2\pi i zt}\,dt.
\tag{3}
\]

Suppose that for **every** nonempty finite multiset `Z` invariant under complex conjugation, with `s(Z)` the number of simple real elements,

\[
\boxed{
s(\mathcal Z)
\ge 2|\mathcal Z|-
\sum_{z,w\in\mathcal Z}H(z-w).
}
\tag{4}
\]

Then necessarily

\[
\boxed{
\phi(t)\ge0\qquad(t\in\mathbb R).
}
\tag{5}
\]

Thus the compact-spectrum no-go of WI-147 extends to every fixed continuous signed density whose direct Fourier representation is defined absolutely on arbitrary complex gaps. In particular, moving compensating positive mass arbitrarily far out does **not** rescue a fixed Gaussian/superexponentially decaying signed profile from the full Lamzouri multiset inequality. The remote-repair mechanism of WI-146 survives all two-point tests but is killed by sufficiently large conjugate-pair families even when the repair is noncompact.

No zeta-zero proportion changes. The result is a route closure for the single-scalar universal interface. It does not cover `T`-dependent profiles without a uniform argument, signed spectral distributions whose complex continuation is not represented by the absolutely convergent integral (3), source-specific inequalities valid only for actual zeta-zero configurations, or genuinely joint/matrix observables.

## 1. Primary-source interface

The finite inequality being abstracted is Proposition 2.1 of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026). Lamzouri takes a real-even compactly supported `eta in L^2(R)` with `widehat(eta^2)(0)=1`, puts

\[
K(\xi)=\widehat{\eta^2}(\xi),
\]

and proves

\[
s(\mathcal Z)
\ge 2|\mathcal Z|-
\sum_{z,w\in\mathcal Z}K(z-w)^2
\tag{6}
\]

for every finite conjugation-invariant multiset. Writing `H=K^2` gives the scalar interface (4). Lamzouri's actual profile is positive: the Fourier density of `K^2` is the autocorrelation/convolution of `eta^2` with itself. WI-143--WI-147 ask how much sign freedom could remain if some different proof produced the same universal scalar census.

Condition (2) is the natural direct-integral replacement for compact support when (4) is required on arbitrary complex multisets. It guarantees absolute convergence of (3) for every `z in C`, allows differentiation under the integral on compact subsets, and, more importantly below, justifies the exact pair-sum identity for arbitrarily deep conjugate pairs. Polynomial-Gaussian and more generally superexponentially decaying profiles lie in this class.

## 2. The universal pair sum is an exact signed spectral integral

For a finite conjugation-invariant multiset `Z`, define

\[
S_{\mathcal Z}(t):=
\sum_{z\in\mathcal Z}e^{-2\pi i tz}.
\tag{7}
\]

Conjugation invariance gives

\[
\sum_{w\in\mathcal Z}e^{2\pi i tw}
=\overline{S_{\mathcal Z}(t)}.
\tag{8}
\]

Since `Z` is finite and (2) dominates the largest imaginary depth occurring in `Z`, Fubini gives

\[
\boxed{
Q_H(\mathcal Z)
:=\sum_{z,w\in\mathcal Z}H(z-w)
=\int_{\mathbb R}\phi(t)|S_{\mathcal Z}(t)|^2\,dt.
}
\tag{9}
\]

If `Z` has no real elements then `s(Z)=0`, so (4) requires

\[
\boxed{
Q_H(\mathcal Z)\ge2|\mathcal Z|>0.
}
\tag{10}
\]

It therefore suffices to show that any negative value of `phi` produces one finite conjugation-invariant non-real multiset for which (9) is negative.

## 3. The same binomial/common-depth probe works with a movable truncation radius

Assume for contradiction that `phi(a)<0` for some `a>0`. If the only initially identified negative point were `0`, continuity would provide a nearby nonzero negative point. Choose `eta>0` and `delta>0`, with `delta<a/2`, such that

\[
\phi(t)\le-\eta
\qquad
(t\in I:=[a-\delta,a+\delta]).
\tag{11}
\]

Let `lambda>=1` be a parameter that will tend to infinity. After `lambda` is fixed, choose a radius

\[
R\ge\max\{2(a+\delta),1\}
\tag{12}
\]

and put

\[
m:=\lceil\lambda R^2\rceil,
\qquad
\lambda_R:=\frac{m}{R^2}.
\tag{13}
\]

Then

\[
\lambda\le\lambda_R\le\lambda+1\le2\lambda.
\tag{14}
\]

Set

\[
\theta:=\frac{\pi a}{2R}\in(0,\pi/4],
\qquad
b:=\frac{m}{4R}\tan\theta,
\tag{15}
\]

and centers

\[
x_k:=\frac{k}{2R},
\qquad 0\le k\le m,
\tag{16}
\]

where `x_k` occurs with multiplicity `binom(m,k)`. Let `Z_{m,R}` consist of the conjugate pairs

\[
x_k+ib,\qquad x_k-ib
\tag{17}
\]

with those multiplicities. It has no real elements and

\[
|\mathcal Z_{m,R}|=2^{m+1}.
\tag{18}
\]

The horizontal polynomial is

\[
P_m(t)
=\sum_{k=0}^m\binom mk e^{-2\pi i tx_k}
=\left(1+e^{-\pi i t/R}\right)^m,
\tag{19}
\]

hence

\[
S_{\mathcal Z_{m,R}}(t)
=2\cosh(2\pi bt)P_m(t).
\tag{20}
\]

Define the even nonnegative weight

\[
W_{m,R}(t)
:=\cosh^2(2\pi bt)
\left(4\cos^2\frac{\pi t}{2R}\right)^m.
\tag{21}
\]

Then (9) becomes

\[
\boxed{
Q_H(\mathcal Z_{m,R})
=4\int_{\mathbb R}\phi(t)W_{m,R}(t)\,dt.
}
\tag{22}
\]

The difference from WI-147 is that `R` is no longer a fixed support radius. It is chosen **after** the localization strength `lambda`, far enough out that the exponentially weighted tail of `phi` is negligible.

## 4. Uniform local Gaussian concentration around the prescribed negative point

For `t>=0` define

\[
F_R(t)
:=\frac{\pi t}{R}\tan\theta
+\log\left(4\cos^2\frac{\pi t}{2R}\right)
\tag{23}
\]

where the logarithm is interpreted as `-infinity` at its zeros. The exact factorization is

\[
W_{m,R}(t)
=\frac14 e^{mF_R(t)}
\left(1+e^{-4\pi bt}\right)^2.
\tag{24}
\]

On `[0,R)` one has

\[
F_R'(t)
=\frac{\pi}{R}
\left(
\tan\theta-	an\frac{\pi t}{2R}
\right),
\tag{25}
\]

so `F_R'(a)=0`, and

\[
F_R''(t)
=-\frac{\pi^2}{2R^2}
\sec^2\frac{\pi t}{2R}
\le-\frac{\pi^2}{2R^2}.
\tag{26}
\]

Therefore for every `0<=t<=R`, by continuity at `t=R`,

\[
\boxed{
F_R(a)-F_R(t)
\ge\frac{\pi^2}{4R^2}(t-a)^2.
}
\tag{27}
\]

On the smaller interval containing `I`, condition (12) gives `t<=R/2`, hence `sec^2(pi t/(2R))<=2`. Thus for `t in I`,

\[
\boxed{
F_R(a)-F_R(t)
\le\frac{\pi^2}{2R^2}(t-a)^2.
}
\tag{28}
\]

Normalize

\[
w_{m,R}(t):=\frac{W_{m,R}(t)}{W_{m,R}(a)}.
\tag{29}
\]

The last factor in (24) lies between `1` and `4`, so

\[
\frac14e^{m(F_R(t)-F_R(a))}
\le w_{m,R}(t)
\le4e^{m(F_R(t)-F_R(a))}.
\tag{30}
\]

Choose `lambda` large enough that `lambda^{-1/2}<delta`, and put

\[
J_\lambda
:=[a-\lambda^{-1/2},a+\lambda^{-1/2}]
\subset I.
\tag{31}
\]

Using (14), (28), and (30), for `t in J_lambda`,

\[
w_{m,R}(t)
\ge\frac14
\exp\left(
-\frac{\pi^2\lambda_R}{2\lambda}
\right)
\ge\frac14e^{-\pi^2}
=:c_0>0.
\tag{32}
\]

Hence the negative band contributes, after normalization by `W_{m,R}(a)`, at most

\[
\boxed{
\int_{J_\lambda}\phi(t)w_{m,R}(t)\,dt
\le-\frac{2\eta c_0}{\sqrt\lambda}.
}
\tag{33}
\]

Meanwhile, for `t in [0,R]\setminus I`, equation (27) gives

\[
w_{m,R}(t)
\le4\exp\left(-\frac{\pi^2\lambda\delta^2}{4}\right).
\tag{34}
\]

Writing

\[
M_+:=\int_0^\infty\phi_+(t)\,dt<\infty,
\tag{35}
\]

the total positive contribution from `[0,R]\setminus I` is therefore at most

\[
4M_+\exp\left(-\frac{\pi^2\lambda\delta^2}{4}\right).
\tag{36}
\]

For large `lambda`, (36) is much smaller than the `lambda^{-1/2}` negative mass in (33).

## 5. Superexponential integrability absorbs the noncompact tail

It remains to control `t>=R`, where the trigonometric factor is periodic and the compact-support proof of WI-147 cannot simply stop the integral.

Put

\[
\alpha_R:=\frac{\pi}{R}\tan\theta.
\tag{37}
\]

Since `theta<=pi/4`, the elementary bound `tan(theta)<=2theta` gives

\[
\alpha_R\le\frac{\pi^2a}{R^2},
\qquad
m\alpha_R\le2\pi^2a\lambda.
\tag{38}
\]

Also

\[
F_R(a)-\log4
=2\theta\tan\theta+2\log(\cos\theta)
\ge0.
\tag{39}
\]

Indeed the right side vanishes at `theta=0` and its derivative is `2 theta sec^2(theta)>0`. Since `log(4 cos^2)<=log4` everywhere, equations (30), (38), and (39) give the global tail estimate

\[
\boxed{
w_{m,R}(t)
\le4e^{2\pi^2a\lambda t}
\qquad(t\ge R).
}
\tag{40}
\]

Now fix a sufficiently large `lambda`. By the exponential-moment hypothesis (2),

\[
\int_0^\infty |\phi(t)|e^{2\pi^2a\lambda t}\,dt<\infty.
\tag{41}
\]

Therefore its tail tends to zero as `R->infinity`. We may choose `R` satisfying (12) so large that

\[
4\int_R^\infty
\phi_+(t)e^{2\pi^2a\lambda t}\,dt
\le\frac{\eta c_0}{2\sqrt\lambda}.
\tag{42}
\]

Choose `lambda` first so large that, in addition,

\[
4M_+e^{-\pi^2\lambda\delta^2/4}
\le\frac{\eta c_0}{2\sqrt\lambda}.
\tag{43}
\]

Combining (33), (36), (40)--(43), and discarding all additional negative contributions gives

\[
\int_0^\infty\phi(t)w_{m,R}(t)\,dt
\le
-\frac{2\eta c_0}{\sqrt\lambda}
+\frac{\eta c_0}{2\sqrt\lambda}
+\frac{\eta c_0}{2\sqrt\lambda}
<0.
\tag{44}
\]

Because `W_{m,R}(a)>0`, equation (44) implies

\[
\int_0^\infty\phi(t)W_{m,R}(t)\,dt<0.
\tag{45}
\]

Evenness of both `phi` and `W_{m,R}` doubles the same sign on the negative half-axis. Thus (22) gives

\[
\boxed{
Q_H(\mathcal Z_{m,R})<0.
}
\tag{46}
\]

But `Z_{m,R}` contains no real points, so the assumed universal inequality requires by (10)

\[
Q_H(\mathcal Z_{m,R})
\ge2|\mathcal Z_{m,R}|=2^{m+2}>0,
\tag{47}
\]

a contradiction. Hence no negative point of `phi` exists and (5) follows.

The order of choices is load-bearing and removes the apparent noncompact obstruction:

\[
\boxed{
\text{choose localization strength }\lambda
\quad\longrightarrow\quad
\text{use (2) to choose a farther truncation radius }R
\quad\longrightarrow\quad
m\asymp\lambda R^2.
}
\tag{48}
\]

The local concentration depends on `m/R^2=lambda_R`, while the uncontrolled far tail is charged only by an exponential moment whose rate is `O(lambda)`. Since (2) supplies every such moment, `R` can always be moved far enough out after `lambda` is fixed.

## 6. Relation to WI-145--WI-147

WI-145 used only the one-conjugate-pair condition `H(iy)>=1`. That test rules out a negative outer tail lying beyond all positive spectral mass because bilateral-Laplace growth eventually has the wrong sign.

WI-146 proved that this one-pair obstruction is not enough: a fixed negative band at radius `a` can be protected at the two-point level by positive mass at a larger radius `R`, with repair mass only `O((a/R)^2)`. This remains a correct statement. It concerns the complete cardinality-two necessary conditions, not full multiset universality.

WI-147 showed that, for a continuous **compactly supported** profile, large binomial conjugate-pair families localize the signed spectral integral at any chosen negative band and kill the repair. The current finding removes compact support by making the binomial period/truncation radius part of the probe. The new implication is

\[
\boxed{
\begin{aligned}
&\text{two-point scalar admissibility}
\not\Rightarrow \phi\ge0,\\
&\text{full scalar universality + compact spectrum}
\Rightarrow \phi\ge0,\\
&\text{full scalar universality + all absolute exponential moments}
\Rightarrow \phi\ge0.
\end{aligned}
}
\tag{49}
\]

So the specific surviving scalar route left by WI-147 -- a **fixed noncompact oscillatory repair with sufficiently rapid decay to define the same Fourier integral on every complex gap** -- is now closed.

## 7. Prior art and novelty boundary

Classical Bochner--Khinchin theory characterizes continuous positive-definite translation kernels on the real line as Fourier transforms of positive measures. Jorge Buescu, A. C. Paixão and A. Symeonides, *Complex Positive Definite Functions on Strips*, Complex Analysis and Operator Theory 11 (2017), 627--649, DOI `10.1007/s11785-015-0527-y`, give a Fourier--Laplace characterization of holomorphic positive-definite functions on strips by exponentially finite positive measures, unifying the real-axis Bochner and imaginary-axis Widder viewpoints.

Those theorems do **not** directly imply the present result. Their input is positive definiteness of all finite quadratic forms with arbitrary coefficients. The Lamzouri-form hypothesis (4) is different: it tests coefficient-one sums arising from conjugation-invariant multisets and includes the population term `2|Z|-s(Z)`. WI-146 already demonstrates that its complete two-point consequences are strictly weaker than Fourier positivity. The additional rigidity here comes from the specific large binomial/common-depth multisets, together with the order-of-limits argument (48).

The primary zeta-side source is Lamzouri Proposition 2.1. The current `weil_inertia` corpus was checked against WI-143--WI-147, which contain the closest scalar/Hilbert/sign obstructions and explicitly leave the noncompact repaired-profile case open after WI-147. Broader searches around Bochner/Widder Fourier--Laplace representation, positive definite functions on strips, signed Fourier measures, copositive kernels, and trigonometric/exponential-polynomial localization did not locate this exact implication from universal conjugation-invariant unit-coefficient multiset testing. This is the novelty boundary used by the line, not a claim of mathematical priority.

## 8. Boundaries and surviving routes

Several restrictions remain important.

First, the theorem concerns one **fixed** scalar profile. A sequence `phi_T` can move its positive repair outward as `T` changes while simultaneously changing the required exponential moments. The proof above chooses `R` after `lambda` for one fixed `phi`; it supplies no uniform statement for a `T`-dependent family unless one has uniform exponential-tail control strong enough to repeat (42).

Second, the theorem assumes the complex kernel is represented by the absolutely convergent Fourier--Laplace integral (3). A signed distribution or a real-line profile whose transform admits some separate analytic continuation despite failure of absolute exponential moments lies outside the argument. Such an object would also require a new prime-side justification before it could replace the standard test-function interface.

Third, universality over **all** finite conjugation-invariant multisets is essential. A theorem proved only for actual zeta-zero configurations could exclude the binomial/common-depth probes. Establishing such a restriction would be new zeta-specific arithmetic or spectral information; it is not supplied by Lamzouri's universal Hilbert inequality.

Fourth, the conclusion is only a necessary sign condition on a single scalar Fourier density. It does not say that every nonnegative profile satisfies (4), and it does not rule out genuinely joint multi-profile inequalities, sign-indefinite matrix observables, nonlinear incidence constraints, or explicit horizontal/negative-inertia correction terms. Those architectures retain information that a single scalar pair sum discards.

Finally, the theorem does not improve the current simple-critical proportion by itself. It is a decisive barrier: within the regular fixed-kernel class naturally compatible with evaluation on arbitrary off-critical complex gaps, **signed Fourier mass cannot be the missing scalar degree of freedom**.

## Research consequence

After WI-148, the single-scalar CGdL/Lamzouri transplant is closed for both compact profiles and the natural noncompact entire-density class. A farther positive spectral repair can defeat every one- and two-point test, but full universal multiset testing eventually localizes any fixed negative band and exposes it.

Accordingly, further optimization of a fixed scalar translation-invariant kernel should not be expected to import the RH-only signed-tail gain unless it leaves at least one hypothesis above. The structurally live directions are now narrower: a genuinely joint/matrix observable; an explicit horizontal or negative-inertia charge; a source-specific inequality using arithmetic restrictions on actual zeros; or a carefully uniform `T`-dependent construction whose tail movement is paid for on both the prime side and the off-line zero side. This is a route closure, not a new numerical zero proportion.