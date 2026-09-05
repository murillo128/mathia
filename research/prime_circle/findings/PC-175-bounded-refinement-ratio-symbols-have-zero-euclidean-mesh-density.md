# PC-175 — bounded weak-refinement ratio symbols have zero Euclidean mesh density

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the ordinary-geometric-symbol escape left open by PC-174. After the canonical `|D|^{1/2}` normalization, exact weak Prime-Circle refinement makes every continuous first-order boundary form a matrix-valued multiplicative Toeplitz operator with entries `Phi(m/l)`. Boundedness then imposes a sharp sampling obstruction that is independent of compactness: every column has uniformly bounded `ell^2` mass, so the symbol has zero mean-square density on every ordinary real ratio interval. Consequently no nonzero continuous, smooth, analytic, or otherwise locally Riemann-regular function of the Euclidean ratio `m/l` can supply the missing noncompact symbol. Any surviving exact-covariant symbol must instead be arithmetically sparse or conductor-decaying in the ordinary ratio topology, or leave the fixed weak-form class altogether.

PC-174 classified the normalized weak-covariant class but deliberately left a large noncompact symbol freedom. Its open geometric question was whether embedded primitive-shell/chord/old-new data can canonically choose a specific noncompact multiplicative-Toeplitz symbol rather than inserting a zeta-bearing symbol by hand. The first natural repair is to let the coefficient depend regularly on the real ratio of the two Fourier scales, as one does for chord, angle, logarithmic-potential, or smooth pseudodifferential profiles. This finding shows that such ordinary ratio geometry is incompatible with boundedness before any spectral or RH interpretation begins.

## 1. Exact weak refinement reduces the question to one ratio column

Use the normalized setting of PC-174. On one orientation block of `L^2_0(S^1)`, write

\[
B=(b_{ml})_{m,l\ge 1},
\qquad
b_{ml}=\Phi(m/l),
\tag{1}
\]

where `B` is bounded on `ell^2(N)` and `Phi:Q_{>0}->C`. The other three orientation blocks have the same form with their own symbols; treating one block is therefore sufficient.

For the standard basis vector `e_l`, the `m`th coordinate of `Be_l` is exactly `Phi(m/l)`. Hence boundedness gives the elementary but load-bearing estimate

\[
\boxed{
\sum_{m\ge1}|\Phi(m/l)|^2
=\|Be_l\|_2^2
\le \|B\|^2
\qquad(l\ge1).
}
\tag{2}
\]

This is stronger than the compactness obstruction of PC-174 in a different direction. PC-174 showed that an exactly covariant compact normalized operator must vanish. Equation (2) applies to every bounded fixed point, including genuinely noncompact multiplicative Toeplitz operators.

For any compact ordinary ratio interval `I=[a,b]` with `0<a<b<infinity`, define the mesh energy

\[
E_l(I)
=\frac1l
\sum_{\substack{m\ge1\\m/l\in I}}
|\Phi(m/l)|^2.
\tag{3}
\]

Equation (2) immediately yields

\[
\boxed{
0\le E_l(I)\le \frac{\|B\|^2}{l}
\longrightarrow0.
}
\tag{4}
\]

Thus every bounded weak-refinement symbol has **zero Euclidean mean-square mesh density** on every fixed positive interval.

There is also a pointwise-density form. For any `delta>0`,

\[
N_l(I,\delta)
=\#\{m:m/l\in I,\ |\Phi(m/l)|\ge\delta\}
\]

satisfies

\[
\boxed{
N_l(I,\delta)\le \frac{\|B\|^2}{\delta^2}
}
\tag{5}
\]

uniformly in `l`. A bounded symbol therefore cannot remain of order one on a positive proportion of the `O(l)` rational samples in any ordinary interval. The number of samples above any fixed amplitude is uniformly `O(1)`, not `O(l)`.

## 2. Every regular real-ratio profile is forced to vanish

Suppose on some compact interval `I=[a,b]` the rational symbol is the restriction of a locally Riemann-integrable function

