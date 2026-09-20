# MC-420 — Lattice rank, not ambient dimension, controls the positive-kernel Fejér floor

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-419` proves that a genuinely `d`-variable positive stationary kernel with rectangular bandwidths `H_1,...,H_d` can lower its forced zero-mode floor to reciprocal bandwidth volume `1/(H_1...H_d)`. Its main unresolved boundary was whether an apparently multivariable arithmetic lift really carries that many independent translation directions.

There is an exact support-rank test.

Let `G` be a complex Hilbert space. Let

\[
A:\mathbb Z^r\hookrightarrow \mathbb Z^d
\tag{1}
\]

be an injective integer homomorphism, represented by a `d x r` integer matrix of rank `r`. Consider an operator-valued trigonometric polynomial on `T^d` whose Fourier support is contained in the lattice image of `A`:

\[
P(\theta)
=
\sum_{\substack{k\in\mathbb Z^r\\ |k_j|<H_j}}
K_k\,e\!\left((Ak)\cdot\theta\right),
\qquad
P(\theta)\succeq0.
\tag{2}
\]

Define

\[
Q(\eta)
:=
\sum_{\substack{k\in\mathbb Z^r\\ |k_j|<H_j}}
K_k e(k\cdot\eta),
\qquad
\eta\in\mathbb T^r.
\tag{3}
\]

Then

\[
\boxed{
P(\theta)=Q(A^T\theta).
}
\tag{4}
\]

The torus homomorphism

\[
\Phi_A:\mathbb T^d\to\mathbb T^r,
\qquad
\Phi_A(\theta)=A^T\theta
\tag{5}
\]

is surjective because its dual map is the injection `(1)`. Therefore positivity of `P` is exactly positivity of `Q`, and normalized Haar measure pushes forward from `T^d` to normalized Haar measure on `T^r`. In particular,

\[
K_0
=
\int_{\mathbb T^d}P(\theta)\,d\theta
=
\int_{\mathbb T^r}Q(\eta)\,d\eta.
\tag{6}
\]

Applying the `r`-variable result of `MC-419` to `Q` gives, for every `theta in T^d`,

\[
\boxed{
P(\theta)
\preceq
\left(\prod_{j=1}^r H_j\right)K_0.
}
\tag{7}
\]

Equivalently,

\[
\boxed{
K_0
\succeq
\frac{1}{\prod_{j=1}^rH_j}P(\theta).
}
\tag{8}
\]

The constant is sharp for this lattice-box class: pull back the `r`-variable product Fejér extremizer through `Phi_A`.

Hence **ambient torus dimension is irrelevant when the Fourier support has lower lattice rank**. The positive diagonal floor is controlled by the bandwidth volume in the effective frequency lattice, not by the number of coordinates used to display the state.

The rank-one case is especially important for the current Möbius frontier. If

\[
P(\theta_x,\theta_y)
=
\sum_{|h|<H}K_h e\!\left(h(\theta_x-\theta_y)\right),
\qquad P\succeq0,
\tag{9}
\]

then the support lies on the anti-diagonal lattice `h -> (h,-h)` and

\[
\boxed{
P(0,0)\preceq H K_0,
}
\tag{10}
\]

not `H^2 K_0`. The sharp extremizer is simply the one-variable Fejér kernel pulled back by `theta_x-theta_y`.

This closes a concrete loophole left by the endpoint representation in `MC-414`: writing a translated correlation in two endpoint coordinates does **not** by itself earn the two-dimensional `1/H^2` floor of `MC-419`. If the positive closure still uses only the relative shift `x-y`, its Fourier support is rank one and it pays the original `1/H` diagonal floor.

No estimate for `M(x)`, no new character-sum bound, and no RH consequence follows.

## 1. Lower-rank Fourier support factors through a smaller torus

Because `A` is injective on `Z^r`, every frequency in its image has a unique representation `Ak`. Thus `(3)` is unambiguous and `(4)` is immediate:

\[
e((Ak)\cdot\theta)=e(k\cdot A^T\theta).
\tag{11}
\]

The only nontrivial structural point is surjectivity of `Phi_A`. For compact abelian groups, a continuous homomorphism has dense image exactly when its dual map is injective. The image of a compact group is compact, hence closed. Since the dual map of `(5)` is precisely

\[
\widehat{\Phi_A}:\mathbb Z^r\to\mathbb Z^d,
\qquad k\mapsto Ak,
\tag{12}
\]

and `(12)` is injective, `Phi_A` has dense and closed image, therefore is onto.

Consequently every `eta in T^r` is `A^T theta` for some `theta`. From `(4)`,

\[
P(\theta)\succeq0\ \forall\theta
\quad\Longleftrightarrow\quad
Q(\eta)\succeq0\ \forall\eta.
\tag{13}
\]

Likewise, the pushforward of normalized Haar measure under a surjective compact-group homomorphism is normalized Haar measure. Equation `(6)` follows. Nothing has been estimated or approximated: the apparently `d`-variable positive polynomial is exactly an `r`-variable positive polynomial written through a quotient map.

This is the precise version of the informal warning in `MC-419` that a diagonal or lower-rank embedding does not manufacture translation volume.

## 2. The sharp floor is inherited from the effective torus

The polynomial `Q` has coordinate degree at most `H_j-1` in its `j`th effective variable. By `MC-419`,

\[
Q(\eta)
\preceq
\left(\prod_{j=1}^rH_j\right)K_0.
\tag{14}
\]

Substituting `eta=A^T theta` gives `(7)`.

Sharpness is equally direct. Let `C\succeq0` be fixed and set

\[
Q(\eta)
=
C\prod_{j=1}^r
\left|\sum_{m=0}^{H_j-1}e(m\eta_j)\right|^2.
\tag{15}
\]

Then

\[
Q(0)=\left(\prod_jH_j^2\right)C,
\qquad
\int Q=\left(\prod_jH_j\right)C.
\tag{16}
\]

The pullback `P=Q circ Phi_A` has Fourier support in `A Z^r`, remains positive, has the same mean by `(6)`, and attains equality in `(7)` at every preimage of zero.

Thus no sharper universal constant can be extracted merely from the fact that the same support was embedded in a higher-dimensional ambient torus.

Rank alone is not a complete support invariant. The product `prod H_j` depends on the chosen effective lattice coordinates and on the actual support region inside them. Sparse non-box supports may have a stronger Turán-type extremal constant. What `(7)` proves is the exact reduction: support geometry must be measured **inside its generated frequency lattice**, not in the ambient coordinate box.

## 3. The two-endpoint lift of one relative shift remains one-dimensional

The endpoint variables isolated in `MC-414` are

\[
x=m+j,
\qquad
y=m,
\qquad
j=x-y.
\tag{17}
\]

At the source-phase level this is useful because

\[
\chi(m+j)\overline{\chi(m)}
=
\chi(x)\overline{\chi(y)}.
\tag{18}
\]

But phase factorization and translation rank are different questions.

The standard positive van der Corput kernel in `MC-415` is the one-variable Fejér polynomial

\[
F_H(t)
=
\sum_{|h|<H}(H-|h|)e(ht)
=
\left|\sum_{j=0}^{H-1}e(jt)\right|^2.
\tag{19}
\]

If one merely rewrites this closure in endpoint coordinates, its natural two-torus lift is

\[
\widetilde F_H(\theta_x,\theta_y)
=
F_H(\theta_x-\theta_y)
=
\sum_{|h|<H}(H-|h|)
 e(h\theta_x-h\theta_y).
\tag{20}
\]

Its Fourier support is exactly the anti-diagonal rank-one lattice

\[
\{(h,-h): |h|<H\}.
\tag{21}
\]

Moreover

\[
\widetilde F_H(0,0)=H^2,
\qquad
\int_{\mathbb T^2}\widetilde F_H=H,
\tag{22}
\]

so the ratio is exactly `H`, not `H^2`. Equation `(10)` is sharp on the nose.

Therefore the endpoint tensorization in `(18)` does not convert the ordinary one-shift positive closure into a genuine two-axis architecture. To invoke the `1/(H_1H_2)` floor from `MC-419`, the arithmetic construction must create Fourier support containing two `Z`-linearly independent translation directions before positivity is imposed.

That is a stronger requirement than having two endpoint labels or a source phase that algebraically factors into two endpoint characters.

## 4. What a genuine second axis would have to change

The result separates three increasingly strong statements:

1. **two coordinates in a representation** — `(x,y)` may encode the same one-dimensional data reversibly;
2. **two factors in a source phase** — `chi(x) overline{chi(y)}` may factor while the positive averaging still moves only along `x-y`;
3. **two independent Fourier directions in the positive closure** — only this can earn a two-dimensional bandwidth volume under `MC-419`.

The first two occur already in `MC-414`. They are insufficient.

A genuine escape must therefore produce, from the arithmetic source rather than by relabelling, a second translation action whose Fourier frequencies are not confined to the rank-one subgroup generated by `(1,-1)` (or by any other single lattice vector). It must then retain a reconstruction of the original Möbius target and control the resulting off-diagonal arithmetic terms.

This also rules out a common false gain. Suppose a proof takes the one-dimensional Fejér family, embeds each shift `h` as `(h,-h)` in a two-dimensional state, and then budgets the diagonal using the ambient rectangular constant `H^2`. That uses a valid but grossly non-sharp bound from `MC-419`; the exact quotient reduction shows that the admissible class still has only the one-dimensional `H` ratio. No extra factor `H` has been earned.

The same statement holds in arbitrary dimension: if all retained translations lie in an `r`-rank lattice, adding coordinates outside that lattice cannot improve the universal positive-kernel floor.

## 5. Prior art and novelty boundary

The group-theoretic mechanism is classical. Pontryagin duality identifies annihilators, subgroups, and quotients of locally compact abelian groups; in particular, Fourier data supported in a subgroup naturally factor through the corresponding quotient. Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962; Wiley reprint), develops the duality between subgroups and quotient groups and Fourier transforms on them. No novelty is claimed for `(4)`–`(6)` as abstract harmonic analysis.

The support-sensitive extremal boundary is also classical. Mihail N. Kolountzakis and Szilard Gy. Revesz, *On Pointwise Estimates of Positive Definite Functions With Given Support*, **Canadian Journal of Mathematics** 58 (2006), 401–418, DOI `10.4153/CJM-2006-017-8`, studies pointwise Turan-type extremal problems for positive-definite functions in `R^d` and `T^d` and emphasizes that support geometry, including effectively one-dimensional structure, governs the extremal problem. Wayne Lawton, *Spectral Factorization of Trigonometric Polynomials and Lattice Geometry*, **Acta Arithmetica** 155 (2012), 339–347, DOI `10.4064/aa155-3-9`, is adjacent prior art on how lattice geometry controls multivariable trigonometric-polynomial structure.

A targeted literature audit on 20 September 2026 found these ingredients and no basis for claiming a new harmonic-analysis theorem. The durable Mathia contribution is the frontier specialization: combining the exact quotient reduction with `MC-414` and `MC-415` proves that the obvious two-endpoint realization of the translated-character family **does not yet supply the independent translation dimension required by `MC-419`**. The standard positive relative-shift closure remains rank one and therefore keeps the one-dimensional Fejer floor.

## Boundaries and falsification tests

- **Fourier support in a fixed lattice image is load-bearing.** If the arithmetic construction produces frequencies outside `A Z^r`, the reduction to `T^r` no longer describes the full kernel.
- **The effective box is measured in lattice coordinates.** A poor choice of basis can inflate `prod H_j`; the theorem does not claim that this product is an invariant optimal constant for arbitrary sparse support.
- **The anti-diagonal application classifies the positive closure, not the source phase.** Equation `(18)` remains genuinely useful for bilinear character estimates on the divisor-dependent domain; the result only says that a relative-shift Fejer closure does not gain a second positive-kernel axis.
- **Two independent endpoint filters are a different architecture.** A product kernel such as `F_{H_1}(theta_x)F_{H_2}(theta_y)` has rank-two support and can achieve the `1/(H_1H_2)` floor. It is not ruled out here; it must be derived from the arithmetic problem and its reconstruction/off-diagonal costs must be paid.
- **Nonstationary or indefinite forms remain outside the theorem.** They may evade a stationary positive-kernel floor, but any negative part or base-point dependence requires independent control.
- **No character-sum theorem is imported.** The conclusion is representational/positive-kernel structure only and does not estimate the incomplete translated family left by `MC-413`–`MC-414`.
- **No RH-scale input is used.** The proof is finite Fourier algebra, compact-group duality, Haar pushforward, and the already-audited Fejer extremal inequality.

## Consequence for the research line

`MC-419` made genuine translation dimension the remaining positive-kernel escape hatch. `MC-420` supplies a decisive admission test for that phrase: **count the rank and geometry of the Fourier lattice actually generated by the arithmetic translations, not the number of coordinates in the retained state**.

For the current endpoint route, the ordinary relative-shift Fejer family fails this test exactly. Its lift to `(x,y)` is supported on one anti-diagonal lattice and still pays the `1/H` diagonal floor. The endpoint representation can still matter through the thin divisor-dependent domains and bilinear character estimates of `MC-414`, but it does not earn tensorized positive bandwidth for free.

The next positive-kernel candidate must therefore exhibit a second arithmetic translation direction that survives before positive closure and is not contained in the lattice generated by the original shift. If no such direction exists, further progress must come from source-specific off-diagonal cancellation, a nonstationary/indefinite architecture with separately controlled cost, or a different representation rather than from formal multivariable tensorization.