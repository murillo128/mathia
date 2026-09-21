---
title: "NB-267 - Rank-adaptive spline cutoffs reach logarithmic Ford mesh coercivity"
date: 2026-09-21
type: research-finding
status: verified
research_line: nyman_beurling
finding_id: NB-267
claim_kind: derived
verification:
  - type: source-audit
    details: "Derived from the exact Euler-anchor reconstruction of NB-264--NB-266 using an explicit K-dependent finite box convolution; no external theorem is load-bearing."
  - type: owner-side-stress-test
    details: "Checked K-dependence of the auxiliary cutoff, fixed support, exact plateau identity, complex-depth strip control, discrete lattice-tail normalization, loss of pointwise coercivity, Ford-shell scaling, and compatibility-only status of the matched packet."
  - type: representation-audit
    details: "The finite-convolution/sinc-power estimate is generic harmonic analysis; the Euler normalization, J=mK coupling, live Ford depth, and conversion of aggregate mesh response into an order-one matched residue are Nyman-Beurling specific."
sources:
  - research/nyman_beurling/findings/NB-266-infinite-convolution-cutoffs-push-ford-mesh-coercivity-through-iterated-log-losses.md
related:
  - NB-266
  - NB-265
  - NB-264
  - NB-263
  - NB-233
---

# NB-267 - Rank-adaptive spline cutoffs reach logarithmic Ford mesh coercivity

## Result

NB-266 pushed the exact Euler-anchor reconstruction to

\[
B_K
=
\log K\times\text{an arbitrarily deep fixed iterated-log loss},
\]

but left the pure logarithmic endpoint open. The obstruction there was the use of one fixed compact smooth cutoff: exponential Fourier decay is impossible for a nonzero compactly supported function, so a fixed cutoff cannot simply be sharpened all the way to the endpoint.

That restriction is unnecessary for the reconstruction argument. The cutoff is an auxiliary dual certificate, not part of the Nyman source. It may therefore depend on the resolved carrier rank \(K\).

A rank-adaptive finite convolution reaches the endpoint.

Keep the NB-266 setup

\[
J=mK,
\qquad
m\to\infty,
\qquad
K\to\infty,
\]

and

\[
C_J(w)
=
\sum_{j=0}^{K-1}c_j e^{ijw/J},
\qquad
\sum_{j=0}^{K-1}c_j=1,
\qquad
\|c\|_2\le M.
\]

At the live shallow depth

\[
u=\log m+d_*,
\]

sample the carrier on the same locked mesh

\[
D_n
=
C_J\!\left(
\frac{2\pi qn}{Y}+i\frac{u}{Y}
\right),
\qquad
\Delta_m=\frac{2\pi q}{Ym}.
\]

Then there is a sequence of compact plateau cutoffs \(\chi_K\), all supported in one fixed interval and satisfying \(0\le\chi_K\le1\) and \(\chi_K=1\) on \([0,1]\), for which the exact Euler-anchor identity has dual coefficients \(d_{n,K}\) satisfying

\[
1
=
\sum_{n\in\mathbb Z}d_{n,K}D_n,
\]

and, for a fixed sufficiently large constant \(B_0\),

\[
\boxed{
\sum_{|n\Delta_m|>B_0\log K}
|d_{n,K}|
=o(K^{-1/2}).
}
\]

Since \(|D_n|\le M\sqrt K\), the omitted part is \(o(1)\). Moreover

\[
|d_{n,K}|\ll \frac1m
\]

uniformly. Hence

\[
\boxed{
\sum_{|n\Delta_m|\le B_0\log K}|D_n|
\gg m.
}
\]

Thus the aggregate coercivity needed by the matched Ford control already occurs at

\[
\boxed{B_K=O(\log K).}
\]

The endpoint left open by NB-266 is therefore attainable for the quantity that matters to the Ford residue.

There is one deliberate qualification. The present proof does not preserve the NB-266 pointwise lower bound \(\sup|D_n|\gg1\). It only gives the aggregate \(\Omega(m)\) response, and a crude averaging bound gives \(\sup|D_n|\gg1/\log K\). The aggregate statement is nevertheless exactly what is needed to build the order-one matched residue.

## 1. Exact reconstruction input

Write

\[
\alpha=\frac{u}{YJ},
\qquad
\beta_K:=\alpha K=\frac{u}{Ym}=o(1).
\]

As in NB-264--NB-266, if \(\chi\) is any compact plateau equal to one on \([0,1]\), set

\[
g_{K}(t)=\chi(t)e^{\beta_K t}.
\]

For large \(m\), the fixed support of \(g_K\) lies inside one period of the mesh periodization. If \(d_{n,K}\) are the resulting Fourier coefficients, then evaluation at \(t=j/K\) gives

