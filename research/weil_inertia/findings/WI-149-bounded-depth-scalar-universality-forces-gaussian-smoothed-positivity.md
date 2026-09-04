# WI-149 — bounded-depth scalar universality forces a Gaussian-smoothed spectral positivity family

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-145--WI-148 progressively close the attempt to import a signed CGdL-style Fourier profile into Lamzouri's universal one-scalar finite inequality. WI-148 proves pointwise Fourier positivity for every fixed continuous profile with absolute exponential moments of all orders by allowing conjugate-pair probes of unbounded off-line depth. The exact intermediate result below quantifies what survives when the finite inequality is available only in a bounded horizontal-depth strip, and it closes a regular version of the `T`-dependent finite-strip escape explicitly left open by WI-148.

Let `B>0`, let `phi : R -> R` be continuous, real-even, normalized by

\[
\int_{\mathbb R}\phi(t)\,dt=1,
\tag{1}
\]

and assume the single exponential moment

\[
\int_{\mathbb R}|\phi(t)|e^{4\pi B|t|}\,dt<\infty.
\tag{2}
\]

Define

\[
H(z)=\int_{\mathbb R}\phi(t)e^{-2\pi i zt}\,dt
\qquad (|\operatorname{Im}z|\le 2B).
\tag{3}
\]

Suppose the Lamzouri-form scalar inequality

\[
s(\mathcal Z)\ge 2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{4}
\]

holds for every nonempty finite conjugation-invariant multiset `Z` contained in `|Im z|<=B`. Then for every `a>0` and every `0<b<B`, putting

\[
k:=\frac{2\pi b}{a},
\tag{5}
\]

and

\[
G_k\phi(x):=\int_{\mathbb R}\phi(t)e^{-k(t-x)^2}\,dt,
\tag{6}
\]

one necessarily has

\[
\boxed{
G_k\phi(a)+e^{-ka^2}G_k\phi(0)\ge0.
}
\tag{7}
\]

Thus finite-depth universality does not immediately force pointwise Fourier positivity, but it does force a one-parameter family of **Gaussian-smoothed positivity constraints**. A negative band at radius `a` is tested at resolution `k^{-1/2} asy sqrt(a/b)`, and only an exponentially damped contribution from the distinguished spectral point `0` can compensate it.

For a `T`-dependent family this becomes a quantitative barrier. If `B_T -> infinity`, the profiles satisfy the corresponding strip-universal inequality, and there are `T`-independent constants `M,L` with

\[
|\phi_T(t)|\le M,
\qquad
|\phi_T(t)-\phi_T(s)|\le L|t-s|,
\tag{8}
\]

then for every fixed `a>0` and `epsilon in (0,1)`, with

\[
k_T=\frac{2\pi(1-\epsilon)B_T}{a},
\tag{9}
\]

one has

\[
\boxed{
\phi_T(a)
\ge
-\frac{L}{\sqrt{\pi k_T}}
-M e^{-k_Ta^2}.
}
\tag{10}
\]

Hence `liminf phi_T(a)>=0` at every fixed positive spectral radius. A regular `T`-dependent scalar family cannot preserve a fixed-amplitude negative Fourier dip merely by noting that each finite-height zero problem has finite horizontal depth. To keep `phi_T(a)<=-delta<0`, one must make the local derivative scale grow at least on the order of `sqrt(B_T)` (unless amplitudes grow fast enough to compensate), move or narrow the signed feature with `T`, or abandon universality over all conjugation-invariant configurations in the physical strip.

## 1. Exact spectral form of the bounded-strip inequality

For a finite conjugation-invariant multiset `Z`, set

\[
S_{\mathcal Z}(t):=\sum_{z\in\mathcal Z}e^{-2\pi i tz}.
\tag{11}
\]

Conjugation invariance gives

\[
\sum_{w\in\mathcal Z}e^{2\pi i tw}=\overline{S_{\mathcal Z}(t)}.
\tag{12}
\]

If every element satisfies `|Im z|<=B`, every difference has imaginary part at most `2B`; assumption (2) therefore justifies Fubini and yields

\[
\boxed{
Q_H(\mathcal Z)
:=\sum_{z,w\in\mathcal Z}H(z-w)
=\int_{\mathbb R}\phi(t)|S_{\mathcal Z}(t)|^2\,dt.
}
\tag{13}
\]

When `Z` has no real elements, (4) implies

\[
Q_H(\mathcal Z)\ge2|\mathcal Z|.
\tag{14}
\]

