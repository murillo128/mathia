# AF-507 — Admission height refines quotient contact into exact plateau onset

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `CONVEX-GEOMETRY`, `QUOTIENT`, `CRITICAL-CONTACT`, `MINIMAL-LIFT`, `ORDER-OF-OPERATIONS`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-506 reduces the existence of a finite-time critical plateau to one boundary-membership bit in the quotient by the observation direction. In finite-dimensional Hilbert geometry that bit has a sharper representation: it is the finiteness of an extended-real **admission height**, and the finite value of that height gives the exact time at which the plateau begins.

Let `Q` be a finite-dimensional real Hilbert space, let `u in Q` be a unit vector, and write

\[
H:=u^\perp,
\qquad
Q=H\oplus\mathbb Ru.
\]

Let `F subset Q` be nonempty, closed, and convex, and assume

\[
u\in\operatorname{rec}(F),
\qquad
-u\notin\operatorname{rec}(F).
\]

For `z in H`, define the admission height

\[
a_F(z):=\inf\{s\in\mathbb R:z+su\in F\},
\]

with `inf emptyset=+infinity`. Then `a_F:H -> R union {+infinity}` is a proper closed convex function and

\[
\boxed{
F=\{z+su:z\in H,\ s\ge a_F(z)\}.
}
\]

Under the canonical identification `Q/Ru congruent H`, the quotient image from AF-506 is exactly

\[
\boxed{q(F)=\operatorname{dom}(a_F).}
\]

For

\[
f(t):=\operatorname{dist}(tu,F),\qquad t\ge0,
\]

one has the exact envelope formula

\[
\boxed{
f(t)^2
=\inf_{z\in H}
\left(
\|z\|^2+(a_F(z)-t)_+^2
\right),
}
\]

where `(r)_+:=max(r,0)` and terms with `a_F(z)=+infinity` are interpreted as `+infinity`.

Let

\[
\lambda:=\operatorname{dist}(0,\operatorname{dom}a_F)
=\operatorname{dist}(0,\overline{\operatorname{dom}a_F}),
\]

and let

\[
z_*:=P_{\overline{\operatorname{dom}a_F}}(0)
\]

be the unique nearest point to the closed convex set `closure(dom a_F)`. Define

\[
\tau_F:=
\begin{cases}
\max\{0,a_F(z_*)\},&a_F(z_*)<+\infty,\\
+\infty,&a_F(z_*)=+\infty.
\end{cases}
\]

Then

\[
\boxed{
\{t\ge0:f(t)=\lambda\}
=
\begin{cases}
[\tau_F,\infty),&\tau_F<\infty,\\
\varnothing,&\tau_F=+\infty.
\end{cases}
}
\]

Thus AF-506's boundary-membership criterion is the coarse question

\[
\boxed{a_F(z_*)<+\infty,}
\]

while exact temporal recovery needs the additional scalar admission height. Replacing the quotient image `dom(a_F)` by its closure loses at least two nested levels of information at the critical transverse point:

- whether the critical fiber exists at all; and
- if it exists, the longitudinal height at which it first becomes admissible.

The first is one bit. The second is genuinely real-valued: a continuum family of closed convex sets can have identical quotient image, identical quotient closure, identical asymptotic threshold, and the same positive contact bit, while realizing every prescribed finite plateau-onset time.

## The ray-invariant convex set is an epigraph

For fixed `z in H`, consider the fiber

\[
I_z:=\{s\in\mathbb R:z+su\in F\}.
\]

Closedness and convexity of `F` make `I_z` a closed convex subset of `R`. Since `u in rec(F)`, every nonempty `I_z` is stable under addition of `R_+`. Hence each fiber is either empty, a ray `[a,infinity)`, or all of `R`.

The last possibility cannot occur under `-u notin rec(F)`. Indeed, if one full affine line parallel to `u` lies in a nonempty closed convex set, then `u` and `-u` are lineality directions of that set: equivalently, every supporting halfspace has normal orthogonal to `u`, so translation by `Ru` preserves the whole set. Thus a full fiber would force `-u in rec(F)`.

Therefore every nonempty fiber is a closed upper ray and

\[
I_z=[a_F(z),\infty).
\]

Under the isometry `H times R -> Q`, `(z,s) mapsto z+su`, the set `F` is exactly the epigraph of `a_F`. Since `F` is nonempty, closed, and convex, `a_F` is proper, lower semicontinuous, and convex. Its effective domain is precisely the transverse projection of `F`, which is the quotient image `q(F)`.

