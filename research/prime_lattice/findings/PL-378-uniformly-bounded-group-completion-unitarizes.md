# PL-378 — Uniformly bounded group-like nonnormal prime representations are unitarizable

**Evidence:** `LITERATURE+EXACT-DERIVED + DIXMIER-DAY + DECISIVE-NARROWING`.

**Parent finding:** `PL-377`.

**Related findings:** `PL-003`, `PL-011`, `PL-023`, `PL-374`, `PL-376`, `PL-377`.

**Status:** `NONNORMALITY-ALONE-IS-NOT-AN-ESCAPE-FROM-PL-377-ONCE-THE-PRIME-SEMIGROUP-EXTENDS-TO-A-UNIFORMLY-BOUNDED-REPRESENTATION-OF-THE-FULL-RATIONAL-GROUP: BY-DIXMIER-DAY-THE-WHOLE-FAMILY-IS-SIMULTANEOUSLY-SIMILAR-TO-COMMUTING-UNITARIES, HENCE-TO-A-SPECTRAL-MEASURE-OF-SCALAR-PRIME-TORUS-CHARACTERS. A-GENUINE-NONNORMAL-MECHANISM-MUST-USE-ONE-SIDED-NONINVERTIBILITY, INVERSE-NORM-GROWTH, UNBOUNDED/DOMAIN-SENSITIVE-STRUCTURE, CONTROLLED-NONMULTIPLICATIVITY, OR-A-NON-SIMILARITY-INVARIANT-ARITHMETIC-METRIC`.

## Claim

Let `H` be a complex Hilbert space and let

\[
\rho:\mathbb N_{>0}\longrightarrow B(H),
\qquad
\rho(1)=I,
\qquad
\rho(mn)=\rho(m)\rho(n).
\tag{PL378-1}
\]

Assume every `rho(n)` is invertible. Exact complete multiplicativity then extends `rho` uniquely to the group completion

\[
G=\mathbb Q_{>0}^{\times}
\simeq
\bigoplus_{p\ \mathrm{prime}}\mathbb Z
\tag{PL378-2}
\]

by

\[
\pi(a/b)=\rho(a)\rho(b)^{-1}.
\tag{PL378-3}
\]

Assume, crucially, uniform boundedness on the **whole group**:

\[
M:=\sup_{q\in\mathbb Q_{>0}^{\times}}\|\pi(q)\|<\infty.
\tag{PL378-4}
\]

Then `G` is abelian, hence amenable, and the classical Day--Dixmier theorem applies: there exists a bounded invertible operator `S` such that

\[
U(q)=S\pi(q)S^{-1}
\tag{PL378-5}
\]

is unitary for every `q in G`. Moreover one may choose `S` with a quantitative equivalence of metrics controlled by `M`; the invariant-mean proof below gives

\[
\|S\|\,\|S^{-1}\|\le M^2.
\tag{PL378-6}
\]

Thus an exactly multiplicative prime representation may be highly nonnormal in the original Hilbert norm and nevertheless carry no irreducible nonnormal operator geometry: under (PL378-4), **all prime generators are simultaneously a single bounded similarity away from commuting unitaries**.

Since

\[
\widehat G\simeq \prod_p\mathbb T,
\tag{PL378-7}
\]

the spectral theorem for the commuting unitary family gives a projection-valued measure `E` on the infinite prime torus such that, for

\[
q=\prod_p p^{k_p},\qquad k_p\in\mathbb Z
\]

with finite support,

\[
U(q)
=
\int_{\mathbb T^{\mathcal P}}
\prod_p z_p^{k_p}\,dE(z).
\tag{PL378-8}
\]

In particular, for positive integers,

\[
\boxed{
\rho(n)
=
S^{-1}
\left(
\int_{\mathbb T^{\mathcal P}}
\prod_p z_p^{v_p(n)}\,dE(z)
\right)
S.
}
\tag{PL378-9}
\]

Every matrix coefficient is therefore a Fourier--Stieltjes mixture of the same scalar prime-torus characters already present in the Bohr/Helson representation:

\[
\langle \rho(n)\xi,\eta\rangle
=
\int_{\mathbb T^{\mathcal P}}
\prod_p z_p^{v_p(n)}\,d\mu_{\xi,\eta}(z),
\tag{PL378-10}
\]

where

\[
d\mu_{\xi,\eta}(z)
=
\langle dE(z)S\xi,S^{-*}\eta\rangle.
\]

The operator-valued exponent lattice has therefore collapsed, up to one global bounded change of Hilbert metric, to scalar characters of the **full group lattice** `Z^(P)`.

## 1. The collapse is an elementary amenability argument, not an RH input

Because the uniform bound (PL378-4) includes inverses, for every `q in G` and `x in H`,

