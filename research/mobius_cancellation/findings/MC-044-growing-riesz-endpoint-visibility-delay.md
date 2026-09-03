# MC-044 — Growing-order Riesz smoothing creates an endpoint-visibility delay independent of Gamma normalization

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let `k>=1` be an integer and, for any coefficient sequence `|a_n|<=1`, define the unnormalized order-`k` Riesz sum

\[
S_{k,a}(x)=\sum_{n\le x}a_n\left(1-\frac nx\right)^k,
\qquad x\ge1,
\tag{1}
\]

and its kernel-mass normalization

\[
A_{k,a}(x)=\frac{k+1}{x}S_{k,a}(x).
\tag{2}
\]

The Gamma-normalized statistic of `MC-042`–`MC-043` is just `R_{k,a}(x)=S_{k,a}(x)/\Gamma(k+1)`. Thus `(2)` deliberately removes the rapid Gamma shrinkage isolated in `MC-043`.

Even after that renormalization, increasing the Riesz order creates a second, independent information loss: the one-scale kernel becomes increasingly blind to coefficients near its current endpoint.

For integers `X>=1` and `1<=L<=X`, if two bounded sequences `a,b` agree for every `n<=X-L`, then

\[
\boxed{
|A_{k,a}(X)-A_{k,b}(X)|
\le
2\left(\frac LX\right)^{k+1}.
}
\tag{3}
\]

In contrast, their ordinary partial sums can differ by order `L`. In particular, there are exact square-free-support controls `a_n,b_n in {-1,0,1}` with the same zero set as `mu(n)` for which, whenever `L>>sqrt(X)`,

\[
\left|\sum_{n\le X}(a_n-b_n)\right|
=
\left(\frac{12}{\pi^2}+o(1)\right)L,
\tag{4}
\]

while `(3)` still holds. Therefore a terminal excursion on an RH-relevant scale such as `L=X^(1/2+epsilon)` can be polynomially large in the ordinary sum and simultaneously have vanishingly small influence on the same-scale mass-normalized Riesz statistic; if `k=k(X)->infinity`, that influence is suppressed faster than any fixed power contributed by a fixed endpoint fraction.

The same effect has an exact scale interpretation. The weight assigned at evaluation scale `Y>N` to a coefficient at index `N` satisfies

\[
\left(1-\frac NY\right)^k
\le e^{-kN/Y}.
\tag{5}
\]

Hence retaining even a fixed weight `eta in (0,1)` on current-scale coefficients requires

\[
\boxed{
\frac YN\ge \frac{k}{\log(1/\eta)}.
}
\tag{6}
\]

So a growing-order kernel evaluated only at scales `Y=O(N)` becomes exponentially insensitive to the coefficients near `N`; constant-strength visibility moves out to a future scale `Y=Omega(kN)`.

This does **not** mean that fixed-order Riesz smoothing destroys information. On every interval containing no integer, with `D=x d/dx`, the Riesz family obeys the exact recursion

\[
D S_{r,a}(x)=r\bigl(S_{r-1,a}(x)-S_{r,a}(x)\bigr),
\tag{7}
\]

and therefore, for integer `k`,

\[
\boxed{
S_{0,a}(x)
=
\prod_{j=1}^{k}\left(1+\frac Dj\right)S_{k,a}(x)
=
\frac1{k!}\prod_{j=1}^{k}(D+j)S_{k,a}(x).
}
\tag{8}
\]

Here `S_{0,a}(x)=sum_{n<=x}a_n` on each open unit interval. Thus the **full same-order function of scale** retains the unsmoothed partial sums, but inversion requires logarithmic derivatives up to order `k`. A diagonal growing-order datum such as `S_{k(x),a}(x)` does not provide those same-order neighboring-scale derivatives merely from a magnitude estimate.

Consequently the variable-order escape left open by `MC-042` and bounded above by the normalization-vacuity threshold in `MC-043` has a second quantitative obligation. It is not enough to choose `k(x)` below the Gamma-vacuity scale and prove that the diagonal smoothed value is small. A useful route must also explain how endpoint/current-scale information is recovered: through same-order multiscale control, a translated/localized carrier, derivative/Tauberian side information, or genuinely arithmetic structure that forbids the coherent endpoint perturbations hidden by `(3)`.

