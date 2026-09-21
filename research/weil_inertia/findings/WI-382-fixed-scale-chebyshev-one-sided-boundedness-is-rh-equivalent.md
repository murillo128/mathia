# WI-382 — One-sided boundedness of the WI-381 fixed-scale Chebyshev remainder is RH-equivalent

**Status:** `EXACT-DERIVED + CLASSICAL-LANDAU-PINTZ + LITERATURE-BACKED + DECISIVE-ROUTE-REDIRECTION + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-381 reduced the unresolved arithmetic content of the centered source-zero gamma-negative trials to a fixed-log-width smoothed Chebyshev-error functional after exact cancellation of the `\sqrt{x}` critical-prime main term against the polar rank-one debt. For the limiting unperforated profile, that remainder has a sharper property than WI-381 recorded:

> **For the exact cosine-convolution kernel selected by the WI-380/WI-381 trials, eventual boundedness from either one side is equivalent to the Riemann hypothesis.**

Fix `L>0` and put

\[
g(s)=\sqrt{\frac2L}\cos\!\left(\frac{\pi s}{L}\right)
\mathbf 1_{|s|\le L/2},
\qquad
q=g*g.
\tag{1}
\]

Define

\[
Q(z):=\int_{-L}^{L}q(t)e^{zt}\,dt
\tag{2}
\]

and the fixed-profile renormalized prime remainder

\[
\boxed{
R_L(x):=
2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
q\!\left(\log\frac n x\right)
-2Q(1/2)\sqrt x .
}
\tag{3}
\]

Then

\[
\boxed{
\mathrm{RH}
\iff R_L(x)=O_L(1)
\iff R_L(x)\ \text{is eventually bounded below}
\iff R_L(x)\ \text{is eventually bounded above}.
}
\tag{4}
\]

The same equivalence holds if the one-sided boundedness hypothesis is assumed only on the integer lattice `x=k+1`.

Moreover the actual perforated WI-381 arithmetic-plus-polar layer differs from `R_L(k+1)` by only `O_L(1)`. Consequently, any uniform eventual one-sided bound on that renormalized layer already excludes every off-critical zeta zero. Contrapositively, if RH is false, the WI-381 fixed-width critical layer has arbitrarily large excursions of **both signs**, even after the exact source perforations and bounded deterministic terms are restored.

This does **not** prove the Gate-II repair inequality. RH gives boundedness of the remainder, not the positive lower margin needed to pay a prescribed gamma tariff. The result instead identifies the sign-control route as an RH-equivalent defect detector and sharply separates it from the still-distinct graph/domain-exclusion route.

## 1. The limiting kernel has no Mellin zero in the right half-plane

Set

\[
a:=\frac\pi L.
\]

The bilateral Laplace transform of `g` is

\[
G(z):=\int_{-L/2}^{L/2}g(s)e^{zs}\,ds
=
\sqrt{\frac2L}\,
\frac{2a\cosh(zL/2)}{z^2+a^2},
\tag{5}
\]

with removable values at `z=\pm ia`. Since `q=g*g`,

\[
\boxed{Q(z)=G(z)^2.}
\tag{6}
\]

The zeros of `\cosh(zL/2)` are

\[
z=i(2j+1)a,
\qquad j\in\mathbb Z.
\]

The two zeros at `z=\pm ia` cancel the denominator singularities in (5); the removable values there are nonzero. Every remaining zero is purely imaginary. Hence

\[
\boxed{Q(z)\ne0\qquad(\Re z>0).}
\tag{7}
\]

Also, on every bounded vertical strip,

\[
Q(\sigma+it)=O_L\!\left((1+|t|)^{-4}\right),
\tag{8}
\]

because `G` has a quadratic denominator and bounded `\cosh` on such a strip.

The nonvanishing (7) is the load-bearing feature: an off-critical zeta zero cannot be hidden by a zero of the smoothing transform.

## 2. Mellin transform of the renormalized remainder

The support of `q` is `[-L,L]`, so the sum in (3) only uses prime powers in the fixed multiplicative annulus

\[
xe^{-L}\le n\le xe^L.
\]

Chebyshev's estimate `\psi(y)=O(y)` therefore gives the unconditional bound

\[
R_L(x)=O_L(\sqrt x).
\tag{9}
\]

For `\Re s>1/2`, define

\[
\mathcal M_L(s)
:=\int_1^\infty R_L(x)x^{-s}\,\frac{dx}{x}.
\tag{10}
\]

For one prime-power term, integration over `0<x<\infty` and the substitution `t=\log(n/x)` give

\[
\int_0^\infty
q\!\left(\log\frac n x\right)x^{-s}\frac{dx}{x}
=n^{-s}Q(s).
\tag{11}
\]

Thus, initially for `\Re s>1/2`,

\[
2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\int_0^\infty
q\!\left(\log\frac n x\right)x^{-s}\frac{dx}{x}
=
2Q(s)\left(-\frac{\zeta'}{\zeta}(s+1/2)\right).
\tag{12}
\]

Passing from `(0,\infty)` to `[1,\infty)` changes (12) by an entire function: for `x<1`, support of `q` forces `n<e^L`, so only finitely many `n` occur and every resulting integral is over a compact interval bounded away from zero. Therefore

\[
\boxed{
\mathcal M_L(s)=
2Q(s)\left(-\frac{\zeta'}{\zeta}(s+1/2)\right)
-
\frac{2Q(1/2)}{s-1/2}
+H_L(s),
}
\tag{13}
\]

where `H_L` is entire.

At `s=1/2`, the pole of `-\zeta'/\zeta(s+1/2)` coming from the pole of `\zeta` at `1` has residue `+1`, so it is canceled exactly by the second term in (13). At a nontrivial zero `\rho` of multiplicity `m_\rho`, (13) instead has residue

