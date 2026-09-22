# AF-500 — Tail compactness must be measured after nuisance quotienting

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NUISANCE-QUOTIENT`, `TRANSLATION-LIMIT`, `MEASURE-OF-NONCOMPACTNESS`, `ORDER-OF-OPERATIONS`, `MINIMAX-RESOLUTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-490 shows that an unrestricted nuisance subspace must be quotiented out before measuring the surviving discriminator. AF-499 shows that, in infinite-dimensional observation spaces, recovery of a large-displacement threshold requires asymptotic compactness of the task-visible translated residuals. These two operations do not commute.

Let `Y` be a Banach space, let `V subset Y` be a closed linear subspace, let

\[
\pi:Y\to Q:=Y/V
\]

be the quotient map, let `C subset Y` be nonempty, and let `s in Y`. Put

\[
\bar s:=\pi(s),
\qquad
D_V:=\overline{\pi(C)}\subset Q.
\]

The nuisance-relative asymptotic separation is

\[
\lambda_{C|V}(s)
:=
\liminf_{t\to\infty}\operatorname{dist}_Y(ts,C+V).
\]

By the quotient norm identity,

\[
\boxed{
\lambda_{C|V}(s)
=
\liminf_{t\to\infty}
\operatorname{dist}_Q(t\bar s,D_V).
}
\]

For `R,T>=0`, define the **quotient-visible tail residual set**

\[
E^V_{T,R}(C,s)
:=
\bigcup_{t\ge T}
\Bigl((D_V-t\bar s)\cap\overline B_R^Q(0)\Bigr),
\]

and its tail Hausdorff measure of noncompactness

\[
\boxed{
\nu^V_C(s;R)
:=
\lim_{T\to\infty}
\chi_Q\bigl(E^V_{T,R}(C,s)\bigr).
}
\]

Define the quotient translation fiber

\[
\mathcal A^V_C(s)
:=
\left\{
 a\in Q:
 \exists\ t_n\to\infty,\ c_n\in C,
 \ \pi(c_n-t_ns)\to a
\right\}.
\]

Then the AF-499 recovery law applies in the **destination quotient**:

- if `lambda_{C|V}(s)<infinity` and `nu^V_C(s;R)=0` for some `R>lambda_{C|V}(s)`, then

\[
\boxed{
\lambda_{C|V}(s)
=
\min_{a\in\mathcal A^V_C(s)}\|a\|_Q
=
\operatorname{dist}_Q(0,\mathcal A^V_C(s));
}
\]

- at an exact radius `r`, quotient-tail compactness restores the actual-contact/fiber equivalence, and the distance-defined equality case additionally needs the same quotient-level attainment/proximinality gate isolated in AF-499.

Most importantly, the raw profile `nu^0_C` in `Y` does **not** determine the quotient profile `nu^V_C`. Both directions fail, even in explicit Hilbert sums:

\[
\boxed{
\nu^0_C>0\ \text{can become}\ \nu^V_C=0,
\qquad
\nu^0_C=0\ \text{can become}\ \nu^V_C>0.
}
\]

Thus compactness cannot be audited before declaring which directions are nuisance. The correct order is

\[
\boxed{
\text{identify nuisance quotient}
\ \longrightarrow\ 
\text{form task-visible residuals}
\ \longrightarrow\ 
\text{test tail compactness}.
}
\]

This is a genuine order-of-operations constraint, not a cosmetic choice of coordinates.

## Quotient reduction

Because `V` is closed, `Q=Y/V` is a Banach space with norm

\[
\|\pi(y)\|_Q
=
\operatorname{dist}_Y(y,V).
\]

For every `y in Y`,

\[
\begin{aligned}
\operatorname{dist}_Q(\pi(y),\pi(C))
&=
\inf_{c\in C}\|\pi(y-c)\|_Q\\
&=
\inf_{c\in C}\inf_{v\in V}\|y-c-v\|_Y\\
&=
\operatorname{dist}_Y(y,C+V).
\end{aligned}
\]

