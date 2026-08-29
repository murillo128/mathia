# WP-009 — Prime-Lattice Weil weights do not define a passive jump Dirichlet form; the global Lévy completion is RH-equivalent

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct passive jump/Dirichlet-energy route.

## Claim

`WP-004` constructs the exact positive Prime-Lattice axis measure

\[
\mu_{1/2}
=
\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n},
\tag{1}
\]

and `WP-005` shows that the finite Weil quadratic term is obtained by using those same atoms as translation shifts. A natural surviving geometric idea is therefore to interpret every prime-power atom as a **positive conductance / jump rate** and use the canonical translation-invariant Dirichlet energy

\[
\mathcal E_{\rm axis}(f)
=
\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
\|f-\tau_{\log n}f\|_2^2,
\qquad
(\tau_a f)(x)=f(x-a).
\tag{2}
\]

This would be attractive for the Weil-positivity program: nonnegativity is independent of RH, the locations and weights are forced by Prime Lattice, and the construction is the standard energy of a symmetric jump network rather than an inserted zeta-zero spectrum.

The route fails in two exact ways.

First, the critical axis measure (1) is **not a Lévy measure** and (2) is infinite for every nonzero compactly supported Weil test function. The obstruction is at large jumps, not at a delicate singularity near zero:

\[
\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
\ge
\sum_p\frac{\log p}{\sqrt p}
=\infty.
\tag{3}
\]

If `supp(f) subset [-L,L]`, then for every `log n>2L` the supports of `f` and `tau_{log n}f` are disjoint, hence

\[
\|f-\tau_{\log n}f\|_2^2=2\|f\|_2^2.
\tag{4}
\]

Equations (3)--(4) force `E_axis(f)=infinity` for every nonzero compactly supported `f`.

Second, even after finite-window truncation the exact finite Weil form differs from the positive jump energy by a **negative self-energy**. Set

\[
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
a_n=\log n,
\qquad
C_L=\sum_{a_n<2L}w_n,
\tag{5}
\]

and

\[
\mathcal E_L(f)=\sum_{a_n<2L}w_n\|f-\tau_{a_n}f\|_2^2.
\tag{6}
\]

Using the normalization of `WP-005`,

\[
W_{\rm fin}(f)
=-2\sum_{a_n<2L}w_n\operatorname{Re}\langle f,\tau_{a_n}f\rangle,
\tag{7}
\]

so exactly

\[
\boxed{
W_{\rm fin}(f)=\mathcal E_L(f)-2C_L\|f\|_2^2.
}
\tag{8}
\]

Thus making the prime comb into a passive positive jump energy does not explain its Weil sign. It adds a positive diagonal self-term that the explicit formula does not contain, and recovering the exact finite Weil term requires subtracting it. Moreover `C_L -> infinity` as `L -> infinity`. In the standard Beurling--Deny framework a regular symmetric Dirichlet form has positive jump and killing measures; equation (8) would instead require a negative killing/self-energy if no additional structure is introduced.

There is also a sharp prior-art redirect. For `sigma>1`, the classical Riemann zeta distribution is compound Poisson with prime-power Lévy measure

\[
N_\sigma
=
\sum_p\sum_{k\ge1}\frac{p^{-k\sigma}}{k}\,\delta_{k\log p}.
\tag{9}
\]

Differentiating its coefficients gives the exact Prime-Lattice family

\[
-\partial_\sigma N_\sigma
=
\sum_p\sum_{k\ge1}(\log p)p^{-k\sigma}\,\delta_{k\log p}
=:
M_\sigma,
\tag{10}
\]

and therefore

\[
\boxed{\mu_{1/2}=M_{1/2}.}
\tag{11}
\]

So the `WP-004` measure is the critical extrapolation of the parameter derivative of a classical positive compound-Poisson object. But the Lévy condition for (9), and finiteness of (10), hold only in the Euler absolute-convergence half-plane `sigma>1`; at `sigma=1/2` the large-jump mass diverges exactly as in (3).

Finally, a known global completion already tests the idea that the missing archimedean/polar terms might restore a Lévy/Markov positivity theorem. Nakamura and Suzuki construct a completed function `g_zeta(t)` containing the prime-power term together with the global completion and prove

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\exp(g_\zeta(t))
\text{ is the characteristic function of an infinitely divisible distribution.}
}
\tag{12}
\]

Under RH its Lévy measure is

\[
\nu_\zeta
=
\sum_\gamma\frac{m_\gamma}{\gamma^2}\,\delta_{-\gamma},
\tag{13}
\]

supported on the zero ordinates themselves. Hence the known global Lévy--Khintchine completion does not provide an independent geometric positivity theorem: its infinite divisibility is **equivalent to RH**, and under RH the positive jump measure has moved from prime powers to inserted zero data.

Consequently the direct branch

```text
WP-004 prime-power weights
    -> passive translation-invariant jump conductances
    -> Dirichlet / resistor / Markov positivity
    -> add the canonical global completion
    -> Weil positivity
```

