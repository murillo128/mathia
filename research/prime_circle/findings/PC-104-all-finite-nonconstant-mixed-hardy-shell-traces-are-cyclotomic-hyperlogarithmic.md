# PC-104 — all finite nonconstant mixed Hardy shell traces are cyclotomic-hyperlogarithmic

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. The rootwise cyclic-separation hypothesis in PC-103 is not needed for any ordinary finite **nonconstant completed-shell trace**. If a finite Hardy root word contains one separated adjacent pair in its actual operator order, its natural finite sections converge in trace norm as in PC-084/PC-086; reciprocal closing or repeated-shell channels only create endpoint factors `1-x_i x_{i+1}` in the cube integral. Because at least one edge is nonsingular, those singular edges form a forest of paths, whose product kernel is locally integrable. The ordinary trace is therefore an absolutely convergent improper cyclotomic Euler integral, and the same polynomial-reduction argument as PC-103 remains linearly reducible with only cyclotomic letters.

Consequently, for every finite shell word `Gamma_{n_1}...Gamma_{n_k}` with `k>=2`, all `n_i>1`, and at least two distinct shell labels,

\[
\boxed{
\operatorname{Tr}(\Gamma_{n_1}\cdots\Gamma_{n_k})
\in
\mathbb Q(\mu_{2N})\cdot \operatorname{MPV}_{\le k}(2N),
\qquad
N=\operatorname{lcm}(n_1,\ldots,n_k).
}
\]

This closes the finite repeated-shell loophole left explicitly by PC-084, PC-086, and PC-103. It does **not** assign an ordinary trace to constant-shell powers, infinite-shell generating constructions, Fredholm/global Hardy determinants, or the global uniformization/monodromy branch.

## 1. Root words need only one separated pair in operator order

For a unit root `alpha`, recall

\[
(\mathcal H_\alpha)_{jk}
=\frac{\alpha^{j+k+1}}{j+k+1},
\qquad j,k\ge0,
\]

and

\[
\Gamma_n=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha.
\]

Let

\[
W=\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k},
\qquad k\ge2.
\]

Assume there is an **ordinary adjacent pair**

\[
\boxed{
\alpha_j\alpha_{j+1}\neq1
\quad\text{for some }1\le j<k.
}
\]

PC-080 gives

\[
\mathcal H_{\alpha_j}\mathcal H_{\alpha_{j+1}}\in\mathcal S_1,
\]

and the separated-pair finite-section estimate used in PC-084 gives

\[
\left\|
P_M\mathcal H_{\alpha_j}P_M
\mathcal H_{\alpha_{j+1}}P_M
-
\mathcal H_{\alpha_j}\mathcal H_{\alpha_{j+1}}
\right\|_1\longrightarrow0.
\]

All other root channels are bounded, while their compressions converge strong-* and are uniformly bounded. Trace-ideal continuity around the displayed nuclear core therefore yields

\[
\boxed{
\left\|
P_M\mathcal H_{\alpha_1}P_M\cdots
P_M\mathcal H_{\alpha_k}P_M
-W
\right\|_1\longrightarrow0.
}
\]

In particular `W` is trace class and its ordinary trace is the limit of the natural interleaved finite sections.

This is exactly the operator-theoretic distinction that matters below. A separated **closing** pair `alpha_k alpha_1 != 1` by itself is not enough to manufacture a trace-class core in the displayed operator order. Scalar finite-section limits can exist even when the operator is not trace class, as PC-086 already showed at length one.

## 2. The finite-section cube formula does not require cyclic separation

Put cyclically

\[
q_i=\alpha_i\alpha_{i+1},
\qquad
\alpha_{k+1}=\alpha_1,
\qquad
A=\prod_{i=1}^k\alpha_i.
\]

For the finite trace

\[
S_M
=\operatorname{Tr}
\bigl(P_M\mathcal H_{\alpha_1}P_M\cdots
P_M\mathcal H_{\alpha_k}P_M\bigr),
\]

the same elementary expansion as in PC-086 is finite and hence needs no convergence hypothesis:

\[
S_M
=
\sum_{0\le j_1,\ldots,j_k\le M}
\prod_{i=1}^k
\frac{\alpha_i^{j_i+j_{i+1}+1}}
{j_i+j_{i+1}+1},
\qquad j_{k+1}=j_1.
\]

