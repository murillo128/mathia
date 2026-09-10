# PF-274 — the fixed-axis massive Jacobi chain is a squared continuous-Hahn operator

**Status:** `LITERATURE+DERIVED + EXACT-CONTINUOUS-HAHN-TRANSFORM + EXACT-SPECTRAL-REPRESENTATION + ROBIN-SOURCE-ROUTE-REFRAMING`.

[[research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes|PF-247]] writes the fixed-axis operator

\[
L=-\partial_\theta(\sin^2\theta\,\partial_\theta)
+\frac34(1+\sin^2\theta)
\]

as two parity Jacobi chains in the corridor Gegenbauer basis, and [[research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer|PF-238]] gives the exact complete-axis realization

\[
L=U(1-\partial_\tau^2)U^*,
\qquad
\tau=\log\tan\frac\theta2.
\]

Those two descriptions fit a classical special-function transform exactly. After applying `U^*` and the ordinary Fourier transform, the PF-247 corridor basis becomes the **equal-parameter symmetric continuous Hahn family** with the distinguished parameter

\[
\boxed{
 a_*:=\frac{\alpha+1/2}{2}
      =\frac{2+\sqrt5}{4},
 \qquad
 \alpha=\frac{1+\sqrt5}{2}.
}
\tag{1}
\]

Consequently the full matrix of `L` in the corridor basis is unitarily equivalent to multiplication by `1+4x^2` in the continuous-Hahn spectral measure. There is one essential phase convention at matrix level. Let `\mathsf H_*` denote the standard real Jacobi operator for multiplication by `x` in the orthonormal continuous Hahn basis with parameters `(a_*,a_*,a_*,a_*)`, and let

\[
D e_n=i^n e_n,
\qquad
\widetilde{\mathsf H}_*:=D^*\mathsf H_*D.
\]

Then the corridor transform carries this degree-dependent phase, and the exact matrix identity is

\[
\boxed{
[L]_{\{e_n\}}
=D^*(I+4\mathsf H_*^2)D
=I+4D^*\mathsf H_*^2D
=I+4\widetilde{\mathsf H}_*^2.
}
\tag{2}
\]

The PF even/odd massive Jacobi chains are therefore not merely asymptotically solvable half-line recurrences: they are the two parity restrictions of the square of one classical exactly diagonalized continuous-Hahn Jacobi operator, expressed in the corridor basis through the phase gauge `D`. In particular the `n\leftrightarrow n+2` entries acquire `i^{\pm2}=-1`, consistently with PF-247's negative same-parity off-diagonal sign.

This gives an exact spectral integral for every bounded Borel function of `L`, including the massive Green kernels used in PF-261--PF-267 and, crucially, the square-root Robin source exposed by [[research/prime_flute/findings/PF-273-seam-square-root-is-a-complete-bernstein-green-continuum-with-mass-one-edge|PF-273]]. It does **not** by itself prove the required `R>1` low-output estimate for the normalized source. Its value is that the live small-mass boundary layer can now be attacked as a concrete continuous-Hahn coefficient problem rather than only through a parameter-uniform family of abstract Jacobi recurrences.

## Claim

Use PF-247's notation

\[
e_n(\theta)
=h_n^{-1/2}\sin^\alpha\theta\,
 C_n^{(\alpha)}(\cos\theta),
\qquad
Ae_n=(n+\alpha)^2e_n,
\tag{3}
\]

with

\[
h_n=
\frac{\pi 2^{1-2\alpha}\Gamma(n+2\alpha)}
{n!(n+\alpha)\Gamma(\alpha)^2}.
\tag{4}
\]

Let the Fourier transform be

\[
\widehat f(\xi)=\int_{\mathbb R}e^{-i\xi\tau}f(\tau)\,d\tau.
\tag{5}
\]

Define `\psi_n=U^*e_n`. Then:

1. one has the exact complete-axis basis formula
   \[
   \boxed{
   \psi_n(\tau)
   =(-1)^n h_n^{-1/2}
   \operatorname{sech}^{2a_*}\!\tau\,
   C_n^{(\alpha)}(\tanh\tau);
   }
   \tag{6}
   \]
