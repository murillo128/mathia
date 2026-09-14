# NB-109 — near-logarithmic confluent rank remains target-poor after full backfill

**Status:** `DERIVED + GROWING-CONFLUENT-RANK + FULL-EARLY-CELL-BACKFILL + TARGET-AWARE-STATE-SUBSPACE + REPRESENTATION-INVARIANT + SOURCE-COMPATIBLE-WHEN-MULTIPLICITY-PRESENT + NEGATIVE/METHOD-BOUNDARY`.

`NB-108` proves that, after restoring every early logarithmic cell, any **fixed-dimensional** confluent/Jordan packet attached to one hypothetical off-critical zero remains asymptotically orthogonal to the Nyman target. Its explicit caveat is that the lower spectral bound used there deteriorates with the packet dimension, so the argument says nothing when the zero multiplicity or the retained Jordan rank grows with the ordinate.

The fixed-rank hypothesis can be removed over a nearly logarithmic window. More importantly, the proof can be made without treating the bad monomial Gram conditioning as geometric data: the relevant obstruction is an intrinsic polynomial **extrapolation cost from the resolved terminal band back to the target endpoint**.

Let

\[
\rho_j=\frac12+a_j+iG_j,
\qquad 0<a_j<\frac12,
\qquad G_j\to\infty,
\]

be hypothetical right-half zeros, put

\[
m_j=\lceil G_j\rceil,
\qquad
R_j=m_jq_j,
\qquad
L_j:=2a_j\log q_j\longrightarrow L\in(0,\infty),
\tag{1}
\]

and fix the left target cutoff `r>=1`. For every integer `d_j>=1`, let

\[
S_j^{(d_j)}
=
\operatorname{span}\{w_{0,j},\ldots,w_{d_j-1,j}\}
\tag{2}
\]

be the derivative-state space from `NB-108`, where

\[
\langle \phi_n,w_{k,j}\rangle
=
\sqrt{2a_j}\,m_j^{\lambda_j}
\int_n^{n+1}
\bigl(2a_j\log(t/m_j)\bigr)^k
 t^{-\lambda_j-3/2}\,dt,
\qquad
\lambda_j=a_j+iG_j.
\tag{3}
\]

Write

\[
e_j=e_{r,R_j}=\sum_{n=r}^{R_j-1}\phi_n,
\qquad
\delta_j^2
:=
\frac{\|P_{S_j^{(d_j)}}e_j\|_2^2}{\|e_j\|_2^2}.
\tag{4}
\]

Then, for every fixed `epsilon>0`,

\[
\boxed{
 d_j
 \le
 \left(\frac12-\varepsilon\right)
 \frac{\log G_j}{\log\log G_j}
 \quad\Longrightarrow\quad
 \delta_j\longrightarrow0.
}
\tag{5}
\]

Thus the target-poorness theorem of `NB-108` is not merely finite-rank: it survives every confluent packet whose rank grows up to a fixed positive fraction below

\[
\frac12\frac{\log G}{\log\log G}.
\]

There is also a sharper scale-sensitive form. Define the radial distance from the resolved band to the fixed target endpoint

\[
A_j:=2a_j\log\frac{m_j}{r}.
\tag{6}
\]

For the ranks in the proof below,

\[
\boxed{
\delta_j^2
\ll_{r,L}
G_j^{-1}
\bigl[C_L(1+A_j)\bigr]^{2d_j}.
}
\tag{7}
\]

Consequently

\[
d_j\log(2+A_j)=o(\log G_j)
\tag{8}
\]

is already sufficient. In the boundary subregime `A_j=O(1)`, for example, every `d_j=o(log G_j)` packet remains target-poor. Formula `(5)` is the rate-free consequence of `(7)`, since `A_j<=log G_j+O_r(1)` for `a_j<1/2`.

## 1. Replace the growing Gram matrix by one polynomial state

For a polynomial

\[
p(u)=\sum_{k=0}^{d-1}c_k u^k,
\tag{9}
\]

write

\[
w_j[p]:=\sum_{k=0}^{d-1}c_k w_{k,j}.
\tag{10}
\]

This is just a change of coordinates inside `S_j^{(d)}`. The exact cell formula from `NB-104` becomes

\[
\langle\phi_n,w_j[p]\rangle
=
\sqrt{2a}\,m^\lambda
\int_n^{n+1}
 p\!\left(2a\log(t/m)\right)
 t^{-\lambda-3/2}\,dt.
\tag{11}
\]

Choose once and for all a compact interval

\[
I=[\alpha,\beta]\Subset(0,L).
\tag{12}
\]

For large `j`, all cells with

\[
u_n:=2a\log(n/m)\in I
\]

lie inside the terminal band. On such a cell,

\[
\frac{G}{n}
\le
\frac{G}{m}\exp\!\left(-\frac{\alpha}{2a}\right)
\le e^{-\alpha}+o(1)<1,
\tag{13}
\]

