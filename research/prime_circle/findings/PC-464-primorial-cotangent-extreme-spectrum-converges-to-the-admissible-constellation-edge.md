# PC-464 — Primorial cotangent extreme spectrum converges to the admissible constellation edge

**Status:** EXACT-DERIVED + LITERATURE+DERIVED. The full conductor-scaled primorial cotangent norm converges, uniformly over complete refinement, to the supremum of the finite admissible-constellation norms from PC-463. A sieve-controlled Fourier approximation supplies the uniform operator-norm step that fixed-size population laws do not provide. Exact refinement formulas also give strictly decreasing finite-matrix upper certificates and an edge strictly below `(1+2/sqrt(3))/6<1/2`. This identifies and bounds the limiting spectral edge, without determining its exact value, constructing a common-space norm limit, localizing individual eigenvectors, or making an RH claim. No historical priority is asserted.

## 1. Objects and theorem

Let
\[
d_y=\prod_{p\le y}p,\qquad N=d_y m,\quad m\ge1,
\qquad Y=\{a\bmod N:(a,d_y)=1\},
\]
\[
T_{ab}=\begin{cases}
\dfrac{i}{N}\cot\dfrac{\pi(a-b)}N,&a\ne b,\\
0,&a=b,
\end{cases}
\qquad T^+=T+J_{|Y|}/N.
\tag{1}
\]
The augmentation includes its diagonal. For any finite integer set `F`, put
\[
(L_F)_{ab}=\begin{cases}i/[\pi(a-b)],&a\ne b,\\0,&a=b.\end{cases}
\]
Call `F` admissible if `|F mod p|<p` for every prime `p`, and define
\[
\beta_\infty=\sup_{F\text{ finite admissible}}\|L_F\|.
\tag{2}
\]
Translation does not change this norm. This is exactly `lim_k beta_k` in [[research/prime_circle/findings/PC-463-every-fixed-cotangent-population-level-is-a-finite-constellation-law]]. That finding proves that the finite-cardinality maxima are attained and strictly increase, with `beta_3=7/(12 pi)` and `beta_infinity<=1/2`.

**Theorem.** For either convention in (1),
\[
\boxed{\quad
\lim_{y\to\infty}\sup_{m\ge1}
\left|\|T^{(+)}\|-\beta_\infty\right|=0.
\quad}
\tag{3}
\]
The largest and smallest eigenvalues separately converge, uniformly in `m`, to `beta_infinity` and `-beta_infinity`. In particular, for every fixed `t>beta_infinity`, both signed eigenvalue counts above magnitude `t` are **zero** for every refinement once `y` is sufficiently large. This strengthens PC-463's bound by every fixed inverse power of `log y`, which alone allowed surviving exceptional eigenvalues.

The proof gives a finite-window certificate. Set
\[
M_L=\max_{\substack{F\subset\{0,\ldots,L-1\}\\F\text{ admissible}}}\|L_F\|,
\tag{4}
\]
with norm zero for the empty set. For the parameters constructed below,
\[
\boxed{\quad
M_L\le\beta_\infty\le
M_L+2\varepsilon+4\frac{\varphi(q)}q+\frac{R}{\pi L}.
\quad}
\tag{5}
\]
Here `q` is any fixed primorial, `0<delta<1/(2q)`, `R` is a sufficiently large Fejer degree depending on `delta,epsilon`, and `L>R` is any integer. Thus finite enumeration can in principle bracket the edge to arbitrary precision. No practical complexity or convergence rate for that enumeration is claimed.

Section 5a gives an alternative upper certificate requiring only one finite primitive-shell matrix. Its upper values decrease strictly as new primes enter the modulus and converge to the same edge. The augmented norm is exactly independent of refinement; the raw norm differs from it by at most `2/N`, substantially less than the norm of the rank-one augmentation when many vertices are retained.

## 2. Exact periodic projection bound near a Fourier jump