\[
\phi:I\to\mathbb C,
\qquad
\Phi(q)=\phi(q)
\quad(q\in I\cap\mathbb Q_{>0}).
\tag{6}
\]

Because `|phi|^2` is Riemann integrable, the uniform rational mesh gives

\[
\frac1l
\sum_{\substack{m\ge1\\m/l\in I}}
|\phi(m/l)|^2
\longrightarrow
\int_a^b |\phi(x)|^2\,dx.
\tag{7}
\]

Combining (4) and (7) gives

\[
\boxed{
\int_a^b|\phi(x)|^2\,dx=0.
}
\tag{8}
\]

Therefore `phi=0` almost everywhere on `I`. In particular, if `phi` is continuous on `I`, then

\[
\boxed{\phi\equiv0.}
\tag{9}
\]

The argument is local. A profile may have singularities at isolated ratios; if it is continuous and nonzero on even one compact subinterval avoiding those singularities, its multiplicative-Toeplitz matrix is unbounded. The same proof applies entrywise to the `2 x 2` orientation symbol of PC-174, because every orientation compression of a bounded `B` is bounded.

This rules out, as normalized fixed symbols, the direct use of any nonzero smooth ordinary-ratio expression such as a function of `exp(2 pi i q)`, chord length `|1-exp(2 pi i q)|`, a fixed power of a nonsingular chord profile, `cot(pi q)` on an interval avoiding its poles, or `log|1-exp(2 pi i q)|` on an interval avoiding the integers. The issue is not their detailed formula. Any such expression has nonzero mean-square mass on some ordinary interval and therefore violates (4).

## 3. The obstruction is sharp: arithmetic dust survives

Equation (4) does **not** say that every bounded multiplicative-Toeplitz symbol vanishes. The topology is the point. For example,

\[
\Phi(q)=\mathbf 1_{\{q=1\}}
\tag{10}
\]

produces the identity operator. More generally a delta supported at one reduced rational ratio gives a bounded partial shift between the corresponding divisibility sublattices. Such symbols are maximally discontinuous in the ordinary real topology and have zero mesh density in the sense of (4).

Denominator-sensitive symbols can also evade the regular-profile corollary when their amplitudes decay sufficiently fast or their support is sufficiently thin. A Riemann-integrable extension may even vanish almost everywhere while retaining nonzero values on a dense rational set. Therefore the exact conclusion is not `B=0`; it is that **nonzero bounded exact-refinement symbols must live on arithmetic rather than Euclidean ratio structure**.

This sharply separates two notions of regularity that can otherwise be conflated. Under the Bohr lift used in PC-174, the multiplicative ratio group is organized by prime-valuation coordinates and the infinite polydisc. Ordinary continuity of `q=m/l` as a positive real number is a different topology, and boundedness forbids a nonzero symbol that is regular in that Euclidean topology while being sampled on every denominator lattice.

## 4. Consequence for intrinsic Prime-Circle geometry

The original root geometry certainly contains smooth Euclidean data: angles, chord lengths, harmonic kernels, logarithmic potentials away from their singularities, and local projective quantities. PC-174 left open the possibility that one of these could directly choose the missing noncompact ratio symbol after exact first-order normalization. Equations (4)--(9) close that direct route.

A geometry-derived symbol that remains inside the fixed weak-covariant class must now acquire an explicitly arithmetic thinning or normalization before it can even define a bounded operator. For example, it may depend discontinuously on the reduced denominator/order, exact shell incidence, valuations, or another conductor-sensitive label, with amplitudes decaying sufficiently to satisfy (2). But those are precisely the directions where the Prime-Circle audit must distinguish genuinely new embedded geometry from the already classical cyclotomic/Bost--Connes/Dirichlet-series organization of rational ratios.

The result also blocks a common workaround: starting with a smooth chord or potential profile `g(q)` and declaring its multiplicative Toeplitz matrix to be the canonical noncompact operator. Unless an additional arithmetic factor suppresses almost all denominator samples or drives their amplitudes to zero, the matrix does not define a bounded normalized weak form at all. Adding such a factor is new structure that must itself be forced by Prime-Circle geometry rather than chosen to repair boundedness.

