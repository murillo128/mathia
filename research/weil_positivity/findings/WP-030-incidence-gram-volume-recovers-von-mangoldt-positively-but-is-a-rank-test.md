# WP-030 — Incidence Gram volume recovers von Mangoldt positively, but only as a rank test

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION` for the direct globalization of the incidence-sensitive positive readout left open by WP-029. The Boolean commutator does admit a canonical degree-sensitive positive compression whose Gram determinant recovers `Lambda(n)` exactly, without a supertrace and without an explicit axis projector. The mechanism is nevertheless only a rank/volume test: it detects that the occupied-prime degree-one space is one-dimensional. It is universal for weighted free commutative monoids, has no archimedean or polar content, and a direct addition of an independent infinite-place degree-one direction kills the determinant even on prime powers. Moreover, after the exact finite Weil coefficients have been extracted, the WP-005 autocorrelation obstruction applies unchanged.

## 1. Start from the exact Boolean commutator

For

\[
\alpha=v(n),\qquad
S=\{p:\alpha_p>0\},\qquad
r=|S|=\omega(n),
\]

WP-029 identifies the backward Boolean cube with

\[
\mathcal H_\alpha\cong\Lambda^*\mathbb C^r
\]

and defines

\[
C_\alpha
=\sum_{p\in S}a_p\gamma_p,
\qquad
a_p=\log p,
\qquad
\gamma_p=i(\iota_p-\epsilon_p).
\tag{1}
\]

Let `P_k` denote the canonical projection onto exterior degree `k`. The new object is not a scalar spectral function of `C_alpha`; it uses the incidence information that WP-029 showed survives off diagonal.

Consider the vacuum-to-one-form block

\[
B_\alpha:=P_1C_\alpha P_0:
\Lambda^0\mathbb C^r\longrightarrow\Lambda^1\mathbb C^r.
\tag{2}
\]

If `Omega` is the unit vacuum and `e_p` is the degree-one basis vector, then

\[
\gamma_p\Omega=-i e_p,
\]

so

\[
B_\alpha\Omega
=-i\sum_{p\in S}a_p e_p.
\tag{3}
\]

Thus `B_alpha` is a canonical rank-one incidence channel carrying all individual `log p` weights.

## 2. Its positive Gram operator has determinant exactly `Lambda(n)^2`

Form the degree-one Gram operator

\[
G_\alpha
:=B_\alpha B_\alpha^*
=P_1C_\alpha P_0C_\alpha P_1
\succeq0.
\tag{4}
\]

In the degree-one basis its matrix is

\[
(G_\alpha)_{pq}=a_pa_q.
\tag{5}
\]

Equivalently, if

\[
a=(a_p)_{p\in S}\in\mathbb R^r,
\]

then

\[
\boxed{G_\alpha=|a\rangle\langle a|.}
\tag{6}
\]

Therefore

\[
\operatorname{rank}G_\alpha=1
\]

for every `n>1`. Taking the determinant on the canonical degree-one space gives

\[
\det_{\Lambda^1\mathbb C^r}G_\alpha
=\begin{cases}
(\log p)^2,&r=1,\\
0,&r\ge2.
\end{cases}
\tag{7}
\]

But `r=1` is exactly the condition that `n=p^k` for some prime `p` and `k>=1`. Since all `a_p` are positive,

\[
\boxed{
\sqrt{\det G_{v(n)}}=\Lambda(n),\qquad n\ge2.
}
\tag{8}
\]

This can be written without determinants as a top-exterior norm. Since

\[
B_\alpha^*: \Lambda^1\mathbb C^r\to\Lambda^0\mathbb C^r
\]

has one-dimensional target,

\[
\boxed{
\left\|\bigwedge^r B_\alpha^*\right\|
=\Lambda(n).
}
\tag{9}
\]

For `r=1` this is simply the norm `log p`; for `r>=2`, the target `\bigwedge^r\Lambda^0` is zero. Equations (8)-(9) are basis-independent. Changing Boolean cell orientations conjugates `G_alpha` unitarily, leaving its determinant unchanged.

So the incidence-sensitive escape left open by WP-029 is real at the finite-place level: **the Mangoldt selector can be obtained from a genuinely positive Gram operator and a canonical volume invariant, with no alternating supertrace.**

## 3. Critical attenuation gives the exact finite Weil coefficient measure

Multiplying (8) by the intrinsic half-energy attenuation gives

\[
e^{-E(\alpha)/2}\sqrt{\det G_\alpha}
=\frac{\Lambda(n)}{\sqrt n}.
\tag{10}
\]

Hence

\[
\boxed{
\sum_{\alpha\ne0}
 e^{-E(\alpha)/2}
 \sqrt{\det G_\alpha}\,\delta_{E(\alpha)}
=
\sum_p\sum_{k\ge1}
(\log p)p^{-k/2}\delta_{k\log p}.
}
\tag{11}
\]

This is the same exact finite positive-location measure obtained in WP-004 and WP-018, but the selector is now realized differently:

```text
WP-004: explicit axis compression + occupation normalization
WP-018: Boolean residual energy + alternating supertrace
WP-030: Boolean incidence block + positive Gram operator + top volume
```

The exponent `k` disappears automatically because the incidence block only sees the occupied coordinate set and its edge weight `log p`.

## 4. Why this does not yet give a positive Weil quadratic form

The positivity in (4) is genuine but limited. The map

\[
G\longmapsto\sqrt{\det G}
\]

is not a positive **linear functional** on operators. It is a nonlinear volume invariant. The exact support cancellation in (8) comes from rank deficiency:

\[
\dim\Lambda^1\mathbb C^r=r,
\qquad
\operatorname{rank}G_\alpha=1.
\]

Thus the determinant vanishes for every mixed-prime integer because a one-dimensional image has zero `r`-dimensional volume when `r>=2`.

This is not the same defect as WP-018's signed supertrace, but it is also not an independent RH-sensitive sign theorem. The arithmetic support is encoded by the elementary fact

\[
\omega(n)=1\iff n\text{ is a prime power}.
\]

The geometric construction packages that fact canonically inside the Boolean incidence algebra; it does not explain any global cancellation between finite and archimedean terms.

Once (11) has been extracted, the exact Weil autocorrelation lift is still the translation comb of WP-005. Therefore the same coefficient measure again becomes an indefinite finite-prime quadratic operator on the Weil test-function space. Replacing the coefficient extraction by a Gram determinant has not changed that forced second step.

## 5. A direct independent infinite-place extension kills the selector

The rank interpretation gives a useful exact globalization obstruction.

Suppose one tries to add an independent archimedean degree-one sector `K_infinity` of dimension `m>=1` while keeping the same scalar-vacuum incidence architecture:

\[
\mathcal H_1^{\rm tot}
=\Lambda^1\mathbb C^r\oplus K_\infty,
\qquad
B_{\rm tot}^*:\mathcal H_1^{\rm tot}\to\mathcal H_0,
\qquad
\dim\mathcal H_0=1.
\tag{12}
\]

Whatever the finite and infinite coefficients are,

\[
\operatorname{rank}(B_{\rm tot}B_{\rm tot}^*)\le1.
\]

But for every nontrivial integer `n`, `r>=1`, so

\[
\dim\mathcal H_1^{\rm tot}=r+m\ge2.
\]

Consequently

\[
\boxed{
\det_{\mathcal H_1^{\rm tot}}
(B_{\rm tot}B_{\rm tot}^*)=0
}
\tag{13}
\]

**even when `n=p^k` is a prime power**. Therefore the exact positive selector (8) cannot be globally completed by simply adjoining one or more independent infinite-place one-form directions to the same rank-one vacuum channel.

There are only two ways around this exact obstruction:

1. compute the determinant only on the finite degree-one block and append the archimedean contribution later, which is a decoupled completion and supplies no common positivity theorem; or
2. change the global geometry so that the degree-zero/boundary target, incidence map, quotient, or coupling has genuinely higher rank and mixes finite and infinite sectors before the positive invariant is taken.

The second possibility remains live, but it is additional structure not contained in the local Boolean Gram mechanism.

## 6. Matched generalized-prime control

Replace rational primes by generators `q_j` of a free commutative monoid with arbitrary positive weights `a_j`. The identical construction gives

\[
B\Omega=-i\sum_j a_j e_j,
\qquad
G=|a\rangle\langle a|,
\]

and hence

\[
\sqrt{\det G}
=\begin{cases}
a_j,&|S|=1,\\0,&|S|\ge2.\end{cases}
\tag{14}
\]

This is exactly the generalized von Mangoldt support/weight rule when `a_j=log|q_j|`. Thus the Gram-volume positivity is universal free-monoid geometry, just like the Boolean selector control in WP-018. It cannot distinguish the rational-prime system from Beurling systems whose zeta functions have zeros far to the right of `1/2`.

That control sharply limits interpretation: (8) is a useful finite arithmetic realization, not evidence that the determinant positivity itself contains RH information.

## 7. Relation to WP-018 and WP-029

WP-018 showed that one canonical local realization of `Lambda` uses a signed Boolean supertrace, so positivity of its residual-energy operator does not imply positivity of the selector. WP-029 then corrected an overstrong attempted no-go by showing that `(C_alpha)_+` can remain positive while retaining off-diagonal Boolean orientation, leaving an incidence-sensitive positive readout as a real escape route.

WP-030 resolves that escape route at the first finite-place level:

```text
oriented Boolean commutator C_alpha
    -> vacuum/one-form incidence block B_alpha
    -> positive Gram G_alpha = B_alpha B_alpha^*
    -> top Gram volume sqrt(det G_alpha)
    -> Lambda(n) exactly
