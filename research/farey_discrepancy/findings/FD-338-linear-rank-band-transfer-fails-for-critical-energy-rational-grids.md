# FD-338 — Linear rank-band transfer fails for critical-energy rational grids

**Status:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + GENERIC-GEOMETRY-BOUNDARY.

FD-337 transfers genuine Farey rank-sine shares to position-Fourier shares for `q=o(Q)`, using a deterministic estimate with small parameter `q Delta`. That restriction cannot be removed using only monotonicity, reflection, `N asymp Q^2`, and `Delta=O(1/Q)`, even if one additionally grants the critical quadratic energy `E=Theta(1/Q)` and uniformly comparable neighboring gaps. An explicit rational grid has a strictly positive limiting difference between the two normalized shares at `q=floor(Q/16)`.

This is an obstruction to a **generic extension of the transfer lemma**, not a counterexample to a statement about genuine Farey fractions. It supplies no new bound for their discrepancy or Mertens coefficients.

## 1. Rational control and the two spectra

Let `Q>=8` tend to infinity through even integers, `N=Q^2`, and
\[
\phi(u)=\max(0,1-|u-1|),\qquad c=\tfrac12.
\]
For `0<=k<=N`, put
\[
t_k=k/N,\quad
D_k=\frac cQ\{\phi(Qt_k)-\phi(Q(1-t_k))\},
\qquad x_k=t_k+D_k.
\tag{1}
\]
The two supports are disjoint. The interpolating map is piecewise affine with slopes `1-c`, `1`, or `1+c`. Hence this is a strictly increasing rational grid with
\[
x_0=0,\quad x_N=1,\quad x_{N-k}=1-x_k,\qquad
\frac1{2N}\le x_k-x_{k-1}\le\frac3{2N}.
\tag{2}
\]
Every point has denominator dividing `2Q^2`; no denominator bound `Q` is asserted. Direct summation gives
\[
\Delta:=\max_k|D_k|=\frac1{2Q},\qquad
E:=\sum_{k=1}^{N-1}D_k^2
=\frac1{3Q}+\frac1{6Q^3}.
\tag{3}
\]
Indeed the first triangle has values `c min(k,2Q-k)/Q^2`, `1<=k<2Q`; reflect its square sum and use the elementary sum of squares.

Use exactly the generic coefficients of FD-337:
\[
d_{2j}=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(2\pi jt_k),\qquad
C_j=\sum_{k=1}^N\cos(2\pi jx_k),\qquad
a_j=-\frac{C_j}{\pi j\sqrt{2N}},
\tag{4}
\]
\[
E_q=\sum_{j=1}^q d_{2j}^2,\quad
T_q=\sum_{j=1}^q a_j^2,\quad
T_\infty=\sum_{j\ge1}a_j^2.
\]
Reflection kills the odd rank sine modes and makes the exponential position sums real. In particular, both shares below have their full-spectrum normalization:
\[
\sum_{j=1}^{N/2-1}d_{2j}^2=E,\qquad
T_\infty=E+\frac1{12N}.
\tag{5}
\]
The second identity is not restricted to Farey grids. To check the endpoint convention directly, write `B_2(u)=u^2-u+1/6`. Its Fourier series gives
\[
T_\infty=\frac1{2N}\sum_{k,l=1}^N B_2(\{x_k-x_l\}).
\]
Reflection implies `sum_(k=1)^N x_k=(N+1)/2`. Expanding the polynomial, using the order of the `x_k`, gives the double sum `2NE+1/6`, proving (5). This also proves convergence of the series. The same total-energy identity used in FD-002 and FD-337 therefore survives in the control; only its band allocation fails to transfer.

## 2. Limiting coefficient profiles at the linear cutoff

