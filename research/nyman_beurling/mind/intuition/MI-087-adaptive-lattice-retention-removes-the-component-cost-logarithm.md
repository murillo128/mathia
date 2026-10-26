# MI-087 — Adaptive lattice retention removes the component-cost logarithm

**Evidence level:** supported synthesis of the proved derivations in
[NB-356](../../findings/NB-356-finite-orbit-target-assembly-is-equivalent-to-a-reciprocal-phase-series.md),
[NB-368](../../findings/NB-368-cubic-logarithmic-seeds-give-deterministic-finite-energy-target-completion.md),
[NB-369](../../findings/NB-369-critical-return-energy-makes-three-orbit-lattice-truncation-logarithmically-sharp.md)
and [NB-370](../../findings/NB-370-adaptive-lattice-selection-removes-the-three-orbit-cutoff-logarithm.md).
The mechanism is classical return counting plus nonlinear approximation;
the two-budget comparison below is a synthesis deduction from those bounds,
not an independently reviewed finding or a claim of new general theory.

Fix positive phases `alpha,beta` with the simultaneous, all-integer bound

\[
R_n=\max(\|n\alpha\|_{\mathbb R/\mathbb Z},\|n\beta\|_{\mathbb R/\mathbb Z})
\ge\gamma n^{-1/2}\quad(n\ge1),\qquad \gamma>0.
\]

For `D_n^2=||n alpha||^2+||n beta||^2` and `w_n=1/(n^2 D_n^2)`, the same
sequence has two different sharp tails:

\[
\sum_{n>M}w_n\asymp_\gamma\frac{\log M}{M},\qquad
\inf_{|\Lambda|\le M}\sum_{n\notin\Lambda}w_n\asymp_\gamma M^{-1}
\quad(M\ge64).
\]

The logarithm measures the cost of retaining a contiguous prefix. It is
not forced by the number of retained indices alone. The distinction
survives optimization over every exact physical component split below.

The counting step must include the first return. If `R_(n_j)<=y<=1/2`,
the hypothesis applied to `n_1` and to successive differences gives
`n_1>=gamma^2/y^2` and `n_(j+1)-n_j>=gamma^2/(4y^2)`. Hence

\[
\#\{n<Y:R_n\le y\}\le4\gamma^{-2}Yy^2.
\]

For `w_n>X^(-2)`, one needs `R_n<X/n`. Counting first below `2X` and then
on `A<=n<2A`, `A=2^(j+1)X`, makes the remaining counts a geometric series:

\[
\#\{n:w_n>\lambda\}\le C_\gamma\lambda^{-1/2},\qquad
C_\gamma=2+8\gamma^{-2}.
\]

Thus the decreasing rearrangement satisfies

\[
\frac2{j^2}\le w_j^*\le\frac{C_\gamma^2}{j^2},\qquad
\frac2{M+1}\le\sum_{j>M}w_j^*\le\frac{C_\gamma^2}{M}.
\]

The lower rearrangement bound comes from the first `j` original indices,
each having `w_n>=2/n^2`; it needs no equidistribution. Together with
`w_n<=1/(gamma^2 n)`, it also puts every one of the `M` largest weights at
`n<=M^2/(2 gamma^2)`. Selection therefore has a finite quadratic search
horizon for the **globally largest** weights.

For an order-optimal cost, that search can be shortened. Define

\[
A_M=\inf_{|\Lambda|\le M}\sum_{n\notin\Lambda}w_n,\qquad
S_K=\sum_{n>K}w_n,\qquad
F_{M,K}=\inf_{\substack{\Lambda\subset\{1,\ldots,K\}\\|\Lambda|\le M}}
\sum_{n\notin\Lambda}w_n.
\]

For any nonnegative summable sequence with an attained best `M`-term set,

\[
\max(A_M,S_K)\le F_{M,K}\le A_M+S_K.
\]

The lower bounds respectively forget the search restriction and count the
unavoidable tail beyond `K`. For the upper bound, intersect a global
best `M`-term set with `{1,...,K}`; the newly omitted mass is at most `S_K`.
Selecting the largest `M` weights inside that prefix can only improve it.
Consequently NB-369 and NB-370 together give the uniform two-budget law

\[
\boxed{F_{M,K}\asymp_\gamma M^{-1}+\frac{\log K}{K}
\quad(K\ge M\ge64).}
\]

