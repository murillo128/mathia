# WI-041 — MRT endpoint stability gives maximal interval `L^2`, isolating the sparse-coefficient loss in welding

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. In the Matomäki--Radziwiłł--Tao long-shift range, the almost-all twin-prime correlation estimate can be upgraded, with only logarithmic losses, to an `L^2` estimate that is **maximal over the summation interval**. Consequently, the `n`-dependent interval selector inside the public Yang--Yang welding weight is not by itself a new arithmetic obstruction: after the exact dispersion swap it can be dominated by this maximal shifted-prime deviation.

The calculation also identifies what this upgrade does **not** provide. On a single sparse progression of shifts `h=rk`, the unweighted MRT `L^2` budget is naturally of size `H`, where `H` is the full physical shift span, not `H/r`. Thus an argument that needs density-normalized control on each large-`r` progression can still lose a factor `sqrt(r)` after Cauchy--Schwarz. Removing that loss requires either the global structured aggregation/outer weights to absorb it, or genuinely stronger information on how correlation-error energy is distributed among residue classes. This sharpens the welding gate left by WI-037--WI-040; it does **not** prove the Yang one-sided fourth-moment theorem and does not change Mathia's current unconditional simple-critical proportion.

## 1. Primary source boundary

The arithmetic input is Kaisa Matomäki, Maksym Radziwiłł and Terence Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. London Math. Soc. 118 (2019), 284--350, arXiv:1707.01315. Put

\[
\sigma=\frac{8}{33}.
\]

For fixed `epsilon>0` and every `A>0`, their Theorem 1.3(i) gives the Hardy--Littlewood asymptotic

\[
\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)
=\mathfrak S(h)X+O_{A,\varepsilon}(X\log^{-A}X)
\tag{1}
\]

for all but `O_{A,epsilon}(H log^{-A} X)` shifts in a movable interval of length `O(H)`, provided

\[
X^{\sigma+\varepsilon}\le H\le X^{1-\varepsilon},
\qquad h_0\le X^{1-\varepsilon}.
\tag{2}
\]

WI-034 already checked that the almost-all statement implies the corresponding hard-window unweighted `L^2` estimate by a good/bad-shift split.

Two additional pieces of the **primary paper** matter here.

1. In the introduction MRT explicitly state that one may work with `1<=n<=X`, rather than `X<n<=2X`, for the prime and divisor correlations "with only minor changes to the arguments below". Thus the same method supplies the prefix form needed below, at the same exponent `8/33` after shrinking the fixed epsilon margin if necessary.
2. Corollary 2.5 is an arbitrary-interval truncation lemma for Dirichlet series. Later, in the proof of the minor-arc Proposition 5.4, the authors write every Type `d_j` / Type II piece as `f' 1_(X/q0,2X/q0]` and explicitly **remove that truncation using Corollary 2.5** before applying the mean-value machinery. This is independent source-level evidence that endpoint truncation is not a load-bearing part of the `8/33` argument; it costs logarithms rather than a new power of `X`.

Primary sources:

- https://arxiv.org/abs/1707.01315
- https://www.math.mcgill.ca/radziwill/correlations.pdf

The use of the prefix variant below is therefore `LITERATURE+DERIVED`, not a claim that MRT print the maximal theorem verbatim.

## 2. Maximal interval `L^2` estimate

For a nonzero shift `h` and an interval `I=(u,v]\subset[X,2X]`, define

\[
D_I(h)
:=
\sum_{n\in I}\Lambda(n)\Lambda(n+h)
-\mathfrak S(h)|I|,
\tag{3}
\]

and

\[
M_X(h):=\sup_{I\subset[X,2X]}|D_I(h)|.
\tag{4}
\]

The derived claim is that, under (2), for every fixed `A>0`,

\[
\boxed{
\sum_{|h-h_0|\le H\atop h\ne0} M_X(h)^2
\ll_{A,\varepsilon}
H X^2(\log X)^{-A}.
}
\tag{5}
\]

The proof only uses the prefix version of MRT plus a polylogarithmic endpoint net.

### Prefix net

Let

\[
P_Y(h)
=
\sum_{n\le Y}\Lambda(n)\Lambda(n+h)
-\mathfrak S(h)Y.
\tag{6}
\]

Fix the desired exponent `A` and take, for definiteness,

\[
B=A+5,
\qquad
C=2A+10.
\tag{7}
\]

Place a grid on `[X,2X]` with mesh

\[
\Delta\le X(\log X)^{-B}
\tag{8}
\]

and `J=O((log X)^B)` grid endpoints `x_j`. Apply the prefix form of MRT at every `x_j`, with exponent `C` and a slightly smaller fixed epsilon margin. Since every `x_j` is comparable with `X`, the same physical `H` lies in the permitted range for all endpoints once `X` is large.

For each endpoint, at most

\[
O(H(\log X)^{-C})
\]

shifts are bad. A union bound over the `J` endpoints therefore leaves a common bad set of size

\[
O\!\left(H(\log X)^{B-C}\right).
\tag{9}
\]

For every common-good shift,

