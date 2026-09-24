# FD-309 — GRH principal-frequency bounds are tangent to the source ceiling

- **Date:** 2026-09-24
- **Status:** proved GRH threshold tangency and excluded the classical additive-bound route from the live capacity range
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens source ceiling / Fejér low-pass witness / GRH Möbius exponential sums / principal-frequency estimate / threshold tangency / route obstruction
- **Depends on:** FD-300, FD-304, FD-307, FD-308
- **Classification:** `LITERATURE+DERIVED + GRH-CONDITIONAL + THRESHOLD-TANGENCY + NEGATIVE/OBSTRUCTION + FRONTIER-CORRECTION`

## Claim

Let

\[
c:=1-\log_2(3/2)=0.4150374992\ldots
\tag{1}
\]

and retain the near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)},
\qquad
x=N^{\lambda+o(1)}.
\tag{2}
\]

FD-300 already gives the unconditional source ceiling

\[
\boxed{
\lambda\le \lambda_{\rm src}:=\frac1{2c}
=1.2047104198\ldots .
}
\tag{3}
\]

Under RH, FD-304 and FD-307 write the capacity-bearing shell as

\[
Q=x^{\rho+o(1)},
\qquad
2c\le \rho\le1,
\qquad
X=NQ=N^{1+\lambda\rho+o(1)},
\tag{4}
\]

and, throughout the nonvacuous common-window range

\[
\lambda>\frac{3}{10c}=0.7228262519\ldots,
\tag{5}
\]

force a frequency `alpha_*` satisfying

\[
\|\alpha_*\|_{\mathbb T}
\le
\delta_N
:=
N^{-1/4-(3c/2)\lambda+o(1)}
\tag{6}
\]

and

\[
|F_X(\alpha_*)|
\ge
X^{1/2}
N^{(9c/4)\lambda-5/8-o(1)},
\tag{7}
\]

where

\[
F_X(\alpha)
=
\sum_{X\le n<2X}\mu(n)e(n\alpha).
\tag{8}
\]

FD-308 left open whether a Möbius bound tailored to the much narrower principal-frequency neighborhood (6) could rule out (7) inside the live interval (3). The classical GRH exponential-sum theorem of Baker--Harman is strong enough to test this directly.

Assume the generalized Riemann hypothesis for Dirichlet `L`-functions. At the GRH endpoint, Baker--Harman gives both the uniform estimate

\[
\max_{\alpha\in\mathbb T}
\left|
\sum_{n\le Y}\mu(n)e(n\alpha)
\right|
\ll_\varepsilon Y^{3/4+\varepsilon}
\tag{9}
\]

and the sharper rational-arc estimate

\[
\left|
\sum_{n\le Y}\mu(n)e(n\alpha)
\right|
\ll_\varepsilon
Y^{1/2+\varepsilon}
q^{1/2}
\bigl(1+Y|\alpha-a/q|\bigr)^{1/2}
\tag{10}
\]

for reduced `a/q`. In particular, on the principal arc `a/q=0/1`, the dyadic block (8) satisfies

\[
\boxed{
|F_X(\alpha)|
\ll_\varepsilon
X^{1/2+\varepsilon}
\bigl(1+X\|\alpha\|_{\mathbb T}\bigr)^{1/2}.
}
\tag{11}
\]

The new threshold audit is that **neither (9) nor the frequency-sensitive strengthening (11) can contradict the FD-307 witness anywhere below the already-existing FD-300 source ceiling**.

For the principal-frequency estimate (11), comparison with (6)--(7) yields a contradiction only if

\[
\boxed{
\lambda>
\lambda_{\rm BH,loc}(\rho)
:=
\frac1{3c-\rho/2}.
}
\tag{12}
\]

Because `rho>=2c`,

\[
\boxed{
\lambda_{\rm BH,loc}(\rho)
\ge
\lambda_{\rm BH,loc}(2c)
=
\frac1{2c}
=
\lambda_{\rm src}.
}
\tag{13}
\]

The inequality required for a genuine power contradiction is strict, so even at the shallowest RH-allowed shell the Baker--Harman principal-frequency estimate merely **touches** the source ceiling; it does not enter the live range.

The global bound (9) has the same tangency. It contradicts (7) only if

\[
\boxed{
\lambda>
\lambda_{\rm BH,unif}(\rho)
:=
\frac7{2(9c-\rho)},
}
\tag{14}
\]

and again

\[
\boxed{
\lambda_{\rm BH,unif}(\rho)
\ge
\lambda_{\rm BH,unif}(2c)
=
\frac1{2c}
=
\lambda_{\rm src}.
}
\tag{15}
\]

