# NB-319 — Nested adjacent cancellations fill every mesoscopic primitive annulus

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-315, NB-316, NB-318
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + PHASE-SPACE + ANNULAR-LOCALIZATION + CENTERED-PRIMITIVE + ADJACENT-WITNESS + METHOD-BOUNDARY + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
F_u(t):=u(1/t),
\qquad
\widetilde F_u(t):=F_u(t)-\mu_N(u),
\]

and let

\[
G_u(T):=\int_0^T\widetilde F_u(s)\,ds
\]

be the centered reciprocal-shell primitive used in `NB-315`--`NB-318`. For an integer scale `M>=1`, define the annular Hilbert primitive amplification

\[
\mathfrak H_N(M)
:=
\sup_{0\ne u\in U_N}
\frac{\sup_{M\le T\le3M}|G_u(T)|}{\|u\|_2}.
\tag{1}
\]

Then for every integer `N>=4` and every integer `M` satisfying

\[
8\le M\le\frac{N^2}{2},
\tag{2}
\]

one has the explicit lower bound

\[
\boxed{
\mathfrak H_N(M)
\ge
\frac{M}{32\sqrt{\log M}}.
}
\tag{3}
\]

Thus the near-quadratic primitive obstruction of `NB-316` is not confined to reciprocal time `K=Theta(N^2)`. Because the finite sections are nested, a smaller adjacent cancellation with index

\[
n=\lfloor\sqrt{2M}\rfloor
\]

reproduces the same mechanism inside **every** reciprocal annulus `[M,3M]` from constant scale through `N^2/2`.

In particular, if `M_N->infinity` and `M_N<=N^2/2`, then

\[
\boxed{
\mathfrak H_N(M_N)
\gg
\frac{M_N}{\sqrt{\log M_N}}.
}
\tag{4}
\]

Consequently no uniform local primitive estimate of the form

\[
\sup_{M\le T\le3M}|G_u(T)|
\le C M^{1-\varepsilon}\|u\|_2
\tag{5}
\]

can hold throughout the linear-to-quadratic range for any fixed `epsilon>0`. Localizing the `NB-315` integration-by-parts argument to a reciprocal annulus therefore cannot by itself buy a positive power of the dilation scale through a uniformly smaller primitive envelope.

This is a boundary for the **primitive-majorant route** only. It is not a lower bound for the weighted bilinear mixing error, not a lower bound for `beta_(N+1)(m)`, and not a target-occupation or Riemann-hypothesis statement. Cancellation in the actual weighted pairing remains a genuine escape route.

## 1. A smaller adjacent witness can be placed at any mesoscopic scale

Fix `M` as in (2) and put

\[
n:=\lfloor\sqrt{2M}\rfloor.
\tag{6}
\]

Then `M>=8` gives `n>=4`, while `M<=N^2/2` gives `n<=N`. Hence the adjacent cancellation

\[
u_n:=g_n-\frac{n-1}{n}g_{n-1}
\tag{7}
\]

belongs to `U_n` and therefore to `U_N`.

`NB-316` computes this witness exactly. Its centered reciprocal profile has period

\[
P_n=n(n-1),
\tag{8}
\]

its centered primitive is `P_n`-periodic, and an exact maximum is attained at

\[
K_n^*:=\left\lfloor\frac n2\right\rfloor(n-1),
\tag{9}
\]

with

\[
\boxed{
|G_{u_n}(K_n^*)|
=
\frac{\lfloor n^2/4\rfloor}{2n}.
}
\tag{10}
\]

Periodicity therefore gives the same value at

\[
K_n:=K_n^*+P_n.
\tag{11}
\]

The point of adding one period is that it places the already-known exact maximum into the prescribed annulus without changing its size.

## 2. The translated maximum always lies in `[M,3M]`

From the definition of `n`,

\[
n^2\le2M.
\tag{12}
\]

Also, for every `M>=8`,

