# MC-215 — Prescribed-residue character phase is gauge; lifted principal/transverse covariance survives

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-213` identifies the remaining square-defect escape as directed character coherence at the source-prescribed residue

\[
a_d\equiv -q\pmod{d^2},
\qquad
(d,q)=1,
\]

rather than an all-residue magnitude estimate. There is a further exact normalization which separates the genuinely source-sensitive content from a coordinate artifact.

Let

\[
G_d=(\mathbb Z/d^2\mathbb Z)^\times,
\qquad
\Phi_d=|G_d|=\varphi(d^2),
\]

and retain the residue profile from `MC-213`,

\[
A_{d,a}(T)
=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv a\pmod{d^2}}}\mu(n),
\]

with

\[
m_d=\frac{R_{qd}(T)}{\Phi_d},
\qquad
E_{d,a}=A_{d,a}(T)-m_d.
\]

Because `a_d` is a unit modulo `d^2`, define the translated profile

\[
\widetilde A_{d,b}:=A_{d,a_db}(T),
\qquad
\widetilde E_{d,b}:=E_{d,a_db},
\qquad b\in G_d.
\tag{1}
\]

Then multiplication by `a_d` is merely a permutation of `G_d`, so

\[
\widetilde A_{d,1}=A_{d,a_d},
\qquad
\widetilde E_{d,1}=E_{d,a_d},
\tag{2}
\]

while the principal mean, every all-residue `L^p` norm, every centered moment, and every permutation-invariant residue variance are unchanged.

For the character coefficients

\[
S_d(\chi)=\sum_{a\in G_d}A_{d,a}(T)\overline{\chi(a)},
\]

translation gives exactly

\[
\boxed{
\widetilde S_d(\chi)=\chi(a_d)S_d(\chi).
}
\tag{3}
\]

Hence the source-selected character reconstruction from `MC-213`,

\[
E_{d,a_d}
=
\frac1{\Phi_d}
\sum_{\chi\ne1}S_d(\chi)\chi(a_d),
\]

becomes after gauge fixing

\[
\boxed{
\widetilde E_{d,1}
=
\frac1{\Phi_d}
\sum_{\chi\ne1}\widetilde S_d(\chi).
}
\tag{4}
\]

At the same time

\[
|\widetilde S_d(\chi)|=|S_d(\chi)|
\tag{5}
\]

for every character. Therefore the explicit phase factors `\chi(-q)` are **not by themselves an arithmetic information carrier**. They are the Fourier representation of the arbitrary decision to label the distinguished residue as `a_d` rather than as the identity. Any proposed gain that uses `\chi(-q)` only as a phase multiplier while all other inputs are invariant under multiplication of residue labels can be normalized to `(4)` without changing the problem.

What survives the normalization is not trivial. The raw source coefficient remains

\[
A_{d,a_d}=m_d+\widetilde E_{d,1},
\tag{6}
\]

and the shell covariance of `MC-213` becomes

\[
\boxed{
I_D
=
\sum_d d\mu^2(d)
\operatorname{Re}\!\left(m_d\overline{\widetilde E_{d,1}}\right).
}
\tag{7}
\]

Thus the genuinely live quantity is the **principal/transverse covariance at the gauge-fixed distinguished coordinate**, or an equivalent relation retaining the integer lift `n+q=d^2m`, interval ordering, or another source structure not erased by residue relabeling. The bare character phase `\chi(-q)` is removable; the arithmetic dependence of the translated coefficients `\widetilde S_d(\chi)` on the original Möbius sample is not.

This sharpens the `MC-213` frontier. A viable interference theorem must prove something about the joint values of `m_d` and `\widetilde E_{d,1}` (or their cross-modulus/lifted analogues), not merely exploit the visible phase vector `(\chi(-q))_\chi`. In particular, all-residue BDH/large-sieve energies, centered moments, and the full character-magnitude spectrum remain matched controls: they are unchanged by `(1)` and therefore cannot certify source-specific phase information on their own.

No new estimate for `I_D`, `A_{d,a_d}`, `M(X)`, or a zeta zero-free region is proved here.

## 1. Translation is a unitary gauge on residue space

Fix `d` and abbreviate `G=G_d`, `a_0=a_d`. Define

\[
(U_{a_0}F)(b)=F(a_0b)
\]

for functions on `G`. Since multiplication by `a_0` is a bijection of `G`, `U_{a_0}` is a permutation matrix and hence unitary on `\ell^2(G)`. More generally, for every `1\le p<\infty`,

\[
\sum_{b\in G}|(U_{a_0}F)(b)|^p
=
\sum_{a\in G}|F(a)|^p.
\tag{8}
\]

It also fixes constants. Therefore subtracting the principal mean commutes with `U_{a_0}`:

\[
U_{a_0}(A-m_d)=U_{a_0}A-m_d.
\tag{9}
\]

This proves invariance of the centered variance `B_d` of `MC-213` and of every higher centered moment `B_{d,k}` of `MC-214`. Any shell energy obtained by summing such per-modulus invariant quantities is unchanged as well.

The same observation applies to a Barban--Davenport--Halberstam-type variance whenever all reduced residue classes are summed with equal weight: multiplication by a fixed unit only permutes the residue index. Thus a global residue variance can measure transverse size while remaining blind to which reduced residue was designated by the square-defect source.

## 2. Character phases transform covariantly

With the Fourier convention above,

\[
\widetilde S_d(\chi)
=
\sum_{b\in G}A_{d,a_0b}\overline{\chi(b)}.
\]

Substitute `a=a_0b`. Since `b=a_0^{-1}a` and Dirichlet characters are unitary on `G`,

\[
\overline{\chi(a_0^{-1}a)}
=
\chi(a_0)\overline{\chi(a)}.
\]

This gives `(3)`. Fourier inversion at the identity then gives `(4)`. Parseval is unchanged:

\[
\frac1{\Phi_d^2}\sum_{\chi\ne1}|\widetilde S_d(\chi)|^2
=
\frac1{\Phi_d^2}\sum_{\chi\ne1}|S_d(\chi)|^2
=B_d.
\tag{10}
\]

Consequently the direction vector `\chi\mapsto\chi(a_d)` appearing before gauge fixing is not invariant data. It can always be absorbed into the Fourier coefficients. What *is* invariant is the value of the profile at the distinguished point, equivalently the inner product between the translated nonprincipal coefficient vector and the all-ones evaluation vector.

This distinction matters for interpreting `MC-213`. Its sharp `d^2` point-evaluation leverage remains exactly valid; the normalization does not turn point evaluation into an all-residue norm. It only shows that the special-looking formula `a_d=-q` does not automatically provide a favorable character phase. Any favorable anti-alignment must already be encoded in the arithmetic values of the coefficient vector after this phase has been removed.

## 3. Principal/transverse interference is gauge invariant

Let

\[
P_D=\sum_d d\mu^2(d)|m_d|^2,
\qquad
Z_D=\sum_d d\mu^2(d)|E_{d,a_d}|^2,
\]

and let `W_D` and `I_D` be as in `MC-213`. Equations `(2)` and `(7)` imply that `P_D`, `Z_D`, `W_D`, and `I_D` are all unchanged by the gauge fixing. In particular,

\[
W_D=P_D+Z_D+2I_D
\tag{11}
\]

retains exactly the same signed interference information.

Therefore the normalization does **not** kill the live route. Instead it gives a falsification rule for how that route must be attacked:

- a theorem stated only in terms of all-residue norms or `|S_d(\chi)|` cannot see the required sign of `I_D`;
- a theorem whose only source-sensitive ingredient is the explicit factor `\chi(-q)` has not yet found invariant arithmetic structure, because `(3)` removes that factor;
- a theorem controlling the joint relation of `m_d` with the translated sum `\sum_{\chi\ne1}\widetilde S_d(\chi)`, or controlling the lifted solutions `n+q=d^2m`, survives the gauge test and remains potentially relevant.

The third category is the actual frontier. It may still admit source-specific structure because the translated profile is not a generic function on `G_d`: its coefficients come from the ordered finite interval of Möbius values and from the exact square-defect lift. The gauge argument does not compare that arithmetic profile with an arbitrary translated synthetic profile, and it does not supply any cancellation estimate.

## 4. Matched-control consequence

Let `\mathcal T_d` denote multiplication of residue labels by an arbitrary unit `u_d\in G_d`. Consider any statistic assembled from, for each modulus `d`, only:

- the principal mean `m_d`;
- all-residue centered `L^p` norms or moments;
- the multiset of nonprincipal magnitudes `\{|S_d(\chi)|\}`;
- equal-weight sums over all reduced residue classes.

Such a statistic is invariant under `\mathcal T_d` (up to permutation of character labels/phases that does not change the listed data). Therefore it cannot distinguish the pair `(A_d,a_d)` from the gauge-normalized pair `(U_{a_d}A_d,1)` on the basis of the residue label itself.

This gives a precise matched control for future candidates: before attributing a gain to the source phase `-q`, gauge the selected residue to `1`. If the proposed mechanism becomes an unchanged norm/moment statement with no residual dependence on the integer lift or on principal/transverse covariance, then the source label was decorative. If a nontrivial source-dependent relation remains, that residual relation is the object that must actually be estimated.

## 5. Prior-art and novelty audit

The transformation law `(3)` is standard finite-abelian-group Fourier analysis: translating a function multiplies each Fourier coefficient by the corresponding character phase. Dirichlet characters are precisely characters of the unit group modulo the modulus. No novelty is claimed for this harmonic-analysis mechanism.

Adam J. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences*, Journal of the London Mathematical Society 112 (2025), e70293, DOI `10.1112/jlms.70293`, studies the quadratic variance obtained by summing arithmetic-progression deviations over residue classes and moduli for general complex sequences. That established variance framework is consistent with the control used here: an equal-weight all-residue quadratic variance is unchanged by multiplying residue labels by a unit. Harper's theorem does not provide the distinguished-coordinate principal/transverse covariance `(7)`.

The mathematical delta of this finding is therefore only the application of the classical translation covariance to the exact `MC-213` square-defect representation. It removes a false source of optimism: `\chi(-q)` looks arithmetic but can be gauged away. The remaining unresolved source information is the translated coefficient profile's relation to its principal mode and to the integer lift `n+q=d^2m`.

## 6. Boundary and falsification conditions

This finding is intentionally narrow.

It does not say that all source-selected residue methods are equivalent to arbitrary-residue methods. The translated profile itself changes, and its arithmetic origin may retain decisive information. It does not say that cross-modulus constructions are gauge-trivial when they couple residue systems through additional non-equivariant data. It does not say that point evaluation is controlled by all-residue variance; `MC-213` and `MC-214` quantify the opposite.

The no-go applies when the candidate's claimed source sensitivity factors entirely through the removable residue label or through translation-invariant magnitude summaries. A counterexample to this finding would require one of the displayed translation identities to fail under the stated reduced-residue hypotheses. A counterexample to the broader research implication would instead exhibit an explicit invariant relation, surviving the gauge fixing, that uses the Möbius source and yields quantitative control of `(7)` cheaper than a Mertens-complete principal estimate.