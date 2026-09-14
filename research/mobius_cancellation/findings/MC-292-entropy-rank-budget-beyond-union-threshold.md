# MC-292 — Entropy gives a global rank budget for biased shell characters beyond the union threshold

**Status:** `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the weighted Boolean-shell setup of `MC-289`--`MC-291`. Let

\[
H\cong \mathbf F_2^r,
\qquad |H|=q=2^r,
\]

let `S subset H` carry positive multiplicities `n_s`, and put

\[
N=\sum_{s\in S}n_s,
\qquad
p(s)=\frac{n_s}{N},
\qquad
E_2=\sum_{s\in S}n_s^2,
\qquad
\eta=\frac{N^2}{qE_2}.
\tag{1}
\]

Thus

\[
\sum_{s\in H}p(s)^2=\frac1{q\eta}.
\tag{2}
\]

For a character `lambda in H^*`, write

\[
x_\lambda
=\sum_{s\in H}p(s)(-1)^{\lambda(s)}
=\frac{A_\lambda}{N},
\tag{3}
\]

and define its `-1`-preferred defect

\[
d_\lambda
:=\Pr_p[\lambda(s)=0]
=\frac{1+x_\lambda}{2}.
\tag{4}
\]

Let

\[
\lambda_1,\ldots,\lambda_R\in H^*
\tag{5}
\]

be linearly independent. Write `d_i=d_{lambda_i}` and let

\[
h_2(u)=-u\log_2u-(1-u)\log_2(1-u)
\tag{6}
\]

be binary Shannon entropy, with the usual endpoint convention.

Then the shell participation ratio imposes the exact information budget

\[
\boxed{
\sum_{i=1}^R\bigl(1-h_2(d_i)\bigr)
\le
\log_2\frac1\eta.
}
\tag{7}
\]

Equivalently,

\[
\boxed{
\eta
\le
2^{-\sum_{i=1}^R(1-h_2(d_i))}.
}
\tag{8}
\]

Because `h_2(u)=h_2(1-u)`, the same statement can be written in terms of absolute Fourier biases:

\[
\boxed{
\sum_{i=1}^R
\left[
1-h_2\!\left(\frac{1-|x_{\lambda_i}|}{2}\right)
\right]
\le
\log_2\frac1\eta.
}
\tag{9}
\]

In particular, for the near-negative spectrum of `MC-291`, if

\[
d_{\lambda_i}\le\tau<\frac12
\qquad(1\le i\le R),
\tag{10}
\]

then

\[
\boxed{
R\bigl(1-h_2(\tau)\bigr)
\le
\log_2\frac1\eta,
}
\tag{11}
\]

so

\[
\boxed{
R
\le
\frac{\log_2(1/\eta)}{1-h_2(\tau)}.
}
\tag{12}
\]

Unlike the common-cell estimate in `MC-291`, this bound has **no requirement that `R tau<1`**. It therefore remains informative after the union-bound intersection argument has become vacuous. It is not uniformly stronger than `MC-291`: when the total defect `sum_i d_i` is small, the explicit common-cell mass retained there can give the sharper estimate. The two bounds cover complementary regimes.

No estimate for `M(x)` follows. The result closes a finite-structural gap in the exceptional-character interface: a large family of independently biased generated characters must spend a finite entropy deficit already visible in the shell's `L^2` participation ratio.

## 1. Collision entropy of the shell is exactly the participation ratio

Let `X` be the `H`-valued random variable with law `p`. Its order-two Rényi entropy is

\[
H_2(X)
:=-\log_2\sum_s p(s)^2.
\tag{13}
\]

Using `(2)`,

\[
\boxed{
H_2(X)=\log_2(q\eta)=r+\log_2\eta.
}
\tag{14}
\]

Shannon entropy dominates collision entropy, so

\[
H(X)\ge H_2(X)=r+\log_2\eta.
\tag{15}
\]

This is the only place where the quadratic participation statistic enters. Thus `log_2(1/eta)` is an upper bound on the number of bits by which the shell measure can fall short of uniform entropy on its generated ambient group.

For completeness, `(15)` follows directly from Jensen: with expectation under `p`,

\[
-H(X)
=\mathbb E_p[\log_2 p(X)]
\le
\log_2\mathbb E_p[p(X)]
=
\log_2\sum_s p(s)^2.
\tag{16}
\]

## 2. Independent biased characters consume independent entropy directions

Consider the surjective linear map

\[
T:H\longrightarrow\mathbf F_2^R,
\qquad
T(s)=(\lambda_1(s),\ldots,\lambda_R(s)).
\tag{17}
\]

Surjectivity follows from independence of the `lambda_i`; every fiber therefore has exactly

\[
2^{r-R}=q/2^R
\tag{18}
\]

points. Let

\[
Y=T(X)=(Y_1,\ldots,Y_R).
\tag{19}
\]

The chain rule gives

\[
H(X)=H(Y)+H(X\mid Y).
\tag{20}
\]

Since a conditional law `X|Y=y` is supported inside one fiber of size `2^{r-R}`,

\[
H(X\mid Y)\le r-R.
\tag{21}
\]

Combining `(15)`, `(20)` and `(21)`,

\[
H(Y)
\ge
H(X)-(r-R)
\ge
R+\log_2\eta.
\tag{22}
\]

On the other hand, Shannon subadditivity gives

\[
H(Y)\le\sum_{i=1}^R H(Y_i).
\tag{23}
\]

By definition, `Pr[Y_i=0]=d_i`, hence

\[
H(Y_i)=h_2(d_i).
\tag{24}
\]

Therefore

\[
R+\log_2\eta
\le
\sum_{i=1}^R h_2(d_i),
\tag{25}
\]

which rearranges to `(7)`.

The proof is finite, exact, and uses no independence assumption on the random bits `Y_i`. Their **linear functionals** are independent; the induced coordinate random variables can be arbitrarily dependent. That distinction is essential.

## 3. The near-negative rank bound survives after common-cell intersection disappears

For `0<=u<1/2`, `h_2(u)` is increasing. Hence `(10)` implies

\[
1-h_2(d_i)\ge1-h_2(\tau)
\tag{26}
\]

for every chosen basis mode. Summing and using `(7)` proves `(11)` and `(12)`.

The comparison with `MC-291` is now precise. Its elementary union argument gives, when `R tau<1`,

\[
\eta
\le
\frac{2^{-R}}{(1-R\tau)^2}.
\tag{27}
\]

That estimate tracks the mass of one exact common preferred-sign cell and is strong when `R tau` is well below one. But once `R tau>=1`, the union bound no longer certifies any common mass and `(27)` disappears entirely.

The entropy inequality instead charges each biased direction separately. As long as `tau<1/2`, every direction costs the positive amount

\[
1-h_2(\tau)>0,
\tag{28}
\]

so a finite rank budget remains even when the defect sets can collectively cover the whole shell.

At the endpoint `tau=0`, `(12)` becomes

\[
R\le\log_2\frac1\eta.
\tag{29}
\]

This scale is exact: if `p` is uniform on an affine fiber of codimension `R` on which all selected characters equal `-1`, then `eta=2^{-R}` and equality holds in `(29)`.

As `tau` tends to `1/2`, `1-h_2(tau)` tends to zero and the bound correctly becomes vacuous: a character with vanishing bias should cost no structural information.

## 4. Geelen-scale reading

The collision-rich frontier in `MC-288`--`MC-291` naturally reaches participation scales of the form

\[
\eta\asymp t2^{-t}.
\tag{30}
\]

Then

\[
\log_2\frac1\eta
=t-\log_2 t+O(1).
\tag{31}
\]

If the near-negative defect is on the reciprocal scale

\[
\tau=\frac c t
\tag{32}
\]

for fixed `c>0`, binary entropy has the expansion

\[
h_2(c/t)
=
\frac c t\log_2\frac t c
+
\frac{c}{t\ln2}
+O_c(t^{-2}).
\tag{33}
\]

Consequently `(12)` gives

\[
\boxed{
R
\le
 t+(c-1)\log_2 t+O_c(1).
}
\tag{34}
\]

The useful point is not the exact lower-order coefficient but the regime change. At `c>=1`, a rank of order `t` lies at or beyond the common-cell union threshold `R tau=1`, while the entropy budget still prevents the exceptional spectrum from acquiring arbitrarily many independent directions. For `c<1`, both mechanisms apply and the common-cell estimate may remain sharper.

Thus the dual exceptional spectrum now has two distinct rigidity mechanisms:

- **intersection rigidity** when the total defect is below one, from `MC-291`;
- **information-budget rigidity** for every fixed bias away from zero, from `(7)`--`(12)`.

Neither mechanism supplies the missing arithmetic theorem controlling actual generated quadratic-character sums.

## 5. Arithmetic interpretation

In the Legendre-shell application of `MC-281`--`MC-291`, each generated functional corresponds to an actual quadratic product character, and

\[
x_\lambda
=
\frac1N\sum_{\rho\in\mathcal R_y}\chi_\lambda(\rho).
\tag{35}
\]

Hence `(7)` says that linearly independent strongly biased product characters cannot be treated as unrelated exceptional modes. Their total bias consumes the shell's finite entropy deficit.

This gives a clean interface for a future arithmetic exceptional-character theorem. Such a theorem need not initially prove that the bad family is tiny in cardinality. It may instead show that many bad generated characters carry independent conductor/residue directions. The entropy budget then turns those independent directions into a contradiction whenever their accumulated bias cost exceeds `log_2(1/eta)`.

Conversely, a bad family can evade `(7)` by being highly linearly dependent even when its cardinality is large. This clarifies why counting exceptional characters and controlling the **rank** of the exceptional family are genuinely different arithmetic tasks, as already suggested by `MC-291`.

## 6. Prior art and novelty audit

The mechanism is classical. Russell Impagliazzo, Cristopher Moore and Alexander Russell, *An Entropic Proof of Chang's Inequality*, SIAM Journal on Discrete Mathematics 28 (2014), 173--176, DOI `10.1137/120877982`, prove Chang-type Fourier-spectrum bounds by exactly the entropy principle used here: independent parity observables cannot collectively be too biased when the underlying distribution retains high entropy. Their paper explicitly records a refinement for highly biased variables, so entropy-sensitive treatment of near-extremal Fourier coefficients is established prior art.

James R. Lee, *Covering the Large Spectrum and Generalized Riesz Products*, SIAM Journal on Discrete Mathematics 31 (2017), 562--572, DOI `10.1137/15M1048604`, formulates Chang's lemma directly for large spectra of probability distributions on finite abelian groups and develops entropy-maximization proofs. This confirms that moving from uniform subsets to weighted probability measures is also established prior art.

The original large-spectrum framework goes back to M.-C. Chang, *A polynomial bound in Freiman's theorem*, Duke Mathematical Journal 113 (2002), 399--419. The monotonicity `H_1>=H_2`, Shannon subadditivity, and the fiber-entropy bound used above are standard information-theoretic inequalities.

Accordingly, **no novelty is claimed** for the entropy argument, Chang's lemma, large-spectrum rank control, or the use of Shannon/Rényi entropy. The durable line-specific content is the exact substitution of the current shell participation ratio `eta` and one-sided defects into that classical mechanism, yielding `(7)` and the threshold-free continuation `(12)` of the rank interface left by `MC-291`.

A targeted literature audit found the surrounding mechanism explicitly in the sources above; it did not justify treating `(7)` as a new general theorem. The statement is therefore recorded as a classical-mechanism frontier refinement only.

## Boundaries and falsification tests

- Independence in `(5)` is linear independence in `H^*`. The random bits `Y_i` need not be probabilistically independent; assuming they are would be false and is not used.
- The participation ratio `eta` is essential to the stated observable bound. Replacing collision entropy by raw support density is valid only in the flat-multiplicity case.
- The entropy estimate is not uniformly stronger than the common-cell estimate of `MC-291`. For `sum_i d_i<1`, retaining the actual intersection mass can give a better bound.
- The threshold-free statement still requires nonzero bias to be informative. At `tau=1/2`, the denominator in `(12)` vanishes exactly.
- The bound controls **rank**, not cardinality. Exponentially many biased characters can in principle lie in a low-dimensional dual subspace.
- The sign is irrelevant to the entropy cost because binary entropy is symmetric, but the arithmetic application still needs the negative sign selected by the odd-moment obstruction in `MC-289` and `MC-290`.
- Nothing here controls the conductors of the generated quadratic product characters, their distribution across moduli, or their shell sums by analytic number theory. Those remain the arithmetic bottleneck.
- No RH, GRH, zeta zero-free region, reciprocal-zeta continuation, random-walk heuristic, or unproved character-sum estimate is used.

## Consequence for the research line

The `R tau<1` condition in the rank part of `MC-291` was a limitation of the common-cell union argument, not a fundamental loss of control. The exceptional spectrum retains a global rank budget for every nontrivial bias level, and the exact cost of each independent mode is `1-h_2(d_lambda)` bits. The finite-geometric side of the current endpoint obstruction is therefore more rigid than the union bound alone suggested.

The remaining frontier is still arithmetic: obtain information about the actual generated quadratic-character family that controls its defect profile, independent rank, conductor complexity, or multiplicity participation. Further purely finite-geometric refinements should now be judged against whether they add such arithmetic leverage rather than merely repackage the same entropy budget.