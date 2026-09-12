# MC-232 — Boolean incidence inversion converts exact cells to clean CRT progression sums at subpower condition cost

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the first square-defect shell of `MC-229`--`MC-231`. Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and let

\[
\mathcal D_y=\{d:\ y<d\le2y,\ d\text{ prime}\},
\qquad
m_y:=|\mathcal D_y|.
\]

For a rough input `n<=T`, recall the exact shell-incidence set

\[
I_y(n)=\{d\in\mathcal D_y:d^2\mid n+P\},
\]

the exact incidence cells

\[
\mathcal E_S
=\{n\le T:(n,P)=1,\ I_y(n)=S\},
\qquad
C_S(X)=\sum_{n\in\mathcal E_S}\mu(n),
\]

and the weight

\[
w(S)=\sum_{d\in S}d.
\]

`MC-230` reduced the first-shell target to the sufficient exact-cell energy

\[
\mathcal C_y(X)
:=\sum_{\varnothing\ne S\subseteq\mathcal D_y}
w(S)|C_S(X)|^2.
\tag{1}
\]

Define instead the **partial-intersection sums**

\[
B_S(X)
:=
\sum_{\substack{n\le T\\(n,P)=1\\S\subseteq I_y(n)}}\mu(n)
=
\sum_{U\supseteq S}C_U(X),
\qquad \varnothing\ne S\subseteq\mathcal D_y,
\tag{2}
\]

and their weighted energy

\[
\mathcal B_y(X)
:=
\sum_{\varnothing\ne S\subseteq\mathcal D_y}
w(S)|B_S(X)|^2.
\tag{3}
\]

Then Boolean-lattice Möbius inversion gives

\[
C_S(X)
=
\sum_{U\supseteq S}(-1)^{|U|-|S|}B_U(X).
\tag{4}
\]

More importantly, the two weighted energies are equivalent up to a **subpower condition factor**. Put

\[
\kappa:=\frac{3+\sqrt5}{2}.
\tag{5}
\]

Then exactly

\[
\boxed{
\mathcal B_y(X)
\le
\kappa^{m_y-1}\mathcal C_y(X),
\qquad
\mathcal C_y(X)
\le
\kappa^{m_y-1}\mathcal B_y(X).
}
\tag{6}
\]

Since the prime number theorem gives

\[
m_y=(c+o(1))\frac{\log X}{\log\log X},
\]

we have

\[
\kappa^{m_y}=X^{o(1)}.
\tag{7}
\]

Consequently

\[
\boxed{
\mathcal C_y(X)\le X^{1+o(1)}
\quad\Longleftrightarrow\quad
\mathcal B_y(X)\le X^{1+o(1)}
}
\tag{8}
\]

at the fixed-power resolution relevant to the line.

This removes another representational complication from the `MC-230` diagonal-cell route. **Exact exclusion masks are not power-essential.** One may replace every exact incidence cell by the corresponding family of ordinary partial intersections without losing a fixed power of `X`.

The payoff is arithmetic rather than merely combinatorial. For

\[
Q_S:=\prod_{d\in S}d^2,
\tag{9}
\]

the CRT identity already established in `MC-229` gives the clean one-dimensional lift

\[
\boxed{
B_S(X)
=
\sum_{\substack{P/Q_S<k\le X/Q_S\\(k,P)=1}}
\mu(kQ_S-P).
}
\tag{10}
\]

Thus the stronger diagonalized first-shell route can be attacked entirely through a sparse family of **source-selected affine Möbius sums**. The awkward condition “divisible by exactly these shell squares and no others” disappears; only the coefficient `Q_S`, the common primorial source `P`, and the roughness condition `(k,P)=1` remain.

The high-incidence sector stays support-harmless. For fixed `0<alpha<c`, if

\[
r_\alpha(X)
=\left\lceil
\alpha\frac{\log X}{\log\log X}
\right\rceil,
\]

then the same support calculation as in `MC-229`--`MC-230` yields

\[
\boxed{
\sum_{|S|\ge r_\alpha(X)}w(S)|B_S(X)|^2
\le X^{2-4\alpha+o(1)}.
}
\tag{11}
\]

In particular the sector `alpha>=1/4` is already at or below `X^{1+o(1)}` without Möbius cancellation. Therefore, when `c>1/4`, a sufficient remaining target is

\[
\boxed{
\sum_{0<|S|<r_{1/4}(X)}
w(S)
\left|
\sum_{\substack{P/Q_S<k\le X/Q_S\\(k,P)=1}}
\mu(kQ_S-P)
\right|^2
\le X^{1+o(1)}.
}
\tag{12}
\]

There are only `2^{m_y}=X^{o(1)}` sets `S`, and every nonzero weight satisfies `y<=w(S)<=2ym_y=X^{o(1)}`. Hence `(12)` is, again at fixed-power resolution, equivalent to the uniform amplitude surface

