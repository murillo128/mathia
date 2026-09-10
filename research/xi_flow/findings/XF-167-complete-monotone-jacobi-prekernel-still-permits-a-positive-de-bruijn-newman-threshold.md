---
type: negative
research_line: xi_flow
finding_id: XF-167
status: canonical
---

# XF-167 — Complete-monotone Jacobi prekernel still permits a positive de Bruijn–Newman threshold

**Confidence:** high. The source construction, Jacobi identity, complete-monotonicity statement, Fourier factorization, and location of the added nonreal zeros are exact. The upper bound on the new transition uses de Bruijn's classical zero-strip contraction, already anchored in `SOURCES.md`; persistence of a nonreal zero for small positive heat time is a direct Rouché argument.

## Statement

XF-166 left complete monotonicity of the reconstructed theta prekernel as the cheapest possible discriminator between Xi and the shifted-source controls. Complete monotonicity is still too weak.

Let

\[
F_\Xi(x):=\sum_{n\ge1}e^{-\pi n^2x},
\qquad
\Theta_\Xi(x):=1+2F_\Xi(x),
\qquad
S_\Xi(u):=e^uF_\Xi(e^{4u}),
\tag{1}
\]

so that

\[
\Phi(u)=\frac18\bigl(S_\Xi''(u)-S_\Xi(u)\bigr).
\tag{2}
\]

Fix `c>0` and introduce the positive symmetric three-point measure

\[
\nu_c
:=\frac12\delta_0
 +\frac{1}{4\cosh c}(\delta_c+\delta_{-c}).
\tag{3}
\]

Its normalization is chosen so that

\[
\int_{\mathbb R}\cosh a\,d\nu_c(a)=1.
\tag{4}
\]

Define the shifted source and prekernel

\[
\rho_c(u):=\int \Phi(u+a)\,d\nu_c(a)
=\frac12\Phi(u)
 +\frac{\Phi(u+c)+\Phi(u-c)}{4\cosh c},
\tag{5}
\]

\[
S_c(u):=\int S_\Xi(u+a)\,d\nu_c(a).
\tag{6}
\]

Then `rho_c` is even, strictly positive, real analytic, and has all finite quadratic-exponential moments. Moreover

\[
S_c''-S_c=8\rho_c
\tag{7}
\]

and the exact real-axis Jacobi reflection survives:

\[
\boxed{S_c(u)-S_c(-u)=-\sinh u.}
\tag{8}
\]

Consequently

\[
F_c(x):=x^{-1/4}S_c\!\left(\frac14\log x\right),
\qquad
\Theta_c(x):=1+2F_c(x)
\tag{9}
\]

satisfy

\[
\boxed{\Theta_c(x)=x^{-1/2}\Theta_c(1/x)}
\qquad(x>0).
\tag{10}
\]

Unlike the synthetic Green lift of XF-166, this prekernel is manifestly a positive Laplace superposition:

\[
\boxed{
F_c(x)
=\frac12F_\Xi(x)
+\frac{e^c}{4\cosh c}F_\Xi(e^{4c}x)
+\frac{e^{-c}}{4\cosh c}F_\Xi(e^{-4c}x).
}
\tag{11}
\]

Hence `F_c` is completely monotone on `(0,infinity)`. Its representing positive discrete Laplace measure is explicitly carried by three scaled square lattices,

\[
\boxed{
\mu_c
=\frac12\sum_{n\ge1}\delta_{\pi n^2}
+\frac{e^c}{4\cosh c}\sum_{n\ge1}\delta_{\pi e^{4c}n^2}
+\frac{e^{-c}}{4\cosh c}\sum_{n\ge1}\delta_{\pi e^{-4c}n^2}.
}
\tag{12}
\]

Thus positivity, exact real-axis Jacobi inversion, cusp normalization, and complete monotonicity still do not force the single Xi square-lattice spectrum.

The zero geometry is even more decisive. Let

