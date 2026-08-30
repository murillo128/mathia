# WP-034 — Prime-Circle boundary birth energy contains the critical Weil ray weights, but is unbounded below

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct attempt to use the finite renormalized Prime-Circle boundary Dirichlet energy of `PC-057` as a positive finite-place Weil form. After primitive-shell normalization, the same intrinsically two-dimensional boundary construction does produce the critical prime-power attenuation `log(p) p^{-k/2}` with the **correct Weil sign** on every interior `p`-ray jump. However, the resulting finite operator is unbounded below along each infinite prime-power ray: on the cutoff `1,p,...,p^A` its lowest eigenvalue is exactly `-A log p`, and on a divisor box `D(N)` the lowest eigenvalue is exactly `-log N`. The full pre-renormalized Dirichlet Gram remains positive only because a universal divergent collision term multiplies the identity after shell extraction. Removing that divergence exposes the Weil-signed finite arithmetic but destroys semiboundedness.

There is also an exact sign-flipped comparison. Subtracting the `PC-057` local operator from its cutoff-independent top eigenvalue gives a positive operator whose interior block is the critical `sigma=1/2` Poisson/GCD kernel of `PL-030` plus a nonnegative height diagonal. Thus the stable positive orientation classicalizes into the already-audited Poisson route of `WP-022`, while the orientation carrying the Weil sign is the one that runs to `-infinity`. The first birth from valuation zero has an additional `sqrt(p/(p-1))` factor, so even the exact interior coefficient bridge is not a translation-invariant realization of the full finite Weil comb.

This finding therefore records a genuine Mathia cross-connection but not a new positivity proof: Prime Circle now supplies an intrinsic route to the critical finite coefficients, yet its own boundary positivity is carried by the divergent background rather than by the renormalized Weil-signed form. No archimedean Gamma/digamma term is generated.

## 1. The exact Prime-Circle finite boundary operator

`PC-057` begins with the full-root harmonic fields

\[
V_n(z)=\Log(1-z^n)
\]

and the exact radial Dirichlet Gram matrix

\[
G^{\rm full}_{m,n}(x)
=
-\gcd(m,n)\log\!\left(1-x^{\operatorname{lcm}(m,n)}\right),
\qquad 0<x<1.
\tag{1}
\]

For fixed `m,n`, as `x -> 1^-`,

\[
G^{\rm full}_{m,n}(x)
=
\gcd(m,n)\Lambda_x
-\gcd(m,n)\log\operatorname{lcm}(m,n)
+o(1),
\tag{2}
\]

where

\[
\Lambda_x=-\log(1-x).
\tag{3}
\]

Let `Z` be divisor incidence, `M=Z^{-1}` its Möbius inverse, and `D_phi=diag(phi(n))`. The classical Smith factorization gives

\[
[\gcd(m,n)]=Z D_\varphi Z^{\mathsf T}.
\tag{4}
\]

Therefore on any fixed finite divisor-closed set the primitive-shell-normalized full Gram has the asymptotic form

\[
\boxed{
\widehat G_x
:=
D_\varphi^{-1/2}M G^{\rm full}(x)M^{\mathsf T}D_\varphi^{-1/2}
=
\Lambda_x I+C+o(1).
}
\tag{5}
\]

Here `C` is exactly the finite normalized birth operator classified in `PC-057`.

For

\[
N=\prod_{p\mid N}p^{A_p},
\]

`PC-057` proves the exact Kronecker-sum decomposition

\[
\boxed{
C_{\mathcal D(N)}
=
\bigoplus_{p\mid N}^{\rm Kron}H_{p,A_p}.
}
\tag{6}
\]

Write

\[
q=p^{-1/2},
\qquad
s=\sqrt{1-q^2},
\qquad
c=\frac1{p-1},
\]

and

\[
H_{p,A}=(\log p)h_{p,A}
\]

on exponent coordinates `a=0,...,A`. Then

\[
(h_{p,A})_{00}=0,
\tag{7}
\]