Passing from `pi(C)` to its closure `D_V` does not change this distance. Hence nuisance-relative separation in `Y` is exactly ordinary separation in the quotient.

The closure also does not enlarge the quotient translation fiber. If

\[
d_n-t_n\bar s\to a,
\qquad d_n\in D_V,
\]

choose `c_n in C` with

\[
\|\pi(c_n)-d_n\|_Q<1/n.
\]

Then

\[
\pi(c_n-t_ns)\to a.
\]

So `mathcal A^V_C(s)` is exactly the AF-499 translation fiber of `D_V` in `Q`, even though it can be represented using the original source set `C`.

Since `Q` is Banach, AF-499 now gives immediately: if `nu^V_C(s;R)=0` at one radius strictly above the quotient liminf level, every quotient-visible near-minimizing residual sequence has a norm-convergent subsequence in `Q`, producing a point of `mathcal A^V_C(s)` at norm exactly `lambda_{C|V}(s)`.

The same reduction applies to the contact statement. Define

\[
\mathcal B^V_C(s;r)
:=
\left\{
 a\in Q:
 \exists\ t_n\to\infty,\ d_n\in D_V,
 \ \|d_n-t_n\bar s\|_Q\le r,
 \ d_n-t_n\bar s\to a
\right\}.
\]

If `nu^V_C(s;r)=0`, unbounded actual radius-`r` quotient contacts are equivalent to `mathcal B^V_C(s;r) != emptyset`. If one asks instead for the distance-defined predicate

\[
\operatorname{dist}_Y(ts,C+V)\le r,
\]

then exact equality still requires distance attainment by `D_V` at the relevant quotient points, just as AF-499 requires in the unquotiented setting.

The theorem therefore introduces no new compactness principle. It identifies **where the existing principle must be evaluated**: after the nuisance compression that defines the downstream task.

## Raw noncompactness can be a false obstruction

Take

\[
Y=\mathbb R\oplus_2\ell^2,
\qquad
V=\{0\}\oplus\ell^2,
\qquad
s=(1,0),
\]

and let `(e_n)` be the standard orthonormal basis of `ell^2`. Set

\[
C:=\{(n,e_n):n\ge1\}.
\]

The set is closed because its first coordinate tends to infinity.

Before quotienting, the exact distance from the ray satisfies

\[
\operatorname{dist}_Y(ts,C)
=
\inf_{n\ge1}\sqrt{(t-n)^2+1}
\ge1,
\]

with equality at every positive integer. At radius `R=1`, the raw tail residual set is therefore exactly

\[
E^0_{T,1}(C,s)
=
\{(0,e_n):n\ge\lceil T\rceil\}.
\]

Its Hausdorff measure of noncompactness is

\[
\boxed{\nu^0_C(s;1)=1.}
\]

The upper bound is given by the unit ball centered at the origin. For the lower bound, fix any center `(a,x) in R direct-sum ell^2`. Since `x_n->0`,

\[
\|(0,e_n)-(a,x)\|^2
\to
1+a^2+\|x\|^2
\ge1.
\]

Thus every ball of radius strictly below `1` contains only finitely many tail basis points, and no finite family of such balls covers the tail.

Now quotient by `V`. Then `Q` is isometric to `R`,

\[
\pi(C)=\mathbb N,
\qquad
\bar s=1.
\]

For every `R<infinity` and every `T`,

\[
E^V_{T,R}(C,s)=[-R,R].
\]

Indeed any `u in [-R,R]` is realized by taking a sufficiently large integer `n` and `t=n-u>=T`. Hence

\[
\boxed{
\nu^V_C(s;R)=0
\quad\text{for every finite }R.
}
\]

The raw infinite-dimensional dispersion was entirely contained in nuisance directions. Treating it as an obstruction before quotienting would incorrectly reject a perfectly compact destination-level problem. In the quotient,

\[
\lambda_{C|V}(s)=0
\]

and the exact integer contacts are faithfully retained.

## Raw compactness can hide a quotient obstruction

The converse failure is just as important. Let

