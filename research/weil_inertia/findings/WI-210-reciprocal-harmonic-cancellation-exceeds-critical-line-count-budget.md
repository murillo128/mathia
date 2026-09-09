# WI-210 — reciprocal-harmonic cancellation exceeds the local critical-line count budget

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-CANDIDATE`.

WI-184 shows that an actual-zeta symmetrized Maynard--Pratt bow with unfolded ordinate spacing

\[
d_T:=\frac{c_T}{2\pi}
\]

must have `d_T >= 2-o(1)`, and that every reciprocal harmonic `alpha=k/d_T` aligns the selected mirror pairs vertically. WI-209 then shows that the first reciprocal harmonic survives on the full Gallagher-scale physical slab with logarithmically superdiagonal residue energy, so any diagonal-scale source theorem would have to produce an asymptotically near-opposite complementary contribution.

There is a rigid obstruction to one natural way of supplying that complement. A positive critical-line population inside the same bow interval cannot cancel a positive-density symmetrized bow simultaneously at all reciprocal harmonics lying strictly inside support one. The obstruction is exact and is just Fejer positivity for the truncated trigonometric moment problem. If `r` reciprocal harmonics are available and the selected bow contains `M` off-line right-half labels, then simultaneous cancellation to `o(m)` accuracy by local critical-line zeros requires at least

\[
\boxed{(2r-o(1))M}
\]

critical-line zero labels, counted with multiplicity. Riemann--von Mangoldt leaves only

\[
\boxed{(d_T-2+o(1))m}
\]

zero labels beyond the selected bow and its compulsory mirrors. Since the number `r` of strictly interior reciprocal harmonics satisfies `d_T<=r+1`, the local count budget is at most `(r-1+o(1))m`. Thus the full Maynard--Pratt bow, for which `M=m-O(1)`, cannot be screened across all of those harmonics by any local population consisting only of critical-line zeros, including arbitrary critical-line multiplicity.

More generally, if `M/m -> kappa`, such screening is possible only if

\[
\boxed{2r\kappa\le d-2}
\]

along a subsequence `d_T->d`. In particular `kappa<(1/2)` is necessary for every bounded spacing `d>=2`, and the permitted fraction is much smaller near the count-saturating value `d=2`.

This is not yet RH and does not close the distinguished-twist clue. Zeros outside the bow interval, additional off-line pairs inside it, and the structured source terms in the WI-195 `Lambda-Lambda^sharp` representation remain possible cancellation reservoirs. The important change is qualitative: **if a future localization theorem forces reciprocal-harmonic cancellation to remain local, an RH-compatible critical-line reservoir cannot absorb a dense bow defect. Local screening must create further off-line defect or fail.** That is an explicit defect-to-defect bootstrap mechanism rather than another proportion-only inequality.

## 1. Reciprocal harmonics of a symmetrized bow

Use the WI-184 normalization

\[
L=\log T,
\qquad
x_j=\gamma_j\frac{L}{2\pi}
=x_0+d_Tj,
\qquad
d_T=\frac{c_T}{2\pi}.
\tag{1}
\]

Let `J` be the set of selected right-half-plane off-critical labels and write

\[
M:=|J|,
\qquad
b_j=(\beta_j-\tfrac12)L>0.
\tag{2}
\]

Functional-equation symmetry supplies the same-ordinate mirror for every `j in J`. At a frequency `alpha`, the pair contributes, up to the common normalization used in WI-184,

\[
2\cosh(b_j\alpha)e^{2\pi i x_j\alpha}.
\tag{3}
\]

For every positive integer `k` with

\[
\alpha_k:=\frac{k}{d_T}<1,
\tag{4}
\]

equation (1) gives

\[
e^{2\pi i x_j\alpha_k}
=e^{2\pi i x_0k/d_T}e^{2\pi i kj}
=e^{2\pi i x_0k/d_T}.
\tag{5}
\]

After rotating away the harmless common phase, the selected bow amplitude at the `k`-th reciprocal harmonic is therefore the positive real number

\[
\boxed{
B_k
=2\sum_{j\in J}\cosh\!\left(\frac{k b_j}{d_T}\right)
\ge2M.
}
\tag{6}
\]

No assumption that the horizontal depths are equal, periodic, bounded, or slowly varying is needed for the lower bound. Horizontal drift can only increase the selected pair amplitude.

Let

\[
r_T:=\max\{k\in\mathbb N:k<d_T\}.
\tag{7}
\]

These are exactly the positive reciprocal harmonics lying strictly inside the support-one band. If `d_T` is an integer, the endpoint `alpha=1` is deliberately excluded, so `r_T=d_T-1`. If `d_T` is not an integer, `r_T=\lfloor d_T\rfloor`. Equivalently,

\[
\boxed{r_T<d_T\le r_T+1.}
\tag{8}
\]

For a source-compatible bow `d_T>=2-o(1)`, at least the first reciprocal harmonic is available asymptotically. When `d_T` rises even slightly above `2`, a second strictly interior harmonic appears.

## 2. A sharp Fejer moment budget for positive critical-line cancellation

Now take any collection `C` of critical-line zeros in the same bow interval that are not among the selected off-line mirror pairs. Count multiplicity by positive integers `mu_l` and write their unfolded ordinates as `u_l`. Relative to the bow origin define

\[
z_l
:=\exp\!\left(\frac{2\pi i(u_l-x_0)}{d_T}\right),
\qquad |z_l|=1.
\tag{9}
\]

After the same phase rotation used in (6), their amplitude at the reciprocal harmonic `alpha_k` is exactly the trigonometric moment

\[
S_k:=\sum_l\mu_lz_l^k,
\qquad
C_0:=\sum_l\mu_l.
\tag{10}
\]

Here `C_0` is the number of critical-line zero labels in this complementary population, counted with multiplicity. Critical-line multiple zeros are therefore already included; they do not evade the argument.

Suppose first that this population cancels the selected bow exactly at the first `r` reciprocal harmonics:

\[
S_k=-B_k,
\qquad 1\le k\le r.
\tag{11}
\]

For `|z|=1`, the Fejer square

\[
F_r(z)
:=|1+z+\cdots+z^r|^2
=(r+1)+2\sum_{k=1}^{r}(r+1-k)\Re z^k
\tag{12}
\]

is nonnegative. Sum (12) against the positive multiplicities `mu_l`. Using (10)--(11) and then (6),

\[
\begin{aligned}
0
&\le (r+1)C_0
+2\sum_{k=1}^{r}(r+1-k)\Re S_k\\
&=(r+1)C_0
-2\sum_{k=1}^{r}(r+1-k)B_k\\
&\le (r+1)C_0
-4M\sum_{k=1}^{r}(r+1-k)\\
&=(r+1)(C_0-2rM).
\end{aligned}
\tag{13}
\]

Hence

\[
\boxed{C_0\ge2rM.}
\tag{14}
\]

The coefficient `r` in the underlying trigonometric moment problem is sharp. If the required target moments were the common value `-A`, a positive measure of total mass `rA` attains them by putting mass `A` at each nontrivial `(r+1)`-st root of unity, since the sum of their `k`-th powers is `-1` for `1<=k<=r`. The extra factor `2M` in (14) comes from the compulsory functional-equation mirror paired with each selected right-half bow label, not from slack in Fejer positivity.

The result is stable. If instead

\[
|S_k+B_k|\le\varepsilon m
\qquad(1\le k\le r),
\tag{15}
\]

then

\[
\Re S_k\le -2M+\varepsilon m,
\]

and the same calculation gives

\[
\boxed{
C_0\ge2rM-r\varepsilon m.
}
\tag{16}
\]

Thus `o(m)` cancellation error at each fixed reciprocal harmonic still costs `(2r-o(1))M` positive critical-line mass.

Equation (14) is equivalently the simplest positive-Toeplitz obstruction. The moments of a positive measure on the unit circle form a positive semidefinite Toeplitz sequence; testing that Toeplitz form on the all-ones vector gives exactly (12)--(14). This is classical trigonometric moment theory, not a new identity.

## 3. Riemann--von Mangoldt leaves far too little local critical-line mass

Return to the source-compatible bow interval of WI-184. Let `m` denote the number of selected right-half bow labels before reflection. The selected bow plus compulsory same-ordinate mirrors contributes the baseline

\[
2m+O(1)
\tag{17}
\]

zero labels, because only `O(1)` displayed Maynard--Pratt labels lie on the critical line. Riemann--von Mangoldt gives for bounded spacing scale

\[
N_I=(d_T+o(1))m.
\tag{18}
\]

Therefore the entire local excess count beyond the selected mirror-closed bow is

\[
\boxed{
E_I=(d_T-2+o(1))m.
}
\tag{19}
\]

This excess includes everything: additional critical-line zeros, additional off-line pairs, and extra multiplicity at selected points. Consequently a critical-line complementary population satisfies the unconditional upper bound

\[
C_0\le E_I+O(1).
\tag{20}
\]

The inequality is deliberately generous. Extra multiplicity at a selected off-line bow ordinate consumes `E_I` but reinforces the selected reciprocal phase rather than helping cancellation, so charging all excess mass to `C_0` only makes the proposed critical-line screening mechanism easier.

Take a subsequence on which `d_T->d>=2` and `r_T=r` is constant; bounded spacing always admits such a further subsequence away from the harmless integer-transition bookkeeping. Equation (8) gives

\[
d-2\le r-1.
\tag{21}
\]

For the displayed Maynard--Pratt bow, `M=m-O(1)`. If its selected reciprocal amplitudes could be cancelled by local critical-line zeros to `o(m)` at every `1<=k<=r`, equations (16), (19)--(21) would require simultaneously

\[
C_0\ge(2r-o(1))m
\tag{22}
\]

and

\[
C_0\le(r-1+o(1))m,
\tag{23}
\]

which is impossible for every `r>=1`.

Thus

\[
\boxed{
\text{a full symmetrized bow cannot be screened at all interior reciprocal harmonics}
\\
\text{by critical-line zeros from the same bow interval alone.}
}
\tag{24}
\]

The quantitative fractional version is also immediate. If

\[
M=(\kappa+o(1))m,
\qquad \kappa>0,
\tag{25}
\]

then local critical-line-only screening with `o(m)` error forces

\[
\boxed{2r\kappa\le d-2.}
\tag{26}
\]

Since `d-2<=r-1`,

\[
\kappa\le\frac{d-2}{2r}
\le\frac{r-1}{2r}<\frac12.
\tag{27}
\]

Near the count-saturating spacing `d=2`, the allowable fraction tends to zero. The exact Maynard--Pratt bow has `\kappa->1`, so it lies far outside the positive-screening feasibility region.

## 4. What kind of cancellation can still survive

The conclusion is intentionally about the **type** of the uncertified complement, not merely its size. A critical-line zero contributes a unit-circle phase and positive multiplicity, so all such local contributions are governed by the positive trigonometric moment constraint (12). This includes multiple zeros on the critical line: multiplicity increases `C_0` and cannot create an indefinite direction.

An additional off-line functional-equation pair is different. Its `k`-th reciprocal amplitude is

\[
2\cosh(b\alpha_k)z^k,
\tag{28}
\]

so the harmonic weights vary with `k`. The resulting sequence is not the moment sequence of one fixed positive measure on the unit circle. That is precisely where the Fejer argument can fail. In matrix language, this is not an accident: a genuinely off-line pair is the indefinite block type that the `weil_inertia` line is trying to charge.

Accordingly (24) gives a genuine defect-to-defect alternative. If a later source/localization theorem forces the selected bow amplitude to be cancelled locally at all reciprocal harmonics, then the local reservoir cannot be made entirely from RH-compatible critical-line zeros. It must contain **additional off-line mass** (or else the cancellation must come from outside the localized zero population or from another source-side term). Screening a dense off-line bow would therefore force fresh horizontal defect rather than allowing critical-line multiplicity to absorb it for free.

This is the first point in the current bow chain where multiple reciprocal harmonics produce a count-amplification factor rather than another scalar visibility estimate. It is also why one harmonic alone is qualitatively weaker: at a single frequency, a positive population can always oppose a selected phase if enough mass is available. Requiring the same positive population to realize `r` consecutive negative moments costs a factor `r`, with the sharp extremizer given by the nontrivial `(r+1)`-st roots of unity.

## 5. Relation to WI-209 and the accepted distinguished-twist clue

WI-209 proves that the selected symmetrized bow residue at the first reciprocal scale is not a bounded-packet signal: on the matching Gallagher slab it is `Omega(log T)` above the raw-prime diagonal in energy for a positive-density bow. Therefore any diagonal-scale bound for the **full** source error would force a complementary vector almost antiparallel to the selected bow vector.

The present finding does not prove such a source bound, and it does not silently replace the one distinguished twist in the accepted clue by `r` already-controlled twists. Its role is to identify what would happen if the localization step were strengthened to the finite family of reciprocal scales

\[
\alpha_k=\frac{k}{d_T},
\qquad 1\le k<d_T.
\tag{29}
\]

All of these frequencies are strictly inside support one. The selected mirror pairs align at every one of them by the same exact arithmetic-spacing identity, but a local critical-line population cannot align oppositely at all of them without violating the local zero-count budget.

Thus the next useful source-side target can be made more specific than “control the complement”: obtain simultaneous source-fixed localization at two or more reciprocal harmonics, or prove that the complementary contribution required by WI-209 is itself local enough that the positive moment budget applies. Either result would turn (24) into an actual bootstrap on off-line mass.

The accepted `CLUE-bow-distinguished-twist-offdiagonal-cancellation` remains unresolved because current arithmetic input still permits cancellation from remote zeros and from the structured `Lambda^sharp`/prime-side component at the distinguished scale. This finding narrows the reservoir but does not supply the missing pointwise source theorem.

## 6. Boundaries and stress tests

Several exclusions are load-bearing.

First, (24) is **local**. Zeros outside the bow interval are not constrained by the excess count (19). A global form-factor square can mix them with the selected bow before taking absolute values, and WI-184 already identifies this extraction problem. No claim is made that remote zeros cannot screen the bow.

Second, the result excludes only a critical-line-only local reservoir. Additional off-line pairs are exactly the escape hatch. Their depth-dependent `cosh(kb/d_T)` weights destroy the fixed positive-unit-circle moment structure; ruling out that escape is a further problem, not something hidden in (12).

Third, all reciprocal harmonics used here are strictly inside support one. The endpoint is never counted. At integer `d_T`, `r_T=d_T-1`; at noninteger `d_T`, `r_T=floor(d_T)`. Therefore no endpoint continuity or wider-Fourier-support assumption enters the theorem.

Fourth, exact arithmetic spacing is used for the clean identity (5). A near-arithmetic bow can be treated perturbatively if the phase errors at all selected harmonics are `o(1)`; then those errors join the `epsilon` term in (15). This finding does not claim such phase control for an arbitrary nonperiodic exceptional configuration.

Fifth, the argument does not use the truth of the Maynard--Pratt bow as a zeta configuration. It says that **if** a source-compatible bow of that form occurs, its local RH-compatible reservoir cannot perform the indicated multi-harmonic screening. The actual existence of such bows remains an adversarial model, not an established property of zeta zeros.

Finally, no unconditional simple-critical-zero proportion changes here. The canonical research objective is stronger: eliminate every off-line zero. The value of (24) is that it converts one piece of the complement from an unconstrained cancellation reservoir into a quantitatively insufficient one and identifies the precise remaining defect-bearing escape.

## 7. Prior-art and novelty audit

The ingredients are separated by provenance.

- **Literature-backed geometry and count:** the Maynard--Pratt bow is prior art; functional-equation reflection and Riemann--von Mangoldt are classical. WI-184 already combines them to obtain `d_T>=2-o(1)`, the excess count `(d_T-2+o(1))m`, and the first reciprocal coherent amplitude.
- **Classical identity:** positivity of (12), or equivalently positive semidefiniteness of Toeplitz moment matrices for positive measures on the unit circle, is classical Fejer/Caratheodory trigonometric moment theory. No novelty is claimed for that lemma or for its sharp roots-of-unity extremizer.
- **Existing Mathia input:** WI-209 establishes that the positive-density symmetrized bow packet is genuinely large on the reciprocal Gallagher slab and quantifies the near-opposite complement required by any diagonal-scale source theorem.
- **New exact deduction here:** equations (13)--(27), especially the `2rM` positive-screening mass requirement and its contradiction with the Riemann--von Mangoldt local excess budget across all strictly interior reciprocal harmonics.

A bounded prior-art audit around Fejer/Caratheodory trigonometric moment constraints, Toeplitz positive measures, zeta zeros in arithmetic progressions, reciprocal/Bragg harmonics, and Maynard--Pratt bows found the classical moment machinery and the known nonperiodicity literature for exact infinite zeta-zero arithmetic progressions, but no source formulating the local multi-harmonic cancellation/count obstruction above. Absence from that search is not used as a priority claim.

## Research consequence

The bow program should not try to use the compulsory critical-line reservoir as a generic explanation for the cancellation demanded by WI-209. At one frequency it remains a possible reservoir; across the full interior reciprocal packet it is provably too small by a linear factor. The useful next step is therefore a **multi-harmonic localization theorem** or a source identity that couples the distinguished reciprocal scale to at least one additional reciprocal harmonic without absoluteizing the signed complement.

If such localization can be obtained, (24) immediately promotes screening into new off-line mass. The subsequent bootstrap question is then concrete: determine whether those newly forced off-line pairs can themselves provide the required radial moment sequence without exhausting the same Riemann--von Mangoldt count budget or violating an independent zero-density/source constraint. That iteration is not proved here, but its first coercive step is now exact and falsifiable.