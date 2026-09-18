# PL-358 — Ordinary multiplicativity tensorizes `H^2` but leaves critical-strip zeros locally programmable

**Evidence:** `CLASSICAL-BOHR+EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-357`.

`PL-357` shows that complete multiplicativity is too rigid in the standard Hardy space of Dirichlet series: it collapses the coefficient vector to a reproducing kernel and is automatically zero-free throughout the native evaluation half-plane `Re(s)>1/2`. The immediate weaker law is ordinary multiplicativity,

\[
a_{mn}=a_ma_n\qquad ((m,n)=1),
\tag{1}
\]

with the prime-power strings `a_{p^k}` left free. This does **not** produce an intermediate zero-sensitive family. In `\mathscr H^2`, ordinary multiplicativity factorizes the vector into independent one-prime Hardy factors, and every zero in the native half-plane is exactly a zero of one of those factors. Moreover, any prescribed point of `1/2<Re(s)<1` can be made a zero of a multiplicative `\mathscr H^2` Dirichlet series with `|a_n|<=1` and `a_p\ne0` for every prime.

Thus complete and ordinary multiplicativity fail in opposite directions: complete multiplicativity forbids native zeros, while ordinary multiplicativity lets a zero be planted at a single prime without any cross-prime arithmetic cancellation.

## 1. Exact tensor factorization

Let

\[
F(s)=\sum_{n\ge1}a_n n^{-s}\in\mathscr H^2,
\qquad a_1=1,
\qquad \sum_n|a_n|^2<\infty,
\tag{2}
\]

and assume (1). For every prime define

\[
f_p(z)=\sum_{k\ge0}a_{p^k}z^k,
\qquad a_{p^0}=1.
\tag{3}
\]

Unique factorization gives

\[
a_n=\prod_p a_{p^{v_p(n)}}.
\tag{4}
\]

For each finite prime set `P`,

\[
\sum_{\operatorname{supp}v(n)\subseteq P}|a_n|^2
=
\prod_{p\in P}\left(\sum_{k\ge0}|a_{p^k}|^2\right).
\tag{5}
\]

Increasing `P` to all primes yields

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

Under the classical Bohr transform this is the restricted tensor product

\[
\boxed{\mathcal BF(z)=\prod_p f_p(z_p).}
\tag{7}
\]

The tensor/Bohr structure is classical. The route-level point is that ordinary multiplicativity imposes no relation between the shapes of the one-variable factors `f_p`.

## 2. Every native zero is local

Fix `s=\sigma+it` with `\sigma>1/2`. Cauchy--Schwarz gives

\[
\sum_{n\ge1}|a_n|n^{-\sigma}
\le
\|F\|_{\mathscr H^2}\,\zeta(2\sigma)^{1/2}<\infty.
\tag{8}
\]

Hence the ordinary multiplicative Euler rearrangement is legitimate at this `s`:

\[
F(s)=\prod_pF_p(s),
\qquad
F_p(s):=f_p(p^{-s})
=
\sum_{k\ge0}a_{p^k}p^{-ks}.
\tag{9}
\]

No analytic continuation is being used. In addition,

\[
\sum_p|F_p(s)-1|
\le
\sum_p\sum_{k\ge1}|a_{p^k}|p^{-k\sigma}<\infty.
\tag{10}
\]

Therefore, if all local factors are nonzero, the infinite product converges to a nonzero value. Conversely, one zero local factor forces the product to vanish. Thus

\[
\boxed{
F(s)=0
\iff
F_p(s)=0\text{ for some prime }p,
\qquad \Re s>\tfrac12.
}
\tag{11}
\]

So within the whole half-plane naturally visible to standard `\mathscr H^2`, the zero set of an ordinarily multiplicative vector is only the union of pullbacks of independent one-coordinate zero sets.

Complete multiplicativity is the special case

\[
f_p(z)=(1-a_pz)^{-1},
\tag{12}
\]

whose local factors have no zeros. This recovers `PL-357` and pinpoints the missing rigidity: it is exactly the unconstrained prime-power strings of ordinary multiplicativity.

## 3. Bounded coefficients still allow a zero anywhere in the critical strip

Let

\[
s_0=\sigma+it,
\qquad \frac12<\sigma<1,
\tag{13}
\]

and set

\[
r=2^{-\sigma}\in(1/2,1/\sqrt2),
\qquad \theta=t\log2.
\tag{14}
\]

Because `r/(1-r)>1`, there is a least `m>=2` such that

