# PL-486 — Mellin filters of order below one cannot preserve a fixed box range

**Evidence/status:** EXACT-DERIVED / NEGATIVE-OBSTRUCTION;
CLASSICAL ENTIRE-FUNCTION AND FINITE-DIFFERENCE INGREDIENTS;
NO EXTERNAL NOVELTY CLAIM.

## Claim and consequence for single-window isolation

Fix \(h>0\), a bounded nonempty open interval \(J\Subset(0,\infty)\),
and
\[
A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,\qquad E=u\partial_u.
\]
Let \(P(s)=\sum_{j\ge0}p_js^j\) be entire with
\[
|P(s)|\le C\exp(C|s|^a),\qquad 0<a<1.                 \tag{1}
\]
Choose \(1<q<1/a\). Write \(G_c^q(J)\) for compactly supported
smooth complex functions in \(J\) satisfying

\(\|f^{(r)}\|_\infty\le C_f R_f^r(r!)^q\) for all \(r\ge0\),

with constants allowed to depend on \(f\). Define the Mellin filter
\[
T_P\varphi=P(-E)\varphi=\sum_{j\ge0}p_j(-E)^j\varphi.
                                                               \tag{2}
\]
On the tests used below this series converges in every smooth norm,
preserves compact support, and multiplies the Mellin transform by

\(\mathcal M(T_P\varphi)(s)=P(s)\mathcal M\varphi(s)\).

For **any one fixed** \(n\in\mathbb Z\setminus\{0\}\), set
\(\xi_n=2\pi n/h\). Then
\[
\boxed{
\left[\widehat{T_PA_hf}(\xi_n)=0
\text{ for every } f\in G_c^q(J),\ \int f=0\right]
\quad\Longleftrightarrow\quad P\text{ is constant}.}             \tag{3}
\]
The Fourier convention is \(\widehat\varphi(\xi)=\int\varphi(u)e^{-i\xi u}du\).
Every member of \(A_h(C_c^\infty(\mathbb R))\) has zero Fourier
transform at every \(\xi_n\). Thus no nonconstant symbol satisfying
(1) preserves the fixed-box range for all these mean-zero inputs.
For each prescribed nonzero harmonic there is a counterexample input;
one input simultaneously breaking every harmonic is not asserted.

This closes a specific possible repair of
[[research/prime_lattice/findings/PL-471-sparse-zero-annihilators-force-prime-variance-on-every-large-block|PL-471]]:
its genus-zero Mellin annihilator cannot be made into a universal
fixed-box-range-preserving filter merely by changing its subunit-order
entire symbol. The obstruction includes arbitrary infinite canonical
products obeying (1), not just the first-order Euler commutator.

It **does not** decide
[[research/prime_lattice/clues/CLUE-single-box-range-sparse-mellin-interpolation|single-box sparse Mellin interpolation]].
That question asks for one specially chosen input depending on the
whole zero set. Such an input could satisfy the box constraints even
though the same filter fails on other inputs. No single-window
prime-variance floor, variance ceiling, or RH/GRH implication is added.

## 1. The infinite differential series is legitimate on this domain

Cauchy's coefficient estimate, optimized at radius proportional to
\(j^{1/a}\), gives
\[
|p_j|\le C_0B^j/(j!)^{1/a}.                                  \tag{4}
\]
Box convolution preserves the derivative bound defining \(G^q\),
and \(A_hf\) has compact support bounded away from zero.
For a function \(\varphi\) on such a fixed compact interval, use
\[
E^j=\sum_{k=0}^j {j\brace k}u^k\partial_u^k,
\qquad
{j\brace k}\le {j\choose k}k^{j-k}.
\]
The bound counts partitions by choosing one representative per block
and assigning each remaining element to a representative. Since
\(k^{j-k}k!\le j!\), the Gevrey bound implies
\[
\|E^j\varphi\|_\infty\le C_1B_1^j(j!)^q.
\]
Also \(\partial_u^\ell E^j=(E+\ell)^j\partial_u^\ell\).
For each fixed \(\ell\), the same argument and
\((k+\ell)!\le2^{k+\ell}k!\ell!\) yield
\[
\|\partial_u^\ell E^j\varphi\|_\infty
\le C_\ell B_\ell^j(j!)^q.
\]
Combining this with (4) gives a summable series because \(q<1/a\).
Each term has the same compact support. Integration by parts and
uniform convergence prove the stated Mellin multiplier identity.
In particular
\[
\int T_PA_hf=P(1)\int f=0.                                  \tag{5}
\]
The range failure below is not a failure of empirical centering.

