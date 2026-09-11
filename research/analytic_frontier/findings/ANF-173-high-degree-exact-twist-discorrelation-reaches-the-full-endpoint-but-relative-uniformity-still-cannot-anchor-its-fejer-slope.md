# ANF-173 — high-degree exact-twist discorrelation reaches the full endpoint but relative uniformity still cannot anchor its Fejer slope

**Status:** `LITERATURE+DERIVED + FULL-ENDPOINT-EXACT-TWIST + ADAPTIVE-CHARGE-OBSTRUCTION + FIXED-ORDER-GOWERS-INSUFFICIENCY + SOURCE-AMPLITUDE-GATE`. `ANF-165` used a degree-six Taylor model of the distinguished logarithmic carrier and therefore stopped its exact-twist all-interval estimate at `H<=X^(2/3+o(1))`. That upper cutoff is not a limitation of the Matomäki--Shao--Tao--Teräväinen all-interval theorem. In the bow regime `K=X^(1-2 epsilon+o(1))`, one may choose a larger but still fixed Taylor degree depending only on the fixed `epsilon`; this extends arbitrary fixed-log discorrelation for the actual `r_X=vartheta-Q_X` twist all the way from `X^(5/8+eta)` to the full endpoint length `K`.

This stronger input still does not control the endpoint completion or the Fejer scale-slope defect of `ANF-172`. There is an adaptive carrier-faithful charge construction showing a sharper information barrier: for any relative bounded-test tolerance `rho_X` with

\[
\sqrt{X\log X}/K=o(\rho_X),
\]

one can use real amplitudes of size at most `rho_X` on an initial block of length `asymp sqrt(X log X)/rho_X`, signed along the **exact** logarithmic carrier rays, to store a charge of size `asymp sqrt(X log X)` and then hold it for `Theta(K)` prefix lengths. Every bounded test correlation on every interval is at most `rho_X` times the interval length, and every fixed-order normalized Gowers norm is at most `rho_X`, yet the endpoint completion is `asymp X K log X`. Hence qualitative Gowers uniformity, arbitrary fixed powers of logarithmic nilsequence saving, and even their validity on the entire endpoint range are not the missing theorem. A relative-uniformity-only architecture would need a genuine power-scale tolerance

\[
\rho_X K=o(\sqrt{X\log X}),
\]

or must use additional source information that forbids arbitrarily small signed carrier-ray amplitudes. For the actual source, that missing information is naturally the prime/rough amplitude and placement law already isolated in `ANF-168`--`ANF-172`.

## 1. A higher fixed Taylor degree removes the artificial `X^(2/3)` ceiling

Retain the bow regime and distinguished height window

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16},
\qquad
A X^2\le U\le B X^2,
\tag{1}
\]

with fixed `0<A<B<infinity`. Let `Y in [X,3X]` be the left endpoint of any physical interval occurring at either bow endpoint and let

\[
I=(Y,Y+H],
\qquad
X^{5/8+\eta}\le H\le K,
\tag{2}
\]

for a fixed `eta>0` small enough for the lower all-interval margin. Since `H<=K`,

\[
\frac{H}{Y}
\ll X^{-2\varepsilon+o(1)}.
\tag{3}
\]

Write `n=Y+j`. For any fixed integer `d>=1`,

\[
\log(Y+j)
=
\log Y+
\sum_{m=1}^{d}
\frac{(-1)^{m+1}}{m}\left(\frac jY\right)^m
+
R_{d+1}(j/Y),
\tag{4}
\]

where, uniformly for `0<=j<=H` and all sufficiently large `X`,

\[
|R_{d+1}(j/Y)|
\ll_d
(H/X)^{d+1}.
\tag{5}
\]

Consequently the phase error after multiplication by `U` obeys

\[
|U R_{d+1}(j/Y)|
\ll_{A,B,d}
X^2(H/X)^{d+1}
\le
X^{2-2\varepsilon(d+1)+o(1)}.
\tag{6}
\]

Choose once and for all, for the fixed bow exponent `epsilon`, an integer degree satisfying

\[
\boxed{d+1>\frac1{\varepsilon}.}
\tag{7}
\]

Then there is a fixed `kappa=kappa(epsilon,d)>0` such that the right side of (6) is `O(X^(-kappa))`. Thus on every interval (2),

\[
n^{-iU}
=
e(P_{Y,U,d}(n))
+
O(X^{-\kappa}),
\tag{8}
\]

for a real polynomial `P_{Y,U,d}` of fixed degree at most `d`. The degree may be large when `epsilon` is small, but it is independent of `X`, exactly as required by the all-interval nilsequence theorem.