\[
Y
=
\mathbb R\oplus_2\ell^2\oplus_2\mathbb R,
\qquad
V
=
\{0\}\oplus\{0\}\oplus\mathbb R,
\qquad
s=(1,0,0),
\]

and define

\[
C:=\{(n,e_n,n):n\ge1\}.
\]

For every fixed finite `R`, the raw radius-`R` tail residual set is eventually empty. Indeed, if

\[
\|(n-t,e_n,n)\|\le R,
\]

then `n<=R` from the last coordinate and `|t-n|<=R`, so necessarily `t<=2R`. Therefore

\[
T>2R
\quad\Longrightarrow\quad
E^0_{T,R}(C,s)=\varnothing,
\]

and hence

\[
\boxed{
\nu^0_C(s;R)=0
\quad\text{for every finite }R.
}
\]

Raw compactness here is vacuous: the growing last coordinate prevents any bounded residual from surviving far along the target ray.

After quotienting by that last-coordinate nuisance, however,

\[
Q\cong\mathbb R\oplus_2\ell^2,
\qquad
D_V=\{(n,e_n):n\ge1\}.
\]

At `t=n` the quotient residual is `(0,e_n)`, so

\[
\lambda_{C|V}(s)=1
\]

and exact critical contacts recur indefinitely. At radius `1`,

\[
E^V_{T,1}(C,s)
=
\{(0,e_n):n\ge\lceil T\rceil\},
\]

thus

\[
\boxed{
\nu^V_C(s;1)=1.
}
\]

Moreover the quotient translation and critical-contact fibers are empty. Any bounded translated witness would require `n_j-t_j` bounded with `t_j->infinity`, hence `n_j->infinity`, while `(e_{n_j})` has no norm-convergent subsequence. Therefore

\[
\boxed{
\mathcal A^V_C(s)=\varnothing,
\qquad
\mathcal B^V_C(s;1)=\varnothing,
}
\]

even though the quotient distance hits its exact critical value `1` at arbitrarily large integer times.

So quotienting can expose a noncompact alias family that was completely invisible to every fixed raw radius. The reason is simple but structural: residuals that escaped to infinity only along nuisance directions are pulled back into the task-visible bounded region when those directions are forgotten.

## Why ordinary operator monotonicity does not save the raw audit

The quotient map is contractive. For any **fixed bounded set** `A subset Y`, classical measure-of-noncompactness theory gives

\[
\chi_Q(\pi(A))\le\chi_Y(A).
\]

There is therefore no contradiction with the second example.

The issue is that quotienting is performed **before radius truncation**. In general

\[
\pi\Bigl((D-ts)\cap\overline B_R^Y\Bigr)
\subsetneq
\Bigl(\overline{\pi(D)}-t\bar s\Bigr)
\cap\overline B_R^Q.
\]

A point may be very large in `Y` solely because of its `V` component while its quotient norm is small. Such a point is excluded by the raw radius cutoff but admitted by the quotient-visible cutoff. The family whose noncompactness is being measured therefore changes before the contractive map is applied.

This is the exact noncommutation:

\[
\boxed{
\text{truncate by raw norm then quotient}
\ \ne\ 
\text{quotient then truncate by task norm}.
}
\]

AF-500 is therefore not a counterexample to data processing for measures of noncompactness. It is a warning that the **task-relevant set itself is defined only after the nuisance quotient**.

## Finite-dimensional quotients automatically pass the compactness gate

If `Q=Y/V` is finite-dimensional, then every bounded subset of `Q` is relatively compact. Consequently

\[
\boxed{
\nu^V_C(s;R)=0
\quad\text{for every }C,s,R<\infty.
}
\]

This explains why the compactness issue is absent from AF-490's finite-dimensional nuisance regression model: once the nuisance subspace is quotiented out, the destination geometry is finite-dimensional and the tail compactness gate is automatic. Only the quotient discriminator size remains.

In an infinite-dimensional destination quotient, both resources must be audited separately:

1. the target direction must survive the nuisance quotient with nonzero task-relevant separation;
2. the bounded quotient-visible alias family must be asymptotically norm-precompact at the required radius.

