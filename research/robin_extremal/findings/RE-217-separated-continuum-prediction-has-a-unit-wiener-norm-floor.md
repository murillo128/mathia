# RE-217 — Separated continuum prediction has a unit Wiener-norm floor

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + CAUSAL-PREDICTION + WIENER-NORM-LOWER-BOUND + PREDICTOR-SOURCE-SEPARATION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-208, RE-215, RE-216.

`RE-216` lowers the explicit coefficient-variation rate of the separated continuum predictor from `12 log 2=8.3177...` to at most `6.081`, while `RE-208` can realize every strict variation exponent below `1/2` by ordinary-prime `{0,1,2}` edits. The remaining factor was described as a predictor/source-norm mismatch, but the spectral side had not been isolated as its own quantitative extremal problem.

The continuous Kaiser test of `RE-215` gives exactly that isolation. Let `mu` be any finite **complex** measure supported on `[H,infinity)`, with `H>0`, and assume

\[
\sup_{|t|\le T}
\left|1-\widehat\mu(t)\right|
\le \epsilon,
\qquad
0\le\epsilon<1.
\tag{1}
\]

Write `||mu||_TV` for its total variation. For fixed `H` and `HT -> infinity`, one has

\[
\boxed{
\|\mu\|_{TV}
\gg_H
(1-\epsilon)
\frac{e^{HT}}{HT\log(HT)}.
}
\tag{2}
\]

For a finite exponential predictor

\[
\widehat\mu(t)=\sum_{j=1}^{J}b_j e^{-itL_j},
\qquad L_j\ge H,
\tag{3}
\]

this is the Wiener-norm bound

\[
\boxed{
\sum_{j=1}^{J}|b_j|
\gg_H
(1-\epsilon)
\frac{e^{HT}}{HT\log(HT)}.
}
\tag{4}
\]

Thus every logarithmic-height predictor with `T_Q=c log Q` and bounded-away-from-one error satisfies

\[
\boxed{
\log\sum_j|b_{Q,j}|
\ge
(Hc-o(1))\log Q.
}
\tag{5}
\]

Equivalently, if its coefficient variation is `Q^{kappa+o(1)}`, then necessarily

\[
\boxed{\kappa\ge Hc.}
\tag{6}
\]

This turns the current constructive gap into a pure approximation constant. Define `C_sep` as the infimum, over separated predictor families with some fixed support corridor `[H,C H]`, uniform error tending to zero on `[-T,T]`, and `HT -> infinity`, of

\[
\limsup
\frac{
\log\|\mu_T\|_{TV}
}{HT}.
\tag{7}
\]

Then

\[
\boxed{1\le C_{sep}\le6.081.}
\tag{8}
\]

The lower bound is (2); the upper bound is the explicit off-center binomial family of `RE-216`, whose support lies in `[H,5H+o(1)]` and whose error tends to zero exponentially in its prediction order.

The arithmetic significance is sharp at leading exponent within the `RE-208` realization interface. If a regular discrete predictor of rate `C` satisfies the spacing and fixed-corridor hypotheses required there, then its variation exponent is `kappa=(C+o(1))Hc`, and `RE-208` realizes it whenever `kappa<1/2`. Hence a predictor with rate arbitrarily close to the spectral floor `C=1` would lift the explicit ordinary-prime construction all the way to every fixed

\[
c<\frac1{2H},
\tag{9}
\]

which is exactly the leading source-capacity ceiling isolated by `RE-214`--`RE-215`. Therefore the present fixed-constant factor `6.081` is not forced by the known prime-placement step: it is the gap between the universal spectral Wiener-norm floor `1` and the best explicit separated predictor currently constructed in the line.

## 1. The continuous Kaiser coercive test already bounds total variation

Put

\[
A:=HT.
\tag{10}
\]

`RE-215` constructs, for large `A`, a nonnegative probability density `W_{A,T}` supported on `[-T,T]` whose Fourier transform `phi_A(L)` satisfies

\[
\int_H^\infty
\left(
|\phi_A'(L)|+|\phi_A(L)|
\right)dL
\ll_H
A\log A\,e^{-A}.
\tag{11}
\]

The derivation there uses the endpoint-zero continuous Kaiser--Bessel profile. Nothing in the estimate requires the source measure paired against the test to be real.

