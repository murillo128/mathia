# WI-276 — Cross-cut energy obeys a sharp nilpotent-shift reserve

## Status

- **Evidence:** `EXACT-DERIVED + CLASSICAL-OPERATOR + CROSS-CUT-BOOTSTRAP + DECISIVE-BOUNDARY + PRIOR-ART-AUDITED`.
- **Scope:** a sign-free strengthening of the first-global-crossing cut constraints in `WI-253`, `WI-269`, `WI-270`, `WI-274`, and `WI-275`. It couples *different* sharp cuts through the PSD form geometry of the first null mode, then converts compact cut support into a sharp numerical-radius bound.
- **What it does not claim:** this is not RH, does not prove that a first null mode is one-signed, does not by itself force nonzero prime overlap in the sign-changing branch, and does not yet give a numerical contradiction. The one-signed prime-overlap corollary still requires the archimedean comparison from `WI-274`.
- **Novelty boundary:** Suzuki supplies the localized Weil operator and first-crossing framework; `WI-253` supplies the exact sliding-window average; `WI-269`--`WI-275` supply the null-form, sharp-cut, and integrated-source identities. Haagerup--de la Harpe supply the sharp numerical-radius inequality for nilpotent contractions. The Mathia deduction is to identify the square-root cut-energy profile with a vector for a truncated translation and thereby obtain a new cross-cut reserve. A targeted prior-art audit found the classical operator inequality but no source applying it to the localized Weil first-crossing cut-energy profile. No priority claim is made.

## Claim

Assume RH is false. Let

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\}
\]

be Suzuki's first unrestricted localized Weil crossing, and let `v` be a normalized real attained zero mode

\[
\|v\|_2=1,\qquad A_av=0,\qquad q_a\ge0,
\tag{1}
\]

extended by zero outside `(-a,a)`. For almost every cut `t\in(-a,a)`, retain the common complementary cut energy of `WI-274`,

\[
Q_t:=q_a\!\left(v\mathbf1_{(-a,t)}\right)
=q_a\!\left(v\mathbf1_{(t,a)}\right)\ge0,
\tag{2}
\]

and extend `Q_t=0` outside `[-a,a]`. Its exact integrated source reserve is

\[
\mathcal S_v=\int_{\mathbb R}Q_t\,dt.
\tag{3}
\]

For `0<r<a`, let `\mathcal F_v(r)` be the sliding-window functional of `WI-253`. Then

\[
\boxed{
\mathcal S_v
\ge
\frac{\mathcal F_v(r)}
{1+\cos\!\left(\frac{\pi}{\lceil a/r\rceil+1}\right)}
\ge
\frac{r\lambda_r}
{1+\cos\!\left(\frac{\pi}{\lceil a/r\rceil+1}\right)}.
}
\tag{4}
\]

Consequently the whole first-crossing family obeys the sign-free reserve

\[
\boxed{
\mathcal S_v\ge
\max\!\left\{
R_{\rm harm}(a),
\sup_{0<r<a}
\frac{r\lambda_r}
{1+\cos\!\left(\frac{\pi}{\lceil a/r\rceil+1}\right)}
\right\},
}
\tag{5}
\]

where

\[
R_{\rm harm}(a)
=2\int_0^a
\frac{\lambda_r\lambda_{a-r}}
{\lambda_r+\lambda_{a-r}}\,dr
\tag{6}
\]

is the sharp mass-only reserve from `WI-275`.

The coefficient in (4) is sharp if one retains only nonnegativity of the cut-energy profile and its support in an interval of length `2a`: the compact-support correlation step below cannot be improved without further source/eigenfunction information.

## 1. Three pieces couple two different cuts

Fix `0<r<a` and put `h=2r`. For a cut location `s`, split the null mode into three consecutive pieces

\[
u_s=v\mathbf1_{(-a,s)},\qquad
w_s=v\mathbf1_{(s,s+h)},\qquad
z_s=v\mathbf1_{(s+h,a)},
\tag{7}
\]

with the obvious zero-extension interpretation when a cut lies outside `(-a,a)`. For almost every `s`, the sharp pieces are admissible by the mollification/domain argument already established in `WI-270` and used in `WI-274`.

