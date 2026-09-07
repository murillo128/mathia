# AF-173 — Unimodular gauge quotient makes complex Blaschke fidelity exactly pseudohyperbolic

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY`, `PHASE/ORIENTATION`, `GAUGE-QUOTIENT`, `POSITIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-172 extends the regular radial Blaschke model to the full complex cyclic parameter and shows that the normalized inner factor

\[
B_{n,a}(z)=\frac{z^n-a}{1-\overline a z^n},
\qquad a\in\mathbb D,
\tag{1}
\]

retains the same complex coefficient that parametrizes the unordered divisor

\[
Z_n(a)=\{z\in\mathbb D:z^n=a\}.
\tag{2}
\]

Its remaining normalization caveat can be resolved exactly. A finite Blaschke product with a fixed zero divisor is intrinsically defined only up to an output factor in `\mathbb T`. Once that harmless unimodular gauge is quotiented out, the ordinary `H^\infty` distance between the degree-`n` cyclic factors is exactly twice the pseudohyperbolic distance between the retained complex coefficients, independently of `n`.

For `a,b\in\mathbb D`, define

\[
F_a(w)=\frac{w-a}{1-\overline a w},
\qquad
\rho(a,b)=\left|\frac{a-b}{1-\overline a b}\right|,
\tag{3}
\]

so that `B_{n,a}=F_a\circ(z\mapsto z^n)`. Put

\[
d_{\mathrm{gauge}}(B_{n,a},B_{n,b})
=
\inf_{|\lambda|=1}
\|B_{n,a}-\lambda B_{n,b}\|_{H^\infty}.
\tag{4}
\]

Then for every `n>=1`,

\[
\boxed{
 d_{\mathrm{gauge}}(B_{n,a},B_{n,b})
 =2\rho(a,b).
}
\tag{5}
\]

The minimizing phase is also explicit. If

\[
A=1-b\overline a,
\qquad
\phi=\arg A,
\tag{6}
\]

then one minimizer is

\[
\boxed{
\lambda_*(a,b)=e^{-2i\phi}
=\frac{1-\overline b a}{1-b\overline a}.
}
\tag{7}
\]

The fixed-normalization distance has a different exact formula. Let

\[
\gamma=\arcsin\rho(a,b)\in[0,\pi/2).
\tag{8}
\]

Since `\operatorname{Re}(1-b\overline a)>0`, one has `|\phi|<\pi/2`, and

\[
\boxed{
\|B_{n,a}-B_{n,b}\|_{H^\infty}
=
2\sin\!\left(
\min\left\{\frac\pi2,\ |\phi|+\gamma\right\}
\right).
}
\tag{9}
\]

Thus the raw normalized metric mixes two effects: the intrinsic displacement `\rho(a,b)` of the zero-set parameter and a normalization phase `\phi`. In the real-diameter case `\phi=0`, equation `(9)` reduces to AF-171's exact identity `2\rho`. For general complex parameters, the raw norm can approach its maximal value `2` partly because of the output-phase convention even when the quotient distance remains strictly smaller.

Equation `(5)` removes that artifact without adding information. The unimodular factor is a genuine gauge: multiplying a finite Blaschke product by it changes neither the zero divisor nor the induced cyclic source object. After taking the quotient, the complete analytic representation carries exactly the classical pseudohyperbolic geometry of its retained complex coefficient.

This sharpens AF-172's compact-annulus bi-Lipschitz estimate. On the cyclic stratum, the correct analytic endpoint geometry can be stated without an arbitrary normalization: the quotient `H^\infty` metric is exactly `2\rho`, while the degree-rescaled source bottleneck metric converges to the logarithmic-polar cylinder from AF-172. Any transfer between the two therefore has a clean two-step audit: first quotient the output gauge exactly, then compare pseudohyperbolic coefficient geometry with the source-forced asymptotic endpoint scale.

## Derivation

### Reduction to one disk automorphism is exact and degree-independent

Because `z\mapsto z^n` maps the unit circle onto itself and both sides of `(1)` are continuous on the closed disk,

\[
\|B_{n,a}-\lambda B_{n,b}\|_{H^\infty}
=
\|F_a-\lambda F_b\|_{H^\infty}
\tag{10}
\]

for every unimodular `\lambda`. Thus the entire question is already present for degree-one disk automorphisms.

Let `\xi=F_a(w)`. The inverse automorphism is

\[
F_a^{-1}(\xi)=\frac{\xi+a}{1+\overline a\xi}.
\tag{11}
\]

Direct substitution gives

\[
G(\xi):=F_b(F_a^{-1}(\xi))
=
\frac{A\xi+C}{\overline C\xi+\overline A},
\qquad
A=1-b\overline a,
\quad C=a-b.
\tag{12}
\]

For `|\xi|=1`, set

\[
q(\xi)=A+C\overline\xi.
\tag{13}
\]

Then

