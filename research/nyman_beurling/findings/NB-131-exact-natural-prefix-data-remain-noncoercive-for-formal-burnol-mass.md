# NB-131 — exact natural-prefix data remain noncoercive for formal Burnol mass

**Status:** `EXACT-DERIVED + EXACT-NATURAL-PREFIX-REINTERPOLATION + HEIGHT-UNIFORM-CONDITIONING + BURNOL-MASS-DECOUPLING + FINITE-DESCRIPTOR-NO-GO + NB-127/NB-130-SYNTHESIS + NEGATIVE/ROUTE-NARROWING + FORMAL-PACKET-ONLY + PRIOR-ART-AUDITED`.

`NB-127` showed that a fixed finite collection of geometric recurrence descriptors cannot control the formal Burnol mass: common vertical translations admit simultaneous phase near-returns while the finite-packet Blaschke defect tends to zero. Its primitive samples, however, only near-returned because the packet coefficients were held fixed. `NB-130` closed a different gap by showing that rank-`R` formal zero powers can interpolate **arbitrary** data on the full natural prefix `1,...,R`, but it did not track what happens to the Burnol mass when the interpolating support is moved vertically.

The two mechanisms splice exactly. **A prescribed natural prefix can be kept literally unchanged while the entire formal zero-power support is translated to arbitrarily large height, with no additional conditioning cost from the translation, and with formal Burnol mass tending to zero.** Moreover, along simultaneous phase-return heights, the re-solved coefficient vector itself returns to its original value. Thus the exact-versus-near gap in `NB-127` is not a source of coercivity at any fixed cutoff.

Precisely, fix `R>=2`, `1/2<beta<1`, `T_0 in R`, and choose `delta>0` so that the `NB-130` Vandermonde nodes are distinct, for example

\[
0<\delta<\frac{2\pi}{\log R}.
\tag{1}
\]

Put

\[
\rho_j^{(0)}
:=
\beta+i(T_0+j\delta),
\qquad
0\le j<R,
\tag{2}
\]

and let `y=(y_1,...,y_R) in C^R` be arbitrary. Then for every real vertical shift `S` there is a unique coefficient vector

\[
c(S)=(c_0(S),\ldots,c_{R-1}(S))
\tag{3}
\]

such that the shifted packet

\[
P_S(n)
:=
\sum_{j=0}^{R-1}
 c_j(S)
 n^{-\overline{\rho_j^{(0)}+iS}}
\tag{4}
\]

satisfies

\[
\boxed{
P_S(n)=y_n,
\qquad
1\le n\le R,
\qquad
\text{for every }S\in\mathbb R.
}
\tag{5}
\]

If `V` is the evaluation matrix at `S=0`, then the shifted matrix is

\[
V(S)=D_SV,
\qquad
D_S:=\operatorname{diag}(1^{iS},2^{iS},\ldots,R^{iS}),
\tag{6}
\]

so one may take

\[
\boxed{
c(S)=V^{-1}D_S^{-1}y.}
\tag{7}
\]

Because `D_S` is unitary,

\[
\kappa_2(V(S))=\kappa_2(V),
\qquad
\|c(S)\|_2
\le
\|V^{-1}\|_2\,\|y\|_2.
\tag{8}
\]

The bound is uniform in the absolute height `S`. It is **not** uniform in `R` or in the internal spacing `delta`; the severe narrow-packet conditioning already isolated in `NB-130` remains intact.

For the corresponding simple formal packet

\[
F_S:=\{\rho_j^{(0)}+iS:0\le j<R\},
\tag{9}
\]

let

\[
\tau(F_S):=1-|B_{F_S}(1)|^2
\tag{10}
\]

be the finite-packet Blaschke target defect used in `NB-127`. Then

\[
\boxed{
\tau(F_S)=O_{R,\beta,T_0,\delta}(S^{-2})
\longrightarrow0
\qquad(S\to+\infty).
}
\tag{11}
\]

Consequently, for every fixed finite prefix `y` and every `epsilon>0`, there is a rank-`R` formal right-half zero-power packet with **exactly** that prefix, the same fixed internal ordinate width `(R-1)delta`, coefficient norm bounded by the same constant as in `(8)`, and formal Burnol mass below `epsilon`.

The qualification **formal** is essential. The translated points in `(9)` are not asserted to be zeros of `zeta`; actual zeta-zero geometry is precisely the information missing from this matched-control class.

## 1. Vertical translation is only a unitary row modulation

Let

\[
V_{n,j}
:=
n^{-\overline{\rho_j^{(0)}}},
\qquad
1\le n\le R,
\quad
0\le j<R.
\tag{12}
\]

