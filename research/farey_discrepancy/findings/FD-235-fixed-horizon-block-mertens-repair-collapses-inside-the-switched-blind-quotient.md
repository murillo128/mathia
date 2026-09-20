# FD-235 — Fixed-horizon block-Mertens repair collapses inside the switched-blind quotient

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** switched-blind quotient / block-Mertens inversion / quantifier order / triangular-array boundary / one-sided cone distance
- **Depends on:** FD-234, FD-233, FD-225
- **Classification:** `EXACT-DERIVED + QUANTIFIER-CORRECTION + FIXED-HORIZON-DEGENERACY + AFFINE-QUOTIENT-COLLAPSE + TRIANGULAR-ARRAY-BOUNDARY`

## Claim

The fixed-profile switched-blind quotient introduced in FD-232--FD-233 is too coarse to carry a nontrivial one-sided obstruction for the canonical block-Mertens repair of FD-234. For every **fixed** integer `N`, that repair is itself switched-blind. Consequently its affine class modulo the FD-233 null space contains the zero profile exactly, so its best negative-capacity density is identically zero.

Retain

\[
(\mathscr A v)(m)
=
\sum_{d\le m}v_dM\!\left(\left\lfloor\frac md\right\rfloor\right),
\]

and

\[
\mathcal R_j(v)
=
(E-I)^{r_j}(\mathscr A v)(2^j),
\qquad
r_j\in\{1,4\}.
\]

FD-233 defines `N_sw` to consist of signed linearly bounded profiles `h` satisfying

\[
\mathcal R_j(h)=o(4^j)
\qquad(j\to\infty).
\tag{1}
\]

For fixed `N`, let the FD-234 canonical real correction be

\[
\widetilde c_N(n)
=-\frac12(\mathbf1*U_N)(n),
\qquad
U_N(d)=M(dN)-M((d-1)N).
\tag{2}
\]

Then

\[
\boxed{\widetilde c_N\in\mathcal N_{\rm sw}}
\tag{3}
\]

for every fixed `N`. Hence

\[
\boxed{
\widetilde c_N+\mathcal N_{\rm sw}
=
\mathcal N_{\rm sw},
}
\tag{4}
\]

and in particular the representative `0` belongs to the affine class. Therefore, with the FD-233 dyadic capacity

\[
C_k=\sum_{d\in[2^k,2^{k+1})}d,
\]

one has the exact fixed-`N` identity

\[
\boxed{
\inf_{h\in\mathcal N_{\rm sw}}
\frac{
\sum_{d\in[2^k,2^{k+1})}
(\widetilde c_N(d)+h_d)^-
}{C_k}
=0
\qquad\text{for every }k.
}
\tag{5}
\]

The rounded FD-225 correction `c_N` has the same property, since FD-234 already proves that `c_N-\widetilde c_N` belongs to `N_sw`.

Thus FD-233's positive-lift theorem remains correct, and FD-234's exact arithmetic representative remains correct, but the **fixed-`N` affine optimization suggested after them is vacuous under the persisted definition of `N_sw`**. Any nontrivial positivity obstruction for the growing reservoir construction must instead use a family-level notion in which `N`, the available divisor depth and the observed switched rows tend to infinity together, with a uniform coefficient normalization and a uniform blind condition on the rows that are actually used.

This is an order-of-quantifiers correction, not a new Mertens estimate. It does not decide the corresponding triangular-array problem.

## 1. The canonical repair has a linear envelope for each fixed N

FD-234 proves directly from `|U_N(d)|<=N` that

\[
|\widetilde c_N(n)|
\le
\frac N2\tau(n)
\le
\frac N2n.
\tag{6}
\]

For each fixed `N`, this is exactly the linear-envelope hypothesis used to define the FD-233 switched-blind space. The envelope constant is allowed to depend on the profile; here it is at most `N/2`.

No cancellation estimate for `M` enters (6).

## 2. The repair response grows only linearly in the dyadic sample index

The defining property of the canonical inverse is

\[
\mathscr A\widetilde c_N(m)
=-\frac12M(mN).
\tag{7}
\]

Therefore

\[
\mathcal R_j(\widetilde c_N)
=
-\frac12
(E-I)^{r_j}M(2^jN).
\tag{8}
\]

Expanding the bounded-order difference gives

\[
\mathcal R_j(\widetilde c_N)
=
-\frac12
\sum_{t=0}^{r_j}
(-1)^{r_j-t}
\binom{r_j}{t}
M(2^{j+t}N).
\tag{9}
\]

Use only the trivial bound `|M(x)|<=x`. Then

\[
\begin{aligned}
|\mathcal R_j(\widetilde c_N)|
&\le
\frac12
\sum_{t=0}^{r_j}
\binom{r_j}{t}2^{j+t}N\\
&=
\frac N2\,2^j(1+2)^{r_j}\\
&\le
\frac{81N}{2}\,2^j,
\end{aligned}
\tag{10}
\]

because `r_j<=4`. Dividing by the FD-233 switched scale gives

\[
\frac{|\mathcal R_j(\widetilde c_N)|}{4^j}
\le
\frac{81N}{2^{j+1}}
\longrightarrow0
\qquad(j\to\infty)
\tag{11}
\]

for every fixed `N`. Together with (6), equation (11) proves (3).

The same proof applies to the nearest-integer correction `c_N` directly up to a uniformly bounded residual. Alternatively, FD-234 already writes

\[
c_N=\widetilde c_N+r_N,
\qquad
r_N\in\mathcal N_{\rm sw},
\]

