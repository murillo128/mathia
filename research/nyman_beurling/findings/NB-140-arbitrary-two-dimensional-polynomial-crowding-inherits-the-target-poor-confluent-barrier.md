# NB-140 — arbitrary two-dimensional polynomial crowding inherits the target-poor confluent barrier

**Status:** `DERIVED + GROWING-SIMPLE-CLUSTER + COMPLEX-CONFLUENCE-CELL + TARGET-AWARE-GRASSMANN-CONTROL + ARBITRARY-TWO-DIMENSIONAL-NODE-GEOMETRY + EXPLICIT-POLYNOMIAL-DIAMETER + MATCHED-ZERO-ENVELOPE-CONTROL + REPRESENTATION-INVARIANT + NEGATIVE/METHOD-BOUNDARY`.

`NB-139` removes all dependence on the internal vertical gap pattern of a logarithmic-rank simple packet, but it deliberately keeps the real part fixed: the split nodes are real displacements of one analytic state family, so only the zero ordinates move. This leaves a genuine geometric escape. A hypothetical zeta packet inside a tiny vertical interval need not lie on one vertical line; its real parts may also vary.

That escape is absent at the same polynomial confluence scale. The analytic family already used in `NB-138` is holomorphic in a complex displacement. Its imaginary displacement changes the radial parameter while its real displacement changes the ordinate. Complex Newton divided differences therefore let the whole **two-dimensional zero cell** converge to the same target-poor confluent jet without introducing any inverse minimum-gap factor.

Fix

\[
r\ge1,\qquad q\ge2,\qquad 0<a<\frac12,
\qquad 0<c<\frac18,
\tag{1}
\]

and put

\[
m_G=\lceil G\rceil,\qquad R_G=m_Gq,
\qquad d_G=\lfloor c\log G\rfloor.
\tag{2}
\]

Retain the cell space, target and analytic one-state family of `NB-137`--`NB-139`,

\[
\mathcal E_{r,R_G}
=\operatorname{span}\{\phi_n:r\le n<R_G\},
\qquad
\phi_n(t)=e^{-t/2}\mathbf1_{[\log n,\log(n+1))}(t),
\tag{3}
\]

\[
e_G=e^{-t/2}\mathbf1_{[\log r,\log R_G)},
\tag{4}
\]

and, for a complex displacement `z`,

\[
\boxed{
\langle\phi_n,w_G(z)\rangle
=
\sqrt{2a}\,m_G^{a+iG+iz}
\int_n^{n+1}t^{-a-iG-iz-3/2}\,dt.
}
\tag{5}
\]

At `z=0`, the derivatives of `w_G` span the confluent zero-state space from `NB-108`--`NB-111`:

\[
\mathcal S_G^{\rm conf}
:=
\operatorname{span}\{w_G^{(j)}(0):0\le j<d_G\}.
\tag{6}
\]

Let

\[
z_{0,G},\ldots,z_{d_G-1,G}\in\mathbb C
\tag{7}
\]

be arbitrary pairwise-distinct nodes satisfying

\[
|z_{j,G}|\le\Delta_G,
\qquad
\Delta_G\longrightarrow0,
\tag{8}
\]

and define

\[
\mathcal S_G^{\rm split}
:=
\operatorname{span}\{w_G(z_{j,G}):0\le j<d_G\}.
\tag{9}
\]

As in `NB-138`--`NB-139`, set

\[
D_a:=1+\frac{4(1-a)}a=\frac4a-3.
\tag{10}
\]

Then the same sufficient scale as in `NB-139`,

\[
\boxed{
\Delta_G\,
G^{c\log D_a}
(\log G)^{25/2}
\longrightarrow0,
}
\tag{11}
\]

implies

\[
\boxed{
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\longrightarrow0.
}
\tag{12}
\]

In particular, for every fixed

\[
\boxed{B>c\log D_a,}
\tag{13}
\]

**every** pairwise-distinct simple packet in the complex displacement disk

\[
\boxed{|z_{j,G}|\le G^{-B}}
\tag{14}
\]

inherits the target-poor confluent barrier, regardless of the direction, anisotropy, ordering or internal pairwise gaps of the packet.

Writing

\[
z_{j,G}=x_{j,G}+iy_{j,G},
\tag{15}
\]

the corresponding physical zero parameters are

\[
\boxed{
\rho_{j,G}
=
\frac12+a-y_{j,G}+i(G+x_{j,G}).
}
\tag{16}
\]

Thus `(14)` is a genuine two-dimensional box/disk statement in the critical strip: both `Re rho` and `Im rho` may move by `O(G^{-B})`.

