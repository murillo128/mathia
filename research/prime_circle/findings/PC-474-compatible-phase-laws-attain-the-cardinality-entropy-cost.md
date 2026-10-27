# PC-474 — Compatible phase laws attain the cardinality entropy cost

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE. Requiring all finite-cutoff selectors to be marginals of **one fixed probability on compatible root phases** does not increase the leading entropy cost for any finite-mean law of finite admissible supports. For a law on finitely many such supports, the optimal second-order cost and its unique attaining phase law are explicit. This is a selection boundary for the unchanged cotangent limits, using classical conditioning and information identities; it is not a geometry-forced selector, a new general entropy theorem, or an RH implication.

## 1. Fixed compatible laws, rather than cutoff-dependent recovery

Use the forbidden-residue convention of
[[research/prime_circle/findings/PC-471-compatible-root-phases-retain-full-spectrum-but-generically-collapse]]:
\[
\Omega=\prod_p(\mathbb Z/p\mathbb Z)^\times,\qquad
C(r)=\{h\in\mathbb Z:h\not\equiv r_p\pmod p\text{ for every }p\}.
\tag{1}
\]
Every support contains zero. Let `m_0` be the product of uniform probabilities on the nonzero residues; subscripts `y` denote restriction to primes `p<=y`. For a **single fixed** probability `nu` on `Omega`, write
\[
D_y(\nu)=D(\nu_y\Vert(m_0)_y).
\tag{2}
\]
The root centers are `c_y=-r mod d_y`, where `d_y=prod_(p<=y)p`; CRT makes them compatible under reduction. Uniformly distributing over any refinement lifts modulo `d_y m` preserves (2). All logarithms are natural.

Let `F_0` be the countable family of finite rooted admissible sets:
\[
F\subset\mathbb Z,\quad 0\in F,\quad
\nu_p(F):=|F\bmod p|<p\quad\text{for every prime }p.
\]
For a probability `P` on this family, put `J(P)=E_P(|F|-1)`.

**Theorem.**

1. For every `P` on `F_0` with `J(P)<infinity`, there is one probability `lambda_P` on `Omega` with `C_*lambda_P=P` and
   \[
   \lim_{y\to\infty}\frac{D_y(\lambda_P)}{\log\log y}=J(P).
   \tag{3}
   \]
   Every compatible law with the same support law has liminf at least `J(P)`. No finite Shannon entropy or bound on support diameter is required.
2. Suppose `P=sum_(j=1)^t w_j delta_(F_j)`, with distinct `F_j`, positive weights and `sum w_j=1`. Define the classical singular series
   \[
   \mathfrak S(F)=\prod_p\frac{1-\nu_p(F)/p}{(1-1/p)^{|F|}},
   \qquad H(P)=-\sum_jw_j\log w_j.
   \tag{4}
   \]
   For **every** fixed compatible law `nu` with `C_*nu=P`, let `nu_j` be its conditional law given `C(r)=F_j`. Then
   \[
   \boxed{\quad
   \lim_{y\to\infty}\left[D_y(\nu)-J(P)\log\log y\right]
   =\gamma J(P)-\sum_jw_j\log\mathfrak S(F_j)-H(P)
     +\sum_jw_j D(\nu_j\Vert\lambda_{F_j}).
   \quad}
   \tag{5}
   \]
   The limit may be `+infinity`; `lambda_F` is the product law defined below. Thus `lambda_P=sum_j w_j lambda_(F_j)` is the **unique** minimizer of the renormalized limit (5).

PC-470's general recovery construction permits a different selector at every cutoff and slowly enlarges its matched window. Formula (3) supplies projectively consistent recovery without such a schedule, while (5) identifies the cost of any additional phase bias or correlation for a finite support mixture. This does not characterize the full exact image of (1): the infinite-support obstructions in PC-472/473 remain intact.

## 2. A product law that realizes exactly one finite support

For finite admissible `F`, define
\[
M_p(F)=(\mathbb Z/p\mathbb Z)\setminus(F\bmod p),\qquad
\lambda_F=\bigotimes_p\operatorname{Unif}(M_p(F)).
\tag{6}
\]
Each factor is nonempty and excludes zero. This is an explicit product measure, **not** an undefined conditioning of `m_0` on an infinite null event.

Every phase in the product (6) preserves `F`. If `h notin F`, then for every sufficiently large prime the residues of `F union {h}` are all distinct. At such a prime the probability that `h` survives is
\[
1-\frac1{p-|F|}.
\tag{7}
\]
Independence and divergence of `sum_p 1/p` make the infinite product of (7) zero. Removing finitely many primes does not change this. Taking the countable union over `h notin F` proves
\[
\lambda_F\{r:C(r)=F\}=1.
\tag{8}
\]
The different `lambda_F` therefore live on disjoint measurable coding fibers. In particular, `lambda_{ {0} }=m_0`, and nontrivial fibers have `m_0` measure zero.

