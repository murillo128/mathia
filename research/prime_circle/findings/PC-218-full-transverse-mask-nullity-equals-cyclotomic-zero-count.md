# PC-218 — full transverse mask nullity equals cyclotomic zero-coefficient count

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the genuinely collective full-operator continuation left open by PC-215--PC-217: retain all proper-divisor Fourier packets simultaneously in the canonical transverse compression

\[
T_n:=P_nM_{g_n}P_n\big|_{E_n},
\qquad
E_n=\operatorname{Ran}P_n,
\]

and ask whether its determinant, zero modes, or nullity contain a source-specific collective invariant not visible in the packetwise phase and metric reductions of PC-216--PC-217.

They do not. For every `n>1`, not only for squarefree `n`, the rank of `T_n` is determined exactly by the support size of the coefficient vector of the cyclotomic polynomial. If

\[
\Phi_n(z)=\sum_{r=0}^{\varphi(n)}a_n(r)z^r,
\qquad
\vartheta(n):=\#\{r:a_n(r)\ne0\},
\]

then

\[
\boxed{\operatorname{rank}T_n=\vartheta(n)-1}
\tag{1}
\]

and hence

\[
\boxed{\dim\ker T_n=\varphi(n)-\vartheta(n)+1.}
\tag{2}
\]

The right side of (2) is exactly the number of zero coefficients among the `\varphi(n)+1` coefficient positions of `\Phi_n`. Equivalently,

\[
\boxed{\det T_n\ne0\iff \Phi_n\text{ has no zero coefficients}.}
\tag{3}
\]

Thus the most immediate collective spectral invariant of the full PC-215 operator -- its complete zero-eigenspace multiplicity -- is neither a new interaction statistic nor hidden critical-line data. It is exactly classical cyclotomic coefficient sparsity in operator form.

This does **not** collapse the nonzero spectrum of `T_n`. PC-215's exact growing locality `\ell(T_N)=\omega(N)-1` for squarefree `N` remains intact, and PC-218 does not diagonalize or bound the distinct nonzero eigenvalues of the simultaneous mixed-conductor assembly. What it closes is the determinant/nullity/zero-mode route through that assembly.

## 1. The full compression has an exact signed evaluation-factorization

Retain the coefficient field from PC-212,

\[
g_n(x)=\sqrt{\frac n{h_n}}\,a_n(x\bmod n),
\qquad
h_n:=\sum_r a_n(r)^2.
\tag{4}
\]

Let

\[
U(n)=(\mathbb Z/n\mathbb Z)^\times,
\qquad
S_n:=\{r:0\le r\le\varphi(n),\ a_n(r)\ne0\},
\tag{5}
\]

so `|U(n)|=varphi(n)` and `|S_n|=vartheta(n)`. In the exact-order Fourier basis of `E_n` indexed by `u in U(n)`, PC-212 gives

\[
\widehat g_n\!\left(\frac an\right)
=\frac{\Phi_n(e^{-2\pi ia/n})}{\sqrt{nh_n}}.
\tag{6}
\]

Put `zeta_n=e^{2pi i/n}` and form the rectangular primitive-root evaluation matrix

\[
A_n=(\zeta_n^{ru})_{r\in S_n,\ u\in U(n)}
\in M_{\vartheta(n)\times\varphi(n)}(\mathbb C)
\tag{7}
\]

and the invertible diagonal coefficient matrix

\[
D_n:=\operatorname{diag}(a_n(r))_{r\in S_n}.
\tag{8}
\]

Depending only on the harmless sign convention for the Fourier basis, the matrix of `T_n` is exactly

\[
\boxed{
T_n=\frac1{\sqrt{nh_n}}A_n^*D_nA_n.
}
\tag{9}
\]

Indeed, its `(u,v)` entry is

\[
\frac1{\sqrt{nh_n}}
\sum_{r\in S_n}a_n(r)\zeta_n^{r(v-u)}
=
\frac{\Phi_n(\zeta_n^{v-u})}{\sqrt{nh_n}},
\tag{10}
\]

which is precisely the multiplication-compression coefficient. Equation (9) keeps every proper-divisor packet coupled at once; no conductor-by-conductor diagonalization has been performed.

## 2. The primitive-root evaluation matrix has exactly one left-kernel direction

The key point is elementary but sharp. Let

\[
c=(c_r)_{r\in S_n}\in\ker A_n^*.
\]

