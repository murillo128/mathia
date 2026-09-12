# MC-234 — Linnik-scale sign mixing covers the hard CRT region but remains amplitude-incomplete

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-233` reduces the diagonalized first-shell route to ordinary reduced-residue Möbius progression sums

\[
M_\mu(Z;q,a)
=
\sum_{\substack{n\le Z\\n\equiv a\pmod q}}\mu(n),
\]

with

\[
q=Q_S=X^{2\alpha+o(1)},
\qquad
Z=T/u=X^{1-\beta+o(1)},
\qquad
a=-Pu^{-1}\pmod q,
\tag{1}
\]

where `u` is the smooth dilation parameter. The component is genuinely hard only when

\[
2\alpha+\beta<\frac12.
\tag{2}
\]

A recent theorem of Matomäki and Teräväinen on Linnik's problem for multiplicative functions gives new unconditional information exactly at this interface. Their Möbius corollary implies that, for every fixed `epsilon>0`, every sufficiently large modulus `Q`, and every reduced residue class `A mod Q`, each sign `Delta in {+1,-1}` is assumed by `mu(n)` at some

\[
n\equiv A\pmod Q,
\qquad
n\ll_\varepsilon Q^{2+\varepsilon}.
\tag{3}
\]

Thus parity **existence** in every reduced class is available unconditionally at essentially the square-root barrier.

For the source-selected family `(1)`, the hard region `(2)` lies strictly inside the range where `(3)` forces both Möbius signs to occur before the component endpoint `Z`. More strongly, a CRT refinement amplifies the published existence theorem to the following quantitative sign-diversity statement: for every fixed `eta>0` and every fixed interior scaling pair `(alpha,beta)` satisfying `(2)`, one has, for each `Delta in {+1,-1}`,

\[
\boxed{
N_\Delta(Z;q,a)
:=
\#\{n\le Z:n\equiv a\pmod q,\ \mu(n)=\Delta\}
\ge
\frac{Z^{1/2-\eta}}{q}
}
\tag{4}
\]

for all sufficiently large `X` (with the threshold depending on `eta` and the fixed scaling pair).

However, the total square-free support in the same reduced progression satisfies the elementary asymptotic

\[
\boxed{
N_{\rm sf}(Z;q,a)
:=N_+(Z;q,a)+N_-(Z;q,a)
=
\left(\frac6{\pi^2}+o(1)\right)\frac Zq
}
\tag{5}
\]

throughout the hard region. Hence the black-box sign abundance obtained from `(3)` is only a vanishing fraction of the available support:

\[
\frac{Z^{1/2-o(1)}/q}{Z/q}
=Z^{-1/2+o(1)}.
\tag{6}
\]

By contrast, the `MC-233` componentwise sufficient target

\[
|M_\mu(Z;q,a)|\le X^{1/2+o(1)}
\tag{7}
\]

requires the two signs to be almost balanced at the power scale. Indeed, from `(5)` and

\[
M_\mu(Z;q,a)=N_+(Z;q,a)-N_-(Z;q,a)
\tag{8}
\]

one sees that `(7)` would force

\[
\min(N_+,N_-)
=
\frac12N_{\rm sf}+O(X^{1/2+o(1)}),
\tag{9}
\]

and therefore relative sign bias at most

\[
\frac{|N_+-N_-|}{N_{\rm sf}}
\le
X^{-(1/2-2\alpha-\beta)+o(1)}.
\tag{10}
\]

The recent Linnik-type theorem therefore crosses an important parity barrier but does **not** cross the amplitude barrier isolated by `MC-233`. The missing statement is no longer merely "show that both Möbius signs occur in the selected progression." Both signs occur abundantly in an absolute sense. What remains is a quantitative **near-balance theorem** whose precision tracks the exact deficit `1/2-2alpha-beta`.

No bound `(7)`, no estimate for `B_S`, no improvement of the first-shell energy, and no consequence for `M(X)` or the zeta zero set is proved here.

## 1. The 2026 Linnik-type theorem supplies both Möbius signs at scale `q^(2+epsilon)`

Kaisa Matomäki and Joni Teräväinen, *Linnik's problem for multiplicative functions*, arXiv:2605.27833 (submitted 27 May 2026), prove that sign changes of a nonvanishing multiplicative function occur in every reduced residue class by essentially `q^2`, unless its sign strongly pretends to a real character. Their Möbius specialization removes that alternative. In particular, their Corollary 1.3 together with Remark 1.4 gives `(3)` for Möbius in a reduced residue class.

The result is stronger at the parity-existence level than the generic logarithmic-savings progression estimates previously audited in this line. It is also structurally relevant: the proof uses a multiplicative dense model, product-set expansion in the unit group modulo `q`, and character-sum estimates, rather than assuming a zero-free region strong enough to manufacture square-root cancellation.

The theorem must nevertheless be used at its actual information level. It guarantees representatives of each sign; it does not state a square-root discrepancy bound for the counts of the two signs in a residue class.

## 2. CRT refinement turns one sign witness per class into `Z^(1/2-o(1))/q` witnesses

Fix a hard component `(q,a,Z)` from `(1)`. Let `epsilon>0` be fixed and let `C_epsilon` be an implied constant in `(3)`. Put

\[
R
= c_\varepsilon\frac{Z^{1/(2+\varepsilon)}}q
\tag{11}
\]

with `c_epsilon>0` sufficiently small. In the strict hard region, after choosing `epsilon` small enough,

\[
R=X^{\gamma+o(1)}
\quad\text{for some }\gamma>0,
\tag{12}
\]

because

\[
\frac{1-\beta}{2}-2\alpha
=
\left(\frac12-2\alpha-\beta\right)+\frac\beta2
>0.
\tag{13}
\]

Choose a prime `ell` with `R<ell<2R`. For large `X`, `ell` is much larger than the shell primes forming `q=Q_S`, so `(ell,q)=1`. For each `b in (Z/ell Z)^*`, CRT gives a distinct reduced residue class `A_b mod q ell` satisfying

\[
A_b\equiv a\pmod q,
\qquad
A_b\equiv b\pmod\ell.
\tag{14}
\]

By the choice of `R`,

\[
C_\varepsilon(q\ell)^{2+\varepsilon}\le Z.
\tag{15}
\]

Apply `(3)` to every `A_b mod q ell`. For each sign `Delta`, this produces an integer `n_{b,Delta}<=Z` with

\[
\mu(n_{b,\Delta})=\Delta,
\qquad
n_{b,\Delta}\equiv a\pmod q,
\qquad
n_{b,\Delta}\equiv b\pmod\ell.
\tag{16}
\]

Different `b` give distinct integers because their residues modulo `ell` differ. Therefore

\[
N_\Delta(Z;q,a)\ge\ell-1\gg_\varepsilon \frac{Z^{1/(2+\varepsilon)}}q.
\tag{17}
\]

For any fixed `eta>0`, choose `epsilon` small enough that `1/(2+epsilon)>1/2-eta`; this gives `(4)`. This is only a derived amplification of the published existence theorem, not a new sign-change theorem independent of it.

## 3. Square-free support has full progression density in the hard region

Because `(a,q)=1`, the classical identity

\[
\mu^2(n)=\sum_{r^2\mid n}\mu(r)
\tag{18}
\]

gives

\[
\begin{aligned}
N_{\rm sf}(Z;q,a)
&=
\sum_{\substack{r\le\sqrt Z\\(r,q)=1}}
\mu(r)
\left(
\frac{Z}{qr^2}+O(1)
\right)\\
&=
\frac Zq
\prod_{p\nmid q}\left(1-\frac1{p^2}\right)
+O(\sqrt Z).
\end{aligned}
\tag{19}
\]

For `q=Q_S`, all prime divisors of `q` lie in `(y,2y]` and

\[
\prod_{p\mid q}(1-p^{-2})^{-1}=1+o(1),
\tag{20}
\]

so the main constant in `(19)` is `6/pi^2+o(1)`. Moreover the hard condition implies

\[
q=X^{2\alpha+o(1)}
=o\!\left(Z^{1/2}\right),
\tag{21}
\]

because `(13)` is positive. Thus `sqrt(Z)=o(Z/q)`, proving `(5)`.

This comparison is useful because it prevents a misleading interpretation of `(4)`. The recent theorem is not revealing that the selected progression contains only a few exceptional square-free integers of either sign. The progression contains `asymp Z/q` square-free values, while the theorem statement plus CRT forces only `Z^{1/2-o(1)}/q` values of each sign.

## 4. The amplitude gap is a sign-balance gap, not a sign-existence gap

The exact identity `(8)` converts the progression problem into a discrepancy between two nonnegative counts. From `(5)`, the natural number of nonzero terms is

\[
N_{\rm sf}=X^{1-\beta-2\alpha+o(1)}.
\tag{22}
\]

In the hard region this exponent is strictly larger than `1/2`. Therefore `(7)` requires cancellation of a polynomial fraction of the natural unsigned mass. Equivalently, both signs must occupy asymptotically half of the square-free support up to the relative error in `(10)`.

By itself, `(4)` gives no such control. Pairing the guaranteed opposite signs can subtract at most an additive

\[
X^{(1-\beta)/2-2\alpha+o(1)}
\tag{23}
\]

from the trivial progression occupancy, while that occupancy has exponent

\[
1-\beta-2\alpha.
\tag{24}
\]

The exponent gap between `(23)` and `(24)` is `(1-beta)/2>0`. Hence the black-box sign theorem leaves the leading power of the trivial amplitude unchanged.

This identifies a precise boundary for importing parity-breaking results into the current first-shell route. A theorem saying that every selected residue contains both signs, even at the optimal `q^(2+o(1))` Linnik scale, is not enough. The required object is a signed count, or an equivalent weighted dense-model statement, that controls **imbalance**, not merely nonemptiness.

## 5. Prior-art and novelty boundary

The sign-change theorem is entirely prior art: Matomäki--Teräväinen, arXiv:2605.27833. Their paper improves the earlier Ford--Radziwiłł result for Liouville sign changes in prime-modulus progressions and reaches the natural `q^(2+o(1))` barrier. No novelty is claimed for that theorem, for CRT, or for square-free counting in arithmetic progressions.

The Mathia-specific derivation is the scale audit against `MC-233`: the new theorem applies throughout the exact hard `(alpha,beta)` region, and the CRT refinement `(11)`--`(17)` quantifies how much sign abundance its stated existence result can force there. The resulting abundance is still polynomially too weak to control the progression amplitude because the live target is near-balance on `asymp Z/q` square-free terms.

A targeted search found the Matomäki--Teräväinen preprint and its Ford--Radziwiłł predecessor, but no theorem in that sign-change line whose stated conclusion gives the near-balanced sign counts required by `(10)`. This is not a literature-absence claim about all possible methods: the internal dense-model estimates in the new proof may contain more quantitative information than the headline corollary, and adapting that proof rather than using `(3)` as a black box remains a legitimate direction.

## 6. Boundaries and falsification tests

- The amplification `(17)` uses the published sign-existence theorem as a black box. It does not claim that the Matomäki--Teräväinen proof cannot be strengthened to count many representatives or control signed discrepancy.
- The auxiliary-prime refinement works in the strict interior of `(2)`, where `R` in `(11)` grows polynomially. Boundary sequences with deficits tending to zero require a separate uniformity audit and are not covered by the fixed-parameter statement `(4)`.
- The square-free asymptotic `(19)` is valid here because the selected residue is reduced and `q=o(sqrt(Z))`. It should not be transported unchanged to non-reduced residues or to the support boundary without rechecking the error term.
- Equation `(9)` is a necessary consequence of the sufficient componentwise target `(7)`. Since `MC-233` explicitly notes that cancellation between smooth-dilation components could prove `B_S` without proving every component bound, failure to obtain `(9)` componentwise does not rule out the true aggregate route.
- The result does not weaken the importance of parity-sensitive methods. On the contrary, it shows that a modern parity-breaking architecture reaches every hard selected class; what remains to be extracted is quantitative balance at a much finer scale.

## Consequence for the live frontier

The first-shell problem should no longer treat **existence of both Möbius parities in the source-selected progression** as a plausible bottleneck. Current unconditional prior art reaches that property throughout the entire hard CRT component region and, after CRT refinement, forces polynomially many representatives of each sign.

The unresolved power is in their **relative mass**. At scale `(alpha,beta)`, the componentwise route needs signed bias at most `X^{-(1/2-2alpha-beta)+o(1)}` relative to square-free support, while the published Linnik-type sign theorem controls only nonemptiness. A promising use of this prior art would therefore have to enter the multiplicative dense-model proof before its final existence conclusion and extract a quantitative signed-count or weighted-discrepancy estimate. Reusing only the `q^(2+o(1))` representative bound cannot change the fixed-power amplitude ledger.