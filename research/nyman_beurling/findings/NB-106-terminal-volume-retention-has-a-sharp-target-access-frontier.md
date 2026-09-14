# NB-106 — terminal volume retention has a sharp target-access frontier

**Status:** `EXACT-DERIVED + TARGET-AWARE-TERMINAL-FRONTIER + BOUNDARY-DOUBLE-SCALING + FIXED-MULTIPLICITY + SINGLE-ZERO-STATE-COROLLARY + NEGATIVE/METHOD-BOUNDARY`.

`NB-105` optimizes the fixed-multiplicity confluent determinant volume under a terminal natural-index budget. Its optimum is expressed on the radial `1/a` scale: if

\[
\lambda_j=a_j+i\Gamma_j,
\qquad a_j\downarrow0,
\qquad G_j:=\max(1,|\Gamma_j|),
\]

and

\[
L_j:=2a_j\log\frac{B_j}{G_j}\to L\in(0,\infty),
\]

then the maximal limiting volume is `Delta_d(L)`, attained at scaled band start `s=0` and zero terminal slack. That result deliberately leaves target conversion separate. The target adds a second scale which the determinant does not see: in Paley--Wiener time the Nyman target is

\[
e(t)=e^{-t/2},
\qquad \|e\|_2^2=1,
\]

so a band beginning at natural index `m` contains only target mass `asymp 1/m`.

Combining these two facts gives a sharp Pareto frontier. Fix `theta in (0,1]`. If an admissible terminal band retains at least a fraction `theta` of the maximal fixed-multiplicity determinant volume, then necessarily

\[
\boxed{
\liminf_{j\to\infty}
2a_j\log\frac{m_j}{G_j}
\ge
\frac1d\log\theta.
}
\tag{1}
\]

If

\[
\mu_j
:=
\left\|e\,\mathbf 1_{[\log m_j,\log(m_jq_j)]}\right\|_2^2
=
\frac1{m_j}-\frac1{m_jq_j},
\tag{2}
\]

then every unit vector supported in that visible band has squared target pairing at most `mu_j`, and `(1)` implies

\[
\boxed{
2a_jd\log\frac1{\mu_j}
\ge
2a_jd\log G_j-
\log\frac1\theta
+o(1).
}
\tag{3}
\]

Thus the quantity

\[
\boxed{
H_j:=2a_jd\log G_j
}
\tag{4}
\]

is the missing **target-access depth**. If `H_j-log(1/theta)` stays bounded below by a positive constant, every band retaining a `theta` fraction of the best determinant volume is forced into an exponentially target-poor tail. Conversely this threshold is sharp at the `NB-105` continuum profile: if `H_j->H<infinity`, the earliest possible start `m_j=1` with asymptotically zero terminal slack retains exactly the fraction

\[
\boxed{e^{-H}}
\tag{5}
\]

of the maximal volume while keeping asymptotically all target mass. Hence whenever `theta<=e^{-H}`, determinant volume alone does **not** force any target loss.

The new point is that `NB-105`'s unique scaled optimum `s=0` does not determine ordinary target access. If `a_j log G_j->0`, even a band starting at `m=1` has `s_j->0` and can be asymptotically volume-optimal. Only when the finer depth `2a_jd log G_j` clears the threshold in `(3)` does terminal volume convert into an unavoidable moving-tail target penalty.

## 1. Retaining determinant volume bounds how early the band may start

Use the terminal coordinates of `NB-105`,

\[
s_j=2a_j\log\frac{m_j}{G_j},
\qquad
\tau_j=2a_j\log\frac{B_j}{m_jq_j}\ge0.
\tag{6}
\]

For every finite limiting placement the normalized confluent volume tends to

\[
\mathcal F_{d,L}(s,\tau)=
\begin{cases}
 e^{ds}\Delta_d(L-\tau),&s\le0<L-\tau,\\[1mm]
 \Delta_d(L-s-\tau),&0\le s<L-\tau,\\[1mm]
 0,&L-\tau\le\max(s,0).
\end{cases}
\tag{7}
\]

and `NB-105` also shows that starts with `s_j->-infinity` have vanishing volume. Suppose now that along a sequence of admissible bands

\[
\mathcal V^{\rm conf}_{d,m_j,q_j}(\lambda_j)
\ge
\theta\Delta_d(L)+o(1).
\tag{8}
\]

If a subsequential limit has `s<=0`, monotonicity of `Delta_d` and `tau>=0` give

\[
\theta\Delta_d(L)
\le
 e^{ds}\Delta_d(L-\tau)
\le
 e^{ds}\Delta_d(L),
\]

hence `s>=(log theta)/d`. If `s>=0`, the same inequality is automatic because `log theta<=0`. The `s=-infinity` regime is incompatible with `(8)`. Applying the argument to every subsequence proves `(1)`.