Thus a search horizon of order `M log M` is sufficient for the `1/M`
squared-cost order. It is also necessary up to constants: `F_(M,K)=O(1/M)`
forces `log(K)/K=O(1/M)` and hence `K=Omega(M log M)`, since `K>=M`.
This does not find the globally largest weights or the exact physical
optimizer. The horizon counts inspected indices, not comparison precision
or arithmetic operations.

To identify the physical quantity, fix `q>1`, put `p=q^alpha,r=q^beta`, and
use `H=L^2(0,1)`, `e=1`,

\[
g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a},\quad
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\}.
\]

Let `N=closure span{g_v:v>1}` and `t=P_N e`. Under the unitary Mellin map
`mathcal M`, one has

\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\qquad \mathcal Mt=Bb/s,
\]

where `H^2=H^2(Re s>1/2)`, `B` is the common zeta inner factor, `b=B(1)>0`, and

\[
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})}.
\]

At `z_k=1+2 pi i k/log q`, `k!=0`, the anchor factor `Theta_q` vanishes.
For finite `Lambda subset N_{>=1}`, let

\[
\mathcal H_\Lambda=\{V\in H^2:V(z_k)=0
\text{ for }k\ne0,\ |k|\notin\Lambda\},\qquad
\mathcal E_{v,\Lambda}=\mathcal M^{-1}(B\Theta_v\mathcal H_\Lambda).
\]

Writing `L=log q`, `C_q=L/(1-q^(-1))`, and

\[
T_{\Lambda^c}=\sum_{\substack{k\ne0\\|k|\notin\Lambda}}
\frac{|b/z_k|^2}{|\Theta_p(z_k)|^2+|\Theta_r(z_k)|^2}
\asymp_{q,\alpha,\beta,b}\sum_{n\notin\Lambda}w_n,
\]

the bounded sampler and its bounded right inverse give

\[
C_q^{-1}T_{\Lambda^c}\le
\inf_{\substack{u_v\in\mathcal C_v\\u_q+u_p+u_r=t}}
\sum_{v=p,r}\operatorname{dist}_H(u_v,\mathcal E_{v,\Lambda})^2
\le(q/L)T_{\Lambda^c}.
\]

The lower bound uses Cauchy--Schwarz at every omitted lattice point for
**any** exact split. The upper bound uses one fixed exact split obtained
by lifting the complete minimum-norm sample data; that split works for
every `Lambda`. Explicitly, with
`a_k=|Theta_p(z_k)|^2+|Theta_r(z_k)|^2`, set
`d_(v,k)=(b/z_k) conjugate(Theta_v(z_k))/a_k` for `k!=0` and `d_(v,0)=0`.
Here `R_q` is NB-356's explicit bounded lattice right inverse.
The non-anchor Hardy components are `U_v=R_q d_v`; the fixed anchor is
`U_q=(b/s-Theta_p U_p-Theta_r U_r)/Theta_q`. Their selected approximants are

\[
h_{v,\Lambda}=\mathcal M^{-1}
\bigl(B\Theta_vR_q(d_v\mathbf1_{\{|k|\in\Lambda\}})\bigr),\qquad v=p,r.
\]

The physical anchor is `u_q=mathcal M^(-1)(B Theta_q U_q)`.

Taking the infimum over subsets of `{1,...,K}` in the physical comparison
transports the same two-budget law, with constants also depending on
`q,alpha,beta,b`. Choosing the largest `M` weights in that prefix attains
its order; it need not minimize the physical norm exactly. The selector
uses only the phases; constructing the physical vectors still uses `B` and `b`.

The cubic pair `(alpha,beta)=(cuberoot(2),cuberoot(4))` satisfies the
hypothesis by NB-368's algebraic norm argument. Mere convergence of
`sum w_n`, rational independence, or an almost-everywhere completion
theorem does not supply the all-integer bound or this adaptive rate for
the particular integer seeds `2,3,5`.

The budget is `M` positive lattice indices shared by two components,
equivalently `2M` nonzero slots. Each `E_(v,Lambda)` still contains an
infinite-dimensional sampler kernel, the value at `z_0=1` is free, and the
anchor is unrestricted. These are squared component distances, not a
lower bound on the residual of their sum: component errors may cancel.
No finite-dilation upper approximation rate follows from lattice selection.
Every orbit sum `w` retains
`||e-w||^2=1-b^2+||t-w||^2`, so the Burnol floor is unchanged.

