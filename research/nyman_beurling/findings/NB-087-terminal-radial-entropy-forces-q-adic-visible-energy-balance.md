# NB-087 — terminal radial entropy forces q-adic visible-energy balance

**Status:** `EXACT-DERIVED + ACTUAL-NYMAN-SOURCE + TERMINAL-VISIBLE-GRAM + Q-ADIC-BRANCH-ENERGY + SCALAR-ENTROPY-OBSTRUCTION + METHOD-ADVANCE`.

`NB-086` reduces every fixed-integer-dilation radial certificate to a finite current-window obstruction. If

\[
\mathfrak S_{R,q}
=\sum_{j<R}\log\frac{G_{j,q}}{\widehat\Pi_{j,R}^2},
\qquad q\ge2,
\]

is the infinite-depth radial floor charge and `mathcal R_(R,q)` is the normalized Gram matrix of the terminal visible innovations

\[
I_{R,q}=\{\lceil R/q\rceil,\ldots,R-1\},
\]

then

\[
\mathfrak S_{R,q}\ge-\log\det\mathcal R_{R,q}.
\]

The live problem was still apparently quadratic-dimensional: estimate the full family of normalized correlations inside a terminal block containing `asymp R` innovations. Exact integer branching collapses a large part of that test to **one scalar per q-adic sibling block**.

For real `x>=1`, let `J_x` denote Paley--Wiener truncation to `[0,log x]`; this extends the integer-cutoff notation already used in the line. Fix an integer `R>=2` and let

\[
\mathcal P_{R,q}
:=
\left\{
 j:\
 \left\lceil\frac{R}{q^2}\right\rceil
 \le j\le
 \left\lfloor\frac{R}{q}\right\rfloor-1
\right\}.
\tag{1}
\]

For every `j in mathcal P_(R,q)`, the complete descendant block

\[
B_j^{(q)}:=\{qj,qj+1,\ldots,q(j+1)-1\}
\tag{2}
\]

lies inside the terminal set `I_(R,q)`. Put

\[
n_{k,R}:=\|J_RD_k\|^2,
\qquad
S_{j,R}^{(q)}:=\sum_{k\in B_j^{(q)}}n_{k,R},
\tag{3}
\]

and define the dimensionless **visible branch-energy distortion**

\[
\boxed{
\eta_{j,R}^{(q)}
:=
\frac{
q\,\|J_{R/q}D_j\|^2
}{
S_{j,R}^{(q)}
}-1.
}
\tag{4}
\]

Then there is a constant `c_q>0`, depending only on the fixed branching factor `q`, such that

\[
\boxed{
\mathfrak S_{R,q}
\ge
c_q
\sum_{j\in\mathcal P_{R,q}}
\left|\eta_{j,R}^{(q)}\right|^2.
}
\tag{5}
\]

The constant is completely explicit. With

\[
\phi(x)=x-1-\log x,
\]

and the quotient extended continuously by `1/2` at `x=1`, one may take

\[
\boxed{
c_q=
\min_{0<x\le q}
\frac{\phi(x)}{(x-1)^2}>0.
}
\tag{6}
\]

For `q=2` the block algebra gives the sharper constant `1`:

\[
\boxed{
\mathfrak S_{R,2}
\ge
\sum_{j=\lceil R/4\rceil}^{\lfloor R/2\rfloor-1}
\left(
\frac{
2\,\|J_{R/2}D_j\|^2
}{
\|J_RD_{2j}\|^2+\|J_RD_{2j+1}\|^2
}
-1
\right)^2.
}
\tag{7}
\]

Thus bounded fixed-`q` radial charge has a strong scalar consequence. Along any sequence on which `mathfrak S_(R,q)<=M`,

\[
\boxed{
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2
\le \frac{M}{c_q}.
}
\tag{8}
\]

Since

\[
|\mathcal P_{R,q}|
=\frac{q-1}{q^2}R+O_q(1),
\tag{9}
\]

