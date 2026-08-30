# WP-050 — reflection-odd cycle current adds a dyadic Mangoldt shadow instead of a Weil grading

**Status:** `EXACT-DERIVED + CLASSICAL-CYCLOTOMIC-IDENTITY + DECISIVE-NEGATIVE` for the most canonical non-scalar/odd-differential escape left open by `WP-049`. The compatible Prime-Circle cycle geometry has a canonical reflection-odd first-order current

\[
D:=\frac{U-U^*}{2i},
\]

which genuinely exchanges reflection-even and reflection-odd primitive modes. Its square is an unconditional positive energy and factors exactly as

\[
4D^2=L_{\rm cyc}(4I-L_{\rm cyc}).
\]

However, on every primitive shell `H_n`, `n>2`, its positive determinant reads both cyclotomic endpoints rather than only the common anchor:

\[
\boxed{
\frac12\log\det(4D^2|_{H_n})
=\log\Phi_n(1)+\log\Phi_n(-1)
=\Lambda(n)+\mathbf 1_{2\mid n}\Lambda(n/2).
}
\]

Thus the first intrinsic odd differential produces the desired odd-prime-power weight **plus an unavoidable antipodal/dyadic shadow**: levels `2p^k` acquire a false `log p`, while powers of two beyond `2` are doubled. Reflection grading does not repair this: for `n>2`, `D` is an invertible odd isomorphism between the two parity sectors, so its positive square remains parity-isospectral and has zero graded trace.

The obstruction is structural for every finite-range translation-invariant scalar differential that is odd under the same anchored reflection. Its Laurent symbol must factor by `z-z^{-1}`, hence its positive square necessarily vanishes at both reflection-fixed characters `z=+1` and `z=-1`. The second fixed point is exactly the order-two mode that `WP-048` independently selected as the real Riemann Gamma channel. Removing the antipodal factor from the canonical current requires inverting `4I-L_cyc`, which is singular precisely on that `q=2` mode and otherwise collapses back to the scalar cycle-Laplacian route already ruled insufficient in `WP-043`.

A newly available Prime-Circle control, `PC-076`, sharpens rather than rescues the mechanism: its first Hardy/Hilbert relative trace produces the **opposite** endpoint combination `Lambda(n)-1_{2|n}Lambda(n/2)`. Combining the current determinant and that signed relative trace algebraically isolates `Lambda(n)`, but only by mixing a nonlinear positive determinant with a sign-indefinite relative trace. This is an exact endpoint decomposition, not an independent positive Weil pairing.

## 1. The canonical cycle current is genuinely reflection odd

Use the compatible Prime-Circle limit from `WP-037`--`WP-049`,

\[
K=\widehat{\mathbb Z},
\qquad
\widehat K=\mathbb Q/\mathbb Z,
\]

and let

\[
(Uf)(x)=f(x+1).
\]

On a character `chi_gamma`,

\[
U\chi_\gamma=e^{2\pi i\gamma}\chi_\gamma.
\]

The anchored reflection selected in `WP-048` is

\[
(Rf)(x)=f(-x),
\qquad
R\chi_\gamma=\chi_{-\gamma},
\qquad
RUR=U^*.
\]

The canonical skew part of the compatible shift is therefore

\[
\boxed{
D:=\frac{U-U^*}{2i}=D^*.
}
\tag{1}
\]

It satisfies

\[
\boxed{RDR=-D,}
\tag{2}
\]

and has exact Fourier multiplier

\[
\boxed{
D\chi_\gamma
=\sin(2\pi\gamma)\chi_\gamma.
}
\tag{3}
\]

So this is not a scalar positive multiplier merely relabelled as a grading. It is the first intrinsic cycle differential that is odd for the very reflection whose fixed geometry selected the real Gamma channel in `WP-048`.

For the exact-order primitive shell

\[
H_n=\operatorname{span}\{\chi_\gamma:\operatorname{ord}(\gamma)=n\},
\]