\[
\boxed{
-2m_\rho Q(\rho-1/2)
}
\tag{14}
\]

at `s=\rho-1/2`.

By (7), every zero with `\Re\rho>1/2` therefore creates a genuine nonremovable pole of the continuation of `\mathcal M_L` in `\Re s>0`.

## 3. A one-sided bound forces RH

Assume first that

\[
R_L(x)\ge-C
\tag{15}
\]

for all sufficiently large `x`. Choose `X_0` after which (15) holds and set

\[
h(x):=R_L(x)+C\ge0,
\qquad x\ge X_0.
\]

Its tail Mellin transform

\[
F(s)=\int_{X_0}^{\infty}h(x)x^{-s}\frac{dx}{x}
\tag{16}
\]

has a finite abscissa of convergence `\sigma_c\le1/2` by (9). The continuous Landau principle says that if a nonnegative Mellin/Laplace transform has finite convergence abscissa `\sigma_c`, then its holomorphic sum is singular at the real boundary point `s=\sigma_c`.

For completeness, this instance is elementary. Put `x=e^u`. If `F` were holomorphic through `\sigma_c`, choose real `\sigma_1>\sigma_c` so close that the Taylor disc at `\sigma_1` crosses the boundary. Since

\[
\frac{(-1)^m}{m!}F^{(m)}(\sigma_1)
=
\int_{\log X_0}^{\infty}
\frac{u^m}{m!}h(e^u)e^{-\sigma_1u}\,du
\ge0,
\tag{17}
\]

Tonelli's theorem lets the Taylor series be summed at a real `\sigma_*<\sigma_c` still inside that disc, giving

\[
F(\sigma_*)
=
\int_{\log X_0}^{\infty}h(e^u)e^{-\sigma_*u}\,du<\infty,
\]

contradicting the definition of `\sigma_c`.

On the other hand, (13), subtraction of the finite interval `[1,X_0]`, and addition of the elementary term `CX_0^{-s}/s` give a meromorphic continuation of (16). It is analytic at every **positive real** `s`: the pole at `1/2` is canceled, the trivial zeta zeros map to negative `s`, and `\zeta(\sigma)` has no real zero for `0<\sigma<1` (equivalently, `\zeta(\sigma)=\eta(\sigma)/(1-2^{1-\sigma})<0` there).

Landau's boundary singularity therefore rules out `\sigma_c>0`. Hence

\[
\sigma_c\le0,
\tag{18}
\]

so the integral (16) itself is holomorphic throughout `\Re s>0`.

If `\zeta` had a zero `\rho` with `\Re\rho>1/2`, (14) and (7) would force a pole of that same holomorphic function at `s=\rho-1/2`, contradiction. Thus there are no zeros to the right of the critical line. Functional-equation symmetry then excludes zeros to the left, proving RH.

The upper-bound case is identical: if `R_L(x)\le C` eventually, apply the argument to `C-R_L(x)\ge0`. Therefore

\[
\boxed{
R_L\ \text{eventually bounded on either one side}
\Longrightarrow \mathrm{RH}.
}
\tag{19}
\]

