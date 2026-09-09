# XF-144 — arbitrarily small real-axis scanning breaks reflected heat degeneracy

**Status:** `EXACT-DERIVED` + `STRUCTURAL/POSITIVE-BOUNDARY` + `SINGLE-MOVING-PROBE` + `REAL-AXIS` + `ARBITRARILY-SMALL-EXCURSION` + `TARGET-GENERAL`. XF-142 shows that heat-time derivatives at one fixed spatial point do not create a new information axis: after the exact heat gauge they collapse to the spatial jet. XF-143 then restores exact full-state identifiability by using two simultaneous real-axis traces separated by half a mean root spacing. There is a strictly smaller exact interface. A **single** real-axis probe whose position moves at any nonzero constant speed already separates every reflected heat-rate pair, even when its total spatial excursion is arbitrarily smaller than one root spacing.

The gain is algebraic, not stable. If the scan travels only distance `D`, the nearest reflected pair alone forces inverse amplification at least `Omega(L/D)`. At a root-spacing excursion this reproduces the `Omega(N)` spatial order of XF-143, while excursions `o(L/N)` are still exactly identifying but become superlinearly ill-conditioned before the independent exponential central-packet obstruction of XF-132--XF-134 is taken into account.

## Result

Let

\[
E(w,s)=\sum_{k=0}^{N}E_k e^{-\delta_k s}w^k,
\qquad
\delta_k=a k(N-k),
\qquad a>0,
\tag{1}
\]

be an arbitrary degree-`N` state under the exact XF-067 coefficient heat flow. No root-location, self-inversive, simplicity, or reality hypothesis is imposed. Fix an observation horizon `S>0`, a unit-circle phase `|\zeta_0|=1`, and a real scanning rate `\nu\ne0`. Define

\[
\boxed{
\zeta(s)=\zeta_0e^{i\nu s},
\qquad
Q_\nu(s):=E(\zeta(s),s),
\qquad 0\le s\le S.
}
\tag{2}
\]

Then the single scalar history `Q_nu` determines every coefficient `E_0,...,E_N` exactly. In fact

\[
\boxed{
Q_\nu(s)
=\sum_{k=0}^{N}
E_k\zeta_0^k e^{\lambda_k s},
\qquad
\lambda_k=-a k(N-k)+i\nu k,
}
\tag{3}
\]

and the `N+1` complex exponents `lambda_k` are pairwise distinct whenever `nu!=0`. Hence knowledge of `Q_nu` on any nonempty open subinterval of `[0,S]` determines the complete polynomial state, its root multiset with multiplicity, and therefore its entire periodic heat trajectory and `Lambda_per`.

In the physical XF-067 coordinate

\[
\zeta(x)=-e^{-2\pi i x/L},
\tag{4}
\]

a scan `(2)` is simply a real path

\[
\boxed{
x(s)=x_0-\frac{\nu L}{2\pi}s\pmod L.}
\tag{5}
\]

Its total travel over `[0,S]` is

\[
\boxed{
D=\frac{|\nu|LS}{2\pi}.}
\tag{6}
\]

For every finite `N` and every prescribed `D>0`, however small, choosing `|nu|=2pi D/(LS)` gives exact full-state identifiability. Thus there is **no positive root-spacing threshold for exact identification by a moving real probe**. The threshold is exactly `D=0`, where the reflected heat-rate degeneracy returns.

The conditioning boundary is equally explicit. Put

\[
d_N=
\begin{cases}
1,&N\text{ odd},\\
2,&N\text{ even},
\end{cases}
\tag{7}
\]

and choose the reflected pair nearest the central shell,

\[
k_-:=\frac{N-d_N}{2},
\qquad
k_+:=\frac{N+d_N}{2}=N-k_-.
\tag{8}
\]

There is a coefficient direction of `ell^infinity` norm one supported only on `(k_-,k_+)` whose moving trace obeys

\[
\boxed{
\|\Delta Q_\nu\|_{L^\infty(0,S)}
\le |\nu|d_NS
=\frac{2\pi d_ND}{L}.
}
\tag{9}
\]

Consequently every local inverse from the moving-trace sup norm to coefficient `ell^infinity` norm has condition number at least

\[
\boxed{
\operatorname{cond}_{\rm scan}
\ge
\frac{L}{2\pi d_ND}.
}
\tag{10}
\]

For `D=cL/N`, this is `Omega(N)`. For `D=o(L/N)`, it is superlinear. This is only the cost of breaking the exact reflected-pair symmetry; complete-state or transition recovery can be much worse because the central divided-difference packets of XF-132--XF-140 introduce exponential instability that is independent of this elementary pairwise lower bound.

