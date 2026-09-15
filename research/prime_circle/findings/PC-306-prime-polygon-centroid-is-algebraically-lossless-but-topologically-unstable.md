# PC-306 — prime-polygon centroid is algebraically lossless but topologically unstable

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the information-threshold interpretation left open by PC-304/PC-305.

PC-304 and PC-305 give constructive reconstruction bounds for the oriented Prime-Circle source: the complete additive DFT is available by tensor degree `q-1`, while the actual equal-weight prime support can already be reconstructed from `L_q=pi(q)-2` consecutive power moments, or from degree `d` and window width `B` once `dB>=L_q`. Those statements are correct sufficient bounds, but they do not describe an intrinsic information threshold.

At prime conductor there is a stronger finite algebraic fact. The normalized centroid of **any nonempty vertex subset of the regular `q`-gon already determines that subset exactly**. Equivalently, the first normalized Fourier coefficient is injective on the class of uniform subset measures. For the canonical Prime-Circle source this means that the degree-one oriented moment already encodes the entire prime support if it is retained as an exact element of the cyclotomic field.

This exact injectivity is nevertheless maximally misleading as an analytic information claim. A prime support and its one-step rotation are disjoint, hence have total-variation distance one, while their first `K=o(q)` Fourier coefficients differ by at most `2*pi*K/q` in sup norm. In particular, even at the PC-305 constructive scale `K=L_q=O(q/log q)`, two disjoint sources become `O(1/log q)`-close in the observed Fourier packet. Any stable discriminator with a fixed output margin must therefore amplify by at least order `q/K`.

The resulting boundary is sharper than a new reconstruction theorem: **exact cyclotomic-field injectivity and stable analytic information are different notions.** Future Prime-Circle proposals based on incomplete Fourier/tensor packets must specify the topology, precision and conditioning in which the source information survives. Exact algebraic recoverability of the input source from one scalar is classical cyclotomic rigidity, not an RH mechanism.

Let `n>=2`, let

\[
\zeta_n=e^{2\pi i/n},
\]

and for every nonempty subset `A subset Z/nZ` define its normalized centroid

\[
 b_n(A):=\frac1{|A|}\sum_{a\in A}\zeta_n^a.
\tag{1}
\]

## 1. Prime conductor is exactly the injective-centroid case

### Theorem

For `n>=2`, the map

\[
A\longmapsto b_n(A)
\]

on nonempty subsets of `Z/nZ` is injective **if and only if `n` is prime**.

Assume first that `n=q` is prime. Let `A,B` be nonempty and suppose

\[
 b_q(A)=b_q(B).
\tag{2}
\]

Write `r=|A|` and `s=|B|`. Then

\[
P(X):=
 s\sum_{a\in A}X^a-r\sum_{b\in B}X^b
\in\mathbb Z[X]
\tag{3}
\]

has degree at most `q-1` and satisfies

\[
P(\zeta_q)=0.
\tag{4}
\]

The minimal polynomial of `zeta_q` over `Q` is

\[
\Phi_q(X)=1+X+\cdots+X^{q-1},
\tag{5}
\]

which has degree `q-1`. Hence (4) forces

\[
P(X)=c\Phi_q(X)
\tag{6}
\]

for some rational `c`. Evaluating at `X=1` gives

\[
P(1)=sr-rs=0=cq,
\]

so `c=0` and therefore `P=0`. Coefficientwise,

\[
 s\,1_A(j)=r\,1_B(j)
\qquad(j\bmod q).
\tag{7}
\]

Because both sets are nonempty, (7) forces identical supports and then `r=s`. Thus

\[
\boxed{b_q(A)=b_q(B)\Longrightarrow A=B.}
\tag{8}
\]

Conversely, let `n` be composite and choose a prime divisor `p|n`. Put

\[
H:=\left\{0,\frac np,2\frac np,\ldots,(p-1)\frac np\right\}
\subset\mathbb Z/n\mathbb Z.
\tag{9}
\]

Since `n/p>=2`, the subsets `H` and `H+1` are distinct. But

\[
\sum_{h\in H}\zeta_n^h
=
\sum_{j=0}^{p-1}\zeta_p^j
=0,
\]

and rotation preserves the zero centroid, so

\[
\boxed{b_n(H)=b_n(H+1)=0.}
\tag{10}
\]

This proves the converse and hence the exact characterization.

The statement is deliberately about **normalized** centroids, because the Prime-Circle source moments in PC-302--305 are expectations under uniform source laws. The same proof also explains why the prime case is exceptional: among the `q` vertices the only rational linear relation is the full cyclotomic relation (5), and normalization removes that remaining ambiguity.

## 2. The degree-one oriented moment already encodes the canonical prime source

The prime-case proof is not merely existential. Since

\[
1,\zeta_q,\ldots,\zeta_q^{q-2}
\]

is a `Q`-basis of `Q(zeta_q)`, the exact field coordinates of `b_q(A)` recover `A` directly.

