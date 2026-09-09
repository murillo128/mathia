# ANF-143 — odd dilations make positive-annihilator slack and span budgets summable

**Status:** `EXACT-DERIVED + POSITIVE-TRANSLATION-CASCADE + ODD-DILATION + ALMOST-PERIODIC-RECURRENCE + FIRST-RETURN-BOUND + SUMMABLE-SLACK-SPEND + SUMMABLE-SPAN + POSITIVE-RESIDUAL-SLACK + SLOW-DIAGONAL`. `ANF-133` shows that a finite critical skeleton can be annihilated by a positive binomial translation polynomial and retuned at a first positive repetition density, but the canonical construction fixes the smallest half-turn shifts. `ANF-138` shows that arbitrary finite-depth conditioning losses can be absorbed by a slow diagonal, while `ANF-141`--`ANF-142` isolate the finite-`A` consequences conditional on a positive residual slack. The remaining construction question is whether the positive-translation class itself can force that residual slack to stay positive without paying superlinear physical span.

It can. At any fixed source-critical stage, multiply every canonical half-turn shift by the same sufficiently large **odd** integer `ell`. The old critical skeleton is still annihilated exactly, but almost-periodic recurrence supplies a positive crest of the dilated annihilator within `O(ell^{-1})` of an old nondegenerate maximum. The old pressure loses only `O(ell^{-2})` there, so the actual first positive return density satisfies

\[
\boxed{0<\theta_\ell\le C_G\ell^{-2}.}
\tag{1}
\]

The constant may depend arbitrarily badly on the frozen stage; no depth-uniform estimate is required. Consequently one can choose a different finite odd dilation at each stage so that both the actual slack spend and the density-weighted physical translation span are summable. This constructs one infinite same-profile positive cascade with

\[
\boxed{\inf_d\delta_d>0,\qquad
\sum_{d\ge1}\theta_d\ell_d\sum_{j=1}^{J_{d-1}}\tau_{j,d-1}<\infty.}
\tag{2}
\]

After returning to the integer exponents `floor(theta_d A)` and applying the slow-diagonal selection of `ANF-138`, there is an unbounded physical depth `D(A)->infinity` for which the source remains `exp(o(A))`-comparable to the base source, a fixed central notch stays exponentially dark, and the complete annihilator contribution has `O(A)` support span. Thus **positive residual slack and linear support span are not existential obstructions inside the positive-translation cascade class**. This does not determine the residual slack of the original minimal-shift recurrence and does not yet prove that the resulting source-heavy family is a fatal non-excisable Montgomery--Taylor near-extremizer.

## 1. Odd dilation preserves exact annihilation and the first positive return

Fix one finite source-critical stage of the `ANF-133` architecture. Its limiting pressure `G` satisfies

\[
G(\alpha)\le0,
\qquad
\sup_{0\le\alpha<1}G(\alpha)=0,
\qquad
G(0)=-\delta<0,
\tag{3}
\]

and its critical skeleton is a finite nonempty set of interior nondegenerate maxima

\[
K=\{\xi_1,\ldots,\xi_J\}\subset(0,1).
\tag{4}
\]

Put

\[
\tau_j:=\frac1{2\xi_j},
\qquad
Q(x):=\prod_{j=1}^{J}\left(1+e^{-2\pi i\tau_jx}\right).
\tag{5}
\]

For an odd integer `ell>=1`, define

\[
Q_\ell(\alpha):=Q(\ell\alpha).
\tag{6}
\]

Oddness is exactly the condition needed to retain the old zeros. At `alpha=xi_j`, the `j`th factor in (6) is

\[
1+e^{-2\pi i\tau_j\ell\xi_j}
=1+e^{-\pi i\ell}=0,
\tag{7}
\]

while

\[
Q_\ell(0)=2^J.
\tag{8}
\]

For `theta>=0`, let

\[
G_{\ell,\theta}(\alpha)
:=G(\alpha)+2\theta\log|Q_\ell(\alpha)|
\tag{9}
\]

and

\[
M_\ell(\theta)
:=\sup_{0\le\alpha<1}G_{\ell,\theta}(\alpha).
\tag{10}
\]

For every fixed odd `ell`, the `ANF-133` first-return argument applies without change. Near each old nondegenerate maximum, `G` has a negative quadratic upper bound while `Q_ell` has a zero of positive finite order; away from fixed neighborhoods of the old maxima, `G` has a fixed negative gap and `|Q_ell|<=2^J`. Hence

