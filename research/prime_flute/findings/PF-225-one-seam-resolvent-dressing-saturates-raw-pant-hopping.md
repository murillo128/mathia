# PF-225 — one-seam resolvent dressing saturates raw pant hopping

**Status:** `EXACT-DERIVED + OPERATOR-THEORETIC + POSITIVE/ROUTE-NARROWING`. PF-224 proves that the reciprocal-prime jump does not regularize the **raw** normalized pant crossings: on many edges `\delta_j\|B_j\|` is at least order `1/\log P_j`, so neither raw trace-norm summation nor even a uniform weak-`S_1` bound on the oriented sum `\sum\delta_jB_j` is possible. The dressed cut flux appearing in the exact PF-222 commutator is quantitatively different. If

\[
X_j:=(1-E_j)DE_j,
\qquad D=(I+K)^{-1},
\]

is the off-diagonal resolvent block across the `j`th prefix cut and `B_j=\Pi_{j+1}K\Pi_j` is the unique raw pant crossing, then every singular value satisfies

\[
\boxed{
 s_k(X_j)\le \min\left\{\frac12,\,s_k(B_j)\right\}.
}
\]

The `s_k(B_j)` bound is the exact one-seam resolvent factorization through the decoupled positive inverse; the universal `1/2` cap comes only from `0\le D\le I`. Since `[D,E_j]` has the singular values of `X_j` twice, the correct strong one-cut currency is not `\|B_j\|_1` but the **saturated channel mass**

\[
\mathfrak c_j
:=\sum_{k\ge1}\min\left\{\frac12,s_k(B_j)\right\}
=\int_0^{1/2}N_{B_j}(t)\,dt,
\]

for which

\[
\boxed{
\|[D,E_j]\|_1\le2\mathfrak c_j.
}
\]

Consequently

\[
\boxed{
\sum_j\delta_j\mathfrak c_j<\infty
\quad\Longrightarrow\quad
[D,\Omega]\in\mathcal S_1,
}
\qquad
\Omega=\sum_j\delta_jE_j.
\]

In particular, if `B_j` has rank `r_j`, then `\|[D,E_j]\|_1\le r_j`; a uniformly finite-channel Jacobi model would make the reciprocal-prime commutator trace class automatically because `\sum_j\delta_j<\infty`. This identifies precisely what the PF-223 countermodel must exploit: not large raw hopping and not fixed-edge noncompactness, but **growing effective transport multiplicity**. It also neutralizes the specific PF-224 lower-bound channel after inversion: regardless of how large `\|B_j\|` becomes,

\[
\delta_j s_1(X_j)\le\frac{\delta_j}{2},
\qquad
\sum_j\frac{\delta_j}{2}<\infty.
\]

Thus the unresolved weak-trace endpoint is now a quantitative **channel-count/frequency-distribution** problem for the dressed one-pant flux. Large raw conductance by itself is no longer a candidate obstruction. The remaining danger is that the number of singular channels surviving near the saturation scale, together with the smaller-frequency tail, grows quickly enough along the thin-pant degeneration to defeat the reciprocal-prime layer weights.

## Claim

Retain the simultaneous normalized boundary decomposition of PF-214--PF-224,

\[
\mathcal B=\bigoplus_{n\ge1}\mathcal B_n,
\qquad
K\ge0,
\qquad
D=(I+K)^{-1},
\qquad 0\le D\le I.
\tag{1}
\]

For the prefix projection

\[
E_j=\sum_{n\le j}\Pi_n,
\qquad F_j:=I-E_j,
\tag{2}
\]

let `K^{(j)}` be PF-222's positive decoupled form obtained by deleting the unique crossing between modules `j` and `j+1`, and put

\[
D^{(j)}=(I+K^{(j)})^{-1}.
\tag{3}
\]

PF-222 proves that the crossing perturbation is the bounded smoothing operator

\[
C_j=B_j+B_j^*,
\qquad
B_j=F_jB_jE_j=\Pi_{j+1}K\Pi_j,
\tag{4}
\]

and that

\[
D-D^{(j)}=-DC_jD^{(j)}.
\tag{5}
\]

Define the dressed oriented cut block

\[
X_j:=F_jDE_j.
\tag{6}
\]

Then for every `k\ge1`,

