# MC-328 — Low-degree endpoint reweighting is blind to half-loaded source mass

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint and common source-package notation of `MC-323`–`MC-327`. Write a mode as

\[
a=(a_1,\ldots,a_R)\in\mathbf F_2^R,
\qquad
\lambda_a=\sum_i a_i\lambda_i,
\]

and let its exact endpoint coefficient be

\[
 x(a)=(-1)^{|a|}\left(1-\frac{2|a|}{R}\right).
\tag{1}
\]

For each source prime `p`, let

\[
s_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_R})\in\mathbf F_2^R\setminus\{0\},
\qquad
a_p:=|s_p|,
\]

so the package representative of mode `a` contains `p` exactly when `a\cdot s_p=1`.

Let `F_R(t)` be any real polynomial of degree `d_R<R/2` such that

\[
w(a):=F_R(x(a))\ge0
\qquad(a\in\mathbf F_2^R).
\tag{2}
\]

The polynomial may depend on `R`. Put

\[
W:=\sum_{a\ne0}w(a)>0,
\qquad
w_0:=w(0)=F_R(1),
\]

and define the weighted source-column loading

\[
\ell_w(s)
:=\frac1W\sum_{\substack{a\ne0\\a\cdot s=1}}w(a).
\tag{3}
\]

Then every source column in the entire middle Hamming band

\[
 d_R<|s|<R-d_R
\tag{4}
\]

has the **same exact loading**

\[
\boxed{
\ell_w(s)
=
\frac12+\frac{w_0}{2W}
\ge\frac12.
}
\tag{5}
\]

Thus a nonnegative mode reweighting obtained from a low-degree polynomial of the endpoint coefficient cannot exploit the half-loaded source band exposed by `MC-327`: throughout that band it does not lower source incidence below one half at all.

More generally, let

\[
\nu_p:=\frac{\log p}{\log P},
\qquad
\mathcal B_R
=
\sum_p\nu_p\left(\frac{2a_p-R}{R}\right)^2
\]

be the logarithmic source-imbalance energy of `MC-327`, and define the exact aggregate loading

\[
C_w:=\sum_p\nu_p\ell_w(s_p).
\tag{6}
\]

The total logarithmic source mass outside `(4)` satisfies

\[
\boxed{
\sum_{\substack{p:\ a_p\le d_R\ {or}\ a_p\ge R-d_R}}
\nu_p
\le
\frac{\mathcal B_R}{(1-2d_R/R)^2}.
}
\tag{7}
\]

Consequently, whenever

\[
d_R=o(R),
\qquad
\mathcal B_R\to0,
\tag{8}
\]

one has

\[
\boxed{C_w\ge\frac12-o(1).}
\tag{9}
\]

If in addition `w_0/W\to0`, then the middle-band loading in `(5)` is `1/2+o(1)` and, since `0\le\ell_w(s)\le1`,

\[
\boxed{C_w=\frac12+o(1).}
\tag{10}
\]

Under the quartic saturation hypothesis

\[
\frac{\log P}{\log y}=4+o(1),
\tag{11}
\]

`MC-327` gives exactly `\mathcal B_R\to0`. Therefore **every diffuse nonnegative endpoint-polynomial weighting of Fourier degree `o(R)` is asymptotically half-loaded by the actual logarithmic source mass**. Such a weighting cannot turn the near-quadratic independent conductor bills of `MC-323` into a source exponent strictly above `4`.

A concrete family is

\[
w_m(a)=x(a)^{2m}
\tag{12}
\]

for any fixed `m\ge1`. In the critical endpoint range in which the full selected family has size `2^R=y^{o(1)}`, the `MC-323` energy bound implies that modes of primitive conductor at most `y^{2-\delta}` carry only `O_\delta(1)` total `w_m`-mass, while

\[
\sum_{a\in\mathbf F_2^R}w_m(a)
=
(2m-1)!!\,\frac{2^R}{R^m}\left(1+O_m(R^{-1})\right).
\tag{13}
\]

Hence almost all `w_m`-mass lies on near-quadratic-conductor modes, but `(10)` says its source loading is still `1/2+o(1)`. Taking higher fixed even moments therefore does **not** amplify the quartic source floor. To obtain a genuine gain from mode selection after `MC-327`, one must use a weighting with Fourier degree comparable to the central source band, an arithmetic restriction on which central incidence columns actually occur, or a joint/signed conductor inequality outside positive independent-bill summation.

No estimate for `M(x)` follows.

## 1. The endpoint coefficient has only top- and bottom-degree Fourier support

For `u\in\mathbf F_2^R`, write the Walsh character

\[
\chi_u(a):=(-1)^{a\cdot u}.
\]

Let `\mathbf1=(1,\ldots,1)` and `e_i` be the coordinate vectors. Then

\[
(-1)^{|a|}=\chi_{\mathbf1}(a),
\qquad
1-\frac{2|a|}{R}
=
\frac1R\sum_{i=1}^R\chi_{e_i}(a).
\tag{14}
\]

Thus

\[
x(a)
=
\chi_{\mathbf1}(a)
\frac1R\sum_i\chi_{e_i}(a).
\tag{15}
\]

