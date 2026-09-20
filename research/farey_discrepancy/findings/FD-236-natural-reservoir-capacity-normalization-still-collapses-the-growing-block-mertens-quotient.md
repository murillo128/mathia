# FD-236 — Natural reservoir-capacity normalization still collapses the growing-block Mertens quotient

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** triangular switched quotient / scale-adapted reservoir capacity / block-Mertens inversion / one-sided positivity / normalization obstruction
- **Depends on:** FD-235, FD-234, FD-233, FD-226
- **Classification:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + TRIANGULAR-QUOTIENT-COLLAPSE + CAPACITY-NORMALIZATION + RESPONSE-SCALE-MISMATCH`

## Claim

FD-235 shows that the fixed-profile switched-blind quotient is vacuous for the canonical block-Mertens repair and leaves open the natural replacement: normalize a growing triangular coefficient family by the physical reservoir capacity and require switched smallness uniformly on the rows actually used by the growing construction.

The most direct source-derived normalization still collapses.

Let `D=D_N=N^{o(1)}` be the divisor depth of a growing switched block, let `J=J(N)` satisfy

\[
2^{j+r_j}\le D
\qquad(0\le j<J),
\tag{1}
\]

where the switched row orders are

\[
r_j\in\{1,4\},
\]

and use the scale-adapted exact floor cells of FD-226. Their prime capacities are, in the FD-226 prime-resolution regime,

\[
|I_d^*\cap\mathbb P|
\asymp
\frac{dN}{D\log(dN)}
\asymp dL_N,
\qquad
L_N:=\frac{N}{D\log N},
\tag{2}
\]

uniformly for `1<=d<=D`.

Thus `L_N d` is the natural coefficient-capacity scale. Define the corresponding triangular blind class to consist of families `h_N=(h_N(d))_(d<=D)` such that

\[
\sup_N\max_{d\le D}
\frac{|h_N(d)|}{L_Nd}<\infty
\tag{3}
\]

and

\[
\max_{0\le j<J}
\frac{|\mathcal R_j(h_N)|}{L_N4^j}
\longrightarrow0,
\tag{4}
\]

where

\[
(\mathscr A h_N)(m)
=
\sum_{d\le m}
 h_N(d)M\!\left(\left\lfloor\frac md\right\rfloor\right),
\qquad
\mathcal R_j(h_N)
=(E-I)^{r_j}(\mathscr A h_N)(2^j).
\tag{5}
\]

Let the canonical real FD-234 correction be

\[
\widetilde c_N(n)
=-\frac12\sum_{d\mid n}
U_N(d),
\qquad
U_N(d)=M(dN)-M((d-1)N).
\tag{6}
\]

Use the already anchored unconditional Korobov--Vinogradov-scale Mertens estimate, after weakening its exponential constant once so that it is uniform on `N<=x<=DN`,

\[
|M(x)|
\ll
x\log x\,e^{-\eta\Phi(N)},
\qquad
\Phi(N)=
\frac{(\log N)^{3/5}}{(\log\log N)^{1/5}},
\tag{7}
\]

and write

\[
T(D)=\max_{n\le D}\tau(n)=D^{o(1)}.
\]

If

\[
\boxed{
\Lambda_N
:=
D\,T(D)(\log N)^2e^{-\eta\Phi(N)}
\longrightarrow0,
}
\tag{8}
\]

then the whole family `\widetilde c_N` belongs to the capacity-normalized triangular blind class (3)--(4). More precisely,

\[
\boxed{
\max_{n\le D}
\frac{|\widetilde c_N(n)|}{L_Nn}
\ll \Lambda_N=o(1),
}
\tag{9}
\]

and

\[
\boxed{
\max_{0\le j<J}
\frac{|\mathcal R_j(\widetilde c_N)|}{L_N4^j}
\ll
D(\log N)^2e^{-\eta\Phi(N)}
=o(1).
}
\tag{10}
\]

Consequently the family-level affine class also contains zero exactly:

\[
\boxed{
\widetilde c_N+\mathcal N_{\rm cap}
=
\mathcal N_{\rm cap},
}
\tag{11}
\]

where `\mathcal N_cap` denotes the triangular class (3)--(4). Choosing `h_N=-\widetilde c_N` gives the zero representative for every `N`.

In particular, throughout the currently certified FD-226 physical blind-block regime, whose stronger common-cushion condition contains an additional factor `D`, the obvious capacity-normalized triangular quotient is still too coarse to carry a nonzero one-sided distance from the positive cone.

This does **not** construct a longer physical countermodel. It identifies a scale mismatch: the coefficient-capacity topology regards the canonical Mertens repair as negligible even though the actual countermodel asks for the switched rows themselves to remain bounded (or otherwise much smaller than the natural quadratic capacity scale). A nonvacuous positivity obstruction therefore needs a finer response topology than `L_N4^j`; once that scale is refined, the fixed-profile FD-233 positive-lift equivalence no longer transfers automatically.

## 1. The scale-adapted reservoirs canonically select `L_N`

FD-226 replaces the common-width divisor reservoirs by

\[
I_d^*
=\left(
 dN\left(1-\frac1{4D}\right),
 dN
\right],
\qquad1\le d\le D,
\tag{12}
\]

while preserving the exact source-side floor table

\[
\left\lfloor\frac{mN}{r}\right\rfloor
=
\left\lfloor\frac md\right\rfloor
\qquad
(r\in I_d^*,\ 1\le m,d\le D).
\tag{13}
\]

In the same prime-number-theorem regime, FD-226 gives

\[
|I_d^*\cap\mathbb P|
\gg
\frac{dN}{D\log(dN)}.
\tag{14}
\]

The matching upper bound follows from the same asymptotic prime-counting input, and `D=N^{o(1)}` gives

\[
\log(dN)=(1+o(1))\log N
\]

uniformly for `d<=D`. Therefore (2) holds up to fixed constants.

This makes `L_N=N/(D\log N)` the smallest-cell occupancy scale and `dL_N` the natural linear capacity at divisor index `d`. Normalizing a coefficient family by `L_N` converts the physical reservoir envelope into a uniform linear envelope. Thus (3) is not an arbitrary functional-analytic normalization; it is the immediate coefficient scale supplied by the exact source representation of FD-226.

The prime asymptotic is needed only for this physical interpretation of the normalization. The collapse proved below uses the already established divisor-response algebra and the Mertens bound.

## 2. The canonical repair is uniformly tiny in the normalized coefficient envelope

FD-234 gives the exact real inverse (6). For `d>=2`, the uniform form of (7) implies

\[
|U_N(d)|
\le
|M(dN)|+|M((d-1)N)|
\ll
 dN\log N\,e^{-\eta\Phi(N)}.
\tag{15}
\]

The same estimate holds for `d=1` after using `U_N(1)=M(N)`. Hence, for `n<=D`,

\[
\begin{aligned}
|\widetilde c_N(n)|
&\le
\frac12
\sum_{d\mid n}|U_N(d)|\\
&\ll
N\log N\,e^{-\eta\Phi(N)}
\sum_{d\mid n}d\\
&\le
N\log N\,e^{-\eta\Phi(N)}
 n\tau(n).
\end{aligned}
\tag{16}
\]

Dividing by

\[
L_Nn
=
\frac{Nn}{D\log N}
\]

gives

\[
\frac{|\widetilde c_N(n)|}{L_Nn}
\ll
D(\log N)^2e^{-\eta\Phi(N)}\tau(n)
\le
\Lambda_N.
\tag{17}
\]

Taking the maximum over `n<=D` proves (9). Thus under (8) the canonical repair is not merely uniformly linearly bounded after capacity normalization; its normalized weighted-sup norm tends to zero.

The stronger sufficient condition retained by FD-226 for the actual full-grid positive-cushion construction is of the form

\[
D^2T(D)(\log N)^2e^{-\eta'\Phi(N)}=o(1)
\tag{18}
\]

for a possibly weakened positive constant `eta'`. After weakening `eta` consistently, (18) implies (8). Therefore every currently certified physical block already lies inside the coefficient-collapse regime (9).

