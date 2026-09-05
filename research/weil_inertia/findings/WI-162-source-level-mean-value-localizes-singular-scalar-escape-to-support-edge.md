# WI-162 — source-level mean value localizes singular scalar escape to the support edge

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

WI-157 proves that regular `T`-dependent support-one scalar Lamzouri tests remain at the Montgomery--Taylor/CCLM barrier, while WI-158 and WI-159 show that the **displayed pointwise** BGSTB error `O((log T)^-1/2)` cannot by itself control singular near-extremizers with deweighted `L^1` norm of order `sqrt(log T)`. Those countermodels are logically correct at the theorem-statement interface, but they deliberately forget the arithmetic structure of the BGSTB proof.

Returning to that proof changes the boundary. The prime Dirichlet series `A_2` appearing in corrected `arXiv:2501.14545v3` is also amenable to the classical Montgomery--Vaughan mean-value theorem. This gives

\[
\boxed{
M_2(x,T)
=T\log x+O\!\bigl(T+x\log(2x)\bigr)
}
\qquad (1\le x\le T),
\]

in addition to the Goldston--Montgomery estimate `T log x + O(T sqrt(log T))` used by the authors. Propagating the better estimate through their exact `A_1+A_2+A_3` decomposition shows that on every fixed compact subinterval of `0<=alpha<1`, the normalized bulk uncertainty is `O(1/log T)`, not `O((log T)^-1/2)`. The larger error is genuinely an endpoint phenomenon at `x asymp T`.

Consequently a changing support-one scalar test is controlled under the strictly larger gate

\[
\|r_L\|_\infty=o(L),\qquad
\|r_L\|_1=o(L),\qquad
\int_{1-\delta}^{1}|r_L(\alpha)|\,d\alpha=o(\sqrt L)
\tag{1}
\]

for some fixed `delta>0`, where `L=log T`. In particular, the explicit singular near-extremizer constructed in WI-158 has all of its amplified high-frequency mass in the **interior** of the support and has only `O(1)` deweighted mass near `|alpha|=1`; it satisfies (1). Its synthetic order-one adverse pairing is therefore excluded by the actual BGSTB source proof even though it remains a valid countermodel to the weaker displayed theorem plus generic positivity/analyticity.

The surviving scalar loophole is thus much narrower: a support-one changing-test escape must push substantial deweighted mass into a neighborhood of the support edge `|alpha|=1`, become still more singular than the present `sqrt(log T)` construction, or use arithmetic information outside this scalar pair-correlation interface. No new zero proportion follows here.

## 1. Source-level input and the second mean-value estimate

Put

\[
L:=\log T.
\]

The corrected proof in Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB), `arXiv:2501.14545v3`, writes for the prefix pair form

\[
\mathcal F_{(0,T]}(x)+O(T^{1/2})+O(x)
=\frac{1}{2\pi}R(x,T),
\tag{2}
\]

where

\[
R(x,T)=\int_0^T|A_1(x,t)+A_2(x,t)+A_3(x,t)|^2dt,
\tag{3}
\]

and

\[
A_2(x,t)
=-\sum_{n\ge1}\frac{\Lambda(n)}{n^{1/2+it}}
\min\!\left\{\frac nx,\frac xn\right\}.
\tag{4}
\]

The source evaluates

\[
M_2(x,T):=\int_0^T|A_2(x,t)|^2dt
=T\log x+O(T\sqrt L)
\tag{5}
\]

by Goldston--Montgomery, uniformly through the endpoint `x=T`. For the present changing-test question, however, (4) allows a complementary estimate that is classical.

Write

\[
a_n(x):=\frac{\Lambda(n)}{\sqrt n}
\min\!\left\{\frac nx,\frac xn\right\}.
\tag{6}
\]

The Montgomery--Vaughan mean-value theorem for Dirichlet series gives, first for finite truncations and then by `L^2` convergence,

\[
\int_0^T\left|\sum_{n\ge1}a_n(x)n^{-it}\right|^2dt
=
T\sum_{n\ge1}|a_n(x)|^2
+O\!\left(\sum_{n\ge1}n|a_n(x)|^2\right).
\tag{7}
\]

