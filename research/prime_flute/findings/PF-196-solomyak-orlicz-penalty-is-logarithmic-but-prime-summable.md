# PF-196 — the critical Solomyak Orlicz penalty is logarithmic but prime-summable

**Status:** `LITERATURE+DERIVED + EXACT-ENDPOINT-ACCOUNTING + POSITIVE/ROUTE-BOUNDARY`. PF-195 shows that the one-sided critical weak-`S_2` route cannot be driven by the square root of the PF-191 `L^1` mass through generic Cwikel theory. The accepted weak-trace clue leaves the directly symmetrized Cwikel--Solomyak route as the closest generic endpoint model and previously treated bounded coefficient `L^1` mass as if it were quantitatively interchangeable with `L log L`. That is too optimistic at the level of the actual theorem: Sukochev--Zanin's weak-`S_1` estimate uses the **Luxemburg norm** for `Phi(t)=t log(e+t)`, and concentration on a set of measure `m` costs an unavoidable factor `log(1/m)` relative to `L^1` even when the coefficient is bounded and arbitrarily small in amplitude. For the exact PF-191 Lambert transport this penalty has the sharp scale `d(1+a)/cosh(a)`, rather than `d/cosh(a)`. Crucially, however, the exact prime/shift tail still sums it. In fact every fixed polynomial loss in the Lambert depth `a_n` remains summable against `d_n/cosh(a_n)`. Thus the symmetrized endpoint route is **not mass-linear**, but its first critical Orlicz concentration loss does not destroy the prime-flute endpoint budget. What remains open is the uniform transfer from the scalar compact Cwikel--Solomyak model to the localized hyperbolic vector-gradient form and the no-loss global reassembly.

## Claim

Let

\[
\Phi(t)=t\log(e+t),\qquad t\ge0,
\tag{1}
\]

and equip `L_Phi` with the Luxemburg norm

\[
\|f\|_{L_\Phi}
=
\inf\left\{\lambda>0:
\int \Phi\!\left(\frac{|f|}{\lambda}\right)d\mu\le1
\right\}.
\tag{2}
\]

For the exact-area Lambert map of PF-191 from `Q(a)` to `Q(a+d)`, let

\[
D_{a,d}(z)=\delta_{g_a,F^*g_{a+d}}(z)
\tag{3}
\]

be the Güneysu--Thalmaier multiplicative metric-deviation scalar. There are fixed `a_0,d_0>0` and constants `0<c<C<infinity` such that for

\[
a\ge a_0,\qquad 0<d\le d_0,
\]

one may use the PF-191 exact-area construction with

\[
\boxed{
 c\,\frac{d(1+a)}{\cosh a}
\le
\|D_{a,d}\|_{L_\Phi(Q(a))}
\le
C\,\frac{d(1+a)}{\cosh a}.
}
\tag{4}
\]

The inverse/target deviation has the same scale. By contrast PF-191 gives

\[
\int_{Q(a)}D_{a,d}\,d\mu
\asymp_{\rm upper}
\frac d{\cosh a},
\tag{5}
\]

so the generic critical Orlicz norm carries one geometric logarithm relative to the persisted `L^1` endpoint currency.

For the exact prime/shift half-cuffs, write

\[
a_n^+=a_n+d_n.
\tag{6}
\]

Then not only the `k=1` Orlicz loss but every fixed Lambert-depth polynomial is summable:

\[
\boxed{
\sum_n
\frac{d_n(1+a_n)^k}{\cosh a_n}<\infty
\qquad\text{for every fixed }k\ge0.
}
\tag{7}
\]

In particular,

\[
\boxed{
\sum_n
\|D_{a_n,d_n}\|_{L_\Phi(Q(a_n))}<\infty,
}
\tag{8}
\]

and likewise on the target side.

Equation (8) is a **coefficient-space result**, not a weak-trace theorem for the prime/shift relative resolvent. It says that the actual logarithmic concentration penalty in the standard symmetrized Cwikel--Solomyak coefficient norm is compatible with the exact prime tail; it does not supply the required hyperbolic/vector-valued operator estimate or its global localization formula.

## 1. The Luxemburg norm is not linearly controlled by bounded `L^1` mass

Sukochev--Zanin's torus theorem is homogeneous in the Luxemburg norm (2), not in the Orlicz modular `int Phi(|f|)`. These quantities must not be conflated at the critical endpoint.

For any nonnegative bounded `f`, put

\[
L=\|f\|_{L^1},\qquad B=\|f\|_{L^\infty}.
\]

If `L>0`, then directly from (2),

\[
\boxed{
\|f\|_{L_\Phi}
\le
L\log\!\left(e+\frac BL\right).
}
\tag{9}
\]

Indeed, set `lambda=L log(e+B/L)`. Since `lambda>=L`,

\[
\begin{aligned}
\int\Phi(|f|/\lambda)
&=\int\frac{|f|}{\lambda}
 \log\!\left(e+\frac{|f|}{\lambda}\right)\\
&\le
\frac L\lambda
\log\!\left(e+\frac B\lambda\right)
\le1.
\end{aligned}
\tag{10}
\]

