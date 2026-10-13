# PC-443 — Coherent profinite cotangent towers have atomic spectral type and universal marked moduli

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. The geometry-forced normalization of the PC-053 cotangent matrices is compatible with **every** power-map refinement and therefore defines a bounded self-adjoint operator on a genuine inverse-limit Hilbert space. Its essential spectrum consists of the same finite bands seen empirically in PC-099, but its spectral type is **pure point**, not absolutely continuous. Meanwhile the PC-442 cotangent/base-marked associative-product parameters survive exact cross-level compatibility as independent rational-character ratios. Both constructions have nonarithmetic, geometrically matched controls. Neither supplies a new zeta-zero or RH mechanism.

## 1. Exact inverse system and the normalized operator

Fix $d>1$, let $r=\varphi(d)$ and $B=P_d^*$, and use the complete tubes and original cotangent matrices of PC-053:
\[
Y_m=\{y\in S^1:y^m\in B\},\qquad
A_m=\mathbb C^{Y_m},\qquad C_m=C_{d,m}.
\tag{1}
\]
For $m\mid n$, put $k=n/m$ and define the *intrinsic*, unital pullback
\[
P_{m,n}:A_m\longrightarrow A_n,\qquad
(P_{m,n}f)(y)=f(y^k).
\tag{2}
\]
Give each $A_m$ the $L^2$ inner product for the uniform **probability** measure on $Y_m$. Every point of $Y_m$ has exactly $k$ preimages in $Y_n$, so $P_{m,n}$ is an isometry. The maps compose exactly.

Let $J_m$ be the all-ones matrix on $Y_m$. Then the **unnormalized** operators do not commute with refinement, but the correct scaling law is
\[
C_nP_{m,n}=kP_{m,n}C_m,\qquad
J_nP_{m,n}=kP_{m,n}J_m.
\tag{3}
\]
Consequently
\[
\boxed{\quad B_m=\frac{C_m}{m},\qquad
B_m^+=\frac{C_m+J_m}{m},\qquad
B_n^{(\!+\!)}P_{m,n}=P_{m,n}B_m^{(\!+\!)}.\quad}
\tag{4}
\]

Here is an exact proof, not merely a spectral matching. Choose representatives $a\in U(d)$ and write $y_{a,t}^{(m)}=\exp(2\pi i(a+dt)/(dm))$. Raising $y_{a,u}^{(mk)}$ to the $k$th power sends its lift index to $u\bmod m$. Thus the fiber Fourier character $j/m$ pulls back to the character $kj/(mk)$ with the **same** rational value. PC-053 gives, for $0\le j<m$,
\[
\frac{K_{m,0}}m=H_d,\qquad
\frac{K_{m,j}}m=D_{j/m}(H_d+J_d)D_{j/m}^{-1}-2\frac jm I
\quad(j>0),\qquad
D_q(a,a)=e^{2\pi iqa/d}.
\tag{5}
\]
The expressions in (5) are unchanged by $m\mapsto mk$, $j\mapsto kj$; this proves the first part of (3). The all-ones relation follows by counting the $k$ preimages of each vertex.

Form the compact profinite space $X=\varprojlim_m Y_m$, whose $r$ fibers are torsors for $\varprojlim\mu_m\simeq\widehat{\mathbb Z}$. The isometries (2) realize
\[
\mathcal H=\overline{\bigcup_mP_m A_m}
=L^2(X,\text{base-uniform}\times\text{fiber-Haar}).
\tag{6}
\]
The character group of the fiber is $\mathbb Q/\mathbb Z$. Because the diagonal matrices $D_q$ in (5) are unitary,
\[
\|B_m\|\le \max\{\|H_d\|,\|H_d+J_d\|+2\},\qquad
\|B_m^+\|\le\|H_d+J_d\|+2.
\tag{7}
\]
Hence (4) defines unique bounded **self-adjoint** operators $B_\infty,B_\infty^+$ on $\mathcal H$ by continuity. No unidentified unbounded limit or choice of subsequence is involved.

## 2. Dense eigenvalues do not give absolutely continuous spectral type

Write $A_d=H_d+J_d$, and use the representative $q\in[0,1)$ for a character of $\mathbb Q/\mathbb Z$. Fourier analysis of (6) gives a unitary decomposition
\[
\mathcal H\simeq\bigoplus_{q\in\mathbb Q/\mathbb Z}\mathbb C^r,
\tag{8}
\]
under which $B_\infty$ acts by the finite Hermitian blocks
\[
\boxed{\quad
\mathcal K_0=H_d,\qquad
\mathcal K_q=D_qA_dD_q^{-1}-2qI\quad(0<q<1).
\quad}
\tag{9}
\]
For $B_\infty^+$, replace only $\mathcal K_0$ by $A_d$. Every block has a full orthonormal eigenbasis, and their union is an orthonormal eigenbasis of $\mathcal H$. **Every vector spectral measure is therefore countably atomic**; the absolutely continuous and singular-continuous spectral subspaces are zero.

