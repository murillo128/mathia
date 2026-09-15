# NB-140 — arbitrary two-dimensional polynomial crowding inherits the target-poor confluent barrier

**Status:** `DERIVED + GROWING-SIMPLE-CLUSTER + COMPLEX-CONFLUENCE-CELL + TARGET-AWARE-GRASSMANN-CONTROL + ARBITRARY-TWO-DIMENSIONAL-NODE-GEOMETRY + EXPLICIT-POLYNOMIAL-DIAMETER + MATCHED-ZERO-ENVELOPE-CONTROL + REPRESENTATION-INVARIANT + NEGATIVE/METHOD-BOUNDARY`.

`NB-139` removes all dependence on the internal vertical gap pattern of a logarithmic-rank simple packet, but deliberately keeps the real part fixed. A hypothetical zeta packet inside a tiny vertical interval need not lie on one vertical line, so horizontal motion remained a genuine geometric escape.

That escape is absent at the same polynomial confluence scale. The state family already used in `NB-138` is holomorphic in a complex displacement: its real part moves the ordinate and its imaginary part moves the radial depth. Complex Newton divided differences therefore let an arbitrary **two-dimensional zero cell** converge to the same target-poor confluent jet without introducing any inverse minimum-gap factor.

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

On the fully backfilled cell space

\[
\mathcal E_{r,R_G}
=
\operatorname{span}\{\phi_n:r\le n<R_G\},
\qquad
\phi_n(t)=e^{-t/2}\mathbf1_{[\log n,\log(n+1))}(t),
\tag{3}
\]

retain the visible target

\[
e_G=e^{-t/2}\mathbf1_{[\log r,\log R_G)}
\tag{4}
\]

and the analytic one-state family

\[
\boxed{
\langle\phi_n,w_G(z)\rangle
=
\sqrt{2a}\,m_G^{a+iG+iz}
\int_n^{n+1}t^{-a-iG-iz-3/2}\,dt.
}
\tag{5}
\]

At `z=0`, the derivatives of `w_G` span the confluent zero-state space of `NB-108`--`NB-111`:

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

inherits the target-poor confluent barrier, independently of its direction, anisotropy, ordering, or internal pairwise gaps.

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

Thus `(14)` is genuinely two-dimensional in the critical strip: both `Re rho` and `Im rho` may move by `O(G^{-B})`.

If also `c<0.10076`, the formal points `(16)` remain compatible with the same coarse right-half zero-count and Vinogradov--Korobov envelopes used in `NB-133`--`NB-139`. Those source laws do not distinguish such an arbitrary logarithmic-rank packet from admissible zero geometry.

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

On the fixed tube `|y|<=a/2`,

\[
\frac a2\le b\le\frac{3a}{2}<\frac34.
\tag{19}
\]

For bounded `x` and large `G`, `|tau|` is comparable to `G`. Evaluating the elementary antiderivative in `(18)` gives uniformly

\[
\left|
\int_n^{n+1}t^{-b-i\tau-3/2}\,dt
\right|
\ll_a
\frac{n^{-b-1/2}}G.
\tag{20}
\]

Since

\[
\|\phi_n\|_2^2
=\frac1n-\frac1{n+1}
=\frac1{n(n+1)},
\tag{21}
\]

the same orthogonal-cell calculation as in `NB-138` gives

\[
\boxed{
\sup_{|\operatorname{Im}z|\le a/2,\ |\operatorname{Re}z|\le1}
\|w_G(z)\|_2
\le C_{a,q,r}
}
\tag{22}
\]

for all sufficiently large `G`.

Eventually `Delta_G<=a/4`. For every `|z|<=Delta_G`, the disk of radius

\[
r_G:=\frac a2-\Delta_G
\tag{23}
\]

centred at `z` lies in the tube used in `(22)`. Cauchy's estimate for the finite-dimensional Hilbert-valued holomorphic map therefore gives