\[
\boxed{
|B_S(X)|\le X^{1/2+o(1)}
\quad
\text{for every }0<|S|<r_{1/4}(X).
}
\tag{13}
\]

This should **not** be read as square-root cancellation relative to the natural length of every lifted sum. If

\[
|S|
=\left(\alpha+o(1)\right)
\frac{\log X}{\log\log X},
\qquad 0\le\alpha<\frac14,
\]

then, because every `d` lies in `(y,2y]`,

\[
Q_S=X^{2\alpha+o(1)},
\qquad
\frac{X}{Q_S}=X^{1-2\alpha+o(1)}.
\tag{14}
\]

The trivial support bound is therefore `X^{1-2alpha+o(1)}`, while `(13)` asks only for `X^{1/2+o(1)}`. The missing fixed-power gain is

\[
\boxed{
X^{1/2-2\alpha+o(1)}.
}
\tag{15}
\]

Equivalently, in terms of the lifted interval length `L_S=X^{1-2alpha+o(1)}`, the required exponent interpolates as

\[
|B_S|
\le
L_S^{\,1/(2(1-2\alpha))+o(1)}.
\tag{16}
\]

At incidence depth `alpha=0`, this is the genuine square-root barrier. As `alpha` approaches `1/4`, the required cancellation weakens continuously to the trivial bound. The remaining diagonalized problem is therefore **graded by incidence depth** rather than requiring GRH-quality square-root-in-length cancellation at every level.

No estimate `(12)` or `(13)` for the deterministic Möbius function is proved. No improvement for `W_y(X)`, `M(X)`, or the zeta zero set follows from this change of representation alone.

## 1. Boolean zeta and Möbius transforms are subpower-conditioned here

Equation `(2)` is the upper Boolean zeta transform. To retain the line's weighted energy exactly, decompose `(1)` and `(3)` by shell coordinate:

\[
\mathcal C_y
=
\sum_{d\in\mathcal D_y}
 d\sum_{S\ni d}|C_S|^2,
\qquad
\mathcal B_y
=
\sum_{d\in\mathcal D_y}
 d\sum_{S\ni d}|B_S|^2.
\tag{17}
\]

Fix one shell prime `d`. Index subsets containing `d` by `U\subseteq\mathcal D_y\setminus\{d\}` and put

\[
c_d(U)=C_{U\cup\{d\}},
\qquad
b_d(U)=B_{U\cup\{d\}}.
\]

Then

\[
b_d(U)=\sum_{V\supseteq U}c_d(V).
\tag{18}
\]

For one Boolean coordinate, the transform matrix is

