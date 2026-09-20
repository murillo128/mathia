# AF-458 — Rademacher type controls sparse-mixture fidelity through paired secants

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `QUANTITATIVE-FIDELITY`, `COMPLETED-SECANT`, `NO-NOVELTY-CLAIM`

## Claim

AF-457 proves the sharp Hilbert ceiling `M/sqrt(2k)` for the total-variation conditioning of bounded affine `k`-sparse mixture encodings. The same mechanism has a broader Banach-space form: the decay exponent is controlled by the Rademacher type of the target, and in a restricted source-law fiber it is already forced by one specific source-side structure — a complete paired sign cube of completable secants.

Let `A` be an alphabet with at least `2k` atoms, let `Y` be a Banach space of Rademacher type `p in [1,2]`, and use the expectation convention

\[
\mathbb E_\varepsilon
\left\|
\sum_{j=1}^n \varepsilon_j y_j
\right\|_Y
\le
T_p(Y)
\left(
\sum_{j=1}^n \|y_j\|_Y^p
\right)^{1/p}
\tag{1}
\]

for independent signs `epsilon_j in {+1,-1}`. Let

\[
\phi:A\to Y,
\qquad
\sup_{a\in A}\|\phi(a)\|_Y\le M,
\tag{2}
\]

and extend `phi` barycentrically,

\[
F_\phi(\mu)=\sum_{a\in A}\mu(a)\phi(a).
\tag{3}
\]

For probability laws supported on at most `k` atoms, retain the AF-456/AF-457 convention

\[
\|\mu-\nu\|_{TV}=\|\mu-\nu\|_1.
\tag{4}
\]

Then the unrestricted sparse-mixture lower modulus satisfies

\[
\boxed{
\kappa_k^{TV}(\phi)
\le
T_p(Y)\,M\,k^{1/p-1}.
}
\tag{5}
\]

Thus every target with nontrivial type `p>1` forces worst-case affine TV fidelity to decay at least as a negative power of mixture complexity. The `p=1` boundary is qualitatively different: `(5)` gives no decay, exactly as AF-456 requires for `ell^1`-type full-simplex fidelity.

More importantly for a constrained arithmetic source law, the full unrestricted simplex is not needed. Let `C` be any normalized completed-secant carrier in the sense of AF-452, with the source norm equal to `ell^1`/TV. Suppose there are `2k` distinct atoms

\[
a_1,b_1,\ldots,a_k,b_k
\tag{6}
\]

such that for every sign vector `epsilon in {+1,-1}^k`, the two disjoint uniform laws

\[
\alpha_\varepsilon
=
\frac1k\sum_{j=1}^k
\begin{cases}
\delta_{a_j},&\varepsilon_j=+1,\\
\delta_{b_j},&\varepsilon_j=-1,
\end{cases}
\qquad
\beta_\varepsilon
=
\frac1k\sum_{j=1}^k
\begin{cases}
\delta_{b_j},&\varepsilon_j=+1,\\
\delta_{a_j},&\varepsilon_j=-1
\end{cases}
\tag{7}
\]

have normalized difference

\[
\eta_\varepsilon
:=
\frac{\alpha_\varepsilon-\beta_\varepsilon}{2}
=
\frac1{2k}
\sum_{j=1}^k
\varepsilon_j(\delta_{a_j}-\delta_{b_j})
\in C.
\tag{8}
\]

Call such a family a **completable paired `k`-cube**. Then the restricted source-law lower gain obeys the same ceiling:

\[
\boxed{
\kappa_C(F_\phi)
\le
T_p(Y)\,M\,k^{1/p-1}.
}
\tag{9}
\]

This is the source-relative bridge missing from the unrestricted statement. A constrained source law does not need to contain every balanced `k`-mixture secant. It is enough that its completed secant carrier contain one full `k`-dimensional paired sign cube.

Finally, the exponent in `(5)` is optimal across Banach target categories. For the canonical one-hot map into `ell^p(A)`,

\[
\phi(a)=M e_a,
\tag{10}
\]

one has exactly

\[
\boxed{
\kappa_k^{TV}(\phi)
=
M(2k)^{1/p-1}.
}
\tag{11}
\]

Hence the universal `k^{1/p-1}` scale cannot be improved in order over all type-`p` targets. At `p=2`, AF-457 supplies the stronger Hilbert-specific sharp envelope `M/sqrt(2k)`; AF-458 is the category-wide exponent theorem rather than a replacement for that sharper endpoint result.

## Exact derivation

### Type controls a paired sign cube

Choose any `2k` distinct atoms and pair them as in `(6)`. Put

