# WP-116 — Scale-free prime-torus power covariance forces homogeneous spectral multipliers and critical divergence

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + COVER/POWER-COVARIANCE + SCALE-FREE + CORRELATION-INDEPENDENT + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION` for the continuous scalar spectral escape left open by `WP-115`.

`WP-109` shows that a positive scalar Kronecker spectral multiplier can have finite critical axis cost only if it decays more strongly than `t^{-2}` at high frequency. `WP-114` shows that every multiplier nondegenerate at zero pays infinite cost because positivity forces divergent mixed-prime Fourier mass arbitrarily near zero. `WP-115` then closes the canonical scalar Markov/Dirichlet compromise, but deliberately leaves positive non-Markov band-pass functional calculi such as

\[
w_m(t)=\frac{t^2}{(1+t^2)^m},\qquad m>2,
\tag{1}
\]

which vanish at zero and decay sufficiently fast at infinity.

There is an exact Mathia-native test for whether such a scalar multiplier is genuinely **scale-free** with respect to the multiplicative exponent geometry. On the prime torus, the integer power maps send an exponent character `alpha` to `n alpha`, so the Kronecker frequency scales exactly by `n`. Requiring a scalar positive spectral form to transform by one fixed degree under every such power map forces its multiplier to be a pure homogeneous power. Every nonzero homogeneous power has infinite critical cost: exponents at or above `-2` diverge on the compulsory one-prime Weil rays, while exponents below `-2` blow up at zero and are killed by the correlation-forced near-zero mass of `WP-114`.

Thus the non-Markov band-pass escape from `WP-115` survives only by **breaking exact scale covariance and introducing a distinguished spectral scale** (as the `1` in `1+t^2` does), or by changing the operator/state architecture before scalar functional calculus. Exact power covariance plus scalar positivity cannot supply a finite critical Weil carrier.

This is not a global Weil-positivity theorem. It produces neither the Gamma contribution nor the polar/global counterterms and does not identify the Weil quadratic functional. It is a canonicity obstruction for one surviving positive spectral route.

## 1. The intrinsic prime-torus power action scales Kronecker energy exactly

Let

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T
\]

be the prime torus used by the Bohr/Prime-Lattice completion, with finitely supported exponent characters

\[
\chi_\alpha(z)=z^\alpha,
\qquad
\alpha\in\mathbb Z^{(\mathcal P)}.
\tag{2}
\]

The multiplicative Kronecker generator has frequency

\[
X\chi_\alpha=E(\alpha)\chi_\alpha,
\qquad
E(\alpha)=\sum_p\alpha_p\log p.
\tag{3}
\]

For every integer `n>=1`, the coordinatewise power map

\[
P_n(z)_p=z_p^n
\tag{4}
\]

preserves product Haar measure. Its pullback

\[
U_nf=f\circ P_n
\tag{5}
\]

is therefore an isometry on `L^2(T^P)` and satisfies

\[
U_n\chi_\alpha=\chi_{n\alpha}.
\tag{6}
\]

Consequently

\[
\boxed{XU_n=nU_nX}
\tag{7}
\]

on the trigonometric-polynomial core. This scaling uses only the exponent lattice and the intrinsic logarithmic energy; it does not use zeta zeros, RH, a fitted kernel, or a regularization.

The map is not unitary: its range consists of characters whose exponent vectors are divisible by `n`. That is harmless. Since `U_n` is isometric,

\[
U_n^*\chi_{n\alpha}=\chi_\alpha,
\tag{8}
\]

which is exactly what is needed for coarse compression of a spectral form.

## 2. Exact all-degree covariance forces a pure power symbol

Let

\[
A=w(|X|)
\tag{9}
\]

be a nonnegative scalar spectral multiplier. Assume `w:(0,infinity)->[0,infinity)` is continuous and finite. The value at zero may be set separately; in particular an energy seminorm may annihilate constants even when the positive-frequency symbol is singular at the origin.

Suppose there is one real covariance degree `kappa` such that on every nonconstant character

\[
\boxed{
U_n^*AU_n=n^\kappa A
\qquad(n\ge1).
}
\tag{10}
\]

Applying (10) to `chi_alpha` and using (6)--(8) gives

\[
\boxed{
w(n|E(\alpha)|)=n^\kappa w(|E(\alpha)|).}
\tag{11}
\]

The positive Kronecker spectrum of finitely supported exponent characters is

\[
\{|E(\alpha)|:E(\alpha)\ne0\}
=
\{|\log q|:q\in\mathbb Q_{>0},\ q\ne1\}.
\tag{12}
\]

Indeed unique factorization identifies an integer exponent vector with a positive rational number. Since the positive rationals are dense in `R_{>0}` and the logarithm is continuous, the set in (12) is dense in `(0,infinity)`.

Therefore continuity extends (11) from the character spectrum to every `t>0`:

\[
w(nt)=n^\kappa w(t)
\qquad(t>0,n\ge1).
\tag{13}
\]

Integer homogeneity already gives rational homogeneity. From

\[
w\!\left(n\frac tn\right)=n^\kappa w(t/n)=w(t)
\]

we obtain `w(t/n)=n^{-kappa}w(t)`, and hence

\[
w\!\left(\frac mn t\right)
=\left(\frac mn\right)^\kappa w(t)
\qquad(m,n\ge1).
\tag{14}
\]

Continuity in the scaling parameter and density of the positive rationals then imply

\[
\boxed{
w(rt)=r^\kappa w(t)
\qquad(r,t>0).}
\tag{15}
\]

Setting `t=1` yields the complete classification

\[
\boxed{
w(t)=c\,t^\kappa,\qquad c=w(1)\ge0.}
\tag{16}
\]

Thus a continuous scalar Kronecker multiplier carrying an exact fixed-degree law under every intrinsic integer power map has no room for a band-pass scale, shifted resolvent, compact spectral window, or other crossover. It is either zero or a homogeneous power.

The classification itself is the familiar dilation-covariance/homogeneity principle from Fourier multiplier theory. The point here is its exact realization on the prime-torus character spectrum, where the logarithms of positive rationals make the spectral test set dense.

## 3. Homogeneity `kappa>=-2` is killed by the compulsory prime axes

Let `mu` be any finite positive critical completion of mass `C>0` with the exact first prime-coordinate moments

\[
\widehat\mu(e_p)=-\frac{\log p}{\sqrt p}.
\tag{17}
\]

For a finite prime set `P`, normalize its marginal by

\[
\eta_P=C^{-1}(\pi_P)_*\mu.
\tag{18}
\]

Then

\[
\left|\widehat\eta_P(e_p)\right|
=\frac{\log p}{C\sqrt p}.
\tag{19}
\]

For a nonnegative symbol define the extended cylindrical cost, with the constant mode omitted if the energy is a seminorm,

\[
\mathcal Q_{w,P}(\eta_P)
=
\sum_{\substack{\alpha\in\mathbb Z^P\\E(\alpha)\ne0}}
w(|E(\alpha)|)
|\widehat\eta_P(\alpha)|^2.
\tag{20}
\]

If `w(t)=ct^kappa` with `c>0`, retaining only the first one-prime harmonics gives

\[
\mathcal Q_{w,P}(\eta_P)
\ge
\frac c{C^2}
\sum_{p\in P}
\frac{(\log p)^{\kappa+2}}p.
\tag{21}
\]

Write `beta=kappa+2`. The prime number theorem and partial summation give

\[
\sum_{p\le x}\frac{(\log p)^\beta}{p}
\sim
\begin{cases}
\dfrac{(\log x)^\beta}{\beta},&\beta>0,\\[6pt]
\log\log x,&\beta=0,
\end{cases}
\tag{22}
\]

up to the usual lower-order normalization at the endpoint. In particular,

\[
\boxed{
\sum_p\frac{(\log p)^\beta}{p}=+\infty
\qquad(\beta\ge0).
}
\tag{23}
\]

Hence

\[
\boxed{
\sup_{P\Subset\mathcal P}\mathcal Q_{w,P}(\eta_P)=+\infty
\qquad(\kappa\ge-2,c>0).
}
\tag{24}
\]

This is exactly the sharp high-frequency boundary already exposed abstractly in `WP-109`: the homogeneous classification shows that an exactly scale-covariant multiplier cannot evade it by bending its high-frequency profile.

## 4. Homogeneity `kappa<-2` is killed by the forced near-zero correlations

For `kappa<-2`, the axis series in (21) converges. This is the only homogeneous regime that passes the mandatory high-frequency test. But now

\[
w(t)=ct^\kappa\longrightarrow+\infty
\qquad(t\downarrow0).
\tag{25}
\]

Fix any `epsilon>0`. Since `kappa<0`, every `0<t<epsilon` satisfies

\[
w(t)\ge c\epsilon^\kappa>0.
\tag{26}
\]

`WP-114` proves, for **every** positive critical completion satisfying (17), that the mixed coefficients at prime-difference frequencies have infinite cylindrical squared mass in every fixed neighborhood of zero:

\[
\sup_{P\Subset\mathcal P}
\sum_{\substack{p,q\in P,\ p\ne q\\
0<|\log p-\log q|<\epsilon}}
|\widehat\eta_P(e_p-e_q)|^2
=+\infty.
\tag{27}
\]

All these frequencies are nonzero by unique factorization. Combining (26) and (27),

\[
\mathcal Q_{w,P}(\eta_P)
\ge
c\epsilon^\kappa
\sum_{\substack{p,q\in P,\ p\ne q\\
0<|\log p-\log q|<\epsilon}}
|\widehat\eta_P(e_p-e_q)|^2,
\tag{28}
\]

so

\[
\boxed{
\sup_{P\Subset\mathcal P}\mathcal Q_{w,P}(\eta_P)=+\infty
\qquad(\kappa<-2,c>0).
}
\tag{29}
\]

Thus the apparent high-frequency escape is exactly exchanged for an infrared catastrophe. Homogeneity cannot suppress both ends: if the power is large enough at infinity to avoid the prime-axis divergence, it is necessarily nondegenerate--indeed singular--on the near-zero mixed frequencies that positivity itself forces.

Combining (24) and (29) gives the main obstruction:

\[
\boxed{
\text{exact all-degree prime-torus power covariance}
+
\text{nonzero continuous scalar positivity}
+
\text{exact critical first moments}
\Longrightarrow
\text{infinite cylindrical spectral cost}.
}
\tag{30}
\]

The conclusion is independent of how the positive completion correlates distinct primes.

## 5. The `WP-115` band-pass falsifier survives only by breaking scale covariance

Return to

\[
w_m(t)=\frac{t^2}{(1+t^2)^m},\qquad m>2.
\tag{31}
\]

`WP-115` chose this family precisely because it evades both necessary endpoint tests: it vanishes quadratically at zero and its prime-axis contribution behaves like `(log p)^{4-2m}/p`, which is summable for `m>2`.

Its covariance ratio is

\[
\frac{w_m(nt)}{w_m(t)}
=
 n^2
\left(\frac{1+t^2}{1+n^2t^2}\right)^m.
\tag{32}
\]

For every `n>1` and `m>0`, this depends nontrivially on `t`. Therefore there is no real `kappa` for which

\[
w_m(nt)=n^\kappa w_m(t)
\]

on any dense set of positive frequencies. The band-pass family is not an overlooked homogeneous solution; its finite endpoint behavior is purchased exactly by the crossover scale in `1+t^2`.

This is the decisive falsifier for the scope of `WP-116`. Positive non-Markov functional calculus remains logically possible. What is no longer possible is to claim that a finite critical band-pass form is simultaneously inherited from the scale-free prime-torus power symmetry. A surviving scalar form must explain, geometrically and independently, **where its distinguished spectral scale comes from**.

## 6. Relation to the earlier cover-positive classification

`WP-093` also studies exact all-degree cover covariance, but on a different Mathia object. There the normalized refinement maps act on the one-ray cover Hilbert space `ell^2(N_0)`, and fixed finite bandwidth plus the degree-one law classifies positive matrices into a weighted Dirichlet cone whose critical ray is `T^*T`.

The present result does not reuse that classification. It acts on the global prime-torus exponent characters, where the intrinsic semigroup operation is the coordinatewise power map `alpha -> n alpha`, and it classifies only **scalar functions of the Kronecker generator**. The overlap is conceptual rather than formal: exact cover/refinement covariance strongly restricts positive geometry before arithmetic scalarization.

This distinction matters for the surviving routes. A matrix-valued, graded, boundary, or nonseparable form need not be a scalar `w(|X|)` and is not covered by (16). Likewise an archimedean coupling can introduce an independent scale before the prime-torus spectral form is taken.

## 7. Matched controls

### Supercritical attenuation removes the critical prime-density endpoint

Replace the first moments by the exact attenuated family

\[
\left|\widehat\eta_{\sigma,P}(e_p)\right|
=\frac{\log p}{C p^\sigma},
\qquad\sigma>\frac12.
\tag{33}
\]

For every fixed homogeneous degree `kappa`, the compulsory axis contribution is

\[
\frac c{C^2}
\sum_p
\frac{(\log p)^{\kappa+2}}{p^{2\sigma}},
\tag{34}
\]

which converges for every real `kappa`. Moreover the short-shell squared first-moment mass used in `WP-114` tends to zero rather than infinity for `sigma>1/2`. Thus the two **forced** critical endpoint mechanisms used in (24) and (29) disappear immediately above one half. This does not assert that every off-critical correlated completion has finite total cost; it is the matched necessary-condition control.

### Sparse generator energies do not reproduce the two-ended trap

The classification (16) is a scale-covariance statement, but the divergence uses the density of the ordinary prime energies. In the generalized-generator control already used in `WP-113` and `WP-114`, take energies with only `O(1)` generators in every fixed-width high-energy window, for example `E_j=j`. Critical-looking amplitudes `E_je^{-E_j/2}` then have exponentially summable squared axis mass, while the fixed-width near-resonance shell explosion of ordinary `log p` is absent.

So (30) is not a universal theorem about every free multiplicative coordinate system. The rational primes matter through the critical density of `log p` and the divergence of their squared first-moment mass.

### A supplied global scale lies outside the theorem

If an independently constructed finite--archimedean object supplies a distinguished positive scale `lambda_0`, a scalar symbol such as

\[
\frac{t^2}{(\lambda_0^2+t^2)^m}
\tag{35}
\]

need not obey (10). `WP-116` does not reject it merely for being nonhomogeneous. The burden then shifts to the actual mandate: `lambda_0` must arise from the same intrinsic global geometry that also produces the Gamma/polar terms, and the sign theorem must precede the arithmetic identification. Choosing `lambda_0` simply to regularize the critical completion would be a hand-picked spectral regularization rather than a solution.

## 8. Prior-art and novelty audit

The structural ingredients are classical.

- The Bohr identification of Dirichlet coefficients with monomials on the infinite prime polytorus is standard; the branch's durable anchor is Hedenmalm--Lindqvist--Seip, *A Hilbert space of Dirichlet series and systems of dilated functions in L2(0,1)*, Duke Math. J. 86 (1997), DOI `10.1215/S0012-7094-97-08601-4`, already recorded in `research/weil_positivity/SOURCES.md`.
- The principle that exact dilation covariance of a scalar Fourier multiplier forces a homogeneous symbol is standard harmonic-analysis structure. Here it is proved directly from (11)--(16), so no external classification theorem is imported.
- The prime-sum threshold in (22)--(23) is the same classical PNT/partial-summation calculation already used in `WP-109`.
- The low-frequency correlation theorem used in (27) is the canonical Mathia result `WP-114`, itself derived from positive covariance matrices plus the prime number theorem.

A targeted audit of dilation-covariant Fourier multipliers, homogeneous multiplier classes, Hardy spaces of Dirichlet series, and the Bohr lift found the expected classical dilation/homogeneity framework but no reason to identify (30) with a known Weil-positivity criterion. No historical novelty is claimed for homogeneous multipliers, Bohr compactification, or dilation covariance.

The retained branch-specific content is the exact synthesis: **the intrinsic integer power action on the prime-torus Kronecker spectrum makes every continuous scale-free scalar multiplier homogeneous, and the critical prime data then force divergence on one of the two spectral ends for every possible homogeneity degree.** This closes the scale-free version of the non-Markov spectral escape explicitly left open by `WP-115`.

## 9. Aggressive falsification and exact boundary

The result survives the main attacks within its stated hypotheses.

**Arbitrary prime correlations do not help.** For `kappa>=-2`, only compulsory one-prime modes are used. For `kappa<-2`, `WP-114` already applies to every positive completion regardless of mixed architecture.

**Taking very negative homogeneity does not help.** It repairs the high-frequency prime sum only by making the symbol singular near zero, exactly where positivity forces unbounded mixed mass.

**An infinite set of spectral zeros cannot help under exact covariance and continuity.** Equations (13)--(16) leave only `ct^kappa`; a nonzero such symbol has no positive-frequency zeros.

**The theorem does not classify arbitrary Borel multipliers.** Without continuity on `(0,infinity)`, values on the dense character spectrum can in principle be extended pathologically off that spectrum. Such an extension changes no cylindrical character energy, but claiming it as intrinsic geometry would require an independent regularity principle. The present statement intentionally closes the continuous functional-calculus route rather than manufacture a measurability theorem irrelevant to the mandate.

**The theorem does not require continuity at zero.** Negative homogeneous powers are allowed as positive-frequency seminorm symbols with the constant mode treated separately; they are still killed by nonzero frequencies accumulating at zero.

**Exact power covariance is a real restriction.** A global geometry with a canonical archimedean length/energy scale may break it. That is a surviving possibility, not a defect in the proof. The finding says precisely that finite critical scalar positivity cannot come from a scale-free prime-torus spectral symmetry alone.

## Research consequence

The scalar spectral frontier after `WP-109`, `WP-114`, and `WP-115` is now narrower. The explicit positive band-pass loophole is not compatible with exact all-degree power covariance of the intrinsic exponent lattice. Every nonzero continuous scalar multiplier that respects that symmetry is forced into a homogeneous power, and every homogeneous power has infinite critical cost.

Therefore a surviving positive scalar mechanism must contain additional geometric information **before** the final spectral functional calculus: a distinguished archimedean/global scale, a non-translation-invariant operator, a boundary or quotient architecture, a matrix/graded/cohomological form, or a genuinely nonseparable finite--archimedean construction. Merely replacing the failed Markov symbol by a scale-free positive band-pass multiplier is not an escape.