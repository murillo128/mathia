# PC-220 — full transverse nonzero spectrum is a signed Ramanujan projection compression

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the nonzero finite-level spectrum left open by PC-218--PC-219: after nullity and inertia have collapsed to cyclotomic coefficient support and sign counts, ask whether the remaining eigenvalue magnitudes/spacings of the canonical full transverse compression

\[
T_n:=P_nM_{g_n}P_n\big|_{E_n}
\]

retain an independent primitive-root phase mechanism.

At a fixed level they do not. With the notation of PC-218, let

\[
\Phi_n(z)=\sum_r a_n(r)z^r,
\qquad
S_n:=\{r:a_n(r)\ne0\},
\qquad
\vartheta(n):=|S_n|,
\]

\[
h_n:=\sum_r a_n(r)^2,
\qquad
A_n=(\zeta_n^{ru})_{r\in S_n,\ u\in U(n)},
\qquad
D_n:=\operatorname{diag}(a_n(r))_{r\in S_n}.
\]

PC-218 proved

\[
T_n=\frac1{\sqrt{nh_n}}A_n^*D_nA_n.
\tag{1}
\]

Define the support-space Gram matrix

\[
C_n:=A_nA_n^*.
\tag{2}
\]

Then every entry is the classical Ramanujan sum

\[
\boxed{(C_n)_{r,s}=c_n(r-s)}
\qquad(r,s\in S_n),
\tag{3}
\]

and the complete nonzero spectrum satisfies

\[
\boxed{
\operatorname{Spec}^{\times}\!\left(\sqrt{nh_n}\,T_n\right)
=
\operatorname{Spec}^{\times}(D_nC_n).
}
\tag{4}
\]

Equivalently, because `C_n` is positive semidefinite, the same nonzero eigenvalues are those of the Hermitian support-space compression

\[
\boxed{C_n^{1/2}D_nC_n^{1/2}.}
\tag{5}
\]

Thus the residual finite-level spectral problem is exactly a signed principal compression of the standard exact-order Fourier/Ramanujan projector by the ordinary coefficient support of `Phi_n`. No additional primitive-root phase channel remains after this reduction.

This does **not** make the nonzero spectrum trivial. The arrangement of the coefficient support inside the Ramanujan kernel can produce genuinely nonintegral real algebraic eigenvalues, and for squarefree levels with growing `omega(n)` it can still encode increasingly high-coordinate incidence. What is classicalized is the finite-level spectral wrapper: all of its characteristic data are explicit signed principal-minor statistics of a standard Ramanujan/gcd projection kernel and the cyclotomic coefficient vector.

## 1. The support Gram matrix is a cropped exact-order Fourier projector

From the definition of `A_n`,

\[
(C_n)_{r,s}
=\sum_{u\in U(n)}\zeta_n^{(r-s)u}
=c_n(r-s),
\]

which proves (3). The full `n x n` circulant matrix

\[
\Pi_n:=\frac1n\bigl(c_n(r-s)\bigr)_{r,s\in\mathbb Z/n\mathbb Z}
\tag{6}
\]

is the orthogonal Fourier projector onto the frequencies of exact order `n`: its Fourier multiplier is `1` on `U(n)` and `0` elsewhere. Hence `C_n/n` is simply the principal compression of this standard projector to the coefficient-index set `S_n`.

For squarefree `n`, the entries are explicitly gcd/divisor data. If

\[
g=\gcd(n,k),
\]

then the classical von Sterneck formula gives

\[
\boxed{
c_n(k)=\mu(n/g)\frac{\varphi(n)}{\varphi(n/g)}.}
\tag{7}
\]

Therefore the support Gram matrix contains no hidden root coordinates: once `S_n` is known, every matrix entry is determined by gcd classes of coefficient-index differences.

PC-218 also gives

\[
\ker A_n^*=\mathbb Ca,
\qquad
a=(a_n(r))_{r\in S_n},
\tag{8}
\]

so

\[
\boxed{\ker C_n=\mathbb Ca,
\qquad
\operatorname{rank}C_n=\vartheta(n)-1.}
\tag{9}
\]

The unique missing support-space direction is therefore the cyclotomic coefficient relation itself.

## 2. The nonzero spectrum transfers exactly to support space

Set

\[
M_n:=A_n^*D_nA_n.
\]

Use the standard `XY/YX` nonzero-spectrum identity with

