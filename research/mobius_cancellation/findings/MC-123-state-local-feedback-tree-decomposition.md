# MC-123 — State-local one-step feedback splits into potential and occupation terms

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `NO-NOVELTY-CLAIM`.

## Claim

Write

\[
M_n=M(n),\qquad \mu_n=\mu(n)=M_n-M_{n-1}\in\{-1,0,1\}.
\]

Consider an arbitrary real one-step observable

\[
\Psi(m,a),\qquad m\in\mathbb Z,\quad a\in\{-1,0,1\},
\]

which is allowed to depend on the current Mertens level and on the next Möbius increment, but on no additional history or arithmetic label.

For every undirected nearest-neighbor edge \(\{m,m+1\}\), define its reversal-odd and reversal-even parts

\[
g_m:=\frac{\Psi(m,1)-\Psi(m+1,-1)}2,
\qquad
r_m:=\frac{\Psi(m,1)+\Psi(m+1,-1)}2.
\tag{1}
\]

Because the state graph \(\mathbb Z\) is a tree, there is a potential \(F:\mathbb Z\to\mathbb R\), unique up to an additive constant, with

\[
F(m+1)-F(m)=g_m.
\tag{2}
\]

Then \(\Psi\) has the exact and unique decomposition

\[
\boxed{
\Psi(m,a)=F(m+a)-F(m)+R(m,a),
}
\tag{3}
\]

where

\[
R(m,1)=r_m,
\qquad
R(m,-1)=r_{m-1},
\qquad
R(m,0)=\Psi(m,0).
\tag{4}
\]

For every nonzero step the residual is **reversal-even**:

\[
R(m,1)=R(m+1,-1).
\tag{5}
\]

Thus every state-local one-step feedback statistic consists of only:

1. a conservative potential increment, whose oriented contribution is a coboundary; and
2. an unoriented edge-crossing occupation term, plus the separate zero-increment loop occupation.

There is no additional oriented state-local component on the one-dimensional Mertens state graph. In particular, \(\Psi\) is a pure potential difference if and only if

\[
\Psi(m,0)=0
\quad\text{and}\quad
\Psi(m,1)+\Psi(m+1,-1)=0
\quad\text{for every }m.
\tag{6}
\]

This gives a complete first-kill test for proposed feedback carriers of the form \(\Psi(M_{n-1},\mu_n)\): if the reversal-even defect in `(6)` vanishes, deterministic weighting can only repackage a path potential; if it does not vanish, all information beyond that potential is occupation-type rather than new oriented memory.

## 1. Exact decomposition on the Mertens state graph

On the edge joining \(m\) to \(m+1\), abbreviate

\[
A_m=\Psi(m,1),
\qquad
B_m=\Psi(m+1,-1).
\]

Equation `(1)` is simply

\[
A_m=g_m+r_m,
\qquad
B_m=-g_m+r_m.
\tag{7}
\]

Choose \(F(0)=0\) and integrate `(2)` along the integer line. There is no cycle-consistency condition to check because every two vertices of \(\mathbb Z\) are joined by a unique path. For a forward step,

\[
F(m+1)-F(m)+R(m,1)=g_m+r_m=A_m.
\]

For a backward step,

\[
F(m-1)-F(m)+R(m,-1)
=-g_{m-1}+r_{m-1}
=B_{m-1}
=\Psi(m,-1).
\]

For \(a=0\), the potential increment vanishes and `(4)` is tautological. This proves `(3)`.

The decomposition is canonical apart from adding a constant to \(F\): reversal parity fixes \(g_m\) and \(r_m\) uniquely on every edge, after which `(2)` fixes all potential differences. Equation `(6)` is therefore necessary and sufficient for the entire residual to vanish.

This is the one-dimensional tree specialization of the standard graph-flow distinction between gradient/conservative edge flows and non-gradient components. Combinatorial Hodge theory treats antisymmetric edge flows as discrete one-forms and decomposes them into gradient and cyclic pieces; on a tree the cycle space is absent, so every antisymmetric edge field is exact. The extra step here is elementary reversal-parity splitting because \(\Psi\) need not itself be antisymmetric.

