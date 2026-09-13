# MC-277 — The Christoffel scalar retains blindness exactly but with a vanishing endpoint margin

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the Christoffel endpoint detector and witness analysis of `MC-268`–`MC-276`. On the Boolean cube write

\[
x=(x_1,\ldots,x_k)\in\{-1,+1\}^k,
\qquad
x_*=(1,\ldots,1),
\]

and define

\[
g_m(x):=\sum_{|S|\le m}x_S,
\qquad
Z:=Z_m(k):=\sum_{s=0}^m\binom ks,
\qquad
P_m(x):=\frac{g_m(x)}{Z}.
\tag{1}
\]

The point `x_*` is the blind vector. `MC-273` showed that every nonblind vector admits a negative witness and then

\[
|g_m(x)|\le H:=\binom{k-1}{m},
\tag{2}
\]

with equality on the positive side when the vector has exactly one negative coordinate. Since

\[
P_m(x_*)=1,
\tag{3}
\]

put

\[
h:=\frac HZ,
\qquad
\delta_{k,m}:=1-h.
\tag{4}
\]

Then the Christoffel scalar itself retains the blind/nonblind bit **exactly**:

\[
\boxed{
 x=x_*
 \iff
 P_m(x)>h.
}
\tag{5}
\]

Indeed every nonblind vector lies in the scalar interval `[-h,h]`, while the blind vector is the isolated value `1`. Moreover the nearest nonblind scalar value is attained, not merely bounded: every vector with exactly one negative coordinate has

\[
P_m(x)=h.
\tag{6}
\]

Therefore the exact scalar separation margin is

\[
\boxed{
\delta_{k,m}
=1-\frac{\binom{k-1}{m}}{\sum_{s=0}^m\binom ks}
=\frac{2\sum_{s=0}^{m-1}\binom{k-1}{s}}
       {\sum_{s=0}^m\binom ks}.
}
\tag{7}
\]

When `m=o(k)`,

\[
\boxed{
\delta_{k,m}
=\frac{2m}{k}
+O\!\left(\frac{m^2}{k^2}\right).
}
\tag{8}
\]

This gives an exact conditioning statement. Suppose only a perturbed scalar

\[
\widetilde P=P_m(x)+e,
\qquad |e|\le\eta,
\tag{9}
\]

is available. A deterministic decoder can classify **every** Boolean input correctly from `\widetilde P` if and only if

\[
\boxed{
\eta<\frac{\delta_{k,m}}2.
}
\tag{10}
\]

For the upper direction, the midpoint threshold

\[
\theta=\frac{1+h}{2}
\tag{11}
\]

separates the perturbed blind interval from every perturbed nonblind interval whenever `(10)` holds. For the lower direction, the blind input and any one-negative input have exact scalar values `1` and `h`; if `\eta\ge\delta_{k,m}/2`, their uncertainty intervals overlap, so the same observed scalar can come from opposite classes.

The same margin gives the exact best Lipschitz conditioning of a scalar decoder. Among all functions `D:[-1,1]\to\mathbb R` satisfying

\[
D(1)=1,
\qquad
D(P_m(x))=0\quad(x\ne x_*),
\tag{12}
\]

the minimum possible Lipschitz constant is

\[
\boxed{
\inf_D \operatorname{Lip}(D)
=\frac1{\delta_{k,m}}.
}
\tag{13}
\]

The lower bound follows from the attained pair `(1,h)`. It is attained by the piecewise-linear ramp

\[
D_*(u)
=
\begin{cases}
0,&u\le h,\\[2mm]
\dfrac{u-h}{1-h},&h\le u\le1.
\end{cases}
\tag{14}
\]

Thus the current low-depth Christoffel scalar does **not** erase blindness. It compresses blindness into a scalar gap whose condition number grows like `k/(2m)`.

At the live support-matched scale

\[
m=t+1,
\qquad
t=\left(\frac1{\log2}+o(1)\right)\log\log y,
\qquad
k\sim\frac y{\log y},
\tag{15}
\]

we obtain

\[
\boxed{
\frac{\delta_{k,m}}2
=
\left(\frac1{\log2}+o(1)\right)
\frac{\log y\,\log\log y}{y},
}
\tag{16}
\]

and

