# WP-097 — Mixed-prime product completion gives a sharp finite diagonal threshold

**Status:** `EXACT-DERIVED + DECISIVE-BOUNDARY + PRIOR-ART-BOUNDARY`. This finding closes the specific mixed-prime escape left open by `WP-096` at the algebraic positive-kernel level. It does **not** produce global Weil positivity: the construction below prescribes the critical one-prime Weil moments, has no archimedean sector, and is universal for free multiplicative generators. The product-measure/Riesz-product ingredients are classical harmonic analysis; no novelty is claimed for them. The Mathia-specific result is the exact sharp threshold and the proof that mixed-prime Fourier terms can restore ordinary positivity with finite diagonal mass, while deleting those terms returns precisely the divergent sparse obstruction of `WP-096`.

## Claim

Keep the exact cover-positive normal form of `WP-096`. Thus a finite-valued nonnegative Hermitian form with

\[
q(W_nx)=nq(x)
\]

is represented, after the `WP-093` critical first-order conjugacy, by a finite positive measure `mu` on the prime torus

\[
\widehat{\mathbb Q_+^\times}\cong\prod_p\mathbb T,
\]

with multiplicative Fourier kernel

\[
\varphi(r)=\int\chi(r)\,d\mu(\chi).
\tag{1}
\]

`WP-096` ruled out finite diagonal mass when the only nonzero off-identity coefficients are the critical one-prime Weil rays

\[
\varphi(p^k)
=-\frac{\log p}{p^{|k|/2}},
\qquad k\in\mathbb Z\setminus\{0\},
\tag{2}
\]

and all mixed-prime coefficients are forced to vanish. It explicitly left open whether nonzero mixed-prime coefficients can restore positivity.

They can, and the required diagonal mass has an exact finite threshold.

Let

\[
C=\varphi(1)=\mu\!\left(\prod_p\mathbb T\right).
\tag{3}
\]

There exists a finite positive measure satisfying **all** ray conditions (2), with arbitrary mixed-prime Fourier coefficients allowed, if and only if

\[
\boxed{
C\ge C_*:=\frac{2\log2}{\sqrt2-1}
=2(\sqrt2+1)\log2.
}
\tag{4}
\]

For every `C>=C_*` one explicit realization is the countable product measure

\[
\boxed{
\mu_C
=C\bigotimes_p
\left[
1+\frac{\log p}{C}
\left(1-P_{p^{-1/2}}(\theta_p)\right)
\right]\frac{d\theta_p}{2\pi},
}
\tag{5}
\]

where

\[
P_r(\theta)
=\frac{1-r^2}{1-2r\cos\theta+r^2}
=1+2\sum_{k\ge1}r^k\cos(k\theta).
\tag{6}
\]

If a reduced rational uses the distinct primes in a finite set `F`,

\[
r=\prod_{p\in F}p^{k_p},
\qquad k_p\ne0,
\]

then (5) has the exact mixed coefficient

\[
\boxed{
\varphi_C(r)
=(-1)^{|F|}C^{1-|F|}
\prod_{p\in F}
(\log p)\,p^{-|k_p|/2}.
}
\tag{7}
\]

In particular (7) restricts to the required Weil value (2) on every one-prime ray.

The important boundary is that these mixed terms are not a harmless optional perturbation. On every finite prime set `P`, deleting all terms involving at least two prime coordinates from the positive density (5) gives exactly the sparse density of `WP-096`,

\[
w^{\rm sparse}_{P,C}(\theta)
=C+\sum_{p\in P}(\log p)
\left(1-P_{p^{-1/2}}(\theta_p)\right),
\tag{8}
\]

whose minimum is

\[
C-D(P),
\qquad
D(P)=2\sum_{p\in P}\frac{\log p}{\sqrt p-1}\longrightarrow\infty.
\tag{9}
\]

Thus the positive completion exists with finite `C`, but its cross-prime Fourier interactions are exactly what prevent the sparse one-prime projection from becoming negative. Any global Weil route using this escape must therefore supply a **structural positivity-preserving operation** that turns those mixed interactions into the desired Weil readout; simple Fourier deletion / first-prime-chaos projection destroys the sign theorem.

## 1. Every one-prime marginal forces a finite lower bound

Assume first that `mu` is any finite positive measure satisfying (2), without making any assumption on mixed-prime coefficients. Push `mu` forward to the `p`-th circle coordinate. Its total mass is `C`, and its nonzero Fourier coefficients are fixed by (2). Because

\[
\sum_{k\ne0}
\left|\frac{\log p}{p^{|k|/2}}\right|<\infty,
\]

Fourier uniqueness identifies this marginal with the continuous density

\[
\begin{aligned}
w_{p,C}(\theta)
&=C-2(\log p)\sum_{k\ge1}p^{-k/2}\cos(k\theta)\\
&=C+(\log p)\left(1-P_{p^{-1/2}}(\theta)\right).
\end{aligned}
\tag{10}
\]

The Poisson kernel is maximized at `theta=0`, where

\[
P_r(0)=\frac{1+r}{1-r}.
\]

