# MC-100 — Tiny bias forces an almost-square Hamming interior spike

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let the source-forced Hamming deformation from `MC-092`--`MC-099` be

\[
\mathcal Q_N(t)
=\sum_{m,n\le N}
\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right)
=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad 0\le t\le1.
\tag{1}
\]

`MC-097` proves that the complete degree-two shell has the positive asymptotic

\[
C_{2,N}\sim c_2\frac{N^2}{(\log N)^2},
\qquad
c_2
=\frac{15}{\pi^2}\left(\gamma+\gamma_1-\frac12\right)>0.
\tag{2}
\]

The higher shells can already be bounded directly at sufficiently small bias without estimating any individual shell. Put

\[
\tau:=\frac{c_2}{2},
\qquad
t_N:=\frac{\tau}{(\log N)^2}.
\tag{3}
\]

Then, for all sufficiently large `N`,

\[
\boxed{
\mathcal Q_N(t_N)
\ge
c_*\frac{N^2}{(\log N)^6}
}
\tag{4}
\]

for an absolute constant `c_*>0`; one may take `c_*=c_2^3/32` after increasing the lower threshold for `N`.

Thus the deformation has an explicit deterministic **almost-square interior spike** already at a bias tending to zero like `(log N)^(-2)`. This is not a random-model fluctuation and does not use a zero-free region: it follows from the source pair sum, the positive degree-two main term, and the elementary bound `|z|<=1/2`.

The spike closes the uniform-interior regularization branch left conditional in `MC-093` and `MC-094`. For every fixed nondegenerate interval

\[
I=[a,b]\subset[0,1],
\qquad a<b,
\tag{5}
\]

one has

\[
\boxed{
\sup_{t\in I}|\mathcal Q_N(t)|
\ge N^{2-o_I(1)}.
}
\tag{6}
\]

In particular, there is no fixed `gamma<2` for which the source deformation can satisfy

\[
\sup_{t\in I}|\mathcal Q_N(t)|=O(N^\gamma)
\tag{7}
\]

on any fixed positive-length bias interval. A fixed interval separated from both `0` and `1` is not an escape: the sublogarithmic source degree from `MC-093` extrapolates a bound on that interval back to the explicit point `t_N` with only `N^{o(1)}` loss.

The same obstruction reaches the deterministic Chebyshev bias family of `MC-094`. For every fixed `0<\eta<1` and every fixed `1\le p<\infty`, if `A_{p,N}(\eta)` is the normalized sampled `ell_p` mean defined there over the `K_N+1` Chebyshev nodes in `(0,1-\eta)`, then

\[
\boxed{
A_{p,N}(\eta)\ge N^{2-o_{\eta,p}(1)}.
}
\tag{8}
\]

Hence neither continuum-uniform interior control nor the stable sublogarithmic Chebyshev sample family can carry a strict power improvement for this exact Hamming deformation. Any surviving use of the deformation must exploit a **signed relation between large values**, a derivative/recurrence with independently controlled cancellation, an `N`-dependent shrinking geometry whose stability is separately audited, or a different source coupling. Treating biased points as uniformly easier amplitudes is now ruled out at polynomial scale.

No improved estimate for `M(x)` is claimed.

## 1. The degree-three-and-higher tail is cubically small at small bias

Write

\[
\mathcal R_{\ge3,N}(t)
:=\sum_{k\ge3}(-t)^kC_{k,N}.
\tag{9}
\]

It is important not to estimate the `C_{k,N}` separately. Return instead to the exact pair representation in `(1)`. The terms contributing to `(9)` are exactly the ordered square-free pairs with

\[
d_\triangle(m,n)\ge3.
\]

For `0\le t\le1`, every such term has absolute value at most

\[
\mu(m)^2\mu(n)^2
 t^{d_\triangle(m,n)}
\left|z\!\left(\frac{N^2}{mn}\right)\right|
\le \frac12t^3.
\tag{10}
\]

There are at most `N^2` ordered pairs. Therefore, without any shellwise triangle inequality beyond the original source terms,

\[
\boxed{
|\mathcal R_{\ge3,N}(t)|
\le \frac12N^2t^3
\qquad(0\le t\le1).
}
\tag{11}
\]

This estimate is deliberately local in the deformation parameter. It does not contradict `MC-098`, which shows that the higher-degree shells have almost-square aggregate signed mass at the endpoint `t=1`. Equation `(11)` says only that multiplying every degree `k>=3` by `t^k` suppresses their **pair-level source contribution** cubically when `t` is small.

## 2. Degree two dominates at the explicit logarithmic bias

Split `(1)` as

\[
\mathcal Q_N(t)
=C_{0,N}-tC_{1,N}+t^2C_{2,N}+\mathcal R_{\ge3,N}(t).
\tag{12}
\]

`MC-098` records the elementary low-shell bounds

