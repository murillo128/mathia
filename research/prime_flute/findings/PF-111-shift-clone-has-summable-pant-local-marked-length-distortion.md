# PF-111 — shift clone has summable pant-local marked-length distortion

**Status:** `LITERATURE+DERIVED + NEGATIVE/BOUNDARY`. Thurston's pair-of-pants length-ratio lemma is classical. The project-specific consequence is that the exact all-composite shift clone `p_n -> p_n+1` cannot amplify its summable **relative cuff defect** into order-one distortion by passing to arbitrarily complicated closed words inside a single tight pair of pants. No global quasiconformal, resolvent, Schatten, scattering, or full primitive-orbit statement is claimed.

## Claim

Let `P_n` be the one-cusp tight pair of pants in the exact prime flute whose two finite boundary cuffs have lengths

\[
\ell_n,\qquad \ell_{n+1},
\]

and let `P_n^+` be the corresponding pair of pants in the exact all-composite shift clone `p_j -> p_j+1` of PF-106, with finite cuff lengths

\[
\ell_n^+,\qquad \ell_{n+1}^+.
\]

For each finite cuff put

\[
\varepsilon_j
:=
\left|\log\frac{\ell_j^+}{\ell_j}\right|.
\tag{1}
\]

PF-107 proves

\[
\sum_j\frac{|\ell_j^+-\ell_j|}{\ell_j}<\infty,
\qquad
\frac{\ell_j^+}{\ell_j}\to1.
\tag{2}
\]

Hence

\[
\boxed{\sum_j\varepsilon_j<\infty.}
\tag{3}
\]

Now let `alpha` be any nonperipheral conjugacy class in `pi_1(P_n)`, and denote by `L_n(alpha)` and `L_n^+(alpha)` the lengths of its geodesic representatives in the two marked pants. Then

\[
\boxed{
\left|\log\frac{L_n^+(\alpha)}{L_n(\alpha)}\right|
\le
\max(\varepsilon_n,\varepsilon_{n+1}).
}
\tag{4}
\]

The bound is uniform in the word length and complexity of `alpha`. Consequently, with

\[
D_n:=
\sup_{\alpha\in\pi_1(P_n)\ \mathrm{nonperipheral}}
\left|\log\frac{L_n^+(\alpha)}{L_n(\alpha)}\right|,
\]

we have

\[
\boxed{
D_n\le\max(\varepsilon_n,\varepsilon_{n+1}),
\qquad
\sum_n D_n<\infty.
}
\tag{5}
\]

Thus the entire marked closed-geodesic length spectrum of each individual tight pant is asymptotically identical to that of its composite-clone mate, with a summable sequence of uniform logarithmic distortions.

## 1. Relative cuff errors are summable

PF-107 gives the sharper tail asymptotics

\[
\ell_j^+-\ell_j
=\frac{2}{p_{j-1}}+o(p_{j-1}^{-1})
\]

and, using the unconditional short-interval bound already admitted there,

\[
\ell_j\gg\log p_{j-1}.
\]

In particular

\[
\frac{|\ell_j^+-\ell_j|}{\ell_j}
=O\!\left(\frac1{p_{j-1}\log p_{j-1}}\right),
\]

whose sum over the prime index converges. Since the length ratio tends to one, the elementary estimate `|log(1+x)| <= 2|x|` for sufficiently small `|x|` converts PF-107's relative `ell^1` statement into (3). Any finite initial segment is harmless.

This step is important because the raw additive cuff defect is **not** in `ell^1`; PF-107 proves only `ell^2 \ ell^1` there. The present argument uses the multiplicative/marked-length scale, not the additive circumference scale.

## 2. Thurston's shrinking-at-the-waist lemma controls every local word

Thurston's Lemma 3.4 in *Minimal stretch maps between hyperbolic surfaces* states the following for two marked hyperbolic structures `g,h` on a pair of pants with geodesic boundary. If `alpha` is not freely homotopic to a boundary component and

\[
r_{gh}(\alpha):=\frac{\ell_h(\alpha)}{\ell_g(\alpha)}>1,
\]

then

\[
r_{gh}(\alpha)
<
\max_i r_{gh}(\partial_i).
\tag{6}
\]

The statement is deliberately stronger than a simple-curve estimate: it applies to any nonperipheral fundamental-group element, so arbitrarily long primitive or nonprimitive words inside the pant are included.

Our tight pants have one cusp rather than three positive geodesic boundaries. To use (6) without assigning a meaningless ratio `0/0` to the cusp, replace the common cusp in both marked pants by a geodesic boundary of the same length `eta>0`. The third boundary ratio is then exactly `1`. Hyperbolic pants and the length of every fixed nonperipheral class depend continuously on their boundary-length parameters, so letting `eta -> 0` gives the cusp version of the same inequalities.

Apply (6) from `P_n` to `P_n^+`. If `L_n^+(alpha)/L_n(alpha)>1`, then

\[
\frac{L_n^+(\alpha)}{L_n(\alpha)}
\le
\max\left(
1,
\frac{\ell_n^+}{\ell_n},
\frac{\ell_{n+1}^+}{\ell_{n+1}}
\right).
\tag{7}
\]

