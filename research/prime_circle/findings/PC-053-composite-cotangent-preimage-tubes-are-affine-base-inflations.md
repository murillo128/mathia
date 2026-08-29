# PC-053 — composite cotangent preimage tubes are affine base inflations

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the canonical **complete multi-level preimage-tube cotangent spectrum**. PC-051 and PC-052 classify one prime refinement. The present result removes the primality restriction completely: for every refinement multiplier `m`, the full `m`-fold power-map preimage of a primitive shell is fiber-circulant, and its intrinsic cotangent operator splits into `m` explicit affine copies of one base operator. When `(d,m)=1`, this preimage is exactly the simultaneous divisor-family union `\bigsqcup_{e\mid m}P_{de}^*`, so keeping all those birth shells and all pairwise cotangent couplings at once still creates no new scale spectrum.

The resulting determinant admits a gamma-quotient notation, but the quotient is exactly a finite polynomial coming from an arithmetic progression of eigenvalue shifts. Thus this route does not produce an intrinsic Riemann gamma completion or critical-line mechanism. The result does **not** cover Lewis–Zagier-type weighted Gram/dilation spaces, arbitrary incomplete selections of levels, nonlinear mixing after fiber Fourier decomposition, shell-dependent kernels, or the global uniformization/monodromy direction of PC-017.

## 1. The complete power-map preimage tube

Let `d>1` and `m>=1`. Write

\[
P_d^*=\{z\in\mathbb C:\operatorname{ord}(z)=d\}.
\]

Consider the complete preimage of the primitive shell under the intrinsic power map

\[
\pi_m:S^1\to S^1,
\qquad z\mapsto z^m,
\]

namely

\[
\boxed{
Y_{d,m}:=\pi_m^{-1}(P_d^*).
}
\]

Every primitive `d`-th root has exactly `m` preimages on the circle, so

\[
|Y_{d,m}|=m\varphi(d).
\]

Using `\zeta_{dm}=e^{2\pi i/(dm)}`, choose `a\in U(d)` and `t\in\mathbb Z/m\mathbb Z`. Then

\[
\boxed{
Y_{d,m}
=
\left\{
\zeta_{dm}^{a+dt}:
 a\in U(d),\ t\in\mathbb Z/m\mathbb Z
\right\}.
}
\]

This coordinate system is canonical up to the usual choice of exponent representatives: `a` records the primitive target point and `t` records the lift inside its power-map fiber.

There is also an exact birth-shell description. If `z` has order `q`, then

\[
\operatorname{ord}(z^m)=\frac{q}{\gcd(q,m)}.
\]

Therefore

\[
\boxed{
Y_{d,m}
=
\bigsqcup_{\substack{q\mid dm\\q/\gcd(q,m)=d}}
P_q^*.
}
\]

In the particularly important coprime-refinement case `(d,m)=1`, this simplifies to

\[
\boxed{
Y_{d,m}
=
\bigsqcup_{e\mid m}P_{de}^*.
}
\]

Thus if `m` is squarefree with several prime factors, the complete preimage tube is exactly the entire divisor cube of birth shells above `P_d^*`, not merely one adjacent pair. For `m=p`, this reduces to the two-shell union in PC-052 when `p\nmid d`; when the refinement prime is already present, the general order criterion recovers the repeated-prime situation of PC-051.

## 2. The full multi-shell cotangent operator is fiber-circulant for every `m`

Use the canonical oriented cotangent kernel on the `dm`-gon,

\[
H_{dm}^{\rm full}(x,y)=
\begin{cases}
i\cot\!\left(\dfrac{\pi(x-y)}{dm}\right),&x\ne y,\\[2mm]
0,&x=y.
\end{cases}
\]

Restrict it to the complete preimage tube:

\[
\boxed{
C_{d,m}:=H_{dm}^{\rm full}[Y_{d,m},Y_{d,m}].
}
\]

In lift coordinates `(a,t)` and `(b,u)`, with `a,b\in U(d)` and `t,u\in\mathbb Z/m\mathbb Z`, one has

\[
C_{d,m}((a,t),(b,u))
=
i\cot\!\left(
\frac{\pi((a-b)+d(t-u))}{dm}
\right)
\]

away from the identical fine vertex, where the diagonal is zero. The fiber variables occur only through `t-u`. Hence simultaneous translation

\[
(t,u)\mapsto(t+r,u+r)
\]

is an exact symmetry for every `r\in\mathbb Z/m\mathbb Z`.

