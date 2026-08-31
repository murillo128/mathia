# WP-072 — Base-point local Dirichlet energy regularizes the Mangoldt anchor positively, but is not a global Weil form

## Claim

Let

\[
F_n(z)=\Log \Phi_n(z)
=-\sum_{m\ge1}\frac{c_n(m)}m z^m,
\qquad n>1,
\]

be the Prime-Circle cyclotomic shell functions from `PC-075`, with the branch normalized by `F_n(0)=0`. On their finite linear span define the boundary-point local Dirichlet form at the distinguished base point `1` by

\[
D_1(F)
:=
\left\|
\frac{F(z)-F(1)}{z-1}
\right\|_{H^2}^2.
\]

Then:

1. every canonical shell `F_n`, `n>1`, has finite `D_1` energy;
2. `D_1` is positive definite on the shell span;
3. the exact arithmetic anchor
   \[
   L(F_n)=F_n(1)=\log \Phi_n(1)=\Lambda(n)
   \]
   is a bounded linear functional for this positive geometry, with
   \[
   |F(1)|^2\le D_1(F);
   \]
4. in the ambient zero-at-origin local Dirichlet space, the monomial `z` is a finite-energy representer of boundary evaluation, so
   \[
   D_1(F-z)=D_1(F)-2\Re F(1)+1\ge0;
   \]
5. the mandatory full-root controls from `WP-068`/`WP-069` are not an approximate null sequence for this metric: for
   \[
   F_N(z)=\log\frac{1-z^N}{1-z},
   \]
   one has the elementary lower bound
   \[
   D_1(F_N)\ge \left\lfloor \frac{N}{e^2}\right\rfloor
   \]
   for all sufficiently large `N`, hence
   \[
   D_1\!\left(\frac{F_N}{\log N}\right)\to\infty.
   \]

Thus the obstruction of `WP-071` is sharp in an important sense: once the **metric itself** is allowed to privilege the Mathia base point, there is a natural positive scalar topology in which all cyclotomic shells survive and the exact Mangoldt boundary functional becomes bounded. This is a genuine finite-place positive survivor.

It is **not** a solution of global Weil positivity. Local Dirichlet positivity is classical and universal; this construction does not intrinsically generate the critical `n^{-1/2}` attenuation, the Weil autocorrelation pairing, the archimedean Gamma term, or the polar/global counterterms.

**Evidence status:** `EXACT-DERIVED + POSITIVE-SURVIVOR + CLASSICAL-LOCAL-DIRICHLET + MATHIA-SPECIALIZATION`.

## 1. Why the endpoint form is intrinsic enough to test

`WP-068` rewrites the canonical Hardy-shell Gram energy in terms of the local difference-quotient family

\[
Q_H(B)=\int_0^1 D_t(F_B)\,dt,
\qquad
D_t(F)=
\left\|
\frac{F(z)-F(t)}{z-t}
\right\|_{H^2}^2.
\]

The present form is the boundary endpoint of that same family:

\[
D_1(F)=\left\|T_1F\right\|_{H^2}^2,
\qquad
T_1F(z):=\frac{F(z)-F(1)}{z-1}.
\]

The point `1` is not selected after seeing a desired coefficient. It is already the distinguished base-shell point: `Phi_1(z)=z-1` vanishes there, while every non-base shell `Phi_n`, `n>1`, is regular there. The exact Prime-Circle resultant identity used in `WP-067` and `WP-071` is precisely

\[
F_n(1)=\log\Phi_n(1)=\Lambda(n).
\]

So `D_1` is the minimal pointed endpoint response suggested jointly by the existing Hardy decomposition and the already-canonical base-shell anchor. It deliberately breaks rotation invariance in the metric, as `WP-071` proved any successful scalar-positive boundary completion must do.

## 2. Every cyclotomic shell has finite `D_1` energy

For fixed `n>1`, the Ramanujan sums `c_n(m)` are periodic modulo `n` and have mean zero over one period. The latter follows directly from

