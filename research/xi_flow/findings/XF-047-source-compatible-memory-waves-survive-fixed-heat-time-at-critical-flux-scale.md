# XF-047 — source-compatible memory waves survive fixed heat time at the critical flux scale

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `NONLINEAR-OBSTRUCTION` + `SOURCE-COMPATIBLE/THRESHOLD`. XF-044 showed that the arithmetic-lattice memory mode has only an order-one Cauchy decay rate on fixed heat time, but that statement was a tangent obstruction and did not check whether the slow mode could simultaneously pass the source-counting tolerances used elsewhere in the line. XF-046 then removed the genuinely remote tail at the required little-`o(R^{-2})` scale, leaving the near buffer as the explicit source-facing burden.

There is a matched control that survives both tests. At height `T`, use the **corrected smooth source spacing**

\[
\sigma_T:=\frac1{\Psi'(T)}
=\frac{4\pi}{\log(T/4\pi)}
=\frac{4\pi}{\log T}\left(1+O\!\left(\frac1{\log T}\right)\right),
\tag{1}
\]

where `Psi` is the Rodgers--Tao/Riemann--von Mangoldt main term already used in XF-046. Let

\[
q=q_T\sim \log^2T,
\qquad
R:=q,
\qquad
M:=Rq=q^2,
\qquad
\varepsilon:=\frac{\kappa}{q^2},
\qquad \kappa>0\ \text{fixed},
\tag{2}
\]

and initialize the exact `q`-periodic logarithmic zero-motion control of XF-041 by

\[
\boxed{
 g_j(0)=\sigma_T
 \left(1+\varepsilon\cos\frac{2\pi j}{q}\right),
 \qquad j\in\mathbb Z.
}
\tag{3}
\]

Then for every fixed heat-time horizon `tau>0` contained in the real-simple regime, the exact nonlinear periodic trajectory has all of the following properties uniformly for `0<=t<=tau`:

1. every gap remains in `sigma_T(1+-varepsilon)`, the period mean remains exactly `sigma_T`, and every translated finite span differs from the corresponding local source lattice by at most `q sigma_T epsilon=O(log^{-3}T)`;
2. the periodized conductance network remains a `1+O(epsilon)` multiplicative perturbation of the arithmetic Cauchy network;
3. the first memory Fourier mode survives with

\[
\boxed{
\left|
\sum_{j=0}^{q-1}
\left(\frac{g_j(t)}{\sigma_T}-1\right)
 e^{-2\pi i j/q}
\right|
=
\frac{q\varepsilon}{2}
 e^{-\rho_qt}
\bigl(1+o(1)\bigr),
}
\tag{4}
\]

where

\[
\rho_q=
\frac{4\pi^2(q-1)}{q^2\sigma_T^2}
=\frac14+o(1);
\tag{5}
\]

4. if `V_M(t)` is the XF-035/XF-044 total variation of the normalized-triple flux over `2M` consecutive gaps, then

\[
\boxed{
\liminf_{T\to\infty}
\inf_{0\le t\le\tau}
M V_M(t)
\ge
6\pi^2\kappa e^{-\tau/4}>0.
}
\tag{6}
\]

Thus the positive stability gate `M V_M=o(1)` is **not forced** by fixed-time universal Cauchy smoothing plus the source-counting precision presently used in the line. The obstruction can be made far smaller than the allowed zero-counting error, can remain uniformly Cauchy-rigid, and can nevertheless sit exactly at the critical `R^{-2}` memory amplitude for an entire fixed heat-time interval.

This does not assert that Xi realizes (3). The construction is a `q`-periodic matched logarithmic-particle control, not a global Xi zero set or a new lower bound for `Lambda`. Its force is falsificatory: any positive argument that rules out the remaining near-buffer mode must use information that distinguishes the actual Xi source from a locally source-compatible memory wave. Counting main terms, gap envelopes, Cauchy rigidity, and the universal nonlinear repulsion dynamics do not supply that distinction by themselves.

## 1. The periodic control passes the source span tests by a wide margin

Write

\[
u_j(t):=\frac{g_j(t)}{\sigma_T}-1.
\tag{7}
\]

XF-041 proves for the exact periodic quotient that the period mean is conserved, the maximum gap is nonincreasing, and the minimum gap is nondecreasing. Hence (3) gives for all `t>=0` in the real-simple interval

\[
\boxed{
\sum_{j=0}^{q-1}u_j(t)=0,
\qquad
|u_j(t)|\le\varepsilon.
}
\tag{8}
\]

Every `q` consecutive gaps therefore have total span exactly `q sigma_T`. Split any translated interval of `L` gaps into complete periods and a remainder of fewer than `q` gaps. Equation (8) gives the deterministic bound

\[
\boxed{
\left|
\sum_{j=a}^{a+L-1}g_j(t)-L\sigma_T
\right|
\le q\sigma_T\varepsilon.
}
\tag{9}
\]

With the scales (1)--(2),

\[
q\sigma_T\varepsilon
=O\!\left(\frac1{\log^3T}\right).
\tag{10}
\]

For `L<=log^2T`, replacing `sigma_T` by the coarser source spacing `4pi/log T` costs only

\[
L\left|
\sigma_T-\frac{4\pi}{\log T}
\right|=O(1),
\tag{11}
\]

which is still `o(log T)`. Thus the Rodgers--Tao memory-span tolerance used in XF-046 cannot see this mode. Notice that this remains true after the nonlinear evolution: no Fourier approximation is needed for (9), only the exact period mean and maximum principle.

The larger `2M`-gap buffer has physical width

\[
2M\sigma_T
\asymp \log^3T=o(T).
\tag{12}
\]

Using the corrected spacing in (1) is important here. Taylor expansion of the smooth counting main term gives, for `|x|=O(log^3T)`,

\[
\Psi(T+x)-\Psi(T)
=\frac{x}{\sigma_T}
+O\!\left(\frac{x^2}{T}\right)
=\frac{x}{\sigma_T}+o(1).
\tag{13}
\]

Meanwhile (9) says that every root position in the periodic block differs from its local arithmetic reference by at most `q sigma_T epsilon=O(log^{-3}T)`. In index units this is `O(q epsilon)=O(log^{-2}T)`. Therefore the finite buffer can be placed inside the smooth source count with discrepancy `O(1)`, far below the global `O(log^2T)` allowance used by XF-020/XF-046.

This is a finite-window compatibility statement, not a claim that the infinite constant-density periodic continuation itself has the global Xi counting function. As in XF-039, the matched control shows that the source constraints actually consumed by the local argument do not exclude the displayed block geometry.

## 2. Uniform gap closeness makes the nonlinear conductance a small operator perturbation

Let `C_ij(t)` be the exact periodized conductance from XF-041, and let `C_ij^*` be its arithmetic-lattice value at constant spacing `sigma_T`:

\[
C_{ij}^*
=\frac{\pi^2}{q^2\sigma_T^2}
\csc^2\!\left(\frac{\pi(i-j)}q\right),
\qquad i\ne j.
\tag{14}
\]

Every root distance spanning `r` gaps is, by (8), between

\[
(1-\varepsilon)|r|\sigma_T
\quad\text{and}\quad
(1+\varepsilon)|r|\sigma_T.
\tag{15}
\]

The two denominator factors in each unperiodized conductance span the same number of gaps. Term by term in the periodization, (15) therefore gives

\[
\boxed{
(1+\varepsilon)^{-2}C_{ij}^*
\le C_{ij}(t)
\le(1-\varepsilon)^{-2}C_{ij}^*.
}
\tag{16}
\]

Let `L(t)` and `L_*` be the symmetric graph Laplacians with weights `C_ij(t)` and `C_ij^*`. From (16), in quadratic-form order,

\[
-\delta_TL_*
\preceq L(t)-L_*
\preceq\delta_TL_*,
\qquad
\delta_T=O(\varepsilon).
\tag{17}
\]

The exact spectrum from XF-041 is

\[
\lambda_\ell(L_*)
=
\frac{2\pi^2}{q^2\sigma_T^2}
\ell(q-\ell),
\qquad
0\le\ell<q,
\tag{18}
\]

so

\[
\|L_*\|_{2\to2}
\le\frac{\pi^2}{2\sigma_T^2}.
\tag{19}
\]

Consequently

\[
\boxed{
\|L(t)-L_*\|_{2\to2}
\ll\frac{\varepsilon}{\sigma_T^2}.
}
\tag{20}
\]

This is stronger than merely invoking the XF-038 Cauchy-rigidity conclusion: the whole periodized conductance operator remains multiplicatively close to its arithmetic value for the entire fixed-time trajectory.

## 3. Duhamel makes the slow-mode persistence nonlinear and uniform

Since the period mean is fixed, (8) and the exact periodic gap equation give

\[
\boxed{
u'(t)=-2L(t)u(t).}
\tag{21}
\]

The symmetric positive conductances imply

\[
\frac{d}{dt}\frac12\|u(t)\|_2^2
=-2\langle u(t),L(t)u(t)\rangle\le0,
\tag{22}
\]

so `||u(t)||_2<=||u(0)||_2`. Let

\[
v(t):=e^{-2L_*t}u(0).
\tag{23}
\]

Duhamel, semigroup contraction, (20), and (22) yield for `0<=t<=tau`

\[
\begin{aligned}
\|u(t)-v(t)\|_2
&\le
2\int_0^t
\|L(s)-L_*\|_{2\to2}\,
\|u(s)\|_2\,ds\\
&\ll
\tau\frac{\varepsilon}{\sigma_T^2}
\|u(0)\|_2.
\end{aligned}
\tag{24}
\]

At the chosen scale,

\[
\frac{\varepsilon}{\sigma_T^2}
=O\!\left(\frac1{\log^2T}\right)=o(1).
\tag{25}
\]

Thus the exact nonlinear trajectory stays `o(1)`-close **relative to its initial `ell^2` amplitude** to the arithmetic linear flow throughout every fixed heat-time interval.

For the initial cosine in (3), `u(0)` is the first Fourier eigenmode of `L_*`. Its amplitude rate is

\[
\rho_q=2\lambda_1(L_*)
=\frac{4\pi^2(q-1)}{q^2\sigma_T^2}
=\frac14+o(1),
\tag{26}
\]

and

\[
\sum_{j=0}^{q-1}u_j(0)e^{-2\pi ij/q}
=\frac{q\varepsilon}{2}.
\tag{27}
\]

Projecting (24) onto that Fourier vector proves (4), uniformly for `0<=t<=tau`. This upgrades the tangent obstruction of XF-044 to an exact nonlinear matched trajectory in the critical source scaling: the slow mode loses only the fixed factor `e^{-t/4+o(1)}`.

## 4. A surviving first Fourier coefficient forces triple-flux BV

The remaining issue is whether nonlinear harmonics could preserve the gap amplitude while somehow making the triple-flux variation `V_M` much smaller. A one-line Fourier/BV inequality prevents that.

Set

\[
y_j(t):=\log g_j(t),
\qquad
d_j:=y_{j+1}-y_j,
\qquad
\phi_j:=F'(d_j),
\tag{28}
\]

with the normalized-triple function `F` from XF-030. Since `|u_j|<=epsilon`,

\[
\log(1+u_j)=u_j+O(\varepsilon^2).
\tag{29}
\]

Let hats denote the unnormalized first Fourier coefficient at frequency `2pi/q`. Equations (4) and (29) give

\[
|\widehat y_1(t)|
=\frac{q\varepsilon}{2}
e^{-\rho_qt}\bigl(1+o(1)\bigr).
\tag{30}
\]

Because `d` is the cyclic first difference,

\[
|\widehat d_1|
=2\sin\frac\pi q\,|\widehat y_1|
=\pi\varepsilon e^{-\rho_qt}
\bigl(1+o(1)\bigr).
\tag{31}
\]

XF-030 gives the exact local expansion

\[
F'(d)=-\frac32d+O(d^3).
\tag{32}
\]

Here `|d_j|=O(epsilon)`, and

\[
q\varepsilon^3=o(\varepsilon)
\tag{33}
\]

at the scale (2). Hence

\[
|\widehat\phi_1|
=\frac{3\pi}{2}\varepsilon e^{-\rho_qt}
\bigl(1+o(1)\bigr).
\tag{34}
\]

Define the cyclic one-period flux variation

\[
V_q(t):=
\sum_{j=0}^{q-1}|\phi_{j+1}-\phi_j|.
\tag{35}
\]

Taking the same Fourier coefficient of the first difference and using the triangle inequality gives the exact BV lower bound

\[
V_q(t)
\ge
2\sin\frac\pi q\,|\widehat\phi_1|.
\tag{36}
\]

Therefore

\[
\boxed{
V_q(t)
\ge
\frac{3\pi^2}{q}\,
\varepsilon e^{-\rho_qt}
\bigl(1+o(1)\bigr).
}
\tag{37}
\]

This step is robust to every nonlinear harmonic generated by the flow. They may increase or rearrange the total variation, but they cannot erase the first Fourier coefficient without paying the BV norm detected by (36).

## 5. Repeating the memory wave across the source buffer saturates the stability gate

Use `2M=2q^2` consecutive gaps from the periodic trajectory and define `V_M` exactly as in XF-035/XF-044, omitting only the two endpoint differences of the finite block. The sequence `|phi_{j+1}-phi_j|` is `q`-periodic and nonnegative, so

\[
V_M(t)\ge(2q-1)V_q(t).
\tag{38}
\]

Multiplying (37) by `M=q^2` yields

\[
\begin{aligned}
M V_M(t)
&\ge
q^2(2q-1)
\frac{3\pi^2}{q}
\varepsilon e^{-\rho_qt}
(1+o(1))\\
&=
6\pi^2\kappa e^{-\rho_qt}
(1+o(1)).
\end{aligned}
\tag{39}
\]

Since `rho_q->1/4`, (39) proves (6).

The scaling is exactly the one isolated by XF-044. A memory wavelength has `q~log^2T` gaps, the source buffer contains `R=q` such wavelengths on each `M` half-block, and the relative gap amplitude is

\[
\varepsilon=\kappa R^{-2}.
\tag{40}
\]

It is therefore at the critical triple-flux scale even though its pointwise size is only `Theta(log^{-4}T)`. The current source count tolerances are much too coarse to see it, while universal nonlinear smoothing needs a time growing like `log R` to force the extra vanishing factor already identified in XF-044.

## 6. Stress tests and exact boundary of the obstruction

There are no collisions. Equation (8) keeps every gap between `sigma_T(1-epsilon)` and `sigma_T(1+epsilon)`, with `epsilon->0`; approaching a collision plays no role.

The source compatibility is deliberately stronger than a zeroth-order mean statement. Every translated period has exactly the source mean, every shorter translated span has error `O(log^{-3}T)`, and the corrected density spacing prevents the constant `log(4pi)/log T` mismatch identified in the adversarial review of XF-046 from accumulating across the `log^3T` physical buffer. The smooth Riemann--von Mangoldt curvature across that buffer is only `O(log^6T/T)=o(1)`.

The result nevertheless remains a **matched control**. The infinite `q`-periodic continuation has constant density and is not claimed to be the zero set of `H_t`, or even to satisfy the global Xi counting law away from the high window in which it is being used. The statement is that the local source constraints currently consumed by the research program cannot exclude the obstruction. A successful Xi theorem may use analytic information that has no counterpart in this periodic model.

The fixed-time restriction is essential. The finding does not contradict XF-041's eventual nonlinear damping. With `rho_q->1/4`, a time of order `log R` can reduce the memory amplitude by the additional factor required to enter `o(R^{-2})`; XF-044 already showed why such a time is unavailable to a bounded-time bootstrap.

Nor does (6) say that a finite Xi window is actively replenished by its near exterior. The periodic quotient removes a hard boundary altogether. What it proves is sharper for proof design: **even after removing the boundary, the source-compatible memory mode itself remains at critical BV strength for fixed time.** Therefore no estimate that treats near-buffer structure only through universal Cauchy smoothing can close the gate. The missing input must distinguish this coherent memory phase from the actual Xi zeros.

## 7. Prior-art and novelty boundary

Rodgers and Tao remain the load-bearing external source for the high-zero counting main term and memory-scale spacing tolerance. Guillin--Le Bris--Monmarche delimit the broad one-dimensional singular-repulsion/contraction mechanism, while time-varying symmetric consensus/Laplacian stability and Duhamel perturbation estimates are classical. A targeted search across deterministic log-gas dynamics, periodic long-range diffusion, and consensus perturbation did not identify an external theorem coupling those generic mechanisms to the de Bruijn--Newman memory scale and the normalized-triple BV threshold used here. Absence of such a match is not used as evidence of general novelty.

No new external theorem is load-bearing. Equations (8), (14), and (18) come from the exact periodic machinery already established in XF-041; the slow rate is the XF-044 mode; the source density correction is the one already persisted in XF-046; and the Fourier/BV lower bound (36) is elementary. `SOURCES.md` therefore requires no change.

The durable Mathia-local content is the simultaneous scale match: an exact nonlinear periodic control can be **source-indistinguishable at the currently used counting precision**, remain uniformly Cauchy-rigid, and still keep `M V_M` bounded away from zero throughout fixed heat time.

## 8. Consequence for `xi_flow`

XF-039 showed that static source rigidity cannot recover the flux-BV gate because microscopic alternation can hide inside the count. XF-040/XF-041 then killed that particular high-frequency obstruction dynamically. XF-047 supplies the complementary low-frequency control: at the full heat-memory wavelength, the same source tests admit a mode whose exact nonlinear decay is only order one and whose triple-flux BV remains critical.

Together with XF-046, this isolates the remaining burden more cleanly. The genuinely remote tail is already below `R^{-2}`, and universal Cauchy smoothing cannot eliminate a locally source-compatible memory wave in fixed time. The next positive step must therefore use **Xi-specific information about the near-buffer memory phase**: a statistic, signed identity, analytic constraint, or source-coupled transport mechanism that rules out coherent `q~log^2T` waves at amplitude `Theta(R^{-2})`. Merely improving count main terms, retaining a uniform gap envelope, or invoking another source-free contraction estimate will not cross the `M V_M=o(1)` gate.