# NB-050 — weighted repair slack is exactly a finite Nyman discretization gap

**Status:** `EXACT-DERIVED + FINITE-CONTINUOUS/DISCRETE-NYMAN-BRIDGE + EXACT-TARGET-LOSS-NORMAL-FORM + EXACT-REPAIR-SLACK-IDENTITY + ORACLE-REFRAMING`. `NB-039` shows that the weighted tail contains a dilated discrete Nyman section, `NB-048` uses that copy to approximate the unique target repair, and `NB-049` shows that ambient-dual localization cannot reach the repair-relevant corridor `M d_N^2=O(1)`. The weighted tail has a stronger exact normal form: after undoing the Bagchi dilation it is not merely a space containing `V_floor(N/M)`, but a finite subspace of the original continuous Nyman family sampled at every parameter `M/n`. Consequently the entire recursive-repair slack is exactly the distance gain obtained by passing from the reciprocal-integer Báez-Duarte grid to this denser finite Nyman grid.

Use the continuous Nyman family on `(0,1]`

\[
\rho_\theta(x)
:=
\left\{\frac{\theta}{x}\right\}
-\theta\left\{\frac1x\right\},
\qquad 0<\theta\le1,
\tag{1}
\]

so the canonical discrete generators are

\[
g_j=\rho_{1/j}.
\tag{2}
\]

For integers `2<=M<=N`, retain the weighted tail of `NB-034`,

\[
\widehat h_n:=n g_n-(n+1)g_{n+1},
\qquad
\widehat W_{M,N}:=
\operatorname{span}(\widehat h_M,\ldots,\widehat h_{N-1}),
\tag{3}
\]

with the span understood as `{0}` when `M=N`. Define the finite continuous-parameter grid space

\[
\boxed{
\mathcal C_{M,N}
:=
\operatorname{span}
\{\rho_{M/n}:M<n\le N\}.
}
\tag{4}
\]

Let `A_M` be the Bagchi dilation isometry used throughout this line. Then

\[
\boxed{
\widehat W_{M,N}=A_M\mathcal C_{M,N}.
}
\tag{5}
\]

Thus, writing

\[
\delta_{M,N}:=\operatorname{dist}(e,\mathcal C_{M,N}),
\qquad e(x)=1,
\tag{6}
\]

the weighted target loss is exactly

\[
\boxed{
\widehat\kappa_{M,N}^2-d_N^2
=\|P_{\widehat W_{M,N}}e\|^2
=\frac{1-\delta_{M,N}^2}{M}.
}
\tag{7}
\]

Now put

\[
K=\left\lfloor\frac NM\right\rfloor,
\qquad
V_K=\operatorname{span}(g_2,\ldots,g_K),
\qquad
d_K=\operatorname{dist}(e,V_K),
\tag{8}
\]

with `V_1={0}` and `d_1=1`. Every reciprocal-integer parameter `1/j`, `2<=j<=K`, occurs in (4) at `n=Mj`, so

\[
\boxed{V_K\subseteq\mathcal C_{M,N},\qquad \delta_{M,N}\le d_K.}
\tag{9}
\]

If

\[
w_{M,N}=P_{\widehat W_{M,N}}e
\tag{10}
\]

is the exact target-selected repair from `NB-040`, while

\[
u_{M,N}=\frac1{\sqrt M}A_M P_{V_K}e
\tag{11}
\]

is the recursively supplied repair from `NB-048`, then the stronger exact identity is

\[
\boxed{
\|w_{M,N}-u_{M,N}\|^2
=
\frac{d_K^2-\delta_{M,N}^2}{M}.
}
\tag{12}
\]

Consequently the recursively repaired skeleton of `NB-048` satisfies

\[
\boxed{
\widetilde d_{M,N}^2-d_N^2
=
\frac{d_K^2-\delta_{M,N}^2}{M}.
}
\tag{13}
\]

The previous bound `0<=\widetilde d_(M,N)^2-d_N^2<=d_K^2/M` is therefore the result of discarding the finite continuous-grid improvement `d_K^2-\delta_(M,N)^2`. The missing target information is now isolated as one precise finite discretization gap.

## 1. Weighted adjacency is a dilated finite Nyman grid

For `M<=n<=N`, define

\[
q_n:=\frac nM\rho_{M/n}.
\tag{14}
\]

Since `\rho_1=0`, one has `q_M=0`. The Bagchi dilation satisfies, on `(0,1/M]`,

\[
(A_Mf)(x)=\sqrt M\,f(Mx),
\tag{15}
\]

and its image vanishes on `(1/M,1]`. A direct substitution gives

