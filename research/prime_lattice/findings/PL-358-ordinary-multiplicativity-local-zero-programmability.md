# PL-358 — Ordinary multiplicativity tensorizes `H^2` but leaves critical-strip zeros locally programmable

**Evidence:** `CLASSICAL-BOHR+EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-357`.

`PL-357` shows that complete multiplicativity is too rigid in the standard Hardy space of Dirichlet series: it collapses the coefficient vector to a reproducing kernel and is automatically zero-free throughout the native evaluation half-plane `Re(s)>1/2`. The immediate weaker arithmetic law is ordinary multiplicativity,

\[
a_{mn}=a_ma_n\qquad ((m,n)=1),
\tag{1}
\]

with the prime-power strings `a_{p^k}` left free. This does not give an intermediate zero-sensitive family. In `\mathscr H^2`, ordinary multiplicativity factorizes the whole problem into independent one-prime Hardy factors, and every zero in the native half-plane is exactly a zero of one of those local factors. In particular, **any prescribed point of the critical strip can be made a zero of a multiplicative Dirichlet polynomial whose coefficients satisfy `|a_n|<=1` and whose degree-one coefficient is nonzero at every prime.**

Thus the strongest naive weakening of complete multiplicativity has the opposite defect from `PL-357`: complete multiplicativity forbids all native zeros, while ordinary multiplicativity allows a zero to be planted locally at one prime without requiring any cross-prime arithmetic cancellation.

## 1. Exact tensor factorization of a multiplicative `\mathscr H^2` vector

Let

\[
F(s)=\sum_{n\ge1}a_n n^{-s}\in\mathscr H^2,
\qquad
a_1=1,
\qquad
\sum_n|a_n|^2<\infty,
\tag{2}
\]

and assume (1). For each prime define the one-variable local factor

\[
f_p(z)=\sum_{k\ge0}a_{p^k}z^k,
\qquad a_{p^0}=1.
\tag{3}
\]

Unique factorization and ordinary multiplicativity give

\[
a_n=\prod_p a_{p^{v_p(n)}}.
\tag{4}
\]

For every finite set `P` of primes,

\[
\sum_{\operatorname{supp}v(n)\subseteq P}|a_n|^2
=
\prod_{p\in P}\left(\sum_{k\ge0}|a_{p^k}|^2\right).
\tag{5}
\]

Increasing `P` to all primes and using monotone convergence yields the exact norm identity

\[
\boxed{
\|F\|_{\mathscr H^2}^2
=
\prod_p\|f_p\|_{H^2(\mathbb D)}^2
=
\prod_p\left(\sum_{k\ge0}|a_{p^k}|^2\right)<\infty.
}
\tag{6}
\]

Under the classical Bohr transform, this is the restricted tensor product

\[
\boxed{
\mathcal BF(z)=\prod_p f_p(z_p).
}
\tag{7}
\]

This is standard tensor-product/Bohr structure, not a novelty claim. The point relevant to the research line is that ordinary multiplicativity imposes no relation between the shapes of the one-variable factors `f_p`.

## 2. In the native half-plane, every zero is local

Fix `s=\sigma+it` with `\sigma>1/2`. Since `F\in\mathscr H^2`, Cauchy--Schwarz gives

\[
\sum_{n\ge1}|a_n|n^{-\sigma}
\le
\left(\sum_n|a_n|^2\right)^{1/2}
\zeta(2\sigma)^{1/2}
<\infty.
\tag{8}
\]

Therefore the ordinary multiplicative Euler rearrangement is legitimate at this `s`:

\[
F(s)
=
\prod_p F_p(s),
\qquad
F_p(s):=f_p(p^{-s})
=
\sum_{k\ge0}a_{p^k}p^{-ks}.
\tag{9}
\]

There is no analytic-continuation step here; (9) is used only where (8) proves absolute convergence. Moreover,

\[
\sum_p|F_p(s)-1|
\le
\sum_p\sum_{k\ge1}|a_{p^k}|p^{-k\sigma}
<\infty.
\tag{10}
\]

Hence, if every `F_p(s)` is nonzero, the infinite product in (9) converges to a nonzero number. Conversely, a zero local factor plainly makes `F(s)=0`. Thus

\[
\boxed{
F(s)=0
\iff
F_p(s)=0\text{ for at least one prime }p,
\qquad \Re s>\tfrac12.
}
\tag{11}
\]

So ordinary multiplicativity does not turn the prime lattice into a global zero constraint. In the entire half-plane where the standard `\mathscr H^2` topology can evaluate the Dirichlet series, its zeros are just pullbacks of independent one-coordinate zero sets.

Complete multiplicativity is the special case

\[
f_p(z)=(1-a_pz)^{-1},
\tag{12}
\]

and these local factors have no zeros, recovering the obstruction of `PL-357`. Ordinary multiplicativity replaces the geometric factor (12) by a free one-variable Hardy factor, immediately restoring local zero freedom.

## 3. Every critical-strip point is programmable with bounded coefficients

The local freedom is strong even under a natural arithmetic-size control. Let

\[
s_0=\sigma+it,
\qquad
\frac12<\sigma<1,
\tag{13}
\]

and put

\[
r=2^{-\sigma}\in(1/2,1/\sqrt2),
\qquad
\theta=t\log2.
\tag{14}
\]

Because `r/(1-r)>1`, there is a least integer `m>=2` with

\[
\sum_{k=1}^m r^k\ge1.
\tag{15}
\]

Set

\[
c_k=1\quad(1\le k<m),
\qquad
c_m=
\frac{1-\sum_{k=1}^{m-1}r^k}{r^m}.
\tag{16}
\]