Thus even after strengthening the ambient hypothesis from RH to full GRH and replacing the unconditional `X^(4/5)` minor-arc ceiling of FD-306 by the classical GRH-quality additive Möbius bounds, the live Farey capacity interval is unchanged.

At balanced depth `lambda=1`, the FD-307 witness remains at size

\[
|F_X(\alpha_*)|
\ge
X^{0.654417\ldots-o(1)}
\quad\text{to}\quad
X^{0.668755\ldots-o(1)},
\tag{16}
\]

as `rho` ranges from `1` down to `2c`. The Baker--Harman uniform ceiling is `X^(3/4+epsilon)`, while the specialized principal-frequency form (11) is no smaller than about `X^0.7616` on the shallow shell and becomes weaker on deeper shells at the edge of the FD-307 localization window. Therefore the remaining gap is still a fixed power, not a logarithmic bookkeeping loss.

The practical conclusion is sharper than FD-308: **classical GRH additive cancellation, including the principal-arc dependence on `alpha`, is exactly too weak at the source boundary**. Any generic pointwise Möbius route that closes the balanced or other live depths must improve on the Baker--Harman `3/4` scale or exploit additional structure not present in a generic additive exponential sum.

## 1. Passing the Baker--Harman prefix estimate to the fixed dyadic block

Write

\[
S(Y,\alpha)
:=
\sum_{n\le Y}\mu(n)e(n\alpha).
\tag{17}
\]

Then, up to immaterial endpoint conventions,

\[
F_X(\alpha)
=
S(2X,\alpha)-S(X,\alpha).
\tag{18}
\]

Under GRH for Dirichlet `L`-functions, Baker--Harman's rational-arc estimate (10) with `q=1` and `a=0` gives

\[
|S(Y,\alpha)|
\ll_\varepsilon
Y^{1/2+\varepsilon}
\bigl(1+Y\|\alpha\|_{\mathbb T}\bigr)^{1/2}.
\tag{19}
\]

Applying this at `Y=X` and `Y=2X` proves (11). The same subtraction applied to (9) gives

\[
\boxed{
|F_X(\alpha)|
\ll_\varepsilon X^{3/4+\varepsilon}
}
\tag{20}
\]

uniformly in `alpha`.

No smooth cutoff or transfer between unrelated intervals is being used. Both estimates apply to exactly the same fixed block `[X,2X)` appearing in FD-307.

## 2. The principal-frequency estimate touches the source ceiling exactly

Insert the FD-307 localization (6) into (11). Since

\[
X\delta_N
=
N^{
3/4+\lambda(\rho-3c/2)+o(1)
},
\tag{21}
\]

and `rho>=2c`, the exponent in (21) is at least

\[
\frac34+\frac{c\lambda}{2}>0.
\tag{22}
\]

Hence throughout the live polynomial regime `X delta_N` tends to infinity by a fixed power. Evaluating (11) at the worst allowed point of the FD-307 arc therefore gives

\[
|F_X(\alpha_*)|
\ll
X^{1/2}
N^{
3/8+\lambda\rho/2-3c\lambda/4+o(1)
}.
\tag{23}
\]

The forced lower bound (7) exceeds (23) by a power only if

\[
\frac{9c\lambda}{4}-\frac58
>
\frac38+rac{\lambda\rho}{2}-\frac{3c\lambda}{4}.
\tag{24}
\]

Rearranging,

\[
3c\lambda-\frac{\rho\lambda}{2}>1,
\tag{25}
\]

which is exactly (12):

\[
\lambda>
\frac1{3c-\rho/2}.
\tag{26}
\]

The denominator is positive throughout `rho<=1`, since `3c-1/2>0`. Moreover the right-hand side is increasing in `rho`, so its minimum on the RH shell range occurs at `rho=2c`. There

\[
3c-\frac{2c}{2}=2c,
\tag{27}
\]

and therefore

\[
\lambda_{\rm BH,loc}(2c)
=
\frac1{2c}
=
\lambda_{\rm src}.
\tag{28}
\]

This is an exact algebraic tangency, not a numerical accident. At `lambda=lambda_src` and `rho=2c` the lower and upper power exponents coincide, while all `epsilon` and `o(1)` losses prevent a contradiction. For every deeper shell the Baker--Harman threshold moves strictly above the source ceiling.

Numerically,

\[
\lambda_{\rm BH,loc}(2c)
=1.2047104198\ldots,
\qquad
\lambda_{\rm BH,loc}(1)
=1.3420792201\ldots .
\tag{29}
\]

