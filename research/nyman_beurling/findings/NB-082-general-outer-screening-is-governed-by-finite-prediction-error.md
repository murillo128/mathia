# NB-082 — general outer screening is governed by finite prediction error

**Status:** `EXACT-DERIVED + MATCHED-BRANCH-CONTROL + FINITE-PREDICTION-ERROR + INNER-OUTER-CLASSIFICATION + VARIABLE-HORIZON-SCREENING + SHARP-METHOD-CALIBRATION`.

`NB-081` computes the variable-depth screening threshold for the special stationary controls

\[
D_j^{(\rho)}=(I-\rho V_m)e_j.
\]

For `0<rho<1` the benign boundary layer is removed after logarithmically many descendant generations, while the outer but noninvertible endpoint `rho=1` needs depth of order `R`. That calculation leaves open whether these are special features of the first-order filter `1-rho z` or manifestations of a general invariant.

They are manifestations of a general invariant. Let `m>=2`, let `V_m` be the block-branching isometry

\[
V_me_j=m^{-1/2}\sum_{k=mj}^{m(j+1)-1}e_k,
\]

and take any nonzero `psi in H^infty(D)` with

\[
c_0:=\psi(0)\ne0,
\qquad
D_j^{(\psi)}:=\psi(V_m)e_j.
\]

For `L>=1` define the scalar finite-prediction energy

\[
\varepsilon_L(\psi)
:=
\inf_{\substack{p\in\mathbb C[z]\\ \deg p\le L,\ p(0)=1}}
\|\psi p\|_{H^2}^2,
\qquad
 a_{\psi,L}:=
\frac{\varepsilon_L(\psi)}{|c_0|^2}-1\ge0.
\tag{1}
\]

For the depth-`L` horizon

\[
N_{R,L}=m^LR-1,
\tag{2}
\]

the complete prediction-volume charge of `NB-074` obeys

\[
\boxed{
K_{m,R,L}\log(1+a_{\psi,L})
\le
\mathfrak J_{R,N_{R,L}}
\le
(R-1)\log(1+a_{\psi,L}),
}
\tag{3}
\]

where

\[
K_{m,R,L}
:=
R-1-
\left\lfloor\frac{m^LR-1}{m^{L+1}}\right\rfloor,
\qquad
\frac{K_{m,R,L}}R\longrightarrow1-\frac1m
\tag{4}
\]

uniformly in `L`. Thus the positive-density finite-depth boundary layer isolated in `NB-080/081` is universal throughout the stationary scalar branch-filter class. The filter enters only through one scalar quantity: its degree-`L` prediction error.

If

\[
\psi=\theta g
\]

is the inner--outer factorization, then

\[
\boxed{
\varepsilon_L(\psi)\downarrow |g(0)|^2,
\qquad
 a_{\psi,L}\downarrow |\theta(0)|^{-2}-1.
}
\tag{5}
\]

Consequently

\[
\boxed{
\psi\text{ outer}
\iff
a_{\psi,L}\to0.
}
\tag{6}
\]

For an outer filter and any `L=L(R)->infinity`, (3) becomes

\[
\boxed{
\mathfrak J_{R,m^{L(R)}R-1}
\asymp_m
R\,a_{\psi,L(R)}.
}
\tag{7}
\]

Hence, within this whole matched-control class,

\[
\boxed{
\mathfrak J_{R,m^LR-1}=O(1)
\iff
R\,a_{\psi,L}=O(1),
}
\tag{8}
\]

and

\[
\boxed{
\mathfrak J_{R,m^LR-1}\to0
\iff
R\,a_{\psi,L}\to0
}
\tag{9}
\]

along schedules with `L->infinity`. Qualitative outerness therefore settles only whether arbitrarily deep screening eventually removes the boundary layer. The amount of future required is controlled exactly by the **finite cyclic prediction rate** `a_(psi,L)`. `NB-081` is the pair of explicit examples where this rate is geometric for `1-rho z`, `rho<1`, and harmonic for `1-z`.

This is a calibration theorem, not an arithmetic Nyman estimate. Its main consequence for the live route is methodological: replacing the first-order controls by an arbitrary outer stationary branch filter does not remove the variable-horizon issue. A source-facing theorem must identify and bound the analogue of `a_(psi,L)` for the actual nonstationary innovations, or use a certificate that does not pay this finite-prediction boundary layer.

## 1. The visible prediction error is always the feedthrough

Write

\[
\psi(z)=\sum_{r\ge0}c_rz^r.
\]

Since every support of `V_m^r e_j` with `r>=1` lies strictly after index `j`,

\[
D_j^{(\psi)}
=c_0e_j+\text{coordinates with index }>j.
\tag{10}
\]

