# WI-145 — a single conjugate pair forbids a CGdL negative-tail kernel in any universal Lamzouri-form scalar bound

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-143 and WI-144 show that positive mixtures, coherent positive-Hilbert lifts, and PSD/Frobenius multi-channel variants of Lamzouri's finite inequality remain in a Fourier-positive autocorrelation cone, so they cannot reproduce the favorable Fourier tail used by Chirre--Gonçalves--de Laat (CGdL) under RH. WI-144 deliberately left open the possibility of abandoning that positive-Hilbert origin and proving a new **sign-indefinite scalar** finite inequality directly.

For the most direct version of that escape there is a stronger obstruction that does not use Gram positivity at all. Any normalized even scalar kernel `H` satisfying a universal Lamzouri-form inequality

\[
 s(\mathcal Z)\ge 2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{1}
\]

for every finite conjugation-invariant multiset must obey

\[
\boxed{H(iy)\ge 1\qquad\text{for every }y\in\mathbb R.}
\tag{2}
\]

This follows from the single test multiset `{iy/2,-iy/2}`. If, moreover, `H` is the Fourier transform of a real-even profile `phi` with enough exponential decay to be evaluated on all imaginary gaps, then any **genuine eventually non-positive outer Fourier tail** forces `H(iy)\to-\infty`; hence it contradicts (2). In particular, the Gaussian-polynomial `A_LP` class used by CGdL to obtain the RH-conditional `1.3208` multiplicity constant and `67.92%` simple-zero consequence cannot simply replace Lamzouri's square kernel in a universal off-line scalar inequality, even if one invents a proof unrelated to positive Hilbert spaces.

The result is narrower than an impossibility theorem for every CGdL-inspired unconditional argument. It closes the direct scalar pair-sum transplant. A joint multi-profile inequality, an additional off-line correction term, a source-specific restriction on horizontal depth, or a genuinely different signed matrix statistic is outside the theorem.

## 1. Exact two-point necessary condition

Let `H:C->C` be even, satisfy `H(0)=1`, and be real on the imaginary axis. Assume that for every nonempty finite multiset `Z` invariant under complex conjugation,

\[
 s(\mathcal Z)
 \ge
 2N-\sum_{z,w\in\mathcal Z}H(z-w),
 \qquad N=|\mathcal Z|,
\tag{3}
\]

where `s(Z)` is the number of simple real elements. This is exactly Lamzouri Proposition 2.1 after writing

\[
H(\xi)=K(\xi)^2,
\qquad K=\widehat{\eta^2}.
\tag{4}
\]

Now fix `y in R` and take

\[
\mathcal Z_y=\{iy/2,-iy/2\}.
\tag{5}
\]

For `y!=0` this is one simple non-real conjugate pair, so `N=2` and `s(Z_y)=0`. Its scalar pair sum is

\[
\sum_{z,w\in\mathcal Z_y}H(z-w)
 =2H(0)+H(iy)+H(-iy)
 =2+2H(iy).
\tag{6}
\]

Substitution into (3) gives

\[
0\ge 4-(2+2H(iy)),
\]

and therefore

\[
\boxed{H(iy)\ge1.}
\tag{7}
\]

No positivity, Gram representation, pair-correlation asymptotic, or zeta-specific input was used. Thus (7) is a necessary condition on **every** scalar kernel proposed for a universal finite inequality of the form (3), however that inequality is proved.

The condition is sharp for the actual Lamzouri class. If `q=eta^2>=0` is even and normalized by `int q=1`, then `K=widehat q` satisfies

\[
K(iy)=\int_{\mathbb R}q(u)\cosh(2\pi yu)\,du\ge1,
\tag{8}
\]

so `H(iy)=K(iy)^2>=1`. The positive spectral density that WI-143--WI-144 identified as restrictive on the real Fourier side is simultaneously what gives the correct **hyperbolic** sign on an off-line conjugate pair.

## 2. A genuine negative outer Fourier tail has the wrong hyperbolic sign

Assume now that `H` has an even real Fourier density `phi`, normalized by `int phi=1`, with

\[
H(z)=\int_{\mathbb R}\phi(u)e^{-2\pi i z u}\,du
\tag{9}
\]

