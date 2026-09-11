# MC-216 — Coherent square-modulus gauge removes cross-modulus selected-character phases

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-215` shows that for each individual square modulus `d^2`, the source-prescribed reduced residue

\[
a_d\equiv -q\pmod{d^2},
\qquad (d,q)=1,
\]

can be translated to the identity, so the visible character factors `\chi(a_d)` are a residue-label gauge rather than an arithmetic phase carrier. A possible escape remained: perhaps the gauges for different moduli are incompatible, so **relative phases across square moduli** could retain source information even though every single-modulus phase is removable.

For the actual square-defect family this escape is absent. The selected residues form a coherent point of the entire inverse system of square-modulus unit groups, and one coherent unit translation gauges them all to the identity simultaneously.

Let

\[
\mathcal D_q
:=
\{d\ge1:d\text{ square-free},\ (d,q)=1\},
\qquad
G_d=(\mathbb Z/d^2\mathbb Z)^\times.
\tag{1}
\]

Whenever `e|d`, let

\[
\pi_{d,e}:G_d\to G_e
\tag{2}
\]

be reduction modulo `e^2`. Then

\[
\boxed{
\pi_{d,e}(a_d)=a_e.
}
\tag{3}
\]

Hence `(a_d)_{d\in\mathcal D_q}` is a coherent element of

\[
\boxed{
G_q^{[2]}
:=
\varprojlim_{d\in\mathcal D_q}G_d
\cong
\prod_{p\nmid q}(\mathbb Z/p^2\mathbb Z)^\times.
}
\tag{4}
\]

Because every `a_d` is a unit, the coherent inverse `(a_d^{-1})_d` exists as well. Thus the translations

\[
(U_dF)(b):=F(a_db)
\tag{5}
\]

are not unrelated per-modulus normalizations: they are the finite projections of **one global translation** in the inverse-limit group.

This global gauge is compatible with the canonical cross-modulus operations. If the fiber-sum pushforward is

\[
(R_{d,e}F)(c)
:=
\sum_{\substack{b\in G_d\\\pi_{d,e}(b)=c}}F(b),
\tag{6}
\]

then exactly

\[
\boxed{
R_{d,e}U_d=U_eR_{d,e}.
}
\tag{7}
\]

The corresponding pullback `P_{e,d}f=f\circ\pi_{d,e}` satisfies

\[
\boxed{
U_dP_{e,d}=P_{e,d}U_e.
}
\tag{8}
\]

Therefore every diagram assembled only from the residue profiles, reductions, CRT identifications, canonical pushforwards/pullbacks, and translation-equivariant operators can be gauge-fixed **simultaneously at all square moduli**. Passing to several moduli does not by itself restore the arithmetic content removed in `MC-215`.

The character formulation is sharper. If `\chi_e` is a character of `G_e` and

\[
\chi_d:=\chi_e\circ\pi_{d,e},
\tag{9}
\]

then coherence `(3)` gives

\[
\boxed{
\chi_d(a_d)=\chi_e(a_e).
}
\tag{10}
\]

Thus even the apparent **relative phase across nested moduli is exactly trivial** for the same inflated character sector.

More generally, take finitely many square-free moduli `d_1,\ldots,d_r`, characters `\chi_j\in\widehat G_{d_j}`, and signs `\varepsilon_j\in\{+1,-1\}` indicating a Fourier coefficient or its complex conjugate. Put

\[
L=\operatorname{lcm}(d_1,\ldots,d_r)
\tag{11}
\]

and inflate every character to `G_L`. The total character charge is

\[
\Psi
:=
\prod_{j=1}^r
(\chi_j\circ\pi_{L,d_j})^{\varepsilon_j}.
\tag{12}
\]

Then the complete selected-residue phase of that mixed character monomial is

\[
\boxed{
\prod_{j=1}^r\chi_j(a_{d_j})^{\varepsilon_j}
=
\Psi(a_L).
}
\tag{13}
\]

Under an arbitrary coherent residue translation, the monomial transforms by the character `\Psi`. Consequently a translation-invariant mixed-character scalar can contain only the **neutral sector** `\Psi=1`; in that sector `(13)` is identically `1`. Any non-neutral phase combination that appears to use the values `\chi_j(-q)` is gauge-covariant rather than invariant.

This closes a specific loophole left by `MC-215`: **cross-modulus character-phase coherence generated solely by the compatible residue systems is still gauge.** The source label `-q` does not become informative merely because several `d^2` are coupled through reduction or CRT.

What survives is exactly the non-equivariant arithmetic structure already isolated by `MC-215`: the transformed coefficient profiles themselves, their gauge-invariant principal/transverse covariance, the finite interval cutoff, the integer representatives, and especially the lift

\[
n+q=d^2m.
\tag{14}
\]

Those data are not functions only of a point in the inverse system of unit groups. A viable next theorem must use such structure, or another operation that genuinely breaks the coherent unit-translation symmetry, rather than a network of explicit `\chi(-q)` factors.

No estimate for the covariance `I_D`, the raw energy `W_D`, `M(X)`, or any zeta zero-free region is proved here.

## 1. The prescribed residues form one inverse-limit point

For `e|d`, reduction modulo `e^2` sends the residue class of `-q` modulo `d^2` to the residue class of `-q` modulo `e^2`, proving `(3)`. Since `(d,q)=1`, this class lies in `G_d` for every active modulus.

For square-free `d`, the Chinese remainder theorem gives

\[
G_d
\cong
\prod_{p\mid d}(\mathbb Z/p^2\mathbb Z)^\times.
\tag{15}
\]

Taking the inverse limit over finite square-free products of primes not dividing `q` gives `(4)`. Under this identification the selected point is simply

\[
a=( -q\bmod p^2)_{p\nmid q}.
\tag{16}
\]

Every component is a unit, so `a^{-1}` exists componentwise. Multiplication by `a` is therefore one automorphism of the full product whose projection at level `d` is exactly the translation used in `MC-215`.

This matters because independent per-modulus gauge freedom would leave open the possibility that a cross-modulus construction compared the gauges themselves. Equation `(16)` shows that no inconsistency exists to compare: the gauges are already the projections of a single coherent unit.

## 2. Canonical bonding maps commute with the global gauge

To prove `(7)`, fix `c\in G_e`. Then

\[
(R_{d,e}U_dF)(c)
=
\sum_{\pi_{d,e}(b)=c}F(a_db).
\tag{17}
\]

Set `x=a_db`. By `(3)`,

\[
\pi_{d,e}(x)=a_ec.
\]

Multiplication by `a_d` is a bijection from the fiber over `c` to the fiber over `a_ec`, hence

\[
(R_{d,e}U_dF)(c)
=
(R_{d,e}F)(a_ec)
=(U_eR_{d,e}F)(c).
\tag{18}
\]

This proves `(7)`. Equation `(8)` is immediate:

\[
(U_dP_{e,d}f)(b)
=f(\pi_{d,e}(a_db))
=f(a_e\pi_{d,e}(b))
=(P_{e,d}U_ef)(b).
\tag{19}
\]

Normalized fiber averages obey the same identities. Compositions with translation-equivariant convolution or spectral multipliers also remain conjugate under the same global gauge. Thus changing from one modulus to a compatible family does not create a phase observable unless some additional operation breaks this naturality.

This is the square-modulus analogue of the sector-preserving transport mechanism already exposed for nested primorials in `MC-191`, but the point here is different: the **distinguished source section itself** is globally gauge-equivalent to the identity section.

## 3. Character inflation has no relative selected phase

For `(9)`, simply evaluate at the coherent selected point:

\[
\chi_d(a_d)
=\chi_e(\pi_{d,e}(a_d))
=\chi_e(a_e),
\]

proving `(10)`. Thus a cross-level product such as

\[
S_d(\chi_d)\overline{S_e(\chi_e)}
\tag{20}
\]

receives opposite copies of exactly the same selected phase under the simultaneous gauge normalization. The phase cancels before any arithmetic estimate enters.

For arbitrary finitely many moduli, every `d_j` divides `L`, and coherence gives

\[
\chi_j(a_{d_j})
=(\chi_j\circ\pi_{L,d_j})(a_L).
\tag{21}
\]

Multiplying `(21)` with the exponents `\varepsilon_j` proves `(13)`.

Now let a coherent unit `u=(u_d)_d\in G_q^{[2]}` act simultaneously at every level. The corresponding Fourier coefficient transforms by the usual character multiplier. Hence the mixed monomial transforms by

\[
\Psi(u_L).
\tag{22}
\]

If a scalar monomial is invariant under all coherent translations, `(22)` must equal `1` for all `u_L\in G_L`. Characters of the finite abelian group `G_L` separate points, so this is equivalent to

\[
\Psi=1.
\tag{23}
\]

For a general polynomial expression, decompose it into character-charge sectors; invariance keeps only the neutral sector. In that sector `(13)` gives

\[
\Psi(a_L)=1.
\tag{24}
\]

Therefore no translation-invariant cross-modulus polynomial can obtain nontrivial arithmetic information from the selected-character phases alone.

## 4. Consequence for the live square-defect frontier

The current raw-energy route needs negative principal/transverse interference,

\[
W_D=P_D+Z_D+2I_D,
\]

with

\[
I_D
=
\sum_d d\mu^2(d)
\operatorname{Re}\!\left(m_d\overline{E_{d,a_d}}\right).
\tag{25}
\]

`MC-215` already shows that `(25)` survives the single-level gauge. The present result says that summing or coupling several moduli through the canonical residue-system maps does not reveal an additional hidden phase of `a_d=-q`: all those selected points normalize coherently.

Accordingly, the next useful object must retain something that the inverse-limit residue system forgets. Examples include the actual integer lift `n+q=d^2m`, the dependence of admissible `m` on the finite endpoint `T`, ordering of integer representatives, a genuinely non-equivariant cross-modulus incidence relation, or a direct arithmetic estimate for the gauge-fixed covariance in `(25)`. Merely replacing one modulus by a network of nested/overlapping square moduli and tracking compatible Dirichlet-character phases is now a matched control rather than a new mechanism.

This does **not** show that every cross-modulus method is gauge-trivial. If the coupling uses data not functorial under unit-group translation — for example the lifted Diophantine relation `(14)` with its integer size constraints — the conjugacy argument above no longer applies. That boundary is deliberate: it identifies exactly where source-specific information must enter.

## 5. Prior-art and novelty audit

The inverse-limit mechanism is standard profinite-group theory. Luis Ribes and Pavel Zalesskii, *Profinite Groups*, 2nd ed., Springer (2010), DOI `10.1007/978-3-642-01642-4`, treats profinite groups as inverse limits of finite groups and provides the standard framework used in `(4)`. Finite/compact abelian character theory and the translation law for Fourier coefficients are standard harmonic analysis; `MC-215` already used that classical mechanism at one modulus.

No novelty is claimed for inverse limits, CRT, character inflation, translation covariance, or the neutral-character selection rule. `MC-191` is also an internal prior-art boundary: it proves that natural quotient-equivariant transport across nested primorial unit groups remains character-sector diagonal. The mathematical delta here is narrower and tied to the live `MC-213`--`MC-215` square-defect route: the family of source-selected residues `-q mod d^2` is itself a coherent inverse-limit point, so even **relative cross-modulus selected phases** can be removed by one simultaneous gauge.

A literature search found no need to posit a new theorem beyond these classical ingredients. The result should therefore be used only as an obstruction and candidate filter, not as a novelty claim.

## 6. Boundary and falsification conditions

The statement is at fixed primorial `q` (equivalently, fixed ambient square-defect problem). When the ambient scale changes and `q` itself changes, additional scale-transport information may enter; this finding does not identify those changing-`q` systems automatically.

The result assumes square-free root moduli only because the active raw-energy shell already carries `\mu^2(d)`. The coherence `-q mod d^2` itself does not depend on square-freeness, but no broader modulus family is needed for the claimed obstruction.

The no-go applies only to constructions whose cross-modulus operations are natural under the coherent unit translations described above. It does not apply to integer-size order, interval endpoints, lifted polynomial relations, or any other explicitly non-equivariant structure.

A counterexample to the exact claim would have to violate one of `(3)`, `(7)`, `(8)`, `(10)`, or `(13)` under the stated hypotheses. A counterexample to the research implication would exhibit a translation-invariant cross-modulus character construction whose dependence on the selected section survives the neutral-charge test `(23)`--`(24)`. In either case the failure mode is concrete and algebraic.