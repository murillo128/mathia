# WI-118 — universal termwise positivity forces support-one pair screening

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. This finding does **not** improve Mathia's unconditional simple-critical zero proportion. It strengthens WI-117 from the specific BGSTB/Tsang positive-definite construction to a property-level obstruction: for any real-even support-one pair profile, **universal termwise nonnegativity on the real vertical axis already forces the support-edge taper that makes the mirror-pair-versus-double statistic asymptotically blind on the WI-005/WI-006 critical screening lattice**.

Consequently, the live escape in `CLUE-higher-zero-correlations-horizontal-rigidity` cannot be realized by inventing a different support-one pair kernel while retaining the same deterministic extraction principle “every cross-height term is nonnegative, so discard the ones not wanted.” To retain a density-scale boundary alias at support one, a pair-level argument must tolerate sign changes and control the signed cross-height reservoir by additional arithmetic information; otherwise it must cross support one or move to a genuinely different mixed/higher-order observable.

## 1. Exact statement

Let `J` be a real-valued even `L^1(R)` profile supported in `[-1,1]`, continuous at `0`, and define

\[
K(z):=\frac1{2\pi}\int_{-1}^{1}J(\alpha)e^{iz\alpha}\,d\alpha.
\tag{1}
\]

Assume

\[
\boxed{K(x)\ge 0\qquad(x\in\mathbb R).}
\tag{2}
\]

Because `J` is real and even, `K(x)` is real. Assumption (2) is weaker than the strip positivity used by Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB),

\[
\operatorname{Re}K(x+iv)>0
\qquad(x\in\mathbb R,\ |v|<b),
\tag{3}
\]

since (3) contains `v=0`.

Then `J` has a continuous representative, still denoted `J`, satisfying

\[
\boxed{J(-1)=J(1)=0.}
\tag{4}
\]

For a fixed normalized horizontal depth `y`, place at each of `M` consecutive critical-lattice ordinates

\[
t_j=t_0+j\frac{2\pi}{L},\qquad L=\log T,
\tag{5}
\]

either the symmetric mirror pair

\[
\frac12+\frac yL+it_j,
\qquad
\frac12-\frac yL+it_j,
\tag{6}
\]

or an on-line double at `1/2+it_j`. Let `Delta_M(y)` be the difference of the complete **unweighted** `K` pair statistics between these two blocks. Then

\[
\boxed{\frac{\Delta_M(y)}{M}\longrightarrow 0.}
\tag{7}
\]

No `1/n^2` Fourier-coefficient decay is needed for (7). If `J` is Lipschitz on `[-1,1]`, then the stronger bound

\[
\boxed{\Delta_M(y)=O_y(\log M)}
\tag{8}
\]

holds. Under the standard BGSTB-type `C^2` one-sided endpoint regularity, the exact Montgomery weight `W(u)=4/(4-u^2)` changes a natural block `M=O(L)` by only `O_y(1)`, so the corresponding weighted block difference is also `o(M)` (and is `O_y(log M)` in the Lipschitz case).

Thus universal real-axis termwise positivity and a density-scale support-edge alias are incompatible at bandwidth one.

## 2. Real-axis positivity alone forces endpoint taper

Use the Fourier convention

\[
\widehat J(w)=\int_{\mathbb R}J(\alpha)e^{-2\pi i w\alpha}\,d\alpha.
\tag{9}
\]

Equation (1) gives

\[
\widehat J(w)=2\pi K(-2\pi w).
\tag{10}
\]

Therefore (2) implies

\[
\widehat J(w)\ge0
\qquad(w\in\mathbb R).
\tag{11}
\]

The classical positive-definite/Fourier argument already used in WI-117 now applies directly to the **final pair profile `J`**, without assuming that `J` was manufactured from a Tsang profile `j/cosh(b alpha)`. For completeness, Gaussian regularization gives

\[
\int_{\mathbb R}\widehat J(w)e^{-\pi\varepsilon w^2}\,dw
=
\int_{\mathbb R}J(\alpha)\varepsilon^{-1/2}
 e^{-\pi\alpha^2/\varepsilon}\,d\alpha.
\tag{12}
\]

The right side tends to `J(0)` as `epsilon downarrow 0`. Because the left integrand is nonnegative, monotone convergence yields

\[
\int_{\mathbb R}\widehat J(w)\,dw=J(0)<\infty.
\tag{13}
\]

Fourier inversion therefore supplies a continuous representative of `J`. Since the original `L^1` profile vanishes almost everywhere on the open set `|alpha|>1`, this continuous representative vanishes there identically and hence at the boundary as well, proving (4).

