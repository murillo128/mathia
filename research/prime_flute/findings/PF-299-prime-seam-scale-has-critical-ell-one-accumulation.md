# PF-299 — prime seam scale has a critical `ell^1` accumulation threshold

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + RETURN-ACCUMULATION-THRESHOLD + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-298-tight-pant-constant-response-is-an-asymptotically-conservative-killed-conductance-edge|PF-298]] proves that the scalar constant-mode transmission through the `n`th tight pant has loss

\[
\varepsilon_n
:=1-\theta_n
=\frac{\kappa_n}{c_n+\kappa_n}
=O(s_n),
\]

where `s_n` is the exact neighboring-cuff distance, `c_n\gtrsim s_n^{-1}` is the large cross-conductance, and `\kappa_n` is the relevant nonnegative shifted killing. PF-298 correctly leaves open whether these vanishing local losses accumulate strongly enough along the infinite flute. The prime geometry puts that question at an exact summability threshold.

If

\[
h_n
=F(p_n)-F(p_{n-1}),
\qquad
F(x)=\log\cot\frac{\pi}{x},
\]

is the exact logarithmic prime mesh and

\[
\boxed{s_n=\frac{h_n+h_{n+1}}2}
\]

is the tight-pant seam distance used in PF-215/PF-298, then

\[
\boxed{
(s_n)\notin\ell^1,
\qquad
(s_n)\in\ell^q\quad\text{for every }q>1.
}
\]

The `ell^1` failure is exact and essentially telescopic: `sum h_n` is `F(p_N)-F(p_0)` and diverges. The `ell^q`, `q>1`, statement follows unconditionally from the Baker--Harman--Pintz short-interval exponent `0.525` by a dyadic gap-sum argument; no prime number theorem or conjectural gap law is needed.

Consequently the scalar pant-loss mechanism has a sharp exponent-level discriminator. If a future refinement proves

\[
\varepsilon_n=O(s_n^q)
\qquad\text{for some }q>1,
\]

then `sum epsilon_n<infinity` and the corresponding infinite product of scalar transmissions remains positive. Such superlinear local killing is therefore **too small to absorb the constant channel completely**. Conversely, if one proves an eventual lower bound

\[
\varepsilon_n\ge c s_n,
\]

then `sum epsilon_n=infinity` and the scalar transmission product vanishes. PF-298's current upper bound `O(s_n)` lies exactly at the non-summable endpoint and cannot decide between these regimes.

This does not identify the full `P/H` mixed return operator with the scalar constant channel. It sharpens one live sub-gate of `CLUE-source-weighted-return-potential-controls-mixed-response`: for accumulated constant-mode pant escape, the next useful quantity is the **first-order asymptotic scale of the relative killing**, not another depth-uniform contraction constant.

## Claim

Let `p_n` denote consecutive odd primes and put

\[
P_n:=p_{n-1},
\qquad
g_n:=p_n-p_{n-1}.
\]

Define the exact prime logarithmic mesh

\[
h_n:=F(p_n)-F(P_n),
\qquad
F(x):=\log\cot\frac{\pi}{x},
\tag{1}
\]

and the exact tight-pant neighboring-cuff distance

\[
\boxed{s_n:=\frac{h_n+h_{n+1}}2.}
\tag{2}
\]

Then:

1. `s_n>0`, `s_n\to0`, and
   \[
   \boxed{\sum_n s_n=\infty.}
   \tag{3}
   \]
2. For every fixed `q>1`,
   \[
   \boxed{\sum_n s_n^q<\infty.}
   \tag{4}
   \]
   Equivalently,
   \[
   \boxed{(s_n)\in\bigcap_{q>1}\ell^q\setminus\ell^1.}
   \tag{5}
   \]
3. Let `0<theta_n<=1` be any scalar transmission sequence and set `epsilon_n=1-theta_n`. If, after a finite head,
   \[
   \varepsilon_n\le C s_n^q
   \quad\text{for some }q>1,
   \tag{6}
   \]
   then
   \[
   \boxed{\prod_n\theta_n>0.}
   \tag{7}
   \]
4. If instead, after a finite head,
   \[
   \varepsilon_n\ge c s_n
   \tag{8}
   \]
   for some `c>0`, then
   \[
   \boxed{\prod_n\theta_n=0.}
   \tag{9}
   \]

Applied to the PF-298 constant-mode pant transmission, these implications are only conditional diagnostics. PF-298 proves `epsilon_n=O(s_n)` but neither a matching lower bound nor a superlinear upper bound.

