# AF-151 — Local envelope conflict exactly classifies Shtarkov-center drift

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `POSITIVE-STABILITY-CRITERION`, `NO-NOVELTY-CLAIM`

## Claim

AF-150 bounded the drift between the Shtarkov center propagated from the source experiment and the Shtarkov center recomputed after compression by the global drop in maximal leakage. That scalar drop is only the mean of a more informative local object. The entire reset mismatch is exactly a change of measure by the **local max-sum conflict factor**, and every standard divergence between the two centers is therefore a moment or convex functional of that factor.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite experiment on a finite sample space `X`, let `K:X\to Y` be a stochastic channel, and define

\[
s(x):=\max_i P_i(x),
\qquad
C_X:=\sum_x s(x).
\tag{1}
\]

For the compressed family `Q_i=P_iK`, put

\[
t(y):=\max_i Q_i(y)
      =\max_i\sum_xP_i(x)K(y\mid x),
\qquad
C_Y:=\sum_y t(y),
\tag{2}
\]

and push the source envelope itself through the channel:

\[
\widetilde t(y):=\sum_x s(x)K(y\mid x)
=\sum_x\max_iP_i(x)K(y\mid x).
\tag{3}
\]

On every output point with positive mass, define

\[
\boxed{
\kappa(y):=\frac{\widetilde t(y)}{t(y)}\ge1.
}
\tag{4}
\]

The ratio is always well-defined on the common support: if `\widetilde t(y)>0`, some source point contributing to `y` has positive envelope mass, hence one experiment member gives `Q_i(y)>0` and therefore `t(y)>0`. Also

\[
1\le\kappa(y)\le m,
\tag{5}
\]

because

\[
\widetilde t(y)
\le\sum_iQ_i(y)
\le m\max_iQ_i(y).
\]

The factor `\kappa(y)` is exactly the failure of `max_i` to commute with channel averaging at output `y`. In particular, `\kappa(y)=1` iff one experiment label can attain the source envelope simultaneously at every source point feeding `y` with positive channel weight. Values larger than one measure local conflict among source-envelope maximizers that are merged by the compression.

Let

\[
q:=M_X^*K=\frac{\widetilde t}{C_X}
\tag{6}
\]

be the propagated source Shtarkov center and

\[
r:=M_Y^*=\frac{t}{C_Y}
\tag{7}
\]

be the recomputed output center. Then

\[
\boxed{
\mathbb E_r\kappa
=\frac{C_X}{C_Y}
=:\mu,
}
\tag{8}
\]

so the maximal-leakage drop from AF-150 is exactly

\[
\boxed{
\Delta_\infty
=\log\frac{C_X}{C_Y}
=\log\mathbb E_r\kappa.
}
\tag{9}
\]

More strongly, the two centers satisfy the exact Radon--Nikodym identity

\[
\boxed{
\frac{dq}{dr}(y)
=\frac{\kappa(y)}{\mathbb E_r\kappa}.
}
\tag{10}
\]

Thus the propagated center is precisely the `\kappa`-size-biased tilt of the recomputed center. Equivalently, with local coherence `\beta=1/\kappa` and `\alpha=C_Y/C_X`,

\[
\frac{dr}{dq}=\frac{\beta}{\mathbb E_q\beta},
\qquad
\mathbb E_q\beta=\alpha.
\tag{11}
\]

Consequently:

1. **Exact center commutation is local-conflict homogeneity.**
   \[
   \boxed{
   q=r
   \iff
   \kappa(y)=\mu\quad r\text{-a.s.}
   }
   \tag{12}
   \]
   A channel may therefore lose maximal leakage while its Shtarkov center still commutes exactly with compression: the loss need only have the same multiplicative max-sum conflict at every surviving output.

2. **Total-variation drift is normalized mean absolute conflict deviation.**
   \[
   \boxed{
   \|q-r\|_{\rm TV}
   =\frac{1}{2\mu}\,\mathbb E_r|\kappa-\mu|.
   }
   \tag{13}
   \]

3. **Pearson drift in the propagated-to-reset direction is exactly squared coefficient of variation.**
   \[
   \boxed{
   \chi^2(q\|r)
   =\frac{\operatorname{Var}_r(\kappa)}{(\mathbb E_r\kappa)^2}.
   }
   \tag{14}
   \]
   Hence `q_n` and `r_n` are chi-square close iff the local conflict profile has vanishing relative variance.

