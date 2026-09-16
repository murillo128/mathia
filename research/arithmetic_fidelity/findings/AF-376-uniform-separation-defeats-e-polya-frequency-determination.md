# AF-376 — Uniform separation defeats E-Pólya-frequency determination

## Status

`EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `SAMPLING` · `CLASSICAL-ADJACENT` · `NO-NOVELTY-CLAIM`

## Claim

Let `E\subset\mathbb R` be uniformly discrete, with separation

\[
\Delta_E:=\inf\{|u-v|:u,v\in E,\ u\ne v\}>0.
\]

Let `I\subset\mathbb R` be an interval of length `\ell<\Delta_E`, and let

\[
f:\mathbb R\to[0,\infty)
\]

be any bounded measurable nonzero function supported in `I`. Then `f` is an `E`-Pólya-frequency function in Ganzburg's sense: for every `n`, every increasing `u_1<\cdots<u_n` in `E`, and every increasing `x_1<\cdots<x_n` in `\mathbb R`,

\[
\det\bigl(f(u_i-x_j)\bigr)_{i,j=1}^n\ge0.
\tag{1}
\]

At the same time, no such nonzero compactly supported integrable function can be a full Pólya-frequency function. Hence **no uniformly discrete sampling set `E` is determining for the exponentially decaying source class `L` used in AF-373**. In fact, every interval shorter than the separation supports an infinite-dimensional cone of exact false positives.

Applied to the frontier left by AF-375, take

\[
E=a\mathbb Z\cup(\tau+a\mathbb Z),
\qquad \tau/a\notin\mathbb Q.
\tag{2}
\]

Although the generated difference subgroup `H_E=a\mathbb Z+\tau\mathbb Z` is dense and therefore removes every nonconstant continuous separable periodic gauge classified in AF-375, the set `E` itself is periodic and uniformly discrete. Writing `\theta\in(0,a)` for the residue of `\tau` modulo `a`,

\[
\Delta_E=\min\{\theta,a-\theta\}>0.
\tag{3}
\]

Therefore `(2)` is **not** determining on `L`: compact-support false positives survive every sampled determinant order and every mixed-row minor. Dense generated difference geometry eliminates the AF-374 multiplicative gauge, but it does not eliminate non-separable target-changing fibres.

## Exact determinant argument

Write the support interval as `I\subset[\alpha,\beta]` with

\[
\beta-\alpha=\ell<\Delta_E.
\]

Fix increasing sampled rows `u_1<\cdots<u_n` and increasing columns `x_1<\cdots<x_n`. A matrix entry can be nonzero only if

\[
u_i-x_j\in I,
\]

which implies

\[
x_j\in J_i:=[u_i-\beta,\,u_i-\alpha].
\tag{4}
\]

For consecutive sampled rows,

\[
(u_{i+1}-\beta)-(u_i-\alpha)
=(u_{i+1}-u_i)-\ell
>0.
\tag{5}
\]

Thus the intervals `J_i` are pairwise disjoint and occur in the same strict order as the rows.

Consequently each column of the matrix `A=(f(u_i-x_j))` has at most one potentially nonzero entry. If some row receives no such column, or two columns are assigned to the same row, then `\det A=0`. Otherwise the column-to-row assignment is a bijection. Because both the `x_j` and the disjoint intervals `J_i` are ordered, that bijection must be the identity permutation. Hence the only possible nonzero Leibniz term is

\[
\det A=\prod_{i=1}^n f(u_i-x_i)\ge0.
\tag{6}
\]

This proves `(1)` simultaneously for every determinant order. The mechanism uses only uniform row separation and support width; it is not a periodic-gauge argument.

## Why the controls are not full Pólya-frequency functions

Every such `f` belongs to Ganzburg's exponentially decaying class `L` because it is bounded and compactly supported. Its bilateral Laplace transform

\[
F(z)=\int_{\mathbb R} f(y)e^{-zy}\,dy
\tag{7}
\]

is entire of exponential type.

Suppose, for contradiction, that `f` were a full Pólya-frequency function. Schoenberg's characterization, in the equivalent form quoted as Theorem 1.1 in Ganzburg's 2008 paper, says that on the Laplace strip

\[
F(z)=\frac{1}{\Phi(z)},
\tag{8}
\]

where `\Phi` extends to an entire Laguerre--Pólya function of the canonical Schoenberg form. Since compact support already makes `F` entire, the identity `F\Phi=1` on the nonempty Laplace strip extends by the identity theorem to all of `\mathbb C`. Thus `F` is a zero-free entire function.

A zero-free entire function of exponential type has Hadamard factorization

\[
F(z)=e^{az+b}
\tag{9}
\]

for constants `a,b`. Because `f\ge0` is nonzero, `F(t)>0` for every real `t`; hence `a` and `b` may be taken real, up to the irrelevant `2\pi i` ambiguity in `b`. Therefore

\[
|F(i\xi)|=e^b
\]

for every real `\xi`. But `f\in L^1(\mathbb R)`, so the Riemann--Lebesgue lemma gives `F(i\xi)\to0` as `|\xi|\to\infty`, a contradiction.

Thus every nonzero control covered by the determinant argument is genuinely outside the full PF class.

## Relation to AF-373 through AF-375

AF-373 separated two fidelity resources: determinant arity and sampling geometry. Ganzburg's determining theorems show that some thin sampling sets are sufficient on `L`, while his `E=\mathbb Z` example gives a compact-support false positive for one lattice.

AF-374 then identified a stronger fixed-lattice obstruction: multiplication by a positive periodic gauge preserves every sampled minor, even inside entire Gaussian-decay source classes. AF-375 classified exactly when that **separable multiplicative** mechanism survives; an incommensurate second lattice phase makes the generated difference subgroup dense and kills every nonconstant periodic separable gauge modulo the universal exponential tilt.

The present result shows that this repair is still insufficient on `L`. The crucial distinction is

\[
\text{generated difference subgroup }\langle E-E\rangle
\quad\text{versus}\quad
\text{geometric separation of the actual row set }E.
\tag{10}
\]

For the two-phase set `(2)`, the first object is dense while the second retains a positive minimum gap. The dense subgroup controls one exact gauge family, but the determinant observation never acquires rows at the new subgroup combinations. A compact-support kernel narrower than the actual row spacing therefore remains invisible to the missing locations.

This closes the specific two-phase question left open in AF-375 for the broad source class `L`: **one incommensurate phase removes the known periodic gauge but does not make the sampled all-order total-positivity certificate target-faithful.**

## Fidelity interpretation

A compression can eliminate a known symmetry of its fibres without becoming determining. Here `H_E` is an exact invariant for separable multiplicative aliases, but it is not a complete invariant for the full observation fibre.

The counterexample is particularly sharp because it retains all determinant orders and all mixed minors allowed by `E`; the failure is not caused by bounded relational arity or by checking the two lattice phases independently. Uniform separation itself permits a local-support regime in which the sampled kernel matrix becomes order-preserving and essentially diagonal, so total positivity is automatic regardless of the internal shape of `f`.

This produces an infinite-dimensional false-positive family, not a residual one-parameter gauge. Any positive bounded measurable profile inside an interval shorter than `\Delta_E` gives the same qualitative sampled certificate while failing the global PF target.

## Riemann specialization

For an RH-facing Pólya-frequency criterion, adding finitely many lattice phases cannot by itself justify replacing full translation total positivity by sampled-row total positivity on the broad exponentially decaying class `L`. This remains true even when the phases are incommensurate and therefore destroy every nonconstant periodic separable gauge from AF-374/AF-375.

A successful discrete sampling reduction must instead use **source-specific structure that excludes the local-support alias**, or use a sampling geometry with no positive minimum separation and enough determining power for that source class. The relevant zeta reciprocal-transform kernel may have much stronger analytic/global constraints than `L`; AF-376 does not rule out a determining theorem on such a narrower class. It does rule out treating dense generated differences, analyticity of a separate gauge family, or all-order mixed minors alone as sufficient.

No zero-location statement follows from this obstruction.

## Prior-art and novelty audit

Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1–8, DOI `10.1016/j.jmaa.2008.04.070`, is the direct classical source. It defines `E`-PF functions, proves that sampling sets with an accumulation point are determining on `L`, gives additional determining geometries, and in Example 2.1 constructs arbitrary compact-support false positives for `E=\mathbb Z`. The determinant proof above is an elementary extension of the same sparse-support mechanism from a lattice to an arbitrary uniformly discrete row set.

I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* **1** (1951), 331–374, DOI `10.1007/BF02790092`, supplies the classical reciprocal Laplace-transform characterization used to exclude nonzero compactly supported integrable PF functions.

A focused search did not identify a standard result stated exactly as the uniformly-discrete extension above. No novelty is claimed: the proof is elementary and the lattice case is already explicit in Ganzburg. The durable Arithmetic Fidelity contribution is the **closure of AF-375's live two-phase question** and the separation of two different geometric resources: dense algebraic generation of differences does not compensate for positive geometric separation of the actually observed row set.

## Boundaries and failure modes

Uniform discreteness is a sufficient obstruction, not a characterization of non-determining sets. The proof says nothing about discrete sets whose gaps tend to zero, and it does not compete with Ganzburg's theorem that an accumulation point makes `E` determining on `L`.

The support-width argument also depends on the broad source class admitting compactly supported nonnegative functions. A narrower quasianalytic, transform-constrained, or otherwise globally rigid source class can exclude these controls. Such a restriction must be justified by the arithmetic kernel itself; it cannot be imposed merely to rescue the sampling proposal.

Finally, `H_E` remains the correct classifier for the separable multiplicative gauges studied in AF-375. AF-376 does not weaken that theorem; it shows why eliminating one classified gauge family is only a necessary intermediate audit and not a full recovery theorem.

## Decisive audit rule

Before trying to prove that an all-order row-sampled Pólya-frequency certificate is determining, compute both the actual separation geometry of `E` and any algebraic group generated by its differences.

If `\Delta_E>0` and the admitted source class contains nonzero bounded nonnegative functions supported in intervals shorter than `\Delta_E`, determination fails immediately, regardless of whether `\langle E-E\rangle` is dense. Only after this local-support obstruction is excluded does the difference-group gauge audit become potentially close to a recovery theorem.

## Consequences

The incommensurate two-phase repair proposed after AF-374 and sharpened in AF-375 is decisively closed on Ganzburg's broad exponentially decaying class `L`.

The next productive question is no longer whether more finite lattice phases remove the periodic gauge. Any finite union of lattice phases with a positive minimum gap remains uniformly discrete and therefore admits the same compact-support false-positive mechanism. Progress requires either a sampling set with genuinely vanishing local spacing, or a mathematically forced source class whose global rigidity forbids compact/local aliases and for which a determining theorem can be proved.