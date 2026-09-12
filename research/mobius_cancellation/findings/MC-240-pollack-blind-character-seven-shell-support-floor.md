# MC-240 — Pollack's prime-nonresidue bound forces every blind character onto at least seven shell primes

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-square smooth-dilation gate of `MC-238` and `MC-239`. Let

\[
y=c\log X,
\qquad
S\subset\{r\text{ prime}:y<r\le 2y\},
\]

\[
Q_S=\prod_{r\in S}r^2,
\qquad
R_S=\prod_{r\in S}r,
\]

and let

\[
H_y(Q_S)=\langle p\bmod Q_S:p\le y\text{ prime}\rangle.
\]

By `MC-239`, every blind character

\[
\chi\in H_y(Q_S)^\perp
\]

factors through the squarefree radical `R_S`. Write its CRT decomposition as

\[
\chi=\prod_{r\in S}\chi_r,
\qquad
\chi_r\pmod r,
\]

and define its shell support

\[
T(\chi)=\{r\in S:\chi_r\ne 1\},
\qquad
k(\chi)=|T(\chi)|.
\]

Then, **unconditionally**, for all sufficiently large `y`, every nonprincipal blind character satisfies

\[
\boxed{k(\chi)\ge 7.}
\tag{1}
\]

Thus the cross-prime obstruction left by `MC-239` cannot be carried by a pair, triple, quadruple, quintuple, or sextuple of shell primes. Any surviving common-quotient relation must couple at least seven shell factors.

The same statement has a concrete quadratic consequence. For the Legendre matrix from `MC-238`,

\[
A_{p,r}=\frac{1-(\frac pr)}2
\qquad
(p\le y\text{ prime},\ r\in S),
\]

every nonzero vector `v\in\ker_{\mathbb F_2}A` has Hamming weight at least seven for all sufficiently large `y`. Equivalently,

\[
\boxed{\operatorname{spark}_{\mathbb F_2}(A)\ge 7,}
\tag{2}
\]

where the spark is the least number of columns with a nontrivial `\mathbb F_2` linear dependence.

No full-rank statement is proved. High-support blind characters may still exist, and `(1)` gives no Fourier-decay estimate for the bounded smooth-dilation measure and no bound for the Möbius progression amplitude `B_S(X)`.

## 1. Reduce a blind character to its active shell support

Because `MC-239` removes the entire prime-square principal-congruence kernel, a blind character descends to

\[
(\mathbb Z/R_S\mathbb Z)^\times
\cong
\prod_{r\in S}(\mathbb Z/r\mathbb Z)^\times.
\]

Discard the principal local components and put

\[
q_\chi:=\prod_{r\in T(\chi)}r.
\tag{3}
\]

The active product

\[
\chi_T(n):=\prod_{r\in T(\chi)}\chi_r(n)
\tag{4}
\]

is a nontrivial Dirichlet character modulo `q_\chi`. Every nonprincipal character modulo a prime `r` has conductor `r`, so `(4)` is in fact primitive of conductor `q_\chi`; primitivity is not needed for the argument below, but it shows that no hidden inactive modulus remains.

Blindness means

\[
\chi(p)=1
\qquad
\text{for every prime }p\le y.
\tag{5}
\]

Since every prime divisor of `q_\chi` lies in `(y,2y]`, none of the primes in `(5)` divides `q_\chi`, and deleting principal local components does not change their values. Hence

\[
\boxed{
\chi_T(p)=1
\quad\text{for every prime }p\le y.
}
\tag{6}
\]

The question is therefore a least-character-nonresidue problem for a conductor built from `k(\chi)` primes all lying in one dyadic shell.

## 2. Pollack's prime witness contradicts support at most six

Paul Pollack proves the following unconditional theorem. For every fixed `\varepsilon>0`, there are constants `m_0(\varepsilon)` and `\kappa(\varepsilon)>0` such that for every integer `m>m_0(\varepsilon)` and every nontrivial Dirichlet character `\psi (\bmod m)`, there are more than `m^{\kappa(\varepsilon)}` primes

\[
\ell\le m^{\theta+\varepsilon},
\qquad
\theta:=\frac1{4\sqrt e},
\tag{7}
\]

for which

\[
\psi(\ell)\notin\{0,1\}.
\tag{8}
\]

Only existence of one such prime is needed here.

Apply this to `\chi_T` modulo `q_\chi`. If `k=k(\chi)`, then because every active shell prime is at most `2y`,

\[
q_\chi\le(2y)^k.
\tag{9}
\]

Now

\[
6\theta
=
\frac{6}{4\sqrt e}
<1.
\tag{10}
\]

Choose once and for all an `\varepsilon>0` satisfying

\[
6(\theta+\varepsilon)<1.
\tag{11}
\]

For example, `\varepsilon=0.01` works. If `1\le k\le6`, Pollack's theorem gives a prime `\ell` such that

\[
\chi_T(\ell)\notin\{0,1\}
\]

and

\[
\ell
\le
q_\chi^{\theta+\varepsilon}
\le
(2y)^{k(\theta+\varepsilon)}
\le
(2y)^{6(\theta+\varepsilon)}.
\tag{12}
\]

