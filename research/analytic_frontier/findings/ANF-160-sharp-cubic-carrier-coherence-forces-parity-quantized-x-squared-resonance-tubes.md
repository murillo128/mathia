# ANF-160 — sharp cubic carrier coherence forces parity-quantized X-squared resonance tubes

**Status:** `EXACT-DERIVED + SHARP-ARC-COHERENCE + DIOPHANTINE-RESONANCE-TUBES + ENDPOINT-GATE-REFINEMENT`. `ANF-159` exhibits one family of heights `U=4 pi q M^2` for which the first two Taylor phases of the bare logarithmic carrier disappear modulo `2 pi`, leaving a coherent `M^{1/3}` block. That cubic scale is not merely an artifact of that family. For every fixed `U asymp M^2`, any block on which all carrier phases stay inside one fixed narrow arc has length `O(M^{1/3})`; the exponent `1/3` is sharp. Moreover, every block attaining a fixed positive fraction of that maximal scale forces `U` into an explicit parity-quantized collection of resonance tubes

\[
U=2\pi cM^2+\pi\sigma M+O(M^{2/3}),
\qquad
\sigma\equiv c\pmod 2,
\qquad
|\sigma|=O(M^{1/3}),
\]

with only finitely many possible integers `c` in any fixed `U/M^2` window. Conversely these scales are attained: for sufficiently small fixed tube constants, the same family remains arc-coherent for `Theta(M^{1/3})` terms. Thus the strong carrier-coherence obstruction left by `ANF-159` is a genuine denominator-one major-arc phenomenon with a sharp cubic physical scale, `M^{2/3}` transverse twist thickness, and an integer parity lattice along the `M`-scale direction. This still does not control large carrier sums that arise without phase concentration, and it does not control the signed arithmetic residual `r_X`; those remain the source-side endpoint gate.

## 1. Fixed-arc coherence has a universal cubic upper scale

Fix constants

\[
0<A<B<\infty,
\qquad
0<\delta<\frac{\pi}{8}.
\tag{1}
\]

For an integer `M>=1`, a real height

\[
AM^2\le U\le BM^2,
\tag{2}
\]

and an integer `1<=L<=M`, call the block `0<=j<L` **delta-arc coherent** if there is a real `alpha` and integers `k_j` such that

\[
\left|
-U\log(M+j)-\alpha-2\pi k_j
\right|
\le\delta
\qquad(0\le j<L).
\tag{3}
\]

This is a deliberately strong notion of carrier coherence: every phasor lies in one arc of angular radius `delta`. It is weaker than demanding equality of phases and stronger than merely demanding a large vector sum.

Put

\[
\phi(x):=-U\log(M+x),
\qquad
\epsilon_j:=\phi(j)-\alpha-2\pi k_j.
\tag{4}
\]

Then `|epsilon_j|<=delta`. For the unit forward difference,

\[
\Delta^3\phi(j)
=
\int_{[0,1]^3}
\phi'''(j+t_1+t_2+t_3)
\,dt_1dt_2dt_3,
\tag{5}
\]

and

\[
\phi'''(x)=-\frac{2U}{(M+x)^3}.
\tag{6}
\]

Hence, uniformly for `0<=j<=M`,

\[
|\Delta^3\phi(j)|\le\frac{2B}{M}.
\tag{7}
\]

On the other hand

\[
\Delta^3\phi(j)
=2\pi\Delta^3k_j+\Delta^3\epsilon_j,
\qquad
|\Delta^3\epsilon_j|\le8\delta.
\tag{8}
\]

Because `8 delta < pi`, for all sufficiently large `M` the right side of

\[
2\pi|\Delta^3k_j|
\le |\Delta^3\phi(j)|+8\delta
\tag{9}
\]

is strictly below `2 pi`. Therefore

\[
\boxed{\Delta^3k_j=0}
\qquad(0\le j<L-3).
\tag{10}
\]

The integer lifts are forced to be a quadratic sequence. In particular every higher-step third difference also vanishes:

\[
\Delta_h^3 k_0=0
\tag{11}
\]

whenever `3h<L`.

Take

\[
h:=\left\lfloor\frac{L-1}{3}\right\rfloor.
\tag{12}
\]

If `h>=1`, equations (3), (11), and the step-`h` version of (5) give

\[
8\delta
\ge
|\Delta_h^3\phi(0)|
=
\int_{[0,h]^3}
\frac{2U}{(M+t_1+t_2+t_3)^3}
\,dt_1dt_2dt_3.
\tag{13}
\]

Since `h<=M/3`, one has `M+t_1+t_2+t_3<=2M`, and therefore

\[
|\Delta_h^3\phi(0)|
\ge
\frac{A}{4}\frac{h^3}{M}.
\tag{14}
\]

Thus

\[
h^3\le\frac{32\delta}{A}M,
\tag{15}
\]

and hence

\[
\boxed{
L
\le
3\left(\frac{32\delta}{A}M\right)^{1/3}+4.
}
\tag{16}
\]

So the `M^{1/3}` scale of `ANF-159` is universal for fixed narrow-arc alignment throughout the whole height regime `U asymp M^2`. No choice of the height can keep the bare carrier inside a fixed arc for a parametrically longer interval.

## 2. Near-maximal coherent blocks force a parity-quantized resonance tube

The quadratic lift in (10) contains more information than the upper bound. Write

\[
k_j-k_0
=a j+c\binom j2,
\qquad
a,c\in\mathbb Z.
\tag{17}
\]

After subtracting the `j=0` relation in (3), define

\[
r(j)
:=
-U\log\left(1+\frac jM\right)
-2\pi a j
-2\pi c\binom j2.
\tag{18}
\]

Then

\[
|r(j)|\le2\delta.
\tag{19}
\]

For `0<=x<=1`, write exactly

\[
\log(1+x)=x-\frac{x^2}{2}+R_3(x),
\qquad
0\le R_3(x)\le\frac{x^3}{3}.
\tag{20}
\]

Substitution into (18) gives

\[
r(j)=Pj+Qj^2-U R_3(j/M),
\tag{21}
\]

where

\[
P=-\frac UM-2\pi a+\pi c,
\qquad
Q=\frac{U}{2M^2}-\pi c.
\tag{22}
\]

Now assume additionally that for some fixed `kappa>0`,

\[
L\ge\kappa M^{1/3}.
\tag{23}
\]

Let `h=floor((L-1)/2)`. For large `M`, one has `h asymp_kappa M^{1/3}` and `2h<L`. The combination `r(2h)-2r(h)` eliminates the linear term in (21), so using (19)--(20),

\[
2|Q|h^2
\le
6\delta
+
U\left(R_3(2h/M)+2R_3(h/M)\right)
\le
6\delta+\frac{10B}{3}\frac{h^3}{M}.
\tag{24}
\]

Consequently

\[
\boxed{Q=O_{B,\delta,\kappa}(M^{-2/3}).}
\tag{25}
\]

Returning to `r(h)` then gives

\[
|P|h
\le
2\delta+|Q|h^2+U R_3(h/M),
\tag{26}
\]

and therefore

\[
\boxed{P=O_{B,\delta,\kappa}(M^{-1/3}).}
\tag{27}
\]

The two coefficient constraints have a direct Diophantine meaning. From (25),

\[
U=2\pi cM^2+O_{B,\delta,\kappa}(M^{4/3}).
\tag{28}
\]

Since `U/M^2` stays in the fixed interval `[A,B]`, only finitely many positive integers `c` can occur. From (27),

\[
U
=\pi M(c-2a)
+O_{B,\delta,\kappa}(M^{2/3}).
\tag{29}
\]

Define the integer

\[
\sigma:=c-2a-2cM.
\tag{30}
\]

It automatically satisfies

\[
\sigma\equiv c\pmod2.
\tag{31}
\]

Combining (28)--(30) yields

