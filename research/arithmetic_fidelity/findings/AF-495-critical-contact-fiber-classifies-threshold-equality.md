# AF-495 — Critical-contact fibers classify the equality case at the fixed-noise alias threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TRANSLATION-LIMIT`, `MINIMAX-RESOLUTION`, `MINIMAL-LIFT`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-494 proves that the bounded-offset translation fiber

\[
\mathcal A_C(s)
:=
\left\{
 a\in Y:
 \exists\ t_n\to\infty,\ c_n\in C,
 \ c_n-t_ns\to a
\right\}
\]

controls the sharp **open** fixed-noise phase boundary through

\[
\lambda_C(s)
:=
\liminf_{t\to\infty}\operatorname{dist}(ts,C)
=
\operatorname{dist}(0,\mathcal A_C(s)).
\]

It deliberately leaves the equality case unresolved: when the ambiguity radius is exactly `r=lambda_C(s)`, the full translation fiber can record a boundary cluster point without recording whether the translated nuisance set ever enters the closed radius-`r` ball at arbitrarily large times.

The missing datum is obtained by applying the task predicate **before** taking the outer limit.

Let `Y` be a finite-dimensional normed real vector space, let `C subset Y` be nonempty, let `s in Y`, and write `D=cl C`. For `r>=0`, define the radius-`r` critical-contact fiber

\[
\mathcal B_C(s;r)
:=
\limsup_{t\to\infty}
\Bigl((D-ts)\cap \overline B_r(0)\Bigr),
\]

where the outer limit is understood sequentially:

\[
a\in\mathcal B_C(s;r)
\iff
\exists\ t_n\to\infty,\ d_n\in D
\quad
\text{with}
\quad
\|d_n-t_ns\|\le r,
\quad
d_n-t_ns\to a.
\]

Then, for the AF-494 ambiguity profile

\[
\Delta_C(\rho;s)
:=
\sup\{t\ge0:\operatorname{dist}(ts,C)\le2\rho\},
\]

one has the exact equivalence

\[
\boxed{
\Delta_C(r/2;s)=\infty
\iff
\mathcal B_C(s;r)\ne\varnothing.
}
\]

Moreover

\[
\boxed{
\mathcal A_C(s)\cap B_r(0)
\subseteq
\mathcal B_C(s;r)
\subseteq
\mathcal A_C(s)\cap\overline B_r(0).
}
\]

Thus the only possible loss between the full bounded-offset fiber and the task-truncated contact fiber lies on the sphere `||a||=r`.

If `lambda=lambda_C(s)<infinity`, define the **critical-contact bit**

\[
\chi_C(s)
:=
\mathbf 1\{\mathcal B_C(s;\lambda)\ne\varnothing\}.
\]

Then the entire finite-versus-infinite fixed-radius ambiguity phase is classified by the pair `(lambda_C(s),chi_C(s))`:

\[
\boxed{
\Delta_C(r/2;s)=\infty
\iff
r>\lambda_C(s)
\ \text{or}\ 
\bigl(r=\lambda_C(s)\text{ and }\chi_C(s)=1\bigr).
}
\]

The bit is genuinely additional information. There are exact nuisance difference sets with the same horizon set, the same `lambda_C(s)`, and the same complete translation fiber `mathcal A_C(s)`, but opposite values of `chi_C(s)`.

## Proof of the contact equivalence

Because distance is unchanged by closure,

\[
\operatorname{dist}(ts,C)=\operatorname{dist}(ts,D).
\]

Assume first that `Delta_C(r/2;s)=infinity`. Then there are `t_n->infinity` with

\[
\operatorname{dist}(t_ns,D)\le r.
\]

Since `D` is closed and `Y` is finite-dimensional, distance to `D` is attained. Choose `d_n in D` with

\[
\|d_n-t_ns\|
=
\operatorname{dist}(t_ns,D)
\le r.
\]

The offsets lie in the compact ball `overline B_r(0)`, so a subsequence converges to some `a`. By definition,

\[
a\in\mathcal B_C(s;r).
\]

Conversely, if `a in mathcal B_C(s;r)`, its witnessing sequence satisfies

\[
\operatorname{dist}(t_ns,C)
=
\operatorname{dist}(t_ns,D)
\le
\|d_n-t_ns\|
\le r
\]

for unbounded `t_n`. Hence `Delta_C(r/2;s)=infinity`.

