# PC-214 — binary mixed-composite mask/transverse compression is a bounded Kronecker-sum spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the first individual mixed-composite coefficient-mask escape left open by PC-212--PC-213: retain the full coefficient field of `Phi_{pq}`, couple it directly to its own exact-order transverse sector before scalar contraction, and ask whether the binary mixed-composite mask creates an irreducible two-prime spectral carrier.

Let `p != q` be primes, `N=pq`, and retain the normalized common-refinement coefficient field of PC-212,

\[
g_N(x)=\sqrt{\frac{N}{h_N}}\,a_N(x\bmod N),
\qquad
\Phi_N(z)=\sum_j a_N(j)z^j,
\qquad
h_N=\sum_j a_N(j)^2,
\tag{1}
\]

on `K=\widehat{\mathbb Z}`. Let `P_N` denote the PC-066 projector onto characters of exact order `N`, and form the source-derived self-adjoint compression

\[
\boxed{
T_{p,q}:=P_NM_{g_N}P_N\big|_{E_N},
\qquad E_N=\operatorname{Ran}P_N.
}
\tag{2}
\]

This is the most direct incidence operator not covered by PC-213: `g_{pq}` is an individual mixed-composite mask and is generally not a compact-open subgroup indicator.

The exact result is strongly restrictive. In the CRT basis

\[
E_{pq}\cong \mathbb C^{(\mathbb Z/p\mathbb Z)^\times}
\otimes
\mathbb C^{(\mathbb Z/q\mathbb Z)^\times},
\tag{3}
\]

one has, up to harmless coordinate permutations,

\[
\boxed{
T_{p,q}
\simeq
B_{p\mid q}\otimes I_{q-1}
+
I_{p-1}\otimes B_{q\mid p}
-c_{p,q}I,
}
\tag{4}
\]

where

\[
c_{p,q}=\frac{1}{\sqrt{pqh_{pq}}}.
\tag{5}
\]

Each one-prime block `B_{p|q}` has **at most three distinct eigenvalues**, with an explicit characteristic polynomial controlled by the modular inverse `q^{-1} mod p`; similarly for `B_{q|p}`. Consequently

\[
\boxed{
|\operatorname{Spec}(T_{p,q})|\le 9
}
\tag{6}
\]

for every pair of distinct primes, even though

\[
\dim E_{pq}=\varphi(pq)=(p-1)(q-1)
\tag{7}
\]

grows without bound.

Thus an individual binary mixed-composite cyclotomic mask does retain genuine cross-prime **modular-inverse parameters**, unlike the prime-power support products of PC-213, but its exact-order transverse operator does not produce an irreducible two-coordinate tensor interaction. It is a Kronecker sum of two one-coordinate blocks and has uniformly bounded spectral complexity. The surviving modular-inverse data are precisely classical binary-cyclotomic coefficient data.

## 1. Fourier support turns the exact-order matrix into a CRT rook operator

PC-212 gives, for every `d|N` and `(a,d)=1`,

\[
\widehat g_N(a/d)
=
\frac{\Phi_N(e^{-2\pi ia/d})}{\sqrt{Nh_N}}.
\tag{8}
\]

For `d=N`, this vanishes because a primitive `N`-th root is a zero of `Phi_N`:

\[
P_Ng_N=0.
\tag{9}
\]

Choose the exact-order character basis indexed by units `r mod N`. The multiplication compression (2) has matrix entries

\[
\langle e_r,T_{p,q}e_s\rangle
=
\widehat g_N((r-s)/N),
\tag{10}
\]

with the fraction reduced to its exact denominator.

Now identify a unit `r mod pq` by its CRT coordinates

\[
(u,v)=(r\bmod p,r\bmod q),
\qquad
u\in(\mathbb Z/p\mathbb Z)^\times,
\quad
v\in(\mathbb Z/q\mathbb Z)^\times.
\tag{11}
\]

For two such units there are only four possibilities.

If both CRT coordinates differ, then `r-s` is coprime to `pq`, so the difference character has exact order `pq`; its matrix entry vanishes by (9). If only the `p`-coordinate differs, then `q|(r-s)` and the difference has exact order `p`. If only the `q`-coordinate differs, the difference has exact order `q`. If both coordinates agree, the entry is the constant Fourier mode.