Consider a monomial `x(a)^j`. The `j`-th power of the average in `(14)` expands into Walsh characters indexed by symmetric differences of at most `j` singleton sets, so its Fourier support has Hamming weight at most `j`.

If `j` is even, the parity factor `\chi_{\mathbf1}^j` is `1`, so `x^j` has Fourier support only at weights at most `j`. If `j` is odd, multiplication by `\chi_{\mathbf1}` complements every Fourier index; hence the support lies only at weights at least `R-j`.

Therefore for every polynomial `F_R` of degree `d_R`, the full-cube weight function

\[
\widetilde w(a):=F_R(x(a))
\]

has Walsh-Fourier support contained in

\[
\boxed{
\{s:|s|\le d_R\}
\ \cup\
\{s:|s|\ge R-d_R\}.
}
\tag{16}
\]

This is the only spectral fact needed below.

## 2. Every middle source column is exactly half loaded

Use the unnormalized Walsh transform

\[
\widehat{\widetilde w}(s)
:=
\sum_{a\in\mathbf F_2^R}
\widetilde w(a)(-1)^{a\cdot s}.
\tag{17}
\]

For `s` in the middle band `(4)`, equation `(16)` gives

\[
\widehat{\widetilde w}(s)=0.
\tag{18}
\]

The conductor sum omits the zero mode. Since `w_0=\widetilde w(0)`, its transform over nonzero modes is therefore

\[
\sum_{a\ne0}w(a)(-1)^{a\cdot s}
=-w_0.
\tag{19}
\]

Split the total nonzero weight according to `a\cdot s=0` or `1`. The odd-parity part is

\[
\begin{aligned}
\sum_{\substack{a\ne0\\a\cdot s=1}}w(a)
&=
\frac12\left(
W-
\sum_{a\ne0}w(a)(-1)^{a\cdot s}
\right)\\
&=
\frac{W+w_0}{2}.
\end{aligned}
\tag{20}
\]

Division by `W` proves `(5)`.

The zero-mode correction is worth retaining. If the polynomial assigns positive weight to `a=0`, removing that analytically useless mode pushes the loading **above**, not below, one half. A low-degree endpoint polynomial therefore cannot hide a sub-half gain inside the omission of the principal mode.

## 3. The MC-327 imbalance energy removes the low/high Fourier tails

If `a_p\le d_R` or `a_p\ge R-d_R`, then

\[
\left|\frac{2a_p-R}{R}\right|
\ge
1-\frac{2d_R}{R}.
\tag{21}
\]

Multiplying the squared version of `(21)` by `\nu_p` and summing over those source primes gives `(7)` directly from the definition of `\mathcal B_R`.

Under `(8)`, the right-hand side of `(7)` tends to zero. Hence logarithmic source mass `1-o(1)` lies in the middle band where `(5)` holds exactly. Since all loadings are nonnegative,

\[
C_w
\ge
\left(\frac12+\frac{w_0}{2W}\right)(1-o(1))
\ge\frac12-o(1),
\]

which proves `(9)`.

If `w_0/W\to0`, then the middle contribution is `(1/2+o(1))(1-o(1))`, while the discarded source tail contributes at most `o(1)` because `\ell_w\le1`. This proves `(10)`.

The logical role of `MC-327` is precise. `MC-326` showed that arbitrary nonnegative mode weights cannot guarantee a universal loading constant below one half when *all* nonzero source columns are allowed. `MC-327` then left open the possibility that the **actual** economical source package, forced into the central Hamming band, might admit a specially chosen weighting with lower loading there. Equations `(5)`–`(10)` close that escape for every endpoint weighting whose Walsh spectrum stays a sublinear distance from the two ends of the Hamming cube.

## 4. Fixed endpoint moments exhaust the MC-323 energy without improving the source exponent

Take `F_R(t)=t^{2m}` with fixed `m\ge1`. Then `d_R=2m=o(R)`, `w_0=1`, and

\[
w_m(a)
=
\left(1-\frac{2|a|}{R}\right)^{2m}.
\tag{22}
\]

If `\varepsilon_1,\ldots,\varepsilon_R` are independent Rademacher variables, then the uniform Hamming-weight distribution gives

\[
2^{-R}
\sum_{a\in\mathbf F_2^R}w_m(a)
=
\mathbb E\left(
\frac{\varepsilon_1+\cdots+\varepsilon_R}{R}
\right)^{2m}.
\tag{23}
\]

The leading contribution to the even moment comes from pairings of the `2m` indices, giving

\[
\mathbb E(\varepsilon_1+\cdots+\varepsilon_R)^{2m}
=(2m-1)!!\,R^m+O_m(R^{m-1}).
\tag{24}
\]

Equations `(23)`–`(24)` prove `(13)`. After deleting the zero mode,

\[
W_m
=(2m-1)!!\,\frac{2^R}{R^m}(1+O_m(R^{-1}))-1,
\tag{25}
\]

so `W_m\to\infty`.

Now fix `\delta>0` and let `\mathcal L_\delta` be the endpoint modes whose minimum primitive source conductor is at most `y^{2-\delta}`. In the critical range `2^R=y^{o(1)}`, equation `(5)` of `MC-323`, applied to this varying-modulus family, gives

