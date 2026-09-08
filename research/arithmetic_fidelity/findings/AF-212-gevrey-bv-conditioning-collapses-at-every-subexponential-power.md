# AF-212 — Gevrey bumps force stretched-exponential BV conditioning collapse at every exponent below one

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-FIDELITY`, `SOURCE-COMPLEXITY-GATE`, `SEVERE-ILL-POSEDNESS`, `NO-NOVELTY-CLAIM`

## Claim

AF-209 proves that every fixed bounded-variation complexity budget restores a positive lower recovery modulus for a positive-width Euler observation band. AF-211 then shows that this modulus deteriorates faster than every algebraic power as the permitted BV complexity grows. The `C_c^\infty` argument in AF-211 deliberately leaves the quantitative decay profile unresolved because generic smoothness controls the Fourier tail only super-algebraically.

That profile can be sharpened by choosing the same fixed-support oscillatory source inside a compactly supported Gevrey class.

Keep the AF-209/AF-211 parameters

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad 0<T<\infty,\qquad L>x,
\]

and the anchored Euler observation

\[
D_T(b)
=
\sup_{|\tau|\le T}
\left|
\int_x^L \phi_\tau(t)b(t)\,dt
\right|,
\qquad
V_h(b)=\int_x^L h(t)|b(t)|\,dt.
\]

Let

\[
\gamma(M)
:=
\inf\left\{
\frac{D_T(b)}{V_h(b)}:
0\ne b\in BV([x,L]),\
\operatorname{Var}(b)\le M V_h(b)
\right\}
\]

be the optimal AF-209 coercivity constant. Then AF-209 gives `\gamma(M)>0` for every finite `M`, but in fact:

\[
\boxed{
\forall\alpha\in(0,1)\ \exists\ c_\alpha,C_\alpha,M_\alpha>0
\quad\text{such that}\quad
\gamma(M)
\le
C_\alpha\exp(-c_\alpha M^\alpha)
\quad(M\ge M_\alpha).
}
\tag{1}
\]

Thus the fixed-band inverse condition number grows at least stretched-exponentially at **every fixed exponent below one** along the BV exhaustion. The constants in `(1)` may deteriorate as `\alpha\uparrow1`; no uniform limit in `\alpha` and no pure exponential statement are claimed.

Equivalently, for every Gevrey order `r>1`, there is one fixed nonnegative nonzero bump `q_r\in G_c^r((a,b))`, with

\[
x<a<b<L,
\]

whose modulated zero-mass directions produce

\[
\boxed{
\gamma(M)\le C_r\exp(-c_r M^{1/r})
}
\tag{2}
\]

for all sufficiently large `M`.

The result is a strict quantitative strengthening of AF-211. It does not create new exact collisions: every finite-budget class remains coercive. The obstruction is that the conditioning constants can deteriorate almost exponentially even though the observation is exactly injective on the unrestricted `L^1` density class.

## Derivation

### 1. Fix one compactly supported Gevrey source profile

Choose a Gevrey order

\[
r>1.
\]

The non-quasianalytic Gevrey class of order `r` contains nonzero compactly supported functions. Fix a nonnegative nonzero

\[
q\in G_c^r((a,b))
\]

with constants `A_q,C_q<\infty` such that

\[
\|q^{(j)}\|_\infty
\le
C_q A_q^j(j!)^r
\qquad(j\ge0).
\tag{3}
\]

For integers `n\ge1`, use exactly the AF-211 oscillatory density

\[
r_n(t)
:=
\frac1n\frac d{dt}\bigl(q(t)\sin(nt)\bigr)
=
q(t)\cos(nt)+\frac{q'(t)}n\sin(nt).
\tag{4}
\]

Compact support gives

\[
\int_x^L r_n(t)\,dt=0.
\tag{5}
\]

The source-side estimates from AF-211 use only smoothness and the fixed bump, so they remain valid. Since `q\ge0`, periodic averaging gives

\[
V_h(r_n)
\longrightarrow
v_*:=\frac2\pi\int_a^b h(t)q(t)\,dt>0.
\tag{6}
\]

Hence, for large `n`,

\[
0<v_-\le V_h(r_n)\le v_+<\infty.
\tag{7}
\]

Also

\[
r_n'(t)
=
-nq(t)\sin(nt)
+2q'(t)\cos(nt)
+\frac{q''(t)}n\sin(nt),
\]

so

\[
\operatorname{Var}(r_n)
\le A_0 n
\tag{8}
\]

for one constant `A_0`. After normalization

\[
b_n:=\frac{r_n}{V_h(r_n)},
\tag{9}
\]

there is `A<\infty` with

\[
V_h(b_n)=1,
\qquad
\operatorname{Var}(b_n)\le An.
\tag{10}
\]

Thus oscillation frequency still costs only linearly in the AF-209 BV complexity budget.

### 2. The fixed Euler band is uniformly analytic on the interior support

Write

\[
u_\tau(t):=\partial_t\phi_\tau(t).
\]

For `|\tau|\le T`, the Euler series defining `\phi_\tau` is holomorphic in a common complex neighborhood of the fixed real interval `[a,b]`. Indeed, with `s=\sigma+i\tau`, choose a strip width `\eta>0` small enough that

\[
\operatorname{Re}(sz)
=\sigma\operatorname{Re}z-\tau\operatorname{Im}z
\ge \frac{\sigma a}{2}>0
\]

whenever `\operatorname{Re}z\in[a,b]`, `|\operatorname{Im}z|\le\eta`, and `|\tau|\le T`. On that common neighborhood the defining exponential series and all its `t`-derivatives converge locally uniformly.

Uniform Cauchy estimates therefore give constants `C_u,R_u<\infty` such that

\[
\sup_{|\tau|\le T}\|u_\tau^{(j)}\|_{L^\infty([a,b])}
\le
C_u R_u^j j!
\qquad(j\ge0).
\tag{11}
\]

Multiplication by an analytic family preserves the Gevrey order of the fixed bump. Put

\[
A_\tau(t):=u_\tau(t)q(t).
\]

By Leibniz' rule, `(3)` and `(11)`,

\[
\begin{aligned}
|A_\tau^{(k)}(t)|
&\le
C_uC_q
\sum_{j=0}^k
\binom{k}{j}
R_u^j j!\,
A_q^{k-j}((k-j)!)^r\\
&\le
C_1 B^k(k!)^r
\end{aligned}
\tag{12}
\]

for fixed `C_1,B<\infty`, uniformly in `|\tau|\le T`. The last step uses

\[
\binom{k}{j}j!((k-j)!)^r
=
k!((k-j)!)^{r-1}
\le(k!)^r
\]

and absorbs the finite geometric sum into `B^k`. Since all `A_\tau` are supported in the same compact subinterval of `(a,b)`, `(12)` also gives

\[
\sup_{|\tau|\le T}\|A_\tau^{(k)}\|_1
\le C_2B^k(k!)^r.
\tag{13}
\]

### 3. Optimize the integration-by-parts order

From `(4)` and one integration by parts exactly as in AF-211,

\[
\int_x^L\phi_\tau(t)r_n(t)\,dt
=
-\frac1n
\int_a^b A_\tau(t)\sin(nt)\,dt.
\tag{14}
\]

Because `A_\tau` is compactly supported in `(a,b)`, repeated integration by parts creates no boundary terms. For every integer `k\ge0`, `(13)` yields

\[
D_T(r_n)
\le
\frac{C_2}{n}
\frac{B^k(k!)^r}{n^k}.
\tag{15}
\]

Using `k!\le k^k`,

\[
D_T(r_n)
\le
\frac{C_2}{n}
\left(\frac{Bk^r}{n}\right)^k.
\tag{16}
\]

Choose

\[
k_n
=
\left\lfloor c_0n^{1/r}\right\rfloor
\tag{17}
\]

with fixed `c_0>0` small enough that `Bc_0^r<1/2`. For large `n`,

\[
\frac{Bk_n^r}{n}\le\frac12,
\]

and `k_n\ge c_1n^{1/r}` for some `c_1>0`. Therefore

\[
D_T(r_n)
\le
\frac{C_2}{n}2^{-k_n}
\le
C_3\exp(-c_2n^{1/r}).
\tag{18}
\]

Combining `(7)`, `(9)` and `(18)` gives

\[
D_T(b_n)
\le
C_4\exp(-c_2n^{1/r}).
\tag{19}
\]

This is the quantitative information absent from the generic `C_c^\infty` proof of AF-211.

### 4. Convert oscillation frequency into the BV budget

For sufficiently large `M`, choose

\[
n(M)=\left\lfloor\frac{M}{A}\right\rfloor.
\tag{20}
\]

After increasing the threshold if necessary, `(10)` makes `b_{n(M)}` admissible in the definition of `\gamma(M)`, while

\[
n(M)\ge\frac{M}{2A}.
\tag{21}
\]

Thus `(19)` gives

\[
\gamma(M)
\le
C_r\exp(-c_rM^{1/r}),
\tag{22}
\]

which proves `(2)`. Given any fixed `\alpha\in(0,1)`, choose `r=1/\alpha>1`; `(22)` becomes `(1)`.

## Associated-function interpretation

The optimization in `(15)` is the fixed-support/source-oscillation counterpart of the associated-function optimization in AF-186. If an amplitude family obeys a derivative envelope

\[
\|A_\tau^{(k)}\|_1\le CR^kW_k,
\]

then the best bound obtained by repeated integration by parts is governed by

\[
\Omega_W(t)
:=
\sup_{k\ge0}\bigl(k\log t-\log W_k\bigr),
\]

because

\[
\inf_{k\ge0}\frac{R^kW_k}{n^k}
=
\exp[-\Omega_W(n/R)].
\tag{23}
\]

For the Gevrey weight `W_k=(k!)^r`, the associated function grows like `t^{1/r}` up to multiplicative constants, exactly matching `(18)`.

The mathematical roles are different from AF-185/AF-186. There the observation derivative budget controls how high an order of **positive moment-cancelling point cluster** can remain invisible as its spatial scale shrinks. Here the observation band and support interval are fixed, the source direction is a **signed oscillatory BV density**, and the regularity profile quantifies how rapidly the AF-209 coercivity constant collapses as the permitted source complexity grows. The common associated-function mathematics exposes a dual conditioning principle rather than duplicating the same source model.

## Exact controls and boundaries

### AF-209 remains valid at every finite budget

Nothing here produces a nonzero kernel element. The densities `b_n` leave every fixed BV-complexity cone because their variation grows linearly with `n`. AF-209 therefore continues to give

\[
\gamma(M)>0
\]

for every finite `M`. AF-212 only sharpens how badly those positive constants may degenerate along `M\to\infty`.

### This is stronger than AF-211 but uses a stricter chosen source profile

AF-211 works with an arbitrary fixed `C_c^\infty` bump and hence can conclude only rapid decay beyond every power, with uncontrolled constants. AF-212 chooses a bump in a fixed Gevrey class and converts its derivative growth into a stretched-exponential rate. The underlying BV source class in the definition of `\gamma(M)` is unchanged; only the explicit test sequence used to upper-bound its optimal coercivity constant is more regular.

### The exponent-one endpoint is not proved or disproved

A nonzero compactly supported real-analytic bump does not exist, and classical Paley-Wiener/Ingham uncertainty prevents a nonzero compactly supported function from having a genuinely exponential Fourier tail of the naive type used here. Accordingly the Gevrey construction reaches every fixed `\alpha<1` but not `\alpha=1`.

This does **not** prove that

\[
\gamma(M)\not\le Ce^{-cM}.
\]

The infimum defining `\gamma` ranges over all admissible BV sources, not only the single-bump modulation family. A different construction could in principle give an exponential or still stronger upper bound. The endpoint is therefore an open conditioning question, not a lower bound supplied by uncertainty theory.

### Constants are not uniform as `\alpha\uparrow1`

For each exponent `\alpha<1`, the proof may use a different Gevrey bump and different derivative constants. Equation `(1)` must not be read as one estimate uniform over all `\alpha`, nor as an asymptotic of the form `\exp(-M^{1-o(1)})` without further quantitative control of those constants.

### The mechanism is signed

The oscillatory density changes sign. AF-184/AF-185 give a different severe-instability mechanism using positive parity-split point clusters with growing cancellation order. AF-212 does not transfer the near-exponential BV rate to positive source cones, mass-one Peano carriers, or generalized-prime controls without a separate realizability and complexity analysis.

### No RH consequence is obtained

The theorem concerns the conditioning of one Euler-log observation family on an expanding signed source class. It neither identifies rational primes nor proves that the actual arithmetic source occupies the bad directions. Any RH-facing use would first require an independent dictionary placing the relevant arithmetic discriminator inside a declared source-complexity regime.

## Prior art and novelty assessment

Every analytic ingredient behind the rate is classical, and no novelty is claimed for Gevrey classes, compactly supported Gevrey bumps, stretched-exponential Fourier decay, Paley-Wiener uncertainty, or integration-by-parts optimization.

- Maurice Gevrey, **“Sur la nature analytique des solutions des équations aux dérivées partielles. Premier mémoire,”** *Annales scientifiques de l'École Normale Supérieure* 35 (1918), 129–190, DOI `10.24033/asens.706`, is the foundational source for Gevrey regularity.
- Luigi Rodino, ***Linear Partial Differential Operators in Gevrey Spaces***, World Scientific (1993), ISBN `9789810208455`, is standard background for compactly supported non-quasianalytic Gevrey classes and their Fourier-decay characterization.
- Elena Cordero, Fabio Nicola, and Luigi Rodino, **“Gabor representations of evolution operators,”** *Transactions of the American Mathematical Society* 367(11) (2015), 7639–7663, DOI `10.1090/S0002-9947-2015-06302-8`, gives modern Gevrey/analytic time-frequency decay estimates and explicitly situates Gevrey regularity as a source of subexponential localization.
- Tamer Tlas, **“Bump functions with monotone Fourier transforms satisfying decay bounds,”** *Journal of Approximation Theory* 278 (2022), 105742, DOI `10.1016/j.jat.2022.105742`, constructs smooth nonnegative compactly supported bumps with two-sided subexponential Fourier-decay bounds and recalls the obstruction to genuinely exponential Fourier decay under compact support.
- AF-185 and AF-186 already use classical Gevrey and ultradifferentiable associated-function theory for adaptive positive source clusters. Their prior-art audit remains the closest internal bridge for the rate optimization used here.

The durable Arithmetic Fidelity content is the specialization to the **same coercivity constant introduced in AF-209**: the positive lower modulus exists at every finite BV budget, yet one fixed-support Gevrey modulation family forces that modulus below `\exp(-cM^\alpha)` for every separately chosen `\alpha<1`. This is a conditioning theorem about the interaction of exact discriminator survival, source-complexity growth, and analytic compression; it is not a novelty claim about Gevrey Fourier analysis.

## Consequences for Arithmetic Fidelity

AF-209--AF-212 now separate four levels that should be audited independently whenever a compression is claimed to preserve a discriminator:

\[
\boxed{
\text{exact injectivity}
\;\not\Rightarrow\;
\text{unrestricted stable recovery}
\;\not\Rightarrow\;
\text{fixed-class coercivity with a useful constant}
\;\not\Rightarrow\;
\text{complexity-uniform conditioning}.
}
\]

For the positive-width Euler band, the first level holds on `L^1`; every fixed BV-complexity slice has the third level; but the constants along those slices can collapse at every stretched-exponential power below one. The source-complexity budget is therefore not a technical side condition. It is part of the mathematical information channel and must be declared together with bandwidth, observation regularity, localization, quotient, and the target discrepancy.

This also sharpens the line's general compression lesson. A transformation may preserve the desired structure **exactly** while still becoming effectively indistinguishable on increasingly complex admissible sources. In that regime the missing object is not necessarily another mark or invariant: it can be a quantitative complexity-to-resolution law strong enough to keep the source away from approximate null directions.