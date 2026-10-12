# NB-338 — Renormalized finite critical phase resolves microscopic even-denominator cusps

- **Status:** proved
- **Research line:** nyman_beurling
- **Depends on:** NB-304, NB-333, NB-334, NB-336, NB-337
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + UNIFORM-FINITE-SECTION + RENORMALIZED-DIOPHANTINE-PHASE + MICROSCOPIC-CRITICAL-CUSP + PHASE-SIGN-REVERSAL + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Retain the projected dilation, rank-one comparison, and adjacent witness of NB-333:

\[
U_n=\operatorname{span}\{g_2,\ldots,g_n\},\qquad
T_{n,m}=P_{U_n}A_m|_{U_n},\qquad
\nu_q=g_q-\frac{q-1}{q}g_{q-1},
\]
\[
m=dq+r,\qquad
\mathcal F_{n;q,d,r}
=\langle(\sqrt m\,T_{n,m}-R_n)g_2,\nu_q\rangle,
\qquad 8\le q\le n,\ d\ge1,\ r\ge0.
\]

Let \(\mathfrak D(x)=\sum_{k\ge1}\|kx\|_{\mathbb Z}^2/k^2\), as in NB-332--NB-337, and put

\[
u=d+\frac rq,\qquad
v=d+\frac{d+r}{q-1},\qquad
c=\frac{q-1}{q},\qquad H=\frac{\pi^2}{72}.
\tag{1}
\]

**Renormalized finite-section profile.** For every fixed \(0<a<b<\infty\) and \(R<\infty\), there exists \(C_{a,b,R}\) such that, uniformly for \(a\le d/q\le b\), \(0\le r/d\le R\), and \(n\ge q\),

\[
\boxed{
q\mathcal F_{n;q,d,r}
=\frac q4\left[
\frac c v\bigl(H-\mathfrak D(v)\bigr)
-\frac1u\bigl(H-\mathfrak D(u)\bigr)
\right]+O_{a,b,R}(q^{-1}).
}
\tag{2}
\]

In particular, since \(\mathfrak D\) is \(1\)-periodic,

\[
\boxed{
q\mathcal F_{n;q,d,r}
=
\frac{\mathfrak D(r/q)
-\mathfrak D((d+r)/(q-1))}{4(d/q)}
+O_{a,b,R}(q^{-1}).
}
\tag{3}
\]

The second argument has denominator \(q-1\), not \(q\). This finite rephasing is the term lost in the fixed-ratio profile of NB-333. It resolves logarithmic-scale effects that the \(O(\log q/q)\) comparison of NB-337 cannot separate.

**Microscopic even-denominator cusp.** Fix integers \(L\ge1\), \(K,s\), a reduced fraction \(0<a_0/B<1\) with **even** \(B\), and let \(q\to\infty\) through multiples of \(B\). Set

\[
d=Lq+K,\qquad r=\frac{a_0q}{B}+s,\qquad n\ge q.
\tag{4}
\]

For all sufficiently large \(q\), these are admissible integers. Then

\[
\boxed{
q\mathcal F_{n;q,d,r}
=
\frac{
\left|K+s+L+a_0/B\right|-|s|
}{4LB}
\frac{\log q}{q}
+O_{L,B,a_0,K,s}(q^{-1}).
}
\tag{5}
\]

The coefficient in (5) is **never zero** for fixed integers \(K,s\), because \(K+L+a_0/B\) is nonintegral. Thus the adjacent channel has a definite eventual sign at *every* fixed integer displacement; that sign can depend on an \(O(1)\) change in the remainder even though the limiting critical aspect ratio and phase are unchanged.

For example, with even \(q\), \(L=1\), \(K=0\), \(a_0/B=1/2\),

\[
\begin{aligned}
d=q,\quad r=q/2
&:\quad
q\mathcal F=\frac3{16}\frac{\log q}{q}+O(q^{-1}),\\
d=q,\quad r=q/2-1
&:\quad
q\mathcal F=-\frac1{16}\frac{\log q}{q}+O(q^{-1}).
\end{aligned}
\tag{6}
\]

Both sequences have \(d/q\to1\) and \(r/d\to1/2\), so NB-333 gives the same zero limiting coefficient for both. Their opposite logarithmic finite-section signs distinguish the microscopic boundary layer.

## 1. A uniform periodic Bernoulli tail

Write \(\varphi(t)=\{t\}-1/2\) and introduce the continuous, periodic second Bernoulli polynomial

\[
B_2(t)=\{t\}^2-\{t\}+\frac16.
\tag{7}
\]

It has mean zero on a unit period, and \(G(t)=B_2(t)/2\) is a continuous periodic primitive of \(\varphi\), in the almost-everywhere sense. Since \(G\) has mean zero, it also has a bounded periodic primitive.

For \(x>0\), set

\[
F(x)=\int_x^\infty\frac{\varphi(t)}{t^2}\,dt.
\]

