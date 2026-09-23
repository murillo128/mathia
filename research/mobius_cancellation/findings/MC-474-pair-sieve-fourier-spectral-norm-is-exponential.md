# MC-474 — Pair-sieve Fourier spectral norm is exponential

**Status:** `EXACT-DERIVED` · `CLASSICAL-INGREDIENTS` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-473` shows that exact Möbius inclusion-exclusion followed by independent completion of every divisor/residue branch pays the exponential branch multiplicity

\[
\mathcal B_W(h)=\prod_{q\mid W}(1+\nu_q(h)).
\]

The most natural exact compression is to avoid those divisor branches, keep the pair-sieve mask

\[
A_{W,h}(n)=\mathbf 1_{(n(n+h),W)=1},
\]

intact, and expand **that mask itself** in additive Fourier modes modulo `W`. This reduces the combinatorial tariff, but it does not make termwise completion affordable. The normalized Fourier `ell^1` norm of the exact pair-sieve mask still grows exponentially in the number of sieve primes.

Let `W` be square-free and define the normalized transform on `Z/WZ` by

\[
\widehat A_{W,h}(r)
:=\frac1W\sum_{x\bmod W}A_{W,h}(x)e_W(-rx),
\qquad
e_W(t):=e^{2\pi i t/W}.
\tag{1}
\]

For every prime `q|W`, put

\[
a_{q,h}(x):=\mathbf 1_{x(x+h)\not\equiv0\pmod q}
\]

and

\[
L_q(h):=\sum_{k\bmod q}|\widehat a_{q,h}(k)|.
\tag{2}
\]

CRT tensorization gives the exact spectral/Fourier-algebra norm factorization

\[
\boxed{
\|\widehat A_{W,h}\|_1
:=\sum_{r\bmod W}|\widehat A_{W,h}(r)|
=\prod_{q\mid W}L_q(h).
}
\tag{3}
\]

The local factors are explicit. If `q|h`,

\[
\boxed{
L_q(h)=2\left(1-\frac1q\right).
}
\tag{4}
\]

If `q` is odd and `q\nmid h`,

\[
\boxed{
L_q(h)
=\frac{q-4+2\csc(\pi/(2q))}{q}.
}
\tag{5}
\]

In particular, for every `q>=5`, irrespective of whether `q|h`,

\[
L_q(h)\ge \frac75.
\tag{6}
\]

The prime `3` contributes at least `1`. At `q=2`, an odd shift makes the pair-sieve mask identically zero, exactly as in `MC-472`; for a surviving even shift the local `ell^1` factor is `1`. Therefore every nonzero pair-sieve channel satisfies

\[
\boxed{
\|\widehat A_{W,h}\|_1
\ge
\left(\frac75\right)^{N_5(W)},
\qquad
N_5(W):=\#\{q\mid W:q\ge5\}.
}
\tag{7}
\]

For the primorial sieve `W=W_z` of `MC-472`, omitting the conductor prime if necessary changes `N_5(W_z)` by at most one. Hence if `z` is a fixed positive power of `p`, the prime number theorem makes `(7)` superpolynomial in `p`.

This gives a second exact representation-level obstruction to the incomplete discrepancy

\[
\mathcal D_{W,h}(I)
=
\sum_{n\in I}K_h(n)A_{W,h}(n)
+\frac{H}{p}\delta_W(h),
\qquad
K_h(n)=\chi(n+h)\overline{\chi(n)},
\tag{8}
\]

where `H=|I|` and

\[
\delta_W(h)=\widehat A_{W,h}(0)
=\prod_{q\mid W}\left(1-\frac{\nu_q(h)}q\right).
\tag{9}
\]

Indeed Fourier inversion gives

\[
\mathcal D_{W,h}(I)
=
\delta_W(h)\left(\sum_{n\in I}K_h(n)+\frac Hp\right)
+
\sum_{\substack{r\bmod W\\r\ne0}}
\widehat A_{W,h}(r)
\sum_{n\in I}K_h(n)e_W(rn).
\tag{10}
\]

In the live source regime `H<=p`, every twisted interval sum in `(10)` obeys the same classical completion envelope

\[
\boxed{
\sup_{r\bmod W}
\left|
\sum_{n\in I}K_h(n)e_W(rn)
\right|
\ll \sqrt p\log(2p),
}
\tag{11}
\]

uniformly in `W` coprime to `p`. Thus the strategy

> exact additive Fourier expansion of the pair sieve -> independent modewise completion -> triangle inequality

produces only

\[
\boxed{
|\mathcal D_{W,h}(I)|
\ll
\sqrt p\log(2p)\,\|\widehat A_{W,h}\|_1,
}
\tag{12}
\]

up to an immaterial absolute constant. By `(7)`, this is again catastrophically noncompetitive once the primorial contains many sieve primes. Additive Fourier compression replaces the larger divisor/residue branch count from `MC-473` by a smaller spectral norm, but the remaining tariff is still exponential.

The obstruction is deliberately **not** an energy obstruction. Parseval gives the exact opposite comparison:

\[
\boxed{
\|\widehat A_{W,h}\|_2^2
=\delta_W(h),
\qquad
\|\widehat{A_{W,h}-\delta_W(h)}\|_2^2
=\delta_W(h)(1-\delta_W(h)).
}
\tag{13}
\]

So the mask has small Fourier `ell^2` energy while its Fourier `ell^1` norm is exponentially large. The live escape is correspondingly sharper: any successful Fourier treatment must control the **family of modes jointly** through a restriction/large-sieve/bilinear/dispersion norm, or keep a truncated/factorable sieve representation through the character estimate. Pointwise control of every mode followed by absolute recombination is now closed alongside the termwise divisor expansion of `MC-473`.

No lower bound for the true discrepancy, no Möbius estimate, no zero-free region and no RH consequence follow.

## 1. CRT makes the Fourier norm multiplicative

Because `W` is square-free,

\[
\mathbb Z/W\mathbb Z
\simeq
\prod_{q\mid W}\mathbb Z/q\mathbb Z,
\tag{14}
\]

and the pair-sieve indicator factors pointwise as

\[
A_{W,h}(x)
=
\prod_{q\mid W}a_{q,h}(x_q).
\tag{15}
\]

The dual group factors by the same CRT decomposition. Under the normalized Fourier convention `(1)`, Fourier transform therefore sends `(15)` to the tensor product of the local transforms. Taking absolute values and summing all dual coordinates gives

\[
\sum_{r\bmod W}|\widehat A_{W,h}(r)|
=
\prod_{q\mid W}
\sum_{k\bmod q}|\widehat a_{q,h}(k)|,
\tag{16}
\]

which is `(3)`.

This is standard finite harmonic analysis; no arithmetic estimate has entered.

## 2. The local spectral norm is explicit

Suppose first that `q|h`. Then the two forbidden residues `0` and `-h` coincide, so `a_{q,h}` is `1` off the single residue `0`. Its normalized transform is

\[
\widehat a_{q,h}(0)=\frac{q-1}{q},
\qquad
\widehat a_{q,h}(k)=-\frac1q\quad(k\ne0).
\tag{17}
\]

Summing absolute values proves `(4)`.

Now let `q` be odd and `q\nmid h`. The two forbidden residues are distinct. Hence

\[
\widehat a_{q,h}(0)=\frac{q-2}{q},
\qquad
\widehat a_{q,h}(k)
=-\frac{1+e_q(kh)}q
\quad(k\ne0).
\tag{18}
\]

Multiplication by `h` permutes the nonzero residues modulo `q`, while

\[
|1+e_q(k)|=2|\cos(\pi k/q)|.
\tag{19}
\]

For odd `q`, symmetry and the elementary finite cosine sum give

\[
\sum_{k=1}^{q-1}|1+e_q(k)|
=4\sum_{k=1}^{(q-1)/2}\cos(\pi k/q)
=2\left(\csc\frac{\pi}{2q}-1\right).
\tag{20}
\]

Substituting `(20)` into `(18)` proves `(5)`.

For `q>=5`, if `q|h`, `(4)` gives `L_q(h)>=8/5`. If `q\nmid h`, use `sin x<=x` to obtain

\[
L_q(h)
\ge
1+\frac4\pi-\frac4q
>
\frac75.
\tag{21}
\]

At `q=3`, formula `(5)` gives exactly `1` in the nondividing case and `(4)` gives `4/3` in the dividing case. At `q=2`, the nondividing case has no survivors; the dividing case has local spectral norm `1`. This proves `(6)`--`(7)` including the parity boundary.

Numerically the nondividing local factor begins

\[
L_3=1,
\quad
L_5\approx1.4944,
\quad
L_7\approx1.7126,
\quad
L_{11}\approx1.9139,
\]

and tends to `1+4/pi`. The growth in `(7)` is therefore not an artifact of the coarse constant `7/5`.

## 3. Uniform modewise completion still costs the full spectral norm

Write the `p`-periodic translated-ratio phase in normalized additive Fourier series

\[
K_h(n)=\sum_{u\bmod p}c_u e_p(un),
\qquad
c_u=\frac1p\sum_{x\bmod p}K_h(x)e_p(-ux).
\tag{22}
\]

The zero coefficient is `c_0=-1/p` by `MC-472`. For `u\ne0`, the same bounded-complexity mixed character sum used in `MC-448` and anchored by `MC-S55` gives

\[
|c_u|\ll p^{-1/2}.
\tag{23}
\]

Fix any real `alpha` and any interval `I` of length `H<=p`. From `(22)`,

\[
\left|
\sum_{n\in I}K_h(n)e(\alpha n)
\right|
\le
\max_u|c_u|
\sum_{u\bmod p}
\min\!\left(H,\frac1{2\|\alpha+u/p\|}\right).
\tag{24}
\]

The `p` points `alpha+u/p (mod 1)` form a translated grid of spacing `1/p`. Ordering them by distance to the nearest integer gives one or two nearest points of contribution at most `H`, and at most two points at each subsequent distance scale `j/p`. Consequently

\[
\sum_{u\bmod p}
\min\!\left(H,\frac1{2\|\alpha+u/p\|}\right)
\ll p\log(2p),
\tag{25}
\]

uniformly in `alpha` when `H<=p`. Combining `(23)`--`(25)` proves `(11)` after taking `alpha=r/W`. The harmless `u=0` coefficient is smaller than the envelope in `(23)` and can be included in the same estimate.

Equation `(10)` and triangle inequality now give

\[
|\mathcal D_{W,h}(I)|
\ll
\sqrt p\log(2p)
\left(
\delta_W(h)+
\sum_{r\ne0}|\widehat A_{W,h}(r)|
\right),
\tag{26}
\]

and the parenthesis is exactly `||widehat A||_1`, proving `(12)`.

For comparison with `MC-473`, a modewise proof could beat the trivial `O(H)` estimate only if

\[
\|\widehat A_{W,h}\|_1
\ll
\frac{H}{\sqrt p\log p}
\le
\frac{\sqrt p}{\log p}.
\tag{27}
\]

When `W=W_z` and `z` is a fixed positive power of `p`, `(7)` violates `(27)` by a superpolynomial factor.

## 4. The exponential loss is specifically an `ell^1` scalarization loss

With the normalized transform `(1)`, Parseval says

\[
\sum_{r\bmod W}|\widehat A_{W,h}(r)|^2
=
\frac1W\sum_{x\bmod W}|A_{W,h}(x)|^2.
\tag{28}
\]

Because `A` is an indicator, the right side is exactly its density `delta_W(h)`, proving the first identity in `(13)`. Subtracting the mean removes only the zero Fourier coefficient, so

\[
\sum_{r\ne0}|\widehat A_{W,h}(r)|^2
=\delta_W(h)-\delta_W(h)^2,
\tag{29}
\]

which proves the second identity.

Thus the exact pair sieve is not spectrally expensive in every norm. It is expensive in precisely the norm created by **independent modewise estimates plus triangle inequality**. That distinction matters: applying `(11)` one mode at a time throws away the low total energy and all possible correlation between the coefficient vector `widehat A(r)` and the twisted-character vector in `(10)`.

This makes the next target more precise than the conclusion of `MC-473`. A useful Fourier route must establish a joint estimate for those two vectors before absolute values, or replace the exact hard mask by weights whose approximation error and Fourier/restriction norm can both be paid inside the source budget.

## 5. Prior art and novelty boundary

Every harmonic ingredient in `(3)`--`(5)` and `(13)` is classical: Fourier transform on finite abelian product groups, tensor-product factorization, Parseval, and elementary finite trigonometric sums. The single-coprimality analogue is the classical Ramanujan-sum Fourier transform of a reduced-residue indicator. No novelty is claimed for these facts or for the terminology `spectral norm`/Fourier `ell^1` norm.

The relevant analytic escape from `ell^1` scalarization also has established prior art. Ben Green and Terence Tao, *Restriction theory of the Selberg sieve, with applications*, Journal de Théorie des Nombres de Bordeaux 18 (2006), no. 1, 147--182, DOI `10.5802/jtnb.538`, proves an `L^2`--`L^p` restriction theorem for Selberg-sieve majorants and applies it to exponential sums over prime tuples. That theorem does not estimate the exact pair mask in `(8)` against the translated-ratio character phase, so no theorem transfer is asserted here; it is an adjacent classical demonstration that retaining joint Fourier norms of sieve weights can avoid naive coefficientwise `ell^1` treatment.

A targeted audit on 23 September 2026 over finite Fourier transforms of sifted/reduced-residue indicators, spectral norms of product Boolean functions, Selberg-sieve restriction theory, and exponential sums over sifted sets found the classical ingredients and adjacent restriction machinery but no reason to claim a new general Fourier theorem. The durable result is the exact specialization to the live `MC-472` pair mask and the quantitative consequence for the route left open by `MC-473`: **changing from divisor branches to exact additive Fourier modes reduces the exponential base but does not remove exponential absolute-recombination cost.**

## Boundaries and falsification tests

- **This is a method obstruction, not a lower bound for `mathcal D`.** Large Fourier `ell^1` norm does not imply that the true discrepancy is large. Cancellation among modes may be substantial.
- **The uniform completion step is only invoked in the live `H<=p` regime.** For longer intervals the additive `W`-twist has joint period `pW`, and `(11)` is not asserted in that form.
- **Odd shifts with `2|W` are already zero channels.** The exponential lower bound is stated only for a nonzero pair-sieve mask; surviving primorial shifts are even.
- **The exact hard mask matters.** Truncated beta-sieve, Selberg-sieve, well-factorable, or signed approximation weights can have different Fourier norms. They remain live provided their approximation error is charged quantitatively.
- **`ell^2` remains cheap.** Equation `(13)` explicitly prevents interpreting `(7)` as a generic spectral-complexity no-go. Restriction, large-sieve, bilinear and dispersion estimates that couple modes before absolute values are not ruled out.
- **The local lower bound is intentionally coarse.** Exact factors `(4)`--`(5)` should be used for any optimized finite-range calculation; `7/5` is only a transparent asymptotic obstruction.
- **No prime-specific conclusion is inferred from generic product structure.** The tensorization itself would hold for matched local product masks. What matters here is only that the exact rational-prime pair sieve cannot be made cheap by this particular exact representation plus scalarization.

## Consequence for the research line

The two obvious exact decompositions of the `MC-472` incomplete pair-sieve discrepancy are now classified at the point where they lose structure. `MC-473` shows that divisor/residue inclusion-exclusion plus branchwise completion pays `B_W(h)`, while the present result shows that exact additive Fourier compression plus modewise completion pays `||widehat A||_1`, which is smaller but still exponential across the primorial.

The surviving target is therefore no longer another exact basis change followed by independent square-root estimates. It is a **joint sieve/trace-function estimate before scalarization**: a truncated or factorable pair sieve whose error is controlled, a restriction/large-sieve bound for the weighted mode family, or a bilinear/dispersion identity coupling sieve and character coefficients before absolute values. The small `ell^2` energy in `(13)` gives a concrete reason such a route is not excluded by the current obstruction.