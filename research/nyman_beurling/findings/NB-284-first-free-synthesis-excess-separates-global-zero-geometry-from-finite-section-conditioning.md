# NB-284 — first-free synthesis excess separates global zero geometry from finite-section conditioning

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-280, NB-282, NB-283
- **Classification:** `EXACT-DERIVED + FIRST-FREE-JET-COST + BLASCHKE-DEFLATION + ZERO-GEOMETRY + SOURCE-CLOSURE + FINITE-SECTION-CONDITIONING + NB-283-REFINEMENT + ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-283` correctly factors first-free-jet neutralization through ordinary value interpolation after dividing by the finite packet Blaschke factor. It then defines the finite-section excess

\[
\mathfrak E_M(Z)
=
\mathcal C_M(Z)-\mathcal C_{\rm amb}(Z)
\ge 0,
\tag{1}
\]

where `C_M` is the least Nyman/Hardy norm attainable by the finite source section and `C_amb` is the unrestricted `H^2` interpolation cost at the packet.

There is, however, a structural refinement that matters before trying to price `(1)` arithmetically. Dividing by the finite packet factor removes only the selected packet zeros. Every actual Nyman source still carries **all other interior zeta zeros**. Therefore the quotient source space does not in general become ambient `H^2` when `M` tends to infinity. A persistent part of `E_M` can be forced by the remaining global zero geometry, and another persistent part can come from any further restriction of the infinite Nyman source closure beyond that zero divisor.

For a fixed packet the total excess splits exactly into three nonnegative pieces:

\[
\boxed{
\mathfrak E_M(Z)
=
\mathfrak G(Z)
+
\mathfrak S_\infty(Z)
+
\mathfrak A_M(Z)
}
\tag{2}
\]

with

\[
\mathfrak G(Z)
=
\mathcal C_{\rm geom}(Z)-\mathcal C_{\rm amb}(Z),
\tag{3}
\]

\[
\mathfrak S_\infty(Z)
=
\mathcal C_\infty(Z)-\mathcal C_{\rm geom}(Z),
\tag{4}
\]

and

\[
\mathfrak A_M(Z)
=
\mathcal C_M(Z)-\mathcal C_\infty(Z).
\tag{5}
\]

The first term is a **global remaining-zero geometry penalty**. The second is a possible **infinite-source closure penalty beyond the common zero divisor**. Only the third is the genuinely **finite-section/source-conditioning penalty**.

Moreover, for every fixed finite packet `Z`, once the first-free interpolation problem is feasible,

\[
\boxed{
\mathcal C_M(Z)\downarrow \mathcal C_\infty(Z),
\qquad
\mathfrak A_M(Z)\longrightarrow 0.
}
\tag{6}
\]

Thus finite-section conditioning cannot produce a persistent floor at a fixed packet. Any arithmetic obstruction of that kind must be a **rate/uniformity obstruction in a moving Ford regime** `Z=Z_X`, `M=M_X`, rather than a nonzero fixed-packet limit of the raw excess `(1)`.

The equations and finite-section reduction of `NB-283` remain valid. The new point is that its total excess should not be interpreted as a single finite-section arithmetic price.

---

## 1. Setup inherited from NB-283

Let

\[
Z=\{(\rho_j,m_j):1\le j\le N\}
\tag{7}
\]

be a finite packet of distinct nontrivial zeros of `zeta` lying strictly inside

\[
\mathbb C_{1/2}=\{s:\Re s>1/2\},
\tag{8}
\]

with actual multiplicities `m_j`.

Let

\[
B_Z(s)
=
\prod_{j=1}^N b_{\rho_j}(s)^{m_j}
\tag{9}
\]

be the finite half-plane Blaschke product carrying those packet multiplicities, with any unimodular normalization.

For a finite Dirichlet polynomial

\[
P(s)=\sum_{n\le M}a_n n^{-s},
\qquad
Q_P(s)=P(s)-P(1),
\tag{10}
\]

write the corresponding Nyman source component as

\[
F_P(s)
=
\frac{\zeta(s)}sQ_P(s).
\tag{11}
\]

