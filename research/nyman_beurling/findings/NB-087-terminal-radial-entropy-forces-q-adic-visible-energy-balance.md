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
\tag{1}
\]

The unresolved test in `NB-086` is still apparently quadratic-dimensional: it asks about all normalized pairings in a terminal block of size `asymp R`. Exact integer branching collapses a substantial part of that test to **one scalar norm ratio per q-adic sibling block**.

For real `x>=1`, let `J_x` denote Paley--Wiener truncation to `[0,log x]`. Define the complete terminal parent set

\[
\mathcal P_{R,q}
:=
\left\{
 j:
 \left\lceil\frac{R}{q^2}\right\rceil
 \le j\le
 \left\lfloor\frac{R}{q}\right\rfloor-1
\right\}.
\tag{2}
\]

For `j in mathcal P_(R,q)`, its entire descendant block

\[
B_j^{(q)}:=\{qj,qj+1,\ldots,q(j+1)-1\}
\tag{3}
\]

lies in `I_(R,q)`. Put

\[
n_{k,R}:=\|J_RD_k\|^2,
\qquad
S_{j,R}^{(q)}:=\sum_{k\in B_j^{(q)}}n_{k,R},
\tag{4}
\]

and define the dimensionless visible branch-energy distortion

\[
\boxed{
\eta_{j,R}^{(q)}
:=
\frac{q\,\|J_{R/q}D_j\|^2}{S_{j,R}^{(q)}}-1.
}
\tag{5}
\]

Then there is an explicit constant `c_q>0`, depending only on `q`, such that

\[
\boxed{
\mathfrak S_{R,q}
\ge
c_q
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2.
}
\tag{6}
\]

One may take

\[
c_q
=
\min_{0<x\le q}
\frac{x-1-\log x}{(x-1)^2}>0,
\tag{7}
\]

with the quotient extended continuously by `1/2` at `x=1`. In the dyadic case the block algebra improves the constant to one:

\[
\boxed{
\mathfrak S_{R,2}
\ge
\sum_{j=\lceil R/4\rceil}^{\lfloor R/2\rfloor-1}
\left(
\frac{2\,\|J_{R/2}D_j\|^2}
{\|J_RD_{2j}\|^2+\|J_RD_{2j+1}\|^2}
-1
\right)^2.
}
\tag{8}
\]

Hence bounded fixed-`q` radial charge forces

\[
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2=O_q(1)
\tag{9}
\]

along the same sequence. Since

\[
|\mathcal P_{R,q}|
=\frac{q-1}{q^2}R+O_q(1),
\tag{10}
\]

the mean square distortion is `O_q(R^(-1))` and its RMS is `O_q(R^(-1/2))`. More sharply, for every fixed `epsilon>0`, bounded charge permits only `O_(q,epsilon)(1)` complete terminal blocks with `|eta_(j,R)^(q)|>=epsilon`.

Conversely,

\[
\boxed{
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2\longrightarrow\infty
\quad\Longrightarrow\quad
\mathfrak S_{R,q}\longrightarrow\infty.
}
\tag{11}
\]

Thus a fixed-`q` radial route can be falsified without estimating any aliased Szegő floor and without reconstructing the full terminal correlation matrix. The live source problem is reduced from `O(R^2)` normalized pairings to `O(R)` explicit two-scale visible norms.

## 1. Exact branching selects a canonical terminal Rayleigh quotient

`NB-084` gives

\[
U_{\log q}D_j
=\frac1{\sqrt q}
\sum_{k=qj}^{q(j+1)-1}D_k.
\tag{12}
\]

Paley--Wiener translation intertwines the matched cutoffs,

\[
J_RU_{\log q}=U_{\log q}J_{R/q}.
\tag{13}
\]

For a complete block set

\[
v_k:=J_RD_k,
\qquad k\in B_j^{(q)}.
\]

Equations (12)--(13) give

\[
\frac1{\sqrt q}
\sum_{k\in B_j^{(q)}}v_k
=U_{\log q}J_{R/q}D_j,
\]

and therefore

\[
\left\|\sum_{k\in B_j^{(q)}}v_k\right\|^2
=q\,\|J_{R/q}D_j\|^2.
\tag{14}
\]

Let `mathcal R_(j;R,q)` be the normalized `q x q` correlation matrix of the child vectors. `NB-062` implies that these vectors are nonzero and independent, so the matrix is positive definite with diagonal one. With

\[
a_j=(\sqrt{n_{k,R}})_{k\in B_j^{(q)}},
\]

we have

\[
a_j^*\mathcal R_{j;R,q}a_j
=\left\|\sum_{k\in B_j^{(q)}}v_k\right\|^2,
\qquad
\|a_j\|^2=S_{j,R}^{(q)}.
\]

Thus

\[
\boxed{
\eta_{j,R}^{(q)}
=
\frac{a_j^*(\mathcal R_{j;R,q}-I)a_j}{\|a_j\|^2}.
}
\tag{15}
\]

In particular,

\[
|\eta_{j,R}^{(q)}|
\le
\|\mathcal R_{j;R,q}-I\|_{\rm op}
\le
\|\mathcal R_{j;R,q}-I\|_F.
\tag{16}
\]

The scalar in (5) is therefore not an arbitrary compression. Exact Nyman branching chooses the average coefficient direction, and its normalized Rayleigh defect is determined entirely by the parent visible norm at scale `R/q` and the diagonal child energy at scale `R`.

## 2. Sibling energy distortion has a compulsory determinant cost

Let `lambda_1,...,lambda_q` be the eigenvalues of `mathcal R_(j;R,q)`. Their sum is `q` and each lies in `(0,q]`. Hence

