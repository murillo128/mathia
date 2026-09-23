# PC-410 — all join-only Mellin-diagonal descendant couplings cancel fresh primes

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the full class of descendant couplings whose two conductor labels enter only through their least common refinement and whose radial action is diagonal in Mellin frequency. This strictly strengthens PC-409: the fresh-prime cancellation does **not** depend on the reciprocal-lcm weight `[m,k]^{-s}`, multiplicativity of the weight, positivity, an Euler product, or even a Dirichlet parameter. It does **not** cover weights depending separately on `m` and `k`, operators mixing distinct Mellin frequencies, source-derived angular/chord/old-new data, nonlinear products that change the state space, or constructions whose effective complexity grows with conductor.

PC-409 showed that the canonical Gram completion

\[
\sum_{m,k\ge1}\frac{\langle h_{nm},h_{nk}\rangle}{[m,k]^s}
\]

annihilates every prime not already dividing the parent shell `n`. Its proof used an Euler factorization, leaving open whether the cancellation was special to the reciprocal-lcm kernel or to multiplicative weights. The answer is stronger: it is a pointwise incidence identity on the prime-exponent chain. Consequently **every** common-refinement-only Mellin-diagonal coupling has the same fresh-prime annihilation.

## 1. Universal descendant coefficients

Keep the PC-405/PC-407 descendant law at a fixed parent `n>1`. In Mellin variables,

\[
\widehat{h_{nm}}(t)=c_{n,m}(t)\widehat h_n(t),
\]

with multiplicative coefficients and prime-power factors

\[
c_{n,p^a}(t)=
\begin{cases}
1,&a=0,\\[1mm]
p^{iat},&a\ge1,\ p\mid n,\\[1mm]
p^{i(a-1)t}(p^{it}-1),&a\ge1,\ p\nmid n.
\end{cases}
\tag{1}
\]

Let `omega_L(t)` be an arbitrary scalar weight attached to the common refinement `L=[m,k]`. It may be nonmultiplicative in `L` and may depend arbitrarily on the Mellin frequency. Whenever the double series is absolutely convergent, define its frequencywise coupling by

\[
\boxed{
K_{n,\omega}(t)
:=
\sum_{m,k\ge1}
c_{n,m}(t)\overline{c_{n,k}(t)}\,
\omega_{[m,k]}(t).
}
\tag{2}
\]

This includes PC-409 by taking `omega_L=L^{-s}`, but also includes any family of dilation-commuting operators `T_L` whose Mellin symbols are `omega_L(t)` and are selected only by the least common descendant level.

## 2. Exact fresh-prime max-shell identity

Fix a fresh prime `p\nmid n`. Separate the `p`-parts

\[
m=p^a m_0,\qquad k=p^b k_0,
\qquad p\nmid m_0k_0,
\]

and put

\[
L=[m_0,k_0],\qquad A=p^{it}.
\]

From (1), the fresh-prime coefficient sequence is

\[
e_0=1,
\qquad
e_a=A^a-A^{a-1}\quad(a\ge1).
\tag{3}
\]

Its cumulative sums telescope:

\[
E_r:=\sum_{a=0}^r e_a=A^r.
\tag{4}
\]

The contribution of all `p`-exponents over this fixed `p`-free pair is

\[
S_{p,L}(t)
=
\sum_{a,b\ge0}
e_a\overline{e_b}\,
\omega_{p^{\max(a,b)}L}(t).
\tag{5}
\]

Group by `r=max(a,b)`. The coefficient multiplying the entire `r`-th max shell is

\[
\sum_{\max(a,b)=r}e_a\overline{e_b}
=
|E_r|^2-|E_{r-1}|^2,
\qquad E_{-1}:=0.
\tag{6}
\]

For real Mellin frequency `t`, `|A|=1`, hence `|E_r|=1` for every `r>=0`. Therefore

\[
|E_0|^2-|E_{-1}|^2=1,
\qquad
|E_r|^2-|E_{r-1}|^2=0\quad(r\ge1),
\]

and the whole fresh-prime tower collapses to

\[
\boxed{
S_{p,L}(t)=\omega_L(t).
}
\tag{7}
\]

Equation (7) is the key strengthening of PC-409. No property of `omega` was used except that all pairs with the same maximum exponent see the same common-refinement weight. In particular, `omega` need not be multiplicative, monotone, positive, rational, Dirichlet-generated, or analytically continued.

The identity is already exact at every finite exponent cutoff. If `0<=a,b<=R`, grouping by the maximum gives the same result because every shell `r>=1` has coefficient zero. Thus the cancellation is algebraic rather than asymptotic.

## 3. Global collapse to the parent-prime semigroup

Under absolute convergence, equation (7) may be applied successively to any finite set of fresh primes. Exhausting the fresh primes and using absolute summability to pass to the limit removes every prime not dividing `n`. Hence