Therefore, at every finite cutoff `R`, the synthesis matrix of

\[
J_RD_1^{(\psi)},\ldots,J_RD_{R-1}^{(\psi)}
\]

in the coordinate basis `e_1,...,e_(R-1)` is triangular with diagonal `c_0`. Back substitution through the suffix `j+1,...,R-1` cancels every visible coordinate after `e_j`, while no later innovation can change the coefficient `c_0` on `e_j`. Thus the visible reverse-prediction errors are exactly

\[
\boxed{
\widehat\Pi_{j,R}^2=|c_0|^2
\qquad(1\le j<R).
}
\tag{11}
\]

In particular

\[
\det A_R=|c_0|^{2(R-1)}.
\tag{12}
\]

This extends the unit-diagonal calculation in `NB-081`; no outerness or invertibility is needed.

## 2. Complete descendant generations reduce exactly to a scalar Hardy prediction problem

Fix `j`. The generation vectors

\[
f_r:=V_m^re_j,
\qquad r\ge0,
\tag{13}
\]

are orthonormal because their consecutive descendant blocks are disjoint. Hence

\[
p(V_m)e_j\longleftrightarrow p(z)
\tag{14}
\]

is an isometric identification of the radial cyclic subspace with scalar `H^2`. Since `psi(V_m)` commutes with `V_m`,

\[
V_m^rD_j^{(\psi)}
=\psi(V_m)V_m^re_j.
\tag{15}
\]

Exact branching also writes each vector in (15) as the normalized average of all depth-`r` descendant innovations, so for `r<=L` it is available whenever the horizon contains the complete first `L` descendant generations.

The nonradial descendant contrasts cannot improve prediction of `D_j^(psi)`. At generation `r`, decompose the descendant coordinate space into the average direction `f_r` and its orthogonal contrast space. If `x` is such a contrast, then every `V_m^nx` remains orthogonal to every radial generation `f_s`: different generations have disjoint support, while at the matching generation isometry gives orthogonality to `f_r`. Consequently `psi(V_m)x` is orthogonal to the whole radial cyclic subspace. Descendant subtrees not belonging to `j` are disjoint and are orthogonal for the same reason.

Therefore, when the finite future contains exactly the first `L` complete descendant generations of `j` and no part of generation `L+1`, the full future prediction problem is exactly

\[
\inf_{a_1,\ldots,a_L}
\left\|
D_j^{(\psi)}+
\sum_{r=1}^La_rV_m^rD_j^{(\psi)}
\right\|^2
=
\varepsilon_L(\psi).
\tag{16}
\]

For a general `j<R`, the same `L` radial predictors are admissible inside the horizon (2), so

\[
|c_0|^2
\le
\Pi_{j,N_{R,L}}^2
\le
\varepsilon_L(\psi).
\tag{17}
\]

Combining (11), (17), and the additive prediction formula of `NB-074` gives the upper bound in (3).

## 3. A positive-density boundary layer attains the scalar error exactly

Put `N=m^LR-1` and consider

\[
\frac{N}{m^{L+1}}<j<R.
\tag{18}
\]

Then `mj>=R`, so no proper descendant of `j` is visible before the cutoff. The first `L` descendant generations lie completely below `N`, while generation `L+1` begins strictly after `N`. Every future innovation that can interact with `D_j^(psi)` therefore belongs to one of those first `L` descendant generations; all other future subtrees are orthogonal.

Equation (16) is consequently exact for every index in (18):

\[
\boxed{
\Pi_{j,N}^2=arepsilon_L(\psi),
\qquad
\widehat\Pi_{j,R}^2=|c_0|^2.
}
\tag{19}
\]

There are exactly `K_(m,R,L)` such indices. Retaining only them in

\[
\mathfrak J_{R,N}
=
\sum_{j<R}
\log\frac{\Pi_{j,N}^2}{\widehat\Pi_{j,R}^2}
\tag{20}
\]

proves the lower bound in (3). This also shows why merely changing the stationary filter cannot remove the boundary layer geometrically: its density tends to `1-1/m` independently of the filter and independently of the chosen depth.

## 4. Inner--outer factorization gives the exact infinite-depth limit

Let

\[
\psi=\theta g
\tag{21}
\]

with `theta` inner and `g` outer. Polynomial multiples of `g` are dense in `H^2`, while multiplication by `theta` is isometric with closed range `theta H^2`. Hence the closure of polynomial multiples of `psi` is `theta H^2`.

The constraint `p(0)=1` means that every candidate `psi p` has value `c_0` at zero. Among functions of `theta H^2` having value `c_0` at zero, the minimum norm is obtained by minimizing the norm of `h` subject to

