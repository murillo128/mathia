# MC-339 — Maximal correlation makes source-phase leakage a compositional information budget

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-338` defines the own-phase leakage

\[
\rho_i^2
:=\left\|\mathbf E[X_i\mid Y_i]\right\|_2^2,
\qquad
X_i:=x_i(A),
\]

for a uniformly sampled nonprincipal mode `A` in

\[
\Xi=\mathbf F_2^R\setminus\{0\},
\qquad m=|\Xi|=2^R-1,
\]

and an admitted source observation `Y_i`. This leakage has an exact classical information-theoretic normalization.

Let

\[
\kappa_i:=\rho_{\mathrm{HGR}}(X_i;Y_i)
\]

be the Hirschfeld--Gebelein--Rényi maximal correlation. Since `X_i` is a nonconstant binary variable and

\[
\mathbf E X_i=-\frac1m,
\qquad
\operatorname{Var}(X_i)=1-\frac1{m^2},
\]

one has the exact identity

\[
\boxed{
\rho_i^2
=\frac1{m^2}
+\left(1-\frac1{m^2}\right)\kappa_i^2.
}
\tag{1}
\]

Equivalently, because one variable is binary,

\[
\kappa_i^2
=D_{\chi^2}
\!\left(P_{X_iY_i}\,\middle\|\,P_{X_i}P_{Y_i}\right),
\tag{2}
\]

so the nontrivial part of `MC-338` leakage is exactly a normalized chi-square information quantity. The residual `m^{-2}` is not dependence at all: it is the deterministic bias created by deleting the principal mode.

Writing

\[
\bar\kappa^2:=\frac1R\sum_{i=1}^R\kappa_i^2,
\]

and keeping the normalized coefficient energy `\mathcal E(W)` and RMS dephasing error `\delta(W)` of `MC-338`, its energy obstruction becomes

\[
\boxed{
\delta(W)\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{
\frac1{m^2}
+\left(1-\frac1{m^2}\right)\bar\kappa^2
}
\right)_+.
}
\tag{3}
\]

Hence exact dephasing obeys

\[
\boxed{
\mathcal E(W)\ge
\frac1{
 m^{-2}+(1-m^{-2})\bar\kappa^2
}.
}
\tag{4}
\]

At matched-filter energy `\mathcal E(W)\le1`, exact dephasing is possible only if

\[
\bar\kappa^2=1.
\]

Since every `\kappa_i\le1`, this forces `\kappa_i=1` for every source, and for binary `X_i` this means that the admitted observation `Y_i` determines the own phase `X_i` almost surely. Thus the unit-energy loophole is now characterized invariantly: **baseline-energy exact dephasing requires complete source-phase information, not merely a convenient coordinate representation.**

The same quantity is compositional. For a genuine Markov processing chain

\[
X_i-U_{i,1}-U_{i,2}-\cdots-U_{i,L}=Y_i,
\]

maximal correlation satisfies

\[
\kappa_i
\le
\prod_{j=0}^{L-1}
\rho_{\mathrm{HGR}}(U_{i,j};U_{i,j+1}),
\qquad U_{i,0}:=X_i.
\tag{5}
\]

Therefore any source-natural architecture whose successive information channels have contraction factors `\alpha_{i,j}` inherits `(3)`--`(4)` with

\[
\kappa_i^2\le\prod_j\alpha_{i,j}^2.
\tag{6}
\]

This turns the informal requirement "the coefficient should not reconstruct its own phase" into a quantitative, coordinate-invariant and data-processing-stable resource budget.

There is also a Shannon-information corollary. With natural logarithms, Pinsker's inequality gives

\[
\rho_i^2-\frac1{m^2}
\le 2 I(X_i;Y_i).
\tag{7}
\]

Thus, for

\[
\bar I:=\frac1R\sum_i I(X_i;Y_i),
\]

one has the weaker but sometimes easier-to-audit obstruction

\[
\boxed{
\delta(W)\ge
\left(
1-\sqrt{\mathcal E(W)}
\sqrt{m^{-2}+2\bar I}
\right)_+.
}
\tag{8}
\]

In particular, along a family with `m\to\infty`, bounded coefficient energy and `\bar I=o(1)` force `\delta(W)\to1`: a vanishing average information budget cannot create an all-mode constant target at bounded energy.

No estimate for `M(x)` follows. The result is a finite reciprocal-endpoint admission theorem for future source-natural analytic coefficient classes.

## 1. Binary source phases collapse Rényi's variational problem to one function

On the full group a nontrivial character has equal `+1` and `-1` mass. Removing the principal point, where every character equals `+1`, gives

\[
\mathbf P(X_i=+1)=\frac{m-1}{2m},
\qquad
\mathbf P(X_i=-1)=\frac{m+1}{2m}.
\tag{9}
\]

Therefore the unique centered unit-variance function of `X_i`, up to sign, is

\[
\phi_i(X_i)
=
\frac{X_i+m^{-1}}{\sqrt{1-m^{-2}}}.
\tag{10}
\]

Rényi's one-function characterization of maximal correlation states

\[
\rho_{\mathrm{HGR}}^2(X;Y)
=
\sup_{\substack{\mathbf Ef(X)=0\\\mathbf E f(X)^2=1}}
\mathbf E\left[\mathbf E[f(X)\mid Y]^2\right].
\tag{11}
\]

Because `X_i` has only two values, the supremum in `(11)` has only the two choices `\pm\phi_i`. Hence

\[
\kappa_i^2
=
\frac{
\mathbf E\left[
\left(\mathbf E[X_i\mid Y_i]+m^{-1}\right)^2
\right]
}{1-m^{-2}}.
\tag{12}
\]

Using `\mathbf E\mathbf E[X_i\mid Y_i]=-m^{-1}` and the definition of `\rho_i` gives

\[
\kappa_i^2
=
\frac{\rho_i^2-m^{-2}}{1-m^{-2}},
\]

which is `(1)`.

The standard finite-alphabet singular-value formula for maximal correlation further gives `(2)` whenever one of the two variables is binary. Thus `\kappa_i^2` is simultaneously the squared HGR maximal correlation, the normalized variance of the optimal conditional-mean predictor, and the chi-square divergence from independence.

## 2. The information budget plugs directly into the MC-338 energy currency

`MC-338` proves

\[
\delta(W)\ge\bigl(1-\rho\sqrt{\mathcal E(W)}\bigr)_+,
\qquad
\rho^2=\frac1R\sum_i\rho_i^2.
\tag{13}
\]

Averaging `(1)` yields

\[
\rho^2
=
\frac1{m^2}
+\left(1-\frac1{m^2}\right)\bar\kappa^2.
\tag{14}
\]

Substitution into `(13)` proves `(3)` and `(4)`.

The unit-energy case is especially rigid. Exact dephasing with `\mathcal E(W)\le1` forces the denominator in `(4)` to equal one, hence `\bar\kappa^2=1`. For binary `X_i`, `\kappa_i=1` is equivalent through `(12)` to

\[
\operatorname{Var}(\mathbf E[X_i\mid Y_i])
=
\operatorname{Var}(X_i),
\]

so the conditional variance vanishes and `X_i` is measurable from `Y_i`. The matched-filter escape of `MC-332` therefore reappears exactly at the point where the information channel has enough capacity to recover the target phase.

## 3. Data processing makes the obstruction stable under re-encoding and staged summaries

For centered `L^2` spaces, conditional expectation is a contraction operator and HGR maximal correlation is its operator norm. If

\[
X-U-V
\]

is a Markov chain, the conditional-expectation operator from functions of `X` to functions of `V` factors through the corresponding operator for `U`. Operator-norm submultiplicativity gives

\[
\rho_{\mathrm{HGR}}(X;V)
\le
\rho_{\mathrm{HGR}}(X;U)
\rho_{\mathrm{HGR}}(U;V).
\tag{15}
\]

Iteration proves `(5)`. Invertible re-encodings have contraction factor one and therefore leave the budget unchanged, while genuinely lossy stages cannot increase it. This is stronger than a syntactic "variable exclusion" rule: it survives arbitrary changes of coordinates and supplies an explicit multiplication law for independent processing stages.

The Markov hypothesis is load-bearing. An architecture with a hidden bypass carrying information from the underlying mode directly to a later stage need not factor as `(5)`; in that case the actual joint law of `(X_i,Y_i)` must be audited rather than multiplying fictitious stagewise contractions.

## 4. Shannon mutual information gives a coarser but convenient sufficient certificate

Let

\[
p=\mathbf P(X_i=+1),
\qquad
q(Y_i)=\mathbf P(X_i=+1\mid Y_i).
\]

Then

\[
\operatorname{Var}(\mathbf E[X_i\mid Y_i])
=4\,\mathbf E\bigl(q(Y_i)-p\bigr)^2.
\tag{16}
\]

Meanwhile

\[
I(X_i;Y_i)
=
\mathbf E_{Y_i}
D_{\mathrm{KL}}
\bigl(\operatorname{Ber}(q(Y_i))\,\|\,\operatorname{Ber}(p)\bigr).
\tag{17}
\]

Pinsker's inequality in nats gives each conditional divergence at least `2(q-p)^2`. Combining `(16)`--`(17)` gives

\[
\operatorname{Var}(\mathbf E[X_i\mid Y_i])
\le 2I(X_i;Y_i),
\]

which is `(7)`. Averaging and inserting this upper bound for `\rho^2` into `(13)` proves `(8)`.

This direction is intentionally one-sided. HGR squared is **not** the general strong data-processing constant for Shannon mutual information; using it as such would be false. The Shannon corollary here follows only from the binary posterior calculation plus Pinsker.

## 5. Prior art and novelty boundary

The dependence theory is classical. Alfréd Rényi, *On measures of dependence*, Acta Mathematica Academiae Scientiarum Hungaricae **10** (1959), 441--451, DOI `10.1007/BF02024507`, develops maximal correlation through conditional means. Venkat Anantharam, Amin Gohari, Sudeep Kamath and Chandra Nair, *On Maximal Correlation, Hypercontractivity, and the Data Processing Inequality studied by Erkip and Cover*, arXiv:1304.6133 (2013), records Rényi's conditional-expectation characterization, the finite-alphabet singular-value form, and the explicit binary identity

\[
\rho_{\mathrm{HGR}}^2(X;Y)
=
D_{\chi^2}(P_{XY}\|P_XP_Y)
\]

when one variable is binary. That paper also supplies an important negative boundary: replacing the correct Shannon strong-data-processing constant by HGR squared is false in general.

Shahab Asoodeh, Mario Diaz, Fady Alajaji and Tamás Linder, *Information Extraction Under Privacy Constraints*, Information **7** (2016), 15, DOI `10.3390/info7010015`, treats maximal correlation as an information-leakage quantity and records its data-processing behavior for Markov filtering.

A targeted audit on 16 September 2026 found these mechanisms to be established information theory. No novelty is claimed for HGR maximal correlation, its conditional-expectation or chi-square characterizations, Pinsker's inequality, or data processing. The durable Mathia delta is the exact specialization `(1)` to the punctured reciprocal source phase and its substitution into the independently derived dephasing-energy theorem `MC-338`, yielding the explicit information/conditioning tradeoffs `(3)`--`(8)`.

## Boundaries and falsification tests

- **This is still an endpoint theorem.** It does not improve `M(x)` and does not show that a natural analytic Möbius construction has small `\bar\kappa` or small `\bar I`.
- **The `m^{-2}` floor is deterministic bias, not hidden dependence.** An observation independent of `X_i` has `\kappa_i=0` but `\rho_i^2=m^{-2}` because the nonprincipal family itself is biased.
- **The exact HGR reduction uses binary `X_i`.** A future source observable with more than two phase values keeps Rényi's variational formula but need not collapse to one centered function or to the binary chi-square identity.
- **Data-processing multiplication requires a real Markov factorization.** Shared latent information or bypass paths invalidate the product bound and must be included in the observation variable.
- **Small Shannon mutual information is sufficient, not necessary, for the HGR obstruction used here.** Equation `(8)` is deliberately weaker than `(3)`.
- **Do not use HGR squared as a Shannon strong-DPI constant.** The literature contains a published counterexample to that tempting but incorrect step.
- **Conditioning and information must be controlled simultaneously.** Small maximal correlation blocks bounded-energy dephasing, but exponentially growing coefficient energy can still exploit correspondingly small leakage as already shown by `MC-338`.
- **No zero-free region or reciprocal-zeta continuation is used.** The proof is finite probability/Hilbert-space algebra on the reciprocal endpoint.

## Consequence for the research line

The source-natural frontier now has a compositional admission variable. Instead of specifying a preferred source coordinate system and forbidding selected variables by syntax, a candidate analytic architecture can be tested by the actual information channel from each own phase into its admitted coefficient observation. HGR maximal correlation gives the exact `L^2` quantity needed by the existing dephasing theorem; Shannon mutual information gives a coarser sufficient certificate when that is easier to bound; and genuine staged summaries inherit a data-processing budget.

The remaining arithmetic obligation is correspondingly sharp: construct a natural Möbius-derived coefficient family whose source observations have provably small own-phase information **and** whose coefficient energy remains at the analytic scale needed for a useful family estimate. Without both properties, the finite endpoint can still be flattened by matched filtering or by ill-conditioned amplification.