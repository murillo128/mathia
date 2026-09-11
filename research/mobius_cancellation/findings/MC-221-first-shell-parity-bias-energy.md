# MC-221 — The first square-defect shell has near-full unsigned energy, so the live target is a square-root-scale parity-balance theorem

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `LITERATURE+DERIVED`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the first active square-defect shell from `MC-218`--`MC-220`. Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
q=\prod_{p\le y}p,
\qquad
T=X-q,
\]

and let `d` be prime with `y<d\le2y`. Put

\[
a_d\equiv-q\pmod{d^2}.
\]

The actual Möbius coordinate is

\[
A_d(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv a_d\pmod{d^2}}}\mu(n),
\tag{1}
\]

while `MC-217` introduced the unsigned square-free support count

\[
N_d(T)
:=
\#\left\{n\le T:
\mu^2(n)=1,
\ (n,q)=1,
\ n\equiv a_d\pmod{d^2}
\right\}.
\tag{2}
\]

On this first shell the support count has the uniform asymptotic

\[
\boxed{
N_d(T)
=
\left(e^{-\gamma}+o(1)\right)
\frac{X}{d^2\log y}
}
\tag{3}
\]

for every shell prime `d`. Consequently its weighted unsigned energy

\[
\mathcal U_y(X)
:=
\sum_{y<d\le2y\atop d\ {m prime}}
 d\,N_d(T)^2
\tag{4}
\]

satisfies

\[
\boxed{
\mathcal U_y(X)
\sim
\frac{3e^{-2\gamma}}{8c^2}
\frac{X^2}{(\log X)^2(\log\log X)^3}.
}
\tag{5}
\]

Thus the source-selected residue classes contain an unsigned square-free population with energy `X^{2-o(1)}`. The diagonal target from `MC-209`, restricted to the same first shell,

\[
W_y(X)
:=
\sum_{y<d\le2y\atop d\ {m prime}}
 d\,|A_d(T)|^2
\le X^{1+o(1)},
\tag{6}
\]

would therefore demand cancellation of an entire extra square-root power inside those populations.

This requirement has an exact parity interpretation. Let `E_d` and `O_d` denote the numbers counted by `(2)` with respectively even and odd `omega(n)`. Since every retained `n` is square-free,

\[
N_d=E_d+O_d,
\qquad
A_d=E_d-O_d.
\tag{7}
\]

Define the relative parity bias

\[
\beta_d:=\frac{A_d}{N_d}
=\frac{E_d-O_d}{E_d+O_d}.
\tag{8}
\]

Then the live energy is exactly

\[
\boxed{
W_y
=
\sum_d dN_d^2|\beta_d|^2.
}
\tag{9}
\]

Combining `(5)` and `(9)`, the target `(6)` is equivalent on this shell to the weighted root-mean-square requirement

\[
\boxed{
\left(
\frac{\sum_d dN_d^2|\beta_d|^2}
{\sum_d dN_d^2}
\right)^{1/2}
\le X^{-1/2+o(1)}.
}
\tag{10}
\]

In other words, the first-shell theorem surface is not merely asking that positive and negative Möbius values both occur, or that every fixed almost-prime layer eventually be compensated. It asks for **even/odd square-free prime-factor parity to balance to relative square-root precision, in weighted mean square, inside one source-prescribed reduced residue modulo each `d^2` after the primorial pre-sieve**.

The matched random multiplicative control from `MC-217` can now be calibrated sharply on the same shell. For its Rademacher prime-sign source `f_xi`, `MC-217` proves exactly

\[
\mathbb E_\xi |A_d^\xi|^2=N_d.
\]

Hence `(3)` gives

\[
\boxed{
\mathbb E_\xi W_y^\xi
\sim
 e^{-\gamma}(\log 2)
\frac{X}{(\log\log X)^2}.
}
\tag{11}
\]

Thus a typical prime-sign source sits at diagonal power scale with room to spare, whereas the deterministic all-minus point `xi_p=-1` is required to satisfy `(10)` by arithmetic rather than probability.

Finally, `(3)` sharpens the moving-degree conclusion of `MC-220`. For every fixed `k`, its fixed-degree count obeys

\[
\frac{B_{k,d}(X)}{N_d(T)}
\ll_k
\frac{\log y}{\log X}L_X^{k-1}
=o(1),
\qquad
L_X\asymp\log\log X.
\tag{12}
\]

So **every fixed collection of Hamming degrees occupies a vanishing fraction of the actual selected support**, uniformly over the first shell. The parity balance in `(10)` is necessarily a moving-degree phenomenon or must be enforced by a non-degree-local identity.

No estimate of the form `(6)`, no improved Mertens bound, and no zero-free consequence is proved here.

