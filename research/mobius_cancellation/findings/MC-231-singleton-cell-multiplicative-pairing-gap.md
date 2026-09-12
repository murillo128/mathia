# MC-231 — Exact singleton cells retain almost all first-shell support, but multiplicative parity pairing reaches only a vanishing fraction

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the exact first-shell incidence decomposition of `MC-221` and `MC-228`--`MC-230`. Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and

\[
\mathcal D_y=\{d:y<d\le2y,\ d\text{ prime}\}.
\]

For a shell prime `d`, let

\[
\mathcal R_d
=\{n\le T:(n,P)=1,\ d^2\mid n+P\}
\]

and let the **exact singleton incidence cell** be

\[
\mathcal E_{\{d\}}
=\{n\in\mathcal R_d:
 e^2\nmid n+P\text{ for every }e\in\mathcal D_y\setminus\{d\}\}.
\tag{1}
\]

Write

\[
N_d
=\#\{n\in\mathcal R_d:\mu^2(n)=1\}
\]

as in `MC-221`, and

\[
N_d^{(1)}
=\#\{n\in\mathcal E_{\{d\}}:\mu^2(n)=1\}.
\tag{2}
\]

Then uniformly for `d\in\mathcal D_y`,

\[
\boxed{
N_d^{(1)}=(1+o(1))N_d
=\left(e^{-\gamma}+o(1)\right)
\frac{X}{d^2\log y}.
}
\tag{3}
\]

Consequently the singleton cells alone retain asymptotically the full unsigned first-shell energy:

\[
\boxed{
\sum_{d\in\mathcal D_y}d\,(N_d^{(1)})^2
\sim
\frac{3e^{-2\gamma}}{8c^2}
\frac{X^2}{(\log X)^2(\log\log X)^3}.
}
\tag{4}
\]

Thus the low-incidence frontier left by `MC-230` is already nontrivial at incidence exactly one; it is not created only by mesoscopic overlaps.

There is also a rigid obstruction to the most direct way of exploiting Möbius parity inside such a cell. If `m<n` are square-free members of the same singleton cell and `m\mid n`, write `n=rm`. Since both satisfy

\[
m\equiv n\equiv-P\pmod{d^2}
\]

and `(m,d)=1`, necessarily

\[
\boxed{r\equiv1\pmod{d^2}.}
\tag{5}
\]

Hence every nontrivial divisibility pair inside the cell has

\[
\boxed{r\ge d^2+1,\qquad m\le\frac{T}{d^2+1}.}
\tag{6}
\]

In particular, consider any disjoint pairing of nonzero Möbius terms in `\mathcal E_{\{d\}}` in which each pair `{m,n}` is related by divisibility and has opposite Möbius signs. Every pair must consume a smaller endpoint from the initial segment `m\le T/(d^2+1)`. Therefore the total number of cell points that such a pairing can cancel is at most

\[
\boxed{
2\left(\frac{X}{d^2(d^2+1)}+1\right)
\ll \frac{X}{d^4}+1.
}
\tag{7}
\]

Compared with `(3)`, this is only the fraction

\[
\boxed{
O\!\left(\frac{\log y}{d^2}\right)+o(1)
=O\!\left(\frac{\log\log X}{(\log X)^2}\right)+o(1)
=o(1)
}
\tag{8}
\]

of the nonzero singleton support.

So a sign-reversing involution obtained by multiplying or dividing by factors while staying inside the same source-selected cell cannot be the missing parity mechanism: the congruence itself forces every nontrivial multiplier to be `1 mod d^2`, creating a multiplicative scale jump of order `(\log X)^2`. Such pairings can touch only a vanishing fraction of the cell that already carries near-full unsigned shell mass.

This does **not** rule out parity cancellation inside singleton cells. It rules out the narrower and natural mechanism of proving that cancellation by a divisibility-preserving multiplicative matching. Any successful cellwise route must instead relate arithmetically incomparable integers, use additive/bilinear/harmonic information, or couple cells by a mechanism not reducible to same-cell multiplication.

No bound for the signed singleton sum, `W_y(X)`, `M(X)`, or the zeta zero set follows from this obstruction.

## 1. Additional shell incidences remove only a vanishing fraction of a singleton coordinate

