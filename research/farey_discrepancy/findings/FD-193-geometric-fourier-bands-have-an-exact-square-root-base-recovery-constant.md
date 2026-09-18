# FD-193 — Geometric Fourier bands have an exact square-root-base recovery constant

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** observation scheduling / exact quotient coverage / sharp constant threshold
- **Depends on:** FD-117, FD-189, FD-191, FD-192
- **Classification:** `EXACT-DERIVED + SHARP-THRESHOLD + FINITE-SCALE-RECOVERY`

## Claim

`FD-189` locates the power-law transition for dyadic signed Farey Fourier bands at exponent `1/2`: a cutoff `H^(1/2+epsilon)` tail-recovers every formal source, while `sqrt(H)` still has exact holes. The power exponent is not the final threshold. At the square-root exponent itself there is an exact multiplicative constant, and it extends to every integer geometric horizon schedule.

Fix an integer `B>=2`. At horizons

\[
H=B^m,\qquad m\ge0,
\tag{1}
\]

retain the complete signed initial Fourier band

\[
1\le k\le K_c(H)
:=\min\!\left(H,\left\lfloor c\sqrt H\right\rfloor\right),
\tag{2}
\]

where `c>0`. By the divisor inversion of `FD-117/FD-189`, this is exactly equivalent to observing the cumulative-source coordinates

\[
A\!\left(\left\lfloor\frac Hk\right\rfloor\right),
\qquad 1\le k\le K_c(H).
\tag{3}
\]

Define the resulting geometric quotient coverage

\[
\mathcal Q_{B,c}
:=
\left\{
\left\lfloor\frac{B^m}{k}\right\rfloor:
 m\ge0,
 1\le k\le K_c(B^m)
\right\}.
\tag{4}
\]

Then

\[
\boxed{
\mathcal Q_{B,c}=\mathbb N
\quad\Longleftrightarrow\quad
c\ge\sqrt B.
}
\tag{5}
\]

More precisely:

1. if `c>=sqrt(B)`, **every** positive integer `n` is sampled, not merely all sufficiently large `n`;
2. if `c<sqrt(B)`, infinitely many positive integers are never sampled, and the missed coordinates can be taken arbitrarily far out.

Consequently the complete signed Farey-band history on geometric horizons is globally injective on formal increment sources exactly at and above `c=sqrt(B)`. Below that constant, after any prescribed finite prefix there are distinct formal sources with identical complete band histories.

For the dyadic schedule this gives the exact constant

\[
\boxed{c_*=\sqrt2.}
\tag{6}
\]

Thus `FD-189` can be sharpened substantially on its own observation geometry: one does not need any fixed super-square-root power. The band `k<=floor(sqrt(2H))` already recovers the entire formal source, whereas `k<=c sqrt(H)` fails for every fixed `c<sqrt2`.

A second consequence is finite-scale information cost. To recover every cumulative coordinate through `N`, it is enough to use geometric horizons `H=O_B(N^2)` and only

\[
\boxed{O_B(N)}
\tag{7}
\]

signed Fourier coefficients in total. This is the optimal order of scalar linear data for exact recovery of an arbitrary `N`-coordinate formal prefix.

The theorem is an identifiability and sampling statement. It is not a stability estimate, does not control prime-extension energy, and does not imply a Franel--Landau/RH bound.

## 1. The endpoint `sqrt(B)` covers every coordinate

Fix `n>=1` and let `H` be the least power of `B` satisfying

\[
H\ge n(n+1).
\tag{8}
\]

Minimality gives

\[
n(n+1)\le H<Bn(n+1).
\tag{9}
\]

Choose the first integer strictly to the right of `H/(n+1)`:

\[
k:=\left\lfloor\frac{H}{n+1}\right\rfloor+1.
\tag{10}
\]

The quotient interval for the value `n` is

\[
\frac{H}{n+1}<k\le\frac Hn.
\tag{11}
\]

Its real length is

\[
\frac Hn-\frac{H}{n+1}
=\frac{H}{n(n+1)}\ge1,
\tag{12}
\]

so the integer in (10) indeed satisfies the upper inequality in (11). Hence

\[
\left\lfloor\frac Hk\right\rfloor=n.
\tag{13}
\]

It remains only to show that this witness lies inside the square-root band. From (9)--(10),

\[
n+1\le k\le Bn.
\tag{14}
\]

Also

\[
(k-1)(n+1)\le H.
\tag{15}
\]

For `k` in the whole interval (14),

\[
k^2\le B(k-1)(n+1).
\tag{16}
\]

Indeed the difference

\[
f(k):=B(k-1)(n+1)-k^2
\tag{17}
\]

is a concave quadratic in `k`, and at the two endpoints of (14)

