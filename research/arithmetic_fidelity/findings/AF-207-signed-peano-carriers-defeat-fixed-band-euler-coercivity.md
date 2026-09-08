# AF-207 — Signed Peano carriers defeat fixed-band Euler coercivity

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-FIDELITY`, `SOURCE-REALIZABILITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-206 identifies higher-convex order, equivalently nonnegativity of the order-`m` Peano kernel, as the positive source cone on which one real Euler defect controls the entire fixed vertical band. That sign condition is load-bearing. Once normalized Peano carriers are allowed to change sign, the same finite band still gives a total-variation upper bound, but it has no uniform lower coercivity on the full signed carrier class.

Fix

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and retain the AF-206 Euler derivatives

\[
g_{m,\tau}(t)
:=(-1)^mF_{\sigma+i\tau}^{(m)}(t)
=(\sigma+i\tau)^m\sum_{k\ge1}k^{m-1}e^{-k(\sigma+i\tau)t},
\qquad |\tau|\le T.
\tag{1}
\]

Put

\[
h(t):=g_{m,0}(x)-g_{m,0}(t)>0\qquad(t>x).
\tag{2}
\]

For a finite signed Borel measure `beta` on `[x,\infty)` with

\[
\beta([x,\infty))=1,
\tag{3}
\]

and finite weighted variation, define

\[
V_h(\beta):=\int h(t)\,d|\beta|(t),
\tag{4}
\]

\[
R_h(\beta):=
\left|\int h(t)\,d\beta(t)\right|,
\tag{5}
\]

and the anchored fixed-band discrepancy

\[
D_T(\beta):=
\sup_{|\tau|\le T}
\left|
\int\bigl(g_{m,\tau}(t)-g_{m,\tau}(x)\bigr)\,d\beta(t)
\right|.
\tag{6}
\]

Then the pointwise comparison already proved in AF-206 implies a finite constant

\[
C=C(m,x,\sigma,T)
\tag{7}
\]

such that every such signed carrier satisfies

\[
\boxed{
R_h(\beta)\le D_T(\beta)\le C V_h(\beta).
}
\tag{8}
\]

For a positive probability carrier, `|beta|=beta` and therefore

\[
R_h(\beta)=V_h(\beta),
\tag{9}
\]

which is exactly the one-sign mechanism behind AF-206. For a signed carrier, however, the ratio

\[
\kappa_h(\beta):=
\frac{R_h(\beta)}{V_h(\beta)}\in[0,1]
\tag{10}
\]

can collapse to zero because positive and negative Peano mass cancel.

The failure is not confined to the real-axis observation. For every prescribed `A>0` there is a sequence of smooth compactly supported signed densities `b_n` on `(x,\infty)` such that

\[
\int_x^\infty b_n(t)\,dt=1,
\tag{11}
\]

while

\[
\boxed{
D_T(b_n(t)dt)\longrightarrow0,
\qquad
V_h(b_n(t)dt)\longrightarrow A>0.
}
\tag{12}
\]

Thus no constant `c>0` can satisfy

\[
D_T(\beta)\ge c V_h(\beta)
\tag{13}
\]

on the full signed mass-one carrier class. A fixed Euler band can therefore become asymptotically blind to a nonvanishing amount of signed localization defect.

Moreover, these carriers are genuine Peano carriers of moment-matched probability source pairs. For every `b_n` in `(12)` there exist probability measures `mu_{-,n},mu_{+,n}` supported on `[x,\infty)` such that, with

\[
\nu_n:=\mu_{+,n}-\mu_{-,n},
\tag{14}
\]

one has

\[
\int u^j\,d\nu_n(u)=0,
\qquad j=0,\ldots,m-1,
\tag{15}
\]

and the normalized order-`m` Peano carrier of `nu_n` is exactly

\[
\beta_{\nu_n}(dt)=b_n(t)dt.
\tag{16}
\]

So the obstruction is not an artifact of enlarging the carrier space beyond realizable source differences. What fails is precisely the sign-definite/higher-convex structure used by AF-206.

## Derivation

### 1. The signed carrier always has an upper bound but only a cancellation-sensitive lower certificate

AF-206 proves the pointwise estimate

\[
|g_{m,\tau}(t)-g_{m,\tau}(x)|
\le C h(t)
\qquad(t\ge x,\ |\tau|\le T).
\tag{17}
\]

Integrating against total variation gives

\[
\begin{aligned}
D_T(\beta)
&\le
\sup_{|\tau|\le T}
\int
|g_{m,\tau}(t)-g_{m,\tau}(x)|\,d|\beta|(t)\\
&\le C\int h(t)\,d|\beta|(t)
=C V_h(\beta),
\end{aligned}
\tag{18}
\]