`WP-049` gives the parity decomposition

\[
H_n=H_n^+\oplus H_n^-.
\]

When `n>2`, no primitive character satisfies `gamma=-gamma`, hence no primitive character is `0` or `1/2`. Equation (3) is therefore nonzero on every primitive mode. In the paired basis

\[
e_\gamma^+=\frac{\chi_\gamma+\chi_{-\gamma}}{\sqrt2},
\qquad
 e_\gamma^-=\frac{\chi_\gamma-\chi_{-\gamma}}{\sqrt2},
\]

one has

\[
D e_\gamma^+
=\sin(2\pi\gamma)e_\gamma^-,
\qquad
D e_\gamma^-
=\sin(2\pi\gamma)e_\gamma^+.
\tag{4}
\]

Consequently

\[
\boxed{
D:H_n^+\overset\sim\longrightarrow H_n^-,
\qquad n>2.
}
\tag{5}
\]

The candidate odd differential exists exactly as hoped, but it has no higher-shell kernel on which a Lefschetz/supersymmetric index could localize.

The exceptional shell is `n=2`: its sole nontrivial character has `gamma=1/2`, and (3) gives

\[
D\chi_{1/2}=0.
\tag{6}
\]

This will be decisive below because the same order-two mode is the canonical archimedean selector of `WP-048`.

## 2. Its positive square has a forced two-endpoint factorization

`WP-043` defines the compatible positive cycle Laplacian

\[
L_{\rm cyc}
=(U-I)^*(U-I)
=2I-U-U^*.
\tag{7}
\]

On `chi_gamma`,

\[
L_{\rm cyc}\chi_\gamma
=4\sin^2(\pi\gamma)\chi_\gamma.
\tag{8}
\]

Combining (3) and (8) gives the exact operator identity

\[
\boxed{
4D^2
=L_{\rm cyc}(4I-L_{\rm cyc}).
}
\tag{9}
\]

Indeed, if `theta=2 pi gamma`, then

\[
4\sin^2\theta
=16\sin^2(\theta/2)\cos^2(\theta/2).
\]

The second factor is itself a canonical positive cycle operator,

\[
\boxed{
4I-L_{\rm cyc}
=(I+U)^*(I+U).
}
\tag{10}
\]

Thus the odd current does produce an unconditional positive geometry, but it is the product of the two distinguished endpoint energies

```text
common-anchor endpoint  +1:  (I-U)^*(I-U) = L_cyc
antipodal endpoint      -1:  (I+U)^*(I+U) = 4I-L_cyc.
```

This factorization already warns that the reflection-odd route cannot see the `+1` arithmetic source without also seeing the antipode.

## 3. The primitive-shell determinant is `Phi_n(1) Phi_n(-1)`

Let `n>2` and write `zeta=e^{2 pi i gamma}` for primitive `n`-th roots. Equation (3) gives

\[
4\sin^2(2\pi\gamma)
=|1-\zeta^2|^2
=|1-\zeta|^2|1+\zeta|^2.
\tag{11}
\]

Multiplying over the primitive shell,

\[
\begin{aligned}
\det(4D^2|_{H_n})
&=\prod_{\operatorname{ord}(\zeta)=n}|1-\zeta^2|^2\\
&=\left|\prod_{\operatorname{ord}(\zeta)=n}(1-\zeta)\right|^2
  \left|\prod_{\operatorname{ord}(\zeta)=n}(1+\zeta)\right|^2.
\end{aligned}
\tag{12}
\]

Since `phi(n)` is even for `n>2`, the two products are the cyclotomic endpoint values

\[
\prod_{\operatorname{ord}(\zeta)=n}(1-\zeta)=\Phi_n(1),
\qquad
\prod_{\operatorname{ord}(\zeta)=n}(1+\zeta)=\Phi_n(-1).
\tag{13}
\]

Both endpoint values are positive integers here. Therefore

