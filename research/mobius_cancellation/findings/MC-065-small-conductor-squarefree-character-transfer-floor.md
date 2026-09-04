# MC-065 — Internal conductor zeros lower the direct squarefree-character certification floor only to 11/19

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-064` studied the square-free-supported quadratic comparator

\[
F_\chi(X):=\sum_{n\le X}\mu(n)^2\chi(n)
\]

under the interpolation convention that the prime conductor `q` satisfies `q>X`. That convention is not needed for the coefficient-transfer inequality or for Munsch's classical squarefree-character estimate. Allowing the conductor to lie **inside** the observed prefix does reduce the Burgess conductor cost, but the zero of the Dirichlet character at its own conductor creates a competing coefficient-fidelity cost.

Let `q` be any odd prime, let

\[
\chi(n)=\left(\frac{n}{q}\right),
\qquad
A_X(\chi):=\sum_{p\le X}\frac{|1+\chi(p)|}{p-1},
\]

and put `F_chi(X)` as above. Then for every `X>=2`,

\[
\boxed{|M(X)-F_\chi(X)|\le X A_X(\chi).}
\tag{1}
\]

This remains valid when `q<=X`, including the terms divisible by `q` where `chi` vanishes. Coupling `(1)` to Munsch's Lemma 2.3 (`MC-S38`) gives, for prime `q`,

\[
\boxed{
|M(X)|
\ll
X A_X(\chi)
+
X^{1/2}q^{3/16}(\log X)(\log q)^{1/2}.
}
\tag{2}
\]

When `q<=X`, the conductor prime itself contributes

\[
\frac{|1+\chi(q)|}{q-1}=\frac1{q-1}
\tag{3}
\]

to `A_X`. Therefore an absolute-defect certificate targeting a power exponent `theta<1` must balance

\[
q\gtrsim X^{1-\theta-o(1)}
\tag{4}
\]

against the Munsch/Burgess term. At power-exponent level, requiring the displayed certificate `(2)` to be `O(X^{theta+o(1)})` forces

\[
\frac12+\frac3{16}(1-\theta)\le\theta,
\]

hence

\[
\boxed{\theta\ge\frac{11}{19}.}
\tag{5}
\]

The balance occurs formally at

\[
q=X^{8/19+o(1)},
\qquad
|M(X)|\text{ certificate scale }X^{11/19+o(1)}.
\tag{6}
\]

Thus removing the `q>X` restriction closes one obvious escape from the `11/16` floor of `MC-064`, but it does **not** make the direct quadratic-comparator architecture RH-scale. Across all prime-conductor sizes, the best power exponent certifiable by this particular package — absolute coefficient transfer plus the classical Munsch/Burgess squarefree-character estimate — bottoms out at `11/19`, still strictly above `1/2`.

This is a **method-specific certification floor**. It is not a lower bound for `M(X)`, not a lower bound for the true value of `F_chi(X)`, and not a claim that signed comparison or a stronger squarefree-character theorem cannot do better.

## 1. The transfer inequality does not require `q>X`

Let `lambda` be the Liouville function and define

\[
g(n):=\lambda(n)\chi(n).
\]

Both factors are completely multiplicative, so `g` is completely multiplicative, with `|g(n)|<=1`; values may vanish when `q|n`. For complex numbers `z,w` of modulus at most one,

\[
|1-zw|
\le |1-z|+|z||1-w|
\le |1-z|+|1-w|.
\tag{7}
\]

Iterating `(7)` over the prime factors of `n` gives

\[
|1-g(n)|
\le
\sum_p v_p(n)|1-g(p)|.
\tag{8}
\]

Since `lambda(p)=-1`,

\[
|1-g(p)|=|1+\chi(p)|
\tag{9}
\]

for every prime, including `p=q`, where `chi(q)=0` and both sides equal one. Summing `(8)` over `n<=X`,

\[
\begin{aligned}
\sum_{n\le X}|1-g(n)|
&\le
\sum_{p\le X}|1+\chi(p)|
\sum_{j\ge1}\left\lfloor\frac{X}{p^j}\right\rfloor\\
&\le
X\sum_{p\le X}\frac{|1+\chi(p)|}{p-1}\\
&=XA_X(\chi).
\end{aligned}
\tag{10}
\]

If `n` is not square-free, both `mu(n)` and `mu(n)^2 chi(n)` vanish. If `n` is square-free, `mu(n)=lambda(n)` and

\[
|\mu(n)-\mu(n)^2\chi(n)|
=|\lambda(n)-\chi(n)|
=|1-\lambda(n)\chi(n)|,
\tag{11}
\]

where the last equality also holds when `chi(n)=0`. Consequently

\[
\sum_{n\le X}|\mu(n)-\mu(n)^2\chi(n)|
\le XA_X(\chi),
\tag{12}
\]

and `(1)` follows by the triangle inequality.

The former hypothesis `q>X` was therefore an interpolation convenience: it ensured that the character never vanished on the prefix. It was not a logical requirement of the absolute transfer.

## 2. Putting the conductor inside the prefix creates its own fidelity charge

If `q<=X`, the single prime `p=q` already gives `(3)`, hence

\[
A_X(\chi)\ge\frac1{q-1}.
\tag{13}
\]

Suppose the first term in `(2)` is to contribute at most `X^{theta+o(1)}`. Then

\[
A_X(\chi)\le X^{\theta-1+o(1)},
\]

so `(13)` forces `(4)`.

This charge reflects a real coefficient mismatch, not only looseness in the weighted prime estimate. Every square-free integer divisible by `q` has comparator coefficient zero while its Möbius coefficient is `+1` or `-1`. In particular, for primes `p<=X/q` with `p!=q`, the integers `qp` each contribute one to the coefficientwise `L^1` defect. Hence, whenever `X/q` tends to infinity,

\[
\sum_{n\le X}|\mu(n)-\mu(n)^2\chi(n)|
\ge
\pi(X/q)-1
=
X^{1-\alpha-o(1)}
\tag{14}
\]

when `q=X^{\alpha+o(1)}` with fixed `alpha<1`. Thus any **coefficientwise absolute** transfer has the same exponent-level small-conductor cost even if `(12)` is replaced by a sharper estimate. Beating it requires using signed cancellation in the difference, rather than merely improving the absolute bookkeeping.

## 3. Balancing fidelity against the classical squarefree-character theorem gives 11/19

Munsch's Lemma 2.3 applies to a nonprincipal character modulo `q` without imposing `q>X`. For prime `q`, the paper's Remark 2.4 gives the power-level estimate

\[
|F_\chi(X)|
\ll
X^{1/2}q^{3/16}(\log X)(\log q)^{1/2}.
\tag{15}
\]

Write `q=X^{alpha+o(1)}` with `0<=alpha<=1`. An absolute-transfer certificate for exponent `theta` must satisfy, at power level,

\[
\alpha\ge1-\theta
\tag{16}
\]

from the conductor-fidelity charge, while `(15)` is certified at exponent

\[
\frac12+\frac{3\alpha}{16}.
\tag{17}
\]

For fixed `theta`, the comparator certificate is best when `alpha` is as small as the transfer permits, namely `alpha=1-theta`. Requiring `(17)` not to exceed `theta` gives exactly

\[
\frac12+\frac3{16}(1-\theta)\le\theta
\iff
\theta\ge\frac{11}{19}.
\tag{18}
\]

At equality, `alpha=8/19`, giving `(6)`. For `q>X`, `MC-064` already yields the weaker floor `11/16`, so the global optimum of this particular prime-quadratic certificate architecture lies in the internal-conductor regime and is `(5)`.

Nothing here asserts the existence, at every scale, of a quadratic character with the required weighted agreement near the formal balance. Any arithmetic obstruction to finding such characters can only make this certificate architecture worse.

## 4. Larger fixed Burgess moment parameters do not improve the internal-conductor balance

The `r=2` exponent in Munsch's elementary square-divisor argument is also the best fixed-`r` Burgess insertion throughout `0<=alpha<=1`.

For `r=2`, ignoring logarithms,

\[
e_2(\alpha)=\frac12+\frac{3\alpha}{16}.
\tag{19}
\]

For every fixed `r>=3`, absolute insertion of the standard Burgess estimate into the square-divisor decomposition gives

\[
e_r(\alpha)
=
1-\frac1r
+\alpha\frac{r+1}{4r^2}.
\tag{20}
\]

The difference `e_r(alpha)-e_2(alpha)` is affine decreasing in `alpha`, so its minimum on `[0,1]` occurs at `alpha=1`. There

\[
e_r(1)-e_2(1)
=
\frac{(r-2)(5r-2)}{16r^2}>0.
\tag{21}
\]

Thus `r=2` is strictly better than every fixed `r>=3` on the whole internal-conductor range. The Pólya–Vinogradov branch is also weaker at power level. The `11/19` balance is therefore not removed by a routine change of Burgess moment parameter inside the same absolute square-divisor scheme.

## 5. Prior art and novelty boundary

The analytic input is classical prior art. `MC-S38` records Marc Munsch, *Character sums over squarefree and squarefull numbers*, Archiv der Mathematik 102 (2014), 555–563, DOI `10.1007/s00013-014-0658-9`. Its Lemma 2.3 studies exactly `sum mu(n)^2 chi(n)` and proves the two squarefree-character estimates used in `MC-064`; Remark 2.4 supplies the prime-modulus logarithmic replacement in the Burgess branch. The theorem is not restricted to conductors exceeding the summation cutoff.

A targeted search around squarefree character sums, Möbius-character comparisons, and the exponent `11/19` found the Munsch theorem as the directly relevant established mechanism but no reason to treat the present optimization as an independent literature theorem. Accordingly this finding makes **no standalone novelty claim**. Its durable role is to audit an omitted parameter regime of the already-persisted `MC-064` certificate and to identify the exact internal-conductor tradeoff imposed by the character's own zero.

The prime number theorem used only to interpret `(14)` at exponent level is classical and not part of the claimed new mechanism.

## 6. Boundaries and falsification tests

The conclusion is deliberately restricted.

- The `11/19` number is a floor for **certification by this exact package**: prime quadratic comparator `mu^2 chi`, coefficientwise absolute transfer, and the classical Munsch/Burgess estimate. It is not a lower bound for the true sums.
- A signed estimate for `M(X)-F_chi(X)` can in principle exploit cancellation among the conductor-induced mismatches and is outside this obstruction.
- A stronger theorem for squarefree character sums with better uniform conductor dependence would change the balance and must be analyzed on its own terms.
- Composite conductors, higher-order characters, non-character comparators, or source-forced families with different zero/support structure are not covered automatically.
- The prime-count lower bound `(14)` is used only when `X/q` grows. If `q` is comparable with `X`, the conductor already has exponent one and is farther from the favorable balance.
- Logarithmic factors are suppressed only in the stated power-exponent optimization. Endpoint logarithms prevent interpreting `(5)` as a sharp literal `O(X^(11/19))` theorem.

The transfer claim is falsified if zeros of `chi` break the complete-multiplicative telescoping argument or the square-free coefficient identity; equations `(7)`–`(12)` show that they do not. The exponent floor is falsified if the conductor term `(3)` can be absent when `q<=X`, if Munsch's theorem requires `q>X`, or if a fixed Burgess parameter `r>=3` improves `(19)` on `0<=alpha<=1`; the character definition, the source theorem, and `(21)` exclude those possibilities.

## Consequence for the active frontier

The moving quadratic-comparator route now has no cheap escape by sliding the conductor below the observation scale. Large conductors pay the `MC-064` Burgess cost; small conductors introduce zeros inside the Möbius prefix, and absolute coefficient fidelity pushes the conductor back upward until the two costs balance at `11/19`.

A surviving character-comparator mechanism must therefore add information absent from this architecture: signed cancellation in the Möbius/comparator defect, a squarefree-character theorem with materially better conductor dependence, a coupled/bilinear use of the square-divisor layers, or a different comparator whose complexity parameter does not simultaneously control cancellation quality and create prefix defects. Merely optimizing the same one-character absolute transfer over conductor size cannot reach the RH boundary.