the root-mean-square branch-energy distortion must be `O_q,M(R^(-1/2))`. Even more sharply, for every fixed `epsilon>0`, the number of terminal sibling blocks with

\[
|\eta_{j,R}^{(q)}|\ge\epsilon
\]

is bounded independently of `R` by `M/(c_q epsilon^2)`.

So a bounded-charge radial proof cannot merely require small **average pair correlation**. On all but `O(1)` complete terminal sibling blocks, the visible energy of the exact branch average must become extremely close to the diagonal child-energy average. Conversely, proving

\[
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2\longrightarrow\infty
\tag{10}
\]

already forces `mathfrak S_(R,q)->infinity` and rules out that fixed-`q` radial certificate, without estimating any individual aliased Szegő floor and without reconstructing the full terminal correlation matrix.

This does **not** decide the actual source. The new scalar distortions may in principle be square-summable across the terminal blocks. The gain is that the `NB-086` frontier has been reduced from an `O(R^2)` family of normalized pairings to `O(R)` explicit two-scale norm ratios tied directly to exact arithmetic branching.

## 1. Exact branching identifies the average-direction Rayleigh quotient

`NB-084` gives the exact integer-dilation identity

\[
U_{\log q}D_j
=\frac1{\sqrt q}
\sum_{k=qj}^{q(j+1)-1}D_k.
\tag{11}
\]

Paley--Wiener translation intertwines the two cutoffs exactly:

\[
J_RU_{\log q}
=U_{\log q}J_{R/q}.
\tag{12}
\]

Therefore, with

\[
v_k:=J_RD_k,
\qquad k\in B_j^{(q)},
\]

we have

\[
\boxed{
\frac1{\sqrt q}
\sum_{k\in B_j^{(q)}}v_k
=
U_{\log q}J_{R/q}D_j.
}
\tag{13}
\]

Taking norms gives

\[
\left\|\sum_{k\in B_j^{(q)}}v_k\right\|^2
=q\,\|J_{R/q}D_j\|^2.
\tag{14}
\]

Let `mathcal R_(j;R,q)` be the normalized `q x q` correlation matrix of these child vectors. Every `v_k` is nonzero and the family is independent by `NB-062`, so this matrix is positive definite with diagonal one. Define

\[
a_j=(\sqrt{n_{k,R}})_{k\in B_j^{(q)}}.
\tag{15}
\]

By the definition of a correlation matrix,

\[
a_j^*\mathcal R_{j;R,q}a_j
=
\left\|\sum_{k\in B_j^{(q)}}v_k\right\|^2
=q\,\|J_{R/q}D_j\|^2,
\tag{16}
\]

while

\[
\|a_j\|^2=S_{j,R}^{(q)}.
\tag{17}
\]

Hence the branch-energy distortion is exactly one Rayleigh deviation from the identity:

\[
\boxed{
\eta_{j,R}^{(q)}
=
\frac{a_j^*(\mathcal R_{j;R,q}-I)a_j}{\|a_j\|^2}.
}
\tag{18}
\]

Consequently

\[
|\eta_{j,R}^{(q)}|
\le
\|\mathcal R_{j;R,q}-I\|_{\rm op}
\le
\|\mathcal R_{j;R,q}-I\|_F.
\tag{19}
\]

This is the scalarization. No individual child pairing has been estimated; exact branching selects one canonical coefficient direction whose Rayleigh defect is determined only by parent and child visible norms.

## 2. Every sibling energy distortion costs normalized Gram volume

Let

\[
\lambda_1,\ldots,\lambda_q>0
\]

be the eigenvalues of `mathcal R_(j;R,q)`. Since its diagonal is one,

\[
\sum_{r=1}^q\lambda_r=q,
\qquad
0<\lambda_r\le q.
\tag{20}
\]

As in `NB-086`, trace normalization gives