Work first on all coordinates of `Z/NZ`, with normalized Fourier vectors
\[
e_j(a)=N^{-1/2}e^{2\pi ija/N}.
\]
Let `q|N`, let `A subset Z/qZ`, and let `U` be the full periodic lift of `A`. Write `P_U` for coordinate projection and `eta=|A|/q`. Direct summation over the `N/q` lifts gives
\[
\langle e_j,P_Ue_k\rangle=0
\quad\text{unless}\quad j-k\equiv0\pmod{N/q},
\qquad
\langle e_j,P_Ue_j\rangle=\eta.
\tag{6}
\]
If a frequency set `E` lies in one circular arc of length strictly less than `1/q` in the variable `j/N`, no two distinct frequencies in `E` differ by a nonzero multiple of `N/q`. For its Fourier projection `P_E`,
\[
P_EP_UP_E=\eta P_E,
\qquad
\|P_UP_EP_U\|=\eta
\tag{7}
\]
when `E` is nonempty; the empty case has norm zero. The norm identity follows from the equal squared norms of `P_UP_E` and its adjoint. For every `Y subset U`, compression yields
\[
\|P_YP_EP_Y\|\le\eta.
\tag{8}
\]
This is a finite Fourier orthogonality identity for arbitrary periodic masks. It does not use primality. For the target support, take `q=d_z` with `z<=y` and `A=(Z/qZ)^*`; then `Y subset U` and `eta=varphi(q)/q`.

The strict arc-width condition is essential. Already with `q=6`, `N=60`, the Fourier indices `0,10` have off-diagonal entry `1/6` in (6) for the unit-residue mask, so (7) fails on this wider set. Small global cardinality alone also would not give (8) for an arbitrary support: periodic containment is the load-bearing hypothesis.

## 3. Fejer approximation becomes uniform after sieve compression

The full normalized cotangent matrix `K_N`, before restriction to `Y`, has Fourier multiplier
\[
h(0)=0,\qquad h(x)=1-2x\quad(0<x<1),
\qquad K_Ne_j=h(j/N)e_j.
\tag{9}
\]
This is the full-polygon identity in [[research/prime_circle/findings/PC-457-growing-base-cotangent-towers-require-conductor-scale-normalization]], §2. It fixes both the sign and the conductor normalization. Thus `T=P_YK_NP_Y` on the retained coordinate space.

The real Fejer polynomial of this periodic sawtooth is
\[
p_R(x)=\frac2\pi\sum_{r=1}^R
\left(1-\frac r{R+1}\right)\frac{\sin(2\pi rx)}r.
\tag{10}
\]
Positivity and unit integral of the Fejer kernel give `|p_R|<=1`. For every fixed `delta>0` and `epsilon>0`, one can choose `R` so that
\[
|h(x)-p_R(x)|\le\varepsilon
\quad\text{when}\quad \operatorname{dist}(x,\mathbb Z)\ge\delta.
\tag{11}
\]
This is uniform convergence away from the jump, not uniform approximation of the discontinuous multiplier on the whole circle. An explicit sufficient estimate follows from
\[
F_R(u)=\frac1{R+1}
\left(\frac{\sin(\pi(R+1)u)}{\sin(\pi u)}\right)^2.
\]
For `0<tau<delta<1/2`, split its convolution into circular distances below and above `tau`. On the first part the sawtooth changes by at most `2 tau`; on the second it changes by at most `2`. Therefore the left side of (11) is at most
\[
2\tau+\frac{2}{(R+1)\sin^2(\pi\tau)}.
\tag{12}
\]
Choose `tau` first and then `R` to make this at most `epsilon`.

Let `G_(N,R)` have Fourier multiplier `p_R(j/N)`, and put `B=P_YG_(N,R)P_Y`. With `E={j:dist(j/N,Z)<delta}` and `2 delta<1/q`, (11) and `|h-p_R|<=2` imply the self-adjoint order bounds
\[
-\varepsilon I-2P_E\le K_N-G_{N,R}\le\varepsilon I+2P_E.
\]
Compress and apply (8):
\[
\boxed{\quad\|T-B\|\le\varepsilon+2\eta=:a.\quad}
\tag{13}
\]
For fixed `q,delta,epsilon,R`, this holds for every `y>=z` and every `m`, with no dimension factor. Since `varphi(d_z)/d_z -> 0`, the error can be made arbitrarily small by choosing `z`, then the smoothing parameters, before taking the conductor limit.

For `N>2R`, the polynomial has the exact finite-range coordinate kernel
\[
(G_{N,R})_{ab}=\begin{cases}
\dfrac{i}{\pi r}\left(1-\dfrac{|r|}{R+1}\right),&0<|r|\le R,\\
0,&\text{otherwise},
\end{cases}
\tag{14}
\]
where `r` is the signed circular displacement `a-b`. Thus (13) is an operator-norm approximation by a **tapered** short-range kernel. It is not an assertion that the absolute row sum of the untapered `1/r` tail is small.

