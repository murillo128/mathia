# WI-117 — BGSTB/Tsang admissibility forces the endpoint taper that triggers support-one screening

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. This finding does **not** improve Mathia's unconditional simple-critical zero proportion. It closes a specific live escape left by WI-115--WI-116: optimizing the support-one kernel inside the Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB)/Tsang positivity architecture cannot make the pair statistic retain a density-scale horizontal signal on the WI-005/WI-006 critical screening lattice. The reason is structural rather than numerical. The BGSTB admissibility condition that the compactly supported profile `j` have nonnegative Fourier transform already forces the support-edge trace `j(+-1)=0`; the generalized Tsang profile `J_b(alpha)=j(alpha)/cosh(b alpha)` therefore has the same endpoint taper, and WI-115's Poisson cancellation applies to the whole admissible class.

The endpoint fact itself is classical Fourier/positive-definite analysis. The durable consequence here is the interface theorem: **the same positivity package used to obtain the Tsang microscopic strip forces the boundary condition that makes the complete support-one pair statistic exactly screen a mirror pair against an on-line double on the critical lattice.** Escaping by a nonzero endpoint alias necessarily leaves this BGSTB/Tsang admissible class and requires a genuinely different pair-sum argument or support beyond one.

## 1. The primary-source admissibility conditions

The source is S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), 357--376; arXiv:2306.04799:

https://arxiv.org/abs/2306.04799

In their §4, BGSTB define Tsang's kernel from a profile `j` that is even, nonnegative, bounded, supported on `[-1,1]`, twice differentiable on `[0,1]` with one-sided endpoint derivatives, and satisfies

\[
\boxed{
0\le \widehat j(w)\ll \frac{1}{1+w^2}
\qquad(w\in\mathbb R).
}
\tag{1}
\]

With their Fourier convention

\[
\widehat j(w)=\int_{\mathbb R}j(\alpha)e^{-2\pi i w\alpha}\,d\alpha,
\tag{2}
\]

they then prove the Tsang properties

\[
\operatorname{Re}K(x+iy)>0\quad(|y|<1),
\qquad
K(z)\ll \frac{e^{|\operatorname{Im}z|}}{|z|^2}.
\tag{3}
\]

The revised follow-up S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros**, arXiv:2501.14545v3, revised 1 September 2026,

https://arxiv.org/abs/2501.14545

uses the generalized strip parameter `b` and

\[
\boxed{
K_b(z)=\frac1{2\pi}\int_{-1}^{1}
\frac{j(\alpha)}{\cosh(b\alpha)}e^{iz\alpha}\,d\alpha,
}
\tag{4}
\]

with `j` specialized there to the Fejer or Montgomery--Taylor profile. Its proof of strip positivity factors the real part as a convolution of `\widehat j` with a strictly positive transform. Thus nonnegativity of `\widehat j` is the load-bearing positivity interface inherited from the general Tsang construction, not an incidental property of the two displayed kernels.

## 2. Nonnegative Fourier transform plus compact support forces endpoint taper

The support-edge condition needed by WI-115 is not an independent design choice inside the class above.

We use the following classical lemma. Let `j in L^1(R)` be supported on `[-1,1]`, continuous at `0`, and suppose

\[
\widehat j(w)\ge0
\qquad(w\in\mathbb R).
\tag{5}
\]

Then `\widehat j in L^1(R)`, the inverse transform gives a continuous representative of `j`, and that representative vanishes at `+-1`.

A short proof makes the load-bearing point explicit. For `epsilon>0`, Gaussian regularization and Fubini give

\[
\begin{aligned}
I_\varepsilon
&:=\int_{\mathbb R}\widehat j(w)e^{-\pi\varepsilon w^2}\,dw\\
&=\int_{\mathbb R}j(\alpha)
\varepsilon^{-1/2}e^{-\pi\alpha^2/\varepsilon}\,d\alpha.
\end{aligned}
\tag{6}
\]

Because `j` is continuous at zero, the right side tends to `j(0)` as `epsilon downarrow 0`. On the left, (5) makes the integrand nonnegative and `e^{-pi epsilon w^2}` increases pointwise to one. Monotone convergence therefore yields

