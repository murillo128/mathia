# PL-364 — Unconstrained infinite signed lattice-shift filters are coefficientwise universal by Möbius inversion

**Evidence:** `EXACT-DERIVED + CLASSICAL-MOBIUS-INVERSION + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-363`.

**Status:** `INFINITE-SUPPORT-ALONE-DOES-NOT-SUPPLY-RIGIDITY-BECAUSE-THE-FILTER-COEFFICIENTS-PROGRAM-ANY-OUTPUT-SEQUENCE`.

## Precise claim

`PL-363` classifies fixed **finite** signed combinations of multiplicative lattice shifts. Their output on the coefficient-one zeta vector is periodic, so pole cancellation moves ordinary convergence from `Re(s)>1` to `Re(s)>0` but yields only the classical periodic/Hurwitz-zeta continuation mechanism.

The first apparent escape is therefore to drop finiteness and allow a fixed infinite signed or complex filter

\[
T_c=\sum_{m\ge1}c_m S_m,
\qquad
S_m e_n=e_{mn}.
\tag{PL364-1}
\]

Without an independent analytic/operator restriction on `c`, however, this enlargement is maximally non-rigid. On the formal coefficient-one vector

\[
\Omega=\sum_{n\ge1}e_n,
\tag{PL364-2}
\]

the coefficient of `e_k` in `T_c\Omega` is well-defined **coefficientwise** for every arithmetic function `c`, because only divisors of `k` can contribute:

\[
(T_c\Omega)_k
=
\sum_{m\mid k}c_m
=(c*\mathbf 1)(k),
\tag{PL364-3}
\]

where `*` is Dirichlet convolution and `\mathbf 1(n)=1`.

Since the Dirichlet inverse of `\mathbf 1` is the Möbius function `\mu`, convolution by `\mathbf 1` is an algebraic bijection on the space of all arithmetic functions. Explicitly, for **every** prescribed target coefficient sequence `b:\mathbb N\to\mathbb C`, the unique filter

\[
c=\mu*b
\tag{PL364-4}
\]

satisfies

\[
\boxed{T_c\Omega=\sum_{n\ge1}b_n e_n}
\tag{PL364-5}
\]

coefficientwise. Thus unrestricted fixed infinite signed lattice-shift filters can program any arithmetic output at all.

This is a decisive negative control on the infinite-support escape left open by `PL-363`: **infinite support is not additional arithmetic structure**. Any RH-relevant mechanism in this direction must impose an independently justified restrictive class of filters—topological, summability, operator-theoretic, functional-equation, source-forced, or otherwise—whose allowed coefficients are not freely programmable by Möbius inversion.

## 1. Exact divisor-convolution calculation

The exponent-lattice shift is

\[
v(mn)=v(m)+v(n),
\qquad
S_m z^{v(n)}=z^{v(m)+v(n)}.
\tag{PL364-6}
\]

For fixed `k`, the term `e_k` can arise from the pair `(m,n)` exactly when `mn=k`. Hence even though (PL364-1) is an infinite formal sum, its action on `\Omega` is locally finite in every coefficient:

\[
[e_k]T_c\Omega
=
\sum_{mn=k}c_m
=
\sum_{m\mid k}c_m.
\tag{PL364-7}
\]

No convergence or rearrangement theorem is being used here. The finite divisor set of `k` makes each coefficient an ordinary finite sum.

Let `\varepsilon` denote the convolution identity,

\[
\varepsilon(1)=1,
\qquad
\varepsilon(n)=0\quad(n>1).
\tag{PL364-8}
\]

Classical Möbius inversion is precisely

\[
\mu*\mathbf 1=\mathbf 1*\mu=\varepsilon.
\tag{PL364-9}
\]

For an arbitrary target arithmetic function `b`, put `c=\mu*b`. Associativity and commutativity of Dirichlet convolution give

\[
(c*\mathbf 1)
=(\mu*b)*\mathbf 1
=b*(\mu*\mathbf 1)
=b*\varepsilon
=b.
\tag{PL364-10}
\]

Conversely, if `c*\mathbf 1=0`, convolution with `\mu` gives `c=0`. Therefore

\[
\boxed{
 c\longmapsto (T_c\Omega)_\bullet=c*\mathbf 1
}
\tag{PL364-11}
\]

is not merely surjective but an algebraic bijection on all complex-valued arithmetic functions.

In formal prime-exponent coordinates the same statement is the elementary factorization

\[
\Omega(z)=\sum_{n\ge1}z^{v(n)}
=
\prod_p(1-z_p)^{-1},
\tag{PL364-12}
\]

