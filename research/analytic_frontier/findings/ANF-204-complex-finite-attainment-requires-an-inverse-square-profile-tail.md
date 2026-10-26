# ANF-204 — Complex finite attainment requires an inverse-square profile tail

**Status:** EXACT-DERIVED + COMPLEX-MULTISET + NECESSARY-TAIL-CONDITION + POISSON-SMOOTHED-POSITIVITY + NONATTAINMENT. For every dominated even profile with nonnegative real Fourier transform, finite attainment of the unrestricted complex Montgomery--Taylor floor at even one positive amplitude forces an inverse-square Fourier tail. If that tail bound fails, every finite conjugation-invariant configuration is strictly improved by arbitrarily distant translated copies, and every minimizing sequence has cardinality tending to infinity. This removes the special sparse-peak hypothesis of ANF-203. It does not prove that the tail condition suffices for complex attainment or settle the unrestricted triangular-notch envelope.

## Object and exact implication

Use \(\widehat f(x)=\int_{\mathbb R}f(u)e^{-2\pi iux}\,du\), with
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,
\]
\[
K(z)=\frac{\cos(\pi z)-a z\sin(\pi z)}{1-2\pi^2z^2},
\qquad a=\sqrt2\pi\cot(1/\sqrt2),
\tag{1}
\]
continuing the removable points. Freeze an integrable real even profile
\[
0\le\phi\le J_0,\qquad \Phi=\widehat\phi\ge0\quad\hbox{on }\mathbb R.
\tag{2}
\]
In particular, \(\phi\) is supported in \([-1,1]\). No regularity,
prescribed decay, or positive exposure at a source zero is assumed.

For a nonempty finite multiset \(W=\overline W\), counting all entries
with their positive integer multiplicities, put
\[
N=|W|,\quad L(W)=2N-\sigma(W),\quad
S_W(u)=\sum_{z\in W}e^{-2\pi iuz},\quad
E_f(W)=\int f(u)|S_W(u)|^2\,du,
\]
\[
Q_t(W)=\frac{E_{J_0-t\phi}(W)}{L(W)},\qquad
q_m(t)=\inf_{\substack{W=\overline W\\1\le|W|\le m}}Q_t(W),\qquad
q_\infty(t)=\inf_{W=\overline W,\ 0<|W|<\infty}Q_t(W).
\tag{3}
\]
Here \(\sigma\) counts distinct simple real sites only. Lamzouri's
inequality gives \(E_{J_0}(W)\ge L(W)>0\), and hence
\(Q_t(W)\ge1-t>0\) for \(0<t<1\).

The necessary condition is
\[
\boxed{
\exists\,t\in(0,1),\ W:\ Q_t(W)=q_\infty(t)
\quad\Longrightarrow\quad
\sup_{x\in\mathbb R}(1+x^2)\Phi(x)<\infty.
}
\tag{4}
\]
In fact, the weaker premise that one finite \(W\) cannot be improved
by any sufficiently distant duplicate already forces the same tail.
Contrapositively, if the supremum in (4) is infinite, then
\[
\boxed{
\forall t\in(0,1),\ \forall W,\ \forall R_0>\operatorname{diam}(\Re W),
\quad\exists R>R_0:\quad
Q_t(W\cup(W+R))<Q_t(W).
}
\tag{5}
\]
The translation may depend on the profile, amplitude, configuration and
requested distance. Unlike ANF-203's special construction, this theorem
does not supply a common prescribed frequency sequence or an asymptotic
size of the improvement.

## A positive Cauchy mixture for the damped complex source

Let
\[
P_c(x)=\frac{c}{\pi(c^2+x^2)}\quad(c>0),\qquad
\widehat P_c(u)=e^{-2\pi c|u|},\qquad P_c*P_d=P_{c+d}.
\tag{6}
\]
These are the classical real-line Poisson kernels. Write each labelled
entry as \(z_j=x_j+iy_j\), allowing repeated entries, and set
\(H=\max_j|y_j|\). For any \(c>2H\) define
\[
\mathcal K_{W,c}(x)=
\widehat{\,e^{-2\pi c|u|}|S_W(u)|^2\,}(x).
\]
The exponential damping makes the whole source integrable on the real
line before taking its Fourier transform. Conjugating both labels in the expansion of
\(|S_W|^2\) preserves \(x_j-x_k\) and reverses \(y_j+y_k\). Thus
\[
|S_W(u)|^2
=\sum_{j,k}e^{-2\pi iu(x_j-x_k)}
       \cosh(2\pi u(y_j+y_k)).
\tag{7}
\]
For real \(b\) with \(|b|<c\),
\[
e^{-2\pi c|u|}\cosh(2\pi bu)
=\tfrac12\{e^{-2\pi(c-b)|u|}+e^{-2\pi(c+b)|u|}\}.
\]
Taking the transform in (7) therefore gives the exact formula
\[
\boxed{
\mathcal K_{W,c}(x)=\frac12\sum_{j,k}
\left\{P_{c-y_j-y_k}(x+x_j-x_k)
       +P_{c+y_j+y_k}(x+x_j-x_k)\right\}\ge0.
}
\tag{8}
\]
Every width is strictly positive. The kernel is a finite positive
mixture with integral \(N^2\).

