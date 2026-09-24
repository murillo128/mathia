# Weil-inertia research lines

This file records the current mathematical questions that survive the Weil-Inertia evidence. It is not a roadmap, task queue, status page, or history.

## Keep source regularity separate from regularity of the canonical defect measure

WI-417--WI-422 identify sharp coercive source-space phenomena for translated-Blaschke probes. With an independently fixed planar density cap, one-target cost has the expected shallow-depth blow-up and critically separated target families converge to a Poisson-capacity problem. Generic TV/Carleson control is too weak because target-adaptive atoms remain cheap. For the bare translated-Blaschke response, ordinary global `L^p` control is bounded exactly for `1<p<2`, with a Lorentz endpoint and different behavior once a finite-TV budget is added.

WI-423 shows why these useful auxiliary spaces cannot simply be imposed on the canonical exact zeta source. The Riesz identity `-Delta U = 2 pi mu_off` makes that source the atomic counting measure of off-critical zeros; exact absolute continuity of the same source would already force the defect measure to vanish. A nontrivial route must therefore generate an auxiliary probe/coefficient source independently and prove an exact or quantitatively controlled coupling from its potential back to the canonical defect measure.

The live question is to derive such an auxiliary source and a target-independent concentration-and-tail budget from accessible prime-side, boundary or explicit-formula data. The norm must be fixed without inspecting hypothetical zero locations and must control the actual Poisson-capacity geometry consumed by the destination.

## Approach the boundary with a source-controlled probe family; projected energy already has a defect quantum

WI-424 identifies the boundary logarithmic derivative of the Kunik Blaschke factor as a canonical positive Poisson defect counter. WI-425 shows that any fixed interior safe line is cubically blind to sufficiently shallow defects. WI-426 gives the same blind-or-singular obstruction for positive multiscale `L^2` line energy, and WI-427 closes every finite-cost positive diagonal `L^p` portfolio below the local pole threshold.

WI-428 closes the two most immediate nonpositive escapes on a fixed safe strip. For the one-defect response, the exact cross-scale kernel is

`K_d(a,b)=16 pi d^2 / [(a+b)((a+b)^2-4d^2)]`.

Any signed or complex cross-scale charge with finite depth-independent weighted variation `int int (a+b)^(-3) d|nu|` therefore produces only `Q_nu(d)=O(d^2)`, while the canonical boundary energy is `2 pi/d`. The relative response is still `O(d^3)`. The same obstruction holds for bounded non-diagonal quadratic forms and for bounded cancellation before taking a Hilbert norm. To retain a fixed fraction of the boundary energy as `d->0` while the probe remains in a fixed safe strip, a quadratic-form operator must have norm at least order `d^(-3)`, or a preprocessing map before squaring must have norm at least order `d^(-3/2)`.

WI-429 identifies a different category in which no operator singularity is needed. On a line `Re(s)=1/2+a`, the norm-one Hardy/Riesz projection `P_+` applied to the finite Kunik logarithmic derivative keeps exactly the zeros with depth `d_j>a` and annihilates those with `d_j<a`:

`P_+ G_(F,a)(t)=sum_(d_j>a) m_j/[a-d_j+i(t-gamma_j)]`.

Its energy has an exact positive pair formula and in particular

`||P_+G_(F,a)||_2^2 >= pi sum_(d_j>a) m_j^2/(d_j-a)`.

For one defect this is `pi/(d-a)>=pi/d`, and as `a downarrow 0` below all depths of a finite subproduct the projected energy tends to one half of the canonical boundary energy. The escape from WI-428 is therefore geometric rather than functional-analytic: the probing line moves inside the defect depth while the projection itself remains bounded. Conversely, every fixed `a>0` is exactly blind after `P_+` to all defects with `0<d<a`, so a complete detector needs a predetermined family `a_n downarrow0`.

WI-430 extracts a global coercive consequence from that positive pair formula. For the finite set of zeros with depth `d_rho>a` and `|gamma_rho|<=T`, the projected energy `E_a(T)` obeys

`E_a(T) > [pi/(1/2-a)] N_(>a)(T)`

whenever the set is nonempty, with multiplicity counted in `N_(>a)(T)`. Each surviving zero therefore pays a uniform first-defect quantum `q(a)=pi/(1/2-a)`. For the extended monotone energy `E_a=sup_T E_a(T)`, finiteness is equivalent to having only finitely many zeros deeper than `a`, and the subquantum condition `E_a<=q(a)` already excludes every zero with `Re(s)>1/2+a`. In particular the formal boundary criterion `liminf_(a downarrow 0) E_a<=2pi` is equivalent to RH. This is diagnostic rather than progress toward RH: an unconditional source-side upper bound at or below that threshold would already contain the missing zero-exclusion theorem.

The live question is therefore deliberately weaker and localized: derive **source-side upper control for `E_a(T)` on a predetermined boundary-approaching family, with explicit joint dependence on `a` and `T`, without importing the unknown zero set into the probe choice**. WI-430 shows that the global `T->infinity` subquantum target is too strong to treat as a benign regularity estimate. The full zeta logarithmic derivative has poles and is not globally an ordinary `L^2` function on these lines, so WI-429's finite-product identity still does not furnish the source theorem. A successful route must localize or interpret the full source distributionally, price the approach `a_n downarrow0`, and obtain an arithmetic upper bound that can first be compared with the exact finite-height count coercivity. Fixed-safe-strip signed or non-diagonal processing remains excluded; a target-adaptive moving line would merely hide the unknown defect in the probe choice.