## 1. Constant-speed motion splits all heat exponents

Substituting `(2)` into `(1)` gives

\[
\begin{aligned}
Q_\nu(s)
&=\sum_{k=0}^N
E_k e^{-ak(N-k)s}
\zeta_0^k e^{i\nu ks}\\
&=\sum_{k=0}^N C_k e^{\lambda_k s},
\qquad
C_k:=E_k\zeta_0^k,
\end{aligned}
\tag{11}
\]

with `lambda_k` as in `(3)`. If `lambda_k=lambda_l`, equality of imaginary parts gives

\[
\nu(k-l)=0.
\tag{12}
\]

Since `nu!=0`, one has `k=l`. Thus all exponents are distinct. This is precisely what a fixed real probe fails to do: at `nu=0`,

\[
\lambda_k=\lambda_{N-k}
\tag{13}
\]

and heat time sees only reflected pairs, as in XF-129--XF-143.

Exact recovery may be written without invoking any infinite-dimensional observability theorem. Fix any time `s_*` in the interior of the observation interval. For `m=0,...,N`,

\[
Q_\nu^{(m)}(s_*)
=\sum_{k=0}^N
C_ke^{\lambda_ks_*}\lambda_k^m.
\tag{14}
\]

The matrix in `(14)` is a Vandermonde matrix in the pairwise distinct nodes `lambda_0,...,lambda_N`, multiplied by a nonzero diagonal matrix. Its determinant is

\[
\left(\prod_{k=0}^Ne^{\lambda_ks_*}\right)
\prod_{0\le k<l\le N}(\lambda_l-\lambda_k)
\ne0.
\tag{15}
\]

Therefore the first `N+1` derivatives at one time determine every `C_k`, hence every `E_k`. Equivalently, if two moving traces agree on any open time interval, their difference is a finite exponential polynomial vanishing on an open set and therefore vanishes identically; linear independence of the distinct exponentials then gives equality coefficient by coefficient.

The statement remains true when `nu=nu_N` tends to zero arbitrarily fast with the degree. Exact uniqueness is a finite-`N` algebraic fact. What deteriorates in that limit is conditioning, not injectivity.

## 2. Motion supplies exactly the missing odd spatial symbol

XF-142 explains the fixed-point failure structurally. After the standard gauge, the heat evolution is generated by a second spatial derivative, so instantaneous time differentiation produces only the same spatial jet already present at that point. In Fourier/Vieta coordinates this appears as the reflection symmetry

\[
k\longleftrightarrow N-k
\tag{16}
\]

of the real heat rate `ak(N-k)`.

A moving observation differentiates along the path rather than vertically in heat time. In the polynomial phase coordinate, its generator is

\[
\frac d{ds}
=\partial_s+i\nu\,w\partial_w.
\tag{17}
\]

On the `k`th coefficient mode, the first term contributes the even/reflection-symmetric symbol `-ak(N-k)`, while the convective term contributes the linear symbol `i nu k`. Their sum is exactly `lambda_k` in `(3)`. Any nonzero motion therefore injects the odd-in-reflection component that XF-142 proves cannot be manufactured from fixed-point heat derivatives alone.

This also clarifies the relation to XF-143. Two stationary real samples break each reflected pair by a spatial phase difference. A moving sample breaks the same symmetry by converting spatial phase into a small imaginary separation between temporal exponents. The two mechanisms have the same root-spacing conditioning order when their spatial apertures are matched.

## 3. The nearest reflected pair gives the sharp small-excursion lower bound

Take the indices `(8)` and define a coefficient perturbation by

\[
\Delta E_{k_-}=\zeta_0^{-k_-},
\qquad
\Delta E_{k_+}=-\zeta_0^{-k_+},
\tag{18}
\]

with all other coefficients zero. Since `|zeta_0|=1`,

\[
\|\Delta E\|_{\ell^\infty}=1.
\tag{19}
\]

The two indices are reflected, so

\[
\delta_{k_-}=\delta_{k_+}=:\delta_*.
\tag{20}
\]

Their moving trace is therefore

\[
\begin{aligned}
\Delta Q_\nu(s)
&=e^{-\delta_*s}
\left(e^{i\nu k_-s}-e^{i\nu k_+s}\right)\\
&=2i e^{-\delta_*s}
e^{i\nu Ns/2}
\sin\!\left(\frac{\nu d_Ns}{2}\right).
\end{aligned}
\tag{21}
\]

Using `|sin u|<=|u|` and `e^{-delta_*s}<=1`,

\[
|\Delta Q_\nu(s)|
\le |\nu|d_Ns
\le |\nu|d_NS.
\tag{22}
\]

Equations `(6)` and `(22)` give `(9)`--`(10)`.

