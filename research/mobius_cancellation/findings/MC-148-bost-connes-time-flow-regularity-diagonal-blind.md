# MC-148 — Canonical Bost–Connes time-flow regularity is diagonal-blind

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Work in the same canonical number-state representation as `MC-138`–`MC-147`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
H\varepsilon_n=(\log n)\varepsilon_n,
\qquad
U_t=e^{itH},
\tag{1}
\]

with the Bost–Connes time evolution implemented by

\[
\alpha_t(T)=U_tTU_t^*.
\tag{2}
\]

On the represented generators this is the standard dynamics

\[
\alpha_t(\pi(e(r)))=\pi(e(r)),
\qquad
\alpha_t(\pi(\mu_m))=m^{it}\pi(\mu_m).
\tag{3}
\]

`MC-147` proved that the strong/weak operator closure of the represented coefficient algebra is

\[
\mathcal C''=\mathcal D\cong\ell^\infty(\mathbb N),
\tag{4}
\]

where `\mathcal D` is the algebra of **all** bounded diagonal operators. The canonical time evolution does not reduce this target-complete class. In fact

\[
\boxed{
B(\ell^2(\mathbb N))^{\alpha}
:=\{T:\alpha_t(T)=T\ \forall t\}
=\mathcal D
=\mathcal C''.
}
\tag{5}
\]

Thus the zero-energy/fixed-point sector of the canonical implemented dynamics is already exactly the target-complete diagonal algebra from `MC-147`.

For every bounded arithmetic sequence `a=(a_n)` let

\[
D_a\varepsilon_n=a_n\varepsilon_n.
\tag{6}
\]

Then `D_a` strongly commutes with `H`, so

\[
\alpha_t(D_a)=D_a
\qquad(t\in\mathbb R).
\tag{7}
\]

Consequently every bounded arithmetic diagonal — the Möbius diagonal

\[
M_\mu\varepsilon_n=\mu(n)\varepsilon_n
\tag{8}
\]

included — has the same maximal regularity with respect to the canonical time flow:

\[
\delta(D_a)=0,
\qquad
\delta^k(D_a)=0\quad(k\ge1),
\tag{9}
\]

for the generator derivation `\delta`, and the orbit `z\mapsto\alpha_z(D_a)` extends to the constant entire function `D_a`.

Therefore a residual escape left by `MC-147` is closed sharply: **regularity imposed only through the canonical Bost–Connes Hamiltonian/time evolution cannot make the von Neumann diagonal completion Möbius-selective.** Membership in the fixed-point algebra, finite or vanishing commutator with `H`, smoothness under the time flow, analyticity under the time flow, or upper bounds built only from iterated time-generator seminorms all admit every bounded diagonal target.

The same blindness appears in the normal low-temperature Gibbs representation. For `\beta>1`, the canonical density

\[
\rho_\beta
=\zeta(\beta)^{-1}e^{-\beta H}
=\zeta(\beta)^{-1}\operatorname{diag}(n^{-\beta})
\tag{10}
\]

defines a faithful normal Gibbs state on `B(\mathcal H)`. Its modular fixed-point algebra/centralizer is again

\[
\boxed{
B(\mathcal H)_{\phi_\beta}
=\{T:[T,\rho_\beta]=0\}
=\mathcal D,
}
\tag{11}
\]

because the eigenvalues `n^{-\beta}` are distinct. Hence modular stationarity in this canonical Gibbs realization also accepts every bounded arithmetic diagonal; it does not distinguish Möbius from an arbitrary bounded lookup table.

This does **not** rule out regularity transverse to the Hamiltonian. For example, commutators with the semigroup isometries satisfy

\[
[D_a,\pi(\mu_m)]\varepsilon_k
=(a_{mk}-a_k)\varepsilon_{mk},
\tag{12}
\]

and therefore probe multiplicative scale variation that the time flow cannot see. A surviving Bost–Connes regularity route must introduce such additional source-forced structure, or another restriction not reducible to the canonical energy orbit, and must still prove a non-tautological transfer to Mertens excursion.

