# NB-333 — Critical off-lattice adjacent drift has an exact Diophantine difference profile

- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-332
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + CRITICAL-SQUARE-SCALE + OFF-LATTICE-DRIFT + BOUNDED-PHASE-EXTENSION + DIOPHANTINE-DIFFERENCE-PROFILE + INTEGER-NODE-STABILITY + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

and let \(R_n\) be the rank-one comparison operator from `NB-314`. For integers

\[
8\le q\le n,\qquad d\ge1,\qquad r\ge0,
\]

write

\[
m=dq+r=d(q+\rho_q),
\qquad
\rho_q:=\frac rd.
\]

Assume, along a sequence with \(q\to\infty\),

\[
\frac dq\longrightarrow\delta\in(0,\infty),
\qquad
\rho_q\longrightarrow\rho\in[0,\infty).
\]

With the adjacent cancellation

\[
\nu_q:=g_q-\frac{q-1}{q}g_{q-1},
\]

define

\[
\mathcal F_{n;q,d,r}
:=
\left\langle
(\sqrt m\,T_{n,m}-R_n)g_2,\nu_q
\right\rangle.
\]

Then

\[
\boxed{
q\,\mathcal F_{n;q,d,r}
\longrightarrow
\Phi(\delta,\rho)
=
\frac{
\mathfrak D(\rho\delta)
-
\mathfrak D((1+\rho)\delta)
}{4\delta},
}
\tag{1}
\]

where

\[
\mathfrak D(x)
:=
\sum_{k=1}^{\infty}
\frac{\|kx\|_{\mathbb Z}^{\,2}}{k^2}.
\tag{2}
\]

The original one-cell regime \(0\le r\le d\) is the special case
\(\rho_q\in[0,1]\). The same profile in fact holds for every convergent
bounded phase \(\rho_q\); no step in the critical cell limit requires the
phase cap \(1\).

For \(\rho=0\), equation (1) reduces to

\[
\Phi(\delta,0)
=
-\frac{\mathfrak D(\delta)}{4\delta},
\]

recovering `NB-332`.

## 1. The scaled adjacent profile works for any bounded phase

Put

\[
\phi(x):=\{x\}-\frac12.
\]

After the exact scaling \(y=dt\), the centered reciprocal profile of the
adjacent witness is

\[
h_{q,\rho_q}(y)
=
\phi\!\left(\left(1+\frac{\rho_q}{q}\right)y\right)
-
\frac{q-1}{q}
\phi\!\left(
\left(1+\frac{1+\rho_q}{q-1}\right)y
\right),
\tag{3}
\]

and

\[
\mathcal F_{n;q,d,r}
=
d\int_0^\infty
F_{g_2}(y/d)\,
h_{q,\rho_q}(y)\,
\frac{dy}{y^2}.
\tag{4}
\]

Formula (3) is exact for every \(\rho_q\ge0\). The restriction
\(0\le\rho_q\le1\) used in the first formulation of this finding merely
described one remainder cell; it is not an algebraic hypothesis.

Fix a phase cap \(R<\infty\) and suppose \(0\le\rho_q\le R\). On a unit
cell \(J\le y<J+1\) with \(J/q\to z>0\), the two near-unit translations in
(3) produce the macroscopic offsets \(\rho z\) and \((1+\rho)z\).
Repeating the cell-mean and centered-first-moment decomposition from
`NB-332` gives, away from the fractional-part break set,

\[
q^3 I_{q,J}
\longrightarrow
C_\rho(z),
\qquad
C_\rho(z)=B_\rho'(z),
\tag{5}
\]

with

\[
B_\rho(z)
=
\frac{
\psi((1+\rho)z)-\psi(\rho z)
}{2z^2},
\qquad
\psi(x):=\{x\}(1-\{x\}).
\tag{6}
\]

The break set is locally finite for fixed \(\rho\), and \(B_\rho\) is
continuous across its breaks because \(\psi\) vanishes at integers.
Thus the derivative may be integrated blockwise without hidden jump
terms.

The tail estimate used in the original off-lattice argument is uniform
on bounded phase sets: for every fixed \(R\),

\[
|I_{q,J}|
\le
C_R\left(
\frac1{qJ^2}
+
\frac1{J^3}
\right),
\tag{7}
\]