The parity factor `d_N` is unavoidable for the nearest nontrivial reflected shell: it equals one in odd degree and two in even degree because the central even shell is self-reflected. Up to this bounded factor, the symmetry-breaking cost is exactly inverse excursion.

If the scan travels half a mean root spacing, as in the total aperture of XF-143,

\[
D\asymp\frac{L}{2N},
\tag{23}
\]

then `(10)` gives a linear lower bound in `N`, matching the order of XF-143's `O(N)` two-point reflected-pair inversion. Thus the linear factor in XF-143 is not a peculiarity of using two simultaneous sensors: it is the generic local price for resolving the nearest reflected heat pair with only root-spacing-scale real-axis phase variation.

## 4. Exact identifiability still does not give a stable transition certificate

Because `(2)` determines the entire coefficient vector exactly, it determines the polynomial roots with multiplicity and hence the periodic transition time:

\[
\boxed{
Q_\nu(\cdot)=\widetilde Q_\nu(\cdot)
\text{ on an open interval}
\Longrightarrow
\Lambda_{\rm per}(E)=\Lambda_{\rm per}(\widetilde E).
}
\tag{24}
\]

This is a positive **identifiability** boundary only. It does not evade the transition-conditioning obstruction already proved by XF-134 and sharpened through XF-140. If the real scan path stays inside one of the central-packet blind patches, restricting the XF-134 matched controls to that path gives two states whose transition times differ by a prescribed `rho` while their complete moving histories are exponentially close. The scan is therefore injective at exact precision and still exponentially useless as a uniformly stable unrestricted transition decoder.

This distinction is especially stark when `D_N` tends to zero. Equation `(15)` remains nonsingular for every `D_N>0`, yet `(10)` already diverges like `L/D_N`; the central-packet family can then make the true transition conditioning exponential in `N`. There is no contradiction. Exact observability is a zero-noise statement, whereas the current Xi interface problem is quantitative and must survive source approximation, normalization, and transport errors.

The result also does not weaken the source-specific alternative. If actual Xi data exclude the XF-134 central packet or provide a relative observation norm with exponentially stronger precision, a moving trace could still be useful. What is ruled out is treating the mere algebraic injectivity of a scan as the missing upper-bound mechanism.

## 5. Prior-art boundary

Moving or scanning point sensors for the heat equation are classical. Alexander Khapalov, **L-infinity-Exact Observability of the Heat Equation with Scanning Pointwise Sensor**, *SIAM Journal on Control and Optimization* 32:4 (1994), 1037--1051, DOI `10.1137/S036301299222737X`, constructs scanning observation curves for exact heat observability and explicitly treats the mobile-point-sensor setting. Classical exponential-polynomial/Prony theory likewise makes linear independence of finitely many distinct complex exponentials standard.

Those results delimit the general observability mechanism; neither is load-bearing here. The proof is the explicit XF-067 spectrum `(1)` plus the constant-speed phase substitution `(2)`, which changes the reflected quadratic rates into the pairwise distinct complex rates `(3)`. The line-specific quantitative addition is the exact nearest-pair excursion cost `(9)`--`(10)` and its match with XF-143 at the root-spacing scale. No external theorem is required, so `SOURCES.md` acquires no new dependency.

No general novelty is claimed for scanning heat sensors, Vandermonde recovery, or uniqueness of finite exponential sums. The durable `xi_flow` content is the precise way an arbitrarily small real-axis motion breaks the **specific** `k <-> N-k` coefficient-heat degeneracy while leaving the already-proved transition-conditioning obstruction intact.

## Consequence for the Xi-flow frontier

XF-142 and XF-143 separate two kinds of local information: more derivatives along the same fixed slice are redundant, whereas a second spatial phase is genuinely new. XF-144 sharpens that boundary further. One does not need a second simultaneous sensor or even a root-spacing-sized displacement for exact information. A single real probe with any nonzero scan speed supplies an independent odd spatial symbol and makes the finite periodic state algebraically identifiable.

The remaining gate is therefore not **how much spatial motion is needed for uniqueness**; the answer is arbitrarily little. It is how much independent geometry and precision are needed for a **stable transition inequality** under the actual Xi source errors. At root-spacing excursion the reflected-pair price is already `Theta(N)`, at smaller excursion it is worse, and the XF-134 central packets show that local scanning still inherits exponential transition blindness in the unrestricted periodic class.

A materially different positive route must consequently use Xi-specific exclusion of those packets, an observation geometry that leaves their blind patch, or a transition functional with source-controlled conditioning. Merely replacing two fixed traces by a continuously scanned local trace changes the algebraic sensor count, not the current quantitative obstruction.