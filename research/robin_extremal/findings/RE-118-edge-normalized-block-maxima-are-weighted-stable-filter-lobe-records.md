# RE-118 — edge-normalized block maxima are weighted stable-filter lobe records

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + EDGE-NORMALIZED-BLOCK-MAXIMUM + MACROSCOPIC-RECOVERY + FORWARD-LOBE-RECORD + SYNDETIC-COMPATIBILITY + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED`.

Assume the finite attained off-critical edge regime of `RE-113`--`RE-117`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
c:=1-\Theta\in(0,1/2),
\tag{1}
\]

and retain the actual edge stable-filter profile

\[
J(u)=F_\Theta(u)+G_\Theta(u),
\qquad
J'(u)=cJ(u)-F_\Theta(u).
\tag{2}
\]

`RE-115` chooses, on a finite positive CA block, the rightmost maximizer of the edge-normalized Robin amplitude

\[
B_\Theta(N)
:=X^c\log X\,\bigl(e^{h(N)}-1\bigr),
\qquad X:=\log N.
\tag{3}
\]

`RE-116` shows that its moving tangent is spectrally compatible with the exact diagonal equation `(uJ(u))'=0`, while `RE-117` shows that a subsequent macroscopic recovery corridor is a positive lobe of the same `J`. A remaining possible escape was that **global block maximality itself** might impose extra leading-edge information: an actual CA selector is not merely a compatible critical point followed by a zero; it is the rightmost largest value of (3) on its whole positive block.

At the attained finite edge this extra condition also collapses to the same one-dimensional stable-filter geometry.

Let `C` be the rightmost maximizer of `B_Theta` on a finite positive CA block, put

\[
Y:=\log C,
\qquad
U:=\log Y,
\qquad
q:=B_\Theta(C),
\tag{4}
\]

and assume along an unbounded family that

\[
\liminf q>0.
\tag{5}
\]

Let `D` be the first later CA state with `h(D)<=0`, put `V=log D`, and assume the surviving macroscopic-recovery regime

\[
V\le AY
\tag{6}
\]

for one fixed `A>1`. Write

\[
r_Y:=\log(V/Y).
\tag{7}
\]

Then, uniformly for every later crossed CA state `N` before or at `D`, with

\[
X:=\log N,
\qquad
t:=\log(X/Y)\in[0,r_Y],
\tag{8}
\]

one has

\[
\boxed{
B_\Theta(N)
=
\left(1+\frac tU\right)J(U+t)+o(1).
}
\tag{9}
\]

Moreover,

\[
\boxed{
J(U)=q+o(1),
\qquad
J'(U)+\frac{J(U)}U=o(1),
}
\tag{10}
\]

and the rightmost block-maximality plus first-recovery conditions imply the continuous forward-record packet

\[
\boxed{
\sup_{0\le t\le r_Y}
\left[
\left(1+\frac tU\right)J(U+t)-J(U)
\right]
\le o(1),
}
\tag{11}
\]

\[
\boxed{
J(U+r_Y)=o(1),
\qquad
\inf_{0\le t<r_Y}J(U+t)\ge-o(1).
}
\tag{12}
\]

In particular, after multiplying (11) by `U`, the actual edge-normalized block maximum is, to leading edge resolution, a **forward record of the weighted stable-filter state**

\[
u\longmapsto uJ(u)
\tag{13}
\]

inside the positive lobe that ends at the first recovery.

This stronger packet is still spectrally noncoercive. There exist constants

\[
U_0>0,
\qquad L<\infty,
\qquad 0<\delta<R<\infty,
\qquad m>0,
\tag{14}
\]

and a syndetic set of phases `u>=U_0` such that, if `r(u)` is the first zero of `J` to the right of `u`, then

\[
\boxed{
(uJ(u))'=0,
\qquad J(u)\ge m,
\qquad \delta\le r(u)\le R,
}
\tag{15}
\]

\[
\boxed{
J(u+s)>0\quad(0\le s<r(u)),
\qquad J(u+r(u))=0,
}
\tag{16}
\]

