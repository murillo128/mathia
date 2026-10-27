# ANF-214 — Cubic notch floors have width-uniform finite-cardinality approximations

**Status:** EXACT-DERIVED + ALL-REAL-MULTISETS + CUBIC-WIDTH-UNIFORM-LOCALIZATION.
Fix `lambda>0` and let the removed spectral height be `a=lambda eta^3`.
At any prescribed accuracy `epsilon eta^4`, the unrestricted real notch
floor can be approximated by a multiset whose total cardinality is
bounded independently of `eta`. Its span is at most `R/eta`, with `R`
depending only on `lambda,epsilon`; it may also be chosen with only
simple/double sites and quarter-interval occupation at most four.
The explicit error below is `O_lambda(eta^4 log R/R)` with cardinality
`O_lambda(R)`. This controls the singular-width approximation problem,
not exact finite attainment or the value of the limiting coefficient.

## Object and quantitative statement

Use `f_hat(x)=int f(u) exp(-2 pi iux) du` and put
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\quad J_0=g*g,\quad F=\widehat g^{\,2},
\]
\[
\tau_\eta(u)=(1-|u|/\eta)_+,\quad
\Phi_\eta(x)=\eta\operatorname{sinc}^2(\eta x),\quad
V=F-\lambda\eta^3\Phi_\eta,
\tag{1}
\]
where `sinc(t)=sin(pi t)/(pi t)` continuously at zero. For distinct
real sites `x_i` with positive integer multiplicities `m_i`, define
\[
N(W)=\sum_i m_i,\quad
\ell(1)=1,\quad\ell(m)=2m\ (m\ge2),\quad L(W)=\sum_i\ell(m_i),
\]
\[
E_0(W)=\sum_{i,j}m_im_jF(x_i-x_j),\quad
E(W)=\sum_{i,j}m_im_jV(x_i-x_j),\quad Q(W)=E(W)/L(W),
\]
\[
q_\eta=\inf_{W\ne\varnothing}Q(W),\qquad
q_{\eta,M}=\inf_{0<N(W)\le M}Q(W).
\tag{2}
\]
All infima in this finding are real; `lambda` is fixed and suppressed.
There is no initial span, separation or density restriction.

The following nonoptimal constants make the quantifiers explicit:
\[
\mathcal A=16(1+2\pi^2)^2,\quad
c_\lambda=\min\{1,(30\mathcal A\lambda)^{-1/3}\},\quad
D_\lambda=3\lambda(3+2/c_\lambda),\quad
B_\lambda=3+6\mathcal A D_\lambda,
\]
\[
\eta_\lambda=\min\{1/2,c_\lambda,(100\lambda)^{-1/3}\},\quad
M_R=\lceil4B_\lambda R\rceil,\quad
\Gamma_\lambda(R)=6\lambda B_\lambda\frac{1+\log R}{R}
\quad(R\in\mathbb N,\ R\ge2).
\tag{3}
\]
Let `q_box(eta,R)` be the infimum over the further restricted class
\[
N(W)\le M_R,\quad \operatorname{diam}(W)\le R/\eta,\quad
m_i\in\{1,2\},\quad
\max_y\sum_{x_i\in[y,y+1/4)}m_i\le4.
\tag{4}
\]
Then, simultaneously for every `0<eta<=eta_lambda` and integer `R>=2`,
\[
\boxed{0\le q_{\eta,M_R}-q_\eta
\le q_{\rm box}(\eta,R)-q_\eta
\le\Gamma_\lambda(R)\eta^4.}
\tag{5}
\]
In particular,
\[
\boxed{\lim_{M\to\infty}
\sup_{0<\eta\le\eta_\lambda}
\frac{q_{\eta,M}-q_\eta}{\eta^4}=0.}
\tag{6}
\]
This is stronger than pointwise convergence of cardinality-restricted
infima at each fixed width. It does not assert that either normalized
floor has a limit as `eta` tends to zero.

## Low notch energy controls occupation on the reciprocal-width scale

