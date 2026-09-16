# RE-170 — Critical Mertens matching still permits compensated local Robin excursions

**Status:** `EXACT-DERIVED + MATCHED-GENERALIZED-SOURCE-CONTROL + CRITICAL-MERTENS-SHARPNESS + TWO-SHELL-COMPENSATION + KV-FIDELITY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-164, RE-167, RE-168, RE-169.

`RE-169` identifies a new global fidelity coordinate. If two sources agree below a selector cutoff, then the difference of their asymptotic Mertens normalizations is exactly the full future Robin-kernel weighted discrepancy. In particular, a compact post-selector relocation producing an order-one normalized Robin displacement changes the Mertens constant by order

\[
(\sqrt p\log p)^{-1}.
\tag{1}
\]

It follows that Mertens matching at the sharper scale

\[
|\Gamma(Q_p)-\gamma|
=o\!\left((\sqrt p\log p)^{-1}\right)
\tag{2}
\]

is necessary to exclude the one-shell controls of `RE-167`. The question left open by `RE-169` is whether (2) by itself is already a prefix-rigidity condition.

It is not.

Fix constants

\[
1<B_1<C_1<B_2<C_2,
\tag{3}
\]

and a fixed Korobov--Vinogradov exponent `b>0`. There are generalized-prime sources `Q_p` obtained from the ordinary primes by finite modifications inside the two disjoint bounded-multiplicative shells

\[
I_{1,p}=[B_1p,C_1p],
\qquad
I_{2,p}=[B_2p,C_2p],
\tag{4}
\]

such that, along all sufficiently large primes `p`, the following hold.

First, the source perturbation is asymptotically negligible even relative to the full KV envelope:

\[
\boxed{
\sup_{t\ge B_1p}
\frac{|\vartheta_{Q_p}(t)-\vartheta(t)|}
{t e^{-bV(t)}}
=o(1),
\qquad
V(t)=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}.
}
\tag{5}
\]

Second, after the first shell but before the second there is still an order-one Robin excursion. For every `U_p` with

\[
C_1p<U_p<B_2p,
\tag{6}
\]

one may arrange

\[
\boxed{
\left|
\mathcal A_{p,U_p}(Q_p)-\mathcal A_{p,U_p}(P)
\right|
\ge \delta_0
}
\tag{7}
\]

for one fixed `delta_0>0`, where

\[
\mathcal A_{p,U}(Q)
=
\frac{\sqrt p\log p}{Z_p}
\int_{p+p^\alpha}^{U}
\bigl(t-\vartheta_Q(t)\bigr)(-h'(t))\,dt,
\qquad
Z_p=2+o(1),
\tag{8}
\]

is the `RE-153`/`RE-169` normalized source coordinate.

Third, a reverse relocation in the second shell can repay that excursion to `o(1)`:

\[
\boxed{
\mathcal A_{p,U}(Q_p)-\mathcal A_{p,U}(P)
=o(1)
\qquad(U\ge C_2p).
}
\tag{9}
\]

Because the perturbation is then compactly supported, the exact `RE-169` sum rule gives

\[
\boxed{
\Gamma(Q_p)-\gamma
=o\!\left(\frac1{\sqrt p\log p}\right).
}
\tag{10}
\]

Thus **even critical-scale Mertens fidelity does not determine a selected finite prefix of the Robin coordinate**. It only imposes a conservation law on the full future history. To turn (2) into rigidity one also needs a tail or spatial-capacity statement preventing the compensating opposite-sign mass from appearing later. This is exactly why the KV-rigid-tail hypothesis in `RE-169` is load-bearing rather than technical.

The result sharpens the information boundary of `RE-169`: global normalization fidelity and spatial source fidelity are genuinely complementary resources. Neither subsumes the other.

## 1. The first shell creates an order-one excursion at vanishing KV cost

For a fixed proportional shell beginning at `T`, `RE-167` identifies the sharp local capacity

\[
\mathfrak L_b(p,T)
=
\sqrt p\log p\,
\frac{e^{-bV(T)}}{\log T}.
\tag{11}
\]

At every bounded-multiplicative scale `T=Bp`,

\[
\mathfrak L_b(p,Bp)
=p^{1/2-o(1)}\longrightarrow\infty.
\tag{12}
\]

Use the mass-balanced relocation from `RE-167` inside `I_{1,p}`: delete ordinary prime mass in an early subinterval and reinsert exactly the same logarithmic Chebyshev mass as generalized real labels in a later subinterval. The cumulative source discrepancy returns to zero at the upper edge of the shell.

Choose its amplitude parameter

\[
\lambda_{1,p}
\asymp
\mathfrak L_b(p,B_1p)^{-1}.
\tag{13}
\]

Then

\[
\lambda_{1,p}=p^{-1/2+o(1)}\to0,
\tag{14}
\]

while the sharpness estimate of `RE-167` gives a positive displacement

\[
D_{1,p}
:=
\mathcal A_{p,C_1p}(Q_p^{(1)})
-
\mathcal A_{p,C_1p}(P)
\tag{15}
\]

satisfying, after fixing the shell geometry and the implicit constant in (13),

\[
0<d_-\le D_{1,p}\le d_+<\infty
\tag{16}
\]

for fixed constants `d_-,d_+`.

The moved logarithmic mass is only of square-root size. Indeed the `RE-167` construction uses

\[
M_{1,p}
\asymp
\lambda_{1,p} B_1p\,e^{-bV(B_1p)}.
\tag{17}
\]

Combining (11) and (13) yields

\[
M_{1,p}\asymp\sqrt p
\tag{18}
\]

up to fixed shell and logarithmic factors tending to one. Since the full KV allowance at `B_1p` is

\[
B_1p\,e^{-bV(B_1p)}=p^{1-o(1)},
\tag{19}
\]

we have

\[
\frac{M_{1,p}}
{B_1p\,e^{-bV(B_1p)}}
=p^{-1/2+o(1)}=o(1).
\tag{20}
\]

After the first shell the Chebyshev discrepancy is exactly reset to zero, so for every `U_p` satisfying (6), the coordinate difference is still exactly `D_{1,p}`. Equation (16) proves (7) with any fixed `delta_0<d_-`.

## 2. Reverse packets in a later shell have an o(1) tuning mesh

The second shell has the same divergent capacity:

\[
\mathfrak L_b(p,B_2p)=p^{1/2-o(1)}\to\infty.
\tag{21}
\]

Reverse the `RE-167` geometry. Insert generalized labels in an early subinterval of `I_{2,p}` and delete equal logarithmic ordinary-prime mass in a later subinterval. During the gap between insertion and deletion,

\[
\vartheta_{Q_p}(t)-\vartheta(t)>0,
\tag{22}
\]

so the contribution to (8) has the opposite sign from `D_{1,p}`. Exact logarithmic mass balance again resets the Chebyshev discrepancy to zero at the end of the shell.

It remains to check that discreteness does not prevent matching the variable target `D_{1,p}`. The required mesh is already negligible.

Fix separated proportional subintervals

\[
[T,\rho T],
\qquad
[\sigma T,CT],
\qquad
1<\rho<\sigma<C,
\tag{23}
\]

with `T=B_2p`. A balanced elementary reverse packet can be formed using `O(\log T)` ordinary primes from the later interval and `O(\log T)` generalized labels from the earlier interval. The reason is elementary: changing the number of labels by one changes the total logarithmic mass by `\asymp\log T`, while moving `m` labels across a fixed proportional interval varies their total logarithmic mass through an interval of width `\asymp m`. Taking `m\asymp\log T` makes these ranges overlap; the continuous generalized-label positions then impose exact equality of total logarithmic mass. The ordinary PNT supplies far more than `O(\log T)` deletion candidates.

Such an elementary packet carries total Chebyshev mass

\[
m_p=O((\log p)^2).
\tag{24}
\]

Its normalized Robin contribution is bounded by

\[
\begin{aligned}
|\Delta_{\rm elem}\mathcal A_p|
&\le
\frac{\sqrt p\log p}{Z_p}
\,m_p\,
\bigl(h(T)-h(CT)\bigr)\\
&=
O\!\left(\frac{(\log p)^2}{\sqrt p}\right)
=o(1),
\end{aligned}
\tag{25}
\]

because `h(t)=(1+o(1))/(t\log t)` uniformly on fixed proportional shells.

Now concatenate disjoint elementary reverse packets. Every packet has the same sign in (8), every packet resets its own Chebyshev discrepancy, and the total available shell capacity tends to infinity by (21). Therefore the resulting negative displacement moves monotonically from zero past the bounded target interval `[d_-,d_+]` with mesh `o(1)`. Stop at the first packet for which its magnitude reaches `D_{1,p}`. Equation (25) gives

\[
D_{2,p}
=-D_{1,p}+o(1).
\tag{26}
\]

This proves (9).

The amount of mass needed in the second shell is again `O(\sqrt p)` because the target displacement is bounded. Hence its perturbation of the KV envelope is also `p^{-1/2+o(1)}`. Since the two shells are disjoint and each balanced packet returns its Chebyshev discrepancy to zero, (5) follows.

## 3. The final Mertens mismatch is below the critical scale

Let

\[
F_p(t)=\vartheta_{Q_p}(t)-\vartheta(t).
\tag{27}
\]

The complete two-shell construction is a finite modification and satisfies

\[
F_p(t)=0
\qquad(t>C_2p).
\tag{28}
\]

Therefore both Mertens constants exist, and the compact-support identity of `RE-169` applies. With the sign convention of (8), for every `U\ge C_2p`,

\[
\Gamma(Q_p)-\gamma
=
-
\frac{Z_p}{\sqrt p\log p}
\left(
\mathcal A_{p,U}(Q_p)-\mathcal A_{p,U}(P)
\right).
\tag{29}
\]

By (9),

\[
\Gamma(Q_p)-\gamma
=o\!\left((\sqrt p\log p)^{-1}\right),
\tag{30}
\]

which proves (10).

Notice the separation of scales. The intermediate prefix carries order-one normalized displacement, while the entire two-shell source has a Mertens mismatch smaller than the critical scale that detects a single uncompensated order-one relocation. Nothing contradicts `RE-169`: the second shell is precisely the future compensation whose existence its debt identity permits.

## 4. Why the KV-rigid tail cannot be dropped from RE-169

The compensation shell lies at `B_2p`, still only a fixed multiplicative distance from the CA frontier. At this height both the local shell capacity and the remote capacity are enormous:

\[
\mathfrak L_b(p,B_2p)=p^{1/2-o(1)},
\qquad
\mathfrak K_b(p,B_2p)=p^{1/2-o(1)}\,\operatorname{polylog}(p).
\tag{31}
\]

Thus there is ample room to repay an order-one debt while perturbing the pointwise KV envelope by only a vanishing relative amount.

By contrast, `RE-169` proves that if one waits until a height `U` for which

\[
\mathfrak K_b(p,U)=o(1),
\tag{32}
\]

then the entire remaining future has insufficient weighted capacity to repay any fixed debt. Equal or critically matched Mertens normalization then forces the finite-prefix ambiguity to vanish.

The two statements therefore form a sharp conceptual pair:

\[
\boxed{
\text{global Mertens matching}
+
\text{vanishing future KV capacity}
\Longrightarrow
\text{prefix rigidity},
}
\tag{33}
\]

while

\[
\boxed{
\text{global Mertens matching alone}
\not\Longrightarrow
\text{prefix rigidity}
}
\tag{34}
\]

within the generalized-source control class.

The missing ordinary-prime information is correspondingly more specific. A successful CA argument cannot merely append the correct asymptotic Mertens constant to a quantitative PNT estimate. It must connect the **selector-selected prefix** to where the compensating future Mertens debt is allowed to live, or supply another source-specific invariant that forbids the two-shell cancellation pattern.

## 5. Falsification checks and boundaries

**Does the construction merely change the PNT constant?** No at the relevant scale. Each shell uses only `O(\sqrt p)` moved logarithmic mass against a KV allowance `p^{1-o(1)}`. Equation (5) says the relative deterioration of the envelope tends to zero.

**Does the second shell corrupt the first-shell prefix?** No. The coordinate in (8) is truncated at `U`. For every `U` in the gap (6), the second shell has not started, while the first shell has already reset its Chebyshev discrepancy. The order-one value in (7) is therefore a genuine finite-prefix difference.

**Does approximate final cancellation suffice for the claimed Mertens precision?** Yes. The exact compact-support identity (29) multiplies the final normalized mismatch by `Z_p/(\sqrt p\log p)`. An `o(1)` final mismatch is exactly the little-`o` critical Mertens scale in (10).

**Could one demand exact equality `\Gamma(Q_p)=\gamma` instead?** The present result does not need that stronger interpolation claim. The `o(1)` packet mesh already reaches the fidelity scale that `RE-169` identified as sufficient once the remote tail is rigid. Establishing exact equality would add no new information to the current obstruction.

**Is this an ordinary-prime or CA counterexample?** No. `Q_p` is a generalized matched control. It shows only that the stated source summaries do not logically determine the selected Robin prefix. The ordinary-prime/CA problem remains to derive a selector-sensitive restriction unavailable to this control.

**Does this duplicate RE-167 or RE-168?** No. Their balanced shell relocations deliberately leave an order-one full Robin displacement and hence, by `RE-169`, a critical-size shift of the Mertens constant. Here two opposite-sign shells are coupled so that the **global** Mertens mismatch is little-`o` of that critical scale while the **intermediate** prefix still moves by order one.

A targeted prior-art audit found the classical Beurling-prime Mertens literature and small-perturbation constructions, including Olofsson's and Pollack's generalized Mertens theorems, but no statement coupling two spatially separated KV-faithful perturbations to preserve the critical Mertens normalization while producing a transient Robin-kernel excursion. Those works are contextual rather than load-bearing here: the proof uses only the exact internal sum rule of `RE-169` and the shell-capacity construction of `RE-167`.

## 6. Consequence for the selector-height frontier

The generalized-source hierarchy is now separated into three independent questions.

A local shell can carry order-one Robin displacement whenever its capacity is nonvanishing. The asymptotic Mertens constant constrains only the **total signed sum** of all such displacements. A quantitative tail estimate determines whether enough future capacity remains to repay an earlier displacement.

For the ordinary primes, all three pieces are present globally, but none yet couples the CA selector to the location of the compensation. Therefore the live `CLUE-clean-peak-selector-height-coupling` is not reduced to proving the ordinary Mertens theorem more accurately. The remaining task is genuinely selector-sensitive: show that a hypothetical self-tangent CA counterexample cannot sit before an admissible compensating future history of the type that the global identities alone permit.
