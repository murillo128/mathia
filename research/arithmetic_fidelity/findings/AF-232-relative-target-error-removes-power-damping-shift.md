# AF-232 — relative target error removes the power-damping information shift

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-FRAMEWORK-SPECIALIZATION`, `QUANTITATIVE-FIDELITY`, `TARGET-METRIC`, `RATE-DISTORTION`, `RELATIVE-ERROR`, `EULER-ATOM`, `PHASE-LAW`, `NO-NOVELTY-CLAIM`

## Claim

AF-231 shows that a power-decaying target can be much cheaper than source localization when fidelity is measured in **absolute target error**. That saving is not intrinsic to the observable: a scale-normalized target metric removes the damping shift completely.

Let

\[
\mathcal P_Q:=\{p\le Q:p\text{ prime}\},
\qquad
n_Q:=\pi(Q),
\]

and let `P_Q` be uniform on `\mathcal P_Q`. Let

\[
f:[2,\infty)\to(0,\infty)
\]

be strictly monotone and `C^1`. Assume that for constants `0<c_-\le c_+<\infty`,

\[
\frac{c_-}{x}
\le
\left|\frac{f'(x)}{f(x)}\right|
\le
\frac{c_+}{x}
\qquad(x\ge2).
\tag{1}
\]

Thus the logarithmic target coordinate

\[
g(x):=\log f(x)
\tag{2}
\]

has derivative comparable to `1/x`.

For `r>0` and `0\le\delta<1`, define the logarithmic-target information price

\[
\mathcal R^{\log f}_Q(r,\delta)
:=
\inf I(P_Q;M),
\tag{3}
\]

where the infimum is over arbitrary finite-valued stochastic marks and positive decoders `d` satisfying

\[
\Pr\!\left\{
|\log f(P_Q)-\log d(M)|>r
\right\}
\le\delta.
\tag{4}
\]

Let `r_Q>0`, `\delta_Q\to\delta\in[0,1)`, and suppose

\[
\beta_Q
:=
\frac{\log^+(1/r_Q)}{\log Q}
\longrightarrow
\beta\in[0,\infty].
\tag{5}
\]

Then

\[
\boxed{
\frac{\mathcal R^{\log f}_Q(r_Q,\delta_Q)}
{\log\pi(Q)}
\longrightarrow
(1-\delta)\min\{\beta,1\}.
}
\tag{6}
\]

The phase is therefore **unshifted**: it depends on the requested multiplicative resolution, not on the power amplitude decay of `f`.

The same law holds for ordinary relative target error. For `0<\varepsilon<1`, define

\[
\mathcal R^{\mathrm{rel},f}_Q(\varepsilon,\delta)
:=
\inf I(P_Q;M)
\tag{7}
\]

under

\[
\Pr\!\left\{
|f(P_Q)-d(M)|>\varepsilon f(P_Q)
\right\}
\le\delta.
\tag{8}
\]

If `\varepsilon_Q\to0`, `\delta_Q\to\delta`, and

\[
\gamma_Q
:=
\frac{\log(1/\varepsilon_Q)}{\log Q}
\longrightarrow
\gamma\in[0,\infty],
\tag{9}
\]

then

\[
\boxed{
\frac{\mathcal R^{\mathrm{rel},f}_Q(\varepsilon_Q,\delta_Q)}
{\log\pi(Q)}
\longrightarrow
(1-\delta)\min\{\gamma,1\}.
}
\tag{10}
\]

For the Euler-log atom

\[
e_a(x):=-\log(1-x^{-a}),
\qquad a>0,
\tag{11}
\]

condition `(1)` holds. Hence AF-231 and `(10)` give two different phase laws for the **same arithmetic observable**:

\[
\frac{\mathcal R^{\mathrm{abs},e_a}_Q(Q^{-\gamma+o(1)},\delta)}
{\log\pi(Q)}
\to
(1-\delta)\min\{(\gamma-a)_+,1\},
\tag{12}
\]

while

\[
\frac{\mathcal R^{\mathrm{rel},e_a}_Q(Q^{-\gamma+o(1)},\delta)}
{\log\pi(Q)}
\to
(1-\delta)\min\{\gamma,1\}.
\tag{13}
\]

Thus the apparent information saving from tail damping disappears when the fidelity criterion measures error relative to the local target scale.

## Derivation

### 1. Logarithmic target geometry has source-scale derivative

By `(1)` and `(2)`,

\[
\frac{c_-}{x}
\le
|g'(x)|
\le
\frac{c_+}{x}.
\tag{14}
\]

Because `f` is positive and strictly monotone, `g` is also strictly monotone and is injective on the prime source. Exact `g(P_Q)` therefore retains exact prime identity; only the declared approximation metric creates compression fibers.

Define the maximal `g`-occupancy

\[
N^g_Q(t)
:=
\max_{y\in\mathbb R}
\#\{p\in\mathcal P_Q:g(p)\in[y,y+t]\}.
\tag{15}
\]

If `p<q\le Q` lie in one interval of `g`-length `t`, the mean-value theorem and the lower bound in `(14)` give

\[
t
\ge
|g(q)-g(p)|
\ge
\frac{c_-}{Q}(q-p).
\tag{16}
\]

Hence

\[
\boxed{
N^g_Q(t)
\le
\min\!\left\{
 n_Q,
 1+\frac{tQ}{c_-}
\right\}.
}
\tag{17}
\]

This is the key cancellation: the power amplitude of `f` has vanished after taking the logarithmic target coordinate.

### 2. Occupancy gives the stochastic converse

The Fano/occupancy argument used in AF-230 and AF-231 is independent of the particular target coordinate. Applied to `g(P_Q)`, every channel satisfying `(4)` obeys

\[
\mathcal R^{\log f}_Q(r,\delta)
\ge
\left[
(1-\delta)
\bigl(\log n_Q-\log N^g_Q(2r)\bigr)
-\log2
\right]_+.
\tag{18}
\]

By the prime number theorem,

\[
\log n_Q=\log Q+o(\log Q).
\tag{19}
\]

If `r_Q=Q^{-\beta+o(1)}`, `(17)` gives

\[
\log N^g_Q(2r_Q)
\le
(1-\min\{\beta,1\})\log Q+o(\log Q),
\tag{20}
\]

with the natural `o(\log Q)` interpretation at `\beta=0` and `\beta=1`. Substitution into `(18)` yields

\[
\liminf_{Q\to\infty}
\frac{\mathcal R^{\log f}_Q(r_Q,\delta_Q)}{\log n_Q}
\ge
(1-\delta)\min\{\beta,1\}.
\tag{21}
\]

### 3. A multiplicative-scale quantizer gives the matching upper bound

For `\beta<1`, choose

\[
A_Q:=\frac{Q}{\log Q},
\qquad
\alpha_Q:=\Pr\{P_Q<A_Q\}.
\tag{22}
\]

PNT gives `\alpha_Q\to0`. Encode every prefix prime below `A_Q` exactly. On `[A_Q,Q]`, divide the ordinary source coordinate into intervals of length at most

\[
L_Q:=\frac{r_QA_Q}{c_+}.
\tag{23}
\]

For `p,q` in one such tail cell, `(14)` gives

\[
|g(p)-g(q)|
\le
\frac{c_+}{A_Q}|p-q|
\le r_Q.
\tag{24}
\]

Thus one representative target value per cell achieves zero logarithmic-target error at radius `r_Q`. The number of tail cells satisfies

\[
J_Q
\le
1+\frac{Q}{L_Q}
=
1+\frac{c_+\log Q}{r_Q}.
\tag{25}
\]

Let `Z_Q` be the resulting deterministic zero-error mark. Then

\[
H(Z_Q)
\le
h(\alpha_Q)
+\alpha_Q\log\pi(A_Q)
+(1-\alpha_Q)\log J_Q,
\tag{26}
\]

so

\[
\limsup_{Q\to\infty}
\frac{H(Z_Q)}{\log n_Q}
\le\beta
\qquad(\beta<1).
\tag{27}
\]

For `\beta\ge1`, use the exact identity mark `Z_Q=P_Q`, whose entropy is `\log n_Q`. As in AF-230/AF-231, an independent erasure of probability `\delta_Q` spends the allowed failure budget and multiplies the first-order mutual information by `1-\delta_Q`. Therefore

\[
\limsup_{Q\to\infty}
\frac{\mathcal R^{\log f}_Q(r_Q,\delta_Q)}{\log n_Q}
\le
(1-\delta)\min\{\beta,1\}.
\tag{28}
\]

Together with `(21)`, this proves `(6)`.

### 4. Relative error is squeezed between two logarithmic radii

For `0<\varepsilon<1`, define

\[
r_-(\varepsilon):=\log(1+\varepsilon),
\qquad
r_+(\varepsilon):=-\log(1-\varepsilon).
\tag{29}
\]

If

\[
|f-d|\le\varepsilon f,
\tag{30}
\]

then

\[
1-\varepsilon\le\frac d f\le1+\varepsilon,
\]

so

\[
|\log d-\log f|\le r_+(\varepsilon).
\tag{31}
\]

Conversely, if

\[
|\log d-\log f|\le r_-(\varepsilon),
\tag{32}
\]

then

\[
\frac1{1+\varepsilon}
\le
\frac d f
\le
1+\varepsilon,
\]

which implies `|f-d|\le\varepsilon f`. Hence

\[
\boxed{
\mathcal R^{\log f}_Q(r_+(\varepsilon),\delta)
\le
\mathcal R^{\mathrm{rel},f}_Q(\varepsilon,\delta)
\le
\mathcal R^{\log f}_Q(r_-(\varepsilon),\delta).
}
\tag{33}
\]

As `\varepsilon\downarrow0`, both `r_-(\varepsilon)` and `r_+(\varepsilon)` are `\varepsilon(1+o(1))`. Therefore the two bounding logarithmic problems have the same exponent in `(5)`, and `(10)` follows from `(6)` by squeezing.

### 5. Euler-log atoms satisfy the logarithmic-derivative gate

Put `u=x^{-a}`. Then

\[
|e_a'(x)|
=
\frac{a x^{-a-1}}{1-x^{-a}},
\tag{34}
\]

and therefore

\[
\frac{|e_a'(x)|}{e_a(x)}
=
\frac a x
\frac{u}{(1-u)(-\log(1-u))}.
\tag{35}
\]

For `0<u<1`,

\[
u\le-\log(1-u)\le\frac{u}{1-u},
\tag{36}
\]

so

\[
1
\le
\frac{u}{(1-u)(-\log(1-u))}
\le
\frac1{1-u}.
\tag{37}
\]

Since `u\le2^{-a}` for `x\ge2`,

\[
\frac a x
\le
\frac{|e_a'(x)|}{e_a(x)}
\le
\frac{a}{(1-2^{-a})x}.
\tag{38}
\]

Thus `(1)` holds with `c_-=a` and `c_+=a/(1-2^{-a})`, proving `(13)`.

## Exact controls and boundaries

### The observable did not become more informative

Both absolute and relative criteria act on the same injective target `f(P_Q)`. Exact target recovery always carries the full prime identity. Equations `(12)`--`(13)` differ because their distortion balls induce different compression fibers, not because the underlying target changed.

This is a direct Arithmetic Fidelity warning: an information price is meaningful only together with the **declared target geometry**. Comparing bit or entropy costs across two distortion metrics without accounting for their induced fibers can manufacture or erase an apparent compression advantage.

### Relative error is a source-scale metric here

Condition `(1)` says that logarithmic target distance is bi-Lipschitz, up to constants, with logarithmic source distance. Infinitesimally,

\[
|d\log f(x)|\asymp \frac{|dx|}{x}.
\tag{39}
\]

Therefore relative target tolerance `\varepsilon` corresponds to source uncertainty of order `\varepsilon x`, which restores the same polynomial occupancy exponent as direct multiplicative localization of the source.

This is the exact mechanism behind the phase reset; no special property of Euler products is required.

### The theorem is not rational-prime-specific

As in AF-231, primality enters only through global source entropy and the vanishing-prefix fact used by the tail quantizer. The same phase holds for the uniform integer control and for broad discrete sources of comparable cardinality with an analogous negligible prefix.

Consequently `(13)` is a metric-calibration control, not a prime discriminator and not evidence for RH.

### The theorem is first-order only

The result identifies the coefficient of `\log\pi(Q)`. It does not optimize finite-`Q` stochastic channels or lower-order terms. Actual prime gaps, exact target curvature, and a more efficient nonuniform quantizer can affect those terms without changing the phase in `(6)` or `(10)`.

### Global arithmetic aggregation remains separate

The Euler specialization still concerns reproduction of one random prime atom `e_a(P_Q)`. It does not price a whole Euler product, accumulated prime sum, explicit formula, zero divisor, analytic continuation, or any RH-facing global sufficient statistic. A global application must define its own target and distortion geometry before importing either the absolute or relative phase law.

## Prior art and novelty assessment

Claude E. Shannon, **“Coding Theorems for a Discrete Source With a Fidelity Criterion,”** *IRE National Convention Record* 7 (1959), 142--163, is the classical origin of mutual-information minimization under a fidelity criterion. The reductions in `(3)` and `(7)` are ordinary single-letter rate-distortion problems.

Tamás Linder and Ram Zamir, **“High-Resolution Source Coding for Non-Difference Distortion Measures: The Rate-Distortion Function,”** *IEEE Transactions on Information Theory* 45(2) (1999), 533--547, DOI `10.1109/18.749001`, develop rate-distortion asymptotics for source-dependent/non-difference distortion measures and explicitly show that local distortion geometry changes high-resolution information cost. This is close conceptual prior art for the metric-dependence emphasized here.

Bernard Smith, **“Instantaneous Companding of Quantized Signals,”** *Bell System Technical Journal* 36(3) (1957), 653--709, DOI `10.1002/j.1538-7305.1957.tb03858.x`, is classical prior art for changing quantization geometry through nonlinear, including logarithmic-type, companding coordinates.

No novelty is claimed for rate-distortion theory, logarithmic companding, relative-error/log-coordinate equivalence, or source-dependent distortion geometry. The line-specific result is the exact prime-cutoff first-order phase `(6)`--`(13)` and its controlled comparison with AF-231: the same decaying Euler atom is cheap under absolute error but loses that power-decay discount under relative error.

## Research consequence

AF-231 established that target-specific contraction can reduce the first-order information bill. AF-232 shows the complementary obstruction: **the bill is not an invariant of the target alone**. It is an invariant of the target together with its operational fidelity geometry.

Any proposed RH-facing compression that claims a gain because prime contributions become small must therefore state why the destination problem naturally uses an absolute metric rather than a scale-normalized one. Conversely, if the downstream sufficient statistic is naturally relative or logarithmic, power damping by itself supplies no first-order information discount.