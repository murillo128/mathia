# PC-039 — inverse-square Kron refinement has a rational alias spectrum and no refinement holonomy

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the canonical linear refinement route obtained by integrating a fine regular polygon down to an exact divisor subpolygon with the inverse-square chord Laplacian. The Schur/Kron quotient law is classical; the durable prime-circle result is that this intrinsic nonlocal refinement has an explicit rational Fourier spectrum and erases the order/path by which a divisor scale is reached.

## 1. The cross-scale question left open by the single-level no-go results

PC-014 shows that exact one-dimensional propagation along subdivided circle arcs is spectrally blind to intermediate vertices. PC-033/PC-034 classify substantial parts of the single-level multi-grounded inverse-square route, while PC-037/PC-038 rule out broad shell-independent rotation-invariant and merely pointed repairs.

A genuinely different construction remains natural in the original roots-of-unity tower. Whenever

\[
d\mid n,
\qquad n=md,
\]

the coarse polygon is literally a subset of the fine one:

\[
P_d=\mu_d\subset\mu_n=P_n.
\]

Instead of sampling or discarding the fine vertices, one can **integrate them out** from the canonical nonlocal inverse-square chord energy. This is the graph-theoretic/electrical operation of Kron reduction, i.e. the Schur complement of the fine Laplacian with respect to the eliminated vertices.

Because the original inverse-square operator couples every pair of polygon vertices, this route is genuinely nonlocal and two-dimensional in its circle embedding; it is not the degree-two subdivision collapse of PC-014.

The question is whether exact refinement/coarse-graining across the divisor tower produces new arithmetic spectral dynamics, especially an order-sensitive prime-refinement effect when the same level can be reached through different divisor chains.

It does not.

## 2. Canonical inverse-square chord Laplacian and divisor-subpolygon reduction

Let

\[
z_a=e^{2\pi ia/n},
\qquad a\in\mathbb Z/n\mathbb Z,
\]

and let

\[
(\mathcal L_n f)_a
=
\sum_{b\ne a}
\frac{f_a-f_b}{|z_a-z_b|^2}.
\]

As used in PC-032, this circulant Laplacian has normalized Fourier eigenvectors

\[
f_k(a)=n^{-1/2}e^{2\pi ika/n}
\]

with exact eigenvalues

\[
\boxed{
\lambda_k^{(n)}=\frac{k(n-k)}2,
\qquad 0\le k<n.
}
\]

Fix a proper divisor `d` with `2 <= d < n`, write `n=md`, and keep the subgroup vertices

\[
H=\{0,m,2m,\ldots,(d-1)m\}\cong\mathbb Z/d\mathbb Z,
\]

which are exactly `P_d` inside `P_n`. Let `I` be the remaining fine vertices. The intrinsic effective operator on the coarse polygon is

\[
\boxed{
K_{n\to d}
:=
(\mathcal L_n)_{HH}
-(\mathcal L_n)_{HI}
(\mathcal L_n)_{II}^{-1}
(\mathcal L_n)_{IH}.
}
\]

The interior Dirichlet block is positive definite because `\mathcal L_n` is the Laplacian of a connected positive-weight graph and a nonempty boundary is retained. Hence the reduction is well-defined without a pseudoinverse or an added gauge.

Equivalently, for prescribed boundary values `y`,

\[
y^*K_{n\to d}y
=
\min_{x|_H=y}x^*\mathcal L_nx.
\]

The subgroup symmetry makes `K_{n\to d}` circulant on `P_d`.

## 3. Exact alias/harmonic-mean spectrum

Let

\[
g_j(s)=d^{-1/2}e^{2\pi ijs/d},
\qquad 0\le j<d,
\]

be a coarse Fourier mode. On the retained vertices `a=ms`, every fine Fourier mode whose frequency satisfies

\[
k\equiv j\pmod d
\]

has the same boundary phase. Thus the fine frequencies in the alias class are

\[
k=j+rd,
\qquad 0\le r<m.
\]

Because

\[
f_{j+rd}(ms)=m^{-1/2}g_j(s),
\]

a fine extension

\[
x=\sum_{r=0}^{m-1}\alpha_r f_{j+rd}
\]

has boundary coefficient `y_j` precisely when

\[
\sum_{r=0}^{m-1}\alpha_r=\sqrt m\,y_j.
\]

For `j != 0`, minimizing the diagonal Fourier energy

\[
\sum_r\lambda_{j+rd}^{(n)}|\alpha_r|^2
\]

under this single constraint gives, by the weighted Cauchy-Schwarz equality case,

\[
\alpha_r
\propto
\frac1{\lambda_{j+rd}^{(n)}}.
\]