\[
-\log\det\mathcal R_{j;R,q}
=
\sum_{r=1}^q
\bigl(\lambda_r-1-\log\lambda_r\bigr).
\tag{21}
\]

By the definition of `c_q` in (6),

\[
-\log\det\mathcal R_{j;R,q}
\ge
c_q
\sum_{r=1}^q(\lambda_r-1)^2
=
c_q\|\mathcal R_{j;R,q}-I\|_F^2.
\tag{22}
\]

Combining (19) and (22),

\[
\boxed{
-\log\det\mathcal R_{j;R,q}
\ge
c_q|\eta_{j,R}^{(q)}|^2.
}
\tag{23}
\]

Now partition the full terminal index set `I_(R,q)` into all complete sibling blocks `B_j^(q)` with `j in mathcal P_(R,q)` plus the remaining individual coordinates. Repeated Fischer determinant inequality for positive-definite principal blocks gives

\[
\det\mathcal R_{R,q}
\le
\prod_{j\in\mathcal P_{R,q}}
\det\mathcal R_{j;R,q},
\tag{24}
\]

because each leftover singleton correlation block has determinant one. Therefore

\[
-\log\det\mathcal R_{R,q}
\ge
\sum_{j\in\mathcal P_{R,q}}
-\log\det\mathcal R_{j;R,q}.
\tag{25}
\]

Insert (23), then use the `NB-086` lower bound

\[
\mathfrak S_{R,q}\ge-\log\det\mathcal R_{R,q}
\tag{26}
\]

to prove (5).

For `q=2`, write the sibling correlation as `rho`. Equation (18) gives

\[
\eta
=
\frac{2\Re\langle v_{2j},v_{2j+1}\rangle}
{\|v_{2j}\|^2+\|v_{2j+1}\|^2}.
\tag{27}
\]

Hence arithmetic--geometric mean gives

\[
|\rho|^2
\ge
\eta^2,
\tag{28}
\]

and therefore

\[
-\log\det
\begin{pmatrix}
1&\rho\\
\overline\rho&1
\end{pmatrix}
=
-\log(1-|\rho|^2)
\ge|\rho|^2
\ge\eta^2.
\tag{29}
\]

This proves the sharper dyadic bound (7).

## 3. Bounded radial charge forces near-exact visible energy conservation on almost every branch

Suppose `mathfrak S_(R,q)<=M` along an unbounded sequence. Equation (5) immediately gives (8). Since the number of complete terminal sibling blocks grows linearly with `R`,

\[
\frac1{|\mathcal P_{R,q}|}
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2
=O_{q,M}(R^{-1}).
\tag{30}
\]

Thus the relevant scalar balance is much stronger than convergence in density at an unspecified rate. The `L^2` average distortion itself must decay at least on the `R^(-1)` scale, and the RMS distortion at least on the `R^(-1/2)` scale.

For a fixed `epsilon>0`, Chebyshev applied to (8) yields

\[
\#\{j\in\mathcal P_{R,q}:|\eta_{j,R}^{(q)}|\ge\epsilon\}
\le
\frac{M}{c_q\epsilon^2},
\tag{31}
\]

uniformly in `R`. Therefore all but a bounded number of complete terminal branches must satisfy

\[
q\,\|J_{R/q}D_j\|^2
=
\left(1+o(1)\right)
\sum_{k=qj}^{q(j+1)-1}\|J_RD_k\|^2
\tag{32}
\]

in the quantitative mean-square sense of (30).

This is a source-facing target that uses only scalar norms at two matched scales. The parent and children have the same relative horizon geometry: the parent is observed up to `R/q`, while its descendants are observed up to `R`. That exact matching comes from the Nyman dilation law rather than from a generic correlation estimate.

A useful falsification threshold follows immediately. If a positive fraction of terminal branches has distortion bounded away from zero, then the radial charge grows linearly. More generally, even distortions of common size `a_R` on `asymp R` branches force a lower bound of order `R a_R^2`. Thus a source asymptotic producing, for example, `a_R` of logarithmic size rather than `R^(-1/2)` size would already destroy the fixed-`q` radial route.

