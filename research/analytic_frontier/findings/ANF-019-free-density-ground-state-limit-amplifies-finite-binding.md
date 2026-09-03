# ANF-019 — the free-density ground-state limit amplifies finite binding

**Status:** `EXACT-DERIVED + CLASSICAL-VARIATIONAL-REDIRECT + STRUCTURAL-BOUNDARY`. The stability functional isolated in `ANF-018` is not merely a finite-cluster correction to the unit-chain thermodynamic energy. For every continuous even `J>=0` supported in `[-1,1]`, with `F=widehat J`, the finite-configuration floor

\[
q_{\rm real}(J)
=\inf_X\frac1{|X|}\sum_{x,y\in X}F(x-y)
\]

is exactly the **large-particle-number free-density ground-state limit**. If `q_n(J)` denotes the minimum normalized energy among `n` distinct real points, then

\[
\boxed{\lim_{n\to\infty}q_n(J)=\inf_{n\ge1}q_n(J)=q_{\rm real}(J).}
\]

Equivalently, if `B_n(F)` is the optimal `n`-particle binding per particle, then

\[
\boxed{\lim_{n\to\infty}B_n(F)=B_{\rm stab}(F).}
\]

The proof is a direct subadditivity/Fekete argument using only `F(x)->0` as `|x|->infty`. Consequently any finite low-energy witness can be replicated into arbitrarily large configurations with essentially the same energy per particle by separating copies far enough. The edge-detuned 15-site witness of `ANF-017` therefore represents an **extensive cluster-binding mechanism** in the unconstrained-density problem, not an effect that vanishes as particle number grows.

This sharpens the boundary left by `ANF-018`: Sütő's unit-chain theorem is a fixed-density bulk statement, whereas `q_real` optimizes over density and may be realized asymptotically by a dilute gas of bound clusters. A proof of the Montgomery--Taylor ceiling must therefore control all such cluster phases, not only the density-one periodic ground state or its boundary correction.

## 1. Fixed-particle ground-state energies

Write

\[
F_0:=F(0)=\int_{-1}^{1}J(\alpha)\,d\alpha.
\]

For `n>=1`, define the off-diagonal `n`-particle ground-state energy

\[
u_n(F)
:=
\inf_{\substack{X\subset\mathbb R\\|X|=n}}
U_F(X),
\qquad
U_F(X):=\sum_{x<y\atop x,y\in X}F(x-y),
\tag{1}
\]

where the points are distinct. Define also

\[
q_n(J)
:=
\inf_{\substack{X\subset\mathbb R\\|X|=n}}
\frac1n\sum_{x,y\in X}F(x-y).
\tag{2}
\]

For every `X` of size `n`,

\[
\sum_{x,y\in X}F(x-y)=nF_0+2U_F(X),
\]

hence

\[
\boxed{q_n(J)=F_0+2\frac{u_n(F)}n.}
\tag{3}
\]

Because `J>=0`, the full Fourier energy is nonnegative:

\[
\sum_{x,y\in X}F(x-y)
=
\int_{-1}^{1}J(\alpha)
\left|\sum_{x\in X}e^{-2\pi i\alpha x}\right|^2d\alpha
\ge0.
\tag{4}
\]

Therefore

\[
u_n(F)\ge-\frac{nF_0}{2},
\tag{5}
\]

so the specific ground-state energies are uniformly bounded below.

## 2. The off-diagonal ground-state sequence is subadditive

Since `J` is continuous and compactly supported, `J\in L^1`, so the Riemann--Lebesgue lemma gives

\[
F(t)\longrightarrow0
\qquad(|t|\to\infty).
\tag{6}
\]

Take positive integers `n,m` and `epsilon>0`. Choose distinct finite configurations `X,Y` with

\[
U_F(X)<u_n+\epsilon,
\qquad
U_F(Y)<u_m+\epsilon.
\tag{7}
\]

Translate `Y` by a real parameter `T`. For sufficiently large `|T|`, the two supports are disjoint and, because there are only `nm` cross pairs,

\[
\left|
\sum_{x\in X}\sum_{y\in Y}F(x-y-T)
\right|<\epsilon.
\tag{8}
\]

Thus

