# PC-396 — critical Riesz Kron contrast vanishes on all polynomial windows

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `DECISIVE-NEGATIVE` for the critical positive inverse-distance (`alpha=1/2`) simultaneous-deletion Kron branch left open by PC-395.

PC-395 closes the irreducible multi-deletion correction `Delta_T` for every fixed polynomial primorial window when the local chord tail is summable, `alpha>1/2`. Its proof necessarily stops at the one-dimensional summability boundary because both the deleted-layer degree and the overlap estimate used there contain `sum h^{-2 alpha}`.

At the critical endpoint `alpha=1/2`, that harmonic divergence does **not** rescue an order-one unscaled spectral outlier. The missing compensation is already present in the same prime-circle state space: the surviving `q`-rough boundary contains every prime above `q`. On a polynomial window this macroscopic prime reservoir forces each deleted vertex to have survivor degree at least `c/log H`. After normalizing the deleted stars, the remaining logarithmic overlap is harmless against the `q`-spacing of the deleted layer.

For every fixed `u>1`, with `H=p^u`, `q` the next prime after `p`, and the normalized regularized chord kernel of PC-390--PC-395 at `alpha=1/2`, one obtains

\[
\boxed{
\|\Delta_T\|_{\rm op}
=O_{\tau,u}\!\left(\frac{\log p}{p}\right)
\longrightarrow0.
}
\tag{1}
\]

Thus the critical positive `1/|d|` tail is still too weak to preserve a nonzero unscaled simultaneous-deletion Kron contrast on **any fixed polynomial primorial window**. The nonsummable escape left by PC-395 therefore begins strictly below the critical exponent, not at it.

## 1. Exact Schur factorization and the critical kernel

Use the successive primorial notation of PC-391--PC-395. Let

\[
S=R_q(H),
\qquad
T=qR_p(H/q)=\{t_1,\ldots,t_k\}
\tag{2}
\]

be the surviving and simultaneously deleted boundary points. With survivor-to-deleted conductance matrix `B`, deleted survivor degrees

\[
d_i=\sum_{a\in S}b_{ai},
\qquad
D=\operatorname{diag}(d_i),
\tag{3}
\]

and `K` the weighted Laplacian of the graph induced on `T`, PC-394 gives the exact factorization

\[
\Delta_T=PQP^\top,
\qquad
P=BD^{-1},
\qquad
0\preceq Q\preceq K.
\tag{4}
\]

Every column of `P` is a probability vector, so

\[
\|P\|_1=1.
\tag{5}
\]

At `alpha=1/2`, the normalized regularized chord kernel is

\[
\kappa_M(d)
=M^{-1}
\left[2\left(\cosh\frac{\tau}{M}-\cos\frac{2\pi d}{M}\right)\right]^{-1/2}.
\tag{6}
\]

On every local polynomial arc `1<=d<=H=o(M)`, the two-sided estimate already used in PC-395 specializes to

\[
\boxed{
\frac{c_\tau}{d}
\le \kappa_M(d)
\le \frac{C_\tau}{d}.
}
\tag{7}
\]

The problem is therefore exactly the borderline one-dimensional Riesz tail `1/d`.

## 2. A macroscopic prime reservoir lower-bounds every deleted survivor degree

The Jacobsthal nearest-survivor estimate used in PC-395 is intentionally local. At the critical exponent it is too weak because the resulting normalized tail is harmonic. The full survivor set contains a stronger global normalization resource.

Fix `u>1` and put `H=p^u`. By Bertrand's postulate, `q<2p`, so for all sufficiently large `p`,

\[
q<\frac H2.
\tag{8}
\]

Every prime `ell` in `[H/2,H]` is then larger than `q`, hence is coprime to the primorial through `q` and belongs to `S=R_q(H)`. The classical prime number theorem gives

\[
\#\{\ell\text{ prime}:H/2\le\ell\le H\}
\asymp \frac H{\log H}.
\tag{9}
\]

For any deleted point `t_i in T subset [1,H]` and any such prime survivor `ell`,

\[
1\le |\ell-t_i|\le H.
\tag{10}
\]

Using the lower half of (7), each contributes at least `c_tau/H` to `d_i`. Therefore, uniformly in the deleted point,

\[
\boxed{
 d_i
 =\sum_{a\in S}\kappa_M(|a-t_i|)
 \gg_{\tau,u}\frac1{\log H}.
}
\tag{11}
\]

No short-interval prime theorem, Jacobsthal estimate, or cancellation is used here. A fixed macroscopic interval of ordinary prime survivors is enough.

Combining (7) and (11), for every survivor `a` and deleted point `t_i`, with `r=|a-t_i|>=1`,

\[
\boxed{
 p_{ai}=\frac{b_{ai}}{d_i}
 \ll_{\tau,u}
 \min\left\{1,\frac{\log H}{r}\right\}.
}
\tag{12}
\]

This is the critical replacement for PC-395's summable-tail Jacobsthal profile bound.

## 3. `q`-spacing keeps the normalized incidence synthesis bounded

Distinct deleted points are multiples of `q`, hence

\[
|t_i-t_j|\ge q
\qquad(i\ne j).
\tag{13}
\]

Fix a survivor `a`. For a `q`-separated set on the line, at most one deleted point can lie inside a ball of radius `O(log H)` once `q/log H -> infinity`; all remaining centers can be grouped into distance shells of width comparable to `q`. Applying (12) gives

\[
\sum_i p_{ai}
\ll_{\tau,u}
1+
\frac{\log H}{q}
\sum_{1\le m\ll H/q}\frac1m.
\tag{14}
\]

Hence

\[
\boxed{
\|P\|_\infty
\ll_{\tau,u}
1+
\frac{\log H}{q}\log\left(2+\frac Hq\right).
}
\tag{15}
\]

