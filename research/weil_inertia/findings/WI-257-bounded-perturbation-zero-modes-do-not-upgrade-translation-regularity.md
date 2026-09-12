# WI-257 — Bounded-perturbation zero modes do not upgrade the translation modulus

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

`WI-239` already isolates Suzuki's fixed-interval Weil operator as a logarithmic principal form plus a bounded zeta-specific remainder, while `WI-256` leaves one plausible small-aperture continuation: use the actual zero-mode equation `A_{a_*}v=0` to obtain stronger translation regularity and thereby control the nonnegative remainder

\[
E_v(r)=\int_0^{2r}\left(\frac rh-\frac12\right)(1-C_v(h))\,dh.
\]

There is now an exact boundary on that idea. After unitary dilation to `(-1,1)`, **all of Suzuki's localized Weil operators have the same operator domain**: the entire `a`-dependence is a bounded self-adjoint perturbation of one fixed logarithmic operator. Consequently, the zero-mode equation supplies no generic operator-domain upgrade beyond membership in that fixed domain. More strongly, for an arbitrary bounded self-adjoint perturbation, *every* vector in the fixed operator domain can be made a zero mode by a rank-at-most-two perturbation. Since that domain contains vectors with different quadratic translation-defect coefficients, abstract bounded-perturbation regularity cannot force the `E_v(r)=o(r^2)` input sought after `WI-256`.

The surviving route must use the **specific arithmetic structure** of Suzuki's perturbation — the von-Mangoldt weighted translations and their prime-power thresholds, together with the fixed archimedean kernel — rather than merely the facts that the perturbation is bounded and the vector solves a zero-eigenvalue equation.

## 1. Suzuki's scaled closed form has an `a`-independent principal part

Let

\[
H=L^2(-1,1)
\]

and let

\[
(U_av)(t)=\sqrt a\,v(at),\qquad U_a:L^2(-a,a)\to H,
\]

be the unitary dilation. Suzuki transfers the localized Weil form to `(-1,1)` and writes its closed form as

\[
\boxed{\bar q_a=\bar q^0+\bar q_a^1,}
\tag{1}
\]

where

\[
\bar q^0(w)=\overline{\mathcal L}(w)-(2A+1)\|w\|_2^2
\tag{2}
\]

is independent of `a`. The explicit Rayleigh formula contains, besides this logarithmic principal form, the scalar `-\log a`, finitely many translation terms with shifts `(\log n)/a` and weights `\Lambda(n)/\sqrt n` for `n\le e^{2a}`, and a continuous-kernel archimedean term. In the proof of lower semicontinuity Suzuki states that on every compact `a`-range

\[
\bar q_a^1(w)=O(\|w\|_2^2)
\tag{3}
\]

uniformly in `a`, and that `\bar q_a^1` is a finite sum of quadratic forms associated with translation operators and integral operators with continuous kernels.

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (revised 17 Aug 2026), especially equations (4.1)--(4.6), (4.9), and Section 4.4: <https://arxiv.org/html/2606.09096v2>.

The source also emphasizes that `D(A_a)` is difficult to describe explicitly and is strictly larger than `H_0^1(-a,a)`; in particular it contains constants. The result below does **not** contradict that observation: it identifies the domains after scaling without producing an intrinsic pointwise/Sobolev description of the common domain.

## 2. Exact operator-domain invariance

Let `T_0` be the lower-bounded self-adjoint operator associated with the closed form `\bar q^0`. By polarization, the bounded Hermitian form `\bar q_a^1` is represented by a bounded self-adjoint operator `K_a\in\mathcal B(H)`:

\[
\bar q_a^1(f,g)=\langle K_af,g\rangle.
\tag{4}
\]

The standard bounded-perturbation theorem for closed forms/operators then gives

\[
\boxed{T_a=T_0+K_a,\qquad D(T_a)=D(T_0),}
\tag{5}
\]

where `T_a` is the self-adjoint operator associated with `\bar q_a`. This is the bounded case of the classical Kato--Rellich perturbation theory; see T. Kato, *Perturbation Theory for Linear Operators*, Springer, 1995 reprint of the 1980 edition, which Suzuki also cites.

Suzuki's scaling identity is an identity of the closed quadratic forms associated with `A_a` and `\bar q_a`. With the unitary normalization above,

\[
Q_W^a(v)=\bar q_a(U_av).
\tag{6}
\]

Uniqueness of the self-adjoint operator represented by a closed lower-bounded form therefore yields

\[
\boxed{U_aA_aU_a^{-1}=T_0+K_a}
\tag{7}
\]

and hence the exact common-domain statement

\[
\boxed{U_aD(A_a)=D(T_0)\quad\text{for every }a>0.}
\tag{8}
\]

Thus the changing support radius changes the bounded part of the scaled operator, not its operator domain.

## 3. A zero mode gives no abstract regularity upgrade

If `v` is a zero mode of `A_a` and `w=U_av`, then (7) gives

\[
(T_0+K_a)w=0,
\qquad
T_0w=-K_aw\in H.
\tag{9}
\]

But `w\in D(T_0)` already means precisely that `T_0w\in H`. Therefore, if one uses only that `K_a` is bounded self-adjoint, (9) does not place `w` in any smaller or smoother generic operator domain.

There is a sharp abstract stress test. Let `u\in D(T_0)` be normalized and put

