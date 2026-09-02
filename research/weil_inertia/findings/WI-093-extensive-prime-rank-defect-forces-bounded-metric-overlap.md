# WI-093 — extensive prime Ramanujan rank defect forces only bounded metric overlap

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It strengthens WI-092 from the sharp one-third boundary layer to **every residual prime pair with positive-density rank defect**: a macroscopic loss of pairwise cross-Gram rank can occur only at a boundary occupying a positive fraction of the joint prime period, and in that regime the two whitened Ramanujan subspaces have only `O(1)` total squared canonical overlap. In particular, extensive rank defect is not accompanied by an extensive supply of strongly aligned metric directions.

Let `p<q<2p` be distinct odd primes, let

\[
G_{p,q}^{(N)}=(U_p^{(N)})^*U_q^{(N)},
\]

and put `delta=delta_N(p,q)` for the nearest-`pq` boundary length. Work in the residual regime

\[
\delta>q-1.
\tag{1}
\]

Write

\[
\delta=kq+s,
\qquad 0\le s<q,
\tag{2}
\]

and let

\[
\tau=(p-1)-\operatorname{rank}G_{p,q}^{(N)}
\tag{3}
\]

be the residual transversality defect of WI-086--WI-088. If `tau>0`, then necessarily the WI-088 exceptional strip holds, so `d=q-p<s<p`.

Let `Pi_p,Pi_q` denote the orthogonal projectors onto the two primitive-frequency sample spaces on the nearest boundary of length `delta`. The new exact tradeoff is

\[
\boxed{
\tau>0
\quad\Longrightarrow\quad
k=\left\lfloor\frac\delta q\right\rfloor\ge \tau+1,
\qquad
\delta>(\tau+1)q.
}
\tag{4}
\]

Consequently

\[
\boxed{
\operatorname{tr}(\Pi_p\Pi_q)
<
q\,\frac{\tau+2}{(\tau+1)^2}
<
2p\,\frac{\tau+2}{(\tau+1)^2}.
}
\tag{5}
\]

Thus if, along any sequence of residual prime pairs,

\[
\frac{\tau}{p}\longrightarrow\theta>0,
\tag{6}
\]

then the total squared canonical overlap is uniformly bounded. Using the exact WI-092 Frobenius formula rather than the coarse finite bound in (5) gives the sharper asymptotic statement

\[
\boxed{
\limsup\operatorname{tr}(\Pi_p\Pi_q)
\le \frac{1-\theta}{\theta}.
}
\tag{7}
\]

If `sigma_1,...,sigma_r` are the nonzero canonical correlations, where

\[
r=p-1-\tau,
\]

then

\[
\sum_{j=1}^r\sigma_j^2=\operatorname{tr}(\Pi_p\Pi_q).
\tag{8}
\]

Hence (6)--(7) imply

\[
\boxed{
\frac1r\sum_{j=1}^r\sigma_j^2=O_\theta(p^{-1}),
\qquad
\limsup p\,\frac1r\sum_{j=1}^r\sigma_j^2\le\frac1\theta,
}
\tag{9}
\]

and for every fixed `eta>0`,

\[
\boxed{
\limsup\#\{j:\sigma_j\ge\eta\}
\le
\frac{1-\theta}{\theta\eta^2}.
}
\tag{10}
\]

So even though the pairwise rank defect itself can be `Theta(p)` — WI-087/WI-088 show the sharp scale `theta=1/3` is attained — only `O_{theta,eta}(1)` canonical directions can have correlation at least a fixed `eta`. The average surviving canonical correlation tends to zero.

## 1. A positive rank defect forces the quotient `k` above the defect

The starting point is the exact partial-cycle model of WI-088. Inside the exceptional strip, put

\[
d=q-p,
\qquad
t=2p-q=p-d.
\tag{11}
\]

WI-088 constructs a partial permutation whose free directed cycles parametrize a superset of the true row kernel. If `c` is the number of free cycles, then

\[
\tau\le c-1.
\tag{12}
\]

Every free cycle avoids the `d` forced-zero vertices, so all free cycles together use at most

\[
t=p-d=2p-q<p
\tag{13}
\]

vertices. If `tau>0`, (12) gives `c>=tau+1`; therefore at least one free cycle has length `ell` with

\[
\ell\le\frac{t}{c}
\le\frac{t}{\tau+1}
<\frac{p}{\tau+1}.
\tag{14}
\]

On such a cycle, each `B`-vertex contributes the translation `kd` and each `A`-vertex contributes `(k+1)d`. If `a` of its `ell` vertices lie in `A`, the total translation around the cycle is

\[
(\ell k+a)d.
\tag{15}
\]

Because `d` is invertible modulo the prime `p` and the cycle closes,

