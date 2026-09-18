# RE-207 — Signed moment stencils push continuum Euler hiding to the 17/30 short-interval boundary

**Status:** `LITERATURE+DERIVED + CONTINUUM-VERTICAL-EULER + SIGNED-MOMENT-STENCIL + ORDER-8-SPATIAL-CANCELLATION + SHORT-INTERVAL-PNT + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + LOGARITHMIC-HEIGHT + KV-FIDELITY + INTEGER-MULTIPLICITIES`.

**Parent finding:** RE-206.

`RE-206` raises the ordinary-prime realization budget for the continuum vertical Euler synthesis from `kappa<1/4` to `kappa<1/3` by replacing one-sided coefficient packing with equal-count symmetric pairs. The gain comes from cancelling the first displacement moment, leaving a quadratic shell-spread error. The explicit caveat there is that a more general signed local stencil might cancel further moments.

That caveat can be resolved. A fixed bounded-sign stencil can cancel **all displacement moments through degree seven** at its nominal prime-bin centers. Its first nonzero spatial term is eighth order. Once this is combined with the current all-interval short-interval prime number theorem, the continuum hiding budget becomes

\[
\boxed{\kappa<\frac{13}{30}.}
\tag{1}
\]

This is not the eighth-order stencil's own geometric limit: its cloud-spread error would still be negligible throughout `kappa<4/9`. The new load-bearing restriction is instead the unknown location of actual primes inside intervals of relative width `Q^(theta-1)`. The Guth--Maynard short-interval input allows every fixed `theta>17/30`; requiring that first-order within-bin error to stay below selector scale gives `kappa<1-theta`, hence the boundary `13/30`.

Keep the notation and continuum synthesis of `RE-204`--`RE-206`:

\[
d_Q:=\frac1{\sqrt Q\log Q},
\qquad
H:=\log 8,
\qquad
T_Q:=c\log Q,
\qquad
\epsilon_Q:=Q^{-\rho},
\tag{2}
\]

and

\[
G_Q(t)=\sum_j b_j e^{-itL_j},
\qquad
\sup_{|t|\le T_Q}|1-G_Q(t)|\le\epsilon_Q,
\tag{3}
\]

with `O(log Q)` remote shells, `L_j>=H`, bounded `L_j=O_(c,rho)(1)`, adjacent synthesis centers separated by `Theta(1/log Q)`, and

\[
A_Q:=\sum_j|b_j|\le Q^{\kappa+o(1)},
\qquad
\kappa:=12H(\log2)c+2\rho.
\tag{4}
\]

If

\[
\boxed{12H(\log2)c+2\rho<\frac{13}{30},}
\tag{5}
\]

then for all sufficiently large `Q` there is a finite ordinary-prime perturbation `c_q in {-1,+1}` such that

\[
D_Q(s):=\sum_q c_q\log(1-q^{-s})^{-1}
\tag{6}
\]

satisfies

\[
\boxed{
\sup_{|t|\le c\log Q}|D_Q(1+it)|=o(d_Q).
}
\tag{7}
\]

Before the first remote repair cloud arrives, the local packet still has

\[
D_{Q,\mathrm{local}}(1)=\Theta(d_Q),
\tag{8}
\]

all modified prime multiplicities remain in `{0,1,2}`, and for every fixed `b>0`,

