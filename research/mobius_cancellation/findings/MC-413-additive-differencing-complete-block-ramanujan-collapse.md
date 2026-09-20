# MC-413 — Additive differencing leaves source coupling only in incomplete conductor blocks

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the well-factorable upper-sieve branch of `MC-409`--`MC-412`. Let `chi` be a primitive Dirichlet character of conductor `q`, let

\[
w(n):=\sum_{d\mid n}\lambda_d,
\qquad
a_n:=w(n)\chi(n),
\tag{1}
\]

with finitely supported complex coefficients `lambda_d`. Ordinary additive van der Corput differencing does pass the first obstruction identified in `MC-410`--`MC-412`: for a nonzero shift `h`, the correlation

\[
C_h(N):=\sum_{n\le N-h}a_{n+h}\overline{a_n}
\tag{2}
\]

contains the genuinely translated character phase `chi(n+h) overline{chi(n)}` rather than the separable product `chi(d)chi(m)` or the removable Fourier phase of `MC-411`.

However, after expanding the divisor weights, **every complete block of one source conductor `q` loses the sieve/lcm phase exactly**. For each compatible divisor pair, the complete-period character correlation is the same Ramanujan sum `c_q(h)`, independent of the two divisors, their lcm, the CRT residue, and even the particular primitive character.

More precisely, expansion of `(2)` gives

\[
C_h(N)
=
\sum_{d,e}\lambda_d\overline{\lambda_e}
\sum_{\substack{n\le N-h\\ d\mid n+h\\ e\mid n}}
\chi(n+h)\overline{\chi(n)}.
\tag{3}
\]

A pair `(d,e)` contributes only if

\[
(d,e)\mid h.
\tag{4}
\]

If additionally `(de,q)>1`, the inner sum is identically zero because one of the two character factors is forced onto a nonunit modulo `q`. Otherwise set

\[
L=[d,e],
\tag{5}
\]

and let `r (mod L)` be the CRT class satisfying `r=0 (mod e)` and `r=-h (mod d)`. Writing `n=r+Lk`, with `L` invertible modulo `q`, gives

\[
\chi(n+h)\overline{\chi(n)}
=
\chi(k+u+a)\overline{\chi(k+u)},
\tag{6}
\]

where

\[
u\equiv rL^{-1}\pmod q,
\qquad
a\equiv hL^{-1}\pmod q.
\tag{7}
\]

For any `q` consecutive values of `k`, translation by `u` and the primitive-character Gauss transform give the exact identity

\[
\boxed{
\sum_{k\bmod q}\chi(k+u+a)\overline{\chi(k+u)}
=c_q(a)=c_q(h).
}
\tag{8}
\]

The last equality uses `(L,q)=1`, so multiplication by `L^{-1}` permutes the unit classes and preserves the Ramanujan sum. Equivalently,

\[
\sum_{x\bmod q}\chi(x+a)\overline{\chi(x)}=c_q(a)
\tag{9}
\]

for every primitive Dirichlet character `chi (mod q)`. In particular, if `q` is squarefree and `g=(h,q)`, then

\[
c_q(h)=\mu(q/g)\varphi(g).
\tag{10}
\]

Thus if the progression in `(3)` contains `K_{d,e}` consecutive `k`-values and

\[
K_{d,e}=B_{d,e}q+s_{d,e},
\qquad 0\le s_{d,e}<q,
\tag{11}
\]

its inner sum has the exact decomposition

\[
\boxed{
B_{d,e}c_q(h)+E_{d,e,h},
\qquad |E_{d,e,h}|\le s_{d,e}<q.
}
\tag{12}
\]

All genuinely nonseparable dependence on the divisor pair is therefore confined to the **incomplete remainder** `E_{d,e,h}`. The complete-block term remembers the divisor pair only through incidence/length data such as `(d,e)|h`, `[d,e]`, and the number of complete blocks; it carries no surviving source-character phase indexed by `[d,e]`.

This sharply narrows the live interpretation of additive differencing. A translated phase really is created, so `MC-412` does not kill the route. But complete-period cancellation cannot be credited as a new well-factorable source interaction: after one full conductor period, that phase has already collapsed to the character-independent Ramanujan scalar `c_q(h)`. Any gain capable of changing the source-depth barrier must therefore come from **collective control of the incomplete translated correlations**, before they are completed or bounded separately.

No new estimate for `C_h(N)`, `M_chi(X)`, or the Mertens function follows.

## 1. Exact divisor-pair expansion and the first genuine translation

