# NB-144 — Euler-product Poisson mass forces logarithmic confluence away from the one-line

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + EULER-PRODUCT + LOG-DERIVATIVE-POISSON-BUDGET + LOCAL-OCCUPANCY + NEAR-ONE-SUBLOG-RANK + XI-CONTROL-SEPARATION + TARGET-AWARE-CONFLUENCE-SPLICE + METHOD-BOUNDARY`.

`NB-143` separates generic `xi`-type analytic realizability from arithmetic realizability: an order-one entire completion with the exact zeta functional equation can still contain the logarithmic-rank target-poor packets of `NB-140`, but Hamburger prevents that particular control from also carrying the ordinary zeta Dirichlet series. The remaining question is whether one can extract any **quantitative local zero law** directly from the actual prime-side source before asking for the much stronger `o(log G)` short-increment theorem isolated by `NB-142`.

There is such a law, and it is already visible from the absolutely convergent Euler product to the right of `Re s=1`.

Let

\[
0<a<\frac12,
\qquad
B>0,
\qquad
h_G:=G^{-B},
\tag{1}
\]

and let `t_G in [G,2G]`. Suppose the actual zeta divisor contains `d_G` zeros, counted with multiplicity, in the right-half cell

\[
\mathcal C_G(a,t_G)
:=
\left\{
\rho=\beta+i\gamma:
\left|\beta-\left(\frac12+a\right)\right|\le h_G,
\quad
|\gamma-t_G|\le h_G
\right\}.
\tag{2}
\]

Then

\[
\boxed{
 d_G
 \le
 \left(\frac18-\frac{a^2}{2}+o(1)\right)\log G.
}
\tag{3}
\]

Equivalently, if the cell is centered at `beta_0=1-epsilon` with fixed `0<epsilon<1/2`, then

\[
\boxed{
 d_G
 \le
 \left(\frac{\epsilon(1-\epsilon)}2+o(1)\right)\log G.
}
\tag{4}
\]

The mechanism is a positive Poisson-mass budget for the zero divisor. For `sigma>1`, every nontrivial zero contributes positively to

\[
\sum_\rho
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(t-\gamma)^2},
\tag{5}
\]

while the Hadamard/logarithmic-derivative identity gives

\[
\sum_\rho
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(t-\gamma)^2}
=
\frac12\log |t|
+
\Re\frac{\zeta'}{\zeta}(\sigma+it)
+O(1).
\tag{6}
\]

The arithmetic input is that on `Re s>1`

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\tag{7}
\]

so

\[
\left|
\frac{\zeta'}{\zeta}(\sigma+it)
\right|
\le
-\frac{\zeta'}{\zeta}(\sigma)
=
\frac1{\sigma-1}+O(1)
\qquad(\sigma\downarrow1).
\tag{8}
\]

Taking `sigma_G=1+(log G)^(-1/2)` makes the prime-side term `o(log G)`. Functional-equation symmetry then charges every right-half zero in `(2)` together with its left-half partner at the same ordinate. The asymptotic charge of one such pair is

\[
\frac1{\frac12-a}
+
\frac1{\frac12+a}
=
\frac1{\frac14-a^2}.
\tag{9}
\]

Comparing `(5)`--`(9)` gives `(3)`.

This does not yet yield the `o(log G)` worst-cell law needed to close `NB-140` at a fixed interior real part. The coefficient in `(3)` is positive for every fixed `a<1/2`. But it is a genuine arithmetic restriction absent from the `NB-143` synthetic completion, and it becomes sublogarithmic automatically when the cell center itself approaches the one-line. More generally, if a right-half cell is centered at

\[
\beta_G=1-\epsilon_G,
\qquad
\epsilon_G\log G\longrightarrow\infty,
\qquad
h_G=o(\epsilon_G),
\tag{10}
\]

then choosing

\[
\sigma_G-1
=
\sqrt{\frac{\epsilon_G}{\log G}}
\tag{11}
\]

gives

\[
\boxed{
 d_G
 \le
 \left(\frac12+o(1)\right)
 \epsilon_G(1-\epsilon_G)\log G.
}
\tag{12}
\]

Hence every actual packet whose center satisfies `epsilon_G -> 0` has `d_G=o(log G)` as soon as `(10)` holds. The Vinogradov--Korobov zero-free region already imported by this line guarantees `epsilon_G log G -> infinity` for any actual zero approaching `Re s=1`, so logarithmic-rank confluence cannot drift into the one-line boundary layer.

The strongest use of `(3)` in the present line is as an explicit separator between `xi`-side and prime-side realizability. For example, take

\[
a=0.49,
\qquad
c=0.01,
\qquad
B=0.02.
\tag{13}
\]

Then

\[
\frac18-\frac{a^2}{2}=0.00495<c,
\tag{14}
\]

while

\[
B
>
c\log\!\left(\frac4a-3\right)
\approx0.01642,
\tag{15}
\]

and `c<0.05038`. Thus the `NB-143` canonical-product construction can realize a `c log G` target-poor packet with these parameters while respecting the functional equation, the explicit zero-count envelope, the imported zero-density envelope and the Vinogradov--Korobov region. Equation `(3)` proves that the actual zeta Euler-product source cannot realize that same packet. This is the first quantitative local discriminator in the current confluence chain that uses arithmetic half-plane structure rather than another global zero envelope.

The discriminator is not yet complete. For every fixed `a<1/2` there remains a positive overlap

\[
0<c<\frac18-\frac{a^2}{2}
\tag{16}
\]

in which `NB-140`'s target-poor logarithmic-rank geometry is not excluded by the Poisson budget. The live problem therefore narrows rather than closes: a successful source theorem must improve the fixed-interior `O(log G)` occupancy law to `o(log G)`, exploit additional prime-side information beyond the one-point logarithmic derivative, or prove directly that the surviving crowded actual cells are Nyman-target-bearing.

## 1. The exterior logarithmic derivative gives a positive zero budget

For `s=sigma+it` with `1<sigma<=2` and `|t|>=3`, the standard Hadamard logarithmic derivative for the completed zeta function, together with Stirling's formula for the gamma factor, gives uniformly

\[
\Re\frac{\zeta'}{\zeta}(s)
=
\sum_\rho
\Re\frac1{s-\rho}
-
\frac12\log |t|
+O(1),
\tag{17}
\]

where zeros are counted with multiplicity and the real zero sum is absolutely convergent. Since every nontrivial zero satisfies `0<beta<1`, for `sigma>1`

\[
\Re\frac1{s-\rho}
=
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(t-\gamma)^2}
>0.
\tag{18}
\]

Thus `(17)` is not merely a representation: it is a positive budget in which any selected zero packet can be discarded from the left side without cancellation.

The actual arithmetic source enters through `(7)`. Absolute convergence implies

\[
\left|
\frac{\zeta'}{\zeta}(\sigma+it)
\right|
\le
\sum_{n\ge1}\frac{\Lambda(n)}{n^\sigma}
=
-\frac{\zeta'}{\zeta}(\sigma).
\tag{19}
\]

The Laurent expansion of zeta at one gives

\[
-\frac{\zeta'}{\zeta}(1+\delta)
=
\frac1\delta+O(1).
\tag{20}
\]

Put

\[
L:=\log G,
\qquad
\delta_G:=L^{-1/2},
\qquad
s_G:=1+\delta_G+it_G.
\tag{21}
\]

Since `t_G` is comparable to `G`, equations `(17)`--`(21)` give

\[
\boxed{
\sum_\rho
\frac{1+\delta_G-\beta}
{(1+\delta_G-\beta)^2+(t_G-\gamma)^2}
\le
\frac12L+O(\sqrt L).
}
\tag{22}
\]

No zero-density theorem, spacing hypothesis, simplicity assumption or cancellation among zeros is used in `(22)`.

## 2. Functional-equation pairs convert the budget into a radial occupancy tax

Take one zero `rho_j=beta_j+i gamma_j` in `(2)`. Since eventually `h_G<a/2`, it lies strictly in the right half of the critical strip. Its functional-equation partner

\[
\widetilde\rho_j
=
1-\overline{\rho_j}
=
(1-\beta_j)+i\gamma_j
\tag{23}
\]

is distinct and has the same multiplicity.

For the right member,

\[
1+\delta_G-\beta_j
=
\frac12-a+o(1),
\qquad
|t_G-\gamma_j|\le h_G=o(1),
\tag{24}
\]

and for the left partner,

\[
1+\delta_G-(1-\beta_j)
=
\frac12+a+o(1).
\tag{25}
\]

Their combined contribution to `(22)` is therefore uniformly

\[
\begin{aligned}
&
\frac{1+\delta_G-\beta_j}
{(1+\delta_G-\beta_j)^2+(t_G-\gamma_j)^2}
+
\frac{\delta_G+\beta_j}
{(\delta_G+\beta_j)^2+(t_G-\gamma_j)^2}
\\[3pt]
&\hspace{25mm}
=
\frac1{\frac12-a}
+
\frac1{\frac12+a}
+o(1)
=
\frac1{\frac14-a^2}+o(1).
\end{aligned}
\tag{26}
\]

All other zeros contribute nonnegatively. Hence `(22)` and `(26)` give first `d_G=O(L)` and then, with the uniform `o(1)` error summed over those `O(L)` packet members,

\[
d_G
\left(
\frac1{\frac14-a^2}+o(1)
\right)
\le
\frac12L+o(L).
\tag{27}
\]

This is exactly `(3)`.

In terms of the distance `epsilon=1-beta_0=1/2-a` from the one-line,

\[
\frac18-\frac{a^2}{2}
=
\frac{\epsilon(1-\epsilon)}2,
\tag{28}
\]

which gives `(4)`. The factor `epsilon(1-epsilon)` is the reciprocal of the total Poisson charge of the functional-equation pair when observed from the boundary point `sigma=1+`.

## 3. Moving toward the one-line forces sublogarithmic packet rank

The fixed-`a` proof can be made uniform when the packet itself approaches `Re s=1`. Let the right-half center be

\[
\beta_G=1-\epsilon_G,
\qquad
0<\epsilon_G\le\frac12,
\tag{29}
\]

and suppose `(10)`. Set

\[
\delta_G
:=
\sqrt{\frac{\epsilon_G}{L}}.
\tag{30}
\]

Then

\[
\frac{\delta_G}{\epsilon_G}
=
\frac1{\sqrt{\epsilon_GL}}
\longrightarrow0,
\qquad
\delta_GL
=
\sqrt{\epsilon_GL}
\longrightarrow\infty.
\tag{31}
\]

Consequently `(19)`--`(20)` give

\[
\left|
\frac{\zeta'}{\zeta}(1+\delta_G+it_G)
\right|
=O(\delta_G^{-1})
=o(L),
\tag{32}
\]

while each packet zero plus its reflected partner contributes

\[
\left(1+o(1)\right)
\left(
\frac1{\epsilon_G}
+
\frac1{1-\epsilon_G}
\right)
=
\frac{1+o(1)}{\epsilon_G(1-\epsilon_G)}.
\tag{33}
\]

The same positive-budget comparison proves `(12)`.

For actual zeta zeros, the Vinogradov--Korobov zero-free region gives, at height comparable to `G`,

\[
\epsilon_G
\gg
(\log G)^{-2/3}
(\log\log G)^{-1/3}.
\tag{34}
\]

Thus `epsilon_G L -> infinity`, so `(12)` applies to every such near-one packet whose horizontal radius is polynomially small. In particular, if `epsilon_G -> 0`, then

\[
\boxed{d_G=o(\log G).}
\tag{35}
\]

At the zero-free boundary scale itself, `(12)` gives the indicative ceiling

\[
d_G
=
O\!\left(
(\log G)^{1/3}
(\log\log G)^{-1/3}
\right),
\tag{36}
\]

up to the fixed zero-free-region constant. The exact exponent in `(36)` is not the point; the source distinction is that logarithmic-rank clustering is impossible in every boundary layer whose distance to `Re s=1` tends to zero.

## 4. The Euler-product law excludes concrete `NB-143` xi-type controls

The `NB-143` construction is flexible in `a,c,B` subject to

\[
0<a<\frac12,
\qquad
0<c<0.05038,
\qquad
B>c\log\!\left(\frac4a-3\right).
\tag{37}
\]

Choose the values `(13)`. Since

\[
\frac4{0.49}-3
\approx5.163265,
\qquad
0.01\log(5.163265)
\approx0.01642<0.02,
\tag{38}
\]

all hypotheses of `NB-143` are met. Its one order-one `Xi_*` can therefore contain infinitely many packets of rank

\[
d_G=(0.01+o(1))\log G
\tag{39}
\]

inside the corresponding polynomial cells while preserving every `xi`-side analytic and coarse-zero constraint audited there.

But `(3)` gives for the actual zeta source at the same horizontal location

\[
d_G
\le
(0.00495+o(1))\log G.
\tag{40}
\]

Thus `(39)` is impossible for zeta. This is a strict matched-control separation:

\[
\boxed{
\text{xi-type completion + FE + coarse zero laws}
\not\Rightarrow
\text{Euler-product Poisson budget}.
}
\tag{41}
\]

The distinction is quantitative, not merely the qualitative Hamburger statement that an exact ordinary Dirichlet series would force `Z_*=zeta`.

The new bound also has a complementary limitation. The Bellotti--Wong zero-count envelope used in `NB-142` gives

\[
d_G
\le
(0.10076+o(1))\log G
\tag{42}
\]

for a right-half polynomial cell after symmetry. The Euler-product bound `(3)` is stronger than `(42)` only when

\[
a
>
\sqrt{2(0.125-0.10076)}
\approx0.22018.
\tag{43}
\]

Near the critical line the explicit global count remains numerically sharper; toward the one-line the prime-side Poisson budget becomes progressively stronger and eventually forces sublogarithmic rank.

## 5. What this changes in the Nyman obstruction

For the fixed-`a` geometry of `NB-140`, target-poor confluence requires only

\[
0<c<\frac18,
\qquad
B>c\log\!\left(\frac4a-3\right).
\tag{44}
\]

The actual zeta source now imposes the additional necessary condition

\[
\boxed{
 c
\le
\frac18-\frac{a^2}{2}
=
\frac{(1/2-a)(1/2+a)}2.
}
\tag{45}
\]

Equivalently, a fixed-positive logarithmic rank `c log G` forces

\[
a
\le
\sqrt{\frac14-2c}+o(1),
\tag{46}
\]

so the packet center must remain a fixed distance

\[
1-\Re\rho
\ge
\frac12-
\sqrt{\frac14-2c}
+o(1)
\tag{47}
\]

away from the one-line. For small `c`, the right side is `2c+O(c^2)`.

This is real source progress: the `NB-143` matched control no longer survives all choices of horizontal location once the Euler product is used. But `(45)` leaves a positive interval of admissible `c` for every fixed `a<1/2`. Since `NB-140` remains target-poor for arbitrarily small fixed positive `c`, the current obstruction survives in the interior of the critical strip.

The next theorem therefore cannot be merely another version of the one-point exterior Poisson budget. To close the route one needs one of three genuinely stronger resources: a fixed-interior improvement from `O(log G)` to `o(log G)` as in `NB-142`; a multi-point/prime-side constraint that makes logarithmic occupancy incompatible with actual zeta arithmetic even when `(45)` holds; or a target-aware theorem showing that the surviving actual crowded cells cannot remain Nyman-target-poor.

## 6. Prior-art and novelty boundary

The analytic ingredients in `(17)`--`(20)` are classical. The Hadamard/logarithmic-derivative representation of zeta zeros and the absolutely convergent von Mangoldt series on `Re s>1` are standard tools in proofs of zero-free regions and local zero bounds. Classical and modern work on local density and clustering near the one-line, including Ramachandra's results and Révész's 2022 treatment of local density/clustering for Beurling zeta functions, lies squarely on this source-side boundary. No novelty is claimed for the generic fact that the logarithmic derivative can bound local zero concentration.

A current neighboring direction is Grigutis--Turčinskas, *Note on the positivity of the real part of the log-derivative of the Riemann xi-function near the critical line*, Lithuanian Mathematical Journal 66 (2026), 199--211, DOI `10.1007/s10986-026-09708-3`, which studies `Re xi'/xi` and zero contributions in a different, near-critical-line regime. The present argument stays on `Re s>1`, where the Euler product is absolutely convergent, and uses only the resulting positive zero budget.

