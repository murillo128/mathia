# MI-015 — Prime-phase worst starts are constant-factor equivalent to a real-elliptope problem for symmetric tapers

**Evidence level:** exact finite-dimensional reduction from VIS-213, exact holonomy and certificate hierarchy through VIS-221, classical symmetric-Grothendieck comparison specialized in [VIS-222](../../findings/VIS-222-symmetric-grothendieck-constant-factor-sdp-torus-equivalence.md), and the exact midpoint-gauge/real-elliptope reduction in [VIS-223](../../findings/VIS-223-midpoint-symmetric-taper-real-elliptope.md). No prime-specific asymptotic SDP estimate, recurrence-time theorem or RH consequence is claimed.

For fixed `y,H`, VIS-213 identifies the worst start exactly with the unit-modulus quadratic optimum

`M_abs(A_(y,H)) = max_(|z_p|=1) |z^*A_(y,H)z|`.

Kronecker density settles equality of the one-parameter supremum with this finite torus optimum; it does not determine its size or the time required to approach a near-maximizer.

VIS-214--VIS-221 build increasingly faithful static relaxations. Cycle holonomy is the gauge-invariant obstruction to coefficient-envelope attainment; fractional cycle packing and the normalized magnetic relaxation are provably too weak in the live prime regime; the full correlation SDP

`U_abs(A)=max_(X>=0, diag(X)=1)|Tr(A X)|`

retains all pair correlations. VIS-222 removes objective-scale ambiguity through

`M_abs(A)<=U_abs(A)<=K_gamma^C M_abs(A)`, `K_gamma^C<=8/pi-1`.

Thus high SDP rank may obstruct exact optimizer recovery but cannot create an unbounded multiplicative gap in the objective value.

VIS-223 shows that the canonical symmetric-taper matrices carry less genuine complex phase than their uncentered formula suggests. For a real taper `v`, midpoint centering gives

`kappa_v(u)=e^(iu/2)[C_v(u)+iS_v(u)]`.

The linear factor `e^(iu/2)` is a vertex coboundary: in the prime graph it is removed exactly by the diagonal gauge `D_H=diag_p e^(iH log p/2)`. If the taper is midpoint-symmetric, `S_v=0`, so

`A_(y,H)=D_H^* B_(y,H) D_H`

with `B` real symmetric. This is not merely a cosmetic real form. For any complex correlation matrix `Y`, `Re(Y)` is a real correlation matrix and a real symmetric `B` satisfies `Tr(BY)=Tr(B Re(Y))`. Therefore

`U_abs(A)=U_abs(B)=max_(X in E_n^R)|Tr(BX)|`.

The exact torus variables remain continuous phases; the reduction does **not** turn the primal problem into an Ising sign optimization. What becomes real is the coefficient matrix and the complete SDP relaxation.

For the quadratic taper `w(x)=6x(1-x)`, the centered transform is

`r_w(u)=12[2 sin(u/2)-u cos(u/2)]/u^3`.

Hence the switched prime matrix is a real signed ratio-shell kernel and its edge signs change only across the deterministic roots `tan(u/2)=u/2`. Cycle holonomy correspondingly collapses from arbitrary `U(1)` gain to the parity of negative edges, `+-1`.

This changes the matched-control discipline. A generic independent complex phase scramble is a broad optimization control, but it is no longer representation-matched to the symmetric-taper branch because it introduces continuous edge phase absent after canonical centering. A sharper null should preserve the edge-magnitude profile and real signed-shell class while perturbing the arithmetic organization.

The live static problem is therefore to determine

`U_abs(B_(y,H))/sqrt(R_v(y,H))`

inside the real elliptope. By VIS-222, boundedness or divergence transfers within a universal constant to the exact worst-start torus objective. Rank-one stress remains useful only for exact finite optimizer recovery, while one-parameter access time is a separate simultaneous-Diophantine issue.

**Boundary.** The real reduction requires midpoint symmetry. For asymmetric tapers the centered odd part `S_v` can carry genuine continuous edge phase. Zeros of the centered transform delete edges, and the signed-shell representation does not make the optimization easy. The result removes a representation artifact; it does not estimate the prime-specific elliptope value.