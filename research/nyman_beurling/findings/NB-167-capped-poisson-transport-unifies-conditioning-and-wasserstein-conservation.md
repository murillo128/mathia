# NB-167 — Capped Poisson transport unifies conditioning and Wasserstein conservation

**Date:** 2026-09-16  
**Status:** `DERIVED + SOURCE-SPECIFIC + SIGNED-CONSERVATION + TRUNCATED-WASSERSTEIN + POISSON-SCALE + NB-165/NB-166-REFINEMENT`.

`NB-165` controls compact signed conservation by total variation, while `NB-166` improves this to ordinary Jordan `W_1` transport by differentiating the high-ordinate one-line bound for `zeta'/zeta`. Both estimates discard part of the geometry. Total variation charges every positive/negative unit equally, even when it almost cancels locally; `W_1` charges distance linearly forever, even after the two signs are separated by more than one Poisson width and a bounded analytic test can no longer distinguish additional distance.

The natural compact currency is therefore neither mass nor uncapped mean transport. It is the Jordan transport for the **truncated Poisson metric**

\[
d_a(s,t):=\min\left\{1,\frac{|s-t|}{a}\right\}.
\]

At distances below one exterior width it agrees with `W_1/a`; beyond one width it charges only the amount of unmatched signed mass. This is the same bounded-Lipschitz/Fortet--Mourier geometry that appears classically for finite measures, but here the cutoff scale is fixed by the distance to `Re s=1` and the test functions are the actual high-ordinate zeta source and Poisson zero kernels.

## Claim

Fix `A,B,kappa>0`. For arbitrarily large `G`, let

\[
0<a_G\le A
\]

and let `nu_G` be a finite real signed Borel measure supported on `[G-B,G+B]`, with zero total mass. Write

\[
\nu_G=\nu_G^+-\nu_G^-,
\qquad
m_G:=\nu_G^+(\mathbf R)=\nu_G^-(\mathbf R),
\qquad
V_G=2m_G.
\]

For couplings `pi in Pi(nu_G^+,nu_G^-)`, define

\[
\mathsf T_G
:=
\inf_\pi
\iint
\min\left\{1,\frac{|s-t|}{a_G}\right\}
\,d\pi(s,t).
\]

For each nontrivial zero `rho=beta+i gamma`, counted with multiplicity, put

\[
Q_G(\rho)
:=
\Re\int
\frac{d\nu_G(t)}{1+a_G+it-\rho},
\qquad
x_\rho:=1+a_G-\beta.
\]

Suppose a positive-ordinate target packet `F_G` satisfies

\[
d_G:=|F_G|\ge\kappa\log G,
\qquad
q_G:=\inf_{\rho\in F_G}Q_G(\rho)>0.
\]

Set

\[
C_G:=\frac{V_G}{q_G},
\qquad
W_G:=\mathsf W_1(\nu_G^+,\nu_G^-),
\qquad
\Theta_G:=\frac{2W_G}{q_Ga_G},
\qquad
\Xi_G:=\frac{\mathsf T_G}{q_G},
\]

and

\[
L_G:=\log G,
\qquad
L_{2,G}:=\log\log G,
\qquad
E_G:=\min\left\{\frac1{a_G},\frac{L_G}{L_{2,G}}\right\}.
\]

Then:

### 1. Capped transport strictly refines both previous conservation currencies

One has

\[
\boxed{
\Xi_G
\le
\frac12\min\{C_G,\Theta_G\}.
}
\]

Moreover the completed explicit-formula conservation remainder satisfies

\[
\boxed{
\sum_\rho Q_G(\rho)
=O_{A,B}(q_G\Xi_GE_G).
}
\]

Thus `NB-165` and `NB-166` are both recovered by the elementary bounds

\[
\mathsf T_G\le m_G,
\qquad
\mathsf T_G\le \frac{W_G}{a_G},
\]

but neither is the intrinsic compact estimate when a coupling contains both very short and very long moves.

### 2. The same capped transport controls every target Poisson response

For every nontrivial zero,

\[
\boxed{
|Q_G(\rho)|
\le
\frac{\mathsf T_G}{x_\rho}.
}
\]

