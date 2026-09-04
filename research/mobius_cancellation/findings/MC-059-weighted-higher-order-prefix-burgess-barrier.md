# MC-059 — Weighted higher-order prefix agreement still forces a near-quartic conductor

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let `q` be prime, let `chi` be a Dirichlet character modulo `q` of order strictly larger than `2`, and fix `X>=2`. Put

\[
\psi=\chi^2.
\]

Then `psi` is a nonprincipal primitive character modulo `q`. Define the weighted squared-phase defect

\[
B_X(\chi)
:=
\sum_{p\le X}
\frac{|1-\chi(p)^2|}{p-1}.
\tag{1}
\]

If there is a fixed `eta in (0,1]` such that

\[
\boxed{B_X(\chi)\le 1-\eta,}
\tag{2}
\]

then the squared character has a linearly large initial sum:

\[
\boxed{
\left|\sum_{n\le X}\chi(n)^2\right|
\ge \eta X.
}
\tag{3}
\]

Consequently the classical Burgess character-sum estimate implies that, for every fixed `delta>0`,

\[
\boxed{
q\gg_{\eta,\delta} X^{4-\delta}.
}
\tag{4}
\]

There is a direct approximate-Möbius corollary. Define

\[
A_X(\chi)
:=
\sum_{p\le X}
\frac{|1+\chi(p)|}{p-1}.
\tag{5}
\]

Since `|chi(p)|<=1`,

\[
|1-\chi(p)^2|
=|1-\chi(p)|\,|1+\chi(p)|
\le 2|1+\chi(p)|,
\]

so

\[
\boxed{
A_X(\chi)\le \frac{1-\eta}{2}
\quad\Longrightarrow\quad
q\gg_{\eta,\delta}X^{4-\delta}.
}
\tag{6}
\]

Thus the exact higher-order interpolation condition in `MC-058`, `chi(p)=-1` for every prime `p<=X`, can be relaxed substantially without making a low-conductor character certificate cheap. It is enough that the **squared phase** remain close to the principal character in the explicit generator-weighted sense `(2)`; direct Burgess then already forces a near-quartic conductor.

The exponent is deliberately weaker than the `X^(4 sqrt(e)-o(1))` floor in `MC-058`. Exact agreement there turns every integer through `X` into a power residue and allows least-power-nonresidue amplification. Under weighted approximate agreement that exact semigroup statement disappears, but the remaining phase information still forces a large ordinary character sum and therefore retains the classical Burgess `1/4` complexity barrier.

No estimate for `M(X)` follows. This is an unconditional complexity obstruction for one higher-order approximate-character comparator class.

## 1. Prime-generator phase defect controls the whole integer prefix

The key point is an elementary multiplicative telescoping inequality. For every positive integer

\[
n=\prod_p p^{v_p(n)},
\]

write the product defining `psi(n)` as a product of `v_p(n)` copies of `psi(p)`. Every Dirichlet-character value has modulus at most one, so repeated use of

\[
|1-zw|
\le |1-z|+|z|\,|1-w|
\le |1-z|+|1-w|
\]

gives

\[
|1-\psi(n)|
\le
\sum_p v_p(n)|1-\psi(p)|.
\tag{7}
\]

This remains valid if `q|n`, because then `psi(n)=0` and the factor at the conductor prime has modulus zero rather than one.

Summing `(7)` over `n<=X` and exchanging the finite sums gives

\[
\begin{aligned}
\sum_{n\le X}|1-\psi(n)|
&\le
\sum_{p\le X}|1-\psi(p)|
\sum_{n\le X}v_p(n)\\
&=
\sum_{p\le X}|1-\psi(p)|
\sum_{j\ge1}\left\lfloor\frac{X}{p^j}\right\rfloor.
\end{aligned}
\tag{8}
\]

The valuation count has the elementary bound

\[
\sum_{j\ge1}\left\lfloor\frac{X}{p^j}\right\rfloor
\le
X\sum_{j\ge1}p^{-j}
=
\frac{X}{p-1}.
\tag{9}
\]

Since `psi(p)=chi(p)^2`, equations `(1)`, `(8)`, and `(9)` yield the exact transfer inequality

\[
\boxed{
\sum_{n\le X}|1-\chi(n)^2|
\le X B_X(\chi).
}
\tag{10}
\]

