# NB-043 — any power decay of the logarithmic tail dual forces a fixed zero-free strip

**Status:** `EXACT-DERIVED + ZERO-FREE-HALF-PLANE-IMPLICATION + POWER-DECAY-INDEX + DUAL-NORM-ORACLE-BOUNDARY + NEGATIVE/METHOD-BOUNDARY`. `NB-041` constructs the explicit logarithmic tail dual `\Omega_M`; `NB-042` identifies its near-square-root norm scale as exactly RH-equivalent. The obstruction begins much earlier than the square-root endpoint. Any fixed positive power decay of this same ambient selector already forces a fixed vertical zero-free strip for `\zeta`.

Use the notation of `NB-041`--`NB-042`,
\[
\Omega_M
=e-\sum_{L=1}^{M-1}\log\frac{L+1}{L}\,\Psi_L,
\tag{1}
\]
\[
\Theta(x)
:=1-\sum_{n\le x}\frac{\mu(n)}n\log\frac xn,
\qquad
m(x):=\sum_{n\le x}\frac{\mu(n)}n.
\tag{2}
\]
Those findings prove the exact identities
\[
\boxed{\langle e,\Omega_M\rangle=\Theta(M),}
\tag{3}
\]
and
\[
\Theta(x)-\Theta(y)
=-\int_y^x m(u)\,\frac{du}{u}.
\tag{4}
\]
They also establish the Mellin identity, initially for `Re s>0`,
\[
\boxed{
F(s):=\int_1^\infty\Theta(x)x^{-s-1}\,dx
=
\frac1s-\frac1{s^2\zeta(s+1)}.
}
\tag{5}
\]

The new consequence is the following quantitative one-way theorem. Let
\[
0<\alpha\le\frac12.
\tag{6}
\]
If
\[
\boxed{
\|\Omega_M\|_2=O(M^{-\alpha}),
}
\tag{7}
\]
then `\zeta` has no nontrivial zero in
\[
\boxed{\Re s>1-\alpha.}
\tag{8}
\]
By the functional equation, all nontrivial zeros consequently lie in the closed strip
\[
\boxed{
\alpha\le\Re\rho\le1-\alpha.
}
\tag{9}
\]

More robustly, the same conclusion follows from the epsilon-loss family
\[
\boxed{
\forall\varepsilon>0,
\qquad
\|\Omega_M\|_2
=O_\varepsilon(M^{-\alpha+\varepsilon}).
}
\tag{10}
\]
The endpoint `\alpha=1/2` recovers the reverse implication of `NB-042`, but the point here is the whole interval `0<\alpha<1/2`: even a very small polynomial improvement over the unconditional `O(1/\log M)` regime would already encode a genuinely uniform zero-free half-plane.

This does **not** give a converse for `\alpha<1/2`, does not improve the finite Nyman distance, and does not resolve the accepted weighted-skeleton target-data clue. It closes a broader version of the same norm-only route: the obstacle is not confined to the RH-critical square-root endpoint.

## 1. Selector norm decay transfers directly to the mollified Möbius defect

From (3) and `\|e\|_2=1`,
\[
|\Theta(M)|
\le\|\Omega_M\|_2.
\tag{11}
\]
Thus (10) gives, for every `\varepsilon>0`,
\[
\Theta(M)=O_\varepsilon(M^{-\alpha+\varepsilon})
\qquad(M\in\mathbb Z_{\ge2}).
\tag{12}
\]

The estimate extends to every real `x`. If `M\le x<M+1`, then (4) and the elementary global bound `|m(u)|\le1` from `NB-035` imply
\[
|\Theta(x)-\Theta(M)|
\le\int_M^{M+1}\frac{du}{u}
\ll\frac1M.
\tag{13}
\]
Since `\alpha\le1/2`, the interpolation error is smaller than the scale in (12). Therefore
\[
\boxed{
\Theta(x)=O_\varepsilon(x^{-\alpha+\varepsilon})
}
\tag{14}
\]
for every positive `\varepsilon`.

No estimate for the Nyman residual `d_N`, no density assumption, and no finite-section projection enters this step. The entire implication is carried by the target pairing of the explicit source-defined dual.

## 2. Mellin continuation turns every positive power into a zero-free half-plane

Assume (10) and suppose, for contradiction, that `\rho=\beta+i\gamma` is a nontrivial zero with
\[
\beta>1-\alpha.
\tag{15}
\]
Choose `\varepsilon>0` so small that
\[
\varepsilon<\beta-(1-\alpha).
\tag{16}
\]
Then (14) makes the integral defining `F` absolutely and locally uniformly convergent in the half-plane
\[
\Re s>-\alpha+\varepsilon.
\tag{17}
\]
Hence `F` is holomorphic there.

Set
\[
s_0:=\rho-1.
\tag{18}
\]
By (15)--(16), `s_0` lies in (17), and `s_0\ne0` because `\rho` is nontrivial. On the original half-plane `Re s>0`, equation (5) identifies `F` with
\[
\frac1s-\frac1{s^2\zeta(s+1)}.
\tag{19}
\]
Analytic continuation therefore identifies the two expressions throughout the connected continuation domain away from the meromorphic singularities. But `1/\zeta(s+1)` has a genuine pole at `s_0`, while `1/s` is regular there. Equation (19) would consequently have a nonremovable pole at a point where the integral continuation of `F` is holomorphic, a contradiction.

Thus no nontrivial zero has real part greater than `1-\alpha`. The functional equation gives the reflected exclusion `\Re\rho<\alpha`, proving (9). For the stronger fixed-power hypothesis (7), the same proof applies directly, or by observing that (7) implies (10).

