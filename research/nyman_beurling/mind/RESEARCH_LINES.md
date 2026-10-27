# Nyman--Beurling research lines

This file records the current mathematical questions that survive the Nyman--Beurling evidence. It is not a roadmap, task queue, status page, or history.

## Keep aggregate Ford coverage separate from Hardy coercivity

NB-264--NB-272 show that large aggregate Ford response can coexist with a vanishing positive Hardy quadratic signal. Resolved shell bands can carry order-one point residue while their projected `H^2` energy leaks with rank, and positive band-diagonal repairs need rank-growing strength to restore a uniform anchored floor. The live destination-side fork remains: either the canonical target quantities themselves stay order one in the moving regime, or a new exact source component supplies the missing rank-growing Gram strength.

## Determine the singular-spectrum transition and actual target occupation

NB-306 identifies the exact unit singular core of the projected integer-dilation operator: singular value `1` persists precisely through `2m<=N`, with unit right-singular subspace `U_floor(N/m)`. NB-309 gives a polynomial lower bound on the first post-core gap, NB-311 shows that the first post-core strip remains near-isometric for every sublinear additive overrun, and NB-312--NB-313 rule out complete source-overlap collapse on every bounded linear dilation scale. NB-314--NB-315 identify the far-external superquadratic regime as asymptotically rank one after the correct `sqrt(m)` normalization.

NB-316--NB-329 then show that the most obvious primitive, denominator and phase effects do not create a clean transition inside the subquadratic window. The centered Cesaro primitive has sharp `Theta(N^(3/2))` growth, exact divisor folds and the full lattice `m=d(n-1)` retain a canonical `1/sqrt(log n)` rank-one-error resonance, and moving one selector cell to `m=dn` flips the adjacent coefficient's sign. On the intermediate cell `m=d(n-1)+r`, `rho=r/d`, the outer adjacent coefficient is `(1-2rho)log 2/(4n)+O(d/n^2)`, so that particular channel vanishes at half drift.

NB-330 proves that this half-cell zero is only witness cancellation. Shifting the target inward by one adjacent mode produces a cell coefficient independent of `rho`, with

`F_(n,d,r)=-log(2)/(4(n-1))+O(d/(n-1)^2)`,

uniformly across the entire drift cell. Consequently every sequence `d_n=o(n)` retains the same logarithmic operator obstruction even at the outer witness's half-cell zero.

NB-331 removes the remaining gaps between those one-cell bands. The same intrinsic adjacent-index calculation works at any `8<=q<=n`: if `m=dq+r`, `0<=r<=d`, the `q`-adjacent witness has the same leading coefficient with error `O(d/q^2)`. For every integer sequence

`n <= m_n = o(n^2)`

one can choose an explicit adaptive inner index `q_n<=n` so that

`q_n <( (sqrt(m_n) T_(n,m_n)-R_n) g_2, nu_(q_n) ) -> -log(2)/4`

and therefore

`liminf sqrt(log n) ||sqrt(m_n)T_(n,m_n)-R_n|| >= sqrt(log 2)/(2 sqrt 2)`.

Thus there is **no faster-mixing external subquadratic window at the operator-norm level** detectable by escaping between the previous resonant lattices: every `n<=m=o(n^2)` carries an adaptive adjacent resonance of the same logarithmic scale. The bound still tends to zero, so it does not prove a fixed positive norm gap.

NB-332's critical-lattice coefficient has the sign-definite profile `Phi(delta)=-(4delta)^(-1) sum_(k>=1)||k delta||_Z^2/k^2`; its integer zeros concern one *fixed* adjacent observer, not the optimized operator. [NB-340](../findings/NB-340-interior-phase-routing-blocks-faster-quadratic-mixing.md) routes around all such zeros by selecting an interior `q asymp_B n` in the original Nyman section. For every fixed `B>0` it obtains the **uniform bounded-quadratic-window obstruction**

`liminf_(n->infinity) sqrt(log n) inf_(n<=m<=B n^2) ||sqrt(m)T_(n,m)-R_n|| >= c_B>0`.

The constant may depend on `B`; this is an operator-source lower bound of order `1/sqrt(log n)`, **not** a nonzero limiting gap. In particular, the previous open question of whether the integer nodes survive optimization over admissible interior witnesses is answered negatively at this scale.

[NB-343](../findings/NB-343-variable-order-reciprocal-equidistribution-reaches-superpolynomial-dilations.md) extends the source-side obstruction with a changing weight. For each fixed `0<eta<1`, put `M_n=floor(n^((1-eta)log_2(log n)))`. Then `inf_(n<=m<=M_n)(1+m/n^2)sqrt(log n)||sqrt(m)T_(n,m)-R_n||>=c>0` for an absolute `c` and sufficiently large `n` (depending on `eta`). The `n^2/m` dilution beyond the quadratic scale is indispensable: this does **not** imply an unweighted `1/sqrt(log n)` bound at superpolynomial dilation.

