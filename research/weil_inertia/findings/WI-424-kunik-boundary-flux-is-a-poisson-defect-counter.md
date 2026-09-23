# WI-424 — Kunik's boundary Blaschke flux is a positive Poisson defect counter with reciprocal-depth energy

Status: `LITERATURE+DERIVED + CLASSICAL-IDENTITY + EXACT-DERIVED + PRIOR-ART-REDIRECT`

Parents: `WI-409`, `WI-411`, `WI-417`, `WI-421`, `WI-422`, `WI-423`

## Claim

`WI-423` shows that the canonical planar Riesz source of the zeta Blaschke defect is atomic, so planar absolute continuity of that exact source would already force zero defect. The same canonical Blaschke product has a different exact object on the boundary which is automatically absolutely continuous: its inward normal flux is a positive superposition of one-dimensional Poisson kernels.

Write an off-critical zero in the right half-strip as

\[
\rho=\frac12+d_\rho+i\gamma_\rho,
\qquad 0<d_\rho<\frac12,
\]

with multiplicity \(m_\rho\). For a finite subproduct \(B_F\) of Kunik's half-plane Blaschke product, define on the critical-line boundary

\[
h_F(t):=-\frac{B_F'(\frac12+it)}{B_F(\frac12+it)}.
\]

Then exactly

\[
\boxed{
h_F(t)=
\sum_{\rho\in F}
\frac{2m_\rho d_\rho}
{(t-\gamma_\rho)^2+d_\rho^2}
\ge0.
}
\tag{1}
\]

Equivalently, if

\[
U_F(x,t):=-\log|B_F(\tfrac12+x+it)|,
\qquad x>0,
\]

then

\[
\boxed{h_F(t)=\partial_xU_F(0^+,t).}
\tag{2}
\]

Thus the atomic planar source from `WI-423` has an exact **Poisson boundary projection**. No smoothing parameter is introduced and no sign cancellation is possible.

For the full Kunik product, wherever the boundary logarithmic derivative is defined, let

\[
h_B(t):=-\frac{B'(\frac12+it)}{B(\frac12+it)}.
\]

Kunik's Theorem 2.5 and its estimate (2.36) imply, for the admissible heights in that theorem,

\[
\boxed{
N_B(T)-\frac1{2\pi}\int_{-T}^{T}h_B(t)\,dt
=O(\log^2T),
}
\tag{3}
\]

where \(N_B(T)\) counts the Blaschke zeta zeros with \(\Re\rho>1/2\) and \(|\Im\rho|\le T\). Since \(N(T)\asymp T\log T\), the error in (3) is negligible at density scale. The boundary flux is therefore an asymptotically exact positive smeared counter for the off-line defect population, not merely an analogy with one.

The regularity cost is also exact. For one defect

\[
h_{d,\gamma}(t)=\frac{2d}{(t-\gamma)^2+d^2},
\]

and every \(p>1/2\) satisfies

\[
\boxed{
\|h_{d,\gamma}\|_p^p
=
C_p d^{1-p},
\qquad
C_p=2^p\sqrt\pi\,
\frac{\Gamma(p-\frac12)}{\Gamma(p)}.
}
\tag{4}
\]

In particular,

\[
\|h_{d,\gamma}\|_1=2\pi,
\qquad
\|h_{d,\gamma}\|_2^2=\frac{2\pi}{d}.
\tag{5}
\]

For every finite positive superposition and \(p\ge1\),

\[
\boxed{
\|h_F\|_p^p
\ge
C_p\sum_{\rho\in F}m_\rho^p d_\rho^{1-p}.
}
\tag{6}
\]

At \(p=2\) there is a stronger exact positive pair identity,

\[
\boxed{
\|h_F\|_2^2
=4\pi
\sum_{\rho,\rho'\in F}
 m_\rho m_{\rho'}
\frac{d_\rho+d_{\rho'}}
{(\gamma_\rho-\gamma_{\rho'})^2+(d_\rho+d_{\rho'})^2}.
}
\tag{7}
\]

Hence

\[
\boxed{
\|h_F\|_2^2
\ge
2\pi\sum_{\rho\in F}\frac{m_\rho^2}{d_\rho}.
}
\tag{8}
\]

Boundary absolute continuity is therefore free, but boundary \(L^p\) control for \(p>1\) is not: it imposes an explicit reciprocal-depth tariff on shallow off-line zeros. This is the useful replacement for the impossible planar-density interpretation ruled out by `WI-423`.

The remaining issue is arithmetic independence. The flux still encodes the off-line zeros exactly, so postulating an \(L^p\) bound for it would be circular. Kunik's logarithmic-derivative identity (2.39), valid for \(\Re s>1/2\), gives a concrete non-oracular interface to attack:

\[
\frac{B'(s)}{B(s)}
=
\frac{\zeta'(s)}{\zeta(s)}
-\frac1s+\frac1{s-1}
+\frac1\pi\int_{-\infty}^{\infty}
\frac{\log|\zeta(\frac12+iu)|}
{(s-\frac12-iu)^2}\,du.
\tag{9}
\]

A genuinely new bridge would have to control an appropriate boundary/localized norm of the left side from the prime-side or critical-line terms on the right, with all singular limiting terms accounted for independently of the unknown off-line zero set. No such estimate is proved here.

## 1. Exact Poisson boundary flux

Kunik's Blaschke factor for one zero \(\rho\) with \(\Re\rho>1/2\) is

\[
B_\rho(s)=
\frac{1-s/\rho}{1-s/(1-\bar\rho)}
\left|\frac{\rho}{1-\rho}\right|.
\]

The constant normalization disappears after logarithmic differentiation:

\[
\frac{B_\rho'(s)}{B_\rho(s)}
=
\frac1{s-\rho}
-
\frac1{s-(1-\bar\rho)}.
\tag{10}
\]

Put \(s=1/2+it\), \(\rho=1/2+d+i\gamma\), and \(u=t-\gamma\). Since \(1-\bar\rho=1/2-d+i\gamma\),

\[
\frac1{-d+iu}-\frac1{d+iu}
=-\frac{2d}{u^2+d^2}.
\tag{11}
\]

Summing (11) with multiplicities proves (1) for every finite subproduct. The same identity gives the boundary trace of the full product wherever Kunik's logarithmic derivative is defined; finite positive subproducts also provide a monotone interpretation when a limiting statement is preferable.

For the potential from `WI-423`, one factor is

\[
U_\rho(x,t)
=\frac12\log
\frac{(t-\gamma)^2+(d+x)^2}
     {(t-\gamma)^2+(d-x)^2}.
\tag{12}
\]

Differentiating at \(x=0^+\) gives

\[
\partial_xU_\rho(0^+,t)
=\frac{2d}{(t-\gamma)^2+d^2},
\tag{13}
\]

which proves (2). The map from the atomic Riesz source to the boundary flux is therefore exactly harmonic measure / the half-plane Poisson kernel, not an arbitrary regularization.

## 2. Kunik's finite-height count relation fixes the normalization

Kunik defines

\[
N_3(T)=
\frac1{2\pi}
\int_{-T}^{T}
\frac{B'(\frac12+iu)}{B(\frac12+iu)}\,du
\tag{14}
\]

in Theorem 2.5 and proves

\[
N_3(T)+N_B(T)=O(\log^2T).
\tag{15}
\]

Since \(h_B=-B'/B\) on the boundary, (14)--(15) are exactly (3). This independently checks both the sign and the factor \(2\pi\) in (1): one isolated Poisson profile has total mass

\[
\int_{\mathbb R}\frac{2d}{(t-\gamma)^2+d^2}\,dt=2\pi.
\tag{16}
\]

Equation (3) must not be read as an exact interval-by-interval localization of each zero. Poisson tails from ordinates outside \([-T,T]\) remain present. Kunik's theorem states that their aggregate effect, together with the boundary truncation, is absorbed in the displayed \(O(\log^2T)\) remainder for the symmetric counting function.

## 3. Exact norm and Fourier tariffs

For \(p>1/2\), substitute \(t-\gamma=du\) into the one-profile integral:

\[
\int_{\mathbb R}
\left(\frac{2d}{(t-\gamma)^2+d^2}\right)^pdt
=
2^pd^{1-p}
\int_{\mathbb R}(1+u^2)^{-p}\,du.
\tag{17}
\]

The beta integral

\[
\int_{\mathbb R}(1+u^2)^{-p}\,du
=
\sqrt\pi\,
\frac{\Gamma(p-\frac12)}{\Gamma(p)}
\tag{18}
\]

proves (4). For \(p\ge1\), all summands in (1) are nonnegative, so pointwise

\[
\left(\sum_j a_j\right)^p\ge\sum_j a_j^p,
\qquad a_j\ge0,
\tag{19}
\]

which gives (6). For infinite configurations this is interpreted through finite subcollections and monotone convergence; the full global norm may of course be infinite.

Under the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
\]

the classical Cauchy/Poisson transform is

\[
\boxed{
\widehat{h_{d,\gamma}}(\xi)
=2\pi e^{-d|\xi|}e^{-i\gamma\xi}.
}
\tag{20}
\]

Thus for a finite defect set

\[
\boxed{
\widehat h_F(\xi)
=2\pi\sum_{\rho\in F}
 m_\rho e^{-d_\rho|\xi|}e^{-i\gamma_\rho\xi}.
}
\tag{21}
\]

The boundary flux is a Laplace-damped exponential sum of off-line zeros. This gives a direct frequency-domain target for any explicit-formula or prime-side estimate, while making clear that the horizontal depths enter through the damping factors rather than disappearing.

For \(p=2\), write

\[
P_d(t)=\frac1\pi\frac{d}{t^2+d^2},
\qquad h_{d,\gamma}(t)=2\pi P_d(t-\gamma).
\]

The Poisson semigroup identity \(P_a*P_b=P_{a+b}\) gives

\[
\int_{\mathbb R}
h_{d,\gamma}(t)h_{e,\eta}(t)\,dt
=
4\pi\frac{d+e}{(\gamma-\eta)^2+(d+e)^2}.
\tag{22}
\]

Summing (22) proves (7); retaining only the diagonal terms gives (8). The pair terms are all positive, so clustering can only increase this boundary energy.

## 4. Consequence for the source-regularity frontier

The distinction from `WI-423` is structural. In the two-dimensional half-plane,

\[
-\Delta U
=2\pi\sum_\rho m_\rho\delta_{w_\rho}
\]

is atomic whenever a defect exists, so an exact planar \(L^p\) source would already imply RH. On the one-dimensional boundary, however,

\[
\partial_xU(0^+,t)
\]

is automatically a Poisson-smoothed density while preserving an exact counting relation. Boundary absolute continuity therefore does **not** hide RH in the hypothesis.

What remains hard is precisely measurable. An independently proved \(L^p\) upper bound with \(p>1\) would, through (6), bound

\[
\sum m_\rho^p d_\rho^{1-p},
\]

and the \(L^2\) case would control the stronger positive pair energy (7), including the reciprocal-depth diagonal (8). Such estimates would rule out increasingly shallow or clustered off-line configurations. Conversely, a bound obtained by first inserting the unknown Blaschke product or the same off-line zeros is only an oracle reformulation and supplies no new information.

Equation (9) makes the next falsifiable question concrete: can one take a controlled approach to \(\Re s=1/2\) in Kunik's exact interior identity and prove a localized norm or square-function estimate for the Blaschke term from independently accessible prime-side / critical-line data? A successful estimate must survive the singularities of \(\zeta'/\zeta\), the differentiated Poisson-Schwarz term, and boundary limiting; failure of every such independent estimate would close this boundary-source route without affecting the exact identities above.

This finding does not yet couple the boundary \(L^p\) tariff to the translated planar probe inequalities of `WI-417`--`WI-422`. That transport is a separate theorem and must not be assumed. The immediate redirect is narrower: after `WI-423`, **the natural canonical regular object is boundary Poisson flux rather than planar Riesz density**, and its useful regularity thresholds have explicit horizontal-depth prices.

## Prior art and novelty audit

No priority claim is made for the analytic ingredients.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829v2 (2009), gives the half-plane factorization (1.2)--(1.4), defines \(N_3\) by the critical-line logarithmic derivative of the Blaschke product in (2.34), proves \(N_3+N_B=O(\log^2T)\) in (2.36), and gives the interior logarithmic-derivative identity (2.39). Those are the primary-source inputs behind (3), (9), and (14)--(15).
- The appearance of the Poisson kernel as the boundary derivative of a half-plane Green/Blaschke factor, its Fourier transform, the semigroup law \(P_a*P_b=P_{a+b}\), and the beta-integral norm are classical harmonic-analysis identities. Kunik himself places the factorization in the Hardy-space/Poisson-Schwarz tradition and cites Koosis, Hoffman, and Garnett.
- `WI-423` already identifies the canonical planar Riesz source with the atomic off-line zero measure. The repository-local delta here is not a new Blaschke theorem: it is the exact boundary reformulation relevant to the current Mathia frontier, together with the explicit \(d^{1-p}\) norm tariff, the positive \(L^2\) pair energy, and the identification of Kunik (2.39) as the non-oracular interface that would have to supply an independent norm budget.

The literature search did not reveal a zeta-specific theorem turning Kunik's boundary logarithmic derivative into the above \(L^p\) or square-function estimate from independent prime-side data. Absence from this search is not used as a novelty claim.

## Boundary and falsification

- The exact formulas (1), (4), (7), (20), and (22) are stated first for finite Blaschke subproducts, where convergence is not an issue. Full-product assertions use Kunik's boundary logarithmic derivative / limiting framework.
- Global \(L^p\) norms of the full flux need not be finite; the norm tariffs are exact finite-configuration statements and lower bounds for any limiting norm when such a norm is controlled.
- Equation (3) is Kunik's symmetric finite-height asymptotic count, not a claim that Poisson kernels have compact support.
- Critical-line zeros do not contribute to this Blaschke flux. The construction measures the off-line component, not multiplicity or simplicity on the line.
- Functional-equation symmetry means it suffices to encode the \(\Re\rho>1/2\) half of each off-line orbit; the left-half-plane partners are not independent missing mass.
- Boundary absolute continuity alone has no coercive content: every individual atomic defect already produces a smooth Poisson profile. Any useful theorem must control a stronger norm, frequency band, concentration functional, or comparable quantity from independent data.
- No new lower bound for the proportion of simple critical zeros and no defect-to-zero bootstrap is claimed here.

A direct algebraic error in (10)--(13), a normalization/sign conflict with Kunik's (2.34)--(2.36), or a failure of the Poisson semigroup calculation would falsify the exact part of the finding. The primary-source sign check in (14)--(16) and the diagonal check \(\|h_{d,\gamma}\|_2^2=2\pi/d\) provide independent internal controls.

## Evidence state

- Kunik factorization, finite-height count relation, and logarithmic-derivative representation: `LITERATURE` / primary source.
- Boundary Poisson-kernel derivative, Fourier transform, beta-integral norm, and Poisson semigroup identity: `CLASSICAL-IDENTITY`.
- Zeta specialization (1)--(8), reciprocal-depth tariff, and positive pair energy: `EXACT-DERIVED`.
- Reorientation from impossible planar source regularity to boundary-flux norm control: `PRIOR-ART-REDIRECT`.

No RH assumption, conjectural zero statistics, wider Fourier support, unproved higher moment, numerical certificate, or floating-point computation is used.