\[
\begin{aligned}
u_{n+m}
&\le U_F\bigl(X\cup(Y+T)\bigr)\\
&=U_F(X)+U_F(Y)
 +\sum_{x\in X}\sum_{y\in Y}F(x-y-T)\\
&<u_n+u_m+3\epsilon.
\end{aligned}
\tag{9}
\]

Letting `epsilon->0` yields the exact subadditivity

\[
\boxed{u_{n+m}(F)\le u_n(F)+u_m(F).}
\tag{10}
\]

No decay rate and no absolute summability of `F` are needed; pointwise decay is enough because only finitely many cross terms are present at each gluing step.

## 3. Fekete's lemma identifies the full stability constant with a large-n limit

By (5), the subadditive sequence `u_n` has finite specific lower bound. Fekete's lemma therefore gives

\[
\boxed{
\lim_{n\to\infty}\frac{u_n(F)}n
=
\inf_{n\ge1}\frac{u_n(F)}n.
}
\tag{11}
\]

Using (3),

\[
\boxed{
\lim_{n\to\infty}q_n(J)
=
\inf_{n\ge1}q_n(J)
=
q_{\rm real}(J).
}
\tag{12}
\]

Now define the best `n`-particle binding per particle by

\[
B_n(F):=-\frac{u_n(F)}n.
\tag{13}
\]

The classical stability constant of `ANF-018` is

\[
B_{\rm stab}(F)
=
\sup_X\left(-\frac{U_F(X)}{|X|}\right)
=
\sup_{n\ge1}B_n(F).
\tag{14}
\]

Equation (11) immediately strengthens this to

\[
\boxed{
\lim_{n\to\infty}B_n(F)
=
\sup_{n\ge1}B_n(F)
=
B_{\rm stab}(F).
}
\tag{15}
\]

The sequence `B_n` need not be monotone. The point is that its limit nevertheless equals the optimal stability constant because the underlying unnormalized ground-state energies are subadditive.

Combining (12) with the exact identity from `ANF-018` recovers

\[
q_{\rm real}(J)=F_0-2B_{\rm stab}(F)
\tag{16}
\]

but now with an additional interpretation: the right side is the asymptotic free-density ground-state energy per particle, not merely an infimum over exceptional small clusters.

## 4. Every finite witness can be amplified without losing its per-particle gain

The large-`n` conclusion has a direct constructive form. Fix a finite configuration `X={x_1,\ldots,x_r}` with normalized energy

\[
e_J(X)=e.
\tag{17}
\]

For every integer `m>=1` and every `epsilon>0`, one can choose translations `T_1,\ldots,T_m` so far apart that the `m` translated copies are disjoint and all cross-copy interactions satisfy

\[
\left|
\sum_{1\le a<b\le m}
\sum_{i,j=1}^{r}
F(T_a-T_b+x_i-x_j)
\right|
<\frac{\epsilon mr}{2}.
\tag{18}
\]

This again uses only `F(t)->0`: for fixed `m` there are finitely many cross terms, so the translations can be chosen successively to make their total contribution as small as desired.

For

\[
Y_m:=\bigcup_{a=1}^{m}(X+T_a),
\qquad |Y_m|=mr,
\]

the full energy splits into the `m` internal cluster energies plus twice the cross-copy energy. Hence (18) gives

\[
\boxed{e_J(Y_m)<e_J(X)+\epsilon.}
\tag{19}
\]

The separations may grow arbitrarily rapidly, so the macroscopic density of `Y_m` can simultaneously be made arbitrarily small. Thus a finite bound cluster can be turned into an arbitrarily large **dilute cluster gas** with the same specific energy to any prescribed accuracy.

This is the mechanism behind subadditivity in concrete form. It also shows why a fixed-density thermodynamic calculation can miss the stability constant even when its particle number is infinite.

## 5. The ANF-017 edge witness is not a vanishing boundary correction

For the cubic spectrum `J_*` of `ANF-016`, the unit-chain bulk value is

\[
j_0=J_*(0)=1.
\]

`ANF-017` gives a 15-site edge-detuned cluster `X_*` with

\[
e_{J_*}(X_*)
=0.998079905262228\ldots,
\]

so

