# MC-353 — Privacy-loss tails exactly price the rare-event source-edge loophole

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-351` shows that bounded-energy reciprocal dephasing forces a nonvanishing average Jeffreys/KL separation across natural neighboring source states. `MC-352` upper-prices that separation when every source edge has a finite essential-supremum log-likelihood radius, but explicitly leaves a rare-event loophole: a tiny exceptional set can carry arbitrarily large likelihood ratio and therefore arbitrarily large KL.

That loophole has an exact distributional currency.

For a natural source edge `e={x,x'}`, write

\[
P_e:=\operatorname{Law}(Y\mid X=x),
\qquad
Q_e:=\operatorname{Law}(Y\mid X=x'),
\]

and retain the half-Jeffreys divergence

\[
b_e
:=\frac12\bigl(D(P_e\|Q_e)+D(Q_e\|P_e)\bigr).
\tag{1}
\]

When `P_e,Q_e` are mutually absolutely continuous, define the privacy-loss / log-likelihood variable

\[
L_e(y):=\log\frac{dP_e}{dQ_e}(y),
\qquad
M_e:=\frac12(P_e+Q_e),
\tag{2}
\]

and

\[
\psi(u):=u\tanh(u/2).
\tag{3}
\]

Then there is the exact identity

\[
\boxed{
 b_e=\mathbf E_{M_e}\,\psi(|L_e|).
}
\tag{4}
\]

If the neighboring laws have a singular part, both sides are interpreted as `+infinity` in the natural extended sense, so every finite upper-budget conclusion below automatically fails rather than hiding the singularity.

Now choose a natural source edge uniformly at random—Hamming-one edges for even rank and parity-preserving pair-flip edges for odd rank—and, conditional on that edge, draw the transcript from its mixture law `M_e`. Let

\[
U_R:=|L_e(Y)|
\tag{5}
\]

under this edge-mixture experiment. If

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad
C<\infty,
\quad \eta>0,
\tag{6}
\]

then the edge-budget bounds already proved in `MC-351` imply, for either parity,

\[
\boxed{
\mathbf E\,\psi(U_R)
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{7}
\]

Thus fixed nontrivial bounded-energy dephasing requires a **constant average privacy-loss mass per natural source edge**. The essential-supremum condition of `MC-352` is sufficient but far stronger than necessary.

For any threshold `u>=0`, define the exceptional privacy-loss tail budget

\[
T_R(u)
:=
\mathbf E\bigl[\psi(U_R)\mathbf1_{\{U_R>u\}}\bigr].
\tag{8}
\]

Since `psi` is increasing,

\[
\mathbf E\psi(U_R)
\le
\psi(u)+T_R(u),
\tag{9}
\]

so `(7)` forces

\[
\boxed{
T_R(u)
\ge
\frac{\eta^2}{C}-\psi(u)-o(1).
}
\tag{10}
\]

In particular, if `u_R->0`, then any surviving bounded-energy dephasing architecture must place asymptotically nonvanishing `psi`-mass in the exceptional likelihood tail. Typical neighboring rows becoming indistinguishable is not enough; the rare exceptional events must remain quantitatively expensive.

There is a directly usable moment form. For every `p>1`, let

\[
B_{p,R}:=\bigl(\mathbf E U_R^p\bigr)^{1/p},
\qquad
q_R(u):=\mathbf P(U_R>u).
\tag{11}
\]

Because `psi(v)<=v`, Hölder gives

\[
T_R(u)
\le
B_{p,R}\,q_R(u)^{1-1/p}.
\tag{12}
\]

Hence every architecture satisfying `(6)` must obey

\[
\boxed{
\psi(u)+B_{p,R}\,q_R(u)^{1-1/p}
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{13}
\]

Consequently, if for some fixed `p>1`

\[
\sup_R B_{p,R}<\infty
\tag{14}
\]

and `U_R->0` in probability under the natural edge-mixture law, then

\[
\mathbf E\psi(U_R)\to0,
\]

contradicting `(7)`. More generally the `L^p` hypothesis can be replaced by uniform integrability of `U_R`: **convergence of source-edge privacy loss to zero in probability plus uniform integrability rules out fixed nontrivial bounded-energy dephasing.**

This is the weaker reverse-regularity target left open by `MC-352`. A future arithmetic/endpoint architecture need not prove a uniform likelihood-ratio ceiling. It is enough to prove that typical neighboring source states induce vanishing privacy loss while exceptional privacy-loss tails are uniformly integrable (or satisfy a quantitative moment bound such as `(12)`). Conversely, any architecture that escapes this barrier must exhibit either nonvanishing typical likelihood contrast, moment blow-up, or a rare-event tail carrying constant Jeffreys mass.

No estimate for `M(x)` follows. This is a finite reciprocal-endpoint admission theorem that identifies exactly what an exceptional likelihood tail must pay.

## 1. Half-Jeffreys divergence is exactly a mixture expectation of privacy loss

Take a common dominating measure and write the two row densities as `p,q`. On their common support set

\[
L=\log(p/q).
\]

The elementary identity

\[
\frac{p-q}{p+q}
=
\tanh(L/2)
\tag{15}
\]

implies

\[
\begin{aligned}
\mathbf E_M\psi(|L|)
&=
\int \frac{p+q}{2}
\,|L|\tanh(|L|/2)\\
&=
\frac12\int(p-q)L\\
&=
\frac12\left(D(P\|Q)+D(Q\|P)\right).
\end{aligned}
\tag{16}
\]

The second equality uses that `p-q` and `L` always have the same sign. This proves `(4)`.

Equation `(16)` also explains the exact function that appeared as an upper envelope in `MC-352`: if `|L|<=epsilon` almost surely, then immediately

\[
b_e\le\psi(\varepsilon).
\tag{17}
\]

Thus the pure likelihood-radius result is the bounded-support special case of the full privacy-loss distribution identity.

## 2. MC-351 gives the same asymptotic tariff in both parities

For even rank, let `E_1` be the surviving Hamming-one edges and write

\[
\overline b_R
:=\frac1{|E_1|}\sum_{e\in E_1}b_e.
\]

Using the exact edge count from `MC-351`,

\[
\mathfrak J_1
=R\Lambda_R\,\overline b_R,
\tag{18}
\]

where `Lambda_R=(2^R-2)/(2^R-1)`. Equation (12) of `MC-351` therefore gives under `(6)`

\[
\overline b_R
\ge
\frac{\eta^2}{C\Lambda_R}-o(1)
=
\frac{\eta^2}{C}-o(1).
\tag{19}
\]

For odd rank, on the conditional even-parity source let `E_2` be the surviving pair-flip edges. Its exact edge count gives

\[
\mathfrak J_2
=
\frac{R}{2}\Lambda_R\Lambda_{R-1}\,\overline b_R.
\tag{20}
\]

Equation (13) of `MC-351` gives

\[
\mathfrak J_2
\ge
\frac{\eta^2}{2C}R-O(1),
\]

hence again

\[
\overline b_R
\ge
\frac{\eta^2}{C\Lambda_R\Lambda_{R-1}}-o(1)
=
\frac{\eta^2}{C}-o(1).
\tag{21}
\]

But by `(4)`, averaging over a uniformly chosen natural edge and then its mixture transcript gives

\[
\overline b_R=\mathbf E\psi(U_R),
\tag{22}
\]

which proves `(7)`.

The parity-dependent graph normalizations therefore disappear at the per-edge level: both source geometries demand the same asymptotic constant average statistical contrast for fixed `(eta,C)`.

## 3. Rare exceptional likelihood events cannot be discarded without a tail budget

The split `(9)` is exact up to replacing the good contribution by its maximum `psi(u)`. The tail term is deliberately not replaced by exceptional-set probability alone.

Indeed, let `0<d<1/2` and consider two laws on `{0,1}`,

\[
P_d(1)=d,
\qquad
Q_d(1)=d e^{-1/d}.
\tag{23}
\]

At output `1`,

\[
L_d(1)=1/d,
\]

while at output `0`,

\[
L_d(0)
=
\log\frac{1-d}{1-d e^{-1/d}}
=-d+O(d^2).
\tag{24}
\]

Under the mixture `M_d=(P_d+Q_d)/2`, the exceptional output `1` has probability

\[
M_d(1)=\frac d2(1+e^{-1/d})\to0.
\tag{25}
\]

Therefore `|L_d|->0` in probability as `d->0`. Nevertheless `(4)` gives

\[
\begin{aligned}
b(P_d,Q_d)
&=M_d(1)\psi(1/d)+M_d(0)\psi(|L_d(0)|)\\
&\longrightarrow\frac12.
\end{aligned}
\tag{26}
\]

The vanishing exceptional set carries a likelihood loss of order `1/d`, leaving constant Jeffreys mass. Equivalently, the family is not uniformly integrable.

This explicit two-point example is the load-bearing counterexample to any attempt to replace `(12)` or uniform integrability by `q_R(u_R)->0` alone. It is also the precise failure mode behind the warning in `MC-352` that approximate likelihood control with positive exceptional mass need not bound KL.

## 4. Uniform integrability is the exact qualitative closure condition

Suppose `U_R->0` in probability and the nonnegative family `{U_R}` is uniformly integrable. Then `psi(U_R)->0` in probability because `psi` is continuous and `psi(0)=0`, while

\[
0\le\psi(U_R)\le U_R.
\tag{27}
\]

Uniform integrability of `U_R` therefore implies uniform integrability of `psi(U_R)`. Vitali convergence gives

\[
\mathbf E\psi(U_R)\to0.
\tag{28}
\]

By `(22)` the average source-edge Jeffreys budget tends to zero, contradicting `(19)` or `(21)` under any fixed `(eta,C)`.

The `L^p` condition `(14)` is only a convenient quantitative sufficient condition for this qualitative criterion. It should not be mistaken for the unique analytic route: exponential moments, Rényi-divergence control, Orlicz bounds, or direct tail integration can all certify the same required uniform-integrability property.

This is useful for arithmetic applications because essential-supremum likelihood control is often destroyed by harmless unbounded noise or by very rare transcript outcomes. The actual obstruction depends on their integrated divergence cost, not on whether the likelihood ratio is literally bounded everywhere.

## 5. Prior art and novelty boundary

The statistical ingredients are classical and no novelty is claimed for them.

The privacy-loss random variable and control of its tails/moments are standard in differential privacy. Ilya Mironov, *Rényi Differential Privacy*, IEEE Computer Security Foundations Symposium (2017), pp. 263–275, DOI `10.1109/CSF.2017.11`, develops Rényi-divergence control specifically as a compact way to represent privacy-loss tails and composition. Cynthia Dwork and Guy Rothblum, *Concentrated Differential Privacy*, arXiv `1603.01887` (2016), and Mark Bun and Thomas Steinke, *Concentrated Differential Privacy: Simplifications, Extensions, and Lower Bounds*, TCC 2016, arXiv `1605.02065`, likewise use moment/tail control of privacy loss rather than a pure worst-case likelihood ceiling.

The Jeffreys divergence identity `(16)` is elementary `f`-divergence algebra, and the implication from convergence in probability plus uniform integrability to convergence of expectations is the classical Vitali convergence principle. The moment-tail estimate `(12)` is Hölder's inequality. A targeted literature audit on 17 September 2026 found no basis for claiming any of these components as new.

The durable Mathia delta is the composition with the independently derived reciprocal-source edge tariff `MC-351`: the rare-event loophole left open by `MC-352` is now quantified by `(10)` and `(13)`. The analytic target is strictly weaker than a pure source-edge likelihood-ratio ceiling and remains representation-invariant because it is stated only through the complete neighboring transcript laws.

Primary/authoritative audit links:

- Mironov 2017, IEEE CSF: `https://doi.org/10.1109/CSF.2017.11` and `https://arxiv.org/abs/1702.07476`.
- Dwork and Rothblum 2016, *Concentrated Differential Privacy*: `https://arxiv.org/abs/1603.01887`.
- Bun and Steinke 2016, *Concentrated Differential Privacy: Simplifications, Extensions, and Lower Bounds*: `https://arxiv.org/abs/1605.02065`.
- Kullback and Leibler 1951, *On Information and Sufficiency*, Annals of Mathematical Statistics 22(1), 79–86, DOI `10.1214/aoms/1177729694`, for relative entropy / symmetric discrimination context.

## Boundaries and falsification tests

- **The complete transcript law is still mandatory.** Tail control for an intermediate statistic is irrelevant unless every admitted downstream observation factors through it.
- **Average edge control is enough here; a worst-edge ceiling is not required.** This is weaker than `MC-352`, but it also permits a small collection of highly expensive source directions as long as the natural edge average satisfies the stated budget.
- **Convergence in probability alone is insufficient.** The binary family `(23)`–`(26)` has vanishing typical privacy loss and constant Jeffreys divergence.
- **A vanishing exceptional-set probability is therefore not an upper bound.** Its likelihood magnitude or another uniform-integrability currency must also be controlled.
- **Moment bounds are sufficient, not necessary.** Failure of a chosen fixed `L^p` bound does not prove that the tail budget is large; a different Orlicz/Rényi/direct-tail estimate may still control it.
- **Singular neighboring rows are deliberately expensive.** They give infinite KL and cannot be regularized away by declaring the singular set exceptional.
- **This remains a finite-source admission theorem.** It does not prove any natural Möbius coefficient architecture has vanishing edge privacy loss, a bounded moment envelope, or an upper tail estimate.
- **Large privacy-loss mass is necessary, not sufficient.** Spending the required edge divergence does not itself produce arithmetic cancellation or an estimate for `M(x)`.

## Research consequence

The reverse-sensitivity target can now be weakened without losing the obstruction. Instead of attempting the often unrealistic pure bound

\[
\sup_e\operatorname*{ess\,sup}|L_e|=o(1),
\]

a concrete Möbius/endpoint architecture may aim to prove

\[
U_R\to0\quad\text{in probability}
\]

under the natural source-edge mixture together with any genuine uniform-integrability certificate for the privacy loss—for example a fixed `L^p`, Rényi, exponential-moment, or direct exceptional-tail bound. If those estimates follow from coefficient precision, bandwidth, analytic regularity, or another independently available resource, `(7)` rules out fixed nontrivial bounded-energy dephasing.

Conversely, if an architecture survives, it must identify where the constant source-edge statistical tariff lives: typical contrast, exceptional tail probability times likelihood magnitude, or moment growth. That is a sharper diagnostic than the pure-likelihood ceiling of `MC-352` and is the next concrete affordability question for the reciprocal endpoint.