\[
\max_j |P_{x_j}(h)|
\ll X(\log X)^{-C}.
\tag{10}
\]

Hence every grid-aligned interval has deviation `O(X log^{-C} X)` by subtracting two prefixes.

### From the net to arbitrary endpoints

Approximate arbitrary `u,v` by grid endpoints. The symmetric difference has total length `O(Delta)`. Pointwise,

\[
\Lambda(n)\Lambda(n+h)\ll (\log X)^2,
\]

while the classical singular-series formula gives `mathfrak S(h) << log log(3|h|)` for nonzero `|h|\ll X`. Therefore moving the two endpoints changes (3) by at most

\[
O\!\left(\Delta(\log X)^2\right)
=
O\!\left(X(\log X)^{2-B}\right).
\tag{11}
\]

Thus on the common-good set

\[
M_X(h)
\ll
X\left((\log X)^{-C}+(\log X)^{2-B}\right).
\tag{12}
\]

On the common-bad set the crude bound

\[
M_X(h)\ll X(\log X)^2
\tag{13}
\]

is enough. Combining (9), (12), and (13),

\[
\begin{aligned}
\sum_h M_X(h)^2
&\ll HX^2\left(
(\log X)^{-2C}
+(\log X)^{4-2B}
+(\log X)^{B-C+4}
\right)\\
&\ll HX^2(\log X)^{-A},
\end{aligned}
\tag{14}
\]

because with (7) the last two exponents are `-2A-6` and `-A-1`. The possible shift `h=0` may be omitted; even a crude treatment of that single shift is negligible compared with `H`, since `H` is a fixed positive power of `X`.

This proves (5) conditional only on the endpoint-stable/prefix reading of the primary MRT theorem, which is the remaining source-audit point stated in Section 7.

## 3. The Yang moving welding interval falls inside this maximal theorem

The pinned public Yang--Yang source is

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

Its exact finite dispersion-swap code fixes

\[
g=(b_1,b_2),
\qquad
r=b_1/g,
\qquad
q=b_2/g,
\tag{15}
\]

and rewrites outer pairs as

\[
m'=m-rk,
\qquad
n'=n-qk.
\tag{16}
\]

The printed analytic welding weight is

\[
w_k(n)=\sum_{m\in I(n)}\Lambda(m)\Lambda(m-rk).
\tag{17}
\]

The public `t2_swaps.py` makes the geometry of `I(n)` explicit. For fixed `n,k`, admissible `m` must simultaneously satisfy the original `m` interval, the translated condition `m-rk` in the same interval, and the strip

\[
0<|b_1n-b_2m|\le J.
\tag{18}
\]

The first two constraints intersect to an interval; the closed strip in (18) intersects it with another interval, and deleting the exact diagonal `b_1n=b_2m` removes at most one integer. Therefore the actual selector is an interval with at most one point deleted, equivalently a union of at most two intervals. This is an exact geometric fact about the public swap, not an analytic assumption.

Consequently, after subtracting the Hardy--Littlewood main term,

\[
\left|
w_k(n)-\mathfrak S(rk)|I(n)|
\right|
\le 2M_X(rk)+O((\log X)^2),
\tag{19}
\]

with the harmless factor `2` accounting for the possible split at the excluded diagonal. Thus **the moving endpoint dependence itself is controlled by the maximal MRT norm (5)**. One does not need a generic theorem saying that an arbitrary divisor-bounded coefficient preserves minor-arc cancellation merely to handle this selector.

This narrows WI-037: its divisor-bounded counterexample still blocks a generic weighted-MRT shortcut, but the specific moving-window component of the public welding coefficient has additional structure that is exploitable.

## 4. Exact remaining loss: sparse sampling of the shift norm

The maximal theorem does not automatically solve welding for large reduced coefficient `r`. Suppose a structured family uses

\[
h=rk,
\qquad 1\le k\le K,
\qquad H\asymp rK.
\tag{20}
\]

From (5) alone one gets only

\[
\boxed{
\sum_{k\le K}M_X(rk)^2
\le
\sum_{|h|\le H}M_X(h)^2
\ll HX^2(\log X)^{-A}
\asymp rKX^2(\log X)^{-A}.
}
\tag{21}
\]

There is no `1/r` density gain in (21). That gain cannot be recovered from an unweighted `L^2` bound by abstract manipulation: all of the allowed error energy could, in principle, be concentrated on one residue class modulo `r`. A density-normalized estimate

\[
\sum_{k\le K}M_X(rk)^2
\ll KX^2(\log X)^{-A}
\tag{22}
\]

would therefore be genuinely stronger information about the distribution of the deviations among arithmetic progressions of shifts.

If one now applies Cauchy--Schwarz in `k`, the first factor supplied by (21) is

\[
\left(\sum_{k\le K}M_X(rk)^2\right)^{1/2}
\ll
X\sqrt{rK}(\log X)^{-A/2},
\tag{23}
\]

rather than the density-normalized `X sqrt(K)`. This is the precise `sqrt(r)` pressure behind the large-coefficient issue. Since WI-039--WI-040 show that `r` can be a genuine power-sized reduced coefficient and cannot be removed by a unimodular reparametrization, no fixed logarithmic saving can absorb that factor **if the consumer needs (22) progression by progression**.