\[
c_n(m)=\sum_{\substack{a\bmod n\\(a,n)=1}}e^{2\pi i am/n}:
\]

summing over one complete period in `m` makes every inner geometric sum vanish. Hence the partial sums

\[
C_n(M):=\sum_{m\le M}c_n(m)
\]

are uniformly bounded in `M` for fixed `n`.

Write

\[
F_n(z)=\sum_{m\ge1}b_mz^m,
\qquad b_m=-\frac{c_n(m)}m,
\qquad S:=F_n(1).
\]

If

\[
T_1F_n(z)=\sum_{k\ge0}q_kz^k,
\]

coefficient comparison in `(z-1)T_1F_n=F_n-F_n(1)` gives

\[
q_k=S-\sum_{m=1}^k b_m
=\sum_{m>k}b_m
=-\sum_{m>k}\frac{c_n(m)}m.
\]

Summation by parts with bounded `C_n(M)` gives

\[
q_k=O_n(k^{-1}).
\]

Therefore

\[
D_1(F_n)=\sum_{k\ge0}|q_k|^2<\infty.
\]

Finite shell combinations inherit this property by linearity. This also addresses the main boundary-domain objection: although `F_n` has logarithmic boundary singularities at primitive `n`th roots, those roots are separated from `1`, and the exact coefficient tails prove finite local energy at the base point.

## 3. The exact Mangoldt anchor becomes a bounded positive-energy observable

Every finite shell combination satisfies `F(0)=0`. Evaluating the difference quotient at zero gives

\[
(T_1F)(0)
=
\frac{F(0)-F(1)}{-1}
=F(1).
\]

Hardy evaluation at zero is contractive, so

\[
\boxed{
|L(F)|^2=|F(1)|^2
=|(T_1F)(0)|^2
\le \|T_1F\|_{H^2}^2
=D_1(F).
}
\]

Thus the exact arithmetic functional that was unbounded for the rotation-invariant Hardy geometry in `WP-068` is bounded for the pointed endpoint geometry.

There is also an explicit ambient representer. Since

\[
T_1z=1,
\qquad D_1(z)=1,
\]

we have, for the sesquilinear form induced by `D_1`,

\[
\langle z,F\rangle_{D_1}
=
\langle 1,T_1F\rangle_{H^2}
=F(1).
\]

Consequently

\[
\boxed{
D_1(F-z)
=D_1(F)-2\Re F(1)+1
\ge0.
}
\]

On each shell generator the cross term is exactly `Lambda(n)`. No zero data, zeta continuation, Möbius projection, fitted prime-power kernel, or RH assumption enters this square.

Strictly, if one completes only the shell span rather than the whole zero-at-origin local Dirichlet space, its Riesz vector is the orthogonal projection of `z` to that closed shell subspace. The boundedness and all shell pairings above are unchanged.

Finally, `D_1` is positive definite on the shell span: `D_1(F)=0` implies `T_1F=0`, hence `F` is constant; since `F(0)=0`, necessarily `F=0`.

## 4. The `WP-069` full-root control is strongly detected

For the cumulative full-root shell used in `WP-068`,

\[
F_N(z)
=
\sum_{\substack{d\mid N\\d>1}}F_d(z)
=
\log\frac{1-z^N}{1-z},
\qquad F_N(1)=\log N.
\]

Its Taylor coefficients are

\[
b_N(m)=\frac{1-N\mathbf 1_{N\mid m}}m.
\]

Hence the coefficients of `T_1F_N` are exactly

\[
q_k
=
\log N-\sum_{m=1}^k b_N(m)
=
\log N-H_k+H_{\lfloor k/N\rfloor},
\]

with `H_0=0`. For

\[
1\le k\le \left\lfloor\frac{N}{e^2}\right\rfloor
\]

we have `k<N`, so `H_{floor(k/N)}=0`, and the elementary bound

