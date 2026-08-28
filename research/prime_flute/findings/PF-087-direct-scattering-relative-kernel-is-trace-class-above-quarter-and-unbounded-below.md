# PF-087 — the relative direct-scattering kernel is trace class above `Re s = 1/4` and unbounded below

**Status:** `POSITIVE-CANONICAL-OPERATOR` + `SHARP-FREDHOLM-THRESHOLD` + `STRENGTHENING-OF-PF-086`.

PF-086 proved that the exact/reference direct-scattering kernel

\[
D(s)_{ij}
=
\begin{cases}
(C_{ij}^E)^{-2s}-(C_{ij}^0)^{-2s},&i\neq j,\\
0,&i=j,
\end{cases}
\]

is Hilbert--Schmidt for `Re s>1/4` and not Hilbert--Schmidt for `0<Re s<=1/4`. The proof there stopped at `S_2` and therefore introduced the regularized determinant `det_2`.

There is a stronger conclusion hidden in the same estimates:

\[
\boxed{
D(s)\in \mathcal S_1
\quad\text{for every }\operatorname{Re}s>\frac14,
}
\]

while

\[
\boxed{
D(s)\text{ has no bounded extension on }\ell^2(\text{cusps})
\quad\text{for }0<\operatorname{Re}s\le\frac14.
}
\]

Thus the quarter-plane is not merely a Hilbert--Schmidt transition. It is a sharp jump from an **ordinary trace-class Fredholm regime** directly to **non-boundedness**. In particular, the natural determinant is the ordinary Fredholm determinant

\[
\boxed{
\mathfrak D_{\rm dir}(s)=\det(I+D(s)),
\qquad \operatorname{Re}s>\frac14,
}
\]

not merely a Carleman--Fredholm `det_2`.

This does **not** yet identify the determinant with the physical scattering determinant of the infinite flute. It is still the exact/reference difference of the canonical identity-double-coset/direct-channel part. The full non-direct double-coset remainder remains the spectral gate.

---

## 1. Input from PF-086

Use the exact endpoints

\[
x_n^E=V(p_n)=\pi\cot\frac{\pi}{p_n}
\]

and the projective reference

\[
x_n^0=p_n.
\]

Let

\[
W_n^\bullet
=2\left(\frac1{\Delta_{n-1}^\bullet}+\frac1{\Delta_n^\bullet}\right),
\qquad
\Delta_n^\bullet=x_{n+1}^\bullet-x_n^\bullet,
\]

and

\[
C_{ij}^\bullet
=\sqrt{W_i^\bullet W_j^\bullet}\,|x_j^\bullet-x_i^\bullet|.
\]

After width-one cusp normalization, `(C_ij)^(-2s)` is exactly the Gamma-factor-stripped identity-double-coset contribution to the standard off-diagonal cusp scattering coefficient in the classical finite-cusp formula.

Set

\[
H_n:=\frac1{W_n^0}
=\frac{g_{n-1}g_n}{2(g_{n-1}+g_n)}.
\]

PF-086 established, locally uniformly in `s` on compact subsets of `Re s>0`,

\[
|D(s)_{ij}|
\le
C_K(p_i^{-2}+p_j^{-2})(C_{ij}^0)^{-2\operatorname{Re}s},
\tag{1}
\]

and, for `i<j`, one may absorb the second endpoint defect into the first:

\[
|D(s)_{ij}|
\ll_K p_i^{-2}(C_{ij}^0)^{-2\operatorname{Re}s}.
\tag{2}
\]

Also

\[
(C_{ij}^0)^{-4\sigma}
=H_i^{2\sigma}H_j^{2\sigma}|p_j-p_i|^{-4\sigma},
\tag{3}
\]

and the elementary dyadic estimate

\[
\boxed{
\sum_n H_n^\alpha p_n^{-2\alpha}<\infty
\iff
\alpha>\frac12
}
\tag{4}
\]

holds. Only the convergent direction of (4) is needed for the trace-class proof.

For odd primes,

\[
\frac12\le H_n\le \frac12\min(g_{n-1},g_n)<\frac{p_n}{2},
\tag{5}
\]

where the last inequality follows from Bertrand.

---

## 2. Rowwise `ell^2` summability is itself summable

Let `K` be a compact subset of `Re s>1/4`. Choose

\[
\frac14<\sigma_0<
\min\left(\frac12,\inf_{s\in K}\operatorname{Re}s\right)
\]

and put

