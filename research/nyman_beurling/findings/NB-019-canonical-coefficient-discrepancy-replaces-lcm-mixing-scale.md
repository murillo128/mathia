# NB-019 — canonical coefficient discrepancy replaces the lcm scale in deep-dilation mixing

**Status:** `EXACT-DERIVED + TARGET-AWARE-COEFFICIENT-CERTIFICATE + PREPERIOD-DILATION-MIXING + EFFECTIVE-VISIBILITY-ASYMPTOTICS + METHOD-BOUNDARY`. `NB-018` identifies the fixed-section deep-dilation limit of the canonical Nyman residual: after compression, `Q_m r_N := sqrt(m) A_m^* r_N` converges to the arithmetic shell mean `mu_N e`. Its direct periodic proof pays the full shell period `Lambda_N=lcm(2,...,N)`, so by itself it only becomes quantitative at an exponential scale. For the **actual finite Nyman residual**, that lcm cost is not intrinsic. The residual is a canonical linear combination of generators whose individual periods are at most `N`; resolving those periods before taking the linear combination yields a much smaller, target-aware mixing scale controlled by the finite projection coefficients.

Write

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\tag{1}
\]

and, using linear independence of the canonical generators, write the projection uniquely as

\[
P_Ne=\sum_{j=2}^N a_{N,j}g_j.
\tag{2}
\]

In Bagchi's harmonic-shell realization,

\[
g_j|_{I_n}=\left\{\frac nj\right\},
\qquad I_n=\left(\frac1{n+1},\frac1n\right].
\tag{3}
\]

The arithmetic shell mean of one generator is

\[
\overline g_j=\frac{j-1}{2j},
\tag{4}
\]

so the mean introduced in `NB-018` has the finite target-aware formula

\[
\boxed{
\mu_N=1-\sum_{j=2}^N a_{N,j}\frac{j-1}{2j}.
}
\tag{5}
\]

Define the canonical coefficient-discrepancy budget

\[
\boxed{
\mathfrak A_N:=\sum_{j=2}^N j\,|a_{N,j}|.
}
\tag{6}
\]

Then for **every** `N>=2` and every integer `m>=2`, one has the effective preperiod mixing estimate

\[
\boxed{
\|Q_mr_N-\mu_Ne\|_{L^\infty(0,1)}
\le \frac{\mathfrak A_N}{4m}.
}
\tag{7}
\]

In particular the same inequality holds in `L^2`. Thus the elementary convergence mechanism of `NB-018` does not intrinsically require `m` to resolve `lcm(2,...,N)`: it already becomes effective once `m` dominates the weighted size of the **actual projection coefficients**. The price is real and source-sensitive. No useful bound for `mathfrak A_N` is asserted here.

The estimate makes the deep full-defect and visible-defect laws effective as well. Put

\[
\mathcal C_N
:=\|\mu_Ne-r_N\|
=\sqrt{\mu_N^2(1-d_N^2)+(1-\mu_N)^2d_N^2},
\tag{8}
\]

and

\[
\mathcal B_N
:=\|\mu_NP_Ne\|
=|\mu_N|\sqrt{1-d_N^2}.
\tag{9}
\]

For every `m>=2`,

\[
\boxed{
\left|\sqrt m\,\|D_mr_N\|-\mathcal C_N\right|
\le\frac{\mathfrak A_N}{4m},
}
\tag{10}
\]

\[
\boxed{
\left|\sqrt m\,\|P_ND_mr_N\|-\mathcal B_N\right|
\le\frac{\mathfrak A_N}{4m}.
}
\tag{11}
\]

Consequently, for any integers `2<=K<=M`,

\[
\boxed{
\left|
\sum_{m=K}^M\|D_mr_N\|^2
-\mathcal C_N^2(H_M-H_{K-1})
\right|
\le
\frac{\mathfrak A_N\mathcal C_N}{2(K-1)}
+\frac{\mathfrak A_N^2}{32(K-1)^2},
}
\tag{12}
\]

and

\[
\boxed{
\left|
\sum_{m=K}^M\|P_ND_mr_N\|^2
-\mathcal B_N^2(H_M-H_{K-1})
\right|
\le
\frac{\mathfrak A_N\mathcal B_N}{2(K-1)}
+\frac{\mathfrak A_N^2}{32(K-1)^2}.
}
\tag{13}
\]