\[
\boxed{
\frac12\log\det(4D^2|_{H_n})
=\log\Phi_n(1)+\log\Phi_n(-1).
}
\tag{14}
\]

`WP-043` already supplies the classical first endpoint identity

\[
\log\Phi_n(1)=\Lambda(n),
\qquad n>1.
\tag{15}
\]

The second endpoint has an equally elementary exact classification, derived next so that no external arithmetic assumption is hidden in the obstruction.

## 4. The antipodal endpoint is exactly a dyadic Mangoldt shadow

For `n>2`, write

\[
n=2^a m,
\qquad m\text{ odd}.
\]

There are three cases.

### Odd `n`

If `a=0`, the standard parity identity

\[
\Phi_{2n}(x)=\Phi_n(-x)
\qquad(n\text{ odd})
\]

gives

\[
\Phi_n(-1)=\Phi_{2n}(1).
\]

Since `2n` has at least two distinct prime factors for odd `n>1`, (15) gives

\[
\Phi_n(-1)=1.
\tag{16}
\]

### Exactly one factor of two

If `a=1`, write `n=2m` with `m` odd. Then

\[
\Phi_{2m}(-1)=\Phi_m(1),
\]

so

\[
\log\Phi_n(-1)=\Lambda(m)=\Lambda(n/2).
\tag{17}
\]

This is nonzero precisely when `m=p^k` is an odd prime power.

### At least two factors of two

For `a>=2` and odd `m`, repeated cyclotomic parity gives

\[
\Phi_{2^a m}(x)
=\Phi_{2m}\!\left(x^{2^{a-1}}\right).
\tag{18}
\]

At `x=-1`, the exponent is even, hence

\[
\Phi_{2^a m}(-1)=\Phi_{2m}(1).
\tag{19}
\]

If `m>1`, `2m` is not a prime power and this is `1`. If `m=1`, then `2m=2` and the value is `2`. Equivalently,

\[
\log\Phi_n(-1)=\Lambda(n/2)
\qquad(a>=2).
\tag{20}
\]

Combining (16)--(20),

\[
\boxed{
\log\Phi_n(-1)
=\mathbf1_{2\mid n}\Lambda(n/2),
\qquad n>2,
}
\tag{21}
\]

with the convention that `Lambda` vanishes away from integer prime powers. Substituting into (14) gives the exact current-energy law

\[
\boxed{
E_n^{\rm cur}
:=\frac12\log\det(4D^2|_{H_n})
=\Lambda(n)+\mathbf1_{2\mid n}\Lambda(n/2),
\qquad n>2.
}
\tag{22}
\]

The first canonical reflection-odd positive energy therefore has the wrong arithmetic support:

\[
\begin{array}{c|c|c}
n & \Lambda(n) & E_n^{\rm cur}\\ \hline
p^k,\ p\text{ odd} & \log p & \log p\\
2p^k,\ p\text{ odd} & 0 & \log p\\
2^k,\ k>=2 & \log2 & 2\log2\\
\text{other composite} & 0 & 0.
\end{array}
\tag{23}
\]

For example,

\[
E_6^{\rm cur}=\log3,
\qquad
E_{10}^{\rm cur}=\log5,
\qquad
E_4^{\rm cur}=2\log2.
\tag{24}
\]

These are exact finite counterexamples, not asymptotic leakage. Multiplying the shell scalar by the critical attenuation `n^{-1/2}` would simply attenuate the false support; it would not remove it.

## 5. The actual positive quadratic form is still shell diagonal

The determinant is only a nonlinear shell readout. The genuine positive quadratic energy generated by the candidate is

\[
\mathcal E_D(f)=\langle f,D^2f\rangle\ge0.
\tag{25}
\]

But `D^2` is a scalar Fourier multiplier and preserves every exact-order shell. Hence for the normalized Ramanujan features `u_n` used in `WP-037`--`WP-049`,

