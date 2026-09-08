# XF-127 — terminal harmonic history admits colliding/simple matched pairs

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `TERMINAL-HARMONIC` + `FULL-HISTORY-NONIDENTIFIABILITY` + `COLLISION-MATCHED-CONTROL`. XF-126 shows that the terminal harmonic history `P_N(s)` is genuinely stronger than any proper sparse harmonic interface: its long-time tail recovers the first active Vieta shell and its magnitude. It left open the sharper adversarial question whether the **complete** scalar history `P_N(s)`, for all `s>=0`, might nevertheless detect collision geometry. It does not.

There are arbitrarily large periodic unit-circle targets, one with isolated double roots and one with all roots simple, whose terminal power-sum heat histories agree **exactly for every nonnegative heat time**. The construction is finite, explicit, and uses only the diagonal Vieta heat flow of XF-067.

## 1. A two-shell target whose terminal history sees only one phase product

Choose coprime integers

\[
1\le a<b<2a,
\tag{1}
\]

an integer `g>=1`, and set

\[
N=(a+b)g,
\qquad
r=ag,
\qquad
d=bg=N-r.
\tag{2}
\]

Then `r` and `d` are distinct and both satisfy

\[
\frac N3<r,d<\frac{2N}{3}.
\tag{3}
\]

For unit phases `U,V in S^1`, consider the unit-circle target polynomial

\[
E_{U,V}(z,0)
=(1+Uz^r)(1+Vz^d)
=1+Uz^r+Vz^d+UVz^N.
\tag{4}
\]

Each factor has all of its roots on the unit circle, hence so does their product. Under the exact periodic coefficient heat flow of XF-067,

\[
E_k(s)=E_k(0)e^{-\delta_k s},
\qquad
\delta_k=\frac{4\pi^2}{L^2}k(N-k),
\tag{5}
\]

we have `delta_r=delta_d`; write

\[
\delta:=\delta_r=\delta_d
=\frac{4\pi^2}{L^2}rd,
\qquad
q(s):=e^{-\delta s}.
\tag{6}
\]

Therefore

\[
E_{U,V}(z,s)
=1+Uqz^r+Vqz^d+UVz^N.
\tag{7}
\]

Newton's logarithmic identity gives

\[
\log E(z,s)
=\sum_{m\ge1}\frac{(-1)^{m-1}}mP_m(s)z^m.
\tag{8}
\]

Because both proper active degrees are strictly larger than `N/3`, no product of three or more proper active monomials can contribute to degree `N`. Since `r+d=N` and neither proper degree equals `N/2`, the only contributions to `[z^N] log E` are the linear terminal coefficient and the quadratic cross term. Hence, **exactly for every `s>=0`**,

\[
[z^N]\log E_{U,V}(z,s)
=UV-UVq(s)^2
=UV\left(1-e^{-2\delta s}\right).
\tag{9}
\]

Equivalently,

\[
\boxed{
P_N(s)
=(-1)^{N-1}N\,UV\left(1-e^{-2\delta s}\right),
\qquad s\ge0.
}
\tag{10}
\]

Thus the full terminal harmonic trajectory depends on `(U,V)` only through the product

\[
W:=UV.
\tag{11}
\]

The relative phase, which will control whether the two cyclic root sets intersect, is completely invisible to this scalar history.

## 2. Collision compatibility is an independent phase condition

A common root `zeta` of the two factors in (4) satisfies, after writing `y=zeta^g`,

\[
y^a=-U^{-1},
\qquad
y^b=-V^{-1}.
\tag{12}
\]

Since `gcd(a,b)=1`, such a common `y` exists if and only if

\[
\boxed{
V^a=(-1)^{a-b}U^b.
}
\tag{13}
\]

Indeed, necessity follows by raising the two equations in (12) to powers `b` and `a`. For sufficiency, let `A=-U^{-1}` and `B=-V^{-1}`; condition (13) is exactly `A^b=B^a`. Choose integers `m,n` with `ma+nb=1` and set `y=A^mB^n`. Then `y^a=A` and `y^b=B`. Uniqueness follows because the ratio of two solutions would have both its `a`-th and `b`-th powers equal to one.

Fixing the terminal-history parameter `W=UV`, condition (13) becomes

\[
\boxed{
U^{a+b}=(-1)^{a-b}W^a.
}
\tag{14}
\]

For each fixed `W`, there are exactly `a+b` special values of `U` satisfying (14), while every generic `U` with `V=W/U` violates it. In the compatible case the unique common `y` has exactly `g` preimages under `z^g=y`; consequently the two factors have exactly `g` common roots. Each factor is simple at every nonzero root, so these are `g` isolated **double** roots and all remaining roots are simple. In the incompatible case the two cyclic root sets are disjoint and all `N` roots are simple.

We have therefore proved the exact matched-pair statement:

\[
\boxed{
\begin{array}{c}
\text{same }N,r,d,W\\
\Downarrow\\
P_N^{\rm coll}(s)=P_N^{\rm simple}(s)
\quad\text{for every }s\ge0,
\end{array}
}
\tag{15}
\]

