# ANF-149 — bow variance reduces to positive primes against the finite Ramanujan rough model

**Status:** `EXACT-DERIVED + SOURCE-NORMAL-FORM + PRIME-POWER-NEGLIGIBLE + FINITE-RAMANUJAN-IDENTITY + SOURCE-SPECIFIC-GATE`. `ANF-148` leaves one genuinely arithmetic escape from the prime-locus matched controls: the actual coefficient law of `Lambda-Lambda^sharp`, rather than free real amplitudes on the prime support. That law can be sharpened substantially. In the bow range `K=X^{1-2 epsilon+o(1)}`, `0<epsilon<1/4`, prime-power terms in `Lambda` are uniformly negligible in the exact moving-window `L^2` seminorm, for every real twist `U`. Hence the target `V_X(U;K)=o(XK log X)` is equivalent to the same target for the fixed-sign source `vartheta-Lambda^sharp`, where `vartheta(n)=log n` on primes and vanishes otherwise. Moreover `Lambda^sharp` is exactly a finite Ramanujan expansion over the primes `<R`, and its complete-period two-point correlation is exactly the truncated Hardy--Littlewood singular series. For every bow lag `1<=h<K<=X`, that truncated local product already agrees with the full prime-pair singular series up to a uniform relative `o(1)` on even lags (and both vanish on odd lags). Thus the remaining bow problem is not merely to exploit “prime versus rough-composite signs”: it is to preserve the exact inclusion--exclusion between a positive prime field and a deterministic small-prime Ramanujan counterterm. A viable source theorem should estimate their **combined twisted correlation error** before taking absolute values.

## 1. Prime powers are uniformly negligible at the bow variance scale

Write

\[
\vartheta(n):=(\log n)1_{\mathbb P}(n),
\qquad
E_{\mathrm{pp}}(n):=\Lambda(n)-\vartheta(n).
\tag{1}
\]

Thus `E_pp` is supported exactly on prime powers `p^j` with `j>=2`. For any arithmetic function `f`, define the bow seminorm

\[
\|f\|_{U,K}^{2}
:=
\int_X^{2X}
\left|
\sum_{x<n\le x+K} f(n)n^{-iU}
\right|^{2}dx.
\tag{2}
\]

No assumption on `U` is needed in this section.

For `x in [X,2X]`, the number of integer `j`th powers in `(x,x+K]` is

\[
\ll 1+\frac{K}{X^{1-1/j}}.
\tag{3}
\]

Indeed, on the relevant range the derivative of `t^j` is `asymp X^{1-1/j}`. Summing (3) over `2<=j<=log_2(3X)` gives, for large `X`,

\[
\#\{p^j\in(x,x+K]:j\ge2\}
\ll
\frac{K}{\sqrt X}+\log X.
\tag{4}
\]

Here the `j=2` term gives `K/sqrt X`, while the total contribution of `j>=3` is

\[
\ll \log X+\frac{K\log X}{X^{2/3}}
\ll \log X+\frac K{\sqrt X}.
\tag{5}
\]

Since every nonzero value of `E_pp` in `[X,3X]` is at most `log(3X)`, and `|n^{-iU}|=1`, (4) yields the pointwise bound

\[
\sup_{X\le x\le2X}
\left|
\sum_{x<n\le x+K}E_{\mathrm{pp}}(n)n^{-iU}
\right|
\ll
\log X\left(\frac K{\sqrt X}+\log X\right).
\tag{6}
\]

Consequently

\[
\boxed{
\|E_{\mathrm{pp}}\|_{U,K}^{2}
\ll
K^{2}\log ^2X+X\log ^4X.
}
\tag{7}
\]

The estimate is uniform in every real `U`. In the bow range

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\tag{8}
\]

both terms in (7) are lower order than the diagonal scale from `ANF-102`:

\[
\frac{K^{2}\log ^2X}{XK\log X}
=
\frac{K\log X}{X}=o(1),
\qquad
\frac{X\log ^4X}{XK\log X}
=
\frac{\log ^3X}{K}=o(1).
\tag{9}
\]

Thus

\[
\boxed{
\|E_{\mathrm{pp}}\|_{U,K}
=o\!\left((XK\log X)^{1/2}\right)
}
\tag{10}
\]

uniformly in `U`.

Now put

