# AF-256 — Keiper cancellation pulls back to zero-coordinate resonance curves

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `LI-DOMINANT-MODE-CONTROL`, `DIOPHANTINE-FIDELITY`, `SOURCE-COORDINATE-PULLBACK`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-255 identifies the exact growth-normalized cancellation condition for one hypothetical off-critical zero, but leaves it expressed in the transformed Keiper phase. That shrinking-target condition has an exact pullback to the original zero coordinates.

Let

\[
\rho=\beta+i\gamma,
\qquad \frac12<\beta<1,
\qquad \gamma\ge1,
\tag{1}
\]

and put

\[
a_\rho=1-\frac1\rho=r_\rho e^{i\theta_\rho},
\qquad
0<\theta_\rho<\frac\pi2,
\qquad
q_\rho=r_\rho^{-1}>1.
\tag{2}
\]

Writing

\[
A_\beta=\beta(1-\beta),
\tag{3}
\]

the phase-height relation is exactly

\[
\boxed{
\cot\theta_\rho
=\gamma-\frac{A_\beta}{\gamma}.
}
\tag{4}
\]

For integers `n>=1` and `k` satisfying

\[
0<\vartheta_{n,k}:=\frac{(2k+1)\pi}{2n}<\frac\pi2,
\tag{5}
\]

define the corresponding **Keiper cancellation resonance height**

\[
\boxed{
\Gamma_{n,k}(\beta)
=
\frac12\left(
\cot\vartheta_{n,k}
+
\sqrt{\cot^2\vartheta_{n,k}+4A_\beta}
\right).
}
\tag{6}
\]

Then

\[
\cos(n\theta_\rho)=0
\quad\Longleftrightarrow\quad
\gamma=\Gamma_{n,k}(\beta)
\tag{7}
\]

for one admissible `k`. Thus the exact cancellation loci are explicit curves in the original `(beta,gamma)` zero plane rather than mysterious conditions on a transformed phase.

Let

\[
\Delta_\rho(n)
=
\min_{k:\,0<\vartheta_{n,k}<\pi/2}
|\gamma-\Gamma_{n,k}(\beta)|.
\tag{8}
\]

For every fixed `rho` as in `(1)`, there are constants `0<c_rho<C_rho<infinity` and `N_rho` such that for all `n>=N_rho`,

\[
\boxed{
 c_\rho\, n\Delta_\rho(n)
\le
\operatorname{dist}\!\left(
 n\frac{\theta_\rho}{\pi},
 \mathbb Z+\frac12
\right)
\le
C_\rho\, n\Delta_\rho(n).
}
\tag{9}
\]

The constants absorb the fixed local factor of order `gamma^{-2}` coming from the phase-height derivative. Consequently, for every unbounded retained set `S subset N`, define

\[
\kappa_\rho(S)
:=
\liminf_{\substack{n\to\infty\\ n\in S}}
\frac{-\log\Delta_\rho(n)}{n},
\tag{10}
\]

with the usual extended-value convention at exact resonance. Then the AF-249/AF-255 cancellation exponent satisfies the exact identity

\[
\boxed{
\kappa_\rho(S)=\tau_\rho(S).
}
\tag{11}
\]

Hence the one-pair restricted root rate from AF-255 can be written entirely in zero coordinates as

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}
\left|q_\rho^nF_\rho(n)\right|^{1/n}
=
\exp\!\left(\log q_\rho-\kappa_\rho(S)\right),
}
\tag{12}
\]

where `F_rho(n)=-2m cos(n theta_rho)` for multiplicity `m`. In particular, the pair remains a superunit off-RH witness exactly when

\[
\boxed{
\kappa_\rho(S)<\log q_\rho.
}
\tag{13}
\]

Full preservation of its dominant rate is equivalent to `kappa_rho(S)=0`.

The source-specific problem left by AF-255 can therefore be stated without Keiper-phase language:

> prove that every hypothetical off-critical Riemann zero stays subexponentially far, along the retained indices, from the explicit resonance curves `(6)`, or at least farther than its own radial growth margin `log q_rho` permits.

This is a nonlinear zero-location/Diophantine condition. It is not the same as ordinary or effective linear independence of zero ordinates.

## Why it matters

AF-255 shows that height simultaneously controls radial growth and angular cancellation: `log q_rho` is of order `(beta-1/2)/gamma^2`, while `theta_rho` is of order `1/gamma`. The remaining obstruction was consequently phrased as an exponential approximation property of the transformed phase `theta_rho/pi`.

Equations `(4)`--`(11)` remove that representational layer. The dangerous set is an explicit moving lattice of resonance curves in the same `(beta,gamma)` coordinates in which zero-free regions, zero-density estimates, zero-spacing information, and other zeta theorems are normally stated. This does not make existing zero-location theorems strong enough, but it gives a direct interface on which such a comparison can be made.

For large height, `(6)` has the elementary approximation

