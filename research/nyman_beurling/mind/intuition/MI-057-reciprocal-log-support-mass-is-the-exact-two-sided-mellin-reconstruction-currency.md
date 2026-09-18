# MI-057 — Reciprocal log-support mass is the exact two-sided Mellin reconstruction currency

**Evidence level:** exact synthesis from [NB-217](../../findings/NB-217-reciprocal-log-support-mass-prices-two-sided-mellin-reconstruction.md), extending the bounded-shell tariffs of NB-215--NB-216 by removing connected/upward-support assumptions.

NB-216 shows that zero mean and upward shell widening do not freely remove the absolute Mellin reconstruction tariff. NB-217 identifies the invariant behind that special geometry. Let `E` be the actual support in logarithmic coordinate `u=log n`, let `h` be supported on `E`, and after `j` ordinary Mellin primitive transfers write

`K_j(v)=int_E u^j h(u)e^(ivu)du`.

For any bounded source functional `M_psi(h)=int_E psi(u)h(u)du` with `||psi||_infinity<=1`, Fourier inversion gives the exact source-normalized lower bound

`||K_j||_1/|M_psi(h)| >= 2pi/J_j(E)`,

where

`J_j(E)=int_E u^(-j)du`.

Thus the geometric currency is not shell width by itself, nor the minimum of an enclosing interval, but the **reciprocal logarithmic support mass actually occupied by the source**. Signs, phases, disconnected support and internal gaps do not evade the bound; a tiny token of support near small `u` does not help unless it contributes enough reciprocal mass.

The first primitive is borderline. Since `J_1([A,B])=log(B/A)`, one can trade reconstruction cost for a genuine two-sided logarithmic span. For `j>=2`, however, `u^-j` is integrable at infinity and

`J_j(E) <= A^(1-j)/(j-1)`

whenever `E subset [A,infinity)`. Hence normalized cost is at least `2pi(j-1)A^(j-1)`, regardless of how far the support extends upward or how disconnected it is.

On the Vinogradov--Korobov diagonal `X=Q^(2/3+o(1))`, a fixed higher primitive `j>=2` can have subpolynomial normalized absolute reconstruction cost only if the lower logarithmic source scale reaches

`A_Q=Q^(o(1))=X^(o(1))`.

In physical coordinates this means coupling a carrier near `x=e^X` to integers as small as `x^(o(1))`; bounded cost forces `A=O(1)`, i.e. support reaching bounded integers. Staying in any relative logarithmic annulus `u asymp X` preserves an `Omega(X^(j-1))` tariff.

This closes ordinary two-sided shell tuning as a higher-primitive escape. A cheap architecture must now exploit oscillatory correlation with the actual zeta primitive before absolute values, use a destination-visible source functional outside bounded `L^infinity` duality and pay its norm, or genuinely globalize the source across widely separated arithmetic scales.

**Boundary.** The theorem controls the full frequency-line `L1` reconstruction norm and does not prove that this mass sits on the contour where the zeta primitive is small. It does not establish discrete realization by Nyman generators or a destination theorem coupling near-optimal approximation to the source functional. Low reciprocal support mass is a necessary source-side cost, not an RH criterion.