4. **Every `f`-divergence in this direction is an exact conflict functional.** For convex `f` with `f(1)=0`,
   \[
   \boxed{
   D_f(q\|r)
   =\mathbb E_r\left[
     f\left(\frac{\kappa}{\mathbb E_r\kappa}\right)
   \right].
   }
   \tag{15}
   \]
   In particular,
   \[
   D_{\rm KL}(q\|r)
   =\mathbb E_r\left[
   \frac{\kappa}{\mu}\log\frac{\kappa}{\mu}
   \right],
   \tag{16}
   \]
   \[
   D_{\rm KL}(r\|q)
   =\mathbb E_r\log\frac{\mu}{\kappa},
   \tag{17}
   \]
   and
   \[
   D_\infty(q\|r)
   =\log\frac{\operatorname*{ess\,sup}_r\kappa}{\mu},
   \qquad
   D_\infty(r\|q)
   =\log\frac{\mu}{\operatorname*{ess\,inf}_r\kappa}.
   \tag{18}
   \]

The conclusion sharpens AF-150's frontier. A scalar maximal-leakage budget controls only `\mathbb E_r\kappa`; **stable recanonicalization in a declared metric requires the corresponding local-conflict profile to be calibrated in the stronger way that metric sees**. Mean loss, provenance of the propagated source center, and reset stability are therefore not three names for the same quantity.

## Derivation

The max-sum inequality gives

\[
t(y)
=\max_i\sum_xP_i(x)K(y\mid x)
\le
\sum_x\max_iP_i(x)K(y\mid x)
=\widetilde t(y),
\tag{19}
\]

so `\kappa\ge1`. The upper bound in `(5)` follows from

\[
\widetilde t(y)
\le\sum_x\sum_iP_i(x)K(y\mid x)
=\sum_iQ_i(y)
\le m t(y).
\tag{20}
\]

For the equality case `\kappa(y)=1`, choose an index `i_*` attaining `t(y)=Q_{i_*}(y)`. Since every summand satisfies

\[
P_{i_*}(x)K(y\mid x)
\le s(x)K(y\mid x),
\]

and equality holds after summing exactly when `t(y)=\widetilde t(y)`, all terms with positive `K(y|x)` must attain equality. Hence `P_{i_*}(x)=s(x)` at every source point that actually contributes to that output. The converse is immediate.

Now use the recomputed center `r=t/C_Y`:

\[
\begin{aligned}
\mathbb E_r\kappa
&=\sum_y\frac{t(y)}{C_Y}\frac{\widetilde t(y)}{t(y)}\\
&=\frac1{C_Y}\sum_y\widetilde t(y)\\
&=\frac1{C_Y}\sum_xs(x)\sum_yK(y\mid x)\\
&=\frac{C_X}{C_Y},
\end{aligned}
\tag{21}
\]

which proves `(8)--(9)`. Meanwhile

\[
\frac{q(y)}{r(y)}
=\frac{\widetilde t(y)/C_X}{t(y)/C_Y}
=\frac{\kappa(y)}{C_X/C_Y}
=\frac{\kappa(y)}{\mathbb E_r\kappa},
\tag{22}
\]

proving `(10)`. Equation `(12)` is then exactly the criterion `dq/dr=1`.

Total variation follows directly:

\[
\begin{aligned}
\|q-r\|_{\rm TV}
&=\frac12\mathbb E_r\left|\frac{dq}{dr}-1\right|\\
&=\frac1{2\mu}\mathbb E_r|\kappa-\mu|.
\end{aligned}
\tag{23}
\]

Likewise

\[
\chi^2(q\|r)
=\mathbb E_r\left(\frac{\kappa}{\mu}-1\right)^2
=\frac{\operatorname{Var}_r(\kappa)}{\mu^2},
\tag{24}
\]

and `(15)--(18)` are the corresponding definitions evaluated with the same likelihood ratio.

The AF-150 one-sided bounds are recovered by switching to `\beta=1/\kappa`. Since `dr/dq=\beta/\alpha`, `0<\beta\le1`, and `\mathbb E_q\beta=\alpha`, for example