Consequently finite Fourier transform in the fiber coordinate block-diagonalizes the entire multi-shell operator **before any shell is projected away or averaged**. This is the key structural point: passing from one prime step to a composite refinement does not introduce interacting prime directions inside the complete preimage tube. It only enlarges one cyclic lift fiber from size `p` to size `m`.

## 3. Exact fiber Fourier blocks for arbitrary composite refinement

Let

\[
\omega=e^{2\pi i/m}.
\]

For `0\le j<m`, Fourier transform the lift coordinate by `t\mapsto\omega^{jt}`. On the base primitive shell define

\[
H_d:=H_d^{\rm full}[U(d),U(d)],
\qquad
A_d:=H_d+J_d,
\]

where `J_d` is the all-ones matrix on `U(d)`. Also put

\[
D_j(a,a)
=
\exp\!\left(\frac{2\pi ija}{dm}\right),
\qquad D_0=I.
\]

Fix `\delta=a-b`. For `\delta\not\equiv0\pmod d`, set

\[
q=e^{2\pi i\delta/(dm)}.
\]

The `j`-th fiber coefficient is

\[
S_j(\delta)
=
\sum_{r=0}^{m-1}
\omega^{-jr}
 i\cot\!\left(
\frac{\pi(\delta+dr)}{dm}
\right).
\]

For the constant mode, the classical cotangent multiplication formula gives

\[
\boxed{
S_0(\delta)
=m\,i\cot\!\left(\frac{\pi\delta}{d}\right).
}
\]

For `1\le j<m`, use

\[
i\cot\theta=\frac{1+e^{2i\theta}}{1-e^{2i\theta}}
\]

and the elementary root-of-unity resolvent identity

\[
\sum_{r=0}^{m-1}
\frac{\omega^{-jr}}{1-q\omega^r}
=
\frac{m q^j}{1-q^m}.
\]

The constant Fourier term vanishes for `j>0`, so

\[
\boxed{
S_j(\delta)
=
\frac{2m q^j}{1-q^m}
=
mq^j
\left(
1+i\cot\!\frac{\pi\delta}{d}
\right).
}
\]

For `\delta=0`, the singular `r=0` term is removed by the zero diagonal. The finite cotangent-circulant transform is

\[
\boxed{
\sum_{r=1}^{m-1}
\omega^{-jr}i\cot\frac{\pi r}{m}
=
\begin{cases}
0,&j=0,\\
m-2j,&1\le j<m.
\end{cases}
}
\]

Therefore the fiber Fourier blocks are exactly

\[
\boxed{K_0=mH_d}
\]

and, for every `1\le j<m`,

\[
\boxed{
K_j
=
mD_jA_dD_j^{-1}-2jI.
}
\]

No use has been made of primality, squarefreeness, a factorization of `m`, analytic continuation, or asymptotics.

## 4. The complete multi-level spectrum is only an affine inflation of base data

The preceding block decomposition gives immediately

\[
\boxed{
\operatorname{Spec}(C_{d,m})
=
m\operatorname{Spec}(H_d)
\;\sqcup\;
\bigsqcup_{j=1}^{m-1}
\left(m\operatorname{Spec}(A_d)-2j\right).
}
\]

Thus all birth shells contained in `Y_{d,m}`, together with **every intrinsic cotangent coupling between them**, have a joint spectrum determined by only the two base matrices `H_d` and `A_d=H_d+J_d`.

As in PC-051/052, rank-one augmentation closes the formula uniformly. Let

\[
\mathcal A_{d,m}:=C_{d,m}+J_{Y_{d,m}}.
\]

In lift coordinates `J_{Y_{d,m}}=J_d\otimes J_m`, so its fiber Fourier transform contributes only `mJ_d` to the constant mode. Hence

\[
\boxed{
\mathcal A_{d,m}
\cong
\bigoplus_{j=0}^{m-1}
\left(
mD_jA_dD_j^{-1}-2jI
\right).
}
\]

Consequently

\[
\boxed{
\operatorname{Spec}(\mathcal A_{d,m})
=
\bigsqcup_{j=0}^{m-1}
\left(m\operatorname{Spec}(A_d)-2j\right).
}
\]

If `r=\varphi(d)` and

\[
\chi_d(z)=\det(zI-A_d),
\]

then the exact characteristic-polynomial multiplication law is

\[
\boxed{
\det(zI-\mathcal A_{d,m})
=
m^{rm}
\prod_{j=0}^{m-1}
\chi_d\!\left(\frac{z+2j}{m}\right).
}
\]

The unaugmented determinant is likewise

