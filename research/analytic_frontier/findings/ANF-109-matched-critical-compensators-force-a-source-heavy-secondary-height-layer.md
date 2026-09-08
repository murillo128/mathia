# ANF-109 — matched-critical compensators force a source-heavy secondary height layer

**Status:** `EXACT-DERIVED + HEIGHT-LAYER-EXTRACTION + COMPENSATOR-CASCADE-STRENGTHENING + CARDINALITY-HEIGHT-TRADEOFF`. `ANF-108` proves that a source-heavy sparse compensator in the matched Montgomery--Taylor source-critical window forces the retained core to reach height at least `(4 pi)^{-1} log log R`, but its theorem is stated only in terms of the maximum core height. The endpoint energy estimate proved there actually forces a stronger conclusion: above every fixed subcritical fraction of that log--log height, the core contains a **source-heavy height layer**. Thus the secondary cascade cannot be witnessed only by source-negligible high points.

More precisely, retain the hypotheses and notation of `ANF-108`. Let

\[
W_n=A_n\sqcup B_n,\qquad
L_n=L(W_n),\qquad
R_n=\frac{L_n}{|B_n|^2}\to\infty,
\]

where `W_n` is Montgomery--Taylor near-extremal, `B_n` is source-heavy,

\[
\liminf_n\frac{E_0(B_n)}{L_n}\ge\lambda>0,
\]

and its maximum height satisfies the matched-critical upper bound

\[
4\pi H_{B,n}
\le
\log R_n+2\log\log R_n+O(1).
\]

For any fixed `0<theta<1`, define

\[
h_{\theta,n}
:=\frac{1-\theta}{4\pi}\log\log R_n,
\]

and split the retained core by height,

\[
A_n^{\le\theta}
:=\{a\in A_n:|\operatorname{Im}a|\le h_{\theta,n}\},
\qquad
A_n^{>\theta}
:=A_n\setminus A_n^{\le\theta}.
\]

Then there is a constant `c_{theta}>0` (depending also on the source-heavy lower bound and the bounded constants in the matched-critical window) such that

\[
\boxed{
\liminf_{n\to\infty}
\frac{E_0(A_n^{>\theta})}{L_n}
\ge c_{\theta}>0.
}
\tag{1}
\]

Hence every subcritical log--log height cut leaves a source-heavy component above it. This upgrades the maximum-height conclusion of `ANF-108` to an energy statement and supplies the missing input for any attempted iterated height decomposition.

## 1. The two inputs from ANF-108

Write

\[
E_{\mathrm{edge},\delta}(X)
:=
\int_{1-\delta\le|\alpha|\le1}
J_0(\alpha)|S_X(\alpha)|^2\,d\alpha.
\]

For

\[
\delta_n
=4\frac{\log\log R_n}{\log R_n},
\]

`ANF-108` proves two uniform consequences of the matched-critical compensator hypotheses. First,

\[
E_0(A_n)\le C_A L_n
\tag{2}
\]

for some finite constant `C_A`. Second, the negative source polarization against `B_n` is forced into the shrinking Montgomery--Taylor endpoint layer, giving

\[
E_{\mathrm{edge},\delta_n}(A_n)
\ge c_A L_n
\tag{3}
\]

for some `c_A>0` and all sufficiently large `n`.

The other input is the bounded-strip endpoint anti-concentration inequality established in that finding. If every point of a physical configuration `X` satisfies `|Im z|<=H`, then

\[
\boxed{
E_{\mathrm{edge},\delta}(X)
\le
C_* (1+H)e^{4\pi H}\delta E_0(X),
\qquad 0<\delta\le\frac12.
}
\tag{4}
\]

No spacing, multiplicity, horizontal-span, or gap hypothesis is present in (4).

## 2. Either the low layer is source-controlled or the high layer is already source-heavy

Set

\[
U_n=A_n^{\le\theta},
\qquad
V_n=A_n^{>\theta}.
\]

The source energy is a Hilbert norm squared, so

\[
\sqrt{E_0(V_n)}
\ge
\bigl|\sqrt{E_0(U_n)}-\sqrt{E_0(A_n)}\bigr|.
\tag{5}
\]

Choose once and for all `M>4C_A`. If along some index `n` one has

\[
E_0(U_n)>M L_n,
\]

then (2) and (5) immediately yield

\[
E_0(V_n)
\ge
(\sqrt M-\sqrt{C_A})^2L_n
\gg L_n.
\tag{6}
\]

Thus an anomalously large source norm below the cut cannot be hidden inside the bounded total core norm without a comparably large high-layer norm. This case requires no endpoint localization at all; it is simply reverse triangle inequality in the exact Montgomery--Taylor Hilbert space.

It remains to consider indices for which

\[
E_0(U_n)\le M L_n.
\tag{7}
\]

Now the endpoint anti-concentration inequality becomes effective because `U_n` has height at most `h_{theta,n}`.

## 3. A subcritical log--log strip has negligible endpoint energy whenever its source norm is controlled

Apply (4) to `U_n` with `H=h_{theta,n}` and `delta=delta_n`. Since

\[
e^{4\pi h_{\theta,n}}
=(\log R_n)^{1-\theta},
\]

(7) gives