Pair (1) against `W_{A,T}`. Since it is nonnegative and has mass one,

\[
\left|
1-
\int_{[H,\infty)}\phi_A(L)d\mu(L)
\right|
\le\epsilon,
\tag{12}
\]

so

\[
\left|
\int\phi_A\,d\mu
\right|
\ge1-\epsilon.
\tag{13}
\]

Define the complex weighted primitive

\[
G(L):=
\int_{[H,L]}e^u\,d\mu(u),
\qquad
R:=\sup_{L\ge H}e^{-L}|G(L)|.
\tag{14}
\]

The Stieltjes integration-by-parts estimate used in `RE-209`--`RE-215` remains valid after absolute values for complex `G`:

\[
\left|
\int\phi_A\,d\mu
\right|
\le
R
\int_H^\infty
\left(
|\phi_A'|+|\phi_A|
\right)dL.
\tag{15}
\]

Equations (11), (13), and (15) give

\[
R
\gg_H
(1-\epsilon)
\frac{e^A}{A\log A}.
\tag{16}
\]

But total variation dominates this primitive pointwise:

\[
\begin{aligned}
|G(L)|
&\le
\int_{[H,L]}e^u\,d|\mu|(u)\\
&\le
e^L\|\mu\|_{TV}.
\end{aligned}
\tag{17}
\]

Hence `R<=||mu||_TV`, and (2) follows immediately. For a discrete measure, total variation is exactly `sum_j |b_j|`, proving (4).

The loss `A log A` is irrelevant to the leading exponential constant. If `T_Q=c log Q`, then `A=Hc log Q`, and

\[
\log(A\log A)=o(\log Q),
\tag{18}
\]

which gives (5)--(6).

## 2. A subexponential number of shells cannot dilute the instability

For a discrete predictor with `J` distinct delays, (4) also implies

\[
\max_j|b_j|
\ge
\frac1J
\|\mu\|_{TV}.
\tag{19}
\]

Therefore if

\[
\log J=o(HT),
\tag{20}
\]

then at least one coefficient obeys

\[
\boxed{
\log\max_j|b_j|
\ge HT-o(HT).
}
\tag{21}
\]

In particular the `J=O(log Q)` predictor architectures used by `RE-205`--`RE-216` cannot trade exponential coefficient growth for a larger but still polylogarithmic number of shells. At `T_Q=c log Q`, some shell necessarily has coefficient magnitude at least `Q^{Hc-o(1)}`.

This is not a new source-capacity converse; `RE-214`--`RE-215` are stronger because they allow arbitrary finite remote support and work directly with the signed prime-count prefix. Equation (21) instead clarifies the **constructive interface**: any low-complexity spectral predictor handed to `RE-208` already contains an exponentially large shell amplitude before prime quantization begins.

## 3. The arithmetic realization is already compatible with the spectral lower floor

The reservoir-centroid theorem `RE-208` accepts regular discrete continuum predictors with `O(log Q)` coefficients, spacing `asymp 1/log Q`, a fixed logarithmic support corridor, and total reciprocal coefficient variation

\[
\|\mu_Q\|_{TV}
\le Q^{\kappa+o(1)}.
\tag{22}
\]

Its ordinary-prime construction works for every strict

\[
\kappa<\frac12.
\tag{23}
\]

The new lower bound says that no separated predictor can have `kappa<Hc` at logarithmic height. Therefore the best possible leading-order use of this interface would be

\[
Hc<\kappa<\frac12.
\tag{24}
\]

For every fixed `c<1/(2H)`, this interval is nonempty. Thus the half-mass arithmetic budget in `RE-208` does not itself force a constant-factor loss relative to the source-capacity ceiling. What is missing is a predictor whose variation exponent is close enough to the unavoidable floor `Hc` while retaining the regular support geometry needed by the prime realization.

The current explicit predictor from `RE-216` instead has

\[
\kappa\le(6.081+o(1))Hc,
\tag{25}
\]

which explains its range `6.081 Hc<1/2`. Equations (6), (23), and (25) locate the remaining leading-order gap without mixing spectral conditioning and arithmetic placement:

\[
\text{spectral floor }1
\quad\le\quad
C_{sep}
\quad\le\quad
6.081
\quad\text{(current explicit construction).}
\tag{26}
\]

