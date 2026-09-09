# WI-215 — fixed-size screens cannot flatten a natural Gallagher slab

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + CLASSICAL-IDENTITY + LITERATURE-CONTEXT`.

WI-212 shows that every fixed finite packet of reciprocal *samples* can be cancelled by only finitely many additional off-line functional-equation pairs. WI-213 then shows that the particular two-pair WI-211 screen cannot flatten the full natural `1/M` neighborhood of the second reciprocal harmonic. The latter left open whether that failure was peculiar to the exact WI-211 phases and equal-depth ansatz.

It is not. There is a general finite-rank obstruction:

> **For every fixed integer `N`, no selected screen built from at most `N` off-line functional-equation pairs can make even one fixed natural reciprocal Gallagher slab subdiagonal for a count-saturating bow.** More generally, the same statement holds for any screen whose normalized local residue is a sum of at most a fixed number `n` of complex exponential channels, with arbitrary coefficients and arbitrary complex exponents depending on `M`.

Quantitatively, for each fixed channel budget `n` one can choose fixed slab/box parameters and obtain a constant `delta_n>0`, independent of all screen depths, phases and coefficients, such that the box-integrated normalized residue has `L^2` energy at least `delta_n` for all sufficiently large `M`. Under the exact source dictionary of WI-213 this implies selected physical residue energy

\[
\gg_n \frac{X_k^2(\log T)^3}{M},
\]

up to the fixed powers of `d`, while the raw-prime Gallagher diagonal on the matching short interval is only

\[
\asymp \frac{X_k^2(\log T)^2}{M}.
\]

Thus every fixed-complexity screen remains `Omega(log T)` superdiagonal in energy on that slab. **Any continuum screen that succeeds asymptotically must therefore use an unbounded number of independent exponential/zero channels.** This is a necessary complexity condition, not a zeta contradiction: complementary zeros and structured source terms may still cancel the selected residue, and the argument gives no useful rate once the channel count tends to infinity.

## 1. Natural bow profile

Let `M` be odd and retain the WI-209--WI-213 bow normalization

\[
D_M(t)=\frac{\sin(\pi Mt)}{\sin(\pi t)},
\qquad
B_M(t)=2\cosh(ht)D_M(t),
\tag{1}
\]

with fixed `h>0`. Fix an integer reciprocal harmonic `k>=1` and put

\[
f_{M,k}(u):=\frac1M B_M\!\left(k+\frac{u}{M}\right).
\tag{2}
\]

Because `M` is odd, the signs in numerator and denominator cancel exactly, so

\[
f_{M,k}(u)
=2\cosh\!\left(hk+\frac{hu}{M}\right)
\frac{\sin(\pi u)}{M\sin(\pi u/M)}.
\tag{3}
\]

Hence uniformly on every fixed compact `u`-interval,

\[
\boxed{
f_{M,k}(u)\longrightarrow
f_k(u):=2\cosh(hk)\frac{\sin(\pi u)}{\pi u}.
}
\tag{4}
\]

The limit is a nonzero sinc profile with a full interval of Fourier frequencies; this is the feature that a fixed-rank exponential screen cannot reproduce.

## 2. Every fixed zero screen has finite translation rank

A selected off-line zero together with its same-ordinate functional-equation mirror contributes in the unfolded variable exactly the WI-213 form

\[
2\cosh(a t)e^{i\phi t}
=e^{(a+i\phi)t}+e^{(-a+i\phi)t}.
\tag{5}
\]

On `t=k+u/M`, after division by `M`, this is a sum of two exponentials in `u`. Therefore a screen with at most `N` such pairs is contained in the larger class

\[
g_M(u)=\sum_{\ell=1}^{n}c_{\ell,M}e^{z_{\ell,M}u},
\qquad n=2N,
\tag{6}
\]

where the coefficients and complex exponents are completely arbitrary. Allowing arbitrary data in (6) only strengthens the obstruction. Any additional fixed number of critical-line or conjugate channels merely changes the fixed value of `n`.

The elementary rank fact needed below is exact. Fix `tau>0`. For every function of the form (6), the `n+1` translates

\[
g_M(s),\ g_M(s+\tau),\ldots,g_M(s+n\tau)
\tag{7}
\]

are linearly dependent as functions of `s`. Indeed, the coefficient vectors of these translates in the at-most-`n` dimensional span of the exponentials `e^{z_{\ell,M}s}` form an `n` by `n+1` matrix. Thus there is a vector

\[
a^{(M)}=(a_0,\ldots,a_n),
\qquad \|a^{(M)}\|_2=1,
\tag{8}
\]

such that

\[
\boxed{
\sum_{j=0}^{n}a_jg_M(s+j\tau)=0
}
\tag{9}
\]

identically. Repeated or coalescing exponents only lower the translation rank, so no separation, bounded-depth or nonconfluence hypothesis is being used.

The same remains true after multiplication by any exponential weight and after box integration, because both operations preserve the number of exponential channels.

## 3. The box-integrated sinc target has infinite translation rank

Fix constants `lambda>0`, `tau>0` and `c>0` with

\[
2c>\lambda+n\tau,
\tag{10}
\]

and set

\[
I=[-c,c-\lambda-n\tau].
\tag{11}
\]

For a function `r`, write

\[
(K_\lambda r)(s):=\int_s^{s+\lambda}r(v)\,dv.
\tag{12}
\]

Put

\[
F_k:=K_\lambda f_k.
\tag{13}
\]

Then the `n+1` functions

\[
F_k(s),F_k(s+\tau),\ldots,F_k(s+n\tau)
\tag{14}
\]

are linearly independent on `I`.

To see this without invoking an approximation theorem, use the classical Fourier identity

\[
\frac{\sin(\pi u)}{\pi u}
=\int_{-1/2}^{1/2}e^{2\pi i\xi u}\,d\xi.
\tag{15}
\]

Therefore

\[
F_k(s)
=2\cosh(hk)
\int_{-1/2}^{1/2}
e^{2\pi i\xi s}m_\lambda(\xi)\,d\xi,
\tag{16}
\]

where

\[
m_\lambda(\xi)
:=\int_0^\lambda e^{2\pi i\xi v}\,dv.
\tag{17}
\]

Suppose `sum_{j=0}^n a_j F_k(s+j tau)=0` on `I`. The left side is entire in `s`, hence it vanishes identically. Fourier uniqueness then gives

\[
m_\lambda(\xi)
P(e^{2\pi i\tau\xi})=0
\quad\text{for a.e. }\xi\in[-1/2,1/2],
\tag{18}
\]

with

\[
P(z)=\sum_{j=0}^{n}a_jz^j.
\tag{19}
\]

The multiplier `m_lambda` has only isolated zeros and is nonzero on an open subinterval. Hence `P` vanishes on an arc of the unit circle and therefore `P=0`. All `a_j` vanish, proving the independence claim.

Let `G_infty` be the Gram matrix of the family (14) in `L^2(I)`. It is positive definite, so

\[
\boxed{
\mu_n:=\lambda_{\min}(G_\infty)>0.
}
\tag{20}
\]

No value of `mu_n` is needed; only its strict positivity for each fixed `n` matters.

## 4. Uniform separation from every n-channel screen

Now incorporate the small source Jacobian exactly rather than treating it as an error. Let

\[
L=\log T,
\qquad
X_k=T^{k/d},
\qquad
x_{k,M}(u)=T^{(k+u/M)/d}
=X_k e^{uL/(dM)},
\tag{21}
\]

and assume the bow scale used throughout WI-183--WI-213,

\[
M=T^{\vartheta+o(1)},
\qquad \vartheta>0.
\tag{22}
\]

Set

\[
\eta_M:=\frac{L}{2dM}.
\tag{23}
\]

The exactly normalized short-interval residue involves

\[
\widetilde f_{M,k}(u):=e^{\eta_Mu}f_{M,k}(u).
\tag{24}
\]

By (4) and `eta_M->0`,

\[
\widetilde f_{M,k}\to f_k
\tag{25}
\]

uniformly on fixed compact intervals. Consequently the Gram matrix `G_M` of

\[
K_\lambda\widetilde f_{M,k}(s+j\tau),
\qquad 0\le j\le n,
\tag{26}
\]

on `I` converges entrywise to `G_infty`. For all sufficiently large `M`,

\[
\lambda_{\min}(G_M)\ge\frac{\mu_n}{2}.
\tag{27}
\]

Let `g_M` be an arbitrary screen of the form (6) and define

\[
H_M(s)
:=K_\lambda\!\left[e^{\eta_M\cdot}
(f_{M,k}+g_M)\right](s).
\tag{28}
\]

Multiplication by `e^{eta_M u}` and application of `K_lambda` preserve the at-most-`n` exponential-channel property of the screen. Choose the normalized dependence vector (8) for those translated screen terms. The screen cancels from the translated combination, so (27) gives

\[
\begin{aligned}
\sqrt{\mu_n/2}
&\le
\left\|
\sum_{j=0}^{n}a_j
K_\lambda\widetilde f_{M,k}(\cdot+j\tau)
\right\|_{L^2(I)}\\
&=
\left\|
\sum_{j=0}^{n}a_jH_M(\cdot+j\tau)
\right\|_{L^2(I)}\\
&\le
\sum_{j=0}^{n}|a_j|
\|H_M(\cdot+j\tau)\|_{L^2(I)}\\
&\le
\sqrt{n+1}
\|H_M\|_{L^2([-c,c-\lambda])}.
\end{aligned}
\tag{29}
\]

Thus

\[
\boxed{
\int_{-c}^{c-\lambda}|H_M(s)|^2ds
\ge
\delta_n:=\frac{\mu_n}{2(n+1)}>0
}
\tag{30}
\]

for every at-most-`n` channel screen and all sufficiently large `M`. The bound is uniform over arbitrarily large radial depths, drifting phases, colliding exponents, coefficients that grow with `M`, and all finite-dimensional degeneracies.

This is the promised fixed-complexity obstruction.

## 5. Exact conversion to the physical Gallagher scale

WI-213 records the exact selected zero-residue identity. With `R_M=M(f_{M,k}+g_M)` and the source coordinate (21), the corresponding twisted short-interval residue is

\[
Q_M(s,\lambda)
=-\int_{x_{k,M}(s)}^{x_{k,M}(s+\lambda)}
x^{-1/2}R_M(t(x))\,dx.
\tag{31}
\]

Using

\[
\frac{dx_{k,M}(u)}{du}
=x_{k,M}(u)\frac{L}{dM},
\tag{32}
\]

one obtains **exactly**

\[
\boxed{
Q_M(s,\lambda)
=-X_k^{1/2}\frac{L}{d}H_M(s).
}
\tag{33}
\]

There is no screen-dependent asymptotic error in (33); the factor `e^{eta_M u}` in (28) is precisely the square-root Jacobian.

Moreover

\[
\frac{dx_{k,M}(s)}{ds}
=X_ke^{sL/(dM)}\frac{L}{dM}
=(1+o(1))\frac{X_kL}{dM}
\tag{34}
\]

uniformly on the fixed slab. Equations (30), (33) and (34) give

\[
\boxed{
\int |Q_M(x)|^2dx
\ge
(\delta_n+o(1))
\frac{X_k^2L^3}{d^3M}.
}
\tag{35}
\]

The physical short length is

\[
K\sim\lambda\frac{X_kL}{dM},
\tag{36}
\]

and the raw-prime Gallagher diagonal is

\[
X_kK\log X_k
\sim
\lambda k\frac{X_k^2L^2}{d^2M}.
\tag{37}
\]

Therefore

\[
\boxed{
\frac{\int |Q_M(x)|^2dx}
{X_kK\log X_k}
\ge
\left(\frac{\delta_n}{\lambda k d}+o(1)\right)L.
}
\tag{38}
\]

For every fixed `n`, the selected screened-bow residue is logarithmically superdiagonal on the natural source slab.

## 6. What this rules out and what it does not

The result upgrades the WI-213 obstruction in a direction that does not depend on its special two-pair algebra. A fixed number of unequal-depth pairs, arbitrary phase lifts, arbitrary coefficients, or a different finite screen ansatz cannot flatten a natural sinc slab. The obstruction is rank-theoretic: the target has more than `n` independent translates, whereas every `n`-channel screen has a linear recurrence among `n+1` translates.

It also sharpens the WI-212 boundary. Fixed finite *samples* are algebraically screenable, but a full fixed natural interval cannot be screened with fixed finite **complexity**. Any successful continuum screen must have

\[
\boxed{n(T)\to\infty.}
\tag{39}
\]

This is only a qualitative complexity charge. The constants `mu_n` and `delta_n` may decay rapidly with `n`; no lower bound uniform in growing `n` is asserted. In particular, this finding does not rule out logarithmic, polylogarithmic, or slower-growing screens. A separate construction may exploit that regime, and any such claim must be assessed on its own evidence and review state.

Nor does (38) prove that an actual zeta bow is impossible. As in WI-213 and WI-195, the full explicit formula includes complementary zeros, pole/trivial terms, contour terms and the structured prime-side source subtraction. A large selected residue can be cancelled by a large complementary source vector unless one proves the missing diagonal-scale upper bound for the **full** source-fixed error. The theorem therefore constrains the architecture of any sparse defect-to-zero bootstrap; it does not close RH.

## 7. Prior art and novelty audit

The finite-dimensional translation principle is classical. Anselone and Korevaar, *Translation invariant subspaces of finite dimension*, Proc. Amer. Math. Soc. **15** (1964), 747--752, DOI `10.1090/S0002-9939-1964-0169048-7`, characterize finite-dimensional translation-invariant spaces by exponential polynomials. Finite-rank Hankel/Prony theory gives the same structural vocabulary from the recurrence side; modern summaries include Plonka, *Prony methods for recovery of structured functions*, GAMM-Mitteilungen **37** (2014), 239--258. The sinc Fourier representation and Fourier uniqueness used in (15)--(19) are classical.

The proof above does not require those theorems as black boxes: the only screen-rank input is the elementary `n` by `n+1` dependence (9), and the target separation is proved directly by Fourier uniqueness. A targeted prior-art search around fixed-rank exponential approximation, finite-dimensional translate spaces, Prony/Hankel rank, sinc approximation, Gallagher mean squares and zeta off-line screening found the classical finite-rank framework but no source asserting this particular uniform fixed-channel separation for a zeta bow or its source-fixed Gallagher consequence. Absence from that search is not used as a priority claim.

## Research consequence

The continuum route now has a clean complexity trichotomy. WI-212 says finitely many reciprocal samples do not force fresh defect. WI-213 says the exact WI-211 two-pair screen leaves a natural-scale continuum residue. WI-215 removes the ansatz dependence: **every uniformly bounded screen population leaves such a residue on any one fixed natural harmonic slab.**

The next useful question is therefore quantitative rather than merely topological: how fast must the effective translation rank grow before the smallest target-translate Gram eigenvalue `mu_n` becomes small enough to permit diagonal-scale screening? Any RH-facing bootstrap based on continuum coercivity must either obtain a lower bound on `mu_n` strong enough to charge a growing screen, couple screen rank to radial/count cost, or invoke genuinely source-specific arithmetic that forbids the required growing exponential family. Merely trying a different fixed finite collection of off-line pairs is now closed.