## 1. The fixed-point algebra of the canonical Hamiltonian is exactly diagonal

For `T\in B(\mathcal H)`, write

\[
T_{mn}=\langle\varepsilon_m,T\varepsilon_n\rangle.
\tag{13}
\]

Since

\[
U_t\varepsilon_n=n^{it}\varepsilon_n,
\tag{14}
\]

the matrix coefficients of the implemented flow are

\[
\langle\varepsilon_m,\alpha_t(T)\varepsilon_n\rangle
=\left(\frac{m}{n}\right)^{it}T_{mn}.
\tag{15}
\]

If `T` is fixed by `\alpha_t` for every real `t`, then

\[
\left(\left(\frac{m}{n}\right)^{it}-1\right)T_{mn}=0
\qquad(t\in\mathbb R).
\tag{16}
\]

For `m\ne n`, `\log(m/n)\ne0`, so there exists `t` for which the scalar in parentheses is nonzero. Hence

\[
T_{mn}=0\qquad(m\ne n).
\tag{17}
\]

Thus every fixed operator is diagonal. Conversely every bounded diagonal commutes with every `U_t`, so it is fixed. This proves `(5)`.

The proof uses only the simple spectrum

\[
\operatorname{spec}_{\mathrm{point}}(H)=\{\log n:n\ge1\};
\tag{18}
\]

no zeta continuation, KMS classification, prime-distribution theorem, or Möbius estimate enters. The zero-energy sector of `B(\mathcal H)` is diagonal because the Hamiltonian separates number states, but that diagonal sector contains no arithmetic selectivity beyond the values one chooses to place on those states.

Combining `(5)` with `MC-147` gives the exact identity

\[
\boxed{
\mathcal C''=B(\mathcal H)^\alpha=\mathcal D.
}
\tag{19}
\]

So the coefficient von Neumann closure is not merely contained in the zero-energy sector: in this representation it **fills it completely**.

## 2. Every bounded diagonal is infinitely time-smooth and entire analytic

Let `a\in\ell^\infty(\mathbb N)`. The diagonal operator `D_a` preserves the domain of the unbounded Hamiltonian. Indeed, for `\xi=(\xi_n)\in\operatorname{Dom}(H)`,

\[
\sum_n(\log n)^2|a_n\xi_n|^2
\le
\|a\|_\infty^2
\sum_n(\log n)^2|\xi_n|^2
<\infty.
\tag{20}
\]

On this domain,

\[
HD_a\xi=D_aH\xi.
\tag{21}
\]

Equivalently, `D_a` commutes with every spectral projection of `H`, hence strongly commutes with `H` and with `U_t`. Equation `(7)` follows.

Let `\delta` denote the generator of the implemented automorphism group on the elements where the norm derivative exists. A fixed point has constant orbit, so

\[
D_a\in\operatorname{Dom}(\delta^k),
\qquad
\delta^k(D_a)=0
\qquad(k\ge1).
\tag{22}
\]

The same constant-orbit observation gives an entire analytic extension:

\[
\alpha_z(D_a):=D_a
\qquad(z\in\mathbb C).
\tag{23}
\]

Thus common energy-regularity tests collapse completely on the arithmetic diagonal. For example, a Lipschitz seminorm of the form

\[
L_H(T)=\|[H,T]\|
\tag{24}
\]

assigns

\[
L_H(D_a)=0
\tag{25}
\]

whenever it is interpreted on this strongly commuting diagonal class. Likewise, every seminorm based only on finitely or countably many `\|\delta^k(T)\|` vanishes on every `D_a` for `k\ge1`.

The obstruction is therefore stronger than saying that Möbius happens to be smooth. **Time-flow smoothness has no resolving power at all inside the target-complete diagonal sector.** Any admissibility criterion whose only nontrivial requirements are continuity, differentiability, analyticity, or upper derivative bounds for the canonical energy orbit leaves all bounded arithmetic sequences admissible.

## 3. The canonical Gibbs modular centralizer has the same degeneracy

