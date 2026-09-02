# MC-027 — Analytic scale doubling has an iteration threshold, not a generic exponent-neutrality barrier

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `NO-NOVELTY-CLAIM`.

## Claim

For the centered Huxley–Watt analytic state used in `MC-023`, the quadratic map is exponent-neutral **at one step**: a bound of size `N^{-alpha}` is sent by a generic quadratic estimate to size `(N^2)^{-alpha}`. That one-step bookkeeping is exact, but it does not imply that a genuinely iterable contraction can only improve constants.

If the normalized state satisfies an actual recurrence

\[
y_{k+1}\le a_k y_k^2,
\qquad N_{k+1}=N_k^2,
\]

then repeated squaring converts sufficient subunit smallness into a strict power gain whenever the weighted logarithmic cost

\[
\sum_{j\ge0}2^{-j-1}\log a_j
\]

is finite. In particular, a fixed factor `a_k=c<1` can increase the power exponent along the square-scale tower; the contraction is not merely a constant improvement.

For the shrinking analytic radii naturally suggested by `MC-023`, `rho_N asymp 1/log N`, the Cauchy loss grows only like `log N`. Along `N_k=N_0^{2^k}`, this produces `log a_k=O(k)`, so the weighted logarithmic cost is finite. **Radius loss alone therefore does not kill iteration.** It creates a finite smallness threshold.

The unresolved obstruction is sharper: the exact Huxley–Watt recursion contains an additive arithmetic residual, and the available norm estimate separates that residual from the quadratic term. Unless the residual itself has the desired improved scale, or there is signed cancellation in the coupled expression before absolute values are taken, it creates a normalized floor that blocks exponent amplification. A square-tower gain also does not automatically give a bound for all `N` without a separate interpolation or coverage argument.

Separately, the fixed-radius zero-free-information boundary remains valid: sufficiently strong polynomial decay of the analytic state on a fixed disk already forces convergence of the Möbius Dirichlet series to the left of `Re(s)=1` and hence a fixed zero-free half-plane. The viable non-circular bootstrap target is therefore an **iterable shrinking-germ recurrence with controlled residual/coupling**, not a generic fixed-radius norm contraction and not a one-step exponent ledger.

## 1. Exact centered recursion and one-step neutrality

Retain the notation of `MC-023`:

\[
F_N(t)=\sum_{n\le N}\frac{\mu(n)}{n^{1+t}},
\qquad
f(t)=\frac1{\zeta(1+t)},
\qquad
A_N(t)=N^t(F_N(t)-f(t)).
\]

The renormalized Huxley–Watt identity is

\[
A_{N^2}(t)
=
\mathcal Q[A_N](t)-\frac{B_N(t)}{N^2},
\tag{1}
\]

where

\[
\mathcal Q[A](t)
=
\frac{A(0)^2}{t}-\frac{A(t)^2}{f(t)}.
\tag{2}
\]

Writing `f(t)=t h(t)` with `h(0)=1`, the singularity at `t=0` is removable and

\[
\mathcal Q[cA]=c^2\mathcal Q[A].
\tag{3}
\]

For fixed nested disks `0<r<R` inside a zero-free neighborhood of `h`, the standard difference-quotient/Cauchy estimate gives

\[
\|\mathcal Q[A]\|_r
\le
C_{r,R}\|A\|_R^2,
\qquad
C_{r,R}=\frac{\|1/h\|_R}{R-r}.
\tag{4}
\]

Therefore if

\[
\|A_N\|_R\le C N^{-\alpha},
\qquad
\frac{\|B_N\|_r}{N^2}\le C_B N^{-2\alpha},
\]

then

\[
\|A_{N^2}\|_r
\le (C_{r,R}C^2+C_B)(N^2)^{-\alpha}.
\tag{5}
\]

Equation (5) proves only a **one-step exponent-neutrality statement**. It does not decide what happens if the same normalized recurrence closes repeatedly with a quantitative contraction margin.

## 2. Exact iteration ledger for a quadratic recurrence

Let

\[
N_k=N_0^{2^k}
\]

