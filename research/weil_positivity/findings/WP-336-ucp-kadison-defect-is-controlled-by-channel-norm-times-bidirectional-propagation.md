---
id: WP-336
title: UCP Kadison defect is controlled by channel norm times bidirectional propagation
branch: weil_positivity
status: supported
kind: ucp-propagation-rigidity-boundary
claim_strength: exact sharp rowwise and operator-norm bounds for martingale Markov/UCP self-maps on finite real source spectra; the WP-335 Mangoldt tail construction attains equality, so asymptotic identity plus subcritical bidirectional propagation restores multiplicative-domain rigidity while fixed defect requires diverging nonlocal propagation budget
created: 2026-09-16
related: [WP-332, WP-333, WP-334, WP-335]
prior_art:
  - Rajendra Bhatia and Chandler Davis, A Better Bound on the Variance, The American Mathematical Monthly 107 (2000), no. 4, 353-357, DOI 10.1080/00029890.2000.12005203
  - Richard V. Kadison, A Generalized Schwarz Inequality and Algebraic Invariants for Operator Algebras, Annals of Mathematics 56 (1952), 494-503, DOI 10.2307/1969657
  - W. Forrest Stinespring, Positive Functions on C*-Algebras, Proceedings of the American Mathematical Society 6 (1955), 211-216, DOI 10.1090/S0002-9939-1955-0069403-4
  - Man-Duen Choi, A Schwarz Inequality for Positive Linear Maps on C*-Algebras, Illinois Journal of Mathematics 18 (1974), 565-574, DOI 10.1215/ijm/1256051007
---

# WP-336 — UCP Kadison defect is controlled by channel norm times bidirectional propagation

## Claim

`WP-335` showed that a support-preserving martingale UCP readout can converge to the identity in ordinary channel norm while retaining a fixed Kadison defect on the moving logarithmic Mangoldt coordinate. The construction paid for that defect by sending a vanishing amount of mass a growing distance backward along the dyadic prime-power ray.

That tradeoff is exact and admits a sharp converse.

Let `Sigma` be a finite subset of the real line, let `X(t)=t`, and let

\[
\Psi:C(\Sigma)\to C(\Sigma)
\]

be a Markov/UCP self-map with transition law `P_x` at `x`. Assume the source coordinate is preserved exactly,

\[
\Psi(X)=X.
\tag{1}
\]

For each `x`, define the off-diagonal mass

\[
\varepsilon_x:=1-P_x(\{x\}),
\tag{2}
\]

and the one-sided propagation radii

\[
L_-(x):=x-\min \operatorname{supp}P_x,
\qquad
L_+(x):=\max \operatorname{supp}P_x-x.
\tag{3}
\]

The Kadison defect of the source coordinate is

\[
Q:=\Psi(X^2)-X^2\ge0.
\tag{4}
\]

Then, row by row,

\[
\boxed{
0\le Q(x)\le \varepsilon_x L_-(x)L_+(x).
}
\tag{5}
\]

Moreover the ordinary operator norm of the Markov perturbation is exactly

\[
\boxed{
\|\Psi-I\|=2\sup_x\varepsilon_x,
}
\tag{6}
\]

so

\[
\boxed{
\|Q\|
\le
\frac12\|\Psi-I\|
\sup_x L_-(x)L_+(x).
}
\tag{7}
\]

Consequently, for a family `(Psi_R,X_R)` on growing finite source spectra, the quantitative condition

\[
\|\Psi_R-I\|\,
\sup_x L_{-,R}(x)L_{+,R}(x)
\longrightarrow0
\tag{8}
\]

forces

\[
\|\Psi_R(X_R^2)-X_R^2\|\longrightarrow0.
\tag{9}
\]

By the Stinespring factorization used in `WP-332`--`WP-335`, the corresponding off-diagonal source-observable coupling also tends to zero. Thus ordinary channel-norm convergence *does* recover asymptotic multiplicative-domain rigidity once it is paired with a subcritical source-coordinate propagation bound.

The estimate is sharp. The asymmetric dyadic tail map of `WP-335` attains equality in both (5) and (7) at every sufficiently large cutoff. Therefore the obstruction found there cannot be removed by improving constants or by replacing a crude diameter estimate with another bound depending only on channel norm and the same one-sided support radii.

This remains a negative boundary theorem, not a Weil-positivity mechanism. It identifies the exact nonlocality price that the surviving UCP escape must pay.

