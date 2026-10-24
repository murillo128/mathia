# PF-351 — mismatched transition nodes can erase the coupled corridor-model angle

**Status:** EXACT-DERIVED + MATCHED-CORRIDOR-MODEL-CONTROL + ACTUAL-GLOBAL-TRANSITION-ANGLE-OPEN.

PF-346's scalar Cauchy correlation invariant does not extend to positive nearest-neighbor assembly with different transition spaces on neighboring modules. Two grounded modules, each using exactly the weighted cosine corridor norm, can have local Dirichlet low/high correlation arbitrarily close to one and globally shorted correlation exactly zero. This remains true after adding arbitrarily many common transition modes and eliminating all of them.

The result isolates a possible mechanism in the globally symmetric sector left open by PF-350. It does not realize that mechanism on the prime flute: the exact cuff Fourier lattices, geometric conductances, seam energy and pant remainders are not identified with this control.

## Exact model and cancellation criterion

Use the weighted space `H=L^2(R,sech(t)dt)`. For `x>1`, define

\[
 k_x(t)=\frac{\cos(\xi_x t)}{\sqrt{\pi(x+1)}},
 \qquad \xi_x=\pi^{-1}\operatorname{arcosh}x.
\]

PF-346's exact cosine identity gives

\[
 \langle k_x,k_y\rangle_H=C(x,y)=\frac1{x+y}.
 \tag{1}
\]

Thus the normalization is an invertible diagonal change of coefficient coordinates in the existing corridor Gram model. It preserves zero mixed entries and absolute normalized correlations after shorting.

Choose `1<a<b` and distinct `c,d in (a,b)`. Retain the two exterior modes on module 1 and allow one transition mode on each module:

\[
 f_1=z_a k_a+z_b k_b+t_c k_c,\qquad f_2=t_d k_d.
\]

The physical transition interval is `(xi_a,xi_b)`, so both eliminated frequencies are strictly between the retained ones. Give the internal edge conductance one and both exterior Dirichlet edges strictly positive conductances `ell,r`:

\[
 E(f_1,f_2)=\ell\|f_1\|_H^2+\|f_1-f_2\|_H^2+r\|f_2\|_H^2.
 \tag{2}
\]

Put

\[
 A=1+\ell,\quad B=1+r,\quad \vartheta=(AB)^{-1}\in(0,1),
 \quad K=\begin{pmatrix}A&-1\\-1&B\end{pmatrix}>0.
 \tag{3}
\]

The coefficient matrix is the corresponding restriction of `K tensor C`: an entry for module-frequency labels `(i,x),(j,y)` is `K_ij C(x,y)`. It is strictly positive because the energy is positive and the distinct modes on each module are linearly independent.

Let `S_loc` be the retained pair after minimizing over `t_c` with `f_2=0`, and `S_glob` after minimizing over both `t_c,t_d`. Then

\[
 \rho_{\rm loc}=\frac{|(S_{\rm loc})_{ab}|}
 {\sqrt{(S_{\rm loc})_{aa}(S_{\rm loc})_{bb}}}
 =\frac{2\sqrt{ab}}{a+b}.
 \tag{4}
\]

Define

\[
 h=\frac{d-c}{d+c},\qquad
 q=h^2\frac{(d-a)(b-d)}{(d+a)(d+b)}>0.
 \tag{5}
\]

The exact cancellation criterion is

\[
 \boxed{(S_{\rm glob})_{ab}=0
 \quad\Longleftrightarrow\quad AB=1+q.}
 \tag{6}
\]

Both shorted diagonals remain strictly positive. In particular, choose the positive grounded-edge conductances

\[
 \boxed{\ell=q/2,\qquad r=q/(2+q).}
 \tag{7}
\]

They give `AB=1+q`, hence `rho_glob=0` while (4) remains positive. No negative energy, indefinite block, nonlocal coupling or singular Schur inverse is used.

## Derivation

Write `b_c(x)=(x-c)/(x+c)`. Eliminate the module-1 transition coefficient first. The retained pair block becomes

