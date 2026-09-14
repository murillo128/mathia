# WI-286 — growing prime screening hits a square-root gap threshold

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-BARRIER + PRIOR-ART-AUDITED`.
- **Scope:** the two-island support obstruction from `WI-285`, now tested against the **full aperture-growing prime family** required by the completely screened one-signed branch of `WI-284`.
- **Result:** complete screening by all active prime lags forces a symmetric two-island support to thin exponentially at the best established prime-in-short-interval scale. Baker--Harman--Pintz gives the exact exponent `19/40` for the width decay. Combining that thinning with an elementary Fourier-uncertainty lower bound for the gamma multiplier and the exact pole factor identifies a sharp exponential-scale transition at prime-gap exponent `1/2`: any uniform prime-in-short-interval theorem with exponent strictly below `1/2` would rule out such two-island zero-critical supports at large aperture, whereas the established exponent `21/40=0.525` does not. In fact the parameter relaxation obtained from the Baker--Harman--Pintz theorem still admits explicit two-bump profiles whose prime-deleted Rayleigh quotient tends to `-infinity`.
- **What it does not claim:** this does not construct a genuinely completely screened support for all active primes, does not improve known prime gaps, does not rule out multi-island or fractal screened supports, and does not prove that the actual Suzuki first null mode has two-island geometry. The negative profiles in §5 satisfy the **width constraint implied by** Baker--Harman--Pintz, not the full prime-avoidance condition.
- **Novelty boundary:** Baker--Harman--Pintz supply the short-interval prime theorem; Suzuki supplies the exact gamma-plus-pole form. The new line-local deduction is the quantitative bridge between the prime-gap exponent and the support-sensitive prime-deleted spectral balance. No historical priority claim is made.

## Claim

Let

\[
E_{R,b}:=(-R-b,-R+b)\cup(R-b,R+b),
\qquad
0<b<\frac{\log2}{4},
\tag{1}
\]

put

\[
\Delta:=2R,
\qquad
a:=R+b,
\qquad x:=e^\Delta,
\tag{2}
\]

and suppose `E_{R,b}` completely screens every active prime lag in the aperture:

\[
|E_{R,b}\cap(E_{R,b}-\log p)|=0
\quad
\text{for every prime }p\text{ with }\log p<2a.
\tag{3}
\]

Then, for all sufficiently large `\Delta`, the Baker--Harman--Pintz theorem implies

\[
\boxed{
2b\le \log\!\left(1+e^{-19\Delta/40}\right)
<e^{-19\Delta/40}.
}
\tag{4}
\]

Thus the fixed-width construction of `WI-285` is impossible once the active prime bases grow with the aperture.

More generally, suppose one has a uniform theorem saying that for some fixed `\theta<1` and `C>0`, every sufficiently large `x` has a prime in

\[
[x,x+Cx^\theta].
\tag{5}
\]

Then complete screening of the two-island support forces

\[
\boxed{
b\le \frac C2 e^{-(1-\theta)\Delta}.}
\tag{6}
\]

For the exact prime-deleted Suzuki form `q_{\rm arch}^a`, there are constants independent of `R,b` such that every nonzero form-domain vector `u` supported in `E_{R,b}` satisfies, for small enough `b`,

\[
\boxed{
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}
\ge
\frac12\log\frac1b-C_1
-8\sinh(b)\cosh(R).
}
\tag{7}
\]

Consequently, if (5) were available with

\[
\boxed{\theta<\frac12,}
\tag{8}
\]

then every completely screened symmetric two-island support would satisfy

\[
\inf_{0\ne u\in\mathfrak D(q_{\rm arch}^a)\cap L^2(E_{R,b})}
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}>0
\tag{9}
\]

for all sufficiently large `\Delta`. This contradicts the exact zero-bottom condition required by `WI-284`. Hence a **strictly sub-square-root uniform prime-gap exponent would eliminate the two-island completely screened branch**.

At the established Baker--Harman--Pintz exponent

\[
\theta=\frac{21}{40},
\tag{10}
\]

the pole allowance left by (4) is instead of size

\[
b e^{\Delta/2}
\lesssim e^{\Delta/40},
\tag{11}
\]

which is exponentially larger than the logarithmic/Fourier cost. The barrier is real for this compressed information: there is an explicit family satisfying the Baker--Harman--Pintz width constraint for which

\[
\boxed{
\frac{q_{\rm arch}^a(u_\Delta)}{\|u_\Delta\|_2^2}\to-\infty.
}
\tag{12}
\]

Therefore the currently established short-interval prime theorem, used only through the nearest-prime width consequence (4), cannot close the `WI-284` spectral contradiction even for the simplest symmetric two-island geometry. Any unconditional closure must exploit more collective arithmetic information than one short-interval prime, quantitative amplitudes from the Suzuki null equation, or another source-specific coupling.

## 1. Complete screening turns a prime near `e^Delta` into a width bound

For the symmetric support (1), an active lag `d>0` produces cross-component overlap exactly when

\[
|d-\Delta|<2b.
\tag{13}
\]

The assumption `b<\log2/4` makes every prime lag larger than the width of a single component, so self-overlap at a prime lag is irrelevant. What matters is the cross gap.

Take `x=e^\Delta`. Baker, Harman and Pintz prove that for every sufficiently large `x`, the interval

\[
[x,x+x^{0.525}]
=[x,x+x^{21/40}]
\tag{14}
\]

contains a prime. Let `p` be such a prime. Then

\[
0\le \log p-\Delta
\le
\log\!\left(1+x^{-19/40}\right).
\tag{15}
\]

If

\[
2b>\log\!\left(1+x^{-19/40}\right),
\tag{16}
\]

then `|\log p-\Delta|<2b`. Moreover

\[
\log p<\Delta+2b=2a,
\tag{17}
\]

so the prime is active. Equation (13) would then contradict complete screening. Hence (4) follows. The final strict inequality uses `\log(1+t)<t` for `t>0`.

Exactly the same argument with (5) gives

\[
2b\le\log(1+Cx^{\theta-1})
\le Cx^{\theta-1},
\tag{18}
\]

which is (6).

This is the first point at which the aperture-growing family does something that `WI-285`'s fixed finite prime bases cannot: a prime base is forced to appear close to the macroscopic separation itself, so a fixed positive island width cannot survive.

## 2. An elementary uncertainty bound forces logarithmic gamma energy on thin supports

Write Suzuki's gamma multiplier as in `WI-240`,

\[
m(z)
=\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi.
\tag{19}
\]

Continuity on the real axis and the standard vertical-line digamma asymptotic give constants `C_\Gamma<\infty` and `m_*>-\infty` such that

\[
m(z)\ge\log(1+|z|)-C_\Gamma,
\qquad
m(z)\ge m_*
\quad(z\in\mathbb R).
\tag{20}
\]

Let `u` be supported in `E_{R,b}`. Since `|E_{R,b}|=4b`, Cauchy--Schwarz gives

\[
|\widehat u(z)|^2\le4b\,\|u\|_2^2.
\tag{21}
\]

With Suzuki's Fourier normalization, Parseval is

\[
\frac1{2\pi}\int_{\mathbb R}|\widehat u(z)|^2dz=\|u\|_2^2.
\tag{22}
\]

Choose

\[
K:=\frac{\pi}{8b}.
\tag{23}
\]

Then (21) gives

\[
\frac1{2\pi}\int_{|z|\le K}|\widehat u(z)|^2dz
\le\frac12\|u\|_2^2.
\tag{24}
\]

Thus at least half the Fourier mass lies at `|z|\ge K`. For `b` small enough that the high-frequency lower bound in (20) exceeds `m_*`, the gamma part

\[
G(u)=\frac1{2\pi}\int m(z)|\widehat u(z)|^2dz
\tag{25}
\]

obeys

\[
\frac{G(u)}{\|u\|_2^2}
\ge
\frac12\bigl(\log(1+K)-C_\Gamma\bigr)
+\frac12m_*
\ge
\boxed{\frac12\log\frac1b-C_1.}
\tag{26}
\]

No Logvinenko--Sereda theorem or smoothness assumption is needed: this is just the `L^1` Fourier bound coming from finite support measure plus the exact asymptotic sign of Suzuki's gamma symbol.

## 3. The polar cross-interaction has the opposite exponential scale

For a general supported vector, not necessarily odd, `WI-240` gives the exact pole factorization

\[
P_a(u)
=2\operatorname{Re}\!\left(L_-(u)\overline{L_+(u)}\right),
\qquad
L_\pm(u)=\int u(x)e^{\pm x/2}dx.
\tag{27}
\]

Cauchy--Schwarz yields

\[
|L_+(u)|^2
\le\|u\|_2^2\int_{E_{R,b}}e^x dx,
\qquad
|L_-(u)|^2
\le\|u\|_2^2\int_{E_{R,b}}e^{-x} dx.
\tag{28}
\]

Symmetry of `E_{R,b}` gives the exact common value

\[
\int_{E_{R,b}}e^{\pm x}dx
=4\sinh(b)\cosh(R).
\tag{29}
\]

Therefore

\[
\boxed{
\frac{|P_a(u)|}{\|u\|_2^2}
\le8\sinh(b)\cosh(R).
}
\tag{30}
\]

Since `q_{\rm arch}^a=G+P_a`, equations (26) and (30) prove (7).

The competing scales are now explicit. If a prime-in-short-interval theorem of exponent `\theta` gives (6), then

\[
\log\frac1b
\ge(1-\theta)\Delta-O(1),
\tag{31}
\]

while, because `R=\Delta/2` and `b\to0`,

\[
8\sinh(b)\cosh(R)
\ll
b e^{\Delta/2}
\ll
\exp\!\left(-(1/2-\theta)\Delta\right).
\tag{32}
\]

For every fixed `\theta<1/2`, the second term tends to zero and the first grows linearly. Thus (7) tends to `+infinity` uniformly over every nonzero vector supported in `E_{R,b}`, proving (9).

This is stronger than excluding the explicit odd vector of `WI-285`: under a sub-square-root prime-gap theorem the **entire prime-deleted form on the two-island support becomes strictly positive**, so it cannot have the zero ground state demanded by complete first-crossing screening.

## 4. Why the established `21/40` exponent lands on the wrong side

For Baker--Harman--Pintz,

\[
1-\theta=\frac{19}{40},
\qquad
\theta-\frac12=\frac1{40}.
\tag{33}
\]

Equation (4) forces exponentially thin islands,

\[
b\ll e^{-19\Delta/40},
\tag{34}
\]

which is a genuine new rigidity compared with `WI-285`. But the worst polar contribution permitted by this width information alone is still

\[
|P_a|/\|u\|_2^2
\ll e^{\Delta/40},
\tag{35}
\]

whereas the guaranteed gamma penalty from (26) is only

\[
G(u)/\|u\|_2^2
\gg \Delta.
\tag{36}
\]

Thus the prime-gap exponent misses the spectral transition by exactly `1/40` in the exponential scale. The conclusion is not that an actual completely screened support realizes this worst case; it is that **compressing all growing-prime information to the single width estimate (4) loses too much information to prove the required positivity**.

The endpoint `\theta=1/2` is deliberately not claimed. Polynomial/logarithmic factors and constants then compete with the logarithmic gamma cost, so a separate endpoint analysis would be required. The robust transition proved here is strict: `\theta<1/2` closes the two-island branch, while the established `21/40` theorem does not through this interface.

## 5. The Baker--Harman--Pintz width relaxation still permits divergent negative energy

To show that the failure in §4 is not merely a weak lower-bound estimate, keep a fixed nonzero even nonnegative

\[
\phi\in C_c^\infty(-1,1)
\tag{37}
\]

and normalize its rescaling by

\[
\phi_b(x):=b^{-1/2}\phi(x/b).
\tag{38}
\]

Set

\[
b_\Delta:=\frac18e^{-19\Delta/40},
\qquad
R=\frac\Delta2,
\tag{39}
\]

and define the odd two-bump vector

\[
u_\Delta(x)
:=\phi_{b_\Delta}(x-R)-\phi_{b_\Delta}(x+R).
\tag{40}
\]

For large `\Delta`, `2b_\Delta` is smaller than the right side of (4), so this family obeys the **necessary width constraint extracted from Baker--Harman--Pintz**. Again, no claim is made that the actual prime lags avoid these intervals.

The norm is constant for disjoint bumps. If

\[
A_0:=\int_{-1}^1\phi(t)dt>0,
\tag{41}
\]

then

\[
\int\phi_b(y)e^{y/2}dy
=b^{1/2}\int_{-1}^1\phi(t)e^{bt/2}dt
=b^{1/2}(A_0+O(b)).
\tag{42}
\]

The odd pole identity from `WI-240` therefore gives

\[
\frac{P_a(u_\Delta)}{\|u_\Delta\|_2^2}
=-c_\phi b_\Delta e^{\Delta/2}(1+o(1))
=-c_\phi' e^{\Delta/40}(1+o(1))
\tag{43}
\]

for constants `c_\phi,c_\phi'>0`.

