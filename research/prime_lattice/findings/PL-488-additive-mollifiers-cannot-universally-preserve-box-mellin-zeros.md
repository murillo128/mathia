# PL-488 — Additive mollifiers cannot universally preserve fixed-box Mellin zeros

**Evidence/status:** EXACT-DERIVED / NEGATIVE-OBSTRUCTION;
CLASSICAL MONODROMY AND COMPACT MOMENT-UNIQUENESS INGREDIENTS;
NO INFINITE-INTERPOLATION NONEXISTENCE OR EXTERNAL NOVELTY CLAIM.

## Claim and relevance to fixed-box interpolation

Let \(h>0\), \(r>0\), and let \(J\Subset(r,\infty)\) be a nonempty
open interval. Let \(\mu\) be a finite complex Borel measure supported
in \([-r,r]\), and define
\[
C_\mu f(v)=\int f(v-t)\,d\mu(t),\qquad
A_hf(u)=h^{-1}\int_0^h f(u-v)\,dv,
\]
\[
K_{s,h}(v)=h^{-1}\int_0^h(v+w)^{s-1}\,dw,
\qquad \Phi_{h,f}(s)=\int f(v)K_{s,h}(v)\,dv.
\tag{1}
\]
The powers use the real logarithm on positive arguments. The support
assumptions ensure that all transforms below are defined; in particular

\(\Phi_{h,f}(s)=\int A_hf(u)u^{s-1}\,du\).

Fix a finite nonempty set of distinct points
\(\Lambda\subset\{s:0<\Re s<1\}\), and one
\(\lambda_*\in\Lambda\). Then
\[
\boxed{
\begin{gathered}
\text{For every }f\in C_c^\infty(J;\mathbb C),\\
\int f=0,\quad \Phi_{h,f}(\lambda)=0\ (\lambda\in\Lambda)
\ \Longrightarrow\ \Phi_{h,C_\mu f}(\lambda_*)=0
\end{gathered}
\quad\Longleftrightarrow\quad \mu=c\delta_0.}
\tag{2}
\]
The same equivalence holds when the inputs are restricted to compact
Gevrey functions of any fixed order \(q>1\). Constants in their derivative
bounds may depend on the input. The measure may depend on the entire
finite packet, \(h\), and \(J\), but is fixed before the universal input.

Thus even preserving **one chosen output zero** for every centered input
satisfying a whole finite packet forces scalar identity convolution.
If \(\mu=\eta(t)\,dt\) with \(\eta\in C_c^\infty\), (2) forces
\(\eta=0\). In particular no normalized compact mollifier has this
universal preservation property, even if it is signed or complex.

This tests a specific possible regularity upgrade in the
[[research/prime_lattice/clues/CLUE-single-box-range-sparse-mellin-interpolation|single-box clue]].
Additive convolution commutes with the box operator and a Gevrey
mollifier produces a Gevrey input. Nevertheless it cannot automatically
retain a finite packet of exact Mellin zeros. Consequently ordinary
mollification alone does not turn an arbitrary smooth finite-packet
solution into the Gevrey input required by
[[research/prime_lattice/findings/PL-487-sparse-mellin-division-preserves-gevrey-decay-and-support|PL-487]].
One can choose \(J\) strictly inside the clue's interval and take \(r\)
small enough that the convolution support stays inside that interval;
the obstruction is not caused by support leakage.

The universal quantifier is essential. This does **not** rule out a
mollifier chosen for one particular input, preservation on an infinite
constraint subspace, direct Gevrey interpolation, or smoothing followed
by exact corrections. It does not settle the clue's existence question.

## 1. Preservation forces a finite analytic span relation

Set \(K_\lambda=K_{\lambda,h}\) and
\[
H(v)=\int K_{\lambda_*}(v+t)\,d\mu(t).
\tag{3}
\]
Fubini, with the sign dictated by \(f(v-t)\), gives
\[
\Phi_{h,C_\mu f}(\lambda_*)=\int f(v)H(v)\,dv.
\tag{4}
\]
All these functionals are complex linear, with no conjugation in the
pairing. If the implication in (2) holds, the last functional vanishes
on the kernel of the finite map
\[
f\longmapsto\left(\int f,(\Phi_{h,f}(\lambda))_{\lambda\in\Lambda}\right).
\]
It therefore factors through the image of that map; extending the
resulting functional to its finite-dimensional codomain yields
\[
H(v)=a_0+\sum_{\lambda\in\Lambda}a_\lambda K_\lambda(v)
\quad(v\in J).
\tag{5}
\]
Equality of the distributions is pointwise because the functions are
analytic. For Gevrey inputs the same conclusion follows by testing the
difference against scaled compact Gevrey bumps centered at each point
of \(J\); these approximate point evaluation. Such bumps exist for every
\(q>1\), as in the Gevrey construction used by PL-487.

All functions in (5) are holomorphic on \(\Re v>r\). Integration
against the finite measure is locally uniformly convergent there.
The identity theorem extends (5) to this half-plane and hence to all
sufficiently large positive \(v\).

## 2. Distinct exponents prevent mixing between the finite constraints