## 1. Exact terminal-block sensitivity

Take integer `X`, integer `L`, and suppose `a_n=b_n` for `n<=X-L`. From `(2)`,

\[
|A_{k,a}(X)-A_{k,b}(X)|
\le
\frac{2(k+1)}{X}
\sum_{X-L<n\le X}
\left(1-\frac nX\right)^k.
\tag{9}
\]

Put `j=X-n`. Then `0<=j<=L-1`, so

\[
\sum_{X-L<n\le X}
\left(1-\frac nX\right)^k
=
\frac1{X^k}\sum_{j=0}^{L-1}j^k.
\tag{10}
\]

Since `t^k` is increasing for `k>=1`,

\[
\sum_{j=0}^{L-1}j^k
\le
\int_0^L t^k\,dt
=
\frac{L^{k+1}}{k+1}.
\tag{11}
\]

Substitution into `(9)` gives `(3)` exactly.

The estimate is normalized at the natural total-kernel scale. Indeed `S_{k,+}(X)` for the all-positive sequence has leading size `X/(k+1)` whenever `k=o(X)`, as already quantified in `MC-043`. Thus `(3)` is not the Gamma-normalization shrinkage in another notation: it measures the fraction of the **mass-normalized** kernel that can see a terminal block.

For a terminal width `L=X^alpha`, `0<alpha<1`, `(3)` becomes

\[
|A_{k,a}(X)-A_{k,b}(X)|
\le
2X^{-(1-alpha)(k+1)}.
\tag{12}
\]

At `alpha=1/2+epsilon`, a perturbation large enough to alter an ordinary partial sum on the RH-relevant polynomial scale is therefore attenuated by `X^{-(1/2-epsilon)(k+1)}` in the same-scale normalized Riesz observation.

## 2. Exact square-free-support matched control

The preceding obstruction is generic, so it is important to check that it is not created only by allowing a support pattern unrelated to Möbius.

Let

\[
q(n)=\mu(n)^2
\]

be the square-free indicator. For fixed `X,L`, define

\[
a_n=q(n)
\]

and

\[
b_n=
\begin{cases}
q(n),&n\le X-L,\\
-q(n),&X-L<n\le X.
\end{cases}
\tag{13}
\]

Both sequences have exactly the Möbius square-free support. Their ordinary partial-sum difference at `X` is

\[
2\sum_{X-L<n\le X}\mu(n)^2.
\tag{14}
\]

Using the elementary square-free counting estimate

\[
Q(t)=\sum_{n\le t}\mu(n)^2
=\frac6{\pi^2}t+O(\sqrt t),
\tag{15}
\]

we get `(4)` whenever `L/sqrt(X)->infinity`. Yet `(3)` applies unchanged because `|a_n|,|b_n|<=1`.

This comparator intentionally preserves **support but not multiplicativity** after the terminal sign flip. It therefore kills only an inverse theorem whose retained hypotheses do not use multiplicativity or another genuinely arithmetic constraint. A Möbius-specific Tauberian theorem is still allowed to exploit such extra structure; it must name and use it explicitly rather than infer endpoint control from the smoothed magnitude alone.

## 3. Growing order moves current-scale visibility into the future

For `0<u<1`, `log(1-u)<=-u`. Taking `u=N/Y` gives `(5)`. If the coefficient at `N` is to retain weight at least `eta`, then

\[
\eta
\le
\left(1-\frac NY\right)^k
\le
 e^{-kN/Y},
\]

which implies `(6)`.

Equivalently, for every fixed `C>1`, all coefficients with index comparable to the evaluation scale satisfy

\[
Y\le CN
\quad\Longrightarrow\quad
\left(1-\frac NY\right)^k\le e^{-k/C}.
\tag{16}
\]

This makes the geometric effect of growing order explicit. The Riesz kernel is anchored at the origin; as `k` increases it puts its effective mass farther and farther below the nominal cutoff. To see coefficients around arithmetic scale `N` with order-one kernel weight, one must evaluate the same order at a cutoff larger by a factor proportional to `k`.

That delay does not prove a variable-order method impossible. It changes the proof obligation: a useful estimate at scale `N` must either survive transport to scales of order `kN`, or the carrier must be redesigned so that its smoothing window is centered/localized near the scale whose ordinary partial sum is being controlled.