\[
p\mid \ell k+a.
\tag{16}
\]

The integer in (16) is positive, and `0<=a<=ell`, so

\[
p\le\ell k+a\le\ell(k+1).
\tag{17}
\]

Combining (14) and (17),

\[
k+1\ge\frac p\ell>\tau+1.
\]

Since `k` and `tau` are integers,

\[
\boxed{k\ge\tau+1.}
\tag{18}
\]

Equation (2) and the exceptional-strip inequality `s>d>0` then give

\[
\delta=kq+s>kq\ge(\tau+1)q,
\]

which is (4).

This relation is stronger than the universal defect ceiling of WI-088 in a different direction. WI-088 controls `tau` through the number of vertices available for free cycles; (18) says that producing those cycles also forces the boundary quotient itself to be at least the defect. A macroscopic defect can therefore occur only at a macroscopic fraction of the full `pq` period.

## 2. Full Fourier Parseval gives a universal Frobenius-energy cap

Let `U_p^(delta)` and `U_q^(delta)` be the primitive Fourier sample matrices on `delta` consecutive rows and write

\[
F=\| (U_p^{(\delta)})^*U_q^{(\delta)}\|_F^2.
\tag{19}
\]

Enlarge both primitive frequency sets to **all** `p` and `q` Fourier characters. Since deleting rows or columns of a matrix cannot increase the sum of squared absolute entries,

\[
F\le
\sum_{a\bmod p}\sum_{b\bmod q}
\left|
\sum_{n=0}^{\delta-1}e\!\left(n\left(\frac bq-\frac ap\right)\right)
\right|^2.
\tag{20}
\]

Expanding the square and summing first over `a,b`, orthogonality forces

\[
n\equiv m\pmod p,
\qquad
n\equiv m\pmod q.
\]

Since `p,q` are distinct primes this means `n≡m (mod pq)`. By definition of nearest boundary,

\[
0<\delta\le\frac{pq}{2}<pq,
\]

so for `0<=n,m<delta` only `n=m` survives. Therefore the full-frequency sum in (20) is exactly

\[
\boxed{pq\delta,}
\tag{21}
\]

and hence

\[
\boxed{F\le pq\delta.}
\tag{22}
\]

This is just finite Fourier orthogonality/Parseval; no analytic number theory is used.

## 3. Whitening converts the energy cap into bounded canonical overlap

Set

\[
H_p=(U_p^{(\delta)})^*U_p^{(\delta)},
\qquad
H_q=(U_q^{(\delta)})^*U_q^{(\delta)}.
\tag{23}
\]

Because `delta>q-1>p-1`, both primitive sample matrices have full column rank. Partitioning the `delta` rows into complete periods plus a remainder gives the exact Loewner lower bounds already used in WI-092,

\[
H_p\succeq p\left\lfloor\frac\delta p\right\rfloor I,
\qquad
H_q\succeq q\left\lfloor\frac\delta q\right\rfloor I.
\tag{24}
\]

Put

\[
a=\left\lfloor\frac\delta p\right\rfloor,
\qquad
k=\left\lfloor\frac\delta q\right\rfloor.
\tag{25}
\]

The projector-overlap identity is

\[
\operatorname{tr}(\Pi_p\Pi_q)
=
\left\|
H_p^{-1/2}G_{p,q}^{(\delta)}H_q^{-1/2}
\right\|_F^2.
\tag{26}
\]

Using (22)--(24),

\[
\operatorname{tr}(\Pi_p\Pi_q)
\le
\frac{F}{pa\,qk}
\le
\frac{\delta}{ak}.
\tag{27}
\]

Since `q>p` and `delta>kq`, one has `a>=k`; while `delta<(k+1)q`. Thus

\[
\operatorname{tr}(\Pi_p\Pi_q)
<q\frac{k+1}{k^2}.
\tag{28}
\]

The function `(x+1)/x^2` decreases for positive `x`, and (18) gives `k>=tau+1`. Hence

\[
\operatorname{tr}(\Pi_p\Pi_q)
<q\frac{\tau+2}{(\tau+1)^2},
\]

proving the first part of (5); `q<2p` gives the second.

In particular, if `tau>=theta p` for a fixed `theta>0`, then already the entirely elementary finite estimate (5) gives

\[
\operatorname{tr}(\Pi_p\Pi_q)=O_\theta(1).
\tag{29}
\]

The phenomenon in WI-092 is therefore not peculiar to the exact or near-exact one-third ceiling. **Every positive-density residual rank defect lies in a bounded-metric-overlap regime.**

## 4. Exact WI-092 energy asymptotics sharpen `O(1)` to `(1-theta)/theta`

WI-092 records the exact primitive cross-energy formula. For `0<delta<pq`, with

