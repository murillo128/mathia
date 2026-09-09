# MC-168 — Bost–Connes twisted Lipschitz regularity is an exact local phase selector, not a cancellation statistic

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the square-free Riemann-gas/Bost–Connes `σ`-spectral triple audited in `MC-167`. On

\[
\mathcal H_F=\overline{\operatorname{span}}\{\varepsilon_n:n\text{ squarefree}\},
\]

let

\[
F\varepsilon_n=\mu(n)\varepsilon_n,
\qquad
H\varepsilon_n=(\log n)\varepsilon_n,
\qquad
D=FH,
\qquad
\sigma(a)=FaF.
\]

Because `F` is a self-adjoint unitary commuting with `H`, one has `|D|=H`. The Lipschitz-regularity test for the twisted triple is therefore

\[
[|D|,a]_\sigma
:=Ha-\sigma(a)H.
\tag{1}
\]

Greenfield–Marcolli–Teh already observe in Remark 4.9 that their Riemann-gas triple is not Lipschitz regular and give, for a square-free semigroup generator `\widetilde\mu_m`, the basis formula

\[
(H\widetilde\mu_m-\sigma(\widetilde\mu_m)H)\varepsilon_\ell
=
\bigl(\log m+(1-\mu(m))\log\ell\bigr)\varepsilon_{m\ell}
\tag{2}
\]

on the nonzero coprime square-free sector. Equation `(2)` gives an exact phase classification:

\[
\boxed{
[|D|,\widetilde\mu_m]_\sigma\text{ is bounded}
\iff \mu(m)=+1
}
\tag{3}
\]

for every nontrivial square-free `m`. In the bounded case,

\[
[|D|,\widetilde\mu_m]_\sigma
=(\log m)\widetilde\mu_m,
\qquad
\|[|D|,\widetilde\mu_m]_\sigma\|=\log m,
\tag{4}
\]

whereas for `\mu(m)=-1` the coefficient in `(2)` is `\log m+2\log\ell` and is unbounded along square-free `\ell` coprime to `m`.

The same dichotomy extends to the natural semigroup-ratio monomials

\[
V_{n,m}=\widetilde\mu_n\widetilde\mu_m^*,
\tag{5}
\]

with square-free `m,n`. Since

\[
\sigma(V_{n,m})=\mu(n)\mu(m)V_{n,m}
\tag{6}
\]

and, on the algebraic core,

\[
[H,V_{n,m}]=\log(n/m)V_{n,m},
\tag{7}
\]

one gets

\[
\boxed{
HV_{n,m}-\sigma(V_{n,m})H
=
\log(n/m)V_{n,m}
+
\bigl(1-\mu(n)\mu(m)\bigr)V_{n,m}H.
}
\tag{8}
\]

Consequently

\[
\boxed{
[|D|,V_{n,m}]_\sigma\text{ is bounded}
\iff \mu(n)\mu(m)=+1.
}
\tag{9}
\]

For the Möbius phase this is exactly the parity-preserving condition

\[
\omega(n)\equiv\omega(m)\pmod 2.
\tag{10}
\]

If the parities agree, `(8)` reduces to the bounded constant-energy shift `\log(n/m)V_{n,m}`. If they disagree, take square-free `k` coprime to `mn` and apply `(8)` to `\varepsilon_{mk}`; the coefficient has magnitude growing like `2\log k`, proving unboundedness.

Thus the canonical twisted Lipschitz test is genuinely **phase-sensitive**, unlike the singular-value data of the bounded twisted commutator in `MC-167`. But that sensitivity is only a direct local `\mathbb Z/2` selector: it reads whether the source and target semigroup labels carry the same Möbius parity. It does not aggregate cancellations among different integers and supplies no quantitative control of `M(x)` or of first-absolute Mertens excursion.

## 1. Matched prime-sign controls show exactly what the test remembers

Use the real prime-sign family from `MC-167`. For arbitrary `z_p\in\{\pm1\}`, set

\[
f_z(r)=\prod_{p\mid r}z_p,
\qquad
F_z\varepsilon_r=f_z(r)\varepsilon_r,
\qquad
D_z=F_zH,
\qquad
\sigma_z(a)=F_zaF_z.
\tag{11}
\]

For square-free `m`,

\[
\sigma_z(\widetilde\mu_m)=f_z(m)\widetilde\mu_m,
\]

so exactly the same calculation gives

\[
(H\widetilde\mu_m-\sigma_z(\widetilde\mu_m)H)\varepsilon_\ell
=
\bigl(\log m+(1-f_z(m))\log\ell\bigr)\varepsilon_{m\ell}.
\tag{12}
\]

Hence

\[
[H,\widetilde\mu_m]_{\sigma_z}\text{ is bounded}
\iff f_z(m)=+1.
\tag{13}
\]

Likewise, for `V_{n,m}` the boundedness criterion is

\[
f_z(n)f_z(m)=+1.
\tag{14}
\]

This control family makes the information content explicit. Twisted Lipschitz regularity does distinguish sign assignments, but only by evaluating their finite multiplicative phase products. In particular, testing prime generators directly reveals the local prime signs: for `m=p`, boundedness is equivalent to `z_p=+1`. The all-plus control makes every prime generator Lipschitz-bounded, while the Möbius assignment `z_p=-1` makes every prime generator fail the test.

