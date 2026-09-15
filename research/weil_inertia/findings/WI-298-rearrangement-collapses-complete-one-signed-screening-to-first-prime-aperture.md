# WI-298 — rearrangement collapses complete one-signed screening to the first-prime aperture

**Status:** `EXACT-DERIVED + CLASSICAL-REARRANGEMENT + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

Let

\[
L:=\log 2,
\qquad
r_2:=\frac{L}{2}.
\]

Suppose `v` is a nonzero real Suzuki localized Weil null mode with `v>=0` a.e. and with **complete prime-power screening** in the sense used in WI-281/WI-284: every active von-Mangoldt translation autocorrelation vanishes, so the full null identity reduces to the prime-deleted archimedean form

\[
q_{\rm arch}(v)=G(v)+P(v)=0.
\]

Then its symmetric decreasing rearrangement `v^*` satisfies

\[
\boxed{
\operatorname{supp} v^*\subseteq[-L/2,L/2],
\qquad
q_{\rm arch}(v^*)\le q_{\rm arch}(v)=0.
}
\]

At the exact first-prime aperture `r_2=L/2`, all prime-power translation terms vanish on `v^*`: the `n=2` shift has length exactly `2r_2=L` and therefore has zero overlap a.e., while every larger prime-power lag exceeds the support diameter. Hence

\[
\boxed{
Q_W^{r_2}(v^*)=q_{\rm arch}(v^*)\le0,
\qquad
\lambda_{r_2}\le0.
}
\tag{1}
\]

This gives a sharp structural collapse for the one-signed complete-screening branch. If `v` is specifically the **first** unrestricted Suzuki crossing mode at aperture `a_*`, then (1) forces

\[
\boxed{a_*\le\frac{\log2}{2}.}
\tag{2}
\]

Therefore a completely screened one-signed first-crossing mode **cannot occur above the first-prime threshold at all**. The remote-satellite/local-to-global propagation problem left by WI-297 is unnecessary for this branch once `a_*>r_2`: symmetric rearrangement already compresses any such screened mode to a nonpositive prime-free test at `r_2`, contradicting first-crossing minimality.

The remaining branch is now much narrower: `a_*<=r_2`, where complete screening is vacuous because no prime-power translation has positive-measure overlap. Consequently any rigorous strict finite-scale positivity theorem

\[
\lambda_{r_2}>0
\]

would rule out the **entire** one-signed complete-screening first-crossing branch. The public `FP-0.35` candidate discussed in WI-259/WI-260 would imply this if its exact certificate were repaired and independently certified, because `0.35>r_2`; WI-260 remains the evidence boundary, so no such positivity input is assumed here.

## 1. Packing from complete screening gives a rearranged support of length at most `log 2`

WI-281 proves that for a nonnegative completely screened mode, the powers of the first prime impose

\[
v(x+kL)v(x)=0
\quad\text{for a.e. }x
\quad\text{and every }k\in\mathbb Z\setminus\{0\}.
\tag{3}
\]

Writing

\[
E:=\{x:v(x)>0\},
\]

(3) makes `E` a measurable selector modulo `L`, and WI-281 gives the exact packing bound

\[
\boxed{|E|\le L.}
\tag{4}
\]

Let `v^*` denote the symmetric decreasing rearrangement of `v`. Equimeasurability preserves every `L^p` norm and the distribution of positive level sets. In particular `v^*` is supported, up to null sets, on the centered interval whose length is `|E|`. Hence from (4),

\[
\boxed{\operatorname{supp}v^*\subseteq[-L/2,L/2].}
\tag{5}
\]

The point of the next two sections is that rearrangement also moves the **entire prime-deleted quadratic form in the favorable direction**. This is stronger than merely rearranging support measure.

## 2. The gamma part decreases under symmetric decreasing rearrangement

Use the Fourier normalization already fixed in WI-294/WI-296, with archimedean multiplier

\[
m(\xi)
=
\Re\psi\!\left(\frac14+\frac{i\xi}{2}\right)-\log\pi.
\]

Gauss's classical integral representation of the digamma function gives, for real `xi`,

\[
\begin{aligned}
m(\xi)-m(0)
&=\int_0^\infty
\frac{e^{-t/4}\bigl(1-\cos(\xi t/2)\bigr)}{1-e^{-t}}\,dt\\
&=2\int_0^\infty
W(h)\bigl(1-\cos(\xi h)\bigr)\,dh,
\end{aligned}
\tag{6}
\]

where

\[
W(h):=\frac{e^{-h/2}}{1-e^{-2h}}
\qquad(h>0).
\tag{7}
\]

The kernel `W` is positive and strictly decreasing: differentiating its logarithm gives

\[
\frac{d}{dh}\log W(h)
=-\frac12-\frac{2e^{-2h}}{1-e^{-2h}}<0.
\]

If

\[
C_f(h):=\int_{\mathbb R} f(x+h)f(x)\,dx,
\]

then Parseval and (6) yield the exact real-space representation

\[
\boxed{
G(f)
=m(0)\|f\|_2^2
+2\int_0^\infty
W(h)\bigl(\|f\|_2^2-C_f(h)\bigr)\,dh.
}
\tag{8}
\]

For the form-domain vectors under discussion the right side is finite. The singularity `W(h)~1/(2h)` at the origin must not be split naively into two divergent integrals, so the rearrangement step is done by monotone truncation.

For `N>0` set

\[
K_N(x):=\min\{W(|x|),N\}.
\]

`K_N` is nonnegative, symmetric decreasing, bounded near zero and integrable at infinity. The Riesz rearrangement inequality therefore gives

\[
\iint f(x)K_N(x-y)f(y)\,dx\,dy
\le
\iint f^*(x)K_N(x-y)f^*(y)\,dx\,dy
\tag{9}
\]

for every nonnegative `f`. Since rearrangement preserves `||f||_2`, (9) is exactly the statement that the truncated translation-difference energy decreases:

\[
2\int_0^\infty K_N(h)
\bigl(\|f^*\|_2^2-C_{f^*}(h)\bigr)\,dh
\le
2\int_0^\infty K_N(h)
\bigl(\|f\|_2^2-C_f(h)\bigr)\,dh.
\tag{10}
\]

For every real `f`, Cauchy--Schwarz gives `C_f(h)<=||f||_2^2`, so the integrands in (10) are nonnegative. Letting `N->infinity` and using monotone convergence in (8) gives

\[
\boxed{G(f^*)\le G(f).}
\tag{11}
\]

This also proves that `f^*` remains in the relevant logarithmic form domain whenever `f` is there; no regularity of the rearranged profile is being assumed separately.

## 3. The pole part also decreases under rearrangement

For nonnegative real `f`, the pole term from WI-294/WI-296 is

\[
P(f)=2L_-(f)L_+(f),
\qquad
L_\pm(f)=\int f(x)e^{\pm x/2}\,dx.
\]

Symmetrizing the double integral gives the translation-invariant distance form

\[
\boxed{
P(f)=2\iint f(x)f(y)
\cosh\!\left(\frac{x-y}{2}\right)dx\,dy.
}
\tag{12}
\]

Let `M=||f||_1` and define the close-pair mass

\[
J_f(t):=
\iint f(x)f(y)\mathbf 1_{\{|x-y|\le t\}}\,dx\,dy.
\]

The kernel `1_{[-t,t]}` is symmetric decreasing, so Riesz gives

\[
J_f(t)\le J_{f^*}(t)
\qquad(t\ge0).
\tag{13}
\]

Using

\[
\cosh(r/2)
=1+\int_0^r\frac12\sinh(t/2)\,dt
\]

and Tonelli's theorem,

\[
\iint f(x)f(y)\cosh\!\left(\frac{x-y}{2}\right)dx\,dy
=
M^2+
\int_0^\infty
\frac12\sinh(t/2)
\bigl(M^2-J_f(t)\bigr)dt.
\tag{14}
\]

The quantity `M^2-J_f(t)` is the weighted mass of pairs farther apart than `t`. Equation (13) says rearrangement can only decrease this far-pair mass. Since all weights in (14) are nonnegative,

\[
\boxed{P(f^*)\le P(f).}
\tag{15}
\]

Combining (11) and (15) gives the exact prime-deleted rearrangement principle needed here:

\[
\boxed{q_{\rm arch}(f^*)\le q_{\rm arch}(f)
\quad\text{for every nonnegative form-domain }f.}
\tag{16}
\]

Notice that both terms move in the same direction. This is special to the one-signed branch: the Riesz inequalities used above do not apply to a general sign-changing null mode.

## 4. Complete screening plus rearrangement produces a nonpositive prime-free test

For the completely screened null mode `v`, WI-284 identifies the full null equation with the prime-deleted one:

\[
q_{\rm arch}(v)=Q_W^a(v)=0.
\tag{17}
\]

Apply (16) and then the packing support bound (5):

\[
q_{\rm arch}(v^*)\le0,
\qquad
\operatorname{supp}v^*\subseteq[-r_2,r_2].
\tag{18}
\]

At radius `r_2=L/2`, the smallest von-Mangoldt translation is exactly `L=2r_2`. Two `L^2` functions supported in `[-r_2,r_2]` have zero overlap a.e. after a translation by `L`; the possible endpoint intersection has Lebesgue measure zero. Thus

\[
C_{v^*}(\log2)=0.
\]

Every other prime-power lag is strictly larger than `L` and also has zero overlap. Therefore the full localized Weil form agrees with the prime-deleted form on `v^*`:

\[
Q_W^{r_2}(v^*)=q_{\rm arch}(v^*)\le0.
\tag{19}
\]

Since rearrangement preserves the nonzero `L^2` norm, (19) is an admissible variational test and proves (1).

Now assume `v` was the unrestricted first-crossing null mode from WI-238, so

\[
a_*:=\inf\{a>0:\lambda_a\le0\},
\qquad
\lambda_a>0\quad(a<a_*).
\]

Because (1) says `lambda_{r_2}<=0`, the definition of `a_*` immediately gives (2). In particular the extensive complete-screening geometry developed for a hypothetical one-signed mode with active prime lags cannot actually occur at the **first** crossing: if `a_*>r_2`, rearrangement contradicts first-crossing minimality before any remote-satellite propagation estimate is needed.

## 5. Prior art and novelty boundary

The ingredients used in the comparison are classical. The Riesz rearrangement inequality is the standard theorem that convolution against a nonnegative symmetric decreasing kernel is increased by symmetric decreasing rearrangement; the truncation in Section 2 is a direct application of that theorem to the singular digamma kernel. Gauss's digamma integral is standard; for a modern formula reference see NIST DLMF §5.9(ii), especially equation 5.9.12. The layer-cake proof in Section 3 is the standard way to reverse the Riesz orientation for a cost increasing with pair distance. No novelty is claimed for any of these rearrangement facts.

A targeted prior-art search around symmetric rearrangement, localized Weil quadratic forms, Suzuki's operator, and digamma/logarithmic energies located the classical rearrangement machinery and the existing Suzuki/Bombieri Weil-form literature, but no source formulating the specific implication

\[
\text{complete one-signed screening}
\Longrightarrow
\lambda_{(\log2)/2}\le0.
\]

Search absence is not a priority claim. The durable Mathia contribution is the exact synthesis of WI-281's arithmetic selector packing with the rearrangement monotonicity of **both** prime-deleted terms, which collapses the screened first-crossing branch to the first-prime aperture.

Relevant classical references:

- F. Riesz, **Sur une inégalité intégrale**, *Journal of the London Mathematical Society* 5 (1930), 162--168; classical rearrangement inequality.
- E. H. Lieb and M. Loss, **Analysis**, 2nd ed., AMS Graduate Studies in Mathematics 14 (2001), rearrangement inequalities.
- NIST Digital Library of Mathematical Functions, §5.9(ii), integral representations of the digamma function, https://dlmf.nist.gov/5.9.
- M. Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), for the localized Weil operator/form framework.

## 6. Boundaries and stress tests

1. **One sign is essential.** The proof uses Riesz with `f>=0` twice. It does not control a sign-changing first mode, including the odd zero mode forced under RH failure by WI-247.
2. **Complete screening is essential.** Equation (17) uses exact disappearance of every active prime-power overlap. If screening is incomplete, the rearrangement can create new prime overlaps and there is no monotone comparison for the full arithmetic form in this argument.
3. **This does not prove finite-scale positivity.** The theorem proves `lambda_{r_2}<=0` *if* a one-signed completely screened null mode exists. Excluding the remaining `a_*<=r_2` branch still requires a strict positivity theorem at `r_2` or another argument. WI-259/WI-260 explain why the public `FP-0.35` certificate is promising but not yet established Mathia evidence.
4. **Endpoint prime overlap is harmless.** At `2r_2=log2`, the translated support intervals meet only at an endpoint. For `L^2` form-domain vectors this contributes zero to the autocorrelation integral; no strict `<` convention is being hidden.
5. **The singular gamma kernel is not used as an integrable convolution kernel directly.** The proof truncates `W` by `K_N=min(W,N)`, applies Riesz at finite `N`, and only then passes to the singular limit by monotone convergence. This is the load-bearing domain step.
6. **Translation choice is harmless.** Both `G` and `P=2L_-L_+` are translation invariant. Centering the rearrangement therefore does not insert a hidden pole penalty.
7. **No claim about the full RH obstruction.** A sign-changing first crossing or an incompletely screened one-signed crossing remains outside this result. The theorem closes only the prime-active part of the one-signed complete-screening branch and reduces the rest to the prime-free aperture.

## Falsification and audit test

The result is falsified by any one of the following: an incorrect normalization in (6)--(8); failure of `W(h)=e^{-h/2}/(1-e^{-2h})` to represent the nonconstant digamma multiplier in Suzuki's normalization; an invalid use of Riesz for the bounded kernels `K_N`; failure of the monotone limit because the localized form domain is not characterized by finite translation-difference energy; a wrong orientation in the pole rearrangement (13)--(15); a mismatch between WI-281's selector measure and the positivity support of the rearranged form-domain vector; or a nonzero endpoint contribution from the `log2` translation at support diameter exactly `log2`.

Each point has a direct audit. Equation (6) follows by subtracting Gauss's integral formula at `xi=0` and substituting `t=2h`. `K_N` is positive, integrable, symmetric decreasing. The energy integrand in (8) is nonnegative by Cauchy--Schwarz. Equation (14) is a positive layer-cake identity, so its orientation is fixed by the close-pair Riesz inequality. Equimeasurability gives the support-length bound, and the endpoint translation overlap has measure zero.

## Research consequence

For the one-signed complete-screening branch, the next decisive gate is no longer a many-component propagation theorem for exponentially small satellites. Rearrangement bypasses that geometry and reduces the branch to one finite-scale question:

\[
\boxed{\lambda_{(\log2)/2}>0\ ?}
\]

A rigorous positive answer rules out this branch completely. Conversely, if `lambda_{(\log2)/2}<=0`, then the rearranged test supplied here is compatible with the remaining prime-free alternative and the source-side screening program cannot by itself eliminate it. The first-prime finite-scale positivity problem isolated conditionally in WI-259 is therefore promoted to a direct elimination gate for the entire one-signed complete-screening first-crossing mechanism.