\[
\mathcal H_t^{(c)}(z)
:=\int_0^\infty e^{tu^2}\rho_c(u)\cos(zu)\,du.
\tag{13}
\]

At `t=0`, translation of the even source gives the exact Fourier multiplier

\[
\boxed{
\mathcal H_0^{(c)}(z)
=\left(\frac12+\frac{\cos(cz)}{2\cosh c}\right)H_0(z)
=\frac{\cosh c+\cos(cz)}{2\cosh c}H_0(z).
}
\tag{14}
\]

The added factor has the simple nonreal zeros

\[
\boxed{
z_{k,\pm}=\frac{(2k+1)\pi}{c}\pm i,
\qquad k\in\mathbb Z.
}
\tag{15}
\]

At the same time, all zeros of `H_0` lie in `|Im z|<1` by the standard critical-strip location of the nontrivial zeta zeros under

\[
H_0(z)=\frac18\xi\!\left(\frac12+\frac{iz}{2}\right).
\tag{16}
\]

Therefore every zero of `H_0^(c)` lies in the closed strip `|Im z|<=1`. De Bruijn's strip-contraction theorem then implies that `mathcal H_t^(c)` has only real zeros for `t>=1/2`. On the other hand, any zero in `(15)` persists off the real axis for all sufficiently small positive `t` by locally uniform convergence and Rouché's theorem. If

\[
\Lambda_c:=\inf\{t:\mathcal H_t^{(c)}\text{ has only real zeros}\},
\tag{17}
\]

then

\[
\boxed{0<\Lambda_c\le\frac12.}
\tag{18}
\]

So **complete monotonicity of the Jacobi-reflecting prekernel is not a source-side coercivity criterion for the de Bruijn–Newman transition**. The surviving rigidity has to retain more of the actual theta coefficient law: at minimum the single square-lattice support and its exact weights, or an equivalent complex/arithmetic constraint that rules out positive mixtures of scaled theta spectra.

## 1. Shift averaging preserves the Xi source class

The Xi source is even and positive. Positivity for `u>=0` is immediate term-by-term from the normalization

\[
\Phi(u)
=\sum_{n\ge1}\pi n^2e^{5u}
\bigl(2\pi n^2e^{4u}-3\bigr)e^{-\pi n^2e^{4u}},
\tag{19}
\]

because `2pi-3>0`; evenness supplies the negative half-line. Therefore `(5)` is strictly positive. Finite shifts preserve real analyticity and the double-exponential tail on each side, so every integral in `(13)` converges locally uniformly for finite complex `t` and `z`.

Linearity of `(2)` gives `(7)`. To prove `(8)`, use symmetry of `nu_c` to rewrite

\[
\int S_\Xi(-u+a)\,d\nu_c(a)
=\int S_\Xi(-u-a)\,d\nu_c(a).
\tag{20}
\]

Then the Xi reflection identity from XF-166 yields

\[
\begin{aligned}
S_c(u)-S_c(-u)
&=\int\bigl(S_\Xi(u+a)-S_\Xi(-u-a)\bigr)\,d\nu_c(a)\\
&=-\int\sinh(u+a)\,d\nu_c(a)\\
&=-\sinh u\int\cosh a\,d\nu_c(a),
\end{aligned}
\tag{21}
\]

because the `sinh a` moment vanishes by symmetry. Equation `(4)` proves `(8)`, and the same algebra as XF-166 converts `(8)` into the Jacobi law `(10)`.

This already gives a nontrivial family of genuine positive source perturbations satisfying the same real-axis reciprocal normalization as Xi. The next step shows that they also satisfy the complete-monotonicity property proposed as the immediate gate in XF-166.

## 2. The reconstructed prekernel is completely monotone

Put `x=e^(4u)`. A shifted Xi prekernel obeys

\[
x^{-1/4}S_\Xi(u+a)
=e^aF_\Xi(e^{4a}x).
\tag{22}
\]