Consequently every target zero satisfies

\[
\boxed{
\Xi_G\ge x_\rho,
\qquad \rho\in F_G.
}
\]

In particular, if `Delta_G` denotes any valid zero-free horizontal depth at height `G`, then for sufficiently large `G`

\[
\Xi_G\ge a_G+\Delta_G.
\]

So the capped metric is not merely a better source-side majorant: the target itself directly measures it at its own Poisson width.

### 3. A logarithmic packet exports full adverse debt whenever `Xi_G E_G=o(log G)`

Let

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\ \gamma>0}}
(Q_G(\rho))_-.
\]

Then

\[
\boxed{
A_G^-
\ge
q_G\left(
 d_G-O_{A,B}(\Xi_GE_G)
\right).
}
\]

Hence

\[
\boxed{
\Xi_GE_G=o(L_G)
\quad\Longrightarrow\quad
A_G^-\ge(\kappa-o(1))q_GL_G.
}
\]

This strictly enlarges the sufficient regime from both predecessor statements. In the extreme boundary layer `a_G << L_{2,G}/L_G`, it is enough that

\[
\boxed{\Xi_G=o(L_{2,G}),}
\]

even if both `C_G` and `Theta_G` are large.

### 4. Capped transport also gives a direct localization and population bound

There is `R_0=R_0(A,B)` such that, for sufficiently large fixed `D=D(A,B,kappa)`,

\[
R_G:=R_0+D\Xi_G
\]

satisfies under `Xi_GE_G=o(L_G)`

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\ \gamma>0\\ |\gamma-G|\le R_G}}
(Q_G(\rho))_-
\gg_{A,B,\kappa}q_GL_G.
}
\]

Using Bellotti's already anchored zero-free depth

\[
\Delta_G
:=
\frac{1}
{53.989\,[\log(2G)]^{2/3}[\log\log(2G)]^{1/3}},
\]

every localized adverse zero obeys the same pointwise capped-transport estimate

\[
|Q_G(\rho)|
\le
\frac{q_G\Xi_G}{a_G+\Delta_G}.
\]

Therefore

\[
\boxed{
\#\{\rho\notin F_G:\gamma>0,\ |\gamma-G|\le R_G,\ Q_G(\rho)<0\}
\gg
\frac{L_G(a_G+\Delta_G)}{\Xi_G}.
}
\]

The right side tends to infinity under the sole hypothesis `Xi_GE_G=o(L_G)`.

## Derivation

### The truncated Jordan metric interpolates mass and `W_1/a`

The cost

\[
d_a(s,t)=\min\{1,|s-t|/a\}
\]

is a bounded metric. Since `d_a<=1` and `d_a<=|s-t|/a`, every coupling gives

\[
\mathsf T_G\le m_G,
\qquad
\mathsf T_G\le W_G/a_G.
\]

Division by `q_G`, together with `m_G=q_GC_G/2` and `W_G=q_Ga_GTheta_G/2`, proves

\[
\Xi_G\le\frac12\min\{C_G,\Theta_G\}.
\]

The improvement can be strict by an arbitrarily large factor. A coupling may move most mass by `o(a_G)` while moving a very small fraction by a fixed macroscopic distance. The long moves dominate `W_1/a_G`, while capped transport charges them only by their mass; total variation, conversely, charges the locally cancelled majority at full price.

### High-ordinate analyticity is bounded-Lipschitz at one Poisson width

Put