No such asymptotic is asserted here. Establishing it requires actual control of the visible norms `||J_RD_j||`, not merely the full norms or raw untruncated Gram entries.

## 4. Relation to the earlier q-adic information ledger and controls

`NB-077`--`NB-079` use integer branching to compare full continuation and prediction information under q-adic refinement, resolving the new fine coordinates into average and contrast channels. The present result uses the same exact branching structure at a different boundary: the terminal visible suffix of `NB-086`, where the radial future is absent from the current window.

The distinction is useful. The earlier ledger still contains conditional-information quantities for complete past/future blocks. Equations (4)--(7) extract from each terminal sibling block a **single canonical Rayleigh quotient** that already has to satisfy a square-summable budget if the infinite radial floor charge is bounded. This does not replace the refinement ledger; it gives a cheaper necessary test for the particular fixed-`q` radial certificate.

The unit-outer control `O=1` calibrates the result exactly. `NB-062` gives orthogonal unit cell innovations, so for every complete sibling block

\[
\|J_RD_k^{(0)}\|^2=1,
\qquad
\|J_{R/q}D_j^{(0)}\|^2=1,
\]

and hence

\[
\eta_{j,R}^{(q)}=0.
\tag{33}
\]

The scalar budget and the terminal determinant deficit both vanish, as they should.

At the opposite extreme, the exact-branching stable-tail controls of `NB-071/072` are not contradicted. They may arrange the visible branch-energy ratios in (4) close enough to one while sustaining their obstruction through other nonlocal geometry. The theorem is therefore a necessary condition for bounded radial charge, not a source-free proof that exact branching eliminates stable tails.

The normalization in (4) is also essential. Raw parent or child norms may grow with the scale, and a fixed additive energy mismatch can become negligible. The radial entropy only sees the mismatch after normalization by the total visible child energy, exactly as (18) records.

## 5. Prior-art boundary and consequence for the live frontier

Fischer's determinant inequality, the Rayleigh-quotient bound by Frobenius norm, and the convex identity `x-1-log x` are classical finite-dimensional matrix facts; no novelty is claimed for them. Exact integer-dilation covariance of the Báez--Duarte family is likewise classical at the generator level and was converted into the innovation branching identity earlier in this line.

The prior-art audit checked Werner Ehm's explicit Nyman Gram-matrix/quadratic-form analysis (`arXiv:2405.06349`) and Hugh Carvill's Mellin-smoothed ladder Gram/block-compressibility analysis (`arXiv:2510.18132`), together with the classical Báez--Duarte dilation literature. Those works study global or smoothed Gram structure, not the present splice between the exact innovation branching law, the **terminal truncated** correlation determinant of `NB-086`, and the scalar two-scale energy ratio (4). A targeted search did not locate this specific visible-energy necessary condition; no priority claim is made.

No specialized external estimate is load-bearing in (5)--(31), so `SOURCES.md` requires no new anchor.

The live fixed-`q` test is now simpler. Before estimating aliased Szegő floors or even individual terminal correlations, estimate

\[
\boxed{
\eta_{j,R}^{(q)}
=
\frac{
q\,\|J_{R/q}D_j\|^2
}{
\sum_{k=qj}^{q(j+1)-1}\|J_RD_k\|^2
}-1
}
\tag{34}
\]

for `j asyp R` in the complete terminal sibling blocks. If its squared mass diverges, the fixed-`q` radial certificate is dead. If its squared mass remains bounded, that necessary test is passed but the remaining within-block directions, cross-block correlations, earlier indices, and the aliased Szegő floors can still make the full charge diverge.

This reduction is therefore deliberately one-sided: it replaces a large matrix obstruction by a scalar arithmetic energy-balance problem without pretending that passing the scalar test proves radial screening or the Nyman closure.