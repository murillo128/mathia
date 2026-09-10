# MC-187 — Classical Mertens cancellation transfers to the logarithmically rough zero mode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The logarithmically rough Möbius zero mode isolated in `MC-180` and `MC-185` inherits the full classical Korobov--Vinogradov-shaped cancellation available for the ordinary Mertens function. This is substantially stronger than the all-fixed-logarithmic-power estimate obtained from the fixed-order Alamoudi expansion in `MC-186`, although it still remains on the subpower side of the fixed-power boundary required by the live variance program.

Let

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y},
\qquad
G_y(x)=\sum_{n\le x}g_y(n),
\tag{1}
\]

and let

\[
s_y(d)=\mathbf 1_{P^+(d)\le y},
\qquad s_y(1)=1.
\tag{2}
\]

The exact inverse convolution from `MC-181`,

\[
 g_y=\mu*s_y,
\tag{3}
\]

implies the exact global identity

\[
\boxed{
G_y(x)=\sum_{\substack{d\le x\\P^+(d)\le y}}M(x/d).
}
\tag{4}
\]

Write

\[
\Phi(x):=(\log x)^{3/5}(\log\log x)^{-1/5}.
\tag{5}
\]

Using the classical unconditional Mertens estimate recorded in `MC-S3`,

\[
M(u)\ll u\exp(-a\Phi(u))
\tag{6}
\]

for some fixed `a>0`, equation `(4)` yields the following uniform transfer. For every fixed `C>0` there is `a_C>0` such that, for all sufficiently large `x` and

\[
2\le y\le C\log x,
\tag{7}
\]

one has

\[
\boxed{
G_y(x)
\ll_C
x\exp(-a_C\Phi(x)).
}
\tag{8}
\]

In particular, at the live cutoff `y=c log X` with fixed `c>0`, uniformly for `x\asymp X`,

\[
\boxed{
G_{c\log X}(x)
\ll_c
X\exp(-a_c\Phi(X)),
}
\tag{9}
\]

and therefore

\[
\boxed{
G_{c\log X}(2X)-G_{c\log X}(X)
\ll_c
X\exp(-a_c\Phi(X)).
}
\tag{10}
\]

Thus the coarse signed rough zero mode does not merely admit cancellation by every fixed logarithmic power: at logarithmic sifting level it inherits the same asymptotic cancellation class as the best classical unconditional bound for `M(x)`, up to a change of constant in the exponential.

This does **not** cross the live fixed-power threshold. Since `Phi(X)=o(log X)`, for every fixed `delta>0`,

\[
\frac{X\exp(-a_c\Phi(X))}{X^{1-\delta}}
=
\exp\!\left(\delta\log X-a_c\Phi(X)\right)
\longrightarrow\infty.
\tag{11}
\]

Hence `(10)` does not imply the zero-mode estimate required by `MC-185`,

\[
G_y(2X)-G_y(X)
\ll
X^{1-\theta\eta/2+o(1)}
\tag{12}
\]

for any fixed `theta eta>0`. The zero-mode frontier is therefore sharper than in `MC-186`: the missing jump is not from fixed logarithmic saving to fixed power, but from **Korobov--Vinogradov-shaped subpower cancellation to one genuine fixed power**.

## 1. Exact transfer from the full Mertens function

Equation `(4)` follows directly by summing the coefficient identity `(3)`. Indeed,

\[
G_y(x)
=
\sum_{n\le x}\sum_{d\mid n}s_y(d)\mu(n/d)
=
\sum_{\substack{d\le x\\P^+(d)\le y}}
\sum_{m\le x/d}\mu(m),
\]

which is `(4)`. No analytic continuation, reciprocal-zeta estimate, contour shift, or zero-free hypothesis beyond the already established unconditional input `(6)` is introduced by this transfer.

The key point is that the inverse kernel is positive and consists of all `y`-smooth integers. Its total harmonic mass is nevertheless small enough at logarithmic `y` that the classical global cancellation survives.

## 2. Small smooth divisors preserve the Korobov--Vinogradov saving

