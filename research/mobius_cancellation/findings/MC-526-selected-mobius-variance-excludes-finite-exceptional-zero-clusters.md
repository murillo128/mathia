# MC-526 — Selected Möbius variance excludes finite exceptional zero clusters

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CONDITIONAL-TRANSFER`, `NO-NOVELTY-CLAIM`.

## Claim and arithmetic boundary

Write
\[
S_{X,H}(y)=M(y+H)-M(y),\qquad
m_{X,H}=X^{-1}\int_X^{2X}S_{X,H}(y)\,dy,
\]
\[
V_\mu(X,H)=\int_X^{2X}|S_{X,H}(y)-m_{X,H}|^2\,dy.
\]
Suppose that, for some fixed \(1/2<\sigma_*<1\), the set
\[
\mathcal Z_* =\{\rho:\zeta(\rho)=0,\ \Re\rho>\sigma_*\}
\tag{1}
\]
is **finite and nonempty**. Let \(\beta\) be its largest real part,
and let \(m\) be the largest multiplicity among its zeros with real
part \(\beta\). Then there are constants \(c,h_0>0\) and \(X_0\),
depending on this fixed zero configuration and \(\sigma_*\), such that
\[
\boxed{V_\mu(X,H)\ge
cH^2X^{2\beta-1}(\log X)^{2m-2}
\quad(X\ge X_0,\ 1\le H\le h_0X,\ H\in\mathbb N).}
\tag{2}
\]
No separate bound on reciprocal-zeta growth, simple-zero hypothesis,
or independence of zero ordinates is assumed.

Consequently, fix \(0<\theta<1\), put \(\alpha=1-\theta/2\), and
suppose there is an unbounded set \(E\subset[2,\infty)\) on which
\[
V_\mu(X,\lfloor X^\theta\rfloor)
\ll_\varepsilon X^{1+\varepsilon}\lfloor X^\theta\rfloor
\quad\text{for every }\varepsilon>0.
\tag{3}
\]
Each constant is uniform for sufficiently large \(X\in E\).
For every fixed \(\sigma>\alpha\), the set of zeta zeros in
\(\Re s>\sigma\) is then either empty or infinite. More precisely,
if a zero has real part \(b>\alpha\), there must be infinitely many
zeros with real part greater than \(b-\delta\), for every
\(0<\delta<b-\alpha\).

This excludes a finite outlying cluster from an actual Möbius
selected-scale premise. It does **not** exclude an infinite sparse
family, prove (3), or establish RH. The selection set need not have
any density or spacing property; its unboundedness suffices for this
conditional consequence.

The distinction from
[MC-525](MC-525-polynomial-strip-growth-forces-pole-variance-on-every-block.md)
is arithmetic: its generic two-pole theorem assumes a polynomial
bound for the pole-subtracted continuation. Here finiteness of the
exceptional **zeta** zeros supplies that bound, and the proof handles
all finite multiplicities and simultaneous leading poles. The arbitrary
Dirichlet-series control in
[MC-524](MC-524-density-one-window-control-coexists-with-prescribed-sparse-poles.md)
has no corresponding growth implication.

## 1. Finite exceptions supply the contour growth bound

Choose \(a\in(\sigma_*,\beta)\) not equal to the real part of any
zero in \(\mathcal Z_*\). Above a fixed height \(T_*\), zeta has no
zeros in \(\Re s>\sigma_*\). For large \(|t|\), the disk centered
at \(2+it\) of radius
\[
R=2-\tfrac12(\sigma_*+a)
\]
is therefore zero-free and avoids the pole at 1. Its analytic logarithm
\(g=\log\zeta\) can be chosen to agree at the center with the
absolutely convergent Euler-product logarithm. On the disk,
\(\Re g=\log|\zeta|\ll\log(2+|t|)\), by classical polynomial
growth of zeta on fixed strips, and \(g(2+it)=O(1)\).
Borel–Carathéodory on the smaller radius \(r=2-a<R\) gives
\[
|g(s)|\ll\log(2+|t|)\quad(|s-(2+it)|\le r).
\]
In particular, for some fixed \(B\),
\[
|1/\zeta(\sigma+it)|\ll(2+|t|)^B
\quad(a\le\sigma\le2,\ |t|\text{ sufficiently large}).
\tag{4}
\]
Only a polynomial bound is needed; no three-circles refinement or
RH-scale reciprocal bound is being imported. This is the high-height
version of the classical logarithm argument also reconstructed in
[MC-521, Section 4](MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md).

Let \(P(s)\) be the finite sum of the full Laurent principal parts
of \(1/\zeta(s)\) at its poles with \(\Re\rho>a\). Then
\(R_0(s)=1/\zeta(s)-P(s)\) is holomorphic on a neighborhood of
the closed strip \(a\le\Re s\le2\) and polynomially bounded
there. At large height this follows from (4) and the finite rational
function \(P\); at bounded height it follows by removal of all the
poles and compactness. The pole of zeta at 1 is a regular zero of its
reciprocal.

This step fails for an arbitrary holomorphic pole-subtracted function:
it uses the polynomial bound for **zeta**, the bounded Euler-product
logarithm at \(2+it\), and the zero-free disks furnished by (1).

## 2. All leading pole profiles survive empirical centering

List the positive-ordinate zeros with real part \(\beta\) and
multiplicity \(m\) as \(\rho_j=\beta+i\gamma_j\),
\(1\le j\le k\). Zeta has no real zero in \((0,1)\): its
alternating eta series is positive there by pairing adjacent terms,
whereas \(1-2^{1-s}<0\). Conjugation pairs the zeros, so \(k\ge1\). Let
\[
c_j=\lim_{s\to\rho_j}(s-\rho_j)^m/\zeta(s)\ne0.
\]
On \((1,2)\), define the \(2k\) real functions
\[
p_{2j-1}(u)=\Re u^{\rho_j-1},\qquad
p_{2j}(u)=\Im u^{\rho_j-1}.
\]
The functions \(1,p_1,\ldots,p_{2k}\) are linearly independent
on every open interval. After \(t=\log u\), they are real forms
of the distinct exponentials with exponents
\(0,\beta-1\pm i\gamma_1,\ldots,\beta-1\pm i\gamma_k\).
Differentiating a vanishing combination through order \(2k\) at
one point gives an invertible Vandermonde system. Neither rational
independence nor separation estimates for the \(\gamma_j\) are needed.

Choose \(\chi\in C_c^\infty((1,2))\), nonnegative, positive on
an interval, with \(\int\chi=1\). Set
\[
\bar p_i=\int\chi p_i,\qquad
f_i=\chi(p_i-\bar p_i),\qquad
G_{i\ell}=\int f_i p_\ell.
\tag{5}
\]
Each \(\int f_i=0\), and \(G\) is a positive-definite covariance
matrix by the preceding independence. Extend the tests by zero and put
\[
\phi_{i,h}(u)=h^{-1}\int_0^h f_i(u-v)\,dv,\qquad
\Phi_{i,h}(s)=\int_0^\infty\phi_{i,h}(u)u^{s-1}\,du.
\tag{6}
\]
For \(0<h\le1\), these smooth functions have uniformly bounded
derivatives and supports in a common compact subset of \((0,\infty)\).
The real matrix with columns
\(\Re\Phi_{i,h}(\rho_j),\Im\Phi_{i,h}(\rho_j)\) is
\(G(h)=G+O(h)\). Choose fixed \(h_0>0\) so that
\[
s_{\min}(G(h))\ge\tfrac12\lambda_{\min}(G)>0
\quad(0<h\le h_0).
\tag{7}
\]
Thus centering removes only the constant profile; it cannot remove
any nonzero combination of all the leading profiles.

## 3. Multiple residues and the exact window normalization

Mellin inversion on \(\Re s=2\), followed by a shift to
\(\Re s=a\), gives
\[
L_i(X,h):=\sum_n\mu(n)\phi_{i,h}(n/X)
=\sum_{\Re\rho>a}\mathop{\rm Res}_{s=\rho}
\frac{X^s\Phi_{i,h}(s)}{\zeta(s)}+O(X^a).
\tag{8}
\]
The error is uniform for \(0<h\le h_0\): integration by parts
in \(\log u\) gives arbitrary polynomial decay of \(\Phi_{i,h}\)
throughout the strip, uniformly in \(h\); (4) then makes the
vertical integrals absolutely convergent and the horizontal integrals
vanish. There are only finitely many residues.

If the Laurent coefficients at a pole of order \(d\) are
\(c_{\rho,r}\), \(1\le r\le d\), its residue in (8) is exactly
\[
X^\rho\sum_{r=1}^d c_{\rho,r}
\sum_{\ell=0}^{r-1}
\frac{(\log X)^{r-1-\ell}}{(r-1-\ell)!\,\ell!}
\Phi_{i,h}^{(\ell)}(\rho).
\tag{9}
\]
In particular its leading logarithmic coefficient is
\(c_{\rho,d}\Phi_{i,h}(\rho)/(d-1)!\), even when its ordinary
residue \(c_{\rho,1}\) vanishes.

Let \(v(X)\in\mathbb R^{2k}\) have the two entries
\(\Re(c_j e^{i\gamma_j\log X}),-\Im(c_j e^{i\gamma_j\log X})\)
for each \(j\). Its norm is the fixed positive number
\((\sum_j|c_j|^2)^{1/2}\). Equations (8)–(9) yield the vector identity
\[
(L_i(X,h))_{i=1}^{2k}
=\frac{2X^\beta(\log X)^{m-1}}{(m-1)!}G(h)v(X)
+o\bigl(X^\beta(\log X)^{m-1}\bigr),
\tag{10}
\]
uniformly in \(h\). Poles on the leading line with smaller
multiplicity lose a logarithmic power; all other poles and the
remainder lose a fixed power of \(X\). Uniform bounds on the
finitely many derivatives in (9) justify both statements. Equations
(7) and (10) therefore give
\[
\sum_i|L_i(X,h)|^2\gg X^{2\beta}(\log X)^{2m-2}.
\tag{11}
\]

For \(h=H/X\), a finite interchange in (6) gives exactly
\[
L_i(X,H/X)=\frac1H\int_X^{2X}
S_{X,H}(y)f_i(y/X)\,dy
=\frac1H\int_X^{2X}
(S_{X,H}(y)-m_{X,H})f_i(y/X)\,dy.
\tag{12}
\]
Indeed, the coefficient of \(\mu(n)\) on the right is
\(H^{-1}\int_{n-H}^n f_i(y/X)dy=\phi_{i,H/X}(n/X)\).
The support of the test handles block endpoints, and its zero integral
removes the empirical mean. Cauchy–Schwarz gives
\[
\sum_i|L_i(X,H/X)|^2
\le\frac{X}{H^2}V_\mu(X,H)\sum_i\|f_i\|_2^2.
\tag{13}
\]
Together with (11), this proves (2).

## 4. Consequence for an arbitrary unbounded selection

If there were finitely many but at least one zero in \(\Re s>\sigma\)
for a fixed \(\sigma>\alpha\), apply (2) with \(\sigma_*=\sigma\).
Its largest real part satisfies \(\beta>\sigma>\alpha\). For
\(H=\lfloor X^\theta\rfloor\), the ratio of (2) to the upper
bound in (3) is at least a positive constant times
\[
X^{2\beta+\theta-2-\varepsilon}(\log X)^{2m-2}.
\tag{14}
\]
Choose \(0<\varepsilon<2\beta+\theta-2\). This diverges as
\(X\to\infty\), including along \(E\), a contradiction.
The refined statement follows by taking \(\sigma=b-\delta\):
the given zero makes that set nonempty, so it must be infinite.
Zeros in bounded regions are finite, so this is infinitude at unbounded
heights, not repetition of a zero by multiplicity.

## Prior art, delta and stress tests

The logarithm estimate is the classical Littlewood–Titchmarsh method:
[Titchmarsh, second edition, Section 14.2](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf),
pp. 336–337, starts with precisely the Borel–Carathéodory step used
here. Only its fixed-disk argument is reused; the absence of zeros in
those disks is derived from (1), not assumed from RH. The existing
source MC-S67 also documents the stronger RH-conditional reciprocal
estimate, which is unnecessary here.

Finite poles, logarithmic factors from multiple poles and smoothed
asymptotics are classical Mellin theory; see Flajolet, Gourdon and Dumas,
[*Mellin Transforms and Asymptotics: Harmonic Sums*, Theorem 4](https://algo.inria.fr/flajolet/Publications/mellin-harm.pdf),
and [DLMF §2.5(i)](https://dlmf.nist.gov/2.5). The required shift and
its shrinking-window uniformity are justified above. The finite
covariance argument is elementary linear algebra, not a new general
spectral principle.

Targeted checks covered finite exceptional zeta zeros, reciprocal growth,
Mertens oscillation, short-interval Möbius variance and Mellin converse
mapping. No external novelty is asserted. The durable local delta is
the **Möbius-specific** finite-exception exclusion under selected-scale
centered moments, with arbitrary finite pole orders. It identifies a
case where the growth obstruction of MC-524 is unavailable, while
leaving a precise infinite-family obstruction.

- An infinite family with \(o(T)\) counting function can still satisfy
  the conclusion after (3). Infinitude is not positive density, and
  the zero-density input in MC-522 does not close this gap.
- The theorem neither assumes nor proves that a rightmost zero exists
  in the unrestricted infinite case. It does not replace infinitely
  many poles by a fixed finite cluster plus a controlled remainder.
- Multiplicity contributes \((\log X)^{2m-2}\); a zero ordinary
  residue does not remove the highest Laurent coefficient in (9).
- Close frequencies may make the constants very small. All frequencies
  are fixed before \(X\) grows. No uniform estimate as the cluster
  size or ordinates grow is claimed.
- At \(\beta=1-\theta/2\), the epsilon-loss ceiling (3) is not
  contradicted by any fixed logarithmic factor. Strict inequality is
  essential.
- The all-plus control has a pole at 1 and constant window sums for
  integer \(H\). It would have zero centered variance; it is excluded
  here both by the Möbius coefficients and by \(\beta<1\). This
  checks why constant-profile independence must be explicit.
- The proof is analytic. No numerical evidence about actual off-line
  zeros, new unconditional Mertens bound, independent adversarial
  approval, or formal verification is asserted.
