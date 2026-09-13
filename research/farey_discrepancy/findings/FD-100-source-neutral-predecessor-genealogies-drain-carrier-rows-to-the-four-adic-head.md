# FD-100 — source-neutral predecessor genealogies drain carrier rows to the four-adic head

**Status:** `EXACT-DERIVED + PREDECESSOR-GENEALOGY + SOURCE-QUOTIENT-INVARIANT + STRICT-ROW-POTENTIAL + FINITE-INVENTORY-CHARGE + FOUR-ADIC-HEAD-TERMINATION + FD099-CASCADE-COMPLETION + FALSE-RH-MATCHED-CONTROL + MASS-SELECTION-FRONTIER + NO-RH-CONTRADICTION`.

`FD-099` gives an important matched obstruction to interpreting horizon descent as source descent: for every fixed depth `m`, a false-RH source record `X` can support `m` exact `4/9` predecessor steps while the sampled source quotient remains identically `X`. The construction starts from row `9^m` and ends after the displayed odd-prime-square repairs at row `4^m`. This shows that arbitrarily much multiplicative horizon descent can be prepaid by repeated-square inventory.

There is, however, a second structural fact hidden in the same predecessor algebra. **Exact source-neutral inventory is finite once the carrier row is fixed.** On an exact carrier state

\[
H=rX,
\qquad r\ge4,
\qquad \mu(r)=0,
\tag{1}
\]

every non-head repair already available in `FD-091` and `FD-093` that preserves the source sample `X` replaces `r` by a strictly smaller nonsquarefree row `r'` satisfying