\[
f_G(t):=\frac{\zeta'}{\zeta}(1+a_G+it).
\]

The two estimates already established in `NB-165` and `NB-166` give uniformly on `[G-B,G+B]`

\[
|f_G(t)|\ll_{A,B}E_G,
\qquad
|f_G'(t)|\ll_{A,B}\frac{E_G}{a_G}.
\]

Therefore for all `s,t` in the support interval,

\[
|f_G(s)-f_G(t)|
\le
\min\left\{2\|f_G\|_\infty,
\|f_G'\|_\infty|s-t|
\right\}
\ll_{A,B}
E_Gd_{a_G}(s,t).
\]

Integrating this inequality against any Jordan coupling and minimizing gives

\[
\left|
\int f_G(t)\,d\nu_G(t)
\right|
\ll_{A,B}E_G\mathsf T_G.
\]

The completed Gamma and rational terms are cheaper. Their oscillation on the bounded high-ordinate interval is `O_{A,B}(|s-t|/G)` (or better). Since bounded support gives `|s-t| \ll_{A,B} d_{a_G}(s,t)` after absorbing the harmless fixed factor and `1/G=o(E_G)`, their signed integrals are `O_{A,B}(E_G\mathsf T_G)` as well. Zero total mass cancels the Hadamard reference constants exactly as in `NB-165/166`. Hence

\[
\sum_\rho Q_G(\rho)
=O_{A,B}(E_G\mathsf T_G)
=O_{A,B}(q_G\Xi_GE_G).
\]

### Poisson kernels belong to the same bounded-Lipschitz class

For

\[
K_{x,\gamma}(t)
:=
\frac{x}{x^2+(t-\gamma)^2},
\]

one has

\[
0\le K_{x,\gamma}\le\frac1x,
\qquad
\|K'_{x,\gamma}\|_\infty
=
\frac{9}{8\sqrt3\,x^2}
<\frac1{x^2}.
\]

For every nontrivial zero, `x_rho>=a_G`. If `|s-t|>=a_G`, the range bound gives

\[
|K(s)-K(t)|\le x_\rho^{-1}d_{a_G}(s,t).
\]

If `|s-t|<a_G`, the derivative bound gives

\[
|K(s)-K(t)|
<
\frac{|s-t|}{x_\rho^2}
\le
\frac1{x_\rho}
\frac{|s-t|}{a_G}.
\]

Thus in all cases

\[
|K(s)-K(t)|
\le
\frac1{x_\rho}d_{a_G}(s,t).
\]

Coupling and minimizing proves `|Q_G(rho)|<=T_G/x_rho`. On the target packet `Q_G(rho)>=q_G`, so `Xi_G=T_G/q_G>=x_rho`.

### Signed debt and localization

For negative ordinates, `t` remains near `G` while `gamma<0`. The Poisson kernel has size `O((G+|gamma|)^{-2})` and derivative `O((G+|gamma|)^{-3})`. Splitting pairs according to whether `|s-t|` is below or above `a_G` yields

\[
|Q_G(\rho)|
\ll_{A,B}
\frac{\mathsf T_G}{(G+|\gamma|)^2}.
\]

Riemann--von Mangoldt shell counting gives

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_{A,B}
\mathsf T_G\frac{L_G}{G},
\]

which is negligible compared with `q_GL_G` when `Xi_GE_G=o(L_G)`. Combining this with the global conservation bound and the target contribution `q_Gd_G` proves the adverse-debt estimate.

For positive zeros with `|gamma-G|>=R>=R_0(A,B)`, the same two-regime argument gives

\[
|Q_G(\rho)|
\ll_{A,B}
\frac{\mathsf T_G}{|\gamma-G|^2}.
\]

Shell counting therefore yields

\[
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_{A,B}
\mathsf T_G\left(\frac{L_G}{R}+\frac{L_G}{G}\right).
\]

Since `T_G=q_GXi_G`, taking `R=R_0+DXi_G` and then `D` sufficiently large leaves a fixed fraction of the global `Omega(q_GL_G)` adverse debt inside the stated window. The hypothesis implies `Xi_G=o(L_G)`, so `R_G=o(G)`.

Finally the universal pointwise bound `|Q_G(rho)|<=T_G/x_rho` and Bellotti's zero-free region give `|Q_G(rho)|<=q_GXi_G/(a_G+Delta_G)` in the window. Dividing the localized debt by this maximum proves the population lower bound.

To check divergence, write

\[
\Xi_GE_G=\varepsilon_GL_G,
\qquad \varepsilon_G\to0.
\]

If `E_G=1/a_G`, then

\[
\frac{L_G(a_G+\Delta_G)}{\Xi_G}
\ge\varepsilon_G^{-1}.
\]

If `E_G=L_G/L_{2,G}`, then `Xi_G=epsilon_G L_{2,G}` and