**Classification:** `EXACT-DERIVED + LITERATURE-BACKED + SHARP-BOUNDARY + UCP-READOUT + MARTINGALE + PROPAGATION-RIGIDITY + MATCHED-CONTROL + DECISIVE-NEGATIVE + NOT-WEIL-POSITIVITY`.

## 1. Rowwise defect is a conditional variance

Fix `x`. Because `Psi(X)=X`, the transition law satisfies

\[
\int t\,dP_x(t)=x.
\tag{10}
\]

Hence

\[
Q(x)
=
\int t^2\,dP_x(t)-x^2
=
\int (t-x)^2\,dP_x(t).
\tag{11}
\]

If `epsilon_x=0`, the row is deterministic and (5) is trivial. Suppose `epsilon_x>0`. Condition `P_x` on leaving `x`, and let `Z=t-x` under that conditional law. Since the mass left at `x` has displacement zero, (10) gives

\[
\mathbb E Z=0.
\tag{12}
\]

Its support lies in

\[
-L_-(x)\le Z\le L_+(x).
\tag{13}
\]

The Bhatia--Davis variance inequality for a real random variable with mean `mu` in `[m,M]` states

\[
\operatorname{Var}(Z)\le(M-\mu)(\mu-m).
\tag{14}
\]

Here `mu=0`, `m=-L_-(x)`, and `M=L_+(x)`, so

\[
\mathbb E Z^2
\le L_-(x)L_+(x).
\tag{15}
\]

Multiplying by the probability `epsilon_x` of leaving the center yields exactly (5):

\[
Q(x)
=
\varepsilon_x\,\mathbb E Z^2
\le
\varepsilon_xL_-(x)L_+(x).
\tag{16}
\]

This proof also exposes why **bidirectional** propagation is the correct quantity. Under the exact martingale condition, nonzero off-diagonal variance requires access to both sides of the current coordinate; one very long direction can be balanced by a short displacement on the other side.

## 2. Channel norm records exactly the escape mass

For each row,

\[
(P_x-\delta_x)(\{x\})=-\varepsilon_x
\tag{17}
\]

and the total positive mass away from `x` is `epsilon_x`. Therefore the total variation norm of the signed row measure is

\[
\|P_x-\delta_x\|_{TV}=2\varepsilon_x.
\tag{18}
\]

The operator norm of a kernel from `C(Sigma)` to itself with the sup norm is the supremum of the total variation norms of its rows. Thus

\[
\|\Psi-I\|
=
\sup_x\|P_x-\delta_x\|_{TV}
=2\sup_x\varepsilon_x,
\tag{19}
\]

which proves (6). Combining (16) and (19) gives (7).

It is useful to isolate the propagation budget

\[
B(\Psi,X):=
\sup_xL_-(x)L_+(x).
\tag{20}
\]

Then the entire stability statement is

\[
\|Q\|\le\frac12\|\Psi-I\|B(\Psi,X).
\tag{21}
\]

In particular, uniformly finite-range or uniformly bounded-propagation martingale kernels cannot realize the `WP-335` escape while converging to the identity in channel norm.

## 3. WP-335 saturates the bound exactly

On the modified row of `WP-335`, write `h=log 2` and `a=a_R`. Its transition probabilities are

\[
p_-={1\over a(a+1)},
\qquad
p_0=1-{1\over a},
\qquad
p_+={1\over a+1},
\tag{22}
\]

with displacements `-ah`, `0`, and `+h`. Therefore

\[
\varepsilon=p_-+p_+={1\over a},
\qquad
L_-=ah,
\qquad
L_+=h.
\tag{23}
\]

The conditional off-diagonal distribution is supported exactly at the two endpoints `-L_-` and `L_+` and has mean zero. This is the equality case of Bhatia--Davis. Hence

\[
Q(y_j)
=
\varepsilon L_-L_+
=
{1\over a}(ah)h
=h^2.
\tag{24}
\]

At the same time `WP-335` proved

\[
\|\Psi-I\|={2\over a}.
\tag{25}
\]

Thus (7) is also saturated:

\[
{1\over2}\|\Psi-I\|L_-L_+
=
{1\over2}{2\over a}(ah)h
=h^2.
\tag{26}
\]

So `WP-335` is not merely a counterexample to an insufficient topology. It is an extremizer for the natural propagation-corrected topology.