\[
\sum_{k=1}^m r^k\ge1.
\tag{15}
\]

Take

\[
c_k=1\quad(1\le k<m),
\qquad
c_m=\frac{1-\sum_{k=1}^{m-1}r^k}{r^m}.
\tag{16}
\]

Minimality gives `0<c_m<=1` and

\[
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

Since `2^{-s_0}=re^{-i\theta}`,

\[
F_2(s_0)
=1+\sum_{k=1}^m a_{2^k}2^{-ks_0}
=1-\sum_{k=1}^m c_kr^k
=0.
\tag{19}
\]

This local factor is a finite polynomial, but the global example can still retain every prime direction. For each odd prime `q`, set

\[
a_q=q^{-2},
\qquad a_{q^k}=0\quad(k\ge2),
\tag{20}
\]

and extend multiplicatively across coprime prime powers. Then every prime has `a_p\ne0`, every coefficient obeys `|a_n|<=1`, and

\[
\|F\|_{\mathscr H^2}^2
=
\left(1+\sum_{k=1}^m c_k^2\right)
\prod_{q\text{ odd prime}}(1+q^{-4})<\infty.
\tag{21}
\]

Hence `F` is a multiplicative `\mathscr H^2` Dirichlet series with all prime directions active and

\[
\boxed{F(s_0)=0.}
\tag{22}
\]

Since `s_0` was arbitrary, ordinary multiplicativity plus the natural size bound `|a_n|<=1` imposes no zero-location restriction anywhere in `1/2<Re(s)<1`.

The same bound does recover the classical Euler-product zero-free regime for `Re(s)>1`: there

\[
\left|\sum_{k\ge1}a_{p^k}p^{-ks}\right|
\le
\frac{p^{-\sigma}}{1-p^{-\sigma}}<1,
\qquad \sigma>1,
\tag{23}
\]

and the product converges absolutely. Ordinary multiplicativity therefore retains the familiar `Re(s)=1` barrier but supplies no mechanism that moves rigidity to `Re(s)=1/2`.

## 4. Prior-art and novelty audit

Source 1 (Hedenmalm--Lindqvist--Seip) supplies the classical `\mathscr H^2`/infinite-polydisk framework. The Euler factorization of an absolutely convergent Dirichlet series with multiplicative coefficients is classical, and (5)--(11) are direct consequences of unique factorization, monotone convergence, and absolute convergence.

A targeted literature audit on 18 September 2026 searched Hardy spaces of Dirichlet series, multiplicative coefficient sequences, Euler products, local factors, and zero behavior. It recovered the standard Bohr/Hardy and multiplier literature, but nothing that justifies a novelty claim for the elementary construction (13)--(22). **No theorem-level novelty is claimed.** The durable result is the exact negative consequence for the live route after `PL-356` and `PL-357`.

This is distinct from `PL-003`. Helson-zeta flexibility changes completely multiplicative prime phases and studies continuation phenomena. Here the law is ordinary multiplicativity inside the native `\mathscr H^2` evaluation half-plane, and a single prime-power factor already creates an arbitrary critical-strip zero with no continuation step at all.

## 5. Adversarial boundaries

The construction deliberately exploits prime-power freedom; a stronger source law that constrains each complete string `(a_{p^k})_{k>=0}` can escape it. Although every prime direction is active, most higher powers at odd primes vanish, so a law requiring nonzero or coupled higher prime powers is not ruled out. Equation (11) is only a statement in `Re(s)>1/2`, where absolute convergence follows from `\mathscr H^2`; it says nothing about a separately supplied meromorphic continuation. No functional equation, archimedean factor, or other global coupling is imposed, and those are precisely plausible ways to destroy the local programmability.

The coefficient bound is essential to the stress test: this is not an artifact of using a huge coefficient to cancel the constant term. The negative result survives `|a_n|<=1` and full degree-one prime support.

## Research consequence

The nonlinear source-law search now has two sharp endpoints. Ordinary multiplicativity gives independent local factors and programmable critical-strip zeros; complete multiplicativity gives reproducing kernels and no native zeros. A viable intermediate family must therefore constrain prime-power factors enough to prevent one-prime zero programming **without** collapsing them to the geometric factors of complete multiplicativity.

Equivalently, the surviving target is a genuine cross-degree or global compatibility law--for example one involving completion, the functional equation, Möbius/prime-power coupling, or a target-relative Nyman/Weil condition--whose effect survives the completion topology and cannot be localized to one prime coordinate.