Because `zeta` vanishes at every `rho_j` with multiplicity `m_j`, `NB-283` factors

\[
F_P=B_Zh_P,
\qquad
h_P\in H^2(\mathbb C_{1/2}),
\tag{12}
\]

and innerness of `B_Z` gives

\[
\|h_P\|_{H^2}=\|F_P\|_{H^2}.
\tag{13}
\]

The first-free-jet neutralization conditions become ordinary values

\[
h_P(\rho_j)=y_j,
\qquad
y_j=\frac{c_Z}{\rho_j},
\qquad |c_Z|=1,
\tag{14}
\]

where the common unimodular constant `c_Z` depends only on the normalization chosen for `B_Z`.

Define the sampling map

\[
L_Zh
=
\bigl(h(\rho_1),\ldots,h(\rho_N)\bigr).
\tag{15}
\]

For the finite quotient source space set

\[
V_{M,Z}
:=
\{h_P:\ P\text{ is supported on }n\le M\}.
\tag{16}
\]

The spaces are nested:

\[
V_{M,Z}\subseteq V_{M+1,Z}.
\tag{17}
\]

The finite-section cost from `NB-283` is exactly

\[
\mathcal C_M(Z)
:=
\inf\left\{
\|h\|_{H^2}^2:
 h\in V_{M,Z},\ L_Zh=y
\right\},
\tag{18}
\]

with the convention `C_M=+infinity` if that finite section is not yet feasible.

`NB-282` implies eventual feasibility, and in fact eventual surjectivity of the first-free value map: for each fixed packet there exists some finite `M_0` such that

\[
L_Z(V_{M_0,Z})=\mathbb C^N.
\tag{19}
\]

This fact will be the only finite-section interpolation input needed below.

---

## 2. The quotient sources still carry every unremoved interior zeta zero

The factorization `(12)` removes the selected packet divisor and nothing else.

Let `Z^rem` denote the multiset of all other zeros of `zeta` lying strictly in `C_{1/2}`, with their actual multiplicities, after deleting exactly the packet multiplicities in `(7)`.

For every finite source `P`, equation `(11)` shows that `F_P` vanishes at every point of `Z^rem` with at least the corresponding zeta multiplicity. Since `B_Z` is nonzero at every point not belonging to the selected packet, the quotient `h_P=F_P/B_Z` inherits those zeros with the same forced multiplicities.

Choose any nonzero quotient source `h_P`. Its interior zero set satisfies the standard Hardy-space Blaschke condition. Hence the common remaining divisor determines an inner half-plane Blaschke factor; denote it by

\[
C_Z.
\tag{20}
\]

Only interior zeros are included in `(20)`. Zeros on the boundary line `Re s=1/2` are not part of this factorization. If there are no remaining interior zeros, define

\[
C_Z\equiv1.
\tag{21}
\]

The unimodular normalization of `C_Z` is irrelevant to every norm and cost below.

Every finite quotient source is divisible by this common factor:

\[
V_{M,Z}\subseteq C_ZH^2(\mathbb C_{1/2}).
\tag{22}
\]

Now define the closed infinite-source quotient space by

\[
\mathcal H_Z^\infty
:=
\overline{\bigcup_{M\ge1}V_{M,Z}}^{\,H^2}.
\tag{23}
\]

Interior point evaluation and every fixed finite-order interior derivative evaluation are continuous on `H^2`. Therefore all the common zero and multiplicity constraints survive closure, giving

\[
\boxed{
V_{M,Z}
\subseteq
\mathcal H_Z^\infty
\subseteq
C_ZH^2
\subseteq
H^2.
}
\tag{24}
\]

This inclusion chain is the missing distinction in the raw excess `(1)`.

Nothing here asserts

\[
\mathcal H_Z^\infty=C_ZH^2.
\tag{25}
\]

That equality may or may not hold. The point of the decomposition below is precisely to avoid assuming it.

---

## 3. Four interpolation costs and the exact three-way decomposition

Besides the finite cost `(18)`, define the closed infinite-source cost

