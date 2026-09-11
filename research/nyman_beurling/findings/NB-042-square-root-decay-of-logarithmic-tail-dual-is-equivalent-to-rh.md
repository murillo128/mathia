# NB-042 — square-root decay of the logarithmic tail dual is equivalent to RH

**Status:** `LITERATURE+EXACT-DERIVED + RH-EQUIVALENCE + SHARP-CRITICAL-NORM-SCALE + NEGATIVE/ORACLE-BOUNDARY`. `NB-041` constructs the source-defined logarithmic tail dual `\Omega_M` and proves the unconditional bounds
\[
M^{-1/2}\le \|\Omega_M\|_2\ll \frac1{\log M}.
\]
The gap between these two scales is not merely an explicit-estimate problem. The square-root endpoint is exactly RH-critical:
\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\forall\varepsilon>0,
\qquad
\|\Omega_M\|_2
=O_\varepsilon\!\left(M^{-1/2+\varepsilon}\right).
}
\tag{1}
\]
Thus the unavoidable support contribution `M^{-1/2}` isolated in `NB-041` is the correct critical exponent. Under RH the explicit dual comes within `M^\varepsilon` of that geometric floor; conversely, any unconditional proof of the same near-square-root norm decay would already prove RH.

This does **not** resolve the accepted weighted-skeleton target-data clue. It instead closes one natural subroute: improving the `NB-041` ambient-dual norm all the way to its support floor is not a cheaper source estimate hiding behind stronger PNT constants. It crosses an RH-equivalent gate. Moreover, a norm-only Cauchy--Schwarz argument at this critical scale still does not give `o(1/log N)` uniformly for every cutoff satisfying only `M/log N -> infinity`; for example the geometric floor itself is `1/log N` at `M=(log N)^2`. Any full solution of the clue in that regime must therefore exploit directional correlation, projected geometry, a different certificate, or additional cutoff growth.

Use the notation of `NB-041`:
\[
m(x):=\sum_{n\le x}\frac{\mu(n)}n,
\qquad
\check m(x):=\sum_{n\le x}\frac{\mu(n)}n\log\frac xn,
\qquad
\Theta(x):=1-\check m(x),
\tag{2}
\]
and
\[
\Omega_M
=e-\sum_{L=1}^{M-1}\log\frac{L+1}{L}\,\Psi_L.
\tag{3}
\]
On the harmonic shell
\[
I_t=\left(\frac1{t+1},\frac1t\right]
\tag{4}
\]
`NB-041` proves the exact formula
\[
\Omega_M|_{I_t}
=
\begin{cases}
(t+1)\Theta(M/t)-t\Theta(M/(t+1)),&1\le t<M,\\
1,&t\ge M,
\end{cases}
\tag{5}
\]
and the differential identity
\[
\Theta(x)-\Theta(y)
=-\int_y^x m(u)\,\frac{du}{u}.
\tag{6}
\]
It also proves the exact target pairing
\[
\boxed{\langle e,\Omega_M\rangle=\Theta(M).}
\tag{7}
\]

## 1. RH forces near-square-root decay of the whole dual norm

Let
\[
\mathcal M(x):=\sum_{n\le x}\mu(n)
\tag{8}
\]
be the Mertens function. Littlewood's classical criterion, in the standard Titchmarsh formulation, gives
\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
\forall\eta>0,
\qquad
\mathcal M(x)=O_\eta(x^{1/2+\eta}).
\tag{9}
\]
Only the forward implication is needed in this section.

Assume RH and fix `eta in (0,1/2)`. Partial summation, together with the classical limit `m(x)->0`, yields
\[
m(x)=O_\eta(x^{-1/2+\eta}).
\tag{10}
\]
Indeed one may write
\[
m(x)
=\frac{\mathcal M(x)}x
-\int_x^\infty\frac{\mathcal M(u)}{u^2}\,du,
\tag{11}
\]
where the tail converges under (9). Since `Theta(x)->0` and (6) gives `Theta'(x)=-m(x)/x` away from jumps of the underlying finite sum,
\[
\Theta(x)
=\int_x^\infty m(u)\,\frac{du}{u}
=O_\eta(x^{-1/2+\eta}).
\tag{12}
\]
After enlarging the implied constants, (10)--(12) may be used uniformly for all real `x>=1`.

