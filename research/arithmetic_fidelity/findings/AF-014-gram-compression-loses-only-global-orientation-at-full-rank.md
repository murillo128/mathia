# AF-014 — Gram compression loses only global orientation at full rank

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`

## Claim

Let

\[
X\in\mathbb R^{d\times n},
\qquad
X=(x_1\ \cdots\ x_n),
\]

be an ordered real vector configuration, and compress it to its positive-semidefinite Gram matrix

\[
\Gamma(X)=X^\top X.
\]

Then the fidelity of this compression depends sharply on the intended geometric gauge.

1. **Gram is complete modulo the full orthogonal group.** If
   \[
   X^\top X=Y^\top Y,
   \]
   then there exists `Q in O(d)` with
   \[
   Y=QX.
   \]
   If `rank(X)=d`, this `Q` is unique.

2. **At full row rank, one Gram fiber contains exactly two `SO(d)`-orbits.** If `rank(X)=d`, the unique orthogonal transporter has determinant `+1` or `-1`. Hence two configurations with the same Gram matrix are `SO(d)`-equivalent exactly when the transporter has determinant `+1`. The quotient defect is precisely
   \[
   O(d)/SO(d)\cong\{\pm1\}.
   \]

3. **Gram retains every relative maximal-minor sign.** For each increasing `d`-subset `I` of `{1,...,n}`, let
   \[
   p_I(X)=\det X_I,
   \]
   and let `p(X)` be the vector of all such maximal minors. For any `d`-subsets `I,J`,
   \[
   \det\Gamma(X)_{I,J}
   =\det(X_I^\top X_J)
   =p_I(X)p_J(X).
   \]
   Therefore the `d`th compound-minor matrix of the Gram matrix is the rank-at-most-one outer product
   \[
   C_d(\Gamma(X))=p(X)p(X)^\top.
   \]
   On the full-rank locus it has rank one because `p(X)\ne0`, and the Gram matrix determines the whole maximal-minor vector up to one common sign:
   \[
   \Gamma(X)=\Gamma(Y)
   \Longrightarrow
   p(Y)=\pm p(X).
   \]
   Thus quadratic/PSD compression does **not** erase the determinant signs independently. It preserves their zero pattern, magnitudes, pairwise products, and all relative signs; only the global simultaneous reversal remains ambiguous.

4. **One nonzero maximal-minor sign repairs the full-rank `SO(d)` defect.** Fix the column order. From a rank-`d` Gram matrix `G`, choose deterministically, for example, the lexicographically first `d`-subset `I_*(G)` with
   \[
   \det G_{I_*,I_*}>0.
   \]
   Then
   \[
   \left(G,\operatorname{sgn}\det X_{I_*(G)}\right)
   \]
   is a complete invariant of `X` up to `SO(d)`. Once the sign fixes
   \[
   p_{I_*}=\operatorname{sgn}(p_{I_*})\sqrt{\det G_{I_*,I_*}},
   \]
   every maximal minor is recovered from
   \[
   p_J=\frac{\det G_{J,I_*}}{p_{I_*}}.
   \]

5. **The two-valued lift is cardinality-minimal on every full-rank Gram fiber.** A reflection `R in O(d)\setminus SO(d)` gives `\Gamma(RX)=\Gamma(X)` but changes the `SO(d)`-orbit. Any mark that makes Gram complete modulo `SO(d)` must distinguish these two classes, so it needs at least two values on such a fiber. An orientation sign attains that lower bound. Intrinsically, the missing datum is a two-element orientation torsor; identifying it with a literal `+/-` bit requires a choice of orientation/trivialization or an ordering convention.

6. **The orientation defect disappears at rank deficiency.** If `rank(X)<d` and `X^\top X=Y^\top Y`, then `X` and `Y` are already `SO(d)`-equivalent. Therefore the twofold chirality defect exists exactly on the configurations that span the ambient space.

The resulting Arithmetic Fidelity lesson is sharper than the slogan that positivity or Gram formation destroys sign. The PSD Gram summary is fully faithful for orthogonal geometry, and even relative to orientation-preserving geometry it loses only one global orientation class at full rank while retaining all relative signed-volume structure.

## Derivation

### Equal Gram matrices are exactly orthogonal congruence

Assume

\[
X^\top X=Y^\top Y.
\]

Define a linear map on the column span of `X` by

\[
U(Xa)=Ya,
\qquad a\in\mathbb R^n.
\]

This is well defined. Indeed,

\[
\|Xa\|^2
=a^\top X^\top Xa
=a^\top Y^\top Ya
=\|Ya\|^2,
\]

so `Xa=0` implies `Ya=0`. The same identity, applied after polarization, gives

\[
\langle Xa,Xb\rangle=\langle Ya,Yb\rangle.
\]

Thus `U` is an isometry from `span{x_i}` onto `span{y_i}`. Extend it orthogonally to all of `R^d`; the extension is some `Q in O(d)` and satisfies

\[
Y=QX.
\]

If `rank(X)=d`, the columns span all of `R^d`, so `Q` is already determined on the whole ambient space and is unique.

Hence

\[
\boxed{
\Gamma(X)=\Gamma(Y)
\iff
Y=QX\text{ for some }Q\in O(d).
}
\]

This is the exact fiber of Gram compression. Consequently Gram formation is not intrinsically lossy: it is lossless whenever `O(d)` is the intended gauge.

### Full rank splits the orthogonal fiber into two oriented classes

Now assume `rank(X)=d`. For any `Y` with the same Gram matrix, let `Q` be the unique orthogonal map with `Y=QX`.

If `det Q=+1`, then `Q in SO(d)` and the configurations are orientation-preservingly congruent. If `det Q=-1`, suppose instead that some `S in SO(d)` also satisfied `Y=SX`. Full row rank would force `S=Q`, contradicting their determinants. Therefore the `det=-1` case is a genuinely different `SO(d)`-orbit.

Both cases occur: if `R` is any reflection, then

\[
\Gamma(RX)=X^\top R^\top RX=X^\top X,
\]

while `R` has determinant `-1`.

So the full-rank Gram fiber, which is one free `O(d)`-orbit, splits into exactly the two cosets of `SO(d)` in `O(d)`.

An explicit two-dimensional witness is

\[
X=I_2,
\qquad
R=\begin{pmatrix}-1&0\\0&1\end{pmatrix},
\qquad
Y=RX.
\]

Both Gram matrices are `I_2`, but `det X=+1` and `det Y=-1`; the unique transporter is the reflection `R`, so no rotation sends the ordered configuration `X` to `Y`.

### Cross-minors of the Gram matrix retain relative orientation data

The previous argument identifies one global orientation ambiguity, but it does not yet say how much signed-volume structure survives inside `G=X^\top X`.

For increasing `d`-subsets `I,J`, the corresponding `d by d` Gram cross-minor is

\[
G_{I,J}=X_I^\top X_J.
\]

Taking determinants gives the exact identity

\[
\boxed{
\det G_{I,J}
=\det X_I\det X_J
=p_I(X)p_J(X).
}
\]

Collecting all maximal minors produces

\[
\boxed{
C_d(G)=p(X)p(X)^\top.
}
\]

If `rank(X)=d`, at least one coordinate `p_{I_0}` is nonzero. From the diagonal entry,

\[
|p_{I_0}|=\sqrt{\det G_{I_0,I_0}},
\]

and after choosing its sign every other coordinate is forced by

\[
p_J=\frac{\det G_{J,I_0}}{p_{I_0}}.
\]

Therefore `G` determines `p(X)` up to simultaneous negation. Equivalently, if two full-rank realizations have the same Gram matrix, then all their maximal-minor signs either agree simultaneously or reverse simultaneously. This is exactly what the orthogonal transporter predicts:

\[
p_I(QX)=\det(Q)p_I(X).
\]

In particular, Gram already determines the realizable determinant-sign pattern up to the conventional global reversal familiar from oriented-volume/chirotope descriptions. A claim that the PSD map has erased all orientation-bearing information is therefore too strong.

### A single sign is a complete and minimal oriented lift

Fix a deterministic way to select a nonzero maximal minor from `G`; with ordered columns, the lexicographically first positive principal `d`-minor is one simple choice. The selection depends only on `G`, so every realization of the same Gram matrix chooses the same subset `I_*`.

If two realizations have the same Gram matrix and the same sign of `p_{I_*}`, their unique orthogonal transporter cannot have determinant `-1`, because a determinant-`-1` transporter reverses every maximal minor. It therefore lies in `SO(d)`. Conversely an `SO(d)` transformation preserves both `G` and every maximal-minor sign.

Hence

\[
\boxed{
\left(\Gamma(X),\operatorname{sgn}p_{I_*(\Gamma(X))}(X)\right)
}
\]

classifies full-rank ordered configurations up to `SO(d)`.

Minimality is fiberwise. For any full-rank `X` and reflection `R`, the two configurations `X` and `RX` have the same Gram matrix but lie in different `SO(d)`-orbits. Therefore any repairing mark must take different values on those two classes. No one-valued mark can work, while a two-valued orientation mark does.

The qualifier about conventions matters. The quotient defect is intrinsically the two-element torsor `O(d)/SO(d)`. Writing its elements as `+1` and `-1`, or choosing the lexicographically first nonzero minor, uses additional conventions. The mathematical minimality claim is about the two classes, not about one privileged encoding of them.

### Rank deficiency absorbs the reflection in the invisible complement

Assume `rank(X)=r<d` and

\[
Y=QX,
\qquad Q\in O(d).
\]

If `det Q=+1`, there is nothing to prove. If `det Q=-1`, the orthogonal complement of `span{x_i}` has positive dimension. Choose a reflection `S in O(d)` that acts as the identity on `span{x_i}` and reverses one direction in its orthogonal complement. Then

\[
SX=X,
\qquad
\det S=-1.
\]

Therefore

\[
(QS)X=QX=Y,
\qquad
\det(QS)=+1.
\]

Thus `QS in SO(d)` also transports `X` to `Y`. The `O(d)`- and `SO(d)`-orbits coincide whenever the configuration fails to span the ambient space.

For example,

\[
X=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
Y=\begin{pmatrix}-1&0\\0&0\end{pmatrix}
\]

have the same Gram matrix. A reflection sends `X` to `Y`, but so does the rotation `-I_2 in SO(2)`. All `2 by 2` minors vanish, consistently with the absence of an ambient chirality discriminator.

## Prior art and novelty assessment

The mathematical ingredients are classical. Gram matrices classify real vector configurations up to orthogonal congruence; the determinant identity above is elementary Cauchy-Binet/compound-matrix algebra; and the determinant-sign language is standard in oriented-volume and oriented-matroid treatments. The Gram/orthogonal background is already anchored in `SOURCES.md` through Horn and Johnson's *Matrix Analysis* under AF-006.

No novelty is claimed for those theorems. The Arithmetic Fidelity contribution is the exact compression audit obtained by combining them:

- the answer depends on the **declared gauge** (`O(d)` versus `SO(d)`), not on the fact that the output is positive-semidefinite;
- full-rank Gram compression loses exactly one global orientation torsor relative to `SO(d)`, rather than independently losing all signed-volume information;
- the Gram cross-minors retain the complete maximal-minor vector up to common sign;
- one two-valued orientation mark is sufficient and cardinality-minimal on full-rank fibers;
- the defect disappears abruptly on the rank-deficient boundary because the unused orthogonal complement can absorb a reflection.

This makes the example a precise model of how a positive quadratic compression may preserve far more provenance than its scalar/signless appearance suggests.

## Boundary conditions and falsification tests

- **Gauge dependence is essential.** If reflection is already an allowed equivalence, Gram is complete and there is no missing orientation to repair.
- **Full rank is essential for the twofold split.** At rank `< d`, the reflection can be moved into the orthogonal complement and the `SO(d)` defect vanishes.
- **Column identity/order is part of this object.** If the target additionally quotients by column permutations or other relabelings, that new quotient must be audited separately; the lexicographic pivot convention is not permutation-natural.
- **The lift is not a hidden frame.** It contributes only the missing two-class orientation datum; all lengths, angles, and relative maximal-minor products are already recoverable from `G`.
- **The theorem is real and finite-dimensional.** Complex unitary phase, indefinite forms, noisy/approximate Gram data, and infinite-dimensional settings have different stabilizers and require separate analysis.
- **No arithmetic consequence follows by itself.** This finding only invalidates blanket heuristics such as "PSD/Gram formation necessarily erases every sign or orientation discriminator." A concrete arithmetic line would still have to identify its intended gauge and show which arithmetic discriminator lives in the surviving Gram data or in the residual orientation torsor.

## Consequences for Arithmetic Fidelity

This example supplies a useful audit order for positive or quadratic compressions:

1. identify the equivalence relation the application actually cares about;
2. compute the exact compression fiber modulo that equivalence;
3. inspect algebraic cross-relations in the compressed object before declaring sign/provenance lost;
4. locate the smallest residual quotient defect;
5. add only a mark that separates that defect, and check what happens on singular strata.

For Gram compression the result is unusually sharp:

\[
\boxed{
\text{full geometry}/O(d)
\quad\xrightarrow[\text{Gram}]{\cong}\quad
\text{PSD Gram data},
}
\]

while on the full-rank oriented quotient

\[
\boxed{
\text{full geometry}/SO(d)
\longrightarrow
\text{PSD Gram data}
}
\]

has exactly a two-element orientation fiber, repaired by one orientation-class mark. On lower-rank strata even that residual fiber collapses.

This complements AF-006. There, the full per-eigenspace Gram matrix restores relations between spectral marks up to unitary gauge. Here, Gram compression itself is audited: it is already relationally complete modulo orthogonal gauge, and its remaining oriented defect is both exact and minimal.