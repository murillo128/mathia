# NB-076 — future cancellation is a cross-cut area of interval partial correlations

**Status:** `EXACT-DERIVED + INTERVAL-PARTIAL-CORRELATION-LATTICE + NONNEGATIVE-CROSS-CUT-AREA + CONTIGUOUS-GRAM-CROSS-RATIOS + FINITE-BAND-CERTIFICATE + STABLE-TAIL-OBSTRUCTION + SOURCE-LOCAL-SCALARIZATION + METHOD-ADVANCE`.

`NB-075` replaces the nonstationary prediction-volume determinant by the exact scalar cancellation budget

\[
\mathfrak J_{R,N}
=
\mathfrak L_R
-
\sum_{n=R}^{N}
\bigl[-\log(1-\beta_{R,n})\bigr],
\tag{1}
\]

where `beta_(R,n)` is the squared multiple correlation of the genuinely new part of `D_n` with the residualized whole prefix `D_1,...,D_(R-1)` after the already admitted future `D_R,...,D_(n-1)` has been removed. This is an exact scalarization, but a single `beta_(R,n)` still contains an `(R-1)`-dimensional regression.

The present finding resolves each such multiple-correlation charge again, now into a **nonnegative lattice of pairwise endpoint partial correlations conditioned only on the indices lying between them**.

For `1<=j<n`, let

\[
\mathcal M_{j,n}
:=
\operatorname{span}\{D_{j+1},\ldots,D_{n-1}\},
\tag{2}
\]

with the empty-span convention for `n=j+1`, and define the two endpoint residuals

\[
x_{j,n}:=(I-P_{\mathcal M_{j,n}})D_j,
\qquad
y_{j,n}:=(I-P_{\mathcal M_{j,n}})D_n.
\tag{3}
\]

Finite independence of the causal innovations from `NB-062` gives `x_(j,n)!=0`, `y_(j,n)!=0`. Put

\[
\rho_{j,n}
:=
\frac{\langle x_{j,n},y_{j,n}\rangle}
{\|x_{j,n}\|\,\|y_{j,n}\|},
\qquad
\kappa_{j,n}
:=
-\log\bigl(1-|\rho_{j,n}|^2\bigr).
\tag{4}
\]

Then

\[
\boxed{\kappa_{j,n}\ge0,}
\tag{5}
\]

and every future cancellation atom of `NB-075` satisfies the exact chain rule

\[
\boxed{
-\log(1-\beta_{R,n})
=
\sum_{j=1}^{R-1}\kappa_{j,n}
\qquad(n\ge R).
}
\tag{6}
\]

Consequently the entire finite future cancellation budget is the cross-cut area

\[
\boxed{
\sum_{n=R}^{N}-\log(1-\beta_{R,n})
=
\sum_{\substack{1\le j<R\\R\le n\le N}}
\kappa_{j,n}.
}
\tag{7}
\]

Thus

\[
\boxed{
\mathfrak J_{R,N}
=
\mathfrak L_R
-
\sum_{\substack{j<R\le n\\n\le N}}
\kappa_{j,n}.
}
\tag{8}
\]

The future of `NB-075` is therefore not merely a sequence of growing-dimensional multiple correlations. It is a nonnegative upper-triangular lattice: an interval `(j,n)` contributes exactly the amount by which the endpoint `D_n` improves prediction of `D_j` after every intervening innovation has already been conditioned out. Only intervals that straddle the cutoff `R` enter the cancellation of the raw continuation volume at that cutoff.

This gives a more local sufficient criterion. For an integer bandwidth `H>=1`, define

\[
\mathfrak A_R(H)
:=
\sum_{h=1}^{H}
\sum_{j=\max(1,R-h)}^{R-1}
\kappa_{j,j+h}.
\tag{9}
\]

Every interval counted in (9) has right endpoint at most `R+H-1`, so

\[
\mathfrak A_R(H)
\le
\sum_{n=R}^{R+H-1}-\log(1-\beta_{R,n}).
\tag{10}
\]

Hence if there are unbounded `R_k`, finite `H_k`, and `C<infinity` such that

\[
\boxed{
\mathfrak A_{R_k}(H_k)
\ge
\mathfrak L_{R_k}-C,
}
\tag{11}
\]

then `NB-074/075` imply

\[
\boxed{\mathcal T_\infty=\{0\}.}
\tag{12}
\]

Since `-log(1-u)>=u`, the stronger but simpler condition

