# WI-238 — Suzuki localization turns any RH failure into a finite-prime zero mode

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

WI-236 and WI-237 isolate a genuine difficulty in Bombieri's zero-side finite truncations: although every finite off-line packet is detected by exact negative inertia, a cofinal negative eigensequence can lose spectral margin and coefficient mass in the infinite limit, and the resulting interval-exponential relation cannot be excluded by a raw span or Riesz argument. A separate established localization theorem shows that this passage-to-limit problem is **not the only route from an individual RH failure to a finite spectral obstruction**.

Suzuki's peer-reviewed 2023 screw-function theorem proves that RH is equivalent to nondegeneracy, for every finite support radius `a`, of a self-adjoint Hilbert--Schmidt integral operator with continuous kernel built from the Weil explicit formula. In the proof of the converse, if RH is false there is a **finite first radius** `a_0` at which the localized form degenerates. Suzuki's 2026 operator-theoretic refinement represents the localized Weil form by a lower-bounded self-adjoint operator `A_a` with discrete spectrum, proves continuity of its lowest eigenvalue `lambda_a`, and states explicitly that RH failure forces `lambda_a<0` for some finite `a`; since `lambda_a>0` for sufficiently small `a`, a finite zero crossing follows.

The exact source formula gives one additional structural consequence useful for this line: for fixed `a`, the relevant continuous kernel is determined by the von Mangoldt data only up to `n <= exp(2a)` (plus explicit archimedean terms). Thus a hypothetical off-critical zero anywhere in the global divisor forces a **source-side, finite-prime, finite-support zero mode**. This does not prove RH, because excluding that zero mode for every `a` is itself an RH-equivalent problem. It does, however, materially redirect the sparse-defect program: coefficient tightness for Bombieri's cofinal zero-side eigenvectors is one possible bridge, not a logically necessary bridge. A second exact target is finite-radius source-side nondegeneracy.

## 1. Peer-reviewed finite-radius nondegeneracy criterion

Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, Journal of the London Mathematical Society 107 (2023), develops a continuous kernel `G_g(t,u)` from the zeta screw function `g`. For every `a>0`, he defines the Hermitian form on `L^2(-a,a)` and the corresponding integral operator

\[
(\mathsf G_g[a]\phi)(t)
=
\int_{-a}^{a}G_g(t,u)\phi(u)\,du.
\tag{1}
\]

The kernel is continuous and Hermitian, so `\mathsf G_g[a]` is self-adjoint and Hilbert--Schmidt. Suzuki's Theorem 1.4 states

\[
\boxed{
\mathrm{RH}
\iff
\mathsf G_g[a]\text{ has no zero eigenvalue for every }a>0.
}
\tag{2}
\]

This is an established theorem, not a Mathia deduction. It is presented by Suzuki as an analogue, in a simpler continuous-kernel Hilbert space, of Yoshida's earlier nondegeneracy criterion for localized Weil forms.

The sufficiency proof is especially relevant to the present line. Let `A` be the set of support radii on which the localized form is nonnegative definite and `B=(0,\infty)\setminus A`. Suzuki proves that `B` is open by continuity of the kernel, while the small-radius theory gives a nonempty initial positive regime. If RH is false, his localized positivity theorem implies that `A` is bounded. Hence `A` has a maximal boundary point `a_0>0`, and Section 5.2 proves that the form degenerates there. In particular,

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\exists a_0\in(0,\infty),\ \exists 0\ne\phi\in L^2(-a_0,a_0):
\mathsf G_g[a_0]\phi=0.
}
\tag{3}
\]

Equation (3) is stronger, for the present diagnostic purpose, than merely saying that the full Weil form is eventually indefinite: an arbitrary global RH failure is forced to leave a zero-mode obstruction at one finite localization radius.

Primary source: Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *J. London Math. Soc.* 107 (2023), DOI `10.1112/jlms.12785`, especially Theorems 1.3--1.4 and Sections 5.1--5.2: <https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12785>.

