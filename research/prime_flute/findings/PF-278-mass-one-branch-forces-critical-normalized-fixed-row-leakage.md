# PF-278 — mass-one branch forces critical normalized fixed-row leakage

**Status:** `EXACT-DERIVED + BRANCH-TO-ENDPOINT-TRANSFER + JACOBI-COEFFICIENT-ASYMPTOTIC + NORMALIZED-FIXED-ROW-OBSTRUCTION + ROUTE-CLOSURE`.

[[research/prime_flute/findings/PF-275-mass-one-continuum-forbids-supercritical-raw-source-fixed-row-leakage|PF-275]] proves that the raw square-root source has no supercritical fixed-row leakage exponent. [[research/prime_flute/findings/PF-276-robin-normalization-is-inverse-positive-and-cannot-zero-the-fixed-axis-threshold-moment|PF-276]] then shows that the noncommuting Robin normalization cannot manufacture an exact zero of the mass-one threshold functional, and [[research/prime_flute/findings/PF-277-robin-source-has-two-strip-analyticity-and-a-nonremovable-mass-one-branch|PF-277]] upgrades that functional statement to a genuine nonremovable square-root Fourier branch at `xi=±i`.

The remaining question in the accepted Robin clue was whether that branch actually controls the large corridor coefficients. It does. Combining the positive small-mass Green continuum of [[research/prime_flute/findings/PF-273-seam-square-root-is-a-complete-bernstein-green-continuum-with-mass-one-edge|PF-273]] with PF-277's analytic source gives an explicit complete-axis tail

\[
(U^*g_w(L)z^{(i)})(\tau)
\sim
-C_\pm e^{-|\tau|}|\tau|^{-3/2}.
\]

After undoing the compactification this becomes an endpoint singularity

\[
\theta^{1/2}\bigl(\log(2/\theta)\bigr)^{-3/2}.
\]

A direct Jacobi/Gegenbauer coefficient calculation, using a terminating Pfaff--Saalschutz sum followed by the Mellin representation of the inverse logarithm, transfers that endpoint law to the exact corridor basis. For each fixed output row, the **fully Robin-normalized** source has the sharp shell scale

\[
\boxed{
\|P_iB_wE_N\|
\asymp
N^{-1}(\log N)^{-3/2}.
}
\]

The logarithm is a real gain over the bare critical `N^{-1}` envelope, but it is not any fixed power. Therefore every `q>1` estimate required by the PF-271 supercritical low-output gate fails already on one fixed row. The accepted fixed-axis Robin-homotopy leakage route is consequently closed before shear, corridor transport, or canonical-tail uniformity enter.

## Claim

Fix `r,s>0`, put `w=rs`, and work in one parity sector `epsilon in {0,1}`. Write

\[
\varphi_j=e_{2j+\varepsilon},
\qquad
E_N=\sum_{N\le j<2N}|\varphi_j\rangle\langle\varphi_j|,
\qquad
P_i=|\varphi_i\rangle\langle\varphi_i|.
\tag{1}
\]

Use PF-276's normalized source vector

\[
u^{(i)}=(I+R)^{-1}\varphi_i,
\qquad
z^{(i)}=A^{-1/4}u^{(i)},
\tag{2}
\]

and its strictly positive threshold moment

\[
T_i^{(\varepsilon)}>0.
\tag{3}
\]

PF-257/PF-276 give the physical fixed-axis Robin injection

\[
B_w^*\varphi_i
=s^{-1/2}g_w(L)z^{(i)},
\qquad
g_w(\lambda)=\sqrt{\sqrt\lambda\tanh(w\sqrt\lambda)}.
\tag{4}
\]

Let

\[
\alpha=\frac{1+\sqrt5}{2},
\qquad
\beta=\alpha-\frac12=\frac{\sqrt5}{2}.
\tag{5}
\]

Then, along the matching parity,

\[
\boxed{
\langle e_n,g_w(L)z^{(i)}\rangle
=
-\frac{\beta\sqrt w\,T_i^{(\varepsilon)}}{\sqrt{2\pi}}
\,n^{-3/2}(\log n)^{-3/2}
\left(1+O\!\left(\frac1{\log n}\right)\right),
}
\tag{6}
\]

as `n -> infinity`, `n congruent epsilon (mod 2)`. Opposite-parity coefficients vanish exactly. Hence