Therefore the coarse eigenvalue is the exact harmonic alias mean

\[
\boxed{
\mu_j(n\to d)
=
\frac{m}
{\displaystyle\sum_{r=0}^{m-1}\frac1{\lambda_{j+rd}^{(n)}}},
\qquad 1\le j<d.
}
\]

The constant mode extends constantly with zero energy, so

\[
\boxed{\mu_0(n\to d)=0.}
\]

This formula is not a numerical fit. It is exactly the Schur-complement spectrum of the fine nonlocal Laplacian on the divisor subpolygon.

## 4. The apparent digamma structure collapses to finite rational harmonic sums

Put

\[
x=\frac jd.
\]

Using

\[
\lambda_{j+rd}^{(n)}
=
\frac{d^2(r+x)(m-r-x)}2
\]

and

\[
\frac1{u(m-u)}
=
\frac1m\left(\frac1u+\frac1{m-u}\right),
\]

we obtain

\[
\sum_{r=0}^{m-1}
\frac1{\lambda_{j+rd}^{(n)}}
=
\frac{2}{d^2m}
D_m(x),
\]

where

\[
D_m(x)
:=
\sum_{r=0}^{m-1}
\left(
\frac1{r+x}
+
\frac1{r+1-x}
\right).
\]

It can be packaged as a digamma difference,

\[
D_m(x)
=
\psi(m+x)+\psi(m+1-x)-\psi(x)-\psi(1-x),
\]

but in the prime-circle specialization `x=j/d` that notation hides a stronger elementary fact. Directly,

\[
D_m(j/d)
=
d\left[
\sum_{r=0}^{m-1}\frac1{j+rd}
+
\sum_{s=1}^{m}\frac1{sd-j}
\right].
\]

Hence

\[
\boxed{
\mu_j(n\to d)
=
\frac{n^2}
{2d\left(
\displaystyle\sum_{r=0}^{m-1}\frac1{j+rd}
+
\displaystyle\sum_{s=1}^{m}\frac1{sd-j}
\right)}
\in\mathbb Q.
}
\]

Thus an expression that superficially resembles an archimedean gamma/digamma contribution is, at every finite divisor refinement, only a finite rational combination of reciprocal arithmetic progressions. There is no spectral variable whose analytic continuation could supply the gamma factor, Riemann zeros, or a critical-line symmetry.

As an exact audit, reduce the decagon to its pentagon, `n=10`, `d=5`, `m=2`. For `j=1`, the alias frequencies are `1,6`, with

\[
\lambda_1=\frac92,
\qquad
\lambda_6=12,
\]

so

\[
\mu_1
=
\frac2{2/9+1/12}
=
\frac{72}{11}.
\]

For `j=2`, the aliases are `2,7`, with `\lambda_2=8` and `\lambda_7=21/2`, giving

\[
\mu_2
=
\frac2{1/8+2/21}
=
\frac{336}{37}.
\]

Therefore

\[
\boxed{
\operatorname{Spec}(K_{10\to5})
=
\left\{
0,
\frac{72}{11},
\frac{336}{37},
\frac{336}{37},
\frac{72}{11}
\right\}.
}
\]

## 5. Exact refinement path independence

The more important obstruction concerns repeated refinement/coarse-graining.

Suppose

\[
d\mid e\mid n.
\]

Then

\[
P_d\subset P_e\subset P_n.
\]

The classical quotient identity for Schur complements says that eliminating variables in stages is exactly the same as eliminating their union at once. Applied to the grounded positive blocks here,

\[
\boxed{
K_{n\to d}
=
\operatorname{Kron}
\left(K_{n\to e},P_d\right).
}
\]

So the effective coarse operator depends only on the endpoint pair `(n,d)`, not on the intermediate divisor chain.

The Fourier formula makes the same fact transparent. For any circulant positive Laplacian spectrum `\lambda_k`, reduction by a subgroup of index `m` sends each nonzero alias class to

\[
\mu_j
=
\frac{m}{\sum_r1/\lambda_{j+rd}}.
\]

If `n=m_1e` and `e=m_2d`, first reducing to `e` and then to `d` nests the harmonic means:

\[
\frac1{\nu_\ell}
=
\frac1{m_1}
\sum_{r_1}\frac1{\lambda_{\ell+r_1e}},
\]

and then

\[
\mu_j
=
\frac{m_2}
{\sum_{r_2}1/\nu_{j+r_2d}}
=
\frac{m_1m_2}
{\sum_{r_2,r_1}1/\lambda_{j+r_2d+r_1e}},
\]

which is exactly the direct alias class for index `m_1m_2=n/d`.

Consequently, if `p` and `q` are distinct primes and the same endpoint scale can be reached by the chains

