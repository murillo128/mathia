# PF-107 — shift-clone endpoint `ell^1` defect amplifies to `ell^2 \ ell^1` in cuff lengths

**Status:** `LITERATURE+DERIVED + NEGATIVE/BOUNDARY`. This refines PF-106 and the accepted relative-operator clue. The canonical all-composite shift clone remains asymptotically close in relative cuff coordinates, but PF-106's `ell^1` sampled-endpoint displacement does **not** pass to an `ell^1` additive defect in the distinguished hyperbolic cuff lengths. No compactness, Schatten, wave-equivalence, or scattering conclusion is claimed.

## Claim

Let consecutive odd primes be

\[
a=p_{n-1},\qquad b=p_n=a+g,
\]

and write

\[
u(x)=\cot\frac{\pi}{x},\qquad
F(x)=\log u(x).
\]

For the exact prime-flute define

\[
h=F(b)-F(a),\qquad
\ell=\Lambda(h):=2\log\coth\frac h4.
\]

For the all-composite shift clone `p -> p+1` of PF-106, hyperbolic translation does not change lengths, so the corresponding cuff is

\[
h^+=F(b+1)-F(a+1),\qquad
\ell^+=\Lambda(h^+).
\]

Then, as `a -> infinity` through consecutive primes,

\[
\boxed{\ell^+-\ell=\frac{2}{a}+o(a^{-1}).}
\tag{1}
\]

Consequently,

\[
\boxed{
\sum_n |\ell_n^+-\ell_n|=\infty,
\qquad
\sum_n |\ell_n^+-\ell_n|^2<\infty.}
\tag{2}
\]

Thus the additive distinguished-cuff defect is in `ell^2` but not `ell^1`, even though PF-106 proves that the canonically normalized sampled-endpoint displacement itself is in `ell^1`.

At the same time the **relative** cuff defect is summable:

\[
\boxed{
\sum_n \frac{|\ell_n^+-\ell_n|}{\ell_n}<\infty.}
\tag{3}
\]

The distinction between (2) and (3) is the durable boundary: the singular change of coordinate from a shrinking logarithmic mesh `h_n` to a growing cuff length amplifies additive errors, but it does not destroy asymptotic multiplicative closeness.

## 1. Shift of the logarithmic mesh

The exact large-`x` expansion is

\[
F(x)
=
\log\frac{x}{\pi}
-\frac{\pi^2}{3x^2}
-\frac{7\pi^4}{90x^4}
+O(x^{-6}).
\tag{4}
\]

Baker--Harman--Pintz give the unconditional consecutive-prime bound

\[
g=O(a^{0.525}),
\tag{5}
\]

so `g/a -> 0`. By the mean-value theorem applied to `F`,

\[
\boxed{h=\frac ga(1+o(1)).}
\tag{6}
\]

Now set

\[
\delta(x):=F(x+1)-F(x).
\]

Differentiating (4) gives

\[
\delta'(x)=-\frac1{x^2}+O(x^{-3}).
\tag{7}
\]

Hence another mean-value estimate, using `g=o(a)`, yields

\[
\boxed{
h^+-h
=\delta(b)-\delta(a)
=-\frac{g}{a^2}(1+o(1)).}
\tag{8}
\]

Combining (6) and (8),

\[
\boxed{
\frac{h^+-h}{h}
=-\frac1a+o(a^{-1}),
\qquad
\frac{h^+}{h}=1-\frac1a+o(a^{-1}).}
\tag{9}
\]

In particular `h^+<h` eventually.

## 2. The cuff coordinate amplifies the defect

PF-001 gives the exact cuff transform

\[
\Lambda(h)=2\log\coth\frac h4.
\]

Its derivative is

\[
\boxed{
\Lambda'(h)=-\frac1{\sinh(h/2)}
=-\frac2h+O(h).}
\tag{10}
\]

Apply the mean-value theorem directly to `Lambda` between `h` and `h^+`. Since both are asymptotic to `g/a` and their ratio tends to one, (8)--(10) give

\[
\ell^+-\ell
=
\Lambda'(\xi)(h^+-h)
=
\frac2a+o(a^{-1}),
\]

which proves (1). The sign is also geometrically consistent: the shift makes the logarithmic mesh slightly smaller, and `Lambda` is decreasing, so the composite-clone cuff is slightly longer.

The coefficient is not a numerical artifact. For example, direct evaluation gives

```text
(a,b)         a * (ell^+ - ell)
(1061,1063)       1.9972008
(1721,1723)       1.9982676
(9433,9437)       1.9994704
(50359,50363)     1.9999007
```

## 3. Additive `ell^1` fails but relative `ell^1` survives

Euler's divergence of the reciprocal-prime sum and convergence of the reciprocal-square sum turn (1) into (2):

\[
\sum_p\frac1p=\infty,
\qquad
\sum_p\frac1{p^2}<\infty.
\]

