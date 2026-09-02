# WI-107 — Sub-square-root scalar multi-target aggregation stays ill-conditioned

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It closes a substantial part of the multi-target escape left open by WI-106: adding any fixed number of full-packed target blocks, or even a growing number below the square-root scale, still cannot produce a uniformly conditioned source-spanning concatenation if one is allowed only one scalar weight per target block.

More precisely, let `J=J(p)>=2` be integer-valued along source primes and suppose

\[
J=o\!\left(\sqrt{\frac{p}{\log p}}\right).
\tag{1}
\]

There are infinitely many source primes `p`, `J` distinct target primes

\[
p<q_1<\cdots<q_J<\frac{4p}{3},
\tag{2}
\]

and one common observation length `N` such that every `(p,q_j,N)` is in the positive-defect exact full-packing regime of WI-096/WI-102/WI-104. Put

\[
G_j=(U_p^{(N)})^*U_{q_j}^{(N)},
\qquad
K_j=\ker G_j^*\subset\mathbf C^{p-1},
\tag{3}
\]

and, for arbitrary complex scalar weights `a_j`, form

\[
B=[\,a_1G_1\;\cdots\;a_JG_J\,].
\tag{4}
\]

The targets can be chosen with total span

\[
\Delta:=q_J-q_1=O(J\log p).
\tag{5}
\]

If at least two weights are nonzero, `B` has full source row rank by pairwise application of WI-104, but nevertheless

\[
\boxed{
\frac{\sigma_{\min}(B)}{\sigma_{\max}(B)}
\le
\sqrt{\frac{3(J-1)\Delta}{2p}}.
}
\tag{6}
\]

Consequently, uniformly over **every** scalar weighting rule,

\[
\boxed{
\kappa_2(B)
=\Omega\!\left(
\frac1J\sqrt{\frac{p}{\log p}}
\right)
\longrightarrow\infty.
}
\tag{7}
\]

If fewer than two weights are nonzero, the concatenation is source-rank deficient because each individual positive-defect block has a nontrivial left kernel, so its condition number is infinite in the extended sense.

Thus the two-target obstruction of WI-106 is not a peculiarity of using exactly two blocks. **Every fixed target count fails, and so does every target count `J=o(sqrt(p/log p))`.** This does not say that `J` of order `sqrt(p/log p)` suffices; it only identifies the first scale not ruled out by this counterfamily.

## 1. A multi-block common-near-kernel lemma

The operator estimate is elementary. Let

\[
A_j:H_j\to H,
\qquad
K_j=\ker A_j^*\subset H
\qquad(1\le j\le J)
\tag{8}
\]

be finite-dimensional operators. Suppose unit vectors `x_j in K_j` have been chosen and write

\[
\delta_{ij}:=\operatorname{dist}(x_i,K_j).
\tag{9}
\]

For arbitrary scalar weights `a_j`, put

\[
B=[\,a_1A_1\;\cdots\;a_JA_J\,],
\qquad
b_j:=|a_j|\,\|A_j\|_2.
\tag{10}
\]

Choose an index `i_*` with

\[
b_{i_*}=\max_j b_j.
\tag{11}
\]

Take `x=x_{i_*}`. Since `A_{i_*}^*x=0`, and since `A_j^*` annihilates the orthogonal projection of `x` onto `K_j`,

\[
\begin{aligned}
\|B^*x\|^2
&=\sum_{j\ne i_*}|a_j|^2\|A_j^*x\|^2\\
&\le\sum_{j\ne i_*}b_j^2\,\delta_{i_*j}^2\\
&\le b_{i_*}^2
\sum_{j\ne i_*}\delta_{i_*j}^2.
\end{aligned}
\tag{12}
\]

On the other hand

\[
\sigma_{\max}(B)=\|B\|_2\ge b_{i_*}.
\tag{13}
\]

Whenever `B` has full row rank, the variational characterization of its smallest singular value therefore gives

\[
\boxed{
\frac{\sigma_{\min}(B)}{\sigma_{\max}(B)}
\le
\left(
\sum_{j\ne i_*}\delta_{i_*j}^2
\right)^{1/2}.
}
\tag{14}
\]

This is the multi-block replacement for the two-subspace `csc(theta)` estimate in WI-106. The important point is that the maximizing weight index `i_*` is chosen **after** the scalar weights are given. A counterfamily therefore needs one kernel witness near every other kernel, not merely one pair of almost-parallel kernels.

