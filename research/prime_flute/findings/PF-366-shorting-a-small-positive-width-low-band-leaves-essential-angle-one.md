# PF-366 — shorting a small positive-width low band leaves essential angle one

**Status:** EXACT-DERIVED + CLASSICAL-CAUCHY-AND-CONCENTRATION-METHOD + ACTUAL-GROWING-LOW-SECTOR-OBSTRUCTION.

Eliminating a growing low sector does not by itself repair the actual prime-flute seam-energy angle. For every fixed `kappa>0`, sufficiently small **fixed positive** widths `lambda` and `eta` allow all modes with `|xi|<=lambda` and `kappa<|xi|<kappa+eta` to be shorted simultaneously, on every cuff and both faces, while the angle between the remaining low and high sectors still has **essential norm one**.

The extra eliminated low sector has dimension `lambda L_i/pi+O(1)` per cuff face: this is not a finite-rank extension of constant removal. Its contribution to scalar residual loss is exponential, rather than PF-365's polynomial loss. A two-cluster inverse-Gram bound pays for its compensation coefficients even though the cosine-node spacing vanishes quadratically at frequency zero. The actual geometric growth still dominates when the two eliminated widths are sufficiently small.

The result concerns the specified actual positive-shift energy completion. It gives no relative-resolvent, scattering, zeta-zero or RH conclusion.

## 1. Exact representation and statement

Use the natural seam cut, centered zero-twist cuff coordinates of period `L_i`, and actual form of PF-364,

\[
 M=Q+\Lambda_E>0,\qquad d_i=s_{i-1}^{-1}+s_i^{-1},\qquad b_0=19/80.
 \tag{1}
\]

Let `H_M` be the completion of finitely supported, finite-Fourier-support traces on both seam faces in this positive-shift `Delta+1` energy. Fix

\[
 0<\lambda<\kappa/4,\qquad 0<\eta<W<1.
\]

The eliminated algebraic space is exactly the finite-support span of **all** constants, sines and cosines on both faces in

\[
 B_i=\{|\xi|\le\lambda\},\qquad
 T_i=\{\kappa<|\xi|<\kappa+\eta\}.
 \tag{2}
\]

Let `E` be its closure in `H_M`, and `R_E=I-P_E`. The remaining low and high algebraic spaces are the finite-support spans of all modes in

\[
 \lambda<|\xi|\le\kappa,\qquad |\xi|\ge\kappa+\eta,
 \tag{3}
\]

respectively. Set

\[
 \mathcal L=\overline{R_E L_{\rm alg}},\quad
 \mathcal H=\overline{R_E H_{\rm alg}},\quad
 Z=P_{\mathcal H}|_{\mathcal L}.
 \tag{4}
\]

These are energy-space projections, not assumed inverses of a bounded Fourier matrix on coefficient `ell^2`. In finite positive sections they give the angle normalized by the low and high diagonal blocks of the **same** shorted form.

For every fixed `kappa>0` there is `W_0>0` such that, for each fixed `0<W<W_0`, all sufficiently small positive `lambda` and `eta` satisfy

\[
 \boxed{\|Z\|_{\rm ess}=1.}
 \tag{5}
\]

The cutoffs are chosen before taking the tail limit. Section 5 gives sufficient inequalities. Witnesses use a low frequency near `nu_*=kappa/2` and only the high strip `[kappa+eta,kappa+W]`. No optimal numerical widths are asserted.

## 2. Coupled lower bound against both eliminated bands

Choose the closest positive Fourier frequency `nu_i` to `nu_*` on cuff `i`, with any fixed tie convention. Put

\[
 a_i=\cosh(\pi\nu_i),\qquad a_*=\cosh(\pi\nu_*),\qquad
 n(a)=\frac{\pi(a+1)}{2a},\qquad a_i=a_*+O(L_i^{-1}).
 \tag{6}
\]

On a sufficiently far tail these carriers lie strictly between `lambda` and `kappa`. For a finitely supported vector `u` let `f_{u,i}(t)=u_i cos(nu_i t)` on both faces. Define `A_+[u]` as the infimum of its symmetric actual energy after freeing **every remote symmetric** mode in (2).