\[
M^{-1}\|x\|
\le
\|\pi(q)x\|
\le
M\|x\|.
\tag{PL378-11}
\]

Indeed,

\[
\|x\|
=
\|\pi(q^{-1})\pi(q)x\|
\le
M\|\pi(q)x\|.
\]

Since `G` is abelian, it admits an invariant mean `m` on bounded functions on `G`. Define a new sesquilinear form by

\[
[x,y]_m
=
m_q\,\langle \pi(q)x,\pi(q)y\rangle.
\tag{PL378-12}
\]

Positivity of the mean and (PL378-11) give

\[
M^{-2}\|x\|^2
\le
[x,x]_m
\le
M^2\|x\|^2,
\tag{PL378-13}
\]

so this is an equivalent Hilbert inner product. Translation invariance of the mean gives

\[
[\pi(r)x,\pi(r)y]_m=[x,y]_m
\qquad(r\in G),
\tag{PL378-14}
\]

hence the whole representation is unitary in that equivalent metric.

Writing

\[
[x,y]_m=\langle Bx,y\rangle
\]

for a positive bounded invertible `B`, equation (PL378-13) yields

\[
M^{-2}I\le B\le M^2I.
\]

Taking `S=B^{1/2}` proves (PL378-5)--(PL378-6). This is precisely the classical Day--Dixmier unitarization mechanism specialized to the free abelian rational-prime group.

No analytic continuation, zeta zero, or special property of rational primes is used. The result applies equally to any countable free abelian group. Its value for `prime_lattice` is therefore eliminative: a purported RH mechanism cannot attribute arithmetic rigidity merely to bounded nonnormal prime generators if those generators satisfy the group-like hypotheses above.

## 2. Group completion turns the exponent cone into the standard infinite torus

The positive-integer exponent vectors form the cone

\[
\mathbb N_0^{(\mathcal P)}.
\]

Adjoining inverses replaces this by the full lattice

\[
\mathbb Z^{(\mathcal P)},
\]

and Pontryagin duality sends that full lattice to

\[
\mathbb T^{\mathcal P}.
\]

Thus the Day--Dixmier similarity does not land in some new spectral object. It lands exactly in the ambient prime torus already underlying Bohr lifts, vertical limit characters, and the Kronecker phases of this research line.

At a spectral point `z=(z_p)_p`, the integer `n` is read only through

\[
z^{v(n)}
=
\prod_p z_p^{v_p(n)}.
\tag{PL378-15}
\]

The special vertical phase

\[
z_p=e^{-it\log p}
\]

is one scalar character trajectory inside this same character space. Day--Dixmier itself supplies no distinguished `log p` flow, no continuation across `Re(s)=1`, no functional equation, and no condition selecting `Re(s)=1/2`. Any such structure must be additional global input.

This is the exact analogue of the conclusion of `PL-377`, but the hypotheses trade places. `PL-377` assumes **normality** and obtains spectral scalarization without requiring inverses or uniform group bounds. `PL-378` drops normality entirely, but requires the representation to be **group-like and uniformly bounded in both positive and negative prime directions**. Under that replacement, nonnormality is removable by one bounded similarity.

## 3. What is and is not erased by the similarity

For every `q in G`, similarity preserves the ordinary spectrum:

\[
\sigma(\pi(q))=\sigma(U(q))\subseteq\mathbb T.
\tag{PL378-16}
\]

It also preserves eigenvalue equations, algebraic relations, invertibility, and any construction that is genuinely functorial under bounded similarity. Consequently these data cannot extract more from the original nonnormal family than from the corresponding commuting unitary family.

However, the theorem does **not** say that the original operators are normal in the original inner product. Quantities such as numerical range, pseudospectrum, singular values, operator norms, and condition numbers are not similarity invariants. They can retain nontrivial information about `S`.

That distinction is important rather than a loophole to ignore. If an RH proposal uses such metric-sensitive nonnormal data, it must justify why the original Hilbert norm is arithmetically canonical and why replacing it by the equivalent invariant norm is forbidden. Otherwise the apparent nonnormal geometry can be manufactured by choosing an arbitrary bounded positive metric `B` and conjugating an ordinary torus representation. In that situation the extra geometry belongs to the chosen metric, not to the prime lattice.

Therefore `PL-378` does not rule out all nonnormal mechanisms; it rules out **nonnormality that disappears under a uniformly controlled global change of Hilbert metric**.

## 4. The full-group uniform bound is load-bearing

It would be incorrect to replace (PL378-4) by the one-sided condition

\[
\sup_{n\ge1}\|\rho(n)\|<\infty.
\tag{PL378-17}
\]