while the target collision geometries differ.

## 3. An explicit `2:3` family hides a fixed positive collision density

Take

\[
a=2,
\qquad b=3,
\qquad N=5g,
\qquad r=2g,
\qquad d=3g,
\qquad W=1.
\tag{16}
\]

For the colliding target choose

\[
U_{\rm c}=e^{i\pi/5},
\qquad
V_{\rm c}=e^{-i\pi/5}.
\tag{17}
\]

Then `U_c^5=-1`, which is exactly (14). For the simple target choose

\[
U_{\rm s}=V_{\rm s}=1,
\tag{18}
\]

for which `U_s^5=1`, so the compatibility condition fails. Both targets nevertheless have the identical complete terminal history

\[
\boxed{
P_N(s)
=(-1)^{N-1}N\left(1-e^{-2\delta s}\right),
\qquad
\delta=\frac{24\pi^2g^2}{L^2}.
}
\tag{19}
\]

The colliding target has exactly `g` double roots. Thus `2g` of its `N=5g` root slots participate in collisions:

\[
\boxed{
\text{collision-slot density}=\frac{2}{5}.
}
\tag{20}
\]

This density is fixed as `g to infinity`; the obstruction is not a single vanishing defect hidden in a large divisor.

## 4. The matched histories can have different transition status

Choose `g` even so that the resulting periodic degree is even, as in the matched-control setup used in XF-125. At the colliding target slice, the `g` common roots are isolated doubles. The local collision discriminant law used in XF-125 makes those pairs leave the real periodic divisor immediately under backward heat, while forward real-root preservation keeps the divisor real for `s>=0`. Hence this matched control has the target slice as its transition boundary,

\[
\Lambda_{\rm per}^{\rm coll}=0.
\tag{21}
\]

The simple matched target has only simple unit-circle roots at `s=0`. By continuity of the finite coefficient heat flow and openness of simple real-rootedness, all roots remain real on some interval `(-epsilon,0]`; together with forward preservation this gives

\[
\Lambda_{\rm per}^{\rm simple}<0.
\tag{22}
\]

Therefore

\[
\boxed{
P_N^{\rm coll}(s)
\equiv
P_N^{\rm simple}(s)
\text{ on }[0,\infty)
\quad\not\Longrightarrow\quad
\Lambda_{\rm per}^{\rm coll}
=
\Lambda_{\rm per}^{\rm simple}.
}
\tag{23}
\]

This answers the explicit adversarial question left by XF-126: **even the complete terminal harmonic heat history is not, by itself, a collision or transition identifier.**

## 5. Why the near-balanced two-shell regime matters

The support restriction in (3) is structural, not cosmetic. It is what makes the terminal logarithmic coefficient stop after the quadratic cross term. At the boundary `r=N/3`, for example, the cubic composition `r+r+r=N` enters `[z^N] log E` and can expose `U^3`; the history then need not collapse to the product `UV`. At the equal split `r=d=N/2`, the two proper coefficients merge into one shell and the relevant coefficient is `U+V`, again exposing relative phase information.

Thus XF-127 does **not** say that the terminal harmonic is useless. XF-126 remains sharp in showing that it recovers global Vieta-tail data invisible to proper sparse harmonics. The new point is subtler: the map from divisor geometry to that scalar tail still has a nontrivial phase fiber, and that fiber already crosses the collision discriminant.

Nor does this prove that every joint family of high-harmonic histories is blind. XF-125 gives a separate semigroup construction for sublinear collections of proper harmonics; XF-127 concerns one distinguished global scalar history and uses a different exact mechanism. Finally, this is a finite periodic matched-control obstruction, not a proof that the source-specific Xi high-degree terminal moment itself has both realizations.

## Prior-art audit

The ingredients used here are classical at the algebraic level: Newton identities, cyclic unit-circle factors, and the diagonal periodic coefficient heat flow. The general backward-heat/unitary-polynomial setting is already anchored in `SOURCES.md` through Kabluchko's unitary-Hermite work. A directed search for results coupling a complete terminal power-sum heat trajectory to collision identifiability did not reveal an external theorem matching the construction above. No external result is load-bearing for (9)--(23), so no source-ledger update is required.

## Consequence for `xi_flow`

The natural scalar repair suggested by XF-126 is now closed. Moving from sublinear proper-harmonic histories to the terminal harmonic `P_N(s)` genuinely recovers information, but **one complete global harmonic history still does not determine whether the target divisor lies on the collision boundary**. A positive interface must therefore combine terminal information with at least one independent cross-shell phase observable, or use a joint full-degree object whose fibers cannot cross the discriminant.

A particularly concrete next gate is to determine the smallest additional harmonic/history coordinate that breaks the `U,V` phase fiber in the near-balanced two-shell model. That is a finite algebraic observability question before any source-specific Xi estimate is attempted.