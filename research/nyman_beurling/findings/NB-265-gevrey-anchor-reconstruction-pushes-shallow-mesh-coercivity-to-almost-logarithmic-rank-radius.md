# NB-265 — Gevrey anchor reconstruction pushes shallow mesh coercivity to almost-logarithmic rank radius

> **Representation:** _Nyman–Beurling / resolved signed-carrier destination interface._ The line-specific inputs are exactly those of `NB-264`: the Euler-normalized `H`-separated carrier dictionary, `J=mK`, bounded resolved shell-Hilbert/`ell^2` cost, legal Ford coordinate `w=R[(gamma-t_0)+i(1-beta)]`, and carrier-locked mesh at shallow physical depth `u=X(1-beta)`. The generic engine is an explicit compactly supported Gevrey extension of the anchor multiplier, whose Fourier coefficients have stretched-exponential rather than merely Schwartz decay. This quantitatively sharpens the rank-coupled boundary left by `NB-264`: for every fixed `epsilon>0`, bounded-Hilbert carriers retain `Omega(m)` aggregate response, and a nonvanishing point response, already inside carrier-frequency radius `O_epsilon((log K)^(1+epsilon))`. At the live depth `u=log m+O(1)` this again yields an order-one matched compatibility control inside Ford radius `O(m (log K)^(1+epsilon))=o(J)`. The result is not a theorem about the actual zeta-zero locations and does not reach the exactly logarithmic radius.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + SIGNED-COMPLEX-CARRIER + EULER-NORMALIZED + H-SEPARATED-DICTIONARY + GEVREY-FOURIER-RECONSTRUCTION + STRETCHED-EXPONENTIAL-TAIL + POLYLOG-RANK-COUPLING + BOUNDED-HILBERT-COERCIVITY + SHALLOW-BOUNDARY-LAYER + MATCHED-COMPATIBILITY-CONTROL + NB-264-SHARPENING + METHOD-BOUNDARY + SOURCE-DESTINATION-INTERFACE + FRESH-PRIOR-ART-AUDIT`.

`NB-264` reconstructs the Euler anchor from the carrier-locked mesh using a fixed `C_c^infty` extension. Because that argument uses only unspecified Schwartz decay, it safely excludes suppression on every fixed-power radius `K^delta`, but deliberately leaves the whole subpolynomial regime open. The same exact reconstruction becomes substantially stronger once the extension is chosen with quantitative Gevrey regularity.

Retain

\[
J=mK,
\qquad
C_J(w)=\sum_{j=0}^{K-1}c_j e^{ijw/J},
\qquad
\sum_{j=0}^{K-1}c_j=1,
\tag{1}
\]

and assume

\[
\|c\|_2\le M
\tag{2}
\]

with `M` independent of `K`. For the fixed carrier-locking integer `q>=1`, put

\[
\Delta_m:=\frac{2\pi q}{Ym},
\qquad
L_m:=\frac{2\pi}{\Delta_m}=\frac{Ym}{q}.
\tag{3}
\]

At physical depth `u>=0`, set

\[
\alpha:=\frac{u}{Ym},
\tag{4}
\]

and denote the mesh values by

\[
D_n
:=C_J\!\left(\frac{2\pi qn}{Y}+i\frac uY\right)
=\sum_{j=0}^{K-1}c_j e^{-\alpha j/K}e^{in\Delta_m j/K}.
\tag{5}
\]

The new quantitative statement is the following.

For every fixed `epsilon>0`, every fixed `A,M<infinity`, and all sufficiently large `m,K`, there are constants `C,c>0` depending only on `epsilon,A,M,q,Y` such that whenever

\[
0\le\alpha\le A,
\qquad
B_K:=C(\log(2+K))^{1+\epsilon},
\tag{6}
\]

one has

\[
\boxed{
\sup_{|n\Delta_m|\le B_K}|D_n|\ge c
}
\tag{7}
\]

and, more strongly,

\[
\boxed{
\sum_{|n\Delta_m|\le B_K}|D_n|\gg m.
}
\tag{8}
\]

Thus the `K^delta` radius in `NB-264` is not the true limit of its reconstruction mechanism. Every fixed superlogarithmic power `(log K)^(1+epsilon)` already captures a coercive amount of the Euler anchor.

## 1. A compact Gevrey plateau with explicit Fourier decay

Fix

\[
s:=1+\epsilon>1.
\tag{9}
\]

We first record the elementary Gevrey cutoff needed below. There exists a real function

\[
\chi_s\in C_c^\infty((-1,2)),
\qquad
\chi_s(t)=1\quad(0\le t\le1),
\tag{10}
\]

and constants `A_s,C_s` such that for every integer `r>=0`,

\[
\boxed{
\|\chi_s^{(r)}\|_1
\le A_s C_s^r(r!)^s.
}
\tag{11}
\]

For completeness, one may construct `chi_s` from the standard flat function

\[
\vartheta(t)
=
\begin{cases}
0,&t\le0,\\
\exp(-t^{-1/(s-1)}),&t>0,
\end{cases}
\tag{12}
\]

by forming a smooth Gevrey step from `vartheta(t)` and `vartheta(1-t)` and multiplying two translated steps. The derivative estimate (11) follows directly from Leibniz/Faa di Bruno together with the elementary maximization of powers of `t^{-1}` against `exp(-t^{-1/(s-1)})`; the resulting factorial growth is precisely `(r!)^s`. No external theorem is needed for (11).

For `0<=alpha<=A`, define

\[
g_\alpha(t):=\chi_s(t)e^{\alpha t}.
\tag{13}
\]

Because `g_alpha` has fixed compact support and multiplication by `e^{alpha t}` preserves the same Gevrey order uniformly for `alpha` in a fixed compact interval, there are constants `A_{s,A},C_{s,A}` with

\[
\|g_\alpha^{(r)}\|_1
\le A_{s,A}C_{s,A}^r(r!)^s.
\tag{14}
\]

Repeated integration by parts gives, for nonzero real `xi`,

\[
|\widehat g_\alpha(\xi)|
\le
|\xi|^{-r}
A_{s,A}C_{s,A}^r(r!)^s.
\tag{15}
\]

Choose `r` comparable to `|xi|^(1/s)` and use the elementary Stirling upper bound `r!<=C r^(r+1/2)e^{-r}`. After adjusting constants for bounded `xi`, this yields the uniform stretched-exponential estimate

\[
\boxed{
|\widehat g_\alpha(\xi)|
\le
A'_{s,A}\exp(-c_{s,A}|\xi|^{1/s}).
}
\tag{16}
\]

This is the only extra analytic input beyond `NB-264`, and it is proved here from the explicit Gevrey plateau.

## 2. Exact anchor reconstruction now has a stretched-exponential tail

For large `m`, the fixed support of `g_alpha` fits strictly inside one period of length `L_m`. Periodize it with that period and define Fourier coefficients

\[
d_{n,\alpha,m}
:=\frac1{L_m}\widehat g_\alpha(n\Delta_m).
\tag{17}
\]

Exactly as in `NB-264`, Fourier reconstruction on `t in [0,1]` gives

\[
e^{\alpha t}
=
\sum_{n\in\mathbb Z}
 d_{n,\alpha,m}e^{in\Delta_m t}.
\tag{18}
\]

Putting `t_j=j/K`, multiplying by `c_j e^{-alpha t_j}`, and summing over `j` produces the exact identity

\[
\boxed{
1
=
\sum_{n\in\mathbb Z}
 d_{n,\alpha,m}D_n.
}
\tag{19}
\]

There is no approximation in (19). From (16) and `L_m=Theta(m)`, `Delta_m=Theta(1/m)`,

\[
|d_{n,\alpha,m}|
\le
\frac{C}{m}
\exp\!\left(-c|n\Delta_m|^{1/s}\right).
\tag{20}
\]

In particular,

\[
\sum_n|d_{n,\alpha,m}|\le C,
\qquad
\sup_n|d_{n,\alpha,m}|\le\frac C m.
\tag{21}
\]

The Riemann-sum comparison for the decreasing stretched exponential gives, after weakening `c` if necessary,

\[
\boxed{
\sum_{|n\Delta_m|>B}|d_{n,\alpha,m}|
\le
C\exp(-c B^{1/s})
}
\tag{22}
\]

for all sufficiently large `B`, uniformly in `m` and `alpha in [0,A]`. Any polynomial factor generated by integrating the tail is absorbed into the exponential after replacing `c` by a smaller constant.

On the carrier side, bounded resolved Hilbert cost still gives

\[
|D_n|
\le\sum_j|c_j|
\le\sqrt K\,\|c\|_2
\le M\sqrt K.
\tag{23}
\]

Consequently the contribution to (19) from `|n Delta_m|>B` is at most

\[
CM\sqrt K\exp(-cB^{1/s}).
\tag{24}
\]

Take

\[
B=B_K=C_0(\log(2+K))^s
\tag{25}
\]

with `C_0` sufficiently large. Then `B_K^(1/s)=C_0^(1/s) log(2+K)`, so (24) is `o(1)`. Hence

\[
\left|
\sum_{|n\Delta_m|\le B_K}
 d_{n,\alpha,m}D_n
\right|
\ge1-o(1).
\tag{26}
\]

Using the total coefficient mass in (21) gives immediately

\[
\sup_{|n\Delta_m|\le B_K}|D_n|
\ge c>0,
\tag{27}
\]

which proves (7). Using instead the atom bound `|d_n|<=C/m` yields

\[
1-o(1)
\le
\frac C m
\sum_{|n\Delta_m|\le B_K}|D_n|,
\tag{28}
\]

which proves (8).

The distinction between (27) and (28) matters. The first forbids uniform `o(1)` suppression throughout the entire polylogarithmic mesh. The second retains enough aggregate response to rebuild the order-one matched Ford obstruction after the depth damping is restored.

## 3. At the live shallow depth the forced mesh stays inside the central shell patch

Return to the live near-full regime of `NB-261`--`NB-264`,

\[
1\ll m\ll\frac{\log J}{Y},
\qquad
K\sim\frac Jm,
\tag{29}
\]

and take

\[
u=\log m+d_*
\tag{30}
\]

with fixed `d_*`. Then

\[
\alpha=\frac{\log m+O(1)}{Ym}\to0,
\tag{31}
\]

so the uniform reconstruction above applies.

On the core mesh from (25), the Ford horizontal coordinate is

\[
x_n
=\frac{2\pi qn}{Y}
=m(n\Delta_m),
\tag{32}
\]

hence

\[
|x_n|
\le
mB_K
\ll
m(\log K)^{1+\epsilon}.
\tag{33}
\]

Since `J=mK`,

\[
\frac{|x_n|}{J}
\le
\frac{B_K}{K}
\to0.
\tag{34}
\]

Therefore the inherited smooth shell envelope satisfies

\[
F\!\left(\frac{x_n+i u/Y}{J}\right)
=F(0)+o(1)
\tag{35}
\]

uniformly over the complete Gevrey reconstruction core. The number of carrier-locked mesh sites is

\[
O(mB_K)
=O\!\left(m(\log K)^{1+\epsilon}\right)
=o(mK)
=o(J).
\tag{36}
\]

Thus the stronger coercivity remains deep inside the central Ford window and uses only a vanishing fraction of the earlier `Theta(J)` population budget.

## 4. The matched compatibility control survives at order one

Partition the complex plane into a fixed finite number of angular cones of aperture strictly below `pi`. By (8), one cone contains a subset `S` of the reconstructed mesh such that

\[
\sum_{n\in S}|D_n|\gg m
\tag{37}
\]

and the values `D_n`, `n in S`, lie in a common cone. Place one formal simple matched zero at each carrier-locked ordinate

\[
\gamma_n
=t_0+\frac{2\pi qn}{X},
\qquad n\in S,
\tag{38}
\]

with common depth

\[
X(1-\beta_n)=\log m+d_*.
\tag{39}
\]

The principal shell carrier is exactly locked,

\[
e^{iX(\gamma_n-t_0)}=1,
\tag{40}
\]

while (35) keeps the fixed shell envelope in one positive cone. The Ford damping is

\[
e^{-X(1-\beta_n)}
=\frac{e^{-d_*}}m.
\tag{41}
\]

After reducing to a narrower angular subcone if necessary, vector addition therefore gives

\[
\boxed{
|\mathcal R_S|
\gg
\frac1m\sum_{n\in S}|D_n|
\gg1.
}
\tag{42}
\]

The spacing is the same `Theta(1/R)` carrier locking used in the earlier matched controls, and the population in (36) is `o(J)`. Hence the inherited zero-free, local-count and aggregate-density ledger used by `NB-264` does not exclude this formal configuration. Equation (42) remains a **matched compatibility control**, not evidence that the actual zeta zeros occupy these sites.

The quantitative advance over `NB-264` is that the compatible obstruction no longer needs a fixed-power enlargement of the packet-scale strip. For every `epsilon>0`, it is already forced within

\[
\boxed{
|x|
\ll_\epsilon
m(\log K)^{1+\epsilon}.
}
\tag{43}
\]

## 5. Boundaries and adversarial audit

The bounded-Hilbert hypothesis is again load-bearing. If

\[
M_K:=\|c\|_2
\]

is allowed to grow, (24) becomes

\[
CM_K\sqrt K\exp(-cB^{1/s}),
\tag{44}
\]

so the same proof works once

\[
B^{1/s}
\gg
\log(M_K\sqrt K).
\tag{45}
\]

Thus large coefficient conditioning can still export the anchor beyond the stated radius; this finding does not replace the total-variation/conditioning questions isolated earlier in the line.

The exponent `1+epsilon` is not claimed optimal. The present self-contained proof uses a compactly supported Gevrey-`s` plateau. Setting `s=1` would require a nonzero compactly supported real-analytic plateau, which is impossible, so this particular Gevrey argument cannot simply be specialized to `B=O(log K)`. More general non-quasianalytic classes can have Fourier decay closer to exponential and may sharpen the iterated-log factors further; that is a distinct quantitative step rather than a formal consequence of the proof above.

The result also does not contradict `NB-263`. Its approximate-annihilator construction chooses a target strip first, pays an uncontrolled finite witness norm, and only afterward makes `K` large enough to amortize that norm. `NB-265` says that if the eventual discrete resolved coefficient norm stays bounded, that diagonal cannot at the same time flatten a carrier-frequency radius as large as `C_epsilon(log K)^(1+epsilon)`. The remaining noncoercive diagonal must export the anchor on a still smaller rank-coupled scale or pay growing conditioning.

Nor does (42) upgrade the matched control to an actual-zeta theorem. The forced response is on a deterministic carrier-locked mesh. Nothing here proves that real zeta zeros sample the high-response subset. Arithmetic information about the actual zero locations remains an independent route to the final destination statement.

A direct falsification test is available. Choose any explicit Gevrey-`s` plateau satisfying (10)--(11), compute its period-`L_m` coefficients, and verify the exact finite-precision version of (19). A bounded-`ell^2` carrier that were uniformly `o(1)` on every site with `|nDelta_m|<=C(log K)^s` would force the complementary coefficient tail to carry asymptotically unit mass, contradicting (22)--(24).

## 6. Prior-art and novelty audit

Compactly supported Gevrey functions with stretched-exponential Fourier localization are standard harmonic-analysis technology. Tamer Tlas, *Bump Functions With Monotone Fourier Transforms Satisfying Decay Bounds*, J. Approx. Theory 278 (2022), 105742, arXiv:2003.12364, gives a particularly explicit neighboring construction with prescribed subexponential-power Fourier decay. A fresh 2026 example of the same generic mechanism is the periodic Gevrey extension and Fourier truncation used by Chenhao Zhao, Yinan Li and Dong An in *Quantum simulation of slow analytic time-dependent Hamiltonians*, arXiv:2608.17653 (18 August 2026). Neither source is used as a theorem in the proof above; (10)--(16) give the needed cutoff and decay directly, so no new durable dependency is required in `SOURCES.md`.

The line-specific content is the scaling bridge absent from that generic literature: the Gevrey tail is inserted into the exact Euler-anchor reconstruction on the Nyman/Ford carrier mesh, combined with `J=mK`, legal depth `u/Y`, bounded resolved shell-Hilbert cost, and the live damping `e^{-u}~1/m`. That converts generic stretched-exponential Fourier localization into the polylogarithmic coercivity statements (7)--(8) and the matched order-one control (42).

## 7. Consequence for the live research line

`NB-264` reduced the unresolved signed-scalar regime from arbitrary `o(K)` horizontal coverage to subpolynomial rank-coupled radii. `NB-265` removes most of that subpolynomial gap. For every fixed `epsilon>0`, bounded resolved Hilbert cost cannot uniformly suppress the carrier-locked live-depth mesh throughout

\[
|n\Delta_m|
\le
C_\epsilon(\log K)^{1+\epsilon}.
\tag{46}
\]

The remaining scalar frontier is therefore **almost logarithmic in the resolved rank**, rather than merely subpolynomial. The next non-circular question is whether one can replace the Gevrey plateau by a quantitatively sharper non-quasianalytic reconstruction and drive (46) down to `log K` times iterated-log losses, or whether the signed approximate-annihilator construction of `NB-263` can actually flatten the natural shallower radius (notably scales tied to `log m`) at bounded resolved Hilbert cost. Independently, actual-zeta sampling of the forced response remains the arithmetic route that could turn these compatibility obstructions into a theorem about the true zero set.