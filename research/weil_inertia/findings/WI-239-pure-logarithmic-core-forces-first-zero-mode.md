# WI-239 — The pure logarithmic core already has a finite first zero mode

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-238 identifies a source-side endgame that avoids Bombieri's cofinal coefficient-escape problem: if RH fails, Suzuki's localized Weil operator has a first finite support radius at which its lowest eigenvalue reaches zero. A natural next hope is that continuity, nested support domains, compact resolvent, positivity below the first radius, parity, or the universal logarithmic singularity might themselves make such a crossing impossible.

They do not. The universal logarithmic core of Suzuki's zeta kernel already has exactly that behavior. Put

\[
g_0(t)=\frac12|t|\log|t|,\qquad g_0(0)=0.
\tag{1}
\]

If `A_{0,a}` is the self-adjoint operator associated with its localized closed quadratic form on `(-a,a)`, then after unitary dilation to `(-1,1)` its entire spectrum translates rigidly:

\[
\boxed{\lambda_{0,k}(a)=\mu_k-1-\log a,}
\tag{2}
\]

where `mu_k` are the eigenvalues of Suzuki's fixed logarithmic form `\overline{\mathcal L}`. Hence

\[
\boxed{\lambda_{0,1}(a)=\mu_1-1-\log a}
\tag{3}
\]

has the unique finite first zero

\[
\boxed{a_0^*=e^{\mu_1-1}.}
\tag{4}
\]

The zero is attained, and the ground state is simple, positive almost everywhere, and even. Therefore the abstract first-crossing package isolated after WI-238 is not coercive. Any localized-Weil proof that excludes RH failure must use genuinely zeta-specific information beyond the logarithmic core: the exact archimedean correction and/or the finite-prime translation/autocorrelation terms.

This is not a counterexample to Suzuki/Yoshida nondegeneracy for the actual zeta kernel. It is a countermodel to an *abstract* `first crossing + compactness + universal singularity => contradiction` strategy.

## 1. Exact core form

Suzuki's 2026 operator formulation writes the zeta screw function near the origin as

\[
g(t)=\frac12|t|\log|t|+A|t|
+\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n)+r(t),
\tag{5}
\]

with explicit `A` and an even `C^2` remainder `r`. Thus (1) is precisely the universal singular term.

For `v\in H_0^1(-a,a)`, define

\[
Q_0^a(v)=\frac12\int_{-a}^{a}\int_{-a}^{a}
|x-y|\log|x-y|\,v'(y)\overline{v'(x)}\,dx\,dy.
\tag{6}
\]

Suzuki proves the exact identities

\[
\int\!\!\int |x-y|v'(y)\overline{v'(x)}\,dx\,dy=-2\|v\|_2^2,
\tag{7}
\]

\[
\int\!\!\int |x-y|\log|x-y|v'(y)\overline{v'(x)}\,dx\,dy
=2\mathcal L_a(v)-2\|v\|_2^2.
\tag{8}
\]

Consequently

\[
\boxed{Q_0^a(v)=\mathcal L_a(v)-\|v\|_2^2.}
\tag{9}
\]

This is exact, not a small-`a` asymptotic.

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), especially equations (1.3), (2.2)--(2.7), Theorem 1.1, Sections 4--5: <https://arxiv.org/abs/2606.09096>.

## 2. Dilation gives the full spectrum exactly

Set `w(t)=v(at)` on `(-1,1)`. Then `\|v\|_2^2=a\|w\|_2^2`. Substitution `x=a\xi`, `y=a\eta` into (6), followed by (7)--(8) on the fixed interval, gives

\[
Q_0^a(v)
=a\left[\mathcal L(w)-(1+\log a)\|w\|_2^2\right].
\tag{10}
\]

Therefore

\[
\boxed{
\frac{Q_0^a(v)}{\|v\|_2^2}
=\frac{\mathcal L(w)}{\|w\|_2^2}-1-\log a.
}
\tag{11}
\]

Let `T` be the self-adjoint operator associated with `\overline{\mathcal L}` on `L^2(-1,1)`. Suzuki proves that its form domain embeds compactly into `L^2`, so `T` has discrete spectrum

\[
\mu_1\le\mu_2\le\cdots\to\infty.
\tag{12}
\]

Under unitary dilation, (10) is the exact operator identity

\[
\boxed{A_{0,a}\simeq T-(1+\log a)I,}
\tag{13}
\]

which proves (2).

The `-\log a` dilation law is standard logarithmic-Laplacian structure. Laptev--Weth prove the analogous exact eigenvalue scaling `\lambda_k(R\Omega)=\lambda_k(\Omega)-\log R` for their Dirichlet `\frac12\log(-\Delta)` problem (their paper treats `d\ge2`). The present one-dimensional identity (13) does **not** rely on extending their theorem to `d=1`; it follows directly from Suzuki's one-dimensional form and (7)--(10). The prior-art point is only that rigid logarithmic spectral translation under dilation is classical, not a Mathia novelty.

Prior art: Ari Laptev and Tobias Weth, **Spectral properties of the logarithmic Laplacian**, *Analysis and Mathematical Physics* 11 (2021), article 133, DOI `10.1007/s13324-021-00527-y`; arXiv:2009.03395, especially Lemma 2.5: <https://arxiv.org/abs/2009.03395>.

## 3. The core has a genuine first crossing

Suzuki proves

\[
\mu_1=\inf_{\|w\|_2=1}\overline{\mathcal L}(w)>0,
\tag{14}
\]

and that the associated semigroup is positivity improving. Hence the first eigenvalue is simple and its eigenfunction may be chosen positive almost everywhere; reflection symmetry then makes it even.

Equation (3) now gives

