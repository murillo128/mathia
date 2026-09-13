# AF-317 — Antipodal extension recursion breaks six-point singular rigidity at eight points

**Status:** `EXACT-DERIVED`, `STRUCTURAL-OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `SELF-INVERSIVE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-315 excludes the six-prime low-harmonic singularity by a strong geometric accident: for six centered unit phases, vanishing of the middle elementary coefficient `e_3` makes the entire root polynomial even, so the phases split into three antipodal pairs. AF-310 then rules that geometry out for a common nonzero rational-prime time because it forces more than one independent integer-character relation.

That mechanism does **not** persist at the next even support.

Let

\[
B=\{b_1,\ldots,b_{2m-2}\}\subset S^1,
\qquad
\sum_{j=1}^{2m-2}b_j=0,
\]

write `e_k(B)` for its elementary symmetric functions and

\[
E_B=e_{2m-2}(B)=\prod_j b_j.
\]

For any `a\in S^1`, append one antipodal pair

\[
Z=B\sqcup\{a,-a\}.
\]

Then `Z` is centered and its middle coefficient satisfies the exact recursion

\[
\boxed{
 e_m(Z)=E_B\,\overline{e_{m-2}(B)}-a^2e_{m-2}(B).
}
\tag{1}
\]

Hence, if `c=e_{m-2}(B)\ne0`, the unique antipodal pair orientation modulo `a\mapsto-a` that lands in the middle-singular stratum is

\[
\boxed{
 a^2=E_B\frac{\overline c}{c}\in S^1.
}
\tag{2}
\]

If `c=0`, then self-inversivity also gives `e_m(B)=0`, and **every** appended antipodal pair has `e_m(Z)=0`.

This recursion explains why six points are misleading. For `m=3`, the lower configuration has four centered unit points and `c=e_1(B)=0` automatically; every such four-point configuration is already two antipodal pairs, so adding a third pair produces exactly the even-polynomial geometry used in AF-315. At eight points (`m=4`), the lower six-point centered configuration can instead have `e_2(B)\ne0` and need not be antipodally invariant. Equation (2) then produces an eight-point middle-singular configuration without forcing the full root set to be invariant under `z\mapsto-z`.

In fact there is an explicit centered eight-point example with

\[
e_4(Z)=0,
\qquad e_3(Z)\ne0,
\]

so its root polynomial is not even; moreover the configuration is nontorsion. Therefore the implication

\[
\text{middle coefficient vanishes}
\Longrightarrow
\text{torsion / global antipodal symmetry}
\]

is false already at support eight.

Consequently, the AF-315 proof that removes the six-point singular harmonic stratum cannot be extrapolated to eight or higher even support using only unit-circle self-inversivity and cyclotomic/antipodal geometry. Any exclusion of the `e_m=0` stratum for a hypothetical even rational-prime hit from eight points onward needs additional source-specific arithmetic information, or the recovery map must retain an extra mark such as the total product phase rather than assuming the singular set is automatically torsion.

## 1. The antipodal-extension identity

Let

\[
P_B(w)=\prod_{j=1}^{2m-2}(w-b_j)
      =\sum_{k=0}^{2m-2}(-1)^k e_k(B)w^{2m-2-k}.
\tag{3}
\]

Appending `a,-a` gives

\[
P_Z(w)=(w^2-a^2)P_B(w).
\tag{4}
\]

The coefficient of `w^m` in `(4)` receives exactly two contributions. The `w^2P_B` term contributes `(-1)^m e_m(B)`, while the `-a^2P_B` term contributes

\[
-a^2(-1)^{m-2}e_{m-2}(B)
=(-1)^m\bigl(-a^2e_{m-2}(B)\bigr).
\]

Therefore

\[
\boxed{
 e_m(Z)=e_m(B)-a^2e_{m-2}(B).
}
\tag{5}
\]

Because every `b_j` lies on the unit circle, the coefficient system of `P_B` is self-inversive:

\[
 e_{2m-2-k}(B)=E_B\,\overline{e_k(B)}.
\tag{6}
\]

Taking `k=m-2` gives

\[
 e_m(B)=E_B\,\overline{e_{m-2}(B)}.
\tag{7}
\]

Substituting `(7)` into `(5)` proves `(1)`. If `c\ne0`, then

\[
\left|E_B\frac{\overline c}{c}\right|=1,
\]

so a unit-modulus square root exists and `(2)` is both necessary and sufficient for `e_m(Z)=0`. If `c=0`, equation `(7)` gives `e_m(B)=0`, and `(5)` vanishes for every `a`.

Thus the middle-singular locus has a recursive source: centered `(2m-2)`-point configurations can be lifted into centered `2m`-point configurations by adding one suitably oriented antipodal pair.

## 2. The recursion is populated in every higher even degree

For every `m\ge4`, take `B` to be the disjoint union of a rotated regular `(m-2)`-gon and a rotated regular `m`-gon. Equivalently, for arbitrary `A,C\in S^1`, let

