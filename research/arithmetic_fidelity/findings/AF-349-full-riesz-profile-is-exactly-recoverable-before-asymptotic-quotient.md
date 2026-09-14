# AF-349 — the full Riesz cutoff profile is exactly recoverable before the asymptotic quotient

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `ARITHMETIC-FIDELITY`, `SOURCE-COMPLEXITY-CONSERVATION`, `BOUNDARY-CLARIFICATION`, `NO-NOVELTY-CLAIM`

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

There is a second exact recovery bridge in the Dirichlet/Mellin category. If

\[
A(s):=\sum_{n\ge1}\frac{a_n}{n^s}
\tag{6}
\]

converges absolutely at `s`, with `Re(s)>0`, then absolute interchange gives

\[
\boxed{
\int_0^\infty
\mathcal R_r[a](X)X^{-s-1}\,dX
=
B(s,r+1)A(s),
}
\tag{7}
\]

where

\[
B(s,r+1)
=
\frac{\Gamma(s)\Gamma(r+1)}{\Gamma(s+r+1)}
=
\frac{r!}{s(s+1)\cdots(s+r)}.
\tag{8}
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
\tag{9}
\]

Thus fixed-order Riesz smoothing separates into two mathematically different operations:

\[
\text{coefficients}
\xrightarrow{\text{full cutoff profile}}
\mathcal R_r[a](\cdot)
\xrightarrow{\text{coarse asymptotic readout}}
\text{leading/error class}.
\tag{10}
\]

The first arrow is faithful. The loss exhibited by AF-347--AF-348 occurs only after the destination forgets the fine cutoff dependence, for example by retaining only a leading term modulo a declared error class.

This locates the information-loss stage exactly: **finite Riesz smoothing is not intrinsically a lossy compression when its entire cutoff profile is retained; the lossy operation is the subsequent scalarization or asymptotic quotient.**

## Derivation

### 1. Local coefficient recovery from truncated powers

Multiplying `(1)` by `X^r` gives, away from irrelevant endpoint conventions,

\[
F_r[a](X)
=
\sum_{n\le X}a_n(X-n)^r
=
\sum_{n\ge1}a_n(X-n)_+^r.
\tag{11}
\]

Only finitely many summands meet any compact interval, so the sum is locally finite as a distribution. The standard truncated-power identity is

\[
D^{r+1}(X-n)_+^r=r!\,\delta_n.
\tag{12}
\]

Applying `(12)` term by term gives `(5)`. No growth, convergence, positivity, or arithmetic hypothesis on `a_n` is required beyond local finiteness of the integer support.

For `r>=1`, an equivalent classical reading avoids the final distributional derivative: `D^rF_r[a]` is piecewise constant and its jump across `X=n` is exactly `r!a_n`. For `r=0`, `F_0[a]` is the ordinary cumulative step function and its jump is `a_n`.

Therefore

\[
\mathcal R_r[a]=\mathcal R_r[b]\text{ for all }X>0
\quad\Longrightarrow\quad
a_n=b_n\text{ for every }n.
\tag{13}
\]

The full cutoff profile is an exact encoding, not merely a statistic with a small kernel.

### 2. Mellin recovery of the Dirichlet series

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
\tag{14}
\]

Absolute convergence permits summation under the integral, yielding

\[
\int_0^\infty \mathcal R_r[a](X)X^{-s-1}\,dX
=
B(s,r+1)\sum_{n\ge1}a_n n^{-s},
\tag{15}
\]

which is `(7)`. For integer `r`, the gamma recurrence gives `(8)`, and division by the nonzero beta factor gives `(9)`.

This is the forward-Mellin counterpart of the classical Perron/Riesz contour formula: typical Riesz means are obtained from a Dirichlet series by an inverse Mellin kernel, and integrating the complete profile against the dual Mellin character recovers the Dirichlet series.

### 3. The AF-348 power control remains distinguishable in the full profile

For the weighted perfect-`k`-power background from AF-344--AF-348,

\[
b_k(n)=
\begin{cases}
km^{k-1},&n=m^k,\ m\ge2,\\
0,&\text{otherwise},
\end{cases}
\tag{16}
\]

its Dirichlet transform is

\[
B_k(s)=k\bigl(\zeta(ks-k+1)-1\bigr).
\tag{17}
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
\tag{18}
\]

The bracket is not identically zero; for example it tends to `-1` as `Re(s)->+infinity`. Therefore the complete Riesz profiles remain different for every finite `r`.

AF-348 proves simultaneously that for `r>=k-1`,

\[
\mathcal R_r[b_k](X)-\mathcal R_r[u](X)=O_{k,r}(1)
\tag{19}
\]

uniformly as `X->infinity`. Equations `(18)` and `(19)` are compatible: a bounded residual profile can still carry the entire coefficient-level distinction. Discarding bounded residuals is an additional quotient, not a property of the Riesz transform itself.

## Exact fidelity factorization

AF-348 can now be sharpened conceptually without changing its theorem. Let `\mathscr P_r` denote the space of full cutoff profiles and let `\mathscr B` denote bounded functions on `[1,\infty)`. On the power-background comparison with `r>=k-1`, the relevant map factors as

