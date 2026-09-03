# AF-082 — Separable global Lipschitz quotient repair collapses to linear splitting

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` be a real or complex Banach space, let `K\subseteq E` be a closed linear subspace, and let

\[
q:E\longrightarrow F=E/K
\tag{1}
\]

be the normalized quotient map. Assume that the quotient `F` is separable. Define the best linear and global Lipschitz section costs by

\[
\lambda_{\mathrm{lin}}(q)
=
\inf\{\|V\|:V:F\to E\text{ bounded linear},\ qV=I_F\},
\tag{2}
\]

and

\[
\lambda_{\mathrm{Lip}}(q)
=
\inf\{\operatorname{Lip}(L):L:F\to E\text{ Lipschitz},\ qL=I_F\},
\tag{3}
\]

with the infimum of an empty family interpreted as `+\infty`. Then:

1. **Global Lipschitz representative selection has exactly the same optimal cost as linear splitting.**

   \[
   \boxed{
   \lambda_{\mathrm{Lip}}(q)=\lambda_{\mathrm{lin}}(q).
   }
   \tag{4}
   \]

   For real Banach spaces this is an immediate quantitative consequence of Godefroy--Kalton, Corollary 3.2: every Lipschitz right inverse of a quotient onto a separable Banach space produces a linear right inverse with the same Lipschitz/operator norm. The converse direction is tautological because every bounded linear section is Lipschitz with the same constant.

   For complex Banach spaces the same infimum identity follows by applying the real theorem to the underlying real spaces and then symmetrizing the resulting real-linear section without increasing its norm.

2. **There is no nonlinear global-Lipschitz escape from the AF-078 splitting gate when the quotient is separable.** Combining (4) with AF-078 gives

   \[
   \boxed{
   \begin{array}{c}
   q\text{ has a global Lipschitz right inverse}\\
   \Longleftrightarrow
   q\text{ has a bounded linear right inverse}\\
   \Longleftrightarrow
   K\text{ is complemented in }E.
   \end{array}}
   \tag{5}
   \]

   Thus enlarging the admissible section category from bounded linear maps to arbitrary globally Lipschitz maps does not enlarge the class of repairable separable quotients. Nonlinearity only creates a genuinely larger existence class after the regularity requirement is weakened below global Lipschitz stability.

3. **Positive-homogeneous global uniform continuity collapses to the same gate.** If a right inverse

   \[
   L:F\to E,
   \qquad qL=I_F,
   \tag{6}
   \]

   is positive homogeneous and globally uniformly continuous, then `L` is automatically globally Lipschitz. Hence, for separable `F`,

   \[
   \boxed{
   \begin{array}{c}
   \exists\text{ globally uniformly continuous positive-homogeneous section}\\
   \Longleftrightarrow
   \exists\text{ global Lipschitz section}\\
   \Longleftrightarrow
   \exists\text{ bounded linear section}.
   \end{array}}
   \tag{7}
   \]

   This is the exact content of the Godefroy--Kalton Corollaries 3.2--3.4 specialized to the Arithmetic Fidelity repair language. By contrast, mere continuity of a positive-homogeneous section is always available for Banach quotients through Bartle--Graves-type selection and therefore lies strictly below this stability threshold.

4. **AF-081's uncomplemented `\ell^p` metric repair is necessarily continuous but globally unstable.** Fix `1<p<\infty`, `p\ne2`, and choose a closed uncomplemented subspace

   \[
   K\subset\ell^p
   \tag{8}
   \]

   as in AF-081. Since `\ell^p` is separable, so is `F=\ell^p/K`. AF-081 gives the unique norm-minimal section

   \[
   s_K:F\to\ell^p,
   \qquad
   q s_K=I_F,
   \qquad
   \|s_K(y)\|=\|y\|_F,
   \tag{9}
   \]

   and uniform convexity makes `s_K` continuous and homogeneous. But (5) and uncomplementability force

   \[
   \boxed{
   s_K\text{ is not globally Lipschitz and is not globally uniformly continuous.}
   }
   \tag{10}
   \]

   In fact no global Lipschitz section of this quotient exists at all. This sharpens AF-081: the nonlinear metric construction bypasses linear nonsplitting only in a continuity-level category. Asking for global pairwise Lipschitz stability closes that escape and returns exactly to the linear obstruction.

5. **Radial norm fidelity does not imply pairwise stability.** The same metric section satisfies the strongest possible radial identity

   \[
   \|s_K(y)-s_K(0)\|=\|y\|_F,
   \tag{11}
   \]

   yet has infinite global Lipschitz constant in the uncomplemented control. Therefore preserving distance perfectly from one distinguished base point can coexist with arbitrarily bad distortion between pairs of retained states. This separates

   \[
   \text{radial fidelity}
   \quad\text{from}\quad
   \text{pairwise/global stability}.
   \tag{12}
   \]

6. **The `1`-Lipschitz endpoint is rigid for the AF-081 metric section.** Suppose more generally that `E` is reflexive and strictly convex, `F` is separable, and `s_K` is the unique minimum-norm section from AF-081. Then

   \[
   \boxed{
   s_K\text{ is }1\text{-Lipschitz}
   \Longleftrightarrow
   s_K\text{ is a linear isometric section of }q.
   }
   \tag{13}
   \]

   Indeed a `1`-Lipschitz section yields, by Godefroy--Kalton, a linear section `V` with `\|V\|\le1`; the quotient inequality forces `\|Vy\|=\|y\|`, and uniqueness of the minimum-norm representative gives `V=s_K`. The converse is immediate. Thus Hilbert-style nonexpansiveness is not a generic consequence of canonical metric recovery.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{repair must be indexed by both mathematical category and regularity;}\\
\text{for separable Banach quotients, global Lipschitz selection is no broader than linear splitting;}\\
\text{continuous canonical nonlinear selection may exist beyond splitting, but its global stability must then fail;}\\
\text{radial norm preservation does not certify pairwise fidelity.}
\end{array}}
\tag{14}
\]

## Derivation

### Real separable quotients: Godefroy--Kalton gives the reverse inequality

Every bounded linear section `V` satisfies

\[
\operatorname{Lip}(V)=\|V\|,
\tag{15}
\]

so immediately

\[
\lambda_{\mathrm{Lip}}(q)
\le
\lambda_{\mathrm{lin}}(q).
\tag{16}
\]

Conversely, let `L:F\to E` be any Lipschitz right inverse. Since `qL(0)=0`, one has `L(0)\in K`; replacing `L` by `L-L(0)` preserves both the right-inverse property and the Lipschitz constant, so assume `L(0)=0`.

For real Banach spaces, Godefroy and Kalton prove that a quotient map onto a separable Banach space with a Lipschitz right inverse `L` has a bounded linear right inverse `V` satisfying

\[
\|V\|=\operatorname{Lip}(L).
\tag{17}
\]

Therefore

\[
\lambda_{\mathrm{lin}}(q)
\le
\operatorname{Lip}(L)
\tag{18}
\]

for every admissible `L`. Taking the infimum and combining with (16) proves (4) in the real case.

### Complex quotients reduce to the real theorem without losing the cost inequality

Assume now that `E` and `F` are complex. Forget the complex scalars temporarily and apply the real theorem to obtain a bounded real-linear right inverse

\[
V_{\mathbb R}:F_{\mathbb R}\to E_{\mathbb R},
\qquad
qV_{\mathbb R}=I,
\qquad
\|V_{\mathbb R}\|=\operatorname{Lip}(L).
\tag{19}
\]

Define

\[
V_{\mathbb C}(y)
=
\frac12\bigl(V_{\mathbb R}(y)-iV_{\mathbb R}(iy)\bigr).
\tag{20}
\]

Then

\[
V_{\mathbb C}(iy)=iV_{\mathbb C}(y),
\tag{21}
\]

so `V_{\mathbb C}` is complex linear, and complex linearity of `q` gives

\[
qV_{\mathbb C}(y)
=
\frac12(y-i(iy))
=y.
\tag{22}
\]

Moreover

\[
\|V_{\mathbb C}\|
\le
\|V_{\mathbb R}\|
=
\operatorname{Lip}(L).
\tag{23}
\]

Thus every complex Lipschitz section produces a complex-linear section with no larger norm. Together with (16), this proves the same infimum identity (4) over the complex field. The source theorem itself is stated for real Banach spaces; the complex statement here is this elementary realification/symmetrization consequence.

### Positive homogeneity upgrades global uniform continuity to Lipschitz continuity

Let `L` be positive homogeneous and globally uniformly continuous. Choose `\delta>0` such that

\[
\|u-v\|<\delta
\quad\Longrightarrow\quad
\|L(u)-L(v)\|<1.
\tag{24}
\]

For `x\ne y`, put

\[
t=\frac{\delta}{2\|x-y\|}>0.
\tag{25}
\]

Then `\|tx-ty\|=\delta/2`, and positive homogeneity yields

\[
t\|L(x)-L(y)\|
=
\|L(tx)-L(ty)\|
<1.
\tag{26}
\]

Hence

\[
\|L(x)-L(y)\|
<
\frac{2}{\delta}\|x-y\|,
\tag{27}
\]

so `L` is globally Lipschitz. This isolates why the homogeneous metric section in AF-081 cannot be globally uniformly continuous when the sequence does not split.

### The uncomplemented uniformly convex control separates continuity from global stability

For `1<p<\infty`, `p\ne2`, AF-081 uses Lindenstrauss--Tzafriri to choose an uncomplemented closed `K\subset\ell^p`. AF-078 therefore gives

\[
\lambda_{\mathrm{lin}}(q)=+\infty.
\tag{28}
\]

The quotient `\ell^p/K` is separable, so (4) gives

\[
\lambda_{\mathrm{Lip}}(q)=+\infty.
\tag{29}
\]

At the same time uniform convexity gives a unique continuous norm-minimal homogeneous section `s_K`. Equations (28)--(29) prove that this section sits strictly between two regularity categories:

\[
\boxed{
\text{continuous homogeneous section exists}
\quad\not\Rightarrow\quad
\text{globally Lipschitz section exists}.
}
\tag{30}
\]

Because positive-homogeneous global uniform continuity would imply Lipschitz continuity, the same example also separates continuity from global uniform continuity.

## Exact controls

### Split control

If `K` is complemented, AF-078 supplies a bounded linear section `V`. It is automatically globally Lipschitz, so the converse implication in (5) requires no nonlinear theory. The new content is that separability forbids obtaining a globally Lipschitz section when this linear gate fails.

### Hilbert control

If `E` is Hilbert and `K` is closed, orthogonal projection identifies the quotient isometrically with `K^\perp`. The minimum-norm section is linear and `1`-Lipschitz, so all gates in (13) coincide. This is the rigid endpoint against which the nonlinear uniformly convex example should be compared.

### Nonseparable boundary

Separability is not cosmetic. Godefroy--Kalton prove that the corresponding lifting theory changes in the nonseparable setting; their Section 4 constructs nonseparable Lipschitz phenomena that do not linearize and proves that nonseparable weakly compactly generated spaces fail the lifting property. Therefore (4)--(7) must not be promoted to arbitrary quotient targets.

### Uniform continuity without homogeneity is a different category

Global or bounded-domain uniform continuity must not be silently identified with Lipschitz stability. Godefroy--Kalton explicitly note after Corollary 3.4 that the global statement fails without positive homogeneity, and Kalton's later uniform-structure work develops quotient sections that are uniformly continuous on the unit ball in settings where linear splitting need not follow. The homogeneity hypothesis in (7) is therefore load-bearing.

### Local and bounded-scale regularity remain separate questions

The theorem controls one **global** regularity category. It does not say that a non-splitting continuous section cannot have useful moduli on restricted subsets, compacta, finite-dimensional slices, or other declared bounded regimes. Such claims require their own scale-sensitive audit. In particular, AF-082 does not convert failure of a global Lipschitz constant into arbitrary local instability.

## Prior art and novelty assessment

The central linearization theorem is classical.

- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141. DOI `10.4064/sm159-1-6`. Corollary 3.2 proves that a quotient map onto a separable Banach space with a Lipschitz right inverse has a linear right inverse with the same norm; Corollary 3.4 gives the positive-homogeneous uniformly continuous consequence. Their Section 4 shows that separability is a genuine boundary. Publisher source: Institute of Mathematics of the Polish Academy of Sciences.
- Nigel J. Kalton, **“Spaces of Lipschitz and Hölder functions and their applications,”** *Collectanea Mathematica* 55(2) (2004), 171--217. DOI `10.1344/CM.V55I2.4055`. Section 10 studies uniformly continuous sections of quotient maps on unit balls and shows that uniform/bounded-scale lifting belongs to a broader nonlinear category than global Lipschitz splitting.
- Robert G. Bartle and Lawrence M. Graves, **“Mappings between function spaces,”** *Transactions of the American Mathematical Society* 72 (1952), 400--413. DOI `10.1090/S0002-9947-1952-0047910-X`. As already recorded in AF-081, the Bartle--Graves selection theorem supplies continuous nonlinear sections for arbitrary Banach quotients, providing the lower-regularity positive control.

No novelty is claimed for Lipschitz-free spaces, the Godefroy--Kalton lifting theorem, Bartle--Graves selection, or the uniform-lifting literature. The Arithmetic Fidelity contribution is the exact **regularity-gate synthesis** with AF-078 and AF-081: linear splitting and global Lipschitz selection have identical existence and optimal-cost thresholds for separable quotients, while the canonical metric repair can cross that threshold only by losing global uniform/Lipschitz stability. Equation (11) additionally isolates a useful failure mode for later compression audits: exact norm preservation from a base point is much weaker than stable pairwise recovery.

## Boundaries and failure modes

- The source Godefroy--Kalton theorem is stated for real Banach spaces. The complex infimum identity in (4) is a derived realification/symmetrization consequence, not a separately cited theorem.
- Equation (4) concerns the best cost among **all** right inverses. It does not say that an arbitrary nonlinear Lipschitz section must itself be linear.
- Complementability guarantees some linear/Lipschitz section, but it does not force AF-081's minimum-norm section to be Lipschitz. The metric selector and the cheapest arbitrary selector are different optimization problems.
- A `1`-Lipschitz minimum-norm section is rigid by (13), but a nonlinear minimum-norm section with a larger finite Lipschitz constant is not ruled out when the quotient already splits.
- Global uniform continuity implies Lipschitz continuity here only because positive homogeneity is present. Do not delete that hypothesis.
- Uniform continuity on a bounded set is not covered by the scaling argument in (24)--(27) and can survive without linear splitting.
- Nonseparable targets lie outside the Godefroy--Kalton Corollary 3.2 hypothesis and can exhibit genuinely different nonlinear lifting behavior.
- A right inverse selects one representative from each quotient class. Full recovery of an arbitrary source `x` still requires the lost kernel coordinate; given a normalized section `L(0)=0`, the associated coordinate `x-L(qx)\in K` reconstructs `x`, but canonicity of that coordinate is a separate structural question.

## Consequences for Arithmetic Fidelity

AF-078 identified splitting as the exact existence gate for **linear** quotient repair and separated that from canonicity. AF-079 and AF-080 then showed how equivariance and order alter the admissible splitting/selection problem. AF-081 demonstrated that richer norm geometry can select a canonical continuous nonlinear representative even when linear splitting is impossible.

AF-082 closes the next stability question in the separable regime. The AF-081 escape is not a stable Lipschitz replacement for splitting: if global Lipschitz control is demanded, Godefroy--Kalton forces the problem back into the linear category with exactly the same optimal section cost. In the uncomplemented uniformly convex control, the canonical metric section is therefore a genuine example of **perfect radial norm fidelity without global pairwise fidelity**.

For later Mathia compressions, the reusable audit is now finer than “can the lost data be recovered?” One must state the admissible carrier category and the required stability scale separately. A nonlinear recovery that exists continuously may be mathematically valid yet unusable for a downstream spectral, perturbative, trace, positivity, or quantitative argument if that argument silently needs uniform or Lipschitz control. Conversely, failure of the global Lipschitz gate does not authorize claiming total information destruction when a weaker but still intrinsic continuous carrier survives.