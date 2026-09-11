# ANF-170 — dyadic endpoint danger forces a moving-window twisted-residual square-function witness

**Status:** `EXACT-DERIVED + POSITIVE-SQUARE-FUNCTION-BRIDGE + ENDPOINT-LOCAL + DISTINGUISHED-TWIST + SOURCE-SPECIFIC`. `ANF-169` shows that target-sized endpoint completion forces one endpoint and one dyadic lag shell to carry a positive signed shifted-correlation block of size `gg X log X/log K` after the natural `1/K` normalization. That is already a sharp source-side witness, but it leaves the next theorem in a signed bilinear form whose four prime/Ramanujan pieces can be awkward to estimate without destroying their common cancellation.

The same dyadic shell has an exact second representation. Reindexing by the later endpoint site factors it as a coefficient paired with a **preceding dyadic moving-window sum**. Cauchy--Schwarz then turns every dangerous signed shell into a lower bound for a positive square function of exact twisted-residual interval sums. Consequently, macroscopic endpoint completion forces a positive endpoint-local Selberg-integral-like witness, and conversely it is enough to prove a uniform upper bound for that positive square function. This does not close the arithmetic gate, but it replaces the signed-shell target by a positive quantity that is structurally closer to large-sieve, short-interval second-moment, or Type-I/II methods while retaining the exact distinguished multiplicative twist.

## 1. A dyadic shifted-correlation shell factors through preceding moving windows

Fix one endpoint `sigma in {-,+}` and suppress `sigma` temporarily. Keep the normalized endpoint correlation from `ANF-169`,

\[
G_h
=
\sum_{j=1}^{K-1-h}
\left(1-\frac{j+h}{K}\right)
\overline{b_j}b_{j+h},
\qquad 1\le h\le K-2.
\tag{1}
\]

For a dyadic integer `H<K`, let

\[
\mathcal H_H
:=
\{h:H\le h<\min(2H,K-1)\}
\tag{2}
\]

and define the signed shell

\[
S_H
:=
\sum_{h\in\mathcal H_H}G_h.
\tag{3}
\]

Write

\[
w_m:=1-\frac mK,
\qquad 1\le m<K,
\tag{4}
\]

and, for every later endpoint position `m`, define the preceding dyadic moving-window sum

\[
\boxed{
B_H(m)
:=
\sum_{\substack{h\in\mathcal H_H\\ h<m}}
 b_{m-h}.
}
\tag{5}
\]

Thus `B_H(m)` sums the coefficients whose lag behind `m` lies between `H` and `2H`, with the natural truncation near the endpoint. Setting `m=j+h` in (1) and summing over the shell gives the exact identity

\[
\boxed{
S_H
=
\sum_{m=H+1}^{K-1}
 w_m b_m\overline{B_H(m)}.
}
\tag{6}
\]

No source assumption, asymptotic approximation, or phase linearization enters (6). It is just a reindexing of the finite triangular correlation ledger. The signed dyadic witness of `ANF-169` is therefore the inner product between the current coefficient and a preceding interval sum of the same endpoint sequence.

Introduce the weighted endpoint mass

\[
A
:=
\sum_{m=1}^{K-1}w_m|b_m|^2
\tag{7}
\]

and the positive moving-window square function

\[
\boxed{
Q_H
:=
\sum_{m=H+1}^{K-1}
 w_m|B_H(m)|^2.
}
\tag{8}
\]

The diagonal ledger of `ANF-169` identifies (7) exactly:

\[
\boxed{
KA=\Delta_\sigma.
}
\tag{9}
\]

Cauchy--Schwarz applied to (6) now gives

\[
\boxed{
|S_H|^2\le A Q_H.
}
\tag{10}
\]

This is the basic bridge. A large signed dyadic correlation cannot occur unless the same endpoint sequence has substantial positive moving-window energy on that dyadic scale.

## 2. Macroscopic completion forces a quantitative positive square-function witness

Retain the bow regime

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac14,
\tag{11}
\]

and the target scale

