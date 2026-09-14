# MC-289 — Weighted odd moments force a single negative shell character

**Status:** `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the collision-rich odd-shell setup of `MC-288`. Let

\[
S\subset \mathbf F_2^d,
\qquad
H:=\langle S\rangle,
\qquad
|H|=2^r=:q,
\]

be the distinct occupied projected Legendre-sign cells and their linear span. Let `n_s>=1` be the number of shell primes in cell `s`, and put

\[
N:=\sum_{s\in S}n_s,
\qquad
E_2:=\sum_{s\in S}n_s^2,
\qquad
\eta:=\frac{N^2}{qE_2}.
\tag{1}
\]

Thus `eta` is the effective occupied fraction seen by the multiplicity distribution: by Cauchy,

\[
0<\eta\le \frac{|S|}{q}.
\tag{2}
\]

Fix an odd target shell weight `t>=3`. Assume, as in the collision-rich branch of `MC-288`, that there is no exact `t`-element endpoint row and that `N-|S|>=t-1`. Then `MC-288` proves that `S` contains no odd zero-sum subset of cardinality at most `t`.

For every nonzero linear functional `lambda in H^*`, define the multiplicity-weighted Fourier coefficient

\[
A_\lambda
:=
\sum_{s\in S} n_s(-1)^{\lambda(s)}.
\tag{3}
\]

Then there exists a nonzero `lambda` such that

\[
\boxed{
\frac{A_\lambda}{N}
\le
-
\left(\frac{\eta}{1-\eta}\right)^{1/(t-2)}.
}
\tag{4}
\]

Equivalently, if every nontrivial generated character has one-sided shell bias

\[
\frac{A_\lambda}{N}>-\delta
\qquad(0<\delta<1),
\tag{5}
\]

then necessarily

\[
\boxed{
\eta
<
\frac{\delta^{t-2}}{1+\delta^{t-2}}.
}
\tag{6}
\]

The coefficient `(3)` is not an abstract graph eigenvalue in the arithmetic application. Any `lambda in H^*` extends to the ambient coordinate space, and the corresponding sign is a product of the projected Legendre coordinates. Hence

\[
A_\lambda
=
\sum_{\rho\in\mathcal R_y}\chi_\lambda(\rho),
\tag{7}
\]

for the associated real quadratic product character on the shell (with the same shell conventions as `MC-281`--`MC-288`). Therefore every collision-rich odd endpoint escape has a scalar arithmetic witness: either its multiplicity distribution has exponentially tiny effective occupancy `eta`, or one generated quadratic character has a quantitatively negative shell average.

At the live scale

\[
t=\left(\frac1{\log 2}+o(1)\right)\log\log y,
\tag{8}
\]

this amplification is substantial. If

\[
\eta\ge e^{-Ct}
\tag{9}
\]

for some fixed `C>0`, then `(4)` gives

\[
-\frac{A_\lambda}{N}
\ge e^{-C+o(1)}.
\tag{10}
\]

In particular, if multiplicities are approximately flat and the support density is near the sharp Geelen scale from `MC-288`,

\[
\eta\asymp \frac{t}{2^t},
\tag{11}
\]

then some generated product character has

\[
\boxed{
\frac{A_\lambda}{N}\le -\frac12+o(1).
}
\tag{12}
\]

Thus the `2^{-t}` non-affine support escape from `MC-288` is not Fourier-invisible when its multiplicities have comparable effective density: the full sequence of forbidden short odd relations amplifies that sparse occupancy into constant one-character bias.

No bound for `M(x)` is improved, and `(4)` alone does not exclude the endpoint escape. It converts the remaining combinatorial obstruction into a precise tradeoff between multiplicity concentration and a single quadratic-character sum.

## 1. No short odd support relation kills every short odd weighted convolution at zero

Define a positive function `w:H->R_{>=0}` by

\[
w(s)=n_s\quad(s\in S),
\qquad
w(s)=0\quad(s\notin S).
\tag{13}
\]

Let `m<=t` be odd. Suppose an ordered `m`-tuple

\[
(s_1,\ldots,s_m)\in S^m
\]

satisfied

\[
s_1+\cdots+s_m=0.
\tag{14}
\]

Cancel every cell occurring an even number of times. The cells left with odd multiplicity form a subset `B subset S` satisfying

\[
\sum_{s\in B}s=0.
\tag{15}
\]

Because `m` is odd, `|B|` is odd; in particular `B` is nonempty, and `|B|<=m<=t`. This contradicts the no-short-odd-zero-sum conclusion of `MC-288`. Hence there are no such tuples and therefore

\[
\boxed{
w^{*m}(0)=0
\qquad\text{for every odd }m\le t.
}
\tag{16}
\]

This point is stronger than merely saying that the distinct support has large odd girth. Repetitions are already included in the convolution, and characteristic two reduces every repeated tuple to exactly the forbidden odd support nucleus.

## 2. Fourier inversion turns the vanished convolutions into exact odd spectral moments

For `lambda in H^*`, write

\[
A_\lambda=\widehat w(\lambda)
=\sum_{s\in H}w(s)(-1)^{\lambda(s)}.
\tag{17}
\]

The principal coefficient is

\[
A_0=N.
\tag{18}
\]

Fourier inversion for convolution on the group `H` gives

\[
\sum_{\lambda\in H^*}A_\lambda^m
=
q\,w^{*m}(0).
\tag{19}
\]

Together with `(16)`, for every odd `m<=t`,

\[
\boxed{
\sum_{\lambda\ne0}A_\lambda^m=-N^m.
}
\tag{20}
\]

Parseval gives the independent second-moment identity

\[
\sum_{\lambda\in H^*}A_\lambda^2
=q\sum_{s\in H}w(s)^2
=qE_2,
\tag{21}
\]

hence

\[
D:=\sum_{\lambda\ne0}A_\lambda^2
=qE_2-N^2
=N^2\left(\frac1\eta-1\right).
\tag{22}
\]

## 3. The top forbidden odd moment amplifies effective occupancy into negative bias

Let

\[
B:=-\min_{\lambda\ne0}A_\lambda.
\tag{23}
\]

Equation `(20)` implies `B>0`. For every nonprincipal coefficient and every odd `m>=3`,

\[
A_\lambda^m
\ge
-B^{m-2}A_\lambda^2.
\tag{24}
\]

Indeed `(24)` is immediate for `A_lambda>=0`; for `A_lambda<0`, it is exactly `|A_lambda|<=B`.

Summing `(24)` over `lambda!=0` and using `(20)` and `(22)` gives

\[
-N^m
\ge
-B^{m-2}D,
\]

so

\[
\left(\frac BN\right)^{m-2}
\ge
\frac{N^2}{D}
=
\frac{\eta}{1-\eta}.
\tag{25}
\]

Already `m=3` shows `eta<=1/2`, as it must in the triangle-free regime. Since the base in `(25)` is at most one, the strongest bound among the available odd moments is obtained from the largest one, namely `m=t`. This proves `(4)`.

Conversely, `(5)` says `B/N<delta`. Substituting into `(25)` at `m=t` and solving for `eta` yields `(6)`.

The exponent `1/(t-2)` is the key gain. A density or participation ratio that is exponentially small in `t` becomes only constantly small after taking this root. At the Geelen scale `eta~t2^{-t}`, taking logarithms in `(4)` gives

\[
\frac1{t-2}
\log\!\left(\frac{\eta}{1-\eta}\right)
=-\log2+o(1),
\]

which is `(12)`.

## 4. Arithmetic interpretation and remaining escape

Represent each projected Legendre-sign cell by bits so that a linear functional `lambda` corresponds to multiplying a subset of the coordinate signs. For a shell prime `rho` in cell `s(rho)`,

\[
(-1)^{\lambda(s(\rho))}=\chi_\lambda(\rho),
\tag{26}
\]

where `chi_lambda` is the associated quadratic product character. Summing over shell primes and grouping by occupied cell gives `(7)` exactly.

This makes `(4)` a useful complement to `MC-288`:

- the affine branch of `MC-288` has a functional with `A_lambda=-N`, the endpoint `B/N=1` of the same scalar obstruction;
- the non-affine branch can avoid a substantial negative character only by making `eta=N^2/(2^r E_2)` exponentially small in `t`;
- small `eta` has two possible causes that must remain distinct: genuinely tiny support density in its own span, or severe multiplicity concentration measured by large `E_2`.

Thus a future arithmetic attack no longer needs to reason only about full pattern occupancy. A one-sided family estimate for the generated quadratic-character shell sums, combined with any independent lower bound on `eta`, would exclude the collision-rich endpoint escape through `(6)`.

The theorem does **not** supply such a lower bound on `eta`. In particular, the density upper bound from `MC-288` cannot be reversed, and highly concentrated multiplicities can make `eta` arbitrarily smaller than `|S|/2^r`. Treating `(12)` as unconditional would therefore be false.

## 5. Prior art and novelty audit

The proof mechanism is classical finite Fourier/spectral graph theory: Fourier characters diagonalize convolution on a finite abelian group, closed-walk counts are spectral moments, and absence of short odd cycles forces the corresponding odd traces to vanish. The weighted formulation above is the same moment mechanism applied to the positive multiplicity function rather than an unweighted adjacency matrix.

A targeted literature check found substantial existing work connecting odd girth and the bottom adjacency eigenvalue, including recent 2026 work by Abiad, Taranchuk and van Veluw on `lambda_max+lambda_min` for graphs of high odd girth, and Yip on the same spectral measure. Those results confirm that bottom-spectrum control as a measure of near-bipartiteness is established prior art. Their graph-normalized statements are not being claimed as the source of `(4)`; `(4)` follows directly from the elementary odd-moment identities above and is recorded only as the specialization needed by the Mathia shell multiplicities.

The finite-geometric input that supplies the no-short-odd-relation hypothesis is the Geelen theorem composition already audited in `MC-288`; no new claim is made about that theorem.

No novelty is claimed for Fourier diagonalization, trace moments, Cayley graphs, odd girth, or least-eigenvalue methods. The research contribution recorded here is the exact weighted arithmetic reduction `(4)`--`(7)`: the current collision-rich shell obstruction forces either exponentially small effective occupancy or one explicit negative generated-character sum.

## Boundaries and falsification tests

- The collision-rich hypothesis from `MC-288` is essential because it is what upgrades absence of one prescribed `t`-row into absence of **every** short odd support relation.
- The target weight `t` must be odd. Even-weight endpoint rows are governed by the pairing obstruction already handled in `MC-285`.
- `eta` is an `L^2` participation ratio, not the raw support density. Replacing it by `K/2^r` in `(4)` without multiplicity control reverses the only available inequality and is invalid.
- The bias is one-sided and negative. Bounds only on positive real parts do not exclude it; an analytic input must control the negative shell character sum relevant to `(7)`.
- The functional lives on `H=<S>`. Extending it to the ambient coordinate space is harmless for values on occupied cells, but different ambient extensions can represent the same character on `H`.
- Nothing here bounds the conductor of the resulting quadratic product character. Large effective coordinate conductor remains a genuine arithmetic escape.
- The derivation is finite and exact; it uses no RH, GRH, zero-free region, or probabilistic independence heuristic.

## Consequence for the research line

The sparse branch left by `MC-288` now has a scalar analytic interface. In the collision-rich odd regime, high odd girth cannot coexist with both a reasonably spread multiplicity distribution and uniformly small negative generated-character sums. At the natural `2^{-t}` density scale, the full odd-moment stack forces order-one character bias rather than the vanishing bias suggested by a second-moment-only argument. The next arithmetic question is therefore sharper: obtain one-sided shell cancellation for the generated quadratic characters, or prove that the actual Legendre shell can drive `eta` below the exponential-in-`t` threshold required by `(6)`.