\[
\Gamma_{n,k}(\beta)
=
\cot\vartheta_{n,k}
+\frac{A_\beta}{\cot\vartheta_{n,k}}
+O_\beta\!\left(\cot^{-3}\vartheta_{n,k}\right)
\tag{14}
\]

whenever the cotangent is large. At small resonance angle this starts with

\[
\Gamma_{n,k}(\beta)
\sim
\frac{2n}{(2k+1)\pi}.
\tag{15}
\]

Thus the obstruction resembles exponentially accurate approximation of a zero ordinate by a rational-like `n/(2k+1)` resonance mesh, but `(6)` is the exact object and retains the dependence on `beta` that the crude reciprocal-height picture loses.

The distinction from zero-ordinate linear independence is structural. The standard LI conjecture concerns rational linear relations among the ordinates `gamma`; Lamzouri's ELI conjecture quantitatively lower-bounds integer linear forms `sum ell_gamma gamma`. The resonance condition `(6)` instead compares one zero coordinate to a nonlinear family involving `cot((2k+1)pi/(2n))` and `beta(1-beta)`. A theorem transferring LI/ELI information to `(13)` would therefore require an additional nonlinear bridge; LI/ELI does not become the needed fidelity statement merely by changing notation.

## Exact derivation

### 1. The Keiper phase has an exact cotangent coordinate

From

\[
a_\rho
=\frac{\rho-1}{\rho},
\]

direct multiplication by the conjugate denominator gives

\[
a_\rho
=
\frac{\gamma^2-\beta(1-\beta)+i\gamma}
{\beta^2+\gamma^2}.
\tag{16}
\]

Because `gamma>=1` and `A_beta<=1/4`, the real and imaginary parts in `(16)` are positive. Hence `theta_rho` lies in `(0,pi/2)` and

\[
\cot\theta_\rho
=
\frac{\gamma^2-A_\beta}{\gamma}
=
\gamma-\frac{A_\beta}{\gamma},
\]

proving `(4)`.

For fixed `beta`, the function

\[
h_\beta(\gamma)=\gamma-\frac{A_\beta}{\gamma}
\tag{17}
\]

is strictly increasing on `(0,infinity)`. Solving `h_beta(gamma)=c` gives the unique positive solution

\[
\gamma
=
\frac12\left(c+\sqrt{c^2+4A_\beta}\right).
\tag{18}
\]

Setting `c=cot vartheta_{n,k}` proves `(6)` and `(7)`.

### 2. Phase distance and resonance-height distance are locally bi-Lipschitz

Write `Theta_beta(gamma)=arccot h_beta(gamma)` on `gamma>=1`. Differentiating `(17)` gives

\[
|\Theta_\beta'(\gamma)|
=
\frac{1+A_\beta/\gamma^2}
{1+(\gamma-A_\beta/\gamma)^2}.
\tag{19}
\]

This derivative is continuous and strictly positive in absolute value. For a fixed `rho`, choose a compact height interval `I_rho` around `gamma`. Equation `(19)` gives constants

\[
0<m_\rho\le |\Theta_\beta'(t)|\le M_\rho<\infty
\qquad(t\in I_\rho).
\tag{20}
\]

The half-integer phase mesh has spacing `pi/n`, so its nearest point to the fixed interior angle `theta_rho` converges to `theta_rho`. By monotonicity of `Theta_beta`, the corresponding resonance height lies in `I_rho` for all sufficiently large `n`, while all resonance points outside a slightly larger local interval stay a fixed positive distance away. Therefore the nearest phase target and the nearest resonance height are related, up to fixed constants, by the mean-value theorem:

\[
 m_\rho\Delta_\rho(n)
\le
\min_k|\theta_\rho-\vartheta_{n,k}|
\le
M_\rho\Delta_\rho(n)
\tag{21}
\]

for all large `n`, after harmlessly renaming the constants if needed.

On the other hand,

\[
\operatorname{dist}\!\left(
 n\frac{\theta_\rho}{\pi},
 \mathbb Z+\frac12
\right)
=
\frac n\pi
\min_k|\theta_\rho-\vartheta_{n,k}|.
\tag{22}
\]

Combining `(21)` and `(22)` proves `(9)`.

At high height, `(19)` is `Theta(gamma^{-2})`, so the inverse height-per-angle factor is `Theta(gamma^2)`. This is a fixed multiplicative conditioning factor for each fixed zero and therefore disappears at the `1/n` logarithmic scale.

### 3. The exponential approximation exponents are identical

Take logarithms in `(9)`. Whenever neither side vanishes,