Associate to `c` the polynomial

\[
C(z):=\sum_{r\in S_n}c_rz^r.
\tag{11}
\]

For every `u in U(n)`, the equation `A_n^*c=0` says

\[
C(\zeta_n^{-u})=0.
\tag{12}
\]

The numbers `zeta_n^{-u}` are exactly all primitive `n`-th roots. Therefore the cyclotomic polynomial `Phi_n`, their minimal polynomial over `Q` and also their monic product over `C`, divides `C`. But

\[
\deg C\le\varphi(n)=\deg\Phi_n.
\tag{13}
\]

Consequently either `C=0` or

\[
C=\lambda\Phi_n
\tag{14}
\]

for some `lambda in C`. If

\[
a=(a_n(r))_{r\in S_n},
\tag{15}
\]

then

\[
\boxed{\ker A_n^*=\mathbb Ca.}
\tag{16}
\]

Hence

\[
\boxed{\operatorname{rank}A_n=\vartheta(n)-1.}
\tag{17}
\]

This already explains why coefficient support rather than matrix dimension is the natural finite invariant. The primitive roots impose exactly one linear relation on the selected coefficient monomials, namely the cyclotomic relation itself; there is no second independent relation of degree at most `phi(n)`.

## 3. The signed coefficient weights create no additional kernel

Because `D_n` contains both signs and magnitudes of the nonzero cyclotomic coefficients, equation (17) alone does not automatically imply the same rank for `A_n^*D_nA_n`: an indefinite diagonal form can in principle acquire an isotropic radical after compression. Here that possible escape is eliminated exactly by the anchored value `Phi_n(1)`.

Suppose

\[
A_n^*D_nA_nx=0
\tag{18}
\]

and set `y=A_nx`. Then

\[
D_ny\in\ker A_n^*=\mathbb Ca,
\tag{19}
\]

so, because every diagonal entry of `D_n` is nonzero,

\[
y=\lambda D_n^{-1}a=\lambda\mathbf1_{S_n}.
\tag{20}
\]

On the other hand

\[
y\in\operatorname{Ran}A_n=(\ker A_n^*)^\perp=a^\perp.
\tag{21}
\]

Taking the inner product with `a` in (20) gives

\[
0=\langle a,y\rangle
=\lambda\sum_{r\in S_n}a_n(r)
=\lambda\Phi_n(1).
\tag{22}
\]

For every `n>1`, the classical anchored cyclotomic value is nonzero:

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\\
1,&n\text{ is not a prime power}.
\end{cases}
\tag{23}
\]

Therefore `lambda=0`, hence `y=0`, and

\[
\ker(A_n^*D_nA_n)=\ker A_n.
\tag{24}
\]

Combining (17), (24), and the nonzero scalar normalization in (9) proves (1). Since `dim E_n=phi(n)`, equation (2) follows immediately.

There is an equivalent geometric interpretation. The coefficient vector `a` is the unique relation among the primitive-root evaluation rows, while the all-ones support vector would be the only direction capable of converting that relation into a new null vector through the signed diagonal form. The common-anchor value `Phi_n(1) != 0` says exactly that these two directions are not orthogonal, so the compression has no hidden additional radical.

## 4. Exact consequences and controls

Equation (2) identifies the zero-mode multiplicity with a familiar coefficient statistic without asymptotics or genericity assumptions. Several regimes illustrate the distinction from PC-215's interaction locality.

For a prime `p`,

\[
\Phi_p(z)=1+z+\cdots+z^{p-1},
\]

so `vartheta(p)=p=phi(p)+1` and `T_p` is invertible. For a prime power `p^k`,

\[
\Phi_{p^k}(z)
=1+z^{p^{k-1}}+\cdots+z^{(p-1)p^{k-1}},
\tag{25}
\]

so

\[
\boxed{\operatorname{rank}T_{p^k}=p-1}
\tag{26}
\]

independently of `k`, while `dim E_{p^k}=p^{k-1}(p-1)` grows. Thus the large nullspace on prime-power refinements is exactly the obvious coefficient-gap sparsity of (25), not an additional spectral degeneracy.

Mixed squarefree levels can behave very differently while obeying the same theorem. Exact direct constructions give, for example,

\[
\begin{array}{c|c|c|c}
n&\varphi(n)&\vartheta(n)&\operatorname{rank}T_n\\ \hline
15&8&7&6\\
35&24&17&16\\
55&40&17&16\\
105&48&33&32
\end{array}
\tag{27}
\]

