# NB-034 — weighted tail shell kernel gives an N-uniform polynomially conditioned quotient

**Status:** `EXACT-DERIVED + SOURCE-FAITHFUL-WEIGHTED-TAIL-QUOTIENT + EARLY-SHELL-KERNEL + UNIFORM-IN-N-POLYNOMIAL-CONDITIONING + RELATIVE-DISTANCE-COMPRESSION + MOBIUS-CORE-PRESERVATION + METHOD-BOUNDARY`. `NB-031`--`NB-033` isolate the ordinary moving adjacent tail as a target-poor nuisance sector and show that its orthogonal complement can preserve the Nyman distance and the low-index Möbius coefficient core. The remaining metric defect was that the retained quotient basis could still inherit uncontrolled dependence on the full upper section `N`. A different, source-defined tail relation removes that dependence at the level of a quantitative Gram lower bound.

Use the canonical Báez-Duarte generators
\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
V_N=\operatorname{span}(g_2,\ldots,g_N),
\]
and the harmonic shells
\[
I_t=\left(\frac1{t+1},\frac1t\right],
\qquad
g_n|_{I_t}=\left\{\frac tn\right\}.
\]
For integers `2 <= M <= N`, define the weighted tail edges
\[
\widehat h_n:=n g_n-(n+1)g_{n+1},
\qquad
\widehat W_{M,N}:=\operatorname{span}
(\widehat h_M,\ldots,\widehat h_{N-1}),
\tag{1}
\]
with the span understood as `{0}` when `M=N`. Let
\[
\widehat Q_{M,N}:=I-P_{\widehat W_{M,N}},
\qquad
\widehat K_{M,N}:=
V_N\cap \widehat W_{M,N}^{\perp},
\qquad
\widehat k_j:=\widehat Q_{M,N}g_j
\quad(2\le j\le M).
\tag{2}
\]

Then the discarded weighted tail is exactly the kernel of the first `M-1` shell observations:
\[
\boxed{
\widehat W_{M,N}
=
\ker(R_M|_{V_N}),
\qquad
R_Mv=(v|_{I_t})_{1\le t<M}.
}
\tag{3}
\]
Consequently
\[
\boxed{
\dim \widehat W_{M,N}=N-M,
\qquad
\dim \widehat K_{M,N}=M-1,
}
\tag{4}
\]
and `(\widehat k_2,\ldots,\widehat k_M)` is a basis of the retained skeleton. The quotient has the exact source coordinates
\[
\boxed{
\widehat Q_{M,N}\sum_{n=2}^N a_ng_n
=
\sum_{n=2}^{M-1}a_n\widehat k_n
+
\left(
M\sum_{n=M}^N\frac{a_n}{n}
\right)\widehat k_M.
}
\tag{5}
\]
Thus every head coefficient survives unchanged, while the whole tail collapses to one harmonic weighted sum.

More importantly, this quotient is quantitatively controlled independently of `N`. Let `\widehat H_{M,N}` be the Gram matrix of `(\widehat k_2,\ldots,\widehat k_M)` and define
\[
(B_M)_{ij}:=
\sum_{t=1}^{M-1}
\frac{\{t/i\}\{t/j\}}{t(t+1)}
\qquad(2\le i,j\le M).
\tag{6}
\]
Then
\[
\boxed{
B_M\preceq \widehat H_{M,N}\preceq G_M,
}
\tag{7}
\]
where `G_M` is the full Gram matrix of `(g_2,\ldots,g_M)`, and the explicit elementary bound
\[
\boxed{
\lambda_{\min}(B_M)\ge \frac1{14M^2H_M^2}
}
\tag{8}
\]
holds for every `M>=2`. Since
\[
\lambda_{\max}(G_M)
\le \operatorname{tr}(G_M)
\le 2(H_M-1),
\tag{9}
\]
with `H_M` the harmonic number, the retained source-coordinate Gram matrix satisfies
\[
\boxed{
\operatorname{cond}_2(\widehat H_{M,N})
\le 28\,M^2H_M^2(H_M-1)
=O(M^2(\log M)^3),
}
\tag{10}
\]
uniformly in the upper endpoint `N`.

