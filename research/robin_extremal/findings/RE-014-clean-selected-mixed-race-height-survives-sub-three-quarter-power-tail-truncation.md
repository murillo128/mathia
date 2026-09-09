# RE-014 — clean selected mixed-race height survives sub-three-quarter-power tail truncation

**Status:** `EXACT-DERIVED + SELECTOR-CONDITIONED-SHORT-HORIZON-BOUND + REMOTE-TAIL-LOCALIZATION + SUB-SQUARE-ROOT-PLATEAU + NEGATIVE/OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-008` represents the endpoint-subtracted Mertens remainder as a future weighted Chebyshev tail, `RE-009` identifies its square-root normalization with the classical mixed reciprocal/standard prime race, and `RE-010` shows that the Robin sign at a clean regular self-tangent CA local peak is decided by whether that selected mixed-race value crosses `2 sqrt(2)`. `RE-012` then proves that the complete smooth germ inside the one prime-free chamber containing the selected coordinate supplies no extra arithmetic degree of freedom.

The nonlocality can be pushed substantially farther. Let `C` run through any unbounded sequence of sufficiently large **clean regular self-tangent CA local peaks**, put

\[
X=\log C,
\]

and let `p<X<q` be its consecutive first-layer boundary primes. Define

\[
\Delta(t):=\vartheta(t)-t,
\qquad
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\qquad
k(t):=\frac1{t\log t},
\]

\[
I(t):=\Delta(t)h'(t)-\bigl(h(t)-k(t)\bigr),
\qquad
\mathcal M_*(x):=\int_x^\infty I(t)\,dt,
\qquad
\mathscr Y(x):=\sqrt x\log x\,\mathcal M_*(x).
\tag{1}
\]

The improper-integral identity in (1) is the real-input continuation of the exact tail formula in `RE-008`; continuity at ordinary primes is supplied by `RE-011`.

Then for every fixed

\[
0<\alpha<\frac34,
\qquad H:=p^\alpha,
\]

one has

\[
\boxed{
\sqrt p\log p
\int_p^{p+H} I(t)\,dt=o(1).
}
\tag{2}
\]

Consequently the selected mixed-race value is unchanged to first Robin order if the initial future window of any fixed sub-`p^(3/4)` power is deleted:

\[
\boxed{
\mathscr Y(p)
=
\sqrt p\log p
\int_{p+p^\alpha}^{\infty} I(t)\,dt+o(1)
\qquad(0<\alpha<3/4).
}
\tag{3}
\]

Combining this with `RE-010` gives the clean Robin-height localization

\[
\boxed{
\sqrt p\log p\,\bigl(\log G(C)-\gamma\bigr)
=
\sqrt p\log p
\int_{p+p^\alpha}^{\infty}I(t)\,dt
-2\sqrt2+o(1).
}
\tag{4}
\]

Thus any unbounded clean Robin-counterexample sequence necessarily satisfies, for every fixed `alpha<3/4`,

\[
\boxed{
\liminf
\sqrt p\log p
\int_{p+p^\alpha}^{\infty}I(t)\,dt
\ge2\sqrt2.
}
\tag{5}
\]

This sharpens the information boundary after `RE-012`: even crossing all ordinary-prime endpoints in a polynomial forward window does not make the direct contribution of that window visible at first Robin order, provided its length is `p^alpha` with `alpha<3/4`. The required positive excursion therefore survives as a genuinely remote tail condition rather than a finite-chamber or short-horizon effect.

There is also a stronger statement for the normalized race itself on shorter scales. For every fixed `0<alpha<1/2`,

\[
\boxed{
\mathscr Y(p+p^\alpha)-\mathscr Y(p)\longrightarrow0.
}
\tag{6}
\]

So the CA-selected mixed coordinate has an asymptotic **sub-square-root plateau** to the right of the boundary prime, despite potentially crossing many ordinary primes. This is a selected-point statement, not a global modulus of continuity for the mixed prime race.

## 1. Clean self-tangency gives a `p^0.52` endpoint bound for `theta(p)-p`

`RE-006` gives the exact clean selector

\[
\Delta(p)=X-p-\Phi_{\ge2}(X).
\tag{7}
\]

`RE-007` proves

\[
\Phi_{\ge2}(X)=\sqrt{2X}+o(\sqrt X),
\qquad X/p\to1.
\tag{8}
\]

The current unconditional short-interval input already anchored in `SOURCES.md` and used in `RE-008` implies that consecutive-prime gaps satisfy