Theorem 1.1(ii) of Matomäki--Shao--Tao--Teräväinen applies to polynomial phases of every fixed degree on intervals `H>=X^(5/8+eta)` and `H<=X^(1-eta')` for fixed positive margins. Equation (1) gives `K<=X^(1-epsilon)` for all sufficiently large `X` after shrinking the upper margin if needed. As in `ANF-165`, Remark 1.2 permits the same globally fixed Cramer--Granville cutoff `R_X` at every local base point `Y asymp X`, so the approximant is the actual bow model `Q_X` rather than a locally renormalized `Q_Y`.

Combining the theorem with (8), the local total-variation estimate already used in `ANF-163`--`ANF-165`, and the target-negligible prime-power correction from `Lambda` to `vartheta`, gives, for every fixed `A_0>0`,

\[
\boxed{
\left|
\sum_{n\in I}
r_X(n)n^{-iU}
\right|
\ll_{A_0,\varepsilon,\eta,A,B}
H(\log X)^{-A_0}
}
\tag{9}
\]

uniformly for **every**

\[
X^{5/8+\eta}\le H\le K.
\tag{10}
\]

Thus the degree-six upper range in `ANF-164`--`ANF-165` was only an approximation-degree choice. The current all-interval theorem already has enough fixed-degree flexibility to follow the exact logarithmic carrier across the complete polynomial endpoint horizon.

This strengthening does not alter the `epsilon=1/16` lower activation boundary in `ANF-165`: the issue there is still that the cubic onset `R_TV` reaches the theorem's lower exponent `5/8`. What changes is the opposite end of the range. Once the theorem is active, no polynomial gap between `X^(2/3)` and `K` remains in the exact-twist discorrelation statement.

## 2. Full-range relative discorrelation still has the wrong information currency

Equation (9) might suggest revisiting the endpoint completion with all scales now controlled. That does not close the gap. If one simply inserts (9) into

\[
E_\partial
=
\sum_{r<K}|S_r^-|^2+
\sum_{r<K}|S_r^+|^2,
\tag{11}
\]

the range above the activation scale contributes at best

\[
\sum_{r\le K}
\frac{r^2}{(\log X)^{2A_0}}
\asymp
\frac{K^3}{(\log X)^{2A_0}}.
\tag{12}
\]

Relative to the bow target

\[
T_{\rm bow}=XK\log X,
\tag{13}
\]

this is

\[
\frac{K^2}{X(\log X)^{2A_0+1}}
=
X^{1-4\varepsilon+o(1)}
(\log X)^{-2A_0-1},
\tag{14}
\]

which diverges by a fixed power for every fixed `A_0` throughout `epsilon<1/4`. So extending the theorem to `H=K` removes a range artifact but not the endpoint obstruction.

There is a stronger reason that no amount of **fixed-log relative uniformity** can solve this by itself. The endpoint primitive integrates a tiny coherent drift over many sites and then remembers the accumulated charge even after the drift stops. The charging length can adapt to the available relative error, rather than being tied to the first interval length at which a theorem happens to become available.

The next section makes this adaptive obstruction exact while retaining the carrier-ray reality constraint of `ANF-168`.

## 3. Any relative tolerance above `sqrt(X log X)/K` admits a carrier-faithful dangerous drift

Fix a small constant `delta>0` and define the critical absolute charge

\[
a_X:=\sqrt{\delta X\log X}.
\tag{15}
\]

Let `rho_X` be any positive sequence satisfying

\[
\rho_X\to0,
\qquad
\boxed{
\frac{a_X}{K}=o(\rho_X).
}
\tag{16}
\]

Set

\[
L_X
:=
\left\lceil
\frac{\pi a_X}{2\rho_X}
\right\rceil.
\tag{17}
\]

Condition (16) implies

\[
L_X=o(K).
\tag{18}
\]

Use the exact distinguished carrier directions

\[
v_j:=(X+j)^{-iU},
\qquad
1\le j\le L_X.
\tag{19}
\]

Exactly as in `ANF-168`, averaging over an angle `theta` gives some `theta_X` for which

\[
\sum_{j\le L_X}
\left|
\operatorname{Re}(e^{-i\theta_X}v_j)
\right|
\ge
\frac2\pi L_X.
\tag{20}
\]

Choose real signs

\[
\sigma_j
:=
\operatorname{sgn}
\operatorname{Re}(e^{-i\theta_X}v_j)
\in\{-1,1\}
\tag{21}
\]

and define a one-endpoint coefficient vector

\[
b_j
:=
\begin{cases}
\rho_X\sigma_j v_j,&1\le j\le L_X,\\
0,&L_X<j<K.
\end{cases}
\tag{22}
\]

This obeys the exact physical carrier-ray constraint