If `q-1 notin A`, then

\[
b_q(A)=\frac1r\sum_{a\in A}\zeta_q^a
\tag{11}
\]

has basis coefficients `1/r` on `A` and `0` elsewhere. If `q-1 in A`, use

\[
\zeta_q^{q-1}=-\sum_{j=0}^{q-2}\zeta_q^j
\]

to obtain coefficients `0` on `A intersect {0,...,q-2}` and `-1/r` on its complement. Thus the exact cyclotomic coordinate vector identifies both the membership pattern and the cardinality.

For the canonical source of PC-302--305,

\[
P_q=\{\ell:2<\ell<q,\ \ell\text{ prime}\},
\qquad
L_q=|P_q|,
\tag{12}
\]

and `q>=5` is odd. Every element of `P_q` is odd whereas `q-1` is even, so `q-1 notin P_q`. Its first normalized Fourier coefficient is

\[
F_q(1)=\frac1{L_q}\sum_{\ell\in P_q}\zeta_q^\ell.
\tag{13}
\]

Equation (11) therefore says that **the exact algebraic number `F_q(1)` already determines `P_q` completely**.

In the oriented frame used in PC-296--305,

\[
y_s=x_{1,s}(1)=N^{-1/2}\zeta_q^s,
\]

so the degree-one source mean is simply

\[
\mathbb E_{s\sim\nu_q}y_s
=N^{-1/2}F_q(1).
\tag{14}
\]

Consequently the tensor hierarchy is already algebraically lossless at degree one on the restricted class of uniform subset sources. PC-305's condition

\[
dB\ge L_q
\]

remains a useful **constructive Newton--Girard sufficient bound from ordinary consecutive complex moments**, but it cannot be interpreted as the onset of exact identifiability. PC-305 already explicitly leaves open earlier reconstruction; (8)--(14) identify the extreme endpoint of that caveat.

This does not produce new arithmetic information. It says that one exact complex scalar in a cyclotomic field of degree `q-1` can carry `q-1` rational coordinates. Treating it as one real/complex degree of freedom would silently discard the algebraic precision present in the representation.

## 3. Exact injectivity is violently nonuniform in the ordinary Fourier topology

The algebraic conclusion above becomes very different once the growing-conductor problem is placed in an analytic topology.

For any nonempty `A subset Z/qZ`, let `nu_A` be the uniform probability measure on `A` and define

\[
F_A(k):=\widehat\nu_A(k)
=\frac1{|A|}\sum_{a\in A}\zeta_q^{ka}.
\tag{15}
\]

Translate the support by one residue. Then

\[
F_{A+1}(k)=\zeta_q^kF_A(k),
\tag{16}
\]

and hence, for `|k|<=q/2`,

\[
|F_{A+1}(k)-F_A(k)|
=|\zeta_q^k-1|\,|F_A(k)|
\le 2\sin\frac{\pi|k|}{q}
\le \frac{2\pi|k|}{q}.
\tag{17}
\]

Therefore for the low-frequency packet

\[
\mathcal F_K(A):=(F_A(k))_{1\le |k|\le K}
\]

with `K<q/2`, one has

\[
\boxed{
\|\mathcal F_K(A+1)-\mathcal F_K(A)\|_{\ell^\infty}
\le \frac{2\pi K}{q}.
}
\tag{18}
\]

Now take the actual prime source `A=P_q`. Since its elements are odd primes larger than two, `P_q+1` consists entirely of even residues. There is no wraparound because every `ell in P_q` satisfies `ell<=q-2`. Hence

\[
P_q\cap(P_q+1)=\varnothing.
\tag{19}
\]

The two uniform source measures therefore have maximal total-variation separation,

\[
\|\nu_{P_q}-\nu_{P_q+1}\|_{\rm TV}=1,
\tag{20}
\]

while (18) gives

\[
\|\mathcal F_K(P_q+1)-\mathcal F_K(P_q)\|_\infty
\le \frac{2\pi K}{q}.
\tag{21}
\]

Thus for every `K=o(q)`, the observed Fourier packets converge to each other even though the underlying supports stay disjoint. In particular, using the PC-305 source cardinality

\[
L_q=\pi(q)-2=O(q/\log q),
\]

one gets

\[
\boxed{
\|\mathcal F_{L_q}(P_q+1)-\mathcal F_{L_q}(P_q)\|_\infty
=O(1/\log q)\to0.
}
\tag{22}
\]

This is the same packet size at which Newton--Girard reconstruction is sufficient in PC-305. Hence exact finite-level recoverability and uniform conditioning separate dramatically: a sequence of packets can converge in sup norm while the exactly recovered supports remain maximally different.

There is also an immediate quantitative obstruction for any stable downstream discriminator. If

\[
G_q:\mathbb C^{2K}\to Y
\]

