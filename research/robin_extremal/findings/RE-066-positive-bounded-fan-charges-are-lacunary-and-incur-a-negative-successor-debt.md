# RE-066 — positive bounded fan charges are lacunary and incur a negative successor debt

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + BOUNDED-EVENT-PACKET + SIGNED-CHARGE-CLASSIFICATION + LACUNARY-POSITIVE-CHARGE + NEGATIVE-SUCCESSOR-DEBT + POLYNOMIAL-INTERRUPTION-LEDGER + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-065` proves that a polynomial-span strong-off-critical fan cannot carry its polynomial exposed complexity through long runs of bounded source-bearing packets whose normalized charges vanish. It therefore leaves three interruption currencies: unbounded packet cardinality, packets with no higher-layer source event, and nonvanishing normalized charge. The last currency still looks sign-symmetric in that formulation. The layer-uniform charge law of `RE-062` and the fringe-host rigidity of `RE-063` show that it is not.

Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on sufficiently late common positive CA counterexample blocks from `RE-040`. Fix a packet-cardinality bound `K`. For a rightmost-fan switch between consecutive exposed states

\[
C_-<C_+,
\qquad
Y_\pm:=\log C_\pm,
\qquad
Y:=Y_-,
\tag{2}
\]

assume that the complete physical packet has at most `K` event occurrences and contains at least one higher-layer occurrence. Let

\[
s:=\sum_i\frac1{j_i}>0
\tag{3}
\]

be the reciprocal-depth mass of those higher-layer occurrences, let `\chi_\pm\in\{0,1\}` be the endpoint fringe bits, and use the normalized selected-residual charge

\[
Q:=
\frac{b\sqrt Y}{\log Y}
\left(
\mathcal R_b(Z_+)-\mathcal R_b(Z_-)
\right).
\tag{4}
\]

By `RE-062`, uniformly over all such packets,

\[
\boxed{
Q=-s+\chi_+-\chi_-+\rho_{J,K}(Y),
\qquad
\rho_{J,K}(Y)\longrightarrow0.
}
\tag{5}
\]

The sign asymmetry is then rigid.

For every fixed `epsilon>0`, every sufficiently late bounded source-bearing switch satisfying

\[
Q\ge\epsilon
\tag{6}
\]

must have

\[
\boxed{
\chi_-=0,
\qquad
\chi_+=1,
\qquad
s\le1-\frac\epsilon2.
}
\tag{7}
\]

Consequently its upper state is one of the nonzero-fringe hosts classified in `RE-063`. If `N^+_{K,\epsilon}(T)` counts distinct such positive-charge switches whose upper physical state scale satisfies `Y_+\le T`, then

\[
\boxed{
N^+_{K,\epsilon}(T)=O_{J,K,\epsilon}(\log T).
}
\tag{8}
\]

Their upper-state scales are multiplicatively lacunary: ordered by scale, every fixed `q<2` is eventually a lower bound for the ratio of successive scales.

There is also a deterministic one-step repayment law. Suppose a switch satisfying (6) is not terminal in the exposed fan, so its upper state `C_1` owns a nonempty threshold cell before the next exposed switch. If the next physical packet is again bounded by `K` and source-bearing, then its normalized charge obeys

\[
\boxed{
Q_{\rm next}\le-1+o_{J,K}(1).
}
\tag{9}
\]

Thus a positive bounded source-bearing charge cannot propagate through a bounded source-bearing fan. It creates a nonzero-fringe upper state, that fringe persists across the state's exposed cell, and the next bounded source-bearing packet must leave that state with fringe pattern `1 -> 0`; its charge therefore carries a negative unit before any reciprocal-depth contribution is counted.

Finally this sharpens the interruption alternative of `RE-065`. In its strong off-critical polynomial-span setting, choose any positive threshold `epsilon_X->0` satisfying

\[
\sup_{Y\ge X}|\rho_{J,K}(Y)|=o(\epsilon_X).
\tag{10}
\]

Let `H_B` count fan switches in the block whose physical packet either has cardinality `>K` or contains no higher-layer event. Let `N^-_B` count the remaining bounded source-bearing switches with

\[
Q<-\epsilon_{X_B}.
\tag{11}
\]

Then, with the exponent `delta>0` from `RE-051` and `RE-065`, every polynomial-span block satisfies

\[
\boxed{
H_B+N^-_B
\ge
X_B^{\delta-o(1)}.
}
\tag{12}
\]

Positive nonquiet charge contributes only `O(\log X_B)` switches and is swallowed by the error term. Hence **polynomial fan complexity cannot be carried by positive bounded charge.** On polynomial physical spans, the surviving alternatives reduce to polynomially many structural interruptions (large packets or first-layer-only packets), polynomially many genuinely negative bounded source-bearing charges, or a mixture of the two. If this ledger is avoided, the already identified escape remains superpolynomial fan stretch.

## 1. A positive bounded charge forces the unique fringe transition `0 -> 1`

For fixed `epsilon>0`, take the packet sufficiently late that

\[
|\rho_{J,K}(Y)|\le\frac\epsilon2.
\tag{13}
\]

If `\chi_+-\chi_-\le0`, then (5) and `s>0` give

\[
Q<\frac\epsilon2,
\]

contradicting (6). Since the fringe difference belongs to `{-1,0,1}`, necessarily

\[
\chi_+-\chi_-=1,
\]

which is exactly the first two assertions of (7). Substituting them back into (5),

\[
\epsilon
\le
1-s+\rho_{J,K}(Y)
\le
1-s+\frac\epsilon2,
\]

and hence `s<=1-epsilon/2`.

This is stronger than merely saying that positive charge needs a fringe correction. The lower endpoint must be completely matched and the upper endpoint must carry the unique unmatched ordinary prime. No `0 -> 0`, `1 -> 0`, or `1 -> 1` bounded source-bearing packet can have a positive charge bounded away from zero.

## 2. Positive charges inherit the base-two lacunarity of fringe hosts

By (7), the upper state of every positive switch has fringe bit one at its breakpoint. `RE-063` applies to **every** selected state with nonzero fringe correction, independently of the transition by which the fan entered it. It proves that the immediate physical successor of that upper state is one unique deep base-two event

\[
\xi=\eta_{2,j},
\qquad j\to\infty,
\tag{14}
\]

and that distinct fringe hosts inject into distinct base-two depths. Moreover

\[
N_{\rm fr}(T)=O(\log T),
\qquad
\liminf\frac{\xi_{n+1}}{\xi_n}\ge2,
\tag{15}
\]

while the selected state scale satisfies `Y_+~xi`.

The upper states attached to distinct fan switches are distinct exposed states, so positive switches inject into this same host family. Equations (14)--(15) immediately prove (8) and the lacunarity statement.

This count is much smaller than the polynomial fan complexity forced by `RE-051`. It does not use a prime-gap density theorem: the sparsity comes from the single fixed base `2` forced by the physical fringe/event mismatch.

## 3. The fringe produced by a positive switch persists to the next breakpoint

Let the positive switch occur at threshold `beta`, with upper exposed state `C_1`, and let `xi` be the immediate outgoing physical event of `C_1`. By `RE-063`, its nonzero fringe is represented by one ordinary prime `r` with

\[
r\le Z_{C_1}(\beta)<\xi\le\eta_{r,1}.
\tag{16}
\]

Suppose `C_1` owns a nonempty exposed threshold cell `(beta,beta')` and participates as the lower tied state at the next breakpoint `beta'`. For one fixed exposed state, `RE-046` gives the exact selector monotonicity

\[
\frac{d}{db}Z_{C_1}(b)>0.
\tag{17}
\]

At the same time every regular selector belonging to `C_1` remains inside its fixed physical CA support chamber, hence

\[
Z_{C_1}(b)<\xi
\qquad(beta\le b\le beta').
\tag{18}
\]

Combining (16)--(18),

\[
r\le Z_{C_1}(\beta)
<Z_{C_1}(\beta')
<\xi
\le\eta_{r,1}.
\tag{19}
\]

Therefore the same fringe atom is still unmatched when `C_1` appears as the lower state of the next switch:

\[
\boxed{\chi_-^{\rm next}=1.}
\tag{20}
\]

This persistence is the bridge that turns the static lacunarity of `RE-063` into a signed dynamical constraint.

## 4. A bounded source-bearing successor repays at least one negative unit

Assume the next physical packet has cardinality at most `K` and contains at least one higher-layer event. `RE-064` excludes the endpoint pattern `(1,1)` for every sufficiently late bounded packet. Together with (20), this forces

\[
\boxed{
\chi_-^{\rm next}=1,
\qquad
\chi_+^{\rm next}=0.
}
\tag{21}
\]

Applying the uniform charge law (5) to the next packet gives

\[
Q_{\rm next}
=-s_{\rm next}-1+\rho_{J,K}(Y_{\rm next}),
\qquad
s_{\rm next}>0.
\tag{22}
\]

Hence (9). In fact the leading charge is strictly below `-1` by the reciprocal-depth mass; the stated bound keeps only the uniform information needed for the aggregate ledger.

This extends the one-step negative rebound proved in `RE-064` after an asymptotically cancelling Egyptian packet. No Egyptian resonance and no assumption `Q->0` are needed: **every genuinely positive bounded source-bearing charge creates the same successor debt.**

## 5. The polynomial interruption ledger loses its positive branch

Use the strong-off-critical setting of `RE-065`: fix a prime short-interval exponent `theta` with `Theta>theta`, a compact

\[
J=[b_0,b_1]\Subset(1-\Theta,1-\theta),
\qquad
\delta:=1-b_1-\theta>0,
\tag{23}
\]

and restrict to blocks with physical fan span

\[
W_B\le X_B^A
\tag{24}
\]

for one fixed `A`. `RE-065` gives polynomially many switches that are not quiet source-bearing:

\[
B_B\ge X_B^{\delta-o(1)}.
\tag{25}
\]

Because the remainder in (5) is uniform for fixed `J,K`, one may choose a deterministic `epsilon_X->0` with (10), for example any monotone majorant asymptotically larger than the square root of that remainder modulus. Apply the `RE-065` definition of quietness with this `epsilon_X`.

Every nonquiet switch counted by `B_B` either belongs to `H_B`, or is bounded and source-bearing with `|Q|>epsilon_{X_B}`. For sufficiently late blocks, the positive members of the latter class satisfy the same `0 -> 1` conclusion as in Section 1 because the remainder is `o(epsilon_X)`. By Section 2 their number is

\[
O(\log W_B)=O_A(\log X_B).
\tag{26}
\]

All other bounded source-bearing nonquiet switches satisfy (11). Therefore

\[
B_B
\le
H_B+N^-_B+O_A(\log X_B).
\tag{27}
\]

Combining (25)--(27) proves (12).

The conclusion is deliberately a ledger, not a contradiction. It does not bound `H_B`, and negative charges at different breakpoints are evaluated with different threshold parameters and square-root normalizations, so they cannot simply be telescoped without controlling the within-cell drift. What is removed is the sign-symmetric escape: **positive normalized charge is too lacunary to account for the polynomial interruption count.** Any successful aggregate-charge argument should therefore target the negative branch and the continuous change of the residual along exposed cells, while any purely combinatorial argument must control the structural interruption count `H_B`.

## 6. Stress tests and prior-art boundary

The proof does not assume that the packet spectrum is fixed. The only packet restriction used in (5) is the fixed cardinality bound `K`, exactly the layer-uniform regime of `RE-062`. It also does not assume an adjacent first-layer entry into a fringe host; `RE-063` deliberately removed that hypothesis. Ties are already counted as event occurrences in the physical packet convention used by `RE-061`--`RE-065`.

The successor statement requires the next packet to remain bounded and source-bearing. If packet cardinality becomes unbounded, or if the next packet contains only first-layer events, that switch returns to the structural interruption class `H_B` rather than being assigned a charge by (5). Terminal positive switches likewise need no successor repayment, but there are only the already lacunary number of possible positive hosts.

A targeted prior-art search for colossally abundant transition packets, Robin extremality, prime-power event layers, and signed residual increments found the classical Alaoglu--Erdos transition structure, recent work on consecutive CA quotients, and Mantovanelli's 2026 prime-layer packet/workload formalism already represented in `SOURCES.md`. Those sources provide the surrounding CA/event bookkeeping but not the adaptive false-RH charge law, the fringe-host base-two lock, or the signed `0 -> 1`/`1 -> 0` pairing used here. No new external theorem is load-bearing, so `SOURCES.md` requires no update.

## Consequence

`RE-065` reduced a polynomial-span false-RH fan to polynomially many interruptions unless the fan stretches superpolynomially. `RE-066` removes one apparent degree of freedom from those interruptions: **positive bounded source-bearing charge is logarithmically sparse and, whenever the next switch remains in the same bounded source-bearing regime, is followed by a charge at most `-1+o(1)`.**

The remaining polynomial burden on a fixed physical span is therefore carried by structural interruptions (`>K` events or no higher-layer source event), genuinely negative bounded source-bearing charges, or both. The next useful theorem should control one of those two currencies or quantify the within-cell residual drift needed to compensate the forced negative charge ledger.