Use nonnegative frequencies once when forming cosine products, including the constant node once on each cuff. Let

\[
 U_j=\{2\pi k/L_j:0\le2\pi k/L_j\le\lambda\}
       \cup\{2\pi k/L_j:\kappa<2\pi k/L_j<\kappa+\eta\},
\]
\[
 Q_j(a)=\prod_{\xi\in U_j}
     \left(\frac{a-\cosh(\pi\xi)}{a+\cosh(\pi\xi)}\right)^2.
 \tag{7}
\]

At a grounded boundary set `Q_0(a)=1`. For nonconsecutive module support `I`,

\[
 \boxed{A_+[u]\ge c\sum_{i\in I}n(a_i)Q_i(a_i)
 \left[s_{i-1}^{-1}Q_{i-1}(a_i)+s_i^{-1}Q_{i+1}(a_i)\right]|u_i|^2.}
 \tag{8}
\]

To justify the enlarged lower certificate, PF-363 (16) bounds actual symmetric energy below by the sum of embedded corridor integrals of the **original-coordinate** trace differences. On an edge incident to `I`, that difference contains at most one retained carrier and has exponential-term count

\[
 N_i\le\frac{\lambda+\eta}{\pi}(L_i+L_{i+1})+O(1).
 \tag{9}
\]

PF-361 (3) is independent of separation and location of frequencies. Its window bound `T_i>=b_0 max(L_i,L_(i+1))-C` therefore shows that the finite window controls a fixed fraction of the full `sech`-weighted norm whenever `lambda+eta` is sufficiently small. For instance, with PF-361's constant `B`, it suffices to require `lambda+eta<pi b_0/(8B)`. The gap between the two frequency clusters does not enter this term count.

Now independently relax the cosine coefficients from both ends of each edge in the full weighted norm. The exact scalar kernel is

\[
 \langle\cos(\xi t),\cos(\zeta t)\rangle_{\operatorname{sech}}
 =\frac{\pi\sqrt{(x+1)(y+1)}}{x+y},
 \qquad x=\cosh(\pi\xi),\quad y=\cosh(\pi\zeta).
 \tag{10}
\]

The Cauchy distance product supplies `n(a_i)` times the squared factors for the union of both eliminated node sets. Duplicates, including the common constant, are counted once by the exact residual. Counting them twice in `Q_i Q_j` only decreases the positive bound. All carrier-to-eliminated separations stay positive; neighboring eliminated nodes need no mutual separation. Sines are odd and orthogonal to the cosine residual in this scalar norm. Summing the disjoint incident edges gives (8). Other edges and seam energy are nonnegative. The bound holds for every global algebraic trial and thus for the infimum over its designated closure.

## 3. Paying for both growing compensation clusters

The upper trial uses only one cuff at a time. On cuff `i` put `h=2pi/L_i`, `m=floor(lambda/h)`, and let `J_i` be all positive lattice frequencies in `(kappa,kappa+W]`, with `N=|J_i|` and `q=N-1`. Form the cosine Gram matrix `G_i` of

\[
 \{0,h,\ldots,mh\}\ \cup\ J_i.
 \tag{11}
\]

For fixed widths, `m,N` both grow linearly with `L_i`. Set constants depending only on `kappa`,

\[
 R_0=\cosh(\pi(\kappa+1)),\quad
 v_0=\pi\sinh(\pi\kappa/2),\quad B_0=2R_0/v_0,
\]
\[
 B_1=4R_0/\pi^2,\qquad
 D=\frac{2R_0}{\cosh(\pi\kappa)-\cosh(\pi\kappa/4)}>1.
 \tag{12}
\]

For each Gram node `x_j`, the cofactor ratio of the Cauchy determinant gives

\[
 (G_i^{-1})_{jj}=\frac{2x_j}{\pi(x_j+1)}
       \prod_{k\ne j}\left(\frac{x_j+x_k}{x_j-x_k}\right)^2.
 \tag{13}
\]

