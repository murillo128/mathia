# WI-140 — Lamzouri off-line confluence defeats every count-only finite stability charge

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. WI-136--WI-139 show that near saturation of Lamzouri's finite Hilbert-space inequality forces off-line odd vectors toward the exceptional span `U`, forces the full signed tensor toward a `2/1/0` quantized operator, identifies exactly one negative eigenvalue per distinct off-line pair, and aligns the negative eigenspace with the horizontal quotient. There is nevertheless a sharp finite obstruction to turning those facts into a universal positive charge per off-line pair: a simple off-line conjugate pair can **confluence continuously to a critical-line double**, with the complete Lamzouri deficit tending to zero quadratically while its negative index stays equal to one at every nonzero horizontal displacement.

More strongly, for every fixed number `k` of distinct simple off-line pairs and every `epsilon>0`, there is an admissible finite Lamzouri configuration containing exactly those `k` pairs and no real points for which

\[
0\le \Delta:=n-(2N-Q)<\epsilon.
\]

Hence no universal inequality of the form `Delta >= c k` with `c>0`, nor even `Delta >= phi(k)` with `phi(k)>0` for one fixed positive `k`, can hold in the abstract class of Proposition 2.1. By combining asymptotically orthogonal simple-real singleton blocks with confluent off-line-pair blocks, one can moreover make `Delta/N -> 0` while prescribing any limiting simple-real fraction `s in [0,1]` and simultaneously obtaining

\[
\frac QN\longrightarrow 2-s,
\]

with **all of the complementary population simple and off-line**. In particular, the finite Hilbert inequality together with the single scalar pair-correlation value used to reach the Montgomery--Taylor constant cannot by itself characterize the uncertified complement.

This is a barrier to a count-only finite stability refinement, not a zeta counterexample. The many-block constructions below are deliberately dilute in Lamzouri's rescaled ordinate variable and do not satisfy the density/correlation constraints of actual zeta zeros. A successful defect-to-zero bootstrap must therefore use some source-specific interaction that forbids or charges this confluence geometry -- for example local density/separation information, a genuinely additional correlation observable, or another arithmetic invariant -- rather than only the finite deficit, negative index, or Hilbert--Schmidt distance already exposed in WI-136--WI-139.

## 1. Exact isolated off-line pair

Use the notation of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882, Proposition 2.1. Let `eta` be his real even compactly supported function, normalized by

\[
\widehat{\eta^2}(0)=\int_{\mathbb R}\eta(u)^2\,du=1.
\]

Take one simple non-real conjugate pair

\[
z=x+iy,\qquad \bar z=x-iy,\qquad y>0.
\]

Lamzouri's vectors are

\[
f_z(u)=\eta(u)e^{-2\pi iuz},
\qquad
 g=\frac{f_z+f_{\bar z}}2,
\qquad
 h=\frac{f_z-f_{\bar z}}{2i}.
\]

They have the explicit form

\[
g(u)=\eta(u)e^{-2\pi iux}\cosh(2\pi uy),
\qquad
h(u)=-i\eta(u)e^{-2\pi iux}\sinh(2\pi uy).
\tag{1}
\]

Because `eta^2` is even while `cosh(2 pi u y) sinh(2 pi u y)` is odd,

\[
\boxed{\langle g,h\rangle=0.}
\tag{2}
\]

Put

\[
t=t(y):=\|h\|^2
=\int_{\mathbb R}\eta(u)^2\sinh^2(2\pi uy)\,du.
\tag{3}
\]

The identity `cosh^2-sinh^2=1` and the normalization of `eta` give

\[
\boxed{\|g\|^2=1+t.}
\tag{4}
\]

For this configuration Lamzouri's spaces are

\[
U=V=\operatorname{span}\{g\},
\qquad
H=W\ominus V=\operatorname{span}\{h\},
\tag{5}
\]

and WI-137's self-adjoint tensor operator is exactly

\[
\mathcal A_F=2(g\otimes g-h\otimes h).
\tag{6}
\]

Since `g` and `h` are orthogonal, its two eigenvalues on `W` are

\[
\boxed{
\lambda_+=2(1+t),
\qquad
\lambda_-=-2t.
}
\tag{7}
\]

Thus WI-138's inertia count is visible without any perturbation theorem: there is exactly one negative eigenvalue for every `y>0`, however small.

The Lamzouri target is

\[
\mathcal D=P_U+P_V=2P_U.
\]

Therefore

\[
\boxed{
\|\mathcal A_F-\mathcal D\|_{\rm HS}^2
=(2t)^2+(-2t)^2=8t^2.
}
\tag{8}
\]