Therefore the matrix has exactly the support pattern of a rook operator on the Cartesian product of the two reduced residue sets: it can change the `p` coordinate or the `q` coordinate, but never both at once. This proves the tensor shape (4) once the two one-coordinate kernels are identified.

Put

\[
S:=\sqrt{pqh_{pq}},
\qquad c_{p,q}=S^{-1}.
\tag{12}
\]

For a nontrivial `p`-th root `z`, the elementary binary cyclotomic identity

\[
\Phi_{pq}(z)=\frac{\Phi_p(z^q)}{\Phi_p(z)}
\tag{13}
\]

is interpreted by cancellation at the common simple zero. Using

\[
\Phi_p'(\zeta)=\frac{p\zeta^{p-1}}{\zeta-1}
\qquad(\zeta^p=1,\ \zeta\ne1),
\tag{14}
\]

gives exactly

\[
\boxed{
\Phi_{pq}(z)
=q\frac{1-z}{1-z^q}.
}
\tag{15}
\]

Hence the full cyclic `p x p` convolution kernel whose principal reduced-residue block is `B_{p|q}` is

\[
\kappa_{p\mid q}(0)=S^{-1},
\qquad
\kappa_{p\mid q}(t)
=
\frac qS
\frac{1-\omega_p^{-t}}{1-\omega_p^{-qt}}
\quad(t\ne0).
\tag{16}
\]

The CRT identification may multiply `t` by a unit modulo `p`; that merely permutation-conjugates the resulting block. Interchanging `p` and `q` gives the second factor in (4). The diagonal constant occurs in both principal blocks, so one copy `c_{p,q}I` must be subtracted, yielding exactly (4).

## 2. Binary residue sums have only two levels

The one-coordinate block is even more rigid than (16) first suggests.

Let

\[
A_{p\mid q}(r)
:=
\sum_{\substack{j\ge0\\j\equiv r\ (\mathrm{mod}\ p)}}a_{pq}(j),
\qquad 0\le r<p,
\tag{17}
\]

and define the degree-`<p` residue polynomial

\[
R_{p\mid q}(z)
:=\sum_{r=0}^{p-1}A_{p\mid q}(r)z^r.
\tag{18}
\]

Choose the least positive inverse

\[
\alpha\in\{1,\ldots,p-1\},
\qquad
q\alpha\equiv1\pmod p,
\tag{19}
\]

and write

\[
q\alpha=1+\beta p,
\qquad \beta\in\mathbb Z_{\ge0}.
\tag{20}
\]

Then the following polynomial identity holds exactly:

\[
\boxed{
R_{p\mid q}(z)
=
q\sum_{j=0}^{\alpha-1}z^{jq\bmod p}
-\beta(1+z+\cdots+z^{p-1}).
}
\tag{21}
\]

To prove it, evaluate both sides on all `p`-th roots. At `z=1`, the right side is

\[
q\alpha-\beta p=1=\Phi_{pq}(1).
\tag{22}
\]

At a nontrivial `p`-th root, the second term vanishes and `q\alpha=1+\beta p` gives

\[
q\sum_{j=0}^{\alpha-1}z^{jq}
=q\frac{1-z^{q\alpha}}{1-z^q}
=q\frac{1-z}{1-z^q}
=\Phi_{pq}(z),
\tag{23}
\]

by (15). Both sides of (21) have degree `<p`, so equality at all `p`-th roots proves the identity.

Equation (21) immediately yields the two-level residue law

\[
\boxed{
A_{p\mid q}(r)=
\begin{cases}
q-\beta,&r\in\{0,q,2q,\ldots,(\alpha-1)q\}\pmod p,\\
-\beta,&\text{otherwise}.
\end{cases}
}
\tag{24}
\]

Thus the mixed prime `q` survives in the `p`-coordinate channel only through the elementary Euclidean/modular-inverse pair `(\alpha,\beta)`, where `q\alpha-\beta p=1`. This is already the classical arithmetic governing binary cyclotomic coefficients.

## 3. The one-coordinate principal block has at most three eigenvalues

