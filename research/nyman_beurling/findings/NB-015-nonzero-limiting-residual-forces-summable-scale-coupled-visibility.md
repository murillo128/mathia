# NB-015 — nonzero limiting residual forces a summable scale-coupled visibility budget

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + SCALE-COUPLED-VISIBILITY-BUDGET + NESTED-SECTION-TELESCOPING + CONDITIONAL-RH-CLOSURE-CRITERION`. `NB-014` isolates the part of finite semigroup defect that is visible to actual section enrichment, but its first calibration is fixed-depth: any positive visibility fraction at arbitrarily large fixed probe depths would already force the limiting Nyman distance to zero. The genuinely open regime is diagonal, with the probe depth growing together with the section. Combining the exact enrichment identity of `NB-014` with the prime-normal-equation lower bound of `NB-011` gives a quantitative obstruction in precisely that regime.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\tag{1}
\]

and retain the Bagchi semigroup defects

\[
D_m=A_m^*-m^{-1/2}I,\qquad
\mathcal E_M(r_N)=\sum_{m=2}^{M}\|D_mr_N\|^2.
\tag{2}
\]

For section enrichment from `N` to `MN`, define

\[
\mathcal J_{N,M}
:=\sum_{m=2}^{M}\|P_ND_mr_N\|^2,
\qquad
F_{N,M}:=\sum_{m=2}^{M}A_mP_NA_m^*,
\tag{3}
\]

and the genuinely new section

\[
W_{N,M}:=V_{MN}\ominus V_N.
\tag{4}
\]

Put

\[
C_{N,M}:=P_{W_{N,M}}F_{N,M}P_{W_{N,M}},
\qquad
\beta_{N,M}:=\|C_{N,M}\|.
\tag{5}
\]

Whenever `\mathcal E_M(r_N)>0`, write

\[
\rho_{N,M}:=
\frac{\mathcal J_{N,M}}{\mathcal E_M(r_N)};
\tag{6}
\]

if the denominator vanishes, set `rho_(N,M)=0`.

Then two statements hold.

1. There are absolute constants `c_0,C_0>0` and an absolute depth threshold such that, if

\[
L:=\lfloor\sqrt{M-1}\rfloor\le N,
\qquad
d_N(\log M)^2\ge C_0,
\tag{7}
\]

and `M` is beyond that threshold, then

\[
\boxed{
\mathcal E_M(r_N)
\ge c_0 d_N^4\log M.
}
\tag{8}
\]

Thus a residual whose norm stays bounded away from zero cannot hide its finite semigroup defect along any growing diagonal with `sqrt(M)\lesssim N`: the actual projection normal equations force at least logarithmically growing defect energy at depth `M`.

2. Let

\[
N_{k+1}=M_kN_k,
\qquad M_k\to\infty,
\tag{9}
\]

be any nested multiplicative section path such that

\[
\lfloor\sqrt{M_k-1}\rfloor\le N_k
\tag{10}
\]

eventually. If

\[
d_\infty:=\lim_{N\to\infty}d_N>0,
\tag{11}
\]

then

\[
\boxed{
\sum_k
\frac{\rho_{N_k,M_k}\log M_k}
{\beta_{N_k,M_k}}
<\infty,
}
\tag{12}
\]

where a term with `beta_(N_k,M_k)=0` is interpreted as zero. Since always

\[
\beta_{N,M}\le M-1,
\tag{13}
\]

one also has the weaker but unconditional frame-budget consequence

\[
\boxed{
\sum_k
\frac{\rho_{N_k,M_k}\log M_k}
{M_k-1}
<\infty.
}
\tag{14}
\]

The contrapositive is an explicit closure criterion. If along one path satisfying (9)--(10) one can prove source-controlled bounds

\[
\rho_{N_k,M_k}\ge\eta_k,
\qquad
\beta_{N_k,M_k}\le b_k,
\tag{15}
\]

with

\[
\boxed{
\sum_k\frac{\eta_k\log M_k}{b_k}=\infty,
}
\tag{16}
\]

then necessarily `d_infinity=0`, and the Báez--Duarte discrete Nyman criterion yields RH.

This does **not** provide the missing visibility lower bound. Its contribution is to convert the accepted scale-coupled visibility question into a sharp accumulated budget: under any nonzero limiting residual, visible defect divided by the residual-relevant compressed frame cost must be summable after the natural `log M` weighting. In particular, positive visibility at isolated very rapidly growing scales can remain too sparse, whereas even a constant positive visibility fraction along moderately growing depths would be closure-strength.

## 1. The prime normal equations force `d_N^4 log M` defect on a growing diagonal

`NB-011` proves the exact finite inequality

\[
\mathcal E_K(r_N)
\ge
\frac{
\left[
 d_N^2S_L-d_N^2P_L/K-d_NP_L/\sqrt K
\right]_+^2
}{
H_{K-1}S_L+9P_L^2/(K-1)
},
\tag{17}
\]

whenever `2<=L<=N` and `K-1>=L^2`, where

\[
S_L=\sum_{p\le L}\frac{(\log p)^2}{p-1},
\qquad
P_L=\sum_{p\le L}\frac{p\log p}{p-1}.
\tag{18}
\]

The same finding records the standard prime-number-theorem asymptotics

\[
S_L=\left(\frac12+o(1)\right)(\log L)^2,
\qquad
P_L=(1+o(1))L.
\tag{19}
\]

Take

\[
K=M,
\qquad
L=\lfloor\sqrt{M-1}\rfloor.
\tag{20}
\]

Then the finite admissibility condition `K-1>=L^2` is automatic, and (7) supplies `L<=N`. As `M` grows,

\[
S_L\asymp(\log M)^2,
\qquad
P_L\asymp\sqrt M,
\qquad
H_{M-1}\asymp\log M.
\tag{21}
\]

The driving term in the numerator of (17) therefore has size

\[
d_N^2S_L\asymp d_N^2(\log M)^2,
\tag{22}
\]

while the two truncation errors have sizes

\[
\frac{d_N^2P_L}{M}=O\!\left(\frac{d_N^2}{\sqrt M}\right),
\qquad
\frac{d_NP_L}{\sqrt M}=O(d_N).
\tag{23}
\]

For sufficiently large `M`, the first error is negligible relative to (22). The second is at most a fixed fraction of (22) whenever

\[
d_N(\log M)^2\ge C_0
\tag{24}
\]

for a sufficiently large absolute `C_0`. Hence the positive part in (17) is bounded below by a fixed multiple of `d_N^2(log M)^2`.

The denominator satisfies

\[
H_{M-1}S_L+9P_L^2/(M-1)
\ll(\log M)^3+1
\ll(\log M)^3.
\tag{25}
\]

Substitution into (17) gives

\[
\mathcal E_M(r_N)
\gg
\frac{d_N^4(\log M)^4}{(\log M)^3}
=d_N^4\log M,
\]

which proves (8). The constants are absolute because all asymptotic comparisons in (19)--(25) can be frozen beyond one absolute threshold.

The condition (24) is important. Equation (8) is not claimed uniformly for arbitrarily tiny residuals at an independently fixed depth. Its intended role is the opposite regime: if the limiting distance is positive, then `d_N>=d_infinity`, so (24) becomes automatic along every sequence `M->infinity`.

## 2. The exact enrichment identity lives on the new quotient section

The dilation identity used in `NB-014` is

\[
A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m),
\tag{26}
\]

so `A_mV_N subset V_(mN)` and the range of `F_(N,M)` lies in `V_(MN)`. Define

\[
u_{N,M}:=P_{MN}r_N=r_N-r_{MN}.
\tag{27}
\]

Because `r_N` is orthogonal to `V_N` and `V_N subset V_(MN)`, one has

\[
u_{N,M}\in W_{N,M}.
\tag{28}
\]

Nested orthogonal projection gives

\[
\|u_{N,M}\|^2
=d_N^2-d_{MN}^2.
\tag{29}
\]

`NB-014` also gives the exact visible-defect identity

\[
\mathcal J_{N,M}
=\langle u_{N,M},F_{N,M}u_{N,M}\rangle.
\tag{30}
\]

Since `u_(N,M)` already lies in `W_(N,M)`, equations (5) and (30) imply the sharper compressed-frame inequality

\[
\boxed{
\mathcal J_{N,M}
\le
\beta_{N,M}
\left(d_N^2-d_{MN}^2\right).
}
\tag{31}
\]

This is the residual-relevant frame cost asked for in the accepted visibility clue. No estimate for `beta_(N,M)` beyond its generic upper bound is assumed here. Because `F_(N,M)` is the sum of `M-1` orthogonal projections,

\[
0\preceq F_{N,M}\preceq(M-1)I,
\]

and compression preserves the order, proving (13).

`NB-014` shows that the **full** frame norm is exactly `M-1` on a broad lcm-overlap regime. That does not determine `beta_(N,M)`: maximal common frame directions need not survive orthogonal compression to `V_(MN)\ominus V_N`. Equation (31) therefore isolates exactly the metric quantity on which any useful improvement over the crude `M-1` denominator must act.

## 3. A nonzero limiting residual has only a finite weighted visibility budget

Assume (11) and set

\[
\delta=d_\infty>0.
\tag{32}
\]

Since the section spaces are nested, `d_N` is nonincreasing and

\[
d_N\ge\delta
\qquad(N\ge2).
\tag{33}
\]

Along any path (9)--(10) with `M_k->infinity`, condition (24) therefore holds for all sufficiently large `k`. Equation (8) gives

\[
\mathcal E_{M_k}(r_{N_k})
\ge c_0\delta^4\log M_k.
\tag{34}
\]

For those `k`, the denominator in (6) is strictly positive. Combining (6), (31), and (34), whenever `beta_(N_k,M_k)>0`, yields

\[
\begin{aligned}
d_{N_k}^2-d_{N_{k+1}}^2
&\ge
\frac{\mathcal J_{N_k,M_k}}{\beta_{N_k,M_k}}\\
&=
\frac{\rho_{N_k,M_k}\mathcal E_{M_k}(r_{N_k})}
{\beta_{N_k,M_k}}\\
&\ge
c_0\delta^4
\frac{\rho_{N_k,M_k}\log M_k}
{\beta_{N_k,M_k}}.
\end{aligned}
\tag{35}
\]

If `beta_(N_k,M_k)=0`, positivity of the compression forces `J_(N_k,M_k)=0`, hence `rho_(N_k,M_k)=0`, so the corresponding weighted term is correctly interpreted as zero.

Now telescope (35). The left side sums to at most

\[
d_{N_0}^2-\delta^2<\infty.
\tag{36}
\]

Therefore

\[
\sum_k
\frac{\rho_{N_k,M_k}\log M_k}
{\beta_{N_k,M_k}}
\le
\frac{d_{N_0}^2-\delta^2}{c_0\delta^4}
+
O_{\delta,N_0}(1),
\tag{37}
\]

where the finite initial segment before (34) is absorbed into the last term. This proves (12). Equation (14) follows from `beta_(N,M)<=M-1`.

No density of the Nyman sections is used. In fact the argument assumes the opposite branch, `d_infinity>0`, and derives a necessary collapse of scale-coupled visibility. The conclusion is therefore a genuine falsification condition for any proposed visibility mechanism rather than a disguised invocation of the closure criterion.

## 4. Divergent visible enrichment is sufficient for closure

Suppose bounds (15) hold on a nested path. If `d_infinity>0`, equation (12) would imply

\[
\sum_k
\frac{\eta_k\log M_k}{b_k}
\le
\sum_k
\frac{\rho_{N_k,M_k}\log M_k}
{\beta_{N_k,M_k}}
<\infty,
\tag{38}
\]

contradicting (16). Hence `d_infinity=0`. The discrete Báez--Duarte criterion then gives RH.

The crude frame bound already illustrates the scale sensitivity. If, for example, a source theorem supplied

\[
\rho_{N_k,M_k}\ge\eta_0>0
\tag{39}
\]

along a path with `M_k` growing only linearly in `k`, then

\[
\sum_k\frac{\eta_0\log M_k}{M_k-1}=\infty,
\tag{40}
\]

so even the generic frame cost would suffice. By contrast, for exponentially sparse depths the corresponding series may converge; positivity of visibility at those isolated scales alone would not close the criterion through this telescoping budget.

This distinction is new compared with the fixed-depth calibration in `NB-014`. There, one positive `N`-uniform visibility constant at each of unboundedly many **fixed** depths is already closure-strength. Here the depth itself moves with the section, and the exact accumulation rate matters.

## 5. Relation to the earlier semigroup singularity and linear-ceiling results

`NB-007` proves that every fixed non-target vector has logarithmically divergent full harmonic semigroup defect. That does not by itself imply (8) on a diagonal sequence of changing residuals: the coefficient in its logarithmic lower bound can collapse with the vector, and `NB-006` exhibits scale-dependent aliases that defeat naive finite-depth uniformity. Equation (8) avoids that gap by using the **actual finite-section normal equations** through `NB-011`; under `d_infinity>0`, their target load stays uniformly nonzero and forces the diagonal `log M` growth.

`NB-012` and `NB-013` do not obstruct the present argument. They show that the prime ensemble already saturates lower-bound amplification within the linear normal-equation/harmonic-Cauchy architecture and its positive quadratic multichannel closure. Here that saturated lower bound is used as an input and transported through a different object: the target-aware section decrement. No attempt is made to amplify `E_M` further inside the closed channel class.

The remaining difficulty is therefore exposed rather than hidden. A successful RH-facing continuation must control at least one of the two quantities in (15) from the actual Nyman geometry: a lower bound on the visible fraction `rho`, an upper bound on the compressed frame cost `beta`, or a direct estimate of their ratio. Merely producing more finite normal-equation energy does not address that transport problem.

## 6. Prior-art boundary, falsification controls, and research consequence

The load-bearing external ingredients are already canonical in this line. Bagchi supplies the discrete dilation Hilbert-space model; Báez--Duarte supplies the discrete closure criterion; the prime number theorem enters only through the weighted prime asymptotics already used and recorded in `NB-011`. No new external theorem is required for (8) or the telescoping argument, so `SOURCES.md` does not change.

A targeted literature check covered Nyman--Beurling finite sections, nested/Galerkin projection geometry, dilation-semigroup formulations, recent multiscale Gram work, and the 2026 Friedrichs-angle formulation of Nyman--Beurling subspaces. The located multiscale work concerns Gram-entry decay and block compressibility, while the Friedrichs-angle paper studies an angle between Nyman--Beurling subspaces and its relation to RH. No located source supplied the residual-specific prime-normal-equation diagonal bound (8), the compressed enrichment quantity (5), or the weighted nested visibility budget (12). Search absence is not a novelty proof; the claim here is the derivation from the canonical Mathia finite-section identities and the explicitly stated literature inputs.

Several boundaries are essential.

- Equation (8) is **residual-specific**. It uses the exact Nyman projection normal equations through `NB-011` and does not hold for arbitrary unit vectors or the Mellin aliases used as earlier controls.
- The diagonal restriction `floor(sqrt(M-1))<=N` is load-bearing because the prime equations up to that depth must already belong to the old section. The exact inequality (17) remains available outside the simplified asymptotic corridor, but (8) is not asserted there.
- Condition `d_N(log M)^2>=C_0` cannot be deleted. It is automatic under the nonzero-limit hypothesis for growing `M`, but not in a regime where the residual itself shrinks rapidly.
- No lower bound for `rho_(N,M)` is proved. The visible defect may collapse, and under a false-RH branch (12) says that sufficient collapse is mandatory.
- No improved bound for `beta_(N,M)` is proved. `NB-014` already warns that the full frame is maximally overlapped on a broad lcm regime, even though the compressed quotient may behave differently.
- The divergence condition (16) is a **sufficient RH criterion**, not an established property of the Nyman residuals and not a new unconditional approximation rate. There is no converse: convergence of the weighted visibility series does not imply failure of RH.

The durable frontier is now a quantitative one. The accepted visible-defect clue need not seek an `N`-uniform positive fraction at every fixed depth, which `NB-014` showed is already too strong. It can instead target one nested growing-scale family and ask whether the actual source geometry supplies enough accumulated visible enrichment to violate the finite budget (12). Any candidate estimate can be judged immediately by the series (16), with the compressed frame cost and scale sparsity paid explicitly.