\[
M_\ell(\theta)<0
\tag{11}
\]

for all sufficiently small `theta>0`.

The origin-saturation density is independent of `ell`:

\[
\theta_0=\frac{\delta}{2J\log2}.
\tag{12}
\]

At `theta_0`, equation (8) gives `G_{ell,theta_0}(0)=0`. Every positive binomial has zero logarithmic-modulus derivative at the origin, so

\[
(G_{\ell,\theta_0})'_+(0)=G'_+(0)=1.
\tag{13}
\]

Therefore `M_ell(theta_0)>0`. Convexity and the same continuity argument used in `ANF-133` give a first strictly positive return

\[
\boxed{
\theta_\ell
:=\inf\{\theta>0:M_\ell(\theta)\ge0\}
\in(0,\theta_0),
\qquad
M_\ell(\theta_\ell)=0.
}
\tag{14}
\]

Thus odd dilation changes the location and cost of the retuning, but not its admissibility.

## 2. Compact phase recurrence gives the sharp `O(ell^-2)` return cost

The key estimate is a finite-dimensional recurrence fact for the frozen polynomial `Q`. Fix any

\[
1<q_0<2^J.
\tag{15}
\]

Consider the continuous homomorphism

\[
\Phi(t)
=\left(e^{-2\pi i\tau_1t},\ldots,e^{-2\pi i\tau_Jt}\right)
\in\mathbb T^J
\tag{16}
\]

and its compact orbit closure

\[
H:=\overline{\Phi(\mathbb R)}\subset\mathbb T^J.
\tag{17}
\]

No rational-independence hypothesis is imposed: `H` is the actual closed subgroup generated by the frequencies. The set

\[
U:=\left\{z\in H:\prod_{j=1}^{J}|1+z_j|>q_0\right\}
\tag{18}
\]

is an open neighborhood of the identity because the product there equals `2^J`. Since `Phi(R)` is dense in `H`, translates of `U` by points of `Phi(R)` cover `H`; compactness gives finitely many times `t_1,...,t_m` whose translates already cover it. Hence there is a finite constant

\[
L:=\max_i|t_i|<\infty
\tag{19}
\]

such that for **every** real `x` one can choose a correction `u` with `|u|<=L` and

\[
\boxed{|Q(x+u)|>q_0.}
\tag{20}
\]

This is the exact recurrence input needed below; it is the elementary compact-group form of the classical relative-density property of finite almost-periodic trigonometric sums.

Choose any old maximum `xi in K` and apply (20) at `x=ell xi`. There is `u_ell` with `|u_ell|<=L` such that

\[
|Q(\ell\xi+u_\ell)|>q_0.
\tag{21}
\]

Set

\[
\alpha_\ell:=\xi+\frac{u_\ell}{\ell}.
\tag{22}
\]

For sufficiently large `ell`, this point remains inside the same smooth zero-free chamber of the inherited stage. Since `xi` is a nondegenerate maximum, a local Taylor lower bound gives a finite constant `C>0` such that

\[
G(\xi+h)\ge-C h^2
\tag{23}
\]

for all sufficiently small `h`. Therefore

\[
G(\alpha_\ell)
\ge-\frac{CL^2}{\ell^2},
\qquad
|Q_\ell(\alpha_\ell)|
=|Q(\ell\xi+u_\ell)|>q_0.
\tag{24}
\]

Evaluate (9) at this one point. If

\[
\bar\theta_\ell
:=\frac{CL^2}{2\log q_0}\,\ell^{-2},
\tag{25}
\]

then

\[
G_{\ell,\bar\theta_\ell}(\alpha_\ell)\ge0,
\tag{26}
\]

so `M_ell(bar theta_ell)>=0`. By the definition of the first positive return,

\[
\boxed{
0<\theta_\ell
\le
\frac{CL^2}{2\log q_0}\,\ell^{-2}
=:C_G\ell^{-2}.
}
\tag{27}
\]

An earlier return only makes the estimate stronger. The proof uses no quantitative Diophantine approximation and no independence of the `tau_j`; all arithmetic relations among the shifts are absorbed into the compact subgroup `H` and the finite recurrence constant `L`.

## 3. The actual first-return spends can be made summable at every stage

Return to the infinite stagewise construction. Let stage `0` be any source-critical seed of the `ANF-129`/`ANF-133` family and write

\[
\delta_0=f_\gamma-2R_0>0.
\tag{28}
\]

Choose in advance positive sequences `(epsilon_d)` and `(zeta_d)` such that

