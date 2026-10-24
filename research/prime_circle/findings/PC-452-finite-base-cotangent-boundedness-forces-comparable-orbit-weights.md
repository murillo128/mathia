# PC-452 — Finite-base cotangent boundedness forces comparable orbit weights

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION. For every fixed finite base of distinct circle points, an equivalent measure makes either unchanged complete cotangent-tower action bounded if and only if its fiber densities are uniformly comparable and one, hence every, fiber density is orbit `A_2`. In this entire class the spectra equal the Haar spectra. Individual orbit `A_2` conditions without cross-fiber comparability are insufficient. This classifies the finite-base equivalent-measure boundary left by PC-451; it supplies no prime discriminator or RH implication.

## 1. Object and theorem

Let
\[
Z=\{e^{2\pi i\theta_a}:1\le a\le r\},\qquad
0\le\theta_a<1,
\]
with distinct angles and fixed finite `r>=1`. The Prime-Circle case is `Z=P_d^*`, with `theta_a=u_a/d` for an enumeration `u_1,...,u_r` of the reduced residues. Its complete level-`m` preimages are
\[
y_{a,t}^{(m)}=e^{2\pi i(\theta_a+t)/m},\qquad t\in\mathbb Z/m\mathbb Z.
\]
The compatible inverse limit is `X={1,...,r} times Zhat`, with base-uniform times fiber-Haar probability `mu_X`. Write `mu` for Haar probability on `Zhat`.

An equivalent probability `nu` has densities
\[
d\nu(a,x)=\frac1r w_a(x)d\mu(x),\qquad
0<w_a<\infty\ \text{a.e.},\qquad
\frac1r\sum_a\int w_a\,d\mu=1.
\tag{1}
\]
No uniform upper or lower bound on the densities is assumed. Retain the pointwise cylinder matrices
\[
(T_m)_{(a,t),(c,s)}=
\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(\theta_a-\theta_c+t-s)}m,
 &(a,t)\ne(c,s),\\
0,&(a,t)=(c,s),
\end{cases}
\qquad T_m^+=T_m+J_{rm}/m.
\tag{2}
\]
These are the compatible normalized actions of PC-053 and PC-443. In particular, changing (1) does not insert quadrature weights into (2).

For `Sx=x+1`, put
\[
[w]_{A_2(S)}=
\operatorname*{ess\,sup}_x\sup_{n\ge1}
\left(\frac1n\sum_{j=0}^{n-1}w(x+j)\right)
\left(\frac1n\sum_{j=0}^{n-1}w(x+j)^{-1}\right).
\tag{3}
\]
Multiplication of a weight by a positive constant does not change (3).

**Theorem.** The following are equivalent:

1. The raw cylinder action `T` extends boundedly to `L^2(nu)`.
2. The raw augmented action `T^+` extends boundedly to `L^2(nu)`.
3. For one reference fiber, say `a=1`,
   \[
   [w_1]_{A_2(S)}<\infty,\qquad
   C^{-1}w_1\le w_a\le Cw_1\quad\text{a.e. for every }a
   \tag{4}
   \]
   with a finite constant `C`.

Define the finite Hermitian base matrices
\[
H_{ac}=i\cot\pi(\theta_a-\theta_c)\quad(a\ne c),\qquad H_{aa}=0,
\qquad A=H+J_r,
\]
and let `lambda_1,...,lambda_r` be the eigenvalues of `A`, with multiplicity. Whenever (4) holds,
\[
\boxed{\displaystyle
\sigma(T^+)=\mathcal B_Z:=\bigcup_{\alpha=1}^r[\lambda_\alpha-2,\lambda_\alpha],
\qquad
\sigma(T)=\mathcal B_Z\cup\sigma(H).}
\tag{5}
\]
These are spectral **sets** of possibly nonnormal operators. No self-adjoint spectral type, Haar orthogonality, or Riesz-basis conclusion follows.

## 2. Necessity: one fiber and then two fibers

