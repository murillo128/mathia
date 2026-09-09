# MC-167 — The canonical Möbius σ-twist is a unitary copy of the phase-free Hamiltonian derivation

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Greenfield–Marcolli–Teh construct a type III `σ`-spectral triple for the supersymmetric Riemann-gas/Bost–Connes system on the square-free Hilbert space

\[
\mathcal H_F=\overline{\operatorname{span}}\{\varepsilon_n:n\text{ squarefree}\},
\]

with Möbius sign operator

\[
F\varepsilon_n=\mu(n)\varepsilon_n,
\qquad F^*=F,
\qquad F^2=I,
\]

Hamiltonian

\[
H\varepsilon_n=(\log n)\varepsilon_n,
\]

Dirac operator `D=FH`, and twisting automorphism

\[
\sigma(a)=FaF.
\tag{1}
\]

Because `F` commutes with `H`, the source's bounded twisted commutator has the exact normal form

\[
\boxed{
[D,a]_\sigma
:=Da-\sigma(a)D
=F[H,a]
}
\tag{2}
\]

on the common algebraic core, for every algebra element `a` for which the expressions are defined. Consequently

\[
\boxed{
[D,a]_\sigma^*[D,a]_\sigma
=[H,a]^*[H,a].
}
\tag{3}
\]

Thus the canonical Möbius twist does not create new singular-value information. Whenever the commutators are bounded,

\[
\|[D,a]_\sigma\|=\|[H,a]\|,
\tag{4}
\]

and compactness, all Schatten memberships, approximation numbers, and every quantity determined only by the singular values of the twisted commutator are exactly the same as for the **phase-free Hamiltonian derivation**.

For a square-free semigroup generator `\widetilde\mu_m`,

\[
[H,\widetilde\mu_m]
=(\log m)\widetilde\mu_m,
\]

so

\[
\boxed{
[D,\widetilde\mu_m]_\sigma
=(\log m)F\widetilde\mu_m,
\qquad
\|[D,\widetilde\mu_m]_\sigma\|=\log m.
}
\tag{5}
\]

The Möbius sign visible in matrix coefficients of `(5)` is therefore a left unitary factor; its absolute operator data are independent of that sign.

This collapse is not peculiar to the all-minus Möbius assignment. For any prime-sign assignment `z_p\in\{\pm1\}`, define on the same square-free Hilbert space

\[
f_z(n)=\prod_{p\mid n}z_p,
\qquad
F_z\varepsilon_n=f_z(n)\varepsilon_n,
\tag{6}
\]

and put

\[
D_z=F_zH,
\qquad
\sigma_z(a)=F_zaF_z.
\tag{7}
\]

The compressed Bost–Connes algebra is preserved by `\sigma_z`: coefficient operators commute with `F_z`, while on a square-free semigroup generator

\[
\sigma_z(\widetilde\mu_m)=f_z(m)\widetilde\mu_m.
\tag{8}
\]

The same calculation gives

\[
\boxed{
[D_z,a]_{\sigma_z}=F_z[H,a],
\qquad
\|[D_z,a]_{\sigma_z}\|=\|[H,a]\|
}
\tag{9}
\]

for every algebraic `a`. Hence the whole family of matched prime-sign controls has identical twisted-commutator singular-value data. The actual Möbius choice `z_p=-1` is not selected by boundedness or by any norm/ideal regularity of these canonical twisted commutators.

The construction still retains the Möbius orientation in **signed** data: equation `(2)` contains one explicit copy of `F`. The source's most direct signed spectral statistic makes that boundary transparent. Its eta function is

\[
\operatorname{Tr}_{\mathcal H_F}(F\,|\widetilde D|^{-\beta})
=\sum_{n\ge1}\frac{\mu(n)}{n^\beta}
=\frac1{\zeta(\beta)}
\tag{10}
\]

in the half-plane of convergence, with the corresponding meromorphic continuation discussed in the source. Thus the canonical construction exhibits a sharp dichotomy relevant to the Möbius line:

- absolute twisted-commutator regularity removes the Möbius orientation completely, reducing to `H`;
- the obvious orientation-sensitive trace retains the Möbius coefficients directly and gives the classical reciprocal-zeta Dirichlet series.

Neither branch supplies an intermediate cancellation theorem by itself. A surviving `σ`-spectral route would need an additional source-forced **signed or relational functional** whose estimate is strictly cheaper than estimating the Möbius sum or `1/ζ` itself.

## 1. Exact algebraic reduction of the twisted commutator

