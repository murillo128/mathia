# NB-108 — fixed confluent state subspaces remain target-poor after full backfill

**Status:** `EXACT-DERIVED + NYMAN-FINITE-WINDOW-GRAM + ACTUAL-NYMAN-SOURCE-WHEN-MULTIPLICITY-IS-PRESENT + FIXED-CONFLUENT-MULTIPLICITY + FULL-EARLY-CELL-BACKFILL + TARGET-AWARE-STATE-SUBSPACE + SHARP-FINITE-RANK-PARETO-FRONTIER + NEGATIVE/METHOD-BOUNDARY`.

`NB-107` closes the most obvious rank-one repair of the one-zero state channel: restoring every earlier integer cell down to a fixed natural scale does not rotate the maximal one-zero state toward the Nyman target. It explicitly leaves open a qualitatively different escape: a repeated zero, or an exact confluence of several zero states, produces a derivative/Jordan state **subspace** rather than one state vector. A badly chosen coordinate basis for that subspace can be singular even when its span is well behaved, so the rank-one angle calculation cannot simply be repeated coordinate by coordinate.

For every fixed confluent multiplicity the escape still fails in the boundary regime controlled by `NB-104`. The terminal ordinate-scale band supplies a uniformly nondegenerate Laguerre Gram for the whole derivative-state span, while the pairing of **every** fixed derivative state with the fully backfilled target is killed by the large Mellin frequency. Consequently the principal angle between the entire fixed-dimensional confluent state space and the target tends to `pi/2`.

More precisely, fix integers `d>=1` and `r>=1`. Let

\[
\lambda_j=a_j+i\Gamma_j,
\qquad
\rho_j=\lambda_j+\frac12,
\qquad
0<a_j<\frac12,
\qquad
a_j\to0,
\qquad
G_j:=|\Gamma_j|\to\infty,
\tag{1}
\]

put

\[
m_j=\lceil G_j\rceil,
\qquad
R_j=m_jq_j,
\qquad
2a_j\log q_j\to L\in(0,\infty),
\tag{2}
\]

and use the complete backfilled cell space

\[
\mathcal E_{r,R_j}
=
\operatorname{span}\{\phi_n:r\le n<R_j\},
\qquad
\phi_n(t)=e^{-t/2}\mathbf 1_{[\log n,\log(n+1))}(t).
\tag{3}
\]

For `0<=k<d`, define the confluent state representer `w_(k,j) in E_(r,R_j)` by its values on the orthogonal cell basis,

\[
\boxed{
\langle \phi_n,w_{k,j}\rangle
=
\sqrt{2a_j}\,m_j^{\lambda_j}
\int_n^{n+1}
\bigl(2a_j\log(t/m_j)\bigr)^k
 t^{-\lambda_j-3/2}\,dt.
}
\tag{4}
\]

Let

\[
\mathcal S_j:=\operatorname{span}\{w_{0,j},\ldots,w_{d-1,j}\}
\tag{5}
\]

and let

\[
e_{r,R_j}=e^{-t/2}\mathbf 1_{[\log r,\log R_j)}
=\sum_{n=r}^{R_j-1}\phi_n
\tag{6}
\]

be the visible target. Then

\[
\boxed{
\frac{\|P_{\mathcal S_j}e_{r,R_j}\|^2}
     {\|e_{r,R_j}\|^2}
\longrightarrow0.
}
\tag{7}
\]

The basis `(4)` is the derivative basis of the analytic confluent state packet used in `NB-103`--`NB-104`, up to harmless nonzero row scalings. If `rho_j` is an actual zeta zero of multiplicity at least `d`, division by the repeated elementary factor `b_(lambda_j)^d` is legitimate and the finite-prefix leakage state range of that repeated factor is exactly `S_j`: expanding

\[
\frac1{b_\lambda(z)^d}
=
\left(1+\frac{2a}{z-\lambda}\right)^d
\tag{8}
\]

