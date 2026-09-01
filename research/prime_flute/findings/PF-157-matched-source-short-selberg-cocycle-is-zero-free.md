# PF-157 — matched source-short Selberg cocycle is holomorphic and zero-free on `Re s > 0`

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + DECISIVE-NEGATIVE/BOUNDARY` for the source-Margulis-short Selberg-factor branch. PF-156 proves that the complete repeated Selberg packets of the canonically matched short primitive geodesics have an absolutely summable prime/shift difference for every fixed admissible smooth test function. The present finding applies that estimate to the **actual local Selberg factor** and upgrades the cancellation to a locally normally convergent relative logarithmic derivative on the whole half-plane `Re s>0`. After one harmless base-point normalization, the corresponding infinite short-core relative factor is holomorphic and has **no zeros anywhere in that half-plane**.

Thus the infinitely many pinching prime-flute geodesics do not produce a hidden critical-line zero divisor after the natural marked subtraction against the exact all-composite shift clone. Any zero set of a future full relative Selberg/scattering object must come from geometric sectors omitted here or from an independently justified continuation, not from the matched source-short local factors themselves.

This is **not** a full relative Selberg zeta function for the infinite flute.

## Claim

For one primitive hyperbolic geodesic of length `L>0`, define the standard local Selberg factor

\[
Z_L(s)
:=
\prod_{m=0}^{\infty}
\left(1-e^{-(s+m)L}\right),
\qquad
\operatorname{Re}s>0.
\tag{1}
\]

It is holomorphic and nonzero on `Re s>0`. Its logarithmic derivative is

\[
\boxed{
\frac{d}{ds}\log Z_L(s)
=
\sum_{k\ge1}
\frac{L e^{-skL}}{1-e^{-kL}}
=
\sum_{k\ge1}
\frac{L}{2\sinh(kL/2)}
e^{-(s-\frac12)kL}.
}
\tag{2}
\]

Let `S_*` be the complete source Margulis-short simple primitive family from PF-138/PF-156, let

\[
L_\eta:=\ell(\eta),
\qquad
L_\eta^+:=\ell_+(\eta),
\tag{3}
\]

and put

\[
\tau_\eta:=\log\frac{L_\eta^+}{L_\eta}.
\tag{4}
\]

PF-156 proves

\[
\boxed{
\sum_{\eta\in S_*}|\tau_\eta|<\infty.
}
\tag{5}
\]

Define the relative short-core logarithmic derivative formally by

\[
G_*(s)
:=
\sum_{\eta\in S_*}
\left[
\frac{d}{ds}\log Z_{L_\eta^+}(s)
-
\frac{d}{ds}\log Z_{L_\eta}(s)
\right].
\tag{6}
\]

Then:

1. the series in (6) converges **absolutely and locally uniformly** on
   \[
   \mathbb H_0:=\{s\in\mathbb C:\operatorname{Re}s>0\};
   \tag{7}
   \]
2. therefore `G_*` is holomorphic on `H_0`;
3. for any base point `s_0 in H_0`, the normalized finite products
   \[
   D_E(s;s_0)
   :=
   \prod_{\eta\in E}
   \frac{Z_{L_\eta^+}(s)}{Z_{L_\eta}(s)}
   \frac{Z_{L_\eta}(s_0)}{Z_{L_\eta^+}(s_0)},
   \tag{8}
   \]
   indexed by finite subsets `E subset S_*`, converge locally uniformly as `E` exhausts `S_*` to
   \[
   \boxed{
   D_*(s;s_0)
   =
   \exp\!\left(
   \int_{s_0}^{s}G_*(w)\,dw
   \right);
   }
   \tag{9}
   \]
4. in particular,
   \[
   \boxed{
   D_*(s;s_0)\neq0
   \qquad
   (\operatorname{Re}s>0).
   }
   \tag{10}
   \]

Changing `s_0` only multiplies `D_*` by a nonzero constant. Hence the zero-free conclusion is normalization-independent.

## 1. The Selberg logarithmic derivative is exactly a PF-156 packet

For fixed `L>0` and `Re s>0`, the Euler product (1) converges normally on compact subsets. Differentiating gives

\[
\frac{d}{ds}\log Z_L(s)
=
\sum_{m\ge0}
\frac{L e^{-(s+m)L}}
{1-e^{-(s+m)L}}.
\tag{11}
\]

Expanding the denominator geometrically and interchanging the absolutely convergent sums yields

\[
\sum_{m\ge0}\sum_{k\ge1}
L e^{-k(s+m)L}
=
\sum_{k\ge1}
\frac{L e^{-skL}}{1-e^{-kL}},
\tag{12}
\]

which is the first form in (2). Since

\[
1-e^{-x}
=
2e^{-x/2}\sinh(x/2),
\tag{13}
\]

the second form follows.

Now use the PF-156 notation

\[
\mathcal T_L(\phi)
=
\sum_{k\ge1}
\frac{L}{2\sinh(kL/2)}\phi(kL).
\tag{14}
\]

With

\[
\phi_s(x):=e^{-(s-\frac12)x},
\tag{15}
\]

equation (2) is exactly

\[
\boxed{
\frac{d}{ds}\log Z_L(s)
=
\mathcal T_L(\phi_s).
}
\tag{16}
\]

So no new artificial generating function has been introduced: the analytic family here is the standard local Selberg factor itself.

## 2. PF-156 is uniform on compact subsets of `Re s>0`

The function entering the PF-156 sampling lemma simplifies to

\[
F_s(x)
=
\frac{x}{2\sinh(x/2)}\phi_s(x)
=
\frac{x e^{-sx}}{1-e^{-x}}.
\tag{17}
\]

Fix a compact set `K subset H_0` and write

\[
\sigma:=\inf_{s\in K}\operatorname{Re}s>0.
\tag{18}
\]

Near `x=0`, the Bernoulli expansion gives

\[
\frac{x}{1-e^{-x}}
=
1+\frac{x}{2}+O(x^2),
\tag{19}
\]

so `F_s`, `F_s'`, and `F_s''` are uniformly bounded there for `s in K`. For large `x`,

