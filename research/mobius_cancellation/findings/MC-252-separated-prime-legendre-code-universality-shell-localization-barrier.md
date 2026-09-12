# MC-252 — Separated-prime Legendre codes are universal; tight shell localization is load-bearing

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-ARITHMETIC-CONTROL`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

The quadratic blind sector of `MC-238` is the kernel of the Legendre matrix

\[
A_{p,r}=\frac{1-(\frac pr)}2\in\mathbb F_2,
\qquad p\le y\text{ prime},\ r\in S.
\tag{1}
\]

`MC-243`, `MC-248`, and `MC-251` use abstract coding theory as a matched control: minimum-support information is compatible with a very large kernel. A natural possible escape is that the matrix `(1)` is not an arbitrary binary matrix but is built from quadratic residue symbols, so reciprocity might impose enough extra arithmetic dependence to rule out those generic high-rate codes.

That escape is false **if the tight shell condition on the column primes is removed**.

Let

\[
\mathcal P_y=\{p:p\le y\text{ prime}\},
\qquad m=|\mathcal P_y|=\pi(y).
\]

For every finite binary matrix

\[
B=(B_{p,j})\in\mathbb F_2^{\mathcal P_y\times\{1,\dots,n\}},
\tag{2}
\]

there exist distinct primes

\[
r_1,\dots,r_n>y
\]

that may be taken arbitrarily large such that

\[
\boxed{
\frac{1-(\frac{p}{r_j})}{2}=B_{p,j}
\qquad
(p\le y\text{ prime},\ 1\le j\le n).
}
\tag{3}
\]

Thus every finite binary matrix occurs **exactly** as a lower-prime / separated-upper-prime Legendre matrix.

Equivalently, if `C\subseteq\mathbb F_2^n` is any binary linear code with

\[
\operatorname{codim}C\le\pi(y),
\tag{4}
\]

then there is a set of distinct primes `S=\{r_1,\dots,r_n\}`, all larger than `y`, for which the quadratic blind sector defined by the lower primes is exactly

\[
\boxed{
K_y(S)=\ker_{\mathbb F_2}A=C.
}
\tag{5}
\]

Consequently the generic coding-theory controls used in `MC-243`--`MC-251` are not merely abstract objects alien to quadratic-residue arithmetic. Whenever their redundancy is at most `\pi(y)`, the same code can be realized by an exact Legendre-symbol matrix after allowing the column primes to move sufficiently far beyond the lower-prime cutoff.

The obstruction therefore sharpens:

\[
\boxed{
\text{quadratic reciprocity + CRT + primality alone}
\not\Rightarrow
\text{extra code rank or distance-profile rigidity}.
}
\tag{6}
\]

Any arithmetic improvement over `MC-251` at the quadratic level must use information that this realization deliberately discards: above all the active localization

\[
r\in(y,2y],
\tag{7}
\]

or a comparably quantitative coupling between the lower-prime rows and the moving shell columns. Bare reciprocity identities do not distinguish the actual blind code from a generic binary code once the two prime sets are allowed to be widely separated.

This does **not** show that arbitrary codes occur in the Mathia shell `(y,2y]`, does not bound the actual blind quotient, and gives no estimate for `M(X)`.

## 1. Every prescribed Legendre column is realized by infinitely many primes

Fix one desired column

\[
b=(B_{p,j})_{p\in\mathcal P_y}.
\]

Put

\[
M_y=8\prod_{\substack{3\le p\le y\\p\text{ prime}}}p.
\tag{8}
\]

For every odd prime `p\le y`, choose a nonzero residue `a_p\pmod p` satisfying

\[
\left(\frac{a_p}{p}\right)=(-1)^{B_{p,j}}.
\tag{9}
\]

Such a residue exists because the nonzero residues modulo an odd prime split equally into quadratic residues and nonresidues.

For the row `p=2`, choose

\[
a_2\equiv
\begin{cases}
1\pmod 8,&B_{2,j}=0,\\
5\pmod 8,&B_{2,j}=1.
\end{cases}
\tag{10}
\]

Both choices are congruent to `1 mod 4`. By the Chinese remainder theorem there is a residue class

\[
a_j\pmod{M_y}
\]

satisfying `(9)` and `(10)`. It is coprime to `M_y`, so Dirichlet's theorem supplies infinitely many primes

\[
r\equiv a_j\pmod{M_y}.
\tag{11}
\]

Choose one with `r>y`. Because `r\equiv1\pmod4`, quadratic reciprocity has no sign for every odd `p\le y`:

\[
\left(\frac p r\right)
=
\left(\frac r p\right)
=
\left(\frac{a_j}{p}\right)
=(-1)^{B_{p,j}}.
\tag{12}
\]

For `p=2`, the supplementary law gives

\[
\left(\frac2r\right)
=
\begin{cases}
+1,&r\equiv1\pmod8,\\
-1,&r\equiv5\pmod8,
\end{cases}
\tag{13}
\]

which realizes the remaining row. Hence `(3)` holds for this column.

Apply the same construction independently to each column. Each admissible residue class contains infinitely many primes, so the primes `r_j` may be chosen pairwise distinct and larger than any prescribed finite threshold. This proves `(3)`.

The proof is intentionally nonquantitative in the size of the `r_j`. That missing size control is exactly the boundary isolated below.

## 2. Every low-codimension binary code is an exact separated-prime blind sector

Let `C\subseteq\mathbb F_2^n` have codimension `\rho\le\pi(y)`. Choose a full-rank parity-check matrix

\[
H\in\mathbb F_2^{\rho\times n}
\qquad\text{with}\qquad
C=\ker H.
\tag{14}
\]

Pad `H` by zero rows to obtain an `m\times n` matrix `B`, where `m=\pi(y)`, and index those rows by the primes `p\le y`. By the construction above there are distinct primes `r_j>y` whose Legendre matrix is exactly `B`. Therefore

\[
K_y(S)=\ker A=\ker B=\ker H=C,
\]

which proves `(5)`.

This converts the earlier coding controls into arithmetic controls. For example, the Gilbert--Varshamov comparison in `MC-243` exhibits codes of length

\[
n\asymp\frac y{\log y}
\]

with the required growing minimum distance and redundancy only

\[
O(\log y\,\log\log y).
\]

That redundancy is `o(\pi(y))`, so codes with the same information profile can be realized by genuine Legendre matrices of the separated-prime form above. Likewise, the generic high-rate `q=2` sphere-packing frontier in `MC-251` cannot be rejected merely by saying that Legendre symbols are arithmetic rather than arbitrary bits.

The realization says nothing about how large the required column primes are. It transfers **algebraic code shape**, not the active shell geometry.

## 3. Why the shell `(y,2y]` is exactly the missing arithmetic constraint

The CRT modulus `(8)` satisfies

\[
\log M_y=(1+o(1))y
\tag{15}
\]

by the prime number theorem. Dirichlet's theorem guarantees primes in each prescribed class modulo `M_y`, but gives no prime in the microscopic interval `(y,2y]`; in fact the modulus itself is exponentially larger than that interval scale.

Thus the proof cannot be pushed into the Mathia shell by a routine quantitative refinement. The actual matrix in `MC-238` asks for many column primes `r\asymp y` while simultaneously prescribing their quadratic residue pattern against essentially all primes `p\le y`. The separated-prime universality theorem deliberately removes exactly that simultaneous size constraint.

This distinguishes two kinds of "arithmetic structure" that should not be conflated:

- **reciprocity algebra:** the values `(p/r)` obey quadratic reciprocity and arise from genuine primes;
- **localized arithmetic geometry:** the same prime `r` must lie in the narrow moving shell `(y,2y]` while interacting with the complete lower-prime row family.

The first kind alone is universal enough to encode arbitrary binary matrices. Any useful rigidity must therefore come from the second kind, from additional source coupling, or from a stronger simultaneous object not preserved by the CRT construction.

This also clarifies the `mind/RESEARCH_LINES.md` suggestion to seek reciprocity/Kummer structure. At the quadratic level, **quadratic reciprocity by itself is not the missing theorem**. A viable reciprocity route must exploit reciprocity together with shell localization, simultaneous prime distribution, or cross-column dependencies that disappear when the columns are allowed to escape to unrelated Dirichlet progressions.

## 4. Relation to MC-055 and prescribed-Legendre prior art

`MC-055` already uses the same classical mechanism in a one-column extremal specialization: for each finite observation scale it constructs a prime `q_X` with

\[
\left(\frac p{q_X}\right)=-1
\qquad(p\le X\text{ prime}),
\]

by CRT, Dirichlet's theorem, and quadratic reciprocity. The present result is not a new prescribed-character theorem. It simply keeps the full sign vector free, repeats the construction independently across finitely many columns, and records the resulting exact **code universality** consequence for the current blind-sector frontier.

Direct prior art is also provided by Brandon Hanson, Robert C. Vaughan and Ruixiang Zhang, *The Least Number with Prescribed Legendre Symbols*, arXiv:1605.05584 (2016). Their setup explicitly identifies vectors of Legendre signs at several fixed primes with `\mathbb F_2^k`, notes the CRT surjectivity of the sign map, and studies the much harder quantitative problem of how small a number can realize every prescribed sign vector. That work reinforces the novelty boundary here: arbitrary finite sign prescription is classical; the difficult information is quantitative size/localization.

Standard references for the ingredients are the quadratic reciprocity and supplementary laws, the Chinese remainder theorem, and Dirichlet's theorem on primes in arithmetic progressions; `MC-055` already audits those ingredients against DLMF §§27.9, 27.11, and 27.15.

No novelty is claimed for any of these theorems or for prescribed Legendre vectors. The durable Mathia delta is the frontier implication `(6)`: the abstract coding no-go from `MC-243`--`MC-251` survives exact realization inside quadratic-residue arithmetic unless the tight shell localization is retained.

## 5. Decisive falsification checks

- **Tight-shell check.** Nothing here realizes arbitrary columns with `r_j\in(y,2y]`. Claiming that would erase the entire point of the result.
- **Quantitative-prime check.** Dirichlet supplies existence in the prescribed class but no bound useful at the shell scale. No Linnik-type estimate is silently substituted for `(7)`.
- **Reciprocity-sign check.** Choosing every `r_j\equiv1\pmod4` is what makes `(p/r_j)=(r_j/p)` for all odd row primes. The `p=2` row is handled separately by `r_j\bmod8`.
- **Coprimality check.** Every CRT component is nonzero modulo its row prime, so the resulting class is reduced modulo `M_y` and Dirichlet applies.
- **Repeated-column check.** Duplicate binary columns cause no problem because a single reduced residue class contains infinitely many primes; distinct column primes can still be selected.
- **Code-dimension check.** The code corollary requires `codim C\le\pi(y)` because the realized Legendre matrix has exactly one row per prime `p\le y`. This is satisfied by the high-rate matched controls relevant to `MC-243`--`MC-251` but is not omitted from the theorem.
- **Higher-primary check.** The theorem is quadratic (`\ell=2`). It does not rule out genuinely stronger constraints from higher power-residue/Kummer structure at odd primary levels.
- **Source-coupling check.** The construction only matches the Legendre incidence matrix. It does not reproduce the exact shell subset, progression amplitudes, rough Möbius coset, or any other source-selected structure from `MC-233`--`MC-246`.

## Updated frontier

`MC-251` showed that generic coding inequalities leave a large low-order blind code possible and suggested that the next theorem must use arithmetic structure beyond minimum distance. The present finding identifies one tempting candidate structure that is insufficient on its own: **being a Legendre-symbol matrix subject to quadratic reciprocity does not reduce the class of finite binary codes once column-prime localization is relaxed**.

The live quadratic generation problem is therefore narrower. To beat the generic coding frontier one must prove a property that fails for the separated-prime realization above. The cleanest such property is the actual shell constraint `r\in(y,2y]`; other possibilities are simultaneous distribution constraints tied to that shell or a source-coupled signed estimate that bypasses generation altogether.

This is a negative result, but it converts "use arithmetic dependence/reciprocity" into a falsifiable requirement: any proposed new invariant should first be tested on arbitrary separated-prime Legendre realizations. If it survives there, it cannot by itself distinguish the Mathia shell from a generic code.