because `2a<1`. Hence the Mellin phase rotates by strictly less than one radian across each logarithmic cell, uniformly in `a`. The exact average of the frozen polynomial factor therefore has modulus bounded below by a constant depending only on `I`.

The radial mesh is even finer:

\[
\Delta u_n
=2a\log(1+1/n)
\ll \frac1G.
\tag{14}
\]

For polynomials of degree `<d`, the elementary `L^2` Markov inequality on the fixed interval `I` gives

\[
\|p'\|_{L^2(I)}
\ll_I d^2\|p\|_{L^2(I)}.
\tag{15}
\]

Using `(14)` first to control the variation of `p` inside each cell and then to compare the cell sum with its radial integral gives, uniformly whenever `d^2/G=o(1)`,

\[
\boxed{
\|w_j[p]\|_2^2
\ge
c_I
\int_I |p(u)|^2e^{-u}\,du.
}
\tag{16}
\]

The point of `(16)` is that no smallest eigenvalue of the monomial moment matrix appears. It is a coercive estimate on the polynomial **function** represented by the packet, and therefore survives whitening or any other invertible basis change in `S_j^{(d)}`.

The ranks in `(5)` satisfy `d^2/G=o(1)` by a huge margin.

## 2. Full target access is an exact endpoint-jet functional

The complete backfilled target pairing also has a basis-free form. Put

\[
u(t)=2a\log(t/m),
\qquad
u(r)=-A,
\qquad
u(R)=L_j.
\]

Then

\[
\langle e_j,w_j[p]\rangle
=
\sqrt{2a}\,m^\lambda
\int_r^R p(u(t))t^{-\rho-1}\,dt.
\tag{17}
\]

Since

\[
\frac{d}{dt}t^{-\rho}=-\rho t^{-\rho-1},
\qquad
u'(t)=\frac{2a}{t},
\]

integration by parts terminates after `d` steps and gives the **exact** identity

\[
\boxed{
\int_r^R p(u(t))t^{-\rho-1}\,dt
=
\sum_{\ell=0}^{d-1}
\frac{(2a)^\ell}{\rho^{\ell+1}}
\left[
 p^{(\ell)}(-A)r^{-\rho}
 -p^{(\ell)}(L_j)R^{-\rho}
\right].
}
\tag{18}
\]

So the target does not inspect the whole polynomial packet independently. It sees two endpoint jets: a remote extrapolation to `-A` and a bounded extrapolation to `L_j`.

Map `I` affinely to `[-1,1]` and expand in normalized Legendre polynomials. Their elementary coefficient/derivative bounds imply, for `0<=ell<d`,

\[
|p^{(\ell)}(-A)|+|p^{(\ell)}(L_j)|
\le
(C_Ld^2)^\ell
\bigl[C_L(1+A)\bigr]^d
\left(\int_I|p(u)|^2e^{-u}\,du\right)^{1/2}.
\tag{19}
\]

This is the usual finite-degree extrapolation cost written in a form suited to `(18)`. Since `|rho|~G`, the derivative terms form a geometric tail with ratio

\[
O_L(d^2/G)=o(1).
\tag{20}
\]

The first endpoint therefore dominates at the level needed here. Using `m~G`, `a<1/2`, and fixed `r`,

\[
\frac{\sqrt{2a}\,m^a}{|\rho|}
\ll G^{-1/2}.
\tag{21}
\]

The `R` endpoint is smaller still. Combining `(18)`--`(21)` yields

\[
\boxed{
|\langle e_j,w_j[p]\rangle|
\ll_{r,L}
G^{-1/2}
\bigl[C_L(1+A)\bigr]^d
\left(\int_I|p(u)|^2e^{-u}\,du\right)^{1/2}.
}
\tag{22}
\]

Finally `(16)` and

\[
\|e_j\|_2^2
=
\sum_{n=r}^{R_j-1}\frac1{n(n+1)}
=
\frac1r-\frac1{R_j}
\longrightarrow\frac1r
\tag{23}
\]

give `(7)` after taking the supremum over nonzero `p` of degree `<d`.

If `(5)` holds, then

\[
\begin{aligned}
\log \delta_j^2
&\le
-\log G_j
+2d_j\log\!\bigl(C_L(1+A_j)\bigr)
+O_{r,L}(1)\\
&\le
-2\varepsilon\log G_j+o(\log G_j),
\end{aligned}
\tag{24}
\]

and hence `delta_j -> 0`.

## 3. Whitening does not remove the obstruction, and Chebyshev gives the matched control

A monomial basis for `(9)` becomes spectacularly ill-conditioned as `d` grows. Treating that smallest Gram eigenvalue as the obstruction would therefore violate the representation audit. Equations `(16)` and `(22)` avoid that mistake: they compare the **subspace norm** directly with the norm of the represented polynomial and then bound the target functional on that same polynomial space. Whitening the packet changes neither side of the principal-angle quantity `(4)`.