\[
 A\,b_c(x)b_c(y)C(x,y),\qquad x,y\in\{a,b\}.
 \tag{8}
\]

The remaining cross entries to the module-2 mode and its pivot are

\[
 -b_c(x)hC(x,d),\qquad
 B V,\quad V=C(d,d)-\vartheta\frac{C(d,c)^2}{C(c,c)}>0.
 \tag{9}
\]

These follow by direct subtraction and the one-node Cauchy identity in PF-346. In particular,

\[
 (S_{\rm glob})_{ab}
 =A b_c(a)b_c(b)
 \left[C(a,b)-\frac{\vartheta h^2 C(a,d)C(d,b)}V\right].
 \tag{10}
\]

The elementary identities

\[
 \frac{C(d,c)^2}{C(c,c)}=C(d,d)(1-h^2),
 \qquad
 \frac{C(a,d)C(d,b)}{C(a,b)C(d,d)}
 =1+\frac{(d-a)(b-d)}{(d+a)(d+b)}
\]

give the useful closed form

\[
 \boxed{(S_{\rm glob})_{ab}
 =A b_c(a)b_c(b)C(a,b)
 \frac{1-\vartheta(1+q)}{1-\vartheta(1-h^2)}.}
 \tag{11}
\]

The denominator is positive. All factors outside the numerator are nonzero, proving (6). Strict positivity of the original matrix proves positivity of the two residual diagonal entries. Equation (4) follows from (8) by cancelling the diagonal factors.

For a rational certificate, take `a=2,b=5,c=3,d=4`. Then

\[
 q=1/1323,\quad \ell=1/2646,\quad r=1/2647,
\]
\[
 S_{\rm glob}
 =\operatorname{diag}\left(\frac{2647}{1852200},
                           \frac{2647}{8890560}\right),
 \qquad \rho_{\rm loc}^2=40/49.
 \tag{12}
\]

## Arbitrarily large shared transition sectors do not repair the invariant

Let `U` be any finite set of distinct nodes in `(a,b)` disjoint from `{c,d}`. Enlarge the transition spaces to

\[
 T_1=\operatorname{span}\{k_u:u\in U\}\oplus\operatorname{span}\{k_c\},
 \qquad
 T_2=\operatorname{span}\{k_u:u\in U\}\oplus\operatorname{span}\{k_d\}.
 \tag{13}
\]

Eliminate the common `U` coordinates on **both** modules first. For a complete tensor matrix the Schur identity is

\[
 (K\otimes C)^{/(\{1,2\}\times U)}
 =K\otimes C^{/U}
 =K\otimes(B_U C B_U),\qquad
 b_U(x)=\prod_{u\in U}\frac{x-u}{x+u}.
 \tag{14}
\]

Indeed, the inverse of the eliminated block is `K^(-1) tensor C_UU^(-1)`, so the Schur subtraction factors. The same identity holds on the selected remaining module-frequency labels: compression to those labels commutes with eliminating the common block. One may equivalently embed in the complete tensor matrix, fix the unused retained coefficients at zero, and then short `U`.

The remaining four-coordinate form is therefore the original model under the invertible diagonal congruence `b_U(x)`. Eliminating `c,d` commutes with that congruence. The globally shorted pair is

\[
 S_{\rm glob,U}
 =\operatorname{diag}(b_U(a),b_U(b))\,S_{\rm glob}\,
   \operatorname{diag}(b_U(a),b_U(b)).
 \tag{15}
\]

Thus (6) survives for every finite `|U|`, with no rank bound. Locally, shorting `U union {c}` still gives exactly (4). A sequence with `|U|` tending to infinity has exact zero correlation at every finite stage. No infinite-dimensional Schur inverse or limit of the unnormalized forms is asserted.

This also exposes the opposite control. If both modules have **identical** transition sets, (14) applies to the whole transition space. The local retained pair on one module retains the scalar Cauchy correlation. Cancellation here requires the mismatch, together with the specific coupling-to-grounding ratio in (6); mere assembly is not enough.

