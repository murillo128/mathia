# RE-178 — Subcritical Euler-jet order is exponent-neutral for KV tail capacity

**Status:** `EXACT-DERIVED + PRIME-SUPPORTED + EULER-BOUNDARY-JETS + GROWING-JET-ORDER + KV-TAIL-CAPACITY + SIGN-PHASE-COMPLEXITY + METHOD-BOUNDARY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-175, RE-176, RE-177.

`RE-175` shows that matching finitely many right boundary Euler jets forces additional sign changes in a prime-supported multiplicity perturbation. `RE-176` and `RE-177` quantify the first nontrivial case: after a Robin-scale deletion packet near `p`, exact Mertens and first-slope matching leave a first-slope debt of order

\[
d_p\asymp \frac1{\sqrt p\log p},
\]

and a tail beginning at `Y` with `M` maximal sign-constant phases has only

\[
(M+\ell_{\rm KV}(Y))e^{-bV(Y)},
\qquad
\ell_{\rm KV}(Y):=\frac{\log Y}{V(Y)},
\qquad
V(Y):=\frac{(\log Y)^{3/5}}{(\log\log Y)^{1/5}},
\]

of absolute first-slope capacity. This yields the leading tradeoff

\[
bV(Y)\le \left(\frac12+\kappa+o(1)\right)\log p
\]

when `M=p^{\kappa+o(1)}`.

A natural next hope is that higher Euler boundary derivatives make the remote tail much more expensive and turn the linear sign-phase tariff into a stronger leading obstruction. The scalar capacity side does **not** do this at any fixed order, nor at any jet order below a sharp logarithmic crossover.

Let

\[
F_s(q):=-\log(1-q^{-s}),
\qquad
J_j(q):=\left.\partial_s^jF_s(q)\right|_{s=1},
\qquad j\ge1.
\]

For a prime-supported multiplicity discrepancy

\[
\Delta\vartheta(x)=\sum_{q\le x}c_q\log q
\]

satisfying the KV envelope

\[
|\Delta\vartheta(x)|\le C_b x e^{-bV(x)},
\]

suppose the nonzero coefficients after `Y` form at most `M` maximal sign-constant phases. If the jet order `j=j(Y)` satisfies

\[
j=o(V(Y)),
\]

then the absolute `j`-th boundary-jet capacity of the tail obeys

\[
\boxed{
\sum_{q\ge Y}|c_q|\,|J_j(q)|
\ll_b
(\log Y)^{j-1}
\bigl(M+\ell_{\rm KV}(Y)\bigr)e^{-bV(Y)}.
}
\tag{1}
\]

The implied estimate is uniform in this subcritical growing-order regime. For `j=1`, (1) is the capacity law behind `RE-177`. Each further derivative contributes only one factor of `log Y`; crucially, the dependence on the number of sign phases remains **linear**.

At the `RE-177` placement scale `V(Y)=Theta(log p)`,

\[
\log Y=(\log p)^{5/3+o(1)},
\]

so after normalizing the `j`-th jet by its natural selector-scale factor `(log p)^{j-1}`, (1) becomes

\[
\boxed{
\frac1{(\log p)^{j-1}}
\sum_{q\ge Y}|c_q|\,|J_j(q)|
\ll_b
\left(\frac{\log Y}{\log p}\right)^{j-1}
\bigl(M+\ell_{\rm KV}(Y)\bigr)e^{-bV(Y)}.
}
\tag{2}
\]

Consequently,

\[
\boxed{
j=o\!\left(\frac{\log p}{\log\log p}\right)
\quad\Longrightarrow\quad
\left(\frac{\log Y}{\log p}\right)^{j-1}=p^{o(1)}.}
\tag{3}
\]

Thus every fixed collection of jets, and even a subcritical growing number of jets, is **leading-exponent neutral on the scalar KV-capacity side**. Whenever such a jet leaves a residual debt of the natural size

\[
d_p(\log p)^{j-1}p^{o(1)},
\]

the corresponding scalar capacity inequality still gives only

\[
\boxed{
bV(Y)\le
\left(\frac12+\kappa+o(1)\right)\log p
\qquad
(M=p^{\kappa+o(1)}),}
\tag{4}
\]

exactly the leading exponent already visible from the first slope.

The first order at which higher derivatives can alter a polynomial-in-`p` capacity exponent by their raw logarithmic leverage is

\[
\boxed{
j_{\rm cap}(p)\asymp\frac{\log p}{\log\log p}.}
\tag{5}
\]

Indeed, if `j~c log p/log log p`, then

\[
\left(\frac{\log Y}{\log p}\right)^{j-1}
=p^{2c/3+o(1)}
\]

throughout `V(Y)=Theta(log p)`. Equation (5) is a **capacity crossover**, not a source-rigidity theorem: it says where higher Euler derivatives first have enough scalar weight to affect the leading polynomial bookkeeping. It does not say that matching that many derivatives is available from Robin, that their residual debts are independent, or that a control realizing them exists.

The practical boundary is therefore sharper than the final question of `RE-177`. Adding any fixed number of higher boundary jets cannot produce a superlinear leading sign-complexity tariff by repeating the same scalar Abel/KV argument. A genuine improvement must exploit **joint moment geometry across several jets**, let the number of matched derivatives grow to at least the crossover scale, or use ordinary-prime/integer-multiplicity structure that is absent from scalar capacity estimates.

## 1. Exact higher boundary kernels have one logarithm per derivative

The Euler factor has the absolutely convergent expansion for `s>1`

\[
F_s(q)
=\sum_{n\ge1}\frac{q^{-ns}}n.
\]

For every integer `j>=1`, termwise differentiation gives

\[
\boxed{
J_j(q)
=(-\log q)^j
\sum_{n\ge1}n^{j-1}q^{-n}.}
\tag{6}
\]

This is the same exact kernel used qualitatively in `RE-175`, but here the dependence on a growing `j` matters. The elementary inequality

\[
n\le2^{n-1}
\qquad(n\ge1)
\]

implies

\[
n^{j-1}\le2^{(n-1)(j-1)}
\]

and therefore, whenever `2^{j-1}<q`,

\[
\sum_{n\ge1}n^{j-1}q^{-n}
\le
\frac{q^{-1}}{1-2^{j-1}/q}.
\tag{7}
\]

If `j=o(V(Y))`, then `j=o(log Y)` because

\[
V(Y)=o(\log Y).
\]

Hence `2^j/Y=o(1)`, and uniformly for all `q>=Y`,

\[
\boxed{
|J_j(q)|
\le(1+o(1))\frac{(\log q)^j}{q}.}
\tag{8}
\]

The prime-power part of the Euler factor is therefore harmless throughout the growing-order range used in (1). The relevant tail weight is still one Chebyshev jump `c_q log q` multiplied by

\[
w_j(q):=\frac{(\log q)^{j-1}}q.
\tag{9}
\]

## 2. Phasewise Abel summation keeps the sign-complexity cost linear

The measure `dDelta theta` has an atom `c_q log q` at each modified prime. On a maximal phase on which all nonzero `c_q` have the same sign,

\[
d|\Delta\vartheta|
=\pm d\Delta\vartheta.
\]

Thus phasewise Stieltjes integration by parts with the weight (9) gives a boundary contribution at each phase endpoint plus an integral involving `|Delta theta(x)| |w_j'(x)|`.