## 2. The transposed filter is a Poisson generating function

Fix \(\xi=\xi_n\ne0\). For the bilinear integral pairing, the
transpose of \(-E\) is \(E+1\). Therefore
\[
\widehat{T_P\varphi}(\xi)=\int\varphi(u)F_\xi(u)\,du,
\quad
F_\xi(u)=P(E+1)e^{-i\xi u}
        =\sum_{k\ge0}P(k+1)\frac{(-i\xi u)^k}{k!}.             \tag{6}
\]
Both transposition and the displayed series are valid, not merely
formal. On a compact complex \(u\)-set, summing the absolute values
after expanding the exponential is bounded by
\[
\sum_{k\ge0}\frac{(|\xi|R)^k}{k!}
                   \sum_{j\ge0}|p_j|(k+1)^j
\le C_2\sum_{k\ge0}\frac{(|\xi|R)^k}{k!}
                         \exp(C_2(k+1)^a)<\infty.
\]
Here (4) bounds the absolute coefficient majorant by an exponential
of order \(a\). Thus \(F_\xi\) is entire and all exchanges in (6)
are justified.

Put \(a_k=P(k+1)\), and define the Poisson generating function
\[
G(z)=e^{-z}\sum_{k\ge0}a_k\frac{z^k}{k!}
    =\sum_{m\ge0}\Delta^m a_0\frac{z^m}{m!},
\quad
\Delta^m a_0=\sum_{k=0}^m(-1)^{m-k}{m\choose k}P(k+1).
                                                               \tag{7}
\]
The second equality is the classical binomial-transform identity
(source 155). Absolute convergence of the double series follows
already from \(|a_k|\le C\exp(C(k+1)^a)\).
Equation (6) becomes
\[
F_\xi(u)=e^{-i\xi u}G(-i\xi u).                              \tag{8}
\]

Crucially, \(G\) also has order below one. For \(m\ge1\), repeated
fundamental-theorem-of-calculus integration gives
\[
\Delta^m a_0=\int_{[0,1]^m}P^{(m)}(1+t_1+\cdots+t_m)\,dt.
\]
Cauchy's derivative bound with \(R=m^{1/a}\), together with
\((x+y)^a\le x^a+y^a\), gives
\[
\begin{aligned}
|\Delta^m a_0|
&\le C m!R^{-m}\exp\bigl(C(m+1+R)^a\bigr)\\
&\le C_3 B_3^m m!m^{-m/a}
 \le C_3B_3^m(m!)^{1-1/a}.                                   \tag{9}
\end{aligned}
\]
Consequently
\[
|G(z)|\le C_4\sum_{m\ge0}\frac{(B_3|z|)^m}{(m!)^{1/a}}
       \le C_5\exp(C_5|z|^a).                                \tag{10}
\]
For the last bound, Stirling's inequality places the maximal term at
\(m=O(|z|^a)\); beyond a sufficiently large multiple of that index
successive terms have ratio at most \(1/2\). The polynomial number
of earlier terms is absorbed into the exponential. This estimate is
what prevents an infinite symbol from evading the polynomial case.

## 3. A single preserved box zero forces periodicity and constancy