and suppose a nonnegative normalized state obeys

\[
y_{k+1}\le a_k y_k^2,
\qquad a_k>0.
\tag{6}
\]

Iterating logarithms gives the exact bound

\[
\log y_k
\le
2^k\log y_0
+
\sum_{j=0}^{k-1}2^{k-1-j}\log a_j.
\tag{7}
\]

Hence

\[
2^{-k}\log y_k
\le
\log y_0
+
\sum_{j=0}^{k-1}2^{-j-1}\log a_j.
\tag{8}
\]

If

\[
S:=\sum_{j\ge0}2^{-j-1}\log a_j<\infty
\]

and

\[
\eta:=-\log y_0-S>0,
\tag{9}
\]

then

\[
y_k\le e^{-\eta 2^k}=N_k^{-\eta/\log N_0}.
\tag{10}
\]

Thus an initially normalized `O(1)` state that lies below the explicit threshold `e^{-S}` acquires a positive power saving along the tower.

The constant-contraction example is immediate. If `a_k=c<1`, then `S=\log c`, and for `y_0=1` one obtains

\[
y_k\le c^{2^k-1}
=c^{-1}N_k^{-(-\log c)/\log N_0}.
\tag{11}
\]

More generally, if an unnormalized estimate is `x_0\le C N_0^{-\alpha}` and the recurrence is `x_{k+1}\le c x_k^2`, then the normalized starting value is `y_0\le C`; a gain occurs when the corresponding threshold condition, in particular `cC<1` in this constant case, is met. A subunit coefficient by itself is therefore not enough, but a truly iterable contraction can become a power gain.

## 3. Shrinking-radius Cauchy loss is iteration-admissible

Take the natural scale-dependent radii

\[
\rho_N=\frac{c_0}{\log N}
\]

for sufficiently large `N`, and along the square tower set

\[
\rho_k:=\rho_{N_k}.
\]

Then

\[
\rho_{k+1}=\frac{\rho_k}{2}.
\tag{12}
\]

Apply (4) with source radius `R=\rho_k` and target radius `r=\rho_{k+1}`. Since `h` is nonzero near the origin, `\|1/h\|_{\rho_k}` is uniformly bounded for large `N_0`; hence

\[
a_k:=C_{\rho_{k+1},\rho_k}
=O\!\left(\frac1{\rho_k}\right)
=O(\log N_k).
\tag{13}
\]

Because `\log N_k=2^k\log N_0`, equation (13) gives

\[
\log a_k=O(k+\log\log N_0).
\]

Therefore

\[
\sum_{k\ge0}2^{-k-1}\log a_k<\infty.
\tag{14}
\]

This is the decisive correction to a generic radius-loss no-go. The Cauchy constants diverge as the germ shrinks, but under the `N\mapsto N^2` dynamics their logarithms have finite dyadic weight. They raise the initial smallness threshold in (9); they do not algebraically forbid an exponent bootstrap.

This does **not** prove that the Möbius state satisfies the required recurrence. It identifies what the analytic loss itself does and does not obstruct.

## 4. The additive residual is the real absolute-value floor

Return to (1), choose the shrinking radii above, and define

\[
x_k=\|A_{N_k}\|_{\rho_k},
\qquad
y_k=N_k^\alpha x_k.
\]

Taking absolute values termwise gives

\[
y_{k+1}
\le
a_k y_k^2+e_k,
\tag{15}
\]

where

\[
e_k
:=
N_{k+1}^\alpha
\frac{\|B_{N_k}\|_{\rho_{k+1}}}{N_k^2}.
\tag{16}
\]

To upgrade from exponent `alpha` to `alpha+delta`, the normalized target is

\[
y_k=O(N_k^{-\delta}).
\tag{17}
\]

A separately bounded positive residual in (15) must therefore satisfy, at the relevant scale,

\[
e_k=O(N_{k+1}^{-\delta})
=O(N_k^{-2\delta}),
\tag{18}
\]

or an equivalent summably smaller condition. Translating (18) back to the unnormalized residual requires