By `NB-130`, condition `(1)` makes `V` invertible. The only sign worth checking carefully is the conjugation under vertical translation:

\[
\overline{\rho_j^{(0)}+iS}
=
\overline{\rho_j^{(0)}}-iS,
\tag{13}
\]

hence

\[
n^{-\overline{\rho_j^{(0)}+iS}}
=
n^{iS}n^{-\overline{\rho_j^{(0)}}}.
\tag{14}
\]

Equation `(14)` gives `(6)`. Multiplying `(7)` by `V(S)` yields

\[
V(S)c(S)
=
D_SVV^{-1}D_S^{-1}y
=y,
\tag{15}
\]

which proves the exact interpolation statement `(5)` for every height, not merely along a subsequence.

Since every diagonal entry of `D_S` has modulus one, left multiplication by `D_S` preserves all singular values. This proves the conditioning identity in `(8)`. Also

\[
\|c(S)\|_2
=
\|V^{-1}D_S^{-1}y\|_2
\le
\|V^{-1}\|_2\|y\|_2.
\tag{16}
\]

Thus moving the packet to high ordinate does not itself make the finite interpolation problem worse. The constant `||V^{-1}||_2` may already be enormous when the `R` exponents are tightly packed; `NB-131` makes no claim to control that `R,delta` dependence.

This distinction matters. `NB-130` left open the possibility that exact high interpolation might require coefficients whose norm grows with absolute height. Equation `(16)` rules out that particular rescue: after fixing one invertible formal support shape, **height is a unitary modulation variable** for natural-prefix interpolation.

## 2. The exact prefix survives while the Burnol mass vanishes

`NB-127` records for a right-half point `rho=beta+i gamma` the one-point defect

\[
\delta_\rho
=
\frac{2\beta-1}{\beta^2+\gamma^2},
\tag{17}
\]

and for a finite packet the elementary product estimate

\[
\tau(F)
\le
\sum_{\rho\in F}\delta_\rho
\tag{18}
\]

with multiplicity. For `(9)`, all real parts remain equal to the fixed `beta`, while

\[
\Im(\rho_j^{(0)}+iS)
=
T_0+j\delta+S.
\tag{19}
\]

Therefore

\[
\tau(F_S)
\le
\sum_{j=0}^{R-1}
\frac{2\beta-1}
{\beta^2+(T_0+j\delta+S)^2}
=
O_{R,\beta,T_0,\delta}(S^{-2}),
\tag{20}
\]

which proves `(11)`.

The coefficients play no role in `(20)`: the formal Burnol defect belongs to the support points. Re-solving the coefficients is therefore free to enforce `(5)` without preventing the support defect from escaping to zero.

This gives a sharper matched-control statement than either precursor alone. `NB-127` preserved fixed finite recurrence data only asymptotically under translation. `NB-130` preserved arbitrary natural-prefix data exactly but did not compare the resulting support to Burnol mass. Here **the full natural prefix is identical, not approximately identical, at every height**, while the zero-sensitive target mass collapses.

In particular, if `y` is chosen to be any finite matched-control prefix already constructed on this line, including the sharp finite control underlying `NB-129`, the same visible natural-grid data can be carried to arbitrarily small formal Burnol mass. This does not say that the resulting packet comes from a Nyman minimizer or from actual zeta zeros; it says that finite-prefix equality itself cannot certify the missing zero-sensitive mass inside the formal zero-power class.

## 3. Along phase recurrences, even the coefficients return

There is a stronger form of the obstruction relevant to attempts to augment the prefix by finitely many recurrence observables. Let `Q` be any fixed finite collection of positive integer bases. The finite-torus recurrence used in `NB-127` gives an unbounded sequence `S_k` such that

\[
\max_{b\in\{1,\ldots,R\}\cup Q}
|b^{iS_k}-1|
\longrightarrow0.
\tag{21}
\]

For the natural-prefix diagonal this means

\[
D_{S_k}\longrightarrow I.
\tag{22}
\]

Equation `(7)` then gives the coefficient return

\[
\boxed{
c(S_k)\longrightarrow c(0).}
\tag{23}
\]

At the same time, for every `q in Q`, each labelled characteristic root obeys

\[
q^{-\overline{\rho_j^{(0)}+iS_k}}
=
q^{iS_k}q^{-\overline{\rho_j^{(0)}}}
\longrightarrow
q^{-\overline{\rho_j^{(0)}}}.
\tag{24}
\]

