# PL-348 — Prime-log modulations are already a form core on every finite Weil window

**Evidence:** `EXACT-DERIVED + CLASSICAL-PALEY-WIENER + DECISIVE-NEGATIVE`

**Status:** `PRIME-LOG-FREQUENCIES-ARE-OVERCOMPLETE + PRIME-MODULATION-GRAM-EQUALS-FULL-LOCALIZED-WEIL-POSITIVITY + NO-INTERMEDIATE-SPARSITY-MECHANISM`

## Precise claim

`PL-347` leaves one natural escape from the two extremes already classified there. One endpoint modulation gives only a classical Riesz channel, while the full Fourier modulation family is a form core and therefore reconstructs the entire localized Weil problem. The obvious Prime-Lattice attempt to sit strictly between those extremes is to retain only modulations by the canonical rational-prime frequencies

\[
\Lambda_{\mathbb P}:=\{\log p:p\text{ prime}\}.
\]

Despite looking arithmetically sparse, this family is **not sparse as a frequency set on any fixed logarithmic window**. Its counting function satisfies

\[
N_{\mathbb P}(R)
:=\#\{p:\log p\le R\}
=\pi(e^R)
\sim \frac{e^R}{R},
\tag{PL348-1}
\]

so it has far more than linearly many frequencies up to height `R`.

Fix `A>0` and `0<s<1/2`. Then

\[
\boxed{
\overline{\operatorname{span}\{e^{i(\log p)x}:p\text{ prime}\}}^{\,H^s(-A,A)}
=H^s(-A,A).
}
\tag{PL348-2}
\]

Consequently, for the endpoint envelope `u_A` of `PL-347`,

\[
u_A(x)=
\frac{e^{-(A-|x|)/2}}{\sqrt{2(1-e^{-A})}}
\mathbf 1_{|x|<A},
\]

the prime-indexed family

\[
u_{A,p}(x):=u_A(x)e^{i(\log p)x}
\tag{PL348-3}
\]

is already a **form core** for the completed localized Weil form `Q_W^A`. Thus the prime-log Gram matrix

\[
K_A^{\mathbb P}(p,q)
:=Q_W^A(u_{A,p},u_{A,q})
\tag{PL348-4}
\]

satisfies

\[
\boxed{
K_A^{\mathbb P}\succeq0\text{ on every finite prime set}
\iff
Q_W^A\ge0\text{ on its full form domain}.
}
\tag{PL348-5}
\]

and therefore

\[
\boxed{
RH
\iff
K_A^{\mathbb P}\succeq0
\quad\text{for every }A>0.
}
\tag{PL348-6}
\]

Equation (PL348-6) is exact but is **not a new RH mechanism**. It is again Weil positivity in coordinates. The canonical attempt to make the modulation family source-sensitive by using only the prime directions fails because the logarithmic prime frequencies are already so dense that no nonzero compactly supported distribution can annihilate all of them.

The useful general boundary is stronger. If a real frequency set `Lambda` satisfies

\[
\frac{N_\Lambda(R)}R\longrightarrow\infty,
\qquad
N_\Lambda(R):=\#(\Lambda\cap[-R,R]),
\tag{PL348-7}
\]

then the same argument gives completeness of its exponentials in `H^s(-A,A)` for every fixed `A` and every finite `s`. Hence every such superlinear-frequency candidate automatically collapses to the full localized form once it is inserted into the `PL-347` endpoint construction. A genuinely intermediate modulation family must at least have **at most linear frequency counting**; otherwise ordinary Paley-Wiener zero-density already makes it a core before any arithmetic relation is used.

## 1. Compact support forbids superlinearly many Fourier zeros

Let `I=(-A,A)` and suppose, contrary to (PL348-2), that the span of the prime exponentials is not dense in `H^s(I)`. By Hahn-Banach there is a nonzero continuous functional

\[
L\in(H^s(I))^*
\]

such that

\[
L(e^{i(\log p)x})=0
\qquad\text{for every prime }p.
\tag{PL348-8}
\]

Represent `L` by a distribution `T` of finite order supported in `[-A,A]`. Its Fourier-Laplace transform

\[
F(z):=\langle T,e^{-izx}\rangle
\tag{PL348-9}
\]

is entire. The Paley-Wiener-Schwartz theorem gives constants `C,N` with

\[
|F(z)|
\le
C(1+|z|)^N e^{A|\operatorname{Im}z|}.
\tag{PL348-10}
\]

The annihilation condition says

\[
F(-\log p)=0
\qquad(p\text{ prime}).
\tag{PL348-11}
\]

