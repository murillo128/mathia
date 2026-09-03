# ANF-008 — every improving n-point bridge certificate saturates the block cap

**Status:** `EXACT-DERIVED + FORMAL-SOURCE-BRIDGE + STRUCTURAL-REDUCTION`. In the parametric `n_point_bound` theorem underlying `ANF-006` and `ANF-007`, once a local finite certificate `(n,c,p)` is fixed, the block size `m` is not an independent optimization variable on the improving branch. If any admissible `m` beats the Montgomery--Taylor baseline, the resulting bound is strictly increasing in `m`, so the optimal integer choice is forced to be the largest one permitted by the bridge cap. This gives an exact scalar admission test for every local certificate before any further block tuning is attempted.

## 1. The parametric bridge

Write

\[
H=\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
=0.6725007036794116\ldots
\]

for the Montgomery--Taylor/Anthropic baseline, and put

\[
r:=n-1\ge1.
\]

The formally proved `n_point_bound` bridge in the frozen `teal-sea/zeta-lab` artifact uses

\[
\Phi_n(c,m,p)
=
\frac{H-r(m-1)/(pm)}
     {1-c(m-r)/m},
\tag{1}
\]

under

\[
n\le m,\qquad p>0,\qquad c>0,
\qquad c(m-r)\le1,
\tag{2}
\]

plus the finite local certificate `c <= F n p g` for every nonnegative gap vector. The same source already records from (2) that

\[
m\le r+\left\lfloor\frac1c\right\rfloor.
\tag{3}
\]

The point here is to determine what freedom in `m` remains after the local certificate has been established.

Because `m>=r+1`, the cap in (2) implies `c<=1`. Also

\[
m-c(m-r)\ge m-1>0,
\tag{4}
\]

so all comparisons below have a positive denominator.

## 2. Exact improvement criterion at a fixed block size

Subtracting `H` from (1) and multiplying numerator and denominator by `m` gives

\[
\boxed{
\Phi_n(c,m,p)-H
=
\frac{cH(m-r)-r(m-1)/p}
     {m-c(m-r)}.
}
\tag{5}
\]

Hence an admissible block size improves the baseline if and only if

\[
\boxed{
pcH>
 r\,\frac{m-1}{m-r}.
}
\tag{6}
\]

Since

\[
\frac{m-1}{m-r}
=1+\frac{r-1}{m-r},
\]

any improvement necessarily implies

\[
\boxed{pcH>r=n-1.}
\tag{7}
\]

For `n=2`, (6) reduces to `pcH>1`, exactly the improvement condition isolated in `ANF-007`. There the overlap-kernel zero gives the stronger obstruction `pcH<1`, killing the entire two-point branch.

## 3. If improvement is possible, larger admissible blocks are always better

Treat `m` temporarily as a real variable on the interval allowed by (2). Differentiating (1) gives the exact identity

\[
\boxed{
\frac{d}{dm}\Phi_n(c,m,p)
=
\frac{r}{p}
\frac{pcH-1-c(r-1)}
     {\bigl(m-c(m-r)\bigr)^2}.
}
\tag{8}
\]

Suppose some admissible integer `m` improves `H`. By (7), `pcH>r`. Since `0<c<=1`,

\[
1+c(r-1)\le r.
\tag{9}
\]

Therefore

\[
pcH>1+c(r-1),
\]

and (8) is strictly positive throughout the whole admissible interval. Thus:

\[
\boxed{
\text{if one admissible block improves }H,
\text{ then }\Phi_n\text{ is strictly increasing in }m.
}
\tag{10}
\]

This is stronger than saying that the examples happened to choose large blocks. It removes `m` as a genuine optimization coordinate on the only branch of interest.

## 4. The optimal block and an exact admission gate

The largest admissible integer is

\[
\boxed{
m_{\max}=r+\left\lfloor\frac1c\right\rfloor.}
\tag{11}
\]

By (10), a fixed local certificate `(n,c,p)` admits **some** improving block if and only if the cap-saturating integer block improves. Combining (6) and (11) gives the exact discrete test

\[
\boxed{
\exists\,m\text{ admissible with }\Phi_n>H
\iff
pcH>
 r\,\frac{m_{\max}-1}{m_{\max}-r}.
}
\tag{12}
\]

