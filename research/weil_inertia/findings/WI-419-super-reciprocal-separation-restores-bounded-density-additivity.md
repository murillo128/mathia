# WI-419 — super-reciprocal separation restores bounded-density Blaschke additivity

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-CONSTRAINT`.

**Parents:** WI-410, WI-417, WI-418.

## Claim

For the translated Burnol--Kunik Blaschke kernel

\[
q_{a,b}(\gamma,d)
=\frac12\log\frac{(\gamma-b)^2+(a+d)^2}{(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\]

consider a finite set of same-depth targets

\[
E=\{(\gamma_j,d):1\le j\le N\},
\qquad
S:=\min_{i\ne j}|\gamma_i-\gamma_j|,
\]

and coefficient measures \(\nu\) on \((0,\infty)\times\mathbb R\) whose total-variation density is bounded by \(B\):

\[
\frac{d|\nu|}{da\,db}\le B.
\]

Let \(M_B(E,Q)\) be the infimum of \(\|\nu\|_{\rm TV}\) among measures giving response at least \(Q>0\) at every target, and let

\[
C_d(Q):=M_B(d,Q)
\]

be the exact one-target capacity computed in WI-417. Write

\[
r_d(Q):=\sqrt{\frac{C_d(Q)}{\pi B}},
\qquad
\kappa(d,S):=\operatorname{arsinh}\frac{2d}{S}.
\]

If

\[
S>2r_d(Q)
\quad\text{and}\quad
Q-NC_d(Q)\kappa(d,S)>0,
\]

then the multi-target capacity obeys the explicit two-sided estimate

\[
\boxed{
N\,C_d\!\left(Q-NC_d(Q)\kappa(d,S)\right)
\le M_B(E,Q)
\le N\,C_d(Q).
}
\]

Consequently, for fixed \(B,Q>0\), if \(d\to0\) and the target number \(N=N(d)\) and minimum separation \(S=S(d)\) satisfy

\[
\frac{N}{dS}\longrightarrow0,
\]

then

\[
\boxed{
M_B(E,Q)
\sim N\,C_d(Q)
\sim \frac{NQ^2}{4\pi B d^2}.
}
\]

For fixed \(N\), the simpler condition \(dS\to\infty\) is sufficient. Thus the reciprocal-depth scale \(1/d\) is a genuine two-sided reuse threshold for this bounded-density model: WI-418 shows that targets lying inside an ordinate pocket of width \(o(1/d)\) can asymptotically share one one-target budget, whereas sufficiently separated targets with \(S\gg1/d\) have asymptotically additive costs.

This is a theorem about the bounded-density translated-Blaschke capacity model. It does **not** by itself establish that hypothetical off-line zeta zeros have the required reciprocal-depth separation, nor that the zeta source side supplies a uniform density cap \(B\).

## 1. Exact tail envelope away from a target ordinate

For vertical offset

\[
r=|\gamma-b|>0,
\]

WI-410's scale optimization applies after translating the ordinate. Since

\[
q_{a,b}(\gamma,d)
=\operatorname{artanh}\!\left(
\frac{2ad}{r^2+a^2+d^2}
\right),
\]

and \(\operatorname{artanh}\) is increasing, maximize

\[
z(a)=\frac{2ad}{r^2+a^2+d^2}.
\]

Differentiation gives

\[
z'(a)
=\frac{2d(r^2+d^2-a^2)}{(r^2+a^2+d^2)^2},
\]

so the unique maximizer is \(a=\sqrt{r^2+d^2}\). Hence

\[
\boxed{
\sup_{a>0}q_{a,b}(\gamma,d)
=\operatorname{arsinh}\frac d r.
}
\]

In particular, any source point with \(|b-\gamma|\ge S/2\) contributes at most

\[
\kappa(d,S)=\operatorname{arsinh}\frac{2d}{S}
\]

per unit coefficient mass.

This exact off-pocket tail estimate is the only cross-target interaction estimate needed below.

## 2. Reduction to positive sources

The kernel is nonnegative. If a signed or complex measure \(\nu\) is feasible in modulus at all targets, then

\[
\left|\int q_{a,b}(\gamma_j,d)\,d\nu\right|
\le
\int q_{a,b}(\gamma_j,d)\,d|\nu|.
\]

The measure \(|\nu|\) has the same total variation and obeys the same density cap. Therefore signed or complex phases cannot lower the capacity and it is enough to consider positive \(\nu\).

This is the same positivity reduction used in WI-417's exact one-target optimization.

## 3. Disjoint ordinate cells force local mass

For each target define the vertical cell

\[
U_j:=\{(a,b):|b-\gamma_j|<S/2\}.
\]

The cells are pairwise disjoint, up to null boundaries. For a feasible positive source \(\nu\), write

\[
M=\nu((0,\infty)\times\mathbb R),
\qquad
m_j=\nu(U_j).
\]

At target \((\gamma_j,d)\), the contribution from \(U_j\) is at most the exact one-target response envelope corresponding to mass \(m_j\) and density cap \(B\). Equivalently, if that local contribution is at least \(q\), then WI-417 forces local mass at least \(C_d(q)\).

The complementary source lies at vertical distance at least \(S/2\), so Section 1 gives

\[
\int_{U_j^c}q_{a,b}(\gamma_j,d)\,d\nu
\le (M-m_j)\kappa(d,S)
\le M\kappa(d,S).
\]

Feasibility therefore implies

\[
\text{local response in }U_j
\ge Q-M\kappa(d,S),
\]

and whenever the right side is positive,

\[
m_j\ge C_d\!\left(Q-M\kappa(d,S)\right).
\]

Summing over the disjoint cells yields the implicit lower bound

\[
M\ge N C_d\!\left(Q-M\kappa(d,S)\right).
\]

This already shows how separation converts the one-target tariff into a many-target constraint: cross-cell reuse is limited solely by the exact tail \(\kappa(d,S)\).

## 4. Matching explicit upper bound

WI-417 identifies the exact one-target optimizer as density \(B\) on a kernel superlevel disk. Its area is \(C_d(Q)/B\), hence its radius is

\[
r_d(Q)=\sqrt{\frac{C_d(Q)}{\pi B}}.
\]

All targets have the same depth, so their optimizing disks have the same horizontal center and radii; translating a target only translates its disk vertically. If

\[
S>2r_d(Q),
\]

these \(N\) optimizer disks are disjoint. Put density \(B\) on their union. The total mass is exactly

\[
N C_d(Q).
\]

Each target receives response \(Q\) from its own disk and an additional nonnegative response from all the others. Hence

\[
\boxed{M_B(E,Q)\le N C_d(Q).}
\]

Now let \(C=C_d(Q)\). For an arbitrary feasible source of mass \(M\), either \(M>NC\), in which case

\[
M\ge NC\ge N C_d(Q-NC\kappa),
\]

or \(M\le NC\), in which case the cell estimate gives

\[
Q-M\kappa\ge Q-NC\kappa
\]

and monotonicity of \(C_d\) gives

\[
M\ge N C_d(Q-NC\kappa).
\]

This proves the displayed finite two-sided estimate whenever \(Q-NC\kappa>0\).

## 5. Shallow-depth asymptotic and growing target sets

WI-417 proved the exact quadratic bounds

\[
\frac{q^2}{4\pi B d^2}
\le C_d(q)
\le
\frac{(q+\pi Bd^2)^2}{4\pi B d^2}.
\]

For fixed \(Q>0\), therefore

\[
C_d(Q)\sim \frac{Q^2}{4\pi Bd^2},
\qquad
r_d(Q)\sim\frac{Q}{2\pi Bd}.
\]

Also

\[
\kappa(d,S)=\operatorname{arsinh}\frac{2d}{S}
\le\frac{2d}{S}.
\]

Thus

\[
NC_d(Q)\kappa(d,S)
=O\!\left(\frac{N}{dS}\right).
\]

If \(N/(dS)\to0\), then this cross-cell error tends to zero. Since \(N\ge1\), the same hypothesis forces \(dS\to\infty\), so the optimizer disks are eventually disjoint. Put

\[
\varepsilon_d:=NC_d(Q)\kappa(d,S)=o(1).
\]

The exact quadratic bounds give, without any differentiability assumption on the capacity,

\[
\frac{C_d(Q-\varepsilon_d)}{C_d(Q)}
\ge
\frac{(Q-\varepsilon_d)^2}{(Q+\pi Bd^2)^2}
\longrightarrow1.
\]

Combining this with the finite two-sided estimate proves

\[
1-o(1)
\le
\frac{M_B(E,Q)}{NC_d(Q)}
\le1.
\]

Hence

\[
M_B(E,Q)
\sim NC_d(Q)
\sim\frac{NQ^2}{4\pi Bd^2}.
\]

For fixed \(N\), this reduces to the transparent separation condition \(dS\to\infty\).

## 6. Relation to WI-418 and the scale boundary

WI-418 showed the opposite asymptotic regime. For any same-depth target cluster contained in a vertical interval of half-width \(L\), if \(Ld\to0\), then

\[
M_B(E,Q)\sim C_d(Q)
\]

independently of the number of target points. A single tangent disk of radius \(\asymp1/d\) serves the whole cluster.

The present result shows that once target spacing is much larger than that same reciprocal-depth scale, the disks decouple and the capacity becomes additive. In the fixed-\(N\) setting the two rigorous regimes are therefore

\[
\text{cluster width }o(1/d):\quad M_B(E,Q)\sim C_d(Q),
\]

versus

\[
\text{minimum spacing }\omega(1/d):\quad
M_B(E,Q)\sim N C_d(Q).
\]

This does not determine the critical crossover \(S\asymp c/d\). At that scale the cross-response remains order one and the optimal source is genuinely multi-target; neither the complete-reuse nor the additive asymptotic is expected to be exact in general.

## 7. Prior art and novelty audit

The ingredients are classical or already established in this line. The half-plane Blaschke/Green kernel and its one-scale optimization are from the Burnol--Kunik framework audited in WI-410. The density-constrained one-target optimizer in WI-417 is an application of the classical bathtub/rearrangement principle to the exact superlevel-disk geometry. Separation as the mechanism that turns analytic interpolation data into independent constraints is classical in Carleson interpolation theory; for example:

- L. Carleson, *An Interpolation Problem for Bounded Analytic Functions*, American Journal of Mathematics **80** (1958), 921--930, DOI `10.2307/2372840`;
- J. B. Garnett, *Bounded Analytic Functions*, Graduate Texts in Mathematics 236, Springer, 2007, especially the treatment of interpolating sequences and Carleson separation;
- G. Poliquin, *Superlevel sets and nodal extrema of Laplace--Beltrami eigenfunctions*, Journal of Spectral Theory **7** (2017), 111--136, DOI `10.4171/JST/157`, as neighboring prior art for Green-function superlevel optimization via the bathtub principle.

Those sources do not state the bounded-density translated-Blaschke multi-target capacity estimate proved here. The prior-art audit searched by the structures `bounded-density Green/logarithmic potential`, `multiple targets`, `separated interpolation`, `Blaschke`, and `bathtub principle`; it found classical separation/interpolation and Green-potential optimization, but no exact result matching this capacity model or its reciprocal-depth additivity threshold. No priority claim is made from that negative search.

The mathematical delta is narrower and exact: combining WI-417's one-target capacity with the sharp translated-tail envelope produces a quantitative separation theorem and proves that WI-418's budget reuse cannot persist across super-reciprocal target separation.

## 8. Boundary conditions and audit checks

The load-bearing assumptions are explicit.

- The theorem uses a common target depth \(d\). Varying depths change both optimizer radii and cross-tail scales and are not covered by the displayed symmetric estimate.
- The density cap is two-dimensional Lebesgue density in \((a,b)\), exactly as in WI-417. A weaker marginal or averaged cap need not imply the same local mass tariff.
- The kernel is nonnegative. The reduction from signed/complex measures to positive measures would fail for a genuinely sign-changing probe family.
- The explicit upper bound uses disjoint one-target optimizer disks. When \(S\asymp1/d\), those disks may overlap and the additive construction is no longer optimal.
- For growing \(N\), merely requiring \(dS\to\infty\) is insufficient for the present proof: the accumulated tail is controlled by the stronger condition \(N/(dS)\to0\).

A direct audit can falsify the result only by breaking one of three exact steps: (i) the pointwise tail supremum `sup_a q = arsinh(d/r)`; (ii) the WI-417 one-target response/capacity inversion inside each disjoint vertical cell; or (iii) the union-of-disks admissible construction. No numerical optimization or asymptotic conjecture is used in the finite estimate.

## Consequences for `weil_inertia`

The bounded-density Blaschke branch now has a sharp qualitative separation picture. Raw multiplicity in one shallow target pocket is still cheap by WI-418, but **distinct target pockets separated by much more than \(1/d\) cannot recycle the same source budget**: their costs add asymptotically, and the result remains valid for a growing number of targets provided \(N=o(dS)\).

This narrows the missing zeta-side theorem. It is no longer enough to seek a density cap \(B\) alone, and it is no longer necessary to prove pairwise additivity at arbitrary spacing. A viable defect-to-zero argument in this architecture can instead try to derive, from independent arithmetic/source information, enough shallow defects occupying reciprocal-depth-separated ordinate pockets that the additive tariff

\[
\frac{Q^2}{4\pi B}\sum_j d_j^{-2}
\]

(or an appropriate varying-depth analogue) exceeds the available source budget. The critical unresolved geometry is the intermediate \(S\asymp1/d\) regime and, more importantly, whether zeta supplies any non-oracular source regularity and target separation strong enough to enter the additive regime.