For two nodes in the lower cluster, the hyperbolic cosine identity and `sinh t>=t` for `t>=0` give

\[
 |x_j-x_k|\ge\frac{\pi^2h^2}{2}|j^2-k^2|.
\]

The endpoint degeneracy is controlled by the exact factorial product

\[
 \prod_{\substack{0\le k\le m\\k\ne j}}|j^2-k^2|
 =\begin{cases}
 (m!)^2,&j=0,\\
 (m-j)!(m+j)!/2,&1\le j\le m,
 \end{cases}
 \quad\ge (m!)^2/2.
 \tag{14}
\]

Consequently the same-cluster product in (13), for a lower row, is at most

\[
 4\left(\frac{e^2B_1}{(hm)^2}\right)^{2m}.
 \tag{15}
\]

For a row in `J_i`, its same-cluster product is at most
`(2eB_0/(hq))^(2q)`, as in PF-364 (10). Every cross-cluster ratio is at most `D`. Thus (13) is bounded by a fixed constant times (15) times `D^(2N)` for lower rows, and by `(2eB_0/(hq))^(2q) D^(2(m+1))` for upper rows.

Define

\[
 \alpha_0(\lambda,W)=\max\left\{
 \frac\lambda\pi\log\frac{e^2B_1}{\lambda^2}
       +\frac W\pi\log D,
 \quad \frac W\pi\log\frac{2eB_0}{W}
       +\frac\lambda\pi\log D\right\}.
 \tag{16}
\]

The inverse trace bounds the inverse operator norm. Since `hm=lambda+O(L_i^(-1))`, `hq=W+O(L_i^(-1))` and the number of rows is `O(L_i)`, for every fixed `alpha>alpha_0(lambda,W)` one has, eventually,

\[
 \lambda_{\min}(G_i)\ge e^{-\alpha L_i}.
 \tag{17}
\]

In particular `alpha_0(lambda,W)->0` as both widths tend to zero. A uniform positive derivative of `cosh(pi xi)` at zero was **not** assumed. The quadratic spacing in (14) is the additional estimate needed beyond PF-364/PF-365.

Let `r_i` be the exact weighted least-squares residual of `cos(nu_i t)` against (11). Put

\[
 P_i(a)=\prod_{\substack{\xi\in J_i\\\xi\ge\kappa+\eta}}
       \left(\frac{a-\cosh(\pi\xi)}{a+\cosh(\pi\xi)}\right)^2.
\]

Projection contractivity and (17) give, for its compensating coefficient vector `c_i`,

\[
 H[r_i]=n(a_i)Q_i(a_i)P_i(a_i),\quad
 c_i^*G_ic_i\le n(a_i),\quad
 \left(1+\sum|c_{i,j}|\right)^2\le C L_i e^{\alpha L_i}.
 \tag{18}
\]

Here `H[f]=integral_R |f(t)|^2 sech(t)dt`. The coefficient estimate uses only one cuff's two clusters. It does not invert the union of nearly coincident lattices from neighboring cuffs.

## 4. Actual upper trial and all eliminated face parities

PF-364 (8), derived from PF-344's complete-pant trial, applies to any single-module cosine combination of bounded frequency, including zero:

\[
 M_{\rm sym}[f]\le C_Kd_iH[f_i]
          +C_KL_i\left(\sum|\text{coefficients of }f_i|\right)^2.
 \tag{19}
\]

It includes both complete adjacent pants and the actual seam. Let `F_+[u]` be the infimum after freeing the symmetric eliminated modes and the symmetric high strip. Use `u_i r_i` on each `i in I` and zero elsewhere. Nearest-neighbor assembly makes these trial costs add on nonconsecutive support, so

\[
 F_+[u]\le C\sum_{i\in I}
 \left[d_i n(a_i)Q_i(a_i)P_i(a_i)+L_i^2e^{\alpha L_i}\right]|u_i|^2.
 \tag{20}
\]

