# PC-219 — full transverse-mask inertia equals cyclotomic coefficient sign counts

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the inertia/signature continuation explicitly left open by PC-218: retain the full canonical transverse compression

\[
T_n:=P_nM_{g_n}P_n\big|_{E_n}
\]

and ask whether its positive/negative spectral counts contain collective information not already present in ordinary cyclotomic coefficients.

They do not. Write

\[
\Phi_n(z)=\sum_{r=0}^{\varphi(n)}a_n(r)z^r
\]

and define

\[
p_n:=\#\{r:a_n(r)>0\},\qquad
m_n:=\#\{r:a_n(r)<0\},\qquad
z_n:=\#\{r:a_n(r)=0\}.
\]

For every `n>1`, with inertia ordered as `(positive, negative, zero)`, the canonical transverse operator satisfies

\[
\boxed{\operatorname{In}(T_n)=(p_n-1,\ m_n,\ z_n).}
\tag{1}
\]

Since `z_n=varphi(n)+1-(p_n+m_n)`, the zero component recovers PC-218 exactly. Equation (1) now classifies the two remaining inertia components as well. In particular,

\[
\boxed{\operatorname{sig}(T_n)=p_n-m_n-1.}
\tag{2}
\]

Thus inertia and signature add no new spectral statistic beyond the sign pattern of the coefficients of `Phi_n`.

This does **not** determine the nonzero eigenvalue magnitudes, spacings, eigenvectors, operator norm, or cross-level behavior of `T_n`. It closes only the inertia/signature branch.

## 1. PC-218 reduces the operator to a signed evaluation form

Use the notation of PC-218. Let

\[
S_n:=\{r:a_n(r)\ne0\},\qquad
\vartheta(n):=|S_n|=p_n+m_n,
\]

let `A_n` be the primitive-root evaluation matrix

\[
A_n=(\zeta_n^{ru})_{r\in S_n,\ u\in U(n)},
\]

and put

\[
D_n:=\operatorname{diag}(a_n(r))_{r\in S_n},\qquad
a:=(a_n(r))_{r\in S_n}.
\]

PC-218 proves the exact factorization

\[
T_n=\frac1{\sqrt{nh_n}}A_n^*D_nA_n,
\tag{3}
\]

with positive scalar `1/sqrt(n h_n)`, together with

\[
\ker A_n^*=\mathbb Ca,
\qquad
\operatorname{Ran}A_n=a^\perp,
\qquad
\operatorname{rank}A_n=\vartheta(n)-1,
\tag{4}
\]

and

\[
\ker(A_n^*D_nA_n)=\ker A_n.
\tag{5}
\]

Hence the only missing information for inertia is the signature of the diagonal Hermitian form `D_n` after restriction to `Ran A_n`.

## 2. The range is a codimension-one `D_n`-orthogonal complement

Let `1` denote the all-ones vector in `C^{S_n}`. By construction,

\[
D_n\mathbf1=a.
\tag{6}
\]

For every `y in Ran A_n=a^perp`, therefore,

\[
\langle\mathbf1,D_ny\rangle
=\langle D_n\mathbf1,y\rangle
=\langle a,y\rangle
=0.
\tag{7}
\]

So `Ran A_n` is `D_n`-orthogonal to the constant direction. That direction is strictly positive because

\[
\langle\mathbf1,D_n\mathbf1\rangle
=\sum_{r\in S_n}a_n(r)
=\Phi_n(1)>0
\qquad(n>1).
\tag{8}
\]

The classical anchored value is `p` when `n=p^k` and `1` otherwise, so only positivity is needed here. Since `Ran A_n` has codimension one and the constant vector is not in it, equations (7)--(8) give the exact orthogonal decomposition for the indefinite Hermitian form defined by `D_n`:

\[
\boxed{
\mathbb C^{S_n}=\mathbb C\mathbf1\ \oplus_{D_n}\ \operatorname{Ran}A_n.
}
\tag{9}
\]

The diagonal matrix `D_n` is nonsingular on `S_n` and has inertia `(p_n,m_n,0)`. The first summand in (9) contributes one positive square. Additivity of inertia under an orthogonal direct sum therefore gives

\[
\boxed{
\operatorname{In}\!\left(D_n\big|_{\operatorname{Ran}A_n}\right)
=(p_n-1,m_n,0).
}
\tag{10}
\]