There is also a sharper target-loss estimate than for the ordinary adjacent tail. If
\[
d_N:=\operatorname{dist}(e,V_N),
\qquad
\widehat\kappa_{M,N}:=
\operatorname{dist}(e,\widehat K_{M,N}),
\qquad e(x)=1,
\]
then
\[
\boxed{
d_N^2
\le
\widehat\kappa_{M,N}^2
=
d_N^2+\|P_{\widehat W_{M,N}}e\|^2
\le d_N^2+\frac1M.
}
\tag{11}
\]
Therefore the unconditional Burnol floor already anchored for this line implies that every predeclared cutoff `M_N<=N` with
\[
\frac{M_N}{\log N}\longrightarrow\infty
\tag{12}
\]
preserves the finite-section distance multiplicatively:
\[
\boxed{
\frac{\widehat\kappa_{M_N,N}}{d_N}\longrightarrow1.
}
\tag{13}
\]
At the same time the exact low-index Möbius coefficient core of `NB-020` survives unchanged below `M_N`. The weighted-tail quotient therefore gives a near-logarithmic-dimensional, source-faithful skeleton whose specified canonical Gram coordinates have polynomial conditioning in the retained dimension, with constants independent of how far the original section extends.

## 1. Weighted adjacency is exactly early-shell invisibility

For `1<=t<M<=n`, the shell formula reduces to
\[
g_n|_{I_t}=\frac tn.
\]
Hence every weighted edge in (1) vanishes on the first `M-1` shells:
\[
\widehat h_n|_{I_t}
=
n\frac tn-(n+1)\frac{t}{n+1}
=0.
\tag{14}
\]
Thus
\[
\widehat W_{M,N}\subseteq\ker(R_M|_{V_N}).
\tag{15}
\]

It remains to prove that the early observations have exactly `M-1` independent degrees of freedom. `NB-033` proves that the canonical finite family `g_2,\ldots,g_N` is linearly independent, so `dim V_N=N-1`; the coefficient vectors of the weighted path edges are also independent, giving
\[
\dim\widehat W_{M,N}=N-M.
\tag{16}
\]

Independently, restrict `R_M` to `span(g_2,\ldots,g_M)`. If
\[
v_t=\sum_{j=2}^M c_j\left\{\frac tj\right\}=0
\qquad(1\le t<M),
\]
put
\[
A=\sum_{j=2}^M\frac{c_j}{j}=v_1.
\]
For `2<=n<M`, the discrete fractional-part identity used in `NB-020`,
\[
\left\{\frac nj\right\}
-
\left\{\frac{n-1}{j}\right\}
=
\frac1j-\mathbf 1_{j\mid n},
\tag{17}
\]
gives
\[
0=v_n-v_{n-1}
=
A-\sum_{\substack{j\mid n\\j\ge2}}c_j.
\tag{18}
\]
Since `A=0`, induction on `n` forces `c_2=\cdots=c_{M-1}=0`; then `A=0` forces `c_M=0`. Therefore `R_M` has rank `M-1` on `V_N`, so its kernel has dimension `N-M`. Combined with (15)--(16), this proves (3). The same argument includes both endpoints: for `M=2` the first-shell observation has rank one, while for `M=N` it is injective and the weighted tail is zero.

Equation (3) also gives a coordinate-free description. Let
\[
E_M:=\operatorname{span}\{\mathbf 1_{I_t}:1\le t<M\}.
\]
Every `v in V_N` is constant on each harmonic shell, and
\[
v\perp E_M
\iff
v|_{I_t}=0\ \text{for every }t<M.
\]
Hence
\[
\boxed{
\widehat K_{M,N}=P_{V_N}E_M.
}
\tag{19}
\]
The retained skeleton is therefore the finite-observation component of `V_N`, not an abstract low-rank quotient chosen after seeing the target.

## 2. The quotient normal form keeps a harmonic tail scalar