\[
Q_R(n):=\Lambda^\sharp(n)
=
\frac{P(R)}{\varphi(P(R))}
1_{(n,P(R))=1},
\qquad
R=e^{(\log X)^{1/10}},
\tag{11}
\]

and define

\[
a_X:=\Lambda-Q_R,
\qquad
r_X:=\vartheta-Q_R.
\tag{12}
\]

Then `a_X=r_X+E_pp`. Since (2) is the squared norm of a linear map into `L^2([X,2X])`, Minkowski gives

\[
\big|\|a_X\|_{U,K}-\|r_X\|_{U,K}\big|
\le \|E_{\mathrm{pp}}\|_{U,K}.
\tag{13}
\]

Combining (10) and (13),

\[
\boxed{
\|a_X\|_{U,K}^{2}=o(XK\log X)
\iff
\|r_X\|_{U,K}^{2}=o(XK\log X).
}
\tag{14}
\]

This equivalence holds for every real twist, not merely `U asymp X^2`. The normalization is unchanged: removing prime powers changes the second moment by only `o(X log X)`, while `ANF-102` already shows that the bow moving diagonal is `(1+o(1))XK log X`.

The coefficient law is therefore simpler than the one left at the end of `ANF-148`. On bulk primes `p asymp X`,

\[
r_X(p)=\log p-c_R>0,
\qquad
c_R:=\frac{P(R)}{\varphi(P(R))}\ll\log R=o(\log X),
\tag{15}
\]

while on `R`-rough composites that are not prime powers,

\[
r_X(n)=-c_R.
\tag{16}
\]

All prime-power exceptional signs can be discarded at the target scale.

## 2. `Lambda^sharp` is exactly a finite Ramanujan model

Let

\[
P:=P(R)=\prod_{p<R}p
\tag{17}
\]

and let `c_q(n)` denote the Ramanujan sum. For a prime `p`,

\[
c_p(n)=
\begin{cases}
p-1,&p\mid n,\\
-1,&p\nmid n.
\end{cases}
\tag{18}
\]

Hence

\[
1-\frac{c_p(n)}{p-1}
=
\begin{cases}
0,&p\mid n,\\
\dfrac p{p-1},&p\nmid n.
\end{cases}
\tag{19}
\]

Multiplying (19) over `p<R` gives the exact identity

\[
\boxed{
Q_R(n)
=
\prod_{p<R}\left(1-\frac{c_p(n)}{p-1}\right)
=
\sum_{q\mid P}\frac{\mu(q)}{\varphi(q)}c_q(n).
}
\tag{20}
\]

The last equality follows by expanding the product and using multiplicativity of Ramanujan sums on the squarefree divisors of `P`. Thus `Lambda^sharp` is not merely a support-level rough-number approximation: it is a **finite small-prime Fourier/Ramanujan field with completely prescribed coefficients**.

Its two-point local profile is equally exact. For an integer shift `h`, let

\[
\nu_p(h):=\#\{0,-h\pmod p\}
=
\begin{cases}
1,&p\mid h,\\
2,&p\nmid h.
\end{cases}
\tag{21}
\]

Averaging over one complete period and using the Chinese remainder theorem gives

\[
\begin{aligned}
\frac1P\sum_{n\bmod P}Q_R(n)Q_R(n+h)
&=
\prod_{p<R}
\frac{p-\nu_p(h)}p
\left(\frac p{p-1}\right)^2\\
&=:\mathfrak S_R(h).
\end{aligned}
\tag{22}
\]

Equivalently, by (20),

\[
\boxed{
\mathfrak S_R(h)
=
\sum_{q\mid P}
\frac{\mu(q)^2}{\varphi(q)^2}c_q(h)
=
\prod_{p<R}
\left(1-\frac{\nu_p(h)}p\right)
\left(1-\frac1p\right)^{-2}.
}
\tag{23}
\]

This is exactly the Hardy--Littlewood pair singular series truncated to local primes `<R`.

## 3. The truncated model already contains essentially the full local pair profile on every bow lag

Let

\[
\mathfrak S(h)
:=
\prod_p
\left(1-\frac{\nu_p(h)}p\right)
\left(1-\frac1p\right)^{-2}
\tag{24}
\]

be the usual two-point Hardy--Littlewood singular series. Once `R>2`, if `h` is odd then the `p=2` factor gives

\[
\mathfrak S_R(h)=\mathfrak S(h)=0.
\tag{25}
\]