\[
n^2\ge M.
\tag{13}
\]

Indeed `n>=\sqrt{2M}-1`, and `(\sqrt{2M}-1)^2>=M` once `M>=6`.

The upper location bound follows immediately from

\[
K_n^*\le\frac{n^2}{2}\le M,
\qquad
P_n<n^2\le2M,
\]

so

\[
\boxed{K_n\le3M.}
\tag{14}
\]

For the lower bound it is enough to show `P_n>=M`. If `n=4`, the condition `floor(sqrt(2M))=4` and `M>=8` gives `8<=M<=12`, while `P_4=12`. If `n>=5`, then

\[
M<\frac{(n+1)^2}{2}
\le n(n-1)=P_n,
\tag{15}
\]

because

\[
2n(n-1)-(n+1)^2=n^2-4n-1>0
\qquad(n\ge5).
\]

Therefore

\[
\boxed{M\le K_n\le3M.}
\tag{16}
\]

So every admissible annulus contains an exact primitive maximum of an adjacent witness from a nested smaller Nyman section.

## 3. Normalizing by the physical Nyman norm gives almost-linear annular growth

`NB-304` and `NB-316` give

\[
\|u_n\|_2^2
\le
\frac{B_n}{n^2},
\qquad
B_n:=2H_{n-2}+1+\frac{\pi^2}{18}.
\tag{17}
\]

Combining (10), (11), and (17),

\[
\frac{|G_{u_n}(K_n)|}{\|u_n\|_2}
\ge
\frac{\lfloor n^2/4\rfloor}{2\sqrt{B_n}}.
\tag{18}
\]

For `n>=4`,

\[
\lfloor n^2/4\rfloor\ge\frac{n^2}{8},
\]

and (13) therefore gives

\[
\frac{|G_{u_n}(K_n)|}{\|u_n\|_2}
\ge
\frac{M}{16\sqrt{B_n}}.
\tag{19}
\]

The harmonic factor is at most logarithmic. Since `H_(n-2)<=1+log n` and `n^2<=2M`,

\[
B_n
\le
3+\frac{\pi^2}{18}+\log(2M)
\le4\log M
\qquad(M\ge8).
\tag{20}
\]

Substitution into (19) gives

\[
\frac{|G_{u_n}(K_n)|}{\|u_n\|_2}
\ge
\frac{M}{32\sqrt{\log M}}.
\tag{21}
\]

Because `u_n in U_N` and `K_n in [M,3M]`, equation (21) proves (3).

The constants are intentionally conservative. The structural point is the scale: after physical Hilbert normalization, **every mesoscopic annulus up to quadratic reciprocal depth contains primitive amplification within a square-root logarithm of linear growth in the annulus radius**.

## 4. What this changes after NB-318

`NB-318` proved that for every fixed `C`, the fixed-time evaluation norm

\[
\mathcal H_N(K)
:=
\sup_{0\ne u\in U_N}
\frac{|G_u(K)|}{\|u\|_2}
\]

is `O_C(N^2)` throughout `K<=CN`. It also observed that the top-index adjacent witness from `NB-316` reaches its maximum only at `K=Theta(N^2)`. Taken alone, that leaves open the possibility that the primitive obstruction is essentially an endpoint phenomenon near quadratic reciprocal time.

The present finding rules out that interpretation. The same adjacent construction is available inside every nested section `U_n subset U_N`. Choosing `n approximately sqrt(M)` moves its natural reciprocal period `n(n-1)` to scale `M`, while retaining a physical normalized primitive of size `M/sqrt(log M)`. Thus the obstruction is **multiscale**: it fills the entire mesoscopic phase-space corridor rather than appearing only when the top index `N` has had quadratic reciprocal time to drift.

This also clarifies what a long-window improvement can and cannot look like. A theorem of the form

\[
\sup_{M\le T\le3M}|G_u(T)|
\lesssim M^{1-\varepsilon}\|u\|_2
\]