If also `c<0.10076`, the formal points `(16)` remain compatible with the same coarse right-half zero-count and Vinogradov--Korobov envelopes used in `NB-133`--`NB-139`. Those source laws therefore do not distinguish an arbitrary logarithmic-rank packet in a polynomially shrinking two-dimensional cell from admissible zero geometry.

## 1. The state family is uniformly holomorphic on the required complex tube

Write

\[
z=x+iy,
\qquad
b=a-y,
\qquad
\tau=G+x.
\tag{17}
\]

Then `(5)` becomes

\[
\langle\phi_n,w_G(z)\rangle
=
\sqrt{2a}\,m_G^{b+i\tau}
\int_n^{n+1}t^{-b-i\tau-3/2}\,dt.
\tag{18}
\]

On the fixed tube

\[
|y|\le\frac a2,
\tag{19}
\]

one has

\[
\frac a2\le b\le\frac{3a}{2}<\frac34.
\tag{20}
\]

For bounded `x` and large `G`, `|tau|` is comparable to `G`. The elementary antiderivative in `(18)` then gives, uniformly on the tube,

\[
\left|
\int_n^{n+1}t^{-b-i\tau-3/2}\,dt
\right|
\ll_a
\frac{n^{-b-1/2}}G.
\tag{21}
\]

Using

\[
\|\phi_n\|_2^2
=\frac1n-\frac1{n+1}
=\frac1{n(n+1)},
\tag{22}
\]

exactly as in `NB-138` yields

\[
\boxed{
\sup_{|\operatorname{Im}z|\le a/2,\ |\operatorname{Re}z|\le1}
\|w_G(z)\|_2
\le C_{a,q,r}
}
\tag{23}
\]

for all sufficiently large `G`.

Now suppose `Delta_G<=a/4`, which holds eventually. For every `|z|<=Delta_G`, the disk of radius

\[
r_G:=\frac a2-\Delta_G
\tag{24}
\]

centred at `z` stays inside the tube `(19)`. Cauchy's estimate for the finite-dimensional Hilbert-valued holomorphic map therefore gives

\[
\boxed{
\|w_G^{(k)}(z)\|_2
\le
C_{a,q,r}\,k!\,r_G^{-k}.
}
\tag{25}
\]

Define

\[
H_G:=\left(1-\frac{2\Delta_G}{a}\right)^{-1}.
\tag{26}
\]

Then

\[
r_G^{-k}
=
\left(\frac2a\right)^k H_G^k.
\tag{27}
\]

Condition `(11)` is much stronger than `Delta_G log G -> 0`. Since `d_G=O(log G)`, it follows that

\[
\boxed{H_G^{d_G}=\exp(O(d_G\Delta_G))=1+o(1).}
\tag{28}
\]

This is the only extra factor created by allowing the nodes to move horizontally as well as vertically.

## 2. Complex Newton divided differences still converge to the same jet

For a fixed `G`, abbreviate `d=d_G` and `z_j=z_{j,G}`. Define the normalized complex Newton columns

\[
u_{j,G}
:=
j!\,[z_0,\ldots,z_j]w_G,
\qquad 0\le j<d.
\tag{29}
\]

Because the nodes are pairwise distinct, `u_(j,G)` is a linear combination of

\[
w_G(z_0),\ldots,w_G(z_j)
\]

whose coefficient at `w_G(z_j)` is

\[
\frac{j!}{\prod_{\ell<j}(z_j-z_\ell)}\ne0.
\tag{30}
\]

Hence the Newton transformation is triangular and invertible, irrespective of how small the complex pairwise gaps are:

\[
\boxed{
\operatorname{span}\{u_{j,G}:0\le j<d\}
=
\mathcal S_G^{\rm split}.
}
\tag{31}
\]

The Hermite--Genocchi identity remains valid for complex nodes. No real-order argument is needed: for two nodes it is simply the fundamental theorem of calculus along the complex line segment,

\[
\frac{w_G(z_1)-w_G(z_0)}{z_1-z_0}
=
\int_0^1
w_G'((1-t)z_0+t z_1)\,dt,
\tag{32}
\]

and iterating `(32)` gives the Banach-valued simplex formula

\[
\boxed{
u_{j,G}
=
\int_{\Sigma_j}
 w_G^{(j)}\!\left(\sum_{\ell=0}^j t_\ell z_\ell\right)
 d\nu_j(t),
}
\tag{33}
\]

where `nu_j` is normalized Lebesgue measure on the standard simplex.

Every convex combination in `(33)` has modulus at most `Delta_G`. Applying the fundamental theorem of calculus once more, now along the segment from `0` to that complex point, and using `(25)` gives

\[
\boxed{
\|u_{j,G}-w_G^{(j)}(0)\|_2
\le
C_{a,q,r}\,
\Delta_G\,(j+1)!
\left(\frac2a\right)^{j+1}
H_G^{j+1}.
}
\tag{34}
\]