The argument below uses only such non-real conjugate-pair multisets. No zeta asymptotic, pair-correlation formula, Gram representation, or positivity assumption on `phi` enters this finite step.

## 2. Binomial probes at asymptotically fixed depth

Fix `a>0`, `0<b<B`, and set

\[
\lambda:=\frac{8b}{\pi a}.
\tag{15}
\]

For `R -> infinity`, define

\[
m_R:=\lfloor\lambda R^2\rfloor,
\qquad
\theta_R:=\frac{\pi a}{2R},
\qquad
b_R:=\frac{m_R}{4R}\tan\theta_R.
\tag{16}
\]

Since `tan(theta_R)=theta_R+O(R^{-3})`,

\[
b_R\longrightarrow \frac{\lambda\pi a}{8}=b,
\tag{17}
\]

so `b_R<B` for all sufficiently large `R`.

Put `x_j=j/(2R)` for `0<=j<=m_R`, give `x_j` multiplicity `binom(m_R,j)`, and let `Z_R` contain the conjugate pair

\[
x_j+ib_R,
\qquad
x_j-ib_R
\tag{18}
\]

with that multiplicity. Then `Z_R` is conjugation-invariant, has no real points, lies in the allowed strip for large `R`, and

\[
|\mathcal Z_R|=2^{m_R+1}.
\tag{19}
\]

The horizontal exponential polynomial is

\[
P_R(t)
:=\sum_{j=0}^{m_R}\binom{m_R}{j}e^{-2\pi i t x_j}
=\left(1+e^{-\pi i t/R}\right)^{m_R},
\tag{20}
\]

hence

\[
|P_R(t)|^2
=4^{m_R}
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}.
\tag{21}
\]

The vertical conjugate-pair factor gives

\[
S_{\mathcal Z_R}(t)
=2\cosh(2\pi b_Rt)P_R(t).
\tag{22}
\]

Combining (13), (14), (19)--(22), then dividing by `4^{m_R+1}`, gives

\[
\int_{\mathbb R}
\phi(t)\cosh^2(2\pi b_Rt)
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}dt
\ge 2^{-m_R}.
\tag{23}
\]

This is the bounded-depth version of the spectral microscope used in WI-147--WI-148. The depth tends to the prescribed finite value `b`, so the limiting localization is Gaussian rather than pointwise.

## 3. The large-window limit and the Gaussian identity

For every fixed real `t`,

\[
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}
\longrightarrow
\exp\left(-\frac{\lambda\pi^2}{4}t^2\right)
=e^{-kt^2},
\tag{24}
\]

because `lambda*pi^2/4 = 2*pi*b/a = k`. Also `b_R -> b`. For large `R`,

\[
0\le
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}
\le1,
\qquad
\cosh^2(2\pi b_Rt)\le e^{4\pi B|t|}.
\tag{25}
\]

The single moment (2) is therefore a dominating integrable function. Dominated convergence in (23), together with `2^{-m_R}->0`, gives

\[
\boxed{
\int_{\mathbb R}\phi(t)e^{-kt^2}\cosh^2(2\pi bt)\,dt\ge0.
}
\tag{26}
\]

Since `2*pi*b=k*a`, the elementary identities

\[
\cosh^2(kat)=\frac{1+\cosh(2kat)}{2}
\tag{27}
\]

and

\[
e^{-kt^2}\cosh(2kat)
=
\frac{e^{ka^2}}{2}
\left(
e^{-k(t-a)^2}+e^{-k(t+a)^2}
\right)
\tag{28}
\]

show, using evenness of `phi`, that the left side of (26) is exactly

\[
\frac{1}{2}G_k\phi(0)
+
\frac{1}{2}e^{ka^2}G_k\phi(a).
\tag{29}
\]

Equation (26) is therefore equivalent to (7). The result is exact for every interior depth `b<B`; no limiting passage `b -> B` is required.

## 4. Quantitative consequence for regular moving profiles

Assume the uniform bounds (8), fix `a>0` and `epsilon in (0,1)`, and take

\[
b_T=(1-\epsilon)B_T,
\qquad
k_T=\frac{2\pi(1-\epsilon)B_T}{a}.
\tag{30}
\]

From (7),

\[
G_{k_T}\phi_T(a)
\ge
-e^{-k_Ta^2}G_{k_T}\phi_T(0)
\ge
-M e^{-k_Ta^2}\sqrt{\frac{\pi}{k_T}}.
\tag{31}
\]

