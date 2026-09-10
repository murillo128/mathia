# PF-276 — Robin normalization is inverse-positive and cannot zero the fixed-axis threshold moment

**Status:** `EXACT-DERIVED + STIELTJES-MATRIX-NORMALIZATION + POSITIVITY-IMPROVING-INVERSE + ZERO-MODE-MOMENT-NONCANCELLATION + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-273-seam-square-root-is-a-complete-bernstein-green-continuum-with-mass-one-edge|PF-273]] and [[research/prime_flute/findings/PF-275-mass-one-continuum-forbids-supercritical-raw-source-fixed-row-leakage|PF-275]] show that the raw square-root source reaches the critical Green mass `mu=1` and has no supercritical fixed-row leakage exponent. [[research/prime_flute/findings/PF-274-fixed-axis-massive-jacobi-chain-is-a-squared-continuous-hahn-operator|PF-274]] therefore isolates the only remaining fixed-axis escape: the noncommuting Robin factor could in principle modify the source vector so that its coefficient at the nearest continuous-Hahn branch points `xi=±i` vanishes.

That escape is much narrower than it looked. In each PF parity chain the finite-seam relative operator

\[
\mathcal R^0_{s,r}=s^{-1}A^{-1/4}f_w(L)A^{-1/4},
\qquad
f_w(\lambda)=\sqrt\lambda\tanh(w\sqrt\lambda),
\qquad w=rs,
\]

is a positive self-adjoint **Z-operator** in the corridor basis: every distinct same-parity matrix entry is strictly negative. Consequently `I+\mathcal R^0_{s,r}` is the infinite-dimensional analogue of a Stieltjes matrix, and its inverse preserves and improves the coefficientwise positive cone.

More importantly, the exact PF-251 zero mode supplies a positive generalized harmonic weight for `\mathcal R^0_{s,r}`. This yields a conserved weighted mass for the normalized source column. The special vector entering the adjoint Robin source therefore has a finite, strictly positive pairing with that zero mode. Under PF-274's Fourier/continuous-Hahn dictionary, the corresponding absolutely convergent corridor-coefficient functional is nonzero at both nearest points `xi=±i`, with the fixed parity sign.

Thus **ordinary coefficient cancellation inside the Robin normalization cannot create the threshold zero requested by the accepted clue**. The unresolved step is now analytic/asymptotic rather than algebraic: one must show that this nonzero threshold functional is the coefficient consumed by the Darboux/Green large-mode law for `g_w(L)z_i`, or identify a genuinely different nonlocal cancellation mechanism. PF-276 does not yet claim the final `N^{-1}`-type lower bound for the normalized operator.

## Claim

Fix `r,s>0`, put `w=rs`, and work in one parity sector `\varepsilon\in\{0,1\}`. Write

\[
\varphi_j=e_{2j+\varepsilon},
\qquad
\kappa_j=2j+\varepsilon+\alpha,
\qquad
D=A^{-1/4},
\qquad
D\varphi_j=\kappa_j^{-1/2}\varphi_j,
\tag{1}
\]

where `\alpha=(1+\sqrt5)/2`. Define

\[
R:=\mathcal R^{0,\varepsilon}_{s,r}
=s^{-1}D f_w(L)D,
\qquad
M:=I+R,
\tag{2}
\]

and, for a fixed basis source `i`,

\[
u^{(i)}:=M^{-1}\varphi_i,
\qquad
z^{(i)}:=Du^{(i)}.
\tag{3}
\]

Then:

1. `R\ge0`, and for all `j\ne k` in the parity chain,
   \[
   \boxed{R_{jk}<0.}
   \tag{4}
   \]
2. `M^{-1}` preserves the coefficientwise nonnegative cone. Since (4) is strict,
   \[
   \boxed{u_j^{(i)}>0\quad\text{for every }j.}
   \tag{5}
   \]
3. let `v_\varepsilon` be PF-251's exact parity-zero mode of `L`, and put
   \[
   c_j:=\langle\varphi_j,v_\varepsilon\rangle>0,
   \qquad
   q_j:=\kappa_j^{1/2}c_j.
   \tag{6}
   \]
   Then `c_j\asymp j^{1/2}`, `q_j\asymp j`, and the finite-seam relative operator annihilates this generalized weight in the exact coordinatewise sense
   \[
   \boxed{Rq=0.}
   \tag{7}
   \]
4. the normalized column has the exact weighted conservation law
   \[
   \boxed{
   \sum_{j=0}^{\infty}q_j u_j^{(i)}=q_i.
   }
   \tag{8}
   \]
   In particular `u^(i)` is absolutely summable and has a finite first moment;
5. the threshold zero-mode moment of the vector in the adjoint source,
   \[
   \boxed{
   T_i^{(\varepsilon)}
   :=\sum_{j=0}^{\infty}c_j z_j^{(i)}
   =\sum_{j=0}^{\infty}\frac{q_j}{\kappa_j}u_j^{(i)},
   }
   \tag{9}
   \]
   converges absolutely and satisfies
   \[
   \boxed{0<T_i^{(\varepsilon)}<\infty.}
   \tag{10}
   \]
6. if `\psi_n=U^*e_n` is PF-274's complete-axis corridor basis and
   \[
   \widehat\psi_n(\xi)=\int_{\mathbb R}e^{-i\xi\tau}\psi_n(\tau)\,d\tau,
   \tag{11}
   \]
   then the absolutely convergent corridor-coefficient threshold sums obey
   \[
   \boxed{
   \sum_{j\ge0}z_j^{(i)}\widehat\psi_{2j+\varepsilon}(-i)
   =T_i^{(\varepsilon)},
   }
   \tag{12}
   \]
   and
   \[
   \boxed{
   \sum_{j\ge0}z_j^{(i)}\widehat\psi_{2j+\varepsilon}(i)
   =(-1)^\varepsilon T_i^{(\varepsilon)}.
   }
   \tag{13}
   \]
   Hence neither nearest branch-point coefficient functional vanishes.

For the physical fixed-axis injection

\[
B_w=(I+R)^{-1}X_w,
\qquad
X_w=s^{-1/2}Dg_w(L),
\qquad
g_w=f_w^{1/2},
\tag{14}
\]

PF-257 gives

\[
B_w^*\varphi_i=s^{-1/2}g_w(L)z^{(i)}.
\tag{15}
\]

Equations (10)--(13) rule out an exact threshold zero produced by sign cancellation in the normalized source vector. They do **not** by themselves prove that the square-root branch of `g_w(1+\xi^2)` yields the sharp leading large-mode asymptotic of (15); that final transfer remains the decisive fixed-axis gate.

## 1. The finite seam is a Stieltjes-type matrix in each parity cone

PF-261 gives the exact positive mass expansion

\[
R
=\frac{2}{rs^2}\sum_{k\ge0}
D\,L(L+a_k^2)^{-1}D,
\qquad
a_k=\frac{(2k+1)\pi}{2rs}.
\tag{16}
\]

For distinct same-parity indices, the identity part of

\[
L(L+a^2)^{-1}=I-a^2(L+a^2)^{-1}
\tag{17}
\]

drops out. PF-267 proves that every below-spectrum Green entry of `(L+a^2)^{-1}` is strictly positive in the PF parity gauge. Therefore

\[
R_{jk}
=-\frac{2}{rs^2\sqrt{\kappa_j\kappa_k}}
\sum_{m\ge0}a_m^2
\langle\varphi_j,(L+a_m^2)^{-1}\varphi_k\rangle<0
\quad(j\ne k),
\tag{18}
\]

while PF-261 already proves `R\ge0`. Thus `M=I+R\ge I` is positive definite with nonpositive off-diagonal matrix entries.

In finite dimensions this is exactly a Stieltjes matrix / symmetric nonsingular M-matrix. Inverse positivity of that class is classical. Here the complete-lift cone statement follows directly. Let `y\ge0` and `x=M^{-1}y`. Write the coefficientwise positive/negative parts as `x=x_+-x_-`. Their supports are disjoint. Finite-support approximation and (18) give

\[
\langle Mx_+,x_-\rangle
=\langle Rx_+,x_-\rangle\le0,
\tag{19}
\]

while

\[
\langle Mx_-,x_-\rangle\ge\|x_-\|^2.
\tag{20}
\]

If `x_-` were nonzero, then

\[
0\le\langle y,x_-\rangle
=\langle Mx_+,x_-\rangle-\langle Mx_-,x_-\rangle<0,
\tag{21}
\]

a contradiction. Hence `M^{-1}` is positivity preserving.

For `y=\varphi_i`, equation `Mu=\varphi_i` first forces `u_i>0`: if `u_i=0`, its `i`-th row would have right side at most zero because all other coefficients are nonnegative and every off-diagonal entry is negative. Once `u_i>0`, the same row argument at any `j\ne i` shows `u_j` cannot vanish because the term `R_{ji}u_i` is strictly negative. This proves (5).

## 2. The exact zero mode becomes a generalized harmonic weight for the relative seam

PF-251 constructs exact zero solutions `v_\varepsilon` of `L` and proves that their parity coefficients

\[
c_j=\langle\varphi_j,v_\varepsilon\rangle
\tag{22}
\]

are strictly positive and satisfy `c_j\asymp j^{1/2}`. Since `Dq=c` for the definition (6), equation (7) reduces to showing that each term in PF-261's massive representation kills `c` after the factor `L`.

Fix `a>0`, let `G_a=(L+a^2)^{-1}`, and define coordinatewise

\[
y_j:=\sum_{k\ge0}(G_a)_{jk}c_k.
\tag{23}
\]

PF-262's fixed-source tail and PF-264's two-index Green law make this series absolutely convergent. Splitting at `k=j` gives

\[
y_j=O_a(j^{1/2}).
\tag{24}
\]

Indeed the moving part has the profile `j^{-1/2+\mu}k^{-1/2-\mu}` for `j\le k` and its symmetric counterpart for `k\le j`, with `\mu=\sqrt{1+a^2}>1`, while `c_k\asymp k^{1/2}`.

Because each Jacobi row of `L` is finite, `(L+a^2)y=c` follows coordinatewise from the Green identity. But `a^{-2}c` is another solution because `Lc=0`. Their difference is a homogeneous solution of `(L+a^2)d=0` satisfying the same left boundary row and growing at most like `j^{1/2}`. PF-262--PF-264 show that any nonzero left-regular homogeneous solution at the resolvent point `-a^2` has dominant behavior

\[
j^{-1/2+\mu},
\qquad\mu>1,
\tag{25}
\]

which grows strictly faster than `j^{1/2}`. Hence the difference vanishes and

\[
\boxed{(L+a^2)^{-1}c=a^{-2}c.}
\tag{26}
\]

Therefore every fixed-mass term in (16) annihilates `q`:

\[
D L(L+a^2)^{-1}Dq
=D L(L+a^2)^{-1}c=0.
\tag{27}
\]

There is no hidden interchange of a conditionally convergent mass sum here. For each fixed mass, the off-diagonal row is negative and (26)--(27) give

\[
\sum_{k\ne j}q_k\bigl|[D L(L+a^2)^{-1}D]_{jk}\bigr|
=[D L(L+a^2)^{-1}D]_{jj}q_j.
\tag{28}
\]

The masses in (16) have positive coefficients, so Tonelli and monotone convergence of the positive diagonal series imply

\[
\sum_{k\ne j}q_k|R_{jk}|=R_{jj}q_j<\infty.
\tag{29}
\]

Thus the full weighted row is absolutely summable and the masswise identities can be summed safely, proving `Rq=0` coordinatewise. Including the diagonal gives the useful identity

\[
\boxed{
\sum_kq_k|R_{jk}|=2R_{jj}q_j\le2\|R\|q_j.
}
\tag{30}
\]

Finally `q_j=\kappa_j^{1/2}c_j\asymp j` follows from PF-251.

## 3. Galerkin comparison gives a conserved weighted mass

The generalized vector `q` is not in `\ell^2`, so (8) should not be obtained by a formal Hilbert-space pairing. Use finite sections first.

Let `P_N` project onto `\varphi_0,\dots,\varphi_N`, let

\[
M_N=P_NMP_N,
\qquad q^{(N)}=P_Nq,
\qquad
u^{(N)}=M_N^{-1}\varphi_i
\quad(N\ge i).
\tag{31}
\]

Each `M_N` is a finite Stieltjes matrix, so `M_N^{-1}` is entrywise nonnegative. The absolutely convergent identity `Mq=q` from (29) and the nonpositive omitted couplings give

\[
M_Nq^{(N)}
=q^{(N)}-P_NR(I-P_N)q
\ge q^{(N)}.
\tag{32}
\]

Applying the positive inverse and using symmetry gives

\[
\sum_{j=0}^Nq_j u_j^{(N)}
=\langle M_N^{-1}q^{(N)},\varphi_i\rangle
\le q_i.
\tag{33}
\]

Because `M\ge I` is bounded and coercive, the Galerkin solutions converge strongly to `u=M^{-1}\varphi_i` as the increasing coordinate subspaces exhaust `\ell^2`. Passing first on each fixed prefix and then increasing the prefix yields

\[
\sum_{j\ge0}q_j u_j\le q_i<\infty.
\tag{34}
\]

The inequality is actually an equality. Equation (30) and (34) make the double series obtained by pairing `Mu=\varphi_i` with `q` absolutely convergent:

\[
\sum_{j,k}q_j|R_{jk}|u_k
=\sum_k u_k\sum_jq_j|R_{jk}|
\le2\|R\|\sum_kq_ku_k<\infty.
\tag{35}
\]

Fubini is therefore legitimate. Symmetry and `Rq=0` cancel the `R` term, giving

\[
q_i
=\sum_jq_j(Mu)_j
=\sum_jq_ju_j,
\tag{36}
\]

which is (8). The Robin normalization redistributes the positive source mass but cannot remove it in the generalized zero-mode weight selected by the finite-seam operator.

## 4. The normalized source has a finite nonzero threshold coefficient functional

Since `z_j=\kappa_j^{-1/2}u_j` and `q_j=\kappa_j^{1/2}c_j`, equation (9) is immediate:

\[
c_jz_j=\frac{q_j}{\kappa_j}u_j.
\tag{37}
\]

All summands are positive. Equation (8) and `\kappa_j\ge\alpha>0` give absolute convergence, while the `j=i` term is strictly positive by (5). Thus (10) follows.

There is a useful probabilistic normalization. Define

\[
\pi_j^{(i)}:=\frac{q_ju_j^{(i)}}{q_i}.
\tag{38}
\]

Then (5) and (8) make `\pi^(i)` a strictly positive probability distribution and

\[
\boxed{
T_i^{(\varepsilon)}
=q_i\sum_{j\ge0}\frac{\pi_j^{(i)}}{\kappa_j}.
}
\tag{39}
\]

So the threshold moment is a positive weighted average, not a difference of competing phases.

PF-274 makes the coefficient-functional meaning explicit. With `\tau=\log\tan(\theta/2)`,

\[
Ue^\tau=v_0-v_1,
\qquad
Ue^{-\tau}=v_0+v_1.
\tag{40}
\]

Hence, directly from the Fourier definition,

\[
\widehat\psi_{2j+\varepsilon}(-i)=c_j,
\qquad
\widehat\psi_{2j+\varepsilon}(i)=(-1)^\varepsilon c_j.
\tag{41}
\]

The absolute convergence already proved in (9) permits termwise evaluation of these corridor-coefficient threshold sums and gives (12)--(13). They are precisely the two points where PF-274 finds the nearest square-root branch of

\[
g_w(1+\xi^2)
=\sqrt w\,(1+\xi^2)^{1/2}(1+O(1+\xi^2)).
\tag{42}
\]

Thus the normalization does not manufacture an algebraic zero by changing signs of the corridor coefficients. The special source vector has a nonzero zero-mode coefficient functional at both nearest branch points.

## 5. Consequence for the accepted Robin-source clue

The accepted clue `CLUE-robin-homotopy-separated-poisson-shear-estimate` had two candidate outcomes after PF-275: either the normalized vector `z_i` acquires a threshold zero, or the mass-one obstruction survives normalization.

PF-276 rules out the most direct form of the first option. The operator `(I+R)^{-1}` is not merely bounded; it is positivity improving in the exact PF corridor cone, and its normalized column obeys the positive conservation law (8). The zero-mode/branch-point coefficient functional (9) is therefore strictly nonzero.

What remains is one precise analytic bridge. One must prove that the large-mode coefficient of

\[
g_w(L)z^{(i)}
\tag{43}
\]

is controlled by the nonzero functional (12)--(13) with the expected mass-one power, uniformly enough to give a fixed-row lower bound. PF-274 explicitly warned that branch-point distance alone is not an asymptotic theorem, so PF-276 does not silently promote (42) to a Darboux result.

If that bridge is established, the normalized fixed-axis injection fails every supercritical PF-271 exponent and this route closes before shear/corridor uniformity. If instead (43) gains a strict exponent despite (12)--(13), the mechanism cannot be an exact zero of the normalized threshold vector; it must come from a subtler failure of the naive branch-to-coefficient transfer.

## 6. Prior art and novelty audit

The matrix-theoretic cone argument is classical. A real symmetric positive-definite matrix with nonpositive off-diagonal entries is a Stieltjes matrix (equivalently a symmetric nonsingular M-matrix), and its inverse is entrywise nonnegative. A standard reference is A. Berman and R. J. Plemmons, *Nonnegative Matrices in the Mathematical Sciences*, SIAM Classics in Applied Mathematics 9 (1994), especially the chapters on generalized inverse-positivity and M-matrices, DOI `10.1137/1.9781611971262`. No novelty is claimed for finite-dimensional Stieltjes matrices, M-matrices, cone-preserving inverses, or the negative-part proof of positivity.

PF-251 already supplies the exact positive zero-mode coefficients, PF-261 supplies the positive massive-resolvent mixture, PF-267 supplies strict Green positivity, and PF-274 supplies the continuous-Hahn/Fourier identification of `xi=±i`. The project-specific delta is their combination for the **actual finite-seam Robin normalization**: the same operator whose square-root source exposes the critical mass-one edge has a Stieltjes-type Gram normalization, and its normalized basis columns retain a strictly positive conserved zero-mode moment.

A targeted prior-art search found the general inverse-positive/M-matrix theory but no source discussing this Prime-Flute operator, its PF-251 generalized zero mode, or the resulting threshold moment (8)--(13). No general novelty is claimed for the underlying matrix theory or Fourier evaluation.

No statement about zeta zeros or RH follows.

## 7. Boundaries and adversarial checks

1. **Threshold coefficient functional is not yet the large-mode theorem.** Equations (12)--(13) prove a nonzero absolutely convergent corridor-basis functional at `xi=±i`; they do not prove the contour/Darboux theorem needed to turn that functional into the sharp coefficient tail of `g_w(L)z_i`.
2. **Fixed axis and fixed seam only.** No uniformity in shear, hypercycle transport, variable corridor scale, canonical-tail parameters, or Robin homotopy follows.
3. **No claim that `B_w` is itself coefficientwise positive or negative.** The inverse `(I+R)^{-1}` is positive in the corridor cone, but multiplication by the square-root source operator `g_w(L)` can mix diagonal and off-diagonal signs. PF-276 does not replace that product by a sign argument.
4. **Generalized-harmonic step is coordinatewise.** The vector `q` is not in `\ell^2`. Equation (7) is justified through the massive Green representation, fixed-mass recurrence asymptotics, and the Tonelli argument (28)--(30), not by pretending that Hilbert-space functional calculus acts directly on `q`.
5. **The mass gap of `R` remains essential.** The proof of (26)--(30) uses the strictly positive masses in PF-261. It does not assert the same generalized-harmonic manipulation for the square-root operator `g_w(L)`, whose representing measure reaches zero mass.
6. **Parity phase is retained.** Equation (13) includes the odd-sector sign at `xi=i`; dropping that sign would repeat the phase error already corrected in PF-274. The magnitude is positive in both sectors.
7. **No premature clue closure.** The accepted clue is narrowed, not resolved, until the branch-to-coefficient step for (43) is proved or refuted.

The result is falsified if PF-261's off-diagonal sign is not strict in the phase-corrected corridor gauge, if the generalized resolvent identity (26) fails under its absolutely convergent Green sum, if the finite-section comparison does not converge to the complete-lift inverse, or if PF-251/PF-274's zero-mode/Fourier identification gives a different threshold sign or magnitude.

## Decisive next test

Prove or refute the fixed-row asymptotic transfer from the nonzero threshold moment to the physical normalized source:

\[
B_w^*\varphi_i=s^{-1/2}g_w(L)z^{(i)}.
\tag{44}
\]

Use PF-274's explicit equal-parameter continuous-Hahn transform to establish a local analytic-continuation and Darboux/contour theorem around `xi=±i` for the special vector `z^(i)`, using the exact weighted conservation (8) as the source regularity input. The target is a nonzero mass-one leading coefficient, or at minimum a PF-275-style lower bound that forbids every fixed-row exponent `q>1`.

If such a theorem follows, mark the accepted Robin clue negatively resolved for this PF-271 route. If it fails, isolate the exact reason the nonzero functional (12)--(13) does not control the large-degree coefficients; that failure would itself identify the only remaining fixed-axis cancellation mechanism worth pursuing.