\[
b_j(X+j)^{iU}
=
\rho_X\sigma_j
\in\mathbb R.
\tag{23}
\]

Its stored charge at the end of the initial block is

\[
E_X
:=
\sum_{j\le L_X}b_j.
\tag{24}
\]

Equations (17), (20), and (21) give

\[
\operatorname{Re}(e^{-i\theta_X}E_X)
\ge
\frac2\pi \rho_X L_X
\ge
a_X,
\tag{25}
\]

and therefore

\[
\boxed{|E_X|\ge a_X.}
\tag{26}
\]

For every prefix `r>=L_X`, the coefficients in (22) vanish after the charging block, so the primitive simply holds the charge:

\[
\sum_{j\le r}b_j=E_X.
\tag{27}
\]

The one-endpoint completion consequently satisfies

\[
E_-(b)
:=
\sum_{r=1}^{K-1}
\left|
\sum_{j\le r}b_j
\right|^2
\ge
(K-L_X)|E_X|^2.
\tag{28}
\]

Using (15), (18), and (26),

\[
\boxed{
E_-(b)
\ge
(\delta-o(1))XK\log X.
}
\tag{29}
\]

The diagonal edge term in the lag ledger is negligible:

\[
\Delta_-(b)
\le
K\sum_{j\le L_X}|b_j|^2
=
K L_X\rho_X^2
\asymp
K a_X\rho_X
=
o(XK\log X),
\tag{30}
\]

because `rho_X=o(a_X)` automatically. Hence the macroscopic completion in (29) is genuinely off-diagonal. By `ANF-169` and the exact identity of `ANF-172`, some dyadic lag block must therefore have a positive Fejer scale-slope defect of the target order:

\[
\boxed{
D_{2H}-D_H
\gg_\delta
\frac{X\log X}{\log K}
}
\tag{31}
\]

for at least one dyadic `H`, up to the harmless absolute constants already tracked there.

Thus the current scale-slope target can fail even though every nonzero coefficient in the charging mechanism has amplitude only `rho_X`.

## 4. The dangerous drift is invisible to every bounded test and every fixed-order Gowers norm at level `rho_X`

The key information-theoretic property of (22) is independent of the detailed carrier phases. Let `I` be any contiguous interval of coefficient indices and let `F` be **any** complex test sequence with

\[
|F(j)|\le1.
\tag{32}
\]

Then

\[
\left|
\sum_{j\in I}b_jF(j)
\right|
\le
\rho_X\,|I\cap[1,L_X]|
\le
\boxed{\rho_X|I|.}
\tag{33}
\]

This is not merely nilsequence discorrelation. It holds for every bounded test, even one chosen adversarially after seeing the coefficients. In particular it automatically implies every fixed-complexity polynomial-phase or nilsequence correlation estimate with relative tolerance `rho_X`, on every interval length, with no activation threshold at all.

The same point gives a fixed-order Gowers statement. Use the normalized short-interval Gowers norm convention of Matomäki--Shao--Tao--Teräväinen. For any fixed `s>=2` and any interval `I`, the pointwise domination

\[
|b_j1_I(j)|
\le
\rho_X1_I(j)
\tag{34}
\]

implies term by term in the defining cube sum that

\[
\boxed{
\|b\|_{U^s(I)}
\le
\rho_X.
}
\tag{35}
\]

No inverse theorem is needed for (35). On the full endpoint interval one even gains support dilution. Since the number of `s`-dimensional additive cubes contained in an interval of length `L` is `asymp_s L^(s+1)`,

\[
\boxed{
\|b\|_{U^s(1,K]}
\ll_s
\rho_X
\left(\frac{L_X}{K}\right)^{(s+1)/2^s}
=
o(\rho_X).
}
\tag{36}
\]

Thus a **macroscopic** endpoint completion and a target-sized Fejer slope defect coexist with arbitrarily strong fixed-order Gowers smallness, provided the norm tolerance remains above the absolute drift scale `a_X/K`.

A particularly transparent specialization is available in the present difficult range. Choose any fixed

\[
0<\gamma<\frac12-2\varepsilon
\tag{37}
\]

and set

\[
\rho_X=X^{-\gamma}.
\tag{38}
\]

Then `rho_X` is smaller than every fixed power of `1/log X`, while

\[
\frac{a_X}{\rho_X}
=
X^{1/2+\gamma}\sqrt{\delta\log X}
=o(K)
\tag{39}
\]

by (37). The construction therefore satisfies simultaneously

\[
\left|
\sum_{j\in I}b_jF(j)
\right|
=
o_A(|I|(\log X)^{-A})
\tag{40}
\]

for **every fixed `A>0`**, every interval `I`, and every bounded test `F`, as well as