\[
Z=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

Its squared Euclidean operator norm is the largest eigenvalue of `Z^*Z`, namely

\[
\|Z\|_2^2=\frac{3+\sqrt5}{2}=\kappa.
\tag{19}
\]

The `m_y-1` coordinate Boolean transform is the tensor power `Z^{\otimes(m_y-1)}`, so

\[
\sum_U|b_d(U)|^2
\le
\kappa^{m_y-1}
\sum_U|c_d(U)|^2.
\tag{20}
\]

The inverse one-coordinate Möbius matrix

\[
Z^{-1}=
\begin{pmatrix}
1&-1\\
0&1
\end{pmatrix}
\]

has the same singular values, so the reverse inequality holds with the same factor. Multiplying by `d` and summing over shell primes proves `(6)`.

The exact constant is not important for the exponent budget. What matters is that the incidence alphabet has only `m_y=o(log X)` Boolean coordinates. Any transform with condition number exponential only in `m_y` costs `X^{o(1)}`, not a fixed power.

## 2. Partial intersections are single CRT progressions

For nonempty `S`, membership in every selected shell support means

\[
n\equiv-P\pmod{d^2}
\qquad(d\in S).
\]

The square moduli are pairwise coprime, so this is simply

\[
n\equiv-P\pmod{Q_S}.
\]

Writing `n=kQ_S-P`, and using `(Q_S,P)=1`, gives

\[
1\le n\le X-P
\iff
P/Q_S<k\le X/Q_S,
\]

and

\[
(n,P)=1
\iff
(k,P)=1.
\]

This proves `(10)`. Unlike an exact cell, there is no product of exclusions over the unselected shell primes.

This representation also makes clear what `MC-231` did and did not rule out. The singleton exact-cell sum `C_{\{d\}}` has poor same-cell divisibility pairing, but its Boolean transform `B_{\{d\}}` is the original progression coordinate `A_d`. Higher `B_S` are the same source-selected problem with a larger square-product coefficient. The open mechanism may therefore be additive, bilinear, harmonic, or dispersion-based across the lifted `k` variable without respecting exact-cell membership pointwise.

## 3. The cancellation demand weakens with incidence depth

For `s=|S|` and shell primes `d\asymp y`, equation `(9)` gives

\[
y^{2s}<Q_S\le(2y)^{2s}.
\tag{21}
\]

If `s=(alpha+o(1))log X/loglog X`, then `(21)` is exactly `(14)`. The number of subsets at any such level remains `X^{o(1)}` because `m_y=O(log X/loglog X)`.

The support-only phase boundary is therefore not merely a statement about rare high-incidence integers. It is also a theorem-search budget for the clean CRT family:

- fixed or `o(log X/loglog X)` incidence remains essentially a square-root-in-`X` problem;
- mesoscopic incidence `alpha>0` shortens the lifted sum to `X^{1-2alpha+o(1)}` and reduces the required gain by `2alpha` powers of `X`;
- at `alpha=1/4`, the lifted support itself is `X^{1/2+o(1)}`, so no sign cancellation is needed.

A prospective theorem need not deliver one uniform “square-root relative to length” estimate across this whole family. It only needs to cross the graded boundary `(15)` in aggregate, or the sufficient uniform surface `(13)`.

## 4. Prior art and novelty boundary

The transform `(2)`--`(4)` is classical Möbius inversion on the Boolean lattice, equivalently inclusion--exclusion. Gian-Carlo Rota's foundational paper, *On the foundations of combinatorial theory I. Theory of Möbius Functions*, Z. Wahrscheinlichkeitstheorie und Verw. Gebiete 2 (1964), 340--368, DOI `10.1007/BF00531932`, develops Möbius inversion in incidence algebras and includes the Boolean-lattice/inclusion--exclusion framework. No novelty is claimed for Boolean Möbius inversion, incidence algebras, CRT, or the tensor-product transform itself.

The line-specific delta is the **condition-number and exponent-budget audit for the active first square-defect shell**. Combining the Boolean transform with `m_y=O(log X/loglog X)` shows that exact-cell sums and partial-intersection sums are interchangeable at fixed-power resolution inside the stronger `MC-230` diagonalized route. Combining that with the exact `MC-229` CRT lift produces the graded affine-sum target `(12)`--`(16)`.

A targeted prior-art check found the classical incidence-algebra theory and standard inclusion--exclusion interpretation, but no reason to treat the transform itself as a new theorem. The useful research content is the specialization: the entire exact-incidence combinatorics can be removed at `X^{o(1)}` cost, exposing a sparse, source-selected family of affine Möbius sums whose required cancellation strength is now explicit level by level.

## 5. Boundaries and falsification tests

- Equation `(8)` is an equivalence between the **two stronger diagonal energies** `mathcal C_y` and `mathcal B_y`; it is not an equivalence with the original shell energy `W_y`. In fact `B_{\{d\}}=A_d`, so `mathcal B_y` contains `W_y` plus additional higher-intersection energies and may be strictly stronger.
- The result therefore does not prove that cross-cell cancellation is absent from the true shell. It shows only that if one follows the stronger diagonalization strategy of `MC-230`, exact exclusion masks can be discarded without a fixed-power penalty.
- The singular-value factor in `(6)` must be applied on `m_y-1` coordinates after fixing `d`; applying an unweighted Boolean norm directly and then inserting `w(S)` without the decomposition `(17)` would not justify the same bound.
- The level estimate `(14)` uses `d\in(y,2y]` and fixed `c`. Changing the shell scale changes the incidence-depth phase diagram.
- The equivalence `(13)` is only at `X^{o(1)}` exponent resolution. It does not identify optimal logarithmic factors or constants.
- For `c<=1/4`, the formal threshold `r_{1/4}(X)` lies at or beyond the shell size, so there is no nontrivial support-harmless high-incidence sector; `(6)`--`(10)` remain valid but the whole nonempty Boolean family stays in the hard range.
- Existing polynomial-Möbius and arithmetic-progression theorems must be checked against the moving coefficients `Q_S`, the fixed primorial source `P`, and the required gain `(15)`. A theorem that gives only `log^{-A}X` savings still cannot cross the fixed-power gap at low incidence.

## Consequence for the live frontier

The first-shell diagonalized route no longer needs to reason directly about exact incidence cells. Its clean arithmetic target is the family `(10)`, with a continuously weakening power requirement as the intersection depth increases. The most difficult levels are now explicit: **small incidence, where `Q_S=X^{o(1)}` and one still needs essentially square-root-in-`X` cancellation for the source-selected affine Möbius sum.** Mesoscopic levels progressively relax, and the entire sector beyond the one-quarter incidence depth is support-only.

The next useful attack should therefore ask for a theorem that exploits the common source `P` across the sparse affine family `(10)` and crosses the graded budget `(15)`—for example through a parity-sensitive bilinear/dispersion mechanism—rather than spending further effort on exact-cell exclusion combinatorics or same-cell multiplicative pairing.
