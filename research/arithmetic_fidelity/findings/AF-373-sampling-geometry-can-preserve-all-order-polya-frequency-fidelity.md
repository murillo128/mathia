# AF-373 — Sampling geometry can preserve all-order Pólya-frequency fidelity

**Status:** `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-FIDELITY`, `TOTAL-POSITIVITY`, `SAMPLING`, `PRIOR-ART-REDIRECT`, `NO-NOVELTY-CLAIM`

## Claim

AF-372 shows that no fixed determinant order can certify Pólya-frequency total positivity on the unrestricted translation-kernel class. Classical work of Ganzburg shows that the other natural complexity axis — **where** the determinants are sampled — behaves very differently.

Let `L` be the class of bounded measurable functions `f : R -> R` with exponential decay

\[
|f(x)|=O(e^{-c|x|})
\qquad (|x|\to\infty)
\tag{1}
\]

for some `c>0`. For an infinite set `E\subset R`, call `f` `E`-Pólya-frequency (`E`-PF) when `f\ge 0`, `0<\int_R f<\infty`, and

\[
\det\big(f(u_i-x_j)\big)_{i,j=1}^m\ge 0
\tag{2}
\]

for every `m`, every increasing `u_1<\cdots<u_m` chosen from `E`, and every increasing `x_1<\cdots<x_m` in `R`.

Ganzburg proved two exact sufficient sampling theorems:

1. if `E` has an accumulation point and `f\in L` is `E`-PF, then `f` is a full Pólya-frequency function;
2. the same conclusion holds if `E` contains a symmetric sequence `u_{-s}=-u_s`, `u_s\to\infty`, with

\[
u_s=o(\sqrt{s}).
\tag{3}
\]

Thus full translation total positivity can, on this source class, be certified by a **strictly structured infinite subfamily** of the determinant tests: one coordinate of every minor may be restricted to a predeclared sampling skeleton `E`. In particular, `E` can be countable; for example any infinite sequence with a finite accumulation point satisfies the first theorem.

This does not contradict AF-372. The retained family still contains determinants of arbitrarily large order. What has been compressed is the **location geometry**, not the relational arity.

The geometry of the retained skeleton is itself essential. Ganzburg gives an explicit counterexample for `E=Z`: if `psi:(0,1]\to[0,\infty)` is bounded, measurable, and has positive integral, then

\[
f_\psi(y)=
\begin{cases}
\psi(y),&y\in(0,1],\\
0,&\text{otherwise}
\end{cases}
\tag{4}
\]

belongs to `L` and is `Z`-PF, but is not a Pólya-frequency function. Hence a single fixed lattice can leave false-positive fibers even though every determinant order is retained.

The durable conclusion is therefore sharper than "all-order total positivity is necessary": **all-order arity and sampling geometry are independent fidelity resources.** Unbounded arity can survive while an overly sparse or poorly placed sampling skeleton still destroys the target discriminator.

## Classical derivation

Ganzburg's 2008 definition of `E`-PF is exactly `(2)`. His Theorem 2.1 states that, for `f\in L`, any sampling set `E` with an accumulation point is determining: `E`-PF implies full PF. The proof uses the variation-diminishing consequences of the restricted kernel together with polynomial approximation at points of `E`, and then closes the argument through Schoenberg's real-zero/Laplace-transform characterization.

Theorem 2.2 removes the need for a finite accumulation point. It is enough that `E` contain a symmetric unbounded sequence satisfying `(3)`. The condition is a sufficient sampling-density hypothesis; no claim is made here that the exponent `1/2` is a sharp boundary for every possible `E`.

The integer lattice gives the complementary exact obstruction. For `(4)`, an integer-row determinant is zero except for the compatible staircase placement, where it reduces to a product of nonnegative values of `psi`. Hence every restricted determinant has the required sign. Nevertheless the Laplace transform of `f_psi` does not have the Schoenberg form required of a PF function, so `f_psi` is not PF.

Ganzburg's 2010 shift-generating formulation exposes the same distinction from another direction. For a fixed `a>0`, an `a`-shift-generating function requires every sequence

\[
\{f(an-x)\}_{n\in\mathbb Z}
\tag{5}
\]

to be a totally positive sequence as `x` varies. A continuous nonexponential `f` is totally positive if and only if it has this property for **every** `a>0`. A single fixed mesh is not enough in general: the paper exhibits functions supported on one interval of length `a` that are `a`-shift-generating but not totally positive.

Together these results give a clean separation:

\[
\text{bounded arity}\quad\text{vs.}\quad
\text{restricted locations}\quad\text{vs.}\quad
\text{source regularity}.
\tag{6}
\]

AF-372 rules out the first compression on the unrestricted class. Ganzburg shows that the second compression can be exact once its geometry and the exponentially decaying source class are specified, while a fixed lattice can still fail.

## Fidelity interpretation

Let

\[
D(f)=\mathbf 1_{\{f\text{ is PF}\}}
\tag{7}
\]

and let `C_E(f)` retain the all-order determinant verdicts `(2)` with the first coordinate restricted to `E`.

On `L`, Ganzburg's determining-set theorems give

\[
D\factor C_E
\tag{8}
\]

whenever `E` has an accumulation point, and also for the symmetric sub-square-root-growth sets in `(3)`. The restricted observation is therefore target-faithful despite omitting almost all row locations.

For `E=Z`, `(4)` gives the opposite conclusion:

\[
D\not\!\factor C_{\mathbb Z}.
\tag{9}
\]

This is a concrete answer to the structured-infinite-family question left after AF-372. The full family of arbitrary translation minors is not minimal in its **location** degrees of freedom. Some one-sided sampling skeletons already force the full target, but not all skeletons do.

The distinction is useful beyond total positivity. A compressed certificate should not be priced by the number of retained inequalities alone. Two infinite test families with the same unbounded determinant order can have different target fidelity because the retained sampling set has different uniqueness geometry. In this example, an accumulation set supplies enough analytic/variation-diminishing rigidity to recover omitted locations, whereas the integer lattice admits compactly supported aliases.

## Riemann specialization

AF-371 records the Schoenberg/Gröchenig equivalence between the Riemann hypothesis and Pólya-frequency total positivity of the appropriate reciprocal-transform kernel. AF-372 then shows that a fixed minor-order cutoff cannot be promoted to a general exact criterion.

AF-373 narrows the remaining search differently: **a smaller exact certificate may come from structured sampling rather than smaller determinant order.** If the relevant Riemann reciprocal-transform kernel is independently placed in a source class to which a determining-set theorem applies, it would be enough to establish all-order determinant positivity on a suitable sampling skeleton `E` rather than at every pair of real location sets.

This is not RH progress by itself. It does not establish those restricted determinants, does not show that the most convenient arithmetic sampling set is determining, and does not remove the need for unbounded order. In particular, a fixed integer lattice cannot be assumed faithful merely because it is arithmetically natural: Ganzburg's `Z`-PF counterexample proves that such a step requires extra source-specific rigidity.

## Prior-art and novelty audit

- Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1–8, DOI `10.1016/j.jmaa.2008.04.070`. Role: defines `E`-PF functions; Theorem 2.1 proves that an accumulation set is determining on the exponentially decaying class `L`; Theorem 2.2 gives the symmetric `u_s=o(sqrt(s))` determining condition; Example 2.1 gives the explicit `E=Z` false positives used above.
- Michael I. Ganzburg, **“On Totally Positive Sequences and Functions,”** *Journal of Mathematical Analysis and Applications* **361**(2) (2010), 466–471, DOI `10.1016/j.jmaa.2009.07.036`. Role: introduces `a`-shift-generating functions and proves that a continuous nonexponential function is totally positive exactly when it is `a`-shift-generating for every mesh `a>0`; fixed-mesh examples show why one sampling scale alone is insufficient.
- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* **1** (1951), 331–374, DOI `10.1007/BF02790092`. Role: classical transform characterization underlying the full PF target and the non-PF conclusion for the compactly supported lattice controls.

No novelty is claimed for the `E`-PF or shift-generating theorems, their proofs, or their counterexamples. The Arithmetic Fidelity contribution is the **resource separation** they enforce after AF-371/AF-372: relational arity and sampling geometry are distinct compression coordinates, and a structured infinite family can be target-faithful only relative to a declared source class and determining-set theorem.

## Decisive audit rule

After a total-positivity route has accepted that unbounded determinant order is unavoidable, do not infer that every location must still be tested. Ask instead whether the source class admits a determining sampling skeleton.

Conversely, do not treat a convenient discrete grid as automatically faithful. For exponentially decaying translation kernels, accumulation sets and certain sufficiently dense unbounded symmetric sets are classically determining, while the integer lattice has exact false positives. Any arithmetic reduction to sampled total positivity must therefore justify **both** unbounded relational order and the uniqueness geometry of its retained sampling set.