\[
A=\left\lfloor\frac{\delta-1}{p}\right\rfloor,
\qquad
C=\left\lfloor\frac{\delta-1}{q}\right\rfloor,
\]

it is

\[
\begin{aligned}
F_{p,q}(\delta)
={}&\delta^2+\delta(pq-p-q)
-2pA\delta+p^2A(A+1)\\
&-2qC\delta+q^2C(C+1).
\end{aligned}
\tag{30}
\]

(The harmless `delta-1` convention changes the floor variables by at most one at period endpoints and does not affect the asymptotics below.)

Define

\[
\alpha=\frac{\delta}{pq}.
\tag{31}
\]

Because `delta=kq+s` with `0<=s<q` and `p<q<2p`,

\[
\alpha=\frac{k}{p}+O(p^{-1}).
\tag{32}
\]

If `tau/p -> theta>0`, (18) yields

\[
\liminf\alpha\ge\theta.
\tag{33}
\]

Uniformly for `alpha` in any fixed compact subinterval of `(0,1/2]`, the floor errors in (30) are `O(1)` and direct division by `p^2q^2` gives

\[
\boxed{
\frac{F_{p,q}(\delta)}{p^2q^2}
=\alpha(1-\alpha)+O(p^{-1}).
}
\tag{34}
\]

Likewise the denominator in the whitening bound satisfies

\[
\frac{p\lfloor\delta/p\rfloor\,q\lfloor\delta/q\rfloor}{p^2q^2}
=\alpha^2+O(p^{-1}).
\tag{35}
\]

Therefore

\[
\operatorname{tr}(\Pi_p\Pi_q)
\le
\frac{1-\alpha}{\alpha}+o(1).
\tag{36}
\]

The function `(1-alpha)/alpha` is decreasing. Together with (33), this proves (7):

\[
\limsup\operatorname{tr}(\Pi_p\Pi_q)
\le\frac{1-\theta}{\theta}.
\]

At the sharp WI-087/WI-088 scale `theta=1/3`, the right side is `2`. This explains the constant approached by the exact sharp family and sharpens WI-092's convenient uniform finite constant `<4` at the asymptotic level.

## 5. Only finitely many strongly correlated directions survive an extensive defect

The singular values of

\[
H_p^{-1/2}G_{p,q}^{(\delta)}H_q^{-1/2}
\]

are the canonical correlations `sigma_j` between the two sampled primitive-frequency subspaces, so (8) is standard principal-angle geometry. If `tau/p->theta`, then

\[
r=p-1-\tau=(1-\theta+o(1))p.
\tag{37}
\]

Dividing (7) by (37) yields

\[
\limsup
p\,\frac1r\sum_{j=1}^r\sigma_j^2
\le
\frac{(1-\theta)/\theta}{1-\theta}
=\frac1\theta,
\]

which is (9). Markov's inequality applied to the nonnegative numbers `sigma_j^2` gives

\[
\#\{j:\sigma_j\ge\eta\}
\le
\frac{\operatorname{tr}(\Pi_p\Pi_q)}{\eta^2},
\]

and (10) follows from (7).

This is the useful rigidity statement: a pair can lose a positive fraction of its **rank**, but it cannot simultaneously carry a positive fraction of canonical directions with order-one **metric alignment**. The two resources are asymptotically incompatible in the prime residual model.

## 6. Relation to WI-088--WI-092 and program consequence

WI-087 constructs an exact close-prime family with `tau/(p-1)->1/3`. WI-088 proves `1/3` is the universal prime residual rank-defect ceiling. WI-089--WI-091 then localize exact and near-exact ceiling configurations arithmetically and show that their incidence at fixed observation length is sparse. WI-092 adds a metric statement on that sharp boundary layer: the total squared canonical overlap is uniformly bounded and only finitely many directions can have a fixed-size canonical correlation.

The present result removes the main scope caveat from that metric conclusion. The bounded-overlap phenomenon does **not** require `tau` to sit within `O(1)` of the one-third ceiling, nor the special opposite-residue boundary formulas of WI-090/WI-091. It follows for every sequence with

\[
\tau\asymp p.
\]

Thus a scalar strategy that treats a macroscopic pairwise rank defect as though it supplied a comparable number of strongly coupled opposite-sign directions is structurally false throughout the entire positive-density defect regime. If a source-faithful signed Ramanujan mechanism is to obtain extensive cancellation from such pairs, it must use either:

- accumulation across many individually weak canonical directions with coefficient scaling strong enough to survive (9),
- collective many-modulus geometry that is not reducible to pairwise alignment,
- or source labels/weights discarded by the scalar projector model.