\[
(h_{p,A})_{0b}=(h_{p,A})_{b0}
=-\frac{q^b}{s},
\qquad b\ge1,
\tag{8}
\]

and, for `a,b>=1`,

\[
(h_{p,A})_{ab}
=
\begin{cases}
-a+c,&a=b,\\[1mm]
-q^{|a-b|},&a\ne b.
\end{cases}
\tag{9}
\]

All statements below are consequences of this exact matrix and its exact spectrum from `PC-057`; no numerical extrapolation or zero data are used.

## 2. The interior off-diagonal entries are exactly the critical Weil weights

For two positive valuations `a,b>=1`, put

\[
k=|a-b|\ge1.
\]

Equation (9) gives

\[
(H_{p,A})_{ab}
=-(\log p)p^{-k/2}.
\tag{10}
\]

Since

\[
\Lambda(p^k)=\log p,
\]

this is precisely

\[
\boxed{
(H_{p,A})_{ab}
=-\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\tag{11}
\]

This is the sign appearing in the finite-prime Weil quadratic functional of `WP-005`. In particular, the half-critical attenuation is not inserted here by the Prime-Lattice heat factor of `WP-004`: it emerges from the `phi`-shell normalization of the two-dimensional Prime-Circle boundary energy.

The same fact can be read directly from the global shell formula in `PC-057`. For `n=dp^k>d`,

\[
C_{n,d}
=-\log p\sqrt{\frac{\varphi(d)}{\varphi(n)}}.
\tag{12}
\]

If `p|d`, then

\[
\varphi(dp^k)=p^k\varphi(d),
\]

so (12) becomes exactly

\[
C_{dp^k,d}
=-\frac{\log p}{p^{k/2}}.
\tag{13}
\]

Thus Prime Circle and Prime Lattice independently reach the same critical finite coefficient, but through different intrinsic constructions.

This is a real bridge. It is nevertheless only an **interior ray** bridge, not yet a global translation rule.

## 3. The valuation-zero endpoint has a fixed arithmetic anomaly

If `p` does not divide `d`, then

\[
\varphi(dp^k)
=
\varphi(d)p^{k-1}(p-1).
\]

Equation (12) therefore gives

\[
\boxed{
C_{dp^k,d}
=
-\sqrt{\frac{p}{p-1}}
\frac{\log p}{p^{k/2}}.
}
\tag{14}
\]

Equivalently, (8) differs from the interior coefficient by the factor

\[
\frac1s
=
\sqrt{\frac{p}{p-1}}.
\tag{15}
\]

The finite Weil translation comb does not have such a base-point dependence: the coefficient attached to the displacement `log p^k` is `-(log p)p^{-k/2}` regardless of whether the starting integer is already divisible by `p`.

Therefore the exact Prime-Circle bridge cannot simply be relabeled as a representation of the full finite Weil translation operator. The primitive-shell geometry distinguishes the **first birth of a prime direction** from later motion along that direction.

This endpoint defect is small for large `p` but is exact and structural; it cannot be discarded in a theorem-level identification.

## 4. The Weil-signed finite boundary operator is unbounded below

The decisive obstruction comes from the exact local spectrum derived in `PC-057`:

\[
\operatorname{Spec}(H_{p,A})
=
(\log p)
\left(
\{-A\}
\cup
\left\{
\frac1{p-1}-j:
0\le j<A
\right\}
\right).
\tag{16}
\]

Because

\[
-A<\frac1{p-1}-(A-1),
\]

the lowest eigenvalue is exactly

\[
\boxed{
\lambda_{\min}(H_{p,A})=-A\log p.
}
\tag{17}
\]

Hence the sequence of finite ray operators has no cutoff-independent lower bound:

\[
\inf_A\lambda_{\min}(H_{p,A})=-\infty.
\tag{18}
\]

The same conclusion is already visible from the diagonal:

\[
(H_{p,A})_{aa}
=(\log p)\left(-a+\frac1{p-1}\right),
\qquad a\ge1,
\tag{19}
\]

which tends to `-infinity` with the prime-power exponent.

For the full divisor box, the Kronecker-sum spectrum adds the local minima. Thus

\[
\boxed{
\lambda_{\min}(C_{\mathcal D(N)})
=-\sum_{p\mid N}A_p\log p
=-\log N.
}
\tag{20}
\]

Consequently, on the canonical exhaustion by divisor boxes, the renormalized boundary operator carrying the Weil-signed interior coefficients is not merely indefinite: its negative edge runs away at the exact height scale `log N`.

A scalar shift preserving every off-diagonal coefficient must therefore satisfy

\[
\delta_{p,A}\ge A\log p
\]

locally, and

\[
\delta_N\ge\log N
\]

globally, if it is to make the finite cutoff positive. The **minimal** scalar shifts are exactly those values by (17) and (20), so they diverge with the cutoff.

This rules out a cutoff-independent positive-energy completion obtained merely by adding one finite diagonal counterterm while retaining the Prime-Circle finite operator unchanged.

## 5. Where the original Dirichlet positivity went

There is no contradiction with the positivity of the original Dirichlet Gram matrix (1). Equation (5) shows exactly where that positivity lives after primitive extraction:

\[
\widehat G_x
=
\underbrace{\Lambda_x I}_{\text{universal collision background}}
+
\underbrace{C}_{\text{finite arithmetic birth term}}
+o(1).
\tag{21}
\]

For every fixed finite box, `Lambda_x -> +infinity` as the boundary is approached. The positive divergent identity masks the negative modes of `C`.

Thus the natural Prime-Circle process has the same qualitative failure pattern encountered elsewhere in this research line, but in a new intrinsic geometry:

```text
positive geometric energy
    -> subtract universal divergent background
    -> exact finite arithmetic / Weil-signed coefficients appear
    -> the renormalized finite form loses semiboundedness.
```

The divergent term in (21) is not the archimedean Gamma/digamma sector of the completed explicit formula. It is the universal logarithmic collision divergence of the circle boundary metric. Keeping it proves positivity of the original Dirichlet energy but does not prove Weil positivity; subtracting it exposes the desired finite arithmetic and removes the sign theorem.

A joint cutoff/boundary limit could deliberately let `Lambda_x` grow with `log N`, but `PC-057` does not force a canonical relation between these two independent cutoffs. Moreover the fixed-`N` expansion (5) is not uniform enough to identify such a joint limit by itself. Any future proposal of this type must derive the coupling from geometry and analyze the exact kernel (1), rather than choose `1-x` as a function of `N` solely to cancel (20).

## 6. The stable positive sign flip is the existing critical Poisson/GCD geometry

The opposite orientation has a completely different behavior. Equation (16) shows that the **largest** eigenvalue of every `H_{p,A}` is cutoff-independent:

\[
\lambda_{\max}(H_{p,A})
=
\frac{\log p}{p-1}
=:\kappa_p.
\tag{22}
\]

Therefore

\[
\boxed{
L_{p,A}:=\kappa_p I-H_{p,A}\succeq0
}
\tag{23}
\]

for every `A`, with no growing local spectral shift.

On the positive-exponent block `a,b>=1`, (9) gives

\[
\frac{1}{\log p}(L_{p,A})_{ab}
=
\begin{cases}
a,&a=b,\\[1mm]
p^{-|a-b|/2},&a\ne b.
\end{cases}
\tag{24}
\]

Let

\[
K_p(a,b)=p^{-|a-b|/2}.
\tag{25}
\]

Then

\[
\boxed{
P_+L_{p,A}P_+
=(\log p)
\left(K_p+\operatorname{diag}(a-1)_{a=1}^A\right).
}
\tag{26}
\]

The kernel `K_p` is exactly the one-prime factor of the normalized GCD kernel of `PL-030` at the critical parameter `sigma=1/2`:

\[
K_{1/2}(m,n)
=
\prod_p p^{-|v_p(m)-v_p(n)|/2}.
\tag{27}
\]

Its positive harmonic representation is the classical Poisson kernel with radius

\[
r_p=p^{-1/2},
\]

whose Fourier coefficients are `r_p^{|k|}`. The Aistleitner--Berkes--Seip Poisson/GCD framework is already recorded in `SOURCES.md`, and `WP-022` has already tested the corresponding critical Poisson score as a Weil-positivity mechanism.

So the stable positive orientation of the new Prime-Circle operator does **not** reveal an independent positive structure. On the interior it decomposes into the already-known critical Poisson/GCD Gram kernel plus an elementary nonnegative height diagonal. Crucially, its off-diagonal entries have the **opposite sign** from (11):

\[
(L_{p,A})_{ab}
=+\frac{\log p}{p^{|a-b|/2}}
\qquad(a\ne b,\ a,b\ge1).
\tag{28}
\]

This produces an exact sign dichotomy:

\[
\boxed{
\begin{array}{ll}
H_{p,A}: & \text{correct Weil sign, but }\lambda_{\min}=-A\log p\to-\infty,\\[1mm]
\kappa_p I-H_{p,A}: & \text{positive with stable shift, but the finite Weil sign is reversed.}
\end{array}
}
\tag{29}
\]

That is the main positivity obstruction.

## 7. The stable shift already points to the Euler pole, not to the Gamma sector

The cutoff-independent local constant in (22) is

\[
\kappa_p
=\frac{\log p}{p-1}.
\tag{30}
\]

For `s>1`, the Euler product gives

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_p\frac{\log p}{p^s-1}.
\tag{31}
\]