\[
\|b\|_{U^s(I)}
=
o_A((\log X)^{-A})
\tag{41}
\]

for every fixed `s` and `A`, yet (29) and (31) remain macroscopic.

This is strictly stronger as an information barrier than the fixed-activation charge in `ANF-166`: the charging block is allowed to lengthen as the relative tolerance improves. It also sharpens the interpretation of the carrier-faithful control in `ANF-168`: exact logarithmic rays plus high-order uniformity still do not anchor the primitive if arbitrarily small real amplitudes are permitted.

## 5. The correct relative-uniformity threshold is set by the full endpoint horizon

The adaptive construction identifies the natural rate barrier for any argument whose source input is exhausted by relative bounded-test or fixed-order Gowers uniformity. To prevent a charge `a_X` from being accumulated somewhere before the full endpoint horizon `K`, one must at least cross

\[
\boxed{
\rho_X K=o(a_X)
=
o(\sqrt{X\log X}).
}
\tag{42}

Equivalently,

\[
\boxed{
\rho_X
=
o\left(
\frac{\sqrt{X\log X}}{K}
\right)
=
o\left(
X^{-1/2+2\varepsilon+o(1)}
\sqrt{\log X}
\right).
}
\tag{43}
\]

The distinction from the first-activation scale in `ANF-166` is important. A shorter activation length can improve an argument that converts a **specific** first controlled interval into an absolute anchor, but relative cancellation alone does not force the drift to stop there. If the allowed coefficient bias is `rho_X`, it can simply continue for `asymp a_X/rho_X` sites. Therefore lowering the activation scale without either an absolute primitive bound or additional coefficient structure does not by itself remove the charge-and-hold escape.

The full-endpoint exact-twist strengthening (9) makes this boundary especially clean. We no longer need to wonder whether the dangerous charge hides in a range where the logarithmic carrier has not been approximated by a polynomial. Relative all-interval discorrelation can be available throughout the entire endpoint and still tolerate the synthetic drift.

For the actual arithmetic source this is not a counterexample. The real amplitudes

\[
r_X(n)=\vartheta(n)-Q_X(n)
\tag{44}
\]

do **not** have a freely tunable alphabet of tiny values `+-rho_X`. Their nonzero values are fixed by prime locations and by the positive rough-number model `Q_X`; the synthetic construction (22) uses exactly the freedom that the real source does not have. This is why the result redirects rather than blocks the program. The next theorem has to use a consequence of that amplitude/placement law: the dyadic prime-minus-Ramanujan correlation of `ANF-169`, the coupled Fejer scale increment of `ANF-172`, or another source-faithful statistic that cannot be reproduced by an arbitrarily weak carrier-aligned drift.

## 6. Prior-art boundary and consequence for the frontier

The external input in Section 1 is the same paper already registered in `SOURCES.md`: Kaisa Matomäki, Xuancheng Shao, Terence Tao and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, Forum of Mathematics, Pi 11 (2023), e29, DOI `10.1017/fmp.2023.28`. Its Theorem 1.1 supplies nilsequence discorrelation for `Lambda-Lambda^sharp` on all intervals above exponent `5/8`, with arbitrary fixed logarithmic saving and with arbitrary fixed nilsequence degree/complexity. The only new use here is to let that fixed degree depend on the already-fixed bow parameter `epsilon`, which permits the higher-order Taylor model (7) and removes the degree-six `X^(2/3)` ceiling. Remark 1.2 supplies the same fixed Cramer-gauge flexibility already used in `ANF-165`.

The paper's Gowers-uniformity consequences, and the stronger almost-all short-interval results in the 2026 sequel, are natural prior-art neighbors for Section 4. They are not load-bearing for the negative statement: inequalities (33)--(36) are elementary consequences of the pointwise amplitude `|b_j|<=rho_X`. No claim is made that the published Gowers theorems should control endpoint completion; the finding proves precisely why their usual **relative-uniformity currency** is insufficient without an additional arithmetic input.

The live source-side conclusion is therefore sharper than after `ANF-172`:

\[
\boxed{
\text{more polynomial degree or more fixed-order uniformity is not the gate;}\quad
\text{the gate is source-faithful exclusion of tiny persistent drift.}
\tag{45}
\]

The exact-twist all-interval theorem already reaches the whole bow endpoint after a finite degree audit. Any next use of higher uniformity should be judged by whether it exploits the discrete prime/rough amplitude law to beat the absolute threshold (43), or directly controls the phase-sensitive dyadic shell / Fejer slope. Merely proving another `o(1)` Gowers norm or another arbitrary-fixed-log bounded-test estimate, even uniformly over every endpoint scale, does not address the surviving obstruction.