The coordinate projection onto a single base fiber is an orthogonal projection in `L^2(nu)`. Compressing either bounded action to that fiber gives exactly the singleton cotangent action, respectively its augmented version. PC-451 therefore gives
\[
[w_a]_{A_2(S)}<\infty\quad\text{for every }a.
\tag{6}
\]
Apply that finding to `w_a/integral w_a` if necessary; scaling does not affect boundedness or (3). In particular every `w_a^{-1}` is integrable. This step uses the nonmaximal necessity theorem of PC-451, not an inference from boundedness of an unrelated maximal operator.

The off-diagonal blocks impose more. Let
\[
w_{a,m}(t)=m\int_{x\equiv t\pmod m}w_a(x)\,d\mu(x).
\]
The squared cylinder norm is `(rm)^{-1} sum_{a,t}|f(a,t)|^2 w_{a,m}(t)`. Suppose either full action has norm `L`. Test it on the indicator of the single input cylinder `(c,t)`, and retain only the output cylinder `(a,t)`, for `a!=c`. With `delta=theta_a-theta_c !=0`, the unaugmented entry is
\[
k_{ac,m}=\frac{i}{m}\cot\frac{\pi\delta}{m}
\longrightarrow\frac{i}{\pi\delta}.
\tag{7}
\]
The augmented entry is `k_{ac,m}+1/m`, whose absolute value is at least `|k_{ac,m}|`, since the two terms are respectively imaginary and real. Thus, for either action,
\[
|k_{ac,m}|^2 w_{a,m}(t)\le L^2w_{c,m}(t).
\tag{8}
\]
Take the cofinal generating partitions `m=k!`. Conditional-expectation convergence gives `w_{a,k!}(x)->w_a(x)` simultaneously for the finitely many fibers, almost everywhere. Taking (7)--(8) to the limit yields
\[
\frac{w_a(x)}{w_c(x)}\le \pi^2(\theta_a-\theta_c)^2L^2.
\tag{9}
\]
The reverse test yields the reciprocal bound. Every pair of densities is therefore uniformly comparable. Possible vanishing of the coarse cotangent entry for antipodal points at `m=1` is irrelevant: the same-lift refined entry has the nonzero limit (7).

This is the load-bearing finite-base obstruction: the full action cannot assign independently singular scales to distinct fibers, even when each separate diagonal action is bounded. The argument needs neither a weighted Fourier basis nor prior boundedness of cross-fiber identifications.

## 3. A bounded multiplier lemma on the common weighted fiber

For sufficiency set `w=w_1`. By (4), the identity on functions is a bounded isomorphism between `L^2(nu)` and
\[
\mathcal K=\mathbb C^r\otimes H_w,\qquad H_w=L^2(\widehat{\mathbb Z},w\mu),
\tag{10}
\]
with the same cylinder action. This changes only to an equivalent norm, not to the Haar norm.

For `q=j/m in [0,1)`, write `chi_q(x)=exp(2 pi i j(x mod m)/m)`. Let `B_w^+` be the singleton augmented operator on `H_w`. PC-451 makes it bounded, and PC-450 proves
\[
B_w^+\chi_q=(1-2q)\chi_q,\qquad
\sigma(B_w^+)=[-1,1],\qquad q\in\mathbb Q\cap[0,1).
\tag{11}
\]
For completeness, the part of its multiplier calculus needed here follows directly from character modulation. Multiplication `Q_b f=chi_b f` is unitary in `H_w`. For rational `0<b<1`,
\[
E_b=bI+\tfrac12(B_w^+-Q_bB_w^+Q_b^{-1}),
\qquad E_b\chi_q=\mathbf1_{[0,b)}(q)\chi_q,
\qquad \|E_b\|\le K:=1+\|B_w^+\|.
\tag{12}
\]
Set `E_0=0,E_1=I`. For any `g in C^1([0,1])` and rational partition `0=b_0<...<b_N=1`, the operators
\[
g(1)I+\sum_{j=1}^N\bigl(g(b_{j-1})-g(b_j)\bigr)E_{b_j}
\tag{13}
\]
have norm at most `|g(1)|+K integral_0^1|g'|`. They converge on each character as the mesh tends to zero, and hence strongly on `H_w`, by density and the uniform bound. The limit `M_g` satisfies
\[
M_g\chi_q=g(q)\chi_q.
\tag{14}
\]
Product identities follow on the dense cylinder algebra and extend by continuity. In particular `M_g M_h=M_{gh}`. The multiplier is specified on representatives `q in [0,1)`; `g(0)` and `g(1)` need not agree. No circle-continuity hypothesis is being smuggled into (13).