\[
|C_{0,N}|\le \frac N2,
\qquad
C_{1,N}=O(N\log\log N).
\tag{13}
\]

From `(2)`, for all sufficiently large `N`,

\[
C_{2,N}\ge\frac{c_2}{2}\frac{N^2}{(\log N)^2}.
\tag{14}
\]

At `t=t_N` from `(3)`, equations `(11)` and `(14)` give

\[
t_N^2 C_{2,N}
\ge
\frac{c_2^3}{8}\frac{N^2}{(\log N)^6},
\tag{15}
\]

while

\[
|\mathcal R_{\ge3,N}(t_N)|
\le
\frac{c_2^3}{16}\frac{N^2}{(\log N)^6}.
\tag{16}
\]

The two low-shell contributions satisfy

\[
|C_{0,N}|+t_N|C_{1,N}|
=O\!\left(N+\frac{N\log\log N}{(\log N)^2}\right)
=o\!\left(\frac{N^2}{(\log N)^6}\right).
\tag{17}
\]

Combining `(12)`--`(17)` and absorbing the `o(1)` loss yields `(4)`, for example with `c_*=c_2^3/32`.

The scale `(log N)^(-2)` is not asserted to be optimal. It is simply the first natural scale at which the positive shell `t^2 C_{2,N}` and the universal pair-level tail bound `N^2t^3` are separated by a fixed constant while the low shells are negligible. More generally, every fixed `0<\kappa<2c_2` gives a positive lower bound of the same `N^2/(log N)^6` order at `t=\kappa/(log N)^2` after choosing the constants with the asymptotic `(2)` in view.

## 3. Every fixed positive-length bias interval inherits almost-square amplitude

`MC-093` proves

\[
D_N:=\deg \mathcal Q_N
=O\!\left(\frac{\log N}{\log\log N}\right).
\tag{18}
\]

Fix an interval `I=[a,b]` with `0<=a<b<=1`. Affinely map `I` to `[-1,1]`. The point `t_N` maps to a real point `x_N` that remains in a fixed compact subset of the real line depending only on `I`: if `a=0`, eventually `t_N` lies inside `I`; if `a>0`, then `x_N` approaches the fixed exterior point corresponding to `t=0`.

The classical one-interval Chebyshev extremal inequality used in `MC-093` therefore gives

\[
|\mathcal Q_N(t_N)|
\le
\sup_{t\in I}|\mathcal Q_N(t)|
\exp(O_I(D_N)).
\tag{19}
\]

By `(18)`,

\[
\exp(O_I(D_N))=N^{o_I(1)}.
\tag{20}
\]

Insert the lower bound `(4)` into `(19)`:

\[
\sup_{t\in I}|\mathcal Q_N(t)|
\gg
\frac{N^2}{(\log N)^6}N^{-o_I(1)}
=N^{2-o_I(1)},
\tag{21}
\]

which proves `(6)` and rules out `(7)` for every fixed `gamma<2`.

This strengthens the interpretation of `MC-093`. That finding showed that a strict power bound on a fixed interior interval would transfer to the Möbius endpoint. The present source-level lower bound shows that **the required strict-power interior premise is itself false**, not merely difficult, for every fixed positive-length interval of the exact deformation.

## 4. The Chebyshev sample family also contains almost-square mass

Fix `0<eta<1` and let `K_N`, the nodes `t_{j,N}`, and the sampled mean `A_{p,N}(eta)` be exactly those of `MC-094`. For sufficiently large `N`, the point `t_N` from `(3)` lies in `[0,1-eta]`.

Exact interpolation at the `K_N+1` Chebyshev roots and the Lebesgue constant bound from `MC-094` imply, throughout that interval,

\[
|\mathcal Q_N(t)|
\le
\Lambda_{K_N}
\max_j|\mathcal Q_N(t_{j,N})|,
\qquad
\Lambda_{K_N}=O(\log(K_N+1)).
\tag{22}
\]

Evaluating at `t_N` and using `(4)`,

\[
\max_j|\mathcal Q_N(t_{j,N})|
\gg
\frac{N^2}{(\log N)^6\Lambda_{K_N}}.
\tag{23}
\]

For fixed `p`, the normalized sampled mean satisfies

\[
A_{p,N}(\eta)
\ge
\frac{\max_j|\mathcal Q_N(t_{j,N})|}{(K_N+1)^{1/p}}.
\tag{24}
\]

Since `K_N=N^{o(1)}` and `Lambda_{K_N}=N^{o(1)}`, equations `(23)`--`(24)` prove `(8)`.

Thus the discrete reconstruction result in `MC-094` is not merely a conditional endpoint-transfer theorem. For the exact source it now calibrates a negative fact: **any stable Chebyshev-node family large enough to reconstruct the deformation already contains almost-square amplitude before endpoint recovery.** No strict power gain can be obtained by proving that all those biased values, or their fixed-`p` mean, are small.