This does **not** prove that the actual Yang covariance lacks such a collective mechanism. WI-083 already shows that overcomplete scalar families can cancel exactly in other regimes, so pairwise metric weakness cannot be promoted to a global no-cancellation theorem without using the true source coefficients. The durable conclusion is narrower and negative: **macroscopic prime pairwise rank defect itself is not an extensive metric-cancellation resource.**

## 7. Prior art and novelty boundary

All load-bearing general ingredients are classical or already present in the Mathia chain.

- Finite Fourier orthogonality/Parseval gives (21)--(22).
- Principal angles/canonical correlations and the identity `tr(PQ)=sum sigma_j^2` for orthogonal projectors are standard matrix-analysis facts.
- The finite-duration Ramanujan-subspace setting and the design of near-orthogonal finite bases are established signal-processing prior art; see P. P. Vaidyanathan and Srikanth Tenneti, **Ramanujan subspaces and digital signal processing**, 48th Asilomar Conference on Signals, Systems and Computers (2014), and P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing—Parts I and II**, *IEEE Transactions on Signal Processing* 62 (2014), already represented in the line's source corpus.
- WI-088 supplies the partial-cycle defect theorem, and WI-092 supplies the exact primitive cross-energy formula and projector-overlap framework used in (30)--(36).

A targeted search around finite Ramanujan subspaces, near-orthogonal finite bases, principal angles and finite Fourier subspace overlap located the classical finite-duration/near-orthogonality literature but no source asserting the specific implication

\[
\tau/p\to\theta>0
\Longrightarrow
\limsup\operatorname{tr}(\Pi_p\Pi_q)\le(1-\theta)/\theta
\]

for the WI-088 residual prime rank defect. **No priority claim is made.** The durable Mathia contribution is the exact combination of the WI-088 cycle arithmetic with finite Fourier energy to turn rank-defect density into a metric-overlap ceiling.

No `SOURCES.md` change is needed because the external ingredients used here are classical and already anchored by the existing Ramanujan-subspace sources; the new implication is internal exact algebra built on WI-088 and WI-092.

## 8. Falsification and boundary conditions

1. **Prime residual regime only.** The cycle argument proving (18) is the prime partial-permutation theorem of WI-088. Composite moduli can have noninvertible steps and different cycle structure; no composite analogue is asserted.
2. **Close primes only when a defect exists.** WI-081/WI-088 already give full residual rank for `q>=2p`; the theorem is stated for `p<q<2p` because that is the only prime residual strip where `tau>0` can occur.
3. **Nearest-boundary convention.** The reduction uses `delta<=pq/2`. Translation to the complementary boundary changes only invertible phase factors and not rank, projector principal angles, or Frobenius norms, as in WI-081/WI-092.
4. **Whitened metric, not raw coefficient size.** `tr(Pi_p Pi_q)` measures canonical subspace overlap after internal frame conditioning. Raw unwhitened Ramanujan blocks carry additional `p,q` scale factors. WI-092 separately records their normalized Frobenius interpretation.
5. **Positive-density defect is essential for the asymptotic constant.** If `tau=o(p)`, (5) need not be `O(1)` and the present theorem does not exclude a growing metric-overlap budget. The new barrier is exactly the macroscopic-defect regime.
6. **Pairwise weakness is not global scalar rigidity.** WI-083 exhibits exact cancellation after overcompleteness. Many weak pairwise couplings can in principle cooperate, and the actual Yang coefficients may weight them nonuniformly. This finding does not infer a global inertia bound from (7).
7. **Numerical checks are non-load-bearing.** Before persistence, direct finite Fourier computations on residual prime examples including `(11,13,47)`, `(17,19,107)`, `(19,23,145)` and `(23,31,237)` found no violation of `k>=tau+1` or (5). Equations (12)--(28), not those computations, carry the result.

## 9. Consequence for the research program

The residual prime-pair picture now has a three-part rigidity ledger:

\[
\boxed{
\begin{array}{c}
\text{WI-088: } \tau/p\le1/3+o(1),\\
\text{WI-090--WI-091: near-ceiling defect is arithmetically sparse at fixed }N,\\
\text{WI-093: every }\tau/p\to\theta>0\text{ has only }O_\theta(1)\text{ metric overlap.}
\end{array}}
\]

This closes a broad version of the tempting pairwise-rank escape: one cannot obtain a macroscopic family of strongly aligned opposite-sign directions merely by moving away from the exact one-third boundary layer to another positive-density prime rank defect. The remaining source-faithful question is genuinely collective and weighted — whether the Yang coefficient law can coherently accumulate many weak canonical couplings or whether its arithmetic normalization forces those contributions to wash out. That is a different problem from maximizing pairwise rank loss and should be treated at the signed many-modulus/operator or original locked-covariance level rather than by further optimization of `tau` alone.