Write `Delta=E_0-L` and `e=Delta/L`. Real pair positivity gives
\[
\Delta=\sum_i(m_i^2-\ell(m_i))
+2\sum_{i<j}m_im_jF(x_i-x_j)\ge0.
\tag{7}
\]
For any partition into half-open intervals of length `h`, with total
multiplicity `n_j` in each cell, ANF-208's weighted triple argument gives
\[
\sum_j n_j^2\le3L+\frac{3\Delta}{\kappa_h},\qquad
\kappa_h=\frac1{16(1+2\pi^2h^2)^2}.
\tag{8}
\]
For completeness, the input is ANF-114's bound `sum_three_pairs F>=kappa_h`
for a triple in an interval of length `h`. In a cell of mass `n`, put
`D=sum m_i^2` and `O=2 sum_(i<j)m_i m_j F(x_i-x_j)`. Sum the triple
bound with weights `m_i m_j m_k`. The identity
`6 sum_(i<j<k)m_i m_j m_k=n^3-3nD+2 sum m_i^3` gives
`n^2<=3D+3O/kappa_h`. Since `D-L_cell>=0` and `kappa_h<=1`,
this is at most `3L_cell+3(D-L_cell+O)/kappa_h`. Summing proves (8),
including cells with fewer than three distinct sites.

The same cell decomposition and the full tail
`Phi_eta(x)<=min(eta,1/(pi^2 eta x^2))` give
\[
\frac{\sum_{i,j}m_im_j\Phi_\eta(x_i-x_j)}L
\le(3\eta+2/h)(3+3e/\kappa_h).
\tag{9}
\]
Indeed the three neighboring cell offsets cost at most `3 eta`,
and the other offsets sum to at most `4/(pi h)<2/h`, by integrating
the decreasing majorant. For each offset use
`sum_j n_j n_(j+d)<=sum_j n_j^2`. No total-cardinality factor enters.

Take `h=c_lambda/eta>=1`. Since `kappa_h^(-1)<=mathcal A h^4`,
(9) implies
\[
Q(W)\ge1-D_\lambda\eta^4+
\{1-3\mathcal A\lambda(3c_\lambda^4+2c_\lambda^3)\}e
\ge1-D_\lambda\eta^4+\tfrac12e.
\tag{10}
\]
Here `c_lambda<=1` and
`15 mathcal A lambda c_lambda^3<=1/2`. Consequently
\[
Q(W)\le1\quad\Longrightarrow\quad e\le2D_\lambda\eta^4.
\tag{11}
\]
Apply (8) once more, now at `H=1/eta>=1`. Every grid of that cell size
satisfies the crucial width-independent estimate
\[
\boxed{\sum_j n_j^2\le B_\lambda L\qquad(Q(W)\le1).}
\tag{12}
\]
The small **excess**, rather than the full source energy, pays the
fourth-power deterioration of the triple gap. Using the quarter-interval
cap alone would leave a cardinality bound growing with `1/eta`.

## Discarding cross-block attraction costs only the fourth-order scale

Fix the grid of size `H=1/eta`. Group it into consecutive blocks of
`R` cells, with a uniformly chosen shift `s` among `0,...,R-1`.
Cells whose indices differ by `d` are separated with probability
`min(d/R,1)`. Entire sites, including all their copies, stay together,
so `sum_b L(W_(s,b))=L(W)` exactly.

Let `E_s=sum_b E(W_(s,b))`. Dropping a positive cross-block `F` term
can only lower this energy. Thus the only upper error is the lost
attraction. Adjacent fine cells have `Phi_eta<=eta`; for index
distance `d>=2` they have
`Phi_eta<=eta/[pi^2(d-1)^2]`. Expanding ordered pairs before averaging,
\[
\frac1R\sum_{s=0}^{R-1}E_s
\le E(W)+\lambda\eta^3\,\mathcal T_R\sum_j n_j^2,
\]
\[
\mathcal T_R=2\eta\left\{\frac1R+
\frac1{\pi^2}\sum_{d=2}^\infty
\frac{\min(d/R,1)}{(d-1)^2}\right\}.
\tag{13}
\]
With `n=d-1`, sum `2/(Rn)` for `n<=R` and `1/n^2` for `n>R`.
The tail is at most `1/R`, and the harmonic sum is at most `1+log R`.
Using `pi>3` therefore yields
\[
\mathcal T_R\le\frac{2\eta}R
\left\{1+\frac{2(1+\log R)+1}{\pi^2}\right\}
\le3\eta\frac{1+\log R}{R}.
\tag{14}
\]
Combining (12)--(14),
\[
\boxed{\frac1{RL}\sum_s E_s
\le Q(W)+3\lambda B_\lambda\eta^4\frac{1+\log R}{R}.}
\tag{15}
\]
There is no minimum gap, empty corridor, periodicity or cancellation
assumption. In particular, the positive source interaction is not
charged as an absolute localization error.

## Select a block with bounded cardinality and nearly minimal quotient

