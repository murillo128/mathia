# RE-206 — Symmetric prime packing raises logarithmic-height Euler hiding budget to one third

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + SHORT-INTERVAL-PNT + SYMMETRIC-MICROBIN-PACKING + FIRST-MOMENT-CANCELLATION + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + LOGARITHMIC-HEIGHT + KV-FIDELITY + INTEGER-MULTIPLICITIES`.

**Parent finding:** RE-205.

`RE-205` pushes continuum vertical Euler hiding from the Korobov--Vinogradov phase scale to a fixed positive fraction of `log Q`. Its ordinary-prime realization puts each remote synthesis coefficient into one one-sided interval. If the continuum synthesis has reciprocal variation

\[
A_Q\le Q^{\kappa+o(1)},
\]

then a bin of length `Q^theta` creates two competing constraints: prime supply requires `kappa<theta-1/2`, while worst-case first-order phase placement requires `kappa<1-theta`. Optimizing those two inequalities gives the quarter-power budget `kappa<1/4` at `theta=3/4`.

That quarter-power barrier is not intrinsic even to the same continuum synthesis. The first-order placement loss can be removed by spreading each large remote coefficient over **paired short intervals symmetric in logarithmic position**. Equal prime counts in the two members of every pair cancel the linear displacement term. The remaining shell-spread error is quadratic and the realizable synthesis budget becomes

\[
\boxed{\kappa<\frac13.}
\tag{1}
\]

The construction still uses only ordinary primes with multiplicities `{0,1,2}`, leaves a selector-scale local debt before the first repair shell, and stays inside every fixed Korobov--Vinogradov Chebyshev envelope.

Put

\[
d_Q:=\frac1{\sqrt Q\log Q},
\qquad H:=\log 8,
\tag{2}
\]

and fix constants `c>0` and `rho>0`. Let

\[
T_Q:=c\log Q,
\qquad
\epsilon_Q:=Q^{-\rho}.
\tag{3}
\]

Use the same one-sided continuum synthesis as `RE-204`--`RE-205`. Its real coefficients `b_j`, remote logarithmic displacements `L_j>=H`, and number of shells satisfy

\[
G_Q(t):=\sum_j b_j e^{-itL_j},
\qquad
\sup_{|t|\le T_Q}|1-G_Q(t)|\le\epsilon_Q,
\tag{4}
\]

\[
A_Q:=\sum_j|b_j|\le Q^{\kappa+o(1)},
\qquad
\kappa:=12H(\log2)c+2\rho,
\tag{5}
\]

with only `O(log Q)` shells and `L_j=O_(c,rho)(1)`. If

\[
\boxed{12H(\log2)c+2\rho<\frac13,}
\tag{6}
\]

then for all sufficiently large `Q` there is a finite ordinary-prime perturbation `c_q in {-1,+1}` for which

\[
D_Q(s):=\sum_q c_q\log(1-q^{-s})^{-1}
\tag{7}
\]

obeys

\[
\boxed{\sup_{|t|\le c\log Q}|D_Q(1+it)|=o(d_Q).}
\tag{8}
\]

Before the first remote repair cloud arrives, the local packet still has

\[
D_{Q,\mathrm{local}}(1)=\Theta(d_Q),
\tag{9}
\]

and, for every fixed `b>0`,

\[
|\Delta\vartheta(x)|=o\!\left(xe^{-bV(x)}\right),
\qquad
V(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\tag{10}
\]

through and beyond all edited scales.

Since `rho` can be chosen arbitrarily small after `c`, (6) gives the explicit logarithmic-height range

\[
\boxed{
0<c<\frac1{36H\log2}
=0.01927\ldots .
}
\tag{11}
\]

This improves the explicit `RE-205` range by the factor `4/3`. More importantly, it identifies the quarter-power barrier there as a **first-moment placement artifact**, not a source-capacity threshold.

## 1. Keep the continuum synthesis and change only the prime realization

Let

\[
X_0:=2Q,
\qquad
X_j:=X_0e^{L_j}.
\tag{12}
\]

The ideal first-harmonic realization of the `j`th remote coefficient uses

\[
N_j\asymp |b_j|e^{L_j}B,
\qquad
B\asymp\frac{\sqrt Q}{\log Q},
\tag{13}
\]

primes near `X_j`, all with sign `-sgn(b_j)`. Since every `L_j` is bounded, the total required remote population and reciprocal variation obey

\[
\sum_j N_j
\ll \frac{Q^{1/2+\kappa+o(1)}}{\log Q},
\qquad
\sum_j\frac{N_j}{X_j}
\ll d_QQ^{\kappa+o(1)}.
\tag{14}
\]

The difference from `RE-205` is that `N_j` is no longer packed into one interval.

Fix the short-interval exponent

\[
\theta:=\frac35>\frac{17}{30}.
\tag{15}
\]

The unconditional short-interval PNT gives, uniformly for `Y` in every fixed multiplicative neighborhood of `Q`,

\[
\#\{q\text{ prime}:Y\le q\le Y+Y^{3/5}\}
=(1+o(1))\frac{Y^{3/5}}{\log Y}.
\tag{16}
\]

Choose a fixed small constant `a_0>0` and define a safe per-bin capacity

\[
M_Q:=\left\lfloor a_0\frac{Q^{3/5}}{\log Q}\right\rfloor.
\tag{17}
\]

For each remote shell replace `N_j` by the nearest even integer `N'_j`; this costs only `O(1)` atoms per shell. Put