For `(2)`, expand both copies of `w`:

\[
w(n+h)\overline{w(n)}
=
\sum_{d\mid n+h}\sum_{e\mid n}
\lambda_d\overline{\lambda_e}.
\tag{13}
\]

The simultaneous congruences

\[
n\equiv-h\pmod d,
\qquad n\equiv0\pmod e
\tag{14}
\]

have a solution exactly when `(d,e)|h`. This is the first place in the `MC-409` representation where the two divisor variables enter a relation that is not the zero-residue scalarization of `MC-412`.

If a prime dividing `q` also divides `e`, then every admissible `n` has `chi(n)=0`; if it divides `d`, every admissible `n+h` has `chi(n+h)=0`. Hence only `(de,q)=1` survives. For such a pair, the CRT solutions are one class `r (mod L)` with `L=[d,e]`.

Substituting `n=r+Lk` and multiplying both character arguments by `L^{-1} (mod q)` yields `(6)`--`(7)`. The scalar `chi(L)` cancels against its conjugate. Unlike `chi(Lm)=chi(L)chi(m)`, the additive shift `h` cannot be removed pointwise by complete multiplicativity. So additive differencing does produce a mathematically real translated character correlation.

The question is how much of that translation survives the next natural compression.

## 2. Primitive-character autocorrelation is exactly a Ramanujan sum

Define the periodic autocorrelation

\[
R_\chi(a):=\sum_{x\bmod q}\chi(x+a)\overline{\chi(x)}.
\tag{15}
\]

For the additive Fourier transform

\[
\widehat\chi(t):=\sum_{x\bmod q}\chi(x)e(-tx/q),
\tag{16}
\]

primitivity gives the classical Gauss-sum dichotomy

\[
|\widehat\chi(t)|^2
=
\begin{cases}
q,&(t,q)=1,\\
0,&(t,q)>1.
\end{cases}
\tag{17}
\]

Applying finite Fourier inversion/Plancherel to the autocorrelation gives

\[
R_\chi(a)
=
\frac1q\sum_{t\bmod q}|\widehat\chi(t)|^2 e(ta/q)
=
\sum_{\substack{t\bmod q\\(t,q)=1}}e(ta/q)
=c_q(a).
\tag{18}
\]

This identity is completely classical. It also shows why the answer is independent of the primitive character: the squared Fourier magnitude has forgotten its multiplicative phase and retains only the unit-support mask.

Now `a=hL^{-1} (mod q)`. Because `L` is a unit modulo `q`, multiplication of the Ramanujan-sum index by `L^{-1}` merely permutes the additive unit frequencies, proving

\[
c_q(hL^{-1})=c_q(h).
\tag{19}
\]

Thus the exact lcm-dependent translation created by `(14)` disappears after a complete source period.

For squarefree `q`, the standard formula

\[
c_q(h)=\sum_{r\mid(q,h)}r\mu(q/r)
\tag{20}
\]

reduces to `(10)`. The complete block can therefore be large when `h` shares source primes with `q`, but that largeness is a function only of `(h,q)`, not of the sieve-factor pair.

## 3. The complete/incomplete split is the real frontier

For fixed `(d,e)`, the admissible `k` form one ordinary integer interval. Partition it into complete blocks of length `q` plus one terminal block of length `s_{d,e}<q`. Equation `(8)` evaluates every full block exactly, producing `(12)`.

This has two consequences.

First, long progression pieces with `K_{d,e}\gg q` do not accumulate a new divisor-dependent character phase. Their bulk is a scalar Ramanujan contribution. Any outer analysis may still use the incidence relation `(d,e)|h`, the lcm through `K_{d,e}`, or cancellation in the sieve coefficients, but those are no longer source-character oscillations.

Second, the only part where the translated phase still knows the starting residue and `L^{-1}` is the incomplete remainder. In the difficult large-source regime it is entirely possible that `K_{d,e}<q`, in which case the whole correlation lies in this incomplete sector. Equation `(12)` therefore does **not** make the route easy; it tells us exactly where the difficulty lives.

The correct next analytic object is consequently a family of incomplete translated sums of the form

\[
\sum_{k\in I_{d,e}}
\chi(k+u_{d,e}+h[d,e]^{-1})
\overline{\chi(k+u_{d,e})},
\qquad |I_{d,e}|<q,
\tag{21}
\]

coupled to well-factorable divisor coefficients and the compatibility condition `(d,e)|h`. A successful continuation must estimate this **family collectively** strongly enough that the gain survives summation over divisor pairs and the later source-frame bookkeeping.