## 2. The 2026 self-adjoint ground-state formulation

Suzuki's later preprint *Weil's quadratic form via the screw function* gives a more direct operator formulation of the same finite-support transition. It starts from the continuous real even function

\[
g(t)=\text{explicit archimedean terms}
+\sum_{n\le e^{|t|}}
\frac{\Lambda(n)}{\sqrt n}(|t|-\log n),
\tag{4}
\]

with the signs and remaining explicit terms fixed in his equation (1.3). Let `G` be convolution by `g`, let `P_a` be the projection onto the mean-zero subspace of `L^2(-a,a)`, and put

\[
G_a=P_aGP_a.
\tag{5}
\]

With `D=i\,d/dx`, Suzuki defines

\[
B_a=D^*G_aD
\tag{6}
\]

on `H_0^1(-a,a)`. His Theorem 1.1 identifies the canonical self-adjoint operator `A_a` representing the localized closed Weil form with the Friedrichs extension of `B_a`. The spectrum of `A_a` is lower bounded and discrete, and its lowest spectral value

\[
\lambda_a
=
\inf_{0\ne v}
\frac{Q_W^a(v)}{\|v\|_2^2}
\tag{7}
\]

is an attained eigenvalue. Corollary 1.2 identifies the same infimum over compactly supported smooth test functions.

Theorem 1.3 then proves unconditionally that

\[
\boxed{a\longmapsto\lambda_a\text{ is continuous}.}
\tag{8}
\]

Suzuki immediately records the RH consequence: `lambda_a>0` for sufficiently small `a`; if RH is false, then `lambda_a<0` for some finite `a`; hence continuity produces a finite radius at which `lambda_a=0`. This is explicitly described as another proof of Yoshida's nondegeneracy equivalence.

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), current manuscript dated 19 Aug 2026 in the HTML source, especially Theorems 1.1 and 1.3, Corollary 1.2, and equations (1.3)--(1.8): <https://arxiv.org/abs/2606.09096>.

## 3. Exact monotonicity sharpens the crossing into a first threshold

There is an elementary consequence not needed for Suzuki's theorem but useful for the WI program. If `0<a<b`, extend a function supported in `(-a,a)` by zero to `(-b,b)`. The global Weil quadratic form and the `L^2` norm do not change under that extension. Therefore the variational classes are nested and

\[
\boxed{
\lambda_b\le\lambda_a
\qquad(0<a<b).
}
\tag{9}
\]

Thus `lambda_a` is not only continuous by (8), but nonincreasing by the definition of the localized Rayleigh infimum.

Assume RH is false and define

\[
a_*:=\inf\{a>0:\lambda_a\le0\}.
\tag{10}
\]

The small-radius positivity and eventual negativity give

\[
0<a_*<\infty.
\tag{11}
\]

Continuity and monotonicity imply the exact threshold statement

\[
\boxed{
\lambda_a>0\ (a<a_*),
\qquad
\lambda_{a_*}=0,
\qquad
\lambda_a\le0\ (a>a_*),
}
\tag{12}
\]

with strict negativity at least at some finite radius beyond `a_*`. Since the ground state of `A_{a_*}` is attained, there is a nonzero `v_*` satisfying

\[
\boxed{
A_{a_*}v_*=0,
\qquad
Q_W^{a_*}(v_*)=0.
}
\tag{13}
\]

The existence of such a first threshold is therefore an exact finite-support consequence of RH failure. No limiting sequence of zero ordinates or Bombieri truncation eigenvectors is required to state it.

## 4. Fixed support means finite prime information

Equation (4) makes the arithmetic locality explicit. In the kernel of `G_a`, both variables lie in `[-a,a]`, so every difference obeys

\[
|x-y|\le2a.
\tag{14}
\]

For such differences the von Mangoldt sum in `g(x-y)` contains only

\[
n\le e^{|x-y|}\le e^{2a}.
\tag{15}
\]

The projections and the differential/Friedrichs construction do not introduce values of `g` outside the same difference range. Hence, for each fixed `a`, the localized source-side form is determined by

