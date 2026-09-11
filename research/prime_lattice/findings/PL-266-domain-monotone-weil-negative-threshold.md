# PL-266 — Domain monotonicity makes the localized Weil negativity threshold Galerkin-detectable without uniform convergence

**Evidence:** `LITERATURE+DERIVED`

**Status:** `STRUCTURAL-SHARPENING + CORRECTION`

## Claim

Let

\[
\lambda_a
=
\inf_{0\ne v\in\mathfrak D(Q_W^a)}
\frac{Q_W^a(v)}{\|v\|_2^2}
\]

be the bottom of Suzuki's localized Weil operator on `[-a,a]`. The family is automatically **nonincreasing** in the support radius:

\[
0<a<b\quad\Longrightarrow\quad \lambda_b\le \lambda_a.
\]

This is an immediate variational consequence of Suzuki's Corollary 1.2, which identifies `lambda_a` with the infimum of the *same global Weil quadratic form* over `C_c^infty(-a,a)`: the test classes are nested as `a` grows.

Combine this domain monotonicity with the fixed-radius Laurent-core theorem used in `PL-261`. Write

\[
\mu_N(a)
=
\lambda_{\min}\bigl(Q_W^a|_{E_N(a)}\bigr)
\]

for the nested Connes--Consani finite compressions at radius `a`. Their form-core result gives, for every fixed `a`,

\[
\mu_N(a)\downarrow\lambda_a
\qquad(N\to\infty),
\]

and restriction of the Rayleigh quotient gives

\[
\mu_N(a)\ge\lambda_a.
\]

Assume RH is false and define the onset of strict negativity

\[
a_-:=\inf\{a>0:\lambda_a<0\}<\infty,
\]

and the finite-compression thresholds

\[
a_N:=\inf\{a>0:\mu_N(a)<0\}\in(0,\infty].
\]

Then

\[
\boxed{a_N\downarrow a_-}
\]

(in the extended sense until the finite thresholds become finite). Suzuki's continuity theorem moreover gives

\[
\lambda_{a_-}=0.
\]

Thus **uniform-in-`a` Galerkin convergence is not needed merely to locate the continuum onset of strict Weil negativity**. Pointwise form-core convergence, the variational upper bound, and support-domain monotonicity already prevent threshold drift.

This corrects the stronger residual statement in `PL-265` that a uniform-in-radius estimate is required to track the first crossing. Uniform control remains load-bearing for rates, eigenvector tracking, analytic-transform convergence such as `PL-262`, arbitrary truncation families lacking the same variational/cofinal structure, and for distinguishing the *earliest zero* from the onset of strict negativity if `lambda_a` has a zero plateau.

## 1. The localized ground energy is domain-monotone

Suzuki proves that for every `a>0`,

\[
\lambda_a
=
\inf_{0\ne v\in C_c^\infty(-a,a)}
\frac{Q_W(v)}{\|v\|_2^2}.
\]

The important point is that the numerator here is the global completed Weil form `Q_W`; the localization only restricts the support of the test function. If `0<a<b`, then zero extension gives the literal inclusion

\[
C_c^\infty(-a,a)\subset C_c^\infty(-b,b),
\]

with both `Q_W(v)` and `||v||_2` unchanged. Taking an infimum over the larger class can only lower the Rayleigh quotient, hence

\[
\lambda_b\le\lambda_a.
\]

No Euler product, zero expansion, or differentiability in `a` is used. This is ordinary domain monotonicity of a variational minimum for one fixed quadratic form.

Two immediate consequences are useful. First, once a localized Weil form has a strict negative direction, every larger support radius has one as well. There can be no reentrant return to positive lower bound. Second, because Suzuki proves `lambda_a>0` for all sufficiently small `a` and proves continuity of `a -> lambda_a`, failure of RH produces a finite boundary `a_-` with