This is the load-bearing step: the common anchored value `Phi_n(1)>0` determines **which** sign is removed by the unique cyclotomic relation.

## 3. Pullback by `A_n` preserves the nonzero inertia

Let

\[
H_n:=(\ker A_n)^\perp.
\]

By (4), the restriction

\[
A_n|_{H_n}:H_n\longrightarrow\operatorname{Ran}A_n
\]

is an isomorphism. On `H_n`, the quadratic form of (3) is the positive scalar multiple of the pullback of `D_n|_{Ran A_n}`:

\[
\langle x,T_nx\rangle
=\frac1{\sqrt{nh_n}}
\langle A_nx,D_nA_nx\rangle.
\tag{11}
\]

Sylvester's law of inertia for Hermitian forms therefore identifies the positive and negative indices of `T_n|_{H_n}` with those in (10). On the complementary space `ker A_n`, equation (5) says that `T_n` vanishes identically. PC-218 gives

\[
\dim\ker A_n
=\varphi(n)-\vartheta(n)+1
=z_n.
\tag{12}
\]

Combining (10)--(12) proves (1).

An equivalent formulation is that the full signed compression is congruent, after separating its kernel, to the coefficient diagonal form with exactly the one positive constant direction removed. No spectral diagonalization of `T_n` is required.

## 4. Exact controls

For `n=6`,

\[
\Phi_6(x)=x^2-x+1,
\]

so `(p_6,m_6,z_6)=(2,1,0)` and (1) gives

\[
\operatorname{In}(T_6)=(1,1,0).
\]

For `n=15`,

\[
\Phi_{15}(x)=x^8-x^7+x^5-x^4+x^3-x+1,
\]

so `(p_{15},m_{15},z_{15})=(4,3,2)` and

\[
\operatorname{In}(T_{15})=(3,3,2).
\]

Prime powers provide a different control. Their nonzero cyclotomic coefficients are all positive, hence `m_n=0`; the theorem makes `T_n` positive semidefinite, with exactly the coefficient-gap nullity already classified by PC-218. These examples are checks only; the proof above is exact for every `n>1`.

## 5. Prior-art and novelty audit

No novelty is claimed for Sylvester's law of inertia or for the sign distribution of cyclotomic coefficients. Sylvester congruence is standard finite-dimensional Hermitian linear algebra. Carlo Sanna, **A survey on coefficients of cyclotomic polynomials**, *Expositiones Mathematicae* 40:3 (2022), 469--494, DOI `10.1016/j.exmath.2022.03.002`, already anchors in `SOURCES.md` the extensive classical and modern theory of cyclotomic coefficients. Positive, negative, zero, support, height, and coefficient-pattern questions therefore belong to established cyclotomic arithmetic rather than constituting new Prime-Circle spectral data.

A directed search by the mathematical structure -- inertia of `A^*DA`, Hermitian restriction to a codimension-one hyperplane, cyclotomic coefficient signs, and positive/negative coefficient counts -- did not locate the exact project-specific identity (1). That absence is **not** used as a novelty claim. The theorem is an elementary consequence of the PC-218 evaluation geometry plus classical inertia theory, and its right-hand side is ordinary cyclotomic coefficient data. The correct classification is an exact Prime-Circle boundary theorem and a classicalization of the candidate inertia invariant.

## 6. RH consequence and surviving boundary

PC-218 showed that the full transverse-mask nullity is exactly coefficient sparsity. PC-219 now shows that the entire inertia is equally rigid:

\[
\boxed{
\text{full transverse compression}
\longrightarrow
\text{positive/negative/zero counts}
\longrightarrow
\text{cyclotomic coefficient sign counts}.
}
\tag{13}
\]

Consequently, an RH mechanism based only on inertia, signature, Morse index, positivity/negativity count, or their finite-level growth for this canonical full-mask operator cannot obtain information not already present in the coefficient sign statistics of `Phi_n`. Any successful use of those counts would require a separate arithmetic theorem about cyclotomic coefficient signs; the spectral wrapping itself adds no independent bridge to zeta, its functional equation, or the critical line.

The result must not be overextended. The nonzero spectrum remains unclassified, as do eigenvalue magnitudes and spacings, coefficient-conditioned eigenvectors, genuinely cross-level couplings, and any nonlinear invariant sensitive to more than inertia. Those are the only legitimate continuations of this full-mask branch after PC-218--PC-219.