and

\[
C(z)\Omega(z)=B(z),
\qquad
C(z)=\sum_{n\ge1}c_nz^{v(n)},
\qquad
B(z)=\sum_{n\ge1}b_nz^{v(n)}.
\tag{PL364-13}
\]

The formal inverse is

\[
\Omega(z)^{-1}
=
\sum_{n\ge1}\mu(n)z^{v(n)}
=
\prod_p(1-z_p),
\tag{PL364-14}
\]

again interpreted coefficientwise: every fixed monomial involves only finitely many contributing divisors. The prime-lattice geometry therefore reproduces exactly the classical Dirichlet-convolution algebra; unrestricted infinite filtering introduces no extra rigidity beyond that algebra.

## 2. Canonical stress test: the Möbius filter annihilates the whole zeta tail

Take the target `b=\varepsilon`. Equation (PL364-4) gives `c=\mu`, so

\[
\boxed{
\left(\sum_{m\ge1}\mu(m)S_m\right)\Omega=e_1
}
\tag{PL364-15}
\]

coefficientwise. Indeed,

\[
\sum_{m\mid k}\mu(m)
=
\begin{cases}
1,&k=1,\\
0,&k>1.
\end{cases}
\tag{PL364-16}
\]

Thus the most arithmetic-looking infinite signed filter already demonstrates the programmability in its sharpest form: it sends the entire coefficient-one lattice to the vacuum coefficient.

Where absolute convergence permits multiplication of Dirichlet series, this is the familiar identity

\[
\left(\sum_{m\ge1}\frac{\mu(m)}{m^s}\right)
\left(\sum_{n\ge1}\frac1{n^s}\right)
=
\frac1{\zeta(s)}\zeta(s)=1,
\qquad \operatorname{Re}s>1.
\tag{PL364-17}
\]

But (PL364-15) is stronger in a different sense: it is a coefficient identity and needs no analytic continuation. Conversely, it supplies **no** continuation past `Re(s)=1`; doing so through (PL364-17) would require importing the meromorphic theory of `\zeta` and `1/\zeta` rather than deriving it from the formal filter.

This control prevents a misleading inference. The appearance of Möbius signs, square-free support, or the formal reciprocal Euler product does not by itself turn the infinite filter into an RH mechanism. `PL-141` already records the complementary divisor-orientation issue for the reciprocal Dirichlet series: nontrivial zeta zeros become poles of `1/\zeta`, so a genuine RH route would need analytic information not contained in the coefficient inversion alone.

## 3. Dirichlet-series readout is only conditional on analytic hypotheses

Let

\[
C(s)=\sum_{m\ge1}c_m m^{-s},
\qquad
B(s)=\sum_{n\ge1}b_n n^{-s}.
\tag{PL364-18}
\]

If `C(s)` and `\zeta(s)` are absolutely convergent at a given `s`, then the standard Dirichlet-product theorem and (PL364-3) give

\[
B(s)=C(s)\zeta(s).
\tag{PL364-19}
\]

More generally, one may state the identity in any region where the relevant rearrangement/product theorem is independently justified. Nothing in the algebraic bijection (PL364-11) provides such a region automatically for an arbitrary `c`.

This distinction is essential for the research mandate. Because `b` can be prescribed arbitrarily, one can choose a target whose Dirichlet series has any convenient convergence behavior, zero set, pole set, or lack of continuation compatible with the chosen sequence. The corresponding `c=\mu*b` then merely encodes that choice. A zero or spectral feature observed after such unconstrained filtering is therefore not evidence that the prime lattice forced it.

In particular, one may not argue

\[
B=C\zeta
\tag{PL364-20}
\]

outside a common legitimate product domain and then attribute the continuation or zero divisor of `B` to the lattice filter. If either side is continued meromorphically, the continuation must come from an external theorem or a separately defined summation/renormalization scheme. The formal coefficient algebra itself stops short of that analytic information.

## 4. What survives after the programmability collapse

The negative result does **not** rule out infinite or scale-dependent signed renormalization. It identifies the missing hypothesis that any such proposal must make load-bearing.

A meaningful infinite-filter class `\mathcal C` must be specified independently of the desired output and be substantially smaller than all arithmetic functions. Examples of potentially nontrivial restrictions include:

- `c` belonging to a fixed `\ell^1`, weighted `\ell^2`, multiplier, Schatten, Hardy, Sobolev, or distributional class with a source-derived norm bound;
- a scale-dependent family `c^{(X)}` obeying a canonical limiting law rather than being selected after specifying the target;
- a counterterm or finite-part prescription forced by a functional equation, trace identity, or local-global symmetry;
- non-coefficientwise mixing for which the divisor-convolution inverse is no longer available;
- a target-relative quotient/compression whose admissible filters are fixed before the zeta zero divisor is read out.

The point is not that any of these succeeds. It is that after (PL364-11), **some independent restriction of this kind is logically necessary**. Without it, “choose an infinite signed lattice filter” is equivalent to “choose the output coefficients.”

This also sharpens the finite/infinite contrast with `PL-363`. Finite support is a genuine restriction: it forces periodic output and hence a classical Hurwitz-zeta mechanism. Removing that restriction entirely does not reveal a richer canonical continuation theory; it removes all rigidity and yields full programmability. The next useful regime must therefore lie strictly between those two extremes.

## 5. Prior-art and novelty audit

No novelty is claimed for Dirichlet convolution, Möbius inversion, or the reciprocal identity `\mu*\mathbf 1=\varepsilon`. These are classical arithmetic-function algebra. The Encyclopedia of Mathematics entry “Dirichlet convolution” states the convolution law, the criterion for Dirichlet invertibility, identifies `\mu` as the inverse of the constant-one function, and gives the Möbius inversion formula. Standard analytic-number-theory texts such as Hardy--Wright and Tenenbaum treat the same material.

The durable delta is only the **line-specific route restriction** obtained by applying that classical algebra to the exact infinite lattice-shift escape left open by `PL-363`. A targeted audit against the nearby programmability findings (`PL-201`--`PL-204`) shows a different mechanism: those findings concern operator-valued prime-edge transports, gauges, and resolvent covariance, whereas (PL364-11) is the direct arithmetic-function classification of the scalar shift filter acting on the coefficient-one zeta vector. The common lesson—unconstrained representations can be programmable—is not claimed as new.

Primary prior-art anchor:

- Encyclopedia of Mathematics, “Dirichlet convolution,” https://encyclopediaofmath.org/wiki/Dirichlet_convolution. It records `(f*g)(n)=sum_{d|n}f(d)g(n/d)`, the convolution ring of arithmetic functions, `\mu` as the inverse of the constant-one function, and the Möbius inversion formula.

No `SOURCES.md` update is needed for this finding: the external ingredient is only the classical Möbius-inversion identity, while the substantive persisted result is the exact line-local application and its falsification consequence.

## 6. Adversarial boundaries

1. **This is a coefficientwise formal action, not a bounded-operator theorem.** For arbitrary `c`, the series `\sum_m c_m S_m` need not converge in operator norm, strongly, weakly, or on any Hilbert-space realization. The claim is only that its action on the formal coefficient-one vector is locally finite coefficient by coefficient.

2. **No analytic continuation follows from programmability.** Equation (PL364-19) requires an independently justified product region or summation theorem. The algebraic inverse does not construct values of zeta or the target Dirichlet series in the critical strip.

3. **Constrained infinite filters remain open.** If `c` is required a priori to lie in a fixed analytic/operator class, `c=\mu*b` may fail that class for most targets. Precisely such failure could create useful rigidity and is the natural next question.

4. **Scale dependence is not classified.** A family `c^{(X)}` whose law depends canonically on a cutoff, boundary condition, renormalization scale, or completed functional equation is not reduced to a single unconstrained arithmetic function by this argument.

5. **Non-coefficientwise maps are outside scope.** Integral transforms, quotient geometries, operator compressions, or other mechanisms that mix exponent-lattice coefficients in a way not represented by convolution with one arithmetic function are not addressed.

6. **Programming a target is not explaining it.** If a filter is constructed from a desired zero set or from the analytically continued zeta function, the resulting zero agreement is circular unless an independent source law forces the same filter.

## Research consequence

The immediate infinite-support extension of `PL-363` is now classified at the algebraic level. Fixed finite signed filters are rigid enough to force periodic coefficients but too weak to select the critical line; completely unrestricted fixed infinite signed filters have the opposite defect—they are so flexible that Möbius inversion programs every coefficient sequence.

Therefore the next viable continuation/readout mechanism cannot be justified merely by allowing infinitely many signed prime-lattice shifts. It must specify an **independently source-forced admissible class or limiting prescription** and prove that the resulting restriction both survives completion and retains a zero-sensitive destination theorem. The mathematically live question is no longer whether infinite signs can cross the positive cone, but which canonical restriction on those signs prevents the Möbius-convolution programmability proved here.