For each shift, Cauchy--Schwarz within each group of `R` fine cells gives
\[
\sum_b N(W_{s,b})^2\le R\sum_j n_j^2\le RB_\lambda L.
\tag{16}
\]
Give every nonempty pair `(s,b)` the probability weight
`L(W_(s,b))/(RL)`. Since `L(W_(s,b))<=2N(W_(s,b))`, (16) gives
\[
\mathbb E[N(W_{s,b})]\le2RB_\lambda,\qquad
\mathbb P\{N(W_{s,b})\le M_R\}\ge\tfrac12.
\tag{17}
\]
Every nonempty block has `Q(W_(s,b))>=q_eta`. By (15), the
nonnegative random variable `Q(W_(s,b))-q_eta` has mean at most
\[
Q(W)-q_\eta+
3\lambda B_\lambda\eta^4\frac{1+\log R}{R}.
\tag{18}
\]
Conditional averaging on the event in (17) selects a block of at most
`M_R` points and span at most `R/eta` with gap at most twice (18).
This uses denominator weights, not a uniform choice of occupied blocks;
the latter would not preserve the energy quotient.

Now take any sequence with `Q(W)->q_eta`. A singleton has
`Q=1-lambda eta^4<1`, so the sequence eventually has `Q<=1`.
ANF-213 allows replacement by submultisets with no higher quotient,
simple/double multiplicities and quarter-interval occupation at most
four, since `lambda eta^3<=1/100`. They still approach `q_eta`.
The selected blocks inherit both restrictions. Letting `Q(W)-q_eta`
tend to zero proves (5). Choosing `R` before varying `eta` and then
sending `R` to infinity proves (6). No minimizing configuration,
compactness extraction or exchange of infinite pair sums is required.

## Prior art, validation and consequence

The averaging method is classical. [Hainzl--Lewin--Solovej,
*The Thermodynamic Limit of Quantum Coulomb Systems: A New Approach*,
section 3.1](https://arxiv.org/pdf/0806.2436), explains the fixed-state,
translated-tiling localization principle through the Graf--Schenker
inequality. Its Coulomb inequality is not used here. [Ruelle,
*Superstable Interactions in Classical Statistical Mechanics*, section 1,
condition (SS)](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B28%5D.pdf),
is the classical occupation-square framework. No new general
localization or superstability principle is claimed.

[Knausgård, sections 7.1--7.2](https://arxiv.org/html/2610.08965v1#S7.SS1)
studies labelled real simple/double pair energies and periodic trial
states for a constrained-density zero-counting objective. It does not
give (5)'s free-span, shrinking-notch approximation theorem. Targeted
searches of these neighboring formulations did not identify that exact
width-uniform statement; this is not an exhaustive novelty claim.

Locally, ANF-106 already gives finite physical-box localization at
fixed height, fixed notch and fixed error. Its source-energy occupation
bound and absolute two-form cross budget do not provide (5)'s uniform
`eta^4` resolution with a width-independent cardinality cap. ANF-208's
excess-paid occupation estimate and the one-sided use of `F>=0` supply
the additional scale control here. ANF-213 supplies the optional exact
simple/double reduction, while ANF-211--ANF-212 show why the surviving
finite witness need not be a two-site state.

The proof checks are (8)'s weighted triple identity, the coefficient
absorption in (10), the complete inverse-square tail in (14), exact
additivity of `L`, and the nonnegative-gap selection in (17)--(18).
Scratch validation checked 271440 finite-grid separation probabilities
with rational arithmetic, the coefficient majorants for `2<=R<=500`,
and 64 floating-point kernel/partition cases including dense clusters,
mixed multiplicities, integer-scale strings and remote components.
Those diagnostics are not the proof; the displayed inequalities cover
all parameters. No numerical minimization or Lean verification is used.

For every fixed `lambda` and positive tolerance, cardinality escape
cannot create an additional fixed-size gap in the normalized real
floor that remains invisible to every sufficiently large fixed finite
test. The cap grows as the tolerance shrinks. Exact finite attainment,
an exact finite-cardinality reduction, the optimal cubic coefficient,
and existence of its limit remain undecided. Physical spans may still
grow like `1/eta`, and collisions require the stated multiplicity-aware
denominator. The estimate is not uniform in growing `lambda` and does
not contradict ANF-207's growing-cardinality regime `a=lambda eta`.
No complex-site localization, improved zeta-zero proportion or exclusion
of off-critical zeros follows: real pair positivity is load-bearing.