and nonsquarefree controls such as `n=9,25,45` give ranks `2,4,6`, respectively, again equal to `vartheta(n)-1`. These checks are illustrative only; the proof above is exact for every `n>1`.

For the squarefree frontier of PC-215, the important point is that **high interaction locality and low rank are logically independent**. A squarefree `T_N` can require `(omega(N)-1)`-body CRT interactions while its kernel dimension is simultaneously forced by coefficient gaps. Therefore locality alone cannot be inferred from rank, and rank deficiency cannot be used as evidence for a new collective arithmetic mode.

## 5. Prior-art and novelty audit

No novelty is claimed for cyclotomic coefficient sparsity itself. Carlo Sanna, **A survey on coefficients of cyclotomic polynomials**, *Expositiones Mathematicae* 40:3 (2022), 469--494, DOI `10.1016/j.exmath.2022.03.002`, surveys the extensive classical and modern literature on cyclotomic coefficients, including gaps and sparsity phenomena. Igor E. Shparlinski and Laurence P. Wijaya, **On nonzero coefficients of binary cyclotomic polynomials**, *Journal of Number Theory* 271 (2025), 246--258, DOI `10.1016/j.jnt.2024.11.008`, explicitly use `vartheta(m)` for the number of nonzero coefficients and study its distribution in the binary family. Thus the statistic appearing on the right side of (1)--(2) is established cyclotomic data, not a new Prime-Circle invariant.

The Fourier-matrix side also has substantial prior art. Chebotarev's classical theorem gives total nonsingularity for Fourier matrices of prime order and underlies finite cyclic uncertainty principles; current composite-order work such as Maria Loukaki, **Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle**, *Bulletin of the London Mathematical Society* 57:12 (2025), 3841--3856, DOI `10.1112/blms.70192`, studies nonvanishing of structured Fourier submatrices for composite orders. Those results are neighboring rank/minor theory, but PC-218 does not require a composite Chebotarev theorem: the exact one-dimensional kernel in (16) follows simply because a degree-at-most-`phi(n)` polynomial vanishing on all primitive roots is a scalar multiple of `Phi_n`.

A directed prior-art search by the mathematical structure -- cyclotomic coefficient support, primitive-root Fourier evaluation matrices, nonzero coefficient counts, Fourier minors, and uncertainty principles -- did not locate the exact project-specific identity `rank(P_nM_{g_n}P_n)=vartheta(n)-1`. That absence is **not** used as a novelty claim. The proof is assembled from elementary minimal-polynomial linear algebra plus the classical nonvanishing of `Phi_n(1)`, and its right-hand side is a classical coefficient statistic. The correct classification is a Prime-Circle exact boundary theorem and prior-art classicalization of a candidate operator invariant.

## 6. RH consequence and surviving boundary

PC-216 showed that each fixed reduced-conductor phase packet is a pure-gauge divisor-cube coboundary. PC-217 showed that its packetwise metric data are finite classical even Dirichlet-`L(1)` data. PC-218 now tests a genuinely collective invariant of the complete simultaneous compression rather than another isolated packet, but its simplest spectral content also collapses:

\[
\boxed{
\text{full mixed-conductor compression}
\longrightarrow
\text{zero modes / determinant}
\longrightarrow
\text{cyclotomic coefficient sparsity}.
}
\tag{28}
\]

Accordingly, a determinant-zero criterion, nullity growth law, or zero-eigenspace count built from this canonical coefficient-mask compression cannot by itself provide a new route to zeta or RH. It contains no spectral parameter `s`, no gamma factor, no `s<->1-s` symmetry, and no explicit-formula zero term; its entire vanishing multiplicity is already encoded in which ordinary coefficients of `Phi_n` are zero.

The result must not be overextended to the nonzero spectrum. PC-215's unbounded tensor locality remains a real source-derived structural feature, and equations (1)--(3) do not classify the positive/negative inertia, nonzero eigenvalue spacings, operator norms, or cross-level behavior of `T_N` as `omega(N)` grows. A legitimate continuation of this branch must therefore study a genuinely collective invariant **after quotienting out the now-classified kernel**, and must compare it against coefficient-support-matched non-arithmetic controls. Repeating determinant, rank, packetwise phase, or packetwise singular-value analysis is exhausted by PC-216--PC-218.