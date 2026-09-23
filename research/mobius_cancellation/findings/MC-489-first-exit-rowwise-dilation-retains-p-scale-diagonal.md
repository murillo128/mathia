# MC-489 — First-exit rowwise dilation passes the q-dependent gate but retains a p-scale diagonal

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-CORRELATION+SIEVE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-488` rules out one common unitary transform of the exact first-exit cells: the cells are disjoint in the original source coordinate, so a common transform cannot manufacture cross-`q` dispersion. The accepted clue deliberately leaves open a narrower possibility: use a transform whose arithmetic depends on the first-exit prime.

The most immediate such operation is the **rowwise first-exit dilation itself**. On the root `q|n`, write `n=qm`; on the root `q|n+h`, write `n+h=qm`. This is genuinely `q`-dependent when the rows are compared in the common `m` coordinate, so it is not covered by the common-transform obstruction of `MC-488`.

For the root `q|n`, define

\[
G_q(m)
:=
K_h(qm)A_q(qm),
\qquad
K_h(x)=\chi(x+h)\overline{\chi(x)},
\qquad
A_q(x)=\mathbf 1_{(x(x+h),P(q))=1},
\tag{1}
\]

where `p` is the prime conductor, `q\ne p` is an active first-exit prime, and `P(q)` is the product of active sieve primes below `q`, with the same fixed exclusions as in `MC-484`--`MC-488`. Assume `h\not\equiv0\pmod p`.

The row has natural period `pP(q)`, and its complete `L^2` energy is exactly

\[
\boxed{
\sum_{m\bmod pP(q)}|G_q(m)|^2
=(p-2)V_q,
}
\tag{2}
\]

where

\[
V_q
:=
\#\{b\bmod P(q):(qb)(qb+h)\text{ is coprime to }P(q)\}
=P(q)d_q
\tag{3}
\]

and

\[
\boxed{
d_q
=\prod_{\substack{\ell<q\\ \ell\ \mathrm{active}}}
\left(1-\frac{\nu_\ell(h)}\ell\right),
\qquad
\nu_\ell(h)=
\begin{cases}
1,&\ell\mid h,\\
2,&\ell\nmid h.
\end{cases}}
\tag{4}
\]

The second root has the same energy after translation. Thus the rowwise `q`-dependent reparameterization does **not** create a power-small row before any cross-row estimate: after removing the purely sieve-period replication,

\[
\boxed{
P(q)^{-1/2}\|G_q\|_2
=\sqrt{(p-2)d_q}.
}
\tag{5}
\]

For every nonempty row, the dimension-two sieve density satisfies

\[
\boxed{
d_q\gg (\log q)^{-2}.}
\tag{6}
\]

Indeed, every odd active prime contributes at least `1-2/ell`; omitted primes or primes dividing `h` only increase the density, while the surviving local factor at `2` is a fixed constant. The identity

\[
1-\frac2\ell
=\left(1-\frac1\ell\right)^2
\left(1-\frac1{(\ell-1)^2}\right)
\tag{7}
\]

for odd primes, together with Mertens' theorem and convergence of the second product, gives `(6)`. If the active prime `2` sees two distinct roots, the row is identically empty; that parity case was already isolated in `MC-472`.

Consequently, in every polynomial first-exit range `q\le p^A` with fixed `A`,

\[
\boxed{
P(q)^{-1/2}\|G_q\|_2
\gg_A \frac{\sqrt p}{\log p}
=p^{1/2-o(1)}.
}
\tag{8}
\]

This yields a method-level obstruction. Any **coefficient-blind Hilbert-space architecture** that applies an isometry/unitary `U_q` separately to each exact row and then seeks a uniform operator-norm saving must retain the row norm `(5)`. If

\[
T(c)=\sum_q c_q\,U_q\!\left(P(q)^{-1/2}G_q\right),
\tag{9}
\]

then, whenever the transformed rows live in a common Hilbert space,

\[
\boxed{
\|T\|_{2\to2}
\ge
\max_q\sqrt{(p-2)d_q}.
}
\tag{10}
\]

This is simply the test `c=e_q`. Therefore row-dependent dilation, completion or Fourier transformation **by itself** cannot prove a uniform `O(p^{1/2-eta})` row-operator bound for any fixed `eta>0` in a polynomial `q` range. The sieve removes only logarithmic density at this level.

The obstruction is deliberately narrower than a no-go for the accepted clue. A specific arithmetic coefficient vector can still cancel across rows, and a dispersion argument can still use signed off-diagonal structure rather than a coefficient-blind operator norm. But the first admissible `q`-dependent transform has now been priced: **changing the row coordinate is not enough; a fixed conductor-power gain must use the actual least-prime weights or a genuinely arithmetic off-diagonal kernel before `L^2` closure.**

No improved estimate for the first-exit family, `M(x)`, a zero-free region, or RH follows.

## 1. Exact diagonal energy

Because `q` is a unit modulo the conductor `p`, multiplicativity gives

\[
K_h(qm)
=\chi(m+hq^{-1})\overline{\chi(m)}.
\tag{11}
\]

Exactly two residues modulo `p`, namely `m=0` and `m=-hq^{-1}`, make this row vanish; on the other `p-2` residues its modulus is one. Hence

\[
\sum_{m\bmod p}|K_h(qm)|^2=p-2.
\tag{12}
\]

The sieve factor in `(1)` depends only on `m mod P(q)`. Since `(p,P(q))=1`, CRT makes the character-support count and the sieve-support count independent on a complete period. This gives `(2)` once `V_q` is counted.

For an active prime `ell<q`, multiplication by `q` is invertible modulo `ell`. The condition

\[
\ell\nmid qm(qm+h)
\]

therefore removes the two classes

\[
m\equiv0,
\qquad
m\equiv-hq^{-1}
\pmod\ell,
\tag{13}
\]

unless they coincide because `ell|h`. CRT across the square-free product `P(q)` proves `(3)`--`(4)`.

This is exactly the same local dimension-two density as the original pair sieve. The rowwise dilation changes the coordinates in which the two forbidden roots are written; it does not add a new local saving.

## 2. The q-dependent dilation does create off-diagonal rows, but complete-period interaction still factorizes

The diagonal floor above is already enough for `(10)`, but the corresponding off-diagonal calculation shows what the row-dependent transform actually creates.

Take distinct active first-exit primes `q<r`, and compare the two root-zero rows in the common `m` coordinate over the joint period `pP(r)`. Put

\[
C_p(q,r)
:=
\sum_{m\bmod p}K_h(qm)\overline{K_h(rm)}.
\tag{14}
\]

The exact shifted-character correlation from `MC-486` gives

\[
\boxed{
C_p(q,r)=
\begin{cases}
p-2,&q\equiv r\pmod p,\\
-1-\chi(hq^{-1})\overline{\chi(hr^{-1})},&q\not\equiv r\pmod p.
\end{cases}}
\tag{15}
\]

so `|C_p(q,r)|<=2` away from repeated conductor residues.

Let

\[
V_{q,r}
:=
\#\{b\bmod P(r):A_q(qb)A_r(rb)=1\}.
\tag{16}
\]

CRT then gives the exact complete-period cross term

\[
\boxed{
\sum_{m\bmod pP(r)}
G_q(m)\overline{G_r(m)}
=C_p(q,r)V_{q,r}.
}
\tag{17}
\]

The sieve count itself factorizes locally. For an active prime `ell<q`, the forbidden set is

\[
\{0,-hq^{-1},-hr^{-1}\}\pmod\ell,
\tag{18}
\]

with coincidences retained exactly; for `q<=ell<r`, only the `r` row is sifted at `ell`, giving the forbidden set

\[
\{0,-hr^{-1}\}\pmod\ell.
\tag{19}
\]

Thus

\[
\frac{V_{q,r}}{P(r)}
=
\prod_{\substack{\ell<q\\\ell\ \mathrm{active}}}
\left(1-\frac{|\{0,-hq^{-1},-hr^{-1}\}\bmod\ell|}{\ell}\right)
\prod_{\substack{q\le\ell<r\\\ell\ \mathrm{active}}}
\left(1-\frac{|\{0,-hr^{-1}\}\bmod\ell|}{\ell}\right).
\tag{20}
\]

So rowwise dilation really does evade the literal hypothesis of `MC-488`: after different rows are rescaled into the same `m` coordinate they can have nonzero cross terms. But on complete periods the new interaction is still a tensor product of a classical shifted-character correlation and an ordinary local sieve overlap. There is no hidden mixed conductor/sieve resonance at this level.

Repeated residues `q\equiv r (mod p)` are a genuine degeneracy, not a gain: the character rows then coincide and `(15)` has size `p`. Any source range allowing such repetitions must aggregate or otherwise account for them explicitly, as already required by `MC-486`.

## 3. Why the diagonal is the decisive coefficient-blind tariff

Suppose a proposed `q`-dependent completion maps each row by an isometry `U_q`. The cross terms between `U_qG_q` and `U_rG_r` may differ radically from `(17)`; `MC-488` no longer forces them to vanish because the transforms are different. Nevertheless, no arrangement of off-diagonal terms can lower the operator norm below the norm of a single column/row in `(9)`. Equation `(10)` is therefore insensitive to whether those off-diagonal terms are favorable, unfavorable, or zero.

This matters because `(6)` shows that the exact first-exit roughness removes only a polylogarithmic fraction of a complete row. If the desired proof is uniform in arbitrary outer coefficients and closes the transformed family by one positive `L^2` operator estimate, the conductor exponent `1/2` has already survived on every nonempty row.

The argument does **not** say that a particular scalar sum over the actual first-exit coefficients is large. A signed coefficient vector may lie close to a small singular direction even when the operator norm is large. Nor does it rule out a bilinear dispersion theorem whose strength comes from the exact coefficient pattern and off-diagonal arithmetic before positive closure. Those are precisely the remaining mechanisms allowed by the accepted clue.

## 4. Prior art and novelty boundary

All ingredients used in the theorem are classical or already audited in the line.

- Buchstab first exit and least-prime assignment are classical sieve theory; `MC-484` and `MC-488` record the exact specialization used here.
- The complete shifted multiplicative-character correlation `(15)` is classical Jacobi-sum/fractional-linear orthogonality, already audited in `MC-485`--`MC-486`; `MC-S55` anchors the more general complete rational-character estimates used elsewhere in this source frame.
- The local pair-sieve factors `(4)` and `(20)` are ordinary CRT survivor counts, already audited in `MC-471`--`MC-472`.
- `MC-S6` supplies the prime-reciprocal Mertens input; `(7)` converts it into the standard dimension-two product scale `(log q)^-2`.

A targeted literature check also found Schlage-Puchta, *Sifted character sums and free quotients of Bianchi groups*, Math. Proc. Cambridge Philos. Soc. 141 (2006), 205--207, DOI `10.1017/S0305004106009261`, confirming that sifted multiplicative-character sums are established analytic-number-theory objects. The very recent Xiao--Li preprints arXiv:`2609.24248` and `2609.24255` study shifted Selberg-weight correlations and their interaction with Kloosterman signs. These are adjacent evidence that shifted sieve weights can support nontrivial oscillatory analysis, but neither source supplies the exact first-exit row Gram `(2)`/`(17)` or a theorem transferring it to the present Möbius source frame.

No novelty is claimed for the finite-field correlation, Mertens product, sieve density, CRT factorization, or Hilbert-space lower bound. The durable Mathia delta is the **frontier classification**: the simplest genuinely `q`-dependent transform left by `MC-488` has now been evaluated with the exact first-exit hard mask, and a coefficient-blind positive `L^2` closure still retains a `p^{1/2-o(1)}` diagonal.

## Boundaries and falsification tests

- **Complete-period statement.** Equations `(2)` and `(17)` concern exact periodic completions. They do not by themselves lower-bound an incomplete source interval; a short-interval theorem using endpoint cancellation lies outside this obstruction.
- **Coefficient-blind `L^2` only.** Equation `(10)` is a uniform operator-norm obstruction. A proved special property of the actual coefficient `c_{q_*(n)}(n)` can still beat it for the one arithmetic vector of interest.
- **Rowwise isometries only.** Artificially rescaling a row can make its norm small, but an exact inversion/reconstruction must then pay the reciprocal scaling. A genuinely non-isometric arithmetic transformation must be priced together with its reconstruction constants before it is compared with `(10)`.
- **Polynomial first-exit range.** The `p^{1/2-o(1)}` conclusion uses `q<=p^A`. Equation `(5)` remains exact without that restriction.
- **Parity and local collisions retained.** If the active prime `2` kills the pair sieve for an odd shift, the row is zero and is removed exactly. Primes dividing `h` or differences such as `q-r` only merge forbidden classes and therefore increase the local overlap densities relative to the generic case.
- **Repeated conductor residues retained.** Distinct source primes congruent modulo `p` produce the large branch in `(15)`; they cannot be treated as independent character rows.
- **No global consequence.** The result is an obstruction for one normalized first-exit proof architecture, not a bound for `M(x)` or a statement about zeta zeros.

## Consequence for the accepted clue

The first `q`-dependent operation suggested by the normalized first-exit family is no longer a live generic escape. Rowwise dilation/completion does create a different cross-row geometry than a common transform, but its exact hard-mask rows retain a `sqrt(p)/log q` complete `L^2` scale and its complete-period cross interactions factor as `(17)`.

The clue should therefore demand more than `q`-dependent coordinates. A surviving continuation must use **load-bearing arithmetic asymmetry** that is absent from one-row energy: the actual least-prime-dependent outer coefficients, a modulus/reciprocity operation in which `q` enters a separate arithmetic slot as in the Pascadi/Yang template of `MC-456`, or a signed off-diagonal estimate that is proved before coefficient-blind positive closure. Another rowwise Fourier/completion argument whose only new feature is the dilation `n=qm` has now been exhausted.