\[
\lambda_{0,1}(a)\to+\infty\quad(a\downarrow0),
\qquad
\lambda_{0,1}(a)\to-\infty\quad(a\to\infty),
\tag{15}
\]

with derivative `-1/a`. Thus (4) is the unique first crossing and

\[
\lambda_{0,1}(a)>0\ (a<a_0^*),\qquad
\lambda_{0,1}(a_0^*)=0,\qquad
\lambda_{0,1}(a)<0\ (a>a_0^*).
\tag{16}
\]

Because the spectrum is discrete, there is an actual nonzero ground state `v_*` with

\[
A_{0,a_0^*}v_*=0.
\tag{17}
\]

So one exact model simultaneously has: a continuous real even kernel with the same leading logarithmic singularity as the zeta screw function; nested support domains; positivity at every smaller radius; compact resolvent; an attained first zero mode; simple/even ground state; and no prime data at all. None of those generic properties can be the missing contradiction in WI-238.

## 4. The whole core inertia drifts through zero

Equation (2) gives a sharper inertia statement. Every eigenvalue branch crosses once at

\[
a_k^*=e^{\mu_k-1},
\tag{18}
\]

and therefore

\[
\boxed{
n_-(A_{0,a})=\#\{k:\mu_k<1+\log a\}.
}
\tag{19}
\]

The universal core naturally accumulates negative directions as the support radius grows. If the actual zeta operator remains nonnegative for all radii, its zeta-specific terms must compensate a core whose spectral floor is driven downward by `-\log a`. This exact inertia drift is the reason the countermodel is directly relevant to the `weil_inertia` mandate.

## 5. What the actual zeta problem must use

Suzuki's fixed-interval scaled Rayleigh form can be decomposed as

\[
q_a(w)
=\overline{\mathcal L}(w)-(1+\log a)\|w\|_2^2+b_a(w),
\tag{20}
\]

where `b_a` is the zeta-specific remainder relative to the pure core. In Suzuki's explicit formula it consists of the archimedean constant/smooth remainder and a finite sum of prime-power translation terms with `\log n\le2a`. On compact `a`-ranges these are bounded form perturbations; in the continuity proof the prime part is a finite sum of translation operators and the smooth part is a continuous-kernel integral operator.

The first-crossing question is therefore not whether a nested compact family *can* reach zero: (13)--(17) answer yes. The useful target is whether the actual `b_a`, coupled to the zero-mode equation and positivity at all smaller radii, can be shown to forbid that crossing. At least one genuinely zeta-specific ingredient must enter. Finiteness of the prime source by itself is not coercive: the countermodel uses zero primes and still crosses.

## 6. A necessary first-crossing support constraint survives

There is a simple exact rigidity statement for the actual zeta first crossing. Suppose `a_*` is the first radius with `\lambda_{a_*}=0` and `v_*\ne0` is a zero mode. Then `v_*` cannot be supported in a strict interior interval `[-b,b]` with `b<a_*`. Otherwise zero extension identifies the same test vector at radius `b` and gives

\[
Q_W^b(v_*)=Q_W^{a_*}(v_*)=0,
\tag{21}
\]

contradicting `\lambda_b>0`. A parity-pure zero-mode component obeys the same conclusion.

This is genuine rigidity, but it does not rescue the abstract route: the pure logarithmic ground state is compatible with the same no-interior-support condition at its crossing.

## 7. Prior-art and novelty audit

The load-bearing pieces separate cleanly.

- **Established Suzuki theory:** the screw-function decomposition, localized closed operator, logarithmic form, identities (7)--(9), compact embedding, and fixed-interval scaling framework are literature-backed. WI-238 already records the finite first-degeneracy consequence for the actual zeta form.
- **Classical logarithmic spectral scaling:** rigid logarithmic eigenvalue translation under spatial dilation is established prior art; Laptev--Weth supplies an independent higher-dimensional Dirichlet instance. No novelty is claimed for that phenomenon.
- **Mathia deduction:** specializing Suzuki's exact one-dimensional core and using its direct dilation identity gives (13)--(19). The substantive new conclusion for this line is the falsification boundary: the generic first-crossing features highlighted after WI-238 are jointly insufficient, because the universal core itself realizes all of them while producing a zero mode.

A targeted prior-art search located Suzuki's decomposition and classical logarithmic-Laplacian scaling, but no source was found that formulates this pure-core family as the specific no-go boundary for the localized-Weil RH strategy. Search absence is not asserted as priority.

## 8. Boundaries

1. `g_0` is not the zeta screw function, so this does not refute the Weil criterion or Suzuki/Yoshida nondegeneracy.
2. No sign is asserted for `b_a`; its prime and archimedean pieces can have mixed behavior on arbitrary states.
3. Fixed-radius finite-prime dependence does not make the actual operator finite-dimensional.
4. No numerical relation between `a_0^*` and a hypothetical zeta first crossing is claimed.
5. The barrier applies to arguments using only nested domains, continuity, compactness, parity, or universal logarithmic scaling. Exact prime hinges, arithmetic identities, the full screw-function structure, or another zeta-specific invariant remain open routes.
6. The constant `-1` in (2)--(3) is tied to the normalization `g_0=\frac12|t|\log|t|` and Suzuki's identities; it must not be mixed with conventions whose Fourier symbol is `2\log|\xi|`.

## Consequence for the research line

WI-238 remains a valid and useful localization of RH failure, but **firstness itself cannot be the contradiction**. The next source-side program should treat the logarithmic core (13) as an exactly solvable baseline and isolate a coercive zeta-specific quantity in `b_a`. Any proposed proof that never uses more than the generic spectral package above should be killed immediately by (13)--(19).