\[
\lambda_{a_-}=0,
\qquad
\lambda_a<0\quad(a>a_-).
\]

The last strict inequality follows from the definition of `a_-` together with monotonicity: for every `a>a_-`, some `b<a` already has `lambda_b<0`, and therefore `lambda_a<=lambda_b<0`.

This does **not** prove that `lambda_a>0` for every `a<a_-`. A zero plateau before strict negativity is not excluded by the present argument. Accordingly `a_-` should be called the onset of strict negativity, not unconditionally the earliest degeneracy radius.

## 2. Pointwise Galerkin convergence already pins down that threshold

For each fixed `a`, the Connes--Consani Laurent spaces used in `PL-261` are nested in Galerkin dimension,

\[
E_N(a)\subset E_{N+1}(a),
\]

and their minimum Rayleigh quotients satisfy

\[
\mu_{N+1}(a)\le\mu_N(a),
\qquad
\mu_N(a)\ge\lambda_a,
\qquad
\mu_N(a)\to\lambda_a.
\]

The first inequality implies that `a_N` is nonincreasing in `N`. The second gives the decisive lower bound. If `a<a_-`, then by definition `lambda_a>=0`, so

\[
\mu_N(a)\ge0
\]

for every `N`. Therefore no finite compression can become negative before the continuum threshold:

\[
a_N\ge a_-.
\]

For the opposite inequality, fix `epsilon>0`. Domain monotonicity gives

\[
\lambda_{a_-+\epsilon}<0.
\]

At this *single fixed radius*, pointwise form-core convergence is enough: for all sufficiently large `N`,

\[
\mu_N(a_-+\epsilon)<0.
\]

Hence

\[
a_N\le a_-+\epsilon
\]

for all sufficiently large `N`. Since `epsilon` is arbitrary,

\[
\limsup_{N\to\infty}a_N\le a_-.
\]

Together with `a_N>=a_-`, this proves

\[
a_N\to a_-.
\]

No estimate of

\[
\sup_a|\mu_N(a)-\lambda_a|
\]

is required. The reason is order-theoretic: the variational restriction prevents false early negativity, while one fixed test radius to the right of the true threshold eventually supplies negativity.

## 3. What this does and does not repair in PL-265

`PL-265` correctly identifies the CvS accumulated source path with the same localized completed Weil form studied by Suzuki. Its bridge claim is unchanged. The only correction is to its residual statement that pointwise fixed-radius convergence is inherently too weak to track a first crossing without drift.

For the specific nested Laurent-core sequence of `PL-261`, that obstruction disappears for the onset of **strict negativity**. The finite thresholds converge to `a_-` even if the convergence `mu_N(a) -> lambda_a` is arbitrarily nonuniform in `a`.

Several stronger moving-radius problems remain genuinely open:

1. A zero plateau is not excluded. The argument locates `inf{a:lambda_a<0}`, not necessarily `inf{a:lambda_a=0}`.
2. No convergence rate for `a_N-a_-` is obtained. Such a rate would require quantitative control of the spectral gap/slope or approximation error near the threshold.
3. No convergence of the minimizing eigenvectors is proved as `a` varies.
4. `PL-262` concerns a different and stronger task: locally uniform convergence of Fourier--Mellin transforms on the critical strip as the support expands. Domain monotonicity gives no control over the endpoint-amplified transform error there.
5. The threshold theorem does not automatically transfer to a different finite truncation unless it has both the restriction inequality `mu_N(a)>=lambda_a` and pointwise cofinal convergence at every fixed `a`.

Thus the useful correction is narrow but exact: **first strict-negativity detection is an order/variational problem, not a uniform approximation problem**.

## 4. Prime-lattice interpretation

Under the parameter dictionary fixed in `PL-265`,

\[
c=e^{2a},
\]

so increasing `a` means accumulating a larger initial segment of the prime-power axis source

\[
\{r e_p:r\log p\le2a\},
\]

