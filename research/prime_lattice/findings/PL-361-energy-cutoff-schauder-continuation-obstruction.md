# PL-361 — Canonical energy-cutoff convergence forbids continuous zeta evaluation across `Re(s)=1`

**Evidence:** `EXACT-DERIVED + CLASSICAL-SCHAUDER-BASIS + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-360`.

**Status:** `NONDIAGONAL-COEFFICIENT-GRAMS-STILL-FAIL-IF-CANONICAL-ZETA-PARTIAL-SUMS-CONVERGE + CRITICAL-STRIP-CONTINUATION-REQUIRES-NONCANONICAL-SUMMATION-OR-NONCONTINUOUS-EVALUATION`.

## Precise claim

`PL-360` rules out every **diagonal** coefficient Hilbert norm that simultaneously contains the coefficient-one zeta vector and makes ordinary point evaluation bounded in the critical strip. The obvious remaining escape is to introduce non-diagonal correlations between exponent-lattice basis vectors. Those correlations do not help if the resulting topology still treats the ordinary zeta Dirichlet polynomials as the canonical norm-convergent expansion of the zeta vector.

Let `X` be any Hausdorff topological vector-space completion of the Dirichlet polynomials, and for `N>=1` put

\[
Z_N(s):=\sum_{n\le N}n^{-s}.
\tag{PL361-1}
\]

Fix `s_0 in C`. Assume that polynomial evaluation

\[
\delta_{s_0}\!\left(\sum_{n\le M}a_n n^{-s}\right)
:=\sum_{n\le M}a_n n^{-s_0}
\tag{PL361-2}
\]

extends to a continuous linear functional on `X`. If

\[
Z_N\longrightarrow Z\qquad\text{in }X,
\tag{PL361-3}
\]

then continuity forces

\[
\sum_{n\le N}n^{-s_0}
=\delta_{s_0}(Z_N)
\longrightarrow
\delta_{s_0}(Z).
\tag{PL361-4}
\]

But the ordinary Dirichlet series `sum n^(-s_0)` converges exactly for `Re(s_0)>1`. Hence

\[
\boxed{
Z_N\to Z\text{ in }X
\quad\Longrightarrow\quad
\delta_s\text{ cannot be continuous on }X
\text{ for any }\Re s\le1.
}
\tag{PL361-5}
\]

No Hilbert-space structure, diagonal metric, positivity, or orthogonality is used. The obstruction is purely topological: **a continuous functional must preserve the limit of the same approximating sequence**.

A useful basis corollary is immediate. Suppose `X` is a Banach or Hilbert completion in which the Dirichlet monomials

\[
e_n(s)=n^{-s}
\tag{PL361-6}
\]

ordered by increasing `n` (equivalently increasing prime-lattice energy `log n`) form a Schauder basis. If an element `Z in X` has canonical basis coefficients

\[
Z\sim\sum_{n\ge1} e_n,
\tag{PL361-7}
\]

then the defining Schauder-basis property gives `Z_N->Z` in `X`. Therefore the bounded point-evaluation domain of such a space cannot meet `Re(s)<=1`.

Thus the non-diagonal escape left open by `PL-360` is much narrower than “choose a non-diagonal Gram matrix.” Any coefficient Hilbert geometry for which the exponent-lattice monomials remain a Schauder basis—and in particular any unconditional or Riesz-basis geometry—still cannot realize analytic continuation of the coefficient-one zeta vector by continuous ordinary evaluation in the critical strip.

## 1. The scalar obstruction is the abscissa of ordinary convergence

For completeness, the scalar convergence boundary in (PL361-5) does not use RH or the functional equation. Write

\[
S_N(s)=\sum_{n\le N}n^{-s}.
\]

For fixed `s=sigma+it` with `sigma>0` and `s!=1`, Euler summation gives

\[
S_N(s)
=\frac{N^{1-s}}{1-s}+C_s+O_s(N^{-\sigma}),
\tag{PL361-8}
\]

for a constant `C_s`. If `0<sigma<1`, the first term has magnitude comparable to `N^(1-sigma)` and therefore diverges. If `sigma=1` and `t!=0`, the term `N^(-it)/(1-s)` has no limit while the remainder tends to zero. At `s=1`, `S_N(1)=log N+O(1)`. For `sigma<=0`, the summands `n^{-s}` do not even tend to zero in modulus. Hence the ordinary zeta Dirichlet series has convergence half-plane exactly `Re(s)>1`.

Equation (PL361-4) therefore cannot be repaired by cancellations hidden in a non-diagonal norm: once the **same raw energy cutoffs** converge in the ambient topology and evaluation is continuous, their scalar evaluations have to converge in the ordinary sense.

## 2. Prime-lattice formulation

Let

\[
H e_n=(\log n)e_n
\tag{PL361-9}
\]

be the canonical prime-lattice energy operator. In exponent coordinates,

\[
\log n=\langle v(n),(\log p)_p\rangle.
\tag{PL361-10}
\]

The polynomial `Z_N` is exactly the coefficient-one vector truncated by the spectral/energy region

\[
\{v(n):\langle v(n),\log p\rangle\le\log N\}.
\tag{PL361-11}
\]

Thus (PL361-5) can be read as an obstruction to a very natural completion principle:

\[
\boxed{
\text{strong convergence of the canonical }H\text{-energy cutoffs of zeta}
+
\text{continuous ordinary evaluation}
\Longrightarrow
\Re s>1.
}
\tag{PL361-12}
\]

The issue is not that a particular Gram kernel is too weak. It is that the canonical positive-cone truncation itself carries the original abscissa of convergence into every topology in which those truncations converge and evaluation remains continuous.