\[
\left|
\frac{-\log\operatorname{dist}(n\theta_\rho/\pi,\mathbb Z+1/2)}{n}
-
\frac{-\log\Delta_\rho(n)}{n}
\right|
\le
\frac{\log n+C_\rho'}{n}
\tag{23}
\]

for a fixed constant `C_rho'`. The right side tends to zero. Exact resonance makes both distances zero simultaneously by `(7)`, so the same conclusion holds in the extended-value sense. Taking the restricted liminf along any unbounded `S` proves `(11)`.

AF-249 identifies the root-scale decay of the one-pair cosine with `tau_rho(S)`, and AF-255 multiplies that angular rate by the exact radial factor `q_rho`. Substituting `(11)` yields `(12)` and `(13)`.

### 4. The resonance mesh is only polynomially fine

For orientation, if `vartheta` is small then

\[
\cot\vartheta
=\vartheta^{-1}+O(\vartheta),
\]

and expanding `(18)` for large positive `c` gives

\[
\frac12(c+\sqrt{c^2+4A_\beta})
=c+\frac{A_\beta}{c}+O_\beta(c^{-3}).
\]

This proves `(14)`--`(15)`. Adjacent resonances near a fixed high `gamma` are separated on the height scale by `Theta_rho(1/n)`. The fidelity obstruction is therefore not ordinary closeness to the mesh, which is automatic as it refines, but **exponential** closeness relative to `n`, exactly as measured by `(10)`.

## Prior-art audit

The Keiper--Li transform and zero-sum framework are classical. Bombieri and Lagarias, **“Complements to Li's Criterion for the Riemann Hypothesis,”** *Journal of Number Theory* 77 (1999), 274--287, DOI `10.1006/jnth.1999.2392`, establish the general zero-set form of Li's criterion. André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9 (2006), 53--63, DOI `10.1007/s11040-005-9002-8`, gives exact/asymptotic Keiper--Li formulae and the non-tempered oscillatory behavior in the off-RH case. Juan Arias de Reyna, **“Asymptotics of Keiper-Li coefficients,”** *Functiones et Approximatio* 45 (2011), 7--21, DOI `10.7169/facm/1317045228`, develops further asymptotic RH-equivalent control of the coefficients.

The zero-ordinate LI conjecture is classical. Youness Lamzouri, **“An effective Linear Independence conjecture for the zeros of the Riemann zeta function and applications,”** arXiv:`2311.04860` (v2, 2024), formulates ELI as a lower bound on integer linear forms in ordinates and uses it for extreme-value questions in prime-number error terms. That is adjacent prior art for quantitative phase control, but its controlled object is linear combinations of `gamma`, not the nonlinear resonance distance `(8)`.

No novelty is claimed for the Möbius-coordinate algebra, cotangent inversion, local bi-Lipschitz change of variable, or standard Diophantine/shrinking-target language. A targeted search did not locate the exact use of the resonance curves `(6)` to pull the AF-249/AF-255 exponential cancellation exponent back to `(beta,gamma)` coordinates. The durable contribution is narrow: the previously abstract Keiper-phase fidelity condition is exactly equivalent, at root scale, to exponential avoidance of an explicit family of zero-coordinate resonance curves.

## Boundaries and failure modes

**This is a coordinate pullback, not a new RH criterion.** AF-255 already supplies the pair-level root-rate criterion. The present result changes the mathematical interface on which its missing source theorem must act.

**The result is one-pair and fixed-zero.** The constants in `(9)` depend on the fixed zero. Multimode affine cancellation remains governed by AF-253's quotient fiber norm and may require simultaneous resonance geometry rather than the scalar curves `(6)`.

**No zero-location theorem is upgraded automatically.** A zero-free region, zero-density estimate, spacing estimate, LI conjecture, or ELI conjecture controls a different quantity unless an explicit theorem connects it to `Delta_rho(n)` uniformly at the exponential scale required by `(13)`.

**The assumption `gamma>=1` is only a clean branch choice.** It guarantees that the Keiper image lies in the first quadrant for `1/2<beta<1`. All nontrivial Riemann zeros are far above this range; lower abstract heights can be handled by tracking the argument branch separately.

**Polynomial conditioning does not matter for one fixed zero but can matter in families.** The derivative scale in `(19)` is `Theta(gamma^{-2})`. It disappears from `(11)` for fixed `rho`, but any theorem uniform over increasing zero height must retain this conditioning rather than silently absorb it into a constant.

## Research consequence

The source-specific frontier after AF-255 is now an explicit zero-coordinate avoidance problem. For each hypothetical dominant off-critical zero and each retained set `S`, the exact target is

\[
\liminf_{\substack{n\to\infty\\n\in S}}
\frac{-\log\operatorname{dist}
\bigl(\gamma,\{\Gamma_{n,k}(\beta)\}_k\bigr)}{n}
<\log q_\rho.
\tag{24}
\]

This formulation suggests a sharper audit of candidate arithmetic inputs. Results about zero ordinates should be admitted only if they yield quantitative separation from `(6)` after the nonlinear Keiper pullback; ordinary irrationality, linear independence, coarse zero-free geometry, and counting information are not the target quantity by themselves.

For multimode families, the analogous next step is to pull AF-253's simultaneous coefficient-annihilator set back through the joint zero-coordinate map and identify whether known or conjectural zero relations control distance to that pulled-back variety. That would test whether the scalar resonance geometry here is merely a convenient reparameterization or the first component of a genuinely source-natural fidelity condition.