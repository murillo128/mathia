# PC-196 — quadratic reciprocal zero scale is a singular even-exponent resonance

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for robustness of the PC-195 `p^(3/4)` prime-shell Fourier-zero scale under fixed reciprocal-exponent deformation.

PC-194 shows that the reciprocal family

\[
H_{p,\alpha}(x)
:=
1-\left(\frac{1-e^{-|x|}}{1-e^{-p|x|}}\right)^\alpha
\tag{1}
\]

is Fourier-positive on prime shells for `0<alpha<=1`, while the canonical quadratic exponent `alpha=2` creates real zeros. PC-195 then identifies the first quadratic zero at the mesoscopic scale `p^(3/4)` and a later sign recovery on the refinement scale `Theta(p)`.

The natural robustness question is whether the `p^(3/4)` mechanism persists when the reciprocal exponent is moved below `2`. It does not. For every fixed

\[
1<\alpha<2,
\tag{2}
\]

prime-shell Fourier zeros are impossible on **every sublinear frequency scale** `t=o(p)`. If zeros occur, their first possible asymptotic scale is the ordinary refinement scale `Theta(p)`. Moreover, zeros do in fact occur on that linear scale for every fixed `alpha` sufficiently close to `2` from below.

Thus the PC-195 `p^(3/4)` law is not a stable feature of the reciprocal family. It is a singular resonance at the even exponent `alpha=2`, caused by cancellation of the leading large-frequency tail of the outer profile.

## 1. Exact outer / refinement-layer decomposition

Write

\[
H_{p,\alpha}=h_\alpha+D_{p,\alpha},
\tag{3}
\]

where

\[
h_\alpha(x)
:=
1-(1-e^{-|x|})^\alpha
\tag{4}
\]

and

\[
D_{p,\alpha}(x)
:=
(1-e^{-|x|})^\alpha
\left[1-(1-e^{-p|x|})^{-\alpha}\right]
\le0.
\tag{5}
\]

The first term is independent of the shell. The second is a negative boundary correction concentrated on the refinement width `x=Theta(1/p)`.

For `t!=0`, integration by parts followed by `u=e^{-x}` gives the exact beta/gamma formula

\[
\boxed{
\widehat h_\alpha(t)
=
\frac{2\Gamma(\alpha+1)}{t}
\operatorname{Im}
\frac{\Gamma(1-it)}{\Gamma(\alpha+1-it)}.
}
\tag{6}
\]

The transform convention is the same as PC-194/PC-195,

\[
\widehat f(t)=\int_{\mathbb R}f(x)e^{-itx}\,dx.
\tag{7}
\]

Equation (6) reduces at `alpha=1` to `2/(1+t^2)` and at `alpha=2` to the PC-195 profile

\[
\widehat h_2(t)
=
\frac{12}{(1+t^2)(4+t^2)}.
\tag{8}
\]

## 2. The outer profile is strictly Fourier-positive through `alpha=2`

Put

\[
r_\alpha(t)
:=
\frac{\Gamma(1-it)}{\Gamma(\alpha+1-it)}.
\tag{9}
\]

For `t>0`, differentiating its argument with respect to `alpha` gives

\[
\frac{\partial}{\partial\alpha}\arg r_\alpha(t)
=
-\operatorname{Im}\psi(\alpha+1-it)
=
\sum_{n\ge0}
\frac{t}{(n+\alpha+1)^2+t^2}
>0.
\tag{10}
\]

At `alpha=0`, `r_0(t)=1`. At `alpha=2`,

\[
r_2(t)=\frac1{(1-it)(2-it)},
\tag{11}
\]

so

\[
0<\arg r_\alpha(t)
\le
\arg r_2(t)
=
\arctan t+\arctan(t/2)
<\pi
\qquad(0<\alpha\le2).
\tag{12}
\]

Hence

\[
\boxed{
\widehat h_\alpha(t)>0
\qquad
(t\in\mathbb R,\ 0<\alpha\le2).
}
\tag{13}
\]

For fixed `1<alpha<2`, the standard gamma-ratio asymptotic in (6) yields

\[
\boxed{
\widehat h_\alpha(t)
\sim
C_\alpha |t|^{-\alpha-1},
\qquad
C_\alpha
:=
2\Gamma(\alpha+1)\sin\frac{\pi\alpha}{2}
>0.
}
\tag{14}
\]

The coefficient is the key quantity. It is strictly positive throughout the open interval `(1,2)`, but vanishes exactly at the endpoint `alpha=2`.

## 3. The refinement correction has total mass `Theta(p^(-alpha-1))`

Because `D_{p,alpha}<=0`,

\[
|\widehat D_{p,\alpha}(t)|
\le
\|D_{p,\alpha}\|_1.
\tag{15}
\]

Changing variables `u=px`,

\[
\begin{aligned}
p^{\alpha+1}\|D_{p,\alpha}\|_1
=
2\int_0^\infty
\bigl[p(1-e^{-u/p})\bigr]^\alpha
\left[(1-e^{-u})^{-\alpha}-1\right]du.
\end{aligned}
\tag{16}
\]