\[
\alpha=2\sigma_0\in\left(\frac12,1\right).
\]

Because `C_ij^0>=2`, replacing `Re s` by the smaller exponent `sigma_0` only enlarges the upper bound by a uniform constant.

For each `i`, let

\[
r_i=(D(s)_{ij})_{j>i}
\]

be the strict upper-triangular row. Split it into

```text
near:  p_i < p_j < 2 p_i,
far:   p_j >= 2 p_i.
```

### 2.1 Near part

From (2) and `C_ij^0>=2`,

\[
|D(s)_{ij}|^2\ll_K p_i^{-4}.
\]

There are at most `p_i` possible integer indices/locations in the near interval, so no prime number theorem is needed:

\[
\|r_i^{\rm near}\|_2^2
\ll_K p_i^{-4}\,p_i
=p_i^{-3}.
\]

Hence

\[
\boxed{
\|r_i^{\rm near}\|_2\ll_K p_i^{-3/2}.
}
\tag{6}
\]

### 2.2 Far part

For `p_j>=2p_i`,

\[
p_j-p_i\ge\frac{p_j}{2}.
\]

Using (2)--(4),

\[
\begin{aligned}
\|r_i^{\rm far}\|_2^2
&\ll_K
p_i^{-4}H_i^\alpha
\sum_{p_j\ge2p_i}H_j^\alpha p_j^{-2\alpha}\\
&\le
C_{K,\alpha}\,p_i^{-4}H_i^\alpha.
\end{aligned}
\]

Therefore

\[
\|r_i^{\rm far}\|_2
\ll_K p_i^{-2}H_i^{\alpha/2}
=p_i^{-2}H_i^{\sigma_0}.
\]

By (5),

\[
\boxed{
\|r_i^{\rm far}\|_2
\ll_K p_i^{-2+\sigma_0}
\le p_i^{-3/2}.
}
\tag{7}
\]

The final inequality uses `sigma_0<1/2`.

Combining (6) and (7),

\[
\boxed{
\|r_i\|_2\ll_K p_i^{-3/2}.
}
\tag{8}
\]

Now

\[
\sum_i p_i^{-3/2}
\le
\sum_{n\ge2}n^{-3/2}
<\infty.
\]

Thus

\[
\boxed{
\sum_i\|r_i\|_2<\infty.
}
\tag{9}
\]

This is strictly stronger than the Hilbert--Schmidt estimate

\[
\sum_i\|r_i\|_2^2<\infty.
\]

---

## 3. Nuclear decomposition and trace class

Let `U(s)` denote the strict upper-triangular part of `D(s)`. Row `r_i` defines a rank-one operator with range spanned by the standard basis vector `e_i`. Consequently

\[
U(s)
=
\sum_i e_i\otimes r_i^*,
\]

with nuclear norm estimate

\[
\|U(s)\|_{\mathcal S_1}
\le
\sum_i\|r_i\|_2.
\]

Equation (9) therefore gives

\[
U(s)\in\mathcal S_1.
\]

Since `C_ij=C_ji`, the kernel is symmetric:

\[
D(s)_{ij}=D(s)_{ji}.
\]

Thus

\[
D(s)=U(s)+U(s)^T,
\]

and

\[
\boxed{
D(s)\in\mathcal S_1
\qquad(\operatorname{Re}s>1/4).
}
\tag{10}
\]

The estimate is locally uniform on compact subsets of the quarter-plane. Termwise holomorphy plus the locally uniform nuclear decomposition shows that

\[
s\longmapsto D(s)
\]

is holomorphic as an `S_1`-valued map on `Re s>1/4`.

Hence the ordinary Fredholm determinant

\[
\boxed{
\mathfrak D_{\rm dir}(s)
:=\det(I+D(s))
}
\tag{11}
\]

is holomorphic there.

PF-086's `det_2(I+D)` remains mathematically valid, but it is non-optimal: the operator is already trace class.

---

## 4. Below the quarter-line the matrix is not even bounded

PF-086 used a fixed row to prove failure of Hilbert--Schmidt. The same observation is stronger.

Fix one cusp `i`. Since `V'(x)>1`, every exact prime gap is larger than its projective-reference gap, hence

\[
W_i^E<W_i^0.
\]

For `j->infinity`,

\[
D_V(p_i,p_j)\to1,
\qquad
W_j^E/W_j^0\to1,
\]

so

\[
\frac{C_{ij}^E}{C_{ij}^0}
\longrightarrow
r_i:=\sqrt{W_i^E/W_i^0}
\in(0,1).
\tag{12}
\]