For distinct shell primes `d,e`, simultaneous membership in `\mathcal R_d` and `\mathcal R_e` implies

\[
n\equiv-P\pmod{d^2e^2}
\]

by CRT. Therefore, even after discarding the roughness and square-free restrictions,

\[
\#(\mathcal R_d\cap\mathcal R_e)
\le
\frac{X}{d^2e^2}+1.
\tag{9}
\]

Every square-free member of `\mathcal R_d` that fails to lie in the exact singleton cell has at least one additional shell incidence, so the union bound gives

\[
0\le N_d-N_d^{(1)}
\le
\sum_{e\in\mathcal D_y\setminus\{d\}}
\left(\frac{X}{d^2e^2}+1\right).
\tag{10}
\]

The prime number theorem on `(y,2y]` yields

\[
|\mathcal D_y|\ll\frac{y}{\log y},
\qquad
\sum_{e\in\mathcal D_y}\frac1{e^2}
\ll\frac1{y\log y}.
\tag{11}
\]

Hence

\[
N_d-N_d^{(1)}
\ll
\frac{X}{d^2y\log y}
+
\frac{y}{\log y}.
\tag{12}
\]

`MC-221` proves uniformly

\[
N_d
=\left(e^{-\gamma}+o(1)\right)
\frac{X}{d^2\log y}.
\tag{13}
\]

Since `d\asymp y\asymp\log X`, dividing `(12)` by `(13)` gives

\[
\frac{N_d-N_d^{(1)}}{N_d}
\ll
\frac1y+
\frac{d^2y}{X}
=o(1),
\tag{14}
\]

uniformly in the shell. This proves `(3)`. Substituting the uniform relation `N_d^{(1)}=(1+o(1))N_d` into the unsigned-energy asymptotic of `MC-221` proves `(4)`.

The conclusion is stronger than merely saying that incidence one is common. On the exact first shell, **almost every nonzero input seen by a fixed coordinate belongs to no other shell coordinate at all**, yet these isolated inputs still reproduce the same `X^{2-o(1)}` unsigned energy scale that requires an extra square-root power of signed cancellation.

## 2. Same-cell divisibility forces a large multiplicative jump

Let `m,n\in\mathcal E_{\{d\}}` and suppose `n=rm` with integer `r>1`. Since both points lie in `\mathcal R_d`,

\[
rm\equiv m\equiv-P\pmod{d^2}.
\]

Thus

\[
(r-1)m\equiv0\pmod{d^2}.
\tag{15}
\]

But `m\equiv-P\pmod{d^2}` and `(P,d)=1`, so `(m,d)=1`; therefore `m` is invertible modulo `d^2`. Equation `(15)` immediately gives `(5)`, and then `(6)` follows from `n=rm\le T`.

This argument does not use square-freeness or the exclusions defining exact incidence. In fact, for any nonempty incidence set `S` and

\[
Q_S=\prod_{d\in S}d^2,
\]

any divisibility pair `m\mid n` inside `\mathcal E_S` satisfies

\[
\frac nm\equiv1\pmod{Q_S},
\tag{16}
\]

so the ratio gap only grows with incidence. The singleton case is the most permissive possible one.

When both endpoints are square-free, a sign-reversing pair additionally has

\[
\mu(n)=\mu(m)\mu(r)=-\mu(m),
\]

so `r` is square-free, coprime to `m`, and has odd prime-factor parity. Those extra requirements can only make admissible multiplicative partners sparser; they are not needed for the upper bound.

## 3. Any divisibility matching can use only the short initial segment

Take any collection of disjoint sign-reversing pairs inside the nonzero singleton support, with the two members of each pair comparable by divisibility. Orient each pair as `m<n`. By `(6)`, every smaller endpoint lies in

\[
\mathcal R_d\cap[1,T/(d^2+1)].
\]

The progression `n\equiv-P mod d^2` has spacing `d^2`, so regardless of roughness, square-freeness, or exact-incidence exclusions,

\[
\#\{m\le T/(d^2+1):m\in\mathcal R_d\}
\le
\frac{X}{d^2(d^2+1)}+1.
\tag{17}
\]