and, exactly rather than asymptotically,

\[
\boxed{
(u+s)J(u+s)\le uJ(u)
\quad(0\le s\le r(u)).
}
\tag{17}
\]

Thus the actual attained edge face already contains, with bounded gaps, exact packets that simultaneously satisfy the self-consistent moving endpoint ray of `RE-116`, a positive first-recovery lobe as in `RE-117`, and the stronger forward weighted-record condition forced by rightmost block maximality.

Consequently, **leading-order block extremality does not provide the missing arithmetic selector coordinate**. In the finite attained-edge branch, a closing argument must resolve placement below the `Y^{-c}/log Y` edge scale, constrain the discrepancy between the discrete CA maximizer and the corresponding weighted lobe record, or import source information not reconstructible from `J`.

## 1. The selector-free recovery expansion applies to the edge-normalized block maximum

The macroscopic quadrature expansion proved in Section 1 of `RE-117` is selector-free. For any two crossed CA states whose logarithmic sizes remain in one fixed multiplicative range it gives, uniformly,

\[
Y^cU\,\bigl(h(C)-h(N)\bigr)
=
\int_0^t e^{-cs}F_\Theta(U+s)\,ds+o(1).
\tag{18}
\]

The fixed-`b` hypothesis enters `RE-117` only later, when its starting height is identified with `J(U)`. For the present starting state that identification instead comes from `RE-115`.

Indeed, under (5), `RE-115` proves

\[
q\asymp1,
\qquad
F_\Theta(U)=cq+o(1),
\qquad
G_\Theta(U)=\Theta q+o(1).
\tag{19}
\]

Therefore

\[
\boxed{J(U)=q+o(1).}
\tag{20}
\]

Since `q=O(1)`, equation (3) gives

\[
h(C)=O\!\left(\frac{Y^{-c}}U\right),
\tag{21}
\]

and hence

\[
Y^cU\,h(C)=q+o(1)=J(U)+o(1).
\tag{22}
\]

The exact stable-filter splitting identity

\[
J(U)
=
\int_0^t e^{-cs}F_\Theta(U+s)\,ds
+e^{-ct}J(U+t)
\tag{23}
\]

combined with (18) and (22) yields

\[
\boxed{
Y^cU\,h(N)
=e^{-ct}J(U+t)+o(1)
}
\tag{24}
\]

uniformly on the whole corridor (8).

Because `J` is bounded, (24) also gives `h(N)=O(Y^{-c}/U)` uniformly. Thus

\[
e^{h(N)}-1=h(N)+O(h(N)^2),
\tag{25}
\]

and the quadratic term is negligible after the normalization (3):

\[
X^c\log X\,h(N)^2
=O\!\left(\frac{Y^{-c}}U\right)=o(1).
\tag{26}
\]

Since `X=Ye^t` and `log X=U+t`, substituting (24) into (3) proves (9):

\[
B_\Theta(N)
=Y^ce^{ct}(U+t)
\left[
\frac{e^{-ct}J(U+t)+o(1)}{Y^cU}
\right]+o(1)
=
\left(1+\frac tU\right)J(U+t)+o(1).
\tag{27}
\]

No new smoothing or continuous surrogate has been introduced: the only analytic input is the exact event-mass quadrature already audited in `RE-117`.

## 2. Rightmost block maximality becomes a forward weighted-record condition

Every CA state after `C` and before `D` belongs to the same positive block. Since `C` is a block maximizer,

\[
B_\Theta(N)\le q
\tag{28}
\]

for every such state. Equations (9) and (20) therefore give on the discrete crossed-state phases `t_j`, uniformly,

\[
\left(1+\frac{t_j}U\right)J(U+t_j)
\le J(U)+o(1).
\tag{29}
\]

`RE-117` proves that the crossed CA states form an `o(1)` mesh in the logarithmic phase `t`: the largest simultaneous event mass is `o(Y)`. Since `J` is uniformly continuous and the weight `1+t/U` varies uniformly continuously on the fixed interval `[0,log A]`, (29) extends from the CA mesh to every `t in [0,r_Y]`. This is (11).