\[
\boxed{
\det(zI-C_{d,m})
=
m^{rm}
\det\!\left(\frac zm I-H_d\right)
\prod_{j=1}^{m-1}
\chi_d\!\left(\frac{z+2j}{m}\right).
}
\]

For `(d,m)=1`, these are determinant identities for the simultaneous operator on the full divisor-shell union `\bigsqcup_{e\mid m}P_{de}^*`. Thus moving from one adjacent prime pair to all levels in a squarefree divisor cube does not create a hidden joint spectral interaction.

## 5. Composite refinement has an exact affine semigroup law

At the level of augmented spectra, one refinement multiplier acts on a base eigenvalue by the finite multiset map

\[
\boxed{
\lambda
\longmapsto
\{m\lambda-2j:0\le j<m\}.
}
\]

If one then refines by `n`, the two steps produce

\[
mn\lambda-2(nj+k),
\qquad
0\le j<m,
\quad
0\le k<n.
\]

The integers `nj+k` run through `0,1,\ldots,mn-1` exactly once. Hence

\[
\boxed{
\mathcal S_n\circ\mathcal S_m
=
\mathcal S_{mn}
=
\mathcal S_m\circ\mathcal S_n
}
\]

as spectral multiset transformations, where

\[
\mathcal S_m(\lambda)=\{m\lambda-2j\}_{j=0}^{m-1}.
\]

Therefore factorizing a composite refinement into prime steps cannot generate ordered-prime holonomy, noncommutative scale curvature, or path dependence in this complete-tube spectrum. The one-prime formulas of PC-051/052 are the generators of a completely explicit multiplicative affine semigroup.

This is stronger than the coarse pushforward path independence of PC-049: no fiber degrees of freedom have been summed away here. The entire complete preimage tube is retained, yet its spectral refinement still composes exactly through a commutative affine law.

## 6. The apparent gamma factor is only finite progression bookkeeping

Because the augmented eigenvalues over one base eigenvalue `\lambda` are

\[
m\lambda,
\ m\lambda-2,
\ \ldots,
\ m\lambda-2(m-1),
\]

its characteristic contribution is

\[
\prod_{j=0}^{m-1}
\left(z-m\lambda+2j\right).
\]

Using only the gamma recurrence `\Gamma(w+m)/\Gamma(w)=\prod_{j=0}^{m-1}(w+j)`, this may be written exactly as

\[
\boxed{
\prod_{j=0}^{m-1}
\left(z-m\lambda+2j\right)
=
2^m
\frac{
\Gamma\!\left(\dfrac{z-m\lambda}{2}+m\right)
}{
\Gamma\!\left(\dfrac{z-m\lambda}{2}\right)
}.
}
\]

Hence

\[
\boxed{
\det(zI-\mathcal A_{d,m})
=
2^{rm}
\prod_{\lambda\in\operatorname{Spec}(A_d)}
\frac{
\Gamma\!\left(\dfrac{z-m\lambda}{2}+m\right)
}{
\Gamma\!\left(\dfrac{z-m\lambda}{2}\right)
},
}
\]

with eigenvalues counted with multiplicity.

This is an important novelty/falsification boundary. A gamma function can indeed appear when the affine refinement ladder is rewritten analytically, but **the gamma quotient is identically a finite polynomial**: every pole cancels and its zeros are exactly the already-known affine copies of the finite base spectrum. It is therefore not an independently generated archimedean completion comparable to the gamma factor in the completed Riemann zeta function.

Introducing a complex change of variables `z=z(s)` after this identity would be an external spectral wrapper. The prime-circle geometry has supplied only the universal arithmetic progression `-2j`; it has not supplied the Riemann functional equation, a Mellin duality `s\leftrightarrow1-s`, or a mechanism selecting `\operatorname{Re}s=1/2`.

## 7. Prior-art and novelty audit

The analytic ingredients are classical.

- The cotangent multiplication/distribution formula and Petersson–Knopp-type scale identities lie in the classical Dedekind-cotangent framework; Matthias Beck, **Dedekind cotangent sums**, *Acta Arithmetica* 109:2 (2003), 109–130, is already anchored in `research/prime_circle/SOURCES.md`.
- Finite Fourier diagonalization of circulant/block-circulant matrices is standard linear algebra.
- Wiktor Ejsmont and Franz Lehner, **The Trace Method for Cotangent Sums**, *Journal of Combinatorial Theory, Series A* 177 (2021), 105324, is a direct prior-art boundary for finite self-adjoint matrix realizations of cotangent spectra and is already recorded in `SOURCES.md`.
- The gamma recurrence and finite arithmetic-progression product are classical special-function identities; the displayed quotient contains no analytic information beyond the finite product.
- John Lewis and Don Zagier, **Cotangent sums, quantum modular forms, and the generalized Riemann hypothesis**, *Research in the Mathematical Sciences* 6 (2019), Article 4, remains the crucial nearby positive boundary. Their GRH criterion uses a genuinely different family of rational-cotangent sums, dilation/Gram determinants, and asymptotic functional analysis rather than the canonical complete power-map preimage tube classified here.