\[
\sum_{n\in\mathbb Z}
d_{n,K}e^{ijn\Delta_m}
=
e^{\beta_K j/K}
=
e^{\alpha j}.
\]

Multiplying by \(c_j e^{-\alpha j}\), summing over \(j\), and using \(\sum_jc_j=1\) yields the exact identity

\[
\boxed{
1
=
\sum_{n\in\mathbb Z}d_{n,K}D_n.
}
\]

The previous findings chose one cutoff first and then sent \(K\to\infty\). Here the cutoff order is allowed to grow with \(K\). This does not change the identity: for every fixed \(K\), \(\chi_K\) is an ordinary compact plateau and the Fourier series is absolutely convergent once its finite convolution order is at least a few derivatives.

## 2. Rank-adaptive compact plateau

Fix once and for all a small \(\sigma\in(0,1/4)\). Let

\[
N=N_K=\lceil A\log K\rceil,
\]

where \(A>0\) will be chosen later. Define the normalized box

\[
\rho_N(t)
=
\frac{N}{\sigma}
\mathbf 1_{[-\sigma/(2N),\,\sigma/(2N)]}(t),
\]

and its \(N\)-fold convolution

\[
\psi_N
=
\rho_N^{*N}.
\]

Then \(\psi_N\) is a nonnegative probability density with

\[
\operatorname{supp}\psi_N
\subset[-\sigma/2,\sigma/2].
\]

It is the elementary one-dimensional B-spline generated by repeated equal box convolution. Its Fourier-Laplace transform is exactly

\[
\widehat\psi_N(z)
=
\operatorname{sinc}\!\left(
\frac{\sigma z}{2N}
\right)^N.
\]

Now define

\[
\chi_K
=
\mathbf 1_{[-\sigma/2,\,1+\sigma/2]}*\psi_N.
\]

Because \(\psi_N\) is a probability density,

\[
0\le\chi_K\le1,
\]

and because its support has radius \(\sigma/2\),

\[
\chi_K(t)=1
\qquad(0\le t\le1).
\]

All cutoffs have the same support bound

\[
\operatorname{supp}\chi_K
\subset[-\sigma,1+\sigma].
\]

The smoothness is finite but increasing: \(\chi_K\) is at least \(C^{N-1}\). Since \(N\to\infty\), this is far more than required for absolute Fourier-series convergence at each sufficiently large \(K\).

The key difference from NB-266 is that the transition profile sharpens with rank instead of converging to one fixed \(C_c^\infty\) cutoff.

## 3. Uniform strip decay beyond frequency O(N)

The interval factor in \(\chi_K\) is harmless on every fixed horizontal strip, so for \(|\eta|\le1\),

\[
|\widehat\chi_K(x+i\eta)|
\ll
\left|
\operatorname{sinc}\!\left(
\frac{\sigma(x+i\eta)}{2N}
\right)
\right|^N.
\]

Fix a constant \(b>0\). There are constants \(R>b\), \(\rho\in(0,1)\), and \(N_0\), depending only on \(b\) and \(\sigma\), such that for \(N\ge N_0\),

\[
bN\le |x|\le RN,
\qquad |\eta|\le1,
\]

implies

\[
\left|
\operatorname{sinc}\!\left(
\frac{\sigma(x+i\eta)}{2N}
\right)
\right|
\le\rho.
\]

Indeed, after rescaling, the real part ranges in a compact set bounded away from zero while the imaginary part is \(O(1/N)\). The real sinc has modulus strictly below one away from the origin, and the complex perturbation is uniform.

For \(|x|\ge RN\), the elementary estimate

\[
|\sin(a+ib)|\le e^{|b|}
\]

gives

\[
\left|
\operatorname{sinc}\!\left(
\frac{\sigma(x+i\eta)}{2N}
\right)
\right|
\ll
\frac{N}{|x|}.
\]

Choosing \(R\) large enough, we obtain the two-region bound

\[
|\widehat\chi_K(x+i\eta)|
\le
\begin{cases}
C\rho^N,
& bN\le|x|\le RN,\\[4pt]
C(C_0N/|x|)^N,
& |x|\ge RN,
\end{cases}
\]

uniformly for \(|\eta|\le1\).

The live depth tilt causes exactly such a bounded imaginary shift, because

\[
\beta_K=\frac{\log m+O(1)}{Ym}\to0.
\]

Therefore the same estimates apply to

\[
\widehat g_K(x)
=
\widehat\chi_K(x+i\beta_K)
\]

for all sufficiently large \(m\).

## 4. Discrete Fourier tail is exponentially small in N

Let \(L_m\asymp m\) denote the period length in the exact reconstruction. Up to the fixed Fourier normalization,

