# NB-336 — Even-denominator phases open logarithmically enhanced critical cusps

- **Date:** 2026-10-11
- **Status:** proved
- **Research line:** nyman_beurling
- **Depends on:** NB-332, NB-333, NB-334
- **Classification:** EXACT-DERIVED + SOURCE-SIDE + CRITICAL-SQUARE-SCALE + DIOPHANTINE-PROFILE + EVEN-DENOMINATOR-LOG-CUSP + PHASE-ANISOTROPY + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED

## Claim

Let

\[
\mathfrak D(x)
:=
\sum_{k=1}^{\infty}
\frac{\|kx\|_{\mathbb Z}^{\,2}}{k^2},
\tag{1}
\]

where \(\|y\|_{\mathbb Z}\) denotes distance from \(y\) to the nearest
integer.

Let \(a/b\) be reduced and suppose \(b\) is even. Then

\[
\boxed{
\mathfrak D\!\left(\frac ab+h\right)
=
\mathfrak D\!\left(\frac ab\right)
-
\frac1b |h|\log\frac1{|h|}
+
O_b(|h|)
}
\qquad(h\to0).
\tag{2}
\]

If \(b\) is odd, the logarithmically enhanced term is absent:

\[
\boxed{
\mathfrak D\!\left(\frac ab+h\right)
-
\mathfrak D\!\left(\frac ab\right)
=
O_b(|h|)
}
\qquad(h\to0).
\tag{3}
\]

Thus even denominator is the exact parity boundary for the
\(|h|\log(1/|h|)\) singularity produced by the half-integer corner of the
nearest-integer square.

This has a direct consequence for the bounded-phase critical profile of
NB-333,

\[
\Phi(\delta,\rho)
=
\frac{
\mathfrak D(\rho\delta)
-
\mathfrak D((1+\rho)\delta)
}{4\delta}.
\tag{4}
\]

Fix \(L\in\mathbb N\) and \(\rho>0\). Suppose the fractional part of
\(\rho L\), written in lowest terms, has even denominator \(b\). Then

\[
\boxed{
\Phi(L+\varepsilon,\rho)
=
\frac{1}{4bL}
|\varepsilon|\log\frac1{|\varepsilon|}
+
O_{L,\rho}(|\varepsilon|)
}
\qquad(\varepsilon\to0).
\tag{5}
\]

In particular, for the explicit phase

\[
\rho=\frac1{2L},
\tag{6}
\]

one has

\[
\boxed{
\Phi\!\left(L+\varepsilon,\frac1{2L}\right)
=
\frac1{8L}
|\varepsilon|\log\frac1{|\varepsilon|}
+
O_L(|\varepsilon|).
}
\tag{7}
\]

The integer critical node is therefore anisotropic. Exactly at
\(\delta=L\), NB-333 gives \(\Phi(L,\rho)=0\) for every bounded phase.
After a small displacement of the macroscopic aspect ratio, the
exact-lattice phase \(\rho=0\) leaves the node through the negative
linear cusp of NB-334,

\[
\Phi(L+\varepsilon,0)
=
-\frac{\log2}{4L}|\varepsilon|
+
O(\varepsilon^2),
\tag{8}
\]

whereas suitable even-denominator phases open a positive channel of
order

\[
|\varepsilon|\log\frac1{|\varepsilon|},
\]

which is logarithmically larger than the linear exact-lattice cusp.

The statement remains a limiting-profile result. It does not supply a
uniform two-parameter estimate when simultaneously
\(q\to\infty\) and \(\varepsilon=\varepsilon_q\to0\).

## 1. Truncate before the nearest-integer folds can move across a residue class

Write

\[
f(x):=\|x\|_{\mathbb Z}^{\,2}.
\tag{9}
\]

Fix a reduced rational \(a/b\). For \(h\ne0\), choose

\[
K
:=
\left\lfloor
\frac{\eta_b}{|h|}
\right\rfloor,
\tag{10}
\]

where \(\eta_b>0\) is small enough that, for every residue class modulo
\(b\) not landing at a half-integer, translation by any \(u\) with
\(|u|\le\eta_b\) stays on the same quadratic branch of \(f\).
For example, when \(b\) is even one may take
\(\eta_b=1/(4b)\).

Split

\[
\mathfrak D\!\left(\frac ab+h\right)
-
\mathfrak D\!\left(\frac ab\right)
=
\Sigma_{\le K}+\Sigma_{>K}.
\tag{11}
\]

Since \(0\le f\le1/4\),