Let $\lambda_1,\ldots,\lambda_r$ be the real eigenvalues of $A_d$, including multiplicity, and set
\[
\mathscr B_d=\bigcup_{\alpha=1}^{r}[\lambda_\alpha-2,\lambda_\alpha].
\tag{10}
\]
The rational numbers $0<q<1$ are dense in $(0,1)$, so the direct-sum spectral theorem gives
\[
\boxed{\quad
\sigma(B_\infty^+)=\sigma_{\rm ess}(B_\infty^+)=\mathscr B_d,\qquad
\sigma_{\rm ess}(B_\infty)=\mathscr B_d,\qquad
\sigma(B_\infty)=\mathscr B_d\cup\sigma(H_d).
\quad}
\tag{11}
\]
Any isolated eigenvalues of the unaugmented $B_\infty$ outside $\mathscr B_d$ come exclusively from the finite-dimensional zero-character block $H_d$. Band endpoints and irrational interior values need not themselves be eigenvalues; **pure-point spectral type** does not mean that every point of the topological spectrum is an eigenvalue.

PC-099 independently established that the normalized **finite-matrix empirical eigenvalue measures** converge weakly to
\[
\mu_d(dx)=\frac1{2r}\sum_{\alpha=1}^r
\mathbf1_{[\lambda_\alpha-2,\lambda_\alpha]}(x)\,dx,
\tag{12}
\]
an absolutely continuous probability law. Equations (8)--(11) resolve an important ambiguity left by that result: (12) is the limit of *changing normalized finite-dimensional traces*, **not** a vector spectral measure or a normal-state spectral distribution of $B_\infty$ or $B_\infty^+$. Indeed every normal positive state $\rho$ on $B(\mathcal H)$ yields the atomic distribution
$\operatorname{Tr}(\rho\,E_{B_\infty}(\cdot))$, by (8)--(9). Thus the empirical-band limit and the compatible-operator limit have the same essential spectral **support** but incompatible spectral **types**. Neither limit secretly creates an absolutely continuous Hilbert-space spectral component.

## 3. Exact cross-level classification of cotangent/base-marked products

There is a separate finite-to-infinite ambiguity in PC-442. On every $A_m[[\varepsilon]]$, allow an associative, unital, fiber-translation-equivariant formal product $\star_m$ reducing to pointwise multiplication, with the exact intrinsic base-coordinate left action
\[
b_m\star_m f=b_mf,\qquad b_m(y)=y^m.
\tag{13}
\]
Require **all** the pullbacks (2) to be algebra homomorphisms between the deformed products. Compare such families only by formal maps $S_m=I+O(\varepsilon)$ that fix the unit, commute with $M_{b_m}$, the fiber action and the fixed external cotangent mark $C_m$, and satisfy $S_nP_{m,n}=P_{m,n}S_m$. The same condition with $B_m=C_m/m$ is equivalent. This is a defined category of *external* operator marks; it does not assert that cotangent is a derivation of the deformed products.

PC-442 gives a **unique** transport $T_m$ for each product, with
\[
f\star_m g=T_m^{-1}((T_mf)(T_mg)),\qquad
T_m|_{V_{a,j}}=t_{a,j/m}^{(m)}I,\quad
t_{a,0}^{(m)}=1.
\tag{14}
\]
Compatibility is stronger than a suggestive equality of moduli. The map
\[
T_nP_{m,n}T_m^{-1}: (\mathbb C^{Y_m}[[\varepsilon]],\cdot)
\longrightarrow(\mathbb C^{Y_n}[[\varepsilon]],\cdot)
\tag{15}
\]
is an algebra homomorphism congruent to $P_{m,n}$ modulo $\varepsilon$. Each point idempotent must map to the same $0$--$1$ indicator as at order zero, because a formal power series over $\mathbb C$ has no idempotents other than $0$ and $1$. Consequently (15) is **exactly** $P_{m,n}$, and
\[
T_nP_{m,n}=P_{m,n}T_m,\qquad
t_{a,kj/(mk)}^{(mk)}=t_{a,j/m}^{(m)}.
\tag{16}
\]
Conversely arbitrary unit series $t_{a,q}\in 1+\varepsilon\mathbb C[[\varepsilon]]$ indexed by $a\in U(d)$ and $q\in\mathbb Q/\mathbb Z\setminus\{0\}$, with $t_{a,0}=1$, restrict to transports satisfying all (16) and hence to a compatible product family.

