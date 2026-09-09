# PF-254 — normalized noncommuting Robin injection splits into square-root amplitude and polar transport

**Status:** `EXACT-DERIVED + NONCOMMUTATIVE-ROBIN-FACTORIZATION + ROUTE-NARROWING`. [[research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing|PF-243]] reduces the live high-high shear problem to a separated Robin-Poisson estimate. [[research/prime_flute/findings/PF-244-one-sided-seam-domination-does-not-imply-separated-poisson-smoothing|PF-244]] shows that a noncommuting seam square root can convert high transverse input into cheap low modes before propagation, while [[research/prime_flute/findings/PF-246-commuting-seam-normalizers-force-all-order-separated-robin-poisson-smoothing|PF-246]] proves all-order smoothing when the seam normalizer commutes with the corridor transverse operator. [[research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window|PF-253]] then proves that a literal square root of the actual parity-Jacobi edge has ample separated margin, namely every weight exponent below `3`.

There is an exact noncommutative algebraic reduction between these results. Relative to a positive transverse operator `K`, the normalized Robin source factor `(K+Q)^{-1}Q^{1/2}` is not an arbitrary seam square root: after the unavoidable `K^{-1/2}` energy factor it is

\[
K^{-1/2}\,h(\mathcal R)\,U,
\qquad
h(\lambda)=\frac{\sqrt\lambda}{1+\lambda},
\qquad
\mathcal R=K^{-1/2}QK^{-1/2},
\]

where `U` is the polar partial isometry of `K^{-1/2}Q^{1/2}`. Thus the **positive relative amplitude has a universal square-root edge**, while all unsmoothed input-orientation information is isolated in `U`. This reconciles PF-244 with PF-246 and sharpens the live Prime-Flute theorem: the remaining question is no longer whether Robin normalization itself has a favorable positive edge. It is whether the actual complete-lift relative seam can be related to PF-247's Jacobi operator and whether its polar transport is sufficiently local in the `K_a` spectral basis.

The statements below are exact for bounded `K>0` with bounded inverse and bounded `Q>=0`; equivalently they hold on every finite spectral/Galerkin regularization of the PF-243 boundary problem. No unproved passage to the full unbounded complete-lift operators is used here to claim the desired smoothing estimate.

## 1. Exact one-boundary factorization

Let `H` be a Hilbert space, let `K` be bounded, self-adjoint, and satisfy

\[
K\ge k_0 I>0,
\]

and let `Q>=0` be bounded and self-adjoint. Define the dimensionless relative seam

\[
\mathcal R:=K^{-1/2}QK^{-1/2}\ge0
\tag{1}
\]

and

\[
X:=K^{-1/2}Q^{1/2}.
\tag{2}
\]

Then

\[
XX^*=\mathcal R.
\tag{3}
\]

Hence the left polar decomposition may be written

\[
X=\mathcal R^{1/2}U,
\tag{4}
\]

where `U` is a partial isometry and is unitary when `Q` is strictly positive on the finite regularization.

Now factor

\[
K+Q
=K^{1/2}(I+\mathcal R)K^{1/2}.
\tag{5}
\]

For the normalized Robin source-to-boundary factor

\[
A_Q:=(K+Q)^{-1}Q^{1/2},
\tag{6}
\]

(2)--(5) give the exact identity

\[
\boxed{
A_Q
=K^{-1/2}h(\mathcal R)U,
\qquad
h(\lambda):=\frac{\sqrt\lambda}{1+\lambda}.
}
\tag{7}
\]

The scalar function is bounded by

\[
0\le h(\lambda)\le\frac12,
\tag{8}
\]

and has the two asymptotic regimes

\[
h(\lambda)
=\lambda^{1/2}-\lambda^{3/2}+O(\lambda^{5/2})
\quad(\lambda\downarrow0),
\tag{9}
\]

\[
h(\lambda)=\lambda^{-1/2}+O(\lambda^{-3/2})
\quad(\lambda\to\infty).
\tag{10}
\]

So the first non-smooth positive edge is exactly a square root. This conclusion requires no commutation between `K` and `Q`.

Two related normalized objects separate the positive amplitude from orientation even more clearly. First,

\[
A_QA_Q^*
=K^{-1/2}h(\mathcal R)^2K^{-1/2},
\tag{11}
\]

because `h(\mathcal R)` vanishes on `ker \mathcal R`, where the polar support projection is absent. Thus the output-side Gram operator is independent of the polar orientation. Second, the positive normalized boundary response

\[
D_Q:=Q^{1/2}(K+Q)^{-1}Q^{1/2}
\tag{12}
\]

satisfies

\[
\boxed{
D_Q=U^*g(\mathcal R)U,
\qquad
g(\lambda):=\frac{\lambda}{1+\lambda}.
}
\tag{13}
\]

This explains why positive boundary-response or singular-value control can survive without controlling the input spectral conversion that PF-244 exposes.

## 2. The Robin reflection is a Cayley transform in the same relative variable

