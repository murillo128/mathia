# WI-094 — Extensive prime rank-defect edges have vanishing dyadic cumulative coherence

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion, does not certify the Yang--Yang one-sided fourth-moment candidate, and does not turn the scalar Ramanujan reduction into the full locked four-prime covariance. It resolves the specific collective escape left open by WI-093 at the Hilbert--Schmidt level: on one dyadic prime scale, even allowing **all** positive-density rank-defect pairs to contribute with adversarial signs, their cumulative pairwise Frobenius coupling is only `O_theta(1/log P)` of the diagonal block energy. Thus macroscopic pairwise rank defect cannot become a macroscopic cancellation resource merely by summing over all primes of comparable size.

Fix `theta>0` and `P>2`. Let `S` be any finite set of primes in `[P,2P]`, let `N>=1` be the common observation length, and for `p in S` write

\[
B_p^{(N)}=U_p^{(N)}(U_p^{(N)})^*
=(c_p(i-j))_{0\le i,j<N}.
\tag{1}
\]

For a pair `p<q` in `S`, let `delta=delta_N(p,q)` be the nearest-`pq` boundary length. When the pair lies in the WI-088/WI-093 residual regime `delta>q-1`, define

\[
\tau_{p,q}
=(p-1)-\operatorname{rank}((U_p^{(N)})^*U_q^{(N)}).
\tag{2}
\]

Call the pair **theta-extensive** when

\[
\tau_{p,q}\ge \theta p.
\tag{3}
\]

Let `E_theta` be any collection of such pairs. Then every edge obeys the finite normalized Frobenius-coherence bound

\[
\boxed{
\frac{\operatorname{tr}(B_p^{(N)}B_q^{(N)})}
{\|B_p^{(N)}\|_F\,\|B_q^{(N)}\|_F}
<\frac{4}{\theta(p-1)}
\le \frac{4}{\theta(P-1)}.
}
\tag{4}
\]

The same bound holds for the Frobenius-normalized orthogonal projectors onto the two sampled primitive-frequency subspaces.

Consequently, for **arbitrary real source weights** `omega_p`, put

\[
\mathcal D
:=\sum_{p\in S}\omega_p^2\|B_p^{(N)}\|_F^2
\tag{5}
\]

and isolate the cross term carried by the extensive-defect edges,

\[
\mathcal C_\theta
:=2\sum_{\{p,q\}\in E_\theta}
\omega_p\omega_q\operatorname{tr}(B_p^{(N)}B_q^{(N)}).
\tag{6}
\]

If `M=|S|`, then

\[
\boxed{
|\mathcal C_\theta|
\le
\frac{4(M-1)}{\theta(P-1)}\,\mathcal D.
}
\tag{7}
\]

Since the classical prime-counting bound gives

\[
M\le \pi(2P)-\pi(P)\ll \frac{P}{\log P},
\tag{8}
\]

we obtain uniformly in `N`, in the chosen prime subset, in the edge set, and in the real weights,

\[
\boxed{
|\mathcal C_\theta|
=O_\theta\!\left(\frac{\mathcal D}{\log P}\right).
}
\tag{9}
\]

In particular, if a signed dyadic prime operator has a fixed-fraction Frobenius cancellation

\[
\left\|\sum_{p\in S}\omega_pB_p^{(N)}\right\|_F^2
\le (1-c)\mathcal D
\qquad(c>0\text{ fixed}),
\tag{10}
\]

then, for every fixed `theta>0`, the net cross term from pairs **outside** `E_theta` must contribute

\[
\le -(c-o_\theta(1))\mathcal D.
\tag{11}
\]

So any fixed-fraction Hilbert--Schmidt cancellation must asymptotically be carried by pairs with vanishing defect density, non-residual/full-rank pairs, cross-scale interactions, or information beyond the scalar pairwise Ramanujan blocks. Positive-density defect edges themselves wash out after dyadic aggregation.

## 1. WI-093 converts defect density into a long boundary

Take one theta-extensive edge `p<q`. WI-093 writes

\[
\delta=kq+s,
\qquad 0\le s<q,
\tag{12}
\]

and proves the exact arithmetic implication

\[
\boxed{k\ge \tau_{p,q}+1.}
\tag{13}
\]

Because `tau_{p,q}>=theta p`, equation (13) gives

\[
k>\theta p.
\tag{14}
\]

