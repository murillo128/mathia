# FD-292 — Higher log-derivative moments reduce the good-gap target to arbitrary inverse-polylog density

- **Date:** 2026-09-23
- **Status:** proved fixed high-moment finite-window phase sparsity and an arbitrary inverse-polylog good-gap sufficiency criterion
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** right-Perron-collar / logarithmic-derivative high moments / Montgomery--Vaughan mean value / admissible-height intersection / zero-gap occupation / route sharpening
- **Depends on:** FD-287, FD-289, FD-291
- **Classification:** `DERIVED + FIXED-HIGH-MOMENT-FINITE-WINDOW + RAPID-POLYLOG-PHASE-SPARSITY + GOOD-GAP-THRESHOLD-SHARPENING`

## Claim

FD-289 bounds the phase-bad part of every polynomial Perron-height window by `O(H/L^2)`, and FD-291 therefore asks the reciprocal-log-safe cores of remainder-good zero gaps to occupy slightly more than that amount. The exponent `2` is not intrinsic. Applying the same Montgomery--Vaughan mean-value theorem to fixed powers of the strict-right logarithmic derivative gives **every fixed even moment**, and hence makes the phase-bad set smaller than any prescribed fixed inverse power of `L`.

Put

\[
L:=\log(2Nx),\qquad b:=L^{-2},\qquad a:=\eta/L,
\tag{1}
\]

with fixed `eta in (0,1)`, and

\[
F_u(t):=-\frac{\zeta'}{\zeta}(1+u+it),
\qquad
M_{\eta,L}^{\rm str}(t)
:=\sup_{b\le u\le a}|\operatorname{Im}F_u(t)|.
\tag{2}
\]

Let `J=[H,H+R]`. For every fixed integer `m>=1` there is a finite constant

\[
C_m:=\sum_{n\ge2}\frac{A_m(n)^2}{n^2},
\qquad
A_m:=\underbrace{\Lambda*\cdots*\Lambda}_{m\ {m times}},
\tag{3}
\]

such that

\[
\boxed{
\left(
\frac1R\int_J
\bigl(M_{\eta,L}^{\rm str}(t)\bigr)^{2m}dt
\right)^{1/(2m)}
\le
C_m^{1/(2m)}
+
O_{m,\eta}\!\left(
\frac1L+
\frac{L^{m+2}}{R^{1/(2m)}}
\right).
}
\tag{4}
\]

Consequently, if

\[
\frac{R}{L^{2m(m+2)}}\longrightarrow\infty,
\tag{5}
\]

then for every fixed `A>0`, uniformly in the starting height `H`,

\[
\boxed{
\frac1R\operatorname{meas}
\{t\in J:M_{\eta,L}^{\rm str}(t)\ge AL\}
\le
\frac{C_m+o_{m,\eta}(1)}{A^{2m}L^{2m}}.
}
\tag{6}
\]

For `m=1`, (4)--(6) recover the `L^6` window condition and `O(L^{-2})` exceptional proportion of FD-289. For every fixed `m`, every polynomial window `R=x^{\tau+o(1)}` with `tau>0` satisfies (5), so the exceptional proportion is `O_m(L^{-2m})`.

Use the FD-287 optimizer

\[
\eta_*:=e^{1-\pi/2},\qquad
f_*:=e^{\pi/2-1},
\tag{7}
\]

fix `kappa in (0,f_*)`, and set `A_kappa=f_*-kappa`. The same boundary-slice and outer-collar bookkeeping as FD-289 shows that the phase-bad set in a polynomial dyadic window `J=[H,2H]` satisfies, for every fixed `m`,

\[
\boxed{
\operatorname{meas}\mathcal P_{\kappa,L}(J)
\le
\left(
\frac{C_m}{A_\kappa^{2m}}+o_{m,\kappa}(1)
\right)
\frac{H}{L^{2m}}.
}
\tag{8}
\]

Equivalently, for every fixed real `P>0`,

\[
\boxed{
\operatorname{meas}\mathcal P_{\kappa,L}(J)
=O_{P,\kappa}\!\left(\frac{H}{L^P}\right).
}
\tag{9}
\]

The implied constant may depend very strongly on `P`; no uniformity in growing moment order is claimed.

Now let `Omega_B(J)` be the FD-291 reciprocal-log-safe occupation of zero gaps on which the complete physical hard remainder is below the desired budget `B_{N,x}`. Equation (9) sharpens the FD-291 intersection criterion to the following form:

> For **any fixed `P>0`**, if there is a fixed `delta_P>0` such that
> \[
> \Omega_B(J)\ge \delta_P\frac{H}{L^P}
> \tag{10}
> \]
> for all sufficiently large members of the family, then one can choose a fixed integer `m>P/2`; the phase-bad measure is then `o(H/L^P)`, so the safe remainder-good set contains a height that is simultaneously phase-good, zero-safe, and remainder-good.

Thus the quadratic-log occupation target of FD-291 can be replaced by **any prescribed fixed inverse-polylogarithmic occupation scale**. The phase-selection mechanism no longer singles out `L^{-2}` as a frontier exponent.

## 1. Fixed even moments are still Montgomery--Vaughan mean squares

For `u>0`, absolute convergence gives

\[
F_u(t)=\sum_{n\ge2}\frac{\Lambda(n)}{n^{1+u}}e^{-it\log n}.
\tag{11}
\]

Raise this identity to the fixed integer power `m`. Dirichlet convolution gives exactly

\[
F_u(t)^m
=
\sum_{n\ge2}
\frac{A_m(n)}{n^{1+u}}e^{-it\log n},
\qquad
A_m=\Lambda^{*m}.
\tag{12}
\]

Hence

\[
|F_u(t)|^{2m}=|F_u(t)^m|^2,
\tag{13}
\]

so the `2m`-th moment is only a mean square of another Dirichlet series. Applying the same translated Montgomery--Vaughan theorem used in FD-289 yields

\[
\frac1R\int_J|F_u(t)|^{2m}dt
\le
C_m+
\frac{O_m(1)}R
\sum_{n\ge2}\frac{A_m(n)^2}{n^{1+2u}}.
\tag{14}
\]

The same device applies to the `u`-derivative. Put

\[
G_u(t):=\partial_uF_u(t)
=-\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+u}}e^{-it\log n}
\tag{15}
\]

