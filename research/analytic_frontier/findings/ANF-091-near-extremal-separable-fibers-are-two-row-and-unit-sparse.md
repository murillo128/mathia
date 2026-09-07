# ANF-091 — near-extremal separable fibers are two-row and unit-sparse

**Status:** `EXACT-DERIVED + NEAR-EQUALITY-RIGIDITY + SEPARABLE-CONE + TWO-ROW-REDUCTION + UNIT-CROWDING-TAX + CONDITIONING-GATE`. `ANF-089` reduces the unresolved central-notch frontier to configurations that are simultaneously Montgomery--Taylor near-extremal and badly cross-conditioned. `ANF-090` then shows that the raw conditioning ratio can blow up exponentially even on the exactly safe separable cone, using long horizontal arithmetic chains with spacing below one. The missing check is whether that conditioning witness can coexist with the near-extremal half of the fatal gate. It cannot: Montgomery--Taylor excess places a fixed tax on every separable fiber with three or more vertical atoms, and on a genuine two-row fiber it places an explicit weighted tax on horizontal multiplicity and on every pair of centers lying inside the zero-free unit interval of the Montgomery--Taylor kernel. Consequently the exponential finite-difference witness of `ANF-090` stays a fixed positive relative distance above the Montgomery--Taylor floor.

Retain the exact Montgomery--Taylor kernel of `ANF-087`,

\[
K(x)=\widehat g(x),
\qquad
F_{\rm MT}(x)=K(x)^2,
\qquad
K(0)=1,
\tag{1}
\]

and for a finite conjugation-invariant multiset `W` write

\[
E_{\rm MT}(W)=\sum_{z,w\in W}K(z-w)^2,
\qquad
L(W)=2|W|-\sigma(W),
\qquad
\Delta(W)=E_{\rm MT}(W)-L(W).
\tag{2}
\]

Consider a separable product fiber as in `ANF-085`. Let the distinct real horizontal centers be `x_1,...,x_r` with positive integer occupancies `a_1,...,a_r`, put

\[
A:=\sum_{i=1}^r a_i,
\qquad
A_X(\alpha):=\sum_{i=1}^r a_i e^{-2\pi i\alpha x_i},
\tag{3}
\]

and let `Y=-Y` be a nonempty finite symmetric vertical multiset of cardinality

\[
m:=|Y|.
\tag{4}
\]

Form

\[
W=X+iY
:=\biguplus_{i=1}^r a_i\,(x_i+iY).
\tag{5}
\]

Then every genuinely complex near-extremizing sequence of such product fibers must eventually have exactly one conjugate vertical pair,

\[
\boxed{Y=\{-y,+y\},\qquad y>0,\qquad m=2,}
\tag{6}
\]

and in that two-row regime one has the explicit lower bound

\[
\boxed{
\frac{\Delta(W)}{L(W)}
\ge
\frac1A\sum_i a_i(a_i-1)
+
\frac2A\sum_{i<j}a_i a_j K(x_i-x_j)^2.
}
\tag{7}
\]

Since `ANF-087` proves that the first positive zero of `K` lies strictly to the right of `1`,

\[
c_1:=\min_{|t|\le1}K(t)^2>0.
\tag{8}
\]

Thus (7) implies the unit-crowding tax

\[
\boxed{
\frac{\Delta(W)}{L(W)}
\ge
\frac1A\sum_i a_i(a_i-1)
+
\frac{2c_1}{A}
\sum_{\substack{i<j\\|x_i-x_j|\le1}}a_i a_j.
}
\tag{9}
\]

In particular, if a sequence of genuine separable complex fibers satisfies

\[
\frac{\Delta(W_n)}{L(W_n)}\longrightarrow0,
\tag{10}
\]

then eventually it has exactly two vertical rows; its normalized repeated horizontal mass tends to zero; and the weighted density of pairs of distinct horizontal centers at distance at most one tends to zero. Here “unit-sparse” means precisely this vanishing weighted pair density. It does **not** assert a uniform minimum gap.

## 1. Three or more vertical atoms pay a fixed relative tax