\[
\boxed{
\langle\varphi_i,B_w\varphi_j\rangle
=
-\frac{\beta\sqrt r\,T_i^{(\varepsilon)}}{\sqrt{2\pi}}
(2j+\varepsilon)^{-3/2}
\bigl(\log(2j+\varepsilon)\bigr)^{-3/2}
\left(1+O\!\left(\frac1{\log j}\right)\right).
}
\tag{7}
\]

Consequently

\[
\boxed{
N(\log N)^{3/2}\|P_iB_wE_N\|
\longrightarrow
\frac{\sqrt3}{8}
\frac{\beta\sqrt r\,T_i^{(\varepsilon)}}{\sqrt{2\pi}}
>0.
}
\tag{8}
\]

In particular, for every `q>1`,

\[
\boxed{
N^q\|P_iB_wE_N\|\longrightarrow\infty.
}
\tag{9}
\]

Any polynomial, logarithmic, or fixed low-output window that eventually contains `P_i` therefore also fails an `O(N^{-q})` bound for every `q>1`.

## 1. The small-mass Green continuum gives an exact complete-axis tail

PF-273 gives the complete-Bernstein measure of `g_w` and, at the lower edge,

\[
 t\,\frac{d\nu_w}{dt}(t)
=
\frac{\sqrt w}{\pi}t^{1/2}(1+O(t)),
\qquad t\downarrow0.
\tag{10}
\]

PF-274 identifies

\[
L=U(1-\partial_\tau^2)U^*,
\qquad
\tau=\log\tan\frac\theta2,
\tag{11}
\]

and PF-277 proves, for

\[
Z_i(\tau):=(U^*z^{(i)})(\tau),
\tag{12}
\]

that

\[
Z_i(\tau)=O(e^{-2|\tau|}),
\qquad
\widehat Z_i(-i)=T_i^{(\varepsilon)},
\qquad
\widehat Z_i(i)=(-1)^\varepsilon T_i^{(\varepsilon)}.
\tag{13}
\]

For `t>=0` put `mu(t)=sqrt(1+t)`. The complete-axis resolvent has kernel

\[
(1-\partial_\tau^2+t)^{-1}(\tau,y)
=\frac{e^{-\mu(t)|\tau-y|}}{2\mu(t)}.
\tag{14}
\]

Choose a fixed small `t_0>0` with `mu(t_0)<2`. Equation (13) then gives, uniformly for `0<=t<=t_0`,

\[
((L+t)^{-1}Z_i)(\tau)
=
\frac{e^{-\mu\tau}}{2\mu}\widehat Z_i(i\mu)
+O(e^{-2\tau})
\qquad(\tau\to+\infty),
\tag{15}
\]

and

\[
((L+t)^{-1}Z_i)(\tau)
=
\frac{e^{\mu\tau}}{2\mu}\widehat Z_i(-i\mu)
+O(e^{2\tau})
\qquad(\tau\to-\infty).
\tag{16}
\]

In the Stieltjes representation

\[
g_w(L)=\int_0^\infty L(L+t)^{-1}\,\nu_w(dt),
\tag{17}
\]

the local identity part of the small-`t` integral inherits the `e^{-2|tau|}` source decay. The nonlocal part is `-t(L+t)^{-1}`. Since

\[
\mu(t)=1+\frac t2+O(t^2),
\qquad
\widehat Z_i(i\mu(t))=(-1)^\varepsilon T_i^{(\varepsilon)}+O(t),
\tag{18}
\]

Watson's lemma applied to (10), (15), and (18) yields

\[
\boxed{
(U^*g_w(L)z^{(i)})(\tau)
=
-\frac{\sqrt w\,(-1)^\varepsilon T_i^{(\varepsilon)}}{\sqrt{2\pi}}
 e^{-\tau}\tau^{-3/2}
\left(1+O(\tau^{-1})\right)
}
\tag{19}
\]

as `tau -> +infinity`. Similarly,

\[
\boxed{
(U^*g_w(L)z^{(i)})(\tau)
=
-\frac{\sqrt w\,T_i^{(\varepsilon)}}{\sqrt{2\pi}}
 e^{\tau}|\tau|^{-3/2}
\left(1+O(|\tau|^{-1})\right)
}
\tag{20}
\]

as `tau -> -infinity`.

The constant is explicit because