Substituting the three atoms of `(3)` proves `(11)`. Since

\[
F_\Xi(x)=\sum_{n\ge1}e^{-\pi n^2x},
\tag{23}
\]

`F_Xi` is completely monotone, and positive scaling in both the argument and amplitude preserves complete monotonicity. More explicitly, differentiating `(11)` termwise gives for every integer `m>=0`

\[
(-1)^mF_c^{(m)}(x)
=\int_0^\infty \lambda^m e^{-\lambda x}\,d\mu_c(\lambda)>0,
\tag{24}
\]

with `mu_c` given by `(12)`.

The coefficients in the corresponding theta mixture sum to one:

\[
\frac12+\frac{e^c+e^{-c}}{4\cosh c}=1,
\tag{25}
\]

so

\[
\Theta_c(x)
=\frac12\Theta_\Xi(x)
+\frac{e^c}{4\cosh c}\Theta_\Xi(e^{4c}x)
+\frac{e^{-c}}{4\cosh c}\Theta_\Xi(e^{-4c}x).
\tag{26}
\]

The two scaled terms exchange under `x -> 1/x` by Jacobi inversion, while the unscaled term maps to itself. This provides a second direct proof of `(10)`. It also shows `Theta_c(x)>1` and `Theta_c(x)->1` as `x->infinity` without invoking the Green reconstruction of XF-166.

Equation `(12)` is the crucial boundary. Bernstein-type complete monotonicity sees only positivity of a Laplace representing measure. It does not remember that Xi uses **unit masses on one arithmetic square lattice** rather than a positive mixture of rescaled copies of that lattice.

## 3. The same source has an explicit nonreal zero seam at time zero

Extend `Phi` and `rho_c` evenly to the real line. Their full Fourier transforms are twice their cosine transforms. Translation by `a` multiplies the full transform by `e^{-iaz}`, so `(3)` gives

\[
\int_{\mathbb R}\rho_c(u)e^{izu}\,du
=\left(\frac12+\frac{e^{icz}+e^{-icz}}{4\cosh c}\right)
\int_{\mathbb R}\Phi(u)e^{izu}\,du,
\tag{27}
\]

which is `(14)`.

Solving

\[
\cos(cz)=-\cosh c
\tag{28}
\]

gives exactly `(15)`. These zeros are simple because

\[
\sin\bigl((2k+1)\pi\pm ic\bigr)=\mp i\sinh c\ne0.
\tag{29}
\]

Thus `mathcal H_0^(c)` has nonreal zeros independently of whether RH is true. Even if one of the points `(15)` happened also to be a zero of `H_0`, the product still has an isolated nonreal zero there; simplicity of the added factor is more than is needed for persistence.

Because the source has superexponential decay, `(13)` is jointly locally uniform in `t,z` near `t=0`. Choose a small disk around one zero `(15)` whose closure stays off the real axis and whose boundary contains no zero of `mathcal H_0^(c)`. Uniform convergence on that boundary implies, by Rouché, that `mathcal H_t^(c)` retains the same number of zeros in the disk for all sufficiently small positive `t`. Hence `Lambda_c>0`.

## 4. De Bruijn contracts the entire added seam by time one-half

Under `(16)`, if `rho=beta+i gamma` is a nontrivial zeta zero then the corresponding `H_0` zero `z=x+iy` has

\[
y=1-2\beta.
\tag{30}
\]

The classical critical strip `0<beta<1` therefore puts all `H_0` zeros strictly inside `|y|<1`. The multiplier in `(14)` contributes only the two horizontal rows `(15)`, exactly on `|y|=1`. Thus

\[
Z(\mathcal H_0^{(c)})\subset\{z:|\operatorname{Im}z|\le1\}.
\tag{31}
\]

De Bruijn's zero-strip theorem, in the heat convention used by this line, sends a strip of half-width `Delta` at time zero to

\[
\sqrt{\max(\Delta^2-2t,0)}
\tag{32}
\]