shows that its state kernels are the polynomial-exponential modes `t^k e^(lambda t)`, `0<=k<d`, whose cell averages are precisely the confluent span `(4)` after triangular rescaling. Thus `(7)` is a source-compatible obstruction for genuine repeated off-critical zeros, not only an analytic continuation of a determinant.

There is also a sharp finite-rank analogue of the `NB-107` leverage-target frontier. Let `B_j>=0` be any positive state update on `E_(r,R_j)` with

\[
\operatorname{ran}B_j=\mathcal S_j,
\tag{9}
\]

in particular the repeated-factor update just described. For nonzero `f`, define

\[
\eta_j(f)
:=
\frac{\langle B_jf,f\rangle}
     {\|B_j\|\,\|f\|^2},
\qquad
\chi_j(f)
:=
\frac{|\langle e_{r,R_j},f\rangle|^2}
     {\|e_{r,R_j}\|^2\,\|f\|^2}.
\tag{10}
\]

Then for every fixed `theta in (0,1]`,

\[
\boxed{
\sup_{\eta_j(f)\ge\theta}\chi_j(f)
=
1-\theta+o(1).
}
\tag{11}
\]

Hence moving from one state to any **fixed-dimensional confluent/Jordan state packet** does not create target coercivity. As in rank one, target-poorness follows only for vectors that carry an asymptotically full fraction of the available state leverage.

## 1. The terminal band uniformly conditions the entire confluent span

Because the cells `(3)` are orthogonal and

\[
\|\phi_n\|^2=\frac1{n(n+1)},
\tag{12}
\]

the Gram matrix of the state basis `(4)` on any set of cells is obtained by multiplying the cell pairings by `n(n+1)` and summing. On the terminal cells `m_j<=n<R_j`, this is **exactly** the matrix `K^(m,q,lambda)` of `NB-104`:

\[
K^{\rm term}_{j;k\ell}
=
2a_j\sum_{n=m_j}^{R_j-1}
 n(n+1)\Phi_{k,n}\overline{\Phi_{\ell,n}},
\tag{13}
\]

with the same `Phi_(k,n)` as in that finding.

Here the ordinate delay is

\[
y_j
=2a_j\log^+\!\left(\frac{G_j}{m_j}\right)=0,
\tag{14}
\]

while the available radial depth tends to `L`. Therefore `NB-104` gives entrywise

\[
\boxed{
K^{\rm term}_{j;k\ell}
\longrightarrow
M_{d,L;k\ell}
:=
\int_0^L u^{k+\ell}e^{-u}\,du.
}
\tag{15}
\]

The limit is the Gram matrix of `1,u,...,u^(d-1)` in `L^2([0,L],e^{-u}du)`, hence is positive definite. Thus for some constant `c_(d,L)>0`,

\[
K_j^{\rm term}\succeq c_{d,L}I_d
\tag{16}
\]

for all sufficiently large `j`.

Let `K_j^full` be the Gram matrix of the same state vectors after all cells `r<=n<R_j` are restored. Earlier cells add another positive semidefinite Gram matrix, so

\[
\boxed{
K_j^{\rm full}\succeq K_j^{\rm term}\succeq c_{d,L}I_d.
}
\tag{17}
\]

This is the key basis-invariant point. Backfill may make some state coordinates huge, and canonical distinct-node coordinates can become ill-conditioned during confluence, but it cannot create a small singular direction in this divided-derivative basis because the terminal band already carries a fixed positive Laguerre volume in **every** confluent direction.

## 2. Every fixed derivative state has vanishing target pairing

The target sum over cells telescopes into one oscillatory integral. From `(4)` and `(6)`,

\[
\boxed{
b_{k,j}
:=\langle e_{r,R_j},w_{k,j}\rangle
=
\sqrt{2a_j}\,m_j^{\lambda_j}
\int_r^{R_j}
\bigl(2a_j\log(t/m_j)\bigr)^k
 t^{-\rho_j-1}\,dt.
}
\tag{18}
\]

Put

