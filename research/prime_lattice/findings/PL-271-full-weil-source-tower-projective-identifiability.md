# PL-271 — The full finite-Weil source tower identifies the source modulo the zero-frequency endpoint

**Evidence:** `LITERATURE+DERIVED`

**Status:** `EXACT-DERIVED + PROJECTIVE-IDENTIFIABILITY + STRUCTURAL-REDIRECT + PRIOR-ART-COMBINATION`

## Claim

Fix the Groskin finite source calculus on `[0,1]`. For a finite real signed Borel measure `mu`, let `Q_N[mu]` be its level-`N` divided-difference/Galerkin source matrix. Groskin's Corollary 2.4 says that `Q_N[mu]` is exactly equivalent to the `2N+1` coordinates

\[
\int_0^1 \omega\,d\mu(\omega),
\]

and, for `1<=k<=N`,

\[
\int_0^1\sin(2\pi k\omega)\,d\mu(\omega),
\qquad
\int_0^1\omega\cos(2\pi k\omega)\,d\mu(\omega).
\]

The projective family over **all** Galerkin bands is much more rigid than any one finite quotient:

\[
\boxed{
Q_N[\mu]=Q_N[\nu]\ \text{for every }N\ge0
\quad\Longleftrightarrow\quad
\mu-\nu=a\,\delta_0
\ \text{for some }a\in\mathbb R.
}
\]

Thus the full tower is injective on finite signed source measures modulo the single zero-frequency atom at `omega=0`. This atom is not an artifact of the proof: it is genuinely invisible because `sin(2 pi omega x)` vanishes identically when `omega=0`.

For the zeta prime source at fixed cutoff `c`,

\[
\nu_c=\sum_{q=p^a\le c}\frac{\Lambda(q)}{\sqrt q}\,
\delta_{1-\log q/\log c},
\]

the only possible invisible atom is the boundary event `q=c` when `c` itself is a prime power. At that exact cutoff its frequency is zero and its sine-source contribution is already identically zero. If `c` is not a prime power, the complete Galerkin tower determines `nu_c` uniquely even among arbitrary finite signed source measures on `[0,1]`.

There is also a finite-support consequence directly relevant to `PL-270`. For any fixed finite support `S subset (0,1]`, there exists some finite band `N_0(S)` such that the restrictions of the Groskin coordinates through level `N_0(S)` already have full rank on measures supported on `S`. Hence, for a fixed prime cutoff, once the band is sufficiently large, there is no nontrivial exact Tchakaloff alias obtained merely by deleting/reweighting atoms on the **same nonzero active support**. No quantitative bound or conditioning estimate for `N_0(S)` is asserted.

Consequently, the finite-band nonidentifiability of `PL-270` does **not** persist as a coherent all-band ambiguity. The surviving source-side target is exactly cross-band coherence: aliases can be chosen separately at every finite band, but one fixed alternative source cannot reproduce the entire tower except for the intrinsically invisible zero-frequency endpoint. This restores source identity, but it does not supply a Weil-sign theorem; the injectivity argument is generic Fourier uniqueness and holds for arbitrary finite measures, not specifically for rational primes.

## 1. Exact kernel of the projective source map

Let `lambda=mu-nu` and assume `Q_N[lambda]=0` for every `N`. Groskin's exact finite quotient gives

\[
\int \omega\,d\lambda=0,
\]

and, for every integer `k>=1`,

\[
\int\sin(2\pi k\omega)\,d\lambda=0,
\qquad
\int\omega\cos(2\pi k\omega)\,d\lambda=0.
\tag{1}
\]

Let `R(omega)=1-omega`. First consider

\[
\sigma:=\lambda-R_*\lambda.
\]

Every cosine Fourier coefficient of `sigma` vanishes identically by reflection symmetry, while every sine coefficient is twice the corresponding sine coefficient of `lambda` and therefore vanishes by (1). Its total mass also vanishes. After identifying `0` and `1`, all Fourier-Stieltjes coefficients of the push-forward of `sigma` to the circle are zero. Classical uniqueness of Fourier coefficients for finite measures on the circle therefore gives zero push-forward. Equivalently,

\[
\lambda=R_*\lambda
\quad\text{on the open interval }(0,1),
\tag{2}
\]

with only a possible endpoint difference left invisible to the circle quotient.

Now put

\[
\eta:=\omega\,\lambda.
\]

The first condition in (1) says that `eta` has total mass zero, and the remaining cosine conditions say that all of its cosine Fourier coefficients vanish. The reflected symmetrization

\[
\tau:=\eta+R_*\eta
\]

therefore has every Fourier coefficient equal to zero: the cosine coefficients are twice those of `eta`, the sine coefficients vanish by symmetry, and the constant coefficient is zero. Its circle push-forward is zero. But `tau` is itself `R`-invariant, whereas the only interval measures killed by the endpoint identification are multiples of `delta_0-delta_1`, which are `R`-anti-invariant. Hence

\[
\tau=0
\tag{3}
\]

as a measure on `[0,1]`.

On `(0,1)`, equation (2) gives

\[
R_*\eta=(1-\omega)R_*\lambda=(1-\omega)\lambda.
\]

Combining this with (3),

