# MC-280 — Atom-sensitive signed endpoint decoders have negligible low-depth Fourier variation

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the Boolean-row endpoint formulation of `MC-275`, `MC-277`, `MC-278`, and `MC-279`. Write

\[
x=(x_1,\ldots,x_k)\in\{-1,+1\}^k,
\qquad
x_*=1^k,
\]

and let

\[
D(x)=\sum_{S\subseteq[k]} a_S x_S
\tag{1}
\]

be an arbitrary real- or complex-valued scalar endpoint decoder satisfying

\[
D(x_*)=1,
\qquad
|D(x)|\le\varepsilon\quad(x\ne x_*).
\tag{2}
\]

No sign, positivity, radiality, rational-degree, or positive-definiteness assumption is imposed on the Walsh coefficients `a_S`. Put

\[
Z_m(k):=\sum_{j=0}^m\binom kj,
\qquad
V_m(D):=\sum_{|S|\le m}|a_S|.
\tag{3}
\]

Then Parseval and Cauchy--Schwarz give the universal signed low-depth bound

\[
\boxed{
V_m(D)
\le
\sqrt{Z_m(k)}
\left(2^{-k}+(1-2^{-k})\varepsilon^2\right)^{1/2}.
}
\tag{4}
\]

In particular,

\[
\left|\sum_{|S|\le m}a_S\right|
\le V_m(D),
\tag{5}
\]

so `(4)` bounds not merely the net low-degree endpoint contribution but its full signed/complex coefficient variation.

At the live blind-count scale, let

\[
C=C_y(t)=\binom{N_y}{t},
\qquad
m=t+1,
\tag{6}
\]

where

\[
k=k_y\sim\frac y{\log y},
\qquad
N_y\sim\frac y{\log y},
\qquad
t=\left(\frac1{\log2}+o(1)\right)\log\log y.
\tag{7}
\]

Any pointwise decoder whose direct sum over the `C` target rows determines an integer blind count with deterministic aggregate error below `1/2` must have

\[
\varepsilon<\frac1{2C}.
\tag{8}
\]

For every decoder satisfying `(2)` and `(8)`, `(4)` yields

\[
\boxed{
V_{t+1}(D)=o(1).
}
\tag{9}
\]

More quantitatively,

\[
V_{t+1}(D)
\le
\sqrt{\frac{Z_{t+1}(k)}{2^k}}
+
\frac{\sqrt{Z_{t+1}(k)}}{2C},
\tag{10}
\]

with

\[
\log\frac{\sqrt{Z_{t+1}(k)}}{C}
=
-\left(\frac1{2\log2}+o(1)\right)
\log y\,\log\log y,
\tag{11}
\]

while

\[
\sqrt{Z_{t+1}(k)2^{-k}}
=
\exp\!\left[-\left(\frac{\log2}{2}+o(1)\right)k\right].
\tag{12}
\]

Since `D(x_*)=\sum_S a_S=1`, `(9)` also forces

\[
\boxed{
\sum_{|S|>t+1}|a_S|
\ge 1-o(1).
}
\tag{13}
\]

Thus the positivity assumption in `MC-279` is **not needed to rule out a full-cube pointwise scalar decoder at the actual atom-sensitive accuracy relevant to the arithmetic aggregation problem**. Even with arbitrary signed or complex Walsh coefficients, a decoder that is uniformly small enough on every nonblind Boolean vector to survive summation over all target rows has negligible coefficient variation at the available source depth `t+1`.

`MC-279` remains stronger in a different direction: for positive-definite decoders, merely requiring `\varepsilon_k\to0` already forces Fourier mass above every `(1/2-\delta)k` cutoff. The present theorem does not give a universal half-depth barrier for signed decoders at slowly vanishing error. It instead uses the much sharper arithmetic requirement `\varepsilon\ll C^{-1}` and proves exactly what the live route needs: signed scalar pointwise decoding cannot compress the exceptional-row test back into the logarithmic source hierarchy.

The surviving alternatives are therefore narrower. A signed mechanism must either exploit cancellation **across target rows without first constructing a uniformly sharp rowwise scalar decoder**, use a decoder defined only on the tightly localized arithmetic image rather than on the full Boolean cube, or keep the inverse as a genuinely source-native arithmetic/operator object whose action is not represented by a scalar function satisfying `(2)`.

No blind relation is excluded, no estimate for `M(X)` follows, and no claim is made that arbitrary signed cross-row aggregation is impossible.

## 1. Parseval controls arbitrary coefficient signs

Use the normalized Walsh coefficients

\[
a_S
=2^{-k}\sum_{x\in\{-1,+1\}^k}D(x)x_S.
\tag{14}
\]

