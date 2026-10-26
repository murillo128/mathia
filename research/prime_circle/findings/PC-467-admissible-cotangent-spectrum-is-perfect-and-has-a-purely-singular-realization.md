# PC-467 — The admissible cotangent spectrum is perfect and has a purely singular realization

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE. The full limiting spectral set identified in PC-466 has no isolated points and is uncountable. Nevertheless, one admissible moving-center limit realizes that entire set with **no absolutely continuous spectral part**. Its cross-block interaction can have arbitrarily small trace norm. The finite Cauchy identities and trace-class perturbation theorem are classical; their admissible-pattern application is derived here. This does not decide gaps, Lebesgue measure, or the pure-point versus singular-continuous decomposition, and gives no RH implication or historical-priority claim.

## 1. Precise statement

A nonempty finite `F subset Z` is admissible if `|F mod p|<p` for every prime `p`. Define
\[
(L_F)_{ab}=\begin{cases}i/[\pi(a-b)],&a\ne b,\\0,&a=b,\end{cases}
\qquad
\Sigma=\overline{\bigcup_{F\text{ finite nonempty admissible}}\sigma(L_F)}.
\tag{1}
\]
By [[research/prime_circle/findings/PC-466-full-primorial-cotangent-spectra-converge-to-the-admissible-pattern-spectrum]], this compact set is the uniform-in-refinement Hausdorff limit of the conductor-scaled primorial cotangent spectra. It contains `0` and both nonzero edges `+/- beta`, with `beta=sup_F ||L_F||`.

**Theorem.**

1. `Sigma` is perfect: every one of its points is an accumulation point. In particular it is uncountable; it is not a discrete collection of the finite-pattern spectral atoms.
2. For every `epsilon>0` there are an admissible infinite `S subset Z`, a partition into finite translated admissible blocks `S=disjoint union G_j`, and
\[
D=\bigoplus_j L_{G_j}\quad\text{on }\ell^2(S)
\]
such that the unchanged Cauchy operator satisfies
\[
L_S=D+K,\qquad K=K^*\in\mathcal S_1,
\qquad \|K\|_1<\varepsilon,
\tag{2}
\]
\[
\boxed{\quad \sigma(L_S)=\sigma_{\rm ess}(L_S)=\Sigma,
\qquad \mathcal H_{\rm ac}(L_S)=\{0\}.\quad}
\tag{3}
\]
Here `S_1` denotes trace-class operators and `H_ac` the absolutely continuous spectral subspace with respect to Lebesgue measure. Thus “purely singular” allows atomic and singular-continuous spectral measures; it does **not** mean purely singular continuous.

Extending these operators by zero to `ell^2(Z)` preserves (3), since `0 in Sigma`. PC-465 then realizes this `L_S` as a strong moving-center limit along any prescribed sequence of primorial cutoffs tending to infinity and any positive integer refinements. The center choices and block placements are existence constructions, not a canonical selection forced by the finite geometry.

## 2. Classical finite Cauchy identities give strict interlacing

This section works for **any** distinct real coordinates `F={a_1,...,a_n}`, without admissibility. Let `X=diag(a_1,...,a_n)` and `e=(1,...,1)^T`. Entrywise,
\[
[X,L_F]=\frac i\pi(ee^*-I).
\tag{4}
\]
For any eigenvector `v`, self-adjointness makes the expectation of this commutator zero. Hence
\[
|e^*v|^2=\|v\|^2.
\tag{5}
\]
Every eigenspace is one-dimensional: otherwise it would contain a nonzero vector orthogonal to `e`, contradicting (5). In particular, a unit eigenvector has `|sum_a v_a|=1`. Simplicity and this sum identity are classical generalized Hilbert-matrix facts; see Preissmann–Leveque, Corollary 1 and Lemma 7 below.

