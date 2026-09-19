# FD-211 — Annulus-free gcd makes fixed root-filter families square-root complete

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** fixed collective signed root filters / bounded-source inversion / spectral dichotomy / RH criterion / route restriction
- **Depends on:** FD-206, FD-209, FD-210
- **Classification:** `EXACT-DERIVED + FIXED-FILTER-FAMILY + ANNULAR-GCD-DICHOTOMY + BOUNDED-SOURCE-INVERSION + RH-EQUIVALENCE + ROUTE-RESTRICTION`

## Claim

`FD-210` proves that a common characteristic root in the physical annulus

\[
\sqrt2<|\rho|\le2
\tag{1}
\]

is a genuine blind direction for every fixed finite family of signed root filters: even a `{-1,0,1}` source can then have super-square-root summatory growth while every filter is `O(1)`. The converse is also true at the level of bounded sources.

Let

\[
A(N)=\sum_{m\le N}u_m,
\qquad |u_m|\le C,
\qquad
\Delta(n)=A(2n)-A(n),
\qquad
(TF)(n)=F(2n),
\tag{2}
\]

where `C` is fixed. Let `P_1,...,P_r in C[z]` be a fixed finite family of nonzero polynomials, and let

\[
G=\gcd(P_1,\ldots,P_r)
\tag{3}
\]

up to a nonzero scalar. Then the following are equivalent.

1. `G` has no zero `rho` satisfying (1).
2. For every bounded source `(u_m)`, the implication

\[
\forall\varepsilon>0,\quad
|P_i(T)\Delta(n)|\ll_{\varepsilon,P_i,C} n^{1/2+\varepsilon}
\quad(1\le i\le r)
\tag{4}
\]

implies

\[
\forall\varepsilon>0,\quad
|A(N)|\ll_{\varepsilon,P_1,\ldots,P_r,C}N^{1/2+\varepsilon}.
\tag{5}
\]

Thus the gcd test of `FD-210` is not merely necessary. It exactly classifies **fixed finite polynomial root-filter families** for square-root completeness on bounded-coefficient sources.

For the physical Möbius source `u_m=mu(m)`, every `P_i(T)Delta` is an exact fixed signed combination of the root-aligned Farey sensors from `FD-206`. Consequently, whenever `G` has no zero in (1),

\[
\boxed{
\mathrm{RH}
\iff
\forall\varepsilon>0,\quad
|P_i(T)[M(2n)-M(n)]|
\ll_\varepsilon n^{1/2+\varepsilon}
\quad(1\le i\le r).
}
\tag{6}
\]

The reverse implication uses only `|mu(n)|<=1`; no Möbius multiplicativity or squarefree support is needed. The forward implication is the classical Mertens square-root criterion followed by finitely many dyadic shifts.

In particular, the fixed-family opening left by `FD-210` closes sharply. A common root in (1) makes the family genuinely blind even on bounded-alphabet sources. If there is no such common root, critical pointwise control of the family is already destination-complete. The remaining signed-filter escape must therefore change with scale, grow in degree, weaken the observation norm, or use another non-fixed/non-pointwise structure.

## 1. Every polynomial transform of the root increment has bounded binary sibling defect

The finite inversion below needs one piece of physical coherence that an arbitrary sequence on dyadic rays would not have. From (2),

\[
\Delta(n)=\sum_{n<m\le2n}u_m,
\]

so

\[
|\Delta(n)|\le Cn.
\tag{7}
\]

For every integer `h>=0`, the two intervals defining `Delta(n+h)` and `Delta(n)` differ in at most `3h` integer sites. Hence

\[
|\Delta(n+h)-\Delta(n)|\le3Ch.
\tag{8}
\]

Let

\[
R(z)=\sum_{j=0}^{d}r_jz^j
\]

be any fixed polynomial and put

\[
X(n)=R(T)\Delta(n)=\sum_{j=0}^{d}r_j\Delta(2^jn).
\tag{9}
\]

Equation (7) gives the linear growth bound

\[
|X(n)|\le C_R n.
\tag{10}
\]

More importantly, applying (8) with `h=2^j` gives

\[
\begin{aligned}
|X(2n+1)-X(2n)|
&\le
\sum_{j=0}^{d}|r_j|
|\Delta(2^j(2n+1))-\Delta(2^{j+1}n)|\\
&\le
3C\sum_{j=0}^{d}|r_j|2^j
=:B_R.
\end{aligned}
\tag{11}
\]

Thus every fixed polynomial transform of the physical root increment has a **uniform bounded sibling defect** on the binary tree. This is the general fixed-filter version of the odd-child control used in `FD-209`.

