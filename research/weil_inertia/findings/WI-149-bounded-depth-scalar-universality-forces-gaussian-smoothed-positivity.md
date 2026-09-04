# WI-149 — bounded-depth scalar universality forces a Gaussian-smoothed spectral positivity family

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-145--WI-148 progressively close the attempt to import a signed CGdL-style Fourier profile into Lamzouri's universal one-scalar finite inequality. WI-148 proves pointwise Fourier positivity for every fixed continuous profile with absolute exponential moments of all orders, using conjugate-pair probes whose common off-line depth is allowed to grow without bound. It explicitly leaves a possible escape through `T`-dependent profiles or through restricting the complex configurations that must be tested.

There is an exact intermediate theorem which quantifies how much of WI-148 survives when the zero-side inequality is assumed only in a **bounded horizontal-depth strip**. Let `B>0`, let `phi : R -> R` be continuous, real-even and normalized by

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

Suppose Lamzouri's scalar-form inequality

\[
 s(\mathcal Z)\ge 2|\mathcal Z|-\sum_{z,w\in\mathcal Z}H(z-w)
\tag{4}
\]

holds for every nonempty finite conjugation-invariant multiset `Z` contained in

\[
|\operatorname{Im}z|\le B.
\tag{5}
\]

Then for every `a>0` and every `0<b<B`, putting

\[
k:=\frac{2\pi b}{a}
\tag{6}
\]

and denoting the unnormalized Gaussian transform by

\[
G_k\phi(x):=\int_{\mathbb R}\phi(t)e^{-k(t-x)^2}\,dt,
\tag{7}
\]

one necessarily has

\[
\boxed{
G_k\phi(a)+e^{-ka^2}G_k\phi(0)\ge0.
}
\tag{8}
\]

Thus finite-depth universality does **not** immediately force pointwise Fourier positivity, but neither does it allow arbitrary signed spectral freedom. A negative band at radius `a` is tested after Gaussian smoothing at resolution `k^{-1/2} \asymp \sqrt{a/b}`, with only an exponentially damped contribution from the distinguished spectral point `0` available to compensate it.

For a `T`-dependent family this gives a quantitative barrier absent from WI-148. If `B_T -> infinity` and the profiles are uniformly bounded, `|phi_T|<=M`, and uniformly Lipschitz with constant `L`, then for every fixed `a>0` and every fixed `0<epsilon<1`, choosing `b=(1-epsilon)B_T` gives

\[
\boxed{
\phi_T(a)
\ge
-\frac{L}{\sqrt{\pi k_T}}
-M e^{-k_Ta^2},
\qquad
k_T=\frac{2\pi(1-\epsilon)B_T}{a}.
}
\tag{9}
\]

Consequently

\[
\liminf_{T\to\infty}\phi_T(a)\ge0
\qquad(a>0\text{ fixed}).
\tag{10}
\]

So a regular `T`-dependent scalar family cannot preserve a fixed-amplitude negative Fourier dip at any fixed radius merely by observing that each finite-height zero set occupies only a finite horizontal-depth strip. To keep `phi_T(a)<=-delta<0`, one must pay at least one genuinely new cost: the local Lipschitz scale must grow on the order of `sqrt(B_T)` (unless the amplitude bound itself grows fast enough to compensate), the negative feature must move/narrow with `T`, or the inequality must cease to be universal over all conjugation-invariant configurations in the physical strip. This does not improve the current simple-critical percentage; it narrows a surviving scalar escape route and identifies its quantitative resolution scale.

## 1. Exact spectral form of the bounded-strip finite inequality

For a finite conjugation-invariant multiset `Z`, define

\[
S_{\mathcal Z}(t):=\sum_{z\in\mathcal Z}e^{-2\pi i tz}.
\tag{11}
\]

Conjugation invariance gives

\[
\sum_{w\in\mathcal Z}e^{2\pi i tw}=\overline{S_{\mathcal Z}(t)}.
\tag{12}
\]

If all elements satisfy `|Im z|<=B`, every difference has imaginary part at most `2B`; (2) therefore justifies Fubini in the pair sum and yields

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

The proof below uses only such non-real conjugate-pair multisets. In particular, no zeta asymptotic, pair-correlation formula, Gram representation or positivity of `phi` is used in the finite step.

## 2. Binomial probes with asymptotically fixed off-line depth

Fix `a>0` and `0<b<B`, and set

\[
\lambda:=\frac{8b}{\pi a}.
\tag{15}
\]

For a real parameter `R -> infinity`, choose

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
b_R\longrightarrow \frac{\lambda\pi a}{8}=b.
\tag{17}
\]

