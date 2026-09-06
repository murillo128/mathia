# ANF-078 — Bernoulli thinning closes every fixed real multiplicity cap

**Status:** `EXACT-DERIVED + REAL-MULTIPLICITY + BERNOULLI-THINNING + OCCUPANCY-CAP-UNIFORM + SUPPORT-UNBOUNDED + MIXED-ONE-TWO-CLOSED`. `ANF-077` reduces heterogeneous real multiplicity at the uniform-occupancy normalization to nested-set excess defects and identifies mixtures of singleton and double sites as the first zero-surplus class. That exact `A=2`, `t=q_real^{-1}` gate is not a shape-level obstruction. A small retreat in the affine intercept, combined with an explicit simple-support floor already implicit in the near-extremizer estimates of `ANF-034`, closes not only the mixed `1/2` class but **every prescribed finite cap on the maximum site multiplicity**, uniformly in the number and geometry of support sites.

More precisely, fix an integer `K>=1`. There are central-notch parameters `eta>0`, `s>0`, a positive simple-support floor `q_0`, a spectral amplitude `t_K=q_0^{-1}`, and an affine intercept `A_K<2` such that every finite real multiset whose site multiplicities satisfy `1<=k_i<=K` obeys

\[
\boxed{
\sigma\ge A_K N-t_KE_{F_s}(k;X),
}
\tag{1}
\]

while the resulting BGSST objective is still strictly better than Montgomery--Taylor. Here

\[
N=\sum_i k_i,
\qquad
\sigma=\#\{i:k_i=1\},
\qquad
F_s=\widehat J_s,
\]

with the central-notch spectrum

\[
J_s=J_{\rm MT}-s\phi_\eta.
\tag{2}
\]

Thus no real-multiplicity no-go with a **fixed a priori bound on the largest occupancy** can kill the central-notch shape family. Together with `ANF-075`, which closes every fixed support-cardinality cap with no occupancy bound, this forces any obstruction that survives arbitrarily narrow notches to send both the number of occupied sites and the maximum site multiplicity to infinity.

## 1. The near-Montgomery--Taylor estimates give an explicit simple-set floor

Keep the notation of `ANF-034`. Put

\[
c_0
:=
\int_{-1}^{1}
\left(\frac{\sin\pi u}{\pi u}\right)^2du,
\qquad
B_{\eta,L}
:=
\frac4{c_0}\left(\eta+\frac4L\right).
\tag{3}
\]

For the deletion scale `L` used there, let

\[
r_L:=\frac2{\kappa_L},
\qquad
a_L:=1+r_L.
\tag{4}
\]

If `X` is any finite set of distinct real points, normalize its Montgomery--Taylor energy by

\[
e_{\rm MT}(X)=1+\Delta(X),
\qquad
\Delta(X)\ge0,
\tag{5}
\]

and write

\[
p_\eta(X):=\int\phi_\eta\,d\mu_X.
\]

Equations (11), (14), and (15) of `ANF-034` give the global estimate

\[
\boxed{
p_\eta(X)
\le
b_\eta B_{\eta,L}
+E_L(\Delta(X)),
}
\tag{6}
\]

where

\[
E_L(u)
=
2\sqrt{a_Lu(1+u)}+a_Lu.
\tag{7}
\]

No small-excess hypothesis is needed in (6); the small-excess split in `ANF-034` was only one way of converting this estimate into a strict separator.

Set

\[
\beta:=s b_\eta.
\tag{8}
\]

Since

\[
e_s(X)
=
1+\Delta(X)-s p_\eta(X),
\]

(6) gives

\[
e_s(X)
\ge
1-\beta B_{\eta,L}
+\Delta-sE_L(\Delta).
\tag{9}
\]

The remaining one-variable loss is quadratic in `s`. Indeed

\[
\sqrt{u(1+u)}\le\sqrt u+u,
\]

so

\[
E_L(u)
\le
2\sqrt{a_L}\sqrt u
+\bigl(2\sqrt{a_L}+a_L\bigr)u.
\tag{10}
\]

Choose `s` small enough that

\[
s\bigl(2\sqrt{a_L}+a_L\bigr)\le\frac12.
\tag{11}
\]

Then

\[
\begin{aligned}
u-sE_L(u)
&\ge
\frac12u-2s\sqrt{a_Lu}\\
&\ge
-2a_Ls^2.
\end{aligned}
\tag{12}
\]

Consequently every finite distinct real set satisfies the explicit support-uniform floor

\[
\boxed{
E_{F_s}(X)
\ge
q_0|X|,
\qquad
q_0:=1-\beta B_{\eta,L}-2a_Ls^2.
}
\tag{13}
\]