Define

\[
C_Q:=(K+Q)^{-1}(K-Q).
\tag{14}
\]

Using (5),

\[
\boxed{
C_Q
=K^{-1/2}c(\mathcal R)K^{1/2},
\qquad
c(\lambda):=\frac{1-\lambda}{1+\lambda}.
}
\tag{15}
\]

Since `|c(\lambda)|<=1` on `[0,\infty)`, `c(\mathcal R)` is a self-adjoint contraction. Thus `C_Q` is contractive in the `K`-energy normalization even though it need not be a contraction in the original Hilbert norm.

Equations (7) and (15) are the noncommutative replacements for the two scalar factors in PF-246,

\[
\frac{\sqrt q}{k+q},
\qquad
\frac{k-q}{k+q}.
\]

They also show exactly where commutativity was used there: not to obtain the favorable scalar amplitudes, but to make the polar transport trivial and to diagonalize the relative seam in the same spectral basis as propagation.

## 3. Exact two-boundary product-corridor formula

The same reduction sums the two-boundary reflection series without assuming that either seam commutes with `K`. Consider the product equation

\[
-u_{XX}+K^2u=0,
\qquad 0<X<1,
\tag{16}
\]

with nonnegative boundary normalizers `Q_0,Q_1`, homogeneous Robin data at `X=0`, and normalized forcing `Q_1^{1/2}f` at `X=1`, exactly as in PF-246. Put `y=1-X` and write

\[
u(y)=e^{-Ky}a+e^{Ky}b.
\tag{17}
\]

For

\[
A_1=(K+Q_1)^{-1}Q_1^{1/2},
\qquad
C_i=(K+Q_i)^{-1}(K-Q_i),
\tag{18}
\]

the left homogeneous condition and right source condition give, in the stated order,

\[
b=e^{-K}C_0e^{-K}a,
\tag{19}
\]

\[
a=A_1f+C_1b.
\tag{20}
\]

Therefore

\[
\boxed{
a
=\bigl(I-C_1e^{-K}C_0e^{-K}\bigr)^{-1}A_1f.
}
\tag{21}
\]

Let

\[
\mathcal R_i=K^{-1/2}Q_iK^{-1/2}
\]

and let `U_1` be the polar partial isometry from (4) for `Q_1`. Conjugating (21) by `K^{1/2}` gives the cleaner energy-normalized identity

\[
\boxed{
K^{1/2}a
=\Bigl(I-c(\mathcal R_1)e^{-K}c(\mathcal R_0)e^{-K}\Bigr)^{-1}
 h(\mathcal R_1)U_1f.
}
\tag{22}
\]

Because both `c(\mathcal R_i)` are contractions and `K>=k_0I`,

\[
\left\|c(\mathcal R_1)e^{-K}c(\mathcal R_0)e^{-K}\right\|
\le e^{-2k_0}<1,
\tag{23}
\]

so

\[
\left\|\Bigl(I-c(\mathcal R_1)e^{-K}c(\mathcal R_0)e^{-K}\Bigr)^{-1}\right\|
\le\frac1{1-e^{-2k_0}}.
\tag{24}
\]

Every reflection-cycle spectral conversion is therefore preceded by positive longitudinal propagation. The one factor exposed to the raw right-boundary input **before any `e^{-K}` smoothing** is

\[
h(\mathcal R_1)U_1.
\tag{25}
\]

That is exactly the location at which PF-244's high-to-low conversion can defeat a separated estimate.

## 4. Checks against PF-244 and PF-246

### Commuting calibration

If `Q=q(K)`, then

\[
\mathcal R=\frac{q(K)}K,
\qquad U=I
\]

on the positive support, and (7) becomes

\[
K^{-1/2}h(\mathcal R)
=\frac{\sqrt{q(K)}}{K+q(K)}.
\tag{26}
\]

Likewise (15) becomes the scalar reflection coefficient `(K-q(K))/(K+q(K))`. Thus (22) reduces exactly to PF-246's modewise formula. The noncommutative factorization is therefore a genuine extension of that calibration rather than a different normalization.

### PF-244 remains a live obstruction

PF-244 is not contradicted. Equation (11) removes `U` only from an output-side Gram operator. PF-243 needs control with high spectral weight on the **input** side. In (7) and (25), `U` acts on that input before longitudinal propagation. An uncontrolled polar partial isometry can therefore rotate high-`K` input into low-`K` channels, after which spatial separation is cheap and does not restore the lost spectral weight. This is precisely the mechanism of PF-244, now localized to one canonical factor.

The result also shows why one-sided form domination of `Q` is insufficient: such domination controls positive size but does not control the polar orientation of `K^{-1/2}Q^{1/2}`.

## 5. Prime-Flute consequence and the Jacobi square-root window

The accepted critical-Jacobi clue asked first whether the actual seam-normalized Robin factor has a favorable positive fractional edge. Equation (7) answers that part at the relative-seam level: **Robin normalization forces the positive amplitude to be**

