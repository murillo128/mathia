# PC-336 — endpoint Mellin distributions are exactly generalized von Mangoldt jets

**Status:** `EXACT-DERIVED` + `LITERATURE` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the point-supported singular/distributional Mellin continuation left open by PC-335.

PC-179 identifies the signed cyclotomic radial flux Mellin transform

\[
\mathcal R_n(s)
=-\Gamma(s)\zeta(s)n^{1-s}
\prod_{p\mid n}(1-p^{s-1}).
\tag{1}
\]

PC-335 rules out every bounded shell-independent Mellin multiplier followed by the corresponding bounded Hermitian quadratic readout as a way to preserve the exact semiprime null while retaining prime-power signal, but deliberately leaves singular/distributional Mellin symbols open. The most intrinsic such escape is concentration at the distinguished endpoint `s=1`, because point evaluation there gives the exact common-vertex selector `\mathcal R_n(1)=\Lambda(n)`.

That entire point-supported distributional class can be classified exactly: **every finite-order distribution supported at `s=1` sees only the classical generalized von Mangoldt hierarchy.** No new zeta-zero carrier, functional-equation symmetry, or critical-line condition appears.

## 1. The endpoint Taylor jet is triangularly equivalent to generalized von Mangoldt data

Put

\[
z=s-1,
\qquad
A_n(z):=n^{-z}\prod_{p\mid n}(1-p^z).
\tag{2}
\]

Expanding the finite Euler product by divisors gives

\[
A_n(z)
=\sum_{d\mid n}\mu(n/d)d^{-z}.
\tag{3}
\]

For `k>=1`, define the standard generalized von Mangoldt functions

\[
\Lambda_k(n)
:=\sum_{e\mid n}\mu(e)
\left(\log\frac ne\right)^k
=\sum_{d\mid n}\mu(n/d)(\log d)^k.
\tag{4}
\]

Thus, for `n>1`,

\[
\boxed{
A_n(z)
=\sum_{k\ge1}\frac{(-1)^k}{k!}\Lambda_k(n)z^k.
}
\tag{5}
\]

Now isolate the removable zeta pole by setting

\[
G(z):=z\,\Gamma(1+z)\zeta(1+z).
\tag{6}
\]

`G` is analytic near zero and satisfies

\[
G(0)=1,
\qquad
G'(0)=0,
\tag{7}
\]

because the linear terms from `Gamma(1+z)` and `z zeta(1+z)` cancel. Equation (1) becomes

\[
\mathcal R_n(1+z)
=-\frac{G(z)}z A_n(z)
=G(z)\sum_{k\ge1}
(-1)^{k+1}\frac{\Lambda_k(n)}{k!}z^{k-1}.
\tag{8}
\]

Write `G(z)=sum_{m>=0} g_m z^m`, with `g_0=1`. Comparing coefficients gives, for every `j>=0`,

\[
\boxed{
\mathcal R_n^{(j)}(1)
=j!\sum_{k=1}^{j+1}
(-1)^{k+1}\frac{g_{j-k+1}}{k!}\Lambda_k(n).
}
\tag{9}
\]

The coefficient of the newest arithmetic function is always nonzero:

\[
\boxed{
\mathcal R_n^{(j)}(1)
=\frac{(-1)^j}{j+1}\Lambda_{j+1}(n)
+\text{a universal linear combination of }
\Lambda_1(n),\ldots,\Lambda_j(n).
}
\tag{10}
\]

Consequently, for every finite `K`, the endpoint jet

\[
\bigl(\mathcal R_n(1),\mathcal R_n'(1),\ldots,
\mathcal R_n^{(K)}(1)\bigr)
\tag{11}
\]

is related by an invertible universal lower-triangular transformation to

\[
\boxed{
\bigl(\Lambda_1(n),\Lambda_2(n),\ldots,
\Lambda_{K+1}(n)\bigr).
}
\tag{12}
\]

Thus no finite endpoint jet contains arithmetic information beyond the generalized von Mangoldt hierarchy.

## 2. Vanishing order records only the number of distinct prime factors

Let `r=omega(n)`. From (2), each distinct prime contributes exactly one simple zero at `z=0`, so

\[
\operatorname{ord}_{z=0} A_n(z)=r.
\tag{13}
\]

Equivalently,

\[
\Lambda_k(n)=0\quad(k<r),
\qquad
\boxed{
\Lambda_r(n)=r!\prod_{p\mid n}\log p.
}
\tag{14}
\]

Because (8) divides by exactly one power of `z` and `G(0)=1`,

\[
\boxed{
\operatorname{ord}_{s=1}\mathcal R_n(s)=\omega(n)-1.
}
\tag{15}
\]

Hence

\[
\mathcal R_n^{(j)}(1)=0
\qquad(j<\omega(n)-1),
\tag{16}
\]

and the first nonzero derivative is

\[
\boxed{
\mathcal R_n^{(\omega(n)-1)}(1)
=(-1)^{\omega(n)-1}(\omega(n)-1)!
\prod_{p\mid n}\log p.
}
\tag{17}
\]

The first cases are exact controls:

\[
\mathcal R_{p^a}(1)=\log p,
\qquad
\mathcal R_n'(1)=-\log p\log q
\quad(\omega(n)=2),
\tag{18}
\]

and

\[
\mathcal R_n''(1)=2\log p\log q\log r
\quad(\omega(n)=3).
\tag{19}
\]

So higher endpoint derivatives do recover successive almost-prime strata, but they do so in exactly the classical generalized-von-Mangoldt manner.