## 5. Endpoint contrast and the surviving signed problem

`MC-098`, using only the classical unconditional Korobov--Vinogradov Mertens estimate together with the Huxley--Watt source identity, proves

\[
\mathcal Q_N(1)
=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\qquad\text{for every fixed }A>0.
\tag{25}
\]

Taking `A>6` and comparing `(25)` with `(4)` gives

\[
\mathcal Q_N(1)
=o(\mathcal Q_N(t_N)).
\tag{26}
\]

So the Hamming path does not regularize the source monotonically as the prime signs move away from the all-minus Möbius endpoint. At the explicit tiny bias `t_N`, the deformed source is much larger than the hard endpoint at the level of logarithmic order, even though both remain on the same fixed polynomial power `N^2`.

This is compatible with the large curvature sign reversal of `MC-099`: the path first develops a source-forced positive low-degree contribution and later must cancel it through signed higher-degree interactions. The new point is amplitude-level rather than curvature-level. It rules out a route based on uniformly small biased values, while leaving open a route that can exploit the **relations among those large values** or the signed cross-degree cancellation itself.

The theorem does not exclude `N`-dependent shrinking intervals or specially chosen unstable sample geometries. But any such proposal must keep its extrapolation/interpolation condition number explicit; it cannot invoke the fixed-geometry `N^{o(1)}` stability of `MC-093`--`MC-094` while avoiding the lower bound above.

## 6. Prior art and novelty boundary

The external mechanisms used in the proof are classical. The Huxley--Watt finite Mertens identity and sawtooth source are recorded as `MC-S24`; the Chebyshev extremal/interpolation machinery is already audited in `MC-093`--`MC-094`. The degree-two asymptotic `(2)` is the canonical line result `MC-097`, while the low-shell bounds and endpoint comparison are recorded in `MC-098`.

Biased random multiplicative functions are themselves established prior art. Marco Aymone and Vladas Sidoravicius, *Partial sums of biased random multiplicative functions*, Journal of Number Theory 172 (2017), 343--382, DOI `10.1016/j.jnt.2016.08.020`, study square-free-supported random multiplicative functions with independent biased prime signs and the relation of their partial sums to Möbius/RH-scale cancellation. That literature confirms that biasing independent prime signs is not a new framework. It does not, from the targeted audit performed here, supply the exact deterministic Huxley--Watt bilinear lower bound `(4)` or the fixed-interval/sample obstruction `(6)`--`(8)`.

A targeted search for Huxley--Watt/Mertens identities together with Hamming/noise deformations and for Möbius Hamming polynomials did not identify a standard theorem matching `(4)`. Search absence is not evidence of novelty, and **no novelty claim is made**. The durable line-specific contribution is the exact composition of the already-established positive degree-two source term with the direct cubic pair-level tail bound, followed by the classical low-degree polynomial stability already present in the line.

## 7. Boundaries and falsification tests

- The lower bound concerns the exact source deformation `(1)`. Altering the sawtooth kernel, truncating the source, reweighting degrees, or changing the prime-sign coupling may remove the degree-two main term or the cubic tail estimate and must be re-audited from scratch.
- Equation `(4)` is a lower bound at one explicit `N`-dependent bias, not a description of the full profile or the location of its maximum.
- Equations `(6)` and `(8)` use the sublogarithmic degree and stable fixed-geometry interpolation. They do not rule out a shrinking interval or moving node geometry whose reconstruction cost is allowed to grow at a polynomial rate; such a cost must be charged against any claimed Mertens gain.
- The biased-random interpretation of `MC-093` is not used to transfer probability statements to Möbius. The proof of `(4)` is deterministic after the exact source polynomial has been defined.
- The result does not strengthen the unconditional bound for `M(x)`. The small endpoint in `(25)` is imported only as a comparison after the spike has already been proved.
- A signed recurrence may remain viable even if every fixed stable sample family contains large values. The missing theorem is still an independently controlled relation that converts the forced cross-degree cancellation into a strict, iterable Mertens contraction.

## Consequence for the research line

`MC-093`--`MC-094` showed that fixed-geometry regularization and a sublogarithmic stable sample family would not spend a polynomial gain when reconstructing the Möbius endpoint. `MC-095`--`MC-099` then showed that radial positive norms discard real cancellation and that the source Hamming path has large signed curvature reversal.

`MC-100` closes the remaining amplitude loophole. **The source is already almost-square at an explicit tiny interior bias, and low polynomial degree propagates that power obstruction to every fixed positive-length bias interval and to the stable Chebyshev sample family.** The deformation cannot be made power-easier by moving to a fixed interior bias region and later interpolating back.

The live Hamming route is therefore narrower: it must use signed, scale-coherent relations among large biased values or derivatives, with an independently available estimate that survives the full `MC-027` iteration ledger. Uniform smallness of biased amplitudes is no longer a plausible source of the gain.