# WP-232 — Bost–Connes Poisson whitening is an indefinite Jacobi normal form; positive escape is range selection

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + KAC-MURDOCK-SZEGO + SOURCE-NONCOMMUTING-WHITENING + ISOMETRY-CLASSIFICATION + JACOBI-NORMAL-FORM + SHIFT-COVARIANT-NO-GO + UNBOUNDED-WHITENING-COLLAPSE + RANGE-SELECTION-ESCAPE + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-231` closes bounded energy-diagonal bimodule processing of the already-formed critical Bost--Connes Weil defect, but deliberately leaves genuinely noncommuting source operations open. The most canonical such operation is already present in the source Gram itself: the one-prime critical conditional Gram

\[
G_r(a,b)=r^{|a-b|},\qquad r=p^{-1/2},
\]

is the half-line Kac--Murdock--Szego/AR(1) covariance kernel, so it has an intrinsic one-step innovation whitening by the unilateral prime-power shift.

That escape can be classified exactly. Let `S e_n=e_{n+1}` on `ell^2(N_0)`, put

\[
A_r:=I-rS,
\qquad
W_{p}:=(\log p)(I-G_r),
\]

and note that `A_r` is boundedly invertible for `0<r<1`. Then

\[
\boxed{
A_r^*G_rA_r=(1-r^2)I
}
\tag{1}
\]

while the **same source-derived noncommuting whitening** sends the exact finite Weil defect to

\[
\boxed{
A_r^*W_pA_r
=2(\log p)r\left(rI-\frac{S+S^*}{2}\right).
}
\tag{2}
\]

The operator in parentheses is the free half-line Jacobi operator shifted by `r`. Since

\[
\operatorname{Spec}\frac{S+S^*}{2}=[-1,1],
\]

its spectrum is

\[
[r-1,r+1],
\]

which crosses zero for every `0<r<1`. Therefore the canonical innovation geometry does not orient the finite Weil ray. It removes the long Poisson tail and exposes a nearest-neighbor **indefinite** normal form.

More strongly, this is not a defect of the particular causal factor `A_r`. Every exact scalar whitener of `G_r` is forced into the same normal form up to an isometric range choice. If a bounded operator `B` satisfies

\[
B^*G_rB=cI,
\qquad c>0,
\tag{3}
\]

then there is an isometry `V` such that

\[
\boxed{
B=\sqrt{\frac{c}{1-r^2}}\,A_rV
}
\tag{4}
\]

and consequently

\[
\boxed{
B^*W_pB
=
\frac{2c(\log p)r}{1-r^2}
V^*\left(rI-\frac{S+S^*}{2}\right)V.
}
\tag{5}
\]

If `B` has dense range, `V` must be unitary, so (5) is unitarily equivalent to the same indefinite Jacobi operator. If the whitener remains covariant with the prime-power shift, `VS=SV`, then `V^*SV=S` and (5) is again exactly the same Jacobi form even when `V` is a proper isometry. Thus **full and source-shift-covariant Poisson whitening cannot supply the missing sign**.

There is an escape, but it is precisely the one the research mandate requires us to audit rather than count as positivity. A proper non-shift-covariant isometry may choose a range contained in the positive spectral subspace of the Jacobi operator, making (5) nonnegative; another range can lie in its negative spectral subspace. Positivity is therefore programmable by the range unless the Bost--Connes/global geometry independently forces that range. In this exact whitening category, the only sign-changing freedom is a noncanonical support/range selection.

This is a substantive narrowing of the live Bost--Connes route. It closes the natural idea that one can use the source's own noncommuting innovation/precision geometry to turn the positive critical Poisson Gram into a positive Weil defect. Any surviving construction must change more than coordinates of the conditional Gram: it needs a source-forced non-shift-covariant correspondence, active finite--archimedean coupling before scalarization, or another global relation whose positivity theorem also creates the Gamma and polar terms.

## 1. Exact source object and critical defect

`WP-216` derives from the Bost--Connes divisibility projections and the actual critical `KMS_1` state the positive Gram

\[
G_1(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}.
\tag{6}
\]

On a fixed prime axis, `m=p^a`, `n=p^b`, this becomes

\[
G_r(a,b)=r^{|a-b|},
\qquad
r=p^{-1/2}.
\tag{7}
\]

The same finding identifies the local finite-Weil Toeplitz ray as

\[
W_p=(\log p)(I-G_r),
\tag{8}
\]

whose nonzero diagonals are exactly

\[
-(\log p)r^{|a-b|}.
\tag{9}
\]

The candidate tested here is therefore source-native. No new kernel, zero data, regularization, or fitted Fourier multiplier is introduced. The only new operation is the canonical one-step innovation factor determined by the same Poisson radius `r`.

## 2. The Poisson Gram has an exact one-step innovation factor

Define

\[
A_r=I-rS.
\tag{10}
\]

Since `||rS||=r<1`, the Neumann series gives

\[
A_r^{-1}=\sum_{j\ge0}r^jS^j,
\tag{11}
\]

so `A_r` is boundedly invertible.

The Toeplitz covariance satisfies

\[
S^*G_rS=G_r.
\tag{12}
\]

Expanding the left-hand side of (1),

\[
A_r^*G_rA_r
=G_r-rS^*G_r-rG_rS+r^2S^*G_rS.
\tag{13}
\]

Entrywise, for `a=b`, the right-hand side is

\[
1-2r^2+r^2=1-r^2,
\tag{14}
\]

while for `a<b`, writing `d=b-a>=1`, it is

\[
(1+r^2)r^d-r\,r^{d-1}-r\,r^{d+1}=0,
\tag{15}
\]

and the case `a>b` follows by symmetry. This proves (1) exactly on the half-line; there is no truncation or asymptotic boundary term.

Equivalently,

\[
\boxed{
G_r^{-1}
=\frac1{1-r^2}
(I-rS)(I-rS^*)
}
\tag{16}
\]

and hence the source Gram has the familiar tridiagonal AR(1) precision operator. The boundary is encoded by `SS^*=I-P_0`; no extra boundary condition is being chosen.

This factorization is useful because it is genuinely noncommuting with the Bost--Connes state Hamiltonian/prime occupation basis. It therefore lies outside the energy-diagonal bimodule class closed in `WP-231`.

## 3. The same whitening exposes an indefinite nearest-neighbor Weil normal form

Using (1) and (8),

\[
\begin{aligned}
A_r^*W_pA_r
&=(\log p)\left(A_r^*A_r-(1-r^2)I\right).
\end{aligned}
\tag{17}
\]

Because `S^*S=I`,

\[
A_r^*A_r
=(1+r^2)I-r(S+S^*).
\tag{18}
\]

Subtracting `(1-r^2)I` gives

\[
A_r^*A_r-(1-r^2)I
=2r^2I-r(S+S^*)
=2rQ_r,
\tag{19}
\]

where

\[
Q_r:=rI-\frac{S+S^*}{2}.
\tag{20}
\]

This proves (2).

The self-adjoint Toeplitz/Jacobi operator `(S+S^*)/2` has spectrum `[-1,1]`; for example, under the standard Hardy-space realization it is the Toeplitz operator with real symbol `cos theta`, whose spectrum is the interval between the minimum and maximum of the symbol. Therefore

\[
\boxed{
\operatorname{Spec}(Q_r)=[r-1,r+1].
}
\tag{21}
\]

Since `0<r<1`, both endpoints have opposite signs. Hence

\[
\boxed{
A_r^*W_pA_r\text{ has strict positive and negative directions.}
}
\tag{22}
\]

The identity gives a useful structural interpretation: the infinite repeated-prime Poisson tail in (9) is the invertible causal spreading of a nearest-neighbor sign defect. Whitening removes that spreading, but the missing positivity does not appear; it becomes the elementary threshold `cos theta=r` in the Jacobi normal form.

## 4. Classification of every exact scalar whitener

Let `B` be bounded and satisfy (3). Since `A_r` is invertible, write

\[
B=A_rT.
\tag{23}
\]

Using (1),

\[
B^*G_rB
=T^*A_r^*G_rA_rT
=(1-r^2)T^*T.
\tag{24}
\]

Comparison with (3) gives

\[
T^*T=\frac{c}{1-r^2}I.
\tag{25}
\]

Thus

\[
T=\sqrt{\frac{c}{1-r^2}}V
\tag{26}
\]

for an isometry `V`, proving (4). Substitution into (2) proves (5).

This has two sharp consequences.

First, if `Ran B` is dense, then `Ran V` is dense because `A_r` is invertible. An isometry has closed range, so `V` is onto and hence unitary. Equation (5) then has exactly the same spectrum, up to the positive scalar factor, as `Q_r`. Every full exact whitening is therefore sign-equivalent to the canonical causal whitening.

Second, if the range choice is required to respect the source prime-power shift,

\[
VS=SV,
\tag{27}
\]

then

\[
V^*SV=V^*VS=S
\tag{28}
\]

and similarly `V^*S^*V=S^*`. Hence

\[
\boxed{V^*Q_rV=Q_r.}
\tag{29}
\]

A proper shift-covariant isometry cannot improve the sign either. This includes the standard Hardy-space isometric multipliers which commute with the unilateral shift.

Thus the source covariance requirement is stronger than generic inertia preservation: it identifies the **complete exact whitening family** and shows that every source-shift-covariant member literally returns the same indefinite normal form.

## 5. Exact whitening has no hidden unbounded-domain escape

One might try to leave the bounded category by using an unbounded exact whitener. The positive lower bound of `G_r` blocks that within the present scalar-whitening condition.

The Poisson symbol satisfies

\[
P_r(\theta)
=\frac{1-r^2}{1-2r\cos\theta+r^2},
\qquad
\min P_r=\frac{1-r}{1+r}>0.
\tag{30}
\]

Hence

\[
G_r\succeq m_r I,
\qquad
m_r=\frac{1-r}{1+r}.
\tag{31}
\]

Suppose a densely defined operator `B` satisfies the exact form identity

\[
\langle Bx,G_rBx\rangle=c\|x\|^2
\tag{32}
\]

on its domain. Then

\[
m_r\|Bx\|^2
\le c\|x\|^2,
\tag{33}
\]

so `B` is bounded on its dense domain and extends uniquely to a bounded operator on the whole Hilbert space. The classification in Section 4 then applies to that extension.

Therefore genuinely domain-sensitive geometry remains open in the research program, but **unboundedness by itself cannot evade this theorem while exact scalar whitening of the Poisson Gram is retained**.

## 6. The only sign-changing whitening freedom is noncovariant range selection

Equation (5) also supplies the aggressive falsification control. Because the positive and negative spectral subspaces of `Q_r` are both infinite-dimensional, there are isometries `V_+` and `V_-` whose ranges lie respectively in those spectral subspaces. Then

\[
V_+^*Q_rV_+\succeq0,
\qquad
V_-^*Q_rV_-\preceq0.
\tag{34}
\]

Thus exact Poisson whitening **can** be made positive if arbitrary proper ranges are allowed. But the same source can be made negative by an equally admissible arbitrary range. The sign is carried by the choice of `Ran V`, not by the Poisson/KMS geometry.

This is the whitening analogue of the sign-programmability boundary in `WP-222`. It is important not to overstate it: (34) does not prove that every non-shift-covariant range is arbitrary, nor that the Bost--Connes system cannot someday force one. It proves that positivity after range restriction has no evidential value unless the range is derived independently of the target sign.

A viable use of (34) would therefore need a source theorem of the form

\[
\text{Bost--Connes/global arithmetic data}
\Longrightarrow
\text{specific noncovariant range }M
\Longrightarrow
Q_r|_M\succeq0,
\tag{35}
\]

with the range fixed before comparison with Weil positivity. The same global object would still have to produce the archimedean Gamma contribution and the polar terms.

## 7. Matched controls and failure of arithmetic specificity

Nothing in Sections 2--6 uses primality except the source identification

\[
r=p^{-1/2},\qquad \ell=\log p.
\]

For any `0<r<1` and any positive scale `ell`, the kernel

\[
G_r(a,b)=r^{|a-b|}
\]

has the same innovation factor, and the defect `ell(I-G_r)` has the same indefinite Jacobi normal form. A generalized-prime system or an arbitrary weighted semigroup ray reproduces the calculation verbatim after assigning its own `r` and `ell`.

This is the correct matched control for the negative result. The whitening mechanism is classical local covariance geometry; it does not distinguish the Riemann arithmetic from a generic geometric-decay ray. The only specifically arithmetic input is that the Bost--Connes critical KMS construction independently fixes `r=p^{-1/2}` and its time evolution fixes `log p`.

Nor does whitening generate any of the missing global terms. Equations (1)--(5) contain no Gamma factor, no real-place scattering phase, no pole at `0` or `1`, and no global test-function pairing. They therefore cannot be reinterpreted as a completed Weil form merely because the starting coefficients were source-forced.

## 8. Prior-art and novelty boundary

The matrix/kernel `r^{|i-j|}` is classical Kac--Murdock--Szego/AR(1) structure. Kac, Murdock, and Szego, *On the eigenvalues of certain Hermitian forms*, J. Rational Mech. Anal. 2 (1953), 767--800, DOI `10.1512/iumj.1953.2.52034`, is the historical anchor. Tridiagonal precision matrices and innovation factorizations for this covariance are standard in Toeplitz and autoregressive theory; see also James H. Justice, *The Szego Recursion Relation and Inverses of Positive Definite Toeplitz Matrices*, SIAM J. Math. Anal. 5 (1974), 503--508, DOI `10.1137/0505052`. No novelty is claimed for AR(1) whitening, Toeplitz inversion, unilateral-shift calculus, or the elementary isometry classification in (23)--(26).

The Bost--Connes source itself is classical: Jean-Benoit Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Math. 1 (1995), 411--457, DOI `10.1007/BF01589495`. `WP-216` is the retained Mathia derivation connecting its critical KMS divisibility geometry to the exact Poisson/GCD Gram used here.

A bounded literature search around Kac--Murdock--Szego/AR(1) whitening, unilateral-shift Toeplitz precision, Bost--Connes KMS geometry, and Weil positivity did not expose a published claim identifying the **critical Bost--Connes Poisson Gram whitener with the Jacobi normal form of its finite-Weil defect**. No new theorem of operator theory is asserted. The durable Mathia delta is the exact source-to-target dictionary and the resulting route closure: once the conditional KMS Gram is required to be whitened exactly, all full or shift-covariant whiteners retain the same wrong sign, while the remaining positive escape is explicitly a noncovariant range-selection problem.

This is not a proof of RH, not a positive Weil form, and not a new representation of zero data.

## Consequence for the research frontier

The recent Bost--Connes sequence has now eliminated several post-formation repairs for the exact source-forced defect: invariant restrictions (`WP-219`--`WP-221`), arbitrary quotients without source selection (`WP-222`), energy-diagonal selection and positive channels (`WP-223`--`WP-225`), self-pairing and ordinary matched positive completion (`WP-226`--`WP-229`), faithful metric reweighting (`WP-230`), and energy-diagonal bimodule processing (`WP-231`). The present result closes the most canonical **noncommuting source-whitening** variant left by that chain.

The remaining route must introduce a relation that is not merely an exact re-coordinate/whitening of the one-prime Poisson Gram. In particular, it must derive before target inspection at least one of:

- a non-shift-covariant range/correspondence selected by independent arithmetic or finite--archimedean geometry;
- an active finite--archimedean incidence that changes the operator before the local defect is scalarized;
- a genuinely global nontracial/cohomological object whose positivity theorem is not congruence or support selection of `W_p`.

Any survivor must still pass the canonical mandate: the same construction must account for finite-prime coefficients, Gamma and polar terms with audited normalization, and a global nonnegativity theorem independent of RH and inserted zero data.