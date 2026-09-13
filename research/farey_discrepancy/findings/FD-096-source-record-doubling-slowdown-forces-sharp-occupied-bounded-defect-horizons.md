# FD-096 — source-record doubling slowdown forces sharp occupied bounded-defect horizons

**Status:** `EXACT-DERIVED + SOURCE-RECORD-GROWTH + DYADIC-SLOWDOWN + FOUR-ADIC-CAUSAL-WINDOW + COMPLETE-SCHUR-DEFECT + FIXED-OCCUPATION + FALSE-RH-SHARP-SUBSEQUENCE + ONE-STEP-ENTRY-GATE-CLOSED`.

`FD-094` identifies the backward normalized Schur-energy record defect as the exact fixed-occupation loss in every repairable predecessor channel, and `FD-095` absorbs the remaining source-head branch under the same bounded-defect hypothesis. Their only first-order entry gate is therefore to produce a sharp occupied horizon `H` for which

\[
\mathfrak R_\sigma(H)=O(1)
\]

for one fixed `sigma in (1/2,Theta)`.

That gate is already forced by the physical source records from `FD-076`. The key observation is that a normalized source record cannot increase by a fixed factor larger than its allowed power growth on **every** doubling interval. Hence infinitely many strict source records `X` have bounded normalized growth from `X` to `2X`. At the four-adic horizon `H=4X`, every complete Schur row `r>=2` then samples the source at an argument at most `2X`, while the nonsquarefree row `r=4` samples the record value at `X` exactly. The same two-scale source envelope therefore gives, simultaneously,

\[
E_{H,1}=H^{2\Theta+o(1)},
\qquad
\frac{U_{H,1}}{E_{H,1}}\gg_{\sigma}1,
\qquad
\mathfrak R_\sigma(H)\ll_{\sigma}1.
\]

Thus the remaining one-step entry gate of `FD-095` closes under false RH. The live frontier moves to **growing-depth composition**: the predecessor constants may still deteriorate from step to step, so no infinite descent is claimed.

## 1. A source record cannot grow too fast on every doubling interval

Assume

\[
\Theta>\frac12
\]

and fix

\[
\frac12<\sigma<\Theta.
\tag{1}
\]

For the physical source `mathcal H`, write

\[
Q_\sigma(n):=\frac{|\mathcal H(n)|}{n^\sigma},
\qquad
P_\sigma(X):=\max_{1\le n\le X}Q_\sigma(n).
\tag{2}
\]

A **strict source `sigma`-record** is an integer `X` with

\[
Q_\sigma(X)=P_\sigma(X)>P_\sigma(X-1).
\tag{3}
\]

`FD-076` proves both that such records are power-dense and that every sufficiently large strict record is sharp:

\[
|\mathcal H(X)|=X^{\Theta+o(1)}.
\tag{4}
\]

The global source frontier from `FD-046` also gives, for every fixed `tau>Theta`,

\[
|\mathcal H(n)|\ll_\tau n^\tau,
\qquad
P_\sigma(Y)\ll_\tau Y^{\tau-\sigma}.
\tag{5}
\]

Now fix any constant

\[
K>2^{\Theta-\sigma}.
\tag{6}
\]

Choose `tau` so that

\[
\Theta<\tau<\sigma+\log_2K.
\tag{7}
\]

Suppose, for contradiction, that every sufficiently large strict record `X` satisfies

\[
P_\sigma(2X)>K P_\sigma(X).
\tag{8}
\]

Starting from one such record `X_0`, equation (8) forces another strict record

\[
X_1\in(X_0,2X_0]
\]

with

\[
P_\sigma(X_1)>K P_\sigma(X_0).
\]

Iterating produces strict records `X_j` with

\[
X_j\le2^jX_0,
\qquad
P_\sigma(X_j)>K^jP_\sigma(X_0).
\tag{9}
\]

But (5) gives

\[
K^jP_\sigma(X_0)
< P_\sigma(X_j)
\ll_\tau (2^jX_0)^{\tau-\sigma}.
\tag{10}
\]

Since `K>2^(tau-sigma)` by (7), (10) fails as `j->infinity`. Therefore

\[
\boxed{
\liminf_{\substack{X\to\infty\\X\;\mathrm{strict\ }\sigma\mathrm{-record}}}
\frac{P_\sigma(2X)}{P_\sigma(X)}
\le 2^{\Theta-\sigma}.
}
\tag{11}
\]

In particular, because `Theta<=1` and `sigma>1/2`, one has `Theta-sigma<1/2`, so there are infinitely many strict records satisfying the convenient uniform bound

\[
\boxed{
P_\sigma(2X)\le2P_\sigma(X).
}
\tag{12}
\]