Hence the finite annihilator coefficients, normalized missing-root margins, and other continuous recurrence observables built from those labelled roots also return to their initial values, exactly as in `NB-127`. But unlike `NB-127`, the natural-prefix component never moved at all:

\[
(P_{S_k}(1),\ldots,P_{S_k}(R))=y
\quad\text{for every }k.
\tag{25}
\]

Combining `(11)`, `(23)`, `(24)`, and `(25)` yields the finite-descriptor no-go. Let `\mathscr D` be any **height-blind finite descriptor** formed continuously from a fixed exact natural prefix, the re-solved coefficient vector, and finitely many periodic phase/recurrence observables such as `(24)`. Then along the sequence above

\[
\mathscr D(F_{S_k},c(S_k))
\longrightarrow
\mathscr D(F_0,c(0)),
\qquad
\tau(F_{S_k})\longrightarrow0.
\tag{26}
\]

Therefore, if a continuous nonnegative functional `Phi` satisfies

\[
\Phi(\mathscr D(F_0,c(0)))>0,
\tag{27}
\]

there cannot be a universal formal-packet inequality

\[
\tau(F)\ge\Phi(\mathscr D(F,c)).
\tag{28}
\]

The adjective **height-blind** is load-bearing. A descriptor containing the raw absolute ordinates `Im rho_j` trivially distinguishes the translated packets. The point is narrower: adding any fixed amount of periodic multibase recurrence information, even together with the exact finite natural prefix and the coefficient vector, does not restore coercivity.

## 4. What this rules out, and what remains live

The finding removes a specific loophole left by `NB-127`: replacing fixed coefficients by an exact finite interpolation does **not** make finite natural-grid data sensitive to the reciprocal-height Burnol defect. The same support shape can be moved vertically, exactly re-fit to the same prefix, and kept uniformly conditioned with respect to height. Along recurrent shifts, even finite coefficient and multibase phase data become indistinguishable from their low-height values.

It does **not** remove the two source-specific routes that have survived the recent negative controls.

First, the construction has rank `R`. Nothing here gives a comparable exact interpolation with rank `o(R)`, so the low-rank recurrence obstructions of `NB-123`--`NB-125` remain meaningful. Second, `(8)` is only height-uniform. As `R` grows or `delta` shrinks, `||V^{-1}||` can deteriorate catastrophically; a genuinely useful **uniform-in-cutoff coefficient/model-space bound** could still separate actual approximants from these controls. This is exactly the conditioning loophole already exposed by `NB-130`, now sharpened by showing that absolute height is not the source of that conditioning.

Most importantly, actual zeta-zero packets cannot be translated at will. Any positive result may therefore use arithmetic geometry of the real zero set: zero counting, spacing, horizontal location, symmetry, residues/derivative weights, or another source-specific compatibility absent from `(9)`. `NB-128` also remains relevant at growing cutoff: the full natural grid has quantitative phase resolution over a large height window. `NB-131` says only that **at every fixed cutoff**, exact reinterpolation defeats a height-blind finite certificate unless one also controls rank, conditioning, or actual-zero provenance.

## 5. Adversarial and prior-art audit

The kill checks are straightforward but important:

- the conjugation sign in `(13)` gives the multiplier `n^{+iS}`, so `(6)`--`(7)` are consistent;
- `D_S` is exactly unitary, hence singular values and the `2`-norm condition number of `V(S)` are independent of `S`;
- the coefficient bound is deliberately **not** claimed uniform in `R` or `delta`;
- re-solving coefficients cannot affect `(20)`, because `tau(F_S)` depends only on the formal support;
- real parts remain in `(1/2,1)` under every translation;
- simple roots already suffice, so no confluent/multiplicity assumption is hidden;
- the simultaneous return `(21)` is needed only for the strengthened finite-descriptor statement, not for the exact-prefix/Burnol decoupling itself;
- no statement is made that translated support points are actual zeros of `zeta`.

A selective prior-art check found the expected neighboring ingredients: classical finite exponential/Vandermonde interpolation and Burnol's zero-sensitive lower-bound/Blaschke framework for Nyman--Beurling approximation. No searched source supplied the line-local splice used here—translate a formal zero-power interpolation support, re-solve to keep the entire finite natural prefix exact, and compare that exact invariant data with the vanishing finite-packet Burnol defect. No external theorem is load-bearing beyond facts already proved or anchored on this research line, so `SOURCES.md` requires no change.

The representation audit also passes: the canonical object is one exact theorem/no-go statement with fixed quantifiers and explicit scope. No clue promotion, `mind/**` update, graph mutation, review sidecar, or source change is warranted.