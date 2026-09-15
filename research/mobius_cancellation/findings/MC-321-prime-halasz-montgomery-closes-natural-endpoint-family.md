# MC-321 — Prime Halász–Montgomery family bound rules out the natural-scale reciprocal endpoint family

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint-partition branch of `MC-296`–`MC-320`. Let

\[
\mathcal R_y
=\{r:y<r\le2y,\ r\text{ prime},\ r\equiv1\pmod4\},
\qquad N_y=|\mathcal R_y|,
\]

and let

\[
\chi_1,\ldots,\chi_R
\]

be the `R` distinct source characters attached to the independent one-defect endpoint directions. Thus each `\chi_i` is `+1` on exactly one defect cell of size `N_y/R` and `-1` on the other `R-1` cells, so

\[
\boxed{
\sum_{r\in\mathcal R_y}\chi_i(r)
=N_y\left(\frac2R-1\right)
\qquad(1\le i\le R).
}
\tag{1}
\]

Assume the exact natural-source package already isolated in `MC-314` and used in `MC-319`:

\[
R\to\infty,
\qquad
2^R=(\kappa_0+o(1))\log y,
\qquad
n=2R,
\qquad
Z\le y^{1/R},
\tag{2}
\]

with `0<\kappa_0<\infty`. If `P` is the common odd squarefree source radical and

\[
q:=4P,
\]

then

\[
P\le Z^{2R}\le y^2,
\qquad
q\le4y^2.
\tag{3}
\]

All `\chi_i` may be viewed as distinct characters modulo this one `q`, without changing their values on `\mathcal R_y`.

The prime Halász–Montgomery estimate recorded as Lemma 12.4 of Klurman–Mangerel–Teräväinen (`MC-S45`), itself attributed there to Puchta, is already strong enough to make `(1)`–`(3)` impossible for all sufficiently large `y`. No zero-free region, exceptional-zero analysis, primitive-conductor lower bound, smoothness hypothesis, or Rodosskii conversion is needed.

More generally, fix `\delta>0`. Suppose `R=o(\log y)`, `R\to\infty`, `q\le y^{8/3-\delta}`, and `\Xi=\{\chi_1,\ldots,\chi_R\}` is a set of distinct characters modulo `q`. If a prime set `\mathcal A_y\subset(y,2y]` has

\[
|\mathcal A_y|\asymp \frac{y}{\log y}
\tag{4}
\]

and every character has a fixed nonvanishing bias

\[
\left|\sum_{p\in\mathcal A_y}\chi_i(p)\right|
\ge c_0|\mathcal A_y|
\qquad(1\le i\le R)
\tag{5}
\]

for some fixed `c_0>0`, then such a family cannot exist for all sufficiently large `y`.

The reciprocal endpoint is a direct specialization: `(1)` gives `(5)` with, say, `c_0=1/2` once `R\ge4`; the fixed progression prime number theorem gives `(4)` with `\mathcal A_y=\mathcal R_y`; and `(3)` lies well inside the modulus range `q<y^{8/3-\delta}` for any fixed `\delta<2/3`.

Thus the residual analytic frontier identified by `MC-319` and `MC-320` closes for this exact natural-scale reciprocal endpoint family. The decisive datum is not primitive conductor provenance after all. It is the **simultaneous bias of a growing set of distinct characters on the same dyadic prime shell**, which Lemma 12.4 controls directly.

No estimate for `M(x)` follows.

## 1. The prime Halász–Montgomery estimate applies directly to the shell

Lemma 12.4 of Klurman–Mangerel–Teräväinen states the following. For an integer `q\ge1`, a set `\Xi` of characters modulo `q`, `k\in\{2,3\}`, `\eta>0`, an auxiliary parameter `2\le B<\sqrt X`, and arbitrary complex prime coefficients `a_p`,

\[
\sum_{\chi\in\Xi}
\left|\sum_{p\le X}a_p\chi(p)\right|^2
\ll_{k,\eta}
\left(
\frac{X}{\log B}
+X^{1-1/k}q^{(k+1)/(4k^2)+\eta}|\Xi|B^{2/k}
\right)
\sum_{p\le X}|a_p|^2.
\tag{6}
\]

The paper attributes this estimate to Puchta, *Primes in short arithmetic progressions*, Acta Arith. 106 (2003), Theorem 3. Klurman–Mangerel–Teräväinen themselves use `(6)` as a sharp mean-square inequality over a small character family.

Take `k=2`, so the modulus exponent is `3/16`, put `X=2y`, and choose

\[
a_p=\mathbf1_{\{p\in\mathcal A_y\}}.
\tag{7}
\]

Then `\sum|a_p|^2=|\mathcal A_y|`. Under `(5)`, the left side of `(6)` is at least

