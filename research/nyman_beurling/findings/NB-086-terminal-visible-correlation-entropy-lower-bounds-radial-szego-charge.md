# NB-086 — terminal visible correlation entropy lower-bounds radial Szegő charge

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + TERMINAL-VISIBLE-GRAM + HADAMARD-DEFICIT + RADIAL-FLOOR-OBSTRUCTION + METHOD-ADVANCE`.

`NB-085` reduces every fixed-integer-dilation radial strategy to the static floor charge

\[
\mathfrak S_{R,q}
=
\sum_{j=1}^{R-1}
\log\frac{G_{j,q}}{\widehat\Pi_{j,R}^2},
\qquad q\ge2,
\tag{1}
\]

where `G_(j,q)` is the infinite-depth Szegő prediction floor along the single descendant ray `j,qj,q^2j,...`, while `widehat Pi_(j,R)` is the prediction error of the same innovation using **all** later innovations visible before `log R`. The unresolved question was whether the aggregate mismatch in (1) can stay bounded without estimating every aliased spectral density separately.

There is an exact finite-window obstruction. Put

\[
m=m(R,q):=\left\lceil\frac Rq\right\rceil,
\qquad
I_{R,q}:=\{m,m+1,\ldots,R-1\}.
\tag{2}
\]

For `j in I_(R,q)`, the first radial descendant `qj` is already at or beyond the current cutoff `R`. Hence the complete radial future is invisible in the current window, while the full causal future used by `widehat Pi_(j,R)` still contains every intermediate innovation `D_(j+1),...,D_(R-1)`. This gives

\[
\boxed{
G_{j,q}\ge \|J_RD_j\|^2
\qquad (j\in I_{R,q}).
}
\tag{3}
\]

Let

\[
K_{R,q}
:=
\bigl(\langle J_RD_i,J_RD_j\rangle\bigr)_{i,j\in I_{R,q}},
\tag{4}
\]

let `Delta_(R,q)` be its diagonal matrix, and normalize to the terminal visible correlation matrix

\[
\mathcal R_{R,q}
:=
\Delta_{R,q}^{-1/2}
K_{R,q}
\Delta_{R,q}^{-1/2}.
\tag{5}
\]

`NB-062` makes the terminal visible innovations linearly independent, so `K_(R,q)>0` and `mathcal R_(R,q)>0`. Reverse Gram--Schmidt on this suffix gives

\[
\det K_{R,q}
=
\prod_{j=m}^{R-1}\widehat\Pi_{j,R}^2.
\tag{6}
\]

Combining (1), (3), and (6) yields the main bound

\[
\boxed{
\mathfrak S_{R,q}
\ge
-\log\det\mathcal R_{R,q}
\ge0.
}
\tag{7}
\]

Thus the single-`q` radial method has a **purely visible finite-window necessary condition**. If its floor charge is bounded along an unbounded sequence, then the normalized Gram determinant of the terminal fraction `j>=R/q` must stay uniformly away from zero. Equivalently, the many intermediate causal innovations skipped by the radial ray may not create an accumulating correlation-volume collapse before the ray even begins.

The condition is stronger than a determinant slogan. If `rho_(ij)^(R,q)` are the entries of `mathcal R_(R,q)` and the floor charge is bounded by `M` along a sequence, then

\[
\boxed{
\sum_{\substack{i,j\in I_{R,q}\\ i\ne j}}
|\rho_{ij}^{(R,q)}|^2
=O_M(1).
}
\tag{8}
\]

Consequently

\[
\boxed{
\sum_{m\le i<j<R}|\rho_{ij}^{(R,q)}|^2\longrightarrow\infty
\quad\Longrightarrow\quad
\mathfrak S_{R,q}\longrightarrow\infty.
}
\tag{9}
\]

So falsifying a fixed-`q` radial proof no longer requires estimating the Szegő floors themselves: it is enough to prove that the terminal visible normalized pair-correlation energy diverges. Conversely, any successful bounded-charge radial route must force the entire growing terminal block to have only bounded total squared correlation energy.

This does **not** decide the radial method for the actual source. Exact branching and the long-range mass theorem of `NB-070` do not by themselves imply (9), because they control unnormalized signed/absolute global correlations rather than the normalized visible suffix energy in (8). The result isolates the next source-specific test without silently converting branching into a determinant estimate.

## 1. The radial future is invisible on the terminal block

`NB-084` gives the exact branching identity

\[
U_{r\log q}D_j
=
q^{-r/2}
\sum_{k=q^rj}^{q^r(j+1)-1}D_k,
\qquad r\ge1,
\tag{10}
\]

and `NB-062` gives

\[
\operatorname{supp}D_k\subseteq[\log k,\infty).
\tag{11}
\]

If `j>=m=ceil(R/q)`, then `qj>=R`. Therefore every positive radial shift in the prediction problem

\[
D_j+\sum_{r=1}^La_rU_{r\log q}D_j
\tag{12}
\]

starts at or after `log R`. Applying `J_R` to (12) leaves exactly `J_RD_j`, independently of the coefficients. Orthogonality of the Paley--Wiener time split gives

\[
\mathcal E_{j,q,L}
\ge
\|J_RD_j\|^2
\qquad(L\ge1).
\tag{13}
\]

Taking `L->infinity` through `NB-085`,

\[
\mathcal E_{j,q,L}\downarrow G_{j,q},
\tag{14}
\]

proves (3). This is the precise loss incurred by the radial restriction: on the terminal `1-1/q` fraction of the visible innovations, the radial predictor cannot touch the current window at all.

## 2. Reverse prediction turns the terminal mismatch into a normalized Gram determinant

For `j<R`, `NB-074` defines

\[
\widehat\Pi_{j,R}^2
=
\inf_{a_{j+1},\ldots,a_{R-1}}
\left\|
J_RD_j+
\sum_{k=j+1}^{R-1}a_kJ_RD_k
\right\|^2.
\tag{15}
\]

Restricting to `j=m,...,R-1` changes nothing in these minimizations: every allowed predictor index is still inside the same suffix. Reverse Gram--Schmidt therefore gives (6).

Every summand in (1) is nonnegative by `NB-085`, so retaining only this suffix and using (3) yields

\[
\begin{aligned}
\mathfrak S_{R,q}
&\ge
\sum_{j=m}^{R-1}
\log\frac{G_{j,q}}{\widehat\Pi_{j,R}^2}\\
&\ge
\sum_{j=m}^{R-1}
\log\frac{\|J_RD_j\|^2}{\widehat\Pi_{j,R}^2}\\
&=
\log
\frac{
\prod_{j=m}^{R-1}\|J_RD_j\|^2
}{
\det K_{R,q}
}.
\end{aligned}
\tag{16}
\]

By definition of the normalized correlation matrix,

\[
\det K_{R,q}
=
\left(
\prod_{j=m}^{R-1}\|J_RD_j\|^2
\right)
\det\mathcal R_{R,q}.
\tag{17}
\]

Substitution proves (7). Hadamard's determinant inequality gives the final nonnegativity, although that nonnegativity is already visible from the reverse-prediction product in (16).

Equation (7) has a useful geometric interpretation. The floor charge must pay at least the logarithmic volume collapse of the normalized visible terminal innovations. This is not a new generic determinant identity; the source-specific content is that the terminal location `j>=R/q` makes that finite visible volume an unavoidable lower bound for the **infinite-depth aliased radial** prediction floor.

## 3. Bounded floor charge forces bounded total terminal correlation energy

Let

\[
n=|I_{R,q}|
\tag{18}
\]

and let `lambda_1,...,lambda_n>0` be the eigenvalues of `mathcal R_(R,q)`. Since its diagonal is one,

\[
\sum_{a=1}^n\lambda_a=n.
\tag{19}
\]

Hence its logarithmic determinant deficit can be written exactly as

\[
\begin{aligned}
-\log\det\mathcal R_{R,q}
&=
\sum_{a=1}^n[-\log\lambda_a]\\
&=
\sum_{a=1}^n
\bigl(\lambda_a-1-\log\lambda_a\bigr).
\end{aligned}
\tag{20}
\]

Put

\[
\phi(x)=x-1-\log x,
\qquad x>0.
\tag{21}
\]

Suppose `mathfrak S_(R,q)<=M`. By (7), every nonnegative summand `phi(lambda_a)` in (20) is at most `M`. The level set

\[
K_M:=\{x>0:\phi(x)\le M\}
\tag{22}
\]

is compact in `(0,infinity)`. Extending `phi(x)/(x-1)^2` continuously by the value `1/2` at `x=1`, define

\[
c_M
:=
\min_{x\in K_M}
\frac{\phi(x)}{(x-1)^2}
>0.
\tag{23}
\]

Then (20) gives

\[
M
\ge
-\log\det\mathcal R_{R,q}
\ge
c_M\sum_{a=1}^n(\lambda_a-1)^2
=
c_M\|\mathcal R_{R,q}-I\|_F^2.
\tag{24}
\]

Because the diagonal of `mathcal R_(R,q)-I` vanishes,

\[
\|\mathcal R_{R,q}-I\|_F^2
=
\sum_{i\ne j}|\rho_{ij}^{(R,q)}|^2.
\tag{25}
\]

Equations (24)--(25) prove (8). Taking the contrapositive proves (9).

The dimension-free conclusion is important. The terminal block has

\[
n=R-\left\lceil\frac Rq\right\rceil
=(1-q^{-1})R+O(1),
\tag{26}
\]

so bounded radial charge does not merely require small **average** correlation across a growing block. It forces the total squared off-diagonal correlation energy of that whole linear-size block to remain bounded.

## 4. Controls and failure modes

For the flat control `O=1`, `NB-062` gives disjoint-cell innovations. Thus the visible terminal Gram matrix is diagonal,

\[
\mathcal R_{R,q}^{(0)}=I,
\tag{27}
\]

and (7) reads `mathfrak S_(R,q)^(0)>=0` with equality in the actual flat floor calculation of `NB-085`. The obstruction therefore does not manufacture a correlation penalty in the memory-free matched control.

The converse of (7) is false. A well-conditioned or even asymptotically orthogonal terminal visible block does not imply bounded `mathfrak S_(R,q)`: earlier indices may contribute, and `G_(j,q)` can exceed the visible prediction error for reasons not encoded in the terminal determinant. The result supplies a necessary condition and a one-sided route-killing test, not a sufficient radial certificate.

Likewise, `NB-070` cannot simply be substituted into (9). Its persistent long-range absolute Gram mass is global and unnormalized; the terminal matrix here contains truncated vectors `J_RD_j` and normalizes each by its own visible norm. Spreading a fixed block correlation over many descendants can preserve an `l^1` mass while keeping `l^2` pair energy bounded. Any use of branching to force divergence in (9) therefore needs an additional source-specific anti-spreading or norm-comparability estimate.

No RH-equivalent target estimate enters (7)--(9). The obstruction concerns only the actual causal innovation geometry and the radial subfamily used to upper-bound the full finite-future prediction problem. Divergence of the terminal correlation energy would kill that fixed-`q` radial certificate, but would not imply a stable tail or failure of RH because the full nonradial future remains available.

## 5. Prior-art boundary and consequence for the frontier

The normalized Gram determinant in (7) is the classical Hadamard volume ratio, and determinant/prediction factorizations are standard linear algebra and prediction theory. No novelty is claimed for those ingredients. The prior-art audit also finds contemporary Nyman--Beurling Gram work, notably Carvill's 2025 Mellin-smoothed two-prime ladder analysis with polynomial off-diagonal decay and block compressibility, and Yang's 2026 Friedrichs-angle geometry. Those results concern different families or different subspace geometry and do not supply the terminal visible determinant bound (7) for the canonical causal innovations.

A targeted search did not locate the specific splice used here: the exact integer-descendant radial restriction of `NB-084`, its positive Szegő floor from `NB-085`, and the observation that the terminal linear-size suffix is completely untouched by every radial descendant, forcing its normalized visible Gram volume into the floor charge. No priority claim is made. No external theorem beyond standard determinant identities is load-bearing, so `SOURCES.md` requires no new anchor.

The live fixed-`q` question is now split into two finite-versus-infinite tests. Before estimating the detailed aliased floors, one can first ask whether

\[
\boxed{
\sup_R
\sum_{\lceil R/q\rceil\le i<j<R}
|\rho_{ij}^{(R,q)}|^2
<\infty
}
\tag{28}
\]

is even possible for the actual source. If the answer is no, then `mathfrak S_(R,q)` diverges and no amount of radial depth can rescue that `q`. If the answer is yes, the determinant obstruction has been passed and the remaining work genuinely lies in the aliased Szegő floors and the earlier-index mismatch, or in cross-ray prediction if the fixed-`q` charge still diverges.

This is a sharper first test than estimating (1) directly: it replaces an infinite-depth spectral quantity by a finite current-window correlation-energy condition on a block of asymptotically `(1-1/q)R` actual innovations.