Hence `b_R<B` for all sufficiently large `R`.

Put

\[
x_j:=\frac{j}{2R},\qquad 0\le j\le m_R,
\tag{18}
\]

and give the center `x_j` multiplicity `binom(m_R,j)`. Let `Z_R` contain at each such center the conjugate pair

\[
x_j+ib_R,\qquad x_j-ib_R.
\tag{19}
\]

Then `Z_R` is conjugation-invariant, has no real points, lies in `|Im z|<B` for large `R`, and

\[
|\mathcal Z_R|=2^{m_R+1}.
\tag{20}
\]

Its horizontal exponential polynomial is exactly

\[
P_R(t)
:=\sum_{j=0}^{m_R}\binom{m_R}{j}e^{-2\pi i t x_j}
=\left(1+e^{-\pi i t/R}\right)^{m_R},
\tag{21}
\]

so

\[
|P_R(t)|^2
=4^{m_R}
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}.
\tag{22}
\]

The conjugate-pair factor is

\[
S_{\mathcal Z_R}(t)
=2\cosh(2\pi b_Rt)P_R(t).
\tag{23}
\]

Combining (13), (14), (20), (22), and (23), then dividing by `4^{m_R+1}`, gives

\[
\int_{\mathbb R}
\phi(t)\cosh^2(2\pi b_Rt)
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}dt
\ge 2^{-m_R}.
\tag{24}
\]

This is the bounded-depth analogue of the spectral microscope used in WI-147--WI-148. The difference is that the depth tends to the prescribed finite value `b`; localization is therefore finite rather than pointwise.

## 3. The large-window limit is an exact Gaussian inequality

For every fixed real `t`,

\[
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}
\longrightarrow
\exp\left(-\frac{\lambda\pi^2}{4}t^2\right).
\tag{25}
\]

Since

\[
\frac{\lambda\pi^2}{4}=\frac{2\pi b}{a}=k,
\tag{26}
\]

the limit is `e^{-kt^2}`. Also `b_R -> b`. For large `R`, `b_R<B`, while

\[
0\le
\left(\cos^2\frac{\pi t}{2R}\right)^{m_R}
\le1
\tag{27}
\]

and

\[
\cosh^2(2\pi b_Rt)\le e^{4\pi B|t|}.
\tag{28}
\]

The single exponential-moment assumption (2) is therefore a dominating integrable function. Dominated convergence in (24), together with `2^{-m_R}->0`, yields the exact necessary condition

\[
\boxed{
\int_{\mathbb R}\phi(t)e^{-kt^2}\cosh^2(2\pi bt)\,dt\ge0.
}
\tag{29}
\]

Because `2 pi b = k a`,

\[
\cosh^2(kat)=\frac12+\frac12\cosh(2kat),
\tag{30}
\]

and the elementary completion-of-squares identity gives

\[
e^{-kt^2}\cosh(2kat)
=
\frac{e^{ka^2}}2
\left(
e^{-k(t-a)^2}+e^{-k(t+a)^2}
\right).
\tag{31}
\]

Evenness of `phi` makes the two shifted Gaussian integrals equal. Thus (29) is exactly

\[
\frac12G_k\phi(0)
+rac12e^{ka^2}G_k\phi(a)
\ge0,
\tag{32}
\]

which is equivalent to (8).

The result is not an approximation and does not require taking `b -> B`. For every strictly interior depth `b<B`, (8) is an exact consequence of bounded-strip universality.

## 4. Quantitative consequence for regular `T`-dependent profiles

Assume now that a family `phi_T` satisfies the strip theorem with depths `B_T`, that

\[
|\phi_T(t)|\le M
\quad\text{and}\quad
|\phi_T(t)-\phi_T(s)|\le L|t-s|
\tag{33}
\]

with constants independent of `T`. Fix `a>0` and `epsilon in (0,1)`, and set

\[
b_T=(1-\epsilon)B_T,
\qquad
k_T=\frac{2\pi(1-\epsilon)B_T}{a}.
\tag{34}
\]

From (8),

\[
G_{k_T}\phi_T(a)
\ge
-e^{-k_Ta^2}G_{k_T}\phi_T(0)
\ge
-M e^{-k_Ta^2}\sqrt{\frac\pi{k_T}}.
\tag{35}
\]

On the other hand, global Lipschitz control gives

\[
G_{k_T}\phi_T(a)
\le
\phi_T(a)\sqrt{\frac\pi{k_T}}
+L\int_{\mathbb R}|u|e^{-k_Tu^2}\,du
=
\phi_T(a)\sqrt{\frac\pi{k_T}}+\frac{L}{k_T}.
\tag{36}
\]

