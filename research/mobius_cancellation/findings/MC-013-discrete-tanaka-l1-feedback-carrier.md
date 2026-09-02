# MC-013 — Discrete Tanaka decomposition isolates the exact L1 feedback carrier

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NO-NOVELTY-CLAIM`.

## Claim

Set `M(0)=0` and use `sgn(0)=0`. Because every Möbius increment satisfies `mu(n) in {-1,0,1}`, the Mertens walk obeys the exact pathwise identity

\[
|M(n)|-|M(n-1)|
=
\operatorname{sgn}(M(n-1))\mu(n)
+
\mathbf 1_{\{M(n-1)=0\}}\mu(n)^2.
\tag{1}
\]

Thus the absolute-value process has two and only two one-step contributions: a **signed feedback term** measuring whether the next Möbius increment agrees with the sign of the current excursion, and a nonnegative **zero-departure local-time term** that appears because `|x|` has a kink at zero.

For every integer `N>=1`, Pintz's mean-absolute statistic satisfies exactly

\[
N D_M(N)
=
\int_0^N |M(u)|\,du
=
\sum_{n=1}^{N-1}(N-n)
\left(
\operatorname{sgn}(M(n-1))\mu(n)
+
\mathbf 1_{\{M(n-1)=0\}}\mu(n)^2
\right).
\tag{2}
\]

Define

\[
C_{\rm sgn}(N)
:=
\sum_{n<N}(N-n)\operatorname{sgn}(M(n-1))\mu(n),
\tag{3}
\]

and

\[
L_0(N)
:=
\sum_{n<N}(N-n)\mathbf 1_{\{M(n-1)=0\}}\mu(n)^2.
\tag{4}
\]

Then

\[
\boxed{N D_M(N)=C_{\rm sgn}(N)+L_0(N).}
\tag{5}
\]

Equation (5) gives a lossless signed interface for the mean-absolute endpoint sought by this line. In particular, the genuinely non-circular sufficient estimate

\[
|C_{\rm sgn}(N)|+L_0(N)
\ll_\varepsilon N^{3/2+\varepsilon}
\tag{6}
\]

would imply

\[
D_M(N)\ll_\varepsilon N^{1/2+\varepsilon}.
\tag{7}
\]

The point is **not** that (5) itself makes (7) easier: a bound on the combined left-hand side of (5) is just the original target in new notation. The useful separation is that (3) and (4) are structurally different arithmetic objects that can now be attacked or falsified independently. Any future use must obtain their control from information not already equivalent to `D_M`.

## 1. Exact discrete Tanaka identity

Let `m=M(n-1)` and `a=mu(n)`. If `m!=0`, a step `a in {-1,0,1}` cannot cross zero without landing on zero, and direct inspection gives

\[
|m+a|-|m|=\operatorname{sgn}(m)a.
\tag{8}
\]

If `m=0`, the signed term vanishes and

\[
|m+a|-|m|=|a|=a^2.
\tag{9}
\]

Equations (8)–(9) prove (1). This is the elementary `{-1,0,1}` specialization of the discrete Tanaka principle: the nonsmooth chain rule for absolute value contains a sign-weighted increment plus local time at the kink.

Since `M(u)=M(k)` on `[k,k+1)` for integer `k`,

\[
\int_0^N|M(u)|\,du
=
\sum_{k=0}^{N-1}|M(k)|.
\tag{10}
\]

Summing (1) from `1` to `k` and then interchanging the two finite sums yields

\[
\sum_{k=0}^{N-1}|M(k)|
=
\sum_{n=1}^{N-1}(N-n)
\left(
\operatorname{sgn}(M(n-1))\mu(n)
+
\mathbf 1_{\{M(n-1)=0\}}\mu(n)^2
\right),
\tag{11}
\]

which is (2).

The local-time component has the elementary upper bound

\[
L_0(N)\le N V_0(N),
\qquad
V_0(N):=\sum_{n<N}\mathbf 1_{\{M(n-1)=0\}}\mu(n)^2,
\tag{12}
\]

where `V_0(N)` counts nonzero Möbius steps that depart from level zero. Therefore one explicit, deliberately stronger-than-necessary route to (7) would be

\[
V_0(N)\ll_\varepsilon N^{1/2+\varepsilon}
\quad\text{and}\quad
|C_{\rm sgn}(N)|\ll_\varepsilon N^{3/2+\varepsilon}.
\tag{13}
\]

No such bounds are asserted here.

## 2. Why the sign feedback is different from the known amplitude correlation

There is a parallel smooth chain rule for the square:

\[
M(n)^2-M(n-1)^2
=
2M(n-1)\mu(n)+\mu(n)^2.
\tag{14}
\]

Consequently, with

\[
Q(N)=\sum_{n\le N}\mu(n)^2,
\]

we have the exact unweighted identity

\[
\boxed{
2\sum_{n\le N}\mu(n)M(n-1)=M(N)^2-Q(N).
}
\tag{15}
\]

This is an important falsification boundary for partial-sum correlation ideas. An **unweighted** correlation between `mu(n)` and `M(n-1)` is not independent information: it is exactly the quadratic chain rule (15). Any new content must enter through a nontrivial weighting, scale structure, conditioning, or a different observable.

The closest recent arithmetic prior art found in the audit is Chavez (`MC-S22`), who studies logarithmically weighted correlations of `mu(n)` with `M(n-1)` and of Liouville with its partial sums. His main asymptotic formulas assume RH and simplicity of the nontrivial zeta zeros and connect the weighted correlations to negative moments of `zeta'(rho)`. That work makes the amplitude-weighted correlation a genuine literature object, but it does not supply an unconditional estimate for the sign-feedback carrier (3).