## 4. Sliding windows localize the quadratic form

Choose `L>R`, `N>2L`, and let `I_s={s,...,s+L-1}` be the cyclic windows. Denote coordinate projection onto `Y intersect I_s` by `Q_s`. Define
\[
\mathcal A=\frac1L\sum_{s\bmod N}Q_sBQ_s.
\tag{15}
\]
Every coordinate belongs to exactly `L` windows. A pair at circular distance `r<=R` belongs to exactly `L-r` windows, so `mathcal A` multiplies its entry of `B` by `1-r/L`. Its error has row sums bounded by
\[
\frac2{\pi L}\sum_{r=1}^R
\left(1-\frac r{R+1}\right)=\frac R{\pi L}.
\]
Hermiticity gives
\[
\|B-\mathcal A\|\le\frac R{\pi L},
\qquad
\|\mathcal A\|\le\max_s\|Q_sBQ_s\|.
\tag{16}
\]
For the second inequality, bound each quadratic form by its local norm and use `sum_s ||Q_s v||^2=L||v||^2`. Inserting (13) once globally and once inside each window proves
\[
\boxed{\quad
\|T\|\le\max_s\|Q_sTQ_s\|+2a+\frac R{\pi L}.
\quad}
\tag{17}
\]
No spectral count or exceptional-vertex deletion occurs here. Consequently the estimate controls even a single extreme eigenvalue. It produces a bounded-window Rayleigh witness to within the stated error; it does not assert support localization of a full-matrix eigenvector.

## 5. Local admissibility and occurrence close the norm limit

When `y>=L`, lift a cyclic window to integer offsets in `[0,L-1]`, and call its retained shape `F_s`. For every prime `p<=y`, it misses the residue `-s mod p`, because `p|N` and all its vertices survive the sieve. For `p>y`, its cardinality is at most `L<p`, so it cannot cover all residues. Thus **every** such local shape is admissible, including windows crossing the coordinate cut.

For `0<|r|<L` and `N>2L`,
\[
\left|\frac1N\cot\frac{\pi r}N-\frac1{\pi r}\right|
\le\frac{\pi^2|r|}{6N^2}.
\tag{18}
\]
Indeed for `0<x<pi/2`, use
`sin x-x cos x=int_0^x t sin t dt<=x^3/3` and `sin x>=2x/pi`.
The absolute row-sum estimate on a window gives
\[
\|Q_sTQ_s-L_{F_s}\|\le\frac{\pi^2L^2}{6N^2}.
\]
Together with (17), this proves the explicit upper bound
\[
\|T\|\le M_L+2\varepsilon+4\eta+
\frac R{\pi L}+\frac{\pi^2L^2}{6N^2}
\quad(y\ge\max(z,L),\ N>2L).
\tag{19}
\]
Given any desired error, first choose `z` so that `eta` is small, then `delta<1/(2d_z)`, then `epsilon` and `R` satisfying (11), then `L>R` making `R/(pi L)` small. Hold all these fixed while `y` tends to infinity. Since `N>=d_y`, the last error is uniform in `m`. This proves
\[
\limsup_{y\to\infty}\sup_{m\ge1}\|T\|\le\beta_\infty.
\tag{20}
\]

For the lower bound, fix any finite admissible `F`. At each prime `p<=y`, there is a translate residue avoiding `-F mod p`. CRT therefore gives at least one translation of `F` inside `Y`, for every `m`, once its distinct offsets remain distinct modulo `N`. In fact the exact number is
\[
\#\{b\bmod N:b+F\subset Y\}
=m\prod_{p\le y}(p-|F\bmod p|)>0.
\tag{21}
\]
The corresponding principal cotangent block converges to `L_F`, uniformly in `m`, by the same finite-displacement estimate. Hermitian compression yields
\[
\liminf_{y\to\infty}\inf_{m\ge1}\|T\|\ge\|L_F\|.
\]
Taking the supremum over fixed `F` proves (3) for `T`. Taking the limit in (19) now also proves (5).

Complex conjugation sends `T` to `-T`, so its extreme eigenvalues are exactly `+||T||` and `-||T||`. Finally,
\[
\|T^+-T\|=|Y|/N=\varphi(d_y)/d_y\longrightarrow0
\tag{22}
\]
uniformly in `m`. Hermitian eigenvalue perturbation proves the norm and both extreme-eigenvalue assertions for the augmentation. Rank one alone would not suffice for this step; its vanishing **norm** is used.