For sufficiently small `s`, `q_0>0`. This is deliberately a certified lower floor, not the exact variational value `q_real(J_s)`.

The diagonal value of the notched kernel is exact:

\[
\boxed{
F_s(0)=1-\beta\eta.
}
\tag{14}
\]

Moreover `B_{eta,L}>eta`, so (13)--(14) give

\[
F_s(0)-q_0
=
\beta(B_{\eta,L}-\eta)+2a_Ls^2
>0.
\tag{15}
\]

## 2. Independent thinning lifts the simple-set floor to bounded integer weights

Now let `x_1,...,x_r` be arbitrary distinct real support sites with integer occupancies

\[
1\le k_i\le K.
\tag{16}
\]

Put

\[
W_2:=\sum_i k_i^2.
\tag{17}
\]

Independently retain site `x_i` with probability

\[
p_i:=\frac{k_i}{K},
\tag{18}
\]

and call the resulting random simple subset `Y`. The empty outcome causes no problem because both sides of the simple-set floor are then zero.

For distinct indices `i!=j`, independence gives

\[
K^2\mathbb E[\mathbf1_{i\in Y}\mathbf1_{j\in Y}]
=k_ik_j,
\]

while on the diagonal

\[
K^2\mathbb E[\mathbf1_{i\in Y}]
=Kk_i.
\]

Therefore the weighted energy has the exact expectation identity

\[
\boxed{
K^2\,\mathbb E E_{F_s}(Y)
=
E_{F_s}(k;X)
+F_s(0)\sum_i k_i(K-k_i).
}
\tag{19}
\]

Applying (13) outcome by outcome and using

\[
\mathbb E|Y|=\frac NK
\]

gives

\[
\begin{aligned}
E_{F_s}(k;X)
&\ge
Kq_0N
-F_s(0)(KN-W_2)\\
&=
\boxed{
F_s(0)W_2
-K\bigl(F_s(0)-q_0\bigr)N.
}
\end{aligned}
\tag{20}
\]

This is the support-uniform weighted floor missing from the crude `H(k)` estimate of `ANF-077`. Its price is linear in total multiplicity `N`, not quadratic in the number of unlike support pairs.

The probabilistic device in (19) is only a proof mechanism: the final inequality (20) is deterministic and holds for every geometry. No random point-process hypothesis, thermodynamic limit, spacing condition, or attainment of `q_real` is used.

## 3. A small intercept retreat closes every occupancy vector below `K`

Define

\[
d_K
:=
\frac{F_s(0)-q_0}{q_0}\ge0,
\qquad
t_K:=\frac1{q_0},
\qquad
\boxed{A_K:=2-(K-1)d_K.}
\tag{21}
\]

Insert (20) into the affine slack

\[
\mathcal S_K(k;X)
:=
\sigma-A_KN+t_KE_{F_s}(k;X).
\tag{22}
\]

Since `F_s(0)/q_0=1+d_K`, one obtains

\[
\begin{aligned}
\mathcal S_K
&\ge
\sigma-2N+(K-1)d_KN
+(1+d_K)W_2-Kd_KN\\
&=
\boxed{
P(k)+d_K(W_2-N),
}
\tag{23}
\]

where, exactly as in `ANF-075` and `ANF-077`,

\[
P(k)
:=
W_2-2N+\sigma
=
\sum_{k_i\ge2}k_i(k_i-2)
\ge0.
\tag{24}
\]

Also

\[
W_2-N
=
\sum_i k_i(k_i-1)
\ge0.
\tag{25}
\]

Thus

\[
\boxed{\mathcal S_K(k;X)\ge0}
\tag{26}
\]

for every finite real multiset with `max_i k_i<=K`, with no support-cardinality restriction.

The critical `K=2` case is especially informative. `ANF-077` showed that at the exact uniform normalization `A=2`, `t=q_real^{-1}`, mixed singleton/double occupancy is equivalent to the unresolved three-set excess inequality

\[
\Delta_q(A)
\le
2\Delta_q(B)+2\Delta_q(A\cup B).
\]

Equation (26) does **not** prove that inequality. It bypasses it: a controlled intercept retreat of size `d_2` makes the whole mixed `1/2` class safe. Therefore failure of the exact excess inequality, if it occurs, would no longer constitute a central-notch shape-level no-go.

## 4. Narrowing the notch makes the retreat cheaper than the spectral gain

It remains to check that the normalization payment in (21) does not erase the Montgomery--Taylor improvement. The exact central-notch identities are

\[
C(J_s)
=
C_{\rm MT}
-\beta\left(1+\frac{\eta^2}{3}\right),
\qquad
F_s(0)=1-\beta\eta.
\tag{27}
\]

Write

