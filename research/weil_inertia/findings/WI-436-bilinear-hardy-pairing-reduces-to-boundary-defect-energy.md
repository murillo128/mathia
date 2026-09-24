# WI-436 — the canonical bilinear Hardy pairing is exactly the boundary defect energy

Status: `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-BARRIER + STRUCTURAL-REDIRECTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parents: `WI-424`, `WI-429`, `WI-431`, `WI-435`

## Claim

`WI-435` leaves mixed positive/negative-frequency functionals as one possible way to add information not already contained in the one-sided Hardy transport. The most canonical translation-invariant mixed functional can be evaluated exactly, and it does **not** supply an independent source channel: for a finite Kunik Blaschke block, it is identically the already-known positive boundary defect energy from `WI-424`.

Let

\[
\rho_j=\frac12+d_j+i\gamma_j,\qquad d_j>0,
\]

be a finite set of right-half zeros with multiplicities \(m_j\), and let \(B_F\) be the corresponding finite Kunik Blaschke product. Put

\[
G_{F,a}(t):=
\frac{B_F'(\frac12+a+it)}{B_F(\frac12+a+it)},
\qquad
0<a<d_*:=\min_j d_j.
\tag{1}
\]

Thus the probe line lies strictly between the critical boundary and every direct zero in the finite block. Let

\[
h_F(t):=-\frac{B_F'(\frac12+it)}{B_F(\frac12+it)}
\tag{2}
\]

be the positive Poisson boundary flux from `WI-424`. Then the **non-Hermitian square** of the interior logarithmic derivative has the exact line-invariant value

\[
\boxed{
\int_{\mathbb R}G_{F,a}(t)^2\,dt
=
\|h_F\|_2^2.
}
\tag{3}
\]

There is no complex conjugation on the left. In particular, the integral is nevertheless real and positive in the whole zero-free strip \(0<a<d_*\), and `WI-424`'s pair identity gives

\[
\boxed{
\int_{\mathbb R}G_{F,a}(t)^2\,dt
=
4\pi
\sum_{j,k}
 m_jm_k
\frac{d_j+d_k}
{(\gamma_j-\gamma_k)^2+(d_j+d_k)^2}.
}
\tag{4}
\]

Hence

\[
\boxed{
\int_{\mathbb R}G_{F,a}(t)^2\,dt
\ge
2\pi\sum_j\frac{m_j^2}{d_j}
>
4\pi\sum_j m_j.
}
\tag{5}
\]

The last strict inequality uses the classical critical-strip bound \(d_j<1/2\). Thus this bilinear observable carries a full boundary reciprocal-depth tariff, twice the one-sided Hardy diagonal tariff at the boundary.

More importantly for the live `WI-435` frontier, (3) is exactly an opposite-Hardy pairing. With the same Fourier convention as `WI-429`, write

\[
G_{F,a}=G_++G_-,\qquad G_\pm=P_\pm G_{F,a}.
\]

Since \(G_+\) and \(G_-\) have strictly positive and negative Fourier support, respectively,

\[
\int_{\mathbb R}G_+(t)^2dt
=
\int_{\mathbb R}G_-(t)^2dt
=0.
\tag{6}
\]

Therefore

\[
\boxed{
2\int_{\mathbb R}G_+(t)G_-(t)\,dt
=
\|h_F\|_2^2.
}
\tag{7}
\]

This is the simplest translation-invariant bilinear coupling of the two Hardy half-spaces. It survives broad height localization: if \(\chi_T(t)=\chi(t/T)\), with \(\chi(0)=1\), \(|\chi|\le C\), and \(\chi_T\to1\) pointwise, then

\[
\boxed{
2\int_{
\mathbb R}
P_+(\chi_TG_{F,a})(t)
P_-(\chi_TG_{F,a})(t)\,dt
\longrightarrow
\|h_F\|_2^2.
}
\tag{8}
\]

Thus the obvious bilinear mixed-frequency escape from `WI-435` is **not** killed by Hardy orthogonality; it sees the defect perfectly. But that is precisely the obstruction: the finite Blaschke countermodel saturates it exactly. The functional is only a repackaging of the canonical inner-factor defect energy, not an independently controlled arithmetic/source quantity.

Consequently, a viable mixed-frequency bootstrap must add structure that is not already determined by the finite inner factor. Examples of logically adequate category changes include a non-translation-invariant/Hankel-type coupling with an independently justified zeta-specific symbol, a genuinely nonlinear arithmetic relation between the two frequency channels, or an explicit-formula observable whose upper bound is fixed without importing the same Blaschke divisor. Merely replacing the Hermitian Hardy norm by the canonical nonconjugated cross pairing does not escape the `WI-435` finite-block control.

## 1. Contour proof of the line-invariant square identity

Shift the critical line to the imaginary axis. For

\[
w_j=d_j+i\gamma_j,\qquad w_j^*=-d_j+i\gamma_j,
\]

Kunik's one-zero logarithmic derivative gives

\[
\mathcal G_F(z)
:=
\frac{B_F'(\frac12+z)}{B_F(\frac12+z)}
=
\sum_j m_j
\left(
\frac1{z-w_j}-
\frac1{z-w_j^*}
\right).
\tag{9}
\]

If \(0<a<d_*\), the closed strip

\[
0\le \Re z\le a
\]

contains neither a direct pole \(w_j\) nor a reflected pole \(w_j^*\). Hence \(\mathcal G_F(z)^2\) is holomorphic throughout that strip.

Each paired summand in (9) has cancellation at infinity:

\[
\frac1{z-w_j}-\frac1{z-w_j^*}
=
\frac{w_j-w_j^*}
{(z-w_j)(z-w_j^*)}
=O(|\Im z|^{-2})
\tag{10}
\]

uniformly for \(0\le\Re z\le a\). Therefore \(\mathcal G_F(z)^2=O(|\Im z|^{-4})\), and the horizontal sides of a rectangle with vertices \(\pm iR\) and \(a\pm iR\) contribute \(o(1)\) as \(R\to\infty\). Cauchy's theorem then gives

\[
\int_{\mathbb R}\mathcal G_F(a+it)^2dt
=
\int_{\mathbb R}\mathcal G_F(it)^2dt.
\tag{11}
\]

On the boundary, `WI-424` gives

\[
\mathcal G_F(it)=-h_F(t),
\tag{12}
\]

so (11) becomes (3). This proof uses only the finite Kunik factor and ordinary contour deformation in a pole-free strip; no limiting full-product assertion is hidden in it.

Substituting `WI-424`'s exact positive pair formula

\[
\|h_F\|_2^2
=4\pi
\sum_{j,k}m_jm_k
\frac{d_j+d_k}
{(\gamma_j-\gamma_k)^2+(d_j+d_k)^2}
\tag{13}
\]

proves (4). Keeping only \(j=k\) yields

\[
\|h_F\|_2^2
\ge
2\pi\sum_j\frac{m_j^2}{d_j},
\tag{14}
\]

and \(d_j<1/2\), \(m_j^2\ge m_j\), give (5).

For one zero of multiplicity \(m\), (3) specializes to the transparent identity

\[
\boxed{
\int_{\mathbb R}
\left(
\frac{m}{a-d+i(t-\gamma)}
-
\frac{m}{a+d+i(t-\gamma)}
\right)^2dt
=
\frac{2\pi m^2}{d},
\qquad 0<a<d.
}
\tag{15}
\]

The right side is independent of the probe depth \(a\). By contrast, the Hermitian one-sided energy from `WI-429` is \(\pi m^2/(d-a)\). The invariance in (15) comes from coupling the direct positive-frequency pole to its reflected negative-frequency partner rather than taking an absolute square of only one half-space.

## 2. Exact Hardy cross-pairing

For \(f,g\in L^2(\mathbb R)\) with products in \(L^1\), the nonconjugated Parseval identity under the repository convention is

\[
\int_{\mathbb R}f(t)g(t)dt
=
\frac1{2\pi}
\int_{\mathbb R}
\widehat f(\xi)\widehat g(-\xi)d\xi.
\tag{16}
\]

If \(f=P_+G_{F,a}\), then \(\widehat f\) is supported in \(\xi>0\), while \(\widehat f(-\xi)\) is supported in \(\xi<0\). Their product vanishes almost everywhere, so

\[
\int f(t)^2dt=0.
\]

The same argument applies to \(P_-G_{F,a}\), proving (6). Expanding

\[
G_{F,a}^2=(G_++G_-)^2
\]

and integrating therefore proves (7).

Because every direct pole lies to the right of the line when \(a<d_*\), the two Hardy channels have a particularly simple interpretation. For \(\xi>0\),

\[
\widehat{G_+}(\xi)
=-2\pi
\sum_jm_j
 e^{-(d_j-a)\xi}e^{-i\gamma_j\xi},
\tag{17}
\]

whereas

\[
\widehat{G_-}(-\xi)
=-2\pi
\sum_km_k
 e^{-(d_k+a)\xi}e^{+i\gamma_k\xi}.
\tag{18}
\]

The product cancels the probe depth:

\[
\widehat{G_+}(\xi)\widehat{G_-}(-\xi)
=
4\pi^2
\sum_{j,k}m_jm_k
 e^{-(d_j+d_k)\xi}
 e^{-i(\gamma_j-\gamma_k)\xi}.
\tag{19}
\]

This is the Fourier-side reason for (3): the factors \(e^{+a\xi}\) and \(e^{-a\xi}\) cancel exactly between the direct and reflected Hardy channels. Integrating (19), pairing \((j,k)\) with \((k,j)\), and using (16) reproduces (4).

## 3. Broad localization does not make the bilinear signal independent

Let \(\chi_T(t)=\chi(t/T)\) with \(\chi(0)=1\) and \(|\chi|\le C\). Since the finite Kunik block belongs to \(L^2(\mathbb R)\), dominated convergence gives

\[
\|(\chi_T-1)G_{F,a}\|_2\to0.
\tag{20}
\]

The Riesz projections are contractions on \(L^2\), hence

\[
P_\pm(\chi_TG_{F,a})
\longrightarrow
P_\pm G_{F,a}
\quad\text{in }L^2.
\tag{21}
\]

The bilinear product is continuous from \(L^2\times L^2\) to \(L^1\) by Cauchy--Schwarz. Therefore (21) implies (8).

This is worth contrasting with `WI-435`. There the safe-line Hardy leakage and the **transported edge forcing** both tend to zero on the same finite Blaschke model, while the one-sided interior defect quantum survives. The bilinear cross-pairing here also survives, but only because it directly pairs the two inner-factor Hardy components. It has not acquired a prime-side or outer-factor constraint. In the finite matched control it is exactly the boundary defect energy and nothing else.

Thus adiabatic localization by itself does not convert (7) into an independent source observable. To do that, a future proposal must specify an additional operator, weight, symbol, or nonlinear relation and prove that its value is constrained by zeta arithmetic in a way the finite Kunik block cannot reproduce.

## 4. Why this closes only the canonical mixed-frequency route

The conclusion is deliberately narrower than a no-go theorem for all mixed Hardy methods.

A **Hermitian** translation-invariant quadratic form is already block-diagonal in Fourier sign: bounded translation-invariant operators on \(L^2(\mathbb R)\) are Fourier multipliers, so their sesquilinear cross blocks \(P_+TP_-\) and \(P_-TP_+\) vanish. That class cannot mix the two channels at all.

The nonconjugated bilinear pairing (7) avoids that orthogonality because translation invariance for a complex-bilinear form pairs opposite frequencies \(\xi\) and \(-\xi\). The present finding shows what the simplest such escape buys: exactly the pre-existing Kunik boundary energy. It is therefore coercive but not independent.

This does **not** exclude a Hankel-type form \(P_-M_\phi P_+\) with a genuinely arithmetic symbol \(\phi\), a localized operator whose non-translation-invariant part remains quantitatively nontrivial for reasons specific to zeta, or nonlinear frequency interactions. Those are category changes because multiplication or nonlinear convolution can transfer frequency. Their publication gate is source independence: the symbol or interaction law must be fixed from arithmetic/boundary information rather than reconstructed from the same off-line divisor.

The result also does not assert that the full zeta Blaschke product admits a positive global square integral on any fixed interior line. If off-line depths accumulate at zero, no fixed \(a>0\) lies to the left of every direct zero. The theorem is finite-block first, exactly like the matched-control requirement of `WI-435`. A full-zeta use would need finite-height localization and explicit control of the zeros shallower than the chosen line and of the resulting window/boundary terms.

## Prior art and novelty audit

No novelty or priority claim is made for the analytic ingredients.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829v2 (2009), supplies the half-plane Blaschke factors and logarithmic-derivative decomposition used throughout `WI-423`--`WI-435`. The exact one-zero factor is the only zeta-specific input in (9).
- Contour invariance of the integral of a holomorphic function across a pole-free strip, the nonconjugated Parseval identity, Paley--Wiener/Hardy Fourier support, and Riesz projections are classical complex/harmonic analysis.
- Classical Hardy-space operator theory distinguishes Fourier multipliers, which preserve frequency support, from Hankel operators such as \(P_-M_\phi|_{H^2}\), which mix Hardy channels through multiplication by a symbol. This is the standard operator-theoretic boundary behind the final paragraph above; no new operator theorem is claimed here.
- G. V. Mikayelyan and F. V. Hayrapetyan, *On integral logarithmic means of Blaschke products for a half-plane*, Proceedings of the YSU A: Physical and Mathematical Sciences 52:3 (2018), 166--171, DOI 10.46991/PYSU:A/2018.52.3.166, is neighboring prior art on Fourier/integral-mean analysis of half-plane Blaschke products. The external audit did not establish that it contains the exact logarithmic-derivative square identity (3), so it is contextual rather than load-bearing.
- Repository-locally, `WI-424` already gives the right side of (3) as the positive boundary flux energy, and `WI-429` gives the separate one-sided Hardy energies. `WI-431` identifies the bare positive-frequency source as residue-only, while `WI-435` shows that edge-only transport cannot exclude finite Blaschke defects. The durable delta here is the exact identification of the **canonical opposite-Hardy bilinear coupling** with the existing boundary defect energy and the resulting closure of that most immediate mixed-frequency escape.

A targeted repository search found no existing `weil_inertia` finding stated in terms of a bilinear Hardy pairing or the nonconjugated square integral, and a targeted literature search around half-plane Blaschke logarithmic derivatives, Hardy/Riesz projections, and integral means did not locate this exact zeta-facing packaging. Absence from either search is not used as evidence of priority.

## Stress tests and falsification

1. **The condition \(a<d_*\) is essential.** If the line crosses one or more direct zeros, \(\mathcal G_F^2\) is no longer holomorphic in the strip from the boundary to the line. Direct poles that have moved to the negative-frequency side introduce signed cross terms, and (3) need not hold. On a line to the right of every direct zero, the finite block has only negative-frequency support and its nonconjugated square integral is zero.

2. **There is no contradiction with Hardy orthogonality.** Orthogonality concerns the Hermitian pairing \(\langle G_+,G_-\rangle=\int G_+\overline{G_-}=0\). Equation (7) uses \(\int G_+G_-\) without conjugation; Fourier reflection rather than equal-frequency overlap governs it.

3. **Positivity is special to the pole-free left-of-all-defects regime.** The integrand \(G_{F,a}(t)^2\) is not pointwise nonnegative. Positivity of the integral follows because it is contour-equal to the real boundary square \(h_F^2\). Once poles lie between the two lines, that argument fails.

4. **Finite-block exactness does not justify a full-product interchange.** An infinite Blaschke product may have arbitrarily shallow defects and may require convergence qualifications. Any full-zeta theorem must specify truncation/localization and prove its limiting passages separately.

5. **The finding is falsified by any missing contour contribution or Fourier-sign error.** For one defect, direct integration must give exactly \(2\pi m^2/d\), independent of \(a\) for \(0<a<d\). This one-pole identity is a complete normalization/sign check.

## Consequence for the research line

The `WI-435` frontier should not treat an unspecified "mixed positive/negative-frequency quadratic form" as automatically new information. There are two sharply different classes.

Hermitian translation-invariant quadratic forms cannot mix the two Hardy channels at all. The canonical complex-bilinear translation-invariant pairing does mix them, but for the Kunik inner factor it collapses exactly to the already-known boundary Poisson defect energy and is fully realized by the finite-Blaschke matched control.

Therefore the next mixed-frequency candidate must identify **where genuinely zeta-specific source information enters the coupling**. A useful proposal should expose a non-inner symbol, a non-adiabatic localization mechanism, a nonlinear arithmetic convolution, or another independently controlled structure, and then be tested on the finite Kunik block before any defect-to-zero conclusion is attempted. The exact identity (3) is the baseline matched control for that test.