\[
T_{\rm bow}:=XK\log X.
\tag{12}
\]

Suppose that along a sequence of `X` the endpoint completion is macroscopic:

\[
E_\partial\ge\delta T_{\rm bow}
\tag{13}
\]

for some fixed `delta>0`. `ANF-169` proves that for all sufficiently large `X` there are an endpoint `sigma` and a dyadic shell `H` such that, with

\[
L:=\log_2(2K),
\tag{14}
\]

one has

\[
\operatorname{Re}S_H^\sigma
\ge
\frac{\delta}{8L}X\log X.
\tag{15}
\]

In particular `|S_H^sigma|` obeys the same lower bound. Combining (10) and (15) yields the self-normalized necessary condition

\[
\boxed{
Q_H^\sigma
\ge
\frac{\delta^2}{64L^2}
\frac{X^2\log^2X}{A_\sigma}.
}
\tag{16}
\]

Equivalently, using (9),

\[
\boxed{
Q_H^\sigma
\ge
\frac{\delta^2}{64L^2}
\frac{KX^2\log^2X}{\Delta_\sigma}.
}
\tag{17}
\]

The formulation (16) is useful because it does not import any extra estimate on the endpoint coefficients: the amount of moving-window energy required is calibrated automatically against the actual weighted endpoint mass.

For the arithmetic source, the pointwise estimate already used in `ANF-157` and `ANF-169`, `|r_X(n)|\ll\log X`, gives

\[
A_\sigma\ll K\log^2X.
\tag{18}
\]

Since `L\asymp\log K\asymp\log X` in (11), (16) implies the coarser but concrete source-independent-in-form lower bound

\[
\boxed{
Q_H^\sigma
\gg_\delta
\frac{X^2}{K\log^2X}.
}
\tag{19}
\]

Thus target-sized completion cannot be supported solely by a delicate cancellation among many tiny moving blocks. At least one dyadic endpoint scale has a positive weighted second moment of twisted-residual block sums at the scale (19).

There is also a simple pointwise consequence. Because `sum_m w_m\le K`, (19) forces at least one later site `m` for which

\[
|B_H^\sigma(m)|
\gg_\delta
\frac{X}{K\log X}
=
X^{2\varepsilon+o(1)}(\log X)^{-1}.
\tag{20}
\]

Equation (20) is weaker than the square-function witness and should not replace it as the theorem target, but it makes the geometry tangible: a dangerous endpoint completion must generate a genuinely growing exact twisted-residual sum on some preceding dyadic block.

## 3. The actual source makes Q_H a positive twisted-residual short-interval energy

For the left endpoint, `ANF-169` has

\[
b_j^-
=
r_X(X+j)(X+j)^{-iU},
\qquad
r_X=\vartheta-Q_R.
\tag{21}
\]

Hence (5) becomes

\[
\boxed{
B_H^-(m)
=
\sum_{\substack{h\in\mathcal H_H\\ h<m}}
 r_X(X+m-h)(X+m-h)^{-iU}.
}
\tag{22}
\]

This is an exact twisted-residual sum over the interval of sites lying approximately between `H` and `2H` behind `X+m`. The right endpoint has the same form after the reversal already recorded in `ANF-169`. Consequently `Q_H^sigma` is a **positive moving-window second moment of exact short-interval sums of `(vartheta-Q_R)(n)n^{-iU}`**, with the triangular endpoint weight retained.

This representation changes the shape of the live arithmetic problem. The signed statistic in `ANF-169` expands into prime--prime, prime--Ramanujan, Ramanujan--prime, and Ramanujan--Ramanujan pieces, and estimating those four pieces independently behind absolute values risks discarding the cancellation built into the post-sieve residual. Equation (8) allows a different route: control the residual sum first and average its square over moving locations. Expanding the square remains available when useful, but it is no longer forced at the outset.

The exact distinguished multiplicative carrier is also preserved. No approximation of `n^{-iU}` by a linear, quadratic, or cubic phase occurs in (22), so the double-resonance warning of `ANF-159` is not bypassed by assumption. Any source theorem proved directly for `Q_H` would automatically be stated in the correct high-frequency gauge.

