# VIS-224 — midpoint-symmetric taper worst starts are constant-factor equivalent to an Ising sign problem

## Claim

Keep the midpoint-symmetric real-taper setup of `VIS-223`. For fixed `(y,H)`, diagonal switching gives

`A_(y,H)=D_H^* B_(y,H) D_H`

with `B_(y,H)` real symmetric and zero diagonal. Define the binary sign objective

`I_abs(B)=max_(epsilon_i in {+1,-1}) |epsilon^T B epsilon|`.

Let

`M_abs(A)=max_(|z_i|=1)|z^*Az|`

be the exact unit-modulus torus objective from `VIS-213`, and let

`U_abs^R(B)=max_(X in E_n^R)|Tr(BX)|`,

`E_n^R={X in R^(n x n): X=X^T, X>=0, diag(X)=1}`,

be the real-elliptope objective identified in `VIS-223`.

Then for every finite midpoint-symmetric instance,

`I_abs(B) <= M_abs(A) <= U_abs^R(B) <= K_gamma^R I_abs(B)`,

where `K_gamma^R` is the real symmetric Grothendieck constant of Friedland--Lim. Their explicit bound gives

`K_gamma^R <= sqrt(2)(8/pi-1) < 2.188`.

Hence the binary Ising sign optimum, the exact continuous-phase prime-torus optimum, and the full real correlation SDP are all equivalent in objective scale up to a universal factor independent of the number of primes and of `(y,H)`.

For the canonical worst-start statistic,

`sup_T |M_v(y;H,T)-1|=M_abs(A_(y,H))`,

so

`I_abs(B_(y,H))`
` <= sup_T |M_v(y;H,T)-1|`
` <= K_gamma^R I_abs(B_(y,H))`.

After division by the exact Haar scale `sqrt(R_v(y,H))`, boundedness or divergence of the normalized worst-start amplitude is therefore **equivalent** to boundedness or divergence of the normalized binary sign optimum.

This is not an exact reduction of the torus optimizer to signs. Continuous phases can improve the finite optimum, but by at most the universal real symmetric-Grothendieck factor.

**Evidence/status:** `LITERATURE+DERIVED + REAL-SYMMETRIC-GROTHENDIECK SPECIALIZATION + CONSTANT-FACTOR ISING/TORUS/SDP EQUIVALENCE + REPRESENTATION REDUCTION + NO-NOVELTY-CLAIM`.

No prime-specific asymptotic estimate, exact Ising optimizer, improvement of a Grothendieck constant, polynomial-time exact algorithm, access-time theorem, or RH consequence is claimed.

## 1. The midpoint gauge leaves a real coefficient matrix

`VIS-223` proves that a midpoint-symmetric real taper has

`kappa_v(u)=exp(iu/2) r_v(u)`,

with `r_v(u)` real and even. The phase `exp(iu/2)` is a vertex coboundary, hence

`A=D_H^* B D_H`

for a real symmetric `B`.

Diagonal unitary switching preserves the unit-modulus torus, so

`M_abs(A)=M_abs(B)`.

The same finding proves that the complex correlation SDP collapses exactly to the real elliptope:

`U_abs(A)=U_abs^R(B)`.

Thus the remaining difference between the exact prime-torus problem and a binary sign problem is no longer a coefficient-field issue. It is only the difference between allowing each vertex to choose an arbitrary phase on the unit circle and restricting it to the two real phases `0,pi`.

## 2. Real symmetric Grothendieck compares the elliptope directly with signs

For a real symmetric matrix `B`, Friedland and Lim's real symmetric Grothendieck seminorms specialize to

`||B||_gamma^R`
` = max_(||x_i||=1) |sum_(i,j) B_ij <x_i,x_j>|`
` = U_abs^R(B)`

and

`||B||_theta^R`
` = max_(epsilon_i in {+1,-1}) |sum_(i,j) B_ij epsilon_i epsilon_j|`
` = I_abs(B)`.

The first equality follows because real unit-vector Gram matrices are exactly the real correlation matrices `E_n^R`. In one real dimension the only unit scalars are `+1` and `-1`, giving the second equality.

The real symmetric Grothendieck inequality therefore gives

`U_abs^R(B) <= K_gamma^R I_abs(B)`.

Friedland--Lim give the explicit universal estimate

`K_gamma^R <= sqrt(2)(8/pi-1)`,

which is below `2.188`.

The opposite inclusion is immediate: every sign vector is a legal torus vector and every rank-one sign matrix `epsilon epsilon^T` is a legal real correlation matrix. Hence

`I_abs(B)<=M_abs(B)<=U_abs^R(B)`.

Combining these inequalities proves the full chain.