Because `q_a\ge0` and `q_a(v)=0`, Cauchy--Schwarz for the PSD form gives

\[
q_a(v,u)=0
\tag{8}
\]

for every admissible `u`. Thus `[v]=0` in the Hilbert quotient by the null space of the form. Since `v=u_s+w_s+z_s`,

\[
[w_s]=-[u_s]-[z_s].
\tag{9}
\]

The two outer pieces have form norms

\[
\|[u_s]\|_q^2=Q_s,
\qquad
\|[z_s]\|_q^2=Q_{s+h}.
\tag{10}
\]

The ordinary and reverse triangle inequalities therefore give the exact two-cut constraint

\[
\boxed{
\left(\sqrt{Q_s}-\sqrt{Q_{s+h}}\right)^2
\le q_a(w_s)\le
\left(\sqrt{Q_s}+\sqrt{Q_{s+h}}\right)^2.
}
\tag{11}
\]

Equivalently, this is the triangle geometry of the `3\times3` compression of the PSD form to the three pieces, whose coefficient vector `(1,1,1)` lies in its kernel. Unlike the mass-only minimax in `WI-275`, (11) relates two separated cut energies through the same null vector.

## 2. Sliding-window averaging becomes an autocorrelation of `sqrt(Q)`

Let

\[
f(s):=\sqrt{Q_s}\in L^2(\mathbb R),
\qquad
\|f\|_2^2=\mathcal S_v,
\tag{12}
\]

with support contained in `[-a,a]`, and define

\[
I_h:=\int_{\mathbb R}f(s)f(s+h)\,ds.
\tag{13}
\]

Integrating (11), using translation invariance of the integral of `Q`, gives

\[
2\mathcal S_v-2I_h
\le
\int_{\mathbb R}q_a(w_s)\,ds
\le
2\mathcal S_v+2I_h.
\tag{14}
\]

The exact sliding-window computation of `WI-253`, with a window of length `h=2r`, is

\[
\int_{\mathbb R}q_a(w_s)\,ds=2\mathcal F_v(r).
\tag{15}
\]

Hence

\[
\boxed{
|\mathcal F_v(r)-\mathcal S_v|\le I_h.
}
\tag{16}
\]

This is the missing cross-cut relation: `WI-275` optimized each cut against its two masses, whereas (16) constrains the entire cut-energy profile at a nonzero translation.

## 3. Compact cut support makes the translation nilpotent

On `L^2(-a,a)`, let `T_h` be the truncated translation

\[
(T_hg)(s)=
\begin{cases}
g(s+h),&s,s+h\in(-a,a),\\0,&\text{otherwise}.
\end{cases}
\tag{17}
\]

It is a contraction. With

\[
N:=\left\lceil\frac{2a}{h}\right\rceil
=\left\lceil\frac a r\right\rceil\ge2,
\tag{18}
\]

we have `T_h^N=0`. Haagerup and de la Harpe's sharp theorem for a nilpotent contraction therefore gives

\[
w(T_h)\le c_N,
\qquad
c_N:=\cos\frac{\pi}{N+1}.
\tag{19}
\]

Since `f` is real and nonnegative,

\[
I_h=\langle f,T_hf\rangle
\le c_N\|f\|_2^2
=c_N\mathcal S_v.
\tag{20}
\]

Insert (20) into the upper side of (16):

\[
\mathcal F_v(r)
\le(1+c_N)\mathcal S_v.
\tag{21}
\]

`WI-253` independently gives

\[
\mathcal F_v(r)\ge r\lambda_r,
\tag{22}
\]

which proves (4). The other side of (16) also yields the useful squeeze

\[
(1-c_N)\mathcal S_v
\le\mathcal F_v(r)
\le(1+c_N)\mathcal S_v.
\tag{23}
\]

For example,

\[
r=a/2\quad\Longrightarrow\quad
N=2,\ c_N=1/2,
\qquad
\mathcal S_v\ge\frac{a\lambda_{a/2}}{3}.
\tag{24}
\]

