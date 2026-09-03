# AF-077 — The canonical compact disk is the minimal functorial witness envelope

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a real Banach space and let `A\subset V` be nonempty and bounded. Define the canonical closed absolutely convex hull

\[
D_V(A)
=
\overline{\operatorname{aconv}}(A)
=
\overline{\operatorname{conv}}(A\cup(-A)),
\tag{1}
\]

where closure is in the norm topology of `V`.

Then:

1. **Canonical-disk compactness is exactly precompactness.**
   \[
   \boxed{
   A\text{ is relatively norm-compact}
   \iff
   D_V(A)\text{ is norm-compact}.
   }
   \tag{2}
   \]
   Thus AF-074's pooled-precompactness resource has a canonical envelope: one need not choose an auxiliary null sequence or compact operator merely to obtain a common compact reservoir.

2. **`D_V(A)` is the smallest closed absolutely convex envelope, and when `A` is precompact it is the smallest compact one.** If `C\subset V` is closed and absolutely convex with `A\subseteq C`, then
   \[
   D_V(A)\subseteq C.
   \tag{3}
   \]
   Hence, when `A` is relatively compact, every compact closed absolutely convex witness envelope containing `A` contains `D_V(A)`.

3. **The canonical disk generates a compactly embedded Banach space.** Assume `A` is relatively compact and put
   \[
   D=D_V(A).
   \]
   On
   \[
   E_A=\operatorname{span}D
   \]
   define the Minkowski gauge
   \[
   p_A(x)
   =
   \inf\{r>0:x\in rD\}.
   \tag{4}
   \]
   Then `(E_A,p_A)` is a Banach space, its closed unit ball is exactly `D`, and the inclusion
   \[
   J_A:E_A\hookrightarrow V
   \tag{5}
   \]
   is compact with
   \[
   J_A(B_{E_A})=D_V(A).
   \tag{6}
   \]
   Therefore
   \[
   \boxed{
   A\text{ is relatively compact}
   \iff
   \exists\text{ a Banach space }E\text{ and compact linear }J:E\to V
   \text{ with }A\subseteq\overline{J(B_E)}.
   }
   \tag{7}
   \]
   Among all such closed absolutely convex operator envelopes, the canonical construction `(E_A,J_A)` is minimal in `V` by inclusion.

4. **Bounded linear post-processing acts functorially on the canonical envelope.** Let `B:V\to W` be bounded linear into another real Banach space and assume `A` is relatively compact. Then
   \[
   \boxed{
   B(D_V(A))=D_W(B(A)).
   }
   \tag{8}
   \]
   In particular the restriction
   \[
   \widetilde B:E_A\to E_{B(A)},
   \qquad
   \widetilde Bx=Bx,
   \tag{9}
   \]
   is a surjective contraction satisfying
   \[
   \widetilde B(B_{E_A})=B_{E_{B(A)}}.
   \tag{10}
   \]
   Hence `E_{B(A)}` carries exactly the quotient norm induced by `\widetilde B`:
   \[
   \boxed{
   E_{B(A)}\cong E_A/\ker\widetilde B
   }
   \tag{11}
   \]
   isometrically.

5. **AF-074 compact-transversal fidelity therefore has a canonical compact-embedding certificate.** For any AF-074 finite approximation scheme `(F_n,\varepsilon_n)` with pooled witness set
   \[
   A=\bigcup_{n\ge1}F_n,
   \tag{12}
   \]
   the pooled-precompactness condition is equivalent to compactness of `D_V(A)`, and equivalently to compactness of the canonical inclusion `J_A:E_A\hookrightarrow V`. Thus AF-074's exact margin `\kappa_{\mathcal K}(L)=\tau_{\mathcal K}(L)` can be read without choosing AF-076's auxiliary generator sequence: positive compact-target failure exists exactly when arbitrarily accurate finite witnesses can be selected at positive target margin so that their **canonical disk** is compact.