\[
\sum_{d\ge1}\varepsilon_d<\delta_0,
\qquad
\sum_{d\ge1}\zeta_d<\infty.
\tag{29}
\]

Suppose stages through `d-1` have been constructed. Their critical skeleton

\[
K_{d-1}=\{\xi_{1,d-1},\ldots,\xi_{J_{d-1},d-1}\}
\tag{30}
\]

is finite, interior, and nondegenerate, and the canonical half-turn shifts

\[
\tau_{j,d-1}=\frac1{2\xi_{j,d-1}}
\tag{31}
\]

are finite. Apply (27) to this **frozen** stage. For all sufficiently large odd `ell`, its actual first-return density obeys

\[
\theta_d(\ell)\le C_{d-1}\ell^{-2}
\tag{32}
\]

with some finite stage constant `C_{d-1}`.

Because the two costs then scale respectively like `ell^-2` and `ell^-1`, choose one finite odd `ell_d` so large that the actual first-return density `theta_d:=theta_d(ell_d)` satisfies simultaneously

\[
\boxed{
2\theta_dJ_{d-1}\log2\le\varepsilon_d,
}
\tag{33}
\]

and

\[
\boxed{
\theta_d\ell_d
\sum_{j=1}^{J_{d-1}}\tau_{j,d-1}
\le\zeta_d.
}
\tag{34}
\]

No freely invented density is substituted here: `theta_d` is the actual first positive pressure return of the dilated stage.

The output is again an admissible stage of the same architecture. On every zero-free cell, dilation changes a binomial curvature only by the positive square of the frequency:

\[
\frac{d^2}{d\alpha^2}
\log\left|1+e^{-2\pi i\ell_d\tau\alpha}\right|
=-(\pi\ell_d\tau)^2
\sec^2(\pi\ell_d\tau\alpha)<0.
\tag{35}
\]

Together with the strictly negative base/digit curvature already used in `ANF-133`, this leaves at most one maximizer in each of finitely many zero-free cells, and every maximizer is nondegenerate. The first-return point is interior by the same origin and `alpha->1` arguments as before. Thus the induction can continue indefinitely.

Let

\[
s_d:=2\theta_dJ_{d-1}\log2
=\delta_{d-1}-\delta_d.
\tag{36}
\]

Summing (33) gives

\[
\boxed{
\delta_d
=\delta_0-\sum_{r=1}^{d}s_r
\ge
\delta_0-\sum_{r\ge1}\varepsilon_r
=: \delta_*>0
}
\tag{37}
\]

for every depth. Therefore

\[
\boxed{\delta_\infty\ge\delta_*>0.}
\tag{38}
\]

Likewise, summing (34) gives the claimed finite density-weighted annihilator span,

\[
\boxed{
\sum_{d\ge1}
\theta_d\ell_d
\sum_j\tau_{j,d-1}
\le\sum_{d\ge1}\zeta_d<\infty.
}
\tag{39}
\]

This is a constructive existence theorem for a positive-residual-slack cascade. It says nothing about the value of `delta_infinity` for the original undilated recurrence `ell_d=1`.

## 4. Integer physical packets retain source and have uniformly linear span

At a fixed finite depth `d`, implement each selected layer by the actual integer repetition count

\[
m_{r,A}:=\lfloor\theta_rA\rfloor,
\qquad 1\le r\le d.
\tag{40}
\]

Every chosen `ell_r`, every shift, every critical cell, and every local conditioning constant is finite once `d` is fixed. The fixed-depth argument of `ANF-133` therefore applies to this dilated variant as well: the ideal exponent has finitely many nondegenerate critical maxima, the floor changes the multiplier at those maxima by only bounded fixed-depth factors, and one-dimensional Laplace localization yields

\[
0<c_d\le
\frac{E_0(X_A^{(d)})}{E_A}
\le C_d<\infty
\tag{41}
\]

for all sufficiently large `A`.

Now apply the slow threshold construction of `ANF-138`, enlarging the depth-`d` threshold additionally so that every retained layer is physically active,

\[
A\theta_r\ge1
\qquad(1\le r\le d),
\tag{42}
\]

and so that the finitely many dilation-dependent chamber widths, shifts, Hessians, and floor constants of that prefix are absorbed. This gives a nondecreasing depth

\[
D(A)\longrightarrow\infty
\tag{43}
\]

with

\[
\boxed{
\log\frac{E_0(X_A^{(D(A))})}{E_A}=o(A).
}
\tag{44}
\]