For $q\ne0$, the off-diagonal entries of the $q$-block (9) are all nonzero:
\[
(\mathcal K_q)_{a,c}
=e^{2\pi iq(a-c)/d}
\left(1+i\cot\frac{\pi(a-c)}d\right)\ne0
\quad(a\ne c).
\tag{17}
\]
Therefore, exactly as in PC-442, an admissible $S_m$ must act by a *common* unit scalar $s_q$ across all base vertices in a fixed character sector; cross-level compatibility identifies that scalar at each representation of $q$. Choosing $a_0\in U(d)$ gives the **complete algebraic marked-diagram quotient**
\[
\boxed{\quad
\{(\star_m)_m\}/\!\sim\
\ \simeq\
\prod_{\substack{a\in U(d)\setminus\{a_0\}\\
q\in(\mathbb Q/\mathbb Z)\setminus\{0\}}}
(1+\varepsilon\mathbb C[[\varepsilon]]),\qquad
u_{a,q}=\frac{t_{a,q}}{t_{a_0,q}}.
\quad}
\tag{18}
\]
This is an exact all-order classification, not a dimension extrapolation. For $r=1$ it is trivial; for $r>1$ it has countably many independent formal series. Without the extra cotangent mark the same **compatible** family is removed by the compatible $T_m$, so these are not nonzero Hochschild classes.

The full parameter product in (18) is an **algebraic** classification on the locally constant direct-limit algebra; arbitrary parameter families are not asserted to extend as uniformly bounded Fourier multipliers on $C(X)$ or $L^2(X)$. Nevertheless the nontriviality is not solely a discontinuous algebraic artifact. Let $E$ be normalized Haar averaging in each profinite fiber and choose fixed complex numbers $c_a$, not all equal. The level-compatible transport
\[
T_\varepsilon=E+(I+\varepsilon M_c)(I-E),
\quad c(y)=c_a\text{ on the fiber over }a,
\tag{19}
\]
acts with $t_{a,0}=1$ and $t_{a,q}=1+\varepsilon c_a$ for $q\ne0$. It and its inverse extend coefficientwise as bounded maps on $C(X)$ and $\mathcal H$ (and are analytically invertible for sufficiently small complex $\varepsilon$). Equation (18) makes its nonconstant ratios genuinely inequivalent **in the externally marked category**, even with a continuous witness.

## 4. Genuine geometric control, prior art and RH boundary

None of the above uses a prime-birth selector. Replace $B=P_d^*$ by any $r$ distinct, possibly non-root-of-unity circle points $\beta_a=e^{2\pi i\theta_a}$, form their complete $m$th-root tubes, use the **same oriented cotangent kernel** and power-map pullbacks, and keep the separating base multiplication mark. The identical Fourier computation gives
\[
\mathcal K^{\rm ctl}_q
=D_q^{\rm ctl}(H_B+J_r)(D_q^{\rm ctl})^{-1}-2qI,
\quad D_q^{\rm ctl}(a,a)=e^{2\pi iq\theta_a},
\tag{20}
\]
with $H_B(a,c)=i\cot(\pi(\theta_a-\theta_c))$ for $a\ne c$, zero diagonal. All nonconstant off-diagonal entries are nonzero. Thus (3)--(4), the pure-point/essential-band dichotomy, and the *same abstract parameter quotient* (18) hold for a geometry-matched nonarithmetic source. Exact numerical band endpoints may depend on the chosen base set; their **finite-source dependence and spectral type**, not universal equality of all endpoints, are the control-blind features.

**Prior art:** PC-053 supplies the finite fiber Fourier identity, PC-099 the empirical uniform-band law, and PC-440--PC-442 finite formal rigidity and marked quotients. Pontryagin duality, Haar Fourier analysis on profinite compact abelian groups and diagonal direct-sum spectral theory are standard; see Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press (2016). Diagram-level distinctions despite rigid constituents are part of established deformation theory; see M. Gerstenhaber and A. Giaquinto, *Deformations associated with rigid algebras*, *J. Homotopy Relat. Struct.* **10** (2015), 437--458, DOI 10.1007/s40062-013-0068-x. No priority claim is made for these abstract ingredients. The Prime-Circle increment is the **exact refinement intertwiner**, the distinction between empirical and normal-state spectral limits, and the jointly marked **refinement-compatible** classification tested against an actual cotangent control.

The theorem fixes a finite base conductor $d$ and uses **complete** tubes, uniform Hilbert probability measures, the $1/m$ cotangent normalization, and the exact formal marked category (13)--(18). It does not analyze a simultaneous $d\to\infty$ limit, incomplete/asymmetrically weighted fibers, nonassociative couplings, or other normalizations. It shows in particular that retaining all compatible refinement levels neither upgrades PC-099's empirical bands to a continuous-spectral RH mechanism nor forces the PC-442 marked parameters to acquire prime-specific constraints.

**Decisive audit:** Check (3) explicitly for $(d,m,k)=(3,2,3)$ and $(5,3,2)$ or prove it from (5) for all $m,k$. Verify isometry under normalized counting measure, uniform bound (7), and the rational-character decomposition (8); distinguish essential spectrum from pure-point *spectral type* and compare a fixed vector's atomic spectral measure with the changing normalized trace in (12). For (18), test the idempotent argument (15)--(16), all-order transport uniqueness, off-diagonal connectivity (17), and the continuous example (19). Repeat (20) using a base with irrational angles. A failure of any of these exact compatibilities, or a new constraint imposed by the stated marks and pullbacks, would invalidate the corresponding part of the result.