This also shows why merely correlating nearby exponent vectors, prime directions, divisor classes, or energy shells is insufficient unless those correlations change a load-bearing convergence mechanism. If the canonical projections still reconstruct the coefficient-one vector, the scalar wall at `Re(s)=1` survives unchanged.

## 3. Continuous analytic realization is equally impossible

There is a function-space version that removes point evaluation from the assumptions. Let `Omega` be a domain and suppose

\[
J:X\longrightarrow \operatorname{Hol}(\Omega)
\tag{PL361-13}
\]

is continuous for the compact-open topology and agrees with the ordinary Dirichlet-polynomial realization on the dense polynomial subspace. If `Z_N->Z` in `X`, then

\[
JZ_N\longrightarrow JZ
\quad\text{locally uniformly on }\Omega.
\tag{PL361-14}
\]

Consequently `Z_N(s)` converges for every `s in Omega`. Therefore no such continuous realization can have

\[
\Omega\cap\{\Re s\le1\}\ne\varnothing.
\tag{PL361-15}
\]

So a non-diagonal coefficient completion cannot obtain the zeta continuation merely by embedding its canonical coefficient-one basis sum continuously into a holomorphic function space across the absolute/ordinary convergence wall.

## 4. What escapes the obstruction

The hypotheses identify exactly what must change. Analytic continuation may still be represented if at least one of the following fails:

- the raw energy cutoffs `Z_N` converge to the completed zeta object;
- ordinary point evaluation is continuous in the completion topology;
- the zeta object is the coefficient-one Schauder expansion of the monomials;
- the realization into holomorphic functions is continuous and agrees with polynomial evaluation term by term.

These are genuine possibilities, not semantic loopholes. Classical continuation already replaces raw partial sums by additional structure: Euler--Maclaurin subtraction introduces an explicit divergent counterterm; Abel/Riesz-type summation changes the approximating family; the functional equation imports a second global representation; Nyman/model-space formulations place zeta in a target-relative Hardy geometry rather than as the norm limit of its coefficient-one Dirichlet truncations. Rigged or distributional pairings can also make the continuation value an unbounded functional.

Therefore (PL361-5) does **not** say that a useful non-diagonal completion is impossible. It says that useful non-diagonal correlations must do more than alter the metric while leaving the canonical basis expansion and bounded evaluation mechanism intact.

## 5. Prior-art and novelty audit

The implication “topological convergence plus continuous evaluation implies scalar convergence” is elementary functional analysis, and the Schauder-basis corollary is built into the definition of a Schauder basis. No theorem-level novelty is claimed. The standard Dirichlet Hardy space in source 1 of `research/prime_lattice/SOURCES.md` is the canonical orthogonal-basis example; its coefficient and evaluation behavior is part of the established Bohr/Dirichlet-series framework already audited in `PL-001`, `PL-007`, and `PL-360`.

A targeted literature audit on 18 September 2026 searched Hardy/Banach/Hilbert spaces of Dirichlet series together with Schauder bases, monomial partial sums, bounded point evaluations, non-diagonal coefficient geometries, and Riesz summability. It recovered established spaces in which Dirichlet monomials are Schauder bases and the classical use of smoothed/Riesz means when raw partial sums are not the appropriate convergence mechanism. Nothing located supports a novelty claim for the abstract lemma. The durable content is the **route restriction relative to `PL-360`**: the diagonal Cauchy--Schwarz argument was not the fundamental continuation barrier. Once the coefficient-one zeta vector is required to arise from its canonical energy-cutoff sums, *every* topology with continuous ordinary evaluation inherits the same `Re(s)=1` wall, including non-diagonal Hilbert metrics.

## 6. Adversarial boundaries

1. **The approximation sequence is load-bearing.** An element can belong to a completion without its raw coefficient truncations converging to it. Spaces using Abel, Cesàro, Riesz, or other summability schemes are not excluded merely because they contain a formal coefficient sequence.

2. **Schauder is sufficient, not necessary.** The theorem only needs `Z_N->Z`; the basis corollary is a convenient broad class. Conversely, failure of the monomials to be a Schauder basis does not supply an RH mechanism—it only evades this obstruction.

3. **Continuity is load-bearing.** An unbounded evaluation, boundary-value distribution, renormalized functional, or separately defined analytic continuation can assign values where the raw scalar series diverges without contradicting (PL361-5).

4. **The wall is `Re(s)=1`, not the critical line.** The result explains why a completion cannot cross the first analytic-continuation barrier by ordinary canonical summation. It contains no mechanism selecting `Re(s)=1/2` or localizing zeros.

5. **No prime-specific cancellation is used.** Rational-prime structure enters through the canonical exponent-lattice energy ordering `log n=<v(n),log p>`, but the topological obstruction would hold for any Dirichlet series whose chosen coefficient expansion has a smaller scalar convergence domain than the proposed continuous evaluation domain. This is a matched generic control, not evidence of RH rigidity.

## Research consequence

After `PL-359` and `PL-360`, “use a non-diagonal coefficient Hilbert space” is still too broad to count as a mechanism. A viable candidate must now specify which side of (PL361-12) it changes. In particular, a proposal based only on a positive non-diagonal Gram matrix, while retaining the monomials as a Schauder basis and interpreting zeta as the coefficient-one basis vector, is already impossible before zero localization enters.

The surviving completion problem is therefore sharper: construct a **source-forced, non-diagonal or target-relative continuation topology in which the critical zeta object is recovered by a controlled noncanonical summation/quotient/distributional mechanism**, and then prove that the resulting continuation retains zero-sensitive arithmetic structure rather than merely inserting the known analytic continuation by hand. Any future candidate should state its summation operators, coefficient-recovery law, evaluation/continuation map, and prime-lattice compatibility explicitly; otherwise it has not crossed the gate established here.