for the imaginary arguments under consideration. It is enough, for example, to assume

\[
\int_{\mathbb R}|\phi(u)|e^{a|u|}\,du<\infty
\quad\text{for every }a>0,
\tag{10}
\]

which makes (9) entire. Suppose there is `R>=0` such that

\[
\phi(u)\le0\qquad(|u|\ge R),
\tag{11}
\]

and that the outer tail is genuine: `phi<0` on a set of positive measure with `|u|>R`. Then the positive part of `phi` is supported in `[-R,R]`, while some negative mass lies at a strictly larger radius.

For `y>0`, evenness gives the bilateral-Laplace identity

\[
H(iy)=\int_{\mathbb R}\phi(u)\cosh(2\pi yu)\,du.
\tag{12}
\]

Choose `delta>0`, `epsilon>0`, and a measurable set `E subset [R+delta,infinity)` of positive finite measure on which `phi(u)<=-epsilon`; such a choice exists from the genuine-tail hypothesis after intersecting with a bounded interval and a level set. If

\[
P:=\int_{\mathbb R}\phi_+(u)\,du,
\]

then the positive contribution to (12) is at most `P exp(2 pi R y)`, whereas the contribution from `E` is at most

\[
-\frac{\epsilon |E|}{2}e^{2\pi(R+\delta)y}.
\tag{13}
\]

All remaining outer contributions are non-positive. Consequently

\[
H(iy)
\le
P e^{2\pi R y}
-\frac{\epsilon |E|}{2}e^{2\pi(R+\delta)y}
\longrightarrow-\infty.
\tag{14}
\]

Equations (7) and (14) are incompatible. Therefore:

\[
\boxed{\text{a universal scalar inequality of the form (3) cannot have a genuinely negative outer Fourier tail.}}
\tag{15}
\]

The decay assumption is not cosmetic. A scalar kernel intended to act on arbitrary off-real elements must first be defined on their complex differences. If its real-line Fourier profile has no exponential moments, the direct analytic continuation needed by (3) may fail before any sign argument begins. If it does have the required continuation and the outer profile is genuinely negative, (14) supplies the obstruction.

## 3. Application to the CGdL semidefinite mechanism

Chirre, Gonçalves and de Laat, *Pair Correlation Estimates for the Zeros of the Zeta Function via Semidefinite Programming*, **Advances in Mathematics 361 (2020), 106926**, arXiv:1810.08843v2, define `A_LP` to consist of even continuous `f in L^1(R)` with

\[
f(0)=\widehat f(0)=1,
\qquad \widehat f\ge0,
\qquad f\text{ eventually non-positive}.
\tag{16}
\]

Writing `r=r(f)` for the last sign change, their Lemma 8 uses the nonnegative real-gap kernel

\[
g(x)=\frac1r\widehat f(x/r).
\tag{17}
\]

Under RH, all zero gaps are real. The form factor is globally nonnegative, while the Fourier transform of `g` is a rescaling of `f` and is non-positive outside the normalized known-correlation band. This favorable unknown-tail sign is the load-bearing freedom behind their improved multiplicity optimization.

To compare with the normalized finite inequality (3), put

\[
H(x):=r g(x)=\widehat f(x/r),
\qquad H(0)=1.
\tag{18}
\]

Up to the harmless reflection fixed by Fourier convention, the Fourier density of `H` is

\[
\phi(u)=r f(ru).
\tag{19}
\]

Thus `phi(u)<=0` for `|u|>=1`. Whenever the tail is genuinely negative, (15) says that this `H` cannot satisfy a universal Lamzouri-form scalar inequality on conjugation-invariant complex multisets.

The actual SDP search class in CGdL Section 4.1 is especially far inside the hypotheses of the obstruction: they use

\[
f(x)=p(x^2)e^{-\pi x^2}
\tag{20}
\]

with polynomial/SOS constraints enforcing eventual non-positivity and nonnegative Fourier transform. Such profiles have exponential moments of every order, so `H` extends entire. If an admissible nonzero polynomial-Gaussian profile has a genuine negative tail, its leading outer sign is negative and (14) applies directly. Hence the analyticity needed to evaluate off-critical gaps does not rescue the SDP profile; it makes the hyperbolic contradiction explicit.