\[
d_{n,K}
=
\frac1{L_m}
\widehat g_K(n\Delta_m),
\qquad
\Delta_m\asymp\frac1m.
\]

Set

\[
B_N=bN.
\]

In the intermediate region \(B_N<|n\Delta_m|\le RN\), there are \(O(mN)\) lattice points and each coefficient has size \(O(m^{-1}\rho^N)\). Hence this part contributes

\[
O(N\rho^N).
\]

In the outer region, use the power bound. If \(n_0\asymp mRN\), then

\[
\frac1m
\sum_{|n|\ge n_0}
\left(
\frac{C_0Nm}{|n|}
\right)^N
\ll
\left(\frac{C_1}{R}\right)^N
\]

for fixed sufficiently large \(R\). Consequently there is a constant \(c>0\), independent of \(m,K\), such that

\[
\boxed{
\sum_{|n\Delta_m|>bN}
|d_{n,K}|
\ll
N e^{-cN}.
}
\]

Now choose

\[
N=\lceil A\log K\rceil
\]

with \(A\) so large that \(cA>1/2\) by a fixed margin. Then

\[
N e^{-cN}
=o(K^{-1/2}).
\]

Thus, with

\[
B_K=bN=O(\log K),
\]

we have

\[
\boxed{
\sum_{|n\Delta_m|>B_K}
|d_{n,K}|
=o(K^{-1/2}).
}
\]

This is the logarithmic endpoint that a single fixed compact cutoff cannot obtain from uniform near-exponential Fourier decay.

There is no contradiction with the classical compact-support barrier. For each \(K\), the cutoff has only finite smoothness, and its order grows with \(K\). We are not constructing one nonzero compactly supported function with exponentially decaying Fourier transform.

## 5. Exact anchor forces aggregate response inside O(log K)

The carrier obeys the universal bounded-cost estimate

\[
|D_n|
\le
\|c\|_2\sqrt K
\le
M\sqrt K.
\]

Therefore the discarded tail in the exact reconstruction is

\[
\left|
\sum_{|n\Delta_m|>B_K}
d_{n,K}D_n
\right|
\le
M\sqrt K
\sum_{|n\Delta_m|>B_K}|d_{n,K}|
=o(1).
\]

Hence

\[
\left|
\sum_{|n\Delta_m|\le B_K}
d_{n,K}D_n
\right|
\ge1-o(1).
\]

The cutoffs have uniformly bounded support and amplitude, while the depth tilt is bounded. Thus

\[
\|g_K\|_1=O(1)
\]

uniformly, and so every Fourier coefficient satisfies

\[
|d_{n,K}|
\ll\frac1m.
\]

It follows that

\[
1-o(1)
\ll
\frac1m
\sum_{|n\Delta_m|\le B_K}|D_n|,
\]

which gives

\[
\boxed{
\sum_{|n\Delta_m|\le C\log K}|D_n|
\gg m.
}
\]

This is the exact quantity used by the matched Ford packet.

Unlike NB-266, the present construction does not give a uniform \(\ell^1\) bound for the full dual coefficient sequence. In fact the sharpening transition makes such a bound naturally grow. Therefore one should not infer

\[
\sup|D_n|\gg1
\]

from this proof. Since the number of retained mesh points is \(O(m\log K)\), the aggregate statement only implies the crude pointwise estimate

\[
\sup_{|n\Delta_m|\le C\log K}|D_n|
\gg\frac1{\log K}.
\]

The loss is harmless for the residue construction because that construction sums a phase-aligned subfamily rather than requiring one large atom.

## 6. Return to physical Ford coordinates

The physical Ford coordinate of the locked mesh is

\[
x_n=m n\Delta_m.
\]

Therefore

\[
|n\Delta_m|\le C\log K
\quad\Longrightarrow\quad
|x_n|\ll m\log K.
\]

Since \(J=mK\),

\[
\frac{|x_n|}{J}
\ll
\frac{\log K}{K}
\to0.
\]

Thus the entire reconstructed region stays inside the same local shell patch as NB-264--NB-266, and

\[
F\!\left(
\frac{x_n}{J}+i\frac{u}{YJ}
\right)
=F(0)+o(1)
\]

uniformly.

The number of available locked sites is

\[
O(m\log K)
=o(mK)
=o(J).
\]

This is smaller than the population used in NB-266, whose radius carried an additional iterated-log loss. Hence all previously audited compatibility ledgers for local zero counts, the Bellotti shallow regime, and the source normalization remain valid without strengthening.

Partition the values \(D_n\) in the retained region into a fixed number of angular cones. One cone carries \(\Omega(m)\) of the aggregate modulus. Place the same matched compatibility packet as before at the corresponding carrier-locked ordinates, with

\[
X(1-\beta_n)
=
\log m+d_*.
\]

