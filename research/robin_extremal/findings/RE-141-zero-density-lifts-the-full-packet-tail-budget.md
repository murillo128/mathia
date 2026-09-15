# RE-141 — zero density lifts the full-packet tail budget

**Status:** `DERIVED + FINITE-ZERO-EDGE + FULL-SUBEDGE-PACKET + ZERO-DENSITY-WEIGHTED-TAIL + PARTIAL-SUMMATION + TURAN-SPLICE + STRICTLY-IMPROVED-CUTOFF-BUDGET + COMPLEXITY-STILL-OPEN + RIGHTMOST-GAIN-STILL-OPEN + PRIOR-ART-AUDITED`.

`RE-140` closes the finite-core/full-tail bookkeeping for the leading Robin packet, but it deliberately bounds the omitted zeros only by the absolute Riemann--von Mangoldt envelope

\[
\|\mathcal S_0-\mathcal S_{0,T}\|_\infty
\ll \frac{\log T}{T}.
\]

That estimate forgets the defining source information of the packet: every omitted zero is constrained to the fixed off-critical strip `beta>=sigma_0>1/2`. The same zero-density input already anchored in the Robin line converts that restriction into an additional cutoff power.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad 0<\kappa<1,
\tag{1}
\]

in the attained finite-edge branch, and retain the full leading strict-subedge packet of `RE-140`,

\[
\mathcal S_0(u)
=
2\Re
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\beta:=\Re\rho<\Theta\\
\gamma:=\Im\rho>0}}
\frac{e^{-(\Theta-\beta)u}e^{i\gamma u}}
{\rho(1-\rho)}.
\tag{2}
\]

For `T>=2`, let `\mathcal S_{0,T}` denote the contribution from `0<gamma<=T`. Put

\[
\nu_I(\sigma):=
\frac{3(1-\sigma)}{2-\sigma},
\qquad \frac12<\sigma<1,
\tag{3}
\]

the classical Ingham zero-density exponent, so that on every fixed compact substrip of `(1/2,1)`,

\[
N(\sigma,X)
:=\#\{\rho=\beta+i\gamma:\beta\ge\sigma,\ 0<\gamma\le X\}
\ll_\sigma X^{\nu_I(\sigma)}(\log X)^C
\tag{4}
\]

for a fixed logarithmic power `C`.

Then for every `epsilon>0`,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_0(u)-\mathcal S_{0,T}(u)|
\ll
T^{-2+\nu_I(\Theta)+\epsilon}(\log T)^C
+
 e^{-c_\epsilon U}\frac{\log T}{T}.
}
\tag{5}
\]

Here `c_epsilon>0` depends only on the fixed strip, `kappa`, and the choice of `epsilon`. Since `nu_I(Theta)<1`, the first term is strictly smaller than the `T^{-1}` absolute tail used in `RE-140`.

The resulting full-packet Turán budget changes correspondingly. Under the same scale hypotheses as `RE-140`,

\[
T=U^B,
\qquad
M_0(U)\ge cU^{-A},
\qquad
G(U,T)\ge cT^{-\eta},
\qquad
N_T\le \alpha\log T,
\tag{6}
\]

a sufficient asymptotic condition becomes

\[
\boxed{
\frac AB+\eta+\Lambda_\kappa\alpha
<
2-\nu_I(\Theta),
}
\tag{7}
\]

with arbitrary fixed slack absorbed by `epsilon`, rather than the `RE-140` condition with right-hand side `1`.

For Ingham's exponent,

\[
\boxed{
2-\nu_I(\Theta)
=
\frac{1+\Theta}{2-\Theta}.
}
\tag{8}
\]

Thus every fixed attained edge `Theta>1/2` gains a strictly positive amount over the crude absolute-tail budget, with the gain increasing as the edge moves right.

The improvement does **not** close the full-packet problem by itself. The geometry-free amplitude comparison of `RE-140` corresponds to `eta=2`, while `2-nu_I(Theta)<2` for every attained `Theta<1`. Even with zero mode-count cost and arbitrarily large `B`, the generic `T^{-2}` rightmost-amplitude transfer remains too weak. Zero density therefore removes much of the exterior-tail loss but leaves the rightmost-gain and effective-complexity questions genuinely live.

## 1. Weighted zero-density tail

For large `gamma` and `beta` in a fixed strip,

\[
\left|\frac1{\rho(1-\rho)}\right|
\ll \frac1{\gamma^2}.
\tag{9}
\]

Fix a number

\[
\sigma_1\in(\sigma_0,\Theta).
\tag{10}
\]

The high-height zeros with `beta>=sigma_1` satisfy, by Stieltjes partial summation,

\[
\sum_{\substack{\gamma>T\\\beta\ge\sigma_1}}
\frac1{\gamma^2}
=
\int_T^\infty t^{-2}\,dN(\sigma_1,t).
\tag{11}
\]

Integrating by parts gives

