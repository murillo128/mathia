# RE-161 — approximate terminal moment matching requires a factorial precision staircase

**Status:** `EXACT-DERIVED + APPROXIMATE-MOMENT-LEAKAGE-LAW + FACTORIAL-PRECISION-STAIRCASE + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + QUALITATIVE-MOMENT-MATCHING-NONCOERCIVE + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-157, RE-158, RE-159, RE-160.

`RE-160` locates the resolution threshold when terminal placement moments are matched **exactly** through a growing order `r-1`. The exact-match remainder is factorially small,

\[
\frac{L^r}{r!},
\]

and gives the growing-order width scale

\[
L\asymp r\,\eta_p^{1/r},
\qquad
\eta_p:=\epsilon_{\mathrm{PNT}}(p)
=\frac{\log U_A(p)}{\sqrt p\log p}.
\]

The exactness assumption is not a technical convenience. If the lower moments are only approximately matched, every residual moment leaks into the Robin coordinate before the factorial remainder is reached. The leakage admits an exact weighted expansion, and retaining the `r`-th-order gain requires a strongly anisotropic precision staircase. In particular, merely requiring **vanishing relative error in every lower moment, even uniformly over arbitrarily many moments, is noncoercive**: there are PNT-small generalized sources whose normalized moment errors all tend to zero while their Robin coordinates remain separated by order one.

The main quantitative statement is as follows. Put

\[
U:=U_A(p),
\qquad
L=o(1),
\qquad
q=Ue^{-z},\quad 0\le z\le L,
\tag{1}
\]

and let two terminal insertion packets `P_1,P_2` each contain `m` distinct non-prime real labels. Write their logarithmic positions as `z_i,y_i` and define signed moment discrepancies

\[
M_k:=\sum_{i=1}^m z_i^k-\sum_{i=1}^m y_i^k,
\qquad
\mu_k:=\frac{M_k}{m}.
\tag{2}
\]

Equal cardinality gives `M_0=0`. For an integer `r>=2`, set

\[
\rho:=\frac{2^{r-1}e^L}{U}.
\tag{3}
\]

Whenever `rho<1`, the exact Robin source coordinate from `RE-153` satisfies

\[
\boxed{
\Delta\mathcal A_p
=
-\frac{m\sqrt p\log p}{Z_pU}
\left[
\sum_{k=1}^{r-1}b_k(U)\mu_k
+\mathcal R_r
\right],
}
\tag{4}
\]

where `Z_p=2+o(1)`,

\[
b_1(U)
=
\frac{U}{U-1}+\frac{Ua(U)}{\log U}
=1+\frac1{\log U}+O(U^{-1}),
\tag{5}
\]

\[
b_k(U)
=
\frac{U}{k!}
\sum_{n\ge1}\frac{n^{k-1}}{U^n}
\qquad(k\ge2),
\tag{6}
\]

and

\[
\boxed{
|\mathcal R_r|
\le
\frac{2e^L}{1-\rho}\frac{L^r}{r!}.
}
\tag{7}
\]

Thus, if

\[
m=\delta_p\frac{U}{\log U},
\qquad
\delta_p\to0,
\tag{8}
\]

then

\[
\boxed{
|\Delta\mathcal A_p|
\le
\frac{\delta_p}{Z_p\eta_p}
\left[
\sum_{k=1}^{r-1}b_k(U)|\mu_k|
+
\frac{2e^L}{1-\rho}\frac{L^r}{r!}
\right].
}
\tag{9}
\]

In the growing-order regime of `RE-160`, `2^r/U=o(1)`, so uniformly for `2<=k<r`,

\[
b_k(U)=\frac{1+o(1)}{k!},
\tag{10}
\]

while `b_1(U)=1+o(1)`. Consequently the robust lower-moment leakage budget is

\[
\boxed{
\mathfrak E_r
:=
\sum_{k=1}^{r-1}\frac{|\mu_k|}{k!}
}
\tag{11}
\]

up to `1+o(1)` factors. The exact-match `r`-th-order gain survives under separate moment estimates only when

\[
\boxed{
\mathfrak E_r
=O\!\left(\frac{L^r}{r!}\right).
}
\tag{12}
\]

At the factorial stability width

\[
\tau_r:=(r!\eta_p)^{1/r},
\tag{13}
\]

condition (12) becomes the particularly simple staircase

\[
\boxed{
\sum_{k=1}^{r-1}\frac{|\mu_k|}{k!}
=O(\eta_p).
}
\tag{14}
\]

Hence a single uncontrolled `k`-th moment can be tolerated only at average scale

\[
|\mu_k|\lesssim k!\eta_p
\tag{15}
\]

if one wants to retain the `RE-160` factorial resolution without using cancellation between different moment errors. For `k=1`, this says that the average terminal logarithmic/Chebyshev mass mismatch must be controlled on the `eta_p` scale itself.

There is also a sharp qualitative obstruction. Suppose only that

\[
\frac{\eta_p}{L_p}\longrightarrow0.
\tag{16}
\]

Then there exist vanishing-budget insertion packets `P_1,P_2` such that

\[
\boxed{
\sup_{k\ge1}
\frac{|\mu_k|}{L_p^k}
\longrightarrow0,
}
\tag{17}
\]

while

\[
\boxed{
\liminf |\Delta\mathcal A_p|>0.
}
\tag{18}
\]

In particular, (17) holds simultaneously through **every** finite or growing moment order. Therefore no statement of the form “all lower terminal moments are matched to vanishing relative error” can substitute for the quantitative precision law (9)--(14).

## 1. Approximate moments enter before the factorial remainder

Retain the exact terminal influence from `RE-158`--`RE-160`,

\[
\Lambda_p(Ue^{-z})
=
\frac{\sqrt p\log p}{Z_pU}G_U(z),
\tag{19}
\]

with

\[
G_U(z)
:=
U\left[
a(Ue^{-z})-a(U)
+\frac{a(U)}{\log U}z
\right],
\qquad
a(t):=-\log(1-t^{-1}).
\tag{20}
\]

The exact absolutely convergent series is

\[
G_U(z)
=
U\sum_{n\ge1}\frac{e^{nz}-1}{nU^n}
+\frac{Ua(U)}{\log U}z.
\tag{21}
\]

Let

\[
\Xi
:=
\sum_{i=1}^m\delta_{z_i}
-
\sum_{i=1}^m\delta_{y_i}.
\tag{22}
\]

Because both packets have the same cardinality, `int 1 dXi=0`. Expand each exponential in (21) only through degree `r-1`. Unlike `RE-160`, the lower Taylor coefficients do not vanish; they give exactly the discrepancies (2). Therefore

\[
\int G_U\,d\Xi
=
\sum_{k=1}^{r-1}b_k(U)M_k
+R_r,
\tag{23}
\]

where the same exponential-remainder estimate as in `RE-160` gives

\[
|R_r|
\le
\frac{2me^L}{1-\rho}\frac{L^r}{r!}.
\tag{24}
\]

Multiplying by the prefactor in (19) proves (4)--(9). No moment-problem theorem is needed: the leakage law is simply the exact analytic series already underlying `RE-160`, with the previously cancelled coefficients retained.

For `k>=2`, the `n=1` term in (6) is `1/k!`. The remainder is bounded uniformly by the same geometric device used in `RE-160`; under `2^r/U=o(1)` it is `o(1/k!)` uniformly for `k<r`. This proves (10)--(12).

The distinction between **signed coupling** and **separate moment control** is important. Equation (4) contains the signed combination

\[
\sum_{k<r}b_k(U)\mu_k.
\tag{25}
\]

A source-specific arithmetic identity may force cancellation inside (25) and can therefore beat the absolute budget (11). But if the available theorem only bounds the moment errors separately, (11) is the natural robust cost. This is exactly the kind of coupling that the open selector-height clue is asking for; `RE-161` does not rule it out.

## 2. The precision staircase is factorially anisotropic

Suppose, more coarsely, that all lower moments are known with a common relative accuracy `eps_p`,

\[
|\mu_k|
\le
\varepsilon_p L^k
\qquad(1\le k<r).
\tag{26}
\]

Since `L=o(1)`, equations (10)--(11) give

\[
\mathfrak E_r
\le
(1+o(1))\varepsilon_p
\sum_{k=1}^{r-1}\frac{L^k}{k!}
=
(1+o(1))\varepsilon_p L.
\tag{27}
\]

Hence

\[
\boxed{
|\Delta\mathcal A_p|
\ll
\frac{\delta_p}{\eta_p}
\left(
\varepsilon_p L
+\frac{L^r}{r!}
\right).
}
\tag{28}
\]

The lower-moment noise is smaller than the factorial remainder only if

\[
\boxed{
\varepsilon_p
\lesssim
\frac{L^{r-1}}{r!}.
}
\tag{29}
\]

Thus increasing the matched order does not merely require “more moments”; it requires rapidly increasing **precision in the already matched moments**. The first moment is the most expensive one under uniform relative control.

At `L=tau_r`, equations (13) and (29) yield

\[
\varepsilon_p
\lesssim
\frac{\eta_p}{\tau_r}.
\tag{30}
\]

Equivalently, the average first-moment discrepancy must satisfy

\[
|\mu_1|\lesssim\eta_p.
\tag{31}
\]

For equal-cardinality packets the first logarithmic-position moment has an exact arithmetic interpretation:

\[
M_1
=
-\left(
\sum_{q\in P_1}\log q
-
\sum_{q\in P_2}\log q
\right).
\tag{32}
\]

So (31) is precisely a terminal Chebyshev/logarithmic-mass precision requirement, not an abstract moment artifact.

## 3. Vanishing relative errors in every moment are still insufficient

The quantitative nature of (29) is essential. Assume (16), and choose

\[
\delta_p
:=
\sqrt{\frac{\eta_p}{L_p}},
\qquad
 t_p
:=
\frac{\eta_p}{\delta_p}
=
\sqrt{\eta_pL_p}.
\tag{33}
\]

Then

\[
\delta_p\to0,
\qquad
\frac{t_p}{L_p}	o0,
\qquad
\frac{\delta_pt_p}{\eta_p}=1.
\tag{34}
\]

Take

\[
m_p
=
\left\lfloor
\delta_p\frac{U}{\log U}
\right\rfloor.
\tag{35}
\]

Because `U` grows super-polynomially in the branch horizon, `m_p->infinity`. Choose `m_p` distinct real positions

\[
z_i\in[t_p^2,2t_p^2]
\tag{36}
\]

so that neither `Ue^{-z_i}` nor `Ue^{-(z_i+t_p)}` is an ordinary prime, and define

\[
y_i:=z_i+t_p.
\tag{37}
\]

For large `p`, both packets lie inside `[0,L_p]`. The forbidden ordinary-prime positions are countable, so the distinct labels can be chosen generically.

For every integer `k>=1`, since `z_i+t_p<=2t_p` eventually,

\[
|y_i^k-z_i^k|
\le
(2t_p)^k.
\tag{38}
\]

Therefore

\[
\boxed{
\frac{|\mu_k|}{L_p^k}
\le
\left(\frac{2t_p}{L_p}\right)^k.
}
\tag{39}
\]

As `2t_p/L_p->0`, the right-hand side is uniformly maximized at `k=1` for large `p`. Hence

\[
\sup_{k\ge1}
\frac{|\mu_k|}{L_p^k}
\le
\frac{2t_p}{L_p}
\longrightarrow0,
\tag{40}
\]

which proves (17) simultaneously for any chosen growing moment cutoff.

Yet the Robin influence does not become close. Differentiate (20) exactly:

\[
G_U'(z)
=
\frac{U}{Ue^{-z}-1}
+\frac{Ua(U)}{\log U}.
\tag{41}
\]

Both terms are positive and the first is larger than `1` for `z>=0`. Hence

\[
G_U(y_i)-G_U(z_i)
\ge t_p.
\tag{42}
\]

The two packet coordinates therefore satisfy

\[
|\Delta\mathcal A_p|
\ge
\frac{m_p\sqrt p\log p}{Z_pU}t_p
=
(1+o(1))
\frac{\delta_pt_p}{Z_p\eta_p}.
\tag{43}
\]

Using (34) and `Z_p=2+o(1)`,

\[
\boxed{
\liminf |\Delta\mathcal A_p|
\ge\frac12.
}
\tag{44}
\]

The constant is arbitrary up to rescaling `t_p` while keeping `t_p=o(L_p)`. Thus (18) is not a small quantitative defect: order-one Robin ambiguity survives even though **all normalized placement moments are asymptotically indistinguishable in relative layer units**.

Both controls remain coarse-PNT-small. Each adds only

\[
m_p=o(U/\log U)
\tag{45}
\]

labels, so

\[
|\pi_Q(x)-\pi(x)|
\le m_p=o(U/\log U)
\tag{46}
\]

and

\[
|\vartheta_Q(x)-\vartheta(x)|
\le(1+o(1))m_p\log U
=o(U).
\tag{47}
\]

As in `RE-157`--`RE-160`, these are generalized-source information tests, not modifications of the ordinary primes.

## 4. Consequence for the `RE-160` moment-count transition

The exact-matching phase transition

\[
r_c
\sim
\frac{\tfrac12\log p}{\log\log p}
\tag{48}
\]

from `RE-160` remains correct for exact moments. But it has no qualitative approximate analogue. On every terminal width with

\[
L_p\gg\eta_p,
\tag{49}
\]

the translated packets above match **arbitrarily many moments with uniformly vanishing relative errors** and still retain order-one Robin separation.

Thus a positive theorem cannot replace exact matching in `RE-160` by a statement such as

\[
\frac{|M_k|}{mL^k}=o(1)
\quad\text{uniformly for }k<r(p)
\tag{50}
\]

and expect the same resolution. It needs one of two stronger inputs:

1. quantitative errors satisfying the weighted leakage law (9)--(14), or
2. a source-specific signed relation forcing cancellation in the combination (25).

The second possibility is genuinely different and remains compatible with the open CA selector-height program. `RE-161` says only that **independent approximate moment estimates are not enough**.

## 5. Prior-art boundary

Approximate and noisy moment recovery is classical. The novelty audit revisited Han--Jiao--Weissman, *Local moment matching* (COLT 2018), already identified in `RE-160`, and found the more recent Musco--Musco--Rosenblatt--Singh, *Sharper Bounds for Chebyshev Moment Matching, with Applications* (COLT 2025), which studies distribution recovery from noisy Chebyshev moments. The statistical Hausdorff moment literature likewise studies reconstruction from noisy moments.

Those works confirm that approximate moment information has an established stability theory, but their targets and norms are unrelated to the terminal Robin influence. The line-specific content here is the exact leakage expansion (4), the `eta_p` normalization, the factorial precision staircase (12)--(14), and the explicit PNT-small translated-source obstruction (33)--(44). No external theorem is used in the proof: all estimates follow from the exact terminal series already derived in `RE-158`--`RE-160` and the monotonicity (41). Therefore no `SOURCES.md` update is required for correctness.

## Scope

This finding does not show that ordinary primes realize the synthetic translated packets, does not produce a Robin counterexample, and does not close the selector-height clue. It isolates an information barrier for generalized terminal sources. In particular, it does not exclude an arithmetic theorem coupling the moment errors with signs that cancel in (25), nor a short-interval or CA-specific rigidity statement that prevents the translated controls altogether.

The result also distinguishes two notions that should not be conflated. Equation (12) is the precision needed to **retain the `r`-th-order factorial remainder** under separate moment bounds. For a fixed insertion intensity `delta_p`, mere Robin stability only requires the weaker signed condition obtained directly from (4),

\[
\frac{\delta_p}{\eta_p}
\left|
\sum_{k<r}b_k(U)\mu_k
\right|
\longrightarrow0,
\tag{51}
\]

plus the corresponding remainder condition. Any future use of approximate moments should state which of these two objectives is intended.

## Research consequence

`RE-160` showed that exact growing-order moment matching reaches a factorial resolution threshold. `RE-161` identifies the missing robustness condition:

\[
\boxed{
\text{exact }M_1=\cdots=M_{r-1}=0
\quad\leadsto\quad
\text{approximate cost }
\sum_{k<r}\frac{|M_k|}{mk!}
\lesssim\frac{L^r}{r!}.
}
\tag{52}
\]

At `L=tau_r`, the right-hand side is exactly `eta_p`. Qualitative `o(1)` relative accuracy, even in every lower moment simultaneously, is far too weak: the translated generalized sources (33)--(44) retain an order-one Robin gap. Any moment-based CA-to-height bridge therefore needs **quantitative factorial-scale precision or genuine signed cross-moment cancellation**, not just a growing count of approximately matched moments.