---
id: WP-380
title: Critical pointed cyclotomic Grams forget fixed-width squarefree factorization
branch: weil_positivity
status: supported
kind: prime-circle-pointed-dirichlet-primitive-shell-critical-scaling-obstruction
claim_strength: exact RH-independent asymptotic reduction showing that critically normalized primitive cyclotomic logarithms on every fixed-width squarefree family with least prime factor tending to infinity converge in pointed Dirichlet geometry to the same full-root Nyman carrier as prime shells, so finite Gram packets become asymptotically blind to prime versus mixed-prime support while the exact Mangoldt boundary distinction is subcritical
created: 2026-09-20
related: [WP-072, WP-073, WP-161, WP-168, WP-378, WP-379]
clues: [CLUE-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical cyclotomic Mobius product formula
  - classical prime number theorem for the optional same-scale prime control
  - Nyman-Beurling and Muenz Mellin geometry already audited in WP-168
---

# WP-380 — Critical pointed cyclotomic Grams forget fixed-width squarefree factorization

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

A possible objection remained important for the `weil_positivity` mandate: a composite `A_N` is an all-root control, not the actual primitive Prime-Circle shell `\log\Phi_N`. Perhaps the primitive cyclotomic shell removes exactly the mixed-prime content that classicalized the full-root Gram and thereby restores arithmetic discrimination.

It does not, at the critical scale forced by `WP-073`, on a broad source-native family.

Let

\[
F_n(z):=\log\Phi_n(z)
\]

with the canonical analytic branch satisfying `F_n(0)=0`, and put

\[
W_n:=n^{-1/2}F_n
\]

in the pointed local Dirichlet space

\[
D_1(F)=\left\|\frac{F(z)-F(1)}{z-1}\right\|_{H^2}^2.
\]

Fix an integer `R>=1`. For every sequence of squarefree integers `n_j` satisfying

\[
\omega(n_j)\le R,
\qquad
P^-(n_j):=\min_{p\mid n_j}p\longrightarrow\infty,
\]

one has

\[
\boxed{
\|W_{n_j}-U_{n_j}\|_{D_1}\longrightarrow0.
}
\tag{1}
\]

Thus any fixed number of growing prime factors becomes invisible to the critically normalized positive pointed geometry. More generally, if `n_j,m_j` are two such squarefree sequences and

\[
\frac{m_j}{n_j}\longrightarrow r\in(0,\infty),
\]

then

\[
\boxed{
\langle W_{n_j},W_{m_j}\rangle_{D_1}
\longrightarrow K(r),
}
\tag{2}
\]

exactly the same kernel as for the full-root controls and hence the same Nyman--Beurling/Muenz modulus-square geometry classified in `WP-168`.

This includes the sharp prime-versus-semiprime control. For distinct primes `p,q`,

\[
\boxed{
F_{pq}=A_{pq}-A_p-A_q.
}
\tag{3}
\]

If `p,q\to\infty`, then

\[
\left\|\frac{F_{pq}}{\sqrt{pq}}-rac{A_{pq}}{\sqrt{pq}}\right\|_{D_1}
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

So the positive critical bulk geometry keeps a nonzero universal Nyman norm while the exact finite-prime selector becomes asymptotically invisible. This is not merely an all-root matched control: the clone is now an **actual primitive mixed-prime cyclotomic shell**.

The result closes the route

\[
\boxed{
\text{primitive Prime-Circle shell}
+\text{pointed }D_1
+\text{forced }n^{-1/2}\text{ scaling}
\not\Rightarrow
\text{prime-power-selective Weil positivity}
}
\]

for every fixed-width squarefree family whose prime factors all escape to infinity. A surviving pointed route must retain arithmetic information before this top-divisor dominance takes over, for example through source-forced small-prime/archimedean incidence, growing-width coupling, a singular boundary object, or an indefinite finite--archimedean assembly formed before the positive critical limit.

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

choosing the analytic logarithm branches that vanish at `z=0` yields the exact identity

\[
\boxed{
F_n=\sum_{d\mid n}\mu(n/d)A_d.
}
\tag{9}
\]

The top divisor `d=n` occurs with coefficient one. Thus

\[
F_n-A_n
=
\sum_{\substack{d\mid n\\ d<n}}
\mu(n/d)A_d.
\tag{10}
\]

For `n=pq` with distinct primes, (10) is exactly (3).

This identity is elementary but important for the research question: primitive-shell projection does not create a new analytic object unrelated to the full-root family. It is an inclusion--exclusion of lower-degree full-root shells. The only question is whether those lower-degree terms survive the intrinsic critical normalization.

## 2. WP-168 supplies the uniform linear energy bound

Taking `M=N` in `WP-168` gives

\[
\frac{D_1(A_N)}{N}
\longrightarrow
C,
\qquad
C:=\log(2\pi)-\gamma>0.
\tag{11}
\]

Consequently there is a fixed constant `B<infinity` such that

\[
\boxed{
D_1(A_d)\le Bd
\qquad(d\ge1),
}
\tag{12}
\]

where `A_1=0` and finitely many small degrees are absorbed into `B`.

Normalize (10) by `n^{-1/2}` and use the triangle inequality in the pointed Hilbert seminorm:

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

Now assume `n` is squarefree. Then every divisor contributes with `|mu|=1`, and the divisor sum factorizes exactly:

\[
\sum_{d\mid n}\sqrt{\frac dn}
=
\prod_{p\mid n}\left(1+p^{-1/2}\right).
\tag{14}
\]

Removing the top divisor gives

\[
\boxed{
\|W_n-U_n\|_{D_1}
\le
\sqrt B
\left[
\prod_{p\mid n}(1+p^{-1/2})-1
\right].
}
\tag{15}
\]

If `omega(n)<=R`, then

\[
\prod_{p\mid n}(1+p^{-1/2})-1
\le
\left(1+P^-(n)^{-1/2}\right)^R-1,
\tag{16}
\]

which tends to zero as `P^-(n)->infinity`. Equations (15)--(16) prove (1).

For semiprimes this reduces to the transparent estimate

\[
\left\|\frac{F_{pq}}{\sqrt{pq}}-rac{A_{pq}}{\sqrt{pq}}\right\|_{D_1}
\le
\sqrt B\left(p^{-1/2}+q^{-1/2}+ (pq)^{-1/2}\,0\right),
\tag{17}
\]

where the `A_1` term is zero. In particular the defect is `O(p^{-1/2}+q^{-1/2})`.

## 3. The full Nyman Gram kernel transfers to primitive mixed-prime shells

Put

\[
E_n:=W_n-U_n.
\]

On the fixed-width squarefree families above, (1) says

\[
\|E_n\|_{D_1}=o(1).
\tag{18}
\]

`WP-168` also gives bounded critical norms for `U_n` and the exact pairwise limit

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

Combining (19)--(20) proves (2).

The statement extends immediately from one pair to every fixed finite Gram packet: if finitely many shell sequences have bounded squarefree width, least prime factor tending to infinity, and convergent pairwise degree ratios, their entire critically normalized primitive-shell Gram matrix converges entrywise to the same matrix obtained from the universal full-root Nyman kernel. The limiting positive form therefore cannot recover which entries came from primes and which came from genuinely mixed-prime primitive shells.

This is stronger than saying that one diagonal statistic is wrong. At the critical scale, the **vectors themselves** differ from their full-root controls by `o(1)` in the geometry whose positivity was supposed to carry the arithmetic theorem.

## 4. Same-scale prime and semiprime primitive shells can become indistinguishable

The previous section already gives a matched composite control without using any distribution theorem for primes. There is also a particularly sharp same-scale version.

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
\left\|W_{n_j}-U_{n_j}\right\|_{D_1}\to0.
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

Yet the exact cyclotomic boundary values are maximally different in support:

\[
F_{\ell_j}(1)=\log\ell_j,
\qquad
F_{n_j}(1)=0.
\tag{27}
\]

The contradiction is only apparent because critical normalization suppresses the prime boundary value:

\[
\frac{\log\ell_j}{\sqrt{\ell_j}}\to0.
\tag{28}
\]

Thus the geometry is internally consistent but unusable for the desired selection: its positive critical topology makes a true prime shell and a true mixed-prime shell asymptotically the same vector precisely while the unnormalized arithmetic boundary functional distinguishes them.

This supplies a stronger matched control than the all-degree control in `WP-168` or the rotated full-root control in `WP-379`.

## 5. Relation to WP-378 and WP-379

`WP-378` computed the canonical unpointed `H^2` Gram of `log Phi_n`. There the mixed-prime obstruction is visible at finite degree: the exact positive kernel Euler-factorizes, gives positive energy to composites, and carries `Lambda(n)` only through the unbounded boundary trace at `z=1`.

The present result tests the principal escape left open there: move to the non-rotation-invariant pointed local Dirichlet metric of `WP-072`, where boundary evaluation is controlled and the degree-cover normalization itself forces the critical half-density. The obstruction changes form but does not disappear. Rather than a finite-degree Euler-factorized Hardy kernel, one gets **top-divisor dominance**: primitive inclusion--exclusion terms from every proper divisor become negligible after critical normalization whenever the number of prime factors is fixed and all of them grow. The primitive shell then classicalizes to the same Nyman carrier as the full-root shell.

`WP-379` found a two-channel version of the same loss for `A_N(z)` and `A_N(-z)`, but its mixed-degree controls were still full-root objects. Equation (1) removes that loophole for actual primitive cyclotomic shells on fixed-width squarefree families.

The three findings therefore expose the same tension at different topological levels:

\[
\text{exact cyclotomic arithmetic boundary}
\quad\text{versus}\quad
\text{positive interior/critical bulk geometry}.
\]

The arithmetic selector survives at finite scale, but the positive critical geometry either has the wrong support (`WP-378`) or asymptotically forgets the support (`WP-380`).

## 6. Aggressive falsification and scope boundary

The negative result is intentionally not universal.

First, the hypothesis `P^-(n)->infinity` matters. Families with a fixed small prime factor, such as `n=2p`, do not satisfy (16): a lower-divisor term can remain at order one after critical normalization. Such families require a separate analysis; `WP-379` already shows that the most immediate half-turn channel does not rescue the finite-prime contrast, but (1) by itself does not classify every small-prime defect.

Second, bounded factor width matters. If `omega(n)` grows, the product in (15) need not tend to one even if individual primes grow. Growing-width incidence remains outside this theorem and would have to be source-forced rather than chosen to encode the desired support.

Third, this result concerns the positive pointed `D_1` Gram after the `n^{-1/2}` normalization forced by the cover isometry. It does not rule out an indefinite precritical pairing, a singular boundary topology, a genuinely finite--archimedean relation formed before scalar Hilbert completion, or a cohomological object whose sign theorem is not the pointed Gram norm.

Fourth, nothing here generates the Gamma term or the polar counterterm of the completed explicit formula. The limiting kernel is exactly the `WP-168` Nyman modulus-square carrier, so its positivity remains unconditional autocorrelation positivity and cannot force RH.

These limitations sharpen rather than weaken the research consequence: a surviving construction must use information that is **not** asymptotically contained in a fixed finite collection of lower-divisor corrections to the universal full-root carrier.

## 7. Prior-art and novelty audit

No new theorem about cyclotomic polynomials, the prime number theorem, or Nyman--Beurling geometry is claimed. The Mobius product (6), the boundary value `Phi_n(1)`, and the prime number theorem are classical. `WP-168` already identified the full-root critical scaling kernel with the classical Nyman--Muenz Mellin modulus square.

A bounded literature search for combinations of local Dirichlet spaces, cyclotomic logarithms, semiprime primitive shells, and Nyman--Beurling geometry did not locate a source stating the branch-specific asymptotic reduction (1)--(2). The mathematical ingredients are elementary once the `WP-168` scaling theorem is available. The substantive contribution is therefore **Mathia-local search-space closure**: the Nyman classicalization of the full-root control survives primitive cyclotomic projection on every fixed-width squarefree family whose least prime factor grows, and a genuine mixed-prime shell can be made asymptotically indistinguishable from a prime shell in the intrinsic critical pointed norm.

This is not a variant of classical Weil positivity, Hilbert--Polya, Connes/trace, Frobenius/cohomology, Sonin/localization, or an inserted zero functional. No zero data are used, and the sign is simply the independent positivity of the pointed Hilbert Gram. That is exactly why the matched control is decisive: a geometry whose positive vectors cannot asymptotically distinguish prime support from mixed-prime support cannot itself yield the required finite Weil selector.

## Consequence for the research line

The pointed Prime-Circle route is now narrower than `WP-379` alone showed. Passing from full roots to the actual primitive shell does not restore arithmetic discrimination at the critical scale whenever only finitely many growing prime factors are involved. The lower-divisor corrections that encode primitiveness are too small in `D_1` after the forced half-density normalization.

The next useful test should therefore target one of the hypotheses that made (15) vanish rather than add another bounded finite channel to the same critical Gram. The most concrete surviving classes are: a source-forced coupling in which a small finite place and the archimedean sector enter the same object before the critical limit; a growing-width incidence whose complexity is intrinsic rather than tuned; or a singular boundary/cohomological topology in which the exact `Lambda` trace remains finite and its global sign follows from an independent theorem. Any candidate should be compared against the prime/semiprime control (26) before its positivity is treated as arithmetic evidence.