\[
q-p=O(p^{0.52}).
\tag{9}
\]

Since `0<X-p<q-p`, equations (7)--(9) give the source-selected endpoint estimate

\[
\boxed{
|\Delta(p)|=O(p^{0.52}).
}
\tag{10}
\]

This is not asserted for arbitrary primes. The improvement over the generic elementary size bound comes from evaluating `Delta` at a boundary prime coupled to the exact clean self-tangent CA selector.

No square-root prime-gap estimate is being assumed. The exponent `0.52` is used only as an unconditional upper bound below `3/4`; any future unconditional exponent `beta<3/4` would serve equally well in the endpoint term of the argument below.

## 2. The Chebyshev discrepancy cannot grow fast enough on a sub-`p^(3/4)` forward window

Fix `alpha<3/4` and put `H=p^alpha`. For sufficiently large `p`, `H<p`, so every `t` in `[p,p+H]` satisfies `t<2p`. Monotonicity of `theta` and the trivial fact that an interval of length `H` contains at most `H+1` integers give

\[
0\le\vartheta(t)-\vartheta(p)
\le(H+1)\log(2p).
\tag{11}
\]

Therefore

\[
\begin{aligned}
|\Delta(t)|
&\le|\Delta(p)|
  +|\vartheta(t)-\vartheta(p)|
  +(t-p)\\
&=O\!\left(p^{0.52}+H\log p\right),
\end{aligned}
\tag{12}
\]

uniformly over the whole interval. This deliberately uses no prime number theorem in short intervals and no cancellation between the prime jumps and the linear drift.

The elementary logarithm expansion gives, uniformly for `t` comparable with `p`,

\[
h(t)-k(t)=O\!\left(\frac1{p^2\log p}\right),
\qquad
h'(t)=O\!\left(\frac1{p^2\log p}\right).
\tag{13}
\]

Combining (12)--(13),

\[
\left|
\int_p^{p+H}I(t)\,dt
\right|
\ll
\frac{H\,p^{0.52}}{p^2\log p}
+
\frac{H^2}{p^2}
+
\frac{H}{p^2\log p}.
\tag{14}
\]

After multiplication by the Robin normalization `sqrt(p) log p`,

\[
\boxed{
\sqrt p\log p
\left|
\int_p^{p+H}I(t)\,dt
\right|
\ll
p^{\alpha-0.98}
+p^{2\alpha-3/2}\log p
+p^{\alpha-3/2}.
}
\tag{15}
\]

Every term tends to zero for fixed `alpha<3/4`, proving (2). The threshold `3/4` here is a **method boundary** produced by the deliberately crude worst-case growth `theta(t)-theta(p)=O(H log p)`. No claim is made that the true local contribution becomes non-negligible at `p^(3/4)`.

## 3. Deleting the short future window leaves the Robin threshold unchanged

`RE-008` proves the convergent improper-tail formula at the boundary prime, and `RE-011` shows that `M_*` is continuous across ordinary primes and differentiable between them with derivative `I`. Hence for every finite `H>0`,

\[
\mathcal M_*(p)
=
\int_p^{p+H}I(t)\,dt
+
\int_{p+H}^{\infty}I(t)\,dt.
\tag{16}
\]

Multiplying (16) by `sqrt(p) log p` and using (2) proves (3). `RE-010` supplies independently

\[
\sqrt p\log p\,\bigl(\log G(C)-\gamma\bigr)
=\mathscr Y(p)-2\sqrt2+o(1),
\tag{17}
\]

so (4) follows immediately. If the clean peaks are Robin counterexamples, the left side of (17) is positive, and (5) follows.

Equation (5) is stronger than saying that the endpoint value `theta(p)-p` is insufficient. It says that after the exact endpoint cancellation of `RE-008`, **all of the direct mixed-tail contribution accumulated through a polynomially long initial future window is still asymptotically negligible at Robin scale**. A successful clean-chamber theorem must therefore control a tail that remains beyond every fixed `p^alpha` horizon with `alpha<3/4`, or use arithmetic information whose effect is transported into that remote tail.

The last qualification is essential. Deleting the integral over `[p,p+H]` does not mean that primes in this window have no influence on later values of `Delta(t)`: their cumulative contribution is carried in the state `theta(t)` beyond the cutoff. The theorem localizes the **direct integral contribution**, not causal dependence of the remote tail on earlier prime data.

