# PC-223 — repeated Mangoldt-axis words are blind to middle-conductor data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most canonical repeated-mask escape left explicitly open by PC-222: keep the common-anchor Mangoldt selector between successive cyclotomic masks so that distinct prime-primary axes can interact noncommutatively before returning to the top primitive sector.

The repeated words are genuinely noncommutative, but they still pass through a fixed thin state space and sample only a sparse set of conductor orders. Let `N` be squarefree, let `P_d` be the exact-order Fourier projector in `H_N=L^2(Z/NZ)`, put

\[
P:=P_N,
\qquad
\mathcal A_N:=\sum_{p\mid N}(\log p)P_p,
\]

and let `M_h` denote multiplication by a real mask `h`. Define

\[
\boxed{
W_{N,r}(h)
:=P M_h\mathcal A_N(M_h\mathcal A_N)^rM_hP,
\qquad r\ge0.
}
\tag{1}
\]

These are exactly the finite-depth words which start in the top exact-order sector, enter a prime-primary axis selected by the common-anchor von Mangoldt observable, undergo `r` further mask-mediated prime-axis transitions, and return to the top sector.

For every depth `r`, the whole operator (1) depends on the Fourier transform of `h` only at conductor orders in

\[
\boxed{
\Sigma_N
=
\{1,N\}
\cup\{p:p\mid N\}
\cup\{pq:p,q\mid N,\ p\ne q\}
\cup\{N/p:p\mid N\}.
}
\tag{2}
\]

For the source cyclotomic mask `g_N`, the order-`N` coefficients vanish, so even that component drops out. No increase in depth enlarges `Sigma_N`.

Consequently, once `omega(N)>=5`, the repeated Mangoldt-axis family is **exactly blind** to every Fourier conductor `d|N` with

\[
3\le\omega(d)\le\omega(N)-2.
\tag{3}
\]

Those are genuine mixed-conductor sectors of the growing locality carrier isolated by PC-215. One can alter them while preserving the normalization and every operator `W_{N,r}` at every depth. Thus the noncommuting prime-axis geometry left open by PC-222 does not recover the middle of the mixed-conductor lattice; it factors through a strict source quotient.

There is a second independent obstruction. Every word (1) factors through

\[
\mathcal K_N:=\operatorname{Ran}\mathcal A_N
=\bigoplus_{p\mid N}E_p,
\]

so

\[
\boxed{
\operatorname{rank}W_{N,r}(h)
\le
R_N:=\sum_{p\mid N}(p-1)
}
\tag{4}
\]

for every mask and every depth. Along squarefree levels with a growing number of prime factors, `R_N/phi(N)` tends rapidly to zero. Therefore the full determinant on `E_N` is identically zero once `R_N<phi(N)`, and any uniformly bounded normalization has an empirical spectral measure asymptotically concentrated at zero along odd primorials.

This is not a no-go for every cross-level Prime-Circle construction. It closes the specific, source-forced family obtained by repeatedly inserting the **scalar common-anchor Mangoldt selector** between masks. A survivor must avoid repeatedly collapsing back to the prime-primary axes—for example by retaining mixed-conductor sectors themselves, using a refinement map that transports them across levels, or introducing another intrinsic operator whose intermediate state space grows with the mixed conductor lattice.

## 1. Exact-order difference lemma

For `k in Z/NZ`, write

\[
\operatorname{ord}_N(k)=\frac{N}{\gcd(k,N)}.
\tag{5}
\]

Because `N` is squarefree, CRT identifies a frequency with its coordinates modulo the primes dividing `N`, and its additive order is the product of the primes on which that coordinate is nonzero.

A frequency in `E_N` is a unit modulo `N`, hence is nonzero in every CRT coordinate. A frequency in `E_p` is nonzero only in its `p` coordinate. Therefore, if `alpha in E_p` and `beta in E_N`, then

\[
\boxed{
\operatorname{ord}_N(\alpha-\beta)
\in\{N/p,N\}.
}
\tag{6}
\]

The first case occurs exactly when the `p` coordinates agree; otherwise every coordinate of `alpha-beta` is nonzero.

Likewise, if `alpha in E_p` and `beta in E_q`, then

\[
\boxed{
\operatorname{ord}_N(\alpha-\beta)
\in
\begin{cases}
\{1,p\},&p=q,\\
\{pq\},&p\ne q.
\end{cases}
}
\tag{7}
\]

These elementary CRT facts are the whole conductor-support mechanism behind (2).

With normalized Fourier basis vectors `e_alpha`, multiplication satisfies

\[
\langle e_\alpha,M_he_\beta\rangle
=\widehat h(\alpha-\beta).
\tag{8}
\]

Equations (6)--(8) therefore say that top-to-prime blocks can see only orders `N/p` and `N`, while prime-to-prime blocks can see only orders `1`, `p`, and `pq`.