The argument is intentionally one-way. It uses only the already-established selector identities and the standard meromorphic continuation of `\zeta`; it does not invoke a converse theorem converting a prescribed zero-free strip back into a power bound for Möbius sums.

## 3. The selector has a natural decay index bounded by the rightmost zeros

Define the line-local power-decay index
\[
\boxed{
\alpha_\Omega
:=
\sup\left\{
\alpha\in[0,1/2]:
\forall\varepsilon>0,
\ \|\Omega_M\|_2=O_\varepsilon(M^{-\alpha+\varepsilon})
\right\}.
}
\tag{20}
\]
Also write
\[
\Theta_\zeta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\tag{21}
\]
The theorem gives the unconditional structural constraint
\[
\boxed{
\alpha_\Omega\le1-\Theta_\zeta.
}
\tag{22}
\]
Indeed, if `\alpha<\alpha_\Omega`, then the preceding argument excludes zeros with real part greater than `1-\alpha`; letting `\alpha\uparrow\alpha_\Omega` yields (22).

The support identity from `NB-041`, `\Omega_M=1` on `(0,1/M]`, gives
\[
\|\Omega_M\|_2\ge M^{-1/2},
\tag{23}
\]
so `\alpha_\Omega\le1/2` for geometric reasons independently of zeros. Under RH, `NB-042` supplies the matching epsilon-loss upper bound at exponent `1/2`, and therefore
\[
\boxed{
\mathrm{RH}\Longrightarrow\alpha_\Omega=\frac12.
}
\tag{24}
\]
Conversely, `\alpha_\Omega=1/2` implies RH by `NB-042`. Thus the endpoint remains exactly critical, while (22) records what every weaker positive exponent would already buy.

This formulation also clarifies the unconditional state. The current `O(1/\log M)` estimate of `NB-041` supplies no positive power exponent. Proving, for example, `\|\Omega_M\|=O(M^{-0.01})` would not be a modest sharpening of the existing selector estimate: it would force all nontrivial zeros into
\[
0.01\le\Re\rho\le0.99.
\tag{25}
\]
More generally, each fixed positive exponent would create a fixed vertical zero-free strip independent of height.

## 4. Consequence for the weighted-skeleton oracle route

The accepted clue `CLUE-weighted-skeleton-target-data-without-full-section-oracle` asks whether the projected repair geometry or an equivalent one-sided target certificate can be recovered at Burnol-scale accuracy without an `N`-scale projection solve. `NB-041` offered one tempting source-only route: strengthen the ambient norm of `\Omega_M`, then use
\[
|\sigma_{M,N}-\Theta(M)|
\le d_N\|\Omega_M\|_2.
\tag{26}
\]
`NB-042` showed that driving the norm all the way to `M^{-1/2+\varepsilon}` is RH-equivalent. The present result shows that the route becomes arithmetically expensive **before** that endpoint. Any uniform power saving
\[
\|\Omega_M\|_2\ll M^{-\alpha},
\qquad \alpha>0,
\tag{27}
\]
already proves a fixed zero-free strip for the zeta function.

This is a route boundary, not an algorithmic impossibility theorem. The actual residual pairing in (26) may be much smaller than the product of the two norms; projected geometry could exploit angles invisible to ambient Cauchy--Schwarz; and a one-sided variational certificate need not estimate `\Omega_M` at all. Those remain precisely the live possibilities identified in `NB-038`--`NB-042`.

What should no longer be treated as a cheap intermediate estimate is **any polynomial ambient-norm decay for this same selector**. The natural next work therefore remains directional: control `<r_N,\Omega_M>` or the explicit source-aligned defect without first proving a global norm theorem whose arithmetic content already includes a fixed zero-free region.

## 5. Prior-art and falsification boundary

The Mellin-transform mechanism is classical analytic number theory. Titchmarsh records Littlewood's endpoint criterion linking square-root-scale Möbius cancellation to RH, already anchored in `SOURCES.md` for `NB-042`. More generally, zero-free regions obtained from Nyman--Beurling-type approximation are classical in spirit: Beurling's `L^p` closure theorem and modern weighted-space formulations make the approximation/zero-free-half-plane bridge explicit. In particular, Eva A. Gallardo-Gutiérrez and Daniel Seco, *Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces*, Complex Analysis and Operator Theory 19 (2025), article 38, DOI `10.1007/s11785-025-01661-2`, prove zero-free half-planes from weighted approximation hypotheses. No novelty is claimed for that general mechanism.

The line-local contribution is narrower: the explicit `NB-041` logarithmic tail dual has an exact target pairing with the mollified Möbius defect, so **its own polynomial Hilbert-norm decay** automatically becomes a zero-free-strip theorem through (5). This converts the qualitative warning after `NB-042` into the quantitative exponent barrier (8), (9), and (22).

The decisive falsification checks are short. Equation (3) must hold with the same `\Omega_M`; the real interpolation (13) must retain the exponent; and the Mellin identity (5) must be used only after establishing its original `Re s>0` domain before analytic continuation. A hypothetical zero with `\Re\rho>1-\alpha` then creates a pole at `s=\rho-1` inside the holomorphic continuation domain, with no possible cancellation from `1/s` because `\rho\ne1`. Failure of any one of these points invalidates the claimed strip.

No converse for subcritical `\alpha`, no new zero-free region, no improved estimate for `d_N`, and no RH claim are asserted. The result identifies the arithmetic price of a proposed norm improvement and directs the live research back toward genuinely target-conditioned information rather than a stronger ambient selector bound.