The principal carrier phase is locked, the local envelope is \(F(0)+o(1)\), and each pole carries damping

\[
e^{-X(1-\beta_n)}
=
\frac{e^{-d_*}}m.
\]

Therefore the selected cone contributes

\[
\frac1m\times\Omega(m)
=
\Omega(1)
\]

to the matched residue.

As throughout NB-230 onward, this packet is adversarial compatibility data only. It does not assert that the actual zeros of \(\zeta\) occupy these sites.

## 7. What the endpoint does and does not settle

The result closes the specific cutoff-optimization gap left by NB-266. The hierarchy

\[
K^\delta
\to
(\log K)^{1+\epsilon}
\to
\log K\times\text{iterated-log loss}
\]

came from insisting on a single auxiliary cutoff whose regularity was fixed before \(K\) grew. Once the dual certificate is allowed to adapt to rank, a finite convolution of order \(N\asymp\log K\) supplies exactly the amount of Fourier-tail suppression needed to beat the universal \(\sqrt K\) carrier bound.

The argument does not prove that \(O(\log K)\) is a universal lower limit for every conceivable reconstruction. Within the equal-box convolution family it is natural: obtaining an \(e^{-cN}\) tail needs \(N\gtrsim\log K\), while fixed support forces the frequency at which all \(N\) factors contract to be \(\gtrsim N\). A general sublogarithmic impossibility would require a separate uncertainty or duality theorem and is not claimed here.

Nor does the finding prove a lower bound for the actual Nyman--Beurling distance. It remains source-side. Its consequence is narrower and useful: **a bounded-cost resolved scalar carrier cannot hide the Euler anchor from the matched Ford mesh merely by surviving every fixed compact-cutoff localization loss; the exact reconstruction can now reach logarithmic radius.**

The remaining substantive bridge is therefore no longer finer cutoff regularity. It is whether the aggregate logarithmic-radius obstruction survives the true Hardy/Nyman projection or whether target-side structure rules out the matched compatibility packet.

## 8. Prior-art audit

Repeated convolution of compact boxes and the resulting sinc-power Fourier transform are classical B-spline facts. The generic mechanism is therefore not new, and no novelty is claimed for it.

What is specific here is the rank-adaptive use of the convolution order \(N\asymp\log K\) inside the exact Euler-anchor reconstruction, together with the cancellation of the mesh density by the \(1/m\) Fourier-coefficient normalization and the conversion of the resulting aggregate \(\Omega(m)\) response into the live Ford residue at depth \(u=\log m+O(1)\).

The proof derives every load-bearing estimate directly, so no new external theorem is required and `SOURCES.md` does not need a new dependency.

## 9. Owner-side adversarial review

Several possible overclaims were checked explicitly.

First, the \(K\)-dependent cutoff is legal only because it is an auxiliary reconstruction certificate. The Nyman source and the resolved carrier coefficients \(c_j\) are not being modified after seeing the zero packet. The exact identity holds separately for every \(K\).

Second, finite smoothness is enough. The periodized cutoff has order tending to infinity, and for every sufficiently large \(K\) its Fourier coefficients are absolutely summable. No passage to a single limiting cutoff is used.

Third, the depth tilt does not destroy the sinc-power gain. It shifts the Fourier transform by \(i\beta_K\) with \(\beta_K=o(1)\), while the strip estimate above is uniform for a fixed neighborhood of the real axis.

Fourth, the endpoint is aggregate rather than pointwise. The proof must not inherit the stronger \(\sup|D_n|\gg1\) statement of NB-266. The phase-cone argument uses only the proved \(\sum|D_n|\gg m\), so no missing pointwise step enters the matched residue.

Fifth, the site count is \(O(m\log K)=o(J)\), and the shell displacement is \(O((\log K)/K)\). Thus the logarithmic localization does not silently leave the local Ford patch or demand a denser compatibility packet than the already-audited NB-266 construction.

Finally, no claim is made that actual zeta zeros realize the matched packet, nor that the Hardy projection preserves the source-side obstruction. Those remain the line's zeta-specific unresolved steps.

## Consequence

The pure logarithmic endpoint in the NB-264--NB-266 Euler-anchor reconstruction is reachable once the auxiliary cutoff is allowed to adapt to carrier rank:

\[
\boxed{
B_K=O(\log K),
\qquad
\sum_{|n\Delta_m|\le B_K}|D_n|\gg m.
}
\]

Hence another refinement of a fixed Gevrey or nonquasianalytic cutoff is no longer the useful next experiment. The live question moves to the target side: whether this aggregate logarithmic-radius response is seen by the exact Hardy/Nyman projection, or whether genuinely zeta-specific structure prevents the matched Ford packet from occurring.