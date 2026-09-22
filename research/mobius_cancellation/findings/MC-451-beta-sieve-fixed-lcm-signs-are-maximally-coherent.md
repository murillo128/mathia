# MC-451 — Beta-sieve fixed-lcm signs are maximally coherent for coprime shifts

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the fixed-lcm incomplete-correlation branch of `MC-413` and the resonant-band obstruction of `MC-450`. Let the sieve divisors be squarefree and let

\[
\lambda_d=\mu(d)\rho_d,
\qquad \rho_d\ge 0,
\tag{1}
\]

with finite support. This includes the standard Rosser--Iwaniec/beta-sieve sign pattern and, in particular, Maynard's well-factorable upper-bound variant `\widetilde\lambda_d^+`, for which the retained coefficient is `(-1)^{\omega(d)}=\mu(d)` on the admissible divisor set and zero otherwise.

Fix a nonzero shift `h` and a squarefree lcm `L` with

\[
(L,h)=1.
\tag{2}
\]

For every supported compatible divisor pair `(d,e)` satisfying

\[
[d,e]=L,
\qquad (d,e)\mid h,
\tag{3}
\]

the coprimality in `(2)` forces

\[
(d,e)=1,
\qquad de=L.
\tag{4}
\]

Let `r=r(d,e)` be the canonical CRT residue

\[
r\equiv0\pmod e,
\qquad r\equiv-h\pmod d,
\qquad 0\le r<L.
\tag{5}
\]

As in `MC-447`, different ordered factorizations `de=L` produce different residues `r`. Hence the fixed-lcm start-set coefficient in `MC-450` is simply

\[
c_{L,r(d,e)}=\lambda_d\lambda_e.
\tag{6}
\]

Define its zero mode and total variation by

\[
A_L:=\sum_r c_{L,r},
\qquad
V_L:=\sum_r|c_{L,r}|.
\tag{7}
\]

Then every nonzero term in the fixed-lcm slice has the **same sign**:

\[
\lambda_d\lambda_e
=\mu(d)\mu(e)\rho_d\rho_e
=\mu(L)\rho_d\rho_e.
\tag{8}
\]

Therefore

\[
\boxed{
A_L
=\mu(L)\!\sum_{\substack{de=L\\ d,e\ \mathrm{supported}}}\rho_d\rho_e,
\qquad
V_L
=\sum_{\substack{de=L\\ d,e\ \mathrm{supported}}}\rho_d\rho_e,
\qquad
|A_L|=V_L.
}
\tag{9}
\]

Equivalently, on squarefree `L` the zero mode is the Dirichlet-convolution value

\[
A_L=(\lambda*\lambda)(L)
=\mu(L)(\rho*\rho)(L)
\tag{10}
\]

with the convolution restricted automatically to coprime factor pairs. The Möbius signs do not cancel at fixed lcm; they **factor out globally as `\mu(L)`**.

Consequently the resonant-band inequality of `MC-450` applies with its strongest possible parameter `\eta=1`. For prime source conductor `p`, `(L,p)=1`, and

\[
W_L(u):=\sum_r c_{L,r}\mathbf 1_{u=rL^{-1}},
\tag{11}
\]

one has

\[
\boxed{
|\widehat W_L(-mL)|\ge \frac12V_L
\quad\text{whenever}\quad
|m|\le \frac{p}{4\pi L}.
}
\tag{12}
\]

Thus, in the clean coprime-shift regime already isolated by `MC-447`, the **total** Rosser--Iwaniec/beta-sieve coefficient cannot evade the low-frequency resonance of `MC-450` through signed fixed-lcm cancellation. Its signs are maximally coherent.

This does **not** close well-factorability itself. Maynard's factorable representation writes the same total sieve coefficient as a finite sum of signed convolutional components. Cancellation may still occur **between or inside those components before they are summed back to `\lambda^+`**, or in a genuinely coefficient-sensitive dispersion form involving the translated-character multiplier. What is closed is the simpler escape in which one hopes that the ordinary Möbius sign pattern of the total upper-sieve coefficients already makes `A_L` small on each fixed-lcm slice.

No estimate for an incomplete character sum, a twisted Mertens sum, or `M(x)` follows.

## 1. The coprime-shift CRT slice is a Boolean partition of the primes of `L`

There are three useful representations of the same fixed-lcm object.