with \(C_R\) independent of \(q,J\) and of
\(\rho_q\in[0,R]\). Indeed an interval of length \(q+\rho_q\) contains
one complete \(q\)-period plus a remainder of length at most \(R\), and
one complete \((q-1)\)-period plus a remainder of length at most
\(R+1\); after subtracting the cell mean the primitive is uniformly
bounded by a constant depending only on \(R\). This is exactly the
centering estimate needed for (7).

Consequently the compact cell sum passes to the macroscopic Riemann
limit, and then (7) lets the compact cutoff tend to infinity. This proves
that the critical limit depends on the phase only through (6), for every
finite \(\rho\).

## 2. Alternating selector blocks give the Diophantine difference

Because \(d\) is an integer, \(F_{g_2}(y/d)\) selects alternating blocks
of \(d\) unit cells exactly as in `NB-332`. On the macroscopic coordinate
\(z=J/q\), their limiting width is \(\delta\). Integrating the derivative
in (5) over those blocks reduces the limit to endpoint values of
\(B_\rho\).

The elementary identity

\[
\psi(x)-\frac12\psi(2x)
=
\|x\|_{\mathbb Z}^{\,2}
\tag{8}
\]

then converts the endpoint series into

\[
\frac{
\mathfrak D(\rho\delta)
-
\mathfrak D((1+\rho)\delta)
}{4\delta},
\]

which is (1). Absolute convergence follows immediately from
\(\|kx\|_{\mathbb Z}\le1/2\).

## 3. Integer nodes survive every bounded remainder phase

The function \(\mathfrak D\) is continuous and \(1\)-periodic. Hence for
every integer \(L\ge1\) and every finite \(\rho\ge0\),

\[
\mathfrak D((1+\rho)L)
=
\mathfrak D(\rho L+L)
=
\mathfrak D(\rho L),
\]

so

\[
\boxed{
\Phi(L,\rho)=0
\qquad
(L\in\mathbb N,\ \rho\ge0).
}
\tag{9}
\]

There is also a phase-compact sequential form. Suppose

\[
\frac dq\to L\in\mathbb N
\]

and \(r/d\) is merely bounded, with no assumed phase limit. Every
subsequence has a further subsequence along which \(r/d\) converges.
Equation (9) makes the limit of \(q\mathcal F_{n;q,d,r}\) zero along
every such subsequence. Therefore

\[
\boxed{
q\,\mathcal F_{n;q,d,r}\longrightarrow0
}
\tag{10}
\]

for every bounded critical remainder phase at an integer node.

This strengthening is useful because redividing a fixed critical
dilation by a nearby witness index naturally produces an ordinary
Euclidean remainder whose ratio to the new quotient is bounded but need
not stay below \(1\). `NB-335` applies (10) to that reindexing problem.

## 4. Operator consequence away from the nodes

Whenever

\[
\Phi(\delta,\rho)\ne0,
\]

the physical norm estimate for the adjacent cancellation from `NB-304`
gives

\[
\liminf
\sqrt{\log q}\,
\|\sqrt m\,T_{n,m}-R_n\|
\ge
\frac{\sqrt2\,|\Phi(\delta,\rho)|}{\sqrt{\log2}}.
\tag{11}
\]

This is still a lower bound from one explicit source/probe channel.
Vanishing of \(\Phi\) does not imply that the full operator mixes, and
nothing here supplies target occupation.

## 5. Prior-art and audit boundary

The nearest classical literature studies Nyman--Beurling fractional-part
generators and the multiplicative autocorrelation of the fractional-part
function. In particular, Báez-Duarte's arithmetical reformulations and
the Báez-Duarte--Balazard--Landreau--Saias / Balazard--Martin
autocorrelation work make periodic Bernoulli and rational-cusp structure
natural in this setting. A targeted audit did not identify the finite
section profile (1), its bounded-phase extension, or the integer-node
statement (10) as a stated theorem. No bibliographic novelty is claimed.

No external theorem is load-bearing for (1)--(10): the argument is the
same finite-section cell calculation already established in `NB-332`
and this finding, with the phase cap inspected explicitly. `SOURCES.md`
therefore requires no new dependency.

The result remains source-side. It gives no upper bound for the full
projected-dilation operator, no finite-section target-distance bound,
and no RH implication.