## 2. One characteristic factor is invertible outside the blind annulus

Consider a fixed complex number `a` and a sequence `X` satisfying (10)--(11). Put

\[
Y=(T-a)X,
\qquad
Y(n)=X(2n)-aX(n).
\tag{12}
\]

Assume, for every `eta>0`,

\[
|Y(n)|\ll_\eta n^{1/2+\eta}.
\tag{13}
\]

If

\[
|a|\le\sqrt2
\tag{14}
\]

then the binary-parent recurrence recovers `X` with square-root loss only. Write

\[
n_t=\left\lfloor\frac{N}{2^t}\right\rfloor,
\qquad
n_t=2n_{t+1}+b_t,
\qquad b_t\in\{0,1\}.
\]

By (11)--(12),

\[
X(n_t)=aX(n_{t+1})+Y(n_{t+1})+\epsilon_t,
\qquad
|\epsilon_t|\le B_R.
\tag{15}
\]

Fix `s=1/2+eta`. Iterating (15) to the terminal binary ancestor gives a forcing series bounded by

\[
N^s\sum_{t\ge0}
\left(\frac{|a|}{2^s}\right)^t.
\tag{16}
\]

For every `eta>0`, (14) makes the ratio strictly smaller than one. The terminal term is `O(N^{log_2|a|})=O(N^{1/2})`, and the accumulated sibling errors are also `O(N^{1/2})` up to an inessential logarithm when `|a|=1`. Hence

\[
|X(N)|\ll_\eta N^{1/2+\eta}.
\tag{17}
\]

At the exact boundary `|a|=sqrt2`, an exact `N^{1/2}` forcing estimate would acquire at most a logarithm; the `+epsilon` criterion absorbs it automatically.

There is a second invertible regime. If

\[
|a|>2,
\tag{18}
\]

iterate (12) forward:

\[
X(n)
=a^{-J}X(2^Jn)
-
\sum_{j=0}^{J-1}a^{-j-1}Y(2^jn).
\tag{19}
\]

By the linear source bound (10), the first term tends to zero as `J->infinity`, because

\[
|a|^{-J}|X(2^Jn)|\ll n\left(\frac2{|a|}\right)^J.
\]

Choose `eta>0` small enough that `2^(1/2+eta)<|a|`. Then the infinite forcing series in (19) converges geometrically and again gives (17).

Therefore a first-order characteristic factor can fail this bounded-source square-root inversion only in the intermediate region

\[
\boxed{\sqrt2<|a|\le2.}
\tag{20}
\]

The two endpoints have distinct meanings. `sqrt2` is the dyadic eigenvalue of square-root growth; `2` is the largest homogeneous dyadic growth compatible with the linear bound forced by bounded source increments. This is exactly the annulus found constructively in `FD-210`.

## 3. Factor-by-factor inversion proves sufficiency of the gcd test

Suppose now that `G` from (3) has no root in (20). Bézout's identity supplies fixed polynomials `Q_1,...,Q_r` such that

\[
G=\sum_{i=1}^{r}Q_iP_i.
\tag{21}
\]

If every filtered observable satisfies (4), then each finite dyadic shift preserves the same power exponent, so

\[
G(T)\Delta(n)\ll_\varepsilon n^{1/2+\varepsilon}
\qquad(\forall\varepsilon>0).
\tag{22}
\]

Factor `G` over `C`:

\[
G(z)=c\prod_{j=1}^{d}(z-a_j).
\tag{23}
\]

Repeated roots are allowed. By hypothesis each `a_j` satisfies either

\[
|a_j|\le\sqrt2
\qquad\text{or}\qquad
|a_j|>2.
\tag{24}
\]

Strip the factors in (23) one at a time. At every step the unknown sequence has the form

\[
X=R(T)\Delta
\]

for a fixed polynomial `R`, so the linear growth and bounded sibling-defect estimates (10)--(11) remain available. Section 2 therefore converts a square-root-plus-epsilon estimate for `(T-a_j)X` into the same type of estimate for `X`.

Because the number of factors is fixed, no exponent accumulates. For a prescribed final `epsilon>0`, choose one sufficiently small intermediate `eta>0`; all low-root geometric ratios in (16) are then strictly contracting, and all high-root series in (19) converge because their moduli exceed `2`. After all factors have been removed,

\[
\boxed{
|\Delta(n)|\ll_\varepsilon n^{1/2+\varepsilon}.
}
\tag{25}
\]