For any fixed `s` with `Re s>0`,

\[
r_i^{-2s}-1\neq0,
\]

because its modulus cannot equal zero when `|r_i^{-2s}|=r_i^{-2\operatorname{Re}s}>1`.

Therefore

\[
|D(s)_{ij}|
\asymp_{i,s}
(C_{ij}^0)^{-2\operatorname{Re}s}
\]

along the far tail. Since `H_j>=1/2` and `p_j-p_i<=p_j`, (3) gives

\[
|D(s)_{ij}|^2
\gtrsim_{i,s}
p_j^{-4\operatorname{Re}s}.
\tag{13}
\]

Hence, if

\[
0<\operatorname{Re}s\le\frac14,
\]

then

\[
\sum_j|D(s)_{ij}|^2=\infty,
\]

using the divergence of the prime Dirichlet series at exponent `<=1` (Euler at the boundary).

But if a matrix defines a bounded operator

\[
T:\ell^2\to\ell^2,
\]

every row must belong to `ell^2`: the `i`-th row is the coefficient vector of `T^*e_i`.

Therefore

\[
\boxed{
D(s)\text{ has no bounded extension on }\ell^2
\qquad
(0<\operatorname{Re}s\le1/4).
}
\tag{14}
\]

Combining (10) and (14), the transition is sharp and has no intermediate bounded non-trace-class phase:

\[
\boxed{
\begin{array}{ll}
\operatorname{Re}s>1/4:&D(s)\in\mathcal S_1,\\[1mm]
0<\operatorname{Re}s\le1/4:&D(s)\text{ is not bounded on }\ell^2.
\end{array}}
\tag{15}
\]

---

## 5. The quarter threshold now belongs to an ordinary Fredholm determinant

Because `D(s)` has zero diagonal and is trace class,

\[
\operatorname{tr}D(s)=0.
\]

In a right half-plane where `||D(s)||<1`, the standard determinant expansion begins at a genuine two-channel round trip:

\[
\log\det(I+D(s))
=-\frac12\operatorname{tr}D(s)^2
+\frac13\operatorname{tr}D(s)^3-\cdots.
\tag{16}
\]

For real `s>1/4`,

\[
\operatorname{tr}D(s)^2
=
\sum_{i\ne j}D(s)_{ij}^2.
\]

Thus the first nonzero Fredholm cycle already sees the same squared direct-scattering amplitudes that produced the quarter threshold in PF-086.

For long channels,

\[
(C_{ij}^0)^{-4s}
=
(H_iH_j)^{2s}|p_j-p_i|^{-4s}.
\tag{17}
\]

Compare this with a long block separator whose tangent length satisfies schematically

\[
e^{-sL_{ij}}
\asymp
(X_iZ_j)^{2s}|p_j-p_i|^{-4s}.
\tag{18}
\]

Equations (17)--(18) explain why PF-084 and PF-086/PF-087 encounter the same quarter-plane wall by distinct constructions: both are based on two endpoint weights propagated across an arbitrarily long block, but the scattering determinant uses the canonical harmonic cusp weights `H_i,H_j` rather than the outer-gap weights of the separator.

This is a structural relation, not an equality of the two determinants.

---

## 6. Relation to the distinguished cuffs

The harmonic cusp scale is

\[
H_n
=\frac{g_{n-1}g_n}{2(g_{n-1}+g_n)}.
\]

Using the distinguished-cuff asymptotic

\[
\ell_n
=2\log\frac{4p_n}{g_{n-1}}+o(1),
\]

the two neighboring gaps entering `H_n` are exponential functions of neighboring cuff scales. Thus a long direct channel carries

```text
left local cuff pair
        +
right local cuff pair
        +
long cusp separation.
```

The trace/Fredholm operation then closes such channels into cycles. This is qualitatively different from a cuff-by-cuff Euler product and from the Grunsky completion of PF-085.

---

## 7. Interior/exterior duality

Everything entering `D(s)` is invariant under the ambient inversion exchanging the two orthogonal-circle realizations:

1. primitive cusp width is normalized to one;
2. the lower-left modulus of the corresponding normalized direct double coset is unchanged by conjugacy/relabeling;
3. the exact/reference comparison is made after the same projective normalization.

Hence the exterior surface produces the same operator up to unitary permutation of the cusp basis. The Fredholm determinant (11) is therefore duality-preserving rather than attached to only one ambient realization.

