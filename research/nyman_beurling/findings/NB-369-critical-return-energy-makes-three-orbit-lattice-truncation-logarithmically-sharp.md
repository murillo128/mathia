# NB-369 — Critical return energy makes three-orbit lattice truncation logarithmically sharp

- **Status:** proved (classical energy mechanism plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-356 for the orbit realization and bounded lattice sampler/lift; NB-368 for deterministic cubic seeds and the convergent-series upper bound
- **Classification:** LITERATURE+DERIVED + EXACT-SHARPNESS + NEGATIVE/OBSTRUCTION

## Claim and scope

The logarithm in NB-368's squared interpolation-tail bound cannot be removed under its simultaneous bad-approximation hypothesis. It is forced by critical two-dimensional reciprocal-distance energy, and survives optimization over **all exact three-orbit decompositions** when approximation is measured by the same anchor-lattice cutoff.

Fix positive real \(\alpha,\beta\) such that
\[
R_n:=\max(\|n\alpha\|_{\mathbb R/\mathbb Z},\|n\beta\|_{\mathbb R/\mathbb Z})
\ge\gamma n^{-1/2}\quad(n\ge1),\qquad \gamma>0.
\tag{1}
\]
Write \(D_n^2=\|n\alpha\|^2+\|n\beta\|^2\). For integer \(N\ge64\),
\[
\boxed{S_{\ge N}:=\sum_{n\ge N}\frac1{n^2D_n^2}
\asymp_\gamma\frac{\log N}{N}\qquad(N\ge64).}
\tag{2}
\]
In particular this applies to \((\alpha,\beta)=(\sqrt[3]2,\sqrt[3]4)\), with the explicit \(\gamma\) proved in NB-368. No new Diophantine hypothesis on that specified pair is needed.

Here is the precise physical sharpness statement. Fix \(q>1\), put \(p=q^\alpha,r=q^\beta\), and use
\[
H=L^2(0,1;dx),\quad e=1,\quad
g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad
A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},
\]
\[
\mathcal C_v=\overline{\operatorname{span}}\{A_ag_v:a\ge1\text{ real}\},
\quad\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\},
\quad t=P_{\mathcal N}e.
\]
Under the unitary Mellin map, NB-356 gives
\[
\mathcal M\mathcal C_v=B\Theta_vH^2,\quad
\mathcal Mt=Bb/s,\quad b=B(1)>0,\qquad
\Theta_v(s)=\frac{s}{s-1}\frac{1-v^{1-s}}{\sqrt v(1-v^{-s})},
\tag{3}
\]
where \(H^2=H^2(\Re s>1/2)\) and the common zeta inner factor \(B\) is retained. Let
\[
L=\log q,\quad\tau=2\pi/L,\quad z_k=1+i\tau k,
\qquad
\mathcal H_N=\{V\in H^2:V(z_k)=0\text{ whenever }|k|\ge N\},
\]
\[
\mathcal E_{v,N}=\mathcal M^{-1}(B\Theta_v\mathcal H_N)\subset\mathcal C_v.
\]
These are closed subspaces. They allow arbitrary low-index samples **and the entire kernel of the lattice sampler**; they are not finite-dimensional spaces or finite-generator Nyman sections. Define the squared component approximation cost
\[
\mathfrak D_N=
\inf_{\substack{u_v\in\mathcal C_v\ (v=q,p,r)\\u_q+u_p+u_r=t}}
\left[\operatorname{dist}_H(u_p,\mathcal E_{p,N})^2
+\operatorname{dist}_H(u_r,\mathcal E_{r,N})^2\right].
\tag{4}
\]
Then the exact-decomposition set is nonempty and
\[
\boxed{\mathfrak D_N\asymp_{q,\alpha,\beta,b,\gamma}\frac{\log N}{N}.}
\tag{5}
\]
Thus changing the exact split, including its unrestricted anchor component, cannot improve this squared cutoff cost to \(O(1/N)\). This is not a lower bound on the error of the *sum* after truncation: errors in different components may cancel.

## 1. A universal prefix lower bound from torus pair counts

Put
\[
A(M)=\sum_{1\le n<M}D_n^{-2}.
\]
For every pair of phases with nonzero denominators in this finite range,
\[
\boxed{A(M)\ge\frac1{64}M\log M\qquad(M\ge64).}
\tag{6}
\]
This part needs no Diophantine condition or equidistribution. A zero denominator instead makes the left side infinite.

Consider the \(M\) torus points \(x_i=(i\alpha,i\beta)\bmod\mathbb Z^2\), \(0\le i<M\). At scale \(j\ge1\), partition \([0,1)^2\) into \(4^j\) half-open squares of side \(2^{-j}\). If \(c_Q\) counts the points in a square, the number of **ordered distinct** pairs in a common square is
\[
C_j=\sum_Qc_Q(c_Q-1)\ge M^2/4^j-M.
\tag{7}
\]
Set \(J=\lfloor\log_4(M/2)\rfloor\). For \(1\le j\le J\), (7) gives \(4^jC_j\ge M^2/2\).