No short-interval theorem is used here. Equation (12) is forced only by the global source power frontier and the impossibility of multiplying a running record by more than its admissible power growth on every factor-two step.

## 2. Slow doubling controls every complete Schur row below `4X`

Take one of the strict records from (12), set

\[
A:=|\mathcal H(X)|,
\qquad
H:=4X,
\tag{13}
\]

and, more generally, retain a fixed bound

\[
P_\sigma(2X)\le K P_\sigma(X)
\tag{14}
\]

with `K=O(1)`. Since `X` is a strict record,

\[
P_\sigma(X)=\frac{A}{X^\sigma}.
\]

Thus every integer `1<=y<=2X` obeys the two-scale source envelope

\[
\boxed{
|\mathcal H(y)|
\le
K A\left(\frac yX\right)^\sigma.
}
\tag{15}
\]

Recall

\[
E_{N,1}
=
\sum_{1<r\le N}
 w(r)\,
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)^2,
\qquad
w(r):=\frac{J_2(r)}{r^2},
\tag{16}
\]

and define the convergent constant

\[
S_\sigma
:=
\sum_{r=2}^{\infty}\frac{w(r)}{r^{2\sigma}}
<\infty,
\tag{17}
\]

where convergence is exactly where `sigma>1/2` enters.

For every `N<=4X` and every row `r>=2` occurring in (16),

\[
\left\lfloor\frac Nr\right\rfloor\le2X.
\]

Applying (15) row by row gives

\[
\begin{aligned}
E_{N,1}
&\le
K^2A^2
\sum_{2\le r\le N}
 w(r)
\left(\frac{N}{rX}\right)^{2\sigma}\\
&\le
\boxed{
K^2S_\sigma A^2
\left(\frac NX\right)^{2\sigma}.
}
\end{aligned}
\tag{18}
\]

Hence, with

\[
F_\sigma(N):=\frac{E_{N,1}}{N^{2\sigma}},
\]

one has uniformly throughout the entire backward history up to `H=4X`,

\[
\boxed{
F_\sigma(N)
\le
K^2S_\sigma\frac{A^2}{X^{2\sigma}}
\qquad(2\le N\le H).
}
\tag{19}
\]

This is the complete-head estimate that was missing after `FD-095`. A source record at `X` alone only controls source arguments up to `X`; the bounded doubling step (14) extends the envelope exactly far enough to cover the smallest Schur row `r=2` all the way to the four-adic horizon `4X`.

## 3. Row four supplies occupation and the denominator for the record defect

At `H=4X`, the row `r=4` is nonsquarefree and samples the source record exactly:

\[
\left\lfloor\frac H4\right\rfloor=X,
\qquad
w(4)=\frac{J_2(4)}{4^2}=\frac34.
\tag{20}
\]

Therefore

\[
U_{H,1}
\ge\frac34A^2,
\qquad
E_{H,1}
\ge\frac34A^2,
\tag{21}
\]

while (18) at `N=H` gives

\[
E_{H,1}
\le
K^2 4^{2\sigma}S_\sigma A^2.
\tag{22}
\]

The nonsquarefree occupation is consequently bounded below by the fixed constant

\[
\boxed{
\frac{U_{H,1}}{E_{H,1}}
\ge
\frac{3}
{4K^2 4^{2\sigma}S_\sigma}
=:c_{\sigma,K}>0.
}
\tag{23}
\]

More importantly, (21) gives

\[
F_\sigma(H)
\ge
\frac34\frac{A^2}{(4X)^{2\sigma}}.
\tag{24}
\]

Combining (19) and (24) with the definition from `FD-094`,

\[
\mathfrak R_\sigma(H)
:=
\max\!\left\{
1,
\sup_{2\le N<H}
\frac{F_\sigma(N)}{F_\sigma(H)}
\right\},
\]

produces

\[
\boxed{
\mathfrak R_\sigma(H)
\le
\frac{4K^2 4^{2\sigma}S_\sigma}{3}
=:C_{\sigma,K}<\infty.
}
\tag{25}
\]

The constants in (23) and (25) are reciprocal with this normalization. For the infinite record subsequence supplied by (12), one may simply take `K=2`, so both constants depend only on the chosen `sigma`.

Finally, (4), (21), and (22) show that these same horizons are sharp:

\[
\boxed{
E_{H,1}=H^{2\Theta+o(1)}.
}
\tag{26}
\]

Thus false RH produces infinitely many horizons satisfying all three requirements simultaneously:

\[
\boxed{
E_{H,1}=H^{2\Theta+o(1)},
\qquad
\frac{U_{H,1}}{E_{H,1}}\ge c_\sigma>0,
\qquad
\mathfrak R_\sigma(H)\le C_\sigma.
}
\tag{27}
\]