Parseval on the Boolean group gives

\[
\sum_{S\subseteq[k]}|a_S|^2
=2^{-k}\sum_x|D(x)|^2.
\tag{15}
\]

By `(2)`,

\[
2^{-k}\sum_x|D(x)|^2
\le
2^{-k}+(1-2^{-k})\varepsilon^2.
\tag{16}
\]

There are exactly `Z_m(k)` subsets of size at most `m`. Therefore

\[
\begin{aligned}
V_m(D)
&=\sum_{|S|\le m}|a_S|\\
&\le
\sqrt{Z_m(k)}
\left(\sum_{|S|\le m}|a_S|^2\right)^{1/2}\\
&\le
\sqrt{Z_m(k)}
\left(2^{-k}+(1-2^{-k})\varepsilon^2\right)^{1/2},
\end{aligned}
\]

which is `(4)`.

The point is precisely that coefficient signs no longer help. In `MC-279`, Fourier positivity allowed the Boolean noise operator to convert low-degree coefficient mass into a positive quantity. Here the much stronger pointwise accuracy `(8)` makes the whole decoder tiny in normalized `L^2`, and the dimension of the low-degree Walsh space is too small to amplify that `L^2` norm back to order one at the endpoint. Cauchy--Schwarz controls the absolute coefficient variation before any signed cancellation can be used.

Equivalently, if `\Pi_{\le m}` denotes orthogonal projection onto Walsh degree at most `m`, then

\[
|\Pi_{\le m}D(x_*)|
\le
V_m(D)
\le
\sqrt{Z_m(k)}\,\|D\|_2.
\tag{17}
\]

The factor `\sqrt{Z_m(k)}` is the norm of endpoint evaluation on this finite-dimensional low-degree subspace; it is the same reproducing-kernel/Christoffel quantity already present in `MC-268` and `MC-277`.

## 2. The live shell count overwhelms the low-degree evaluation norm

For `m=o(k)`, the top binomial term controls the Hamming-ball dimension at logarithmic scale:

\[
\log Z_m(k)
=m\log\frac{k}{m}+O(m).
\tag{18}
\]

Likewise, for `t=o(N_y)`,

\[
\log C_y(t)
=t\log\frac{N_y}{t}+O(t).
\tag{19}
\]

At `m=t+1`, the prime number theorem gives `k/N_y\to1`; moreover `\log k=\log y+O(\log\log y)` and `\log t=O(\log\log\log y)`. Hence

\[
\begin{aligned}
\log\frac{\sqrt{Z_{t+1}(k)}}{C_y(t)}
&=
\frac12(t+1)\log\frac{k}{t+1}
-t\log\frac{N_y}{t}
+O(t)\\
&=
-\left(\frac t2+o(t)\right)\log y\\
&=
-\left(\frac1{2\log2}+o(1)\right)
\log y\,\log\log y,
\end{aligned}
\tag{20}
\]

which proves `(11)`. Since `t+1=o(k)`, `(18)` also gives `\log Z_{t+1}(k)=o(k)`, proving `(12)`.

Combining `(4)`, `(8)`, and `\sqrt{a+b}\le\sqrt a+\sqrt b` gives `(10)` and hence `(9)`.

Finally, evaluation at the blind point gives

\[
1=D(x_*)
=\sum_{|S|\le t+1}a_S
+
\sum_{|S|>t+1}a_S.
\tag{21}
\]

Therefore

\[
\sum_{|S|>t+1}|a_S|
\ge
\left|\sum_{|S|>t+1}a_S\right|
\ge
1-V_{t+1}(D),
\]

and `(13)` follows.

## 3. Why this is not the OR approximate-degree theorem again

`MC-275` uses the classical approximate degree of OR to show that a polynomial which is itself uniformly close to the blind/nonblind indicator cannot have low degree. That statement rules out replacing the whole decoder by a low-degree polynomial.

The present statement allows `D` to have **arbitrary total Walsh degree** and arbitrary rational, transcendental, or externally specified scalar form after evaluation on the cube. It asks a different representation question: how much of such a sharp decoder can live in the pre-existing degree-`m` source hierarchy?

Equation `(4)` says that, at the error scale required by direct aggregate counting, the answer is asymptotically none in `L^1` Fourier variation. Thus a formally low rational degree does not help if its Boolean evaluation achieves pointwise atom sensitivity by importing high Walsh depth; `MC-278` exhibited that phenomenon explicitly for `(1+b)^{-q}`, and `(4)` shows it for arbitrary signed scalar decoders at the live accuracy.

