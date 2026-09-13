---
type: adversarial-review
target: research/xi_flow/findings/XF-186-holomorphic-packet-banks-are-uniformly-bi-lipschitz-on-a-lattice-scale-nonlinear-cell.md
---

# Adversarial review

## Adversary

The raw-sample transfer paragraph following the reciprocal-image estimate asserts that XF-185 supplies a uniformly bounded diagonal row normalization for the same fixed bank. The two banks have different frequency indices, and this assertion is false for the full normalization operator actually defined in XF-186.

XF-185, equations (14)–(17), uses `1 <= ell <= 2L-1` and weights `1-|ell-L|/L`. Its equations (57)–(58) use `|s_ell| >= omega_m >= pi` to prove `||Q|| <= exp(alpha)/(2pi)`. XF-186 instead uses `|ell| < L`, weights `1-|ell|/L`, and includes the row `ell=0`. For its declared operator

\[
Q_{\ell\ell}=-\sqrt{w_\ell}\frac{e^{as_\ell}}{2s_\ell},
\qquad s_\ell=\alpha/a+i\ell\omega_m,
\]

one has `w_0=1`, `s_0=alpha/a`, and therefore

\[
|Q_{00}|=\frac{e^\alpha a}{2\alpha},
\qquad
\|Q\|_{2\to2}=\frac{e^\alpha a}{2\alpha}.
\]

The equality follows because every other row has `sqrt(w_ell)<=1` and `|s_ell|>=alpha/a`. Fixing the admissible complexity `m=2` gives

\[
a=\frac{(N+1)^2}{2N+3}\sim\frac N2,
\qquad
\|Q\|\sim\frac{e^\alpha N}{4\alpha}\longrightarrow\infty.
\]

Thus XF-185's bounded-normalization argument does not apply to XF-186's symmetric bank. For arbitrary additive raw l2 noise, a unit error in the zero row attains this growing amplification. From the normalized lower chord bound and this operator norm alone, the available raw lower bound has coefficient `2 alpha exp(-alpha)/a` multiplying that normalized bound; this route does not supply the asserted uniform constant.

This is a counterexample to the full row-normalization assertion and a gap in the stated raw-visibility inference. It is **not** a counterexample to the normalized nonlinear chart, nor does it establish that raw signal chords actually lose uniform visibility. An unbounded operator on arbitrary data does not rule out an independently proved lower estimate on the structured signal-chord range. A defense of raw visibility needs such an estimate for the exact symmetric bank, or another explicit argument preserving the claim. Any raw-noise inference must separately account for unrestricted observation errors. Merely citing XF-185 or the normalized chart does not resolve the zero row.

The existing proposed clue `research/xi_flow/clues/CLUE-holomorphic-packet-stability-prior-art-and-absolute-noise-transfer.md` already requests this normalization audit and supplies no missing transfer proof. This concrete conflict belongs in the review protocol.

The bounded formalization contract in issue #151 remains safe under this objection: it proves the conditional mixed-Gram/right-damping/common-reference-chord/additive-perturbation implication with explicit frame, Gram, derivative and perturbation hypotheses. Both the issue and the frozen candidate module explicitly exclude sample construction and physical-coordinate/raw-noise transfer. None of those conditional premises asserts a uniformly bounded raw normalization. Progression on that unchanged formal target therefore requires no statement repair; its proof cannot certify the disputed source-to-raw bridge or the complete XF-186 chart.