This is an information boundary, not a proof that the full Yang aggregation fails. WI-034 already proves the different global statement

\[
\sum_{r\in\mathcal R}\sum_{k\le H/r}|D(rk)|^2
\ll HX^2(\log X)^{-A}
\tag{24}
\]

for a structured set whose multiplicity is divisor-bounded. The final welding ledger may be normalized so that the `H`-scale in (24), together with the outer `b_1,b_2` weights, is exactly what is required. That normalization has not yet been reconstructed end to end. What (21)--(23) rule out is silently replacing (24) by the stronger per-progression density law (22).

## 5. Relation to WI-037--WI-040

The earlier findings isolated apparently competing failure modes:

- WI-037: divisor-boundedness alone cannot carry minor-arc cancellation through the welding weight;
- WI-038: the Gallagher collar and two-modulus major-arc compatibility are automatic on the MRT-covered zone;
- WI-039: generic higher-uniformity transference has a fixed-coefficient hypothesis incompatible with power-sized reduced `r,q`;
- WI-040: a unimodular change of variables cannot make both reduced coefficients small.

The present result separates the endpoint issue from the coefficient issue:

\[
\boxed{
\text{moving interval selector}
\xrightarrow[\text{polylog loss}]{\text{MRT prefix + endpoint net}}
\text{maximal }L^2,
}
\tag{25}
\]

but

\[
\boxed{
\text{maximal unweighted }L^2
\not\Rightarrow
\text{density-normalized }L^2\text{ on }h=rk
}
\tag{26}
\]

without additional structure. Thus the next load-bearing question is no longer whether the moving boundary destroys MRT. It is whether the **actual outer weighted dispersion normalization** consumes the global `H`-budget of (24), or whether it implicitly requires the stronger progression-wise budget (22).

## 6. Prior-art and novelty audit

No novelty is claimed for MRT's almost-all shifted-prime theorem, the prefix-range remark, Corollary 2.5, endpoint discretization, union bounds, or maximalization by a polylogarithmic net. A targeted search for maximal inequalities found nearby literature on maximal prime averages and on primes in short intervals/progressions, but no primary source was located that states exactly (5) for the MRT twin-prime deviation. This absence is **not** used as a priority claim.

The durable contribution here is the audit-level combination specific to the Yang welding interface:

1. extract a uniform maximal interval norm from the endpoint-stable MRT proof with an explicit logarithmic budget;
2. verify from the public swap geometry that the `n`-dependent welding selector is a union of at most two intervals, so it lies inside that norm;
3. identify the exact `H` versus `H/r` information loss that remains after maximalization;
4. separate that loss from both the generic divisor-bound obstruction of WI-037 and the fixed-coefficient Gowers obstruction of WI-039--WI-040.

No claim of priority is made for this organization or for the elementary sparse-sampling observation.

## 7. Decisive audit / falsification tests

Narrow or withdraw the maximal statement (5) if the source-level endpoint bridge fails any of the following checks.

1. Re-run the proof of MRT Theorem 1.3(i) with the prefix cutoff `1_[1,Y]` uniformly for `Y in [X,2X]`, retaining the arbitrary logarithmic saving and movable `h_0`; the introductory "minor changes" sentence must not hide a power loss.
2. Alternatively, propagate Corollary 2.5 through the exact Proposition 5.4 / circle-method proof with arbitrary endpoints and verify that all introduced losses are logarithmic and uniform over the `O(log^B X)` endpoint net.
3. Verify that after shrinking `epsilon` by a fixed factor, the same `H` satisfies the MRT lower/upper range at every grid endpoint `Y comparable to X`.
4. In the Yang swap, verify for every retained covered cell that the coefficient called `I(n)` has no hidden `n`-dependent arithmetic weight beyond the interval/strip selector. A bounded union of intervals is covered; an additional oscillatory or congruence weight is not.
5. Reconstruct the final outer `b_1,b_2,k` normalization. If its Cauchy--Schwarz step requires (22) rather than the global structured budget (24), the remaining coefficient wall is genuine; if the weights consume (24) directly, this finding removes the moving-window gate and the proof audit should proceed to the next remainder interface.

## 8. Consequence for `weil_inertia`

This finding does not promote the Yang `0.6916` candidate and does not alter the exact support-one bound already stored in Mathia. It does, however, change the most useful next audit target. The welding problem should no longer be treated as one undifferentiated "weighted minor arc" obstacle. The moving interval can be maximalized with classical MRT technology; the unresolved arithmetic content is concentrated in the **sparse large-coefficient/outer-family normalization** and any non-interval weights that survive the exact swap.

A successful audit showing that the public dispersion ledger consumes the global budget (24) without asking for progression-wise (22) would close a substantial part of WI-037's remaining gate using only established long-shift technology. Conversely, an unavoidable need for (22) would turn the `sqrt(r)` loss into a precise analytic barrier requiring new residue-class energy information rather than another reformulation of the existing MRT estimate.