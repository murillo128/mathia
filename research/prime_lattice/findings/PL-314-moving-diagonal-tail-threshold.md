# PL-314 — The moving Green atom makes weighted `L^1` matching insufficient; `Qm(Q) -> 0` restores rank-one transfer

**Evidence:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + POSITIVE-TAIL-CRITERION`

**Status:** `EXACT-SUFFICIENT-TAIL + SMOOTH-L1-COUNTEREXAMPLE + ACTUAL-BRANCH-TAIL-CONTROL-OPEN`

## Precise claim

`PL-313` proves the corner-to-outer rank-one transfer for compactly supported physical mismatches and identifies the candidate extension weight

\[
Q=-\log\frac{1-y}{2},
\qquad
\frac{dy}{1-y}=dQ.
\]

It explicitly leaves open whether weighted integrability of a genuine mismatch reaching the endpoint is enough. It is not.

Fix `r>0`, let

\[
x_s(r)=1-2e^{-r/s},
\]

and write the logarithmic-distance mismatch as a function `m:(0,\infty)\to\mathbb C`, so that its physical representative is

\[
\widetilde m(y)=m\!\left(-\log\frac{1-y}{2}\right).
\]

Define the rank-one-scaled Green transfer

\[
\mathcal A_s[m](r)
:=\frac1s\int_{-1}^{1}G_s(x_s(r),y)\widetilde m(y)\,dy.
\tag{PL314-1}
\]

Then the following two statements hold.

**Sufficient tail criterion.** If

\[
m\in L^1(0,\infty),
\qquad
\boxed{Qm(Q)\longrightarrow0\quad(Q\to\infty),}
\tag{PL314-2}
\]

then

\[
\boxed{
\mathcal A_s[m](r)
\longrightarrow
 e^{-r}\int_0^\infty m(Q)\,dQ.
}
\tag{PL314-3}
\]

Thus the compact-support theorem of `PL-313` extends to a natural endpoint-decay class.

**Weighted `L^1` alone is insufficient.** For every fixed `r>0` there exists a nonnegative `m\in C^\infty(0,\infty)\cap L^1(0,\infty)` with

\[
m(Q)\to0,
\qquad
\int_0^\infty m(Q)\,dQ<\infty,
\tag{PL314-4}
\]

such that (PL314-3) fails. The physical function `\widetilde m` is smooth in `(-1,1)`, extends continuously by zero at `y=1`, and satisfies the exact weighted condition

\[
\int_{-1}^{1}\frac{|\widetilde m(y)|}{1-y}\,dy
=\int_0^\infty |m(Q)|\,dQ<\infty.
\tag{PL314-5}
\]

The obstruction is the diagonal atom of the stretched Green limit from `PL-310`. A sparse tail can place bumps at the moving locations

\[
Q_s=\frac rs,
\tag{PL314-6}
\]

with height `Theta(s)`. Their weighted `L^1` mass can be arbitrarily small, while after the `1/s` normalization in (PL314-1) each selected bump still contributes `Theta(1)` through the Green atom. Condition (PL314-2) excludes exactly this pointwise scale because it forces `m(r/s)=o(s)`.

No necessity claim is made for (PL314-2); weaker averaged anti-concentration conditions may suffice. The durable conclusion is that **matching the leading `Q^{-1/2}` outer coefficient strongly enough to obtain only an `L^1(dQ)` residual does not yet justify the `PL-313` rank-one law.** The residual must also be prevented from concentrating along the moving Green diagonal, or controlled by an equivalent source-structured estimate.

## 1. Rewriting the transfer with the stretched Green measure

Let `\mu_{s,r}` be the positive Green measure from `PL-310`,

\[
d\mu_{s,r}(q)
=k_s(r,q)\,dq
:=G_s(x_s(r),x_s(q))\frac{2}{s}e^{-q/s}\,dq.
\tag{PL314-7}
\]

Since

\[
y=x_s(q)=1-2e^{-q/s}
\quad\Longleftrightarrow\quad
Q=\frac qs,
\]

(PL314-1) is exactly

\[
\boxed{
\mathcal A_s[m](r)
=\frac1s\int_0^\infty m(q/s)\,d\mu_{s,r}(q)
=\int_0^\infty k_s(r,sQ)m(Q)\,dQ.
}
\tag{PL314-8}
\]

`PL-310` proves the weak limit

\[
\mu_{s,r}\Longrightarrow
\mu_r
=e^{-r-q}\mathbf1_{0<q<r}\,dq
+e^{-2r}\delta_r.
\tag{PL314-9}
\]

For each fixed `Q`, the physical point `q=sQ` lies in the compressed corner and `PL-313` gives

\[
\boxed{k_s(r,sQ)\longrightarrow e^{-r}.}
\tag{PL314-10}
\]

The issue is that the test function in the first representation of (PL314-8), `s^{-1}m(q/s)`, depends on `s`. Weak convergence of `\mu_{s,r}` therefore does not permit replacing it by the limiting measure without tail control; the atom at `q=r` samples precisely `m(r/s)/s`.

## 2. Exact pre-diagonal domination

The classical interval Green formula used in `PL-309`--`PL-313` yields a useful uniform bound before the moving diagonal. Put

\[
t=e^{-r/s},\qquad u=e^{-q/s},\qquad 0<q<r.
\]

Bucur's formula gives

\[
k_s(r,q)
=\frac{u(u-t)^{2s-1}}{s\Gamma(s)^2}
\int_0^{R}\frac{z^{s-1}}{\sqrt{1+z}}\,dz,
\]

with

\[
R=\frac{4tu(1-t)(1-u)}{(u-t)^2}.
\tag{PL314-11}
\]

Using

\[
\int_0^R\frac{z^{s-1}}{\sqrt{1+z}}\,dz
\le\frac{R^s}{s}
\]

and `\Gamma(1+s)=s\Gamma(s)` gives the exact estimate

\[
\boxed{
 k_s(r,q)
\le
\frac{4^s e^{-r-q}(1-t)^s(1-u)^s}
{\Gamma(1+s)^2\bigl(1-e^{-(r-q)/s}\bigr)}.
}
\tag{PL314-12}
\]

Hence for fixed `r>0`, all sufficiently small `s`, and `0<q\le r/2`,

\[
\boxed{k_s(r,q)\le C_r e^{-r-q}\le C_r e^{-r}.}
\tag{PL314-13}
\]

This is the domination needed in the compressed physical corner; it does not cross the moving diagonal `q=r`.

## 3. Proof of the sufficient tail criterion

Split (PL314-8) at `Q=r/(2s)`:

\[
\mathcal A_s=A_s^{\rm pre}+A_s^{\rm tail}.
\]

For the pre-diagonal part, (PL314-13) gives

\[
|k_s(r,sQ)m(Q)|\le C_r e^{-r}|m(Q)|,
\]

while (PL314-10) gives pointwise convergence to `e^{-r}m(Q)`. Since `m\in L^1`, dominated convergence yields

\[
A_s^{\rm pre}\longrightarrow e^{-r}\int_0^\infty m(Q)\,dQ.
\tag{PL314-14}
\]

For the tail define

\[
\omega(R):=\sup_{Q\ge R}Q|m(Q)|.
\]

Condition (PL314-2) is exactly `\omega(R)\to0`. Returning to the `q` representation,

\[
|A_s^{\rm tail}|
\le
\frac1s\int_{q\ge r/2}|m(q/s)|\,d\mu_{s,r}(q)
\le
\frac{2}{r}\,\omega\!\left(\frac{r}{2s}\right)
\mu_{s,r}((0,\infty)).
\tag{PL314-15}
\]

The total Green mass is explicit from `PL-310`,

\[
\mu_{s,r}((0,\infty))
=
\frac{\sqrt\pi}{2^{2s}\Gamma(1+s)\Gamma(s+1/2)}
(1-x_s(r)^2)^s
\longrightarrow e^{-r},
\tag{PL314-16}
\]

so it is uniformly bounded. Equation (PL314-15) tends to zero, proving (PL314-3).

The proof isolates the two mechanisms cleanly. Ordinary `L^1(dQ)` controls the entire pre-diagonal corner because the kernel is uniformly bounded there. The only extra requirement is suppression of the part whose stretched coordinate reaches the moving diagonal and the post-diagonal region.

## 4. Smooth `L^1` counterexample

The failure of bare `L^1` can be proved without guessing the microscopic width of the Green atom.

Choose `\chi\in C_c^\infty((-1,1))` with

\[
0\le\chi\le1,
\qquad
\chi=1\text{ on }[-1/2,1/2].
\]

Choose numbers `\delta_n>0` with `\delta_n<r/4` and summable total as small as desired. By the weak convergence (PL314-9) and the Portmanteau theorem, for every fixed `\delta_n`,

\[
\liminf_{s\downarrow0}
\mu_{s,r}\bigl((r-\delta_n/2,r+\delta_n/2)\bigr)
\ge e^{-2r}.
\tag{PL314-17}
\]

Recursively choose `s_n\downarrow0` so fast that

\[
\mu_{s_n,r}\bigl((r-\delta_n/2,r+\delta_n/2)\bigr)
\ge\frac34e^{-2r},
\tag{PL314-18}
\]

and the intervals

\[
J_n=
\left(
\frac{r-\delta_n}{s_n},
\frac{r+\delta_n}{s_n}
\right)
\tag{PL314-19}
\]

are pairwise disjoint and escape to infinity. This is possible because after meeting (PL314-18), `s_n` may be decreased further.

Define the fixed, `s`-independent function

\[
\boxed{
 m(Q)=\sum_{n\ge1}
 s_n\,\chi\!\left(\frac{s_nQ-r}{\delta_n}\right).
}
\tag{PL314-20}
\]

The supports are disjoint and locally finite, so `m\in C^\infty(0,\infty)`, `m\ge0`, and `m(Q)\to0`. Moreover,

\[
\int_0^\infty m(Q)\,dQ
=
\left(\int_{-1}^{1}\chi(z)\,dz\right)
\sum_{n\ge1}\delta_n,
\tag{PL314-21}
\]

which is finite and can be made arbitrarily small.

At `s=s_n`, the `n`-th bump satisfies

\[
m(q/s_n)\ge s_n
\qquad
\text{for }|q-r|<\delta_n/2.
\]

Positivity of the Green measure and (PL314-18) therefore give

\[
\boxed{
\mathcal A_{s_n}[m](r)
\ge
\mu_{s_n,r}\bigl((r-\delta_n/2,r+\delta_n/2)\bigr)
\ge\frac34e^{-2r}.
}
\tag{PL314-22}
\]

Choose the summable `\delta_n` so that the rank-one candidate obeys

\[
e^{-r}\int_0^\infty m(Q)\,dQ<\frac14e^{-2r}.
\tag{PL314-23}
\]

Then (PL314-22) and (PL314-23) contradict (PL314-3). The same construction also records the natural diagonal threshold:

\[
Q_n:=\frac r{s_n},
\qquad
Q_nm(Q_n)=r,
\tag{PL314-24}
\]

so the counterexample violates (PL314-2) exactly at the sparse points that the moving atom sees.

No shrinking-neighborhood limit has been assumed in this construction. Each `\delta_n` is fixed first; weak convergence is then used to choose a sufficiently small `s_n`. This avoids any unjustified inference from the fixed-neighborhood weak limit to a prescribed `s`-dependent atom width.

## 5. Consequence for completed-Weil matching

`PL-313` showed that if the actual completed-Weil branch can be decomposed into the singular outer profile plus a physical mismatch whose weighted moment

\[
\int\frac{m(y)}{1-y}\,dy
\]

is meaningful, then that moment is the candidate scalar entering the regular outer solvability condition. The present result sharpens the hypothesis needed for such a theorem.

In the logarithmic coordinate, merely proving

\[
m\in L^1(dQ)
\]

does **not** justify replacing the finite-`s` Green transfer by its rank-one limit. A sparse residual with total weighted mass as small as desired can still be sampled at `Q\asymp1/s` by the moving diagonal and produce an order-one error after the matching normalization.

A clean sufficient target is

\[
\boxed{m\in L^1(dQ)\quad\text{and}\quad Qm(Q)\to0,}
\tag{PL314-25}
\]

or a source-structured averaged condition strong enough to imply the same diagonal suppression. In physical distance `\delta=1-y=2e^{-Q}`, the pointwise condition is

\[
\left|\log\frac{\delta}{2}\right|\,\widetilde m(1-\delta)\longrightarrow0.
\tag{PL314-26}
\]

This is stronger than equality of the leading `Q^{-1/2}` boundary coefficient plus weighted `L^1` integrability, but it is compatible with a next asymptotic term such as `O(Q^{-1-\varepsilon})` or `O(Q^{-3/2})`.

The condition is not claimed necessary. The actual eigen-equation could forbid sparse diagonal spikes through monotonicity, BV, a quantitative boundary expansion, or another compactness property. What `PL-314` rules out is the shortcut from **weighted integrability alone** to the rank-one matching law.

## Prior-art and novelty audit

The interval Green kernel is classical and already ledgered as source `102` (Bucur 2016). `PL-310` supplies the load-bearing weak Green-measure limit with its diagonal atom, and `PL-313` supplies the compact-support corner transfer. The proof above combines those persisted results with an exact kernel bound and a diagonal bump construction; it introduces no additional external theorem beyond the standard Portmanteau theorem.

A targeted literature audit around small-order fractional-Laplacian Green kernels, logarithmic-Laplacian limits, boundary decay, and small-order boundary asymptotics recovered the established small-order spectral/eigenfunction theory and classical Green-function estimates, but no direct theorem for this particular `Q=q/s` moving-test-function limit or the tail threshold (PL314-2). Search absence is not treated as evidence of broad novelty. The durable claim is the line-local exact distinction: `L^1(dQ)` is insufficient, while `L^1(dQ)` plus `Qm(Q)->0` is sufficient for the rank-one transfer at each fixed outer `r>0`.

## Adversarial controls and limits

- **The counterexample is a single fixed mismatch.** The function (PL314-20) is built once after selecting the sequence `s_n`; it is not changed separately at each `s`.
- **The mismatch is genuinely weighted-integrable at the physical endpoint.** Equation (PL314-5) is exactly the weight suggested by `PL-313`, not a weaker bulk norm.
- **Weak convergence is used only with fixed neighborhoods.** The sequence `s_n` is selected after each fixed `\delta_n`, so no rate of concentration of the diagonal atom is smuggled into the proof.
- **The positive theorem crosses no diagonal estimate.** Domination is used only for `q\le r/2`; the remaining region is killed by (PL314-2) and the bounded total Green mass.
- **No arithmetic sign is obtained.** The threshold is universal fractional Green geometry. Rational-prime specificity can enter only through a theorem showing that the actual completed-Weil mismatch satisfies a stronger tail law or through the later scalar compatibility/sign calculation.
- **No necessity of `Qm(Q)->0` is claimed.** Oscillatory or averaged tails may pass the transfer without pointwise decay at this rate.

## Verdict

**Exact obstruction plus a usable sufficient replacement.** The endpoint matching gate left by `PL-313` is stricter than weighted `L^1`: the moving Green atom can detect sparse `O(s)` bumps at `Q=r/s` that carry negligible total weighted mass. The simple condition `Qm(Q)->0` removes that mechanism and, together with `L^1(dQ)`, gives the desired rank-one transfer.

The next branch-specific theorem should therefore target a quantitative remainder estimate or anti-concentration property for the actual completed-Weil boundary mismatch, not merely prove existence of the weighted moment. Once that stronger control is available, the scalar corner/source balance from `PL-313` can be invoked without an unexamined moving-diagonal defect.