There is a useful exact noncancellation identity for an added real coordinate `b notin F`. Set `d_a=(b-a)^(-1)` and `R_b=diag(d_a)`. Then
\[
[R_b,L_F]=\frac i\pi\bigl(dd^*-\operatorname{diag}(d_a^2)\bigr).
\tag{6}
\]
Indeed `(d_a-d_c)/(a-c)=d_a d_c` off the diagonal. Taking the expectation in an eigenvector gives
\[
\left|\sum_{a\in F}\frac{v_a}{b-a}\right|^2
=\sum_{a\in F}\frac{|v_a|^2}{(b-a)^2}>0.
\tag{7}
\]
Thus every eigenvector couples nontrivially to the added coordinate, including when `b` lies between old coordinates. This is stronger than merely excluding finitely many zeros of a rational coupling function.

In an orthonormal eigenbasis of `L_F`, the enlarged matrix is an arrowhead matrix with old eigenvalues `lambda_1<...<lambda_n`, new diagonal entry zero, and couplings `g_j` satisfying
\[
|g_j|^2=\frac1{\pi^2}\sum_{a\in F}
\frac{|v_{j,a}|^2}{(b-a)^2}>0.
\tag{8}
\]
Its characteristic polynomial evaluated at `lambda_j` is
`-|g_j|^2 prod_(k!=j)(lambda_j-lambda_k)`, so old and new spectra are disjoint. Cauchy interlacing is therefore strict:
\[
\mu_1<\lambda_1<\mu_2<\cdots<\lambda_n<\mu_{n+1}.
\tag{9}
\]
No assumption that a generic Hermitian principal compression strictly interlaces is being made; (7) supplies exactly the missing condition.

## 3. Far admissible extensions remove every isolated spectral point

Fix a finite admissible `F` of size `n` and a member `a_0`. Let
\[
Q=\prod_{p\le n+1}p,
\qquad b_k=a_0+kQ>\max F.
\tag{10}
\]
For every prime at most `n+1`, the new point repeats an existing residue of `F`; larger primes cannot be covered by `n+1` points. Thus every such `F union {b_k}` is admissible. This is the admissible-extension mechanism of PC-463, now applied to **all** eigenvalues instead of just the top one.

In the old coordinates plus the new coordinate,
\[
\left\|L_{F\cup\{b_k\}}-(L_F\oplus0)\right\|
=\frac1\pi\left(\sum_{a\in F}\frac1{(b_k-a)^2}\right)^{1/2}
\longrightarrow0.
\tag{11}
\]
Hermitian spectral perturbation gives, for each `lambda in sigma(L_F)`, eigenvalues of the enlarged blocks converging to `lambda`. By (9), none equals `lambda`. This includes an old zero eigenvalue: one must compare with `L_F direct-sum 0`, including its possible repeated zero, rather than assume continuity of a fixed index in the old list.

Consequently every member of the union in (1) is an accumulation point of that union. Its closure has no isolated point: an isolated point of a closure must belong to the dense defining set and would then contradict the preceding conclusion. A nonempty perfect closed subset of the real line is uncountable, proving part 1. This elementary topological conclusion does not show that `Sigma` contains an interval or has positive measure.

## 4. Admissible gluing with a summable trace-norm budget

Enumerate all finite nonempty admissible integer shapes modulo translation as `F_j`, repeating each shape infinitely often. This is a countable collection. We choose translations `G_j=t_j+F_j` inductively so that the finite partial union `U_j=union_(i<=j) G_i` stays admissible and the total absolute cross-block kernel is summable.

The needed gluing fact from PC-465 is elementary. Given finite admissible `U,F`, put `n=|U|+|F|`. For each prime `p<=n`, select omitted residues `r_p` of `U` and `s_p` of `F`, and impose
\[
t\equiv r_p-s_p\pmod p.
\tag{12}
\]
Then `U union (t+F)` misses `r_p` modulo `p`. Larger primes are handled by cardinality. CRT gives a translation class, and adding arbitrarily large multiples of its modulus puts the new block beyond any prescribed distance. In particular, no old block ever moves.