These are finite inequalities, not merely fixed-`N` asymptotics. In the special case `mu_N=0`, (13) gives the explicit all-depth tail bound

\[
\boxed{
\sum_{m=K}^{\infty}\|P_ND_mr_N\|^2
\le\frac{\mathfrak A_N^2}{32(K-1)^2}.
}
\tag{14}
\]

Thus the two branches already visible qualitatively in `NB-018` have an effective source scale: nonzero `mu_N` creates a harmonic visible tail once the coefficient-discrepancy error is small relative to `mathcal B_N`, while `mu_N=0` forces the deep visible tail to decay quadratically beyond the coefficient budget.

There is also a direct consequence for the future residual field of `NB-017`. Let

\[
q_k=\langle r_N,g_k\rangle,
\qquad s_k=kq_k.
\tag{15}
\]

For every `2<=j<=N` and `m>=2`, the exact dilation identity gives

\[
\langle Q_mr_N,g_j\rangle
=\frac{s_{mj}-s_m}{j}.
\tag{16}
\]

Since `\langle e,g_j\rangle=\log j/j`, (7) implies

\[
\boxed{
|s_{mj}-s_m-\mu_N\log j|
\le
\frac{j\,\|g_j\|_2\,\mathfrak A_N}{4m}
\le\frac{j\mathfrak A_N}{4m}.
}
\tag{17}
\]

So `NB-017`'s reciprocal blind fields do not need the full lcm period to acquire the logarithmic cocycle found in `NB-018`: the transition is already quantitatively controlled by `mathfrak A_N/m`. This does **not** prove that the transition occurs inside the `NB-015` diagonal corridor; that is now an explicit coefficient-growth question.

## 1. The correct intrinsic quantity is consecutive shell discrepancy

The period estimate in `NB-018` can be sharpened before using any Nyman-specific structure. For a real periodic shell sequence `h=(h_n)` with arithmetic mean `mu(h)`, define its consecutive discrepancy

\[
\Delta(h)
:=\sup_{A\le B}
\left|\sum_{n=A}^B(h_n-\mu(h))\right|.
\tag{18}
\]

Full periods have zero centered sum, so `Delta(h)` is finite and can be computed inside one period. The compressed adjoint formula reconstructed in `NB-018` is

\[
(Q_mh)|_{I_n}
=mn(n+1)
\sum_{\ell=mn}^{m(n+1)-1}
\frac{h_\ell}{\ell(\ell+1)}.
\tag{19}
\]

The weights

\[
\omega_\ell
=\frac{mn(n+1)}{\ell(\ell+1)}
\tag{20}
\]

are positive, decreasing, sum to one, and satisfy

\[
\omega_{mn}=\frac{n+1}{mn+1}\le\frac2m.
\tag{21}
\]

Apply Abel summation to the centered values `u_l=h_l-mu(h)` over the block in (19). If

\[
U_t=\sum_{\ell=mn}^t u_\ell,
\]

then `|U_t|<=Delta(h)` and

\[
\sum_{\ell=mn}^{m(n+1)-1}\omega_\ell u_\ell
=
\omega_bU_b+
\sum_{\ell=mn}^{b-1}(\omega_\ell-\omega_{\ell+1})U_\ell,
\qquad b=m(n+1)-1.
\tag{22}
\]

Monotonicity of the weights makes the total coefficient on the right exactly `omega_(mn)`. Therefore

\[
\boxed{
\|Q_mh-\mu(h)e\|_\infty
\le\frac{2\Delta(h)}m.
}
\tag{23}
\]

The bound of `NB-018`, which used period times sup norm, follows from the generic estimate `Delta(h)<=P||h-mu(h)e||_infty` for a period `P`. Equation (23) shows that the period itself was only a sufficient way to control discrepancy, not the intrinsic mixing scale.

## 2. Each canonical generator has only linear, explicitly computable discrepancy

For the shell sequence in (3), center one period by

\[
u_j(n)=\left\{\frac nj\right\}-\frac{j-1}{2j}.
\tag{24}
\]

For `0<=t<=j-1`, its prefix sum over `n=1,...,t` is

\[
S_j(t)
=\frac{t(t-j+2)}{2j},
\tag{25}
\]

while `S_j(j)=0`. Since a zero-mean periodic sequence has consecutive discrepancy equal to the range of its prefix sums over one period,