## 4. What the sharp boundary excludes

Suppose a source-derived positive readout on the finite Mangoldt cutoffs remains martingale on the logarithmic coordinate and is asymptotically the identity in channel norm. If its source-coordinate propagation satisfies

\[
B_R:=\sup_xL_{-,R}(x)L_{+,R}(x)=O(1),
\tag{27}
\]

or more generally

\[
\|\Psi_R-I\|B_R\to0,
\tag{28}
\]

then its Kadison defect must vanish. Such a family cannot preserve a fixed nonzero off-diagonal Stinespring coupling to `X_R`.

Conversely, if

\[
\limsup_R\|Q_R\|>0
\quad\text{while}\quad
\|\Psi_R-I\|\to0,
\tag{29}
\]

then (21) forces

\[
B_R
\gtrsim
{1\over\|\Psi_R-I\|}
\tag{30}
\]

along a subsequence. Any surviving mechanism in this commutative martingale/UCP class must therefore spend a diverging bidirectional propagation budget. The `WP-335` map sits exactly at this critical scale: its channel error is `Theta(1/a_R)` while `B_R=Theta(a_R)`.

This is more precise than imposing a bound on the full support diameter. The extremal escape is highly asymmetric: one side grows like `a_R h`, the other remains exactly `h`. The product `L_-L_+`, rather than `max(L_-,L_+)^2`, captures the actual second-moment cost sharply.

## 5. Matched controls and limits of the theorem

Nothing in (5)--(21) is specific to primes. The argument applies to every finite real spectrum and every Markov kernel preserving its coordinate barycentrically. Generic equally spaced rays and artificial geometric tails obey the same inequality. Therefore this theorem does not itself detect Mangoldt support or distinguish the Riemann source from matched controls.

The hypotheses are also real restrictions. The conclusion can fail to address a candidate that:

- does not preserve the source coordinate exactly;
- uses a genuinely noncommutative observable for which the scalar support-radius reduction is unavailable;
- leaves the Markov/UCP readout category;
- allows the propagation product to grow at the critical or supercritical rate in (30).

For an approximately preserved coordinate, a separate bias term enters and must be controlled; that regime is not claimed here. Likewise the theorem says nothing about generating the archimedean Gamma contribution or the polar counterterms, and it supplies no global Weil sign.

These exclusions are deliberate. The result closes only the natural proposal that the `WP-335` escape could survive after adding ordinary locality/quasilocality to channel-norm convergence.

## 6. Prior-art and novelty audit

The variance estimate used in (14)--(16) is classical. Bhatia and Davis proved the sharp bound

\[
\operatorname{Var}(Z)\le(M-\mu)(\mu-m),
\tag{31}
\]

with equality precisely at the endpoint-supported extremal distribution. No novelty is claimed for that inequality. Positive-operator approximation theory also classically treats control of `1`, `x`, and `x^2` as the decisive test family, so the broad principle that second moments are load-bearing is not new.

The repository-level mathematical delta is the exact application to the moving source geometry isolated by `WP-332`--`WP-335`: the Kadison defect factors into **escape probability times a sharp bidirectional propagation cost**, ordinary channel norm is exactly twice the maximal escape probability, and the intrinsic dyadic Mangoldt counterexample from `WP-335` is an equality case. This converts the qualitative redirect toward an energy/moment topology into a precise sharp threshold and identifies exactly which form of source locality restores rigidity.

The result is therefore `LITERATURE+DERIVED`, not a claim of a new variance theorem.

## 7. Consequence for the Weil-positivity search

The viable UCP boundary is now narrower. A source-forced positive geometry cannot retain a fixed critical Mangoldt coupling through a readout that is simultaneously

\[
\text{asymptotically identity in bounded-channel norm}
\quad\text{and}\quad
\text{subcritical in bidirectional source propagation}.
\tag{32}
\]

To evade (21), it must keep a nonvanishing channel deformation, pay a diverging nonlocal propagation cost at least reciprocal to the channel error, or use structure outside the scalar martingale/UCP coordinate framework.

This does not advance the missing Gamma/polar assembly by itself. It does, however, turn the vague requirement of an `energy/graph-norm or moment-weighted topology` from `WP-335` into a falsifiable quantitative resource bound. Any future source-derived positive completion in this lane can now be tested first against (21) before investing in its global Weil interpretation.