The residue class of the source's adjacent phase also matters after scaling. [NB-346](../findings/NB-346-fixed-rational-offsets-have-unbounded-dilation-parity-law.md) gives a logarithmically growing normalized coefficient at fixed rational offsets with **even** reduced denominator, but a finite limit when it is odd, uniformly over unrestricted growth of the integer dilation multiplier. [NB-347](../findings/NB-347-parity-divisor-fourier-regularity-gives-generic-finite-offset-limit.md) identifies the Fourier coefficients of the phase profile `D(x)=sum_(k>=1)||kx||_Z^2/k^2`, proves `D in H^1(T)` with `int_0^1 |D'(x)|^2 dx=pi^2/18`, and obtains the finite adjacent coefficient `L(t)=-(pi^2/72-D(t))/2-t D'(t)/4` at almost every offset. This is not a uniform bound: `L(t)` is essentially unbounded **in both signs** on each nonempty open offset interval; its nonvanishing is established only on an explicit positive-measure subset, not almost everywhere.

The remaining gap is **target occupation**, not the integer-node loophole. All of NB-340--NB-347 concern the available compressed source/observer operator. A Nyman--Beurling target-distance consequence still requires the physical first-free Ford datum to occupy the obstructed modes after sampling/null decomposition, lower-section conditioning and off-critical contraction. The exact transition beyond the weighted superpolynomial range is likewise not settled by these results.

## Convert selected lattice components into finite dilation combinations

[MI-087](intuition/MI-087-adaptive-lattice-retention-removes-the-component-cost-logarithm.md) combines NB-369 and NB-370 into the two-budget comparison `F_(M,K) asymp 1/M+log(K)/K`, where `M` positive lattice indices may be retained inside the search prefix `{1,...,K}`. The hypothesis is `max(||n alpha||,||n beta||)>=gamma/sqrt(n)` for every positive integer. A horizon of order `M log M` is necessary and sufficient, up to constants, for squared component cost of order `1/M`; the quadratic horizon for finding the globally largest weights is a different requirement.

For the specified cubic seeds, what joint coefficient, column-count and maximal-dilation budgets suffice to replace the selected vectors `h_(p,Lambda),h_(r,Lambda)` and the fixed anchor `u_q` by finite combinations of `A_a g_v`, with additional total `L^2` error `O(M^(-1/2))` when `K asymp M log M`? [NB-371](../findings/NB-371-critical-line-zeros-force-unbounded-finite-dilation-synthesis-cost.md), retained in MI-087, already forces `S_M=sum|c_nu|=Omega(M)` for any resulting approximation to `t` at that accuracy, with all seeds and dilation ranges allowed. A fixed critical-line zero of multiplicity `m` strengthens this to `Omega(M^m)`; an Euclidean coefficient bound `C_M` implies `J_M C_M^2=Omega(M^(2m))`. Can an upper synthesis control these resources together? No sharpness of the lower coefficient exponent is known here.

Every fixed nonzero finite lattice lift also has positive distance from each bounded same-seed absolute-coefficient closure, although its closed-orbit approximation exists. The component's zero and lower-bound constant need not be uniform as the selection grows; use the final-target bound for the uniform budget. Neither the lattice-slot law nor this necessary conditioning cost supplies a finite-generator upper rate or a source-only construction of the common inner factor `B`. The Burnol floor remains `1-b^2`.

[NB-372](../findings/NB-372-bounded-effective-dilation-range-retains-a-strict-projected-target-gap.md), also retained in MI-087, prices the effective range `R=max(a_nu v_nu)` with unlimited coefficients and columns. Local Möbius inversion and a cutoff dual give the all-range certificate `Delta_R^2>=c_rho R^(-1/(2m))`. More strongly, local Fourier regularity transfers Burnol's duals to the actual projected target and yields `liminf_(R->infinity)(log R)Delta_R^2>=b^2 sum_(rho in F)m_rho^2/|rho|^2` for every fixed finite critical-zero set `F`, without assuming finitely many off-critical zeros. Thus error `O(M^(-1/2))` requires **exponential** effective range `R_M>=exp(cM)` eventually, together with `S_M=Omega(M^m)`. For fixed cubic seeds the maximal dilation has the same exponential cost; with variable seeds only `av` is constrained. Can a joint finite-generator upper synthesis attain the required accuracy with `log R_M=O(M)`, or does its geometry force a larger range? The onset of the logarithmic lower estimate is not effective here, and no upper synthesis or source-only construction of `B` follows. Physical range remains distinct from the `M log M` lattice search horizon; the estimate bounds excess above the Burnol floor itself.
