# NB-256 — Microscopic dipoles can inflate signed total variation without buying carrier cancellation

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + SIGNED-COMPLEX-MIXTURE + MICRODIPOLE-CONTROL + EULER-NORMALIZED + SOURCE-NORM-STABLE + CARRIER-STABLE + NB-255-REFINEMENT + METHOD-BOUNDARY + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-255` shows that a signed or complex scalar carrier mixture with Euler-normalized coefficient total variation `V` is guaranteed to remain coherent in a disk of radius at least `c/(WV)`. It therefore identifies `V \gtrsim R/W` as a necessary scale for escaping that particular *worst-case lower bound* on the coherence radius. The open question was whether paying such a large `V` must also create a comparable source, Hardy, or Nyman norm cost.

The answer is already negative for raw coefficient total variation. One can add a pair of almost coincident opposite shells with coefficients `+N` and `-N`, separated by only `H/N^2`. Their Euler-normalized total variation grows like `2N`, while their contribution to the actual smooth shell source tends to zero in both `L^1` and the natural shell-scaled `L^2` norm. Their contribution to the carrier transform also tends to zero uniformly on the relevant `1/W` coherence scale.

Thus `V` is **not an intrinsic conditioning norm of the resulting source**. It can be inflated arbitrarily by microscopic dipoles that neither damage the source norm nor purchase useful carrier cancellation. The `WV` quantity in `NB-255` is a valid worst-case bound, but it can be arbitrarily non-sharp because it forgets the separation scale of opposite coefficients.

A sharper elementary modulus already appears before any zeta input:

\[
M_1(\lambda):=\int |\xi|\,d|\lambda|(\xi),
\qquad
|B_\lambda(z)-1|
\le
|z|e^{W|\Im z|/2}M_1(\lambda).
\]

`NB-255` used only the crude inequality `M_1(\lambda)\le WV/2`. The control below makes `V\to\infty` while keeping `M_1=\Theta(W)` and keeping the actual carrier profile unchanged at scale `1/W`. This does not prove that `M_1` is the final coercive invariant; it shows that any continuation of the signed-carrier route must quotient out or otherwise discount near-cancelling microscopic dipoles instead of treating raw coefficient variation as physical cost.

## 1. Keep the exact Euler normalization of NB-255

Retain the Ford-scale notation of `NB-255`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty,
\tag{1}
\]

and the mesoscopic multi-carrier regime

\[
H\ll W=o(X).
\tag{2}
\]

Let

\[
0<a<b<1,
\qquad
0\le \phi\in C_c^\infty((a,b)),
\qquad
\phi\not\equiv0,
\tag{3}
\]

and define the translated shell

\[
k_\xi(u)
:=
\frac1H\phi\!\left(\frac{u-X-\xi}{H}\right).
\tag{4}
\]

As in `NB-255`, it is cleaner to work with the Euler-tilted coefficient measure `lambda`. If `nu` is the actual shell coefficient measure, put

\[
d\lambda(\xi):=e^{-r\xi/X}\,d\nu(\xi),
\qquad
\lambda(\mathbb R)=1.
\tag{5}
\]

Conversely, for any finite signed or complex `lambda` of total mass one, define

\[
d\nu(\xi):=e^{r\xi/X}\,d\lambda(\xi).
\tag{6}
\]

Then the Euler normalization is exact:

\[
\int e^{-r\xi/X}\,d\nu(\xi)
=
\int d\lambda(\xi)
=1.
\tag{7}
\]

For a zero `rho=beta+i gamma`, the same cancellation used in `NB-255` turns the carrier factor into

\[
B_\lambda(z_\rho)
:=
\int e^{i\xi z_\rho}\,d\lambda(\xi),
\qquad
z_\rho:=(\gamma-t_0)+i(1-\beta).
\tag{8}
\]

Thus the source-side question can be asked directly in terms of `lambda`: does making `||lambda||_{TV}` large necessarily change either the actual smooth source or its Ford-scale carrier profile by a comparable amount?

## 2. A baseline with an ordinary `1/W` coherence window

Use the simple positive baseline

\[
\lambda_0
:=
\frac12\delta_{-W/2}
+
\frac12\delta_{W/2}.
\tag{9}
\]

It has

\[
\lambda_0(\mathbb R)=1,
\qquad
\|\lambda_0\|_{\rm TV}=1,
\tag{10}
\]

and

\[
B_0(z)
:=B_{\lambda_0}(z)
=
\cos\!\left(\frac{Wz}{2}\right).
\tag{11}
\]

In particular, on the real axis,

\[
|u|\le \frac{\pi}{3W}
\quad\Longrightarrow\quad
B_0(u)\ge \cos(\pi/6)=\frac{\sqrt3}{2}.
\tag{12}
\]

So this baseline has exactly the order-`1/W` central coherence predicted by `NB-254`.

Now choose `N -> infinity` and set

\[
\varepsilon_N:=\frac{H}{N^2}.
\tag{13}
\]

For all sufficiently large `N`, `0<epsilon_N<W/2`. Add the zero-mass microscopic dipole

\[
\boxed{
\lambda_N
:=
\lambda_0
+N\delta_0
-N\delta_{\varepsilon_N}.
}
\tag{14}
\]

The Euler normalization is unchanged because the added dipole has total mass zero:

\[
\lambda_N(\mathbb R)=1.
\tag{15}
\]

The support still spans `W`, but, because the four atoms are distinct,

\[
\boxed{
V_N:=\|\lambda_N\|_{\rm TV}=1+2N\to\infty.
}
\tag{16}
\]

Hence the raw conditioning parameter used in `NB-255` can be made arbitrarily large without changing the carrier span or the Euler return.

## 3. The actual smooth source converges back to the baseline

Let `nu_N` be obtained from `lambda_N` by (6), and write

\[
h_N(u):=\int k_\xi(u)\,d\nu_N(\xi),
\qquad
h_0(u):=\int k_\xi(u)\,d\nu_0(\xi).
\tag{17}
\]

The dipole contribution is exactly

\[
h_N-h_0
=
N(k_0-k_{\varepsilon_N})
-
N\big(e^{r\varepsilon_N/X}-1\big)k_{\varepsilon_N}.
\tag{18}
\]

For `1<=p<=infinity`, translation of the smooth shell gives

\[
\|k_0-k_\varepsilon\|_p
\le
|\varepsilon|\,H^{-2+1/p}\|\phi'\|_p.
\tag{19}
\]

For `p=1`, using `||k_epsilon||_1=||phi||_1` and `epsilon_N=H/N^2`, (18) yields

\[
\begin{aligned}
\|h_N-h_0\|_1
&\le
N\frac{\varepsilon_N}{H}\|\phi'\|_1
+
N\big|e^{r\varepsilon_N/X}-1\big|\|\phi\|_1\\
&\le
\frac{\|\phi'\|_1}{N}
+
O_{\phi,r}\!\left(\frac{H}{NX}\right)
=o(1).
\end{aligned}
\tag{20}
\]

The same calculation at the natural `L^2` shell scale gives

\[
\boxed{
H^{1/2}\|h_N-h_0\|_2
\le
\frac{\|\phi'\|_2}{N}
+
O_{\phi,r}\!\left(\frac{H}{NX}\right)
=o(1).
}
\tag{21}
\]

Here `H/X=1/(YJ)->0`. Thus there is no lower bound of the form

\[
\|h_\nu\|_{L^1}\gtrsim \|\lambda\|_{\rm TV}
\quad\text{or}\quad
H^{1/2}\|h_\nu\|_{L^2}\gtrsim \|\lambda\|_{\rm TV}
\tag{22}
\]

for arbitrary signed scalar mixtures of the class allowed in `NB-255`. The same source, up to `o(1)`, admits representations with coefficient variation tending to infinity.

This is not merely cancellation in an abstract coefficient space. It occurs after the actual shells have been translated and combined: two enormous opposite coefficients attached to almost coincident smooth shells produce an `o(1)` physical perturbation.

## 4. The extra variation also buys essentially no carrier cancellation

The transformed dipole is equally transparent. From (14),

\[
\boxed{
B_N(z)
=
B_0(z)
+N\big(1-e^{i\varepsilon_N z}\big).
}
\tag{23}
\]

For complex `z`,

\[
|1-e^{i\varepsilon z}|
\le
\varepsilon |z|e^{\varepsilon|\Im z|}.
\tag{24}
\]

Hence for every fixed `C>0`,

\[
\sup_{|z|\le C/W}
|B_N(z)-B_0(z)|
\le
\frac{CH}{NW}
\exp\!\left(\frac{CH}{N^2W}\right)
=o(1).
\tag{25}
\]

The last limit uses `H/W->0`. Therefore the carrier profile of `lambda_N` converges uniformly to the positive baseline throughout the entire natural `1/W` coherence neighborhood, even though

\[
V_N\sim2N\to\infty.
\tag{26}
\]

This directly exhibits the non-sharpness that `NB-255` left open. Its universal lower bound guarantees coherence only out to roughly

\[
\frac1{WV_N}\asymp\frac1{WN},
\tag{27}
\]

while this family remains coherent on the much larger baseline scale `Theta(1/W)`. The large `V_N` has not been converted into spectral cancellation; it has simply been hidden in a microscopic positive-negative dipole.

The same statement survives the small Ford imaginary displacement. If the positive-mixture capacity

\[
J_W:=\frac RW\to\infty,
\tag{28}
\]

then in the corresponding critical layer `X(1-beta)=log J_W+O(1)` one has

\[
W(1-\beta)
=
O\!\left(\frac{\log J_W}{J_W}\right)
=o(1).
\tag{29}
\]

Thus `B_0(z_rho)` remains order one on the matched `1/W` Ford patch, and (25) says that the microscopic dipole does not alter it there. The formal increase in `V` therefore does not move the *actual* coherence boundary for this family.

## 5. `WV` was a worst-case surrogate for a scale-sensitive moment

There is an elementary refinement of the `NB-255` estimate. Since `lambda(R)=1`,

\[
B_\lambda(z)-1
=
\int\big(e^{i\xi z}-1\big)\,d\lambda(\xi).
\tag{30}
\]

Define the first absolute offset moment relative to the chosen carrier center,

\[
M_1(\lambda)
:=
\int |\xi|\,d|\lambda|(\xi).
\tag{31}
\]

For `supp(lambda) subset [-W/2,W/2]`,

\[
\boxed{
|B_\lambda(z)-1|
\le
|z|e^{W|\Im z|/2}M_1(\lambda).
}
\tag{32}
\]

The `NB-255` total-variation estimate follows immediately from

\[
M_1(\lambda)
\le
\frac W2\|\lambda\|_{\rm TV}
=
\frac{WV}{2}.
\tag{33}
\]

But for the microscopic-dipole family,

\[
M_1(\lambda_N)
=
\frac W2+N\varepsilon_N
=
\frac W2+\frac HN
=\frac W2+o(W),
\tag{34}
\]

whereas `V_N -> infinity`. The moment sees the amplitude-times-separation of the dipole; raw total variation sees only its amplitude.

Equation (32) does **not** establish `M_1` as the final source-conditioning invariant. Higher multipoles can create analogous representation effects for other low-frequency seminorms. What it does establish is the direction any useful invariant must take: cancellation cost has to be measured at the scale at which the carrier or source can resolve it, rather than by coefficient mass before near-coincident opposite terms have been quotiented out.

## 6. Consequence for the signed-scalar route

`NB-255` remains mathematically correct: if all one knows is support diameter `W` and coefficient total variation `V`, then `1/(WV)` is a valid compulsory coherence radius. The present control changes the interpretation of that bound.

In particular, the condition

\[
V\gtrsim \frac RW
\tag{35}
\]

is **not by itself evidence that a construction has paid a real norm price or has purchased carrier cancellation**. One may force (35), or make `V` much larger still, by inserting microscopic dipoles whose effect on both the smooth source and the Ford-scale transform is `o(1)`.

Therefore a future attempt to close the signed route by proving a lower bound purely in terms of `V` would attack a representation artifact. A meaningful conditioning quantity must first identify mixtures that are close after smooth-shell synthesis. Two natural ways to do that are:

1. work with a scale-sensitive norm or transport/flat-type seminorm of the tilted measure rather than raw total variation; or
2. restrict to a stable carrier dictionary, for example by imposing a minimum separation comparable to `H`, and then prove that the resulting synthesis map is coercive on that restricted coefficient class.

The second option is especially concrete. The construction above uses separation `epsilon_N/H=1/N^2 -> 0`. A theorem showing that a useful multi-carrier construction can always be reduced to `Omega(H)`-separated centers without losing its cancellation would remove this degeneracy and could make coefficient variation meaningful again.

## 7. Adversarial review and method boundaries

### 7.1 This does not produce a successful Nyman--Beurling approximant

The family is a **control against a proposed conditioning argument**, not a new approximation theorem. It shows that raw coefficient variation cannot be converted automatically into a source-norm cost and that large `V` need not represent useful carrier cancellation.

It does not show that the baseline positive mixture, or the dipole-perturbed mixture, closes the Nyman--Beurling distance.

### 7.2 Very large `V` still interacts with arithmetic error bookkeeping

The PNT/Stieltjes reductions used earlier in the Ford line often bounded componentwise errors by absolute coefficient variation. If one takes `N` so large that `V_N` reaches or exceeds `R/W`, those existing *proof bounds* need not remain uniform. Equation (20) suggests that taking cancellation before absolute values may yield a much better error estimate, but that has not been proved here.

Consequently this finding does **not** claim that an arbitrary `V_N >> R/W` dipole construction is already legal through every arithmetic step of the Nyman route. It establishes the narrower but decisive source-side fact: any arithmetic loss proportional to raw `V_N` would itself be sensitive to a nearly-null representation and should be re-audited before being treated as intrinsic.

### 7.3 The control disappears under a minimum-separation hypothesis

If future scalar-carrier constructions require distinct centers to satisfy

\[
|\xi_j-\xi_k|\gtrsim H,
\tag{36}
\]

then the microscopic dipole (14) is forbidden. No claim is made here that large total variation can always be hidden under such a separated-dictionary constraint. That is a concrete falsifier of the present mechanism and a natural next case to test.

### 7.4 `M_1` is a diagnostic, not yet a coercive theorem

The first moment in (31) captures this particular dipole because it charges amplitude times displacement. It is not proved to control the Hardy/Nyman norm from below, nor is it proved necessary for every form of useful carrier cancellation. The durable conclusion is only that `V` is too representation-sensitive on its own.

## 8. Representation and novelty audit

The mathematical ingredients in (19), (24), and (32) are generic harmonic analysis: translation continuity of a smooth kernel and the elementary estimate for an exponential increment. The phenomenon that a large opposite-sign microscopic dipole is small in weak or transport-sensitive topologies is likewise generic.

The line-specific content is the way this interacts with the exact Euler tilt of `NB-255`, the shell scale `H`, the carrier span `W`, and the Ford coherence question. The construction preserves the **actual Euler normalization exactly**, leaves the synthesized smooth source asymptotically unchanged, and leaves the relevant `1/W` carrier profile asymptotically unchanged while sending the `NB-255` coefficient parameter `V` to infinity.

A fresh prior-art audit on 2026-09-20 searched for signed-measure convolution conditioning, microscopic dipoles, bounded-Lipschitz/transport norms, and Nyman--Beurling signed smooth carrier constructions. It found the standard generic weak/transport viewpoint but no Nyman--Beurling or Ford result that supplies the missing scale-sensitive coercive norm or invalidates the explicit control above. No new external result is load-bearing, so `SOURCES.md` requires no addition.

This finding is therefore classified as a **route refinement / method boundary**, not as a theorem about the actual zero set of `zeta` and not as progress on the final Nyman--Beurling distance by itself.

## 9. Next test

The immediate question is no longer

\[
\text{``does }V\asymp R/W\text{ cost too much?''}
\]

but rather:

\[
\boxed{
\text{what scale-sensitive coefficient/source norm must become large to suppress the }1/W\text{ carrier window?}
}
\tag{37}
\]

A concrete next pass should test one of two routes. First, impose `Omega(H)` separation between carrier centers and determine whether the translate family of `phi` has a quantitative lower frame/Riesz bound strong enough to turn useful signed cancellation into an unavoidable source norm. Second, keep arbitrary centers but rewrite the arithmetic and Hardy estimates in a quotient norm that measures the synthesized source (or a flat/transport-type norm of `lambda`) rather than its nonunique raw coefficient decomposition.

A decisive positive result would be a coercive inequality for such an **effective** conditioning norm together with a proof that destroying the Ford coherence window forces that norm to reach the relevant `R/W` scale. A decisive negative result would be a legal, Euler-normalized family whose synthesized source stays controlled while its actual carrier transform—not merely its raw coefficient variation—loses order-one coherence throughout the Ford patch.