## 3. The switched rows are also negligible at quadratic capacity scale

The exact FD-234 inverse satisfies

\[
\mathscr A\widetilde c_N(m)
=-\frac12M(mN).
\tag{19}
\]

Consequently

\[
\mathcal R_j(\widetilde c_N)
=-\frac12
(E-I)^{r_j}M(2^jN).
\tag{20}
\]

Expanding the bounded-order difference,

\[
\mathcal R_j(\widetilde c_N)
=-\frac12
\sum_{t=0}^{r_j}
(-1)^{r_j-t}
\binom{r_j}{t}
M(2^{j+t}N).
\tag{21}
\]

Condition (1) keeps all arguments `2^{j+t}N` within the uniform range `<=DN`. Applying (7), using `r_j<=4`, and absorbing the bounded binomial factor gives

\[
|\mathcal R_j(\widetilde c_N)|
\ll
2^jN\log N\,e^{-\eta\Phi(N)}.
\tag{22}
\]

Since

\[
L_N4^j
=
\frac{N}{D\log N}4^j,
\]

we obtain

\[
\frac{|\mathcal R_j(\widetilde c_N)|}{L_N4^j}
\ll
\frac{D(\log N)^2e^{-\eta\Phi(N)}}{2^j}.
\tag{23}
\]

