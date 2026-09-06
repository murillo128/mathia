# MC-103 — Shrinking low-bias linear reconstruction is superpolynomially ill-conditioned

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-093` and `MC-094` showed that the source-forced Hamming deformation can be extrapolated from a **fixed-gap** interior set to the Möbius endpoint with only subpolynomial loss because its available degree ceiling is

\[
K_N:=\max_{\substack{a\le N^2\\a\ \mathrm{squarefree}}}\omega(a)
=O\!\left(\frac{\log N}{\log\log N}\right).
\tag{1}
\]

`MC-101` and `MC-102` then moved to shrinking low-bias windows, where the source amplitude genuinely drops to the degree-two scale and finally saturates at a positive linear diagonal floor. The remaining reconstruction question is quantitatively different: **can several values from a shrinking low-bias window be combined with signed weights cheaply enough to recover the hard endpoint?**

For black-box linear reconstruction based only on polynomial degree and low-bias point values, the answer is no. The obstruction is the exact Chebyshev extrapolation norm.

Let `0<tau<1` and let `\mathcal P_K` denote the real polynomials of degree at most `K`, equipped with

\[
\|P\|_{[0,\tau]}:=\sup_{0\le t\le\tau}|P(t)|.
\tag{2}
\]

Then endpoint evaluation has the exact operator norm

\[
\boxed{
\sup_{P\in\mathcal P_K\setminus\{0\}}
\frac{|P(1)|}{\|P\|_{[0,\tau]}}
=
\kappa_K(\tau)
:=T_K\!\left(\frac2\tau-1\right).
}
\tag{3}
\]

The constant is attained by

\[
P_*(t)=T_K\!\left(\frac{2t}{\tau}-1\right).
\tag{4}
\]

Consequently, if nodes `t_j\in[0,\tau]` and signed weights `w_j` reconstruct endpoint evaluation exactly for **every** degree-`K` polynomial,

\[
P(1)=\sum_j w_jP(t_j)
\qquad(P\in\mathcal P_K),
\tag{5}
\]

then necessarily

\[
\boxed{
\sum_j|w_j|\ge\kappa_K(\tau).
}
\tag{6}
\]

The same lower bound holds for any exact signed-measure formula

\[
P(1)=\int_{[0,\tau]}P(t)\,d\nu(t),
\tag{7}
\]

with `\|\nu\|_{TV}\ge\kappa_K(\tau)`.

Knowing and subtracting finitely many low Hamming shells does not remove this degree-only instability. Fix `0\le r<K` and restrict to polynomials whose Taylor coefficients of degrees `0,...,r` vanish. The explicit witness

\[
P_{K,r}(t)
=
\left(\frac t\tau\right)^{r+1}
T_{K-r-1}\!\left(\frac{2t}{\tau}-1\right)
\tag{8}
\]

has `\|P_{K,r}\|_{[0,\tau]}\le1`, vanishes to order `r+1` at zero, and satisfies

\[
\boxed{
|P_{K,r}(1)|
=
\tau^{-(r+1)}
T_{K-r-1}\!\left(\frac2\tau-1\right).
}
\tag{9}
\]

Thus any universal exact linear reconstruction that is also allowed the first `r+1` Taylor coefficients must still have point-value amplification at least the right side of `(9)` on the residual subspace.

For the Hamming source, this becomes fatal to a **degree-only** shrinking-window transfer at every polynomially small bias. If

\[
\tau_N=N^{-\alpha},\qquad \alpha>0,
\tag{10}
\]

then

\[
\operatorname{arcosh}\!\left(\frac2{\tau_N}-1\right)
=
\alpha\log N+\log4+o(1).
\tag{11}
\]

Since `K_N\to\infty` and `(1)` holds,

\[
\boxed{
\frac{\log\kappa_{K_N}(\tau_N)}{\log N}
=
\alpha K_N+o(K_N)
\longrightarrow\infty.
}
\tag{12}
\]

Hence the optimal black-box exact reconstruction constant grows faster than every fixed power of `N`. At the square-root transition isolated by `MC-102`, for fixed `u>0`,

\[
\tau_N=u\frac{\log N}{\sqrt N},
\tag{13}
\]

one likewise has

\[
\boxed{
\frac{\log\kappa_{K_N}(\tau_N)}{\log N}
=\left(\frac12+o(1)\right)K_N
\longrightarrow\infty.
}
\tag{14}
\]

Therefore the genuine low-bias amplitude reduction proved in `MC-101`--`MC-102` cannot be transported to `t=1` by an exact linear interpolation, quadrature, or signed value recurrence whose only structural input is the degree ceiling and finitely many known low shells. Its **best possible universal conditioning cost is already superpolynomial** in precisely the polynomially shrinking regimes where the source amplitude gains a fixed power.

This does **not** show that the actual arithmetic polynomial `\mathcal Q_N` itself has degree `K_N`, nor that every source-specific signed relation is ill-conditioned. It rules out the generic reconstruction escape left after `MC-102`: any survivor must exploit additional algebraic constraints on the actual Hamming coefficients, a source-specific relation not valid for arbitrary degree-bounded polynomials, a non-point observable, or a genuinely different source coupling.

## 1. Exact endpoint evaluation norm

Map `[0,\tau]` affinely to `[-1,1]` by

\[
x=\frac{2t}{\tau}-1,
\qquad
t=\frac\tau2(x+1).
\tag{15}
\]

The endpoint `t=1` corresponds to

\[
x_\tau=\frac2\tau-1>1.
\tag{16}
\]

For `P\in\mathcal P_K`, set

\[
Q(x)=P\!\left(\frac\tau2(x+1)\right).
\tag{17}
\]

Then `\deg Q\le K` and

\[
\|Q\|_{[-1,1]}=\|P\|_{[0,\tau]}.
\tag{18}
\]

The classical one-interval Chebyshev extremal theorem gives

\[
|Q(x_\tau)|
\le
T_K(x_\tau)\|Q\|_{[-1,1]}.
\tag{19}
\]

Substituting `(16)`--`(18)` proves the upper bound in `(3)`. Equality is attained by `Q=T_K`, equivalently by the polynomial `(4)`, because `|T_K(x)|\le1` on `[-1,1]`. Thus `(3)` is an exact norm identity, not merely a convenient interpolation estimate.

This also clarifies the fixed-gap result of `MC-093`. If `\tau=1-\eta` with fixed `0<\eta<1`, then

\[
\frac2\tau-1=\frac{1+\eta}{1-\eta},
\]

so `(3)` is exactly the Chebyshev factor already appearing there. Fixed-gap extrapolation is cheap because the exterior point in the normalized coordinate is fixed while the source degree is sublogarithmic. Shrinking `\tau` moves that point to infinity and changes the ledger completely.

## 2. Signed sampling cannot beat the exact norm

Suppose `(5)` holds. Apply it to the extremal polynomial `(4)`. Every node lies in `[0,\tau]`, hence

\[
|P_*(t_j)|\le1.
\tag{20}
\]

Therefore

\[
\kappa_K(\tau)
=|P_*(1)|
=\left|\sum_jw_jP_*(t_j)\right|
\le\sum_j|w_j|,
\tag{21}
\]

which proves `(6)`.

The signed-measure version is identical:

\[
\kappa_K(\tau)
=\left|\int P_*\,d\nu\right|
\le
\int|P_*|\,d|\nu|
\le\|\nu\|_{TV}.
\tag{22}
\]

Thus adding more low-bias sample points cannot create a hidden stable linear recurrence solely by cancellation among the reconstruction weights. Any exact formula valid on the complete degree-bounded class must carry at least the Chebyshev total-variation cost.

The result is independent of the choice of nodes. Chebyshev nodes can optimize interpolation stability inside a controlled interval, as used in `MC-094`, but no node placement inside `[0,\tau]` can beat the exterior evaluation norm itself.

## 3. Finitely many known low shells do not repair generic conditioning

One possible response to `MC-102` is to subtract the now-understood low Hamming shells before reconstructing. The degree-only obstruction survives any fixed number of such subtractions.

Let

\[
\mathcal P_{K,r}^0
:=\{P\in\mathcal P_K:P^{(j)}(0)=0\text{ for }0\le j\le r\}.
\tag{23}
\]

The witness `(8)` lies in this subspace. On `[0,\tau]`, both factors in `(8)` have absolute value at most one, so

\[
\|P_{K,r}\|_{[0,\tau]}\le1.
\tag{24}
\]

At `t=1` it gives `(9)`. Therefore the endpoint evaluation norm on `\mathcal P_{K,r}^0` is at least the right side of `(9)`.

Equivalently, suppose a reconstruction is allowed to use the Taylor data `P^{(j)}(0)` for `j\le r` in addition to arbitrary point values in `[0,\tau]`. Applying that reconstruction to `P_{K,r}` kills all of the extra Taylor terms. The same triangle-inequality argument then forces the point-value coefficient mass to be at least `(9)`.

For fixed `r`, replacing `K` by `K-r-1` does not alter the shrinking-window power diagnosis once `K\to\infty`. In particular, exact knowledge of `C_{0,N}`, `C_{1,N}`, and `C_{2,N}` does not by itself make low-bias extrapolation a stable generic operation. Additional information must constrain the **remaining source coefficients jointly**, not merely remove finitely many radial degrees.

## 4. The Hamming shrinking regimes are on the wrong side of the conditioning ledger

For `x>1`,

\[
T_K(x)=\cosh(K\operatorname{arcosh}x).
\tag{25}
\]

As `\tau\downarrow0`,

\[
\operatorname{arcosh}\!\left(\frac2\tau-1\right)
=
\log\!\left(\frac4\tau\right)+O(\tau).
\tag{26}
\]

Consequently, whenever `K\operatorname{arcosh}(2/\tau-1)\to\infty`,

\[
\log\kappa_K(\tau)
=
K\log\!\left(\frac4\tau\right)
+O(K\tau+1).
\tag{27}
\]

Apply `(27)` with the available Hamming ceiling `K=K_N`. The elementary argument already used in `MC-093` gives the upper bound `(1)`. Also `K_N\to\infty`: for every fixed `J`, the product of the first `J` primes is fixed and is eventually at most `N^2`, so eventually `K_N\ge J`.

For the polynomial bias `(10)`, equations `(27)` and `(1)` yield `(12)`. The additive `K_N\log4` and `O(K_N\tau_N)` terms are `o(K_N\log N)`, while `K_N\to\infty` makes the normalized logarithm diverge.

For `(13)`,

\[
\log\frac4{\tau_N}
=
\frac12\log N-\log\log N+O_u(1),
\tag{28}
\]

and `(14)` follows.

These estimates should be compared with the source amplitudes already proved, not with a heuristic random-walk scale. `MC-101` shows that for `\tau_N=N^{-\alpha}`, `0<\alpha<1/2`, the maximum amplitude on `[0,\tau_N]` is asymptotic to

\[
c_2\frac{N^{2-2\alpha}}{(\log N)^2}.
\tag{29}
\]

`MC-102` then shows that at and below the square-root transition the source is instead pinned at a positive linear scale by the diagonal shell. Those are genuine deterministic regularization gains. But multiplying either scale by the optimal degree-only exact reconstruction cost from `(12)` or `(14)` loses more than every fixed power. The regularization and reconstruction ledgers therefore do not balance for black-box low-bias value extrapolation.

A useful general criterion is visible directly from `(27)`. Degree-only endpoint recovery can be subpolynomial only when the relevant exterior growth satisfies

\[
K_N\log(1/\tau_N)=o(\log N)
\tag{30}
\]

(up to harmless constants in regimes with `\tau_N\to0`). The polynomial and square-root bias windows violate `(30)` by an unbounded factor. By contrast, the fixed-gap case has `\log(1/\tau)=O(1)` and `(1)` makes the cost `N^{o(1)}`, exactly matching `MC-093`.

Equation `(30)` is a conditioning criterion for the degree-bounded class, not a new arithmetic estimate for `\mathcal Q_N`.

## 5. Prior art and novelty boundary

The extremal mechanism in `(3)` is classical Chebyshev/Remez approximation theory. B. Eichinger and P. Yuditskii, *Pointwise Remez inequality*, Constructive Approximation 54 (2021), 529--554, DOI `10.1007/s00365-021-09562-1`, record the one-interval Remez extremal solution in terms of rescaled Chebyshev polynomials. This source is already the approximation-theoretic boundary used in `MC-093`.

A still closer modern prior-art formulation is A. A. Trembach, *Optimal extrapolation of polynomials given with error*, Trudy Instituta Matematiki i Mekhaniki UrO RAN 30 (2024), no. 4, 265--275, DOI `10.21538/0134-4889-2024-30-4-265-275`. The paper studies optimal extrapolation as an optimal-recovery problem, relates it directly to Chebyshev least-deviation problems, and states an exact solution for extrapolation from `[-1,1]` to the real line.

Thus neither the exact norm `(3)` nor the ill-conditioning principle is claimed as new. The signed-sampling lower bound `(6)` is the immediate dual consequence of the same extremal polynomial. The low-shell witness `(8)` is an elementary specialization.

A targeted audit around pointwise Remez inequalities, optimal polynomial extrapolation/recovery, and stable interpolation supplied no basis for a novelty claim. **No novelty claim is made.** The durable line-specific content is the quantitative insertion of this classical optimal-recovery constant into the shrinking Hamming regime left open by `MC-101`--`MC-102`, including the source-relevant finite-low-shell control `(9)`.

## 6. Boundaries and falsification tests

- The theorem is a **black-box degree-class obstruction**. The actual `\mathcal Q_N` may occupy a much smaller coefficient manifold than all of `\mathcal P_{K_N}`. A source-specific identity exploiting such extra constraints can evade `(12)` because it need not reconstruct arbitrary degree-bounded polynomials.
- `K_N` is an available degree ceiling, not a proved exact value of `\deg\mathcal Q_N`. If a future source theorem proves a much smaller actual degree or a stronger coefficient relation, the correct reconstruction norm must be recomputed on that restricted class.
- The result concerns exact linear reconstruction from values supported inside `[0,\tau_N]`, optionally augmented by finitely many low Taylor coefficients. It does not rule out nonlinear source identities, derivatives or moments carrying genuinely additional information, a moving interior window not contained near zero, or an observable not reducible to point evaluation of this Hamming polynomial.
- Approximate reconstruction is not automatically covered by `(6)`. Any proposed approximation must state a function class, reconstruction error, and stability norm. The extremal witnesses remain a natural adversarial test, but a quantitative approximate-recovery theorem requires its own audit.
- Subtracting a number of shells that grows with `N` is outside the fixed-`r` statement `(9)`. Such a proposal must account for how those shells are obtained independently and whether their acquisition already reconstructs the hard source.
- No estimate for `\mathcal Q_N(1)`, `M(N)`, or `M(N^2)` follows. No zeta continuation or zero-free-region information enters the proof.
- The finding does not challenge the deterministic low-bias asymptotics of `MC-101`--`MC-102`; it explains why their power gain is unusable under one broad reconstruction class.

A decisive escape is therefore concrete: exhibit an exact or sufficiently stable relation for the **actual source coefficients** whose condition number is polynomially smaller than the Chebyshev class norm because of a proved arithmetic constraint not shared by generic polynomials. If no such constraint enters, changing nodes or signed weights cannot help.

## Consequence for the research line

`MC-102` closed the first low-bias escape by showing that individual endpoint-anchored Hamming amplitudes stop shrinking at the positive `c_0N` floor. It left open whether several low-bias values could be coupled with signed information at a reconstruction cost smaller than the regularization gain.

`MC-103` closes the **generic linear value-reconstruction** version of that escape. Once the sampling window shrinks by any fixed power of `N`, the exact Chebyshev endpoint norm for the available degree class is already superpolynomial; at the square-root transition it is superpolynomial as well. Finitely many known low shells do not change that verdict.

The surviving burden is narrower and more arithmetic: a useful recurrence or coupling must exploit additional source-specific relations among the Hamming coefficients, carry information not reducible to low-bias point values plus finitely many Taylor shells, or change the source itself. The next candidate should be judged first on that structural distinction before any interpolation numerics are pursued.
