# PC-195 — quadratic reciprocal prime-shell zeros have universal boundary-layer scales

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for rescuing the quadratic reciprocal Prime-Circle Fourier zeros through their quantitative locations.

PC-194 proves that the canonical quadratic reciprocal amplitude already destroys the zero-free prime-power classifier: sufficiently large prime shells acquire at least two real Fourier zeros. It leaves open whether the **locations** of those zeros might nevertheless carry a stable arithmetic spectral signal.

For the prime shell, that possibility already has a strong negative answer. The first positive zero has an exact universal asymptotic scale

\[
\boxed{
\tau_p
\sim
c_*p^{3/4},
\qquad
c_*
=
\left(\frac{3}{\zeta(2)+\zeta(3)}\right)^{1/4}.
}
\tag{1}
\]

A second, asymptotically separated zero occurs on the ordinary refinement scale `Theta(p)`. More precisely, the entire linear-scale boundary layer has a universal limiting Fourier profile

\[
\boxed{
 p^3\widehat H_p(cp)\longrightarrow K(c)
 \qquad(c>0),
}
\tag{2}
\]

where

\[
H_p(x)
:=
1-\left(\frac{1-e^{-|x|}}{1-e^{-p|x|}}\right)^2
=-G_{p,2}(x)
\tag{3}
\]

and

\[
\boxed{
K(c)
=
2\int_0^\infty
u^2\left[1-(1-e^{-u})^{-2}\right]\cos(cu)\,du.
}
\tag{4}
\]

The limit satisfies

\[
K(0)=-4\bigl(\zeta(2)+\zeta(3)\bigr)<0,
\qquad
K(c)=\frac{2}{c^2}+o(c^{-2})>0
\quad(c\to\infty).
\tag{5}
\]

Hence fixed constants `0<c_-<c_+<infinity` exist such that every sufficiently large prime shell has a zero in `(c_-p,c_+p)`. This zero is distinct from the first one in (1), since `p^{3/4}=o(p)`.

Thus the first two forced sign changes in the source-natural quadratic reciprocal profile are organized by **two endpoint/refinement boundary scales**, not by the nontrivial zero set of zeta. The only zeta values entering the first scale are the fixed positive constants `zeta(2)` and `zeta(3)` produced by an elementary boundary-layer moment. This closes the most immediate quantitative-zero-location repair left by PC-194.

## 1. Exact outer profile and negative refinement layer

Write, as in PC-194,

\[
h(x)=2e^{-|x|}-e^{-2|x|},
\tag{6}
\]

so that

\[
\widehat h(t)
=
\frac{12}{(1+t^2)(4+t^2)}>0.
\tag{7}
\]

Then

\[
H_p=h+D_p,
\tag{8}
\]

with

\[
D_p(x)
=(1-e^{-|x|})^2
\left[1-(1-e^{-p|x|})^{-2}\right]
\le0.
\tag{9}
\]

The sign of `D_p` is useful because it turns its Fourier-zero control into an `L^1` estimate rather than an oscillatory estimate:

\[
|\widehat D_p(t)|
\le \|D_p\|_1
=-\widehat D_p(0).
\tag{10}
\]

The boundary-layer calculation of PC-194 at zero frequency gives

\[
\boxed{
p^3\|D_p\|_1
\longrightarrow
A,
\qquad
A:=4\bigl(\zeta(2)+\zeta(3)\bigr).
}
\tag{11}
\]

The scale `p^{-3}` is therefore the total available negative Fourier mass coming from the refinement layer.

## 2. The smallest positive zero is asymptotic to `c_* p^(3/4)`

Define

\[
c_*:=\left(\frac{12}{A}\right)^{1/4}
=
\left(\frac{3}{\zeta(2)+\zeta(3)}\right)^{1/4}.
\tag{12}
\]

Let `epsilon>0` be fixed and smaller than `c_*`, and put

\[
T_-=(c_*-\epsilon)p^{3/4},
\qquad
T_+=(c_*+\epsilon)p^{3/4}.
\tag{13}
\]

Because (7) is decreasing for `t>=0`, equations (8)--(11) give, uniformly for `0<=t<=T_-`,

\[
\widehat H_p(t)
\ge
\widehat h(T_-)-\|D_p\|_1.
\tag{14}
\]

Multiplying by `p^3`,

\[
 p^3\widehat h(T_-)
\longrightarrow
\frac{12}{(c_*-\epsilon)^4}
>
A
\tag{15}
\]