[NB-371](../../findings/NB-371-critical-line-zeros-force-unbounded-finite-dilation-synthesis-cost.md)
prices the missing coefficient resource in this exact normalization. For
any finite sum, allowing arbitrary real seeds `v_nu>1` and dilations
`a_nu>=1`, put

\[
w=\sum_{\nu=1}^J c_\nu A_{a_\nu}g_{v_\nu},\quad
Q=\sum_\nu|c_\nu|(v_\nu^{-1}+v_\nu^{-1/2}),\quad
S=\sum_\nu|c_\nu|,\qquad Q\le2S.
\]

On `s=1/2+iy`, dilation has unit modulus and

\[
\mathcal M(A_ag_v)(s)=a^{1/2-s}\frac{\zeta(s)}s(v^{-1}-v^{-s}),
\qquad |\mathcal Mt(s)|=b/|s|\quad\text{a.e.}
\]

Thus a fixed budget cannot fill the target's modulus near a critical-line
zero:

\[
\|t-w\|^2\ge\frac1{2\pi}\int_{\mathbb R}
\frac{[b-Q|\zeta(1/2+iy)|]_+^2}{|1/2+iy|^2}\,dy
\ge c_{\rho,b}(1+Q)^{-1/m},
\]

where `rho` is any one fixed critical-line zero of multiplicity `m`.
The last estimate integrates a mismatch of fixed height over an interval
of width comparable to `(1+Q)^(-1/m)`. It is not point evaluation on the
Hardy boundary. Infinitely many critical-line zeros are known without RH;
simplicity is not assumed.

Consequently any finite synthesis of the **final target** with
`||t-w_M||=O(M^(-1/2))` requires `S_M=Omega(M^m)`, hence at least
`Omega(M)`. If its coefficient Euclidean norm is at most `C_M`, then
`S_M<=sqrt(J_M) C_M` gives `J_M C_M^2=Omega(M^(2m))`.
This is uniform over the selected lattice sets because it tests `t`, not
the separate component errors. It does not give a column-count bound
without coefficient control, a maximal-dilation bound, or a matching upper
synthesis rate. Rescaling the generators would change this budget.

Even a **fixed nonzero finite lift** already lies outside every bounded
same-seed coefficient closure. With `E` its finite nonzero data support,

\[
R_qd(s)=\frac{1-q^{1-s}}{\log q}
\sum_{k\in E}\frac{d_k}{s-z_k}.
\]

The rational numerator has degree at most `|E|-1`; the prefactor has no
critical-line zeros. Some critical-line zeta zero therefore leaves
`R_qd` nonzero. Integrating the same mismatch for
`h=mathcal M^(-1)(B Theta_v R_qd)` gives a positive distance from every
fixed `sum|c_nu|` budget in `span{A_a g_v}`. Hence finite interpolation
support does not mean a finite generator sum, or a finite-total-variation
mixture of dilations. The zero and constant may depend on the lift; this
argument supplies no uniform component bound as `Lambda` grows.

[NB-372](../../findings/NB-372-bounded-effective-dilation-range-retains-a-strict-projected-target-gap.md)
adds an independent range restriction, even with unbounded coefficients
and column counts. For every finite `R>1`, put

\[
\mathcal W_R=\overline{\operatorname{span}}
\{A_ag_v:a\ge1,\ v>1,\ av\le R\}
=\overline{\operatorname{span}}\{g_v:1<v\le R\},\qquad
\Delta_R=\operatorname{dist}(t,\mathcal W_R)>0.
\]

The second equality uses `A_a g_v=sqrt(a)(g_(av)-v^(-1)g_a)`.
The obstruction survives Hilbert closure because the inverse source
retains its support, not because coefficients remain bounded. Under
`Uf(u)=e^(-u/2)f(e^(-u))`, extended by zero for `u<0`, define

\[
\mathfrak m=\sum_{n\ge1}\mu(n)n^{-1/2}\delta_{\log n},\qquad
\mathscr I h=\mathfrak m*(\partial_u+1/2)h.
\]

This is continuous from `L^2` to distributions on each compact interval:
only finitely many atoms contribute there. Direct floor-function
cancellation gives

\[
\mathscr I U(A_ag_v)
=v^{-1}\delta_{\log a}-v^{-1/2}\delta_{\log(av)}.
\]

