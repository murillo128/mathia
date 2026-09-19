# AF-426 — Exact-square amplitude has an irreducible integer-source packet gap

## Status

`EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `SQUARE-TRANSITION` · `SIGNED-RESUMMATION` · `INTEGER-SOURCE` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-425 on the exact square-amplitude fiber

\[
a=m^2,
\qquad m\ge 1.
\]

Let `d_n\in\mathbb Z`, put

\[
s_n=2n+d_n,
\qquad
\alpha_n=\frac{d_n}{n},
\qquad
b_n=m^2 n^{d_n/n},
\]

and assume the square-transition condition

\[
b_n\longrightarrow m^2.
\tag{1}
\]

Let `Q_{n,m}` be AF-425's ratio of the two complete adjacent square packets. Then **the integer source cannot tune those packets to cancellation**:

\[
\boxed{Q_{n,m}\not\longrightarrow 1.}
\tag{2}
\]

More precisely, if `\log Q_{n,m}` is bounded along any subsequence satisfying `(1)`, then necessarily

\[
\boxed{d_n=-1}
\tag{3}
\]

eventually on that subsequence, and there

\[
\boxed{
Q_{n,m}\longrightarrow mK_m
=
\frac{4m^2e^{2m}}{(2m-1)^2\zeta(2m)}
>1.
}
\tag{4}
\]

Thus the continuously balanced source depth tends to `-1`, but integrality leaves a fixed nonzero packet mismatch even at that unique nearest depth. In particular, AF-425's shrinking-target condition

\[
H_n(d_n)=o(n^{-2})
\]

has no solution on the entire amplitude fiber `a=m^2`, not merely on AF-422's canonical subpath `d_n=0`.

For `m\ge2`, AF-421's tied packet rate `\Lambda_m>1` therefore cannot be neutralized by odd-parity adjacent-packet cancellation anywhere on this exact-amplitude fiber. For `m=1`, `(2)--(4)` still close the packet-cancellation mechanism, but no exponential-divergence conclusion follows because `\Lambda_1=1`.

## 1. The square condition forces vanishing derivative ratio

With `a=m^2`, condition `(1)` is exactly

\[
n^{d_n/n}\longrightarrow1,
\]

hence

\[
\frac{d_n\log n}{n}\longrightarrow0.
\tag{5}
\]

In particular `\alpha_n=d_n/n\to0`. Therefore AF-425 applies, and its explicit coefficient functions `B_1(\alpha_n)` and `B_2(\alpha_n)` remain bounded.

AF-425 gives

\[
\log Q_{n,m}
=
\Omega_{n,m}(d_n)
+
\frac{B_1(\alpha_n)}{n}
+
\frac{B_2(\alpha_n)}{n^2}
+o(n^{-2}),
\tag{6}
\]

so

\[
\log Q_{n,m}-\Omega_{n,m}(d_n)\longrightarrow0.
\tag{7}
\]

## 2. Bounded packet balance has one possible integer depth

On `a=m^2`, AF-425's exact affine detuning becomes

\[
\Omega_{n,m}(d)
=
\log n+\log K_m
+d\left(\log\frac{n}{m}+\frac{m}{n}\right).
\tag{8}
\]

Write

\[
L_{n,m}=\log\frac{n}{m}+\frac{m}{n}\sim\log n.
\]

If `\log Q_{n,m}` is bounded along a subsequence, `(7)` makes `\Omega_{n,m}(d_n)` bounded there. Dividing `(8)` by `L_{n,m}` gives

\[
\frac{\Omega_{n,m}(d_n)}{L_{n,m}}
=
\frac{\log n+\log K_m}{L_{n,m}}+d_n.
\tag{9}
\]

The left side tends to zero, while the first term on the right tends to one. Hence

\[
d_n\longrightarrow-1.
\]

Because every `d_n` is an integer, `(3)` follows: `d_n=-1` eventually on every bounded-ratio subsequence.

This is stronger than saying that the source lattice has spacing `\sim\log n`. On this fiber the moving continuous balancing center itself converges to the integer `-1`, so there is exactly one asymptotically admissible depth to inspect.

## 3. The unique nearest depth misses by a fixed positive amount

Substitute `d=-1` into `(8)`:

\[
\Omega_{n,m}(-1)
=
\log(K_m m)-\frac{m}{n}.
\tag{10}
\]

Together with `(7)`, this yields

\[
\log Q_{n,m}\longrightarrow\log(K_m m),
\]

which is `(4)`.

The limiting factor cannot accidentally equal one. Indeed

\[
mK_m
=
\frac{4m^2}{(2m-1)^2}\,
\frac{e^{2m}}{\zeta(2m)}.
\]

For `m\ge1`,

\[
\frac{4m^2}{(2m-1)^2}>1,
\qquad
\zeta(2m)\le\zeta(2)<2,
\]

and therefore

\[
mK_m>\frac{e^{2m}}2>1.
\tag{11}
\]

Thus the best integer source depth leaves an order-one logarithmic detuning rather than an inverse-power residual. In particular `Q_{n,m}` cannot approach one and `H_n(d_n)=o(n^{-2})` is impossible.

## 4. Arithmetic-fidelity interpretation

AF-422 closed the most obvious exact-square path `a=m^2, d_n=0`, where the rectangle ratio grows like `K_m n`. AF-425 then showed that a varying integer depth might in principle retune a square transition and reduced the surviving problem to an inhomogeneous source-lattice target.

The present result shows that **the whole exact-amplitude fiber is already rigid**. Retaining the source coordinate does not merely reveal a finer correction: it exposes a discrete obstruction that the continuous saddle hierarchy hides. The coarse square statistic `b_n\to m^2` permits a formal balancing center, but the original integer source has only the depth `d=-1` near that center, and the retained prefactor `K_m m` prevents cancellation there.

This is a concrete fidelity example in which a continuous asymptotic compression creates an apparent tunable degree of freedom that does not exist in the source category. Restoring source provenance changes the admissible parameter space from a continuum to an integer lattice and kills the natural exact-amplitude escape route.

## Prior-art and novelty audit

No new external theorem is needed. The argument is an exact corollary of AF-425's source-lattice formula and complete-packet expansion, plus the elementary monotonicity bound `\zeta(2m)\le\zeta(2)<2`. AF-422 already audits the surrounding coalescing-saddle and Schur/partition literature; AF-424--AF-425 audit the complete-packet and shrinking-target refinements.

A targeted search for discrete/integer-parameter coalescing-saddle detuning did not identify a standard result that supplies `(2)--(4)` independently of the Mathia formulas. **No novelty claim is made.** The durable mathematical delta is narrower: AF-425's unresolved integer-source gate is solved completely on `a=m^2`, including all source-compatible varying integer depths rather than only `d_n=0`.

## Boundaries and falsification checks

- The result fixes `m` and the exact amplitude `a=m^2`. It does not settle AF-425's moving shrinking target for `a\ne m^2`.
- The assumption `b_n\to m^2` is essential. Without it, `\alpha_n\to0` and the AF-425 square-packet expansion need not hold in the required form.
- Equation `(3)` is conditional on a bounded complete-packet log ratio. It is not a claim that every square-compatible integer sequence has `d_n=-1`; sequences with other depths simply fail balance more strongly.
- For `m\ge2`, the no-cancellation conclusion combines with AF-421's already established tied exponential rate. For `m=1`, only the packet-cancellation obstruction is asserted here.
- Nothing here resolves the genuinely supercritical regime `s_n/n\to\sigma>2`, the `a\ne m^2` Diophantine target, omitted-`1` sectors, rational-prime discrimination, zeta-zero recovery, or RH.

## Consequence for the research line

The exact-square amplitude is no longer part of the live shrinking-target frontier. The finite-window source-realizability question can be narrowed to `a\ne m^2`, where the continuous balancing depth grows on the `n/\log n` scale and genuine inhomogeneous Diophantine behavior remains possible.

This also sharpens the compression lesson: restoring a discarded source coordinate can turn an apparently delicate all-orders tuning problem into a zeroth-order discrete obstruction. The next finite-window work should therefore analyze the nonzero displacement

\[
\log\!\left(\frac{m^2}{a}\right)\ne0,
\]

rather than spend further effort on beyond-all-orders cancellation at `a=m^2`.