\[
\theta(0)h(0)=c_0.
\]

Evaluation at zero in `H^2` has norm one, so the minimum squared norm is

\[
\left|\frac{c_0}{\theta(0)}\right|^2
=|g(0)|^2.
\tag{22}
\]

Finite polynomials are dense in the cyclic subspace and evaluation at zero is continuous, so the constrained finite minima decrease to this value. This proves (5).

Since `c_0=theta(0)g(0)`, the limiting normalized excess is

\[
\boxed{
a_{\psi,\infty}
=\frac{|g(0)|^2}{|\psi(0)|^2}-1
=|\theta(0)|^{-2}-1.
}
\tag{23}
\]

It vanishes exactly when `theta` is constant, i.e. exactly when `psi` is outer. If `psi` has a nonconstant inner factor, (3) therefore stays linear in `R` even when `L->infinity`, matching the nonzero stable-tail classification of `NB-072/073`.

For finite `L` the same scalar is computable directly from a Toeplitz Gram matrix. Let

\[
T_L(\psi)
:=
\bigl(\langle z^r\psi,z^s\psi\rangle\bigr)_{0\le r,s\le L}.
\tag{24}
\]

Then quadratic minimization with the first coefficient fixed to one gives

\[
\boxed{
\varepsilon_L(\psi)
=\frac1{(T_L(\psi)^{-1})_{00}}.
}
\tag{25}
\]

Thus the depth threshold is not an informal conditioning parameter. It is an exact finite prediction/Toeplitz quantity.

## 5. Calibrations and boundary conditions

The flat filter `psi=1` has `a_(psi,L)=0` for every `L`, so (3) gives `mathfrak J=0`, as required.

For `psi(z)=1-rho z`, `0<rho<1`, the radial calculation of `NB-080/081` gives

\[
a_{\psi,L}
=
\frac{(1-\rho^2)\rho^{2L+2}}
{1-\rho^{2L+2}},
\tag{26}
\]

and (7)--(9) recover the logarithmic-depth threshold of `NB-081`. At the outer boundary `psi(z)=1-z`,

\[
a_{\psi,L}=\frac1{L+1},
\tag{27}
\]

so bounded charge requires `L` of order `R` and vanishing requires `L/R->infinity`.

A nonconstant inner factor supplies the opposite calibration: (23) is a fixed positive constant, so no finite-depth schedule with `L->infinity` can make the positive-density boundary contribution disappear. This is exactly compatible with the model-space stable tail in `NB-072`.

Multiplying `psi` by a nonzero scalar changes `epsilon_L` and `|c_0|^2` by the same factor, so `a_(psi,L)` and the charge threshold are invariant under trivial source rescaling.

The theorem is restricted to stationary scalar branch filters `psi(V_m)`. The actual Nyman innovations are nonstationary shrinking-cell outputs and are not identified with one fixed branch filter. In particular, the half-plane outerness of Burnol's deflated multiplier `O(s)` does not supply a rate for (1) in the Wold branch variable. Transferring (7) to the arithmetic source requires a new dictionary or a direct estimate of the corresponding nonstationary finite-prediction errors.

## 6. Prior-art boundary and research consequence

The scalar ingredients are classical. Beurling's theorem identifies outer functions with cyclic vectors in `H^2`; finite prediction errors and the Toeplitz Schur-complement formula (25) belong to classical Hardy/Szegő prediction theory. Contemporary work on optimal polynomial approximants likewise studies finite polynomial approximation of reciprocals of cyclic functions. No novelty is claimed for those scalar theories.

The line-local result is their exact insertion into the `NB-074` prediction-volume certificate together with the integer block-branching geometry: a fixed positive fraction of every prefix realizes exactly the same scalar degree-`L` prediction defect, yielding the two-sided global charge estimate (3). A targeted prior-art search found no Nyman--Beurling source using this finite-prediction rate as the exact variable-horizon screening threshold for the branch-matched controls. No priority claim is made.

No specialized external estimate is load-bearing beyond Beurling outer cyclicity already anchored in `SOURCES.md`, so that file is unchanged.

The live methodological target is now sharper than after `NB-081`. The phrase "quantitative outerness" can be replaced by an exact object: **the decay rate of the finite prediction excess**. For stationary controls, bounded screening is equivalent to making that excess `O(1/R)` at the chosen descendant depth. Therefore a polynomial arithmetic horizon can only follow from a source-specific theorem strong enough to produce the analogous `1/R` prediction accuracy after `O(log R)` generations; qualitative outerness, exact branching, and zero stable tail alone do not provide such a rate.