\[
0=\eta+R_*\eta
=\omega\lambda+(1-\omega)\lambda
=\lambda
\]

on `(0,1)`. Thus `lambda` is supported on the endpoints. Write

\[
\lambda=a\delta_0+b\delta_1.
\]

The moment condition `int omega dlambda=0` forces `b=0`, while `a delta_0` annihilates every Groskin coordinate. Therefore

\[
\boxed{\ker\{\mu\mapsto(Q_N[\mu])_{N\ge0}\}=\mathbb R\delta_0.}
\]

No analytic continuation, zeta-zero information, or prime-number theorem is used in this derivation.

## 2. Finite support eventually saturates

Let `S={omega_1,...,omega_M} subset (0,1]` be fixed and let `V_N(S)` be the coordinate map obtained by restricting the level-`N` Groskin functions to `S`. Its ranks are nondecreasing in `N` and bounded by `M`.

Suppose no finite band had full rank. The descending sequence of annihilator subspaces

\[
\ker V_0(S)\supseteq\ker V_1(S)\supseteq\cdots
\]

would then stabilize in the finite-dimensional space `R^M` with positive dimension. A nonzero stabilized vector would define a nonzero signed measure supported on `S` that annihilates every coordinate at every level. The projective-kernel theorem above says that such a measure must be a multiple of `delta_0`, impossible because `0 notin S`. Therefore

\[
\boxed{\exists N_0(S)<\infty:\ \operatorname{rank}V_N(S)=M\quad(N\ge N_0(S)).}
\]

If `0` is included in `S`, the same argument gives eventual rank `M-1`, with the unique missing direction equal to the zero-frequency atom.

This is an algebraic identifiability statement only. It gives no useful upper bound on `N_0(S)` and no lower bound on the smallest singular value of `V_N(S)`. As prime-power frequencies cluster under changing cutoffs, numerical recovery can remain badly conditioned even when exact rank is full.

## 3. Consequence for the live source-positivity route

`PL-270` proves that one fixed band sees only a `2N+1`-dimensional quotient and therefore admits exact positive support-preserving aliases whenever sufficiently many prime-power events are active. The present result identifies the precise boundary of that obstruction. The aliases cannot be promoted to a single coherent source across all bands: the projective tower recovers the source function completely, modulo the source-null endpoint `omega=0`.

This makes cross-band compatibility mathematically substantive rather than merely a bookkeeping suggestion. A source-forced positivity mechanism is allowed to use relations among growing bands that no one fixed quotient contains. In particular, the canonical persistence of the von Mangoldt masses as `N` varies is information that the independent Tchakaloff compressions of `PL-270` do not preserve.

However, projective identifiability is not itself an RH mechanism. The proof works for every finite signed measure on `[0,1]`, including matched generalized-prime or synthetic source measures. It therefore fails the line's rational-prime specificity test if used alone. Restoring the full source merely removes the finite-band information-loss objection; a successful RH argument still needs an additional completed/global relation that turns the recovered rational-prime source into positivity of the localized Weil form.

A further warning is that using the entire tower only to reconstruct `nu_c` is formally lossless but may offer no simplification over the original explicit formula. The useful next theorem would have to exploit a **cross-band constraint stronger than reconstruction**—for example a positivity, monotonicity, compatibility, or rigidity law forced by the canonical source and absent from matched controls.

## 4. Novelty and adversarial audit

The finite source quotient is due to Groskin, and the uniqueness step is classical Fourier-Stieltjes uniqueness on the circle. The current literature audit checked Groskin's paper, its stated novelty boundary, current searches around the exact source quotient, and general derivative/Hermite sampling literature. Groskin explicitly treats the quotient at fixed `N` and emphasizes that no `N`-limit enters the finite dictionary; the audit did not find the projective-kernel statement above presented as a zeta/Weil theorem. This absence is not evidence of novelty. The durable content here is therefore recorded as an exact **combination and structural redirect**, not as a claim of a new sampling theorem.

The strongest controls are built into the statement. A different source may match any one finite band and may even be chosen positive on a sparse subset as in `PL-270`; it cannot match every band unless it differs only at zero frequency. Conversely, the theorem does not distinguish the rational-prime source from a generic source, does not constrain zeta zeros, and does not prove any sign. The endpoint exception is genuine and cannot be removed without changing the source representation: `delta_0` produces the identically zero sine source.

A falsifying example would be a nonzero finite signed measure supported away from `0` whose Groskin coordinates vanish for every `N`. By the reflection/Fourier argument above such a measure cannot exist. A materially stronger future result would need quantitative stability as both cutoff and band move, or an arithmetic cross-band law not shared by generic finite measures.

## Sources

- Akiva Groskin, **“A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form,”** arXiv:2607.02828v3 [math.NT] (submitted 2 July 2026; revised 14 August 2026). Lemma 2.3 and Corollary 2.4 give the exact finite source calculus and the `2N+1` source quotient used here. The paper treats the finite-band dictionary and does not assert the projective source-kernel statement recorded above.
- Classical Fourier-Stieltjes uniqueness on `T`: a finite Borel measure whose full set of Fourier coefficients vanishes is zero. In the proof above this can be obtained directly from density of trigonometric polynomials in `C(T)`; no specialized zeta input is required.