\[
\mathcal C_\infty(Z)
:=
\inf\left\{
\|h\|_{H^2}^2:
 h\in\mathcal H_Z^\infty,\ L_Zh=y
\right\},
\tag{26}
\]

the common-zero-geometry cost

\[
\mathcal C_{\rm geom}(Z)
:=
\inf\left\{
\|h\|_{H^2}^2:
 h\in C_ZH^2,\ L_Zh=y
\right\},
\tag{27}
\]

and the unrestricted ambient cost

\[
\mathcal C_{\rm amb}(Z)
:=
\inf\left\{
\|h\|_{H^2}^2:
 h\in H^2,\ L_Zh=y
\right\}.
\tag{28}
\]

Eventual surjectivity `(19)` makes all three constrained costs finite for the fixed packet. From `(24)`,

\[
\boxed{
\mathcal C_M(Z)
\ge
\mathcal C_\infty(Z)
\ge
\mathcal C_{\rm geom}(Z)
\ge
\mathcal C_{\rm amb}(Z).
}
\tag{29}
\]

Subtracting `C_amb` and inserting the two intermediate costs yields the exact identity

\[
\begin{aligned}
\mathfrak E_M(Z)
&=\mathcal C_M-\mathcal C_{\rm amb}\\
&=(\mathcal C_{\rm geom}-\mathcal C_{\rm amb})
 +(\mathcal C_\infty-\mathcal C_{\rm geom})
 +(\mathcal C_M-\mathcal C_\infty).
\end{aligned}
\tag{30}
\]

Thus define

\[
\boxed{
\mathfrak G(Z)
:=
\mathcal C_{\rm geom}(Z)-\mathcal C_{\rm amb}(Z)
\ge0,
}
\tag{31}
\]

\[
\boxed{
\mathfrak S_\infty(Z)
:=
\mathcal C_\infty(Z)-\mathcal C_{\rm geom}(Z)
\ge0,
}
\tag{32}
\]

and

\[
\boxed{
\mathfrak A_M(Z)
:=
\mathcal C_M(Z)-\mathcal C_\infty(Z)
\ge0.
}
\tag{33}
\]

Equation `(30)` is exactly the claimed decomposition `(2)`.

The three terms have genuinely different meanings.

`G(Z)` is already present if the only persistent restriction on the infinite quotient source is the remaining zeta zero divisor. It is global zero geometry, not finite-section arithmetic.

`S_infty(Z)` measures whatever restriction remains after accounting for that common divisor. It is intentionally left as a separate term because proving `(25)` would itself be a substantial completeness statement about the Nyman source closure.

`A_M(Z)` is the transient cost of realizing the infinite-source feasible geometry inside the finite section. This is the term to which phrases such as **finite-section conditioning**, **cutoff cost**, or **finite arithmetic synthesis price** properly apply.

---

## 4. The global zero-geometry term has an explicit reduced-sampling formula

Let

\[
G_Z^{\rm red}
=
\left(
\frac1{\rho_j+\overline{\rho_k}-1}
\right)_{1\le j,k\le N}
\tag{34}
\]

be the ordinary half-plane reproducing-kernel Gram at the distinct packet sites, exactly as in `NB-283`.

Then

\[
\mathcal C_{\rm amb}(Z)
=
y^*(G_Z^{\rm red})^{-1}y.
\tag{35}
\]

Because the packet multiplicities were removed from the remaining divisor, none of the selected `rho_j` is a zero of `C_Z`. Hence

\[
C_Z(\rho_j)\ne0.
\tag{36}
\]

Write every element of the geometry space as

\[
h=C_Zg.
\tag{37}
\]

Multiplication by the inner function `C_Z` is isometric, while the interpolation conditions become

\[
g(\rho_j)
=
\frac{y_j}{C_Z(\rho_j)}.
\tag{38}
\]

Define

\[
d_j
:=
\frac{y_j}{C_Z(\rho_j)}.
\tag{39}
\]

Ordinary minimum-norm interpolation therefore gives

