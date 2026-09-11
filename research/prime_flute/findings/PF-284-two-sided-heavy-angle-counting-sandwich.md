# PF-284 — two-sided heavy-angle counting separates sufficient and obstructive endpoint scales

**Status:** `EXACT-DERIVED + CLASSICAL-SINGULAR-VALUE-CALCULUS + ENDPOINT-REDUCTION + ROUTE-SHARPENING`.

[[research/prime_flute/findings/PF-283-heavy-angle-counting-criterion-for-weak-trace-endpoint|PF-283]] proved the one-sided estimate

\[
N_T(a+2\tau)\le N_{\Gamma_\tau}(a)
\]

for the physical factorization

\[
T=F_P\Gamma F_H,
\qquad 0\le F_P,F_H\le I,
\qquad \Gamma=V_P^*V_H,
\]

and therefore reduced a sufficient weak-trace endpoint route to the matched heavy-angle bound

\[
N_{\Gamma_\tau}(2\tau)=O(\tau^{-1}).
\]

The same thresholding admits an exact reverse comparison on the heavy subspaces. This supplies the missing distinction between **failure of the sufficient route** and a **genuine obstruction to weak trace class**.

For arbitrary `0<\alpha,\beta<1`, set

\[
Q_P^\alpha=\mathbf 1_{[\alpha,1]}(F_P),
\qquad
Q_H^\beta=\mathbf 1_{[\beta,1]}(F_H),
\]

\[
\Gamma_{\alpha,\beta}=Q_P^\alpha\Gamma Q_H^\beta,
\qquad
T_{\alpha,\beta}=Q_P^\alpha TQ_H^\beta.
\]

Then for every `a>0`,

\[
\boxed{
N_T(a+\alpha+\beta)
\le
N_{\Gamma_{\alpha,\beta}}(a)
\le
N_T(\alpha\beta a).
}
\tag{PF-284 counting sandwich}
\]

In the symmetric matched choice `\alpha=\beta=\tau`, `a=2\tau`, this becomes

\[
\boxed{
N_T(4\tau)
\le
N_{\Gamma_\tau}(2\tau)
\le
N_T(2\tau^3).
}
\tag{1}
\]

Thus PF-283's `O(\tau^{-1})` angle count remains a sufficient endpoint theorem, but weak trace class itself only forces the much weaker necessary bound

\[
\boxed{
T\in\mathcal S_{1,\infty}
\Longrightarrow
N_{\Gamma_\tau}(2\tau)=O(\tau^{-3}).
}
\tag{2}
\]

Consequently, growth strictly faster than `\tau^{-1}` merely kills the PF-283 sufficient route; it does **not** refute the endpoint. By contrast,

\[
\boxed{
\sup_{0<\tau<\tau_0}
\tau^3N_{\Gamma_\tau}(2\tau)=\infty
\Longrightarrow
T\notin\mathcal S_{1,\infty}.
}
\tag{3}
\]

More generally, the asymmetric heavy sectors give the necessary weak-trace test

\[
\boxed{
T\in\mathcal S_{1,\infty}
\Longrightarrow
\sup_{\alpha,\beta,a}
\alpha\beta a\,
N_{\Gamma_{\alpha,\beta}}(a)<\infty,
}
\tag{4}
\]

where the supremum is taken over positive thresholds in the regime being tested. Any canonical sequence for which the quantity in (4) diverges is therefore an actual endpoint obstruction.

## Claim

Under the hypotheses and notation of PF-282/PF-283, for all `0<\alpha,\beta<1` and `a>0`:

1. the weak-strength complement satisfies
   \[
   \|T-T_{\alpha,\beta}\|\le \alpha+\beta;
   \]
2. the heavy block satisfies the two-sided singular-value comparison
   \[
   \alpha\beta\,s_j(\Gamma_{\alpha,\beta})
   \le s_j(T_{\alpha,\beta})
   \le s_j(\Gamma_{\alpha,\beta});
   \]
3. since compression cannot increase singular/approximation numbers,
   \[
   s_j(T_{\alpha,\beta})\le s_j(T),
   \]
   and hence the counting sandwich above follows;
4. the symmetric matched statistic has a two-power gap between the `O(\tau^{-1})` sufficient scale and the `O(\tau^{-3})` necessary scale;
5. the asymmetric statistic `\alpha\beta a\,N_{\Gamma_{\alpha,\beta}}(a)` is a genuine falsification observable for weak trace class.

## 1. The upper comparison allows asymmetric strength thresholds