This is a classical harmonic-analysis fact, not new mathematics: nonnegative Fourier transform makes the compactly supported profile positive definite/continuous, and continuity plus compact support forces its boundary trace to vanish. The new point is the interface consequence below: **any** support-one pair kernel that obtains a universal same-sign extraction by termwise nonnegativity automatically enters the screened endpoint class, even if its positivity proof is unrelated to Tsang's convolution construction.

## 3. Fejer averaging proves density-scale screening without coefficient decay

As in WI-115, after cancelling the two same-sign ordered pairs, the mirror-pair-versus-double difference at lattice separation `n` is

\[
d_n(y)
=
\frac1\pi\int_{-1}^{1}
J(\alpha)e^{2\pi i n\alpha}
\bigl(\cosh(2y\alpha)-1\bigr)\,d\alpha.
\tag{14}
\]

Put

\[
f_y(\alpha):=J(\alpha)\bigl(\cosh(2y\alpha)-1\bigr).
\tag{15}
\]

By (4) and the central factor,

\[
f_y(-1)=f_y(0)=f_y(1)=0.
\tag{16}
\]

For `M` consecutive sites,

\[
\begin{aligned}
\Delta_M(y)
&=\sum_{|n|<M}(M-|n|)d_n(y)\\
&=\frac1\pi\int_{-1}^{1}
f_y(\alpha)
\left|\sum_{j=0}^{M-1}e^{2\pi i j\alpha}\right|^2d\alpha.
\end{aligned}
\tag{17}
\]

Let

\[
F_M(\alpha)
:=\frac1M\left|\sum_{j=0}^{M-1}e^{2\pi i j\alpha}\right|^2
\tag{18}
\]

be the period-one Fejer kernel. Splitting `[-1,1]` into two periods gives

\[
\frac{\Delta_M(y)}{M}
=
\frac1\pi\int_0^1
\bigl(f_y(t)+f_y(t-1)\bigr)F_M(t)\,dt.
\tag{19}
\]

The bracket defines a continuous periodic function `g_y(t)` with

\[
g_y(0)=g_y(1)=f_y(0)+f_y(-1)=0.
\tag{20}
\]

Fejer's approximate-identity theorem therefore sends the right side of (19) to `g_y(0)/pi=0`, proving (7). This is stronger than the Poisson/absolute-summability route in WI-115: density-scale blindness follows solely from continuity and the three alias zeros.

If `J` is Lipschitz, then `g_y(t)=O_y(dist(t,Z))` near the period boundary. Using

\[
F_M(t)\ll \min\!\left(M,\frac1{M\,\|t\|^2}\right)
\tag{21}
\]

on the circle gives

\[
\int_0^1 |g_y(t)|F_M(t)\,dt
=O_y\!\left(\frac{\log M}{M}\right),
\tag{22}
\]

which proves (8).

## 4. Standard smoothness also leaves the exact Montgomery weight screened

BGSTB's unconditional evaluation carries the auxiliary factor

\[
W(u)=\frac4{4-u^2}.
\tag{23}
\]

Suppose now that `J` has the ordinary Tsang/BGSTB smoothness needed for two integrations by parts (for example `C^2` on `[0,1]` with one-sided endpoint derivatives, extended evenly), but do **not** assume their special representation `J=j/cosh(b alpha)`. From the already-forced endpoint condition (4), two integrations by parts give, uniformly for fixed bounded imaginary shift `v`,

\[
K(x+iv)=O_v\!\left(\frac1{1+x^2}\right).
\tag{24}
\]

Set

\[
h=\frac{2\pi}{L},\qquad a=\frac{2y}{L},\qquad u_n=nh.
\tag{25}
\]

For `|n|<=cL`, the elementary estimates used in WI-115 remain profile-independent:

\[
|W(iu_n)-1|\ll_c\frac{n^2}{L^2},
\qquad
|W(\pm a+iu_n)-W(iu_n)|\ll_{c,y}\frac1L.
\tag{26}
\]

Combining (24) and (26) gives the same per-separation comparison as WI-115,

\[
|d^W_{n,L}(y)-d_n(y)|
\ll_{c,y}
\left(
\frac1{L^2}+\frac1{L(1+n^2)}
\right).
\tag{27}
\]

After triangular summation over every natural block `M<=cL`,

\[
\sum_{|n|<M}(M-|n|)
\bigl(d^W_{n,L}(y)-d_n(y)\bigr)=O_{c,y}(1).
\tag{28}
\]

Together with (7), this proves `Delta^W_M(y)=o(M)`. Thus changing the *proof* of termwise positivity does not create an escape through the exact Montgomery weight as long as the replacement kernel retains the standard support-one smoothness/decay class.