6. **Canonicity moves one level upstream rather than solving provenance by itself.** Once the pooled witness family `A` has been specified, `D_V(A)` and `E_A` are forced. But a research construction may still have many inequivalent ways to select the finite witnesses whose union is `A`. Therefore AF-077 removes the noncanonicity of the *envelope choice* identified in AF-076; it does not remove the need to derive the witness family itself intrinsically from the source mathematics.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{precompact cross-scale provenance has a canonical minimal absolutely convex carrier;}\\
\text{that carrier is the unit ball of a compactly embedded Banach space;}\\
\text{bounded linear compression sends the carrier to the canonical carrier of the image}\\
\text{and acts exactly by a Banach-space quotient.}
\end{array}}
\tag{13}
\]

This gives a precise composition rule unavailable in AF-076's existential null-sequence presentation. The common compact resource cannot acquire new directions under bounded linear post-processing: it is functorially quotiented. Any discriminator lost in `\ker\widetilde B` is therefore absent from the canonical downstream provenance space and cannot be restored there without adding extra structure.

## Derivation

### Relative compactness makes the canonical disk compact

Suppose `A` is relatively norm-compact and put

\[
K=\overline A.
\tag{14}
\]

Then `K` is compact. The symmetric compact set

\[
H=K\cup(-K)
\tag{15}
\]

is compact as well. In a Banach space, more generally in a complete Hausdorff locally convex space, the closed convex hull of a compact set is compact. Therefore

\[
\overline{\operatorname{conv}}(H)
\tag{16}
\]

is compact.

Because a convex symmetric set contains `0` and is balanced over real scalars of modulus at most one,

\[
\overline{\operatorname{conv}}(H)
=
\overline{\operatorname{aconv}}(K)
=
\overline{\operatorname{aconv}}(A)
=D_V(A).
\tag{17}
\]

Thus relative compactness of `A` implies compactness of `D_V(A)`.

Conversely,

\[
A\subseteq D_V(A).
\tag{18}
\]

If the latter is compact, every subset of it is relatively compact. This proves (2).

The Banach completeness hypothesis is load-bearing in the forward direction. In an incomplete locally convex normed space the closed convex hull of a compact set need only be precompact in the ambient completion and may fail to be compact in the original space.

### Minimality is built into the hull

Let `C\subset V` be closed and absolutely convex with `A\subseteq C`. Since `C` contains every finite absolutely convex combination of points of `A`,

\[
\operatorname{aconv}(A)\subseteq C.
\tag{19}
\]

Closedness then gives

\[
D_V(A)=\overline{\operatorname{aconv}}(A)\subseteq C,
\tag{20}
\]

which is (3). If `A` is precompact, `D_V(A)` itself is compact by (2), so it is the unique least element of the inclusion order on compact closed absolutely convex envelopes of `A`.

This is stronger than AF-076's statement that *some* null-sequence synthesis envelope exists. Such an envelope may be much larger than necessary and is highly nonunique. The canonical disk is forced by `A` alone.

### A compact disk is a Banach disk

Assume now that `D=D_V(A)` is compact. It is closed, bounded, absolutely convex, contains `0`, and is absorbing in its algebraic span `E_A=\operatorname{span}D`. The Minkowski gauge `p_A` in (4) is therefore a seminorm on `E_A`.

Because `D` is bounded in the Hausdorff normed space `V`, the gauge is actually a norm. Let

\[
M=\sup_{d\in D}\|d\|_V<\infty.
\tag{21}
\]

For every `x\in E_A` and every `r>p_A(x)` one has `x\in rD`, so

\[
\|x\|_V\le rM.
\]

Letting `r\downarrow p_A(x)` gives

\[
\|x\|_V\le M p_A(x).
\tag{22}
\]

Hence `p_A(x)=0` implies `x=0`.

Closedness of `D` gives the exact unit-ball identity

\[
\{x\in E_A:p_A(x)\le1\}=D.
\tag{23}
\]