The passage to the infinite series is legitimate because the second weighted sum below converges. Splitting at `n=x`,

\[
\sum_n|a_n(x)|^2
=
\frac1{x^2}\sum_{n\le x}\Lambda(n)^2n
+x^2\sum_{n>x}\frac{\Lambda(n)^2}{n^3},
\tag{8}
\]

while

\[
\sum_n n|a_n(x)|^2
=
\frac1{x^2}\sum_{n\le x}\Lambda(n)^2n^2
+x^2\sum_{n>x}\frac{\Lambda(n)^2}{n^2}.
\tag{9}
\]

The standard prime-number-theorem consequence

\[
\sum_{n\le u}\Lambda(n)^2=u\log u-u+O(u)
\tag{10}
\]

and partial summation give

\[
\boxed{
\sum_n|a_n(x)|^2=\log x+O(1)
},
\qquad
\boxed{
\sum_n n|a_n(x)|^2\ll x\log(2x)
}.
\tag{11}
\]

Substitution into (7) proves

\[
\boxed{
M_2(x,T)=T\log x+O\!\bigl(T+x\log(2x)\bigr).
}
\tag{12}
\]

This does not replace (5) near `x=T`; the useful source-level estimate is their minimum. For `x=T^\alpha`,

\[
\frac{M_2-T\log x}{TL}
\ll
\min\!\left(
L^{-1/2},
L^{-1}+\alpha T^{\alpha-1}
\right).
\tag{13}
\]

Thus every fixed margin `alpha<=1-delta` has normalized `M_2` error `O_delta(L^-1)`.

## 2. The other source terms preserve the interior improvement

The improvement in (13) would be useless if the `A_3` cross terms recreated an `L^-1/2` error in the interior. They do not. The corrected source gives

\[
M_1:=\int_0^T|A_1|^2dt
=\frac{T}{x^2}(L^2+O(L)),
\tag{14}
\]

\[
M_3:=\int_0^T|A_3|^2dt
\ll\frac{T}{x^2}+x,
\tag{15}
\]

and

\[
\int_0^T A_1\overline{A_2}\,dt\ll L.
\tag{16}
\]

Keep the first line of the source decomposition rather than its later coarse simplification:

\[
R=M_1+M_2
+O\!\left(\left|\int A_1\overline{A_2}\right|\right)
+O(\sqrt{M_1M_3})
+O(\sqrt{M_2M_3})
+O(M_3).
\tag{17}
\]

Let `x=T^alpha=e^y`, `y=alpha L`, and assume `0<=alpha<=1-delta`. From (12), `M_2\ll T(y+1)`. Dividing (17) by `TL` then gives

\[
\frac{\sqrt{M_1M_3}}{TL}
\ll e^{-2y}+\frac1{\sqrt{Tx}},
\tag{18}
\]

\[
\frac{\sqrt{M_2M_3}}{TL}
\ll
\frac{e^{-y}}{\sqrt L}
+rac{T^{-\delta/2}}{\sqrt L},
\tag{19}
\]

and

\[
\frac{M_3}{TL}
\ll\frac{e^{-2y}}L+\frac{T^{-\delta}}L.
\tag{20}
\]

The mixed term (16), as well as the `O(T^{1/2})+O(x)` error in (2), is smaller. Hence the normalized prefix form factor has, uniformly on `0<=alpha<=1-delta`, the error shape

\[
O_\delta\!\left(
 e^{-2L\alpha}
 +\frac{e^{-L\alpha}}{\sqrt L}
 +\frac1L
\right).
\tag{21}
\]

WI-161 already showed that the corrected first line of the prefix estimate survives subtraction from heights `2T` and `T`, and that the cross-boundary zero term is `O(T)` (indeed the source proves `O(T^{1/2}+x)`). Applying the same subtraction to (21) therefore yields the dyadic interior estimate

\[
\boxed{
F_T^{\rm dyad}(\alpha)
=L e^{-2L\alpha}+\alpha
+O_\delta\!\left(
 e^{-2L\alpha}
 +\frac{e^{-L\alpha}}{\sqrt L}
 +\frac1L
\right)
}
\tag{22}
\]

