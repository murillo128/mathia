# PC-011 — common-vertex chord correlations are Dedekind/Vasyunin sums

**Status:** `DECISIVE-NEGATIVE` for the branch based on first/second angular correlations of the common-vertex chord fan.

## Exact geometry

Fix the regular \(q\)-gon

\[
P_q=\{\zeta_q^k=e^{2\pi i k/q}:0\le k<q\}
\]

with common vertex \(1\). For \(1\le k\le q-1\), let \(L_k\) be the Euclidean line through \(1\) and \(\zeta_q^k\).

Write

\[
\theta_k=\frac{\pi k}{q}.
\]

The two endpoints of the chord have arguments \(0\) and \(2\theta_k\), so the supporting line has equation

\[
\boxed{x\cos\theta_k+y\sin\theta_k=\cos\theta_k.}
\]

Hence its intercept with the vertical diameter \(x=0\) is

\[
\boxed{y_k=\cot\frac{\pi k}{q}.}
\]

Thus cotangent sums have a literal interpretation in the original prime-circle drawing: they are statistics of the intercepts/directions of the chords issued from the common vertex.

## Multiplicative relabelling gives Dedekind sums exactly

For \(h\in(\mathbb Z/q\mathbb Z)^\times\), multiplication by \(h\) permutes the nonzero vertex labels

\[
k\mapsto hk\pmod q.
\]

The correlation between the two chord-intercept fields is therefore

\[
C(h,q)
=
\sum_{k=1}^{q-1}
\cot\frac{\pi k}{q}
\cot\frac{\pi hk}{q}.
\]

The classical cotangent formula for the Dedekind sum is

\[
s(h,q)
=
\frac1{4q}
\sum_{k=1}^{q-1}
\cot\frac{\pi k}{q}
\cot\frac{\pi hk}{q}.
\]

Consequently,

\[
\boxed{C(h,q)=4q\,s(h,q).}
\]

So a very natural attempt to retain information beyond the crossing count of PC-009 — namely, correlate the actual chord directions under the modular permutation induced by another level/multiplier — lands exactly on a classical Dedekind sum.

## First angular moment gives the RH-related cotangent sums

A second natural statistic couples the angular rank \(m/q\) to the chord intercept after multiplicative relabelling:

\[
A(h,q)
:=
-\sum_{m=1}^{q-1}
\frac mq
\cot\left(\frac{\pi mh}{q}\right).
\]

This is exactly the standard cotangent sum

\[
\boxed{A(h,q)=c_0(h/q).}
\]

The equivalent Vasyunin sums use the fractional-part coordinate produced by the modular permutation,

\[
V(h/q)
=
\sum_{m=1}^{q-1}
\left\{\frac{mh}{q}\right\}
\cot\left(\frac{\pi mh}{q}\right),
\]

and are related to \(c_0\) by modular inversion of \(h\).

These cotangent/Vasyunin sums are already a well-developed part of the Nyman–Beurling/Báez-Duarte approach to the Riemann hypothesis and are tied to the Estermann zeta function and period functions.

## Decisive negative conclusion

The branch

\[
\boxed{
\text{common-vertex chord directions/intercepts}
+\text{multiplicative vertex permutation}
\to
\text{pair correlations or first angular moments}
}
\]

is not a new RH mechanism. Its most natural observables are exactly classical Dedekind and Vasyunin/cotangent sums, whose RH connections are already extensively studied.

This rules out, as novelty claims, constructions based only on:

- signed chord slopes/intercepts;
- quadratic correlations of those slopes under \(k\mapsto hk\);
- first moments against the angular rank or its fractional-part permutation;
- equivalent cotangent statistics obtained by changing axes or orientation.

## What survives

The reduction does **not** capture the full embedded arrangement. Potentially new information can still live in quantities that are not functions only of the one-dimensional chord intercept field, for example:

- the actual two-dimensional crossing locations between different polygon edges/fans;
- crossing radii and their joint distribution with birth levels;
- higher-order concurrency of three or more levels;
- nonlinear invariants of the whole embedded arrangement;
- off-circle interior/exterior harmonic fields.

Those observables retain geometric data discarded both by the Bost–Connes abstraction of PC-010 and by the Dedekind/cotangent reduction here.

## Literature / novelty check

The cotangent formula

\[
s(h,q)=\frac1{4q}\sum_{k=1}^{q-1}\cot(\pi k/q)\cot(\pi hk/q)
\]

is classical. The sums \(c_0(h/q)\) and the equivalent Vasyunin sums are extensively studied because of their relation to the Estermann zeta function and the Nyman–Beurling criterion for RH. See, among others:

- S. Bettin and B. Conrey, *Period functions and cotangent sums*, Algebra & Number Theory 7 (2013).
- H. Maier and M. T. Rassias, works on cotangent sums related to the Riemann hypothesis.
- surveys on cotangent sums associated with the Nyman–Beurling criterion.

The elementary identification \(y_k=\cot(\pi k/q)\) gives a direct prime-circle geometric reading of these sums, but the resulting arithmetic objects and their RH connection are classical. The result is therefore recorded as a branch-closing negative, not as a novelty claim.