Choose a conjugation permutation of the labelled multiset. For each
\(j\), the ordered pair \((j,\bar j)\) has equal real parts and
opposite heights, contributing exactly \(P_c(x)\) to (8). These are
\(N\) distinct ordered label pairs, even with multiplicities. Hence
\[
\boxed{\mathcal K_{W,c}(x)\ge N P_c(x).}
\tag{9}
\]
No positivity of \(\Phi\) at complex arguments has been asserted.
The operation that restores positivity is damping the entire source,
not discarding individual complex pair terms.

## Recover a pointwise profile tail from a one-sided source tail

Define the real even bounded function
\[
B_W(x)=\widehat{\phi|S_W|^2}(x).
\]
Suppose only that, for a finite \(D\ge0\),
\[
B_W(x)\le\frac{D}{1+x^2}\quad(x\in\mathbb R).
\tag{10}
\]
This is an upper bound, not an absolute-value bound; \(B_W\) can change
sign. Fix \(c=1+2H\). The product/convolution identity, (8)--(9), and
\(\Phi\ge0\) imply
\[
N(\Phi*P_c)(x)
\le(\Phi*\mathcal K_{W,c})(x)
=(B_W*P_c)(x)
\le\pi D P_{c+1}(x).
\tag{11}
\]
The last step uses (10), positivity of \(P_c\), and (6). All integrals
are absolutely convergent: \(\Phi,B_W\) are bounded and the convolution
kernels are integrable. The middle identity also follows directly by
Fubini from \(\phi\in L^1\) and (8); no integrability assumption on
\(\Phi\) is needed.

To undo the smoothing at the level of an upper bound, use the explicit
band reproducer
\[
v(x)=4\operatorname{sinc}^2(2x)-\operatorname{sinc}^2(x),
\qquad \operatorname{sinc}(x)=\frac{\sin(\pi x)}{\pi x}.
\tag{12}
\]
Its transform is
\(\widehat v(u)=2(1-|u|/2)_+-(1-|u|)_+\), which equals one on
\([-1,1]\). As \(v\in L^1\) and \(\phi\) is supported in that band,
Fubini gives \(\Phi=\Phi*v\). The elementary estimates
\(|v(x)|\le5\) and \(|v(x)|\le2/(\pi^2x^2)\) for \(x\ne0\) yield
\[
|v(x)|\le\frac{10}{1+x^2}=10\pi P_1(x)
\le10\pi c P_c(x)\qquad(c\ge1).
\tag{13}
\]
Consequently, nonnegativity of \(\Phi\) and (11) give
\[
\Phi(x)\le(\Phi*|v|)(x)
\le10\pi c(\Phi*P_c)(x)
\le\frac{10\pi^2cD}{N}P_{c+1}(x).
\]
In particular,
\[
\boxed{
\sup_x(1+x^2)\Phi(x)\le\frac{10\pi c(c+1)D}{N}<\infty.
}
\tag{14}
\]
The constant is deliberately nonoptimal. The substantive point is that
one-sided decay of the potentially signed whole-source transform
already controls the nonnegative profile transform pointwise.

## Distant-copy stability supplies that one-sided bound

For a fixed \(W\), also put
\[
A_W(x)=\widehat{J_0|S_W|^2}(x)
      =\sum_{z,w\in W}F(x+z-\bar w).
\tag{15}
\]
On any fixed horizontal line, (1) gives \(K(x+iy)=O_y(|x|^{-1})\).
The finitely many fixed shifts in (15), continuity on the remaining
compact interval and the removable-point continuation therefore give
\[
|A_W(x)|\le\frac{C_W}{1+x^2}\qquad(x\in\mathbb R)
\tag{16}
\]
for a finite constant depending on the entire configuration.

Conjugation invariance implies \(S_W(-u)=\overline{S_W(u)}\), so
\(A_W,B_W\) are real and even. For
\(R>\operatorname{diam}(\Re W)\), the two copies have disjoint real
projections. Site multiplicities and real/nonreal types are preserved,
so \(L(W\cup(W+R))=2L(W)\). Expanding the source gives
\[
\boxed{
Q_t(W\cup(W+R))-Q_t(W)
=\frac{A_W(R)-tB_W(R)}{L(W)}.
}
\tag{17}
\]
The two cross terms and the doubled denominator cancel the same factor
two.