Integration by parts, first using \(G'=\varphi\) and then a bounded primitive of \(G\), gives

\[
F(x)=-\frac{G(x)}{x^2}
+2\int_x^\infty\frac{G(t)}{t^3}\,dt
=
-\frac{B_2(x)}{2x^2}+O(x^{-3}),
\qquad x\ge1.
\tag{8}
\]

The remainder constant is absolute and independent of the fractional part of \(x\). In particular (8) remains valid when \(x\) passes through integer folds; no fixed-distance-from-discontinuities hypothesis is used.

## 2. Exact alternating-block decomposition

NB-333 and the exact selector identity (5) of NB-337 give

\[
q\mathcal F_{n;q,d,r}
=\frac{qd}{2}
\sum_{j\ge0}
\int_{(2j+1)d}^{(2j+2)d}
\frac{\varphi(\alpha y)-c\varphi(\beta y)}{y^2}\,dy,
\tag{9}
\]
where

\[
\alpha=1+\frac{r}{dq}=\frac{q+r/d}{q},
\qquad
\beta=1+\frac{d+r}{d(q-1)}=\frac{q+r/d}{q-1}.
\tag{10}
\]

Thus \(\alpha d=u\), \(\beta d=v\), and, crucially,

\[
\boxed{cv=u,\qquad v/u=q/(q-1).}
\tag{11}
\]

For any \(0<A<B\), substitution \(t=\kappa y\) gives the exact identity

\[
\int_A^B\frac{\varphi(\kappa y)}{y^2}\,dy
=\kappa\bigl[F(\kappa A)-F(\kappa B)\bigr].
\tag{12}
\]

Consequently (9) is exactly

\[
q\mathcal F
=\frac{qu}{2}
\sum_{j\ge0}
\Bigl[
F((2j+1)u)-F((2j+2)u)
-F((2j+1)v)+F((2j+2)v)
\Bigr].
\tag{13}
\]

This identity retains the complete finite-section normalization and the offset between the \(q\)- and \((q-1)\)-phases.

## 3. The alternating Bernoulli sum is the Diophantine profile

Define the absolutely convergent periodic series

\[
S(x)=\sum_{k\ge1}\frac{(-1)^{k+1}B_2(kx)}{k^2}.
\tag{14}
\]

Using (8) termwise in (13) is uniform because \(u\ge d\ge aq\) and \(v\ge u\). The total error is bounded by

\[
Cqu\sum_{k\ge1}
\left((ku)^{-3}+(kv)^{-3}\right)
\le C'\frac{q}{u^2}
=O_{a,b,R}(q^{-1}).
\tag{15}
\]

The resulting expression is

\[
q\mathcal F
=
\frac q4\left[\frac c v S(v)-\frac1u S(u)\right]
+O_{a,b,R}(q^{-1}).
\tag{16}
\]

To identify \(S\), put \(\psi(x)=\{x\}(1-\{x\})\). Then

\[
B_2(x)=\frac16-\psi(x),\qquad
\psi(x)-\tfrac12\psi(2x)=\|x\|_{\mathbb Z}^2.
\tag{17}
\]

Since \(\sum_{k\ge1}(-1)^{k+1}/k^2=\pi^2/12\),

\[
\begin{aligned}
S(x)
&=\frac{\pi^2}{72}
-\sum_{k\ge1}\frac{\psi(kx)}{k^2}
+\frac12\sum_{k\ge1}\frac{\psi(2kx)}{k^2}\\
&=\frac{\pi^2}{72}-\mathfrak D(x).
\end{aligned}
\tag{18}
\]

Substitution into (16) proves (2). Moreover, \(r/d\le R\) and \(d/q\in[a,b]\) give

\[
\frac qu=\frac{1}{d/q}+O_{a,b,R}(q^{-1}),
\qquad
\frac{qc}{v}=\frac{1}{d/q}+O_{a,b,R}(q^{-1}).
\tag{19}
\]

The boundedness of \(S\) and periodicity of \(\mathfrak D\) now yield (3).

As a consistency check, replacing \((d+r)/(q-1)\) in (3) by \((d+r)/q\) changes the argument by

\[
\frac{d+r}{q(q-1)}=O_{a,b,R}(q^{-1}).
\tag{20}
\]

The global modulus \(|\mathfrak D(x+h)-\mathfrak D(x)|
\ll |h|\log(e/|h|)\), established in NB-337, therefore recovers its uniform \(O(\log q/q)\) error. The sharper rephased form (3) retains the missing fold information instead of estimating it away.

## 4. Resolve fixed integer offsets at even-denominator phases

For (4), both arguments in (3) approach the same rational point \(a_0/B\). Indeed

\[
\begin{aligned}
u&=Lq+K+\frac{a_0}{B}+\frac{s}{q},\\
v&=Lq+K+L+\frac{a_0}{B}
+\frac{K+s+L+a_0/B}{q-1}.
\end{aligned}
\tag{21}
\]

By periodicity,

\[
\mathfrak D(u)=
\mathfrak D\left(\frac{a_0}{B}+\frac{s}{q}\right),
\quad
\mathfrak D(v)=
\mathfrak D\left(\frac{a_0}{B}+
\frac{K+s+L+a_0/B}{q-1}\right).
\tag{22}
\]

NB-336 gives, for reduced even denominator \(B\),

\[
\mathfrak D\left(\frac{a_0}{B}+h\right)
=\mathfrak D\left(\frac{a_0}{B}\right)
-\frac{|h|}{B}\log\frac1{|h|}
+O_B(|h|).
\tag{23}
\]

For every fixed real \(\xi\), including \(\xi=0\), this implies the uniform-in-\(q\) specialization

\[
\mathfrak D\left(\frac{a_0}{B}+\frac{\xi}{q+O(1)}\right)
=\mathfrak D\left(\frac{a_0}{B}\right)
-\frac{|\xi|}{B}\frac{\log q}{q}+O_{B,\xi}(q^{-1}).
\tag{24}
\]

To see this at \(\xi=0\), both sides are equal exactly apart from the displayed zero remainder; for \(\xi\ne0\), the discarded term \(|\xi|\log|\xi|/q\) is bounded by \(O_\xi(q^{-1})\).

Apply (24) to the two values in (22). Their difference is

\[
\frac{|K+s+L+a_0/B|-|s|}{B}
\frac{\log q}{q}+O_{L,B,a_0,K,s}(q^{-1}).
\tag{25}
\]

Since \(d/q=L+O(q^{-1})\), insertion in (3) gives (5). The leading coefficient cannot vanish: equality of the two absolute values would require
\(K+s+L+a_0/B=\pm s\), which is impossible because \(a_0/B\notin\mathbb Z\). Substituting the two remainder choices yields (6).

**Odd-denominator control.** If the reduced denominator of \(a_0/B\) is odd, NB-336 gives only a Lipschitz-size displacement \(O_B(|h|)\). The same calculation yields \(q\mathcal F=O(q^{-1})\), with no logarithmically enhanced channel. Thus the parity mechanism survives the exact finite rephasing.

## 5. Audits, prior art, and limitations

The key uniformity test is at integer folds, where a naive cellwise Taylor expansion is not uniform. Here the periodic primitive in (8) is continuous across all folds, and the absolute \(O(x^{-3})\) remainder requires no Diophantine separation. The summation error in (15) is controlled before any rational-cusp expansion. All limits are for the actual finite section \(n\ge q\), not for a profile with aspect ratio held fixed first.

As a numerical falsification check, direct evaluation of the exact alternating selector-block integrals for \(d=q\), even \(q=48,96,192\), gives respectively approximate values \(0.01387,\ 0.00837,\ 0.00489\) for \(q\mathcal F\) when \(r=q/2\), and \(-0.00224,\ -0.00152,\ -0.00097\) when \(r=q/2-1\). The finite-block evaluations are corroborative; equations (8)--(25), not numerical extrapolation, prove the asymptotic signs.

The primary neighboring literature is L. Báez-Duarte, M. Balazard, B. Landreau and E. Saias, *Sur l'autocorrelation multiplicative de la fonction partie fractionnaire* (arXiv:math/0306251), and M. Balazard and B. Martin, *Sur l'autocorrélation multiplicative de la fonction partie fractionnaire et une fonction définie par J. R. Wilton* (arXiv:1305.4395). They establish the fractional-part autocorrelation setting and rational-point regularity context, not a cited finite adjacent-section identity of the form (2) or its microscopic consequence (5). The Bernoulli integration and alternating-series identity are elementary classical tools; no bibliographic originality is claimed and no additional external theorem is load-bearing. Existing SOURCES.md anchors suffice.

The microscopic coefficient is an observable of one **source/probe channel**. Its size is \(O(\log q/q)\) in \(q\mathcal F\) and therefore vanishes as \(q\to\infty\); it does not establish a fixed operator-norm gap, controlled target occupation, an approximation-distance rate, or any implication for RH. The formula requires \(d/q\) in a fixed compact positive interval and \(r/d\) bounded. For moving \(K\) or \(s\) it remains usable through (3), but the fixed-offset expansion (5) cannot be applied with unbounded offset constants without a new uniform cusp estimate.

**Mathematical delta.** NB-337 proved that mesoscopic offsets \(|K|\to\infty\), \(|K|=o(q)\) preserve the positive even-denominator cusp, but its \(O(\log q/q)\) error left \(|K|=O(1)\) unresolved. The exact \(q\) versus \(q-1\) phase relation and Bernoulli-tail resummation reduce the error to \(O(1/q)\) around a *rephased* Diophantine profile. This resolves fixed microscopic offsets, including \(K=0\), and shows that shifting the remainder by one integer can reverse the leading finite-channel sign at the same critical node. The genuinely target-aware Nyman implication remains open.
