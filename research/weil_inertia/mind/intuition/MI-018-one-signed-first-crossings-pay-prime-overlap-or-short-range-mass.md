# MI-018 — One-signed first crossings have an exact positive-tail operator budget, with a Carleman wall at zero gap

**Evidence level:** exact on the one-signed branch of a hypothetical first unrestricted Suzuki crossing through [WI-273](../../findings/WI-273-positive-tail-hankel-norm-sharpens-gap-screening-but-hits-the-carleman-wall.md). No theorem makes the actual first null mode one-signed, forces an internal gap, or proves RH. The sign-changing branch remains governed by the PSD/nodal compensation structure.

At a first crossing, the source-ground-state transform makes every bounded Lipschitz multiplier energy nonnegative. On the one-signed branch, a genuine internal support gap `(alpha,beta)` can be used to split the mode into exact left and right pieces. The cut energy must then be financed by prime-power crossing overlap plus the positive part of Suzuki's archimedean source.

Earlier scalar control priced that continuous contribution by the tail mass

`B(L)=integral_L^h0 w(h) dh`,

where `L=beta-alpha` and `h_0` is the unique sign-change length of the archimedean kernel. WI-273 identifies the actual `L^2` object instead. After translating the two sides of the gap, the positive continuous term is exactly the bilinear form of the Hankel operator

`K_L(u,y)=w(L+u+y) 1_(u+y<h_0-L)`

with norm `Theta(L)`. Only the two collars of width `h_0-L` can contribute. The sharp source-conditioned tariff is therefore

`P_gap >= max(lambda_(r_L) M_L, lambda_(r_R) M_R) - Theta(L) sqrt(m_L^col m_R^col)`.

This strictly sharpens the mass-only estimate at positive gap width. One has

`Theta(L) <= min(B(L), H(L), pi/2)`,

where `H(L)^2=integral_L^h0 (h-L)w(h)^2 dh`. Near `h_0`, the Hilbert--Schmidt envelope improves the scalar tail by the exact leading factor `1/sqrt(3)`. Complete screening also forces a quantitative collar-concentration inequality, not merely a total left/right mass ratio.

The important negative result is the zero-gap limit. The exact positive Suzuki kernel has the same leading `1/(2h)` singularity as one half of the Carleman kernel, and WI-273 proves

`Theta(L)<pi/2` for every `L>0`, but `Theta(0)=pi/2` and `Theta(L)->pi/2` as `L downarrow 0`.

Thus replacing the previous Young `L^1` tail bound by the **exact** positive-source `L^2` operator norm removes the artificial logarithmic divergence but does not create a uniform narrow-gap gain. The mass-only operator route itself reaches a sharp Carleman wall.

**Research consequence.** For positive-width gaps, use `Theta(L)` and the visible collar masses rather than the coarser scalar tail `B(L)`. For the gapless or arbitrarily narrow regime, another refinement of the same global `L^2` operator norm cannot supply a strict uniform improvement: progress must exploit additional structure of the null mode, the simultaneous family of cuts, or the distributional null equation. The one-signed residual has therefore moved from “find a sharper source-conditioned norm” to “use information that an operator norm deliberately forgets.”

**Boundary.** The tariff is conditional on a one-signed first null mode and a genuine separating gap. It does not transfer to sign-changing cross-gap products, where long-range negative archimedean compensation remains active.