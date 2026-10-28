# RE-278 — Product-compensator triples have a sharp quarter initial-excursion ceiling

**Status:** EXACT-DERIVED + SHARP-ARCHITECTURE-BOUND; conditional prime-source sharpness; independent adversarial review pending.

**Dependency:** RE-274 motivates the three-prime construction and its conditional packing. The algebra, optimization and prime-admissibility argument below are reconstructed independently.

Within the positive-slope, common-intercept-one architecture with three affine deletions, two affine insertions and their deletion product as the last insertion, the initial positive Robin excursion has a sharp reciprocal-height coefficient of `1/4`. Distinct labels force strict inequality; rational families approach the ceiling. Every such identity also requires deletion slope spread at least four, with equality only in a repeated-label degeneration. Thus RE-274's coefficient `1/15` is improvable **conditionally on a different specified prime-triple supply**, but cannot be improved arbitrarily inside this architecture.

This is not a bound for all balanced integer repairs, for their largest excursion at arbitrary cutoffs, or for ordinary CA states. Algebraic attainability and prime-source supply remain separate.

## 1. Exact architecture and its two moment constraints

Let `0<a<=b<=c` and `0<d<=e` be fixed real slopes, and put
\[
r=am+1,\quad s=bm+1,\quad t=cm+1,\quad
A=dm+1,\quad B=em+1,\quad P=rst,
\qquad F(x)=\frac{x}{x-1}.
\]
Consider the rational-function identity in `m`
\[
F(r)F(s)F(t)=F(A)F(B)F(P).
\tag{1}
\]
With `S=a+b+c`, `Q=ab+ac+bc`, cross multiplication shows that (1) is equivalent to
\[
de=\frac{abc}{S},\qquad d+e=\frac QS.
\tag{2}
\]
Indeed `P-1=Sm+Qm^2+abc m^3`, and (1) reduces to
`de(P-1)=abc m(dm+1)(em+1)`. Comparing coefficients proves necessity and sufficiency; no asymptotic equality is substituted for exact matching.

Use reciprocal slopes
\[
u=1/a\ge v=1/b\ge w=1/c>0,\qquad
\alpha=1/d\ge\beta=1/e>0.
\]
Then (2) becomes
\[
\alpha+\beta=u+v+w,\qquad
\alpha\beta=uv+uw+vw.
\tag{3}
\]
Hence positive real insertions exist exactly when
\[
\Delta=(u-v-w)^2-4vw\ge0,
\qquad
\alpha,\beta=\frac{u+v+w\pm\sqrt\Delta}{2}.
\tag{4}
\]
For rational deletion slopes, rational insertions exist exactly when `Delta` is a rational square. The two insertion slopes are then unique up to interchange.

## 2. Sharp spread and initial-excursion bounds

Factor the discriminant as
\[
\Delta=[u-(\sqrt v+\sqrt w)^2]
       [u-(\sqrt v-\sqrt w)^2].
\]
The second factor is strictly positive because `u>=v>=w>0`. Therefore real feasibility is equivalent to
\[
u\ge(\sqrt v+\sqrt w)^2.
\tag{5}
\]
In particular `u>=4w`, giving
\[
\boxed{c/a\ge4.}
\tag{6}
\]
Equality forces `v=w=u/4`, hence `b=c=4a` and `d=e=4a/3`. It cannot occur for distinct deletion and insertion labels.

The quadratic with roots `alpha,beta` takes values `vw>0` at `u` and `uw>0` at `v`. Condition (5) puts `u` above its vertex and `v` below its vertex. Consequently
\[
u>\alpha\ge\beta>v,
\qquad a<d\le e<b\le c.
\tag{7}
\]
Thus every feasible distinct identity in this architecture has its first insertion strictly after its first deletion; it has the positive initial excursion of RE-273, without imposing an additional sign hypothesis.

The sharp quantitative bound is
\[
\boxed{\alpha\ge\tfrac34u,
\qquad 0<1-a/d\le\tfrac14.}
\tag{8}
\]
Here is a direct proof retaining the equality case. Normalize `u=1` and write `z=v+w`, `q=vw<=z^2/4`. If `z>=1/2`, (4) gives `alpha>=(1+z)/2>=3/4`. If `z<1/2`, then
\[
\Delta-(\tfrac12-z)^2
=\tfrac34-z-4q\ge\tfrac34-z-z^2>0.
\]
Thus `sqrt(Delta)>1/2-z` and again `alpha>3/4`. Equality in (8) requires `z=1/2`, `Delta=0`, hence `v=w=1/4`. It is exactly the repeated-label case of (6). Distinct identities therefore satisfy `c/a>4` and `1-a/d<1/4`.