together with the corresponding completed pole and archimedean terms. The theorem says that, at the level of the *completed localized Weil form*, this growing support family has a one-way sign transition in its ground energy.

This should not be misread as saying that the individual von-Mangoldt shocks force monotonicity. `PL-264` shows that their event-local geometry is universal and insufficient to explain the RH sign. The monotonicity here comes instead from **nested support domains of one global quadratic form**. It survives any matched control built from a fixed quadratic form with the same domain nesting, so it is not a zeta-specific positivity mechanism.

The arithmetic content remains concentrated in whether the threshold is finite at all. Under RH, Weil positivity keeps every `lambda_a>=0`; under failure of RH, some finite radius becomes negative. Domain monotonicity organizes that dichotomy but does not decide it.

## 5. Prior-art and novelty audit

The two load-bearing ingredients are already registered in `research/prime_lattice/SOURCES.md`:

- source 56, **Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2**. Corollary 1.2 identifies `lambda_a` with the infimum of the global Weil Rayleigh quotient over `C_c^infty(-a,a)`; Theorem 1.3 proves continuity; the surrounding discussion records positivity for sufficiently small `a` and equivalence of RH failure with strict negativity at some finite `a`.
- source 27, **Alain Connes and Caterina Consani, “Spectral triples and zeta-cycles,” L'Enseignement Mathématique 69 (2023)**. The Laurent polynomials are a form core at fixed semilocal scale, and the minima of the nested finite compressions converge to the lower bound; this is the theorem already distilled in `PL-261`.

Suzuki does not state the domain monotonicity as a named theorem in the inspected 2026 paper, and a targeted literature search did not locate a separate result asserting the finite-threshold convergence above. Nevertheless neither ingredient is technically novel: support-domain monotonicity and the threshold argument are elementary variational consequences once the two published statements are combined. **No originality is claimed for the general lemma.**

The durable line-specific delta is instead twofold: it removes a false obstruction from the post-`PL-265` frontier, and it identifies exactly which moving-radius tasks still need quantitative uniform control. No new source entry is required.

## 6. Adversarial audit and falsification

The argument was tested against the main ways pointwise convergence usually fails to control moving thresholds.

- **Spurious early crossings:** impossible here because every finite Rayleigh minimum is a restriction of the continuum problem, so `mu_N(a)>=lambda_a` pointwise.
- **Crossings drifting to the right:** impossible asymptotically because every fixed radius strictly to the right of `a_-` has `lambda_a<0`, and pointwise convergence eventually detects that negativity.
- **Nonmonotone finite dependence on `a`:** irrelevant. The proof does not require `a -> mu_N(a)` to be monotone; it uses only the definition of its first negative radius. Monotonicity in `N` follows from the nested Galerkin spaces at each fixed `a`.
- **Zero plateau:** not excluded and explicitly retained as a boundary. This is why the theorem concerns onset of strict negativity rather than earliest degeneracy.
- **Arbitrary truncation schemes:** excluded unless the restriction and pointwise-core hypotheses are proved for them.

The claim would fail if Suzuki's `lambda_a` could not be represented as the infimum of the same global `Q_W` over nested compact-support classes, or if the finite Laurent minima did not dominate and converge pointwise to that infimum. Those are exactly the published inputs cited above.

## Consequence for the research line

The localized CvS/Suzuki branch no longer needs a uniform-in-radius theorem merely to know **where strict negativity first appears in the Galerkin limit**. That threshold is already stable under the fixed-radius form-core convergence of `PL-261`.

What remains RH-facing is harder and more specific: derive the sign itself from source arithmetic; rule out or understand any zero plateau if earliest degeneracy is needed; obtain quantitative rates/eigenvector control near the threshold; or solve the expanding-window transform stability problem isolated in `PL-262`. A successor proposal that asks only for uniform convergence in order to prevent first-negative-threshold drift is solving an obstruction that is not actually present.