The weight `1/(p-1)` is not chosen by analogy with pretentious distance. It is forced by the total number of appearances of the prime generator `p` in the factorizations of integers up to `X`. In that sense `(10)` is an explicit local-to-global Lipschitz bound for the multiplicative map from prime phases to the finite integer prefix.

## 2. A defect below one leaves a linearly large principal component

Write

\[
\sum_{n\le X}\psi(n)
=
X-
\sum_{n\le X}(1-\psi(n)).
\]

By the reverse triangle inequality and `(10)`,

\[
\begin{aligned}
\left|\sum_{n\le X}\psi(n)\right|
&\ge
X-
\left|\sum_{n\le X}(1-\psi(n))\right|\\
&\ge
X-
\sum_{n\le X}|1-\psi(n)|\\
&\ge
X\bigl(1-B_X(\chi)\bigr).
\end{aligned}
\tag{11}
\]

Assumption `(2)` therefore proves `(3)`.

This argument is intentionally one-sided. The condition `B_X<1` is sufficient, not necessary, for a large character sum. It makes no independence assumption and does not average over characters. The entire conclusion comes from multiplicativity plus the weighted prime-phase budget.

There is also no hidden exact-prefix hypothesis. A character may deviate from `-1` at many observed primes and still satisfy `(6)` if the total weighted phase error is small enough. Conversely, a small number of low primes can consume most of the budget because the generator multiplicity weight is large there. That asymmetry is intrinsic to the proof and is one reason this is not merely an unweighted Hamming approximation statement.

## 3. Higher order is exactly what makes Burgess available after squaring

Let `r=ord(chi)>2`. Since `chi` is a character modulo the prime `q`, its order divides `q-1`. The squared character has order

\[
\operatorname{ord}(\psi)
=
\frac{r}{\gcd(r,2)}.
\]

This is greater than one for every `r>2`, so `psi` is nonprincipal. Every nonprincipal character modulo a prime is primitive. Thus the prime modulus is cubefree and the arbitrary-fixed-parameter form of Burgess used in `MC-056` and anchored by `MC-S34` applies to `psi`.

For every fixed integer `R>=1` and every `epsilon>0`, Burgess gives

\[
\left|\sum_{n\le X}\psi(n)\right|
\ll_{R,\varepsilon}
X^{1-1/R}
q^{(R+1)/(4R^2)+\varepsilon}.
\tag{12}
\]

Combining `(3)` and `(12)` gives

\[
\eta X^{1/R}
\ll_{R,\varepsilon}
q^{(R+1)/(4R^2)+\varepsilon}.
\tag{13}
\]

For fixed `R`, taking the Burgess epsilon arbitrarily small makes the corresponding conductor exponent arbitrarily close to

\[
\frac{4R}{R+1}.
\]

Given `delta>0`, choose `R` large enough that `4R/(R+1)>4-delta/2`, then choose the Burgess epsilon small enough that the remaining exponent loss is below `delta/2`. Absorbing the fixed `eta`, `R`, and epsilon constants gives `(4)`.

No statement about zeta zeros, no Mertens estimate, and no analytic continuation of `1/zeta` enters this deduction.

## 4. Approximate Möbius prime signs imply the squared-phase hypothesis

At an observed prime, Möbius has value `mu(p)=-1`. For any complex number `z` with `|z|<=1`,

\[
|1-z^2|=|1-z|\,|1+z|\le2|1+z|.
\tag{14}
\]

Taking `z=chi(p)`, summing with weight `1/(p-1)`, and using `(5)` gives

\[
B_X(\chi)\le2A_X(\chi).
\tag{15}
\]

Hence `(6)` follows from `(4)`.

This corollary is useful as a falsification rule for the surviving boundary of `MC-058`. A higher-order character cannot be made into a polynomially low-conductor approximate Möbius-prefix certificate merely by replacing exact conditions `chi(p)=-1` with uniformly small weighted phase errors. If the error budget is small enough to leave a fixed principal component after squaring, the same `q=X^(4-o(1))` Burgess barrier reappears.

The squaring step deliberately forgets some information. In particular, a prime with `chi(p)=+1` has zero squared-phase defect even though its Möbius-sign error is maximal. Therefore `(2)` is weaker than genuine closeness to the Möbius prime law, and `(6)` is only one sufficient way to enter it. This loss is a feature of the obstruction: even after discarding the sign distinction between `+1` and `-1`, enough coherent multiplicative phase remains to force large conductor.

