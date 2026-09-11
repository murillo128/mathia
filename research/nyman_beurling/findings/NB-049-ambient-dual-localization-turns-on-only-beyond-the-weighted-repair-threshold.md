# NB-049 — ambient-dual localization turns on only beyond the weighted repair threshold

**Status:** `EXACT-DERIVED + METHOD-OBSTRUCTION + SHARP-SCALE-ALIGNMENT + LOCALIZATION/COMPRESSION-SEPARATION + CLUE-NARROWING`. `NB-047` localizes the logarithmic step-tail flow by bounding the ambient norm of the explicit dual `Omega_M`; `NB-039` identifies the sharp relative-compression threshold of the weighted skeleton; `NB-048` quantifies the residual one-line repair. These scales are not independent. The exact support floor of `Omega_M` forces every ambient-norm proof of relative tail-flow localization into the regime where the unrepaired weighted skeleton already preserves the Nyman distance.

For `2<=M<=N/2`, use the canonical residual and distance

\[
r_N=e-P_{V_N}e,
\qquad d_N=\|r_N\|,
\tag{1}
\]

the logarithmic prefix flow

\[
S_{M,N}=\sum_{L=1}^{M-1}\log\frac{L+1}{L}\,D_{L,N},
\tag{2}
\]

and the dual `Omega_M` from `NB-041`. `NB-046`--`NB-047` give the exact identity

\[
\boxed{S_{M,N}=d_N^2-\langle r_N,\Omega_M\rangle.}
\tag{3}
\]

The same dual satisfies the exact support floor

\[
\boxed{\|\Omega_M\|\ge M^{-1/2},}
\tag{4}
\]

because `Omega_M=1` on `(0,1/M]`. Hence the standard ambient Cauchy route

\[
\frac{|S_{M,N}-d_N^2|}{d_N^2}
\le \frac{\|\Omega_M\|}{d_N}
\tag{5}
\]

can yield a vanishing relative error only in a regime satisfying

\[
\boxed{
\frac{\|\Omega_M\|}{d_N}\to0
\quad\Longrightarrow\quad
M d_N^2\to\infty.
}
\tag{6}
\]

But `NB-039` proves, uniformly for `N>=2M`, the sharp weighted-skeleton equivalence

\[
\boxed{
M d_N^2\to\infty
\quad\Longleftrightarrow\quad
\frac{\widehat\kappa_{M,N}}{d_N}\to1,
}
\tag{7}
\]

where `widehat kappa_(M,N)` is the target distance after discarding the weighted tail. Therefore

\[
\boxed{
\frac{\|\Omega_M\|}{d_N}\to0
\quad\Longrightarrow\quad
\frac{\widehat\kappa_{M,N}}{d_N}\to1.
}
\tag{8}
\]

Thus **ambient-dual localization turns on only after the weighted quotient has already become asymptotically lossless at relative scale**. This is a method boundary, not a claim that the actual directional correlation in (3) cannot be much smaller than Cauchy predicts.

`NB-048` makes the same alignment explicit for recursive repair. Its recursively supplied one-line repair satisfies

\[
0\le \widetilde d_{M,N}^2-d_N^2
\le \frac{d_{\lfloor N/M\rfloor}^2}{M}
\le \frac1M.
\tag{9}
\]

Consequently every ambient-norm localization regime from (6) also obeys

\[
\boxed{
0\le
\frac{\widetilde d_{M,N}^2-d_N^2}{d_N^2}
\le \frac1{M d_N^2}
\longrightarrow0.
}
\tag{10}
\]

The recursive repair may still be geometrically interesting there, but it is already negligible for relative recovery of the finite Nyman distance.

## 1. The support floor fixes the ambient-norm threshold

Suppose a localization argument closes by proving

\[
\frac{\|\Omega_{M_N}\|}{d_N}\longrightarrow0
\tag{11}
\]

for some predeclared cutoff sequence `M_N<=N/2`. The lower bound (4) gives

\[
0\le \frac1{\sqrt{M_N}\,d_N}
\le \frac{\|\Omega_{M_N}\|}{d_N},
\tag{12}
\]

so (11) forces

\[
M_Nd_N^2\longrightarrow\infty.
\tag{13}
\]

There is no room to evade this implication by sharpening the *ambient norm estimate*: the obstruction is the actual norm itself, not the quality of its known upper bound.

Conversely, on any subsequence for which

\[
M_Nd_N^2\le C<\infty,
\tag{14}
\]

one has

\[
\boxed{
\frac{\|\Omega_{M_N}\|}{d_N}
\ge \frac1{\sqrt{M_Nd_N^2}}
\ge C^{-1/2}.
}
\tag{15}
\]

Therefore no proof whose decisive step is simply the ambient estimate (5) can establish `S_(M_N,N)=(1+o(1))d_N^2` in the critical/subcritical regime (14). A successful proof there would have to use the orientation of `r_N` relative to `Omega_M`, cancellation inside the exact shell representation, or another relation stronger than an ambient norm product.

This distinction is essential. Equation (15) **does not** imply

\[
|\langle r_N,\Omega_M\rangle|\not=o(d_N^2).
\tag{16}
\]

The scalar product can be much smaller than `d_N||Omega_M||`. The result rules out only an ambient-norm route to the desired relative localization.

## 2. The same parameter is the exact weighted-compression threshold

`NB-039` gives, for `N>=2M`,

\[
\frac{\log2}{M}
\le \widehat\kappa_{M,N}^2-d_N^2
\le \frac1M.
\tag{17}
\]