\[
\boxed{
\sum_{h=1}^{H_k}
\sum_{j=\max(1,R_k-h)}^{R_k-1}
|\rho_{j,j+h}|^2
\ge
\mathfrak L_{R_k}-C
}
\tag{13}
\]

also suffices. The new target is consequently a **band of contiguous finite Gram blocks near the cutoff**, rather than the inverse of one growing residualized-prefix Gram matrix.

## 1. Endpoint partial correlation is exactly one prediction-error decrement

Retain the finite future-prediction error of `NB-074`, now with the convenient convention

\[
\Pi_{j,n}^2
:=
\operatorname{dist}\!\left(
D_j,
\operatorname{span}\{D_{j+1},\ldots,D_n\}
\right)^2,
\qquad n\ge j,
\tag{14}
\]

so `Pi_(j,j)^2=||D_j||^2`.

For `j<n`, first project `D_j` and `D_n` orthogonally off the middle space `M_(j,n)`. Before admitting `D_n`, the residual prediction error of `D_j` is

\[
\Pi_{j,n-1}^2=\|x_{j,n}\|^2.
\tag{15}
\]

Admitting `D_n` adds only the residual direction `y_(j,n)`. The one-dimensional projection formula gives

\[
\begin{aligned}
\Pi_{j,n}^2
&=
\|x_{j,n}\|^2
-
\frac{|\langle x_{j,n},y_{j,n}\rangle|^2}
{\|y_{j,n}\|^2}\\
&=
\Pi_{j,n-1}^2
\bigl(1-|\rho_{j,n}|^2\bigr).
\end{aligned}
\tag{16}
\]

Finite independence implies strict positivity of the left side, hence `|rho_(j,n)|<1`. Therefore

\[
\boxed{
\kappa_{j,n}
=
\log\frac{\Pi_{j,n-1}^2}{\Pi_{j,n}^2}.
}
\tag{17}
\]

This identity is load-bearing. `rho_(j,n)` is **not** the raw correlation of `D_j` with `D_n`; it is the correlation of the two endpoint residuals after the entire intervening interval has been removed. It therefore counts only the genuinely new predictive link supplied by the right endpoint.

## 2. Each lattice atom is a contiguous-Gram determinant cross-ratio

Let

\[
G_{a:b}
:=
\operatorname{Gram}(D_a,\ldots,D_b),
\qquad
\Delta_{a,b}:=\det G_{a:b},
\tag{18}
\]

with `Delta_(b+1,b)=1` for an empty block. Finite independence makes every nonempty determinant positive. Standard Gram/Schur complementation gives

\[
\boxed{
\Pi_{j,n}^2
=
\frac{\Delta_{j,n}}{\Delta_{j+1,n}}.
}
\tag{19}
\]

Combining (17) and (19),

\[
\boxed{
\kappa_{j,n}
=
\log\frac{
\Delta_{j,n-1}\,\Delta_{j+1,n}
}{
\Delta_{j,n}\,\Delta_{j+1,n-1}
}.
}
\tag{20}
\]

Equivalently,

\[
1-|\rho_{j,n}|^2
=
\frac{
\Delta_{j,n}\,\Delta_{j+1,n-1}
}{
\Delta_{j,n-1}\,\Delta_{j+1,n}
}.
\tag{21}
\]

The nonnegativity in (5) is the endpoint form of the classical Hadamard--Fischer/log-determinant submodularity inequality. Formula (20) is useful here because every atom depends only on one **contiguous** block `D_j,...,D_n`. The arithmetic source is therefore asked for interval-conditioned local data, not for arbitrary subsets of the full prefix.

The same formula gives an exact discrete-curvature interpretation. If

\[
\Phi(a,b):=\log\Delta_{a,b},
\tag{22}
\]

then `kappa_(j,n)` is the nonnegative mixed second difference

\[
\kappa_{j,n}
=
\Phi(j,n-1)+\Phi(j+1,n)
-
\Phi(j,n)-\Phi(j+1,n-1).
\tag{23}
\]

So the cancellation budget is literally the accumulated nonnegative log-Gram curvature of all intervals crossing the causal cut.

## 3. The multiple-correlation variables of `NB-075` factor exactly over the lattice

`NB-074` proves the reverse-prediction determinant factorization

\[
\det S_{R,n}
=
\prod_{j=1}^{R-1}\Pi_{j,n}^2.
\tag{24}
\]

`NB-075` proves the rank-one future update

\[
\det S_{R,n}
=
\det S_{R,n-1}(1-\beta_{R,n}).
\tag{25}
\]

