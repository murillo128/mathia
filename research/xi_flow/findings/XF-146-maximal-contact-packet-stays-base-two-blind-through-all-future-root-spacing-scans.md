# XF-146 — maximal-contact packet stays base-two blind through all future root-spacing scans

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/FULL-FUTURE-ROOT-SPACING-SCAN-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-SCAN` + `TRANSITION-TIME` + `SHARP-EXPONENTIAL-RATE`. XF-145 shows that the maximal-contact XF-141 packet is superexponentially invisible on a root-spacing real tube while `NaS_N -> 0`, and leaves `s asymp 1/(aN)` as the first heat scale where that particular estimate stops forcing superexponential blindness. The same packet in fact remains exponentially transition-blind on the **entire future heat history** of that tube. Its sharp exponential visibility rate is base two: the complete tube difference is `exp[-(log 2)N+o(N)]`, and a signal of that exponential size is already attained near the later clock `as log N/N`.

## Claim

Let

\[
N=2M,
\qquad
r=M-1=\frac N2-1,
\tag{1}
\]

and use the XF-141 amplitude family

\[
E_\lambda(w,s)
=1+w^N+\lambda t_*\Delta E(w,s),
\qquad 0<\lambda\le1,
\tag{2}
\]

under the coefficient heat flow

\[
E_k(s)=E_k(0)e^{-ak(N-k)s},
\qquad a>0.
\tag{3}
\]

For every fixed `rho>0`, set

\[
\lambda_\rho=\lambda_{r,\rho}
=\mathcal A_r(-\rho)^{-1}
\tag{4}
\]

as in XF-141. Then

\[
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_\rho})=-\rho.
\tag{5}
\]

Observe the real axis through

\[
R_\lambda(x,s)
:=E_\lambda\!\left(-e^{-2\pi i x/L},s\right).
\tag{6}
\]

Fix `C>0`. For every even `N>=4`, uniformly for all future heat times,

\[
\boxed{
\sup_{s\ge0}\sup_{|x|\le CL/N}
|R_1(x,s)-R_{\lambda_\rho}(x,s)|
\le
16e^{2\pi C}2^{-N}.
}
\tag{7}
\]

Thus a decoder from the **complete future root-spacing tube** to `Lambda_per` cannot have polynomial conditioning. If `K_N` is a Lipschitz constant for such a decoder in the tube sup norm, then

\[
\boxed{
K_N
\ge
\frac{\rho}{16e^{2\pi C}}\,2^N.
}
\tag{8}
\]

The exponential rate in `(7)` is sharp for this maximal-contact packet. Put

\[
s_N:=\frac{\log N}{aN}.
\tag{9}
\]

At the center `x=0`,

\[
\boxed{
|R_1(0,s_N)-R_{\lambda_\rho}(0,s_N)|
=
\left(1+o(1)\right)
\frac{16}{eN}\,2^{-N}.
}
\tag{10}
\]

Consequently

\[
\boxed{
\lim_{N\to\infty}\frac1N
\log
\sup_{s\ge0,\ |x|\le CL/N}
|R_1-R_{\lambda_\rho}|
=-\log2.
}
\tag{11}
\]

So the inverse-degree scale isolated by XF-145 is only the crossover from **superexponential** to **exponential** visibility. No fixed or growing amount of future heat observation, while spatial access remains inside one root-spacing tube, makes this maximal-contact transition direction polynomially visible. Its first near-optimal exponential signal appears only after a logarithmic multiple of the inverse-degree clock.

## 1. The XF-145 Gaussian representation has a global future envelope

Use the XF-145 coordinate

\[
\beta=-\frac{2\pi iNx}{L},
\qquad
y=\frac\beta N=-\frac{2\pi ix}{L},
\qquad
u:=as.
\tag{12}
\]

For the maximal packet, XF-145 gives the exact finite-dimensional heat-semigroup identity

\[
t_*\Delta Q_\beta(s)
=-2(-1)^{M+r}e^{\beta/2-M^2u}
\mathbb E\,
\sinh^{2r}\!\left(
\frac y2+\sqrt{\frac u2}\,Z
\right),
\qquad Z\sim N(0,1).
\tag{13}
\]

For the physical real probe, write

\[
y=iv,
\qquad
|v|\le\frac{2\pi C}{N},
\qquad
q:=\sqrt{\frac u2}.
\tag{14}
\]

The exact modulus identity

\[
|\sinh(qZ+iv/2)|^2
=\sinh^2(qZ)+\sin^2(v/2)
\tag{15}
\]

is the key extra structure. Put

\[
b:=|\sin(v/2)|\le\frac{\pi C}{N}.
\tag{16}
\]

For `t>=0`,

\[
\sqrt{\sinh^2t+b^2}
\le \sinh t+b
\le \frac12e^t(1+2b).
\tag{17}
\]

Hence

\[
\begin{aligned}
|t_*\Delta Q_\beta(s)|
&\le
2e^{-M^2u}4^{-r}(1+2b)^{2r}
\mathbb E e^{2rq|Z|}\\
&\le
4\,4^{-r}(1+2b)^{2r}e^{-(M^2-r^2)u}.
\end{aligned}
\tag{18}
\]

The last step uses the elementary Gaussian bound

\[
\mathbb E e^{t|Z|}\le2e^{t^2/2}.
\tag{19}
\]

Now the maximal depth gives the exact spectral edge gap

\[
M^2-r^2=N-1,
\tag{20}
\]

while `(16)` gives

\[
(1+2b)^{2r}
\le e^{4rb}
\le e^{2\pi C}.
\tag{21}
\]

Since

\[
4\,4^{-r}
=16\,2^{-N},
\tag{22}
\]

we obtain

\[
\boxed{
|t_*\Delta Q_\beta(s)|
\le16e^{2\pi C}2^{-N}e^{-(N-1)u}
\le16e^{2\pi C}2^{-N}
}
\tag{23}
\]

for every `u>=0` and every point of the root-spacing tube. Finally,

\[
R_1-R_{\lambda_\rho}
=(1-\lambda_\rho)t_*\Delta Q,
\tag{24}
\]

with `0<lambda_rho<=1`, so `(23)` proves `(7)`.

This argument does not truncate the heat interval and does not use `Nu -> 0`. The base-two factor comes from the exact `4^{-r}` central-difference normalization after the maximal choice `2r=N-2`; the remaining heat factor is dissipative because the nearest surviving spectral shell lies `N-1` above zero.

## 2. A logarithmic inverse-degree heat time reaches the base-two scale

At the tube center `v=0`, the Gaussian integrand in `(13)` is nonnegative, so no triangle inequality is needed. Define

\[
A_N(u)
:=|t_*\Delta Q_0(s)|
=2e^{-M^2u}
\mathbb E\sinh^{2r}(qZ).
\tag{25}
\]

Using evenness and, for `z>=0`,

\[
\sinh(qz)
=\frac12e^{qz}(1-e^{-2qz}),
\tag{26}
\]

complete the Gaussian square. With

\[
\mu:=2rq=r\sqrt{2u},
\tag{27}
\]

one obtains the exact positive representation

\[
\boxed{
A_N(u)
=4^{1-r}e^{-(N-1)u}J_N(u),
}
\tag{28}
\]

where

\[
J_N(u)
:=
\int_0^\infty
\frac{e^{-(z-\mu)^2/2}}{\sqrt{2\pi}}
(1-e^{-2qz})^{2r}\,dz,
\qquad
0\le J_N(u)\le1.
\tag{29}
\]

Take

\[
u_N=as_N=\frac{\log N}{N}.
\tag{30}
\]

Under the shifted Gaussian density in `(29)`, write `z=mu+Y` with `Y=O_P(1)`. Then

\[
2qz
=2ru_N+2qY
=\log N+o_P(1),
\tag{31}
\]

because `2r=N-2` and `q->0`. Therefore

\[
2r\,e^{-2qz}\longrightarrow1
\quad\text{in probability},
\tag{32}
\]

and hence

\[
(1-e^{-2qz})^{2r}\longrightarrow e^{-1}
\quad\text{in probability}.
\tag{33}
\]

Also `mu->infinity`, so the omitted Gaussian mass below `z=0` tends to zero. Since the integrand in `(29)` is bounded by `1`, dominated convergence gives

\[
\boxed{J_N(u_N)\longrightarrow e^{-1}.}
\tag{34}
\]

Moreover

\[
e^{-(N-1)u_N}
=N^{-(N-1)/N}
=\frac{1+o(1)}N.
\tag{35}
\]

Combining `(28)`, `(34)`, `(35)`, and `4^{1-r}=16\,2^{-N}` yields

\[
\boxed{
A_N(u_N)
=\left(1+o(1)\right)
\frac{16}{eN}2^{-N}.
}
\tag{36}
\]

It remains only to check that the transition retuning does not suppress this witness. XF-141 defines

\[
\lambda_\rho
=\left[
\frac1{H_r}\sum_{j=0}^r
|c_j|e^{a(M^2-j^2)\rho}
\right]^{-1}.
\tag{37}
\]

Every rate obeys `M^2-j^2>=M^2-r^2=N-1`, so for fixed `rho>0`,

\[
0<\lambda_\rho
\le e^{-a(N-1)\rho}.
\tag{38}
\]

Thus

\[
1-\lambda_\rho=1+o(1),
\tag{39}
\]

and `(36)` proves the matched-control asymptotic `(10)`. Together with `(7)`, this proves the sharp exponential rate `(11)`.

## 3. The full future history does not repair XF-144 conditioning

XF-144 proves an exact-identifiability statement: an arbitrarily small nonconstant real-axis scan over a nonempty time interval can break the reflected-shell degeneracy. XF-145 then shows that a root-spacing scan over `o(1/N)` heat time is superexponentially ill-conditioned for the transition functional.

XF-146 closes the temporal escape for the **same maximal-contact packet**. Even if the observer is given every spatial point with `|x|<=CL/N` and every future heat time `s>=0`, the two admissible histories in `(5)` remain only `O_C(2^{-N})` apart. A moving probe that stays inside this tube receives strictly less information, so the same exponential lower bound applies to any such trajectory.

The scale

\[
s\asymp\frac1{aN}
\tag{40}
\]

is therefore not a stable-recovery threshold. It is only where the maximal-contact signal ceases to be forced below every `e^{-cN}` scale. The packet keeps unfolding until the later clock

\[
s\asymp\frac{\log N}{aN},
\tag{41}
\]

where `(10)` shows that it finally reaches its natural base-two exponential scale. More future heat time cannot improve the exponential order of the complete root-spacing-tube signal.

This separates two notions that were still partially conflated after XF-145:

- **short-time contact order** controls the superexponential `N^{-Theta(N)}` invisibility near the transition slice;
- **maximal-shell normalization** controls the eventual `2^{-N}` visibility ceiling after the packet has unfolded.

The crossover is intrinsic to this matched-control family and does not depend on a finite time Taylor truncation.

## 4. Logarithmic and reference-normalized observations inherit the obstruction

Fix `0<C<1/4`. The common endpoint carrier

\[
B(x)=1+e^{-2\pi iNx/L}
\tag{42}
\]

obeys

\[
|B(x)|\ge2\cos(\pi C)>0
\tag{43}
\]

throughout the root-spacing tube. Equation `(23)` shows that the entire maximal packet is `O_C(2^{-N})` there for every future time. Hence, for all sufficiently large `N`, every interpolation

\[
B+\theta t_*\Delta Q,
\qquad 0\le\theta\le1,
\tag{44}
\]

is uniformly zero-free on the tube. Choosing compatible logarithms,

\[
\log R_1-\log R_{\lambda_\rho}
=
\int_{\lambda_\rho}^1
\frac{t_*\Delta Q}{B+\theta t_*\Delta Q}\,d\theta,
\tag{45}
\]

so the complete future logarithmic tube difference is also `O_C(2^{-N})`. Dividing both controls by any common nonvanishing analytic reference cancels from `(45)` exactly.

Thus the Gaussian/reference quotient remains potentially useful only through a **source-specific restriction** or a genuinely different observation geometry. It cannot by itself improve the target-side conditioning of this root-spacing full-future scan.

## 5. Relation to XF-136 and novelty boundary

XF-136 already gives a stronger numerical exponential aperture constant `b_*=0.779767...` for **another optimization regime**: it chooses `r/M -> alpha_*=0.546705...` to hide a transition-sharp packet on a macroscopic complex patch for all future times. The maximal-contact choice `r=M-1` used here is not optimal for that complex-patch envelope and should not replace XF-136.

The new statement is instead the missing continuation of XF-141/XF-145. Maximal depth is what gives exact contact through spatial order `N-3` and the `exp[-N log N+O(N)]` root-spacing invisibility at `s=0`. XF-146 shows that this same high-contact packet does **not** become polynomially observable when one waits beyond the `1/(aN)` boundary left open by XF-145. Its full-future real-tube modulus has the separate sharp exponent `log 2`.

A directed prior-art audit checked the neighboring literature on fast heat observability/Lebeau--Robbiano spectral inequalities, Remez--Turan propagation of smallness, and classical central finite differences/divided differences. Exponential heat-observability costs and high-order finite-difference cancellation are classical mechanisms, but the proof above uses no external theorem beyond elementary Gaussian completion of the square. The audit did not locate the specific combination of a transition-sharp unit-circle heat family, maximal parabolic contact, a complete root-spacing real tube, and the sharp base-two future visibility exponent. No new external dependency is load-bearing, so `SOURCES.md` does not need a new anchor.

## Checks and falsifiers

The global bound has two direct checks. At `u=0`, XF-145 gives the much smaller exact identity

\[
|t_*\Delta Q|
=2\left|\sin\frac{\pi x}{L}\right|^{N-2},
\tag{46}
\]

which is compatible with `(23)`. For large `u`, the nearest surviving shells are `j=\pm r`; their heat rate is exactly `N-1`, matching the dissipative factor in `(23)`.

The asymptotic `(10)` is falsified if the shifted integral `(29)` fails to converge to `e^{-1}` at `u_N=(log N)/N`. Equations `(31)`--`(34)` reduce this to a bounded-convergence calculation under a Gaussian whose mean tends to infinity. The transition factor is independently controlled by `(38)`.

The theorem is target-side and periodic. It does **not** assert that the actual Xi source realizes the maximal central packet, and it does not exclude an Xi-specific relation that removes this direction. It also does not rule out observations that leave the root-spacing tube, probe a distinct complex height/shell, or use a genuinely nonlocal source-sensitive transform. Those remain the live escape routes.

## Consequence for the current frontier

The target-side real-scan route now has a cleaner quantitative boundary. Exact state identification can occur after arbitrarily small motion, but the transition functional remains exponentially ill-conditioned even under the complete future history of a one-root-spacing real tube. The high-contact packet changes rate class from superexponential to exponential as heat time reaches inverse degree, and reaches its best exponential order only around `(log N)/(aN)`.

Accordingly, merely waiting longer at the same microscopic spatial aperture is no longer a plausible polynomial-conditioning repair. Progress must enlarge the observation geometry beyond root-spacing scale, exploit a nonlocal transition-specific observable, or prove a source-faithful Xi theorem excluding the central packet direction.