The closure in the definition introduces no extra bounded-offset cluster points. Indeed

\[
\mathcal A_C(s)=\mathcal A_D(s),
\]

because any `d_n in D` occurring in a convergent-offset witness can be approximated by `c_n in C` with `||c_n-d_n||<1/n`.

## Truncate before the outer limit versus after it

The right-hand inclusion

\[
\mathcal B_C(s;r)
\subseteq
\mathcal A_C(s)\cap\overline B_r(0)
\]

is immediate from the definitions.

For the other inclusion, take `a in mathcal A_C(s)` with `||a||<r`. Choose witnesses `t_n->infinity` and `c_n in C` such that

\[
c_n-t_ns\to a.
\]

Since `a` lies strictly inside the radius-`r` ball, eventually

\[
\|c_n-t_ns\|<r.
\]

Thus the same tail witnesses `a in mathcal B_C(s;r)`.

Therefore

\[
\limsup_{t\to\infty}
\Bigl((D-ts)\cap\overline B_r\Bigr)
\]

and

\[
\left(\limsup_{t\to\infty}(D-ts)\right)
\cap\overline B_r
\]

can differ only through cluster points on the boundary sphere. This is exactly the standard set-limit phenomenon that outer limits need not commute with intersection at a boundary.

For Arithmetic Fidelity this order matters: **compress first to the unmarked outer-limit fiber, then ask the closed-radius question** can forget from which side the boundary was approached. Applying the task predicate before compression retains that one-sided contact information.

## Exact critical phase classification

Let

\[
\lambda:=\lambda_C(s)<\infty.
\]

AF-494 already gives:

\[
r>\lambda
\Longrightarrow
\Delta_C(r/2;s)=\infty,
\]

and

\[
r<\lambda
\Longrightarrow
\Delta_C(r/2;s)<\infty.
\]

At `r=lambda`, the contact equivalence gives

\[
\Delta_C(\lambda/2;s)=\infty
\iff
\mathcal B_C(s;\lambda)\ne\varnothing
\iff
\chi_C(s)=1.
\]

Hence `(lambda,chi)` is task-sufficient for every finite radius. The scalar `lambda` determines the open phase boundary; `chi` determines whether the boundary itself belongs to the ambiguous phase.

This is a minimal lift in the task-relative sense: once `lambda` is fixed, the remaining output is one binary decision, and examples below show that neither `lambda` nor the complete untruncated fiber `mathcal A_C(s)` determines it.

## Same translation fiber, opposite critical-contact bit

Use the genuine difference-set family from AF-494. Work in `Y=R^2` with `s=e_1`, set

\[
H_n=2^{2^n},
\]

and for a nonnegative sublinear sequence `(g_n)` define

\[
a_n=(0,H_n),
\qquad
b_n=(n,H_n+g_n),
\qquad
K_g=\{a_n,b_n:n\ge1\},
\qquad
C_g=K_g-K_g.
\]

Fix `L>0` and compare

\[
g_n^{(0)}=L,
\qquad
 g_n^{(+)}=L+\frac1n.
\]

AF-494 already shows that both difference sets have the same horizon geometry and

\[
\lambda_{C_g}(e_1)=L.
\]

They also have the same complete bounded-offset translation fiber:

\[
\boxed{
\mathcal A_{C_{g^{(0)}}}(e_1)
=
\mathcal A_{C_{g^{(+)}}}(e_1)
=
\mathbb R\times\{L\}.
}
\]

To see this, any bounded-offset sequence following `t e_1` must eventually use the same-index positive differences

\[
b_n-a_n=(n,g_n),
\]

because unequal-index height differences escape vertically. If `n-t_n->u`, the offset tends to `(u,L)`, and every `u in R` is realized by choosing `t_n=n-u` for large `n`.

Nevertheless their critical-contact fibers at radius `L` differ:

\[
\boxed{
\mathcal B_{C_{g^{(0)}}}(e_1;L)=\{(0,L)\},
\qquad
\mathcal B_{C_{g^{(+)}}}(e_1;L)=\varnothing.
}
\]

For `g_n=L`, choosing `t=n` gives the exact radius-`L` offset `(0,L)` arbitrarily far out. For `g_n=L+1/n`, every same-index offset has vertical coordinate strictly larger than `L`, hence lies outside the closed radius-`L` ball; the separated cross-pairs cannot create another bounded horizontal witness.