Indeed, if `p_A(x)\le1`, then for every `r>1` one has `x\in rD`; equivalently `x/r\in D`. Letting `r\downarrow1` in `V` and using closedness of `D` yields `x\in D`.

To prove completeness, let `(x_n)` be `p_A`-Cauchy. Equation (22) makes it norm-Cauchy in `V`, so

\[
x_n\to x\in V.
\tag{24}
\]

Fix `\varepsilon>0`. For large `n,m`,

\[
p_A(x_n-x_m)\le\varepsilon,
\]

so by (23)

\[
x_n-x_m\in\varepsilon D.
\tag{25}
\]

Let `m\to\infty` in `V`. Since `\varepsilon D` is compact and hence closed,

\[
x_n-x\in\varepsilon D.
\tag{26}
\]

Thus `x\in E_A` and `p_A(x_n-x)\le\varepsilon`. Therefore `(E_A,p_A)` is Banach.

The inclusion `J_A` is bounded by (22), and its closed unit ball maps exactly to compact `D`. Hence `J_A` is compact and (6) holds.

### Compact operator envelopes all contain the canonical disk

Let `E` be a Banach space and let `J:E\to V` be compact. Then

\[
C_J=\overline{J(B_E)}
\tag{27}
\]

is compact. Because `B_E` is absolutely convex and `J` is linear, `C_J` is closed and absolutely convex. If

\[
A\subseteq C_J,
\tag{28}
\]

minimality (3) gives

\[
D_V(A)\subseteq C_J.
\tag{29}
\]

Conversely, when `A` is precompact, the canonical compact inclusion `J_A` itself satisfies

\[
A\subseteq J_A(B_{E_A})=D_V(A).
\tag{30}
\]

This proves (7) and the operator-envelope minimality statement.

Note that the closure in (27) is necessary for arbitrary compact operators: a compact operator is required to have relatively compact unit-ball image, not necessarily a closed one. The canonical inclusion is stronger because its unit-ball image is the compact disk itself and is therefore closed.

### Functoriality under bounded linear compression

Let `B:V\to W` be bounded linear and let `A` be relatively compact. Since `D_V(A)` is compact, its continuous image

\[
B(D_V(A))
\tag{31}
\]

is compact and therefore closed in `W`. It is absolutely convex and contains `B(A)`. Minimality of the downstream disk gives

\[
D_W(B(A))\subseteq B(D_V(A)).
\tag{32}
\]

For the reverse inclusion, continuity and linearity give

\[
\begin{aligned}
B(D_V(A))
&=B\!\left(\overline{\operatorname{aconv}}(A)\right)\\
&\subseteq\overline{B(\operatorname{aconv}(A))}\\
&=\overline{\operatorname{aconv}}(B(A))\\
&=D_W(B(A)).
\end{aligned}
\tag{33}
\]

Combining (32) and (33) proves (8).

Because

\[
B(\operatorname{span}D_V(A))
=
\operatorname{span}D_W(B(A)),
\tag{34}
\]

the restriction `\widetilde B` in (9) is surjective. If `x\in rD_V(A)`, then by (8)

\[
Bx\in rD_W(B(A)),
\]

so

\[
p_{B(A)}(Bx)\le p_A(x).
\tag{35}
\]

Thus `\widetilde B` is a contraction.

Equation (8) also yields exact unit-ball surjectivity (10). Let

\[
q(y)=\inf\{p_A(x):\widetilde Bx=y\}
\tag{36}
\]

be the quotient seminorm. The contraction estimate gives

\[
p_{B(A)}(y)\le q(y).
\tag{37}
\]

Conversely, if `r=p_{B(A)}(y)>0`, then `y/r\in D_W(B(A))=B(D_V(A))`, so there exists `x_0\in D_V(A)` with

\[
Bx_0=y/r.
\]

Taking `x=rx_0` gives

\[
q(y)\le p_A(x)\le r=p_{B(A)}(y).
\tag{38}
\]