Split `(4)` at `d=sqrt(x)`. If `d<=sqrt(x)`, then `u=x/d>=sqrt(x)`. For sufficiently large `x`,

\[
\Phi(u)
\ge
2^{-3/5}\Phi(x),
\tag{13}
\]

because `log u >= (1/2) log x` while `log log u <= log log x`. Therefore `(6)` gives

\[
\begin{aligned}
\sum_{\substack{d\le\sqrt x\\P^+(d)\le y}}|M(x/d)|
&\ll
x\exp(-a2^{-3/5}\Phi(x))
\sum_{P^+(d)\le y}\frac1d\\
&=
x\exp(-a2^{-3/5}\Phi(x))
\prod_{p\le y}(1-p^{-1})^{-1}.
\end{aligned}
\tag{14}
\]

The classical Mertens product estimate gives

\[
\prod_{p\le y}(1-p^{-1})^{-1}\ll\log(2y).
\tag{15}
\]

Under `(7)`, this is only `O_C(log log x)`, which is absorbed by a harmless reduction of the constant in the exponential. Hence the small-divisor contribution is

\[
\boxed{
\ll_C x\exp(-a_1\Phi(x))
}
\tag{16}
\]

for some `a_1>0` depending at most on the constants already present in `(6)` and on `C` through the harmless uniform range.

This is the main term in the transfer. It shows that the exact smooth inverse does not degrade the classical Mertens cancellation to a logarithmic saving.

## 3. Large smooth divisors are exponentially rarer than the required scale

For `d>sqrt(x)`, use only the trivial bound `|M(x/d)|<=x/d`. Then

\[
\sum_{\substack{d>\sqrt x\\P^+(d)\le y}}|M(x/d)|
\le
x\sum_{\substack{d>\sqrt x\\P^+(d)\le y}}\frac1d.
\tag{17}
\]

Choose

\[
\alpha=\frac1{2\log y}.
\tag{18}
\]

For `y>=2`, one has `0<alpha<1`, and Rankin's trick gives

\[
\sum_{\substack{d>\sqrt x\\P^+(d)\le y}}\frac1d
\le
x^{-\alpha/2}
\sum_{P^+(d)\le y}d^{-1+\alpha}
=
x^{-1/(4\log y)}
\prod_{p\le y}(1-p^{-1+\alpha})^{-1}.
\tag{19}
\]

For every `p<=y`,

\[
p^\alpha\le e^{1/2},
\]

so the logarithm of the Euler product in `(19)` is

\[
O\!\left(\sum_{p\le y}\frac1p\right)
=O(\log\log(2y)).
\tag{20}
\]

Consequently

\[
\sum_{\substack{d>\sqrt x\\P^+(d)\le y}}\frac1d
\le
\exp\!\left(
-\frac{\log x}{4\log y}
+O(\log\log(2y))
\right).
\tag{21}
\]

When `y<=C log x`, the negative exponent has size

\[
\frac{\log x}{\log\log x},
\tag{22}
\]

which dominates `Phi(x)`. Thus the large-divisor contribution in `(17)` is actually smaller than the target scale in `(16)`:

\[
\boxed{
\sum_{\substack{d>\sqrt x\\P^+(d)\le y}}|M(x/d)|
\ll_C x\exp(-a_2\Phi(x))
}
\tag{23}
\]

for some `a_2>0`. Combining `(16)` and `(23)` proves `(8)`.

## 4. Consequence for `MC-186` and the zero-mode frontier

`MC-186` correctly audits Alamoudi's current fixed-order rough-sum expansion. For each fixed order `N`, its `k=1` specialization gives at `y=c log X` a remainder of size

\[
X\frac{(\log\log X)^{N+1}}{(\log X)^{N+2}},
\]

and hence `X/log^A X` for every fixed `A` after choosing `N=N(A)`. Its growing-order calculation correctly shows that **that particular expansion mechanism** would require order roughly `log X/log log X` to manufacture a fixed power, with no such uniformity supplied by the source.