\[
\boxed{
U
=2\pi cM^2+\pi\sigma M
+O_{A,B,\delta,\kappa}(M^{2/3}),
}
\tag{32}
\]

and (28) further forces

\[
\boxed{|\sigma|=O_{A,B,\delta,\kappa}(M^{1/3}).}
\tag{33}
\]

Equations (31)--(33) classify every fixed-fraction `M^{1/3}` arc-coherent block into a thin parity-quantized resonance tube. The `4 pi q M^2` family from `ANF-159` is the even branch `c=2q`, `sigma=0`; it is only the simplest member of the full lattice.

The parity is not cosmetic. The quadratic integer lift is naturally expressed in the integer-valued basis `j`, `binom(j,2)`, rather than in the monomial basis `j`, `j^2`. The resulting compatibility condition is precisely `sigma congruent c (mod 2)`.

## 3. The tube exponents are attained

The scales in (32)--(33) are not only necessary. Fix an integer `c>=1`. Let `sigma=sigma_M` be any integer satisfying

\[
\sigma\equiv c\pmod2,
\qquad
|\sigma|\le sM^{1/3},
\tag{34}
\]

and take

\[
U
=2\pi cM^2+\pi\sigma M+\Delta,
\qquad
|\Delta|\le dM^{2/3}.
\tag{35}
\]

For an integer `j`, the phase

\[
\pi\left(cj^2-2cMj-\sigma j\right)
\tag{36}
\]

is always a multiple of `2 pi`: indeed `sigma congruent c (mod 2)` makes `j(cj-sigma)` even. Expanding as in (20), the carrier relative to its value at `M` therefore differs from this invisible integer phase by

\[
\eta_j
=
-\frac{\Delta}{M}j
+
\left(\frac{\pi\sigma}{2M}+\frac{\Delta}{2M^2}\right)j^2
-U R_3(j/M).
\tag{37}
\]

For

\[
0\le j\le \kappa M^{1/3},
\tag{38}
\]

one has uniformly

\[
|\eta_j|
\le
 d\kappa
+\frac{\pi s}{2}\kappa^2
+\frac{2\pi c}{3}\kappa^3
+o(1).
\tag{39}
\]

Thus for every fixed target arc radius `delta_0>0`, one may choose positive constants `kappa`, `s`, and `d` small enough that the right side of (39) is below `delta_0`. Then all heights in the tube (34)--(35) produce a `delta_0`-arc-coherent block of length `floor(kappa M^{1/3})`.

This proves sharpness of all three exponents in the classification:

\[
\boxed{
L\asymp M^{1/3},
\qquad
|\sigma|\asymp M^{1/3},
\qquad
|\Delta|\asymp M^{2/3}
}
\tag{40}
\]

are simultaneously compatible with fixed-arc coherence, up to the fixed constants in (39). In particular the exact resonances of `ANF-159` are stable under absolute twist perturbations of order `M^{2/3}` when observed on the cubic physical scale.

## 4. The exceptional height set is thin but fragmented

Fix `A,B,delta,kappa` as above and restrict `U` to `[AM^2,BM^2]`. Equation (28) leaves only `O_{A,B}(1)` possible values of `c`. For each such `c`, equation (33) leaves `O(M^{1/3})` admissible integers `sigma`, with spacing `2` because of parity. The corresponding centers in (32) are separated by `2 pi M`, while each tube has radius `O(M^{2/3})`; hence the tubes are disjoint for large `M`.

Therefore the set of heights that can support a `delta`-arc-coherent block of length at least `kappa M^{1/3}` is contained in a union of

\[
O_{A,B,\delta,\kappa}(M^{1/3})
\tag{41}
\]

intervals, each of length

\[
O_{A,B,\delta,\kappa}(M^{2/3}).
\tag{42}
\]

Its total Lebesgue measure is consequently

\[
\boxed{O_{A,B,\delta,\kappa}(M).}
\tag{43}
\]