## 3. The binary problem already determines the RMS-normalized asymptotic scale

Let

`Q(y,H)=I_abs(B_(y,H))/sqrt(R_v(y,H))`,

`W(y,H)=M_abs(A_(y,H))/sqrt(R_v(y,H))`.

The pointwise comparison is

`Q(y,H) <= W(y,H) <= K_gamma^R Q(y,H)`.

Because the constant is universal, it survives arbitrary growing parameter regimes. Consequently

`Q=O(1)` if and only if `W=O(1)`,

and

`Q -> infinity` if and only if `W -> infinity`.

The same statement holds for the real SDP ratio because it lies between `W` and `K_gamma^R Q`.

This changes the live static question from `VIS-221`--`VIS-223`. To decide only whether the worst-start amplitude remains on Haar-RMS scale or escapes it by a divergent factor, one does **not** need to solve the continuous `U(1)` torus optimization or characterize high-rank elliptope optimizers. It suffices, up to a fixed factor, to estimate the signed quadratic form on the hypercube.

## 4. Quadratic taper: a concrete signed-shell Ising Hamiltonian

For the canonical quadratic taper `w(x)=6x(1-x)`, `VIS-223` gives

`B_(p,q)=Q_y^(-1) p^(-alpha)q^(-alpha) r_w(H log(q/p))`,

with

`r_w(u)=12[2 sin(u/2)-u cos(u/2)]/u^3`.

Therefore the binary proxy is the explicit weighted Ising Hamiltonian

`I_abs(B)`
` = max_(epsilon_p in {+1,-1})`
`   |sum_(p!=q) Q_y^(-1) p^(-alpha)q^(-alpha)`
`      r_w(H log(q/p)) epsilon_p epsilon_q|`.

The sign of every coupling is determined by the deterministic ratio shells cut out by the roots of

`tan(u/2)=u/2`.

This representation preserves exactly the centered coefficient signs and magnitudes. It is therefore better matched to the symmetric-taper branch than a control that injects independent continuous edge phases.

The reduction does not say that this Ising problem is easy. It may still contain extensive frustration and its prime-specific optimum may remain analytically difficult. What it removes is the need to attribute the coarse asymptotic scale to genuinely continuous vertex phases.

## 5. Prior art and novelty boundary

The decisive external input is Shmuel Friedland and Lek-Heng Lim, **Symmetric Grothendieck inequality**, arXiv:2003.07345 (2020). Their real symmetric inequality compares the real `gamma` and `theta` seminorms for arbitrary real symmetric matrices, and Corollary 4.6 gives

`K_gamma^R <= sqrt(2)(8/pi-1)`.

`VIS-222` already uses the complex version of the same theory to compare the full complex correlation SDP with the unit-modulus torus optimum. The present finding uses the additional real structure proved in `VIS-223`: once the objective matrix is real and the SDP has collapsed to the real elliptope, the real `theta` seminorm is a binary sign quadratic form.

No novelty is claimed for the symmetric Grothendieck theorem, its real constant bound, Gram representations of the elliptope, or Ising quadratic optimization. The Mathia-specific content is the exact chain from midpoint symmetry of the observation taper to a real signed prime matrix and then to the constant-factor binary proxy for the original worst-start statistic.

## Boundaries and falsification

The result requires the midpoint-symmetric real-taper reduction of `VIS-223`. For an asymmetric taper, the centered odd part can leave genuine complex edge phases and the real sign comparison does not apply directly.

The factor is multiplicative, not additive, and does not identify the exact optimizer. A continuous torus phase assignment can outperform every binary sign assignment at finite dimension. The theorem says only that the improvement is universally bounded.

The result also does not address the time required for the one-parameter prime-log orbit to approach a near-optimal torus point. `VIS-213`'s density identity concerns the supremum, not quantitative recurrence.

Falsify this finding by locating a mismatch between `E_n^R` and the real `gamma` seminorm, between the sign hypercube and the real `theta` seminorm, an invalid use of the real symmetric Grothendieck inequality for indefinite `B`, or an error in the midpoint gauge/real-elliptope reduction of `VIS-223`.

## Research consequence

The accepted clue `CLUE-prime-phase-sdp-rms-tightness` remains open at the arithmetic-estimate level, but its decisive object can now be simplified. For midpoint-symmetric tapers, determine the asymptotic scale of

`I_abs(B_(y,H))/sqrt(R_v(y,H))`.

A bounded ratio implies Haar-RMS-scale worst starts; a divergent ratio forces a divergent worst-start/RMS ratio. The full real SDP remains a useful convex upper proxy and exact stress certificates remain useful for finite optimizer recovery, but neither is necessary merely to decide the bounded-versus-divergent asymptotic scale.