and let

\[
B_m:=\underbrace{(\Lambda\log)*\cdots*(\Lambda\log)}_{m\ {m times}}.
\tag{16}
\]

Then `G_u^m` has Dirichlet coefficients `B_m(n)n^{-1-u}`, so

\[
\frac1R\int_J|G_u(t)|^{2m}dt
\le
D_m+
\frac{O_m(1)}R
\sum_{n\ge2}\frac{B_m(n)^2}{n^{1+2u}},
\tag{17}
\]

where

\[
D_m:=\sum_{n\ge2}\frac{B_m(n)^2}{n^2}<\infty.
\tag{18}
\]

No higher-moment theorem beyond the same Montgomery--Vaughan mean square is required.

## 2. The coefficient energies have only polynomial cost as `u -> 0+`

Let `d_m(n)` denote the ordered `m`-fold divisor function. Since every factor in a term of `A_m(n)` divides `n`,

\[
0\le A_m(n)\le d_m(n)(\log n)^m,
\tag{19}
\]

and similarly

\[
|B_m(n)|\le d_m(n)(\log n)^{2m}.
\tag{20}
\]

For fixed `m`, the Euler product

\[
D_m^{\rm div}(s):=\sum_{n\ge1}\frac{d_m(n)^2}{n^s}
\tag{21}
\]

satisfies

\[
D_m^{\rm div}(1+v)\ll_m v^{-m^2}
\qquad(0<v\le1).
\tag{22}
\]

A direct proof is enough here. At a prime,

\[
\sum_{r\ge0}d_m(p^r)^2z^r
=1+m^2z+O_m(z^2)
\qquad(|z|\le1/2),
\tag{23}
\]

so taking logarithms of the Euler product gives

\[
\log D_m^{\rm div}(s)
\le
m^2\sum_p p^{-s}+O_m(1)
\le
m^2\log\zeta(s)+O_m(1),
\tag{24}
\]