For `lambda>=0` define the continuous functions, with value zero at zero,
\[
\begin{aligned}
F(\lambda)&=2\sqrt2 c\int_0^2\phi(u)\sin(2\pi\lambda u)\,du,\\
G(\lambda)&=\frac{\sqrt2}{\pi\lambda}\int_0^2
 \{\cos(2\pi\lambda u)-\cos(2\pi\lambda(u+c\phi(u)))\}\,du.
\end{aligned}
\tag{6}
\]
For every fixed `rho>0`, uniformly for integers `1<=j<=rho Q`,
\[
Qd_{2j}=F(j/Q)+O_\rho(Q^{-1}),\qquad
Qa_j=G(j/Q)+O_\rho(Q^{-1}).
\tag{7}
\]
For sufficiently large `Q` all these `j` are below `N/2`. Reflection gives the exact localized rank sum
\[
Qd_{2j}=\frac{2\sqrt2 c}{Q}
\sum_{k=1}^{2Q-1}\phi(k/Q)\sin(2\pi(j/Q)(k/Q)).
\]
For the position sum, subtract the vanishing uniform-grid cosine sum before localizing. The two ends contribute equally, so
\[
Qa_j=\frac{\sqrt2}{\pi\lambda Q}
\sum_{k=1}^{2Q-1}
\{\cos(2\pi\lambda k/Q)
-\cos(2\pi\lambda(k/Q+c\phi(k/Q)))\},\qquad\lambda=j/Q.
\tag{8}
\]
These are Riemann sums for (6). Uniformity down to `lambda=1/Q` follows by removing the apparent singularity *before* estimating the sum:
\[
\frac{\cos(2\pi\lambda u)-\cos(2\pi\lambda(u+c\phi(u)))}{\lambda}
=2\pi\int_0^{c\phi(u)}\sin(2\pi\lambda(u+v))\,dv.
\tag{9}
\]
On each affine piece the integrands and their `u` derivatives are bounded uniformly for `0<=lambda<=rho`. Thus their Riemann errors are `O_rho(1/Q)`, including the continuous value at zero.

With `q=floor(rho Q)`, (3), (5), and (7) yield
\[
\boxed{
\frac{E_q}{E}\longrightarrow3\int_0^\rho F(\lambda)^2d\lambda,
\qquad
\frac{T_q}{T_\infty}\longrightarrow3\int_0^\rho G(\lambda)^2d\lambda.}
\tag{10}
\]
For example, the uniform `O(1/Q)` errors in (7) contribute `o(1)` to `Q E_q` and `Q T_q`; this explicitly justifies the growing-cutoff passage. The correction `1/(12N)` in (5) is negligible relative to (3).

## 3. A strictly separated pair of shares

Fix `rho=1/16`. From (9),
\[
\begin{aligned}
F(\lambda)&=2\sqrt2\int_0^2\int_0^{c\phi(u)}
 \sin(2\pi\lambda u)\,dv\,du,\\
G(\lambda)-F(\lambda)&=2\sqrt2\int_0^2\int_0^{c\phi(u)}
 \{\sin(2\pi\lambda(u+v))-\sin(2\pi\lambda u)\}\,dv\,du.
\end{aligned}
\tag{11}
\]
Here `0<=u+v<=u+c phi(u)<=2`. For `0<lambda<=rho`, all angles lie in `[0,pi/4]`, where sine is strictly increasing. Thus `G>F>0` throughout the open band, and
\[
\boxed{
\lim_{Q\to\infty}\left(\frac{T_{\lfloor Q/16\rfloor}}{T_\infty}
-\frac{E_{\lfloor Q/16\rfloor}}E\right)
=L:=3\int_0^{1/16}(G^2-F^2)\,d\lambda>0.}
\tag{12}
\]
There is also an elementary explicit lower bound. Use `sin z>=2z/pi` on `[0,pi/2]`, `cos z>=1/sqrt2` on `[0,pi/4]`, and
`int_0^2 u phi(u)du=1`, `int_0^2 phi(u)^2du=2/3`. Equation (11), retaining `c=1/2`, gives
\[
F(\lambda)\ge8\sqrt2 c\lambda,
\qquad G(\lambda)-F(\lambda)\ge\frac{4\pi c^2}3\lambda.
\]
Consequently
\[
L\ge\frac{\sqrt2\pi}{1536}>0.00289.
\tag{13}
\]
This is a proved lower bound, not a numerical certificate. For a convenient check, with `z=2 pi lambda`, direct integration of (6) gives
\[
F=\frac{\sqrt2(2\sin z-\sin2z)}{z^2},\qquad
G=\frac{2\sqrt2((4/3)\sin(3z/2)-\sin2z)}{z^2}.
\tag{14}
\]
At zero both expressions are interpreted continuously. Numerical integration gives `L approximately 0.00635814`; only (12)–(13) are needed for the obstruction.