is closed. A successful boundary/scattering construction must do more than reinterpret the `WP-004` atoms as passive jump rates. It must introduce a nontrivial compression, quotient, grading, cohomological/intersection structure, or other global operation whose positivity is proved independently and which simultaneously accounts for the required self-energy/counterterms.

## 1. The critical axis measure fails the Lévy integrability condition

For a Lévy measure `nu` on the real line, the Lévy--Khintchine condition requires

\[
\int_{\mathbb R}(1\wedge x^2)\,\nu(dx)<\infty.
\tag{14}
\]

The atoms of (1) lie at `log n >= log 2`, and all atoms with `n>=3` lie at distance greater than one from the origin. Therefore (14) would in particular require finite total mass in the tail.

But the prime terms alone give

\[
\mu_{1/2}([1,\infty))
\ge
\sum_{p\ge3}\frac{\log p}{\sqrt p}.
\]

For `p>=3`, `log p/sqrt(p) >= 1/p`, and Euler's divergence of `sum_p 1/p` yields (3). Thus (1) is not a Lévy measure.

This is not a removable normalization defect. Multiplying all weights by a positive constant leaves divergence unchanged. Compensating the small-jump linear term in Lévy--Khintchine also does not help because the obstruction is infinite mass at **large** jumps, where a Lévy measure must have finite mass.

One could map the distances `log n` to small distances such as `1/n`, but then the translations would no longer be the `log n` shifts forced by the explicit formula and `WP-005`. That is a different functional, not an escape from this obstruction.

## 2. The candidate energy has no nonzero compactly supported Weil tests in its domain

Let `0 != f in C_c^infinity(R)` and choose `L` with `supp(f) subset [-L,L]`. If `a>2L`, then

\[
\operatorname{supp}(f)\cap\operatorname{supp}(\tau_a f)=\varnothing.
\]

Hence

\[
\|f-\tau_a f\|_2^2
=
\|f\|_2^2+\|\tau_a f\|_2^2
=2\|f\|_2^2.
\]

Substituting every prime power with `a_n>2L` into (2) gives

\[
\mathcal E_{\rm axis}(f)
\ge
2\|f\|_2^2
\sum_{a_n>2L}w_n
=\infty.
\tag{15}
\]

So the direct jump energy is not merely unbounded or difficult to close: **every nonzero compactly supported test has infinite energy**. The ordinary Weil seed class cannot be a core for this form.

This supplies an exact geometric-domain obstruction that is distinct from `WP-005`. There the finite prime autocorrelation operator was indefinite. Here the proposed way of converting those same shifts into a manifestly positive Markov/Dirichlet energy fails before positivity can be useful, because its natural domain excludes the test functions on which Weil's criterion is posed.

## 3. Finite truncation exposes the missing diagonal rather than fixing it

For a compact support window `[-L,L]`, only shifts `a_n<2L` affect the autocorrelation term, so (6) is finite and positive. Expanding a summand gives

\[
\|f-\tau_a f\|_2^2
=2\|f\|_2^2-2\operatorname{Re}\langle f,\tau_a f\rangle.
\tag{16}
\]

Summation gives

\[
\mathcal E_L(f)
=2C_L\|f\|_2^2
-2\sum_{a_n<2L}w_n\operatorname{Re}\langle f,\tau_{a_n}f\rangle,
\]

which is exactly (8).

Therefore the positive energy contains a diagonal term

\[
2C_L\|f\|_2^2
\]

that is absent from `W_fin`. Removing it is exactly what restores the indefinite finite-prime form found in `WP-005`.

This mirrors `WP-001` at a different level. In `WP-001`, adding the natural positive diagonal to a single-prime kernel created a `k=0` term absent from Weil, and deleting it restored indefiniteness. Here the same phenomenon occurs after all prime powers have been assembled as translation jumps: passive energy requires a positive diagonal degree/self-energy, while the explicit formula retains the off-diagonal correlations with the opposite sign.

For regular symmetric Markov forms, the Beurling--Deny decomposition does not permit this discrepancy to be hidden as a negative killing rate: the jump and killing measures are nonnegative. This does **not** rule out a Schur complement of a larger indefinite/graded system or a relative construction. It rules out the direct interpretation of the WP-004 weights themselves as passive conductances whose ordinary Dirichlet principle supplies the Weil sign.

## 4. Exact relation to the classical zeta compound-Poisson measure

For `sigma>1`, Euler's product gives

\[
\frac{\zeta(\sigma+it)}{\zeta(\sigma)}
=
\exp\left(
\sum_p\sum_{k\ge1}
\frac{p^{-k\sigma}}{k}
(e^{-itk\log p}-1)
\right),
\tag{17}
\]

up to the harmless sign convention for the random variable `log n` versus `-log n`. This is the characteristic function of the classical Riemann zeta compound-Poisson distribution, with Lévy measure (9).

The coefficient derivative is immediate:

\[
-\partial_\sigma\left(\frac{p^{-k\sigma}}{k}\right)
=(\log p)p^{-k\sigma}.
\]

Hence (10). Its total mass is

