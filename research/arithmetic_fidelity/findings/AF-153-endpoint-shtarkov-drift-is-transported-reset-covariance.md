# AF-153 — Endpoint Shtarkov drift is transported reset covariance

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `QUANTITATIVE-FIDELITY`, `TARGET-RELATIVE`, `POSITIVE-STABILITY-CRITERION`, `NO-NOVELTY-CLAIM`

## Claim

AF-152 showed that, along a chain of stochastic compressions with the Shtarkov/NML center recomputed after every stage, the current density mismatch evolves by conditional averaging followed by a local canonical reset. Its additive total-variation bound deliberately discarded how later channels contract an earlier reset.

There is an exact complementary representation that keeps that missing transport information. Every endpoint mismatch is the signed superposition of the individual local reset defects pushed through the remaining suffix channels. Consequently, the contribution of one local Shtarkov conflict to a declared endpoint discriminator is not its reset magnitude alone: it is its covariance with that discriminator pulled backward through the later compressions.

Let

\[
\mathcal E_0=(P_i^{(0)})_{i=1}^m
\]

be a finite experiment and let

\[
X_0\xrightarrow{K_1}X_1\xrightarrow{K_2}\cdots\xrightarrow{K_n}X_n
\tag{1}
\]

be stochastic channels. Use the notation of AF-152:

\[
P_i^{(j)}=P_i^{(0)}K_1\cdots K_j,
\qquad
M_j=\frac{s_j}{C_j},
\qquad
s_j(x)=\max_i P_i^{(j)}(x),
\tag{2}
\]

for the stage-`j` Shtarkov center, and

\[
q_j:=M_0K_1\cdots K_j,
\qquad
R_j:=M_{j-1}K_j.
\tag{3}
\]

Define the signed local reset defect

\[
\Delta_j:=R_j-M_j.
\tag{4}
\]

For `j<n`, write

\[
K_{j+1:n}:=K_{j+1}\cdots K_n,
\tag{5}
\]

and let `K_{n+1:n}` be the identity channel on `X_n`. Then

\[
\boxed{
q_n-M_n
=
\sum_{j=1}^n \Delta_j K_{j+1:n}.
}
\tag{6}
\]

Thus the endpoint error is an exact discrete variation-of-constants formula: each recanonicalization injects a signed defect at its own stage, and all later compression acts only by transporting or contracting that defect.

AF-151 identifies each reset density exactly. Define the local envelope-conflict factor

\[
\kappa_j(y)
=
\frac{\sum_x s_{j-1}(x)K_j(y\mid x)}{s_j(y)},
\qquad
\mu_j
=
\mathbb E_{M_j}\kappa_j
=
\frac{C_{j-1}}{C_j}.
\tag{7}
\]

Then

\[
\frac{dR_j}{dM_j}
=
\rho_j
=
\frac{\kappa_j}{\mu_j},
\qquad
\Delta_j=(\rho_j-1)M_j.
\tag{8}
\]

Therefore every bounded endpoint observable `f:X_n -> R` satisfies the exact target-relative identity

\[
\boxed{
(q_n-M_n)(f)
=
\sum_{j=1}^n
\frac{1}{\mu_j}
\operatorname{Cov}_{M_j}
\!\left(
\kappa_j,
K_{j+1:n}f
\right).
}
\tag{9}
\]

This is the load-bearing distinction. `kappa_j` measures which source-envelope maximizers were put into local conflict by stage `j`; `K_{j+1:n}f` measures which part of the final discriminator is still visible when pulled back to that stage. A large local conflict does not affect the chosen endpoint discriminator when those two quantities are uncorrelated.

In particular, if the suffix channel makes `f` constant at stage `j`, then the `j`th contribution in `(9)` is exactly zero. This includes AF-152's extreme control in which a later channel collapses the whole state space to one point: all earlier reset defects are annihilated, not merely bounded crudely.

## Exact transport derivation

The one-step identity is purely algebraic:

