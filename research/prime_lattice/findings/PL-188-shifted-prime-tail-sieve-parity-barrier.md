# PL-188 — Local shifted-factorization data hits the classical sieve parity barrier; parity breaking needs a bilinear/global tail input

## Claim

`PL-186` isolates the first genuinely hard affine target left after the one-point flattening results: for a fixed nonzero shift `h`, every bounded observable of the truncated exponent vector

\[
(v_\ell(q+h))_{\ell\le y},\qquad y=X^{o(1)},
\]

is asymptotically governed by Ford's independent Kubilius model as `q` ranges over primes, while the full Möbius/Liouville parity of `q+h` remains unresolved. This is not merely a quantitative gap in the current coordinate cutoff. The natural strategy of recovering the missing sign by accumulating ever more **local divisor/exponent information** runs into the classical parity problem of sieve theory.

The exact matched control is Selberg's Liouville example, recorded and used explicitly by Friedlander--Iwaniec. Let

\[
a_n^+=\frac{1+\lambda(n)}2,
\]

so in prime-exponent coordinates

\[
a_n^+=1
\quad\Longleftrightarrow\quad
\sum_p v_p(n)\equiv0\pmod2.
\]

Thus `A^+` is the even-total-exponent half of the lattice and contains **no primes at all**. Nevertheless Friedlander--Iwaniec state that this sequence satisfies their classical sieve remainder hypothesis `(R)` to level

\[
D=x^{1-\varepsilon},
\]

while it fails precisely the additional bilinear hypothesis `(B)` that they introduce to break the parity problem. Their paper further identifies the cancellation in `(B)` with sign changes of `mu(mn)` in a bilinear range.

Therefore even very deep control of ordinary divisor/congruence marginals does not determine the global parity character

\[
\lambda(n)=(-1)^{\langle v(n),\mathbf 1\rangle}.
\]