whereas `p^3\|D_p\|_1 -> A`. Hence

\[
\widehat H_p(t)>0
\qquad
(0\le t\le T_-)
\tag{16}
\]

for all sufficiently large primes.

On the other side, PC-194 proves for every fixed `c>0`

\[
 p^3\widehat H_p(cp^{3/4})
\longrightarrow
\frac{12}{c^4}-A.
\tag{17}
\]

At `c=c_*+epsilon` this limit is strictly negative, so

\[
\widehat H_p(T_+)<0
\tag{18}
\]

for all sufficiently large primes. Since `\widehat H_p` is continuous, its smallest positive zero `tau_p` lies in `(T_-,T_+)`. Because `epsilon` was arbitrary,

\[
\boxed{
\frac{\tau_p}{p^{3/4}}
\longrightarrow c_*.
}
\tag{19}
\]

This is stronger than the existence argument in PC-194: the first sign change is asymptotically pinned to the balance between the universal `t^{-4}` outer tail and the `p^{-3}` negative refinement mass.

## 3. The second boundary regime is the full refinement scale `t=cp`

The same exact decomposition produces a different limit when the frequency resolves the refinement layer itself. Set

\[
t=cp,
\qquad c>0\text{ fixed}.
\tag{20}
\]

From (7),

\[
p^3\widehat h(cp)\longrightarrow0.
\tag{21}
\]

For `D_p`, evenness and the change of variables `u=px` give

\[
\begin{aligned}
p^3\widehat D_p(cp)
&=
2\int_0^\infty
\bigl[p(1-e^{-u/p})\bigr]^2
\left[1-(1-e^{-u})^{-2}\right]
\cos(cu)\,du.
\end{aligned}
\tag{22}
\]

The elementary bound

\[
0\le p(1-e^{-u/p})\le u
\tag{23}
\]

and the integrability of

\[
u^2\left[(1-e^{-u})^{-2}-1\right]
\tag{24}
\]

permit dominated convergence. Therefore

\[
\boxed{
 p^3\widehat H_p(cp)
\longrightarrow K(c)
}
\tag{25}
\]

with `K` as in (4). The same domination gives uniform convergence on every compact `c`-interval contained in `(0,infinity)`.

The limiting profile is therefore not a fitted numerical object. It is the exact Fourier transform of the rescaled refinement boundary layer.

## 4. The linear-scale limit must cross back to positive sign

Expanding

\[
(1-e^{-u})^{-2}
=
\sum_{m\ge0}(m+1)e^{-mu}
\tag{26}
\]

gives the absolutely convergent representation

\[
\boxed{
K(c)
=-4\operatorname{Re}
\sum_{m\ge1}
\frac{m+1}{(m-ic)^3}.
}
\tag{27}
\]

Equivalently, in standard polygamma notation,

\[
K(c)
=-4\operatorname{Re}
\left[
\psi^{(1)}(1-ic)
-
\frac{1+ic}{2}\psi^{(2)}(1-ic)
\right].
\tag{28}
\]

At `c=0`, (27) gives

\[
\boxed{
K(0)
=-4\sum_{m\ge1}\left(\frac1{m^2}+\frac1{m^3}\right)
=-A<0.
}
\tag{29}
\]

To determine the opposite end, write

\[
g(u)
:=
2u^2\left[1-(1-e^{-u})^{-2}\right].
\tag{30}
\]

Near zero,

\[
g(u)=-2-2u+O(u^2),
\tag{31}
\]

and at infinity `g` and all derivatives needed below decay exponentially. Thus `g''` is integrable. Two integrations by parts in

\[
K(c)=\int_0^\infty g(u)\cos(cu)\,du
\tag{32}
\]

give