Assume the left side of (3). Fubini and (6) give
\[
0=\int_J f(v)B_\xi(v)\,dv,
\qquad B_\xi(v)=h^{-1}\int_0^hF_\xi(v+t)\,dt.                \tag{11}
\]
We may take \(f=\eta'\) for every \(\eta\in G_c^q(J)\).
Integration by parts implies \(B_\xi'=0\) on \(J\): scaled
Gevrey bumps form approximate point masses, and \(B_\xi'\) is
continuous. Hence
\[
F_\xi(v+h)-F_\xi(v)=0\quad(v\in J).
\]
Both sides are entire, so the identity holds on the whole complex
plane. Since \(e^{-i\xi h}=1\), (8) implies
\[
G(z-2\pi i n)=G(z)\qquad(z\in\mathbb C).                    \tag{12}
\]

A nonzero entire function bounded by \(C\exp(C|z|^a)\), \(a<1\),
cannot have zeros on an infinite arithmetic progression. Indeed,
after removing any zero at the origin, Jensen's formula gives
\[
n_F(R)\log2\le \log M_F(2R)-\log|F(0)|=O(1+R^a),           \tag{13}
\]
whereas a nontrivial arithmetic progression supplies \(\gg R\)
zeros. This is the classical zero-count consequence of Jensen's
formula (source 156).

Apply it to \(G-G(0)\), whose zeros include every multiple of
\(2\pi i n\) by (12). Thus \(G\equiv c\). Comparing Taylor
coefficients in (7) gives \(P(k+1)=c\) for every \(k\ge0\).
Applying (13) again to \(P-c\) yields \(P\equiv c\).
Conversely a constant filter preserves every box zero. This proves (3).

The contrapositive also identifies a witness. If \(P\) is nonconstant,
then \(B_\xi'\) is nonzero somewhere in \(J\). A sufficiently small
Gevrey bump \(\eta\) around such a point has
\(\int\eta B_\xi'\ne0\), and \(f=\eta'\) is a mean-zero input
with \(\widehat{T_PA_hf}(\xi)\ne0\). No uniform witness norm is
asserted.

## Checks, prior art and the remaining question

The first-order check is especially transparent. For \(P(s)=s\),
\[
\widehat{-E A_hf}(\xi_n)=\widehat f(\xi_n),\qquad n\ne0,
\]
because \(\widehat{-E\varphi}=\widehat\varphi+
\xi\partial_\xi\widehat\varphi\) and
\(\xi_n\widehat b_h'(\xi_n)=1\), where
\(b_h=h^{-1}\mathbf1_{[0,h]}\). This checks the transpose shift,
Fourier sign and box normalization. Exact rational-arithmetic checks
of (7) for \(P(s)=s^d\), \(0\le d\le12\), agree with repeated
application of \(z\partial_z+1\) to \(e^z\); they are auxiliary
algebra checks, not evidence for the infinite-order argument.

[Flajolet--Sedgewick (1995), §1, equation (5)](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf)
provides the classical finite-difference/exponential-generating-function
identity underlying (7). [Jensen (1899), equations (8)--(9)](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5052-11511_2006_Article_BF02417878.pdf)
provides the classical entire-function zero-count principle.
The Gevrey domain and sparse-product coefficient estimate are the same
ones used in PL-471. Box-multiplier zeros and compact convolution
inversion are the classical background already compared with sources
140 and 142 in PL-473 and PL-475. None of these sources is cited as
claiming the specific fixed-box Mellin-preserver theorem (3).

The local delta is the classification of **all** symbols satisfying
(1), including infinite sparse products: universal preservation fails
even for one required harmonic and even after restricting inputs to
mean zero. The proof combines classical tools; external priority is
not asserted.

- The universal quantifier over inputs is essential. The theorem
  does not say that \(T_PA_hf\) leaves the range for every nonzero
  \(f\), or that a joint Mellin/Fourier interpolant cannot exist.
- The growth bound is essential to the stated proof. No assertion
  about arbitrary order-one symbols, nonlocal dilation operators,
  input-dependent correction operators, or distributional inputs is
  made. The convergence domain in §1 must not be dropped.
- Constants, including zero, pass the test. The argument works for
  complex symbols and complex tests; it assumes neither positivity
  nor conjugation symmetry.
- This is an analytic obstruction independent of prime coefficients.
  Prime support, Helson phases and generalized-prime models cannot
  change it. Those sources still require their own explicit-formula
  and noncancelling-residue input for any variance consequence.
- The single-box clue remains proposed. Its surviving task is to
  choose a compatible input or construct an admissible sparse-set
  counterexample; universal Mellin filtering no longer supplies a
  possible missing compatibility lemma. No Lean verification or
  independent adversarial approval is claimed.