Put \(z=1/v\). On a small punctured disk, with a chosen branch,
\[
K_\lambda(1/z)=z^{1-\lambda}B_\lambda(z),\qquad
B_\lambda(z)=h^{-1}\int_0^h(1+wz)^{\lambda-1}\,dw,
\tag{6}
\]
\[
H(1/z)=z^{1-\lambda_*}C(z),\qquad
C(z)=h^{-1}\int\!\int_0^h
 (1+(t+w)z)^{\lambda_*-1}\,dw\,d\mu(t).
\tag{7}
\]
Here \(B_\lambda,C\) are single-valued analytic germs at zero and
\(B_\lambda(0)=1\). Compact support justifies the convergent binomial
expansions and integrations when \(|z|(r+h)<1\).

Analytic continuation once around zero multiplies the term in (6)
by \(\omega_\lambda=e^{2\pi i(1-\lambda)}\). The multipliers
\(1,(\omega_\lambda)_{\lambda\in\Lambda}\) are all distinct:
equality between two would require their exponents to differ by an
integer, impossible for distinct points in this open strip.

Apply to (5) polynomials in this continuation operator. A polynomial
equal to one at one of the finitely many multipliers and zero at all
the others projects onto its corresponding summand. The constant
summand gives \(a_0=0\); each \(\lambda\ne\lambda_*\) gives
\(a_\lambda B_\lambda=0\), so \(a_\lambda=0\). Consequently
\[
H(v)=cK_{\lambda_*}(v),\qquad C(z)=cB_{\lambda_*}(z).
\tag{8}
\]
At \(z=0\), (7) identifies \(c=m_0:=\mu(\mathbb R)\).
This step is why allowing a finite packet of other zero constraints
does not provide a universal smoothing escape.

## 3. The remaining eigenfunction identity determines every kernel moment

Let \(m_j=\int t^j\,d\mu(t)\). Comparing the coefficients of \(z^n\)
in (8), and cancelling the nonzero number
\(\binom{\lambda_*-1}{n}\), gives
\[
\sum_{j=0}^n\binom nj m_j\frac{h^{n-j}}{n-j+1}
       =m_0\frac{h^n}{n+1}\qquad(n\ge0).
\tag{9}
\]
The binomial coefficient is nonzero at every order because
\(\lambda_*-1\) is not a nonnegative integer. The \(j=0\) term
already equals the right side. Induction in \(n\ge1\) therefore gives
\[
m_n=0\qquad(n\ge1).
\tag{10}
\]
The compact measure \(\mu-m_0\delta_0\) has every polynomial moment
zero. Polynomials are uniformly dense in continuous functions on a
compact real interval, and integration against a finite complex measure
is continuous in that norm. Hence this measure is zero. Equivalently,
its entire Fourier transform has every Taylor coefficient zero, and
Fourier uniqueness gives the same conclusion. Thus
\(\mu=m_0\delta_0\). Conversely scalar identity convolution plainly
satisfies (2), completing the proof.

## Checks, prior art and precise boundary

The first two nonconstant equations in (9) read

\(m_1+(h/2)m_0=(h/2)m_0\),

\(m_2+hm_1+(h^2/3)m_0=(h^2/3)m_0\).

They force \(m_1=m_2=0\). A nonzero translation of a Dirac mass fails
the first test; a symmetric normalized positive mollifier passes that
test but fails the second. The proof through all moments is needed for
signed or complex kernels, whose initial moments can vanish. These are
exact normalization and degeneracy checks, not numerical evidence for
the general theorem.

The strip assumption has real content. At \(s=1\), \(K_{1,h}=1\) and
the zero condition is just centering, preserved by every convolution.
At \(s=2\), \(K_{2,h}(v)=v+h/2\), and its transpose under convolution
is \(m_0K_{2,h}+m_1\); every convolution therefore preserves that zero
on centered inputs. Polynomial exponents do not force all moments.
Outside a strip of width one, integer differences also defeat the
distinct-monodromy argument; no classification there is asserted.

The underlying uniqueness mechanism is classical. For real
\(0<\lambda<1\), (7) before the \(z=1/v\) substitution is a generalized
Stieltjes transform of the convolution of \(\mu\) with the normalized
box, of order \(1-\lambda\). [Schwarz (2005), equations (8) and
(22)--(25)](https://arxiv.org/pdf/math-ph/0405050) describes this
transform and its iterated-Laplace inversion for positive real order.
The complex-exponent, compact-measure argument above is supplied
directly; that paper is not invoked as a fixed-box preserver theorem.
Compact moment uniqueness, finite-dimensional duality and separation
by monodromy are standard ingredients. No external priority is claimed.

The local mathematical delta is a classification of a different repair
from [[research/prime_lattice/findings/PL-486-subunit-order-mellin-filters-cannot-preserve-a-fixed-box-range|PL-486]].
That result obstructs universal **Mellin filtering** while retaining a
box Fourier zero. Here additive convolution retains the box range
automatically, but universal retention of even one specified zero from
a finite Mellin packet forces the identity. It remains possible to
construct compatible inputs directly or repair smoothing errors with
input-dependent corrections. The theorem concerns homogeneous simple
zero constraints; extra selected-value normalization, Hermite conditions
or infinitely many constraints restrict the input class further and
are not silently included in its universal statement.

Finite exact Gevrey interpolation is itself feasible: the independent
analytic functionals can be tested on Gevrey bumps just as on smooth
bumps. The obstruction is to one convolution rule preserving every
finite-packet solution, not to the existence of finite-packet solutions.
An infinite construction still needs support, derivative-seminorm and
selected-value control. The finding neither disproves that construction
nor supplies a single-window variance floor or an arithmetic energy
ceiling. It is independent of prime coefficients, Helson phases and
generalized-prime choices; no RH/GRH progress, Lean verification or
independent adversarial approval is claimed.
