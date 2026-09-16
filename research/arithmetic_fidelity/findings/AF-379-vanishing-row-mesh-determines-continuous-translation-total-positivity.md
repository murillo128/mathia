# AF-379 — Vanishing row mesh determines continuous translation total positivity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `SAMPLING` · `PRIME-LOGS` · `DETERMINING-SET` · `CLASSICAL-ADJACENT` · `NO-NOVELTY-CLAIM`

## Claim

For a translation kernel

\[
K_f(u,x)=f(u-x),
\]

row sampling is target-faithful for total nonnegativity whenever the sampled row set is dense enough **modulo common translation** to approximate every finite ordered row pattern.

For `k\ge 2`, define the normalized row-pattern set

\[
\mathcal P_k(E)
:=
\left\{
(u_2-u_1,\ldots,u_k-u_1):
 u_1<\cdots<u_k,\ u_i\in E
\right\}
\subset
\mathcal C_k,
\tag{1}
\]

where

\[
\mathcal C_k
:=
\{(d_2,\ldots,d_k):0<d_2<\cdots<d_k\}.
\tag{2}
\]

Let `r\in\mathbb N\cup\{\infty\}`. Assume `f:\mathbb R\to\mathbb R` is continuous and

\[
\overline{\mathcal P_k(E)}=\mathcal C_k
\qquad (2\le k\le r).
\tag{3}
\]

If every sampled minor of order at most `r` is nonnegative,

\[
\det\bigl(f(u_i-x_j)\bigr)_{i,j=1}^k\ge0
\tag{4}
\]

for every `k\le r`, every increasing `u_1<\cdots<u_k` in `E`, and every increasing `x_1<\cdots<x_k` in `\mathbb R`, then `K_f` is globally totally nonnegative of order `r`. Thus `(3)` is a source-independent sufficient determining condition for continuous translation kernels.

A simple geometric condition forces `(3)`: if `E` contains an increasing unbounded sequence

\[
e_1<e_2<\cdots,\qquad e_n\to\infty,
\]

whose consecutive mesh vanishes,

\[
e_{n+1}-e_n\to0,
\tag{5}
\]

then `\mathcal P_k(E)` is dense in `\mathcal C_k` for every finite `k`. Consequently, sampled total nonnegativity on `E` determines full total nonnegativity for every continuous translation kernel.

The arithmetic specialization is exact. For

\[
E_{\mathbb P}:=\{\log p:p\text{ prime}\},
\tag{6}
\]

the prime number theorem gives

\[
\log p_{n+1}-\log p_n
=
\log\!\left(\frac{p_{n+1}}{p_n}\right)
\longrightarrow0.
\tag{7}
\]

Hence `E_{\mathbb P}` satisfies `(5)`. Therefore, for every continuous `f`, total nonnegativity of `f(u-x)` at **all prime-log row locations and arbitrary real columns** already forces global translation total nonnegativity. If `f` is also nonzero and integrable, then being `E_{\mathbb P}`-Pólya-frequency in Ganzburg's sense is equivalent to being a full Pólya-frequency function.

This is a determining theorem, but it also gives a fidelity warning: inside the continuous translation-kernel category, an all-order positivity certificate on `\log p` rows cannot remain specifically prime-sensitive. Once it holds on every prime-log row pattern, continuity and the asymptotically vanishing log-prime mesh propagate it to every real row pattern.

## Exact pattern-closure proof

Fix `k\le r`, arbitrary increasing target rows

\[
a_1<\cdots<a_k,
\]

and arbitrary increasing columns

\[
b_1<\cdots<b_k.
\]

Set

\[
d_i:=a_i-a_1,\qquad i=2,\ldots,k.
\]

By `(3)`, there are sampled row tuples

\[
u_1^{(m)}<\cdots<u_k^{(m)},\qquad u_i^{(m)}\in E,
\]

such that

\[
u_i^{(m)}-u_1^{(m)}\longrightarrow d_i
\qquad (i=2,\ldots,k).
\tag{8}
\]

Translate the columns by the sampled first row:

\[
y_j^{(m)}
:=
b_j+u_1^{(m)}-a_1.
\tag{9}
\]