## 2. A clustered modulus-three family supplies arbitrarily many common near-kernels

Take source primes

\[
p\equiv1\pmod3.
\tag{15}
\]

For every sufficiently large such `p`, the prime number theorem in arithmetic progressions for the fixed modulus `3`, already used in WI-105, gives

\[
M_p
:=\#\left\{q:\ p<q<\frac{4p}{3},\ q\equiv2\pmod3\right\}
\sim\frac{p}{6\log p}.
\tag{16}
\]

Order these targets as `Q_1<...<Q_{M_p}`. For any `J<=M_p/2`, consider the `M_p-J+1` consecutive `J`-windows. If `g_s=Q_{s+1}-Q_s`, then

\[
\sum_{r=1}^{M_p-J+1}
(Q_{r+J-1}-Q_r)
\le
(J-1)\sum_{s=1}^{M_p-1}g_s
<\frac{(J-1)p}{3}.
\tag{17}
\]

Since `M_p-J+1>=M_p/2`, at least one such window has span

\[
\boxed{
\Delta=O(J\log p).
}
\tag{18}
\]

The regime (1) is much smaller than `M_p`, so this selection is available for all sufficiently large `p`.

Rename the primes in this window `q_1<...<q_J` and put

\[
d_j=q_j-p,
\qquad
t_j=2p-q_j=p-d_j,
\qquad h_j=\frac{d_j}{2}.
\tag{19}
\]

Because every sufficiently large source prime in (15) is `1 mod 6` and every odd target prime `q_j congruent 2 mod 3` is `5 mod 6`,

\[
d_j\equiv4\pmod6,
\qquad
h_j\equiv2\pmod3,
\qquad
3\mid t_j.
\tag{20}
\]

Also `d_J<p/3`, hence `h_J<p/6`. Choose an integer

\[
h_J<c<p-h_J,
\qquad
c\equiv2\pmod3,
\tag{21}
\]

and define

\[
\boxed{
\rho_j=c-h_j.
}
\tag{22}
\]

Then

\[
0<\rho_j<t_j,
\qquad
3\mid\rho_j,
\qquad
\gcd(\rho_j,t_j)\ge3.
\tag{23}
\]

Thus every target lies in the genuinely positive-defect full-packing chart, and the deleted intervals have the same center `c`.

## 3. One actual observation length realizes all targets simultaneously

For each `j`, choose the unique `k_j in {0,...,p-1}` with

\[
k_jd_j\equiv\rho_j\pmod p
\tag{24}
\]

and set

\[
r_j=k_jq_j+d_j+\rho_j.
\tag{25}
\]

Exactly as in WI-105,

\[
r_j\equiv2\rho_j+d_j=2c\pmod p.
\tag{26}
\]

The moduli `pq_j` have pairwise greatest common divisor `p`, and all residues `r_j` agree modulo `p`. The generalized Chinese remainder theorem therefore gives a single integer `N` such that

\[
\boxed{
N\equiv r_j\pmod{pq_j}
\qquad(1\le j\le J).
}
\tag{27}
\]

The nearest-boundary sign can differ from target to target. This does not disturb the geometry: WI-105 checked the complementary chart exactly and WI-104's source-side phase correction sends it back to the same **actual** deleted-interval start `rho_j`. Hence all `J` full-packed kernels may be compared in one common source coordinate system.

Their exterior intervals are

\[
I_j=[\rho_j-t_j,\rho_j-1],
\qquad |I_j|=t_j.
\tag{28}
\]

Because the deleted holes are concentric and `q_1<...<q_J`, these exterior intervals are nested. Since `3|gcd(rho_j,t_j)`, every kernel contains the same order-three quotient-character pattern on its own support:

\[
f_j(w)=e(w/3)\quad(w\in I_j),
\qquad
f_j=0\quad\text{on the hole}.
\tag{29}
\]

WI-105's Parseval normalization identifies these residue functions with actual unit source-kernel vectors after division by `sqrt(t_j)`. Write the normalized vectors as `x_j in K_j`. For every pair,

\[
\boxed{
|\langle x_i,x_j\rangle|^2
=\frac{\min(t_i,t_j)}{\max(t_i,t_j)}.
}
\tag{30}
\]

Therefore