\[
c_0^2 R|\mathcal A_y|^2.
\tag{8}
\]

This choice is the critical difference from the Rodosskii route in `MC-319`: the theorem already sums **over primes**, and its coefficients may localize to the exact dyadic shell and the exact `1 mod 4` projector. There is no need to infer prime cancellation from an ordinary integer character sum or from a broad power interval.

## 2. A slowly growing auxiliary cutoff absorbs the diagonal term

Let `C_\eta` denote a fixed implicit constant in `(6)` after choosing `k=2` and a sufficiently small fixed `\eta>0`. Choose a fixed constant `A>0` later and set

\[
B:=y^{A/R}.
\tag{9}
\]

Because `R\to\infty` and `R=o(\log y)`, eventually

\[
2\le B<\sqrt{2y}.
\tag{10}
\]

Also

\[
\log B=\frac{A\log y}{R}.
\tag{11}
\]

Using `(4)`, the first term on the right side of `(6)` is

\[
\ll
\frac{y}{\log B}\frac{y}{\log y}
=
\frac{R}{A}\frac{y^2}{(\log y)^2}.
\tag{12}
\]

The lower bound `(8)` has size

\[
\gg
R\frac{y^2}{(\log y)^2}.
\tag{13}
\]

Therefore choosing `A` sufficiently large, depending only on `c_0`, the constants in `(4)`, and the fixed constant in `(6)`, makes `(12)` strictly smaller than (for example) half of `(13)`.

This is precisely the gain missing from the generic multiplicative-large-sieve capacity in `MC-301`: the diagonal contribution here is `X/\log B`, and the free parameter `B=y^{A/R}` converts it into an arbitrarily small fixed fraction of the simultaneous endpoint energy.

## 3. The modulus penalty is subcritical below `y^(8/3)`

For `k=2`, the second term in `(6)` contributes at most

\[
\ll
 y^{1/2}q^{3/16+\eta}R B\frac{y}{\log y}.
\tag{14}
\]

Divide `(14)` by the lower-bound scale `(13)`. The ratio is

\[
\ll
 y^{-1/2}q^{3/16+\eta}B\log y.
\tag{15}
\]

If

\[
q\le y^{8/3-\delta},
\]

choose `\eta>0` sufficiently small in terms of `\delta`. Then

\[
-\frac12+\left(\frac83-\delta\right)
\left(\frac3{16}+\eta\right)<0.
\tag{16}
\]

Since `B=y^{A/R}=y^{o(1)}`, the quantity in `(15)` tends to zero. Thus the second term is `o((13))`, while the first term was already made a strict fraction of `(13)`. This contradicts `(6)` and proves the general family obstruction `(4)`–`(5)`.

For the endpoint it is enough to use the much stronger concrete bound `q\le4y^2`. For example, take `\eta=1/64`. Then

\[
q^{3/16+\eta}\ll y^{3/8+1/32},
\]

so `(15)` is

\[
\ll y^{-3/32+A/R}\log y=o(1).
\tag{17}
\]

Hence the contradiction holds with substantial exponent margin.

## 4. Exact endpoint specialization

In the reciprocal endpoint partition, each `\chi_i` has one positive cell and `R-1` negative cells of equal size, giving `(1)` exactly. Thus for `R\ge4`,

\[
\left|
\sum_{r\in\mathcal R_y}\chi_i(r)
\right|
\ge\frac12N_y.
\tag{18}
\]

The fixed-modulus prime number theorem in the progression `1 mod 4` gives

\[
N_y\sim\frac{y}{2\log y}.
\tag{19}
\]

The natural-source realization contains only `2R` lower-prime coordinates with each source prime at most `Z\le y^{1/R}`. Therefore its common radical obeys

\[
P\le Z^{2R}\le y^2,
\tag{20}
\]

and inducing all selected characters to `q=4P` gives `(3)`. The characters remain distinct because their shell functionals are independent, and no shell prime divides `q` because every source prime lies below the shell.

Apply the general obstruction with `\mathcal A_y=\mathcal R_y`. Equations `(18)`–`(20)` satisfy all hypotheses, while `(2)` gives `R\to\infty` and `R=o(\log y)`. Contradiction.

The exact natural-scale reciprocal endpoint family considered in `MC-314`, `MC-319`, and `MC-320` therefore cannot be arithmetically realized for all sufficiently large `y`.

## 5. Relation to the previous capacity and resolution barriers

`MC-301` inserted varying primitive source characters into the classical multiplicative large sieve. Its `y+C^2` envelope reached square-root conductor but left a factor-`R` energy gap at the critical endpoint rank.