At stage `j>=2`, choose the distance `d_j` from `G_j` to `U_(j-1)` large enough that
\[
\frac{2|U_{j-1}|\,|F_j|}{\pi d_j}<\varepsilon 2^{-j}.
\tag{13}
\]
Use (12) to realize this separation while preserving admissibility. The increasing union `S=union_j G_j` is admissible: covering every residue modulo a prime would have finitely many witnesses already in one partial union.

Each cross-block matrix entry is a rank-one operator of trace norm equal to its absolute value. Counting both directions, (13) gives the **entrywise nuclear majorant**
\[
\sum_{j\ge2}\ \sum_{a\in G_j,\ b\in U_{j-1}}
\frac2{\pi|a-b|}
<\sum_{j\ge2}\varepsilon2^{-j}<\varepsilon.
\tag{14}
\]
Therefore the series of cross-block matrix units converges in trace norm to a self-adjoint `K` with the bound in (2). This is an absolute estimate for a deliberately very sparse block placement, not absolute summability of the full integer Cauchy kernel. Each stage counts every interaction with preceding blocks, so future blocks do not invalidate the total budget.

The block-diagonal `D` is bounded by `beta` and has a complete orthonormal basis of finite-block eigenvectors. The admissible Cauchy form defines a bounded self-adjoint `L_S` with the same bound, by PC-465. Its matrix entries agree with those of `D+K`, hence these bounded operators agree. This proves (2) without replacing or suppressing any actual Cauchy interaction.

## 5. The full spectral set survives while the absolutely continuous part vanishes

Every finite shape occurs infinitely often among the blocks. Thus each eigenvalue in the defining union (1) is an eigenvalue of `D` of infinite multiplicity. Direct-sum spectral theory, or a uniform blockwise resolvent outside the closed union, gives
\[
\sigma(D)=\sigma_{\rm ess}(D)=\Sigma.
\tag{15}
\]
Although `D` has an eigenbasis, its spectral **set** is the uncountable closure of a countable set of eigenvalues. There is no conflict between this fact and part 1.

Since `K` is compact, Weyl's theorem preserves essential spectrum:
\[
\sigma_{\rm ess}(L_S)=\Sigma.
\tag{16}
\]
One must separately exclude possible spectral points outside this set; compact perturbation alone does not do so. For any `lambda in sigma(L_S)`, bounded self-adjointness and density of finite-support vectors give finite-support unit approximate eigenvectors `v`. If `F=supp(v) subset S`, compressing the residual yields
\[
\operatorname{dist}(\lambda,\sigma(L_F))
\le\|(L_F-\lambda)v\|
\le\|(L_S-\lambda)v\|.
\tag{17}
\]
Every such `F` is admissible. Taking the residual to zero proves `sigma(L_S) subset Sigma`, which together with (16) gives the first equality in (3).

Finally, the Kato–Rosenblum theorem makes the absolutely continuous parts of `D` and `D+K` unitarily equivalent under a self-adjoint trace-class perturbation. The eigenbasis of `D` makes its absolutely continuous subspace zero. Hence `H_ac(L_S)={0}`. Hilbert–Schmidt control alone would not license this argument, nor does trace-class control preserve the singular-continuous or atomic parts individually.

## 6. Mathematical delta, matched controls and prior art

PC-463 gives strict growth of maximal eigenvalues; PC-466 gives the whole spectral-set limit and an essential-spectrum realization but leaves its topology and spectral type undetermined. The present result removes isolated points throughout that limit and constructs a realization with no absolutely continuous part. Therefore full essential-spectrum recovery, even of an uncountable set, does not force an absolutely continuous channel for a moving-center realization.

The finite identities hold for arbitrary distinct real coordinates. The sparse trace-class construction works for any translation-invariant hereditary class of finite integer patterns that admits arbitrarily separated finite gluing, has uniformly bounded Cauchy blocks, and supplies a corresponding bounded infinite compression. Perfectness additionally uses arbitrarily far admissible singleton extensions. Arithmetic enters the modular preservation and the identification of `Sigma` with the original finite cotangent limits. These controls demonstrate generic mechanisms; they do not assert that `Sigma` itself has lost all arithmetic information.