\[
f(n+1)=(n+1)((B-1)n-1)\ge0,
\tag{18}
\]

\[
f(Bn)=B((B-1)n-1)\ge0.
\tag{19}
\]

Therefore (15)--(16) imply

\[
k^2\le BH,
\qquad
k\le\sqrt{BH}.
\tag{20}
\]

Thus the witness `k` is retained when `c=sqrt(B)`, and hence for every larger `c` as well. Since every divisor `d|k` also satisfies `d<=k`, the divisor Möbius inversion used in `FD-189` is entirely available inside the same retained band and reconstructs `A(n)` exactly.

This proves the forward coverage statement in (5), including `n=1`.

## 2. Every smaller constant has infinitely many exact holes

Now fix

\[
0<c<\sqrt B.
\tag{21}
\]

Let

\[
X=B^r
\tag{22}
\]

with `r` large, and choose `d` to be the least positive integer satisfying

\[
d^2+d\ge X.
\tag{23}
\]

Minimality also gives

\[
d^2-d<X,
\tag{24}
\]

and in particular `d=sqrt(X)+O(1)`. Set

\[
n:=X+d,
\qquad
H_0:=X^2=B^{2r}.
\tag{25}
\]

At the central horizon `H_0`, a denominator producing the quotient `n` would have to lie in

\[
\left(
\frac{X^2}{X+d+1},
\frac{X^2}{X+d}
\right].
\tag{26}
\]

The two inequalities (23)--(24) imply

\[
\frac{X^2}{X+d+1}\ge X-d,
\tag{27}
\]

and

\[
\frac{X^2}{X+d}<X-d+1.
\tag{28}
\]

Thus (26) lies between two consecutive integers, with the left integer excluded if equality occurs. It contains no integer at all. Hence `n` is not sampled at `H_0`, independently of any frequency cutoff.

No earlier geometric horizon can sample `n` either. If

\[
H=B^{2r-s},\qquad s\ge1,
\tag{29}
\]

and some integer `k` satisfied `floor(H/k)=n`, then multiplying numerator and denominator by `B^s` would give

\[
\left\lfloor\frac{H_0}{B^s k}\right\rfloor=n,
\tag{30}
\]

contradicting the empty interval (26).

For later horizons write

\[
H_j=B^jH_0,
\qquad j\ge1.
\tag{31}
\]

Any denominator producing `n` must satisfy

\[
k>\frac{H_j}{n+1}.
\tag{32}
\]

But

\[
\frac{\sqrt{H_j}}{n+1}
\ge
\frac{\sqrt B\,X}{X+d+1}
\longrightarrow\sqrt B
\qquad(r\to\infty).
\tag{33}
\]

Because `c<sqrt(B)`, for all sufficiently large `r` the right side of (33) exceeds `c`. Then (32) forces

\[
k>c\sqrt{H_j},
\tag{34}
\]

so no retained denominator can sample `n` at any later horizon.

Therefore the values `n=B^r+d_r` supplied by (23) are exact holes for all sufficiently large `r`. They tend to infinity, proving the reverse implication in (5).

As in `FD-189`, every such hole gives a formal two-increment null direction: increase the increment at `n` by `epsilon` and decrease the increment at `n+1` by `epsilon`. The cumulative perturbation is supported only at the unsampled coordinate `n`, so all retained signed Fourier data remain unchanged. The construction can be placed beyond any prescribed finite prefix.

## 3. The exact root band has linear total sampling cost

The witness construction is also quantitative. For every `n<=N`, its selected horizon satisfies

\[
H<Bn(n+1)\le BN(N+1).
\tag{35}
\]

Collect the root-constant bands

\[
1\le k\le\left\lfloor\sqrt{BH}\right\rfloor
\tag{36}
\]

at all `B`-geometric horizons up to the scale on the right of (35). The total number of retained signed coefficients is bounded by a geometric series in `sqrt(B)`:

\[
\sum_{B^m\ll_B N^2}\sqrt{B\,B^m}
=O_B(N).
\tag{37}
\]

Equations (10)--(20) show that these data recover `A(n)` for every `1<=n<=N`, and hence recover all increments in the prefix.

This improves the finite-scale schedule in `FD-189`. There the power-law statement used `H^(1/2+epsilon)` and therefore `O_epsilon(N^(1+2epsilon))` signed coefficients through coordinate scale `N`. The exact constant analysis removes the power loss completely.

The linear order is also the natural information floor in this unrestricted linear model: exact recovery of an arbitrary `N`-coordinate cumulative prefix requires the measurement map to have rank at least `N`, hence at least `N` scalar linear measurements. The geometric root-band schedule is therefore order-optimal in total scalar data, although no claim is made that its constant factor or its `O(N^2)` maximum physical horizon is optimal among arbitrary schedules.

