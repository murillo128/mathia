# AF-512 — The convergence boundary does not restore relative-curvature provenance

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `QUANTITATIVE-OBSTRUCTION` · `DIRICHLET-SOURCE` · `REMOTE-ATOM` · `GLOBAL-RELATIVE-PROFILE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P_{\mathbb P}(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_{\mathbb P}(s)=\frac{d^2}{ds^2}\log P_{\mathbb P}(s),
\qquad s>1,
\]

and, for an odd prime `a=p_n\ge 7`, replace that prime by the neighboring composite integer `b=a+1`:

\[
R_a=(\mathbb P\setminus\{a\})\cup\{b\}.
\tag{1}
\]

As in AF-511, every `R_a` is a primitive simple unit-weight positive-integer source, differs genuinely from the rational-prime source, and retains the same scale anchor `m=\log2` and the same two smallest generators `2,3`.

AF-511 proved that for each fixed `\sigma>1`, the curvature profiles become uniformly relatively indistinguishable on `[\sigma,\infty)`. The apparent remaining escape was to let the observation reach all the way down toward the convergence boundary `s\downarrow1`, where the prime zeta function diverges.

That escape also fails. One has

\[
\boxed{
\sup_{s>1}
\frac{|\kappa_{R_a}(s)-\kappa_{\mathbb P}(s)|}
     {\kappa_{\mathbb P}(s)}
\longrightarrow0
\qquad(a\to\infty\text{ through primes}).
}
\tag{2}
\]

Consequently,

\[
\boxed{
\sup_{s>1}
\left|\log\kappa_{R_a}(s)-\log\kappa_{\mathbb P}(s)\right|
\longrightarrow0.
}
\tag{3}
\]

Thus the rational-prime source has zero positive provenance margin even in the **full-domain uniform relative-curvature topology** on `(1,\infty)`. Extending the AF-511 observation window toward `s=1` does not recover robust exact-prime provenance.

The obstruction is stronger than mere right-tail suppression. Near `s=1`, the prime-zeta curvature itself diverges at order

\[
\kappa_{\mathbb P}(1+t)
\asymp
\frac{1}{t^2\log(1/t)},
\qquad t\downarrow0,
\tag{4}
\]

while replacing one remote neighboring generator changes the prime Dirichlet sum and its first two derivatives only by `O(a^{-2}(1+\log^2 a))` on a fixed neighborhood of the boundary. The divergence therefore *dilutes* the relative effect of that remote arithmetic change rather than amplifying it.

## Derivation

Write

\[
P(s):=P_{\mathbb P}(s),
\qquad
\kappa(s):=\kappa_{\mathbb P}(s),
\qquad
D_a(s):=b^{-s}-a^{-s},
\]

so that

\[
P_{R_a}(s)=P(s)+D_a(s)=P(s)(1+\eta_a(s)),
\qquad
\eta_a(s):=\frac{D_a(s)}{P(s)}.
\tag{5}
\]

Then

\[
\kappa_{R_a}(s)-\kappa(s)
=
\frac{d^2}{ds^2}\log(1+\eta_a(s)).
\tag{6}
\]

The proof splits the domain into a fixed neighborhood of `s=1` and the complementary closed right half-line.

### 1. Prime-zeta asymptotics give a quantitative curvature scale near `s=1`

For real `s>1`, the classical Möbius inversion formula is

\[
P(s)=\sum_{k\ge1}\frac{\mu(k)}{k}\log\zeta(ks).
\tag{7}
\]

Near `s=1`, the `k=1` term contains the only singularity; the sum over `k\ge2` is analytic with bounded derivatives on a sufficiently small real neighborhood of `1`. Since `\zeta(1+t)=t^{-1}+O(1)` as `t\downarrow0`, equation `(7)` gives, with

\[
L(t):=\log\frac1t,
\]

the standard estimates

\[
P(1+t)=L(t)+O(1),
\tag{8}
\]

\[
P'(1+t)=-\frac1t+O(1),
\qquad
P''(1+t)=\frac1{t^2}+O(1).
\tag{9}
\]

Put `g=\log P`. From `(8)`--`(9)`, after fixing a sufficiently small `\delta_0>0`, there are constants `c,C>0` such that for all `0<t\le\delta_0`,

\[
\frac1{P(1+t)}\le\frac{C}{L(t)},
\qquad
|g'(1+t)|\le\frac{C}{tL(t)},
\tag{10}
\]

and

\[
\boxed{
\frac{c}{t^2L(t)}
\le
\kappa(1+t)=g''(1+t)
\le
\frac{C}{t^2L(t)}.
}
\tag{11}
\]

Indeed,

\[
\kappa
=\frac{P''}{P}-\left(\frac{P'}P\right)^2,
\]

where the first term has size `1/(t^2L)` and the second is smaller by an additional factor `1/L`.

Equation `(11)` is the key boundary fact: the retained curvature becomes large as the convergence boundary is approached.

### 2. A neighboring remote replacement is uniformly second-order small in generator scale

For `j=0,1,2`, differentiate `D_a(s)` with respect to `s`. Each derivative is the difference of the values at `a` and `a+1` of a function of the form

\[
x\longmapsto (-\log x)^j x^{-s}.
\]

The mean-value theorem in the generator variable `x` therefore gives, uniformly for `1<s\le1+\delta_0`,

\[
|D_a(s)|\le \frac{C}{a^2},
\tag{12}
\]

\[
|D_a'(s)|\le \frac{C(1+\log a)}{a^2},
\qquad
|D_a''(s)|\le \frac{C(1+\log^2a)}{a^2}.
\tag{13}
\]

The extra factor `a^{-1}` compared with a crude single-atom bound is the exact cancellation produced by replacing `a` with its neighbor `a+1` rather than merely deleting `a`.

### 3. Relative curvature perturbation is uniformly small all the way to the boundary

From `\eta_a=D_a/P` and `g=\log P`, direct differentiation gives

\[
\eta_a'
=\frac1P\left(D_a'-g'D_a\right),
\tag{14}
\]

and

\[
\eta_a''
=\frac1P
\left[
D_a''-2g'D_a'
+\big((g')^2-\kappa\big)D_a
\right].
\tag{15}
\]

Using `(10)`--`(13)` in `(15)` and then dividing by the lower bound in `(11)` yields

\[
\frac{|\eta_a''(1+t)|}{\kappa(1+t)}
\le
\frac{C}{a^2}
\left[
 t^2(1+\log^2a)
 +\frac{t(1+\log a)}{L(t)}
 +\frac1{L(t)}
 +\frac1{L(t)^2}
\right].
\tag{16}
\]

Because `0<t\le\delta_0` and `L(t)` is bounded below by a positive constant there, `(16)` implies the uniform estimate

\[
\sup_{1<s\le1+\delta_0}
\frac{|\eta_a''(s)|}{\kappa(s)}
\le
C_{\delta_0}\frac{1+\log^2a}{a^2}.
\tag{17}
\]

Similarly, `(14)` gives

\[
\sup_{1<s\le1+\delta_0}
\frac{|\eta_a'(s)|^2}{\kappa(s)}
\le
C_{\delta_0}
\left(\frac{1+\log^2a}{a^2}\right)^2.
\tag{18}
\]

Also `|\eta_a|\to0` uniformly on this interval. Hence for all sufficiently large `a`, `|\eta_a|\le1/2`, and from

\[
\frac{d^2}{ds^2}\log(1+\eta_a)
=
\frac{\eta_a''}{1+\eta_a}
-
\frac{(\eta_a')^2}{(1+\eta_a)^2}
\tag{19}
\]

we obtain

\[
\boxed{
\sup_{1<s\le1+\delta_0}
\frac{|\kappa_{R_a}(s)-\kappa(s)|}{\kappa(s)}
\le
C_{\delta_0}\frac{1+\log^2a}{a^2}
\longrightarrow0.
}
\tag{20}
\]

Thus the singular boundary is not a hidden high-resolution region for this discriminator. Its own curvature scale grows too quickly for a single remote neighboring replacement to retain a nonvanishing relative signature.

### 4. AF-511 controls the rest of the half-line

On the complementary region

\[
s\ge1+\delta_0,
\]

AF-511 applies with the fixed abscissa `\sigma=1+\delta_0` and gives

\[
\sup_{s\ge1+\delta_0}
\frac{|\kappa_{R_a}(s)-\kappa(s)|}{\kappa(s)}
\le
C_{\delta_0}(1+\log^2(a/2))
\left(\frac3a\right)^{1+\delta_0}
\longrightarrow0.
\tag{21}
\]

Taking the maximum of `(20)` and `(21)` proves the full-domain relative estimate `(2)`.

For sufficiently large `a`, the supremum in `(2)` is less than `1/2`. Since both curvature profiles are strictly positive and `|\log(1+x)|\le2|x|` for `|x|\le1/2`, equation `(3)` follows.

## Fidelity and matched-control audit

Define the full-domain scale-invariant metric

\[
d_{(1,\infty)}(Q,R)
:=
\sup_{s>1}|\log\kappa_Q(s)-\log\kappa_R(s)|.
\tag{22}
\]

For the exact-prime provenance discriminator

\[
D(Q)=\mathbf1_{\{Q=\mathbb P\}},
\]

one has `D(R_a)=0` for every control and `D(\mathbb P)=1`, while `(3)` says

\[
d_{(1,\infty)}(R_a,\mathbb P)\to0.
\tag{23}
\]

The same controls keep the AF-509 scale anchor exactly fixed, so adjoining `m_Q=\log\min Q` does not repair the margin.

This closes the most immediate topology escape left open by AF-511. Merely observing the same relative-curvature carrier on a larger interval, even the entire domain of absolute convergence, cannot create robust rational-prime provenance.

The result does **not** say that every stronger topology fails. A topology that explicitly prices remote generator scale, an atom-indexed observation, or an independent arithmetic incidence such as congruence/additive structure can be genuinely stronger than `(22)` and is not tested here. What is ruled out is the idea that the missing margin was caused only by truncating the observation away from `s=1`.

## Prior art and novelty assessment

The analytic ingredients are classical and no novelty is claimed for prime-zeta behavior at the convergence boundary.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187–202, DOI `10.1007/BF01933420`, is a classical source for the prime zeta function and its Möbius-inversion relation to `\log\zeta`.
- NIST Digital Library of Mathematical Functions, §25.2, records the meromorphic continuation of `\zeta(s)` with its unique simple pole at `s=1` of residue `1`; combined with the Möbius formula, this gives `(8)`--`(9)` directly.
- AF-511 already audits the surrounding inverse-Laplace and Prony stability literature and proves the closed-half-line estimate used in `(21)`. The present finding does not claim a new general inverse-problem theorem.

A literature search for prime-zeta curvature, log-prime-zeta second-derivative variance, and remote finite-generator replacement did not expose a standard theorem matching `(2)`. The durable Arithmetic Fidelity delta is nevertheless intentionally narrow: `(2)` is an application-specific completion of AF-511 showing that the convergence boundary does not restore the missing provenance margin.

## Boundaries and failure modes

- **Exact fidelity is unchanged.** AF-509 still proves that equality of the complete curvature profile classifies primitive simple integer sources exactly, and AF-510 still gives a canonical exact inverse. This finding concerns continuity and separation margin, not injectivity.
- **Neighbor replacement matters to the boundary estimate.** The `a\mapsto a+1` control gives the `a^{-2}` cancellation in `(12)`--`(13)`. The present proof does not claim the same quantitative bound for arbitrary remote replacement distances growing with `a`.
- **The metric is relative curvature.** Stronger source-aware norms, moving windows tied to generator scale, atom-indexed measurements, or independent arithmetic lifts remain open.
- **The target is exact rational-prime provenance.** A finite Euler modification is much stronger than what many RH-facing discriminators need to distinguish. In fact, if one formally forms the Euler product associated with the modified generator set, it differs from `\zeta(s)` by a finite Euler-factor ratio, so its nontrivial zero set in `0<\Re s<1` is not changed by this local replacement. Therefore `(2)` should not be promoted into an obstruction to every RH-relevant carrier.
- **No value at `s=1` is used.** The metric is over the open domain `(1,\infty)`; the proof controls the limit toward the boundary rather than assigning a finite curvature value there.

## Research consequence

AF-511 left two superficially different explanations for the zero provenance margin: remote generators are exponentially suppressed on fixed right half-lines, or the observation window simply starts too far from the convergence boundary. Equation `(2)` removes the second explanation.

For this curvature carrier, a successful robust rational-prime lift must therefore change the **information topology**, not merely enlarge the same observation domain. In particular, the next viable tests should ask whether a source-scale-adaptive observation, a genuinely arithmetic incidence mark, or a deliberately coarser RH-relevant target has a positive separation margin that the full-domain relative curvature lacks.