2. if `p_n(x;a,b,c,d)` is the standard continuous Hahn polynomial, then
   \[
   \boxed{
   \widehat\psi_n(\xi)
   =i^n d_n
   B\!\left(a_*+\frac{i\xi}{2},a_*-\frac{i\xi}{2}\right)
   p_n\!\left(\frac\xi2;a_*,a_*,a_*,a_*\right),
   }
   \tag{7}
   \]
   where
   \[
   d_n=
   \frac{2^{2a_*-1}(2\alpha)_n}
   {\sqrt{h_n}\,(2a_*)_n^2}>0;
   \tag{8}
   \]
3. the functions `(2\pi)^{-1/2}\widehat\psi_n` form an orthonormal basis of `L^2(\mathbb R,d\xi)`, and `L` is multiplication by `1+\xi^2` in this representation;
4. hence, for every bounded Borel `H`,
   \[
   \boxed{
   \langle e_m,H(L)e_n\rangle
   =\frac1{2\pi}\int_{\mathbb R}
   H(1+\xi^2)
   \overline{\widehat\psi_m(\xi)}
   \widehat\psi_n(\xi)\,d\xi;
   }
   \tag{9}
   \]
5. with `\mu=\sqrt{1+a^2}`, the massive Green family has the exact form
   \[
   \boxed{
   \langle e_m,(L+a^2)^{-1}e_n\rangle
   =\frac1{2\pi}\int_{\mathbb R}
   \frac{
   \overline{\widehat\psi_m(\xi)}
   \widehat\psi_n(\xi)}
   {\xi^2+\mu^2}\,d\xi;
   }
   \tag{10}
   \]
6. PF-273's square-root source multiplier satisfies
   \[
   \boxed{
   \langle e_m,g_w(L)e_n\rangle
   =\frac1{2\pi}\int_{\mathbb R}
   g_w(1+\xi^2)
   \overline{\widehat\psi_m(\xi)}
   \widehat\psi_n(\xi)\,d\xi,
   }
   \tag{11}
   \]
   where
   \[
   g_w(\lambda)
   =\sqrt{\sqrt\lambda\tanh(w\sqrt\lambda)}.
   \tag{12}
   \]

Opposite parities vanish in (9)--(11), consistently with PF-247. No claim below turns the continuous-Hahn representation itself into an RH mechanism or imports any independent zeta information.

## 1. The complete-axis image of the corridor basis has exactly the Fourier-transform weight

PF-238 defines

\[
(U\phi)(\theta)=\sin^{-1/2}\theta\,\phi(\tau(\theta)),
\qquad
\tau=\log\tan\frac\theta2.
\tag{13}
\]

The elementary identities

\[
\sin\theta=\operatorname{sech}\tau,
\qquad
\cos\theta=-\tanh\tau
\tag{14}
\]

and Gegenbauer parity give

\[
\begin{aligned}
\psi_n(\tau)
&=(U^*e_n)(\tau)\\
&=h_n^{-1/2}\sin^{\alpha+1/2}\!\theta\,
C_n^{(\alpha)}(\cos\theta)\\
&=(-1)^nh_n^{-1/2}
\operatorname{sech}^{\alpha+1/2}\!\tau\,
C_n^{(\alpha)}(\tanh\tau).
\end{aligned}
\tag{15}
\]

Since `2a_*=\alpha+1/2`, this is (6). The exponent is not chosen to manufacture a special-function family: it is forced jointly by PF-247's corridor eigenbasis and the `\sin^{-1/2}\theta` density in PF-238's unitary compactification.

## 2. The Fourier transform is exactly symmetric continuous Hahn

Put `y=\tanh\tau` in (5). Since

\[
d\tau=\frac{dy}{1-y^2},
\qquad
e^{-i\xi\operatorname{arctanh}y}
=(1-y)^{i\xi/2}(1+y)^{-i\xi/2},
\tag{16}
\]

the transform in (6), before its factor `(-1)^nh_n^{-1/2}`, is

\[
\int_{-1}^1
(1-y)^{a_*-1+i\xi/2}
(1+y)^{a_*-1-i\xi/2}
C_n^{(\alpha)}(y)\,dy.
\tag{17}
\]

Using