at later time `t`. Setting `Delta=1` proves that all zeros are real by `t=1/2`, hence `Lambda_c<=1/2`. Together with the Rouché lower bound this proves `(18)`.

The number `1/2` is only a universal upper bound for this family; the exact value of `Lambda_c` is not determined here. The point is that it is **strictly positive** despite the full package of source regularity tested above.

## Relation to prior findings

XF-162 isolated the Xi theta-tail hazard. XF-163 showed that Gaussian source tilts preserve that tail jet while translating the heat origin. XF-164 and XF-165 strengthened the no-go against tail-only and finite-jet source criteria. XF-166 then showed that exact real-axis Jacobi inversion, positivity, and cusp normalization can be synthesized for the same negative controls, leaving complete monotonicity and inverse-Laplace support as the immediate next tests.

XF-167 closes the cheaper of those two tests. Rather than deciding whether the particular Green lift of the Gaussian tilt is completely monotone, it constructs a stronger counterexample family for which complete monotonicity is manifest from the start and the zero obstruction is explicit. The result pushes the viable frontier directly to **coefficient-level spectral rigidity**: the locations and weights of the theta Laplace atoms, or an equivalent genuinely complex-modular/arithmetic condition.

## Prior-art and novelty audit

The ingredients are classical separately. Jacobi inversion and the Xi theta prekernel are standard, while de Bruijn's 1950 theorem gives the zero-strip contraction used in `(32)` and is already recorded in `SOURCES.md`. A targeted search across scaled/self-reciprocal theta mixtures, de Bruijn–Newman theta deformations, and Fourier multipliers of shifted Xi kernels did not locate the project-specific combination used here: a positive symmetric translation mixture normalized by a `cosh` moment, whose prekernel is simultaneously Jacobi-reflecting and completely monotone, while its time-zero Fourier transform acquires an explicit nonreal zero seam and therefore a strictly positive transition threshold.

No newly located theorem is load-bearing. The only literature-dependent step beyond standard Xi normalization is the already-registered de Bruijn strip theorem, so `SOURCES.md` requires no update.

## Falsification boundary

This finding does **not** show that the exact Xi square-lattice spectrum is sufficient to force `Lambda=0`; proving that would be essentially the original source problem rather than a classifier test. It only proves that complete monotonicity, even combined with positivity, exact real-axis Jacobi inversion, the Xi differential source extraction, and the standard cusp normalization, does not force that spectrum and does not prevent `Lambda>0`.

Nor does it rule out genuinely complex modular constraints. `Theta_c` is constructed and controlled on the positive real axis; no claim is made that it is a holomorphic modular form with the full theta transformation law in the modular parameter. Likewise, the three-lattice measure `(12)` is a positive discrete spectrum, so the obstruction does not say that discreteness alone is insufficient in every strengthened formulation; it says that **positive discrete Laplace structure plus real Jacobi reciprocity still allows scaled-lattice contamination**.

Finally, `(18)` gives only `0<Lambda_c<=1/2`. Determining `Lambda_c` more sharply would not advance the present source gate unless that calculation exposed a coefficient invariant that distinguishes the single Xi lattice from the scaled mixture.

## Consequence for `xi_flow`

Do not spend the next pass trying to prove complete monotonicity of the Gaussian-tilt Green reconstruction as a route to source rigidity. Even if that specific reconstruction failed complete monotonicity, the property itself is now known to coexist with a positive de Bruijn–Newman transition in an explicit positive analytic source family.

The next discriminator should act on the inverse-Laplace measure itself. The cheapest concrete question is whether an exact **single** square-lattice support/weight law can be weakened in any nontrivial way while still quantitatively controlling zero collision: for example, stability under small displacement or reweighting of the atoms, or a complex-theta identity that forbids the scaled-lattice mixture `(12)`. Any useful theorem must do more than identify Xi; it must transport that coefficient rigidity to the mesoscopic source mass or zero geometry responsible for the transition.