\[
\chi^2(r\|q)
=\frac{\operatorname{Var}_q(\beta)}{\alpha^2}
\le\frac{\alpha(1-\alpha)}{\alpha^2}
=\frac1\alpha-1.
\tag{25}
\]

Thus AF-150's scalar inequalities are moment bounds obtained after discarding the local profile.

## Separating controls

### Private-label collapse makes the local mechanism explicit

For AF-146's family

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\qquad i=1,\ldots,m,
\tag{26}
\]

and the channel that fixes `0` while merging all private labels to `*`, one gets

\[
\kappa(0)=1,
\qquad
\kappa(*)=m,
\tag{27}
\]

under

\[
r=(1-\rho)\delta_0+\rho\delta_*.
\tag{28}
\]

Hence

\[
\mu=\mathbb E_r\kappa
=1+(m-1)\rho
=C_X/C_Y.
\tag{29}
\]

At the AF-150 scale `\rho=1/m`, the mean conflict tends to `2`, but the rare high-conflict output produces

\[
\chi^2(q\|r)
=\frac{(m-1)^3}{(2m-1)^2}
\sim\frac m4,
\tag{30}
\]

and

\[
D_\infty(q\|r)
=\log\frac{m}{2-1/m}
\sim\log(m/2),
\tag{31}
\]

while AF-150 found the reverse-direction `D_\infty(r\|q)\to\log2`. The asymmetry is not accidental: the source-propagated center retains substantial mass on an output event that the recomputed center regards as rare.

### Vanishing maximal-leakage drop still need not give strong reset stability

The sharper separating scale is

\[
\rho=\frac1{m^2}.
\tag{32}
\]

Then

\[
\mu
=1+\frac{m-1}{m^2}
\longrightarrow1,
\qquad
\Delta_\infty=\log\mu\longrightarrow0.
\tag{33}
\]

So the global maximal-leakage drop vanishes and, by AF-150 or `(13)`, the two centers also approach each other in total variation. Nevertheless

\[
\operatorname{Var}_r(\kappa)
=(1-\rho)(1-\mu)^2+\rho(m-\mu)^2
\longrightarrow1,
\tag{34}
\]

and therefore

\[
\boxed{
\chi^2(q\|r)\longrightarrow1,
\qquad
D_\infty(q\|r)\sim\log m.
}
\tag{35}
\]

Thus even a vanishing global leakage drop does not make reset stable in every stronger likelihood-ratio geometry. The missing hypothesis is precisely tail/dispersion control on local envelope conflict. More generally, for `\rho=m^{-a}` with `a>1`, the mean conflict tends to one, whereas the leading second-moment contribution is `\rho m^2=m^{2-a}`. The chi-square reset threshold is therefore at `a=2`, not at the first-moment leakage threshold `a=1`.

This is the concrete calibration lesson: **different downstream certificates require different moments or tails of the same local conflict profile.** A source theorem that only makes maximal-leakage drop small may be enough for total variation but still be too weak for a chi-square, reverse-kernel, or worst-case likelihood-ratio argument.

## Prior art and novelty assessment

The global objects in this finding remain classical. Shtarkov's normalized maximum-likelihood law is the minimax order-infinity center; Sibson information radius and maximal leakage identify `\log C_X`; and data processing for that quantity is established prior art, as already recorded in AF-149--AF-150.

The closest literature located for treating leakage as an **outcome-wise profile rather than only a scalar average/capacity** is:

- Sara Saeidian, Giulia Cervia, Tobias J. Oechtering, and Mikael Skoglund, **“Pointwise Maximal Leakage,”** *IEEE Transactions on Information Theory* 69(12), 8054–8080 (2023), DOI `10.1109/TIT.2023.3304378`, arXiv:`2205.04935`. They define pointwise maximal leakage for a fixed joint law, interpret leakage as a random variable over released outcomes, and study post-processing and composition.
- Ibrahim Issa, Aaron B. Wagner, and Sudeep Kamath, **“An Operational Approach to Information Leakage,”** *IEEE Transactions on Information Theory* 66(3), 1625–1657 (2020), DOI `10.1109/TIT.2019.2962804`, arXiv:`1807.07878`. They identify maximal leakage with Sibson mutual information of order infinity and explicitly connect the closed-form sum of pointwise channel maxima to the Shtarkov sum.
- Barış Nakiboğlu, **“The Rényi Capacity and Center,”** *IEEE Transactions on Information Theory* 65(2), 841–860 (2019), DOI `10.1109/TIT.2018.2861002`. This is the established Rényi-capacity/radius/center framework in which the Shtarkov law is the finite order-infinity center.

