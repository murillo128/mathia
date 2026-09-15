# NB-151 — Fixed-scale horizontal differencing forces a neighboring logarithmic adverse packet

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + XI-CONSERVATION + FIXED-SCALE-OBSTRUCTION + NB-150-FRONTIER`.

`NB-150` closed the mesoscopic escape for the two-point horizontal signed sampler: when the horizontal scale `L_G` tends to infinity, ordinary Riemann--von Mangoldt density fills both Poisson lobes with `Theta(log G)` actual-zero mass. It deliberately left `L=O(1)` open, because on a fixed ordinate scale the classical `O(log G)` zero-count remainder is as large as the expected main term and therefore cannot force either lobe to be populated.

At fixed horizontal scale there is, however, a stronger source-specific identity that `NB-150` did not use. The horizontal difference of `xi'/xi` is an **absolutely convergent signed sum over the actual zeros**, and all nonzero Hadamard background terms cancel before any positive/negative separation. Since the two exterior sample points remain a fixed distance inside `Re s>1`, the resulting total signed zero charge is only `O(1)`. Consequently, if an exceptional target packet itself contributes `Omega(log G)` positive charge, actual zeros in the adverse lobe must contribute matching `Omega(log G)` negative charge. A unit-interval consequence of Riemann--von Mangoldt then shows that this debt cannot be exported to remote heights: it is carried by `Theta(log G)` zeros in a bounded neighboring ordinate annulus.

Fix constants

\[
L>0,\qquad c>1,
\tag{1}
\]

and put

\[
s_1=1+L+iG,
\qquad
s_2=1+cL+iG.
\tag{2}
\]

For a nontrivial zeta zero `rho=beta+i gamma`, counted with multiplicity, write

\[
\theta:=1-\beta\in(0,1),
\qquad
y:=G-\gamma,
\tag{3}
\]

and define the signed horizontal-difference charge

\[
Q_{L,c}(\rho;G)
:=
\frac{L+\theta}{(L+\theta)^2+y^2}
-
\frac{cL+\theta}{(cL+\theta)^2+y^2}.
\tag{4}
\]

A direct factorization gives

\[
\boxed{
Q_{L,c}(\rho;G)
=
\frac{(c-1)L\big((L+\theta)(cL+\theta)-y^2\big)}
{\big((L+\theta)^2+y^2\big)
 \big((cL+\theta)^2+y^2\big)}.
}
\tag{5}
\]

Thus every zero with

\[
|\gamma-G|<\sqrt c\,L
\tag{6}
\]

has positive charge, while negative charge can occur only when

\[
|\gamma-G|>
\sqrt{(L+\theta)(cL+\theta)}
\ge \sqrt c\,L.
\tag{7}
\]

Now fix also

\[
0<h<\sqrt c\,L,
\qquad
\kappa>0,
\tag{8}
\]

and suppose that for arbitrarily large `G` there is a packet `F_G` of positive-ordinate nontrivial zeros satisfying

\[
|\gamma-G|\le h
\qquad(\rho\in F_G),
\tag{9}
\]

with multiplicity-weighted cardinality

\[
d_G:=|F_G|\ge\kappa\log G.
\tag{10}
\]

Then there exists a constant

\[
R=R(L,c,h,\kappa)>\sqrt c\,L
\tag{11}
\]

such that, for all sufficiently large such `G`,

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\
                  \gamma>0\\
                  |\gamma-G|\le R}}
\bigl(Q_{L,c}(\rho;G)\bigr)_-
\gg_{L,c,h,\kappa}\log G,
}
\tag{12}
\]

where `(u)_-:=max(-u,0)`. In particular,

\[
\boxed{
\#\left\{
\rho:\ \gamma>0,\ \sqrt c\,L<|\gamma-G|\le R,\ Q_{L,c}(\rho;G)<0
\right\}
\asymp_{L,c,h,\kappa,R}\log G.
}
\tag{13}
\]

