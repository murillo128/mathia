# WP-038 — compatible adelic-solenoid Dirichlet energy is rational-square and noncoercive

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the most direct positive-energy route opened by `PC-064`. The compatible-circle inverse limit does force a canonical positive leafwise Dirichlet form once one requires the ordinary circle energies to agree under refinement. But that requirement uniquely rescales level `n` by `n^{-2}`, so the resulting global form is diagonal on the rational character group with symbol `4 pi^2 q^2`. It has arbitrarily soft nonconstant modes, no compact resolvent or heat trace, and its only canonical logarithmic place decomposition is the ordinary product-formula sum of valuations, which gives `log n`, not the Mangoldt prime-power selector. Thus the bare Mathia-native adelic solenoid supplies a genuine global positive geometry, but not the global Weil positivity mechanism.

## 1. The new global candidate from PC-064

`PC-064` identifies the all-level compatible circle refinement with the universal arithmetic solenoid

\[
\Sigma_{\mathbb Q}
=\varprojlim_{m\mid n}(S^1,p_{n,m}),
\qquad
p_{n,m}(z)=z^{n/m},
\]

and hence with

\[
\Sigma_{\mathbb Q}\cong\widehat{\mathbb Q}
\cong(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z
\cong\mathbb A_{\mathbb Q}/\mathbb Q.
\]

This is the first Prime-Circle construction in the current `weil_positivity` search that couples the original archimedean circle and the profinite finite-adic fiber in one intrinsic compact space before any zeta transform is inserted. It therefore deserves the strongest possible version of the obvious positivity test: use the ordinary positive Dirichlet energy of the circles themselves and ask whether it globalizes through the inverse system.

Write each level as `R/Z` with normalized Haar coordinate `theta` and let

\[
\mathcal E_n^0(F)
=\int_0^1 |F'(\theta)|^2\,d\theta
\tag{1}
\]

be the standard circle Dirichlet form. We allow a scalar normalization `a_n>0` at level `n`,

\[
\mathcal E_n=a_n\mathcal E_n^0,
\tag{2}
\]

but require that the same cylinder function have the same energy no matter at which compatible refinement level it is represented.

That compatibility condition forces the normalization uniquely.

## 2. Cover compatibility forces the `n^{-2}` scale

Let `m|n` and put `d=n/m`. In angular coordinates the bonding map is

\[
\theta\longmapsto d\theta\pmod1.
\]

For a smooth function `F` on level `m`, normalized Haar measure is preserved by the covering, while the derivative gains a factor `d`. Therefore

\[
\mathcal E_n^0(F\circ p_{n,m})
=d^2\mathcal E_m^0(F).
\tag{3}
\]

Exact compatibility of (2) means

\[
\mathcal E_n(F\circ p_{n,m})=\mathcal E_m(F),
\]

hence

\[
a_n d^2=a_m.
\tag{4}
\]

Taking `m=1` gives

\[
\boxed{a_n=\frac{a_1}{n^2}.}
\tag{5}
\]

Thus, up to one overall positive constant, there is only one scalar rescaling of the ordinary circle energies that descends to the inverse limit. With `a_1=1`, define on smooth cylinder functions

\[
\boxed{
\mathcal E_\Sigma(F\circ\pi_n)
=\frac1{n^2}\mathcal E_n^0(F).
}
\tag{6}
\]

Equation (3) proves that (6) is independent of the chosen presentation level. Positivity is inherited directly from (1); no RH input, zero data, continuation, or explicit-formula identity is involved.

This is therefore a genuinely Mathia-native positive global form, not a positivity functional imported from zeta.

## 3. Its exact Fourier symbol is rational square

By `PC-064`, the Pontryagin dual of `Sigma_Q` is the discrete additive group `Q`. A rational character `q=k/n` can be represented on level `n` as

\[
\chi_{k/n}(\theta)=e^{2\pi i k\theta}.
\]

Using (6),

\[
\mathcal E_\Sigma(\chi_{k/n})
=\frac1{n^2}(2\pi k)^2
=4\pi^2\left(\frac kn\right)^2.
\tag{7}
\]

Hence the closure of the cylinder form is exactly

\[
\boxed{
\mathcal E_\Sigma(f)
=4\pi^2\sum_{q\in\mathbb Q}q^2|\widehat f(q)|^2,
}
\tag{8}
\]

with form domain

\[
\operatorname{Dom}\mathcal E_\Sigma
=\left\{f\in L^2(\Sigma_{\mathbb Q}):
\sum_{q\in\mathbb Q}q^2|\widehat f(q)|^2<\infty\right\}.
\tag{9}
\]

The associated nonnegative self-adjoint leafwise Laplacian therefore has eigenvalues

\[
\boxed{\lambda_q=4\pi^2q^2,\qquad q\in\mathbb Q.}
\tag{10}
\]

This agrees with the standard covering-solenoid picture: leafwise Hodge/Laplacian theory on measured Riemannian solenoids is classical, and the spectrum of a covering solenoid is governed by the spectra accumulated through its finite covers. The project-specific point is that the Prime-Circle refinement maps make the compatible normalization and the rational-square symbol completely explicit.

## 4. Finite-adic refinement creates arbitrarily soft modes

The form is positive, but it is maximally noncoercive in the direction relevant to the new profinite fiber. The characters

\[
\chi_{1/n},\qquad n=1,2,\ldots,
\]

are mutually orthogonal and nonconstant, while

\[
\mathcal E_\Sigma(\chi_{1/n})
=\frac{4\pi^2}{n^2}\longrightarrow0.
\tag{11}
\]

Therefore there is no Poincare gap on the orthogonal complement of the constants:

\[
\boxed{
\inf_{f\perp1,\ f\ne0}
\frac{\mathcal E_\Sigma(f)}{\|f\|_2^2}=0.
}
\tag{12}
\]

Equivalently, zero is an accumulation point of the nonzero spectrum. The inverse refinement has turned higher-conductor transverse information into cheaper and cheaper leafwise modes.

This immediately rules out the ordinary compact-Hodge/spectral package. For every `t>0`,

\[
\operatorname{Tr}(e^{-t\Delta_\Sigma})
=\sum_{q\in\mathbb Q}e^{-4\pi^2tq^2}
=\infty,
\tag{13}
\]

because infinitely many rationals lie, for example, in `[-1,1]`, where every summand is bounded below by `e^{-4 pi^2 t}`. Thus the resolvent is not compact and there is no honest heat-trace determinant or discrete Hodge spectrum to which one could attach the completed zeta by the usual compact-geometric route.

This is not itself the decisive Weil obstruction—the research question explicitly rejects merely manufacturing another determinant—but it shows that the most canonical positive global geometry does not even produce the compact spectral architecture that might have hidden the missing arithmetic.

## 5. The product-formula logarithm gives `log n`, not Mangoldt

One might try to recover finite places from the rational eigenvalue itself. Since the character group is `Q`, the first canonical arithmetic operation available on a nonzero frequency `q` is the rational product formula

\[
\log|q|_\infty+\sum_p\log|q|_p=0.
\tag{14}
\]

Taking the logarithm of (10) gives, up to the harmless constant `log(4 pi^2)`,

\[
\log\lambda_q
=2\log|q|_\infty
=-2\sum_p\log|q|_p.
\tag{15}
\]

For the denominator character `q=1/n`,

\[
\log\lambda_{1/n}
=\log(4\pi^2)-2\log n
=\log(4\pi^2)-2\sum_{p\mid n}v_p(n)\log p.
\tag{16}
\]

The finite arithmetic supplied canonically by the solenoidal energy is therefore the **total additive logarithm of every prime valuation**. It is the same place-additive quantity already intrinsic to Prime Lattice, not the Weil coefficient

\[
\Lambda(n)
=\begin{cases}
\log p,&n=p^k,\\
0,&\text{if }n\text{ has at least two distinct prime factors}.
\end{cases}
\tag{17}
\]

In particular, for `n=p^a q^b` with distinct primes `p,q`, (16) contains both `a log p` and `b log q`, while (17) vanishes. No product-formula decomposition of the ordinary rational-square energy supplies the prime-power support cancellation.

This is exactly the structural divide isolated independently in `WP-031`: place-additive positive quadratic readouts do not select prime powers. Applying a logarithm here does not evade that divide; it also destroys positivity because `log lambda_q` has both signs as `|q|` crosses the normalization scale.

Thus the tempting chain

\[
\text{positive solenoid energy}
\to\text{rational eigenvalue}
\to\text{product formula}
\to\text{finite Weil weights}
\]

stops at ordinary `log n` before the Mangoldt selector appears.

## 6. Why the finite-adic fiber is present topologically but absent energetically

`PC-064` gives the exact extension

\[
0\to\widehat{\mathbb Z}
\to\Sigma_{\mathbb Q}
\to S^1
\to0.
\tag{18}
\]

So the finite-adic fiber is not missing from the space. What is missing is a positive **transverse energy** forced by the same construction. The compatible form (8) differentiates along the real leaf. A character of denominator `n` certainly varies in the profinite direction, but its cost is only `1/n^2`; increasing finite conductor makes it softer rather than generating local prime penalties.

Haar measure on the fiber, derived in `PC-059`, supplies an intrinsic transverse measure but not a transverse gradient. The radial Prime-Circle analysis does supply additional finite-adic structure, but `WP-037` shows that the arithmetic birth operator occurs as a singular signed first variation of that Haar background, not as an ordinary positive tangent measure.

Consequently, merely placing the positive leafwise energy and the profinite Haar fiber inside the same solenoid does not combine their strengths:

\[
\boxed{
\text{global topology couples }S^1\text{ and }\widehat{\mathbb Z},
\quad
\text{but the compatible positive Dirichlet form remains leafwise.}
}
\tag{19}
\]

A true finite--archimedean Weil geometry would need an additional nonseparable or transverse operator **before** positivity is taken.

## 7. Matched controls show that the positivity is not RH-specific

Nothing in Sections 2--4 uses primality. The same argument works for any one-dimensional covering solenoid whose dual is a dense additive subgroup `G subset R`: the compatible leafwise Dirichlet form is diagonal with symbol `4 pi^2 g^2`, `g in G`.

In particular, the Prime-Circle all-level refinement uses the entire divisibility tower, not a prime-only tower, and the same positive energy exists whether one interprets the denominators arithmetically or merely as covering degrees. The positivity therefore survives matched non-prime controls automatically.

This is the correct behavior for a geometric energy but the wrong behavior for a purported RH discriminator. The arithmetic information needed by Weil begins only after one asks for the singular prime-power selector or introduces multiplicative correspondences.

## 8. Prior-art and novelty audit

No historical novelty is claimed for any of the ambient analytic ingredients.

- The arithmetic solenoid itself is classical; `PC-064` already redirects its identification to the universal one-dimensional solenoid / additive adelic quotient literature.
- Vicente Munoz and Ricardo Perez-Marco, *Hodge Theory for Riemannian Solenoids* (2010/2011), develop leafwise `L^2` Hodge theory on measured Riemannian solenoids. This establishes that positive leafwise Dirichlet/Hodge forms are standard solenoidal geometry rather than a new RH construction.
- Raymond Lei, *The spectrum of a solenoid*, arXiv:1907.06712 (2019), proves for covering solenoids that the leafwise Laplacian spectrum is the closure of the spectra accumulated from the covering levels. The rational-square accumulation in (10)--(12) is the explicit one-dimensional arithmetic-solenoid instance.
- Adelic and `p`-adic pseudo-differential/transverse operators, wavelets, and Vladimirov-type energies are also a developed literature. Their existence cannot be counted as a Mathia derivation of the missing finite-place sign; a particular operator and its coefficients would have to be forced by Prime Circle rather than selected because it reproduces zeta data.

The durable Mathia-specific result is narrower: **starting from the actual circle metric at every PC-064 refinement level and demanding exact inverse-limit compatibility uniquely produces (8), and that positive form has the wrong finite arithmetic architecture.** It is a direct falsification of the most intrinsic ordinary-energy route on the first Mathia-native space that topologically couples the real and finite-adic sectors.

This is not a reformulation of RH, zeta, or its zeros. The proof uses only the covering maps, circle energy, Pontryagin character group, and elementary rational product formula.

## 9. Boundaries of the obstruction

`WP-038` does **not** rule out:

- a nonlocal transverse Dirichlet or pseudo-differential form canonically forced by the Prime-Circle radial/divisor-Haar geometry;
- an infinite-rank coupling between the real leaf and `\widehat{\mathbb Z}` fiber formed before taking a quadratic sign;
- a solenoidal metric or lamination energy with genuinely cross-level terms rather than scalar-rescaled circle energies;
- a non-invertible compression/quotient that removes the rational soft modes for an independently geometric reason;
- multiplicative correspondences on the solenoid whose fixed-point/intersection theory supplies Mangoldt weights without importing the Tate/Connes apparatus by hand;
- the singular profinite tangent of `WP-037` if it is paired with a new geometric sign theorem before being reduced to its signed scalar moments;
- or the global primitive-root uniformization/accessory branch left outside the bare compact-group structure in `PC-064`.

These are real escapes. In particular, the result must not be paraphrased as saying that the adelic solenoid is irrelevant. On the contrary, `PC-064` makes it the cleanest Mathia-native finite--archimedean carrier found so far. `WP-038` says only that its **ordinary compatible leafwise positivity** is too weak and too place-additive.

## 10. Exact falsification tests and research consequence

The exact core can be audited without numerical experiments:

1. verify the pullback scaling `E_n^0(F o p_{n,m})=(n/m)^2 E_m^0(F)` under normalized Haar;
2. solve the compatibility relation `a_n(n/m)^2=a_m` and recover `a_n=a_1/n^2`;
3. represent the rational character `k/n` at level `n` and recover the energy `4 pi^2(k/n)^2`;
4. check that the orthonormal sequence `chi_{1/n}` has energy tending to zero;
5. conclude directly that the heat trace diverges for every positive time;
6. apply the rational product formula to `q=1/n` and recover `-2 log n`, not `Lambda(n)`.

Failure of items 1--3 would invalidate the claimed canonical form. Failure of items 4--5 would contradict elementary Fourier analysis on the rational character group. Item 6 is the exact arithmetic mismatch.

The research consequence is a sharper requirement on any continuation of the solenoidal route:

\[
\boxed{
\text{the missing positivity cannot be ordinary leafwise Hodge/Dirichlet energy.}
}
\]

The next viable structure must put a **prime-sensitive transverse or cross-place operator** on the solenoid before the sign theorem is applied, and it must derive both the Mangoldt support and the archimedean/polar terms from that coupled geometry. If the needed transverse operator is chosen from standard adelic analysis solely because its trace reproduces zeta, the route collapses back to the prior art excluded by the research question.

## Internal dependencies

- `research/prime_circle/findings/PC-059-infinite-divisor-haar-limit-is-profinite-valuation-measure.md`
- `research/prime_circle/findings/PC-064-compatible-circle-refinement-is-the-adelic-solenoid.md`
- `research/weil_positivity/findings/WP-031-place-additive-positive-quadratic-readouts-cannot-select-prime-powers.md`
- `research/weil_positivity/findings/WP-037-prime-circle-weil-birth-form-is-singular-profinite-haar-tangent.md`