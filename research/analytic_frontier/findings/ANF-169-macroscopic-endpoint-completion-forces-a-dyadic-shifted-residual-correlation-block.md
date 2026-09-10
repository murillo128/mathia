# ANF-169 — macroscopic endpoint completion forces a dyadic shifted residual-correlation block

**Status:** `EXACT-DERIVED + ENDPOINT-CORRELATION-LEDGER + DYADIC-SHIFT-WITNESS + PRIME-RAMANUJAN-GATE + SOURCE-SPECIFIC`. `ANF-157` writes the finite bow energy as full Fejer source energy minus an exact endpoint-completion square function. `ANF-166`--`ANF-168` then show that diagonal normalization, local `L^1/L^2` activity, exact centering, arbitrary fixed-log all-interval cancellation, reality of the pre-demodulated coefficients, and even the exact logarithmic carrier do not control that completion. The remaining objection was qualitative: a successful theorem has to use the actual prime/rough amplitude law.

The endpoint square itself admits a sharper source-side normal form. Expanding it by lags gives an exact **triangular shifted-correlation ledger** supported only on the first and last `K` source coefficients. Its diagonal part is exactly the coefficient-edge defect already shown in `ANF-157` to be `o(XK log X)` for the actual residual. Therefore any completion carrying a fixed positive fraction of the bow scale must create a positive bilinear correlation of size `asymp XK log X` at the endpoints. A dyadic pigeonhole then forces one endpoint and one dyadic lag block to carry at least `gg XK log X/log K` of signed weighted correlation, or equivalently `gg X log X/log K` after normalizing the triangular weight by `K`.

For the actual source `r_X=vartheta-Q_R` of `ANF-149`, this witness is an explicit endpoint-local prime-minus-Ramanujan shifted correlation at the distinguished phase `((n+h)/n)^(-iU)`. Thus the live source theorem after `ANF-168` can be stated quantitatively: rule out these positive dyadic endpoint correlation blocks while preserving the four signed prime/rough terms. This is strictly more specific than asking for another one-point discrepancy estimate and does not assume a prime-pair asymptotic.

## 1. Endpoint completion has an exact triangular lag ledger

Retain the exact integer bow geometry of `ANF-157`. Let

\[
N=X,
\qquad
M=N+K-1,
\tag{1}
\]

and let `b=(b_1,...,b_M)`. Define the two endpoint sequences

\[
b_j^-:=b_j,
\qquad
b_j^+:=b_{M-j+1},
\qquad 1\le j<K,
\tag{2}
\]

so that both endpoint contributions are ordinary prefix squares:

\[
E_\partial(b)
=
E_-(b)+E_+(b),
\qquad
E_\sigma(b)
:=
\sum_{r=1}^{K-1}
\left|
\sum_{j=1}^{r}b_j^\sigma
\right|^2,
\quad \sigma\in\{-,+\}.
\tag{3}
\]

Expanding the square and counting how many prefix lengths contain a fixed pair gives, exactly,

\[
E_\sigma
=
\sum_{j,k=1}^{K-1}
\bigl(K-\max\{j,k\}\bigr)
 b_j^\sigma\overline{b_k^\sigma}.
\tag{4}
\]

Separating the diagonal and writing `k=j+h` in the upper triangle yields

\[
\boxed{
E_\sigma
=
\Delta_\sigma
+2\operatorname{Re}
\sum_{h=1}^{K-2} C_h^\sigma,
}
\tag{5}
\]

where

\[
\Delta_\sigma
:=
\sum_{j=1}^{K-1}(K-j)|b_j^\sigma|^2
\tag{6}
\]

and

\[
\boxed{
C_h^\sigma
:=
\sum_{j=1}^{K-1-h}
(K-j-h)
\overline{b_j^\sigma}b_{j+h}^\sigma.
}
\tag{7}
\]

Thus the endpoint square is not an opaque nonlinear boundary term. It is a positive diagonal edge budget plus a signed sum of ordinary shifted products with the explicit triangular weight `K-j-h`.

Summing (6) over the two endpoints recovers exactly the edge defect from `ANF-157`:

\[
\boxed{
\Delta_-+\Delta_+
=
K\|b\|_2^2-D_{N,K}(b).
}
\tag{8}
\]

No approximation or source hypothesis enters (4)--(8).

It is useful to normalize the correlation weight by the window length. Put

\[
G_h^\sigma
:=
\frac1K C_h^\sigma
=
\sum_{j=1}^{K-1-h}
\left(1-\frac{j+h}{K}\right)
\overline{b_j^\sigma}b_{j+h}^\sigma.
\tag{9}
\]

Then

\[
E_\partial
=
\Delta_-+\Delta_+
+2K\operatorname{Re}
\sum_{\sigma\in\{-,+\}}
\sum_{h=1}^{K-2}G_h^\sigma.
\tag{10}
\]