Putting `r=p^{-1/2}` gives

\[
\min_\theta w_{p,C}(\theta)
=C-c_p,
\qquad
c_p:=\frac{2\log p}{\sqrt p-1}.
\tag{11}
\]

A positive marginal therefore forces

\[
C\ge c_p
\qquad\text{for every prime }p.
\tag{12}
\]

The function

\[
c(x)=\frac{2\log x}{\sqrt x-1}
\]

is strictly decreasing for `x>1`. Indeed, with `y=sqrt(x)`,

\[
c(x)=\frac{4\log y}{y-1},
\]

and the derivative has the sign of

\[
1-\frac1y-\log y<0
\qquad(y>1).
\tag{13}
\]

Hence

\[
\sup_p c_p=c_2=C_*.
\tag{14}
\]

This proves the necessity of (4). Notice how much weaker it is than the sparse condition of `WP-096`: once mixed-prime Fourier data are permitted, positivity of the coordinate marginals asks for the **maximum** one-prime self-energy, not the divergent **sum** of all one-prime self-energies.

## 2. The sharp bound is attained by a positive product measure

Now assume `C>=C_*` and define for each prime

\[
\rho_{p,C}(\theta)
:=1+\frac{\log p}{C}
\left(1-P_{p^{-1/2}}(\theta)\right).
\tag{15}
\]

Equation (11) gives

\[
\rho_{p,C}(\theta)\ge1-\frac{c_p}{C}\ge0,
\tag{16}
\]

while the zero Fourier coefficient of `1-P_r` vanishes, so

\[
\int_{\mathbb T}\rho_{p,C}\,dm=1.
\tag{17}
\]

Thus every `rho_{p,C}dm` is a probability measure. Their countable product exists on the compact product torus, and multiplying by `C` gives the finite positive measure (5).

For `k!=0`, the Fourier expansion (6) yields

\[
\widehat{\rho_{p,C}}(k)
=-\frac{\log p}{C}\,p^{-|k|/2}.
\tag{18}
\]

Characters of `prod_p T` involve only finitely many coordinates, so product integration factors exactly. For

\[
r=\prod_{p\in F}p^{k_p}
\]

we obtain

\[
\begin{aligned}
\varphi_C(r)
&=C\prod_{p\in F}
\widehat{\rho_{p,C}}(k_p)\\
&=(-1)^{|F|}C^{1-|F|}
\prod_{p\in F}(\log p)p^{-|k_p|/2},
\end{aligned}
\]

which proves (7), and hence sufficiency. Together with the marginal lower bound, this proves the `if and only if` statement (4).

At the endpoint `C=C_*`, only the dyadic marginal reaches zero at `theta_2=0`; it remains a perfectly valid nonnegative probability density. No limiting subtraction or infinite diagonal is required.

## 3. Sparse Weil support is exactly the sign-destroying truncation

For a finite prime set `P`, the pushforward of `mu_C` has density

\[
\boxed{
w^{\rm prod}_{P,C}(\theta)
=C\prod_{p\in P}
\left[
1+\frac{\log p}{C}
\left(1-P_{p^{-1/2}}(\theta_p)\right)
\right]
\ge0.
}
\tag{19}
\]

Expanding the product by the number of distinct prime coordinates gives

\[
w^{\rm prod}_{P,C}
=C
+\sum_{p\in P}(\log p)(1-P_p)
+\text{terms involving at least two distinct primes},
\tag{20}
\]

where `P_p` abbreviates `P_{p^{-1/2}}(theta_p)`. The degree-zero plus degree-one part in (20) is precisely (8), the finite sparse carrier derived in `WP-096`.

This gives a matched control unavailable in `WP-096`: start from an honest positive measure that already has the exact desired one-prime moments, then erase only its mixed-prime Fourier coefficients. The result is not merely less positive; it becomes the exact `WP-096` obstruction.

At the simultaneous extremal point `theta_p=0`, write `c_p` as in (11). Then

\[
w^{\rm prod}_{P,C}(0)
=C\prod_{p\in P}\left(1-\frac{c_p}{C}\right)\ge0,
\tag{21}
\]

whereas

\[
w^{\rm sparse}_{P,C}(0)=C-D(P).
\tag{22}
\]

Therefore the aggregate contribution of the mixed-prime terms at that point is

\[
\boxed{
w^{\rm prod}_{P,C}(0)-w^{\rm sparse}_{P,C}(0)
=C\prod_{p\in P}\left(1-\frac{c_p}{C}\right)-C+D(P).
}
\tag{23}
\]

Whenever `D(P)>C`, (21) implies that (23) is at least `D(P)-C`; hence it diverges along prime exhaustion. The stabilizing mixed-prime sector is therefore **nonperturbative in aggregate** in the all-prime limit. A construction that first proves positivity and then simply discards mixed-prime data is throwing away the part of the form that pays for positivity.

## 4. Adversarial falsification and controls

This exact completion does not satisfy the research mandate by itself.

**The ray data are still prescribed.** The factors (15) were chosen so that their Fourier tails equal the critical values (2). The construction proves compatibility of those values with ordinary positivity; it does not explain why Mathia geometry should canonically select them.