which implies (22).

Using

\[
(\log n)^r\ll_r u^{-r}n^u
\tag{25}
\]

in (19)--(22) gives the deliberately crude but sufficient estimates

\[
\sum_{n\ge2}\frac{A_m(n)^2}{n^{1+2u}}
\ll_m u^{-(m^2+2m)},
\tag{26}
\]

and

\[
\sum_{n\ge2}\frac{B_m(n)^2}{n^{1+2u}}
\ll_m u^{-(m^2+4m)}.
\tag{27}
\]

At exponent `2`, the same Euler-product argument immediately makes `C_m` and `D_m` finite. Substituting (26)--(27) into (14) and (17) yields

\[
\|F_u\|_{2m,J}
\le
C_m^{1/(2m)}
+O_m\!\left(
R^{-1/(2m)}u^{-(m/2+1)}
\right),
\tag{28}
\]

\[
\|G_u\|_{2m,J}
\le
D_m^{1/(2m)}
+O_m\!\left(
R^{-1/(2m)}u^{-(m/2+2)}
\right),
\tag{29}
\]

where the norms are normalized by `R^{-1}` over `J`.

## 3. The maximal strict-right strip is rapidly polylog-sparse

For every `u in [b,a]`, the fundamental theorem of calculus gives

\[
|F_u(t)|
\le
|F_a(t)|+
\int_b^a|G_v(t)|\,dv.
\tag{30}
\]

Since `M_{eta,L}^{str}(t)<=sup_{b<=u<=a}|F_u(t)|`, Minkowski in `L^{2m}(J)` and (28)--(29) imply

\[
\|M_{\eta,L}^{\rm str}\|_{2m,J}
\le
C_m^{1/(2m)}
+O_{m,\eta}\!\left(
\frac1L
+
R^{-1/(2m)}
\int_b^a v^{-(m/2+2)}dv
\right).
\tag{31}
\]

Because `b=L^{-2}`,

\[
\int_b^a v^{-(m/2+2)}dv
\ll_m b^{-(m/2+1)}
=L^{m+2}.
\tag{32}
\]

This proves (4). Condition (5) makes the last term `o(1)`, so

\[
\frac1R\int_J
\bigl(M_{\eta,L}^{\rm str}(t)\bigr)^{2m}dt
\le
C_m+o_{m,\eta}(1).
\tag{33}
\]

Markov's inequality at height `AL` is exactly (6).

The consistency check `m=1` is useful: (26) becomes the `u^{-3}` coefficient error of FD-289, (27) becomes its `u^{-5}` derivative error, (32) becomes `L^3`, and (5) becomes `R/L^6 -> infinity`. Thus the present argument is a genuine fixed-moment extension of the existing finite-window proof, not a different phase estimate.

For a polynomial dyadic window `R=H=x^{tau+o(1)}`, every fixed power of `L` is negligible compared with `H`; hence (5) holds for every fixed `m`. Choosing `m` after fixing the desired inverse-log exponent proves (9).

## 4. The remaining occupation theorem can be arbitrarily sparse on a polylog scale

FD-291 defines

\[
\mathcal Q_B(J)
=
\bigcup_{j:\,G_j\ {m remainder\text{-}good}}
G_j^{\rm safe}(J),
\qquad
\operatorname{meas}\mathcal Q_B(J)=\Omega_B(J),
\tag{34}
\]

and every point of `Q_B(J)` is already remainder-good and zero-safe. Therefore the only universal exceptional set still to avoid is the phase-bad set.

Fix any `P>0` and suppose (10) holds. Choose once and for all an integer `m>P/2`. Equation (8) gives

\[
\operatorname{meas}\mathcal P_{\kappa,L}(J)
=O_{m,\kappa}\!\left(\frac{H}{L^{2m}}\right)
=o\!\left(\frac{H}{L^P}\right).
\tag{35}
\]

Hence

\[
\operatorname{meas}
\bigl(\mathcal Q_B(J)\setminus\mathcal P_{\kappa,L}(J)\bigr)
>0
\tag{36}
\]

for all sufficiently large `x`. This produces the desired simultaneous cutoff.