Using

\[
\frac1{j_i+j_{i+1}+1}
=\int_0^1x_i^{j_i+j_{i+1}}\,dx_i
\]

and regrouping the powers of each `j_i` gives, after a cyclic relabeling,

\[
\boxed{
S_M
=A\int_{[0,1]^k}
\prod_{i=1}^k
\left(
\sum_{m=0}^M(q_i x_i x_{i+1})^m
\right)
\,dx_1\cdots dx_k,
\qquad x_{k+1}=x_1.
}
\]

No assumption `q_i!=1` has entered. The only new issue relative to PC-103 is whether the limiting factors with `q_i=1` are jointly integrable at the boundary.

## 3. Reciprocal edges form an integrable forest whenever one edge is separated

Let

\[
E_1=\{i:q_i=1\}.
\]

If at least one cyclic edge has `q_i!=1`, then `E_1` is a proper subset of the edges of the cycle. Hence the graph consisting of the singular edges is a disjoint union of finite paths.

It suffices to prove integrability on one path of `r` singular edges with vertices `x_0,...,x_r`. Set

\[
u_i=1-x_i.
\]

Then

\[
1-x_{i-1}x_i
=u_{i-1}+u_i-u_{i-1}u_i
\ge\frac{u_{i-1}+u_i}{2}.
\]

For edge `i=1,...,r`, choose

\[
\theta_i=\frac{r+1-i}{r+1}.
\]

Weighted AM-GM gives

\[
u_{i-1}+u_i
\ge u_{i-1}^{\theta_i}u_i^{1-\theta_i}.
\]

Multiplying the resulting bounds is especially clean: every vertex receives total exponent exactly `r/(r+1)`. Thus

\[
\boxed{
\prod_{i=1}^r\frac1{1-x_{i-1}x_i}
\le
2^r\prod_{i=0}^r
u_i^{-r/(r+1)}.
}
\]

Since `r/(r+1)<1`, the right-hand side is integrable on `[0,1]^{r+1}`. Different path components involve disjoint vertex sets, so their bounds multiply. Therefore

\[
\boxed{
\prod_{i\in E_1}\frac1{1-x_ix_{i+1}}
\in L^1([0,1]^k)
}
\]

for every proper singular-edge subset of the cycle.

This is also the exact power-counting boundary. If **every** edge is singular, the singular graph is the whole cycle; simultaneous scaling near the all-one corner has equal denominator and integration dimension and gives the familiar logarithmic criticality rather than the forest gain of one vertex per path component.

## 4. Dominated convergence identifies the ordinary trace with the improper cube

For `0<=t<=1` and `q=1`,

\[
0\le\sum_{m=0}^M t^m\le\frac1{1-t}.
\]

For a fixed root of unity `q!=1`, define

\[
c_q=\min_{0\le t\le1}|1-qt|>0.
\]

Then

\[
\left|\sum_{m=0}^M(qt)^m\right|
=\left|\frac{1-(qt)^{M+1}}{1-qt}\right|
\le\frac2{c_q}.
\]

Hence the finite-section integrands in Section 2 are dominated, uniformly in `M`, by a constant times the integrable forest kernel from Section 3. Away from a measure-zero boundary set the geometric factors converge pointwise. Dominated convergence therefore gives

\[
\boxed{
\lim_{M\to\infty}S_M
=
A\int_{[0,1]^k}
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-q_i x_ix_{i+1}},
}
\]

where the integral is an **ordinary absolutely convergent improper integral**.

Under the operator-order hypothesis of Section 1, the left side is independently the ordinary trace of `W`. Thus

\[
\boxed{
\operatorname{Tr}
(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k})
=
A\int_{[0,1]^k]
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-q_i x_ix_{i+1}}
}
\]

with the obvious correction that the integration domain in the displayed formula is `[0,1]^k`.

The bracket typo in the compact display is purely typographical; the exact formula is the preceding boxed identity with domain `[0,1]^k`. No Abel or other regularization is being introduced.

## 5. Allowing `q_i=1` does not change the hyperlogarithmic reduction class

PC-103 proves linear reducibility of the same rational cycle integral by a parity-adapted variable order. Algebraically, that proof uses only that the edge phases lie in a finite multiplicative group. The identity element causes no new polynomial type.

