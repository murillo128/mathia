# PL-432 — Abel transport replaces the dyadic quarter-turn coefficient-mass bottleneck by ordinary short-interval norms

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-ABEL-SUMMATION + QUANTITATIVE-ROUTE-REFINEMENT`.

**Parent findings:** `PL-423`, `PL-428`, `PL-429`, `PL-430`, `PL-431`.

## Claim

`PL-431` shows that, for a source supported in one fixed multiplicative band, the missing imaginary character coherence can be read from one shrinking vertical displacement

\[
t_X=-\frac{\pi}{2\log X},
\]

but its deterministic error was bounded by the coefficient mass `B_X/log X`. That `ell^1` bound is unnecessarily crude for the actual short-interval source. Abel--Stieltjes summation gives a cancellation-preserving transport estimate in physical `y`-space.

Let `X>=2`, `0<h<=X`, and let `mu,nu` be finite complex measures on `[X,3X]`. For `y in [X,2X]` and `0<=r<=h`, put

\[
U(y,r):=\mu((y,y+r]),
\qquad
V(y,r):=\nu((y,y+r]),
\]

and

\[
J_\mu(X,r):=\int_X^{2X}|U(y,r)|^2\,dy,
\qquad
J_\nu(X,r):=\int_X^{2X}|V(y,r)|^2\,dy.
\tag{1}
\]

Define the vertically twisted second source and its cross response by

\[
V_t(y,h):=\int_{(y,y+h]}u^{-it}\,d\nu(u),
\]

\[
C_{\mu,\nu}(t)
:=\int_X^{2X}U(y,h)\overline{V_t(y,h)}\,dy.
\tag{2}
\]

Then Abel--Stieltjes summation yields the exact identity

\[
V_t(y,h)
=(y+h)^{-it}V(y,h)
+it\int_0^h V(y,r)(y+r)^{-it-1}\,dr.
\tag{3}
\]

Consequently

\[
\left\|
V_t(\cdot,h)-(\cdot+h)^{-it}V(\cdot,h)
\right\|_{L^2([X,2X])}
\le
\frac{|t|}{X}
\int_0^h J_\nu(X,r)^{1/2}\,dr.
\tag{4}
\]

At the quarter-turn displacement `t=t_X`, since `X<=y+h<=3X`, one obtains

\[
\boxed{
\begin{aligned}
|C_{\mu,\nu}(t_X)+iC_{\mu,\nu}(0)|
\le{}&
\frac{\pi\log3}{2\log X}
\sqrt{J_\mu(X,h)J_\nu(X,h)}\\
&+
\frac{\pi}{2X\log X}
J_\mu(X,h)^{1/2}
\int_0^h J_\nu(X,r)^{1/2}\,dr.
\end{aligned}}
\tag{5}
\]

Thus, if the scalar observable is

\[
R_{\mu,\nu}(t):=2\Re C_{\mu,\nu}(t),
\]

then

\[
\boxed{
\left|
\frac12R_{\mu,\nu}(t_X)-\Im C_{\mu,\nu}(0)
\right|
\le \text{right-hand side of (5)}.
}
\tag{6}
\]

The important change from `PL-431` is not the `1/log X` carrier error; that was already known. It is the norm controlling the phase-transport remainder. The global coefficient mass `B_X=sum|beta_n|` disappears and is replaced by the integrated family of **ordinary, unshifted short-interval `L^2` norms** in (1). These are exactly Selberg-integral-type quantities and preserve the cancellation of the arithmetic source.

This does **not** determine the oriented sample `R(t_X)` from same-shift variance data. `PL-428` forbids that. It only removes the artificial `ell^1` conditioning bottleneck from the deterministic quarter-turn step and recasts that part of the problem in the natural short-interval norm geometry.

## 1. Exact Abel transport

Fix `y`. Let

\[
F_y(r)=\nu((y,y+r]),
\qquad 0\le r\le h.
\]

For the smooth weight `f(u)=u^{-it}`, Stieltjes integration by parts gives

\[
\int_{(y,y+h]}f(u)\,d\nu(u)
=f(y+h)F_y(h)-\int_0^hF_y(r)f'(y+r)\,dr.
\]

Since

\[
f'(u)=-it\,u^{-it-1},
\]

this is exactly (3). No Dirichlet-series continuation, Euler product, or asymptotic prime statement is involved.

Subtract the first term in (3), take `L^2([X,2X])`, and use Minkowski's integral inequality. Because `y+r>=X`,

\[
\begin{aligned}
\|V_t-(\cdot+h)^{-it}V\|_2
&\le
|t|\int_0^h
\left(
\int_X^{2X}\frac{|V(y,r)|^2}{(y+r)^2}\,dy
\right)^{1/2}dr\\
&\le
\frac{|t|}{X}
\int_0^h J_\nu(X,r)^{1/2}\,dr,
\end{aligned}
\]

which proves (4).

Pairing against `U(\cdot,h)` and applying Cauchy--Schwarz gives

\[
\left|
C_{\mu,\nu}(t)
-
\int_X^{2X}(y+h)^{it}
U(y,h)\overline{V(y,h)}\,dy
\right|
\le
J_\mu(X,h)^{1/2}
\frac{|t|}{X}
\int_0^hJ_\nu(X,r)^{1/2}\,dr.
\tag{7}
\]

This is the cancellation-preserving replacement for the coefficientwise triangle inequality used in `PL-431`.

## 2. Quarter-turn specialization

For

\[
t_X=-\frac{\pi}{2\log X},
\]

write

\[
(y+h)^{it_X}
=-i\exp\left(
-\frac{i\pi}{2\log X}
\log\frac{y+h}{X}
\right).
\tag{8}
\]

Since `1<=(y+h)/X<=3`, the elementary inequality `|e^{iv}-1|<=|v|` gives

\[
\sup_{X\le y\le2X}
|(y+h)^{it_X}+i|
\le
\frac{\pi\log3}{2\log X}.
\tag{9}
\]

Therefore

\[
\left|
\int_X^{2X}
\bigl((y+h)^{it_X}+i\bigr)
U(y,h)\overline{V(y,h)}\,dy
\right|
\le
\frac{\pi\log3}{2\log X}
\sqrt{J_\mu(X,h)J_\nu(X,h)}.
\tag{10}
\]

Combining (7)--(10), with `|t_X|=pi/(2 log X)`, proves (5). Taking real parts and using `Re(-iz)=Im z` proves (6).

The asymmetry between `mu` and `nu` in the second term is only because the vertical twist was placed on the second source. Twisting the first source instead gives the symmetric companion bound with the roles reversed. One may use the better of the two when both realizations of the scalar response are available.

## 3. Natural variance scale

Suppose, illustratively, that throughout `0<r<=h` the second source obeys a Selberg-type bound

\[
J_\nu(X,r)\le A_\nu XrL_X,
\tag{11}
\]

and that

\[
J_\mu(X,h)\le A_\mu XhL_X
\tag{12}
\]

for some slowly varying scale `L_X`. Then

\[
\int_0^hJ_\nu(X,r)^{1/2}\,dr
\le
\frac23A_\nu^{1/2}X^{1/2}L_X^{1/2}h^{3/2},
\]

so the Abel remainder in (5) is at most

\[
\frac{\pi}{3}
(A_\mu A_\nu)^{1/2}
\frac{h^2L_X}{\log X}.
\tag{13}
\]

On the natural end-scale `XhL_X`, this is smaller by

\[
O\left(\frac{h}{X\log X}\right),
\]

while the carrier-variation term is `O(1/log X)` times the geometric mean of the two end-scale norms.

Equation (13) is not being asserted as an unconditional prime theorem for every short range. Its role is to show that the phase transport itself is compatible with the natural second-moment scale once ordinary multiscale Selberg bounds are available. The `ell^1` mass appearing in `PL-431` is therefore not an intrinsic obstruction of the quarter-turn geometry.

## 4. Exact compatibility with deterministic principal-channel subtraction

The measure formulation is useful because it handles the load-bearing centering distinction of `PL-423` without approximation.

For a nonprincipal character `chi (mod 5)`, take, up to the unitary character normalization,

\[
d\nu_\chi(u)
=\sum_n\Lambda(n)\overline{\chi(n)}\,\delta_n(du).
\tag{14}
\]

For the principal character, deterministic subtraction of the PNT main term is represented by the signed measure

\[
d\nu_{\chi_0}(u)
=\sum_{5\nmid n}\Lambda(n)\,\delta_n(du)-du,
\tag{15}
\]

again up to the same fixed normalization. Then

\[
\nu_{\chi_0}((y,y+h])
=
\sum_{\substack{y<n\le y+h\\5\nmid n}}\Lambda(n)-h,
\tag{16}
\]

which is precisely the surviving principal fluctuation channel isolated in `PL-423`.

Under vertical translation the coherent centered source is

\[
\int_{(y,y+h]}u^{-it}\,d\nu_{\chi_0}(u)
=
\sum_{\substack{y<n\le y+h\\5\nmid n}}
\Lambda(n)n^{-it}
-
\int_y^{y+h}u^{-it}\,du.
\tag{17}
\]

Thus the deterministic center rotates together with the prime source. Equation (3) applies to the **entire signed source**, including the continuous subtraction. This resolves the bookkeeping warning in `PL-431`: no spurious oriented component is generated by freezing the center.

## 5. Prior-art and novelty audit

The mechanism in (3) is classical Abel/partial summation. No novelty is claimed for it. A close modern number-theoretic use is Alexander P. Mangerel, “Divisor-bounded multiplicative functions in short intervals,” *Research in the Mathematical Sciences* **10** (2023), Article 12, DOI `10.1007/s40687-023-00376-0`: Corollary 3.9 uses partial summation to compare a sum weighted by `n^{-it_0}` with the corresponding ordinary partial sums. The same elementary transport principle underlies (3), although the present quantity is a moving short-interval `L^2` cross response rather than Mangerel's long partial sum.

Weighted Selberg integrals and mean squares of weighted short-interval arithmetic sums are also established machinery; see Giovanni Coppola, “Generations of Correlation Averages,” *Journal of Numbers* (2014), Article 140840, DOI `10.1155/2014/140840`, and Giovanni Coppola--Maurizio Laporta, “Symmetry and short interval mean-squares,” arXiv `1312.5701`. These sources are prior-art guardrails for the `L^2` bookkeeping, not sources for an RH implication.

Targeted searches for combinations of `n^{it}`/`n^{-it}`, Abel or partial summation, twisted/weighted Selberg integrals, and prime short-interval variance did not locate the exact line-specific estimate (5), namely the use of multiscale unshifted short-interval norms to condition the `PL-431` shrinking quarter-turn reconstruction. This is an absence-of-located-prior-art statement only. The durable contribution is the **route refinement**: replacing a coefficientwise `ell^1` error by a source-native `L^2` transport error.

## 6. Adversarial audit

1. **This does not recover the blind coherence from same-shift variances.** `PL-428` remains untouched. Equation (5) relates the genuinely oriented sample at `t_X` to the complex unshifted covariance; it does not manufacture `R(t_X)` from `R(0)`.

2. **The analytic theorem at `t_X` is still required.** `PL-431` reduced the aperture to two samples. The present finding improves the deterministic conditioning of that reduction, but an arithmetic theorem or other non-circular control of the shifted scalar observable is still needed.

3. **The coefficient-mass bottleneck is replaced, not erased.** The new requirement is the integrated multiscale quantity `int_0^h J_nu(X,r)^(1/2) dr`. If short-scale norms are anomalously large, (5) may still be too weak. The gain is that this requirement preserves arithmetic cancellation and belongs to the ordinary Selberg-integral geometry.

4. **The principal center must move with the twist.** Formula (17), not a prime sum minus the frozen constant `h`, is the correct vertically shifted principal source. Freezing the center would invalidate the exact Abel transport and can create a false imaginary signal.

5. **The `log 3` constant uses the actual dyadic support.** It comes from `y in [X,2X]` and `h<=X`. Other multiplicative windows change only this carrier-width constant; broad support down to fixed integers returns to the `PL-430` finite-aperture problem.

6. **No critical-strip identity is used.** Everything here is a finite-measure identity on the prime/source side. Its relevance to RH remains conditional on the earlier source-to-zero/positivity program and supplies no analytic continuation by itself.

7. **Second-moment scale is not the PL-421 floor.** Even an optimal bound in (5) does not prove `lambda_min>=1/4`. The diagonal channel sizes, mixed covariances, source-model replacement error, and margin required by `PL-421` remain separate obligations.

## Consequence for the line

The warning at the end of `PL-431` can now be sharpened. The quantity

\[
\frac{B_X}{\log X}
\]

is not an intrinsic conditioning parameter for the short-prime quarter-turn. After Abel transport, the deterministic deformation cost is controlled by ordinary unshifted short-interval norms through (5).

Accordingly the next arithmetic target should not be “prove an `ell^1` coefficient-mass bound strong enough for the quarter turn.” It is narrower and more natural:

\[
\boxed{
\begin{gathered}
\text{control the oriented scalar response at }
 t_X=-\pi/(2\log X),\\
\text{while controlling the ordinary multiscale diagonal Selberg norms}
\quad J_\chi(X,r),\ 0<r\le h,
\end{gathered}}
\]

with errors below the `PL-421` spectral margin. The first requirement still contains the missing arithmetic orientation; the second now conditions the representation step without discarding cancellation.