\[
\sum_{a\in\mathcal L_\delta}|x(a)|^2=O_\delta(1).
\tag{26}
\]

Because `|x(a)|\le1`,

\[
\sum_{a\in\mathcal L_\delta}w_m(a)
\le
\sum_{a\in\mathcal L_\delta}|x(a)|^2
=O_\delta(1).
\tag{27}
\]

Thus all but `O_\delta(1)` total `w_m`-mass lies on modes with minimum primitive conductor greater than `y^{2-\delta}`. Every fixed package representative `m_a` has conductor at least that minimum, so

\[
\sum_{a\ne0}w_m(a)\log m_a
\ge
(2-\delta)(W_m-O_\delta(1))\log y.
\tag{28}
\]

On the source side, exact double counting gives

\[
\sum_{a\ne0}w_m(a)\log m_a
=
W_m C_{w_m}\log P.
\tag{29}
\]

If one now tries to contradict quartic saturation `(11)`, `MC-327` supplies `\mathcal B_R\to0`, and `(10)` supplies

\[
C_{w_m}=\frac12+o(1).
\tag{30}
\]

Combining `(28)`–`(30)` yields only the same asymptotic quartic bill already exposed by pairs:

\[
\frac{\log P}{\log y}
\ge
4-2\delta-o(1).
\tag{31}
\]

Letting the fixed `\delta` tend to zero recovers `4`, not a strict improvement. The full bias-energy hierarchy therefore does not create hidden amplification at any fixed even moment.

## 5. Prior art and novelty boundary

The analytic input is exactly the varying-modulus prime Halász–Montgomery estimate already audited in `MC-323`: Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143–149, DOI `10.4064/aa106-2-4`, Theorem 3. No strengthening of that theorem is claimed here.

The Fourier mechanism is classical analysis on the Boolean cube. Walsh characters form the Fourier basis, products of coordinate characters add their indices in `\mathbf F_2^R`, and a polynomial of degree `d` in degree-one characters has Fourier support of degree at most `d`. In radial form this is the standard Krawtchouk/Hamming-scheme language already audited in `MC-325`; see Philippe Delsarte and Vladimir I. Levenshtein, *Association schemes and coding theory*, IEEE Transactions on Information Theory **44** (1998), 2477–2504, DOI `10.1109/18.720545`. A fresh literature check on 16 September 2026 also found the standard modern Boolean-Fourier formulation in Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), DOI `10.1017/CBO9781139814782`, and current low-degree Hamming-cube work, but no need for a stronger external theorem.

No novelty is claimed for Walsh-Fourier support, Krawtchouk duality, Rademacher moments, or polynomial degree. The line-specific result is their exact composition with the reciprocal endpoint coefficient `(1)` and the `MC-327` logarithmic half-loading rigidity. That composition shows that the most direct bias-aware low-degree reweightings are spectrally incapable of seeing a sub-half source-loading advantage precisely where a quartic-saturating arithmetic package is forced to live.

## Boundaries and falsification tests

- **Polynomial/low spectral degree is load-bearing.** A discontinuous threshold in `x(a)`, a high-degree polynomial, or an arbitrary mode selector can have Walsh support in the central Hamming band and is not covered by `(16)`.
- **Nonnegative weights are load-bearing.** They match positive summation of independent conductor lower bounds. Signed weights require a joint identity or inequality that controls cancellations between unknown conductor costs; this is exactly the escape already isolated by `MC-326`–`MC-327`.
- **Quartic saturation enters only through source concentration.** The exact middle-band identity `(5)` is unconditional for the endpoint algebra. The passage to `(9)`–`(10)` uses `\mathcal B_R\to0`, which `MC-327` obtains only when `\log P/\log y=4+o(1)`.
- **The mode weights must be genuinely diffuse for equality `(10)`.** If `w_0/W` does not vanish, the middle loading is strictly above one half, which weakens rather than strengthens the conductor-summing route.
- **The fixed-moment corollary uses the critical family-size range.** Equation `(26)` invokes the `MC-323` energy bound for the entire low-conductor endpoint family and therefore assumes `2^R=y^{o(1)}` (in particular the previously studied `2^R\asymp\log y` regime). The source-side theorem `(5)`–`(10)` does not require this assumption.
- **High Fourier degree remains open.** To use the actual near-half-loaded incidence set in a way not killed here, a future nonnegative selector must place substantial Fourier mass at source-column weights `R/2+o(R)`. Such a selector is necessarily high-degree/nonlocal in the endpoint mode variable.
- **Arithmetic restriction remains open.** This finding treats every source column in the central band identically. A theorem showing that the Legendre-source columns occupy a much smaller arithmetic subset of that band can still produce a gain.
- **Joint conductor information remains open.** Determinants, covariance inequalities, signed combinations, or other relations among primitive conductors are not reducible to the positive weighted identity `(29)` and are not ruled out.
- **No Möbius or RH conclusion is asserted.** The reciprocal endpoint remains a conditional source geometry. This finding closes one source-weighting architecture inside that model and nothing more.