uniformly for `0<=alpha<=1-delta`, in the normalization of WI-157/WI-161.

On the remaining edge `1-delta<=alpha<=1`, WI-161 supplies

\[
\boxed{
F_T^{\rm dyad}(\alpha)
=L e^{-2L\alpha}+\alpha
+O(e^{-2L\alpha})+O(L^{-1/2}).
}
\tag{23}
\]

Equations (22)--(23) are the load-bearing refinement: the `L^-1/2` uncertainty only has to be paid where `alpha` approaches the support endpoint.

## 3. A broader changing-test gate

Let

\[
r_L(\alpha)=\phi_L(\alpha)-\frac{\phi_L''(\alpha)}{4L^2}
\tag{24}
\]

be the exact Lamzouri/BGSTB deweighted spectral profile from WI-157, real and even with support in `[-1,1]`. Integrating the error in (22) against `r_L` on `[0,1-delta]` gives

\[
\int_0^{1-\delta}e^{-2L\alpha}|r_L(\alpha)|d\alpha
\le\frac{\|r_L\|_\infty}{2L},
\tag{25}
\]

\[
\frac1{\sqrt L}
\int_0^{1-\delta}e^{-L\alpha}|r_L(\alpha)|d\alpha
\le\frac{\|r_L\|_\infty}{L^{3/2}},
\tag{26}
\]

and

\[
\frac1L\int_0^{1-\delta}|r_L(\alpha)|d\alpha
\le\frac{\|r_L\|_1}{L}.
\tag{27}
\]

The edge contribution from (23) is bounded by

\[
O\!\left(
\frac{\|r_L\|_\infty}{L}e^{-2(1-\delta)L}
+rac1{\sqrt L}\int_{1-\delta}^{1}|r_L(\alpha)|d\alpha
\right).
\tag{28}
\]

Therefore, for any fixed `delta>0`, the three conditions

\[
\boxed{
\|r_L\|_\infty=o(L),
\qquad
\|r_L\|_1=o(L),
\qquad
\int_{1-\delta}^{1}|r_L(\alpha)|d\alpha=o(\sqrt L)
}
\tag{29}
\]

imply that the complete integrated dyadic arithmetic error is `o(1)`.

This strictly contains the theorem-statement gate in WI-157,

\[
\|r_L\|_\infty=o(L),\qquad \|r_L\|_1=o(\sqrt L),
\tag{30}
\]

because large `L^1` mass is now allowed throughout the interior. What matters is whether the dangerous mass reaches the support edge where the short-Dirichlet-polynomial saving disappears.

## 4. WI-158's explicit singular family is controlled by the source proof

WI-158 chose

\[
f_L=g_L+h_L,
\qquad
h_L(u)=\varepsilon_L\psi(u)\cos(2\pi n_Lu),
\tag{31}
\]

up to a normalization tending to one, with

\[
\varepsilon_L=L^{-1/4},
\qquad n_L\asymp L^{3/2},
\qquad
\operatorname{supp}\psi\subset(-1/4,1/4),
\tag{32}
\]

while `g_L` is a smooth Montgomery--Taylor approximation supported in `(-1/2,1/2)`. It proved

\[
\|r_L\|_1=\Theta(\sqrt L),
\qquad
\|r_L\|_\infty=O(\sqrt L).
\tag{33}
\]

The key extra fact is support geometry. Since

\[
\phi_L=f_L*f_L,
\qquad
\phi_L''=f_L'*f_L',
\tag{34}
\]

the terms involving at least one copy of `h_L` are supported inside

\[
(-3/4,3/4)
\tag{35}
\]

(the `h_L*h_L` terms are even narrower). Thus on `3/4<=|alpha|<=1`, the profile `r_L` contains only the smooth `g_L*g_L` and `g_L'*g_L'/(4L^2)` pieces. The cutoff used in WI-158 has

\[
\|g_L\|_1=O(1),
\qquad
\|g_L'\|_1=O(1),
\tag{36}
\]

so Young's inequality gives

\[
\boxed{
\int_{3/4}^{1}|r_L(\alpha)|d\alpha=O(1).
}
\tag{37}
\]