On the other hand, the vertical-line digamma upper bound

\[
|m(z)|\ll1+\log(2+|z|)
\tag{44}
\]

and the Schwartz decay of `\widehat\phi` give after the change of variable `t=b_\Delta z`

\[
\frac{|G(u_\Delta)|}{\|u_\Delta\|_2^2}
=O_\phi\!\left(1+\log\frac1{b_\Delta}\right)
=O_\phi(\Delta).
\tag{45}
\]

The exponential negative term (43) dominates (45), proving (12). Hence the BHP-derived width relaxation itself still contains arbitrarily negative prime-deleted directions. A proof of `WI-284` cannot pass through that relaxation alone.

## 6. Prior-art audit

The prime-distribution input is the peer-reviewed theorem of R. C. Baker, G. Harman and J. Pintz, **The difference between consecutive primes, II**, *Proceedings of the London Mathematical Society* 83:3 (2001), 532--562, DOI `10.1112/plms/83.3.532`. Its abstract states the uniform result used here: `[x,x+x^{0.525}]` contains primes for all sufficiently large `x`. The exponent is `21/40`.

A current-status cross-check is Lingyu Guo and Victor Zhenyu Guo, **Piatetski-Shapiro Primes in short intervals**, arXiv:2606.01115 (2026), whose introduction distinguishes the more recent Guth--Maynard asymptotic-formula result from Baker--Harman--Pintz as the best known lower-bound/existence result for ordinary primes in short intervals. Guth and Maynard, **New large value estimates for Dirichlet polynomials**, arXiv:2405.20552, obtain an asymptotic formula at length `x^{17/30+o(1)}`, which is longer than the `x^{21/40}` interval needed for the present existence estimate and therefore does not improve (4).

