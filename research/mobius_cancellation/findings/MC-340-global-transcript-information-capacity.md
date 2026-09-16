# MC-340 — Bounded-energy dephasing requires linear global source information

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-338` and `MC-339` measure, source by source, how much the admitted observation can predict its own reciprocal endpoint phase. That local information budget has a global form: a coefficient architecture that dephases all source phases at bounded energy must expose a transcript carrying a **linear amount of information about the joint source vector**.

Keep the reciprocal endpoint notation

\[
G=\mathbf F_2^R,\qquad
\Xi=G\setminus\{0\},\qquad
m=|\Xi|=2^R-1,
\]

and sample `A` uniformly from `Xi`. Write

\[
X_i:=x_i(A)\in\{-1,+1\},
\qquad
X:=(X_1,\ldots,X_R).
\]

For each source let `Y_i` be its admitted observation as in `MC-339`, and collect the complete architecture transcript

\[
Y:=(Y_1,\ldots,Y_R).
\]

Let

\[
\rho_i^2
:=\mathbf E\left|\mathbf E[X_i\mid Y_i]\right|^2,
\qquad
\rho^2:=\frac1R\sum_{i=1}^R\rho_i^2,
\]

and let `E(W)` and `delta(W)` denote the normalized coefficient energy and all-mode RMS dephasing error of `MC-338`.

Define Watanabe total correlation, in nats,

\[
\operatorname{TC}(X)
:=\sum_{i=1}^R H(X_i)-H(X).
\]

Then every admitted coefficient family obeys

\[
\boxed{
\rho^2
\le
\frac1{m^2}
+\frac{2}{R}
\bigl(I(X;Y)+\operatorname{TC}(X)\bigr).
}
\tag{1}
\]

Combining `(1)` with `MC-338` gives the global transcript-capacity obstruction

\[
\boxed{
\delta(W)\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{
\frac1{m^2}
+\frac{2}{R}
\bigl(I(X;Y)+\operatorname{TC}(X)\bigr)
}
\right)_+.
}
\tag{2}
\]

The source law makes the dependence penalty explicit. Put

\[
p_R:=\mathbf P(X_i=+1)=\frac{m-1}{2m},
\qquad
h(p):=-p\log p-(1-p)\log(1-p).
\]

For even `R`, the source-character map is invertible on the full cube and puncturing deletes exactly the all-`+1` pattern, so

\[
H(X)=\log m,
\qquad
\operatorname{TC}(X)=R h(p_R)-\log m.
\tag{3}
\]

For odd `R`, the source characters satisfy one parity relation and the all-`+1` image has one surviving preimage while every other image has two, so

\[
H(X)
=
\log m-\frac{m-1}{m}\log 2,
\]

and hence

\[
\operatorname{TC}(X)
=
R h(p_R)-\log m+\frac{m-1}{m}\log 2.
\tag{4}
\]

Therefore

\[
\operatorname{TC}(X)\to0
\quad(R\to\infty,\ R\ \mathrm{even}),
\qquad
\operatorname{TC}(X)\to\log2
\quad(R\to\infty,\ R\ \mathrm{odd}).
\tag{5}
\]

The source dependence costs only `O(1)` nats; it cannot supply the linear information required by bounded-energy dephasing.

A particularly concrete consequence follows when the joint transcript has at most `K_R` possible values. Since

\[
I(X;Y)\le H(Y)\le\log K_R,
\]

equation `(2)` yields

\[
\boxed{
\delta(W)\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{
\frac1{m^2}
+\frac{2}{R}
\bigl(\log K_R+\operatorname{TC}(X)\bigr)
}
\right)_+.
}
\tag{6}
\]

Thus, if `E(W)=O(1)` and `log K_R=o(R)`, then

\[
\delta(W)\to1.
\tag{7}
\]

Equivalently, if `delta(W)<=1-eta` for fixed `eta>0` and `E(W)<=C`, then

\[
\boxed{
I(X;Y)
\ge
\frac{R}{2}
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-\operatorname{TC}(X),
}
\tag{8}
\]

so every discrete transcript satisfies the same lower bound with `log K_R` in place of `I(X;Y)`. Any constant-factor dephasing at bounded energy therefore requires exponentially many transcript states.

There is a stronger near-exact statement at matched-filter energy. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\]

then

\[
\boxed{
I(X;Y)
\ge
H(X)
-
R\,h\!\left(\varepsilon-\frac{\varepsilon^2}{2}\right).
}
\tag{9}
\]

Hence `epsilon -> 0` forces the joint transcript to carry asymptotically the full source entropy. At `epsilon=0`, equation `(9)` gives

\[
I(X;Y)=H(X),
\tag{10}
\]

so the complete source vector is determined by the joint transcript. This recovers the exact unit-energy rigidity of `MC-339` in a global, representation-independent form and extends it quantitatively to near-exact dephasing.

No estimate for `M(x)` follows. The result is a finite reciprocal-endpoint admission theorem: a future source-natural analytic architecture must control not only each own-phase leakage and coefficient energy, but also the **joint information capacity of the observations it exposes**.

## 1. Total correlation converts local leakage into one transcript budget

`MC-339` proves, with natural logarithms,

\[
\rho_i^2-\frac1{m^2}
\le
2I(X_i;Y_i).
\tag{11}
\]

Because `Y_i` is a component of `Y`, data processing gives

\[
I(X_i;Y_i)\le I(X_i;Y).
\tag{12}
\]

Introduce the conditional total correlation

\[
\operatorname{TC}(X\mid Y)
:=
\sum_i H(X_i\mid Y)-H(X\mid Y)
\ge0.
\tag{13}
\]

Expanding definitions gives the exact identity

\[
\begin{aligned}
\sum_i I(X_i;Y)
&=
\sum_i H(X_i)-\sum_i H(X_i\mid Y)\\
&=
I(X;Y)
+\operatorname{TC}(X)
-\operatorname{TC}(X\mid Y).
\end{aligned}
\tag{14}
\]

Therefore

\[
\sum_i I(X_i;Y_i)
\le
I(X;Y)+\operatorname{TC}(X).
\tag{15}
\]

Summing `(11)`, dividing by `R`, and using `(15)` proves `(1)`. Substitution into the independently derived `MC-338` inequality

\[
\delta(W)\ge
\bigl(1-\rho\sqrt{\mathcal E(W)}\bigr)_+
\tag{16}
\]

proves `(2)`.

The total-correlation term is load-bearing. The source phases are not exactly independent under the punctured-mode law, and for odd rank they also carry one exact parity relation. Equation `(14)` charges those dependencies explicitly rather than pretending that the `X_i` are independent.

## 2. The punctured source law has only constant total correlation

Every nontrivial source character has full-cube mean zero. Removing the principal mode, where all source characters equal `+1`, gives

\[
\mathbf P(X_i=+1)=\frac{m-1}{2m},
\qquad
\mathbf P(X_i=-1)=\frac{m+1}{2m}.
\tag{17}
\]

Hence every marginal entropy is `h(p_R)`.

For even `R`, the vectors `s_i=1+e_i` form a basis of `F_2^R`. Thus `a -> X(a)` is a bijection from the full mode cube onto `{-1,+1}^R`; restricting to `Xi` deletes one image point. The resulting `X` is uniform on `m` states, which proves `(3)`.

For odd `R`, the vectors `s_i` have the single relation

\[
s_1+\cdots+s_R=0,
\]

equivalently

\[
X_1\cdots X_R=1.
\tag{18}
\]

The full-cube character map has a two-point kernel. After deleting `a=0`, the all-`+1` image has probability `1/m`, while each of the other `2^(R-1)-1` parity-compatible images has probability `2/m`. Therefore

\[
\begin{aligned}
H(X)
&=
-\frac1m\log\frac1m
-\left(2^{R-1}-1\right)\frac2m\log\frac2m\\
&=
\log m-\frac{m-1}{m}\log2,
\end{aligned}
\]

which proves `(4)`.

Since `p_R=1/2-1/(2m)`, the binary entropy expansion

\[
h(p_R)=\log2-\frac1{2m^2}+O(m^{-4})
\]

together with `m=2^R-1` gives `(5)`.

This calculation is useful beyond bookkeeping. The odd-rank parity decoder of `MC-337` contributes only one asymptotic bit of intrinsic source dependence. A proposed architecture cannot explain a linear average own-phase leakage merely by pointing to that global relation.

## 3. Subexponential transcript complexity cannot dephase at bounded energy

If `Y` has at most `K_R` states, then `I(X;Y)<=log K_R`; inserting this into `(2)` proves `(6)`. Equations `(5)` and `m -> infinity` then give `(7)` whenever `log K_R=o(R)` and the normalized coefficient energy remains bounded.

For the converse resource statement, `delta(W)<=1-eta` and `(16)` imply

\[
\rho\sqrt{\mathcal E(W)}\ge\eta.
\tag{19}
\]

Using `E(W)<=C` and `(1)` gives

\[
\frac{\eta^2}{C}
\le
\frac1{m^2}
+\frac2R\bigl(I(X;Y)+\operatorname{TC}(X)\bigr),
\]

which rearranges to `(8)`.

Thus low state count, low mutual information and low own-phase predictability are not three unrelated regularity notions in this endpoint model. Under bounded coefficient energy they are linked by one quantitative capacity budget.

The finite-state corollary should not be overread. A real- or complex-valued observation may have a huge or effectively full discrete information content even if it is described by one scalar coordinate. The invariant quantity is `I(X;Y)`, not the syntactic dimension of the output space.

## 4. Fano turns near-unit-energy dephasing into near-complete source recovery

For source `i`, let

\[
b_i(Y_i):=\mathbf E[X_i\mid Y_i].
\]

The Bayes error in predicting the binary phase from `Y_i` is

\[
e_i
=
\frac{1-\mathbf E|b_i(Y_i)|}{2}.
\tag{20}
\]

Because `|u|>=u^2` on `[-1,1]`,

\[
e_i
\le
\frac{1-\rho_i^2}{2}.
\tag{21}
\]

Binary Fano gives

\[
H(X_i\mid Y_i)\le h(e_i).
\tag{22}
\]

Since `Y` contains every `Y_i`,

\[
H(X\mid Y)
\le
\sum_i H(X_i\mid Y)
\le
\sum_i H(X_i\mid Y_i).
\tag{23}
\]

Using `(21)`, monotonicity of `h` on `[0,1/2]`, and concavity of binary entropy,

\[
H(X\mid Y)
\le
R\,h\!\left(\frac{1-\rho^2}{2}\right).
\tag{24}
\]

Now suppose `E(W)<=1` and `delta(W)<=epsilon`. Equation `(16)` forces

\[
\rho\ge1-\varepsilon,
\]

hence

\[
\frac{1-\rho^2}{2}
\le
\varepsilon-\frac{\varepsilon^2}{2}.
\]

Substituting this into `(24)` and using `I(X;Y)=H(X)-H(X|Y)` proves `(9)`.

This is substantially stronger than the small-information Pinsker direction when the architecture is close to the matched-filter energy floor. At exact unit energy, the conditional entropy vanishes. At near-exact error, the missing information is at most the binary-entropy penalty in `(9)`.

## 5. Prior art and novelty boundary

The information-theoretic ingredients are classical.

Satosi Watanabe, *Information Theoretical Analysis of Multivariate Correlation*, IBM Journal of Research and Development **4** (1960), 66--82, DOI `10.1147/rd.41.0066`, introduced total correlation as the entropy deficit

\[
\sum_i H(X_i)-H(X).
\]

Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley (2006), Chapter 2, develop the entropy and mutual-information chain rules, data processing and Fano's inequality used above.

`MC-339` already audited the separate classical ingredients behind the per-source inequality `(11)`: Rényi/HGR maximal correlation, the binary chi-square identity, data processing and the Pinsker conversion to Shannon mutual information.

A targeted literature audit on 17 September 2026 found the multivariate information mechanisms to be standard. No novelty is claimed for total correlation, conditional total correlation, Fano, Pinsker, entropy subadditivity or data processing. The durable Mathia delta is the exact specialization to the punctured reciprocal source law: `(3)`--`(5)` compute the dependence surcharge of that law, and `(1)`--`(10)` combine it with the independently derived endpoint energy obstruction to show that bounded-energy all-mode dephasing requires linear **joint transcript information**, with near-unit-energy near-exact dephasing requiring nearly the full source entropy.

## Boundaries and falsification tests

- **This remains a finite endpoint theorem.** It does not improve `M(x)` and supplies no analytic estimate for a natural Möbius coefficient family.
- **The transcript is the whole observation family.** Bounding one `I(X_i;Y_i)` is not enough to bound `I(X;Y)`; many individually weak observations can jointly encode the source vector.
- **The `TC(X)` surcharge is essential.** Dropping it would incorrectly treat punctured source phases, and especially the odd-rank parity family, as independent.
- **State count is only a corollary.** A low-dimensional real-valued statistic can carry linear or full discrete information. Future analytic work must bound actual mutual information or an equivalent source-natural capacity, not count coordinates.
- **Energy can substitute for information.** Equations `(2)` and `(8)` obstruct bounded-energy architectures; they do not rule out exponentially ill-conditioned amplification.
- **The near-complete recovery bound uses the matched-filter scale.** Equation `(9)` assumes `E(W)<=1`; larger energy weakens the required phase predictability and can lower the information demand.
- **No Shannon strong-DPI claim is made.** The proof uses only the per-source Pinsker inequality already established in `MC-339`, ordinary data processing, entropy identities and Fano.
- **No zero-free region or reciprocal-zeta continuation is used.** All arguments are finite probability/Hilbert-space algebra on the endpoint source model.

## Consequence for the research line

The source-natural frontier now has a genuinely global admission test. A candidate coefficient architecture cannot be justified merely by saying that each source omits its own phase, uses few named variables, or passes through a low-dimensional-looking statistic. At bounded normalized energy, any nontrivial all-mode dephasing must be paid for by a transcript whose information about the complete source vector is linear in the number of sources; at the matched-filter energy floor, near-exact dephasing requires near-complete source recovery.

The next arithmetic step is therefore sharper than after `MC-339`: identify a natural Möbius-derived observation family for which the **joint** transcript information can be bounded sublinearly (or otherwise quantified) while the coefficient energy remains bounded at the needed analytic scale. A source-specific construction whose observations collectively reconstruct the whole phase vector does not pass this stronger gate even if every individual observation appears locally innocuous.