\[
\begin{aligned}
\frac{E_{\mathrm{edge},\delta_n}(U_n)}{L_n}
&\le
C_*M(1+h_{\theta,n})
(\log R_n)^{1-\theta}
4\frac{\log\log R_n}{\log R_n}\\
&\ll_{\theta,M}
\frac{(\log\log R_n)^2}{(\log R_n)^\theta}
\longrightarrow0.
\end{aligned}
\tag{8}
\]

The endpoint restriction is itself a Hilbert seminorm. Therefore, by (3), (8), and the reverse triangle inequality in that restricted norm,

\[
\begin{aligned}
\sqrt{E_{\mathrm{edge},\delta_n}(V_n)}
&\ge
\sqrt{E_{\mathrm{edge},\delta_n}(A_n)}
-
\sqrt{E_{\mathrm{edge},\delta_n}(U_n)}\\
&\ge
\frac12\sqrt{c_A L_n}
\end{aligned}
\]

for all sufficiently large indices satisfying (7). Hence

\[
E_0(V_n)
\ge
E_{\mathrm{edge},\delta_n}(V_n)
\ge
\frac{c_A}{4}L_n.
\tag{9}
\]

Combining (6) and (9) proves (1), including sequences that alternate between the two cases. The argument is deliberately insensitive to the low--high cross term: either that cross term hides a large low-layer source norm, in which case the high layer is source-heavy by (5), or the low-layer norm is controlled and its endpoint energy is killed by (4).

## 4. The source-heavy layer obeys a quantitative cardinality--height tradeoff

Let

\[
m_{\theta,n}=|A_n^{>\theta}|,
\qquad
H_{A,n}=\max_{a\in A_n}|\operatorname{Im}a|.
\]

The universal tail estimate of `ANF-103` applies to any finite physical subconfiguration, not only to a component already designated as a tail. For `H_{A,n}>=1`,

\[
E_0(A_n^{>\theta})
\ll
m_{\theta,n}^2
\frac{e^{4\pi H_{A,n}}}{H_{A,n}^2}.
\tag{10}
\]

Together with (1), this gives the population/height tradeoff

\[
\boxed{
m_{\theta,n}
\gg_{\theta}
\sqrt{L_n}\,H_{A,n}e^{-2\pi H_{A,n}}.
}
\tag{11}
\]

In particular, if the retained core stays near the minimal secondary scale,

\[
4\pi H_{A,n}
\le
(1+o(1))\log\log R_n,
\]

then `H_{A,n}>=h_{theta,n}` and (11) forces

\[
\boxed{
m_{\theta,n}
\ge
\sqrt{L_n}\,
\frac{\log\log R_n}{(\log R_n)^{1/2+o(1)}}.
}
\tag{12}
\]

So at the minimal log--log height the cascade cannot be carried by finitely many exceptional points: a growing population is required.

Conversely, whenever

\[
m_{\theta,n}=o(\sqrt{L_n}),
\]

put

\[
R_{\theta,n}=\frac{L_n}{m_{\theta,n}^2}\to\infty.
\]

Because (1) says this high layer is source-heavy relative to `L_n`, the same `ANF-103` inversion yields

\[
\boxed{
4\pi H_{A,n}
\ge
\log R_{\theta,n}
+2\log\log R_{\theta,n}
+O_{\theta}(1).
}
\tag{13}
\]

Thus the second layer has exactly the same alternatives as the original sparse tail: either it reaches square-root cardinality scale, or its own sparsity ratio forces another logarithmic height budget.

## 5. Adversarial checks, prior-art boundary, and remaining frontier

The main possible failure in trying to upgrade `ANF-108` is that the low layer could have enormous full source norm even though the total core has only `O(L_n)` norm; then applying endpoint anti-concentration to the low layer would be useless because its right-hand side contains `E_0(U_n)`. Equations (5)--(6) are the necessary repair. Large hidden low-layer energy already proves the desired conclusion, since it can be cancelled down to (2) only by a high layer of comparable Montgomery--Taylor norm. Therefore no unproved monotonicity of `E_0` under deleting points is used.

The height split need not be horizontally separated and need not preserve any geometric gap. The proof after the `ANF-108` inputs uses only Hilbert-space triangle inequalities and the geometry-free anti-concentration estimate (4). It also does **not** prove that `A_n^{>theta}` is sparse, notch-visible, near-extremal on its own, or a new compensator with the affine polarization properties of `B_n`. Those stronger properties would require additional information and are not smuggled into (13).

The nearest classical concentration literature remains the large-sieve/uncertainty-principle neighborhood already audited in `ANF-108`, including Donoho--Logan's small-set concentration inequalities. The new step here is an internal consequence of the Mathia-specific endpoint anti-concentration estimate plus elementary Hilbert-space norm geometry; no standalone novelty claim about Hilbert decomposition is made and no new external theorem is load-bearing. `SOURCES.md` therefore requires no change.

The immediate gate left by `ANF-108` is now closed: the secondary log--log cascade is source-relevant, not merely a maximum-height witness. The next obstruction is sharper. One must either control the cardinality of `A_n^{>theta}` strongly enough that `R_{theta,n}->infinity` can be exploited recursively, or handle the alternative in which a square-root-scale population of the core rises into the log--log strip. Even in the sparse alternative, (13) alone does not recreate the negative-polarization hypothesis needed to iterate `ANF-108`; a new argument must show that the extracted source-heavy layer participates in the required cancellation rather than merely carrying positive source energy.