\[
h(\mathcal R)=\mathcal R^{1/2}(I+\mathcal R)^{-1},
\tag{27}
\]

so its leading edge is exactly `\mathcal R^{1/2}`.

This makes PF-253's `\sigma=1/2` result structurally relevant. If the actual fixed-axis relative seam `\mathcal R_w` can be reduced to, or compared with, PF-247's parity Jacobi operator `J_\varepsilon` in a way that preserves the load-bearing off-diagonal kernel, then the positive amplitude has the same fractional exponent for which PF-253 proves the sharp separated window

\[
R<3,
\]

comfortably above PF-243's required `R>1`.

What is **not** established is equally important. The complete-lift seam in PF-238 is built from noncommuting congruences and functional calculus involving the fixed-axis operators; this finding does not prove

\[
\mathcal R_w=J_\varepsilon
\]

or any equivalent identity. Nor does it show that the polar factor `U_w` is local, pseudolocal, banded, order zero, or harmless for high-to-low mode conversion. Therefore PF-243 remains open.

The live theorem is now two-part and explicit:

1. derive the actual fixed-axis relative seam `\mathcal R_w=K_a^{-1/2}Q_w^{\rm act}K_a^{-1/2}` in the correct form realization and compare its low edge with PF-247's `J_\varepsilon`;
2. control the high-to-low blocks of the corresponding polar transport `U_w` strongly enough that some exponent `R>1` survives in the separated Robin-Poisson map.

A counterexample to either part would close the current Jacobi-transfer route without questioning PF-253 itself.

## 6. Prior-art and novelty audit

General Dirichlet-to-Neumann and Robin-to-Robin boundary maps, their linear-fractional structure, and boundary-triplet/M-function formulations are classical. A directly relevant reference is S. Clark, F. Gesztesy, and M. Mitrea, *Boundary Data Maps for Schrödinger Operators on a Compact Interval*, Mathematical Modelling of Natural Phenomena **5** (2010), 73--121, DOI `10.1051/mmnp/20105404`, which systematically studies Robin-to-Robin maps and their resolvent representations. A broader boundary-triplet reference is M. Brown, M. Marletta, S. Naboko, and I. Wood, *Boundary triplets and M-functions for non-selfadjoint operators, with applications to elliptic PDEs and block operator matrices*, Journal of the London Mathematical Society **77** (2008), 700--718, DOI `10.1112/jlms/jdn006`.

The polar decomposition used in (4), the positive functional calculus in (7), and the Cayley transform in (15) are standard operator theory. **No new general theorem about Robin maps or polar decomposition is claimed.** The project-specific contribution is the exact organization of the PF-243/PF-244/PF-246 obstruction: it proves that the normalized positive injection has a square-root relative edge and isolates the remaining unsmoothed spectral-conversion problem in a polar transport factor, thereby giving a precise bridge target for PF-253.

A structural search did not locate this exact Prime-Flute/Jacobi application in the boundary-map literature. That absence is not used as a novelty claim; the mathematical value here is the exact reduction of the current local research gate.

## 7. Boundary conditions and failure modes

- The displayed operator identities are asserted exactly only in the bounded positive setting, including finite spectral/Galerkin regularizations. The complete PF seam and corridor operators are unbounded form objects, so a rigorous passage to the full realization remains part of the live theorem.
- A square-root positive edge in `\mathcal R` is not the same statement as a square-root functional calculus of PF-247's `J_\varepsilon`. The relation between those operators must be derived, not inferred by analogy.
- `A_QA_Q^*` being polar-free does not imply the input-weighted estimate needed by PF-243. The location of `U` relative to the high-frequency projector is decisive.
- The contraction bound (24) controls the reflection series in the `K`-energy normalization; it does not by itself prove transverse smoothing.
- PF-245's lack of a uniform wider analytic strip for the bare seam square root is neither used nor contradicted. The favorable factor here arises from real-axis Robin normalization.
- No consequence for global flute scattering, resonances, determinants, zeta zeros, or RH follows from this local factorization.

## Decisive next test

On the actual fixed-axis complete-lift seam, derive the regularized pair `(\mathcal R_w,U_w)` from

\[
K_a^{-1/2}(Q_w^{\rm act})^{1/2}=\mathcal R_w^{1/2}U_w
\]

without replacing `Q_w^{\rm act}` by the commuting matched seam. Then prove either:

\[
E_d\,h(\mathcal R_w)U_wK_a^RP_Z
\]

has the separated bound required by PF-243 for some uniform `R>1` (with PF-253 providing the candidate `R<3` positive-amplitude budget after a valid `\mathcal R_w`--`J_\varepsilon` comparison), or construct an actual-seam sequence showing that `U_w` or the relative-seam comparison destroys every such exponent.

That test is strictly narrower than the former request to understand an arbitrary noncommuting seam square root: the positive amplitude and all reflection coefficients are now explicit bounded functions of the relative seam.