\[
\boxed{
s_k(X_j)\le s_k(B_j)
}
\tag{7}
\]

and independently

\[
\boxed{
\|X_j\|\le\frac12.
}
\tag{8}
\]

Hence

\[
\boxed{
s_k(X_j)\le\min\left\{\frac12,s_k(B_j)\right\}.
}
\tag{9}
\]

Relative to the cut decomposition `E_j\mathcal B\oplus F_j\mathcal B`,

\[
[D,E_j]
=
\begin{pmatrix}
0&-X_j^*\\
X_j&0
\end{pmatrix},
\tag{10}
\]

so every nonzero singular value of `X_j` occurs twice in `[D,E_j]`. Therefore

\[
\boxed{
\|[D,E_j]\|_1
=2\sum_{k\ge1}s_k(X_j)
\le
2\sum_{k\ge1}\min\left\{\frac12,s_k(B_j)\right\}.
}
\tag{11}
\]

Writing

\[
\mathfrak c_j
:=\sum_{k\ge1}\min\left\{\frac12,s_k(B_j)\right\},
\tag{12}
\]

one also has the exact counting representation

\[
\boxed{
\mathfrak c_j
=\int_0^{1/2}N_{B_j}(t)\,dt.
}
\tag{13}
\]

For the reciprocal-prime layer weights of PF-221/PF-222,

\[
\delta_j
=\frac1{P_j}-\frac1{P_{j+1}}>0,
\qquad
\sum_j\delta_j<\infty,
\tag{14}
\]

PF-222 gives the operator-norm identity

\[
[D,\Omega]
=\sum_{j\ge1}\delta_j[D,E_j].
\tag{15}
\]

Consequently the stronger weighted channel-count condition

\[
\boxed{
\sum_{j\ge1}\delta_j\mathfrak c_j<\infty
}
\tag{16}
\]

implies convergence of (15) in trace norm and therefore

\[
\boxed{[D,\Omega]\in\mathcal S_1.}
\tag{17}
\]

The same conclusion holds a fortiori for the physical low/high remainder `P[D,\Omega]H`.

Two useful specializations are immediate. If `r_j=\operatorname{rank}B_j<\infty`, then

\[
\boxed{\mathfrak c_j\le\frac{r_j}{2},
\qquad
\|[D,E_j]\|_1\le r_j.}
\tag{18}
\]

Thus

\[
\sum_j\delta_jr_j<\infty
\quad\Longrightarrow\quad
[D,\Omega]\in\mathcal S_1,
\tag{19}
\]

and in particular `\sup_jr_j<\infty` is sufficient without any bound on `\|B_j\|`.

More generally, for every `0<p\le1`,

\[
\mathfrak c_j
\le 2^{p-1}\sum_k s_k(B_j)^p,
\tag{20}
\]

so a weighted small-`p` Schatten estimate

\[
\sum_j\delta_j\|B_j\|_p^p<\infty
\tag{21}
\]

is another sufficient trace-class route. Equation (20) is only a convenient corollary; the saturation/counting form (12)--(13) is the sharper currency because it does not continue charging a channel once its raw normalized hopping exceeds order one.

## 1. The decoupled resolvent factorization preserves raw singular-value tails

PF-222 already supplies the domain-safe resolvent identity (5), so no global boundedness of `[K,\Omega]` is needed here. Since `D^{(j)}` commutes with `E_j`,

\[
X_j
=F_j(D-D^{(j)})E_j
=-F_jDC_jD^{(j)}E_j.
\tag{22}
\]

The rightmost factor `D^{(j)}E_j` has range in the prefix. Therefore the `B_j^*` half of `C_j` annihilates it and

\[
C_jD^{(j)}E_j
=B_jE_jD^{(j)}E_j.
\tag{23}
\]

Likewise the result of (23) lies in the tail, so

\[
\boxed{
X_j
=-(F_jDF_j)B_j(E_jD^{(j)}E_j).
}
\tag{24}
\]

Both diagonal compressions in (24) are contractions: `0\le D,D^{(j)}\le I`. The standard singular-value ideal inequality for bounded left/right multiplication therefore gives

\[
s_k(X_j)
\le
\|F_jDF_j\|\,s_k(B_j)\,\|E_jD^{(j)}E_j\|
\le s_k(B_j),
\tag{25}
\]