Write

\[
L:=\log Y,
\qquad
W(u):=V(e^u)=\frac{u^{3/5}}{(\log u)^{1/5}}.
\]

For `u` large,

\[
uW'(u)
=\left(\frac35-\frac1{5\log u}\right)W(u).
\tag{10}
\]

Because `j=o(W(L))`, the function

\[
u^{j-1}e^{-bW(u)}
\]

is already decreasing at `u=L` and remains in its lower-end Laplace regime for `u>=L`. In particular, both the phase-endpoint envelope and the integral remainder are uniform in the admitted range:

\[
(\log x)^{j-1}e^{-bV(x)}
\le
(1+o(1))L^{j-1}e^{-bV(Y)},
\qquad x\ge Y,
\tag{11}
\]

and

\[
\begin{aligned}
\int_Y^\infty
|\Delta\vartheta(x)|\,|w_j'(x)|\,dx
&\ll_b
\int_L^\infty
u^{j-1}e^{-bW(u)}\,du\\
&\ll_b
L^{j-1}\frac{L}{W(L)}e^{-bW(L)}\\
&=
L^{j-1}\ell_{\rm KV}(Y)e^{-bV(Y)}.
\end{aligned}
\tag{12}
\]

The final estimate follows by one-sided Laplace integration by parts: for `j=o(W(L))`, the logarithmic derivative of the integrand is

\[
\frac{j-1}{u}-bW'(u)
=-(1+o(1))bW'(u),
\]

while `|W''(u)|/W'(u)^2=O(1/W(u))`, so the endpoint approximation is uniform.

There are `O(M)` phase endpoints and the integral pieces concatenate over the disjoint phases. Hence

\[
\int_{[Y,\infty)} w_j\,d|\Delta\vartheta|
\ll_b
L^{j-1}
\bigl(M+\ell_{\rm KV}(Y)\bigr)e^{-bV(Y)}.
\tag{13}
\]

Combining (8), (9), and (13) proves (1). The important structural feature is visible directly in (13): **new sign phases only reset the boundary term**. Higher derivatives make each reset more heavily weighted in logarithmic location, but they do not change the linear count of resets.

## 3. The selector-normalized crossover is `log p / log log p`

The deletion packet used in `RE-173` and inherited by `RE-175`--`RE-177` has Mertens debt

\[
d_p\asymp(\sqrt p\log p)^{-1}.
\]

At primes on a fixed multiplicative scale around `p`, (6) and `H(q)~1/q` show that the `j`-th jet is naturally measured in units of

\[
d_p(\log p)^{j-1}
\]