Suppose now that `h` is even. The missing Euler factors satisfy

\[
\frac{\mathfrak S(h)}{\mathfrak S_R(h)}
=
\prod_{\substack{p\ge R\\p\mid h}}
\frac p{p-1}
\prod_{\substack{p\ge R\\p\nmid h}}
\left(1-\frac1{(p-1)^2}\right).
\tag{26}
\]

For `R` large,

\[
\left|\log\frac{\mathfrak S(h)}{\mathfrak S_R(h)}\right|
\ll
\sum_{\substack{p\ge R\\p\mid h}}\frac1p
+
\sum_{p\ge R}\frac1{p^2}.
\tag{27}
\]

The second sum is `O(1/R)`. If `omega_R(h)` denotes the number of prime divisors of `h` that are at least `R`, then

\[
R^{\omega_R(h)}\le h,
\qquad
\omega_R(h)\le\frac{\log(2h)}{\log R},
\tag{28}
\]

so

\[
\sum_{\substack{p\ge R\\p\mid h}}\frac1p
\le
\frac{\log(2h)}{R\log R}.
\tag{29}
\]

Therefore

\[
\boxed{
\mathfrak S(h)
=
\mathfrak S_R(h)
\left(
1+O\!\left(
\frac1R+
\frac{\log(2h)}{R\log R}
\right)
\right)
}
\tag{30}
\]

uniformly for even `h` as soon as the error is small. In particular, because

\[
R=e^{(\log X)^{1/10}},
\tag{31}
\]

for every bow lag `1<=h<K<=X`,

\[
\boxed{
\mathfrak S(h)
=\mathfrak S_R(h)(1+o(1))
}
\tag{32}
\]

uniformly on the even lags, while (25) handles the odd lags.

Equation (32) has to be interpreted carefully. It is a **local-factor statement**, not a prime-pair theorem. It does not assert that an interval average of `vartheta(n)vartheta(n+h)` equals `mathfrak S(h)`, and it does not identify a twisted correlation with the complete-period average (22). Also, the relative `o(1)` in (32) cannot be multiplied by `K` under absolute values and declared negligible: `K` is polynomial in `X`, whereas the tail in (30) is only subpolynomially small. The useful conclusion is structural instead: on every lag seen by the bow window, `Lambda^sharp` has already encoded essentially the entire **finite local obstruction pattern** predicted for prime pairs.

## 4. The exact bow ledger is a signed prime--rough correlation error

For the source-normal form `r_X=vartheta-Q_R`, the overlap expansion of `ANF-102` becomes

\[
\begin{aligned}
\|r_X\|_{U,K}^2
&=D_{r}(K)\\
&\quad+2\operatorname{Re}
\sum_{1\le h<K}
\sum_n
r_X(n)r_X(n+h)
\left(\frac{n+h}{n}\right)^{-iU}
\omega_K(n,n+h),
\end{aligned}
\tag{33}
\]

where `omega_K` is the exact moving-window overlap and

\[
D_r(K)=(1+o(1))XK\log X.
\tag{34}
\]

The source product in the off-diagonal has the exact inclusion--exclusion

\[
\boxed{
\begin{aligned}
r_X(n)r_X(n+h)
={}&\vartheta(n)\vartheta(n+h)
-\vartheta(n)Q_R(n+h)\\
&-Q_R(n)\vartheta(n+h)
+Q_R(n)Q_R(n+h).
\end{aligned}
}
\tag{35}
\]

This is the source information absent from the matched controls of `ANF-146`--`ANF-148`. The four terms cannot be replaced by independent magnitude estimates without discarding the only fixed arithmetic cancellation still available.

There is a useful formal local-factor diagnostic. At primes `<R`, the natural two-point local factor for a prime variable paired with a `Q_R` variable is the same factor in (23): one residue class is excluded by the prime condition and one by the rough condition, collapsing to one excluded class when `p|h`. Thus the three terms in (35) that contain `Q_R` carry the same finite local profile `mathfrak S_R(h)`. The Hardy--Littlewood local profile for the first term is `mathfrak S(h)`. At the level of these local main terms, inclusion--exclusion therefore leaves

\[
\mathfrak S(h)-\mathfrak S_R(h),
\tag{36}
\]

which is locally `o(mathfrak S_R(h))` by (30)--(32).

