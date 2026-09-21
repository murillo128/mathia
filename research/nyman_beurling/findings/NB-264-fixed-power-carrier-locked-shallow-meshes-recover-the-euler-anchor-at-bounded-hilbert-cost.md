# NB-264 — Fixed-power carrier-locked shallow meshes recover the Euler anchor at bounded Hilbert cost

> **Representation:** _Nyman–Beurling / resolved signed-carrier destination interface._ The line-specific inputs are the Euler-normalized `H`-separated carrier dictionary and shell-Hilbert/`ell^2` identification used in `NB-257`--`NB-263`, with `J=mK`, legal complex Ford coordinate `w=R[(gamma-t_0)+i(1-beta)]`, and shallow physical depth `u=X(1-beta)`. The generic engine is an exact Fourier-series reconstruction of the Euler anchor from the carrier-locked Ford mesh. The result supplies the rank-coupled boundary left open by `NB-263`: although every positive-depth strip prescribed before `K` is chosen can be flattened at vanishing resolved Hilbert cost, a strip whose horizontal carrier-locked radius grows like any fixed power `K^delta` cannot be uniformly suppressed by an Euler-normalized carrier with bounded resolved Hilbert cost. At the live depth `u=log m+O(1)`, the surviving mesh response has aggregate `ell^1` mass `Omega(m)` and supports an order-one matched compatibility control inside an `o(J)` central Ford window. This is a source/destination-interface obstruction, not a theorem that the actual zeta zeros occupy the surviving mesh.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + SIGNED-COMPLEX-CARRIER + EULER-NORMALIZED + H-SEPARATED-DICTIONARY + FOURIER-SERIES-ANCHOR-RECONSTRUCTION + CARRIER-LOCKED-MESH + FIXED-POWER-RANK-COUPLING + BOUNDED-HILBERT-COERCIVITY + SHALLOW-BOUNDARY-LAYER + MATCHED-COMPATIBILITY-CONTROL + NB-263-BOUNDARY-SHARPENING + METHOD-BOUNDARY + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-263` proves a strong noncoercivity statement, but its order of quantifiers is essential. Given a positive-depth strip

\[
|x|\le mB,
\qquad
 a\le u\le U,
\]

one first constructs a finite-norm Fourier--Laplace approximate annihilator and only afterward chooses `K` large enough to amortize that norm. In the diagonal version one explicitly has `B/K -> 0`. The finding therefore leaves open what happens when the requested horizontal coverage is tied to the resolved rank itself.

That boundary can be located sharply enough for the current Ford mechanism. Retain

\[
J=mK,
\qquad
C_J(w)=\sum_{j=0}^{K-1}c_j e^{ijw/J},
\qquad
\sum_{j=0}^{K-1}c_j=1,
\tag{1}
\]

and assume the resolved coefficient cost is bounded,

\[
\|c\|_2\le M
\tag{2}
\]

with `M` independent of `K`. Fix the same carrier-locking integer `q>=1` used in the earlier matched-packet audits and put

\[
\Delta_m:=\frac{2\pi q}{Ym}.
\tag{3}
\]

At physical Ford depth `u>=0`, write

\[
\alpha:=\frac{u}{Ym}.
\tag{4}
\]

Then the values on the carrier-locked mesh are

\[
D_n
:=C_J\!\left(\frac{2\pi qn}{Y}+i\frac uY\right)
=\sum_{j=0}^{K-1}c_j
   e^{-\alpha j/K}e^{in\Delta_m j/K}.
\tag{5}
\]

The central exact identity is that, as long as `alpha` stays in a fixed compact interval, the Euler anchor `sum c_j=1` can be reconstructed from these mesh values with an absolutely summable family of coefficients whose individual size is `O(1/m)` and whose frequency tails are Schwartz. Consequently, for every fixed `delta>0`,

\[
\boxed{
\sum_{|n\Delta_m|\le K^\delta}|D_n|\gg m
}
\tag{6}
\]

uniformly for all sufficiently large `K`, provided (2) holds. In particular

\[
\boxed{
\sup_{|n\Delta_m|\le K^\delta}|D_n|\not\longrightarrow0.
}
\tag{7}
\]

The statement remains valid if `K^delta` is replaced by any radius `B_K` for which the reconstruction tail satisfies `sqrt(K) tau(B_K)->0`; the fixed-power corollary is the robust formulation that needs no quantitative smoothness bookkeeping beyond `C_c^infty`.

Thus the successful diagonals of `NB-263` cannot have polynomial horizontal coverage in the eventual rank while keeping bounded resolved Hilbert cost. If

\[
\sup_{|n\Delta_m|\le B_K}|D_n|\to0
\]

along such a bounded-cost family, then necessarily

\[
\boxed{
B_K=K^{o(1)}.
}
\tag{8}
\]

The surviving unresolved regime is therefore subpolynomial in the resolved rank, not an arbitrary `o(K)` horizontal strip.

## 1. Exact reconstruction on the carrier-locked mesh

Choose once and for all a real cutoff

\[
\chi\in C_c^\infty(\mathbb R),
\qquad
\chi(t)=1\quad(0\le t\le1),
\]

with support contained, say, in `(-1,2)`. For `0<=alpha<=A` define

\[
g_\alpha(t):=\chi(t)e^{\alpha t}.
\tag{9}
\]

Let

\[
L_m:=\frac{Ym}{q},
\qquad
\Delta_m=\frac{2\pi}{L_m}.
\tag{10}
\]

For large `m`, the support of `g_alpha` fits strictly inside one period of length `L_m`. Periodize `g_alpha` with that period. Its absolutely convergent Fourier series has coefficients

\[
d_{n,\alpha,m}
:=\frac1{L_m}\widehat g_\alpha(n\Delta_m),
\qquad
\widehat g_\alpha(\xi)
:=\int_{\mathbb R}g_\alpha(t)e^{-i\xi t}\,dt,
\tag{11}
\]

and therefore, for every `t in [0,1]`,

\[
e^{\alpha t}
=\sum_{n\in\mathbb Z}
 d_{n,\alpha,m}e^{in\Delta_m t}.
\tag{12}
\]

Put `t_j=j/K`. Multiplying (12) by `c_j e^{-alpha t_j}` and summing over `j` gives the exact anchor reconstruction

\[
\boxed{
1
=\sum_{n\in\mathbb Z}
 d_{n,\alpha,m}
 C_J\!\left(\frac{2\pi qn}{Y}+i\frac uY\right).
}
\tag{13}
\]

No asymptotic approximation enters (13). The sample locations are exactly the Ford coordinates of the carrier-locked ordinates

\[
\gamma_n=t_0+\frac{2\pi qn}{X},
\qquad
R(\gamma_n-t_0)=\frac{2\pi qn}{Y}.
\tag{14}
\]

Thus the reconstruction is not merely a continuum strip statement later sampled on a convenient grid; it is already written on the same discrete mesh that generates the matched Ford controls.

## 2. The reconstruction coefficients have bounded mass and `1/m` atom size

Because the family `g_alpha`, `0<=alpha<=A`, is bounded in every Schwartz seminorm after Fourier transform, for every integer `p>=2` there is `C_{A,p}` such that

\[
|\widehat g_\alpha(\xi)|
\le C_{A,p}(1+|\xi|)^{-p}
\tag{15}
\]

uniformly in `alpha`. Since `L_m^{-1}=Delta_m/(2pi)=Theta(m^{-1})`, this gives

\[
\boxed{
|d_{n,\alpha,m}|
\le
\frac{C_A}{m}
}
\tag{16}
\]

and

\[
\boxed{
\sum_{n\in\mathbb Z}|d_{n,\alpha,m}|
\le C_A.
}
\tag{17}
\]

More importantly, for every `B>=1`,

\[
\boxed{
\sum_{|n\Delta_m|>B}|d_{n,\alpha,m}|
\le C_{A,p}B^{1-p}.
}
\tag{18}
\]

The constants are uniform in `m` and `alpha in [0,A]`. Equation (18) is just the Riemann-sum estimate for a Schwartz tail; the factor `1/L_m=Delta_m/(2pi)` exactly cancels the increasing number of mesh frequencies per unit interval.

On the other hand, (2) gives the crude but sufficient uniform response bound

\[
|D_n|
\le\sum_j|c_j|
\le\sqrt K\,\|c\|_2
\le M\sqrt K,
\tag{19}
\]

because the depth damping in (5) is at most one.

Split (13) at `|n Delta_m|=B`. Equations (18)--(19) imply

\[
\left|
\sum_{|n\Delta_m|>B}d_{n,\alpha,m}D_n
\right|
\le
C_{A,p}M\sqrt K\,B^{1-p}.
\tag{20}
\]

Take

\[
B=K^\delta
\tag{21}
\]

with fixed `delta>0`, and choose the fixed integer `p` so large that

\[
\delta(p-1)>\frac12.
\]

Then the right side of (20) is `o(1)`. Hence the core of (13) carries asymptotically all of the Euler anchor:

\[
\left|
\sum_{|n\Delta_m|\le K^\delta}
 d_{n,\alpha,m}D_n
\right|
\ge1-o(1).
\tag{22}
\]

Using the atom bound (16),

\[
1-o(1)
\le
\frac{C_A}{m}
\sum_{|n\Delta_m|\le K^\delta}|D_n|,
\]

which proves (6).

A useful way to read the result is that the Euler anchor is a **distributed observable** of the carrier-locked mesh. The reconstruction weights have total mass `O(1)` but individual mass only `O(1/m)`, so bounded Hilbert cost cannot export the entire anchor beyond every polynomially growing mesh radius.

## 3. Relation to the `NB-263` noncoercivity construction

The result does not contradict `NB-263`. There the strip radius `B_n` is chosen first, an approximate annihilator with some finite but uncontrolled norm `M_n` is constructed, and `K_n` is then taken so large that both `M_n/sqrt(K_n)` and the discretization error are tiny. The same diagonal explicitly enforces

\[
\frac{B_n}{K_n}\to0.
\]

Equation (20) shows what must happen more sharply if the resulting discrete coefficient norms remain bounded. A suppressing sequence cannot satisfy

\[
B_n\ge K_n^\delta
\]

for any fixed `delta>0` along an infinite subsequence. Otherwise the truncated carrier-locked reconstruction would force (6). Thus the freedom exploited in `NB-263` necessarily pushes the covered horizontal scale into

\[
B_n=K_n^{o(1)}.
\]

This is a quantifier boundary, not a reversal of the noncoercivity theorem. Compact or subpolynomial positive-depth boxes may still be flattened by increasingly ill-conditioned approximate annihilators. What fails is the extrapolation from that fact to rank-coupled polynomial coverage.

There is also a useful distinction from `NB-258`. That finding obtains a source-side real-axis obstruction from finite-order derivative control. Here the zeros are evaluated at their legal positive complex depth, and the proof does not approximate the carrier by a low-degree polynomial. The anchor is recovered instead from a complete family of carrier-locked Fourier samples. The logarithmic complex displacement that defeated the real-axis bridge in `NB-259` therefore does not defeat (13).

## 4. The live shallow depth is inside the uniform regime

Return to the near-full scaling of `NB-261`--`NB-263`,

\[
1\ll m\ll \frac{\log J}{Y},
\qquad
K\sim\frac Jm.
\tag{23}
\]

The live replacement depth is

\[
u=\log m+d_*,
\tag{24}
\]

with fixed `d_*`. Then

\[
\alpha
=\frac{u}{Ym}
=\frac{\log m+O(1)}{Ym}
\longrightarrow0.
\tag{25}
\]

Hence the uniform reconstruction above applies with any fixed `A>0` for all sufficiently large `J`.

Choose now

\[
0<\delta<1.
\tag{26}
\]

The reconstructed mesh lies in

\[
|x|
=\left|\frac{2\pi qn}{Y}\right|
\le mK^\delta.
\tag{27}
\]

Since `J=mK`,

\[
\frac{|x|}{J}\le K^{\delta-1}\to0.
\tag{28}
\]

Therefore the original smooth shell envelope satisfies

\[
F\!\left(\frac{x+i u/Y}{J}\right)
=F(0)+o(1)
\tag{29}
\]

uniformly on the entire reconstructed mesh. The new coercivity is therefore located inside the same central shell patch used by the earlier matched Ford controls, not in a remote side-lobe where the original envelope could suppress it.

The number of carrier-locked mesh sites in (27) is

\[
O(mK^\delta)=o(mK)=o(J).
\tag{30}
\]

Thus the rank-coupled window remains a vanishing fraction of the complete hard Ford window while already forcing aggregate carrier response `Omega(m)`.

## 5. A matched compatibility control recovers order-one residue mass

Equation (6) can be converted into the same type of adversarial control used throughout the Ford branch. Partition the nonzero complex plane into a fixed finite number of angular cones. From (6), one cone contains a subset `S` of indices in the reconstructed mesh for which

\[
\sum_{n\in S}|D_n|\gg m
\tag{31}
\]

and all `D_n`, `n in S`, have arguments inside that common cone.

Place one simple matched control zero at each

\[
\gamma_n=t_0+\frac{2\pi qn}{X},
\qquad n\in S,
\tag{32}
\]

with common depth (24),

\[
\beta_n=1-\frac{u}{X}.
\tag{33}
\]

The main shell carrier is exactly locked,

\[
e^{iX(\gamma_n-t_0)}=1,
\tag{34}
\]

and (29) keeps the fixed smooth envelope in one positive cone because `F(0)=int phi>0` in the inherited nonnegative shell. The Ford damping is

\[
e^{-X(1-\beta_n)}
=e^{-u}
=\frac{e^{-d_*}}m.
\tag{35}
\]

Consequently the complete contribution from `S` has magnitude bounded below by a positive constant:

\[
\boxed{
|\mathcal R_S|
\gg
\frac1m\sum_{n\in S}|D_n|
\gg1.
}
\tag{36}
\]

The population of `S` is at most `O(mK^delta)=o(J)`, with the same carrier spacing `Theta(1/R)` as the matched packets already audited in `NB-230`, `NB-231`, and `NB-261`. Its depth is exactly the `NB-261` shallow replacement depth, and its total population is below the earlier `Theta(J)` critical population budget. The inherited zero-free, local-count, and aggregate-density controls therefore do not exclude this formal configuration. As before, (36) is a **matched compatibility control**: it shows that the current source-side/counting information cannot certify decay for every admissible zero configuration. It does not assert that the actual zeta zeros choose the high-response mesh sites.

The advantage over the one-side-lobe control of `NB-262` is structural. `NB-263` correctly showed that any preassigned packet-scale box can be flattened. Equation (36) says that, once the box is required to grow polynomially with the rank, the Euler anchor forces enough response back onto the **carrier-locked mesh itself** to rebuild an order-one compatible obstruction.

## 6. Boundaries and adversarial audit

The bounded-Hilbert hypothesis is load-bearing. More generally, if `M_K=||c||_2` is allowed to grow, the proof only requires

\[
M_K\sqrt K
\sum_{|n\Delta_m|>B_K}|d_{n,\alpha,m}|	o0.
\tag{37}
\]

A sufficiently violent coefficient blow-up can therefore export the anchor into the Fourier-series tail. This is consistent with the conditioning currency isolated in `NB-255`, `NB-256`, and `NB-263`; `NB-264` does not replace a total-variation analysis.

The fixed-power conclusion is deliberately not claimed at the logarithmic or other subpolynomial radius. The Schwartz tail proves every `B_K>=K^delta`, fixed `delta>0`, but does not give a universal threshold for `B_K=(log K)^A` without adding quantitative regularity choices for the extension `chi`. The remaining continuous/mesh coverage problem is therefore genuinely subpolynomial.

The depth restriction is also explicit. Uniformity above requires

\[
0\le\frac{u}{Ym}\le A.
\]

This includes `u=log m+O(1)` and, more generally, every `u=O(m)`. No claim is made for depths with `u/m->infinity`, where the Fourier reconstruction kernel itself changes scale.

Finally, the argument is still upstream of the actual Hardy/Nyman distance. It proves a coercive property of the resolved Euler-normalized carrier and exhibits a zero configuration compatible with the inherited counting ledger. Actual zeta zeros may avoid the high-response sites, and the final Hardy projection may introduce structure not encoded by this scalar carrier model. Those are genuine remaining arithmetic/destination questions rather than representation artifacts.

A decisive falsification test is exact: for finite `K`, compute the Fourier coefficients (11) of any fixed smooth periodized extension and verify (13) numerically or symbolically. Any proposed bounded-`ell^2` carrier that is uniformly `o(1)` on all carrier-locked sites with `|n Delta_m|<=K^delta` must force the omitted Fourier tail in (13) to carry asymptotically unit mass. Equations (15), (19), and the choice of `p` make that impossible.

## 7. Prior-art and novelty audit

The harmonic-analysis engine is classical. Smooth periodic extension, absolute Fourier-series reconstruction, and rapid decay of Fourier coefficients are standard; no novelty is claimed for them. The nearest broader prior-art families found in a fresh search are Turan--Nazarov inequalities for exponential polynomials and Logvinenko--Sereda-type observability/uncertainty principles. In particular, F. L. Nazarov's classical local estimates for exponential polynomials and the 2026 disk-growth treatment of measurable Turan--Nazarov inequalities by Omer Friedland concern propagation of smallness from sets of positive measure. They are conceptually adjacent but are not used in the proof above: (13) is an elementary exact reconstruction tailored to the carrier-locked Ford mesh.

The line-specific contribution is the scaling bridge that those generic results do not supply automatically: `J=mK`, mesh spacing `2pi q/(Ym)`, legal complex depth `u/Y`, bounded resolved shell-Hilbert cost, and the conclusion that every fixed-power rank-coupled mesh retains `Omega(m)` aggregate response and hence an order-one matched Ford compatibility control at `u=log m+O(1)`. No external theorem is load-bearing, so this finding introduces no new durable literature dependency in `SOURCES.md`.

## 8. Consequence for the live research line

`NB-263` removed the packet-scale side-lobe of the two-constraint optimizer as a universal obstruction: with arbitrary conditioning and enough rank, every strip fixed before `K` is chosen can be flattened. The new result shows that this freedom has a hard rank-coupled limit under bounded resolved Hilbert cost. A successful signed scalar family cannot flatten the carrier-locked shallow mesh throughout any horizontal radius `K^delta`, however small the fixed exponent `delta>0`.

The live scalar frontier is therefore narrower:

\[
\boxed{
\text{bounded-Hilbert suppression can only remain universal on }B_K=K^{o(1)}
\text{ carrier-frequency radii,}
}
\tag{38}
\]

unless one uses arithmetic information about the actual zero locations rather than compatibility with current count/density constraints. The next non-circular question is not another fixed or polynomial strip. It is whether the subpolynomial mesh regime—especially radii tied to the natural `log m` population/conditioning scales—still admits low-cost signed annihilation, or whether a quantitative Fourier/Hardy conditioning law becomes coercive there. A second, independent route is to ask whether actual zeta zeros sample the forced high-response mesh often enough to replace the matched compatibility control by a theorem about the true zero set.