which proves the upper half of `(8)` without any positivity assumption.

At `tau=0`, however,

\[
g_{m,0}(t)-g_{m,0}(x)=-h(t),
\tag{19}
\]

so the band supremum contains the exact scalar value

\[
D_T(\beta)
\ge
\left|\int h\,d\beta\right|
=R_h(\beta).
\tag{20}
\]

For positive `beta`, `(20)` equals the total weighted mass `(4)`, giving AF-206's lower coercivity. For signed `beta`, it sees only the net weighted mass. Equation `(8)` therefore separates two quantities that positivity had identified: weighted size `V_h` and weighted signed resultant `R_h`.

### 2. A far-tail dipole defeats the entire fixed band

Choose a nonnegative smooth bump `q` with compact support in `(0,1)` and

\[
\int q(t)\,dt=1.
\tag{21}
\]

For `a>x` and `r>0`, let

\[
q_{a,r}(t):=r^{-1}q((t-a)/r).
\tag{22}
\]

Take sequences

\[
\varepsilon_n\downarrow0,
\qquad
y_n\to\infty,
\tag{23}
\]

with all three supports below disjoint, and define

\[
b_n(t)
:=
q_{x,\varepsilon_n}(t)
+M q_{y_n,1}(t)
-M q_{y_n+2,1}(t),
\tag{24}
\]

where `q_{x,epsilon}` is understood as any translated copy supported inside `(x,x+epsilon)` and

\[
M:=\frac{A}{2g_{m,0}(x)}.
\tag{25}
\]

The far pair has zero total mass, so `(11)` holds.

Because the fixed band has uniformly bounded derivative near the anchor, AF-206's derivative estimate gives

\[
\sup_{|\tau|\le T}
\left|
\int(g_{m,\tau}(t)-g_{m,\tau}(x))q_{x,\varepsilon_n}(t)dt
\right|
=O(\varepsilon_n).
\tag{26}
\]

For the far dipole, the anchor term cancels exactly because its total mass is zero. Also, from `(1)`,

\[
\sup_{|\tau|\le T}|g_{m,\tau}(t)|\longrightarrow0
\qquad(t\to\infty),
\tag{27}
\]

uniformly on the fixed band. Therefore

\[
\begin{aligned}
&\sup_{|\tau|\le T}
\left|
M\int g_{m,\tau}(t)
\bigl(q_{y_n,1}(t)-q_{y_n+2,1}(t)\bigr)dt
\right|\\
&\qquad\le
2M\sup_{|\tau|\le T,\ t\ge y_n}|g_{m,\tau}(t)|
\longrightarrow0.
\end{aligned}
\tag{28}
\]

Combining `(26)` and `(28)` proves the first limit in `(12)`.

On the other hand,

\[
h(t)\longrightarrow g_{m,0}(x)>0
\qquad(t\to\infty),
\tag{29}
\]

and the supports in `(24)` are disjoint. Hence

\[
\begin{aligned}
V_h(b_n(t)dt)
&=
\int h q_{x,\varepsilon_n}
+M\int h q_{y_n,1}
+M\int h q_{y_n+2,1}\\
&\longrightarrow
0+2M g_{m,0}(x)
=A,
\end{aligned}
\tag{30}
\]

which proves the second limit in `(12)`.

The mechanism is therefore exact: a unit positive carrier concentrates at the anchor while a zero-mass signed dipole escapes to a region where every fixed-band Euler observable has the same asymptotic value. The band forgets the dipole, but weighted total variation does not.

### 3. Every smooth signed carrier in the construction comes from a moment-flat probability pair

Let `b` be any one of the smooth compactly supported densities in `(24)` and define the finite signed measure

\[
d\lambda(t):=(-1)^m b^{(m)}(t)\,dt.
\tag{31}
\]

Repeated integration by parts, with no boundary terms because `b` is compactly supported inside `(x,\infty)`, gives

\[
\int t^j\,d\lambda(t)=0
\qquad(j=0,\ldots,m-1),
\tag{32}
\]

and

\[
\int t^m\,d\lambda(t)=m!\int b(t)dt=m!.
\tag{33}
\]

Distributionally,

\[
\frac{d^m}{dt^m}
\left[
\frac1{(m-1)!}
\int(u-t)_+^{m-1}\,d\lambda(u)
\right]
=(-1)^m\lambda,
\tag{34}
\]

and both the bracketed function and `b` vanish with their derivatives at infinity. Thus the Peano kernel of `lambda` is exactly

\[
K_\lambda(t)=b(t).
\tag{35}
\]

