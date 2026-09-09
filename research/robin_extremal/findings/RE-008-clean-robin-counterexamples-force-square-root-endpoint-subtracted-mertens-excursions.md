# RE-008 — clean Robin counterexamples force square-root endpoint-subtracted Mertens excursions

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SELECTOR-HEIGHT-COUPLING + ENDPOINT-CANCELLATION + MERTENS-TAIL-REDUCTION + CLEAN-COUNTEREXAMPLE-SQUARE-ROOT-EXCURSION + PRIOR-ART-BOUNDED`. `RE-006` gives an exact clean-peak selector in which the left boundary Chebyshev discrepancy and the accumulated higher CA layers determine the position `X-p` of a regular self-tangent local peak inside its consecutive-prime gap. `RE-007` then exposes the leading square-root mismatch but still does not distinguish a safe peak from a Robin counterexample. Combining the selector with the exact Euler-product height **before** taking absolute values produces a stronger structural reduction: the endpoint value `vartheta(p)-p` cancels identically.

For a sufficiently large clean regular self-tangent CA local peak `C`, put

\[
X:=\log C,
\]

and let `p<q` be its consecutive first-layer boundary primes, so `p<X<q`. Write

\[
\Delta(t):=\vartheta(t)-t,
\qquad
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\qquad
k(t):=\frac1{t\log t}.
\tag{1}
\]

Retain the higher-layer mass

\[
\Phi_{\ge2}(X)
:=\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\
                   \eta_{r,j}\le X}}\log r
\tag{2}
\]

and, if

\[
C=\prod_{r\le p}r^{a_r},
\]

define the exponent-tail correction

\[
T(C):=-\sum_{r\le p}\log\!\left(1-r^{-(a_r+1)}\right)\ge0.
\tag{3}
\]

Finally let the ordinary logarithmic Mertens-product error be

\[
E(p):=
\sum_{r\le p}-\log(1-r^{-1})
-\gamma-\log\log p
\tag{4}
\]

and define the **endpoint-subtracted Mertens remainder**

\[
\boxed{
\mathcal M_*(p):=E(p)-\Delta(p)h(p).
}
\tag{5}
\]

Then the Robin height of the clean peak satisfies the exact identity

\[
\boxed{
\log G(C)-\gamma
=
\mathcal M_*(p)-T(C)-\Phi_{\ge2}(X)h(p)+Q(p,X),
}
\tag{6}
\]

where

\[
\boxed{
Q(p,X):=\int_p^X\bigl(h(p)-k(t)\bigr)\,dt\ge0.
}
\tag{7}
\]

Thus the endpoint Chebyshev discrepancy selected in `RE-006` is not an independent height error. It cancels exactly against the endpoint term arising from partial summation of the Mertens product. What remains is a nonlocal Mertens/Chebyshev history term, the positive CA exponent tail, the higher-layer mass, and a small positive geometric correction.

More importantly, along any unbounded sequence of **clean Robin counterexample peaks** one necessarily has

\[
\boxed{
\liminf
\sqrt p\,\log p\;\mathcal M_*(p)
\ge 2\sqrt2.
}
\tag{8}
\]

This is a new necessary source-selection condition for the clean chamber. It does not prove that such excursions are impossible. It says that a clean counterexample cannot be produced merely by the endpoint tuning of `RE-007`: its selected boundary prime must also carry a positive square-root-scale excursion of the endpoint-subtracted Mertens remainder.

## 1. The complete Robin factorization keeps the selector and height on the same source

The divisor ratio factors exactly as

\[
\frac{\sigma(C)}C
=
\prod_{r\le p}
\frac{1-r^{-(a_r+1)}}{1-r^{-1}}.
\tag{9}
\]

Taking logarithms and using `G(C)=sigma(C)/(C log log C)` with `X=log C` gives

\[
\boxed{
\log G(C)-\gamma
=E(p)-T(C)+\log\frac{\log p}{\log X}.
}
\tag{10}
\]

This is classical finite Euler-product bookkeeping. By itself it is only another form of the Robin height. The useful step is to express `E(p)` in the same `vartheta` source that appears in the clean selector.

Since

\[
-\log(1-r^{-1})=h(r)\log r,
\]

Stieltjes summation gives

\[
\sum_{r\le p}-\log(1-r^{-1})
=\int_{2^-}^{p}h(t)\,d\vartheta(t).
\tag{11}
\]

Writing `vartheta(t)=t+Delta(t)` and integrating the `Delta` term by parts, with `Delta(2^-)=-2`, yields the exact identity

\[
E(p)
=B(p)+\Delta(p)h(p)
-\int_2^p\Delta(t)h'(t)\,dt,
\tag{12}
\]

where

\[
B(p):=2h(2)+\int_2^p h(t)\,dt-\gamma-\log\log p.
\tag{13}
\]

Consequently

\[
\boxed{
\mathcal M_*(p)
=B(p)-\int_2^p\Delta(t)h'(t)\,dt.
}
\tag{14}
\]

No zeta-zero estimate or RH assumption is used in (11)--(14).

## 2. The clean self-tangent selector cancels the endpoint Chebyshev error exactly

`RE-006` proves

\[
X-p
=\Phi_{\ge2}(X)-\bigl(p-\vartheta(p)\bigr)
=\Phi_{\ge2}(X)+\Delta(p),
\tag{15}
\]

so

\[
\boxed{
\Delta(p)=X-p-\Phi_{\ge2}(X).
}
\tag{16}
\]

Also

\[
\log\frac{\log p}{\log X}
=-\int_p^X k(t)\,dt.
\tag{17}
\]

Insert (12) and (16) into (10) **before** estimating either term. The endpoint contribution becomes

\[
\Delta(p)h(p)-\int_p^Xk(t)\,dt
=-\Phi_{\ge2}(X)h(p)
+\int_p^X\bigl(h(p)-k(t)\bigr)\,dt.
\tag{18}
\]

Equations (14) and (18) are exactly (6)--(7). In particular, the value `vartheta(p)-p` that drives the selected displacement in `RE-006` is absent from the final height formula. Treating the selector error and Mertens-product error independently would miss this cancellation.

The correction `Q` has a fixed sign. Since

\[
-\log(1-p^{-1})>p^{-1},
\]

one has `h(p)>k(p)`, while `k` is decreasing for `p>1`. Hence

\[
Q(p,X)\ge0.
\tag{19}
\]

This sign is useful but not enough by itself to prove Robin's inequality.

## 3. The correction `Q` is negligible at the square-root height scale

Put `d=X-p`. For large `p`, the elementary logarithm remainder gives

\[
0<h(p)-k(p)
\le
\frac{1}{2p(p-1)\log p}.
\tag{20}
\]

Moreover, on `p\le t\le X<2p`, the mean-value theorem applied to `k` gives

\[
0\le k(p)-k(t)
\ll \frac{t-p}{p^2\log p}.
\tag{21}
\]

Therefore

\[
\boxed{
0\le Q(p,X)
\ll
\frac{d}{p^2\log p}
+\frac{d^2}{p^2\log p}.
}
\tag{22}
\]

The current unconditional short-interval input recorded in `SOURCES.md` gives consecutive-prime gaps `q-p=O(p^{0.52})`; since `0<d<q-p`, (22) implies

\[
\boxed{
\sqrt p\log p\,Q(p,X)\longrightarrow0.
}
\tag{23}
\]

Any prime-gap exponent strictly below `3/4` would suffice for this particular negligibility statement. The `0.52` input is therefore used only as a comfortable unconditional boundary, not as an attempted square-root gap theorem.

## 4. Each of the two negative height corrections contributes at least `sqrt(2)`

`RE-007` proves

\[
\Phi_{\ge2}(X)=\sqrt{2X}+o(\sqrt X),
\qquad
\frac Xp\to1.
\tag{24}
\]

Since

\[
h(p)=\frac{1+O(p^{-1})}{p\log p},
\]

it follows that

\[
\boxed{
\sqrt p\log p\;\Phi_{\ge2}(X)h(p)
\longrightarrow\sqrt2.
}
\tag{25}
\]

The exponent tail has an independent contribution of the same size. The second-layer localization proved in `RE-007` says

\[
\eta_{r,2}=\frac{r^2}{2}(1+o(1)).
\tag{26}
\]

Fix `epsilon>0` and set

\[
y_\varepsilon(X):=
\sqrt{\frac{2X}{1-\varepsilon}}.
\tag{27}
\]

For all sufficiently large `X`, a prime `r>y_epsilon(X)` cannot yet have its second CA layer active. Every such prime with `r\le p` therefore occurs in `C` with exponent exactly one. Hence, from (3),

\[
T(C)
\ge
\sum_{y_\varepsilon(X)<r\le p}
-\log(1-r^{-2})
\ge
\sum_{y_\varepsilon(X)<r\le p}\frac1{r^2}.
\tag{28}
\]

The prime number theorem and partial summation give

\[
\sum_{r>y}\frac1{r^2}
\sim\frac1{y\log y}.
\tag{29}
\]

The omitted tail above `p` is `O((p\log p)^{-1})`, which is negligible after multiplication by `sqrt(p) log p`. Thus (27)--(29), followed by `epsilon downarrow0`, yield

\[
\boxed{
\liminf
\sqrt p\log p\;T(C)
\ge\sqrt2.
}
\tag{30}
\]

This is only a lower bound. Smaller-prime higher exponents add further positive mass and cannot weaken the argument.

## 5. A clean Robin counterexample forces the `2 sqrt(2)` excursion

If the clean peak is a Robin counterexample, then

\[
\log G(C)-\gamma>0.
\tag{31}
\]

Rearranging (6) gives

\[
\mathcal M_*(p)
>
T(C)+\Phi_{\ge2}(X)h(p)-Q(p,X).
\tag{32}
\]

Along any unbounded sequence of clean counterexample peaks, equations (23), (25), and (30) prove (8):

\[
\liminf
\sqrt p\log p\;\mathcal M_*(p)
\ge2\sqrt2.
\]

The two copies of `sqrt(2)` have different origins. One is the active higher-layer mass already visible in the self-tangent selector; the other is the Euler-product truncation tax from the large primes whose second layer has not yet activated. Their sum is therefore not obtained by inserting a known Ramanujan coefficient by hand.

## 6. The remaining Mertens remainder is a nonlocal Chebyshev tail

Mertens' product theorem gives `E(p)->0`, while the prime number theorem gives `Delta(p)h(p)->0`. Hence

\[
\mathcal M_*(p)\to0.
\tag{33}
\]

From (14), differentiating between prime jumps and then taking the improper limit gives the exact tail representation

\[
\boxed{
\mathcal M_*(p)
=
\int_p^\infty
\left[
\Delta(t)h'(t)-\bigl(h(t)-k(t)\bigr)
\right]dt,
}
\tag{34}
\]

where the integral is understood in the convergent improper sense supplied by (33). Since `h'(t)<0`, a positive excursion of `mathcal M_*` requires sufficiently negative weighted history of `vartheta(t)-t` after the selected boundary, after paying the deterministic positive `h-k` term.