The exact spectral input is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), through the gamma multiplier and pole factor already source-audited in `WI-240` and `WI-284`. The Fourier support-measure estimate in §2 is elementary and does not import an external uncertainty theorem.

The line-local novelty audit against `WI-240`, `WI-267`, `WI-281`--`WI-285` finds no earlier bridge from a growing-prime short-interval exponent to the prime-deleted support spectrum. `WI-285` stops precisely at the fact that a fixed finite family does not constrain the width uniformly as the aperture grows; the present result quantifies what the full prime family does next and locates the `1/2` spectral threshold. Targeted external searches found the classical short-interval prime theorem and current surveys/status statements, but not this Suzuki support-spectral deduction. Search absence is audit context only, not a priority claim.

A May 2026 arXiv preprint advertises a dramatically stronger `O(\log^2 p)` maximal-prime-gap bound. That claim is recent, unrefereed, and far beyond the established short-interval record, so it is **not used as evidence or as an input here**. The finding rests only on the peer-reviewed Baker--Harman--Pintz theorem and Suzuki's exact form.

## 7. Research consequence

`WI-285` showed that no fixed finite set of prime bases can control the prime-deleted restricted inertia. The full growing prime family does impose a qualitatively new constraint: symmetric endpoint islands must shrink at least as

\[
e^{-19\Delta/40}.
\tag{46}
\]

But the exact gamma/pole balance explains why this is not yet enough. The pole couples the two remote components at the `e^{\Delta/2}` scale, so the arithmetic thinning must beat a square-root relative prime-gap scale before ordinary support uncertainty forces positivity.

Thus the two-island branch exposes a concrete arithmetic/spectral gate:

\[
\boxed{
\text{nearest-prime control alone closes the branch only beyond the square-root exponent.}
}
\tag{47}
\]

Since established unconditional prime gaps stop at `21/40>1/2`, the next useful theorem should not ask this program to solve a major prime-gap problem as a side effect. It should instead retain information discarded by the nearest-prime reduction: simultaneous action of many prime lags, the exact positive amplitudes of the first-crossing null equation, or support geometry beyond two isolated components. This is the source-specific information that remains capable of converting complete screening into the zero-defect contradiction required by the canonical mandate.