\[
|\Sigma_{>K}|
\le
\frac14\sum_{k>K}\frac1{k^2}
=
O_b(|h|).
\tag{12}
\]

Thus every term larger than order \(|h|\) must come from the finite
range \(k\le K\), where the residue class of \(k\bmod b\) determines
which local quadratic branch is seen.

## 2. Even denominator produces one and only one half-integer class

Assume now that \(b\) is even. Since \((a,b)=1\), \(a\) is odd. Among
the residue classes \(r\bmod b\), there is exactly one for which

\[
\frac{ar}{b}
\equiv
\frac12
\pmod1,
\]

namely

\[
r_\ast=\frac b2.
\tag{13}
\]

For \(k\equiv r_\ast\pmod b\) and \(k\le K\), the choice of
\(\eta_b\) gives \(|kh|<1/2\), so

\[
f\!\left(\frac12+kh\right)-f\!\left(\frac12\right)
=
-|kh|+k^2h^2.
\tag{14}
\]

After division by \(k^2\), this residue class contributes

\[
-|h|
\sum_{\substack{k\le K\\k\equiv b/2\;(\mathrm{mod}\;b)}}\frac1k
+
h^2
\#\{k\le K:k\equiv b/2\pmod b\}.
\tag{15}
\]

For every fixed residue class modulo \(b\),

\[
\sum_{\substack{k\le K\\k\equiv r\;(\mathrm{mod}\;b)}}\frac1k
=
\frac1b\log K+O_b(1),
\tag{16}
\]

and the counting term in (15) is \(O_b(K)\). Hence the unique cusp
class gives

\[
-\frac1b|h|\log K+O_b(|h|)+O_b(h^2K).
\tag{17}
\]

Because \(K\asymp_b |h|^{-1}\),

\[
h^2K=O_b(|h|),
\qquad
\log K=\log\frac1{|h|}+O_b(1),
\tag{18}
\]

so its contribution is

\[
-\frac1b|h|\log\frac1{|h|}
+
O_b(|h|).
\tag{19}
\]

## 3. All smooth residue classes cancel their harmonic slopes

For any other residue class \(r\ne b/2\), the point

\[
y_r:=\left\{\frac{ar}{b}\right\}
\]

stays away from the half-integer corner. On the fixed quadratic branch
containing \(y_r\), there is a slope \(s_r\) such that, for \(k\le K\)
with \(k\equiv r\pmod b\),

\[
f(y_r+kh)-f(y_r)
=
s_rkh+k^2h^2.
\tag{20}
\]

Thus the linear part from this residue class is

\[
s_rh
\sum_{\substack{k\le K\\k\equiv r\;(\mathrm{mod}\;b)}}\frac1k
=
\frac{s_r}{b}h\log K+O_b(|h|).
\tag{21}
\]

Multiplication by \(a\) permutes the grid
\(\{0,1/b,\ldots,(b-1)/b\}\). After removing the unique half-integer
point, the remaining grid points pair as \(j/b\) and \(1-j/b\).
Their derivatives under \(f\) are opposite, while the derivative at
the integer point is zero. Consequently

\[
\sum_{r\ne b/2}s_r=0.
\tag{22}
\]

The potentially logarithmic terms in (21) therefore cancel after
summing over all smooth residues. Their complete contribution is only

\[
O_b(|h|),
\tag{23}
\]

and their quadratic terms contribute

\[
O_b(h^2K)=O_b(|h|).
\tag{24}
\]

Combining (12), (19), (23), and (24) proves (2).

## 4. Odd denominator is the matched control

Suppose \(b\) is odd. No point of the grid
\(\{j/b:0\le j<b\}\) is a half-integer. Hence every residue class is
smooth for sufficiently small \(\eta_b\), and the calculation is only
the smooth-residue calculation (20)--(24).

The grid again pairs symmetrically around \(1/2\), so the sum of all
local slopes is zero. Therefore the \(h\log K\) terms cancel and one is
left with

\[
\mathfrak D\!\left(\frac ab+h\right)
-
\mathfrak D\!\left(\frac ab\right)
=
O_b(|h|),
\]

which proves (3).

This control is important: the logarithmic enhancement is not a generic
feature of rational points. It is exactly the contribution of the
residue class that lands on the derivative jump of
\(\|x\|_{\mathbb Z}^{\,2}\).

## 5. Propagation into the NB-333 critical profile

Let \(L\in\mathbb N\), let \(\rho>0\), and suppose

\[
x_0:=\{\rho L\}
\]

is rational with reduced even denominator \(b\). Since \(L\) is an
integer,