In divisor-pair coordinates, `(L,h)=1` and `(d,e)|h` imply `(d,e)=1`; together with `[d,e]=L`, this gives `de=L`. Every prime of `L` is assigned to exactly one of `d` or `e`.

In CRT-idempotent coordinates, `MC-447` shows that the residue `r` records exactly this binary assignment. If `q|L`, then either

\[
r\equiv0\pmod q
\quad\text{or}\quad
r\equiv-h\pmod q,
\tag{13}
\]

and the two residues are distinct because `(h,L)=1`. Hence different prime partitions give different starts. There is no aggregation collision capable of changing the coefficient sign before the fixed-lcm Fourier transform is formed.

In Dirichlet-convolution coordinates, the same Boolean partition is precisely a divisor decomposition `de=L`, so summing the fixed-lcm coefficients gives `(\lambda*\lambda)(L)`. This representation exposes the semantic point hidden by the CRT notation: when `\lambda=\mu\rho` with nonnegative `\rho`, complete multiplicativity of the parity of `\omega` over coprime factors makes every summand carry the same outer sign `\mu(L)`.

The convolution representation is therefore not merely shorter notation. It identifies the exact structural reason the candidate cancellation fails: at fixed squarefree lcm and coprime shift, Möbius parity is a function of `L`, not of the Boolean partition of `L` between the two sieve divisors.

## 2. Exact sign coherence

Because `d` and `e` are squarefree and coprime,

\[
\mu(d)\mu(e)=\mu(de)=\mu(L).
\tag{14}
\]

Multiplying by the nonnegative amplitudes in `(1)` gives `(8)`. Summing over the supported factorizations proves the first identity in `(9)`, while taking absolute values termwise proves the second. Hence `|A_L|=V_L` exactly.

No assumption that every factorization of `L` lies in the sieve support is needed. Support restrictions merely delete some nonnegative amplitudes `\rho_d\rho_e`; every surviving term still has sign `\mu(L)`. In particular the statement remains valid when `L>D` but both factors happen to lie in the level-`D` support.

For a beta-sieve coefficient with `\rho_d\in\{0,1\}`, equation `(9)` reduces further to

\[
A_L=\mu(L)N_L,
\qquad
V_L=N_L,
\tag{15}
\]

where `N_L` is the number of admissible ordered supported factorizations `de=L`. The entire fixed-lcm zero mode is then a signed count, with no internal cancellation at all.

## 3. The `MC-450` resonant band is therefore unavoidable for the total weight

`MC-450` proved for arbitrary fixed-lcm coefficients that

\[
|\widehat W_L(-mL)-A_L|
\le \frac{2\pi |m|L}{p}V_L.
\tag{16}
\]

Its possible escape was explicitly that actual signed coefficients might make `|A_L|\ll V_L`. Equation `(9)` shows that this does not happen for the total beta-sieve coefficient in the coprime-shift regime: `|A_L|=V_L`.

Taking `|m|\le p/(4\pi L)` in `(16)` gives

\[
|\widehat W_L(-mL)|
\ge |A_L|-\frac12V_L
=\frac12V_L,
\tag{17}
\]

which is `(12)`. The bare start-set resonance from `MC-450` is therefore not only a support-geometric possibility here; it is forced by the classical sign pattern of the **recombined fixed-lcm upper-sieve coefficients**.

This is a local spectral obstruction, not a lower bound for the full translated-character correlation. The character multiplier `\widehat g_h(m)`, the interval kernel, and cancellation across different `L` may still suppress these frequencies. The result says specifically that one cannot obtain that suppression by claiming that the total Rosser--Iwaniec coefficient has already canceled its own fixed-lcm zero mode.

## 4. Why well-factorability remains live

The distinction between the total upper-sieve weight and its factorable decomposition is essential.

Maynard recalls Iwaniec's factorable variant of the linear-sieve upper weights and writes it, for a chosen factorization of the sieve level, as a bounded finite sum of convolutions. The **total** variant still has the beta-sieve sign pattern: if `d=p_1\cdots p_r` satisfies the admissibility inequalities, then `\widetilde\lambda_d^+=(-1)^r=\mu(d)`, and otherwise it is zero. This is exactly the form `(1)` with `\rho_d` an indicator.

But a decomposition