Take `g_a(q)=exp(2 pi i theta_a q)`. Both `M_{g_a}` and `M_{1/g_a}` are bounded inverses by (13)--(14). Thus
\[
\mathcal D=\operatorname{diag}(M_{g_1},...,M_{g_r})
\tag{15}
\]
is a bounded invertible operator on (10). It need not be unitary in the weighted norm.

## 4. Similarity and the full spectral equality

PC-053's exact finite Fourier calculation, extended to arbitrary distinct angles as in PC-443, gives the rational-character blocks
\[
K_q^+=D(q)AD(q)^{-1}-2qI_r,
\qquad D(q)=\operatorname{diag}(e^{2\pi i\theta_aq}),
\tag{16}
\]
for all `0<=q<1`. The unaugmented block is the same for `q>0`, and equals `H` at `q=0`.

Equations (11), (14) and (16), first on cylinders, imply
\[
\boxed{\displaystyle
T^+=\mathcal D\bigl((A-I_r)\otimes I+I_r\otimes B_w^+\bigr)\mathcal D^{-1}.}
\tag{17}
\]
The right side is bounded, proving sufficiency for the augmented action. Since `A` is a finite Hermitian matrix, a constant unitary diagonalization makes the middle operator a finite direct sum of `B_w^++(lambda_alpha-1)I`. Its spectrum is exactly `mathcal B_Z` by (11). Bounded similarity and the equivalent norm (10) prove the first equality in (5).

To handle the exceptional raw block without assuming invariance of spectra under finite-rank perturbations, use the bounded Haar-average projection
\[
P_0f=\left(\int f\,d\mu\right)\mathbf1.
\tag{18}
\]
It is bounded because both `integral w` and `integral w^{-1}` are finite. It commutes with the multipliers, and `mathcal D` is the identity on `C^r tensor ran P_0`. The space `ker P_0` is the closure in `H_w` of the nonconstant characters: apply `I-P_0` to cylinder approximations.

On this kernel,
\[
\sigma(B_w^+|_{\ker P_0})=[-1,1].
\tag{19}
\]
Indeed the nonconstant rational-character eigenvalues are dense in that interval. For every `z` outside it, the `C^1` multiplier `g(q)=(1-2q-z)^{-1}` from (13) gives a bounded inverse preserving `ker P_0`. This proves both inclusions in (19), rather than deducing equality from eigenvalue density alone.

On cylinders, `T=T^+-J_r tensor P_0`, so the right side defines its bounded extension. Conjugating by (15) leaves that correction unchanged. The resulting direct decomposition has finite block `H` on the constant-fiber space and blocks `B_w^+|ker P_0+(lambda_alpha-1)I` on its complement. This proves boundedness of `T` and the second equality in (5).

## 5. Why individual A2 weights do not suffice

PC-450 constructs a positive integrable, essentially unbounded orbit `A_1` weight `W>=1` by iterating the ergodic maximal operator. It is also orbit `A_2`. For any `r>=2`, choose, up to the common normalization required in (1),
\[
w_1=W,\qquad w_2=\cdots=w_r=1.
\tag{20}
\]
All separate fiber actions are bounded by PC-451. But `w_1/w_2` is essentially unbounded, contradicting the necessary condition (9). Both full actions are therefore unbounded on their cylinder domain. This conclusion does not assert nonclosability or empty resolvent.

Conversely, if every `w_a` is bounded above and below by positive constant multiples of this same `W`, then (4) holds. Both full actions are bounded and have (5), although no equivalence with the Haar norm is available. Thus the new condition is cross-fiber compatibility, not a hidden requirement that each density be essentially bounded.

## 6. Prior art, controls and consequence

The finite affine blocks come from [[research/prime_circle/findings/PC-053-composite-cotangent-preimage-tubes-are-affine-base-inflations]] and their coherent limit from [[research/prime_circle/findings/PC-443-coherent-profinite-cotangent-tower-has-atomic-bands-and-universal-marked-moduli]]. The exact singleton weight theorem is [[research/prime_circle/findings/PC-451-cotangent-tower-boundedness-is-exactly-orbit-a2]], with the interval calculus and nontrivial weight example in [[research/prime_circle/findings/PC-450-bounded-weighted-cotangent-towers-retain-the-haar-band]].