Thus both examples have identical

\[
C^\infty,
\qquad
\lambda_C(e_1),
\qquad
\mathcal A_C(e_1),
\]

but

\[
\chi_{C_{g^{(0)}}}(e_1)=1,
\qquad
\chi_{C_{g^{(+)}}}(e_1)=0.
\]

So even the **entire bounded-offset outer-limit fiber** is not sufficient for the equality predicate. The missing information is not another point of the limit set; it is whether the prelimit sets enter the closed task region before converging to its boundary.

## Prior-art and novelty audit

No broad novelty is claimed for Painleve-Kuratowski outer limits, Fell hyperspaces, distance-function convergence, or the general fact that set limits can lose boundary-side information.

- R. Tyrrell Rockafellar and Roger J. B. Wets, *Variational Analysis*, Springer (1998), DOI `10.1007/978-3-642-02431-3`. The book treats set convergence, set-valued mappings, epi-convergence, horizon constructions, and distance-based variational analysis; its set-convergence chapter is the natural general language for `mathcal A_C` and `mathcal B_C`.
- J. M. G. Fell, “A Hausdorff Topology for the Closed Subsets of a Locally Compact Non-Hausdorff Space,” *Proceedings of the American Mathematical Society* 13 (1962), 472–476, DOI `10.1090/S0002-9939-1962-0139135-6`. This is foundational prior art for local convergence of closed sets and hyperspace limits.
- Gerald Beer, “On convergence of closed sets in a metric space and distance functions,” *Bulletin of the Australian Mathematical Society* 31(3) (1985), 421–432, DOI `10.1017/S0004972700009370`. This studies the relation between Kuratowski convergence of closed sets and convergence of their distance functions.

The mathematical ingredients of the contact-fiber theorem are therefore classical set-convergence and compactness facts. The durable AF contribution is narrower: **the AF-494 equality ambiguity is exactly an order-of-operations loss between task truncation and outer-limit compression, and one critical-contact bit completes the fixed-radius phase classification even though the full untruncated translation fiber does not.**

## Falsification and boundary audit

- Finite dimensionality supplies compactness of the closed radius-`r` ball and attainment of distance to the closed set `D=cl C`. In a non-proper infinite-dimensional space, an unbounded sequence of critical hits need not yield a norm-convergent bounded-offset subsequence, so nonemptiness of this norm-topology contact fiber need not remain equivalent to recurrent hits.
- The result classifies only whether the admissible-radius hit set is unbounded, equivalently whether `Delta_C(r/2;s)` is infinite. It does not determine the finite value of `Delta_C` below or at a nonrecurrent boundary.
- The closure replacement is legitimate for the distance-defined AF-494 ambiguity profile and for `mathcal A_C`, but an application whose semantics require exact membership in a nonclosed nuisance set rather than arbitrarily close approximation must keep that distinction explicit.
- `mathcal B_C(s;r)` is task-dependent: changing the downstream acceptance region changes the truncation. This is intentional. The finding is a theorem about task-relative sufficiency, not a claim that one universal marking repairs every compression.
- The one-bit statement is specific to the binary phase question “finite or infinite ambiguity at a declared radius.” It is not a claim that one bit reconstructs the translated nuisance geometry.
- The synthetic difference sets prove insufficiency of horizon geometry, `lambda`, and even `mathcal A` for the critical equality decision in the unrestricted nuisance class. They do not imply that every natural arithmetic nuisance family exhibits this boundary pathology.
- Nothing here identifies a rational-prime discriminator or advances RH directly. It sharpens the abstract preservation theory that later arithmetic applications must satisfy.

## Relationship to AF-493 and AF-494

AF-493 shows that blow-down/horizon geometry controls only normalized first-order escape. AF-494 adds the bounded-offset translation fiber and proves that its distance from the origin gives the sharp open fixed-noise threshold, while explicitly leaving equality undecided.

AF-495 closes that exact gap. The hierarchy is now:

\[
\text{blow-down/horizon data}
\longrightarrow
\text{bounded-offset outer-limit fiber}
\longrightarrow
\text{task-truncated critical-contact fiber}.
\]

Each stage retains information discarded by the previous one. At the last step the extra information is exceptionally small for the fixed-radius phase task: after `lambda_C(s)` is known, only the boundary-contact bit `chi_C(s)` remains.