So a fixed-scale two-point horizontal sampler cannot logarithmically charge one narrow exceptional packet while leaving its adverse discrete lobe sparse. **A logarithmic target packet forces a second logarithmic population of actual zeros at bounded ordinate distance.**

## 1. Horizontal `xi'/xi` differencing gives an exact discrete conservation law

Use the completed zeta function

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{14}
\]

The genus-one Hadamard representation gives, in the standard symmetric regularization,

\[
\frac{\xi'}{\xi}(s)
=
B+
\sum_\rho
\left(
\frac1{s-\rho}+\frac1\rho
\right).
\tag{15}
\]

Subtracting `(15)` at the two points `(2)` cancels both `B` and every `1/rho` regularizer. The difference is absolutely summable because

\[
\frac1{s_1-\rho}-\frac1{s_2-\rho}
=
\frac{s_2-s_1}{(s_1-\rho)(s_2-\rho)}
\tag{16}
\]

has quadratic decay in `|gamma|`. Taking real parts therefore yields the exact identity

\[
\boxed{
\sum_\rho Q_{L,c}(\rho;G)
=
\Re\left(
\frac{\xi'}{\xi}(s_1)
-
\frac{\xi'}{\xi}(s_2)
\right).
}
\tag{17}
\]

The right side is bounded uniformly in `G`. Indeed,

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+
\frac1{s-1}
-
\frac12\log\pi
+
\frac12\psi(s/2)
+
\frac{\zeta'}{\zeta}(s),
\tag{18}
\]

where `psi=Gamma'/Gamma`. At the fixed real parts `1+L` and `1+cL`, the Euler series for `zeta'/zeta` is absolutely convergent and hence `O_{L,c}(1)`. The rational terms are bounded, and the leading `log G` parts of the two digamma terms cancel under horizontal differencing. Thus

\[
\boxed{
\sum_\rho Q_{L,c}(\rho;G)=O_{L,c}(1).
}
\tag{19}
\]

This is the fixed-scale replacement for the asymptotic lobe sampling used in `NB-150`. Ordinary local Riemann--von Mangoldt cannot resolve a fixed window to `o(log G)`, but `(19)` does not estimate the two lobes separately: it constrains their **signed difference exactly enough** for a target-conditioned argument.

Zeros with negative ordinate do not carry a hidden logarithmic part of `(19)`. For `gamma<0`,

\[
|G-\gamma|=G+|\gamma|,
\tag{20}
\]

and `(4)` gives

\[
|Q_{L,c}(\rho;G)|
\ll_{L,c}(G+|\gamma|)^{-2}.
\tag{21}
\]

Using `N(T)\ll T\log(T+2)` and dyadic summation,

\[
\sum_{\gamma<0}
|Q_{L,c}(\rho;G)|
\ll_{L,c}
\frac{\log G}{G}
=o(1).
\tag{22}
\]

Hence `(19)` may equivalently be read on the positive-ordinate zero set up to `o(1)`.

## 2. A logarithmic target packet creates logarithmic signed debt

For every `rho in F_G`, equations `(5)` and `(9)` give the uniform lower bound

\[
Q_{L,c}(\rho;G)
\ge q_*(L,c,h)>0,
\tag{23}
\]

where one explicit admissible choice is

\[
\boxed{
q_*(L,c,h)
:=
\frac{(c-1)L(cL^2-h^2)}
{\big((L+1)^2+h^2\big)
 \big((cL+1)^2+h^2\big)}.
}
\tag{24}
\]

Indeed, the numerator factor in `(5)` is at least `cL^2-h^2`, while each denominator factor is at most the corresponding factor in `(24)`. Therefore

\[
\sum_{\rho\in F_G}Q_{L,c}(\rho;G)
\ge q_*d_G
\ge \kappa q_*\log G.
\tag{25}
\]

Split all remaining positive-ordinate zeros into their positive and negative charges. Combining `(19)`, `(22)`, and `(25)` gives

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\\gamma>0}}
\bigl(Q_{L,c}(\rho;G)\bigr)_-
\ge
q_*d_G-O_{L,c}(1).
}
\tag{26}
\]