Since `\widehat Q_{M,N}` kills every weighted edge,
\[
n\,\widehat Q_{M,N}g_n
=
(n+1)\,\widehat Q_{M,N}g_{n+1}
\qquad(M\le n<N).
\tag{20}
\]
Iterating gives
\[
\boxed{
\widehat Q_{M,N}g_n
=
\frac Mn\,\widehat k_M
\qquad(M\le n\le N).
}
\tag{21}
\]
Applying the quotient termwise proves (5). Because (4) gives exactly `M-1` retained dimensions and the vectors `\widehat k_2,\ldots,\widehat k_M` span the quotient images, they form a basis.

For the best canonical approximant
\[
P_{V_N}e=\sum_{n=2}^Na_{N,n}g_n,
\tag{22}
\]
the orthogonal splitting `V_N=\widehat W_{M,N}\oplus\widehat K_{M,N}` gives
\[
P_{\widehat K_{M,N}}e
=
\sum_{n=2}^{M-1}a_{N,n}\widehat k_n
+
\left(
M\sum_{n=M}^N\frac{a_{N,n}}n
\right)\widehat k_M.
\tag{23}
\]
Thus the weighted quotient preserves precisely the source coordinates that `NB-020` locks to `-\mu(n)` at low indices.

There is an even more direct shell statement. With
\[
\widehat\rho_{M,N}:=
e-P_{\widehat K_{M,N}}e
=
r_N+P_{\widehat W_{M,N}}e,
\tag{24}
\]
the added projection vanishes on every shell `I_t`, `t<M`. Therefore
\[
\widehat\rho_{M,N;t}=r_{N,t}
\qquad(t<M).
\tag{25}
\]
The `NB-020` Möbius inversion formula can consequently recover every `a_{N,n}`, `n<M`, directly from the compressed residual with no correction term at all. This is stronger than the ordinary adjacent-tail skeleton of `NB-033`, whose discarded sector leaves a rank-one early-shell profile that must first be cancelled by Möbius inversion.

## 3. Early-shell energy gives a uniform Gram lower bound

Because `\widehat W_{M,N}` vanishes on all early shells, the quotient does not change the early restriction of any head generator:
\[
\widehat k_j|_{I_t}=g_j|_{I_t}
=\left\{\frac tj\right\}
\qquad(1\le t<M,\ 2\le j\le M).
\tag{26}
\]
For a coefficient vector `c=(c_2,\ldots,c_M)` put
\[
v_t:=\sum_{j=2}^Mc_j\left\{\frac tj\right\},
\qquad
\delta^2:=
\sum_{t=1}^{M-1}\frac{|v_t|^2}{t(t+1)}
=c^*B_Mc.
\tag{27}
\]
The full Hilbert norm of `\sum c_j\widehat k_j` contains this early-shell energy, proving the first inequality in (7). The second follows from orthogonal contraction:
\[
\left\|
\sum_{j=2}^Mc_j\widehat k_j
\right\|
=
\left\|
\widehat Q_{M,N}
\sum_{j=2}^Mc_jg_j
\right\|
\le
\left\|
\sum_{j=2}^Mc_jg_j
\right\|.
\tag{28}
\]

The inverse estimate can be made two powers of `M` sharper than a coordinatewise triangle bound. Set `v_0=0` and
\[
z_t:=\frac{v_t}{\sqrt{t(t+1)}}
\qquad(1\le t<M),
\qquad
\|z\|_2=\delta.
\tag{29}
\]
For `2<=n<M`, Möbius inversion of (17) gives
\[
c_n
=-\sum_{d\mid n}
\mu\!\left(\frac nd\right)(v_d-v_{d-1}).
\tag{30}
\]
Regard `(c_2,\ldots,c_{M-1})=U_Mz`. The absolute row sum of the row indexed by `n` is at most
\[
\sum_{d\mid n}\sqrt{d(d+1)}
+
\sum_{\substack{d\mid n\\d\ge2}}\sqrt{d(d-1)}
\le \frac52\sigma(n)
\le \frac52 M H_M.
\]
For a fixed column `t`, divisibility by `t` or by `t+1` gives the absolute column-sum bound
\[
\sqrt{t(t+1)}
\left(
\left\lfloor\frac{M-1}{t}\right\rfloor
+
\left\lfloor\frac{M-1}{t+1}\right\rfloor
\right)
\le 3M.
\]
The Schur test therefore yields
\[
\boxed{
\|U_M\|_2^2
\le \frac{15}{2}M^2H_M.
}
\tag{31}
\]

