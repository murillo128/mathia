# FD-065 — growing Schur heads improve the packet occupation bound but worsen scalar leverage

**Status:** `EXACT-DERIVED + ZERO-FRONTIER-CALIBRATED + GROWING-SCHUR-HEAD + DIRECT-TRANSFER-PACKET + NORMALIZATION-TRADEOFF + TWO-THIRDS-INVARIANCE + ROUTE-OBSTRUCTION`.

`FD-064` classifies direct short-interval packet transfer with a fixed Schur head. One possible repair is to let the head grow toward the packet host, deleting small Jordan rows whose source samples lie far beyond the transferred spike. This does make the **packet-based lower bound** for the tail occupation stronger, because the remaining denominator has a shorter power tail. It does not imply that the actual occupation ratio is monotone in the head size.

For the RH-facing scalar relaxation, however, the same maneuver is counterproductive. The Schur leverage after eliminating a head of size `D` is

\[
\Delta_{T,D}=C_T-C_D\asymp D^{-1},
\]

while the zero-frontier denominator saving is only `D^(2Theta-1)`. Their product contributes

\[
D^{-1}D^{2\Theta-1}=D^{-2(1-\Theta)},
\]

which is a genuine loss for every `Theta<1`. Quantitatively, every positive head-growth exponent adds the same penalty to both the packet obstruction of `FD-064` and the deterministic terminal-row obstruction of `FD-032`, so the `Theta=2/3` crossover survives unchanged.

## 1. Growing-head packet setup

Retain the notation and direct-transfer regime of `FD-064`. Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\qquad 0.55<\Theta<1,
\]

and choose a spike sequence

\[
A_X:=|\mathcal H(X)|=X^{\Theta+o(1)}.
\tag{1}
\]

Fix

\[
0.55<\vartheta<\Theta,
\qquad
1-\Theta<\lambda\le1-\vartheta,
\qquad
0<\kappa<\Theta+\lambda-1.
\tag{2}
\]

Let

\[
K_X=\lfloor X^\kappa\rfloor,
\qquad q=X^{\lambda+o(1)},
\qquad T=qX,
\]

with `q` in the host corridor of `FD-064`, and set

\[
x_{q,d}:=\left\lfloor\frac{T}{q+d}\right\rfloor
\qquad(1\le d\le K_X).
\tag{3}
\]

The existing transfer gives uniformly

\[
\boxed{\mathcal H(x_{q,d})=\mathcal H(X)+o(A_X).}
\tag{4}
\]

Now let the Schur head satisfy

\[
1\le D\le q/2,
\qquad
D=X^{\delta+o(1)},
\qquad
0\le\delta\le\lambda.
\tag{5}
\]

The endpoint `delta=lambda` is represented by a fixed fraction of `q`, for example `D=floor(q/2)`. Define

\[
E_{T,D}:=\sum_{r>D}\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2,
\]