The tensor norm is equally explicit. Orthogonality in (2) gives

\[
\begin{aligned}
Q=\|F\|^2
&=4\bigl(\|g\|^4+\|h\|^4\bigr)\\
&=4\bigl((1+t)^2+t^2\bigr)\\
&=4+8t+8t^2.
\end{aligned}
\tag{9}
\]

Here `N=2` and `n=0`, so the complete finite deficit is

\[
\boxed{
\Delta=n-(2N-Q)=Q-4=8t+8t^2.
}
\tag{10}
\]

This also checks WI-137 term by term. The `U` coefficient excess is `B=2t`, while `H_U=H_V=t`; hence

\[
\Delta
=\underbrace{8t^2}_{\|A_F-D\|_{HS}^2}
 +\underbrace{4t}_{2B}
 +\underbrace{4t}_{4H_V}.
\tag{11}
\]

For this pair the negative eigenspace is exactly `H` for every `y`, so the principal-angle loss in WI-139 is identically zero. The isolated pair therefore saturates the **orientation** requirement perfectly while its amplitude collapses.

## 2. Quadratic confluence to a real double

Compact support of `eta` permits termwise Taylor expansion in (3). If

\[
\mu_2:=\int_{\mathbb R}u^2\eta(u)^2\,du>0,
\]

then as `y -> 0`,

\[
\boxed{
t(y)=4\pi^2\mu_2 y^2+O(y^4).}
\tag{12}
\]

Consequently

\[
\boxed{
\lambda_-=-8\pi^2\mu_2 y^2+O(y^4),
\qquad
\Delta=32\pi^2\mu_2 y^2+O(y^4).
}
\tag{13}
\]

At `y=0` the two points merge into a real point of multiplicity two. Then `h=0`, the space `H` disappears, and the operator is simply

\[
\mathcal A_F=2f_x\otimes f_x=2P_U,
\]

which is an exact equality configuration for Lamzouri's finite inequality. Thus the simple off-line pair approaches the real double continuously in every norm quantity entering WI-136--WI-139, while the negative index changes discontinuously at the confluent endpoint.

This identifies the fundamental obstruction to converting WI-138's exact sign count into a norm-based spectral gap. Sylvester inertia remembers that `lambda_-<0` for every finite `y>0`; the deficit only sees its vanishing magnitude and the simultaneously vanishing odd-vector charge. There is no contradiction between exact negative index and arbitrarily small total slack.

## 3. Fixed-`k` no-go for every positive pair-count charge

The one-pair calculation already disproves `Delta >= c k` for `k=1`. The obstruction persists for every prescribed finite `k` even when all pairs are distinct.

Let

\[
K(t):=\widehat{\eta^2}(t).
\]

First place `k` real double points at distinct real centers `x_1,...,x_k`. This collapsed configuration has `N=2k`, `n=0`, and

\[
Q_0=4\sum_{i,j=1}^k K(x_i-x_j)^2.
\tag{14}
\]

Since `K(0)=1`,

\[
\Delta_0=Q_0-4k
=4\sum_{i\ne j}K(x_i-x_j)^2.
\tag{15}
\]

The function `eta^2` is in `L^1`, so the classical Riemann--Lebesgue lemma gives `K(t)->0` on the real axis. For any `delta>0`, choose the centers sufficiently far apart that

\[
|K(x_i-x_j)|<\delta
\qquad(i\ne j).
\tag{16}
\]

Then

\[
0\le\Delta_0<4k(k-1)\delta^2.
\tag{17}
\]

Now replace each double at `x_j` by the simple conjugate pair `x_j\pm iy`. Because `eta` is compactly supported, `K` extends to an entire function, and the finite pair sum `Q_y` depends continuously on `y`. Hence

\[
\Delta_y=Q_y-4k\longrightarrow\Delta_0
\qquad(y\to0).
\tag{18}
\]

Given any `epsilon>0`, first choose `delta` so that the right-hand side of (17) is below `epsilon/2`, then choose `y>0` so small that `|Delta_y-Delta_0|<epsilon/2`. The resulting multiset consists of exactly `k` distinct simple off-line conjugate pairs and satisfies

\[
\boxed{0\le\Delta_y<\epsilon.}
\tag{19}
\]

Therefore

\[
\boxed{
\inf\{\Delta:\text{exactly `k` distinct simple off-line pairs}\}=0
\quad\text{for every }k\ge1.
}
\tag{20}
\]

In particular, no abstract stability theorem for Lamzouri's Proposition 2.1 can have