This is the essential arithmetic input. A positive-density rank defect can occur only after the nearest boundary has traversed a positive fraction of the joint prime period. WI-093 used this to show bounded **whitened** canonical overlap for one pair. Here the same boundary length is fed into the raw Frobenius normalization needed for a signed scalar-block aggregation.

## 2. One extensive-defect edge has `O_theta(1/P)` normalized raw overlap

Put

\[
G_{p,q}^{(N)}=(U_p^{(N)})^*U_q^{(N)}.
\tag{15}
\]

For positive semidefinite Gram blocks,

\[
\operatorname{tr}(B_p^{(N)}B_q^{(N)})
=\|G_{p,q}^{(N)}\|_F^2.
\tag{16}
\]

WI-092--WI-093 prove that complete `pq` periods cancel from this cross Gram up to the harmless complementary-boundary phase convention, and that on the nearest boundary

\[
\boxed{
\|G_{p,q}^{(N)}\|_F^2
\le pq\delta.
}
\tag{17}
\]

The same findings give the exact residue-count frame lower bounds. Set

\[
a=\left\lfloor\frac\delta p\right\rfloor,
\qquad
k=\left\lfloor\frac\delta q\right\rfloor.
\tag{18}
\]

Since `N>=delta`,

\[
\begin{aligned}
\|B_p^{(N)}\|_F
&\ge p\,a\sqrt{p-1},\\
\|B_q^{(N)}\|_F
&\ge q\,k\sqrt{q-1}.
\end{aligned}
\tag{19}
\]

As `q>p`, one has `a>=k`. Also `delta<(k+1)q`. Combining (17)--(19),

\[
\begin{aligned}
\mu_{p,q}
&:=
\frac{\operatorname{tr}(B_p^{(N)}B_q^{(N)})}
{\|B_p^{(N)}\|_F\,\|B_q^{(N)}\|_F}\\
&\le
\frac{\delta}{ak\sqrt{(p-1)(q-1)}}\\
&<
\frac{q(k+1)}{k^2\sqrt{(p-1)(q-1)}}.
\end{aligned}
\tag{20}
\]

Because both primes lie in one dyadic interval, `p<q<2p`, and therefore

\[
\sqrt{(p-1)(q-1)}>p-1,
\qquad q<2p.
\tag{21}
\]

For `k>=1`, `(k+1)/k^2<=2/k`; using (14),

\[
\mu_{p,q}
<\frac{4p}{k(p-1)}
<\frac{4}{\theta(p-1)},
\tag{22}
\]

which is (4).

There is a parallel whitened statement. WI-093 proves

\[
\operatorname{tr}(\Pi_p\Pi_q)
<q\frac{\tau+2}{(\tau+1)^2}.
\tag{23}
\]

Since `\|\Pi_p\|_F=\sqrt{p-1}` and `\|\Pi_q\|_F=\sqrt{q-1}`, the same elementary estimates give

\[
\frac{\operatorname{tr}(\Pi_p\Pi_q)}
{\|\Pi_p\|_F\|\Pi_q\|_F}
<\frac{4}{\theta(p-1)}.
\tag{24}
\]

Thus positive-density rank-defect pairs are not merely bounded in total canonical overlap as in WI-093; when each whole block is normalized as one Hilbert--Schmidt atom, their mutual coherence is `O_theta(P^{-1})`.

## 3. Prime sparsity makes the cumulative extensive-defect coherence vanish

Normalize each raw block in the Hilbert space of `N x N` matrices with Frobenius inner product:

\[
C_p=\frac{B_p^{(N)}}{\|B_p^{(N)}\|_F},
\qquad
x_p=\omega_p\|B_p^{(N)}\|_F.
\tag{25}
\]

Then `\|C_p\|_F=1`, `\mathcal D=\sum_p x_p^2`, and (6) becomes

\[
\mathcal C_\theta
=2\sum_{\{p,q\}\in E_\theta}
x_px_q\langle C_p,C_q\rangle_F.
\tag{26}
\]

Using (4) and `2|xy|<=x^2+y^2`,

\[
\begin{aligned}
|\mathcal C_\theta|
&\le
\frac{8}{\theta(P-1)}
\sum_{\{p,q\}\in E_\theta}|x_px_q|\\
&\le
\frac{4}{\theta(P-1)}
\sum_{\{p,q\}\in E_\theta}(x_p^2+x_q^2)\\
&=
\frac{4}{\theta(P-1)}
\sum_{p\in S}\deg_{E_\theta}(p)x_p^2\\
&\le
\frac{4(M-1)}{\theta(P-1)}\mathcal D.
\end{aligned}
\tag{27}
\]