Directed searches around cotangent distribution, cotangent matrix spectra, Petersson–Knopp/Hecke scaling, block-circulant refinements, and cotangent GRH criteria did not locate this exact all-`m` primitive-shell preimage-tube formulation. That absence is not evidence of historical priority, and no novelty claim is made for the Fourier, cotangent, gamma, or determinant ingredients.

The durable prime-circle contribution is the structural obstruction forced by its own birth geometry:

\[
\boxed{
\text{the complete multi-level power-map preimage tube has only affine base cotangent spectrum.}
}
\]

In particular, the extra intermediate shells present for composite `m` do not create a new coupled spectrum when the complete geometrically natural tube is retained.

## 8. Consequence for the RH search

PC-052 left open the possibility that several levels retained simultaneously might escape the one-prime affine collapse. The result above closes the most canonical such extension. For coprime composite refinement,

\[
\boxed{
P_d^*
\longrightarrow
\bigsqcup_{e\mid m}P_{de}^*
\longrightarrow
\text{full intrinsic cotangent operator}
\longrightarrow
\text{joint determinant}
}
\]

produces only an affine semigroup inflation of base-level finite spectra.

Therefore the chain

\[
\boxed{
\text{multi-level divisor birth geometry}
\to
\text{complete cotangent preimage tube}
\to
\text{composite scale spectrum / gamma completion}
\to
\text{new RH mechanism}
}
\]

fails under the stated construction. Neither keeping all intermediate birth shells nor factoring the refinement into different prime orders creates new spectral data. The only gamma expression available from the determinant is a finite progression identity with complete pole cancellation.

The surviving boundary is narrower but nonempty. This result does **not** rule out:

- an **incomplete** or asymmetrically weighted collection of levels that destroys the full cyclic lift fiber for a mathematically intrinsic reason;
- rectangular Gram/dilation spaces coupling several levels with nontrivial weights, as in the broad Lewis–Zagier/Nyman–Beurling neighborhood;
- nonlinear operations that couple different fiber Fourier sectors after the canonical cotangent operator is formed;
- shell-dependent kernels carrying independently derived geometric data rather than the same universal cotangent kernel at every level;
- genuinely two-dimensional global uniformization/monodromy data from PC-017.

The practical restriction is now exact: **simply retaining more divisor-related cotangent shells is not enough.** A surviving multi-scale mechanism must use a scale coupling that is not the complete power-map preimage geometry itself.

## 9. Exact falsification tests

The result is finite-dimensional and has direct audit tests.

1. Verify from `\operatorname{ord}(z^m)=\operatorname{ord}(z)/\gcd(\operatorname{ord}(z),m)` that
   \[
   Y_{d,m}=\bigsqcup_{q/\gcd(q,m)=d}P_q^*,
   \]
   and, when `(d,m)=1`, recover `\bigsqcup_{e\mid m}P_{de}^*`.
2. Order `Y_{d,m}` by `(a,t)` and verify that every cotangent entry depends on the fiber coordinates only through `t-u`.
3. Fourier transform the `m`-fiber and check the root-of-unity resolvent sum for arbitrary composite `m`.
4. Verify the diagonal cotangent transform `0,m-2,m-4,\ldots,2-m`.
5. Recover exactly `K_0=mH_d` and `K_j=mD_j(H_d+J_d)D_j^{-1}-2jI` for every `1\le j<m`.
6. Check the augmented characteristic-polynomial product against direct finite matrices at composite refinements, e.g. `(d,m)=(5,6)` or `(7,4)`.
7. Factor `m=uv` in two different orders and verify that the affine spectral digits compose to `0,\ldots,m-1` exactly once.
8. Expand the gamma quotient with the recurrence relation and verify that all poles cancel and the result is precisely the finite characteristic factor.

Failure of the general fiber Fourier block formula or of the shell description would invalidate the obstruction. No claim is made about incomplete/weighted multi-level families, Lewis–Zagier-type asymptotic Gram determinants, or other operators not equal to the canonical cotangent restriction on the complete power-map preimage tube.