is impossible uniformly over `U_N` in this range. Any successful improvement of the `NB-315` rank-one mixing threshold must therefore either tolerate almost-linear primitive size and exploit the `1/t^2`-type weight more efficiently, use cancellation between different primitive excursions, or estimate the bilinear mixing error directly without replacing it by a primitive supremum.

## 5. Relation to the moving rank-one problem

The integration-by-parts step in `NB-315` controls the centered projected-dilation error through a uniform primitive envelope. A natural response to `NB-318` is to try to replace the global quantity `||G_u||_infinity` by a local envelope at the reciprocal times actually sampled by the weight. Equation (3) shows that **localization alone does not create a polynomial saving in reciprocal radius**: on every annulus before the quadratic edge there is an admissible unit source whose primitive is already essentially linear in that radius.

This does not imply that the corresponding weighted mixing integral is large. The adjacent witness is exactly the family for which `NB-305` showed strong self-dilation decorrelation, illustrating that a large primitive excursion can be nearly invisible after the signed weighted pairing. Therefore (3) should be read as a method boundary, not as evidence that the true projected-dilation transition must occur at quadratic scale.

The strongest remaining escape is consequently more specific than before: exploit cancellation **inside the bilinear pairing** rather than trying to win a positive power through any scale-uniform `L^infinity` control of the centered primitive. Frequency-sensitive norms, weighted square functions, or direct reduced-denominator analysis of the mixing integral are not constrained by (3).

## 6. Adversarial checks and prior-art audit

The scale placement uses only exact formulas already proved in `NB-316`. The same centering convention is preserved because `u_n` is considered as the same function after embedding `U_n subset U_N`; its reciprocal mean is intrinsic to the periodic profile and does not change with the ambient section. Adding one full period is legitimate because the centered profile has zero integral over that period, so the primitive itself, not merely its derivative, is periodic.

The potentially fragile inequality is the lower annulus boundary. It does not rely on an asymptotic: `n=4` is checked separately, and for every `n>=5` equation (15) puts the full period beyond `M`. The normalization also uses an upper bound on `||u_n||_2`, which is the correct direction for producing a lower bound on the normalized primitive. No assertion is made for each individual reciprocal time inside the annulus; only existence of at least one large evaluation time is proved.

A fresh prior-art audit checked the neighboring fractional-part and Nyman--Beurling literature, including Balazard--Martin on multiplicative autocorrelation of the fractional-part function (arXiv:1305.4395), Báez-Duarte--Balazard--Landreau--Saias on the same autocorrelation structure, Balazard on integer dilations of the fractional-part function, Werner Ehm's recent Gram-matrix analysis (arXiv:2405.06349), and recent Gram/lattice work of Carvill. The material reviewed contains the expected autocorrelation, dilation, Gram, and periodic fractional-part machinery, but I did not identify this finite-section annular localization statement obtained by nesting adjacent cancellations. This is recorded only as the boundary of the audit, not as a claim of bibliographic novelty.

No external theorem is load-bearing for the proof: the result follows from the exact adjacent-witness formulas and norm estimate already canonical in `NB-304`/`NB-316`, plus elementary scale inequalities. Therefore `SOURCES.md` requires no new dependency.

## Classification and next discriminator

This is a rigorous negative/method-boundary finding. It strengthens the phase-space diagnosis of `NB-318`: primitive-large directions do not merely escape beyond linear reciprocal time; nested adjacent cancellations regenerate them at every larger scale up to the quadratic frontier.

The next useful discriminator is therefore not another annular `L^infinity` primitive bound with a power saving in `M`. The more promising question is whether the **weighted bilinear error itself** admits cancellation unavailable to the primitive supremum. An estimate on that pairing which beats the almost-linear annular witness could still move the moving rank-one transition substantially below the superquadratic sufficient regime of `NB-315`, and this finding does not obstruct such a route.