The product factorization from `ANF-085` is

\[
S_W(\alpha)=A_X(\alpha)B_Y(\alpha),
\qquad
B_Y(\alpha)=\sum_{y\in Y}e^{2\pi\alpha y}.
\tag{11}
\]

Symmetry of `Y` gives

\[
B_Y(\alpha)\ge B_Y(0)=m
\qquad(\alpha\in\mathbb R).
\tag{12}
\]

Because the Montgomery--Taylor spectral weight is nonnegative,

\[
E_{\rm MT}(W)
\ge
m^2 E_{\rm MT}(X).
\tag{13}
\]

On the real axis every off-diagonal term is nonnegative and the diagonal contribution is `a_i^2`, so

\[
E_{\rm MT}(X)
=\sum_i a_i^2
+2\sum_{i<j}a_i a_jK(x_i-x_j)^2
\ge\sum_i a_i^2
\ge A.
\tag{14}
\]

Also `|W|=mA` and `sigma(W)>=0`, hence

\[
L(W)\le2mA.
\tag{15}
\]

Combining (13)--(15),

\[
\boxed{
\frac{E_{\rm MT}(W)}{L(W)}\ge\frac m2.
}
\tag{16}
\]

Therefore every product fiber with `m>=3` obeys

\[
\boxed{
\frac{\Delta(W)}{L(W)}\ge\frac12.
}
\tag{17}
\]

This conclusion is independent of vertical height, horizontal cardinality, collisions, and multiplicities. For a genuinely complex symmetric fiber `m>=2`; therefore relative near equality forces `m=2`. Symmetry then leaves only one nonzero conjugate pair `Y={-y,+y}`. A two-point zero fiber would be entirely real and belongs to the already closed real branch.

## 2. The two-row branch has an exact multiplicity-and-crowding lower bound

Take now

\[
Y=\{-y,+y\},
\qquad y>0.
\tag{18}
\]

There are no real points, so

\[
|W|=2A,
\qquad
\sigma(W)=0,
\qquad
L(W)=4A.
\tag{19}
\]

Equation (13) specializes to

\[
E_{\rm MT}(W)\ge4E_{\rm MT}(X).
\tag{20}
\]

Consequently

\[
\frac{\Delta(W)}{L(W)}
=\frac{E_{\rm MT}(W)}{4A}-1
\ge\frac{E_{\rm MT}(X)-A}{A}.
\tag{21}
\]

Using the exact real expansion from (14),

\[
E_{\rm MT}(X)-A
=
\sum_i a_i(a_i-1)
+2\sum_{i<j}a_i a_jK(x_i-x_j)^2,
\tag{22}
\]

which proves (7). Both terms are nonnegative and therefore separately controlled by the relative excess. In particular,

\[
\frac1A\sum_i a_i(a_i-1)
\le\frac{\Delta(W)}{L(W)}.
\tag{23}
\]

Thus a two-row near-extremizer cannot hide a positive fraction of its horizontal mass in repeated sites. This is stronger than merely requiring most distinct centers to be simple: an occupancy `a_i` is penalized quadratically through `a_i(a_i-1)`.

## 3. The zero-free unit interval converts near equality into horizontal dilution

`ANF-087` identifies all positive zeros of `K` as

\[
r_n=n+\delta_n,
\qquad n\ge1,
\qquad 0<\delta_n<\frac12.
\tag{24}
\]

Hence `K` has no zero on `[-1,1]`. Continuity gives the fixed constant `c_1>0` in (8). Restricting the pair sum in (7) to distances at most one proves (9).

Define the weighted unit-crowding count

\[
C_1(X):=
\sum_{\substack{i<j\\|x_i-x_j|\le1}}a_i a_j.
\tag{25}
\]

Every two-row near-extremizing sequence therefore satisfies

\[
\boxed{
\frac{C_1(X_n)}{A_n}
\le
\frac{1}{2c_1}
\frac{\Delta(W_n)}{L(W_n)}
\longrightarrow0.
}
\tag{26}
\]