is `C_q`-Lipschitz with respect to the packet sup norm and some output metric `d_Y`, then

\[
d_Y\bigl(G_q(\mathcal F_K(P_q)),
G_q(\mathcal F_K(P_q+1))\bigr)
\le C_q\frac{2\pi K}{q}.
\tag{23}
\]

To maintain a fixed positive separation `delta` between this matched source/control pair, one must have

\[
\boxed{C_q\ge \frac{\delta}{2\pi}\frac qK.}
\tag{24}
\]

At `K=L_q` this already requires logarithmically growing amplification; for fixed `K` it requires linear amplification in `q`. Any proposal that claims a stable arithmetic effect from such low-order packets must therefore exhibit and control this amplification rather than appeal to exact identifiability alone.

## 4. Prior-art and novelty audit

The algebra behind Section 1 is classical cyclotomic theory. T. Y. Lam and K. H. Leung, **On Vanishing Sums of Roots of Unity**, *Journal of Algebra* 224 (2000), 91--109, DOI `10.1006/jabr.1999.8089`, gives a broad classification framework for vanishing sums of roots of unity. For prime conductor the minimal-polynomial argument above is elementary and already proves the required rigidity. No novelty is claimed for that theorem as abstract mathematics.

The stability distinction is equally classical in neighboring inverse-moment and super-resolution theory. Emmanuel Candès and Carlos Fernandez-Granda, **Towards a Mathematical Theory of Super-Resolution**, *Communications on Pure and Applied Mathematics* 67 (2014), 906--956, DOI `10.1002/cpa.21455`, makes low-frequency recovery/stability depend on geometric separation. Stefan Kunis, Thomas Peter, Tim Römer and Ulrich von der Ohe, **A multivariate generalization of Prony's method**, *Linear Algebra and its Applications* 490 (2016), 31--47, DOI `10.1016/j.laa.2015.10.037`, likewise separates finite-moment uniqueness from quantitative reconstruction conditions.

Accordingly the project-local contribution is not a new roots-of-unity uniqueness theorem or a new super-resolution theorem. It is the boundary these classical facts impose on the Prime-Circle oriented-frame program: **at prime conductor, one exact degree-one scalar is already a lossless algebraic encoding of every uniform subset source, while the same encoding becomes arbitrarily ill-conditioned in the natural growing-`q` complex/Fourier topology.** This removes “number of exact Fourier coefficients” as a meaningful standalone measure of information gain.

The proof is self-contained and the references are novelty/stability context rather than load-bearing dependencies, so no new `SOURCES.md` anchor is required.

## 5. Falsification and finite controls

The prime injectivity theorem is directly falsifiable. For a small prime `q`, enumerate all nonempty subsets, compute the exact cyclotomic centroids and test for collisions. Equations (3)--(8) predict none. For composite `n`, (9)--(10) give an explicit collision without search; for example at `n=6`, the two triangles

\[
\{0,2,4\},\qquad\{1,3,5\}
\]

both have centroid zero.

The topological statement has an equally direct numerical control. For each prime `q`, compute the packets for `P_q` and `P_q+1`; their entrywise ratio must be exactly `zeta_q^k` wherever `F_{P_q}(k)` is nonzero, and the packet sup distance must satisfy (21). Their support overlap must be zero. Any violation of these finite identities refutes the stated mechanism.

The conclusion is also deliberately limited. Equation (24) is a lower bound on the conditioning required to separate one canonical matched pair. It does not prove that every growing-order construction is unstable, nor that every geometry-forced operator has bounded Lipschitz constant. A singular or renormalized operation may amplify the shrinking packet difference, but then that amplification and its topology become the mathematical mechanism that must be justified.

## 6. Consequence for the live Prime-Circle frontier

PC-303--305 classify a large oriented-frame branch in terms of finite polyspectra and source reconstruction. The present result sharpens what “partial information” can mean there. If exact cyclotomic arithmetic is allowed at each finite level, **there is no nontrivial information threshold at all for uniform subset sources at prime conductor: the first moment is injective**. If instead the research question concerns a growing-level operator limit, exact injectivity is insufficient because the inverse map is not uniformly continuous in the natural low-frequency packet topology, as the disjoint translated-prime control demonstrates.

A surviving mechanism therefore has to state which of these regimes it uses. It may exploit a geometry-forced operation whose singular amplification is quantitatively controlled, a topology stronger than ordinary complex packet convergence that is itself intrinsic to the roots-of-unity model, or genuinely cross-level/mixed-conductor structure that is not equivalent to decoding each finite-level source and post-processing it. What no longer counts as evidence is the mere statement that a finite packet, determinant, tensor hierarchy or scalar “contains enough information” in the exact algebraic sense.

This is a classification/boundary result, not an RH bridge. It introduces no spectral parameter, gamma factor, functional equation, explicit-formula kernel or critical-line constraint; rather, it prevents exact finite-level encodability from being mistaken for such a mechanism.