## 4. Verification, prior art, and precise boundary

A standard-library Python audit built (1) using exact rational arithmetic at every even `8<=Q<=64`: all 29 grids passed strict ordering, reflection, the exact supremum and energy in (3), and the minimum gap in (2). A separate exact double Bernoulli-kernel calculation at `Q=8,10,12` verified (5). At `Q=16,32,64`, direct full-grid cosine and sine transforms agreed with the localized sums for every `1<=j<=Q/4`, with maximum absolute discrepancy below `6.9e-13`. Floating-point evaluations of the two shares at `Q=32,64,128,256,512,1024` approached (10); a 20,000-cell midpoint integration of (14) gave limiting shares about `0.01840651` and `0.02476465`. These computations test signs, constants, endpoint handling, and the distinct normalizations. The proof of the nonzero limit is (6)–(13), not finite extrapolation. No genuine-Farey confirmation panel was inspected or tuned.

The underlying phenomenon—small spatial deformations affecting sufficiently high Fourier frequencies—is classical. Stéphane Mallat, *Group Invariant Scattering*, Communications on Pure and Applied Mathematics **65**(10) (2012), 1331–1398, [DOI 10.1002/cpa.21413](https://doi.org/10.1002/cpa.21413), Section 2.1, gives a neighboring Fourier-instability example; the [author-hosted published paper](https://www.di.ens.fr/~mallat/College/CPAM-Mallat-Scat.pdf) distinguishes that phenomenon from stable wavelet representations. Its deformation norm and observable differ from the two grid spectra here; no scattering theorem is applied. The Bernoulli/Fourier total-energy identity is also classical. M. N. Huxley's *Identities involving Farey fractions*, Proc. Steklov Inst. Math. **276** (2012), 125–139, [primary record](https://www.mathnet.ru/eng/tm3374), is the neighboring weighted discrete/continuous Franel-identity literature, not a source of bandwise equality. No new general Fourier-instability principle or literature priority is claimed.

The line-local mathematical delta is the explicit failure of **normalized band-energy transfer at critical Franel energy**, despite exact total-energy agreement, reflection, the Dress-size displacement bound, and uniformly positive comparable gaps. Merely adding `E=O(1/Q)` to the geometric hypotheses cannot improve the `q=o(Q)` guarantee of FD-337 to all `q=Theta(Q)`.

These rational controls preserve every hypothesis of that generic proposed implication. They do **not** preserve genuine Farey fractions, the denominator-edge inventory, Ramanujan sums, or the first empty Farey interval of length `1/Q`. Here `Q` indexes the geometric scale, not a bound on reduced denominators. Therefore the counterexample must not be used to refute an arithmetic-specific linear-band transfer, a denominator-conditioned null, or an RH-scale estimate for the genuine sequence. It also does not claim every linear cutoff fails or the constant `8 pi/3` in FD-337 is optimal. The fixed positive value `q Delta ->1/32` suffices to defeat a uniform vanishing-error conclusion from the listed data alone. An actual-Farey extension requires an additional input absent from this geometric argument.
