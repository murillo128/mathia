# PC-007 — cumulative new vertices are the Farey sequence; angular-discrepancy RH geometry is classical

**Status:** `DECISIVE-PRIOR-ART` + `BRANCH-CLOSED-AS-NOVELTY`

## Claim

The most direct global geometry of the original prime-circle construction — the angular positions of all vertices that have appeared for the first time up to level `N` — is exactly the Farey sequence of order `N`, modulo the identification of `0` and `1` at the common circle vertex.

For level `q`, the newly born vertices are

\[
P_q^*=\left\{e^{2\pi i a/q}:1\le a\le q,\ (a,q)=1\right\}.
\]

Therefore

\[
\bigcup_{q\le N}P_q^*
\]

ordered by angle is precisely the set of reduced fractions `a/q` with `q<=N`, i.e. the Farey points `F_N`, mapped to the unit circle by

\[
x\longmapsto e^{2\pi i x}.
\]

This means that any investigation based only on how uniformly the cumulative new vertices fill the circle is not a new RH mechanism: it is the classical Farey-discrepancy formulation of RH.

## Franel–Landau gate

Write the ordered Farey points as

\[
f_{1,N}<\cdots<f_{M_N,N},
\qquad
M_N=\sum_{q\le N}\varphi(q),
\]

and define

\[
d_{j,N}=f_{j,N}-\frac{j}{M_N}.
\]

Franel proved that RH is equivalent to the quadratic discrepancy estimate

\[
\sum_{j=1}^{M_N}d_{j,N}^2
=O_\varepsilon(N^{-1+\varepsilon})
\qquad \forall\varepsilon>0,
\]

and Landau gave the corresponding `L^1` formulation

\[
\sum_{j=1}^{M_N}|d_{j,N}|
=O_\varepsilon(N^{1/2+\varepsilon})
\qquad \forall\varepsilon>0.
\]

Thus RH was already expressed in 1924 as the rate at which exactly these primitive/new angular vertices regularize toward uniform spacing.

## Pure circle-geometric restatement

Let

\[
z_{j,N}=e^{2\pi i f_{j,N}},
\qquad
\omega_{j,N}=e^{2\pi i j/M_N}.
\]

Then

\[
|z_{j,N}-\omega_{j,N}|^2
=4\sin^2(\pi d_{j,N}).
\]

Since Farey discrepancy tends uniformly to zero (indeed the classical absolute discrepancy is of order `1/N`), this is uniformly comparable to `d_{j,N}^2`. Consequently the Franel criterion can be rewritten immediately as a chordal matching statement for the original circle:

\[
\boxed{
\mathrm{RH}
\iff
\sum_j |z_{j,N}-\omega_{j,N}|^2
=O_\varepsilon(N^{-1+\varepsilon})
\quad\forall\varepsilon>0.
}
\]

This formulation is geometrically native to the polygon construction, but it is only a repackaging of Franel–Landau and must not be counted as progress toward RH.

## Research consequence

Close as novelty any branch that uses only:

- the cumulative set of newly born vertices;
- their one-dimensional angular distribution;
- discrepancy from uniform spacing;
- `L^1`, `L^2`, Wasserstein/chordal matching, or equivalent norms that are quantitatively comparable to Farey discrepancy.

A genuinely new use of the prime-circle must retain information discarded by the Farey union, for example the **birth level**, inter-level interactions, refinement maps, interior/exterior fields, or a nontrivial dynamics coupling different polygon levels.

## Prior art

- J. Franel, *Les suites de Farey et le problème des nombres premiers* (1924).
- E. Landau, *Bemerkungen zu der vorstehenden Abhandlung von Herrn Franel* (1924).
- Modern expositions continue to state the Franel–Landau criteria as RH-equivalent Farey discrepancy estimates.

No novelty is claimed for the RH equivalence or the Farey identification; this finding is a decisive prior-art closure for a major branch of the original geometric idea.