\[
\boxed{
\mathcal C_{\rm geom}(Z)
=
d^*(G_Z^{\rm red})^{-1}d.
}
\tag{40}
\]

Consequently

\[
\boxed{
\mathfrak G(Z)
=
d^*(G_Z^{\rm red})^{-1}d
-y^*(G_Z^{\rm red})^{-1}y
\ge0.
}
\tag{41}
\]

The nonnegativity in `(41)` is guaranteed by the subspace inclusion `C_ZH^2 subset H^2`; it need not be read off entrywise from the two vectors.

This formula exposes a mechanism invisible in the ambient cost. If an unremoved interior zero is pseudohyperbolically close to a selected packet site, then the modulus of the remaining inner factor at that site can be small, so the renormalized datum `d_j=y_j/C_Z(rho_j)` can be much larger than the ambient datum `y_j`. Whether that produces an order-one or larger penalty in a Ford packet still depends on the full inverse Gram and cannot be inferred from one factor alone.

If there are no remaining interior zeta zeros, then `C_Z=1`, `d=y`, and

\[
\mathfrak G(Z)=0.
\tag{42}
\]

No statement here assumes either the existence or the absence of such remaining interior zeros.

---

## 5. The genuine finite-section gap vanishes for every fixed packet

The key additional fact is that `A_M(Z)` cannot persist at fixed `Z`.

### Proposition

For every fixed packet `Z`,

\[
\mathcal C_M(Z)\downarrow\mathcal C_\infty(Z)
\qquad(M\to\infty),
\tag{43}
\]

and hence

\[
\boxed{
\mathfrak A_M(Z)\to0.
}
\tag{44}
\]

### Proof

By `(17)`, the feasible finite spaces are nested, so once feasible the sequence `C_M(Z)` is nonincreasing. Since `V_{M,Z} subset H_Z^infty`,

\[
\mathcal C_M(Z)\ge\mathcal C_\infty(Z).
\tag{45}
\]

It remains to prove that every feasible infinite-source vector can be approximated by **feasible** finite-source vectors, not merely by arbitrary elements of the union.

From `NB-282`, choose `M_0` such that `(19)` holds. Because the range is finite dimensional, there exists a bounded linear right inverse

\[
R:\mathbb C^N\longrightarrow V_{M_0,Z}
\tag{46}
\]

satisfying

\[
L_ZR=I_{\mathbb C^N}.
\tag{47}
\]

Now take any

\[
h\in\mathcal H_Z^\infty,
\qquad L_Zh=y.
\tag{48}
\]

By definition `(23)`, choose finite-source vectors `v_q` with

\[
v_q\in V_{M_q,Z},
\qquad
v_q\to h
\quad\text{in }H^2.
\tag{49}
\]

Point evaluation at each fixed `rho_j` is bounded on `H^2`, so

\[
L_Zv_q\to L_Zh=y.
\tag{50}
\]

Correct the finite interpolation defect by

\[
\widetilde v_q
:=
v_q+R\bigl(y-L_Zv_q\bigr).
\tag{51}
\]

For `q` large enough that `M_q>=M_0`, nesting gives

\[
\widetilde v_q\in V_{M_q,Z}.
\tag{52}
\]

Equation `(47)` makes the correction exactly feasible:

\[
L_Z\widetilde v_q
=L_Zv_q+y-L_Zv_q
=y.
\tag{53}
\]

Since `R` is bounded and the defect in `(50)` tends to zero,

\[
\|\widetilde v_q-v_q\|_{H^2}
\le
\|R\|\,\|y-L_Zv_q\|
\longrightarrow0.
\tag{54}
\]

Together with `(49)`,

\[
\widetilde v_q\to h
\quad\text{in }H^2.
\tag{55}
\]

Thus every feasible vector in the closed infinite-source space can be approximated in norm by feasible finite-source vectors.

Given `epsilon>0`, choose `h` feasible with

\[
\|h\|^2
\le
\mathcal C_\infty(Z)+\epsilon.
\tag{56}
\]

Using `(55)`, a sufficiently large finite feasible vector satisfies