The analytic ingredients are classical. Atencia and Martín-Reyes, *The maximal ergodic Hilbert transform with weights*, Pacific J. Math. **108** (1983), 257--263, [Theorem 1.2](https://msp.org/pjm/1983/108-2/pjm-v108-n2-p01-s.pdf), supplies the weighted ergodic input already checked in PC-451. Berkson and Gillespie, *Spectral decompositions, ergodic averages, and the Hilbert transform*, Studia Math. **144** (2001), 39--61, [DOI 10.4064/sm144-1-2](https://doi.org/10.4064/sm144-1-2), is the spectral-family prior-art boundary for (12)--(14); those exact multiplier formulas are proved here.

Weighted discrete Cauchy/Hilbert transforms with different source and destination weights also belong to established two-weight theory; see Belov, Mengestie and Seip, *Discrete Hilbert transforms on sparse sequences*, Proc. London Math. Soc. **103** (2011), 73--105, [arXiv:0912.2899](https://arxiv.org/abs/0912.2899), DOI `10.1112/plms/pdq053`. Its sparse-sequence hypotheses are not invoked for this profinite system. Here the cross-fiber restriction follows directly from one persistent matrix entry (7), without a general two-weight theorem. No historical novelty is claimed for matrix-entry testing, conditional-expectation convergence, equivalent norms, or bounded-variation multiplier calculus.

The line-local delta is a necessary and sufficient classification for **all equivalent measures on every fixed finite-base tower**, including the independent cross-fiber constraint missed by separate scalar tests, and a bounded conjugation proving full spectral equality beyond the Haar-equivalent-norm regime. PC-446's surviving-eigenvalue obstruction did not establish this equality for arbitrary nonnormal weighted realizations.

All formulas and tests work for distinct irrational-angle base points under the same embedded cotangent rule. Numerical band endpoints retain the finite base geometry through `A` and `H`; the classification does not say those endpoints agree for different bases. The bounded equivalent-measure construction cannot change the spectrum of its own Haar tower and does not acquire prime-birth selectivity. A growing base, singular measures, unbounded closed realizations, incomplete fibers, or an intrinsically changed interaction lies outside this theorem. In particular, the constants may deteriorate with the base geometry; no uniform growing-base assertion is made.

## 7. Validation and decisive audit

Standard-library Python complex-arithmetic checks used the primitive bases `d=2,3,4,5,6,8`, the antipodal base `{0,1/2}`, and the irrational-angle bases `{sqrt(2),sqrt(3)} mod 1` and `{sqrt(2),sqrt(3),sqrt(5)} mod 1`. For `m=1,2,3,6,11` and both actions, **90 finite matrix cases** verified the Fourier blocks (16), with maximum entry error below `4.4e-15`. On the positive finite weights
\[
w_{a,m}(t)=(a+1)\exp\!\left(0.7\cos\frac{2\pi t}{m}
+0.3\sin\frac{2\pi(a+t)}m\right),\qquad a=0,...,r-1,
\]
**1,840 cross-fiber same-lift entries** checked the coefficient underlying (8), with maximum error below `1.8e-14`. Inverses assembled from the Fourier blocks at `z=i,2i` had weighted residual below `7.8e-15`. Six signed values `delta=+/-0.9,+/-0.5,+/-0.01` checked the ratio in (7) at `m=100000` to error below `1e-8`. These are finite floating-point diagnostics, not an infinite norm estimate or proof of (3)--(5).

The proof's decisive checks are: retain one output coordinate before taking the factorial-partition limit in (8); use the complete action to obtain comparability, rather than assuming it from individual `A_2`; prove the phase multipliers and their inverses bounded in the common weighted norm; and separate the constant block when passing from `T^+` to `T`. A bounded full action with noncomparable fiber densities, or an off-band spectral point under (4) beyond the stated finite `H` block, would falsify the theorem. The general claim is analytically derived, not formally verified.