`MC-304` then used the fixed common radical and a sparse Halász–Montgomery estimate over **integer** sums. That sharpened the structure to a totient-versus-radical dichotomy but still allowed the natural endpoint to escape through a large common radical.

`MC-319` exploited the radical's smoothness to obtain a strong collective zero-free region, but its Rodosskii consequence averaged on a logarithmic interval scale too broad to see the dyadic endpoint signal. `MC-320` correctly showed that arbitrarily good **ordinary interval** cancellation is insufficient by itself: an imprimitive conductor-`4` character can have tiny integer-interval sums and maximal bias on the selected prime shell.

Lemma 12.4 attacks a different observable. It bounds the total squared correlation of a **set of distinct characters directly against arbitrary coefficients supported on primes**. The conductor-inflated control of `MC-320` has only one biased primitive pattern and therefore does not fake the growing `R`-character simultaneous-bias hypothesis `(5)`. The endpoint does, and the small-family prime mean-square inequality detects exactly that coherence.

Thus primitive conductor/source cost is not needed to close this branch. Common-modulus embedding plus family multiplicity and exact prime-shell localization suffice.

## Prior art and novelty boundary

The analytic theorem `(6)` is not new. It is Lemma 12.4 of Oleksiy Klurman, Alexander P. Mangerel and Joni Teräväinen, *Multiplicative functions in short arithmetic progressions*, Proc. London Math. Soc. 127 (2023), 366–446, DOI `10.1112/plms.12546`, arXiv `1909.12280`, retained as `MC-S45`. Their lemma explicitly attributes the estimate to J.-C. Puchta, *Primes in short arithmetic progressions*, Acta Arith. 106 (2003), 143–149, Theorem 3.

A targeted audit of the KMT theorem and its application confirms that the estimate allows an arbitrary set of characters modulo one `q` and arbitrary complex coefficients indexed by primes. No primitivity, smoothness, zero-free region, or relation between `q` and `X` beyond what appears quantitatively in `(6)` is imposed in the lemma statement.

No standalone novelty claim is made for the general analytic inequality or for the exponent `3/16`. The durable Mathia contribution is the endpoint-specific parameter bridge: choosing coefficients supported exactly on `\mathcal R_y`, exploiting the simultaneous one-defect bias, and tuning `B=y^{A/R}` converts the classical small-family prime estimate into a contradiction in the natural common-modulus range. This closes a branch that the coarser large-sieve, zero-free, and integer-interval estimates in `MC-301`, `MC-304`, `MC-319`, and `MC-320` left open.

## Boundaries and falsification tests

- **The reciprocal endpoint partition is load-bearing.** The proof uses `R` distinct characters each carrying a fixed-size bias on the same shell. A general defect pattern with only `o(R)` strongly biased directions is not ruled out by this statement without a corresponding lower bound on the family energy.
- **The common-modulus bound is load-bearing.** The contradiction uses `q\le4y^2`. A realization whose common modulus exceeds the `y^(8/3)` threshold by a fixed power is outside the general theorem derived here.
- **The natural source cap is load-bearing only through `q`.** Smoothness `P^+(q)\le y^{1/R}` is not used after deriving `P\le y^2`; neither is the lower bound `P\ge y/(\log y)^{O(1)}` from `MC-305`.
- **Primitivity is not used.** Lemma 12.4 is stated for characters modulo `q`; induced characters are allowed. This is why the argument genuinely bypasses the primitive-conductor question posed after `MC-320`.
- **Distinctness is essential.** The theorem sums over a set `\Xi`, so repeatedly counting one character cannot manufacture the `R`-fold lower bound. The selected endpoint source characters are distinct by independence of the corresponding shell functionals.
- **The prime support is essential.** The result does not contradict `MC-320`; it uses a theorem whose coefficients live on primes, precisely the information ordinary interval discrepancy discards.
- **No exceptional-zero issue remains in this argument.** The estimate is unconditional and contains no Page/Siegel exception.
- **No RH or Mertens estimate follows.** The contradiction kills the exact natural-scale reciprocal endpoint realization only; it does not prove the global Möbius cancellation target.

## Consequence for the research line

The primitive-conductor dyadic clue generated after `MC-320` is resolved more strongly than proposed: the sought dyadic discriminator already exists at the family level, and it does not need primitive conductor information. The exact natural-scale reciprocal endpoint cannot support `R\asymp\log\log y` simultaneously biased source characters inside a common modulus `q\le4y^2`.

Future work on this branch should therefore not spend effort sharpening individual-character zero-free/Rodosskii or ordinary interval estimates for the same endpoint model. Any surviving endpoint variant must first escape one of the actual hypotheses above: lose the growing family of simultaneously biased distinct characters, enlarge the common modulus beyond the prime Halász–Montgomery range, or abandon the exact reciprocal one-defect partition structure.