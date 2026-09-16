# RE-160 — growing terminal moment matching has a factorial resolution threshold

**Status:** `EXACT-DERIVED + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + GROWING-MOMENT-ORDER + UNIFORM-ANALYTIC-REMAINDER + SUBSET-SUM-LOWER-CONTROL + GROWING-ORDER-WIDTH-BRACKET + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-157, RE-158, RE-159.

`RE-159` proves, for every **fixed** integer `r`, that matching terminal logarithmic-position moments through degree `r-1` moves the first free Robin mode to order `r`, with fixed-order root scale

\[
\epsilon_r(p)=\epsilon_{\mathrm{PNT}}(p)^{1/r},
\qquad
\epsilon_{\mathrm{PNT}}(p)
=
\frac{\log U_A(p)}{\sqrt p\log p}.
\]

Its final boundary is essential: all constants were allowed to depend on `r`. When the number of matched moments grows with `p`, the root law is not uniform. The exact exponential series behind the terminal influence supplies a factorial gain on the universal upper side, while an exact subset-sum parity construction gives a lower obstruction on the same `r epsilon_PNT^(1/r)` width scale up to universal multiplicative constants. The growing-order crossover is therefore bracketed at

\[
\boxed{
L_\epsilon
\asymp
r\,\epsilon_{\mathrm{PNT}}(p)^{1/r}
}
\tag{1}
\]

in this scale sense, rather than at `epsilon_PNT^(1/r)` with an `r`-independent constant. Here

\[
L_\epsilon:=-\log(1-\epsilon)
\sim\epsilon
\qquad(\epsilon\to0).
\]

More precisely, put

\[
U:=U_A(p),
\qquad
\eta_p:=\epsilon_{\mathrm{PNT}}(p)
=
\frac{\log U}{\sqrt p\log p},
\qquad
\lambda_p:=\log\frac1{\eta_p}.
\tag{2}
\]

Let `r=r(p)->infinity`, with `r=o(log U)`, and let two terminal insertion packets `P_1,P_2` each contain `m` distinct non-prime real labels

\[
q=Ue^{-z},
\qquad
0\le z\le L:=L_\epsilon=o(1),
\]

with exact moment matching

\[
\sum_{z\in P_1}z^k
=
\sum_{z\in P_2}z^k
\qquad(1\le k\le r-1).
\tag{3}
\]

Define

\[
\rho:=\frac{2^{r-1}e^L}{U}.
\tag{4}
\]

Then, whenever `rho<1`, the exact Robin source coordinate from `RE-153` satisfies the uniform upper bound

\[
\boxed{
|\Delta\mathcal A_p|
\le
\frac{2e^L}{Z_p(1-\rho)}
\frac{m\sqrt p\log p}{U}
\frac{L^r}{r!},
}
\tag{5}
\]

where `Z_p=2+o(1)`. If

\[
m=\delta_p\frac{U}{\log U},
\qquad
\delta_p\to0,
\tag{6}
\]

this becomes

\[
\boxed{
|\Delta\mathcal A_p|
\ll
\delta_p
\frac{L^r}{r!\eta_p}.
}
\tag{7}
\]

Thus the natural growing-order stability scale is

\[
\boxed{
\tau_r(p):=
\bigl(r!\eta_p\bigr)^{1/r}.
}
\tag{8}
\]

Every vanishing-budget family satisfying (3) is `o(1)`-stable whenever `L<=tau_r`; more generally, (7) is decisive exactly when

\[
\delta_p\left(\frac{L}{\tau_r}\right)^r\longrightarrow0.
\tag{9}
\]

For `r->infinity`, Stirling gives

\[
\boxed{
\tau_r(p)
=
\left(1+o(1)\right)
\frac r e\,\eta_p^{1/r}.
}
\tag{10}
\]

The factor `r` is genuine. There is an explicit family of equal-cardinality packets satisfying (3) for which

\[
\boxed{
|\Delta\mathcal A_p|
\ge
(1-o(1))
\frac{m\sqrt p\log p}{U}
\left(\frac{L}{32r}\right)^r.
}
\tag{11}
\]

Consequently, if

\[
\boxed{
\left(
\frac{32r(p)\eta_p^{1/r(p)}}{L_p}
\right)^{r(p)}
\longrightarrow0,
}
\tag{12}
\]

one can choose a budget `delta_p->0` and matched generalized sources with order-one separated Robin coordinates. In particular, any fixed width ratio

\[
L_p\ge C r(p)\eta_p^{1/r(p)}
\qquad(C>32)
\tag{13}
\]

satisfies (12) once `r->infinity`. Equations (7)--(13) place the growing-order transition within universal multiplicative constants in terminal width.

The fixed-order statement of `RE-159` is recovered because `r` and `r!` are then constants. The new content is that the hidden dependence becomes decisive as soon as `r` grows.

## 1. The exact terminal influence admits a uniform moment remainder

Retain the exact one-label influence from `RE-158`--`RE-159`,

\[
\Lambda_p(Ue^{-z})
=
\frac{\sqrt p\log p}{Z_p}
\left[
a(Ue^{-z})-a(U)
+
\frac{a(U)}{\log U}z
\right],
\tag{14}
\]

where

\[
a(t):=-\log(1-t^{-1}).
\]

It is convenient to scale out the explicit `1/U` size and write

\[
G_U(z)
:=
U\left[
a(Ue^{-z})-a(U)
+
\frac{a(U)}{\log U}z
\right],
\tag{15}
\]

so that

\[
\Lambda_p(Ue^{-z})
=
\frac{\sqrt p\log p}{Z_pU}G_U(z).
\tag{16}
\]

The absolutely convergent series used in `RE-159` is exact:

\[
G_U(z)
=
U\sum_{n\ge1}
\frac{e^{nz}-1}{nU^n}
+
\frac{Ua(U)}{\log U}z.
\tag{17}
\]

Let

\[
\Xi
:=
\sum_{z\in P_1}\delta_z
-
\sum_{y\in P_2}\delta_y.
\]

Equal cardinality gives `int 1 dXi=0`, and (3) gives

\[
\int z^k\,d\Xi(z)=0
\qquad(1\le k\le r-1).
\tag{18}
\]

Since `r>=2`, the explicit linear correction in (17) also vanishes after integration. Therefore

\[
\int G_U\,d\Xi
=
U\sum_{n\ge1}
\frac1{nU^n}
\int e^{nz}\,d\Xi(z).
\tag{19}
\]

For `0<=z<=L`, subtract the Taylor polynomial of `e^{nz}` of degree `r-1`. Equation (18) removes it exactly, while the elementary exponential remainder gives

\[
\left|
\int e^{nz}\,d\Xi(z)
\right|
\le
2m\,e^{nL}\frac{(nL)^r}{r!}.
\tag{20}
\]

Hence

\[
\left|
\int G_U\,d\Xi
\right|
\le
\frac{2mL^r}{r!}
U\sum_{n\ge1}
\frac{n^{r-1}e^{nL}}{U^n}.
\tag{21}
\]

For every integer `n>=1`, `n<=2^(n-1)`. Thus

\[
n^{r-1}
\le
2^{(n-1)(r-1)},
\]

and the remaining sum is bounded geometrically:

\[
U\sum_{n\ge1}
\frac{n^{r-1}e^{nL}}{U^n}
\le
\frac{e^L}{1-\rho},
\qquad
\rho=rac{2^{r-1}e^L}{U}.
\tag{22}
\]

Combining (16), (21), and (22) proves (5). In the regime relevant below, `r` is only of order `log p/log log p`, whereas

\[
\log U
=A(\log p)^{5/3}(\log\log p)^{1/3},
\]

so `rho=o(1)` by an enormous margin. The technical condition `r=o(log U)` therefore does not constrain the moment-order transition found here.

## 2. A subset-sum parity packet gives the growing-order lower obstruction

The fixed-order Prouhet--Thue--Morse packet in `RE-159` was deliberately used only with `r` fixed. For growing `r`, its particular dyadic spacing wastes too much terminal width. A more symmetric subset-sum version of the same generating-function idea keeps the exact cancellation while controlling the `r`-dependence.

Choose positive real increments

\[
\frac{L}{16r}
\le a_j\le
\frac{L}{8r}
\qquad(1\le j\le r)
\tag{23}
\]

that are rationally independent over the integers. Then all subset sums are distinct and

\[
\sum_{j=1}^r a_j\le\frac L8.
\]

For a generic translation `tau` in `(L/4,L/3)`, define one signed block by the `2^r` positions

\[
z_S
:=
\tau+
\sum_{j\in S}a_j,
\qquad
S\subseteq\{1,\ldots,r\},
\tag{24}
\]

placing even-cardinality subsets in one packet and odd-cardinality subsets in the other. Each side contains `2^(r-1)` distinct positions, all strictly inside `(0,L)`.

The exponential generating function factorizes exactly:

\[
\boxed{
\sum_S(-1)^{|S|}e^{tz_S}
=
e^{t\tau}
\prod_{j=1}^r(1-e^{ta_j}).
}
\tag{25}
\]

The right-hand side has a zero of exact order `r` at `t=0`. Differentiating there proves

\[
\sum_S(-1)^{|S|}z_S^k=0
\qquad(0\le k<r),
\tag{26}
\]

so the two positive packets have equal cardinality and match every placement moment required in (3).

More importantly, the same identity can be inserted directly into the **exact** series (19); no growing-order Taylor lower estimate is needed. The contribution of one block is

\[
U\sum_{n\ge1}
\frac{e^{n\tau}}{nU^n}
\prod_{j=1}^r(1-e^{na_j}).
\tag{27}
\]

Every summand in (27) has the same sign `(-1)^r`. Therefore its magnitude is at least the `n=1` term:

\[
\left|
\int G_U\,d\Xi_{\rm block}
\right|
\ge
 e^\tau
\prod_{j=1}^r(e^{a_j}-1)
\ge
\prod_{j=1}^r a_j
\ge
\left(\frac{L}{16r}\right)^r.
\tag{28}
\]

Repeat the block `N` times using generic distinct translations in the same interval. Translation preserves (26); the translations can be chosen to keep every resulting position distinct and to avoid the countable set of positions corresponding to ordinary primes. If each positive packet has

\[
m=N2^{r-1}
\tag{29}
\]

labels, equations (28)--(29) give

\[
\left|
\int G_U\,d\Xi
\right|
\ge
2m
\left(\frac{L}{32r}\right)^r.
\tag{30}
\]

Using (16) and `Z_p=2+o(1)` proves (11).

If `m` is chosen at the PNT-small scale (6), then (11) reads

\[
|\Delta\mathcal A_p|
\ge
(1-o(1))
\frac{\delta_p}{\eta_p}
\left(\frac{L}{32r}\right)^r.
\tag{31}
\]

Under (12), choose `delta_p` proportional to

\[
\eta_p
\left(\frac{32r}{L}\right)^r
=
\left(
\frac{32r\eta_p^{1/r}}{L}
\right)^r.
\tag{32}
\]

After adjusting the constant, (31) gives any prescribed fixed nonzero separation while (12) makes `delta_p->0`. Rounding `m` to a multiple of `2^(r-1)` is negligible: because `L=o(1)`, the budget in (32) is still much larger than the one-block density `2^r log U/U` throughout the transition regime, while `U` grows super-polynomially in `p`.

As in `RE-157`--`RE-159`, each control is coarse-PNT-small:

\[
|\pi_Q(x)-\pi(x)|\le m=o(U/\log U),
\]

and

\[
|\vartheta_Q(x)-\vartheta(x)|
\le(1+o(1))m\log U=o(U).
\tag{33}
\]

For `r>=2`, the matched first placement moment also makes the two terminal controls agree exactly in total inserted logarithmic/Chebyshev mass after the layer is passed.

## 3. The fixed-order root hierarchy acquires an `r` factor

The universal stability scale (8) and the lower construction (12) are the same order in `r`. Write

\[
\epsilon_r:=\eta_p^{1/r}.
\]

Stirling gives

\[
(r!)^{1/r}
=
(1+o(1))\frac r e,
\]

so

\[
\tau_r
=(1+o(1))\frac r e\epsilon_r.
\tag{34}
\]

The explicit lower packets retain order-one ambiguity whenever (12) holds; for example every fixed `C>32` in (13) suffices. Thus the stable and ambiguous sufficient regimes are separated only by universal constants on the width scale

\[
\boxed{
L_{\rm grow}(p,r)
=\Theta\!\left(
r\eta_p^{1/r}
\right).
}
\tag{35}
\]

There is no contradiction with `RE-159`: for fixed `r`, the factor `r` is merely part of the constant hidden in `asymp_r`. What changes is that the constant is no longer harmless when `r=r(p)`.

This also shows why naively substituting a growing `r` into

\[
\epsilon_r=\eta_p^{1/r}
\]

would overstate the resolving power of moment matching by a factor of order `r`. The factorial in the analytic remainder supplies the compensating growing-order scale on the upper side; the entropy of the `2^r` equal-weight subset partition supplies the same `r` order on the lower side.

## 4. A moment-count phase transition occurs near `log p / log log p`

The width scale in (35) can itself stop shrinking. Since

\[
r\eta_p^{1/r}
=
\exp\!\left(
\log r-\frac{\lambda_p}{r}
\right),
\tag{36}
\]

the boundary is set by

\[
 r\log r\asymp\lambda_p.
\tag{37}
\]

This yields a qualitative phase transition.

If for some fixed `kappa>0`,

\[
r\log r
\le
(1-\kappa)\lambda_p,
\tag{38}
\]

then

\[
r\eta_p^{1/r}\longrightarrow0.
\tag{39}
\]

Hence shrinking layers satisfying (12) exist. For example, after multiplying `r eta_p^(1/r)` by any sufficiently slowly diverging factor that still leaves the product `o(1)`, the generalized-source ambiguity survives with a vanishing PNT budget.

Conversely, if

\[
r\log r
\ge
(1+\kappa)\lambda_p,
\tag{40}
\]

then Stirling gives

\[
\log\tau_r
=
\log r-1-rac{\lambda_p}{r}+o(1)
\longrightarrow+\infty.
\tag{41}
\]

Every shrinking terminal layer eventually has `L<tau_r`, so (7) forces

\[
\boxed{
\Delta\mathcal A_p=o(1)
}
\tag{42}
\]

for **every** vanishing-budget insertion family matching moments through order `r-1`.

Let `r_c` denote the solution of the simpler asymptotic balance

\[
r_c\log r_c=\lambda_p.
\]

Then

\[
\boxed{
r_c
=
\frac{\lambda_p}{W(\lambda_p)}
}
\tag{43}
\]

and the factorial stability balance `log(r!)=lambda_p` has the same value up to a relative `1+o(1)` factor. Thus (43) locates the transition asymptotically.

For the horizon used throughout this branch,

\[
\eta_p
=
A p^{-1/2}
(\log p)^{2/3}
(\log\log p)^{1/3},
\tag{44}
\]

so

\[
\lambda_p
=
\frac12\log p
-
\frac23\log\log p
-
\frac13\log\log\log p
-
\log A,
\tag{45}
\]

and therefore

\[
\boxed{
r_c
\sim
\frac{\tfrac12\log p}{\log\log p}.
}
\tag{46}
\]

This order is far below `log U`, so the uniformity condition behind (22) is automatically satisfied at the transition.

## 5. What the phase transition does and does not say

Equation (46) is an information threshold inside the same generalized-source control class used by `RE-157`--`RE-159`. It says that a terminal theorem supplying only finitely many moments is qualitatively different from one supplying a growing hierarchy. Roughly `log p/log log p` exact matched placement moments are enough to defeat **this entire PNT-small insertion-placement ambiguity on every shrinking terminal layer**. Below that moment count by a fixed multiplicative margin, there remain shrinking layers on which order-one ambiguity can be manufactured.

This does **not** prove that ordinary primes or a colossally abundant selector actually provide those moments. It does not construct prime packets, modify the primes, or give a Robin counterexample. The controls insert distinct non-prime real labels and are used only to test information content. A positive ordinary-prime theorem can still win much earlier through short-interval rigidity, a source-specific identity, coupling between moments, or another arithmetic constraint absent from these synthetic controls.

The result also requires exact lower-moment matching. Quantitative moment errors would introduce their own lower-order leakage terms and must be compared with the factorial remainder separately. Nor is (5) claimed when `r` approaches `log U`; the geometric majorant was chosen for the substantially smaller regime relevant to (46).

The open selector-height clue therefore remains open. `RE-160` sharpens what one possible positive bridge would have to deliver, but supplies no new CA-to-prime arithmetic coupling and does not justify a clue-state transition.

## 6. Prior-art boundary

The constituent ideas are classical. Equal-power partitions belong to Prouhet--Tarry--Escott theory, already bounded in `RE-159` by Wright's historical reference. The identity (25) is the elementary Boolean-subset version of the same finite-difference generating-function mechanism and is proved here directly.

The broader principle that matching moments controls expectations through polynomial approximation is also standard in the truncated Hausdorff moment problem and in modern statistical uses of local moment matching. A nearby modern reference located in the novelty audit is Yanjun Han, Jiantao Jiao, and Tsachy Weissman, *Local moment matching: A unified methodology for symmetric functional estimation and distribution estimation under Wasserstein distance*, COLT 2018, PMLR **75**, 3189--3221, arXiv:1802.08405. Their setting and targets are unrelated to Robin/CA arithmetic; it is prior-art context for the generic moment-matching/approximation principle, not a dependency of (5) or (11).

A targeted search across truncated moment problems, polynomial approximation under moment matching, Prouhet--Tarry--Escott constructions, and local moment matching found the generic mechanisms but not the Robin terminal influence, its `eta_p` normalization, the growing-order scale `r eta_p^(1/r)`, or the moment-count phase (37)--(46). The line-specific mathematical delta is the exact splice of the terminal Robin influence with a uniform growing-order analytic remainder and a matching subset-sum generalized-source obstruction.

No external theorem is load-bearing. The upper bound follows from the exact series (17), the elementary Taylor remainder, and `n<=2^(n-1)`; the lower bound follows from the explicitly proved product identity (25). Therefore no `SOURCES.md` update is required for correctness.

## Research consequence

`RE-159` ended with a fixed-order warning. `RE-160` resolves that warning quantitatively:

\[
\boxed{
\text{match moments }0,\ldots,r-1
\quad\Longrightarrow\quad
\text{growing-order ambiguity width bracket}
\asymp
r\epsilon_{\mathrm{PNT}}^{1/r},
}
\tag{47}
\]

with the exact stable/ambiguous sufficient conditions given by (9) and (12). The corresponding moment-count transition is

\[
\boxed{
r\log r\asymp\log(1/\epsilon_{\mathrm{PNT}}),
\qquad
r_c\sim\frac{\tfrac12\log p}{\log\log p}.
}
\tag{48}
\]

This turns the terminal source frontier into a concrete quantitative question. A future positive CA/ordinary-prime theorem need not recover an entire terminal distribution abstractly; one candidate route is to prove enough controlled terminal moments, with quantitative errors, to cross (48). Whether the arithmetic selector supplies anything close to that information is now the substantive missing bridge.