## 2. Deterministic weighting cannot restore lost orientation

Let \(w_1,\ldots,w_N\) be arbitrary deterministic real weights and write

\[
\Psi_n=\Psi(M_{n-1},\mu_n),
\qquad
R_n=R(M_{n-1},\mu_n).
\]

Substituting `(3)` and summing by parts gives

\[
\boxed{
\begin{aligned}
\sum_{n=1}^N w_n\Psi_n
={}&w_NF(M_N)-w_1F(M_0)\\
&+\sum_{n=1}^{N-1}(w_n-w_{n+1})F(M_n)
+\sum_{n=1}^N w_nR_n.
\end{aligned}
}
\tag{8}
\]

Hence changing only the deterministic kernel \(w_n\) cannot create a new oriented carrier from the reversal-odd part. That part is already a potential transform. The only non-potential information left in a state-local one-step statistic is the weighted occupation residual in the last term of `(8)`.

This complements `MC-122`. There the candidate class \(\mu_nM_{n-1}\) plus its square-free correction was shown directly to collapse to quadratic path energy under arbitrary deterministic weights. Equation `(8)` explains the structural reason: after the correction, the square carrier is a pure gradient on the state graph.

The statement does **not** say that the residual is easy. Edge-crossing occupations and zero-step occupations can have difficult arithmetic dependence. It says only that they forget the direction of each nonzero crossing after conditioning on the crossed edge. Any genuinely new oriented memory must therefore enter through additional state, time/scale dependence, longer history, or arithmetic information not contained in the pair \((M_{n-1},\mu_n)\).

## 3. The square and Tanaka carriers are the two canonical examples

For the quadratic chain rule, take

\[
\Psi_Q(m,a)=2ma+a^2=(m+a)^2-m^2.
\tag{9}
\]

Then `(6)` holds exactly and `(3)` has \(F(m)=m^2\), \(R=0\). The amplitude-only term \(ma\) fails `(6)` by a constant reversal-even defect; adding \(a^2/2\) is exactly the correction that makes it conservative. This is the local version of the weighted quadratic-energy collapse in `MC-122`.

For the discrete Tanaka carrier from `MC-013`, take

\[
\Psi_T(m,a)
=\operatorname{sgn}(m)a
+\mathbf 1_{\{m=0\}}a^2.
\tag{10}
\]

The exact identity

\[
\Psi_T(m,a)=|m+a|-|m|
\tag{11}
\]

means again that `(6)` holds, now with \(F(m)=|m|\) and \(R=0\). Thus the **combined** sign-feedback plus zero-departure local-time carrier is a pure potential increment. Triangular weighting recovers the first absolute path energy precisely because it is summation by parts applied to that potential.

This sharpens the interpretation of `MC-013`: its usefulness cannot come from treating the combined Tanaka carrier as an independent source statistic. The nontrivial research question is whether its two separately nonconservative pieces admit independent Möbius-specific estimates whose combination yields the required \(L^1\) control.

The correction terms in `(9)` and `(10)` are therefore not incidental bookkeeping. They are exactly what cancels the reversal-even defect and turns the raw feedback into a state potential.

## 4. What survives outside the coboundary class

For a general \(\Psi\), the edge residual \(r_m\) contributes the same value whenever the path traverses \(\{m,m+1\}\) in either direction. If

\[
N_m^+(N)=\#\{n\le N:(M_{n-1},M_n)=(m,m+1)\},
\]

and

\[
N_m^-(N)=\#\{n\le N:(M_{n-1},M_n)=(m+1,m)\},
\]

then for unit weights its nonzero-step contribution is

\[
\sum_m r_m\bigl(N_m^+(N)+N_m^-(N)\bigr).
\tag{12}
\]

Only the **total crossing occupation** appears. The oriented imbalance