Equation (34) identifies the actual unresolved source theorem. `RE-007` constrains the endpoint `psi(p)-p`; (34) shows that the clean counterexample height also demands a nonlocal future-tail alignment. An endpoint estimate alone cannot supply it.

## 7. Prior art, controls, and evidence boundary

The finite Mertens-product error in (4) is classical. Diamond--Pintz proved that the ordinary Mertens product changes sign in both directions, and Lamzouri derived an explicit normalized zero formula and explained its prime-square bias. Those results are important boundaries: ordinary Mertens-product oscillation is not new, and its sign by itself cannot settle (8). The object here is the **endpoint-subtracted** combination `M_*(p)=E(p)-Delta(p)h(p)` evaluated at boundary primes selected simultaneously by the clean CA self-tangent condition.

Lamzouri's normalized remainder also naturally lives at square-root scale, so the scale in (8) is not claimed as novel analytic-number-theory phenomenology. The Mathia-specific contribution is the exact splice (6), which shows that the clean CA selector removes the endpoint Chebyshev term and forces the remaining source history to exceed the two independent CA/Euler-product taxes. Nicolas's Ramanujan analysis already contains the characteristic `sqrt(2)-1` coefficient discussed in `RE-007`; no novelty is claimed for that coefficient either.

As a finite regression check, the safe clean peak `C_2` from `RE-005`, whose rightmost included prime is `p=53`, satisfies the exact identity (6) numerically to ordinary high-precision rounding. It remains well below the Robin barrier, so this check is only a sign/normalization control and is not asymptotic evidence for (8).

The clean-boundary hypothesis is load-bearing throughout. Peaks touching a higher-layer or tied transition remain in the exceptional chamber isolated by `RE-004`; (6) does not replace their selector. Nor does (8) prove that the required Mertens excursion is impossible. Diamond--Pintz show that the ordinary product oscillates, while Lamzouri's zero formula explains why square-root normalization is natural; neither theorem supplies the **source-selected endpoint-subtracted lower bound** required here or rules it out.

Finally, (8) is a necessary condition only along a clean counterexample subsequence. Under RH failure, `RE-001` gives infinitely many regular self-tangent counterexample peaks, but `RE-004` still allows them in principle to concentrate on the zero-density exceptional transition chamber. A complete Robin argument must therefore exclude both that exceptional concentration and the clean source-history excursion. The present finding sharpens the clean obligation without proving Robin's inequality or RH.