\[
K(c)
=-\frac{g'(0)}{c^2}
-
\frac1{c^2}\int_0^\infty g''(u)\cos(cu)\,du.
\tag{33}
\]

Since `g'(0)=-2`, the Riemann--Lebesgue lemma yields

\[
\boxed{
K(c)=\frac2{c^2}+o(c^{-2})
\qquad(c\to\infty).
}
\tag{34}
\]

So `K` is negative for all sufficiently small positive `c` and positive for all sufficiently large `c`. Choose fixed constants `c_-<c_+` in those two sign regions. Equation (25) then gives

\[
\widehat H_p(c_-p)<0,
\qquad
\widehat H_p(c_+p)>0
\tag{35}
\]

for every sufficiently large prime. Hence there is at least one zero

\[
\boxed{
\sigma_p\in(c_-p,c_+p).
}
\tag{36}
\]

Because `tau_p=Theta(p^{3/4})`, this `sigma_p=Theta(p)` is a genuinely distinct second zero for large `p`.

No uniqueness claim for the linear-scale zero is needed or made here. The universal function `K` could in principle have additional sign changes; any such zeros would still belong to the same classical refinement-layer profile (27), not to a newly introduced zeta spectral divisor.

## 5. Prime powers inherit the same scales by exact dilation

For `n=p^k`, PC-194 records the exact cyclotomic identity

\[
H_{p^k,2}(x)
=H_{p,2}(p^{k-1}x),
\tag{37}
\]

and therefore

\[
\widehat H_{p^k,2}(t)
=
p^{1-k}
\widehat H_{p,2}(p^{1-k}t).
\tag{38}
\]

Every Fourier zero is simply multiplied by `p^{k-1}`. In particular, as the base prime tends to infinity,

\[
\boxed{
\tau_{p^k}
\sim
c_*p^{k-1/4}
=
c_*\,p^k p^{-1/4},
}
\tag{39}
\]

while the separated refinement-layer zero satisfies

\[
\boxed{
\sigma_{p^k}=\Theta(p^k).
}
\tag{40}
\]

Repeated-prime depth therefore does not create a new spectral law; it only dilates the two prime-shell boundary scales.

## 6. Prior-art and novelty audit

The analytic mechanisms used above are classical. The large-frequency estimate (34) is ordinary endpoint Fourier asymptotics obtained by repeated integration by parts, and the passage from a rescaled boundary layer to a limiting cosine transform is standard dominated-convergence analysis. The polygamma form (28) is the standard summation of shifted reciprocal powers. No novelty is claimed for any of those tools.

A directed literature search around continuous Fourier transforms of `Phi_p(e^{-x})^{-1}`, reciprocal cyclotomic amplitudes, exponent-dependent cyclotomic Fourier zeros, and boundary-layer zero scaling did not locate the specific limits (19) or (25). Nearby cyclotomic Fourier literature concerns finite Fourier analysis of polynomial values at roots of unity rather than the radial continuous transform studied here. This absence is only a bounded novelty check, not a historical novelty claim.

The Prime-Circle-specific contribution is the exact architecture diagnosis: once the quadratic reciprocal amplitude is chosen, its first zero is fixed by the balance of the elementary outer tail with the `p^{-3}` refinement mass, while the later sign recovery is governed by the universal rescaled layer `K`. The constants `zeta(2)+zeta(3)` in (12) and the polygamma values in (28) are classical transform moments; neither introduces the nontrivial zero set, the completed zeta functional equation, or a critical-line symmetry.

## 7. Consequence for the live Prime-Circle frontier

PC-194 left two possible scalar reactions to the failure of the zero-free classifier: identify a geometry-forced reciprocal exponent, or seek a stable quantitative law in the resulting zero locations. The exponent `alpha=2` is the most natural energy-like higher reciprocal power, so it is the first place where the quantitative repair should work if this scalar family contains deeper arithmetic spectral information.

Equations (19) and (25)--(36) show instead that the first two sign-change scales are already explained by ordinary radial boundary geometry. The first is `p^{3/4}` with the fixed constant (12); the next is the refinement scale `p` with universal profile (27). Prime powers merely dilate both scales by (38).

This does **not** classify `1<alpha<2`, prove uniqueness or simplicity of every Fourier zero, or exclude a different geometry-forced operator outside the reciprocal scalar family. It does close the immediate claim that the quadratic prime-shell zero locations themselves expose a new zeta/RH spectrum. A surviving route still needs information not reducible to this one-shell boundary-layer competition: source-forced cross-shell coupling, a genuinely second carrier, nonlocal angular/radial interaction before scalarization, singular boundary data with new structure, or the global nonlinear uniformization sector.

## Audit / falsification tests

The first-zero asymptotic can be falsified by a sequence of primes for which the smallest positive zero fails (19). The proof reduces this to two explicit checks: the `L^1` mass limit (11) and the mesoscopic limit (17), both derived from the exact decomposition (8)--(9).

The linear-scale claim can be falsified by failure of the dominated-convergence limit (25), by an error in the series identity (27), or by failure of the endpoint expansion (31). Each is independent of any numerical root finder or unproved statement about zeta zeros.