\[
P_{k,j}(t)=\bigl(2a_j\log(t/m_j)\bigr)^k,
\qquad
I_{k,j}=\int_r^{R_j}P_{k,j}(t)t^{-\rho_j-1}\,dt.
\tag{19}
\]

Integration by parts uses

\[
P'_{k,j}(t)=\frac{2a_jk}{t}P_{k-1,j}(t)
\]

and gives the exact recurrence

\[
\boxed{
I_{k,j}
=
\frac{P_{k,j}(r)r^{-\rho_j}-P_{k,j}(R_j)R_j^{-\rho_j}}
     {\rho_j}
+
\frac{2a_jk}{\rho_j}I_{k-1,j},
}
\tag{20}
\]

with

\[
I_{0,j}=\frac{r^{-\rho_j}-R_j^{-\rho_j}}{\rho_j}.
\tag{21}
\]

Since `|rho_j|~G_j~m_j`, `2a_j<=1`, and

\[
|P_{h,j}(r)|
\le \log(m_j/r)^h,
\qquad
P_{h,j}(R_j)
=(2a_j\log q_j)^h=O_{h,L}(1),
\tag{22}
\]

iteration of `(20)` yields, for each fixed `k`,

\[
|I_{k,j}|
\ll_{k,r,L}
\frac{r^{-a_j-1/2}(1+\log^k m_j)
      +R_j^{-a_j-1/2}}
     {G_j}.
\tag{23}
\]

Multiplying by the prefactor in `(18)` and using `m_j^{a_j}/G_j<=m_j^{-1/2}(1+o(1))`, because `a_j<1/2`, gives

\[
\boxed{
|b_{k,j}|
\ll_{k,r,L}
\sqrt{a_j}\,m_j^{-1/2}(1+\log^k m_j)
+o(1)
\longrightarrow0.
}
\tag{24}
\]

The large ordinate therefore kills not only the basic state-target coupling of `NB-107`, but every fixed polynomial derivative of that state. The possible growth of the derivative weights on the early cells is only polylogarithmic; the Mellin integration-by-parts factor `1/|rho_j|` beats it uniformly at every fixed derivative order.

## 3. The whole state-subspace principal angle tends to ninety degrees

Let

\[
b_j=(b_{0,j},\ldots,b_{d-1,j})^T.
\tag{25}
\]

For a nonorthogonal spanning family with Gram `K_j^full`, the squared norm of the orthogonal projection of the target onto its span is

\[
\|P_{\mathcal S_j}e_{r,R_j}\|^2
=b_j^*(K_j^{\rm full})^{-1}b_j.
\tag{26}
\]

Equations `(17)` and `(24)` imply

\[
\|P_{\mathcal S_j}e_{r,R_j}\|^2
\le c_{d,L}^{-1}\|b_j\|^2
\longrightarrow0.
\tag{27}
\]

Meanwhile

\[
\|e_{r,R_j}\|^2
=\frac1r-\frac1{R_j}
\longrightarrow\frac1r.
\tag{28}
\]

This proves `(7)`. In particular, if

\[
\delta_j
:=
\frac{\|P_{\mathcal S_j}e_{r,R_j}\|}
     {\|e_{r,R_j}\|},
\tag{29}
\]

then `delta_j->0` independently of the coordinate conditioning used to represent the confluent packet.

This is stronger than proving that each chosen basis vector is individually target-poor: `(17)` prevents a linear combination of those vectors from hiding a target-bearing direction through cancellation of the state coordinates.

## 4. The sharp Pareto frontier is dimension-free once the subspace angle is known

Let `P_j=P_(S_j)`. Because `B_j>=0` and `ran B_j=S_j`,

\[
0\preceq B_j\preceq\|B_j\|P_j.
\tag{30}
\]

Hence every unit vector with `eta_j(f)>=theta` has

\[
s_j:=\|P_jf\|^2\ge\theta.
\tag{31}
\]

Write the normalized target as

\[
\widehat e_j
=P_j\widehat e_j+(I-P_j)\widehat e_j,
\qquad
\|P_j\widehat e_j\|=\delta_j.
\]

