# FD-200 — Matched horizon-mode dilations are a universal divisor cocycle

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** cross-horizon Fourier algebra / matched dilation / route restriction
- **Depends on:** FD-117, FD-121, FD-198, FD-199
- **Classification:** `EXACT-DERIVED + CROSS-HORIZON-DIVISOR-COCYCLE + UNIVERSAL-TRIANGULAR-RECURRENCE + NEGATIVE/ROUTE-RESTRICTION`

## Claim

The post-`FD-199` frontier leaves signed cross-mode and cross-horizon combinations as plausible ways to avoid the simultaneous positive-energy tariff of the square-root Fourier band. One especially natural construction is to dilate a Fourier mode and the Farey horizon by the same prime. That entire matched-dilation direction is algebraically flat before any Möbius-specific input is used.

Let `A(0)=0` and let `A(n)` be any cumulative source. Define the signed Farey/divisor coordinate

\[
\mathcal B_H(k)
:=
\sum_{d\mid k}d\,A\!\left(\left\lfloor\frac Hd\right\rfloor\right).
\tag{1}
\]

For every prime `p`, every positive integer `H`, and every `k>=1`,

\[
\boxed{
\mathcal B_{pH}(pk)
=
\mathcal B_{pH}(k)
+p\mathcal B_H(k)
-p\mathbf 1_{p\mid k}\mathcal B_H(k/p).
}
\tag{2}
\]

Equivalently, if `k=p^a m` with `(p,m)=1` and

\[
D_a(H;m)
:=
\mathcal B_H(p^a m)-\mathcal B_H(p^{a-1}m),
\qquad
\mathcal B_H(p^{-1}m):=0,
\tag{3}
\]

then

\[
\boxed{
D_{a+1}(pH;m)=pD_a(H;m)
\qquad(a\ge0).
}
\tag{4}
\]

Thus the first difference along the `p`-adic mode direction at the enlarged horizon is exactly a scaled copy of the previous first difference at the smaller horizon. The matched horizon-mode plane has a universal lower-triangular transport law; there is no Möbius-specific residual to estimate.

When `(q,k)=1`, the prime rule tensorizes to the exact divisor cocycle

\[
\boxed{
\mathcal B_{qH}(qk)
=
\sum_{a\mid q}a\,\mathcal B_{(q/a)H}(k).
}
\tag{5}
\]

This relation is invertible by ordinary Dirichlet Möbius inversion:

\[
\boxed{
\mathcal B_{qH}(k)
=
\sum_{a\mid q}\mu(a)a\,
\mathcal B_{(q/a)H}((q/a)k),
\qquad (q,k)=1.
}
\tag{6}
\]

Consequently, on any divisor-closed collection of matched coprime dilations, the coordinates with both horizon and mode multiplied by `q` contain exactly the same linear information as the fixed-mode horizon coordinates. Cross-horizon averaging along this diagonal cannot create independent deterministic constraints on the source.

The prime-shell specialization is particularly direct. Taking `k=1` in (2),

\[
\boxed{
\frac{\mathcal B_{pH}(p)-\mathcal B_{pH}(1)}p
=
\mathcal B_H(1)
=A(H).
}
\tag{7}
\]

For the physical source `A=M`, every prime-mode observation placed on the matched ridge `(pH,p)` is therefore an exact duplicate of the same Mertens value `M(H)`. Repeating that coordinate at many horizons or primes does not provide the kind of independent cross-horizon cancellation missing from `FD-198`--`FD-199`.

This does **not** say that cross-horizon structure is useless. `FD-121` already proves the opposite. It says that a future gain cannot be attributed to the smallness of a matched-dilation residual such as the left side of (2), because that residual vanishes for every source after the explicit lower-mode leakage is included. Useful cross-horizon information must come from a mismatch not removed by this universal divisor algebra: fixed-mode comparisons, nonlocal signed couplings of different quotient coordinates, order-sensitive information, nonlinear combinations before taking a norm, or another source-specific relation.

## 1. Prime-step proof and the lower-mode collision

Write

\[
k=p^a m,
\qquad
(p,m)=1.
\tag{8}
\]