Thus every `w in W_R` has inverse source supported in `[0,log R]`, even
when colliding parameters and diverging coefficients produce distributional
limits rather than measures. If `nu_t=mathscr I Ut` had compact support,
its transform `E(s)=<nu_t,e^(-(s-1/2)u)>` would be entire, with
`E(s)=bB(s)/zeta(s)` for `Re s>1`. Continuation and the a.e. inner boundary
modulus would force `|zeta(1/2+iy)E(1/2+iy)|=b` everywhere by continuity,
contradicting a critical-line zero. This uses no boundary-point evaluation
of a general Hardy function and no continuation of `B` across that zero.

A test `phi in C_c^infinity((log R,infinity))` with
`nu_t(conjugate(phi))!=0` yields a bounded Hilbert dual. If its support is
below `T`, set

\[
\psi_\phi(u)=\sum_{n\le e^T}\frac{\mu(n)}{\sqrt n}
[-\phi'(u+\log n)+\phi(u+\log n)/2],\qquad u\ge0.
\]

Then `Delta_R>=|nu_t(conjugate(phi))|/||psi_phi||_2>0`.
Finding this tail response is existential and depends on the projected
target. NB-372 obtains a quantitative bound by testing the **approximant's
compact source** instead. Put `T=log R` and choose a smooth cutoff `chi_T`
equal to one near `[0,T]`, supported in `(-1,T+1)`, with
`0<=chi_T<=1` and `|chi_T'|<=4` on the positive half-line. For
`s_y=1/2+iy` and `w in W_R`, integration by parts gives

\[
E_w(s_y)=\langle\mathscr I Uw,e^{-iyu}\rangle
=\int_0^\infty Uw(u)q_{R,y}(u)\,du,
\]
\[
q_{R,y}(u)=\sum_{n\le eR}\frac{\mu(n)}{\sqrt n}
 e^{-iy(u+\log n)}
 [s_y\chi_T(u+\log n)-\chi_T'(u+\log n)].
\]

This is a bilinear pairing. The cutoff is one on a neighborhood of the
support, so endpoint distributional derivatives are retained. The bound
`sum_(n<=e^(T+1-u)) n^(-1/2)<=2e^((T+1-u)/2)` yields

\[
K_R(y):=\|q_{R,y}\|_2\le2\sqrt{eR}(|s_y|+4).
\]

Integrating this decaying envelope avoids a spurious `sqrt(log R)` loss.
For the projection `w_R=P_(W_R)t`, `||w_R||<=b` and
`mathcal M w_R= zeta E_(w_R)/s`; hence

\[
\Delta_R^2\ge\frac{b^2}{2\pi}\int_{\mathbb R}
\frac{[1-|\zeta(s_y)|K_R(y)]_+^2}{|s_y|^2}\,dy
\ge c_\rho R^{-1/(2m)}.
\]

The second inequality integrates over a width `asymp_rho R^(-1/(2m))`
near a fixed critical-line zero `rho` of multiplicity `m`. The constant
can be independent of the unknown inner factor: `g_2 in N` gives
`b^2>=|<e,g_2>|^2/||g_2||^2=log 2`. Thus the rate holds without RH,
even above a positive Burnol floor. It is a necessary lower bound, not a
sharp rate or an improvement of the classical logarithmic rate under RH.

For a finite synthesis of effective range at most `R`, the two necessary
costs give the simultaneous lower bound

\[
\|e-w\|^2\ge1-b^2+
\max\{c_\rho R^{-1/(2m)},\ c_{\rho,b}(1+Q)^{-1/m}\}.
\]

The resources are therefore distinct: retained lattice count `M`, search
horizon `K`, generator coefficients, and effective range `max(av)`.
Final-target error `epsilon` requires `R=Omega_rho(epsilon^(-4m))`;
error `O(M^(-1/2))` therefore needs both `R_M=Omega_rho(M^(2m))` and
`S_M=Omega(M^m)`. In particular the range is at least quadratic in `M`
without assuming simplicity. For fixed seeds this also prices `max(a)`;
variable seeds can instead enlarge `v`. The physical range `av` is not
the lattice search horizon `K`: the `M log M` selection law does not
supply finite synthesis within that physical range. Conversely
`Delta_R->0` as `R->infinity`, by full-space density.
Neither restriction removes the Burnol floor, supplies an upper synthesis,
or quantifies column count without coefficient control. A cutoff bound for
distance to `e` cannot simply be reduced by the positive floor to obtain a
rate for `Delta_R`. These are source-backed necessary costs, not a measured
improvement in research utility.