\[
F_s(x)=O_K(xe^{-\sigma x}),
\qquad
F_s'(x)=O_K((1+x)e^{-\sigma x}),
\qquad
F_s''(x)=O_K((1+x)e^{-\sigma x}).
\tag{20}
\]

Consequently

\[
\sup_{s\in K}
\left(
\|F_s'\|_{L^1}
+
L_*\|F_s''\|_{L^1}
\right)
<\infty
\tag{21}
\]

for every fixed finite `L_*>0`.

PF-156 proves the logarithmic-length Lipschitz estimate

\[
|\mathcal T_{L'}(\phi)-\mathcal T_L(\phi)|
\le
\left(
\|F_\phi'\|_1+L_*\|F_\phi''\|_1
\right)
\left|\log\frac{L'}L\right|
\tag{22}
\]

whenever `L,L'<=L_*`. Applying (22) uniformly to `phi_s`, `s in K`, gives a constant `C_K` such that

\[
\boxed{
\sup_{s\in K}
\left|
\frac{d}{ds}\log Z_{L'}(s)
-
\frac{d}{ds}\log Z_L(s)
\right|
\le
C_K
\left|\log\frac{L'}L\right|.
}
\tag{23}
\]

PF-156 also supplies one finite `L_*` containing every interpolation between the matched lengths in `S_*`.

Combining (23) with (5) gives the Weierstrass majorant

\[
\sum_{\eta\in S_*}
\sup_{s\in K}
\left|
\frac{d}{ds}\log Z_{L_\eta^+}(s)
-
\frac{d}{ds}\log Z_{L_\eta}(s)
\right|
<\infty.
\tag{24}
\]

This proves absolute local-uniform convergence of (6), hence holomorphy of `G_*`.

## 3. The normalized infinite relative factor exists

The half-plane `H_0` is simply connected. Therefore the holomorphic function `G_*` has a primitive. Define `D_*` by (9).

For a finite `E`, each local factor `Z_L` is nonzero on `H_0`, so the logarithmic derivative of (8) is

\[
\frac{d}{ds}\log D_E(s;s_0)
=
\sum_{\eta\in E}
\left[
\frac{d}{ds}\log Z_{L_\eta^+}(s)
-
\frac{d}{ds}\log Z_{L_\eta}(s)
\right]
=:G_E(s),
\tag{25}
\]

and `D_E(s_0;s_0)=1`. Thus

\[
D_E(s;s_0)
=
\exp\!\left(
\int_{s_0}^{s}G_E(w)\,dw
\right).
\tag{26}
\]

Local-uniform convergence `G_E -> G_*` implies local-uniform convergence of the path integrals on every compact subset of `H_0`, and therefore

\[
D_E(s;s_0)\longrightarrow D_*(s;s_0)
\tag{27}
\]

locally uniformly.

Equation (9) now proves the zero-free statement directly: an exponential of a finite holomorphic primitive never vanishes. There is no Hurwitz-limit loophole and no hidden choice of logarithm.

If `s_1 in H_0` is another base point, then

\[
D_*(s;s_1)
=
\frac{D_*(s;s_0)}
{D_*(s_1;s_0)}.
\tag{28}
\]

Thus the base-point normalization changes only a nonzero scalar.

## 4. The critical-line consequence is negative

The natural Selberg spectral variable has critical axis `Re s=1/2`. The whole half-plane

\[
\operatorname{Re}s>0
\tag{29}
\]

contains that axis. Therefore the normalized factor generated by the **entire matched source Margulis-short family**, with all repetitions included through the local Selberg factors, has no zero at any point of `Re s=1/2`.

This rules out the branch

```text
infinitely many prime-flute pinching geodesics
    -> divide by the exact all-composite matched pinching sector
    -> relative short-core Selberg factor
    -> critical-line zero divisor
    -> RH selector.
```

The third arrow fails in the strongest possible way on the domain proved here: the factor is holomorphic and zero-free.

The boundary `Re s=0` should not be reinterpreted as a new arithmetic critical line. Already for one local factor,

\[
Z_L(s)=0
\quad\Longleftrightarrow\quad
s=-m+\frac{2\pi i n}{L},
\qquad
m\in\mathbb Z_{\ge0},\ n\in\mathbb Z,
\tag{30}
\]

so the first elementary length-dependent zero lattice lies on `Re s=0`. The present argument deliberately makes no continuation or cancellation claim across that boundary.

## 5. Prior art and novelty audit

The local factor (1) and its role in hyperbolic degeneration are classical.

- **M. Schulze**, *On the resolvent of the Laplacian on functions for degenerating surfaces of finite geometry*, Journal of Functional Analysis 236 (2006), 120--160, DOI `10.1016/j.jfa.2006.01.005`, arXiv `math/0410434`. For geometrically finite surfaces of fixed topological type with finitely many pinched geodesics, Schulze divides the Selberg zeta by the product of the pinching local factors and proves convergence to the limit zeta for `Re s>1/2`.
- **M. Avdispahić, J. Jorgenson, L. Smajlović**, *Asymptotic Behavior of the Selberg Zeta Functions for Degenerating Families of Hyperbolic Manifolds*, Communications in Mathematical Physics 310 (2012), 217--236, DOI `10.1007/s00220-011-1408-5`. They likewise isolate the product of local pinching factors and prove convergence of the quotient for `Re s>(d-1)/2` in dimensions two and three.
- **J. Jorgenson, R. Lundelius**, *A regularized heat trace for hyperbolic Riemann surfaces of finite volume*, Commentarii Mathematici Helvetici 72 (1997), 636--659, DOI `10.1007/S000140050039`, is the finite-volume pinching/heat source already used directly in PF-156.

Those results explain why the local factor is the correct classical object; they do **not** prove the present infinite-family statement. Their degeneration frameworks pinch only finitely many distinguished geodesics on finite-topology/geometrically finite surfaces. Here one fixed infinite-type prime flute contains infinitely many source Margulis-short primitives and the ordinary absolute orbital measure is nowhere locally finite by PF-036.

Directed searches around relative Selberg zeta functions, pinching local factors, geometrically finite degeneration, and infinite-type hyperbolic surfaces recovered the classical finite-pinching theory above but did not locate a theorem that directly treats this exact countably infinite matched `ell^1` logarithmic-length deformation. No general novelty is claimed for the analytic estimate itself. The durable project-specific content is the composition

\[
\boxed{
\text{PF-109/PF-138/PF-156 } \ell^1
\text{ matched short-length defect}
+
\text{classical local Selberg factor}
\Longrightarrow
\text{normal relative log-derivative convergence and a zero-free cocycle on }Re\,s>0.
}
\tag{31}
\]

The novelty classification is therefore a **prime-flute boundary result**, not a new general Selberg-zeta theorem.

## 6. Scope and falsification boundary

PF-157 does **not** construct a full relative Selberg zeta for the prime/shift pair. In particular it does not control:

- primitive geodesics outside the source Margulis-short family;
- cusp-winding classes or the universal parabolic sector of PF-103/PF-117;
- a full relative trace formula;
- the global squared-resolvent `S_1` gate of PF-146--PF-148;
- wave/scattering completeness;
- resonances or meromorphic continuation through continuous spectrum;
- a relative determinant of the Laplacians;
- any correspondence with Riemann zeros.

The distinction is essential because the canonical README falsification controls explicitly reject conclusions drawn from a selected orbit sector when omitted primitive sectors can restore a different analytic boundary. PF-157 is retained precisely as a **negative** result for the natural pinching-sector escape left by PF-156, not as evidence that the selected factor is the full dynamical object.

A later adversary can falsify the finding through a short chain:

1. check the standard local factor (1) and logarithmic derivative identity (2);
2. verify the exact simplification `F_s(x)=x e^{-sx}/(1-e^{-x})`;
3. verify uniform `W^{1,1}` control of `F_s'` on compact subsets of `Re s>0`;
4. apply PF-156's logarithmic-length Lipschitz bound and its persisted `sum |tau_eta|<infinity`;
5. use the Weierstrass M-test to obtain local-normal convergence of (6);
6. integrate the resulting holomorphic function on the simply connected half-plane and compare with finite normalized products;
7. retain the normalization caveat and all omitted-sector caveats above.

A refutation would require failure of the PF-156 `ell^1` matched short-core estimate, a mistake in the local Selberg logarithmic derivative, loss of uniformity on compact subsets of `Re s>0`, or an invalid identification of the finite normalized product with the exponential primitive.

## Research consequence

PF-156 showed that canonical marked subtraction removes the worst absolute repeated-short-orbit divergence at smooth test-function level. PF-157 now shows what happens when that cancellation is promoted to the standard local Selberg analytic family:

\[
\boxed{
\text{the matched source-short sector becomes a holomorphic, zero-free relative cocycle on }Re\,s>0.
}
\]

So the pinching sector is analytically **tamer** after the all-composite control, but that tameness does not reveal an RH selector. Any future full relative zeta/scattering mechanism must obtain its zeros or singular spectral information from the genuinely global remainder—longer primitive classes, cusp/scattering coupling, or a nonlocal operator comparison—not from the countably infinite source-short local factors already controlled here.