\[
\boxed{
\{\Lambda(n):n\le e^{2a}\}
}
\tag{16}
\]

plus explicit archimedean terms. The same finite-prime character is emphasized independently in the modern Connes--Consani--Moscovici spectral-triple program, where the corresponding finite-scale constructions use Euler-product data only up to the scale parameter.

Combining (12)--(16) yields the structural statement relevant here:

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\text{a finite radius }a_*
\text{ at which a finite-prime localized Weil operator has a nonzero zero mode.}
}
\tag{17}
\]

`Finite-prime` in (17) refers to the **source data entering the fixed-radius kernel**, not to finite-dimensionality. `A_{a_*}` acts on an infinite-dimensional Hilbert space, and proving that its kernel is trivial remains a genuinely analytic spectral problem.

## 5. Why this materially changes the WI passage-to-limit diagnosis

WI-236 correctly shows that Bombieri's finite negative index already detects every finite off-line packet and that the missing implication in that particular zero-side truncation scheme is coercive passage to a nonzero full-Weil witness. WI-237 correctly shows that generic interval-exponential linear independence or a positive `L^2` angle cannot supply that coercivity; the remaining Bombieri-side currency is coefficient budget plus, for infinitely many off-line zeros, height tightness.

Equations (3) and (17) expose a different exact route:

\[
\text{RH failure}
\Longrightarrow
\text{finite localized source operator reaches a zero mode}.
\tag{18}
\]

Therefore a theorem closing RH need not first establish a uniform negative margin for Bombieri's cofinal zero-side matrices, nor prove the coefficient-cost inequality proposed in WI-237. Those remain legitimate approaches, but they are not logically forced by individual-defect detectability. An alternative is to prove **source-side nondegeneracy at every finite radius**, or to exploit the special first-crossing structure (12)--(13).

This is a prior-art redirect rather than a claimed new RH criterion. Suzuki and Yoshida already prove the nondegeneracy equivalence. The Mathia contribution is the exact integration of that criterion with the WI-236/WI-237 sparse-defect diagnosis, the nested-ground-state threshold (9)--(13), and the finite-prime locality statement (14)--(17).

## 6. Relation to the quantitative Montgomery/Weil inertia program

This finding does not improve the current unconditional simple-critical proportion, and it does not identify the uncertified complement. Its relevance is at the mandate's endgame: a zero-density or even finite exceptional set is invisible to normalized bulk moments, while the localized source operator cannot hide a genuine RH failure forever. Any failure creates a finite `a_*` at which the bottom eigenvalue reaches zero.

That suggests a different quantitative question from the existing percentage bootstraps. Instead of asking only for a density-level defect charge, ask whether the source formula can impose a **strict finite-radius coercivity reserve** preventing (13). Because `a_*` is a first crossing, any such argument may use information unavailable in an arbitrary indefinite form: positivity for every smaller radius, the explicit continuous kernel, and the finite-prime structure at radius `a_*`.

A concrete future target is therefore:

\[
\boxed{
\text{derive from the source kernel and prior positivity on }(0,a)
\text{ a contradiction to }\ker A_a\ne\{0\}.
}
\tag{19}
\]

Equation (19) is a research target, not an established theorem. It is also much closer to global Weil positivity than the Montgomery--Taylor bulk bound, so work on it must preserve this line's scope boundary: the present finding records an exact localization/inertia consequence and does not assume the positivity that RH asks one to prove.

## 7. Prior-art audit and provenance

The load-bearing provenance is as follows.

