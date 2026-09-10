# MC-203 — One-sign symmetric support interactions collapse to the same conditioned principal carrier

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `DECISIVE-NEGATIVE`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-200` found a quadratic source bridge by retaining the square-free support field beside the signed Möbius field, `MC-201` showed that its centered support covariance is already harmless at the RH scale for a sufficiently small logarithmic primorial, and `MC-202` closed affine support centering as an escape. A natural remaining attempt is to keep one signed factor but replace the affine support factor by a higher-order or nonlinear symmetric function of all other support sites in the same residue class.

That entire source family has an exact collapse.

Work at a complete block

\[
X=Nq,\qquad q=q_y=\prod_{p\le y}p,\qquad y=c\log X,\qquad 0<c<\tfrac12,
\tag{1}
\]

and write the source values in each reduced residue class `a mod q` as

\[
x_{a,i}\in\{-1,0,1\},\qquad 1\le i\le N.
\tag{2}
\]

Put

\[
A_a=\sum_i x_{a,i},\qquad B_a=\sum_i x_{a,i}^2,
\qquad S=\sum_aA_a,
\qquad u_a=A_a-\frac S\phi,
\tag{3}
\]

where `phi=phi(q)`. Let `F:{0,1,...,N-1}->C` be arbitrary and define the one-sign, support-symmetric source statistic

\[
T_F:=\sum_a\sum_{i=1}^N
x_{a,i}
F\!\left(\sum_{j\ne i}x_{a,j}^2\right).
\tag{4}
\]

Then, with no analytic hypothesis,

\[
\boxed{
T_F=\sum_a A_aF(B_a-1).
}
\tag{5}
\]

If

\[
w_a:=F(B_a-1),\qquad
\bar w:=\frac1\phi\sum_aw_a,
\tag{6}
\]

then

\[
\boxed{
T_F=\bar w S+\sum_a u_a(w_a-\bar w).
}
\tag{7}
\]

Thus arbitrary nonlinear **permutation-symmetric processing of the other support bits does not create a third signed channel**. With exactly one signed source factor, it can only assign a support-determined scalar weight to the class sum `A_a`, after which the same principal/transverse decomposition reappears. If `bar w=0`, the statistic loses the linear principal coefficient exactly; if `bar w!=0`, it has the exact decoder

\[
S=\frac{T_F-\sum_a u_a(w_a-\bar w)}{\bar w}.
\tag{8}
\]

The most natural higher-order hierarchy makes the collapse quantitative. For integer `k>=0`, let

\[
(t)_k=t(t-1)\cdots(t-k+1),\qquad (t)_0=1,
\tag{9}
\]

and define the ordered one-sign / `k`-support interaction

\[
E_k:=
\sum_a
\sum_{\substack{i_0,i_1,\ldots,i_k\\\text{all distinct}}}
 x_{a,i_0}\prod_{r=1}^k x_{a,i_r}^2.
\tag{10}
\]

Then exactly

\[
\boxed{
E_k=\sum_a A_a(B_a-1)_k.
}
\tag{11}
\]

Set

\[
\lambda_k:=\frac1\phi\sum_a(B_a-1)_k,
\qquad
C_k:=\sum_a u_a\bigl((B_a-1)_k-\lambda_k\bigr).
\tag{12}
\]

Equation `(7)` becomes

\[
\boxed{E_k=\lambda_k S+C_k.}
\tag{13}
\]

Here `k=0` is `E_0=S`, while `k=1` is exactly the mixed source aggregate `E_{1,2}` of `MC-200`, with

\[
\lambda_1=\frac Q\phi-1,
\qquad C_1=C_{1,2}.
\tag{14}
\]

Now insert the support regularity already proved in `MC-201`:

\[
B_a=NP_y+O(\sqrt X)
\quad\text{uniformly in }a,
\qquad
P_y=\prod_{p>y}\left(1-\frac1{p^2}\right)=1-o(1).
\tag{15}
\]

For every fixed `k`, since `N=X^{1-c+o(1)}` and `sqrt(X)=o(N)`, one has uniformly

\[
(B_a-1)_k=(NP_y)^k+O_k(N^{k-1}\sqrt X),
\tag{16}
\]

hence

\[
\lambda_k=(NP_y)^k(1+o(1))
\tag{17}
\]

and

\[
\max_a\left|(B_a-1)_k-\lambda_k\right|
\ll_k N^{k-1}\sqrt X.
\tag{18}
\]

Since `|u_a|<=2N`,

\[
|C_k|\ll_k\phi N^k\sqrt X,
\tag{19}
\]

so after normalizing by the decoder coefficient,

\[
\boxed{
\frac{|C_k|}{|\lambda_k|}
\ll_k \phi\sqrt X
\le q\sqrt X
=X^{1/2+c+o(1)}.
}
\tag{20}
\]

Therefore for any target `epsilon>0`, choosing the same sufficiently small fixed `c` used in `MC-201` gives

\[
\boxed{
\frac{E_k}{\lambda_k}
=S+O_{k,\varepsilon}(X^{1/2+\varepsilon/2})
}
\tag{21}
\]

for every fixed `k`. In particular,

\[
\boxed{
\frac{E_k}{\lambda_k}
=
\frac{E_1}{\lambda_1}
+O_{k,\varepsilon}(X^{1/2+\varepsilon/2}).
}
\tag{22}
\]

So **all fixed-order one-sign/support interactions are the same target-scale carrier as the quadratic `MC-200` statistic, modulo an error already below the requested RH exponent.** Merely adding more square-free-support factors cannot improve the power budget.

The conclusion extends to slowly growing support order. If `k=k(X)` satisfies

\[
k\frac{\sqrt X}{N}=o(1),
\tag{23}
\]

then the ratio formula for falling factorials gives relative support-weight variation

\[
\frac{(B_a-1)_k}{(NP_y-1)_k}
=
1+O\!\left(k\frac{\sqrt X}{N}\right)
\tag{24}
\]

uniformly, and therefore

\[
\boxed{
\frac{|C_k|}{|\lambda_k|}
\ll k\phi\sqrt X.
}
\tag{25}
\]

Any subpower order `k=X^{o(1)}` obeys `(23)` for fixed `c<1/2` and only adds a subpower loss. Growing the number of support factors does not create a favorable new exponent; it preserves or worsens the existing conditioning budget.

No improved bound for `M(X)`, the rough sum `G_y(X)`, or the zeta zero set is claimed.

## 1. Exact collapse of an arbitrary support-symmetric kernel

For a fixed class `a`, abbreviate `x_i=x_{a,i}` and `B=B_a`. In the summand of `(4)`, if `x_i=0` then the whole term vanishes. If `x_i` is nonzero, then `x_i^2=1`, and therefore

\[
\sum_{j\ne i}x_j^2=B-1.
\tag{26}
\]

Every nonzero signed site in the class consequently receives the same coefficient `F(B-1)`. Thus

\[
\sum_i x_iF\!\left(\sum_{j\ne i}x_j^2\right)
=F(B-1)\sum_ix_i
=A_aF(B_a-1),
\tag{27}
\]

which proves `(5)`.

The hypothesis in `(4)` is exactly permutation symmetry in the support bits seen from the distinguished signed site. A symmetric function of Boolean support variables depends only on their Hamming weight, so `(4)` already represents the full class of such one-sign local kernels; polynomial degree is irrelevant.

Decomposing `A_a=S/phi+u_a` in `(5)` and using `sum_a u_a=0` proves `(7)`. This is the same principal/transverse algebra exposed for affine support centering in `MC-202`, but now the source-level reduction occurs **before** any choice of nonlinear support function.

## 2. Ordered support tuples give the complete fixed-degree hierarchy

For a distinguished nonzero site `i_0`, exactly `B_a-1` other sites in the class have square equal to one. The number of ordered `k`-tuples of distinct such sites is therefore `(B_a-1)_k`. If `x_{a,i_0}=0`, its contribution to `(10)` vanishes regardless of the other sites. Summing first over the support tuple and then over `i_0` proves `(11)`.

This makes `MC-200` the first nontrivial member of an exact hierarchy rather than an isolated quadratic coincidence. Replacing its single support factor by two, three, or any fixed number of distinct support factors changes only the scalar weight `(B_a-1)_k` applied to `A_a`.

## 3. Support flatness makes fixed order exponent-neutral

Equation `(15)` implies `B_a=NP_y+O(sqrt(X))` with `NP_y asymp N`. For fixed `k`, the falling factorial is a degree-`k` polynomial whose derivative on this range is `O_k(N^(k-1))`. The discrete mean-value bound therefore gives `(16)` and `(18)`; averaging `(16)` gives `(17)`.

The elementary class-capacity bounds

\[
|A_a|\le N,
\qquad
\frac{|S|}{\phi}\le N
\tag{28}
\]

imply `|u_a|<=2N`, and `(19)` follows by absolute summation. Dividing by `(17)` proves `(20)`.

The important cancellation is in the **conditioning ledger**, not in the source sum: adding `k` support factors enlarges the decoder coefficient from order `N` to order `N^k`, but it enlarges the worst-case transverse fluctuation by the same power `N^k`. After normalization, the factor `N^k` disappears and the residual remains `phi sqrt(X)`, exactly the scale already present at `k=1`.

For growing `k`, use

\[
\frac{(t+1)_k}{(t)_k}=\frac{t+1}{t+1-k}.
\tag{29}
\]

When `(23)` holds, all relevant `B_a` remain a distance much larger than `k` from the lower endpoint, and iterating `(29)` across an `O(sqrt(X))` support fluctuation gives `(24)`. The same absolute-sum argument then yields `(25)`. This extension is intentionally only a conditioning statement; it does not assert that large-`k` source correlations are analytically accessible.

## 4. Relation to the previous quotient and affine no-go results

This finding does not merely repeat `MC-199`. That result says centered signed data, even with the full support profile retained, cannot universally recover the deleted principal coordinate. Here the statistic starts from **uncentered source data** and therefore can retain `S`; equation `(7)` classifies exactly how it does so when there is one signed factor and the remaining within-class information is symmetric support data.

Nor is this only `MC-202` with a different notation. `MC-202` classifies affine centering inside the quadratic mixed statistic. Equation `(5)` shows that arbitrary nonlinear support processing, and in particular the entire arbitrary-order tuple hierarchy `(10)`, first collapses to a support-weighted linear statistic in `A_a`. The affine principal/transverse dichotomy then reappears at the more general level `(7)`.

The result therefore closes one explicit escape left after `MC-202`: **higher support degree by itself cannot manufacture a new target-scale channel.** A useful continuation must leave at least one hypothesis of `(4)`--`(5)`: introduce additional signed factors, retain order/site/divisor information not determined by the support Hamming weight, couple different residue classes before symmetric collapse, or use a singular/rapidly varying support functional whose own arithmetic control is genuinely new.

## 5. Prior art and novelty audit

The combinatorial mechanism behind `(5)` is classical. Permutation-symmetric functions on Boolean inputs are functions of Hamming weight, and ordered distinct tuple counts are falling factorials of that weight. The decomposition `(7)` is ordinary mean-plus-centered decomposition, adjacent to the same centered/U-statistic language already audited in `MC-202`. No novelty is claimed for symmetric Boolean functions, falling factorial moments, U-statistics, or centering as general mathematics.

On the arithmetic side, `MC-S28` already places fixed-shift products containing one Möbius factor and any fixed collection of square-free-support factors inside the established logarithmically averaged multiplicative-correlation framework when the pointwise product satisfies the required nonpretentiousness condition. `MC-200` further audits why fixed-shift/logarithmically averaged control does not pay the polynomially sparse growing-shift bill of the primorial source aggregate. The present result does not claim a new correlation theorem; it shows instead that increasing only the number of support factors does not alter the target-scale conditioning even before those analytic estimates are attempted.

A targeted external audit of symmetric Boolean/Hamming-weight reductions, U-statistic kernels, and mixed Möbius/square-free correlation language found these classical component mechanisms and no reason to reinterpret `(5)` as a new general combinatorial theorem. The durable contribution is the line-specific collapse and quantitative insertion into the current `MC-200`--`MC-202` logarithmic-primorial frontier.

## Boundaries and falsification tests

- Equation `(5)` requires exactly one distinguished signed factor and permutation symmetry in the remaining support bits within each residue class. It does not cover kernels that depend on the ordered locations of support sites, their divisor structure, or another signed factor.
- The exact algebra `(5)`--`(14)` holds for arbitrary ternary arrays and uses no Möbius cancellation, analytic continuation, or zero-free region.
- The target-scale estimates `(15)`--`(25)` use the logarithmic-primorial complete-block regime and the uniform square-free support estimate already established in `MC-201`.
- The fixed-`k` conclusion does not say that `E_k` is analytically as hard as `S` in every possible proof. It says that **support multiplicity alone supplies no improved decoder exponent**: any gain must come from a genuinely stronger estimate for the uncentered source statistic.
- A highly singular or rapidly varying `F` can amplify the small class-to-class support fluctuations and is not ruled out by `(20)`. Such a proposal must pay for that sensitivity with an independent arithmetic theorem; support flatness no longer makes its transverse part harmless automatically.
- The growing-order estimate `(25)` is asserted only under `(23)`. It is not a statement about support order approaching the full class capacity.

The core exact claim is falsified by any finite ternary array and support-symmetric kernel for which direct evaluation of `(4)` disagrees with `(5)`. The tuple specialization is falsified if a direct enumeration of ordered distinct support tuples disagrees with `(11)`. The fixed-order conditioning claim is falsified if `MC-201`'s uniform bound `(15)` fails to imply `(18)`--`(20)`.

## Consequence for the active frontier

After `MC-202`, one plausible next move was to replace the affine support factor by a richer symmetric function or simply add more square-free-support factors. That route is now classified. With one signed source factor, every permutation-symmetric support kernel collapses to a support-weighted class sum, and every fixed-order tuple member normalizes to the same rough principal carrier as `MC-200` up to an RH-scale-harmless transverse error.

The remaining mixed-source problem is therefore not a shortage of polynomial degree in the **unsigned** channel. The next viable mechanism must exploit information that the class support count `B_a` does not contain: another signed factor, ordered/divisor-sensitive source geometry, cross-class coupling before support symmetrization, or a genuinely new arithmetic theorem for a support-sensitive weight whose variation is strong enough to matter but still controllable independently of the target Mertens sum.