\[
N_m^+(N)-N_m^-(N)
\]

belongs to the potential part and is fixed by the endpoint relative to that edge. Zero increments contribute separately through

\[
\sum_{n\le N:\,\mu_n=0}\Psi(M_{n-1},0).
\tag{13}
\]

For Möbius, `(13)` can still couple the Mertens state to the nonsquare-free support. That coupling is not declared trivial. The classification simply identifies it as loop occupation rather than oriented feedback.

Consequently a state-local proposal can survive this obstruction in only two ways: prove a genuinely arithmetic theorem controlling one of these occupation residuals, or enlarge the observable beyond the state pair \((M_{n-1},\mu_n)\). Merely changing a deterministic weight, smooth nonlinear potential, or local coordinate cannot manufacture another oriented degree of freedom on the same one-dimensional state graph.

## Prior art and novelty assessment

The graph-theoretic mechanism is classical. Xiaoye Jiang, Lek-Heng Lim, Yuan Yao and Yinyu Ye, *Statistical ranking and combinatorial Hodge theory*, Mathematical Programming 127 (2011), 203–244, DOI `10.1007/s10107-010-0419-x`, treats pairwise data as antisymmetric edge flows and decomposes them into gradient and cyclic components using combinatorial Hodge theory. On a tree the cyclic component is absent, so an antisymmetric edge field integrates to a vertex potential. No novelty is claimed for this graph fact.

Fujita (`MC-S21`) is the existing line-local probability anchor for the discrete Tanaka/local-time mechanism. `MC-013` already specialized that mechanism to the Mertens walk. The present result does not claim a new stochastic-calculus theorem; it combines elementary reversal parity on directed nearest-neighbor transitions with the tree property to classify the whole state-local one-step observable class used by several live feedback proposals.

A targeted literature search for graph edge-flow Hodge decomposition, Markov/additive coboundaries, reversal symmetry, and discrete Tanaka formulas found the established gradient/cyclic and local-time languages above, but no reason to treat `(3)` as a new general theorem. The Mathia contribution is the exact application boundary: it identifies which part of a proposed Mertens feedback observable is automatically a path potential and what information can remain after that collapse.

## Boundaries and falsification tests

- This finding gives no new bound for \(M(x)\), \(D_M(x)\), edge occupations, or zero-step occupations.
- A reversal-even residual is not automatically useless. A Möbius-specific theorem controlling it could still be highly informative.
- Time-dependent or data-dependent observables \(\Psi_n\), multiscale couplings, delayed states, prime labels, divisor structure, or other enlarged state spaces are outside the fixed state-local class classified here.
- Deterministic weighting is covered by `(8)`, but a rule that chooses weights from additional arithmetic data may itself introduce new information and must be audited as such.
- On a state graph with cycles, an antisymmetric edge field can have a genuine non-gradient cyclic component. The absence of such a component here depends essentially on using only the scalar Mertens level as state.
- The loop term \(\Psi(m,0)\) cannot be absorbed into a vertex potential because a zero increment leaves the state unchanged. For Möbius it may encode square-free-support coupling and must be retained explicitly.
- A candidate should be killed as a purported new **oriented** carrier when its reversal-even defect vanishes and its only remaining novelty is a deterministic reweighting of the resulting potential. It should not be killed merely because it has a nonzero occupation residual.

## Consequence for the line

`MC-013` and `MC-122` are instances of one exact structural boundary. The scalar state \(M_{n-1}\) plus the current step \(\mu_n\) supplies no hidden oriented feedback degree of freedom beyond a potential difference. After the canonical reversal decomposition, everything else is unoriented edge or loop occupation.

The current mean-absolute frontier should therefore test new local feedback proposals against `(6)` immediately. If they are conservative, they are path-energy reformulations. If they are not, the precise surviving object is the occupation residual and should be attacked directly. A route seeking genuinely richer signed cross-scale information must introduce mathematically justified information beyond the one-step scalar state rather than repeatedly changing kernels inside the same conservative class.