The distinction also explains why there is no contradiction with the exact Christoffel threshold representation of `MC-277`. The scalar `P_m` separates blind from nonblind rows by a margin `\delta_{k,m}\asymp m/k`, but it is not uniformly `O(C^{-1})` on the nonblind cube. Applying a sharp scalar nonlinearity to turn that margin into pointwise error `O(C^{-1})` necessarily introduces the high-degree Fourier variation detected by `(9)` unless the operation is kept outside the scalar full-cube decoder model.

## 4. Prior art and novelty boundary

The mathematical ingredients of `(4)` are classical Walsh--Fourier Parseval and Cauchy--Schwarz. Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), DOI `10.1017/CBO9781139814782`, is a standard reference for normalized Walsh expansions, Parseval, low-degree projections, and Boolean noise. Irit Dinur, Ehud Friedgut, Guy Kindler and Ryan O'Donnell, *On the Fourier tails of bounded functions over the discrete cube*, Israel Journal of Mathematics 160 (2007), 389--412, DOI `10.1007/s11856-007-0068-9`, studies substantially deeper general constraints on Fourier tails of bounded cube functions.

The nearby polynomial-approximation boundary remains the classical approximate-degree theory already audited in `MC-275`; in particular the small-error degree of symmetric Boolean functions has the `\sqrt{k\log(1/\varepsilon)}` scale relevant there. The present proof neither improves nor reproves that optimal approximate-degree theorem.

A targeted literature search through 14 September 2026 did not locate this exact `V_m(D)` inequality stated as an atom-sensitive signed-decoder obstruction. That absence is not evidence of novelty: `(4)` is an immediate Hilbert-space estimate once the question is posed. No novelty is claimed for the abstract Boolean inequality.

The durable Mathia contribution is the frontier consequence obtained by inserting the live arithmetic scales `(6)`--`(8)`: the signed-coefficient loophole explicitly left open by `MC-279` disappears for **full-cube pointwise scalar decoding at the accuracy actually required to detect one exceptional target row**.

## Boundaries and falsification tests

- **Uniform full-cube accuracy is essential.** The `L^2` estimate `(16)` uses smallness on every nonblind Boolean vector. A decoder defined or controlled only on the actual Legendre-sign image may have large values elsewhere and need not satisfy `(4)` with the same `\varepsilon`.
- **Direct rowwise decoding is essential.** A signed aggregate may combine different target rows before any rowwise decoder satisfying `(2)` exists. Such phase-sensitive cross-row cancellation is not constrained by this theorem.
- **No universal half-depth theorem for signed decoders.** If `\varepsilon` merely tends to zero slowly, the factor `\sqrt{Z_m(k)}\varepsilon` can be large. `MC-279` retains its stronger positivity-based `(1/2-o(1))k` conclusion in that regime.
- **The theorem controls coefficient variation only below the chosen cutoff.** It gives no upper bound on total Fourier `L^1` norm and does not identify where above `m` the necessary variation sits.
- **The arithmetic asymptotic uses the live shell scale.** A different target-family size or source-depth regime must re-evaluate the dimension/error product `\sqrt{Z_m(k)}\varepsilon` rather than importing `(9)` mechanically.
- **No arithmetic specificity is proved.** The finite-cube inequality holds for every function. Any surviving route must obtain its advantage from the localized arithmetic image, cross-row sign structure, or a non-scalar source-native inverse.
- **No RH or Mertens consequence.** This is a representation no-go, not a cancellation estimate for the Möbius function.

A direct falsification would be a function satisfying `(2)` and `(8)` at the live scales for which `V_{t+1}(D)` stays bounded below by a fixed positive constant. Equations `(15)`--`(20)` exclude this.

## Consequence for the research line

The scalar-decoder frontier has now split cleanly by what information is retained before aggregation.

`MC-277` shows that the existing degree-`m` Christoffel scalar already contains the blind bit with exact but shrinking margin. `MC-278` shows that a low-rational-degree pointwise decoder can sharpen that margin only by importing macroscopic Walsh depth in one explicit positive example. `MC-279` proves a universal half-depth obstruction for all positive-definite sharp decoders. The present result closes the remaining **signed full-cube pointwise scalar** loophole at the much stronger `1/C` accuracy needed by direct exceptional-row counting.

Accordingly, changing coefficient signs, rational formula, radial shape, or scalar nonlinearity cannot by itself recover a source-cheap pointwise decoder on the full cube. The useful open routes are now genuinely different: obtain arithmetic control of the raw Christoffel scalar at its natural margin before provenance is discarded; exploit signed cancellation across target rows without demanding uniform rowwise atom suppression; or derive a source-native arithmetic/operator inverse whose action is restricted enough that the full-cube Parseval barrier is not the relevant model.