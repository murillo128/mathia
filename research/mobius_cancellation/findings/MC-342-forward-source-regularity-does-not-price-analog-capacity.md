# MC-342 — Forward source regularity does not price analog transcript capacity

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-340` shows that bounded-energy reciprocal-endpoint dephasing requires a transcript carrying a linear amount of joint source information, while `MC-341` shows that a low-dimensional Euclidean realization can hide that information only through exponentially fine metric separation. A natural next attempt is to replace the minimum-separation requirement by a more intrinsic **forward source-regularity** condition: bounded Lipschitz constant from the source cube, bounded source-gradient energy, or bounded average displacement under source-bit flips.

That replacement fails already on the exact even-rank reciprocal source law.

Let `R` be even. By the source-coordinate calculation used in `MC-340`, the reciprocal source vector can be identified with

\[
B=(B_1,\ldots,B_R)
\sim \operatorname{Unif}(S_R),
\qquad
S_R:=\{0,1\}^R\setminus\{\mathbf 1\},
\qquad
m:=|S_R|=2^R-1.
\tag{1}
\]

Define the scalar dyadic transcript

\[
T_R(B):=\sum_{i=1}^R 2^{-i}B_i.
\tag{2}
\]

Then all of the following hold simultaneously.

First, `T_R` is injective on `S_R`, so it carries the complete source entropy:

\[
\boxed{
I(B;T_R)=H(T_R)=H(B)=\log(2^R-1).
}
\tag{3}
\]

Second, with raw Hamming distance `d_H` on the source cube,

\[
\boxed{
\operatorname{Lip}(T_R:S_R\to\mathbf R)=\frac12,
\qquad
\operatorname{diam} T_R(S_R)=1-2^{1-R}<1.
}
\tag{4}
\]

Thus full linear source information is compatible with a uniformly bounded forward Lipschitz constant and uniformly bounded range.

Third, this remains true under every fixed positive-moment source-gradient budget. For `p>0`, define the punctured directed edge energy

\[
\mathcal D_p(T)
:=
\frac1m
\sum_{b\in S_R}
\sum_{\substack{1\le i\le R\\ b^{(i)}\in S_R}}
|T(b)-T(b^{(i)})|^p,
\tag{5}
\]

where `b^(i)` flips the `i`th source bit. Then

\[
\boxed{
\mathcal D_p(T_R)
=
\frac{m-1}{m}
\sum_{i=1}^R 2^{-ip}
=
\frac{m-1}{m}
\frac{1-2^{-pR}}{2^p-1}
<\frac1{2^p-1}.
}
\tag{6}
\]

In particular,

\[
\mathcal D_1(T_R)<1,
\qquad
\mathcal D_2(T_R)<\frac13
\tag{7}
\]

uniformly in `R`, even though `(3)` is asymptotically `R log 2` nats.

The cost is entirely **inverse conditioning**. The support is the dyadic grid with its top point removed, so

\[
\Delta_R
:=
\min_{u\ne v\in T_R(S_R)}|u-v|
=2^{-R},
\tag{8}
\]

and therefore

\[
\boxed{
\operatorname{spr}(T_R)
=
\frac{1-2^{1-R}}{2^{-R}}
=2^R-2.
}
\tag{9}
\]

This exactly saturates the sharp scalar packing lower bound `spr(T)>=K_T-1` from `MC-341`, because `K_T=2^R-1`.

There is an equally sharp source-sensitivity contrast. If one forgets displacement size and merely counts whether a valid source edge changes the transcript, then

\[
\boxed{
\mathcal I_0(T_R)
:=
\frac1m
\sum_{b\in S_R}
\sum_{\substack{i\\ b^{(i)}\in S_R}}
\mathbf 1_{\{T_R(b)\ne T_R(b^{(i)})\}}
=
R\frac{m-1}{m}
=R-o(1).
}
\tag{10}
\]

Every source coordinate remains combinatorially visible; its amplitude is merely pushed to an exponentially decreasing precision scale.

Consequently there can be no representation-independent implication of the form

\[
\text{bounded diameter + bounded forward Hamming Lipschitz constant
+ bounded fixed-}p\text{ edge energy}
\Longrightarrow I(B;T)=o(R).
\tag{11}
\]

The exact reciprocal source control `(2)` violates such an implication for every fixed `p>0`.

The live metric question after `MC-341` is therefore narrower than “find a canonical forward source energy”. **A useful analytic transcript theorem must charge inverse resolution/stability** — for example minimum distinguishable separation, co-Lipschitz distortion, finite precision, noise robustness, or another arithmetic condition that forbids information from being hidden in exponentially small source-dependent displacements. Forward regularity by itself does not couple analog geometry to source information.

No estimate for `M(x)` follows. This is a finite reciprocal-endpoint no-go theorem about which conditioning currencies can plausibly close the analog-transcript loophole.

## 1. The dyadic transcript carries the entire punctured source state

For even `R`, the reciprocal source characters form an invertible binary coordinate system on the full mode cube. Removing the principal mode removes exactly the all-`+1` source pattern; after converting signs to bits this is precisely the punctured law `(1)`.

Multiplying `(2)` by `2^R` gives

\[
2^R T_R(b)
=
\sum_{i=1}^R 2^{R-i}b_i,
\tag{12}
\]

which is the ordinary length-`R` binary integer represented by `b`. Hence distinct source vectors give distinct transcript values. Since `B` is uniform on `m` states, `(3)` follows immediately.

This is deliberately not presented as a sophisticated encoder. Its role is adversarial: any proposed general capacity theorem based only on forward smoothness must survive the simplest positional encoding before it can constrain an arithmetic transcript.

## 2. Forward Hamming regularity stays bounded

For any `b,c in S_R`, the triangle inequality gives

\[
|T_R(b)-T_R(c)|
\le
\sum_{i:b_i\ne c_i}2^{-i}
\le
\frac12 d_H(b,c).
\tag{13}
\]

The constant `1/2` is attained by two valid states differing only in the first bit, so the first identity in `(4)` is exact.

The minimum transcript value is `0`. The full-cube maximum `1-2^{-R}` corresponds to the excluded all-ones state. The largest surviving binary integer is `2^R-2`, hence

\[
\max T_R(S_R)
=\frac{2^R-2}{2^R}
=1-2^{1-R},
\tag{14}
\]

which proves the diameter statement in `(4)`.

Thus neither bounded range nor bounded one-sided Hamming-to-Euclidean Lipschitz constant detects the linear information content.

## 3. Every fixed positive-moment forward edge energy also stays bounded

Flipping source bit `i` changes `(2)` by exactly `2^{-i}` in absolute value. For each `i`, among the `m` states of `S_R` exactly one state — the all-ones vector with bit `i` changed to zero — has its `i`-flip equal to the deleted point. Therefore exactly `m-1` directed valid source states contribute at coordinate `i`.

Substituting into `(5)` gives

\[
\mathcal D_p(T_R)
=
\frac{m-1}{m}
\sum_{i=1}^R 2^{-ip},
\]

and summing the geometric series proves `(6)`.

This closes a tempting loophole left by the purely metric statement of `MC-341`. Replacing minimum separation by an `L^1`, `L^2`, or any fixed `L^p` aggregate of forward source displacements does not help. The transcript can encode successive source bits at geometrically decreasing amplitudes, keeping every such aggregate bounded while preserving exact injectivity.

The limit `p downarrow 0` is intentionally different. Equation `(10)` counts changed edges without discounting small amplitudes and is asymptotically linear. The distinction identifies the missing resource precisely: **whether arbitrarily tiny nonzero displacements count as fully distinguishable information**.

## 4. The exponential spread barrier of MC-341 is sharp even under strong forward regularity

Because `(12)` takes consecutive dyadic-grid values except for the final point, the minimum separation is exactly `2^{-R}`. Combining this with `(14)` proves `(9)`.

For a scalar transcript with `K` support points, `MC-341` proves the elementary packing inequality

\[
\operatorname{spr}(T)\ge K-1.
\tag{15}
\]

Here `K=m=2^R-1`, and `(9)` gives equality:

\[
\operatorname{spr}(T_R)=m-1.
\tag{16}
\]

So the exponential precision cost exposed by `MC-341` is not an artifact of a crude volume argument or a pathological large-range realization. It is attained by a bounded-range, uniformly Lipschitz scalar encoding whose fixed-`p` source-gradient energies are all bounded.

Equivalently, the inverse map is necessarily ill-conditioned. Since two valid states differing only in the last bit have Hamming distance one but transcript distance `2^{-R}`, any inverse-Lipschitz constant is at least `2^R`. The source information is stored in inverse precision, not in forward amplitude.

## 5. Finite precision recovers the information barrier immediately

The same control makes the operational role of precision explicit. Let `Q_k(T_R)` retain only the first `k` binary fractional digits, with `k<=R`. Its support has at most `2^k` states, so

\[
I(B;Q_k(T_R))
=H(Q_k(T_R))
\le k\log2.
\tag{17}
\]

Suppose a coefficient observation family `Y` is downstream of `Q_k(T_R)` and is required to meet the bounded-energy dephasing regime of `MC-340`. If `MC-340` forces

\[
I(B;Y)\ge L_R,
\tag{18}
\]

then data processing and `(17)` give

\[
\boxed{
k\ge\frac{L_R}{\log2}.}
\tag{19}
\]

For fixed nontrivial dephasing at bounded coefficient energy, `L_R=Theta(R)`, so the required scalar precision is exponentially fine:

\[
2^{-k}\le e^{-L_R}.
\tag{20}
\]

At the exact unit-energy matched-filter floor, `MC-340` requires full source recovery. Since

\[
\log_2(2^R-1)>R-1,
\]

integer `k` must satisfy `k>=R`. The dyadic control therefore meets the endpoint capacity requirement exactly by exposing all `R` binary digits.

This does not strengthen the information lower bound of `MC-340`; it shows that the precision alternative in `MC-341` is quantitatively real and essentially sharp.

## 6. Prior art and novelty boundary

The construction `(2)` is ordinary finite binary positional encoding. No novelty is claimed for representing a finite binary word by a dyadic real number, for Hamming-cube coordinate differences, or for the observation that exact decoding of such an encoding requires access to its least significant digits.

Ryan O'Donnell, *Analysis of Boolean Functions* (Cambridge University Press, 2014; corrected public version arXiv:2105.10386), is a standard reference for Hamming-cube coordinate flips, influences and source sensitivity. Classical influence counts whether a bit flip changes a Boolean output; the amplitude-weighted quantities `(5)` are defined here only as candidate forward conditioning currencies for this endpoint problem.

Nathan Linial, Eran London and Yuri Rabinovich, *The geometry of graphs and some of its algorithmic applications*, Combinatorica **15** (1995), 215–245, DOI `10.1007/BF01200757`, treats metric embeddings through **distortion**, i.e. two-sided control of source and image distances. That established viewpoint is the correct prior-art boundary for the lesson here: one-sided Lipschitz control is not a faithful-capacity notion because inverse contraction may be arbitrarily severe.

A targeted audit on 17 September 2026 found no basis for a novelty claim about binary positional coding, Boolean-cube influences, Lipschitz maps, or metric distortion. The durable Mathia delta is the exact specialization to the punctured reciprocal source law and its composition with `MC-340`--`MC-341`: the explicit control `(2)` saturates the scalar spread lower bound while keeping diameter, forward Lipschitz constant and every fixed positive-moment edge energy uniformly bounded. This rules out an entire class of prospective generic strengthenings of the current endpoint obstruction.

## Boundaries and falsification tests

- **Even rank is enough for the no-go.** The construction uses the especially clean even-`R` source law where the punctured source vector is uniform on all binary words except one. A generic implication such as `(11)` is already false on this infinite subsequence; no odd-rank analogue is needed for that conclusion.
- **The encoder is intentionally artificial.** Nothing here says a genuine Möbius-derived analytic transcript uses geometrically weighted binary digits. The point is that forward regularity alone cannot exclude such behavior; arithmetic naturalness must supply an additional hypothesis.
- **Combinatorial influence is not small.** Equation `(10)` is linear. The result does not contradict Boolean-function theorems in which influence counts whether an output changes rather than weighting the change by an arbitrarily small amplitude.
- **No forward-energy lower bound follows from information alone.** The example simultaneously has `H(T_R)=Theta(R)` and `D_p(T_R)=O_p(1)` for every fixed `p>0`.
- **Inverse conditioning remains expensive.** Minimum separation, inverse Lipschitz constant and finite precision all detect the hidden cost and recover the exponential barrier of `MC-341`.
- **Arbitrary re-encoding remains a live issue.** A candidate arithmetic norm or metric matters only if it is canonically tied to the analytic construction; one cannot reject a representation merely because an externally chosen chart gives bad inverse conditioning.
- **This is not an arithmetic estimate.** It proves no cancellation for `M(x)`, no zero-free region and no statement about actual Möbius coefficient families.

## Consequence for the research line

The analog-transcript frontier is now sharper. `MC-340` forces linear source information; `MC-341` prices that information through metric spread once a meaningful resolution scale exists; the present control shows that **forward** source smoothness cannot manufacture that scale. Even a bounded-range scalar transcript can be uniformly Hamming-Lipschitz and have bounded `L^p` source-gradient energy for every fixed `p>0` while carrying the complete reciprocal source state.

The next admissible arithmetic mechanism must therefore do one of two things: provide a canonical inverse-conditioning/noise/precision theorem for the actual Möbius-derived transcript, or exploit additional arithmetic structure that forbids hierarchical sub-resolution coding of source phases. Merely proving bounded forward coefficient sensitivity, bounded source-gradient energy or bounded analog range cannot close the endpoint loophole.