## 1. Exact primorial inclusion-exclusion gives the rough support density

First ignore square-freeness and count

\[
R_d(T)
:=
\#\{n\le T:(n,q)=1,\ n\equiv a_d\pmod{d^2}\}.
\tag{13}
\]

Because `d>y`, one has `(d,q)=1`; because `a_d=-q mod d^2`, the residue is reduced modulo `d`. Inclusion-exclusion over the square-free divisors of `q` gives

\[
R_d(T)
=
\sum_{r\mid q}\mu(r)
\#\{n\le T:r\mid n,\ n\equiv a_d\pmod{d^2}\}.
\tag{14}
\]

For every `r|q`, the Chinese remainder theorem leaves exactly one residue class modulo `rd^2`, so

\[
\#\{n\le T:r\mid n,\ n\equiv a_d\pmod{d^2}\}
=
\frac{T}{rd^2}+O(1).
\tag{15}
\]

Therefore

\[
\boxed{
R_d(T)
=
\frac{T}{d^2}\prod_{p\le y}\left(1-\frac1p\right)
+O(\tau(q)).
}
\tag{16}
\]

At `y=c log X`,

\[
\tau(q)=2^{\pi(y)}=X^{o(1)},
\tag{17}
\]

while the main term in `(16)` is `X^{1-o(1)}` uniformly for `d~y`. Mertens' product theorem, in the same classical Rosser--Schoenfeld source already retained as `MC-S6`, gives

\[
\prod_{p\le y}\left(1-\frac1p\right)
\sim\frac{e^{-\gamma}}{\log y}.
\tag{18}
\]

Thus `(16)` already has the main term claimed in `(3)` before the square-free restriction is imposed.

## 2. Square-full contamination is lower order uniformly on the shell

Any number counted by `R_d-N_d` has `p^2|n` for some prime `p>y`, because `(n,q)=1`. The prime `p=d` is impossible: `n\equiv-q mod d^2` is nonzero modulo `d`. For `p\ne d`, the simultaneous congruences `p^2|n` and `n\equiv a_d mod d^2` select at most

\[
\frac{T}{d^2p^2}+O(1)
\]

integers. Hence the union bound gives

\[
0\le R_d-N_d
\ll
\frac{T}{d^2}\sum_{p>y}\frac1{p^2}
+\pi(\sqrt T)
\ll
\frac{T}{d^2y}
+\frac{\sqrt X}{\log X}.
\tag{19}
\]

Relative to the main term `X/(d^2 log y)`, both terms in `(19)` are `o(1)` uniformly for `y<d\le2y`. Together with `(16)`--`(18)` this proves `(3)`.

The argument is deliberately elementary. It uses the unusually favorable logarithmic primorial cutoff: exact inclusion-exclusion costs only `tau(q)=X^{o(1)}`. No distribution theorem for rough numbers in large moduli is needed for this first-shell support asymptotic.

## 3. The unsigned energy is almost quadratic

Squaring `(3)` and summing with weight `d` gives

\[
\mathcal U_y
\sim
 e^{-2\gamma}\frac{X^2}{(\log y)^2}
\sum_{y<d\le2y\atop d\ {m prime}}\frac1{d^3}.
\tag{20}
\]

The prime number theorem and partial summation give

\[
\sum_{y<p\le2y}\frac1{p^3}
\sim
\frac{3}{8y^2\log y}.
\tag{21}
\]

Since `y=c log X` and `log y~log log X`, `(20)`--`(21)` prove `(5)`.

Likewise the exact Walsh second moment from `MC-217` yields

\[
\mathbb E W_y^\xi
=
\sum_{y<d\le2y\atop d\ {m prime}}dN_d
\sim
 e^{-\gamma}\frac{X}{\log y}
\sum_{y<d\le2y\atop d\ {m prime}}\frac1d.
\tag{22}
\]

Another PNT partial summation gives

\[
\sum_{y<p\le2y}\frac1p
\sim\frac{\log2}{\log y},
\tag{23}
\]

which proves `(11)`.

The comparison is informative because the random source retains the rational-prime locations, square-free support, primorial pre-sieve and square-divisor incidence geometry. What changes is only the deterministic parity assignment on prime generators.

## 4. Fixed almost-prime layers account for asymptotically none of the support

`MC-220` proves, for each fixed `k>=1`, uniformly over this shell,

\[
B_{k,d}(X)
=
\frac{T}{\varphi(d^2)\log T}
\left(
\frac{L_X^{k-1}}{(k-1)!}
+O_k(L_X^{k-2}+1)
\right).
\tag{24}
\]

