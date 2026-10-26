# XF-211 — three-gap periodic triple discriminants are strictly monotone

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `STRUCTURAL/DYNAMIC`.

The finite-gap overlap question has a positive answer for a complete
three-gap period. Let \(x_{i+3}=x_i+L\), \(L>0\), be an ordered
real-simple periodic logarithmic zero flow with the opening-time sign

\[
x_i'=2\operatorname{PV}\sum_{k\ne i}\frac1{x_i-x_k}.
\]

Write its three gaps as \(a,b,c>0\), with \(a+b+c=L\), and use the
normalized triple discriminant of XF-030,

\[
J(p,q)=2\log p+2\log q+2\log(p+q)
 -3\log\!\left[\frac23(p^2+pq+q^2)\right].
\]

Then the full one-period sum satisfies

\[
\boxed{\mathcal H(a,b,c):=J(a,b)+J(b,c)+J(c,a),\qquad
 \mathcal H'\ge0,}
\tag{1}
\]

with equality exactly at \(a=b=c\). This holds at arbitrary positive
gap ratios, without a small-perturbation assumption or a prescribed
lower-gap bound. In fact \(\mathcal H\) increases under **every symmetric
positive-conductance diffusion of three positive coordinates**.

The reason is specific and testable: the cyclic sum on three gaps
contains all unordered pairs and is strictly Schur-concave. Section 2
gives an explicit positive polynomial certificate, and Section 3
retains every periodic image in the actual heat-flow application.
This is an aggregate statement; individual triple derivatives need
not be assigned a sign by the proof.

## 1. The three-coordinate gradient

Put \(S_{uv}=u^2+uv+v^2\). Expanding the three terms gives

\[
\mathcal H=4\log(abc)+2\log[(a+b)(b+c)(c+a)]
 -3\log(S_{ab}S_{bc}S_{ca})-9\log(2/3).
\tag{2}
\]

In particular \(\mathcal H\) is symmetric in \(a,b,c\), not merely
invariant under cyclic relabeling. Direct differentiation, with the
three variables independent before restricting to a fixed sum, gives

\[
\boxed{\mathcal H_a-\mathcal H_b=-(a-b)D(a,b;c),}
\tag{3}
\]
where

\[
D(a,b;c)=\frac4{ab}+\frac2{(a+c)(b+c)}+\frac3{S_{ab}}
 -\frac{3[2ab+c(a+b)-c^2]}{S_{ac}S_{bc}}.
\tag{4}
\]

For example, the only potentially adverse term follows from

\[
\frac{2a+c}{S_{ac}}-\frac{2b+c}{S_{bc}}
 =\frac{(a-b)[c^2-c(a+b)-2ab]}{S_{ac}S_{bc}}.
\]

Thus strict concavity in the *logarithmic contrast* of one triple is
not being confused with concavity in the physical gaps. The needed
physical-gap gradient comparison is proved separately.

## 2. A positive coefficient certificate

Let

\[
Q=ab(a+c)(b+c)S_{ac}S_{bc}>0.
\]

The exact numerator identity is

\[
\boxed{D(a,b;c)=\frac3{S_{ab}}+\frac{P(a,b,c)}Q,}
\tag{5}
\]
with

\[
\begin{aligned}
P={}&a^2b^2(a+b)c
 +ab(7a^2+9ab+7b^2)c^2\\
 &+[4(a^3+b^3)+18ab(a+b)]c^3\\
 &+[8(a^2+b^2)+21ab]c^4
 +8(a+b)c^5+4c^6.
\end{aligned}
\tag{6}
\]

Every coefficient is positive. One can verify (6) simply by expanding

\[
4(a+c)(b+c)S_{ac}S_{bc}+2abS_{ac}S_{bc}
 -3ab(a+c)(b+c)[2ab+c(a+b)-c^2].
\tag{7}
\]

Consequently \(D(a,b;c)>3/S_{ab}>0\), and the analogous identities
hold for every pair by symmetry. Equation (3) is the strict
Schur--Ostrowski gradient criterion for Schur concavity. Only its
displayed pairwise inequality, not an imported majorization theorem,
is needed below.

Indeed, suppose \(z=(a,b,c)\) obeys

\[
z_i'=2\sum_{j\ne i}C_{ij}(z_j-z_i),\qquad
C_{ij}=C_{ji}>0.
\tag{8}
\]

The coefficients may depend on time and the entire current state.
Pairing the two directed terms, and writing \(k\) for the remaining
coordinate, yields the exact production formula

\[
\boxed{\mathcal H'
 =2\sum_{i<j}C_{ij}(z_i-z_j)^2D(z_i,z_j;z_k)
 \ge6\sum_{i<j}C_{ij}\frac{(z_i-z_j)^2}{S_{z_i z_j}}.}
\tag{9}
\]

No derivative of \(C_{ij}\) is involved. The sum is strictly positive
unless all three gaps coincide. This proves the claimed sign and
equality case independently of the special form of the heat-flow
conductances.

## 3. Complete periodic heat flow, including the third gap

For any initial \(a,b,c>0\), set \(L=a+b+c\) and

\[
f_0(z)=\sin\frac{\pi z}L\,
       \sin\frac{\pi(z-a)}L\,
       \sin\frac{\pi(z-a-b)}L,
\qquad f_t=e^{-t\partial_z^2}f_0.
\tag{10}
\]

The third gap is the distance from \(a+b\) to the next copy of zero,
not an artificial endpoint. The finite Fourier sum defines (10) for
all real \(t\). At every real-simple slice its roots obey

\[
x_i'=\frac{2\pi}{L}\sum_{\substack{0\le j<3\\j\ne i}}
 \cot\frac{\pi(x_i-x_j)}L.
\tag{11}
\]

This is the full reciprocal field by the cotangent partial fraction;
same-residue self-images cancel in symmetric pairs. The exact gap
identity used in XF-041 gives

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),\qquad
c_{ik}=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0.
\tag{12}
\]