\[
\int_T^\infty t^{-2}\,dN(\sigma_1,t)
\ll
\frac{N(\sigma_1,T)}{T^2}
+
\int_T^\infty\frac{N(\sigma_1,t)}{t^3}\,dt.
\tag{12}
\]

Using (4), and noting that `nu_I(sigma_1)<1<2`, both terms are bounded by

\[
\boxed{
\sum_{\substack{\gamma>T\\\beta\ge\sigma_1}}
\frac1{\gamma^2}
\ll_{\sigma_1}
T^{-2+\nu_I(\sigma_1)}(\log T)^C.
}
\tag{13}
\]

No phase cancellation has been used. The gain comes entirely from the fact that high zeros in the right half-strip are sparse enough that the `gamma^{-2}` Robin coefficient is summable with an improved exponent.

## 2. The farther-left tail is exponentially damped in the observation window

Split the omitted zeros in (2) into

\[
\beta\ge\sigma_1
\qquad\text{and}\qquad
\sigma_0\le\beta<\sigma_1.
\tag{14}
\]

For the first set, the horizontal factor has modulus at most one, so (13) directly controls its contribution.

For the second set, every

\[
u\in[(1-\kappa)U,U]
\]

satisfies

\[
 e^{-(\Theta-\beta)u}
\le
 e^{-(\Theta-\sigma_1)(1-\kappa)U}.
\tag{15}
\]

The ordinary Riemann--von Mangoldt estimate, together with (9), gives the global absolute coefficient tail

\[
\sum_{\gamma>T}\frac1{\gamma^2}
\ll \frac{\log T}{T}.
\tag{16}
\]

Hence

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
\left|
\sum_{\substack{\gamma>T\\
\sigma_0\le\beta<\sigma_1}}
\frac{e^{-(\Theta-\beta)u}e^{i\gamma u}}
{\rho(1-\rho)}
\right|
\ll
 e^{-(\Theta-\sigma_1)(1-\kappa)U}
\frac{\log T}{T}.
}
\tag{17}
\]

Again no signed cancellation is required.

## 3. Move the density line arbitrarily close to the edge

The function `nu_I(sigma)` is continuous on `(1/2,1)`. Given `epsilon>0`, choose `sigma_1<Theta` sufficiently close to `Theta` that

\[
\nu_I(\sigma_1)
\le
\nu_I(\Theta)+\epsilon.
\tag{18}
\]

Then (13) and (17), with conjugate pairing absorbed into the constant, give (5). The exponentially damped term has

\[
c_\epsilon
=(\Theta-\sigma_1)(1-\kappa)>0.
\tag{19}
\]

This split is important. Applying zero density only at the fixed lower strip edge `sigma_0` would give a valid but unnecessarily weak exponent `nu_I(sigma_0)`. The Robin kernel itself suppresses the part of the tail bounded away from `Theta`, so the polynomial cutoff cost is governed by zero density **arbitrarily close to the actual edge**.

The same argument works with any stronger locally valid zero-density law

\[
N(\sigma,T)
\ll T^{\nu(\sigma)+o(1)}
\tag{20}
\]

provided a fixed neighborhood immediately to the left of `Theta` is controlled. Then the right side of (7) becomes `2-nu(Theta-)`, interpreted with the appropriate upper limiting exponent. Equation (7) is stated with Ingham because that input is continuous, unconditional, and already anchored in this research line.

## 4. Splice with the finite-core Turán witness

`RE-140` supplies constants `c_(Theta,kappa)>0` and

\[
\Lambda_\kappa
=2\log\frac{16e}{\kappa}
\tag{21}
\]

such that some `u_*` in the same relative window satisfies

\[
|\mathcal S_{0,T}(u_*)|
\ge
c_{\Theta,\kappa}
G(U,T)e^{-\Lambda_\kappa N_T}M_0(U).
\tag{22}
\]

Under (6), the finite-core lower bound is

\[
\gg
U^{-A}
T^{-\eta-\Lambda_\kappa\alpha}
=
U^{-A-B(\eta+\Lambda_\kappa\alpha)}.
\tag{23}
\]

The polynomial part of (5) is

\[
T^{-2+\nu_I(\Theta)+\epsilon}(\log T)^C
=
U^{-B(2-\nu_I(\Theta)-\epsilon)}
(\log U)^C.
\tag{24}
\]

Thus the core dominates the omitted tail whenever

\[
A+B(\eta+\Lambda_\kappa\alpha)
<
B(2-\nu_I(\Theta)-\epsilon).
\tag{25}
\]

Because (7) is strict, `epsilon>0` can be chosen small enough that (25) holds. The exponentially damped term in (5) is negligible for every fixed polynomial cutoff `T=U^B`. This proves the advertised budget.

The change from `1` to `2-nu_I(Theta)` is therefore not heuristic: it is exactly the amount of reciprocal-height tail recovered by inserting fixed-strip zero density before taking absolute values over all omitted zeros.

## 5. What this changes, and what it does not

### Zero density helps through the tail, not through raw Turán cardinality

