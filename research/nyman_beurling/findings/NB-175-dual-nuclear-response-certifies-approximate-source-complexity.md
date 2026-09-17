# NB-175 — Dual nuclear response certifies approximate source complexity

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + DUAL-CERTIFICATE + NUCLEAR-RESPONSE + CAPPED-TRANSPORT + NB-174-LOWER-BOUND`.

`NB-174` identifies the epsilon-approximate linear source complexity `mathfrak L_T(epsilon)` as the source-resolved repertoire that an arbitrarily adaptive compact sampler must possess before logarithmic Euler rescue can persist on positive density. That theorem is useful only if the complexity can be bounded from the structure of a concrete sampler family. Syntactic rank or parameter count is not invariant enough: the same realized range can admit many very different dictionaries.

The present finding gives a representation-independent lower certificate. Probe finitely many realized templates by a jointly contractive family of linear observables in the capped-Poisson transport norm and assemble their responses into a matrix `A`. Its nuclear norm cannot be large unless every `epsilon`-approximate stationary dictionary has large `mY^2`. The certificate is intrinsic to the realized source geometry, not to a chosen parametrization.

The generic matrix inequality behind the argument is classical. The source-specific content is that the dual probes can be realized directly by vector-valued Lipschitz tests for the **same truncated transport metric** that controls `zeta'/zeta` in `NB-167`, and the residual penalty is exactly the `epsilon` used by `NB-174`.

## Claim

Fix one `T` and abbreviate

\[
\|\sigma\|_{P,T}
:=
\frac{\mathsf D_{a_T}(\sigma)}{q_T}
\]

for zero-mass finite signed measures supported on `[-B,B]`. Let `mathcal R_T` be the realized template range from `NB-174`.

Choose any `N` templates

\[
\nu_1,\ldots,\nu_N\in\mathcal R_T
\]

and any `K` linear functionals `ell_1,...,ell_K` on these signed measures satisfying the joint contraction

\[
\boxed{
\left(\sum_{k=1}^{K}|\ell_k(\sigma)|^2\right)^{1/2}
\le
\|\sigma\|_{P,T}
\qquad\text{for every zero-mass }\sigma.
}
\tag{1}
\]

Form the `N x K` response matrix

\[
A_{ik}:=\ell_k(\nu_i),
\]

and put `r=min{N,K}`. Then for every `epsilon>=0`,

\[
\boxed{
\mathfrak L_T(\epsilon)
\ge
\frac{
\left(
\|A\|_*
-
\epsilon\sqrt{Nr}
\right)_+^2
}{N},
}
\tag{2}
\]

where `||A||_*` is the nuclear (trace) norm, the sum of the singular values.

Consequently the quantity

\[
\mathfrak C_T(\epsilon)
:=
\sup
\frac{
\left(
\|A\|_*
-
\epsilon\sqrt{N\min\{N,K\}}
\right)_+^2
}{N},
\tag{3}
\]

where the supremum runs over all finite choices of realized templates and all jointly contractive probe families satisfying (1), is an invariant dual certificate with

\[
\boxed{
\mathfrak C_T(\epsilon)
\le
\mathfrak L_T(\epsilon).
}
\tag{4}
\]

No claim of equality is made.

## Derivation

Take any admissible `epsilon`-approximate dictionary in the definition of `mathfrak L_T(epsilon)` from `NB-174`:

\[
\nu_i
=
\sum_{j=1}^{m}\beta_{ij}\tau_j+r_i,
\qquad
\|\tau_j\|_{P,T}\le1,
\qquad
\|r_i\|_{P,T}\le\epsilon,
\]

with every coefficient row satisfying

\[
\sum_{j=1}^{m}|\beta_{ij}|^2\le Y^2.
\]

Let `B` be the `N x m` coefficient matrix, let `D` be the `m x K` dictionary-response matrix

\[
D_{jk}:=\ell_k(\tau_j),
\]

and let `E` be the residual-response matrix

\[
E_{ik}:=\ell_k(r_i).
\]

Then

\[
A=BD+E.
\tag{5}
\]

The row bound on the coefficients gives

\[
\|B\|_F\le\sqrt N\,Y.
\tag{6}
\]