## 4. Prior-art and representation audit

Causal prediction of band-limited signals is classical. Vaidyanathan's 1987 finite-order predictor uses Chebyshev polynomials and proves convergence above the Nyquist sampling rate; Mugler--Splettstoesser derive prediction from Newton-series difference methods; and more recent limited-memory work of Dokuchaev constructs bounded-support predictors by polynomial approximation of periodic exponentials. These results establish that one-sided prediction itself is not a novel mechanism. The relevant references found in the audit are:

- P. P. Vaidyanathan, *On predicting a band-limited signal based on past sample values*, Proceedings of the IEEE **75** (1987), 1125--1127, DOI `10.1109/PROC.1987.13856`.
- D. H. Mugler and W. Splettstoesser, *Difference Methods for the Prediction of Band-Limited Signals*, SIAM Journal on Applied Mathematics **46** (1986), DOI `10.1137/0146055`.
- N. Dokuchaev, *Limited memory predictors based on polynomial approximation of periodic exponentials*, Journal of Forecasting **41** (2022), 1037--1045, DOI `10.1002/for.2843`.

None is load-bearing for (2): the lower bound is derived entirely from the internal continuous-Kaiser estimate of `RE-215`. Their role is to delimit novelty. Qualitative convergence, `L2` prediction, or existence of a finite-order predictor does not control the total coefficient variation needed by the ordinary-prime realization. The Mathia-specific quantity is the uniform-arc Wiener cost and its coupling to bounded-multiplicity prime synthesis.

The bound is also representation-stable in the ways that matter here. Rescaling delays by `lambda` and frequencies by `1/lambda` leaves the product `HT` and the coefficient total variation unchanged. Splitting one atom into many atoms does not evade the theorem because (2) is stated for the total variation of the resulting measure after exact cancellations are combined. Moving support arbitrarily far to the right does not help either: no upper support bound entered (2).

A decisive negative control is `H=0`. Then the zero-delay atom `mu=delta_0` predicts the constant exactly with total variation one, so no exponential lower bound can hold. The instability is therefore tied to the **strict causal/separation gap**, not to exponential sums in general. Likewise, replacing total variation by an unrelated norm would change the statement; the Wiener/TV norm matters because it is precisely the coefficient currency consumed by the ordinary-prime population realization.

## 5. Adversarial checks and remaining problem

The main possible failure would be to confuse the signed-prefix lower bound of `RE-215` with total coefficient variation. Equation (17) removes that gap directly: the weighted prefix is always bounded by total variation, with no sign, spacing, cardinality, or real-coefficient assumption. Complex predictors therefore do not escape (2).

The second possible escape is to use very many tiny coefficients. This can reduce the largest individual coefficient only when `J` itself is exponentially large in `HT`; it cannot reduce the total-variation floor. Such an architecture is outside the current `RE-208` interface and would create a separate prime-carrier/discretization problem rather than refute the bound.

The third possible confusion is with the source-capacity threshold. Equation (2) alone does **not** prove that `C_sep=1`, and it does not construct a predictor approaching the floor. `RE-216` supplies only the upper bound `C_sep<=6.081`. The exact pure-approximation problem is now explicit:

\[
\boxed{
\text{Determine } C_{sep},
\qquad 1\le C_{sep}\le6.081,
}
\tag{27}
\]

preferably with a construction whose delays and shell count remain compatible with `RE-208`. Classical Chebyshev/Newton predictor formulas are natural candidates to audit, but their convergence alone is insufficient: the quantity that has to be extracted is their **uniform-error Wiener norm at prediction depth `HT`**.

## Research consequence

The leading fixed-constant gap in the separated vertical-Euler program can now be localized cleanly. The prime realization already tolerates every coefficient exponent below `1/2`, while continuum prediction itself forces coefficient exponent at least `Hc`. If the spectral extremal constant is one, the existing arithmetic interface is in principle capable of reaching every fixed height below the source-capacity boundary `c=1/(2H)`; if it is larger than one, that excess is a genuine prediction-theory obstruction rather than a prime-placement loss.

For the current explicit family, the only proven statement is

\[
1\le C_{sep}\le6.081.
\]

Closing this interval is therefore a more precise next target than further tuning of the `6.081` construction or further strengthening of the already unit-rate converse window.