The eliminated real Fourier dimension on one face, and hence in its antisymmetric copy, is
`r_i=(lambda+eta)L_i/pi+O(1)`. PF-350's collective proof applies to this disjoint bounded-frequency union as well: each normalized sine/cosine/constant has pant self-energy `O_K(d_i/L_i+1)`, positive nearest-neighbor assembly gives `C<=2 direct-sum C_ii`, and the antisymmetric seam has lower bound `1/[w_i(1+w_i^2)]`, including zero frequency. Using `w_i d_i<=C`, the same calculation yields

\[
 C\le bQ_-,\qquad b\le C_K(\lambda+\eta)+\epsilon_{\rm tail},
 \qquad \epsilon_{\rm tail}\to0.
 \tag{21}
\]

The positive-block Schur inequality of PF-350 gives a factor `(1+b)^(-1)` before or after all symmetric eliminated modes are shorted. For actual squared distances `A[u]` from `f_u` to `E` and `F[u]` from `f_u` to eliminated-plus-full-high modes,

\[
 A[u]\ge(1+b)^{-1}A_+[u],\qquad F[u]\le F_+[u].
 \tag{22}
\]

These inequalities hold uniformly over finite sections containing any trial, then pass to the specified closures. A small fixed parity error is sufficient because it multiplies a distance ratio tending to zero; no compactness transfer under a fixed form error is asserted.

## 5. Strict margins and the infinite angle

Define the positive continuous function, on the two compensating bands,

\[
 \ell_*(\xi)=-\log\left|
       \frac{a_*-\cosh(\pi\xi)}{a_*+\cosh(\pi\xi)}\right|,
\]
\[
 \delta=\frac1\pi\left[\int_0^\lambda\ell_*(\xi)d\xi
                   +\int_\kappa^{\kappa+\eta}\ell_*(\xi)d\xi\right],
 \qquad
 \gamma=\frac1\pi\int_{\kappa+\eta}^{\kappa+W}\ell_*(\xi)d\xi.
 \tag{23}
\]

The constant endpoint is harmless here because `a_*>1`. The carrier stays a fixed distance from both eliminated bands. Riemann sums, (6), and neighboring-period comparability imply, for `j=i-1,i,i+1`,

\[
 Q_j(a_i)=e^{-\delta L_j+O(1)},\qquad
 P_i(a_i)=e^{-\gamma L_i+O(1)}.
 \tag{24}
\]

For the actual prime cuffs, the inputs of PF-364 give, for any fixed `R>40/19`,

\[
 L_i\to\infty,\quad \max(L_{i-1},L_{i+1})\le R L_i,
 \quad d_i\ge c e^{b_0L_i}.
 \tag{25}
\]

The `O(1)` in (24) includes rounding and the `O(1/L_i)` carrier displacement multiplied by neighboring lengths at most `R L_i`. Uniform separation from the eliminated bands bounds the needed derivatives; no Diophantine separation is used.

Dividing (20) by (8), and applying (22)–(25), yields

\[
 \boxed{\frac{F[u]}{A[u]}\le C\max_{i\in I}
 \left[e^{-(\gamma-R\delta)L_i}
       +L_i^2e^{-[b_0-\alpha-(1+R)\delta]L_i}\right].}
 \tag{26}
\]

Sufficient conditions are the concentration condition following (9) and

\[
 \alpha>\alpha_0(\lambda,W),\qquad
 \gamma>R\delta,\qquad \alpha+(1+R)\delta<b_0.
 \tag{27}
\]

These hold on a nonempty range of fixed positive widths. First choose `W` small enough that both `W log D/pi` and `W log(2eB_0/W)/pi` are below `b_0/2`. Fix `alpha` strictly between their maximum and `b_0`. Then take `lambda,eta` sufficiently small. Equation (16) stays below `alpha`, `delta->0`, and `gamma` tends to the strictly positive integral over `[kappa,kappa+W]`. This proves the quantifiers in (5).

On a grounded tail, (8) and (22) make the residual low span generated by each infinite spatial parity infinite dimensional. For `x=R_E f_u`,

\[
 \|Zx\|_M^2/\|x\|_M^2=1-F[u]/A[u].
 \tag{28}
\]