\[
\int_0^\infty t^{1/2}e^{-t|\tau|/2}\,dt
=\Gamma(3/2)\left(\frac2{|\tau|}\right)^{3/2}.
\tag{21}
\]

The part of the Stieltjes measure bounded away from `t=0` has `mu>=sqrt(1+t_0)>1` and therefore lies behind a strictly faster exponential scale. Equivalently, after PF-277 the only singularities at imaginary height one are the two nonremovable mass-one branch germs; the source transform is holomorphic through a larger strip. Thus (19)--(20) isolate the leading tail rather than only one contribution to it.

## 2. Compactification turns the mass-one tail into a logarithmic square-root endpoint

PF-238/PF-274 use

\[
(UF)(\theta)=\sin^{-1/2}\theta\,F(\tau(\theta)).
\tag{22}
\]

As `theta -> 0`,

\[
e^\tau=\tan(\theta/2)=\frac\theta2(1+O(\theta^2)),
\qquad
|\tau|=\log\frac2\theta+O(\theta^2).
\tag{23}
\]

Combining (20), (22), and (23) gives

\[
\boxed{
g_w(L)z^{(i)}(\theta)
=A_i\,\theta^{1/2}
\left(\log\frac2\theta\right)^{-3/2}
\left(1+O\!\left(\frac1{\log(2/\theta)}\right)\right),
}
\tag{24}
\]

where

\[
A_i=-\frac{\sqrt w\,T_i^{(\varepsilon)}}{2\sqrt{2\pi}}\ne0.
\tag{25}
\]

At the other endpoint, with `delta=pi-theta`, equations (19) and (22) give

\[
g_w(L)z^{(i)}(\pi-\delta)
=(-1)^\varepsilon A_i\,\delta^{1/2}
\left(\log\frac2\delta\right)^{-3/2}
\left(1+O\!\left(\frac1{\log(2/\delta)}\right)\right).
\tag{26}
\]

Thus the two endpoint amplitudes have exactly the parity relation required to reinforce, rather than cancel, in the matching corridor sector.

## 3. The endpoint law has an exact Gegenbauer coefficient transfer

The normalized corridor basis is

\[
e_n(\theta)
=h_n^{-1/2}\sin^\alpha\theta\,C_n^{(\alpha)}(\cos\theta),
\tag{27}
\]

with

\[
h_n=
\frac{\pi2^{1-2\alpha}\Gamma(n+2\alpha)}
{n!(n+\alpha)\Gamma(\alpha)^2}.
\tag{28}
\]

Put `beta=alpha-1/2`. The exact Jacobi relation is

\[
C_n^{(\alpha)}(x)
=\frac{(2\alpha)_n}{(\alpha+1/2)_n}
P_n^{(\beta,\beta)}(x).
\tag{29}
\]

For `Re rho>-1`, the terminating hypergeometric integral and Pfaff--Saalschutz summation give

\[
\begin{aligned}
I_n(\rho)
&:=\int_{-1}^1(1-x)^\rho(1+x)^\beta
P_n^{(\beta,\beta)}(x)\,dx\\
&=2^{\rho+\beta+1}B(\rho+1,\beta+1)
\frac{(\beta+1)_n}{n!}
\frac{(\beta-\rho)_n}{(\beta+\rho+2)_n}.
\end{aligned}
\tag{30}
\]

Combining (28)--(30) and Stirling's formula gives the normalized one-endpoint power law

\[
h_n^{-1/2}
\frac{(2\alpha)_n}{(\alpha+1/2)_n}
I_n(\rho)
=
K_\beta(\rho)
 n^{\beta-2\rho-3/2}(1+O(n^{-1})),
\tag{31}
\]

where

\[
K_\beta(\rho)
=2^{\rho+1}\frac{\Gamma(\rho+1)}{\Gamma(\beta-\rho)}.
\tag{32}
\]

The physical endpoint exponent in (24) corresponds to

\[
\rho_0=\frac\beta2.
\tag{33}
\]

The logarithm can be inserted without a Tauberian guess. For `0<1-x<2`,

\[
\left(\log\frac2{1-x}\right)^{-3/2}
=
\frac1{\Gamma(3/2)}
\int_0^\infty t^{1/2}
\left(\frac{1-x}{2}\right)^t dt.
\tag{34}
\]