This shows that endpoint `ell^1` control is not stable under the intrinsic cuff-length coordinate.

However PF-001 together with (5) gives

\[
\ell
=2\log\frac{4a}{g}+o(1)
\ge (0.95+o(1))\log a.
\tag{11}
\]

Therefore

\[
\frac{|\ell^+-\ell|}{\ell}
=O\left(\frac1{a\log a}\right).
\tag{12}
\]

A standard Chebyshev bound and partial summation imply

\[
\sum_p\frac1{p\log p}<\infty,
\]

which proves (3). So the natural multiplicative length-spectrum comparison remains compatible with a summable tail even though the raw additive cuff changes have divergent total mass.

## 4. Collar warning

For the standard collar half-width

\[
w(\ell)=\operatorname{arsinh}\frac1{\sinh(\ell/2)},
\]

large cuffs satisfy `w(ell)=2e^{-ell/2}(1+o(1))`. Hence (1) gives

\[
\boxed{
\log\frac{w(\ell^+)}{w(\ell)}
=-\frac1a+o(a^{-1}).}
\tag{13}
\]

Thus the logarithmic relative distortion of the **standard collar width** is again non-`ell^1`. Equation (13) is a warning about geometric coordinates, not an operator theorem: the collars themselves have rapidly shrinking area/width, so this harmonic-prime logarithmic defect does not by itself imply divergence of any weighted surface integral or failure of compactness.

## 5. Consequence for the accepted relative-operator clue

PF-106 motivated the question whether its `ell^1` endpoint deformation can be promoted to a compact/Schatten relative Laplacian perturbation. PF-107 shows that the first conversion to intrinsic pants data is already nonuniform:

\[
\boxed{
\ell^1\text{ endpoint displacement}
\not\Rightarrow
\ell^1\text{ additive cuff-length displacement}.}
\]

The mechanism is explicit: consecutive endpoint ratios have `h_n -> 0`, while the cuff map has

\[
|\Lambda'(h_n)|\sim\frac2{h_n}\to\infty.
\]

Therefore any future trace-class or Schatten argument must estimate the **actual surface metric/Jacobian distribution**, especially through long-cuff thin regions; it cannot sum PF-106 endpoint errors or additive cuff errors as a proxy.

This does **not** close the operator-comparison program. Absolute cuff differences still tend to zero, relative cuff differences are summable by (3), and the local pants comparison prior art recorded in the accepted clue remains potentially usable. The unresolved question is whether the shrinking geometric support compensates for the amplified coordinate defect when one passes to metric-deviation integrals, resolvents, heat kernels, or scattering.

## 6. Prior art and novelty audit

No novelty is claimed for the ingredients:

- Baker--Harman--Pintz's `0.525` short-interval theorem is standard input (PLMS 83 (2001), 532--562, DOI `10.1112/plms/83.3.532`);
- divergence of `sum_p 1/p`, convergence of `sum_p 1/p^2`, and convergence of `sum_p 1/(p log p)` are classical;
- the sensitivity of infinite-type Fenchel--Nielsen/length-spectrum comparisons to unbounded cuffs is part of the established literature. Basmajian--Šarić, *Geodesically Complete Hyperbolic Structures* (Math. Proc. Camb. Phil. Soc. 166 (2019), 219--242, DOI `10.1017/S0305004117000792`), explicitly studies complete flutes with rapidly increasing cuff lengths and related quasiconformal/length-spectrum pathologies.

The existing infinite-type literature does not supply the project-specific asymptotic (1), and no directed search located this exact `p_n -> p_n+1` all-composite control or an operator-ideal theorem that would follow from it. The durable new content for Mathia is therefore the **explicit amplification law**

\[
\boxed{
\ell_n^+-\ell_n\sim\frac2{p_{n-1}},
}
\]

and its boundary consequence `ell^2 \ ell^1` for additive cuffs versus `ell^1` for relative cuffs.

## 7. Audit / falsification core

The reusable checks are:

1. verify the expansion (4) of `log cot(pi/x)`;
2. use Baker--Harman--Pintz only to obtain `g=o(a)` and the quantitative lower growth (11);
3. derive (7)--(9) by two mean-value estimates;
4. differentiate the exact PF-001 cuff transform to obtain (10);
5. apply a mean-value estimate to `Lambda` to get the coefficient `2` in (1);
6. separate the three summability statements: additive cuffs diverge in `ell^1`, additive cuffs lie in `ell^2`, and relative cuffs lie in `ell^1`;
7. do not infer an operator class from (2), (3), or (13) without an explicit common-manifold metric comparison and the hypotheses of the relevant spectral theorem.

A mathematical refutation of PF-107 would need to break one of steps 1--6. An operator-level counterexample to the programmatic warning is possible and would be welcome: it would require proving that the surface geometry supplies enough shrinking support to recover a compact/Schatten comparison despite the non-`ell^1` additive cuff defect.