The order of the columns is unchanged, so `(4)` applies to `u_i^{(m)}` and `y_j^{(m)}`. Moreover,

\[
\begin{aligned}
u_i^{(m)}-y_j^{(m)}
&=
\bigl(u_i^{(m)}-u_1^{(m)}\bigr)+a_1-b_j\\
&\longrightarrow
(a_i-a_1)+a_1-b_j\\
&=a_i-b_j.
\end{aligned}
\tag{10}
\]

Continuity of `f` therefore gives entrywise convergence of the sampled matrices to the arbitrary target matrix,

\[
\bigl(f(u_i^{(m)}-y_j^{(m)})\bigr)_{i,j}
\longrightarrow
\bigl(f(a_i-b_j)\bigr)_{i,j}.
\tag{11}
\]

The determinant is continuous in its entries. Since every determinant on the left is nonnegative,

\[
\det\bigl(f(a_i-b_j)\bigr)_{i,j=1}^k\ge0.
\tag{12}
\]

The target rows and columns were arbitrary, proving global total nonnegativity through order `r`.

The mechanism is exact and uses no decay, transform theory, or integrability. The only analytic input is continuity of the profile; the only sampling input is density of normalized finite row patterns. Common row location is irrelevant because translation of all rows can be absorbed by the unrestricted column variable as in `(9)`.

## Vanishing mesh implies pattern density

Assume `(5)`. Fix an arbitrary target pattern

\[
0=d_1<d_2<\cdots<d_k
\]

and a tolerance `\varepsilon>0` smaller than one third of the minimum target gap.

Because `e_{n+1}-e_n\to0`, there is a tail of the sequence on which every consecutive gap is below `\varepsilon`. Choose a large translation `T` so that all points

\[
T+d_1,\ldots,T+d_k
\]

lie inside that tail. For each `i`, choose `u_i\in\{e_n\}` immediately at or immediately below `T+d_i`. Then

\[
|u_i-(T+d_i)|<\varepsilon.
\tag{13}
\]

For the chosen tolerance the `u_i` remain strictly increasing, and

\[
\left|(u_i-u_1)-d_i\right|<2\varepsilon.
\tag{14}
\]

Letting `\varepsilon\downarrow0` proves

\[
\overline{\mathcal P_k(E)}=\mathcal C_k.
\tag{15}
\]

Thus vanishing tail mesh supplies arbitrarily accurate translated copies of every finite ordered configuration. This is stronger than having a dense generated difference subgroup: it realizes the required differences **simultaneously inside one sampled tuple**, which is exactly what a determinant observes.

## Prime-log corollary

Let `p_n` be the `n`-th prime. The prime number theorem in the standard equivalent form

\[
p_n\sim n\log n
\tag{16}
\]

implies

\[
\frac{p_{n+1}}{p_n}
=
\frac{p_{n+1}}{(n+1)\log(n+1)}
\frac{(n+1)\log(n+1)}{n\log n}
\frac{n\log n}{p_n}
\longrightarrow1.
\tag{17}
\]

Taking logarithms gives `(7)`. Hence the ordered set of prime logarithms has vanishing consecutive mesh even though it has no finite accumulation point.

More concretely, for every finite multiplicative pattern

\[
1=c_1<c_2<\cdots<c_k
\]

and every `\varepsilon>0`, sufficiently far out one can choose primes `q_1<\cdots<q_k` such that

\[
\left|
\log\frac{q_i}{q_1}-\log c_i
\right|<\varepsilon
\qquad(i=2,\ldots,k).
\tag{18}
\]

Thus prime ratios, after a common large scaling and logarithm, approximate every finite positive ratio pattern. Equation `(18)` is not a statement about special prime constellations at bounded additive gaps; it is only the coarse relative-density consequence of the prime number theorem needed by the translation-kernel closure argument.

For a continuous integrable profile `f`, Ganzburg's sampled condition on

\[
E=E_{\mathbb P}=\{\log p\}
\]

therefore has no residual target fibre with respect to full Pólya-frequency status:

\[
f\text{ is }E_{\mathbb P}\text{-PF}
\quad\Longleftrightarrow\quad
f\text{ is PF}.
\tag{19}
\]