This explains why simply combining unconditional form-factor nonnegativity with the CGdL tail sign is insufficient. The RH proof only evaluates `H` on the real axis. A universal unconditional replacement must also survive imaginary differences created by functional-equation/conjugation pairs, and a single such pair already sees the negative Fourier tail through a bilateral Laplace transform.

## 4. Relation to Lamzouri, WI-143/WI-144, and prior art

Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, Proposition 2.1, is the primary zero-side source. In the discussion immediately preceding that proposition, Lamzouri notes a different obstruction: the older termwise-positive Montgomery argument would require `Re K(z)>=0` for all complex `z`, which no nonconstant entire kernel can satisfy. Proposition 2.1 escapes that termwise condition by controlling the **whole square-kernel pair sum** through Hilbert geometry.

The present obstruction is therefore not a restatement of the termwise-positivity no-go. It grants the proposed scalar replacement every possible cancellation in the global sum (3) and asks only what (3) itself forces. The two-element multiset shows that global cancellation has nowhere to hide: any such inequality must satisfy the hyperbolic condition (7).

A public `teal-sea/zeta-lab` frontier-math audit already identifies the broader CGdL transplant bottleneck: unconditional form-factor nonnegativity is available, but the CGdL negative Fourier tail is not realized by the existing Gram/autocorrelation zero-side machinery. WI-143 specialized that obstruction to positive Lamzouri mixtures, and WI-144 extended it to coherent positive-Hilbert and PSD/Frobenius lifts. No novelty is claimed for CGdL's SDP method, Lamzouri's finite inequality, Fourier/Laplace continuation, or the broader observation that Gram autocorrelations cannot supply the desired tail.

The Mathia deduction is the exact extension beyond that Gram-origin objection: **even if one discards the positive-Hilbert derivation entirely and postulates a new scalar Lamzouri-form inequality, the lone conjugate-pair test forces `H(iy)>=1`, while a genuine CGdL `A_LP` tail forces the opposite asymptotic sign.** A search of the current `weil_inertia` corpus and the closest public follow-up located no stored proof of this two-point hyperbolic obstruction. This is not a priority claim; it is the novelty boundary used for this research line.

## 5. Boundaries and surviving routes

The result does not prove that the RH-conditional `67.92%` constant is unconditionally inaccessible. It rules out the cheapest remaining scalar transplant after WI-143/WI-144: replace Lamzouri's `K^2` by one normalized scalar CGdL-type gap kernel and prove the same universal finite inequality by some new argument.

Several routes remain genuinely different. A finite inequality may carry an explicit correction depending on horizontal depth or negative inertia rather than only the scalar pair sum. Multiple profiles may be retained jointly and constrained nonlinearly instead of being collapsed to one `H`. A sign-indefinite matrix statistic could couple conjugate pairs in a way not representable by (3). A source-specific theorem might confine the relevant off-line depths before the kernel is applied. Finally, a `T`-dependent construction would require a separate uniform analysis and is not covered merely by the fixed-kernel argument above.

The obstruction also does not say that every sign-changing Fourier profile fails. The load-bearing hypothesis is an outer region containing no positive mass but genuine negative mass at a strictly larger radius. A profile whose unknown-band behavior oscillates with both signs, or whose negative part is compensated by positive mass farther out, does not satisfy the simple Laplace dominance argument and needs its own two-point test.

## Research consequence

The direct scalar version of the `CGdL + Lamzouri` splice should now be treated as closed at the finite zero-side level. Any future proposal of that form must first test the one-pair condition (7); the genuine `A_LP` negative-tail mechanism fails before prime-side optimization enters.

This narrows the live direction left by WI-144. To exploit CGdL-like favorable tail information unconditionally, the zero-side certificate must retain **additional structure beyond one scalar translation-invariant pair kernel**—for example a joint/matrix observable or an explicit horizontal-defect charge capable of paying for the negative hyperbolic response of off-line conjugate pairs. No new zeta-zero percentage is claimed here.