So the frequency-sensitive estimate cannot remove even a sliver of the interval still permitted by FD-300.

## 3. The uniform `3/4` theorem has the same boundary tangency

The uniform estimate (20) can be compared directly with (7). Since

\[
X=N^{1+\lambda\rho+o(1)},
\tag{30}
\]

the lower bound (7) has `N`-exponent

\[
-\frac18
+\lambda\left(\frac\rho2+\frac{9c}{4}\right),
\tag{31}
\]

whereas (20) has `N`-exponent

\[
\frac34(1+\lambda\rho).
\tag{32}
\]

A power contradiction requires

\[
-\frac18
+\lambda\left(\frac\rho2+\frac{9c}{4}\right)
>
\frac34(1+\lambda\rho).
\tag{33}
\]

Equivalently,

\[
-\frac78
+
\frac\lambda4(9c-\rho)>0,
\tag{34}
\]

or

\[
\lambda>
\frac7{2(9c-\rho)},
\tag{35}
\]

which is (14). This threshold is also increasing in `rho`. At the shallow shell,

\[
9c-2c=7c,
\tag{36}
\]

so

\[
\lambda_{\rm BH,unif}(2c)
=
\frac7{14c}
=
\frac1{2c}
=
\lambda_{\rm src}.
\tag{37}
\]

At the deepest allowed shell,

\[
\lambda_{\rm BH,unif}(1)
=1.2795496016\ldots .
\tag{38}
\]

The uniform theorem is in fact stronger than the simple `q=1` specialization near the outer edge of the FD-307 arc for deeper shells, but this does not change the conclusion: the minimum contradiction threshold of either Baker--Harman route is exactly the already-known source ceiling.

## 4. Balanced-depth calibration

Take `lambda=1`. FD-307 gives

\[
\delta_N
=N^{-0.8725562489\ldots+o(1)}
\tag{39}
\]

and

\[
|F_X(\alpha_*)|
\ge
X^{1/2}N^{0.3088343734\ldots-o(1)}.
\tag{40}
\]

For the shallowest RH-allowed shell `rho=2c`,

\[
X=N^{1.8300749986\ldots+o(1)},
\tag{41}
\]

so (40) is

\[
|F_X(\alpha_*)|
\ge
X^{0.6687550366\ldots-o(1)}.
\tag{42}
\]

At `rho=1`,

\[
X=N^{2+o(1)}
\tag{43}
\]

and the same lower bound becomes

\[
|F_X(\alpha_*)|
\ge
X^{0.6544171867\ldots-o(1)}.
\tag{44}
\]

Thus a shell-uniform generic additive theorem would need an exponent below approximately `0.6544` to kill every balanced carrier directly by pointwise comparison. The classical GRH exponent `3/4` misses this by about `0.0956` powers of `X` in the deepest-shell case.

The frequency-sensitive principal estimate does not recover that gap. At the outer edge `|alpha|=delta_N`, (11) has effective `X`-exponent

\[
0.7616064233\ldots
\tag{45}
\]

when `rho=2c`, and

\[
0.7818609378\ldots
\tag{46}
\]

when `rho=1`. These are only envelope calibrations: `alpha_*` might lie much closer to zero, in which case (11) is stronger. But FD-307 provides only the upper location bound (39), not a lower bound on `|alpha_*|`, so a proof that relies on additional closeness must first derive it from new structure.

This distinction is important. The present obstruction does not say that every frequency in the FD-307 arc saturates Baker--Harman. It says that the **available localization alone** is insufficient to turn the theorem into a contradiction anywhere in the source-live region.

## 5. Prior-art boundary

The load-bearing external input is R. C. Baker and G. Harman, *Exponential Sums Formed with the Möbius Function*, Journal of the London Mathematical Society (2) **43** (1991), 193--198, DOI `10.1112/jlms/s2-43.2.193`. The theorem is now anchored in `SOURCES.md`.

As a verification and current prior-art check, Wei Zhang, *On an exponential sum related to the Möbius function*, Proceedings of the American Mathematical Society **151** (2023), arXiv `2204.04613v2`, restates the Baker--Harman rational-arc estimate and improves the uniform zero-free-half-plane exponent for `1/2<a<4/7`. Zhang's formula is

\[
b(a)=\frac{8a-7a^2}{4-2a},
\tag{47}
\]

and his Remark 1 notes that it agrees with Baker--Harman at the GRH endpoint `a=1/2`, where

\[
b(1/2)=\frac34.
\tag{48}
\]