\[
d_j=\phi(a_j)-\phi(b_j).
\tag{12}
\]

The norm budget `(2)` gives

\[
\|d_j\|_Y\le2M.
\tag{13}
\]

For the normalized secant `(8)`, linearity gives

\[
\int\phi\,d\eta_\varepsilon
=
\frac1{2k}
\sum_{j=1}^k\varepsilon_j d_j.
\tag{14}
\]

Average `(14)` over all `2^k` sign vectors and apply the type inequality `(1)`:

\[
\begin{aligned}
\mathbb E_\varepsilon
\left\|
\int\phi\,d\eta_\varepsilon
\right\|_Y
&=
\frac1{2k}
\mathbb E_\varepsilon
\left\|
\sum_{j=1}^k\varepsilon_j d_j
\right\|_Y\\
&\le
\frac{T_p(Y)}{2k}
\left(
\sum_{j=1}^k\|d_j\|_Y^p
\right)^{1/p}\\
&\le
T_p(Y)M k^{1/p-1}.
\end{aligned}
\tag{15}
\]

Therefore at least one sign vector satisfies

\[
\left\|
\int\phi\,d\eta_\varepsilon
\right\|_Y
\le
T_p(Y)M k^{1/p-1}.
\tag{16}
\]

If all normalized paired secants `(8)` belong to a completed source-law carrier `C`, then `(16)` immediately proves `(9)` by the AF-452 identification of fixed-fiber conditioning with minimum gain on the normalized completed-secant carrier.

For the unrestricted `k`-sparse simplex, every pair `(alpha_epsilon,beta_epsilon)` in `(7)` is admissible. Since their supports are disjoint,

\[
\|\alpha_\varepsilon-\beta_\varepsilon\|_1=2,
\tag{17}
\]

and `(16)` is exactly the ratio bound `(5)`. Notice that the proof needs only `2k` distinct atoms for a fixed `k`; an infinite alphabet is needed only when the statement is to hold for arbitrarily large mixture complexity.

### `ell^p` one-hot marks attain the exponent

For `(10)`, write `h=mu-nu`. If `mu,nu` are each supported on at most `k` atoms, then

\[
|\operatorname{supp}h|\le2k.
\tag{18}
\]

Holder's inequality gives

\[
\|h\|_1
\le
(2k)^{1-1/p}\|h\|_p,
\tag{19}
\]

so

\[
\frac{
\|F_\phi(\mu)-F_\phi(\nu)\|_p
}{
\|\mu-\nu\|_1
}
=
M\frac{\|h\|_p}{\|h\|_1}
\ge
M(2k)^{1/p-1}.
\tag{20}
\]

Take two disjoint uniform `k`-point laws. Then `h` has exactly `2k` nonzero coordinates, all of magnitude `1/k`, and equality holds in `(19)`. This proves `(11)`.

For `1<=p<=2`, `ell^p` has Rademacher type `p`, so `(11)` shows that the exponent in `(5)` is genuinely the target-geometry scale and not an artifact of the proof. The constants need not coincide in the general type-`p` theorem. At `p=2`, AF-457 uses Hilbert weak geometry to improve `(5)` from `M/sqrt(k)` to the sharp `M/sqrt(2k)`.

## What this adds to AF-452 and AF-457

AF-452 says that quantitative fidelity on a fixed affine source-law fiber is exactly a minimum-gain problem over the normalized completed secants that the source law actually admits. AF-457 says bounded Hilbert geometry has a sharp square-root obstruction on unrestricted sparse mixtures, but explicitly leaves open whether a physical arithmetic source law contains enough of those bad directions.

AF-458 identifies one concrete sufficient source-side structure. The relevant richness is not merely "many secants" or "large support": a **paired sign cube** lets the Rademacher type of the target act directly on the source carrier. If such cubes exist with unbounded dimension `k`, every bounded affine target of nontrivial type `p>1` has vanishing TV lower gain along the corresponding source-law family.

Conversely, if a proposed arithmetic source law is stably represented in such a target, it must exclude these paired cubes at the scales where the claimed lower gain stays positive. That exclusion is not a technicality; it is now a precise source-law rigidity theorem that the arithmetic construction would have to supply.

This sharpens the current source-relative frontier into a two-sided test:

- **cube presence** transfers a classical type-`p` compression obstruction into the arithmetic fiber;
- **cube exclusion** is a necessary structural escape route for stable bounded affine encoding in any nontrivial-type target.

No claim is made that paired-cube exclusion is sufficient for arithmetic fidelity. Other secant geometries can still force collapse.

## Prior art and novelty audit