\[
\Delta\ge c\,k
\qquad(c>0)
\tag{21}
\]

or even `Delta >= phi(k)` with `phi(k)>0` at one fixed positive `k`, unless it imposes additional geometric/arithmetic hypotheses not present in the finite proposition.

Taking `k->infinity` and choosing the construction with, say, `Delta_k<1/k` yields

\[
\boxed{
\frac{\Delta_k}{N_k}\to0,
\qquad
N_k=2k,
}
\tag{22}
\]

while every point remains simple and off-line. This is an abstract finite-Hilbert-space near-extremizer family, not a zeta-density model.

## 4. Mixed near-extremizers match any scalar `Q/N`

The obstruction is stronger than the pure off-line example because it can reproduce the scalar relation used in the asymptotic zeta application at any desired simple-real fraction.

There are two exact/asymptotic local blocks:

- one isolated simple real point has `(N,n,Q)=(1,1,1)` and `Delta=0` exactly;
- one simple off-line conjugate pair at horizontal depth `y` has `(N,n,Q)=(2,0,4+o(1))` and `Delta=o(1)` as `y->0` by (9)--(10).

Take `a` singleton blocks and `b` pair blocks. Separate all their real centers sufficiently far that every cross-block kernel term is negligible. For fixed small `y`, the relevant horizontal translates of `K` are Fourier transforms of compactly supported `L^1` functions and obey the same Riemann--Lebesgue decay; since each construction is finite, the centers can be chosen so that the total cross contribution is arbitrarily small. Then let `y->0`. The combined configuration satisfies

\[
N=a+2b,
\qquad
n=a,
\qquad
Q=a+4b+o(N),
\tag{23}
\]

and therefore

\[
\boxed{
\frac nN=\frac{a}{a+2b},
\qquad
\frac QN=2-\frac nN+o(1),
\qquad
\frac\Delta N\to0.
}
\tag{24}
\]

Given any prescribed `s in [0,1]`, choose integer sequences `a_j,b_j` with

\[
\frac{a_j}{a_j+2b_j}\longrightarrow s
\]

and make the cross interactions and pair depths small enough at each stage. Then

\[
\boxed{
\frac nN\to s,
\qquad
\frac QN\to2-s,
\qquad
\frac\Delta N\to0,
}
\tag{25}
\]

while the entire complementary fraction `1-s` consists of simple off-line points; there are no real multiple zeros at all.

Taking `s` equal to the Montgomery--Taylor simple-critical baseline gives an abstract finite configuration with the same limiting scalar `Q/N` relation that drives Lamzouri's application and with asymptotically sharp finite inequality, yet with every uncertified point off the real axis in Lamzouri coordinates. This does **not** say that zeta zeros can realize such a configuration. It says that the finite Hilbert inequality plus the scalar value of `Q/N` does not contain enough information to exclude it.

This also supplies a clean control for the research mandate's population separation. Real doubles are not being silently reclassified as off-line zeros: they are used only as the exact confluent endpoint that proves the limiting construction, and every finite member at `y>0` consists of genuinely simple non-real pairs.

## 5. What WI-136--WI-139 can and cannot bootstrap

The construction simultaneously satisfies all of the rigidity conditions exposed in the preceding Lamzouri findings.

For an isolated pair, WI-136's odd-vector charge is

\[
H_U=t(y)\to0.
\]

WI-137's full operator distance is

\[
\|\mathcal A_F-(P_U+P_V)\|_{HS}^2=8t(y)^2\to0.
\]

WI-138's negative index remains exactly one, but its unique negative eigenvalue is

\[
\lambda_-=-2t(y)\to0.
\]

Finally, WI-139's negative spectral subspace is already **equal** to `H` for the orthogonal pair, so its principal-angle term is zero before taking any limit.

Thus the four necessary near-sharpness conditions are mutually compatible. There is no hidden contradiction obtained merely by combining them more tightly at the one-pair level. Any proposed bootstrap that assigns a universal positive cost to the existence of an off-line pair through these norm quantities is killed by (1)--(13).

The many-pair construction shows that the obstruction is not repaired simply by counting more negative directions. One can have `k` negative eigenvalues, all required by inertia, while making their collective finite deficit arbitrarily small by letting each signed direction confluence and suppressing interactions between different pairs.

What remains live is precisely an **interaction theorem** that prevents this simultaneous cheap confluence for source-compatible zero configurations. Such a theorem could still exploit local crowding, a density-scale fraction of non-negligible pair interactions, a determinant/principal-minor constraint with a zeta-specific lower bound, or an independently evaluated arithmetic statistic. WI-140 rules out only a universal count-only charge available in the abstract finite proposition.