Minimality of `m` gives

\[
0<c_m\le1,
\qquad
\sum_{k=1}^m c_kr^k=1.
\tag{17}
\]

Define the `2`-local coefficients by

\[
a_{2^k}=-c_ke^{ik\theta}\quad(1\le k\le m),
\qquad
a_{2^k}=0\quad(k>m).
\tag{18}
\]

Then

\[
\begin{aligned}
F_2(s_0)
&=1+\sum_{k=1}^m a_{2^k}2^{-ks_0}\\
&=1-\sum_{k=1}^m c_ke^{ik\theta}r^ke^{-ik\theta}\\
&=1-\sum_{k=1}^m c_kr^k
=0.
\end{aligned}
\tag{19}
\]

To prevent this from being dismissed as a rank-one support artifact, activate every other prime as well. For each odd prime `q`, set

\[
a_q=q^{-2},
\qquad
a_{q^k}=0\quad(k\ge2),
\tag{20}
\]

and extend all coefficients multiplicatively across coprime prime powers. Then every prime has `a_p\ne0`, every coefficient satisfies

\[
|a_n|\le1,
\tag{21}
\]

and the exact norm factorization gives

\[
\|F\|_{\mathscr H^2}^2
=
\left(1+\sum_{k=1}^m c_k^2\right)
\prod_{q\text{ odd prime}}(1+q^{-4})
<\infty.
\tag{22}
\]

Thus `F` is a genuine multiplicative `\mathscr H^2` Dirichlet series with all prime directions active, bounded coefficients, and

\[
\boxed{F(s_0)=0.}
\tag{23}
\]

Since `s_0` was arbitrary in `1/2<Re(s)<1`, ordinary multiplicativity plus `|a_n|<=1` places **no zero-location restriction anywhere in the critical strip**.

The coefficient bound is not cosmetic. In `Re(s)>1`, the same bound yields the classical absolutely convergent Euler-product zero-free regime: for every prime,

\[
\left|\sum_{k\ge1}a_{p^k}p^{-ks}\right|
\le
\frac{p^{-\sigma}}{1-p^{-\sigma}}<1,
\qquad \sigma>1,
\tag{24}
\]

and the product converges absolutely. Thus the ordinary multiplicative law naturally remembers the familiar boundary at `Re(s)=1`; it does not by itself move any rigidity to `Re(s)=1/2`.

## 4. Prior-art and novelty audit

The ambient ingredients are classical. Source 1 (Hedenmalm--Lindqvist--Seip) identifies `\mathscr H^2` with square-summable Dirichlet coefficients and with Hardy `H^2` on the infinite prime polydisk/character space. The factorization of an absolutely convergent Dirichlet series with ordinary multiplicative coefficients into prime-power Euler factors is classical, and (5)--(11) are direct consequences of unique factorization, monotone convergence, and absolute convergence.

A targeted literature audit on 18 September 2026 searched Hardy spaces of Dirichlet series, multiplicative coefficient sequences, Euler products, local factors, and zero behavior. It recovered the standard Bohr/Hardy framework and general multiplier literature, but no evidence warranting a novelty claim for the elementary local construction (13)--(23). **No theorem-level novelty is claimed.** The durable content is the exact route restriction relative to `PL-356` and `PL-357`: ordinary multiplicativity is provably too weak, even with bounded coefficients and every prime direction present.

This finding is also distinct from `PL-003`. Helson-zeta flexibility changes completely multiplicative prime phases and studies continuation beyond the native Euler-product region. Here the coefficient law is ordinary multiplicativity inside the standard `\mathscr H^2` evaluation half-plane, and the obstruction is stronger in a different sense: a single prime-power factor can already plant an arbitrary critical-strip zero without any continuation at all.

## 5. Adversarial boundaries

1. **The construction exploits prime-power freedom.** This is exactly the distinction from complete multiplicativity. A proposed intermediate law that rigidly constrains each prime-power string may escape the example.

2. **The zero is locally generated, not an analogue of a Riemann zero mechanism.** That is the negative conclusion: ordinary multiplicativity fails to force zeros to be global cancellation phenomena.

3. **All prime directions are active, but most higher prime powers are not.** Requiring nonzero or structured coefficients at every `p^k` would be a genuinely stronger condition and is not ruled out here.

4. **The statement is confined to the native `\mathscr H^2` half-plane.** Equation (11) uses absolute convergence obtained from `\sigma>1/2`; it says nothing about a separately supplied meromorphic continuation to the left.

5. **The coefficient bound `|a_n|<=1` is retained.** Therefore the counterexample is not an artifact of allowing a huge coefficient to cancel the constant term at one prime.

6. **No functional equation or archimedean coupling is imposed.** Such global input is precisely the kind of additional relation that could prevent independent local zero programming.

## Research consequence

The nonlinear escape left after `PL-356` now has two exact endpoints:

\[
\text{ordinary multiplicativity}
\quad\Longrightarrow\quad
\text{independent local factors and programmable critical-strip zeros},
\]

whereas

\[
\text{complete multiplicativity}
\quad\Longrightarrow\quad
\text{reproducing kernels and no native zeros}.
\]

So the useful target is no longer merely "an infinite nonlinear multiplicative relation." A viable source-forced family must constrain the prime-power factors enough to prevent one-prime zero programming **without** collapsing them to the geometric kernel factors of complete multiplicativity. Equivalently, it needs a nontrivial cross-degree or global compatibility law--potentially involving completion, the functional equation, Möbius/prime-power coupling, or a target-relative Nyman/Weil condition--whose effect survives the completion topology and cannot be localized to one prime coordinate.