\[
-\log\det\mathcal R_{j;R,q}
=
\sum_{r=1}^q
(\lambda_r-1-\log\lambda_r)
\ge
c_q\sum_{r=1}^q(\lambda_r-1)^2.
\]

Since the matrix is Hermitian,

\[
\sum_{r=1}^q(\lambda_r-1)^2
=\|\mathcal R_{j;R,q}-I\|_F^2.
\]

Combining with (16),

\[
\boxed{
-\log\det\mathcal R_{j;R,q}
\ge
c_q|\eta_{j,R}^{(q)}|^2.
}
\tag{17}
\]

Partition the full terminal correlation matrix into all complete sibling blocks together with leftover singleton coordinates. Repeated Fischer determinant inequality gives

\[
\det\mathcal R_{R,q}
\le
\prod_{j\in\mathcal P_{R,q}}
\det\mathcal R_{j;R,q},
\tag{18}
\]

because every leftover singleton block has determinant one. Therefore

\[
-\log\det\mathcal R_{R,q}
\ge
c_q
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2.
\tag{19}
\]

Equation (6) now follows from the terminal entropy bound (1).

For `q=2`, if `rho` is the normalized sibling correlation, then (15) becomes

\[
\eta
=
\frac{2\Re\langle v_{2j},v_{2j+1}\rangle}
{\|v_{2j}\|^2+\|v_{2j+1}\|^2}.
\]

Arithmetic--geometric mean gives `|rho|^2>=eta^2`, so

\[
-\log(1-|\rho|^2)\ge|\rho|^2\ge\eta^2,
\]

which proves the sharper dyadic inequality (8).

## 3. The bounded-charge threshold is now scalar and quantitative

Suppose `mathfrak S_(R,q)<=M` along an unbounded sequence. Equation (6) gives

\[
\sum_{j\in\mathcal P_{R,q}}
|\eta_{j,R}^{(q)}|^2
\le\frac{M}{c_q}.
\tag{20}
\]

Dividing by (10) yields the `O(R^(-1))` mean-square law. For any fixed tolerance `epsilon>0`, Chebyshev also gives

\[
\#\{j\in\mathcal P_{R,q}:|\eta_{j,R}^{(q)}|\ge\epsilon\}
\le
\frac{M}{c_q\epsilon^2}.
\tag{21}
\]

The precise consequence is therefore an `l^2` budget, not uniform pointwise convergence: a bounded number of order-one failures is allowed at each scale, and an unbounded number of smaller failures is allowed only if their squared total remains bounded.

This makes the falsification threshold transparent. If a positive fraction of the `asymp R` complete terminal branches has distortion bounded below by a fixed constant, the charge grows linearly. More generally, distortion of common size `a_R` on `asymp R` branches forces a lower bound of order `R a_R^2`. Any actual-source estimate substantially larger than the `R^(-1/2)` RMS threshold therefore kills the fixed-`q` radial route.

No such visible-norm asymptotic is claimed here. Full innovation norms are insufficient: (5) uses the matched truncated norms `||J_(R/q)D_j||` and `||J_RD_k||`. Estimating those quantities is the next source-specific problem.

## 4. Controls, prior art, and the new frontier

For the unit-outer control `O=1`, `NB-062` gives orthogonal unit cell innovations. Every complete sibling block has

\[
\|J_RD_k^{(0)}\|^2=1,
\qquad
\|J_{R/q}D_j^{(0)}\|^2=1,
\]

so `eta_(j,R)^(q)=0` identically. The new obstruction therefore does not manufacture entropy in the memory-free control.

The exact-branching stable-tail controls of `NB-071/072` are also not contradicted. They may keep the scalar ratios in (5) sufficiently balanced while sustaining their obstruction through other nonlocal directions. Equation (6) is a necessary condition for bounded radial charge, not a source-free stable-tail theorem.

`NB-077`--`NB-079` already resolve q-adic refinement into average and contrast information channels. The present result acts at a different boundary: the terminal visible suffix where `NB-086` makes the radial future completely invisible. Its extra content is that one canonical average-direction Rayleigh quotient per terminal sibling block already carries a compulsory determinant cost. Passing this scalar test does not control the remaining within-block directions, cross-block correlations, earlier indices, or the aliased Szegő floors.

Fischer's determinant inequality, Rayleigh/Frobenius comparison, and the convex identity `x-1-log x` are classical matrix facts; no novelty is claimed for them. The prior-art audit checked Werner Ehm's explicit Nyman Gram/quadratic-form analysis (`arXiv:2405.06349`), Hugh Carvill's Mellin-smoothed ladder Gram and block-compressibility analysis (`arXiv:2510.18132`), and the classical Báez--Duarte dilation literature. Those works do not supply this splice between the exact innovation branching law, the terminal **truncated** determinant of `NB-086`, and the two-scale scalar visible-energy ratio (5). No priority claim is made.

No specialized external estimate is load-bearing, so `SOURCES.md` requires no new anchor.

The live fixed-`q` question can now be attacked before any detailed Toeplitz/Szegő analysis: estimate

\[
\boxed{
\eta_{j,R}^{(q)}
=
\frac{q\,\|J_{R/q}D_j\|^2}
{\sum_{k=qj}^{q(j+1)-1}\|J_RD_k\|^2}-1
}
\tag{22}
\]

for `j\asymp R` in the complete terminal sibling blocks. Divergent squared mass kills that radial certificate. Bounded squared mass only passes this necessary test; it does not prove radial screening or the Nyman closure.