## 1. The seam-distance series diverges exactly

The function `F` is increasing on the prime tail, so `h_n>0`. More importantly, consecutive increments telescope:

\[
\sum_{n=N}^{M}h_n
=F(p_M)-F(p_{N-1}).
\tag{10}
\]

Since

\[
F(x)=\log\frac{x}{\pi}+O(x^{-2}),
\tag{11}
\]

one has `F(p_M)\to\infty`; hence

\[
\sum_n h_n=\infty.
\tag{12}
\]

Equation (2) gives

\[
\sum_{n=N}^{M}s_n
=\frac12h_N+\sum_{n=N+1}^{M}h_n+\frac12h_{M+1},
\tag{13}
\]

so (3) follows without any distribution theorem for primes. The non-summable local geometric scale is built directly into the exact ordered prime mesh.

PF-107 gives the tail asymptotic

\[
\boxed{h_n=\frac{g_n}{P_n}(1+o(1)),}
\tag{14}
\]

and Baker--Harman--Pintz implies `g_n/P_n\to0`; therefore `h_n\to0` and hence `s_n\to0`.

## 2. Every power above one is summable

Fix `q>1` and write

\[
x_n:=\frac{g_n}{P_n}.
\tag{15}
\]

It is enough by (14) to prove `sum x_n^q<infinity`. Let `X=2^k` and restrict to indices with

\[
X\le P_n<2X.
\]

Baker--Harman--Pintz gives, for a fixed `theta=0.525<1` and all sufficiently large `X`,

\[
g_n\le C X^\theta
\tag{16}
\]

throughout this dyadic block, up to a harmless absolute change in `C`. Because the `g_n` are consecutive prime increments, their sum over one such block telescopes across an interval of length `O(X)`; the possible final overshoot is `O(X^theta)`. Thus

\[
\sum_{X\le P_n<2X}g_n=O(X).
\tag{17}
\]

Using `g_n^q=g_n\,g_n^{q-1}`, equations (16)--(17) give

\[
\begin{aligned}
\sum_{X\le P_n<2X}x_n^q
&\le X^{-q}\left(\max g_n\right)^{q-1}
       \sum g_n\\
&\le C_q X^{-q+\theta(q-1)+1}\\
&=C_q X^{-(1-\theta)(q-1)}.
\end{aligned}
\tag{18}
\]

The exponent is strictly negative for every `q>1`. Summing (18) over dyadic `X=2^k` is therefore a convergent geometric series. Hence

\[
\sum_n x_n^q<\infty,
\qquad
\sum_n h_n^q<\infty.
\tag{19}
\]

Convexity yields

\[
s_n^q
=\left(\frac{h_n+h_{n+1}}2\right)^q
\le\frac{h_n^q+h_{n+1}^q}{2},
\tag{20}
\]

so (4)--(5) follow.

The numerical value `0.525` is not load-bearing. The argument needs only any unconditional bound `g_n=O(P_n^theta)` with `theta<1`; Baker--Harman--Pintz is already the canonical audited input used throughout the Prime Flute line.

## 3. Infinite transmission products expose the critical exponent

Let `epsilon_n=1-theta_n` with `0<=epsilon_n<1` eventually. If (6) holds, equations (4) and (6) imply

\[
\sum_n\varepsilon_n<\infty.
\tag{21}
\]

Because `epsilon_n\to0`, after a finite head one has, for example,

\[
-2\varepsilon_n\le\log(1-\varepsilon_n)\le-\varepsilon_n.
\tag{22}
\]

The logarithmic series therefore converges to a finite number, proving (7).

If (8) holds, then (3) gives

\[
\sum_n\varepsilon_n=\infty.
\tag{23}
\]

The upper inequality in (22), or simply `log(1-epsilon)<=-epsilon`, forces

\[
\sum_n\log\theta_n=-\infty,
\]

which proves (9).

Thus the ordered prime geometry distinguishes the linear seam scale from every strictly higher power:

\[
\boxed{
\text{linear loss can accumulate infinitely, whereas every power }s_n^q,\ q>1,\text{ is summable.}
}
\tag{24}
\]

The word `can` in the first clause matters: non-summability of `s_n` does not give a lower bound for an actual loss sequence.

## 4. Consequence for the PF-298 source/escape gate

For the exact PF-298 scalar constant compression,

