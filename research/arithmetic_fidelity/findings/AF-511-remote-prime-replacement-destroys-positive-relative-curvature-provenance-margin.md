# AF-511 — Remote prime replacement destroys any positive relative-curvature provenance margin

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-OBSTRUCTION` · `DIRICHLET-SOURCE` · `REMOTE-ATOM` · `RELATIVE-PROFILE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P_{\mathbb P}(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_{\mathbb P}(s)=\frac{d^2}{ds^2}\log P_{\mathbb P}(s),
\qquad s>1,
\]

be the rational-prime Dirichlet sum and its log-curvature profile. For an odd prime `p_n\ge 7`, replace that one remote prime generator by the neighboring composite integer

\[
R_n=(\mathbb P\setminus\{p_n\})\cup\{p_n+1\}.
\tag{1}
\]

Then `R_n` is a simple unit-weight primitive positive-integer source, contains the same two smallest generators `2,3`, has the same AF-509 scale anchor

\[
m_{R_n}=m_{\mathbb P}=\log 2,
\tag{2}
\]

and is not the rational-prime source because `p_n` is missing while the composite `p_n+1` is present.

For every fixed `\sigma>1`, there is a constant `C_\sigma<\infty`, independent of `n`, such that for all sufficiently large `n`,

\[
\boxed{
\sup_{s\ge\sigma}
\frac{|\kappa_{R_n}(s)-\kappa_{\mathbb P}(s)|}
     {\kappa_{\mathbb P}(s)}
\le
C_\sigma\bigl(1+\log^2(p_n/2)\bigr)
\left(\frac{3}{p_n}\right)^\sigma .
}
\tag{3}
\]

Consequently

\[
\boxed{
\sup_{s\ge\sigma}
\left|\log\kappa_{R_n}(s)-\log\kappa_{\mathbb P}(s)\right|
\longrightarrow0.
}
\tag{4}
\]

Thus the exact curvature compression from AF-509 and the canonical inverse from AF-510 have **zero positive provenance margin** at the rational-prime source in the natural uniform relative-profile topology on every closed half-line `[\sigma,\infty)\subset(1,\infty)`.

Equivalently, within the same primitive integer source class that makes exact curvature equality rigid, there are non-prime-generator controls with the exact same scale anchor and curvature profiles arbitrarily close to the prime profile over the *entire observed half-line*. Exact source fidelity therefore does not upgrade to robust exact-prime provenance under any fixed nonzero relative tolerance merely by observing the full curvature profile.

## Derivation

### 1. One remote replacement is a multiplicative perturbation of the prime sum

Fix `\sigma>1`. Write

\[
P(s):=P_{\mathbb P}(s),
\qquad
\kappa(s):=\kappa_{\mathbb P}(s),
\qquad
a:=p_n,
\qquad b:=a+1.
\]

The perturbed source has Dirichlet sum

\[
P_n(s)
=P(s)-a^{-s}+b^{-s}
=P(s)(1+\eta_n(s)),
\tag{5}
\]

where

\[
\eta_n(s)=u_b(s)-u_a(s),
\qquad
u_x(s):=\frac{x^{-s}}{P(s)}.
\tag{6}
\]

Since `P(s)\ge2^{-s}`,

\[
|\eta_n(s)|
\le u_a(s)
\le\left(\frac2a\right)^s
\le\left(\frac2a\right)^\sigma.
\tag{7}
\]

Hence, for all sufficiently large `n`, `|\eta_n(s)|\le1/2` uniformly on `s\ge\sigma`. In particular `P_n(s)>0` there and

\[
\kappa_{R_n}(s)-\kappa(s)
=\frac{d^2}{ds^2}\log(1+\eta_n(s)).
\tag{8}
\]

### 2. Remote atom ratios and their first two derivatives are exponentially small

Define the exponentially tilted prime mean

