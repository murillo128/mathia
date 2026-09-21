# WI-388 — Dilute high-frequency sidebands defeat gamma-to-spectral tightness

**Status:** `EXACT-DERIVED + CLASSICAL-INPUT + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-387 leaves loss of uniform zeta-frequency spectral tightness as the intrinsic fixed-width escape from its coefficient-independent recurrence theorem. A natural possible repair would be to argue that the same negative archimedean budget needed by the separated-lobe construction already prevents such high-frequency escape. That implication is false.

There are constants `L, beta, kappa, delta>0` and real even normalized profiles

\[
g_j\in C_c^\infty((-L/2,L/2)),
\qquad \|g_j\|_2=1,
\tag{1}
\]

with carrier frequencies `R_j\to\infty` such that their WI-386 archimedean lobe energies obey the uniform strict bound

\[
\boxed{B_{g_j}\le-\beta<0,}
\tag{2}
\]

while, on the RH spectral interface of WI-387,

\[
\boxed{
\sum_{\gamma\in[R_j-\delta,R_j+\delta]}
 m_\gamma |G_j(i\gamma)|^2\ge\kappa,
}
\qquad
G_j(z)=\int g_j(s)e^{zs}\,ds.
\tag{3}
\]

Consequently

\[
\boxed{
\lim_{T\to\infty}\sup_j
\sum_{|\gamma|>T}m_\gamma |G_j(i\gamma)|^2\ne0,
}
\tag{4}
\]

so the uniform spectral-tightness hypothesis of WI-387 does not follow from a uniform negative archimedean margin. The construction uses a high-frequency sideband with only `epsilon_R=c/\log R` of the `L^2` mass. The archimedean difference form charges such a sideband only logarithmically, so its total archimedean cost is `O(c)` (with an `O(sqrt(c))` cross term), whereas a fixed-length ordinate window contains `Omega(log R)` zeta zeros along a suitable sequence. The sampled mass is therefore `Omega((\log R)(1/\log R))=Omega(1)`.

The construction necessarily leaves every uniformly `H^1`-bounded class: in fact `\|g_j'\|_2\gg R_j/\sqrt{\log R_j}`. Thus there is no conflict with WI-387. It instead shows that WI-387's spectral-tightness assumption is genuinely additional structure, not something recoverable merely from `B_g<0`.

The same countermodel can be placed on a diagonal sequence of exact source-zero endpoint trials. For each fixed member the WI-386/WI-384 source-slot perforation tends to zero as the endpoint recedes, so the endpoint can be chosen far enough out that both the archimedean perturbation and the Fourier perturbation are much smaller than the sideband packet. Hence exact source slots do not restore uniform spectral tightness either.

This is a route-pruning result. It does **not** construct a positive Weil gap, does not evade the recurrence theorem by itself, and does not prove anything against RH. It rules out the weaker proposed continuation "negative gamma energy should compactify all admissible fixed-width adaptive profiles." Any extension of WI-387 to the unbounded-complexity regime needs a stronger norm/moment, a direct arithmetic control of zeta-sampled high-frequency mass, an endpoint-phase argument that survives spectral escape, or a change of geometry/operator category.

## 1. A smooth gamma-negative base profile exists

For a real normalized fixed-width profile write, as in WI-386,

\[
B_g=-C_\Gamma+\frac12\mathcal E(g),
\qquad
\mathcal E(g)=
\iint h(|s-t|)|g(s)-g(t)|^2\,ds\,dt,
\tag{5}
\]