This is stronger than intersecting the independently constructed occupied blocks of `FD-083`--`FD-084` with Schur-energy records. It constructs the required occupied bounded-defect states directly from a subsequence of the source records.

## 4. The first-order composition gate of `FD-095` is closed

Equation (27) is exactly the hypothesis left open by the one-step closure theorem of `FD-095`. For every sufficiently large horizon in the selected sequence, the repeated-prime predecessor decomposition therefore produces some genuine lower physical state `C<H` which is again

\[
E_{C,1}=C^{2\Theta+o(1)},
\qquad
\frac{U_{C,1}}{E_{C,1}}\gg1,
\qquad
\mathfrak R_\sigma(C)=O(1).
\tag{28}
\]

This conclusion covers all currently possible branches: odd-prime square reembedding, the already-eligible dyadic half-scale branch, the repaired dyadic nonhead branch, and the amplitude-scale source-head backstep of `FD-095`.

Consequently the old frontier

\[
\text{``find a sharp occupied packet with bounded record defect''}
\]

is no longer an independent research gate. Under a false-RH frontier, such packets exist infinitely often by (27), and each admits at least one lower sharp occupied bounded-defect continuation by (28).

There is also a safe finite-depth consequence. For every **fixed** integer `m`, one may start sufficiently far along the sequence (27) and apply the one-step closure `m` times. The occupation and defect constants may depend badly on `m`, but they remain finite positive constants for fixed `m`, and every intermediate scale still tends to infinity with the starting horizon. Thus the present mechanism already gives arbitrarily long *fixed-depth* predecessor chains.

It does **not** give a chain whose depth tends to infinity with the starting scale. That distinction is now the main composition frontier.

## 5. Why the factors `2` and `4` are structural

The construction exposes a useful causal mismatch. At horizon `2X`, a source record at `X` controls the complete Schur history automatically because the smallest row `r=2` never samples beyond `X`. But the row that carries the record value there is `r=2`, which is squarefree and therefore does not certify nonsquarefree occupation.

The first universally available nonsquarefree row is `r=4`. Moving the horizon to `4X` places the record value on that row, but the complete Schur head now reaches source arguments as far as `2X` through row `r=2`. The single additional input needed to bridge this causal gap is precisely the bounded source-record growth

\[
P_\sigma(2X)\ll P_\sigma(X).
\]

Section 1 shows that the source power frontier itself forces infinitely many record times with this property. In that sense the factor-two source slowdown and the four-adic occupation witness are matched exactly; there is no leftover scalar-density intersection problem.

The restriction `sigma>1/2` is also real. At `sigma=1/2`, the series `S_sigma` in (17) has harmonic-size divergence, so this argument loses a logarithm and no fixed bound for `mathfrak R_sigma(H)` follows. The result therefore lives naturally in the same false-RH interval `1/2<sigma<Theta` already used by `FD-094`--`FD-095`.

## 6. Remaining boundary and prior-art audit

The result closes the **entry** problem, not the full recursive contradiction. The inherited constants in `FD-094`--`FD-095` can deteriorate at every predecessor step. In particular, a head backstep may decrease the horizon only by `H^(Theta-o(1))`, while other branches may contract multiplicatively. To obtain an actual infinite descent or a contradiction one now needs a depth-uniform invariant, a quantitative re-recording mechanism, or a proof that the accumulated occupation/defect losses cannot grow fast enough along a long chain.

The slow-doubling lemma is deliberately a statement about normalized **source** records. It does not say that complete Schur-energy records themselves have bounded multiplicative gaps, nor does it identify every occupied horizon with a record. Its role is narrower and sufficient: source records create a special four-adic subsequence on which complete Schur occupation and historical denominator control coexist.

A targeted prior-art audit covered recent Farey local-discrepancy work, current Mertens computations, and the Mertens maximal-order result already used in `FD-076`. No located source states this Mathia-specific coupling between normalized source-record growth, the `X -> 2X` causal envelope, four-adic nonsquarefree embedding, and backward complete-Schur record defect. The only external load-bearing input remains Pintz's fixed-power-window Mertens maximal-order theorem through `FD-076`, and that dependency is already recorded in `SOURCES.md`; no source-file update is required here.

The falsification boundary is explicit. If one drops `sigma>1/2`, the row sum in (17) ceases to be uniformly summable. If one moves to `4X` without a bound such as (14), rows `2` and `3` escape the source record and can dominate the complete denominator. If one keeps only `2X`, the record sits on the squarefree row `2` and does not provide the required nonsquarefree occupation. The gain is exactly the simultaneous resolution of those three constraints on an infinite false-RH subsequence.