\[
\boxed{
\int_{\mathbb R}\widehat j(w)\,dw=j(0)<\infty.
}
\tag{7}
\]

Hence Fourier inversion produces the continuous function

\[
j_c(\alpha)=\int_{\mathbb R}\widehat j(w)e^{2\pi i w\alpha}\,dw
\tag{8}
\]

which agrees with `j` at its continuity points. Since the original `j` vanishes almost everywhere on the open sets `|alpha|>1`, continuity forces `j_c` to vanish there identically and therefore

\[
\boxed{j_c(-1)=j_c(1)=0.}
\tag{9}
\]

BGSTB's stated regularity makes `j` continuous up to the one-sided support edges, so its actual endpoint traces equal those of `j_c`. Thus every profile in their admissible class satisfies

\[
\boxed{j(-1)=j(1)=0.}
\tag{10}
\]

Condition (1)'s explicit `O(w^{-2})` decay is stronger than needed for (10); nonnegativity of the Fourier transform already forces integrability through (6)--(7). The stronger decay remains useful below for absolute summability of the lattice coefficients.

## 3. Every such generalized Tsang profile is exactly screened on the critical lattice

For any fixed `b>0`, put

\[
J_b(\alpha):=\frac{j(\alpha)}{\cosh(b\alpha)}.
\tag{11}
\]

Equation (10) immediately gives

\[
\boxed{J_b(-1)=J_b(1)=0.}
\tag{12}
\]

Now place one two-zero object at each critical lattice ordinate

\[
t_k=t_0+k\frac{2\pi}{L},
\qquad L=\log T,
\tag{13}
\]

and compare a symmetric off-line pair of normalized horizontal depth `y`,

\[
\frac12+\frac yL+it_k,
\qquad
\frac12-\frac yL+it_k,
\tag{14}
\]

with an on-line double at the same ordinate. As in WI-115, after cancelling the two same-sign ordered pairs, the difference contributed by lattice separation `n` is

\[
\boxed{
 d_n(y)=\frac1\pi\int_{-1}^{1}
 J_b(\alpha)e^{2\pi i n\alpha}
 \bigl(\cosh(2y\alpha)-1\bigr)\,d\alpha.
}
\tag{15}
\]

Define

\[
f_y(\alpha):=J_b(\alpha)\bigl(\cosh(2y\alpha)-1\bigr).
\tag{16}
\]

The central factor gives `f_y(0)=0`, while (12) gives `f_y(+-1)=0`. The Tsang decay in (3), or the corresponding `b`-version in the 2026 paper,

\[
K_b(z)\ll_b\frac{e^{|\operatorname{Im}z|}}{1+|z|^2},
\tag{17}
\]

implies `d_n(y)=O_{b,y}(n^{-2})`. The Fourier series is therefore absolutely summable, and Poisson summation at the critical dual lattice gives

\[
\boxed{
\sum_{n\in\mathbb Z}d_n(y)
=\frac1\pi\sum_{m\in\mathbb Z}f_y(m)
=\frac1\pi\bigl(f_y(-1)+f_y(0)+f_y(1)\bigr)
=0.
}
\tag{18}
\]

For every nontrivial nonnegative `j` and `y != 0`, the same-height term remains strictly positive,

\[
d_0(y)
=\frac1\pi\int_{-1}^{1}
J_b(\alpha)\bigl(\cosh(2y\alpha)-1\bigr)\,d\alpha>0.
\tag{19}
\]

Thus all of that local horizontal excess is cancelled exactly by the cross-height terms:

\[
\boxed{
\sum_{n\ne0}d_n(y)=-d_0(y)<0.
}
\tag{20}
\]

This is WI-115's screening identity, now with its endpoint hypothesis discharged automatically from the Tsang admissibility conditions rather than checked kernel by kernel.

## 4. The finite-block obstruction also holds throughout the class

For `M` consecutive screening sites, write

\[
\Delta_M(y)=\sum_{|n|<M}(M-|n|)d_n(y).
\tag{21}
\]

Using (18) and `d_n=O(n^{-2})` gives exactly as in WI-115

\[
\boxed{\Delta_M(y)=O_{b,y}(\log M)=o(M).}
\tag{22}
\]