Thus `kappa_p` is exactly the local `s -> 1^+` value of the summand in (31). Its all-prime sum diverges:

\[
\sum_p\kappa_p=\infty.
\tag{32}
\]

No prime number theorem is required for divergence; for all sufficiently large primes,

\[
\frac{\log p}{p-1}\ge\frac1p,
\]

and Euler's prime harmonic series diverges.

This is also the same local pole-normalization coefficient appearing, up to the conventional factor `2`, in the critical product-Poisson score of `WP-022`:

\[
2\frac{\log p}{p-1}
-2\sum_{k\ge1}\frac{\log p}{p^{k/2}}\cos(k\theta).
\tag{33}
\]

Accordingly the Prime-Circle boundary calculation independently rediscovers both pieces already visible in the Prime-Lattice Poisson analysis:

- the critical finite ray scale `(log p)p^{-k/2}`;
- a local normalization coefficient whose global sum hits the zeta pole at `s=1`.

But it still produces **no archimedean Gamma/digamma contribution**, and the pole coefficient occurs in the sign-flipped positive completion rather than turning the Weil-signed operator itself positive.

This is a cross-Mathia consistency check, not a completed local-to-global mechanism.

## 8. Matched control and novelty audit

The broad ingredients are classical and no theorem-level novelty is claimed.