which is (7).

This estimate is deliberately one-sided. It does not say that a large singular value of `B_j` remains large after inversion. PF-224's entire warning is that using `B_j` as though it were the dressed flux is too crude. Equation (25) preserves the useful **small** singular-value tail of the smoothing pant crossing while leaving room for the inverse to suppress its large modes.

## 2. Positivity imposes a sharp universal `1/2` cap after inversion

The missing large-mode estimate uses no pant geometry. Let `x\in E_j\mathcal B` and `y\in F_j\mathcal B` be unit vectors and write

\[
a=\langle x,Dx\rangle,
\qquad
c=\langle y,Dy\rangle,
\qquad
b=\langle y,Dx\rangle.
\tag{26}
\]

The two-dimensional compression of `D` to `\operatorname{span}\{x,y\}` is a positive contraction. Positivity of `D` gives

\[
|b|^2\le ac,
\tag{27}
\]

while positivity of `I-D` gives

\[
|b|^2\le(1-a)(1-c).
\tag{28}
\]

If `a+c\le1`, then `ac\le1/4`; if `a+c\ge1`, then `(1-a)(1-c)\le1/4`. Hence in all cases

\[
|b|\le\frac12.
\tag{29}
\]

Taking the supremum over `x,y` proves (8). The constant is sharp already for the rank-one projection onto `(1,1)/\sqrt2` in a two-dimensional cut.

Combining (8) with (25) yields the pointwise saturation inequality (9). This is the exact mechanism missing from the raw PF-224 budget: the inverse `D=(I+K)^{-1}` cannot transmit arbitrarily large normalized precision hopping across any cut. Once a channel reaches order-one dressed coupling, additional growth of the raw precision singular value is free at the level of (11).

## 3. The layer expansion is charged by channel count, not raw amplitude

Equation (10) shows directly that

\[
[D,E_j]^*[D,E_j]
=
\begin{pmatrix}
X_j^*X_j&0\\
0&X_jX_j^*
\end{pmatrix},
\tag{30}
\]

which proves the doubled singular-value statement and (11). For any nonnegative singular-value sequence,

\[
\sum_k\min\{a,s_k\}
=\int_0^aN(t)\,dt,
\tag{31}
\]

so (13) follows with `a=1/2`.

This gives a concrete interpretation of `\mathfrak c_j`: it is the area under the one-pant singular-value counting function only up to the **resolvent saturation scale**. A huge first raw singular value and a merely order-one first raw singular value cost the same order in this budget. What can still become expensive is having many boundary-frequency channels above that scale or a sufficiently thick tail of subcritical singular values.

If (16) holds, equation (11) gives

\[
\sum_j\delta_j\|[D,E_j]\|_1<\infty.
\tag{32}
\]

Thus the finite layer sums are Cauchy in `\mathcal S_1`. Their trace-norm limit agrees with PF-222's operator-norm limit (15), proving (17).

The finite-rank consequence (18) is especially diagnostic for PF-223. Fixed-edge finite rank alone is not enough because the rank may grow without control, exactly as its transport packets do. But **uniform** rank would have killed that countermodel immediately, regardless of how large the raw block norms became. PF-223's failure mode is therefore quantitatively pinned to effective channel multiplicity rather than to positivity, nearest-neighbor support, or raw hopping size.

## 4. PF-224's lower-bound channel is summable after dressing

PF-224 proves on a large set of actual prime-flute edges that

\[
\delta_j\|B_j\|
\gtrsim\frac1{\log P_j}.
\tag{33}
\]

That lower bound is fatal to any argument replacing the dressed flux by `\delta_jB_j`. It says nothing comparable about the dressed block. From (8),

\[
\boxed{
\delta_j\|X_j\|
\le\frac{\delta_j}{2}.
}
\tag{34}
\]

Since the reciprocal-prime variation telescopes,

\[
\sum_j\delta_j
=\frac1{P_1}<\infty
\tag{35}
\]

up to the harmless finite-head convention. Therefore the **single large channel** detected by PF-215/PF-224 cannot by itself generate a dressed divergence, even if it is present on every tail edge.

This does not contradict PF-112's non-trace-class theorem for the complete first relative resolvent. It does not even prove `[D,\Omega]\in\mathcal S_1`: equation (11) can still fail to be summable through a growing number of saturated or near-saturated channels. It only identifies which quantitative feature remains capable of doing so.

