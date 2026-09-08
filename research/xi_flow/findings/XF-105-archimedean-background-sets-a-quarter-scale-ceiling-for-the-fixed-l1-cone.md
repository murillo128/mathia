# XF-105 — archimedean background sets a quarter-scale ceiling for the fixed l1 cone

**Status:** `EXACT-DERIVED` + `INTERFACE-BOUNDARY` + `METHOD-OBSTRUCTION` + `ARCHIMEDEAN-CEILING`. XF-104 showed that the prime-enriched Vieta interface remains transition-nonidentifying on a fixed positive fraction of the natural arithmetic scale by keeping its normalized raw moment mass inside the fixed-margin cone of XF-085. The constant hidden in that fraction cannot be pushed arbitrarily far by sharpening the prime estimate or optimizing the bump. The deterministic endpoint background alone eventually fills the available fixed `ell^1` margin.

Keep the XF-104 scales

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\tag{1}
\]

and the same distribution-safe prime-enriched moments

\[
Q_m^\psi
=
B(m\Delta)
-
\frac1{2\Delta}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right),
\qquad
\lambda_n=\frac12\log n,
\tag{2}
\]

for `1<=m<=K=floor(L/Delta)`, where `psi` is fixed and supported in `[-1,1]`. If

\[
L=\log a+c
\tag{3}
\]

with fixed `c in R`, then independently of the size or detailed placement of the prime-power term,

\[
\boxed{
\frac1N\sum_{m\le K}|Q_m^\psi|
\ge e^c-o(1).
}
\tag{4}
\]

Consequently the fixed-margin sufficient condition used by XF-085,

\[
2\sum_{m\le K}|Q_m^\psi|\le(1-\kappa)N,
\qquad \kappa>0\text{ fixed},
\tag{5}
\]

is impossible whenever

\[
c\ge \log\frac{1-\kappa}{2}+o(1).
\tag{6}
\]

In particular, after allowing any fixed positive margin `kappa`, this entire `ell^1`/Gershgorin realization mechanism cannot reach

\[
\boxed{
L\ge\log a-\log2+o(1).
}
\tag{7}
\]

Since the mesh state contains the complete prime-power contribution through `n<=exp(2L-2Delta)`, the limiting boundary `(7)` corresponds to

\[
\boxed{
 n\le \left(\frac14+o(1)\right)a^2.
}
\tag{8}
\]

Thus XF-104 is qualitatively optimal for the **fixed raw-`ell^1` cone**: it can reach a nonvanishing fraction of `a^2 asymp q`, but no argument that retains the same fixed-margin condition can be extended through the full natural `a^2` arithmetic scale. Crossing this boundary requires a less lossy moment-feasibility mechanism, such as the Toeplitz/Caratheodory route left open by XF-084, rather than a better estimate of the prime mass inside the same cone.

## 1. Away from prime mesh cells the target is exactly the archimedean background

XF-052 gives

\[
B(\xi)
=e^\xi+e^{-\xi}-\frac{e^{-\xi}}{1-e^{-4\xi}}
=
\boxed{
e^\xi-\frac{e^{-5\xi}}{1-e^{-4\xi}}.
}
\tag{9}
\]

Let `E` be the set of mesh indices `1<=m<=K` on which the atomic term in `(2)` can be nonzero. Because `supp psi subset [-1,1]`, every prime-power atom affects at most three integer mesh sites. Moreover an atom affecting the visible prefix must satisfy

\[
\lambda_n\le L+\Delta,
\qquad
n\le e^{2(L+\Delta)}.
\tag{10}
\]

Without using the prime number theorem, or even Chebyshev, the trivial fact that prime powers are integers therefore gives

\[
\boxed{
|E|\le 3e^{2(L+\Delta)}=O_c(a^2).
}
\tag{11}
\]

For every `m notin E`, the source target is exactly

\[
Q_m^\psi=B(m\Delta).
\tag{12}
\]

This exact untouched set is the key point. The prime atoms may be individually large, but at the `L=log a+O(1)` scale they occupy only a vanishing fraction of the `K asymp Delta^{-1}log a` mesh cells. They therefore cannot erase the raw absolute mass carried by the smooth background on the remaining cells.

## 2. The untouched background has normalized mass `e^c+o(1)`

Restrict first to `m\Delta>=1`. On that half-line `(9)` is positive and

\[
B(m\Delta)
=e^{m\Delta}+O(e^{-5m\Delta}).
\tag{13}
\]

The full background sum there is a geometric sum:

\[
\begin{aligned}
\sum_{1\le m\Delta\le L}B(m\Delta)
&=
\sum_{1\le m\Delta\le L}e^{m\Delta}
+O(\Delta^{-1})\\
&=
\frac{e^L}{\Delta}(1+o(1)).
\end{aligned}
\tag{14}
\]

The amount lost by deleting the atom-affected cells is much smaller. Since `B(\xi)<=e^\xi` for `\xi>0`, equations `(3)` and `(11)` give

\[
\sum_{\substack{m\in E\\m\Delta\ge1}}B(m\Delta)
\le |E|e^L
=O_c(e^{3L}).
\tag{15}
\]

Relative to the main term in `(14)`, this costs

\[
\frac{e^{3L}}{e^L/\Delta}
=O_c(e^{2L}\Delta)
=O_c(a^2\Delta).
\tag{16}
\]

But `(1)` implies

