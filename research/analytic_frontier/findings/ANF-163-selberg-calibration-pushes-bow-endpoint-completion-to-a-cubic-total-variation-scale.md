# ANF-163 — Selberg calibration pushes bow endpoint completion to a cubic total-variation scale

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC-L1 + ENDPOINT-CUMULATIVE-ENERGY-LOCALIZATION + SHARP-INFORMATION-BOUNDARY`. `ANF-162` used the local quadratic mass of the actual residual `r_X=\vartheta-Q_R` to move the endpoint threat from `sqrt(X/log X)` to a square-root-`X` wavelength. The same source law has a stronger feature in total variation. On every interval `I subset [X,3X]` of length `H>=X^eta`, with fixed `eta>0`, Brun--Titchmarsh controls the positive prime mass and a dimension-one Selberg upper-bound sieve controls the `R`-rough support of `Q_R`; because the counterterm normalization is `c_R=P(R)/phi(P(R))<<log R`, these two bounds combine to

\[
\boxed{\sum_{n\in I}|r_X(n)|\ll_\eta H.}
\]

Consequently every distinguished-twist endpoint prefix or suffix satisfies `|S_r|<<r` once `r>=X^eta`. Inserted into the exact endpoint square function of `ANF-157`, this shows that target-scale completion `XK log X` cannot be accumulated on prefix/suffix lengths smaller than

\[
\boxed{R_{\rm TV}(X,K):=(XK\log X)^{1/3}.}
\]

In the bow range `K=X^{1-2epsilon+o(1)}`, `0<epsilon<1/4`, this is a genuine mesoscopic scale

\[
\sqrt X\ll R_{\rm TV}
=X^{2/3-2\epsilon/3+o(1)}(\log X)^{1/3}
\ll K.
\]

A single target-sized endpoint spike must already occur at length `Omega(sqrt(X log X))`, improving the `Omega(sqrt X)` support floor of `ANF-162`, while a macroscopic amount of the **integrated endpoint completion energy** must persist out to constant multiples of `R_TV`. The cubic scale is sharp if one retains only this local `L^1` law and pointwise boundedness: a triangular bounded control has cumulative-square energy `asymp R^3`. Thus the remaining theorem cannot come from coefficient sparsity or total variation alone; it must use signed arithmetic decorrelation of the prime-minus-rough residual against the distinguished logarithmic twist.

## 1. The actual residual has uniformly bounded local total variation on every polynomial interval

Retain the source-normal form of `ANF-149`,

\[
r_X(n)=\vartheta(n)-Q_R(n),
\qquad
Q_R(n)=c_R\,1_{(n,P(R))=1},
\qquad
c_R:=\frac{P(R)}{\varphi(P(R))},
\tag{1}
\]

with

\[
R=e^{(\log X)^{1/10}},
\qquad
c_R\ll\log R=(\log X)^{1/10}.
\tag{2}
\]

Here `vartheta(n)=log n` on primes and vanishes otherwise. Fix `eta>0`, and let `I subset [X,3X]` be an integer interval of length

\[
H\ge X^\eta.
\tag{3}
\]

The prime part has bounded `L^1` mass. Brun--Titchmarsh in the case of modulus one gives

\[
\#(I\cap\mathbb P)\ll \frac{H}{\log H},
\tag{4}
\]

uniformly in the location of `I`. Since `log H>=eta log X` and every prime in the interval has logarithm at most `log(3X)`,

\[
\boxed{
\sum_{n\in I}\vartheta(n)
\ll_\eta H.
}
\tag{5}
\]

The rough counterterm has the same scale for a different reason. Put

\[
N_R(I):=\#\{n\in I:(n,P(R))=1\}.
\tag{6}
\]

Apply the classical dimension-one Selberg upper-bound sieve to the translated interval, sieving the residue class `0 mod p` for every prime `p<R`. For each squarefree `d|P(R)`, the divisibility count is

\[
\#\{n\in I:d\mid n\}=\frac Hd+O(1).
\tag{7}
\]

The standard Selberg bound therefore gives, for example by taking sieve level `R^2`,

\[
N_R(I)
\ll \frac{H}{\log R}
+
\sum_{\substack{d<R^2\\ d\mid P(R)}}3^{\omega(d)}.
\tag{8}
\]

For the present application no optimization of the remainder is needed. The crude estimate `3^{omega(d)}<=d` gives

\[
\sum_{d<R^2}3^{\omega(d)}\ll R^4.
\tag{9}
\]

But `R^4=\exp(4(\log X)^{1/10})=X^{o(1)}`, so (3) implies

\[
R^4=o_\eta\!\left(\frac H{\log R}\right).
\tag{10}
\]

Hence

\[
N_R(I)\ll_\eta\frac H{\log R}.
\tag{11}
\]

Multiplying by the exact counterterm amplitude and using (2),

\[
\boxed{
\sum_{n\in I}Q_R(n)
=c_RN_R(I)
\ll_\eta H.
}
\tag{12}
\]

The cancellation of scales in (12) is the key source calibration: the rough set has density at most order `1/log R`, while the finite Ramanujan counterterm has amplitude order `log R`. Since both `vartheta` and `Q_R` are nonnegative, (5) and (12) give

\[
\boxed{
\sum_{n\in I}|r_X(n)|
\le
\sum_{n\in I}\vartheta(n)+\sum_{n\in I}Q_R(n)
\ll_\eta H.
}
\tag{13}
\]

This is stronger than the local `L^2` statement of `ANF-162` in a different currency. It does not assert cancellation of `r_X`; it says that the **total available signed mass** on every polynomial-length interval is only linear in the interval length. Multiplication by any unit-modulus phase leaves (13) unchanged.

## 2. Distinguished-twist endpoint partial sums are linearly bounded after a tiny polynomial cutoff

Use the exact integer bow model of `ANF-157` and `ANF-158`, with

\[
b_n=r_X(X+n)(X+n)^{-iU},
\qquad
1\le n\le N+K-1,
\tag{14}
\]

and define the two endpoint cumulative sums

\[
S_r^-:=\sum_{n=1}^{r}b_n,
\qquad
S_r^+:=\sum_{n=M-r+1}^{M}b_n,
\qquad 1\le r<K.
\tag{15}
\]

All intervals appearing here lie inside `[X,3X]` in the bow range `K<=X`. Because `|n^{-iU}|=1`, (13) yields, for every fixed `eta>0`,

\[
\boxed{
|S_r^-|+|S_r^+|\ll_\eta r
\qquad (r\ge X^\eta),
}
\tag{16}
\]

uniformly in the real twist `U`. For shorter prefixes the pointwise source bound retained from `ANF-149`,

\[
|r_X(n)|\ll\log X,
\tag{17}
\]

gives

\[
|S_r^-|+|S_r^+|\ll r\log X.
\tag{18}
\]

Thus the source has a deterministic endpoint envelope which is much smaller than the coefficient-class envelope `r log X` as soon as the prefix length reaches any fixed positive power of `X`. This uses no oscillation of the distinguished carrier and therefore survives every resonance scenario from `ANF-159`--`ANF-161`.

## 3. Endpoint completion cannot accumulate macroscopically below a cubic length scale

The exact endpoint completion is

\[
E_\partial(b)
=
\sum_{r=1}^{K-1}|S_r^-|^2
+
\sum_{r=1}^{K-1}|S_r^+|^2.
\tag{19}
\]

For `1<=R_0<K`, let

\[
E_{\partial,\le R_0}(b)
:=
\sum_{r\le R_0}|S_r^-|^2
+
\sum_{r\le R_0}|S_r^+|^2.
\tag{20}
\]

Take `eta=1/4` in (16). Splitting (20) at `X^{1/4}`, using (18) below the split and (16) above it, gives uniformly in `U`

\[
\boxed{
E_{\partial,\le R_0}(b)
\ll
R_0^3+X^{3/4}\log^2X.
}
\tag{21}
\]

The bow target scale is

\[
T_{\rm bow}(X,K):=XK\log X.
\tag{22}
\]

Define

\[
\boxed{
R_{\rm TV}(X,K):=T_{\rm bow}(X,K)^{1/3}
=(XK\log X)^{1/3}.
}
\tag{23}
\]

Then for every function `omega(X)->infinity`, with

\[
R_0=\left\lfloor\frac{R_{\rm TV}}{\omega(X)}\right\rfloor,
\tag{24}
\]

(21) gives

\[
E_{\partial,\le R_0}(b)
\ll
\frac{XK\log X}{\omega(X)^3}
+X^{3/4}\log^2X.
\tag{25}
\]

In the bow range

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac14,
\tag{26}
\]

the second term in (25) is also `o(XK log X)`. Therefore

\[
\boxed{
E_{\partial,\le R_{\rm TV}/\omega}(b)
=o(XK\log X).
}
\tag{27}
\]

This is an integrated strengthening of the square-root support statement in `ANF-162`. If for some fixed `delta>0`

\[
E_\partial(b)\ge\delta XK\log X,
\tag{28}
\]

then (21) lets one choose a constant `c_delta>0`, independent of `X`, such that

\[
E_{\partial,\le c_\delta R_{\rm TV}}(b)
\le\frac\delta2 XK\log X
\tag{29}
\]

for all sufficiently large `X`. Hence

\[
\boxed{
E_{\partial,>c_\delta R_{\rm TV}}(b)
\ge\frac\delta2 XK\log X.
}
\tag{30}
\]

A macroscopic endpoint correction cannot therefore be an exclusively square-root-`X` phenomenon. A macroscopic amount of its cumulative-square energy must persist to prefix or suffix lengths of order at least `R_TV` up to a constant depending on the target fraction.

## 4. The new length is genuinely between `sqrt X` and the bow window

Substituting (26) into (23) gives

\[
\boxed{
R_{\rm TV}
=X^{2/3-2\varepsilon/3+o(1)}(\log X)^{1/3}.
}
\tag{31}
\]

Relative to the square-root scale from `ANF-162`,

\[
\frac{R_{\rm TV}}{\sqrt X}
=X^{(1-4\varepsilon)/6+o(1)}(\log X)^{1/3}
\longrightarrow\infty,
\tag{32}
\]

for every fixed `epsilon<1/4`. Relative to the full bow window,

\[
\frac{R_{\rm TV}}K
=
\left(\frac{X\log X}{K^2}\right)^{1/3}
=X^{(-1+4\varepsilon)/3+o(1)}(\log X)^{1/3}
\longrightarrow0.
\tag{33}
\]

Thus the total-variation input exposes a new, honest mesoscopic endpoint scale: polynomially larger than `sqrt X` but still a vanishing fraction of `K`.

There is also a simpler one-spike consequence. `ANF-158` proves that (28) forces

\[
M_\partial(b)
:=
\max_{r<K}\max\{|S_r^-|,|S_r^+|\}
\gg_\delta\sqrt{X\log X}.
\tag{34}
\]

The crude pointwise bound (17) first implies that any maximizing length is at least `Omega(sqrt(X/log X))`, hence certainly exceeds `X^{1/4}`. Equation (16) then applies and gives

\[
\boxed{
r_{\rm spike}\gg_\delta\sqrt{X\log X}.}
\tag{35}
\]

This improves the `Omega(sqrt X)` length forced by the local `L^2` input of `ANF-162`. Equation (35) concerns one large cumulative spike; the stronger scale (31) concerns where a target-sized **sum of cumulative squares** must continue to live. The two statements should not be conflated.

## 5. The cubic scale is sharp from total variation alone

The exponent `1/3` in (23) cannot be improved by manipulating only the deterministic local `L^1` envelope (13). Let `R<K/2`, and consider a synthetic left-edge coefficient sequence

\[
e_n=
\begin{cases}
1,&1\le n\le R,\\
-1,&R<n\le2R,\\
0,&n>2R.
\end{cases}
\tag{36}
\]

Its coefficients satisfy the strongest possible pointwise and local-total-variation bounds,

\[
|e_n|\le1,
\qquad
\sum_{n\in J}|e_n|\le|J|
\tag{37}
\]

for every interval `J`. Its cumulative sums form a triangle,

\[
S_r=
\begin{cases}
r,&r\le R,\\
2R-r,&R<r\le2R,\\
0,&r>2R,
\end{cases}
\tag{38}
\]

so

\[
\boxed{
\sum_{r<K}|S_r|^2
=\left(\frac23+o(1)\right)R^3.
}
\tag{39}
\]

Taking `R asymp (XK log X)^{1/3}` therefore produces endpoint completion of bow size while obeying every mass bound used in Sections 1--3. This is an information-boundary control, not a model of `vartheta-Q_R`: it deliberately discards the arithmetic placement and the fixed prime-minus-rough coefficient law. Its purpose is to show that the new mesoscopic gate is sharp **for the total-variation architecture itself**.

The consequence is negative but useful. Neither Brun--Titchmarsh sparsity, the rough-number sieve, local `L^2`, local `L^1`, nor pointwise coefficient control can make the endpoint completion `o(XK log X)` by themselves. Any next improvement has to use the signs/phases of the actual residual rather than only the amount of available mass.

## 6. Prior-art boundary and next gate

The only new load-bearing analytic ingredient beyond the previous source ledger is the classical Selberg upper-bound sieve applied to a translated interval. A convenient reference is D. R. Heath-Brown, **Lectures on sieves**, arXiv:math/0209360 (2002), whose Selberg-sieve fundamental theorem gives the upper bound used in (8). In our interval, the remainders are explicitly `O(1)` as in (7), and the special choice `R=exp((log X)^{1/10})` makes even the crude aggregate remainder `R^4=X^{o(1)}` negligible against every `H>=X^eta`. The Brun--Titchmarsh input is the same classical Montgomery--Vaughan large-sieve consequence already used in `ANF-162`.

The audit also checked the all-interval higher-uniformity theorem of Matomäki, Shao, Tao and Teräväinen, **Higher uniformity of arithmetic functions in short intervals I. All intervals**, *Forum of Mathematics, Pi* 11 (2023), e29, DOI `10.1017/fmp.2023.28`. It gives logarithmically saving correlations for `Lambda-Lambda^sharp` with fixed-complexity nilsequences once the interval is at least `X^{5/8+eta}`. That is important neighboring evidence that all-interval arithmetic decorrelation becomes available above a polynomial threshold, but its stated logarithmic relative saving does not by itself imply the power-scale endpoint square-function control required here over the entire range up to `K`. It is therefore prior-art boundary rather than a theorem imported into (13)--(39).

The Mathia-specific delta is the interaction between the calibrated rough counterterm and the exact finite-horizon completion identity. `ANF-162` showed that a target correction must contain a square-root-scale concentration. `ANF-163` now shows that **having such a concentration is not enough to account for its integrated energy**: under the actual source total variation, a macroscopic completion has to persist into the larger mesoscopic regime (31).

The next useful theorem can consequently be stated without carrier-only detours. One route is a distinguished-twist estimate of the form

\[
\sum_{r\asymp R}
\left|
\sum_{n\le r}
r_X(X+n)(X+n)^{-iU}
\right|^2
=o(XK\log X)
\tag{40}
\]

uniformly across dyadic endpoint scales

\[
R_{\rm TV}\lesssim R<K,
\tag{41}
\]

with the analogous right-edge estimate, at the exact bow twist `U asymp X^2`. A potentially stronger route is to keep the prime and `Q_R` terms coupled and prove directly that the positive Fejer source energy in `ANF-157` dominates the endpoint completion. Either route must exploit signed prime--rough arithmetic information; another coefficient-mass estimate cannot cross the sharp control (39).

A decisive falsification test is equally clear: construct an arithmetic control preserving the actual positive-prime/rough-counterterm law and the local sieve bounds while realizing target-size cumulative energy at the scale (31). Such a control would show that even calibrated total variation is not the missing source invariant. Conversely, any source theorem that saves a fixed power over the linear prefix envelope throughout (41) would immediately reduce the endpoint square function below the bow scale and would be qualitatively stronger than every source estimate currently stored in this line.