It can also be derived by shifting one of the two velocity sums when
forming \(x_{i+1}'-x_i'\). Periodicity gives \(x_k=Lk/3+O(1)\), so
the unmatched endpoints vanish and the difference sum converges
absolutely. Collecting residues defines

\[
C_{ij}=\sum_{n\in\mathbb Z}c_{i,j+3n}\quad(i\ne j).
\tag{13}
\]

These sums converge, are positive, and satisfy \(C_{ij}=C_{ji}\):
exchange the root indices and shift both by a whole period.
Terms with the same residue have \(g_k-g_i=0\). Thus (12) becomes
exactly (8), and (9) proves (1) for the complete flow.

For completeness this flow stays real and simple for every forward
time \(t\ge0\). The minimum gap is nondecreasing and the maximum
nonincreasing under (8), so each remains in the positive compact
interval set by the initial gaps. The sum of the three velocities in
(11) is zero; after fixing the center, the ordered configurations stay
in a compact subset away from collision. The finite ODE therefore
continues. Initially the roots agree with (10) by implicit
differentiation and uniqueness. Multiplying \(f_t(z)\) by
\(e^{3\pi iz/L}\) gives a degree-three polynomial in
\(e^{2\pi iz/L}\) with nonzero extreme coefficients; the three
continued roots per period exhaust its roots. This maintains the
agreement at every finite forward time. There is no finite-polynomial
truncation or omitted exterior field in the argument.

## 4. What this excludes, and why three does not settle larger periods