\[
\Delta(g_j)
=\max_{0\le t\le j}S_j(t)-
\min_{0\le t\le j}S_j(t).
\tag{26}
\]

The maximum is `(j-1)/(2j)` and the minimum is

\[
-\frac{1}{2j}
\left\lfloor\frac{(j-2)^2}{4}\right\rfloor.
\]

Hence

\[
\boxed{
\Delta(g_j)=
\begin{cases}
 j/8,&j\text{ even},\\[2mm]
 (j^2-1)/(8j),&j\text{ odd},
\end{cases}
\le\frac j8.
}
\tag{27}
\]

Now (2), (4), and (5) give the centered residual identity

\[
r_N-\mu_Ne
=-\sum_{j=2}^N a_{N,j}(g_j-\overline g_je).
\tag{28}
\]

Consecutive discrepancy is subadditive, so (27) yields

\[
\boxed{
\Delta(r_N)
\le\sum_{j=2}^N|a_{N,j}|\Delta(g_j)
\le\frac{\mathfrak A_N}{8}.
}
\tag{29}
\]

Combining (23) and (29) proves (7).

This is where the exponential lcm disappears. Taking the period of the sum first treats all possible lcm-scale frequencies as if they were independently present. Equation (29) instead keeps the canonical generator decomposition and pays the discrepancy of each actual period before summing. The price is the weighted absolute coefficient budget `mathfrak A_N`, which can itself be large; no cancellation between different generators is used in (29).

## 3. The budget is finite target-aware Gram data, not a new free parameter

The coefficient vector in (2) is determined by exactly the target-aware finite data emphasized by `NB-001`. In the real Bagchi normalization let

\[
G_N=(\langle g_j,g_k\rangle)_{2\le j,k\le N},
\qquad
b_N=\left(\frac{\log j}{j}\right)_{2\le j\le N}.
\tag{30}
\]

The canonical generators are independent, so

\[
\boxed{
a_N=G_N^{-1}b_N.}
\tag{31}
\]

Therefore `mathfrak A_N` is an explicit statistic of the same finite target-aware certificate, not an externally chosen regularizer. A crude conditioning bound is

\[
\boxed{
\mathfrak A_N
\le
\left(\sum_{j=2}^N j^2\right)^{1/2}
\sqrt{\frac{1-d_N^2}{\lambda_{\min}(G_N)}}.
}
\tag{32}
\]

Indeed `a_N^*G_Na_N=||P_Ne||^2=1-d_N^2`, so `||a_N||_2<=sqrt((1-d_N^2)/lambda_min(G_N))`, and Cauchy--Schwarz gives (32).

Equation (32) is only a diagnostic. It may be much too weak, and replacing `mathfrak A_N` by a poor condition-number estimate can destroy the gain over the lcm bound. The useful question is the actual target-selected weighted coefficient growth, or still better the intrinsic discrepancy `Delta(r_N)`, which may exhibit cancellation invisible to the absolute coefficient majorant (29).

## 4. Effective full and visible defect laws

From the definition of `D_m=A_m^*-m^{-1/2}I`,

\[
\sqrt m\,D_mr_N=Q_mr_N-r_N.
\tag{33}
\]

Equation (7) shows that the right side differs from `mu_Ne-r_N` by at most `mathfrak A_N/(4m)` in `L^2`. The reverse triangle inequality proves (10).

Because `P_Nr_N=0`,

\[
\sqrt m\,P_ND_mr_N=P_NQ_mr_N.
\tag{34}
\]

Projection is contractive, so (7) shows that the right side differs from `mu_NP_Ne` by at most the same amount. This proves (11).

If nonnegative numbers `x,c` satisfy `|x-c|<=epsilon`, then

\[
|x^2-c^2|\le\epsilon(2c+\epsilon).
\tag{35}
\]

Apply (35) to (10)--(11), divide by `m`, and use

\[
\sum_{m=K}^{\infty}\frac1{m^2}\le\frac1{K-1},
\qquad
\sum_{m=K}^{\infty}\frac1{m^3}\le\frac1{2(K-1)^2}.
\tag{36}
\]

This gives (12)--(13). When `mu_N=0`, `mathcal B_N=0`; let `M` tend to infinity in (13) to obtain (14).

The same argument also quantifies the cocycle in (17). From the exact dilation law