When (12) holds, `m=m_max` is the unique optimal integer block size.

There is also a useful continuous upper envelope. Saturating the cap continuously at

\[
m_*=r+\frac1c
\]

gives

\[
\Phi_*(n,c,p)
=
H\frac{1+rc}{1+(r-1)c}-\frac rp,
\tag{13}
\]

and hence, on the improving branch,

\[
\Phi_n(c,m,p)-H
\le
\boxed{
\frac{Hc}{1+(r-1)c}-\frac rp.
}
\tag{14}
\]

A necessary condition for any integer improvement is therefore

\[
\boxed{
pcH>r\bigl(1+(r-1)c\bigr).}
\tag{15}
\]

The exact discrete gate (12) is slightly sharper because it keeps the floor in (11).

## 5. The published/frozen instances already sit exactly at this forced boundary

The source parameters used in the current evidence chain all choose precisely the `m_max` dictated by (11):

- the unconditional three-point certificate has `c=1345/10^6`, `r=2`, hence `m_max=745`, exactly the theorem's `m=745`;
- the unconditional four-point certificate has `c=2310/10^6`, `r=3`, hence `m_max=435`, exactly `m=435`;
- Ainta's seven-point certificate has `c=19/5000`, `r=6`, hence `m_max=269`, exactly `m=269`;
- the zeta-lab seven-point laboratory certificate has `c=34697/10^7`, `r=6`, hence `m_max=294`, exactly `m=294`;
- the conditional eight-point certificate has `c=41763/10^7`, `r=7`, hence `m_max=246`, exactly `m=246`.

The frozen bridge source states the formula (1), the cap (2), and the cap-induced maximum (3), and records these parameter choices. The monotonicity theorem (8)--(12) explains the pattern: once `(n,c,p)` is fixed, choosing a smaller `m` cannot improve the final constant if the certificate is capable of beating `H` at all.

## 6. What this isolates as the real configuration-level frontier

`ANF-006` showed that delaying global compression and retaining ordered local configuration can beat the global pair-moment ceiling. `ANF-007` then showed that two points are insufficient and three are the minimal successful local order in this bridge. The present result removes a further apparent degree of freedom: **the scalar block-size tuning after the local certificate does not create additional information.**

For the parametric bridge, a candidate local theorem should therefore be evaluated first through the exact gate (12). Once it passes, the best `m` is automatic. Progress inside this architecture must come from improving the local certificate itself -- changing `n`, `p`, the attainable `c`, or the local functional that produces those quantities -- or from changing the analytic bridge architecture. Searching over `m` after fixing `(n,c,p)` is mathematically redundant.

This does not say that pinching, shifted-block averaging, or the block argument is dispensable. Those steps are part of the theorem that produces (1). It says only that **after their effect has been compressed into `Phi_n`, the remaining block-length parameter carries no independent optimization or zero information on the improving branch.**

## 7. Prior art, falsification, and novelty boundary

The exact `Phi_n` formula, the side condition `c(m-(n-1))<=1`, and the resulting cap on `m` are formal-source material from the `teal-sea/zeta-lab` `n_point_bound` bridge at the frozen source commit already anchored in `SOURCES.md`. Ainta's proof and the bridge sources also instantiate particular maximal blocks. No novelty is claimed for those ingredients or for elementary differentiation of a fractional-linear function.

A targeted check of the bridge documentation and Ainta proof surface did not locate the general monotonicity/admission statement (8)--(12). Absence from those sources is not a publication-level novelty claim. The durable Mathia contribution is the structural reduction relevant to the live research question: **for every improving certificate in this exact bridge, the cap-saturating block is forced, and the existence of any gain is decidable from one scalar inequality.**

The finding would be falsified if the formal bridge used a different `Phi_n`, if the admissible cap were not (2), or if the denominator in (5) could change sign. The frozen formal source gives (1)--(2), and (4) rules out the sign issue. The result is scoped only to this `n_point_bound` architecture; a Bellman/coboundary method, a different block deduction, or another nonlinear configuration-level bridge may introduce genuinely new memory parameters not covered here.