\[
P_B(w)=(w^{m-2}-A)(w^m-C).
\tag{8}
\]

Both blocks are centered because their sizes are at least two, so `B` is centered. Expanding `(8)` gives

\[
P_B(w)=w^{2m-2}-A w^m-C w^{m-2}+AC.
\tag{9}
\]

Hence `e_{m-2}(B)` and `e_m(B)` are both nonzero and their ratio is

\[
\frac{e_m(B)}{e_{m-2}(B)}=\frac CA.
\tag{10}
\]

Choosing `a^2=C/A` in `(4)` therefore gives a centered `2m`-point configuration with `e_m=0`.

This block example is deliberately only an existence check; it carries obvious torsion inside the regular polygons. Its role is to show that the recursive middle-singular mechanism is present for every even support `2m\ge8`, not to model a rational-prime phase tuple.

## 3. Eight points already admit a nontorsion, non-antipodal singular configuration

The stronger failure of six-point rigidity occurs already for `m=4`.

Set

\[
x=\frac{-1+2i\sqrt2}{3},
\qquad
y=\frac{1+i\sqrt{35}}6,
\qquad
\eta=e^{i\pi/3}=\frac{1+i\sqrt3}{2}.
\tag{11}
\]

All three numbers have unit modulus. Define the six-point multiset

\[
B=
\{1,x,\overline x,-y\eta,-y\overline\eta,-\overline y\}.
\tag{12}
\]

It is centered. Indeed,

\[
1+x+\overline x=\frac13,
\]

while `\eta+\overline\eta=1` and `y+\overline y=1/3`, so

\[
y\eta+y\overline\eta+\overline y
=y+\overline y
=\frac13.
\]

Thus the last three entries of `(12)` sum to `-1/3`.

Direct symmetric-function calculation gives

\[
 e_2(B)=\frac{5+i\sqrt{35}}{18},
\qquad
 e_3(B)=\frac{20-4i\sqrt{35}}{27},
\qquad
 E_B=-y.
\tag{13}
\]

In particular `e_2(B)\ne0` and `e_3(B)\ne0`. Self-inversivity gives `e_4(B)=E_B\overline{e_2(B)}`, and here

\[
\frac{\overline{e_2(B)}}{e_2(B)}=-y.
\tag{14}
\]

Therefore

\[
\frac{e_4(B)}{e_2(B)}
=E_B\frac{\overline{e_2(B)}}{e_2(B)}
=y^2.
\tag{15}
\]

Choose the appended antipodal pair to be `{y,-y}` and set

\[
Z=B\sqcup\{y,-y\}.
\tag{16}
\]

Equation `(5)` with `m=4` now gives

\[
 e_4(Z)=e_4(B)-y^2e_2(B)=0.
\tag{17}
\]

But the third coefficient is unchanged because `e_1(B)=0`:

\[
 e_3(Z)=e_3(B)-y^2e_1(B)
       =\frac{20-4i\sqrt{35}}{27}
e0.
\tag{18}
\]

A root multiset invariant under `z\mapsto-z` has an even monic root polynomial. Equation `(18)` shows that the degree-eight root polynomial of `Z` has a nonzero odd-power coefficient, so `Z` is **not** globally antipodally invariant. Concretely, `1\in Z` while `-1\notin Z`.

The same example is nontorsion. The phase `x` satisfies the irreducible quadratic

\[
3x^2+2x+3=0.
\tag{19}
\]

Its monic minimal polynomial over `\mathbb Q` is therefore

\[
w^2+\frac23w+1,
\]

which is not integral. Hence `x` is not an algebraic integer, while every root of unity is an algebraic integer. Thus `x` is not a root of unity. Since `1` and `x` both occur in `Z`, the normalized configuration is not a torsion point of the phase torus.

This is the exact distinction needed after AF-310: the eight-point middle-singular stratum is not confined to the torsion regime that prime-log arithmetic automatically excludes.

## 4. Why six points are exceptional

For six points, `m=3` and the lower configuration `B` has four unit points. Centering gives

\[
e_1(B)=0,
\]

and self-inversivity gives `e_3(B)=E_B\overline{e_1(B)}=0`. Therefore `(5)` yields `e_3(Z)=0` for **every** appended antipodal pair.

But a centered four-point unit configuration is necessarily two antipodal pairs. Consequently every configuration produced by the recursion is three antipodal pairs, and AF-315 proves the converse directly from the even degree-six polynomial. The singular stratum and the antipodal-pairing stratum coincide.

At eight points the lower centered object has six phases. Centering only forces `e_1=e_5=0`; it does not force `e_2` or `e_3` to vanish. The antipodal-extension equation can therefore kill the middle coefficient `e_4` while leaving `e_3\ne0`, as `(12)`–`(18)` show. The polynomial is no longer forced to contain only even powers.

So the six-point argument is not the first member of a stable even-support pattern. It is a low-degree coincidence in which the centered coefficient pair `e_1,e_5` plus the middle condition `e_3=0` exhaust all odd coefficients.

