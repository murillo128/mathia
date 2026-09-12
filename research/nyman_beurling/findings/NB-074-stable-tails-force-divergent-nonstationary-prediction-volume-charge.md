# NB-074 — stable tails force divergent nonstationary prediction-volume charge

**Status:** `EXACT-DERIVED + FINITE-DETERMINANT-CERTIFICATE + NONSTATIONARY-PREDICTION-VOLUME + STABLE-TAIL-DIVERGENCE + CAUSAL-RENORMALIZATION + METHOD-ADVANCE`.

`NB-073` identifies the exact missing datum in the stationary scalar branch-filter controls: the stable tail is detected by the gap between the future-prediction energy forced by the Gram and the actual causal feedthrough. The live arithmetic problem is nonstationary, however, and the actual Nyman innovations have substantial visible forward memory inside every finite Paley--Wiener window. Comparing a global prediction error directly with `||C_j||` therefore mixes two effects: benign memory that is already visible before the cutoff, and genuinely unresolved continuation beyond the cutoff.

The present finding gives an exact renormalization that separates them. Retain the causal innovations `D_j`, visible Gram `A_R`, and finite-future Schur complement `S_(R,N)` from `NB-062/067`. For `N>=R>=2`, define

\[
\boxed{
\mathfrak J_{R,N}
:=
\log\det\!\left(
A_R^{-1/2}S_{R,N}A_R^{-1/2}
\right)
=
\log\frac{\det S_{R,N}}{\det A_R}.
}
\tag{1}
\]

Then

\[
\boxed{\mathfrak J_{R,N}\ge0,}
\tag{2}
\]

and the complete generalized-eigenvalue certificate of `NB-067` is scalarized by

\[
\boxed{
1+\Lambda_R^2
\le
\Xi_{R,N}
\le
\exp(\mathfrak J_{R,N}).
}
\tag{3}
\]

Consequently, if the stable tail is nonzero, then for **every** finite horizon schedule `N(R)>=R`,

\[
\boxed{
\mathfrak J_{R,N(R)}\longrightarrow\infty.
}
\tag{4}
\]

More quantitatively, every nonzero `t in T_infinity` forces

\[
\boxed{
\mathfrak J_{R,N}
\ge
\log\!\left(
1+\frac{\|J_Rt\|^2}{\|(I-J_R)t\|^2}
\right)
}
\tag{5}
\]

for every `N>=R`. Thus a persistent locally-natural/global-orthogonal mode must create an unbounded **prediction-volume charge** in every finite future certificate.

The converse useful for the line is immediate: if there are unbounded `R_k` and finite `N_k>=R_k` with

\[
\sup_k\mathfrak J_{R_k,N_k}<\infty,
\tag{6}
\]

then

\[
\boxed{\mathcal T_\infty=\{0\}.}
\tag{7}
\]

This is stronger as a hypothesis than the matrix bound in `NB-067`, but it replaces a growing-dimensional Loewner/eigenvalue problem by one positive scalar with an exact prediction factorization. In particular, even the one-step horizon `N=R` gives the entirely finite source-only test

\[
\boxed{
\exp(\mathfrak J_{R,R})
=
\frac{\det H^{(R)}}{\|D_R\|^2\det A_R},
}
\tag{8}
\]

where `H^(R)` is the global Gram matrix of `D_1,...,D_R`. Boundedness of (8) on any unbounded sequence already rules out the entire stable tail.

## 1. The Schur complement dominates the visible Gram

Use the notation of `NB-067`. For `c in C^(R-1)`, put

\[
s_c=\sum_{j<R}c_jD_j,
\qquad
g_c=J_Rs_c,
\tag{9}
\]

so that

\[
\|g_c\|^2=c^*A_Rc.
\tag{10}
\]

For the finite future space

\[
\mathcal F_{R,N}=\operatorname{span}\{D_R,\ldots,D_N\},
\tag{11}
\]

`NB-067` proves

\[
c^*S_{R,N}c
=
\inf_{v\in\mathcal F_{R,N}}\|s_c+v\|^2.
\tag{12}
\]

Every `v in F_(R,N)` starts at time at least `log R`, hence `J_Rv=0`. The Paley--Wiener split is orthogonal, so