\[
X=A_n^*D_n,
\qquad
Y=A_n.
\]

Then

\[
XY=M_n,
\qquad
YX=D_nC_n,
\]

so the nonzero eigenvalues, including algebraic multiplicities, agree. Equation (1) proves (4).

Although `D_nC_n` is not generally Hermitian in the standard support-space inner product, its nonzero spectrum is real because it is also the nonzero spectrum of `M_n`. More canonically, apply the same identity to

\[
X=C_n^{1/2}D_n,
\qquad
Y=C_n^{1/2}.
\]

This transfers the nonzero spectrum of `D_nC_n` to the Hermitian matrix `C_n^{1/2}D_nC_n^{1/2}`, proving (5). Thus no arbitrary spectral wrapper is being introduced: the reduction is an exact change of finite state space for the source-derived operator.

There is exactly one zero eigenvalue of `D_nC_n` algebraically. The right null vector is `a`, while the all-ones row is a left null vector because

\[
\mathbf1^TD_n=a^T,
\qquad
a^TC_n=0.
\tag{10}
\]

Their pairing is

\[
\mathbf1^Ta=\Phi_n(1)\ne0.
\tag{11}
\]

Hence a Jordan chain at zero is impossible: if `D_nC_nx=a`, left multiplication by `1^T` would contradict (11). Since (9) already gives geometric nullity one, zero is algebraically simple.

## 3. The reduced characteristic polynomial is integral Ramanujan-minor data

Define

\[
R_n(X):=\frac{\det(XI_{\vartheta(n)}-D_nC_n)}{X}.
\tag{12}
\]

By the simplicity of the zero root, `R_n` is the monic characteristic polynomial of the scaled nonzero spectrum in (4), of degree `vartheta(n)-1`. Because `D_n` and `C_n` are integer matrices,

\[
\boxed{R_n(X)\in\mathbb Z[X].}
\tag{13}
\]

Consequently every scaled nonzero eigenvalue `sqrt(n h_n) lambda` is a real algebraic integer.

More explicitly, let `e_k(n)` be the `k`-th elementary symmetric function of those scaled nonzero eigenvalues. The principal-minor expansion of a characteristic polynomial gives, for `1<=k<=vartheta(n)-1`,

\[
\boxed{
e_k(n)
=
\sum_{\substack{R\subseteq S_n\\|R|=k}}
\left(\prod_{r\in R}a_n(r)\right)
\det\bigl[c_n(r-s)\bigr]_{r,s\in R}.
}
\tag{14}
\]

Every Ramanujan determinant in (14) is nonnegative because it is a principal Gram minor of `C_n=A_nA_n^*`; all signs come from the ordinary cyclotomic coefficients. Thus the *entire* fixed-level characteristic polynomial is a signed weighted sum of classical Ramanujan projection minors.

The product of the nonzero scaled eigenvalues has an especially compact exact form. Since `C_n` has corank one and kernel `Ca`,

\[
\operatorname{adj}(C_n)=\gamma_n aa^T.
\tag{15}
\]

Because the constant coefficient of every cyclotomic polynomial with `n>1` is `a_n(0)=1`,

\[
\gamma_n=
\det\bigl[c_n(r-s)\bigr]_{r,s\in S_n\setminus\{0\}}.
\tag{16}
\]

Summing the order-`vartheta(n)-1` principal minors and using `sum_r a_n(r)=Phi_n(1)` yields

\[
\boxed{
\prod_{\lambda\in\operatorname{Spec}^{\times}(T_n)}
\left(\sqrt{nh_n}\,\lambda\right)
=
\left(\prod_{r\in S_n}a_n(r)\right)
\Phi_n(1)
\det\bigl[c_n(r-s)\bigr]_{r,s\in S_n\setminus\{0\}}.
}
\tag{17}
\]

Equation (17) is the pseudodeterminant continuation of PC-218's nullity theorem: after removing the forced cyclotomic relation, even the product of the surviving eigenvalues is an ordinary coefficient sign product times a principal Ramanujan Gram determinant.

## 4. Exact controls show both the collapse and its limit

For `n=6`, the reduced polynomial of the scaled spectrum is

\[
R_6(X)=(X-3)(X+1),
\]

and the product in (17) is `-3`.

For `n=15`, direct exact arithmetic gives

\[
\boxed{
R_{15}(X)
=(X-15)(X-9)(X-5)(X+1)(X+10)^2.
}
\tag{18}
\]