\[
H_k\le1+\log k
\]

gives

\[
q_k
\ge
\log N-1-\log(N/e^2)
=1.
\]

Therefore

\[
\boxed{
D_1(F_N)
=\sum_{k\ge0}|q_k|^2
\ge
\left\lfloor\frac{N}{e^2}\right\rfloor.
}
\]

For the normalized controls `Y_N=F_N/log N`, which satisfy `Y_N(1)=1`,

\[
D_1(Y_N)
\ge
\frac{\lfloor N/e^2\rfloor}{(\log N)^2}
\longrightarrow\infty.
\]

This is the opposite of the failure in `WP-068` and `WP-070`, where the same normalized arithmetic discriminator had energy tending to zero. The endpoint metric changes the finite topology by far more than the order-one amount that `WP-069` proved was necessary.

## 5. Adversarial controls: why this is not Weil positivity

The construction survives the immediate falsification tests, but it also exposes its own limitation.

### Universal point-energy control

For **any** analytic `F` with `F(0)=0` and finite `D_1`, not just a cyclotomic shell,

\[
|F(1)|^2\le D_1(F).
\]

Thus the sign theorem is universal local Dirichlet geometry. Arithmetic enters through the special Mathia identity `F_n(1)=Lambda(n)`, not through the positivity theorem itself. A non-arithmetic family with the same boundary regularity enjoys the same sign.

### No critical attenuation

The shell readout is `Lambda(n)`. Nothing in `D_1` forces

\[
\frac{\Lambda(n)}{\sqrt n}.
\]

Rescaling shell states by `n^{-1/2}` would insert the critical scale by hand unless an additional intrinsic construction forced that rescaling.

### No Weil autocorrelation channel

The square above controls a linear boundary functional. It does not produce the translation/autocorrelation structure of the finite part of Weil's quadratic form. `WP-005` therefore still applies once one asks for the actual finite Weil convolution geometry.

### No archimedean or polar sector

There is no Gamma-factor term, pole contribution, or global counterterm in `D_1`. In particular, the construction does not answer the line's central requirement that one structure generate both finite-prime and archimedean/global contributions before the sign theorem is invoked.

Accordingly this finding must not be promoted to an RH criterion or a global Weil form. It only establishes that **bounded positive realization of the exact finite Mangoldt anchor is possible inside a Mathia-native pointed shell topology**.

## 6. Relation to `WP-067`–`WP-071`

The result materially changes the scalar-positive frontier without contradicting the previous no-go chain.

- `WP-067` found the formal positive Hardy completion but its canonical finite part was indefinite.
- `WP-068` proved the exact Mangoldt anchor is unbounded in the integrated Hardy metric using full-root controls.
- `WP-069` upgraded that sequence to a topology obstruction: any successful positive extension must assign non-vanishing energy to those controls.
- `WP-070` showed the canonical `q=2` antipodal positive correction still misses them.
- `WP-071` ruled out every positive **rotation-invariant** scalar Hilbert completion with bounded evaluation at `1`, and explicitly left a genuinely pointed/non-homogeneous metric as an escape route.

`D_1` realizes exactly that escape route. It retains all cyclotomic shells, bounds the exact arithmetic anchor, and sends the mandatory normalized controls to infinite rather than zero energy. The remaining obstruction is no longer the existence of a finite positive scalar topology; it is the absence of a canonical **global finite–archimedean coupling** that turns this topology into the Weil form.

## 7. Prior art and novelty audit

The local Dirichlet integral and its difference-quotient/Douglas formula are classical. A primary anchor is:

- Stefan Richter and Carl Sundberg, *A formula for the local Dirichlet integral*, Michigan Math. J. **38** (1991), no. 3, 355–379, DOI `10.1307/mmj/1029004388`.

Modern local-Dirichlet literature likewise treats

\[
D_\zeta(f)
=
\left\|
\frac{f-f(\zeta)}{z-\zeta}
\right\|_{H^2}^2
\]