Thus for `(10)` the actual adverse zero mass is already `Omega(log G)`. No Jordan majorant is being inserted here. Unlike `NB-149`, `(26)` is a statement about the **true discrete zero set**: the target's positive charge itself forces an equally large negative debt because the complete signed sum is only `O(1)`.

There is also an `O(log G)` upper bound for the total absolute charge. The Riemann--von Mangoldt estimate already anchored in this line implies

\[
N(t+1)-N(t)\ll\log(t+2).
\tag{27}
\]

On a unit shell `k<=|gamma-G|<k+1` beyond a fixed `L,c`-dependent radius, `(4)` gives

\[
|Q_{L,c}(\rho;G)|\ll_{L,c}k^{-2}.
\tag{28}
\]

Summing `(28)` with `(27)`, and treating the bounded central region separately, yields

\[
\sum_{\gamma>0}|Q_{L,c}(\rho;G)|
\ll_{L,c}\log G.
\tag{29}
\]

Hence the adverse mass forced in `(26)` is genuinely `Theta(log G)` whenever the target rank is `Theta(log G)`.

## 3. The debt cannot escape to remote ordinates

The same shell estimate localizes the negative debt. For every sufficiently large fixed `R`, splitting the positive ordinates into `R<=|gamma-G|<=G` and the farther tail gives

\[
\boxed{
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_{L,c}(\rho;G)|
\ll_{L,c}
\frac{\log G}{R}
+
\frac{\log G}{G}.
}
\tag{30}
\]

The first term comes from

\[
\sum_{k\ge R}^{G}
\frac{O(\log G)}{k^2}
\ll
\frac{\log G}{R},
\tag{31}
\]

while for `k>=G` one uses `O(log(k+2))` zeros per unit shell and obtains `O(log G/G)`.

Choose the fixed constant `R` in `(11)` sufficiently large that the first term of `(30)` is at most, say, `(kappa q_*/2) log G`. Combining `(26)` and `(30)` proves `(12)`.

Every negative contribution in `(12)` automatically lies outside the central sign boundary `(7)`, hence in the bounded annulus

\[
\sqrt c\,L
<
|\gamma-G|
\le R.
\tag{32}
\]

Moreover each single zero has bounded negative charge:

\[
\bigl(Q_{L,c}(\rho;G)\bigr)_-
\le
\frac1L+
\frac1{cL}.
\tag{33}
\]

Thus `(12)` forces `Omega(log G)` distinct multiplicity-counted zeros in `(32)`. Conversely `(27)` gives only `O_{L,c,R}(log G)` zeros in that fixed annulus. This proves `(13)`.

Since `(32)` is the union of two intervals of fixed total length, one may partition it into finitely many subintervals of any fixed positive width. At least one such subinterval contains `Omega(log G)` adverse zeros. Therefore the conclusion can be read literally as a **neighboring logarithmic confluence packet**, not merely as a diffuse weighted tail.

## 4. Why the fixed-scale loophole in `NB-150` is now closed

For mesoscopic `L_G`, `NB-150` used mean zero density to prove that both lobes are populated irrespective of any exceptional target packet. That proof necessarily broke at `L=O(1)`, because the Riemann--von Mangoldt remainder is then the same order as the expected local count.

The present argument conditions on exactly the exceptional geometry relevant to the Nyman obstruction. Once a target packet has `d_G>=kappa log G`, its fixed-scale positive charge is itself `Omega(log G)`. The completed zeta function then leaves no room for this charge to disappear into the prime side or the Hadamard background: the horizontal `xi'/xi` difference is only `O(1)`. Actual zeros must supply the opposite charge, and quadratic kernel decay keeps most of that charge at bounded vertical distance.

This closes the two-point horizontal fixed-scale escape left explicitly open in `NB-150`:

\[
\boxed{
\begin{array}{c}
L_G\to\infty,\ L_G=o(G)
\quad\text{(`NB-150`): both lobes are background-filled},\\[4pt]
L=O(1),\ d_G\gg\log G
\quad\text{(`NB-151`): the target packet forces a neighboring adverse packet}.
\end{array}
}
\tag{34}
\]

The two mechanisms are different. `NB-150` is unconditional mean-density sampling of a broad profile; `NB-151` is a target-conditioned conservation law for a microscopic profile.

## 5. Stress tests and boundaries

- **No RH, simplicity, pair correlation, or local asymptotic zero count is used.** Multiplicity is counted throughout, and the only zero-count input beyond the `xi` product is the classical `O(log T)` unit-interval upper bound derived from Riemann--von Mangoldt.
- **The result does not exclude logarithmic confluence by itself.** It says an isolated logarithmic packet cannot coexist with a harmless adverse lobe for this sampler. A second nearby logarithmic population is still compatible with the `O(log G)` local zero-count budget.
- **Paired exceptional packets are not ruled out.** Re-centering the argument on the adverse packet may return charge toward the original packet, so naive iteration does not produce an immediate contradiction.
- **The theorem is still two-point and same-ordinate.** General signed measures, vertical offsets, many-point finite differences, or kernels engineered to have several alternating lobes are not classified here.
- **The prime side is bounded, not assumed to cancel.** For fixed `L>0`, absolute convergence in `Re s>1` gives `zeta'/zeta(s_j)=O_{L,c}(1)`. Hence an `Omega(log G)` target charge cannot be absorbed there.
- **Shrinking horizontal scales remain separate.** If `L=L_G->0`, the Euler-product bound near `Re s=1` deteriorates and the kernel geometry changes. `NB-151` makes no claim in that regime.

A direct falsification test is available. Fix explicit `L,c,h,kappa` obeying `(8)`, find a sequence of packets satisfying `(9)`--`(10)`, and compute the signed charges `(4)`. If the negative mass outside the packet were `o(log G)`, then the absolutely convergent identity `(17)` would force the horizontal difference `xi'/xi(s_1)-xi'/xi(s_2)` to grow like `log G`, contradicting the fixed-half-plane bound from `(18)`.

## 6. Prior-art and novelty audit

The ingredients are classical: Hadamard factorization of `xi`, the logarithmic derivative in `Re s>1`, Poisson kernels attached to zeros, and the Riemann--von Mangoldt local upper bound. This line already anchors the required zeta and zero-count sources in `SOURCES.md`; no new external theorem is load-bearing here.

A structure-based literature audit finds extensive use of Poisson kernels and logarithmic derivatives in explicit-formula arguments, including modern bandlimited Poisson-kernel treatments of `Re zeta'/zeta`. The present delta is narrower and source-conditioned: subtract two exterior `xi'/xi` evaluations at fixed horizontal separation, exploit the resulting **absolutely convergent discrete conservation law**, and condition on a logarithmic target confluence to force a neighboring logarithmic adverse population. No exact prior-art theorem packaging this target-to-adverse-packet implication was identified, so the result is recorded as a derived route obstruction rather than as a new general zero-statistics theorem.

## 7. Consequence for the Nyman--Beurling frontier

`NB-148` showed that zero-mass signed sampling exports an equal continuous negative lobe; `NB-149` showed that Jordan domination repays the full positive logarithmic budget; `NB-150` showed that mesoscopic horizontal spreading makes both lobes logarithmically occupied by the actual zero set. `NB-151` now removes the most obvious microscopic exception for the same two-point architecture: **if the positive microscopic lobe contains the logarithmic target packet one hoped to isolate, the completed zeta function itself forces a neighboring logarithmic negative packet.**

The surviving signed route must therefore change architecture, not merely scale. It must use a more structured many-point signed kernel, vertical/nonuniform sampling, a shrinking scale with genuinely different prime-side behavior, or couple the signed identity directly to target-bearing Nyman data before lobe separation. Fixed-scale two-point horizontal differencing does not provide an isolated positive certificate for a logarithmic confluence packet.