\[
A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m)
\tag{37}
\]

one gets (16). Pairing the error in (7) with `g_j`, then using `||g_j||_2<=1`, proves (17).

## 5. Consequence for the live scale-coupled problem

`NB-018` correctly identifies `mu_N` as the scalar governing the fixed-section endpoint and correctly warns that its direct period estimate is exponentially late. `NB-019` sharpens the **quantitative mechanism**, not the fixed-section limit: the canonical residual can enter that endpoint regime much earlier whenever its target-selected coefficient discrepancy is controlled.

For example, along any sequence of section/probe scales with

\[
\frac{\mathfrak A_N}{M_N}\longrightarrow0,
\tag{38}
\]

one has uniformly for `m` comparable with `M_N`,

\[
Q_mr_N-\mu_Ne\longrightarrow0
\quad\text{in }L^\infty.
\tag{39}
\]

Thus if `M_N<=N^2`, a subquadratic bound `mathfrak A_N=o(N^2)` would already place the top part of the `NB-015` admissible diagonal inside the mixing regime, without resolving `Lambda_N`. This is only a reduction: no such coefficient estimate is proved here.

Even (38) would not settle the visibility budget. Two independent losses remain. First, `mu_N` may be small or zero; equations (11), (13), and (14) show that in that branch deep semigroup defect can remain almost entirely invisible to the old section. Second, `NB-016`--`NB-017` show that the compressed enrichment frame has exact multiplicative blind directions, so visible energy still has to be compared with the quotient frame cost in the `NB-015` telescoping criterion.

The new boundary is therefore sharper than “the lcm period is too large.” The actionable source questions are now:

- how large is the intrinsic consecutive discrepancy `Delta(r_N)` or its finite certificate `mathfrak A_N` as `N` grows;
- how does that scale interact with `mu_N`, especially when the latter approaches zero;
- and, once preperiod mixing is visible, whether its source field has enough mass in the nonblind generalized eigenspaces to beat the compressed frame cost.

A bound on `mathfrak A_N` that is merely another restatement of the desired Nyman closure would not count as progress. The useful target is a genuinely weaker arithmetic/conditioning estimate that places some growing diagonal inside (7) before invoking the `NB-015` budget.

## 6. Prior-art boundary and falsification controls

The load-bearing ingredients are already canonical in this line. Bagchi supplies the harmonic-shell model and compressed dilation semigroup; `NB-018` reconstructs the block-average formula (19); `NB-001` supplies the target-aware finite projection viewpoint. Equation (27) is an elementary exact discrepancy computation for the sawtooth shell sequence, and the remaining estimates are Abel summation and Hilbert-space projection inequalities. No new specialized external theorem is used, so `SOURCES.md` does not change.

A targeted literature check covered Bagchi's periodic-sequence/semigroup formulation, Báez--Duarte's discrete criteria and coefficient constructions, Bettin--Conrey--Farmer's optimal Dirichlet-polynomial coefficients, Ehm's 2024 Gram decompositions, recent multiscale Gram work, and searches for block averages or coefficient-controlled mixing of finite Nyman residuals. No located source stated the effective bound (7), the exact generator discrepancy (27) in this role, or the finite tail estimates (12)--(14). Search absence is not a novelty proof; the claim here is the exact derivation above.

Several controls are load-bearing. `mathfrak A_N` is canonical only relative to the fixed Báez--Duarte generator family; an arbitrary ill-conditioned change of basis can change a coefficient `l1` statistic, so (6) is not advertised as an invariant Hilbert quantity. The intrinsic version is `Delta(r_N)` in (18), and (29) is only one sufficient finite upper bound for it. Small `mathfrak A_N` is not proved, `mu_N` is not proved nonzero, and neither (7) nor (13) upper-bounds the compressed frame cost `beta_(N,M)`. Consequently no improved Nyman approximation rate, Möbius estimate, zero-free region, or RH implication follows from this finding alone.

The result is falsified by any canonical generator whose centered consecutive discrepancy exceeds (27), any violation of the exact weighted block formula (19), or any finite residual for which (7) fails when its exact projection coefficients are inserted. As an independent arithmetic check, (27) was verified exactly for `2<=j<=100`, and the generator specialization of (7) was checked with exact rational arithmetic for `2<=j<=14`, `2<=m<=20`, and `1<=n<=20`; these checks support but do not replace the proof.