inside a height window of length `Theta(M^2)`. This is consistent with the `X`-scale generic twist localization in `ANF-144`, but is more geometric: the carrier's strongest local coherence is not one broad exceptional plateau. It is fragmented into parity-quantized `M^{2/3}` tubes whose total budget is only `O(M)`.

The measure statement is not an avoidance theorem for the bow. The bow uses one distinguished height, not a random height, so a set of relative measure `O(1/M)` can still contain exactly the point that matters. Its value is that the remaining carrier test is now explicit: determine whether the distinguished height enters one of the tubes (32) at either endpoint scale.

## 5. Relation to the endpoint threat scale

`ANF-158` proves that target-scale endpoint completion forces a twisted residual prefix or suffix sum of size

\[
\Omega(\sqrt{X\log X}),
\tag{44}
\]

and the pointwise bound `|r_X(n)|<<log X` implies that such a spike uses at least

\[
\Omega\left(\sqrt{\frac{X}{\log X}}\right)
\tag{45}
\]

endpoint sites. This minimum physical support is much larger than the universal strong carrier-coherence scale:

\[
X^{1/3}
=o\left(\sqrt{\frac{X}{\log X}}\right).
\tag{46}
\]

Thus a target-scale endpoint threat cannot be explained by saying that the bare logarithmic carrier simply remains inside one fixed narrow arc over the entire minimally required support. `ANF-159` already showed that its explicit coherent block is too small in the bow normalization; (16) now shows that this limitation is universal for **fixed-arc carrier alignment**, not merely a weakness of that example.

This is still not an endpoint bound for the actual source. A large exponential sum does not require every phasor to lie in one arc, and the signed arithmetic residual `r_X` can itself rephase, suppress, or reinforce the carrier. Equations (44)--(46) therefore rule out only the most rigid carrier-only explanation of a dangerous endpoint spike. The live theorem remains source-specific: either prove that the distinguished height avoids the explicit resonance tubes strongly enough for exponential-sum machinery to control the remaining less-coherent sums, or obtain the necessary saving from the prime--Ramanujan residual itself.

## 6. Prior-art boundary and next gate

The surrounding technology is classical. Van der Corput derivative tests and the Bombieri--Iwaniec method analyze short exponential sums by replacing smooth phases with low-degree polynomial phases and isolating rational approximations to their leading coefficients. In particular, the modern literature on the `k`-th derivative test explicitly uses phases of the form `M^{k-1} log(M+m)+P(m)`, while the Bombieri--Iwaniec method reduces short pieces to cubic phases with rational quadratic coefficient. That is the natural prior-art neighborhood of (32).

No external estimate is load-bearing here. The cubic upper bound follows directly from finite differences and the sign of the third derivative; the tube classification follows from the forced integer-valued quadratic lift and the elementary Taylor remainder (20). The specific parity lattice, the `M^{2/3}` tube width, and the bow-scale comparison are therefore recorded as derived statements inside this line, without claiming that the general major-arc philosophy is new. Since no external theorem is imported into the proof, `SOURCES.md` does not need a new durable dependency.

The concrete next gate is now narrower than the one left by `ANF-159`. At each endpoint base `M`, compute the distance of the distinguished bow height from

\[
\mathcal R_M
:=
\left\{
2\pi cM^2+\pi\sigma M:
 c\in\mathbb Z_{>0},
 \ \sigma\equiv c\pmod2,
 \ |\sigma|\ll M^{1/3}
\right\}.
\tag{47}
\]

If that distance is `omega(M^{2/3})` uniformly at every endpoint scale relevant to the completion, then maximal `M^{1/3}` fixed-arc carrier coherence is excluded and one can legitimately move to quantitative derivative/exponent-pair bounds for the remaining carrier geometry. If the distinguished height enters these tubes, the tube classification says exactly where generic carrier oscillation loses leverage, and the saving must come from arithmetic cancellation in `r_X` or from an aggregate endpoint-energy estimate. Neither outcome by itself proves or disproves the bow target, but the Diophantine alternative is now explicit and sharp at the strongest possible fixed-arc coherence scale.