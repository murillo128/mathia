# WP-108 — Exact critical prime-torus completions have infinite cylindrical Kronecker density energy

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CORRELATION-ROBUST + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-097`--`WP-107` leave a specific geometric escape after ordinary coordinatewise Fisher and relative-entropy routes fail at the Weil boundary: perhaps the positive prime-torus completion should not be differentiated in every prime coordinate separately. The prime logarithms already define a canonical **one-dimensional multiplicative/Kronecker flow**, so one could instead use the ordinary positive Dirichlet energy of the completion density along that single flow.

That route also has an exact correlation-independent critical obstruction.

Let

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T,
\qquad
m=\bigotimes_p\frac{d\theta_p}{2\pi},
\]

and let `mu_sigma` be a finite positive measure of mass `C>0` with the exact one-prime Weil rays

\[
\boxed{
\widehat\mu_\sigma(k e_p)
=-(\log p)p^{-|k|\sigma}
\qquad(p\text{ prime},\ k\in\mathbb Z\setminus\{0\}).
}
\tag{1}
\]

For a finite prime set `P`, normalize the marginal

\[
\eta_P:=\frac1C(\pi_P)_*\mu_\sigma,
\qquad
m_P:=\bigotimes_{p\in P}\frac{d\theta_p}{2\pi}.
\tag{2}
\]

The prime energies determine the canonical Kronecker flow

\[
\Phi_t((\theta_p)_{p\in P})
=(\theta_p+t\log p)_{p\in P}\pmod{2\pi},
\tag{3}
\]

with infinitesimal generator

\[
\boxed{
X_P:=\sum_{p\in P}(\log p)\,\partial_{\theta_p}.
}
\tag{4}
\]

Define the extended positive density energy

\[
\mathcal E_P^{\rm Kr}(\eta_P)
:=
\begin{cases}
\|X_Ph_P\|_{L^2(m_P)}^2,
&\eta_P=h_Pm_P,\ h_P\in L^2(m_P),\ X_Ph_P\in L^2(m_P),\\
+\infty,&\text{otherwise}.
\end{cases}
\tag{5}
\]

and its cylindrical global cost

\[
\mathcal E_{\rm cyl}^{\rm Kr}(\mu_\sigma)
:=\sup_{P\Subset\mathcal P}\mathcal E_P^{\rm Kr}(\eta_P).
\tag{6}
\]

Then every finite cylinder obeys

\[
\boxed{
\mathcal E_P^{\rm Kr}(\eta_P)
\ge
\frac{2}{C^2}
\sum_{p\in P}(\log p)^4
\frac{p^{-2\sigma}(1+p^{-2\sigma})}
{(1-p^{-2\sigma})^3}.
}
\tag{7}
\]

In particular, the first harmonics alone give

\[
\boxed{
\mathcal E_P^{\rm Kr}(\eta_P)
\ge
\frac{2}{C^2}
\sum_{p\in P}\frac{(\log p)^4}{p^{2\sigma}}.
}
\tag{8}
\]

Hence

\[
\boxed{
\mathcal E_{\rm cyl}^{\rm Kr}(\mu_\sigma)=+\infty
\qquad(\sigma\le1/2).
}
\tag{9}
\]

The threshold is sharp for this architecture: for every `sigma>1/2`, the positive product completion already used in `WP-097` and `WP-107` has the exact rays (1) and finite cylindrical Kronecker density energy.

Thus allowing arbitrary mixed-prime correlations and then collapsing the geometry to the canonical multiplicative one-parameter flow does **not** produce a finite ordinary `L^2` Dirichlet sign source at the critical exponent. The obstruction uses no zero data, no RH-equivalent positivity criterion, and no archimedean insertion.

## 1. The flow is intrinsic to the Prime-Lattice energy, not an added frequency choice

Prime Lattice writes a multiplicative state as an exponent vector `alpha=(alpha_p)` with logarithmic energy

\[
E(\alpha)=\sum_p\alpha_p\log p.
\tag{10}
\]

On the dual prime torus, the character

\[
z^\alpha(\theta)
:=\exp\!\left(i\sum_{p\in P}\alpha_p\theta_p\right)
\]

therefore satisfies

\[
\boxed{
X_Pz^\alpha=iE(\alpha)z^\alpha.
}
\tag{11}
\]

So (3)--(4) are the dual geometric realization of the already-present Mathia energy, rather than a hand-picked vector field designed after seeing the Weil coefficients.

For finite `P`, the numbers `{log p:p in P}` are rationally independent over `Q`: an integer relation `sum_p alpha_p log p=0` would imply `prod_p p^{alpha_p}=1`, and unique factorization forces every `alpha_p=0`. Thus the flow has no nonconstant zero-frequency character. This is the standard Kronecker/Bohr multiplicative flow associated with prime logarithms.

The Hilbert/Fourier framework itself is classical. In particular, the Bohr realization of square-summable Dirichlet coefficients as Hilbert geometry on the infinite prime polydisc/character space is part of the classical Hardy-space theory recorded in `SOURCES.md` through Hedenmalm--Lindqvist--Seip (1997). The new content claimed here is only the Mathia-specific obstruction obtained by combining that geometry with the exact critical cover moments.

## 2. Parseval makes the exact ray cost additive even under arbitrary correlations

Assume first that the finite marginal has finite energy in (5), so

\[
\eta_P=h_Pm_P.
\]

Use the Fourier convention

\[
\widehat h_P(\alpha)
=\int_{\mathbb T^P}h_P(\theta)\overline{z^\alpha(\theta)}\,dm_P.
\]

From (11), the weak derivative has Fourier coefficients

\[
\widehat{X_Ph_P}(\alpha)
=iE(\alpha)\widehat h_P(\alpha).
\]

Parseval therefore gives the exact positive decomposition

\[
\boxed{
\|X_Ph_P\|_2^2
=
\sum_{\alpha\in\mathbb Z^P}
|E(\alpha)|^2\,|\widehat h_P(\alpha)|^2.
}
\tag{12}
\]

The normalized exact ray moments from (1) are

\[
\widehat h_P(k e_p)
=-\frac{\log p}{C}\,p^{-|k|\sigma}.
\tag{13}
\]

Because `h_P` is real, the coefficients at `k e_p` and `-k e_p` have equal magnitude. Keeping only these orthogonal one-prime modes in (12) yields

\[
\begin{aligned}
\mathcal E_P^{\rm Kr}(\eta_P)
&\ge
\frac{2}{C^2}
\sum_{p\in P}\sum_{k\ge1}
(k\log p)^2(\log p)^2p^{-2k\sigma}\\
&=
\frac{2}{C^2}
\sum_{p\in P}(\log p)^4
\sum_{k\ge1}k^2p^{-2k\sigma}.
\end{aligned}
\tag{14}
\]

Using

\[
\sum_{k\ge1}k^2q^k
=\frac{q(1+q)}{(1-q)^3},
\qquad |q|<1,
\tag{15}
\]

proves (7).

This is the key correlation-robust step. Mixed-prime Fourier coefficients can be chosen arbitrarily subject to positivity. They enter (12) as **additional nonnegative squares** and therefore cannot cancel any mandatory axis cost. Possible near-resonances among mixed signed frequencies are irrelevant: the exact axis modes already give (8).

If a finite marginal has no `L^2` density or has no square-integrable weak derivative along `X_P`, its energy was defined as `+infinity`, so the same lower bound holds in the extended sense. No global absolute continuity is assumed.

## 3. The Weil boundary forces divergence even for a single geometric direction

At `sigma=1/2`, (8) becomes

\[
\mathcal E_P^{\rm Kr}(\eta_P)
\ge
\frac{2}{C^2}
\sum_{p\in P}\frac{(\log p)^4}{p}.
\tag{16}
\]

The prime harmonic series diverges, and `(log p)^4>=1` for all sufficiently large primes, so

\[
\sum_p\frac{(\log p)^4}{p}=+\infty.
\tag{17}
\]

Exhausting the primes proves (9) at the critical exponent. For `sigma<1/2`, the terms are eventually larger, so divergence persists.

The point is structural. `WP-102` showed that the exact critical state has infinite **coordinatewise square-root/Fisher** energy. A conceivable response was that summing separate prime directions was the wrong geometry: the multiplicative system has a distinguished one-dimensional flow, and perhaps differentiation only along that flow would remain finite. Equations (12)--(17) show that ordinary quadratic density energy does not gain that escape. Orthogonality of the one-prime Fourier modes recreates an additive prime cost inside the single generator.

This does not follow merely from the statement that the Kronecker orbit is dense. It follows from the exact spectrum of its generator and from the mandatory one-prime Fourier amplitudes.

## 4. The threshold is sharp above one half

For `sigma>1/2`, choose a finite constant `C` satisfying

\[
C\ge\sup_p\frac{2\log p}{p^\sigma-1}.
\tag{18}
\]

As in `WP-097` and `WP-107`, define

\[
\rho_{p,C,\sigma}(\theta)
:=1+\frac{\log p}{C}
\bigl(1-P_{p^{-\sigma}}(\theta)\bigr),
\tag{19}
\]

where `P_r` is the Poisson kernel. Condition (18) makes every factor nonnegative with Haar mean one, and the product completion

\[
\mu_{C,\sigma}
:=C\bigotimes_p\rho_{p,C,\sigma}\,dm
\tag{20}
\]

has exactly

\[
\widehat\mu_{C,\sigma}(k e_p)
=-(\log p)p^{-|k|\sigma}
\qquad(k\ne0).
\tag{21}
\]

Write `r_p=p^{-sigma}` and `a_p=(log p)/C`. The Fourier series of the Poisson kernel gives

\[
\|\rho_p\|_2^2
=1+\frac{2a_p^2r_p^2}{1-r_p^2},
\tag{22}
\]

and

\[
\|\rho_p'\|_2^2
=2a_p^2
\frac{r_p^2(1+r_p^2)}{(1-r_p^2)^3}.
\tag{23}
\]

For a finite product `h_P=prod_{p in P} rho_p`,

\[
X_Ph_P
=\sum_{p\in P}(\log p)\rho_p'
\prod_{q\in P\setminus\{p\}}\rho_q.
\tag{24}
\]

All cross terms in its squared `L^2` norm vanish because

\[
\int_{\mathbb T}\rho_p\rho_p'\,dm
=\frac12\int_{\mathbb T}(\rho_p^2)'\,dm=0.
\tag{25}
\]

Hence

\[
\boxed{
\|X_Ph_P\|_2^2
=
\left(\prod_{q\in P}\|\rho_q\|_2^2\right)
\sum_{p\in P}
(\log p)^2
\frac{\|\rho_p'\|_2^2}{\|\rho_p\|_2^2}.
}
\tag{26}
\]

For `sigma>1/2`,

\[
\sum_p(\|\rho_p\|_2^2-1)
\ll_C
\sum_p\frac{(\log p)^2}{p^{2\sigma}}<\infty,
\tag{27}
\]

so the finite products in (26) are uniformly bounded. Equations (23) and (26) also give

\[
\sum_p(\log p)^2\|\rho_p'\|_2^2
\ll_C
\sum_p\frac{(\log p)^4}{p^{2\sigma}}<\infty.
\tag{28}
\]

Therefore

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal E_P^{\rm Kr}((\mu_{C,\sigma}/C)_P)<\infty
\qquad(\sigma>1/2).
}
\tag{29}
\]

So `sigma=1/2` is the exact boundary between finite and forced-infinite cylindrical Kronecker density energy for this exact-moment architecture.

## 5. Relation to WP-101--WP-107

`WP-101` shows that correlations can produce a critical positive completion equivalent to Haar, but every globally absolutely continuous completion lies below the classical `L(log L)^{1/2}` regularity endpoint. That already warns that an ordinary global `L^2` density is unavailable. The present result is more geometric and cylindrical: it places the canonical multiplicative generator into the finite-coordinate marginals and proves an explicit divergent derivative-energy lower bound without assuming a global density at all.

`WP-102` proves a correlation-robust obstruction for the coordinatewise square-root/Fisher energy

\[
4\sum_p\|\partial_p\sqrt{h_P}\|_2^2.
\]

It explicitly leaves one-dimensional Kronecker-flow geometry outside its theorem. `WP-108` closes the most direct such route, namely the ordinary positive `H^1`/Dirichlet energy of the **density itself** along the intrinsic multiplicative generator `X`. It does not identify that energy with Fisher information and does not inherit the proof of `WP-102`.

`WP-103` computes a divergent Kronecker derivative energy for the **log density of one specific product Gibbs selector**. That result does not cover arbitrary positive completions or mixed-prime correlations. Here the exact Weil rays are moments of the completion itself, the density may contain arbitrary mixed coefficients, and Parseval makes the obstruction correlation-independent.

`WP-107` rules out ordinary KL/total-correlation geometry by a different additive mechanism. `WP-108` shows that reducing the number of geometric derivative directions from one per prime to the single multiplicative direction does not repair ordinary quadratic state regularity.

## 6. Matched generalized-generator control

Nothing in the Parseval argument uses zeros or the functional equation. For any free commutative generator system with positive energies `lambda_j`, torus coordinates `theta_j`, flow

\[
X_\lambda=\sum_j\lambda_j\partial_{\theta_j},
\]

and prescribed first moments

\[
\widehat\mu(e_j)
=-\lambda_j e^{-\sigma\lambda_j},
\]

the same calculation gives

\[
\mathcal E_P^{\rm Kr}
\ge
\frac{2}{C^2}\sum_{j\in P}
\lambda_j^4e^{-2\sigma\lambda_j}.
\tag{30}
\]

Thus the mechanism is ordinary positive harmonic analysis on a free-generator character torus. The special arithmetic input is the prime energy sequence `lambda_p=log p` and the critical half-weight already forced elsewhere in Mathia. Generalized-prime systems with comparable prime-density growth exhibit the same critical regularity obstruction, so (9) is not by itself an arithmetic theorem capable of distinguishing the Riemann zeta function from matched Euler-product controls.

This is exactly the novelty boundary: the Fourier/Bohr/Kronecker machinery is classical; the retained contribution is the exact Mathia-specific no-go for a surviving candidate sign source.

## 7. Aggressive falsification and surviving routes

Several apparent escapes do not affect the theorem:

- **Mixed-prime correlations:** they add nonnegative terms to (12); they cannot cancel the exact axis squares.
- **Near-resonant mixed frequencies:** even if some `E(alpha)` are small, (8) uses only `alpha=+-e_p`, whose frequency is exactly `+-log p`.
- **Global singularity:** no global density is assumed. A bad finite marginal already has energy `+infinity`; otherwise the finite-cylinder Parseval bound applies.
- **Constant time rescaling:** replacing `X` by `cX`, `c ne 0`, only multiplies the energy by `c^2`.
- **Subtracting the divergent axis contribution:** that is a renormalization of a positive sum, not positivity inherited from the ordinary Dirichlet form. It would require a separate intrinsic theorem fixing both subtraction and sign.

The following remain genuinely outside `WP-108`:

1. a square-root/Fisher or another nonlinear state geometry taken **only along** the Kronecker flow, where correlations can couple the relevant vectors and the Parseval argument above does not directly apply;
2. negative-order, nonlocal, sub-Riemannian, or distributional norms whose symbol deliberately suppresses the mandatory axis frequencies, provided Mathia forces that symbol independently rather than it being chosen to absorb the divergence;
3. an infinite-codimension quotient or nonlinear observable acting before the state is scalarized;
4. a finite--archimedean coupling that changes the completed state or its geometry before positivity is taken;
5. a positive form on external test functions rather than a regularity energy of the prime-torus completion density.

Those distinctions matter. `WP-108` does **not** prove that every conceivable one-dimensional multiplicative geometry fails, and it does not produce the archimedean or polar terms of the Weil explicit formula. It proves a narrower but decisive statement: the canonical first-order `L^2` Dirichlet energy of the exact positive completion density is already forced to infinite cost at the critical exponent, even after arbitrary correlations are allowed.

## 8. Consequence for the research line

The positive-completion route has now survived successively stronger freedoms -- mixed modes, correlations, Haar-equivalent critical completions, nonlinear Gibbs selectors, and information projection -- but its ordinary positive state geometries keep becoming singular exactly at `sigma=1/2`.

`WP-108` removes the most direct attempt to evade the coordinatewise Fisher obstruction by using only the intrinsic multiplicative flow:

\[
\boxed{
\text{exact positive prime-torus completion}
\to
\text{canonical }\log p\text{ Kronecker flow}
\to
\|Xh\|_2^2\ge0
\not\to
\text{finite critical global sign source}.
}
\tag{31}
\]

The remaining route must therefore change more than the direction in which the same completion density is differentiated. To bear on the canonical mandate, it still has to produce in one construction the finite Mangoldt structure, the archimedean/polar counterterms, and an independent geometric sign theorem rather than another regularized representation of already-known arithmetic data.