\[
\frac{\|B_{N_k}\|_{\rho_{k+1}}}{N_k^2}
=O(N_{k+1}^{-(\alpha+\delta)}).
\tag{19}
\]

So a proof that estimates `Q[A_N]` and `B_N/N^2` separately by absolute values risks demanding the improved exponent from the residual before the bootstrap can produce it.

There is one important escape: equation (1) is signed. A useful arithmetic mechanism may estimate the coupled quantity

\[
\mathcal Q[A_N](t)-\frac{B_N(t)}{N^2}
\tag{20}
\]

directly and obtain cancellation that is invisible after the triangle inequality. The residual-floor obstruction applies to separated positive norm bounds, not to a proved signed coupling.

## 5. Square-tower amplification still needs global coverage

Even if (6)–(10) hold, they directly control only

\[
N_0,\ N_0^2,\ N_0^4,\ldots
\]

A global bound for all large `N` requires an additional interpolation, monotonicity, comparison, or overlapping-family argument. The analytic state `A_N(t)` is not known to be monotone in `N`, so this step cannot be assumed.

Thus an iterable contraction has three logically separate requirements:

1. **small-state threshold:** the normalized germ must eventually enter the basin described by (9);
2. **residual/coupling control:** the additive term must not impose the old exponent as a floor, unless signed coupling beats the separated estimate;
3. **scale coverage:** tower control must propagate to arbitrary `N`.

Failure of any one is enough to prevent a global exponent bootstrap.

## 6. Fixed-radius decay still imports zero-free information

The fixed-radius warning survives independently of the iteration correction. Fix `delta>0` inside an admissible disk and suppose

\[
\|A_N\|_R=O(N^{-\alpha}),
\qquad R>\delta,
\qquad \alpha>\delta.
\tag{21}
\]

At `t=-delta`,

\[
F_N(-\delta)-f(-\delta)
=N^\delta A_N(-\delta)
=O(N^{\delta-\alpha})\to0.
\tag{22}
\]

Hence

\[
\sum_{n\le N}\frac{\mu(n)}{n^{1-\delta}}
\]

converges. Standard Dirichlet-series theory then gives a holomorphic sum on `Re(s)>1-delta`; on `Re(s)>1` it equals `1/zeta(s)`. By analytic continuation of the identity `G(s)zeta(s)=1` away from the pole at `s=1`, zeta has no zeros in that half-plane. Equivalently, standard Abel/Kronecker arguments give a corresponding power saving for `M(N)`.

Therefore a fixed analytic neighborhood with sufficiently fast polynomial decay is not a weak local input. The shrinking regime `rho_N asymp 1/log N` remains the natural way to avoid importing a fixed zero-free strip.

## 7. Prior art and novelty boundary

The scale-doubling identity is due to M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. `MC-023` derived the reciprocal-zeta-centered analytic specialization used here.

The Cauchy estimate, elementary iteration of a quadratic recurrence, Dirichlet-series convergence theory, and the relation between Möbius partial sums and zero-free half-planes are classical. No novelty is claimed for these ingredients or for the recurrence algebra.

The durable result is a correction and a sharper boundary for the active Mathia route: one-step exponent neutrality cannot be promoted to an iteration no-go, and the natural `1/log N` radius loss has finite dyadic logarithmic cost. The remaining load-bearing issue is quantitative smallness plus the additive/signed residual and global scale coverage.

## 8. Consequence for the research line

The analytic continuation of `MC-023` is more viable than a one-step exponent ledger suggests, but only in a very specific form. A useful bootstrap would need to prove that a shrinking analytic germ enters an iterative small-state basin, then control the Huxley–Watt residual either at the improved scale or through direct signed cancellation, and finally bridge square-scale towers to all `N`.

This focuses the next attack on the exact coupled residual rather than on searching for a generic norm in which the quadratic map merely has a bounded constant. A candidate mechanism that cannot beat the normalized floor in (15), or cannot propagate beyond a sparse tower, cannot improve the Mertens exponent even if its pure quadratic part contracts.