Since

\[
0\le p(1-e^{-u/p})\le u,
\tag{17}
\]

and

\[
u^\alpha\left[(1-e^{-u})^{-\alpha}-1\right]
\tag{18}
\]

is bounded at `u=0` and exponentially decaying at infinity, dominated convergence gives

\[
\boxed{
p^{\alpha+1}\|D_{p,\alpha}\|_1
\longrightarrow
A_\alpha,
}
\tag{19}
\]

where

\[
\boxed{
A_\alpha
:=
2\int_0^\infty
u^\alpha\left[(1-e^{-u})^{-\alpha}-1\right]du
\in(0,\infty).
}
\tag{20}
\]

At `alpha=2`, this specializes to the PC-195 constant

\[
A_2=4\bigl(\zeta(2)+\zeta(3)\bigr).
\tag{21}
\]

## 4. No fixed exponent `1<alpha<2` can have a sublinear prime-shell zero scale

Let `alpha` be fixed in `(1,2)` and let `t_p>=0` be any sequence satisfying

\[
t_p=o(p).
\tag{22}
\]

Then

\[
\boxed{
\widehat H_{p,\alpha}(t_p)>0
}
\tag{23}
\]

for all sufficiently large primes `p`.

If `t_p` remains bounded along a subsequence, (13) gives a positive lower bound for `\widehat h_\alpha` on the relevant compact interval, while (19) makes `\|D_{p,\alpha}\|_1` tend to zero. If `t_p->infinity`, equations (14), (15), and (19) give

\[
\widehat h_\alpha(t_p)
\asymp
t_p^{-\alpha-1},
\qquad
|\widehat D_{p,\alpha}(t_p)|
=O(p^{-\alpha-1}),
\tag{24}
\]

and therefore

\[
\frac{|\widehat D_{p,\alpha}(t_p)|}
{\widehat h_\alpha(t_p)}
=
O\left((t_p/p)^{\alpha+1}\right)
\longrightarrow0.
\tag{25}
\]

The two cases cover an arbitrary sequence by subsequences. Consequently **there is no analogue of the PC-195 `p^(3/4)` first-zero scale for any fixed exponent below `2`**. More generally, no `p^beta` scale with `beta<1`, no logarithmic scale, and no other `o(p)` frequency can host prime-shell zeros asymptotically.

## 5. The first possible fixed-exponent failure is a universal linear-scale profile

Set

\[
t=cp,
\qquad c>0\text{ fixed}.
\tag{26}
\]

Equation (14) gives

\[
p^{\alpha+1}\widehat h_\alpha(cp)
\longrightarrow
C_\alpha c^{-\alpha-1}.
\tag{27}
\]

For the boundary term, the same change of variables as in (16) gives, locally uniformly for `c` in compact subsets of `(0,infinity)`,

\[
\boxed{
p^{\alpha+1}\widehat H_{p,\alpha}(cp)
\longrightarrow
K_\alpha(c),
}
\tag{28}
\]

with

\[
\boxed{
K_\alpha(c)
=
C_\alpha c^{-\alpha-1}
+
2\int_0^\infty
u^\alpha
\left[1-(1-e^{-u})^{-\alpha}\right]
\cos(cu)\,du.
}
\tag{29}
\]

The profile is positive at both asymptotic ends. First,

\[
K_\alpha(c)\longrightarrow+\infty
\qquad(c\downarrow0),
\tag{30}
\]

because `C_alpha>0`. For the opposite end, define

\[
g_\alpha(u)
:=
u^\alpha\left[1-(1-e^{-u})^{-\alpha}\right].
\tag{31}
\]

Near zero,

\[
g_\alpha(u)
=
-1-\frac\alpha2u+u^\alpha+O(u^2),
\tag{32}
\]

so `g_alpha'(0)=-alpha/2`. For `1<alpha<2`, `g_alpha''` is integrable: its only singular contribution at zero is `O(u^(alpha-2))`, and the function decays exponentially at infinity. Two integrations by parts therefore give

\[
2\int_0^\infty g_\alpha(u)\cos(cu)\,du
=
\frac\alpha{c^2}+o(c^{-2}).
\tag{33}
\]

Since the outer term in (29) is `O(c^(-alpha-1))=o(c^-2)`,

\[
\boxed{
K_\alpha(c)
=
\frac\alpha{c^2}+o(c^{-2})
>0
\qquad(c\to\infty).
}
\tag{34}
\]

Thus fixed-exponent sign changes, if present, must be created at finite `c` inside the ordinary refinement layer rather than by a new mesoscopic balance.

## 6. The Fourier failure already persists for exponents just below `2`

The linear profile is not merely a no-go envelope. It shows that the zero-producing regime extends into the open interval below the quadratic exponent.

At `alpha=2`, the leading outer coefficient vanishes,

\[
C_2
=2\Gamma(3)\sin\pi
=0,
\tag{35}
\]

and the boundary part of (29) at zero frequency is exactly