```

So it would be incorrect to claim that **every** exact local Mangoldt selector must use alternating signs. A positive Gram geometry can encode the same support by degeneracy instead.

The new limitation is different and more precise: this positive realization is nonlinear and rank-sensitive, remains universal under generalized-prime controls, is destroyed by the naive addition of an independent infinite-place degree-one direction, and still enters the indefinite WP-005 autocorrelation operator once converted into the actual Weil quadratic form.

## 8. Prior-art and novelty audit

No theorem-level novelty is claimed.

- The von Mangoldt support rule `Lambda(p^k)=log p`, zero on integers with at least two distinct prime factors, is classical.
- Positivity of `BB^*`, the Gram-determinant/volume identity, rank-one determinants, and exterior-power norms are standard finite-dimensional linear algebra.
- The generalized-prime control is the same standard generalized-von-Mangoldt structure already anchored in this branch.

Searches for combinations of von Mangoldt/prime-power selectors with Gram determinants, exterior algebra, and Clifford/Boolean incidence did not reveal a reliable prior source for this exact packaging, but absence of a search hit is not a novelty claim. The durable Mathia-specific content is the exact specialization to the WP-029 commutator and the resulting boundary statement (13).

The novelty gate is therefore intentionally conservative: **this is a new organization of already-elementary ingredients inside the current Mathia construction, not a new theorem about the von Mangoldt function.** Its value is that it changes the research frontier: local positive incidence geometry can reproduce the finite coefficient without supertrace, so future no-go arguments must target the global coupling/sign theorem rather than assume local positivity and exact Mangoldt support are incompatible.

## 9. Falsification / audit tests

Withdraw or narrow this finding if any of the following fails:

1. `B_alpha=P_1 C_alpha P_0` sends the vacuum to `-i sum_p (log p)e_p`;
2. `G_alpha=B_alpha B_alpha^*` is the rank-one matrix `((log p)(log q))_{p,q in S}`;
3. its determinant is `(log p)^2` for support size one and zero for support size at least two;
4. therefore `sqrt(det G_{v(n)})=Lambda(n)` for every `n>=2`;
5. the determinant is invariant under unitary changes of the degree-one basis/orientation gauge;
6. the same calculation survives arbitrary positive generator weights and generalized-prime controls;
7. any direct extension with a nonzero independent archimedean degree-one sector and the same one-dimensional vacuum target has total Gram rank at most one and hence zero top determinant for every `n>1`;
8. using (10) as the finite coefficient measure leaves the WP-005 autocorrelation lift unchanged.

All eight points are finite-dimensional or immediate consequences of the already-audited WP-005 coefficient-to-Weil lift. No RH assumption, zero data, analytic continuation, or numerical experiment enters the derivation.

## 10. Consequence for the research line

The finite-place problem is now sharper than after WP-029. **Prime Lattice does contain an intrinsic positive Gram object whose own nonnegative volume gives the exact Mangoldt coefficient.** The obstacle is no longer merely that Möbius/Boolean cancellation needs signs.

But the mechanism succeeds by a local rank degeneracy, not by a global positivity theorem. It supplies neither the gamma/pole sector nor positivity of the autocorrelation form, and the simplest attempt to place the infinite place in the same one-form geometry annihilates the selector.

A surviving global route must therefore do more than preserve Boolean orientation. It must introduce a genuinely coupled finite/archimedean geometry with enough rank or boundary structure to avoid (13), while producing a **linear quadratic Weil form whose nonnegativity is independently geometric**. That remains the missing step.

## Internal dependencies

- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-005-prime-lattice-axis-positivity-does-not-survive-weil-autocorrelation-lift.md`
- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-029-even-commutator-energies-radialize-but-positive-one-sided-parts-retain-orientation.md`