\[
\frac{L_G(a_G+\Delta_G)}{\Xi_G}
\ge
\frac{L_G\Delta_G}{\varepsilon_GL_{2,G}}
\asymp
\frac{L_G^{1/3}}
{\varepsilon_GL_{2,G}^{4/3}}
\longrightarrow\infty.
\]

## Representation and generalized-control audit

The capped-transport lemma itself is not arithmetic. Any bounded test `f` with `||f||_infty<=M` and `Lip(f)<=M/a` obeys

\[
\left|\int f\,d\nu\right|
\ll M\mathsf T_a(\nu).
\]

Likewise the Poisson-kernel estimate is pure kernel geometry. The source-specific input is exactly the high-ordinate zeta statement that `zeta'/zeta` belongs to this bounded-Lipschitz class with `M=O(E_G)`. Thus a matched non-arithmetic control with the same sup-norm and derivative bounds satisfies the same conservation inequality. The new information is not a hidden RH claim; it identifies the correct representation-invariant signed geometry seen by all such tests and shows where the actual zeta estimate enters.

This audit also exposes why neither predecessor currency is canonical. Two measures can have the same total variation but arbitrarily different `T_a`; they can also have the same `W_1` but very different `T_a` by reallocating a small amount of mass beyond the cutoff. Hence the improvement is not a basis reparameterization of `C_G` or `Theta_G`.

## What this changes after NB-165 and NB-166

The compact source budget is now controlled by

\[
\boxed{\Xi_GE_G,\qquad \Xi_G=\mathsf T_G/q_G,}
\]

where `T_G` measures how much positive/negative Jordan mismatch survives after one Poisson width of resolution. At short distances this reduces to the transport currency of `NB-166`; at long distances it reduces to the mass currency of `NB-165`; mixed geometries can be substantially cheaper than either global summary.

This tightens the surviving escape route. Large total variation is irrelevant if it is locally paired, and large ordinary `W_1` is irrelevant if it is carried by too little mass beyond one width. To defeat the present conservation argument in the extreme boundary layer, the sampler needs capped mismatch `Xi_G` of order at least `log log G` (up to non-vanishing factors), not merely a large value of one predecessor parameter.

The target inequality `Xi_G>=x_rho` also gives a useful interpretation: `Xi_G` is an effective unresolved signed width measured in the same units as the zero's Poisson scale. The open regime is therefore no longer described well by either 'high conditioning' or 'large transport' alone. What matters is whether a logarithmic packet can coexist with enough **Poisson-resolution Jordan mismatch** to reach the source-side threshold while still avoiding the adverse population forced above.

## Prior-art and novelty audit

A fresh search found the classical bounded-Lipschitz/Fortet--Mourier/Dudley probability metrics and the equivalent truncated-Wasserstein viewpoint with cost `min(1,d)`. That metric technology is standard and is not claimed as new. Searches combining those terms with Nyman--Beurling approximation, signed Poisson sampling, and high-ordinate `zeta'/zeta` did not locate the present transfer: scale the truncated cost by the exterior Poisson width, use the high-ordinate one-line value and Cauchy derivative bounds to place the zeta source in the corresponding bounded-Lipschitz class, and propagate the resulting currency simultaneously through target gain, signed zero conservation, localization, and adverse population.

No new external theorem is load-bearing. The Cully--Hugill--Leong high-ordinate bound, Bellotti zero-free region, and Riemann--von Mangoldt counting are already anchored in `SOURCES.md`; the capped-coupling inequalities above are proved directly. Therefore `SOURCES.md` is unchanged.

## Boundaries and failure modes

The sampler is still confined to one exterior vertical line and a bounded vertical interval. Growing vertical diameter or horizontal support requires a scale-dependent version of the capped cost. The condition `Xi_GE_G=o(log G)` is sufficient, not necessary: actual signed values of `zeta'/zeta` can cancel more strongly than any bounded-Lipschitz majorant records.

The target packet remains conditional. No crowded off-critical packet is asserted to exist, and no conclusion here proves RH. Adverse zeros are counted with multiplicity, consistently with the preceding findings.