so `c_N in N_sw` follows from (3) and linearity.

## 3. The one-sided affine distance is therefore exactly zero at fixed N

The switched-blind class is a vector space: sums and scalar multiples preserve a linear envelope and the `o(4^j)` row condition. Since `\widetilde c_N in N_sw`, also

\[
-\widetilde c_N\in\mathcal N_{\rm sw}.
\]

Choosing

\[
h=-\widetilde c_N
\]

inside the FD-233 affine search produces the zero profile. Its negative part vanishes identically on every dyadic band, proving (4)--(5).

This exposes a quantifier issue in the interpretation following FD-233--FD-234. Those findings correctly show that negative-capacity sparsity is the exact criterion for positive lifting **once a nontrivial switched-response class has been fixed**. But for the particular block-Mertens correction, the fixed-profile quotient itself identifies that correction with zero. It therefore cannot supply a positive lower bound for the one-sided cone distance.

The point is not special cancellation in Möbius. It follows already from the crude growth mismatch

\[
M(2^jN)=O_N(2^j)
\]

versus the quadratic quotient scale `4^j`.

## 4. The growing-block construction has the opposite quantifier order

The countermodels of FD-222--FD-226 do not take `N` fixed and then send `j` to infinity. They choose a growing row depth `J=J(N)` and use only

\[
0\le j<J(N),
\qquad
2^{J(N)}\asymp D_N,
\]

with `D_N=N^{o(1)}` in the currently certified Vinogradov--Korobov regime. Thus

\[
J(N)=o(\log N).
\tag{12}
\]

The elementary estimate (11) becomes small only once `2^j` dominates `N`. Along the actual growing blocks one instead has

\[
2^j\le D_N=N^{o(1)}\ll N.
\tag{13}
\]

So the fixed-`N` proof of blindness says nothing about the rows used by the construction. This is exactly why the two limits cannot be interchanged.

A nontrivial replacement for `N_sw` must therefore be a **triangular family class**, not a separate asymptotic quotient for each `N`. At minimum it must specify:

- a normalization `L_N` putting the relevant coefficient families under one uniform linear envelope;
- a coupled limit `N->infinity` with the actual available depth `J(N)` or `D_N`;
- uniform switched smallness on the relevant row window rather than `j->infinity` after `N` has been frozen.

For example, after normalizing a family by `L_N`, the natural type of condition is

\[
\max_{0\le j<J(N)}
\frac{|\mathcal R_j(h_N/L_N)|}{4^j}
\longrightarrow0.
\tag{14}
\]

Equation (14) is only a template, not a new canonical definition: the correct `L_N` must be chosen from the source-side capacity regime being tested. What is exact is the obstruction to reusing the old quotient. Under (14), the formerly trivial choice `h_N=-\widetilde c_N` is admissible only if

\[
\max_{0\le j<J(N)}
\frac{
|(E-I)^{r_j}M(2^jN)|
}{2L_N4^j}
\longrightarrow0,
\tag{15}
\]

which is now a genuine coupled Mertens-scale statement rather than an automatic consequence of `|M(x)|<=x`.

Thus the family-level formulation restores exactly the information that the fixed-profile quotient discarded.

## 5. Consequence for the current positivity route

The sequence FD-230--FD-233 still establishes an important generic fact: nonnegative linear-capacity profiles cannot carry persistent dyadic mass while remaining switched-subquadratic, and for any genuinely nontrivial signed response class, vanishing negative-capacity density is precisely the coefficient-level positive-lift criterion.

What FD-235 removes is a stronger conclusion that had been suggested for the concrete Mertens repair. One cannot now seek an intrinsic obstruction by taking, for each fixed `N`,

\[
\widetilde c_N+\mathcal N_{\rm sw}
\]

and asking for its asymptotic distance from the positive cone. That distance is already zero. Any useful lower bound has to survive a **uniform growing-block quotient** whose constants and row range reflect the same source capacity problem as the reservoir construction.

This also clarifies what would count as future progress. A lower bound proved only after freezing `N` cannot obstruct the countermodel. Conversely, an adjustment that is blind only after `j` has passed well beyond `log N` is irrelevant to the precoverage block `j=O(Phi(N))`. The quantitative object must couple the two scales.

The result does not show that a suitable triangular positive lift exists, does not improve the depth of FD-225--FD-226, and does not weaken the exact source-side requirement of nonnegative integer prime occupancy. It only closes the fixed-profile affine formulation as a possible source of the missing obstruction.

## 6. Prior-art boundary and verdict

The external audit found the standard theories of weighted `c_0` sequence spaces, positive cones and triangular-array asymptotics. Those frameworks reinforce the general distinction between pointwise/fixed-parameter convergence and uniform family convergence, but no external theorem is load-bearing here. No novelty is claimed for that general distinction or for little-`o` arithmetic.

The research-specific statement is the exact calculation (8)--(11) inside the Mathia divisor-response representation: the canonical block-Mertens correction itself belongs to the persisted FD-233 null space for every fixed `N`. The proof uses only FD-234's exact inverse and the elementary inequality `|M(x)|<=x`, so no new source anchor is required in `SOURCES.md`.

**Verdict.** The one-sided affine problem after FD-234 is nontrivial only if its asymptotic class is upgraded from a fixed-profile quotient to a uniformly normalized triangular family. Under the current fixed-`N` definition, the canonical Mertens correction is already switched-blind and is equivalent to zero, making the negative-capacity infimum exactly zero. The next meaningful positivity test must therefore formulate and analyze the coupled `N,J(N)` quotient actually seen by the growing reservoir construction.