Expanding the divisor sum at the enlarged horizon gives

\[
\mathcal B_{pH}(pk)
=
\sum_{j=0}^{a+1}
\sum_{d\mid m}
 p^j d\,
 A\!\left(
 \left\lfloor\frac{pH}{p^j d}\right\rfloor
 \right),
\tag{9}
\]

whereas

\[
\mathcal B_{pH}(k)
=
\sum_{j=0}^{a}
\sum_{d\mid m}
 p^j d\,
 A\!\left(
 \left\lfloor\frac{pH}{p^j d}\right\rfloor
 \right).
\tag{10}
\]

Their difference is therefore only the new top `p`-adic divisor layer,

\[
\mathcal B_{pH}(pk)-\mathcal B_{pH}(k)
=
\sum_{d\mid m}
 p^{a+1}d\,
 A\!\left(
 \left\lfloor\frac{H}{p^a d}\right\rfloor
 \right).
\tag{11}
\]

For `a=0`, the right side is simply `p B_H(k)`, which is (2) in the coprime case. For `a>=1`, the same top layer is exactly

\[
p\bigl(\mathcal B_H(p^a m)-\mathcal B_H(p^{a-1}m)\bigr),
\tag{12}
\]

because subtracting the two divisor sums at horizon `H` cancels all `p`-adic layers except the top one. Equations (11)--(12) prove (2) and the transport form (4).

This isolates the only obstruction to the naive coprime rectangle. If `p` does not divide `k`,

\[
\mathcal B_{pH}(pk)-\mathcal B_{pH}(k)-p\mathcal B_H(k)=0.
\tag{13}
\]

If `p` already divides `k`, the defect is not a new cross-horizon source observable; it is the explicit lower mode

\[
\mathcal B_{pH}(pk)-\mathcal B_{pH}(k)-p\mathcal B_H(k)
=-p\mathcal B_H(k/p).
\tag{14}
\]

Thus repeated-prime collisions make the algebra triangular rather than flat, but they still do not generate an unexplained residual.

## 2. Coprime composite dilations are just Dirichlet convolution

Assume `(q,k)=1`. Every divisor of `qk` has a unique factorization `ab` with `a|q` and `b|k`. Hence

\[
\begin{aligned}
\mathcal B_{qH}(qk)
&=
\sum_{a\mid q}\sum_{b\mid k}
 ab\,A\!\left(
 \left\lfloor\frac{qH}{ab}\right\rfloor
 \right)\\
&=
\sum_{a\mid q}
 a\,
 \mathcal B_{(q/a)H}(k),
\end{aligned}
\tag{15}
\]

which is (5). For fixed `H,k`, regard

\[
F(q):=\mathcal B_{qH}(qk),
\qquad
G(q):=\mathcal B_{qH}(k)
\tag{16}
\]

on integers `q` coprime to `k`. Then (5) is simply

\[
F=\operatorname{id}*G.
\tag{17}
\]

The Dirichlet inverse of `id(q)=q` is `mu(q)q`, because

\[
\sum_{a\mid q}a\,\mu(q/a)(q/a)
=q\sum_{a\mid q}\mu(q/a)
=\mathbf 1_{q=1}.
\tag{18}
\]

Applying this inversion gives (6).

The information statement must be read with the same boundary as the formula. If the observation set contains the divisor-closed family needed on the right side, matched and fixed-mode coordinates are linearly interconvertible and no rank is gained. A sparse sensor that omits the intermediate divisor horizons need not be able to execute (5)--(6) internally. The theorem is an algebraic redundancy statement for the available matched family, not a claim that every sparse geometric ladder contains every term of the inversion.

For a **prime** geometric dilation there is no such caveat: (13) already couples only the two horizons `H,pH` and the two modes `k,pk`. Thus on a dyadic ladder, for example, every matched step with odd `k` is exactly flat.

## 3. Relation to the current square-root Fourier frontier

The same-horizon prime-shell identity from `FD-198` is

\[
\mathcal B_H(p)-\mathcal B_H(1)
=pM\!\left(\left\lfloor\frac Hp\right\rfloor\right).
\tag{19}
\]