\[
a^2\Delta
=(N\Delta)^2\Delta
=4q^4\Delta^3
=O(q^{-1/2})
\longrightarrow0.
\tag{17}
\]

Hence the background surviving on untouched cells still obeys

\[
\sum_{\substack{m\le K\\m\notin E}}|Q_m^\psi|
\ge
\sum_{\substack{1\le m\Delta\le L\\m\notin E}}B(m\Delta)
=
\frac{e^L}{\Delta}(1-o(1)).
\tag{18}
\]

Using `N=a/Delta` and `(3)` proves `(4)`:

\[
\frac1N\sum_{m\le K}|Q_m^\psi|
\ge
\frac{e^L}{a}(1-o(1))
=e^c-o(1).
\tag{19}
\]

No cancellation estimate between the archimedean and prime sectors enters. The proof deliberately discards every mesh cell on which such cancellation could occur.

## 3. The same one-half boundary appears in the static and dynamic arguments

XF-085 realizes the target by exactly `N` equal-weight unit-circle nodes whenever `(5)` holds. Writing

\[
S(0):=\frac1N\sum_{m\le K}|Q_m^\psi|,
\tag{20}
\]

that sufficient condition is simply

\[
S(0)\le\frac{1-\kappa}{2}.
\tag{21}
\]

Combining `(19)` and `(21)` gives `(6)`. If `L=log a-log2+o(1)`, then `S(0)>=1/2-o(1)`, so `(21)` fails for every fixed `kappa>0` once the scale is large enough. Equation `(8)` follows from the complete-band relation already used in XF-104,

\[
X_{\rm full}=e^{2(L-\Delta)}.
\tag{22}
\]

The same threshold is also exactly where the forward-invariant `ell^1` argument of XF-102--XF-104 loses its fixed interior. Their Dini inequality is

\[
D^+S
\le
\bigl[-(a-L)+2aS\bigr]D.
\tag{23}
\]

A scale-independent inward-pointing cone requires `S<=1/2-delta` for some fixed `delta>0`, because `L/a->0`. But `(19)` places the endpoint state at `S(0)>=1/2-o(1)` as soon as `(7)` is reached. Therefore both pieces of the XF-104 mechanism -- exact equal-weight realization by the explicit positive-density cone and preservation of that cone under periodic heat -- encounter the same deterministic one-half mass wall.

This coincidence does **not** prove that the moment trajectory must leave every realizable set. It proves that the particular fixed raw-`ell^1` interior used in XF-085 and XF-102--XF-104 has reached its natural endpoint.

## 4. Stress tests and evidence boundary

The result does not assume prime sparsity in any analytic-number-theory sense. The bound `(11)` uses only that there are at most `e^{2(L+Delta)}` integers below the arithmetic cutoff. At `L=log a+O(1)` this is enough because `a^2 Delta->0`. Prime clustering, prime powers landing unusually close in frequency, or destructive cancellation at the affected cells cannot weaken `(18)`, since all affected cells are removed before taking the lower bound.

The constant `1/4` in `(8)` belongs to the **current `ell^1` sufficient cone**, not to the underlying equal-weight moment problem. XF-084 requires only Toeplitz positive semidefiniteness for a weighted representing measure, and many realizable moment vectors lie far outside the Gershgorin condition. Gilboa--Peled's quadrature theorem also applies to much broader doubling weights than the explicit density manufactured in XF-085. Nothing here shows that a real-divisor carrier ceases to exist at `(8)`, that the full prime-enriched prefix becomes transition-identifying there, or that Xi itself has any particular value of `Lambda`.

The argument is also insensitive to the precise fixed bump `psi` beyond its compact mesh-scale support. It therefore cannot be repaired by optimizing the bump amplitude or by replacing the Chebyshev upper estimate of XF-104 with a sharper prime-number estimate. Such changes affect only the discarded set `E`; the lower bound comes from cells on which the arithmetic sector is exactly absent.

A decisive next test is correspondingly different: evaluate the Toeplitz/Caratheodory feasibility of the source-derived prefix at `L=log a+O(1)` without replacing positivity by coefficientwise `ell^1` control. A negative eigenvalue with a scale-stable margin would create a genuine real-divisor obstruction; persistent PSD would show that the one-quarter ceiling is purely an artifact of the current sufficient cone.

## 5. Prior art and consequence for the Xi-flow frontier

The ingredients are classical and already source-anchored in this line. Guinand--Weil explicit-formula theory supplies the separation into archimedean background and prime-power atoms used in XF-052. Gilboa--Peled supplies the equal-weight quadrature theorem used by XF-085. A targeted search of explicit-formula Fourier decompositions, Toeplitz/trigonometric moment problems, and Chebyshev-type equal-weight quadrature found no external result asserting the scale-matched ceiling `(4)`--`(8)`. No novelty is claimed for geometric sums, compact-support counting, the explicit formula, or the quadrature theorem, and no new source becomes load-bearing; `SOURCES.md` therefore needs no change.

The durable line-specific conclusion is that the fixed-fraction success of XF-104 and its failure to reach the whole natural arithmetic scale are two sides of the same deterministic geometry. **The next source-interface advance cannot come from squeezing constants inside the raw `ell^1` cone.** To cross the `a^2/4` leading boundary it must exploit correlations and signed moment structure that XF-085 intentionally discards, or abandon the autonomous prefix interface altogether. Transition coercivity remains a separate downstream obligation even if that stronger realization gate is solved.