\[
\begin{aligned}
q_j-M_j
&=q_{j-1}K_j-M_j\\
&=(q_{j-1}-M_{j-1})K_j
 +(M_{j-1}K_j-M_j)\\
&=(q_{j-1}-M_{j-1})K_j+\Delta_j.
\end{aligned}
\tag{10}
\]

Since `q_0=M_0`, iterating `(10)` gives `(6)` exactly.

Now let `f` be a bounded function on `X_n`. Acting on `f` and using the Markov pullback convention

\[
(Kf)(x)=\sum_yK(y\mid x)f(y)
\tag{11}
\]

gives

\[
(q_n-M_n)(f)
=
\sum_{j=1}^n
\Delta_j(K_{j+1:n}f).
\tag{12}
\]

By `(8)`, for any bounded `g` on `X_j`,

\[
\begin{aligned}
\Delta_j(g)
&=\mathbb E_{M_j}[(\rho_j-1)g]\\
&=\operatorname{Cov}_{M_j}(\rho_j,g)\\
&=\frac1{\mu_j}
\operatorname{Cov}_{M_j}(\kappa_j,g),
\end{aligned}
\tag{13}
\]

because `E_{M_j} rho_j=1`. Substituting `g=K_{j+1:n}f` proves `(9)`.

Equation `(9)` is not a new divergence. It is a decomposition of one declared endpoint response into the local conflict components that can actually reach that response.

## Suffix-contracted total-variation budget

For a Markov kernel `L`, define its Dobrushin contraction coefficient

