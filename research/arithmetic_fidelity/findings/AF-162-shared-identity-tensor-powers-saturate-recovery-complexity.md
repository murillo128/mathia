# AF-162 — Shared-identity tensor powers saturate recovery complexity instead of multiplying it

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `COMPOSITION-LAW`, `STRUCTURAL-RIGIDITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-161 proves that the barycentric domination radius `Lambda_bar` tensorizes exactly for the **full Cartesian product experiment**. Consequently, if each coordinate may choose its experiment member independently, the source complexity required by AF-159's Pearson-to-optimal-recovery calibration grows exponentially.

That obstruction is not a generic consequence of repeated independent observations. It is a consequence of allowing the **alternative identity itself to recombine independently across coordinates**. If the same alternative label is preserved across all coordinates, the behavior is opposite: the domination complexity stays uniformly bounded and asymptotically saturates at the number of distinct alternatives, while AF-160's extra convex-hull penalty vanishes.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite sample space `X`, after removing duplicate members, so the `P_i` are pairwise distinct. Define its shared-identity or diagonal `n`-fold experiment by

\[
\mathcal E^{\Delta n}
:=
(P_i^{\otimes n})_{i=1}^m
\quad\text{on }X^n.
\tag{1}
\]

This differs essentially from AF-161's full Cartesian tensor power

\[
\mathcal E^{\otimes n}
=
(P_{i_1}\otimes\cdots\otimes P_{i_n})_{(i_1,\ldots,i_n)\in[m]^n}.
\tag{2}
\]

For the diagonal family write

\[
s_n(x^n)=\max_i P_i^{\otimes n}(x^n),
\qquad
C_n=\sum_{x^n}s_n(x^n),
\tag{3}
\]

and

\[
\Lambda_n
:=
\Lambda_{\rm bar}(\mathcal E^{\Delta n}),
\qquad
G_n:=\frac{\Lambda_n}{C_n},
\qquad
d_n:=\log G_n.
\tag{4}
\]

For each pair define the Hellinger/Bhattacharyya affinity

\[
a_{ij}
:=
\sum_{x\in X}\sqrt{P_i(x)P_j(x)}.
\tag{5}
\]

Because the members are distinct, `0<=a_ij<1`. Then for every `n`,

\[
\boxed{
 m-\sum_{i<j}a_{ij}^n
\le
C_n
\le
\Lambda_n
\le
m.
}
\tag{6}
\]

Consequently,

\[
\boxed{
C_n\longrightarrow m,
\qquad
\Lambda_n\longrightarrow m,
\qquad
G_n\longrightarrow1,
\qquad
d_n\longrightarrow0.
}
\tag{7}
\]

The convergence is exponentially fast. If

\[
a_*:=\max_{i<j}a_{ij}<1,
\]

then

\[
0\le m-C_n
\le {m\choose2}a_*^n,
\tag{8}
\]

and whenever the denominator is positive,

\[
\boxed{
1\le G_n
\le
\frac{m}{m-{m\choose2}a_*^n},
\qquad
0\le d_n
\le
-\log\left(1-\frac{m-1}{2}a_*^n\right).
}
\tag{9}
\]

Thus AF-159's bounded-likelihood-complexity gate is automatically stable for a **fixed finite shared-identity family**:

\[
\Lambda_n\le m
\qquad\forall n.
\tag{10}
\]

In particular, if `M_n` is an optimal barycentric reference for the diagonal family and `Gamma_{M_n}` is AF-159's propagated Pearson defect, then the same theorem gives the `n`-independent calibration

\[
\boxed{
4\delta_{\rm rec}^2
\le
\Gamma_{M_n}
\le
m(m+2)\,\delta_{\rm rec}.
}
\tag{11}
\]

No analogous uniform source constant exists for AF-161's full Cartesian tensor powers of a nontrivial experiment.

The structural distinction is therefore exact: **independent evidence does not create the exponential calibration obstruction; independent recombination of the hidden alternative does.** Preserving one common identity across coordinates is a relational provenance constraint, and that constraint changes the local-to-global fidelity budget from multiplicative growth to finite saturation.

## Derivation

### The Shtarkov mass is exactly a uniform-prior classification success probability

For the diagonal family, consider the finite `m`-hypothesis decision problem with uniform prior and observations `X^n`. The Bayes/maximum-likelihood correct-decision probability is

\[
\begin{aligned}
p_{\rm corr}^{(n)}
&=
\sum_{x^n}\max_i
\frac1mP_i^{\otimes n}(x^n)\\
&=
\frac{C_n}{m}.
\end{aligned}
\tag{12}
\]

Hence, if `e_n^*` denotes the minimum uniform-prior classification error,

\[
\boxed{
C_n=m(1-e_n^*).
}
\tag{13}
\]

This gives a direct decision-theoretic meaning to the diagonal Shtarkov mass: it approaches `m` precisely as repeated observations make the fixed alternatives distinguishable.

### Pairwise overlap gives an elementary exponential bound

At any fixed observation `x^n`, for nonnegative numbers

\[
r_i=P_i^{\otimes n}(x^n),
\]

one has

\[
\sum_i r_i-\max_i r_i
\le
\sum_{i<j}\min(r_i,r_j).
\tag{14}
\]

Summing `(14)` over `x^n` gives

\[
\begin{aligned}
m-C_n
&\le
\sum_{i<j}\sum_{x^n}
\min\left(P_i^{\otimes n}(x^n),P_j^{\otimes n}(x^n)\right)\\
&\le
\sum_{i<j}\sum_{x^n}
\sqrt{P_i^{\otimes n}(x^n)P_j^{\otimes n}(x^n)}.
\end{aligned}
\tag{15}
\]

The Hellinger affinity factorizes under products:

\[
\sum_{x^n}
\sqrt{P_i^{\otimes n}(x^n)P_j^{\otimes n}(x^n)}
=
\left(
\sum_x\sqrt{P_i(x)P_j(x)}
\right)^n
=a_{ij}^n.
\tag{16}
\]

Combining `(15)` and `(16)` proves the first inequality in `(6)` and the exponential estimate `(8)`. Pairwise distinctness implies `a_ij<1`, so `C_n->m`.

### Barycentric domination is squeezed between Shtarkov mass and the fixed hypothesis count

AF-160 proves for every finite experiment that

\[
C\le\Lambda_{\rm bar}.
\tag{17}
\]

Applying this to `E^{Delta n}` gives `C_n<=Lambda_n`.

For the reverse bound choose the uniform barycenter

\[
M_n^{\rm unif}
:=
\frac1m\sum_{i=1}^mP_i^{\otimes n}.
\tag{18}
\]

Pointwise,

\[
P_i^{\otimes n}\le mM_n^{\rm unif}
\qquad\forall i,
\tag{19}
\]

and therefore every member of the convex hull obeys the same domination bound. By the definition of `Lambda_bar`,

\[
\Lambda_n\le m.
\tag{20}
\]

Together with `C_n->m`, equations `(17)` and `(20)` squeeze `Lambda_n->m`, proving the first three limits in `(7)`. AF-160 gives `G_n=Lambda_n/C_n=exp(d_n)`, so `G_n->1` and `d_n->0` as well. Combining `(8)` with `C_n<=Lambda_n<=m` gives `(9)`.

The conclusion is sharper than mere boundedness. The unrestricted Shtarkov center and the best automatically recoverable barycentric center become asymptotically equivalent in AF-160's directed order-infinity sense:

\[
d_\infty\left(
M_{{\rm Sh},n},
\operatorname{conv}(\mathcal E^{\Delta n})
\right)
=d_n\longrightarrow0.
\tag{21}
\]

Thus repeated identifiability removes the **convex-hull mismatch** even though the total source complexity approaches the nontrivial value `m` rather than `1`.

## Exact contrast with AF-161

For one nontrivial base experiment, AF-161 gives

\[
\Lambda_{\rm bar}(\mathcal E^{\otimes n})
=
\Lambda_{\rm bar}(\mathcal E)^n,
\tag{22}
\]

because the full Cartesian family contains every independently chosen label tuple `(i_1,...,i_n)`.

For the diagonal family, `(10)` gives instead

\[
\Lambda_{\rm bar}(\mathcal E^{\Delta n})\le m.
\tag{23}
\]

The difference is not probabilistic dependence of the observations: conditional on the common label `i`, the coordinates in `(1)` are still independent. What changes is the admissible **provenance relation among alternatives**. In `(1)` the same label must explain every coordinate; in `(2)` each coordinate may choose a new label independently.

This supplies an explicit example of a general Arithmetic Fidelity theme. Forgetting a cross-coordinate identity relation can be far more destructive than forgetting local scalar data: once the common label is discarded, the admissible control family expands from `m` coherent alternatives to `m^n` independently recombined alternatives, and AF-161's multiplicative complexity law reappears.

## Arithmetic/analytic stress test: repeated observations of the local `p=2` Euler-factor family

AF-157--AF-161 use the two-member local family

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right).
\tag{24}
\]

Its pairwise Hellinger affinity is exactly

\[
\begin{aligned}
a
&=
\sum_{k=1}^3\sqrt{P_1(k)P_2(k)}\\
&=
\frac{9+2\sqrt2}{7\sqrt3}
<1.
\end{aligned}
\tag{25}
\]

For the **shared-label** repeated family

\[
(P_1^{\otimes n},P_2^{\otimes n}),
\]

AF-162 therefore gives

\[
\boxed{
2-a^n
\le
C_n
\le
\Lambda_n
\le
2,
}
\tag{26}
\]

and

\[
1\le G_n\le\frac{2}{2-a^n},
\qquad
d_n\le-\log\left(1-\frac{a^n}{2}\right).
\tag{27}
\]

Hence `Lambda_n->2` and `G_n->1`. At one copy AF-159 gives `Lambda_1=11/9`; repeated evidence increases the optimal domination radius only toward the finite ceiling `2`.

By contrast, AF-161's **full Cartesian** family generated by the same local source has

\[
\Lambda_{{\rm bar},n}^{\rm Cart}
=\left(\frac{11}{9}\right)^n,
\qquad
G_{{\rm hull},n}^{\rm Cart}
=\left(\frac{77}{75}\right)^n.
\tag{28}
\]

So the same local distributions exhibit both regimes. The difference is entirely whether the alternative identity is coherent across factors or freely recombinable. This is a concrete matched control for the claim that **cross-factor provenance can itself be the structure that prevents a compression/recovery budget from exploding**.

This remains only a finite local arithmetic-derived model. It does not assert that the rational-prime Euler product is a diagonal repeated-sampling experiment. Its value is to isolate, in an exact setting, what kind of global coherence would be mathematically capable of defeating AF-161's Cartesian obstruction.

## Prior-art and novelty audit

The ingredients are classical and no novelty is claimed for the coding or testing facts themselves.

- Yu. M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3) (1987), introduced normalized maximum likelihood and the Shtarkov normalizing sum as the exact minimax-regret object. Equation `(12)` is the elementary finite-hypothesis decision interpretation of the same pointwise maximum.
- A. Bhattacharyya, **“On a Measure of Divergence between Two Statistical Populations Defined by Their Probability Distributions,”** *Bulletin of the Calcutta Mathematical Society* 35 (1943), 99–109, introduced the affinity underlying `(5)` and `(16)`.
- H. Chernoff, **“A Measure of Asymptotic Efficiency for Tests of a Hypothesis Based on the Sum of Observations,”** *Annals of Mathematical Statistics* 23(4) (1952), 493–507, DOI `10.1214/aoms/1177729330`, is classical prior art for exponential discrimination of distinct product distributions.
- Andrew Barron, Jorma Rissanen, and Bin Yu, **“The Minimum Description Length Principle in Coding and Modeling,”** *IEEE Transactions on Information Theory* 44(6) (1998), 2743–2760, DOI `10.1109/18.720554`, reviews normalized-maximized-likelihood and mixture coding as universal-coding constructions.

A targeted literature search found extensive classical work on NML/Shtarkov complexity, Bayes mixtures, and asymptotic hypothesis discrimination, but did not isolate AF-160's convex-hull-restricted `Lambda_bar` together with the specific diagonal-versus-Cartesian recovery-calibration comparison above. This is not a novelty claim: inequalities `(6)--(9)` are elementary consequences of those classical ingredients plus AF-160's exact `C<=Lambda_bar<=m` geometry.

The durable result for this line is the **structural boundary** obtained by placing those facts next to AF-161: the exponential local-to-global obstruction is caused by growth of the admissible alternative family under independent recombination, and a shared identity constraint is sufficient to replace that growth by a finite complexity ceiling.

## Boundaries and counterarguments

1. **Fixed finite alternative class is essential to the uniform ceiling.** If the number of coherent alternatives itself grows with `n`, the bound `Lambda_n<=m` must be replaced by the actual class size or a sharper model-specific radius. AF-162 does not give a dimension-free theorem for arbitrary growing families.

2. **Diagonal coherence is not automatically arithmetic provenance.** A real arithmetic application must derive the shared-label or analogous compatibility constraint intrinsically. Declaring that all local pieces came from one hidden global object without proving the compatibility relation would merely reinsert provenance by hand.

3. **The total complexity does not vanish.** `G_n->1` means the convex-hull penalty disappears, but `Lambda_n->m`, not `1`. The fixed family remains genuinely discriminating, and AF-159's optimal-recovery modulus retains an `m`-dependent source constant.

4. **Pairwise distinguishability drives the limit.** If duplicate laws are retained in the presentation, they must first be quotiented because `Lambda_bar` is convex-hull invariant. More general asymptotically indistinguishable or `n`-dependent alternatives require their own analysis.

5. **No RH consequence is established.** The theorem identifies one mathematically sufficient form of cross-scale coherence for avoiding a known fidelity-complexity blow-up. It does not show that rational primes possess the needed representation at any candidate RH compression.

## Consequence for the line

AF-161 ended with a precise fork: a scalable arithmetic application must either restrict the destination witness class or exploit genuine dependence/coherence that prevents the full Cartesian family of local alternatives from being admissible.

AF-162 resolves one side of that fork in a canonical model. **A common alternative identity across independent coordinates is enough:** the barycentric recovery complexity stays bounded by the fixed number of alternatives, approaches that finite ceiling, and the additional Shtarkov-to-hull mismatch vanishes exponentially.

The next arithmetic question is therefore sharper than “are the local factors independent?” It is: **what exact compatibility relation prevents independently matched local controls from being recombined into a globally admissible control?** If such a relation exists intrinsically, it is itself part of the information that must survive compression. If it is forgotten, AF-161's Cartesian obstruction is the appropriate matched-control model.