The support bound is stronger than the generic `A^{1+o(1)}` bound needed for the canonical cascade. A single copy of the stage-`d` dilated annihilator has maximal translation

\[
\ell_d\sum_j\tau_{j,d-1}.
\]

Because `m_{d,A}<=theta_dA`, equations (34) and (39) give, for every finite terminal depth,

\[
\begin{aligned}
\operatorname{Span}_{\rm ann}(D,A)
&\le
\sum_{d=1}^{D}m_{d,A}\ell_d
\sum_j\tau_{j,d-1}\\
&\le
A\sum_{d=1}^{D}\theta_d\ell_d
\sum_j\tau_{j,d-1}\\
&\le A\sum_{d\ge1}\zeta_d.
\end{aligned}
\tag{45}
\]

Hence

\[
\boxed{\operatorname{Span}_{\rm ann}(D(A),A)=O(A).}
\tag{46}
\]

The `ANF-129` seed itself also has `O(A)` span: it contains `Theta(A)` digit levels with fixed per-level translation diameter. Adding the seed therefore leaves the complete physical packet at `O(A)` horizontal span.

The positive residual slack also freezes a notch without requiring a uniform Laplace constant. For the physical cascade, positivity gives `|P(alpha)|<=P(0)` for every translation polynomial. Its physical copy rate is no larger than the corresponding ideal rate, so using the base inequality `F_gamma(alpha)<=alpha`,

\[
G_A^{\rm phys}(\alpha)
\le \alpha-\delta_*
\tag{47}
\]

on the exponential scale, up to the already absorbed `o(1)` seed/floor perturbations. Thus for every fixed

\[
0<\eta<\delta_*,
\tag{48}
\]

comparison with (44) gives

\[
\boxed{
\limsup_{A\to\infty}
\frac1A\log
\frac{E_\eta(X_A^{(D(A))})}
{E_0(X_A^{(D(A))})}
\le \eta-\delta_*<0.
}
\tag{49}
\]

Finally, the ideal copy rate satisfies

\[
R_d=\frac{f_\gamma-\delta_d}{2}
\le\frac{f_\gamma-\delta_*}{2}
<\frac{f_\gamma}{2}.
\tag{50}
\]

Combining this fixed exponential cardinality margin with (44) preserves the same source-heavy affine separation as `ANF-138`. The odd-dilation freedom therefore buys residual slack and linear span without consuming the source-to-cardinality budget.

## 5. Prior-art boundary, adversarial controls, and consequence

The recurrence lemma (20) is classical in mechanism. Finite trigonometric/exponential polynomials are Bohr almost-periodic, and their almost-periods are relatively dense. The compact orbit-closure proof above is included so that no external recurrence theorem or Diophantine approximation is load-bearing. A directed prior-art audit found the expected classical almost-periodic/compact-group framework, but no result that supplies the Mathia-specific combination of odd exact annihilation, first-positive-return pressure tuning, the `O(ell^-2)` density law, and simultaneous summable slack/span budgets. No novelty is claimed for almost-periodicity itself, and `SOURCES.md` gains no new dependency.

Several failure modes are explicitly excluded. The proof does not assume rational independence of the critical shifts. It does not replace the first return by an arbitrary small repetition density: (27) is an upper bound on the **actual** first positive return. Large `ell_d` is chosen only after the preceding finite stage is frozen; the later physical diagonal then waits until `A` is large enough for every retained floor exponent to be nonzero and for the `ell_d^{-1}` chamber scale to be resolved. The resulting theorem is existential and non-effective in depth, exactly as in `ANF-138`.

The construction also does not solve the original minimal-shift recurrence, and it does not establish fatality for the Montgomery--Taylor fixed-notch envelope. The produced family is source-heavy, has a fixed dark notch, positive residual slack, and linear span, but a final global argument must still decide whether the complete block is non-excisable under the affine normalization or whether a source decomposition/oversource mechanism neutralizes it. Those are genuinely downstream questions rather than hidden failures of the slack or support budgets.

**Consequence for `analytic_frontier`.** The proposed odd-dilation escape is real. Within the same-profile positive-translation class, the freedom to choose large odd multiples of the half-turn annihilator shifts lets each critical retuning cost quadratically less copy-rate slack while costing only linearly more translation distance. The two budgets can therefore be made summable simultaneously. Any remaining no-go theorem for the frozen-notch route must use information beyond “an infinite positive cascade necessarily saturates its copy-rate slack” or “preserving slack necessarily forces superlinear translation span.”