For `\beta>1`, equation `(10)` is trace class and strictly positive, so

\[
\phi_\beta^{\mathrm G}(T)
=\operatorname{Tr}(\rho_\beta T)
\tag{26}
\]

defines a faithful normal state on `B(\mathcal H)`. Its modular automorphism group is

\[
\sigma_s^{\phi_\beta^{\mathrm G}}(T)
=\rho_\beta^{is}T\rho_\beta^{-is}.
\tag{27}
\]

The scalar normalization in `\rho_\beta` cancels from conjugation, while

\[
\rho_\beta^{is}
=\zeta(\beta)^{-is}e^{-i\beta sH}.
\tag{28}
\]

Therefore

\[
\sigma_s^{\phi_\beta^{\mathrm G}}(T)
=\alpha_{-\beta s}(T).
\tag{29}
\]

The modular fixed points are consequently the same fixed points as `(5)`. Equivalently, for a density-matrix state the centralizer consists of operators commuting with the density, and the diagonal entries `n^{-\beta}` are pairwise distinct. Hence `(11)` follows.

This gives a precise limit to a possible refinement of the `MC-147` residual. Requiring a bounded arithmetic target to lie in the canonical normal Gibbs centralizer is not more selective than requiring it to be diagonal: every `D_a`, including `M_\mu`, is already there.

The statement is deliberately restricted to this normal `\beta>1` Gibbs realization on `B(\mathcal H)`. It is **not** a claim about the centralizers of all Bost–Connes KMS factors in every temperature regime or representation.

## 4. Relation to `MC-139` and `MC-147`

`MC-139` established an exact KMS selection rule: nonzero time-evolution degree is annihilated in every positive-temperature KMS expectation, and distinct prime energy degrees cannot compensate one another. Its residual was therefore a genuinely degree-zero arithmetic carrier.

`MC-147` then showed that weakening the coefficient topology from norm closure to unrestricted strong/weak closure makes the diagonal information class universal: `\mathcal C''=\ell^\infty(\mathbb N)`. It explicitly left source-natural energy/modular regularity among the restrictions that might conceivably recover selectivity.

The present finding intersects those two boundaries. In the canonical number-state representation,

\[
\boxed{
\text{degree zero under the canonical implemented flow}
=\text{all bounded diagonals}
=\text{target-complete coefficient von Neumann closure}.
}
\tag{30}
\]

Hence **canonical energy degree and canonical energy smoothness are not the missing restriction.** Passing to the zero-energy sector avoids the KMS annihilation of `MC-139`, but after von Neumann completion that sector is still large enough to encode every bounded arithmetic target.

This also identifies what a nontrivial regularity proposal would have to change. The Hamiltonian measures only the number-state energy `\log n`; diagonal multiplication does not move energy and is therefore invisible to its commutator. In contrast, the semigroup isometries move `k` to `mk`, and `(12)` measures an exact multiplicative finite difference of the diagonal sequence. Regularity involving those transverse directions is not classified by the present no-go and cannot be replaced by a bound on `[H,D_a]`.

No favorable conclusion for Möbius follows from this observation. A semigroup-commutator condition could still be universal, too strong, equivalent to reconstructing `\mu`, or unrelated to anchored additive order. It survives only as a mathematically distinct first-kill surface.

## 5. Prior art and novelty audit

The source dynamics and operator-algebraic ingredients are established.

- Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), 411–457, DOI `10.1007/BF01589495`, define the Bost–Connes arithmetic `C^*`-dynamical system and its time evolution. The standard generator formulas `\sigma_t(\mu_m)=m^{it}\mu_m` and invariance of the cyclotomic coefficient generators were already audited for this line in `MC-139`.
- Marcelo Laca and Iain Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, gives the semigroup-crossed-product and representation-theoretic framework used throughout the current Bost–Connes sequence.
- The concrete Hamiltonian `H\varepsilon_n=(\log n)\varepsilon_n` implementing the canonical number-state dynamics is standard in presentations of the Bost–Connes system; it is the Hamiltonian whose partition function is `\zeta(\beta)`.
- The facts that the fixed points of an inner flow `\operatorname{Ad}(e^{itH})` are the commutant of the spectral resolution of `H`, that fixed points are entire analytic for the flow, and that the centralizer of a faithful density-matrix state is the commutant of its density are standard operator/modular theory.