The first-recovery argument of `RE-117` applies unchanged to (24). The crossing overshoot is `o(1)` after edge normalization, while every earlier crossed CA state has positive Robin height. Hence (12) follows.

Condition (5) and (20) also give a uniform positive starting amplitude. Since `J'` is bounded, (12) forces `r_Y` to be bounded away from zero, while (6) gives `r_Y<=log A`. Thus the actual packet occupies a genuine fixed-width phase scale rather than collapsing to one point.

Finally, (19), (20), and the exact identity `J'=cJ-F_Theta` imply

\[
J'(U)=o(1).
\tag{30}
\]

As `J(U)=O(1)` and `U\to\infty`,

\[
\boxed{
J'(U)+\frac{J(U)}U=o(1),
}
\tag{31}
\]

which is the second relation in (10). By `RE-116`, the left-hand side is exactly the self-consistent moving-ray residual. Thus the block maximum is not merely a forward record: at leading edge resolution it also lies on the same weighted-critical geometry already isolated by the moving tangent.

The argument deliberately does **not** infer an `o(1/U)` error or a second-derivative sign. The edge projection only supplies `o(1)` control here; claiming finer localization of the discrete CA maximizer would require precisely the lower-order source information still missing from the line.

## 3. Exact weighted lobe records are syndetic in the actual edge profile

It remains to test whether (11)--(12), together with the moving-ray condition, distinguish the actual zeta edge face from its own almost-periodic recurrence. They do not.

From `RE-114`--`RE-117`, `J` is a nonzero real `C^1` uniformly almost-periodic function with zero Bohr mean, and both `J` and `J'` are bounded. Therefore `J` takes both positive and negative values. Uniform almost-periodicity upgrades one positive value and one negative value to relatively dense sign-margin sets: there exist

\[
m_+>0,
\qquad m_->0,
\qquad L_+,L_-<\infty
\tag{32}
\]

such that every sufficiently long interval of length `L_+` contains `v` with

\[
J(v)\ge m_+,
\tag{33}
\]

and every interval of length `L_-` contains a point where

\[
J\le-m_-.
\tag{34}
\]

Take a sufficiently large positive-margin point `v` and let `(a_v,d_v)` be the connected component of `{J>0}` containing it. The negative recurrence (34) bounds both sides of this component uniformly:

\[
v-a_v\le L_-+O(1),
\qquad
d_v-v\le L_-+O(1).
\tag{35}
\]

On the compact closure `[a_v,d_v]`, consider

\[
H(x):=xJ(x).
\tag{36}
\]

For large positive `v`, `H(v)>0`, while

\[
H(a_v)=H(d_v)=0.
\tag{37}
\]

Let `u_v` be the **rightmost global maximizer** of `H` on this component. Then `u_v` is interior, so