Let `C_{p|q}` be the full `p x p` circulant with kernel (16). Fourier diagonalization and (17)--(18) give only two eigenvalues:

\[
\boxed{
a_{p\mid q}:=\frac{p(q-\beta)}S
\quad\text{with multiplicity }\alpha,
}
\tag{25}
\]

and

\[
\boxed{
b_{p\mid q}:=-\frac{p\beta}S
\quad\text{with multiplicity }p-\alpha.
}
\tag{26}
\]

The block `B_{p|q}` is the principal minor obtained by deleting the zero residue, because exact-order `pq` characters have nonzero CRT coordinates. Since every Fourier eigenvector of the circulant has squared modulus `1/p` at every coordinate, the standard diagonal-resolvent/cofactor identity used already in PC-032 gives

\[
\boxed{
\det(\lambda I-B_{p\mid q})
=\frac1p\frac{d}{d\lambda}
\left[(\lambda-a_{p\mid q})^\alpha
(\lambda-b_{p\mid q})^{p-\alpha}\right].
}
\tag{27}
\]

Therefore

\[
\boxed{
\operatorname{Spec}(B_{p\mid q})
=
\left\{
\begin{array}{ll}
a_{p\mid q}&\text{mult. }\alpha-1,\\
b_{p\mid q}&\text{mult. }p-\alpha-1,\\
r_{p\mid q}&\text{mult. }1,
\end{array}
\right.
}
\tag{28}
\]

with zero multiplicities omitted, where

\[
\boxed{
r_{p\mid q}
=\frac{\alpha b_{p\mid q}+(p-\alpha)a_{p\mid q}}p.
}
\tag{29}
\]

The same formulas, with

\[
\delta=p^{-1}\pmod q,
\qquad
p\delta=1+\varepsilon q,
\tag{30}
\]

give the at-most-three-point spectrum of `B_{q|p}`.

Combining (4) and (28) yields the complete binary mixed-composite spectrum:

\[
\boxed{
\operatorname{Spec}(T_{p,q})
=
\{\lambda+\mu-c_{p,q}:
\lambda\in\operatorname{Spec}(B_{p\mid q}),
\ \mu\in\operatorname{Spec}(B_{q\mid p})\},
}
\tag{31}
\]

with multiplicities equal to the products of the corresponding one-coordinate multiplicities. This proves the uniform bound (6).

## 4. Exact control at `N=15`

Take `p=3`, `q=5`. Then

\[
\Phi_{15}(z)
=z^8-z^7+z^5-z^4+z^3-z+1,
\qquad
h_{15}=7,
\qquad
S=\sqrt{105}.
\tag{32}
\]

For the `p=3` block,

\[
\alpha=5^{-1}\pmod3=2,
\qquad
\beta=3,
\tag{33}
\]

so the full cyclic eigenvalues are `6/S` with multiplicity two and `-9/S` with multiplicity one. Equation (27) gives

\[
\operatorname{Spec}(B_{3\mid5})
=\left\{\frac6S,-\frac4S\right\}.
\tag{34}
\]

For the `q=5` block,

\[
\delta=3^{-1}\pmod5=2,
\qquad
\varepsilon=1,
\tag{35}
\]

and

\[
\operatorname{Spec}(B_{5\mid3})
=
\left\{\frac{10}S,
-\frac5S,-\frac5S,
\frac4S\right\}.
\tag{36}
\]

Since `c_{3,5}=1/S`, (31) gives the eight-dimensional compression exactly as

\[
\boxed{
\operatorname{Spec}(T_{3,5})
=
\left\{
\frac{15}S,
\frac9S,
\frac5S,
-\frac1S,
0,0,
-\frac{10}S,-\frac{10}S
\right\}.
}
\tag{37}
\]

Direct construction of the `8 x 8` exact-order Fourier compression agrees with (37). The control also shows why raw matrix size is misleading: the complete spectrum is generated by two tiny one-coordinate packets.

## 5. Prior-art and novelty audit

The mixed-prime modular-inverse content is classical binary cyclotomic theory, not a new arithmetic discovery.

T. Y. Lam and K. H. Leung, **On the Cyclotomic Polynomial `Phi_{pq}(X)`**, *The American Mathematical Monthly* 103:7 (1996), 562--564, DOI `10.1080/00029890.1996.12004786`, give the explicit coefficient description of binary cyclotomic polynomials in terms of the unique Euclidean/modular-inverse parameters. Their formula makes the `{-1,0,1}` flatness and the two-prime residue geometry explicit. The residue law (21)--(24) is a short Fourier/reduction reformulation of that classical binary structure.

The remaining ingredients are standard and already anchored in the Prime-Circle corpus. The exact-order decomposition and Ramanujan/Pontryagin projectors are the classical harmonic framework used by PC-066 and PC-212--PC-213. The principal-minor derivative identity is the same flat local spectral-measure mechanism already used in PC-032/PC-038. Kronecker-sum spectral addition is elementary finite-dimensional linear algebra.

A directed search did not locate this exact project-specific compression `P_{pq}M_{g_{pq}}P_{pq}`. That absence is not used as evidence of novelty. Equations (4), (21), and (27) show that its structure is assembled completely from CRT separation, classical binary cyclotomic modular inverses, circulant Fourier diagonalization, and a principal cofactor.

The correct classification is therefore a Prime-Circle **boundary theorem**, not a novel RH mechanism.

## 6. RH consequence and surviving boundary

This result sharpens the frontier after PC-213 in two directions.

First, PC-213's strict prime-local factorization does **not** extend verbatim to an individual mixed-composite mask. The binary field `g_{pq}` remembers `q^{-1} mod p` and `p^{-1} mod q`; this is genuine relational arithmetic between the two prime axes. Any analysis that replaces `g_{pq}` by independent prime-power support indicators loses that information.

Second, retaining that information in the most direct exact-order transverse operator is still too weak for RH. The two coordinates never change simultaneously, the operator is a Kronecker sum, and its number of distinct eigenvalues is bounded by nine independently of `p` and `q`. There is no intrinsic spectral parameter `s`, no gamma factor, no functional equation, no critical-line symmetry, and no growing spectral packet whose zeros could plausibly model the nontrivial zeta zeros. Aggregating (31) over many pairs with an externally chosen Mellin/Dirichlet weight would reintroduce the scale by hand.

The binary case also identifies the first level at which a genuinely irreducible mixed-coordinate coefficient incidence is structurally possible. For `N=pq`, every proper divisor is `1`, `p`, or `q`, so every nonzero Fourier difference can move at most one CRT coordinate. For a squarefree ternary conductor `N=pqr`, proper-divisor Fourier sectors such as `pq`, `pr`, and `qr` can in principle move two coordinates simultaneously. Thus

\[
\boxed{
\text{binary mixed-composite masks cannot create irreducible transverse tensor coupling;}
\quad
\omega(N)\ge3
\text{ is the first possible coefficient-mask frontier.}
}
\tag{38}
\]

This is only a necessary structural condition, not evidence that the ternary channel succeeds. Ternary cyclotomic coefficients and their modular-inverse structure have substantial classical prior art and require the same matched-control and novelty scrutiny before any arithmetic interpretation.

The other surviving directions from PC-212--PC-213 remain untouched: vertexwise old/new incidence based on embedded roots rather than coefficient masks, non-Haar matrix fibers, growing nonlinear tensors, source-derived cross-level operators not compressed to one finite conductor, and global uniformization/monodromy.

## 7. Falsification boundary

The theorem can be falsified by any pair of distinct primes for which the exact operator (2), built with the PC-212 normalization, has a matrix entry coupling two CRT basis states that differ in both reduced-residue coordinates, or by a spectrum not representable by (31).

Equation (10) makes the first failure condition equivalent to a nonzero exact-order-`pq` Fourier coefficient of `g_{pq}`, contradicting the defining cyclotomic zero. Equations (21)--(27) make the second condition an exact finite-algebra check. Small controls including `N=10`, `15`, `21`, and `35` agree with the formulas.

The result does **not** claim that all observables of `Phi_{pq}` have bounded complexity, that modular-inverse statistics are uninteresting, or that ternary and higher mixed-composite masks factorize similarly. It closes only the canonical individual-binary-mask/exact-order compression identified above.