This is the exact Landau--Pintz mechanism specialized to the WI-381 kernel, with (7) preventing smoothing from screening an off-critical pole.

## 4. RH gives two-sided boundedness

Conversely assume RH. Mellin inversion of (12), followed by the standard explicit-formula contour shift, gives

\[
R_L(x)=
-2\sum_\rho
m_\rho Q(\rho-1/2)x^{\rho-1/2}
+B_L(x),
\tag{20}
\]

where `B_L(x)=O_L(1)` contains the bounded contribution of the shifted contour and the trivial zeros. This shift is harmless here because of the fourth-power vertical decay (8).

Under RH, `\rho-1/2=i\gamma`. The classical zero count `N(T)=O(T\log T)` and (8) imply

\[
\sum_\rho m_\rho |Q(i\gamma)|<\infty.
\tag{21}
\]

Hence the zero series in (20) converges absolutely and uniformly in `\log x`, and every factor `x^{i\gamma}` has modulus one. Therefore

\[
\boxed{\mathrm{RH}\Longrightarrow R_L(x)=O_L(1).}
\tag{22}
\]

Together with (19), this proves (4).

## 5. Sampling only at `x=k+1` loses no one-sided information

The equivalence remains true on the exact lattice used by WI-381. The kernel `q` is continuously differentiable with bounded derivative. Differentiating (3) locally term by term gives

\[
R_L'(x)=
-\frac2x
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
q'\!\left(\log\frac n x\right)
-Q(1/2)x^{-1/2}.
\tag{23}
\]

Again by Chebyshev on the fixed annulus,

\[
\boxed{R_L'(x)=O_L(x^{-1/2}).}
\tag{24}
\]

Consequently

\[
\sup_{x\in[k+1,k+2]}
|R_L(x)-R_L(k+1)|
=O_L(k^{-1/2}).
\tag{25}
\]

An eventual lower or upper bound on the integer samples therefore extends to all sufficiently large real `x`, and Section 3 applies. Thus

\[
\boxed{
\mathrm{RH}
\iff \{R_L(k+1)\}\ \text{is eventually bounded below}
\iff \{R_L(k+1)\}\ \text{is eventually bounded above}.
}
\tag{26}
\]

## 6. The source-perforated WI-381 remainder is only an `O(1)` perturbation

The criterion is not an artifact of replacing the admissible source-zero trial by the unperforated cosine. WI-380 gives, in centered coordinates,

\[
p_k=\chi_k g,
\qquad 0\le\chi_k\le1,
\tag{27}
\]

and its source-slot estimate gives total modified measure

\[
\mu_k=O_L(x_k^{-1/2}),
\qquad x_k=k+1.
\tag{28}
\]

Since `g` is bounded and supported on a fixed interval,

\[
\|p_k-g\|_1=O_L(x_k^{-1/2}).
\tag{29}
\]

For `q_k=p_k*p_k`, Young's inequality therefore improves the qualitative convergence used in WI-381 to

\[
\boxed{
\|q_k-q\|_\infty=O_L(x_k^{-1/2}).
}
\tag{30}
\]

The weighted Mangoldt mass in the critical annulus is `O_L(\sqrt{x_k})`, so (30) gives

\[
2\sum_n\frac{\Lambda(n)}{\sqrt n}
\left[
q_k\!\left(\log\frac n{x_k}\right)
-q\!\left(\log\frac n{x_k}\right)
\right]
=O_L(1).
\tag{31}
\]

Likewise, with

\[
I_{k,+}=\int e^{s/2}p_k(s)\,ds,
\qquad
I_+=\int e^{s/2}g(s)\,ds,
\]

(29) implies

\[
I_{k,+}-I_+=O_L(x_k^{-1/2}),
\]

and therefore

\[
\sqrt{x_k}\left(I_{k,+}^2-I_+^2\right)=O_L(1).
\tag{32}
\]

WI-381 already proves that its same-lobe arithmetic term is `O_L(1)` and that the remaining polar cross/error terms after subtraction of `-2\sqrt{x_k}I_{k,+}^2` are bounded. Combining those facts with (31)--(32) yields

\[
\boxed{
Q_k^{\rm arith}+Q_k^{\rm pol}
=R_L(x_k)+O_L(1).
}
\tag{33}
\]

The `O_L(1)` is uniform in `k`.

Thus a uniform eventual lower bound on the actual renormalized arithmetic-polar layer implies an eventual lower bound on `R_L(k+1)` and hence RH; the same holds for an upper bound. Contrapositively,

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\limsup_{k\to\infty}R_L(k+1)=+\infty,
\qquad
\liminf_{k\to\infty}R_L(k+1)=-\infty,
}
\tag{34}
\]