To identify the Robin quantity precisely, suppose a specialization has distinct prime deletions `r,s,t` and composite insertions `A,B,P`, all beyond an unchanged ordinary-prime prefix through `p`. Let `Q_source` denote that modified source, let `Delta vartheta` be its weighted counting difference from the ordinary primes, and set
\[
f(x)=\log F(x),\quad h(x)=f(x)/\log x,\qquad
E(U)=\int_p^U\Delta\vartheta(x)h'(x)\,dx.
\]
Only `r` has been deleted through the first insertion cutoff. Since `h'<0`,
\[
E(A)=\log r\,[h(r)-h(A)]>0,
\qquad
r E(A)\longrightarrow1-a/d=1-\alpha/u.
\tag{9}
\]
The limit is along any unbounded sequence of valid prime specializations of a fixed slope identity. It follows from `f(x)=1/x+O(x^-2)` and `log r/log A -> 1`. Equation (8) bounds this initial reciprocal-height coefficient; it makes no claim about all later cutoffs or scale-dependent slopes.

## 3. Rational sharpness with distinct labels

For any rational `1/2<tau<1`, choose
\[
u=1,\qquad v=\tfrac14,\qquad
w=\frac{5-2\tau-2/\tau}{4},
\qquad
\alpha=\frac{5-2\tau}{4},\quad
\beta=\frac{5-2/\tau}{4}.
\tag{10}
\]
These are positive, satisfy (3), and have
\[
0<w<v<\beta<\alpha<u.
\]
Consequently their reciprocal slopes satisfy the strict ordering
`a<d<e<b<c`. Directly,
\[
\Delta=(\tau-1/\tau)^2/4,\qquad
1-a/d=\frac{2\tau-1}{4}\uparrow\frac14,
\qquad c/a=1/w\downarrow4
\tag{11}
\]
as `tau` increases to one. Thus both bounds are sharp within distinct rational identities. The limiting identity itself has repeated deletions and insertions and is not an admissible distinct source repair.

A common positive integer multiplier of all five slopes clears their denominators without changing any ratio or the matching (2). We may therefore take `a,b,c,d,e` to be positive integers. All six labels are distinct for sufficiently large positive integer `m`, with
\[
r<A<B<s<t<P.
\tag{12}
\]
The counting path at these events is `-1,0,1,0,-1,0`, so its absolute counting budget is one. Exact Euler matching preserves the Mertens normalization under any valid finite prime-source specialization.

For example, `tau=2/3` gives integer slopes
\[
(a,b,c,d,e)=(11,44,66,12,22).
\]
On `m=210n+102`, `A` is divisible by seven and `B` by five. At `n=1`, trial division certifies
\[
D=\{3433,13729,20593\},\qquad
B_{\rm ins}=\{3745,6865,970582212601\}.
\tag{13}
\]
The exact Euler identity holds and its initial coefficient is `1/12`. This finite instance certifies neither infinitude nor a critical-budget supply.

## 4. Composite insertions do not create a local prime obstruction

For every fixed integer slope tuple from (10), choose distinct primes `ell_d,ell_e>3` with
\[
\ell_d\nmid d(d-a)(d-b)(d-c),\qquad
\ell_e\nmid e(e-a)(e-b)(e-c).
\]
All displayed factors are nonzero, so such primes exist. The Chinese remainder theorem supplies a residue `m_0` modulo `M=6 ell_d ell_e` with
\[
m_0=0\pmod6,\quad
m_0=-d^{-1}\pmod{\ell_d},\quad
m_0=-e^{-1}\pmod{\ell_e}.
\tag{14}
\]
On `m=Mn+m_0`, both affine insertions are composite for all sufficiently large `n`. Each deletion form
\[
L_x(n)=xMn+xm_0+1,\qquad x\in\{a,b,c\},
\tag{15}
\]
is primitive. A prime dividing `x` cannot divide its intercept. For primes dividing `M`, the intercept is one modulo two and three; modulo either chosen prime it is nonzero by the excluded slope differences. This proves primitivity at every possible divisor of its slope.

The three forms are locally admissible together. At two and three all are one. At the chosen primes all are nonzero. At any other prime `ell>3`, each primitive form excludes at most one residue class, leaving at least one of the `ell` classes. This is a proof of admissibility, not simultaneous primality.

## 5. Conditional critical-budget consequence and exact limitation

Fix one rational `tau` and one progression (14). Suppose its particular triple (15) satisfies the quantitative hypothesis
\[
\#\{n\in[x,(1+\eta)x]:L_a(n),L_b(n),L_c(n)
\text{ all prime}\}\gg_\eta x/(\log x)^3
\tag{H_tau}
\]
for every fixed `eta>0` and all sufficiently large `x`. This is the same type of unproved prescribed-tuple input as RE-274, for different forms; RE-274's hypothesis does not imply it.