\[
A\xi+C=\xi q(\xi),
\qquad
\overline C\xi+\overline A=\overline{q(\xi)},
\]

so

\[
\boxed{
\frac{G(\xi)}{\xi}
=
\frac{q(\xi)}{\overline{q(\xi)}}.
}
\tag{14}
\]

The circle traced by `q` has center `A` and radius `|C|`. It misses the origin because

\[
|A|^2-|C|^2
=|1-b\overline a|^2-|a-b|^2
=(1-|a|^2)(1-|b|^2)>0.
\tag{15}
\]

Hence its visible angular half-width from the origin is

\[
\gamma
=
\arcsin\frac{|C|}{|A|}
=\arcsin\rho(a,b).
\tag{16}
\]

If `\phi=\arg A`, the arguments of all points on that circle fill exactly

\[
[\phi-\gamma,\phi+\gamma].
\tag{17}
\]

Equation `(14)` doubles these angles. Consequently the boundary values of `G(\xi)/\xi` form the unit-circle arc with angular center `2\phi` and half-width `2\gamma`.

### Quotienting the output phase centers that arc optimally

For `|\xi|=1`,

\[
|F_a(w)-\lambda F_b(w)|
=|\xi-\lambda G(\xi)|
=\left|1-\lambda\frac{G(\xi)}{\xi}\right|.
\tag{18}
\]

Choosing `\lambda=e^{-2i\phi}` rotates the arc in `(17)` so that the arguments in `(18)` range symmetrically over

\[
[-2\gamma,2\gamma].
\tag{19}
\]

The maximum chordal distance from `1` on this centered arc occurs at either endpoint and equals

\[
2\sin\gamma=2\rho(a,b).
\tag{20}
\]

No other phase can improve this. The boundary-value set in `(18)` is a connected circular arc of angular length `4\gamma<2\pi`; among all rotations of such an arc, centering it at `1` uniquely minimizes the largest absolute principal angle, whose minimum possible value is the half-length `2\gamma`. Therefore `(20)` is the infimum in `(4)`, proving `(5)`. Formula `(7)` is exactly the centering phase.

This is a metric quotient, not a side channel. The minimizing operation discards a degree of freedom that is irrelevant to the zero divisor; it does not append a mark capable of reconstructing lost source information.

### The fixed-normalization formula isolates the gauge penalty

With `\lambda=1`, equation `(18)` becomes

\[
\left|1-e^{2i\theta}\right|=2|\sin\theta|,
\qquad
\theta\in[\phi-\gamma,\phi+\gamma].
\tag{21}
\]

The center satisfies `|\phi|<\pi/2` because

\[
\operatorname{Re}A
=1-\operatorname{Re}(b\overline a)
\ge1-|a||b|>0.
\tag{22}
\]

The largest value of `|\sin\theta|` on the interval `(21)` is therefore

\[
\sin\!\left(
\min\left\{\frac\pi2,|\phi|+\gamma\right\}
\right),
\tag{23}
\]

which gives `(9)`.

When `a` and `b` lie on the same real diameter, `A` is positive real and `\phi=0`, so `(9)` becomes `2\sin\gamma=2\rho`, exactly recovering AF-171. Away from that diameter, equation `(9)` identifies why a naive extension of the radial `2\rho` identity fails before quotienting the unimodular normalization.

### Relation to the cylindrical source scale

Write as in AF-172

\[
a=e^{-u+i\theta},
\qquad
b=e^{-v+i\psi},
\qquad
\delta=d_{\mathbb T}(\theta,\psi).
\tag{24}
\]

Then

\[
|a-b|^2
=(e^{-u}-e^{-v})^2
+4e^{-(u+v)}\sin^2(\delta/2),
\tag{25}
\]

and

\[
|1-\overline a b|^2
=(1-e^{-(u+v)})^2
+4e^{-(u+v)}\sin^2(\delta/2).
\tag{26}
\]

Therefore `(5)` gives an exact bounded analytic metric on the logarithmic-polar quotient parameter:

\[
\boxed{
 d_{\mathrm{gauge}}
 =
2\frac{
\sqrt{(e^{-u}-e^{-v})^2+4e^{-(u+v)}\sin^2(\delta/2)}
}{
\sqrt{(1-e^{-(u+v)})^2+4e^{-(u+v)}\sin^2(\delta/2)}
}.
}
\tag{27}
\]

On every compact logarithmic annulus `0<c<=u,v<=d<\infty`, this is bi-Lipschitz equivalent to AF-172's cylindrical metric

\[
D_{\mathrm{cyl}}=\sqrt{(u-v)^2+\delta^2},
\tag{28}
\]

because `|a-b|` is already bi-Lipschitz to `(28)` there and `|1-\overline a b|` is bounded above and below away from zero. Thus the gauge quotient does not disturb the positive boundary-layer result; it identifies its intrinsic analytic metric more cleanly.