The zero case is immediate. Hence `q=p_{B(A)}` and (11) follows.

This is the exact compression law: once cross-scale provenance is encoded by the canonical compact disk, every bounded linear downstream map acts on that provenance space by quotienting out precisely its kernel directions.

## Exact controls

### Boundedness without precompactness does not produce a compact disk

Let `V=\ell^2` and

\[
A=\{e_n:n\ge1\}
\tag{39}
\]

for the standard orthonormal basis. `A` is bounded but not relatively compact. Since `A\subseteq D_V(A)`, the canonical disk cannot be compact. Thus taking a closed absolutely convex hull does not manufacture compact provenance from a jumping witness family; AF-073--AF-075's escape obstruction survives canonicalization unchanged.

### Compact canonical disks can remain genuinely infinite-dimensional

In `V=\ell^2`, take

\[
A=\left\{\frac{e_n}{n}:n\ge1\right\}\cup\{0\}.
\tag{40}
\]

Then `A` is compact, so `D_V(A)` is compact by (2), while its linear span is infinite-dimensional. Hence the canonical compact-embedding certificate is not an eventual finite-dimensional truncation statement. It packages a genuinely infinite-dimensional carrier whose unit ball is compact only in the weaker ambient `V` norm.

### Functoriality does not imply discriminator fidelity

Take any nontrivial precompact `A` and let

\[
B=0.
\]

Then

\[
D_W(B(A))=\{0\}=B(D_V(A)),
\tag{41}
\]

and `E_A` is quotiented completely to the zero space. Equation (8) therefore tracks provenance/non-escape under composition, not injectivity or recovery. AF-001/AF-002-style fiber tests remain necessary for the discriminator itself.

### The witness pool can still be chosen post hoc

Suppose a finite-resolution problem admits many alternative witness sets `F_n`. AF-077 canonically constructs the envelope only after one pooled family

\[
A=\bigcup_nF_n
\]

has been selected. Different selections can yield different canonical disks and different compact-embedding spaces. Therefore the theorem does not authorize choosing witnesses after inspecting the desired downstream discriminator and then calling the resulting disk intrinsic. Source-level naturality has moved from the envelope to the witness-selection rule.

## Prior art and novelty assessment

All functional-analytic ingredients are classical.

- François Trèves, ***Topological Vector Spaces, Distributions and Kernels***, Dover reprint (2006; original Academic Press edition 1967), especially the compactness discussion around the closed convex hull of compact sets in complete locally convex spaces and the later auxiliary-space/Banach-disk construction. Role: authoritative background for the compact closed-convex-hull step and for Minkowski-gauge spaces generated by bounded disks.
- Lawrence Narici and Edward Beckenstein, ***Topological Vector Spaces***, 2nd ed., Chapman & Hall/CRC (2011), especially the chapters on compactness in locally convex spaces and Banach disks. Role: modern systematic source for total boundedness/compactness under convex and balanced hulls in complete spaces, and for the criterion that a bounded complete disk generates a Banach space under its gauge.
- Ignacio Monterde and Vicente Montesinos, **“Convex-compact sets and Banach discs,”** *Czechoslovak Mathematical Journal* 59(3), 773–780 (2009), DOI `10.1007/s10587-009-0046-y`. Role: direct prior art for embedding suitable convex-compact subsets of locally convex spaces into Banach disks and for the structural importance of the generated gauge space.
- Alexander Grothendieck, **“Critères de compacité dans les espaces fonctionnels généraux,”** *American Journal of Mathematics* 74(1), 168–186 (1952), DOI `10.2307/2372076`. Role: foundational compactness/factorization background adjacent to the compact-disk and compact-operator representations used here.

No novelty is claimed for closed absolutely convex hulls, compactness of closed convex hulls of compact sets in Banach spaces, Minkowski gauges, Banach disks, compact embeddings, or quotient norms. The minimality of `D_V(A)` is definitional once the hull is chosen, and the functorial identity (8) is an elementary consequence of compactness plus linearity.