Thus that refinement does not move the `3/4` endpoint used in the audit above. A fresh literature search did not identify a published generic uniform additive Möbius theorem under GRH with an exponent below `3/4` that could alter the comparison.

No novelty is claimed for (9)--(11). The new content is the exact comparison of those classical GRH bounds with the source-selected Farey witness and the resulting tangency identities (28) and (37).

## 6. Adversarial audit and failure modes

Several stronger readings would be unjustified.

First, GRH is strictly stronger than the RH assumptions used in FD-304--FD-308 because Baker--Harman requires zero control for Dirichlet `L`-functions, not only for `zeta`. The result is therefore a **negative conditional audit**: even granting the stronger hypothesis does not close the live Farey range by this generic additive route.

Second, the comparison uses the same fixed block `[X,2X)` and the same source-selected frequency as FD-307. There is no averaging over `X`, no replacement by a prefix without paying the exact two-prefix decomposition (18), and no transfer between source-selected scales.

Third, (11) is evaluated using only the guaranteed upper bound `|alpha_*|<=delta_N`. It is possible that an independent argument could force `alpha_*` into a much smaller neighborhood where Baker--Harman becomes decisive. Such a further localization is **not** supplied by FD-307 and would be genuinely new information.

Fourth, the equality at `lambda=lambda_src`, `rho=2c` is not a contradiction. The lower bound has an `N^{-o(1)}` loss while Baker--Harman has an arbitrary `X^epsilon` loss. The present argument therefore requires a strict power separation and cannot claim closure of the endpoint.

Fifth, the source ceiling (3) remains unconditional. Strengthening RH to GRH cannot reopen depths `lambda>lambda_src`; it can only potentially shrink the interval below that ceiling. Equations (13) and (15) show that these particular GRH estimates fail to do so.

Sixth, no claim is made that exponent `3/4` is an optimal consequence of GRH in an absolute sense. The finding only records that the classical Baker--Harman theorem, including its sharper local rational-arc form and the later Zhang endpoint check, is tangent to the existing source boundary. A genuinely stronger additive theorem could still change the frontier.

Finally, this finding reinforces the ownership boundary already identified in FD-303 and FD-308. Once the Farey reduction has produced the generic fixed-block additive witness (6)--(8), improving a global Möbius exponential-sum exponent is naturally a `mobius_cancellation` problem. The Farey line should continue only if it can derive extra shell, frequency, multiplicity, or geometric structure that makes the witness more constrained than a generic additive Möbius sum.

## Consequences for the research line

FD-308 asked whether the low-frequency localization of FD-307 could make a tailored Möbius estimate strong enough inside

\[
0.7228262519\ldots
<\lambda
\le
1.2047104198\ldots .
\tag{49}
\]

FD-309 answers that question negatively for the strongest classical GRH input of the Baker--Harman type. Both the global `X^(3/4+epsilon)` theorem and the more refined `q=1` principal-frequency estimate first become contradictory only at or beyond the exact depth where FD-300 has already exhausted the finite length-`N` source capacity.

Therefore simply replacing the unconditional FD-306 exponent by a standard GRH additive estimate is a dead end. A nonvacuous next step must do at least one of three things:

1. derive a pointwise additive Möbius exponent strictly below the Baker--Harman barrier in the source-selected regime;
2. prove that the FD-307 witness lies **strictly closer to zero** than (6) by a new power, so that the local factor in (11) drops enough before the source ceiling; or
3. return upstream and exploit additional Farey/source structure—such as shell concentration, multiplicity, or compatibility among the many large blocks—before collapsing the problem to one generic Fourier coefficient.

The third option is the one that remains most clearly inside the mandate of `farey_discrepancy`. The first is generic Möbius cancellation and should not be duplicated here without a new Farey-specific constraint.

## Conclusion

The FD-307 low-pass witness survives a substantial strengthening of the analytic input. Under full GRH, Baker--Harman supplies both a uniform `X^(3/4+epsilon)` Möbius exponential-sum bound and a sharper principal-frequency estimate. Yet after inserting the RH shell floor `rho>=2c`, the contradiction threshold of **each** estimate has minimum

\[
\boxed{
\lambda=\frac1{2c}=1.2047104198\ldots,
}
\tag{50}
\]

exactly the unconditional source ceiling already proved by FD-300.

The current low-frequency certificate is therefore not merely beyond the reach of the unconditional `X^(4/5)` minor-arc theorem. **It is also beyond the reach of the classical GRH additive theory throughout the entire live Farey interval.** Progress at balanced depth now requires genuinely stronger Möbius cancellation or, more appropriately for this line, an additional Farey/source constraint before the final generic Fourier collapse.