\[
R_j:=\left\lceil\frac{N'_j}{2M_Q}\right\rceil.
\tag{18}
\]

Choose logarithmic offsets

\[
u_r:=C_0rQ^{-2/5},
\qquad 1\le r\le R_j,
\tag{19}
\]

where `C_0` is a sufficiently large fixed constant, and place paired one-sided prime bins at nominal centers

\[
Y_{j,r}^{\pm}:=X_je^{\pm u_r},
\qquad
I_{j,r}^{\pm}:=
[Y_{j,r}^{\pm},Y_{j,r}^{\pm}+(Y_{j,r}^{\pm})^{3/5}].
\tag{20}
\]

For large `Q`, the choice of `C_0` makes all bins inside one cloud disjoint. Equation (16) gives at least `M_Q` primes in every bin. Fill complete pairs with exactly `M_Q` selected primes on each side and use one final partial pair if needed, always selecting the **same number of primes from the `+` and `-` bins**. Every selected prime in the cloud receives sign `-sgn(b_j)`.

The largest number of pairs is

\[
R_j
\ll
1+Q^{\kappa-1/10+o(1)},
\tag{21}
\]

so the logarithmic half-width of any remote cloud is

\[
\Delta_Q
:=\max_{j,r}u_r
\ll
Q^{-2/5}+Q^{-1/2+\kappa+o(1)}.
\tag{22}
\]

If `kappa<1/3`, then `Delta_Q=o(1/log Q)`. Consecutive synthesis centers in `RE-205` are separated by `Theta(1/log Q)` in logarithmic position, hence the paired clouds belonging to different synthesis shells remain disjoint as well.

The local packet needs no large coefficient and can be placed in one `Q^{3/5}` short interval around `X_0`. It contains only `B=Q^{1/2+o(1)}` primes, well below the available `Q^{3/5+o(1)}` supply.

## 2. Pairing removes the first-order shell-placement error

Let

\[
s=1+it,
\qquad |t|\le T_Q.
\tag{23}
\]

Ignore the internal width of the microbins for the moment and put a selected pair exactly at the nominal centers `X_je^{\pm u}`. With `m` primes on each side, its first-harmonic contribution before the common sign is

\[
mX_j^{-s}\left(e^{-su}+e^{su}\right)
=2mX_j^{-s}\cosh(su).
\tag{24}
\]

The desired zeroth-order contribution is `2mX_j^{-s}`. Because

\[
T_Q\Delta_Q=o(1)
\tag{25}
\]

under `kappa<1/3`, the elementary Taylor bound gives uniformly over every pair

\[
|\cosh(su)-1|
\ll (1+T_Q)^2u^2.
\tag{26}
\]

Thus equal paired counts cancel the entire linear displacement term. Summing (26) over all pairs and all remote coefficients, and using the reciprocal-variation bound in (14), gives the **cloud-center error**

\[
\ll
d_QQ^{\kappa+o(1)}(\log Q)^2\Delta_Q^2.
\tag{27}
\]

By (22), the relative factor in (27) is bounded by

\[
Q^{\kappa-4/5+o(1)}
+
Q^{3\kappa-1+o(1)}.
\tag{28}
\]

Both terms tend to zero precisely throughout the new relevant range

\[
\boxed{\kappa<\frac13.}
\tag{29}
\]

The second term is the load-bearing one. It has a transparent interpretation. A coefficient population of size `Q^{1/2+kappa}` occupies total logarithmic width `Q^{-1/2+kappa}` at natural prime density. Symmetry removes the linear phase error, so the residual costs the square of that width. Multiplying by total coefficient variation `Q^kappa` produces `Q^{3kappa-1}`.

## 3. Internal bin width, integer rounding and prime powers are cheaper

Actual primes are not at the nominal centers. For every `q in I_{j,r}^{\pm}`,

\[
q=Y_{j,r}^{\pm}(1+O(Q^{-2/5})).
\tag{30}
\]

Uniformly on `|t|<=T_Q`,

\[
q^{-s}
=(Y_{j,r}^{\pm})^{-s}
\left(1+O((1+T_Q)Q^{-2/5})\right).
\tag{31}
\]

After multiplication by the full reciprocal variation, the resulting **within-bin placement error** is

\[
\ll d_QQ^{\kappa-2/5+o(1)}.
\tag{32}
\]

This is `o(d_Q)` whenever `kappa<2/5`, hence throughout (29). The use of one-sided short intervals therefore does not spoil the first-moment cancellation at the paired-bin-center level.

Making every remote target population even and filling a final partial pair changes each ideal shell population by at most `O(1)`. Across `O(log Q)` synthesis shells, the corresponding first-harmonic rounding error is

\[
O\!\left(\frac{\log Q}{Q}\right)=o(d_Q).
\tag{33}
\]

The exact Euler factor obeys, uniformly on `Re s=1`,

\[
\log(1-q^{-s})^{-1}=q^{-s}+O(q^{-2}).
\tag{34}
\]

Using (14), all higher prime powers contribute

\[
\ll d_QQ^{\kappa-1+o(1)}=o(d_Q).
\tag{35}
\]

The local `Q^{3/5}` bin contributes only `o(d_Q)` placement and prime-power errors. Combining (4), (27), (32), (33) and (35) proves (8).

## 4. Prime supply and KV fidelity still have a fixed power margin

The paired construction never asks one microbin to contain more than `M_Q` selected primes, and (16) supplies that many ordinary primes. The number of microbins grows when a coefficient is large, rather than the density inside one bin. Because the cloud half-width is `Delta_Q=o(1/log Q)`, this redistribution fits comfortably between adjacent synthesis centers.

All edits remain honest deletions or duplications relative to the ordinary-prime baseline. Therefore every multiplicity is still in `{0,1,2}`.

The total absolute Chebyshev edit mass is unchanged in order from `RE-205`:

\[
\ll Q^{1/2+\kappa+o(1)}.
\tag{36}
\]

For `kappa<1/3` this is `Q^{5/6-o(1)}` up to a fixed strict power margin, while at every affected scale `x\asymp Q`,

\[
xe^{-bV(x)}=Q^{1-o(1)}
\tag{37}
\]

for each fixed `b>0`. Hence even the total absolute edit mass is `o(xe^{-bV(x)})`. The same bound controls every partial excursion inside each microbin or between microbins, so no hidden cancellation is needed for KV fidelity.

The first remote cloud remains centered at logarithmic displacement at least `H=log 8`, while its half-width tends to zero. Thus it starts beyond a fixed multiple of `Q`. Before any remote edit arrives, the local packet alone has

\[
\sum_{q\in P_Q}\log(1-q^{-1})^{-1}
=\Theta(B/Q)
=\Theta(d_Q),
\tag{38}
\]

which proves the selector-debt statement (9).

## Representation audit

The cancellation

\[
\frac{e^{-su}+e^{su}}2-1
=O(|s|^2u^2)
\]

is elementary symmetric quadrature/Taylor cancellation; no novelty is claimed for that analytic identity. The short-interval prime theorem is external input already used in `RE-205`.

The line-specific step is to realize a **large signed continuum-synthesis coefficient with bounded ordinary-prime multiplicities by spatial width rather than per-bin density**, while arranging that width symmetrically so its first Euler displacement moment vanishes. The resulting source budget is not the `RE-205` supply-versus-linear-phase minimum. Its dominant exponent is instead the cubic balance `Q^kappa (Q^{-1/2+kappa})^2=Q^{3kappa-1}`.

This is therefore a correction to the interpretation of `RE-205`: the `1/4` threshold is not the logarithmic-height continuum barrier for the present ordinary-prime source class. Even without improving the continuum FIR coefficients, the same synthesized transform remains realizable through every `kappa<1/3`.

## Adversarial self-review

**Does pairing require primes at exactly symmetric locations?** No. Exact symmetry is imposed only on the nominal short-interval centers and on the number of selected primes. The unknown locations of the actual primes inside their bins contribute the separate first-order error (32), which is smaller because the bins have relative width `Q^{-2/5}`.

**Can the many microbins overlap when one coefficient is as large as the full `A_Q`?** No. A worst-case cloud has half-width `Q^{-1/2+kappa+o(1)}`. For `kappa<1/3` this is `o(1/log Q)`, whereas adjacent synthesis centers are `Theta(1/log Q)` apart. The fixed spacing constant `C_0` keeps microbins within a cloud disjoint.

**Is the short-interval theorem uniform enough for polynomially many bins?** Yes. The input used here is an all-interval PNT for every fixed exponent `theta>17/30`, not an almost-all statement. Every microbin lies in a fixed multiplicative neighborhood of `Q`, so the same sufficiently-large threshold applies uniformly over the deterministic family used by the construction.

**Does equal population on the two sides double the prime-supply cost?** Only by a constant. The total required population remains `N_j`; it is split into equal pair counts. The number of pairs grows to supply the coefficient, and the total logarithmic span is exactly what produces (22).

**Does the real damping `q^{-1}` break the symmetry?** It is already part of `s=1+it`. Equation (24) uses `e^{\pm su}`, not only the phase `e^{\pm itu}`. The linear real-amplitude displacement cancels together with the linear phase displacement.

**Could a better packing remove the new `1/3` threshold as well?** Possibly. The present construction only cancels the first displacement moment. Positive equal-sign pairs necessarily retain a quadratic spread term. More elaborate signed local stencils could cancel higher moments, but they would introduce additional positive/negative prime populations and new capacity constraints. Equation (29) is a threshold of this symmetric-pair realization, not a source-wide coercivity theorem.

**Does this create a full Robin counterexample or reproduce every matched coordinate from `RE-188`--`RE-199`?** No. As in `RE-204`--`RE-205`, the result isolates a genuine selector-scale reciprocal debt and hides its exact complex Euler profile on a continuum while preserving ordinary-prime/KV source fidelity. It does not by itself prove the complete order-one Robin destination displacement or simultaneous matching of all earlier auxiliary coordinates.

## Research consequence

The immediate continuum frontier moves from the quarter-power packing law to a first-moment hierarchy. The next discriminating test is whether a bounded-sign **local stencil** can cancel the quadratic displacement moment while remaining realizable with `{0,1,2}` multiplicities and short-interval prime supply. If an `r`th-order spatial moment cancellation can be realized without coefficient blow-up that consumes the gain, the logarithmic-height hiding range could move again. Conversely, a source-wide lower bound on the unavoidable second moment of same-sign prime populations would make the `1/3` balance the first genuine packing obstruction.

A refinement of the continuum polynomial itself is no longer required to improve on `RE-205`; the source realization geometry already does so.

## Sources

- `RE-205`, *Three-quarter prime bins push continuous vertical Euler hiding to logarithmic height*.
- Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics **203** (2026), no. 2, 623--675, DOI `10.4007/annals.2026.203.2.6`, arXiv:2405.20552. We use only the unconditional all-interval prime-number-theorem consequence at the fixed exponent `theta=3/5>17/30`; this paper is already anchored in `research/robin_extremal/SOURCES.md`.