The natural source currency of a dangerous endpoint completion is therefore a **positive signed average of weighted shifted correlations**, not merely a large single prefix.

## 2. A bow-scale completion forces one positive dyadic lag block

Now specialize to the actual post-sieve source in the bow range

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac14.
\tag{11}
\]

As in `ANF-157`, the pointwise bound `|r_X(n)|\ll\log X` gives

\[
0\le
\Delta_-+\Delta_+
\ll
K^2\log^2X.
\tag{12}
\]

Relative to the bow scale

\[
T_{\rm bow}:=XK\log X,
\tag{13}
\]

this is negligible:

\[
\frac{K^2\log^2X}{T_{\rm bow}}
=
\frac KX\log X
=
X^{-2\varepsilon+o(1)}\log X
=o(1).
\tag{14}
\]

Suppose, along some sequence of `X`, that the endpoint completion is macroscopic:

\[
E_\partial(b)
\ge
\delta T_{\rm bow}
\tag{15}
\]

for a fixed `delta>0`. Combining (10), (14), and (15) gives

\[
\operatorname{Re}
\sum_{\sigma}
\sum_{h=1}^{K-2} C_h^\sigma
\ge
\left(\frac\delta2-o(1)\right)T_{\rm bow}.
\tag{16}
\]

Hence one endpoint, denoted `sigma`, satisfies

\[
\operatorname{Re}
\sum_{h=1}^{K-2}C_h^\sigma
\ge
\left(\frac\delta4-o(1)\right)T_{\rm bow}.
\tag{17}
\]

Partition `1<=h<=K-2` into the dyadic blocks

\[
\mathcal H_H
:=
\{h:H\le h<\min(2H,K-1)\},
\qquad
H=1,2,4,\ldots.
\tag{18}
\]

There are at most `ceil(log_2 K)` such blocks. For all sufficiently large `X`, (17) therefore forces at least one dyadic `H<K` for which

\[
\boxed{
\operatorname{Re}
\sum_{h\in\mathcal H_H}C_h^\sigma
\ge
\frac{\delta}{8\log_2(2K)}
XK\log X.
}
\tag{19}
\]

Equivalently, in the normalized ledger (9),

\[
\boxed{
\operatorname{Re}
\sum_{h\in\mathcal H_H}G_h^\sigma
\ge
\frac{\delta}{8\log_2(2K)}
X\log X.
}
\tag{20}
\]

The constants are deliberately non-optimized. The structural point is the scale: target-sized endpoint completion cannot be hidden entirely in a diffuse collection of individually harmless lags. It forces **one endpoint and one logarithmic lag scale** to carry a positive signed correlation of order `X log X/log K` after the natural `1/K` normalization.

Conversely, (10) gives a clean sufficient source theorem. If some `eta_X->0` satisfies, uniformly for both endpoints and every dyadic block,

\[
\left|
\sum_{h\in\mathcal H_H}G_h^\sigma
\right|
\le
\eta_X\frac{X\log X}{\log(2K)},
\tag{21}
\]

then summing the `O(log K)` blocks and using (14) yields

\[
\boxed{E_\partial(b)=o(XK\log X).}
\tag{22}
\]

Thus (20)--(21) give a quantitative necessary-witness/sufficient-exclusion interface at exactly the missing boundary identified by `ANF-166`--`ANF-168`.

## 3. The actual source turns the witness into a prime-minus-Ramanujan statistic

Use the source-normal form of `ANF-149`, after the target-negligible removal of prime powers,

\[
r_X(n)=\vartheta(n)-Q_R(n),
\qquad
Q_R(n)=\Lambda^\sharp(n)
=
\sum_{q\mid P(R)}
\frac{\mu(q)}{\varphi(q)}c_q(n).
\tag{23}
\]

For the left endpoint,

\[
b_j^-
=
r_X(X+j)(X+j)^{-iU}.
\tag{24}
\]

Therefore every shifted product in (9) is exactly

\[
\boxed{
\overline{b_j^-}b_{j+h}^-
=
r_X(X+j)r_X(X+j+h)
\left(\frac{X+j+h}{X+j}\right)^{-iU}.
}
\tag{25}
\]

The right endpoint is the same object after reversal. With

\[
m_j^+:=2X+K-j,
\tag{26}
\]

one has

\[
\overline{b_j^+}b_{j+h}^+
=
r_X(m_j^+)r_X(m_j^+-h)
\left(\frac{m_j^+-h}{m_j^+}\right)^{-iU}.
\tag{27}
\]

Thus (20) is an explicit arithmetic event involving the **actual distinguished multiplicative phase**; no Taylor replacement by a polynomial phase is needed to state the gate.

Expanding the source product in (25) gives the same four signed terms isolated globally in `ANF-149`:

\[
\begin{aligned}
r_X(n)r_X(n+h)
={}&\vartheta(n)\vartheta(n+h)
-\vartheta(n)Q_R(n+h)\\
&-Q_R(n)\vartheta(n+h)
+Q_R(n)Q_R(n+h).
\end{aligned}
\tag{28}
\]

The new point is localization and weight. The surviving endpoint obstruction is controlled by these four terms on one of the two length-`K` boundary regions, summed over one dyadic lag scale with the triangular factor `1-(j+h)/K`. A proof that estimates the prime and rough terms separately behind absolute values can again lose precisely the common cancellation that `ANF-149` showed should be preserved.

Accordingly the source-specific gate can now be written without reference to synthetic controls: prove (21), or any stronger bound implying it, for the fixed residual (23) at the distinguished `U` relevant to the bow.

## 4. This is different from the global bow correlation ledger of ANF-149

`ANF-149` already expands the bow variance itself as a diagonal plus a signed shifted correlation over the complete moving-window overlap. The present identity does not duplicate that reduction. It expands the **endpoint completion term** introduced later by `ANF-157`, which is the only remaining obstruction to transferring full Fejer information back to the cropped bow after `ANF-158`--`ANF-168`.

The distinction is visible in the weights. The global bow ledger uses the exact overlap multiplicity of two source sites across observed length-`K` windows. Equations (7)--(9) instead use the complementary triangular incidence of two sites in the unobserved prefix/suffix rows of the completed convolution. The two ledgers fit together exactly because both arise from the same rectangular box-convolution matrix, but they ask for different arithmetic information.

This also explains the charge-and-hold control of `ANF-166`. A primitive plateau looks like a one-point memory effect, but after (5) its energy has to be paid by positive pair correlation among the coefficients that created the initial charge. `ANF-167` shows that local activity budgets can coexist with that payment, and `ANF-168` shows that the coefficients can even lie on the exact logarithmic carrier rays. What those controls are free to choose, and the arithmetic source is not, is the real amplitude/sign pattern entering the bilinear products (25)--(28).

So the surviving obstruction is no longer merely “some source-specific placement law”. It is the possibility that the fixed prime-minus-Ramanujan source generates a positive endpoint-local shifted-correlation block of the explicit size (20).

## 5. Prior-art boundary and stress tests

The identities (4)--(10) and the dyadic extraction (19) are elementary finite sums; no external theorem is load-bearing. A bounded prior-art audit found the expected neighboring literature on averaged shifted correlations of the von Mangoldt function and on short-interval prime uniformity. Those results reinforce that averaging over `h` is a natural arithmetic interface, but they do not directly provide (21): the present statistic is simultaneously endpoint-local in `n`, uses the post-sieve residual `vartheta-Q_R`, carries the distinguished high-frequency multiplicative phase, keeps the prime/Ramanujan signs coupled, and has a triangular boundary weight. `SOURCES.md` therefore needs no new load-bearing anchor for this finding.

Several boundaries are important. First, (19) asserts a large **dyadic sum of real parts**, not a large individual lag. No individual prime-pair correlation theorem is being smuggled in. Second, the diagonal term cannot manufacture the witness because (14) makes it target-negligible for every fixed `epsilon>0` in the bow range. Third, all identities are valid for arbitrary real `U`; the specialization `U\asymp X^2` enters only when the statistic is connected back to the analytic-frontier bow. Fourth, (28) is an exact algebraic decomposition and does not assume Hardy--Littlewood prime pairs or replace interval averages by complete Ramanujan periods.

Finally, the implication is one-way at the witness level. A macroscopic endpoint square forces some block satisfying (19), but a single positive block need not by itself force a macroscopic endpoint square because other lag blocks may contribute negatively. The uniform exclusion criterion (21) is sufficient because it controls every dyadic block in absolute value.

## 6. Consequence for the analytic frontier

The sequence `ANF-166`--`ANF-168` rules out three increasingly source-shaped but still coefficient-generic fixes: stronger long-interval increments, local activity/mass information, and exact logarithmic carrier rays with real amplitudes. The present result identifies the first concrete statistic that those matched controls can fake but the arithmetic source fixes completely.

The next useful theorem is therefore a **dyadic endpoint shifted-correlation estimate** for

\[
(\vartheta-Q_R)(n)(\vartheta-Q_R)(n+h)
\left(\frac{n+h}{n}\right)^{-iU},
\tag{29}
\]

with `n` restricted to a bow endpoint, `h` restricted to a dyadic block, and the four signed prime/Ramanujan pieces kept together through the estimate. A bound at the scale (21) would eliminate target-sized endpoint completion and remove the charge-and-hold escape from the Fejer reduction.

This does not solve the bow. It does something narrower but decisive for the research architecture: **the source-specific endpoint gate is now a quantitative bilinear correlation problem, not an undefined demand for “more arithmetic structure”.** Further one-point discrepancy improvements should be judged by whether they imply this endpoint correlation bound; otherwise they do not address the surviving obstruction.