\[
A_Mq_n
=
\sqrt M\left[
\frac nM\left\{\frac1{nx}\right\}
-
\left\{\frac1{Mx}\right\}
\right]
\qquad(0<x\le1/M).
\tag{16}
\]

Hence the common last term cancels between adjacent indices and

\[
A_M(q_n-q_{n+1})
=
\frac1{\sqrt M}
\left[
 n\left\{\frac1{nx}\right\}
-(n+1)\left\{\frac1{(n+1)x}\right\}
\right].
\tag{17}
\]

But the bracket is exactly `\widehat h_n`: the two `-{1/x}` terms in `n g_n-(n+1)g_(n+1)` cancel. `NB-034` already proves that every weighted edge with `n>=M` vanishes on `(1/M,1]`, so (17) is a global identity,

\[
\boxed{
\widehat h_n
=
\sqrt M\,A_M(q_n-q_{n+1}).
}
\tag{18}
\]

The adjacent differences in (18) span exactly the points `q_(M+1),...,q_N`: starting from `q_M=0`, telescoping recovers each `q_n`, and conversely every difference lies in their span. Nonzero scalar factors do not change spans, so

\[
\operatorname{span}(q_{M+1},\ldots,q_N)
=
\operatorname{span}(\rho_{M/(M+1)},\ldots,\rho_{M/N})
=\mathcal C_{M,N}.
\tag{19}
\]

Equations (18)--(19) prove (5). This is stronger than the inclusion `A_MV_K subseteq \widehat W_(M,N)` used in `NB-039`: that inclusion is simply the subgrid obtained from the indices `n=Mj`.

## 2. The target loss and recursive repair have exact discretization formulas

Let

\[
e_T:=\mathbf1_{(0,1/M]}.
\tag{20}
\]

The dilation isometry obeys

\[
e_T=\frac1{\sqrt M}A_Me.
\tag{21}
\]

Since `\widehat W_(M,N)=A_M\mathcal C_(M,N)` and the weighted tail is supported on `(0,1/M]`, orthogonal projection commutes with the isometric copy:

\[
\boxed{
w_{M,N}
=P_{\widehat W_{M,N}}e
=P_{\widehat W_{M,N}}e_T
=
\frac1{\sqrt M}A_M P_{\mathcal C_{M,N}}e.
}
\tag{22}
\]

Therefore

\[
\|w_{M,N}\|^2
=
\frac1M\|P_{\mathcal C_{M,N}}e\|^2
=
\frac{1-\delta_{M,N}^2}{M},
\tag{23}
\]

which proves (7) using the exact Pythagorean target-loss identity of `NB-034`.

The recursive vector (11) is the same construction with the nested subspace `V_K subseteq \mathcal C_(M,N)`. Thus

\[
w_{M,N}-u_{M,N}
=
\frac1{\sqrt M}A_M
\left(P_{\mathcal C_{M,N}}e-P_{V_K}e\right).
\tag{24}
\]

For nested closed finite-dimensional subspaces, the projection increment is orthogonal to the smaller projection, hence

\[
\begin{aligned}
\left\|P_{\mathcal C_{M,N}}e-P_{V_K}e\right\|^2
&=
\|P_{\mathcal C_{M,N}}e\|^2-
\|P_{V_K}e\|^2\\
&=(1-\delta_{M,N}^2)-(1-d_K^2)\\
&=d_K^2-\delta_{M,N}^2.
\end{aligned}
\tag{25}
\]

Combining (24)--(25) proves (12). `NB-048` already identifies the squared distance penalty of its repaired skeleton with `||w_(M,N)-u_(M,N)||^2`, giving (13).

Equation (23) also turns the `NB-039` recursive sandwich

\[
\frac{1-d_K^2}{M}
\le
\widehat\kappa_{M,N}^2-d_N^2
\le\frac1M
\tag{26}
\]

into a transparent nested-space statement:

\[
1-d_K^2
\le
1-\delta_{M,N}^2
\le1.
\tag{27}
\]

The lower estimate in `NB-039` was exactly the approximation power of the reciprocal-integer subgrid inside the full finite parameter grid.

## 3. The critical corridor now depends on a gap, not on the whole smaller distance

The exact relative repair error is

\[
\boxed{
\frac{\widetilde d_{M,N}^2}{d_N^2}-1
=
\frac{d_K^2-\delta_{M,N}^2}{M d_N^2}.
}
\tag{28}
\]

Therefore the sufficient condition from `NB-048`,

\[
\frac{d_K^2}{M d_N^2}\to0,
\tag{29}
\]