The logarithm in (9) is real, not an artifact of the proof. If `E` has measure `m`, then homogeneity and (2) give exactly

\[
\|B\mathbf1_E\|_{L_\Phi}
=
\frac B{\Phi^{-1}(1/m)}.
\tag{11}
\]

For `m->0`,

\[
\Phi^{-1}(1/m)\asymp
\frac{1/m}{\log(e/m)},
\]

hence

\[
\boxed{
\|B\mathbf1_E\|_{L_\Phi}
\asymp
B m\log(e/m).
}
\tag{12}
\]

Thus no homogeneous estimate `||f||_{L_Phi}<=C(B)||f||_1` can hold uniformly over increasingly concentrated bounded functions. Small amplitude does not remove this phenomenon because the Luxemburg norm is homogeneous.

## 2. The PF-191 Lambert profile pays exactly one depth logarithm

PF-191's finite triangular branch has area coordinates

\[
d\mu=dy\,d\tau,
\]

and pointwise deviation

\[
D_{a,d}(\tau,y)
\le
C\frac d{1+\sinh^2\tau}.
\tag{13}
\]

The exact cross-section integration in PF-191 gives

\[
\int D_{a,d}\,d\mu
\le C\frac dA,
\qquad
A:=\cosh a,
\tag{14}
\]

while (13) gives `||D_{a,d}||_infinity<=Cd`. Applying (9) to the finite branch, or equivalently to its pointwise majorant, yields

\[
\|D_{a,d}^{\rm fin}\|_{L_\Phi}
\le
C\frac dA\log(e+A)
\le
C\frac{d(1+a)}A.
\tag{15}
\]

PF-191's fixed corner correction has deviation `O(d e^{-2a})` on uniformly bounded area, so its `L_Phi` norm is `O(d e^{-2a})`. The outer branch is an exact isometry. This proves the upper bound in (4).

The same scale is already visible in the actual canonical finite-branch map, not only in the majorant. PF-191 writes

\[
e(\tau)
=
\frac{\lambda^2-1}{1+\lambda^2\sinh^2\tau},
\qquad
\lambda=\frac{\sinh(a+d)}{\sinh a}.
\tag{16}
\]

Since `coth(a)>=1`,

\[
\lambda
=\cosh d+\coth(a)\sinh d
\ge e^d,
\]

so `lambda^2-1>=c d` uniformly for small `d`. On a fixed interval `0<=tau<=tau_0`, equation (16) therefore gives `e(tau)>=c d`. The exact relative metric matrix in PF-191 has, at `y=0`, eigenvalues

\[
1+e(\tau),\qquad (1+e(\tau))^{-1}.
\tag{17}
\]

On the substrip `0<=y<=Y_a(tau)/2`, continuity and the fact that `Y_a(tau)asymp A^{-1}` for fixed small `tau` preserve a lower logarithmic eigenvalue deviation `>=c d` for all large `a`. The Güneysu--Thalmaier scalar is a fixed smooth increasing function of the maximal absolute logarithmic eigenvalue, so

\[
D_{a,d}\ge c d
\tag{18}
\]

on a set of area `m>=c/A`. Equations (11)--(12) then give

\[
\|D_{a,d}\|_{L_\Phi}
\ge
c\,d\frac{\log(e+A)}A
\ge
c\frac{d(1+a)}A,
\tag{19}
\]

which completes (4). Because the PF-191 map is exactly area preserving and inverse metric eigenvalues are reciprocals, the target-side deviation has the same distributional scale.

This identifies the precise bookkeeping correction to the accepted weak-trace clue: boundedness makes the **Orlicz modular** harmless, but the homogeneous Luxemburg norm appearing in the operator theorem still detects the shrinking effective cross-section.

## 3. Prime arithmetic absorbs every fixed Lambert-depth polynomial

PF-191 records the exact collar conversion

\[
\frac1{\sinh a_n}=\sinh\frac{h_n}{2},
\tag{20}
\]

where PF-114 writes

\[
h_n=F(p_{n+1})-F(p_n)
=\int_{p_n}^{p_{n+1}}
\frac{2\pi}{t^2\sin(2\pi/t)}\,dt.
\tag{21}
\]

On the tail the integrand is two-sided comparable to `1/t`. Consequently

\[
\frac1{\cosh a_n}\le C h_n,
\qquad
a_n\le C+\log(1/h_n).
\tag{22}
\]

The prime gap is at least `2`, and Bertrand's postulate gives `p_{n+1}<2p_n`. The lower comparison in (21) therefore gives

\[
h_n\ge c/p_n,
\tag{23}
\]

and hence

\[
a_n\le C+\log p_n.
\tag{24}
\]

PF-121/PF-107 give

\[
d_n\le C/p_n.
\tag{25}
\]

For every fixed `k>=0`, equations (21)--(25) imply

\[
\frac{d_n(1+a_n)^k}{\cosh a_n}
\le
C_k\frac{(1+\log p_n)^k}{p_n}
\int_{p_n}^{p_{n+1}}\frac{dt}{t}.
\tag{26}
\]