Even invertibility of every positive-semigroup operator does not repair that gap. The scalar representation

\[
\rho_\alpha(n)=n^{-\alpha}I,
\qquad \alpha>0,
\tag{PL378-18}
\]

satisfies `sup_n ||rho_alpha(n)||=1` and every `rho_alpha(n)` is invertible, but its rational-group extension obeys

\[
\|\pi_\alpha(1/n)\|=n^\alpha,
\]

so it is not uniformly bounded on `G` and cannot be similar to a unitary representation.

Still more importantly, the canonical one-sided shifts appearing throughout the Nyman/Hardy side of this line are typically **noninvertible isometries**. They do not extend to a uniformly bounded representation of the rational group on the same Hilbert space. Day--Dixmier therefore does not collapse the one-sided semigroup geometry isolated in `PL-017`--`PL-020`.

The surviving boundary is consequently sharp enough to guide further work:

- **one-sided noninvertibility** can carry genuine shift/model-space information;
- **inverse-norm growth** can obstruct unitarization even when every prime operator is invertible;
- **unbounded/domain-sensitive representations** are outside the bounded theorem;
- **controlled failure of exact multiplicativity** is outside the group representation setting;
- **metric-sensitive observables** remain possible only if the arithmetic problem supplies a canonical Hilbert metric not removable by similarity.

This is a materially narrower version of the generic `nonnormality` escape left by `PL-377`.

## 5. Prior-art and adversarial audit

The unitarization theorem is classical and no novelty is claimed for it.

- Mahlon M. Day, “Means for the Bounded Functions and Ergodicity of the Bounded Representations of Semi-Groups,” *Transactions of the American Mathematical Society* **69**(2) (1950), 276--291, DOI `10.2307/1990358`: https://doi.org/10.2307/1990358.
- Jacques Dixmier, “Les moyennes invariantes dans les semi-groupes et leurs applications,” *Acta Scientiarum Mathematicarum (Szeged)* **12A** (1950), 213--227: https://acta.bibl.u-szeged.hu/13605/.
- Michael Brannan and Sang-Gyun Youn, “On the similarity problem for locally compact quantum groups,” *Journal of Functional Analysis* **276**(4) (2019), 1313--1337, DOI `10.1016/j.jfa.2018.07.017`, states the classical Day--Dixmier theorem in its modern similarity form before studying quantum analogues: https://doi.org/10.1016/j.jfa.2018.07.017.

The targeted literature audit found the expected broad prior art on unitarizable amenable groups and the Dixmier problem, not an arithmetic theorem attaching new RH content to this specialization. That is exactly how this finding should be classified: **a classical representation-theoretic theorem applied as a decisive boundary test on the current prime-lattice operator search**, not a new operator theorem.

The adversarial checks are also essential to the interpretation:

1. Uniform boundedness only on `N` is insufficient; (PL378-18) is an explicit counterexample to that overstatement.
2. Similarity does not preserve metric-sensitive nonnormal observables, so the result cannot dismiss every pseudospectral or norm-geometric construction.
3. The theorem uses the group completion and therefore says nothing by itself about noninvertible prime shifts or unilateral Hardy/Nyman geometry.
4. The torus spectral representation is valid because the unitarized family is commuting and unitary; it is not being inferred from mere commutativity of arbitrary nonnormal operators.
5. Nothing here continues an Euler product or Dirichlet series past its honest convergence domain. The result concerns only the operator representation of the exponent lattice.

A repository prior-art check found no existing `prime_lattice` finding making this Day--Dixmier specialization. `PL-377` is the closest internal result: it scalarizes bounded **normal** representations. The present finding closes the complementary **nonnormal but uniformly bounded group-like** subclass.

## Consequence for `prime_lattice`

After `PL-377`, “nonnormality” remained one of the broad escape routes from scalar prime-character mixtures. `PL-378` shows that this label is too coarse.

If the positive prime semigroup has been upgraded to invertible operators in such a way that the full rational group is uniformly bounded, then its nonnormality is only a bounded change of Hilbert metric. After that one global similarity, the representation is an ordinary commuting-unitary spectral measure on the prime torus, and its matrix coefficients are scalar Fourier--Stieltjes mixtures of exponent-lattice characters.

Hence a genuinely new RH-relevant nonnormal mechanism must fail at least one load-bearing hypothesis above. The most credible surviving branches are now the intrinsically one-sided semigroup case, inverse-norm or resolvent growth that prevents uniform group boundedness, genuinely unbounded/domain-sensitive structure, or a canonically arithmetic metric-sensitive observable whose meaning is not invariant under Day--Dixmier renorming. Simply choosing bounded nonnormal prime operators and retaining exact complete multiplicativity is not enough once the representation is uniformly group-like.