- H. Yoshida, **On Hermitian Forms attached to Zeta Functions**, in *Zeta Functions in Geometry*, Advanced Studies in Pure Mathematics 21 (1992), 281--325. Classical localized nondegeneracy route; Suzuki explicitly compares his theorems with Yoshida's Theorem 2 and related propositions.
- Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, *Rend. Lincei Mat. Appl.* 11 (2000), 183--233. Classical variational/localized Weil-form and finite-zero-side truncation framework underlying WI-236/WI-237.
- Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *J. London Math. Soc.* 107 (2023), DOI `10.1112/jlms.12785`. Theorem 1.4 and Section 5.2 are the primary established source for the finite-radius degeneracy implication (3).
- Alain Connes and Caterina Consani, **Spectral triples and zeta-cycles**, *Enseign. Math.* 69 (2023), 93--148, DOI `10.4171/LEM/1049`. Established localized Weil/spectral framework and finite-scale small-eigenvalue program.
- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026). Theorems 1.1 and 1.3 and Corollary 1.2 provide the self-adjoint `A_a` realization and unconditional continuity of its ground-state eigenvalue.
- Alain Connes, Caterina Consani and Henri Moscovici, **Zeta Spectral Triples**, arXiv:2511.22755 (2025; published in the EMS lecture series in 2026). Context for finite-prime spectral constructions; its conjectural convergence statements are **not** used as evidence for (17).

A targeted audit found that the decisive nondegeneracy/first-degeneracy mechanism is already explicit in Suzuki 2023 and is refined operator-theoretically in Suzuki 2026. Therefore no novelty claim is made for the RH-equivalent criterion, the existence of a finite degeneracy radius, or the broad finite-scale spectral program. The new content recorded by WI-238 is the WI-specific logical relocation: Bombieri coefficient escape is a bottleneck of one zero-side truncation architecture, not a necessary bottleneck for converting a sparse individual RH failure into finite spectral data.

## 8. Adversarial boundaries and falsification

1. **Equation (17) is not progress toward proving nondegeneracy by itself.** Showing that `A_a` has no zero mode for every `a` is RH-equivalent. The finding changes the location of the missing theorem; it does not supply it.

2. **Finite-prime does not mean finite-dimensional.** At fixed `a`, only finitely many von Mangoldt values enter the continuous kernel, but the localized operator still acts on an infinite-dimensional function space. No determinant of a fixed finite matrix is asserted to decide RH at that radius.

3. **The critical radius is not tied here to a particular off-line zero.** Equations (10)--(17) are global consequences of RH failure through the Weil criterion. They do not provide a formula `a_*=a(\rho)` or a lower bound in terms of the horizontal depth of an offending zero.

4. **Do not import conjectural spectral convergence.** The Connes--Consani--Moscovici finite-matrix spectra and Suzuki's large-interval Hilbert--Polya limit are contextual. Their unproved convergence is not needed for the exact localization statements above and is not upgraded here.

5. **Bombieri's coefficient-budget problem remains genuine inside Bombieri's truncation.** WI-238 supplies an alternative source-side route; it does not refute WI-236 or WI-237 and does not magically make their limiting eigenvectors tight.

6. **Monotonicity uses the actual localized Weil Rayleigh problem.** It must not be transferred to unrelated finite matrix approximations whose trial spaces or normalizations are not nested by zero extension.

7. **The source locality scale is `exp(2a)`.** The factor two comes from `|x-y|<=2a` on `[-a,a]^2`. Replacing it by `exp(a)` without changing the support convention would be an error.

8. **This line remains complementary to global Weil positivity.** The finding may motivate source-side first-crossing analysis, but routine WI research must not silently assume full Weil positivity or read another Mathia line outside an explicit grant.

## Consequence for the research line

The current sparse-defect endgame should maintain two distinct coercivity targets. The Bombieri target is to prevent negative zero-side eigenvectors from losing spectral margin/coefficient mass as the truncation grows. The Suzuki/Yoshida target is to prevent the **finite-radius first zero mode** of the localized source-side Weil operator. The latter has a key structural advantage: any RH failure is forced into a finite support radius and uses only finitely many prime powers in its kernel.

Accordingly, a future clue or research pass should first ask whether positivity on every smaller radius constrains a putative kernel vector at the first crossing strongly enough to derive an exact source-side contradiction. If no such first-crossing coercivity exists, proving that barrier would itself materially narrow the RH program.