PF-283 used the same threshold on both sides. Nothing in its norm argument requires symmetry. Because the spectral projections commute with their respective strength factors,

\[
T-T_{\alpha,\beta}
=(I-Q_P^\alpha)T
+Q_P^\alpha T(I-Q_H^\beta),
\]

and therefore

\[
\|T-T_{\alpha,\beta}\|
\le
\|(I-Q_P^\alpha)F_P\|
+
\|F_H(I-Q_H^\beta)\|
\le \alpha+\beta.
\tag{5}
\]

Moreover,

\[
T_{\alpha,\beta}
=(Q_P^\alpha F_PQ_P^\alpha)
\Gamma_{\alpha,\beta}
(Q_H^\beta F_HQ_H^\beta),
\]

and the outer factors are contractions, so

\[
s_j(T_{\alpha,\beta})
\le s_j(\Gamma_{\alpha,\beta}).
\tag{6}
\]

Combining (5) with the standard perturbation inequality gives

\[
s_j(T)
\le s_j(\Gamma_{\alpha,\beta})+\alpha+\beta,
\]

hence

\[
N_T(a+\alpha+\beta)
\le N_{\Gamma_{\alpha,\beta}}(a).
\tag{7}
\]

This recovers PF-283 when `\alpha=\beta=\tau`.

## 2. Heavy strength also gives a reverse singular-value bound

On `\operatorname{Ran}Q_P^\alpha`, the positive operator

\[
A_\alpha=Q_P^\alpha F_PQ_P^\alpha
\]

satisfies `A_\alpha\ge\alpha I`; similarly

\[
B_\beta=Q_H^\beta F_HQ_H^\beta\ge\beta I
\]

on `\operatorname{Ran}Q_H^\beta`. Thus both are invertible on their heavy subspaces and

\[
\|A_\alpha^{-1}\|\le\alpha^{-1},
\qquad
\|B_\beta^{-1}\|\le\beta^{-1}.
\]

Since

\[
T_{\alpha,\beta}=A_\alpha\Gamma_{\alpha,\beta}B_\beta,
\]

we may solve on the heavy subspaces:

\[
\Gamma_{\alpha,\beta}
=A_\alpha^{-1}T_{\alpha,\beta}B_\beta^{-1}.
\]

The ordinary ideal inequality for approximation/singular numbers yields

\[
s_j(\Gamma_{\alpha,\beta})
\le
(\alpha\beta)^{-1}s_j(T_{\alpha,\beta}),
\]

or equivalently

\[
\alpha\beta\,s_j(\Gamma_{\alpha,\beta})
\le s_j(T_{\alpha,\beta}).
\tag{8}
\]

Finally, `T_{\alpha,\beta}=Q_P^\alpha TQ_H^\beta` is a two-sided compression by contractions, so

\[
s_j(T_{\alpha,\beta})\le s_j(T).
\tag{9}
\]

If `s_j(\Gamma_{\alpha,\beta})>a`, equations (8)--(9) force `s_j(T)>\alpha\beta a`. Counting indices gives

\[
N_{\Gamma_{\alpha,\beta}}(a)
\le N_T(\alpha\beta a).
\tag{10}
\]

Equations (7) and (10) are the claimed two-sided sandwich.

## 3. What the symmetric heavy-angle count can and cannot decide

Set `\alpha=\beta=\tau` and `a=2\tau`. Then (7) and (10) give (1). If `T\in\mathcal S_{1,\infty}`, the standard counting characterization supplies a constant `C` such that

\[
N_T(x)\le \frac{C}{x}
\]

for small positive `x`. Therefore

\[
N_{\Gamma_\tau}(2\tau)
\le N_T(2\tau^3)
\le \frac{C}{2\tau^3},
\]

which proves (2). The contrapositive is (3).

This corrects the interpretation of a prospective negative result for the accepted heavy-angle clue. A sequence with

\[
\tau N_{\Gamma_\tau}(2\tau)\to\infty
\]

shows only that the PF-283 **sufficient criterion** fails. It does not show that `T` is outside weak trace class. To obtain a genuine endpoint obstruction from the same symmetric statistic, one needs the stronger divergence

\[
\tau^3N_{\Gamma_\tau}(2\tau)\to\infty
\]

along some sequence, or another argument not passing through this counting sandwich.

The gap is structural: thresholding at strength `\tau` on both sides can suppress a heavy-angle singular direction by a factor as small as `\tau^2`, while the angle itself is being tested at scale `\tau`. That produces the cubic comparison scale `\tau^3`. It is an artifact of this matched threshold statistic, not a claim that `3` is a universal prime-flute exponent.