The right side tends uniformly to one on progressively farther such spans by (26). The kernel of any finite-rank map meets each span in a unit vector. Thus the distance of `Z` from every finite-rank map is at least one; contractivity and norm-density of finite-rank maps in compact maps give essential norm one.

Restoring a fixed finite head adds only finitely many eliminated modes, even though their number grows along the infinite tail. Project them off the closed tail eliminated space; their residual span is finite dimensional. Intersect each tail residual low span with its orthogonal complement. This leaves an infinite-dimensional span with unchanged denominator, while the old tail high trials remain admissible. Equations (26)–(28) prove (5) in the full completion of Section 1. No alternative condition at infinity or intersection vector of norm one is inferred.

## 6. Prior art, controls and boundary

The Gram residual product is classical: J. M. Almira, *Müntz Type Theorems I*, Surveys in Approximation Theory 3 (2007), Section 2.1, pp. 154–155 ([journal copy](https://www.maths.tcd.ie/EMIS/journals/SAT/papers/10/10.pdf), S31). Equation (13) follows directly by taking the principal cofactor ratio in the same Cauchy determinant. The new coefficient estimate here is derived in (14)–(17); no new general Cauchy identity is claimed.

The location-independent exponential-polynomial estimate is Theorem 1.1 of O. Friedland and Y. Yomdin, *An observation on the Turán–Nazarov inequality* ([primary paper](https://arxiv.org/abs/1107.0039), S34), specialized and integrated in PF-361. Positive shorting has the Anderson–Trapp framework, *Shorted Operators. II*, SIAM J. Appl. Math. 28 (1975), 60–71 ([publisher](https://epubs.siam.org/doi/10.1137/0128007)); the completion argument used here is explicit above. Wentworth's [DtN determinant gluing paper](https://arxiv.org/abs/2209.11863) treats compact surfaces and degeneration of determinant invariants, not this infinite-chain normalized Fourier-sector angle.

The prior-art audit covered Cauchy inverse/residual algebra, clustered Gram conditioning, exponential-polynomial concentration and surface DtN degeneration. These tools are classical. The derived addition is simultaneous elimination of a **positive-width low interval with linearly growing rank** in the actual seam form. PF-365 eliminated one constant per cuff; its polynomial residual loss and one-node congruence do not control (11). Here both the exponentially small denominator and the two-cluster coefficient amplification are included before passing to the actual infinite angle.

Supplementary standard-library exact arithmetic checked 560 factorial identities (14), for `m=1,...,32`, and 32 rational two-cluster controls: lower nodes `1+(hj)^2`, `j=0,...,m`, upper nodes `3+hj`, `j=0,...,N-1`, with `m,N in {1,2,4,6}`, `h in {1/100,1/10}`, and target node `2`. For the kernel `1/(x+y)`, exact elimination verified the residual product, every inverse diagonal, and the inverse-trace projection-coefficient bound. Six grounded paths with `2,3,4` modules tested (8) by rational positive-semidefinite elimination, using alternating retained carriers `2+i/100`, eliminated nodes `{1,1+1/100,3}` or `{1,1+1/(100+i),3+i/11}`, endpoint conductances `1/1000`, and interior conductances `10^(2i-2)` for edge `i=1,...,d-1`. All passed. These are checks of finite algebra, not actual pant solves, prime-lattice numerics, an independent review or formal verification. Scratch remains under `/tmp`.

The geometric inputs remain PF-363's trace-preserving coupled lower bound, PF-344/PF-364's complete-pant upper trial, PF-350's seam coercivity and nearest-neighbor assembly, and the period/conductance bounds (25). A failure of any input breaks the transfer. The finite scalar conditioning lemma alone is not a substitute for them; a standalone Lean transcription would not verify the actual theorem, so no bounded formalization/compute handoff is proposed.

Widths outside (27), removal of an arbitrary large part of the low spectrum, variable cutoffs not covered by these estimates, other completions and different observables remain unresolved. The result excludes compact Schatten and compact weak-Schatten classes for this specified angle. It applies to nonprime flutes satisfying the same geometric bounds, supplies no primality-specific invariant, and does not imply RH or a relative spectral theorem.