## Arithmetic-fidelity consequence

For a hypothetical exact rational-prime hit with even support `n=2m`, AF-316 uses the middle relation

\[
e_m=E\overline{e_m}
\]

to recover the total product phase `E` from the low harmonics whenever `e_m\ne0`. The unresolved exceptional set is precisely `e_m=0`.

AF-315 showed that for six primes the exceptional set is source-impossible because `e_3=0` forces several antipodal relations. AF-317 shows why that source-specific closure cannot simply be inherited by eight primes: already in the ambient centered unit-circle geometry, `e_4=0` contains nontorsion configurations with no global antipodal symmetry.

The next decisive arithmetic question is therefore sharper than “does the singular coefficient vanish?”:

> Can the eight-point centered singular variety `e_4=0` contain a configuration whose normalized integer-character relation lattice has rank at most one, as required by AF-310 for a common nonzero rational-prime time?

AF-317 does **not** answer that question. The explicit example above is only a nontorsion/non-antipodal witness; it may still carry additional exact character relations. What it proves is that any rank-two exclusion, if true, must use structure finer than global torsion or the even-polynomial argument.

This separates two obstructions that were accidentally identical at six points:

1. **recovery singularity:** the self-inversive middle coefficient vanishes, so the simple phase-recovery formula for `E` disappears;
2. **arithmetic inadmissibility:** the phase geometry forces too many integer-character relations for a prime-log orbit.

At six points `(1)` implies `(2)`. At eight points AF-317 proves that the elementary symmetry route from `(1)` to `(2)` has broken.

## Prior art and novelty assessment

No novelty is claimed for self-inversive coefficient reciprocity, elementary symmetric functions, or multiplication by an antipodal factor `w^2-a^2`.

- Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, London Mathematical Society Lecture Note Series 352, Cambridge University Press (2010), pp. 312–321, DOI `10.1017/CBO9780511721274.020`, is standard prior art for unit-circle/self-inversive polynomial structure.
- Kathleen L. Petersen and Christopher D. Sinclair, **“Conjugate Reciprocal Polynomials with All Roots on the Unit Circle,”** *Canadian Journal of Mathematics* 60(5) (2008), 1149–1167, DOI `10.4153/CJM-2008-050-8`, studies the coefficient-space geometry/topology of conjugate-reciprocal polynomials with all roots on the circle.

A targeted literature search for the particular “centered middle coefficient + antipodal extension” recursion did not identify a standard named theorem, but that is not evidence of novelty and none is claimed. Equation `(5)` is a direct coefficient identity. The durable Arithmetic Fidelity contribution is the **boundary diagnosis** relative to AF-310, AF-315, and AF-316: the six-point singularity is cyclotomically rigid for an accidental low-degree reason, while the first higher even case already contains exact nontorsion, non-antipodal singular geometry.

## Boundaries and failure modes

- The explicit eight-point witness does not prove that a rational-prime common-time orbit hits `e_4=0`, or even that the singular variety contains a point with character-relation rank at most one.
- “Nontorsion” here means the normalized phase tuple is not a torsion point. It does **not** mean the example has no torsion subrelations. The construction deliberately contains an appended antipodal pair, so at least one torsion character relation is present.
- Equation `(2)` gives the pair orientation only modulo `a\mapsto-a`, which leaves the unordered antipodal pair unchanged.
- The recursive family need not exhaust the full `e_m=0` stratum for `m\ge4`; it is an explicit embedded source of singular configurations.
- The regular-block family `(8)`–`(10)` is a structural existence control, not a prime-like model; its internal root-of-unity relations make it unsuitable as evidence of arithmetic incidence.
- The result concerns exact unit-circle phase geometry. It supplies no conditioning estimate near `e_m=0`; AF-316's separate stability question remains open.
- The result does not show that low harmonics fail to recover every point of the singular stratum by some alternative nonlinear rule. It shows only that the self-inversive middle-coefficient shortcut for recovering `E` degenerates there and that the six-point torsion exclusion cannot be generalized by the same symmetry argument.
- Nothing here supplies a zeta zero, analytic continuation mechanism, explicit-formula sign theorem, or RH implication.

## Consequence for the research line

AF-316 isolated `e_m=0` as the unresolved even-support recovery stratum. AF-317 now removes the simplest possible way to dismiss that stratum beyond six points.

The useful split is:

\[
\boxed{
\text{middle singularity}
\not\Rightarrow
\text{torsion or global antipodal symmetry}
\quad\text{from support }8.
}
\]

Accordingly, future even-support work should stop treating the six-point `e_3=0` exclusion as representative. The mathematically decisive next gate is whether the first higher singular variety forces **two independent character relations** despite being nontorsion, or whether it already contains relation-rank-`0/1` points compatible with AF-310. Only after that gate is settled does it make sense to ask whether the specific rational-prime flow can hit the surviving stratum.