\[
\|s_c+v\|^2
=
\|g_c\|^2
+
\|(I-J_R)(s_c+v)\|^2.
\tag{13}
\]

Taking the infimum gives the exact positive decomposition

\[
\boxed{
S_{R,N}=A_R+E_{R,N},
\qquad E_{R,N}\succeq0.
}
\tag{14}
\]

Therefore

\[
M_{R,N}:=A_R^{-1/2}S_{R,N}A_R^{-1/2}\succeq I.
\tag{15}
\]

If its eigenvalues are

\[
1\le\lambda_1\le\cdots\le\lambda_{R-1},
\tag{16}
\]

then

\[
\Xi_{R,N}=\lambda_{R-1},
\qquad
\exp(\mathfrak J_{R,N})=\prod_{i=1}^{R-1}\lambda_i.
\tag{17}
\]

Since every factor except the maximum is at least one,

\[
\Xi_{R,N}\le\exp(\mathfrak J_{R,N}).
\tag{18}
\]

`NB-067` gives

\[
\Xi_{R,N}\downarrow1+\Lambda_R^2
\quad(N\to\infty),
\tag{19}
\]

which proves (3).

If `0!=t in T_infinity`, `NB-066` gives

\[
\Lambda_R
\ge
\frac{\|J_Rt\|}{\|(I-J_R)t\|}.
\tag{20}
\]

Combining (3) and (20) proves (5). Since `J_Rt -> t != 0` and `(I-J_R)t -> 0`, the right side tends to infinity, proving (4). No target vector and no RH-equivalent estimate enter this implication.

For `N=R`, the future block in the Gram matrix is the scalar `||D_R||^2`. The block determinant identity gives

\[
\det H^{(R)}
=
\|D_R\|^2\det S_{R,R},
\tag{21}
\]

which proves (8).

## 2. The charge is a sum of nonnegative prediction gaps, not a determinant cancellation

The determinant in (1) has an exact coordinate interpretation. For `1<=j<R<=N`, define the finite global future-prediction error

\[
\Pi_{j,N}^2
:=
\inf_{a_{j+1},\ldots,a_N}
\left\|
D_j+\sum_{k=j+1}^Na_kD_k
\right\|^2,
\tag{22}
\]

and the prediction error visible inside the current window

\[
\widehat\Pi_{j,R}^2
:=
\inf_{a_{j+1},\ldots,a_{R-1}}
\left\|
J_RD_j+\sum_{k=j+1}^{R-1}a_kJ_RD_k
\right\|^2.
\tag{23}
\]

Finite independence from `NB-062` makes all these quantities positive. Reverse Gram--Schmidt, equivalently repeated scalar Schur complementation, gives

\[
\det H^{(N)}
=
\prod_{j=1}^N\Pi_{j,N}^2,
\tag{24}
\]

while the future principal block satisfies

\[
\det H_{FF}^{(N)}
=
\prod_{j=R}^N\Pi_{j,N}^2.
\tag{25}
\]

Because

\[
\det H^{(N)}
=
\det H_{FF}^{(N)}\det S_{R,N},
\tag{26}
\]

we obtain

\[
\boxed{
\det S_{R,N}
=
\prod_{j=1}^{R-1}\Pi_{j,N}^2.
}
\tag{27}
\]

Applying the same reverse Gram--Schmidt factorization to the visible vectors `J_RD_1,...,J_RD_(R-1)` gives

\[
\boxed{
\det A_R
=
\prod_{j=1}^{R-1}\widehat\Pi_{j,R}^2.
}
\tag{28}
\]

For every choice of global future coefficients in (22), truncation to the first `R` window produces an admissible visible residual in (23), while orthogonal projection cannot increase norm. Hence

\[
\boxed{
\Pi_{j,N}\ge\widehat\Pi_{j,R}.
}
\tag{29}
\]

Combining (1), (27), and (28) yields the exact additive form

\[
\boxed{
\mathfrak J_{R,N}
=
\sum_{j=1}^{R-1}
\log\frac{\Pi_{j,N}^2}{\widehat\Pi_{j,R}^2},
\qquad
\log\frac{\Pi_{j,N}^2}{\widehat\Pi_{j,R}^2}\ge0.
}
\tag{30}
\]