The line-local contribution is the splice. `NB-140` gives an explicit logarithmic-rank **target-poor** Nyman confluence geometry; `NB-143` shows that xi-type analytic realizability still admits it; the present finding computes the first direct Euler-product occupancy tax on exactly that geometry, shows that it excludes a concrete open family of `NB-143` controls, and proves that every dangerous packet approaching the one-line loses logarithmic rank. The surviving fixed-interior overlap `(16)` is stated explicitly rather than hidden as a claimed resolution.

No new external theorem is load-bearing beyond standard identities derived in the proof and the Vinogradov--Korobov region already anchored in `SOURCES.md`, so no source-anchor change is required for this finding.

## 7. Adversarial audit

**This is not a proof of the `NB-142` short-increment law.** For fixed `a<1/2`, equation `(3)` is still `C(a) log G` with `C(a)>0`. It does not imply `o(log G)` and therefore does not eliminate all fixed-interior `NB-140` packets.

**No RH or Lindelöf input is used.** The argument evaluates the actual zeta logarithmic derivative in the half-plane of absolute Euler-product convergence. The only zero-location facts used are the critical-strip location, functional-equation symmetry and, for the moving-center corollary, the already imported unconditional Vinogradov--Korobov zero-free region.

**The prime-side term is genuinely subleading.** Choosing `sigma_G-1=L^(-1/2)` for fixed `a` gives `|zeta'/zeta|=O(sqrt L)`. In the moving-center argument, `(30)` simultaneously makes `delta_G=o(epsilon_G)` and `delta_G^(-1)=o(L)` exactly because `epsilon_G L -> infinity`.