## 5. The obstruction is sharp: a boundary alias requires sign changes

The endpoint condition is exactly where a support-one pair statistic can see the critical lattice at leading order. To expose the boundary, take the deliberately non-tapered box profile

\[
J_{\rm box}(\alpha)=1\qquad(|\alpha|\le1).
\tag{29}
\]

Then

\[
K_{\rm box}(x)=\frac{\sin x}{\pi x},
\tag{30}
\]

which changes sign, so universal termwise positivity fails. On the other hand, for the mirror-pair defect,

\[
f_y(0)=0,
\qquad
f_y(\pm1)=\cosh(2y)-1.
\tag{31}
\]

The same Fejer calculation, now with the nonzero boundary trace, gives

\[
\boxed{
\frac{\Delta_M^{\rm box}(y)}{M}
\longrightarrow
\frac{\cosh(2y)-1}{\pi}>0
\qquad(y\ne0).
}
\tag{32}
\]

So a support-edge alias really can restore an order-`M` horizontal signal; it does so precisely by leaving the universally nonnegative-kernel class. This prevents an overstrong interpretation of the no-go. The theorem does **not** say all support-one pair observables are screened. It says that the two desired features

\[
\boxed{
\text{universal termwise positivity}
\quad\text{and}\quad
\text{nonzero density-scale critical-lattice alias}
}
\tag{33}
\]

cannot coexist for a real-even support-one profile.

## 6. Primary-source bridge and prior-art audit

BGSTB's 2024 paper, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357--376; arXiv:2306.04799, makes the distinction needed here explicit. Its Lemma 5 evaluates the zero-pair sum for a broad class: any real-valued even `L^1` profile supported on `[-1,1]` and Lipschitz at zero. Thus unconditional support-one evaluation itself does **not** impose positive definiteness or endpoint taper. In §4, Tsang's additional kernel package gives `K(x)>0` for every real `x`, `K(z)=O(e^{|Im z|}/|z|^2)`, and strip positivity.

The revised follow-up, S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros**, arXiv:2501.14545v3 (revised 1 September 2026), makes the logical use of positivity especially clear: Lemma 3 proves `Re K_b(x+iy)>0` in `|y|<b`, and the proof of their later zero-count inequality discards unwanted terms because every term in the box-restricted sum is positive.

The harmonic-analysis ingredients used above are classical. The implication “nonnegative Fourier transform -> positive-definite continuous representative” is the Euclidean Bochner/Fourier-inversion framework; the concentration of (18) is Fejer's classical approximate-identity theorem. No novelty is claimed for either fact, nor for the endpoint vanishing of a continuous compactly supported function.

A targeted prior-art search found no source formulating the specific zeta-zero screening consequence (33). Absence of such a source is not evidence of priority. The durable Mathia contribution is the exact interface theorem: WI-117's endpoint obstruction is not merely a feature of the published Tsang construction; **universal termwise positivity itself forces entry into the screened support-one class**.

## 7. Consequence for the horizontal-rigidity program

WI-115 established that a complex pair kernel contains local horizontal information but that the complete tapered support-one statistic cancels it on the critical lattice. WI-116 showed that currently established zero-density estimates cannot simply discard the bad-pair reservoir. WI-117 then showed that ordinary kernel optimization inside the BGSTB/Tsang compactly supported positive-definite design cannot activate the endpoint alias.

The present result closes a broader loophole left by WI-117. One cannot keep support one, replace Tsang by a different real-even kernel, and recover the same deterministic same-height extraction through some *other* proof of universal termwise positivity: the positivity property itself implies the endpoint taper and hence (7).

What remains live is genuinely different information. A support-one pair route must allow sign changes and prove a source-specific bound for the signed cross-height reservoir; positivity only on a rigorously controlled discrete subset of separations would also lie outside the theorem, but would require new information about where zeta separations occur. Otherwise one must activate a justified support-`>1` alias or use a mixed/higher-order horizontally sensitive statistic. The accepted `CLUE-higher-zero-correlations-horizontal-rigidity` therefore remains unresolved, but its “different support-one positivity mechanism” branch is now closed at the universal termwise level.

### Decisive falsification boundary

This finding would not obstruct a proposed method if its pair profile is not real-even/support-one, if it does not require `K(x)>=0` for all real vertical separations, or if it controls the signed cross-height contribution by an independent arithmetic theorem instead of discarding it termwise. It also says nothing against supercritical support or genuinely higher-order observables. Within the stated class, however, the endpoint implication (10)--(13) and the exact Fejer identity (17)--(20) leave no optimization parameter that can restore a density-scale screening alias.