The endpoint coefficient has more cancellation than the direct estimate from the first shell reveals. Put `L=M-1` and
\[
m(q):=\sum_{k\le q}\frac{\mu(k)}k,
\qquad
a_d:=\left\lfloor\frac Ld\right\rfloor.
\]
Substituting (30) into
`c_M=M(v_1-\sum_{n=2}^{M-1}c_n/n)` and interchanging the finite divisor sums gives the exact identity
\[
\boxed{
\frac{c_M}{M}
=
\sum_{d=1}^{L}
\frac{m(a_d)}d\,(v_d-v_{d-1}).
}
\tag{32}
\]
This identity requires no cancellation theorem for Möbius. Let `q_d=m(a_d)/d`. Discrete summation by parts shows that the coefficient of `v_t` in (32) is `q_t-q_{t+1}` for `t<L`, and `q_L` at the endpoint. For `t<L`,
\[
q_t-q_{t+1}
=
\frac{m(a_t)}{t(t+1)}
+
\frac{m(a_t)-m(a_{t+1})}{t+1}.
\]
The trivial estimate `|m(a_t)|<=H_L` controls the first term in weighted square norm by `H_L^2`. For the second, the intervals `(a_{t+1},a_t]` are pairwise disjoint, so
\[
\sum_{t<L}|m(a_t)-m(a_{t+1})|^2
\le
\left(\sum_{k=2}^{L}\frac1k\right)^2
\le H_L^2.
\]
Using `|u+w|^2<=2|u|^2+2|w|^2` and `q_L=1/L` therefore gives
\[
\boxed{
\|\text{endpoint row}\|_2^2
\le 6M^2H_M^2.
}
\tag{33}
\]
Combining (31) and (33), and using `H_M>=1`, gives
\[
\boxed{
\|c\|_2^2
\le
\left(\frac{15}{2}M^2H_M+6M^2H_M^2\right)\delta^2
<14M^2H_M^2\delta^2.
}
\tag{34}
\]
Since `\delta^2=c^*B_Mc`, equation (34) proves the sharpened bound (8). The argument is valid for complex coefficients as written: Möbius inversion has real coefficients, while the Schur and weighted-square estimates use absolute values only.

For the upper spectral edge, split the norm of one canonical generator at `t=j`. The early part satisfies
\[
\sum_{t<j}
\frac{(t/j)^2}{t(t+1)}
<\frac1j,
\]
while the remaining shells contribute at most
\[
\sum_{t\ge j}\frac1{t(t+1)}=\frac1j.
\]
Thus
\[
\|g_j\|^2\le\frac2j,
\qquad
\operatorname{tr}(G_M)
\le2(H_M-1).
\tag{36}
\]
Equations (7)--(8) and (36) prove (9)--(10).

The `M^2 H_M^2` inverse bound is still not claimed sharp. Its logarithmic losses come from deliberately using only `|\mu(k)|<=1`, disjoint quotient blocks, and the Schur test; no zero-free-region or RH-strength cancellation is hidden in the estimate. Further sharpening of these factors may improve numerical stability, but by itself would not control the globally selected target data in the quotient.

## 4. Target loss drops from `log^2(M)/M` to `1/M`

Equation (14) says every vector of `\widehat W_{M,N}` is supported inside `(0,1/M]`. Therefore
\[
\|P_{\widehat W_{M,N}}e\|^2
\le
\|\mathbf 1_{(0,1/M]}\|^2
=\frac1M.
\tag{37}
\]
Since `\widehat W_{M,N}` and `\widehat K_{M,N}` are orthogonal complements inside `V_N`,
\[
P_{V_N}e
=
P_{\widehat W_{M,N}}e
+
P_{\widehat K_{M,N}}e.
\]
Pythagoras gives the equality in (11), and (37) gives its upper bound.