A targeted literature search for the Bost–Connes time evolution, canonical Hamiltonian, fixed-point language, KMS spectral subspaces, and modular/centralizer structures found the standard dynamics and equilibrium framework, together with broader spectral-triple and modular constructions. No inference of novelty is made from whether the exact identity `(19)` or the line-specific no-go above appears verbatim in those sources.

Accordingly **no novelty is claimed** for the time evolution, fixed-point computation, smoothness statement, or Gibbs centralizer. The durable Mathia delta is the classification of one explicit residual from `MC-147`: adding only canonical time/energy regularity to the target-complete diagonal weak closure does not restore arithmetic selectivity.

## Boundaries and falsification tests

- **Representation-specific.** Equations `(5)`, `(19)`, and `(30)` use the canonical number-state representation. Another representation may have spectral multiplicities or a different implemented von Neumann flow and requires a separate audit.
- **Energy-only regularity.** The no-go applies to restrictions defined solely through the canonical Hamiltonian/time orbit or its generator on the diagonal weak closure. A different Dirac operator, spectral triple, derivation, correspondence, or noncommuting geometric structure is not covered merely because it is also called spectral regularity.
- **The universal algebra is not being identified with `B(\mathcal H)`.** `MC-147` and the present result concern the represented von Neumann closure. They do not assert that arbitrary bounded diagonal lookup tables belong to the original Bost–Connes `C^*`-algebra.
- **The Gibbs-centralizer statement is low-temperature and normal.** Equation `(11)` concerns the canonical `\beta>1` density-matrix state on `B(\mathcal H)`. Type-III KMS representations and other phases are not classified by it.
- **Transverse semigroup regularity survives.** Equation `(12)` is generally nonzero and is not controlled by `(9)`. Any proposed no-go extending this finding to semigroup commutators must prove an additional theorem.
- **Small energy seminorm does not imply cancellation.** Here the stronger statement `L_H(D_a)=0` holds for every bounded diagonal, including deliberately non-cancelling comparators; no Mertens estimate can be inferred from it.
- **Analyticity is not arithmetic analyticity.** Entire analyticity of the operator orbit `z\mapsto\alpha_z(D_a)` is a dynamical regularity statement and must not be confused with analytic continuation of a Dirichlet series attached to `a`.
- **No RH consequence is asserted.** The finding removes a representation-level route and proves no new bound for `M(x)`.

A proposed energy-regularized weak-completion mechanism is decisively non-informative if its only discriminator is fixed-point membership, `H`-commutation, time-orbit smoothness/analyticity, iterated canonical time derivatives, or membership in the canonical normal Gibbs centralizer. To survive, it must add a mathematically source-forced restriction that excludes generic bounded diagonals and then prove a cheaper quantitative transfer to the anchored Mertens statistic.

## Consequence for the line

The Bost–Connes weak-completion frontier is now narrower than after `MC-147`. The unrestricted von Neumann closure was already target-complete; the most immediate source-natural regularity repair — use the system's own Hamiltonian/time evolution — does not reduce that diagonal target class at all. Its fixed-point algebra is exactly `\ell^\infty(\mathbb N)`, every bounded arithmetic diagonal has zero canonical energy derivative to all orders, and the canonical normal Gibbs centralizer is the same algebra.

The remaining regularity question must therefore be **transverse to canonical energy**. Semigroup commutators such as `(12)`, a genuinely additional spectral/geometric operator, a controlled state/source class, or another non-energy complexity constraint remain logically open only if they first defeat matched arbitrary-diagonal controls. Even then they must bridge multiplicative structure to the additive prefix order in `M(x)` without reconstructing the target at comparable cost.

Canonical time-flow regularity alone is now closed as a Möbius-selective escape from the target-completeness result of `MC-147`.