as standard boundary-point function-space geometry. No novelty is claimed for that theorem, for Hardy evaluation at zero, or for the abstract positivity of a squared norm.

The Mathia-specific derived content is the exact synthesis of three already-intrinsic Prime-Circle facts:

1. the Hardy shell energy decomposes through local difference-quotient energies (`WP-068`);
2. the base endpoint `1` is the exact cyclotomic Mangoldt anchor (`PC-080`, `WP-067`);
3. at that endpoint the full-root sequence that kills the rotation-invariant candidates is instead detected with at least linear energy.

Searches by the structural combinations “cyclotomic logarithm + local Dirichlet”, “Ramanujan sum + local Dirichlet”, and “von Mangoldt + local Dirichlet + cyclotomic” did not locate an external theorem asserting this Prime-Circle specialization. That absence is not used as a novelty claim: the status remains `MATHIA-SPECIALIZATION`, with the function-space mechanism explicitly classical.

This route is also distinct from the prior-art classes excluded by the research mandate: no zeros define a spectrum, no Weil kernel is inserted, no RH-equivalent positivity criterion is assumed, and no regularization constant is fitted. Conversely it does **not** yet supply the missing cohomological/intersection/global structure that those mature approaches address.

## 8. Exact audit and falsification surface

The finding can be refuted by any of the following exact failures:

1. a non-base shell `F_n` for which the quotient `(F_n-F_n(1))/(z-1)` is not in `H^2`;
2. failure of the tail-coefficient identity
   \[
   q_k=-\sum_{m>k}c_n(m)/m;
   \]
3. failure of the boundary-anchor inequality `|F(1)|^2 <= D_1(F)` on the zero-at-origin shell span;
4. failure of
   \[
   q_k=\log N-H_k+H_{\lfloor k/N\rfloor}
   \]
   for the full-root controls;
5. an external result showing that the Mathia-specific synthesis above is already a standard arithmetic Dirichlet-space construction, in which case the claim should be classicalized but the exact mathematical facts remain valid.

The claim deliberately does **not** include a global completion. Any proposed continuation from this finite survivor must independently derive the critical attenuation, Weil autocorrelation, Gamma term, and polar/global terms from one coupled construction and must re-run the matched controls before claiming a global positivity mechanism.

## Research consequence

`WP-071` should no longer be read as evidence that scalar positive shell topology itself is exhausted. The viable scalar branch is narrower and more concrete:

\[
\boxed{
\text{Prime-Circle base endpoint}
\;\longrightarrow\;
D_1\ge0
\;\longrightarrow\;
\text{bounded exact }\Lambda\text{ anchor}
}
\]

is available without zero data and passes the mandatory full-root discriminator. What remains is the hard part required by the canonical mandate: a Mathia-native operation that couples this pointed finite geometry to the archimedean/global sector **before** positivity, while also forcing the `1/2` scale and the Weil autocorrelation structure rather than inserting them.

## Dependencies

- `research/prime_circle/findings/PC-075-cyclotomic-log-hankel-core-is-universal-hilbert-channels.md`
- `PC-080` — exact Hardy-shell resultant/Mangoldt anchor
- `research/weil_positivity/findings/WP-067-base-shell-hardy-canonical-zero-finite-part-is-indefinite.md`
- `research/weil_positivity/findings/WP-068-full-root-hardy-differences-make-mangoldt-anchor-functional-unbounded.md`
- `research/weil_positivity/findings/WP-069-positive-hardy-extensions-cannot-carry-unbounded-mangoldt-anchor-at-finite-energy.md`
- `research/weil_positivity/findings/WP-070-q2-antipodal-hardy-correction-is-blind-to-odd-full-root-controls.md`
- `research/weil_positivity/findings/WP-071-rotation-invariant-hilbert-completions-cannot-bound-mangoldt-boundary-anchor.md`