The reverse implication is immediate; the forward implication is the pattern-closure theorem above.

## Relation to AF-373 through AF-378

AF-373 established from Ganzburg that sampling geometry can itself carry enough information to make `E`-Pólya-frequency equivalent to full Pólya-frequency on an exponentially decaying class, while a fixed lattice admits exact aliases. AF-374 and AF-375 then isolated periodic and separable-gauge fibres, and AF-376 showed that every uniformly discrete row set admits compact-support false positives on Ganzburg's broad source class. AF-377 strengthened that local-support obstruction through bounded interaction components.

The present result supplies the opposite exact regime anticipated after AF-376. Positive minimum separation is a universal source of aliases on a broad class; **vanishing tail mesh is a universal determining resource on the continuous translation-kernel class**. It is not merely absence of the AF-376 counterexample: the closure proof positively transports every sampled determinant inequality to every missing row configuration.

It also sharpens AF-375. A dense generated subgroup

\[
\langle E-E\rangle
\]

kills the classified periodic separable gauge but need not place any new row tuples in the observation. Pattern density `(3)` is stronger and determinant-native: the required finite differences must occur simultaneously, up to arbitrarily small error, inside actual sampled tuples.

AF-378 remains an essential representation boundary. A nonlinear map can turn a uniformly discrete set into one with vanishing displayed gaps while preserving the old sampled fibre if the kernel is transported with that map. AF-379 does **not** claim otherwise. Its hypothesis concerns a translation kernel that is genuinely of the form `f(u-x)` in the coordinate where `(3)` or `(5)` is asserted. Applying the theorem to `\log p` is legitimate only when logarithmic/additive difference structure is part of the mathematical model itself; taking logarithms solely to make an old sample set look denser is the invalid replacement diagnosed in AF-378.

## Fidelity interpretation

The exact observable carried by row-sampled translation total positivity is not the absolute sample set but its family of finite configurations modulo common translation. The normalization `(1)` removes the degree of freedom that the arbitrary columns already make invisible.

This yields a reusable hierarchy of sampling geometry:

- a dense algebraic difference group can remove some separable gauges without determining the target;
- unbounded support-scale interaction can remove local compact-support aliases without yet proving determination;
- dense finite row patterns modulo translation are sufficient to determine every continuous translation minor by closure.

The last condition is strong enough that no source-specific theorem is needed beyond continuity. In Arithmetic Fidelity terms, the sampled observation has become target-faithful because the target inequalities lie in the topological closure of the observed inequalities.

The price is equally clear: once this closure holds, the sampling locations themselves no longer encode a special arithmetic discriminator at the level of the Boolean total-positivity certificate. Any distinction between rational primes and a matched non-prime set with the same finite-pattern closure must live in additional structure, in the values of another observable, or in a non-translation mechanism.

## Riemann specialization

AF-371 records the classical Schoenberg/Gröchenig equivalence between RH for the completed Riemann `Xi` function and full Pólya-frequency structure of the corresponding reciprocal-transform kernel. AF-379 does not prove any of the required positivity inequalities and therefore gives no evidence for RH.

It does, however, close one possible sampling question. Suppose an RH-facing proposal produces a **continuous translation kernel in an intrinsically logarithmic coordinate** and claims that checking all total-nonnegativity minors only at row locations `\log p` is a weaker prime-specific condition. It is not: by `(19)`, that sampled condition is already equivalent to full Pólya-frequency status.

This has two opposite uses.

First, it is a legitimate reduction theorem: if the prime-log sampled minors were somehow accessible from arithmetic, continuity would allow one to recover all missing row minors without a separate analytic interpolation theorem.

Second, it is a discriminator warning: the final positivity property contains no extra prime specificity merely because its rows were checked at prime logarithms. The prime arithmetic would have to enter in the mechanism that proves those sampled inequalities, in an additional marking/orientation, or in a richer non-translation object. Once all sampled minors are nonnegative, the location restriction itself has disappeared under closure.

This distinction is exactly the Arithmetic Fidelity question: **where does the arithmetic discriminator survive, rather than where are prime labels still written in the notation?**

