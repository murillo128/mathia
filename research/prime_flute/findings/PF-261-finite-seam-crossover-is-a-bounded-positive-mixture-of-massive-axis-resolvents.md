# PF-261 — finite seam crossover is a bounded positive mixture of massive axis resolvents

**Status:** `EXACT-DERIVED + CLASSICAL-PARTIAL-FRACTION + FIXED-AXIS-COMPLETE-LIFT-CLOSURE + POSITIVE-RESOLVENT-MIXTURE + FINITE-S-CROSSOVER-REDUCTION + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-258-thin-seam-relative-edge-is-a-linearly-weighted-jacobi-tangent-with-intrinsic-dimension-six|PF-258]] identifies the thin-seam tangent of the fixed-axis relative seam,

\[
\mathcal R_{s,r}^0
=s^{-1}A^{-1/4}f_{rs}(L)A^{-1/4}
\longrightarrow rH,
\qquad
H=A^{-1/4}LA^{-1/4},
\]

and [[research/prime_flute/findings/PF-259-intrinsic-six-tangent-has-anchored-gaussian-large-time-control|PF-259]]--[[research/prime_flute/findings/PF-260-davies-gaffney-closes-short-time-intrinsic-six-fractional-window|PF-260]] prove that the tangent retains the separated square-root window `1<R<2` required to keep the local Robin route alive. The remaining fixed-axis obstruction is not the tangent itself but the growing crossover region `rs\sqrt L\asymp1`, where PF-258's finite-dimensional `O(s^2)` expansion is not uniform.

That crossover admits an exact reduction which is substantially more rigid than an arbitrary noncommuting perturbation. For every finite `s>0`, the full fixed-axis relative seam is a **bounded positive operator**, its relative square-root map is bounded on the complete lift, and the polar-free Robin identity of [[research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform|PF-257]] holds there without Galerkin truncation. Moreover the entire nonlinear multiplier `s^{-1}\sqrt\lambda\tanh(rs\sqrt\lambda)` is an exact positive partial-fraction sum of ordinary resolvents of `L` at the negative masses

\[
a_k^2=\frac{(2k+1)^2\pi^2}{4r^2s^2}.
\]

Consequently every **off-diagonal** Gegenbauer matrix element of `\mathcal R_{s,r}^0` is a weighted sum of the Green matrices of `L+a_k^2`. Since PF-238 identifies `L` unitarily with `1-\partial_\tau^2` on the complete axis, those resolvents have the explicit kernel

\[
\frac{e^{-\sqrt{1+a_k^2}|\tau-\sigma|}}{2\sqrt{1+a_k^2}}.
\]

Thus the finite-`s` problem no longer requires controlling `\tanh` functional calculus abstractly. It reduces to a concrete uniform Green-function question for a one-parameter family of **massive complete-axis resolvents**, followed by the regular bounded transform `X(I+X^*X)^{-1}`. This does not yet prove the required weighted `R>1` high-to-low estimate, but it closes the fixed-axis domain/closure caveat in PF-257 and gives a precise analytic object on which the crossover can be won or killed.

## Claim

Use the fixed-axis operators from PF-235/PF-238/PF-258,

\[
A=-\partial_\theta^2+\csc^2\theta,
\qquad
L=U(1-\partial_\tau^2)U^*,
\qquad
0<L\le2A,
\tag{1}
\]

with

\[
f_w(\lambda)=\sqrt\lambda\tanh(w\sqrt\lambda),
\qquad
Q_{rs}^0=f_{rs}(L),
\qquad
K_s^0=sA^{1/2},
\tag{2}
\]

and fixed `r>0`, `s>0`. Put

\[
\mathcal R_{s,r}^0
=(K_s^0)^{-1/2}Q_{rs}^0(K_s^0)^{-1/2}
=s^{-1}A^{-1/4}Q_{rs}^0A^{-1/4}
\tag{3}
\]

in quadratic-form sense. Then:

1. the seam form satisfies the two exact scalar-calculus bounds
   \[
   0\le Q_{rs}^0\le rsL,
   \qquad
   0\le Q_{rs}^0\le L^{1/2}\le\sqrt2\,A^{1/2};
   \tag{4}
   \]
2. therefore
   \[
   0\le\mathcal R_{s,r}^0\le rH
   \quad\text{in form sense},
   \qquad
   \boxed{\|\mathcal R_{s,r}^0\|\le\frac{\sqrt2}{s}};
   \tag{5}
   \]
3. if
   \[
   X_{s,r}^0:=\overline{(K_s^0)^{-1/2}(Q_{rs}^0)^{1/2}},
   \tag{6}
   \]
   then `X_{s,r}^0` is bounded on the complete fixed-axis boundary space and
   \[
   \boxed{
   X_{s,r}^0(X_{s,r}^0)^*=\mathcal R_{s,r}^0,
   \qquad
   \|X_{s,r}^0\|\le2^{1/4}s^{-1/2};
   }
   \tag{7}
   \]
4. the full fixed-axis energy-normalized Robin source factor therefore has the bounded extension
   \[
   \boxed{
   B_{s,r}^0
   =(I+X_{s,r}^0(X_{s,r}^0)^*)^{-1}X_{s,r}^0
   =X_{s,r}^0(I+(X_{s,r}^0)^*X_{s,r}^0)^{-1},
   }
   \tag{8}
   \]
   with
   \[
   \boxed{\|B_{s,r}^0\|\le\frac12;}
   \tag{9}
   \]
   in particular PF-257's bounded-regularization algebra is exact on the **untruncated fixed-axis complete lift** for every `s>0`;
5. defining
   \[
   a_k=\frac{(2k+1)\pi}{2rs},
   \qquad k=0,1,2,\dots,
   \tag{10}
   \]
   one has the scalar identity
   \[
   \boxed{
   \frac1s\sqrt\lambda\tanh(rs\sqrt\lambda)
   =\frac{2}{rs^2}\sum_{k=0}^{\infty}
   \frac{\lambda}{\lambda+a_k^2},
   \qquad \lambda\ge0;
   }
   \tag{11}
   \]
6. spectral calculus and the bounded sandwich in (5) therefore give the positive strong-operator/form expansion
   \[
   \boxed{
   \mathcal R_{s,r}^0
   =\frac{2}{rs^2}\sum_{k=0}^{\infty}
   A^{-1/4}L(L+a_k^2)^{-1}A^{-1/4};
   }
   \tag{12}
   \]
7. if `Ae_n=\kappa_n^2e_n` is PF-247's Gegenbauer basis, then opposite parities do not mix, and for `i\ne j` of the same parity
   \[
   \boxed{
   \langle e_i,\mathcal R_{s,r}^0e_j\rangle
   =-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
   \sum_{k=0}^{\infty}a_k^2
   \langle e_i,(L+a_k^2)^{-1}e_j\rangle;
   }
   \tag{13}
   \]
8. with `\mu_k=\sqrt{1+a_k^2}`, PF-238 gives the exact complete-axis Green representation
   \[
   \boxed{
   (L+a_k^2)^{-1}
   =U(-\partial_\tau^2+\mu_k^2)^{-1}U^*,
   }
   \tag{14}
   \]
   whose integral kernel in `\tau` is
   \[
   \boxed{
   G_k(\tau,\sigma)
   =\frac{1}{2\mu_k}e^{-\mu_k|\tau-\sigma|}.
   }
   \tag{15}
   \]

Equations (5)--(15) are exact for the fixed-axis finite seam. They do **not** assert the uniform weighted mode decay required by PF-243, nor do they transfer automatically to the actual hypercycle/corridor operator.

## 1. Finite seam scale is form-bounded by the first-order corridor scale

For every `x\ge0`,

\[
0\le\tanh x\le\min\{x,1\}.
\tag{16}
\]

Applying (16) to (2) gives

\[
0\le f_{rs}(L)\le rsL
\tag{17}
\]

and

\[
0\le f_{rs}(L)\le L^{1/2}.
\tag{18}
\]

PF-238 proves `L\le2A` in quadratic-form sense. The square-root function is operator monotone, so the Löwner--Heinz inequality gives

\[
L^{1/2}\le\sqrt2\,A^{1/2}.
\tag{19}
\]

Equations (17)--(19) prove (4). The first inequality reproduces PF-258's tangent domination,

\[
\mathcal R_{s,r}^0\le rA^{-1/4}LA^{-1/4}=rH.
\tag{20}
\]

The second is qualitatively different. For every `u`,

\[
\begin{aligned}
\langle u,\mathcal R_{s,r}^0u\rangle
&=s^{-1}\langle A^{-1/4}u,Q_{rs}^0A^{-1/4}u\rangle\\
&\le \frac{\sqrt2}{s}
\langle A^{-1/4}u,A^{1/2}A^{-1/4}u\rangle\\
&=\frac{\sqrt2}{s}\|u\|^2.
\end{aligned}
\tag{21}
\]

Hence the relative seam is a bounded positive operator for every nonzero finite seam scale even though its `s\downarrow0` tangent `rH` is unbounded. This is the exact order change expected from

\[
f_{rs}(\lambda)\sim rs\lambda
\quad(rs\sqrt\lambda\ll1),
\qquad
f_{rs}(\lambda)\sim\sqrt\lambda
\quad(rs\sqrt\lambda\gg1),
\tag{22}
\]

but (21) makes the statement rigorous after the noncommuting `A^{-1/4}` sandwich.

## 2. The fixed-axis relative square-root map closes on the complete lift

Let `K=K_s^0` and `Q=Q_{rs}^0`. Equation (4) says

\[
Q\le\frac{\sqrt2}{s}K
\tag{23}
\]

as forms. Since `A\ge\alpha^2>0`, `K^{-1/2}` is bounded. Form domination implies that

\[
Y:=Q^{1/2}K^{-1/2}
\tag{24}
\]

is bounded on the whole Hilbert space and

\[
\|Y\|^2\le\frac{\sqrt2}{s}.
\tag{25}
\]

The densely defined product `K^{-1/2}Q^{1/2}` therefore has bounded adjoint `Y` and a bounded closure

\[
X=Y^*.
\tag{26}
\]

Moreover

\[
XX^*=Y^*Y
=K^{-1/2}QK^{-1/2}
=\mathcal R_{s,r}^0
\tag{27}
\]

as bounded operators, proving (7).

The form sum also factorizes without truncation:

\[
K+Q
=K^{1/2}(I+XX^*)K^{1/2}
\tag{28}
\]

in the sense of closed positive forms on `D(K^{1/2})`. Since `K` is strictly positive and `XX^*` is bounded, inversion of the form factorization gives the bounded extension of the normalized source factor

\[
K^{1/2}(K+Q)^{-1}Q^{1/2}
=(I+XX^*)^{-1}X.
\tag{29}
\]

The bounded push-through identity gives the second expression in (8), and PF-257's block-functional-calculus argument gives (9). Thus the **fixed-axis finite-`s` complete lift** has now passed the domain/closure gate that PF-257 deliberately left open.

This does not settle the actual seam. PF-235/PF-256 still have to transport the fixed-axis statement through the intrinsic hypercycle and actual corridor operators with the required weighted locality.

## 3. The `tanh` crossover has an exact positive resolvent decomposition

The classical partial fraction for `\coth` is

\[
\coth z=\frac1z+2z\sum_{n=1}^{\infty}\frac1{z^2+n^2\pi^2}.
\tag{30}
\]

Together with the elementary identity

\[
\tanh z=2\coth(2z)-\coth z,
\tag{31}
\]

the even terms cancel and one obtains

\[
\boxed{
\tanh z
=8z\sum_{k=0}^{\infty}
\frac1{(2k+1)^2\pi^2+4z^2}.
}
\tag{32}
\]

Substitute `z=rs\sqrt\lambda` and define (10). This gives (11) directly. All summands in (11) are nonnegative on `\lambda\ge0`; the partial sums increase pointwise to the left side. The spectral theorem therefore yields monotone form convergence after applying the function to `L`. Sandwiching by `A^{-1/4}` and using the finite bound (21) upgrades the partial sums to strong convergence to `\mathcal R_{s,r}^0`, proving (12).

The partial fraction is classical. NIST DLMF §4.36.3 records (30), and §4.36 derives hyperbolic partial fractions from the corresponding trigonometric expansions. No novelty is claimed for (30)--(32).

## 4. Off-diagonal mode conversion is exactly a massive-resolvent Green problem

For every `a>0`,

\[
L(L+a^2)^{-1}=I-a^2(L+a^2)^{-1}.
\tag{33}
\]

Because `A^{-1/4}` is diagonal in the Gegenbauer basis, the identity contribution in (33) vanishes when `i\ne j`. Applying (33) term by term to the strongly convergent partial sums in (12) gives (13).

This is the useful cancellation. The diagonal of (12) cannot be split into an infinite sum of identity pieces, but every separated high-to-low matrix element — exactly the type relevant to the current clue — contains only the resolvent Green terms. There is no residual polynomial/tangent approximation error to estimate.

PF-247 shows that `L` preserves Gegenbauer parity and is tridiagonal inside each parity chain. Therefore each matrix in (13) is the Green matrix of a one-dimensional Jacobi operator at the negative spectral point `-a_k^2`. The smallest mass is already

\[
a_0=\frac{\pi}{2rs},
\tag{34}
\]

and higher terms have the odd ladder `(2k+1)a_0`. The difficult crossover `rs\sqrt L\asymp1` has therefore become a family-uniform Green-function problem with an explicit mass parameter, not an uncontrolled difference between `f_{rs}(L)` and its tangent.

## 5. PF-238 makes every massive resolvent explicit on the complete axis

PF-238 proves the exact unitary compactification

\[
L=U(1-\partial_\tau^2)U^*.
\tag{35}
\]

Hence (14) follows with

\[
\mu_k=\sqrt{1+a_k^2},
\tag{36}
\]

and the Green kernel of `-\partial_\tau^2+\mu_k^2` on `\mathbb R` is exactly (15).

If `e_n` is PF-247's normalized eigenbasis of `A`,

\[
e_n(\theta)
=h_n^{-1/2}\sin^\alpha\theta\,C_n^\alpha(\cos\theta),
\qquad
\alpha=\frac{1+\sqrt5}{2},
\tag{37}
\]

then

\[
\psi_n(\tau):=U^*e_n
=h_n^{-1/2}\operatorname{sech}^{\alpha+1/2}\tau\,
C_n^\alpha(-\tanh\tau).
\tag{38}
\]

Thus every Green matrix element in (13) is the explicit double integral

\[
\boxed{
\langle e_i,(L+a_k^2)^{-1}e_j\rangle
=\frac1{2\mu_k}
\iint_{\mathbb R^2}
\overline{\psi_i(\tau)}
 e^{-\mu_k|\tau-\sigma|}
\psi_j(\sigma)\,d\tau d\sigma.
}
\tag{39}
\]

This representation also exposes a classical special-function route. Since

\[
\operatorname{sech}^{\alpha+1/2}\tau
=(1-\tanh^2\tau)^{\alpha/2+1/4},
\tag{40}
\]

the functions (38), up to the harmless parity sign, are exactly in the one-dimensional Gegenbauer family whose Fourier transforms are beta/gamma factors times continuous Hahn polynomials. A convenient modern reference is E. Güldoğan Lekesiz, R. Aktaş, I. Area, *Fourier Transform of the Orthogonal Polynomials on the Unit Ball and Continuous Hahn Polynomials*, Axioms 11 (2022), 558, DOI `10.3390/axioms11100558`, especially the `r=1` specialization around equations (31)--(33). By Plancherel, (39) can therefore be rewritten as a one-dimensional continuous-Hahn integral with denominator `\xi^2+\mu_k^2`.

That literature identity is **not** being used here to claim the missing mode-decay estimate. It provides an exact coordinate system in which the next estimate can be attempted without inventing another interpolation.

## 6. What the crossover problem has become

The current accepted clue asks whether some strict `R>1` part of PF-259/PF-260's tangent margin survives finite seam scale. PF-261 reduces that question to two concrete layers.

First, prove a separated-cone estimate for the massive Green matrices in (13), uniformly over the coupled regime of `s`, `k`, and mode indices. The exact axis kernel (39) or the equivalent continuous-Hahn Fourier representation are natural starting points. The odd mass ladder must then be summed with the prefactor in (13). A bound for one fixed `k`, one fixed output row, or one fixed `s` is not enough.

Second, feed that control into the **combined** bounded Robin factor (8). The left Gram variable is already the bounded `\mathcal R_{s,r}^0`, but PF-257/PF-244 warn that Gram control alone does not determine high-to-low locality of `B_{s,r}^0`; the source orientation must remain correlated with its singular amplitude. The benefit of (7)--(9) is that this correlation is now defined rigorously on the full fixed-axis lift rather than only in Galerkin models.

The route is killed at this stage if the exact Green sum (13) exhibits high-to-low leakage that destroys every uniform `R>1` weight in the crossover. If it preserves such a weight, the next gate is the actual-corridor/hypercycle transfer already isolated by PF-255/PF-256 and the downstream Robin--Poisson clue.

## 7. Prior-art and novelty audit

The ingredients used here are classical:

- NIST DLMF §4.36 gives the hyperbolic partial-fraction machinery behind (30)--(32);
- the Löwner--Heinz square-root monotonicity used in (19) is standard operator theory;
- functional calculus representations of Dirichlet-to-Neumann operators by complete Bernstein functions belong to a broad classical/modern framework; see M. Kwaśnicki and J. Mucha, *Extension technique for complete Bernstein functions of the Laplace operator*, Journal of Evolution Equations 18 (2018), 1341--1379, DOI `10.1007/s00028-018-0444-4`;
- the Fourier/Gegenbauer-to-continuous-Hahn transform used only as a possible exact analysis coordinate is established in the 2022 Lekesiz--Aktaş--Area reference above.

A targeted search did not locate the Prime-Flute-specific quarter-order normalized operator (3), its complete-lift bound (5)--(9), or the exact use of the odd-pole resolvent expansion to reduce the finite-`s` **Gegenbauer high-to-low** crossover to (13)/(39). No novelty is claimed for `\tanh` partial fractions, complete Bernstein functions, one-dimensional resolvent kernels, form domination, or continuous Hahn transforms. The durable project-specific result is the exact reduction and domain closure for the already-defined PF seam.

## 8. Falsification and boundary checks

1. **Fixed axis only.** `Q_{rs}^0` and `K_s^0` are the PF-235/PF-258 reference operators. Nothing above proves the same bound or Green representation after the actual hypercycle/corridor transport.
2. **Finite `s>0` only for boundedness.** The estimate `\|\mathcal R_{s,r}^0\|\le\sqrt2/s` degenerates as `s\downarrow0`, consistently with the unbounded tangent `rH`. It is not a uniform tangent bound.
3. **Form order is not weighted locality.** The inequalities `\mathcal R_{s,r}^0\le rH` and `\mathcal R_{s,r}^0\le(\sqrt2/s)I` do not imply the separated weighted estimates by themselves.
4. **Strong series is not termwise norm summability.** Equation (12) is a positive strong/form expansion. Do not bound its terms independently by a non-summable operator-norm majorant and call that a proof of weighted locality.
5. **Off-diagonal cancellation is essential.** Equation (13) uses `i\ne j`; the identity pieces in (33) cannot be separated on the diagonal into a convergent series.
6. **Explicit axis kernel is not mode locality.** Exponential decay in `|\tau-\sigma|` does not automatically imply the required high-to-low decay in Gegenbauer index. The continuous-Hahn bridge still needs a uniform asymptotic/weighted estimate.
7. **Combined transform remains load-bearing.** Boundedness and exact closure of `X` do not license replacing `B_X` by a naked polar factor or by a function of `XX^*` alone.
8. **No global/RH conclusion.** Nothing here proves PF-243's separated Robin--Poisson estimate, trace-class shear reassembly, finite-pant completion, scattering/determinant statements, a zeta-zero statement, or RH.

## Decisive next test

Use (13) and (39), or the equivalent continuous-Hahn Fourier representation of (38), to prove or refute a **uniform separated-cone bound for the full odd-mass resolvent sum** in the crossover `rs\sqrt L\asymp1`. The target is not sharpness: it is preservation of any fixed exponent `R>1` after the `A^{-1/4}` endpoint weights and the combined bounded Robin transform are included. A counterexample at this exact fixed-axis level would close the current route before the more expensive actual-corridor and global assembly steps.