## 5a. Exact refinement norms and monotone periodic upper certificates

For any integer `q>=2`, write `U(q)={a mod q:(a,q)=1}` and define the **unscaled** base matrices
\[
(H_q)_{ab}=i\cot\frac{\pi(a-b)}q\quad(a\ne b),
\qquad (H_q)_{aa}=0,\qquad A_q=H_q+J_{\varphi(q)},
\]
\[
a_q=\lambda_{\max}(A_q),\qquad
c_q=a_q/q,\qquad h_q=\|H_q\|/q.
\tag{23}
\]
Let `T_(q,m)` and `T^+_(q,m)` mean (1) with `d_y` replaced by `q` and `N=qm`. Then, for every `m>=1`,
\[
\boxed{\quad
\|T^+_{q,m}\|=c_q,\qquad
\|T_{q,m}\|=\max\{h_q,c_q-2/(qm)\},\qquad
0\le c_q-\|T_{q,m}\|\le 2/(qm).
\quad}
\tag{24}
\]
The exact augmented extreme eigenvalues are `c_q` and `-c_q+2/(qm)`; the raw extremes are plus and minus the second expression in (24).

To prove this, first take **any nonempty finite set of distinct circle points** with arguments `theta_a mod 1`. Define `H` by the same zero-diagonal cotangent kernel, `A=H+J`, and `D=diag(exp(2 pi i theta_a))`. Entrywise,
\[
e^{2i\theta}(1+i\cot\theta)=-1+i\cot\theta,
\qquad
DAD^*=2I-\overline A.
\tag{25}
\]
The diagonal also agrees because the augmentation includes it. This is the phase identity used in [[research/prime_circle/findings/PC-448-haar-admixture-does-not-close-rigid-cotangent-towers]], now applied to the finite spectral edges. Since `A` is Hermitian, (25) makes its spectrum symmetric about **one**. If `a=lambda_max(A)`, then `lambda_min(A)=2-a`, `a>=1`, and `||A||=a`. Complex conjugation sends `H` to `-H`, while `A-H=J>=0`. Comparing both extreme eigenvalues therefore gives
\[
\|H\|\le a\le\|H\|+2.
\tag{26}
\]
This is a bound on the change of the extreme eigenvalues, not the false assertion `||J||<=2`.

The exact fiber Fourier transform of [[research/prime_circle/findings/PC-053-composite-cotangent-preimage-tubes-are-affine-base-inflations]], §§3--4, gives augmented eigenvalues
\[
\frac{\lambda_\alpha(A_q)-2j/m}{q},
\qquad 0\le j<m.
\tag{27}
\]
The largest is `c_q`, attained at `j=0`, and the smallest is `-c_q+2/(qm)`, attained at `j=m-1`. For the raw matrix, replace just the `j=0` block by `H_q/q`. When `m>=2`, the remaining blocks have extreme eigenvalues exactly `+/- (c_q-2/(qm))`. This proves (24) in that case. For `m=1`, (26) gives `c_q-2/q<=h_q`, so the same maximum formula reduces correctly to `h_q`. No small-density or large-refinement limit is used.

The values `c_q` obey the exact divisibility rules
\[
q\mid r\ \Longrightarrow\ c_r\le c_q,
\qquad
c_{qp}=c_q\ (p\mid q),
\qquad
c_{qp}<c_q\ (p\nmid q),
\tag{28}
\]
where `p` is prime. Indeed `A_r/r` is a principal compression of the augmented complete `r/q`-fold tube above `U(q)`, whose norm and top eigenvalue are `c_q` by (24). If `p|q`, the primitive support at `qp` is the entire `p`-fold tube, giving equality.

For strictness when `p` is new, the top eigenspace of the augmented `p`-fold tube lies entirely in its constant fiber Fourier sector: every `j>0` block in (27) has top eigenvalue strictly below `c_q`. A vector in this top eigenspace is constant on the `p` lifts of each base point. Exactly one lift of every base residue is divisible by `p` and is deleted in the compression to `U(qp)`. No nonzero top eigenvector can therefore be supported on the retained coordinates. Equality in the Hermitian compression bound would produce just such an eigenvector by extending a maximizing vector by zero. This contradiction proves strictness without assuming that the base top eigenvalue is simple or that its eigenvectors have no zero coordinates.