\[
c_\eta:=1+\frac{\eta^2}{3}
\]

and define

\[
\boxed{
D_K(\eta,L)
:=
c_\eta+(K-1)\eta
-(C_{\rm MT}+K-1)B_{\eta,L}.
}
\tag{28}
\]

For every fixed `K` one can choose `eta>0` sufficiently small and then `L` sufficiently large so that

\[
\boxed{D_K(\eta,L)>0.}
\tag{29}
\]

Indeed `B_{eta,L}->0` when first `eta->0` and then `L->infinity`, while the first term in (28) tends to `1`.

After fixing such `eta,L`, choose `s>0` small enough to satisfy (11), `q_0>0`, and

\[
\boxed{
2a_Ls(C_{\rm MT}+K-1)
<
b_\eta D_K(\eta,L).
}
\tag{30}
\]

Using `q_0=1-beta B_{eta,L}-2a_Ls^2`, a direct expansion gives

\[
\begin{aligned}
&C(J_s)+(K-1)\bigl(F_s(0)-q_0\bigr)-C_{\rm MT}q_0\\
&\qquad=
-sb_\eta D_K(\eta,L)
+2a_Ls^2(C_{\rm MT}+K-1)
<0.
\end{aligned}
\tag{31}
\]

Equivalently,

\[
\boxed{
A_K-t_KC(J_s)
>
2-C_{\rm MT}.
}
\tag{32}
\]

In the equivalent `M+delta` normalization, the scaled kernel `t_KF_s` has

\[
\delta_K
:=
1+t_KF_s(0)-A_K
=Kd_K,
\tag{33}
\]

and (32) says

\[
\boxed{
M(t_KF_s)+\delta_K
<m_{\rm MT}.
}
\tag{34}
\]

Thus the bounded-occupancy certificate is a genuine strict Montgomery--Taylor improvement, not merely a feasibility statement.

For a fixed width/deletion pair, (29) also gives an explicit scale for the occupancy cap. Because `B_{eta,L}>eta`, the condition is equivalent, whenever the numerator is positive, to

\[
\boxed{
K-1
<
\frac{c_\eta-C_{\rm MT}B_{\eta,L}}
{B_{\eta,L}-\eta}.
}
\tag{35}
\]

If `L` is taken so that `L^{-1}=o(eta)`, then

\[
B_{\eta,L}
=\left(\frac4{c_0}+o(1)\right)\eta,
\]

so the admissible occupancy ceiling grows on the order of `eta^{-1}` as the notch narrows. The deletion constant `a_L` can force the allowed amplitude `s` in (30) to become much smaller; that affects the size of the strict improvement but not its existence.

## 5. Boundary, prior art, and next scalar gate

This result is orthogonal to `ANF-075`. That finding allows arbitrarily large multiplicities but fixes the number of distinct support sites; the present argument allows arbitrarily many support sites but fixes the maximum multiplicity. Hence a real-multiplicity obstruction robust against the central-notch narrowing strategy must escape **both** compactness directions. It must have support cardinality tending to infinity and maximum occupancy tending to infinity. `ANF-077` remains the correct exact bookkeeping framework for that doubly growing regime.

No claim is made that one fixed choice of `eta,s,A` in the present theorem handles all integer multiplicities. The parameters depend on `K`, and the intercept payment grows with the occupancy cap. Therefore this is not yet a universal real-multiset certificate and has no RH consequence. The remaining scalar question is whether the superlevel-excess structure of `ANF-077`, together with the central-notch near-face control used here, can prevent a counterexample when support and occupancy grow simultaneously on the reciprocal-notch scale.

Independent Bernoulli thinning, randomized rounding, and expectation identities for quadratic forms are classical probabilistic devices; no novelty is claimed for them. The neighboring Fisher--Ruelle superstability literature likewise studies lower bounds expressed through local occupation numbers. A targeted prior-art search did not identify an external theorem that yields (19)--(34) in the present finite deterministic affine setting. The load-bearing ingredients are the already-canonical Montgomery--Taylor near-face estimate of `ANF-034` and the elementary Bernoulli expectation calculation above, so the existing Sütő/Procacci stability anchors in `SOURCES.md` remain sufficient and no source-file change is needed.

The main adversarial checks are explicit. The proof never upgrades `q_0` to the exact `q_real`; it uses only the certified inequality (13). Empty thinned subsets are harmless. The diagonal correction in (19) has the sign shown and is essential — omitting it would falsely assert that simple-support stability automatically extends to arbitrary positive weights. Finally, `K=2` closes the zero-surplus mixed class only after reoptimizing the affine intercept, so it does not retroactively establish the exact `A=2` inequality left open in `ANF-077`.