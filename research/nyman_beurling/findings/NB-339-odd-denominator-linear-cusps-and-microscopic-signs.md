# NB-339 — Odd-denominator rational phases have linear cusps and microscopic finite-section signs

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** nyman_beurling
- **Depends on:** NB-332, NB-333, NB-334, NB-336, NB-338
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + ODD-DENOMINATOR-LINEAR-CUSP + MICROSCOPIC-FINITE-SECTION + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Put
\[
f(t)=\|t\|_{\mathbb Z}^{2},\qquad
\mathfrak D(x)=\sum_{k\ge1}\frac{f(kx)}{k^2},\qquad
H=\frac{\pi^2}{72}.
\]
Fix a reduced rational \(0<a/B<1\) with **odd** \(B\ge3\).
Since no \(ka/B\) is a half-integer, the slopes
\(s_k=f'(ka/B)\) are well defined, periodic modulo \(B\), and
have zero mean. Set
\[
\Lambda_{a,B}=\sum_{k\ge1}\frac{s_k}{k}
=-\frac1B\sum_{r=1}^{B}s_r\,\psi_0(r/B),
\tag{1}
\]
where \(\psi_0=\Gamma'/\Gamma\) is the digamma function. The
series is conditionally convergent. Then, **with a quadratic
remainder from both sides**, 
\[
\boxed{\mathfrak D(a/B+h)
=\mathfrak D(a/B)+\Lambda_{a,B}h
+\frac{\log2}{B}|h|+O_{a,B}(h^2).}
\tag{2}
\]
In particular every reduced odd-denominator rational is a genuine
linear cusp: the right and left derivatives differ by \(2\log2/B\).
The logarithmic cusp of NB-336 occurs instead at even denominators.

For the exact projected-dilation adjacent coefficient of NB-338,
\[
\mathcal F_{n;q,d,r}
=\left\langle(\sqrt{dq+r}\,T_{n,dq+r}-R_n)g_2,\,
g_q-\frac{q-1}{q}g_{q-1}\right\rangle,\qquad 8\le q\le n,
\]
take \(q\to\infty\) through positive multiples of \(B\), fix integers
\(L\ge1,K,s\), and put
\[
d=Lq+K,\quad r=\frac{aq}{B}+s,\quad
\xi=K+s+L+\frac aB,\quad
S_0=H-\mathfrak D(a/B).
\tag{3}
\]
The integers \(d,r\) are admissible for sufficiently large \(q\).
Uniformly for \(n\ge q\),
\[
\boxed{
q^2\mathcal F_{n;q,d,r}
=
\frac{-\Lambda_{a,B}(K+L+a/B)
+\frac{\log2}{B}(|s|-|\xi|)
-2S_0}{4L}
+O_{L,K,s,a,B}(q^{-1}).
}
\tag{4}
\]
The term \(-2S_0\) comes from **finite normalization**, not from the
local cusp. It is absent if the factors with denominators \(q\) and
\(q-1\) are prematurely identified. Equation (4) determines the
microscopic \(q^2\mathcal F\) limit at odd phases, beyond the
\(O(q^{-1})\) error in \(q\mathcal F\) of NB-338.

## 1. Exact odd-residue average and the cusp

The uniformly convergent classical Fourier series
\[
f(t)=\frac1{12}+\frac1{\pi^2}
\sum_{\ell\ge1}\frac{(-1)^\ell\cos(2\pi\ell t)}{\ell^2}
\tag{5}
\]
implies, because \(B\) is odd and multiplication by \(a\) permutes
residue classes,
\[
F_B(t):=\frac1B\sum_{r=1}^{B}f(t+ra/B)
=\frac{1-B^{-2}}{12}+\frac1{B^2}f(Bt).
\tag{6}
\]
Every \(ra/B\) avoids the half-integer corner, so (6) gives
\(\sum_{r=1}^B s_r=0\). Dirichlet's test proves convergence of
(1), and grouping its zero-mean residue classes gives the stated
digamma expression.

Set \(g_r(t)=f(t+ra/B)-F_B(t)\), \(1\le r\le B\). Then
\(\sum_r g_r(t)=0\) for every real \(t\). As all the grid points
remain on fixed quadratic branches for \(|t|<1/(2B)\),
\[
g_r(t)-g_r(0)=s_rt
\quad\text{whenever }|t|<1/(2B).
\tag{7}
\]
Define \(p_r(t)=g_r(t)-g_r(0)-s_rt\). Thus
\(\sum_r p_r(t)=0\), \(p_r(t)=0\) near zero, and, globally,
\[
|p_r(t)|\le C_B(1+|t|),\qquad
|p_r(t)-p_r(t')|\le C_B|t-t'|.
\tag{8}
\]
The latter follows from Lipschitz continuity of \(f,F_B\) and
bounded slopes \(s_r\).

Splitting each term of \(\mathfrak D(a/B+h)\) with (6) yields
\[
\mathfrak D(a/B+h)-\mathfrak D(a/B)
=\frac1{B^2}\mathfrak D(Bh)+h\Lambda_{a,B}
+\sum_{k\ge1}\frac{p_{k\bmod B}(kh)}{k^2}.
\tag{9}
\]
Here the final series is taken in increasing \(k\), with
\(p_{0\bmod B}=p_B\). It is conditionally summable by the
zero-mean block cancellation established next.

Let \(0<|h|<1/(4B^2)\). Terms with
\(k<1/(2B|h|)\) vanish by (7). For the remainder group
\(k=jB+r\), \(1\le r\le B\), into full blocks. At the common
argument \(t=jBh\), the sum of \(p_r(t)\) is zero. Replacing
\((jB+r)h\) by \(jBh\) and \((jB+r)^{-2}\) by
\((jB)^{-2}\) costs at most
\[
C_B\left(\frac{|h|}{j^2}
+\frac{1+j|h|}{j^3}\right)
\tag{10}
\]
in each block. All remaining blocks have
\(j\gg_B |h|^{-1}\), and
\[
\sum_{j\gg_B |h|^{-1}}
\left(\frac{|h|}{j^2}+\frac1{j^3}\right)
=O_B(h^2).
\tag{11}
\]
At most one incomplete initial block contributes \(O_B(h^2)\)
using (8) and \(k\asymp_B |h|^{-1}\). Consequently the last
term of (9) is \(O_B(h^2)\), **not merely**
\(O_B(h^2\log(1/|h|))\).

NB-334 gives the exact integer cusp
\(\mathfrak D(z)=(\log2)|z|+O(z^2)\) from its
bounded-variation Riemann sum. Apply it with \(z=Bh\) in (9):
\[
B^{-2}\mathfrak D(Bh)
=\frac{\log2}{B}|h|+O_B(h^2).
\]
This proves (2). The estimate holds for both signs of \(h\);
no differentiated infinite series or unproved interchange of
a rational limit is used.

## 2. Sharpen the finite adjacent coefficient by one Bernoulli order

Retain the exact notation from NB-338:
\[
u=d+\frac rq,\quad
v=d+\frac{d+r}{q-1},\quad
c=\frac{q-1}{q},\quad cv=u,
\]
and write \(\varphi(t)=\{t\}-1/2\) and
\(J(x)=\int_x^\infty\varphi(t)t^{-2}\,dt\).
Its alternating-block identity is
\[
q\mathcal F
=\frac{qu}{2}\sum_{k\ge1}(-1)^{k+1}
\bigl[J(ku)-J(kv)\bigr].
\tag{12}
\]

Periodic Bernoulli primitives give the uniform expansion, valid
across integer folds,
\[
J(x)=
-\frac{B_2(x)}{2x^2}
-\frac{B_3(x)}{3x^3}
+O(x^{-4}),\qquad x\ge1,
\tag{13}
\]
where
\(B_2(x)=\{x\}^2-\{x\}+1/6\) and
\(B_3(x)=\{x\}^3-\tfrac32\{x\}^2+\tfrac12\{x\}\).
Indeed \(B_2/2\) is a mean-zero periodic primitive of \(\varphi\);
\(B_3/6\) is its mean-zero periodic primitive, and a bounded
primitive of \(B_3\) controls the remainder by a third integration
by parts.

Put
\[
S_j(x)=\sum_{k\ge1}\frac{(-1)^{k+1}B_j(kx)}{k^j},
\quad j=2,3.
\]
Equation (18) of NB-338 gives \(S_2=H-\mathfrak D\).
Inserting (13) in (12), with absolutely summable errors, yields
\[
q\mathcal F
=\frac{q}{4u}\left[c^2S_2(v)-S_2(u)\right]
+\frac{q}{6u^2}\left[c^3S_3(v)-S_3(u)\right]
+O(q/u^3).
\tag{14}
\]
The periodic \(B_3\) is globally Lipschitz and
\(\sum_{k\ge1}k^{-2}<\infty\), hence \(S_3\) is periodic and
globally Lipschitz. Under (3),
\[
u=Lq+K+\frac aB+\frac sq,\qquad
v=Lq+K+L+\frac aB+\frac{\xi}{q-1}.
\tag{15}
\]
Modulo integers their difference is \(O(q^{-1})\), so
\(S_3(v)-S_3(u)=O(q^{-1})\).
Also \(c^3-1=O(q^{-1})\) and \(u\asymp_L q\).
The entire second term and remainder of (14) are therefore
\(O(q^{-2})\):
\[
q\mathcal F
=\frac q{4u}[c^2S_2(v)-S_2(u)]
+O_{L,K,s,a,B}(q^{-2}).
\tag{16}
\]
This is a *local, common-phase* improvement; it does not
claim an \(O(q^{-2})\) remainder uniformly at unrelated phases.

## 3. Extract the microscopic normalization term

Let \(b=\log2/B\). By periodicity and (2), (15) gives
\[
\begin{aligned}
S_2(u)&=S_0-\frac{\Lambda_{a,B}s+b|s|}{q}
+O_{a,B,s}(q^{-2}),\\
S_2(v)&=S_0-\frac{\Lambda_{a,B}\xi+b|\xi|}{q}
+O_{a,B,L,K,s}(q^{-2}).
\end{aligned}
\tag{17}
\]
Since \(c^2=1-2/q+O(q^{-2})\),
\[
c^2S_2(v)-S_2(u)
=-\frac{1}{q}\left[
\Lambda_{a,B}(\xi-s)
+b(|\xi|-|s|)
+2S_0\right]+O(q^{-2}).
\tag{18}
\]
Now \(q/u=1/L+O_{L,K,a,B}(q^{-1})\)
and \(\xi-s=K+L+a/B\).
Combining (16)--(18) and multiplying by \(q\) proves (4).
The \(2S_0\) term is exactly the contribution of \(c^2-1\),
which cannot be discarded at the scale \(q^2\mathcal F\).

## 4. Falsification, prior art, and limits

For \(B=3\), elementary residue sums yield
\[
\Lambda_{1,3}=\frac{2\pi}{9\sqrt3},\quad
\Lambda_{2,3}=-\frac{2\pi}{9\sqrt3},\quad
\mathfrak D(1/3)=\mathfrak D(2/3)=\frac{4\pi^2}{243},\quad
S_0=-\frac{5\pi^2}{1944}.
\tag{19}
\]
For \(L=1,K=s=0\), (4) yields respectively
\[
\lim_{\substack{q\to\infty\\3\mid q}}
q^2\mathcal F_{n;q,q,q/3}
=-0.1986794693\ldots,
\quad
\lim_{\substack{q\to\infty\\3\mid q}}
q^2\mathcal F_{n;q,q,2q/3}
=+0.0843663363\ldots
\tag{20}
\]
uniformly over all \(n\ge q\). Rational evaluation using
\(\mathfrak D(p/Q)=Q^{-2}\sum_{r=1}^{Q-1}
f(pr/Q)\psi_1(r/Q)\) (where \(\psi_1\) is trigamma)
checks the \(S_2\) contribution of (16): at \(q=960\)
it gives approximately \(-0.1981613\) and \(+0.0845928\),
consistent with the predicted limits and the
\(O(q^{-1})\) correction. These are falsification checks,
not substitutes for the proof.

The parity control is decisive: (6) specifically requires
odd \(B\), whereas NB-336 supplies an
\(|h|\log(1/|h|)\) cusp for even \(B\). The finite-section
control is also essential: dropping the \(q-1\) phase
or the \(c^2\) normalization changes (4).
Every limit fixes \(B,a,L,K,s\); no claim is made for
growing rational denominators or moving offsets.

The closest cited primary neighborhood is
Báez-Duarte--Balazard--Landreau--Saias,
*Étude de l'autocorrélation multiplicative de la fonction partie
fractionnaire* (Ramanujan J. 9 (2005), arXiv:math/0306251),
and Balazard--Martin,
*Sur l'autocorrélation multiplicative de la fonction partie
fractionnaire et une fonction définie par J. R. Wilton*
(arXiv:1305.4395). These analyze nearby fractional-part
autocorrelation and rational singularity phenomena.
The Fourier grid average and Bernoulli integrations here are
classical ingredients. No claim of bibliographic originality
or new outside theorem is made; the existing SOURCES.md
contains the required literature anchors.

**Mathematical delta.** NB-336 identified the parity boundary
but left the odd-denominator regularity at \(O_B(|h|)\).
Equation (2) determines its cusp coefficient and drift slope
with a quadratic remainder. NB-338 resolved even-denominator
microscopic signs at scale \((\log q)/q\) in \(q\mathcal F\);
(4) instead resolves the smaller \(1/q\) scale and
explains its finite-normalization correction.
This is still one *source/probe-channel* observable, not a
target-pairing or finite-section approximation-distance bound.
It supplies neither a fixed mixing norm gap nor an RH consequence.