## Representation audit

No stronger observable has been inserted. `FD-117` gives the physical signed Farey Fourier coordinate, and `FD-189` proves by divisor Möbius inversion that retaining all signed modes through a cutoff `K` is exactly equivalent to retaining the quotient samples `A(floor(H/k))` for `k<=K`. The present theorem changes only the horizon schedule and asks the resulting exact coverage question.

The proof does not reconstruct source information before acquisition, impose multiplicativity, or use prime-extension energy as an added sensor. Its upper half is a deterministic witness in the original quotient coordinates; its lower half is a deterministic hole family in the same coordinates. Thus the `sqrt(B)` transition is an observation-geometry property, not an artifact of a stronger source representation.

The finite-scale rank comment also concerns the signed linear data model only. Scalar Fourier energies discard coefficient identities and do not inherit this inversion or the linear sample count.

## Prior-art and novelty boundary

Fixed-horizon sets of values `{floor(X/k)}` are classical. Randell Heyman's *Cardinality of a Floor Function Set* (Integers **19** (2019), A67; arXiv `1905.00533`) gives their cardinal structure, while Jeffrey C. Lagarias and David Harry Richman's *The floor quotient partial order* (Advances in Applied Mathematics **153** (2024), 102615; arXiv `2212.11689`) develops the floor-quotient relation as a partial order and studies its internal structure. These are the nearest general prior-art boundaries found in the targeted search.

A search for geometric-horizon unions of floor-quotient sets with a `c sqrt(H)` denominator budget, for a sharp `sqrt(B)` coverage constant, and for the corresponding Farey Fourier sampling statement did not surface a matching theorem. No global novelty claim is made. The exact contribution claimed here is the line-local classification (5) and its linear signed-data corollary after composing it with the already established Farey/Fourier divisor inversion.

No external theorem is load-bearing in the proof: all steps are elementary floor inequalities and geometric-horizon scaling. `SOURCES.md` is therefore unchanged under its durable-dependency policy.

## Boundary conditions and failure modes

The threshold concerns the **complete signed initial band** at every horizon in the exact integer geometric schedule `B^m`. It need not persist for an arbitrary sparse selection of modes, a non-geometric horizon family, a scalar band energy, or another observation that mixes frequencies before they are retained.

The lower construction is a formal-source obstruction. Unlike `FD-191`, it is not asserted to preserve squarefree support, exact prime values, or Möbius signs. For `B=2`, `FD-191` already shows arithmetic-admissible noninjectivity at the smaller constant `c=1`, while the present theorem gives unconditional formal recovery at `c=sqrt2`. Whether coordinatewise Möbius fidelity lowers the exact constant somewhere in the open interval `1<c<sqrt2` is a separate arithmetic question.

Exact injectivity at `c=sqrt(B)` is not stable recovery. Small noise can still be amplified by the divisor inversion, and nothing here bounds Franel discrepancy or Mertens cancellation. Likewise the `O_B(N)` data count says nothing about the computational or physical cost of observing horizons as large as `O_B(N^2)`.

## Research consequence

The square-root power transition of `FD-189` has an exact second layer: **the missing parameter is a constant, not a further power**. For the dyadic schedule, increasing the complete signed band from `sqrt(H)` to `sqrt(2H)` changes the unrestricted formal problem from having infinitely many exact null directions to global injectivity, and it does so with only linear total scalar data through any target source scale.

This sharpens the observation-side target after `FD-192`. If one is willing to reconstruct the source, a signed geometric low-band already reaches the information-theoretic linear order; a genuinely more informative Farey bridge is therefore not needed to improve the sample-count exponent. Its value would instead have to come from **relation sensitivity, stability, or smaller physical horizons**—for example controlling prime-extension/divisor-cube consistency without full coefficient reconstruction.

For arithmetic-admissible sources the new exact gap is also precise. The dyadic constant `c=1` remains noninjective even under squarefree prime/sign fidelity by `FD-191`, while `c=sqrt2` is injective without any arithmetic hypothesis. Determining whether cross-coordinate arithmetic restrictions move the constant inside `1<c<sqrt2` is now a sharply bounded question rather than an exponent-level one.

## Related findings

- `FD-117` — the signed Farey Fourier field is invertibly equivalent to quotient-source samples.
- `FD-189` — the dyadic power-law band threshold is `alpha=1/2`.
- `FD-191` — the exact dyadic `c=1` endpoint remains null under strong coordinatewise Möbius fidelity.
- `FD-192` — square-root-and-below dyadic nulls hide prime-extension energy at its rigidity rate.