After a fixed endpoint cutoff, substitute `rho=rho_0+t` into (31). The integral is concentrated at `t=O(1/log n)`, so (32) may be frozen at `rho_0`; moreover

\[
\frac1{\Gamma(3/2)}
\int_0^\infty t^{1/2}e^{-t(2\log n+\log2)}dt
\sim 2^{-3/2}(\log n)^{-3/2}.
\tag{35}
\]

The elementary conversion from `theta` to `x=cos theta` contributes the complementary powers of two. Since

\[
K_\beta(\beta/2)=\beta 2^{\beta/2},
\tag{36}
\]

a single endpoint with amplitude `A` in the normalization of (24) contributes

\[
\boxed{
\beta A\,n^{-3/2}(\log n)^{-3/2}
\left(1+O((\log n)^{-1})\right).
}
\tag{37}
\]

The `O(1/log)` correction in (24) gives one further inverse logarithm under the same Mellin argument; extra positive endpoint powers are polynomially smaller. Away from the endpoints the fixed-axis source is smooth by local elliptic functional calculus for `A`, `L`, and the coercive order-zero normalization `I+R`; after a cutoff, repeated Sturm--Liouville integration by parts makes the interior contribution smaller than (37). Thus no unaccounted interior term occurs at the same scale.

Because

\[
e_n(\pi-\theta)=(-1)^n e_n(\theta),
\tag{38}
\]

the endpoint amplitude (26) makes the two copies of (37) add for `n congruent epsilon (mod 2)` and cancel for the opposite parity, which is already exactly absent from the operator. Equations (25) and (37) therefore give (6).

## 4. The normalized Robin row is critical up to an inverse logarithm

Multiply (6) by the exact `s^{-1/2}` factor in (4) and use `w=rs`. For `n=2j+epsilon`, this gives (7). The fixed-row shell norm is

\[
\|P_iB_wE_N\|^2
=\sum_{N\le j<2N}
|\langle\varphi_i,B_w\varphi_j\rangle|^2.
\tag{39}
\]

Since

\[
\sum_{N\le j<2N}j^{-3}
\sim\frac{3}{8}N^{-2},
\tag{40}
\]

(7) implies the positive limit (8). This is stronger than merely showing a nonzero branch germ: it identifies the exact leakage currency consumed by PF-271.

The result sits precisely at the critical power. The normalization does improve the fixed-row mass-one leakage by the slowly varying factor `(log N)^(-3/2)`, but for every `q>1`,

\[
N^qN^{-1}(\log N)^{-3/2}\to\infty.
\tag{41}
\]

Therefore neither PF-271's sublinear low-output window nor its logarithmic window can satisfy the required supercritical polynomial decay. A single fixed row already lies inside both windows and witnesses failure.

## 5. Consequence for the Robin-homotopy route

The accepted clue `CLUE-robin-homotopy-separated-poisson-shear-estimate` isolated one final fixed-axis escape after PF-275--PF-277: perhaps the genuine mass-one branch would fail to control discrete corridor coefficients strongly enough for the normalization to recover an exponent above one.

Equations (6)--(9) close that escape. The actual normalized source has a nonzero mass-one coefficient tail and its fixed-row shell norm is exactly critical up to an inverse logarithm. Thus the PF-271 low-output hypothesis fails **before** PF-255/PF-256 shear/corridor transport and before any canonical-tail uniformity question. Those later steps cannot repair a fixed-axis estimate that is already false.

This is a route closure, not a global negative theorem about Prime Flute. PF-243's separated source-to-bulk strategy could only survive through a different factorization or estimate that does not require a supercritical polynomial low-output bound on this normalized conversion. The present result says that the specific PF-269--PF-277 attempt to obtain that bound from Robin normalization is exhausted.

## 6. Prior art and novelty audit

Every analytic ingredient used above is classical. Watson's lemma for Laplace integrals is standard asymptotic analysis; the terminating `3F2(1)` evaluation in (30) is the Pfaff--Saalschutz summation; and Jacobi/Gegenbauer coefficient decay for algebraic and logarithmic endpoint singularities has an extensive approximation-theory literature. In particular:

- Shuhuang Xiang, *Convergence Rates on Spectral Orthogonal Projection Approximation for Functions of Algebraic and Logarithmatic Regularities*, SIAM Journal on Numerical Analysis **59** (2021), 1374--1398, DOI `10.1137/20M134407X`, derives optimal Jacobi/Gegenbauer coefficient decay from Hilb-type formulas for algebraic/logarithmic singularities. It is methodological prior art; the exact negative fractional logarithm and PF normalization above are not imported from that paper.
- Haiyong Wang, *On the Optimal Estimates and Comparison of Gegenbauer Expansion Coefficients*, SIAM Journal on Numerical Analysis **54** (2016), 1557--1581, DOI `10.1137/15M102232X`, provides broader prior art for sharp Gegenbauer coefficient estimates and endpoint singularities.
- Cao--Li--Lin's 2019 continuous-Hahn asymptotics, already audited in PF-275, concern large-degree continuous Hahn polynomials; the present proof instead uses the exact PF Gegenbauer/Jacobi endpoint integral after PF-274's representation has identified the branch.

Standard local elliptic regularity for complex/fractional powers supplies the cutoff-interior smoothness used after (37); no novelty is claimed for that step. The classical reference is R. T. Seeley, *Complex powers of an elliptic operator*, Proc. Symp. Pure Math. **10** (1967), 288--307.

No novelty is claimed for Watson asymptotics, Pfaff--Saalschutz, Mellin representations, Jacobi/Gegenbauer asymptotics, continuous-Hahn polynomials, or elliptic complex powers. The project-specific contribution is the exact chain from PF-273's mass-one complete-Bernstein edge, through PF-276/PF-277's nonzero normalized threshold source, to the explicit fixed-row asymptotic (7) and the PF-271 route closure (8)--(9).

## 7. Boundaries and adversarial checks

1. **Fixed axis and fixed seam parameters.** Constants depend on `r,s,i` and parity. This is enough for the negative conclusion: a uniform supercritical estimate cannot hold if it already fails for one fixed admissible parameter choice and one fixed output row.
2. **The logarithmic gain is retained.** The theorem does not replace the tail by a bare `N^{-1}` slogan. Robin normalization leaves the sharper `N^{-1}(log N)^{-3/2}` shell scale, but that is still weaker than every fixed power `N^{-q}`, `q>1`.
3. **Both endpoints are required.** The parity sign in PF-277 is preserved. For the matching parity, the `theta=0` and `theta=pi` contributions reinforce; dropping the sign would give the wrong constant and could create a fictitious cancellation.
4. **Degree versus parity-shell index is tracked.** Equation (6) uses the full Gegenbauer degree `n`; equations (7)--(8) substitute `n=2j+epsilon`. The factor `sqrt(3)/8` in (8) includes this conversion and the dyadic sum in (40).
5. **No branch-distance heuristic is used as the coefficient theorem.** PF-277's branch germ is first converted to the physical endpoint law by the exact one-dimensional massive Green kernel and PF-273's positive lower-edge density. The corridor coefficient is then computed by (30)--(37).
6. **Interior regularity is not allowed to manufacture the leading term.** The asymptotic is localized to the two endpoints. Standard local elliptic regularity and repeated integration by parts make compact interior pieces lower order; a failure of that regularity for the actual fixed-axis operator would invalidate the stated remainder and is an explicit audit target.
7. **No downstream global conclusion.** The result does not establish or refute a weak-trace theorem by another route, physical `P/H` recoupling, finite-pant reassembly, neighboring-cell control, scattering/determinants, prime/control separation, a zeta-zero statement, or RH.

The finding is falsified if PF-273's lower-edge density (10) is wrong, PF-276/PF-277's nonzero threshold values (13) fail, the Green-kernel tail (15)--(16) does not hold uniformly at small mass, the exact Jacobi moment (30) or normalization (31)--(37) is incorrect, or the local interior regularity required to isolate the endpoint contribution fails.

## Decisive next test

Do not spend another pass trying to obtain a supercritical PF-271 leakage exponent from the fixed-axis normalized Robin source: (8)--(9) rule it out. Mark the accepted Robin leakage clue negatively resolved for this route.

Any continuation of the PF-243 program must change the proof currency rather than sharpen the same estimate — for example, find a composed cancellation that acts only after coupling to the far propagator and is not implied by an operator-norm high-to-low bound, or return to another still-open local clue whose decisive test does not assume the now-false supercritical normalized-source estimate. Such alternatives require a new derivation and are not asserted by PF-278.