This proves (7). Nothing about the weights was used beyond reality; they may have arbitrary sizes and signs. Nothing about the incidence graph was used beyond the trivial degree ceiling `M-1`.

The last step is arithmetic sparsity of the available moduli. The classical estimate `pi(x) << x/log x` implies (8), hence (9). In cumulative-coherence language, the individual `O_theta(P^{-1})` interaction is multiplied by only `O(P/log P)` possible dyadic prime atoms, leaving a vanishing `O_theta(1/log P)` budget.

The argument is deliberately stronger than a source-weight average. It survives adversarial reweighting and even the pessimistic assumption that **every available dyadic prime pair** is an extensive-defect edge.

## 4. Consequence for signed cancellation

Write the full Frobenius expansion as

\[
\left\|\sum_{p\in S}\omega_pB_p^{(N)}\right\|_F^2
=\mathcal D+\mathcal C_\theta+\mathcal C_{<\theta},
\tag{28}
\]

where `\mathcal C_{<\theta}` contains every pair not in `E_theta`: small-defect residual pairs, zero-defect/full-rank pairs, and any pair outside the residual defect regime.

If (10) holds, then

\[
\begin{aligned}
\mathcal C_{<\theta}
&\le -c\mathcal D-\mathcal C_\theta\\
&\le -c\mathcal D+|\mathcal C_\theta|\\
&=-(c-o_\theta(1))\mathcal D,
\end{aligned}
\tag{29}
\]

which proves (11).

This gives a clean separation that WI-093 did not yet have. WI-093 left open the possibility that many individually weak positive-density-defect pairs might accumulate into a macroscopic cancellation. Equation (29) closes exactly that possibility on a dyadic prime scale **in Frobenius energy**. The pairwise-rank-defect sector can contribute only a vanishing fraction of the cancellation ledger.

Equivalently, if a dyadic family is such that every interacting pair belongs to `E_theta`, then

\[
\boxed{
\left\|\sum_{p\in S}\omega_pB_p^{(N)}\right\|_F^2
\ge
\left(1-O_\theta\!\left(\frac1{\log P}\right)\right)
\sum_{p\in S}\omega_p^2\|B_p^{(N)}\|_F^2.
}
\tag{30}
\]

So a whole positive-density-defect cluster is asymptotically Riesz-like when its blocks are viewed as Hilbert--Schmidt atoms, despite the large rank losses inside each pairwise cross Gram.

## 5. Near-sharp WI-091 edges are even more negligible

WI-091 proves that, at fixed `N`, a near-sharp one-third defect graph with integer tolerance `D_0` satisfying its gap condition has

\[
\deg_N(p)\le 8D_0+4.
\tag{31}
\]

Whenever such an edge family also satisfies the fixed density condition `tau>=theta p`, equation (27) may use (31) instead of the trivial degree `M-1`. Therefore

\[
\boxed{
|\mathcal C_{\theta,\mathrm{near\text{-}sharp}}|
\le
\frac{4(8D_0+4)}{\theta(P-1)}\mathcal D
=O_{\theta,D_0}(P^{-1})\mathcal D.
}
\tag{32}
\]

Thus the exact/near-exact one-third layer is doubly suppressed: WI-091 makes its incidence bounded, while WI-092--WI-093 make each surviving metric coupling `O(P^{-1})` after block normalization.

## 6. Relation to WI-083 and the live Yang interface

The result does **not** contradict WI-083's exact saturated cancellation. WI-083 uses primes larger than the sample window, where

\[
B_p^{(N)}=pI_N-J_N
\]

and three freely weighted prime blocks can cancel identically. Those pairs are precisely outside the positive-density residual-defect mechanism studied here: the short window has not entered the long boundary regime forced by (13). The two findings therefore fit together:

\[
\boxed{
\begin{array}{ll}
\tau/p\ge\theta>0
&\Longrightarrow\text{ dyadic rank-defect cross energy is cumulatively negligible},\\
\text{short/full-rank saturated regime}
&\Longrightarrow\text{ exact scalar cancellation can occur.}
\end{array}}
\tag{33}
\]

This materially redirects the scalar search. Further optimization of the **size** of the residual prime rank defect cannot explain a macroscopic signed cancellation, even collectively across all comparable primes. Any source-faithful scalar cancellation must instead exploit the low-/zero-defect regime, cross-scale structure, the exact Yang coefficient law, or labels discarded by scalarization. The original locked-covariance clue remains open because Mathia has not proved that the full post-local-main Yang object is exhausted by the scalar block model.