## 5. Prior art and novelty audit

The ambient operator class is classical and was already anchored for PC-174. Hilberdink studies matrices whose entries are functions of the rational ratio `i/j`, including their determinants and zeta connections. Guo--Yan identify infinite multiplicative Toeplitz matrices with Toeplitz operators on `H^2(T^infinity)` and prove the appropriate Brown--Halmos framework. Nicola Thorn's 2018 work **Bounded multiplicative Toeplitz operators on sequence spaces** studies exactly the mapping

\[
(\mathscr M_f x)_n=\sum_{k\ge1}f(n/k)x_k
\]

and gives boundedness criteria in `ell^p` spaces, including sharp norm statements for positive symbols in the edge cases. This confirms that boundedness of the ratio matrix is an established operator-theoretic problem rather than a new Prime-Circle category.

No historical novelty is claimed for multiplicative Toeplitz operators, column-norm estimates, or Riemann-sum arguments. Targeted searches for continuity or ordinary-real-topology conditions on the rational ratio symbol did not locate this exact formulation, but absence of an exact wording match is not used as a novelty claim. The durable Prime-Circle contribution is the line-specific compression: once PC-174 has forced the weak-refinement loophole into multiplicative Toeplitz form, the one-column estimate (2) proves that the most geometrically immediate noncompact repair -- a regular function of the real Fourier-scale ratio -- cannot be bounded.

The closest literature remains the multiplicative-Toeplitz/Dirichlet-series operator theory already recorded in `research/prime_circle/SOURCES.md`; the theorem here is an elementary consequence specialized to the exact Prime-Circle refinement boundary rather than a claim of a new general operator theorem.

## 6. Stress tests and exact boundary

The conclusion requires the PC-174 hypotheses: one fixed continuous first-order form, exact refinement covariance, and the `|D|^{1/2}` normalization that turns the form into a bounded operator `B`. More singular forms whose normalized representative is unbounded are outside the theorem, as are level-dependent or shell-dependent families, cross-level relations, nonlinear constructions, and the zero Fourier mode treated separately in the preceding boundary findings.

Ordinary-ratio regularity is also load-bearing only for the corollary (8)--(9). The universal mesh estimate (4) does not assume continuity. Arithmetic symbols that are nowhere ordinary-continuous, supported on sparse rational subsets, or decay with reduced denominator remain possible. The identity example (10) proves that exact covariance plus boundedness does not itself force triviality.

The theorem is directly falsifiable. A counterexample to (4) would be a bounded ratio matrix with a sequence of denominator meshes carrying a positive lower mean-square density on one fixed interval; this contradicts the exact column norm bound (2). A counterexample to (9) would be a nonzero continuous real-ratio profile whose sampled matrix is bounded; its Riemann sums would have positive limiting `L^2` mass, contradicting (4).

## 7. Consequence for the Prime-Circle/RH search

The noncompact freedom left by PC-174 is now topologically narrower. Exact weak refinement does not permit a bounded operator whose symbol is simply a smooth geometric response to the ordinary scale ratio. A surviving fixed-form symbol must instead be an **arithmetically thin rational-ratio object** satisfying the uniform column constraint (2), or the construction must abandon at least one of the fixed-form, first-order, bounded-normalization, or exact-refinement hypotheses.

This is a decisive negative for the regular geometric-symbol branch, not for the whole weak-covariant boundary program. It produces no spectral parameter, gamma factor, functional equation, zeta-zero set, or critical-line selector. Its value is to prevent a false positive: a smooth chord/potential ratio kernel cannot be promoted to the PC-174 operator merely because it looks intrinsic. Before any RH claim can be considered, the symbol must first survive the exact zero-mesh-density constraint, and any arithmetic mechanism used to achieve that survival must itself pass the Prime-Circle novelty controls.