can be replaced exactly by

\[
\boxed{
\frac{d_K^2-\delta_{M,N}^2}{M d_N^2}\to0.
}
\tag{30}
\]

This distinction matters precisely after `NB-049`. In the critical/subcritical regime `M d_N^2=O(1)`, ambient Cauchy control through `Omega_M` cannot prove relative localization, and the coarse estimate `d_K^2/M` need not be negligible. Equation (30) leaves a genuinely different possibility: the recursive repair can still be asymptotically exact if the intermediate parameters `M/n` improve the finite approximation only slightly beyond the reciprocal-integer subgrid, even when neither `d_K^2` nor `1/M` is small relative to `d_N^2`.

This does **not** prove that the discretization gap is small. It identifies the exact finite quantity that must now be controlled. A source-specific continuation can ask whether

\[
d_{\lfloor N/M\rfloor}^2-
\operatorname{dist}
\left(e,
\operatorname{span}\{\rho_{M/n}:M<n\le N\}
\right)^2
\tag{31}
\]

admits a one-sided estimate at `M d_N^2=O(1)` that is cheaper than recovering the full `N`-section target oracle. Such an estimate would evade the ambient-norm obstruction of `NB-049` because (31) is a nested finite-space approximation increment, not an upper bound for `||Omega_M||`.

There is also a useful geometric interpretation. The weighted edges are discrete derivatives, in the uniform variable `alpha=n/M`, of

\[
\alpha\,\rho_{1/\alpha}.
\tag{32}
\]

After dilation, telescoping those derivatives restores the sampled continuous Nyman family itself. The weighted-tail quotient is therefore removing a finite **off-grid enrichment** of the Báez-Duarte reciprocal lattice. The exact target repair is the projection onto the enriched grid; `NB-048` keeps only the reciprocal-integer subgrid.

## 4. Boundary checks and falsification conditions

The endpoint `M=N` is exact. Then `\widehat W_(M,M)={0}`, the set in (4) is empty, `\delta_(M,M)=1`, and (7) gives zero target loss. Also `K=1`, so `d_K=1` and (12)--(13) give zero repair slack.

When `M<N<2M`, one still has `K=1`, hence the recursive repair is zero, while `\mathcal C_(M,N)` may already be nontrivial. Equations (12)--(13) reduce to

\[
\|w_{M,N}\|^2
=
\frac{1-\delta_{M,N}^2}{M},
\tag{33}
\]

as required. Thus no hidden `N>=2M` hypothesis is needed for the exact normal form; that restriction enters only later when one wants the uniform `log 2/M` floor from `NB-039`.

The result is an identity, not a source-access theorem. Computing `P_(\mathcal C_(M,N))e` or `\delta_(M,N)` directly can be as target-oracular as computing the original weighted repair. Nor does the classical equivalence between the full continuous and reciprocal-integer Nyman closures supply a quantitative estimate for the finite gap (31). Any claim that (31) is small at a useful scale must be proved without assuming the desired Nyman-distance behavior.

A decisive audit can falsify the finding at its first step: verify (18) pointwise from the definitions of `A_M`, `rho_theta`, and the weighted edge. Once (18) holds, the span identity (5), projection formula (22), and gap identities are finite Hilbert-space algebra. Numerical finite-section checks may test these equalities but are not evidence for an asymptotic estimate of (31).

## 5. Prior-art boundary and research consequence

The continuous Nyman family and Báez-Duarte's reduction to the much smaller reciprocal-integer family are classical; no novelty is claimed for that distinction. Báez-Duarte's strengthening establishes the global closure equivalence relevant to RH, and Bagchi supplies the dilation Hilbert-space framework already anchored in `SOURCES.md`. A targeted audit over finite Nyman--Beurling approximation, continuous versus natural parameter families, dilation formulations, and recent multiscale/Gram work did not reveal an external theorem needed for (5), (7), or (12). Search absence is not a priority claim, so `SOURCES.md` does not change.

The line-local advance is the exact finite identification of the weighted-tail geometry with the sampled space `\mathcal C_(M,N)` and the resulting equality (13). It replaces an amorphous smaller-section oracle error by one sharply defined approximation increment. The accepted weighted-skeleton data-access question therefore narrows again: below the `NB-049` ambient threshold, the relevant target quantity is no longer the whole smaller distance `d_K^2`, but the **continuous-grid versus reciprocal-grid gap** `d_K^2-\delta_(M,N)^2`. Determining whether that gap has source-accessible cancellation at `M d_N^2=O(1)` is now a precise route that is not eliminated by the existing ambient-dual obstruction.