\[
\boxed{
\inf_D\operatorname{Lip}(D)
=
\left(\frac{\log2}{2}+o(1)\right)
\frac{y}{\log y\,\log\log y}.
}
\tag{17}
\]

This scale is radically different from the one-row mass of the target shell. With

\[
C=\binom{N_y}{t},
\]

`MC-263` and `MC-274` give

\[
C^{-1}
=\exp\!\left[-\left(\frac1{\log2}+o(1)\right)
\log y\,\log\log y\right],
\tag{18}
\]

whereas the rowwise scalar robustness radius in `(16)` is only of order `y^{-1}` up to logarithms. Therefore the severe atom-scale requirements exposed by positive or distributional aggregation are **not caused by loss of the blind discriminator in the degree-`m` row representation**. They arise when the `C` row identities are aggregated and one asks a scalar sum, norm, or loss to certify that no exceptional row exists.

This does not exclude a blind relation and does not give a new estimate for `M(X)`. It identifies the present bottleneck more sharply: low source depth already carries the rowwise blind bit, but only through a shrinking margin, so a useful arithmetic theorem must control the exact row scalar at that margin or preserve enough target-row phase through aggregation. Merely replacing the hard threshold by a stable low-complexity average returns to the obstructions already isolated in `MC-270`, `MC-275`, and `MC-276`.

## 1. The separation is an exact consequence of the negative-witness collapse

At the blind point every Walsh character in `(1)` is `+1`, so `(3)` is immediate. If `x` is nonblind, choose a negative coordinate. `MC-273` cancels its factor against the cumulative-degree denominator and gives

\[
g_m(x)
=e_m(x_{\widehat i}),
\tag{19}
\]

where the right side is a sum of exactly `\binom{k-1}{m}` signs. Hence `(2)` follows. If the chosen negative coordinate is the unique negative coordinate, all remaining signs are positive and every term in `(19)` is `+1`, proving attainment `(6)`.

Consequently no nonblind input can enter the interval `(h,1]`, while the blind point lies at its upper endpoint. This proves `(5)` without any probabilistic model or arithmetic hypothesis.

Pascal's identity, in the form already derived in `MC-273`, gives

\[
Z-H
=2\sum_{s=0}^{m-1}\binom{k-1}{s},
\tag{20}
\]

which is `(7)`. For `m=o(k)`, the top term dominates the lower partial sum and

\[
\sum_{s=0}^{m-1}\binom{k-1}{s}
=
\binom{k-1}{m-1}
\left(1+O\!\left(\frac mk\right)\right),
\tag{21}
\]

while

\[
\frac{\binom{k-1}{m-1}}{\binom{k-1}{m}}
=\frac{m}{k-m}.
\tag{22}
\]

Substituting into `(7)` proves `(8)`.

## 2. The additive-noise radius and Lipschitz constant are minimax exact

For any `\eta>=0`, the possible observed values from the blind point fill

\[
I_{\rm blind}=[1-\eta,1+\eta],
\tag{23}
\]

while the one-negative nonblind vectors already fill the uncertainty interval

\[
I_1=[h-\eta,h+\eta].
\tag{24}
\]

Every other nonblind exact scalar is at most `h`. Hence all perturbed nonblind observations lie below `h+\eta`.

If `2\eta<1-h`, then

\[
h+\eta<\frac{1+h}{2}<1-\eta,
\tag{25}
\]

so the midpoint threshold classifies every input. If `2\eta\ge1-h`, `(23)` and `(24)` intersect. Choosing errors of opposite sign produces the same observation from a blind and a one-negative input, proving impossibility for any decoder based only on the perturbed scalar. This establishes `(10)` exactly, including the sharp boundary.

For Lipschitz decoding, `(6)` and `(12)` force

\[
1
=|D(1)-D(h)|
\le
\operatorname{Lip}(D)(1-h),
\tag{26}
\]

so `\operatorname{Lip}(D)>=1/\delta_{k,m}`. The ramp `(14)` has precisely this slope and is already zero on the entire nonblind range `[-h,h]`, proving `(13)`.

An approximate decoder with error at most `\varepsilon<1/2` on the two classes similarly satisfies

\[
\operatorname{Lip}(D)
\ge
\frac{1-2\varepsilon}{\delta_{k,m}}.
\tag{27}
\]

Thus the conditioning cost is intrinsic to this scalar representation and is not an artifact of a particular threshold rule.