Put
\[
\alpha:=\frac12-\eta>0.
\tag{13}
\]
Rewrite (5) as
\[
\Omega_M|_{I_t}
=
\Theta(M/t)
+t\left[\Theta(M/t)-\Theta(M/(t+1))\right].
\tag{14}
\]
By (6), (10), and `t log((t+1)/t)<=1`, uniformly for `1<=t<M`,
\[
\begin{aligned}
|\Omega_M|_{I_t}|
&\le |\Theta(M/t)|
+t\int_{M/(t+1)}^{M/t}|m(u)|\,\frac{du}{u}\\
&\ll_\eta \left(\frac Mt\right)^{-\alpha}.
\end{aligned}
\tag{15}
\]
The shell lengths are `|I_t|=1/(t(t+1))`, while the region `t>=M` is exactly `(0,1/M]` and contributes `1/M`. Therefore
\[
\begin{aligned}
\|\Omega_M\|_2^2
&=
\sum_{t=1}^{M-1}
\frac{|\Omega_M|_{I_t}|^2}{t(t+1)}
+\frac1M\\
&\ll_\eta
M^{-2\alpha}
\sum_{t<M}t^{2\alpha-2}
+\frac1M.
\end{aligned}
\tag{16}
\]
Because `alpha<1/2`, the series in (16) is uniformly bounded. Since `2 alpha<1`, the final `1/M` term is no larger than the displayed main scale. Hence
\[
\boxed{
\mathrm{RH}
\Longrightarrow
\|\Omega_M\|_2
=O_\eta(M^{-1/2+\eta})
}
\tag{17}
\]
for every `eta>0`.

The proof uses the full shell resummation of `NB-041`; applying triangle inequality directly to (3) would again lose all of the Möbius cancellation.

## 2. Near-square-root dual decay forces RH

Now assume that for every `epsilon>0`,
\[
\|\Omega_M\|_2
=O_\varepsilon(M^{-1/2+\varepsilon})
\qquad(M\in\mathbb Z_{\ge2}).
\tag{18}
\]
The target pairing (7) and `\|e\|_2=1` immediately give
\[
|\Theta(M)|
\le \|\Omega_M\|_2
=O_\varepsilon(M^{-1/2+\varepsilon}).
\tag{19}
\]
This integer estimate extends to real `x`. If `M<=x<M+1`, equation (6) and the global elementary bound `|m(u)|<=1` used already in `NB-035` give
\[
|\Theta(x)-\Theta(M)|
\le\int_M^{M+1}\frac{du}{u}
\ll \frac1M.
\tag{20}
\]
Consequently
\[
\boxed{
\Theta(x)=O_\varepsilon(x^{-1/2+\varepsilon})
}
\tag{21}
\]
for every `epsilon>0`.

The Mellin transform of this defect exposes the zero-free content directly. For `Re s>0`, absolute convergence permits interchange of sum and integral, and
\[
\begin{aligned}
\int_1^\infty \check m(x)x^{-s-1}\,dx
&=
\sum_{n\ge1}\frac{\mu(n)}n
\int_n^\infty \log\frac xn\,x^{-s-1}\,dx\\
&=
\frac1{s^2}
\sum_{n\ge1}\frac{\mu(n)}{n^{s+1}}\\
&=
\frac1{s^2\zeta(s+1)}.
\end{aligned}
\tag{22}
\]
Therefore
\[
\boxed{
F(s):=\int_1^\infty\Theta(x)x^{-s-1}\,dx
=
\frac1s-\frac1{s^2\zeta(s+1)}
}
\qquad(\Re s>0).
\tag{23}
\]
By (21), the integral defining `F` is holomorphic throughout
\[
\Re s>-\frac12.
\tag{24}
\]
Indeed, on any compact subset of this half-plane choose `epsilon>0` smaller than the compact distance to `Re s=-1/2`.

Suppose `rho` were a nontrivial zero of `zeta` with `Re rho>1/2`. Then
\[
s_0:=\rho-1
\tag{25}
\]
lies in the holomorphy half-plane (24), and `s_0!=0`. The right side of (23), continued meromorphically from `Re s>0`, has a pole at `s_0` because `1/zeta(s+1)` has a pole there, while `1/s` is regular. This contradicts the holomorphy of the integral continuation. Thus there are no nontrivial zeros with real part greater than `1/2`; the functional equation supplies the symmetric exclusion on the left, proving RH.

Combining this implication with (17) proves (1).

## 3. The support floor is the RH-critical exponent

`NB-041` already records the unconditional identity `Omega_M=1` on `(0,1/M]`. Hence
\[
\boxed{
\|\Omega_M\|_2\ge M^{-1/2}
}
\tag{26}
\]
without any arithmetic input. Together with (1), this yields the sharp exponent statement
\[
\mathrm{RH}
\Longrightarrow
M^{-1/2}
\le\|\Omega_M\|_2
\ll_\varepsilon M^{-1/2+\varepsilon}.
\tag{27}
\]
So the geometric support tail already sits exactly at the critical exponent selected by the zero symmetry. The unconditional `O(1/log M)` estimate of `NB-041` is genuinely far from this critical regime, but closing that gap up to arbitrary powers `M^epsilon` is equivalent to RH rather than a routine quantitative sharpening.