\[
\boxed{
\|w_G^{(k)}(z)\|_2
\le
C_{a,q,r}\,k!\,r_G^{-k}.
}
\tag{24}
\]

Define

\[
H_G:=\left(1-\frac{2\Delta_G}{a}\right)^{-1}.
\tag{25}
\]

Then

\[
r_G^{-k}
=
\left(\frac2a\right)^k H_G^k.
\tag{26}
\]

Condition `(11)` implies `Delta_G log G -> 0`. Since `d_G=O(log G)`,

\[
\boxed{
H_G^{d_G}
=
\exp(O(d_G\Delta_G))
=1+o(1).
}
\tag{27}
\]

This asymptotically unit factor is the only extra derivative cost caused by allowing horizontal as well as vertical zero motion.

## 2. Complex Newton divided differences remove all minimum-gap dependence

For fixed `G`, abbreviate `d=d_G` and `z_j=z_{j,G}`. Define

\[
u_{j,G}
:=
j!\,[z_0,\ldots,z_j]w_G,
\qquad 0\le j<d.
\tag{28}
\]

Because the nodes are pairwise distinct, `u_{j,G}` is a linear combination of

\[
w_G(z_0),\ldots,w_G(z_j)
\]

whose coefficient at `w_G(z_j)` is

\[
\frac{j!}{\prod_{\ell<j}(z_j-z_\ell)}\ne0.
\tag{29}
\]

Hence the Newton transformation is triangular and invertible regardless of how small the complex pairwise gaps are:

\[
\boxed{
\operatorname{span}\{u_{j,G}:0\le j<d\}
=
\mathcal S_G^{\rm split}.
}
\tag{30}
\]

The Hermite--Genocchi identity also holds for these complex nodes. For two nodes it is just the fundamental theorem of calculus along a complex line segment,

\[
\frac{w_G(z_1)-w_G(z_0)}{z_1-z_0}
=
\int_0^1
w_G'((1-t)z_0+t z_1)\,dt,
\tag{31}
\]

and iterating `(31)` gives

\[
\boxed{
u_{j,G}
=
\int_{\Sigma_j}
 w_G^{(j)}\!\left(\sum_{\ell=0}^j t_\ell z_\ell\right)
 d\nu_j(t),
}
\tag{32}
\]

where `nu_j` is normalized Lebesgue measure on the standard simplex. Every convex combination in `(32)` has modulus at most `Delta_G`. Integrating once more along the segment from `0` to that point and using `(24)` yields

\[
\boxed{
\|u_{j,G}-w_G^{(j)}(0)\|_2
\le
C_{a,q,r}\,
\Delta_G\,(j+1)!
\left(\frac2a\right)^{j+1}
H_G^{j+1}.
}
\tag{33}
\]

There is no reciprocal minimum-gap factor. Near-collision may make the Newton coefficients enormous, but it does not enlarge the direct Hilbert-space comparison `(33)`.

## 3. Laguerre coercivity transfers the entire complex packet

Use the same Laguerre-normalized confluent columns as `NB-138`--`NB-139`,

\[
g_{k,G}
=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 w_G^{(j)}(0),
\qquad 0\le k<d,
\tag{34}
\]

and define

\[
\widetilde g_{k,G}
:=
\sum_{j=0}^{k}
\binom kj
\frac{(2i(1-a))^j}{j!}
 u_{j,G}.
\tag{35}
\]

This is another triangular change of coordinates with nonzero diagonal, so

\[
\operatorname{span}\{\widetilde g_{k,G}:0\le k<d\}
=
\mathcal S_G^{\rm split}.
\tag{36}
\]

Put

\[
X:=\frac{4(1-a)}a,
\qquad D_a=1+X.
\tag{37}
\]

From `(33)` and `H_G>=1`,