\[
\boxed{
\langle u_m,D^2u_n\rangle=0
\qquad(m\ne n).
}
\tag{26}
\]

So the new odd first-order operator does not evade the category mismatch in `WP-043` after positivity is taken: its square returns to scalar spectral/convolution geometry, while the finite Weil birth form uses pointwise products `eta_R(u_mu_n)` and has essential cross-shell couplings.

Using `D` itself does not produce a positive form. Using `D^*D=D^2`, `|D|`, or any even functional calculus restores positivity but also restores shell-preserving scalar calculus. Thus the determinant identity (22) is the strongest arithmetic feature of this direct route, not a hidden Weil quadratic form.

## 6. Reflection supertrace and index are forced to cancel above order two

Equation (5) gives a stronger obstruction than the parity-isospectral statement of `WP-049` for the original cycle Laplacian. The candidate odd differential itself has no higher-shell cohomology:

\[
\ker(D|_{H_n})=0,
\qquad n>2.
\tag{27}
\]

Its positive square acts with the same nonzero singular values on `H_n^+` and `H_n^-`. Therefore, for every scalar function `F` for which the finite-shell expression is defined,

\[
\boxed{
\operatorname{Tr}\left(RF(D^2)|_{H_n}\right)=0,
\qquad n>2.
}
\tag{28}
\]

and any supersymmetric index built only from this odd pair is zero. The sole primitive zero mode is the order-two reflection-fixed character (6), not the prime-power tower.

Thus the exact sequence one might have hoped for,

```text
anchored reflection
    -> odd cycle differential D
    -> positive square D^2
    -> Hodge/Lefschetz grading
    -> Mangoldt shell index
```

fails twice: `D^2` has the dyadic determinant shadow, and the actual graded index cancels completely for every `n>2`.

## 7. The obstruction extends to every local scalar reflection-odd cycle differential

The failure at `q=2` is not special to choosing the shortest difference `(U-U^*)/(2i)`.

Let

\[
Q=d(U)
\]

be any finite-range translation-invariant scalar cycle operator, with Laurent polynomial symbol

\[
d(z)=\sum_{k=-M}^M a_k z^k.
\]

If `Q` is odd under the anchored reflection,

\[
RQR=-Q,
\]

then `RUR=U^{-1}` forces

\[
\boxed{d(z^{-1})=-d(z).}
\tag{29}
\]

In particular, both reflection-fixed spectral points satisfy

\[
d(1)=0,
\qquad
d(-1)=0.
\tag{30}
\]

More precisely, every anti-invariant Laurent polynomial factors as

\[
\boxed{
d(z)=(z-z^{-1})h(z+z^{-1})
}
\tag{31}
\]

for an ordinary polynomial `h`. This follows termwise from

\[
z^k-z^{-k}
=(z-z^{-1})
U_{k-1}\!\left(\frac{z+z^{-1}}2\right),
\]

where `U_{k-1}` is the Chebyshev polynomial of the second kind.

Consequently every such local odd differential has positive square symbol containing the mandatory factor

\[
|z-z^{-1}|^2
=L_{\rm cyc}(4-L_{\rm cyc})
\tag{32}
\]

on the unit circle, up to the nonnegative factor `|h(z+z^{-1})|^2`.

This yields a reusable boundary condition:

\[
\boxed{
\text{finite-range + translation-invariant + scalar + reflection-odd}
\Longrightarrow
\text{annihilates the order-two mode.}
}
\tag{33}
\]

The conclusion does **not** cover a non-translation-invariant operator that mixes exact-order shells, a matrix-valued/noncommutative differential, or a singular nonlocal multiplier undefined at `z=-1`. Those are precisely the kinds of genuinely new structure that could evade the factorization.

## 8. Direct removal of the antipodal factor collapses back to WP-043 and deletes the q=2 selector

For the canonical current, equation (9) makes the apparent repair explicit. On a subspace where `4I-L_cyc` is invertible,