Combining (35)--(36) proves (9). In explicit `B_T` form,

\[
\phi_T(a)
\ge
-
\frac{L\sqrt a}{\pi\sqrt{2(1-\epsilon)B_T}}
-
M e^{-2\pi(1-\epsilon)aB_T}.
\tag{37}
\]

Therefore a fixed negative dip of size `delta` at a fixed radius forces, up to the exponentially small second term,

\[
L_T\gtrsim
\delta\,\pi\sqrt{\frac{2(1-\epsilon)B_T}{a}}.
\tag{38}
\]

This is the promised quantitative cost. A `T`-dependent escape is not ruled out absolutely, but it must become increasingly nonuniform on the Gaussian scale `B_T^{-1/2}`, move its signed structure with `T`, or abandon universal strip testing.

## 5. Relation to Lamzouri, positive-definite strips, and copositive-kernel prior art

The zero-side source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1. Lamzouri's actual kernel is generated by positive Hilbert-space data and satisfies the finite inequality for all conjugation-invariant multisets, not merely a bounded strip. WI-145--WI-148 abstract that proposition to ask whether a different scalar kernel could carry signed Fourier mass.

Jorge Buescu, A. C. Paixão and A. Symeonides, *Complex Positive Definite Functions on Strips*, Complex Analysis and Operator Theory 11 (2017), 627--649, DOI `10.1007/s11785-015-0527-y`, characterize holomorphic **positive-definite** functions on horizontal strips as Fourier--Laplace transforms of exponentially finite positive measures. That theorem assumes positivity of arbitrary finite quadratic forms and therefore forces a positive representing measure outright. It does not directly imply (8): the Lamzouri census supplies only coefficient-one conjugation-invariant multiset tests plus the population term, a substantially different hypothesis.

The neighboring infinite-dimensional copositive-kernel literature likewise keeps copositivity distinct from positive semidefiniteness; see, for example, C. Dobre, M. Dür, L. Frerick and F. Vallentin, *A copositive formulation for the stability number of infinite graphs*, Mathematical Programming 160 (2016), 65--83, DOI `10.1007/s10107-015-0974-2`, and O. Kuryatnikova and J. C. Vera, *Positive semidefinite approximations to the cone of copositive kernels*, arXiv:1812.00274. Those works concern general copositive-kernel cones and do not supply the special Gaussian constraint (8) from conjugate-pair Fourier--Laplace geometry.

The Gaussian/heat-kernel approximate-identity manipulations in (25)--(37), binomial large-deviation scaling, and Fourier--Laplace dominated convergence are classical ingredients. A targeted search of the current `weil_inertia` corpus and the closest positive-definite-strip/copositive-kernel literature located no stored theorem giving (8) from bounded-depth Lamzouri-form universality. This is the novelty boundary used for this line, not a claim of mathematical priority.

## 6. Boundaries and research consequence

The strongest limitation is the word **universal**. Actual zeta zeros at height `T` occupy only a highly structured subset of the physically allowed strip. A source-specific theorem may exploit arithmetic restrictions that exclude the binomial configurations (19), and this finding does not rule that out. Proving such a restriction would itself be new zeta-specific information of exactly the kind the canonical `weil_inertia` mandate permits.

The regular-family corollary also assumes uniform `L^infinity` and Lipschitz control. It does not forbid a `T`-dependent profile whose negative bands narrow on scales smaller than `B_T^{-1/2}`, whose amplitudes/derivatives grow, or whose entire signed pattern moves to spectral radii increasing with `T`. Those evasions are not free on the prime side, but this finding does not supply the required arithmetic cost theorem.

Finally, the theorem concerns one scalar translation-invariant pair kernel. Joint multi-profile inequalities, sign-indefinite matrix observables, explicit horizontal/negative-inertia charges, and non-scalar incidence statistics remain outside it. No new unconditional zero proportion is claimed.

What is closed is a more specific escape left open by WI-148: **finite physical depth by itself does not restore ordinary signed-kernel freedom.** At depth `B`, universal scalar testing already forces Gaussian-smoothed positivity down to resolution about `B^{-1/2}` at every fixed spectral radius; as the available depth tends to infinity, any uniformly regular `T`-dependent family is driven back into the nonnegative Fourier cone pointwise. Any successful scalar escape must therefore exploit nonuniform fine-scale motion or genuinely zeta-specific restrictions rather than the mere finiteness of the strip.