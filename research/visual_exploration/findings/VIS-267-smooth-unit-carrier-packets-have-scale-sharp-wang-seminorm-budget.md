# VIS-267 — smooth unit-carrier packets have a scale-sharp Wang seminorm budget

## Claim

Fix an integer `m>=1`, a fixed support margin `0<lambda<theta<1`, and write `L=log T`. Let `b=b(T)` satisfy `0<b<lambda`. Consider any real even smooth test

`g_b in C_c^infinity((-b,b))`

with the cusp-adapted cancellations

`int g_b(q)dq=0`,

`int |q|g_b(q)dq=0`,

and, for `m>=2`,

`int q^(2j)g_b(q)dq=0`, `j=1,...,m-1`,

normalized so that

`int q^(2m)g_b(q)dq=1`.

Let `E_m` be the sharp approximation constant from `VIS-259`:

`E_m = dist_(C[0,1])(t^(2m), span{1,t,t^2,t^4,...,t^(2m-2)}).`

Then every such smooth realization obeys

`||g_b||_infinity >= (2E_m)^(-1) b^(-(2m+1))`

and

`||g_b'||_infinity >= (2E_m)^(-1) b^(-(2m+2)).`

The powers are sharp. For every fixed `m` there exists a real even profile `h_m in C_c^infinity((-1,1))` with the required cancellations and unit `2m`-th moment such that

`g_b(q)=b^(-(2m+1)) h_m(q/b)`

has exactly

`||g_b||_infinity = Theta_m(b^(-(2m+1)))`,

`||g_b'||_infinity = Theta_m(b^(-(2m+2))).`

Combining this with the quantitative moving-test bound extracted from Wang's proof in `VIS-266`, a smooth unit-carrier family can satisfy that proof's normalized seminorm budget only if

`1/(L b^(2m+2)) -> 0`

and

`T^(lambda-theta) L / b^(2m+1) -> 0`.

Conversely, the fixed-profile family above satisfies Wang's proof budget whenever these two conditions hold. Thus, for fixed `lambda<theta`, these are the scale-sharp admissibility conditions for this smooth packet class, up to constants depending on the chosen fixed profile and on `lambda,theta`.

For logarithmic bandwidth

`b=L^(-q)`,

the power-saving support margin makes the second condition automatic, and the exact exponent gate is

`q < 1/(2m+2).`

In particular:

- a unit quadratic cusp-cancelled packet (`m=1`) can be certified only on scales `b=L^(-q)` with `q<1/4`;
- a unit quartic cusp-plus-quadratic-cancelled packet (`m=2`) can be certified only with `q<1/6`.

The statement concerns **what Wang's present proof can certify after the packet is realized as a smooth moving test**. It does not prove that the pair-correlation asymptotic itself fails at the boundary or beyond it.

**Evidence/status:** `EXACT-DERIVED + SCALE-SHARP SMOOTH-REALIZATION GATE + LITERATURE-TRANSFER + NEGATIVE/REDESIGN CONTROL + NO-NOVELTY-CLAIM`.

## 1. `VIS-259` forces the sup-norm scale

Treat `g_b(q)dq` as a finite signed measure. Its total variation is

`||g_b(q)dq||_TV = ||g_b||_1`.

Because the packet has unit `2m`-th moment and all the nuisance moments required by `VIS-259`, the sharp packet inequality there gives

`1 <= E_m b^(2m) ||g_b||_1`.

Hence

`||g_b||_1 >= E_m^(-1)b^(-2m).`

The support has length at most `2b`, so

`||g_b||_1 <= 2b ||g_b||_infinity`.

Therefore

`||g_b||_infinity >= (2E_m)^(-1)b^(-(2m+1)).`

This lower bound is not a feature of any particular atomic extremizer. It applies to every smooth density representing the same unit-carrier cancellation problem.

## 2. Zero mass forces one further inverse bandwidth in the derivative

Because `g_b` is even and has zero total mass,

`int_0^b g_b(q)dq=0`.

The function is nonzero because its `2m`-th moment equals one. Continuity therefore implies that `g_b` has a zero somewhere in `[0,b]`. Let `q_* in [0,b]` satisfy

`|g_b(q_*)|=||g_b||_infinity`,

and let `q_0 in [0,b]` be a zero. The mean-value theorem gives

`||g_b||_infinity <= |q_*-q_0| ||g_b'||_infinity <= b ||g_b'||_infinity`.

Combining with the previous bound yields

`||g_b'||_infinity >= (2E_m)^(-1)b^(-(2m+2)).`

Thus smoothing does not merely inherit the total-variation cost `b^(-2m)` from `VIS-259`. Realizing that signed packet as an actual smooth test necessarily adds one inverse bandwidth in amplitude and another in the first derivative seen by Wang's theorem interface.

## 3. The exponents are attainable by a fixed smooth profile

Consider the finite family of even moment functionals on `C_c^infinity((-1,1))`:

`h -> int h`,

`h -> int |x|h(x)dx`,

`h -> int x^(2j)h(x)dx`, `j=1,...,m`.

They are linearly independent. Indeed, a linear relation among them that vanished on every even smooth compactly supported test would imply that the corresponding linear combination of

`1, |x|, x^2, x^4, ..., x^(2m)`

