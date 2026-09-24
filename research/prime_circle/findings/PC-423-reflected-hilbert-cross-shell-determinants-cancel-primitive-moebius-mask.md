# PC-423 — reflected Hilbert cross-shell determinants cancel the primitive Möbius mask

- **Finding ID:** `PC-423`
- **Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE`
- **Research line:** `prime_circle`
- **Result type:** exact cross-shell Hilbert-commutator / incidence factorization
- **Scope:** closes the finite reflected bilinear matrix/determinant repair left open by PC-422 on divisor-closed shell families

## Claim

PC-422 left open a natural matrix-valued repair: instead of taking the reflected Hilbert-commutator pairing shell by shell, retain the full cross-shell matrix

\[
P_{m,n}(\sigma)
:=
\operatorname{Tr}\!\left(C_{m,\sigma}C_{n,1-\sigma}\right),
\qquad 0<\sigma<1,
\]

where

\[
h_{n,\sigma}(u)=e^{\sigma u}\rho_n(e^u),
\qquad
C_{n,\sigma}=[H,M_{h_{n,\sigma}}],
\]

and `rho_n` is the signed radial cyclotomic flux of PC-179.

This matrix does couple distinct primitive shells before taking a scalar determinant. Nevertheless its shell dependence factors exactly through the ordinary divisor Möbius incidence matrix. If `S` is any finite shell set and `D(S)` is the set of all nontrivial divisors of shells in `S`, then

\[
\boxed{
P_S(\sigma)=M_{S,D}\,K_D(\sigma)\,M_{S,D}^{\mathsf T},
}
\tag{1}
\]

where `M_{S,D}(n,d)=mu(n/d) 1_{d|n}` and `K_D` is a universal reflected Mellin kernel on the divisor labels. In particular, if the finite family itself is nontrivial-divisor-closed, so `S=D`, then `M_D` is unit lower triangular and

\[
\boxed{
\det P_D(\sigma)=\det K_D(\sigma).
}
\tag{2}
\]

Thus the determinant removes the primitive-shell Möbius birth mask exactly. At the half-density line, `K_D(1/2)` is a strictly positive Gram matrix, hence every such finite determinant is strictly positive even though the scalar weight contains the Riemann zeros. A zero-free matched control obtained by deleting the common `zeta` factor has the same incidence factorization, reflection symmetry, full rank and half-line positivity.

The conclusion is a negative one: **finite reflected bilinear cross-shell Hilbert matrices do not turn the PC-421/PC-422 scalar Mellin repackaging into a new RH spectral mechanism.** They retain a genuine matrix of divisor frequencies, but primitive-shell extraction is only an invertible incidence-basis change on divisor-closed families, and the `zeta` factor enters only as a common scalar spectral weight.

This does not classify higher noncommutative operator words before trace, shell-dependent kernels/domains, angular--radial couplings, or infinite-dimensional limits in which an entire family of moments reconstructs a scalar measure.

## 1. Exact cross-shell reflected polarization

PC-179 gives, for every `n>1`,

\[
\rho_n(x)
=-\sum_{k\ge1}c_n(k)e^{-kx}
=-\sum_{d\mid n}\mu(n/d)\frac{d}{e^{dx}-1},
\]

with Mellin transform

\[
\mathcal R_n(s)
:=
\int_0^\infty \rho_n(x)x^{s-1}\,dx
=
-\Gamma(s)\zeta(s)A_n(s),
\qquad \Re s>0,
\tag{3}
\]

where

\[
\boxed{
A_n(s)
=
\sum_{d\mid n}\mu(n/d)d^{1-s}
=
n^{1-s}\prod_{p\mid n}(1-p^{s-1}).
}
\tag{4}
\]

For `0<sigma<1`, both `C_{m,sigma}` and `C_{n,1-sigma}` are Hilbert--Schmidt by PC-421, so their product is trace class. Fourier polarization of the Hilbert commutator, with the same normalization as PC-422, gives

\[
\boxed{
P_{m,n}(\sigma)
=
\frac1{\pi^2}
\int_{\mathbb R}
|t|\,
\mathcal R_m(\sigma+it)
\mathcal R_n(1-\sigma-it)
\,dt.
}
\tag{5}
\]

Put

\[
s=\sigma+it,
\qquad
Z(s)=\Gamma(s)\zeta(s).
\]

Then (3) turns (5) into

\[
P_{m,n}(\sigma)
=
\frac1{\pi^2}
\int_{\mathbb R}
|t|\,Z(s)Z(1-s)
A_m(s)A_n(1-s)
\,dt.
\tag{6}
\]

The matrix construction therefore has only one place where new shell interaction could enter: the finite factors `A_n`.

## 2. The primitive factors are an exact Möbius incidence basis change

For every `n>1`,

\[
\sum_{d\mid n}\mu(n/d)=0.
\]

Define, for `d>1`,

\[
\boxed{
\psi_d(s):=d^{1-s}-1.
}
\tag{7}
\]

Subtracting the vanishing constant from (4) gives the exact identity

\[
\boxed{
A_n(s)
=
\sum_{\substack{d\mid n\\d>1}}
\mu(n/d)\psi_d(s).
}
\tag{8}
\]

Now let `S` be any finite set of shell indices greater than one and let

\[
D(S)=\{d>1:\ d\mid n\text{ for some }n\in S\}.
\]

Define the rectangular incidence matrix

\[
M_{S,D}(n,d)
=
\mu(n/d)\mathbf 1_{d\mid n}.
\tag{9}
\]

On the divisor labels define

\[
\boxed{
K_{d,e}(\sigma)
:=
\frac1{\pi^2}
\int_{\mathbb R}
|t|\,Z(s)Z(1-s)
\psi_d(s)\psi_e(1-s)
\,dt.
}
\tag{10}
\]

Substituting (8) twice in (6) and interchanging only finite sums with the convergent Hilbert--Schmidt polarization proves (1):

\[
\boxed{
P_S(\sigma)=M_{S,D}K_D(\sigma)M_{S,D}^{\mathsf T}.
}
\tag{11}
\]

There is no hidden shell-dependent analytic kernel in (11). All analytic/operator information is in `K_D`; all primitive-shell extraction is in the finite Möbius incidence matrix.

For an arbitrary shell subset `S`, (11) says the reflected shell matrix is a finite incidence compression of the divisor kernel. For a nontrivial-divisor-closed set `D` -- meaning that `n in D` and `d|n`, `d>1`, imply `d in D` -- order the elements increasingly. Then

\[
M_D(n,d)=0\quad(d>n),
\qquad
M_D(n,n)=1,
\]

so `M_D` is unit lower triangular:

\[
\boxed{\det M_D=1.}
\tag{12}
\]

Taking determinants in (11) proves (2) exactly:

\[
\boxed{
\det P_D(\sigma)
=(\det M_D)^2\det K_D(\sigma)
=
\det K_D(\sigma).
}
\tag{13}
\]

A minimal check is `D={2,4}`:

\[
M_D=
\begin{pmatrix}
1&0\\
-1&1
\end{pmatrix},
\qquad
\det M_D=1.
\]

Thus even the first repeated-prime birth refinement changes the reflected matrix by congruence without changing its determinant.

This is related in spirit to the fixed divisor-Haar classification of PC-058, but it is not the same kernel. PC-058 concerns finite-radius Dirichlet Grams of `gcd(m,n)F(lcm(m,n))`; here the entries are continuous-scale Hilbert-commutator polarizations with the complementary Mellin weights `s` and `1-s`. The common mechanism is the same exact cyclotomic Möbius extraction acting as an incidence transform.

## 3. Reflection symmetry is matrix transposition, not a zeta functional equation

Cyclicity of the trace gives

\[
\operatorname{Tr}(C_{m,\sigma}C_{n,1-\sigma})
=
\operatorname{Tr}(C_{n,1-\sigma}C_{m,\sigma}).
\]

Therefore

\[
\boxed{
P_D(1-\sigma)=P_D(\sigma)^{\mathsf T},
}
\tag{14}
\]

and hence

\[
\boxed{
\det P_D(1-\sigma)=\det P_D(\sigma).
}
\tag{15}
\]

The same statement follows directly from (10) after `t -> -t` and swapping `d,e`. No Riemann functional equation is used. The involution is already forced by pairing complementary Mellin weights, exactly as the scalar Mellin-Parseval boundary in PC-422 predicts.

Equation (15) is therefore not evidence that the determinant has discovered the completed-zeta functional equation. It is a generic transpose symmetry of the reflected bilinear construction.

## 4. At one half the full cross-shell matrix is strictly positive definite

Set `sigma=1/2`. Then

\[
s=\frac12+it,
\qquad
1-s=\overline{s},
\]

and, because `Gamma`, `zeta` and `psi_d` have the required real conjugation symmetry,

\[
\boxed{
K_{d,e}(1/2)
=
\frac1{\pi^2}
\int_{\mathbb R}
|t|\,
|\Gamma(\tfrac12+it)\zeta(\tfrac12+it)|^2
\psi_d(\tfrac12+it)
\overline{\psi_e(\tfrac12+it)}
\,dt.
}
\tag{16}
\]

Thus `K_D(1/2)` is a Gram matrix in the positive measure

\[
d\nu(t)
=
\pi^{-2}|t|\,
|\Gamma(\tfrac12+it)\zeta(\tfrac12+it)|^2dt.
\]

It is not merely semidefinite. For distinct `d>1`,

\[
\psi_d(\tfrac12+it)
=
\sqrt d\,e^{-it\log d}-1.
\tag{17}
\]

Suppose a finite linear combination vanishes `nu`-almost everywhere. Since the weight is positive almost everywhere -- `Gamma` has no zeros and the zeros of `zeta` on a vertical line are discrete -- continuity makes the exponential polynomial vanish on all real `t`:

\[
\sum_{d\in D}a_d\sqrt d\,e^{-it\log d}
-
\sum_{d\in D}a_d
=0.
\tag{18}
\]

The frequencies `0` and `log d` are distinct, so finite exponential-polynomial uniqueness forces every `a_d=0`. Hence

\[
\boxed{
K_D(1/2)>0.
}
\tag{19}
\]

Since `M_D` is invertible,

\[
\boxed{
P_D(1/2)>0,
\qquad
\det P_D(1/2)>0
}
\tag{20}
\]

for every finite nontrivial-divisor-closed `D`.

This is an important matched stress test. The Riemann zeros on the line appear only as isolated zeros of the scalar density in (16); they have measure zero and cannot create a null vector in any finite Gram matrix. In particular, neither singularity nor determinant vanishing at `sigma=1/2` can encode RH in this construction.

## 5. Removing zeta leaves the matrix mechanism intact

To test whether the matrix structure itself is zeta-specific, define the smooth divisor-control profiles

\[
\boxed{
q_n(x)
:=
\sum_{d\mid n}\mu(n/d)d\,e^{-dx}.
}
\tag{21}
\]

Their Mellin transforms are elementary:

\[
\mathcal Q_n(s)
=
\int_0^\infty q_n(x)x^{s-1}\,dx
=
\Gamma(s)
\sum_{d\mid n}\mu(n/d)d^{1-s}
=
\boxed{\Gamma(s)A_n(s)}.
\tag{22}
\]

Thus this control preserves exactly the finite shell factor `A_n(s)` and deletes only the universal `zeta(s)` multiplier supplied by the Bose/Lambert tail of the cyclotomic flux.

Apply the same log-radius weighting and Hilbert-commutator construction to `q_n`. The derivation of (11)--(15) is unchanged, with

\[
Z_0(s)=\Gamma(s)
\]

in place of `Z(s)=Gamma(s)zeta(s)`. At the half line the kernel is the strictly positive Gram matrix

\[
K^{(0)}_{d,e}(1/2)
=
\frac1{\pi^2}
\int_{\mathbb R}
|t|\,|\Gamma(\tfrac12+it)|^2
\psi_d(\tfrac12+it)
\overline{\psi_e(\tfrac12+it)}dt,
\tag{23}
\]

and the same exponential-polynomial argument gives

\[
\boxed{
K_D^{(0)}(1/2)>0,
\qquad
P_D^{(0)}(1/2)>0.
}
\tag{24}
\]

The control therefore reproduces all of the structural features under test:

- exact Möbius-incidence congruence;
- determinant cancellation of the primitive mask on divisor-closed families;
- `sigma <-> 1-sigma` transpose/determinant symmetry;
- strict full rank and positivity at `sigma=1/2`.

What it does not reproduce is the scalar multiplier `|zeta(1/2+it)|^2` inside the continuous Gram density. Hence the finite matrix construction has not converted the zeta zero set into a new spectral condition; it has only reweighted a classical continuous Gram measure.

## 6. Prior-art and novelty audit

The analytic ingredients lie on established ground.

- The complementary Mellin pairing with arguments `s` and `1-s` is the classical Mellin Parseval formula; NIST DLMF §1.14(iv), Eq. 1.14.36, records the standard identity: <https://dlmf.nist.gov/1.14.E36>. PC-422 already used this as the direct prior-art control for the reflected scalar construction.
- Hilbert-transform commutators and their Schatten/Hankel realizations are classical. Janson and Wolff, **Schatten classes and commutators of singular integral operators**, *Arkiv för Matematik* 20 (1982), 301--310, DOI `10.1007/BF02390515`, and V. V. Peller, **Vectorial Hankel operators, commutators and related operators of the Schatten-von Neumann class**, *Integral Equations and Operator Theory* 5 (1982), 244--272, DOI `10.1007/BF01694041`, cover the surrounding operator-theoretic framework.
- The matrix `M_D` is the ordinary Möbius element of the incidence algebra of the divisibility poset. Its unitriangularity and inverse divisor-zeta matrix are classical Möbius inversion, not a new spectral phenomenon.
- PC-058 already shows a different Prime-Circle radial Gram family becoming rigid after the same divisor Möbius extraction. That earlier theorem is a strong internal control against interpreting an incidence-basis change as new arithmetic dynamics.

A directed novelty audit therefore finds the transform, commutator and incidence machinery on the classical side. No novelty is claimed for those ingredients. The line-local contribution is the exact factorization (11), determinant identity (13), and half-line full-rank test (20) for the specific reflected continuous-scale Prime-Circle commutators left open by PC-422.

The result is deliberately a boundary theorem, not a claim that all matrix-valued Prime-Circle spectralizations collapse. The decisive point is narrower: **the most direct finite cross-shell matrix repair of PC-422 is only an incidence congruence of a universal Mellin kernel, and even its determinant removes the primitive Möbius mask.**

## 7. Falsification audit and surviving boundary

The load-bearing statements have independent checks.

- **Mellin factorization:** equation (3) is PC-179 and can be checked by termwise Mellin integration in `Re(s)>1`, then continuation to `Re(s)>0`.
- **Incidence factorization:** equation (11) follows from the finite identity (8); no infinite rearrangement is involved.
- **Determinant cancellation:** equation (13) requires the explicitly stated divisor-closed hypothesis. It is not claimed for arbitrary nonclosed shell subsets.
- **Reflection:** equation (14) follows from trace cyclicity independently of the Mellin formula.
- **Half-line definiteness:** equation (19) reduces to uniqueness of a finite exponential polynomial with distinct frequencies; isolated zeta zeros cannot remove positive measure.
- **Matched control:** equation (22) is a direct Gamma integral and reproduces the same finite shell factor without any zeta zero set.

A falsification of the negative classification would require a finite reflected bilinear matrix invariant that is not determined by the congruence (11), or a geometric reason that the common scalar zeta weight in (10) becomes a zero-confining operator condition rather than an absolutely continuous Gram density. Neither occurs here.

What remains open is structurally different. A serious continuation must introduce information **before** this bilinear trace/Mellin scalarization: higher noncommuting operator words, shell-dependent kernels or domains, angular/chord variables coupled nonseparably to radial scale, old/new geometry that is not an incidence basis change, or an infinite-dimensional construction with a source-forced topology and a matched control showing that its new property is not merely reconstruction of the same scalar Mellin measure.
