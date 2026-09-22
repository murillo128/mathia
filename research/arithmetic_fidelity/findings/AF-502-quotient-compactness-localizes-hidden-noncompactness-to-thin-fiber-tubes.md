# AF-502 — Quotient compactness localizes hidden noncompactness to thin fiber tubes

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NUISANCE-QUOTIENT`, `MEASURE-OF-NONCOMPACTNESS`, `ASYMPTOTIC-COMPACTNESS`, `FIBER-LOCALIZATION`, `MINIMAL-LIFT`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-501 separates two universal failures when a nuisance quotient is taken before a compactness test: source nonsaturation can admit new bounded aliases, while an infinite-dimensional nuisance fiber can hide bounded noncompact motion. Its finite-dimensional-fiber criterion is deliberately universal over all bounded sets. For a **fixed** residual family, the exact replacement is more local: once the quotient image is compact at the relevant scale, every remaining noncompactness must already occur inside arbitrarily thin neighborhoods of individual quotient fibers.

Let `Y` and `Q` be Banach spaces and let

\[
\pi:Y\to Q
\]

be a bounded linear map of norm at most `1`; the main application is the canonical quotient map `Y -> Y/V`. Let `chi_Y` and `chi_Q` denote the Hausdorff measures of noncompactness. For a bounded set `A subset Y` define

\[
\beta(A):=\chi_Q(\pi(A))
\]

and, for `rho>0`, the **quotient-tube noncompactness**

\[
\Phi_\rho(A;\pi)
:=
\sup_{q\in Q}
\chi_Y\!\left(
A\cap \pi^{-1}(B_Q(q,\rho))
\right),
\]

where `B_Q(q,rho)` is the open radius-`rho` ball and `chi(emptyset)=0`.

Then:

1. For every bounded `A` and every `rho>0`,

\[
\boxed{\Phi_\rho(A;\pi)\le \chi_Y(A).}
\]

2. More strongly, as soon as the tube radius exceeds the noncompactness of the quotient image,

\[
\boxed{
\rho>\beta(A)
\quad\Longrightarrow\quad
\Phi_\rho(A;\pi)=\chi_Y(A).
}
\]

Thus if `pi(A)` is relatively compact, then for **every** `rho>0`,

\[
\boxed{
\chi_Y(A)
=
\sup_{q\in Q}
\chi_Y\!\left(
A\cap\pi^{-1}(B_Q(q,\rho))
\right).
}
\]

All noncompactness of `A` is therefore visible inside arbitrarily thin quotient tubes. It cannot be sustained merely by spreading compact pieces over a compact quotient image.

3. Exact fiber compactness is not enough. There exists a closed bounded `A` with compact quotient image and with every exact fiber

\[
A\cap\pi^{-1}(\{q\})
\]

finite, yet `A` is noncompact. The missing resource is **uniform compactness in shrinking neighborhoods of the fibers**, not pointwise compactness of each fiber separately.

4. Apply this to the raw radius-truncated translated tails from AF-499--AF-501,

\[
A_{T,R}:=E^0_{T,R}(C,s).
\]

Define

\[
\bar\nu_{C,V}(s;R)
:=
\lim_{T\to\infty}
\chi_Q(\pi(A_{T,R}))
\]

and

\[
\phi_{C,V}(s;R,\rho)
:=
\lim_{T\to\infty}
\sup_{q\in Q}
\chi_Y\!\left(
A_{T,R}\cap\pi^{-1}(B_Q(q,\rho))
\right).
\]

Both limits exist because the relevant tail sets decrease with `T`. For every

\[
\rho>\bar\nu_{C,V}(s;R),
\]

one has the exact localization identity

\[
\boxed{
\nu_C^0(s;R)
=
\phi_{C,V}(s;R,\rho).
}
\]

If, in addition, the closed source `D=cl C` is `V`-saturated and `V` is proximinal, AF-501 gives

\[
\pi(E^0_{T,R})=E^V_{T,R},
\]

so

\[
\bar\nu_{C,V}(s;R)=\nu_C^V(s;R).
\]

Hence in the quotient-compact regime

\[
\nu_C^V(s;R)=0,
\]

the full upstream defect is exactly the defect inside every positive-width quotient tube:

\[
\boxed{
\nu_C^0(s;R)
=
\phi_{C,V}(s;R,\rho)
\qquad(\rho>0).
}
\]

This is the fixed-family refinement of AF-501. Finite-dimensionality of `V` is the exact **universal** condition that makes every bounded hidden fiber harmless. For a particular infinite-dimensional nuisance family, what is actually required is that its task-visible tail have vanishing noncompactness uniformly in sufficiently thin quotient tubes.

## The finite-cover localization identity

The first inequality is immediate from monotonicity of the Hausdorff measure of noncompactness: every tube intersection is a subset of `A`, so

\[
\chi_Y\!\left(A\cap\pi^{-1}(B_Q(q,\rho))\right)
\le
\chi_Y(A).
\]

Taking the supremum over `q` gives

\[
\Phi_\rho(A;\pi)\le\chi_Y(A).
\]

Now suppose

\[
\rho>\beta(A)=\chi_Q(\pi(A)).
\]

By the definition of Hausdorff measure of noncompactness, there are finitely many centers `q_1,...,q_N` such that

\[
\pi(A)
\subset
\bigcup_{j=1}^N B_Q(q_j,\rho).
\]

Therefore

\[
A
=
\bigcup_{j=1}^N
\left(A\cap\pi^{-1}(B_Q(q_j,\rho))\right).
\]

The Hausdorff measure of noncompactness of a finite union is the maximum of the measures of its pieces. Hence

\[
\chi_Y(A)
=
\max_{1\le j\le N}
\chi_Y\!\left(A\cap\pi^{-1}(B_Q(q_j,\rho))\right)
\le
\Phi_\rho(A;\pi).
\]

Combined with the opposite inequality, this proves

\[
\Phi_\rho(A;\pi)=\chi_Y(A).
\]

The result is not an additive decomposition into a quotient defect plus a fiber defect. It is a **localization law**: once the quotient can be covered at radius `rho` by finitely many cells, at least one of those cells must carry the entire Hausdorff noncompactness of `A`.

## The strict radius threshold is sharp

The condition

\[
\rho>\chi_Q(\pi(A))
\]

cannot in general be weakened to `rho>=chi_Q(pi(A))` when open balls are used.

Take

\[
Y=Q=\ell^2,
\qquad
\pi=\operatorname{id},
\qquad
A=\{e_n:n\ge1\},
\]

where `(e_n)` is the standard orthonormal sequence. Its Hausdorff measure of noncompactness is

\[
\chi_{\ell^2}(A)=1.
\]

Indeed, the ball of any radius greater than `1` centered at zero covers `A`, while no finite family of balls of radius strictly less than `1` can cover the orthonormal sequence.

At the boundary radius `rho=1`, however, every open unit ball meets `A` only finitely. If `q=0`, it meets none of the `e_n`. If `q != 0` and

\[
\|e_n-q\|<1,
\]

then

\[
1+\|q\|^2-2\operatorname{Re}\langle e_n,q\rangle<1,
\]

so

\[
\operatorname{Re}\langle e_n,q\rangle>\frac{\|q\|^2}{2}.
\]

The coordinates of an `ell^2` vector tend to zero, so this can hold for only finitely many `n`. Consequently

\[
\Phi_1(A;\operatorname{id})=0
\qquad\text{while}\qquad
\chi(A)=1.
\]

The strict inequality in the localization theorem is therefore genuine rather than a proof artifact.

## Compact exact fibers do not prevent drifting hidden noncompactness

The localization law exposes a sharper boundary than the phrase “compact fibers.” Let

\[
Y=\mathbb R\oplus_2\ell^2,
\qquad
Q=\mathbb R,
\qquad
\pi(x,u)=x,
\]

and define

\[
A
:=
\{(0,0)\}
\cup
\{(1/n,e_n):n\ge1\}.
\]

Then `A` is closed and bounded in `Y`, and

\[
\pi(A)=\{0\}\cup\{1/n:n\ge1\}
\]

is compact. Every exact fiber of the restriction `pi|_A` is a singleton, hence compact. Nevertheless `A` is not relatively compact: the `ell^2` components contain the orthonormal sequence, and in fact

\[
\chi_Y(A)=1.
\]

For every `rho>0`, the tube around the limiting quotient point `0` contains all sufficiently late terms:

\[
A\cap\pi^{-1}(B_\mathbb R(0,\rho))
\supset
\{(1/n,e_n):n>1/\rho\}.
\]

Therefore

\[
\boxed{
\chi_Y\!\left(
A\cap\pi^{-1}(B_\mathbb R(0,\rho))
\right)=1
\qquad(\rho>0).
}
\]

The noncompactness moves through distinct exact fibers whose quotient labels converge to the same point. A pointwise audit of the fibers misses it completely; every positive-width tube catches it.

This is also the classical topological distinction between compact fibers and a **perfect/proper compactness-lifting map**. The restricted map `pi|_A` is not closed: the subset

\[
\{(1/n,e_n):n\ge1\}
\]

is closed in `A`, while its image `\{1/n:n>=1\}` is not closed in `pi(A)`. Classical perfect-map theory therefore predicts that compact fibers alone are insufficient. The tube profile above gives the quantitative metric version needed by Arithmetic Fidelity.

## Tail specialization after nuisance quotienting

Fix `R<infinity` and write

\[
A_T:=E^0_{T,R}(C,s).
\]

Because `A_T` decreases with `T`, both

\[
\chi_Y(A_T)
\quad\text{and}\quad
\chi_Q(\pi(A_T))
\]

are nonincreasing. Likewise, for each fixed `rho>0`,

\[
\sup_q
\chi_Y\!\left(A_T\cap\pi^{-1}(B_Q(q,\rho))\right)
\]

is nonincreasing. The three tail limits defining `nu_C^0`, `bar nu_{C,V}`, and `phi_{C,V}` therefore exist.

Now choose

\[
\rho>\bar\nu_{C,V}(s;R).
\]

For all sufficiently large `T`,

\[
\rho>\chi_Q(\pi(A_T)).
\]

The finite-cover localization identity applies at every such `T`, giving

\[
\chi_Y(A_T)
=
\sup_q
\chi_Y\!\left(A_T\cap\pi^{-1}(B_Q(q,\rho))\right).
\]

Taking the tail limit proves

\[
\nu_C^0(s;R)
=
\phi_{C,V}(s;R,\rho).
\]

If `D` is `V`-saturated and `V` is proximinal, AF-501 identifies the quotient image of the raw tail exactly with the quotient-visible tail:

\[
\pi(A_T)=E^V_{T,R}.
\]

Then

\[
\bar\nu_{C,V}(s;R)
=
\nu_C^V(s;R),
\]

so the threshold controlling tube localization is itself the downstream quotient noncompactness already measured by AF-500/AF-501.

In particular, if the quotient-visible tail is asymptotically compact, then for every positive tube width `rho`,

\[
\nu_C^0(s;R)=\phi_{C,V}(s;R,\rho).
\]

Thus an infinite-dimensional nuisance fiber does **not** by itself block compactness lifting for a fixed arithmetic family. The exact remaining test is whether noncompactness persists uniformly in arbitrarily thin quotient neighborhoods along that family's escaping residual tail.

## Prior-art and novelty audit

No broad novelty is claimed for Hausdorff measures of noncompactness, their finite-union law, perfect maps, proper maps, or compactness lifting.

- R. R. Akhmerov, M. I. Kamenskii, A. S. Potapov, A. E. Rodkina, and B. N. Sadovskii, *Measures of Noncompactness and Condensing Operators*, Operator Theory: Advances and Applications 55, Birkhauser (1992), DOI `10.1007/978-3-0348-5727-7`. Role: standard Hausdorff-measure-of-noncompactness machinery, including monotonicity, the finite-union maximum property, and compactness kernel used in the localization argument.
- James R. Munkres, *Topology*, 2nd ed., Prentice Hall (2000), §26 exercises on perfect maps. Role: classical perfect-map language: a continuous closed map with compact fibers lifts compactness of the target to compactness of the domain. This is the topological counterpart of the distinction between pointwise compact fibers and the uniform near-fiber control isolated here.
- Richard S. Palais, **“When proper maps are closed,”** *Proceedings of the American Mathematical Society* 24(4), 835–836 (1970), DOI `10.1090/S0002-9939-1970-0254818-X`. Role: classical proper-map background and the relation between inverse-image compactness and closedness under standard topological hypotheses.

The exact finite-cover equality for `Phi_rho` is derived directly from the defining covering characterization of `chi`; no novelty is claimed for its ingredients. The durable Arithmetic Fidelity contribution is its placement after AF-499--AF-501: **once downstream quotient noncompactness falls below a scale `rho`, every remaining upstream noncompactness is forced into a single `rho`-tube, and when the quotient tail is compact this remains true at every positive scale.** This replaces AF-501's universal finite-dimensional-fiber gate by an exact family-level diagnostic and shows why auditing only exact fibers is insufficient.

## Falsification and boundary audit

- The localization formula uses the Hausdorff measure of noncompactness specifically through its finite-cover definition and finite-union maximum law. An analogous statement for another compactness defect must be checked rather than assumed.
- The threshold is strict. At the exact value `rho=chi_Q(pi(A))`, a finite `rho`-net need not exist; the orthonormal control above shows the identity can fail maximally at the boundary.
- Compactness of every exact fiber is not sufficient. The drifting-fiber example shows that compactness must be uniform across quotient labels that approach one another. In classical topology this missing uniformity appears as failure of closedness/properness.
- The theorem does not say that the supremum is attained by one fixed quotient center as `T->infinity`. The center carrying near-maximal noncompactness may drift with the tail. A stronger fixed-center conclusion would require additional compactness/semicontinuity hypotheses.
- Without source saturation and proximinality, `pi(E^0_{T,R})` need not equal the full quotient-visible tail `E^V_{T,R}`. The raw-image localization theorem remains valid, but identifying its quotient defect with `nu_C^V(s;R)` requires the AF-501 commutation hypotheses or another exact replacement.
- Vanishing tube defect is a compactness-lifting condition, not a rational-prime discriminator. It says when quotient-visible tightness can be lifted through a particular nuisance family; it does not establish that the retained structure distinguishes ordinary primes from Beurling or other matched controls.
- The criterion is deliberately family-level. Infinite-dimensional `V` remains fatal for the **universal** bounded-lifting property of AF-501, because one can always choose a bounded noncompact subset inside a single fiber.

## Consequence for the research line

AF-499 split critical contact fidelity into distance attainment and tail compactness. AF-500 showed that compactness must generally be measured after nuisance quotienting. AF-501 separated quotient-induced alias admission from noncompact nuisance-fiber motion. AF-502 now identifies the exact fixed-family form of the latter obstruction.

The compactness audit can be sharpened to

\[
\boxed{
\text{quotient tail defect}
\quad+\quad
\text{uniform near-fiber tail defect},
}
\]

with the important qualification that the second term is not additive: once the quotient defect lies below the chosen tube radius, the near-fiber term equals the entire upstream Hausdorff noncompactness.

For future arithmetic applications, the practical question is therefore no longer merely whether nuisance fibers are finite-dimensional or individually compact. It is whether, after the arithmetic nuisance equivalence has been fixed and source-admission has been audited, **bounded residual aliases whose quotient labels become arbitrarily close can still carry a noncompact family upstream**. That is the remaining compactness-lifting obstruction that a rational-prime source model must control.