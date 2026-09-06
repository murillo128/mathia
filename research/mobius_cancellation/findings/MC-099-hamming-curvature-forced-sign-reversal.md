# MC-099 — The source Hamming deformation has a forced large curvature sign reversal

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let the source-forced Hamming deformation from `MC-092`--`MC-093` be

\[
\mathcal Q_N(t)
=\sum_{m,n\le N}
\mu(m)^2\mu(n)^2(-t)^{d_\triangle(m,n)}
 z\!\left(\frac{N^2}{mn}\right),
\qquad 0\le t\le1,
\tag{1}
\]

and equivalently write its radial expansion as

\[
\mathcal Q_N(t)=\sum_{k=0}^{D_N}(-t)^k C_{k,N},
\qquad
D_N=O\!\left(\frac{\log N}{\log\log N}\right).
\tag{2}
\]

`MC-097` and `MC-098` show that the complete degree-two shell has a positive main term

\[
C_{2,N}\sim c_2\frac{N^2}{(\log N)^2},
\qquad c_2>0,
\tag{3}
\]

while the signed higher-degree tail cancels it at the endpoint. Those facts force a stronger geometric statement about the **whole interpolation path**: its curvature cannot remain nonnegative, or even merely small on the negative side.

There is an absolute constant `c>0` such that, for every sufficiently large `N`, some

\[
t_N\in(0,1)
\]

satisfies

\[
\boxed{
\mathcal Q_N''(t_N)
\le
-c\frac{N^2}{D_N^3(\log N)^4}.
}
\tag{4}
\]

Hence, using `(2)`,

\[
\boxed{
\mathcal Q_N''(t_N)
\le
-c'\frac{N^2(\log\log N)^3}{(\log N)^7}
}
\tag{5}
\]

for some `c'>0` and all sufficiently large `N`.

At the opposite endpoint of the deformation parameter,

\[
\boxed{
\mathcal Q_N''(0)=2C_{2,N}
\sim 2c_2\frac{N^2}{(\log N)^2}>0.
}
\tag{6}
\]

Thus `mathcal Q_N''` changes sign on `[0,1]`, and the negative curvature is still of almost-full-square polynomial scale: only polylogarithmic factors separate `(4)` from `N^2`.

This gives a concrete source-natural **signed cross-degree carrier** of the cancellation isolated abstractly in `MC-098`:

\[
\boxed{
\mathcal Q_N''(t)
=
\sum_{k\ge2}k(k-1)(-1)^k t^{k-2}C_{k,N}.
}
\tag{7}
\]

The carrier is not positive. In particular, a proposed Hamming/noise route cannot obtain the missing Mertens gain from convexity, nonnegative curvature, or a positive degreewise energy along this interpolation. Any useful recurrence based on the deformation must preserve the signed curvature interaction, control where it occurs uniformly in scale, or use a different source coupling.

No improved estimate for `M(x)` is claimed.

## 1. Endpoint Taylor remainder is exactly the signed degree-two-and-higher coupling

Taylor's formula with integral remainder gives the exact finite-polynomial identity

\[
\mathcal Q_N(1)
=\mathcal Q_N(0)+\mathcal Q_N'(0)
+\int_0^1(1-t)\mathcal Q_N''(t)\,dt.
\tag{8}
\]

From `(2)`,

\[
\mathcal Q_N(0)=C_{0,N},
\qquad
\mathcal Q_N'(0)=-C_{1,N},
\tag{9}
\]

so

\[
\boxed{
\int_0^1(1-t)\mathcal Q_N''(t)\,dt
=
\mathcal Q_N(1)-C_{0,N}+C_{1,N}
=
\sum_{k\ge2}(-1)^kC_{k,N}.
}
\tag{10}
\]

The last equality can also be checked coefficientwise, since

\[
\int_0^1(1-t)k(k-1)t^{k-2}\,dt=1
\qquad(k\ge2).
\tag{11}
\]

Therefore `(10)` is not an externally chosen smoothing kernel: the weight `1-t` is exactly the Taylor remainder that recombines every radial degree with its Möbius parity sign.

`MC-098` supplies the unconditional endpoint estimate, derived from the Korobov--Vinogradov Mertens bound `MC-S3` and the Huxley--Watt identity `MC-S24`,

\[
\mathcal Q_N(1)
=O_A\!\left(\frac{N^2}{(\log N)^A}\right)
\quad\text{for every fixed }A>0,
\tag{12}
\]

and also

\[
C_{0,N}=O(N),
\qquad
C_{1,N}=O(N\log\log N).
\tag{13}
\]

Consequently the total signed curvature integral in `(10)` is smaller than `N^2/(\log N)^A` for arbitrarily large fixed `A`, apart from the still smaller low-degree terms.

## 2. The curvature starts macroscopically positive

Differentiating `(2)` twice and evaluating at zero leaves only degree two:

\[
\mathcal Q_N''(0)=2C_{2,N}.
\tag{14}
\]

By `MC-097`, for all sufficiently large `N`,

\[
A_N:=\mathcal Q_N''(0)
\ge
c_2\frac{N^2}{(\log N)^2}.
\tag{15}
\]

So the cancellation in `(10)` cannot come from the curvature being uniformly tiny. It begins with a definite positive almost-square-scale value.

## 3. The source degree bounds how quickly the curvature can escape

The pair-level representation `(1)` gives a direct derivative bound without taking absolute values shell by shell. Let

\[
D_N:=\deg \mathcal Q_N.
\]

