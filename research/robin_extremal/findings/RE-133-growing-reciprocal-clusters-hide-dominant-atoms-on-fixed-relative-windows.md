# RE-133 — growing reciprocal clusters hide dominant atoms on fixed-relative windows

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SIMPLE-SPECTRUM + FUNCTIONAL-EQUATION-SYMMETRY + ARBITRARILY-SPARSE-OFF-CRITICAL-DENSITY + DOMINANT-ATOM-HIDING + GROWING-RECIPROCAL-CLUSTER + MACROSCOPIC-WINDOW-HIDING + DECISIVE-NEGATIVE + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-132` shows that one simple `pi/U` doublet can hide a globally dominant algebraic subedge atom on every sublinear window, but the same pair becomes visible on a fixed-relative window because `1-e^{i pi t/U}` is then order one. `RE-131` exploits precisely that stronger observation scale: if the actual packet stays small on `|u-U|<=kappa U`, it forces a polylogarithmic-reciprocal, horizontally locked cancelling companion.

The macroscopic scale does not by itself close the formal matched-control class. A **growing finite cluster** of reciprocal-scale increments can suppress the same coefficient kernel uniformly on a fixed-relative window, while the full off-critical spectrum remains simple, functional-equation symmetric, and arbitrarily sparse in every one-level counting sense.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad K\ge0,
\qquad A>0,
\qquad 0<\kappa<\frac12.
\tag{1}
\]

Let `L(T)` be any nondecreasing function with `L(T)->infinity`. There exists a formal simple zero spectrum `Z_ctl`, closed under

\[
\rho\mapsto\bar\rho,
\qquad
\rho\mapsto1-\rho,
\tag{2}
\]

with a finite attained right edge `Re rho=Theta`, an infinite subedge set in `sigma_0<=Re rho<Theta`, and phases `U_j->infinity`, such that for the same order-`K` coefficient law

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right]
\tag{3}
\]

and formal positive-frequency packet

\[
\mathcal S_K^{\rm ctl}(u)
:=2\Re\sum_{\substack{\rho\in\mathcal Z_{\rm ctl}\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
a_{\rho,K}(u)e^{i\Im(\rho)u},
\tag{4}
\]

one has

\[
\boxed{
M_K^{\rm ctl}(U_j)
:=\max_{\substack{\rho\in\mathcal Z_{\rm ctl}\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
|a_{\rho,K}(U_j)|
=(1+o(1))U_j^{-A},
}
\tag{5}
\]

Here and in (6), `M_K^{ctl}` is the maximum over exactly the strict-subedge positive-frequency index set in (4); the fixed attained-edge quartet is excluded from this normalization. Thus

\[
\boxed{
\sup_{|u-U_j|\le\kappa U_j}
|\mathcal S_K^{\rm ctl}(u)|
=o\!\left(M_K^{\rm ctl}(U_j)\right).
}
\tag{6}
\]

At the same time the positive-ordinate right-half-strip count can be made smaller than the prescribed divergent envelope,

\[
\boxed{
N_{\rm ctl}(\sigma_0,T)
\le L(T)
}
\tag{7}
\]

for all sufficiently large `T`, after an immaterial fixed multiplicative enlargement of `L` if one wishes to count an added edge quartet. Thus no one-level upper density condition, however slowly divergent, forbids macroscopic hiding in this formal class.

The word **formal** remains essential. As in `RE-132`, the construction preserves the zero symmetries and the exact finite-order Robin/CA coefficient kernel but is not asserted to be the zero set of `zeta`, of an Euler product, or of any analytic function satisfying the zeta explicit formula.

## 1. A contractive reciprocal-scale factor exists on every strict relative window

Choose `0<r<1` so small that

\[
r^{1-\kappa}<2\cos(\pi\kappa).
\tag{8}
\]

This is possible because `kappa<1/2`. Put

\[
\lambda:=-\log r>0.
\tag{9}
\]

For `|s|<=kappa`, define

\[
F(s):=1-r^{1+s}e^{i\pi s}.
\tag{10}
\]

Writing `x=r^(1+s)` gives

\[
|F(s)|^2=1+x^2-2x\cos(\pi s).
\tag{11}
\]

Because

\[
x\le r^{1-\kappa}
<2\cos(\pi\kappa)
\le2\cos(\pi s),
\tag{12}
\]

we have `|F(s)|<1` throughout the compact interval `[-kappa,kappa]`. Hence

\[
\boxed{
q:=\max_{|s|\le\kappa}|F(s)|<1.
}
\tag{13}
\]

This strict contraction is the entire macroscopic mechanism. A single `pi/U` pair corresponds essentially to one factor and leaves a fixed nonzero residual on a relative window. Repeating independent reciprocal-scale increments makes the residual a product of factors bounded by `q<1`.

## 2. The stage-`j` simple cluster realizes the product with the actual coefficient kernel

Choose a phase `U_j`, eventually extremely lacunary, and put

\[
\Gamma_j:=U_j^{A/2},
\qquad
\delta_j:=U_j^{-2}.
\tag{14}
\]

Use `m_j:=j` reciprocal increments. To keep every subset coordinate simple and distinct, let

\[
\varepsilon_{j,\ell}:=U_j^{-3}3^{-\ell},
\qquad 1\le\ell\le j.
\tag{15}
\]

For every subset `S` of `{1,...,j}`, define

\[
\rho_{j,S}=\beta_{j,S}+i\gamma_{j,S},
\tag{16}
\]

where

\[
\Theta-\beta_{j,S}
:=
\delta_j+\frac{|S|\lambda}{U_j},
\tag{17}
\]

and

\[
\gamma_{j,S}
:=
\Gamma_j+\frac1{U_j}
\sum_{\ell\in S}(\pi+\varepsilon_{j,\ell}).
\tag{18}
\]

The ternary perturbations make different subsets have different ordinate sums. If two subsets have different cardinalities, the integer multiple of `pi` already separates them; if they have the same cardinality, uniqueness of finite base-three sums with digits `0,1` separates them. Thus all `2^j` positive-ordinate right-half-strip coordinates are simple. Since `j/U_j->0`, all of them lie in `sigma_0<=beta<Theta` for sufficiently large `j`.

Close the stage under (2). If an attained edge is required, adjoin a fixed finite simple quartet with right member on `Re rho=Theta`, exactly as in `RE-132`; it is absent from the strict-subedge packet (4).

Write

\[
u=U_j(1+s),
\qquad |s|\le\kappa,
\tag{19}
\]

and denote the empty-subset coordinate by `rho_(j,emptyset)`. The exponential damping ratio is exact:

\[
\frac{
 e^{-(\Theta-\beta_{j,S})u}
}{
 e^{-(\Theta-\beta_{j,\varnothing})u}
}
=
r^{(1+s)|S|}.
\tag{20}
\]

The rational bracket in (3) is stable across the microscopic cluster. Uniformly in `S` and `|s|<=kappa`, the coefficient asymptotic used in `RE-124`--`RE-132` gives

\[
\frac{
 a_{\rho_{j,S},K}(u)
}{
 a_{\rho_{j,\varnothing},K}(u)
}
=
r^{(1+s)|S|}
\left(1+O_K(\eta_j)\right),
\tag{21}
\]

with, for example,

\[
\eta_j
:=
\frac1{U_j}+
\frac{j}{U_j\Gamma_j}
=o(1).
\tag{22}
\]

Indeed the finite-`K` corrections are relatively `O_K(1/u)`, while logarithmic differentiation of `1/[rho(1-rho)]` over a displacement `O(j/U_j)` costs `O(j/(U_j Gamma_j))` because `Gamma_j->infinity`.

The phase ratio is also explicit:

\[
e^{i(\gamma_{j,S}-\Gamma_j)u}
=
\prod_{\ell\in S}
\left[
- e^{i\pi s}
  e^{i\varepsilon_{j,\ell}(1+s)}
\right].
\tag{23}
\]

Consequently, if the harmless bracket variation in (21) is momentarily frozen, the full positive-frequency stage cluster factors as

\[
\begin{aligned}
& a_{\rho_{j,\varnothing},K}(u)e^{i\Gamma_j u}
\sum_{S}
 r^{(1+s)|S|}
 e^{i(\gamma_{j,S}-\Gamma_j)u}
\\
&\qquad=
 a_{\rho_{j,\varnothing},K}(u)e^{i\Gamma_j u}
\prod_{\ell=1}^{j}
\left[
1-r^{1+s}e^{i\pi s}
  e^{i\varepsilon_{j,\ell}(1+s)}
\right].
\end{aligned}
\tag{24}
\]

Because the perturbations in (15) tend uniformly to zero and (13) has a strict margin, there is a fixed `q_1<1` such that for all sufficiently large `j`,

\[
\max_{|s|\le\kappa}
\left|
1-r^{1+s}e^{i\pi s}
  e^{i\varepsilon_{j,\ell}(1+s)}
\right|
\le q_1
\tag{25}
\]

for every `ell`. Hence the frozen main term in (24) is at most

\[
|a_{\rho_{j,\varnothing},K}(u)|q_1^j.
\tag{26}
\]

The aggregate error from restoring the actual brackets in (21) is bounded before any cancellation by

\[
\begin{aligned}
&|a_{\rho_{j,\varnothing},K}(u)|
O_K(\eta_j)
\sum_S r^{(1+s)|S|}
\\
&\qquad\le
|a_{\rho_{j,\varnothing},K}(u)|
O_K(\eta_j)
\left(1+r^{1-\kappa}\right)^j.
\end{aligned}
\tag{27}
\]

When the phases `U_j` are chosen below, we may and do require

\[
\eta_j\left(1+r^{1-\kappa}\right)^j\longrightarrow0.
\tag{28}
\]

Equations (26)--(28) therefore give the uniform stage estimate

\[
\boxed{
\sup_{|u-U_j|\le\kappa U_j}
\left|
\sum_S a_{\rho_{j,S},K}(u)e^{i\gamma_{j,S}u}
\right|
=o\!\left(U_j^{-A}\right).
}
\tag{29}
\]

The empty-subset atom itself remains algebraically strong. Uniformly at the center,

\[
|a_{\rho_{j,\varnothing},K}(U_j)|
=(1+o(1))\Gamma_j^{-2}
=(1+o(1))U_j^{-A}.
\tag{30}
\]

For every nonempty `S`, (21) at `s=0` gives

\[
\frac{|a_{\rho_{j,S},K}(U_j)|}
{|a_{\rho_{j,\varnothing},K}(U_j)|}
=
r^{|S|}(1+o(1))<1.
\tag{31}
\]

Thus the cluster contains a unique asymptotic dominant atom, and its first-generation companions already have fixed amplitude ratio `r+o(1)`, reciprocal-scale ordinate separation `(pi+o(1))/U_j`, and horizontal separation `lambda/U_j`. The geometry required by `RE-131` is therefore present rather than evaded.

## 3. Lacunarity isolates each growing cluster and permits any divergent density envelope

Choose the phases recursively. Besides `U_(j+1)>=U_j^4`, require `U_j` large enough for (28), for every stage coordinate to lie to the right of `sigma_0`, and for

\[
L(\Gamma_j)\ge 2^{j+3}.
\tag{32}
\]

This is possible because `L(T)->infinity` and `Gamma_j=U_j^(A/2)`.

We also impose two standard lacunary separation budgets. When choosing `U_(j+1)`, enlarge it until every already chosen cluster is exponentially negligible throughout the next relative window:

\[
\sum_{n\le j}
2^n
\frac{
\exp[-(1-\kappa)U_{j+1}/(2U_n^2)]
}{1+\Gamma_n^2}
\le
U_{j+1}^{-A-j-4}.
\tag{33}
\]

This is possible because each previous minimum horizontal edge distance `delta_n=U_n^-2` is fixed once stage `n` is chosen. For the future tail require, after further enlargement,

\[
2^{j+1}U_{j+1}^{-A}
\le
2^{-j}U_j^{-A-j-4}.
\tag{34}
\]

Subsequent phases can be chosen so rapidly that the full future series is dominated by this first tail term. Using the universal coefficient envelope

\[
|a_{\rho,K}(u)|\ll_K(1+\gamma^2)^{-1},
\tag{35}
\]

(33)--(35) imply, uniformly on `|u-U_j|<=kappa U_j`,

\[
\sum_{n\ne j}
\sum_{S\subseteq\{1,\ldots,n\}}
|a_{\rho_{n,S},K}(u)|
=o(U_j^{-A}).
\tag{36}
\]

Combining (29), (30), (31), and (36) proves (5) on the strict-subedge index set in (4) and then proves (6). Taking `2Re` cannot enlarge the complex packet estimate.

The same recursion proves the arbitrary one-level sparsity claim. After stage `j`, the total number of positive-ordinate right-half-strip coordinates from all completed clusters is

\[
\sum_{n\le j}2^n<2^{j+1}.
\tag{37}
\]

For `T` from the top of stage `j` until stage `j+1` first appears, monotonicity of `L` and (32) give

\[
N_{\rm ctl}(\sigma_0,T)
<2^{j+1}+O(1)
\le L(T)
\tag{38}
\]

for all sufficiently large `j`. Enlarging `U_j` never harms any already imposed condition, so (32)--(34) are compatible.

Thus even a spectrum whose off-critical count grows more slowly than any preassigned divergent envelope can contain, at isolated heights, enough microscopic local complexity to suppress a dominant atom on a fixed-relative observation window. Global sparsity and local cluster cardinality are independent resources.

## 4. Why this does not contradict `RE-131`

`RE-131` is a necessary-geometry theorem. Its conclusion is satisfied many times over here. For each stage, every singleton `S={ell}` has

\[
|\gamma_{j,S}-\gamma_{j,\varnothing}|
=\frac{\pi+o(1)}{U_j},
\tag{39}
\]

\[
\beta_{j,S}-\beta_{j,\varnothing}
=-\frac\lambda{U_j},
\tag{40}
\]

and

\[
|a_{\rho_{j,S},K}(U_j)|
=(r+o(1))M_K^{\rm ctl}(U_j).
\tag{41}
\]

Its target-demodulated center phase is `pi+o(1)`, so its projection is genuinely cancelling. This is stronger than the logarithmic amplitude fraction and polylogarithmic-reciprocal distance that `RE-131` forces.

The new point is that one companion is not asked to cancel the dominant atom by itself throughout the whole relative window. The `2^j` subset atoms realize the finite product (24). Every additional reciprocal increment contributes another factor whose modulus is uniformly below one on `[-kappa,kappa]`, and the number of factors tends to infinity. The macroscopic residual therefore tends to zero even though each individual pair loses exact cancellation away from the center.

The construction makes the remaining possible discriminator explicit. **Growing microscopic cluster complexity is load-bearing.** With a fixed number of factors, (26) gives only a fixed suppression constant, not `o(M)`. Thus this finding does not rule out a theorem proving that actual near-edge zeta zeros have uniformly bounded effective occupancy, incompatible correlations, or another source-specific restriction inside reciprocal-scale boxes.

## 5. Adversarial audit

The main failure modes were checked directly.

First, the construction uses the actual finite-order coefficient law (3), not freely assigned exponential-sum coefficients. The horizontal offsets in (17) generate the geometric amplitudes needed by the product, and the vertical offsets in (18) generate the signs and phase drift. The nonmultiplicative rational bracket is absorbed only after summing its absolute error in (27); no termwise `o(1)` is mistaken for a packet-level error across `2^j` modes.

Second, simplicity is genuine. Exact subset-frequency collisions that would occur with repeated identical increments are removed by the ternary perturbations (15), while their total phase effect is much smaller than the strict contraction margin in (13). No multiplicity or coincident ordinate is used.

Third, the cluster remains inside the prescribed half-strip. Its horizontal diameter is

\[
O\!\left(\frac{j}{U_j}\right),
\tag{42}
\]

and its vertical diameter is

\[
O\!\left(\frac{j}{U_j}\right).
\tag{43}
\]

Both vanish. The empty-subset coordinates still approach the attained edge, so the subedge remains nonisolated. The cluster cardinality `2^j` can simultaneously be much smaller than `log Gamma_j`, or any other prescribed diverging local allowance, by enlarging `U_j`.

Fourth, the full infinite packet rather than an isolated stage is controlled. Previous stages are killed by their fixed positive horizontal edge gaps, future stages by the `1/gamma^2` coefficient envelope and lacunarity. The estimates are uniform on the entire fixed-relative interval, including its left endpoint where damping is weakest.

Fifth, (7) is not being converted into a local-density theorem. Quite the opposite: the example exploits the fact that an arbitrarily small global count may be concentrated into a growing microscopic cluster at a lacunary sequence of heights. Any argument excluding the control must use information stronger than a one-level counting function.

Finally, nothing here constructs actual zeta zeros. The spectrum need not satisfy an Euler product, a zero-detection identity, pair-correlation law, explicit-formula compatibility beyond the coefficient kernel being tested, or any determinant/positivity condition that might couple nearby zeros. Those are precisely possible source-specific inputs left open by the matched control.

## 6. Prior-art boundary

The finite factorization in (24) is elementary harmonic analysis, not a novelty claim about exponential polynomials. A targeted audit checked classical Riesz-product constructions and Turan-type lower bounds for exponential sums. Finite Riesz products likewise expand a product into exponentially many Fourier terms, while Turan and later refinements show lower bounds under other coefficient, frequency, or sampling hypotheses. None of those results is used here, and none supplies an unconditional zeta-specific restriction preventing the geometrically weighted microscopic cluster above.

The zeta-side audit again includes Maynard--Pratt's half-isolated-zero method, whose zero detector is sensitive to vertical clustering. It does not give an unconditional minimum separation or bounded-occupancy theorem for arbitrary off-critical reciprocal-scale boxes. The present control therefore does not collide with the local-zero literature already audited in `RE-131`--`RE-132`.

No external theorem is load-bearing in the proof: the contraction (11)--(13), subset-product identity (24), coefficient stability, and lacunary embedding are all derived directly. `SOURCES.md` therefore needs no new dependency. The line-specific delta is the embedding of a growing finite-product cancellation pattern into the exact Robin/CA subedge coefficient law while retaining simplicity, zeta symmetries, a dominant algebraic atom, fixed-relative-window hiding, and arbitrarily slow one-level off-critical growth.

## 7. Research effect

`RE-132` left macroscopic visibility as a plausible escape from its two-mode matched control. `RE-133` removes that escape at the level of the formal coefficient-and-symmetry class. Even if one proves that a Robin/CA subedge packet is tiny throughout `[(1-kappa)U,(1+kappa)U]`, the necessary `RE-131` cancelling geometry can be realized by an arbitrarily sparse simple spectrum once a slowly growing microscopic cluster is allowed.

Accordingly, the implication

\[
\text{macroscopic packet hiding}
+
\text{arbitrarily strong one-level zero sparsity}
\Longrightarrow
\text{contradiction}
\tag{44}
\]

is false in the matched class.

The finite-edge branch is now pinned to a more source-specific question: can actual off-critical zeta zeros realize growing reciprocal-scale clusters whose horizontal damping and vertical phases cooperate in this way? A successful closure must impose a local occupancy/correlation restriction, a zeta-specific zero-detection or explicit-formula compatibility, or another arithmetic relation that destroys the subset-product mechanism. Merely strengthening `N(sigma,T)`, extracting a stronger dominant atom, or obtaining a fixed-relative observation window does not suffice by itself.