---

## 8. Novelty / prior-art audit

The functional-analytic ingredients are standard:

- an operator whose rows admit a nuclear rank-one decomposition with summable row `ell^2` norms is trace class;
- ordinary Fredholm determinants are holomorphic for holomorphic trace-class families;
- finite-cusp hyperbolic scattering coefficients have the classical double-coset Dirichlet expansion.

The relevant geometric/spectral literature found in the audit does **not** already provide (15):

1. Standard Selberg/scattering theory treats finite-area or geometrically finite surfaces, hence finitely many cusp channels.
2. Pohl--Wabnitz, *Selberg zeta functions, cuspidal accelerations, and existence of strict transfer operator approaches* (Memoirs AMS, 2026), constructs nuclear transfer operators for geometrically finite noncompact hyperbolic orbisurfaces. This does not cover an infinitely generated tight flute with countably many cusps and non-discrete primitive length spectrum.
3. Liu--Wang, *Cusps, Kleinian groups, and Eisenstein series* (Forum Math. Sigma, 2023), explicitly treats general Kleinian groups and discusses examples with infinitely many cusps. Its Eisenstein construction is controlled by Poincare-series convergence and is aimed at Eisenstein cohomology/intertwining; it does not construct a countable cusp scattering Fredholm determinant or a Schatten threshold of this type.
4. The existing infinite-area Selberg-zeta literature located in the audit is convex-cocompact/geometrically finite and relies on finite symbolic/cross-section structure.

No source located in targeted searches contains the exact/reference prime-circle kernel

\[
(C_{ij}^E)^{-2s}-(C_{ij}^0)^{-2s}
\]

on countably many width-normalized cusp channels, nor the sharp dichotomy

\[
\mathcal S_1\quad\text{for }\operatorname{Re}s>1/4
\qquad\text{vs}\qquad
\text{unbounded for }0<\operatorname{Re}s\le1/4.
\]

Accordingly the novelty claim should remain narrow: **the prime-derived direct relative scattering operator has a sharp trace-class/Fredholm threshold at one quarter.** Trace-class theory, cusp scattering, and prime Dirichlet divergence are of course standard separately.

Literature anchors:

- Anke Pohl and Paul Wabnitz, *Selberg zeta functions, cuspidal accelerations, and existence of strict transfer operator approaches*, Memoirs AMS (2026), DOI 10.1090/memo/1616.
- Hongbin Liu and Shi Wang, *Cusps, Kleinian groups, and Eisenstein series*, Forum of Mathematics, Sigma (2023), https://doi.org/10.1017/fms.2023.11 .
- Classical finite-area cusp scattering / Eisenstein theory for the double-coset expansion.

---

## 9. What this does and does not establish

### Established

\[
\boxed{
D(s)\in\mathcal S_1
\iff_{\text{within }\operatorname{Re}s>0}
\operatorname{Re}s>\frac14,
}
\]

where below/equal to the boundary the statement is actually stronger: the coefficient matrix has no bounded `ell^2` realization.

Therefore an ordinary canonical Fredholm determinant exists:

\[
\boxed{
\mathfrak D_{\rm dir}(s)=\det(I+D(s)),
\qquad\operatorname{Re}s>\frac14.
}
\]

### Not established

The zeros of this determinant are **not** presently Laplace eigenvalues or resonances. `D(s)` contains only the distinguished identity-double-coset contribution from each pair of cusp channels.

The remaining decisive gate is still the full relative physical scattering operator. If one can decompose, after a mathematically justified analytic continuation,

\[
\Phi_E(s)-\Phi_0(s)=A(s)D(s)+R(s),
\]

then one must determine whether `R(s)` is trace class (or at least a controlled relative perturbation) in any domain reaching `Re s>1/4`.

A direct termwise double-coset argument is unlikely to suffice below the ordinary Poincare/Eisenstein convergence half-plane; analytic continuation or a resolvent/NtD construction would be required.

---

## 10. Next decisive test

The most useful next branch is no longer to improve the operator ideal of the direct kernel: it is already trace class at the optimal boundedness threshold.

The next test should instead compare finite truncations of the **full** physical scattering matrices for the exact and projective flutes, subtract the direct kernel, and ask whether the remainder has a uniform trace-class estimate as the number of pants/cusps tends to infinity.

A positive result would promote (11) toward a genuine relative scattering determinant. A negative result would isolate the non-direct dynamical proliferation as the exact obstruction.