Taking `delta=1/4`, equations (33) and (37) satisfy every condition in (29). Hence for the **actual arithmetic form factor governed by the BGSTB proof**,

\[
\boxed{
\text{integrated arithmetic error against the WI-158 family}=o(1).
}
\tag{38}
\]

This does not retract WI-158 or WI-159. Their precise conclusion was that the published pointwise asymptotic, even with generic positivity, analyticity and square structure, does not logically determine the changing-test integral. Their synthetic central oscillation is still a valid countermodel to that weaker information set. Equation (38) shows only that the countermodel violates additional source-specific arithmetic information already latent in the BGSTB `A_2` representation.

## 5. What survives

The scalar support-one loophole is now localized rather than merely labeled “nonuniform.” A family with global `\|r_L\|_1\asymp\sqrt L` can no longer exploit arbitrary interior frequencies: if its endpoint mass is `o(sqrt L)`, the source proof controls it. To retain order-one susceptibility at this scale, a candidate must instead arrange

\[
\int_{1-\delta}^{1}|r_L(\alpha)|d\alpha\asymp\sqrt L
\tag{39}
\]

for every fixed margin that removes the endpoint, or violate the broader global gates in (29). Equivalently, the live arithmetic problem has moved to a support-edge concentration regime where the associated Dirichlet-polynomial length is comparable with the height.

This suggests a much more specific next stress test than another generic form-factor regularity argument: determine whether near-CCLM Lamzouri factorizations can place `Theta(sqrt L)` deweighted mass in a shrinking edge layer while preserving their scalar cost, and if they can, whether endpoint mean-value/large-sieve information stronger than the pointwise BGSTB remainder controls that layer. A negative answer to either question would close another part of the growing-family scalar escape.

Nothing here constrains the matrix/Gram-defect improvements, joint multi-profile inequalities, higher correlations, or wider Fourier support. It also gives no new numerical lower bound for simple critical zeros.

## 6. Prior-art and novelty audit

The source decomposition and corrected dyadic theorem are literature-backed: S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*, `arXiv:2501.14545v3` (1 Sep 2026), Section 3, especially equations (3.4)--(3.8). Their proof supplies (2)--(5), (14)--(17), and the dyadic cross-boundary estimate. WI-161 already audited the sharper first-line spike error through prefix subtraction.

The mean-value input is classical: H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`. The standard Dirichlet-series corollary is exactly the form used in (7): `int_0^T |sum a_n n^{-it}|^2 dt = sum |a_n|^2 (T+O(n))` when the weighted square sum converges. The endpoint-strength estimate (5) remains the Goldston--Montgomery input cited by BGSTB: D. A. Goldston and H. L. Montgomery, *Pair correlation of zeros and primes in short intervals*, in *Analytic Number Theory and Diophantine Problems*, Progress in Mathematics 70 (1987), 183--203.

Classical pair-correlation literature already distinguishes the easier strict-interior range `x<=T^(1-epsilon)` from the endpoint `x=T`; the existence of an interior mean-value saving is therefore not claimed as new. A targeted audit around changing support-one tests, Montgomery--Vaughan mean values, the corrected BGSTB proof, and the recent Lamzouri scalar formulation did not locate the specific gate (29) or its application (38) to the WI-158 singular family. This absence is not used as a priority claim. The Mathia contribution recorded here is the exact source-level bridge from the classical `A_2` mean value to endpoint localization of the singular scalar loophole.

## Evidence boundary

Equations (2)--(5), (14)--(17), and the dyadic prefix/cross-boundary machinery are literature-backed by current `arXiv:2501.14545v3`. Equation (7) is classical Montgomery--Vaughan. Equations (8)--(13) and (18)--(29) are exact standard deductions from those inputs; (31)--(37) reuse the explicit construction and norm bounds already established in WI-158. Equation (38) is therefore a derived source-level consequence for that concrete family.

No claim is made that every singular support-one family satisfies (29), no new endpoint theorem is supplied, and no new zero proportion follows. The remaining possibility of `sqrt(L)`-scale deweighted mass concentrated at `|alpha|=1` is explicitly open.