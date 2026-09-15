# MC-302 — Quadratic large sieve extends the source horizon but not the endpoint energy budget

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`, `NON-RH`.

## Claim

Continue the source-character setup of `MC-293`–`MC-301`. Let

\[
\mathcal R_y
=\{r:y<r\le2y,\ r\text{ prime},\ r\equiv1\pmod4\},
\qquad N=|\mathcal R_y|,
\]

let `H` be the binary span of the occupied lower-prime Legendre sign cells, and for `\lambda\in H^*` write

\[
x_\lambda
=\frac1N\sum_{r\in\mathcal R_y}(-1)^{\lambda(s(r))}.
\]

For nonzero `\lambda`, let `\mathcal Q(\lambda)` be the minimum lower-prime product source cost of `MC-293`. Choosing a minimizing squarefree representative gives the primitive real character

\[
\chi_\lambda(n)=\left(\frac{n}{m_\lambda}\right),
\qquad
m_\lambda=\mathcal Q(\lambda),
\]

and `MC-301` proves

\[
Nx_\lambda=\sum_{r\in\mathcal R_y}\chi_\lambda(r),
\]

with distinct `\lambda` giving distinct selected real characters.

Define the cumulative low-source Fourier energy

\[
E_y(C)
:=
\sum_{\substack{\lambda\ne0\\\mathcal Q(\lambda)\le C}}
|x_\lambda|^2.
\]

Because every selected source character is quadratic, Heath-Brown's quadratic large sieve applies more efficiently than the generic multiplicative large sieve used in `MC-301`. For every fixed `\varepsilon>0`,

\[
\boxed{
E_y(C)
\ll_\varepsilon
(Cy)^\varepsilon
\left(1+\frac Cy\right)\log y.
}
\tag{1}
\]

Using Zihao Liu's 2026 explicit version, this can be made uniform in the varying parameters as

\[
\boxed{
E_y(C)
\le
L(Cy)
\left(1+\frac Cy\right)\log y,
\qquad
L(X)=\exp\!\left(O\!\left(\frac{\log X}{\log^{(4)}X}\right)\right),
}
\tag{2}
\]

for sufficiently large `Cy`, with an absolute constant hidden in the `O`-term. In particular, for `C\le y`,

\[
\boxed{
E_y(C)\le y^{o(1)}\log y.
}
\tag{3}
\]

This replaces the generic large-sieve conductor factor

\[
1+C^2/y
\]

from `MC-301` by the quadratic-family factor

\[
1+C/y.
\]

So the natural collective source horizon moves from square-root conductor to linear conductor.

However, this does **not** repair the live endpoint gap. For the reciprocal endpoint partition of `MC-295`–`MC-301`, an `R`-dimensional selected subspace `L` has exact total Fourier energy

\[
\sum_{\lambda\in L}|x_\lambda|^2=\frac{2^R}{R}.
\tag{4}
\]

At the blind-support floor from `MC-242`,

\[
R=\log_2\log y+o(\log\log y),
\tag{5}
\]

so

\[
\frac{2^R}{R}
=
\frac{(\log y)^{1+o(1)}}{R}.
\tag{6}
\]

Even an **idealized loss-free** quadratic-large-sieve estimate of the same `(C+y)` theorem shape would give, for `C\le y`, only

\[
E_y(C)\ll\log y.
\tag{7}
\]

The right side of `(7)` is larger than the **entire** reciprocal-partition energy `(6)` by a factor of order `R` at the critical floor. Therefore removing Liu's subpower loss, improving constants, or merely exploiting the fact that the source characters are quadratic cannot by itself force any endpoint energy above conductor `y` at the live rank.

With the actually available explicit theorem the comparison is weaker still. Combining `(2)` and `(4)` can certify positive energy above `C\le y` only when

\[
\frac{2^R}{R}
>
1+L(Cy)\left(1+\frac Cy\right)\log y.
\tag{8}
\]

At `C=y` this requires, up to constants in the explicit loss,

\[
R
\gtrsim
\log_2\log y
+\log_2R
+\log_2 L(y^2),
\tag{9}
\]

where

\[
\log L(y^2)
=O\!\left(\frac{\log y}{\log^{(4)}y}\right).
\tag{10}
\]

Thus the quadratic large sieve buys a much larger **conductor horizon**, but its published uniform form does not buy the missing **energy factor**. More importantly, `(7)` shows that this failure is not solely an artifact of Liu's explicit `\varepsilon`-dependence: the black-box `(C+y)\|a\|_2^2` envelope still has enough capacity to contain the complete reciprocal endpoint spectrum at the blind-support floor even if the subpower loss were removed entirely.

No estimate for `M(x)`, no improvement of the blind-support floor, and no proof that the actual shell realizes the reciprocal endpoint partition follows.

## 1. The source family is exactly a quadratic-large-sieve subfamily

Fix nonzero `\lambda` and a minimizing lower-prime representative `V`. As in `MC-301`, put

\[
m_\lambda=\prod_{p\in V}p=\mathcal Q(\lambda).
\]

The moduli in `V` are distinct odd primes, so `m_\lambda` is odd and squarefree and

\[
\chi_\lambda(n)
=\prod_{p\in V}\left(\frac np\right)
=\left(\frac n{m_\lambda}\right).
\tag{11}
\]

For shell primes `r\equiv1\pmod4`, quadratic reciprocity gives

\[
\chi_\lambda(r)
=\prod_{p\in V}\left(\frac rp\right)
=\prod_{p\in V}\left(\frac pr\right)
=(-1)^{\lambda(s(r))}.
\tag{12}
\]

Hence

\[
Nx_\lambda
=\sum_{r\in\mathcal R_y}
\left(\frac r{m_\lambda}\right).
\tag{13}
\]

Distinct shell functionals give distinct selected characters, by the injectivity argument already recorded in `MC-301`. Thus the family with `\mathcal Q(\lambda)\le C` can be inserted into a quadratic-large-sieve sum over odd squarefree `m\le C` without multiplicity.

This is the key difference from the generic character treatment in `MC-301`: the selected source family is not merely primitive and real; it is literally a Jacobi-symbol family indexed by squarefree conductors.

## 2. Heath-Brown gives a linear rather than quadratic conductor term

Heath-Brown's quadratic large sieve states, in the standard squarefree form, that for every fixed `\varepsilon>0`,

\[
\sum_{m\le M}^{*}
\left|
\sum_{n\le Y}^{*}
a_n\left(\frac nm\right)
\right|^2
\ll_\varepsilon
(MY)^\varepsilon(M+Y)
\sum_{n\le Y}^{*}|a_n|^2,
\tag{14}
\]

where the stars restrict to odd squarefree variables. Take `Y=2y` and

\[
a_n=
\mathbf 1_{\{n\in\mathcal R_y\}}.
\tag{15}
\]

Every supported `n` is an odd prime and therefore squarefree, and

\[
\sum_n|a_n|^2=N.
\tag{16}
\]

Restricting the nonnegative outer sum in `(14)` to the selected `m_\lambda\le C`, then using `(13)`, gives

\[
N^2E_y(C)
\ll_\varepsilon
(Cy)^\varepsilon(C+y)N.
\tag{17}
\]

The prime number theorem in the fixed progression `1 mod 4` gives

\[
N\sim\frac{y}{2\log y},
\tag{18}
\]

so division by `N^2` proves `(1)`.

The improvement over `MC-301` is structural. The ordinary multiplicative large sieve pays `y+C^2`; the quadratic family pays `y+C`, up to its characteristic subpower loss. Consequently the conductor at which the second term becomes comparable with the interval length moves from `C\asymp\sqrt y` to `C\asymp y`.

## 3. Liu makes the parameter loss auditable

For a fixed `\varepsilon`, `(1)` is insufficient for a frontier in which `C` and the selected dimension vary with `y`: the hidden constant may depend arbitrarily on `\varepsilon`, so one cannot silently choose `\varepsilon=\varepsilon(y)`.

Liu's explicit quadratic large sieve resolves exactly that bookkeeping issue. In the notation already audited in `MC-262`, his theorem gives the dyadic quadratic-large-sieve constant

\[
\mathcal B(M,Y)
\le
\exp_4(A\varepsilon^{-1})(MY)^\varepsilon(M+Y)
\tag{19}
\]

for an absolute `A>0`, and the initial-range form has the same fourth-iterated-exponential dependence. Optimizing `\varepsilon` yields the subpower multiplier

\[
L(MY)
=
\exp\!\left(
O\!\left(\frac{\log(MY)}{\log^{(4)}(MY)}\right)
\right).
\tag{20}
\]

Applying the same restriction as in Section 2 proves `(2)`.

This is the **source-side** specialization of the same classical theorem used in `MC-262`. `MC-262` placed products of shell primes in the outer modulus variable in order to study high-order blind relations. Here the outer moduli are instead the minimizing products of lower-prime source coordinates attached to shell Fourier modes. The two applications therefore have different arithmetic objects and different frontier questions even though the analytic inequality is the same.

## 4. The reciprocal endpoint exposes a theorem-shape barrier independent of the explicit loss

The exact reciprocal endpoint profile from `MC-296` is

\[
x_{\lambda_I}
=(-1)^{|I|}
\left(1-\frac{2|I|}{R}\right)
\qquad(I\subseteq[R]),
\tag{21}
\]

and `MC-301` sums its squares to obtain `(4)`.

At the critical rank `(5)`, equation `(6)` follows. Compare this not first with the published quadratic large sieve, but with the stronger hypothetical estimate obtained by deleting **all** `\varepsilon` and subpower losses from `(14)` while retaining its natural `M+Y` scale. The resulting source-energy conclusion for `C\le y` is exactly `(7)`.

But

\[
\frac{\log y}{2^R/R}
=R(\log y)^{o(1)}
\tag{22}
\]

at `(5)`. Therefore the hypothetical upper bound remains compatible with placing the entire selected endpoint spectrum below the conductor cap. It cannot imply that any positive endpoint energy must escape above `C`.

This is a narrower but stronger negative conclusion than merely observing that Liu's explicit loss is large. The live mismatch has two layers:

1. **published uniformity loss:** the known quadratic theorem carries `L(Cy)=y^{o(1)}` in the polynomial conductor range;
2. **intrinsic black-box energy mismatch:** even if that loss vanished, an `O(log y)` source-energy envelope is still too large by a factor of order `R` compared with the reciprocal endpoint spectrum at the blind-support floor.

Only the first layer is a defect of the current quadratic-large-sieve technology. The second says that a successful collective theorem must exploit additional structure beyond replacing the generic character family by all quadratic characters.

This does **not** prove an information-theoretic lower bound of `\log y` for every possible theorem. A thinner selected-family estimate, a maximum/large-deviation theorem, or an arithmetic coupling among the selected conductors could have a smaller effective capacity. The claim concerns the black-box all-quadratic-family mean-square envelope.

## 5. Prior art and novelty audit

The analytic input is classical. D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica **72** (1995), no. 3, 235–275, DOI `10.4064/aa-72-3-235-275`, proves the quadratic large sieve underlying `(14)`.

Zihao Liu, *Explicit quadratic large sieve inequality*, Acta Arithmetica **223** (2026), no. 3, 227–252, DOI `10.4064/aa250722-27-1`, published online 19 May 2026, makes the `\varepsilon`-dependence explicit. The paper's Theorem 1 gives the fourth-iterated-exponential dependence used in `(19)`, and its initial-range corollaries yield the optimized subpower form `(20)`. These are Liu's theorems, not Mathia results.

A targeted literature check on 15 September 2026 found no later general quadratic-character large-sieve theorem that replaces the `(M+Y)(MY)^{o(1)}` envelope by a source-family-specific capacity capable of supplying the missing reciprocal-endpoint factor. Nearby 2026 work on large sieves for polynomial or quadratic moduli concerns different modulus families and does not alter the application above. This is not a completeness claim.

No novelty is claimed for quadratic reciprocity, Jacobi-symbol factorization, the Heath-Brown inequality, Liu's explicit refinement, or the generic observation that a coarse mean-square bound can be too large to detect a smaller structured spectrum. The durable Mathia delta is the exact **source-side comparison** with `MC-301`: quadraticity enlarges the collective conductor horizon from `sqrt(y)` to `y`, while the reciprocal endpoint calculation proves that even the ideal loss-free theorem shape does not repair the live factor-`R` energy deficit.

## Boundaries and falsification tests

- The argument depends on the source representatives being products of distinct odd lower primes, so that `(11)` lies in the squarefree Jacobi-symbol family. This is exactly the source-cost model of `MC-293`–`MC-301`.
- The supported coefficient sequence consists of shell primes, hence satisfies the squarefree inner-variable restriction in `(14)` without modification.
- The selected family is only a subset of all squarefree quadratic moduli. Equations `(1)` and `(2)` are capacity upper bounds and are not claimed sharp for the actual selected family.
- Equation `(2)` uses Liu's explicit parameter dependence; one may not obtain it by choosing a varying `\varepsilon` inside an unspecified `\ll_\varepsilon` constant.
- Equation `(7)` is an **idealized theorem-shape audit**, not a proved sharper large-sieve theorem. It intentionally grants the route the removal of every subpower loss to test whether that alone could close the endpoint.
- Failure of `(7)` to contradict `(6)` does not rule out a thin-family large sieve, inverse large sieve, maximum estimate, conductor-coupling theorem, or another argument whose capacity is genuinely below the all-quadratic-family diagonal scale.
- No claim is made that the actual Legendre shell attains the reciprocal endpoint partition. The partition remains an exact finite control showing what the current generic information permits.
- No RH, GRH, critical-strip zero-free region, random-walk model, or continuation of `1/\zeta(s)` is used. No bound for `M(x)` follows.

## Consequence for the active frontier

`MC-301` left the square-root source horizon as an artifact of the generic multiplicative large sieve. The present finding removes that artifact: the actual source family is quadratic, and the classical quadratic large sieve reaches linear conductor collectively.

That does not close the frontier. At the blind-support rank, the reciprocal endpoint obstruction carries only about `log y / R` total Fourier energy, whereas even the ideal loss-free all-quadratic mean-square envelope permits `O(log y)` below conductor `y`. The missing factor of order `R` therefore survives the quadratic refinement.

The next useful collective theorem must do something qualitatively more source-specific: reduce the capacity of the **selected varying-conductor family** below the all-quadratic envelope, prove that the actual arithmetic obstruction carries more than reciprocal-partition energy, or exploit algebraic/arithmetic coupling among the selected conductors so that their biases cannot spend the generic quadratic-large-sieve budget independently.