## 4. A positive square-function bound is sufficient to close the ANF-169 endpoint witness

The bridge also gives a clean sufficient theorem. Suppose that for both endpoints and every dyadic `H<K`, uniformly in the bow regime,

\[
\boxed{
A_\sigma Q_H^\sigma
=
o\!\left(
\frac{X^2\log^2X}{\log^2(2K)}
\right).
}
\tag{23}
\]

Then (10) gives

\[
|S_H^\sigma|
=
o\!\left(
\frac{X\log X}{\log(2K)}
\right)
\tag{24}
\]

uniformly over all endpoint/dyadic shells. The sufficient exclusion criterion of `ANF-169` then yields

\[
\boxed{
E_\partial=o(XK\log X).
}
\tag{25}
\]

Thus (23) is a positive square-function replacement for the signed dyadic correlation target. Under only the coarse pointwise mass bound (18), a stronger but simpler sufficient estimate is

\[
Q_H^\sigma
=o\!\left(
\frac{X^2}{K\log^2K}
\right)
\tag{26}
\]

uniformly in `sigma,H`; constants and harmless powers of `log X/log K` are interchangeable in the bow regime. The self-normalized form (23) is preferable because a sharper arithmetic estimate for `A_sigma` is automatically exploited rather than discarded.

This does not mean that generic all-interval discrepancy has suddenly become enough. `ANF-165` already obtains arbitrary fixed logarithmic savings above its admissible interval threshold, while `ANF-166`--`ANF-168` construct matched controls showing that coefficient-generic interval information can coexist with target-sized completion. The new object is useful precisely because it asks for a **source-faithful positive second moment across moving endpoint blocks**, not another uniform one-block bound detached from the actual amplitude law.

## 5. Prior-art boundary, stress tests, and next gate

The identities (6), (9), and (10) are elementary finite-sum consequences of the `ANF-169` ledger; no external theorem is load-bearing. A bounded prior-art audit found the expected neighboring literature on Selberg-integral/short-interval second moments and averaged shifted correlations of von Mangoldt-type sequences. Those are natural methodological neighbors, but they do not directly provide (23) for a fixed bow endpoint, the post-sieve residual `vartheta-Q_R`, the distinguished `U\asymp X^2` multiplicative twist, the triangular endpoint weight, and the full range of dyadic `H` that may carry the witness. `SOURCES.md` therefore requires no new anchor for this finding.

The implication must not be overstated. Large `Q_H` is necessary for the particular dangerous shell extracted from macroscopic completion, but large `Q_H` alone does not force positive `S_H`: the current coefficient may remain nearly orthogonal to its preceding moving sum. Conversely, (23) is sufficient because it controls every shell through Cauchy--Schwarz, not because the square function is exactly equal to endpoint completion.

Matched charge-and-hold controls are consistent with the result rather than counterexamples to it. If they realize the positive shell demanded by `ANF-169`, (10) says they must also pay the corresponding moving-window energy. The new discrimination problem is whether the *fixed* prime-minus-Ramanujan amplitude law permits that payment at the quantitative level (16), not whether arbitrary coefficient sequences can do so.

The next useful source theorem is therefore: bound the positive quantity `Q_H^sigma` sharply enough to establish (23), preferably by exploiting the exact prime/rough residual before taking absolute values. A direct short-interval second-moment argument, a large-sieve formulation adapted to the multiplicative carrier, or a Type-I/II decomposition that keeps the Cramer--Granville subtraction coupled are all structurally relevant routes. Any such estimate must be checked against the actual admissible dyadic range rather than inferred from generic long-interval logarithmic cancellation.

The main architectural gain is that the endpoint frontier now has a positive target. `ANF-169` says dangerous completion leaves a signed dyadic bilinear witness; `ANF-170` says that witness necessarily leaves a **positive moving-window twisted-residual energy witness**. The remaining problem is arithmetic size, not representation.