\[
\begin{aligned}
\operatorname{dist}(x_i,K_j)^2
&\le1-|\langle x_i,x_j\rangle|^2\\
&=\frac{|t_i-t_j|}{\max(t_i,t_j)}\\
&=\frac{|q_i-q_j|}{\max(t_i,t_j)}\\
&\le\frac{3\Delta}{2p},
\end{aligned}
\tag{31}
\]

because every `q_j<4p/3` gives `t_j>2p/3`.

## 4. Scalar conditioning fails below the square-root target-count scale

Apply the general lemma (14) to `A_j=G_j`. For the weight-maximizing index `i_*`, equation (31) gives

\[
\sum_{j\ne i_*}
\delta_{i_*j}^2
\le
\frac{3(J-1)\Delta}{2p}.
\tag{32}
\]

If at least two scalar weights are nonzero, select any two such blocks. WI-104 says their left kernels have trivial intersection, so those two blocks already span the full source row space; adding more blocks preserves full row rank. Hence (14) applies and proves (6).

Combining (6) with the clustered-prime span (18),

\[
\frac{\sigma_{\min}(B)}{\sigma_{\max}(B)}
=O\!\left(J\sqrt{\frac{\log p}{p}}\right),
\tag{33}
\]

uniformly in all scalar weights. Under (1) the right-hand side tends to zero, proving (7).

For fixed `J`, this specializes to the same `Omega(sqrt(p/log p))` divergence scale as WI-106 up to a `J`-dependent constant. The new content is that the obstruction survives a growing number of simultaneously realized targets and degrades only linearly in `J` under the present estimate.

## 5. Stress tests and sharp boundary of the claim

The first important stress test is logical: WI-106 alone does **not** imply this result. Extra blocks can increase the smallest singular value of a horizontal concatenation, so a bad pair need not obstruct a larger family. Equation (14) works because the arithmetic construction supplies a vector in the kernel of the largest weighted block that is simultaneously close to the kernels of **all** other blocks.

The second stress test is the target-count dependence. The proof gives only

\[
O\!\left(J\sqrt{\frac{\log p}{p}}\right)
\tag{34}
\]

for the relative gap. At `J` comparable to `sqrt(p/log p)`, this ceases to force degeneration. No sufficiency statement is made at or above that scale.

The third boundary is the weighting model. The theorem permits arbitrary complex `a_j`, with unrestricted dependence on all arithmetic data, but each `a_j` is one scalar multiplying an intact target block. Non-scalar diagonal weights, internal operator preconditioners, row/column-dependent weights, or a source normalization tied to additional analytic information are outside the claim.

Finally, the construction is a finite-window structural counterfamily. The generalized CRT may produce a very large common `N`; no claim is made that these windows occur with positive analytic density in the zeta problem. The conclusion is therefore a **uniform-coercivity no-go** for the full-packed algebraic interface, not a new asymptotic statement about zeta zeros.

## 6. Prior art, novelty boundary, and program consequence

The linear-algebra ingredients are classical. WI-105 already anchored the principal-angle formalism of Björck--Golub, and WI-106 anchored Demmel's classical relationship between small subspace angles and bad conditioning. A targeted audit around weighted fusion frames, multi-subspace analysis operators, sums of projections, principal angles, and block conditioning found the standard multi-subspace framework but no result that supplies the arithmetic construction above or a uniform scalar rescue from it. That negative search is **not** a priority claim.

Likewise, the prime input is not new: the only distribution theorem used is the fixed-modulus prime number theorem in arithmetic progressions already used in WI-105. The new exact deduction is the combination of a short `J`-prime window, one generalized-CRT full-packing realization, the common order-three quotient character, and the multi-block near-kernel estimate.

This materially narrows the escape left by WI-106. A proposed rescue based only on adding three, ten, or any other fixed number of scalar-weighted target blocks is now closed; more generally, so is every sub-square-root count in (1). To evade this counterfamily while retaining full packing, a scalar-only construction would need at least order `sqrt(p/log p)` genuinely distinct target blocks **as far as this obstruction can see**, or else it must use information that the theorem deliberately discards: non-scalar internal weights, detailed singular-vector/singular-value structure, absolute normalization from the analytic problem, or positive slack away from exact full packing.

The decisive falsification test is explicit. Any proposed uniform relative source-coercivity theorem for `J=o(sqrt(p/log p))` intact scalar-weighted full-packed target blocks must survive the modulus-three clustered family (15)--(31). Equations (6) and (33) show that it cannot.