This also identifies a precise limitation of the direct scalar route in the accepted weighted-skeleton clue. `NB-041` gives, for the optimal residual,
\[
|\sigma_{M,N}-\Theta(M)|
\le d_N\|\Omega_M\|_2.
\tag{28}
\]
If this is used only through `d_N<=1`, then even the smallest possible norm scale allowed by (26) is `M^{-1/2}`. Thus a norm-only Cauchy--Schwarz certificate cannot be `o(1/log N)` at cutoffs as small as `M=(log N)^2`, let alone uniformly over every sequence satisfying merely `M/log N->infinity`. Under RH, (17) does give such scalar accuracy for substantially larger polynomial-log cutoffs, e.g. `M=(log N)^A` with fixed `A>2` after choosing `epsilon` sufficiently small, but that is a different cutoff regime.

The conclusion is deliberately route-specific. Equation (26) does **not** imply that the actual pairing `<r_N,Omega_M>` must saturate Cauchy--Schwarz. A source-specific angular cancellation, a projected-tail identity, or a one-sided variational certificate could still outperform the norm bound. What is ruled out is treating a near-square-root improvement of the ambient selector norm as a cheap unconditional input.

## 4. Adversarial checks and boundary conditions

The converse does not assume density of the Nyman span, any estimate for `d_N`, or any upper-section limit `N->infinity`. It concerns only the explicit source-defined sequence `Omega_M`. The finite-section target problem enters only through the interpretation (28), not through the RH equivalence itself.

The Mellin identity (23) is initially proved only in `Re s>0`, where the sum/integral interchange is absolute. The decay hypothesis then continues the **integral** holomorphically to `Re s>-1/2`; identity of analytic continuations transfers (23) there away from the meromorphic singularities. At a hypothetical zero `rho` with `Re rho>1/2`, no cancellation with `1/s` is possible because `rho!=1`, hence `s_0!=0`. Trivial zeros lie outside the relevant half-plane after the shift.

The quantifier `for every epsilon>0` is essential. No claim is made that RH implies the false Mertens conjecture scale `O(M^{-1/2})` for this norm, nor that an epsilon-free bound should hold. Likewise, the fixed-exponent statement `||Omega_M||=O(M^{-alpha})` is not promoted here to a converse zero-free theorem without the additional growth hypotheses needed for the corresponding classical Dirichlet-series boundary theory.

At the opposite endpoint, the unconditional estimate `O(1/log M)` from `NB-041` remains valuable: it is strong enough to show that the zero-loss logarithmic coordinate is asymptotically source-locked in absolute scale. `NB-042` only identifies how much deeper one must go before that particular selector norm begins to encode the full RH zero-free half-plane.

## 5. Prior art and research consequence

The arithmetic ingredients are classical. Littlewood's Mertens-function criterion, in the standard form
\[
\mathrm{RH}\iff \mathcal M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0,
\]
is recorded in Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., §14.25. The logarithmically mollified sum `check m(x)` and quantitative estimates for it are prior art in Ramaré--Zuniga-Alterman with Balazard, already anchored for `NB-041`. The Mellin-transform mechanism converting decay of a Möbius smoothing into a zero-free half-plane is standard analytic-number-theory structure; no novelty is claimed for that mechanism in isolation.

A targeted literature search across the mollified Möbius sum, Mertens/RH criteria, and Nyman--Beurling norm criteria did not locate the specific equivalence (1) for the `NB-041` Hilbert-space selector. The line-local contribution is therefore stated conservatively as the exact bridge from the already-defined `Omega_M` shell norm to the classical RH boundary, together with its consequence for the weighted-skeleton oracle route. The claim does not depend on the absence of prior wording: if an equivalent norm criterion is found later, the mathematics here remains a valid classicalization of the route boundary.

For the live research direction, the important consequence is negative but precise. The scalar oracle isolated by `NB-040` is source-controlled by `NB-041`, yet the most obvious attempt to strengthen that control by driving `||Omega_M||` to its natural support scale encounters an RH-equivalent barrier. The accepted clue should therefore continue to target the **projected repair geometry**, the explicit `NB-038` source-aligned defect, directional residual cancellation, or a genuinely different one-sided target certificate, rather than expecting a substantially sharper unconditional norm estimate for the same ambient dual to supply the missing finite-distance information.