`RE-140` already observes that substituting a polynomial zero-density bound directly into the factor `exp(-Lambda_kappa N_T)` is useless for polynomial visibility: the Turán floor pays exponentially for the retained mode count. The present argument uses the same source information in a different place. Weighted by `gamma^{-2}`, polynomial zero density becomes a **polynomially improved exterior tail**, which is exactly the scale needed by the core/tail comparison.

Thus the conclusion is not that the mode-count obstruction has disappeared. It is that zero density was being charged to the wrong side of the budget if it was used only as a cardinality estimate.

### The generic rightmost transfer still cannot close the budget

`RE-140` has the geometry-free comparison

\[
G(U,T)\gg T^{-2}.
\tag{26}
\]

This corresponds to `eta=2`. Since

\[
\nu_I(\Theta)>0
\qquad(\Theta<1),
\tag{27}
\]

the right side of (7) is strictly below `2`. Consequently (7) fails with `eta=2` even if `A/B` and `alpha` are formally sent to zero.

So the zero-density tail lift narrows the source gap but does not manufacture the missing rightmost gain. The remaining horizontal/height coupling must still recover at least approximately `T^{nu_I(Theta)}` relative to the crude `T^{-2}` amplitude transfer, before strong-atom and complexity costs are paid.

### No zero spacing or simplicity input is used

The count `N(sigma,T)` includes multiplicity. The argument does not assume simple zeros, pair correlation, minimum spacing, or a short-interval zero-count theorem. Clustering at high ordinate can be arbitrarily bad as long as the fixed-strip density estimate holds globally.

### This remains a sufficient certificate, not a statement about the actual sign pattern

The tail estimate is absolute. It does not claim the omitted zeros align adversarially, nor that the finite-core Turán witness is close to sharp. A signed-tail theorem could improve (5) further, and a different infinite-packet observability theorem could bypass truncation entirely.

## 6. Quantitative size of the recovered cutoff power

For the classical Ingham exponent,

\[
2-\nu_I(\Theta)
=
2-\frac{3(1-\Theta)}{2-\Theta}
=
\frac{1+\Theta}{2-\Theta}.
\tag{28}
\]

At the critical boundary `Theta=1/2`, this equals `1`, matching the crude `T^{-1}` scale and giving no improvement. For every fixed off-critical attained edge `Theta>1/2`, it is strictly larger than `1`; as `Theta` approaches `1`, it approaches `2`.

This is structurally the right behavior. The farther right the edge lies, the rarer such zeros are under zero-density theory, while the Robin coefficient still contributes the same quadratic ordinate decay. The source therefore makes the high-height exterior progressively cheaper exactly in the regime where the false-RH edge is farther from the critical line.

## 7. Prior-art and novelty boundary

The load-bearing external theorem is Ingham's classical estimate for `N(sigma,T)`, already anchored in `SOURCES.md` and already used elsewhere in `robin_extremal`. The passage from (4) to (13) is standard Stieltjes partial summation, and the global `gamma^{-2}` tail in (16) is the same Riemann--von Mangoldt consequence already used by `RE-123` and `RE-140`. No new literature dependency is introduced, so `SOURCES.md` does not need to change.

A targeted literature scan also does not change the boundary: modern zero-density improvements can sharpen the numerical exponent in ranges where they apply, but they do not alter the architecture of the argument. Results about simple zeros, pair correlation, or short-interval zero statistics are not needed for (5) and do not by themselves remove the retained-mode Turán cost.

No novelty is claimed for weighted zero-density tails as a general analytic-number-theory technique. The durable line-specific delta is the splice with the exact `RE-140` gain/complexity certificate: it raises the available cutoff budget from `1` to `2-nu(Theta)` and separates two roles that had previously been conflated -- zero density is useful immediately for **exterior tail suppression**, while a genuinely new source input is still required for **effective finite-core complexity**.

## 8. Consequence for the Robin-extremal frontier

The full-packet problem after `RE-141` is quantitatively narrower than after `RE-140`. With a polynomial cutoff, the direct certificate now asks for

\[
\boxed{
\frac AB
+
\eta
+
\Lambda_\kappa\alpha
<
2-\nu(\Theta),
}
\tag{29}
\]

where `nu(Theta)` is any justified local zero-density exponent immediately to the left of the attained edge.

The exterior tail is therefore no longer the one-full-power obstruction suggested by the geometry-free Riemann--von Mangoldt bound. What survives is more specific: the source must provide enough **rightmost horizontal gain versus ordinate inflation** to improve the generic `eta=2`, and the Turán witness must pay for only logarithmically many effective modes, or be replaced by a certificate whose cost is not exponential in the raw retained cardinality.

This rules out one unproductive next move: merely sharpening the absolute `O(log T/T)` tail without using the off-critical location. Zero density already extracts a strictly stronger polynomial tail from information the line possesses. The next useful advance should attack the rightmost gain/effective-complexity side of (29), or replace the finite-core Turán architecture altogether.