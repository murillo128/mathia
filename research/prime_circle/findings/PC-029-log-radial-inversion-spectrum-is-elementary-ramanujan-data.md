# PC-029 — log-radial inversion spectralization is elementary Ramanujan data, not the zeta functional equation

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the most canonical branch that linearizes the exact interior/exterior inversion in logarithmic radius and then Fourier/Mellin-transforms that radial coordinate in search of the zeta functional equation or critical line.

PC-003 gives an exact spatial inversion of the primitive-shell potential, while the full-field Dirichlet-transform result recorded as PC-015 showed that an ordinary transform in the polygon level leaves the scale variable unchanged and therefore does not implement `s -> 1-s`. That left open a more intrinsic possibility: first linearize the *spatial* inversion itself by using logarithmic radius, remove the forced exterior growth, and only then spectralize the resulting inversion-even field. This finding performs that construction exactly. The reflection exists, but it is purely kinematic and its complete spectrum reduces to Ramanujan/divisor data and elementary cylinder Green kernels.

## 1. The canonical inversion-even radial field

For `n>1`, write

\[
U_n(re^{i\theta})=\log|\Phi_n(re^{i\theta})|.
\]

Cyclotomic reciprocity gives

\[
U_n(re^{i\theta})
=\varphi(n)\log r+U_n(r^{-1}e^{i\theta}).
\]

Put `x=log r`. Inversion is now exactly

\[
x\longmapsto -x.
\]

The exterior field has the forced affine growth `phi(n) x` as `x -> +infinity`. Remove precisely that term and no more:

\[
\boxed{
K_n(x,\theta)
:=U_n(e^{x+i\theta})-\varphi(n)x_+,
\qquad x_+=\max(x,0).
}
\]

The reciprocity law then gives the exact identity

\[
\boxed{
K_n(x,\theta)=U_n(e^{-|x|+i\theta})
=K_n(-x,\theta).
}
\]

Thus this is the minimal renormalized field on the logarithmic cylinder that simultaneously retains the angular variable, the primitive shell, and the interior/exterior involution. It decays exponentially as `|x| -> infinity`; logarithmic singularities at angles occupied by primitive roots are locally integrable.

For `x != 0`, the interior cyclotomic expansion is

\[
\boxed{
K_n(x,\theta)
=-\sum_{k\ge1}\frac{c_n(k)}{k}
 e^{-k|x|}\cos(k\theta),
}
\]

where `c_n(k)` is the Ramanujan sum.

## 2. Exact log-radial Fourier spectrum

Use the inversion-invariant multiplicative measure

\[
dx=\frac{dr}{r}
\]

and Fourier-transform in the coordinate that inversion negates:

\[
\widehat K_n(t,\theta)
:=\int_{-\infty}^{\infty}
K_n(x,\theta)e^{-itx}\,dx.
\]

Since

\[
\int_{-\infty}^{\infty}e^{-k|x|}e^{-itx}\,dx
=\frac{2k}{k^2+t^2},
\]

absolute summability after integration gives

\[
\boxed{
\widehat K_n(t,\theta)
=-2\sum_{k\ge1}
\frac{c_n(k)\cos(k\theta)}{k^2+t^2}.
}
\]

The inversion symmetry is now only the elementary spectral symmetry

\[
\boxed{
\widehat K_n(t,\theta)=\widehat K_n(-t,\theta).
}
\]

No zeta function has appeared.

## 3. The entire angular family resums to a finite divisor expression

Use the classical divisor formula

\[
c_n(k)=\sum_{\substack{d\mid n\\d\mid k}}d\,\mu(n/d).
\]

For `t != 0`, let `vartheta_d` be the representative of `d theta mod 2 pi` in `[0,2 pi]`. The standard cylinder Green-function identity

\[
\sum_{j\ge1}\frac{\cos(jy)}{j^2+a^2}
=
\frac{\pi}{2a}
\frac{\cosh(a(\pi-y))}{\sinh(\pi a)}
-\frac1{2a^2}
\qquad(0\le y\le2\pi)
\]

then yields the exact finite resummation

\[
\boxed{
\widehat K_n(t,\theta)
=
\frac{\varphi(n)}{t^2}
-\frac{\pi}{t}
\sum_{d\mid n}\mu(n/d)
\frac{
\cosh\!\left(\frac{t}{d}(\pi-\vartheta_d)\right)
}{
\sinh(\pi t/d)
}.
}
\]

The apparent singularity at `t=0` is removable, as is already clear from the absolutely convergent integral definition.

At the distinguished common-vertex ray `theta=0`, this becomes especially transparent:

\[
\boxed{
\widehat K_n(t,0)
=
\frac{
\varphi(n)-\pi t\sum_{d\mid n}
\mu(n/d)\coth(\pi t/d)
}{t^2}.
}
\]

So even after retaining the complete nonlocal radial profile rather than a finite anchor jet, the radial spectrum is a **finite Möbius combination of universal hyperbolic/cylinder kernels**. This is not a hidden zeta spectrum.

## 4. Why an apparent `s <-> 1-s` reflection is not the zeta functional equation

The same conclusion is clearest in the bilateral Mellin/Laplace parameter. For the safe strip `|Re(lambda)|<1`, define

\[
\mathcal M_n(\lambda,\theta)
:=\int_{-\infty}^{\infty}
K_n(x,\theta)e^{-\lambda x}\,dx.
\]

Then

\[
\boxed{
\mathcal M_n(\lambda,\theta)
=-2\sum_{k\ge1}
\frac{c_n(k)\cos(k\theta)}{k^2-\lambda^2},
}
\]

and therefore

\[
\boxed{
\mathcal M_n(\lambda,\theta)
=\mathcal M_n(-\lambda,\theta).
}
\]

If one *renames*

\[
\lambda=s-\frac12,
\]

this can of course be written

\[
\mathcal M_n(s-\tfrac12,\theta)
=
\mathcal M_n(\tfrac12-s,\theta).
\]

But the center `1/2` has not been derived. The original geometry selected `x=log r`, the inversion `x -> -x`, the invariant Haar measure `dx=dr/r`, and hence the spectral center `lambda=0`. Any shift `lambda=s-c` would rewrite the same evenness as a reflection about `Re(s)=c`.

In particular, choosing `c=1/2` merely makes the kinematic reflection *look like* the Riemann functional equation. The construction supplies neither

- the completed zeta function,
- its gamma factor,
- a coupling between the radial parameter `lambda` and the polygon-level/Dirichlet scale variable,
- nor a condition that places zeta zeros on the unitary radial spectrum `lambda=it`.

The meromorphic continuation visible in the partial fractions has only the elementary radial-mode singularities `lambda=+/-k` when the corresponding Ramanujan/angular coefficient is nonzero. It does not generate the nontrivial zeros of zeta.

## 5. Relation to earlier no-go results

This closes a branch that PC-015 explicitly left open: a transform that acts on the spatial inversion *and* logarithmic radius before any Dirichlet transform in `n` is introduced.

It is complementary to PC-020 and PC-027:

- PC-020 shows that every **finite local jet** at the anchor is Jordan-totient data;
- PC-027 shows that the canonical **quadratic all-mode Dirichlet energy** is a Möbius basis change;
- the present result shows that the complete **nonlocal radial profile**, spectralized in the coordinate on which inversion acts, is still a finite divisor/Ramanujan package and that its reflection symmetry has no intrinsic critical-line center.

Thus simply retaining infinitely many radial modes does not turn circle inversion into the zeta functional equation.

## 6. Prior art and novelty audit

No novelty is claimed for the ingredients:

- the Ramanujan expansion of the cyclotomic logarithm is classical and is already anchored in `SOURCES.md` through Ramanujan, Hardy, and the modern cyclotomic-product treatment of Bal;
- the divisor formula for `c_n(k)` is classical;
- the partial-fraction/Green-kernel sums producing `coth`, `sinh`, and `cosh` are standard Mittag-Leffler/Fourier identities;
- evenness under Fourier or bilateral Laplace transform is elementary once inversion has become `x -> -x`.

Directed searches did not locate this exact prime-circle packaging, but that is not a priority claim. Its research value is negative: it explicitly evaluates the most natural simultaneous inversion/log-scale transform and shows why the resulting reflection cannot be counted as an explanation of Riemann's functional equation.

## 7. Boundary of the obstruction

The result does **not** rule out every possible use of interior/exterior geometry. It rules out the canonical scalar-potential route

\[
\boxed{
U_n(r,\theta)
\to
\text{minimal inversion-even log-radius renormalization}
\to
\text{Fourier/Mellin spectrum in }\log r
\to
\text{new functional-equation/critical-line mechanism}.
}
\]

A surviving mechanism must derive additional structure that couples the radial spectral variable to arithmetic scale nontrivially, rather than identify them after the fact. Examples still outside this no-go include a genuinely shell-dependent nonlinear two-dimensional operator, the collective uniformization/accessory sector of PC-017 after the PC-028 symmetry restrictions, or another intrinsic construction whose half-density and spectral center are forced together with the prime-scale dynamics.