This places the nonclosed-image mechanism in standard convex-analysis language: a closed proper convex function can have a nonclosed effective domain even though its epigraph is closed.

## Exact distance-profile formula

For fixed `z` with `a_F(z)<infinity`, minimize the squared Euclidean distance from `(0,t)` to the upper ray over that transverse coordinate:

\[
\inf_{s\ge a_F(z)}
\left(\|z\|^2+(s-t)^2\right).
\]

The optimal longitudinal coordinate is `s=t` when `t>=a_F(z)` and `s=a_F(z)` otherwise. Therefore

\[
\inf_{s\ge a_F(z)}
\left(\|z\|^2+(s-t)^2\right)
=
\|z\|^2+(a_F(z)-t)_+^2.
\]

Taking the infimum over `z` gives

\[
f(t)^2
=\inf_{z\in H}
\left(\|z\|^2+(a_F(z)-t)_+^2\right).
\]

The quotient closure controls only the limiting transverse cost

\[
\lambda^2
=\inf_{z\in\operatorname{dom}a_F}\|z\|^2.
\]

The finite-time excess above `lambda` is the best tradeoff between transverse displacement away from the critical point and the remaining longitudinal admission penalty. In particular,

\[
f(t)^2-\lambda^2
=
\inf_{z\in H}
\left(
\|z\|^2-\lambda^2+(a_F(z)-t)_+^2
\right).
\]

This identifies a more refined future audit surface: in the no-contact branch, the rate at which `f(t)` approaches `lambda` is controlled by how `a_F(z)` diverges as admissible transverse points approach `z_*`.

## Plateau onset is one boundary value

Because `closure(dom a_F)` is closed and convex in finite-dimensional Hilbert space, `z_*` exists and is unique.

If `a_F(z_*)<infinity`, then for every

\[
t\ge\max\{0,a_F(z_*)\}
\]

one has `z_*+tu in F`. Hence

\[
f(t)\le\|z_*\|=\lambda.
\]

AF-506 gives the opposite inequality `f(t)>=lambda`, so equality holds.

Conversely, suppose `f(t)=lambda` for some finite `t>=0`. Distance to the nonempty closed set `F` is attained in finite dimensions, so there exists

\[
y=z+su\in F
\]

with

\[
\|y-tu\|^2
=\|z\|^2+(s-t)^2
=\lambda^2.
\]

Since `z in dom(a_F)`, one has `||z||>=lambda`. Equality of the sum therefore forces

\[
\|z\|=\lambda,
\qquad
s=t.
\]

Uniqueness of the projection onto `closure(dom a_F)` gives `z=z_*`. Since `z_*+tu in F`,

\[
a_F(z_*)\le t.
\]

Thus `a_F(z_*)` is finite and no critical contact can occur before `max(0,a_F(z_*))`. This proves the exact terminal-ray formula for the equality set.

The AF-506 membership bit is therefore not a separate invariant from convex epigraph geometry. It is simply the finite-versus-infinite status of the admission height at the nearest point of the closed quotient image.

## Same quotient, same contact bit, arbitrary onset

Fix `L>0`, take `Q=R^2`, `u=e_1`, and identify `H` with the vertical coordinate. For every `c>=0`, define

\[
F_c:=\{(x,y):x\ge c,\ y\ge L\}.
\]

Then

\[
\operatorname{rec}(F_c)=\mathbb R_+^2,
\qquad
q(F_c)=[L,\infty),
\qquad
\lambda=L,
\]

independently of `c`. The unique nearest quotient point is `z_*=L`, and

\[
a_{F_c}(L)=c.
\]

Consequently

\[
\operatorname{dist}(te_1,F_c)=L
\iff
t\ge c.
\]

All members of the family therefore have:

- the same quotient image, not merely the same quotient closure;
- the same critical value `lambda`;
- the same positive boundary-membership/contact bit;
- different plateau-onset times ranging over every `c>=0`.

Hence quotient data plus the AF-506 membership bit cannot recover the exact temporal onset. More strongly, on this matched family any exact onset-recovering lift must distinguish every value of `c`, so its range must have cardinality at least that of the continuum. The scalar `tau_F` has exactly that cardinality and is sufficient. This is a target-relative cardinality-minimal lift on the family, not a claim of canonical minimality among all possible mathematical representations.

The AF-505/AF-506 no-contact control is recovered by

\[
F_+
=
\left\{(x,y):x\ge0,\ y\ge L+\frac1{x+1}\right\}.
\]

Its admission function is