The polynomial-reduction class remains

\[
x,
\qquad A-Bx,
\qquad Ax-By,
\qquad A,B\in\langle q_1,\ldots,q_k\rangle.
\]

Resultants stay in the same affine/link class. For even cycle length the alternating independent-set elimination removes every bilinear edge. For odd cycle length the only possible terminal degree-two obstruction is still the binomial identified in PC-103; the chain-closing factor is proportional to

\[
1-\alpha_k^2x_k^2
=(1-\alpha_kx_k)(1+\alpha_kx_k).
\]

Setting some `q_i=1` can merge factors or put a letter at the endpoint `1`, but it cannot create a non-cyclotomic letter or an irreducible higher-degree factor. Standard hyperlogarithmic endpoint regularization handles such intermediate `0/1` collisions; here it is only an evaluation device, because Section 4 has already proved that the original multivariate integral is absolutely convergent and selects an ordinary value.

If `N` is a common order of the `alpha_i`, every final nonzero letter lies in `mu_{2N}`. With the same regularized-hyperlogarithm convention as PC-103,

\[
\boxed{
\operatorname{Tr}
(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k})
\in
\mathbb Q(\mu_{2N})\cdot\operatorname{MPV}_{\le k}(2N)
}
\]

whenever the word has an ordinary adjacent separated pair.

## 6. Every finite nonconstant completed-shell word satisfies the hypothesis

Let

\[
W_{\mathbf n}=\Gamma_{n_1}\cdots\Gamma_{n_k},
\qquad
k\ge2,
\qquad n_i>1,
\]

and suppose the label sequence is nonconstant. Then some ordinary adjacent labels satisfy

\[
n_j\neq n_{j+1}
\qquad(1\le j<k),
\]

because equality of every ordinary adjacent pair would force all labels to be equal.

For every root tuple

\[
\alpha_i\in P_{n_i}^*,
\]

exact order is preserved by inversion. Therefore

\[
\alpha_j\alpha_{j+1}=1
\quad\Longrightarrow\quad
\operatorname{ord}(\alpha_j)=\operatorname{ord}(\alpha_{j+1}),
\]

contradicting `n_j!=n_{j+1}`. So **every** root word in the finite expansion of `W_n` has the trace-class core required above.

Since

\[
W_{\mathbf n}
=(-1)^k
\sum_{\alpha_i\in P_{n_i}^*}
\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k},
\]

we may take ordinary traces term by term. With

\[
N=\operatorname{lcm}(n_1,\ldots,n_k),
\]

each term lies in the same cyclotomic hyperlogarithm algebra, and the sum is finite. Hence

\[
\boxed{
\operatorname{Tr}(\Gamma_{n_1}\cdots\Gamma_{n_k})
\in
\mathbb Q(\mu_{2N})\cdot\operatorname{MPV}_{\le k}(2N)
}
\]

for **every finite nonconstant shell word**, including arbitrary repetitions and reciprocal root channels at repeated-shell junctions.

The concrete word `Gamma_3 Gamma_2 Gamma_3`, which PC-084 used as the model repeated-shell case, is therefore not a residual regularization loophole. Root tuples with reciprocal first/last roots merely contribute a single singular closing edge `1-x_3x_1`; that edge is integrable because the two order-changing edges are nonsingular.

## 7. Constant-shell powers are a genuine boundary, not a missing case

The conclusion must not be extended to `Gamma_n^k` by formal analogy. PC-075 gives a nontrivial absolutely continuous essential spectrum for `Gamma_n` when `n>2`; therefore a positive power is generally noncompact and cannot be trace class. There is no ordinary operator trace to classify by the argument above.

At root level this obstruction is visible in reciprocal alternating words. A word may have no separated pair in its actual operator order even though a closing phase is nonsingular. Its scalar finite-section cube can still converge conditionally or even through the forest bound, but that does not make the operator trace class — exactly the distinction isolated in PC-086. For even alternating cycles one can also reach the full singular cycle, where the cube itself has logarithmic criticality.

Thus the correct finite boundary is sharp for the present method:

\[
\boxed{
\text{nonconstant completed-shell word}
\Longrightarrow
\text{ordinary trace + cyclotomic hyperlogarithm},
}
\]

while constant-shell powers require a different relative/renormalized question and cannot be inserted into the ordinary-trace theorem.