Equation (1) is the `L^1` analogue of (14): replacing the smooth energy `x^2` by `|x|` replaces the amplitude `M(n-1)` with the subgradient `sgn(M(n-1))` and forces the local-time correction (4). The correction cannot be dropped. At `M(n-1)=0`, the sign feedback is identically zero while a nonzero Möbius step increases `|M|` by one.

## 3. Relation to the existing local-to-global barriers

`MC-001` shows that a black-box short-interval argument retaining only local magnitudes and exceptional-set measure pays a triangle-inequality budget `eta X+B+H`. `MC-006` similarly shows that feeding the available averaged two-point Chowla estimate through black-box van der Corput retains only logarithmic global saving.

The carrier (3) identifies exactly one kind of information those routes discard: **whether the next Möbius increment tends to point toward or away from zero conditional on the sign of the accumulated past**. This is signed and history-dependent rather than a fixed-shift correlation.

That history dependence is also the main obstruction. Existing fixed-shift Chowla statements, logarithmically averaged correlations, and standard nilsequence orthogonality do not automatically estimate

\[
\mu(n)\operatorname{sgn}(M(n-1)),
\]

because the multiplier is generated endogenously by the same Möbius sequence up to time `n-1`. Treating it as an external deterministic test function would simply hide the hard part.

The local-time term (4) exposes a second missing datum: the frequency and timing of departures from zero. Bounding only the sign feedback is insufficient if the zero-departure contribution is left uncontrolled; conversely, bounding `L_0` alone says nothing about coherent drift during long excursions.

Thus (5) narrows the mean-absolute transfer question to a concrete two-component interface rather than solving it.

## Prior art and novelty assessment

Discrete Tanaka formulas and local-time corrections for random walks are classical probability-theory mechanisms. Fujita (`MC-S21`) explicitly derives a discrete Tanaka formula from a discrete Itô formula for simple random walks. The zero-increment variant used in (1) is an elementary pathwise specialization and no novelty is claimed for the Tanaka mechanism itself.

Chavez (`MC-S22`) is direct 2026 prior art for correlations between Möbius/Liouville values and their own partial sums. His observable is amplitude-weighted and logarithmically averaged; the theorem quoted in the paper is conditional on RH and simple zeros. Equation (15) also shows why the completely unweighted amplitude correlation would be algebraically non-independent.

A targeted search for `Tanaka`, `local time`, `sgn(M(n))`, and Möbius/Mertens partial-sum correlations found the random-walk Tanaka literature and Chavez's amplitude-correlation paper, but no source establishing this exact Mertens sign-feedback decomposition as a new number-theoretic theorem. Because (1)–(5) are elementary specializations of a classical chain-rule mechanism, **no novelty claim is made from absence of an exact literature hit**. The value of the finding is the audited research interface it exposes.

## Boundaries and failure modes

This finding does not improve any unconditional bound for `M(x)` or `D_M(x)`, prove RH, or validate the fresh Pintz theorem in `MC-009`.

Several tempting overinterpretations are explicitly excluded:

- the combined estimate `C_sgn(N)+L_0(N)=O(N^(3/2+epsilon))` is exactly equivalent to the desired bound for `D_M(N)` through (5), so it is not an independent criterion;
- `sgn(M(n-1))` is an endogenous global-history observable, not a fixed external phase or a standard Chowla shift;
- separate bounds such as (6) are stronger than necessary because a negative sign-feedback term can offset part of the positive local-time contribution;
- Brownian or random-walk behavior of sign feedback and local time is heuristic comparison only and cannot be transferred to deterministic Möbius without proof;
- the count `V_0(N)` alone is not a proxy for `D_M`: many zero visits may be accompanied by compensating negative feedback, while few zero visits may coexist with long large excursions.

The decisive next test is therefore non-circular: derive a polynomial upper bound for the triangular sign-feedback and local-time interface from independently controlled arithmetic information, or build a matched multiplicative/control model satisfying the available local/Chowla inputs while one of these components remains too large. Either outcome would materially answer whether the weaker mean-absolute endpoint is more accessible than pointwise Mertens control.

## Consequences for the line

The proposed mean-absolute transfer direction now has an exact candidate information carrier:

```text
Möbius increment
      +
current excursion sign
      +
zero-departure local time
      |
      v
exact triangular Tanaka identity
      |
      v
D_M(N)
```

This is more specific than asking generically for a signed or multiscale statistic, but it deliberately leaves the hard step exposed. To become an RH-relevant route, the sign-feedback/local-time terms must admit **independent polynomial control**; merely estimating their exact sum restates the endpoint.

If the Pintz mean-absolute zero-boundary theorem in `MC-009` survives its remaining audit, an independently proved estimate of the form (6) would feed directly into that weaker RH-complete endpoint. Until then, (5) is useful on its own as a precise local-to-global interface and a falsification target for correlation-based approaches.