At each finite cutoff the marginal in (6) is precisely uniform conditioning on preserving `F`. Its relative entropy is
\[
a_y(F):=D_y(\lambda_F)
=-\log\prod_{p\le y}\frac{p-\nu_p(F)}{p-1}.
\tag{9}
\]
The rooted CRT/singular-series calculation of
[[research/prime_circle/findings/PC-470-root-selection-entropy-classifies-finite-cotangent-limits]], §§2,4, gives, for each fixed `F`,
\[
a_y(F)=(|F|-1)\log\log y
       +( |F|-1)\gamma-\log\mathfrak S(F)+o_F(1).
\tag{10}
\]
Indeed the product in (9) equals `eta_y^(|F|-1)` times the partial singular series, where `eta_y=prod_(p<=y)(1-1/p)`. Mertens's theorem supplies `eta_y~e^(-gamma)/log y`; away from the finitely many prime divisors of pair differences, the singular-series factors are `1+O_F(p^(-2))`. No prime-tuple occurrence conjecture enters.

## 3. The uniform bound needed for countable mixtures

Pointwise asymptotics (10) alone do not justify averaging over unbounded patterns. There is an absolute constant `B` such that for every finite admissible `F`, all `y>=3`, and `k=|F|`,
\[
0\le a_y(F)\le(k-1)(\log\log y+B).
\tag{11}
\]
For `k=1` this is exact with both sides zero. For `k>=2`, split the prime sum at `2k`. At the small primes, admissibility gives
\[
\sum_{p\le\min(y,2k)}\log\frac{p-1}{p-\nu_p(F)}
\le\sum_{p\le2k}\log p=O(k).
\tag{12}
\]
The last estimate is the elementary Chebyshev bound; it follows by summing the dyadic bound obtained from the prime divisors of `binom(2n,n)<=4^n`.

For `p>2k`, use `nu_p(F)<=k` and `-log(1-u)<=u+2u^2` for `0<=u<=1/2`:
\[
\log\frac{p-1}{p-\nu_p(F)}
\le\frac{k-1}{p-1}+\frac{2(k-1)^2}{(p-1)^2}.
\tag{13}
\]
The quadratic tail sums to `O(k)`, even if summed over all integers. Also
`sum_(p<=y)1/(p-1)<=log log y+O(1)`, by Mertens's product theorem and convergence of `sum_p p^(-2)`. Finally `k<=2(k-1)` absorbs both `O(k)` terms. The constants in (11) are independent of the locations, diameters and residue collisions of `F`.

Now set
\[
\lambda_P=\sum_{F\in\mathcal F_0}P(F)\lambda_F.
\tag{14}
\]
Equation (8) proves its exact output law. Convexity of relative entropy, (10), (11) and dominated convergence yield
\[
\limsup_y\frac{D_y(\lambda_P)}{\log\log y}
\le\lim_y\sum_F P(F)\frac{a_y(F)}{\log\log y}=J(P).
\tag{15}
\]
For any fixed compatible law, the finite sieve masks converge pointwise almost surely to `C(r)`, so their laws converge weakly to its coding law. PC-470's finite-window entropy lower bound therefore applies to its CRT marginals and gives the opposite liminf. This proves (3) and optimality. The domination step is what removes any integrability requirement on `log S(F)`, support diameter, or `H(P)` from the leading-order theorem.

## 4. Exact second-order cost of changing the phase law

Assume now the finite-mixture hypotheses of (5). Under any `nu` with coding law `P`, every conditional marginal `(nu_j)_y` is supported on phases preserving `F_j`. On this finite event the density of `(lambda_(F_j))_y` relative to `(m_0)_y` is the constant `exp(a_y(F_j))`. Splitting the logarithm gives the exact identity
\[
D((\nu_j)_y\Vert(m_0)_y)
=a_y(F_j)+D((\nu_j)_y\Vert(\lambda_{F_j})_y).
\tag{16}
\]
Let `J` be the random support label and `R_y=(r_p)_(p<=y)`. The finite-alphabet chain rule then gives
\[
D_y(\nu)
=\sum_jw_j a_y(F_j)
 +\sum_jw_jD((\nu_j)_y\Vert(\lambda_{F_j})_y)
 -I_\nu(J;R_y).
\tag{17}
\]
Every term here is finite at fixed `y`. Increasing coordinate sigma-fields generate the Borel sigma-field of `Omega`, hence
\[
D((\nu_j)_y\Vert(\lambda_{F_j})_y)
\uparrow D(\nu_j\Vert\lambda_{F_j}).
\tag{18}
\]
Moreover `J` is determined almost surely by the full phase, because its support is `C(r)`. Mutual information therefore increases to `H(P)`. Equivalently, the finite-label conditional probabilities given `R_y` converge by the martingale theorem to the indicators of the coding fibers; boundedness of the finite-label entropy gives conditional entropy tending to zero.

Substitute (10) into (17), then use (18) and the information limit. There is no subtraction of two infinite quantities: the label entropy and the finite sum of singular-series constants are finite. This proves (5), including its extended-real case.