The joint contraction (1), applied to each normalized dictionary atom, gives

\[
\sum_{k=1}^{K}|D_{jk}|^2\le1,
\qquad
\|D\|_F\le\sqrt m.
\tag{7}
\]

Similarly every residual row has Euclidean norm at most `epsilon`, so

\[
\|E\|_F\le\epsilon\sqrt N.
\tag{8}
\]

The Schatten Hölder inequality and the elementary rank bound for the nuclear norm now yield

\[
\|BD\|_*
\le
\|B\|_F\|D\|_F
\le
\sqrt{Nm}\,Y,
\tag{9}
\]

and

\[
\|E\|_*
\le
\sqrt{\operatorname{rank}E}\,\|E\|_F
\le
\epsilon\sqrt{Nr}.
\tag{10}
\]

Therefore

\[
\|A\|_*
\le
\sqrt{Nm}\,Y
+
\epsilon\sqrt{Nr}.
\]

Rearranging and squaring gives

\[
mY^2
\ge
\frac{
(\|A\|_* - \epsilon\sqrt{Nr})_+^2
}{N}.
\]

Taking the infimum over all admissible dictionaries proves (2), and then taking the supremum over finite probe configurations proves (4).

The proof does not require measurability of the adaptive rule and does not inspect the parametrization that generated the templates. It sees only the realized range in the normalized capped-transport geometry.

## Capped-Poisson probes are available intrinsically

Condition (1) is not an abstract extra structure. Write

\[
d_{a_T}(u,v)
:=
\min\left\{1,\frac{|u-v|}{a_T}\right\}.
\]

Let

\[
F=(f_1,\ldots,f_K):[-B,B]\to\ell_2^K
\]

be any vector-valued map satisfying

\[
\boxed{
\|F(u)-F(v)\|_2
\le
d_{a_T}(u,v)
\qquad(u,v\in[-B,B]).
}
\tag{11}
\]

Define

\[
\ell_k(\sigma)
:=
\frac1{q_T}\int f_k(u)\,d\sigma(u).
\tag{12}
\]

For any coupling `pi` of the positive and negative Jordan parts of a zero-mass `sigma`,

\[
\left(\sum_k|\ell_k(\sigma)|^2\right)^{1/2}
=
\frac1{q_T}
\left\|
\iint(F(u)-F(v))\,d\pi(u,v)
\right\|_2.
\]

By the triangle inequality in `ell_2^K` and (11),

\[
\left(\sum_k|\ell_k(\sigma)|^2\right)^{1/2}
\le
\frac1{q_T}
\iint d_{a_T}(u,v)\,d\pi(u,v).
\]

Taking the infimum over couplings gives exactly (1). Thus every vector-valued `1`-Lipschitz map for the truncated Poisson metric generates an admissible dual witness. This is the same metric that appears in `NB-167`; no new source scale is introduced.

Equivalently, the problem of proving a lower bound for `mathfrak L_T(epsilon)` can be attacked by constructing a finite family of realized templates and a single Hilbert-valued capped-Lipschitz observable whose response matrix has large nuclear norm.

## Near-orthogonal source responses force linear complexity growth

A useful special case makes the meaning of (2) transparent. Take `K=N` and suppose the probe matrix is approximately diagonal:

\[
A=\alpha I_N+R,
\qquad
\|R\|_*\le N\delta.
\tag{13}
\]

The triangle inequality for the nuclear norm gives

\[
\|A\|_*
\ge
N(\alpha-\delta).
\]

Therefore

\[
\boxed{
\mathfrak L_T(\epsilon)
\ge
N(\alpha-\delta-\epsilon)_+^2.
}
\tag{14}
\]

In particular, `N` realized templates that possess `N` jointly contractive source observables with order-one diagonal response and small cross-talk require approximate source complexity of order `N`, even if the templates arise from a concise nonlinear rule and even if their syntactic parameter count is tiny.

At the admissible `NB-174` resolution

\[
\epsilon_T
=\Theta\!\left(\frac{\log T}{H_T}\right),
\]

the same statement remains meaningful only when the source-visible singular values of the response matrix survive that tolerance. This is exactly the intended quotient: directions that differ below the resolution of `zeta'/zeta` are removed automatically by the `epsilon sqrt{Nr}` term rather than counted as genuine source complexity.