\[
1-e_{J_*}(X_*)
=0.001920094737772\ldots .
\tag{20}
\]

Applying (19), for every `epsilon>0` and arbitrarily large particle numbers divisible by 15 there exist real configurations with

\[
q_n(J_*)
\le
0.998079905262228\ldots+\epsilon.
\tag{21}
\]

Therefore the gain exposed by detuning two boundary gaps of one 15-site cluster does **not** decay like `1/n` in the free-density stability problem. Replicating the bound cluster makes that local edge pattern occupy a fixed fraction of the particles and converts its energy gain into an order-one specific binding energy.

The correct distinction is consequently:

- the unit chain is a fixed-density (`rho=1`) bulk test;
- the 15-site witness is a finite bound cluster;
- the stability constant allows arbitrarily many such clusters separated by vacuum, so the finite binding persists in the large-`n` unconstrained-density limit.

This does not contradict Sütő's density-one critical-chain result. It shows that the stability functional being used by the universal affine zeta certificate is a different variational problem because it does not impose a positive density, connectedness, or a fixed box volume.

## 6. Consequence for the Montgomery--Taylor scalar frontier

`ANF-018` reduced the remaining scalar no-go to

\[
q_{\rm real}(J)
\le
\frac{C(J)}{C_{\rm MT}},
\tag{22}
\]

or equivalently the corresponding lower bound on `B_stab(F)`. By (12), this is exactly

\[
\boxed{
\lim_{n\to\infty}q_n(J)
\le
\frac{C(J)}{C_{\rm MT}}.
}
\tag{23}
\]

Thus the scalar frontier may be attacked as a genuine thermodynamic ground-state problem, but it is a **free-density** one. A proof can construct low-energy clusters of any convenient finite size and amplify them; a counterexample must prove a uniform lower bound on `q_n` for every `n`, equivalently a lower bound on the large-`n` limit.

In particular, proving that the unit chain minimizes energy at density one, or even throughout a high-density regime, is insufficient. The remaining obstruction can live in a lower-density molecular or cluster phase and survive at arbitrarily large particle number through phase separation by vacuum.

This redirects the classical-mechanics search from "finite boundary corrections versus the thermodynamic lattice" to **unconstrained-density ground states and cluster binding**. Fixed-density structure-factor theorems remain valuable controls, but they cannot by themselves identify `B_stab` unless they also exclude lower-density bound clusters.

## 7. Prior-art and audit boundary

The ingredients of the limit argument are classical: Ruelle stability is defined through a uniform linear lower bound on finite-particle energies, and subadditivity plus Fekete's lemma is standard variational machinery. Procacci remains the repository anchor for the stability-constant convention used in `ANF-018`; Sütő remains the anchor for compact-spectrum positive-type ground states at fixed density. A targeted search of stability, ground-state-energy, and compact-spectrum literature found the expected classical stability framework but no reason to identify Sütő's density-one bulk energy with the best stability constant.

The Mathia contribution here is the exact specialization (10)--(15) to the `q_real` functional and the resulting correction of interpretation for the Montgomery--Taylor frontier: finite binding is automatically amplifiable and therefore belongs to the large-`n` free-density ground-state problem. No publication-level novelty claim is made for the subadditivity principle itself.

The argument relies on `F(t)->0`, guaranteed here by `J\in L^1`. It does not require `F\in L^1`, periodic replication, an attained finite minimizer, or any quantitative decay rate. If one imposed a fixed positive density or confinement volume, the separation argument would no longer apply; that is precisely why fixed-density theorems and `q_real` answer different variational questions.

## 8. Next boundary

The live scalar question remains the sharp inequality of `ANF-018`, but the cheapest useful attack has changed form. One should seek either:

1. a universal construction of finite bound clusters whose specific energy reaches `C(J)/C_MT` whenever the unit-chain first-moment test does not already do so; or
2. a genuine free-density ground-state lower bound for a candidate spectrum proving that **all** cluster sizes stay above that threshold.

Because any successful finite cluster can be amplified, there is no need for the witness itself to resemble a large zeta-zero block or a density-one lattice. Conversely, a candidate scalar survivor cannot be validated by high-density or periodic tests alone: it must exclude dilute cluster binding across the full large-`n` limit.