## 5. Relation to the exact-prefix and pretentious barriers

`MC-058` starts from exact higher-order interpolation. Squaring then gives

\[
\psi(n)=1
\qquad(1\le n\le X),
\]

so the least power nonresidue lies beyond `X`. Classical smooth-number amplification strengthens the direct Burgess scale from `q=X^(4-o(1))` to the least-power-nonresidue exponent `q=X^(4 sqrt(e)-o(1))`.

The present finding shows what survives when exactness is removed. Condition `(2)` no longer guarantees a nonresidue-free prefix, so the `4 sqrt(e)` amplification cannot simply be imported. But `(10)` says the weighted prime-generator defect still controls the total integer-prefix defect, and a fixed residual principal component is enough for direct Burgess. The natural exponent therefore drops to the near-quartic character-sum boundary rather than disappearing altogether.

This is also distinct from ordinary pretentious distance. Standard pretentious weights are of order `1/p` and typically enter logarithmic/exponential mean-value estimates; `MC-002` and `MC-045` show why a one-scale prime-harmonic scalar can miss power-sized endpoint information. Here the quantity is used for a different purpose: after squaring a **Dirichlet character**, the total weighted phase defect is required to stay below a fixed absolute threshold, which forces the full initial character sum itself to retain linear size. The conclusion then comes from Burgess, not from Halász.

`MC-047` already showed that the Jung--Lemke Oliver power-aware carrier repairs the particular terminal-prime invisibility of ordinary pretentiousness. The current obstruction is complementary: it acts on a moving higher-order character certificate and converts sufficiently coherent approximate prime data directly into a conductor lower bound. Neither result supplies an unconditional cancellation estimate for Möbius.

## 6. Prior art and novelty boundary

The decisive analytic theorem is classical Burgess character-sum theory, already anchored as `MC-S34`: Enrique Treviño, *The Burgess inequality and the least k-th power non-residue*, International Journal of Number Theory 11 (2015), 1653–1678, DOI `10.1142/S1793042115400163`, arXiv `1412.3062`. The same source is used by `MC-056` and `MC-058` for direct character sums and least-power-nonresidue bounds.

The general literature on least character nonresidues, large character sums, and high-order character value distribution already studies how long a nonprincipal character may remain principal-like. A targeted search around weighted prime defects and high-order character clustering found that established literature rather than a separate novelty basis for `(4)`. No standalone theorem novelty is claimed.

The line-specific contribution is the elementary exact bridge `(10)` from a **weighted approximate prime-phase condition** left open by `MC-058` to a linearly large initial sum of `chi^2`, followed by the classical Burgess complexity bound. It should therefore be read as a Mathia-specific matched-control obstruction assembled from standard character theory, not as a new character-sum theorem.

## 7. Boundaries and surviving route

The conclusion has several load-bearing restrictions.

- The character must have order greater than `2`. For quadratic `chi`, `chi^2` is principal and this squared-character Burgess argument disappears; the different quadratic obstruction in `MC-057` remains relevant.
- The weighted defect must leave a fixed gap below one. The argument gives only `|sum psi| >= X(1-B_X)`; if `B_X` approaches one or exceeds it, this proof supplies no useful character-sum lower bound.
- The result constrains conductor complexity, not the comparator's Möbius-weighted partial sum and not `M(X)` itself.
- The near-quartic exponent comes from direct Burgess and is not asserted sharp. Exact agreement permits the stronger least-power-nonresidue amplification of `MC-058`.
- Squaring discards the distinction between the phases `+1` and `-1`; the theorem does not by itself quantify how many actual Möbius sign errors a character may contain.
- No existence theorem is provided for characters near the conductor floor, and no uniform cancellation theorem for a moving comparator family follows from the lower bound.

Accordingly, the approximate-character escape after `MC-058` is narrowed but not closed. A surviving low-complexity higher-order route must leave the small-defect regime `(2)`, abandon a single Dirichlet-character certificate, or exploit signed/multiscale structure that is not compressed into the squared-phase generator budget. Any future approximate-prefix proposal should compute `B_X(chi)` first: if it remains below `1-eta`, Burgess already rules out conductor `X^(4-c)` for every fixed `c>0`.