This also shows why merely requiring the filters to be coprime is unnecessarily strong. If `G=1`, (21) recovers `Delta` directly. Common roots are harmless as long as they lie at or below the RH radius `sqrt2`, or outside the bounded-source radius `2`; only the intermediate annulus creates an admissible supercritical mode.

## 4. Root increments recover the whole bounded-source summatory function

It remains to pass from (25) to (5). If `N=2n+b` with `b in {0,1}`, then

\[
A(N)=A(n)+\Delta(n)+b\,u_{2n+1}.
\tag{26}
\]

Follow the binary ancestors of `N`. Since `|u_m|<=C`, iteration of (26) yields

\[
|A(N)|
\le
O_C(\log N)
+
\sum_{t\ge1}
\left|\Delta\!\left(\left\lfloor\frac{N}{2^t}\right\rfloor\right)\right|.
\tag{27}
\]

Using (25) and summing the geometric square-root scale,

\[
\sum_{t\ge1}
\left(\frac{N}{2^t}\right)^{1/2+\varepsilon}
=O_\varepsilon(N^{1/2+\varepsilon}),
\]

which proves (5).

Combining this sufficiency with the bounded-alphabet construction of `FD-210` proves the claimed equivalence. If `G` has a root in (20), `FD-210` supplies one source `u_m in {-1,0,1}` for which all `P_i(T)Delta` are `O(1)` but `A(N)` has super-square-root growth on an unbounded subsequence. If `G` has no such root, Sections 1--4 force square-root-plus-epsilon growth for every bounded source.

## 5. Möbius/Farey consequence

For `A=M`, `u_m=mu(m)`, the bounded-source hypothesis is automatic. By `FD-206`, each dyadic root increment

\[
\Delta(2^jn)=M(2^{j+1}n)-M(2^jn)
\]

is an exact root-aligned Farey sensor on the corresponding source-independent horizon. Hence every fixed `P_i(T)Delta` is representation-native: it is a fixed signed combination of actual Farey observations, not an abstract transform-space surrogate.

If RH holds, the classical Mertens criterion gives

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon}),
\]

so every fixed finite signed dyadic combination satisfies (4). Conversely, when the gcd annulus is empty, (4) implies (5) for `A=M`, hence the same Mertens criterion gives RH. This proves (6).

The result does **not** make these filters analytically easy. It classifies their theorem surface. Once a fixed family passes the spectral visibility test, a pointwise critical estimate for that family is already as strong as the destination. A family that fails the test is genuinely too weak even for generic bounded-alphabet sources.

## 6. Prior-art and representation audit

The factor-by-factor argument is elementary characteristic-root/difference-equation algebra. General recurrence, exponential-dichotomy, and dilation/Mahler-equation frameworks are classical; no novelty is claimed for solving a first-order equation `(T-a)X=Y` or for Bézout reduction of a polynomial family. A literature search found those broad frameworks but no source formulated the exact bounded-increment dyadic classification (20) for this Farey/Mertens root-sensor problem. No external theorem is load-bearing in Sections 1--4.

The only arithmetic theorem used in the RH corollary is the classical Littlewood/Mertens criterion already anchored in `SOURCES.md`. Therefore this finding does not require a new source anchor.

The representation boundary is explicit. The sufficiency theorem assumes only a bounded source and the exact binary coherence inherited by its summatory function. It does not infer source properties from arbitrary transform coordinates. The necessity direction uses the actual bounded-alphabet source constructed in `FD-210`. Thus the dichotomy is genuinely source-side, while its Farey relevance comes from the exact root-sensor realization of `FD-206`.

## Boundaries and research consequence

This classification is restricted to a **fixed finite** polynomial family. It does not cover:

- degrees or coefficients that grow with the observation scale;
- the diagonal regime in which a depth `q=q(n)` changes along binary ancestors;
- infinite filter families without a fixed finite Bézout reduction;
- averaged, sparse, exceptional-set, or otherwise non-pointwise control that does not imply (4);
- adaptive filters chosen from the observed source.

Those distinctions are substantive. `FD-209` already closes common sublogarithmic depth on a whole scale window, while the varying-depth diagonal case does not provide one common polynomial along the ancestor chain. The present theorem therefore closes the other fixed-family opening left by `FD-210` without resolving that scale-dependent case.

The resulting design rule is sharp for bounded sources: **fixed critical-cost filters have only two spectral dispositions.** A common root in `sqrt2<|rho|<=2` leaves a concrete supercritical blind source; absence of such a common root makes critical pointwise control square-root complete. There is no third fixed finite spectral regime between blindness and destination completeness.