Dividing by `d_N^2` yields

\[
\frac{\log2}{Md_N^2}
\le \frac{\widehat\kappa_{M,N}^2}{d_N^2}-1
\le \frac1{Md_N^2}.
\tag{18}
\]

Hence `Md_N^2` is not merely a sufficient scale: it exactly governs relative target loss for this weighted quotient. Combining (12) and (18) shows that the support mass responsible for the ambient-dual obstruction and the target mass discarded by the quotient meet at the same dimensionless parameter

\[
\boxed{M d_N^2.}
\tag{19}
\]

When this parameter diverges, the quotient is already relatively faithful and ambient localization may become available. When it stays bounded, the quotient can lose a macroscopic fraction of `d_N^2`, while the dual support floor prevents Cauchy from proving relative prefix localization. The regime in which a repair bridge would actually change the relative target distance is therefore precisely the regime that ambient-norm localization cannot reach.

## 3. The concrete NB-047 localization window is already beyond the repair threshold

`NB-047` uses

\[
V(x)=(\log x)^{3/5}(\log\log x)^{-1/5}
\tag{20}
\]

and proves that a sequence satisfying

\[
\frac{V(M_N)}{\log\log N}\longrightarrow\infty
\tag{21}
\]

has

\[
S_{M_N,N}=(1+o(1))d_N^2.
\tag{22}
\]

Since `V(M)<=log M` eventually, (21) implies

\[
\frac{\log M_N}{\log\log N}\longrightarrow\infty,
\tag{23}
\]

and therefore

\[
\frac{M_N}{\log N}\longrightarrow\infty.
\tag{24}
\]

Burnol's unconditional lower bound gives, for every fixed `0<eta<mathfrak B_zeta` and all sufficiently large `N`,

\[
d_N^2\ge\frac{\eta}{\log N}.
\tag{25}
\]

Thus every `NB-047` cutoff that also remains in the weighted-skeleton range `M_N<=N/2` eventually satisfies

\[
M_Nd_N^2\ge \eta\frac{M_N}{\log N}
\longrightarrow\infty.
\tag{26}
\]

For such cutoffs,

\[
\boxed{
\frac{S_{M_N,N}}{d_N^2}\to1,
\qquad
\frac{\widehat\kappa_{M_N,N}}{d_N}\to1,
\qquad
\frac{\widetilde d_{M_N,N}^2}{d_N^2}\to1.
}
\tag{27}
\]

The concrete deterministic choice from `NB-047`,

\[
M_N=\left\lceil\exp((\log\log N)^{5/3+\varepsilon})\right\rceil,
\tag{28}
\]

is `N^{o(1)}`, so it does satisfy `M_N<=N/2` eventually. It is still superlogarithmic by far, whereas the conjectural scale `d_N^2\asymp1/\log N` places the relative weighted-repair threshold near `M\asymp\log N`.

Therefore the first test proposed by `CLUE-localized-tail-flow-controls-recursive-repair`—compare the localized prefix with the recursive repair at the concrete `NB-047` scale—is asymptotically non-discriminating. Both the source-flow localization and relative target preservation already hold there for independent reasons.

## 4. What remains open below the threshold

The durable question survives, but in a narrower regime. To make the localized directional flow informative about a repair that is non-negligible at relative scale, one must work with

\[
M d_N^2=O(1),
\tag{29}
\]

or at least avoid assuming its divergence. At the conjectural `d_N^2\asymp1/\log N` scale this means cutoffs of order `\log N`, rather than the doubly-logarithmic stretched-exponential cutoff currently obtained from the Vinogradov--Korobov ambient estimate.

A positive bridge in this regime could still be a direct source-computable inequality controlling the `NB-048` repair slack from selected `D_(L,N)`, a directional estimate for `\langle r_N,\Omega_M\rangle` that beats Cauchy, or a different witness family whose norm/support floor is lower while retaining the required target information. This finding proves none of those possibilities impossible.

Likewise, the fact that the `NB-047` prefix contains essentially all of `d_N^2` does not make the prefix source-computable: its individual discrepancies still contain optimal coefficient tails. The present result is about the **scale compatibility of two exact reductions**, not about an algorithm for constructing the finite projector.

## 5. Prior art, audit, and research consequence

No new external theorem is load-bearing. The ingredients are the line-local exact partial-flow identity and support floor of `NB-041`/`NB-047`, the sharp weighted target-loss estimate of `NB-039`, the recursive repair bound of `NB-048`, and Burnol's already anchored unconditional lower bound. Cauchy--Schwarz and the projection comparisons are elementary.

A targeted audit around finite Nyman--Beurling approximation, dilation methods, quantitative distance bounds, and zero-free-region approximation did not change the classification: the generic approximation machinery and the individual quantitative ingredients are prior art, while the useful line-local content here is the exact alignment of the ambient-dual localization gate with the weighted-compression parameter `Md_N^2`. Search absence is not a priority claim, and no addition to `SOURCES.md` is required.

The practical consequence is a sharper separation of tasks. Improving the unconditional **ambient** bound on `||Omega_M||` can move the deterministic localization window only within the regime allowed by (6); it cannot by itself enter the repair-relevant critical corridor. Future work on the localized-tail-flow/recursive-repair bridge should therefore target directional cancellation or a direct source-to-slack relation at `Md_N^2=O(1)`, rather than further shrinking the same ambient-dual norm and testing the bridge only at the existing `NB-047` cutoff.