\[
\boxed{(u_vJ(u_v))'=0.}
\tag{38}
\]

By rightmost global maximality,

\[
\boxed{
(u_v+s)J(u_v+s)\le u_vJ(u_v)
\quad(0\le s\le d_v-u_v),
}
\tag{39}
\]

and by definition of the positive component,

\[
J(u_v+s)>0
\quad(0\le s<d_v-u_v),
\qquad
J(d_v)=0.
\tag{40}
\]

The maximizer has a uniform amplitude floor. Indeed `u_v=v+O(1)` by (35), and

\[
u_vJ(u_v)\ge vJ(v)\ge vm_+,
\tag{41}
\]

so for all sufficiently large `v`,

\[
J(u_v)\ge \frac{m_+}{2}.
\tag{42}
\]

Let

\[
B:=\sup|J'|<\infty.
\tag{43}
\]

Since `J(d_v)=0`, the mean-value theorem and (42) give the uniform lower bound

\[
d_v-u_v\ge \frac{m_+}{2B}.
\tag{44}
\]

The upper bound follows from (35). Hence, after renaming constants,

\[
\delta\le d_v-u_v\le R.
\tag{45}
\]

Finally the positive-margin points `v` are syndetic, while `u_v-v=O(1)` uniformly. By applying the positive recurrence inside a fixed right-shifted subinterval, the resulting `u_v` themselves form a syndetic set. Taking

\[
r(u_v):=d_v-u_v
\tag{46}
\]

proves (14)--(17).

At every such exact weighted maximum, `RE-116` turns (38) into the exact moving endpoint ray

\[
b(u)G_\Theta(u)-(1-b(u))F_\Theta(u)=0,
\qquad
b(u)=c+\frac1u.
\tag{47}
\]

Thus the spectral control satisfies a strictly stronger version of the actual leading packet: exact weighted criticality, exact forward record maximality, exact positivity up to the first zero, a uniform amplitude floor, and bounded first-zero distance.

## 4. Representation audit and matched control

The object under test is the edge-normalized positive CA block together with its rightmost `B_Theta` maximizer and subsequent first recovery. The target is whether block extremality contributes a source coordinate independent of the leading edge state `J`. Translation in logarithmic phase, overall edge amplitude, and the vanishing `1/U` drift are nuisance variation; the controls are the exact moving-ray identity of `RE-116` and the macroscopic event-staircase profile of `RE-117`.

Equation (9) is the decisive representation reduction: after those controls, the whole forward block segment is reconstructed from the single scalar function `J` by the known weight `(U+t)/U`. Equation (11) is therefore not a new coordinate; it is an order condition on a known one-dimensional profile.

A matched single-frequency control makes the no-go explicit. Take

\[
J(u)=A\cos(\gamma u+\phi),
\qquad A>0.
\tag{48}
\]

On each sufficiently late positive cosine lobe, `uJ(u)` has an interior global maximum satisfying

\[
\cos(\gamma u+\phi)
-\gamma u\sin(\gamma u+\phi)=0,
\tag{49}
\]

equivalently

\[
\tan(\gamma u+\phi)=\frac1{\gamma u}.
\tag{50}
\]

That point is the exact moving-ray root, is the forward weighted record until the next cosine zero, has order-one positive amplitude, and its first-zero distance tends to `pi/(2|gamma|)`. These packets recur periodically. The full actual edge profile needs only uniform almost-periodicity, not any special multi-frequency cancellation, to reproduce the same geometry syndetically.

There is therefore no decisive mismatch at leading edge order.

## 5. Prior-art boundary and consequence

The fresh prior-art audit found current 2026 work on Robin's inequality that organizes CA counterexamples through explicit windows, smoothing identities, or the exact prime-layer workload, including the Mantovanelli workload framework already anchored in `SOURCES.md`. Those sources do not identify the hypothetical finite attained zeta edge with the edge-normalized CA block maximum, nor do they classify the block-maximality plus first-recovery packet as a weighted almost-periodic stable-filter lobe record. No new external theorem is load-bearing here, so `SOURCES.md` requires no change.

The novelty claim is deliberately narrow. Almost-periodic recurrence, existence of maxima on bounded positive components, and the calculus identity `(uJ)'=J+uJ'` are classical. The line-specific content is the combination of:

1. the selector-free event-staircase recovery expansion from `RE-117`;
2. the edge-normalized CA block maximizer and endpoint source projection from `RE-115`;
3. the resulting uniform identity (9) for the actual block objective itself;
4. the reduction of rightmost block maximality to the forward weighted-record condition (11); and
5. the proof that the actual attained edge face realizes exact stronger weighted-record/recovery packets syndetically.

This closes a real leading-order escape after `RE-117`. The phrase **arithmetic selector placement** can no longer mean merely that the chosen CA state is the largest edge-normalized Robin value in its positive block: that condition is already encoded by a weighted lobe record of `J` and has exact syndetic spectral controls. A future finite-edge closing theorem must detect the discrete placement error relative to those lobe records, exploit a finer recovery constant than the `o(1)` edge profile retains, or use lower-order arithmetic data not determined by `J`.