For a simple ordered base `x_1<...<x_q`, every adjacent gap at most one contributes a distinct pair to `C_1`. Thus the number of such adjacent gaps is `o(q)` under relative near equality. The statement is deliberately density-level rather than a separation theorem: an exceptional cluster containing `o(q)` points is still allowed, as are gaps just beyond the unit scale.

More generally, because the first positive zero is `r_1>1`, the same argument works with any fixed `delta<r_1`, replacing `c_1` by

\[
c_\delta:=\min_{|t|\le\delta}K(t)^2>0.
\tag{27}
\]

The unit version is the most relevant one for the conditioning mechanism of `ANF-090` and for neighboring nonharmonic-Fourier gap heuristics.

## 4. The exponential conditioning witness of ANF-090 cannot enter the fatal gate

`ANF-090` fixes `0<delta<1` and uses the simple arithmetic chain

\[
X_n=\{0,\delta,2\delta,\ldots,n\delta\},
\qquad
W_n=X_n+i\{-y,+y\}.
\tag{28}
\]

Its source Gram matrix has an exponentially small eigenvalue, producing exponential growth of the raw cross-metric ratio `chi_s(W_n)`. But the same chain contains `n` adjacent pairs at distance exactly `delta`. Applying (7) to those terms alone gives

\[
\boxed{
\frac{\Delta(W_n)}{L(W_n)}
\ge
\frac{2n}{n+1}K(\delta)^2.
}
\tag{29}
\]

Therefore

\[
\boxed{
\liminf_{n\to\infty}
\frac{\Delta(W_n)}{L(W_n)}
\ge2K(\delta)^2>0.
}
\tag{30}
\]

So the explicit exponential ill-conditioning mechanism that invalidates a uniform bound on raw `chi_s` is **disjoint** from the Montgomery--Taylor near-extremizer regime required by `ANF-086` and `ANF-089`. Raw conditioning can indeed blow up on the safe cone, but this particular blow-up is paid for by a macroscopic amount of the exact source excess.

This does not restore `chi_s` as the correct invariant: one may still have sparse ill-conditioned clusters whose size is `o(A)`, critical-scale degeneracies not captured by a fixed unit count, or destination amplification from vertical geometry. It does show that any surviving conditioning obstruction must be substantially subtler than a positive-density subunit finite-difference chain.

## 5. Adversarial checks and evidence boundary

The proof uses only exact ingredients already established on this line: the positive spectral product domination of `ANF-085`, the exact Montgomery--Taylor normalization and zero set of `ANF-087`, and elementary nonnegativity of the real pair energy. No compactness, asymptotic pair-correlation conjecture, Riesz lower bound, or separation theorem is imported.

There are three important non-conclusions. First, (26) does not force a uniform gap greater than one; `o(A)` exceptional crowded mass can survive. Second, the result concerns the separable cone and therefore does not by itself control the genuinely nonseparable configurations that a fatal central-notch counterexample must have. Third, a small density of short horizontal pairs need not prevent a source Gram matrix from being badly conditioned if the bad direction is concentrated on a sparse subset or uses a different complex-frequency mechanism.

Classical Ingham/nonharmonic-Fourier theory is neighboring prior art for the qualitative relationship between frequency gaps and Riesz conditioning, but it is not load-bearing here. A targeted prior-art check found no theorem that supplies the line-specific relative-excess inequalities (17), (7), or the exclusion (30). Lamzouri and the Montgomery--Taylor Hilbert machinery are already anchored in `SOURCES.md`; no new durable external dependency is required.

## Research consequence

The conditioning frontier after `ANF-090` can now discard its explicit positive-density subunit-chain pathology. On the safe separable cone, any sequence that simultaneously approaches the Montgomery--Taylor floor must first collapse to a single conjugate two-row fiber and then become horizontally unit-sparse in the weighted density sense (26). A useful next invariant should therefore measure conditioning **after removing or charging the source-excess-supported crowded directions**. Equivalently, a negative construction now has to place severe source ill-conditioning on a vanishing-density component while keeping destination distance from the separable cone macroscopically nonzero. That is a materially narrower target than unrestricted Gram degeneracy.