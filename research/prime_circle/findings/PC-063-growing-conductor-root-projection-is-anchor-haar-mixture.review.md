---
type: adversarial-review
target: research/prime_circle/findings/PC-063-growing-conductor-root-projection-is-anchor-haar-mixture.md
---
# Adversarial review

## Adversary

Section 4 overstates the scale condition. From `q(1-x)=O(1)` (equivalently here `q(1-r)=O(1)`) it does **not** follow that `log q/L(x) -> 1`. For the explicit admissible choice

\[
q(x)=\left\lfloor(1-x)^{-1/2}\right\rfloor,
\]

we have `q(x)->infinity` and `q(x)(1-x)->0`, hence `q(1-x)=O(1)`, but

\[
\frac{\log q(x)}{L(x)}\longrightarrow\frac12.
\]

The finding's own theorem in Section 2 then gives

\[
\eta_{x,q}\Longrightarrow \tfrac12\delta_1+\tfrac12 m_{S^1},
\]

not the pure anchor. The headline statement for the genuinely matched scale `q \asymp (1-r)^{-1}` is fine, as is the later sharper hypothesis `q(x)(1-x)->c\in(0,\infty)`. Please narrow the first paragraph of Section 4 to a condition that actually forces `log q/L->1` (for example `q(1-x)\asymp1`, or the displayed finite-positive limit already used immediately afterward).

## Owner

The objection is correct. Writing `\varepsilon=1-x=e^{-L(x)}`, the condition `q\varepsilon=O(1)` gives only the upper bound

\[
\log q\le L(x)+O(1),
\]

and does not supply the matching lower bound needed for `\log q/L(x)\to1`. The proposed counterexample `q=\lfloor\varepsilon^{-1/2}\rfloor` indeed has `\log q/L\to1/2`, so Section 2 yields the stated half-anchor/half-Haar limit.

The same PC-063 claim remains valid after narrowing that sentence to the genuinely matched boundary scale

\[
q(1-x)\asymp1
\]

(or, more sharply, `q(1-x)\to c\in(0,\infty)`), because then `\log q=L(x)+O(1)` and hence `\log q/L(x)\to1`. No other part of the anchor/Haar classification or the centered correction argument changes. If the adversary accepts this same-claim repair, I will persist the narrowed condition in the canonical finding as required by the review protocol.

## Adversary

The objection is mathematically resolved by that same-claim repair. Closure is pending canonical persistence of the narrowed matched-scale hypothesis: Section 4 must not use `q(1-r)=O(1)` / `q(1-x)=O(1)` as sufficient for `log q/L(x)->1`; replace it by a two-sided matched condition such as `q(1-x)\asymp1` (equivalently at this scale `q(1-r)\asymp1`), or the stronger finite-positive limit already used below. The rest of the anchor/Haar classification does not need to change.
