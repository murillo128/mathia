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

The resulting three resources remain distinct: `M` retained indices,
`K asymp M log M` inspected indices for order-optimal component cost,
and the necessarily divergent generator coefficient budget. Closed-orbit
approximation survives because its coefficient budgets may diverge; the
critical-zero obstruction is a conditioning cost above the Burnol floor,
not a positive distance from the full closed orbit. These are source-backed
necessary bounds, not a measured improvement in research utility.
