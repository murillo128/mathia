# AF-501 — Source saturation and finite-dimensional fibers separate quotient-compactness failures

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NUISANCE-QUOTIENT`, `SATURATION`, `MEASURE-OF-NONCOMPACTNESS`, `MINIMAL-LIFT`, `ORDER-OF-OPERATIONS`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-500 shows that raw tail compactness and post-quotient tail compactness can disagree in either direction. The two failures have different causes. One is caused by **new bounded aliases becoming admissible only after quotienting**; the other is caused by **noncompact motion inside the fibers that the quotient deliberately forgets**.

These mechanisms can be separated exactly.

Let `Y` be a Banach space, let `V subset Y` be a closed linear subspace, and write

\[
\pi:Y\to Q:=Y/V.
\]

Let `C subset Y` be nonempty, put `D:=\overline C`, fix `s in Y`, and write `\bar s=\pi(s)`. As in AF-499 and AF-500, define

\[
E^0_{T,R}(C,s)
:=
\bigcup_{t\ge T}
\bigl((D-ts)\cap \overline B_R^Y(0)\bigr),
\]

\[
D_V:=\overline{\pi(C)},
\qquad
E^V_{T,R}(C,s)
:=
\bigcup_{t\ge T}
\bigl((D_V-t\bar s)\cap \overline B_R^Q(0)\bigr),
\]

with tail Hausdorff noncompactness profiles

\[
\nu_C^0(s;R)
:=
\lim_{T\to\infty}\chi_Y(E^0_{T,R}),
\qquad
\nu_C^V(s;R)
:=
\lim_{T\to\infty}\chi_Q(E^V_{T,R}).
\]

Then:

1. **Raw contacts always map to quotient contacts.** For every `T,R`,

\[
\boxed{
\pi(E^0_{T,R})\subseteq E^V_{T,R}.
}
\]

2. **Saturation prevents quotienting from admitting genuinely new bounded aliases.** If the closed source is `V`-saturated,

\[
\boxed{D+V=D,}
\]

then `D_V=\pi(D)` and, for every `\varepsilon>0`,

\[
\boxed{
E^V_{T,R}
\subseteq
\pi(E^0_{T,R+\varepsilon}).
}
\]

Consequently

\[
\boxed{
\nu_C^V(s;R)
\le
\nu_C^0(s;R+\varepsilon)
\qquad(\varepsilon>0).
}
\]

If `V` is proximinal in `Y`, the radius inflation is unnecessary:

\[
\boxed{
E^V_{T,R}=\pi(E^0_{T,R}),
\qquad
\nu_C^V(s;R)\le\nu_C^0(s;R).
}
\]

Thus saturation removes AF-500's **false-certificate direction**: once all nuisance translates are already legitimate source states, compactness verified upstream at the relevant radius cannot be destroyed merely by forgetting the nuisance direction.

3. **Finite-dimensional fibers prevent quotient compactness from hiding raw noncompactness.** If

\[
\boxed{\dim V<\infty,}
\]

then for every `C,s,R`, with no saturation assumption,

\[
\boxed{
\nu_C^V(s;R)=0
\Longrightarrow
\nu_C^0(s;R)=0.
}
\]

Moreover finite dimensionality is the exact universal condition behind this lifting property:

\[
\boxed{
\dim V<\infty
\iff
\bigl[
A\subset Y\text{ bounded and }\pi(A)\text{ relatively compact}
\Rightarrow
A\text{ relatively compact}
\bigr].
}
\]

4. Combining the two gates, if `D` is `V`-saturated and `V` is finite-dimensional, then `V` is proximinal and

\[
\boxed{
\nu_C^0(s;R)=0
\iff
\nu_C^V(s;R)=0
\qquad\text{for every }R<\infty.
}
\]

The two hypotheses are independently sharp as universal statements. AF-500's second Hilbert-sum example has one-dimensional `V` but a nonsaturated source and satisfies raw tail compactness while quotient tail compactness fails. Conversely, an infinite-dimensional `V` can defeat the reverse implication even for a fully `V`-saturated source.

The resulting structural decomposition is

\[
\boxed{
\text{alias admission is controlled by source saturation,}
\qquad
\text{compact lifting is controlled by nuisance-fiber compactness.}
}
\]

AF-500's noncommutation is therefore not one indivisible pathology. It is the superposition of two logically independent information-loss mechanisms.

## Saturation gives the correct quotient-truncation inclusion

The forward inclusion requires no hypothesis. If

\[
x=d-ts\in E^0_{T,R},
\]

then

\[
\pi(x)=\pi(d)-t\bar s,
\qquad
\|\pi(x)\|_Q\le\|x\|_Y\le R,
\]

and `\pi(d) in D_V`. Hence `\pi(x) in E^V_{T,R}`.

Now assume `D+V=D`. Because `D` is saturated for the quotient map,

\[
D=\pi^{-1}(\pi(D)).
\]

A saturated set is closed exactly when its image is closed in the quotient topology, so `\pi(D)` is closed. Continuity of `\pi` and density of `C` in `D` give

\[
D_V
=
\overline{\pi(C)}
=
\pi(D).
\]

Take any `\bar x in E^V_{T,R}`. Then for some `t>=T` and `d in D`,

\[
\bar x=\pi(d-ts),
\qquad
\|\bar x\|_Q\le R.
\]

By the quotient norm definition, for every `\varepsilon>0` there exists `v in V` with

\[
\|d-ts-v\|_Y\le R+\varepsilon.
\]

Saturation gives `d-v in D`, so

\[
x:=(d-v)-ts\in E^0_{T,R+\varepsilon}
\]

and `\pi(x)=\bar x`. Therefore

\[
E^V_{T,R}
\subseteq
\pi(E^0_{T,R+\varepsilon}).
\]

Since the quotient map is contractive, the Hausdorff measure of noncompactness cannot increase on a fixed bounded set:

\[
\chi_Q(\pi(A))\le\chi_Y(A).
\]

Taking tail limits proves

\[
\nu_C^V(s;R)
\le
\nu_C^0(s;R+\varepsilon).
\]

If `V` is proximinal, the quotient norm of every coset has a minimizing representative, so one can choose `v` with

\[
\|d-ts-v\|_Y=\|\pi(d-ts)\|_Q\le R.
\]

The reverse inclusion at the same radius follows, and therefore

\[
E^V_{T,R}=\pi(E^0_{T,R}).
\]

This identifies precisely what failed in AF-500's raw-compact/quotient-noncompact control. There the last coordinate was declared nuisance only after the source set had tied that coordinate rigidly to the integer index. Removing it in the quotient admitted bounded residuals for source states that had no bounded representative inside the original `C`. The source was not saturated under the nuisance equivalence.

## Finite-dimensional fibers are exactly the universal bounded-lifting gate

Assume `dim V<infinity`. Let `(x_n)` be any bounded sequence in `Y` such that `(\pi(x_n))` has a convergent subsequence. Relabel so that

\[
\pi(x_n)\to\pi(x)
\]

for some `x in Y`. Then

\[
\operatorname{dist}_Y(x_n-x,V)
=
\|\pi(x_n-x)\|_Q
\to0.
\]

Choose `v_n in V` with

\[
\|x_n-x-v_n\|_Y\to0.
\]

Because `(x_n)` is bounded, `(v_n)` is bounded. The closed bounded subsets of finite-dimensional `V` are compact, so after passing to a subsequence

\[
v_n\to v\in V.
\]

Hence

\[
x_n\to x+v
\]

in norm. Thus every bounded sequence whose quotient image is relatively compact is itself relatively compact.

Apply this to a raw radius-`R` tail sequence

\[
x_n=d_n-t_ns,
\qquad
 t_n\to\infty,
\qquad
\|x_n\|\le R.
\]

Its quotient sequence belongs to the quotient-visible radius-`R` tail. If `\nu_C^V(s;R)=0`, AF-499's sequential characterization in the Banach quotient `Q` gives a convergent quotient subsequence. The finite-dimensional lifting argument then gives a norm-convergent raw subsequence. AF-499's characterization in `Y` yields

\[
\nu_C^0(s;R)=0.
\]

The converse universal compact-lifting property forces finite dimensionality. If `V` is infinite-dimensional, its closed unit ball `B_V` is bounded and

\[
\pi(B_V)=\{0\}
\]

is compact, while `B_V` is not relatively compact by the classical Riesz finite-dimensional compactness criterion. Hence

\[
\bigl[
A\text{ bounded},\ \pi(A)\text{ relatively compact}
\Rightarrow A\text{ relatively compact}
\bigr]
\]

fails already on a single quotient fiber.

Finite dimensionality is therefore not an arbitrary sufficient assumption. It is exactly the condition under which **bounded motion hidden entirely inside a nuisance fiber is universally precompact**.

## Exact commutation when both resources are present

Suppose now that `D+V=D` and `dim V<infinity`.

Every finite-dimensional subspace of a Banach space is proximinal, so saturation gives the exact truncation identity

\[
E^V_{T,R}=\pi(E^0_{T,R}).
\]

If the raw tail is asymptotically compact, contractivity of `\pi` makes the quotient tail asymptotically compact. Conversely, if the quotient tail is asymptotically compact, finite-dimensional compact lifting makes every bounded raw residual sequence precompact. Hence

\[
\boxed{
\nu_C^0(s;R)=0
\iff
\nu_C^V(s;R)=0.
}
\]

This is the regime in which the order warning of AF-500 becomes unnecessary **for the zero/nonzero compactness gate itself**. One may test tail compactness either before or after quotienting and obtain the same yes/no answer.

The statement does not say that the two numerical measures of noncompactness are equal. Quotienting can still reduce distances and covering radii. What commutes is the property needed by AF-499: vanishing tail noncompactness, equivalently norm-precompactness of every bounded escaping residual sequence.

## Sharp controls separate the two hypotheses

### Finite-dimensional nuisance without saturation

AF-500 already supplies this control:

\[
Y=\mathbb R\oplus_2\ell^2\oplus_2\mathbb R,
\qquad
V=\{0\}\oplus\{0\}\oplus\mathbb R,
\qquad
s=(1,0,0),
\]

\[
C=\{(n,e_n,n):n\ge1\}.
\]

Here `dim V=1`, but `C` is not `V`-saturated. For every fixed finite `R`, the raw tail is eventually empty, so

\[
\nu_C^0(s;R)=0.
\]

After quotienting, however, the radius-`1` residuals contain the orthonormal family `(0,e_n)`, giving

\[
\nu_C^V(s;1)=1.
\]

Thus finite-dimensional nuisance fibers do not prevent the quotient from revealing new bounded aliases when the source model was not saturated under the nuisance equivalence.

### Saturation with an infinite-dimensional nuisance fiber

Let

\[
Y=\mathbb R\oplus_2\ell^2,
\qquad
V=\{0\}\oplus\ell^2,
\qquad
s=(1,0),
\]

and take the closed saturated source

\[
C=D=\mathbb N\times\ell^2.
\]

Then `D+V=D`. In the quotient `Q congruent R`,

\[
\pi(D)=\mathbb N,
\]

and for every `T` the quotient radius-`1` tail is the compact interval

\[
E^V_{T,1}=[-1,1].
\]

Therefore

\[
\boxed{\nu_C^V(s;1)=0.}
\]

But at every sufficiently large integer time `t=n`, the raw radius-`1` tail contains

\[
\{0\}\times\overline B_1^{\ell^2}(0).
\]

The unit ball of `ell^2` has Hausdorff measure of noncompactness `1`, so

\[
\boxed{\nu_C^0(s;1)=1.}
\]

The quotient correctly regards the whole `ell^2` direction as nuisance; upstream compactness fails only because that nuisance orbit itself contains infinitely many mutually separated bounded representatives. Saturation has removed the new-alias problem, but an infinite-dimensional fiber still creates a false raw obstruction.

These controls show that the two gates solve different halves of AF-500's bidirectional failure.

## Prior-art and novelty audit

No broad novelty is claimed for quotient norms, saturated subsets, proximinality, finite-dimensional compactness, or measures of noncompactness.

- Robert E. Megginson, *An Introduction to Banach Space Theory*, Graduate Texts in Mathematics 183, Springer (1998), DOI `10.1007/978-1-4612-0603-3`. Role: standard Banach quotient theory, quotient norms, finite-dimensional compactness, and the basic lifting framework used here.
- Ivan Singer, *Best Approximation in Normed Linear Spaces by Elements of Linear Subspaces*, Grundlehren der mathematischen Wissenschaften 171, Springer (1970), DOI `10.1007/978-3-662-41583-2`. Role: classical best-approximation/proximinality theory; finite-dimensional subspaces are proximinal, which removes the `epsilon` radius inflation in the saturated finite-dimensional case.
- R. R. Akhmerov, M. I. Kamenskii, A. S. Potapov, A. E. Rodkina, and B. N. Sadovskii, *Measures of Noncompactness and Condensing Operators*, Operator Theory: Advances and Applications 55, Birkhauser (1992), DOI `10.1007/978-3-0348-5727-7`. Role: standard Hausdorff-measure-of-noncompactness machinery and contractivity under bounded linear maps.
- Standard quotient-topology theory identifies saturated subsets as inverse images of subsets of the quotient; in particular a closed saturated subset has closed image under the canonical quotient topology.

The ingredients are classical. The durable Arithmetic Fidelity contribution is the exact decomposition of AF-500's order-of-operations pathology into two independently falsifiable resources: **saturation controls whether post-quotient truncation admits source states that had no bounded upstream representative, while finite-dimensionality of the nuisance fiber is exactly the universal condition that prevents bounded compactness from being lost solely inside a forgotten fiber.**

## Falsification and boundary audit

- Saturation is imposed on `D=cl C`, not merely on the raw set `C`, because AF-499/AF-500 distance and tail geometry already work with the closure. If exact membership in `C` matters operationally, a separate exact-source audit is required.
- Without proximinality, saturation gives the inclusion only with an arbitrary positive radius inflation. Therefore `nu_C^0(s;R)=0` at one exact radius need not by itself imply `nu_C^V(s;R)=0`; it is sufficient that the raw profile vanish at some radius strictly above `R`. This boundary issue disappears for finite-dimensional `V`.
- Finite dimensionality is necessary only for the **universal** bounded-lifting property over all bounded sets. A particular infinite-dimensional nuisance family may still have compact fibers or otherwise satisfy the needed lifting condition.
- Saturation is likewise a structural sufficient condition for preventing new post-quotient aliases, not a claim that every nonsaturated source must fail. Nonsaturated families can commute accidentally.
- The exact equivalence concerns vanishing versus positive tail noncompactness, not equality of the numerical profiles `nu_C^0` and `nu_C^V`.
- The second sharpness control is deliberately saturated and synthetic. It isolates fiber escape cleanly but does not claim that a natural arithmetic nuisance family contains an entire infinite-dimensional affine fiber.
- Nothing here identifies a rational-prime discriminator. The result supplies a stronger audit for future arithmetic models: decide separately whether the declared nuisance equivalence saturates the admissible source family and whether bounded forgotten fibers are compact enough to lift destination-level tightness.

## Consequence for the research line

AF-500 established the forced order `quotient -> truncate -> test compactness` in general. AF-501 identifies when that order can be relaxed and, more importantly, why it fails when it cannot.

A future compression audit should now distinguish two questions before treating pre- and post-compression compactness as comparable:

1. **Admission:** is the admissible source already saturated under the nuisance equivalence, so quotienting does not create new task-visible bounded aliases?
2. **Lifting:** are bounded nuisance fibers precompact strongly enough that quotient-level compactness can be lifted back upstream?

For linear nuisance quotients, finite-dimensional `V` is exactly the universal answer to the second question. This turns the bidirectional counterexamples of AF-500 into a two-gate structural classification rather than a generic warning that quotienting and compactness need not commute.