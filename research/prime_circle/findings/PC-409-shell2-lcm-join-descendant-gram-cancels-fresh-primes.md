# PC-409 — least-common-refinement Gram sum cancels every fresh-prime channel

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-GCD/JOIN-KERNEL` + `DECISIVE-NEGATIVE` for the canonical two-index Hilbert coupling obtained by pairing distinct shell-2 descendants first and only then summing them with the least-common-refinement conductor. This closes a natural part of the distinct-descendant-index escape left open by PC-407/PC-408. It does **not** classify arbitrary cross-index weights, source-derived angular/chord/old-new couplings, products that change the descendant state space, or genuinely renormalized interactions whose complexity grows with conductor.

PC-405 gives an exact multiplicative descendant tree, PC-406 classifies its one-index Dirichlet completion, PC-407 squares each descendant before the conductor sum, and PC-408 treats fixed-degree products at one common descendant index. A remaining natural question is whether two *different* descendant labels can interact nontrivially before conductor summation. The divisibility lattice supplies a canonical nonseparable way to do this: two descendant conductors `m,k` have minimal common refinement `[m,k]=lcm(m,k)`. Weighting their Hilbert pairing by `[m,k]^{-s}` couples the labels through the join operation instead of summing them independently.

The result is unexpectedly rigid. In the Mellin representation of PC-407, every prime not already present in the parent cancels **exactly** from this double sum. Only finitely many Euler factors from primes dividing the parent survive. Thus the most canonical join-coupled cross-index Gram completion does not merely remain source-blind: it erases the entire fresh-prime Euler product.

## 1. Descendant multipliers from PC-407

For a fixed parent shell `n>1`, PC-407 represents the conjugated radial-flux field as

\[
h_n\in\mathcal H=L^2(\mathbb R_+,dx/x)
\]

and its multiplicative descendants as

\[
h_{nm}=C_{n,m}h_n.
\tag{1}
\]

Under Mellin-Plancherel,

\[
\widehat{V_a h}(t)=a^{it}\widehat h(t),
\tag{2}
\]

so for a prime power `p^a` the scalar descendant multiplier is

\[
c_{n,p^a}(t)=
\begin{cases}
1,&a=0,\\[1mm]
p^{iat},&a\ge1,\ p\mid n,\\[1mm]
p^{i(a-1)t}(p^{it}-1),&a\ge1,\ p\nmid n.
\end{cases}
\tag{3}
\]

For general `m`, multiplicativity gives

\[
\widehat{h_{nm}}(t)=c_{n,m}(t)\widehat h_n(t),
\qquad
c_{n,m}(t)=\prod_p c_{n,p^{v_p(m)}}(t).
\tag{4}
\]

The important distinction is again fresh versus repeated primes: a fresh prime contributes one discrete difference, while a prime already dividing `n` contributes only a phase.

## 2. The least-common-refinement Gram completion

The divisibility lattice has join `[m,k]=lcm(m,k)`. Therefore the minimal common descendant level of the parallel labels `m` and `k` is canonically measured by `[m,k]`. For real `sigma>1`, define

\[
\boxed{
\mathcal J_n(\sigma)
:=
\sum_{m,k\ge1}
\frac{\langle h_{nm},h_{nk}\rangle_{\mathcal H}}
{[m,k]^\sigma}.
}
\tag{5}
\]

This is genuinely a two-index coupling before conductor summation: the weight is not a product of a function of `m` and a function of `k`.

The series is absolutely convergent for `sigma>1`. Indeed each fresh prime contributes an operator factor of norm at most `2`, repeated primes are unitary, and the local absolute majorant at a prime is `1+O(p^{-sigma})`; hence the Euler product of absolute majorants converges in that half-plane. Mellin-Plancherel then gives

\[
\mathcal J_n(s)
=
\frac1{2\pi}\int_{\mathbb R}
|\widehat h_n(t)|^2 K_n(s,t)\,dt,
\qquad \Re(s)>1,
\tag{6}
\]

where

\[
K_n(s,t)
:=
\sum_{m,k\ge1}
\frac{c_{n,m}(t)\overline{c_{n,k}(t)}}{[m,k]^s}.
\tag{7}
\]

Because both the descendant coefficients and `lcm` are primewise multiplicative, (7) has an Euler product.

## 3. Fresh primes cancel exactly

Fix a prime `p\nmid n`, put

\[
A=p^{it},\qquad x=p^{-s},
\]

and write `e_a=c_{n,p^a}(t)`. From (3),

\[
e_0=1,
\qquad
e_a=A^a-A^{a-1}\quad(a\ge1).
\tag{8}
\]

The local join factor is

\[
K_p^{\mathrm{fresh}}(s,t)
=
\sum_{a,b\ge0} e_a\overline{e_b}\,x^{\max(a,b)}.
\tag{9}
\]

Let

\[
E_r:=\sum_{a=0}^r e_a.
\]

The fresh-prime difference telescopes exactly:

\[
\boxed{E_r=A^r.}
\tag{10}
\]

Grouping (9) by `r=max(a,b)` gives the elementary join-kernel identity

\[
K_p^{\mathrm{fresh}}
=
\sum_{r\ge0}x^r
\bigl(|E_r|^2-|E_{r-1}|^2\bigr),
\qquad E_{-1}:=0.
\tag{11}
\]

For real Mellin frequency `t`, `|A|=1`, so `|E_r|=1` for every `r`. Therefore every shell `r>=1` cancels and

\[
\boxed{
K_p^{\mathrm{fresh}}(s,t)=1
\qquad(p\nmid n).
}
\tag{12}
\]

This is stronger than a classicalization into a zeta quotient: **there is no fresh-prime Euler factor left at all**.

A finite truncation makes the cancellation equally transparent. If exponents are restricted to `0<=a,b<=R`, then (11) is already exactly `1`; no limit or analytic continuation is needed. The infinite statement only uses absolute convergence to multiply the local identities over primes.

## 4. Only parent-prime factors survive

For `p\mid n`, equation (3) gives `e_a=A^a`. Hence

\[
E_r=1+A+\cdots+A^r.
\tag{13}
\]

Using the same grouping identity (11), now with `x=p^{-s}`, gives

\[
\begin{aligned}
K_p^{\mathrm{rep}}(s,t)
&=(1-x)\sum_{r\ge0}|E_r|^2x^r\\[1mm]
&=\boxed{
\frac{1+x}{(1-Ax)(1-A^{-1}x)}
}.
\end{aligned}
\tag{14}
\]

The formula also holds at `A=1` by continuity, where it becomes `(1+x)/(1-x)^2`.

Combining (12) and (14) yields the complete frequency symbol

\[
\boxed{
K_n(s,t)
=
\prod_{p\mid n}
\frac{1+p^{-s}}
{(1-p^{-(s-it)})(1-p^{-(s+it)})},
\qquad \Re(s)>1.
}
\tag{15}
\]

The product is finite. In particular, for the shell-2 parent the entire infinite descendant lattice contributes only the single local factor at `p=2`.

Substituting (15) into (6),

\[
\boxed{
\mathcal J_n(s)
=
\frac1{2\pi}\int_{\mathbb R}
|\widehat h_n(t)|^2
\prod_{p\mid n}
\frac{1+p^{-s}}
{(1-p^{-(s-it)})(1-p^{-(s+it)})}\,dt.
}
\tag{16}
\]

Thus the cross-index join coupling creates no all-prime zeta divisor, no new zero set, and no critical-line selector. Any zeta data in the actual Prime-Circle value of (16) are inherited from the already-classified one-shell factor `|widehat h_n(t)|^2` of PC-179/PC-406/PC-407.

## 5. Why the cancellation is structural rather than accidental

The kernel in (5) is a reciprocal-LCM join kernel. Since

\[
\frac1{[m,k]^s}
=
\frac{(m,k)^s}{m^sk^s},
\tag{17}
\]

it is diagonally equivalent to a classical GCD kernel. GCD/Poisson kernels and their Hilbert-space role are already part of the prior-art boundary recorded in `SOURCES.md` through Aistleitner--Berkes--Seip, and the broader meet/join-matrix literature treats `gcd` and `lcm` as the meet and join of the divisibility lattice. No novelty is claimed for that kernel technology.

The project-specific point is the exact interaction between this classical join kernel and the **source-forced fresh-prime difference** in the PC-405 descendant law. On the prime-exponent chain the coefficient sequence (8) is the first difference of the unit-modulus phase sequence `A^r`; the join quadratic form depends on its cumulative sums `E_r`; and those cumulative sums reconstruct the phase exactly. Equation (12) is therefore an incidence/telescoping identity, not a hidden spectral phenomenon.

This also explains why PC-407 behaved differently. Its same-index energy keeps only the diagonal `m=k`, so the positive fresh-prime factor `|A-1|^2` survives. The present least-common-refinement sum includes the off-diagonal descendant pairings, and those are precisely what cancel the diagonal fresh-prime contribution.

## 6. Matched arbitrary-profile control

Let `h` be **any** element of `L^2(R_+,dx/x)` and generate synthetic descendants with exactly the universal PC-405/PC-407 operators `C_{n,m}`. Nothing in (3)--(16) uses the cyclotomic formula for `h_n`. Therefore

\[
\sum_{m,k\ge1}
\frac{\langle C_{n,m}h,C_{n,k}h\rangle}{[m,k]^s}
=
\frac1{2\pi}\int_{\mathbb R}
|\widehat h(t)|^2K_n(s,t)\,dt
\tag{18}
\]

with exactly the same finite product (15).

Hence the entire least-common-refinement architecture is source-independent. The cyclotomic source contributes only its base spectral density. Replacing that base field by a matched nonarithmetic profile preserves the cross-index cancellation and the complete conductor dependence.

## 7. Off-diagonal Mellin frequencies show the exact boundary

The cancellation uses the Hilbert pairing, which identifies the two Mellin frequencies. If one formally keeps frequencies `t` and `u` separate, the fresh-prime cumulative products are

\[
E_r(t)\overline{E_r(u)}=p^{ir(t-u)},
\]

and the local join factor becomes

\[
\boxed{
K_p^{\mathrm{fresh}}(s;t,u)
=
\frac{1-p^{-s}}
{1-p^{-(s-i(t-u))}}.
}
\tag{19}
\]

Thus even before setting `t=u`, the fresh-prime contribution is only the same universal shifted-zeta-ratio architecture already encountered in PC-406. On the canonical Hilbert diagonal `t=u`, that ratio collapses identically to `1`.

This identifies the real escape condition. A future cross-level mechanism must not merely pair parallel descendants through the canonical Hilbert/Mellin diagonal and the divisor-lattice join. It would need a source-derived operation that couples different Mellin frequencies, introduces independent angular/chord/old-new data, changes the product law, or otherwise prevents the cumulative fresh-prime difference from telescoping.

## 8. Novelty audit, falsification, and research consequence

The prior-art check found no reason to regard the `gcd/lcm` kernel or its incidence factorization as new; they are classical number-theoretic matrix structures. Nor is the generalized-Jordan fresh-prime factor new by PC-406/PC-407. The durable new project-level statement is the exact cancellation theorem (12)--(16) at their intersection: **the canonical lcm-join coupling of distinct Prime-Circle descendants removes every fresh-prime channel rather than combining them into a richer Euler product**.

The result is easy to falsify. For any fresh prime `p`, any real `t`, any `|x|<1`, directly summing

\[
\sum_{a,b\ge0}
(A^a-A^{a-1})
(\overline A^b-\overline A^{b-1})
 x^{\max(a,b)},
\]

with the `a=0` or `b=0` terms interpreted by `e_0=1`, must give `1`. Failure at any finite exponent truncation already disproves the claimed telescoping because the grouped truncation is exactly `|E_R|^2x^R+(1-x)\sum_{r<R}|E_r|^2x^r=1`. Likewise, a direct numerical double sum for a repeated parent prime must converge to (14).

The research consequence is deliberately narrow but useful. The explicit frontier left after PC-408 included **coupling distinct descendant indices before conductor summation**. The most canonical such coupling supplied by the refinement lattice itself — Hilbert pairing weighted by the least common descendant conductor — is now closed, and it fails more strongly than the one-index and same-index completions: the new prime directions annihilate each other. What remains must use a different information law, not merely a more elaborate summation over the same universal descendant semigroup.