\[
a_{F_+}(y)
=
\begin{cases}
\max\left\{0,\frac1{y-L}-1\right\},&y>L,\\
+\infty,&y\le L.
\end{cases}
\]

Thus

\[
\operatorname{dom}(a_{F_+})=(L,\infty),
\qquad
\overline{\operatorname{dom}(a_{F_+})}=[L,\infty),
\qquad
z_*=L,
\qquad
a_{F_+}(z_*)=+\infty.
\]

The same closed quotient geometry therefore produces the no-plateau branch exactly by excluding the critical transverse point from the effective domain.

## Two-sided lineality removes this boundary defect

The one-sided assumption is essential to the nonclosed-domain mechanism. If also

\[
-u\in\operatorname{rec}(F),
\]

then `F` is saturated by the whole line `Ru`:

\[
F+\mathbb Ru=F.
\]

Hence

\[
F=q^{-1}(q(F)).
\]

Because `q` is a quotient map and `F` is closed, `q(F)` is closed. In the orthogonal model this is simply

\[
F=(F\cap H)+\mathbb Ru
\]

with `F cap H` closed. The boundary-membership failure isolated in AF-506 therefore cannot arise from closure of the quotient image in this lineality branch.

The converse is false: a quotient image can already be closed under only one-sided recession. The family `F_c` above is an explicit example. Thus two-sided lineality is a sufficient structural gate for closedness here, not a necessary one.

## Prior-art audit

The epigraph, effective-domain, recession-cone, lower-semicontinuity, and metric-projection ingredients are classical convex analysis.

- R. Tyrrell Rockafellar, *Convex Analysis*, Princeton University Press (1970), especially the treatment of closed proper convex functions, recession cones, and closedness of linear images/epigraphs. Rockafellar explicitly emphasizes that closedness of an epigraph does not force its linear image or effective domain to be closed.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press (2004), especially §3.1 on epigraphs and extended-real convex functions. A function is convex exactly when its epigraph is convex, and closed convex functions are naturally handled as extended-real functions on possibly nonclosed effective domains.
- Dimitri P. Bertsekas, *Convex Optimization Theory*, Athena Scientific (2009), especially the sections on epigraphs, closed proper convex functions, and recession cones.

No novelty is claimed for representing a directionally upper closed convex set as an epigraph, for the standard facts about effective domains and recession cones, or for Hilbert-space projection onto a closed convex set.

The Arithmetic Fidelity contribution is the **task-specific synthesis** obtained after AF-506: the missing boundary-membership bit is exactly the finiteness of a one-point admission height; the same boundary value gives the exact plateau-onset time; and a matched continuum family proves that the Boolean contact lift is insufficient for exact temporal recovery even when the entire quotient image is retained.

## Boundaries and falsification

- The exact squared-distance envelope uses the Hilbert orthogonal decomposition. In a general normed quotient one still has AF-506's membership criterion, but not this Pythagorean formula.
- Finite dimensionality is used to make distance to `F` attained and to make projection onto the closed quotient domain immediate. Reflexive Hilbert variants are possible but are not asserted here without a separate domain/attainment audit.
- The numerical onset depends on the normalization of the ray parameter; fixing `||u||=1` removes this scale ambiguity. Finiteness of the height is the invariant contact bit under positive reparameterization.
- `a_F(z_*)` is not claimed to be a universal minimal representation of `F`. The minimality statement is only target-relative: exact recovery of the plateau-onset discriminator on the matched family `F_c` requires continuum many lift states.
- Closedness of `q(F)` does not imply two-sided lineality; `F_c` rules out that converse.
- The result does not supply an RH mechanism. It refines one generic compression boundary in the Arithmetic Fidelity theory and identifies the next quantitative object governing approach-to-contact when the critical fiber is missing.

## Consequence

For the convex ray-contact channel, the information flow is now explicit:

\[
F
\longmapsto
\operatorname{dom}(a_F)
\longmapsto
\overline{\operatorname{dom}(a_F)}.
\]

The first quotient discards longitudinal admission height while retaining which transverse fibers exist. Closure then discards boundary membership as well. At the critical nearest transverse point `z_*`, these losses appear as a nested lift hierarchy:

\[
\boxed{
\text{closed quotient geometry}
\ +\ \mathbf 1_{\{a_F(z_*)<\infty\}}
\ +\ \tau_F.
}
\]

The first term recovers the asymptotic critical value, the bit recovers whether a finite plateau exists, and the scalar recovers exactly when that plateau begins. The remaining no-contact problem is therefore not simply whether information survives, but how the admission height diverges near the missing critical fiber and how that divergence controls the asymptotic approach rate.