# PC-274 — all-bandwidth raw near-resonance laws are prime-blind

**Status:** `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the raw ordered near-resonance source law left open after PC-271--PC-273.

PC-272 showed that the finite-window quantity

\[
\Delta_B(p,r;q)
=
\min_{0<\max(|h|,|k|)\le B}
\left\|\frac{hp+kr}{q}\right\|_{\mathbb R/\mathbb Z}
\]

retains ordered source placement that the exact ratio lattice loses. PC-273 then proved that its prime-source distribution is asymptotically indistinguishable from the all-residue matched control when `B=o(log q)`, but left `B` comparable with or larger than `log q` as an apparent open raw-distribution regime.

That remaining raw regime actually collapses once PC-273 is combined with the universal Dirichlet bound already proved in PC-271. For every prime upper level `q` and every integer bandwidth `B>=1`, let `rho^prime_{q,B}` and `rho^grid_{q,B}` be the prime-pair and distinct nonzero-residue-grid laws defined in PC-273. Then

\[
\boxed{
W_1\!\left(\rho^{\mathrm{prime}}_{q,B},
           \rho^{\mathrm{grid}}_{q,B}\right)
\le
\min\!\left(
C\frac{B}{\log q}+C\frac{\log q}{q},
\frac1{(B+1)^2}
\right)
}
\tag{1}
\]

for an absolute constant `C` and all sufficiently large prime `q`. Consequently,

\[
\boxed{
\sup_{B\ge1}
W_1\!\left(\rho^{\mathrm{prime}}_{q,B},
           \rho^{\mathrm{grid}}_{q,B}\right)
\ll
(\log q)^{-2/3}+\frac{\log q}{q}
\longrightarrow0.
}
\tag{2}
\]

Thus **the raw unscaled `Delta_B` source law is asymptotically prime-blind for every bandwidth sequence `B=B(q)`**, including arbitrary oscillating sequences and the entire intermediate regime between fixed resolution and the exact-resonance scale. The finite PC-272 information-gain witness remains correct, but it cannot survive as a raw asymptotic distributional discriminator.

This supersedes only the boundary interpretation in PC-273 that treated `B` comparable with or larger than `log q` as still open for the raw `Delta_B` law. The quantitative PC-273 theorem itself remains correct. What survives is a **rescaled or enriched** near-resonance problem, not the unscaled law.

## 1. Two independent bounds control opposite bandwidth regimes

PC-273 proves, from the prime number theorem and the `B`-Lipschitz property of the finite-window minimum,

\[
W_1\!\left(\rho^{\mathrm{prime}}_{q,B},
           \rho^{\mathrm{grid}}_{q,B}\right)
\ll
\frac{B}{\log q}+\frac{\log q}{q}.
\tag{3}
\]

This is strongest when `B` is small relative to `log q`.

Independently, PC-271 proves for every admissible rational source pair that

\[
\boxed{
\Delta_B(p,r;q)\le\frac1{(B+1)^2}.
}
\tag{4}
\]

Exactly the same pigeonhole proof applies to the all-residue control

\[
D_B(a/q,b/q)
=
\min_{0<\max(|h|,|k|)\le B}
\left\|\frac{ha+kb}{q}\right\|_{\mathbb R/\mathbb Z}.
\tag{5}
\]

Hence both probability measures are supported in the same shrinking interval

\[
\left[0,\frac1{(B+1)^2}\right].
\tag{6}
\]

Any two probability measures supported in an interval of diameter `d` have `W_1<=d`. Therefore

\[
\boxed{
W_1\!\left(\rho^{\mathrm{prime}}_{q,B},
           \rho^{\mathrm{grid}}_{q,B}\right)
\le\frac1{(B+1)^2}.
}
\tag{7}
\]

No prime number theorem, character sum, or arithmetic input enters (7). At growing bandwidth, the raw observable itself is forced to zero uniformly over **all** rational source configurations.

Taking the better of (3) and (7) gives (1).

## 2. Uniform all-bandwidth convergence

Put `L=log q`. Split the integer bandwidths at

\[
B=L^{1/3}.
\tag{8}
\]

If `1<=B<=L^{1/3}`, equation (3) gives

\[
W_1
\ll
L^{-2/3}+\frac{L}{q}.
\tag{9}
\]

If `B>L^{1/3}`, equation (7) gives

\[
W_1
\le
(B+1)^{-2}
<
L^{-2/3}.
\tag{10}
\]

Combining the two regions proves (2). Equivalently, for **every** choice of bandwidth sequence `B(q)>=1`,

\[
\boxed{
W_1\!\left(\rho^{\mathrm{prime}}_{q,B(q)},
           \rho^{\mathrm{grid}}_{q,B(q)}\right)
\to0.
}
\tag{11}
\]

There is no hidden regularity assumption on `B(q)`: it may stay bounded, diverge, or oscillate between the two regimes. Bounded/sub-cuberoot values are killed by one-dimensional prime equidistribution; larger values are killed by the universal two-dimensional Dirichlet collapse of the observable itself.

The exponent `1/3` is not a new arithmetic scale. It is merely where the two available upper bounds `B/L` and `B^{-2}` balance.

## 3. Why this is stronger than PC-273

PC-273 correctly established that at fixed bandwidth, and more generally at `B=o(log q)`, the prime-source and grid-source laws agree asymptotically. Its final boundary discussion treated the remaining growing-resolution region as potentially source-sensitive because the PNT/Lipschitz estimate no longer tends to zero there.

But failure of that **particular estimate** is not failure of matched-control convergence. Once `B` grows, the geometric quantity being compared shrinks uniformly by (4). Thus the two regimes complement rather than compete with one another:

\[
\text{small }B:
\quad
\text{source measures become indistinguishable};
\qquad
\text{large }B:
\quad
\text{the observable itself collapses to }0.
\tag{12}
\]

This closes the raw-distribution route across the complete bandwidth axis. The finite example

\[
\Delta_1(3,5;13)\ne\Delta_1(7,3;13)
\]

from PC-272 still proves that finite-window ordered placement contains information absent from the ratio quotient. PC-274 shows that **raw asymptotic distribution is too coarse to preserve that gain**.

## 4. The nontrivial continuation must renormalize or retain more structure

Equation (4) identifies the first natural non-collapsing scale. Define

\[
X_{q,B}:=(B+1)^2\Delta_B.
\tag{13}
\]

Then `0<=X_{q,B}<=1`; unlike raw `Delta_B`, its support does not collapse merely because `B` grows. This normalization is also intrinsic to PC-271's partial-window mechanism: the universal coherent-window boundary is `M asymp B^2`, and the relevant phase parameter is `M Delta_B`.

Scaling PC-273's transport estimate gives the preliminary matched-control bound

\[
W_1\!\left(
\operatorname{Law}_{\mathrm{prime}}(X_{q,B}),
\operatorname{Law}_{\mathrm{grid}}(X_{q,B})
\right)
\ll
\frac{B^3}{\log q}
+
\frac{B^2\log q}{q},
\tag{14}
\]

up to harmless constants from replacing `B+1` by `B`. Hence even this normalized carrier is prime-blind under the same all-residue control throughout

\[
B=o\!\left((\log q)^{1/3}\right).
\tag{15}
\]

The cuberoot boundary in (15) is only where this elementary control stops forcing convergence. It is **not** evidence that prime arithmetic appears there. In particular, a stricter smooth-density control reflecting the classical `dt/log t` prime intensity can move that comparison scale, so (15) must not be promoted to a new RH scale without a fresh audit.

Other honest survivors are the signed/directional near-resonance vector rather than its scalar minimum, centered or singular source fluctuations, conditioning on source subfamilies, or a source-forced nonlocal transfer observable coupled to the near-resonance event. Each preserves information discarded by the raw scalar law and therefore requires a separate matched-control and prior-art test.

## 5. Prior-art and novelty audit

No new external theorem is required for (1)--(11). The two inputs were already classicalized in the immediately preceding findings.

PC-271 identifies `Delta_B` with the standard rank-one-lattice/Diophantine spectral-test carrier and proves (4) by the elementary two-dimensional pigeonhole/Dirichlet argument. Its literature anchors include Sloan--Joe on rank-one lattice rules, Niederreiter on lattice spectral tests, Cassels on geometry of numbers, and Pillichshammer--Sonnleitner on spectral tests and discrepancy.

PC-273 obtains (3) from the ordinary prime number theorem plus elementary one-dimensional Wasserstein transport. Its source anchor is Montgomery--Vaughan, *Multiplicative Number Theory I: Classical Theory*, together with standard weak-convergence/transport facts.

A targeted external search against rank-one lattice spectral tests, shrinking-target/Diophantine minima, normalized prime empirical measures, and Wasserstein formulations of prime equidistribution found the same classical ingredients and neighboring shrinking-target literature, but no additional theorem is needed for the squeeze argument. **No novelty is claimed for PNT equidistribution, the Dirichlet `B^{-2}` bound, Wasserstein diameter bounds, or their abstract combination.** The durable project-local result is the closure of the exact raw `Delta_B` source-statistics escape that PC-273 had left open: the two already-established classical controls cover complementary bandwidth ranges and together eliminate the entire raw family.

The natural normalized/shrinking-target continuation in (13) belongs to established Diophantine and shrinking-target territory at the carrier level. Any future Prime-Circle claim must therefore establish source-specific arithmetic beyond those classical mechanisms rather than count the normalization itself as progress.

## 6. Audit and falsification tests

The conclusion has direct failure tests.

1. Find an admissible rational source pair with `Delta_B>1/(B+1)^2`. This would contradict the exact PC-271 pigeonhole argument and would invalidate the large-bandwidth half of the squeeze.
2. Find a prime upper level `q`, bandwidth `B`, and either source law with mass outside `[0,(B+1)^{-2}]`. This is the measure-level form of the same contradiction.
3. Reproduce the PC-273 PNT/Wasserstein estimate (3). Any failure there would affect the small-bandwidth half but not the universal collapse (7).
4. Exhibit a bandwidth sequence `B(q)` for which the raw prime/grid `W_1` distance stays bounded below by a positive constant. Equations (9)--(10) rule this out for every possible sequence.
5. Rescale by `(B+1)^2`, retain the minimizing vector `(h,k)`, condition on rare source events, or couple `Delta_B` to another operator. Such an observable lies outside the raw-law theorem and is a legitimate continuation rather than a counterexample.

## 7. Consequences for the research line

The route

\[
\text{ordered prime placement}
\longrightarrow
\text{raw }\Delta_B\text{ source law at any bandwidth}
\longrightarrow
\text{prime-specific asymptotic spectral signal}
\]

is closed against the all-residue rational-torus control.

This is a stronger negative boundary than PC-273: there is no intermediate raw bandwidth window to search. Any further work on the PC-271/PC-272 ordered-time escape must preserve the shrinking scale, direction, conditioning, or an additional nonlocal coupling. The most immediate scalar continuation is the normalized variable `(B+1)^2 Delta_B`, not `Delta_B` itself, and even that remains classicalized against the basic grid control below cuberoot-log bandwidth.