\[
C_n^{(\alpha)}(y)
=\frac{(2\alpha)_n}{n!}
{}_2F_1\!\left(
-n,n+2\alpha;\alpha+\frac12;\frac{1-y}{2}
\right)
\tag{18}
\]

and integrating the terminating series term by term gives the classical Jacobi/Gegenbauer Fourier-transform formula

\[
\begin{aligned}
(17)
={}&2^{2a_*-1}\frac{(2\alpha)_n}{n!}
B\!\left(a_*+\frac{i\xi}{2},a_*-\frac{i\xi}{2}\right)\\
&\times{}_3F_2\!\left(
\begin{matrix}
-n,\ n+2\alpha,\ a_*+i\xi/2\\
2a_*,\ \alpha+1/2
\end{matrix};1\right).
\end{aligned}
\tag{19}
\]

Now the PF exponent produces the exact coincidence

\[
2a_*=\alpha+\frac12,
\qquad
4a_*-1=2\alpha.
\tag{20}
\]

For the standard continuous Hahn normalization,

\[
p_n(x;a,a,a,a)
=i^n\frac{(2a)_n^2}{n!}
{}_3F_2\!\left(
\begin{matrix}
-n,\ n+4a-1,\ a+ix\\
2a,\ 2a
\end{matrix};1\right).
\tag{21}
\]

Substituting `a=a_*`, `x=\xi/2` into (21), then combining (19) with the prefactor in (6), proves (7)--(8). In particular the four continuous-Hahn parameters coincide; no asymmetric parameter remains hidden in the PF compactification.

The classical continuous-Hahn weight for these parameters is

\[
w_*(x)=|\Gamma(a_*+ix)|^4.
\tag{22}
\]

Equation (7) carries exactly this Gamma envelope because

\[
B(a_*+ix,a_*-ix)
=\frac{|\Gamma(a_*+ix)|^2}{\Gamma(2a_*)}.
\tag{23}
\]

The `n`-dependent scalar in (8) is precisely the normalization inherited from the already orthonormal PF corridor modes.

## 3. The PF parity chains are phase-twisted squares of one continuous-Hahn Jacobi operator

The map `U^*` is unitary and the Fourier transform (5) is Plancherel-unitary after multiplication by `(2\pi)^{-1/2}`. Therefore the family

\[
\Phi_n(\xi):=(2\pi)^{-1/2}\widehat\psi_n(\xi)
\tag{24}
\]

is an orthonormal basis of `L^2(\mathbb R,d\xi)`. Under the same transform,

\[
1-\partial_\tau^2\longmapsto 1+\xi^2.
\tag{25}
\]

Equations (13) and (25) prove (9). If one instead uses `x=\xi/2`, the multiplier is `1+4x^2`. Let `\mathcal S` be the standard real continuous-Hahn spectral transform, so multiplication by `x` corresponds to the standard real Jacobi operator `\mathsf H_*`. Equation (7) shows that the actual corridor transform is `\mathcal T=\mathcal S D` with `D e_n=i^n e_n`. Hence multiplication by `x` in the transformed corridor basis is `D^*\mathsf H_*D`, and multiplication by `x^2` is `D^*\mathsf H_*^2D`. This proves (2). The factor `i^{\pm2}=-1` on the `n\leftrightarrow n+2` entries recovers the negative same-parity off-diagonal sign in PF-247.

Thus the even/odd restrictions of `L` are exactly the two parity restrictions of the square of the phase-twisted Jacobi operator `\widetilde{\mathsf H}_*=D^*\mathsf H_*D`. This supplies a structural explanation for two facts previously derived directly in the PF basis: exact parity tridiagonality and the complete spectrum `[1,\infty)` of the massive fixed-axis operator. More importantly for the current route, it identifies the **entire** mass family with one fixed classical spectral measure instead of treating each `L+a^2` recurrence as a separate asymptotic problem.

Equation (10) is immediate from (9). It packages PF-262--PF-267's Green family into the Cauchy transform of the same continuous-Hahn measure, with the physical mass entering only through the pair of poles `\xi=\pm i\mu`.

## 4. PF-273's mass-one edge becomes the nearest multiplier branch point