## 8. Prior-art and novelty audit

The function class and reduction technology are classical.

- Erik Panzer, **Algorithms for the symbolic integration of hyperlogarithms with applications to Feynman integrals**, *Computer Physics Communications* 188 (2015), 148–166, DOI `10.1016/j.cpc.2014.10.019`, gives the standard hyperlogarithmic integration, polynomial-reduction, and regularized-limit machinery for linearly reducible rational integrals. This is already the main reduction anchor in `research/prime_circle/SOURCES.md` for PC-102/PC-103.
- A. B. Goncharov, **Multiple polylogarithms, cyclotomy and modular complexes**, *Mathematical Research Letters* 5 (1998), 497–516, DOI `10.4310/MRL.1998.v5.n4.a7`, supplies the classical multiple-polylogarithm special-value algebra at roots of unity.
- The operator input is not new abstract trace-ideal theory: PC-084/PC-086 already reduce the finite-section issue to one separated trace-class pair plus bounded strong-* factors. The new point here is to combine that exact operator boundary with the elementary forest integrability estimate, removing the cyclic-separation restriction from the **completed nonconstant shell** period classification.

Directed checks around linearly reducible Euler/Feynman integrals, endpoint-singular hyperlogarithmic integration, and cyclotomic multiple polylogarithms found established general technology rather than a new transcendental class. No historical novelty is claimed for hyperlogarithms, endpoint regularization, or the forest power-counting argument. The durable Prime-Circle result is the closure of the repeated-shell finite ordinary-trace boundary left open by PC-103.

## 9. RH consequence

PC-082 showed that higher Hardy traces can contain relational information beyond pairwise cyclotomic resultants. PC-100, PC-102, and PC-103 then classicalized all finite cyclically separated cycles. The remaining repeated-shell escape now closes as well:

\[
\boxed{
\text{every fixed finite nonconstant Prime-Circle Hardy shell trace}
\longrightarrow
\text{absolutely convergent cyclotomic Euler integral}
\longrightarrow
\text{finite cyclotomic hyperlogarithm period}.
}
\]

So repetition, reciprocal root channels, and finite mixed-shell ordering do not by themselves supply a new RH function class, a geometry-forced free complex parameter, a gamma factor, an `s\leftrightarrow1-s` symmetry, a positivity criterion, or a Riemann-zero divisor.

The surviving Hardy boundary is no longer a finite-word period question. It lies in intrinsically organized **infinite-shell** limits, Fredholm/relative determinants or other global Hardy constructions, shell-dependent structures introduced before taking such a limit, or outside this branch in the global nonlinear uniformization/monodromy geometry. Constant-shell powers may enter only through a separately justified relative or renormalized construction; their lack of an ordinary trace is not evidence for an RH mechanism.

## 10. Falsification surface

1. For any root word claimed to have an ordinary trace here, identify an actual adjacent pair `1<=j<k` with `alpha_j alpha_{j+1}!=1`; a merely separated closing edge is insufficient for the operator argument.
2. Verify the PC-084 separated-pair finite-section estimate and the standard strong-* trace-ideal extension to the surrounding bounded factors.
3. Expand the finite trace directly and recover the geometric-sum cube formula before taking any limit.
4. The set of edges with `q_i=1` must be a proper subset of the cycle. Decompose it into paths and check the displayed weighted-AM-GM bound; every path vertex must receive exponent exactly `r/(r+1)<1`.
5. Use the forest kernel as an `M`-independent dominator. If a full singular cycle occurs, the dominated-convergence theorem above does not apply.
6. Re-run PC-103 polynomial reduction with `q_i=1` allowed. Vanishing resultants or merged factors may simplify the alphabet but must not generate a new irreducible polynomial; the odd terminal quadratic must still split over `mu_{2N}`.
7. For a nonconstant shell-label sequence, verify that some ordinary adjacent labels differ and hence every primitive-root tuple has a separated pair at that position.
8. Do not infer an ordinary trace for constant-shell powers from convergence of selected scalar finite sections. PC-075's essential spectrum supplies the matched operator-level obstruction.
9. The result concerns fixed finite words only. No infinite-shell sum, Fredholm determinant, analytic continuation, or RH-sensitive parameter follows from this theorem without a separate convergence and novelty argument.