\[
\{(1+\rho)L\}
=
\{\rho L\}
=
x_0.
\tag{25}
\]

For \(\delta=L+\varepsilon\), the two arguments of
\(\mathfrak D\) in (4) are displaced from the same rational point by

\[
\rho\varepsilon
\qquad\text{and}\qquad
(1+\rho)\varepsilon.
\tag{26}
\]

Applying (2) to both terms,

\[
\begin{aligned}
\mathfrak D(\rho\delta)
&=
\mathfrak D(x_0)
-
\frac{\rho}{b}|\varepsilon|
\log\frac1{|\varepsilon|}
+
O_{L,\rho}(|\varepsilon|),\\
\mathfrak D((1+\rho)\delta)
&=
\mathfrak D(x_0)
-
\frac{1+\rho}{b}|\varepsilon|
\log\frac1{|\varepsilon|}
+
O_{L,\rho}(|\varepsilon|).
\end{aligned}
\tag{27}
\]

The constants involving
\(\log\rho\) and \(\log(1+\rho)\) are absorbed into
\(O_{L,\rho}(|\varepsilon|)\). Subtracting gives

\[
\mathfrak D(\rho\delta)
-
\mathfrak D((1+\rho)\delta)
=
\frac1b|\varepsilon|
\log\frac1{|\varepsilon|}
+
O_{L,\rho}(|\varepsilon|).
\tag{28}
\]

Since \(1/(4\delta)=1/(4L)+O(\varepsilon)\), equations (4) and (28)
give (5).

For \(\rho=1/(2L)\), one has \(x_0=1/2\), so \(b=2\) and (7) follows.

As a direct arithmetic check,

\[
\mathfrak D\!\left(\frac12\right)
=
\sum_{\substack{k\ge1\\k\ \mathrm{odd}}}
\frac{1}{4k^2}
=
\frac{\pi^2}{32}.
\tag{29}
\]

## 6. Prior-art and novelty audit

The nearest classical literature studies multiplicative autocorrelation
of the fractional-part function and arithmetic Fourier series with
rational singularities. In particular, work of
Báez-Duarte--Balazard--Landreau--Saias and Balazard--Martin makes
non-smooth behavior at rational points natural in this neighborhood;
arithmetic Fourier/Davenport and Eisenstein-derived series provide
additional structural analogies.

A targeted search did not identify the exact series (1), the parity
criterion (2)--(3), or the coefficient \(1/b\) as a stated theorem.
No bibliographic novelty is claimed. No external theorem is
load-bearing for the proof above, so this finding introduces no new
durable literature dependency in SOURCES.md.

The result is instead classified by the exact finite arithmetic
mechanism exposed here: one half-integer residue class creates the
logarithmic cusp, and the other residue classes cancel their harmonic
slopes collectively.

## 7. Boundaries and falsification controls

Several limits must remain separate.

First, (2) is a local statement for a fixed rational \(a/b\). The
constant in \(O_b(|h|)\) may depend on \(b\); no uniformity in growing
denominator is asserted.

Second, (5) is a statement about the already-established limiting
profile \(\Phi\). It is valid after taking the critical finite-section
limit defining NB-333 and then studying
\(\delta=L+\varepsilon\). It does not justify substituting a moving
\(\varepsilon_q\to0\) into the finite-\(q\) coefficient.

Third, a nonzero value of \(\Phi\) is a source-side channel statement.
It does not imply that the actual Nyman target occupies the channel.
The sampling/null decomposition, target pairing, and finite-section
conditioning remain independent requirements.

Fourth, the odd-denominator control (3) is a decisive falsification
test for the proposed mechanism. Any attempted strengthening claiming
the same logarithmic coefficient at all rationals would contradict the
residue-class calculation above.

## Research consequence

NB-334 shows that the exact-lattice phase leaves an integer critical
node through a negative linear cusp. The present result shows that the
full bounded-phase profile is substantially more singular in selected
directions: phases whose value at the node has even reduced denominator
open a positive cusp of order

\[
|\varepsilon|\log\frac1{|\varepsilon|}.
\]

Hence the critical integer node is not merely a one-dimensional cusp;
it is an anisotropic meeting point of different local singularity
classes.

This sharpens the next source-side question. The pointwise limiting
profile now identifies a log-enhanced channel, but a genuine moving
critical theorem still requires a uniform estimate comparing the
finite-\(q\) remainder of NB-333 with the scale

\[
|\varepsilon_q|\log\frac1{|\varepsilon_q|}.
\]

Only after that comparison is controlled would it make sense to ask
whether the selected channel remains visible to the actual moving
Nyman target.