For primorial moduli, (3), (24) and (28) now imply
\[
\boxed{\quad
c_{d_y}\downarrow\beta_\infty,
\qquad
\beta_\infty<c_q\quad\text{for every fixed primorial }q.
\quad}
\tag{29}
\]
The strict inequality follows by adjoining one more prime and then taking the decreasing limit. More directly, if `q=d_z`, then for every `y>=z` and every refinement `m`, both matrices in (1) are principal compressions of the corresponding `N/q`-fold complete tube over `U(q)`. Thus
\[
\|T^{(+)}\|\le c_q
\quad(y\ge z, m\ge1).
\tag{30}
\]
This is a finite-conductor upper certificate, not merely an eventual asymptotic bound. Equations (29)--(30) use the norm limit already proved in §§2--5 to identify the infimum; divisibility monotonicity alone would not identify it with the admissible-constellation supremum.

For example, on `U(6)={1,5}`,
\[
A_6=\begin{pmatrix}
1&1+i/\sqrt3\\1-i/\sqrt3&1
\end{pmatrix},
\qquad
c_6=\frac{1+2/\sqrt3}{6}.
\]
Consequently
\[
\boxed{\qquad
\beta_\infty<\frac{1+2/\sqrt3}{6}<\frac12.
\qquad}
\tag{31}
\]
The non-strict bound by `c_6` holds for every finite admissible `L_F` as well: CRT translates `F` into the unit residues modulo `6`, embed that fixed translate in a sufficiently large complete tube, and pass its principal block to the Cauchy limit. Only the exclusions modulo two and three are needed for this bound. Strictness for the full edge uses the next sieve step as in (29), not an unsupported inference from strict bounds on each individual finite shape.

Together, `M_L<=beta_infinity<c_q`, `M_L` increasing to the edge, and (29) give lower and upper certificates that converge from opposite sides. The upper side requires one primitive-shell eigenvalue rather than enumeration of every admissible window subset. Its matrix dimension still grows as `varphi(q)`; no efficient convergence rate or certified decimal value of the edge is asserted. The phase symmetry, exact refinement norms and compression mechanism hold for arbitrary finite base masks. Arithmetic enters the nested unit supports and their identification with all admissible local shapes.

## 6. Mathematical delta, controls and boundaries

PC-463 gives an exact hierarchy of fixed-cardinality populations but explicitly does not interchange constellation size with the conductor limit. Equations (7), (13) and (17) provide that missing uniform control at the level of the extreme norm. There is no need to sum the singular-series population hierarchy or assume any prime-tuple conjecture. For each fixed accuracy, one fixed finite window captures the edge across every sufficiently sieved conductor and every complete refinement.

This is a limit of **numbers**, not convergence of the full operators to a single finite or compact operator in a chosen embedding. It is consistent with the escaping spatial sectors and failure of the anchor/antipodal norm limits in [[research/prime_circle/findings/PC-459-primorial-cotangent-local-limits-split-into-anchor-pair-and-antipodal-dyadic-kernel]]. Section 5a rules out saturation of the earlier parity-only ceiling `1/2`, makes the finite upper certificates monotone, and shows that complete refinement changes the raw edge by at most `2/N` from the augmented edge. It does not determine the exact `beta_infinity`, assert a rate in `y`, identify its maximizing infinite configuration, or extend the fixed-size counting laws to thresholds moving with `y`.

The deterministic mechanism has matched controls: (6)--(17) hold for arbitrary periodic masks and all their subsets, with `|A|/q` replacing the totient density. The arithmetic part is exactly the sieve containment, admissibility of bounded windows and CRT occurrence of every finite admissible shape. A different support with these same properties has the same edge; vanishing cardinality density alone is insufficient. The edge still retains extremal constellation information, so it has not been proved prime-blind by comparing supports that already match that information.

The result closes the previously unresolved possibility of eigenvalues staying a fixed positive distance above **all** finite admissible-constellation norms. It leaves the edge's value and any genuinely different source-forced coupling as separate questions. There is no connection here between this real norm limit and zeta-zero locations, no zero-exclusion estimate, and no new RH criterion.

## 7. Prior art and validation