\[
a
\xrightarrow{\;R_r\;}
\mathcal R_r[a](\cdot)
\xrightarrow{\;Q\;}
[\mathcal R_r[a]]\in\mathscr P_r/\mathscr B.
\tag{20}
\]

The first map is injective by `(5)`. The second map is not faithful to the dense-versus-power discriminator because `(19)` gives

\[
Q(\mathcal R_r[b_k])=Q(\mathcal R_r[u]).
\tag{21}
\]

So the exact kernel responsible for the AF-348 example is introduced by `Q`, not by `R_r`.

The same warning applies to any destination that observes only a normalization such as `\mathcal R_r(X)/X`, only finitely many asymptotic coefficients, or only membership in a coarse error class. A smoothing operator may regularize a source while remaining mathematically invertible; information is lost only when a later observer identifies profiles that the inverse would distinguish.

## Relation to AF-347--AF-348

AF-347 and AF-348 remain correct. Their exact estimates prove that raw support locality is unavailable to a theorem whose declared observable identifies all bounded residual profiles after enough smoothing.

AF-349 narrows the causal statement. It is not enough to say that "Riesz smoothing erases locality" without specifying the destination metric. At full-profile resolution the smoothing is faithful. The demonstrated collapse occurs at **polynomial/asymptotic resolution** because the sparse and dense outputs enter the same bounded-error class.

This distinction is important for the line's current source-resource program. A candidate source functional should not be rejected merely because a smoothing stage reduces its visible magnitude. One must ask whether the actual destination keeps the whole transformed object, a norm controlling the residual, or only a quotient that kills it. Conversely, exact invertibility of the smoothing stage is not useful if the final RH theorem consumes only the coarse quotient.

## Prior art and novelty assessment

No novelty claim is made for Riesz means, the Perron/Mellin kernel, truncated-power differentiation, or Dirichlet-series uniqueness.

- Marcel Riesz, **“Une méthode de sommation équivalente à la méthode des moyennes arithmétiques,”** *Comptes rendus de l’Académie des sciences* 152 (1911), 1651–1654, is the classical source for Riesz summation/typical means.
- G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* 41, 119–196, DOI `10.1007/BF02422942`, use Riesz means in the analytic-number-theory setting and connect them to zeta/prime-distribution questions.
- Ingo Schoolmann, **“On Bohr's theorem for general Dirichlet series,”** *Mathematische Nachrichten* 293(8), 1591–1612 (2020), DOI `10.1002/mana.201800542`, explicitly treats approximation by typical Riesz means for general Dirichlet series and derives the relevant Perron-type representation.

The Mellin identity `(7)` is the direct forward transform of this classical kernel, and `(5)` is the elementary truncated-power recovery identity. The Arithmetic Fidelity contribution is the placement of these standard facts against AF-348's matched control: the earlier bounded-error collapse is localized to an explicit **post-smoothing quotient** rather than to the full smoothing representation itself.

## Boundaries and failure modes

### Full-profile access is a strong observation model

Injectivity requires access to the complete function `X->R_r[a](X)` with exact resolution. Sampling it on a sparse cutoff set, retaining only asymptotic coefficients, adding noise, or passing to a norm/quotient can destroy stable or exact recovery. AF-349 does not claim numerical conditioning of the inverse.

### Exact recovery can be violently unstable

Equation `(5)` differentiates `r+1` times. Even though the map is injective, differentiation can amplify small perturbations severely. Exact fidelity and stable fidelity therefore remain distinct. A downstream noisy or approximate theorem needs a conditioning estimate, not merely injectivity.

### The Mellin formula begins in an absolute-convergence half-plane

Equation `(7)` is asserted first where the coefficient Dirichlet series and the interchange are absolutely convergent with `Re(s)>0`. Any continuation beyond that region is extra analytic structure and is not supplied by the recovery identity alone.

### Bounded-error collapse is target-relative

The quotient by bounded functions in `(20)` is the precise abstraction of the AF-348 comparison only for a destination that is insensitive to bounded residuals. A theorem that uses the bounded term, its jumps, oscillation, Mellin transform, or another fine statistic may still distinguish the controls.

### This does not yet identify the RH-consumed source resource

The result locates one false bottleneck: fixed-order Riesz smoothing itself is not the irreversible step. It does not prove that the final RH-relevant operation retains the full profile, nor does it identify a normalized source functional that excludes the perfect-power backgrounds and survives the actual critical-line theorem with a quantitative margin.

## Consequence for Arithmetic Fidelity

AF-349 supplies an exact composition rule for the current obstruction program:

\[
\boxed{
\text{do not attribute discriminator loss to an invertible intermediate transform when the loss occurs in a later observation quotient.}
}
\tag{22}
\]

For the AF-344--AF-348 control family, the sparse-versus-dense distinction survives every fixed finite Riesz order in the complete cutoff profile and in its Mellin/Dirichlet transform. What disappears is only its visibility after quotienting by the bounded residual class (or an equally coarse asymptotic readout).

The next useful source-resource theorem must therefore be paired with the **actual final observer**: identify a discriminator, propagate it through the intermediate transform, and show that it remains outside the kernel or tolerated error class of the terminal operation. Source complexity alone and intermediate invertibility alone are each insufficient.