PF-273 proves that the raw square-root source is `g_w(L)` and that its Stieltjes resolution reaches the limiting Green mass `\mu=1`. In the present representation there is an equivalent, sharper way to see why this edge appears.

Near `\lambda=0`,

\[
\sqrt\lambda\tanh(w\sqrt\lambda)
=w\lambda+O(\lambda^2),
\tag{26}
\]

so

\[
\boxed{
g_w(\lambda)=\sqrt w\,\lambda^{1/2}(1+O(\lambda)).}
\tag{27}
\]

Thus the multiplier in (11) has square-root branch points at

\[
\boxed{\xi=\pm i,}
\tag{28}
\]

where `1+\xi^2=0`. By contrast, the Beta/Gamma envelope in (7) is meromorphic and its nearest poles occur at

\[
\xi=\pm2ia_*
=\pm i\frac{2+\sqrt5}{2},
\qquad 2a_*>1.
\tag{29}
\]

Other zeros or poles inherited from `\tanh(w\sqrt\lambda)` lie at negative `\lambda` away from zero and therefore map farther from the real `\xi` axis than the points (28). Hence the mass-one edge seen in PF-273 is not an artifact of the Stieltjes decomposition: the exact spectral multiplier itself introduces a singularity closer to the physical line than the continuous-Hahn basis envelope.

There is also a useful contrast with the raw relative seam. Its scalar core is

\[
f_w(\lambda)=g_w(\lambda)^2
=\sqrt\lambda\tanh(w\sqrt\lambda)
=w\lambda+O(\lambda^2),
\tag{30}
\]

which is analytic through `\lambda=0`. Squaring the source therefore removes precisely the branch point (28). This is consistent with [[research/prime_flute/findings/PF-272-sublinear-output-windows-restore-a-strict-finite-seam-exponent|PF-272]]: the raw seam can retain a strict deep-low-output margin even though PF-273 shows that the unsquared source has a mass-one continuum.

Equations (27)--(30) are only analytic-geography statements. They do **not** by themselves turn distance of a complex singularity into an asymptotic for continuous-Hahn coefficients; that requires a separate uniform Darboux/contour or difference-equation argument.

## 5. Consequence for the accepted Robin-source clue

The accepted local clue `CLUE-robin-homotopy-separated-poisson-shear-estimate` asks whether

\[
B_w=(I+\mathcal R_{s,r}^0)^{-1}X_w,
\qquad
X_w=s^{-1/2}A^{-1/4}g_w(L),
\tag{31}
\]

has strict high-to-low leakage after the normalization is inserted. PF-273 phrased the immediate technical gate as a small-mass Green estimate uniform when `t\log(j/i)=O(1)`.

Equation (11) supplies an exact alternative formulation of the same gate. Since `A^{-1/4}` is diagonal in the corridor basis,

\[
\boxed{
\langle e_m,X_we_n\rangle
=s^{-1/2}(m+\alpha)^{-1/2}
\frac1{2\pi}\int_{\mathbb R}
 g_w(1+\xi^2)
 \overline{\widehat\psi_m(\xi)}
 \widehat\psi_n(\xi)\,d\xi.
}
\tag{32}
\]

Therefore the source side of the clue is now an explicit equal-parameter continuous-Hahn coefficient problem. The small-`t` Stieltjes boundary layer and the complex branch points `\xi=\pm i` are two representations of the same unresolved threshold. One may work in whichever representation gives the sharper uniform estimate; there is no longer a need to regard the PF-262 recurrence coefficients as an unspecified Jacobi family.

The rational normalization in (31) is still genuinely noncommutative because `A` is diagonal in the corridor basis while functions of `L` are diagonal in the continuous-Hahn/Fourier representation. Nothing here proves that `(I+\mathcal R_{s,r}^0)^{-1}` cancels, preserves, or worsens the branch-controlled high-to-low coefficient of `X_w`.

## 6. Prior art and novelty audit

The transform technology is classical and is **not** claimed as new.