For `t in [p_n,p_{n+1}]`, Bertrand gives `t<=2p_n`, so

\[
\frac{(1+\log p_n)^k}{p_n t}
\le
C_k\frac{(1+\log t)^k}{t^2}.
\tag{27}
\]

The prime intervals partition the tail. Summing (26)--(27) therefore yields

\[
\sum_n\frac{d_n(1+a_n)^k}{\cosh a_n}
\le
C_k\int^{\infty}\frac{(1+\log t)^k}{t^2}\,dt
<\infty,
\tag{28}
\]

proving (7). Taking `k=1` and using (4) proves (8).

This argument needs no fine prime-gap theorem. The gain comes from charging the logarithm against the **effective Lambert cross-section** and then summing over the actual prime intervals.

## Prior art and novelty assessment

**F. A. Sukochev, D. V. Zanin**, *Solomyak-type eigenvalue estimates for the Birman--Schwinger operator*, Sbornik: Mathematics **213** (2022), no. 9, 1250--1289. DOI `10.4213/sm9732e`.

- Their equation (2.1) is the Luxemburg norm (2).
- Their Theorem 1.1 proves on `T^d`

\[
\|(1-\Delta)^{-d/4}M_f(1-\Delta)^{-d/4}\|_{1,\infty}
\le c_d\|f\|_{L_\Phi},
\qquad \Phi(t)=t\log(e+t).
\]

- Their Theorem 1.3 gives the corresponding symmetrized Euclidean result with an additional spatial logarithmic moment and explicitly notes that the torus estimate does not literally extend to `R^d` for any symmetric function space.

**F. Sukochev, D. Zanin**, *Optimal Cwikel--Solomyak Estimates*, Journal of Fourier Analysis and Applications **29** (2023), article 21. DOI `10.1007/s00041-023-10003-9`.

- This establishes optimality of the critical Cwikel--Solomyak scale within the relevant Orlicz/Lorentz classes. It reinforces that the `L log L` norm should be treated as a real endpoint currency rather than replaced silently by `L^1`.

No novelty is claimed for the Luxemburg definition, the fundamental function of `L log L`, Bertrand's postulate, or the Cwikel--Solomyak theorem. The project-specific result is (4) and (7): **the exact PF-191 Lambert deformation has a sharp one-logarithm Orlicz concentration cost, and the exact prime/shift sequence absorbs that cost -- indeed any fixed polynomial in Lambert depth -- while retaining global summability.** A targeted literature search did not locate this prime-flute specialization; absence of exact wording is not used as a novelty argument.

## Falsification and boundary checks

A later adversary can test PF-196 by:

1. checking (9) directly from the Luxemburg definition;
2. checking the indicator identity (11) and the elementary asymptotic `Phi^{-1}(s)asymp s/log(e+s)`;
3. inserting PF-191's exact finite-branch profile into (9) to recover (15);
4. checking the lower strip using PF-191's exact `e(tau)` and relative metric matrix, with area `asymp 1/cosh(a)`;
5. verifying (20)--(25) from PF-114/PF-121/PF-191;
6. summing (26) over the disjoint prime intervals using only `p_{n+1}<2p_n`.

The finding would be overclaimed if read as any of the following, none of which is asserted:

- Sukochev--Zanin's torus theorem already applies to the noncompact hyperbolic prime flute;
- a scalar multiplication theorem automatically controls PF-175's matrix-valued vector-gradient form;
- the normalized PF modules have already been reduced to one compact Cwikel--Solomyak model with uniform constants;
- the endpoint conservative splice of PF-183 is constructed;
- finite-color localization and off-diagonal reassembly are lossless;
- the full first relative resolvent is in `S_{1,infinity}`;
- PF-190's `log^2(n)/n` global singular-value envelope has been improved;
- any spectral distinction between primes and the shift clone, zeta identity, or RH consequence follows.

In particular, (7) concerns logarithms of **local Lambert depth**. It does not imply that an arbitrary logarithmic loss in singular-value index, number of localization blocks, or global reassembly is harmless.

## Consequences for the research line

PF-195 showed that the generic one-sided critical route loses the PF-191 effective-area currency much more severely: the standard local-sup weak-`S_2` coefficient norm charges a Lambert body at order `d_n`, and `sum d_n` diverges. PF-196 shows that the directly symmetrized `L log L` route behaves differently. Its homogeneous critical norm does charge concentration and is not literally `L^1`-linear, but the price is only a Lambert-depth logarithm, and that price remains summable on the exact prime/shift tail.

The analytic endpoint gate should therefore no longer demand a local weak-`S_1` estimate with quasi-norm strictly proportional to `int delta`. A uniform reduction to a symmetrized critical estimate with cost

\[
O\!\left(\frac{d_n(1+a_n)^k}{\cosh a_n}\right)
\]

for any fixed `k` is still globally admissible. The unresolved work is to obtain such an estimate for the **actual localized hyperbolic vector-gradient form** and then reassemble it without introducing a different, nonlocal logarithmic loss.