## 7. Prior art and novelty boundary

The aggregation step is standard Hilbert-space coherence logic, not a new general theorem. Joel A. Tropp's **Greed is Good: Algorithmic Results for Sparse Approximation**, *IEEE Transactions on Information Theory* 50:10 (2004), 2231--2242, DOI `10.1109/TIT.2004.834793`, introduced cumulative coherence/Babel-function methods for controlling the accumulation of pairwise inner products in normalized dictionaries. Fusion-frame literature likewise treats `tr(P_iP_j)` as the natural pairwise subspace-overlap/chordal-distance quantity; see Gitta Kutyniok, Ali Pezeshki, Robert Calderbank and Taotao Liu, **Robust Dimension Reduction, Fusion Frames, and Grassmannian Packings**, *Applied and Computational Harmonic Analysis* 26 (2009), DOI `10.1016/j.acha.2008.09.001`. Ramanujan subspaces and their finite-duration near-orthogonality are already anchored in `SOURCES.md` through Vaidyanathan--Tenneti.

A targeted prior-art search found these standard coherence/fusion-frame frameworks but no source coupling them to the WI-088 arithmetic defect density, the WI-093 boundary quotient `k>=tau+1`, and dyadic prime sparsity to obtain (9). **No priority claim is made.** The durable Mathia content is the arithmetic application: the exact WI-093 rank-defect mechanism supplies `O(P^{-1})` Hilbert--Schmidt coherence, and the fact that there are only `O(P/log P)` comparable prime moduli prevents collective recovery of a constant cancellation fraction.

No `SOURCES.md` change is required for the proof: Tropp/fusion-frame language is contextual prior art, while every load-bearing matrix identity is proved above or inherited from WI-091--WI-093, and the only new external asymptotic input is the classical elementary prime-counting upper bound `pi(x)<<x/log x`.

## 8. Falsification and boundary conditions

1. **Frobenius cancellation only.** Equations (7)--(11) control the Hilbert--Schmidt energy ledger. They do not by themselves give a source-normalized operator-norm or inertia bound; small pairwise Frobenius contribution must not be silently promoted to spectral-sign rigidity.
2. **Positive-density defect is essential.** If `tau=o(p)`, the factor `k` need not be `Omega(p)` and (4) need not be `O(P^{-1})`. This is exactly the remaining regime singled out by (11).
3. **One dyadic prime scale.** Cross-scale prime pairs require a separate multiscale summation. The present result prevents accumulation within each comparable-prime band; it does not assert that summing infinitely many bands is harmless under arbitrary source weights.
4. **Prime residual theorem.** The implication `k>=tau+1` is WI-093's prime partial-cycle result. Composite moduli can have different rank and period geometry.
5. **The scalar block is an information quotient.** The Yang clue is a locked four-prime covariance with direction, residue, collision, and local-main labels. WI-079 explicitly warns that an exact reduction of the whole source object to (1) has not been proved. This finding narrows only the scalar pairwise-rank route.
6. **No contradiction with exact overcomplete cancellation.** WI-083 lives in the low-boundary/full-rank regime deliberately excluded by (3). Its exact zero operator is a necessary control showing why the `theta>0` hypothesis cannot simply be dropped.
7. **Prime sparsity, not weight regularity, supplies the accumulation saving.** The weights in (7) are arbitrary. If a future source reduction contains many repeated copies or additional labels per prime modulus, those labels cannot be merged into the present `M=O(P/log P)` count without proving that the merge preserves the relevant Frobenius atom.

## 9. Program consequence

The pairwise prime-rank branch now has a collective endpoint:

\[
\boxed{
\text{positive-density rank defect}
\Longrightarrow
O(P^{-1})\text{ pair coherence}
\Longrightarrow
O((\log P)^{-1})\text{ total dyadic coherence}.
}
\tag{34}
\]

The first arrow is arithmetic (`WI-093`); the second uses only dyadic prime sparsity and cumulative-coherence algebra. Hence the unresolved sentence at the end of WI-093 can be narrowed: **many weak couplings from the extensive-defect sector cannot coherently accumulate to a fixed fraction of the scalar Hilbert--Schmidt energy, even under adversarial real weights.**

The next source-faithful question is therefore not another optimization of `tau`. It is whether the actual Yang coefficient law creates cancellation through the complementary low-/zero-defect or cross-scale pairs, or whether the full locked four-prime representation retains additional orthogonality that kills those sectors as well. That is the remaining many-modulus/operator problem.