Thus the determinant charge cannot become large through cancellation between coordinates. A persistent tail forces a growing aggregate of individually nonnegative discrepancies between what the finite window predicts and what the same innovations cost when their unseen future is included.

This is the useful nonstationary analogue of the scalar prediction gap in `NB-073`. The new feature is the denominator `widehat Pi_(j,R)`: the actual source already has forward memory visible inside the current window, and that memory must be removed before calling the remainder an inner/stable-tail signal.

## 3. Causal feedthrough splits the charge into visible and unseen parts

`NB-062` gives the nonzero newest-cell component

\[
C_j=(J_{j+1}-J_j)D_j.
\tag{31}
\]

Every innovation `D_k` with `k>j` starts at or after `log(j+1)`. Therefore no future correction can change the `I_j=[log j,log(j+1)]` component of `D_j`. Both prediction errors satisfy

\[
\boxed{
\Pi_{j,N}^2
\ge
\widehat\Pi_{j,R}^2
\ge
\|C_j\|^2.
}
\tag{32}
\]

Define the global finite-horizon feedthrough charge

\[
\mathfrak F_{R,N}
:=
\sum_{j<R}
\log\frac{\Pi_{j,N}^2}{\|C_j\|^2},
\tag{33}
\]

and the already-visible memory charge

\[
\mathfrak V_R
:=
\sum_{j<R}
\log\frac{\widehat\Pi_{j,R}^2}{\|C_j\|^2}.
\tag{34}
\]

Then

\[
\boxed{
\mathfrak J_{R,N}
=
\mathfrak F_{R,N}-\mathfrak V_R.
}
\tag{35}
\]

Both terms on the right are nonnegative, but only their difference isolates continuation beyond the current window. This corrects the most tempting direct transfer of `NB-073`: in the nonstationary Nyman system, a large ratio `Pi/||C||` by itself is not evidence of a stable-tail mechanism, because the same excess may already be completely accounted for by visible finite-window memory.

Equation (35) identifies the quantity that an arithmetic proof should control. One may estimate global prediction relative to the feedthrough, but the benign visible contribution must be subtracted rather than silently attributed to an inner defect.

## 4. Stationary Wold rays recover exactly the `NB-073` inner charge

The renormalization has the required stationary calibration. In the matched-control class of `NB-072/073`, fix a unit wandering vector

\[
w\in\ker V_m^*
\]

and consider one Wold ray

\[
x_r=\psi(V_m)V_m^rw,
\qquad r\ge0,
\tag{36}
\]

with

\[
\psi=\theta g,
\qquad \psi(0)\ne0.
\tag{37}
\]

Under the Wold unitary this is the scalar Hardy family `psi(z)z^r`. Truncation to the first `L` Wold coordinates gives a square triangular Toeplitz synthesis matrix with constant diagonal `psi(0)`. Hence the visible Gram determinant is exactly

\[
\det A_L^{\rm ray}=|\psi(0)|^{2L}.
\tag{38}
\]

`NB-073` proves that the full future-prediction error on every shifted ray is

\[
\Pi(\psi)^2=|g(0)|^2.
\tag{39}
\]

Reverse prediction therefore gives the infinite-future Schur determinant

\[
\det S_L^{\rm ray}=|g(0)|^{2L}.
\tag{40}
\]

Thus the limiting ray charge is

\[
\boxed{
\mathfrak J_L^{\rm ray}
=L\log\frac{|g(0)|^2}{|\psi(0)|^2}
=-2L\log|\theta(0)|
=L\,\mathfrak J(\psi),
}
\tag{41}
\]

where `mathfrak J(psi)` is exactly the stationary inner charge of `NB-073`.

This calibration separates the same boundary cases correctly. If `psi` is outer, including the noninvertible boundary example `psi=1-z`, the charge density in (41) is zero even though Gram conditioning may degenerate. A nonconstant Blaschke or singular inner factor gives strictly positive charge density and therefore linear growth. The determinant construction is consequently not a disguised condition-number test.

Equation (41) is a calibration on a single Wold ray; it does **not** identify the integer-ordered nonstationary Nyman innovations with that stationary ray. The arithmetic source still requires its own estimate of (1).