## 3. Every point-supported distribution is exhausted by the same hierarchy

A standard structure theorem for distributions states that any distribution `T` on the Mellin-frequency line supported only at `t=0` has finite order and can be written

\[
T=\sum_{j=0}^{K}a_j\,\delta_0^{(j)}.
\tag{20}
\]

Apply it to

\[
f_n(t):=\mathcal R_n(1+it).
\tag{21}
\]

Since

\[
f_n^{(j)}(0)=i^j\mathcal R_n^{(j)}(1),
\tag{22}
\]

one obtains

\[
\boxed{
\langle T,f_n\rangle
=\sum_{j=0}^{K}a_j(-i)^j
\mathcal R_n^{(j)}(1).
}
\tag{23}
\]

By (9)--(12), every such readout is therefore a finite linear functional of

\[
\Lambda_1(n),\ldots,\Lambda_{K+1}(n),
\tag{24}
\]

and conversely every finite generalized-von-Mangoldt jet can be recovered from endpoint derivatives by the invertible triangular transformation. This is a complete classification of the point-supported singular symbols, not merely a statement about delta evaluation itself.

## 4. The bounded-to-singular transition is visible quantitatively

For a nonnegative compactly supported approximate identity `phi` with integral one, define

\[
h_\varepsilon(t)=\varepsilon^{-1}\phi(t/\varepsilon),
\qquad
Q_\varepsilon(n)
:=\int_{\mathbb R}h_\varepsilon(t)
|\mathcal R_n(1+it)|^2dt.
\tag{25}
\]

If `r=omega(n)`, (17) gives locally uniformly on bounded `u`

\[
\mathcal R_n(1+i\varepsilon u)
=(-1)^{r-1}(i\varepsilon u)^{r-1}
\prod_{p\mid n}\log p+O(\varepsilon^r).
\tag{26}
\]

Therefore

\[
\boxed{
Q_\varepsilon(n)
=
\left(\prod_{p\mid n}\log p\right)^2
\varepsilon^{2r-2}
\int \phi(u)u^{2r-2}du
+O(\varepsilon^{2r-1}).
}
\tag{27}
\]

In particular, any fixed `epsilon>0` produces nonzero semiprime leakage of order `epsilon^2`; three-prime leakage is of order `epsilon^4`, and so on. Exact Mangoldt support is recovered only in the singular point-evaluation limit, where `||h_epsilon||_infty` diverges like `1/epsilon`. This matches rather than evades the bounded-multiplier obstruction of PC-335.

## 5. Prior-art and novelty audit

The arithmetic functions in (4) are classical generalized von Mangoldt functions. Their support on integers with at most `k` distinct prime factors is standard sieve-theoretic material, and RH formulations using their summatory/twisted behavior already exist. In particular, William D. Banks and Saloni Sinha, *The Riemann Hypothesis via the generalized von Mangoldt function*, Functiones et Approximatio Commentarii Mathematici **72** (2025), DOI `10.7169/facm/240713-22-7`, study RH-equivalent estimates built from these functions. Thus the appearance of `Lambda_k`, their almost-prime support, and their connection to RH are **not** novelty claims here.

Likewise, (20) is the classical Schwartz structure theorem for distributions supported at a point.

The line-local contribution is narrower: equations (8)--(24) identify the **entire endpoint-supported distributional Mellin sector of the prime-circle signed radial flux** with this pre-existing arithmetic hierarchy by an exact invertible triangular map. This is useful as a no-go boundary, not as a new RH criterion.

The result also survives the main nearby prior-art hazards from the prime-circle mandate. It is not a hidden recovery of `-zeta'/zeta`, not an arbitrary spectral wrapper, and not a new Farey/Bost--Connes or Ramanujan mechanism; after the exact cyclotomic Mellin factorization, the endpoint singularity produces only classical generalized von Mangoldt data.

## 6. Implication and boundary of the no-go

The natural singular escape left by PC-335 is therefore closed:

\[
\boxed{
\text{Mellin distribution supported at }s=1
\Longrightarrow
\text{finite generalized-von-Mangoldt jet only}.
}
\tag{28}
\]

Delta evaluation gives ordinary `Lambda`; delta derivatives give the higher `Lambda_k` hierarchy up to the universal triangular mixing in (9). Merely increasing the order of an endpoint singularity cannot produce an independent zeta-zero spectrum, the completed-zeta gamma symmetry, `s <-> 1-s`, or a critical-line selection mechanism.

This does **not** rule out singular or unbounded Mellin symbols whose support is not concentrated at the endpoint, shell-dependent distributional order, non-scalar refinement cocycles, nonlinear radial operations, or genuine cross-shell mixing before the final readout. Those remain outside the theorem.

## Verification

The derivation uses only the exact factorization (1), a finite divisor expansion, Taylor coefficients at the removable pole, and the standard point-support theorem for distributions. Direct symbolic checks for `n=4,6,12,30` reproduce the predicted vanishing order `omega(n)-1` and the leading coefficient in (17); these checks are confirmatory only and are not load-bearing evidence.

## Provenance

- **Inputs:** PC-179 exact signed radial-flux Mellin transform; PC-335 bounded indefinite radial no-go and its explicitly open point-supported singular channel; canonical prime-circle mandate.
- **Evidence:** exact derivation plus classical distribution theory and generalized-von-Mangoldt prior art.
- **Scope:** original prime-circle radial/cyclotomic geometry only; no hyperbolic prime-flute structure is used.