This bound is unaffected by unused terminal budget. Slack can only replace `Delta_d(L)` by the smaller `Delta_d(L-tau)`, so it cannot buy an earlier target-rich start at the same retained-volume fraction. Starting above the ordinate scale is also harmless for `(1)`: it only makes `m` larger and the target tail smaller.

For an **absolute** desired limiting volume `eta` with `0<eta<Delta_d(L)`, put

\[
\theta=\frac{\eta}{\Delta_d(L)}.
\]

Then the target-access threshold becomes

\[
\boxed{
H_j
>
\log\frac{\Delta_d(L)}{\eta}
}
\tag{9}
\]

by a positive margin. This separates the radial resource `L=2a log(B/G)` from the additional amount of scaled depth that must be crossed merely to reach target-bearing early indices.

## 2. The target-tail penalty is coordinate-free and exponentially sharp

The target mass in a visible natural-index band is exact:

\[
\begin{aligned}
\mu_j
&=
\int_{\log m_j}^{\log(m_jq_j)}e^{-t}\,dt\\
&=
\frac1{m_j}-\frac1{m_jq_j}
\le
\frac1{m_j}.
\end{aligned}
\tag{10}
\]

Therefore every unit vector `v` in the corresponding cell space obeys

\[
\boxed{
|\langle e,v\rangle|^2\le\mu_j\le\frac1{m_j}.
}
\tag{11}
\]

This is a Hilbert-space statement, not a coefficient-normalization estimate. Combining `m_j=G_j exp(s_j/(2a_j))` with `(1)` gives `(3)`. In particular, if for some fixed `epsilon>0`

\[
H_j
\ge
\log\frac1\theta+\epsilon,
\tag{12}
\]

then

\[
\boxed{
\mu_j
\le
\exp\!\left(
-\frac{\epsilon+o(1)}{2a_jd}
\right)
\longrightarrow0.
}
\tag{13}
\]

So once the target-access depth clears the retained-volume threshold by a fixed scaled margin, the surviving target mass is not merely small: it is exponentially small in `1/a_j`.

The converse shows that the exponent and threshold are not artifacts of Cauchy--Schwarz. Assume

\[
H_j=2a_jd\log G_j\to H<\infty.
\tag{14}
\]

Choose `m_j=1` and use the terminal budget completely, for example `q_j=floor(B_j)`. Then

\[
s_j=-2a_j\log G_j\to-\frac Hd,
\qquad
\tau_j\to0,
\]

so `(7)` yields

\[
\boxed{
\frac{\mathcal V^{\rm conf}_{d,1,q_j}(\lambda_j)}
     {\Delta_d(L)}
\longrightarrow e^{-H}.
}
\tag{15}
\]

At the same time

\[
\mu_j=1-\frac1{q_j}\longrightarrow1.
\tag{16}
\]

Hence for every fixed `theta<e^{-H}` -- and also at the boundary after the usual `o(1)` interpretation -- there are terminal bands that satisfy the required determinant-volume fraction while reaching the target origin. No theorem using only the `NB-105` volume profile can force target-poorness in that regime.

This exposes a subscale hidden by the statement "the optimum is at `s=0`." If `H_j->0`, the choice `m=1` itself has `s_j->0` and retains asymptotically the full maximal volume. Scaled placement uniqueness therefore does not imply ordinary-index localization near `G_j`.

## 3. The actual one-zero causal state is even more target-poor at the ordinate start

For `d=1` there is a sharper source-specific control at the concrete ordinate-scale placement. Let

\[
\rho_j=\frac12+a_j+i\gamma_j,
\qquad
G_j=|\gamma_j|\to\infty,
\]

and choose

\[
\frac{m_j}{G_j}\to1,
\qquad
R_j=m_jq_j,
\qquad
2a_j\log q_j\to L\in(0,\infty).
\tag{17}
\]

Let `u_j` be the Riesz representer in the visible cell space from `NB-094` for the one-zero causal state functional. Its squared norm is the exact leverage

\[
\Lambda_j
=
\frac{2a_j}{|\rho_j|^2}R_j^{2a_j}
\sum_{n=m_j}^{R_j-1}
 n(n+1)
\left|n^{-\rho_j}-(n+1)^{-\rho_j}\right|^2.
\tag{18}
\]

Then

\[
\boxed{
\Lambda_j\longrightarrow e^L-1.
}
\tag{19}
\]

One way to see the ordinate-uniformity is to split the sum at `K G_j`. On `m_j<=n<KG_j`, the integral identity

\[
n^{-\rho}-(n+1)^{-\rho}
=\rho\int_n^{n+1}t^{-\rho-1}\,dt
\]

bounds the normalized contribution by `O_L(a_j log K)=o(1)` for fixed `K`. On `n>=KG_j`, `|rho_j|/n=O(1/K)`, so the difference is `rho_j n^{-rho_j-1}(1+O(1/K))`; the resulting radial sum tends to `e^L-1+O(1/K)`. Letting `K->infinity` proves `(19)`.