Suppose the left side is nonnegative for all sufficiently large \(R\).
Equations (16)--(17) imply
\(B_W(R)\le C_W/[t(1+R^2)]\) there. Evenness supplies the negative
tail. On the remaining compact interval use
\(|B_W(x)|\le E_\phi(W)<\infty\) and enlarge the constant. This is
exactly (10), and (14) proves the tail condition in (4). A global
minimizer must pass every disjoint-copy test, proving (4).

If the tail condition fails, the same reasoning shows that no finite
configuration can pass all tests beyond any prescribed distance.
This proves the strict, arbitrarily distant improvement in (5).

## Finite caps and the surviving boundary

ANF-203's fixed-cap existence argument applies to every profile in
(2), without Fourier positivity or a decay rate: source domination
bounds energy, ANF-201 bounds height at fixed cardinality, and finite
horizontal cluster extraction yields an attaining cluster. Its
collision bookkeeping uses \(L(V_a)\ge L_a\), and positivity of
\(q_m(t)\ge1-t\) prevents a denominator loss at the minimum.

Combining that existing existence theorem with (5), whenever the tail
bound fails, gives for every \(m\ge1\) and fixed \(0<t<1\)
\[
\boxed{1-t\le q_\infty(t)<q_{2m}(t)<q_m(t).}
\tag{18}
\]
Indeed, duplicate an attaining configuration for \(q_m\) using (5).
The resulting size is at most \(2m\). The attained value \(q_{2m}\)
cannot equal the unattained unrestricted floor. Thus every sequence
approaching \(q_\infty(t)\) has \(|W_j|\to\infty\), since any
bounded-cardinality subsequence would stay above a fixed capped floor.

ANF-200 gives necessity and small-amplitude sufficiency of the tail
condition in the **real** class when exposure at a source zero is
positive. The present result extends necessity and the full
nonattainment consequence to the **complex** class for every profile
in (2). Complex sufficiency remains unproved. In particular, an
\(H^2\) profile has the required tail but is not thereby shown to have
a finite complex minimizer. The ordinary triangular notch passes the
tail condition, so this obstruction does not decide it. Neither (4)
nor (18) evaluates the unrestricted exposure derivative at zero.

## Prior art, adversarial checks and evidence boundary

The source inequality is
[Lamzouri, Proposition 2.1](https://arxiv.org/html/2609.02882v2#S2);
the explicit source extremizer appears in
[Carneiro--Chandee--Littmann--Milinovich, Corollary 14](https://arxiv.org/pdf/1406.5462).
No RH-conditional zero-statistics theorem is used. The translated-copy
test and the capped existence theorem are already local findings;
[Procacci, equation (1.3)](https://arxiv.org/pdf/2005.10362) supplies
the classical stability-constant setting, not finite attainment.

The Poisson transform and semigroup identity are classical; see
[Shapiro, section 3.4](https://users.math.msu.edu/users/shapiro/pubvit/Downloads/DecompCyc/decomposable.pdf).
The difference of scaled sinc squares in (12) is the classical
de la Vallee Poussin reproducing construction. Its precise plateau
and bound are proved above, so no external sampling theorem is
imported. Positive Fourier--Laplace representations on strips are
also classical, as in the existing Buescu--Paixao--Symeonides anchor.
The additional local implication is (8)--(14): positivity after
whole-source Poisson damping, retention of the conjugate-pair
\(NP_c\) component, and recovery of a pointwise profile tail from
only a one-sided whole-source bound. This closes the necessity gap
left by ANF-200 and generalizes ANF-203 beyond its chosen sparse peaks.
Targeted checks of complex positive-definite kernels, Poisson
representations, bandlimited reproduction and finite pair-energy
stability did not identify this exact implication. No novelty is
claimed for the classical kernels or a general positivity theorem.

The decisive audit points are the **sum** of heights in (7), the
strict condition \(c>2H\), the ordered conjugate-label count in (9),
both uses of \(\Phi\ge0\) in (11)--(14), and denominator additivity
only for disjoint copies. A signed profile transform does not support
the two positive-convolution comparisons. Signed source coefficients
would likewise invalidate (8)--(9). A smoothed bound alone does not
control pointwise peaks for arbitrary functions; the exact band
reproducer is essential. None of the constants is uniform in growing
configuration height or geometry.

As a noncertifying check, composite Simpson quadrature with 16,384
panels on \([0,6]\), using evenness, tested (8) at translations
\(0,0.37,8\) on six configurations: a singleton, a double real site,
a conjugate pair, mixed real/nonreal sites, repeated conjugate pairs,
and a seed-204 mixed configuration. The largest error divided by
\(\max(1,|\mathcal K_{W,c}|)\) was below \(8.2\cdot10^{-10}\),
and all sampled values satisfied (9). These finite floating-point
checks do not prove any tail, positivity statement or nonattainment;
(7)--(17) supply the analytic argument. No Lean proof is claimed.

This is an auxiliary finite-configuration obstruction. There is no
new zero-density estimate, critical-line proportion or RH conclusion.