## 3. Why this does not contradict the OR approximate-degree barrier

`MC-275` proved that a polynomial whose **values themselves** uniformly approximate the nonblind indicator on the full cube has the classical OR approximate-degree cost, and exact polynomial normalization reaches degree `k`.

Equation `(5)` is a different statement. `P_m` is not a low-degree polynomial approximation to the blind indicator; it is a low-degree **polynomial threshold representation** with a shrinking margin. The final map `(14)` is piecewise linear and nonpolynomial. Replacing that hard/hinge decoder by a uniformly accurate low-degree polynomial returns to the approximate-degree lower bound of `MC-275`.

This distinction is classical in Boolean-function analysis: threshold representation and uniform polynomial approximation measure different resources. Polynomial threshold functions and their spectral representation are longstanding objects; see, for example, J. Bruck and R. Smolensky, *Polynomial Threshold Functions, AC^0 Functions, and Spectral Norms*, SIAM Journal on Computing 21 (1992), DOI `10.1137/0221003`. Ryan O'Donnell, *Analysis of Boolean Functions* (Cambridge University Press, 2014; corrected arXiv edition `2105.10386`) is a standard modern reference for Fourier/Walsh representations, Boolean thresholds, and noise/sensitivity language.

The Krawtchouk generating-function identity underlying the exact value bound is classical; NIST DLMF §18.23 records the standard Krawtchouk generating-function family. No novelty is claimed for polynomial-threshold terminology, Lipschitz margin arguments, Krawtchouk algebra, or the elementary perturbation bound.

The durable Mathia contribution claimed here is only the exact **frontier synthesis** for the forced Christoffel scalar: after the L2 normalization collapse of `MC-276`, the representation itself can now be separated from the aggregation loss. The degree-`m` scalar preserves the blind discriminator with exact margin `(7)`, and the corresponding decoder has the sharp conditioning `(10)`–`(17)`.

## Boundaries and falsification tests

- **No proof of nonblindness.** Showing `P_m(T)<=h` uniformly on the actual arithmetic target family without already knowing a negative witness is itself equivalent to excluding blind rows. Equation `(5)` is a compressed criterion, not a proof of it.
- **No claim of arithmetic specificity.** The separation theorem holds on the full Boolean cube. The separated-prime universality control of `MC-252` therefore satisfies the same scalar geometry.
- **No aggregate theorem.** The rowwise robustness radius `(16)` does not imply that the sum `L_{m,y}(t)`, the energy `E_{m,y}(t)`, or another aggregate can resolve one exceptional row among `C` targets.
- **No polynomial-decoder escape.** Uniformly replacing the threshold/ramp by low-degree polynomial approximation remains subject to `MC-275`.
- **No claim that `P_m` is margin-optimal among all degree-`m` polynomials.** The theorem computes the exact margin and conditioning of the specific Christoffel scalar forced by the current endpoint-energy route; a different bounded polynomial may have a different threshold margin.
- **No numerical or random-sign inference.** Every displayed separation and conditioning statement is deterministic and finite.

A direct falsification would be a nonblind Boolean vector with `P_m>H/Z`, or a scalar decoder robust to adversarial additive error `eta>=delta/2` on both the blind point and the attained one-negative class. Both are excluded by `(2)` and the overlapping uncertainty intervals.

## Consequence for the research line

`MC-276` showed that distributional L2 approximation can look excellent precisely because its loss subtracts the blind atom. The present result shows that this should **not** be interpreted as loss of the blind bit inside the low-depth Christoffel representation itself. The bit is still there, separated exactly by `(5)`.

The sharper diagnosis is a representation/conditioning/aggregation split:

- degree `m` is enough to encode the rowwise blind discriminator;
- the encoding margin is only `delta~2m/k`, so stable decoding costs condition number `~k/(2m)`;
- aggregating over `C` target rows creates the vastly harder one-exception problem seen in the positive-energy and distributional-loss routes.

Accordingly, the next useful theorem should not merely search for a richer row representation. It should either obtain arithmetic control of the existing scalar at its natural margin scale before row identities are discarded, or prove genuinely signed cancellation across target rows while retaining enough information that a blind contribution cannot be masked. This is the same phase-sensitive frontier isolated in `MC-276`, now with the rowwise information loss separated quantitatively from the conditioning and aggregation losses.