Disjointness gives at most one pair per smaller endpoint, proving `(7)`. Combining `(7)` with `(3)` proves `(8)`.

Equivalently, the terminal multiplicative block

\[
\left(\frac{T}{d^2+1},T\right]
\tag{18}
\]

contains almost all nonzero singleton points but cannot contain both endpoints of any nontrivial same-cell divisibility pair. A parity argument based on adding or removing prime factors while preserving the cell therefore has no local matching geometry on the scale where almost all of the mass lives.

## 4. Prior art and novelty boundary

The congruence calculation `(5)` and the matching bound `(7)` are elementary. No novelty is claimed for the fact that two invertible elements in one residue class can be related multiplicatively only by a ratio congruent to `1` modulo the modulus.

The relevant conceptual prior art is the classical sieve **parity phenomenon**, recorded in `MC-S39` (Friedlander--Iwaniec): local divisibility data can preserve density information while failing to distinguish even from odd prime-factor parity. `MC-082` already gives an exact Liouville specialization of that information-loss mechanism. The present finding does not restate that theorem. It specializes the active first-shell geometry and shows that even the most direct parity-sensitive repair -- pairing opposite Möbius signs by multiplication inside one exact source cell -- is structurally unavailable on almost all of the cell because the prescribed square residue forces a scale jump by at least `d^2`.

`MC-S40` is the corresponding positive boundary: Friedlander--Iwaniec parity-sensitive sieve methods can break the classical parity barrier in special sequences by adding genuinely bilinear/harmonic arithmetic information. That is consistent with the present obstruction and points in the same direction: if the first-shell route survives, its parity carrier must be relational information beyond same-cell divisor matching.

A bounded external literature audit for this exact same-residue multiplicative-pairing specialization found nearby work on parity breaking and multiplicative functions in arithmetic progressions, but no reason to treat `(5)`--`(8)` as a named theorem or as external novelty. The durable contribution here is the application to the current Mathia shell frontier, and the result is therefore classified `NO-NOVELTY-CLAIM`.

## 5. Boundaries and falsification tests

- The result rules out only cancellation certificates built from **disjoint same-cell divisibility pairs**. It does not rule out additive pairings, many-to-many identities, bilinear forms, character decompositions, spectral methods, or cancellation between arithmetically incomparable integers.
- A higher-incidence exact cell may be much smaller than its containing CRT progression. The near-full support statement `(3)` is asserted only for singleton cells, where the union bound over one additional shell square is enough.
- Equation `(4)` is an unsigned statement. Large signed cancellation may already occur among singleton points; the finding neither proves nor disfavors it.
- Higher-incidence cells can still contribute signed corrections to the coordinate sum `A_d`. Their support is only logarithmically smaller at low incidence, so they cannot be discarded at the `X^{1/2+o(1)}` target merely because `(3)` holds.
- The ratio gap depends on preserving the exact source-selected residue. A transformation allowed to move between cells or alter the modulus need not satisfy `r\equiv1 mod d^2`.
- The `+1` endpoint term in `(7)` is harmless because `d\asymp\log X` while the singleton support in `(3)` is polynomially large.

The result is falsified if additional-incidence support is not `o(N_d)` uniformly, if a nontrivial same-cell divisibility ratio can fail to be `1 mod d^2`, or if a disjoint divisibility matching can contain more pairs than there are eligible smaller endpoints below `T/(d^2+1)`.

## Consequence for the live frontier

`MC-230` reduced a sufficient first-shell theorem to signed cancellation inside low/mesoscopic exact incidence cells. The present result sharpens the lowest end of that range: **incidence-one cells already retain asymptotically all nonzero support of each first-shell coordinate and reproduce its full unsigned power scale**.

At the same time, multiplicativity does not supply an internal parity involution there. Preserving the source-selected square residue forces every nontrivial multiplicative move to jump by at least `d^2\asymp(\log X)^2`, so only a vanishing initial fraction of the cell can participate in a divisibility matching.

The next viable theorem therefore cannot be "pair each Möbius sign with the opposite sign obtained by adding or removing a factor while staying in the cell." It must explain cancellation among mostly divisibility-incomparable singleton inputs, or use an explicitly source-coupled relation that moves between cells without losing the required sign information.