- E. Koelink, *On Jacobi and continuous Hahn polynomials*, Proceedings of the American Mathematical Society **124** (1996), 887--898; arXiv:`math/9409230`. Koelink proves that Jacobi polynomials with the appropriate hyperbolic weight are mapped by Fourier transform to continuous Hahn polynomials and obtains their orthogonality from Parseval.
- E. Güldoğan Lekesiz, R. Aktaş, I. Area, *Fourier Transform of the Orthogonal Polynomials on the Unit Ball and Continuous Hahn Polynomials*, Axioms **11** (2022), 558, DOI `10.3390/axioms11100558`. Its univariate specialization gives exactly the Fourier transform of `(1-\tanh^2x)^a C_n^{(\mu)}(\tanh x)` as the Beta factor times the terminating `{}_3F_2` used in (19).
- NIST DLMF §18.19 records the standard continuous Hahn normalization, Gamma weight, and orthogonality used in (21)--(23).
- D. Romik, *Orthogonal polynomial expansions for the Riemann xi function in the Hermite, Meixner-Pollaczek, and continuous Hahn bases*, Mathematika **65** (2019), 1104--1156; arXiv:`1902.06330`, independently uses the symmetric continuous Hahn family with parameters `(3/4,3/4,3/4,3/4)` in an expansion of `\Xi`. That is separate prior art and is **not** evidence for the Prime-Flute mechanism: the PF parameter is the different forced value (1), and no zeta information is imported into (2)--(32).

A targeted repository search found no existing Prime-Flute finding identifying the fixed-axis basis with continuous Hahn polynomials, and the recent PF-262--PF-273 route treats the same object through Jacobi recurrence/Green estimates and Stieltjes mass resolution. No novelty is claimed for continuous Hahn polynomials, Fourier diagonalization of `1-\partial_\tau^2`, Parseval, or the generic Jacobi-to-continuous-Hahn transform. The project-specific result is the exact parameter matching forced by PF-238/PF-247, the phase-corrected squared-Jacobi identification (2), and the resulting direct representation (32) of the currently live square-root source.

## 7. Boundaries and falsification

1. **No leakage exponent yet.** Equations (11) and (32) are exact representations, not a proof of any `N^{-R-\varepsilon}` block estimate.
2. **No automatic singularity-to-coefficient theorem.** Although `\pm i` are the nearest branch points introduced by `g_w(1+\xi^2)`, extracting uniform large-degree continuous-Hahn coefficients requires justified contour/asymptotic control.
3. **Normalization remains open.** The operator `(I+\mathcal R_{s,r}^0)^{-1}` does not commute with the continuous-Hahn multiplier representation because of the corridor `A^{-1/4}` factors.
4. **Fixed axis only.** No uniformity in shear, variable corridor scale, hypercycle transport, or the canonical tail follows from this transform.
5. **No imported RH content.** The appearance of the same classical polynomial family in Romik's unrelated `\Xi` expansion supplies prior-art context only. It is not a bridge between the prime flute and zeta zeros.
6. **Phase convention is harmless only spectrally.** Changing the Fourier sign or continuous-Hahn phase conjugates the standard Jacobi matrix by a diagonal unitary. The spectral measure and functional-calculus formulas (9)--(11) are unchanged, but the phase cannot be dropped from the corridor-basis matrix identity: it is exactly what produces PF-247's negative same-parity off-diagonal sign.

The finding would fail if PF-238's unitary density were different, if PF-247's Gegenbauer exponent did not satisfy `2a_*=\alpha+1/2`, or if the hypergeometric parameters in (19) did not match (21). Equations (15), (19), and (20) make those three checks explicit.

## Decisive next test

Use (32) to derive the strongly separated large-degree asymptotic of

\[
\langle e_m,g_w(L)e_n\rangle,
\qquad m\le n^\theta
\quad\text{or}\quad
m\le A\log n,
\tag{33}
\]

uniformly in the complete output window required by PF-271. The first target should be the contribution forced by the branch points `\xi=\pm i`, with a proof that the farther Beta/Gamma singularities and the remaining `\tanh` singularities are lower order. Compare the resulting estimate with the small-mass Stieltjes boundary layer of PF-273 as an independent consistency check.

Only after the raw source coefficient is sharp should the accepted clue spend effort on the noncommuting factor `(I+\mathcal R_{s,r}^0)^{-1}`. A strict power beyond `R=1` would reopen the positive separated Robin route; a sharp critical lower bound would instead isolate the normalization as the only possible place where the missing margin can be created.