Equation (7) is its matched cross-horizon counterpart. If the horizon is enlarged from `H` to `pH` while the mode is enlarged from `1` to `p`, the quotient coordinate no longer changes at all:

\[
\left\lfloor\frac{pH}{p}\right\rfloor=H.
\tag{20}
\]

The normalized centered observation is exactly the old endpoint value. Therefore one tempting way to escape the `FD-198`/`FD-199` positive-energy overcoercion—replicate the same quotient witness across horizons and combine those copies—is deterministically redundant. Any improvement from multiple horizons has to compare **different** quotient coordinates or use a source relation between them.

The recurrence also clarifies what happened in the earlier dyadic coherence theorem `FD-121`. Its low-mode identities include

\[
\mathcal B_{2H}(2)=\mathcal B_{2H}(1)+2\mathcal B_H(1),
\tag{21}
\]

which is exactly the flat coprime step (2) with `k=1`. The next mode satisfies

\[
\mathcal B_{2H}(4)
=
\mathcal B_{2H}(2)
+2\mathcal B_H(2)
-2\mathcal B_H(1),
\tag{22}
\]

which is the first repeated-prime triangular step. `FD-121` obtains a genuine energy gap not because either residual in (21)--(22) contains hidden Möbius cancellation—they are universal identities—but because the **separate horizon-local equality rays are incompatible with this common-source triangular transport**.

That distinction is useful at the current frontier. Cross-horizon algebra can still be load-bearing when combined with a nontrivial norm, an extremal geometry, or source restrictions. What is ruled out is a simpler claim that the matched-dilation residual itself is a new signed Farey invariant carrying arithmetic cancellation. It is identically prescribed before the physical source is chosen.

## 4. Representation audit and hostile checks

The result stays entirely in the observation representation of `FD-117`. No inverse source map is used: equations (2) and (5) are obtained by repartitioning the divisors already present in the raw signed Fourier/divisor coordinates. They therefore hold for an arbitrary cumulative source `A`, including synthetic controls that have no multiplicativity, squarefree support or Möbius signs.

This source universality is also the main hostile control. Any proposed statistic formed only from the left side of (2), after adding the explicit lower-mode correction, vanishes on every source and cannot distinguish `M` from the null examples constructed earlier in the line. Conversely, omitting the lower-mode term when `p|k` would manufacture a nonzero quantity whose value is already exactly `-p B_H(k/p)`; interpreting that as new curvature would double-count an existing coordinate.

The floor functions introduce no error. After a divisor `p^j d` is factored, the identity

\[
\left\lfloor\frac{pH}{p^j d}\right\rfloor
=
\left\lfloor\frac{H}{p^{j-1}d}\right\rfloor
\qquad(j\ge1)
\tag{23}
\]

is exact. The recurrence was additionally checked on finite arbitrary integer-valued source arrays over random choices of `H`, `p`, and `k`; the computation is only a regression check, while (9)--(12) are the proof.

The theorem also does not collapse the broader cross-horizon program. Fixed-mode comparisons such as `B_(pH)(k)` versus `B_H(k)`, unmatched mode pairs, or nonlinear combinations are not determined by (2) alone. Those are precisely the directions in which a source-specific relation could still survive.

## 5. Prior-art and formalization gates

The algebra in (5)--(6) is ordinary divisor decomposition and Dirichlet convolution, and the prime recurrence has the same formal flavor as classical prime-step recurrences for divisor sums. No novelty is claimed for those algebraic operations in isolation. A targeted search for the specific floor-quotient Farey/Mertens transform, matched horizon-mode dilation, and Hecke-style prime recurrences did not locate a direct prior formulation of (2)--(7). The line-specific contribution is the route classification at the `FD-198`--`FD-199` frontier: matched cross-horizon Fourier copies are universal divisor redundancy, while repeated-prime collisions leak only into lower existing modes.

No external theorem is load-bearing, so `SOURCES.md` is unchanged. No formalization issue is opened. The finite core is an elementary partition of divisors and Dirichlet inversion; its value here is the representation boundary it places on future cross-horizon constructions rather than a difficult standalone lemma requiring dedicated formal infrastructure.