There is again no reciprocal minimum-gap factor. Arbitrarily severe local collision affects the Newton coefficients but not the direct Hilbert-space comparison `(34)`.

## 3. Laguerre coercivity transfers the whole two-dimensional packet

Use the same Laguerre-normalized confluent columns as `NB-138`--`NB-139`,

\[
g_{k,G}
=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 w_G^{(j)}(0),
\qquad 0\le k<d,
\tag{35}
\]

and define

\[
\widetilde g_{k,G}
:=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 u_{j,G}.
\tag{36}
\]

The transformation from the Newton columns to the `widetilde g` columns is triangular with nonzero diagonal, so `(31)` implies

\[
\operatorname{span}\{\widetilde g_{k,G}:0\le k<d\}
=
\mathcal S_G^{\rm split}.
\tag{37}
\]

Put

\[
X:=\frac{4(1-a)}a,
\qquad D_a=1+X.
\tag{38}
\]

From `(34)` and `H_G>=1`,

\[
\begin{aligned}
\|\widetilde g_{k,G}-g_{k,G}\|_2
&\le
C_{a,q,r}\Delta_G H_G^{k+1}
\sum_{j=0}^{k}
\binom kj(j+1)X^j\\
&=
C_{a,q,r}\Delta_G H_G^{k+1}
(1+X)^{k-1}(1+(k+1)X).
\end{aligned}
\tag{39}
\]

Hence

\[
\boxed{
\|\widetilde g_{k,G}-g_{k,G}\|_2
\le
C_{a,q,r}\Delta_G H_G^{k+1}(k+1)D_a^k.
}
\tag{40}
\]

Let

\[
A_G\alpha=\sum_{k<d}\alpha_k g_{k,G},
\qquad
B_G\alpha=\sum_{k<d}\alpha_k\widetilde g_{k,G}.
\tag{41}
\]

A Frobenius estimate and `(28)` give

\[
\boxed{
\|B_G-A_G\|
\le
(1+o(1))
C_{a,q,r}\Delta_G d_G^{3/2}D_a^{d_G}.
}
\tag{42}
\]

The Laguerre coercivity theorem of `NB-111`, in exactly these coordinates, gives for `d_G=floor(c log G)` and `c<1/8`

\[
\boxed{
\sigma_{\min}(A_G)
\gg_{a,q,r,c}
(\log G)^{-10}.
}
\tag{43}
\]

Therefore

\[
\vartheta_G
:=
C_{a,q,r,c}
\Delta_G d_G^{3/2}D_a^{d_G}(\log G)^{10}
\longrightarrow0
\tag{44}
\]

under `(11)`. Standard finite-dimensional range perturbation then yields

\[
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\le
\frac{\|P_{\mathcal S_G^{\rm conf}}e_G\|}
     {\|e_G\|}
+
\frac{\vartheta_G}{1-\vartheta_G}
+o(1).
\tag{45}
\]

The first term tends to zero by `NB-111`, while the other terms vanish by `(44)`. This proves `(12)`.

For `Delta_G=G^(-B)`,

\[
D_a^{d_G}
=G^{c\log D_a+o(1)},
\tag{46}
\]

so every fixed `B>c log D_a` satisfies `(11)` and `(44)`.

## 4. The complex displacement is exactly two-dimensional zero motion

The complex extension is not an artificial extra coordinate. From `(5)` and `(15)`,

\[
a+iG+iz_{j,G}
=
(a-y_{j,G})+i(G+x_{j,G}).
\tag{47}
\]

Thus `Re z` moves the ordinate and `Im z` moves the horizontal zero depth. Put

\[
a_{j,G}:=a-y_{j,G}.
\tag{48}
\]

For large `G`, `(8)` gives `a_(j,G)>a/2>0`. The canonically normalized simple-state representer at the physical parameter `(16)` has the same cell integrals as `(5)` with prefactor `sqrt(2a_(j,G))` instead of `sqrt(2a)`. Consequently

\[
w_G(z_{j,G})
=
\sqrt{\frac{a}{a_{j,G}}}\,
\widehat w_{j,G},
\tag{49}
\]

where `widehat w_(j,G)` denotes the canonically normalized state. The scalar in `(49)` is finite and nonzero, so

\[
\boxed{
\operatorname{span}\{w_G(z_{j,G})\}
=
\operatorname{span}\{\widehat w_{j,G}\}.
}
\tag{50}
\]

Therefore `(12)` is genuinely a statement about the physical simple-state range, not an artifact of holding the normalization at the central radial depth.

The common reference `m_G` is likewise only a nonzero column normalization. Replacing it by a nearby per-zero reference changes each state by a nonzero scalar and cannot alter the range or the target projection.

## 5. The same coarse zeta laws still permit the matched two-dimensional packet

