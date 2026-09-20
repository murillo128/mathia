---
id: WP-380
title: Critical pointed cyclotomic Grams forget factorization when reciprocal-root mass vanishes
branch: weil_positivity
status: supported
kind: prime-circle-pointed-dirichlet-primitive-shell-critical-scaling-obstruction
claim_strength: exact RH-independent asymptotic reduction showing that critically normalized primitive cyclotomic logarithms converge in pointed Dirichlet geometry to the same full-root Nyman carrier whenever the reciprocal square-root mass of their distinct prime factors tends to zero; this includes arbitrary prime-power exponents and growing-width families, so finite Gram packets become asymptotically blind to prime versus mixed-prime support while the exact Mangoldt boundary distinction is subcritical
created: 2026-09-20
related: [WP-072, WP-073, WP-161, WP-168, WP-378, WP-379]
clues: [CLUE-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical cyclotomic Mobius product formula
  - classical prime number theorem for the optional same-scale prime control
  - Nyman-Beurling and Muenz Mellin geometry already audited in WP-168
---

# WP-380 — Critical pointed cyclotomic Grams forget factorization when reciprocal-root mass vanishes

## Claim

`WP-168` found a positive critical scaling limit for the pointed local-Dirichlet geometry of the full-root controls

\[
A_N(z):=\log\frac{1-z^N}{1-z},
\qquad
U_N:=N^{-1/2}A_N,
\]

and showed that their Gram kernel converges to the classical Nyman--Mellin autocorrelation

\[
K(r)=r^{-1/2}\int_0^\infty a(x)a(x/r)\,dx,
\qquad
a(x)=H_{\lfloor x\rfloor}-\log x-\gamma.
\]

A possible objection remained important for the `weil_positivity` mandate: a composite `A_N` is an all-root control, not the actual primitive Prime-Circle shell `\log\Phi_N`. Perhaps primitive cyclotomic projection removes exactly the mixed-prime content that classicalized the full-root Gram and restores arithmetic discrimination.

It does not at the critical scale forced by `WP-073` whenever the distinct prime factors have vanishing reciprocal square-root mass.

Let

\[
F_n(z):=\log\Phi_n(z),
\qquad
W_n:=n^{-1/2}F_n,
\]

with the canonical analytic branch `F_n(0)=0`, in the pointed local Dirichlet space

\[
D_1(F)=\left\|\frac{F(z)-F(1)}{z-1}\right\|_{H^2}^2.
\]

Define

\[
\eta(n):=\sum_{p\mid n}p^{-1/2}.
\]

For every integer sequence `n_j>1` satisfying

\[
\eta(n_j)\longrightarrow0,
\]

one has

\[
\boxed{
\|W_{n_j}-U_{n_j}\|_{D_1}\longrightarrow0.
}
\tag{1}
\]

No squarefreeness or bounded-factor-width hypothesis is needed. In particular, (1) includes arbitrary prime-power exponents, every bounded-width family whose least prime factor tends to infinity, and also growing-width families for which the collective reciprocal-root mass still tends to zero.

More generally, if `n_j,m_j` satisfy

\[
\eta(n_j)+\eta(m_j)\longrightarrow0,
\qquad
\frac{m_j}{n_j}\longrightarrow r\in(0,\infty),
\]

then

\[
\boxed{
\langle W_{n_j},W_{m_j}\rangle_{D_1}
\longrightarrow K(r).
}
\tag{2}
\]

Thus the same Nyman--Beurling/Muenz modulus-square geometry classified in `WP-168` survives primitive cyclotomic projection on a substantially larger class than the original fixed-width squarefree statement.

This includes the sharp prime-versus-semiprime control. For distinct primes `p,q`,

\[
\boxed{
F_{pq}=A_{pq}-A_p-A_q.
}
\tag{3}
\]

If `p,q\to\infty`, then

\[
\left\|\frac{F_{pq}}{\sqrt{pq}}-
\frac{A_{pq}}{\sqrt{pq}}\right\|_{D_1}
\longrightarrow0,
\tag{4}
\]

although

\[
F_{pq}(1)=\log\Phi_{pq}(1)=0
\]

while for a prime shell

\[
F_p(1)=\log p=\Lambda(p).
\]

At critical half-density the latter boundary value is only

\[
\frac{\log p}{\sqrt p}\longrightarrow0.
\tag{5}
\]

The same suppression occurs on a prime-power shell `p^a`:

\[
\frac{F_{p^a}(1)}{\sqrt{p^a}}
=
\frac{\log p}{p^{a/2}}
\longrightarrow0
\qquad(p\to\infty).
\]

So the positive critical bulk geometry keeps a nonzero universal Nyman norm while the exact finite-prime selector becomes asymptotically invisible. This is not merely an all-root matched control: the clone can be an actual primitive mixed-prime cyclotomic shell.

The route now closed is

\[
\boxed{
\text{primitive Prime-Circle shell}
+\text{pointed }D_1
+\text{forced }n^{-1/2}\text{ scaling}
+\eta(n)\to0
\not\Rightarrow
\text{prime-power-selective Weil positivity}.
}
\]

A surviving pointed route must therefore retain arithmetic information before this top-divisor dominance takes over, for example through persistent small-prime mass, source-forced finite--archimedean incidence, a singular boundary object, or an indefinite/global assembly formed before the positive critical limit.

## 1. Primitive cyclotomic logarithms are Mobius combinations of full-root shells

The classical cyclotomic product identity gives, for `n>1`,

\[
\Phi_n(z)=\prod_{d\mid n}(1-z^d)^{\mu(n/d)}.
\tag{6}
\]

Since

\[
\sum_{d\mid n}\mu(n/d)=0,
\tag{7}
\]

and

\[
A_d(z)=\log(1-z^d)-\log(1-z),
\tag{8}
\]

choosing analytic logarithm branches vanishing at `z=0` yields

\[
\boxed{
F_n=\sum_{d\mid n}\mu(n/d)A_d.
}
\tag{9}
\]

The top divisor `d=n` occurs with coefficient one, so

\[
F_n-A_n
=
\sum_{\substack{d\mid n\\d<n}}
\mu(n/d)A_d.
\tag{10}
\]

Equivalently, with `e=n/d`,

\[
F_n-A_n
=
\sum_{\substack{e\mid n\\e>1}}
\mu(e)A_{n/e}.
\]

Only squarefree `e` contribute, regardless of the exponents in `n`. This is the key point hidden by the original squarefree specialization.

## 2. The defect is controlled by reciprocal-root prime mass

Taking `M=N` in `WP-168` gives

\[
\frac{D_1(A_N)}{N}
\longrightarrow
C,
\qquad
C:=\log(2\pi)-\gamma>0.
\tag{11}
\]

Hence there is a fixed `B<infinity` such that

\[
\boxed{
D_1(A_d)\le Bd
\qquad(d\ge1),
}
\tag{12}
\]

with `A_1=0` and finitely many small degrees absorbed into `B`.

Normalize (10) by `n^{-1/2}` and use the triangle inequality:

\[
\begin{aligned}
\|W_n-U_n\|_{D_1}
&\le
\frac1{\sqrt n}
\sum_{\substack{d\mid n\\d<n}}
|\mu(n/d)|\,\|A_d\|_{D_1}\\
&\le
\sqrt B
\sum_{\substack{d\mid n\\d<n}}
|\mu(n/d)|\sqrt{\frac dn}.
\end{aligned}
\tag{13}
\]

Changing variables to `e=n/d` gives the uniform bound, valid for every `n>1`,

\[
\|W_n-U_n\|_{D_1}
\le
\sqrt B
\sum_{\substack{e\mid n\\e>1}}
|\mu(e)|e^{-1/2}.
\tag{14}
\]

The nonzero terms are indexed by squarefree divisors of `rad(n)`, hence

\[
\boxed{
\|W_n-U_n\|_{D_1}
\le
\sqrt B\left[
\prod_{p\mid n}(1+p^{-1/2})-1
\right].
}
\tag{15}
\]

For squarefree `n`, the `e=n` term in the product bound corresponds to `A_1=0`, so (15) may overcount one harmless zero term; it remains a valid bound. Since `1+x\le e^x`,

\[
\boxed{
\|W_n-U_n\|_{D_1}
\le
\sqrt B\left(e^{\eta(n)}-1\right).
}
\tag{16}
\]

Therefore `eta(n_j)->0` proves (1).

The original sufficient condition is recovered immediately: if `omega(n)<=R` and `P^-(n)->infinity`, then

\[
\eta(n)\le \frac{R}{\sqrt{P^-(n)}}\longrightarrow0.
\]

But the proof now also permits `omega(n)->infinity`, provided the entire reciprocal-root mass tends to zero. For example, any family satisfying

\[
\omega(n)=o\!\left(\sqrt{P^-(n)}\right)
\]

has `eta(n)->0`. This is only a convenient sufficient condition; `eta(n)->0` itself is the sharper hypothesis supplied by the exact divisor estimate.

For semiprimes, (15) yields

\[
\left\|\frac{F_{pq}}{\sqrt{pq}}-
\frac{A_{pq}}{\sqrt{pq}}\right\|_{D_1}
\le
\sqrt B\left(p^{-1/2}+q^{-1/2}+p^{-1/2}q^{-1/2}\right),
\tag{17}
\]

where the last product term merely overcounts the zero `A_1` contribution. In particular the defect is `O(p^{-1/2}+q^{-1/2})`.

For a prime power, the identity is even sharper:

\[
F_{p^a}=A_{p^a}-A_{p^{a-1}},
\]

so

\[
\left\|p^{-a/2}F_{p^a}-p^{-a/2}A_{p^a}\right\|_{D_1}
\le \sqrt B\,p^{-1/2}.
\]

Thus repeated prime exponents do not rescue the positive critical geometry.

## 3. The full Nyman Gram kernel transfers under the same condition

Put

\[
E_n:=W_n-U_n.
\]

Under `eta(n_j)->0`, (16) gives

\[
\|E_{n_j}\|_{D_1}=o(1).
\tag{18}
\]

`WP-168` also gives bounded critical norms for `U_n` and the pairwise limit

\[
\langle U_{n_j},U_{m_j}\rangle_{D_1}
\longrightarrow K(r)
\quad\text{when }m_j/n_j\to r.
\tag{19}
\]

Therefore Cauchy--Schwarz gives

\[
\begin{aligned}
&\left|
\langle W_{n_j},W_{m_j}\rangle_{D_1}
-
\langle U_{n_j},U_{m_j}\rangle_{D_1}
\right|\\
&\qquad\le
\|E_{n_j}\|\,\|U_{m_j}\|
+\|U_{n_j}\|\,\|E_{m_j}\|
+\|E_{n_j}\|\,\|E_{m_j}\|
\longrightarrow0.
\end{aligned}
\tag{20}
\]

This proves (2). It also transfers immediately to every fixed finite Gram packet whose shell sequences all satisfy `eta->0` and have convergent pairwise degree ratios. The limiting positive form cannot recover which vectors came from prime powers and which came from genuinely mixed-prime primitive shells.

This is stronger than a bad diagonal statistic: the normalized primitive vectors themselves approach the universal full-root controls in the geometry whose positivity was supposed to carry the arithmetic theorem.

## 4. Same-scale prime and semiprime primitive shells can become indistinguishable

Choose any semiprime sequence

\[
n_j=p_jq_j,
\qquad
p_j,q_j\to\infty,
\tag{21}
\]

and let `ell_j` be a prime with

\[
\frac{\ell_j}{n_j}\to1.
\tag{22}
\]

Such a choice is available unconditionally from the classical prime number theorem, equivalently from the standard consequence that consecutive-prime ratios tend to one.

Because a prime primitive shell is exactly a full-root shell,

\[
F_{\ell_j}=A_{\ell_j},
\tag{23}
\]

while (4) gives

\[
\|W_{n_j}-U_{n_j}\|_{D_1}\to0.
\tag{24}
\]

`WP-168` with `ell_j/n_j->1` gives

\[
\|U_{\ell_j}-U_{n_j}\|_{D_1}^2
\longrightarrow
K(1)+K(1)-2K(1)=0.
\tag{25}
\]

Hence

\[
\boxed{
\left\|
\frac{F_{\ell_j}}{\sqrt{\ell_j}}
-
\frac{F_{n_j}}{\sqrt{n_j}}
\right\|_{D_1}
\longrightarrow0.
}
\tag{26}
\]

Yet

\[
F_{\ell_j}(1)=\log\ell_j,
\qquad
F_{n_j}(1)=0.
\tag{27}
\]

The apparent contradiction is resolved by critical scaling:

\[
\frac{\log\ell_j}{\sqrt{\ell_j}}\to0.
\tag{28}
\]

The geometry is internally consistent but unusable for prime-power selection: it makes a true prime shell and a true mixed-prime shell asymptotically the same vector precisely while the unnormalized arithmetic boundary functional distinguishes them.

## 5. Relation to WP-378 and WP-379

`WP-378` computed the canonical unpointed `H^2` Gram of `log Phi_n`. There the mixed-prime obstruction is visible at finite degree: the exact positive kernel Euler-factorizes, gives positive energy to composites, and carries `Lambda(n)` only through the unbounded boundary trace at `z=1`.

The present result tests the principal escape left open there: move to the non-rotation-invariant pointed local Dirichlet metric of `WP-072`, where boundary evaluation is controlled and the degree-cover normalization itself forces the critical half-density. The obstruction changes form but does not disappear. Primitive inclusion--exclusion terms are controlled by the reciprocal-root mass of distinct prime divisors. When that mass vanishes, all proper-divisor corrections disappear in the critical norm and the primitive shell classicalizes to the same Nyman carrier as the full-root shell.

`WP-379` found a two-channel version of the same loss for `A_N(z)` and `A_N(-z)`, but its mixed-degree controls were still full-root objects. Equation (1) removes that loophole for actual primitive cyclotomic shells and now includes arbitrary exponents and some growing-width families.

The three findings expose the same tension at different topological levels:

\[
\text{exact cyclotomic arithmetic boundary}
\quad\text{versus}\quad
\text{positive interior/critical bulk geometry}.
\]

The arithmetic selector survives at finite scale, but the positive critical geometry either has the wrong support (`WP-378`) or asymptotically forgets the support (`WP-380`).

## 6. Aggressive falsification and scope boundary

The negative result is intentionally not universal.

First, `eta(n)->0` is a sufficient condition supplied by the top-divisor estimate, not a necessary condition for collapse. Families with persistent small-prime mass, such as `n=2p`, satisfy `eta(n)>=2^{-1/2}` and lie outside the theorem. A lower-divisor channel can remain order one there. `WP-379` already shows that the most immediate half-turn channel does not rescue the finite-prime contrast, but (1) does not classify every small-prime defect.

Second, growing factor width by itself is no longer an escape. The theorem includes every growing-width family with `eta(n)->0`. What remains outside this argument is growing-width or other incidence for which the reciprocal-root mass does not vanish, and any successful use of that regime would still have to be source-forced rather than tuned to encode the desired support.

Third, the result concerns the positive pointed `D_1` Gram after the `n^{-1/2}` normalization forced by the cover isometry. It does not rule out an indefinite precritical pairing, a singular boundary topology, a genuinely finite--archimedean relation formed before scalar Hilbert completion, or a cohomological object whose sign theorem is not the pointed Gram norm.

Fourth, nothing here generates the Gamma term or the polar counterterm of the completed explicit formula. The limiting kernel is exactly the `WP-168` Nyman modulus-square carrier, so its positivity remains unconditional autocorrelation positivity and cannot force RH.

The consequence is therefore precise: a surviving construction must use information not controlled away by the distinct-prime reciprocal-root defect estimate, or must couple the arithmetic boundary to the global sign mechanism before the critical Hilbert completion forgets it.

## 7. Prior-art and novelty audit

No new theorem about cyclotomic polynomials, the prime number theorem, or Nyman--Beurling geometry is claimed. The Mobius product (6), the boundary value `Phi_n(1)`, and the prime number theorem are classical. `WP-168` already identified the full-root critical scaling kernel with the classical Nyman--Muenz Mellin modulus square.

A bounded literature search for combinations of cyclotomic logarithms, local Dirichlet spaces, Nyman--Beurling geometry, prime-factor asymptotics, and primitive-shell limits did not locate a source stating the branch-specific reduction (1)--(2). The strengthening from bounded squarefree width to `eta(n)->0` uses only the same classical Mobius identity and the `WP-168` linear energy bound: changing variables from divisors `d` to squarefree complementary divisors `e=n/d` exposes that prime-power exponents are irrelevant and that width matters only through the aggregate product `prod_{p|n}(1+p^{-1/2})`.

The substantive contribution is therefore **Mathia-local search-space closure**, not a broad novelty claim: primitive cyclotomic projection still classicalizes to the full-root Nyman carrier on every family with vanishing reciprocal-root prime mass, including some growing-width families and arbitrary exponents.

This is not a variant of classical Weil positivity, Hilbert--Polya, Connes/trace, Frobenius/cohomology, Sonin/localization, or an inserted zero functional. No zero data are used, and the sign is simply the independent positivity of the pointed Hilbert Gram. That is exactly why the matched control is decisive: a positive geometry whose vectors can forget the arithmetic support cannot itself supply the required finite Weil selector.

## Consequence for the research line

The pointed Prime-Circle route is narrower than the original form of this finding stated. Squarefreeness and bounded factor width were artifacts of the first estimate, not essential hypotheses. The natural control parameter of the proof is

\[
\eta(n)=\sum_{p\mid n}p^{-1/2}.
\]

Whenever `eta(n)->0`, lower-divisor corrections encoding primitiveness are too small in `D_1` after forced half-density normalization, regardless of prime-power exponents and even when the number of distinct primes grows.

The next useful test should therefore target a regime not killed by (16), rather than merely add more factors or another bounded finite channel to the same critical Gram. The most concrete surviving classes are a source-forced construction with persistent small-prime/archimedean coupling; a nonvanishing-`eta` growing-width incidence whose complexity is intrinsic; or a singular boundary/cohomological topology in which the exact `Lambda` trace remains finite and its global sign follows from an independent theorem. Any candidate should still be checked against the prime/semiprime control (26) before its positivity is treated as arithmetic evidence.