Global Lipschitz control also gives

\[
G_{k_T}\phi_T(a)
\le
\phi_T(a)\sqrt{\frac{\pi}{k_T}}
+L\int_{\mathbb R}|u|e^{-k_Tu^2}\,du
=
\phi_T(a)\sqrt{\frac{\pi}{k_T}}+\frac{L}{k_T}.
\tag{32}
\]

Combining (31)--(32) gives (10), or explicitly

\[
\phi_T(a)
\ge
-
\frac{L\sqrt a}{\pi\sqrt{2(1-\epsilon)B_T}}
-
M e^{-2\pi(1-\epsilon)aB_T}.
\tag{33}
\]

Thus a fixed negative dip of size `delta` at a fixed radius forces, up to the exponentially small second term,

\[
L_T\gtrsim
\delta\,\pi\sqrt{\frac{2(1-\epsilon)B_T}{a}}.
\tag{34}
\]

The remaining evasions are correspondingly nonuniform: narrower features on scales below `B_T^{-1/2}`, growing amplitude/derivative norms, or spectral structure whose radius itself moves with `T`.

## 5. Prior-art audit and novelty boundary

The primary zero-side source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1. Lamzouri's actual kernel is generated by positive Hilbert-space data and his finite inequality is universal over all conjugation-invariant multisets; WI-145--WI-148 abstract that proposition to test whether a different scalar kernel can carry signed Fourier mass.

Jorge Buescu, A. C. Paixão and A. Symeonides, *Complex Positive Definite Functions on Strips*, Complex Analysis and Operator Theory 11 (2017), 627--649, DOI `10.1007/s11785-015-0527-y`, characterize holomorphic **positive-definite** functions on horizontal strips as Fourier--Laplace transforms of exponentially finite positive measures. Their input is positivity of arbitrary finite quadratic forms, which forces a positive representing measure outright. It does not directly imply (7): the Lamzouri census supplies only coefficient-one conjugation-invariant multiset tests plus a population term, a genuinely weaker/different hypothesis.

The neighboring copositive-kernel literature also keeps copositivity distinct from positive semidefiniteness; see C. Dobre, M. Dür, L. Frerick and F. Vallentin, *A copositive formulation for the stability number of infinite graphs*, Mathematical Programming 160 (2016), 65--83, DOI `10.1007/s10107-015-0974-2`, and O. Kuryatnikova and J. C. Vera, *Positive semidefinite approximations to the cone of copositive kernels*, arXiv:1812.00274. Those works concern general copositive-kernel cones and do not provide the special Gaussian constraint (7) from bounded-depth conjugate-pair Fourier--Laplace geometry.

The Gaussian/heat-kernel approximate-identity calculation, binomial scaling, and dominated-convergence ingredients are classical. A targeted audit of the current `weil_inertia` corpus and the closest positive-definite-strip/copositive-kernel literature located no stored theorem giving (7) from bounded-depth Lamzouri-form universality. This is the novelty boundary used for the line, not a claim of mathematical priority.

## 6. Boundaries and research consequence

The strongest limitation is **universality**. Actual zeta zeros at height `T` form a highly structured subset of all conjugation-invariant multisets allowed by their physical horizontal-depth range. A source-specific theorem may exclude the binomial configurations above, and WI-149 does not rule that out. Proving such a restriction would itself be new zeta-specific arithmetic or spectral information of exactly the kind permitted by the canonical `weil_inertia` mandate.

The moving-family corollary also assumes uniform `L^infinity` and Lipschitz control. It does not forbid profiles whose signed features narrow faster than `B_T^{-1/2}`, whose norms grow, or whose negative/positive bands move to larger spectral radii with `T`. Those evasions are likely to have a prime-side cost, but no such arithmetic cost theorem is asserted here.

Finally, WI-149 concerns one scalar translation-invariant pair kernel. Joint multi-profile inequalities, sign-indefinite matrix observables, explicit horizontal/negative-inertia charges, and nonlinear incidence statistics remain outside it. No new unconditional zero proportion is claimed.

What is closed is a precise finite-strip loophole after WI-148: **finite horizontal depth by itself does not restore ordinary signed-kernel freedom.** At depth `B`, universal scalar testing already forces Gaussian-smoothed spectral positivity down to resolution about `B^{-1/2}` at every fixed positive radius; as the available depth grows, every uniformly regular moving family is driven pointwise back toward the nonnegative Fourier cone.