On `\mathcal H_F`, `F` is a self-adjoint unitary and `F` commutes strongly with `H`, since both are diagonal in the number-state basis. With `D=FH` and `\sigma(a)=FaF`, one has

\[
\begin{aligned}
Da-\sigma(a)D
&=FHa-(FaF)(FH)\\
&=FHa-FaH\\
&=F(Ha-aH)\\
&=F[H,a].
\end{aligned}
\tag{11}
\]

This identity explains the boundedness mechanism in Theorem 4.8 of Greenfield–Marcolli–Teh. The ordinary commutator with `D` can be unbounded because changing a number state also changes the Möbius sign multiplying its growing energy `\log n`. Twisting by `\sigma=\operatorname{Ad}F` cancels precisely that state-dependent sign mismatch, leaving only the ordinary energy increment measured by `[H,a]`.

Because left multiplication by `F` is unitary,

\[
(F[H,a])^*(F[H,a])
=[H,a]^*F^*F[H,a]
=[H,a]^*[H,a],
\tag{12}
\]

which proves `(3)` and all singular-value consequences. This is stronger than norm equality: any proposal based only on the absolute value `|[D,a]_\sigma|`, compactness, Schatten decay, or another unitarily invariant size of the twisted commutator is exactly phase-blind.

For coefficient elements `x\in C^*(\mathbb Q/\mathbb Z)`, `[H,x]=0`, so the twisted commutator vanishes. For the compressed semigroup shifts, the number-state energy changes by the constant `\log m`; hence `(5)` follows. This agrees with the source's basis formula

\[
(D\widetilde\mu_m-\sigma(\widetilde\mu_m)D)\varepsilon_\ell
=\mu(m)\mu(\ell)(\log m)\varepsilon_{m\ell}
\]

on the nonzero square-free/coprime sector.

## 2. Matched prime-sign controls have the same twisted regularity

The line-specific control family can be imposed without changing the square-free support. Choose arbitrary `z_p\in\{\pm1\}` and define `F_z` by `(6)`. Then `F_z` is again a self-adjoint unitary commuting with `H`.

Coefficient operators are diagonal, so they commute with `F_z`. If `m` and `\ell` are squarefree and coprime, then

\[
f_z(m\ell)=f_z(m)f_z(\ell),
\]

and therefore

\[
F_z\widetilde\mu_mF_z\varepsilon_\ell
=f_z(m)\widetilde\mu_m\varepsilon_\ell.
\tag{13}
\]

Thus conjugation by `F_z` preserves the same algebraic compressed Bost–Connes generators, giving `(8)`. Since `|D_z|=H`, the compact-resolvent and theta-summability properties are unchanged, while the twisted commutator again reduces exactly as in `(11)`.

The comparison includes the extreme control `z_p=+1` for all primes, for which `F_z=I` on the square-free space and the twist becomes trivial. It has exactly the same twisted-commutator norms as the Möbius choice `z_p=-1` for all primes. Therefore the critical arithmetic content cannot be inferred from those norms or regularity classes.

This control is intentionally restricted to real prime signs. Arbitrary unimodular phases would make `F_z` unitary but not self-adjoint, so `D_z=F_zH` would not in general be a self-adjoint Dirac operator of the same type.

## 3. Relation to the existing Bost–Connes boundary

`MC-148` showed that the canonical Hamiltonian time flow is blind on diagonal arithmetic targets: every bounded diagonal commutes with `H`. It explicitly left a different Dirac operator or twisted spectral triple outside scope. The present result addresses the canonical Möbius `σ`-spectral triple from the literature and finds that its bounded twisted derivation reduces back to that same Hamiltonian derivation after multiplication by one sign unitary.

`MC-149` then studied raw transverse commutators of a bounded arithmetic diagonal with semigroup shifts. For Möbius these raw commutators are maximally noncompact, and the stronger regularity classes reject the target. The `σ`-twist repairs the unbounded energy-weighted analogue, but equation `(11)` identifies the price of the repair: it cancels the state-dependent Möbius mismatch and leaves the universal energy shift.

`MC-165`–`MC-166` classified finite raw commutator words and finite coefficient-decorated variants into support-only and one-copy Möbius phase sectors. Equation `(2)` lands on the same conceptual boundary from a source-forced construction: the canonical twist leaves one explicit `F` factor multiplying a phase-free operator. The present finding does **not** claim that every possible modular twist or every nonlinear functional of the type III triple is covered by those finite-word results.

## 4. The eta function retains orientation by directly retaining the target coefficients