\[
\widetilde\lambda^+
=\sum_j \alpha^{(j)}*\beta^{(j)}
\tag{18}
\]

need not preserve that same-sign property component by component. Indeed, the analytic purpose of factorability is to expose signed variables before the total coefficient is reconstructed. A dispersion argument that keeps the `j`, `u`, and `v` variables alive could therefore use information that `(9)` deliberately discards.

So the frontier after `MC-451` is narrower than “use the actual signs”. The surviving question is:

> can the **pre-recombination factorable components** cancel against one another or against the translated-character multiplier in a way that changes the true dispersion diagonal before they reassemble into the sign-coherent total beta-sieve slice?

If the components are first summed to `\widetilde\lambda^+` and only then grouped by `L`, equation `(9)` has already removed this possible escape.

## 5. Prior art and novelty boundary

The sieve sign pattern is classical. Maynard, *Primes in arithmetic progressions to large moduli II: Well-factorable estimates* (Memoirs AMS 306 (2025), arXiv:2006.07088), Section 9, recalls the factorable variant of Iwaniec's upper linear-sieve weights. In the displayed construction, an admissible squarefree `d=p_1\cdots p_r` receives coefficient `(-1)^r` and an inadmissible `d` receives zero; the same section records the finite convolutional factorization of the variant. Maynard explicitly attributes the construction to Iwaniec, *A new form of the error term in the linear sieve* (Acta Arith. 37 (1980), 307--320).

The CRT injectivity for coprime shifts and the low-frequency inequality are already established internally by `MC-447` and `MC-450`. The identity `\mu(d)\mu(e)=\mu(de)` for coprime squarefree `d,e` and the convolution identity `(10)` are elementary.

A targeted literature search on 22 September 2026 found the standard Rosser--Iwaniec sign-alternation structure and the established well-factorable decomposition, but no reason to assign independent number-theoretic novelty to `(9)`. No novelty is claimed. The durable Mathia contribution is the branch-specific closure obtained by combining those classical signs with the exact fixed-lcm CRT/Fourier geometry already derived here: the most obvious “actual coefficient cancellation” escape left by the resonant-band statement of `MC-450` fails maximally for the total beta-sieve weight.

## Boundaries and falsification tests

- **Coprime shift is load-bearing.** If `(L,h)>1`, the divisor pair may have a nontrivial gcd. Then `\mu(d)\mu(e)=\mu(L)\mu((d,e))`, so common-prime assignments can change the sign. This regime is not covered by the maximal-coherence statement.
- **The coefficients must have the beta-sieve sign form `\mu(d)\rho_d` with `\rho_d\ge0`.** An arbitrary signed well-factorable sequence need not satisfy `(9)`.
- **The result concerns the total sieve coefficient.** Individual factorable components in `(18)` can have different signs and remain a legitimate pre-recombination resource.
- **Distinct CRT starts are required to identify `V_L` termwise.** This is guaranteed by `(L,h)=1` as in `MC-447`; with shift-common primes, several divisor assignments can share one start and aggregate before the Fourier transform.
- **The resonant band is not the full character sum.** Cancellation from the translated-character multiplier, interval factor, or cross-lcm interaction remains possible.
- **No source-depth gain is disproved in general.** The finding closes only the route that attributes the missing gain to zero-mode cancellation of the total beta-sieve signs on one coprime fixed-lcm slice.
- **No RH input enters.** The argument is finite divisor/CRT algebra plus the classical beta-sieve coefficient sign pattern.

## Consequence for the research line

`MC-450` left small fixed-lcm zero mode as one concrete way actual signed coefficients might defeat the deterministic low-frequency resonance. For the classical total Rosser--Iwaniec/beta-sieve upper weight, that escape is now closed in the clean regime used throughout `MC-447`--`MC-450`: the Möbius signs are constant across all coprime divisor partitions of a fixed squarefree lcm, so `|A_L|=V_L` exactly.

The next useful calculation should therefore stay **before total beta-sieve recombination**. It should retain the finite well-factorable decomposition `(18)` and compute the corresponding component-level dispersion/Gram form, asking whether its diagonal is genuinely smaller before the components sum back to `\widetilde\lambda^+`. A proof that first reconstructs the total `\mu(d)\rho_d` coefficient and then hopes for same-lcm sign cancellation has already lost by `(9)`.