\[
\mu(s):=-\frac{P'(s)}{P(s)}.
\tag{9}
\]

For every fixed `x>1`, direct differentiation gives

\[
\nu_x'(s)=\nu_x(s)(\mu(s)-\log x)
\tag{10}
\]

and, because `\mu'(s)=-\kappa(s)`,

\[
\nu_x''(s)
=\nu_x(s)\left((\mu(s)-\log x)^2-\kappa(s)\right).
\tag{11}
\]

On the closed half-line `s\ge\sigma`, the differentiated prime Dirichlet series converge uniformly after choosing any intermediate abscissa `1<\sigma_0<\sigma`. Therefore

\[
M_\sigma:=\sup_{s\ge\sigma}|\mu(s)-\log2|<\infty,
\qquad
K_\sigma:=\sup_{s\ge\sigma}\kappa(s)<\infty.
\tag{12}
\]

For `x=a` or `x=b=a+1`, equations `(7)`, `(10)`, and `(11)` therefore imply, after enlarging a constant depending only on `\sigma`,

\[
|\nu_x^{(j)}(s)|
\le
C_\sigma\bigl(1+\log^2(a/2)\bigr)
\left(\frac2a\right)^s,
\qquad
j=0,1,2,
\tag{13}
\]

uniformly for `s\ge\sigma`. The quadratic logarithmic factor is deliberately coarse; it simultaneously controls the first and second derivatives and absorbs the harmless ratio `(a+1)/a`.

Since `\eta_n=\nu_b-\nu_a`, the same bound holds for `\eta_n`, `\eta_n'`, and `\eta_n''`.

Now

\[
\frac{d^2}{ds^2}\log(1+\eta_n)
=
\frac{\eta_n''}{1+\eta_n}
-
\frac{(\eta_n')^2}{(1+\eta_n)^2}.
\tag{14}
\]

Using `|\eta_n|\le1/2` and `(13)` gives

\[
\boxed{
|\kappa_{R_n}(s)-\kappa(s)|
\le
A_\sigma\bigl(1+\log^2(a/2)\bigr)
\left(\frac2a\right)^s
}
\tag{15}
\]

for all `s\ge\sigma` and all sufficiently large `n`.

### 3. The fixed `2,3` pair supplies a uniform lower envelope for prime curvature

AF-509 identifies `\kappa` as the variance of `\log p` under the tilted weights

\[
w_p(s)=\frac{p^{-s}}{P(s)}.
\]

Hence

\[
\kappa(s)
=\frac12\sum_{p,q}w_p(s)w_q(s)(\log p-\log q)^2.
\tag{16}
\]

Retaining only the two ordered cross-terms from `p=2` and `q=3` yields

\[
\kappa(s)
\ge
w_2(s)w_3(s)\log^2\frac32.
\tag{17}
\]

Put

\[
Z_\sigma:=2^\sigma P(\sigma)
=\sum_{p\in\mathbb P}\left(\frac2p\right)^\sigma<\infty.
\tag{18}
\]

For `s\ge\sigma`, every ratio `2/p\le1`, so

\[
2^sP(s)=\sum_p(2/p)^s\le Z_\sigma.
\tag{19}
\]

Therefore

\[
w_2(s)\ge Z_\sigma^{-1},
\qquad
w_3(s)\ge Z_\sigma^{-1}\left(\frac23\right)^s,
\tag{20}
\]

and thus

\[
\boxed{
\kappa(s)
\ge
c_\sigma\left(\frac23\right)^s,
\qquad
c_\sigma:=Z_\sigma^{-2}\log^2\frac32>0.
}
\tag{21}
\]

This lower envelope is the quantitative reason a perturbation at a much larger generator cannot compete with the persistent `2,3` curvature carrier.

### 4. Division by the lower envelope gives a half-line relative bound

Combining `(15)` and `(21)` gives

\[
\frac{|\kappa_{R_n}(s)-\kappa(s)|}{\kappa(s)}
\le
B_\sigma\bigl(1+\log^2(a/2)\bigr)
\left(\frac3a\right)^s.
\tag{22}
\]

Because `a=p_n>3`, the right side decreases with `s`. Taking the supremum over `s\ge\sigma` proves `(3)`:

\[
\sup_{s\ge\sigma}
\frac{|\kappa_{R_n}(s)-\kappa(s)|}{\kappa(s)}
\le
B_\sigma\bigl(1+\log^2(p_n/2)\bigr)
\left(\frac3{p_n}\right)^\sigma
\longrightarrow0.
\tag{23}
\]

For large `n` the relative error in `(23)` is below `1/2`. The elementary inequality `|\log(1+x)|\le2|x|` for `|x|\le1/2` then gives `(4)`.

Thus even the scale-invariant profile metric

\[
d_\sigma(Q,R)
:=
\sup_{s\ge\sigma}
|\log\kappa_Q(s)-\log\kappa_R(s)|
\tag{24}
\]

places primitive integer controls distinct from `\mathbb P` arbitrarily close to the prime source.

### 5. The controls already satisfy the exact source-category anchors from AF-509

For every `n` with `p_n\ge7`, `R_n` contains both `2` and `3`; therefore

\[
\gcd(R_n)=1,
\qquad
\min R_n=2.
\tag{25}
\]

Because `p_n` is odd, `p_n+1>2` is even and composite. Hence `R_n` is not merely a dilation or relabeling of the rational primes: it deletes one rational-prime generator and inserts one composite integer generator.

The AF-509 scalar anchor remains exactly fixed:

\[
m_{R_n}=\log\min R_n=\log2=m_{\mathbb P}.
\tag{26}
\]

The second generator `3` is also unchanged, so the AF-510 leading right-tail fingerprint

\[
\kappa(s)\sim\log^2(3/2)(2/3)^s
\]

is shared to leading order. The obstruction is therefore not the one-dimensional dilation gauge already classified by AF-509. It is a **conditioning failure inside the gauge-fixed primitive-integer category itself**.

## Fidelity and matched-control audit

AF-509 proves an exact statement: among primitive simple integer sources, equality of the complete curvature profile forces equality of the source. AF-510 then gives an exact constructive inverse. The sequence `(R_n)` does not contradict either result, because no `R_n` has exactly the same curvature profile as `\mathbb P`.

What `(3)`--`(4)` establish is the missing quantitative boundary. Define the exact-prime provenance discriminator

\[
D(Q)=\mathbf 1_{\{Q=\mathbb P\}}
\]

on primitive simple integer sources with smallest atom `2`. Then `D(R_n)=0` for every `n`, while `D(\mathbb P)=1` and

\[
d_\sigma(R_n,\mathbb P)\to0.
\tag{27}
\]

So `D` is not continuous at the prime source in the retained curvature-profile topology, and there is no positive `d_\sigma`-ball around the prime profile containing only the rational-prime source.

This remains true after adjoining the AF-509 scale anchor, because `(26)` gives exact equality of that anchor for all controls. Therefore the enriched observation `(\kappa_Q,m_Q)` is exactly faithful but has zero robust provenance margin against this natural primitive-integer control family.

The control also avoids a weaker criticism of generalized-prime counterexamples. Each `R_n` is an ordinary positive-integer generator set, agrees with the rational primes on every fixed bounded range once `n` is large enough, and differs only by one remote prime-to-composite replacement. The loss of margin is therefore not caused by nonintegral dilation, arbitrary weights, or a change of the two leading generators.

## Prior art and novelty assessment

No novelty is claimed for the general phenomenon that inverse Laplace or exponential-sum recovery can be severely ill-conditioned.

- Chen Wei Dong, **“A Regularization Method for the Numerical Inversion of the Laplace Transform,”** *SIAM Journal on Numerical Analysis* 30(3), 759–773 (1993), DOI `10.1137/0730038`, explicitly treats numerical inverse Laplace transformation as an ill-posed problem and uses Tikhonov regularization.
- Pierre Maréchal, Faouzi Triki, and Walter C. Simo Tao Lee, **“Regularization of the inverse Laplace transform by mollification,”** *Inverse Problems* 40 (2024), 025010, DOI `10.1088/1361-6420/ad1609`, derive a global logarithmic stability estimate and emphasize the severe/exponential instability of inverse Laplace recovery.
- Gerlind Plonka and Manfred Tasche, **“Prony methods for recovery of structured functions,”** *GAMM-Mitteilungen* 37(2), 239–258 (2014), DOI `10.1002/gamm.201410011`, survey classical and generalized Prony recovery for exponential sums and related structured signals.
- Rami Katz, Nuha Diab, and Dmitry Batenkov, **“On the accuracy of Prony's method for recovery of exponential sums with closely spaced exponents,”** *Applied and Computational Harmonic Analysis* 73 (2024), 101687, DOI `10.1016/j.acha.2024.101687`, give quantitative noisy-recovery bounds in a super-resolution regime and provide direct neighboring prior art for stability, rather than mere exact identifiability, of exponential parameters.

Those sources establish the surrounding inverse-problem and exponential-recovery landscape; they do not by themselves supply the specific prime-curvature matched-control estimate `(3)`. The durable Arithmetic Fidelity delta is narrower and application-specific: after AF-509/AF-510 establish exact quotient fidelity, `(3)` gives an explicit primitive-integer, same-anchor control family proving that the rational-prime point has **zero uniform relative-curvature separation margin** on every fixed right half-line.

This should therefore be read as a concrete conditioning/no-go certificate for one declared provenance channel, not as a new general theorem about inverse Laplace transforms or Prony systems.

## Boundaries and failure modes

- **Exact equality remains rigid.** No control in `(1)` has exactly the prime curvature. AF-509 and AF-510 remain intact.
- **The half-line starts at fixed `\sigma>1`.** The constants need not remain bounded as `\sigma\downarrow1`, where the prime Dirichlet sum itself approaches its convergence boundary. No uniform statement including `s=1` is claimed.
- **The target is exact rational-prime provenance.** Replacing one remote prime by a composite changes the source identity, but this finding does not show that it changes every coarser arithmetic discriminator relevant to RH.
- **Finite Euler modifications are especially important here.** A finite change of Euler data need not alter the nontrivial-zero question in the same way as a global deformation. Therefore `(3)` is not an obstruction to every RH mechanism that uses curvature-like data; it is an obstruction to robustly recovering the exact rational-prime source from this channel under unrestricted remote primitive-integer edits.
- **The noise statement is metric-specific.** The no-margin result concerns uniform relative/multiplicative error on `[\sigma,\infty)`. A stronger observation norm that weights remote source contributions, accesses independent integral/congruence structure, or charges high-order derivatives differently may separate the controls.
- **No algorithmic lower bound beyond the channel metric is claimed.** Equation `(27)` is enough to rule out a positive separation margin for exact provenance, but it is not a minimax rate theorem for a specified stochastic noise model.
- **The replacement is intentionally remote.** The proof exploits the exponentially weak contribution of a large generator on a fixed right half-line. If the observation window moves left with `p_n` or includes source-dependent rescaling, the estimate must be redone.

## Consequences for the research line

AF-509 and AF-510 separate exact quotient fidelity from the dilation gauge. AF-511 now separates **exact fidelity from quantitative provenance stability** inside the already gauge-fixed primitive-integer category.

The immediate lesson is that “primitive integer support + one exact curvature profile” is enough for zero-noise source identification but not for any positive robustness margin against remote edits. The missing resource is not another integration constant. A robust rational-prime discriminator must either:

- observe a topology/norm that does not make remote generator edits asymptotically invisible;
- retain independent integral, additive, congruence, or incidence structure that detects the remote replacement at nonvanishing cost; or
- weaken the target from exact source identity to an RH-relevant discriminator proved invariant under the admissible remote edits.

This narrows the AF-510 quantitative frontier. The next useful stability question should state the target discriminator and observation norm *before* attempting an inverse estimate; otherwise exact recoverability can coexist with a zero decision margin, as `(27)` demonstrates.