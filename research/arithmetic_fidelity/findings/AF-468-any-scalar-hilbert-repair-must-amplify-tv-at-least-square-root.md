# AF-468 — Any scalar Hilbert repair must amplify TV at least at square-root scale

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-METRIC-REPAIR`, `QUANTITATIVE-FIDELITY`, `NONLINEAR-TARGET`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-467 classifies the power family `d_TV^alpha` and finds the sharp Hilbert threshold `alpha=1/2`. The same paired-mixture cube gives a stronger statement that is not restricted to powers: **any scalar transformation of TV that supports complexity-independent Hilbert fidelity on the full probability simplex must magnify sufficiently small TV distances by at least square-root order.**

Let `A` contain arbitrarily many atoms, let

\[
\Delta(A)=\left\{\mu\in\ell^1(A):\mu(a)\ge0,\ \sum_a\mu(a)=1\right\},
\qquad
d(\mu,\nu)=\|\mu-\nu\|_1,
\]

and let

\[
\phi:[0,2]\to[0,\infty)
\]

satisfy `phi(0)=0` and `phi(2)>0`. Suppose that for every `k` there is a map

\[
F_k:\Delta_k(A)\to H_k
\]

into a Hilbert space and constants `0<kappa<=L<infinity`, independent of `k`, such that

\[
\kappa\,\phi(d(\mu,\nu))
\le
\|F_k(\mu)-F_k(\nu)\|_{H_k}
\le
L\,\phi(d(\mu,\nu))
\tag{1}
\]

for all `mu,nu in Delta_k(A)`. Then for every integer `k>=1`,

\[
\boxed{
\phi(2/k)
\ge
\frac{\kappa}{L}\,\frac{\phi(2)}{\sqrt{k}}.
}
\tag{2}
\]

If `phi` is also nondecreasing, then for every `0<t<=1`,

\[
\boxed{
\phi(t)
\ge
\frac{\kappa\phi(2)}{L\sqrt3}\,\sqrt t.
}
\tag{3}
\]

Consequently,

\[
\boxed{
\frac{\phi(t)}{t}\to\infty
\quad\text{at least along }t=2/k,
}
\tag{4}
\]

and, under monotonicity, the lower bound diverges like `t^{-1/2}` throughout a full neighborhood of zero.

Thus a scalar metric repair cannot simultaneously remain uniformly comparable to the original linear TV scale near zero and produce dimension-free Hilbert fidelity for unrestricted mixtures. The singular forward sensitivity exposed by AF-466 and AF-467 is not a peculiarity of the square root or of power snowflakes; it is forced by the source geometry.

There is also a broad classical positive class matching this boundary. If `g` is a nonzero Bernstein function with `g(0)=0`, then

\[
\phi_g(t)=\sqrt{g(t)}
\tag{5}
\]

gives an **isometric Hilbert metric** on the full TV simplex:

\[
\boxed{
\|\Psi_g(\mu)-\Psi_g(\nu)\|_H
=
\sqrt{g(d(\mu,\nu))}.
}
\tag{6}
\]

Because every Bernstein function is increasing and concave, `g(0)=0` implies on `0<=t<=2`

\[
g(t)\ge \frac{t}{2}g(2),
\]

so every nontrivial transform in this sufficient class already obeys

\[
\boxed{
\phi_g(t)
\ge
\sqrt{\frac{g(2)}2}\,\sqrt t.
}
\tag{7}
\]

The square-root scale is therefore both a universal **necessary lower scale** for bounded-distortion scalar Hilbert repair of the unrestricted TV simplex and the natural local scale attained by a large classical family of negative-type transforms. This is not a characterization of all admissible transforms: `(3)` is necessary, while the Bernstein construction is a sufficient class.

## Exact obstruction derivation

Use the paired-mixture cube from AF-464. Choose distinct atoms

\[
a_1,b_1,\ldots,a_k,b_k
\]

and for `epsilon in {-1,+1}^k` define

\[
\mu_\varepsilon
=
\frac1k\sum_{j=1}^k
\begin{cases}
\delta_{a_j},&\varepsilon_j=+1,\\
\delta_{b_j},&\varepsilon_j=-1.
\end{cases}
\tag{8}
\]

A one-coordinate flip has TV distance `2/k`, while antipodes have TV distance `2`. Put

\[
f(\varepsilon)=F_k(\mu_\varepsilon).
\]

Hilbert space has Enflo type `2` with constant `1`, hence

\[
\mathbb E_\varepsilon
\|f(\varepsilon)-f(-\varepsilon)\|^2
\le
\sum_{j=1}^k
\mathbb E_\varepsilon
\|f(\varepsilon)-f(\varepsilon^{(j)})\|^2.
\tag{9}
\]

The lower half of `(1)` on antipodes gives

\[
\mathbb E_\varepsilon
\|f(\varepsilon)-f(-\varepsilon)\|^2
\ge
\kappa^2\phi(2)^2,
\tag{10}
\]

while the upper half on cube edges gives

\[
\sum_{j=1}^k
\mathbb E_\varepsilon
\|f(\varepsilon)-f(\varepsilon^{(j)})\|^2
\le
kL^2\phi(2/k)^2.
\tag{11}
\]

Combining `(9)`--`(11)` yields exactly `(2)`.

No regularity or monotonicity of `phi` is needed for this reciprocal-scale obstruction. To pass from `(2)` to every sufficiently small scale, assume `phi` is nondecreasing. Given `0<t<=1`, set

\[
k=\lceil 2/t\rceil.
\]

Then `2/k<=t` and `k<=2/t+1<=3/t`, so

\[
\phi(t)
\ge
\phi(2/k)
\ge
\frac{\kappa}{L}\frac{\phi(2)}{\sqrt{k}}
\ge
\frac{\kappa\phi(2)}{L\sqrt3}\sqrt t,
\]

which is `(3)`.

The same estimate makes the original-TV sensitivity cost explicit. Along a cube edge,

\[
\frac{\|F_k(\mu_\varepsilon)-F_k(\mu_{\varepsilon^{(j)}})\|}
     {d(\mu_\varepsilon,\mu_{\varepsilon^{(j)}})}
\ge
\kappa\frac{\phi(2/k)}{2/k}
\ge
\frac{\kappa^2\phi(2)}{2L}\sqrt{k}.
\tag{12}
\]

Therefore any family realizing `(1)` has original-TV forward Lipschitz constants growing at least as `sqrt(k)`. In particular, if a single map on the full infinite simplex satisfies `(1)`, it cannot have any finite global upper Lipschitz modulus with respect to the undeformed TV metric.

## Classical positive class from negative type

The positive construction is standard Schoenberg/Bernstein theory.

The `L^1` distance kernel is conditionally negative definite. Hence the restriction

\[
(\mu,\nu)\mapsto d(\mu,\nu)
\]

on `Delta(A)` is conditionally negative definite as well. If `g` is a Bernstein function with `g(0)=0`, the classical composition theorem for Bernstein and negative-definite functions implies that

\[
(\mu,\nu)\mapsto g(d(\mu,\nu))
\]

is again conditionally negative definite. Schoenberg's Hilbert-embedding criterion therefore supplies a Hilbert space `H_g` and a map `Psi_g` with

\[
\|\Psi_g(\mu)-\Psi_g(\nu)\|_{H_g}^2
=
g(d(\mu,\nu)),
\]

which is `(6)`.

This class contains much more than the power family from AF-467. Examples include

\[
g(t)=t^\beta,\qquad 0<\beta\le1,
\]

which recovers `phi(t)=t^{beta/2}`, but also transforms such as

\[
g(t)=1-e^{-\lambda t}
\qquad\text{and}\qquad
g(t)=\log(1+t).
\]

The latter two are locally square-root after taking `sqrt(g)`, while their macroscopic behavior differs strongly from a pure snowflake. Thus AF-468 moves the line from one-parameter exponent classification to a genuine functional metric-transform question.

The concavity estimate `(7)` is elementary: for `0<=t<=2`, concavity and `g(0)=0` give

\[
g(t)
\ge
\frac t2 g(2)+\left(1-\frac t2\right)g(0)
=
\frac t2g(2).
\]

So the sufficient Bernstein class automatically respects the necessary square-root lower scale.

## What this adds to AF-464, AF-466, and AF-467

AF-464 fixes the original TV metric and proves that arbitrary nonlinear Hilbert encoders with finite upper TV sensitivity lose inverse conditioning like `k^{-1/2}`. AF-466 exhibits one exact escape: replace `d` by `sqrt(d)`. AF-467 proves that, among powers, exponent `1/2` is the sharp transition.

AF-468 removes the power-family restriction. It proves that the cost observed in those findings is structural: **every scalar transform supporting uniform Hilbert fidelity on all paired-mixture complexities must expand small TV scales by at least square-root order.** A transform that is asymptotically linear, differentiable at zero with finite derivative, or otherwise satisfies `phi(t)=O(t)` cannot work.

Conversely, classical negative-type functional calculus supplies many exact Hilbert repairs with the required singular scale. Hence the remaining question is no longer whether a clever non-power scalar transform can stay close to TV near zero while evading the cube obstruction. It cannot. What remains is whether a downstream arithmetic mechanism can legitimately consume one of these singularly expanded metrics, or whether the source family itself is rigid enough to avoid the unrestricted-mixture geometry.

## Prior art and novelty audit

The ingredients are classical and **no theorem-level novelty is claimed for metric transforms, negative type, Bernstein-function composition, or Enflo/Hamming-cube distortion.**

- I. J. Schoenberg, **“Metric Spaces and Positive Definite Functions,”** *Transactions of the American Mathematical Society* 44(3), 522–536 (1938), DOI `10.1090/S0002-9947-1938-1501980-0`. This provides the Hilbert/negative-type criterion and the classical `L^p` power embeddings used already in AF-466/467.
- Michel Deza and Monique Laurent, ***Geometry of Cuts and Metrics***, Algorithms and Combinatorics 15, Springer (1997), DOI `10.1007/978-3-642-04295-9`, especially Chapter 9, **“Metric Transforms of L1-Spaces.”** This is direct prior art that functional transforms preserving or changing `L^1` embeddability form an established metric-geometry subject; AF-468 is not introducing that program.
- René L. Schilling, Renming Song, and Zoran Vondraček, ***Bernstein Functions: Theory and Applications***, 2nd ed., De Gruyter Studies in Mathematics 37 (2012), ISBN `978-3-11-026933-8`, especially Chapters 3–4. This is the standard modern source for Bernstein functions, their Lévy–Khintchine representation, and their interaction with positive/negative definite functions, including the composition principle used above.
- Per Enflo, **“On the nonexistence of uniform homeomorphisms between `L_p`-spaces,”** *Arkiv för Matematik* 8 (1969), 103–105, DOI `10.1007/BF02589549`, together with Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665–678 (2020), DOI `10.4007/annals.2020.192.2.8`. These supply the classical cube/type framework behind `(9)`.

The line-specific mathematical delta is the direct combination of these established tools on the probability-law source: the paired-mixture cube forces the functional lower-scale law `(2)`--`(4)`, while Bernstein composition supplies a large exact positive family. The resulting statement turns the singularity seen in AF-466/467 from an example/power-law phenomenon into a general encoding-burden theorem for scalar Hilbert repairs of TV.

## Boundary and falsification audit

- **The square-root lower scale is necessary, not sufficient.** A nondecreasing `phi` satisfying `phi(t)>=c sqrt(t)` need not make `phi(d_TV)` Hilbertian or even be a metric. The Bernstein family is one sufficient class, not a classification of all valid transforms.
- **The obstruction is for unrestricted growing mixture complexity.** A restricted arithmetic source can evade `(2)` if it excludes paired-mixture cubes of growing dimension. Such an escape requires a proved source restriction, not merely an assertion that the data are arithmetic.
- **Uniform distortion is load-bearing.** If `kappa/L` is allowed to decay with `k`, `(2)` simply records that loss. The theorem does not forbid finite-dimensional embeddings with complexity-dependent distortion.
- **The transform is scalar and radial in TV.** State-dependent, anisotropic, marked, relational, or non-radial source reparameterizations are outside the claim and may have different local costs.
- **Monotonicity is needed only for the all-small-scales statement `(3)`.** The reciprocal sequence `(2)` and the resulting blow-up along `2/k` require no monotonicity.
- **`phi(2)>0` excludes the degenerate transform.** If the transform collapses antipodal source laws already at macroscopic scale, there is no fidelity to audit.
- **The positive Bernstein construction is generally lossless rather than compressive.** Exact Hilbert embeddability does not imply finite rank, compactness, spectral compression, or preservation after any later quotient/average/determinant/trace operation.
- **No rational-prime selectivity is created.** Both the obstruction and the positive transforms work on arbitrary alphabets. They classify transport geometry, not primality.

## Arithmetic specialization

Take `A` to be the rational primes and allow arbitrary finite-support probability laws on prime labels. Any proposed scalar TV reparameterization followed by a Hilbert-valued carrier with complexity-independent two-sided fidelity must satisfy

\[
\phi(t)\gtrsim\sqrt t
\]

near zero. Therefore a prime-facing spectral or positivity construction cannot evade the Hilbert/TV obstruction merely by choosing a smoother scalar transform whose infinitesimal scale remains comparable to TV. If its transformed metric does admit uniform Hilbert fidelity, small changes of prime weights must be amplified with an unbounded ratio relative to their original TV size.

This remains only a transport constraint. A successful RH-facing use must still show that the later analytic operation both tolerates this singular scale and preserves the specific rational-prime discriminator against matched non-prime/Beurling controls.

## Consequence for the line

The scalar metric-repair branch now has a sharper boundary. The question is not merely which exponent or named transform makes TV Hilbertian. For the full mixture source, **every dimension-free scalar Hilbert repair must pay a universal local square-root-or-stronger amplification cost**, and classical Bernstein/Schoenberg transforms provide a broad family that pays exactly this kind of price.

Accordingly, future attempts to preserve original-TV semantics through a Hilbert stage have only two genuine exits: prove that the admissible arithmetic source excludes the growing paired-mixture geometry, or prove that the downstream theorem is compatible with a singularly expanded source metric. Searching for a non-power scalar transform that is both locally TV-Lipschitz and uniformly Hilbert-faithful on unrestricted mixtures is now closed by `(2)`--`(4)`.