Together with `||P||_1=1`, the induced-norm inequality yields

\[
\boxed{
\|P\|_2^2
\le \|P\|_1\|P\|_\infty
=O_{\tau,u}(1)
}
\tag{16}
\]

on every fixed polynomial window. In fact the correction term in (15) is `O_u((log p)^2/p)`.

This is the essential compensation at criticality: the individual `1/r` tails are nonsummable, but normalization by the macroscopic survivor degree makes their collective synthesis uniformly bounded.

## 4. The deleted-layer Laplacian has only logarithmic degree growth

Write deleted points as `t_i=q r_i` with distinct integers `r_i in R_p(H/q)`. From the upper half of (7),

\[
c_{ij}
=\kappa_M(|t_i-t_j|)
\ll_\tau
\frac1{q|r_i-r_j|}.
\tag{17}
\]

For fixed `i`, there are at most two integer locations at each distance `h=|r_i-r_j|`. Therefore

\[
\sum_{j\ne i}c_{ij}
\ll_\tau
\frac1q
\sum_{1\le h\le H/q}\frac1h
\ll_\tau
\frac1q\log\left(2+\frac Hq\right).
\tag{18}
\]

A weighted graph Laplacian has operator norm at most twice its maximum weighted degree, so

\[
\boxed{
\|K\|_{\rm op}
\ll_\tau
\frac1q\log\left(2+\frac Hq\right).
}
\tag{19}
\]

This is where the critical harmonic divergence survives, but only as a logarithm.

## 5. The critical simultaneous-deletion correction still vanishes

From (4), positivity gives `||Q||_op<=||K||_op`. Hence (16) and (19) imply

\[
\|\Delta_T\|_{\rm op}
\le
\|P\|_2^2\,\|Q\|_{\rm op}
\ll_{\tau,u}
\frac1q\log\left(2+\frac Hq\right).
\tag{20}
\]

For `H=p^u` and fixed `u>1`, Bertrand's bound `p<q<2p` gives

\[
\log\left(2+\frac Hq\right)=O_u(\log p),
\tag{21}
\]

and therefore

\[
\boxed{
\|\Delta_T\|_{\rm op}
=O_{\tau,u}\!\left(\frac{\log p}{p}\right)
\to0.
}
\tag{22}
\]

When `1<u<=2`, there is eventually only the single deleted point `q`, so the simultaneous interaction correction is already exactly zero. Equation (22) supplies the genuinely multi-deletion range as well.

By Weyl's inequality, every ordered eigenvalue of the true simultaneous Kron response differs from the independent-star baseline by `o(1)`. Thus no fixed polynomial window produces a persistent **unscaled** exceptional eigenvalue from the irreducible deleted-layer interaction at the critical `1/d` tail.

## 6. Prior-art and novelty audit

The abstract ingredients are classical. Dörfler--Bullo, already anchored in `SOURCES.md`, covers graph-Laplacian Kron reduction and Schur complementation. The prime-number theorem and Bertrand's postulate are classical distribution results, and the harmonic-series estimate and induced matrix-norm inequality are elementary.

A targeted prior-art search also finds the classical Riesz-energy literature for equally spaced roots of unity, notably Brauchart--Hardin--Saff, *The Riesz energy of the Nth roots of unity: an asymptotic expansion for large N* (Bull. London Math. Soc. 41 (2009), 621--633, DOI `10.1112/blms/bdp034`, arXiv:0808.1291). That work shows that scalar Riesz energies of roots of unity have classical zeta-bearing asymptotics. It does not supply the primorial rough-boundary Schur/Kron estimate above, and no novelty is claimed for Riesz asymptotics themselves.

Targeted searches for combinations of Kron reduction, Riesz/inverse-distance graph kernels, rough-number or primorial boundaries, and sieve structure did not locate an established theorem matching (11)--(22). Absence from search is not a novelty proof. The durable project-specific delta is narrower: **the exact prime-circle survivor set itself supplies enough normalization to close the `alpha=1/2` unscaled Kron-outlier loophole left explicitly open by PC-395**.

This result does not recover a zeta function or critical-line criterion. On the contrary, it removes another route by which a positive source-forced boundary interaction might have retained order-one spectral information.

## 7. Boundary and falsification tests

The proof uses positivity, the exact Schur factorization of PC-391/PC-394, the local-arc comparison `kappa_M(d)asymp1/d`, and the fact that **all** primes above `q` survive the primorial sieve. It concerns fixed polynomial windows and an unscaled operator norm.

It does not cover:

- slower tails `alpha<1/2`;
- a diverging renormalization that is independently forced by the source geometry;
- signed or indefinite kernels;
- nonlinear elimination or observables not exhausted by the positive Schur response;
- cross-level orientation/evolution of the thin contrast subspaces.

The estimate is directly falsifiable. At finite `p`, construct `S,T,B,D,K`, form `P=BD^{-1}` and `Q=D-D(D+K)^{-1}D`, and compare `||Delta_T||` with `||P||_2^2||K||`. Asymptotically, a counterexample would require failure of at least one of: the survivor-degree lower bound (11), the `q`-spaced row-overlap estimate (15), or the deleted-layer degree estimate (19).

## Consequence for the research line

PC-395 identified `alpha<=1/2` as the remaining positive nonsummable-tail regime. The endpoint is now closed: for `alpha=1/2`, every fixed polynomial primorial window still has

\[
\|\Delta_T\|_{\rm op}\to0.
\]

Accordingly, merely tuning the positive inverse-power chord interaction to its one-dimensional summability threshold does not create a new spectral carrier. Any surviving positive-tail investigation must move to `alpha<1/2` or change the observable through a source-justified renormalization or cross-level structure; signed/indefinite and nonlinear mechanisms remain logically distinct.