\[
\begin{aligned}
\|\widetilde g_{k,G}-g_{k,G}\|_2
&\le
C_{a,q,r}\Delta_G H_G^{k+1}
\sum_{j=0}^{k}\binom kj(j+1)X^j\\
&=
C_{a,q,r}\Delta_G H_G^{k+1}
(1+X)^{k-1}(1+(k+1)X).
\end{aligned}
\tag{38}
\]

Hence

\[
\boxed{
\|\widetilde g_{k,G}-g_{k,G}\|_2
\le
C_{a,q,r}\Delta_G H_G^{k+1}(k+1)D_a^k.
}
\tag{39}
\]

Let

\[
A_G\alpha=\sum_{k<d}\alpha_k g_{k,G},
\qquad
B_G\alpha=\sum_{k<d}\alpha_k\widetilde g_{k,G}.
\tag{40}
\]

A Frobenius estimate and `(27)` give

\[
\boxed{
\|B_G-A_G\|
\le
(1+o(1))
C_{a,q,r}\Delta_G d_G^{3/2}D_a^{d_G}.
}
\tag{41}
\]

The Laguerre coercivity theorem of `NB-111`, in these same coordinates, gives for `(2)` and `c<1/8`

\[
\boxed{
\sigma_{\min}(A_G)
\gg_{a,q,r,c}
(\log G)^{-10}.
}
\tag{42}
\]

Therefore

\[
\vartheta_G
:=
C_{a,q,r,c}
\Delta_G d_G^{3/2}D_a^{d_G}(\log G)^{10}
\longrightarrow0
\tag{43}
\]

under `(11)`. Standard finite-dimensional range perturbation gives

\[
\frac{\|P_{\mathcal S_G^{\rm split}}e_G\|}
     {\|e_G\|}
\le
\frac{\|P_{\mathcal S_G^{\rm conf}}e_G\|}
     {\|e_G\|}
+
\frac{\vartheta_G}{1-\vartheta_G}
+o(1).
\tag{44}
\]

The first term tends to zero by `NB-111`, and the remaining terms vanish by `(43)`. This proves `(12)`.

For `Delta_G=G^(-B)`,

\[
D_a^{d_G}
=G^{c\log D_a+o(1)},
\tag{45}
\]

so every fixed `B>c log D_a` satisfies the hypothesis.

## 4. Complex displacement is exactly two-dimensional zero motion

From `(5)` and `(15)`,

\[
a+iG+iz_{j,G}
=
(a-y_{j,G})+i(G+x_{j,G}).
\tag{46}
\]

Thus `Re z` moves the ordinate and `Im z` moves the horizontal depth. Set

\[
a_{j,G}:=a-y_{j,G}.
\tag{47}
\]

For large `G`, `(8)` gives `a_{j,G}>a/2>0`. The canonically normalized simple-state representer at `(16)` has the same cell integrals as `(5)` but prefactor `sqrt(2a_(j,G))` instead of `sqrt(2a)`. Therefore

\[
w_G(z_{j,G})
=
\sqrt{\frac{a}{a_{j,G}}}\,
\widehat w_{j,G},
\tag{48}
\]

where `widehat w_(j,G)` is the canonical state. The scalar is nonzero, so

\[
\boxed{
\operatorname{span}\{w_G(z_{j,G}):j<d_G\}
=
\operatorname{span}\{\widehat w_{j,G}:j<d_G\}.
}
\tag{49}
\]

Thus `(12)` concerns the physical simple-state range, not an artifact of fixing the central normalization.

## 5. The coarse zeta laws still permit the matched two-dimensional packet

Take `(16)` with `Delta_G=G^(-B)`. All ordinates lie in

\[
[G-\Delta_G,G+\Delta_G],
\tag{50}
\]

a vertical interval of length `2G^(-B)`. The explicit zero-count estimate already anchored for this line has endpoint error

\[
0.10076\log T+0.24460\log\log T+O(1).
\tag{51}
\]

Across `(50)`, the Riemann--von Mangoldt main term changes by

