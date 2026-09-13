# AF-307 — Small saturated prime supports split exact zero fidelity from stable margin

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SATURATED-DISCRETE-SOURCES`, `KRONECKER-WEYL`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-306 shows that saturation `k alpha=1` removes coefficient freedom but does not restore a positive zero margin. On the imaginary axis the remaining **exact** point-zero problem has a sharper, cardinality-sensitive structure.

For a finite set `A` of distinct rational primes, write

\[
P_A(s)=\frac1{|A|}\sum_{p\in A}p^{-s}.
\tag{1}
\]

Then:

1. for every fixed `k>=2` and every fixed `k`-prime support `A`,
   \[
   \inf_{t\in\mathbb R}|P_A(it)|=0,
   \tag{2}
   \]
   with values arbitrarily close to zero at arbitrarily large positive heights;
2. for `k=2`, every support has exact imaginary-axis zeros, and the saturated class already admits a same-deletion-fiber zero/safe collision at one common height;
3. for `k=3`, AF-306 proves that no support has an exact imaginary-axis zero;
4. for `k=4`, no support has an exact imaginary-axis zero either.

Consequently, on saturated equal-weight rational-prime sources at `Re(s)=0`, exact point-zero fidelity and stable zero-margin fidelity are qualitatively different resources. Stable margin collapses for every `k>=2`, while exact zeros occur for `k=2` but are arithmetically forbidden for `k=3,4`.

In particular, the exact discriminator can become **vacuously faithful** after saturation: for `k=3,4` the binary predicate `P_A(it)=0` is identically false on the whole source class, even though its normalized distance to failure has infimum zero for every fixed support. This is not evidence that the compression has retained useful zero-sensitive information.

The first unresolved saturated cardinalities on the imaginary axis are therefore `k>=5`.

## Every fixed saturated support has zero margin

Let

\[
A=\{p_1,\ldots,p_k\},\qquad k\ge2,
\]

with distinct rational primes. Unique factorization implies that

\[
\log p_1,\ldots,\log p_k
\]

are linearly independent over `Q`: a nonzero integer relation would exponentiate to a nontrivial multiplicative relation among distinct primes.

The continuous Kronecker-Weyl theorem therefore makes the orbit

\[
t\longmapsto
\bigl(p_1^{-it},\ldots,p_k^{-it}\bigr)
\tag{3}
\]

dense in the full torus `T^k`. Let

\[
\zeta_j=e^{2\pi i(j-1)/k},
\qquad 1\le j\le k,
\]

so that

\[
\sum_{j=1}^k\zeta_j=0.
\tag{4}
\]

For every `epsilon>0` and every `H>0`, density and recurrence give a `t>H` with all `p_j^{-it}` arbitrarily close to the corresponding `zeta_j`. Hence

\[
|P_A(it)|<\epsilon.
\tag{5}
\]

This proves (2) for every fixed saturated support, not merely after changing the support with `epsilon` as in the family-level construction of AF-306.

Equation (2) says nothing about whether the infimum is attained. That exact-attainment question is where the small cardinalities separate.

## Two primes: exact saturated collision survives

Let

\[
A=\{p,q\},\qquad p\ne q.
\]

Then

\[
P_A(it)=0
\]

if and only if the two unit phases are antipodal:

\[
(q/p)^{-it}=-1.
\]

Thus the exact zero heights are

\[
t_m=\frac{(2m+1)\pi}{\log(q/p)},
\qquad m\in\mathbb Z,
\tag{6}
\]

with the sign of the denominator fixing the orientation of the progression.

This already produces an exact same-fiber failure for the saturated `k=2` class. Choose four distinct primes `p,q,r,s`, put

\[
A=\{p,q\},\qquad B=\{r,s\},
\]

and take

\[
t=\frac{\pi}{\log(q/p)}.
\tag{7}
\]

Then `P_A(it)=0`. If `P_B(it)=0` also held, there would be an integer `n` such that

\[
t\log(s/r)=(2n+1)\pi.
\]

Combining with (7) would give

\[
\frac{\log(s/r)}{\log(q/p)}=2n+1\in\mathbb Q.
\tag{8}
\]

After clearing denominators, (8) exponentiates to a nontrivial multiplicative relation among the four distinct primes, impossible by unique factorization. Therefore

\[
P_A(it)=0,
\qquad
P_B(it)\ne0.
\tag{9}
\]

Delete all coordinates in `A union B`. The two uniform two-point sources then have the same retained state `0` but different exact point-zero values at the common height `t`. Saturation therefore does **not** repair exact deletion fidelity at `k=2`.

## Four unit phases summing to zero must pair antipodally

The new exact ingredient for `k=4` is elementary but decisive.

Let

\[
z_1,z_2,z_3,z_4\in\mathbb C,
\qquad |z_j|=1,
\qquad z_1+z_2+z_3+z_4=0.
\tag{10}
\]

Set

\[
u=z_1+z_2=-(z_3+z_4).
\]

If `u=0`, then `z_2=-z_1` and also `z_4=-z_3`, so the four phases already split into two antipodal pairs.

Assume `u\ne0`. Because `|z_1|=|z_2|=1`,

\[
\overline u
=z_1^{-1}+z_2^{-1}
=\frac{u}{z_1z_2},
\]

hence

\[
z_1z_2=\frac{u}{\overline u}.
\tag{11}
\]

Applying the same identity to `z_3+z_4=-u` gives

\[
z_3z_4=\frac{-u}{-\overline u}
=\frac{u}{\overline u}.
\tag{12}
\]

Therefore `z_3,z_4` are the two roots of

\[
x^2+ux+\frac{u}{\overline u}=0.
\tag{13}
\]

But `-z_1,-z_2` have the same sum `-u` and the same product `z_1z_2=u/\overline u`, so they are the same unordered root pair. Thus

\[
\boxed{
\{z_3,z_4\}=\{-z_1,-z_2\}
}
\tag{14}
\]

after a suitable relabelling. Every zero-sum quadruple of unit complex numbers consists of two antipodal pairs.

## Four distinct prime phases cannot realize both antipodal pairs

Take four distinct rational primes

\[
A=\{p_1,p_2,p_3,p_4\}
\]

and suppose for contradiction that

\[
P_A(it)=0
\tag{15}
\]

for some real `t`. Equation (15) cannot hold at `t=0`, so `t\ne0`.

By (14), after relabelling the primes there are two antipodal phase pairs:

\[
p_2^{-it}=-p_1^{-it},
\qquad
p_4^{-it}=-p_3^{-it}.
\tag{16}
\]

Hence for some integers `m,n`,

\[
t\log(p_2/p_1)=(2m+1)\pi,
\qquad
t\log(p_4/p_3)=(2n+1)\pi,
\tag{17}
\]

up to the harmless common sign convention from the ordering of each pair. Dividing the two nonzero equations yields

\[
\frac{\log(p_2/p_1)}{\log(p_4/p_3)}
=\frac{2m+1}{2n+1}
\in\mathbb Q.
\tag{18}
\]

Clearing denominators in (18) and exponentiating produces a multiplicative relation between the disjoint prime ratios `p_2/p_1` and `p_4/p_3`. Unique factorization forces every prime exponent in that relation to vanish, contradicting the nonzero odd integers in (17).

Therefore

\[
\boxed{
P_A(it)\ne0
\quad\text{for every real }t
}
\tag{19}
\]

for every four-element rational-prime support `A`.

Combined with (2), this gives

\[
\boxed{
Z_A:=\{t\in\mathbb R:P_A(it)=0\}=\varnothing,
\qquad
\inf_t |P_A(it)|=0
}
\tag{20}
\]

for every saturated four-prime source. AF-306 established the same empty-zero-set / zero-margin dichotomy for `k=3`.

## Prior art and novelty assessment

No novelty claim is made for the ingredients or for the general exponential-sum setting.

- Alexandre Bailleul, *Explicit Kronecker-Weyl theorems and applications to prime number races*, **Research in Number Theory** 8 (2022), Article 43, DOI `10.1007/s40993-022-00349-2`, gives modern continuous and discrete Kronecker-Weyl formulations. The present use is the classical continuous torus-density consequence for rationally independent prime logarithms.
- J. M. Sepulcre, *On the Result of Invariance of the Closure Set of the Real Projections of the Zeros of an Important Class of Exponential Polynomials*, **Journal of Function Spaces** 2016, Article 3605690, DOI `10.1155/2016/3605690`, places rationally independent exponential-polynomial frequencies in established zero-location theory and recalls Moreno's criterion for zeros arbitrarily close to vertical lines. This prior art is especially relevant to the distinction here: closure/near-zero geometry does not decide whether the original one-parameter line hits zero exactly.
- Janne Heittokangas, Katsuya Ishizaki, Kazuya Tohge, and Zhi-Tao Wen, *Value distribution of exponential polynomials and their role in the theories of complex differential equations and oscillation theory*, **Bulletin of the London Mathematical Society** 55(1) (2023), 1–77, DOI `10.1112/blms.12719`, surveys the century-old zero theory of exponential sums and explicitly includes finite Dirichlet sums as exponential sums.
- The four-unit-phase antipodal lemma is elementary circle geometry/algebra, and the rational independence of logarithms of distinct rational primes is an immediate consequence of unique factorization.

A targeted literature search found broad classical and modern theories of exponential-sum zeros, almost-periodic value closure, and rationally independent frequencies, but no reason to treat the small rational-prime specialization (19) as a new theorem. Its durable role here is instead the Arithmetic Fidelity boundary: **near-zero accessibility survives while exact zero membership changes discontinuously with the discrete source class**.

## Boundaries and failure modes

- The zero-free conclusions for `k=3,4` are specific to equal weights on the imaginary axis. They do not imply zero-freeness for `sigma\ne0`, unequal coefficients, repeated coordinates, or a different nonlinear observation.
- The `k=4` proof uses distinct rational primes critically. Generic four-frequency exponential sums can have exact zeros; the obstruction comes from the multiplicative independence of the two prime ratios forced by antipodal pairing.
- Equation (2) is an approximation statement from torus density. It does not imply exact zero attainment for `k>=5`.
- For `k=2`, the same-fiber collision uses deletion of the complete supports. A compression retaining a compulsory common coordinate has different fiber geometry and must be audited separately.
- For `k=3,4`, exact point-zero recovery under arbitrary compression is vacuous because the target is constant false on this restricted source class. It must not be advertised as preservation of a useful arithmetic discriminator.
- The result concerns a pointwise imaginary-axis zero predicate for finite equal-weight prime Dirichlet polynomials. It does not establish a zeta zero count, analytic continuation, a global RH criterion, or a transfer theorem for the Riemann zero divisor.

## Consequence for the research line

The saturation frontier now has a first exact classification on `Re(s)=0`:

- `k=2`: exact zero/safe same-fiber collisions exist;
- `k=3`: no exact zeros, but zero margin, by AF-306;
- `k=4`: no exact zeros, but zero margin, by (19)–(20);
- `k>=5`: exact attainment remains open, while stable margin is already known to collapse.

This removes `k=4` from the live exact-collision search and exposes a stronger audit rule. A downstream RH argument cannot count "the exact discriminator survives" as meaningful unless the discriminator is nontrivial on the admissible source class. Exact factorization may arise either because the compression retained the needed structure or because the source geometry made the bad event impossible. Those cases have opposite implications for robustness.

The next honest saturated-source question is therefore `k>=5` (or `sigma\ne0`) together with an explicit non-vacuity check: first determine whether the source class contains both zero and safe instances at the same information layer, then ask whether the compression distinguishes them. Stable transfer needs a separate positive margin and is already ruled out by saturation alone.