## Prior-art and novelty audit

Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1–8, DOI `10.1016/j.jmaa.2008.04.070`, is the direct classical sampling framework. It defines `E`-PF functions, proves that a set with a finite accumulation point is determining for the exponentially decaying class `L`, gives a second determining theorem for suitable symmetric slowly growing unbounded sequences, and exhibits integer-lattice false positives. Those results establish that sparse sampling geometry can either determine or fail to determine PF structure depending on the geometry and source class.

I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* **1** (1951), 331–374, DOI `10.1007/BF02790092`, and Samuel Karlin, ***Total Positivity, Vol. I*** (Stanford University Press, 1968), are the classical sources for translation total positivity and Pólya-frequency functions.

The prime-number input `(16)`--`(17)` is the classical prime number theorem. No short-interval theorem, bounded-gap theorem, or conjectural prime-distribution statement is used.

A focused search for `E`-Pólya-frequency determining sets, total-positive-kernel sampling, dense finite row patterns, vanishing sampling mesh, and prime-log sampling did not identify a published result stated as `(3)` or its `E={\log p}` corollary. No novelty is claimed: the pattern-closure proof is an elementary continuity argument, and Ganzburg is the direct neighboring theory. The durable Arithmetic Fidelity contribution is the **exact audit criterion and arithmetic specialization**: normalized finite-pattern density is a sufficient target-fidelity condition, vanishing mesh forces it, and the prime-log set satisfies that condition by the prime number theorem.

## Boundaries and failure modes

Continuity is essential to this proof. Ganzburg's definition permits merely measurable integrable profiles, and `(3)` alone does not justify passing determinant signs to unsampled configurations for a discontinuous function. AF-379 therefore does not replace Ganzburg's source-class-dependent theorems.

Vanishing mesh is sufficient, not necessary. Ganzburg's analytic determining theorems can succeed for sampling geometries not covered by `(5)`, because source rigidity may compensate for missing geometric closure. Conversely, failure of `(5)` does not imply non-determination.

The theorem concerns nonnegative minors. Strict total positivity does not pass from sampled strict inequalities to strict inequalities in a limit: a sequence of positive determinants may converge to zero. No strict-positivity conclusion is claimed.

The prime-log corollary uses all primes and all determinant orders, with arbitrary real columns. Finite prime ranges, selected prime subsequences, bounded determinant order, discretized columns, noisy inequalities, or quantitative stability are different compression problems and are not covered by `(19)`.

Finally, the logarithmic coordinate must be intrinsic to the translation structure under study. If an existing kernel is merely reparameterized nonlinearly, AF-378 requires transporting the kernel as well; one may not replace the transported kernel by a fresh `g(s-t)` and call the improved spacing a fidelity gain.

## Decisive audit rule

For any row-sampled translation-total-positivity proposal with continuous profile, compute the closure of the normalized finite row-pattern sets `\mathcal P_k(E)` before searching for complicated interpolation or recovery machinery.

If `\overline{\mathcal P_k(E)}=\mathcal C_k` through the determinant orders needed by the target, the sampled inequalities already determine the corresponding global inequalities by continuity. In particular, an increasing sampling tail with consecutive mesh tending to zero passes this gate at every finite order.

For arithmetic sampling on `E={\log p}`, the prime number theorem already supplies that geometry. Any claimed prime-specific content must therefore be located **before or beyond** the bare continuous translation-total-positivity certificate, not in the fact that its row labels happen to be prime logarithms.

## Consequences

AF-376's broad dichotomy now has a positive companion. Uniform separation guarantees exact compact-support aliases on `L`; vanishing tail mesh guarantees target determination for continuous translation kernels. The unresolved middle regime consists of sampling sets whose local spacing degenerates only intermittently, or source classes whose rigidity may recover missing configurations without full pattern closure.

For the Riemann-facing branch, the most useful next question is no longer whether prime-log row sampling has enough geometric coverage: it does, at the continuous translation-kernel level. The sharper question is whether an arithmetic construction can **intrinsically produce or control those prime-log sampled minors** without having already imported the full Schoenberg/Pólya-frequency target. That moves the discriminator audit back to the arithmetic mechanism that generates the inequalities, where prime specificity could genuinely survive.