\[
h(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\tag{6}
\]

WI-385 provides a first-Dirichlet cosine lobe with strictly negative `B_g`. That profile belongs to `H_0^1` on its fixed interval and has nonzero integral. Smooth real even compactly supported profiles are dense there, and the difference form is continuous in `H^1`: for a fixed support interval,

\[
\mathcal E(v)\ll_L \|v\|_2^2+\|v'\|_2^2.
\tag{7}
\]

Indeed, after writing the double integral by the increment `u=s-t`, use

\[
\|v(\cdot+u)-v\|_2^2
\le \min\{4\|v\|_2^2,u^2\|v'\|_2^2\},
\tag{8}
\]

while `h(u)\asymp1/u` near zero and decays exponentially at infinity. Therefore a sufficiently close even smooth approximation of the WI-385 cosine gives a profile

\[
\phi\in C_c^\infty((-L/2,L/2);\mathbb R),
\quad \phi(-s)=\phi(s),
\quad \|\phi\|_2=1,
\quad \int\phi\ne0,
\tag{9}
\]

and some `beta>0` for which

\[
B_\phi\le-3\beta.
\tag{10}
\]

No new numerical archimedean estimate is used here; only the strict margin already supplied by WI-385 and continuity of the fixed-width form.

## 2. A carrier of frequency R costs only O(log R) archimedean energy

For `R>1` put

\[
v_R(s)=\phi(s)\cos(Rs),
\qquad
\alpha_R=\langle\phi,v_R\rangle,
\tag{11}
\]

\[
\widetilde v_R=v_R-\alpha_R\phi,
\qquad
b_R=\|\widetilde v_R\|_2,
\qquad
u_R=\widetilde v_R/b_R.
\tag{12}
\]

Riemann--Lebesgue gives `\alpha_R\to0` and `b_R\to1/\sqrt2`. Thus `\nu_R` is real, even, smooth, supported in the same fixed interval, normalized, and orthogonal to `\phi`.

The identity

\[
v_R(s)-v_R(t)
=\cos(Rs)(\phi(s)-\phi(t))
+\phi(t)(\cos(Rs)-\cos(Rt))
\tag{13}
\]

and

\[
|\cos(Rs)-\cos(Rt)|
\le \min\{2,R|s-t|\}
\tag{14}
\]

show that

\[
\mathcal E(v_R)\ll_{\phi,L}1+J(R),
\tag{15}
\]

where

\[
J(R)=\int_0^L h(u)\min\{4,R^2u^2\}\,du.
\tag{16}
\]

Splitting at `u=1/R` and using `h(u)\ll_L 1/u` on `(0,L]` gives

\[
J(R)\ll_L 1+\log R.
\tag{17}
\]

Orthogonalization by the vanishing scalar `\alpha_R` and normalization by `b_R\to1/\sqrt2` preserve the order, so

\[
\boxed{\mathcal E(\nu_R)\ll_{\phi,L}1+\log R.}
\tag{18}
\]

This logarithmic carrier cost is the same general high-frequency scale that appears in the logarithmic-Laplacian literature: Chen--Weth's logarithmic Laplacian has Fourier symbol `2\log|\xi|`. That literature is context rather than a load-bearing theorem here; (13)--(18) prove the needed estimate directly.

Choose now

\[
\varepsilon_R=\frac{c}{\log R}
\tag{19}
\]

for a fixed sufficiently small `c>0`, and define

\[
g_R=\sqrt{1-\varepsilon_R}\,\phi
+\sqrt{\varepsilon_R}\,\nu_R.
\tag{20}
\]

Orthogonality makes `\|g_R\|_2=1`. Since `\mathcal E^{1/2}` is a seminorm, (18) yields

\[
\mathcal E(g_R)^{1/2}
\le
\sqrt{1-\varepsilon_R}\,\mathcal E(\phi)^{1/2}
+\sqrt{\varepsilon_R}\,\mathcal E(\nu_R)^{1/2}.
\tag{21}
\]

Hence

\[
\mathcal E(g_R)-\mathcal E(\phi)
\le C_{\phi,L}(\sqrt c+c)+o_R(1).
\tag{22}
\]

Taking `c` small enough relative to the fixed margin in (10), and then `R` large, gives

\[
\boxed{B_{g_R}\le-\beta.}
\tag{23}
\]

At the same time the derivative cost diverges. The leading term in `(\phi\cos Rs)'` is `-R\phi\sin Rs`; another Riemann--Lebesgue application gives `\|\nu_R'\|_2\asymp R`. Therefore

\[
\boxed{
\|g_R'\|_2\gg_{\phi}\sqrt{\varepsilon_R}R
\asymp \frac{R}{\sqrt{\log R}}\to\infty.
}
\tag{24}
\]

Equation (24) locates the construction exactly outside the sufficient compactness class of WI-387.

## 3. The sideband retains 1/log R Fourier mass across a fixed packet

Let

\[
\Phi(\xi)=\int\phi(s)e^{i\xi s}\,ds.
\tag{25}
\]

Because `\Phi(0)=\int\phi\ne0`, continuity gives constants `\delta,a>0` such that

\[
|\Phi(v)|\ge a
\qquad(|v|\le\delta).
\tag{26}
\]

The modulated transform is

\[
V_R(\xi)
=\frac12\bigl(\Phi(\xi-R)+\Phi(\xi+R)\bigr),
\tag{27}
\]

and therefore

\[
U_R(\xi)
:=\int\nu_R(s)e^{i\xi s}\,ds
=
\frac{V_R(\xi)-\alpha_R\Phi(\xi)}{b_R}.
\tag{28}
\]

Since `\phi` is smooth and compactly supported, `\Phi` decays faster than every power. Uniformly for `|\xi-R|\le\delta`, equations (26)--(28), `\alpha_R\to0`, and `b_R\to1/\sqrt2` imply

\[
|U_R(\xi)|\ge a_0>0
\tag{29}
\]

for all sufficiently large `R`. The base packet `\Phi(\xi)` is superpolynomially small there, while the sideband coefficient is only `(\log R)^{-1/2}`. Thus for the transform `G_R` of (20),

\[
\boxed{
|G_R(i\xi)|^2\ge \frac{c_0c}{\log R}
\qquad(|\xi-R|\le\delta)
}
\tag{30}
\]

for some fixed `c_0>0` and all sufficiently large `R`.

## 4. Riemann--von Mangoldt supplies zero-dense carrier windows

The classical Riemann--von Mangoldt formula gives

\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\tag{31}
\]

Partition `[T,2T]` into intervals of length `2\delta`. Since

\[
N(2T)-N(T)\asymp T\log T,
\tag{32}
\]

whereas the number of intervals is `O_\delta(T)`, at least one interval contains

\[
\boxed{\Omega_\delta(\log T)}
\tag{33}
\]

zero ordinates counted with multiplicity. Choose a sequence of such intervals and let `R_j` be their centers. Then `R_j\to\infty`, and (30)--(33) give a constant `\kappa>0` such that

\[
\sum_{\gamma\in[R_j-\delta,R_j+\delta]}
 m_\gamma |G_{R_j}(i\gamma)|^2
\ge\kappa.
\tag{34}
\]

Under RH these ordinates are exactly the real spectral frequencies used in the nonnegative WI-387 representation. Setting `g_j=g_{R_j}` proves (2)--(4). Notice that no local zero-density lower bound for *every* fixed interval is needed: a dense interval somewhere in each dyadic block is enough because the adaptive profile is free to move its carrier there.

This is the key scale match. The archimedean form charges a carrier by `O(\log R)`, so allocating only `1/\log R` of the profile mass keeps the gamma budget bounded. Riemann--von Mangoldt supplies `Omega(\log R)` sampled frequencies in a suitable fixed-width packet, exactly compensating that dilution.

## 5. Exact source perforation can be imposed diagonally

The preceding construction concerns the unperforated fixed-width profiles appearing in the abstract tightness condition of WI-387. It is not an artifact of ignoring Desogus's exact source zeros.

WI-386 proves that for **each fixed** smooth profile, the source-slot perforation converges back to that profile in the quantities needed by the Weil form as the endpoint `A_k=\log(k+1)` tends to infinity; WI-384 supplies the prime-power sparsity behind the vanishing fixed-window hole measure. Uniform `H^1` control was needed in WI-387 only to make that transfer uniform over all `k` at once.

For the present sequence, fix `j` first. Because `g_j` is a single smooth compactly supported profile, choose an endpoint index `k_j` so large that the corresponding perforated positive lobe `p_j` satisfies

\[
\|p_j-g_j\|_1=o_j((\log R_j)^{-1/2})
\tag{35}
\]

and its archimedean form error is `<\beta/2`. The fixed-profile convergence permits this diagonal choice even though the constants deteriorate with `j`. Fourier transforms differ uniformly by at most the `L^1` error, so (30) survives, after normalization, with only a fixed-factor loss. Reflecting the lobe with odd sign gives the exact source-zero two-lobe trial used in WI-386.

Thus one can simultaneously retain a strict negative archimedean margin and an `Omega(1)` high-zero sampled packet after imposing the exact source slots. Source exactness therefore does not imply the spectral tightness missing from WI-387.

This diagonal statement deliberately makes no claim that the resulting endpoint phases produce a positive Weil floor. The chosen `k_j` are used only to show compatibility between source exactness and high-frequency escape; controlling the factors `sin^2(\gamma A_{k_j}/2)` is a separate problem.

## 6. Prior art, novelty, and falsification audit

The individual ingredients are classical. Riemann--von Mangoldt supplies (31); Riemann--Lebesgue and ordinary Fourier decay supply the packet estimates; high-frequency logarithmic energy is consistent with H. Chen and T. Weth, *The Dirichlet problem for the logarithmic Laplacian*, arXiv:1710.03416 / Comm. PDE 44 (2019), whose Fourier symbol is `2\log|\xi|`. Weil's explicit-formula spectral side and the source-slot machinery are already anchored in this line.

The local prior art is also close enough that the distinction matters. WI-358 already uses a real high-frequency modulation to show that a source-derived logarithmic-energy **upper budget** does not force cofinal threshold continuity. WI-385 supplies a gamma-negative fixed lobe; WI-386 proves fixed-profile spectral recurrence; WI-387 identifies uniform zeta-frequency tightness as the exact coefficient-independent compactness hypothesis and bounded `H^1` as one sufficient condition. The deduction here is different: it couples a **vanishing-mass** `1/\log R` sideband to a Riemann--von Mangoldt dense zero window, preserving a uniform negative `B_g` margin while forcing a fixed amount of zeta-sampled mass to escape to infinity.

A targeted literature audit checked Weil-form/explicit-formula modulation, logarithmic-Laplacian high-frequency energy, zeta almost-periodicity, and zero-density formulations. It found the classical ingredients and the logarithmic-energy framework, but no source stating this dilute-sideband implication for the WI-387 zeta-sampled tightness condition. That negative search result is not used as a priority claim.

The result would fail if the archimedean carrier cost grew faster than logarithmically, if the adaptive profile were forbidden from centering its carrier on zero-dense windows, or if an additional admissibility condition controlled the zeta-sampled tail directly. Those are precisely the possible inputs a stronger theorem must exploit.

## Evidence boundary

- **Classical / literature-backed:** Riemann--von Mangoldt; Riemann--Lebesgue; rapid Fourier decay of `C_c^\infty`; elementary translation/difference estimates; logarithmic-Laplacian context for the `\log R` scale.
- **Inherited local evidence:** the exact gamma functional and a strict gamma-negative fixed lobe from WI-385/WI-386; fixed-profile source-perforation convergence from WI-384/WI-386; the uniform spectral-tightness interface of WI-387.
- **Exact deduction here:** the orthogonal dilute-sideband construction; `O(\log R)` carrier cost; preservation of `B_g\le-\beta`; the `1/\log R` packet lower bound; placement on `Omega(\log R)` zero-dense windows; failure of uniform zeta-frequency tightness; diagonal compatibility with exact source perforation.
- **Conditional interface:** the use of those ordinates as the nonnegative spectral frequencies in WI-387 is under RH, exactly as in WI-386/WI-387. The Riemann--von Mangoldt counting statement itself is unconditional.
- **Not claimed:** a positive coercive gap, a contradiction to RH, a new simple-critical-zero proportion, or a counterexample to WI-387. The theorem only blocks deriving WI-387 tightness from negative gamma energy plus source exactness.