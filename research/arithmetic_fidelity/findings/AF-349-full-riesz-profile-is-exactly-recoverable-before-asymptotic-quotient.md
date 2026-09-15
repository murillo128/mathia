# AF-349 — the full Riesz cutoff profile is exactly recoverable before the asymptotic quotient

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `SOURCE-COMPLEXITY-CONSERVATION`, `BOUNDARY-CLARIFICATION`, `STABILITY-CLARIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-347--AF-348 show that, for the weighted perfect-`k`-power background, sufficiently high fixed-order Riesz smoothing makes the sparse background and dense unit mass differ by only `O(1)` uniformly in the cutoff. That is a real loss of **polynomial-scale asymptotic visibility**, but it does not mean that the full Riesz cutoff profile has destroyed the source coefficients.

For a coefficient sequence `a=(a_n)_{n>=1}` and integer `r>=0`, define the full order-`r` Riesz profile

\[
\mathcal R_r[a](X)
:=
\sum_{n\le X}a_n\left(1-\frac nX\right)^r,
\qquad X>0,
\tag{1}
\]

with the usual step-function interpretation at `r=0`. Then the map

\[
a\longmapsto \bigl(X\mapsto \mathcal R_r[a](X)\bigr)
\tag{2}
\]

is injective for every fixed finite `r`.

More precisely, set

\[
F_r[a](X):=X^r\mathcal R_r[a](X).
\tag{3}
\]

As a locally finite distribution on `(0,\infty)`,

\[
F_r[a](X)
=
\sum_{n\ge1}a_n(X-n)_+^r,
\tag{4}
\]

and therefore

\[
\boxed{
D^{r+1}F_r[a]
=
r!\sum_{n\ge1}a_n\,\delta_n.
}
\tag{5}
\]

Equivalently, the `r`-th derivative of `F_r[a]` has a jump of size `r!a_n` at `X=n`. Hence every coefficient is exactly recoverable from the complete cutoff profile.

This recovery has an exact finite-horizon stability metric. For two sources `a,b`, put `c=a-b`. For every integer `N>=1`,

\[
\boxed{
\operatorname{TV}_{(0,N+1/2)}\!\left(D^rF_r[c]\right)
=
r!\sum_{n\le N}|c_n|.
}
\tag{6}
\]

Thus the full Riesz map is an isometry, up to the fixed factor `r!`, from local coefficient `\ell^1` distance into the total variation of the `r`-th derivative of the scaled profile. Stability is therefore not intrinsically lost by the smoothing map; it depends on the metric retained at the destination.

There is a second exact recovery bridge in the Dirichlet/Mellin category. If

\[
A(s):=\sum_{n\ge1}\frac{a_n}{n^s}
\tag{7}
\]

converges absolutely at `s`, with `Re(s)>0`, then absolute interchange gives

\[
\boxed{
\int_0^\infty
\mathcal R_r[a](X)X^{-s-1}\,dX
=
B(s,r+1)A(s),
}
\tag{8}
\]

where

\[
B(s,r+1)
=
\frac{\Gamma(s)\Gamma(r+1)}{\Gamma(s+r+1)}
=
\frac{r!}{s(s+1)\cdots(s+r)}.
\tag{9}
\]

The beta factor has no zero in `Re(s)>0`, so the Dirichlet transform is recoverable there:

\[
\boxed{
A(s)
=
\frac{s(s+1)\cdots(s+r)}{r!}
\int_0^\infty
\mathcal R_r[a](X)X^{-s-1}\,dX.
}
\tag{10}
\]

Thus fixed-order Riesz smoothing separates into two mathematically different operations:

\[
\text{coefficients}
\xrightarrow{\text{full cutoff profile}}
\mathcal R_r[a](\cdot)
\xrightarrow{\text{coarse asymptotic readout}}
\text{leading/error class}.
\tag{11}
\]

The first arrow is faithful, and it is quantitatively exact in the derivative-variation metric `(6)`. The loss exhibited by AF-347--AF-348 occurs only after the destination forgets the fine cutoff dependence, for example by retaining only a leading term modulo a declared error class.

This locates the information-loss stage exactly: **finite Riesz smoothing is not intrinsically a lossy compression when its entire cutoff profile is retained; the lossy operation is the subsequent scalarization, weak target metric, or asymptotic quotient.**

## Derivation

### 1. Local coefficient recovery from truncated powers

Multiplying `(1)` by `X^r` gives, away from irrelevant endpoint conventions,

\[
F_r[a](X)
=
\sum_{n\le X}a_n(X-n)^r
=
\sum_{n\ge1}a_n(X-n)_+^r.
\tag{12}
\]

Only finitely many summands meet any compact interval, so the sum is locally finite as a distribution. The standard truncated-power identity is

\[
D^{r+1}(X-n)_+^r=r!\,\delta_n.
\tag{13}
\]

Applying `(13)` term by term gives `(5)`. No growth, convergence, positivity, or arithmetic hypothesis on `a_n` is required beyond local finiteness of the integer support.

For `r>=1`, an equivalent classical reading avoids the final distributional derivative: `D^rF_r[a]` is piecewise constant and its jump across `X=n` is exactly `r!a_n`. For `r=0`, `F_0[a]` is the ordinary cumulative step function and its jump is `a_n`.

Therefore

\[
\mathcal R_r[a]=\mathcal R_r[b]\text{ for all }X>0
\quad\Longrightarrow\quad
a_n=b_n\text{ for every }n.
\tag{14}
\]

The full cutoff profile is an exact encoding, not merely a statistic with a small kernel.

### 2. The same jump identity gives an exact recovery norm

Let `c=a-b`. Since `D^rF_r[c]` is the right-continuous step function whose jump at `n` is `r!c_n`, its total variation on a finite interval containing exactly the jumps `1,...,N` is the sum of the jump magnitudes:

\[
\operatorname{TV}_{(0,N+1/2)}\!\left(D^rF_r[c]\right)
=
r!\sum_{n\le N}|c_n|.
\tag{15}
\]

This includes `r=0`, where `F_0[c]` itself is the cumulative step function. For complex coefficients, total variation is still the sum of the moduli of the atomic jumps, so the same formula holds.

Define on Riesz-image profiles the finite-horizon seminorm

\[
\|G\|_{r,\mathrm{var};N}
:=
\frac1{r!}
\operatorname{TV}_{(0,N+1/2)}
\!\left(D^r[X^rG(X)]\right).
\tag{16}
\]

Then `(15)` becomes the exact identity

\[
\boxed{
\|\mathcal R_r[a]-\mathcal R_r[b]\|_{r,\mathrm{var};N}
=
\sum_{n\le N}|a_n-b_n|.
}
\tag{17}
\]

So the inverse is perfectly conditioned in the source-matched metric `(16)`. The warning that coefficient recovery differentiates the profile and may amplify perturbations is correct only relative to weaker observation topologies that do not control this derivative variation.

### 3. Mellin recovery of the Dirichlet series

Assume `sum_n |a_n|n^{-sigma}<infinity` for `sigma=Re(s)>0`. For one coefficient `a_n`, substitute `u=n/X` in the cutoff integral:

\[
\begin{aligned}
\int_n^\infty
\left(1-\frac nX\right)^r X^{-s-1}\,dX
&=
n^{-s}\int_0^1(1-u)^r u^{s-1}\,du\\
&=
n^{-s}B(s,r+1).
\end{aligned}
\tag{18}
\]

Absolute convergence permits summation under the integral, yielding

\[
\int_0^\infty \mathcal R_r[a](X)X^{-s-1}\,dX
=
B(s,r+1)\sum_{n\ge1}a_n n^{-s},
\tag{19}
\]

which is `(8)`. For integer `r`, the gamma recurrence gives `(9)`, and division by the nonzero beta factor gives `(10)`.

This is the forward-Mellin counterpart of the classical Perron/Riesz contour formula: typical Riesz means are obtained from a Dirichlet series by an inverse Mellin kernel, and integrating the complete profile against the dual Mellin character recovers the Dirichlet series.

### 4. The AF-348 power control separates the weak and strong destination metrics

For the weighted perfect-`k`-power background from AF-344--AF-348,

\[
b_k(n)=
\begin{cases}
km^{k-1},&n=m^k,\ m\ge2,\\
0,&\text{otherwise},
\end{cases}
\tag{20}
\]

its Dirichlet transform is

\[
B_k(s)=k\bigl(\zeta(ks-k+1)-1\bigr).
\tag{21}
\]

Dense unit mass `u(n)=1` has transform `\zeta(s)`. Thus, for `Re(s)>1`,

\[
\int_0^\infty
\bigl(\mathcal R_r[b_k](X)-\mathcal R_r[u](X)\bigr)
X^{-s-1}\,dX
=
B(s,r+1)
\left[
 k\bigl(\zeta(ks-k+1)-1\bigr)-\zeta(s)
\right].
\tag{22}
\]

The bracket is not identically zero; for example it tends to `-1` as `Re(s)->+infinity`. Therefore the complete Riesz profiles remain different for every finite `r`.

AF-348 proves simultaneously that for `r>=k-1`,

\[
\mathcal R_r[b_k](X)-\mathcal R_r[u](X)=O_{k,r}(1)
\tag{23}
\]

uniformly as `X->infinity`. In fact the residual is globally bounded on `X>=1` after enlarging the constant to cover the initial compact range.

Now put

\[
c_k(n):=b_k(n)-1,
\qquad
M:=\lfloor N^{1/k}\rfloor.
\tag{24}
\]

Among `1,...,N`, every non-`k`-th power contributes `1` to `|c_k(n)|`, while at `n=m^k`, `m>=2`, the contribution is `km^{k-1}-1`. Hence exactly

\[
\begin{aligned}
\sum_{n\le N}|c_k(n)|
&=N-2M+2+k\sum_{m=2}^{M}m^{k-1}\\
&=2N+O_k\!\left(N^{1-1/k}\right),
\end{aligned}
\tag{25}
\]

where the last step is the standard power-sum estimate together with `N-M^k=O_k(M^{k-1})`.

Combining `(17)`, `(23)`, and `(25)`, for every fixed `r>=k-1`,

\[
\boxed{
\sup_{1\le X\le N+1/2}
|\mathcal R_r[b_k](X)-\mathcal R_r[u](X)|
=O_{k,r}(1),
}
\tag{26}
\]

while

\[
\boxed{
\|\mathcal R_r[b_k]-\mathcal R_r[u]\|_{r,\mathrm{var};N}
=
2N+O_k\!\left(N^{1-1/k}\right).
}
\tag{27}
\]

Thus the same transformed residual is uniformly bounded in the raw amplitude metric while its source-matched derivative-variation norm grows linearly and asymptotically saturates the order-`N` coefficient discrepancy. There is no `N`-independent inverse modulus from the raw `C^0` profile norm to local coefficient `\ell^1` on this control family, whereas `(17)` is an exact isometry in the stronger metric.

This is the quantitative content missing from injectivity alone: **conditioning belongs to the pair (representation, destination metric), not to the representation in isolation.**

## Exact fidelity factorization

AF-348 can now be sharpened conceptually without changing its theorem. Let `\mathscr P_r` denote the space of full cutoff profiles and let `\mathscr B` denote bounded functions on `[1,\infty)`. On the power-background comparison with `r>=k-1`, the relevant map factors as

\[
a
\xrightarrow{\;R_r\;}
\mathcal R_r[a](\cdot)
\xrightarrow{\;Q\;}
[\mathcal R_r[a]]\in\mathscr P_r/\mathscr B.
\tag{28}
\]

The first map is injective by `(5)` and is exactly stable in the derivative-variation metric `(16)`. The second map is not faithful to the dense-versus-power discriminator because `(23)` gives

\[
Q(\mathcal R_r[b_k])=Q(\mathcal R_r[u]).
\tag{29}
\]

So the exact kernel responsible for the AF-348 example is introduced by `Q`, not by `R_r`. Equations `(26)`--`(27)` add that even before taking the literal quotient, a destination using only raw amplitude has no uniform coefficient-recovery modulus on this family.

The same warning applies to any destination that observes only a normalization such as `\mathcal R_r(X)/X`, only finitely many asymptotic coefficients, or only membership in a coarse error class. A smoothing operator may regularize a source while remaining mathematically invertible; information is lost only when a later observer identifies profiles that the inverse would distinguish, and stable information is lost when the observer's metric is too weak to control the inverse.

## Relation to AF-209 and AF-347--AF-348

AF-209 already separates exact injectivity from stable recovery for positive-width Euler bands: a normalized precompact/BV-bounded source class restores a uniform inverse modulus after high-complexity approximate-null directions are excluded. AF-349 supplies the complementary Riesz phenomenon. Here the full transform admits an exact source-matched norm identity on the unrestricted locally finite coefficient class, but that strong metric is not what the AF-348 asymptotic observer retains.

AF-347 and AF-348 therefore remain correct. Their exact estimates prove that raw support locality is unavailable to a theorem whose declared observable identifies all bounded residual profiles after enough smoothing.

AF-349 narrows the causal statement further. It is not enough to say that "Riesz smoothing erases locality" without specifying both the destination object and its metric. At full-profile resolution the smoothing is faithful. In the derivative-variation metric it is even exactly conditioned. In raw amplitude, the power controls remain `O(1)` apart while carrying `Theta(N)` local coefficient distance. The demonstrated collapse occurs at **polynomial/asymptotic resolution** because the sparse and dense outputs enter the same bounded-error class.

This distinction is important for the line's current source-resource program. A candidate source functional should not be rejected merely because a smoothing stage reduces its visible magnitude. One must ask whether the actual destination keeps the whole transformed object, a norm controlling the residual, or only a quotient that kills it. Conversely, exact invertibility of the smoothing stage is not useful if the final RH theorem consumes only the coarse quotient.

## Prior art and novelty assessment

No novelty claim is made for Riesz means, the Perron/Mellin kernel, truncated-power differentiation, total variation of step functions, or Dirichlet-series uniqueness.

- Marcel Riesz, **“Une méthode de sommation équivalente à la méthode des moyennes arithmétiques,”** *Comptes rendus de l’Académie des sciences* 152 (1911), 1651–1654, is the classical source for Riesz summation/typical means.
- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41, 119–196, DOI `10.1007/BF02422942`, use Riesz means in the analytic-number-theory setting and connect them to zeta/prime-distribution questions.
- Ingo Schoolmann, **“On Bohr's theorem for general Dirichlet series,”** *Mathematische Nachrichten* 293(8), 1591–1612 (2020), DOI `10.1002/mana.201800542`, explicitly treats approximation by typical Riesz means for general Dirichlet series and derives the relevant Perron-type representation.
- Standard BV calculus identifies the total variation of a step function with the sum of the magnitudes of its jumps; AF-209 already uses the same bounded-variation framework for a different Euler-band stability gate.

The Mellin identity `(8)` is the direct forward transform of the classical Riesz kernel, `(5)` is the elementary truncated-power recovery identity, and `(6)` is its immediate total-variation consequence. The Arithmetic Fidelity contribution is not a new spline or BV theorem. It is the calibrated comparison against AF-348's matched control: the same transformed object is exactly faithful in one natural strong metric and uniformly coarse in the metric used by the asymptotic quotient.

## Boundaries and failure modes

### Full-profile access in the strong metric is a demanding observation model

Injectivity requires access to the complete function `X->R_r[a](X)` with exact cutoff resolution. The exact isometry `(17)` requires enough regularity of the observation model to control the variation of `D^r[X^rG(X)]`. Sampling the profile on a sparse cutoff set, retaining only asymptotic coefficients, adding noise controlled only in `C^0`, or passing to a weak norm/quotient can destroy stable or exact recovery.

### Stability is target-metric-relative

Equation `(17)` shows that recovery is perfectly conditioned in the derivative-variation metric, while `(26)`--`(27)` show that the inverse has no uniform `C^0`-to-local-`ell^1` modulus on the power controls. Therefore the earlier generic warning that differentiation can amplify perturbations must be read relative to the perturbation topology: `C^0` control does not bound derivative variation, but a destination that retains the atomic derivative measure has retained essentially the full source coefficient complexity.

This is not a cheap repair of compression. The strong metric is deliberately expensive: on the Riesz image it is exactly equivalent to the source `ell^1` resource one is trying to preserve.

### The Mellin formula begins in an absolute-convergence half-plane

Equation `(8)` is asserted first where the coefficient Dirichlet series and the interchange are absolutely convergent with `Re(s)>0`. Any continuation beyond that region is extra analytic structure and is not supplied by the recovery identity alone.

### Bounded-error collapse is target-relative

The quotient by bounded functions in `(28)` is the precise abstraction of the AF-348 comparison only for a destination that is insensitive to bounded residuals. A theorem that uses the bounded term, its jumps, oscillation, Mellin transform, derivative variation, or another fine statistic may still distinguish the controls.

### This does not yet identify the RH-consumed source resource

The result locates one false bottleneck: fixed-order Riesz smoothing itself is not the irreversible step. It does not prove that the final RH-relevant operation retains the full profile or the derivative-variation metric, nor does it identify a normalized source functional that excludes the perfect-power backgrounds and survives the actual critical-line theorem with a quantitative margin.

## Consequence for Arithmetic Fidelity

AF-349 supplies an exact composition rule for the current obstruction program:

\[
\boxed{
\text{do not attribute discriminator loss to an invertible intermediate transform when the loss occurs in a later observation quotient or weak target metric.}
}
\tag{30}
\]

For the AF-344--AF-348 control family, the sparse-versus-dense distinction survives every fixed finite Riesz order in the complete cutoff profile and in its Mellin/Dirichlet transform. It is recovered isometrically by derivative variation, yet it becomes only `O(1)` in raw profile amplitude once `r>=k-1`. What disappears is therefore not the coefficient information itself but its visibility under the terminal metric or quotient.

The next useful source-resource theorem must be paired with the **actual final observer**: identify a discriminator, propagate it through the intermediate transform, and prove a quantitative margin in the exact topology consumed by the final operation. Source complexity alone, intermediate invertibility alone, and a strong metric that simply re-encodes the full source are each insufficient.