\[
M_\sigma(\mathbb R)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n^\sigma}
=-\frac{\zeta'(\sigma)}{\zeta(\sigma)},
\qquad \sigma>1.
\tag{18}
\]

At `sigma=1/2`, (10) is exactly the Prime-Lattice measure (1). Thus there is a clean classical interpretation of the `WP-004` positive weights: they are the formal critical-line continuation of an object that is genuinely a finite jump intensity in the Euler-product region.

But (17) also gives a strong novelty control. Infinite divisibility of the raw Euler product is classical and lives where the Euler product converges absolutely. Extrapolating its positive jump geometry to `sigma=1/2` is not a new geometric mechanism; the required Lévy integrability has already broken before reaching the critical strip.

## 5. The global infinitely-divisible completion is already an RH criterion

Nakamura and Suzuki's 2023 theorem is an even closer prior-art test. Their `g_zeta(t)` is built from the completed Riemann data and includes the same finite primitive

\[
\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}
(|t|-\log n)
\tag{19}
\]

that is adjacent to the Suzuki screw-function route identified in `WP-007`, together with the polar and archimedean terms needed for the completed object.

They prove the equivalence (12). Under RH they derive the Lévy--Khintchine representation

\[
g_\zeta(t)
=
\sum_\gamma m_\gamma\frac{e^{-i\gamma t}-1}{\gamma^2},
\tag{20}
\]

and therefore the atomic zero measure (13).

For the present research line this is a decisive novelty boundary:

- the raw prime-power jump measure is positive but ceases to be a legitimate Lévy measure at the critical weight;
- adding the full known completion can restore an infinitely-divisible interpretation **exactly when RH holds**;
- under that hypothesis the positive Lévy measure is expressed in the zero ordinates, so the sign theorem is not independent of the target statement.

Thus `infinite divisibility`, `conditional negative definiteness`, or `Markov jump positivity` cannot be accepted as the missing mechanism merely because the completed formula can be written in that language. One must prove the relevant positivity from additional geometry before using RH-equivalent identities or zero data.

## 6. Prior art and novelty assessment

No novelty is claimed for:

- Lévy--Khintchine theory or the integrability condition (14);
- Beurling--Deny jump Dirichlet forms;
- the Riemann zeta compound-Poisson distribution for `sigma>1`;
- the Nakamura--Suzuki infinitely-divisible criterion for RH;
- Suzuki's screw-function representation already audited in `WP-007`.

The Mathia-specific contribution is the exact **passive-energy no-go** obtained by combining the intrinsic `WP-004` measure with the `WP-005` translation geometry:

1. the canonical conductance measure fails the Lévy condition at the exact critical weight;
2. the corresponding positive jump energy is infinite on every nonzero compactly supported Weil test;
3. finite truncation differs from the actual finite Weil term by precisely the positive diagonal self-energy (8), whose required subtraction diverges globally;
4. the nearest known global Lévy completion is already RH-equivalent and zero-supported under RH.

This rules out a mathematically natural class of `resistor network / passive jump process / ordinary Dirichlet principle` explanations without claiming anything about more general non-Markovian, graded, compressed, or cohomological constructions.

## 7. Boundary conditions and falsification tests

The exact part of the finding can be falsified by any failure of the following checks:

1. verify from `WP-004` that the jump weights and locations are `w_n=Lambda(n)/sqrt(n)` and `a_n=log n` on prime powers;
2. verify `sum_p log(p)/sqrt(p)=infinity` (Euler's divergence of `sum_p 1/p` already suffices for comparison);
3. for compactly supported nonzero `f`, verify disjointness and equation (4) for all sufficiently large `a_n`;
4. expand (6) and compare with the exact `WP-005` normalization to obtain (8);
5. derive (10) by differentiating the classical compound-Poisson coefficients in (9);
6. verify from Nakamura--Suzuki that infinite divisibility of `exp(g_zeta)` is equivalent to RH and that the RH Lévy measure is (13).

An escape from this finding must change at least one structural ingredient rather than regularize (2) arbitrarily. In particular, a viable construction could use a canonical relative subtraction forced by a larger geometry, a compression/Schur complement, a graded supertrace, or a cohomological/intersection pairing. But it must prove the resulting nonnegativity independently and must explain why the subtraction/counterterm is canonical rather than inserted to reproduce the known explicit formula.

## Consequence for the research line

`WP-004` remains the strongest finite-place success: Prime Lattice intrinsically gives the exact positive Mangoldt weights. `WP-005` showed that the autocorrelation lift makes their finite Weil operator indefinite. `WP-009` now rules out the most direct attempt to recover independent positivity by promoting those shifts to a passive jump-network energy.

The obstruction identifies the missing feature more sharply. **Ordinary passive energy wants the diagonal degree term; Weil's arithmetic term does not.** At the global level, the known Lévy completion that incorporates the missing terms has positivity exactly equivalent to RH. Therefore a successful Mathia geometry must force a nontrivial relative/global cancellation before positivity emerges; simple positive conductances on the logarithmic prime-power graph are not enough.