Apply the same lemma in the reverse direction. If `L_n(alpha)/L_n^+(alpha)>1`, then

\[
\frac{L_n(\alpha)}{L_n^+(\alpha)}
\le
\max\left(
1,
\frac{\ell_n}{\ell_n^+},
\frac{\ell_{n+1}}{\ell_{n+1}^+}
\right).
\tag{8}
\]

Taking logarithms of (7)--(8) proves (4) for every nonperipheral `alpha`.

Combining (4) with (3),

\[
\sum_n D_n
\le
\sum_n \max(\varepsilon_n,\varepsilon_{n+1})
\le
2\sum_n\varepsilon_n
<\infty,
\]

which is (5).

## 3. What this closes

PF-109 already proves uniform multiplicative matching for the special PF-004 family of canonical multi-gap separating geodesics, including pinching sequences. A different possible amplification remained: perhaps a fixed local pant contains complicated primitive words whose lengths react much more strongly to the small prime/composite cuff perturbation than the distinguished boundaries do.

PF-111 rules out exactly that mechanism:

\[
\boxed{
\text{summable relative cuff defect}
\not\longrightarrow
\text{large distortion through pant-local word complexity}.
}
\]

The conclusion is uniform over the **entire marked local length spectrum** of each pant, not merely over simple curves or a bounded collection of short words. Consequently a local primitive-orbit package attached independently to each tight pant cannot manufacture an order-one arithmetic distinction by taking increasingly complicated words inside those pieces.

This is relevant to the accepted relative-operator clue because it removes another natural source of geometric amplification. Together with PF-108 and PF-109, the shift clone now has:

- summable transverse/collar and area-weighted defects on explicitly controlled pieces;
- uniform multiplicative matching of all canonical multi-gap separators;
- summable uniform marked-length distortion for every closed word contained in an individual tight pant.

Any obstruction to a global perturbative comparison must therefore use information that is genuinely **cross-pant or operator-nonlocal**.

## 4. What this does not prove

Equation (5) is not a global length-spectrum theorem for the infinite flute. Closed geodesics that traverse several pants are not controlled by applying the closed-word estimate independently inside each pant: cutting such a curve produces geodesic arcs, and the gluing data for those arcs is a separate geometric problem.

In particular PF-111 does **not** prove:

1. a global quasiconformal or asymptotically isometric conjugacy of the prime and clone surfaces;
2. uniform control of every closed geodesic in the full flute;
3. compactness or Schatten membership of a relative resolvent;
4. wave/scattering equivalence;
5. convergence or analytic continuation of a full relative Selberg/Ruelle product.

This boundary is essential. PF-110 already rules out the convenient bounded-ideal-triangulation route to a global coordinate comparison. The surviving direct pants/collar program still has to control maps on seams, cusp regions and glued cross-pant trajectories, and then verify the hypotheses of an actual relative-operator theorem.

## 5. Prior art and novelty audit

The general marked-length inequality is classical. Thurston's `Shrinking at the waist` lemma was introduced as part of his minimal-Lipschitz comparison theory for hyperbolic surfaces. The surrounding literature on the Thurston asymmetric metric treats boundary and measured-lamination length ratios systematically. No novelty is claimed for (6), for pair-of-pants rigidity by boundary lengths, or for continuity as a boundary length tends to a cusp.

Directed searches for prime/cotangent flutes, the all-composite shift `p_n -> p_n+1`, and this particular length-spectrum comparison did not locate the specialization above. The durable project contribution is the composition

\[
\boxed{
\text{PF-107 summable relative cuff defect}
+
\text{Thurston pair-of-pants length-ratio lemma}
\Rightarrow
\text{summable uniform pant-local marked-length defect}.
}
\]

That consequence is useful as a **negative boundary**, not as a new general theorem in Teichmuller theory and not as evidence for RH.

## 6. Audit / falsification core

The reusable checks are:

1. take PF-107's proved `sum |ell_j^+-ell_j|/ell_j < infinity` and `ell_j^+/ell_j -> 1` as the only arithmetic/geometric input;
2. convert it to `sum |log(ell_j^+/ell_j)| < infinity` by an elementary small-relative-error estimate;
3. verify Thurston Lemma 3.4 with its crucial quantifier over **any** nonperipheral fundamental-group element, not only simple closed curves;
4. obtain the one-cusp version by approximating the common cusp with equal boundary length `eta` and passing to `eta -> 0`;
5. apply the lemma in both directions to get the absolute logarithmic bound (4);
6. sum `D_n <= max(epsilon_n,epsilon_{n+1})` to obtain (5);
7. do not extend the result to cross-pant geodesics, quasiconformal equivalence or an operator class without an additional gluing theorem.

A refutation would need to break PF-107's relative summability, the applicability/cusp limit of Thurston's pair-of-pants lemma, or the two-direction deduction of (4). A failure of the broader global operator-comparison program would not refute PF-111; it would identify precisely the cross-pant/nonlocal amplification that this finding leaves open.

## References

- W. P. Thurston, *Minimal stretch maps between hyperbolic surfaces*, preprint, arXiv:math/9801039 (1998), especially Lemma 3.4 (`Shrinking at the waist`).
- PF-107, PF-108, PF-109 and PF-110 in this research ledger.