Because `d~y->infinity`, `phi(d^2)=d^2(1+o(1))`. Dividing `(24)` by `(3)` gives

\[
\frac{B_{k,d}}{N_d}
=
O_k\left(
\frac{\log y}{\log X}
(1+L_X^{k-1})
\right)
=o(1),
\tag{25}
\]

which is `(12)`. Summing any fixed finite set of degrees preserves `o(1)`.

This separates two obligations that can otherwise be conflated. `MC-220` proves that every fixed signed truncation has enormous energy and must be cancelled by higher degrees. The present support calculation proves additionally that fixed degrees are not merely insufficient because their alternating sum points the wrong way: they represent asymptotically negligible mass inside each selected residue. The actual parity statistic in `(8)` lives overwhelmingly in growing degree.

## 5. Prior art and novelty boundary

Nothing in the support asymptotic is claimed as a new sieve theorem. Mertens' product theorem and the prime number theorem are classical; `MC-S6` supplies a retained explicit source for the former, and the exact inclusion-exclusion argument `(14)`--`(19)` is a logarithmic-cutoff specialization of elementary sieve counting.

The broader warning that positive support density does not determine prime-factor parity is also classical. `MC-S39` records Friedlander--Iwaniec's exposition of the sieve parity phenomenon, while `MC-S40` records a parity-sensitive sieve showing that additional arithmetic structure can sometimes break that blindness. `MC-082` already turns this classical phenomenon into an exact Liouville divisor-density control pair.

There is also direct modern adjacent work on multiplicative functions in arithmetic progressions. `MC-S45` records Klurman--Mangerel--Teraevainen's 2023 work; among other results their Proposition 2.3 gives correct-order lower bounds for both signs `mu(n)=+1` and `mu(n)=-1` in reduced residue classes for almost all prime moduli in its stated range. Such occurrence or positive-density information is far weaker than the relative `X^{-1/2+o(1)}` weighted parity balance in `(10)`, and it does not include the present moving primorial pre-sieve and source-selected square-modulus family.

A targeted search over square-free numbers in arithmetic progressions, rough-number progression counts, Möbius signs in residue classes and the classical sieve parity problem found no basis for claiming a new external theorem here. **No novelty claim is made.** The durable delta is the exact source-specific information budget: the `MC-209` first-shell target is equivalent to square-root-scale balancing of Möbius parity inside a quantitatively explicit `X^{2-o(1)}` unsigned population, with a matched random baseline known exactly.

## 6. Boundaries and falsification tests

- Equation `(3)` is specific to the first active shell `y<d<=2y`. The proof uses `d~log X`, so exact inclusion-exclusion and the square-full error are cheap. No analogous asymptotic is asserted here for root moduli approaching a power of `X`.
- Equation `(10)` is a reformulation of the sufficient energy target `(6)`, not a proof that actual Möbius has the required parity balance.
- Weighted RMS control does not give a pointwise bound for every `beta_d`. A sparse exceptional set of shell primes can remain unless additional information rules it out.
- The random expectation `(11)` is a calibration only. It cannot be transferred to the deterministic all-minus prime-sign assignment.
- The square-free correction in `(19)` is used only as an upper bound. Its exact secondary constant is irrelevant to `(3)` and is not claimed.
- Fixed-degree negligibility `(25)` uses `k` fixed. It says nothing quantitative about the moving central degree window itself; a Sathe--Selberg-type analysis with the rough cutoff and selected progression retained would be needed there.
- Generic sieve parity blindness does not rule out bilinear, spectral, Type-II or other parity-sensitive mechanisms. The result narrows the obligation to the exact signed parity balance `(10)` rather than declaring it impossible.

The exact claims are falsified if the CRT count `(15)` is not uniform over shell primes, if square-full contamination contributes at the same order as `(16)`, if the prime-shell sums `(21)` or `(23)` have different leading constants, or if the first-shell energy in `MC-209` is not exactly the weighted parity-bias energy `(9)`.

## Consequence for the research line

`MC-218`--`MC-220` progressively show that primes, semiprimes and then every fixed number of prime factors cannot explain the required first-shell cancellation. `MC-221` identifies the global object those layers were approximating: a large, explicitly countable square-free rough population whose only missing information is its **parity imbalance** in the selected square-modulus residue.

The next positive mechanism should therefore be judged against a sharper test. It must control the weighted parity bias in `(10)` by information that survives the classical parity obstruction and distinguishes the deterministic Möbius point from the matched random multiplicative ensemble, without importing an RH-equivalent Mertens estimate. A moving-degree Sathe--Selberg description may locate where the mass sits, but positive degree counts alone cannot prove the required sign balance; the missing input must couple the even and odd moving-degree sectors or bypass degree localization altogether.