The distinction is useful. The source bottleneck after multiplication by `n` converges to the unbounded local cylinder `(28)`, whereas the analytic quotient metric is the bounded pseudohyperbolic metric `(27)`. They are uniformly comparable on compact windows, but neither should be silently substituted for the other in a downstream quantitative theorem.

## Prior art and novelty assessment

All complex-analysis ingredients are classical, and no novelty is claimed for disk automorphisms, the pseudohyperbolic metric, finite Blaschke products, their unimodular normalization freedom, or the elementary circle geometry used above.

- A. F. Beardon and D. Minda, **“The hyperbolic metric and geometric function theory,”** in *Quasiconformal Mappings and Their Applications*, 9–56, Narosa (2007), gives a standard treatment of the automorphism group of the disk, its Möbius normal forms, and hyperbolic invariance.
- Stephan Ramon Garcia, Javad Mashreghi, and William T. Ross, ***Finite Blaschke Products and Their Connections***, Springer (2018), DOI `10.1007/978-3-319-78247-8`, is a modern reference for finite Blaschke products, Möbius transformations, normalization, zero sets, mapping properties, and hyperbolic geometry.
- The standard pseudohyperbolic identity `\rho(a,b)=|(a-b)/(1-\overline a b)|` and its automorphism interpretation are classical Schwarz--Pick geometry; a modern explicit reference is Alejandro Miralles, **“Lipschitz continuity of the dilation of Bloch functions on the unit ball of a Hilbert space and applications,”** *Annals of Functional Analysis* 15, 17 (2024), DOI `10.1007/s43034-024-00317-0`.

A targeted search of disk-automorphism, finite-Blaschke, pseudohyperbolic, uniform-norm, and Möbius-transformation literature found the expected mature hyperbolic/automorphism framework. No claim is made that `(5)`, `(7)`, or `(9)` is a new theorem of complex analysis; they are elementary consequences of that framework. The Arithmetic Fidelity contribution is the **gauge audit relative to AF-172**: the phase discrepancy left by a chosen Blaschke normalization can be separated exactly from the zero-divisor geometry, and quotienting precisely that irrelevant phase turns the complex cyclic `H^\infty` fidelity metric into `2\rho` with no degree dependence.

## Boundary conditions and falsification checks

- The result concerns the cyclic one-complex-parameter stratum `Z_n(a)`. Generic degree-`n` divisors have `n` complex symmetric coordinates and collision/conditioning phenomena not represented by one disk parameter.
- Equation `(5)` compares equivalence classes under **output multiplication by one unimodular scalar**. Quotienting a larger transformation group could erase genuine divisor information and requires a separate fidelity audit.
- The gauge is harmless here because multiplication by `\lambda\in\mathbb T` leaves every zero and its multiplicity unchanged. A phase attached to another mathematical object is not automatically disposable merely because it looks like a scalar normalization.
- Formula `(9)` is the exact fixed-normalization correction to AF-171. It shows explicitly why `2\rho(a,b)` is not the raw complex-parameter `H^\infty` distance in general.
- `a=b` gives `\rho=\gamma=0` and zero quotient distance. No singular phase choice is needed; `(7)` then equals `1`.
- The parameter may include `a=0` or `b=0`; equations `(3)--(23)` remain valid. What disappears at the zero parameter is the logarithmic-polar orientation coordinate used in `(24)--(28)`, not the disk-automorphism theorem.
- Compact logarithmic-annulus assumptions are needed only for the comparison with `D_{\mathrm{cyl}}`; the exact gauge identity `(5)` holds throughout the disk.
- The quotient distance is bounded by `2`, while the cylindrical coordinate is not globally bounded. Their compact-window equivalence must not be promoted to a global bi-Lipschitz equivalence.
- No RH consequence follows directly. An arithmetic transfer must justify both that the scalar normalization is genuinely gauge for the destination theorem and that the arithmetic endpoint is naturally measured in a geometry comparable to the retained pseudohyperbolic coordinate.

## Consequences for the research line

AF-170--AF-172 separated exact recovery, growing-degree conditioning, endpoint scale, and quotient orientation. AF-173 adds one more necessary distinction: **representation normalization is not the same thing as structural provenance**. A normalization phase can dramatically alter a raw function-space distance while carrying no zero-divisor information at all.

For this cyclic model the separation is exact. Before declaring phase or orientation information lost, first quotient the transformations that provably act only as gauge on the declared endpoint. After that quotient, any residual phase geometry is real retained structure: here it is precisely the pseudohyperbolic displacement of the complex coefficient `a`, which simultaneously encodes radial and quotient-orientation information.

This yields a reusable audit rule for future compression problems. Specify the downstream endpoint quotient first; identify the maximal transformation group that is genuinely null for that endpoint; take the data metric on that quotient rather than on arbitrary representatives; only then ask for a recovery modulus. Otherwise an apparent instability can be caused by representative choice, while an apparent repair can merely choose a convenient gauge instead of preserving additional mathematics.