Since `lambda` has total mass zero, its Jordan positive and negative parts have equal mass

\[
a:=\lambda^+([x,\infty))
=\lambda^-([x,\infty))>0.
\tag{36}
\]

Define probability measures

\[
\mu_+:=a^{-1}\lambda^+,
\qquad
\mu_-:=a^{-1}\lambda^-.
\tag{37}
\]

Then `nu=mu_+-mu_-=a^{-1}lambda` satisfies the moment cancellations `(15)`, while

\[
K_\nu=a^{-1}b,
\qquad
\Delta_m:=\int t^m\,d\nu(t)=\frac{m!}{a}>0.
\tag{38}
\]

Therefore its normalized signed Peano carrier is

\[
\frac{m!}{\Delta_m}K_\nu(t)dt
=b(t)dt,
\tag{39}
\]

proving `(16)`.

The negative lobe in `(24)` ensures that these source pairs lie outside the higher-convex cone of AF-206. No arbitrary or nonrealizable carrier has been inserted by hand.

## Arithmetic Fidelity consequence

AF-206's positive Peano probability is not merely a convenient representation. Positivity converts the monotone real-axis Euler observation into a norm-like quantity because signed resultant and weighted variation coincide. Once sign is lost, those notions separate, and a far-tail zero-mass component can survive at order one in weighted variation while disappearing from every observable in a fixed Euler band.

This identifies a sharper preservation rule for later arithmetic applications:

\[
\boxed{
\text{moment cancellation alone is not enough; one needs sign coherence, tightness, or another source restriction that forbids invisible signed escape.}
}
\tag{40}
\]

In particular, replacing the positive higher-convex carrier by an arbitrary signed Peano kernel does not extend AF-206. It destroys the lower recovery theorem. Any proposed prime-sensitive source class outside the higher-convex cone must therefore supply an independent anti-cancellation mechanism before fixed-band Euler observations can certify localization.

This is an instance of the line's general compression question. The compressed observable family is asymptotically constant on a remote region, so a signed zero-mass direction lies asymptotically in its kernel. Positivity had removed that direction from the admissible cone.

## Prior art and novelty assessment

The underlying ingredients are classical, and no novelty is claimed for Peano-kernel representation, total-variation error bounds, or the usefulness of one-sign kernels.

- Classical Peano-kernel theory represents polynomial-annihilating linear functionals by integration against their Peano kernel and bounds the functional by an `L^1`/total-variation norm of that kernel.
- David Ferguson, **“Sufficient Conditions for Peano's Kernel to Be of One Sign,”** *SIAM Journal on Numerical Analysis* 10(6) (1973), 1047--1054, DOI `10.1137/0710087`, explicitly treats one-sign Peano kernels as the condition enabling sharper error estimates for interpolation/quadrature functionals.
- AF-206 already audits the higher-convex-order characterization of nonnegative Peano kernels through Denuit, Lefèvre, and Shaked (1998) and records the classical Peano representation used here.

The present result is the Euler-band specialization and source-realizable obstruction: the AF-206 pointwise domination, uniform far-tail decay of the Euler family, and a smooth signed dipole combine to prove that fixed-band coercivity fails on the full signed normalized carrier class. The construction is elementary enough that it should be treated as a derived boundary theorem, not as a novelty claim.

## Boundaries and failure modes

1. The theorem is for a **fixed finite vertical band** and fixed `sigma>0`. It does not rule out an observation family whose strength grows with the escaping scale or which includes nondecaying probes capable of detecting the far dipole.
2. The counterexample uses escape to infinity. It does not prove failure on a uniformly tight signed carrier family, on a common compact support, or on a source class with an independent tail/coherence bound.
3. Positivity is sufficient and removes this obstruction, but the theorem does not say that every useful source class must be positive. A signed class can still be coercive if its internal structure prevents the cancellation/escape sequence.
4. The probability-pair realization preserves the normalized carrier exactly, but the surviving moment `Delta_m=m!/a` depends on the constructed carrier. Absolute unnormalized transfer statements still need the amplitude/profile factor emphasized in AF-206.
5. The result is a control theorem. It provides no rational-prime discriminator, no zeta-zero selection mechanism, and no implication for RH.

## Consequence for the next research step

The next source-side question is now narrower. Outside higher-convex order, do not search for a lower recovery theorem on unrestricted signed Peano carriers. First identify a mathematically forced restriction that blocks the kernel exposed by `(24)`: for example uniform tightness, a quantitative sign-coherence floor, bounded support after normalization, or a structural arithmetic constraint on admissible Peano kernels. Only then ask whether the resulting restricted signed class admits finite-band coercivity strong enough to distinguish rational-prime data from matched controls.