The right side is maximal at the first row. Because `T(D)>=1`, condition (8) implies that this maximum tends to zero, proving (10).

This is the coupled `N,J(N)` estimate missing from FD-235. The collapse is no longer caused by first freezing `N` and then sending `j` far past `\log N`; it holds uniformly on the actual precoverage row window itself after normalization by the natural reservoir capacity.

## 4. The natural triangular affine problem is therefore still vacuous

Let `\mathcal N_cap` denote the family class defined by (3)--(4). Equations (9)--(10) show that

\[
\widetilde c_N\in\mathcal N_{\rm cap}.
\tag{24}
\]

The class is linear, so also `-\widetilde c_N` belongs to it. Therefore the affine family

\[
\widetilde c_N+\mathcal N_{\rm cap}
\]

contains the zero coefficient vector at every `N`, proving (11). Any one-sided negative-capacity distance computed in this quotient is consequently zero, regardless of whether it is measured bandwise or over the whole finite divisor range.

This rules out the most immediate repair of the quantifier problem found in FD-235. Coupling `N` and `J(N)` is necessary, but **capacity normalization plus coupled rows is still not sufficient**: the physical Mertens repair itself becomes a blind perturbation at that scale.

The result also clarifies the surviving `D^2` pressure of FD-226. That pressure cannot be recovered by asking only whether the signed correction is small relative to each reservoir's total coefficient capacity. In the currently certified regime it is much smaller than that capacity. The extra factor `D` appears only when one asks for a single nonnegative filling whose switched output remains at the much finer target scale used by the countermodel.

## 5. Why the FD-233 positive-lift theorem cannot simply be transplanted to a finer quotient

FD-233 proves, for a fixed coefficient profile at the quadratic switched scale, that vanishing negative aggregate capacity is exactly the criterion for adding the minimal nonnegative slack without changing the switched response by more than `o(4^j)`. After the source normalization used here, the analogous coarse response scale is `L_N4^j`.

FD-236 shows that this coarse scale is too permissive: it already declares the entire canonical physical repair negligible. To retain the information needed by the physical construction, a future triangular quotient must therefore impose a finer tolerance, say `S_{N,j}`, with

\[
S_{N,j}=o(L_N4^j)
\tag{25}
\]

on at least the decisive row range. The bounded switched target of FD-225 is an extreme example of such a much finer scale.

But once (25) replaces the capacity scale, the FD-233 sufficiency proof no longer applies automatically. Its elementary estimate shows that a nonnegative slack with asymptotically sparse capacity contributes `o(L_N4^j)` after normalization; it does **not** in general show that the same slack is `o(S_{N,j})` for an arbitrarily smaller response scale.

Thus the live positivity question has two coupled pieces rather than one:

1. choose a response normalization fine enough that the canonical Mertens repair is not itself quotiented out on `0<=j<J(N)`;
2. prove a matching one-sided positive-lift theorem at that finer scale, rather than importing the capacity-scale criterion from FD-233.

This is a genuine normalization obstruction. The coefficient scale is dictated naturally by the physical reservoirs, but the response topology required by exact switched cancellation is strictly finer than the quadratic response naturally generated by that coefficient capacity.

## 6. Prior-art boundary and verdict

The external audit found only generic theories of weighted sequence spaces, positive cones and weighted triangular arrays. They supply standard language for row-uniform normalization but no theorem that identifies the Mathia divisor-response scale or resolves the one-sided block-Mertens problem. No such general result is load-bearing here.

The only analytic input used in the proof is the Korobov--Vinogradov-scale unconditional Mertens estimate already recorded in `SOURCES.md` for Lee--Leong and already used by FD-223--FD-226. The remaining steps are exact consequences of FD-226's reservoir capacities and FD-234's divisor inversion. No new source anchor is therefore required.

No novelty is claimed for weighted triangular-array normalization, positive cones, or the estimate `T(D)=D^{o(1)}`. The research-specific conclusion is the scale comparison: the obvious source-derived normalization proposed by the FD-235 frontier still places the canonical block-Mertens repair itself in the triangular blind class throughout the existing construction regime.

**Verdict.** Replacing the fixed-profile quotient by the natural reservoir-capacity triangular quotient does not make the one-sided Mertens obstruction nontrivial. The canonical repair is uniformly negligible both in normalized coefficient size and in normalized switched response, so its affine class again contains zero. The next meaningful formulation must refine the **response scale**, not merely the order of quantifiers or the coefficient normalization, and must re-prove positive-lift control at that finer scale.