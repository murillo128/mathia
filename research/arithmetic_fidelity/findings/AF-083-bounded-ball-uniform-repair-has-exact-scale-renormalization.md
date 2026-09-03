# AF-083 — Bounded-ball uniform quotient repair has exact scale renormalization

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` be a real Banach space, let `K\subseteq E` be a closed linear subspace, and let

\[
q:E\longrightarrow F=E/K
\tag{1}
\]

be the normalized quotient map. A **bounded-ball uniform repair** means a right inverse on the quotient unit ball

\[
\phi:B_F\to E,
\qquad
q\phi(y)=y,
\tag{2}
\]

that is uniformly continuous on `B_F`.

Kalton's uniform-lifting theory and the exact scaling forced by homogeneity give the following classification.

1. **A bounded-ball uniform section can be homogenized without leaving the bounded-scale category.** If (2) exists, one may replace it by a positive-homogeneous section on `B_F` and extend it to a positive-homogeneous right inverse

   \[
   L:F\to E,
   \qquad
   qL=I_F,
   \qquad
   L(ty)=tL(y)\quad(t\ge0),
   \tag{3}
   \]

   that is uniformly continuous on every bounded ball. Thus the ball problem is not merely a local germ problem: after homogeneous normalization it supplies one coherent section at all finite radii, but with a modulus that may deteriorate with radius.

2. **The deterioration is governed by an exact renormalization law.** For `R>0`, define

   \[
   \omega_R(t)
   =
   \sup\{\|L(x)-L(y)\|:
   \|x\|,\|y\|\le R,\ \|x-y\|\le t\},
   \qquad 0\le t\le2R.
   \tag{4}
   \]

   Then positive homogeneity gives exactly

   \[
   \boxed{
   \omega_R(t)=R\,\omega_1(t/R).
   }
   \tag{5}
   \]

   Hence bounded-scale fidelity is completely controlled by the unit-ball modulus together with the dilation action. There is no independent modulus to choose at each scale.

3. **Scale-invariant Lipschitz control collapses back to linear splitting.** For a positive-homogeneous section `L`, the following are equivalent:

   \[
   \boxed{
   \begin{array}{c}
   L|_{B_F}\text{ is Lipschitz with constant }C;\\
   L\text{ is globally Lipschitz with the same constant }C;\\
   \sup_{0<t\le2}\omega_1(t)/t\le C.
   \end{array}}
   \tag{6}
   \]

   The implication from the ball to the whole space is forced by homogeneity: scale any pair into one common ball. Therefore, if `F` is separable, AF-082 and Godefroy--Kalton imply

   \[
   \boxed{
   \text{bounded-ball Lipschitz repair}
   \Longleftrightarrow
   \text{global Lipschitz repair}
   \Longleftrightarrow
   \text{bounded linear splitting}.}
   \tag{7}
   \]

   A genuinely nonlinear escape from splitting can therefore occur in the bounded-ball **uniform** category only through a non-Lipschitz modulus.

4. **That nonlinear bounded-scale category is strictly larger than linear/global-Lipschitz repair.** Kalton proves that if the discarded kernel `K` is super-reflexive, then the quotient map (1) admits a uniformly continuous section on `B_F`.

   Choose `1<p<\infty`, `p\ne2`, and a closed uncomplemented subspace

   \[
   K\subset\ell^p.
   \tag{8}
   \]

   Such a `K` exists by the Lindenstrauss--Tzafriri complemented-subspace theorem used in AF-081. Since `\ell^p` is super-reflexive and super-reflexivity passes to closed subspaces, `K` is super-reflexive. Kalton's theorem therefore gives a bounded-ball uniformly continuous section

   \[
   B_{\ell^p/K}\to\ell^p.
   \tag{9}
   \]

   But `K` is uncomplemented, so AF-078 and AF-082 give no bounded linear section and no global Lipschitz section. Thus

   \[
   \boxed{
   \text{bounded-ball uniform repair}
   \not\Rightarrow
   \text{linear/global-Lipschitz repair},}
   \tag{10}
   \]

   even for a separable uniformly convex source and separable quotient.

5. **Every nonsplitting bounded-ball repair must lose scale-invariant first-order control.** Let `L` be a positive-homogeneous extension as in (3) for a quotient with no global Lipschitz section. Then

   \[
   \boxed{
   \limsup_{t\downarrow0}\frac{\omega_1(t)}{t}=+\infty.}
   \tag{11}
   \]

   Indeed uniform continuity on the path-connected unit ball makes `L(B_F)` bounded. If `\omega_1(t)/t` were bounded for all sufficiently small `t`, boundedness would control the remaining larger scales and make `L|_{B_F}` Lipschitz; (6) would then make `L` globally Lipschitz, contradiction.

   More generally, if a particular section satisfies a Hölder estimate

   \[
   \omega_1(t)\le C t^\alpha,
   \qquad 0<\alpha<1,
   \tag{12}
   \]

   then (5) forces

   \[
   \boxed{
   \omega_R(t)\le C R^{1-\alpha}t^\alpha.}
   \tag{13}
   \]

   The factor `R^{1-\alpha}` is the exact scale price of that sub-Lipschitz modulus. Equation (13) is conditional on the declared Hölder control; it is not a claim that Kalton's sections always have a Hölder modulus.

6. **Bounded-ball uniform repair can split the uniform topology without splitting the Banach extension.** Kalton's Proposition 7.2 shows that existence of a uniformly continuous quotient section on the ball yields a uniform homeomorphism

   \[
   \boxed{
   B_E\ \simeq_{\mathrm{unif}}\ B_K\times B_F.}
   \tag{14}
   \]

   Applied to the uncomplemented `\ell^p` control above, the unit ball has a uniform product decomposition while the exact sequence does not split linearly. Thus topological/uniform decomposition of bounded state space and linear decomposition of the ambient source are genuinely different fidelity categories.

7. **Bounded-ball uniform repair is still a real existence gate, not an automatic consequence of quotient structure.** Kalton's Theorem 7.6 proves that if the source is an `\mathcal L_1`-space or an `\mathcal L_\infty`-space, every quotient map onto `\ell^2` fails to admit a uniformly continuous lift on `B_{\ell^2}`. Hence

   \[
   \boxed{
   \text{continuous nonlinear selection}
   \not\Rightarrow
   \text{bounded-ball uniformly continuous selection}.}
   \tag{15}
   \]

   Bartle--Graves continuity therefore lies strictly below the bounded-scale uniform category, just as bounded-scale uniformity lies strictly below scale-invariant Lipschitz control in (10).

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{quotient repair has a genuine scale axis in addition to algebraic category and canonicity;}\\
\text{bounded-ball uniform recovery may exist beyond every linear/global-Lipschitz split;}\\
\text{after homogeneous normalization its entire scale behavior is }\omega_R(t)=R\omega_1(t/R);\\
\text{the nonlinear escape is therefore paid for by a non-Lipschitz small-scale modulus.}
\end{array}}
\tag{16}
\]

## Derivation

### Homogeneous normalization turns one ball section into a coherent bounded-scale section

Kalton starts with a quotient map `q:E\to F` admitting a uniformly continuous section `\phi:B_F\to E`. On the unit sphere one may replace `\phi` by the odd symmetrization

\[
\phi_0(y)
=
\frac12\bigl(\phi(y)-\phi(-y)\bigr),
\qquad \|y\|=1.
\tag{17}
\]

Because `q\phi(y)=y` and `q\phi(-y)=-y`, one still has

\[
q\phi_0(y)=y.
\tag{18}
\]

Extend radially on the ball and then to all of `F` by positive homogeneity. Kalton proves that this normalization can be performed while retaining uniform continuity on the ball, and that the resulting homogeneous extension is uniformly continuous on bounded sets. This is the precise literature bridge behind (3).

The normalization matters. Without homogeneity, moduli at different radii need not be linked by any exact law, and bounded-ball uniformity would remain only a statement about one chosen scale.

### Homogeneity gives the exact modulus renormalization

Fix `R>0`. Every pair `x,y` in the radius-`R` ball can be written uniquely as

\[
x=Ru,
\qquad
y=Rv,
\qquad
\|u\|,\|v\|\le1.
\tag{19}
\]

Moreover

\[
\|x-y\|\le t
\quad\Longleftrightarrow\quad
\|u-v\|\le t/R,
\tag{20}
\]

and positive homogeneity gives

\[
\|L(x)-L(y)\|
=R\|L(u)-L(v)\|.
\tag{21}
\]

Taking suprema over the corresponding pair sets proves both inequalities in (5), hence equality. In particular, uniform continuity of `L` on `B_F` immediately implies uniform continuity on every `RB_F`.

### A Lipschitz unit-ball modulus is already global

Assume

\[
\omega_1(t)\le Ct
\qquad(0\le t\le2).
\tag{22}
\]

For arbitrary `x,y\in F`, choose

\[
R=\max\{\|x\|,\|y\|\}>0.
\tag{23}
\]

Then (5) yields

\[
\|L(x)-L(y)\|
\le
\omega_R(\|x-y\|)
=R\omega_1(\|x-y\|/R)
\le C\|x-y\|.
\tag{24}
\]

So `L` is globally `C`-Lipschitz. The converse is immediate by restriction. This proves (6). For separable `F`, AF-082 then invokes Godefroy--Kalton to turn a global Lipschitz section into a bounded linear right inverse with no larger cost, proving (7).

This also explains why positive-homogeneous **global** uniform continuity is not an intermediate category: AF-082 shows that it automatically upgrades to global Lipschitz continuity. The genuinely wider regime is uniform continuity on each bounded set with a modulus that is allowed to renormalize with scale.

### Super-reflexive kernels give a strict separation from splitting

Kalton's Theorem 10.1 states that if a closed subspace `K` of a Banach space `E` is super-reflexive, then the quotient map

\[
E\to E/K
\tag{25}
\]

admits a uniformly continuous section on the quotient unit ball.

For `1<p<\infty`, `\ell^p` is super-reflexive, and every closed subspace is therefore super-reflexive. For `p\ne2`, AF-081 uses the Lindenstrauss--Tzafriri theorem to choose an uncomplemented closed subspace `K\subset\ell^p`. Kalton gives (9), while uncomplementability excludes a bounded linear section by AF-078. Since the quotient is separable, AF-082 excludes every global Lipschitz section as well. This proves the strict implication (10) without relying on a merely hypothetical nonlinear example.

The result is category-sensitive in a second way: Theorem 10.1 is an existence theorem. It does not declare the resulting section unique or canonical. AF-081's metric projection may supply canonicity under stricter norm geometry, but bounded-ball uniformity by itself only says that some stable bounded-scale representative selection exists.

### Nonsplitting forces infinite small-scale slope

Let `L` be uniformly continuous on `B_F`, homogeneous, and normalized by `L(0)=0`. Choose `\delta>0` such that

\[
\|u-v\|<\delta
\quad\Longrightarrow\quad
\|L(u)-L(v)\|<1
\tag{26}
\]

for `u,v\in B_F`.

For any `x\in B_F`, divide the segment from `0` to `x` into `N` equal pieces with `1/N<\delta`. Summing the increments gives a bound

\[
\|L(x)\|\le N,
\tag{27}
\]

so `M=\sup_{B_F}\|L\|<\infty`.

Suppose instead of (11) that there are `C<\infty` and `\varepsilon>0` with

\[
\omega_1(t)\le Ct
\qquad(0<t\le\varepsilon).
\tag{28}
\]

For `\varepsilon\le t\le2`, boundedness gives

\[
\frac{\omega_1(t)}{t}
\le
\frac{2M}{\varepsilon}.
\tag{29}
\]

Together (28)--(29) make `\sup_{0<t\le2}\omega_1(t)/t` finite. By (6), `L` would be globally Lipschitz. Therefore every bounded-ball uniform repair of a nonsplitting separable quotient has unbounded first-order slope arbitrarily close to zero, proving (11).

Equation (13) follows directly from (5):

\[
\omega_R(t)
=R\omega_1(t/R)
\le
RC(t/R)^\alpha
=CR^{1-\alpha}t^\alpha.
\tag{30}
\]

### Uniform product decomposition does not imply linear decomposition

Kalton's Proposition 7.2 associates to a bounded-ball uniformly continuous section a uniform homeomorphism between the source unit ball and the product of the kernel and quotient unit balls. The construction uses the selected representative together with the residual kernel coordinate. Therefore (14) is a genuine reconstruction statement at the bounded uniform level.

The uncomplemented `\ell^p` example proves that (14) does not imply a bounded linear complement of `K`. What survives is the uniform type of the bounded state space, not an additive linear splitting of `E`.

## Exact controls

### Linear/Hilbert control: no scale deterioration

If `E` is Hilbert and `K` is closed, the orthogonal representative section is linear and `1`-Lipschitz. Its modulus is

\[
\omega_R(t)=t
\tag{31}
\]

for every admissible `R,t`. Equation (5) is exact but produces no radius dependence. This is the rigid scale-invariant endpoint.

### Nonlinear nonsplitting control: bounded-scale uniformity survives

For an uncomplemented `K\subset\ell^p`, `1<p<\infty`, `p\ne2`, Kalton guarantees a uniformly continuous quotient section on the ball. After homogeneous normalization, the section is uniformly continuous on every bounded ball but cannot be globally Lipschitz. Consequently its unit-ball modulus must satisfy (11).

This is the decisive matched control showing that bounded-scale stability is not merely a weak restatement of linear splitting.

### Existence failure: `\mathcal L_1/\mathcal L_\infty` sources onto `\ell^2`

Kalton's Theorem 7.6 gives the opposite control: for an `\mathcal L_1`-space or `\mathcal L_\infty`-space source, a quotient onto `\ell^2` has no uniformly continuous lift on the quotient unit ball. Continuous nonlinear selections still exist by general selection theory, so the failure is specifically a uniform bounded-scale obstruction.

### Conditional Hölder control: scale cost is forced

If a chosen homogeneous section has `\omega_1(t)\le Ct^\alpha`, then the radius dependence in (13) is not an artifact of a proof estimate: it follows exactly from the equality (5). For `\alpha<1`, any attempt to compare the same absolute perturbation at larger and larger radii must pay the factor `R^{1-\alpha}`.

## Prior art and novelty assessment

The nonlinear lifting mechanisms are classical.

- Nigel J. Kalton, **“Spaces of Lipschitz and Hölder Functions and Their Applications,”** *Collectanea Mathematica* 55(2) (2004), 171--217, DOI `10.1344/CM.V55I2.4055`. Proposition 7.1 supplies an exact nonlinear section with prescribed modulus in the free-space model. The discussion preceding Proposition 7.2 shows how a uniformly continuous quotient section on the ball may be homogenized and extended to a section uniformly continuous on bounded sets. Proposition 7.2 gives the uniform product decomposition of unit balls. Theorem 7.6 gives the `\mathcal L_1/\mathcal L_\infty\to\ell^2` no-lift control. Theorem 10.1 proves the super-reflexive-kernel existence theorem used in (10).
- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141, DOI `10.4064/sm159-1-6`. Their separable quotient linearization theorem is the classical source behind AF-082 and the collapse (7) from global Lipschitz repair to bounded linear splitting.
- AF-078, AF-081, and AF-082 supply the already-persisted Mathia boundaries used here: linear repair equals complementability, uniformly convex metric repair can exist beyond complementability, and separable global Lipschitz repair collapses back to linear splitting.

No novelty is claimed for uniformly continuous sections on balls, Kalton's super-reflexive lifting theorem, the uniform product decomposition, the `\mathcal L_1/\mathcal L_\infty` obstruction, or Godefroy--Kalton linearization. The modulus identity (5) is an elementary consequence of positive homogeneity and is not claimed as an external novelty.

The durable Arithmetic Fidelity contribution is the **scale-relative classification** obtained by putting these classical facts behind AF-078--AF-082. It identifies bounded-ball uniformity as a genuine intermediate repair category, proves that a homogeneous repair carries an exact dilation law, and localizes the price of escaping linear splitting: the unit-ball modulus must have unbounded Lipschitz slope at arbitrarily small scales.

## Boundaries and failure modes

- The result is stated for real Banach spaces because Kalton's 2004 paper works in the real category. Complex variants require a separate check of the homogenization/lifting statements rather than silent scalar transfer.
- Super-reflexivity of the kernel is a sufficient condition for bounded-ball uniform lifting, not a necessary characterization.
- Existence of a bounded-ball uniform section does not imply uniqueness, naturality, equivariance, or canonicity. A section chosen using external data is not automatically an intrinsic repair.
- The exact renormalization law (5) applies after positive-homogeneous normalization. An arbitrary nonhomogeneous ball section need not carry the same scale law before normalization.
- Uniform homeomorphism (14) is a bounded-uniform statement, not a linear, bi-Lipschitz, isometric, or affine product decomposition.
- The strict separation (10) uses a separable quotient so that AF-082/Godefroy--Kalton excludes global Lipschitz escape. Nonseparable Lipschitz lifting has different behavior.
- Equation (11) concerns the modulus of a homogeneous nonsplitting section. It does not say that every local directional derivative is unbounded, nor that instability occurs along every pair family.
- Equation (13) is conditional on a Hölder modulus and should not be read as a universal quantitative estimate for all bounded-ball uniform sections.
- The theorem concerns full representative selection for a quotient. A particular discriminator may require far less information than reconstruction of an entire quotient representative.
- No arithmetic or prime-specific conclusion follows from this Banach-space classification alone.

## Consequences for Arithmetic Fidelity

AF-078--AF-082 separated linear existence, symmetry/order canonicity, continuous metric selection, and global Lipschitz stability. AF-083 inserts a previously missing **scale-sensitive** category between continuity and global Lipschitz control.

For homogeneous repairs, the unit-ball modulus is now the complete bounded-scale stability datum through (5). This gives a concrete next audit surface: classify which structural hypotheses force particular modulus classes, which modulus classes remain stable under composition of compressions, and when a proposed relational lift has a scale-invariant bound rather than a radius-dependent one.

The main warning for later arithmetic applications is precise. A representation may preserve a discriminator on every bounded region while still have no uniform global transport law. Before interpreting such a lift as surviving an asymptotic or infinite-scale compression, one must audit how its modulus renormalizes with the scale actually used by the downstream construction.