\[
2\int_0^\infty
u^2\left[1-(1-e^{-u})^{-2}\right]du
=
-4\bigl(\zeta(2)+\zeta(3)\bigr)<0.
\tag{36}
\]

By continuity in `c`, choose a fixed sufficiently small `c_0>0` for which the `alpha=2` boundary cosine integral remains negative. For this fixed `c_0`, the integral in (29) is continuous in `alpha` as `alpha->2^-`, while

\[
C_\alpha c_0^{-\alpha-1}\longrightarrow0.
\tag{37}
\]

Hence there exists

\[
\alpha_0<2
\tag{38}
\]

such that

\[
\boxed{
K_\alpha(c_0)<0
\qquad
(\alpha_0<\alpha<2).
}
\tag{39}
\]

Combined with (30) and (34), this forces at least two positive zeros of `K_alpha`: one while the profile moves from positive to negative, and one while it returns to positive. The locally uniform convergence in (28) transfers those sign changes to every sufficiently large prime shell. Therefore, for every fixed `alpha` in a nonempty interval immediately below `2`,

\[
\boxed{
\widehat H_{p,\alpha}
\text{ has at least two positive real zeros at }t=\Theta(p)
}
\tag{40}
\]

for all sufficiently large primes.

No exact transition exponent is asserted here. The argument establishes existence of an interval `(alpha_0,2)` but does not identify its optimal left endpoint.

## 7. Why `alpha=2` is singular

For fixed `1<alpha<2`, the positive outer tail has size

\[
\widehat h_\alpha(t)
\sim
C_\alpha t^{-\alpha-1},
\qquad C_\alpha>0,
\tag{41}
\]

while the entire negative refinement correction has size `Theta(p^(-alpha-1))`. These can compete only once `t` reaches `Theta(p)`.

At `alpha=2`, however, the leading coefficient `C_alpha` vanishes because

\[
\sin(\pi\alpha/2)=0.
\tag{42}
\]

The exact outer transform then decays as

\[
\widehat h_2(t)
\sim12t^{-4},
\tag{43}
\]

rather than the generic `t^{-3}` suggested by the first gamma-ratio magnitude. The refinement mass is `Theta(p^-3)`, so balancing the two gives

\[
t^{-4}\asymp p^{-3}
\quad\Longleftrightarrow\quad
t\asymp p^{3/4},
\tag{44}
\]

which is precisely the PC-195 first-zero scale.

The exponent `3/4` is therefore explained by an **even-integer cancellation in the outer Fourier tail**, not by a stable arithmetic spectral law. Moving the exponent by any fixed amount below `2` restores the generic positive tail and pushes all possible zeros out to the refinement scale.

## 8. Prime powers and limits of the result

PC-194 gives the exact prime-power dilation

\[
H_{p^k,\alpha}(x)
=
H_{p,\alpha}(p^{k-1}x),
\tag{45}
\]

so

\[
\widehat H_{p^k,\alpha}(t)
=
p^{1-k}
\widehat H_{p,\alpha}(p^{1-k}t).
\tag{46}
\]

The entire fixed-exponent conclusion transfers verbatim after this deterministic dilation. Repeated-prime depth does not create an additional zero mechanism.

The result does **not** determine the optimal transition exponent below `2`, exclude all superlinear-frequency zeros, classify every linear-scale zero of `K_alpha`, or supply a source-derived rule selecting a reciprocal exponent. It also does not constrain genuinely cross-shell, multi-carrier, angular/radial nonlocal, or nonlinear operators that are not scalar functions of a single radial cyclotomic profile.

## 9. Prior-art and novelty audit

The analytic ingredients are classical: beta/gamma evaluation of the half-line transform, the digamma series, gamma-ratio asymptotics, dominated convergence, and endpoint Fourier asymptotics by integration by parts. No novelty is claimed for those tools or for the special-function identities themselves.

A directed literature search around continuous Fourier transforms of reciprocal cyclotomic radial profiles, `Phi_p(e^{-x})` reciprocal powers, exponent-dependent positivity, and prime-shell Fourier-zero boundary layers did not locate the specific no-sublinear-zero theorem (23) or the profile transition (28)--(40). Nearby cyclotomic Fourier work is predominantly finite Fourier analysis at roots of unity rather than this continuous radial deformation. This is a bounded novelty audit, not a historical novelty claim.

The Prime-Circle-specific content is the robustness diagnosis joining PC-194 and PC-195: **the quadratic `p^(3/4)` scale is singular, while fixed exponents immediately below `2` fail only on the ordinary `Theta(p)` refinement scale**. That sharply downgrades the quantitative quadratic zero law as a candidate bridge to zeta or the critical line.

## Audit / falsification tests

The no-sublinear-zero theorem fails if either the gamma-tail coefficient (14) has the wrong sign/order or the refinement mass estimate (19) has the wrong scaling. Both follow directly from the exact decomposition (3)--(5).

The linear-profile claim fails if the dominated-convergence limit (28), the endpoint expansion (32), or the continuity argument leading to (39) fails. The result is independent of numerical root finding and makes no unproved assumption about zeta zeros.