The next canonical calculation should therefore stop asking for an upper bound on `\|B_j\|`. That norm is allowed to diverge. Instead estimate the actual one-pant counting function

\[
N_{B_j}(t),
\qquad 0<t\le\frac12,
\tag{36}
\]

in the physical seam-frequency variable, or estimate the corresponding dressed low/high count directly. PF-212 already shows why physical frequency rather than artificial cell count is the right currency on the seam strips. PF-225 does not import PF-212's strip estimate as a pant-crossing theorem; it identifies the precise counting quantity a successful transfer must control.

## 5. Prior art and novelty audit

No novelty is claimed for the abstract ingredients. Block resolvent/Schur-complement factorization is standard matrix and operator theory; a general reference is Fuzhen Zhang (ed.), *The Schur Complement and Its Applications*, Springer, 2005, DOI `10.1007/b105056`. Singular-value monotonicity under bounded left/right multiplication and trace-ideal convergence are standard; see Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., AMS Mathematical Surveys and Monographs 120 (2005). PF-222 already audits the separate elliptic fact that a fixed cross-component pant DtN block is smoothing.

The `1/2` cap is proved above directly from the elementary order inequalities `0\le D\le I`; it is not presented as a new general positive-operator theorem. A targeted search of block-matrix/Schur-complement and trace-ideal literature did not identify a result that supplies the missing **PF-degeneration-dependent** channel count. Fixed-domain Schur-complement or DtN smoothing theorems do not control how many normalized crossing singular values remain order one as the canonical one-cusp pants degenerate.

The project-specific durable deduction is the combination of PF-222's exact one-seam decoupling with PF-224's raw-hopping obstruction: **resolvent dressing replaces raw trace mass by saturated channel mass, so the actual PF endpoint cannot fail merely because one or finitely many normalized pant hopping modes diverge.** Any remaining obstruction must be multiplicity/frequency accumulation after that saturation.

## 6. Falsification and boundary checks

1. Equation (24) uses exactly PF-222's decoupled positive resolvent and its bounded fixed-edge crossing. It does not assume a globally bounded `[K,\Omega]`.
2. The orientation of `B_j` matters: `B_j=F_jB_jE_j`. The adjoint half of `C_j` vanishes on `D^{(j)}E_j`, which is why the factorization contains one copy of `B_j` rather than `C_j`.
3. The contractions in (24) are compressions of positive contractions. No lower bound on them is asserted; hence (9) is an upper estimate only.
4. The `1/2` cap applies to the dressed off-diagonal block of **any** positive contraction. It does not bound the raw precision block and therefore does not contradict PF-215/PF-224.
5. The trace criterion (16) is sufficient, not necessary. Its failure would not prove that `[D,\Omega]` or `P[D,\Omega]H` is outside weak trace class.
6. PF-223 is not contradicted: its adjacent blocks have finite but uncontrolled growing ranks/effective channel counts. PF-225 shows exactly why that growth is load-bearing.
7. PF-212's high-frequency Poisson estimate is not silently transferred to `B_j`. A new geometric estimate is still required for the one-pant normalized DtN crossing or directly for the dressed low/high flux.
8. Nothing here proves the full reciprocal-prime commutator is trace class, the physical remainder is weak trace class, PF-204's unsmoothed endpoint, PF-183's true-short-collar splice, wave-operator completeness, determinant/resonance control, prime/clone separation, or any RH implication.

## Consequences for the research line

PF-224 closes the raw-amplitude route; PF-225 shows what inversion gives back for free. The canonical smooth endpoint no longer needs to control the divergent norm of the normalized pant crossing. It needs to control **how many** one-pant singular channels remain significant after energy normalization and how the subcritical tail decays with physical seam frequency.

A decisive positive continuation should estimate `N_{B_j}(t)` for `0<t\le1/2` or, better, the corresponding low/high dressed counting function strongly enough to combine with the exact reciprocal-prime layers. A decisive negative continuation must exhibit PF-compatible growth of that saturated channel count; reproducing PF-224's one-channel raw norm divergence is insufficient. The unsmoothed PF-204 route and the independent PF-183 true-short-collar splice remain separate live alternatives.