## 4. Exact same-order inversion and why there is no contradiction with MC-042

Fix `r>0` and an open interval `(m,m+1)`. The set of terms in `(1)` is constant on that interval, so termwise differentiation is legitimate. For one term,

\[
D\left(1-\frac nx\right)^r
=
r\frac nx\left(1-\frac nx\right)^{r-1}
=
r\left[
\left(1-\frac nx\right)^{r-1}
-
\left(1-\frac nx\right)^r
\right].
\tag{17}
\]

Summing gives `(7)`. For integer `k>=1`, rearrange it as

\[
S_{k-1,a}
=\left(1+\frac Dk\right)S_{k,a}.
\tag{18}
\]

Iterating from `k` to `0` gives `(8)`. The factors commute because they are polynomials in the same Euler derivative `D`.

This identity explains the apparent tension with `MC-042`. A fixed-order Riesz transform is not an irreversible quotient when its complete scale dependence is retained. `MC-042` likewise showed, through the fixed Mellin multiplier, that a critical bound for the full fixed-order family remains RH-equivalent.

The information loss identified here is different: **one-scale magnitude control discards the derivative/neighboring-scale information needed by `(8)`, and a diagonal family with changing order does not restore that information automatically.** As `k` grows, the exact inverse has increasing differential order at the same time that `(3)` and `(6)` show increasing endpoint attenuation.

No derivative norm estimate follows from a pointwise magnitude bound for this piecewise-smooth family without additional hypotheses. Supplying such a derivative, variation, monotonicity, analytic, or arithmetic constraint is precisely a Tauberian side condition rather than a free property of smoothing.

## 5. Prior art and novelty boundary

Riesz and Cesàro summability, their inclusion relations, and inverse/Tauberian theorems are classical. `MC-S30` already anchors the general principle that stronger ordinary conclusions from a summability method require side conditions, while `MC-S31` anchors the specific generalized Möbius Riesz family and its fixed/growing-order use.

A targeted literature check also finds the classical inverse-theorem literature for Cesàro and Riesz methods, including J. Karamata, *Quelques Théorèmes Inverses Relatifs Aux Procédés Sommabilité De Cesàro Et Riesz* (Publications de l'Institut Mathématique 3(9), 1950, 53–71), as well as modern Riesz-summability work that explicitly treats localization and boundary recovery for Dirichlet series. These sources confirm that inverse recovery is established Tauberian territory.

No novelty is claimed for Riesz kernels, Tauberian inversion as a subject, the inequality `log(1-u)<=-u`, square-free counting, or differentiation of the kernel. The durable line-specific contribution is the **quantitative information audit of the currently live growing-order escape**: after removing the Gamma normalization identified in `MC-043`, the kernel still has an exact endpoint-sensitivity factor `(L/X)^(k+1)`, a linear-in-`k` visibility delay, and an exact same-order inverse whose differential order grows with `k`.

## 6. Consequence for the active transfer problem

`MC-042` closed every fixed-order endpoint as an easier RH target. `MC-043` then showed that sufficiently fast growth of the normalized order makes a square-root-looking bound vacuous because the total kernel mass already shrinks below that scale.

The present finding narrows the remaining region **below** that vacuity threshold. Renormalizing away total kernel mass does not make a diagonal growing-order statistic a cancellation-faithful replacement for `M(X)`: current endpoint information is still suppressed, and exact recovery needs same-order scale derivatives or equivalent Tauberian structure.

Accordingly, the next viable smoothing candidate must do more than select a slowly growing `k(X)` and bound `R_{k(X),\mu}(X)`. It must provide at least one genuinely additional carrier of information, for example:

- same-order control over a sufficiently rich neighboring/future scale range to support the inverse in `(8)`;
- a translated or localized Riesz-type kernel whose mass remains centered on the current arithmetic scale;
- a quantitative derivative/variation relation proved from independently weaker Möbius arithmetic;
- or a nonlinear/multiplicative coupling that rules out the terminal coherent perturbations exposed by `(3)`.

A matched exact-support or multiplicative control satisfying the proposed extra hypotheses while retaining a large ordinary endpoint sum would kill the corresponding candidate. Without such extra information, growing-order smoothing has changed where the Mertens burden is hidden, not removed it.