For `0\le t\le1`, every nonzero third derivative term has magnitude at most

\[
d_\triangle(m,n)
(d_\triangle(m,n)-1)
(d_\triangle(m,n)-2)
|z(N^2/(mn))|
\le \frac12D_N^3,
\]

because `|z|\le1/2`. There are at most `N^2` ordered pairs, hence

\[
\boxed{
\sup_{0\le t\le1}|\mathcal Q_N'''(t)|
\le B_N:=\frac12N^2D_N^3.
}
\tag{16}
\]

Set

\[
\delta_N:=\frac{A_N}{2B_N}
=\frac{A_N}{N^2D_N^3}.
\tag{17}
\]

For large `N`, `delta_N<1/2`. The mean-value bound from `(16)` shows that throughout `0\le t\le\delta_N`,

\[
\mathcal Q_N''(t)
\ge A_N-B_N\delta_N
=\frac{A_N}{2}.
\tag{18}
\]

Thus the positive contribution to the exact signed integral `(10)` from this initial interval is at least

\[
P_N
:=\int_0^{\delta_N}(1-t)\mathcal Q_N''(t)\,dt
\ge
\frac{A_N\delta_N}{4}
=
\frac{A_N^2}{4N^2D_N^3}.
\tag{19}
\]

Using `(15)`,

\[
\boxed{
P_N
\ge
\frac{c_2^2}{4}
\frac{N^2}{D_N^3(\log N)^4}.
}
\tag{20}
\]

The sublogarithmic degree bound of `MC-093` therefore gives

\[
P_N
\gg
\frac{N^2(\log\log N)^3}{(\log N)^7}.
\tag{21}
\]

## 4. The remaining interval must contain comparably large negative curvature

Let

\[
I_N:=\int_0^1(1-t)\mathcal Q_N''(t)\,dt.
\]

Taking, for example, `A=9` in `(12)` and using `(13)` shows

\[
I_N=o(P_N).
\tag{22}
\]

Hence for all sufficiently large `N`,

\[
\int_{\delta_N}^1(1-t)\mathcal Q_N''(t)\,dt
=I_N-P_N
\le-\frac{P_N}{2}.
\tag{23}
\]

Since

\[
\int_{\delta_N}^1(1-t)\,dt
=\frac{(1-\delta_N)^2}{2}
\le\frac12,
\tag{24}
\]

there must be a point `t_N in [delta_N,1]` for which

\[
\mathcal Q_N''(t_N)\le-P_N.
\tag{25}
\]

Combining `(20)` and `(25)` proves `(4)`, and `(2)` then gives `(5)`. Continuity together with `(6)` also proves an actual curvature sign change before `t_N`.

The argument uses no RH-strength estimate. The smallness of the total integral comes only from the classical unconditional zero-free-region bound already used in `MC-098`.

## 5. What the sign reversal does and does not rule out

The result closes a specific tempting escape from the radial-shell obstruction. After `MC-097`--`MC-098`, one might hope that the large positive degree-two shell is compensated gradually while the one-parameter deformation remains governed by a positive convexity or energy principle. Equations `(4)`--`(6)` rule that out: the exact source polynomial must enter a region of large **negative** curvature.

This does not show that the Hamming deformation itself is useless. Equation `(7)` is precisely a signed cross-degree observable of the type left alive by `MC-098`, and the proof shows that it carries substantial deterministic structure. What remains unavailable is an independently cheaper theorem controlling that signed observable in the direction needed for a strict Mertens contraction.

The location `t_N` is also not controlled uniformly. It may move with `N`, and `(17)` only supplies a tiny initial interval on which positivity is forced. Therefore a per-scale negative-curvature witness is not an iterable recurrence. Any future use of `(7)` must additionally control comparator turnover/location across scales or integrate the signed curvature in a way that does not simply reconstruct the endpoint identity `(10)`.

Finally, the theorem is specific to the source Hamming deformation. It does not assert sign reversal for an arbitrary noise operator, altered sawtooth kernel, truncated deformation, or random multiplicative comparator.

## 6. Prior art and novelty boundary

The finite Huxley--Watt Mertens identity is classical (`MC-S24`). The sublogarithmic degree estimate is already established in `MC-093`, while the degree-two asymptotic and forced higher-degree cancellation are the canonical Mathia results `MC-097` and `MC-098`. The remaining ingredients here are elementary Taylor's theorem and the derivative bound obtained directly from the finite source sum.

A targeted literature search for Huxley--Watt/Mertens identities combined with Hamming, Walsh/noise, radial-degree, or curvature formulations did not identify an established theorem matching `(4)`. That search outcome is not evidence of novelty, and **no novelty claim is made**. The durable contribution is the exact consequence for this already-defined source deformation: the cross-degree cancellation known at the endpoint necessarily appears as a large curvature sign reversal along the interpolation path.

## Consequence for the research line

The radial branch is now narrower than the statement "keep signs until the end." Its simplest source-natural signed carrier, `mathcal Q_N''(t)`, is forced to change sign at almost-full-square scale. Positive shell norms lose the cancellation (`MC-097`--`MC-098`), while positive curvature along the Hamming path is impossible by `(4)`--`(6)`.

A surviving deformation mechanism must therefore control a **signed, scale-coherent cross-degree quantity** without replacing it by an absolute norm and without using the endpoint itself as input. The main unresolved burden is no longer existence of cross-degree cancellation; it is obtaining an independent uniform estimate or recurrence for that cancellation with a strict power gain.