## Narrow bands and the required grounding scale

Fix `x_0>1` and place all four nodes in `[x_0,x_0+delta]`. Then

\[
 0<q\le\frac{\delta^4}{64x_0^4}.
 \tag{16}
\]

The first factor of (5) is at most `delta^2/(4x_0^2)`; the second is at most `delta^2/(16x_0^2)`. With distinct interior proportions fixed, `q` is of order `delta^4`. The physical frequency width is of order `delta` because `arcosh` has finite positive derivative near `x_0>1`.

Consequently, arbitrarily narrow positive physical bands admit the cancellation control, with local correlation tending to one. However, its grounding-to-internal-conductance ratios also tend to zero at fourth order. The result does **not** exhibit cancellation with an independently fixed positive lower bound on both grounding ratios. At `c=d`, the mismatch disappears and `q=0`; the construction would demand zero grounding and is outside the strictly positive setup.

For the flute, the conductances and frequency lattices come from the same endpoint geometry. They cannot be tuned independently as in (7). Determining whether actual transition transmission can approach this weak-grounding regime is an additional geometric question, not a consequence of this counterexample.

## Prior art, independent checks and significance

Cauchy Schur structure and correlation normalization are classical: Gohberg, Kailath and Olshevsky, *Fast Gaussian Elimination with Partial Pivoting for Matrices with Displacement Structure* (1995), [author manuscript](https://www2.math.uconn.edu/~olshevsky/papers/geppdsam.pdf); Forrester and Zhang, *Parametrising correlation matrices* (2020), [arXiv:1812.07685](https://arxiv.org/abs/1812.07685), already S23. Grounded graph Schur elimination is classical Kron reduction: Dörfler and Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60 (2013), 150–163, [arXiv:1102.2950](https://arxiv.org/abs/1102.2950). These sources supply context; (6), (11), and the model control are derived directly here. No novel general matrix theorem is claimed.

The coefficient matrix in (2) is a Gram-valued network form, not a scalar graph Laplacian in the frequency coordinates. Therefore scalar Kron rules about signs of off-diagonal graph conductances do not prohibit the cancellation in (11).

Supplementary exact rational elimination checked 48 controls: `a=2`, `b=a+delta`, `delta in {1,1/10,1/100,1/1000}`, `(c,d)=(a+i delta/4,a+j delta/4)` for `(i,j) in {(1,2),(2,1),(1,3)}`, and `|U| in {0,1,4,12}`. For `m=|U|`, use `U={a+delta(2j+1)/(8m+8):0<=j<m}` and the grounds (7). Every elimination pivot was positive; the global mixed entry vanished exactly; (14)–(15) and the local squared correlation `4ab/(a+b)^2` held. Three further rational choices of `A,B>1` checked (10) away from the root. These are checks of finite algebra, not numerical evidence about the pant PDE. The proofs do not depend on the checks.

PF-348 already gives an arbitrary positive-matrix control showing that further relaxation can erase correlation. The additional content here is its realization **within the same exact cosine kernel and a positive nearest-neighbor difference energy**, with an explicit mismatch/grounding threshold and an unbounded shared-transition rank. PF-279 concerns extension mass in scalar resolvent cut norms; it does not address this frequency-normalized Schur correlation.

This closes the inference that PF-346's scalar correlation invariance, positive pant-style adjacency and a large transition sector alone force a surviving global symmetric witness. PF-350's parity comparison does not supply the missing symmetric witness. Conversely, erasing this single retained pair in a control is not evidence for compactness of the full low/high angle, even for the control, and proves no ideal bound for the actual surface.

The decisive remaining comparison must retain the actual unequal cuff Fourier lattices, their geometric conductance/grounding constraints, and errors measured relative to the same shorted diagonal energies. The finite common sets in (13) need not be complete Fourier bands for any pair of physical cuff periods. No assertion of prime-flute realization, scattering, weak trace class, zeta structure or RH follows.