- Fejer positivity, approximate identities and trigonometric approximation are classical. D. Potts, *Numerical Fourier Analysis: Theory and Applications*, [lecture notes based on Plonka--Potts--Steidl--Tasche, Example 19 and Theorem 20](https://www-user.tu-chemnitz.de/~potts/paper/slidesI.pdf), gives the standard kernel framework. The necessary away-from-jump estimate is derived explicitly in (12); no continuous-function theorem is applied across the sawtooth jump.
- X. Chen, R. Tessera, X. Wang and G. Yu, *Metric sparsification and operator norm localization*, **Advances in Mathematics 218** (2008), 1496--1511, [DOI](https://doi.org/10.1016/j.aim.2008.03.016), [author manuscript](https://arxiv.org/abs/0711.2093), supplies the established general context for recovering norms from bounded supports. The special cyclic-window estimate (16) is proved directly. That general theory does not by itself give the sieve-dependent finite-range approximation (13) for this discontinuous Fourier symbol.
- J. C. Lagarias, [*Euler's constant: Euler's work and modern developments*, Theorem 3.3.2](https://arxiv.org/pdf/1303.1856), records Mertens's product theorem. Only the consequence `varphi(d_z)/d_z -> 0` is needed, not a sharp error term.
- The different cross-scale cotangent Gram/determinant RH criteria of Lewis--Zagier, [*Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis*](https://doi.org/10.1007/s40687-018-0159-8), do not identify the compressed finite-polygon norm studied here. Their existence prevents extending this result to a blanket exclusion of cotangent RH mechanisms.
- W. Ejsmont and F. Lehner, *The Trace Method for Cotangent Sums*, **J. Combinatorial Theory A 177** (2021), 105324, [author manuscript, §2](https://arxiv.org/pdf/2002.06052), studies finite self-adjoint matrices realizing cotangent values as eigenvalues. This is neighboring finite spectral theory, not the same primitive-shell matrix or a source of the monotone primorial certificates. Section 5a is a derived consequence of the existing PC-053 Fourier blocks, PC-448 phase identity and Hermitian compression, combined with the norm limit proved here; no new general spectral theorem is claimed.

The local duplication check covered PC-457--PC-463 and searched the local growing-operator findings for norm limits, Fourier-band compression and finite-range localization. The new result is the full primorial extreme-norm limit and its finite-window certificate; Fejer smoothing, Fourier alias orthogonality, norm localization and CRT are classical ingredients. Targeted external searches for sieved discrete Hilbert/cotangent spectra and admissible-constellation edges did not establish historical priority.

The proof is analytic and has not been Lean-verified or independently adversarially approved. A deterministic standard-library Python audit using system LAPACK `zheev` through `ctypes` checked:

- **40** periodic Fourier-projection identities, for primorial and nonarithmetic masks, with maximum entry residual below `7e-14`; a wider-band control has a nonzero `1/6` off-diagonal entry;
- **48** compressed smoothing bounds and **35** cyclic-window norm bounds, with maximum ratios to their respective bounds below `0.245` and `0.218`;
- **480** finite cotangent-to-Cauchy block error bounds, with maximum ratio below `0.194`;
- **9,828** cyclic windows for local admissibility and **45** exact CRT occurrence counts;
- **8** complete raw/augmented spectra through dimension `480`, checking sign symmetry and the vanishing-density perturbation bound.

These are finite sign, normalization, wraparound and inequality checks, not proofs of (3) or a numerical determination of the edge. Scratch code and output remain outside Git. The decisive analytic audit points are the strict Fourier arc width, periodic containment before taking density small, both uses of (13) in (17), admissibility only after `y>=L`, and fixing the entire finite-window certificate before the conductor limit.

An additional standard-library Python/LAPACK audit of §5a checked **70** finite point sets, including irrational-angle and singleton controls: (25), spectral reflection about one and (26) had maximum identity residual below `2.9e-14`. On **104** complete tubes from primitive and arbitrary masks, through dimension `240`, direct diagonalization verified (27) and both exact norms in (24), with maximum residual below `1.6e-15`. It checked **37** prime-power equalities, **67** strict new-prime decreases, and the modulo-six bound on **366** admissible Cauchy shapes of sizes two through six. These diagnostics do not replace the proofs or certify the asymptotic edge numerically. Local deduplication checked the finite affine-spectrum and phase-identity findings as well as the current edge/population results; the certificate is integrated into this same edge claim rather than promoted as an independent mechanism. The extra audit points are the included augmented diagonal, using both extreme eigenvalues in (26), the `m=1` case, and the equality condition for compression in the strict-decrease proof.