- The Smith/power-GCD factorization behind `PC-057` is classical matrix arithmetic; `PC-057` already audits that literature and identifies the finite boundary term as the tangent of a power-GCD family.
- The kernel `rho^{|a-b|}` is the classical Kac--Murdock--Szego / Poisson covariance kernel.
- `PL-030` identifies the product of the local kernels `p^{-sigma|a-b|}` with the normalized GCD Gram geometry, and Aistleitner--Berkes--Seip provide the established Poisson-polydisc realization.
- `WP-022` already derives the critical finite Weil cosine coefficients and the pole-bearing normalization from the logarithmic score of that Poisson family, and proves that its Fisher positivity becomes infinite at the critical boundary.

The durable Mathia-specific content here is the **exact cross-identification forced by a different intrinsic construction**: the two-dimensional Prime-Circle boundary-renormalization operator has, after the canonical `phi` shell normalization, the same critical half-weight on its interior prime-power jumps. Its exact spectrum then shows why this does not supply a second positivity route.

The positivity component itself is not rational-prime-specific. Replacing `log p` by a positive generator energy `a` and `p^{-1/2}` by `e^{-a/2}` gives the same positive Poisson kernel `e^{-|j-k|a/2}` on a free one-generator ray. What is special in the rational-prime construction is how the cyclotomic shell populations produce the exact `phi` normalization and the first-birth endpoint factor. This matched control prevents interpreting the local positive kernel as hidden RH information.

