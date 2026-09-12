# FD-075 — power records force growing same-parity large-radical swarms inside protected blocks

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + POWER-RECORD-BACKWARD-MASS + SAME-PARITY-SWARM + LARGE-RADICAL-MULTIPLICITY + FALSE-RH-GROWING-HOST-CLOUD`.

`FD-074` constrains the arithmetic factorization of the strict power-record center itself. The exact record inequality is stronger: when read against every earlier point in an amplitude-length backward window, it forces a positive amount of **signed physical coefficient mass** to accumulate throughout that window. Combining that mass law with

\[
\mathcal H(N)=\sum_{n\le N}c(n),
\qquad
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}{n},
\qquad
|c(n)|\le1,
\]

shows that a large record cannot be supported by one exceptional endpoint alone.

Fix

\[
0<\sigma<1,
\qquad
R_\sigma(n):=\frac{|\mathcal H(n)|}{n^\sigma},
\]

and let `X>=2` be a strict `sigma`-record. Put

\[
A:=|\mathcal H(X)|>0,
\qquad
\varepsilon:=\operatorname{sgn}\mathcal H(X)\in\{-1,1\}.
\]

For every integer `1<=h<X`, define the aligned coefficient set

\[
P_h:=\{n:X-h<n\le X,\ \varepsilon c(n)>0\}.
\]

Then the strict record condition gives the exact lower bound

\[
\boxed{
\sum_{n\in P_h}|c(n)|
>
A\left[1-\left(1-\frac hX\right)^\sigma\right]
\ge
\frac{\sigma Ah}{X}.
}
\tag{1}
\]

Consequently

\[
\boxed{|P_h|>\frac{\sigma Ah}{X}.}
\tag{2}
\]

Thus every strict power record forces many increments with the same squarefree-kernel parity as the record sign, not just the final increment identified by `FD-074`.

There is also a quantitative large-radical refinement. Fix `0<eta<1`, `0<theta<1`, and let `1<=h<=eta A`. Define

\[
Q_{h,\theta}:=
\left\{
\begin{array}{c}
X-h<n\le X:\ \varepsilon c(n)>0,\\[2mm]
\varphi(\operatorname{rad}n)>
\theta\sigma(1-\eta)A
\end{array}
\right\}.
\]

Then

\[
\boxed{
|Q_{h,\theta}|
>
(1-\theta)\frac{\sigma Ah}{X}.
}
\tag{3}
\]

Every `n` in this set satisfies simultaneously

\[
\boxed{
\mu(\operatorname{rad}n)=\varepsilon,
\qquad
\varphi(\operatorname{rad}n)>	heta\sigma(1-\eta)A,
\qquad
\operatorname{rad}n>	heta\sigma(1-\eta)A.
}
\tag{4}
\]

Taking `h=floor(eta A)` once `eta A>=2` therefore yields

\[
\boxed{
|Q_{\lfloor\eta A\rfloor,\theta}|
>
\frac{(1-\theta)\sigma\eta}{2}\frac{A^2}{X}.
}
\tag{5}
\]

Under a false-RH zero frontier `Theta>1/2`, choose fixed

\[
\frac12<\sigma<\Theta.
\]

Along the strict record sequence from `FD-074`, write

\[
A_j=X_j^\sigma R_\sigma(X_j),
\qquad
R_\sigma(X_j)\longrightarrow\infty.
\]

Equation (5) gives a growing arithmetic cloud inside the backward half of the `FD-073` protected block:

\[
\boxed{
|Q_j|
\gg_{\sigma,\eta,\theta}
X_j^{2\sigma-1}R_\sigma(X_j)^2
\longrightarrow\infty.
}
\tag{6}
\]

Uniformly for `n in Q_j`, equations (4) also give

\[
\boxed{
\frac{\operatorname{rad}n}{X_j^\sigma}
\gg_{\sigma,\eta,\theta}R_\sigma(X_j)
\longrightarrow\infty,
\qquad
\frac{n}{\operatorname{rad}n}
=o(X_j^{1-\sigma}).
}
\tag{7}
\]

All these points lie in `|n-X_j|<=eta A_j`; hence `FD-073` simultaneously makes each one a quantitative near-record and gives its recentered horizon `T=4n`, `D=3` a uniform positive nonsquarefree occupation and Schur defect. A false-RH power record therefore creates not one arithmetically admissible causal anchor but a diverging collection of same-parity, large-radical anchors inside one protected source block.

This still does **not** prove global recurrence. The guaranteed cloud has relative density only of order `A/X` inside a block of length order `A`, and that ratio may tend to zero. The blocks themselves may also remain multiplicatively sparse. The gain over `FD-074` is different: the exact physical coefficient law now constrains a growing number of points inside every supercritical record block, so a negative spacing model must reproduce a whole local parity/radical cloud rather than merely place isolated record centers on eligible large-radical integers.

## 1. A strict record forces signed mass in every backward window

Because `X` is a strict `sigma`-record, for every `1<=h<X`,

\[
\frac{|\mathcal H(X-h)|}{(X-h)^\sigma}
<
\frac{A}{X^\sigma}.
\]

Therefore

\[
|\mathcal H(X-h)|
<
A\left(1-\frac hX\right)^\sigma.
\tag{8}
\]

Multiply the source increment over `(X-h,X]` by the record sign:

\[
\begin{aligned}
\varepsilon\sum_{X-h<n\le X}c(n)
&=\varepsilon\bigl(\mathcal H(X)-\mathcal H(X-h)\bigr)\\
&=A-\varepsilon\mathcal H(X-h)\\
&\ge A-|\mathcal H(X-h)|.
\end{aligned}
\]

Using (8),

\[
\varepsilon\sum_{X-h<n\le X}c(n)
>
A\left[1-\left(1-\frac hX\right)^\sigma\right].
\tag{9}
\]

For `0<sigma<1`, concavity gives

\[
\left(1-\frac hX\right)^\sigma
\le
1-\frac{\sigma h}{X},
\]

so

\[
\boxed{
\varepsilon\sum_{X-h<n\le X}c(n)
>
\frac{\sigma Ah}{X}.
}
\tag{10}
\]

The anti-aligned coefficients have `epsilon c(n)<0` and can only decrease the left side of (10). Hence the aligned absolute mass alone is larger than the same lower bound, proving (1). Since every physical coefficient has absolute value at most one, (2) follows immediately.

For `h=1`, this recovers the qualitative endpoint phenomenon behind `FD-074`; for larger `h`, it shows that the endpoint restriction is only the first member of a nested family of signed-mass constraints.

## 2. Most of the forced signed mass cannot come from small radicals

Fix `eta,theta in (0,1)` and `1<=h<=eta A`. Since `|c(n)|<=1` and `mathcal H(0)=0`, one has `A<=X`. Therefore

\[
h\le\eta A\le\eta X,
\]

and every `n in (X-h,X]` satisfies

\[
n\ge X-h\ge(1-\eta)X.
\tag{11}
\]

Split the aligned set `P_h` into coefficients above and below the totient threshold

\[
\theta\sigma(1-\eta)A.
\]

If an aligned `n` lies below this threshold, then by (11)

\[
|c(n)|
=
\frac{\varphi(\operatorname{rad}n)}{n}
\le
\frac{\theta\sigma(1-\eta)A}{(1-\eta)X}
=
\frac{\theta\sigma A}{X}.
\tag{12}
\]

There are at most `h` such coefficients, so their total aligned mass is at most

\[
\frac{\theta\sigma Ah}{X}.
\tag{13}
\]

Subtracting (13) from the forced aligned mass in (1) leaves strictly more than

\[
(1-\theta)\frac{\sigma Ah}{X}
\]

of aligned mass on coefficients whose totient-radical value exceeds the threshold. Because each such coefficient again has absolute value at most one, their number exceeds the same quantity. This proves (3).

For each `n in Q_(h,theta)`, alignment gives

\[
\operatorname{sgn}c(n)=\varepsilon.
\]

The coefficient formula has positive magnitude factor `phi(rad n)/n`, so

\[
\mu(\operatorname{rad}n)=\varepsilon=(-1)^{\omega(n)}.
\]

The totient and radical bounds in (4) are then immediate. Thus the conclusion is genuinely arithmetic: the forced mass cannot be supplied by arbitrary one-Lipschitz increments of the correct sign.

## 3. Supercritical records create diverging arithmetic host clouds

Assume `Theta>1/2` and fix `1/2<sigma<Theta`. By `FD-046` and `FD-074`, there is a strict record sequence `X_j` for which

\[
R_\sigma(X_j)\to\infty.
\]

Set

\[
A_j=|\mathcal H(X_j)|=X_j^\sigma R_\sigma(X_j).
\]

For fixed `eta in (0,1)`, eventually `eta A_j>=2`; then

\[
h_j:=\lfloor\eta A_j\rfloor\ge\frac{\eta A_j}{2}.
\]

Applying (3) gives

\[
|Q_j|
>
\frac{(1-\theta)\sigma\eta}{2}
\frac{A_j^2}{X_j}
=
\frac{(1-\theta)\sigma\eta}{2}
X_j^{2\sigma-1}R_\sigma(X_j)^2,
\]

which tends to infinity because `2sigma-1>0`. This proves (6).

For every point in the cloud,

\[
\operatorname{rad}n
>
\theta\sigma(1-\eta)A_j
=
\theta\sigma(1-\eta)X_j^\sigma R_\sigma(X_j),
\]

proving the first statement in (7). Since `n<=X_j`,

\[
\frac{n}{\operatorname{rad}n}
<
\frac{X_j^{1-\sigma}}
{\theta\sigma(1-\eta)R_\sigma(X_j)}
=o(X_j^{1-\sigma}),
\]

which proves the second.

This extends the endpoint statement of `FD-074` in the direction its falsification boundary left open: large-radical arithmetic is forced at a diverging number of interior block points, not solely at the strict record center.

## 4. Coupling to the causal occupation mechanism

`FD-073` proves that, for every fixed `eta<1`, every integer `Y` satisfying

\[
|Y-X_j|\le\eta A_j
\]

is a quantitative `sigma`-near-record, with a lower-quality factor depending only on `eta` and `sigma`. For `sigma>1/2`, its recentered causal horizon `T=4Y`, `D=3` therefore has a uniform positive lower bound for the nonsquarefree Jordan occupation and the associated Schur defect.

The cloud `Q_j` lies entirely in the backward part of exactly that interval. Hence `FD-073` and the present result can be imposed simultaneously: every `n in Q_j` is both an arithmetically constrained coefficient host and a protected causal observation point.

This coupling is stronger than either input separately. `FD-073` alone allows all interior points to be treated as abstract one-Lipschitz near-records with no factorization information. `FD-074` alone constrains one endpoint but permits the rest of the protected block to be arithmetically arbitrary. Equations (3)--(7) show that the actual source forces a growing set where both structures coexist.

The natural next recurrence question is therefore no longer only whether record centers with `rad X >> A` can be sparse. A countermechanism must permit arbitrarily sparse amplitude-length protected blocks while, inside each block, accommodating at least order `A^2/X` indices of one fixed distinct-prime parity whose radicals are order `A` or larger. Whether this local multiplicity can be converted into logarithmic recurrence remains open.

## 5. Falsification and prior-art boundary

The proof uses only the exact physical coefficient law, the strict normalized-record inequality, and the already-established causal block theorem. No new external theorem is load-bearing. A targeted literature search around normalized records of summatory multiplicative functions and correlations between Möbius-type coefficients and their partial sums found neighboring work, but no result matching the source-specific implication (3)--(7). No priority claim is made from that search, and `SOURCES.md` does not need a new anchor.

Several stronger-looking statements are **not** proved here. The cloud need not have positive relative density inside its protected block: dividing (5) by a block length of order `A` leaves only order `A/X`, which may tend to zero. Nothing bounds the multiplicative gaps between successive strict records or between their blocks. The argument gives no uniform lower bound for `U_(H,D)/E_(H,D)` at arbitrary horizons, no improvement of the zeta-zero exponent, and no RH implication.

The exact durable content is narrower: every strict power record forces signed physical coefficient mass in every backward window; on any fixed amplitude-scale backward window, a fixed fraction of that forced mass must be carried by same-parity coefficients with totient-radical size comparable with the record amplitude; and under a false-RH frontier the resulting number of protected large-radical causal anchors diverges polynomially in the record scale.