A nonzero entire function satisfying (PL348-10) can have only `O(R)` zeros in `|z|\le R`, counted with multiplicity. This follows directly from Jensen's formula: after translating to a point where the function is nonzero, the circle maximum in radius `2R` is at most `exp(O(R)+O(log R))`, so the zero count in radius `R` is `O(R)`.

But (PL348-11) supplies at least

\[
\pi(e^R)\sim e^R/R
\]

zeros in the disk of radius `R`. This contradicts the linear zero-count bound for every nonzero exponential-type entire function. Therefore `F` vanishes identically. Fourier-transform injectivity for compactly supported distributions gives `T=0`, contradicting the choice of `L`. This proves (PL348-2).

Nothing zeta-specific enters this argument. Even the full prime number theorem is more than necessary: any lower bound making `\pi(e^R)/R\to\infty` suffices. The load-bearing fact is the **frequency counting after applying logarithm**, not unique factorization, Euler products, or a relation between different prime coordinates.

## 2. Passage from exponential completeness to the Weil form core

`PL-347` established the localized form-domain bridge needed here. On a fixed window, convergence in `H^s`, with any `0<s<1/2`, controls the logarithmic Fourier form norm

\[
\|f\|_{\log}^2
=
\int_{\mathbb R}\log(2+|\xi|)|\widehat f(\xi)|^2\,d\xi
+\|f\|_2^2,
\tag{PL348-12}
\]

because

\[
\log(2+|\xi|)\ll_s 1+|\xi|^{2s}.
\tag{PL348-13}
\]

Smooth compactly supported functions form a core for `Q_W^A`. Take `f in C_c^infty(-A,A)` and write

\[
g=f/u_A.
\]

On the finite interval `u_A` is bounded above and away from zero and is piecewise Lipschitz. By (PL348-2), there are finite prime-log exponential sums

\[
P_m(x)=\sum_{p\in S_m}c_{m,p}e^{i(\log p)x}
\]

with

\[
P_m\longrightarrow g
\quad\text{in }H^s(-A,A).
\tag{PL348-14}
\]

For `s<1/2`, multiplication by the zero-extension interval indicator is bounded on `H^s`, and multiplication by the bounded piecewise-Lipschitz factor `u_A` is bounded as used already in `PL-347`. Hence

\[
\|u_AP_m-f\|_{H^s(\mathbb R)}\to0,
\]

and therefore, by (PL348-13),

\[
\|u_AP_m-f\|_{\log}\to0.
\tag{PL348-15}
\]

Every `u_AP_m` lies in the algebraic span of the prime-indexed states (PL348-3). Thus

\[
\boxed{
\overline{\operatorname{span}\{u_{A,p}:p\text{ prime}\}}^{\,\mathrm{form}}
=D(Q_W^A).
}
\tag{PL348-16}
\]

The Gram equivalence (PL348-5) now follows by polarization exactly as in `PL-347`: positivity of all finite prime Gram matrices is positivity on the algebraic span, and form-core density extends it to the full closed form domain. Weil's completed positivity criterion then gives (PL348-6) after quantifying over every aperture `A`.

No Euler product is analytically continued in this proof. The continuation-sensitive arithmetic is already packaged in the completed Weil form. The new statement concerns only whether the canonical prime-frequency coordinate family is genuinely smaller than that form. It is not.

## 3. Why this is a negative result for the live intermediate-sufficiency route

The research frontier after `PL-347` asked for a restricted modulation family whose positivity might be arithmetically sufficient without becoming a generic form-core reconstruction. The first canonical choice is exactly `Lambda_P={log p}` because these are the Kronecker frequencies dual to the prime basis directions of the exponent lattice.

That choice fails the intended test in the strongest possible way. On a finite physical window, `log p` becomes **overdense**, not sparse:

\[
N_{\mathbb P}(R)\asymp e^R/R.
\]

The corresponding exponentials already determine every compactly supported distribution, and hence every vector in the relevant Sobolev/form topology. The prime-indexed Gram criterion is therefore not intermediate between one scalar Riesz channel and the complete modulation matrix of `PL-347`; it lands at the complete end immediately.

The same conclusion holds a fortiori for larger natural exponent-lattice frequency sets such as

\[
\{\log n:n\ge2\},
\]

or the prime-power energies `\{k\log p\}`. Once the prime logs alone form a core, adjoining semigroup combinations cannot recover lost sparsity.

This also supplies a useful early rejection rule. For an endpoint-modulation proposal with frequency set `Lambda`, first compute `N_Lambda(R)`. If it is superlinear, compact-support Fourier theory already implies completeness on every fixed aperture. There is then no need to analyze Gram positivity in detail: the proposal can only re-coordinate the whole localized Weil form unless some additional relation restricts the allowed linear combinations or changes the topology/domain.