There is an equivalent counting statement. If every selected remainder-good gap has length at least `(2+c)/L`, then each contributes at least `c/L` of safe core. To obtain (10) it is enough to have

\[
K\gg_{P,c}\frac{H}{L^{P-1}}
\tag{37}
\]

such gaps. Since a polynomial window contains `Theta(HL)` zero gaps, this corresponds to only an `L^{-P}` fraction of the total gap population. Because `P` may be any fixed number, the phase condition permits a remainder-good family thinner than **any preassigned fixed inverse power of `log(2Nx)`**, provided that power is fixed before the asymptotic limit.

This does not prove that such remainder-good gaps exist. It removes the phase-exception exponent as a meaningful obstruction to proving their existence.

## 5. Adversarial checks and limitations

The first check is moment-order uniformity. None is available or claimed. The constants `C_m`, `D_m`, the Euler-product constants and the required polylogarithmic window exponent can grow rapidly with `m`. The argument allows `m` to be any **fixed** integer chosen before `x -> infinity`; it does not justify taking `m=m(L)`. Therefore (9) means `O_P(L^{-P})` for every fixed `P`, not an exponential or super-polynomial exceptional estimate with uniform constants.

The second check is the shrinking strip. The high moment is taken at `u>=L^{-2}>0`, where the Dirichlet series is absolutely convergent. The ultra-thin slice `0<=u<=L^{-2}` is not included in (4); it is handled exactly as in FD-288--FD-289 by the already anchored pointwise logarithmic-derivative bound at polynomial height, whose integrated phase cost across width `L^{-2}` is `o(1)`. No passage of the Dirichlet series through `Re(s)=1` is used.

The third check is the contour consequence. The high-moment estimate for the strict-right strip is unconditional. RH remains required only for the inherited prime-sector witness below `T=x^{1/2-epsilon}`. The result also does not control cancellation between the protected right collar and the rest of the complete hard remainder.

The fourth check is the role of gapwise constancy. Equation (10) concerns the FD-291 **safe-core length mass**, not merely a count of good gap labels. Very short gaps contribute no safe core and cannot be promoted by a high-moment phase estimate. The counting corollary (37) therefore assumes the stated reciprocal-log length lower bound.

The fifth check is endpoint discreteness. A prescribed discrete sequence of isolated heights could still lie entirely in the phase-bad set. The FD-291 mechanism does not require such a sequence: it selects continuously inside positive-length safe cores. That is why the measure estimate (8) is the correct interface here.

## Prior-art check

The only load-bearing external theorem is the same Montgomery--Vaughan mean-value theorem already anchored in `SOURCES.md` for FD-289. Passing from the second moment of `F_u` to the `2m`-th moment by applying that mean-square theorem to `F_u^m` is standard Dirichlet-series algebra, and no novelty is claimed for that general high-moment device. A fresh search also finds substantial literature on higher moments of zeta and its logarithmic derivative in harder near-critical regimes; those results are not needed here because the present strip remains strictly in `Re(s)>1`.

The line-specific contribution is the quantitative combination of this fixed high-moment upgrade with the FD-287 phase tariff and the FD-291 gapwise-constant remainder architecture. That combination removes the previously visible `L^{-2}` occupation threshold and replaces it by the arbitrary fixed inverse-polylog criterion (10). No new external theorem is load-bearing, so `SOURCES.md` requires no change.

## Frontier after FD-292

The admissible-height problem is now more sharply separated. Phase-good selection can beat **any fixed inverse-polylogarithmic sparse family** of safe remainder-good gaps in a polynomial window. Therefore a useful next theorem no longer needs to match a distinguished quadratic-log density. It is enough to prove, at the physical repair budget, that safe cores of remainder-good gaps occupy `H/L^P` for **some finite fixed `P`**.

If even that cannot be shown, the obstruction is in the complete hard remainder or in the arithmetic mechanism producing good gaps, not in the near-one phase exceptional set. A proof that loses the Farey consecutive-difference/divisor-replication structure and becomes only a generic estimate for Möbius/Mertens zero-sum remainders should be handed to `mobius_cancellation`; a proof that exploits the physical repair map or the gapwise source geometry remains owned here.