Closest primary sources and exact roles:

- E. Preissmann and O. Leveque, *On generalized weighted Hilbert matrices*, **Pacific J. Math. 265** (2013), 199–219, [paper](https://msp.org/pjm/2013/265-1/pjm-v265-n1-p09-p.pdf), DOI `10.2140/pjm.2013.265.199`. Corollary 1 establishes simplicity and Lemma 7 gives (5), including a weighted version. Equations (4)–(9) above give a direct commutator/arrowhead proof for the required unweighted specialization. These finite identities are not new arithmetic structure.
- Y. B. Suris, *Why are the rational and hyperbolic Ruijsenaars–Schneider hierarchies governed by the same R-operators as the Calogero–Moser ones?*, [author manuscript](https://arxiv.org/abs/hep-th/9602160), equation (4.18). The rational Calogero–Moser rank-one commutator is exactly (4), with coupling `i/pi` and zero diagonal momenta. This is an additional classical boundary, not an imported Hamiltonian dynamics for Prime Circle.
- J. S. Howland, *On the Kato-Rosenblum theorem*, **Pacific J. Math. 123** (1986), 329–335, [paper](https://msp.org/pjm/1986/123-2/pjm-v123-n2-p05-s.pdf). Its opening theorem states the precise absolutely-continuous invariance used after (14), and the paper explains why analogous singular-part invariance fails. The trace-class hypothesis is established here by the explicit placement budget.

The local duplication check covered PC-463–PC-466 and targeted searches for perfect spectra, strict Cauchy interlacing and singular realizations. Structural literature searches found the finite simplicity/sum identities and perturbation mechanism in classical sources. No claim of historical novelty is made for their combination with admissible CRT gluing.

The result neither determines `beta`, gaps, Hausdorff dimension, Lebesgue measure, eigenvalue statistics nor spectral type for **every** admissible support. Even the constructed support's atomic versus singular-continuous split remains open here. Uncountability is not evidence of positive measure; absence of an absolutely continuous part is not evidence of a discrete spectral set. Actual prime-tuple occurrence, a canonical limiting chart, zeta-zero identification and critical-line selection are all outside the conclusion.

## 7. Validation and evidence boundary

The argument is analytic, not Lean-verified or independently adversarially approved. A deterministic standard-library Python audit used system LAPACK `zheev` through `ctypes` on **93** admissible integer shapes and **64** nonarithmetic rational-coordinate controls. It checked (5) on **673** eigenvectors, (7) on **2,405** eigenvector/extension pairs, **565** strict interlacings and perturbation bounds, and **11,973** entries of (6) in exact rational arithmetic. Maximum sum-identity error was below `6.0e-15`, maximum relative coupling-identity error below `6.1e-15`, and the smallest tested strict interlacing margin exceeded `2.4e-6`. Added coordinates included points on either side and between old coordinates; odd-dimensional zero modes and singletons were included.

Separately, **25** exact CRT gluings produced an admissible 106-point union with 40-digit offsets. Every stage satisfied its allocated rational majorant, using `pi>3`; the total cross-block trace majorant was below `0.05073` against a budget of `1/16`. These checks audit finite formulas, congruences and the summable budget, not perfectness, infinite spectral type or Kato–Rosenblum itself. Scratch code and output remain outside Git.

The decisive proof checks are the nonzero coupling at **every** old eigenvalue, preserving admissibility under distant extension, including the extra zero in (11), counting both directions in the trace estimate, repeating all finite shapes, excluding off-set spectrum via (17), and keeping spectral-set topology separate from spectral-measure type. No compute or formalization handoff is warranted: the finite identities already have an exact classical source, while the new application is the analytic gluing/perturbation passage rather than a distinct bounded formal fertility target.