## 4. Prior-art and novelty audit

The analytic engine is classical. The Paley-Wiener-Schwartz theorem identifies Fourier-Laplace transforms of compactly supported distributions by polynomial-times-exponential growth; the zero-count consequence follows from Jensen's formula. This is standard entire-function/completeness theory and is not claimed as new. A convenient modern statement of the compactly-supported-distribution estimate is the introduction of J. Toft et al., “Paley-Wiener properties for spaces of entire functions,” *Analysis and Mathematical Physics* **10** (2020), DOI `10.1007/s13324-020-00361-8`; classical Beurling-Malliavin completeness theory gives a much broader framework for such exponential systems, but is not needed for the elementary superlinear-count argument here.

The arithmetic counting input is only the classical prime number theorem. The completed Weil-form and form-domain inputs are already anchored by the Weil/Bombieri/Suzuki literature used in `PL-347`. `PL-262` independently records the same compact-support/exponential-type Fourier geometry in the expanding-window CCM context, but it studies stability of evaluation rather than completeness of the prime-log exponential family.

A targeted literature search on 18 September 2026 for prime-log exponential completeness, systems `\{p^{it}\}`, and Paley-Wiener/Beurling-Malliavin formulations did not locate the exact specialization (PL348-2). That absence is **not** evidence of novelty: (PL348-2) is an immediate application of classical exponential-type zero counting once the frequency growth (PL348-1) is written down. The durable value here is the route restriction for `prime_lattice`, not a priority claim.

This is not `PL-156`: that finding samples Suzuki's scalar completed function at ordinary-prime energies and uses prime-gap interpolation. Here the prime energies are **frequencies** of test-state modulations, and the conclusion is form-core completeness. It is not `PL-189`: that finding uses compact frequency support and Fourier uniqueness to propagate flattening of affine phase windows; here compact **physical** support produces an entire transform whose zero density forbids an annihilator. It is not `PL-347`: that finding proves completeness for the full arithmetic Fourier grid `pi k/A`; the present result shows that the apparently much more arithmetic set `{log p}` is already complete by a different zero-density mechanism.

## 5. Adversarial boundaries

1. **No rational-prime selectivity is proved.** The proof only uses the coarse growth of the frequency set. Any admissible control set `Lambda` with `N_Lambda(R)/R -> infinity` has the same completeness property. This is exactly why the result is a negative for a new arithmetic mechanism.

2. **Completeness is aperture-by-aperture.** The argument fixes `A<infinity`. It does not assert a global basis property on the full real line, nor does it supply uniform frame bounds as `A->infinity`.

3. **No frame/Riesz-basis claim is made.** The prime-log exponentials are extremely redundant. Density alone is enough for the form-core conclusion; stability, conditioning, and uniqueness of coefficients are separate questions.

4. **The result uses arbitrary finite linear combinations of prime modulations.** A source law that allows only constrained coefficients, positive coefficients, coupled coefficients across apertures, or a genuinely noncommutative family is not covered. Such a constraint could prevent the Hahn-Banach completeness argument from being the relevant notion of sufficiency.

5. **At-most-linear counting is only a necessary escape condition, not a mechanism.** A thinner selected prime subsequence may fail to be complete, may still be complete by finer Beurling-Malliavin density, or may simply discard the RH-sensitive information. Passing the counting gate does not make a proposal promising by itself.

6. **The critical line is not selected here.** `1/2` enters through the completed Weil form and the subcritical Sobolev device inherited from `PL-347`; the prime-log completeness theorem itself works for every finite Sobolev order and contains no RH localization.

7. **No continuation shortcut occurs.** The proof never equates a prime exponential sum with `zeta(s)` outside an absolute-convergence region. All RH content remains in the pre-existing completed Weil criterion.

## Research consequence

The most canonical restricted family suggested by `PL-347` is closed: replacing the complete Fourier grid by the prime frequencies does **not** create a smaller RH-sensitive subsystem. The logarithm maps rational primes to a frequency set with exponential counting density, and compact-window Fourier theory turns that coarse abundance into full form-core completeness.

The live intermediate-sufficiency question must therefore impose more than “use prime-generated frequencies.” A candidate must either select a genuinely much thinner frequency family with at most linear counting and then prove arithmetic sufficiency, constrain the allowed coefficient combinations in a source-defined way, couple aperture and frequency so that fixed-window completeness no longer trivializes the problem, or introduce a relation/operator that is not invariant under replacing its states by an arbitrary complete frame.

This is a strict narrowing, not progress on RH itself: it removes the easiest Prime-Lattice implementation of the restricted-modulation escape while leaving open whether a genuinely source-constrained subsystem can retain enough completed Weil information without merely reconstructing the whole form.