Greenfield–Marcolli–Teh also study `\widetilde D=F e^H`. On `\mathcal H_F`, `|\widetilde D|\varepsilon_n=n\varepsilon_n`, so their eta function is exactly `(10)`. They further define decorated eta functionals such as

\[
\varphi_\beta(e(r))
=\sum_{n\ge1}\mu(n)\frac{\zeta_r^n}{n^\beta},
\tag{14}
\]

which are Möbius-weighted additive twists at roots of unity.

Equation `(10)` is important prior art but not a new cancellation mechanism for this line: in its initial convergence half-plane it is exactly the classical Dirichlet series for `1/\zeta`, and using its continuation or zero set to obtain the desired Mertens exponent would require the same zero information the line forbids importing circularly.

The decorated functionals `(14)` are not ruled out here. They retain more than singular-value data and could in principle interact with arithmetic progressions or other structure. To matter for Möbius cancellation, however, a future argument must prove an estimate for such a functional from independent source information and then transfer it to an anchored Mertens bound with all inversion losses exposed.

## 5. Prior art and novelty audit

The primary source is Mark Greenfield, Matilde Marcolli and Kevin Teh, *Type III sigma-spectral triples and quantum statistical mechanical systems*, p-Adic Numbers, Ultrametric Analysis and Applications **6** (2014), 81–104, DOI `10.1134/S2070046614020010`, arXiv `1305.5492`.

Their Proposition 4.7 constructs the Möbius sign operators and records the zeta/eta functions, including `\eta_{\widetilde D}(\beta)=1/\zeta(\beta)`. Their Theorem 4.8 constructs the Riemann-gas type III `σ`-spectral triple with `D=FH` and `\sigma(a)=FaF`, and explicitly computes the bounded twisted commutator on semigroup generators. The source therefore already contains all structural ingredients used above.

The identity `[D,a]_\sigma=F[H,a]` is an immediate algebraic consequence of those definitions, and the singular-value equality follows immediately from `F^*F=I`. A targeted literature search recovered the source construction and its explicit generator formulas but did not provide a reason to treat this elementary rewriting as a new general theorem. **No novelty claim is made.** The durable line-specific contribution is the falsification statement: the canonical source-forced Möbius twist, when judged by boundedness or absolute twisted-commutator regularity, is exactly indistinguishable from matched prime-sign controls and from the phase-free Hamiltonian derivation.

## Boundaries and falsification tests

- **Square-free Riemann-gas representation.** The proof uses the source's `\mathcal H_F`, where `F^2=I`. On the full `\ell^2(\mathbb N)` Möbius multiplication has a kernel on squareful states and is not unitary, so `(3)` is not asserted there.
- **Absolute twisted-commutator data.** Equations `(3)`–`(4)` classify singular-value information. Signed matrix elements, products involving `F`, cyclic cocycles, eta functionals, or other orientation-retaining constructions are not automatically phase-blind.
- **Matched controls change the twist together with the sign operator.** Equation `(9)` shows that the canonical construction has no norm-level preference for the Möbius sign assignment when repeated across the natural sign family. It does not say that all those automorphisms are identical.
- **The eta function is target-complete, not useless.** Exact recovery of `1/\zeta` can be mathematically valuable. The obstruction is only that it cannot serve as an *independent* proof of Möbius cancellation without a new estimate not equivalent to the desired zero information.
- **Other twists remain open.** A twist not of the inner form `\operatorname{Ad}F_z`, a genuinely nonlinear orientation-sensitive functional, an infinite analytic completion, or a source-forced state/cocycle may escape `(2)` and requires its own derivation.
- **No RH consequence is claimed.** The result classifies one canonical prior-art escape and supplies a matched-control obstruction; it gives no improved bound for `M(x)`.

## Consequence for the research line

The most canonical literature-backed `σ`-spectral repair does not supply the missing intermediate cancellation category. Its success at boundedness is algebraically explained by removing the Möbius-dependent energy mismatch, after which every absolute regularity statistic is the ordinary Hamiltonian statistic. Keeping the sign instead leads immediately to the Möbius Dirichlet series or to other explicitly Möbius-weighted functionals.

Accordingly, further Bost–Connes work should not treat `σ`-spectral boundedness, twisted Lipschitz-size surrogates based solely on `\|[D,a]_\sigma\|`, compactness/Schatten regularity, or the unweighted eta function as latent evidence for a cheaper Mertens transfer. A viable continuation must identify a source-forced orientation-sensitive functional whose arithmetic estimate is independently available and whose inverse transfer does not reconstruct the target at the same exponent.