The target restricted to the same band is exactly the sum of the cell vectors, so the state pairing telescopes:

\[
\boxed{
\langle e,u_j\rangle
=
\frac{\sqrt{2a_j}}{\rho_j}
R_j^{a_j+i\gamma_j}
\left(m_j^{-\rho_j}-R_j^{-\rho_j}ight),
}
\tag{20}
\]

up to the immaterial inner-product conjugation convention. Therefore

\[
|\langle e,u_j\rangle|^2
=
\frac{2a_j}{|\rho_j|^2m_j}
q_j^{2a_j}
|1-q_j^{-\rho_j}|^2.
\tag{21}
\]

Because `a_j->0`, `(17)` forces `q_j->infinity`, while `q_j^{2a_j}->e^L` and `|q_j^{-rho_j}|->0`. Dividing `(21)` by `(19)` gives the target energy carried by the normalized causal state:

\[
\boxed{
\left|
\left\langle e,
\frac{u_j}{\|u_j\|}
\right\rangle
\right|^2
=
\frac{2a_j}
{|\rho_j|^2G_j\,\Delta_1(L)}
\,(1+o(1)),
}
\tag{22}
\]

since `Delta_1(L)=1-e^{-L}`. As `|rho_j|~G_j`, this is of order

\[
\boxed{
\frac{a_j}{G_j^3}
}
\tag{23}
\]

for fixed `L`. The ambient band already contains only `asymp G_j^{-1}` target mass, and the specific zero-state direction pays the additional Hardy evaluation scale `2a_j/|rho_j|^2`.

Equation `(22)` is deliberately a statement about the terminal causal-state direction, not about the full Nyman residual. It shows why a large one-zero leverage or a healthy determinant volume at the natural ordinate start does not automatically become a target obstruction.

## 4. Adversarial controls and method boundary

The first control is the sharp converse `(15)`--`(16)`. It prevents the new target-tail estimate from being read as a uniform consequence of positive determinant volume. When `2a_jd log G_j` is too small, the band can be moved all the way to `m=1` while losing only the allowed determinant fraction. In particular, an off-critical zero approaching the critical line sufficiently rapidly relative to its ordinate remains outside the reach of a volume-only argument.

Second, `(11)` controls every vector supported in the visible band, but the actual finite Nyman approximant is not required to live only there. Cross-scale cooperation with earlier cells can carry target mass, exactly as the moving-tail controls in `NB-031` warn. The theorem therefore supplies a **necessary target-access gate** for converting the terminal state geometry; it is not a finite-section distance lower bound.

Third, the determinant statement remains fixed-multiplicity. For `d>1`, `(1)`--`(16)` apply to the confluent volume and to the target mass of the entire visible cell space, but `(22)` is proved only for the single elementary zero state. Genuine repeated-zero Jordan states and growing multiplicity require separate target calculations.

Fourth, the comparison does not repair diagonal normalization or the multi-zero conditioning problem. `NB-102`'s Menger-curvature gate and `NB-103`--`NB-105`'s determinant-volume gate remain distinct observables. The new quantity `H=2ad log G` enters only because the target has a preferred origin in Paley--Wiener time.

## 5. Prior-art boundary and research consequence

The Hardy-space fact that a zero gives a reproducing-kernel obstruction, and the classical Nyman--Beurling/Baez--Duarte target geometry, are already represented in `SOURCES.md` through Burnol, Báez-Duarte, and the modern Hardy-space literature. A targeted search covering Nyman--Beurling reproducing kernels, Blaschke zero obstructions, finite sections, target projections, and zero-sensitive Hardy-space orthogonality did not locate the specific terminal-volume/target-access frontier `(1)`--`(5)` or the natural-start causal-state asymptotic `(22)`. Search absence is not a priority claim.

No external theorem is load-bearing here. Equations `(1)`--`(16)` use the locally proved `NB-105` profile plus the exact time-domain target norm, while `(18)`--`(22)` use the exact one-zero state formula of `NB-094` and an elementary split of its cell sum. `SOURCES.md` therefore needs no new dependency.

The durable change in the research frontier is that terminal resolution is now two-dimensional. `NB-105` identified

\[
L=2a\log(B/G)
\]

as the determinant-volume resource **beyond** the zero ordinate. Target conversion also depends on

\[
H=2ad\log G,
\]

the scaled depth **from the target origin to** that ordinate. For a requested fraction `theta` of the best terminal volume, the exact continuum threshold is

\[
\boxed{
H=\log(1/\theta).
}
\tag{24}
\]

Above it, every such terminal band is forced into an exponentially target-poor tail; below it, a target-origin band can retain the requested volume fraction. This narrows the live target-aware question considerably: a successful zero obstruction must either exploit a regime where `H` is large enough for `(3)` to bite, or use a mechanism that transports the terminal zero-state information back across the gap to early target-bearing scales. The accepted target-aware finite-section clue remains unresolved because no lower bound for the full residual or dual certificate is claimed.