Cauchy--Schwarz gives, for any unit `f`,

\[
\sqrt{\chi_j(f)}
\le
\delta_j\sqrt{s_j}
+
\sqrt{1-\delta_j^2}\sqrt{1-s_j}.
\tag{32}
\]

For fixed `theta>0` and large `j`, the right side is decreasing for `s_j>=theta`, so `(31)` implies

\[
\sup_{\eta_j(f)\ge\theta}\chi_j(f)
\le1-\theta+o(1).
\tag{33}
\]

The bound is sharp. Choose a unit top eigenvector `u_j in S_j` of `B_j`, and let `z_j` be the normalized projection of the target onto `S_j^perp`. Then

\[
f_j=\sqrt\theta\,u_j+\sqrt{1-\theta}\,z_j
\tag{34}
\]

has `eta_j(f_j)=theta`, while `(7)` gives

\[
\chi_j(f_j)=1-\theta+o(1).
\tag{35}
\]

This proves `(11)`. The rank-one formula of `NB-107` is therefore not a peculiarity of a one-dimensional state: after the source-specific principal angle has collapsed, the normalized leverage-target frontier is the same for every fixed finite rank.

## 5. Prior-art boundary, controls, and what remains open

Derivative reproducing kernels for repeated Blaschke zeros, polynomial-exponential Jordan states, confluent Cauchy matrices, and principal-angle geometry are classical Hardy/model-space structures. No novelty is claimed for those abstract ingredients. The closest Nyman-specific boundaries already anchored in `SOURCES.md` are Burnol's Blaschke projection theorem, the finite Blaschke/arithmetic Gram split of Ziad, and Yang's Friedrichs-angle formulation. A targeted audit across Nyman--Beurling multiple-zero/multiplicity language, finite Blaschke model spaces, repeated-zero kernel derivatives, and confluent Cauchy geometry did not locate the source-specific statement `(7)` or the finite-rank target/leverage consequence `(11)`. No external theorem beyond the already persisted line dependencies is load-bearing here, so `SOURCES.md` needs no new entry.

Several boundaries are essential. First, `d` is fixed. The lower eigenvalue in `(17)` depends on the fixed Laguerre moment matrix and can deteriorate with `d`; no growing-rank conclusion follows. This is precisely where a genuinely new multi-zero invariant could still appear.

Second, the boundary theorem uses `a_j->0`, natural ordinate start `m_j~G_j`, and fixed positive radial depth `2a_j log q_j->L`. It does not assert a uniform statement when `L->0`, when the band begins below the ordinate scale by positive radial delay, or for arbitrary multi-center zero configurations.

Third, `(7)` concerns the state subspace inside the complete visible integer-cell space. It does not prove that the canonical Nyman residual must carry a large fraction of state leverage. Equation `(11)` shows exactly why that missing bridge remains decisive: every fixed leverage fraction `theta<1` leaves the complementary target fraction `1-theta` available.

Finally, the repeated-zero interpretation requires actual zero multiplicity at least `d`; the analytic confluent packet exists independently, but an artificial derivative packet is not evidence that zeta has a repeated zero. The result removes fixed repeated-zero/Jordan backfill as an escape route **if that source configuration occurs**; it does not constrain zeta-zero multiplicity itself.

## 6. Consequence for the Nyman line

`NB-107` left two natural ways to evade rank-one target-poorness: restore early cells, or replace one state by a finite derivative/Jordan packet. The first was already excluded there; `(7)` excludes the second at every fixed multiplicity in the hardest boundary scaling covered by `NB-104`. The obstruction is subspace-level and therefore survives arbitrary changes of basis inside the confluent packet.

The live target-coercivity problem is consequently pushed to **growing effective rank or genuinely multi-center state geometry**, together with a theorem forcing the actual Nyman residual to occupy near-maximal state leverage. Fixed-dimensional confluence, repeated-zero derivatives, coordinate shear, determinant volume, and full fixed-scale backfill no longer provide that missing coercive bridge.