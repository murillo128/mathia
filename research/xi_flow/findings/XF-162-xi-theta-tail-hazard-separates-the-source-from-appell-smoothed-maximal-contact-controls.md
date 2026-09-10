---
type: positive
research_line: xi_flow
finding_id: XF-162
status: canonical
---

# XF-162 — Xi theta-tail hazard separates the source from Appell-smoothed maximal-contact controls

**Confidence:** high for the source asymptotics and the separation from the concrete XF-160/XF-161 controls. The proof uses only the explicit theta-source formula already present in the line and elementary Gaussian-mixture identities. This is **not** yet a transition-time theorem: it identifies an Xi-specific quantitative source invariant that the current negative controls fail, but does not prove that every source satisfying the invariant excludes maximal-contact blindness.

## Statement

XF-160 and XF-161 showed that positivity, absolute continuity, strict positivity, and real-analytic source regularity do not by themselves rule out prescribed transition gaps. The remaining source distinction can be made quantitative.

In the line normalization

\[
H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\]

the Xi theta source is

\[
\Phi(u)=\sum_{n\ge1}
\pi n^2e^{5u}\bigl(2\pi n^2e^{4u}-3\bigr)
 e^{-\pi n^2e^{4u}},
\qquad u\ge0.
\tag{1}
\]

Define the normalized tail action and logarithmic hazard

\[
\mathfrak T_\rho(u):=-e^{-4u}\log\rho(u),
\qquad
\mathfrak H_\rho(u):=-e^{-4u}\frac{d}{du}\log\rho(u),
\tag{2}
\]

whenever `rho` is a positive differentiable density. Then the Xi source satisfies

\[
\boxed{
\mathfrak T_\Phi(u)\longrightarrow\pi,
\qquad
\mathfrak H_\Phi(u)\longrightarrow4\pi,
\qquad
-e^{-4u}(\log\Phi)''(u)\longrightarrow16\pi.
}
\tag{3}
\]

In particular, `Phi` has quadratic exponential moments of every order:

\[
\boxed{
\int_0^\infty e^{t u^2}\Phi(u)\,du<\infty
\quad\text{for every }t\ge0.
}
\tag{4}
\]

By contrast, every fixed-`sigma` Appell-smoothed source from XF-161 is a finite positive Gaussian mixture

\[
\nu_\sigma(\xi)
=
\frac{\sigma}{\sqrt{2\pi}}
\int
\exp\!\left[-\frac{\sigma^2}{2}(\xi-\eta)^2\right]d\mu_M(\eta),
\tag{5}
\]

with `mu_M` supported in `[-M,M]`. It obeys

\[
\boxed{
\lim_{\xi\to+\infty}\mathfrak H_{\nu_\sigma}(\xi)=0,
\qquad
\lim_{\xi\to+\infty}-e^{-4\xi}(\log\nu_\sigma)''(\xi)=0,
}
\tag{6}
\]

and its quadratic exponential-moment domain is exactly

\[
\boxed{
\int_{\mathbb R}e^{t\xi^2}\nu_\sigma(\xi)d\xi<\infty
\quad\Longleftrightarrow\quad
t<\frac{\sigma^2}{2}.
}
\tag{7}
\]

The separation also survives the maximal-contact scaling itself. For the XF-161 family at its outer spectral scale `xi=M+1`, with the fixed `sigma` used to realize any prescribed finite heat window,

\[
\boxed{
\mathfrak H_{\nu_\sigma}(M+1)\longrightarrow0,
\qquad
\mathfrak H_\Phi(M+1)\longrightarrow4\pi.
}
\tag{8}
\]

Thus the current smooth maximal-contact controls are quantitatively outside the Xi tail-hazard class. The atomic XF-160 controls are outside it for the simpler reason that they do not possess a strictly positive source density at all. Their finite support does give all quadratic exponential moments, so **all-time moment admissibility alone is not the missing rigidity**; the useful source information is the conjunction of a genuine density with the Xi-scale double-exponential tail law, or something still stronger that forces it.

## 1. The first theta summand controls the complete tail jet

Put

\[
x=e^{4u}
\]

and isolate the `n=1` summand

\[
\phi_1(u)
=
\pi e^{5u}(2\pi x-3)e^{-\pi x}.
\tag{9}
\]

For `n>=2`, division by `(9)` gives

\[
\frac{\phi_n(u)}{\phi_1(u)}
=
n^2\frac{2\pi n^2x-3}{2\pi x-3}
 e^{-\pi(n^2-1)x}.
\tag{10}
\]

Since `x>=1`, the rational prefactor is `O(n^4)` uniformly in `x`, while `n^2-1>=3`. Summing `(10)` therefore yields

\[
\Phi(u)=\phi_1(u)
\left(1+O(e^{-3\pi x})\right).
\tag{11}
\]

Applying `d/du=4x d/dx` any fixed number of times only introduces polynomial factors in `x`; these remain negligible compared with `e^{-3\pi x}`. Hence `(11)` may be differentiated twice at the logarithmic level for the limits used below.

The leading logarithm is explicit:

\[
\log\phi_1(u)
=
-\pi e^{4u}+9u+\log(2\pi^2)
+\log\!\left(1-\frac{3}{2\pi}e^{-4u}\right).
\tag{12}
\]

Consequently

\[
(\log\phi_1)'(u)
=
9+\frac{12}{2\pi e^{4u}-3}-4\pi e^{4u},
\tag{13}
\]

and

\[
(\log\phi_1)''(u)
=
-16\pi e^{4u}
-\frac{96\pi e^{4u}}{(2\pi e^{4u}-3)^2}.
\tag{14}
\]

