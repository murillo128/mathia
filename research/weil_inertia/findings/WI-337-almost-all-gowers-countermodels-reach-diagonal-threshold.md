# WI-337 — almost-all Gowers countermodels reach the diagonal-energy threshold

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED`.

WI-336 leaves an asymptotically one-order strip between two statements about **all-interval** normalized Gowers smallness: matched-energy Rademacher countermodels are simultaneously small on every interval when

\[
R_s(K,N):=\frac{2^s\log\log N}{\log K}\le 1-\eta,
\]

whereas the diagonal-cube energy floor makes ordinary normalized `U^s=o(1)` impossible for every comparable-energy source once `R_s\ge2+\eta`. That gap is real for an all-start theorem, but it is not a gap for an **almost-all interval** theorem of the type supplied by the 2026 Matomäki--Radziwiłł--Shao--Tao--Teräväinen result.

For density-one interval information, the same random-sign obstruction reaches every fixed margin below the deterministic diagonal threshold `R_s=2`. More precisely, fix

\[
0<\kappa<1,\qquad K=N^{\kappa+o(1)},
\]

let `u_n` be any deterministic unit-modulus carrier, and for each start `x` choose any deterministic interval

\[
I_x=[x+1,x+L_x],\qquad K\le L_x\le2K.
\]

For every fixed `0<\eta<2`, there is a real sequence

\[
b_n=\sqrt{\log N}\,\varepsilon_n,
\qquad \varepsilon_n\in\{-1,+1\},
\]

and a set of good starts `G_N` with `|G_N|=N-o(N)` such that, uniformly for every `x\in G_N` and every integer `s\ge2` satisfying

\[
\boxed{
2^s\log\log N\le(2-\eta)\log K,
}
\tag{1}
\]

one has

\[
\boxed{
\|b\|_{U^s(I_x)}
\le
(\log N)^{-\eta/(4(2-\eta))+o(1)}
=o(1),
}
\tag{2}
\]

while those same good starts still carry asymptotically the entire diagonal sliding variance:

\[
\boxed{
\sum_{x\in G_N}
\left|\sum_{n\in I_x}b_nu_n\right|^2
=
\left(\sum_x L_x+o(NK)\right)\log N.
}
\tag{3}
\]

Thus **almost-all local Gowers smallness through every order below `R_s=2-\eta` does not force any saving in the bow-style quadratic mean**. Coupled with WI-336, which proves that comparable-energy sources cannot have ordinary normalized `U^s=o(1)` once `R_s\ge2+\eta`, this pins the density-one black-box transition to the diagonal threshold `R_s=2` up to arbitrary fixed margins. The remaining one-order strip in WI-336 is specifically an all-start/all-interval question.

This matters for the accepted distinguished-bow clue. The 2026 higher-uniformity theorem gives Gowers smallness only for **almost all** intervals and only for fixed `s`. Even a hypothetical growing-order strengthening of that theorem cannot close the WI-195 bow `L^2` gate merely by retaining the same output `U^s=o(1)` on a density-one set: below the diagonal threshold the present countermodel preserves the full variance on the good set itself, and above the threshold ordinary norm smallness is incompatible with the required source energy. Any successful continuation must therefore use source-specific signed covariance, an all-start input, or a genuinely renormalized statistic that removes the diagonal degeneracies rather than asking only for higher ordinary Gowers order.

## 1. Density-one Gowers smallness reaches every fixed margin below `R_s=2`

Use the interval normalization from WI-335--WI-336,

\[
\|f\|_{U^s(I)}
:=
\frac{\|f1_I\|_{U^s(\mathbb Z)}}
     {\|1_I\|_{U^s(\mathbb Z)}}.
\]

Let the `\varepsilon_n` initially be independent Rademacher signs and set

\[
F_{s,x}
:=
\frac{\|\varepsilon1_{I_x}\|_{U^s(\mathbb Z)}^{2^s}}
     {\|1_{I_x}\|_{U^s(\mathbb Z)}^{2^s}}.
\tag{4}
\]

The elementary cube count already proved in WI-335 is uniform for `K\le L_x\le2K` and for `s=O(\log\log N)`: for an absolute `C`, after harmless enlargement of `C`,

\[
\boxed{
\mathbb EF_{s,x}\le\frac{(Cs)^s}{K}.
}
\tag{5}
\]

Fix `\eta\in(0,2)` and put

\[
\delta:=\frac\eta4.
\tag{6}
\]

Call a start `x` bad if, for at least one order satisfying (1),

\[
F_{s,x}>K^{-1+\delta}.
\tag{7}
\]

Every retained order satisfies `s=O(\log\log N)`, so

\[
(Cs)^s=K^{o(1)}.
\tag{8}
\]

Markov's inequality, followed by a union bound over only `O(\log\log N)` possible orders, gives

\[
\mathbb P(x\text{ is bad})
\le K^{-\delta+o(1)}.
\tag{9}
\]

If `B` denotes the number of bad starts among `N` consecutive starts, then

\[
\mathbb EB\le NK^{-\delta+o(1)}.
\tag{10}
\]

A second application of Markov therefore gives, with probability `1-o(1)`,

\[
\boxed{
B\le NK^{-\delta/2}=o(N).
}
\tag{11}
\]

For every good start and every retained order,

\[
\begin{aligned}
\log\|b\|_{U^s(I_x)}
&=\frac12\log\log N+\frac{1}{2^s}\log F_{s,x}\\
&\le\frac12\log\log N
-\frac{(1-\delta)\log K}{2^s}.
\end{aligned}
\tag{12}
\]

Condition (1) implies

\[
\frac{\log K}{2^s}
\ge\frac{\log\log N}{2-\eta},
\]

and hence, using `\delta=\eta/4`,

\[
\log\|b\|_{U^s(I_x)}
\le
\left(
\frac12-\frac{1-\eta/4}{2-\eta}
\right)\log\log N
=
-\frac{\eta}{4(2-\eta)}\log\log N.
\tag{13}
\]

Integer floors and the `K=N^{\kappa+o(1)}` normalization contribute only an `o(\log\log N)` term, yielding (2). The key difference from WI-335--WI-336 is that no bounded-difference concentration is needed: density-one control follows from the first moment (5) alone, and that is strong enough to reach the full fixed-margin range below `R_s=2`.

## 2. Removing the exceptional starts does not remove the diagonal variance

It is not enough to know that only `o(N)` intervals are bad: in principle those intervals could carry most of the sliding square. The same Rademacher realization can be chosen so that this does not happen.

Define

\[
S_x:=\sum_{n\in I_x}\varepsilon_nu_n,
\qquad
V:=\sum_x|S_x|^2,
\qquad
D_N:=\sum_xL_x.
\tag{14}
\]

Since `|u_n|=1` and the signs are independent,

\[
\mathbb EV=D_N,
\qquad
NK\le D_N\le2NK.
\tag{15}
\]

Also

\[
\mathbb E|S_x|^4\le3L_x^2=O(K^2).
\tag{16}
\]

Two sums `S_x,S_y` are independent whenever their intervals are disjoint. Since every interval has length at most `2K`, only `O(NK)` pairs of starts can overlap. Cauchy--Schwarz and (16) then give

\[
\operatorname{Var}(V)=O(NK^3).
\tag{17}
\]

Because `K=o(N)`, Chebyshev implies

\[
V=D_N+o(NK)
\tag{18}
\]

with probability `1-o(1)`.

To control the contribution from the random bad set, put

\[
W:=\sum_x|S_x|^4.
\tag{19}
\]

Equation (16) gives `\mathbb EW=O(NK^2)`. By Markov, with probability `1-o(1)`,

\[
W\le NK^2K^{\delta/4}.
\tag{20}
\]

Intersect the high-probability events (11), (18), and (20). On their intersection, Cauchy--Schwarz gives

\[
\begin{aligned}
\sum_{x\ \mathrm{bad}}|S_x|^2
&\le B^{1/2}W^{1/2}\\
&\le
\left(NK^{-\delta/2}\right)^{1/2}
\left(NK^2K^{\delta/4}\right)^{1/2}\\
&=NK\,K^{-\delta/8}
=o(NK).
\end{aligned}
\tag{21}
\]

Therefore

\[
\sum_{x\ \mathrm{good}}|S_x|^2
=D_N+o(NK).
\tag{22}
\]

At least one Rademacher realization lies in this intersection. Fix it and multiply by `\sqrt{\log N}`. Equations (2) and (22) then hold simultaneously, and (22) becomes exactly (3). In particular the exceptional `o(N)` starts cannot be charged with the missing covariance: the density-one set on which all the retained Gowers norms are small still carries `(1+o(1))` of the raw diagonal-scale energy.

## 3. The density-one threshold matches the deterministic diagonal floor

WI-336 proves for every sequence supported on an interval `I` of length `L` with energy `E=\sum_I|f|^2` that

\[
\|f\|_{U^s(I)}
\ge
\sqrt{\frac{E}{2L}}\,L^{-1/2^s}.
\tag{23}
\]

At the bow-relevant energy `E\gg L\log N`, this makes `U^s=o(1)` impossible whenever

\[
\frac{2^s\log\log N}{\log L}\ge2+\eta.
\tag{24}
\]

The present construction gives the converse information-theoretic obstruction, up to an arbitrary fixed margin, for density-one interval data:

\[
\begin{array}{ll}
R_s\le2-\eta:
&\text{density-one simultaneous norm smallness can coexist with full sliding variance},\\[2mm]
R_s\ge2+\eta:
&\text{comparable-energy ordinary norm smallness is deterministically impossible}.
\end{array}
\tag{25}
\]

No assertion is made at the exact transition `R_s=2`, and (25) does not say that Gowers information is sufficient there. It says that, for an **almost-all** black-box theorem, there is no open interval of Gowers orders left between the generic countermodel and the diagonal-energy obstruction. The apparent `1<R_s<2` escape in WI-336 comes from demanding one realization be small on every interval simultaneously.

## 4. Consequence for the arithmetic source interface

Matomäki, Radziwiłł, Shao, Tao and Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. 244 (2026), prove that the relevant short-interval Gowers norms of `\Lambda-\Lambda^\sharp` are asymptotically small for **any fixed order** `s` on almost all intervals in their stated ranges. Their theorem does not make `s=s(X)` grow, and the present finding does not claim that such a strengthening is available.

The point is conditional on the **interface**, not on a new theorem about primes: even granting a hypothetical growing-order version with density-one normalized `U^s=o(1)`, such information alone cannot imply the WI-195 diagonal-scale variance saving. Below `R_s=2`, the explicit matched-energy model satisfies the same form of density-one norm output while retaining the entire variance on those good starts. Above `R_s=2`, WI-336 says that the source's own quadratic energy obstructs ordinary norm smallness before arithmetic enters.

This separates the 2026 almost-all theorem sharply from the 2023 Matomäki--Shao--Tao--Teräväinen **all-interval** theorem used in WI-331. In the low-bow regime `0<\vartheta<3/16`, all-start arithmetic control is genuinely stronger and the WI-336 critical strip remains logically available to a future all-interval theorem or to a new critical statistic. The present result closes only the idea that the almost-all quantifier can be rescued by moving to higher and higher ordinary Gowers order.

None of this proves that the actual `\Lambda-\Lambda^\sharp` covariance is diagonal-sized, supplies the required negative off-diagonal sign, excludes an off-critical zero, or improves a zeta-zero proportion. It is a decisive information-interface obstruction inside the defect-elimination program.

## 5. Prior-art and novelty audit

The arithmetic theorem surface being tested is established prior art. The 2026 Inventiones paper cited above explicitly states almost-all short-interval Gowers smallness for each fixed `s`; the 2023 all-interval paper used in WI-331 gives the corresponding stronger start quantifier at the longer `X^{5/8+\varepsilon}` scale. Neither source asserts growing-order uniformity.

Random functions as small-Gowers models are classical, and WI-334--WI-336 already record that background. A fresh bounded search around random Boolean/Rademacher functions, growing-order Gowers norms, degenerate-cube energy floors, and almost-all interval concentration located the standard random-function heuristic and the fixed-order arithmetic theorems, but no source matching the specific density-one threshold statement (1)--(3). **No priority claim is made.** The Mathia delta is the exact first-moment observation that the WI-335 cube expectation reaches `R_s<2` once the requirement is weakened from every interval to density one, together with the fourth-moment argument showing that deleting those exceptional starts still leaves the full sliding variance.

## 6. Boundary conditions and decisive audit tests

This finding must be narrowed if any of the following fails: the WI-335 expectation bound (5) is not uniform over the retained `s=O(\log\log N)` range; the union in (9) hides more than `K^{o(1)}` order dependence; the varying deterministic intervals can create more than `O(NK)` overlapping pairs; or the bad-start contribution in (21) cannot be removed with the fourth-moment bound (16). All four points are explicit finite/probabilistic estimates and do not use arithmetic conjectures.

The countermodel deliberately does not satisfy the prime singular-series identities, the exact `\Lambda^\sharp` structure, positivity of `\Lambda`, or any source-specific signed shifted-prime theorem. Those are valid ways to evade the obstruction. Consequently the finding rules out only a black-box implication from density-one ordinary Gowers smallness plus matched quadratic energy to the bow covariance saving; it does not rule out arithmetic information richer than that interface.