**Multiplicity causes no loophole.** The Hadamard sum counts zeros with multiplicity, and functional-equation reflection preserves multiplicity. The estimate is therefore stronger than the simple-packet statement needed by `NB-140`.

**The factor from symmetry is not double-counted.** A right-half zero `beta+i gamma` is paired with the distinct zero `(1-beta)+i gamma`. Its complex conjugate lies near ordinate `-G` and is not used in the lower bound at `s=1+delta+i t_G`.

**Polynomial cell size is more than sufficient.** The fixed-`a` proof only needs `h_G=o(1)`. The moving-center version needs `h_G=o(epsilon_G)`. For the polynomial `NB-140` cells and any actual near-one zero allowed by Vinogradov--Korobov, this holds automatically.

**The synthetic separation is legitimate but scoped.** `NB-143` does not claim that `Xi_*` has an Euler product; indeed Hamburger forbids its ordinary zeta Dirichlet-series realization. Equations `(13)`--`(40)` use the synthetic function only as a matched control showing that the new inequality contains arithmetic information absent from the earlier analytic envelope.

**No sharpness claim is made for the coefficient.** The value `1/8-a^2/2` is the sharp coefficient produced by this one-point exterior Poisson-budget limit `sigma -> 1+`. A stronger arithmetic argument may lower it. The finding claims only the derived necessary condition and its consequences for the current matched controls.

## Outcome

Arithmetic half-plane structure begins to constrain the confluence obstruction before one reaches a full converse theorem. The actual zeta Euler product forces a right-half polynomial cell centered at `1/2+a` to contain at most

\[
\left(\frac18-\frac{a^2}{2}+o(1)\right)\log G
\]

zeros, and any such cell whose center tends to `Re s=1` has sublogarithmic rank. This excludes explicit `xi`-type controls that all previously imported zero envelopes still permit, so the distinction exposed qualitatively by `NB-143` is now quantitative.

The obstruction nevertheless survives at every fixed interior horizontal location at sufficiently small positive logarithmic rank. The live source problem is therefore sharper: **extract from the prime-side source a fixed-interior sublogarithmic occupancy law, a stronger relational constraint on crowded cells, or a direct target-bearing consequence.** The Euler product has entered the geometry, but one exterior Poisson budget does not yet close it.