\[
n\to n/p\to n/(pq)
\]

or

\[
n\to n/q\to n/(pq),
\]

the two resulting coarse operators are identical.

There is therefore no commutator, curvature, ordered-prime memory, or refinement holonomy hidden in exact linear Kron reduction of this fixed nonlocal polygon operator.

## 6. Why this is a decisive negative for the canonical refinement/RG route

This construction survived several previous no-go hypotheses:

- it is not a scalar evaluation of `U_n`;
- it is genuinely nonlocal on the full fine polygon;
- it uses two levels intrinsically related by `P_d subset P_n`;
- it integrates out the fine geometry instead of merely sampling it;
- it produces a nontrivial operator on the retained coarse polygon.

Nevertheless, exact symmetry plus Schur minimization resolves the entire operation into a rational harmonic alias spectrum. More importantly, the quotient law removes the one feature that could have made refinement dynamics richer than endpoint data: **the history/order of refinement is pure gauge for this linear reduction**.

Thus the natural chain

\[
\boxed{
\text{nested root-of-unity polygons}
\to
\text{inverse-square nonlocal energy}
\to
\text{Kron/Schur refinement flow}
\to
\text{ordered prime-scale spectral dynamics}
\to
\text{RH}
}
\]

is ruled out under its stated hypotheses.

The endpoint spectrum may still depend nontrivially on `n` and `d`; the result does not say it is constant or factorization-blind. The obstruction is sharper: its dependence is an explicit finite rational alias transform, and **no additional information can be generated by composing exact divisor refinements in different orders**.

## 7. Prior art and novelty audit

The general mechanisms are classical.

- Calogero--Perelomov, already anchored for PC-032, supplies the classical regular-polygon `csc^2` spectral setting from which `\lambda_k=k(n-k)/2` is taken.
- Florian Dörfler and Francesco Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks*, IEEE Transactions on Circuits and Systems I 60:1 (2013), 150--163, DOI `10.1109/TCSI.2012.2215780`, treat graph-Laplacian Kron reduction as a Schur complement and analyze its algebraic, spectral, resistive, and graph-theoretic properties.
- Douglas E. Crabtree and Emilie V. Haynsworth, *An identity for the Schur complement of a matrix*, Proceedings of the American Mathematical Society 22:2 (1969), 364--366, DOI `10.1090/S0002-9939-1969-0255573-1`, give the classical quotient identity underlying staged-versus-direct elimination.

Targeted searches for combinations of inverse-square/cosecant-squared root-of-unity Laplacians, divisor-subpolygon Kron reduction, and circulant Schur reduction did not locate a source using the exact rational alias formula above as an RH mechanism. That absence is not a novelty proof.

No general theorem novelty is claimed. The durable contribution is the project-specific classification and obstruction: for this canonical prime-circle operator, the intrinsic cross-scale Schur flow is explicitly solvable and composition has no path-dependent arithmetic content.

## 8. Boundary of the no-go

This finding does **not** classify the primitive-set principal blocks

\[
A_n=\mathcal L_n[U(n),U(n)]
\]

of PC-033. For squarefree `n=pq`, the primitive set is not a divisor subgroup `P_d`, so the surviving multi-prime radical problem remains distinct.

It also does not rule out:

- an operator that couples several levels simultaneously rather than eliminating one fixed fine operator down a divisor chain;
- shell-dependent or anchor-asymmetric off-diagonal kernels;
- nonlinear elimination/variational principles for which Schur associativity no longer applies;
- operators retaining correlations between eliminated fields rather than only their minimum-energy boundary response;
- global uniformization, monodromy, Liouville, or Weil--Petersson data from PC-017.

A viable refinement mechanism must therefore contain structure that is **not functorial linear Schur elimination of a single translation-invariant fine-level operator**. In particular, if ordered prime refinements are to matter, that noncommutativity must be created intrinsically before the reduction; exact Kron reduction cannot generate it afterwards.

## 9. Exact audit/falsification tests

Under the stated hypotheses the claim is finite-dimensional and directly falsifiable. Any one of the following would invalidate it:

1. a direct Schur complement `K_{n->d}` whose nonzero Fourier eigenvalue differs from `m / sum_r 1/lambda_{j+rd}`;
2. a divisor pair for which the rational reciprocal-progression formula differs from that alias eigenvalue;
3. a nested triple `d|e|n` for which staged Kron reduction differs from direct reduction;
4. two divisor chains with the same endpoints that produce different coarse operators.

The first two contradict the Fourier constrained-minimization calculation; the latter two contradict the classical Schur-complement quotient identity. The obstruction is therefore exact for the canonical linear refinement route.