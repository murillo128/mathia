# WP-107 — Exact critical prime-torus completions have infinite cylindrical relative entropy, regardless of correlations

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATION-ROBUST + SHARP-THRESHOLD + INFORMATION-GEOMETRY + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-097` shows that exact cover positivity can coexist with all critical one-prime Weil moments at finite diagonal mass once mixed-prime moments are allowed, and `WP-101` shows that correlations can even make such a critical completion equivalent to product Haar. This leaves a natural nonlinear possibility: use an information-theoretic positive functional rather than a positive linear quotient, so that marginalization can forget mixed-prime correlations while relative entropy supplies an independent sign theorem.

That route has a correlation-independent critical obstruction.

Let

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T,
\qquad
m=\bigotimes_p\frac{d\theta_p}{2\pi},
\]

and let `mu_sigma` be any finite positive measure of mass `C>0` satisfying just the first exact one-prime moments

\[
\boxed{
\widehat\mu_\sigma(e_p)
=-\frac{\log p}{p^\sigma}
\qquad\text{for every prime }p.
}
\tag{1}
\]

No assumption is made on mixed-prime Fourier coefficients, factorization, absolute continuity, or global measure class. For a finite prime set `P`, normalize its marginal by

\[
\eta_P:=\frac1C(\pi_P)_*\mu_\sigma,
\qquad
m_P:=\bigotimes_{p\in P}\frac{d\theta_p}{2\pi}.
\tag{2}
\]

Define the cylindrical relative-entropy cost

\[
\mathcal H_{\rm cyl}(\mu_\sigma)
:=\sup_{P\Subset\mathcal P}
D_{\rm KL}(\eta_P\|m_P).
\tag{3}
\]

Then every finite cylinder satisfies the exact lower bound

\[
\boxed{
D_{\rm KL}(\eta_P\|m_P)
\ge
\frac1{2C^2}
\sum_{p\in P}\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{4}
\]

Consequently

\[
\boxed{
\mathcal H_{\rm cyl}(\mu_\sigma)=+\infty
\qquad(\sigma\le1/2).
}
\tag{5}
\]

In particular, **every** exact critical positive completion has infinite cylindrical KL cost, including correlated completions that are globally Haar-equivalent. Mixed-prime correlations can pay the ordinary positivity debt of `WP-096` and can repair the product-measure singularity of `WP-100`, but they cannot make ordinary relative-entropy geometry finite at the Weil boundary.

The threshold is sharp for this architecture. For every `sigma>1/2`, a direct supercritical extension of the `WP-097` product completion has the same exact one-prime moments and finite cylindrical relative entropy.

This closes the natural route

\[
\text{exact positive prime-torus completion}
\to
\text{marginalization / information projection}
\to
\text{finite KL or total-correlation geometry}
\to
\text{independent global Weil sign}
\]

at `sigma=1/2`. A renormalized entropy difference, a non-KL nonlinear invariant, a reference measure that is itself globally coupled, or a genuinely nonseparable finite--archimedean object can lie outside the theorem, but its sign cannot be inherited from a finite ordinary KL energy of the exact critical prime-torus state.

## 1. One exact coordinate moment forces a KL cost

Fix a finite prime set `P` and a prime `p in P`. Let `eta_p` be the `p`-th one-coordinate marginal of `eta_P`. From (1),

\[
a_p
:=\int_{\mathbb T}\overline z\,d\eta_p(z)
=-\frac{\log p}{C p^\sigma}.
\tag{6}
\]

The Haar first moment is zero. With total variation normalized as

\[
\|\nu-\rho\|_{\rm TV}
:=\sup_A|\nu(A)-\rho(A)|,
\]

any complex function bounded by one obeys

\[
\left|\int f\,d(\nu-\rho)\right|
\le2\|\nu-\rho\|_{\rm TV}.
\]

Applying this to the circle character gives

\[
|a_p|
\le2\|\eta_p-m_p^{(1)}\|_{\rm TV},
\tag{7}
\]

where `m_p^(1)` is circle Haar. Pinsker's inequality in natural logarithms gives

\[
D_{\rm KL}(\eta_p\|m_p^{(1)})
\ge2\|\eta_p-m_p^{(1)}\|_{\rm TV}^2.
\tag{8}
\]

If the marginal is singular, the left side is already `+infinity`. Otherwise (7)--(8) imply

\[
\boxed{
D_{\rm KL}(\eta_p\|m_p^{(1)})
\ge\frac{|a_p|^2}{2}
=
\frac1{2C^2}\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{9}
\]

Only the first one-prime Fourier coefficient is used. No mixed moment can cancel this one-coordinate information cost.

## 2. Total correlation makes the lower bounds additive

The crucial point is that correlations do not merely fail to cancel (9) one prime at a time; ordinary relative entropy decomposes them off as an additional nonnegative term.

For finite `P`, let

\[
\eta_P^{\rm prod}:=\bigotimes_{p\in P}\eta_p.
\tag{10}
\]

Whenever `D_KL(eta_P||m_P)` is finite, the Radon--Nikodym chain rule gives

\[
\boxed{
D_{\rm KL}(\eta_P\|m_P)
=
D_{\rm KL}(\eta_P\|\eta_P^{\rm prod})
+
\sum_{p\in P}D_{\rm KL}(\eta_p\|m_p^{(1)}).
}
\tag{11}
\]

The first term is Watanabe's total correlation and is nonnegative. If the left side is infinite, the desired lower bound is automatic. Combining (9) and (11) therefore proves (4).

This is stronger than a factorization argument. The joint law may contain arbitrary mixed-prime Fourier coefficients and arbitrary dependence. Those correlations can only contribute the extra nonnegative term in (11); they cannot reduce the sum of the mandatory marginal KL costs.

At the critical exponent,

\[
\sum_p\frac{(\log p)^2}{p}=+\infty,
\tag{12}
\]

already because `sum_p 1/p` diverges and `(log p)^2` is eventually bounded below by a positive constant. Exhausting the primes in (4) proves (5) for `sigma=1/2`; smaller `sigma` only increases the tail.

If a global relative entropy `D_KL(mu_sigma/C || m)` is considered, data processing under every finite-coordinate projection gives

\[
D_{\rm KL}(\mu_\sigma/C\|m)
\ge D_{\rm KL}(\eta_P\|m_P),
\]

so (5) also forces the global KL divergence to be infinite. The cylindrical formulation is the more informative statement because it detects the divergence through finite marginals even when the infinite-product measure itself is singular or has no useful global density.

## 3. The boundary is sharp above one half

The lower bound is not an artifact of Pinsker at the critical point. For `sigma>1/2`, choose any finite `C` satisfying

\[
C\ge
\sup_p\frac{2\log p}{p^\sigma-1}.
\tag{13}
\]

The supremum is finite. Define the one-coordinate densities

\[
\rho_{p,C,\sigma}(\theta)
:=1+\frac{\log p}{C}
\bigl(1-P_{p^{-\sigma}}(\theta)\bigr),
\tag{14}
\]

where `P_r` is the Poisson kernel. Exactly as in `WP-097`, (13) makes every factor nonnegative with Haar mean one, and the product measure

\[
\mu_{C,\sigma}
:=C\bigotimes_p\rho_{p,C,\sigma}\,dm
\tag{15}
\]

has

\[
\widehat\mu_{C,\sigma}(k e_p)
=-(\log p)p^{-|k|\sigma}
\qquad(k\ne0).
\tag{16}
\]

In particular it satisfies (1).

Its local KL costs are summable. Since `log x<=x-1` for `x>=0` and each `rho` has mean one,

\[
\begin{aligned}
D_{\rm KL}(\rho_{p,C,\sigma}m\|m)
&=\int\rho_{p,C,\sigma}\log\rho_{p,C,\sigma}\,dm\\
&\le\int(\rho_{p,C,\sigma}-1)^2\,dm.
\end{aligned}
\tag{17}
\]

The Poisson Fourier series gives

\[
\|P_r-1\|_2^2
=2\sum_{k\ge1}r^{2k}
=\frac{2r^2}{1-r^2},
\]

so

\[
\boxed{
D_{\rm KL}(\rho_{p,C,\sigma}m\|m)
\le
\frac{2(\log p)^2}{C^2(p^{2\sigma}-1)}.
}
\tag{18}
\]

For `sigma>1/2`, the sum of the right-hand side over primes converges. KL additivity for finite products therefore yields

\[
\sup_{P\Subset\mathcal P}
D_{\rm KL}((\mu_{C,\sigma}/C)_P\|m_P)
<\infty.
\tag{19}
\]

Thus the critical value `sigma=1/2` is the exact transition for finite cylindrical KL geometry in this moment architecture.

## 4. Relation to WP-101--WP-103

`WP-101` proves a global regularity obstruction: every globally absolutely continuous critical completion lies below the classical `L(log L)^{1/2}` endpoint, while correlations can nevertheless restore Haar equivalence. The present statement does not assume global absolute continuity at all. It gives a quantitative finite-cylinder entropy lower bound from the first coordinate moments alone and shows that the KL cost diverges through the growing family of finite prime marginals.

`WP-102` proves the analogous correlation-robust obstruction for first-order spatial Fisher geometry,

\[
\mathcal I_P\gtrsim
\sum_{p\in P}\frac{(\log p)^2}{p^{2\sigma}}.
\]

`WP-107` is the zero-order information-geometric counterpart: even before taking derivatives of a density or square root, the exact coordinate bias already carries an additive KL cost with the same critical square-summability threshold. The two results rule out different sign sources; neither follows from the other's hypotheses.

`WP-103` studies a different nonlinear construction: exponentiating the sparse `WP-022` score produces a positive Gibbs density whose **log density**, rather than its density moments, has exact Weil rays, and that particular Gibbs family has divergent critical relative entropy. The present theorem should not be conflated with that selector. Here the exact Weil rays are moments of the positive completion itself, as in `WP-097`/`WP-101`, and the divergence holds for every correlated completion with those moments.

## 5. Why marginal entropy does not rescue the mixed-prime clue

Relative entropy initially looks unusually well matched to the live clue after `WP-098`/`WP-099`. Marginalization is canonical and positive, and the chain rule (11) separates the correlation sector from the one-prime sector without applying the non-positive first-chaos Fourier projector.

But the price is exact: each critical one-prime observable contributes a nonnegative cost of order

\[
\frac{(\log p)^2}{p},
\]

and these costs add. The all-prime information geometry therefore has infinite mass before any Gamma or polar term is introduced.

One can subtract the divergent marginal sum, take a finite part, or compare two infinite entropies. Such a renormalized difference may be mathematically meaningful, but its sign is no longer a consequence of ordinary KL nonnegativity. Under the research mandate that subtraction must acquire its own independently forced geometric theorem; choosing it to leave the Weil functional would simply reinsert the desired answer.

Likewise a globally coupled reference state may change the decomposition (11). That is a genuine escape only if Mathia supplies the reference and its finite--archimedean coupling intrinsically. It is not a repair of ordinary product-Haar relative entropy.

## 6. Matched free-generator control

The argument contains no arithmetic fact specific to the rational primes except the growth of the prescribed amplitudes. For a free commutative generator system with energies `E_j>0`, character torus `prod_j T`, and exact first moments

\[
\widehat\mu_\sigma(e_j)
=-E_j e^{-\sigma E_j},
\tag{20}
\]

any finite positive completion of mass `C` obeys

\[
\boxed{
D_{\rm KL}(\eta_J\|m_J)
\ge
\frac1{2C^2}
\sum_{j\in J}E_j^2e^{-2\sigma E_j}.
}
\tag{21}
\]

Thus the obstruction is the universal square-summability cost of biased independent coordinates under a product reference. Rational primes specialize to `E_p=log p`, where the boundary is `sigma=1/2`. This matched control prevents interpreting the entropy divergence itself as Riemann-specific evidence.

## 7. Prior art and novelty audit

The information-theoretic ingredients are classical. Satosi Watanabe, *Information Theoretical Analysis of Multivariate Correlation*, IBM Journal of Research and Development **4** (1960), 66--82, DOI `10.1147/rd.41.0066`, introduced total correlation and its entropy decompositions. M. S. Pinsker, *Information and Information Stability of Random Variables and Processes*, Holden-Day (1964), is the classical source for the inequality relating KL divergence and total variation used in (8). Csiszar's divergence framework and later information-theory texts place both steps in standard data-processing/relative-entropy theory.

No novelty is claimed for Pinsker's inequality, total correlation, the KL chain rule, product additivity, or the Poisson-factor construction as general mathematics. The Mathia-specific durable consequence is their combination with the exact cover-positive critical moments (1): every correlation pattern pays an additive finite-cylinder entropy cost whose sharp transition is exactly the same `sigma=1/2` boundary already exposed by the line's Gram and Fisher analyses.

A targeted prior-art search found standard total-correlation decompositions, Pinsker/f-divergence inequalities, and moment-versus-entropy variational bounds, not an independent arithmetic positivity mechanism that would turn this classical entropy cost into the global zeta Weil form.

## Consequence for the research line

The mixed-prime completion escape is narrower again. Correlations are powerful enough to restore ordinary positivity and even Haar equivalence at the critical Weil rays, but **ordinary relative entropy cannot be the finite global geometric energy that converts that carrier into Weil positivity**:

\[
\boxed{
\text{exact critical one-prime moments}
\Longrightarrow
\mathcal H_{\rm cyl}=+\infty
\quad\text{for every positive completion.}
}
\]

Together with `WP-102`, this removes the two most canonical local information-geometric sign sources—KL and product-coordinate Fisher energy—from the exact critical prime-torus completion route. A survivor must change the reference geometry, use a genuinely nonlocal/degenerate information metric, or form the finite and archimedean sectors together before the critical moment completion is interpreted as a standalone positive state. It must then prove the resulting sign independently and survive the generalized-generator control.