\[
(4D^2)(4I-L_{\rm cyc})^{-1}=L_{\rm cyc}.
\tag{34}
\]

At the determinant level this removes `Phi_n(-1)` and leaves exactly the `Phi_n(1)` Mangoldt determinant of `WP-043`.

But this is not a new positive completion. It simply returns to the scalar cycle operator whose positivity already lives in the wrong pairing category. Worse, globally

\[
4I-L_{\rm cyc}=(I+U)^*(I+U)
\]

has kernel exactly at

\[
U=-1,
\qquad \gamma=\frac12.
\tag{35}
\]

Thus the inverse in (34) is singular precisely on the order-two mode that `WP-048` independently singled out as the canonical `q=2` real-Gamma channel.

A pseudoinverse or quotient can of course remove that one mode, but then the construction has explicitly separated away the very archimedean selector the line is trying to obtain from the same geometry. Such a quotient would require an additional independent sign theorem and a principled treatment of the removed channel; it is not supplied by the current energy itself.

This is the sharp finite--archimedean tension exposed by the odd-differential route:

\[
\boxed{
\text{reflection oddness forces an antipodal zero,}
\quad
\text{while the antipode is the intrinsic real-Gamma selector.}
}
\tag{36}
\]

## 9. The new Hardy relative trace gives the opposite endpoint combination, but not a positive rescue

The contemporaneous Prime-Circle finding

`research/prime_circle/findings/PC-076-hardy-hilbert-relative-trace-is-parity-twisted-von-mangoldt.md`

provides an unusually strong matched control because it comes from a genuinely nonlocal Hardy/Hankel construction rather than scalar cycle calculus. For its trace-class remainder `T_n`, it proves

\[
\boxed{
2\operatorname{Tr}T_n
=\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2),
\qquad n>1.
}
\tag{37}
\]

For `n>2`, equations (22) and (37) are respectively the **sum** and **difference** of the same two endpoint logarithms. Hence

\[
\boxed{
\Lambda(n)
=\frac12\left(
E_n^{\rm cur}+2\operatorname{Tr}T_n
\right),
\qquad n>2,
}
\tag{38}
\]

and

\[
\boxed{
\mathbf1_{2\mid n}\Lambda(n/2)
=\frac12\left(
E_n^{\rm cur}-2\operatorname{Tr}T_n
\right).
}
\tag{39}
\]

This is an exact and canonical decomposition of the two cyclotomic endpoints across two Mathia-native readouts. It does **not** solve the positivity problem.

The current contribution `E_n^{cur}` is the logarithm of a determinant of a positive shell energy, hence a nonlinear scalar invariant. The Hardy term is a relative trace whose sign is genuinely mixed: `PC-076` gives negative values at `n=2p^k` for odd prime powers and zero on higher powers of two. Equation (38) therefore isolates the desired finite support only by adding a signed correction to a nonlinear positive determinant readout.

Exponentiating (38), taking a determinant ratio, or naming the pair an intersection form does not change that fact. No positive quadratic form on the Weil test space has been produced, and no independent theorem forces the signed Hardy correction to combine globally with the selected Gamma channel into Weil nonnegativity.

The control is nevertheless useful: **two independently derived nonlocal/local Prime-Circle constructions now resolve exactly the same `+1/-1` endpoint pair.** This makes it less plausible that another scalar endpoint recombination, determinant, or first relative trace will supply the missing global sign. A surviving construction must create information before this endpoint collapse.

## 10. Prior-art and novelty audit

No historical novelty is claimed for the ingredients in the calculation.

- The cycle shift, its symmetric Laplacian, and the skew current `(U-U^*)/(2i)` are standard discrete Fourier/cycle operators.
- The anti-invariant Laurent-polynomial factorization in (31) is elementary invariant theory for `z <-> z^{-1}`; equivalently it follows from the standard Chebyshev identity displayed there.
- The cyclotomic endpoint identities `Phi_n(1)` and `Phi_n(-1)` are classical. `WP-043` and the newly read `PC-076` already persist the exact endpoint classifications needed here.
- Reflection-paired cancellation of an invertible odd operator is standard supersymmetric/Lefschetz structure and is consistent with the broader cancellation warning already recorded in `WP-020`.