There is nevertheless a genuine growing-rank cost, and it is not a coordinate artifact. Let `T_{d-1}` be the Chebyshev polynomial transported from `[-1,1]` to the fixed interval `I`. At an exterior point `-A`,

\[
|T_{d-1}(\xi(-A))|
=
\frac12
\left(
|\xi(-A)+\sqrt{\xi(-A)^2-1}|^{d-1}
+
|\xi(-A)-\sqrt{\xi(-A)^2-1}|^{d-1}
\right),
\tag{25}
\]

so for `A>=1` its endpoint value grows like

\[
[c_I(1+A)]^{d-1}
\tag{26}
\]

while its `L^2(I)` norm is only polynomial in `d`. Thus the exponential dependence on `d log(1+A)` in `(19)`--`(22)` has the correct order for polynomial extrapolation.

This matched control matters conceptually. The `1/2` in the universal window `(5)` is **not claimed to be a sharp transition for the actual Nyman subspace**, because the full state norm also contains all unresolved and intermediate cells. But one cannot remove the growing-rank loss merely by choosing a better derivative basis, orthogonalizing the monomials, or whitening the Gram matrix. Any improvement beyond `(7)` has to use additional structure of the full state measure or of the zeta-zero source, not linear-algebra conditioning alone.

## 4. The finite-rank leverage frontier survives in this growing window

`NB-108` observed that its Pareto statement is dimension-free once the whole update range has small principal angle to the target. The same proof therefore applies verbatim here.

Let `B_j>=0` be any nonzero operator with

\[
\operatorname{Ran}(B_j)\subset S_j^{(d_j)},
\]

and define

\[
\eta_j(f)
=
\frac{\langle f,B_jf\rangle}
     {\|B_j\|\,\|f\|^2},
\qquad
\chi_j(f)
=
\frac{|\langle f,e_j\rangle|^2}
     {\|f\|^2\|e_j\|^2}.
\tag{27}
\]

For every fixed `theta in (0,1)`, under `(5)` or the sharper condition from `(7)`,

\[
\boxed{
\sup_{\eta_j(f)\ge\theta}\chi_j(f)
=
1-\theta+o(1).
}
\tag{28}
\]

So allowing a near-logarithmically growing Jordan packet does not open a hidden high-leverage/high-target channel.

## 5. Source meaning and remaining boundary

For each finite `j`, if `rho_j` is an actual zeta zero of multiplicity at least `d_j`, the repeated elementary Blaschke factor is source-compatible and its first `d_j` confluent leakage states span exactly `S_j^{(d_j)}` up to an invertible triangular change of basis. Therefore `(5)` applies directly to an actual repeated-zero packet whenever its **entire relevant multiplicity** lies in this window.

This does not dispose of arbitrary multiplicity growth. The classical unconditional bound for a zeta-zero multiplicity is only `O(log G)` (for example Hall, *J. London Math. Soc.* 59 (1999), 65--75, citing the Jensen/Titchmarsh argument), which is larger than the universal `log G/log log G` window proved here. Thus there remains a genuine source/method gap rather than a bookkeeping gap.

The prior-art audit also checked the classical/modern Nyman--Beurling Hardy-space and Blaschke formulations already anchored in `SOURCES.md`, Yang's 2026 subspace-angle formulation, and the literature on smallest eigenvalues of growing Hankel moment matrices (for example Zhu--Chen--Emmart--Weems, *Applied Mathematics and Computation* 334 (2018), 375--387). The latter confirms that monomial moment matrices have a real growing-dimension conditioning problem, but that problem is deliberately not used as an invariant here. I did not locate a source deriving the growing-rank repeated-zero target-angle estimate `(7)` or the near-logarithmic consequence `(5)` for finite Nyman sections.

No external theorem is load-bearing in the derivation above: the only polynomial inputs are the elementary fixed-interval Markov/Legendre/Chebyshev estimates used explicitly in the proof. `SOURCES.md` therefore does not need a new durable dependency.

## Consequence for the research frontier

`NB-108` left two interpretations open: perhaps fixed-rank target-poorness was merely an artifact of keeping the Jordan packet finite, or perhaps repeated-zero state geometry remains irrelevant to target access for substantially larger packets. `NB-109` resolves that question over a nontrivial growing regime. The packet may contain almost `log G/log log G` confluent directions and still become orthogonal to the target after **all** early cells are restored.

The remaining frontier is now narrower. To rescue a one-zero repeated packet by multiplicity alone, one must enter a rank regime at least comparable with the intrinsic polynomial extrapolation scale from the resolved radial band back to the fixed target endpoint. Equivalently, the next useful attack is no longer another fixed-`d` Laguerre determinant or a better-conditioned derivative basis; it is either a source-specific multiplicity restriction, or a direct analysis of the full growing-rank polynomial state measure in the transition region where the early endpoint can begin to compete with terminal coercivity.