and the same two-sided unboundedness survives the bounded perturbation (33).

Equation (34) is the useful defect characterization: any off-critical zero forces arbitrarily large signed excursions in precisely the critical arithmetic layer that WI-381 left unresolved.

## 7. Consequences for the research line

This closes one ambiguity in the Gate-II frontier. The fixed-scale sign/coercivity question left by WI-381 is not merely beyond the prime number theorem as currently estimated. For the limiting trial it is an **RH-equivalent criterion**: even the qualitatively weak assertion that the renormalized remainder never goes below some finite constant eventually would already rule out every off-critical zero.

That has two consequences.

First, standard refinements of PNT error bounds or zero-free regions cannot be expected to supply the needed uniform one-sided control unless they cross all the way to RH. They may still quantify finite ranges or conditional margins, but there is no intermediate asymptotic one-sided theorem of this form compatible with an off-critical zero.

Second, the same fact makes the remainder a legitimate defect detector rather than only a nuisance term. Under any RH failure, the exact fixed-width trial family sees that failure through unbounded oscillation of both signs. A viable bootstrap could therefore try to relate the **negative excursions** in (34) directly to the rooted-domain or Schur geometry, rather than attempting to dominate them by a crude positive prime-mass estimate.

The alternative live route remains unchanged: prove that the source-zero gamma-negative trials are not in the actual rooted graph/domain before the old--old quadratic form is tested. WI-382 does not compare the difficulty of that domain route with RH.

## 8. Prior-art and novelty audit

- **Classical mechanism:** Landau's boundary-singularity theorem for nonnegative Dirichlet/Laplace transforms and the Landau--Pintz program relating arithmetic remainder terms to zero-free regions are established prior art. J. Pintz, *Distribution of the zeros of the Riemann zeta function and oscillations of the error term in the asymptotic law of the distribution of prime numbers*, Proc. Steklov Inst. Math. 296 (2017), 198--210, is a direct modern reference for the oscillation direction.
- **Closest smooth-weight prior art:** Songlin Han, *The Error in a Smooth Weighted Prime Number Formula and Zero-free Regions for the Riemann Zeta Function*, arXiv:2505.23795 (2025; revised 2026), proves zero-free-region/error-term correspondences for a smooth weighted prime formula using Pintz's method. This materially constrains novelty: the general philosophy "smooth prime error control detects zeta zeros" is not new here.
- **Recent general exposition:** D. R. Johnston and T. Trudgian, *A round of Pintz to celebrate oscillations in sums*, Analysis Mathematica (published 10 Aug 2026), develops the general Landau--Pintz direction from arithmetic information to zero-free regions. Again, that general mechanism is prior art.
- **Primary operator source:** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1 (17 Sep 2026), supplies the localized rooted-operator normalization used by WI-380/WI-381. None of its claimed RH conclusion is used here.
- **Mathia-specific deduction:** the audited sources were not found to state the specialization (4) for the exact WI-381 cosine-convolution kernel, the transform nonvanishing (7), the integer-lattice equivalence (26), or the `O(1)` transfer (33) from the source-perforated rooted trial. These are recorded as derived facts, not as a priority claim.

## 9. Boundaries and falsification

The equivalence depends critically on the fact that `Q(z)` has no zero for `\Re z>0`. For a different smoothing kernel whose Mellin transform vanishes at `\rho-1/2`, an off-critical pole could be screened and the implication in Section 3 would need to be re-audited.

The transfer to the actual WI-381 trial depends on the quantitative source-perforation estimate (28). If the admissible rooted construction modifies a set of larger total measure than WI-380 proves, the `O(1)` comparison (33) need not survive.

Finally, no claim is made that RH supplies the **sign** required for Gate-II repair. Equation (22) gives only boundedness. A bounded almost-periodic zero sum can have either sign, and a fixed positive gamma tariff is not discharged by boundedness alone. Therefore WI-382 is an RH-equivalent defect characterization and route restriction, not a proof of rooted positivity or RH.

The next high-value test is to ask whether the rooted graph/domain identities constrain the negative excursions of (33), or exclude the trial at exactly the moments when those excursions occur. A direct attempt to prove a uniform one-sided lower bound for (33) should now be treated explicitly as an RH-strength argument rather than as a routine PNT-error estimate.