\[
\mathcal C_M(Z)
\le
\mathcal C_\infty(Z)+2\epsilon.
\tag{57}
\]

Combined with `(45)` and monotonicity, this proves `(43)` and `(44)`. `square`

The proof uses only fixed-packet boundedness. It gives **no uniform rate** in `Z`, in the packet height, in `N`, in Ford depth, or in the norm of the right inverse `(46)`.

That lack of uniformity is exactly where a finite-section arithmetic obstruction can still live.

---

## 6. What NB-283's excess is measuring after the split

The total quantity

\[
\mathfrak E_M(Z)
=
\mathcal C_M(Z)-\mathcal C_{\rm amb}(Z)
\tag{58}
\]

remains correct and useful. The refinement is semantic and structural: it mixes three distinct phenomena.

At fixed `Z`, `(43)` gives

\[
\lim_{M\to\infty}\mathfrak E_M(Z)
=
\mathfrak G(Z)+\mathfrak S_\infty(Z).
\tag{59}
\]

So any persistent limiting excess is **not** finite-section conditioning. It is already present in the infinite quotient-source problem.

Conversely,

\[
\boxed{
\mathfrak A_M(Z)
=
\mathfrak E_M(Z)
-
\mathfrak G(Z)
-
\mathfrak S_\infty(Z)
}
\tag{60}
\]

is the true finite-section remainder.

This matters directly for the research direction proposed after `NB-283`. A lower bound on the raw `E_M` would not by itself show that sparse Dirichlet neutralization is expensive. It could be detecting only the zeros that were never deflated, or a persistent restriction of the infinite Nyman closure.

To isolate source-native finite-section coercivity, one must either control/subtract the first two terms or compare the finite section directly with its own closed infinite-source limit.

---

## 7. The arithmetic question is therefore a moving-packet rate problem

The fixed-packet theorem `(43)` does **not** close the route relevant to the Ford regime.

There the packet itself moves with the scale:

\[
Z=Z_X,
\qquad
N=N_X,
\qquad
M=M_X.
\tag{61}
\]

The right inverse supplied by `NB-282` can become badly conditioned as the packet moves, and the amount of finite support required to approximate a near-minimizer in `H^infty_{Z_X}` can grow much faster than the available cutoff `M_X`.

The genuine finite-section target is therefore

\[
\boxed{
\mathfrak A_{M_X}(Z_X)
=
\mathcal C_{M_X}(Z_X)-\mathcal C_\infty(Z_X).
}
\tag{62}
\]

A durable order-one lower bound for `(62)` under the legal Nyman cutoff would be a real finite-section/source-conditioning obstruction. By contrast, an order-one lower bound only for

\[
\mathcal C_{M_X}(Z_X)-\mathcal C_{\rm amb}(Z_X)
\tag{63}
\]

would still be ambiguous until the global geometry and infinite-closure terms are separated.

This turns the vague question

> is first-free neutralization expensive?

into the sharper one

> how rapidly does the constrained finite quotient space approximate the constrained infinite quotient-source space, uniformly over Ford-scale packets?

That is the arithmetic conditioning problem left by `NB-282` and `NB-283`.

---

## 8. Adversarial audit

### 8.1 This does not refute the formulas of NB-283

The reduced sampling Gram, the finite-section Gram formula, and the nonnegative total excess in `NB-283` remain valid. `NB-284` refines the interpretation of that excess by inserting two mathematically natural intermediate spaces.

### 8.2 No completeness equality is assumed

The argument deliberately uses only

\[
\mathcal H_Z^\infty\subseteq C_ZH^2.
\tag{64}
\]

It does not assume or prove `H_Z^infty=C_ZH^2`. Any strictness is retained in the explicit term `S_infty(Z)`.

### 8.3 No hypothesis about RH is used

Only zeta zeros lying strictly inside `Re s>1/2` enter the Hardy-space inner factor `C_Z`. If the selected packet exhausts all such zeros, then `C_Z=1`. If other interior zeros exist, they contribute to the geometry term. Boundary zeros are not silently treated as interior Blaschke zeros.

### 8.4 Multiplicities are preserved