For the cyclotomic coefficient mask of PC-212/PC-215,

\[
\widehat g_N(k)
=\frac{\Phi_N(\zeta_N^{-k})}{\sqrt{Nh_N}},
\tag{9}
\]

and the primitive roots are exactly the zeros of `Phi_N`; hence

\[
\widehat g_N(k)=0
\iff \operatorname{ord}_N(k)=N.
\tag{10}
\]

So the `N` part of (6) is absent for the actual Prime-Circle source mask.

## 2. Every repeated word is a finite-state moment of the prime-axis compression

Since `mathcal A_N` is positive, define

\[
J_N(h):=\mathcal A_N^{1/2}M_hP:
E_N\longrightarrow\mathcal K_N
\tag{11}
\]

and

\[
B_N(h):=
\mathcal A_N^{1/2}M_h\mathcal A_N^{1/2}
\quad\text{on }\mathcal K_N.
\tag{12}
\]

Because `M_h` is self-adjoint for real `h`, `B_N(h)` is self-adjoint. Direct multiplication gives the exact factorization

\[
\boxed{
W_{N,r}(h)=J_N(h)^*B_N(h)^rJ_N(h).
}
\tag{13}
\]

Thus arbitrary depth does not create an expanding conductor state space. It only takes successive moments of the single operator `B_N(h)` on

\[
\dim\mathcal K_N
=\sum_{p\mid N}\dim E_p
=\sum_{p\mid N}(p-1)=R_N.
\tag{14}
\]

Equation (4) follows immediately. More generally, whenever a scalar function `F(B_N)` is defined—for example a polynomial or a resolvent away from the spectrum—the response

\[
J_N^*F(B_N)J_N
\tag{15}
\]

has the same rank bound and the same conductor blindness. Passing from finite depth to a convergent resolvent/functional calculus does not enlarge the sampled source data.

Equations (6)--(8) also prove (2) directly: `J_N` uses only orders `N/p` and `N`, while `B_N` uses only `1`, `p`, and `pq`. Since every `W_{N,r}` is built solely from `J_N` and `B_N`, no other Fourier conductor can enter at any depth.

## 3. Exact matched control: change the omitted mixed conductors and every repeated word stays fixed

Assume first that `N` is odd, squarefree, and `k=omega(N)>=5`. Choose a divisor `d|N` with

\[
3\le\omega(d)\le k-2.
\tag{16}
\]

Then `d` is not in `Sigma_N`. Let `V_d` be the real Fourier subspace consisting of the conjugate-paired frequencies of exact order `d`. The source mask has nonzero Fourier coefficient at every such proper-order frequency by (9)--(10).

Choose a nontrivial real orthogonal transformation `U_d` on `V_d`, acting as the identity on every other exact-order Fourier subspace and preserving conjugation. Define a matched real mask `\widetilde g_N` by applying `U_d` to the Fourier coefficients of `g_N` and leaving all other coefficients unchanged.

This control preserves the full `L^2` norm exactly, hence preserves the normalization of the source mask. It also preserves every Fourier coefficient in `Sigma_N`. Therefore

\[
\boxed{
J_N(\widetilde g_N)=J_N(g_N),
\qquad
B_N(\widetilde g_N)=B_N(g_N),
}
\tag{17}
\]

and hence, for **every** depth,

\[
\boxed{
W_{N,r}(\widetilde g_N)=W_{N,r}(g_N)
\qquad(r\ge0).
}
\tag{18}
\]

Nevertheless the full transverse compression

\[
T_N(h):=P_NM_hP_N
\tag{19}
\]

can distinguish the two masks. Indeed, for every exact-order `d` frequency `k_d` with `d` as in (16), CRT lets one choose units `u,v in U(N)` satisfying `u-v=k_d`: at each prime in `d`, choose two nonzero residues with the prescribed nonzero difference, and at every prime outside `d` choose the same nonzero residue. Therefore

\[
\langle e_u,T_N(h)e_v\rangle=\widehat h(k_d)
\tag{20}
\]

samples precisely the coefficient that the control can change.

This is the requested information-gain control in the negative direction. The source and control agree on the common-anchor scalar quotient, every one-prime channel of PC-222, the entire prime-to-prime transition operator `B_N`, and all repeated responses (1), while they differ on a genuine middle mixed-conductor component already present in the intrinsic top-sector mask geometry of PC-215.

The restriction to odd `N` in this clean construction is only to avoid the one-dimensional CRT factor at `p=2`. The same phenomenon occurs whenever the chosen omitted divisor involves only odd primes. For example, at

\[
N=2310=2\cdot3\cdot5\cdot7\cdot11,
\qquad d=105=3\cdot5\cdot7,
\tag{21}
\]

