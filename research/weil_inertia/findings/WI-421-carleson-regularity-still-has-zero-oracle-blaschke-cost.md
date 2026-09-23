# WI-421 — Carleson regularity still has zero oracle Blaschke targeting cost

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

**Parents:** [WI-416](./WI-416-oracle-blaschke-targeting-has-zero-tv-infimum.md), [WI-417](./WI-417-bounded-density-restores-shallow-depth-blaschke-coercivity.md), [WI-420](./WI-420-critical-reciprocal-blaschke-crossover-is-poisson-capacity.md).

## Claim

WI-416 showed that finite total variation alone does not control target-adaptive translated Blaschke probes: on any finite discrete defect set, arbitrarily small atomic coefficients can be compensated by moving each probe arbitrarily close to its assigned logarithmic singularity. WI-417 restored coercivity by imposing the genuinely two-dimensional pointwise density cap `d|nu|/(da db) <= B`. A natural question left between those two regimes is whether a softer Hardy-space regularity, especially a Carleson-measure condition, already suffices to prevent the oracle concentration.

It does not. More generally, **every source gauge that tolerates interior Dirac atoms with locally bounded cost has the same zero-cost oracle failure as total variation**.

For

\[
q_{a,b}(\gamma,d)
=\frac12\log\frac{(\gamma-b)^2+(a+d)^2}
{(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\tag{1}
\]

let

\[
E=\{(\gamma_j,d_j):1\le j\le N\}
\subset \mathbb R\times(0,\infty)
\tag{2}
\]

be a finite target set and let `R` be a nonnegative, positively homogeneous, subadditive functional on positive finite atomic measures on the source half-plane. Suppose that for every target `z_j=(d_j,gamma_j)` there is a punctured sequence of source points `x_{j,n}->z_j` and a constant `C_j<infinity` such that

\[
R(\delta_{x_{j,n}})\le C_j
\qquad\text{for all }n.
\tag{3}
\]

Then for every `Q>0` and every `epsilon>0` there exists a positive finite atomic measure `nu` such that

\[
\boxed{
\|\nu\|_{\rm TV}<\varepsilon,
\qquad
R(\nu)<\varepsilon,
\qquad
Q_\nu(\gamma_j,d_j)\ge Q
\quad(1\le j\le N),
}
\tag{4}
\]

where

\[
Q_\nu(\gamma,d)
=\int q_{a,b}(\gamma,d)\,d\nu(a,b),
\tag{5}
\]

and all sampled kernel values can be kept finite. Hence the infimum oracle source cost is zero for any such atom-tolerant regularity.

The standard Carleson norm is an especially sharp corollary. For an interval `I subset R` write

\[
Q(I)=\{(a,b):0<a<|I|,\ b\in I\}
\tag{6}
\]

and for a positive measure `nu` define

\[
\|\nu\|_{\mathcal C}
:=\sup_I\frac{\nu(Q(I))}{|I|}.
\tag{7}
\]

For one interior atom one has exactly

\[
\boxed{
\|w\delta_{(a,b)}\|_{\mathcal C}=\frac wa.
}
\tag{8}
\]

Consequently, for every finite target set, every `Q>0`, and every `epsilon,eta>0`, there is a positive finite atomic probe measure with

\[
\boxed{
\|\nu\|_{\rm TV}<\varepsilon,
\qquad
\|\nu\|_{\mathcal C}<\eta,
\qquad
Q_\nu(\gamma_j,d_j)\ge Q\ \forall j.
}
\tag{9}
\]

The same construction uses only finitely many interior atoms and therefore also satisfies the usual local vanishing-Carleson condition: for all sufficiently short boundary intervals `I`, `nu(Q(I))=0`. In the equivalent Hardy-space embedding language, finite interior atomic measures give finite-rank, hence compact, sampling maps. Thus replacing the `L^infinity(da db)` density cap of WI-417--WI-420 by ordinary Carleson or vanishing-Carleson control does **not** repair WI-416.

No zeta zero is excluded and no statement of RH follows. The conclusion is a source-side no-go: a viable regularity theorem must actually exclude or quantitatively penalize two-dimensional atomic concentration, rather than merely bound a norm that assigns finite local cost to Dirac masses.

## 1. The singularity defeats every locally atom-tolerant gauge

At equal horizontal depth `a=d` and nonzero vertical offset `r=b-gamma`, equation (1) becomes

\[
\boxed{
q_{d,\gamma+r}(\gamma,d)
=\frac12\log\left(1+\frac{4d^2}{r^2}\right).
}
\tag{10}
\]

Hence

\[
q_{d,\gamma+r}(\gamma,d)\longrightarrow+\infty
\qquad(r\to0,\ r\ne0).
\tag{11}
\]

More generally, `q_x(z)->+infinity` whenever the source point `x=(a,b)` tends to the interior target point `z=(d,gamma)` without coinciding with it. Every cross response is nonnegative because the numerator in (1) exceeds the denominator by `4ad`.

Choose positive weights `w_j` so small that

\[
\sum_jw_j<\varepsilon,
\qquad
\sum_jC_jw_j<\varepsilon.
\tag{12}
\]

For each `j`, use (3) and the divergence (11) to choose one point `x_j` sufficiently close to `z_j` that

\[
R(\delta_{x_j})\le C_j,
\qquad
w_j q_{x_j}(z_j)\ge Q.
\tag{13}
\]

The punctured sequence may be thinned to avoid the finitely many target points in `E`, so every cross kernel value is finite. Put

\[
\nu=\sum_jw_j\delta_{x_j}.
\tag{14}
\]

Positive homogeneity and subadditivity give

\[
R(\nu)
\le\sum_jw_jR(\delta_{x_j})
\le\sum_jC_jw_j
<\varepsilon.
\tag{15}
\]

The total variation inequality follows from (12), while positivity of all cross terms gives

\[
Q_\nu(z_j)
\ge w_j q_{x_j}(z_j)
\ge Q.
\tag{16}
\]

This proves (4). The mechanism is completely local. No information about the number, spacing, height distribution, or multiplicity of the other targets can repair it as long as the source regularity still assigns locally bounded cost to arbitrarily concentrated interior atoms.

## 2. Exact Carleson specialization

For a single source atom, a Carleson box contains `(a,b)` only if its base interval contains `b` and has length strictly greater than `a`. Therefore

\[
\sup_{I:(a,b)\in Q(I)}\frac{w}{|I|}
=\frac wa,
\]

which proves (8). For a finite positive atomic measure

\[
\nu=\sum_jw_j\delta_{(a_j,b_j)},
\]

subadditivity yields the useful bound

\[
\boxed{
\|\nu\|_{\mathcal C}
\le\sum_j\frac{w_j}{a_j}.
}
\tag{17}
\]

The oracle construction can now be made explicit. Assume repeated identical targets have first been merged, which does not change the response requirement. Choose a constant `c>0` satisfying

\[
c\sum_jd_j<\varepsilon,
\qquad
Nc<\eta,
\tag{18}
\]

and set

\[
w_j=cd_j.
\tag{19}
\]

Place the `j`th source at

\[
(a_j,b_j)=(d_j,\gamma_j+r_j),
\tag{20}
\]

where `r_j` is nonzero and chosen outside the finite set of offsets that would make `(a_j,b_j)` coincide with another target. By (10), `r_j` can be taken arbitrarily small while forcing

\[
w_jq_{d_j,\gamma_j+r_j}(\gamma_j,d_j)\ge Q.
\tag{21}
\]

Equations (17)--(20) then give

\[
\|\nu\|_{\rm TV}
=c\sum_jd_j<\varepsilon,
\qquad
\|\nu\|_{\mathcal C}
\le\sum_j\frac{cd_j}{d_j}
=Nc<\eta,
\tag{22}
\]

and (21) plus positivity gives all target constraints. This proves (9).

There is no hidden small-box defect. If `a_*:=min_j a_j>0`, then every Carleson box with `|I|<=a_*` contains no atom at all. Thus

\[
\sup_{|I|\le h}\frac{\nu(Q(I))}{|I|}=0
\qquad(0<h\le a_*).
\tag{23}
\]

So the construction survives not only a finite Carleson norm but an arbitrarily small one and the local vanishing-Carleson requirement. The distinction from WI-417 is therefore qualitative, not a matter of constants: an `L^infinity` area-density cap forbids atoms altogether, whereas Carleson control permits interior atoms and charges each by only `w/a`.

## 3. Hardy-space prior art makes this a redirect, not a new function-theory claim

The relevant analytic background is classical. Kunik's half-plane factorization records that

\[
\frac{s-1}{s}\zeta(s)=\zeta_B(s)B(s)
\qquad(\Re s>1/2),
\tag{24}
\]

where `B` is the Blaschke product over zeta zeros with `Re rho>1/2`; the same paper notes the Hardy-space membership of `(s-1)zeta(s)/s^2`. This is the established inner/outer setting already used by WI-409--WI-411. See Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:`0804.4829`, especially equations (1.2)--(1.4), and Jean-François Burnol, *A note on Nyman's equivalent formulation of the Riemann hypothesis*, Contemp. Math. 287 (2001), 23--26, arXiv:`math/9910055`.

Hardy-space membership by itself is far too permissive to create the missing source density. Kristian Seip proves that, for a **bounded** sequence in `Re s>1/2`, the Blaschke condition is necessary and sufficient for it to be the zero sequence of a nontrivial function in the Dirichlet--Hardy space `H^2` of Dirichlet series, and moreover that ordinary half-plane `H^2` data can be interpolated on such a Blaschke sequence. See Kristian Seip, *Zeros of functions in Hilbert spaces of Dirichlet series*, Math. Z. 274 (2013), 1327--1339, arXiv:`1206.2815`. This is not a theorem about the Riemann zeta function's actual zeros; it is prior-art evidence that generic Hardy/Dirichlet-Hardy membership does not impose the two-dimensional atom exclusion required by WI-417.

Carleson's interpolation theory is likewise classical; see Lennart Carleson, *An Interpolation Problem for Bounded Analytic Functions*, Amer. J. Math. 80 (1958), 921--930, DOI `10.2307/2372840`. No novelty claim is made for Carleson boxes, Carleson measures, Blaschke products, inner/outer factorization, or Hardy-space zero-set theory. The exact contribution here is the line-specific no-go (4)/(9): **those softer regularity notions do not close the oracle loophole for the translated Blaschke kernel because their local atomic cost remains finite while the target response diverges logarithmically.**

A targeted prior-art audit found classical Hardy/Blaschke and Carleson machinery, including the zeta-specific Kunik--Burnol factorization and Seip's Dirichlet-Hardy zero-set theorem, but no result turning generic Hardy/Carleson control into a Lebesgue-area density cap on an independently generated zeta probe measure. None is assumed here.

## 4. Boundary of the obstruction

The theorem does **not** rule out source regularity that is genuinely concentration-sensitive. In particular, it does not touch:

- absolute continuity with an `L^infinity` bound as in WI-417--WI-420;
- other `L^p` or Orlicz bounds that quantitatively penalize concentration after a source measure has been independently identified;
- a fixed mesh, bandwidth, transport, uncertainty, or resolution constraint justified from the prime/source side rather than chosen after the target zeros are known;
- a non-oracular arithmetic construction whose source points or density are fixed before the exceptional zero set is read off;
- a different invariant that couples source and zero geometry without passing through a target-adaptive probe measure.

Nor does the finding assert that the hypothetical off-critical zeta zeros form an interpolating sequence or a Carleson--Newman Blaschke product. Such statements would be additional arithmetic information and are not needed for the no-go.

The exact dividing line exposed here is simpler: **finite local cost for interior atoms is already too weak**. Any candidate source norm proposed as the missing input after WI-420 should first be tested on `R(delta_x)` as `x` approaches a target. If that quantity stays locally bounded, the oracle construction above kills the route immediately.

## Consequence

WI-416--WI-420 can now be read as a sharper trichotomy:

\[
\boxed{
\begin{array}{rcl}
\text{finite TV / atom-tolerant norms} &\Longrightarrow& \text{zero oracle cost},\\[1mm]
\text{Carleson / vanishing-Carleson control} &\Longrightarrow& \text{still zero oracle cost},\\[1mm]
L^\infty(da\,db)\text{ density cap} &\Longrightarrow& \text{positive }d^{-2}\text{ capacity}.
\end{array}
}
\tag{25}
\]

Therefore the live source-side question should not be weakened to "derive some Hardy/Carleson regularity for the probe family." The useful target is specifically an **atom-excluding or concentration-priced arithmetic regularity theorem**, or an independently fixed non-oracular source geometry. This is a decisive early rejection test for future defect-to-zero proposals along the Blaschke-capacity branch.