The common remaining divisor carries actual zeta multiplicities. Interior derivative evaluation is continuous in `H^2`, so those multiplicity constraints survive the closure in `(23)`.

### 8.5 Small finite sections may be infeasible

For such `M`, `C_M=+infinity` by definition. `NB-282` supplies a finite threshold after which surjectivity and hence feasibility hold. The convergence statement begins in that eventual regime.

### 8.6 Fixed-packet convergence is not uniform Ford convergence

Equation `(43)` is intentionally pointwise in the packet. It provides no estimate on the size of `M` required to make `A_M` small when `N`, height, separation, or Ford depth vary. Treating `(43)` as a uniform moving-packet theorem would erase the very arithmetic conditioning problem that remains open.

### 8.7 The normalization of the remaining Blaschke product is harmless

Replacing `C_Z` by `omega C_Z`, `|omega|=1`, multiplies every datum `d_j` in `(39)` by the same unimodular scalar. The quadratic interpolation cost `(40)` is unchanged.

---

## 9. Prior-art audit

A fresh search was made around Hardy-space Blaschke factorization, model/subspace interpolation, Burnol/Nyman zero sampling, and finite-section constrained interpolation.

The generic ingredients used here are classical: zeros of nonzero Hardy functions satisfy a Blaschke condition; multiplication by an inner function is isometric; point and finite-order interior derivative evaluations are bounded; and minimum-norm finite interpolation is controlled by the reproducing-kernel Gram.

The Nyman/Burnol zero-sampling background was already represented in this research line and in `SOURCES.md`. No new external theorem is load-bearing for the split `(30)` or for the fixed-packet convergence proof `(43)`, both of which are derived directly above. Therefore this pass adds no new source entry.

The research-specific contribution is the distinction between the ambient reduced-zero cost, the persistent global remaining-zero geometry, a possible extra infinite-source closure restriction, and the transient finite-section cost in the exact first-free-jet setup of `NB-283`.

---

## 10. Next frontier

The next useful computation should **not** attempt to lower-bound the raw first-free excess `E_M` and call the result finite-section arithmetic coercivity.

Instead, for a moving Ford packet `Z_X`, compare the legal finite source cutoff directly with the closed quotient-source problem and estimate

\[
\mathfrak A_{M_X}(Z_X).
\tag{65}
\]

There are two complementary ways to proceed.

First, obtain an explicit quantitative right inverse for the first-free sample map together with an `H^2` approximation rate from `H^infty_{Z_X}` into `V_{M_X,Z_X}`. The proof of `(43)` shows exactly which constants need uniform control.

Second, compute or bound the persistent baseline

\[
\mathfrak G(Z_X)+\mathfrak S_\infty(Z_X)
\tag{66}
\]

separately. In particular, `(41)` makes the remaining-zero geometry term explicit once the relevant interior zero configuration is specified. This prevents a global zero-divisor effect from being misidentified as sparse-source conditioning.

If `(65)` stays bounded below at Ford scale while `(66)` is accounted for, that would be a genuinely source-native obstruction. If `(65)` tends to zero within the legal cutoff, then first-free neutralization is not where the missing Nyman coercivity lives, even if the total excess `(58)` remains large.

---

## Conclusion

`NB-283` correctly identifies first-free neutralization as a reduced zero-sampling problem, but its total finite-versus-ambient excess mixes persistent and transient restrictions.

After the selected packet divisor is removed, every Nyman quotient source still carries every unremoved interior zeta zero. Introducing that common inner factor and the closed infinite quotient-source space gives the exact decomposition

\[
\mathfrak E_M
=
\mathfrak G
+
\mathfrak S_\infty
+
\mathfrak A_M.
\tag{67}
\]

For every fixed packet,

\[
\mathfrak A_M\to0.
\tag{68}
\]

Therefore a persistent fixed-packet excess cannot be attributed to finite-section conditioning. The real arithmetic problem is now sharply localized to the **uniform decay rate of `A_{M_X}(Z_X)` in the moving Ford regime**, after the persistent global zero geometry and infinite-source closure floor have been separated.