The durable Arithmetic Fidelity contribution is the way these classical pieces close the canonicity gap left by AF-076 and sharpen the composition law for the exact AF-074 fidelity resource. AF-076 showed that a precompact pooled witness family lies in *some* null-sequence synthesis envelope, but that representation is noncanonical. AF-077 shows that the pooled family itself forces one least compact absolutely convex envelope and one associated compactly embedded Banach space. In that canonical representation, every bounded linear downstream compression becomes an exact quotient. This separates two questions cleanly: **assembly provenance** is carried functorially by the compact disk, while **discriminator survival** is exactly the additional question of whether the relevant quotient kernel removes the source distinction.

## Boundary conditions and audit

- **Banach completeness is essential to (2) as stated.** In an incomplete normed/local-convex space, the closed convex hull of a compact set may fail to be compact even though it is precompact in the completion.
- **The theorem is real-linear as stated.** A complex version uses the complex balanced/absolutely convex hull and the same gauge argument; no complex-specific novelty is asserted.
- **`A` must be bounded to obtain a normed gauge space.** Relative compactness implies boundedness automatically, but the bounded hypothesis keeps the canonical disk/gauge construction meaningful before compactness is known.
- **The canonical disk is minimal only within the declared envelope category.** It is least among closed absolutely convex subsets of `V` containing `A`. A nonlinear, nonconvex, marked, ordered, or category-enriched carrier can retain information that the disk deliberately forgets.
- **Absolute convexification may erase discriminators.** The theorem uses `D_V(A)` only as a canonical compact provenance envelope. It does not assert that points introduced by convexification are genuine source states or that the hull preserves phase, sign, marking, arithmetic provenance, or another target discriminator.
- **Compactness of the inclusion is ambient-topology dependent.** Replacing the norm topology by weak, weak-*, or another topology changes both the disk compactness theorem and the meaning of compact embedding.
- **Functoriality requires bounded linear post-processing.** For a nonlinear map `F`, generally `F(D_V(A))` need not equal the canonical disk of `F(A)` and no quotient-space law follows.
- **The quotient law is not a recovery theorem.** It identifies exactly how the canonical assembly carrier changes. A discriminator is recoverable downstream only if it is constant on the relevant quotient fibers or an independently justified lift restores the missing relation.
- **Canonicity is conditional on the witness family.** AF-077 does not solve the remaining RH-specific problem identified in AF-076: the finite witnesses, or an equivalent common carrier, must still be forced by source arithmetic rather than chosen to encode the desired conclusion.

## Consequences for Arithmetic Fidelity

AF-073--AF-076 progressively identified cross-scale provenance as a compactness resource: explicit Hausdorff coherence, pooled precompactness, width decay, and one common null-sequence synthesis envelope were equivalent ways to prevent finite-resolution witnesses from escaping every common reservoir.

AF-077 removes an unnecessary existential choice from that hierarchy. For a fixed pooled witness family `A`, the relevant compact carrier is canonically

\[
D_V(A)=\overline{\operatorname{aconv}}(A),
\]

and its gauge space `E_A` is the canonical compactly embedded Banach source generated by those witnesses. A bounded linear compression does not merely preserve existence of *some* compact envelope as in AF-076; it sends the canonical disk exactly to the canonical downstream disk and turns the provenance space into the corresponding quotient.

The next live question is therefore no longer “can one choose a canonical compact envelope?” at this level: yes, once the witnesses are fixed. The unresolved question has moved to a sharper and more application-relevant boundary: **which source-natural witness-selection or carrier rule is forced before convexification, and which discriminators survive the quotient kernel of the actual downstream operator?** For RH-facing applications, the useful audit is consequently two-stage: derive the witness pool/common carrier without target-dependent choice, then test whether the prime-specific discriminator survives the canonical quotient induced by the proposed analytic or spectral compression.