By `(11)`, the last expression is `<y` for all sufficiently large `y`. Therefore Pollack supplies a prime `\ell\le y` with `\chi_T(\ell)\notin\{0,1\}`, contradicting `(6)`, which says `\chi_T(\ell)=1` for every prime up to `y`.

This proves `(1)`.

The argument can be stated as a general support/exponent rule: if a least-prime character witness is known below `m^{\vartheta+o(1)}`, then a shell-built blind character whose active modulus is a product of primes comparable with `y` must asymptotically use at least

\[
\left\lceil\frac1\vartheta\right\rceil
\]

shell factors, with the integer-boundary case interpreted using the available `+\varepsilon` loss. Pollack's `\vartheta=1/(4\sqrt e)` gives the concrete floor seven.

## 3. Quadratic blind relations have minimum Hamming weight seven

For a quadratic blind character, `MC-238` writes

\[
\chi_v(n)
=
\prod_{r\in S}
\left(\frac nr\right)^{v_r},
\qquad
v\in\mathbb F_2^S,
\]

and proves

\[
\chi_v\in H_y(Q_S)^\perp
\iff
Av=0.
\tag{13}
\]

The active shell support of `\chi_v` is exactly the Hamming support of `v`. Applying `(1)` to every nonzero `v` satisfying `(13)` yields

\[
0\ne v\in\ker A
\quad\Longrightarrow\quad
|\operatorname{supp}v|\ge7,
\tag{14}
\]

which is `(2)`.

This upgrades the conclusion of `MC-239` in the quadratic sector. There, subdirectness only forced at least two nonprincipal local components. Here the analytic least-nonresidue theorem rules out **all bounded relations of support at most six**. In coding-language terms, the quadratic annihilator may still be nonzero, but it has minimum distance at least seven.

## 4. What this closes, and what remains open

The result removes the smallest common-quotient mechanisms from the live smooth-dilation route:

- one-coordinate blindness was already excluded by `MC-239`;
- pairwise through six-way cross-prime blind relations are now excluded unconditionally;
- in particular, no low-support quadratic dependence among the Legendre columns can explain failure of the small-prime subgroup to fill the shell product.

This does **not** make the blind quotient trivial. The full shell has about `y/log y` prime factors, so a relation involving seven or many more coordinates remains compatible with `(1)`. Nor does low-support elimination give a quantitative spectral gap for the smooth-dilation measure: a character with large support can still be exactly blind, and even complete group generation would leave the separate Fourier-decay/amplitude gate identified in `MC-238` and the fixed-power sign-amplitude gate summarized in the local Research Mind.

The next algebraic question is therefore more specific than `(16)` of `MC-239`: determine whether **high-support** simultaneous relations

\[
\prod_{r\in T}\chi_r(p)=1
\qquad
\text{for every prime }p\le y,
\qquad |T|\ge7,
\tag{15}
\]

can persist for shell primes `r\in(y,2y]`, and whether the source-selected progression vector couples to such relations in a way that makes them analytically harmless or dangerous.

## 5. Prior art and novelty audit

The external input is classical least-character-nonresidue technology, not a new theorem of this line:

Paul Pollack, *Bounds for the first several prime character nonresidues*, Proceedings of the American Mathematical Society 145 (2017), no. 7, 2815–2826, DOI `10.1090/proc/13432`, arXiv `1508.05035`. Pollack proves exactly the prime-witness statement `(7)`--`(8)` for every nontrivial Dirichlet character modulo an arbitrary sufficiently large integer modulus. The proof uses the fundamental lemma of the sieve, Norton's refinement of Burgess bounds, and smooth-number distribution.

The surrounding least-character-nonresidue literature treats the size of the first prime at which a character leaves `{0,1}` and related average or explicit questions. The prior-art search performed for this finding did not identify a separate theorem formulated as a support bound for the specific shell-product annihilator of `MC-238`/`MC-239`. No novelty is claimed for Pollack's bound, CRT factorization, conductor reduction, or the abstract conversion from a witness exponent to a support floor.

The durable Mathia delta is the specialization to the exact source-selected shell subgroup: once `MC-239` has shown that blind characters are tame cross-prime objects, Pollack's witness theorem immediately forces those objects to be at least seven-way. This is a frontier narrowing, not a new analytic-number-theory theorem.

## 6. Boundaries and falsification tests

- The threshold seven is asymptotic. The proof uses Pollack's `m_0(\varepsilon)` and the eventual inequality `(2y)^{6(\theta+\varepsilon)}<y`; no explicit finite `y` cutoff is asserted.
- The theorem applies to characters in the exact annihilator `H_y(Q_S)^\perp`; it does not say that arbitrary characters modulo `R_S` have large support.
- The result is not restricted to quadratic characters. Equation `(1)` applies to every nonprincipal blind character; `(2)` is only its quadratic matrix translation.
- The use of Pollack is unconditional and does not import GRH, RH, a zero-free region for `zeta`, or a Mertens estimate.
- Support `>=7` is not a power-saving estimate. It must not be substituted for the fixed-power Fourier decay or signed progression cancellation still required by the live route.
- The proof uses the dyadic shell bound `r<=2y`. If the shell width changes materially, the exponent conversion `(9)`--`(12)` must be redone rather than copied unchanged.