A constant-weight collection of whole three-gap periods has derivative
equal to the number of periods times \(\mathcal H'\ge0\). A fixed
three-gap shape therefore cannot furnish a negative interior *mean*
production for the overlap/taper question. This strengthens XF-041's
eventual variance damping in a different direction: the singular
normalized shape sum itself has the right instantaneous sign at every
positive-gap slice of this class.

There is also a growing-buffer consequence with explicit quantifiers.
Fix one such configuration at one time, let
\(p_j=\mathcal J_j'\) be its three-periodic derivative sequence, and
let \(A\in C_c^\infty(\mathbb R)\) be fixed, nonnegative, nonzero.
For \(a_j^{(M)}=A(j/M)\), finite Fourier decomposition of \(p\) gives,
for every integer \(r\ge1\),

\[
\sum_j a_j^{(M)}p_j
 =\frac{\mathcal H'}3\sum_j a_j^{(M)}
   +O_{A,r,p}(M^{1-r}).
\tag{14}
\]

To check the remainder, for each nonconstant cubic root of unity
\(\omega\), summation by parts \(r\) times bounds
\(\left|\sum_j A(j/M)\omega^j\right|\) by
\(|1-\omega|^{-r}\sum_j|\Delta^r A(j/M)|=O_{A,r}(M^{1-r})\).
The mean term is positive of order \(M\) for a fixed nonuniform
shape; at the uniform shape every \(p_j=0\). Hence the tapered
derivative is eventually nonnegative. This is **not uniform** over
shapes depending on \(M\), degenerating gaps, or arbitrary weights.

The proof does not extend just by substituting a larger period.
Already at four gaps the cyclic sum is not symmetric in all gap
coordinates. For \(u\ne v>0\),

\[
\begin{aligned}
\mathcal H_4(u,u,v,v)&=-2\log2+2J(u,v),\\
\mathcal H_4(u,v,u,v)&=4J(u,v),\\
\mathcal H_4(u,u,v,v)-\mathcal H_4(u,v,u,v)
 &=2[-\log2-J(u,v)]>0,
\end{aligned}
\tag{15}
\]

where strictness follows from XF-030's unique maximum at equal gaps.
These are permutations of the same gap multiset. Therefore the
Schur-concavity argument is unavailable for the four-gap cyclic
observable. Equation (15) is a boundary of this proof, **not** a
negative-flow example or a proof that larger-period monotonicity fails.

## 5. Prior art, checks, and Xi boundary

Schur concavity, pairwise averaging, and the gradient criterion are
classical; see Marshall, Olkin and Arnold, *Inequalities: Theory of
Majorization and Its Applications*, second edition (2011),
[Chapter 3](https://doi.org/10.1007/978-0-387-68276-1_3).
The reciprocal heat-zero equation is classical, with the opposite
time sign in [Tao's exposition](https://terrytao.wordpress.com/2017/10/17/heat-flow-and-zeroes-of-polynomials/).
Periodic summation uses [DLMF 4.22.3](https://dlmf.nist.gov/4.22.E3).
XF-030 supplies \(J\), and XF-041 already supplies the exact periodic
positive-conductance diffusion; neither construction is new here.

The additional local result is the explicit strict Schur-concavity
certificate (3)--(7) for this nonseparable three-gap observable,
and consequently the complete finite-amplitude production law (9).
This is an application of classical majorization structure, not a
claim of a new general entropy principle or literature-wide novelty.
The targeted prior-art check did not supply this particular
three-gap certificate; the proof does not rely on search absence.

Integer polynomial expansion checks every coefficient in (6) against
(7); exact rational substitution independently checks the gradient
identity (3). The equations above are the analytic proof. No numerical
trajectory search, target-model inference, or Lean validation is
claimed. Equal gaps, arbitrary permutations, positive rescaling,
small positive gaps, the time sign, and all periodic images are
accounted for. At an actual zero gap \(J\) is undefined, and no
collision-crossing claim is made.

The Xi-facing gap remains substantial: Xi is not a three-gap periodic
system. These controls are not asserted to obey its arithmetic source
law, even symmetry, or global counting asymptotic. Arbitrary larger
periods, nonperiodic source replenishment, and uniform taper estimates
remain open. In particular (1) supplies no upper bound on the
de Bruijn--Newman constant and no backward continuation through a
collision. It removes one finite-gap interior counterexample class
from the overlap investigation without settling that investigation.