Under `H_tau`, let `p` tend to infinity through ordinary primes. For every prefix `T(p)>=p` with `T/p -> 1` and integer budget
`1<=K=o(p/(log p)^3)`, one can select `K` disjoint repairs such that all alterations exceed `T`, exact Mertens normalization and eventual count balance hold, the maximum absolute count is `K`, and at one common first-insertion cutoff
\[
\boxed{E_Q(U)=\left(\frac{2\tau-1}{4}+o(1)\right)\frac Kp.}
\tag{16}
\]
For completeness, restrict the first deletion to `[(1+eta)p,(1+2eta)p]`. For each sufficiently small fixed `eta`, all six bands in (12) are separated. Hypothesis `H_tau` supplies `gg_eta p/(log p)^3` parameters, more than `K`. Every label is strictly increasing in the parameter inside its band; the separated bands ensure all chosen labels are distinct across repairs. Multiplying (1) preserves exact matching. The count passes from zero to `-K`, then to `K`, back to `-K`, and finally zero, without leaving that interval.

Choose successively smaller fixed accuracies only after their onset thresholds. This standard diagonal choice gives `r_j=p+o(p)` and `A_j=(d/a)p+o(p)`, while keeping the prefix condition. At `U=min_j A_j`, all first deletions and no other events contribute to the integral, so
\[
E_Q(U)=\sum_j[f(r_j)-h(U)\log r_j]
=(1-a/d+o(1))K/p.
\]
The error is uniform over the chosen labels; this proves (16) without a prime theorem in a prescribed shrinking interval. If `K~lambda sqrt(p)/log p`, the normalized limit is `lambda(2tau-1)/4`.

Thus any fixed coefficient strictly below `1/4` can be exceeded by an appropriate rational shape, **if that shape's own `H_tau` holds**. No single fixed distinct shape attains `1/4`; an exact limiting critical constant would require an additional sequence of prime-supply hypotheses and a further diagonal argument, which is not asserted here. Neither the algebra nor local admissibility supplies even one unbounded prime sequence.

## 6. Audit, prior art and research boundary

The proof consists of coefficient comparison, the quadratic discriminant, the explicit inequality in Section 2, and CRT; no computation is needed for it. Supplementary exact rational-arithmetic checks tested (10), (1), all label orderings and the six-event counting path for `tau=k/(k+1)`, `2<=k<=101`, after clearing denominators, at `1<=m<=20` (2000 identities). A separate exhaustive slope grid `1<=a<=20`, `a<=b<=60`, `b<=c<=80` checked (6) whenever the discriminant was nonnegative; its 331 rational-root cases also passed (7)--(8), including the unique equality geometry. Trial division for the concrete progression in (13), `0<=n<1000`, found 38 prime triples. Those finite checks neither establish `H_tau` nor independently audit the proof.

The algebraic mechanism is classical coefficient matching and quadratic factorization, with rational parametrization of a conic. No new general theorem about moments, discriminants or Diophantine parametrization is claimed. Targeted prior-art comparison covered polynomial Euler/totient-factor identities, rational discriminants, Chernick-type polynomial products and prescribed affine prime tuples; failure to locate this exact optimization is not a global novelty claim.

Bernd C. Kellner, [*On primary Carmichael numbers*, Integers **22** (2022), A38](https://math.colgate.edu/~integers/w38/w38.pdf), Section 4 and Theorem 4.2, provides neighboring prior art for polynomial universal forms conditioned on simultaneous primality. It does not supply this identity, its optimization, or a prime theorem; no Carmichael property is asserted here. Ben Green and Terence Tao, [*Linear equations in primes*, Annals of Mathematics **171** (2010), 1753--1850](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf), Conjecture 1.4 and the subsequent one-variable discussion, provide the conjectural prime-counting comparison for `H_tau`. Finite-complexity affine prime results do not prove this prescribed one-variable triple input. Nor does a theorem selecting unspecified primes from a larger panel select (15).

The line-specific delta is a complete real/rational feasibility test and a sharp initial-excursion optimization for the exact positive family underlying RE-274, with a proof that integrality and composite insertions do not destroy rational near-extremizers. The ceiling identifies an architecture limit; the explicit near-extremizers improve the conditional coefficient without improving the unproved prime-supply boundary.

Different affine intercepts, a last insertion other than the deletion product, rational or nonlinear small insertions, more labels, and global extrema over cutoffs remain outside the theorem. These are synthetic factors `F(B)`, not the ordinary divisor-sum factors of composite integers. There is no CA realization, selected ordinary-prime signed-tail estimate, Robin counterexample or RH conclusion.