A targeted literature audit of cyclotomic endpoint values, cycle/current operators, reflection-odd discrete differentials, and determinant formulas found the expected classical component identities, but no basis for treating their conjunction as a new general theorem about Weil positivity. Absence of a source using the Prime-Circle vocabulary is not novelty evidence.

The durable project-specific content is the collision of four already intrinsic Mathia structures:

1. the compatible positive cycle geometry and Mangoldt shell determinant of `WP-043`;
2. the canonical anchored reflection and `q=2` Gamma selector of `WP-048`;
3. the need for a genuinely odd/non-scalar coupling left open by `WP-049`;
4. the opposite antipodal endpoint trace newly derived in `PC-076`.

The exact result is a **no-go for the canonical local odd-differential completion**, not a new cyclotomic identity or a new proof of any explicit formula.

## 11. Matched controls and falsification surface

The strongest matched control is deliberately non-arithmetic. Any anchored cyclic root tower with the same compatible shift and reflection has equations (1)--(13), the factorization (31), and the mandatory zeros at `+1` and `-1`. Thus the sign theorem `D^2>=0` is universal cycle geometry rather than RH-specific information.

The finding has short exact failure points:

1. verify `RUR=U^*` and hence `RDR=-D`;
2. verify the multiplier `sin(2 pi gamma)` and invertibility on every primitive shell `n>2`;
3. verify `4D^2=L_cyc(4I-L_cyc)`;
4. multiply the primitive-shell eigenvalues and obtain `(Phi_n(1)Phi_n(-1))^2`;
5. check the three parity cases in Section 4 and recover (21);
6. check the finite falsifiers `n=4,6,10` in (24);
7. verify that every finite-range scalar anti-invariant Laurent symbol factors as in (31);
8. verify that cancelling `4I-L_cyc` returns `L_cyc` and that the cancelled factor vanishes at `gamma=1/2`;
9. independently compare (22) with the canonical `PC-076` trace formula (37).

Failure of any of 1--5 would invalidate the arithmetic obstruction. Failure of 7 would invalidate the broader local-odd class statement while leaving the canonical `D` counterexample intact. Success of all nine still says nothing against a shell-mixing, matrix-valued, singular, noncommutative, boundary, or genuinely cohomological construction outside the stated hypotheses.

## 12. Consequence for the Weil-positivity search

The post-`WP-049` escape can now be narrowed substantially. It is no longer enough to say that reflection orientation survives inside a positive operator and therefore an odd differential might recover a Hodge/Lefschetz sign. The most intrinsic odd differential exists and can be analyzed exactly:

```text
anchored reflection
    -> canonical odd current D
    -> positive square D^2
    -> mandatory (+1) x (-1) endpoint product
    -> Lambda(n) + dyadic Lambda(n/2)
    -> zero higher-shell index.
```

Moreover, every local translation-invariant scalar reflection-odd differential inherits the antipodal zero, while the antipode is precisely the `q=2` archimedean selector. The direct inverse repair removes that selector and collapses to `WP-043`. The independent Hardy/Hankel route supplies the opposite endpoint difference, but only as a signed relative trace.

A viable continuation must therefore break at least one of the hypotheses behind (33) **before** taking positivity. In concrete terms it needs a shell-mixing or matrix-valued/noncommutative operator, an infinite-dimensional boundary/cohomological sector, or another nonseparable finite--archimedean construction in which the order-two mode can couple to higher primitive shells without being annihilated by reflection oddness. Its final nonnegativity must then follow from an independent geometric theorem and produce the finite birth coefficients, Gamma term, and polar/global counterterms in one audited form rather than from a determinant-plus-signed-trace recombination.