The new point is that fixed-order rough-sum asymptotics are not the strongest available route to the magnitude of the zero mode at this logarithmic cutoff. The exact inverse `(4)` imports the already-proved Korobov--Vinogradov cancellation of the ordinary Mertens function through a kernel whose small-divisor harmonic mass is only logarithmic and whose large-divisor tail is much smaller still.

Accordingly, Alamoudi's expansion remains valuable as source-specific information about the rough object and as evidence about the limitations of fixed-order Selberg--Delange expansion. It should no longer be read as defining the best unconditional cancellation class known for `G_{c log X}`. The best immediate bound available from the current Mathia corpus is `(9)`.

This also strengthens the structural interpretation of `MC-181`. At fixed-power local-variance scale, the logarithmic rough split was already shown to be subpower-reversible on dilation-stable families. Equation `(8)` now gives a global analogue at the classical zero-free-region scale: removing all primes up to `c log X` does not, by itself, make the coarse rough zero mode substantially easier or harder in asymptotic cancellation currency.

## 5. Prior art and novelty boundary

The rough Möbius sum itself is classical. Alladi's 1982 paper *Asymptotic estimates of sums involving the Moebius function* studies

\[
\sum_{n\le x,\,P^-(n)>y}\mu(n)
\]

uniformly in the sifting parameter, and later restricted-prime-factor literature develops the same object. `MC-180` already records that prior-art boundary. The convolution identity `(3)` is the exact classical Euler-factor inverse already derived in `MC-181`, while `(6)` is the established unconditional Mertens estimate recorded in `MC-S3`.

A targeted literature check around Alladi's rough sum, restricted-prime-factor Möbius sums, and modern rough-sum asymptotics confirms that the object and its uniform study are established prior art. No claim is made that the elementary composition `(4)`--`(23)` is a new theorem of analytic number theory. It is stored because it materially corrects the **rate ledger of the active Mathia frontier**: the current corpus already implies a stronger zero-mode bound than `MC-186` obtained from its source-specific fixed-order expansion.

## 6. Boundaries and falsification tests

- Equation `(8)` is an upper-bound transfer. It does not assert that `G_y(x)` actually has Korobov--Vinogradov order, nor that a stronger unconditional estimate is impossible.
- The logarithmic sifting range is essential to the cheap tail argument. The proof uses `log y=O(log log x)`; it does not claim the same uniform transfer for `y=x^delta` with fixed `delta>0`.
- The large-divisor estimate uses no Möbius cancellation. If the Rankin tail in `(21)` were not smaller than `exp(-a Phi(x))` in the stated range, the transfer would fail at the claimed scale.
- The bound `(11)` is only a comparison of available upper-bound currencies. It does not prove that the rough zero mode fails every fixed-power estimate.
- No new zero-free region follows from `(8)` because `(8)` is derived from the existing unconditional Mertens bound `(6)`.
- Nothing here proves the uncentered short-interval variance target of `MC-180`. Even after the coarse zero mode is controlled at `(8)`, both `MC-185` and the current mind frontier require a genuinely fixed-power signed estimate, and the off-diagonal rough parity field remains unresolved.

The finding is falsified if `(3)` does not imply `(4)`, if the smooth harmonic factor in `(14)` costs more than subexponential `exp(o(Phi(x)))` at `y<=C log x`, if the large smooth-divisor tail in `(21)` is not negligible relative to the Korobov--Vinogradov scale, or if `(8)` is claimed to imply a fixed exponent below `1` without additional arithmetic information.

## Consequence for the active frontier

The immediate coarse-mode question is now cleaner. Reproving `G_{c log X}(x)<<X/log^A X`, optimizing a fixed number of Selberg--Delange terms, or otherwise obtaining another logarithmic/sub-Korobov saving cannot change the fixed-power variance budget. The coarse mode already inherits the strongest classical unconditional Mertens cancellation class available in the line.

A useful next theorem must therefore inject genuinely new signed information: either a fixed-power bound for the rough zero mode, a mechanism coupling that zero mode to the fluctuating short-interval parity field so it is not paid independently, or a direct parity-sensitive variance estimate whose proof simultaneously controls the zero frequency. The unsigned support side remains closed by `MC-184`; the remaining obstruction is still the signed rough prime-factor-parity field.