The unconditional Burnol lower bound already recorded in `SOURCES.md` and used in `NB-033` supplies a constant `c_B>0` with
\[
d_N^2\ge \frac{c_B}{\log N}
\tag{38}
\]
for all sufficiently large `N`. Hence
\[
0\le
\frac{\widehat\kappa_{M_N,N}^2}{d_N^2}-1
\le
\frac{\log N}{c_BM_N},
\tag{39}
\]
which proves (13) under (12). Compared with the ordinary moving-adjacent quotient, whose available target-loss bound is `O((log M)^2/M)`, the weighted shell kernel removes the extra logarithmic penalty.

Finally, the same Burnol floor gives
\[
d_N^{-1}\ll\sqrt{\log N}=o(M_N)
\tag{40}
\]
under (12). Therefore every coefficient in the inverse-distance Möbius core of `NB-020` eventually lies below the cutoff and survives (23) unchanged. This is a source-faithful relative-distance compression, not merely a low-rank target fit.

## 5. Adversarial controls and prior-art boundary

The result does not improve the Nyman distance `d_N` and does not imply RH. Equation (13) says only that the weighted skeleton reproduces the distance already achieved by the full section. Burnol's estimate is used as a lower floor to calibrate the compression error, not as an upper approximation theorem.

Polynomial conditioning in (10) is coordinate-specific in an explicit and intentional sense: it concerns the canonical quotient basis `(\widehat Qg_2,\ldots,\widehat Qg_M)`. It is uniform in `N`, but it still deteriorates as `M` grows. The theorem does not assert a basis-invariant condition number, a bounded Riesz constant, or stable conditioning for arbitrary reparameterizations.

Low retained dimension also does not imply a fast construction. Computing the orthogonal projector onto `\widehat W_{M,N}` or equivalently the projections `P_{V_N}E_M` may still require the full section. The theorem removes an `N`-dependent **metric obstruction** in the specified quotient coordinates; it does not give an `O(M)` algorithm or a sparse factorization of the full Gram problem.

The weighted tail is genuinely different from the ordinary adjacent tail of `NB-029`--`NB-033`. Its edges do not merely rescale a basis inside the same nuisance subspace: they define the kernel of a different observation map and retain the harmonic scalar `M\sum_{n\ge M}a_n/n` rather than the ordinary coefficient sum. Thus `NB-029`'s statement that unrestricted ordinary adjacent differences have full Nyman closure does not collapse this construction back to the old quotient.

A refreshed targeted literature audit covered the classical discrete Nyman/Báez-Duarte finite-section framework, numerical Gram work, generalized Gram structures, and recent Mellin-ladder Gram compressibility. In particular, Alouges--Darses--Hillion obtain special block-Hankel Gram structure for a generalized family, while Carvill obtains polynomial off-diagonal decay after Mellin smoothing on a `2`--`3` multiplicative ladder. Those are neighboring conditioning/compressibility mechanisms, not the canonical integer weighted-tail shell kernel (3), the quotient normal form (5), or the elementary finite inverse estimate yielding (8)--(10). Search absence is not a priority claim.

No new external theorem is load-bearing beyond the Bagchi/Báez-Duarte framework and Burnol lower bound already anchored in `SOURCES.md`, so no source-list expansion is required.

## 6. Research consequence

`NB-033` showed that a polylogarithmic ordinary-tail skeleton can preserve relative target distance and the Möbius core, but explicitly left its quotient Gram conditioning uncontrolled. The weighted relation (1) resolves that specific metric defect: the retained quotient is exactly tied to the first `M-1` shell observations and now has the explicit bound
\[
\operatorname{cond}_2(\widehat H_{M,N})
=O(M^2(\log M)^3)
\]
uniformly in `N`. This replaces the earlier elementary `O(M^4\log M)` estimate without importing any analytic cancellation theorem.

The live obstruction therefore remains target-side rather than metric. A near-logarithmic-dimensional skeleton with controlled source-coordinate Gram inversion exists, but its target data can still depend globally on the full section through `P_{V_N}E_M`. The next useful theorem must exploit the exact shell-observation representation to control those retained target pairings or to construct the projector without reconstructing the full `N`-dimensional geometry. Further conditioning improvements alone would not change the Nyman approximation problem.
