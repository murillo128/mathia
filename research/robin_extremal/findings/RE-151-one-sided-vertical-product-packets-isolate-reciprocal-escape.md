# RE-151 — one-sided vertical product packets isolate reciprocal escape

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FINITE-ZERO-EDGE + LEADING-ROBIN-PACKET + ZERO-HORIZONTAL-SPREAD + PURE-VERTICAL-ESCAPE + ONE-SIDED-WINDOW + SCALE-MAXIMAL-ANCHOR + EXPONENTIAL-RADIUS-SUPPRESSION + ARBITRARILY-SLOW-SCALED-ESCAPE + DECISIVE-NEGATIVE + REVIEW-REPAIRED`.

This finding replaces `RE-149`. The adversarial review identified a real window mismatch: the product construction in `RE-149` proves contraction on `u/U in [1-kappa,1]`, while its headline displayed a symmetric window around `U`. The vertical obstruction survives unchanged on the interval actually proved, but no claim is made here for `[U,(1+kappa)U]`.

The substantive conclusion is still strong. A strict-subedge Robin atom can be scale-maximal and algebraically strong while a packet lying **exactly on its vertical line** hides it exponentially well on a fixed macroscopic one-sided observation window. The scaled vertical radius may diverge as slowly as prescribed. Thus removing the near-left horizontal mechanism of `RE-144` does not by itself close the Robin visibility problem; pure vertical phase geometry remains an independent obstruction.

Fix

\[
\frac12<\sigma_0<\Theta<1,\qquad A>0,\qquad 0<\kappa<\frac12,
\tag{1}
\]

and let `W(U)` and `L(T)` be arbitrary nondecreasing functions tending to infinity. There is a single formal simple spectrum `Z_ctl`, closed under conjugation and `rho -> 1-rho`, with attained finite right edge `Re rho=Theta`, phases `U_j->infinity`, and strict-subedge target atoms

\[
\rho_{0,j}=\beta_j+i\Gamma_j,
\tag{2}
\]

such that, for

\[
a_{\rho,0}(u):=\frac{e^{-(\Theta-\beta)u}}{\rho(1-\rho)},
\tag{3}
\]

the target is algebraically strong and globally scale-maximal at `U_j`,

\[
M_0^{\rm ctl}(U_j)
=(1+o(1))|a_{\rho_{0,j},0}(U_j)|
\asymp U_j^{-A}.
\tag{4}
\]

Every atom responsible for the stage cancellation has exactly the same real part,

\[
\beta=\beta_j,
\tag{5}
\]

and lies in the one-sided scaled vertical interval

\[
0\le U_j(\gamma-\Gamma_j)\le W(U_j).
\tag{6}
\]

Nevertheless

\[
\boxed{
\sup_{(1-\kappa)U_j\le u\le U_j}
|\mathcal S_0^{\rm ctl}(u)|
=o\!\left(M_0^{\rm ctl}(U_j)\right).
}
\tag{7}
\]

If `R_j` is the scaled vertical radius of the active stage, then for constants `c_kappa,C_kappa>0`,

\[
R_j\asymp_\kappa j,
\qquad
\sup_{(1-\kappa)U_j\le u\le U_j}
|\mathcal S_{0,j}(u)|
\le C_\kappa e^{-c_\kappa R_j}
|a_{\rho_{0,j},0}(U_j)|.
\tag{8}
\]

The off-critical one-level count can simultaneously be made arbitrarily sparse:

\[
N_{\rm ctl}(\sigma_0,T)\le L(T)
\tag{9}
\]

for all sufficiently large `T`, up to a harmless fixed enlargement for the quartet used to attain the edge.

## 1. Contractive phase block on the proved window

Put

\[
I_\kappa=[1-\kappa,1],\qquad
x_c=1-\frac\kappa2,\qquad
\omega_\kappa=\frac\pi{x_c}.
\tag{10}
\]

Then `e^{i omega_kappa x_c}=-1`, so for `x in I_kappa`,

\[
|1+e^{i\omega_\kappa x}|
=|1-e^{i\omega_\kappa(x-x_c)}|
\le
2\sin\!\left(\frac{\pi\kappa}{4(1-\kappa/2)}\right)
=:q_\kappa.
\tag{11}
\]

Because `kappa<1/2`, the argument of the sine is `<pi/6`, hence

\[
0<q_\kappa<1.
\tag{12}
\]

This is the only interval estimate used below. In particular, (11) does **not** assert contraction on `[1,1+kappa]`; this is precisely the scope correction relative to `RE-149`.

## 2. Same-real-part subset packet

Choose `U_j` recursively and set

\[
\Gamma_j=U_j^{A/2},\qquad
\delta_j=U_j^{-2},\qquad
\beta_j=\Theta-\delta_j.
\tag{13}
\]

For `1<=ell<=j`, let

\[
\varepsilon_{j,\ell}=U_j^{-3}3^{-\ell},\qquad
\omega_{j,\ell}=\omega_\kappa+\varepsilon_{j,\ell},
\tag{14}
\]

and for every subset `S` of `{1,...,j}` define

\[
\rho_{j,S}=\beta_j+i\gamma_{j,S},\qquad
\gamma_{j,S}=\Gamma_j+\frac1{U_j}\sum_{\ell\in S}\omega_{j,\ell}.
\tag{15}
\]

The `2^j` points are simple and have exactly the same real part. The ternary perturbations separate equal-cardinality subset sums, while different cardinalities differ by an integer multiple of `omega_kappa` plus a negligible perturbation. The empty subset is the target.

At fixed `beta_j in (1/2,1)`,

\[
|\rho(1-\rho)|^2
=(\beta_j^2+\gamma^2)((1-\beta_j)^2+\gamma^2)
\tag{16}
\]

is strictly increasing for `gamma>0`. Since every nonempty subset raises the ordinate, the target is the unique exact maximizer of the leading coefficient within the stage. Moreover

\[
|a_{\rho_{0,j},0}(U_j)|
=(1+o(1))\Gamma_j^{-2}
=(1+o(1))U_j^{-A}.
\tag{17}
\]

For `u=U_jx`, `x in I_kappa`, all stage points have identical horizontal damping and

\[
\frac{d_{\rho_{j,S}}}{d_{\rho_{0,j}}}
=1+O\!\left(\frac{j}{U_j\Gamma_j}\right),
\qquad d_\rho:=\frac1{\rho(1-\rho)}.
\tag{18}
\]

Their relative carriers satisfy

\[
e^{i(\gamma_{j,S}-\Gamma_j)u}
=\prod_{\ell\in S}e^{i\omega_{j,\ell}x}.
\tag{19}
\]

Freezing the harmless coefficient variation, the positive-frequency stage factors as

\[
a_{\rho_{0,j},0}(u)e^{i\Gamma_j u}
\prod_{\ell=1}^{j}(1+e^{i\omega_{j,\ell}x}).
\tag{20}
\]

Choose `q_1` with `q_kappa<q_1<1`. For large `j`, every factor in (20) has modulus at most `q_1` uniformly on `I_kappa`. Restoring (18) costs at most

\[
|a_{\rho_{0,j},0}(u)|
O\!\left(\frac{j2^j}{U_j\Gamma_j}\right).
\tag{21}
\]

The recursive choice of `U_j` can impose

\[
\frac{j2^j}{U_j\Gamma_j}\le q_1^j,
\tag{22}
\]

so

\[
\sup_{(1-\kappa)U_j\le u\le U_j}
\left|\sum_S a_{\rho_{j,S},0}(u)e^{i\gamma_{j,S}u}\right|
\ll q_1^j|a_{\rho_{0,j},0}(U_j)|.
\tag{23}
\]

Taking `2 Re` preserves the same exponential order.

## 3. Exponential dependence on vertical radius

The scaled horizontal radius is exactly zero and the scaled vertical radius is

\[
R_j
=U_j\max_S|\gamma_{j,S}-\Gamma_j|
=j\omega_\kappa+o(1).
\tag{24}
\]

Thus (23) is precisely exponential suppression in radius:

\[
\sup_{(1-\kappa)U_j\le u\le U_j}|\mathcal S_{0,j}(u)|
\ll
\exp[-(c_\kappa+o(1))R_j]
|a_{\rho_{0,j},0}(U_j)|,
\tag{25}
\]

where any

\[
0<c_\kappa<\frac{-\log q_\kappa}{\omega_\kappa}
\tag{26}
\]

is admissible after increasing the stage index.

The normalized empirical measure of the scaled offsets is supported on the vertical segment `Re lambda=0`, `0<=Im lambda<=R_j`, and its transform is

\[
Q_j(x)=2^{-j}\prod_{\ell=1}^{j}(1+e^{i\omega_{j,\ell}x}).
\tag{27}
\]

Hence

\[
\sup_{x\in I_\kappa}|Q_j(x)|
\le(q_1/2)^j
=\exp[-\Omega_\kappa(R_j)].
\tag{28}
\]

So the `exp(-O(R))` functional order in `RE-145/148` is already sharp inside a purely vertical positive-measure model, on the one-sided observation interval where the product is controlled.

Because `W(U)->infinity`, the phases can also be enlarged until

\[
W(U_j)\ge j(1+\omega_\kappa),
\tag{29}
\]

which gives (6). The escape from every fixed reciprocal box may therefore be arbitrarily slow.

## 4. Embedding and scale-maximality

Close every stage under conjugation and `rho -> 1-rho`, and adjoin one fixed simple quartet with right member on `Re rho=Theta`. Choose the phases strongly lacunary and enlarge them recursively so that earlier stages are horizontally damped throughout the **same one-sided window**:

\[
\sum_{n<j}2^n
\frac{e^{-(1-\kappa)U_j/(2U_n^2)}}{1+\Gamma_n^2}
=o(U_j^{-A}),
\tag{30}
\]

and future stages have summable coefficient tail

\[
\sum_{n>j}2^n U_n^{-A}=o(U_j^{-A}).
\tag{31}
\]

Equations (23), (30), and (31) prove (7), while (16)--(17) and the same tail budgets give (4). Requiring additionally `L(Gamma_j)>=2^{j+3}` gives (9).

Taking `T_j=2Gamma_j`, future stages lie above the truncation and previous stages have smaller real part. Thus for every fixed `R>0`, the shell

\[
\{\rho:0<\Im\rho\le T_j,\ \Re\rho\ge\beta_j+R/U_j\}
\tag{32}
\]

is empty for all large `j`. The cancellation is therefore neither the near-left mechanism of `RE-144` nor a sufficiently rightward shell: it is purely vertical at `beta=beta_j`.

## 5. Boundary and research effect

This remains a matched-control theorem, not a claim that the actual zeros of zeta realize the subset-product geometry. It preserves simplicity, functional-equation symmetry, an attained finite edge, the leading Robin coefficient law, an algebraically strong scale-maximal anchor, and arbitrarily sparse off-critical counting. It does not preserve an Euler product, zeta's explicit formula, GUE, determinant identities, or any target-conditioned local law capable of forbidding the packet.

The adversarial correction is equally important: this construction supplies no symmetric-window no-go for `|u-U_j|<=kappa U_j`. The equal-amplitude single factor (11) is controlled only on `[1-kappa,1]`; for the upper half a different phase construction would be needed. Downstream arguments may use (7)--(8) only with the one-sided window.

Within that corrected scope, the conclusion is decisive: **zero horizontal spread does not force visibility**. Any actual-zeta closure of the early-window splice must control vertical occupancy/phase geometry or invoke source information absent from the positive-measure model.