**The diagonal is not canonically selected.** Positivity permits every `C>=C_*`. The minimal value `C_*` is selected by the dyadic marginal because `c_p` decreases with `p`; this is a sharp positivity threshold, not an intrinsic archimedean or polar normalization theorem.

**There is no archimedean completion.** Equations (5)-(23) live entirely on the finite-prime character torus. They generate neither the Gamma/digamma term nor the full polar functional of the Weil explicit formula.

**The mechanism is universal.** Replace the rational primes by free multiplicative generators `g`, prescribe positive weights `a_g` and radial decays `0<r_g<1`, and the same product construction works whenever

\[
\sup_g\frac{2a_gr_g}{1-r_g}<\infty.
\tag{24}
\]

Thus positivity of this product carrier does not distinguish the arithmetic of `Q` from a generalized-prime/free-generator model.

**Simple projection is fatal.** The most direct operation that extracts exactly the desired sparse Weil support is the Fourier projection onto constants plus one-prime coordinate subspaces. Equations (8)-(9) show that this projection is not positivity preserving. A viable quotient/compression must therefore be subtler than deleting higher prime-coordinate chaos.

These controls reject the tempting but invalid conclusion

```text
exact ray moments + positive prime-torus measure
    => global Weil positivity.
```

What has actually been proved is the narrower boundary

```text
exact ray moments
    + arbitrary mixed-prime Fourier data
    + ordinary positive finite measure
    <=> finite diagonal C >= C_*

but

positive product completion
    --erase mixed-prime interactions-->
WP-096 sparse carrier
    --> divergent negative minimum.
```

## 5. Relation to prior findings and prior art

- `WP-096` proved that **zero** mixed-prime coefficients force `C>=D(P)` on every finite prime set and hence infinite all-prime diagonal mass. The present finding proves that its stated mixed-prime escape is real and gives the sharp opposite endpoint: with unrestricted mixed coefficients, `C>=C_*` is necessary and sufficient.
- `WP-022` used a different product-Poisson object. There the canonical Poisson densities have Fourier moments given by the GCD kernel, while the **logarithmic radial score** produces the critical finite-Weil coefficients; Fisher positivity then diverges at `sigma=1/2`. Here the critical coefficients are moments of the positive measure itself, not score coefficients, and finite positive mass is possible only because nonzero mixed-prime moments are retained. Thus this is not a Fisher-information repair of `WP-022`.
- `WP-005` remains untouched: even a positive finite coefficient carrier does not imply positivity after the exact Weil autocorrelation lift. The present result concerns the earlier multiplicative-Gram layer classified by `WP-096`.
- `WP-039` concerns conditionally negative Markov/Dirichlet symbols and their subgroup zero sets. The measures here are ordinary positive-definite Gram carriers, not Markov generator symbols.
- `WP-051` shows a different phenomenon: canonical positive Schatten energies of the Prime-Circle Hardy remainder have unwanted full composite shell support. Equation (7) likewise produces mixed-prime support, but here that support is quantitatively necessary for positivity rather than merely an unwanted readout.

The surrounding harmonic-analysis technology is classical. The infinite prime torus/Dirichlet-series character realization is already anchored in `SOURCES.md` by Hedenmalm--Lindqvist--Seip. Product probability measures and Riesz-product constructions on compact abelian groups are standard; the novelty audit found classical Riesz-product literature extending such constructions to general compact abelian groups. No theorem-level novelty is claimed for (5) as a measure construction.

The project-specific content is instead the exact boundary forced by the Mathia cover-positive normal form:

\[
\boxed{
\text{sparse ray support: }C=\infty
\quad\longrightarrow\quad
\text{allow structural mixed-prime support: }C\ge C_*<\infty.
}
\tag{25}
\]

## Consequence for the research line

`WP-096` showed that arbitrary nonlocality was not enough if the desired finite-Weil comb was demanded as the entire prime-torus Fourier support. `WP-097` shows that **cross-prime coupling really can pay the positivity debt**: ordinary exact-cover positivity is compatible with every critical one-prime Weil coefficient at once and with finite diagonal mass.

That is a genuine reopening, but a tightly constrained one. The missing object can no longer be sought as a positive kernel whose mixed-prime coefficients simply vanish. It must instead explain, from Mathia-native geometry,

1. why a specific positive cross-prime coupling is canonical rather than hand-picked;
2. how its mixed-prime stabilizers are converted or eliminated by a positivity-preserving geometric operation rather than Fourier deletion;
3. why the resulting readout retains the one-prime Mangoldt coefficients;
4. how the same geometry forces the archimedean Gamma and polar terms; and
5. why the mechanism fails under generalized-prime/free-generator controls.

The elementary product completion (5) satisfies none of those global requirements. Its role is therefore not a candidate solution but a **decisive boundary result**: the mixed-prime escape from `WP-096` is mathematically real, finite, and sharp, yet the most obvious extraction back to the sparse Weil comb destroys exactly the interactions that made positivity possible.
