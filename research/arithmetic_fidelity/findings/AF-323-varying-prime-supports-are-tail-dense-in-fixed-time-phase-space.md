# AF-323 — Varying prime supports are tail-dense in fixed-time phase space

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-CONSEQUENCE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SUPPORT-UNIFORMITY-OBSTRUCTION`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-322 proves that for every **fixed** eight-prime support `P`, the common-time prime orbit stays at least a support-dependent inverse power of the time height away from the four-antipodal-pair locus. The dependence on `P` is not merely an artifact of the Baker-type estimate.

Fix any nonzero real time `tau`, any integer `m>=1`, and any lower prime cutoff `X>=1`. Define

\[
\mathcal P_{m,\tau}(X)
=
\left\{
(p_1^{-i\tau},\ldots,p_m^{-i\tau}):
 p_1,\ldots,p_m>X\text{ are pairwise distinct rational primes}
\right\}
\subset (S^1)^m.
\tag{1}
\]

Then

\[
\boxed{
\overline{\mathcal P_{m,\tau}(X)}=(S^1)^m
\qquad
(\tau\ne0,\ m\ge1,\ X\ge1).
}
\tag{2}
\]

Thus allowing the rational-prime support to vary — even while forcing every selected prime arbitrarily far out in the prime tail and keeping the clock time fixed — makes the resulting finite prime-phase configurations dense in the entire ambient torus.

Equivalently, for every continuous observable

\[
C:(S^1)^m\to Y
\tag{3}
\]

with `Y` Hausdorff,

\[
\boxed{
\overline{C(\mathcal P_{m,\tau}(X))}=C((S^1)^m).
}
\tag{4}
\]

Every ambient value of a continuous finite-phase compression is therefore approximable by **actual rational-prime supports**, not merely by generalized-prime or continuously perturbed matched controls.

For the eight-point singular geometry of AF-320--AF-322, let `A_8` be the four-antipodal-pair locus and

\[
\delta_P(t)=\operatorname{dist}(Z_P(t),A_8),
\qquad
Z_P(t)=(p_1^{-it},\ldots,p_8^{-it}).
\tag{5}
\]

Then at every fixed `tau!=0`,

\[
\boxed{
\inf_{P}\delta_P(\tau)=0,
}
\tag{6}
\]

where the infimum runs over eight-element rational-prime supports, and the same remains true if all primes are required to exceed an arbitrary cutoff `X`.

Consequently there cannot exist support-independent constants `c>0` and `kappa>0` such that

\[
\delta_P(t)\ge c(1+|t|)^{-\kappa}
\tag{7}
\]

for every eight-prime support `P` and every nonzero `t`. More generally, no positive lower modulus depending only on `|t|` can hold uniformly over unrestricted prime supports: fixing one nonzero `tau` already contradicts it.

The high-symmetry collision behind AF-321 is also approached by actual prime supports. Put

\[
\omega=e^{i\pi/4},
\qquad
R_\rho=(\rho,\rho\omega,\ldots,\rho\omega^7),
\qquad \rho\in S^1.
\tag{8}
\]

For

\[
s_r(Z)=\sum_{j=1}^8 z_j^r,
\qquad
E(Z)=\prod_{j=1}^8z_j,
\tag{9}
\]

one has

\[
s_r(R_\rho)=0\qquad(1\le r\le7),
\tag{10}
\]

while

\[
E(R_\rho)=-\rho^8.
\tag{11}
\]

Hence for every target product phase `eta in S^1`, every `X`, and every fixed `tau!=0`, there is a sequence of eight-prime supports `P_n`, all with primes greater than `X`, such that

\[
(s_1,\ldots,s_7)(Z_{P_n}(\tau))\longrightarrow0,
\qquad
E(Z_{P_n}(\tau))\longrightarrow\eta.
\tag{12}
\]

In particular, there is **no uniformly continuous decoder**

\[
R:H_7(\mathcal P_{8,\tau}(X))\to S^1,
\qquad
H_7(Z)=(s_1(Z),\ldots,s_7(Z)),
\tag{13}
\]

satisfying

\[
R(H_7(Z_P(\tau)))=E(Z_P(\tau))
\tag{14}
\]

for every eight-prime support in the domain. If exact recovery by such a rule is not even well-defined, that is already stronger failure; if it is well-defined on the discrete source image, `(12)` rules out uniform continuity.

This does **not** settle the exact middle-singular incidence question left open by AF-322. The approximating prime configurations in `(12)` need not satisfy `s_1=0` or `e_4=0` exactly. What it settles is the support-uniform metric route: exact incidence or a support-scale resource must do any remaining work. There is no open phase-space separation supplied merely by the fact that the frequencies came from rational primes once the finite support itself is allowed to vary.

## 1. Prime logarithms have vanishing successive gaps

Let

\[
2=p_1<p_2<\cdots
\tag{15}
\]

be the rational primes. The prime number theorem, in the equivalent form

\[
p_n\sim n\log n,
\tag{16}
\]

implies

\[
\frac{p_{n+1}}{p_n}\longrightarrow1.
\tag{17}
\]

Therefore

\[
\boxed{
\log p_{n+1}-\log p_n
=\log\frac{p_{n+1}}{p_n}
\longrightarrow0.
}
\tag{18}
\]

This elementary consequence is the only arithmetic distribution input needed below. No prime-tuple theorem, short-interval estimate with a shrinking relative window, or equidistribution theorem for primes is required.

## 2. Any unbounded sequence with vanishing gaps is tail-dense modulo a fixed period

Let `x_n` be strictly increasing, unbounded, and satisfy

\[
x_{n+1}-x_n\to0.
\tag{19}
\]

Fix a period `L>0`, a residue target `a in R/LZ`, and `epsilon>0`. Choose a real representative `a_0`. For each sufficiently large integer `k`, let `n(k)` be the first index with

\[
x_{n(k)}\ge a_0+kL.
\tag{20}
\]

Then

\[
0\le x_{n(k)}-(a_0+kL)
\le x_{n(k)}-x_{n(k)-1}.
\tag{21}
\]

The right-hand side tends to zero as `k->infinity`. Hence, for arbitrarily large indices,

\[
\operatorname{dist}_{\mathbb R/L\mathbb Z}(x_n,a)<\epsilon.
\tag{22}
\]

So every tail of `{x_n mod L}` is dense in `R/LZ`.

Applying this to

\[
x_n=\log p_n,
\qquad
L=\frac{2\pi}{|\tau|},
\tag{23}
\]

and using `(18)` shows that

\[
\{p^{-i\tau}:p>X\text{ prime}\}
\tag{24}
\]

is dense in `S^1` for every `X`.

This is a tail statement. The approximation can always be performed beyond any finite set of already-used primes.

## 3. Coordinatewise tail density gives the full prime-support torus

Fix a target point

\[
Z^*=(\zeta_1,\ldots,\zeta_m)\in(S^1)^m
\tag{25}
\]

and a product neighborhood

\[
U=U_1\times\cdots\times U_m
\tag{26}
\]

of `Z^*`.

Choose `p_1>X` with `p_1^{-i\tau}\in U_1`. Having chosen distinct primes `p_1,...,p_{j-1}`, increase the cutoff beyond all of them and use the tail density `(24)` to choose a new prime `p_j` whose phase lies in `U_j`. After `m` steps,

\[
(p_1^{-i\tau},\ldots,p_m^{-i\tau})\in U
\tag{27}
\]

with all coordinates supplied by distinct rational primes larger than `X`.

Every basic neighborhood of every torus point therefore meets `\mathcal P_{m,\tau}(X)`, proving `(2)`.

The use of independently selected prime coordinates is essential. No simultaneous prime-pattern conjecture is hidden here: the coordinates are constrained only to be distinct primes, not consecutive primes, fixed translates, or values of one shared polynomial pattern.

## 4. Continuous finite-phase observables inherit the ambient closure

Let `C:(S^1)^m->Y` be continuous with `Y` Hausdorff. For any `Z in (S^1)^m`, density `(2)` supplies prime-source points `Z_n->Z`. Hence

\[
C(Z_n)\to C(Z),
\tag{28}
\]

so

\[
C((S^1)^m)
\subseteq
\overline{C(\mathcal P_{m,\tau}(X))}.
\tag{29}
\]

The reverse inclusion follows because the torus is compact, so `C((S^1)^m)` is compact and therefore closed in a Hausdorff target. This proves `(4)`.

This is the general Arithmetic Fidelity statement. If the support may vary without a retained support-scale or provenance restriction, **continuous phase-level observation cannot topologically separate rational-prime source configurations from the ambient finite torus**. The source remains discrete before phase projection, but its projected union has the largest possible closure.

## 5. AF-322's fixed-support modulus cannot be made support-uniform

Take `m=8`. The set `A_8` is nonempty; for example every regular octagon lies in it. Fix `Z^* in A_8`. By `(2)`, for every `epsilon>0` there is an eight-prime support `P` with all primes beyond any prescribed cutoff and

\[
\operatorname{dist}(Z_P(\tau),Z^*)<\epsilon.
\tag{30}
\]

Therefore

\[
\delta_P(\tau)
=\operatorname{dist}(Z_P(\tau),A_8)
\le
\operatorname{dist}(Z_P(\tau),Z^*)
<\epsilon,
\tag{31}
\]

which proves `(6)`.

AF-322 remains fully valid: for each **fixed** `P`, Baker-type lower bounds supply constants `c_P,kappa_P>0` with a polynomial exclusion tube in the time height. AF-323 says those constants must degenerate along some sequence of supports. Their support dependence encodes real arithmetic geometry; it cannot be removed by sharpening the same fixed-support argument.

In particular, a support-uniform theorem now has to retain or control an additional source scale — for example a norm-height parameter, a restricted support family, or some stronger exact arithmetic condition. Time height alone is insufficient.

## 6. Actual prime supports approach the AF-321 collision fiber

For the regular octagon `(8)`, the geometric sum gives

\[
\sum_{k=0}^7\omega^{kr}=0
\qquad(1\le r\le7),
\tag{32}
\]

which proves `(10)`. Its product is

\[
\prod_{k=0}^7\rho\omega^k
=
\rho^8\omega^{28}
=-\rho^8,
\tag{33}
\]

proving `(11)`.

As `rho` ranges over `S^1`, `-rho^8` ranges over all of `S^1`. For a chosen `eta`, pick `rho` with

\[
-\rho^8=\eta.
\tag{34}
\]

Apply `(2)` to the target `R_rho`, with shrinking neighborhoods and an increasing prime cutoff. This produces pairwise-distinct eight-prime supports `P_n` tending in phase space to `R_rho`. Continuity of every power sum and of the product gives `(12)`.

Now choose two target phases, for example `eta_+=1` and `eta_-=-1`, and corresponding support sequences `P_n^+` and `P_n^-`. Then

\[
\|H_7(Z_{P_n^+}(\tau))-H_7(Z_{P_n^-}(\tau))\|
\longrightarrow0,
\tag{35}
\]

while

\[
|E(Z_{P_n^+}(\tau))-E(Z_{P_n^-}(\tau))|
\longrightarrow2.
\tag{36}
\]

A uniformly continuous exact decoder `(13)--(14)` would send the left-hand convergence to zero on the product side, contradicting `(36)`.

This strengthens the interpretation of AF-321 in one specific direction. AF-321 used exact rank-one matched controls to approach the regular-octagon collision. AF-323 shows that, once support variation is admitted, the **actual rational-prime source family itself** approaches the same collision at any prescribed nonzero clock time. What remains special to the prime source is therefore not a support-uniform open neighborhood in phase space.

## 7. Relation to AF-309 and the exact-incidence frontier

AF-309 proves that exact-zero incidence is dense and measure-zero in the ambient continuous frequency-difference space: near a fixed prime-log vector one can perturb frequencies to both exact-hit and exact-safe controls. Those nearby controls need not themselves be prime logarithms.

AF-323 is orthogonal. It keeps the time fixed, keeps every coordinate inside the exact rational-prime source class, and instead lets the discrete support escape through the prime tail. Under that operation the source image becomes dense in phase space.

Together the two results isolate two different kinds of instability:

- **frequency-space instability at fixed source location:** exact incidence has no open ambient neighborhood (AF-309);
- **support-uniform phase-space instability inside the prime source class:** varying actual prime supports approximates every finite phase geometry (AF-323).

Neither instability decides whether one specified support has an exact hit. In particular, `(2)` does not imply that any prime support lies exactly on `A_8` or exactly satisfies the middle-singular system

\[
s_1=0,
\qquad
e_4=0.
\tag{37}
\]

The live AF-322 incidence question therefore survives, but in a sharper form: if exact middle-singular prime hits have stronger support-uniform behavior, that strength must come from **exact incidence arithmetic** or an explicitly retained support resource. It cannot be inherited from a support-uniform continuous neighborhood of the rational-prime phase source.

## Prior art and novelty assessment

No broad novelty claim is made. The arithmetic input is the classical prime number theorem, specifically the standard equivalent asymptotic `p_n~n log n`; see NIST DLMF §27.2 and §27.12. The implication `log p_{n+1}-log p_n->0`, the tail-density lemma modulo a fixed period, the coordinatewise product-density argument, and the continuous-image corollary are elementary consequences assembled here for the Arithmetic Fidelity question.

A targeted literature search also encountered work on logarithmic/digital distributions of primes and Benford-type questions, but none is needed for the theorem: `(2)` does not assert equidistribution or a limiting phase law. Density follows already from the prime number theorem, and the proof deliberately avoids importing a stronger distribution statement.

The durable contribution here is the **category boundary**, not a claimed new theorem about the primes: fixed-support Diophantine separation and support-uniform phase separation are fundamentally different resources. AF-322 establishes the former; AF-323 rules out the latter for unrestricted finite rational-prime supports.

Primary literature anchor used:

- NIST Digital Library of Mathematical Functions, §27.2 “Functions” and §27.12 “Asymptotic Formulas: Primes,” especially the prime-number-theorem asymptotic `p_n~n log n`: https://dlmf.nist.gov/27.2 and https://dlmf.nist.gov/27.12.

## Boundaries and failure modes

- `tau=0` is excluded. At zero time every prime phase equals `1`, so `(2)` is false.
- The support is allowed to vary over arbitrary distinct rational primes. The theorem does not claim density for the first `m` primes, consecutive-prime blocks, a bounded support set, or another rigidly coupled support family.
- The result is tail-dense, not quantitatively equidistributed. It provides no useful approximation rate as a function of the largest selected prime.
- The result concerns continuous finite-phase observables. Exact/discontinuous arithmetic predicates can still distinguish rational-prime provenance.
- Density gives arbitrarily accurate approximation, not exact incidence. It does not create an exact prime regular octagon, exact antipodal pairing, exact center, or exact middle-singular hit.
- The no-uniform-decoder conclusion `(13)--(14)` is over the union of unrestricted eight-prime supports at fixed time. It does not by itself rule out a stable decoder after restricting to an exact incidence subset such as `s_1=e_4=0`; that subset remains arithmetically unresolved.
- A stability modulus that explicitly depends on support scale, support geometry, or the individual primes is not contradicted. AF-322 is exactly of that type.
- Relabelling the prime coordinates changes the labelled torus point but does not affect the density statement or the symmetric harmonic corollaries.