\[
O(\Delta_G\log G)=o(\log G),
\tag{52}
\]

while the two endpoint errors leave a whole-strip allowance of

\[
(0.20152+o(1))\log G.
\tag{53}
\]

Every point `(16)` is eventually strictly right of the critical line. Functional-equation symmetry pairs each with a left-half point at the same ordinate, so the corresponding right-half allowance remains

\[
(0.10076+o(1))\log G.
\tag{54}
\]

Thus every fixed `c<0.10076` remains below what this coarse counting law alone can exclude.

Horizontal motion does not activate the Vinogradov--Korobov zero-free region. Since

\[
\operatorname{Re}\rho_{j,G}
\le
\frac12+a+\Delta_G,
\tag{55}
\]

and `a<1/2` is fixed, the packet eventually stays a fixed positive distance left of `1`, whereas the Vinogradov--Korobov forbidden boundary approaches `1`.

This is a matched-control statement, not an assertion that zeta realizes such packets. It says that the source laws currently imported into this route contain too little local two-dimensional information to rule them out.

## 6. Stress tests, prior art, and evidence boundary

Setting every `y_{j,G}=0` recovers the vertical geometry of `NB-139`. The new content is that an `O(G^-B)` horizontal spread does not open an escape. Conversely, setting every `x_{j,G}=0` gives a purely horizontal cluster: varying radial depths alone also converges to the same complex jet because the state map is holomorphic in the full zero parameter.

No minimum complex separation is used. The Newton coefficients in `(29)` may become arbitrarily large, but `(30)` is an exact identity of ranges and `(33)` depends only on the enclosing cell diameter. Exact repeated nodes are already confluent states and therefore do not evade the `NB-111` target-poor window; mixed multiplicities would require Hermite notation but no new mechanism.

The conclusion concerns the target projection of this packet, not the full Nyman distance. Other zero sectors may remain target-bearing. It also does not treat packets whose two-dimensional diameter is larger than the quantified confluence scale.

Complex Newton divided differences and the Hermite--Genocchi formula are classical interpolation machinery; no novelty is claimed for them. The proof above derives the exact Banach-valued identity needed here directly from integration along complex line segments. A targeted literature audit found no prior result giving the line-specific splice between a two-dimensional zeta-zero cell and this Nyman target-angle barrier.

The current zero-spacing literature does not supply the missing source theorem either. Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals* (arXiv:2609.07918, 7 September 2026), gives lower bounds for simple/distinct zeros in short intervals, not a deterministic upper bound excluding `Theta(log G)` right-half zeros from every polynomially shrinking two-dimensional cell. Global positive-proportion results for simple/distinct zeros likewise do not control the maximum local off-critical occupancy required here. None of these results is an input to the proof, so `SOURCES.md` needs no new load-bearing anchor.

## 7. Consequence for the live source discriminator

`NB-139` showed that internal vertical spacing geometry is irrelevant once a logarithmic-rank packet lies in a sufficiently small polynomial cell, but left the horizontal coordinate frozen. The present result removes that one-dimensional artifact:

\[
\boxed{
\text{logarithmic-rank simple packet}
+
\text{two-dimensional polynomial confluence}
\Longrightarrow
\text{target-poor state geometry},
}
\tag{56}
\]

under `(11)`.

A source-side repair therefore cannot consist merely of showing that nearby zeros have slightly different real parts, combining a vertical minimum-gap statement with bounded horizontal drift, or stabilizing a coordinate chart. To break this matched control one needs information forcing at most `o(log G)` relevant right-half zeros in every forbidden **two-dimensional polynomial confluence cell**, or a direct source theorem forcing nonvanishing target occupation even when such a cell is populated.

The live unknown is consequently sharper than ordinary node spacing: it is **target-bearing local occupancy in the actual zeta zero plane**. A source theorem controlling that occupancy would be genuinely new arithmetic input; the zero count and zero-free region currently imported into this line do not provide it.