Pointwise maximal leakage is adjacent but not identical to `\kappa`. Its pointwise quantity is defined relative to a **fixed prior and the resulting output marginal**. Here `\kappa` is the noncommutation ratio between `sum_x max_i` and `max_i sum_x`, and `(10)` compares a source-selected minimax center pushed through `K` with a newly optimized minimax center after `K`. The propagated Shtarkov center need not be the output marginal generated by any fixed prior over experiment labels. A targeted search across Shtarkov/NML, Rényi-center, maximal-leakage, and pointwise-maximal-leakage literature did not locate the exact size-biased identity `(10)` or the private-label moment separation `(32)--(35)`. The algebra is elementary, so **no novelty claim is made**; the value is the exact local diagnostic it supplies to the Arithmetic Fidelity program.

## Boundary conditions and falsification tests

1. **Finite experiment and finite output are load-bearing here.** The Shtarkov center exists automatically and `1\le\kappa\le m`. Continuous/infinite model classes require existence and integrability conditions before `(8)--(18)` can be transferred.

2. **`\kappa` is label-family relative.** Adding redundant or near-duplicate controls can alter the pointwise envelope and therefore the conflict profile. An arithmetic use must derive the control family intrinsically rather than tune it after seeing the desired certificate.

3. **A small mean is not a universal stability certificate.** Equation `(35)` is the decisive counterexample. Global maximal-leakage drop controls the first moment of conflict and one direction of reset divergence, not all moments, tails, or reverse likelihood ratios.

4. **A constant conflict factor can hide substantial information loss.** Equation `(12)` says exact center commutation only detects spatial variation of the max-sum conflict, not its absolute size. Therefore `q=r` does not imply `C_X=C_Y`, sufficiency, or recoverability of the experiment.

5. **The local factor is a diagnostic, not a recovery map.** Small dispersion of `\kappa` proves stability of the canonical centers in the chosen divergence. It does not by itself produce a reverse channel for the experiment; AF-144--AF-145 still require a propagated reference and an actual small data-processing loss for the experiment members.

6. **Metric choice is part of the theorem.** Total variation, chi-square, KL, and order-infinity stability read different convex/tail functionals of the same normalized `\kappa`. A downstream argument must declare which geometry it needs instead of calling all small reset errors equivalent.

7. **The equality characterization is representation-sensitive only through the declared experiment/channel.** Harmless relabelings preserve `s,t,\widetilde t` up to the same relabeling, hence preserve `\kappa`; arbitrary enlargement of the model/control class is a genuinely different experiment and may change it.

## Arithmetic Fidelity consequence

AF-150 left two possibilities: find additional hypotheses making source-natural information-center recanonicalization stable, or accept that recomputation destroys provenance even under approximate recoverability. AF-151 identifies the exact missing hypothesis at the finite order-infinity center level. **Recanonicalization stability is not controlled by recovery deficiency or by maximal-leakage drop alone; it is controlled by the normalized distribution of local max-sum conflict.**

This supplies a practical theorem surface for later arithmetic use. Given an intrinsic family of arithmetic controls and a proposed compression, compute or bound

\[
\kappa(y)
=\frac{\sum_x\max_iP_i(x)K(y\mid x)}
       {\max_i\sum_xP_i(x)K(y\mid x)}.
\]

If the downstream mechanism needs chi-square-stable recanonicalization, it must prove `\operatorname{Var}_r(\kappa)/(\mathbb E_r\kappa)^2\to0`; if it needs worst-case likelihood-ratio stability, it must control the essential range of `\kappa/\mathbb E_r\kappa`; and if only total variation is needed, the normalized mean absolute deviation is the exact quantity. This separates **mean information loss**, **local conflict heterogeneity**, and **the metric actually required by the destination theorem** instead of compressing all three into one scalar fidelity score.