## 4. Asymmetric thresholds give a sharper falsification surface

The prime-flute `P/H` split is physically asymmetric, so forcing a common threshold is unnecessary. Equation (10) says that weak trace class implies

\[
\alpha\beta a\,
N_{\Gamma_{\alpha,\beta}}(a)
\le C
\tag{11}
\]

for every sufficiently small product `\alpha\beta a`. Thus a geometric construction is free to choose thresholds adapted to the actual low-fed and high-fed extension-strength distributions. If some canonical sequence `\alpha_k,\beta_k,a_k` satisfies

\[
\alpha_k\beta_k a_k\,
N_{\Gamma_{\alpha_k,\beta_k}}(a_k)\to\infty,
\]

then `T\notin\mathcal S_{1,\infty}`.

Conversely, equation (7) gives an asymmetric sufficient route: for each small target scale `x`, it is enough to find positive `\alpha,\beta,a` with

\[
a+\alpha+\beta=x
\]

and

\[
x\,N_{\Gamma_{\alpha,\beta}}(a)=O(1).
\]

This does not close the endpoint, but it removes an artificial symmetry constraint from the geometric theorem one must seek.

## Relevance to the prime flute

The current frontier is a theorem about simultaneous one-cusp-pant extension geometry, not another operator-ideal choice. PF-284 sharpens what that theorem has to accomplish in three distinct senses:

- `O(\tau^{-1})` for the symmetric matched angle count is a clean **positive sufficient target**;
- growth faster than `\tau^{-1}` is only a **route-null result**, not an endpoint refutation;
- divergence of the necessary weighted count, symmetrically `\tau^3N_{\Gamma_\tau}(2\tau)` or asymmetrically `\alpha\beta aN_{\Gamma_{\alpha,\beta}}(a)`, is a **true endpoint obstruction**.

This distinction matters for variable corridor/reservoir geometry because a dense heavy reservoir may defeat the strongest convenient Weyl law while remaining compatible with weak trace class after strength damping.

## Prior art and novelty assessment

The ingredients are classical operator-ideal facts: stability of approximation/singular numbers under multiplication by bounded operators, compression monotonicity, norm perturbation, and the counting characterization of weak Schatten ideals. They are part of the same standard weak-trace/singular-value calculus already audited in [[research/prime_flute/SOURCES#s20--weak-trace-class-and-weak-schatten-endpoint-ideal-calculus|S20]]. No novelty is claimed for those inequalities or for principal-angle language itself.

The durable content is their exact two-sided organization for the PF-282 physical strength-angle factorization. It upgrades PF-283 from a sufficient test to a quantitative decision surface separating sufficient closure, failure of that particular route, and an actual weak-trace obstruction. The prior-art audit found no basis for presenting this elementary specialization as a new general operator theorem.

## Boundary conditions and failure modes

This finding does **not** estimate the canonical prime-flute heavy-angle count and does not prove or disprove `T\in\mathcal S_{1,\infty}`. In particular:

- `N_{\Gamma_\tau}(2\tau)=O(\tau^{-3})` is necessary under weak trace, not sufficient;
- failure of `O(\tau^{-3})` only becomes an obstruction when the weighted quantity is genuinely unbounded, not merely larger than the PF-283 `O(\tau^{-1})` target;
- the cubic symmetric scale comes from the matched choice `\alpha=\beta=\tau`, `a=2\tau`; different threshold schedules produce different products `\alpha\beta a`;
- if a heavy compression is noncompact, its counting function may be infinite, in which case (10) immediately rules out weak trace at that threshold;
- all comparisons must retain the physical `P/H` projections fixed by the simultaneous extension problem; a scalar same-mode reservoir does not substitute for `\Gamma_{\alpha,\beta}`;
- no wave-operator, trace-formula, prime/clone separation, or RH consequence follows from the counting sandwich alone.

## Decisive audit test

Check the sandwich on finite-rank diagonal strength models with independently chosen `P/H` strength spectra and prescribed principal angles. The upper bound must survive norm-small weak sectors, and the lower bound must become sharp when the heavy strengths sit near their thresholds.

For the canonical prime flute, the useful geometric experiment/theorem should now report which of three regimes occurs: a sufficient weighted count closing the endpoint, an intermediate count that only kills the current sufficient route, or a necessary weighted-count violation that genuinely rules out weak trace class.