# WP-153 — Natural-cutoff root spectral measure is a universal two-atom boundary law

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + NORMALIZED-ADJACENCY + LOCAL-SPECTRAL-MEASURE + NATURAL-SHELL-CUTOFF + TWO-ATOM-LIMIT + BOUNDED-FUNCTIONAL-CALCULUS + STAR-GRAPH-CLASSICALIZATION + PRIOR-ART-AUDITED`

## Claim

`WP-152` identifies the only non-strong fixed-shell defect of the natural arithmetic-size cutoff

\[
F_X=\{1,\ldots,X\}
\]

for the symmetrically normalized Prime-Circle resultant adjacency

\[
N_X=D_X^{-1/2}J_XD_X^{-1/2}.
\]

Every fixed non-root state satisfies `\|N_X\delta_m\|\to0`, while at the root `N_X\delta_1\rightharpoonup0` but

\[
\|N_X\delta_1\|^2\longrightarrow
c:=1-\frac1{\sqrt2}.
\tag{1}
\]

A possible residual escape is that higher returns, a resolvent, heat kernel, or another fixed spectral transform of `N_X` might retain arithmetic information that the first-step moving profile of `WP-152` does not show.

They do not. Let `\mu_{X,m}` be the local spectral probability measure of the self-adjoint contraction `N_X` at `\delta_m`, so

\[
\int_{-1}^{1}\lambda^k\,d\mu_{X,m}(\lambda)
=
\langle\delta_m,N_X^k\delta_m\rangle.
\tag{2}
\]

Then, under the same natural cutoff,

\[
\boxed{
\mu_{X,m}\Rightarrow\delta_0
\qquad(m\ge2\text{ fixed}),
}
\tag{3}
\]

whereas at the root

\[
\boxed{
\mu_{X,1}
\Rightarrow
\frac12\delta_{-\sqrt c}
+
\frac12\delta_{\sqrt c}.
}
\tag{4}
\]

Equivalently, for every fixed continuous `f:[-1,1]\to\mathbb C`,

\[
\boxed{
\langle\delta_1,f(N_X)\delta_1\rangle
\longrightarrow
\frac{f(\sqrt c)+f(-\sqrt c)}2,
}
\tag{5}
\]

while for every fixed `m\ge2`,

\[
\boxed{
\langle\delta_m,f(N_X)\delta_m\rangle
\longrightarrow f(0).
}
\tag{6}
\]

Thus **all fixed bounded continuous local spectral readouts collapse to a universal law**. The root retains only a scaled Bernoulli/Rademacher two-point distribution, and every other fixed shell becomes spectrally trivial. The arithmetic-specific prime-power interaction does not reappear at higher return order.

This is stronger than the first-step boundary-mass statement of `WP-152`. It closes fixed local powers, bounded spectral filters, heat responses, and off-spectrum local resolvents as ways of recovering hidden Weil data from the natural-cutoff normalized resultant escape. The remaining possibilities must change the test space with the cutoff, use a genuinely nonlocal/global observable, change the interaction before normalization, or assemble a finite--archimedean object before the universal star boundary layer forms.

## 1. The top-half prime leaves give an asymptotic two-step eigenrelation

Retain the notation of `WP-152`. For

\[
\frac X2<p\le X
\tag{7}
\]

prime, `p` is an exact leaf of the induced resultant graph on `F_X`: its only neighbor is the root `1`. Let `P_X^{\rm leaf}` be the orthogonal projection onto those leaf-prime coordinates and decompose

\[
N_X\delta_1=v_X+w_X,
\qquad
v_X:=P_X^{\rm leaf}N_X\delta_1.
\tag{8}
\]

`WP-152` proves that all root-neighbor squared mass outside this leaf layer is negligible and that the leaf mass converges to (1). Hence

\[
\boxed{
\|v_X\|^2=:c_X\longrightarrow c,
\qquad
\|w_X\|\longrightarrow0.
}
\tag{9}
\]

Write

\[
\alpha_{X,p}
:=
\langle\delta_p,N_X\delta_1\rangle
\qquad(X/2<p\le X).
\tag{10}
\]

Because each such `p` is an exact leaf and `N_X` is symmetric with zero diagonal,

\[
N_X\delta_p=\alpha_{X,p}\delta_1.
\tag{11}
\]

Therefore the whole leaf vector returns exactly to the root:

\[
N_Xv_X
=
\sum_{X/2<p\le X}\alpha_{X,p}^2\delta_1
=
\boxed{c_X\delta_1}.
\tag{12}
\]

Combining (8), (9), and the contraction bound `\|N_X\|\le1`,

\[
N_X^2\delta_1
=c_X\delta_1+N_Xw_X,
\]

so

\[
\boxed{
\|N_X^2\delta_1-c\delta_1\|
\le |c_X-c|+\|w_X\|
\longrightarrow0.
}
\tag{13}
\]

This is the load-bearing fact. Although `N_X\delta_1` itself has no strong limit, its second iterate returns asymptotically to the fixed root direction with the universal scalar `c`.

## 2. All root moments converge to a scaled Bernoulli law

Put

\[
A_X:=N_X^2.
\tag{14}
\]

Every `A_X` is a positive contraction. Equation (13) says

\[
A_X\delta_1=c\delta_1+\varepsilon_X,
\qquad
\|\varepsilon_X\|\to0.
\tag{15}
\]

For every fixed integer `k\ge1`, the telescoping identity

\[
A_X^k\delta_1-c^k\delta_1
=
\sum_{j=0}^{k-1}
 c^{k-1-j}A_X^j\varepsilon_X
\tag{16}
\]

and `\|A_X\|\le1`, `0<c<1` imply

\[
\boxed{
A_X^k\delta_1\longrightarrow c^k\delta_1
\quad\text{strongly}.
}
\tag{17}
\]

Consequently the even moments satisfy

\[
\boxed{
\langle\delta_1,N_X^{2k}\delta_1\rangle
\longrightarrow c^k.
}
\tag{18}
\]

For the odd moments, use self-adjointness and (17):

\[
\langle\delta_1,N_X^{2k+1}\delta_1\rangle
=
\langle N_X\delta_1,A_X^k\delta_1\rangle.
\tag{19}
\]

Since `\langle N_X\delta_1,\delta_1\rangle=0` exactly and `\|N_X\delta_1\|\le1`,

\[
\left|
\langle N_X\delta_1,A_X^k\delta_1\rangle
-c^k\langle N_X\delta_1,\delta_1\rangle
\right|
\le
\|A_X^k\delta_1-c^k\delta_1\|
\to0.
\]

Thus

\[
\boxed{
\langle\delta_1,N_X^{2k+1}\delta_1\rangle
\longrightarrow0.
}
\tag{20}
\]

The probability measure

\[
\mu_*
:=
\frac12\delta_{-\sqrt c}
+
\frac12\delta_{\sqrt c}
\tag{21}
\]

has moments

\[
\int\lambda^{2k}\,d\mu_*=c^k,
\qquad
\int\lambda^{2k+1}\,d\mu_*=0.
\tag{22}
\]

All `\mu_{X,1}` are supported on the common compact interval `[-1,1]`. Polynomial approximation on that interval therefore upgrades (18)--(20) from moment convergence to weak convergence, proving (4) and (5).

## 3. Every fixed non-root local spectral measure collapses to `delta_0`

For a fixed shell `m\ge2`, `WP-152` gives

\[
\|N_X\delta_m\|\longrightarrow0.
\tag{23}
\]

But the second moment of the local spectral measure is exactly

\[
\int\lambda^2\,d\mu_{X,m}(\lambda)
=
\langle\delta_m,N_X^2\delta_m\rangle
=
\|N_X\delta_m\|^2.
\tag{24}
\]

Hence for every `\eta>0`,

\[
\mu_{X,m}(|\lambda|\ge\eta)
\le
\frac1{\eta^2}
\int\lambda^2\,d\mu_{X,m}(\lambda)
\longrightarrow0.
\tag{25}
\]

This proves (3) directly. In particular, there is no hidden higher-moment obstruction at a fixed non-root arithmetic shell: once the normalized first-step norm vanishes, the entire local spectral probability measure concentrates at zero.

## 4. Resolvents, heat responses, and the normalized Laplacian are universal

The fixed continuous functional-calculus statement makes several natural attempted readouts explicit.

For `z\notin[-1,1]`, the local resolvent of the normalized adjacency satisfies

\[
\boxed{
\langle\delta_1,(z-N_X)^{-1}\delta_1\rangle
\longrightarrow
\frac{z}{z^2-c},
}
\tag{26}
\]

whereas for fixed `m\ge2`,

\[
\boxed{
\langle\delta_m,(z-N_X)^{-1}\delta_m\rangle
\longrightarrow\frac1z.
}
\tag{27}
\]

Similarly, for fixed real `t`,

\[
\langle\delta_1,e^{tN_X}\delta_1\rangle
\longrightarrow
\cosh(t\sqrt c),
\qquad
\langle\delta_m,e^{tN_X}\delta_m\rangle
\longrightarrow1.
\tag{28}
\]

For the symmetric normalized Laplacian

\[
\mathcal L_X=I-N_X,
\tag{29}
\]

the fixed non-root spectral measures converge to `\delta_1`, while the root measure converges to

\[
\boxed{
\frac12\delta_{1-\sqrt c}
+
\frac12\delta_{1+\sqrt c}.
}
\tag{30}
\]

So changing from normalized adjacency to the standard positive normalized Laplacian does not recover any finite-prime detail. It merely translates the same universal two-point boundary law.

## 5. Why lower-shell cycles and prime powers cannot re-enter through long walks

The resultant graph is not a star. It contains many prime-power triangles, spectator squares, and larger multiplicative subgraphs. A priori, higher powers of `N_X` could wander from the root into that interior and return with arithmetic-dependent weights.

Equation (13) shows why this does not happen at fixed spectral order. Every first step from the root outside the top-half leaf layer is contained in `w_X`, whose norm tends to zero. Since each subsequent normalized adjacency is a contraction, no fixed number of additional steps can amplify that vanishing component. All surviving first-step norm enters exact leaves, and every such leaf is forced to return immediately to the root. Iterating produces the scalar recurrence `N_X^2\delta_1\sim c\delta_1`, which controls every fixed moment.

This is stronger than arguing term-by-term that particular families of closed walks are small. The contraction estimate closes **all** lower-shell excursions at once for every fixed walk length.

## 6. Matched control: the mechanism is classical star spectral geometry

The two-point limit is not special to cyclotomic arithmetic. Suppose a sequence of self-adjoint contractions `T_i` on rooted spaces satisfies

\[
T_i e=v_i+w_i,
\qquad
\|w_i\|\to0,
\qquad
\|v_i\|^2\to c,
\qquad
T_iv_i=\|v_i\|^2e.
\tag{31}
\]

The proof of Sections 1--2 applies verbatim and gives the root local spectral limit

\[
\frac12\delta_{-\sqrt c}+\frac12\delta_{\sqrt c}.
\tag{32}
\]

A weighted rooted graph in which asymptotically all root one-step norm sits on leaves has exactly this structure. `WP-152` already gave a matched regular-variation graph reproducing the moving boundary mass; the present result shows that its **entire fixed local spectral law** is reproduced as well.

This is also close to classical star-graph spectral limit theory. Nobuaki Obata, *Quantum Probabilistic Approach to Spectral Analysis of Star Graphs*, Interdisciplinary Information Sciences **10** (2004), 41--52, DOI `10.4036/iis.2004.41`, proves asymptotic Bernoulli spectral behavior for growing star graphs. Thibault Espinasse and Paul Rochet, *A Coupling of the Spectral Measures at a Vertex*, Electronic Journal of Combinatorics **26** (2019), #P3.23, DOI `10.37236/8674`, formulate local spectral measures through rooted closed-walk moments and extend Obata-type star limits.

Those results classicalize the generic spectral mechanism. What is Mathia-specific here is only the exact specialization that `WP-152` supplies:

\[
\text{natural cyclotomic shell cutoff}
\Longrightarrow
\text{asymptotically dominant top-half prime leaves}
\Longrightarrow
c=1-2^{-1/2}
\Longrightarrow
\text{scaled Bernoulli local spectral law}.
\tag{33}
\]

Targeted searches for cyclotomic resultants together with normalized adjacency/Laplacian spectral measures did not locate this exact specialization. No novelty is claimed for star-graph Bernoulli limits, local spectral measures, the spectral theorem, or normalized graph operators.

## 7. Relation to the Weil-positivity obstruction chain

`PC-004` gives the unexpectedly exact finite-place datum: square-root-normalized primitive-shell resultants reproduce `(\log p)p^{-k/2}` on every prime-power ray. `WP-145`--`WP-147` show that the raw global resultant kernel is not a positive Weil form. `WP-148` repairs every finite cutoff by the canonical graph Dirichlet completion, but `WP-149` shows the unchanged all-prime energy space short-circuits completely. `WP-150` proves that local positive renormalization restores finite fixed-shell energy only by erasing every fixed arithmetic edge. `WP-151` then shows that the remaining normalized mass escape depends on exhaustion, and `WP-152` evaluates the distinguished arithmetic-size exhaustion as a universal top-half prime boundary layer.

`WP-153` closes the natural spectral follow-up to that last result. The surviving root norm cannot be mined by taking fixed powers, a fixed heat kernel, a fixed resolvent, or any other bounded continuous local spectral function: all such readouts are determined by the single universal constant `c`. At every fixed non-root shell the whole local spectral measure collapses to a point mass.

Thus the resultant route has reached a sharper boundary than “normalized adjacency loses fixed coefficients.” Even the full fixed-shell local spectral calculus of the natural normalized operator is universal.

## 8. Falsification boundary and surviving escapes

The claim is exact under its stated hypotheses, but its scope matters.

It does **not** assert convergence of `N_X` in operator norm or strong convergence on the root; indeed `WP-152` proves that `N_X\delta_1` has no strong limit. Local spectral measures can converge even when the corresponding one-step vectors escape spatially.

It also does not cover:

- an `X`-dependent or unbounded spectral filter that deliberately magnifies the vanishing interior component `w_X`;
- moving shell states `m=m(X)` or test vectors that retain the rescaled boundary coordinate `n/X`;
- the global empirical spectral distribution of `N_X`;
- a nonlocal observable involving several moving shells before the limit;
- an interaction changed by source-forced mixed-prime terms;
- a finite--archimedean coupling formed before graph normalization.

The first two are precisely new regularization/test-space choices, not consequences of the fixed natural local spectral geometry. To qualify under the research mandate they would need an intrinsic Mathia derivation and must survive the same matched-control and prior-art audits rather than selecting a frequency/cutoff dependence merely to recover the desired arithmetic.

## 9. Consequence for the research mandate

The finite-cutoff normalized Laplacians remain honest positive geometries for an independent graph-theoretic reason. But under the most intrinsic shell-size cutoff currently available, their fixed-shell spectral content is exhausted by

\[
\boxed{
\delta_0\quad(m\ge2),
\qquad
\frac12\delta_{-\sqrt{1-1/\sqrt2}}
+
\frac12\delta_{\sqrt{1-1/\sqrt2}}
\quad(m=1)
}
\tag{34}
\]

for normalized adjacency, with the corresponding translation by `1` for the positive normalized Laplacian.

There is no finite-prime Mangoldt selector left in this local spectral law, no archimedean/Gamma term, and no global Weil counterterm. The only nontrivial fixed-root spectral datum is the universal star-boundary constant selected by the cutoff.

Therefore a viable Mathia-native Weil-positive mechanism cannot arise by simply applying a fixed local spectral function to the natural-cutoff normalized resultant operator. It must preserve arithmetic before this universalization occurs, most plausibly through a genuinely nonlocal/mixed object, a source-forced moving geometric state richer than shell size, or a nonseparable finite--archimedean construction whose positivity is established before taking the all-prime normalized limit.

## Internal dependencies

- `research/prime_circle/findings/PC-004-normalized-resultants-weil-local-kernels.md`
- `research/weil_positivity/findings/WP-145-resultant-hessian-positivity-loses-prime-power-support-and-splits-real-place-curvature.md`
- `research/weil_positivity/findings/WP-148-canonical-resultant-graph-laplacian-has-infinite-critical-degree-and-trivial-l2-domain.md`
- `research/weil_positivity/findings/WP-149-spectator-prime-parallel-paths-collapse-resultant-resistance-and-energy-space.md`
- `research/weil_positivity/findings/WP-150-local-finite-energy-renormalizations-erase-resultant-arithmetic-edges.md`
- `research/weil_positivity/findings/WP-151-normalized-resultant-mass-escape-is-exhaustion-dependent.md`
- `research/weil_positivity/findings/WP-152-natural-shell-size-cutoff-leaves-only-a-universal-root-boundary-layer.md`

## External references

- Nobuaki Obata, *Quantum Probabilistic Approach to Spectral Analysis of Star Graphs*, Interdisciplinary Information Sciences **10** (2004), 41--52. DOI: `10.4036/iis.2004.41`.
- Thibault Espinasse and Paul Rochet, *A Coupling of the Spectral Measures at a Vertex*, Electronic Journal of Combinatorics **26** (2019), #P3.23. DOI: `10.37236/8674`.
- Fan R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics 92, American Mathematical Society, 1997.
- T. M. Apostol, *Resultants of cyclotomic polynomials*, Proceedings of the American Mathematical Society **24** (1970), 457--462.