vanishes on `(0,1)`, where these functions are linearly independent. Therefore the finite-dimensional moment map is onto its target, and one may choose a fixed real even smooth profile `h_m` for which all nuisance moments vanish while

`int x^(2m)h_m(x)dx=1`.

Now scale by

`g_b(q)=b^(-(2m+1))h_m(q/b)`.

A change of variables preserves every required zero moment and gives unit `2m`-th moment. Directly,

`||g_b||_infinity=b^(-(2m+1))||h_m||_infinity`,

`||g_b'||_infinity=b^(-(2m+2))||h_m'||_infinity`.

Hence the lower-bound powers in the previous sections are optimal. No choice of smooth packet shape can improve those bandwidth exponents while keeping the same support and unit-carrier normalization.

## 4. Composition with Wang's moving-test estimate

`VIS-266` reads the proof of Biao Wang's Theorem 2.2 quantitatively. For fixed `lambda<theta`, a real even smooth family supported in `[-lambda,lambda]` satisfies the normalized leading Montgomery law with proof error bounded by

`O_(lambda,theta)( ||g_T'||_infinity/L`
` + ||g_T||_infinity [1/L + L^(-3/2) + T^(lambda-theta)L + 1/(T^theta L)] ).`

For the unit-carrier packet above, the derivative lower bound implies that this displayed seminorm criterion cannot tend to zero unless

`1/(L b^(2m+2)) -> 0`.

The amplitude lower bound similarly forces

`T^(lambda-theta)L/b^(2m+1) -> 0`.

The remaining `||g_b||_infinity/L` and `L^(-3/2)` pieces are weaker once `b<=1` and the derivative condition holds.

For the scaled fixed profile from Section 3, the same powers give matching upper bounds. Consequently the two displayed asymptotic conditions are not only necessary for satisfying Wang's present seminorm budget but sufficient for an explicit smooth realization of the packet.

When `b=L^(-q)` and `delta=theta-lambda>0` is fixed,

`T^(-delta)L^(1+q(2m+1)) -> 0`

for every fixed `q`. The derivative term is therefore decisive:

`L^(q(2m+2)-1) -> 0`

if and only if

`q<1/(2m+2)`.

At the boundary `q=1/(2m+2)`, Wang's present norm bound stays at order one for every unit-carrier smooth packet because of the universal derivative lower bound; beyond it the bound diverges.

## 5. Prior-art and novelty boundary

The load-bearing external input is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially Theorem 2.2 and its proof. Wang proves a short-interval Montgomery pair-correlation theorem for fixed smooth test functions. `VIS-266` already records the Mathia-specific bookkeeping that exposes the dependence on `||g||_infinity` and `||g'||_infinity` for a fixed outer support margin.

The lower bounds here use only `VIS-259`, support length, zero mass, and the mean-value theorem. The matching smooth scaling is elementary finite-dimensional moment interpolation followed by dilation. A targeted check of the current Wang source did not reveal this cusp-adapted unit-carrier optimization because that packet problem is not the object of the paper.

No novelty is claimed for the individual approximation-duality, moment-interpolation, norm, or mean-value ingredients. The durable content is their exact composition with the active Mathia packet interface: it identifies the bandwidth exponent consumed when the sharp signed-measure conditioning problem is converted into the smooth moving-test seminorms that Wang's proof actually charges.

## 6. Boundaries and falsification

This result normalizes the first surviving even moment to one. If an application uses another normalization, all amplitude and derivative bounds scale linearly with that carrier normalization.

The lower bounds use evenness, zero mass, support in `[-b,b]`, the `VIS-259` cancellation constraints, and unit `2m`-th moment. Dropping or materially changing any of these hypotheses changes the optimization problem. A theorem controlled by a weaker norm than `||g'||_infinity`, a structured signed error orthogonal to the packet, or a direct nonsmooth-test formulation could evade this particular gate.

Most importantly, failure of Wang's **current proof bound** to vanish is not a lower bound on the true pair-correlation error. The conditions here characterize the interface supplied by `VIS-266`, not an impossibility theorem for all future short-interval pair-correlation methods.

The fixed support margin remains essential. Nothing here controls the constants as `lambda` approaches `theta`, so the moving-support-edge obstruction in `VIS-265` is unchanged.

No untouched confirmation-zero data are used.

## Research consequence

The accepted support-edge redesign now has an explicit smooth-transfer price. A unit quadratic cusp-cancelled probe cannot simultaneously shrink like `L^(-q)` and remain certified by Wang's present proof unless `q<1/4`; the quartic branch is stricter, requiring `q<1/6`; the order-`2m` branch requires `q<1/(2m+2)`.

This compounds the negative message of `VIS-259`: higher cancellation not only increases total-variation conditioning from `b^-2` to `b^-4`, `b^-6`, and so on, but also tightens the fastest logarithmic bandwidth at which the resulting packet can be realized as a theorem-compatible smooth moving test.

The next useful question is therefore not another generic packet optimization. For a pre-registered quadratic or quartic source-specific coefficient, one must check whether there exists a bandwidth window that simultaneously satisfies this smooth-transfer gate and makes the actual arithmetic signal dominate the theorem/transfer/covariance remainder. If no such window exists for the derived source coefficient and error law, that branch should be killed rather than repaired by adding further moment cancellations.