For `n=30`, however,

\[
\boxed{
R_{30}(X)
=(X-10)(X^2-45)(X^3+2X^2-85X-150).
}
\tag{19}
\]

The quadratic and cubic factors in (19) are important falsification controls against overclaiming. The reduction does **not** say that the spectrum is integer-valued, diagonal in an obvious divisor basis, or determined only by coefficient support size and sign counts. It says that its complete finite-level algebraic content is already the spectrum of a signed compression of the classical Ramanujan projection kernel.

Levels such as `n=105` likewise produce nontrivial real algebraic spectra. Therefore PC-220 does not erase the growing mixed-prime geometry identified by PC-214--PC-215; it relocates that geometry precisely into how the cyclotomic coefficient support sits inside a standard gcd/Ramanujan Gram kernel.

## 5. Prior-art and novelty audit

No novelty is claimed for Ramanujan-sum matrices, their Fourier diagonalization, or cyclotomic coefficient arithmetic. Noboru Ushiroya, **Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums**, *Journal of Integer Sequences* 21 (2018), Article 18.2.6, arXiv:1803.02970, gives finite Fourier spectral analysis for classical Ramanujan-sum matrices. L. Tóth, **Sums of products of Ramanujan sums**, *Annali dell'Università di Ferrara* 58 (2012), 183--197, DOI `10.1007/s11565-011-0143-3`, anchors the classical multiplicative/product algebra of Ramanujan sums. Both are already recorded in `SOURCES.md`.

On the coefficient side, Carlo Sanna, **A survey on coefficients of cyclotomic polynomials**, *Expositiones Mathematicae* 40:3 (2022), 469--494, DOI `10.1016/j.exmath.2022.03.002`, surveys the established arithmetic of cyclotomic coefficients, while Maria Loukaki, **Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle**, *Bulletin of the London Mathematical Society* 57:12 (2025), 3841--3856, DOI `10.1112/blms.70192`, is neighboring modern prior art for structured composite-order Fourier minors. These sources are also already anchored in `SOURCES.md`.

A directed search by the actual mathematical structure -- Ramanujan-sum matrices, exact-order Fourier projectors, cropped/principal Ramanujan matrices, cyclotomic coefficient weighted Fourier compressions, and characteristic polynomials of signed Ramanujan compressions -- did not locate the exact project-specific identities (4), (12), or (14). That absence is **not** a novelty claim. The reduction is assembled from the source-derived PC-218 factorization plus standard `XY/YX` spectral transfer and classical Ramanujan projection theory. Its endpoint is explicitly classical data, so the correct classification is a finite-level boundary theorem and prior-art classicalization, not a new RH mechanism.

## 6. RH consequence and surviving boundary

PC-218 reduced nullity to cyclotomic coefficient sparsity, and PC-219 reduced inertia to coefficient sign counts. PC-220 now classifies the remaining fixed-level characteristic data one step further:

\[
\boxed{
\text{full transverse finite-level spectrum}
\longrightarrow
\text{signed support compression}
\longrightarrow
\text{cyclotomic coefficients + Ramanujan/gcd projector minors}.
}
\tag{20}
\]

Therefore the nonzero eigenvalue magnitudes or spacings of a **single finite** `T_n` cannot be interpreted as a new primitive-root spectral channel merely because they are nontrivial algebraic numbers. They arise from a standard exact-order Fourier projection after restriction to the ordinary cyclotomic coefficient support. There is still no intrinsic complex spectral parameter `s`, gamma factor, `s<->1-s` symmetry, or explicit-formula zero term.

The result must not be overextended into a no-go for the entire collective branch. PC-215's squarefree locality `omega(n)-1` survives, and equations (14)--(19) show exactly where it can live: in the growing pattern of coefficient-index subsets and Ramanujan principal minors. A legitimate continuation must therefore prove something genuinely new about the **cross-level or asymptotic assembly** of these signed projection compressions -- for example a nontrivial norm/pseudospectral law, a non-Haar matrix-fibre limit, or a multi-conductor coupling that is not removable by a common transform or diagonal similarity. It must also survive matched controls with the same divisor-Fourier support but without the prime-specific coefficient relation.

Repeating finite-level determinant, nullity, inertia, packetwise metric, or merely spectralizing the same coefficient mask is exhausted by PC-216--PC-220.