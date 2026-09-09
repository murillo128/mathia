# PC-224 — new-prime-coordinate leakage is fiberwise conditional variance

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` for the most direct cross-level escape left open by PC-223: transport an old state through a canonical coprime prime refinement, apply the source cyclotomic mask at the refined level, and retain the entire sector carrying the new prime coordinate rather than compressing immediately to prime-primary axes.

That escape is genuinely larger than the prime-axis state space, but a single refinement followed by a single diagonal mask still does not create a relational mixed-conductor operator. Under the canonical CRT identification, the full old-to-new leakage splits into independent fibers over the coarse level, and its positive square is exactly multiplication by the **fiberwise conditional variance** of the mask. Consequently its singular spectrum, rank, Schatten norms, and every observable depending only on `L^*L` are classified by one scalar profile on the old level. For the cyclotomic source mask that profile is a residue-class second-moment statistic of the coefficients of `Phi_{qN}`.

This does **not** prove that the variance profile itself is arithmetically trivial. It closes the operator architecture in which one refines once, applies one source mask, keeps all new-prime sectors, and then forgets their internal exact-order labels through singular-value or `L^*L` data. A surviving cross-level mechanism must retain more structure, for example exact-order projectors between multiple masks, path labels through repeated refinements, or an intrinsic operation coupling distinct coarse fibers before the new-prime information is compressed.

## 1. Canonical old/new decomposition under a prime refinement

Let `q` be prime with `q \nmid N`, and put

\[
H_m:=L^2(\mathbb Z/m\mathbb Z)
\]

with normalized counting measure. Reduction modulo `N` gives the canonical isometric pullback

\[
J_{N,qN}:H_N\longrightarrow H_{qN},
\qquad
(J_{N,qN}f)(x)=f(x\bmod N).
\tag{1}
\]

CRT identifies

\[
\mathbb Z/qN\mathbb Z\cong
\mathbb Z/q\mathbb Z\times\mathbb Z/N\mathbb Z.
\]

Writing a point as `(a,y)`, (1) becomes

\[
(J_{N,qN}f)(a,y)=f(y).
\tag{2}
\]

Thus the old subspace is precisely the space of functions independent of the new `q` coordinate. Let

\[
E_q:=J_{N,qN}J_{N,qN}^*.
\tag{3}
\]

Then `E_q` is the orthogonal projection, equivalently the finite conditional expectation, onto the old subspace:

\[
(E_qF)(a,y)=\frac1q\sum_{b\bmod q}F(b,y).
\tag{4}
\]

In Fourier coordinates, `E_q` keeps exactly the frequencies whose `q`-coordinate is zero. Therefore `(I-E_q)H_{qN}` is the direct sum of **all** exact-order Fourier sectors whose conductor is divisible by `q`; no mixed `q`-containing conductor is discarded at this stage.

Let `g` be any mask on `Z/qNZ`, let `M_g` denote multiplication by `g`, and define the one-step old-to-new leakage operator

\[
L_{N,q}(g)
:=(I-E_q)M_gJ_{N,qN}.
\tag{5}
\]

This is the most direct realization of the post-PC-223 proposal "transport the mixed state through refinement before collapsing to prime axes" when the only source insertion at the refined level is one multiplication mask.

## 2. Exact conditional-variance reduction

For each coarse point `y`, write the `q`-fiber of the mask as

\[
g_y(a):=g(a,y),
\qquad
\bar g(y):=\frac1q\sum_{a\bmod q}g_y(a).
\tag{6}
\]

Equations (2)--(5) give directly

\[
\boxed{
(L_{N,q}(g)f)(a,y)
=
\bigl(g_y(a)-\bar g(y)\bigr)f(y).
}
\tag{7}
\]

The fibers for distinct `y` are orthogonal. Hence

\[
\boxed{
L_{N,q}(g)^*L_{N,q}(g)=M_{v_{N,q}(g)},
}
\tag{8}
\]

where

\[
\boxed{
v_{N,q}(g)(y)
=
\frac1q\sum_{a\bmod q}|g_y(a)|^2
-
|\bar g(y)|^2
=
\frac1q\sum_{a\bmod q}|g_y(a)-\bar g(y)|^2.
}
\tag{9}
\]

Thus the positive square is exactly the conditional variance of `g` along the new prime coordinate. In particular,

\[
\operatorname{Spec}_{\mathrm{sing}} L_{N,q}(g)
=
\{\sqrt{v_{N,q}(g)(y)}:y\bmod N\},
\tag{10}
\]

with zeros included with multiplicity, and

\[
\operatorname{rank}L_{N,q}(g)
=
\#\{y:v_{N,q}(g)(y)>0\}
\le N.
\tag{11}
\]

The whole new-prime subspace has dimension `(q-1)N`, yet one mask acting on one old scalar per coarse fiber can excite at most one direction in each `(q-1)`-dimensional new fiber.

If `g` is normalized by `||g||_{H_{qN}}=1`, then the total leakage energy is

\[
\boxed{
\frac1N\operatorname{tr}\bigl(L_{N,q}(g)^*L_{N,q}(g)\bigr)
=
1-\|E_qg\|_{H_{qN}}^2.
}
\tag{12}
\]

So even the total old-to-new transfer is just the Pythagorean variance left after conditional expectation.

## 3. Source cyclotomic mask

Let

\[
\Phi_{qN}(z)=\sum_{r=0}^{qN-1}a_{qN}(r)z^r,
\qquad
h_{qN}:=\sum_{r=0}^{qN-1}a_{qN}(r)^2,
\tag{13}
\]

where coefficients beyond the degree are padded by zero, and use the normalized coefficient mask from the common-refinement line,

\[
g_{qN}(r):=\sqrt{\frac{qN}{h_{qN}}}\,a_{qN}(r).
\tag{14}
\]

For a fixed residue `y mod N`, the `q` lifts are `y+tN`, `0<=t<q`. Substituting (14) into (9) gives the exact source profile

\[
\boxed{
v_{N,q}(y)
=
\frac{N}{h_{qN}}
\left[
\sum_{t=0}^{q-1}a_{qN}(y+tN)^2
-
\frac1q
\left(\sum_{t=0}^{q-1}a_{qN}(y+tN)\right)^2
\right].
}
\tag{15}
\]

The first folded moment

\[
S_{N,q}(y):=\sum_{t=0}^{q-1}a_{qN}(y+tN)
\tag{16}
\]

is the coefficient vector of `Phi_{qN}` reduced modulo `z^N-1`. Its discrete Fourier transform is therefore the vector of root values

\[
\Phi_{qN}(\zeta_N^k),
\qquad k\bmod N,
\tag{17}
\]

placing that part of (15) next to the root-value transfer already classicalized in PC-216 and PC-217. But (15) also contains the folded square statistic

\[
T_{N,q}(y):=\sum_{t=0}^{q-1}a_{qN}(y+tN)^2,
\tag{18}
\]

which is not determined by the linear fold (16) alone. Therefore the correct conclusion is **not** that the source profile has collapsed completely to previous root-value or Ramanujan data. The exact reduction is instead

\[
\boxed{
\text{one-step all-new-sector leakage}
\quad\longrightarrow\quad
\text{one scalar cyclotomic coefficient-variance profile on }\mathbb Z/N\mathbb Z.
}
\tag{19}
\]

The arithmetic question, if pursued further, has moved from a mixed-sector operator to the residue-class statistic (15).

For reference, (12) becomes

\[
\|E_qg_{qN}\|^2
=
\frac1{q h_{qN}}
\sum_{y\bmod N}S_{N,q}(y)^2,
\tag{20}
\]

so the total leakage knows only the global folded-square norm, while the full singular spectrum knows the pointwise variances (15).

## 4. Matched-mask control and exact information loss

The reduction is not special to cyclotomic masks. For fixed `N,q`, let `g` and `h` be any two masks satisfying

\[
v_{N,q}(g)(y)=v_{N,q}(h)(y)
\qquad\text{for every }y\bmod N.
\tag{21}
\]

For each `y`, the centered fiber vectors

\[
g_y-\bar g(y)\mathbf1,
\qquad
h_y-\bar h(y)\mathbf1
\]

lie in the same `(q-1)`-dimensional space `\mathbf1^\perp` and have the same norm. Hence there is a unitary `U_y` on that fiber taking one to the other. Their direct sum `U=\bigoplus_yU_y` gives

\[
\boxed{
L_{N,q}(h)=U L_{N,q}(g).
}
\tag{22}
\]

Thus any invariant which forgets the distinguished internal exact-order decomposition after the leakage—singular values, `L^*L`, rank, Schatten norms, or a scalar determinant built only from `L^*L`—cannot distinguish the cyclotomic mask from an arbitrary matched mask with the same variance profile. The apparent transport into many mixed exact-order sectors is therefore not by itself a new arithmetic operator invariant.

This is also the decisive boundary of the statement. The fiber unitary in (22) need not preserve the exact-order Fourier projectors inside `(I-E_q)H_{qN}`. Consequently, inserting such projectors **before** the information is collapsed, or applying another noncommuting source operator which distinguishes those directions, can retain information absent from (8). PC-224 does not rule out that stronger architecture.

## 5. Relation to the existing Prime-Circle boundary

PC-212 identified the canonical common-refinement embedding and exact-order/Haar organization. PC-221 showed that summing all lower-conductor Feshbach paths at one level collapses back to compressed mask data. PC-223 then showed that repeatedly returning through the common-anchor Mangoldt prime axes is blind to the middle of the mixed-conductor lattice and explicitly left transport of mixed sectors through refinement as a survivor.

Equation (8) tests the simplest such survivor without prematurely projecting to a prime axis: **keep the entire new-`q` complement**. Nevertheless, after one multiplication mask, the CRT geometry makes the map an orthogonal family of independent fiber stars. There is no coupling between distinct coarse points `y`, and the large mixed-conductor codomain contributes only one active direction per fiber unless additional structure is interrogated before compression.

Accordingly, this closes the route

\[
\text{old state at }N
\to
\text{canonical refinement to }qN
\to
\text{one diagonal source mask}
\to
\text{all new-}q\text{ sectors}
\to
\text{singular/positive-square spectrum}
\tag{23}
\]

as a genuinely mixed operator mechanism for RH. It does **not** close:

- multiple masks separated by exact-order projectors or another noncommuting intrinsic operator;
- refinement networks of growing depth with path labels retained;
- source-forced couplings that mix distinct coarse fibers `y` before taking an invariant;
- a direct study of the scalar variance profile (15), provided it passes matched controls and a separate novelty audit rather than being wrapped spectrally by fiat.

## 6. Prior-art and novelty audit

The identity behind (8)--(12) is classical Hilbert-space probability: conditional expectation is the `L^2` orthogonal projection onto the coarse sigma-algebra, and the norm of the orthogonal complement is conditional variance. Therefore **the operator reduction itself is not a new abstract theorem**.

The arithmetic input in (15) belongs to the extensively studied theory of cyclotomic coefficients. Carlo Sanna, *A survey on coefficients of cyclotomic polynomials*, Expositiones Mathematicae 40:3 (2022), 469--494, DOI `10.1016/j.exmath.2022.03.002`, arXiv `2111.04034`, is already recorded in `research/prime_circle/SOURCES.md` as the broad coefficient-theory boundary. The novelty audit found no source using the particular old/new CRT leakage operator (5) or its variance reduction (15) as a zeta/RH mechanism.

This is therefore recorded as a **project-specific exact boundary**, not as a novelty claim for conditional variance or cyclotomic coefficient statistics. Its value is falsificatory: the first source-native attempt to carry *all* new-prime mixed sectors across one refinement still scalarizes unless their internal conductor labels are interrogated before taking a spectral invariant.

## Research consequence

The post-PC-223 frontier can be sharpened. Merely enlarging the intermediate state from prime-primary axes to the whole new-prime complement is insufficient when the cross-level word contains only one refinement and one diagonal mask. A viable next test must create interaction **between** the fiber directions before forgetting them. The cleanest source-forced candidates are repeated refinements with exact-order projectors retained between stages, or a second intrinsic operator whose CRT action is not diagonal fiber-by-fiber. Any proposed construction should be stress-tested against masks with the same conditional-variance profile to verify that it uses information beyond PC-224.