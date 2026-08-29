# WI-008 — shortening the critical-sampled compression to buy higher moments loses the rank budget needed to improve 0.6725

**Status:** `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the single-compression route that keeps the Alpöge--Furman critical sampling rule `h=2π/L`, shortens the window to make a third or higher trace moment accessible by the unconditional Rudnick--Sarnak diagonal range, and then tries to improve the simple-critical proportion through rank/inertia or a finite-moment spectral certificate on that same matrix.

## 1. The apparent loophole

WI-001 records the arithmetic obstruction at the full Alpöge--Furman bandwidth

\[
L=\ell:=\log(T/2\pi),\qquad X=e^L\asymp T.
\]

At this scale the second moment is available unconditionally, but the ordinary Rudnick--Sarnak diagonal method does not supply the third and higher trace moments needed by a stronger finite-moment spectral certificate.

A natural workaround is to shorten the window. Alpöge--Furman already introduce

\[
L=\lambda\ell,\qquad 0<\lambda<1,
\qquad X=e^L=(T/2\pi)^\lambda.
\]

Since smaller `X` enlarges the range in which multiplicative relations among prime powers can be separated from the off-diagonal, perhaps one could sacrifice some bandwidth in exchange for an unconditional third or fourth moment and thereby beat the Montgomery--Taylor constant.

For the **critically sampled single compression**, this trade is self-defeating for a simple reason: the same `λ` that buys the higher moment also shrinks the matrix dimension, and the dimension ceiling is reached before the new moment becomes arithmetically available.

## 2. Critical sampling makes the matrix dimension `λN`

Alpöge--Furman choose the modulation grid

\[
\alpha_j=T+jh,
\qquad
h=\frac{2\pi}{L},
\]

and

\[
d=\left\lfloor\frac{LT}{2\pi}\right\rfloor.
\]

At the full scale `L=ell`, Riemann--von Mangoldt gives

\[
d=N(T,2T)+o(N).
\]

With `L=lambda ell` and the same critical-sampling rule,

\[
\boxed{
\frac dN=\lambda+o(1).
}
\tag{1}
\]

The simple-on-line part `P_1` of the compressed Weil matrix satisfies

\[
\operatorname{rank}P_1\le s_1,
\qquad
\operatorname{rank}P_1\le d.
\]

Therefore any certificate in this single-matrix architecture whose lower bound for `s_1` is obtained through rank/positive spectral mass of this compression has the hard asymptotic ceiling

\[
\boxed{
\frac{s_1^{\rm certified}}N\le \lambda+o(1).
}
\tag{2}
\]

This ceiling is independent of how many moments of the `d x d` matrix are known or how sharply their finite moment problem is solved.

## 3. The Rudnick--Sarnak range forces `k lambda < 2`

Alpöge--Furman §7.2(e) state the relevant unconditional higher-moment range explicitly. For the `k`-th trace moment, the prime-side diagonal evaluation based on multiplicative relations among `k` prime powers is available in the Rudnick--Sarnak support range

\[
X^k\le T^{2-\varepsilon}.
\tag{3}
\]

Substituting `X=(T/2pi)^lambda` gives, for fixed `k`,

\[
k\lambda<2
\tag{4}
\]

as the asymptotic admissibility condition (with a fixed margin corresponding to `epsilon`). Combining (2) and (4) yields the resource inequality

\[
\boxed{
\frac{s_1^{\rm certified}}N
<\frac{2}{k}+o(1)
}
\tag{5}
\]

for any attempt to purchase the `k`-th moment by shortening **this same critically sampled compression**.

For the first genuinely new moment, `k=3`, one must take

\[
\lambda<\frac23,
\]

so the matrix itself can certify at most a proportion strictly below `2/3`. But the already verified Montgomery--Taylor theorem gives

\[
0.672500703679\ldots>\frac23.
\]

Thus the third moment becomes unconditionally diagonal-accessible only after the compression has lost enough rank capacity that it cannot even recover the current record.

The trade worsens at higher order:

| new moment order `k` | Rudnick--Sarnak requirement | critical-sampled rank ceiling |
| ---: | ---: | ---: |
| 3 | `lambda < 2/3` | `< 2/3` |
| 4 | `lambda < 1/2` | `< 1/2` |
| 5 | `lambda < 2/5` | `< 2/5` |
| 6 | `lambda < 1/3` | `< 1/3` |

So no third-or-higher moment obtained merely by shortening the critical-sampled window can improve `0.672500703679...`.

## 4. Why this does not contradict the existing second moment

The endpoint second moment is special. Alpöge--Furman obtain it at

\[
X\asymp T,
\]

using the Montgomery--Vaughan bilinear inequality together with the unconditional pair-correlation inputs of Aryan and Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh. That endpoint estimate is exactly the input behind the `2-R(psi)` theorem.

The obstruction above concerns **new moments `k>=3` through the ordinary Rudnick--Sarnak diagonal range**. It does not re-derive or weaken the special endpoint `k=2` argument.

Alpöge--Furman themselves summarize the same arithmetic fact by saying that at `X asymp T` unconditionally available higher moments add nothing. The additional point isolated here is the quantitative reason the obvious shorter-window workaround also fails: at critical sampling the support budget and the rank budget are the same parameter `lambda`.

## 5. The obstruction is deliberately scoped: two escape routes remain live

This finding does **not** prove that unconditional higher moments are useless in every architecture.

First, one could keep the full-bandwidth `lambda=1` matrix as the main rank carrier and use one or more shorter compressions only as **auxiliary constraints on the same zero configuration**. Then the final certificate need not be bounded by the dimension of the shorter auxiliary matrix. This is a genuinely joint/multi-profile problem, not the single-compression trade ruled out above. The unaudited Devine `0.673399` claim is relevant precisely because it advertises several admissible profiles and pair interactions rather than one shortened replacement matrix.

Second, one could try to **decouple sampling density from window bandwidth**. The equation `d/N -> lambda` used above comes from the critical choice `h=2pi/L`; a denser modulation grid would make `d` larger while keeping `X=T^lambda`. Such an oversampled Gabor family is redundant, so its effective spectral/rank information must be audited rather than inferred from the raw matrix dimension. This finding makes no claim that oversampling succeeds or fails. It identifies it as a precise place where a genuinely different idea would have to enter.

Conditional prime-pair information is the other known escape: if moments `k>=3` become available at `lambda=1`, the dimension ceiling returns to `N`, and Alpöge--Furman's conditional Christoffel calculation shows that the fourth-moment data can already raise the bound to `13/18`.

## 6. Prior art and novelty assessment

No novelty is claimed for any ingredient:

- the sample dimension `d=floor(LT/(2pi))` and the parameter `L=lambda ell` are in Alpöge--Furman;
- the range `X^k <= T^{2-epsilon}` is their §7.2 summary of the Rudnick--Sarnak diagonal support restriction;
- the fact that rank cannot exceed matrix dimension is elementary.

A bounded novelty search found no separate source formulating the combined inequality (5) as a support--moment--rank tradeoff. That absence is not evidence of novelty. The durable contribution is the **scope classification** relevant to this research line: a tempting attempt to evade the full-bandwidth higher-moment wall by shrinking `X` cannot improve the current theorem if one keeps the same critical-sampled single-compression architecture.

## 7. Research consequence

Do not spend further effort on the recipe

\[
\text{shorten }L
\to
\text{obtain }\operatorname{tr}G^k\text{ diagonally}
\to
\text{apply a stronger moment/rank certificate to that same }G.
\]

For every genuinely new `k>=3`, arithmetic accessibility forces the rank ceiling below the already proved Montgomery--Taylor proportion.

The higher-value questions are now more specific:

1. can a full-bandwidth rank carrier and shorter-bandwidth moment probes be coupled in one rigorous certificate without collapsing to the bandwidth-one adversarial law of WI-001?
2. can oversampling preserve order-`N` usable spectral dimension while keeping prime cutoff `X<T^{2/k}` for a higher moment, or does Gabor redundancy reintroduce an effective `lambda N` ceiling?
3. can any unconditional arithmetic estimate extend a higher moment beyond the Rudnick--Sarnak diagonal range without requiring the full Hardy--Littlewood/pair-correlation input?

The compact obstruction is

\[
\boxed{
\text{critical sampling:}\qquad
k\lambda<2,
\quad
\frac{\text{certifiable rank}}N\le\lambda
\quad\Longrightarrow\quad
\frac{N_{0}^{s,\rm cert}}N<\frac2k.
}
\]

For `k>=3`, buying the new moment by bandwidth reduction costs more certifiable rank than the moment can possibly recover.