\[
\boxed{4\le r'\le \frac r2.}
\tag{2}
\]

Consequently the row potential

\[
\boxed{\mathfrak I(r):=\log_2\frac r4}
\tag{3}
\]

drops by at least one at every exact source-neutral predecessor step. Any such carrier genealogy therefore reaches the unique minimal nonsquarefree row `r=4` after at most

\[
\boxed{
\left\lceil\log_2\frac{r_0}{4}\right\rceil
}
\tag{4}
\]

steps. At `H=4X`, the next dyadic deflation is exactly the terminal `m=1` source-head atom of `FD-093`; there is no further non-head source-neutral repair.

Thus the repeated-prime inventory mentioned after `FD-099` **can be charged exactly at the coordinate-genealogy level**. What remains open is not whether one fixed source quotient can support an infinite exact carrier genealogy; it cannot. The real obstruction is lifting this row potential to the adaptive energy packets selected by the predecessor argument while retaining enough projective quality, and then accumulating the genuinely source-moving head steps whose guaranteed displacement is only additive (`FD-095`) or additive times a logarithmic factor (`FD-098`).

## 1. Exact carrier states remove every rounding ambiguity

The predecessor formulas in `FD-091` and `FD-093` contain ceilings and floors because a general physical horizon need not be divisible by the carrier row. To isolate the inventory question, consider the exact-divisor geometry already used by the matched construction of `FD-099`: fix an integer source argument `X>=1` and a nonsquarefree carrier row `r`, and put

\[
H=rX.
\tag{5}
\]

Then the carrier coordinate samples the source exactly:

\[
\left\lfloor\frac Hr\right\rfloor=X.
\tag{6}
\]

For this geometry all canonical predecessor horizons associated with that coordinate are integral, so the source-preservation question can be checked without asymptotic or transport error.

There are exactly three non-head repair types in the current decomposition.

### Odd repeated-prime repair

Suppose `p>=3` and

\[
p^2\mid r,
\qquad r=p^2t.
\tag{7}
\]

The first predecessor of `FD-091` is

\[
A_p=\left\lceil\frac Hp\right\rceil=ptX,
\tag{8}
\]

and the square reembedding gives

\[
C_p
=4\left\lfloor\frac{A_p}{p}\right\rfloor
=4tX.
\tag{9}
\]

The repaired row is

\[
r'=4t=\frac{4r}{p^2},
\tag{10}
\]

so

\[
C_p=r'X,
\qquad
\left\lfloor\frac{C_p}{r'}\right\rfloor=X.
\tag{11}
\]

Because `4|r'`, the child row is nonsquarefree. Since `p>=3`,

\[
\boxed{
\frac{r'}r=\frac4{p^2}\le\frac49<\frac12.
}
\tag{12}
\]

Thus an odd-square repair consumes source-neutral row potential by more than one binary unit.

### Dyadic eligible repair

Suppose `2|r` and the first dyadic child

\[
s=\frac r2
\tag{13}
\]

is still nonsquarefree. Since `H=rX` is even, the first dyadic predecessor in `FD-093` is exactly

\[
A=\left\lceil\frac H2\right\rceil=\frac H2=sX.
\tag{14}
\]

The same source value is therefore sampled on row `s`:

\[
\left\lfloor\frac As\right\rfloor=X.
\tag{15}
\]

Here

\[
\boxed{r'=s=\frac r2.}
\tag{16}
\]

This is the least contracting non-head source-neutral move, and it drops `mathfrak I` by exactly one.

### Dyadic terminal non-head repair

The remaining dyadic case from `FD-093` has

\[
r=4m,
\qquad m>1\text{ odd and squarefree}.
\tag{17}
\]

Choose the deterministic odd prime `p|m` used by that finding and write

\[
m=pt.
\tag{18}
\]

The second dyadic deflation is now exact:

\[
B=\frac H4=mX,
\tag{19}
\]

and the terminal repair gives

\[
C_p
=4\left\lfloor\frac Bp\right\rfloor
=4tX.
\tag{20}
\]

Its row is

\[
r'=4t=\frac rp,
\tag{21}
\]

again with exact source quotient `X`. Since `p>=3`,

\[
\boxed{
\frac{r'}r=\frac1p\le\frac13.
}
\tag{22}
\]

These three formulas exhaust the non-head source-neutral repair mechanisms presently proved.

## 2. The binary row potential is a strict Lyapunov function

Equations (12), (16), and (22) imply the common estimate

\[
4\le r'\le\frac r2
\tag{23}
\]

whenever the repair remains in the nonsquarefree sector and avoids the source head. Therefore

\[
\mathfrak I(r')
=\log_2\frac{r'}4
\le
\log_2\frac r4-1
=\mathfrak I(r)-1.
\tag{24}
\]

No prime-factor bookkeeping is needed: `log_2(r/4)` already charges every odd-square repair, every eligible dyadic deflation, and every dyadic terminal non-head repair in the same currency.

Iterating (24), a source-neutral genealogy starting from row `r_0` has length at most

\[
\left\lceil\mathfrak I(r_0)\right\rceil
=
\left\lceil\log_2\frac{r_0}{4}\right\rceil
\tag{25}
\]

before reaching the smallest possible nonsquarefree row. Since the only nonsquarefree integer below `5` is `4`, termination occurs at

\[
r_*=4,
\qquad H_*=4X.
\tag{26}
\]

Now apply the dyadic decomposition once more. The row `4` becomes the row `2` at horizon `2X`; that row is squarefree, so it enters the terminal channel. The second deflation reaches `B=X`, and the terminal parameter is exactly `m=1`. This is the unique source-head atom isolated in `FD-093`.

Hence

\[
\boxed{
\text{fixed source quotient }X
\quad\Longrightarrow\quad
\text{finite exact non-head genealogy ending at the four-adic head }4X.
}
\tag{27}
\]

This is a termination theorem for a **single exact carrier genealogy**. It is not yet a theorem that the mass-selected predecessor process must follow one carrier all the way to the head: the dominant packet may switch rows and source arguments between steps. That distinction is precisely where the current global problem survives.

## 3. The `FD-099` odd-square cascade can be drained completely

The row potential exposes an omitted continuation of the matched stress test in `FD-099`. There the exact source-neutral chain is

\[
q_j=4^j9^{m-j},
\qquad
H_j=q_jX,
\qquad
0\le j\le m,
\tag{28}
\]

and the first `m` steps use the odd repeated prime `p=3`:

\[
(q_j,H_j)
\longmapsto
\left(\frac49q_j,\frac49H_j\right).
\tag{29}
\]

After those steps one is at

\[
q_m=4^m=2^{2m},
\qquad
H_m=4^mX.
\tag{30}
\]

The construction does **not** stop there. As long as the current power of two is at least `8`, its dyadic half remains nonsquarefree. We may therefore append exactly

\[
2m-2
\tag{31}
\]

eligible dyadic predecessor steps,

\[
(2^kX,2^k)
\longmapsto
(2^{k-1}X,2^{k-1}),
\qquad
k=2m,2m-1,\ldots,3.
\tag{32}
\]

Every one of them keeps the sampled source value equal to `X`. The completed genealogy has

\[
\boxed{3m-2}
\tag{33}

exact source-neutral predecessor steps and ends at

\[
\boxed{(H,r)=(4X,4).}
\tag{34}

Thus the odd-square stock in `FD-099` does not create an indefinitely reusable source-neutral mechanism. The `p=3` repairs convert odd-square stock into a large dyadic exponent; the eligible dyadic steps then drain that exponent until the four-adic head is exposed.

The depth can nevertheless be arbitrarily large because the initial row itself can grow. Indeed

\[
3m-2
\asymp
\log q_0,
\qquad q_0=9^m,
\tag{35}
\]

which is close to the universal upper bound (25):

\[
\log_2\frac{9^m}{4}
=m\log_2 9-2
\approx3.17m-2.
\tag{36}
\]

So the row-potential estimate has the correct logarithmic scale and the `FD-099` family nearly saturates it.

## 4. The completed cascade retains the same false-RH quality scale

The extra dyadic tail does not require a new source-growth hypothesis. `FD-099` chooses, for each fixed `m`, a strict normalized source record `X` for which

\[
P_\sigma(9^mX)\le3^mP_\sigma(X)
\tag{37}
\]

and obtains the envelope

\[
|\mathcal H(y)|
\le
3^mA\left(\frac yX\right)^\sigma,
\qquad
A:=|\mathcal H(X)|,
\qquad
1\le y\le9^mX.
\tag{38}
\]

Every appended dyadic horizon lies in

\[
4X\le H\le4^mX\le9^mX,
\tag{39}
\]

so the same envelope controls its complete energy. With

\[
S_\sigma
:=
\sum_{r=2}^{\infty}
\frac{J_2(r)}{r^{2+2\sigma}}<\infty,
\tag{40}
\]

we retain

\[
E_{N,1}
\le
9^mS_\sigma A^2
\left(\frac NX\right)^{2\sigma}
\qquad(N\le9^mX).
\tag{41}
\]

At every dyadic state `H=2^kX` in (32), the row `2^k` samples `X` exactly and

\[
\frac{J_2(2^k)}{2^{2k}}=rac34.
\tag{42}
\]

Hence

\[
U_{H,1}\ge\frac34A^2.
\tag{43}
\]

For fixed `m`, (41)--(43) give the same qualitative conclusions as in `FD-099`: every appended state is frontier-sharp, has positive nonsquarefree occupation, and has bounded normalized-energy record defect, with constants at worst `exp(O_\sigma(m))`. On the diagonal choice `m->infinity`, `log X_m>=m^2`, those losses remain subpower because

\[
\exp(O(m))=X_m^{o(1)}.
\tag{44}
\]

Therefore even the **completed** source-neutral genealogy may have depth tending to infinity while every state retains the power-exponent quality used in `FD-097`--`FD-099`. What changes is the endpoint: once all carrier inventory has been charged, the chain is forced to expose the source head at `4X`.

## 5. What this removes, and what it does not

`FD-099` correctly rules out any argument saying that a positive density of multiplicative horizon contractions automatically implies source descent. The present finding refines the obstruction in the opposite direction: the contraction inventory is not inexhaustible at a fixed carrier. It is measured by the elementary row potential (3), and exact source-neutral repair cannot cycle because the row decreases by at least a factor `2` at every step.

This removes one overly broad version of the current frontier question. We do **not** need a mysterious prime-by-prime conservation law merely to prove that one fixed exact source carrier eventually runs out of repeated-prime stock. That part is already algebraically forced.

What remains genuinely nontrivial is the packet-level statement needed by the RH program. The predecessor theorem selects energy, not a tagged coordinate. Between steps it may move to a different carrier row or a different source quotient. To exploit (24) globally one needs a scale-sensitive quantity such as an energy-weighted row potential that survives the compression from many row-adaptive carriers to one physical predecessor, or another argument showing that frequent switches of carrier/source cannot preserve frontier-sharp projective quality indefinitely.

If a lineage does reach `r=4`, the remaining source progress is exactly the head problem already quantified in `FD-095` and `FD-098`: the guaranteed backward source motion is only

\[
X^{\Theta+o(1)}
\quad\text{or}\quad
X^{\Theta+o(1)}(\log X)^\kappa,
\tag{45}
\]

not a fixed fraction of `X`. Thus carrier-inventory termination by itself still gives no infinite descent contradiction.

A useful reformulation of the next target is therefore:

\[
\boxed{
\text{lift the strict coordinate potential }\log_2(r/4)
\text{ to the adaptive energy packet, or force sufficiently many genuine source-head/source-refresh events.}
}
\tag{46}
\]

The first route would convert the qualitative phrase “charge repeated-prime inventory” into an actual packet invariant. The second would bypass carrier genealogy and attack the slow additive source motion directly.

## 6. Adversarial checks and prior-art boundary

Several points were checked explicitly.

First, the factor `1/2` in (2) is sharp for the available repair algebra: a pure dyadic carrier `r=2^k`, `k>=3`, follows the eligible branch `r->r/2`. Hence no uniformly stronger contraction of row potential can be claimed.

Second, the terminal boundary is exact. At `r=4`, the first dyadic child is `2`, which is squarefree, and the second deflation is the `m=1` head. There is no missing nonsquarefree child below row `4` that could continue the source-neutral genealogy.

Third, this does not contradict the arbitrarily deep construction of `FD-099`. The depth bound depends logarithmically on the **initial row**, and that construction deliberately lets the initial row grow as `9^m`. Arbitrarily long finite genealogies and strict termination for each fixed carrier are fully compatible.

Fourth, the theorem is intentionally stated for exact carrier geometry `H=rX`. General predecessor packets include ceiling/floor transport and may switch carriers, so (27) is not promoted to a global termination theorem for the adaptive physical process. Doing so would silently assume the very coherence that remains open.

The prior-art audit included classical and recent Farey-discrepancy/Mertens literature, including the 2026 local-discrepancy work and current Mertens computation literature. Those sources concern discrepancy bounds, Möbius/Mertens size, or computation; they do not supply or analyze the internal predecessor-genealogy maps (10), (16), and (21). The proof above is therefore entirely internal to the exact identities already established in `FD-091`, `FD-093`, and `FD-099`; no new external source is load-bearing, so `SOURCES.md` does not require an update.
