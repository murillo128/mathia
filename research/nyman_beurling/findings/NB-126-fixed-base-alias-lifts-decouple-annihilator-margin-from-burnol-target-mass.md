# NB-126 — fixed-base alias lifts decouple annihilator margin from Burnol target mass

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + FIXED-BASE-ALIAS-INVARIANCE + BURNOL-MASS-DECOUPLING + NB-125-ROUTE-BOUNDARY + MULTIBASE-REDIRECT + REPRESENTATION-AUDIT`.

`NB-125` leaves a precise proposed bridge: couple the rootwise annihilator height budget to the inverse-height target-bearing compression law of `NB-116`. Before trying to prove such a coupling, one has to check that the two scalar currencies can in principle see the same source information. At one fixed geometric base they cannot. The `q`-adic zero-power recurrence sees an ordinate only modulo the exact alias period

\[
T_q:=\frac{2\pi}{\log q},
\]

whereas the Burnol defect sees the absolute ordinate through `gamma^2`. This produces an exact matched control: one may move a formal zero-power packet arbitrarily high while preserving every `q`-geometric primitive trace and the exact `NB-124` annihilator margin, yet drive its elementary Burnol target mass to zero.

The alias period itself is not new; `NB-084` already identifies the same period in the actual radial prediction spectrum. The new point here is the splice with `NB-123`--`NB-125`: **the fixed-base recurrence geometry and the absolute-height Blaschke budget are exactly decoupled before any inequality is applied.** Consequently no proof that uses only one fixed-base annihilator margin together with a scalar Burnol tail can manufacture the missing compression lower bound. Some non-aliased joint source statistic must enter first.

## 1. Vertical alias lifts preserve the complete confluent `q`-geometric trace

Fix an integer `q>=2`. Let

\[
F=\{(\rho_j,m_j):1\le j\le s\},
\qquad
\rho_j=\beta_j+i\gamma_j,
\qquad
\frac12<\beta_j<1,
\]

be a finite formal zero-power packet, where `m_j>=1` is the confluent multiplicity and

\[
d(F):=\sum_{j=1}^s m_j.
\]

The adjective *formal* is essential: the points need not be zeros of `zeta`. They are a matched source model for the representation class isolated in `NB-117`.

For integers `ell_j`, define the vertical alias lift

\[
\rho_j^{(\ell)}
:=
\beta_j+i(\gamma_j+\ell_jT_q).
\tag{1}
\]

Then

\[
\boxed{
q^{-\overline{\rho_j^{(\ell)}}}
=
q^{-\overline{\rho_j}}.
}
\tag{2}
\]

Indeed,

\[
q^{-\overline{\rho_j^{(\ell)}}}
=
q^{-\beta_j}e^{i(\gamma_j+\ell_jT_q)\log q}
=
q^{-\beta_j}e^{i\gamma_j\log q}e^{2\pi i\ell_j}.
\]

The invariance is stronger than equality of characteristic roots. For every integer `k>=0` and every confluent degree `0<=r<m_j`,

\[
\boxed{
(q^k)^{-\overline{\rho_j^{(\ell)}}}
(\log q^k)^r
=
(q^k)^{-\overline{\rho_j}}
(\log q^k)^r.
}
\tag{3}
\]

Hence the complete sampled primitive spaces coincide:

\[
\operatorname{span}\left\{
(q^k)^{-\bar\rho_j}(\log q^k)^r
\right\}_{j,r}
=
\operatorname{span}\left\{
(q^k)^{-\overline{\rho_j^{(\ell)}}}(\log q^k)^r
\right\}_{j,r}
\tag{4}
\]

as sequence spaces in `k`. Repeated roots, true multiplicity and accidental alias collisions cause no problem: each factor is preserved individually.

In particular the `NB-124` annihilator

\[
A_{F,q}(z)
=
\prod_{j=1}^s
\bigl(z-q^{-\bar\rho_j}\bigr)^{m_j}
\]

is exactly invariant,

\[
\boxed{A_{F^{(\ell)},q}=A_{F,q},}
\tag{5}
\]

and therefore so is its normalized missing-root margin

\[
\boxed{
\mathfrak s_{F^{(\ell)},q}
=
\mathfrak s_{F,q}.
}
\tag{6}
\]

The rank `d(F)` is unchanged as well. Thus whenever `R>=q^(d+1)`, the full fixed-base target-angle certificate of `NB-124` is numerically identical before and after the lift.

## 2. The same lift drives the Burnol target mass to zero

The elementary Burnol/Blaschke defect of one right-half point is, as in `NB-114`--`NB-116`,

\[
\delta_\rho
=
\frac{2\beta-1}{\beta^2+\gamma^2}.
\tag{7}
\]

For the lifted point `(1)`,

\[
\delta_{\rho_j^{(\ell)}}
=
\frac{2\beta_j-1}
{\beta_j^2+(\gamma_j+\ell_jT_q)^2}
\longrightarrow0
\qquad(|\ell_j|\to\infty).
\tag{8}
\]

For a finite packet, the corresponding finite Blaschke target mass satisfies

\[
\tau(F)
:=1-|B_F(1)|^2
=
1-\prod_j(1-\delta_{\rho_j})^{m_j}
\le
\sum_jm_j\delta_{\rho_j}.
\tag{9}
\]

Consequently, if every lifted ordinate tends to infinity in modulus,

\[
\boxed{
\tau(F^{(\ell)})\longrightarrow0
\quad\text{while}\quad
A_{F^{(\ell)},q}=A_{F,q},
\quad
\mathfrak s_{F^{(\ell)},q}=\mathfrak s_{F,q}.
}
\tag{10}
\]

Equivalently, for every `eta>0` and every finite formal packet `F`, there is a vertical alias lift with

\[
\tau(F^{(\ell)})<\eta
\]

and exactly the same `q`-geometric zero-power traces, recurrence rank, annihilator polynomial and normalized margin.

This remains a valid matched control even if one imposes the **numerical envelopes** used in `NB-116` and `NB-125`. For fixed `beta_j<1`, Bellotti's Vinogradov--Korobov lower bound on `1-beta_j` is eventually satisfied as `|gamma_j+ell_jT_q|` tends to infinity, because its right-hand side tends to zero. Likewise, if the lifted packet has minimum positive ordinate `G` larger than `d(F)`, its synthetic horizontal first moment is zero below `G` and bounded by `d(F)/2` above it, hence obeys an `A_F(T)<=T` envelope. These statements do **not** make the lifted points actual zeta zeros; they show only that the one-sided scalar inequalities themselves do not reject the matched model.

There is therefore no positive function depending only on the fixed-base recurrence margin that can lower-bound the Burnol target mass throughout this representation class. For example, no universal implication of the form

\[
\mathfrak s_{F,q}\ge s_0>0
\quad\Longrightarrow\quad
\tau(F)\ge\Phi_q(s_0)>0
\tag{11}
\]

can hold for formal strip packets: the left side is invariant under `(1)` while the right side can be made arbitrarily small.

## 3. What this rules out in the `NB-116` / `NB-125` bridge

`NB-116` and `NB-125` remain individually source-faithful for actual zeta zeros. The failure is more specific. Their present scalar outputs have discarded complementary information:

- `NB-124`--`NB-125` retain a fixed-base geometric recurrence margin, which is periodic in the ordinate with period `T_q`;
- `NB-116` retains absolute-height Blaschke mass, but not the geometric phase that determines where the same root lands in the recurrence.

Equation `(10)` shows that these two reduced observables do not couple algebraically at one base. In particular, merely substituting the Vinogradov--Korobov height budget from `NB-125` into the inverse-height tail scale from `NB-116` cannot produce a lower bound on target-bearing compression retention. The formal lift can make the height allowance arbitrarily generous and the Burnol mass arbitrarily small without moving the `q`-adic recurrence geometry at all.

This is a route boundary, not a counterexample to any theorem about actual zeros. The actual zeta zero set has strong global constraints and is not invariant under `(1)`. A successful coupling theorem must therefore use some piece of that non-aliased structure rather than only the two scalar summaries already extracted.

## 4. Two multiplicatively independent bases remove the exact alias symmetry

There is a sharp structural redirect. Let `p,q>=2` be multiplicatively independent integers. If a vertical displacement `Delta` preserves the characteristic root at both bases,

\[
p^{-\overline{\rho+i\Delta}}
=p^{-\bar\rho},
\qquad
q^{-\overline{\rho+i\Delta}}
=q^{-\bar\rho},
\tag{12}
\]

then

\[
\Delta\log p\in2\pi\mathbb Z,
\qquad
\Delta\log q\in2\pi\mathbb Z.
\tag{13}
\]

If `Delta!=0`, dividing the two identities would make `log p/log q` rational. That would imply `p^a=q^b` for some positive integers `a,b`, contradicting multiplicative independence. Therefore

\[
\boxed{\Delta=0.}
\tag{14}
\]

So the exact altitude blindness is genuinely a **one-base** phenomenon. A joint certificate at, say, bases `2` and `3`, or a certificate that keeps the full natural-grid primitive rather than one geometric subsequence, has access to information that `(10)` cannot erase.

This does not yet supply the missing compression bound. Near-aliasing at two bases is a Diophantine problem, and separate lower bounds such as `NB-125` can again destroy the phase information if applied before the two bases are coupled. The useful conclusion is narrower and operational: the next bridge should retain a joint non-aliased root statistic **before** taking rootwise radial lower bounds or absolute-height tails.

## 5. Adversarial and prior-art audit

Several possible false strengthenings were checked explicitly.

First, `(10)` is not an actual-zero construction. Vertical aliases generally are not zeta zeros, so the finding cannot refute a theorem that uses an actual-zero relation not encoded by the current scalar budgets. Second, the invariance is exact for all confluent powers because the logarithmic polynomial factor in `(3)` depends only on `k`, not on the absolute ordinate. Third, conjugation symmetry can be preserved by lifting a pair `beta+-i gamma` to `beta+-i(gamma+ell T_q)`; both characteristic roots remain unchanged and both Burnol defects tend to zero. Fourth, the two-base conclusion is exact only for multiplicatively independent bases; powers of one common base retain a common alias period. Finally, `(14)` excludes exact aliases, not arbitrarily accurate simultaneous near-aliases.

`NB-084` is the direct internal prior-art boundary: it already proves that integer-dilation prediction periodizes the Mellin boundary in alias classes of spacing `2pi/log q`. No novelty is claimed for sampling aliasing itself. The line-local advance is that the same exact symmetry now yields a matched control for the **zero-power annihilator/Burnol interface** created by `NB-124`--`NB-125`, and identifies a concrete way to break it. A targeted literature search found neighboring Nyman--Beurling multiscale and Hardy-space work but no result that supplies this specific fixed-base annihilator-to-Burnol coupling; no external theorem is needed for the proof, so `SOURCES.md` requires no new dependency.

## Consequence

The frontier after `NB-125` should be sharpened. The missing theorem is not merely “convert height entropy into compression retention.” At one fixed base that formulation has an exact alias matched control. The source-facing task is first to construct a **joint non-aliased target-bearing statistic**—for example from two multiplicatively independent geometric grids or directly from the natural integer cells—and only then ask whether actual zeta zero density and zero-free information force that statistic away from the inverse-section near-kernel. This preserves the useful rank/height obstruction of `NB-125` while removing an exact representation-level blind spot before further quantitative work.