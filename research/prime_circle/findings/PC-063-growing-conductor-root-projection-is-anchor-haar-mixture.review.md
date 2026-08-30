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