For a fixed distinct pair \((i,h)\), let \(\rho=\|x_i-x_h\|_{\infty,\mathbb T^2}\). If it shares a square at scale \(j\), then \(\rho<2^{-j}\). Therefore
\[
\sum_{j=1}^J4^j\mathbf1_{\text{same square at scale }j}
\le\frac4{3\rho^2}.
\tag{8}
\]
The geometric-series factor in (8) pays for counting the same pair at multiple scales. Summing over pairs yields
\[
E_\infty(M):=\sum_{i\ne h}\|x_i-x_h\|_{\infty,\mathbb T^2}^{-2}
\ge\frac34\sum_{j=1}^J4^jC_j\ge\frac38M^2J.
\tag{9}
\]
The orbit's difference structure, and \(D_n^2\le2R_n^2\), give
\[
E_\infty(M)=2\sum_{n=1}^{M-1}(M-n)R_n^{-2}
\le4M A(M).
\tag{10}
\]
Thus \(A(M)\ge3MJ/32\). For \(M\ge64\),
\(J\ge\log M/(2\log4)\), which implies (6). The logarithm counts spatial scales; it is not an estimate for the number of exceptionally close returns alone.

## 2. Bad approximation prevents the prefix mass from hiding below the cutoff

A prefix lower bound by itself does **not** bound every tail: early large summands might exhaust it. Condition (1) supplies the upper bound needed to remove that possibility.

Enumerate the indices with \(R_n\le y\) as \(n_1<n_2<\cdots\), for \(0<y\le1/2\). Applying (1) to the first index and to consecutive differences gives
\[
n_1\ge(\gamma/y)^2,\qquad
n_{i+1}-n_i\ge(\gamma/(2y))^2,
\quad n_i\ge i(\gamma/(2y))^2.
\tag{11}
\]
If \(\rho_1\le\cdots\le\rho_{M-1}\) are the ordered values of \(R_n\) for \(1\le n<M\), then \(\rho_j\ge(\gamma/2)\sqrt{j/M}\). Consequently
\[
A(M)\le\sum_{n<M}R_n^{-2}
\le4\gamma^{-2}M H_{M-1}
\le8\gamma^{-2}M\log M\quad(M\ge2).
\tag{12}
\]
Here \(H_m=\sum_{j=1}^m1/j\). Choose once and for all an integer
\[
K\ge\max(2,1024\gamma^{-2}).
\]
For every integer \(N\ge64\), (6) and (12) imply
\[
A(KN)-A(N)
\ge\frac{KN\log(KN)}{64}-8\gamma^{-2}N\log N
\ge\frac{KN\log N}{128}.
\]
Therefore
\[
\boxed{S_{\ge N}\ge\sum_{N\le n<KN}\frac1{n^2D_n^2}
\ge\frac{\log N}{128KN}.}
\tag{13}
\]
The upper bound from NB-368 is
\[
S_{\ge N}\le16\gamma^{-2}\frac{1+\log(2N)}N,
\tag{14}
\]
which proves (2). The constants in (13) are deliberately nonoptimal. The fixed multiplicative block enlargement is essential to this proof; no lower bound for each exact dyadic block is asserted.

## 3. The cutoff cost is comparable to the complete weighted sample tail

Let \(f=b/s\) and, for \(k\ne0\), put
\[
a_k=|\Theta_p(z_k)|^2+|\Theta_r(z_k)|^2,
\qquad T_{\ge N}=\sum_{|k|\ge N}\frac{|f(z_k)|^2}{a_k}.
\]
The explicit factors in (3) satisfy
\[
a_k\asymp_{q,p,r}D_{|k|}^2,\qquad
|f(z_k)|^2\asymp_{q,b}|k|^{-2}.
\tag{15}
\]
In particular \(a_k>0\), \(T_{\ge1}<\infty\), and \(T_{\ge N}\asymp S_{\ge N}\). NB-356 supplies the sampler and lift bounds
\[
\sum_{k\in\mathbb Z}|F(z_k)|^2\le C_q\|F\|_{H^2}^2,
\quad C_q=\frac L{1-q^{-1}},\qquad
(R_qd)(z_k)=d_k,\quad \|R_qd\|^2\le(q/L)\|d\|_2^2.
\tag{16}
\]

Take **any** exact decomposition \(f=\Theta_qU_q+\Theta_pU_p+\Theta_rU_r\). At \(z_k\), \(k\ne0\), the anchor vanishes, so Cauchy--Schwarz gives
\[
\frac{|f(z_k)|^2}{a_k}\le |U_p(z_k)|^2+|U_r(z_k)|^2.
\]
For arbitrary \(V_p,V_r\in\mathcal H_N\), these tail samples are also the samples of \(U_p-V_p,U_r-V_r\). Summing over \(|k|\ge N\) and using (16) proves
\[
\|U_p-V_p\|^2+\|U_r-V_r\|^2\ge C_q^{-1}T_{\ge N}.
\tag{17}
\]
Multiplication by \(B\Theta_v\) is isometric. Taking both infima in (4) proves its lower bound, without assuming the split is samplewise optimal.