the order-`105` Fourier sector is omitted by `Sigma_N`. A direct finite check with the exact cyclotomic mask shows that perturbing only the conjugate frequencies of order `105` changes `T_N` while leaving `J_N`, `B_N`, and the first several `W_{N,r}` unchanged to numerical precision; this is only a check of the exact support proof above, not evidence on which the theorem depends.

## 4. The depth-independent rank loss survives every final full-sector compression

The rank bound is not merely a finite-depth count. Any operator of the form (15) factors through `K_N`, so its kernel in `E_N` has dimension at least

\[
\boxed{
\dim\ker\bigl(J_N^*F(B_N)J_N\bigr)
\ge
\varphi(N)-R_N.
}
\tag{22}
\]

Hence whenever `R_N<phi(N)`, every full determinant on the top sector vanishes identically. For odd squarefree controls,

\[
\begin{array}{c|c|c|c}
N & R_N & \varphi(N) & R_N/\varphi(N)\\ \hline
105 & 12 & 48 & 1/4\\
1155 & 22 & 480 & 11/240\\
15015 & 34 & 5760 & 17/2880\\
255255 & 50 & 92160 & 25/46080
\end{array}
\tag{23}
\]

and the ratio tends to zero along the odd primorial sequence because the numerator is a sum of `p-1` while the denominator is their product.

Let `X_N` be any normalization of (15) whose operator norm is uniformly bounded. Its empirical spectral measure on `E_N` gives mass at least `1-R_N/phi(N)` to zero. Therefore for every bounded continuous test function `f`,

\[
\frac1{\varphi(N)}\operatorname{tr}f(X_N)
-f(0)
\longrightarrow0
\tag{24}
\]

along odd primorials. In particular, all normalized trace moments with `f(0)=0` vanish under any normalization that keeps the spectrum uniformly bounded.

This does not rule out information stored in the **nonzero** `R_N`-dimensional spectrum or its pseudodeterminant. It does show that repeated prime-axis mixing cannot turn into a bulk spectral law on the primitive sector, regardless of depth.

## 5. Prior-art and novelty audit

The pieces used in the reduction are classical. Orthogonal decompositions of finite signals into exact divisor-period/Ramanujan subspaces and their projectors are standard; a direct modern reference is P. P. Vaidyanathan, *Ramanujan Sums in the Context of Signal Processing—Part II: FIR Representations and Applications*, IEEE Transactions on Signal Processing 62 (2014), 4158–4172, DOI `10.1109/TSP.2014.2331624`. The finite Fourier evaluation of cyclotomic polynomials at roots of unity is classical and is treated explicitly by B. Bzdęga, A. Herrera-Poyatos and P. Moree, *Cyclotomic polynomials at roots of unity*, Acta Arithmetica 184 (2018), 215–230, DOI `10.4064/aa170112-20-12`; PC-215 already uses this as the prior-art boundary for the scalar coefficients.

The algebraic form `J^*B^rJ` is ordinary finite-dimensional moment/compression structure, closely related to standard Krylov/model-reduction transfer moments. Nothing about that wrapper is zeta-specific. A directed search through exact-period/Ramanujan subspaces, cyclotomic root-value transforms, Bost–Connes/cyclotomic dynamics, and finite-dimensional compression/moment methods found no source asserting the project-specific conductor support set (2) for this Prime-Circle word family. That absence is not treated as evidence of novelty.

The durable mathematical delta is instead the exact **blindness theorem**: once the source-forced common-anchor selector is inserted between every mask, arbitrary noncommutative depth still samples only (2), and a norm-preserving matched control can change middle mixed-conductor data while leaving the whole family unchanged. This is a new consequence inside the persisted Prime-Circle construction, not a claim of new cyclotomic or operator theory.

No zeta spectral parameter, gamma factor, `s <-> 1-s` symmetry, explicit-formula zero term, or critical-line condition emerges. The result is therefore a boundary theorem for a natural repair of PC-222, not progress toward RH by itself.

## 6. Consequence for the current frontier

PC-222 correctly left repeated mask-mediated prime-axis words open because the projections attached to different primes need not commute. PC-223 shows that noncommutativity alone is insufficient: all of those words are moments of one operator on `K_N`, and their source access never grows beyond endpoint orders `N/p` plus one- and two-prime conductor orders.

This closes the canonical chain

\[
\text{common-anchor Mangoldt selector}
\;\to\;
\text{repeated cyclotomic masks}
\;\to\;
\text{noncommuting prime-axis dynamics}
\;\to\;
\text{recovered mixed-conductor information}.
\]

The remaining escape must change a hypothesis that actually causes the obstruction. In particular, an informative cross-level operator must let intermediate states retain mixed exact-order sectors, or transport them through refinement before scalar prime-primary selection. Merely increasing the depth of `M_g \mathcal A_N` cannot do so.