## 5. Flat control and failure modes

For the unit-outer control `O=1`, `NB-062/067` give cell-local orthogonal innovations. There is no forward memory, so

\[
\Pi_{j,N}
=
\widehat\Pi_{j,R}
=
\|C_j\|
\tag{42}
\]

and therefore

\[
\boxed{\mathfrak J_{R,N}=0}
\tag{43}
\]

for every `R,N`. This is the required zero-charge calibration.

The converse to (4) is false in a general nonstationary causal family. A zero stable tail may coexist with

\[
\mathfrak J_{R,N(R)}\to\infty
\tag{44}
\]

because a growing number of moderate generalized eigenvalues can make the determinant diverge even while their maximum stays bounded. Thus bounded determinant charge is a sufficient no-tail certificate, while divergent charge is only a necessary condition for persistence. The matrix criterion of `NB-067` remains strictly sharper in that sense.

For the same reason, replacing `det A_R` in (1) by the raw product `prod_(j<R)||C_j||^2` is not an admissible stable-tail detector. That replacement adds the visible charge `V_R` from (34), which can grow for ordinary causal memory unrelated to any global defect. The exact finite-window Gram normalization is load-bearing.

A second limitation is numerical. Determinants of large Gram matrices can underflow or hide conditioning catastrophes. Any computational use should work with certified log-determinants, Cholesky/LDL factorizations, or interval bounds. Floating-point positivity of (1) is not evidence. No computation is required for the theorem itself.

Finally, (7) eliminates the collective stable late quotient `T_infinity`; it does not by itself prove an Nyman approximation rate or RH. It supplies a source-only obstruction test upstream of those target questions.

## 6. Prior-art and novelty boundary

The block determinant identity, Schur-complement determinant formula, reverse Gram--Schmidt product, and inequality `lambda_max <= product lambda_i` for eigenvalues at least one are standard finite-dimensional linear algebra. No novelty is claimed for those ingredients. The stationary calibration uses only the already-persisted Wold/inner--outer/prediction statements of `NB-072/073`.

A targeted literature audit checked current Nyman--Beurling Gram work. Werner Ehm's `arXiv:2405.06349` derives explicit Gram formulae, reciprocity relations, and quadratic-form decompositions. Hugh Carvill's `arXiv:2510.18132` develops Mellin-smoothed off-diagonal decay and block compressibility. The search did not locate the line-specific construction (1)--(5): normalizing the finite-future Schur determinant by the **visible causal Gram determinant**, factoring the result into nonnegative global-versus-visible prediction gaps, and using `NB-066/067` to force its divergence under a persistent stable tail. No priority claim is made.

No new specialized external estimate is load-bearing, so `SOURCES.md` remains unchanged.

## 7. Consequence for the live Nyman frontier

`NB-073` left the source-facing target as a nonstationary comparison between future-prediction energy and causal feedthrough. The present result shows that the first robust quantity is not a raw pointwise ratio `Pi_R^2/||C_R||^2`. Visible forward memory must first be removed. The exact finite object is the excess prediction volume

\[
\boxed{
\mathfrak J_{R,N}
=
\log\frac{\det S_{R,N}}{\det A_R}
=
\sum_{j<R}\log\frac{\Pi_{j,N}^2}{\widehat\Pi_{j,R}^2}.
}
\tag{45}
\]

This produces a concrete arithmetic theorem target. It is enough to find an unbounded sequence `R_k` and any finite horizons `N_k>=R_k` for which (45) stays bounded. The most local version requires only

\[
\boxed{
\frac{\det H^{(R)}}{\|D_R\|^2\det A_R}=O(1)
}
\tag{46}
\]

on an unbounded sequence. If the one-step horizon is too costly, increasing `N` can only decrease `S_(R,N)` and hence decrease the charge.

Conversely, a nonzero stable mode forces every such finite certificate to accumulate unbounded excess prediction volume, with the quantitative lower bound (5). The next arithmetic question is therefore sharply scalar: can the exact Mellin/Paley--Wiener Gram structure keep the **unseen** prediction volume bounded after the already-visible causal memory has been divided out? That is the determinant-level nonstationary analogue of excluding the inner charge in `NB-073`.
