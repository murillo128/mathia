# RE-214 — Prime-count capacity caps separated vertical hiding without KV fidelity

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + TWOFOLD-KAISER + WEIGHTED-PRIMITIVE-LOWER-BOUND + ORDINARY-PRIME-SOURCE + BOUNDED-MULTIPLICITY-CAPACITY + NO-KV-FIDELITY-ASSUMPTION + LOGARITHMIC-HEIGHT-BARRIER`.

**Parent findings:** RE-209, RE-213.

`RE-213` closes the Korobov--Vinogradov endpoint for the separated vertical-Euler repair architecture by proving a generic weighted-prefix lower bound with exponential rate one. Its stated arithmetic consequence still uses fidelity to every fixed KV envelope. Two further facts sharpen the source-side interpretation.

First, the uniform Kaiser estimate in `RE-213` does not need a growing convolution order. Taking the smallest integrable power, namely two Kaiser factors, gives the explicit generic lower bound

\[
\boxed{
R\gg_H (1-\epsilon)
\left(\frac{\sinh(HT/2)}{HT/2}\right)^2
\gg_H (1-\epsilon)\frac{e^{HT}}{(HT)^2}.
}
\tag{1}
\]

Second, for the ordinary-prime `{0,1,2}` source the same weighted primitive is a normalized signed prime-count prefix. Bounded multiplicity alone therefore gives the universal capacity upper bound

\[
\boxed{R\ll \sqrt Q,}
\tag{2}
\]

independently of any PNT/KV fidelity requirement on the *perturbed* source. Combining (1) and (2), every separated ordinary-prime repair of the `RE-209` type that hides the selector-scale local packet on `|t|\le T_Q`, with `T_Q=O(\log Q)`, must satisfy

\[
\boxed{
H T_Q-2\log(H T_Q)
\le \frac12\log Q+O_H(1).
}
\tag{3}
\]

Hence

\[
\boxed{
H T_Q
\le \frac12\log Q+2\log\log Q+O_H(1).
}
\tag{4}
\]

In particular, for `T_Q=c\log Q` every fixed

\[
\boxed{c>\frac1{2H}}
\tag{5}
\]

is impossible even if all KV constraints on the resulting prime-multiplicity source are discarded. For the current corridor `H=\log 8`, this means that

\[
\boxed{c>\frac1{2\log 8}=0.2404491734\ldots}
\tag{6}
\]

cannot be hidden by any finite separated ordinary-prime `{0,1,2}` repair simply because there are not enough distinct prime edits to support the signed prefix forced by continuum observability.

This isolates the role of KV more cleanly than `RE-213`. **Strictly above** the half-logarithmic threshold, bounded ordinary-prime multiplicity already gives the obstruction. KV fidelity is needed only to push the exclusion to the exact endpoint and to force the stronger near-endpoint deficit

\[
\frac{\frac12\log Q-H T_Q}{V(Q)}\to+\infty
\]

proved in `RE-213`.

## 1. Two Kaiser factors give unit exponential rate with only logarithmic loss

Use the generic separated spectral-gap notation of `RE-213`. Let `\nu` be a finite real signed measure supported on `[H,\infty)` and assume

\[
\sup_{|t|\le T}|1-\widehat\nu(t)|\le\epsilon,
\qquad 0\le\epsilon<1.
\tag{7}
\]

Define

\[
G(L):=\int_{[H,L]}e^u\,d\nu(u),
\qquad
R:=\sup_{L\ge H}e^{-L}|G(L)|,
\qquad
A:=HT.
\tag{8}
\]

For the normalized Kaiser--Bessel density from `RE-212`--`RE-213`, write

\[
\Phi_\beta(x)
=C_\beta\frac{\sin\sqrt{x^2-\beta^2}}
{\sqrt{x^2-\beta^2}},
\qquad
C_\beta:=\frac{\beta}{\sinh\beta},
\qquad x\ge\beta.
\tag{9}
\]

`RE-213` proves uniformly in `\beta\ge1` and every integer `n\ge2` that

\[
\int_\beta^\infty |\Phi_\beta(x)|^n\,dx
\ll C_\beta^n,
\qquad
\int_\beta^\infty |(\Phi_\beta^n)'(x)|\,dx
\ll nC_\beta^n.
\tag{10}
\]

The previous finding chose `\beta=o(A)` and let `n\to\infty`. That is unnecessary for the weighted-primitive argument. Take instead

\[
\boxed{
\beta=\frac A2,
\qquad n=2.
}
\tag{11}
\]

For `A\ge2`, scale the Kaiser density to support `[-T/2,T/2]` and convolve it with itself. The resulting nonnegative probability density is supported on `[-T,T]`, and its Fourier transform is

\[
\phi(L)=\Phi_{A/2}(LT/2)^2.
\tag{12}
\]

Since `L\ge H`,

\[
\frac{LT}{2}\ge\frac{HT}{2}=\beta,
\]

so the tail estimates (10) apply on the entire repair support. Scaling back from `x=LT/2` gives

\[
\int_H^\infty (|\phi'(L)|+|\phi(L)|)\,dL
\ll_H C_{A/2}^2.
\tag{13}
\]

The `|\phi|` term has an extra factor `2/T=2H/A`, hence is harmless for `A\ge2`. Pairing (7) against this probability density and integrating by parts exactly as in `RE-209` gives

\[
1-\epsilon
\le
R\int_H^\infty (|\phi'|+|\phi|)\,dL.
\tag{14}
\]

Therefore

\[
R
\gg_H
(1-\epsilon)
\left(\frac{\sinh(A/2)}{A/2}\right)^2.
\tag{15}
\]

For large `A`,

\[
\frac{\sinh(A/2)}{A/2}
=\frac{e^{A/2}}{A}(1+o(1)),
\]

so

\[
\boxed{
\log R
\ge
A-2\log A-O_H(1)-\log\frac1{1-\epsilon}.
}
\tag{16}
\]

This is strictly sharper than the `A-O(\sqrt{A\log A})` specialization recorded in `RE-213`. The exponential coefficient is unchanged and remains optimal for positive compact-window tests; only the subexponential loss improves from stretched-exponential to polynomial.

The choice `n=2` is not cosmetic. For the Kaiser transform itself, `|\Phi_\beta(x)|\asymp x^{-1}` along generic tails, so the `n=1` `|\phi|` integral required by the same integration-by-parts norm is not absolutely integrable. Squaring is the smallest power for which both tail terms in (13) close. No claim is made that the polynomial factor `A^2` is optimal among other positive windows or other coercive representations.

## 2. Ordinary-prime bounded multiplicity gives an absolute prefix-capacity ceiling

Return to the ordinary-prime architecture of `RE-209` and `RE-213`. Put

\[
X_0:=2Q,
\qquad
B\asymp\frac{\sqrt Q}{\log Q},
\qquad
d_Q:=\frac1{\sqrt Q\log Q}.
\tag{17}
\]

The local packet consists of `B` ordinary primes near `X_0`. Every remote edit is an ordinary prime `q\ge X_0e^H` used at most once, with coefficient `c_q\in\{-1,+1\}`. Assume `T_Q=O(\log Q)`, `H T_Q\to\infty`, and

\[
\sup_{|t|\le T_Q}|D_Q(1+it)|=o(d_Q)
\tag{18}
\]

for the exact Euler discrepancy.

The exact-Euler to first-harmonic reduction of `RE-209` is unchanged. After normalization, (18) produces a signed measure `\nu_Q` satisfying (7) with `\epsilon=o(1)`. Its weighted primitive is exactly

\[
G_Q(L)
=-\frac1B
\sum_{\substack{q\le X_0e^L\\q\text{ remote}}}c_q
=-\frac{C_Q(X_0e^L)}B,
\tag{19}
\]

where `C_Q(y)` is the signed remote prime-count prefix. Hence

\[
R_Q
=
\sup_{L\ge H}
\frac{e^{-L}|C_Q(X_0e^L)|}{B}.
\tag{20}
\]

Because every ordinary prime can be edited at most once,

\[
|C_Q(y)|\le\pi(y).
\tag{21}
\]

The standard unconditional prime-count bound `\pi(y)\ll y/\log y`—already far weaker than the PNT input anchored in `SOURCES.md`—therefore gives, uniformly for every `L\ge H`,

\[
\frac{e^{-L}|C_Q(X_0e^L)|}{B}
\ll
\frac{X_0}{B\log(X_0e^L)}
\le
\frac{X_0}{B\log X_0}
\asymp\sqrt Q.
\tag{22}
\]

Thus

\[
\boxed{R_Q\ll\sqrt Q.}
\tag{23}
\]

This upper bound contains no assumption that the *modified* multiplicity source obeys a KV envelope, a PNT error term, a Chebyshev discrepancy bound, or any analogous fidelity condition. It uses only the ordinary-prime carrier set and the bounded edit multiplicity.

Combining (15) with `\epsilon=o(1)` and (23), with `A_Q:=H T_Q`, yields

\[
\frac{e^{A_Q}}{A_Q^2}
\ll_H\sqrt Q,
\tag{24}
\]

or equivalently

\[
A_Q-2\log A_Q
\le
\frac12\log Q+O_H(1).
\tag{25}
\]

Since this inequality itself forces `A_Q=O(\log Q)`, it follows that

\[
\boxed{
A_Q
\le
\frac12\log Q+2\log\log Q+O_H(1),
}
\tag{26}
\]

which is (4).

The same leading ceiling holds for any fixed edit bound `|c_q|\le M`: (21) becomes `|C_Q(y)|\le M\pi(y)`, changing only the `O(1)` term in (25). What fails if unbounded multiplicities are allowed is precisely the source-capacity upper bound (23).

## 3. Separation of bounded-multiplicity and KV roles

Equation (26) changes the interpretation of the half-logarithmic boundary. Suppose

\[
T_Q=c\log Q
\]

with fixed `c`. If `Hc>1/2`, then the left side of (25) exceeds `(1/2)\log Q` by a positive multiple of `\log Q`, while the logarithmic correction is only `O(\log\log Q)`. This contradicts bounded prime capacity. Therefore every fixed `c>1/(2H)` is impossible **before any KV fidelity condition is imposed**.

At the exact endpoint `Hc=1/2`, however, (25) is compatible with the source capacity because of the `2\log A_Q` loss. This is where `RE-213` supplies genuinely stronger arithmetic information: fidelity to every fixed KV envelope implies

\[
\frac{\frac12\log Q-H T_Q}{V(Q)}\to+\infty,
\]

which excludes equality and, in fact, requires a deficit of `\omega(V(Q))` below the half-logarithmic height.

Thus the current obstruction has two distinct layers:

- **bounded ordinary-prime multiplicity:** forces `H T_Q\le\frac12\log Q+O(\log\log Q)` and excludes every fixed `c>1/(2H)`;
- **KV fidelity:** strengthens this to `\frac12\log Q-H T_Q=\omega(V(Q))`, excluding the endpoint and a much thicker near-endpoint region.

This distinction is source-specific and survives arbitrary sign interlacing, arbitrary finite remote support, and arbitrary global distortion of the perturbed source outside the bounded-multiplicity constraint.

## 4. Representation audit, prior-art boundary, and falsification checks

The Kaiser--Bessel window and its Fourier transform are classical signal-processing objects. The elementary prime-count estimate in (22) is classical and is weaker than the unconditional PNT already anchored in `SOURCES.md`. Broad prior-art search found the expected literature on Kaiser windows, time--band concentration, spectral-gap oscillation, and analytic continuation, but no statement coupling the twofold-Kaiser weighted-prefix tariff to the cardinality capacity of an ordinary-prime `{0,1,2}` Euler repair. No new external theorem is load-bearing, so `SOURCES.md` requires no update.

The main falsification checks are as follows. The twofold test remains a nonnegative probability density supported on the full observed interval, so a uniform Euler error cannot be amplified by pairing. The `n=2` Kaiser tail is absolutely integrable both before and after differentiation, whereas `n=1` is not sufficient for this exact norm. The prime-power remainder remains the same `o(1)` normalized term as in `RE-209` because no step changes the Euler-to-first-harmonic reduction. The capacity estimate uses the **signed count prefix before partial summation**, so cancellation in the Chebyshev weights cannot evade it. Finally, moving the offending prefix to an arbitrarily remote shell does not help: the factor `e^{-L}` in `R_Q` cancels the physical scale `X_0e^L`, leaving the uniform `\sqrt Q` capacity ceiling.

The result does not improve the constructive range of `RE-208`, does not settle whether the `2\log\log Q` correction is sharp, and does not exclude the exact half-logarithmic endpoint without a stronger source condition such as KV fidelity. It also does not prove that a hypothetical Robin counterexample exposes this continuum vertical observable. The live constructive/coercive constant gap therefore remains, but its upper side is now decomposed cleanly into a bounded-multiplicity barrier and a stricter KV barrier.

## Research consequence

The half-logarithmic vertical ceiling is not merely an artifact of asking the synthetic source to preserve the ordinary-prime PNT with KV accuracy. **Above the threshold, the obstruction already follows from the finite supply of distinct ordinary primes available to a bounded-multiplicity repair.** KV enters only at the endpoint and in the `V(Q)`-scale boundary layer below it.

For `H=\log 8`, every fixed `c>0.2404491734\ldots` is therefore excluded for separated ordinary-prime `{0,1,2}` continuum hiding even after dropping all global fidelity requirements on the modified source. The next constructive question is correspondingly sharper: a successful architecture below the half-log ceiling must not only beat the absolute-variation accounting of `RE-208`; it must realize the necessary signed prefix while staying within the ordinary-prime cardinality budget, and KV then imposes the stronger near-endpoint restriction from `RE-213`.