# NB-335 — Integer critical nodes persist under sublinear adjacent reindexing

- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-333
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + CRITICAL-SQUARE-SCALE + ADJACENT-WITNESS-REINDEXING + INTEGER-NODE-STABILITY + DISCRETE-MACROSCOPIC-BLIND-SCALES + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let \(q_j\to\infty\), let \(8\le q_j\le n_j\), and let \(m_j\) be
positive integers satisfying

\[
\frac{m_j}{q_j^2}\longrightarrow L
\qquad
\text{for some }L\in\mathbb N.
\tag{1}
\]

Choose another admissible adjacent index \(p_j\) with

\[
8\le p_j\le n_j,
\qquad
\frac{p_j}{q_j}\longrightarrow c\in(0,\infty),
\tag{2}
\]

and suppose

\[
K:=\frac{L}{c^2}\in\mathbb N.
\tag{3}
\]

With

\[
\nu_{p_j}
:=
g_{p_j}
-
\frac{p_j-1}{p_j}g_{p_j-1},
\]

one has

\[
\boxed{
p_j
\left\langle
(\sqrt{m_j}T_{n_j,m_j}-R_{n_j})g_2,
\nu_{p_j}
\right\rangle
\longrightarrow0.
}
\tag{4}
\]

In particular, taking \(c=1\),

\[
\boxed{
\frac{p_j}{q_j}\to1
\quad\Longrightarrow\quad
p_j
\left\langle
(\sqrt{m_j}T_{n_j,m_j}-R_{n_j})g_2,
\nu_{p_j}
\right\rangle
\to0
}
\tag{5}
\]

at every integer critical node. Thus no adjacent reindexing

\[
p_j=q_j+o(q_j)
\]

restores the leading \(1/p_j\) coefficient, even when
\(|p_j-q_j|\to\infty\).

More generally, (3) exhibits a discrete family of guaranteed
macroscopic blind scales,

\[
\frac{p_j}{q_j}
\longrightarrow
\sqrt{\frac{L}{K}},
\qquad
K\in\mathbb N,
\tag{6}
\]

subject only to admissibility \(p_j\le n_j\). These scales are guaranteed
zeros of this adjacent channel; no claim is made that they exhaust its
zero set.

## 1. Redivide the same dilation by the new witness

Use ordinary Euclidean division,

\[
m_j=D_jp_j+s_j,
\qquad
0\le s_j<p_j.
\tag{7}
\]

From (1)--(3),

\[
\frac{m_j}{p_j^2}
=
\frac{m_j/q_j^2}{(p_j/q_j)^2}
\longrightarrow
\frac{L}{c^2}
=
K.
\tag{8}
\]

Since \(s_j<p_j\),

\[
\frac{D_j}{p_j}
=
\frac{m_j}{p_j^2}
-
\frac{s_j}{p_j^2}
\longrightarrow K.
\tag{9}
\]

The new remainder phase is automatically bounded:

\[
0\le
\frac{s_j}{D_j}
<
\frac{p_j}{D_j}
\longrightarrow
\frac1K.
\tag{10}
\]

This is the point at which the bounded-phase strengthening in `NB-333`
matters. Ordinary Euclidean redivision does not guarantee
\(s_j\le D_j\) when \(K=1\), but it always gives (10), which is exactly
the phase compactness needed by the strengthened profile.

## 2. Integer periodicity kills every phase accumulation point

Apply `NB-333` with the new adjacent index \(p_j\), quotient \(D_j\),
and remainder \(s_j\). Equations (9)--(10) put the sequence at the
integer critical ratio \(K\) with bounded phase. The phase need not
converge: every subsequence has a further subsequence on which
\(s_j/D_j\to\rho\) for some finite \(\rho\).

For each such phase limit, the `NB-333` profile is

\[
\Phi(K,\rho)
=
\frac{
\mathfrak D(\rho K)
-
\mathfrak D((1+\rho)K)
}{4K}.
\tag{11}
\]

Because \(K\) is an integer and \(\mathfrak D\) is \(1\)-periodic,

\[
\mathfrak D((1+\rho)K)
=
\mathfrak D(\rho K+K)
=
\mathfrak D(\rho K),
\]

so every subsequential limit in (11) is zero. Hence the whole sequence
in (4) tends to zero.

No estimate on \(|p_j-q_j|\) beyond the ratio condition is used. The
sublinear statement (5) is therefore not an \(O(1)\)-shift result: it
includes mesoscopic displacements growing without bound.

## 3. Relation to the cusp at the original index

`NB-334` shows that if the exact-lattice aspect ratio of a *fixed*
adjacent index is displaced from an integer \(L\) by a small fixed
amount, its limiting profile leaves the node through a linear cusp.
That is a different perturbation from (4).

Here the dilation \(m_j\) is kept fixed and the witness itself is
reindexed. Redivision changes the effective critical ratio to

\[
\frac{D_j}{p_j}
\longrightarrow
\frac{L}{c^2}.
\tag{12}
\]

When this new ratio is another integer, periodicity forces a new blind
node. In particular \(c=1\) keeps the same integer node, so every
sublinear witness displacement stays blind at leading order.

There is no contradiction with the cusp. The cusp describes moving the
critical aspect ratio away from an integer for one limiting channel;
this finding identifies witness rescalings that land on an integer node
again.

## 4. What the result does and does not rule out

The theorem removes one natural escape route from the critical integer
nodes: optimizing over adjacent witnesses within a \(1+o(1)\)
multiplicative neighborhood cannot recover the leading adjacent
coefficient. A successful source-side route around such a node must
therefore use at least one of the following: a macroscopic witness scale
not landing on (6), a different source/probe family, or genuinely
target-aware information.

The theorem is not an operator-norm upper bound. Another adjacent
witness outside the blind scales may remain resonant, and a non-adjacent
source direction may do so even when every witness covered here is
blind. Nor does (4) give a quantitative two-parameter rate for how fast
the coefficient vanishes when \(p_j/q_j\) approaches a blind scale.

The result is also not a Nyman-distance estimate. It says nothing about
occupation of these source directions by the actual moving target datum,
the first-free sampling excess, or RH.

## 5. Prior-art and audit boundary

The closest audited literature covers the Nyman--Beurling/Báez-Duarte
fractional-part family, generalized dilation criteria, and the
multiplicative autocorrelation of the fractional-part function. Those
sources contain no identified statement about the finite-section
adjacent channel in `NB-333`, Euclidean redivision of one critical
dilation across moving witness indices, or the discrete blind scales
(6). No bibliographic novelty is claimed.

The proof uses no external theorem beyond elementary Euclidean division
and the already-persisted bounded-phase profile of `NB-333`. The
substantive delta is the reindexing invariant: **integer critical
blindness is stable under every sublinear adjacent reindexing and
recurs at the discrete macroscopic scales (6).**