## 9. Boundary of the obstruction

WP-034 does **not** rule out:

- using the **exact unrenormalized** boundary Gram (1) in a geometrically forced joint limit where the radial boundary scale and arithmetic cutoff are coupled nontrivially;
- a quotient or compression that removes the runaway negative-height direction while preserving the exact interior Weil coefficients and whose positivity follows from an independent theorem;
- a construction that uses the valuation-zero endpoint anomaly as useful boundary data rather than trying to erase it;
- coupling Prime Circle to an archimedean/boundary/cohomological sector **before** subtracting the universal collision term;
- a non-scalar positive completion that changes the state space or interaction while retaining a rigorously derived bridge to the Weil test-function space;
- a genuinely global operation in which the Poisson/GCD block is only one local component and the Gamma/polar terms arise from the same object.

Those are real escape routes. The finding rules out the much more direct claim that the finite renormalized Prime-Circle boundary energy itself is the missing positive Weil form, or that its stable sign-flipped positivity is new evidence beyond the already-classified Poisson/GCD mechanism.

## 10. Falsification tests and research consequence

The claim can be falsified by any failure of the following exact checks:

1. primitive-shell normalization sends the leading GCD collision form to the identity as in (5);
2. the `PC-057` local entries are (7)--(9);
3. for `a,b>=1`, the off-diagonal entry is exactly `-(log p)p^{-|a-b|/2}`;
4. the first-birth edge from valuation zero has the factor `sqrt(p/(p-1))` in (14);
5. the exact local spectrum is (16), giving minimum `-A log p` and maximum `(log p)/(p-1)`;
6. Kronecker addition of local minima gives the global divisor-box minimum `-log N`;
7. therefore every scalar positivity shift that keeps the Weil-signed cutoff operator unchanged diverges at least as `log N` on the canonical exhaustion;
8. the cutoff-independent positive sign flip (23) has the interior decomposition (26);
9. `K_p(a,b)=p^{-|a-b|/2}` is exactly the local `sigma=1/2` Poisson/GCD kernel already present in `PL-030`;
10. `kappa_p=(log p)/(p-1)` is the local `s=1` Euler-log-derivative coefficient and its prime sum diverges;
11. none of these constructions generates the archimedean Gamma/digamma term or proves positivity of the assembled Weil functional.

All eleven tests use finite matrix algebra, classical Euler/Poisson identities, or already-persisted exact Mathia findings. No RH assumption, zero ordinate, analytic continuation to the critical strip, or numerical fitting enters.

The research consequence is a sharper classification of the strongest current Prime-Circle boundary route:

\[
\boxed{
\text{positive 2D Dirichlet Gram}
\to
\text{remove universal collision background}
\to
\text{exact critical Weil-signed interior edges}
\to
\text{finite operator unbounded below};
}
\]

while

\[
\boxed{
\text{stable positive sign flip}
\to
\text{critical Poisson/GCD kernel + height}
\to
\text{already-audited pole normalization, no Gamma sector}.
}
\]

So the missing global mechanism is no longer allowed to treat Prime Circle's finite boundary correction as a ready-made positive form. It must explain, geometrically and before positivity is asserted, how to handle **all three** obstructions visible here: the runaway negative height, the valuation-zero endpoint mismatch, and the absent archimedean completion.

## Internal dependencies

- `research/prime_circle/findings/PC-057-finite-boundary-birth-energy-separates-into-prime-local-spectra.md`
- `research/prime_lattice/findings/PL-030-gcd-poisson-measure-class-transition.md`
- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-005-prime-lattice-axis-positivity-does-not-survive-weil-autocorrelation-lift.md`
- `research/weil_positivity/findings/WP-009-prime-lattice-weil-weights-fail-passive-jump-energy.md`
- `research/weil_positivity/findings/WP-022-prime-torus-poisson-score-fisher-positivity-breaks-at-critical-boundary.md`