## 6. Relation to the critical-lattice screening obstruction

WI-006 gives a different obstruction inside the Alpöge--Furman critical Gabor compression: long blocks of simple off-line mirror pairs on the critical vertical lattice are operator-equivalent in the bulk to on-line doubles, for every admissible support-one window. That is a **dense screening** phenomenon. It preserves the full compressed operator asymptotically and survives every fixed spectral moment of the same compression.

The present confluence barrier is logically distinct. It is visible directly in Lamzouri's finite Proposition 2.1, does not require the critical sampling lattice, and is exact already for one isolated pair. Its many-block near-extremizers obtain cheapness by making pairs horizontally shallow and vertically dilute rather than by Poisson screening at density scale.

The distinction matters for interpretation. WI-006 by itself shows that support-one matrix information can fail to distinguish doubles from certain dense off-line blocks. WI-140 shows that even the conjugation-adapted Lamzouri tensor, which **does** retain exact negative index and the stronger `U/V/H` geometry, cannot have a uniform norm gap between a simple off-line pair and a real double. The negative sign survives; its magnitude does not.

Conversely, WI-140 is not a zeta-compatible replacement construction. Actual rescaled zeta ordinates have prescribed mean density and nontrivial pair-correlation information, whereas the proof of (20)--(25) deliberately sends block separations to infinity to suppress interactions. A zeta-specific density theorem can therefore still invalidate the dilute construction. That is exactly the kind of extra information a successful unconditional improvement now has to exploit.

## 7. Prior-art and novelty audit

The source-side Hilbert construction, vectors `f_z,g_z,h_z`, nested spaces, and finite inequality are Lamzouri's arXiv:2609.02882. The exact slack/operator form and inertia consequences used here are the persisted Mathia deductions WI-136--WI-139. The linear-algebra principles are classical: continuity of eigenvalues under norm perturbation, Sylvester's law of inertia, and the Riemann--Lebesgue lemma carry no novelty claim.

Bombieri's 2000 work on Weil's quadratic functional and Alpöge--Furman's 2026 matrix proof already establish the classical principle that off-critical pairs carry negative index in suitable Weil-form truncations. WI-138 explicitly reconnects Lamzouri's newer tensor to that inertia viewpoint. The present result does not claim a new inertia theorem; it identifies the **sharp stability obstruction** created by confluence inside Lamzouri's exact finite model.

A targeted audit of Lamzouri's current preprint, the Alpöge--Furman/Bombieri inertia discussion, the public `AxiomMath/ZetaZeros` formalization, and the current `weil_inertia` findings located the negative-index count and general warnings that negative eigenvalue magnitudes may collapse, but not the exact one-pair formulas (7)--(13), the universal fixed-`k` infimum (20), or the mixed construction (25) matching an arbitrary scalar `Q/N` while putting the whole complement off-line. Absence from that bounded audit is not evidence of priority, and no priority claim is made.

No new source anchor is needed in `SOURCES.md`: Lamzouri, Alpöge--Furman, Bombieri, and the relevant harmonic-analysis background are already recorded there.

## 8. Research implication

The defect-to-zero problem has become more precise. WI-138 removes the need to **detect** negative directions: there is exactly one per distinct off-line pair. WI-137/WI-139 control their magnitude and orientation by the finite slack. WI-140 shows why this still cannot close the complement abstractly: each negative direction has a genuine confluence channel through which its eigenvalue, odd residual, and complete slack vanish together as the corresponding pair approaches a real double.

Therefore a positive-density off-line exclusion must prevent many such channels from operating simultaneously under the actual zeta constraints. A useful next theorem should have the schematic form

\[
\text{zeta-compatible density/correlation constraint}
\quad+\quad
k\asymp N
\quad\Longrightarrow\quad
\Delta\ge cN
\]

for some explicit `c>0`, or else produce a zeta-compatible screened/confluent countermodel showing that even the source constraints leave `Delta=o(N)` possible. A theorem depending only on `k`, `n_-(A_F)`, `||A_F-D||_{HS}`, or the WI-139 principal-angle budget cannot succeed without additional hypotheses, because the exact confluence family already makes all of those norm charges arbitrarily small at fixed nonzero negative index.

This is a decisive negative result for the count-only Lamzouri/inertia bootstrap, but it leaves the research mandate's main escape route intact: exploit arithmetic or density-scale interaction information that the abstract finite Hilbert inequality deliberately forgets.