The new reserve is not merely another optimization of the scalar mass split from `WI-275`: it uses the `q`-seminorm geometry of *two different cuts*. At the level of abstract monotone firstness profiles, the harmonic integral can be made arbitrarily small by concentrating the fall of `lambda_r` after a chosen radius while the corresponding single-radius quantity in (4) remains positive. Conversely, broad profiles can favor the harmonic integral. The safe combined statement is therefore the maximum in (5).

## 4. The numerical-radius coefficient is a sharp support-only boundary

The constant `c_N` in (20) remains sharp even after restricting to nonnegative real functions. Because `N=ceil(2a/h)`,

\[
2a>(N-1)h.
\tag{25}
\]

Choose a sufficiently short measurable interval `E` so that

\[
E,E+h,\ldots,E+(N-1)h
\tag{26}
\]

are disjoint and all lie in `(-a,a)`. Put

\[
f=\sum_{k=0}^{N-1}b_k\mathbf1_{E+kh},
\qquad
b_k=\sin\frac{(k+1)\pi}{N+1}>0.
\tag{27}
\]

Then

\[
\frac{\langle f,T_hf\rangle}{\|f\|_2^2}
=
\frac{\sum_{k=0}^{N-2}b_kb_{k+1}}
{\sum_{k=0}^{N-1}b_k^2}
=
\cos\frac{\pi}{N+1}.
\tag{28}
\]

Thus support length plus `Q\ge0` alone cannot replace `c_N` by a smaller uniform constant. Any improvement after (20) must exploit information absent from this relaxation: the exact Weil-source representation of `Q_t`, regularity/shape restrictions on an actual first eigenfunction, or simultaneous constraints at several shifts.

This is also a useful no-go result for the next search stage. Merely proving a generic decorrelation inequality for arbitrary nonnegative `Q` supported in `[-a,a]` cannot beat (19)--(20).

## 5. Relation to the active defect-to-zero program

The mechanism is sign-free through (5). It therefore advances the active first-global-crossing route without assuming a positive ground state, which the nonlocal Weil form does not currently provide.

On the one-signed branch, `WI-274` gives the exact archimedean budget

\[
K_+=\int_0^{\log\rho}h\,w(h)\,dh,
\qquad \rho^3-\rho-1=0,
\tag{29}
\]

and hence the prime overlap satisfies

\[
\mathcal P_v\ge\mathcal S_v-K_+.
\tag{30}
\]

Combining with (5) strengthens the sufficient spectral test for nonzero active-prime overlap to

\[
\max\!\left\{
R_{\rm harm}(a),
\sup_{0<r<a}
\frac{r\lambda_r}
{1+\cos\!\left(\frac{\pi}{\lceil a/r\rceil+1}\right)}
\right\}>K_+.
\tag{31}
\]

No corresponding prime-overlap conclusion is asserted for a sign-changing null mode: cancellation in the source remains a live obstruction. The immediate next gate is quantitative. Either certified information on the interior profile `lambda_r` makes the maximum in (31) cross the relevant source budget, or one must go beyond the sharp support-only bound by exploiting the actual source shape of `Q_t` and/or several translations simultaneously.

## Prior art and provenance

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), supplies the localized closed Weil form/operator and the compact-support spectral framework: https://arxiv.org/abs/2606.09096.
- `WI-253` proves the exact translated-window average `int q(window)=2 F_v(r)` and `F_v(r)>=r lambda_r` at the first unrestricted crossing.
- `WI-269` supplies the PSD signed-source Laplacian/null-form identity; `WI-270` supplies the sharp-cut form-domain justification; `WI-274` identifies `int Q_t dt=S_v`; `WI-275` gives the sharp mass-only harmonic reserve.
- Uffe Haagerup and Pierre de la Harpe, **The numerical radius of a nilpotent operator on a Hilbert space**, *Proceedings of the American Mathematical Society* **115** (1992), no. 2, 371--379, DOI `10.1090/S0002-9939-1992-1072339-6`, proves `w(T)<=||T|| cos(pi/(N+1))` for `T^N=0`, with sharp constant.
- A targeted audit across Suzuki/localized-Weil work, the current `weil_inertia` findings, and the nilpotent numerical-radius literature found the operator theorem itself but no prior application yielding (4)--(5). This is recorded only as a novelty audit, not as a priority claim.