Take the formal points `(16)` with `Delta_G=G^(-B)`. Their ordinates lie in

\[
[G-\Delta_G,G+\Delta_G],
\tag{51}
\]

a vertical interval of length `2G^(-B)`. The explicit zero-count estimate already anchored for this line has endpoint error

\[
0.10076\log T+0.24460\log\log T+O(1).
\tag{52}
\]

Across `(51)`, the Riemann--von Mangoldt main term changes by only

\[
O(\Delta_G\log G)=o(\log G),
\tag{53}
\]

while the two endpoint errors leave a whole-strip allowance of

\[
(0.20152+o(1))\log G.
\tag{54}
\]

Every point `(16)` is eventually strictly to the right of the critical line. Functional-equation symmetry pairs it with a left-half point at the same ordinate, so the corresponding right-half allowance remains

\[
(0.10076+o(1))\log G.
\tag{55}
\]

Thus every fixed `c<0.10076` remains below what this coarse counting law can exclude.

Horizontal variation does not activate the Vinogradov--Korobov zero-free region either. Since

\[
\operatorname{Re}\rho_{j,G}
\le
\frac12+a+\Delta_G,
\tag{56}
\]

and `a<1/2` is fixed, the packet stays a fixed positive distance to the left of `1` for all sufficiently large `G`, whereas the Vinogradov--Korobov forbidden boundary approaches `1`.

This is only a matched-control statement. It does not assert that zeta has such a packet. It says that the source laws currently used by this route do not contain enough local two-dimensional information to rule it out.

## 6. Stress tests, prior art and evidence boundary

Several checks are important.

First, setting every `y_(j,G)=0` reduces the theorem to the vertical geometry of `NB-139`. The new content is that an `O(G^-B)` horizontal spread does not open an escape. Conversely, a purely horizontal cluster with `x_(j,G)=0` is covered as well: variation of radial depths alone still converges to the same complex jet because the state map is holomorphic in the full zero parameter.

Second, no minimum complex separation is used. The Newton coefficients in `(30)` may become arbitrarily large, but the span identity `(31)` is exact and the direct simplex estimate `(34)` contains only the diameter of the enclosing complex cell. This is the same representation-invariant distinction that was essential in `NB-139`.

Third, pairwise distinctness is imposed only to describe a simple packet using ordinary divided differences. Exact repeated nodes are already confluent states and therefore do not provide an escape from the `NB-111` target-poor window. Mixed multiplicities would require Hermite notation but do not change the mechanism established here.

Fourth, the conclusion concerns the target projection of this packet, not the full Nyman distance. Other zero sectors or other source directions may remain target-bearing. The theorem also says nothing about packets whose horizontal or vertical diameter is larger than the quantified confluence scale.

The interpolation machinery is classical. Complex Newton divided differences and the Hermite--Genocchi formula are not claimed as new; the proof above derives the precise Banach-valued identity needed here directly from integration along complex line segments. A targeted literature audit found no prior result supplying the line-specific splice `(11)`--`(16)` between a two-dimensional zeta-zero cell and the Nyman target angle.

The current zero-spacing literature also does not supply the missing source theorem. In particular, Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals* (arXiv:2609.07918, 7 September 2026), proves lower bounds for simple/distinct zeros in short intervals; it does not give a deterministic upper bound excluding `Theta(log G)` right-half zeros from every polynomially shrinking two-dimensional cell. Likewise, global positive-proportion results for simple/distinct zeros do not control the maximum local off-critical occupancy needed here. None of those results is used as an input to the proof, so `SOURCES.md` needs no new load-bearing anchor.

## 7. Consequence for the live source discriminator

`NB-139` showed that internal vertical spacing geometry is irrelevant once a logarithmic-rank packet lies in a sufficiently small polynomial cell, but it left the horizontal coordinate frozen. The present result removes that last one-dimensional artifact:

\[
\boxed{
\text{logarithmic-rank simple packet}
+
\text{two-dimensional polynomial confluence}
\Longrightarrow
\text{target-poor state geometry},
}
\tag{57}
\]

under `(11)`.

Therefore a source-side repair cannot consist merely of showing that nearby zeros have slightly different real parts, nor of combining a vertical minimum-gap statement with bounded horizontal drift, nor of stabilizing a coordinate chart for the packet. To break this matched control one needs information that forces at most `o(log G)` relevant right-half zeros in every forbidden **two-dimensional polynomial confluence cell**, or a direct source theorem forcing nonvanishing target occupation even when such a cell is populated.

This leaves a cleaner representation-invariant frontier. The relevant unknown is not ordinary node spacing but **target-bearing local occupancy in the actual zeta zero plane**. A source theorem controlling that occupancy would be genuinely new arithmetic input; the currently imported zero count and zero-free region do not provide it.