Bounding each remainder separately by Burgess/Pólya--Vinogradov-type estimates and then taking absolute values may simply restore the same conductor tariff in another coordinate. The point of the retained-variable clue is to determine whether factorability or dispersion can exploit the joint variation of `u_{d,e}` and `h[d,e]^{-1}` before that loss occurs.

## 4. Prior-art and novelty boundary

The primitive Gauss-sum formula `(17)`, the autocorrelation identity `(18)`, and the Ramanujan-sum formula `(20)` are classical. No novelty is claimed for them. Standard treatments of primitive Dirichlet characters derive the same Gauss-transform support and `|tau(chi)|=sqrt(q)`; for example Iwaniec--Kowalski, *Analytic Number Theory* (AMS Colloquium Publications 53, 2004), and Helfgott, *The Ternary Goldbach Problem*, Chapter 3, use the primitive Gauss transform together with Ramanujan sums.

The analytic significance of **incomplete** shifted character correlations is also established prior art. Heath-Brown's q-analogue of the van der Corput `A`-process and Irving's *Estimates for character sums and Dirichlet L-functions to smooth moduli* (Int. Math. Res. Not. 2016; arXiv:1503.07156) use differencing to replace a short character sum by shifted products and then exploit modulus factorization before completion. Irving explicitly describes the `A`-process as reducing the modulus and the `B`-process as completion; progressively more complicated complete sums are the price of iteration.

Those results do not directly estimate `(3)` with a well-factorable divisor weight, nor do they supply the source-frame gain sought here. Conversely, the present calculation does not improve Burgess/Heath-Brown/Irving bounds. It identifies which part of the classical shifted-correlation mechanism remains nontrivial after the **specific divisor-pair geometry of `MC-409`** is inserted.

A targeted literature audit on 20 September 2026 found the complete primitive-character autocorrelation and q-van der Corput machinery as standard ingredients, but no result that turns the particular well-factorable divisor-pair family `(21)` into the source-cost improvement required by this Mathia branch. No novelty claim is made from that absence.

The durable Mathia contribution is therefore a frontier classification: additive differencing is the first tested operation after `MC-409` that genuinely creates a nonseparable translated character phase, but its complete-conductor component collapses universally to a Ramanujan scalar. The retained-variable search has been reduced from all shifted correlations to their incomplete, divisor-coupled boundary pieces.

## Boundaries and falsification tests

- **This does not kill additive differencing.** It isolates the only sector where its source/lcm phase remains nontrivial: incomplete conductor blocks.
- **The complete-block scalar is not always small.** `c_q(h)` can be large when `(h,q)` is large. The claim is independence from the divisor pair and primitive-character phase, not a uniform smallness estimate.
- **Outer lcm/incidence structure remains.** The block count `B_{d,e}`, compatibility `(d,e)|h`, and interval geometry still depend on the divisor pair. The finding says only that the complete-period *character oscillation* no longer does.
- **Imprimitive characters are outside the exact statement.** Their Fourier magnitude has extra conductor/presentation structure. Any use of a larger presentation modulus must descend to the primitive conductor before being compared with `(18)`.
- **No triangle inequality is hidden in `(8)`--`(12)`.** The complete-period collapse is exact. A future argument must preserve the incomplete family before absolute values if it hopes to obtain a collective gain.
- **Generic individual short-sum bounds are not yet a source-frame gain.** A continuation must propagate the resulting estimate through the divisor-pair coefficients and source-depth/common-radical bookkeeping.
- **No RH or zero-free continuation is used.** All identities are finite harmonic analysis and CRT/divisor algebra.

## Consequence for the research line

`MC-410` showed that the raw factorable product is Mellin-separable, `MC-411` showed that ordinary completion of the unshifted product is only a dual permutation, and `MC-412` showed that the bare divisor condition is the degenerate zero residue. Additive differencing escapes those three obstructions only temporarily: it creates the required translation, but every full source-conductor block then becomes the universal Ramanujan correlation `c_q(h)`.

The next decisive calculation should therefore stay inside the incomplete family `(21)`. It should ask whether the well-factorable coefficients and the coupled CRT data `(u_{d,e},h[d,e]^{-1})` permit a **collective** q-van der Corput/dispersion estimate whose post-Cauchy diagonal is smaller than the current source-depth tariff. If completion is applied first and replaces the family by `(8)`, the candidate has already discarded the only surviving divisor-dependent source phase and cannot solve the retained-variable problem by that route.