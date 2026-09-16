# NB-165 — High-ordinate one-line bounds cap the inverse boundary-gap tariff

**Date:** 2026-09-16  
**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + BOUNDARY-APPROACH + HIGH-ORDINATE-LOG-DERIVATIVE + NB-154-REFINEMENT`.

`NB-154` shows that a compact zero-mass signed exterior sampler pays an Euler remainder of size `O(V_G/a_G)` when its closest horizontal distance to `Re s=1` is `a_G`. That estimate is obtained by discarding all oscillation in the actual high-ordinate logarithmic derivative and using only absolute convergence of the Euler product. It is therefore sharp as a boundary-only majorant but not as a high-ordinate source estimate.

The actual zeta source supplies a second bound. Cully--Hugill and Leong prove uniformly for `sigma>=1` and sufficiently large `t` that

\[
\left|\frac{\zeta'}{\zeta}(\sigma+it)\right|
\ll \frac{\log t}{\log\log t},
\]

with an explicit constant. Taking the better of this estimate and the absolute Euler bound caps the `1/a_G` tariff once `a_G` falls below about `log log G/log G`. Thus arbitrarily close boundary approach does not make the signed conservation remainder arbitrarily expensive: at high ordinate it saturates at the one-line logarithmic-derivative scale.

## Claim

Fix `A,B,kappa>0`. For arbitrarily large `G`, let

\[
0<a_G\le A
\]

and let `mu_G` be a finite real signed Borel measure supported on

\[
K_G\subset
\{w\in\mathbf C:
 a_G\le\Re w\le A,
\ |\Im w|\le B\}
\]

with

\[
\mu_G(K_G)=0,
\qquad
V_G:=\|\mu_G\|_{\rm TV}.
\]

For each nontrivial zeta zero `rho=beta+i gamma`, counted with multiplicity, define

\[
Q_G(\rho)
:=
\Re\int_{K_G}
\frac{d\mu_G(w)}{1+w+iG-\rho}.
\]

Suppose a positive-ordinate target packet `F_G` satisfies

\[
d_G:=|F_G|\ge\kappa\log G,
\qquad
q_G:=\inf_{\rho\in F_G}Q_G(\rho)>0,
\]

and write

\[
C_G:=\frac{V_G}{q_G}.
\]

Put

\[
L_G:=\log G,
\qquad
L_{2,G}:=\log\log G,
\qquad
M_G:=\min\left\{\frac1{a_G},\frac{L_G}{L_{2,G}}\right\}.
\]

Then:

### 1. The signed conservation remainder pays the smaller of the boundary and high-ordinate costs

There is a constant depending only on `A,B` such that

\[
\boxed{
\sum_\rho Q_G(\rho)
=O_{A,B}(V_G M_G).
}
\]

Consequently, if

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\ \gamma>0}}
(Q_G(\rho))_-,
\]

then more generally

\[
\boxed{
A_G^-
\ge
q_G\left(
 d_G-O_{A,B}(C_GM_G)
\right),
}
\]

and for a logarithmic target packet,

\[
\boxed{
A_G^-
\ge
q_GL_G
\left(
\kappa-O_{A,B}\!\left(\frac{C_GM_G}{L_G}\right)
\right).
}
\]

Hence the adverse debt remains asymptotically full whenever

\[
\boxed{
C_GM_G=o(L_G).
}
\]

This condition interpolates two genuinely different regimes:

\[
a_G\gg \frac{L_{2,G}}{L_G}
\quad\Longrightarrow\quad
M_G\asymp a_G^{-1},
\]

which recovers the `NB-154` boundary-normalized condition, whereas

\[
a_G\ll \frac{L_{2,G}}{L_G}
\quad\Longrightarrow\quad
M_G\asymp \frac{L_G}{L_{2,G}},
\]

so the sufficient condition becomes simply

\[
\boxed{C_G=o(L_{2,G})}
\]

with no remaining dependence on how fast `a_G` tends to zero.

### 2. A fixed fraction of the adverse debt remains within radius `O(1+C_G)`

There are constants `R_0=R_0(B)` and, after choosing a sufficiently large fixed `M=M(A,B,kappa)`, the radius

\[
R_G:=R_0+MC_G
\]

satisfies under `C_GM_G=o(L_G)`

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\ \gamma>0\\ |\gamma-G|\le R_G}}
(Q_G(\rho))_-
\gg_{A,B,\kappa}
q_G L_G.
}
\]

Thus replacing the absolute Euler estimate by the high-ordinate one-line estimate changes the global conservation budget but does not buy long-range ordinate escape.

### 3. The localized debt still requires a divergent adverse zero population

Let

\[
\Delta_G
:=
\frac{1}
{53.989\,[\log(2G)]^{2/3}[\log\log(2G)]^{1/3}},
\]

using the explicit Vinogradov--Korobov zero-free region already anchored in this line. Since `C_GM_G=o(L_G)` implies `C_G=o(L_G)`, one has `R_G=o(G)`. Hence for every zero in the localization window and all sufficiently large `G`,

\[
1-\beta\ge\Delta_G.
\]

Every such zero therefore obeys the pointwise estimate

\[
|Q_G(\rho)|
\le
\frac{V_G}{a_G+\Delta_G}
=
\frac{q_GC_G}{a_G+\Delta_G}.
\]

Combining this with the localized adverse mass gives, counting zeros with multiplicity,

\[
\boxed{
\#\left\{
\rho\notin F_G:
\gamma>0,
|\gamma-G|\le R_G,
Q_G(\rho)<0
\right\}
\gg
\frac{(a_G+\Delta_G)L_G}{C_G}.
}
\]

Under `C_GM_G=o(L_G)` the right side tends to infinity. In the extreme boundary regime `a_G\ll L_{2,G}/L_G` and `C_G=o(L_{2,G})`, the zero-free part alone yields

\[
\#\{\text{localized adverse zero occurrences}\}
\gg
\frac{L_G^{1/3}}
{C_G L_{2,G}^{1/3}},
\]

which still diverges even when `C_G` approaches the permitted `o(L_{2,G})` scale.

## Derivation

### High-ordinate arithmetic caps the Euler term

As in `NB-154`, zero total sampler mass makes the zero sum absolutely convergent after subtracting any reference point in `K_G`, and termwise integration of the completed logarithmic derivative gives

\[
\sum_\rho Q_G(\rho)
=
\Re\int_{K_G}
\frac{\xi'}{\xi}(1+w+iG)
\,d\mu_G(w).
\]

The rational completed-function terms contribute `O_{A,B}(V_G/G)`. Stirling gives uniformly on the bounded support

\[
\psi((1+w+iG)/2)
=
\log(iG/2)+O_{A,B}(1/G),
\]

and the common logarithm disappears because `mu_G(K_G)=0`. The only potentially large term is therefore the actual logarithmic derivative of zeta.

Two independent pointwise estimates are available. Absolute convergence of the Euler product gives, exactly as in `NB-154`,

\[
\left|
\frac{\zeta'}{\zeta}(1+w+iG)
\right|
\ll_A \frac1{a_G}.
\]

On the other hand, Corollary 2 of Cully--Hugill--Leong gives for `sigma>=1` and `t>=500`

\[
\left|
\frac{\zeta'}{\zeta}(\sigma+it)
\right|
\le
113.3\frac{\log t}{\log\log t}.
\]

Since `|Im w|<=B`, uniformly on `K_G`

\[
\left|
\frac{\zeta'}{\zeta}(1+w+iG)
\right|
\ll_B \frac{L_G}{L_{2,G}}.
\]

Taking the smaller of the two estimates proves

\[
\left|
\int_{K_G}
\frac{\zeta'}{\zeta}(1+w+iG)
\,d\mu_G(w)
\right|
\ll_{A,B}V_GM_G,
\]

and hence the first conservation formula.

### The target packet still exports signed debt

The target contributes at least `q_Gd_G`. Negative-ordinate zeros are still a quadratic-distance tail, uniformly in the compact geometry:

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_{A,B}
V_G\frac{L_G}{G}.
\]

Because `M_G` is bounded below by a positive constant depending only on `A` for large `G`, this tail is negligible compared with `V_GM_G`. Splitting the remaining positive-ordinate zero contributions into positive and negative parts therefore yields

\[
A_G^-
\ge
q_Gd_G-O_{A,B}(V_GM_G),
\]

which is the stated debt estimate after substituting `V_G=q_GC_G`.

The crossover at `a_G\asymp L_{2,G}/L_G` is now explicit. Above it the elementary boundary majorant is stronger. Below it, the actual high-ordinate zeta source prevents the source-side remainder from continuing to grow like `1/a_G`. This is the precise sense in which the inverse-gap tariff saturates rather than disappears everywhere.

### Localization is unchanged

For `|G-\gamma|` larger than a fixed multiple of `B+1`, the real Cauchy kernel gives

\[
|Q_G(\rho)|
\ll_{A,B}
\frac{V_G}{(G-\gamma)^2}.
\]

Riemann--von Mangoldt shell counting therefore gives, for `R>=R_0(B)` and `R=o(G)`,

\[
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_{A,B}
V_G\left(
\frac{L_G}{R}+
\frac{L_G}{G}
\right).
\]

Since `M_G\gg_A1`, the condition `C_GM_G=o(L_G)` implies `C_G=o(L_G)`, hence `R_G=o(G)`. With `R_G=R_0+MC_G`, the first tail term is `O(q_GL_G/M)`, uniformly even when `C_G` is small because `C_G/(R_0+MC_G)<=1/M`. Choosing `M` large enough leaves a fixed fraction of the `Omega(q_GL_G)` adverse debt inside the displayed localization window.

### The zero-free region converts adverse mass into population

For a localized zero `rho=beta+i gamma`, Bellotti's anchored zero-free region and `|gamma|<=2G` imply `1-beta>=Delta_G` for all sufficiently large `G`. For `w=u+iv in K_G`,

\[
1+u-\beta
\ge
a_G+\Delta_G.
\]

Since

\[
\Re\frac1{1+w+iG-\rho}
=
\frac{1+u-\beta}
{(1+u-\beta)^2+(G+v-\gamma)^2}
\le
\frac1{a_G+\Delta_G},
\]

integration against total variation proves the pointwise bound. Dividing the localized adverse mass by this maximum contribution gives the population estimate.

To see that the lower bound diverges under the sole conservation hypothesis, write `C_G=epsilon_G L_G/M_G` with `epsilon_G->0`. Then

\[
\frac{(a_G+\Delta_G)L_G}{C_G}
=
\frac{(a_G+\Delta_G)M_G}{\epsilon_G}.
\]

If `M_G=1/a_G`, the numerator is at least one. If `M_G=L_G/L_{2,G}`, then

\[
\Delta_GM_G
\asymp
\frac{L_G^{1/3}}{L_{2,G}^{4/3}}
\longrightarrow\infty.
\]

Thus in either branch the required adverse population tends to infinity.

## What this changes after NB-154 and NB-164

`NB-154` correctly identified `C_G/a_G` as the cost visible from the absolutely convergent Euler series alone. The present result shows that this currency has a high-ordinate ceiling for the **actual zeta source**. The correct available conservation estimate in compact geometry is governed by

\[
\boxed{
C_G\min\left\{a_G^{-1},\frac{\log G}{\log\log G}\right\},
}
\]

not by `C_G/a_G` in every boundary regime.

This matters precisely in the very thin boundary layer. If `a_G` is fixed or only moderately small, `NB-154` remains stronger and nothing is lost. Once `a_G` is below `log log G/log G`, however, further movement toward `Re s=1` no longer worsens the conservation remainder at the `1/a_G` rate. In particular, bounded conditioning continues to force essentially the full adverse `q_G log G` debt no matter how quickly `a_G->0`.

`NB-164` independently shows that increasing local moment order cannot rescue a one-width sampler without exponential conditioning or nonlocal support. Together, these results make the surviving compact route more source-specific still: a bounded/controlled-order one-width interlaced sampler would need **actual signed cancellation inside the high-ordinate logarithmic derivative substantially beyond the already nontrivial one-line pointwise bound**, while retaining target gain. Merely approaching the boundary is no longer an unlimited source of arithmetic amplification.

## Prior-art and novelty audit

The load-bearing high-ordinate estimate is not new. Michaela Cully--Hugill and Nicol Leong, *Explicit estimates for the Riemann zeta function close to the 1-line*, J. Math. Anal. Appl. 540 (2024), Article 128494, prove explicit `log t/log log t` bounds for the logarithmic derivative near and on the one-line; Corollary 2 supplies the uniform `sigma>=1` estimate used above. Earlier explicit work such as Trudgian's `O(log t)` logarithmic-derivative bound lies in the same classical source-estimation direction.

A fresh search across Nyman--Beurling criteria, Poisson-kernel sampling, signed measures, and logarithmic-derivative estimates found the expected approximation/Gram literature and the classical zeta source bounds, but not the line-specific transfer used here: inserting a high-ordinate one-line `zeta'/zeta` estimate into the zero-mass Hadamard conservation law to cap the inverse boundary-gap tariff, then combining that with localization and the explicit zero-free region to force a divergent adverse population. No novelty is claimed for the Cully--Hugill--Leong estimate, Riemann--von Mangoldt counting, or Bellotti's zero-free region separately.