Hence the failure is at the density scale relevant to a proportion theorem, not merely on the infinite ideal lattice. WI-115 also proves that restoring the exact unconditional Montgomery weight

\[
W(u)=\frac4{4-u^2}
\tag{23}
\]

changes a natural block `M=O(L)` by only `O(1)` under the same `1/n^2` kernel decay. Therefore the weighted BGSTB observable remains `o(M)`-blind to the mirror-pair-versus-double replacement for every kernel in this admissible support-one class.

No statement here says that actual zeta zeros form such a lattice. The lattice is a falsifier for what the proposed information carrier can distinguish: a deterministic density-scale controller derived only from this statistic must also hold on the screening configuration, where the horizontal signal vanishes asymptotically.

## 5. What kernel optimization can and cannot change

WI-115 left open the possibility that Fejer and Montgomery--Taylor happened to be unfortunate because both taper at the support edge. Equations (5)--(12) remove that loophole for the BGSTB/Tsang positivity architecture.

The three relevant properties are linked:

\[
\boxed{
\begin{array}{c}
\operatorname{supp}j\subset[-1,1]
\quad+\quad
\widehat j\ge0\\[1mm]
\Downarrow\\[1mm]
j(+-1)=0\\[1mm]
\Downarrow\\[1mm]
\text{the critical-lattice boundary aliases vanish}\\[1mm]
\Downarrow\\[1mm]
\text{the complete support-one horizontal signal screens at density scale.}
\end{array}
}
\tag{24}
\]

Changing the shape of `j`, optimizing the Tsang strip constant, or replacing Fejer/Montgomery--Taylor by another compactly supported positive-definite profile cannot alter this implication. In particular, one cannot keep the same convolution proof of strip positivity, merely choose `j(1) != 0`, and activate a boundary alias: a nonzero endpoint is incompatible with the stated nonnegative-Fourier compact-support class.

There remains an important scope boundary. BGSTB's unconditional evaluation lemma for a generic support-one test function is broader than the Tsang positivity class: it only asks for a real even `L^1` profile with a local Lipschitz condition at zero. A discontinuous/non-tapered support edge can therefore be inserted into the **evaluation identity** in isolation. This finding does **not** prove that every such support-one pair kernel is screened or unusable. Rather, once the nonnegative-transform/Tsang positivity package and the decay needed for the published same-height extraction are retained, endpoint taper is forced. An escape through a boundary alias must therefore supply a new positivity or signed-cancellation argument; it cannot be obtained by ordinary kernel optimization inside the existing Tsang proof.

## 6. Prior art, novelty, and research consequence

The analytic fact behind (6)--(10) is classical. It is a direct Fourier-inversion/Bochner-type consequence of nonnegative Fourier transform and compact support, and no novelty is claimed for compactly supported positive-definite functions being continuous and vanishing at the boundary of their support. BGSTB's own hypotheses already contain all ingredients; their papers do not need the present statement because they use explicit tapered kernels and are not studying the WI screening extremizer.

A targeted audit found no source formulating the specific zeta-zero consequence that the Tsang positivity admissibility itself forces the endpoint condition responsible for the critical-lattice mirror-pair/double cancellation. Absence of a search hit is not evidence of priority. The Mathia contribution is the exact interface audit against WI-005--WI-007 and WI-115--WI-116.

This closes one of the cheap routes left in `CLUE-higher-zero-correlations-horizontal-rigidity`: **another support-one kernel from the same BGSTB/Tsang positive-definite class cannot defeat screening merely by kernel optimization.** The live pair-level alternatives are now genuinely different: control the signed/weighted bad-pair reservoir directly, construct a support-one observable whose horizontal signal survives screening using a positivity mechanism outside this class, or cross support one and pay for the new arithmetic alias channel identified in WI-007. Mixed/higher-order horizontally sensitive observables remain separately open.

The decisive falsification boundary is equally clear. This finding would not obstruct a proposed pair kernel if its proof does not require a compactly supported `j` with `\widehat j>=0`, or if it obtains an order-one nonzero alias by a justified support-`>1` evaluation. It is a no-go theorem for the current Tsang admissible architecture, not for pair correlation as a whole.