\[
\theta_{n,L\to R}
=\frac{c_n}{c_n+\kappa_{n,R}},
\qquad
\varepsilon_{n,L\to R}
=\frac{\kappa_{n,R}}{c_n+\kappa_{n,R}}.
\tag{25}
\]

PF-298 proves only

\[
0<\varepsilon_{n,L\to R}\le C s_n.
\tag{26}
\]

Equation (26) is exactly endpoint-scale information: its majorant has divergent sum, while every superlinear power of that majorant is summable. It therefore cannot decide whether repeated pant passage loses all scalar mass or leaves a positive asymptotic survival fraction.

A materially stronger scalar calculation now has a crisp target. Any estimate of the form

\[
\varepsilon_n=O(s_n^{1+\delta}),
\qquad \delta>0,
\tag{27}
\]

would prove that accumulated constant-mode pant killing is insufficient by itself. An eventual lower bound `epsilon_n\gtrsim s_n` would prove the opposite for this scalar chain. More generally, an asymptotic for the ratio `kappa_n/c_n` near the linear seam scale would settle the scalar accumulation question directly.

This is sharper than seeking a local contraction bounded away from one, which PF-298 has already ruled out. It also shows why a heuristic such as `theta_n=1-o(1)` carries essentially no global information here: the prime seam sequence sits precisely at a critical summability boundary.

## 5. Prior art and novelty audit

No novelty is claimed for the analytic-number-theory or infinite-product ingredients. Baker, Harman and Pintz, *The Difference Between Consecutive Primes, II*, Proceedings of the London Mathematical Society **83** (2001), 532--562, DOI `10.1112/plms/83.3.532`, prove the short-interval exponent `0.525`; that source is already recorded as S6 in `SOURCES.md`. The dyadic estimate (18) is an elementary consequence of a sublinear maximal-gap bound plus telescoping of consecutive gaps. The criterion `sum(1-theta_n)<infinity` for positivity of a product with `theta_n->1` is classical elementary analysis.

A structure-directed search did not identify a reason to regard `(g_n/p_n) in ell^q` for every `q>1` as a standalone new prime-gap theorem, and none is claimed. The project-specific content is the combination with the exact prime-flute coordinate (2) and PF-298's killed-conductance transmission: it identifies **linear seam loss as the critical accumulation scale for this return mechanism**.

## 6. Boundaries and falsification

1. **Scalar constant compression only.** Equations (7)--(9) concern a product of scalar pant transmissions. PF-298 explicitly does not prove that this constant compression is invariant under the complete physical `P/H` Schur problem. No conclusion about the full PF-290 mixed response follows without that reassembly.
2. **No hidden lower bound.** PF-298's `epsilon_n=O(s_n)` is only an upper bound. Equation (3) does not imply `sum epsilon_n=infinity`.
3. **No hidden superlinear gain.** Conversely, `epsilon_n=o(s_n)` alone is not enough to infer summability. The sufficient conclusion (7) needs a genuinely summable bound, such as one fixed power `s_n^q` with `q>1`, or another directly summable majorant.
4. **Finite heads are irrelevant.** All BHP estimates and product comparisons may discard finitely many indices without changing (3)--(9).
5. **The `0.525` exponent is only a convenient audited input.** Any proven `theta<1` maximal-gap exponent yields the same `ell^q`, `q>1`, conclusion by (18).
6. **No weak-trace or RH conclusion.** This finding sharpens a source/escape subproblem. It does not prove compactness, weak `S_{1,infinity}`, scattering, a zeta-zero correspondence, the critical line, or RH.

A refutation would have to break the exact telescoping identity (10), the PF-107 asymptotic (14), the dyadic use of the audited sublinear gap bound, or the elementary infinite-product implications. The open mathematical quantity is not the summability of the seam scale; it is the actual asymptotic loss produced by the pant inside the complete normalized return problem.

## Consequence for the research line

PF-297 and PF-298 eliminate a uniform local discount from the Robin and constant-pant pieces. PF-299 adds the missing accumulation calibration: **the canonical pant seam sequence is non-summable only at the linear exponent**. Therefore the scalar part of the accepted source-weighted return-potential clue should no longer ask vaguely whether many small pant losses accumulate. It should determine the first-order scale of `kappa_n/c_n` (or of the exact scalar loss `epsilon_n`) and then return to the full `P/H`-split reassembly. A superlinear loss law closes this scalar escape route negatively; a linear lower law closes it positively; endpoint-sublinear laws require their own summability test.