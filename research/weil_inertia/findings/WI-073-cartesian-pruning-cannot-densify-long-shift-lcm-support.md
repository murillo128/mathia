# WI-073 — Cartesian pruning cannot densify the long-shift Yang support without paying a power

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + DECISIVE-NEGATIVE`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It strengthens the geometric obstruction in WI-071--WI-072. WI-071 showed that, after the coefficient-free change of variables

\[
(h_1,h_2)=(rk,qk),\qquad (r,q)=1,
\]

the complete changing-slope Yang support is contained in an `lcm`-sublevel set and has density `O((log X)^2/X)` in the full free-shift square. WI-072 then showed that any source-agnostic fixed-`L^p` restriction from that ambient square pays a power of this sparsity. A remaining cheap escape was to ask whether one could first prune the two shift coordinates separately to much better one-dimensional sets `A_1,A_2`, and only then invoke a bounded-coefficient theorem on the Cartesian product `A_1 x A_2`.

That escape is also blocked on every genuine long-shift dyadic shell. The exact Yang map gives

\[
\gcd(|h_1|,|h_2|)=|k|.
\]

Hence a shell `|k|\asymp K` is a **large-GCD relation** inside a product of shift intervals of lengths/scales `X_1\asymp RK` and `X_2\asymp QK`. Green--Walker's peer-reviewed extremal GCD theorem implies that if `A_i` occupy relative densities `alpha_i` in those coordinate intervals and a proportion `delta` of `A_1 x A_2` lies on the Yang envelope, then for every fixed `epsilon>0`,

\[
\boxed{
\delta
\ll_{\varepsilon}
(\alpha_1\alpha_2)^{-1/(2+\varepsilon)}
K^{-2/(2+\varepsilon)}.
}
\]

In particular, if both coordinate prunings retain `K^{-o(1)}` density, then

\[
\boxed{\delta\le K^{-1+o(1)}.}
\]

Thus on every long-shift interior with `K\ge X^{\kappa}` for fixed `\kappa>0`, no Cartesian product built from two subpolynomially dense coordinate sets can turn the Yang source into a positive-density bounded-coefficient shift family. Haozhe Gou's 2026 LCM extremal theorem gives the same conclusion directly from `lcm(h_1,h_2)\ll RQK`, with the slightly cleaner form `delta \ll (alpha_1 alpha_2)^(-1/2) K^{-1} L^{epsilon/2}`. The program consequence is therefore robust under arbitrary **separate coordinate pruning**: escaping WI-071 requires non-Cartesian incidence/divisor structure, source-correlated arithmetic cancellation, the multivariate polynomial representation of WI-070, or another theorem normalized to the actual Yang support.

## 1. Exact Yang shell is simultaneously an lcm and a large-gcd relation

The pinned public source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

As reconstructed in WI-069 and WI-071, for fixed prime-power bases `b_1,b_2`, write

\[
g=(b_1,b_2),\qquad r=b_1/g,\qquad q=b_2/g,
\tag{1}
\]

so `(r,q)=1`. The equal-lock swap is exactly

\[
m'=m-rk,\qquad n'=n-qk,
\tag{2}
\]

and the physical shifted-prime separations are

\[
\boxed{h_1=rk,\qquad h_2=qk.}
\tag{3}
\]

Because `(r,q)=1`,

\[
\boxed{
\gcd(|h_1|,|h_2|)=|k|,
\qquad
\operatorname{lcm}(|h_1|,|h_2|)=rq|k|.
}
\tag{4}
\]

WI-071 used the second identity and the source windows to obtain `rq|k|\ll X`. For the present purpose the first identity is equally important.

Take a dyadic source shell

\[
r\asymp R,\qquad q\asymp Q,\qquad |k|\asymp K.
\tag{5}
\]

After splitting the harmless factor-four ranges into `O(1)` ordinary dyadic intervals, the absolute shifts lie in boxes

\[
|h_1|\in[X_1,2X_1],\qquad
|h_2|\in[X_2,2X_2],
\tag{6}
\]

with

\[
X_1\asymp RK,\qquad X_2\asymp QK.
\tag{7}
\]

Every actual Yang pair in this shell satisfies

\[
\gcd(|h_1|,|h_2|)\ge cK
\tag{8}
\]

for an absolute shell constant `c>0`, and also

\[
\operatorname{lcm}(|h_1|,|h_2|)\le C RQK.
\tag{9}
\]

Signs contribute only `O(1)` quadrants and play no role in the density estimate. The actual prime/prime-power base restrictions can only make the support smaller than the arithmetic envelopes (8)--(9).

## 2. Green--Walker forbids a dense Cartesian reboxing

Ben Green and Aled Walker proved the following theorem in **Extremal problems for GCDs**, *Combinatorics, Probability and Computing* 30 (2021), 922--929, DOI `10.1017/S0963548321000092`, arXiv:2012.02078:

if

\[
A\subset[X,2X],\qquad B\subset[Y,2Y]
\]

and at least a proportion `delta` of the pairs in `A x B` satisfy

\[
\gcd(a,b)\ge D,
\]

then for every fixed `epsilon>0`,

\[
\boxed{
|A||B|
\ll_{\varepsilon}
\delta^{-2-\varepsilon}
\frac{XY}{D^2}.
}
\tag{10}
\]

This is established peer-reviewed prior art; no novelty is claimed for (10).

Now let `A_1,A_2` be **arbitrary** coordinate prunings of one box (6), and write

\[
|A_1|=\alpha_1 X_1,
\qquad
|A_2|=\alpha_2 X_2
\tag{11}
\]

up to harmless endpoint constants. Suppose a proportion `delta` of `A_1 x A_2` belongs even to the enlarged Yang large-GCD envelope (8). Apply (10) with `D=cK`. Then

\[
\alpha_1\alpha_2 X_1X_2
\ll_{\varepsilon}
\delta^{-2-\varepsilon}
\frac{X_1X_2}{K^2},
\tag{12}
\]

so cancellation of the coordinate scales gives

\[
\boxed{
\delta^{2+\varepsilon}
\ll_{\varepsilon}
\frac{1}{\alpha_1\alpha_2 K^2},
}
\tag{13}
\]

and hence

\[
\boxed{
\delta
\ll_{\varepsilon}
(\alpha_1\alpha_2)^{-1/(2+\varepsilon)}
K^{-2/(2+\varepsilon)}.
}
\tag{14}
\]

This estimate is independent of `R` and `Q`. The power-sized reduced bases that caused the coefficient wall have disappeared from the theorem interface, but the exact common factor `k=gcd(h_1,h_2)` restores the same long-shift sparsity as an extremal GCD obstruction.

If

\[
\alpha_1,\alpha_2=K^{-o(1)},
\tag{15}
\]

then for arbitrarily small fixed `epsilon`, (14) gives

\[
\boxed{\delta=K^{-1+o(1)}.}
\tag{16}
\]

Consequently, on a source region with `K\ge X^\kappa`, any coordinate-wise pruning that keeps only subpolynomial losses still leaves the Yang relation power-sparse.

## 3. Direct LCM formulation gives the same conservation law

A recent independent formulation is Haozhe Gou, **Extremal Problems for GCDs and LCMs in Higher Dimensions**, arXiv:2604.21122v1 (22 Apr 2026). Theorem 1.5 states that for `A_i subset [X_i,2X_i]`, if a proportion `delta` of the `k`-fold Cartesian product has least common multiple at most `L`, then

\[
\prod_i|A_i|
\ll_{k,\varepsilon}
\delta^{-k/(k-1)}
\frac{L^{k/(k-1)+\varepsilon}}
{(\prod_iX_i)^{1/(k-1)}}.
\tag{17}
\]

For `k=2`,

\[
\boxed{
|A_1||A_2|
\ll_{\varepsilon}
\delta^{-2}
\frac{L^{2+\varepsilon}}{X_1X_2}.
}
\tag{18}
\]

Gou's paper is a recent preprint rather than the evidence tier of Green--Walker's published theorem. However, the `k=2` LCM bound is also easy to reconstruct directly: if `d_A(l)` counts divisors of `l` belonging to `A`, then

\[
\delta|A_1||A_2|
\le
\sum_{l\le L}d_{A_1}(l)d_{A_2}(l),
\tag{19}
\]

Cauchy--Schwarz and the classical divisor bound give

\[
\sum_{l\le L}d_A(l)^2
\ll_{\eta}
L^{1+\eta}X^{-1}|A|,
\tag{20}
\]

because `max_{l<=L} d_A(l) <= tau(l) <<_eta L^eta` and

\[
\sum_{l\le L}d_A(l)
=
\sum_{a\in A}\left\lfloor\frac La\right\rfloor
\ll \frac LX|A|.
\tag{21}
\]

Squaring (19) after Cauchy proves (18), after renaming `2 eta` as `epsilon`. Thus the program consequence does not depend on trusting an opaque numerical or analytic step in the new preprint.

Insert the Yang scales

\[
L\asymp RQK,
\qquad
X_1X_2\asymp RQK^2,
\tag{22}
\]

and (11) into (18). One obtains

\[
\boxed{
\delta
\ll_{\varepsilon}
(\alpha_1\alpha_2)^{-1/2}
K^{-1}L^{\varepsilon/2}.
}
\tag{23}
\]

For every fixed long-shift exponent one may choose `epsilon` sufficiently small, recovering (16) in the usual `X^{o(1)}` form. This is exactly the LCM-side version of the Green--Walker large-GCD argument.

## 4. What this closes beyond WI-071 and WI-072

WI-071 counted the complete all-integer LCM envelope inside the **full** free-shift rectangle and found density `O(1/K)` on a dyadic long-shift block. That left a representation-level question: perhaps the full rectangle was simply a poor ambient set, and one could choose special one-dimensional coordinate sets whose product was already concentrated on the source relation.

Equations (14)--(16) answer that question. The `1/K` density is not an artifact of filling the coordinate axes with irrelevant integers. It persists, up to subpower losses, for **every Cartesian product whose two coordinate sets themselves retain subpolynomial density** in the natural shift ranges.

WI-072 then converts this geometric density into the exact fixed-`L^p` selector cost. Combining the two findings gives a stronger no-go:

\[
\boxed{
\begin{array}{c}
\text{large Cartesian coordinate pruning}\\
+\text{ambient fixed-}L^p\text{ control with only logarithmic saving}\\
\not\Longrightarrow\\
\text{source-normalized Yang covariance control}
\end{array}}
\tag{24}
\]

on a genuine long-shift shell. One cannot evade the fixed-`L^p` power penalty merely by choosing smarter sets of allowed `h_1` and `h_2` separately.

There is a complementary way to state the conservation law. To make `delta` order one in (14), the product density `alpha_1 alpha_2` itself must be power-small, of order at most roughly `K^{-2+o(1)}`. The apparent gain in source density is then paid back by selecting a power-small Cartesian ambient family before any prime theorem is applied.

## 5. Prior-art and novelty boundary

No novelty is claimed for Green--Walker's theorem, the identity `gcd(a,b) lcm(a,b)=ab`, dyadic decomposition, divisor counting, Cauchy--Schwarz, or Gou's general LCM theorem. Green--Walker is the authoritative published source for the load-bearing two-dimensional extremal statement. Gou is recent prior art for the direct LCM formulation and explicitly notes that the two-dimensional LCM problem reduces to Green--Walker; its Theorem 1.5 supplies a direct counting proof with an `L^epsilon` loss.

A bounded search around sparse-modulus large sieves, GCD/LCM extremal sets, and directional lattice averages also located general sparse-large-sieve and directional harmonic-analysis literature, but no theorem whose printed interface estimates the Yang four-prime covariance on the weighted LCM incidence set itself. That negative search is not used as novelty or impossibility evidence.

The durable Mathia deduction is only the source-specific specialization: the exact Yang change of variables makes every long-shift shell a large-GCD/low-LCM incidence relation, so extremal GCD/LCM theory proves that **all large Cartesian reboxings remain power-sparse**. This closes one representation shortcut left open by WI-071--WI-072; it does not claim priority for the extremal theorem.

Primary references:

- Ben Green and Aled Walker, *Extremal problems for GCDs*, Combinatorics, Probability and Computing 30:6 (2021), 922--929, DOI `10.1017/S0963548321000092`, arXiv:2012.02078.
- Haozhe Gou, *Extremal Problems for GCDs and LCMs in Higher Dimensions*, arXiv:2604.21122v1, 22 Apr 2026, especially Theorem 1.5 and its direct counting proof.

## 6. Boundary conditions and falsification gates

This finding is deliberately narrower than a no-go for the Yang route.

1. **Short-shift boundary.** If `K=X^{o(1)}` or `K=O(1)`, (16) is not a power barrier. This is the same boundary regime already separated in WI-071.
2. **Power-small coordinate sets.** The theorem does not prevent choosing `A_1,A_2` so thin that `alpha_1 alpha_2` already pays the required power. It says such pruning is not a free densification.
3. **Non-Cartesian supports.** A theorem normalized directly to the incidence relation `gcd(h_1,h_2)\asymp K` / `lcm(h_1,h_2)\ll RQK`, a divisor-fiber decomposition, or a source-adapted large sieve can use structure not represented by `A_1 x A_2` and is outside the obstruction.
4. **Arithmetic cancellation.** Source weights may correlate favorably across the LCM/GCD fibers. Neither Green--Walker nor the counting argument controls signed prime-error cancellation.
5. **Polynomial representation.** WI-070's `(r,q,k)` representation retains source cardinality and is not Cartesian physical-shift pruning; its obstacle remains the quantitative multivariate polynomial-pattern theorem gap.
6. **Exact source identity.** A cancellation in the full Yang `S1-2S2+S3` combination could bypass the free-shift representation entirely.

Narrow or retire the program consequence if a source-faithful reparameterization produces bounded-coefficient prime forms on a product set whose coordinate densities are subpolynomially large while the source occupies positive density, contradicting the exact map (3)--(4) or one of the theorem hypotheses used above.

## 7. Consequence for `weil_inertia`

The accepted Yang locked-covariance question remains open, but the coefficient-free branch is now more sharply classified:

\[
\boxed{
\begin{array}{rcl}
\text{full free-shift box} &:& \text{power-sparse by WI-071},\\
\text{fixed finite }L^p\text{ localization} &:& \text{power cost by WI-072},\\
\text{large Cartesian reboxing} &:& \text{still power-sparse by WI-073},\\
\text{non-Cartesian lcm/gcd incidence} &:& \text{still live},\\
\text{source variables }(r,q,k) &:& \text{multivariate polynomial gap by WI-070}.
\end{array}}
\tag{25}
\]

Further work on the free-shift representation should therefore target genuinely incidence-aware arithmetic information rather than another ambient rectangle or separate coordinate thinning. A successful result now has to exploit what WI-073 intentionally discards: divisor/GCD fiber structure, source weights, prime-error orthogonality, or a theorem stated directly on the Yang incidence set.