For the `prime_lattice` affine branch this gives a structural falsification rule: extending Ford/Kubilius-style one-point coordinate control, Siegel--Walfisz residue control, or classical Type-I/divisor information cannot by itself be treated as progress on the full shifted-prime Möbius/Liouville sign. A surviving mechanism must inject a genuinely parity-sensitive **bilinear, signed, or otherwise nonlocal coupling of the large-coordinate tail** before the final averaging.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT` for the route

\[
\text{increasing local exponent/divisor resolution of }q+h
\longrightarrow
\text{recovery of full Möbius/Liouville parity}.
\]

The classical parity obstruction and the bilinear escape are prior art. The line-specific contribution is the bridge to `PL-186`: its large-prime tail is not just where the current Kubilius theorem stops; for the natural local-divisibility strategy it is exactly where one encounters the established sieve parity barrier. This is **not** an impossibility theorem for all analyses of the tail, nor a proof that a stronger joint factorization theorem could not settle the shifted-prime problem.

## 1. Exponent-lattice matched control: opposite global parity, the same fixed local divisor statistics

Define both parity halves

\[
a_n^\pm=\frac{1\pm\lambda(n)}2.
\]

For every integer `d>=1`, complete multiplicativity of Liouville gives the exact divisor-count identity

\[
\begin{aligned}
A_d^\pm(x)
&:=\sum_{\substack{n\le x\\ d\mid n}}a_n^\pm\\
&=\frac12\left\lfloor\frac xd\right\rfloor
\pm\frac{\lambda(d)}2
\sum_{m\le x/d}\lambda(m).
\end{aligned}
\]

The prime number theorem is equivalent to

\[
L(y):=\sum_{m\le y}\lambda(m)=o(y),
\]

so for every fixed `d`,

\[
A_d^\pm(x)=\frac{x}{2d}+o(x).
\]

In lattice language, the event `d|n` imposes finitely many coordinate lower bounds

\[
v_p(n)\ge v_p(d).
\]

Hence every fixed divisibility cylinder has the same limiting density in the two opposite total-parity classes even though

\[
\lambda(n)\equiv+1\text{ on }A^+,
\qquad
\lambda(n)\equiv-1\text{ on }A^-.
\]

This elementary calculation is only a finite-cylinder illustration. The stronger theorem-level control needed here is the Selberg example as audited by Friedlander--Iwaniec: `A^+` satisfies the classical remainder axiom `(R)` with `D=x^(1-epsilon)` despite having `a_p=0` for every prime. Thus the failure is not repaired merely by pushing ordinary divisor distribution to a very high level.

The geometric lesson is precise. The global Walsh character

\[
(-1)^{|v(n)|_1}
\]

is not determined by the local incidence data that a classical sieve records. This is exactly the kind of distinction `PL-186` exposes for `q+h`: all coordinates below every subpower cutoff can be statistically generic while the final parity remains in the unobserved tail.

## 2. Friedlander--Iwaniec identify the missing input as bilinear and parity-sensitive

Friedlander--Iwaniec study nonnegative sequences `A=(a_n)` through the divisor sums

\[
A_d(x)=\sum_{\substack{n\le x\\d\mid n}}a_n
      =g(d)A(x)+r_d(x).
\]

Their standard sieve input `(R)` controls weighted sums of `|r_d|` through a level `D`. They emphasize that the classical framework, even with `D=x^(1-epsilon)`, cannot in general detect primes because of the parity problem.

The extra hypothesis `(B)` is qualitatively different. In their notation it controls bilinear forms containing

\[
\sum_m\left|
\sum_{N<n\le2N\atop mn\le x}
\gamma(n)\mu(mn)a_{mn}
\right|.
\]

They explicitly note that the useful cancellation comes from the sign changes of `mu(mn)`. With `(B)` added to the classical hypotheses they obtain an asymptotic formula for the prime-weighted sequence. Their Selberg control `a_n^+=(1+lambda(n))/2` satisfies `(R)` deeply but fails `(B)`, exactly where it must: its total prime-factor parity has been frozen by construction.

This distinction matters for `prime_lattice`. Divisibility counts, residue labels, finite or slowly growing coordinate marginals and Kubilius local models are Type-I/local information. A bilinear expression couples two complementary factor ranges and carries a sign depending on their **combined** factorization. It therefore reads information across the coordinate cutoff rather than merely enlarging the cutoff one prime at a time.

No novelty is claimed for this Type-I/Type-II distinction or for parity-sensitive sieves. The relevant primary source is:

- John Friedlander and Henryk Iwaniec, “Asymptotic sieve for primes,” *Annals of Mathematics* **148** (1998), 1041--1065, DOI `10.2307/121035`, arXiv `math/9811186`. The opening discussion identifies the classical parity limitation; equations `(R)` and `(B)` separate divisor-distribution from the additional bilinear input; the Selberg example `a_n=(1+lambda(n))/2` is given immediately after the theorem to show why `(B)` is load-bearing.
- Atle Selberg, “On elementary methods in prime-number theory and their limitations,” Proc. 11th Scandinavian Mathematical Congress, Trondheim (1949), 13--22; reprinted in *Collected Papers*, Vol. I, Springer, 1989, 388--397. Friedlander--Iwaniec cite this as the classical source of the limitation.

## 3. Why this is directly relevant to the shifted-prime target

For fixed `h`, local information about `q+h` is naturally divisibility information. For a prime power `ell^k`, the condition

\[
\ell^k\mid q+h
\]

is the residue condition

\[
q\equiv-h\pmod{\ell^k}.
\]

`PL-185` shows that small-modulus residue targets are scalarized by Siegel--Walfisz in the affine phase regime under study. `PL-186` goes much further: Ford's theorem simultaneously models the complete valuation vector below `y=X^{o(1)}` in total variation. Therefore every bounded statistic of that whole local exponent block is already under probabilistic control.

Yet the full sign uses the entire factorization:

\[
\lambda(q+h)=(-1)^{\sum_\ell v_\ell(q+h)},
\]

and on squarefree values the Möbius sign is the same parity character. The factors above `y` can flip that sign. Classical sieve parity shows why this is not an accidental inconvenience of Ford's cutoff: local divisor distributions, even when very strong, are not by themselves a mechanism for determining the total number-of-prime-factors parity.

This interpretation is consistent with the best validated theorem on the actual shifted-prime Möbius problem. Lichtman's peer-reviewed result proves cancellation only after averaging over the shift, and the proof does **not** obtain the sign from sieve marginals alone. Standard sieve estimates first remove atypical factorizations; the parity-sensitive step then uses Fourier decoupling together with Matomäki--Radziwiłł--Tao-type averaged Möbius/Chowla input. The fixed prescribed shift remains the folklore conjectural frontier.

Primary target-specific anchor:

- Jared Duker Lichtman, “Averages of the Möbius Function on Shifted Primes,” *The Quarterly Journal of Mathematics* **73**(2) (2022), 729--757, DOI `10.1093/qmath/haab054`, arXiv `2009.08969`.

This does not prove that the missing fixed-shift estimate is literally equivalent to a Friedlander--Iwaniec `(B)` estimate. It shows instead that every validated route that actually crosses the parity wall must supply information of a different kind from the one-point/local sieve data classicalized in `PL-185`--`PL-186`.

## 4. Adversarial boundaries

The conclusion is deliberately narrower than “sieve theory cannot see parity.” Friedlander--Iwaniec themselves break the parity problem once additional analytic data are supplied. The obstruction concerns the **original/classical local-divisor input class**, not every method bearing the name sieve and not every possible theorem about a growing exponent vector.

Likewise, `PL-186` cannot be upgraded to an impossibility theorem saying that all information above `X^{o(1)}` is inaccessible. A future theorem could control a joint statistic involving small and large factors, a bilinear factorization across complementary ranges, or even the complete shifted factorization. Such a theorem would leave the parity-blind class precisely because it contains nonlocal information.

There is also no RH implication here. Cancellation of `mu(q+h)` or `lambda(q+h)` for a fixed shift is already a difficult pseudorandomness problem, but this finding supplies no quantitative bridge from such cancellation to the zero-free half-plane `Re(s)>1/2`. The result is a research-direction filter: it prevents local coordinate refinement from being mistaken for an RH-sensitive mechanism.

Finally, the Selberg matched control lives on all integers rather than on the shifted-prime sequence itself. It is used as a **falsification control for the information class**, not as a counterexample to the shifted-prime conjecture. Any stronger claim that the exact affine sequence satisfies or fails a particular Friedlander--Iwaniec bilinear axiom would require a separate derivation.

## Consequence for the research line

After `PL-186` and `PL-187`, the affine branch has a sharper surviving target. `PL-187` already shows that broad frequency-window averaging destroys even an arbitrary bounded hard target. `PL-188` now shows that, without such averaging, merely increasing local factorization/divisibility resolution still stays inside a classical parity-blind information class.

A live affine/exponent-lattice candidate should therefore expose an explicit cross-tail object before assigning geometric or spectral meaning. Examples of admissible *forms* include a bilinear factor-range coupling, a signed Möbius/Chowla correlation, a genuinely joint large-factor statistic, or a completed source/target operator whose matrix elements provably contain such information. The decisive audit question is:

\[
\boxed{
\text{what term in the proposed construction is impossible to recover from Type-I/local divisor marginals alone?}
}
\]

If there is no such term, the candidate has not escaped the classical sieve parity barrier and should be rejected as another local-coordinate reformulation. If there is one, that term -- not the surrounding lattice, trace, phase, or spectral packaging -- is the mathematical object that must be estimated and novelty-audited.