For the reverse bound, use the square-summable minimum-norm data
\[
d_{v,k}=f(z_k)\overline{\Theta_v(z_k)}/a_k\quad(k\ne0,\ v=p,r),
\qquad d_{v,0}=0.
\]
Let \(U_v=R_qd_v\). The remaining numerator vanishes at all the zeros of the pure Blaschke factor \(\Theta_q\), so
\[
U_q=(f-\Theta_pU_p-\Theta_rU_r)/\Theta_q\in H^2.
\]
This is an exact decomposition with finite anchor norm: for
\(H_*:=\|U_p\|^2+\|U_r\|^2\), one has \(\|U_q\|\le b+\sqrt{2H_*}\). The point \(z_0=1\) is removable and nonzero for \(\Theta_q\), and imposes no divisibility condition.

Set \(V_v=R_q(d_v\mathbf1_{|k|<N})\in\mathcal H_N\). Then
\[
\sum_{v=p,r}\|U_v-V_v\|^2\le(q/L)T_{\ge N}.
\]
Together with (17), this yields the explicit comparison
\[
\boxed{\frac{1-q^{-1}}L T_{\ge N}\le\mathfrak D_N
\le\frac qL T_{\ge N}.}
\tag{18}
\]
Equations (2), (15), and (18) prove (5). They also prove that the particular Fourier-data truncation in NB-368 has squared component error of this same order. The lower bound allows arbitrary changes in the sampler kernel, so that freedom cannot remove the logarithm.

## Prior art, mathematical delta, and boundaries

The energy mechanism is classical. Hardin and Saff, *Minimal Riesz Energy Point Configurations for Rectifiable d-Dimensional Manifolds*, [Theorem 2.1 and Lemma 3.1, arXiv:math-ph/0311024v3](https://arxiv.org/pdf/math-ph/0311024), establish the critical \(M^2\log M\) scale for reciprocal-distance energy at exponent equal to dimension. The argument (7)--(10) directly proves the needed torus version and constants; it does not assume that these orbit points minimize energy, nor apply a Euclidean theorem to a different metric without a comparison.

Fregoli, *Sums of reciprocals of fractional parts*, [Section 1, gap argument preceding Theorem 1.2](https://pure.royalholloway.ac.uk/ws/files/34774891/1805.00865v1.pdf), is the neighboring classical source for the return-gap upper-bound mechanism, already anchored for NB-368. Its reciprocal linear-form sum is different from the sum of squared coordinate distances here. Both required bounds are proved above, with the maximum norm and Euclidean denominator kept distinct. The Hardy interpolation machinery is already reconstructed in NB-356. No new general energy, interpolation, or Diophantine theorem is claimed.

NB-368 establishes a convergent series and an upper bound for one construction. The additional result here is the matching cutoff obstruction after optimizing the *physical* component split, not another example of finite-energy membership. The source of sharpness is universal two-dimensional recurrence energy combined with a target whose anchor-lattice samples have size comparable to \(1/|k|\).

- The sharpness concerns the declared anchor-lattice cutoff. A different sampling geometry or a scheme retaining selected high-index samples is not excluded.
- The spaces \(\mathcal E_{v,N}\) remain infinite-dimensional. Neither (5) nor (18) counts dilation generators, limits their range, or bounds their absolute coefficients.
- Component approximation cost is not the Nyman target residual. There is no lower bound here for \(\|t-w\|\) in terms of \(N\), and no finite discrete-section rate follows.
- The two non-anchor components are counted together. No individual lower bound for each is asserted. Optimizing the anchor cannot evade (17), because its factor vanishes on the retained test lattice.
- The inner factor and projected target remain in the definitions. Every orbit sum \(w\) still satisfies \(\|e-w\|^2=1-b^2+\|t-w\|^2\). The Burnol floor and RH are unchanged; the construction is not source-only access to the unknown \(B\).
- Condition (1) supplies the crucial prefix upper bound. The universal prefix lower bound alone does not give (2) for arbitrary phase pairs. No conclusion for the specified integer triple \(2,3,5\), or for the exceptional-completion question of NB-366, is obtained.

Evidence is the analytic proof and inspected primary literature. An ephemeral exact-rational audit used 64 torus-orbit prefixes of sizes 2 through 256, passing 112 cell-count checks, 364,072 pairwise multiscale checks, and 4,504 ordered-return checks. It used finite rational controls with no collisions within each prefix, not purported infinite badly approximable examples. These checks audit factors, multiplicities, and ordering; they do not prove any infinite tail or Hardy assertion. The decisive analytic checks are paying repeated pair counts in (8), subtracting the prefix with a fixed sufficiently large \(K\), and enforcing (17) for every exact split. No Lean verification or independent adversarial approval is asserted.