\[
y=-T_0u,
\qquad
\alpha=\langle y,u\rangle\in\mathbb R,
\qquad
z=y-\alpha u\perp u.
\tag{10}
\]

With Suzuki's convention that the inner product is linear in the first variable, define

\[
Kf=\alpha\langle f,u\rangle u
   +\langle f,u\rangle z
   +\langle f,z\rangle u.
\tag{11}
\]

Then `K` is bounded, self-adjoint, has rank at most two, and

\[
Ku=\alpha u+z=y=-T_0u.
\tag{12}
\]

Hence

\[
\boxed{(T_0+K)u=0.}
\tag{13}
\]

So **every normalized vector in `D(T_0)` can be a zero mode of some bounded self-adjoint perturbation of the same logarithmic principal operator**. No regularity statement that follows only from `u\in D(T_0)` plus an unspecified bounded self-adjoint zero-mode equation can distinguish the actual Weil zero mode.

## 4. The common domain already permits incompatible `E(r)` coefficients

The rank-two stress test becomes directly relevant to `WI-256` because `D(T_0)` contains vectors with different small-translation behavior.

First, Suzuki proves that constants belong to `D(A_a)`. By (8), the normalized constant

\[
u_0=2^{-1/2}\mathbf 1_{(-1,1)}
\tag{14}
\]

belongs to `D(T_0)`. After zero extension,

\[
C_{u_0}(h)=1-\frac h2\qquad(0\le h\le2),
\tag{15}
\]

so for `0<r<1`

\[
\boxed{E_{u_0}(r)=\frac12r^2.}
\tag{16}
\]

Second, choose a normalized `\phi\in C_c^\infty(-1,1)`. Since `H_0^1` is the domain of Suzuki's symmetric operator `B_a` and `A_a` is its Friedrichs extension, dilation and (8) give `\phi\in D(T_0)`. Standard translation differentiability in `L^2` gives

\[
1-C_\phi(h)=\frac12\|\tau_h\phi-\phi\|_2^2=O(h^2),
\tag{17}
\]

and consequently

\[
\boxed{E_\phi(r)=O(r^3)=o(r^2).}
\tag{18}
\]

By (10)--(13), both `u_0` and `\phi` can be zero modes of bounded self-adjoint perturbations of `T_0`. Therefore the abstract class

\[
\text{logarithmic principal operator} + \text{bounded self-adjoint perturbation} + \text{zero mode}
\]

cannot determine even the quadratic coefficient of `E(r)`: it allows `1/2` in (16) and `0` in (18).

## 5. What this closes, and what remains open

This is a strengthening of the boundary already found in `WI-239`, not a rediscovery of its pure-core countermodel. `WI-239` shows that generic first-crossing/compactness/logarithmic-singularity structure does not prevent a zero mode. The new point is that **even after inserting the zero-mode equation**, abstract bounded-perturbation operator theory supplies no additional translation modulus: the scaled operator domain is fixed, and arbitrary vectors of that domain can be abstract zero modes.

Accordingly, the small-radius continuation suggested by `WI-256` is now falsified if it has the form

\[
A_{a_*}v=0
\quad\Longrightarrow\quad
\text{extra regularity solely because the remainder is bounded}.
\tag{19}
\]

A viable continuation must instead use information discarded by (19), for example the exact finite sum of von-Mangoldt weighted translations, the way new shifts enter when `2a` crosses `\log n`, coupling across several aperture radii, or the specific smooth archimedean kernel. The medium-radius/multi-threshold branch of the accepted sliding-autocorrelation clue therefore survives and becomes relatively more important.

This finding does not change any simple-zero proportion, does not bound off-line zero mass, and does not prove or disprove RH.

## 6. Prior-art and novelty audit

The load-bearing pieces separate as follows.

- **Literature-backed:** Suzuki's scaled form, its `a`-independent logarithmic principal part, the uniformly `L^2`-bounded finite-translation/continuous-kernel remainder, the Friedrichs realization of `A_a`, and the inclusion of constants in `D(A_a)`.
- **Classical operator theory:** a bounded self-adjoint perturbation of a self-adjoint operator is self-adjoint on the same operator domain; equivalently, adding a bounded Hermitian form to a closed lower-bounded form produces the operator `T_0+K` on `D(T_0)`. This is standard Kato perturbation theory.
- **Mathia deduction:** applying that theorem to Suzuki's *scaled* decomposition gives (7)--(8); the rank-two construction (10)--(13) then proves the no-go for generic zero-mode regularity and, with (16)--(18), falsifies any abstract attempt to determine the second-order translation-defect coefficient from bounded-perturbation zero-modehood alone.

A targeted prior-art audit around Suzuki's operator formulation, Kato bounded perturbations, and logarithmic-Laplacian domain theory located the ingredients above but no source formulating this particular fixed-domain/rank-two no-go for the localized Weil first-crossing program. Search absence is not a priority claim.

## Consequence for the research line

`WI-256` correctly identified the zero-mode equation as the only plausible source of an improved small-radius translation modulus after generic `H^\log`/domain regularity failed. `WI-257` narrows that statement: **the zero-mode equation is useful only through the special arithmetic form of `K_{a_*}`.** Treating it as an arbitrary bounded perturbation cannot improve `E_v(r)` at all. Future small-aperture work should therefore derive a source-specific identity from the actual prime-translation operator, or abandon generic regularity and move to the medium-radius prime-threshold/full-family constraints of `WI-253`.