The last term of (5) is nonnegative and vanishes exactly when every `nu_j=lambda_(F_j)`. Equation (8) makes those laws valid conditional laws of (14), proving existence and uniqueness of the minimizer. For example, a nonuniform tilt at just one prime coordinate preserves the almost-sure output (8), but creates a strictly positive finite second-order penalty if it changes that component law. Such tilts still have the same leading rate: uniqueness is a **second-order** statement, not a uniqueness assertion for (3).

## 5. Consequences and limits for Prime Circle

The compatible operator limit remains
\[
(L_F)_{hk}=\mathbf1_{h,k\in F}
\begin{cases}i/[\pi(h-k)],&h\ne k,\\0,&h=k.\end{cases}
\tag{19}
\]
PC-471's boundedness and column-tail estimate prove strong convergence along every compatible phase, uniformly in refinement on each fixed vector. Under (14), this gives the law `F~P`, followed by the finite operator `L_F`. Thus imposing consistency across cutoffs does not remove any of PC-470's finite-mean output laws, including nonzero operators. A fixed product law for `{0,2}` already has leading cost one and a nonzero two-point block; no selection changing with the cutoff is needed.

Conversely, the PC-470 lower bound still excludes positive mass on infinite supports under a bounded `D_y/log log y` budget. Compatibility changes the exact infinite-support image, but does not create an additional leading entropy threshold in the finite-cost sector. These are constraints on laws on residue phases, not spatially invariant measures or dynamical entropy rates.

The construction deliberately inputs `P`; neither compatibility nor entropy minimization chooses that output law from the circle geometry. The leading cost is ordinary cardinality/rare-event information. Formula (5) additionally retains classical singular-series constants and the ordinary mixture entropy. Neither term supplies a relation to zeta-zero location. The infinite-phase relative entropy `D(nu||m_0)` is generally infinite; (3)--(5) concern its finite-coordinate growth and renormalization, not finite total entropy. For countably many support labels we assert (3), **not** formula (5) with potentially divergent constants or label entropy. No operator-norm or spectral-type convergence is inferred from strong convergence.

## 6. Prior art, audit and evidence boundary

The underlying coding is the classical B-free window coding in Kasjan--Keller--Lemańczyk, *Dynamics of B-free sets: a view through the window*, **IMRN 2019**, 2690--2734, DOI [10.1093/imrn/rnx196](https://doi.org/10.1093/imrn/rnx196), [manuscript](https://arxiv.org/abs/1702.02375). Its invariant-measure questions are distinct from the rooted, generally nonstationary laws used here. PC-471 supplies the precise local coding and operator bridge.

R. M. Gray, *Entropy and Information Theory*, first edition (1990), [author's corrected 2023 edition](https://ee.stanford.edu/~gray/it.pdf), Corollary 2.5.1 and Corollaries 5.2.3--5.2.5, supply the classical information chain rule and convergence of relative entropy along generating coordinate sigma-fields. These support (17)--(18); equations (6)--(17) explicitly derive the residue-law specialization. No new information-theory principle is claimed.

The arithmetic inputs are the standard singular series in K. S. Kedlaya, *Notes on analytic number theory*, [Chapter 19, Definition 19.1](https://kskedlaya.org/ant/chap-k-tuples.html), and Mertens's product theorem as stated in J. C. Lagarias, *Euler's constant: Euler's work and modern developments*, **Bull. Amer. Math. Soc. 50** (2013), 527--628, [manuscript](https://arxiv.org/pdf/1303.1856), Theorem 3.3.2. PC-470 already derives their exact rooted normalization. The uniform bound (11), projectively consistent recovery, and second-order characterization distinguish the present claim from its cutoff-dependent recovery theorem.

Targeted local duplication searches covered compatible entropy, fixed phase laws, mixtures and information projection. External searches covered B-free coding measures, sieve selection entropy, mixture identities and entropy convergence. The result is classified as a classical-method specialization with a new local selection boundary, without a historical-priority claim. No finite-hole or general infinite-support compatibility criterion is established.

A standard-library audit under `/tmp` completed **652 checks**. Exact rational calculations verified product normalization, inclusion probabilities for every offset from `-8` through `8`, and marginal consistency of four component laws and their mixtures at prime cutoffs through `13` (up to **5,760 phase points**). Both uniform components and single-coordinate nonuniform tilts were checked. The two entropy decompositions in (17) agreed to at most **2.23e-16**. The count includes **98 numerical stress checks** of the cardinality-only majorant over sizes through `100001` and cutoffs through `100000`; those checks do not prove (11). The all-prime exclusion, uniform domination and generating-sigma-field limits are proved above, not by finite computation.

This is not Lean-verified or independently adversarially approved. The consequential proof boundary is the combination of infinite product exclusion, countable-mixture domination and the phase-fiber information limit. No separate bounded formalization-fertility target is asserted and no executor is enrolled. The result closes the fixed-law consistency cost question without advancing RH.
