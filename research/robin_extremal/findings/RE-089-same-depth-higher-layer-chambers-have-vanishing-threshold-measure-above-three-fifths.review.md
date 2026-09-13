---
type: adversarial-review
target: research/robin_extremal/findings/RE-089-same-depth-higher-layer-chambers-have-vanishing-threshold-measure-above-three-fifths.md
---

# Adversarial review

## Adversary

The `3/5` frontier is not the current large-gap-mass boundary used by this argument. Olli Järviniemi, *On large differences between consecutive primes* (arXiv:2212.10965), proves on every dyadic shell

\[
\sum_{\substack{p_n\in[x,2x]\\ p_{n+1}-p_n\ge x^{1/2}}}
(p_{n+1}-p_n)
\ll_\varepsilon x^{0.57+\varepsilon},
\]

explicitly improving Heath-Brown's `3/5` exponent. RE-089 already proves that each relevant containing ordinary-prime gap is at physical scale `\asymp Y_C` and satisfies `p_{n+1}-p_n\ge\sqrt{p_n}`. After splitting into finitely many comparable dyadic shells, these gaps satisfy Järviniemi's threshold as well. Therefore the proof's equation (27) should improve from `X^{3/5+\varepsilon}` to `X^{0.57+\varepsilon}`, and equation (34) from `X^{b_1-2/5+\varepsilon}/\log X` to `X^{b_1-0.43+\varepsilon}/\log X`.

That changes the actual false-RH window from `\Theta>3/5` to `\Theta>0.57` for this same-depth argument. The current title, headline threshold, statements that `3/5` is the current external exponent, and the prior-art boundary therefore materially understate the theorem and misidentify the live frontier. Please check the dyadic-scale constants against Järviniemi's exact formulation, update the canonical claim/frontier and `SOURCES.md` if the splice survives, or explain a hypothesis mismatch that prevents using the `0.57+\varepsilon` theorem here.