Equation (36) is deliberately **not** promoted to an asymptotic for the actual weighted sums in (33). Proving the needed prime--prime and prime--rough twisted correlations is precisely the missing theorem. Its role is to identify the correct architecture: `Lambda^sharp` behaves as a small-prime singular-series counterterm, so a bow proof should carry the four signed correlations together until their common local factors have cancelled.

This also clarifies why a componentwise type-I/type-II estimate can miss the desired scale. If each term of (35) is put behind absolute values before the common `mathfrak S_R` profile is exposed, the cancellation represented by (36) is irreversibly lost; one is then back in the factor-`K` coherence regime isolated by `ANF-145`--`ANF-148`.

## 5. Prior-art boundary and adversarial audit

The exact approximant (11) is the Matomäki--Radziwiłł--Shao--Tao--Teräväinen `Lambda^sharp` already anchored in `SOURCES.md`. Their paper explicitly treats it as a refined sieve/W-trick model, approximates it by a type-I divisor sum through the fundamental lemma, and later uses the local factors `p/(p-1) 1_{p\nmid n}` in its pseudorandomness arguments. The product identity (20), the complete-period correlation (22), and the tail estimate (30) are elementary derivations from that same model; no additional theorem is load-bearing.

A bounded prior-art audit also found the expected neighboring literature on correlations of truncated divisor-sum prime models and on short-interval variance of rough numbers. Those subjects confirm that singular-series correlations of sieve models are classical territory, but they do not supply the distinguished `U asymp X^2` signed four-term correlation required by (33)--(35). No new external source is therefore needed to support the exact Mathia claim, and `SOURCES.md` remains unchanged.

The main stress tests are explicit:

- The prime-power removal does not use cancellation in `U`; (7) is uniform in every real twist.
- The finite Ramanujan identity is exact because `P(R)` is squarefree.
- The complete-period average (22) is **not** silently substituted for an interval average on `[X,2X]`; the period `P(R)` may be far larger than `X`.
- The comparison (30) is only a local Euler-product comparison and does not assume Hardy--Littlewood prime pairs.
- The uniform relative `o(1)` in (32) is not strong enough to survive a naive absolute sum over all `h<K`; any such step would reintroduce an uncontrolled polynomial factor.
- Nothing here proves that the distinguished bow twist has small variance. The finding only reduces the source class and identifies the signed correlation object that a proof must control.

These checks prevent the normal form from smuggling in either a prime-pair conjecture or an unjustified periodic averaging argument.

## 6. Consequence for the bow frontier

`ANF-148` showed that actual prime locations, real coefficients, logarithmic coefficient size, and the exact carrier still do not determine the bow energy when amplitudes are allowed to adapt. The present result removes the remaining ambiguity about what source information has to replace that freedom.

Up to an `o(XK log X)` perturbation in the exact bow seminorm, the source is now uniquely represented as

\[
\boxed{
\vartheta(n)-
\sum_{q\mid P(R)}\frac{\mu(q)}{\varphi(q)}c_q(n).
}
\tag{37}
\]

The first term is a positive field on the actual primes; the second is a deterministic finite Ramanujan field whose two-point local product is `mathfrak S_R`. Thus the next useful theorem should not be another support/magnitude estimate and should not separately bound the prime and rough pieces. It should control the **combined twisted correlation error**

\[
\sum_{1\le h<K}\sum_n
\bigl(\vartheta(n)-Q_R(n)\bigr)
\bigl(\vartheta(n+h)-Q_R(n+h)\bigr)
\left(\frac{n+h}{n}\right)^{-iU}
\omega_K(n,n+h)
\tag{38}
\]

at the distinguished bow twist while preserving the signs in (35).

The decisive positive target remains the one forced by `ANF-102`:

\[
2\operatorname{Re}(38)
=-(1+o(1))XK\log X,
\tag{39}
\]

or any equivalent estimate implying `\|r_X\|_{U,K}^2=o(XK log X)`. A negative result would instead show that the fixed prime--Ramanujan source (37) cannot approach the low-gain moving-window modes at the required twist. Either outcome now acts on the actual source law rather than on a matched coefficient class.

For `analytic_frontier`, this is the clean source-specific gate after `ANF-148`: **prime powers are irrelevant, the rough component is an exact finite singular-series counterterm, and the unresolved mathematics is a signed twisted prime-versus-rough correlation theorem.**