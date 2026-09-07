# WI-191 — the bow B-process dual is exactly an Atkinson-phase transform

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTIFICATION + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`. This finding sharpens WI-190 without claiming a new bound for the shifted-prime covariance. The exact stationary phase already derived there is not merely reminiscent of the square-root phases in the divisor problem: after grouping a dual stationary mode by the product `n=hk`, it is **exactly the classical Atkinson phase for the zeta mean-square problem, up to the elementary parity factor `(-1)^n` and a fixed phase shift**. Moreover, the square-root Dirichlet normalization `1/sqrt(m(m+h))` has exactly the stationary Jacobian that underlies the differentiated Atkinson/Jutila amplitude. The count-saturating bow therefore leads to a von-Mangoldt-weighted deformation of a classical Atkinson/Voronoi transform, on the same natural dual length `U/H^2` that occurs in short-interval Atkinson theory.

This is a prior-art redirection, not an imported estimate. Classical Atkinson/Jutila/Kolesnik bounds exploit the divisor coefficient and its transforms; they do not apply by domination to the present fiber coefficients, which retain shifted-prime arithmetic. The durable gain is that the remaining arithmetic target can now be stated against a classical exact phase-and-Jacobian skeleton rather than as a generic two-dimensional chirp problem.

## 1. Exact identification of the WI-190 dual phase

Use the notation of WI-190. On a dyadic block `m ~ X`, put

\[
A:=\frac{U}{2\pi},\qquad
f_h(m):=A\log\!\left(1+\frac hm\right).
\tag{1}
\]

For the stationary dual mode `-k`, `k>0`, WI-190 solved

\[
\frac{Ah}{m(m+h)}=k.
\tag{2}
\]

With

\[
n:=hk,\qquad q:=\frac nA=\frac{2\pi n}{U},\qquad y:=\frac hm,
\tag{3}
\]

stationarity is equivalent to

\[
q=\frac{y^2}{1+y},
\qquad
y=\frac{q+\sqrt{q^2+4q}}2.
\tag{4}
\]

The negative Legendre phase in cycles is

\[
g_U(n)
=A\left[\log(1+y)+\frac{y}{1+y}\right].
\tag{5}
\]

The two elementary identities

\[
\log(1+y)=2\operatorname{arsinh}\frac{\sqrt q}{2}
\tag{6}
\]

and

\[
\frac{y}{1+y}=\frac{\sqrt{q^2+4q}-q}{2}
\tag{7}
\]

are exact. Substituting `q=2 pi n/U` gives

\[
\boxed{
 g_U(n)
 =\frac{U}{\pi}\operatorname{arsinh}\sqrt{\frac{\pi n}{2U}}
 +\frac12\sqrt{n^2+\frac{2Un}{\pi}}
 -\frac n2.
}
\tag{8}
\]

Now take the standard Atkinson phase normalization used, for example, by Simonič--Starichkova,

\[
F_U(n)
:=2U\operatorname{arsinh}\sqrt{\frac{\pi n}{2U}}
 +\sqrt{(\pi n)^2+2\pi nU}
 -\frac{\pi}{4}.
\tag{9}
\]

Comparison of (8) and (9) gives the exact identity

\[
\boxed{
 g_U(n)=\frac{F_U(n)}{2\pi}+\frac18-\frac n2.
}
\tag{10}
\]

Equivalently, with `e(t)=exp(2 pi i t)`,

\[
\boxed{
 e(g_U(n))
 =e(1/8)(-1)^n\exp(iF_U(n)).
}
\tag{11}
\]

Thus WI-190's product dependence is not only a small-`q` square-root approximation. The **full exact phase**, at every stationary product in the B-process range, is Atkinson's phase modulo the elementary parity/constant factors. Different conventions in the literature place the fixed `pi/4` term with the opposite sign; (10) is stated against the explicit normalization (9), so the convention is not hidden.

## 2. Prime-pair parity removes the only linear correction on the main arithmetic support

The source covariance from WI-188 contains

\[
\Lambda(m)\Lambda(m+h),
\qquad m\asymp X,\quad 1\le h\lesssim K:=X/H.
\tag{12}
\]

If `h` is odd and both von-Mangoldt factors are nonzero, then `m` and `m+h` have opposite parity. The even member must therefore be a power of `2`. In a fixed dyadic interval there are `O(1)` such powers. Consequently, for bounded smooth localizer/cutoff weights,

\[
\sum_{\substack{h\le K\\h\ {m odd}}}
\sum_{m\asymp X}
\Lambda(m)\Lambda(m+h)
\ll K\log X.
\tag{13}
\]

This is negligible at the raw WI-188 target scale:

\[
K\log X=\frac{X}{H}\log X=o(X\log X)
\qquad(H\to\infty).
\tag{14}
\]

After the external `H/X` normalization of the local covariance it is only `O(log X)=o(H log X)`. Hence the load-bearing part may be restricted to **even shifts** without asking for prime-pair cancellation. For those shifts `h`, every stationary product `n=hk` is even, and therefore

\[
-\frac n2\in\mathbb Z.
\tag{15}
\]

The parity factor in (11) becomes trivial. On the asymptotically relevant prime-pair support the dual oscillation is therefore, exactly modulo a fixed unit scalar,

\[
\boxed{
 e(g_U(hk))=e(1/8)\exp(iF_U(hk)).
}
\tag{16}
\]

This upgrades WI-190's observation that the first correction `-hk/2` is "parity-type": the correction supplies **no oscillation at all** on the dominant odd-prime/odd-prime covariance.

## 3. The stationary Jacobian has the classical Atkinson/Jutila shape

There is a second exact match. From (1),

\[
f_h''(m)
=\frac{Ah(2m+h)}{m^2(m+h)^2}>0.
\tag{17}
\]

The square-root Dirichlet factors in the source polynomial contribute the smooth geometric weight

\[
\frac1{\sqrt{m(m+h)}}.
\tag{18}
\]

At a stationary point, the leading one-dimensional B-process/saddle Jacobian multiplies this by `1/sqrt(f_h''(m))`. Writing again `y=h/m` gives the **exact** product-only factor

\[
\begin{aligned}
\frac1{\sqrt{m(m+h)f_h''(m)}}
&=A^{-1/2}\sqrt{\frac{1+y}{y(2+y)}}\\
&=A^{-1/2}[q(q+4)]^{-1/4}\\
&=\boxed{\left[n\left(n+\frac{2U}{\pi}\right)\right]^{-1/4}}.
\end{aligned}
\tag{19}
\]

The second equality uses

\[
\frac{y(2+y)}{1+y}=\sqrt{q(q+4)},
\tag{20}
\]

which follows directly from (4). Up to the conventional factor generated when conjugate stationary contributions are combined into a cosine, (19) is the same amplitude profile occurring in the differentiated Atkinson/Jutila formula for `|zeta(1/2+iU)|^2`. Akio Miyai's explicit comparison of the two classical formulas writes that coefficient as

\[
\sqrt2\,n^{-1/2}
\left(\frac14+\frac{U}{2\pi n}\right)^{-1/4}
=2\left[n\left(n+\frac{2U}{\pi}\right)\right]^{-1/4}.
\tag{21}
\]

The factor `2` is exactly the expected cosine/conjugate pairing relative to the single stationary contribution (19).

Equation (19) must **not** be read as a B-process theorem for the unsmoothed factor `Lambda(m)Lambda(m+h)`. Those arithmetic coefficients cannot simply be passed through stationary phase as a smooth amplitude. The statement is narrower and exact: once the arithmetic transform is made legitimate (for example after a suitable decomposition), its phase and square-root/Jacobian skeleton are the classical Atkinson ones; the remaining difficulty is in the transformed arithmetic coefficient.

## 4. Hyperbolic fibers become a prime-weighted Atkinson transform on the same dual scale

Because both (10) and (19) depend on `(h,k)` only through

\[
n=hk,
\tag{22}
\]

any legitimate dualized expression of the schematic form

\[
\sum_{(h,k)\in\mathcal D} C_{h,k}\,e(g_U(hk))
\tag{23}
\]

can be regrouped exactly as

\[
\sum_n B_n\,e(g_U(n)),
\qquad
B_n:=\sum_{\substack{hk=n\\(h,k)\in\mathcal D}}C_{h,k}.
\tag{24}
\]

In the unweighted model the factor-pair aggregation is the mechanism that produces divisor coefficients. Here `B_n` is instead a **shifted-prime / von-Mangoldt deformation of a divisor coefficient**: the admissible factor pairs carry the arithmetic data inherited from `Lambda(m)Lambda(m+h)`, the cutoff, and the localizer. There is no phase cancellation inside a fixed product fiber; all phase oscillation after (24) occurs between different `n`.

The range also matches classical short-interval Atkinson geometry. WI-189 gives total stationary-product scale

\[
n\lesssim \rho K^2
\asymp \frac{U}{H^2},
\qquad
\rho=\frac{U}{X^2},\quad K\asymp\frac XH.
\tag{25}
\]

In Jutila's short-interval use of Atkinson's formula, as summarized explicitly by Simonič--Starichkova, the relevant Atkinson sum is truncated at

\[
M=U Y^{-2}(\log U)^8
\tag{26}
\]

for a short-interval scale `Y` in the classical range. Setting `Y=H` shows that the bow produces the **same power-scale dual length `U/H^2`**, with only the familiar technical logarithmic padding differing. This is not a numerical coincidence: both constructions are generated by the same saddle map (2)--(4).

## 5. Prior-art audit and evidence boundary

The exact classical anchor is F. V. Atkinson, **The mean value of the Riemann zeta function**, *Acta Mathematica* 81 (1949), 353--376, DOI `10.1007/BF02395027`. A modern explicit statement is Aleksander Simonič and Valeriia V. Starichkova, **Atkinson's formula for the mean square of zeta(s) with an explicit error term**, *Journal of Number Theory* 246 (2023), 111--168; arXiv:2105.06821. Their Theorem 1 states the phase (9) and reviews the Jutila/Atkinson short-interval reduction, including the dual truncation `M=TY^{-2} log^8 T` and the later use of delicate multiple-exponential-sum estimates.

For the differentiated formula and amplitude comparison in (21), see Akio Miyai, **On the Two Expressions of the Explicit Formulas for the Square of the Riemann Zeta-Function**, *Annual Report of the Faculty of Education, Iwate University* 60:2 (2001), 35--47, especially the displayed Jutila coefficient `A(T,n)`. The underlying short-interval/divisor connection is Matti Jutila, **Riemann's zeta-function and the divisor problem**, *Arkiv för Matematik* 21 (1983), 75--96.

The classical literature therefore already contains a deep technology stack around precisely this phase: Atkinson dissection, Voronoi summation, Jutila's short-interval formulas, and Kolesnik-style multiple exponential sums. No new Atkinson identity or B-process theorem is claimed here. A targeted prior-art search did **not** locate the specific observation that the WI-188/WI-190 count-saturating bow covariance lands on exactly this Atkinson phase after the product substitution `n=hk`; this absence is not evidence of priority.

The main non-transfer point is equally important. Classical estimates control special coefficients such as `(-1)^n d(n)` and exploit the divisor/Voronoi structure. They do not imply a comparable estimate for arbitrary coefficients merely bounded by a divisor function, and they do not automatically control the present `B_n`, which encodes shifted-prime correlations. Thus this finding does not close the covariance and does not improve the current simple-critical-zero proportion.

## 6. Research consequence

WI-188--WI-190 had left three broad escapes: uniform control on the alias locus, a genuinely joint shifted-prime estimate, or cancellation across the dual `(h,k)` family. The exact identification above narrows the third route substantially. The relevant dual object is not a generic two-dimensional oscillatory family. Its geometric transform is the **classical one-dimensional Atkinson transform**, while all source-specific difficulty is pushed into the hyperbolically aggregated coefficient `B_n`.

A useful next theorem target is therefore of the form

\[
\boxed{
\sum_{n\lesssim U/H^2}
B_n\exp(iF_U(n))
=o(\text{the WI-188 covariance scale}),
}
\tag{27}
\]

with `B_n` derived honestly from the shifted-von-Mangoldt source rather than replaced by `d(n)` or by an absolute-value majorant. This suggests a more focused prior-art program: inspect which pieces of Atkinson--Voronoi--Jutila--Kolesnik survive under a prime-pair deformation of the divisor coefficient, and which fail precisely because the needed shifted-prime transform is unavailable.

The identification also supplies a falsification criterion for proposed "new" dual-phase methods: if an argument uses only the phase and the square-root stationary Jacobian, then it is operating on classical Atkinson geometry and must explain what genuinely new control it obtains over the **arithmetic fiber coefficient**. Any claimed gain from treating `(h,k)` as a generic nondegenerate two-dimensional phase misses the exact product collapse (22)--(24). This keeps the research aligned with the canonical mandate: progress toward zero defect now has to enter through source-specific arithmetic coercivity, not through geometric phase novelty that is already classical.