\[
|\Delta\vartheta(x)|=o\!\left(xe^{-bV(x)}\right),
\qquad
V(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\tag{9}
\]

through and beyond every edited scale.

Since `rho` may be chosen arbitrarily small after `c`, (5) gives the explicit continuum-height range

\[
\boxed{
0<c<\frac{13}{360H\log2}
=0.02505\ldots .
}
\tag{10}
\]

This is a factor `13/10` larger than the explicit `RE-206` range.

## 1. A fixed signed stencil cancels seven displacement moments

The needed local representation is finite-dimensional and elementary. For every sufficiently large integer `R`, put

\[
x_k:=\frac{k}{R},
\qquad -R\le k\le R.
\tag{11}
\]

There are real symmetric weights `w_(R,k)=w_(R,-k)` satisfying

\[
\sum_{k=-R}^R w_{R,k}=1,
\qquad
\sum_{k=-R}^R w_{R,k}x_k^r=0
\quad(1\le r\le7),
\tag{12}
\]

and, uniformly in `R`,

\[
\max_k|w_{R,k}|\ll\frac1R,
\qquad
\sum_k|w_{R,k}|\ll1.
\tag{13}
\]

To see this, seek

\[
w_{R,k}=\frac1R P_R(x_k),
\qquad
P_R(x)=a_{R,0}+a_{R,1}x^2+a_{R,2}x^4+a_{R,3}x^6.
\tag{14}
\]

The four even conditions in (12) form a `4 x 4` linear system whose matrix is

\[
M_R(a,b)
=\frac1R\sum_{k=-R}^R x_k^{2(a+b)},
\qquad 0\le a,b\le3.
\tag{15}
\]

As `R->infinity`, this converges to the positive-definite Gram matrix

\[
M_\infty(a,b)=\int_{-1}^{1}x^{2(a+b)}\,dx
=\frac{2}{2(a+b)+1}.
\tag{16}
\]

Hence `M_R^(-1)` is uniformly bounded for large `R`, which proves (13). Symmetry kills every odd moment exactly. The limiting polynomial is explicitly

\[
P_\infty(x)
=\frac{1225-11025x^2+24255x^4-15015x^6}{512},
\tag{17}
\]

with

\[
\int_{-1}^{1}P_\infty(x)\,dx=1,
\qquad
\int_{-1}^{1}x^rP_\infty(x)\,dx=0
\quad(1\le r\le7),
\tag{18}
\]

and first surviving moment

\[
\int_{-1}^{1}x^8P_\infty(x)\,dx=-\frac7{1287}.
\tag{19}
\]

For a logarithmic cloud half-width `Delta`, define

\[
\Phi_R(s,\Delta)
:=\sum_{k=-R}^R w_{R,k}e^{-s\Delta x_k}.
\tag{20}
\]

Taylor's theorem, (12), and the bounded total variation in (13) give uniformly for `|s|Delta<=1`,

\[
\boxed{
|\Phi_R(s,\Delta)-1|
\ll |s\Delta|^8.
}
\tag{21}
\]

Thus the signed cloud acts like one Euler atom at its center up to eighth order in logarithmic displacement. The use of negative weights is essential: positive same-sign populations cannot cancel their even second moment, which is why the symmetric-pair construction of `RE-206` stops at quadratic order.

## 2. Realize the stencil by disjoint ordinary-prime microbins

Assume first `1/3<=kappa<13/30`; the smaller range is already covered by `RE-206`. Choose a fixed exponent

\[
\boxed{
\frac{17}{30}<\theta<1-\kappa.
}
\tag{22}
\]

Such a `theta` exists exactly because `kappa<13/30`.

The unconditional short-interval PNT consequence already used in `RE-205`--`RE-206` gives, uniformly for `Y` in every fixed multiplicative neighborhood of `Q`,

\[
\#\{q\text{ prime}:Y\le q\le Y+Y^\theta\}
=(1+o(1))\frac{Y^\theta}{\log Y}.
\tag{23}
\]

Choose a safe per-bin capacity

\[
M_Q:=\left\lfloor a_0\frac{Q^\theta}{\log Q}\right\rfloor
\tag{24}
\]

with fixed sufficiently small `a_0>0`, and a logarithmic bin spacing

\[
h_Q:=C_0Q^{\theta-1}
\tag{25}
\]

with fixed sufficiently large `C_0`.

As before, let

\[
X_0:=2Q,
\qquad
X_j:=X_0e^{L_j},
\qquad
B\asymp\frac{\sqrt Q}{\log Q}.
\tag{26}
\]

The ideal `j`th repair coefficient requires a signed population

\[
N_j\asymp |b_j|e^{L_j}B
\tag{27}
\]

near `X_j`. Choose

\[
R_j:=\max\!\left\{R_*,
\left\lceil C_*\frac{N_j}{M_Q}\right\rceil\right\},
\tag{28}
\]

where the fixed constants `R_*` and `C_*` are large enough for the stencil lemma and the capacity bound below. Put

\[
u_{j,k}:=k h_Q,
\qquad |k|\le R_j,
\tag{29}
\]

and use the nominal prime bins

\[
I_{j,k}:=
\left[
X_je^{u_{j,k}},
X_je^{u_{j,k}}+(X_je^{u_{j,k}})^\theta
\right].
\tag{30}
\]

For large `Q`, all bins in one cloud are disjoint by the choice of `C_0`. Their logarithmic half-width obeys

\[
\Delta_j:=R_jh_Q
\ll
Q^{\theta-1}+|b_j|Q^{-1/2+o(1)}.
\tag{31}
\]

Consequently

\[
\max_j\Delta_j
\ll
Q^{\theta-1}+Q^{\kappa-1/2+o(1)}
=o(1/\log Q).
\tag{32}
\]

The clouds belonging to distinct continuum-synthesis centers therefore remain disjoint because those centers are separated by `Theta(1/log Q)`.

Let `w_(R_j,k)` be the signed stencil weights from Section 1. In bin `I_(j,k)`, select the nearest integer to

\[
N_j|w_{R_j,k}|
\tag{33}
\]

ordinary primes and assign them perturbation sign

\[
-\operatorname{sgn}(b_j)\operatorname{sgn}(w_{R_j,k}).
\tag{34}
\]

Because `|w_(R,k)|<<1/R` and `R_j` was chosen as in (28), the selected population in every bin is at most `M_Q` after increasing `C_*` once. Equation (23) supplies that many distinct ordinary primes. Every edited prime belongs to exactly one bin and is changed only once, so all multiplicities remain in `{0,1,2}`.

The signed stencil has bounded total variation, hence the total population used by the `j`th cloud is

\[
O(N_j+R_j).
\tag{35}
\]

The `O(R_j)` term is solely integer rounding.

## 3. Eighth-order cloud error is below selector scale

Ignore integer rounding and unknown within-bin prime locations momentarily. At the nominal centers, the `j`th signed cloud differs from its ideal single shell by the factor

\[
\Phi_{R_j}(1+it,\Delta_j)-1.
\tag{36}
\]

Since `T_Q Delta_j=o(1)`, (21) gives an error, relative to `d_Q`, bounded by

\[
\sum_j |b_j|(T_Q\Delta_j)^8.
\tag{37}
\]

Using (31), `sum |b_j|<=A_Q`, and `sum |b_j|^9<=A_Q^9`,

\[
\sum_j |b_j|(T_Q\Delta_j)^8
\ll
Q^{\kappa+8\theta-8+o(1)}
+
Q^{9\kappa-4+o(1)}.
\tag{38}
\]

The first exponent is negative because `theta<1-kappa`:

\[
\kappa+8\theta-8<-7\kappa<0.
\tag{39}
\]

The second is negative because

\[
\kappa<\frac{13}{30}<\frac49.
\tag{40}
\]

Therefore the entire **nominal stencil-spread error** is `o(d_Q)` uniformly for `|t|<=T_Q`.

This is the key improvement over `RE-206`. There the corresponding relative term is `Q^(3kappa-1+o(1))`, because only the first moment vanishes. Here all terms through degree seven vanish exactly and the cloud-width contribution is pushed to `Q^(9kappa-4+o(1))`.

## 4. Integer rounding is cheaper than the stencil gain

Rounding every signed target count in (33) changes at most `O(R_j)` atoms in the `j`th cloud. Summing (28),

\[
\sum_jR_j
\ll
\log Q+\frac{B}{M_Q}A_Q
\ll
Q^{\kappa+1/2-\theta+o(1)}+Q^{o(1)}.
\tag{41}
\]

Each such atom contributes `O(1/Q)` to the first Euler harmonic, so after normalization by `d_Q\asymp B/Q`, the rounding error is

\[
\ll
\frac{\sum_jR_j}{B}
\ll
Q^{\kappa-\theta+o(1)}+Q^{-1/2+o(1)}
=o(1),
\tag{42}
\]

because `theta>17/30>13/30>kappa`.

Thus integer quantization does not reintroduce any of the cancelled low moments at selector scale.

## 5. Unknown prime positions create the actual 13/30 barrier

The selected primes are only known to lie inside the one-sided short intervals (30); they are not located exactly at their nominal centers. For every selected prime `q in I_(j,k)`,

\[
q=X_je^{u_{j,k}}
\left(1+O(Q^{\theta-1})\right).
\tag{43}
\]

Uniformly for `|t|<=T_Q`,

\[
q^{-1-it}
=
(X_je^{u_{j,k}})^{-1-it}
\left(
1+O((1+T_Q)Q^{\theta-1})
\right).
\tag{44}
\]

The reciprocal total variation of all stencil populations is still only a fixed constant multiple of the continuum coefficient variation:

\[
\sum_q\frac{|c_q|}{q}
\ll d_QQ^{\kappa+o(1)}.
\tag{45}
\]

Hence the total **within-bin placement error**, divided by `d_Q`, is

\[
\ll
Q^{\kappa+\theta-1+o(1)}
=o(1),
\tag{46}
\]

precisely because of the upper inequality in (22).

This is now load-bearing. The current all-interval PNT requires `theta>17/30`, while (46) requires `theta<1-kappa`. These two open inequalities are simultaneously satisfiable exactly when

\[
\boxed{\kappa<\frac{13}{30}.}
\tag{47}
\]

So the `13/30` threshold is not another moment-conditioning constant. It is the complement of the current unconditional all-interval short-prime exponent.

## 6. Exact Euler factors, the local debt and KV fidelity survive

For `Re s=1`,

\[
\log(1-q^{-s})^{-1}=q^{-s}+O(q^{-2}).
\tag{48}
\]

The total number of selected remote atoms is

\[
\ll BA_Q+\sum_jR_j
\ll
\frac{Q^{1/2+\kappa+o(1)}}{\log Q}.
\tag{49}
\]

Therefore all higher prime powers together contribute, relative to `d_Q`,

\[
O(Q^{\kappa-1+o(1)})=o(1).
\tag{50}
\]

The unchanged local packet may be placed in one `Q^theta` short interval because `theta>17/30>1/2`; its own placement and prime-power errors are `o(d_Q)` uniformly over the same vertical window.

Combining the ideal synthesis error from (3), the eighth-order cloud error (38), integer rounding (42), within-bin placement (46), and prime powers (50) gives

\[
\sup_{|t|\le T_Q}|D_Q(1+it)|
\le
\left(
Q^{-\rho}+o(1)
\right)d_Q
=o(d_Q),
\tag{51}
\]

which proves (7).

Every remote cloud remains centered at logarithmic displacement at least `H=log 8` and has half-width `o(1)`. Hence before the first remote cloud the local packet alone still contributes `Theta(d_Q)`, proving (8).

Finally, the total absolute Chebyshev edit mass is

\[
\ll Q^{1/2+\kappa+o(1)}.
\tag{52}
\]

At the limiting budget `kappa<13/30`, its exponent is strictly below

\[
\frac12+\frac{13}{30}=\frac{14}{15}<1.
\tag{53}
\]

All affected scales remain fixed multiplicative translates of `Q`, so for every fixed `b>0`,

\[
Q^{14/15+o(1)}
=o\!\left(Qe^{-bV(Q)}\right).
\tag{54}
\]

The same absolute bound controls every partial excursion inside a cloud. Thus KV fidelity requires no cancellation between positive and negative stencil pieces.

## Representation and prior-art audit

The finite signed moment stencil is generic approximation theory. Vanishing-moment kernels, finite-difference stencils and signed quadrature rules routinely annihilate low polynomial moments; no novelty is claimed for that mechanism. The proof above deliberately reduces the needed fact to a `4 x 4` positive-definite moment matrix, so no external quadrature theorem is load-bearing.

The external arithmetic input is the same Guth--Maynard all-interval short-interval PNT consequence already used by `RE-205` and `RE-206`: every fixed exponent `theta>17/30` has the required prime asymptotic. That source is already anchored in `research/robin_extremal/SOURCES.md`.

The line-specific result is the coupling of a bounded-total-variation **signed moment stencil** to the existing continuum Euler synthesis while preserving ordinary-prime `{0,1,2}` realization, selector-scale transient debt and every fixed KV source envelope. The main structural delta is that the source realization no longer stops at the second spatial moment: after cancelling moments through degree seven, the current short-interval prime-location uncertainty becomes the first obstruction.

## Adversarial self-review

**Do negative stencil weights violate honest prime multiplicities?** No. Multiplying the stencil sign by the target shell sign merely decides whether a distinct ordinary prime in that microbin is deleted or duplicated. Every prime is edited at most once because all bins and all clouds are disjoint, so multiplicities remain exactly in `{0,1,2}`.

**Does cancelling moments of logarithmic position ignore the real `q^-1` damping?** No. The expansion is in the full complex variable `s=1+it`: each offset contributes `e^(-s u)`. Equation (12) kills the Taylor coefficients of that complete factor through degree seven, simultaneously cancelling real-amplitude and phase displacement terms.

**Can the signed weights require more primes than one microbin contains?** No. Uniformly `|w_(R,k)|=O(1/R)`. Choosing `R_j` proportional to `N_j/M_Q` when necessary bounds every requested absolute population by the safe capacity `M_Q`. Large coefficients consume spatial width, not per-bin density.

**Does the stencil width cause neighboring continuum synthesis shells to overlap?** No. Equation (32) is `o(1/log Q)` while the synthesis centers inherited from `RE-204`--`RE-206` are separated by `Theta(1/log Q)`.

**Does integer rounding destroy exact moment cancellation?** It destroys it microscopically, but the total discrepancy is only one atom per microbin. Equation (42) controls the entire rounded discrepancy in absolute Euler norm, without relying on any remaining moment cancellation.

**Is `13/30` a source-wide coercivity threshold?** No. It is the boundary of this realization using the current all-interval short-interval PNT and no information about prime centroids inside each bin. Better source localization, a way to balance the actual first moments of selected primes, or a stronger short-interval theorem could move it. Conversely, the present eighth-order cloud itself still has room until `kappa<4/9`.

**Does this prove a Robin counterexample or all matched coordinates from the earlier jet construction?** No. As in `RE-204`--`RE-206`, it proves selector-scale noncoercivity for the complete vertical Euler continuum over the stated logarithmic-height window while retaining ordinary-prime/KV fidelity. It does not by itself produce a genuine Robin violation or simultaneously reproduce every auxiliary coordinate of `RE-188`--`RE-199`.

## Research consequence

The continuum vertical branch now has a sharper representation diagnosis. The progression `1/4 -> 1/3 -> 13/30` is not evidence for a sequence of intrinsic Euler rigidity thresholds. The first two values were packing artifacts: one-sided first-order placement and then positive-pair second-order spread. A fixed signed stencil removes both and enough additional moments that the **current prime-localization theorem**, not continuum Fourier complexity, becomes the bottleneck.

More generally, if an all-interval PNT were available at exponent `theta_0<1`, the same order-eight stencil would support every

\[
\kappa<\min\!\left\{1-\theta_0,\frac49\right\}.
\tag{55}
\]

Higher fixed moment order can move the `4/9` cloud limit toward `1/2`; it cannot remove the first-order within-bin restriction `kappa<1-theta_0` without additional information about where the selected primes lie inside each short interval. The next discriminating question is therefore no longer whether another nominal spatial moment can be cancelled. It is whether the **actual prime-location error inside the shortest guaranteed all-x intervals** can itself be balanced with bounded `{0,1,2}` edits, or whether a lower bound on that source-side first moment produces the first genuine continuum obstruction.

## Sources

- `RE-206`, *Symmetric prime packing raises logarithmic-height Euler hiding budget to one third*.
- Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics **203** (2026), no. 2, 623--675, DOI `10.4007/annals.2026.203.2.6`, arXiv:2405.20552. We use the same unconditional all-interval short-interval prime-number-theorem consequence at every fixed `theta>17/30` already invoked by `RE-205`--`RE-206`.