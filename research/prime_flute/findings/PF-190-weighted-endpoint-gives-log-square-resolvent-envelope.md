# PF-190 — weighted endpoint control gives a log-square resolvent singular-value envelope

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + CONDITIONAL/ENDPOINT`. PF-175 proves that two-sided inverse-unit-ball weighted metric defect in `L^r`, `r>1`, places the dual-volume first relative resolvent in `S_r`, but its proof stops at `r=1` because each gradient-resolvent half-factor reaches a logarithmically divergent strong-`S_2` time integral. Tracking that divergence instead of discarding it gives a quantitative endpoint extrapolation. If the same two-metric comparison has finite weighted `L^1` defect, then the dual-volume relative resolvent satisfies

\[
s_n(T)\le C\,\frac{(1+\log(n+1))^2}{n+1},
\qquad
T:=R_hJ^\vee-IR_g.
\]

Thus the PF-175 bridge has a concrete log-square weak-trace envelope even without a genuine weak-`S_1` theorem. This is strictly weaker than `S_{1,\infty}` and must not be called weak trace class. PF-189 is stronger on the complete decoupled short-collar central sector, so any genuine full-surface endpoint loss beyond `1/n` is not forced by the collapsing central family itself.

## Claim

Use the complete quasi-isometric hyperbolic two-metric setup and notation of PF-175. In particular,

\[
R_g=(H_g+1)^{-1},
\qquad
R_h=(H_h+1)^{-1},
\qquad
J^\vee=(I^{-1})^*,
\]

and let `delta=delta_{g,h}` be the Güneysu--Thalmaier metric-deviation scalar. Define

\[
A_1:=
\int_M W_g\,\delta\,d\mu_g
+
\int_M W_h\,\delta\,d\mu_h.
\tag{1}
\]

Assume

\[
\boxed{A_1<\infty.}
\tag{2}
\]

Because the metrics are globally quasi-isometric, `delta` is uniformly bounded by a constant depending only on the quasi-isometry constant. Then there is a constant `C`, depending only on the same geometric/quasi-isometry constants as PF-175, such that for every

\[
1<r\le\frac32,
\]

\[
\boxed{
\|R_hJ^\vee-IR_g\|_{\mathcal S_r}
\le
C(1+A_1)(r-1)^{-2}.
}
\tag{3}
\]

Consequently, for all `n>=1`, after enlarging `C` to absorb the finite head,

\[
\boxed{
s_n(R_hJ^\vee-IR_g)
\le
C(1+A_1)
\frac{(1+\log(n+1))^2}{n+1}.
}
\tag{4}
\]

Equation (4) is an endpoint **upper envelope**, not a weak-trace conclusion. It does not imply

\[
R_hJ^\vee-IR_g\in\mathcal S_{1,\infty},
\tag{5}
\]

and it does not prove failure of (5) either.

If the comparison is area preserving, so that `rho=1` and hence

\[
J^\vee=I=U,
\tag{6}
\]

then (3)--(4) apply to the standard density-unitary/common-Hilbert-space first relative resolvent as well. For the prime/shift pair that would coexist with PF-112's non-`S_1` theorem; it would still leave the exact weak-`S_1` endpoint open.

## 1. Weighted `L^1` supplies every PF-175 power with controlled size

Let

\[
D:=\|\delta\|_{L^\infty}<\infty.
\tag{7}
\]

For `r>1`, put

\[
A_r:=
\int_M W_g\,\delta^r\,d\mu_g
+
\int_M W_h\,\delta^r\,d\mu_h.
\tag{8}
\]

Pointwise boundedness gives

\[
\delta^r\le D^{r-1}\delta,
\]

and therefore

\[
\boxed{A_r\le D^{r-1}A_1.}
\tag{9}
\]

Thus the endpoint hypothesis (2) automatically supplies PF-175's hypothesis at every exponent `r>1`. What remains is to retain the dependence of the `S_r` constant as `r` approaches `1`.

## 2. The only singular near-endpoint constant is the gradient half-factor

PF-175 obtains its dual-volume factorization from the exact form identity

\[
\begin{aligned}
\langle Tf,z\rangle_h
={}&-
\int_M g^*(C\,dR_gf,dR_hz)\,d\mu_g\\
&-
\int_M b\,(R_gf)\overline{R_hz}\,d\mu_g,
\end{aligned}
\tag{10}
\]

with coefficient fields satisfying

\[
|C|+|b|\le C_0\delta.
\tag{11}
\]

Its interpolated heat-gradient estimate is, for `q>=2` and `0<t<=1`,

\[
\|M_a d e^{-tH_j}\|_{\mathcal S_q}
\le
C_q t^{-1/2-1/q}
\|a\|_{L^q(W_jd\mu_j)}.
\tag{12}
\]

The interpolation constants `C_q` remain bounded for `2<=q<=3`: they come from interpolation between the fixed Hilbert--Schmidt and operator endpoints, so there is no singularity in `C_q` itself as `q` decreases to `2`.

Integrating the resolvent representation over `0<t<=1` gives

\[
\int_0^1 t^{-1/2-1/q}\,dt
=
\frac{2q}{q-2}.
\tag{13}
\]

The `t>=1` part is uniformly harmless by semigroup contractivity after one fixed positive time. Hence, uniformly for `2<q<=3`,

\[
\boxed{
\|M_a dR_j\|_{\mathcal S_q}
\le
C\frac{q}{q-2}
\|a\|_{L^q(W_jd\mu_j)}.
}
\tag{14}
\]

By contrast, the scalar heat estimate has small-time power `t^{-1/q}`. Its time integral stays uniformly finite for `2<=q<=3`, so

\[
\boxed{
\|M_aR_j\|_{\mathcal S_q}
\le C
\|a\|_{L^q(W_jd\mu_j)}
}
\tag{15}
\]

on the same exponent range.

Set `q=2r`. Then

\[
\frac{q}{q-2}=\frac{r}{r-1}.
\tag{16}
\]

Using `a=|C|^{1/2}` on the two sides of the gradient term, PF-175's quasi-isometric source/target norm conversion, and Schatten Hölder gives

\[
\|T_{\rm grad}\|_{\mathcal S_r}
\le
C\left(\frac{r}{r-1}\right)^2 A_r^{1/r}.
\tag{17}
\]

The scalar term satisfies the better uniform estimate

\[
\|T_{\rm scalar}\|_{\mathcal S_r}
\le C A_r^{1/r}.
\tag{18}
\]

For `1<r<=3/2`, equations (9), (17), and (18) imply

\[
A_r^{1/r}
\le
D^{(r-1)/r}A_1^{1/r}
\le C_D(1+A_1),
\tag{19}
\]

and (3) follows.

The square in `(r-1)^{-2}` has a precise origin: the principal coefficient perturbation in (10) is sandwiched between **two** gradient-resolvent half-factors, and each is critical at strong `S_2`.

## 3. Optimizing the Schatten exponent produces the log-square envelope

For every compact operator and `r>0`, decreasing singular values satisfy

\[
n\,s_n(T)^r
\le
\sum_{k=1}^n s_k(T)^r
\le
\|T\|_{\mathcal S_r}^r.
\tag{20}
\]

Therefore

\[
s_n(T)
\le
n^{-1/r}\|T\|_{\mathcal S_r}.
\tag{21}
\]

For sufficiently large `n`, choose

\[
r_n=1+\frac1{\log n},
\tag{22}
\]

which lies in `(1,3/2]`. Then

\[
(r_n-1)^{-2}=(\log n)^2,
\tag{23}
\]

while

\[
n^{-1/r_n}
=
\frac1n n^{(r_n-1)/r_n}
\le
\frac e n.
\tag{24}
\]

Substituting (3) into (21) proves (4), with small `n` absorbed into the constant.

This argument is deliberately elementary. It does not invoke a limiting interpolation theorem at `r=1`, and it does not pretend that membership in every `S_r`, `r>1`, alone implies a harmonic `1/n` singular-value bound. The quantitative norm growth is the entire point.

## 4. What PF-189 says about the possible source of the logarithmic loss

PF-189 proves a strictly stronger statement on the complete fixed-central Dirichlet short-collar sector:

\[
A_{\rm thin}^D\in\mathcal S_{1,\infty}\setminus\mathcal S_1,
\qquad
s_n(A_{\rm thin}^D)=O(n^{-1}).
\tag{25}
\]

It also gives a vanishing tail weak-trace budget. Therefore the `log^2 n/n` envelope in (4) is not forced by the mere existence, pinching, or multiplicity of the canonical Margulis-short central collars.

There are two possibilities left open. The logarithmic loss may be only an artifact of extrapolating the coarse PF-175 global half-factor bound, in which case a true weak-`S_2` endpoint estimate for the gradient halves could remove it. Or the full body/interface/uncut assembly may contain a genuine endpoint mechanism absent from the orthogonal thin-sector model. PF-190 does not choose between those possibilities.

For the accepted `CLUE-shift-clone-sharp-schatten-threshold`, the critical endpoint test is therefore sharper than simply asking for all `S_r`, `r>1`: after the global weighted geometry is controlled, determine whether the two critical gradient half-factors admit a project-specific weak-`S_2` estimate or whether the full assembly exhibits an unavoidable logarithmic loss.

## 5. Prime/shift consequence remains conditional on the global geometry

PF-174 proves the endpoint weighted `L^1` budget on the complete Margulis-short collar family, and PF-189 places its central first-resolvent sector directly in weak trace class. Neither result supplies the missing globally coherent body/interface comparison.

Thus (4) becomes a theorem about the exact prime flute versus its all-composite shift clone only after one marking satisfies the full two-sided weighted endpoint condition (2). In particular, PF-130/PF-139's unweighted body control cannot be substituted for (2), and the unresolved collar/body assembly cannot be dropped.

If the future comparison is also area preserving, then (6) removes PF-175's identification strip and the standard first relative resolvent would satisfy the same log-square envelope for free. This would still be a **negative control** rather than arithmetic evidence: the comparator is an exact all-composite flute preserving the ordered prime gaps.

## 6. Prior art and novelty audit

No novelty is claimed for the elementary implication from a quantified family of Schatten norms to a logarithmically weakened singular-value estimate. Equation (21) followed by optimization of `r` is standard sequence-space/operator-ideal reasoning.

A directed audit of critical Cwikel--Solomyak and weak-Schatten literature confirms that true critical weak ideals are normally separate endpoint statements rather than automatic consequences of strong `S_r` membership for every `r>1`. In particular, the critical symmetrized Cwikel--Solomyak theory on compact `d`-dimensional models treats `L_{1,\infty}` through endpoint function spaces such as `L log L`; those theorems have different operators and hypotheses and are **not imported** here. The present proof needs no new external theorem beyond the heat/gradient estimates already audited in PF-174/PF-175.

The project-specific mathematical delta is the quantitative extraction of the near-endpoint constant already latent in PF-175 and its comparison with PF-189: finite weighted endpoint geometry gives a full dual-resolvent singular-value envelope `O(log^2 n/n)`, while the exact collapsing central family is known to obey the sharper `O(1/n)` law.

No claim is made that the exponent `2` on the logarithm is sharp, new in general operator theory, or realized by the prime/shift pair.

## 7. Audit / falsification core

A later adversary can check PF-190 through the following finite chain:

1. verify from quasi-isometry that `delta` is uniformly bounded and hence (9) follows from the endpoint budget (2);
2. revisit PF-175's interpolation from the fixed `S_2` and operator heat-gradient endpoints and check that `C_q` stays bounded for `2<=q<=3`;
3. integrate the exact small-time exponent in (12) and recover the sole near-endpoint divergence `2q/(q-2)`;
4. set `q=2r`, apply the two-sided coefficient factorization and Schatten Hölder, and verify the square `(r-1)^{-2}` in (17);
5. verify that the scalar half-factors have no corresponding endpoint divergence;
6. use (9) only after preserving both weighted source and target measures from PF-175;
7. apply the elementary singular-value estimate (20), choose (22), and verify (24);
8. do **not** upgrade (4) to `S_{1,\infty}` without a separate weak-endpoint argument;
9. do **not** transfer the dual conclusion to the standard density-unitary identification unless the density correction is separately controlled or `rho=1`;
10. preserve PF-189's decoupling boundary and PF-175's global weighted-geometry boundary.

A refutation would need to show that one of PF-175's fixed-time interpolation constants is not uniform near `q=2`, that the resolvent half-factor estimate has additional hidden exponent loss, that the endpoint weighted budget fails to imply (9), or that the singular-value optimization has been applied to an `r`-dependent operator rather than the fixed operator `T`. None of those issues is present in the stated conditional setup.

## Research consequence

The first-resolvent endpoint now has three distinct levels that must not be conflated:

\[
\mathcal S_1
\subsetneq
\mathcal S_{1,\infty}
\subsetneq
\left\{T:s_n(T)=O\!\left(\frac{\log^2 n}{n}\right)\right\}
\tag{26}
\]

at the level of the bounds established here. PF-112 excludes the first level for the standard prime/shift identification, PF-189 reaches the second on the complete decoupled thin sector, and PF-190 supplies the third conditionally for the full dual-volume resolvent under a global endpoint weighted metric budget.

The next endpoint advance must therefore come from a genuine weak-`S_2` gradient-half estimate, sharper project-specific body/interface localization, or a counterexample showing that the full assembly really loses logarithms. Merely proving `S_r` separately for every `r>1` without tracking constants cannot decide that boundary.