## 4. The normalized mixed race is flat on every fixed sub-square-root power window

The local estimate also yields an actual normalized-value comparison when the change of normalization is small. Since

\[
\mathcal M_*(p+H)-\mathcal M_*(p)
=-\int_p^{p+H}I(t)\,dt,
\tag{18}
\]

equation (2) gives

\[
\sqrt p\log p\,
\bigl(\mathcal M_*(p+H)-\mathcal M_*(p)\bigr)=o(1)
\tag{19}
\]

for every fixed `alpha<3/4`.

Now let `alpha<1/2`. For `s(x)=sqrt(x) log x`, the mean-value theorem gives

\[
s(p+H)-s(p)
=O\!\left(\frac{H\log p}{\sqrt p}\right)
=o(1).
\tag{20}
\]

Mertens' product theorem together with the prime number theorem gives `M_*(x)->0`, as already used in `RE-008`. Therefore

\[
\begin{aligned}
\mathscr Y(p+H)-\mathscr Y(p)
&=[s(p+H)-s(p)]\mathcal M_*(p+H)\\
&\quad+s(p)\bigl(\mathcal M_*(p+H)-\mathcal M_*(p)\bigr)
=o(1),
\end{aligned}
\tag{21}
\]

which proves (6).

The `1/2` threshold is again only what follows from changing the external normalization without importing a quantitative decay rate for `M_*`. Equation (3) remains valid all the way to every fixed `alpha<3/4` because it keeps the normalization frozen at the selected boundary `p`.

## 5. Prior art and novelty boundary

The global mixed prime-race coordinate is prior art. Bhattacharya--Martin--Simpson study correlations of standard and reciprocal weighted prime-counting errors, and `RE-009` already records that global one-sided control of the relevant mixed difference is RH-equivalent. Their theory concerns global normalized errors and their correlation/distribution; it does not provide the clean CA selector or the selected future-tail truncation (2)--(5).

The self-tangent CA event measure and exact workload representation are likewise closest to Mantovanelli's August 2026 preprint and computational companion, already anchored in `SOURCES.md`. The public companion certifies finite event sweeps, self-tangent returns, packet identities, moment identities, and prime-frontier decompositions. It is not used as a premise for the asymptotic short-horizon estimate here.

A targeted search across current weighted-prime-error correlation work, Mertens-product short-interval terminology, and the recent Robin/CA literature did not locate the specific selector-conditioned statement that the first `p^alpha`, `alpha<3/4`, portion of the endpoint-subtracted future tail is `o(1)` after Robin normalization. No blanket novelty claim is made: the finite-window estimate is elementary once the existing exact selector and tail representation are spliced. The Mathia-specific delta is the **source-selected consequence** (4)--(5), which moves the unresolved clean counterexample excursion beyond a polynomial forward horizon without invoking an RH-strength global bound.

No new source anchor is needed. The only non-elementary external input beyond canonical findings is the same `p^0.52` unconditional consecutive-prime-gap consequence of Runbo Li already recorded in `SOURCES.md` and used in `RE-008`; all finite-window growth estimates in Section 2 are elementary.

## 6. Falsification boundaries and research consequence

Several quantifiers are load-bearing. The point `p` must be the left ordinary-prime boundary of an unbounded **clean regular self-tangent CA local-peak** sequence; (10) is not claimed at arbitrary primes. The cutoff exponent `alpha` is fixed strictly below `3/4`; neither the error term nor the argument is uniform as `alpha` approaches `3/4` with `p`. Equation (6) uses the stronger restriction `alpha<1/2` because the normalization itself changes across the interval.

The result does not bound the remote tail, prove that its liminf is below `2sqrt(2)`, or make the selected correlation problem easier by itself. It also does not apply to the exceptional higher-layer/tied boundary chamber isolated in `RE-004`. Under RH failure, forced counterexample peaks may still concentrate there.

What it does rule out is another natural local continuation after `RE-012`: crossing finitely many prime endpoints, or even all endpoints in any fixed sub-`p^(3/4)` power window, cannot by its **direct contribution** decide the first-order clean Robin height. The clean obligation from `RE-010` is genuinely long-range. A useful positive theorem must exploit source information that controls the remote weighted Chebyshev/Mertens tail at CA-selected boundaries, a nonlocal correlation across growing scales, or else force hypothetical counterexamples into the exceptional event chamber. More local derivatives, fixed prime-layer depth, and now short forward horizons all fail as independent first-order channels.