Equations `(11)`--`(14)` prove all three limits in `(3)`. They also make the relevant geometry explicit: the natural Xi hazard is of order `e^(4u)`, not linear in `u` as for a Gaussian tail.

Finally, `(12)` gives

\[
\Phi(u)=\exp\bigl(-\pi e^{4u}+O(u)\bigr).
\tag{15}
\]

For every fixed `t>=0`, the exponent `tu^2-\pi e^(4u)+O(u)` tends to `-infinity` faster than any quadratic, proving `(4)`.

## 2. Gaussian-mixture log hazards are only linear

Write `(5)` as a finite mixture over atoms `eta_j` with positive weights and let `w_j(xi)` be the posterior mixture weights at a given `xi`. If

\[
\bar\eta_\xi=\sum_jw_j(\xi)\eta_j,
\]

then direct differentiation gives the exact identities

\[
(\log\nu_\sigma)'(\xi)
=-\sigma^2(\xi-\bar\eta_\xi),
\tag{16}
\]

and

\[
(\log\nu_\sigma)''(\xi)
=-\sigma^2+
\sigma^4\operatorname{Var}_{w(\xi)}(\eta).
\tag{17}
\]

For each fixed finite support, `(16)` is `O(xi)` and `(17)` is bounded as `xi->+infinity`, proving `(6)` after multiplication by `e^(-4xi)`.

More importantly, `(16)` evaluates uniformly on the XF-160/XF-161 spectral scale. Because `|eta_j|<=M`,

\[
\left|(\log\nu_\sigma)'(M+1)\right|
\le \sigma^2(2M+1).
\tag{18}
\]

For fixed `sigma`, therefore,

\[
0\le
\left|\mathfrak H_{\nu_\sigma}(M+1)\right|
\le
\sigma^2(2M+1)e^{-4(M+1)}
\longrightarrow0,
\tag{19}
\]

whereas `(3)` gives `mathfrak H_Phi(M+1)->4pi`. This is the decisive scale-stable separation requested by the source-tail clue.

The moment boundary `(7)` is equally direct. Each component has exponent

\[
t\xi^2-\frac{\sigma^2}{2}(\xi-\eta_j)^2
=
\left(t-\frac{\sigma^2}{2}\right)\xi^2
+\sigma^2\eta_j\xi+O(1).
\tag{20}
\]

The integral converges on both tails exactly when `t<sigma^2/2`. At equality the remaining exponential-linear or constant factor is not integrable; above equality the quadratic term grows. This recovers, from the source alone, the finite positive-time Appell horizon of XF-161.

## 3. What the discriminator does and does not exclude

The result closes one concrete source-side ambiguity left by XF-161. Its Gaussian smoothing can reproduce positivity, strict positivity, analyticity and any prescribed finite heat horizon, but it cannot reproduce the Xi tail hazard or a single source valid under every positive quadratic heat multiplier. The distinction is not qualitative: `(8)` keeps a fixed `4pi` gap in a normalized logarithmic derivative directly on the maximal-contact scale.

The atomic XF-160 control is a useful stress test. Because a finite measure has every quadratic exponential moment, the property `(4)` by itself cannot exclude that family. Conversely, requiring a smooth positive density by itself was already defeated by XF-161. A viable source theorem must combine quantitative tail shape with enough global rigidity to prevent replacing the compact or mesoscopic part of the source while preserving the same asymptotic tail.

This last qualification is essential. Nothing proved here prevents constructing some other strictly positive all-time source with the same limits `(3)` and a maximal-contact transition gap. Tail asymptotics can often be preserved under compactly supported or super-small perturbations. Therefore **XF-162 does not upgrade XF-159's observation lower bound, does not bound the de Bruijn--Newman transition time, and does not imply RH**.

The next decisive gate is a no-splicing question: derive an Xi-specific identity or inequality that couples the tail law `(3)` to the finite and mesoscopic spectral mass strongly enough to obstruct the folded-binomial maximal-contact direction. Alternatively, construct a positive all-time smooth source with the same normalized tail hazard and a prescribed transition gap; that would falsify tail hazard alone and force the search deeper into the theta coefficient structure.

## Prior-art and novelty audit

The theta-kernel representation and dominance of its first summand in the far tail are classical, and recent work on the Xi kernel studies stronger shape properties such as log-concavity and theta-tail inequalities. A directed prior-art search did not locate a theorem identifying the normalized quantity `(2)` as a de Bruijn--Newman transition discriminator, nor a result comparing it with Appell-smoothed maximal-contact controls.

No external theorem is load-bearing here: `(3)` follows directly from the explicit source formula `(1)`, and `(6)`--`(8)` follow directly from the Gaussian-mixture formula of XF-161. The novelty claimed is only the Mathia-specific comparison and the resulting source-side gate, not the classical theta asymptotic itself. `SOURCES.md` therefore requires no update.

## Consequence for `xi_flow`

The source frontier is now more precise. XF-160 shows that source positivity is noncoercive; XF-161 shows the same for positive analytic densities on arbitrary finite heat windows; XF-162 identifies a concrete invariant those smooth controls cannot fake: Xi has a nonzero `e^(4u)`-normalized logarithmic hazard and infinite positive heat-moment radius, while the Appell-smoothed controls have normalized hazard zero and finite radius.

That is enough to accept the source-tail research direction as genuine traction, but not to resolve it. The next useful work is no longer to list additional qualitative properties of `Phi`; it is to test whether the tail hazard is **globally coupled** to the source by theta structure, or whether it can be spliced onto another maximal-contact source without changing the transition mechanism.