The Banach-space geometry in this finding is classical. **No novelty is claimed for Rademacher type, the discrete-cube mechanism, or the `k^{1/p-1}` rate.**

- Grigory Ivanov, **“No-dimension Tverberg's theorem and its corollaries in Banach spaces of type p,”** *Bulletin of the London Mathematical Society* 53(2), 631–641 (2021), DOI `10.1112/blms.12449`. Ivanov uses the same expectation convention for the type constant `T_p(X)` and proves dimension-free Radon/Tverberg/Caratheodory bounds with exponent `(1-p)/p = 1/p-1`. His no-dimension colorful Radon theorem is direct prior art for balanced-partition collapse at this scale; Maurey's lemma is the classical convex-approximation mechanism behind the surrounding theory.
- Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665–678 (2020), DOI `10.4007/annals.2020.192.2.8`. This establishes the equivalence between linear Rademacher type and its metric discrete-cube analogue, confirming that sign-cube geometry as a probe of Banach-space type is established structure rather than a new Arithmetic Fidelity principle.

The elementary calculation `(12)`--`(16)` is a direct specialization of Rademacher type to a paired difference family. The line-specific contribution is organizational: AF-452 supplies the completed-source-law secant carrier, and `(8)` identifies a finite combinatorial certificate inside that carrier whose presence is sufficient to import the classical type obstruction into a constrained arithmetic fiber.

## Boundary and falsification audit

- **The result is affine/barycentric.** A nonlinear encoder of the whole probability law is not constrained by `(5)` solely because its codomain has type `p`.
- **The target norm budget matters.** Rescaling `phi` rescales every lower modulus. The homogeneous parameter `M` cannot be omitted.
- **The type exponent is a ceiling, not a pairwise statement.** The theorem guarantees at least one low-gain sign orientation in a full paired cube; it does not say every sparse pair has this distortion.
- **A restricted source law need not contain a paired cube.** Equation `(9)` applies only after completion feasibility is proved for every sign orientation in one paired block. Assuming unrestricted prime mixtures would beg the main source-law question.
- **Paired-cube presence is sufficient, not necessary.** A carrier can have poor conditioning without containing this exact cube structure.
- **`p=1` is a genuine boundary.** Every Banach space has type `1`, but the resulting ceiling is constant. Canonical `ell^1` one-hot marking has exact gain `M` for every `k`, so no decay theorem can follow from type `1` alone.
- **Hilbert space has extra structure.** The general type-2 argument gives `M/sqrt(k)` when `T_2=1`; AF-457 improves this to the sharp `M/sqrt(2k)`. The loss of a factor `sqrt(2)` here is deliberate and prevents overstating the general type theorem.
- **Finite alphabets impose a complexity cutoff.** The argument at level `k` requires `2k` distinct atoms. No conclusion is drawn beyond that combinatorial supply.

## Arithmetic specialization

Take `A=P`, the rational primes. For unrestricted `k`-sparse probability laws on primes and any bounded affine prime mark into a Banach space of type `p>1`,

\[
\boxed{
\kappa_k^{TV}(\phi)
\le
T_p(Y)M k^{1/p-1}
\longrightarrow 0.
}
\tag{21}
\]

Thus the Hilbert square-root obstruction from AF-457 is one point on a broader target-geometry spectrum. Moving from Hilbert space to another reflexive/smooth Banach target does not by itself remove mixture collapse: any nontrivial Rademacher type still imposes a complexity-dependent loss, with exponent determined by the available type.

For an actual arithmetic source-law fiber, however, the decisive question is no longer the unrestricted inequality. By AF-452 and `(9)`, it is enough to determine whether the completed rational-prime secant carrier contains paired sign cubes of increasing dimension. If it does, bounded affine encodings into every nontrivial-type target lose uniform TV conditioning. If it does not, the arithmetic reason those cubes are excluded becomes a concrete rigidity mechanism worth isolating before any downstream spectral, positive, quotient, or asymptotic compression is attempted.

## Consequence for the line

The source-mixture frontier now has a target/source compatibility test rather than a Hilbert-only warning:

\[
\boxed{
\text{completed paired }k\text{-cube in the source}
+
\text{target of type }p
\Longrightarrow
\kappa\lesssim k^{1/p-1}.
}
\tag{22}
\]

The next arithmetic question is correspondingly sharper. Instead of asking generically whether the physical source law has "enough balanced secants," test whether its completed secant carrier admits paired sign cubes whose dimension grows with arithmetic complexity. A positive answer transfers the obstruction immediately; a negative answer identifies the exact combinatorial rigidity that a surviving arithmetic discriminator would have to exploit.