\[
\boxed{
K_{n,\omega}(t)
=
\sum_{\substack{m,k\ge1\\
\operatorname{rad}(mk)\mid\operatorname{rad}(n)}}
\left(\frac{m}{k}\right)^{it}
\omega_{[m,k]}(t).
}
\tag{8}
\]

For the surviving labels all prime divisors already divide the parent, so (1) reduces to the pure phases `c_{n,m}(t)=m^{it}`. The infinite descendant tree has therefore lost **all fresh-prime directions before any further spectral or conductor analysis begins**.

For the shell-2 parent, (8) is especially restrictive:

\[
K_{2,\omega}(t)
=
\sum_{a,b\ge0}
2^{i(a-b)t}\,
\omega_{2^{\max(a,b)}}(t).
\tag{9}
\]

Every odd-prime descendant direction cancels identically. A zeta or all-prime structure can remain only if it was already inserted into the scalar family `omega_L(t)` independently of the Prime-Circle descendant data. Such an insertion is an external spectral wrapper, not a source-forced bridge under the research mandate.

## 4. Matched arbitrary-profile control

The proof does not use the cyclotomic formula for the parent field. Let `h` be any profile in the Mellin Hilbert space and generate descendants with the same universal PC-405 operators. A common-refinement-only Mellin-diagonal quadratic form has integrand

\[
|\widehat h(t)|^2 K_{n,\omega}(t),
\]

and equations (7)--(8) remain unchanged. Replacing the arithmetic parent by a matched nonarithmetic profile therefore preserves the entire fresh-prime cancellation.

This is a source-blindness control stronger than the one in PC-409: the cancellation is not a special property of one chosen conductor kernel. It is forced jointly by (i) the universal fresh-prime first-difference cocycle and (ii) dependence on the two descendant labels only through their join in the divisibility lattice.

## 5. Exact escape boundary: Mellin mixing survives

The proof also identifies precisely where this no-go stops. Keep two Mellin frequencies `t` and `u` distinct. Then the fresh-prime cumulative products are

\[
E_r(t)\overline{E_r(u)}
=p^{ir(t-u)},
\tag{10}
\]

so the max-shell coefficient is

\[
\boxed{
p^{ir(t-u)}-p^{i(r-1)(t-u)}}
\qquad(r\ge1),
\tag{11}
\]

which is generically nonzero. Thus an operator genuinely mixing Mellin frequencies can retain fresh-prime information even if it is organized by common refinement. PC-409's shifted-zeta ratio is the special reciprocal-lcm realization of this off-diagonal fact; the diagonal `t=u` is exactly where every positive max shell disappears.

Other constructions outside (2) are equally clear: a kernel `W_{m,k}` that depends on the two labels separately rather than only on `[m,k]`; a source-derived angular/chord/old-new coupling that is not encoded by the descendant dilation cocycle; nonlinear interactions changing the descendant state space; or an architecture whose rank/depth/degree grows with conductor. Those remain legitimate frontier directions.

## 6. Prior-art and novelty audit

The abstract matrix technology is classical. `gcd`/`lcm` are the meet and join operations of the divisibility lattice, and general meet/join matrices and their incidence factorizations are treated, for example, by Korkee and Haukkanen, *On a general form of join matrices associated with incidence functions*, Aequationes Math. 75 (2008), doi:10.1007/s00010-007-2922-6, and by Mattila and Haukkanen, *On the positive definiteness and eigenvalues of meet and join matrices*, Discrete Math. 326 (2014), 9--19, doi:10.1016/j.disc.2014.02.014. No novelty is claimed for max/join kernels or their incidence algebra.

Nor does (8) produce an RH criterion by itself. It gives no gamma factor, functional equation, critical-line selector, or zero-generating operator. Its significance is negative and project-specific: the Prime-Circle descendant cocycle turns **every** Mellin-diagonal join-only coupling into a projector that deletes all new prime directions. PC-409 was therefore not an accident of the kernel `[m,k]^{-s}`; it was the first example of a considerably broader obstruction.

A direct falsification test is immediate. Pick any fresh prime `p`, any real `t`, any finite `R`, and arbitrary numbers `w_0,...,w_R`. Then

\[
\sum_{0\le a,b\le R}
e_a\overline{e_b}\,w_{\max(a,b)}=w_0
\tag{12}
\]

with `e_a` from (3). A single counterexample disproves the theorem. Conversely, (4)--(6) prove (12) coefficient by coefficient for arbitrary `w_r`.

The research consequence is sharp. PC-409 left "arbitrary cross-index weights" open; after PC-410 that phrase must be narrowed. **Changing the lcm weight while preserving join-only dependence and Mellin diagonality cannot help.** Any surviving distinct-descendant-index mechanism must break at least one of those two information constraints rather than merely choose a more elaborate function of the common refinement.