That is stronger phase sensitivity than the absolute twisted-commutator norm, but it is not a cheaper global statistic. It is a local readout of the sign data already inserted into `F_z` and `\sigma_z`.

## 2. Relation to `MC-166` and `MC-167`

`MC-166` shows that finite coefficient-decorated raw commutator words retain only two global Möbius phase sectors: a phase-free sector and a sector carrying one copy of the original sign field. `MC-167` then audits the canonical literature-backed `σ`-twist and proves

\[
[D,a]_\sigma=F[H,a],
\]

so every singular-value statistic of the **bounded twisted commutator** is phase-blind.

The Lipschitz test uses a different operator: `|D|=H` but keeps the same twist `\sigma`. It therefore does not fall under the singular-value collapse of `MC-167`. Equations `(3)` and `(9)` show exactly what survives: the unbounded term appears precisely when the twist changes the sign of the semigroup transition. The source-forced operation has recovered phase sensitivity, but only at the already-classified two-sector level.

This closes a natural loophole in the Bost–Connes branch. The failure of absolute twisted-commutator data to see Möbius phase cannot be repaired merely by moving to twisted Lipschitz regularity: the latter sees phase maximally locally, but still does not create a relational quantity whose estimate could average or cancel those phases.

## 3. Prior art and novelty audit

The primary source is Mark Greenfield, Matilde Marcolli and Kevin Teh, *Type III sigma-spectral triples and quantum statistical mechanical systems*, p-Adic Numbers, Ultrametric Analysis and Applications **6** (2014), 81–104, DOI `10.1134/S2070046614020010`, arXiv `1305.5492`.

Their Theorem 4.8 constructs the Riemann-gas `σ`-spectral triple and computes the bounded twisted commutator. Their Remark 4.9 explicitly states that the triple is not Lipschitz regular and gives formula `(2)` for semigroup generators. Thus the non-Lipschitz phenomenon and the generator formula are established prior art.

The general definition of Lipschitz regularity for a twisted spectral triple requires boundedness of `|D|a-\sigma(a)|D|`; Connes–Moscovici's twisted-spectral-triple framework also explains why this is the condition needed to pass to the phase/Fredholm-module picture.

The extension from the source's generator formula to the exact `V_{n,m}` criterion `(9)` and to the matched real prime-sign family `(13)`–`(14)` is an immediate algebraic consequence of the same representation. A targeted literature check found the source formula itself and the standard Lipschitz-regularity framework; there is no basis for a novelty claim. **No novelty claim is made.** The durable contribution here is the line-specific information audit: this apparently promising phase-sensitive regularity test is exactly a local parity selector and therefore supplies no independent global cancellation mechanism.

Primary web anchors checked for this audit:

- arXiv `1305.5492`: https://arxiv.org/abs/1305.5492
- Greenfield–Marcolli–Teh publication DOI: https://doi.org/10.1134/S2070046614020010

## Boundaries and falsification tests

- **Square-free representation.** The classification is for the compressed square-free Riemann-gas representation, where `F` and the matched `F_z` are self-adjoint unitaries. It is not asserted for the full `\ell^2(\mathbb N)` Möbius multiplication operator.
- **Real sign controls.** The matched family uses `z_p\in\{\pm1\}` so that `D_z=F_zH` remains self-adjoint. Arbitrary unit-circle phases require a different spectral-triple audit.
- **Pure semigroup transitions.** Equation `(9)` classifies `V_{n,m}`. Multiplying a transition by a coefficient-algebra element can mask the high-energy domain by vanishing on it, so no universal iff statement is asserted for every coefficient-decorated algebra element.
- **Phase sensitivity is not cancellation.** The bounded/unbounded bit is determined by the finite product `f_z(n)f_z(m)`. It does not measure cancellation among a growing family of Möbius values, exceptional-set mass, or Mertens excursion.
- **No converse arithmetic consequence.** Knowing all these Lipschitz boundedness bits reconstructs local sign products rather than proving a bound on their ordered summatory behavior. No implication toward RH is claimed.
- **Other orientation-sensitive functionals remain open.** Cyclic cocycles, eta-like functionals, genuinely infinite nonlocal constructions, modular data not reducible to this local selector, or another source-forced relational observable require separate analysis.

## Consequence for the research line

The Bost–Connes branch now has a sharper three-way boundary. Absolute twisted-commutator regularity is phase-blind (`MC-167`); twisted Lipschitz regularity is phase-sensitive but merely reads the finite local parity inserted into the twist (`MC-168`); and the obvious global signed eta function directly gives the reciprocal-zeta Dirichlet series (`MC-167`). None supplies the missing intermediate source-to-excursion theorem.

Future Bost–Connes candidates therefore need more than phase sensitivity or a critical-looking regularity threshold. They must produce a genuinely relational or nonlocal statistic whose arithmetic estimate is independently accessible and whose transfer to mean-absolute or endpoint Mertens cancellation is quantitatively cheaper than reconstructing the Möbius signs themselves.