Because the Cully--Hugill--Leong theorem is now load-bearing rather than merely neighboring literature, it is added to `SOURCES.md`. Bellotti's zero-free region was already anchored.

## Boundaries and failure modes

This is an upper bound on the total signed source remainder, not a lower bound on actual Euler leakage. A specially designed sampler may cancel the actual values of `zeta'/zeta(1+w+iG)` much more strongly; that remains the source-specific escape rather than being ruled out here.

The support remains horizontally and vertically compact apart from its distance `a_G` to the one-line. The argument does not automatically cover samplers whose vertical diameter grows comparably with `G`, because then the one-line bound and the completed-Gamma variation must be tracked across the whole sampled height range. Nor does the result claim that `log G/log log G` is the optimal possible pointwise logarithmic-derivative scale for this application; it is the explicit verified source estimate used in this finding.

The target packet hypothesis is conditional. The theorem does not assert the existence of a logarithmic crowded zero packet or prove RH. It states that if such a packet is uniformly positively charged by a compact zero-mass exterior sampler, then the rest of the actual zeta divisor must carry the quantified adverse debt.

The population count is with multiplicity. No simplicity assumption is used, and the present inputs do not convert that lower bound into the same number of distinct ordinates.

## Source map

- `NB-144`: the elementary absolute Euler-product estimate `|zeta'/zeta(1+a+it)|<<1/a`.
- `NB-154`: boundary-normalized signed conservation, localization and the original `C_G/a_G` adverse-debt condition.
- `NB-160`--`NB-164`: separated-support, transport and moment obstructions that narrow the surviving signed geometry to source-specific one-width interlacing or explicitly nonlocal/ill-conditioned constructions.
- Cully--Hugill--Leong (2024): uniform high-ordinate `log t/log log t` bound for `zeta'/zeta` on `sigma>=1`.
- Bellotti (2024): explicit Vinogradov--Korobov zero-free region used to turn localized adverse mass into a divergent population.

## Consequence for the line

Boundary approach is not an unlimited conditioning resource for compact signed zeta samplers. **The source-side conservation cost is bounded by `V_G min{1/a_G, log G/log log G}`. Therefore every logarithmic target packet still exports essentially its full signed adverse debt whenever `C_G min{1/a_G, log G/log log G}=o(log G)`. Below the crossover `a_G~log log G/log G`, the inverse-gap tariff saturates and `C_G=o(log log G)` suffices regardless of how fast the sampler approaches `Re s=1`.** The remaining compact escape must exploit cancellation in the actual arithmetic source beyond this pointwise one-line control; boundary motion alone no longer changes the budget.