Dividing (24) at horizons `n-1` and `n`, then using (17), yields

\[
\begin{aligned}
-\log(1-\beta_{R,n})
&=
\log\frac{\det S_{R,n-1}}{\det S_{R,n}}\\
&=
\sum_{j=1}^{R-1}
\log\frac{\Pi_{j,n-1}^2}{\Pi_{j,n}^2}\\
&=
\sum_{j=1}^{R-1}\kappa_{j,n},
\end{aligned}
\tag{26}
\]

which proves (6). In particular, if

\[
c_{R,n}:=-\log(1-\beta_{R,n}),
\tag{27}
\]

then

\[
\boxed{
c_{R+1,n}-c_{R,n}=\kappa_{R,n}\ge0.
}
\tag{28}
\]

Thus the cancellation supplied by a fixed future innovation `D_n` is monotone as the causal cut moves rightward, and its exact increment is the interval-conditioned link from the newly admitted prefix endpoint `D_R` to `D_n`.

Summing (26) over `R<=n<=N` proves (7). No approximation, stationarity assumption, asymptotic interchange, or target vector is used.

There is also a dual telescoping by left endpoint. For every `j<R`,

\[
\sum_{n=R}^{N}\kappa_{j,n}
=
\log\frac{\Pi_{j,R-1}^2}{\Pi_{j,N}^2}.
\tag{29}
\]

Summing (29) over `j<R` recovers exactly

\[
\sum_{\substack{j<R\le n\\n\le N}}\kappa_{j,n}
=
\log\frac{\det H_{<R}}{\det S_{R,N}},
\tag{30}
\]

which is the total raw-volume cancellation in `NB-075`. The lattice representation therefore introduces no extra budget and double-counts nothing.

## 4. Infinite future and the stable-tail obstruction

All `kappa_(j,n)` are nonnegative. For fixed `R`, `NB-075` gives

\[
0\le
\sum_{n=R}^{\infty}c_{R,n}
\le
\mathfrak L_R<\infty.
\tag{31}
\]

Tonelli/monotone convergence applied to (26) therefore gives the exact infinite-area identity

\[
\boxed{
\sum_{n=R}^{\infty}c_{R,n}
=
\sum_{\substack{j<R\le n<\infty}}\kappa_{j,n}.
}
\tag{32}
\]

Combining this with `NB-075` yields

\[
\boxed{
\mathfrak J_{R,\infty}
=
\mathfrak L_R
-
\sum_{\substack{j<R\le n<\infty}}\kappa_{j,n}
\ge0.
}
\tag{33}
\]

If `0!=t in T_infinity`, then `NB-074/075` force

\[
\boxed{
\mathfrak L_R
-
\sum_{\substack{j<R\le n<\infty}}\kappa_{j,n}
\ge
\log\!\left(
1+\frac{\|J_Rt\|^2}{\|(I-J_R)t\|^2}
\right)
\longrightarrow\infty.
}
\tag{34}
\]

A stable tail therefore requires not merely large raw continuation volume and not merely weak aggregate future prediction. It requires a **divergent deficit of cross-cut interval-conditioned correlation area** after every future interval has been allowed to contribute exactly once.

Conversely, (11) is now a finite-band source criterion. It is sufficient to recover `L_R` to `O(1)` using only partial correlations whose conditioning intervals have length at most `H_R-1`. This can be strictly easier to attack than the whole-prefix variable `beta_(R,n)` when the arithmetic innovations admit local or mesoscopic contiguous-block estimates.

## 5. Stress tests and falsification boundaries

The flat `O=1` control from `NB-056/062` has mutually orthogonal cell innovations. Hence

\[
\rho_{j,n}=0,
\qquad
\kappa_{j,n}=0
\tag{35}
\]

for every `j<n`. It also has `L_R=0`, so (8) gives `J_(R,N)=0` identically, as required.

The two-coordinate control from `NB-075` gives the opposite calibration. Take orthonormal `e_0,e_1` and

\[
D_1=e_0+Me_1,
\qquad
D_2=e_1.
\tag{36}
\]

Then

\[
|\rho_{1,2}|^2=\frac{M^2}{1+M^2},
\qquad
\kappa_{1,2}=\log(1+M^2).
\tag{37}
\]

At the cut `R=2`, this single lattice atom equals the full raw charge `L_2`, so the future cancels everything and `J_(2,2)=0`. This reproduces the exact cancellation mechanism that motivated `NB-075`.