\[
U_{T,D}:=\sum_{\substack{r>D\\\mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2,
\qquad
\nu_{T,D}:=\frac{U_{T,D}}{E_{T,D}}.
\tag{6}
\]

For the Schur relaxation of `FD-031`--`FD-032`, write

\[
\varepsilon_{T,D}:=\frac{\rho_{T,D}^2}{E_{T,D}},
\qquad
\mathfrak D_{T,D}:=C_T-\widehat R_{T,D}
=\Delta_{T,D}\varepsilon_{T,D},
\]

\[
\Delta_{T,D}:=C_T-C_D.
\tag{7}
\]

The distinguished equality ray vanishes on every nonsquarefree Jordan row, hence the finite-horizon support argument of `FD-032` gives, for growing `D` as well,

\[
\boxed{\varepsilon_{T,D}\ge\nu_{T,D}.}
\tag{8}
\]

## 2. Head growth saves denominator power but loses more leverage

`FD-003` gives

\[
C_N=\sum_{n\le N}\frac{\mu(n)^2}{J_2(n)},
\]

so

\[
\Delta_{T,D}=\sum_{D<n\le T}\frac{\mu(n)^2}{J_2(n)}.
\tag{9}
\]

Since `J_2(n)>=n^2/zeta(2)`, one has `Delta_(T,D)<<D^(-1)`. Conversely, restricting (9) to squarefree `D<n<=2D`, using the classical estimate

\[
\sum_{n\le x}\mu(n)^2=\frac{x}{\zeta(2)}+O(\sqrt x),
\]

and `J_2(n)<=n^2`, gives `Delta_(T,D)>>D^(-1)` whenever `D->infinity` and `2D<T`. Thus

\[
\boxed{\Delta_{T,D}=X^{-\delta+o(1)}}
\tag{10}
\]

at the power scale; for fixed or subpower `D`, this reads `Delta_(T,D)=X^{o(1)}`.

For every fixed `sigma>Theta`, `FD-046` gives `|mathcal H(n)|<<_sigma n^sigma`, hence

\[
E_{T,D}
\ll_\sigma
T^{2\sigma}\sum_{r>D}r^{-2\sigma}
\ll_\sigma T^{2\sigma}D^{1-2\sigma}.
\tag{11}
\]

Therefore, for every `eta>0`,

\[
\boxed{
E_{T,D}
\ll_\eta
X^{2\Theta(1+\lambda)+\delta(1-2\Theta)+\eta}.
}
\tag{12}
\]

Relative to a fixed head, the power-level denominator bound is better by `D^(2Theta-1)`. But multiplying an angle or occupation bound by the scalar leverage (10) changes that apparent gain into

\[
\boxed{D^{-1}D^{2\Theta-1}=D^{-2(1-\Theta)}.}
\tag{13}
\]

For every false frontier `Theta<1`, a positive power of head growth therefore worsens the scalar normalization supplied by this mechanism.

## 3. Packet obstruction: the occupation bound improves, the scalar gap worsens

Because `D<=q/2`, every packet row `q+d` lies in the physical tail. One quarter up to `O(1)` of the integers `q+d`, `1<=d<=K_X`, are divisible by `4`. Using (4) and `J_2(r)/r^2>=1/zeta(2)` gives

\[
\boxed{
U_{T,D}
\ge
\left(\frac1{4\zeta(2)}-o(1)\right)K_XA_X^2
=X^{2\Theta+\kappa+o(1)}.
}
\tag{14}
\]

Combining (12) and (14), for every `eta>0`,

\[
\boxed{
\nu_{T,D}
\gg_\eta
X^{-\{2\Theta\lambda-\kappa-\delta(2\Theta-1)\}-\eta}.
}
\tag{15}
\]

So the **packet-derived lower bound** for raw occupation becomes stronger as `delta` grows. But (8), (10), and (15) give

\[
\boxed{
\mathfrak D_{T,D}
\gg_\eta
X^{-\{2\Theta\lambda-\kappa+2\delta(1-\Theta)\}-\eta}.
}
\tag{16}
\]

Since `T=X^(1+lambda+o(1))`, the associated physical-horizon loss exponent is

\[
\boxed{
\gamma_{\rm pkt}(\Theta,\lambda,\kappa,\delta)
=
\frac{2\Theta\lambda-\kappa+2\delta(1-\Theta)}{1+\lambda}.
}
\tag{17}
\]

For fixed `Theta,lambda,kappa`, this is strictly increasing in `delta`. Thus head growth cannot strengthen the packet-based **scalar** gap; its optimum is the fixed-head value `delta=0` already present in `FD-064`.

## 4. The deterministic terminal obstruction pays the identical penalty

Independently of the packet, `FD-032` gives for every `D<T/2`

\[
\rho_{T,D}^2\gg T.
\tag{18}
\]

Using (12) and then (10), for every `eta>0`,

\[
\boxed{
\mathfrak D_{T,D}
\gg_\eta
X^{-\{(2\Theta-1)(1+\lambda)+2\delta(1-\Theta)\}-\eta}.
}
\tag{19}
\]

Its physical-horizon loss exponent is

\[
\boxed{
\gamma_{\rm term}(\Theta,\lambda,\delta)
=(2\Theta-1)
+\frac{2\delta(1-\Theta)}{1+\lambda}.
}
\tag{20}
\]

Equations (17) and (20) contain the same head-growth penalty

\[
\boxed{\frac{2\delta(1-\Theta)}{1+\lambda}.}
\tag{21}
\]

At `delta=0`, the terminal exponent returns the zero-frontier bound `2Theta-1` underlying `FD-049`. Increasing the head may improve a denominator-side view of the tail, but the scalar leverage shrinks enough to make both currently available scalar obstructions weaker.

## 5. The two-thirds crossover is invariant under head growth

At the largest direct packet allowed by `FD-064`, let `kappa` approach `Theta+lambda-1` from below. Then

\[
\boxed{
\gamma_{\rm pkt}-\gamma_{\rm term}
\longrightarrow
\frac{2-3\Theta}{1+\lambda}.
}
\tag{22}
\]

The common term (21) cancels. Hence the terminal obstruction is stronger for `Theta<2/3`, the packet obstruction is stronger for `Theta>2/3`, and they meet exactly at

\[
\boxed{\Theta=\frac23.}
\tag{23}
\]

This is the same phase boundary found in `FD-064`, now after allowing every polynomial Schur-head scale up to the packet host. Moreover, both scalar exponents are minimized at `delta=0`. **Within the direct-transfer plus generic zero-frontier denominator framework, moving the Schur cut toward the host cannot repair the normalization barrier.**

## 6. Prior-art boundary and what remains open

The load-bearing ingredients are already internal: `FD-003` supplies the exact GCD coordinate constants, `FD-031`--`FD-032` the Schur relaxation and terminal support defect, `FD-046` the zero-frontier source envelope, and `FD-064` the host/packet transfer. The squarefree counting estimate used to calibrate (10) is classical. A targeted literature audit across GCD/meet matrices, Schur complements, Farey--Franel criteria, Mertens transforms, and recent restricted-denominator Farey results located the expected classical GCD-matrix factorization/inverse literature and modern Farey variants, but no statement matching the head-growth tradeoff (13), exponents (17)/(20), or common penalty (21). No priority claim is made, and no new external theorem is load-bearing, so `SOURCES.md` does not need an update.

The boundary is narrow but useful. Equation (15) does **not** say the actual occupation ratio is monotone in `D`; it says the existing packet argument proves a stronger lower bound after the denominator tail is shortened. The result also does not rule out a new fixed-head estimate coupling `E_(T,D)` directly to the selected spike, host averaging that exploits numerator/denominator correlations, a stronger relation among Jordan rows, or source cancellation below the square-root interval scale. It rules out only the tempting normalization repair obtained by growing the Schur head while keeping the same direct-transfer and generic zero-frontier inputs.