The first is the AF-490 discrimination gate; the second is the AF-499 compactness gate. Neither can be inferred safely from pre-quotient geometry.

## Prior-art and novelty audit

No broad novelty is claimed for Banach quotients, quotient norms, Hausdorff measures of noncompactness, or asymptotic compactness.

- Robert E. Megginson, *An Introduction to Banach Space Theory*, Graduate Texts in Mathematics 183, Springer (1998), DOI `10.1007/978-1-4612-0603-3`, especially the basic quotient-space theory. Role: standard source for `Y/V`, the quotient norm, and completeness when `V` is closed.
- R. R. Akhmerov, M. I. Kamenskii, A. S. Potapov, A. E. Rodkina, and B. N. Sadovskii, *Measures of Noncompactness and Condensing Operators*, Operator Theory: Advances and Applications 55, Birkhauser (1992), DOI `10.1007/978-3-0348-5727-7`. Role: classical measure-of-noncompactness theory for bounded sets and bounded linear operators; in particular, continuous linear images cannot create noncompactness on a fixed bounded input set beyond the operator Lipschitz factor.
- Junya Nishiguchi, **“Asymptotic compactness in topological spaces,”** *Topology and its Applications* 287 (2021), 107451, DOI `10.1016/j.topol.2020.107451`. Role: established asymptotic-compactness language for families of sets and compact limit behavior, already used in AF-499.
- David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *Annals of Statistics* 22(1), 238–270 (1994), DOI `10.1214/aos/1176325367`. Role: classical minimax/optimal-recovery background for nuisance-induced indistinguishability and quotient geometry, already adjacent to AF-490.

The classical pieces therefore exist separately. The durable Arithmetic Fidelity result is the composition statement and its two exact controls: **the compactness resource required by AF-499 is destination-relative and must be measured after the nuisance quotient; pre-quotient tail compactness can give either a false obstruction or a false certificate.**

## Falsification and boundary audit

- `V` must be closed so that `Q=Y/V` is Banach and AF-499's completeness argument applies directly. For nonclosed `V`, the correct Hausdorff destination first requires quotienting by `cl V` or otherwise changing category.
- The theorem concerns an unrestricted linear nuisance subspace. Bounded, nonlinear, discrete, or parameter-dependent nuisance classes generally produce a different quotient/fiber geometry and must be analyzed in their own destination space.
- `D_V=cl pi(C)` is deliberate. The image of a closed set under a quotient map need not be closed, and distance only sees its closure. Applications whose semantics require exact membership rather than arbitrary approximation must retain that distinction.
- Quotient-tail compactness is sufficient for the AF-499 recovery route, not necessary for every accidental equality of scalar thresholds. Positive `nu^V` can coexist with a correct threshold identity for special families.
- The two Hilbert-sum examples are synthetic controls. They prove logical independence of raw and quotient tail compactness; they do not assert that a natural arithmetic nuisance family realizes either pathology.
- A finite-dimensional quotient removes the compactness obstruction but does not guarantee arithmetic provenance. It says only that the destination-level bounded residual family is compact.
- Nothing here identifies a rational-prime discriminator or advances RH directly. The result sharpens the order in which a later arithmetic observation model must be audited.

## Relationship to AF-490 and AF-499

AF-490 establishes that nuisance directions must be removed before measuring discriminator strength: raw depth can disappear completely after quotienting by an unknown-amplitude direction. AF-499 establishes that large-displacement recovery in infinite-dimensional geometry depends on tail compactness of the bounded residual family.

AF-500 composes those two results and shows that the composition has a forced order. The relevant compactness profile is neither an ambient-space property nor a property that can be safely checked upstream. It belongs to the **post-nuisance destination geometry**.

For future arithmetic applications, this gives a sharper audit rule: first write the actual nuisance equivalence induced by normalization, unknown amplitudes, gauge, phase, boundary data, or other ignored directions; only then ask whether the surviving near-aliases are compact/tight enough to retain the discriminator at the requested noise scale.