## Stress test and limitation

The joint condition (1) is essential. Without it one could duplicate the same scalar functional `K` times and inflate the response matrix artificially. The `ell_2` contraction forces all probes to share one unit dual budget, so a large nuclear response reflects genuinely simultaneous distinguishability rather than bookkeeping duplication.

The certificate is deliberately one-sided. Large `mathfrak C_T(epsilon)` proves large approximate linear source complexity, but small `mathfrak C_T(epsilon)` need not imply that the family is simple. A family may have large `mathfrak L_T(epsilon)` while every conveniently constructed jointly contractive probe system has low nuclear response. No converse duality is established here.

Likewise, metric entropy alone does not force a large nuclear certificate. A long or densely sampled rank-one amplitude family may have many separated points while all response matrices remain essentially rank one. This is consistent with `NB-173`--`NB-174`: covering complexity and linear source complexity are different currencies.

For `N=1`, (2) reduces to an amplitude-type lower bound and adds essentially no new information beyond `NB-167` and equation (16) of `NB-174`. The gain begins when several templates can be distinguished simultaneously by source-native directions.

Finally, this finding does **not** prove that a natural Nyman--Beurling template family has large complexity, nor that large complexity produces arithmetic rescue. It only supplies an invariant lower-bound mechanism for the resource isolated in `NB-174`. The sparse-height escape, the ultra-thin `a_T \lesssim T^{-1/2}` regime and the global Nyman approximation problem remain untouched.

## Representation audit

The matrix step is generic finite-dimensional analysis: nuclear norms, Frobenius factorization bounds and singular-value perturbation are classical. Closely related factorization norms such as `gamma_2` are standard tools for representation-independent matrix complexity. Transportation-cost/Lipschitz-free spaces are likewise classical realizations of the dual geometry of `W_1`-type metrics.

The source-specific transfer is narrower. The Banach geometry here is fixed by the **capped Poisson cost** `d_{a_T}` discovered in `NB-167`, the dictionary normalization and residual tolerance are exactly those of `NB-174`, and (11)--(12) turn that transport geometry into an `ell_2` family of simultaneous observables. The resulting nuclear response therefore measures distinctions that the arithmetic source can resolve at its own scale rather than distinctions inherited from an arbitrary ambient parametrization.

A focused prior-art search over nuclear/Frobenius factorization inequalities, `gamma_2` factorization norms, Lipschitz-free/transportation-cost spaces and vector-valued Kantorovich--Rubinstein constructions found the classical surrounding technologies, including the factorization-norm literature and modern work on Lipschitz-free spaces, but not this capped-Poisson-to-`NB-174` transfer. That absence is not used as evidence of novelty. No new external theorem is load-bearing: the matrix inequalities are proved at the level used above, while the capped transport/Kantorovich input is already anchored in this line's source ledger.

## Evidence ledger

**Internal load-bearing dependencies:** `NB-167` for the capped Poisson transport geometry; `NB-173` for the stationary linear dictionary currency; `NB-174` for `mathfrak L_T(epsilon)` and its source-resolution role.

**External load-bearing dependencies:** none beyond the Kantorovich--Rubinstein/transport background already recorded in `research/nyman_beurling/SOURCES.md`.

**Context-only prior art consulted:** classical nuclear/trace-norm factorization and `gamma_2` factorization-norm literature; transportation-cost/Lipschitz-free-space literature. These are representation technology, not evidence for a new arithmetic theorem.

## Frontier moved

`NB-174` asked for an invariant way to lower-bound source-resolved approximate linear complexity. Equations (2)--(4) provide one: **dual nuclear response under a shared capped-transport budget**.

The next non-formal step is no longer to invent a complexity statistic. It is to instantiate the certificate for source-natural nonlinear template families. Concretely, one should ask whether a proposed arithmetic rule admits many realized templates and one vector-valued `d_{a_T}`-Lipschitz witness with source-visible singular values surviving `epsilon_T = Theta(log T/H_T)`. If such witnesses cannot be built, the gap between `mathfrak C_T` and `mathfrak L_T` itself becomes the next structural obstruction to understand.