\[
\delta(L)
:=
\sup_{x,x'}
\|L(\cdot\mid x)-L(\cdot\mid x')\|_{\rm TV}.
\tag{14}
\]

For every finite signed measure `sigma` of total mass zero,

\[
\|\sigma L\|_{\rm TV}
\le
\delta(L)\|\sigma\|_{\rm TV}.
\tag{15}
\]

Applying `(15)` term by term to the exact superposition `(6)` gives

\[
\boxed{
\|q_n-M_n\|_{\rm TV}
\le
\sum_{j=1}^n
\delta(K_{j+1:n})
\|R_j-M_j\|_{\rm TV}.
}
\tag{16}
\]

The identity suffix has coefficient one, while for earlier stages

\[
\delta(K_{j+1:n})
\le
\prod_{r=j+1}^n\delta(K_r).
\tag{17}
\]

Hence the product form

\[
\boxed{
\|q_n-M_n\|_{\rm TV}
\le
\sum_{j=1}^n
\left(
\prod_{r=j+1}^n\delta(K_r)
\right)
\|R_j-M_j\|_{\rm TV}.
}
\tag{18}
\]

AF-151 supplies the exact local reset term

\[
\|R_j-M_j\|_{\rm TV}
=
\frac{1}{2\mu_j}
\mathbb E_{M_j}|\kappa_j-\mu_j|.
\tag{19}
\]

Combining `(16)` and `(19)` yields the Shtarkov-specific stability certificate

\[
\boxed{
\|q_n-M_n\|_{\rm TV}
\le
\sum_{j=1}^n
\frac{\delta(K_{j+1:n})}{2\mu_j}
\mathbb E_{M_j}|\kappa_j-\mu_j|.
}
\tag{20}
\]

AF-152's unweighted additive TV estimate is the special case obtained by replacing every suffix coefficient by the trivial bound `delta <= 1`. Formula `(20)` is therefore strictly more informative whenever later stages mix or coarse-grain strongly.

The same statement can be expressed on observables. For

\[
\operatorname{osc}(f):=\max f-\min f,
\tag{21}
\]

one has

\[
\operatorname{osc}(Lf)
\le
\delta(L)\operatorname{osc}(f),
\tag{22}
\]

and every zero-mass signed measure satisfies

\[
|\sigma(f)|
\le
\|\sigma\|_{\rm TV}\operatorname{osc}(f).
\tag{23}
\]

Thus

\[
|(q_n-M_n)(f)|
\le
\operatorname{osc}(f)
\sum_{j=1}^n
\delta(K_{j+1:n})
\|R_j-M_j\|_{\rm TV}.
\tag{24}
\]

The TV bound is the uniform version of this target-relative statement.

## A variance-sensitive target bound

The covariance form `(9)` also gives a different certificate that does not first collapse each reset to TV. Cauchy--Schwarz gives

\[
\begin{aligned}
\left|
\frac1{\mu_j}
\operatorname{Cov}_{M_j}
(\kappa_j,K_{j+1:n}f)
\right|
&\le
\frac{\sqrt{\operatorname{Var}_{M_j}(\kappa_j)}}{\mu_j}
\sqrt{
\operatorname{Var}_{M_j}(K_{j+1:n}f)
}\\
&=
\sqrt{\chi^2(R_j\|M_j)}
\sqrt{
\operatorname{Var}_{M_j}(K_{j+1:n}f)
},
\end{aligned}
\tag{25}
\]

where the final equality is AF-151. Therefore

\[
\boxed{
|(q_n-M_n)(f)|
\le
\sum_{j=1}^n
\sqrt{\chi^2(R_j\|M_j)}
\sqrt{
\operatorname{Var}_{M_j}(K_{j+1:n}f)
}.
}
\tag{26}
\]

This separates two quantities that a scalar information-loss budget conflates:

- how nonuniform the local canonical reset is; and
- how much variance of the declared endpoint witness remains visible before that reset.

A large `chi^2` reset can be harmless for one target whose pulled-back witness is nearly constant, while a much smaller reset can matter if it aligns with the surviving target direction.

## Separating controls

### Complete later collapse annihilates every earlier reset

Suppose some suffix channel `K_{j+1:n}` is constant, sending every point of `X_j` to the same endpoint law. Then

\[
\delta(K_{j+1:n})=0
\tag{27}
\]

and for every endpoint observable `f`, `K_{j+1:n}f` is constant. Both `(9)` and `(16)` therefore say that the entire `j`th transported reset vanishes exactly.

This recovers AF-152's singleton control, but now identifies the general mechanism: the local defect is a zero-mass signed measure, so a suffix that forgets its source state annihilates it.

### No later contraction recovers the unweighted budget

If every suffix acts isometrically on the relevant signed defect -- for example the remaining maps are deterministic bijections -- then

\[
\delta(K_{j+1:n})=1
\tag{28}
\]

and no generic improvement over AF-152's unweighted TV budget is available from contraction alone. The improvement in `(16)` is therefore not formal decoration; it measures an actual property of the downstream channel chain.

### Target orthogonality is finer than metric smallness

Even when

\[
\|R_j-M_j\|_{\rm TV}>0,
\qquad
\delta(K_{j+1:n})=1,
\tag{29}
\]

the stage can contribute exactly zero to a specified `f` whenever

\[
\operatorname{Cov}_{M_j}
(\kappa_j,K_{j+1:n}f)=0.
\tag{30}
\]

Thus a metric certificate answers whether **every** bounded endpoint discriminator is stable, whereas `(9)` answers whether the particular discriminator under study is aligned with the local conflict. This distinction is essential for an RH application, where the relevant target is not the full probability law but a specific arithmetic or analytic witness family.

## Prior art and novelty assessment

The transport and contraction ingredients are classical.

- E. Seneta, **“Coefficients of ergodicity: structure and applications,”** *Advances in Applied Probability* 11(3), 576--590 (1979), DOI `10.2307/1426955`, develops coefficients of ergodicity for finite stochastic matrices and their contraction role.
- A. Yu. Mitrophanov, **“Sensitivity and convergence of uniformly ergodic Markov chains,”** *Journal of Applied Probability* 42(4), 1003--1014 (2005), DOI `10.1017/S0021900200001066`, gives perturbation bounds in terms of ergodicity coefficients of iterated transition kernels. This is direct neighboring prior art for weighting local perturbations by how later Markov evolution contracts them.
- Stéphane Gaubert and Zheng Qu, **“Dobrushin’s Ergodicity Coefficient for Markov Operators on Cones,”** *Integral Equations and Operator Theory* 81(1), 127--150 (2015), DOI `10.1007/s00020-014-2193-2`, characterizes the total-variation contraction ratio of the dual Markov operator and, by duality, the corresponding Hopf-oscillation contraction.
- Yury Polyanskiy and Yihong Wu, **“Strong data-processing inequalities for channels and Bayesian networks,”** arXiv:`1508.06025` (2015, revised 2016), surveys channel contraction and studies end-to-end composition including Dobrushin total-variation coefficients.

The signed telescoping identity `(6)`, Dobrushin inequalities `(15)--(18)`, and observable duality `(22)--(24)` are standard Markov-operator / perturbation mathematics. **No novelty is claimed for these general facts.**

The Shtarkov specialization comes only from inserting AF-151's exact local reset density into that classical transport calculus. A targeted prior-art search did not locate a source stating the specific covariance decomposition `(9)` for repeatedly recomputed Shtarkov/NML centers, but absence from that search is not a novelty claim. The durable content recorded here is the exact bridge between the already-derived local max-sum conflict profile and the classical suffix-contraction machinery.

## Boundary conditions and audit

The theorem is stated for finite sample spaces, where all Shtarkov centers and Radon--Nikodym ratios used by AF-151 are elementary. The exact signed transport identity `(6)` itself needs only probability measures and Markov kernels and extends far more generally whenever the compositions are defined; the Shtarkov conflict formulas require the existence and normalizability assumptions of AF-151/AF-152.

The Dobrushin coefficient controls total variation uniformly over all zero-mass signed perturbations. It may therefore be pessimistic for a particular reset direction. Equation `(9)` is the finer target-relative statement and should be preferred when the endpoint discriminator is known.

Conversely, target-relative covariance can be zero for one witness while other information is badly damaged. It is not a certificate of full experiment recovery. A family-wide fidelity claim needs the relevant witness family to be norming or otherwise complete for the declared destination category.

The bounds `(16)`, `(18)`, `(20)`, and `(26)` are one-sided sufficient estimates. The exact identity `(6)` allows different transported signed defects to cancel at the endpoint, so a sum of positive stage costs cannot generally supply a converse lower bound without additional alignment or sign hypotheses.

Finally, `delta(K_{j+1:n})` measures contraction of the **actual suffix channel**, not recanonicalization drift. A strong pipeline audit therefore has two independent stage quantities: the local Shtarkov reset injected by recanonicalization and the later transport that determines how much of that reset survives.

## Consequence for Arithmetic Fidelity

AF-150 separated approximate experiment recovery from Shtarkov-center provenance. AF-151 identified the complete local reset profile `kappa_j`. AF-152 supplied its nonlinear density recursion and showed that local reset costs alone overestimate endpoint drift because later averaging can erase earlier mismatch.

The present result closes that composition gap at the signed-response level:

\[
\boxed{
\text{endpoint response}
=
\sum_j
\text{local conflict}
\times
\text{surviving pulled-back witness}.
}
\tag{31}
\]

This is more informative than asking whether each compression is individually small. For a future rational-prime application, a candidate downstream observable family should be pulled backward through the proposed compression chain and tested against the local arithmetic-conflict profiles. A stage is dangerous only to the extent that its reset aligns with a discriminator that survives the later maps.

Accordingly, the next arithmetic-fidelity gate is not merely to minimize a scalar loss or choose a canonical reference. It is to identify a source-natural prime discriminator or witness family and prove that its backward transport remains sufficiently nonconstant, while the corresponding local conflicts are either controlled or deliberately aligned. The theorem does not supply that prime discriminator or an RH implication; it specifies exactly how such information would have to survive a chain once declared.