# FD-307 — Fejér low-pass localization forces the principal major arc and closes deep capacity

- **Date:** 2026-09-24
- **Status:** proved principal-frequency localization and an RH-conditional deep-capacity exclusion
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / sliding Möbius energy / Fejér kernel / additive Fourier localization / principal major arc / capacity obstruction
- **Depends on:** FD-303, FD-304, FD-306
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + LOW-PASS-LOCALIZATION + PRINCIPAL-MAJOR-ARC-SELECTION + DEEP-CAPACITY-EXCLUSION + ROUTE-REDUCTION`

## Claim

Continue with

\[
L_N(x)=\sum_{x<d\le2x}|G_N(d)|,
\qquad
c:=1-\log_2(3/2)=0.4150374992\ldots,
\tag{1}
\]

and assume the near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)}.
\tag{2}
\]

Assume RH and write

\[
x=N^{\lambda+o(1)},
\qquad
Q=x^{\rho+o(1)},
\qquad
X=NQ,
\tag{3}
\]

for the dyadic shell supplied by FD-300. FD-304 gives

\[
2c\le \rho\le1
\tag{4}
\]

up to `o(1)` in the exponent. FD-303 gives the sliding moment

\[
J_\mu(X,N)
:=
\sum_{X\le y<2X}
\left|M(y+N)-M(y)\right|^2
\tag{5}
\]

with

\[
\frac{J_\mu(X,N)}{XN}
\ge
H,
\qquad
H:=N^{3c\lambda-1/2-o(1)}.
\tag{6}
\]

The new observation is that (5) is intrinsically a **low-pass certificate**. Define the fixed Möbius block

\[
F_X(\alpha)
:=
\sum_{X\le n<2X}\mu(n)e(n\alpha)
\tag{7}
\]

and the length-`N` Dirichlet kernel

\[
D_N(\alpha):=\sum_{r=1}^N e(r\alpha).
\tag{8}
\]

Whenever

\[
\boxed{
\lambda>\frac{3}{10c}
=0.7228262519\ldots,
}
\tag{9}
\]

the RH shell floor `Q>=x^(2c-o(1))` makes the terminal `N` sliding starts negligible, and one obtains

\[
\boxed{
\int_0^1
|F_X(\alpha)|^2|D_N(\alpha)|^2\,d\alpha
\gg
J_\mu(X,N).
}
\tag{10}
\]

Consequently there is a frequency `alpha_*` satisfying

\[
\boxed{
\|\alpha_*\|_{\mathbb T}
\le
N^{-1/4-(3c/2)\lambda+o(1)}
}
\tag{11}
\]

and

\[
\boxed{
|F_X(\alpha_*)|
\ge
X^{1/2}
N^{(9c/4)\lambda-5/8-o(1)}.
}
\tag{12}
\]

Thus throughout the common-window regime (9), the source-selected spectral witness is already polynomially larger than square-root scale and lies in a shrinking neighborhood of the **principal frequency `0`**. In particular, its location is not an arbitrary rational phase inherited from FD-305.

The localization becomes stronger when combined with the Vinogradov minor-arc ceiling of FD-306. If the carrying shell has exponent `rho` as in (3), then whenever

\[
\boxed{
\lambda>
\lambda_{\rm loc}(\rho)
:=
\frac{37}{90c-12\rho},
}
\tag{13}
\]

the lower bound (12) exceeds

\[
X^{4/5}(\log X)^{O(1)}.
\tag{14}
\]

Hence `alpha_*` must lie on one of the FD-306 major arcs. But (11) is already `o(X^(-2/5))` in the regime (9), so this principal neighborhood cannot meet any major arc centered at a nonzero reduced fraction with denominator `<X^(2/5)`. Therefore (13) forces

\[
\boxed{
\|\alpha_*\|_{\mathbb T}
\le X^{-3/5},
}
\tag{15}
\]

i.e. the relevant rational major arc is specifically the **principal `q=1` arc**.

This finally turns the major-arc localization into an exclusion. Under RH, partial summation from

\[
M(t)=O_\varepsilon(t^{1/2+\varepsilon})
\tag{16}
\]

gives uniformly on the principal arc

\[
\boxed{
|F_X(\alpha)|
\le
X^{9/10+o(1)}
\qquad
(\|\alpha\|\le X^{-3/5}).
}
\tag{17}
\]

Comparing (12) and (17), the near-capacity premise (2) is impossible whenever

\[
\boxed{
\lambda>
\lambda_{\rm kill}(\rho)
:=
\frac{41}{90c-16\rho}.
}
\tag{18}
\]

Since every carrying shell has `rho<=1`, this gives the shell-uniform consequence

\[
\boxed{
\lambda>
\frac{41}{90c-16}
=
1.9200711889\ldots
\quad\Longrightarrow\quad
L_N(x)<N^{1/2}x^{1+c-o(1)}
}
\tag{19}
\]

under RH, in the precise sense that no fixed positive near-capacity lower bound of the form (2) can persist in that polynomial-depth regime.

At the shallowest RH-allowed shell `rho=2c`, the exclusion threshold is already

\[
\boxed{
\lambda>
\frac{41}{58c}
=
1.7032112832\ldots .
}
\tag{20}
\]

Therefore for depths between (20) and the uniform ceiling (19), any surviving near-capacity shell is forced progressively toward the maximal denominator scale. Rearranging (18), survival requires

\[
\boxed{
\rho
\ge
\frac{90c-41/\lambda}{16}.
}
\tag{21}
\]

As `lambda` approaches `1.920071...` from below, the right side of (21) approaches `1`. The source carrier is thus squeezed simultaneously in additive frequency and in divisor-shell depth before it disappears altogether.

## 1. Removing the terminal sliding starts

FD-303 gives (6). To connect its sliding sums to the fixed block (7), restrict (5) to

\[
X\le y<2X-N.
\tag{22}
\]

For these starts, every term in

\[
S_N(y)=\sum_{r=1}^N\mu(y+r)
\tag{23}
\]

lies strictly inside `[X,2X)`. The omitted terminal range contains at most `N` starts, and trivially

\[
|S_N(y)|\le N.
\tag{24}
\]

Hence its total contribution is at most

\[
N^3.
\tag{25}
\]

On the other hand, (6) gives

\[
J_\mu(X,N)
\ge
XN H
=
N^2QH.
\tag{26}
\]

Using the RH shell floor from FD-304,

\[
Q\ge x^{2c-o(1)},
\tag{27}
\]

we obtain

\[
\frac{J_\mu(X,N)}{N^3}
\ge
N^{5c\lambda-3/2-o(1)}.
\tag{28}
\]

The exponent is positive precisely under (9). Thus the truncated sliding moment

\[
J_\mu^\circ(X,N)
:=
\sum_{X\le y<2X-N}|S_N(y)|^2
\tag{29}
\]

satisfies

\[
J_\mu^\circ(X,N)
=(1-o(1))J_\mu(X,N).
\tag{30}
\]

This is the same numerical threshold that appeared in FD-304 when removing moving-start boundary errors, but here it removes the endpoint leakage needed for an exact fixed-block Fourier representation.

## 2. Parseval turns sliding energy into a Fejér-weighted fixed-block spectrum

Extend the fixed block

\[
f_X(n):=\mu(n)\mathbf 1_{[X,2X)}(n)
\tag{31}
\]

by zero to all integers. Define

\[
T_N(y):=\sum_{r=1}^N f_X(y+r).
\tag{32}
\]

For every start in (22), `T_N(y)=S_N(y)`. Parseval for the discrete convolution therefore gives

\[
\begin{aligned}
J_\mu^\circ(X,N)
&\le
\sum_{y\in\mathbb Z}|T_N(y)|^2\\
&=
\int_0^1
|F_X(\alpha)|^2|D_N(\alpha)|^2\,d\alpha.
\end{aligned}
\tag{33}
\]

This proves (10). Up to normalization, `|D_N|^2` is exactly the Fejér kernel. The Farey-generated sliding anomaly is therefore not spectrally neutral: it heavily weights additive frequencies near `0`.

The elementary bounds

\[
|D_N(\alpha)|\le N,
\qquad
|D_N(\alpha)|\ll \|\alpha\|_{\mathbb T}^{-1}
\tag{34}
\]

are all that is needed below.

## 3. A polynomial principal-frequency spike is forced

Choose a sufficiently large fixed constant `A` and put

\[
\delta_\alpha
:=
\frac{A}{\sqrt{NH}}.
\tag{35}
\]

Outside

\[
\mathcal I
:=
\{\alpha:\|\alpha\|_{\mathbb T}\le\delta_\alpha\},
\tag{36}
\]

(34) and Parseval give

\[
\begin{aligned}
\int_{\mathbb T\setminus\mathcal I}
|F_X(\alpha)|^2|D_N(\alpha)|^2\,d\alpha
&\ll
\delta_\alpha^{-2}
\int_0^1|F_X(\alpha)|^2\,d\alpha\\
&\le
\frac{NH}{A^2}\,X.
\end{aligned}
\tag{37}
\]

Since (26) is `>=XNH`, taking `A` large enough makes (37) at most a fixed small fraction of the lower bound in (33). Hence

\[
\int_{\mathcal I}
|F_X(\alpha)|^2|D_N(\alpha)|^2\,d\alpha
\gg
XNH.
\tag{38}
\]

Using `|D_N|<=N`,

\[
\int_{\mathcal I}|F_X(\alpha)|^2\,d\alpha
\gg
\frac{XH}{N}.
\tag{39}
\]

The arc has measure `O(delta_alpha)`, so some `alpha_*` in it satisfies

\[
|F_X(\alpha_*)|^2
\gg
\frac{XH}{N\delta_\alpha}
\asymp
XH^{3/2}N^{-1/2}.
\tag{40}
\]

Taking square roots gives

\[
|F_X(\alpha_*)|
\gg
X^{1/2}H^{3/4}N^{-1/4}.
\tag{41}
\]

Substituting (6) yields (11)--(12). Note that the factor over square-root size is

\[
N^{(9c/4)\lambda-5/8-o(1)}.
\tag{42}
\]

This already grows polynomially once

\[
\lambda>\frac{5}{18c}=0.6692835666\ldots,
\tag{43}
\]

so every depth satisfying the stronger endpoint-removal condition (9) has a genuine power-above-square-root spike in the principal-frequency neighborhood.

This improves the localization mechanism of FD-305 in a different direction. FD-305 obtained a stronger unrestricted fourth-moment certificate from common-window correlations. Equation (41) is instead tied directly to the sliding origin of those correlations and therefore retains the low-frequency information that was lost when the shifts were compressed only through Wiener--Parseval.

## 4. Vinogradov minor arcs select denominator `q=1`

Write the selected shell as `Q=x^(rho+o(1))`, so

\[
X=N^{1+\lambda\rho+o(1)}.
\tag{44}
\]

The forced lower bound (12) has `N`-exponent

\[
-\frac18
+\lambda\left(\frac\rho2+\frac{9c}{4}\right),
\tag{45}
\]

whereas the FD-306 minor-arc ceiling `X^(4/5)(log X)^O(1)` has exponent

\[
\frac45(1+\lambda\rho).
\tag{46}
\]

Their difference is

\[
-\frac{37}{40}
+\lambda\left(\frac{9c}{4}-\frac{3\rho}{10}\right).
\tag{47}
\]

This is positive exactly under (13). Thus `alpha_*` must then lie in the major-arc set

\[
\mathfrak M_X
=
\bigcup_{q<X^{2/5}}
\bigcup_{(a,q)=1}
\left\{
\alpha:
\left\|\alpha-\frac aq\right\|_{\mathbb T}
\le
\frac{X^{-3/5}}q
\right\}.
\tag{48}
\]

It remains to determine which denominator is compatible with (11). From (11),

\[
\delta_\alpha X^{2/5}
=
N^{
3/20+\lambda(2\rho/5-3c/2)+o(1)
}.
\tag{49}
\]

For every `rho<=1`, the exponent in (49) is already negative throughout (9). Hence

\[
\delta_\alpha=o(X^{-2/5}).
\tag{50}
\]

Suppose an `alpha` in `mathcal I` belongs to a major arc centered at a nonzero reduced fraction `a/q`, `q<X^(2/5)`. Then

\[
\frac1q
\le
\left\|\frac aq\right\|_{\mathbb T}
\le
\|\alpha\|_{\mathbb T}
+
\left\|\alpha-\frac aq\right\|_{\mathbb T}
\le
\delta_\alpha+
\frac{X^{-3/5}}q.
\tag{51}
\]

Multiplying by `q` and using `q<X^(2/5)` plus (50) gives

\[
1\le o(1)+X^{-3/5},
\tag{52}
\]

a contradiction. Therefore the only major arc meeting `mathcal I` is the one centered at `0/1`, proving (15).

This answers the denominator-selection question left open by FD-306 in the range where the forced Fejér spike clears the Vinogradov minor-arc ceiling: the source mechanism does not merely force **some** rational major arc. It selects the principal denominator.

## 5. RH then rules out a sufficiently deep principal spike

For `||alpha||<=X^(-3/5)`, summation by parts gives

\[
F_X(\alpha)
=
O\left(
\sup_{X\le t\le2X}|M(t)|
+
|\alpha|
\int_X^{2X}|M(t)|\,dt
\right).
\tag{53}
\]

Under RH, for every fixed `epsilon>0`,

\[
M(t)=O_\varepsilon(t^{1/2+\varepsilon}),
\tag{54}
\]

so (53) yields

\[
|F_X(\alpha)|
\ll_\varepsilon
X^{1/2+\varepsilon}
+X^{-3/5}X^{3/2+\varepsilon}
\ll
X^{9/10+\varepsilon}.
\tag{55}
\]

The lower bound (12) beats (55) when

\[
-\frac18
+\lambda\left(\frac\rho2+\frac{9c}{4}\right)
>
\frac9{10}(1+\lambda\rho).
\tag{56}
\]

Equivalently,

\[
-\frac{41}{40}
+\lambda\left(\frac{9c}{4}-\frac{2\rho}{5}\right)>0,
\tag{57}
\]

which is precisely (18). Since (18) is stronger than the localization condition (13), there is no gap in the argument: whenever (57) is positive, the spike has already been forced onto the principal major arc before (55) is invoked.

The shell-uniform bound follows by taking the worst allowed `rho=1`, giving (19). At `rho=2c`, (18) reduces to (20). Between those endpoints, solving the negation of (18) gives the survival floor (21).

For example, at `lambda=1.8`, (21) requires

\[
\rho\ge0.91097\ldots,
\tag{58}
\]

and at `lambda=1.9` it requires

\[
\rho\ge0.98590\ldots.
\tag{59}
\]

Thus before the uniform contradiction at `lambda=1.920071...`, the capacity-bearing shell is already forced to the extreme top of the available divisor-depth range.

## 6. Prior-art boundary and adversarial review

The short-interval/Fourier connection through Dirichlet or Fejér kernels is classical. Gallagher-type inequalities and their weighted variants are part of the standard toolkit for translating short-interval moments into frequency information; the present finding does not claim that Parseval, the Fejér kernel, or short-sum spectral localization is new. A prior-art check included the Gallagher-lemma literature and modern Möbius short-interval work, including Matomäki--Radziwiłł and Matomäki--Teräväinen. None of that literature is used here to supply the lower bound (6): the anomaly is generated internally by the Farey block-Mertens capacity premise through FD-300 and FD-303.

The load-bearing external analytic inputs were already anchored before this finding. The RH Mertens estimate is the Titchmarsh--Heath-Brown/Littlewood criterion used in FD-304, and the Vinogradov-quality Möbius minor-arc estimate is the Robles input anchored for FD-306. `SOURCES.md` therefore needs no new dependency.

The main adversarial checks are as follows. First, (33) is an inequality in the correct direction: the fixed-block convolution contains all interior sliding starts, so a large interior moment forces a large Fourier-weighted integral. Second, endpoint removal costs at most `N^3`, and the RH shell floor makes this `o(J_mu)` exactly above (9); no unproved cancellation is used at the boundary. Third, the principal arc width in (35) is chosen from a lower bound for `J_mu`, so if the actual moment is larger the outside contribution is only easier to dominate. Fourth, no assumption that the Fejér kernel is supported near zero is made; its `||alpha||^(-2)` tail is summed against the exact Parseval energy `<=X`, producing (37). Fifth, the pointwise spike follows from local `L^2` mass and the actual measure of `mathcal I`, not from an unsupported concentration heuristic.

Sixth, the `q=1` conclusion uses the geometry of the exact major arcs from FD-306. A nonzero reduced fraction has circular distance at least `1/q` from zero, while the source-selected neighborhood is `o(X^(-2/5))`; hence no nonprincipal denominator `<X^(2/5)` can enter it. Seventh, the RH principal-arc bound (55) is obtained directly by partial summation and is not an imported major-arc asymptotic. Eighth, all inequalities are strict at the exponent thresholds; no endpoint claim is made. Ninth, the result is conditional on RH because both the shell floor (27) and the final Mertens estimate (54) use RH. Finally, (19) excludes the specific near-capacity block-Mertens premise, not every conceivable Farey representation or every spectral mechanism at smaller depth.

## 7. Consequence for the Farey route

FD-306 left a clean ownership question: could Farey source selection constrain the denominator of the surviving Möbius major arc, or had the problem already become a generic rational-twist question for `mobius_cancellation`?

FD-307 answers that question for the deep regime. The source mechanism retains one more piece of information that the fourth-moment compression had discarded: the large correlations came from **length-`N` sliding sums**. Their Fejér weight forces a power-scale coefficient into a principal neighborhood. Once the coefficient clears the Robles minor-arc ceiling, that neighborhood can intersect only the `q=1` major arc. Under RH, the same principal location is too rigid to support the required amplitude beyond (18).

So there are now two distinct outcomes. For

\[
\lambda>1.9200711889\ldots,
\tag{60}
\]

the near-capacity block-Mertens route is closed under RH. For somewhat smaller deep exponents, survival requires an increasingly top-heavy shell according to (21), while the source-selected spectral anomaly is already confined near frequency zero. Any further work in that surviving corridor should therefore focus on the joint relation between shell depth and the principal-frequency Möbius block, rather than unrestricted rational twists.

## Bottom line

The sliding-energy certificate of FD-303 contains more spectral location information than the unrestricted fourth moment of FD-305. After trimming only `N` endpoint starts, exact convolution and Parseval force

\[
\|\alpha_*\|
\le
N^{-1/4-(3c/2)\lambda+o(1)},
\qquad
|F_X(\alpha_*)|
\ge
X^{1/2}N^{(9c/4)\lambda-5/8-o(1)}.
\tag{61}
\]

Above the shell-dependent threshold `37/(90c-12rho)`, the current Vinogradov minor-arc theorem therefore puts this spike specifically on the principal `q=1` major arc. RH then bounds that arc by `X^(9/10+o(1))`, excluding the near-capacity premise once

\[
\lambda>
\frac{41}{90c-16\rho}.
\tag{62}
\]

Uniformly over every allowable shell, this closes the route for `lambda>1.9200711889...`; before that ceiling, surviving shells are forced toward `Q=x^(1-o(1))`. The denominator freedom left by FD-306 is therefore not generic: the Farey-origin sliding structure selects the principal phase and, at sufficient depth, makes the required capacity impossible under RH.