once one lower logarithmic location difference has been extracted. This motivates the normalization in (2); it is not an additional arithmetic assumption.

Now assume the remote tail lies on the moving KV horizon, so `V(Y)=Theta(log p)`. Inverting the definition of `V` gives

\[
\log Y
=(\log p)^{5/3+o(1)},
\tag{14}
\]

and more precisely

\[
\log\frac{\log Y}{\log p}
=\left(\frac23+o(1)\right)\log\log p.
\tag{15}
\]

Therefore

\[
\log\left[
\left(\frac{\log Y}{\log p}\right)^{j-1}
\right]
=
\left(\frac23+o(1)\right)j\log\log p.
\tag{16}
\]

Equation (3) follows immediately. Conversely, for

\[
j\sim c\frac{\log p}{\log\log p},
\]

(16) becomes `(2c/3+o(1)) log p`, yielding the polynomial factor stated after (5).

This identifies a real method boundary. A fixed-order extension of the `RE-177` argument can improve constants and polylogarithmic factors, and `RE-175` still forces additional qualitative sign changes, but it cannot improve the **leading polynomial relation between remote KV distance and sign-phase complexity**. Scalar higher-jet capacity only enters that leading exponent once the jet order itself grows on the scale (5).

## 4. Adversarial checks and scope boundary

Several possible overclaims are excluded explicitly.

First, (1) is a capacity upper bound, not a lower bound on the debt left by exact `j`-jet matching. Different moments can cancel jointly, and the amount of residual `j`-th debt depends on the preceding sign geometry. Equation (4) is therefore asserted only when a scalar residual debt of natural selector size is independently available. `RE-178` does **not** prove that every higher jet produces such a debt.

Second, the restriction `j=o(V(Y))` is substantive. When `j` approaches the local KV decay parameter, the factor `(log x)^{j-1}` can move the saddle of the weighted tail away from `Y`; then the endpoint capacity formula (12) is no longer uniform. The crossover (5) lies safely inside the admitted regime because `V(Y)=Theta(log p)` there.

Third, the phase count `M` is finite. An infinite-sign tail requires a different complexity control. `RE-178` only says that for finite `M`, each extra phase enters scalar fixed/subcritical jet capacity linearly.

Fourth, the boundary jets remain **extra matched-control information**. Nothing here derives `D_Q^{(j)}(1+)=0` from Robin's criterion. The result prices what those coordinates would buy if they were legitimately available; it does not promote them to source-native Robin invariants.

Finally, this does not duplicate the terminal moment hierarchy of `RE-159`--`RE-160`. Those findings study Taylor moments of flexible generalized-label insertion packets near a finite terminal horizon and the resulting ambiguity of the Robin influence itself. Here the labels remain ordinary primes, the coordinates are derivatives of the Euler discrepancy at `s=1`, the control is a global KV envelope, and the question is the remote capacity of a many-sign compensating tail.

## 5. Representation and prior-art audit

The proof has a generic analytic layer and a line-specific arithmetic layer.

The generic layer is phasewise Abel/Stieltjes summation for a signed cumulative function under an envelope `x e^{-bV(x)}`. For weights `(log x)^{j-1}/x`, each sign phase contributes one boundary reset and the remaining integral has the standard one-sided Laplace length `log Y/V(Y)`. This part would apply to another atomic source with the same cumulative envelope.

The Euler-specific layer is the exact identity (6), which turns the `j`-th right boundary derivative of a prime Euler factor into the weighted Chebyshev kernel `(log q)^j/q` up to a uniformly negligible prime-power correction in the admitted range. The Robin-specific layer is the debt scale `d_p~1/(sqrt(p) log p)`, the selector normalization by `(log p)^{j-1}`, and the comparison with the moving sign-complexity horizon of `RE-177`.

The load-bearing KV source envelope is already anchored in `research/robin_extremal/SOURCES.md` through the line's prime-number-theorem source. The remaining ingredients are the elementary Euler-factor expansion, Stieltjes summation, and an endpoint Laplace estimate derived above. A prior-art search found the expected general literature on Euler products, logarithmic derivatives, and Korobov--Vinogradov estimates, but no result needed as a new external theorem for (1)--(5). No new source anchor is required.

## 6. Research consequence

The final open sentence of `RE-177` can now be narrowed. **Higher boundary jets do not automatically impose a superlinear sign-complexity tariff.** On the scalar capacity side, every fixed jet and every jet order

\[
j=o(\log p/\log\log p)
\]

is exponent-neutral at the moving KV horizon. A stronger closure must therefore use at least one mechanism not present in the repeated scalar argument:

- simultaneous moment geometry across many boundary jets rather than one coordinate at a time;
- jet order reaching the crossover `Theta(log p/log log p)` with uniform control of the Chebyshev/moment structure;
- or genuinely discrete ordinary-prime/integer-multiplicity information that makes highly oscillatory compensation impossible.

This is a negative result about the present method, but it removes a misleading next step. Merely differentiating the Euler boundary identity a few more times cannot turn `RE-177` into a stronger leading placement theorem.