A third control shows why raw off-diagonal Gram decay cannot replace (4). In a three-dimensional Hilbert space let

\[
D_1=e_1,
\qquad
D_2=e_1+e_2+\varepsilon e_3,
\qquad
D_3=e_2,
\qquad \varepsilon\ne0.
\tag{38}
\]

The endpoints are raw-orthogonal,

\[
\langle D_1,D_3\rangle=0,
\tag{39}
\]

but after conditioning on the middle vector,

\[
\rho_{1,3}
=-\frac1{1+|\varepsilon|^2},
\tag{40}
\]

so `|rho_(1,3)|` can be arbitrarily close to one. Therefore a bound on raw pairwise Gram entries, even a very small one at separated indices, does **not** by itself bound the lattice atoms after intervening directions are eliminated. A useful Nyman estimate must control the relevant contiguous Schur complements or partial correlations, not merely the unconditioned Gram kernel.

This is also why (6) is not a disguised sum of ordinary correlations. The conditioning interval is load-bearing: it prevents the same predictive direction from being counted repeatedly and is exactly what makes the total logarithmic charge agree with the Schur determinant.

Several further boundaries are essential. The lattice depends on the natural integer ordering of the causal innovations; arbitrary permutation changes the partial correlations. That is intended, because the Nyman flag itself is ordered by the logarithmic support thresholds. Pairwise notation does not make the atoms statistically or algebraically independent; each `rho_(j,n)` already encodes all intermediate directions. Finally, (11)--(13) are sufficient criteria, not estimates proved for the arithmetic source. This finding does not bound any `rho_(j,n)`, does not show that a bounded or polylogarithmic bandwidth suffices, and does not improve the Nyman distance by itself.

## 6. Prior-art audit and source boundary

The finite-dimensional identities behind (16), (19)--(21), and (26) are classical. Partial correlations are standard residual correlations; determinant cross-ratios of positive Gram/covariance matrices are instances of Hadamard--Fischer/log-determinant submodularity. For a formal centered Gaussian vector with covariance equal to a normalized Gram matrix, `kappa_(j,n)/2` is exactly the conditional mutual information between the two endpoints given the intervening coordinates. No novelty is claimed for any of this general linear-algebra/statistical structure.

The targeted Nyman--Beurling audit checked Werner Ehm's `arXiv:2405.06349`, which derives explicit Nyman Gram formulae and quadratic-form decompositions, and Hugh Carvill's `arXiv:2510.18132`, which proves Mellin-smoothed off-diagonal Gram decay and block compressibility. Searches combining Nyman--Beurling/Báez--Duarte with partial correlation, partial autocorrelation, Schur prediction, and determinant cross-ratios did not locate the specific causal use above: the `NB-075` future cancellation budget factored into the nonnegative interval lattice (6)--(8), together with the stable-tail cross-cut criterion (34) and finite-band sufficient criterion (11). Search absence is not a priority claim.

No specialized external theorem is load-bearing: the proof uses the already-persisted `NB-062/074/075` finite independence and determinant/prediction identities plus elementary Hilbert-space projection and finite determinant algebra. `SOURCES.md` therefore remains unchanged.

## 7. Consequence for the live Nyman frontier

`NB-075` left one difficult scalar per future innovation, but that scalar was still a multiple correlation against the whole residualized prefix. The present factorization identifies the exact smaller units:

\[
\boxed{
\text{future cancellation across }R
=
\sum_{j<R\le n}
\text{interval-conditioned endpoint charge }\kappa_{j,n}.
}
\tag{41}
\]

This makes the source-facing question spatial in the integer index. The next useful theorem does not need to invert the complete prefix Gram matrix. It can instead estimate contiguous blocks `D_j,...,D_n`, or directly the endpoint partial correlations, and ask how much nonnegative curvature crosses the cutoff.

The finite-band criterion (11) gives a concrete mesoscopic target. If an arithmetic argument can find bandwidths `H_R` for which the short/intermediate intervals crossing `R` already carry `L_R-O(1)` total charge, then the stable tail is impossible. Conversely, if those bands carry too little charge, the lattice identifies exactly where a hypothetical obstruction must hide: in increasingly long conditioned intervals crossing the cutoff.

That distinction is compatible with `NB-070/071`. Those findings show that long-range nonlocal structure can sustain stable-tail controls despite good global conditioning and exact branching. `NB-076` now states the corresponding exact arithmetic diagnostic: what matters is not raw long-range Gram mass but the **interval-conditioned cross-cut curvature after all intermediate innovations have been removed**.