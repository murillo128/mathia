# MC-188 — Smooth-primorial dispersion is transverse to the rough Möbius zero mode

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
q_y=\prod_{p\le y}p,
\qquad
y=c\log X,
\qquad 0<c<1,
\]

and keep the rough Möbius coefficient

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y},
\qquad
G_y(X)=\sum_{n\le X}g_y(n).
\]

The smooth-modulus variance theorem of Klurman--Mangerel--Teräväinen (`MC-S45`, Theorem 1.3) applies unconditionally to the exact primorial modulus `q_y` for all sufficiently large `X`, after choosing its parameter `epsilon` in an admissible slowly decreasing range. On reduced residue classes modulo `q_y`, Möbius and the rough coefficient coincide, so this theorem gives a genuine signed **transverse dispersion estimate** for the rough parity field.

However, the global rough sum `G_y(X)` is exactly the principal-character/constant mode of that residue-class vector. The theorem has the following sharp dichotomy:

1. if its distinguished character `chi_1` is principal, the theorem subtracts `G_y(X)` itself as the rank-one main term and gives no estimate for the rough zero mode;
2. if `chi_1` is nonprincipal, Cauchy--Schwarz bounds the rough zero mode only at logarithmic strength,

\[
|G_y(X)|
\ll \sqrt\varepsilon\,X\frac{\varphi(q_y)}{q_y}
\asymp
\frac{\sqrt\varepsilon\,X}{\log y}.
\tag{1}
\]

Moreover, the theorem's own smoothness condition prevents choosing `epsilon` polynomially small at the active cutoff. An admissible near-threshold choice has

\[
\varepsilon\asymp (\log\log X)^{-1/3},
\]

so even in the favorable nonprincipal branch (1) yields only

\[
|G_y(X)|
\ll
\frac{X}{(\log\log X)^{7/6+o(1)}}.
\tag{2}
\]

This is asymptotically much weaker than the Korobov--Vinogradov rough zero-mode estimate in `MC-187`, and far above the fixed-power budget forced by `MC-185`.

Thus smooth-primorial arithmetic-progression dispersion is a real parity-sensitive transverse category, but **it does not supply the missing rough zero mode**. Any successful use of this prior art must add a mechanism that couples the principal mode to the controlled transverse modes, rather than merely strengthening equidistribution among reduced residue classes.

## 1. The active primorial passes the smooth-modulus theorem

Klurman--Mangerel--Teräväinen prove the following form of smooth-modulus variance. Let `1<=q<=Q<=x/10`, let

\[
(\log(x/Q))^{-1/200}\le \varepsilon\le1,
\qquad
\varepsilon'=\exp(-\varepsilon^{-3}),
\]

and suppose `q` is `q^{epsilon'}`-smooth and `(x/Q)^{epsilon^2}`-typical. For a `1`-bounded multiplicative function `f`, if `chi_1 (mod q)` minimizes their pretentious distance, then

\[
\sum_{a\,(\mathrm{mod}\ q)}^{*}
\left|
\sum_{\substack{n\le x\\n\equiv a\,(\mathrm{mod}\ q)}} f(n)
-
\frac{\chi_1(a)}{\varphi(q)}
\sum_{n\le x}f(n)\overline{\chi_1(n)}
\right|^2
\ll
\varepsilon\,\varphi(q)\left(\frac{x}{q}\right)^2.
\tag{3}
\]

The point relevant here is that Theorem 1.3 has **no exceptional-modulus set** once its smoothness and typicality hypotheses hold.

Set `x=X`, `Q=q=q_y`. The prime number theorem gives

\[
\log q_y=\vartheta(y)=y+o(y),
\]

hence

\[
q_y=X^{c+o(1)}.
\tag{4}
\]

First take any fixed `epsilon>0`. Since `epsilon'>0` is then fixed,

\[
q_y^{\varepsilon'}
=
\exp((c\varepsilon'+o(1))\log X)
\gg \log X\asymp y,
\]

so `q_y` is `q_y^{epsilon'}`-smooth for large `X`.

For typicality, write

\[
Y=(X/q_y)^{\varepsilon^2}
=X^{(1-c+o(1))\varepsilon^2}.
\]

Then `Y/y -> infinity`. For every `z>=Y`, all prime divisors of `q_y` lie below `y`, and therefore

\[
|\{p\le z:p\mid q_y\}|=\pi(y)=o(\pi(z)).
\]

In particular the defining `1/100` typicality inequality holds for sufficiently large `X`. Hence (3) applies to this exact primorial modulus; the fact that `q_y` contains every small prime does not make it exceptional, because the theorem tests prime-divisor density only above the much larger typicality threshold `Y`.

## 2. Reduced residue classes are exactly the rough support

Apply (3) with `f=mu`. For each reduced residue class define

\[
A_a(X)=
\sum_{\substack{n\le X\\n\equiv a\,(\mathrm{mod}\ q_y)}}\mu(n).
\]

If `(a,q_y)=1`, every integer in that class is coprime to every prime `p<=y`; conversely every integer with `P^-(n)>y` lies in a reduced class modulo `q_y`. Therefore

\[
A_a(X)
=
\sum_{\substack{n\le X\\n\equiv a\,(\mathrm{mod}\ q_y)}}g_y(n),
\qquad
G_y(X)=\sum_{a\,(\mathrm{mod}\ q_y)}^{*} A_a(X).
\tag{5}
\]

Let

\[
C_{\chi_1}(X)=\sum_{n\le X}\mu(n)\overline{\chi_1(n)}
\]

and write the residual in (3) as

\[
E_a=A_a-rac{\chi_1(a)}{\varphi(q_y)}C_{\chi_1}.
\]

Equation (3) becomes

\[
\sum_a^{*}|E_a|^2
\ll
\varepsilon\,\varphi(q_y)(X/q_y)^2.
\tag{6}
\]

This is genuine signed information about the rough parity field, not the unsigned periodic-support estimate of `MC-183`.

## 3. The principal-mode dichotomy is exact

If `chi_1` is the principal character `chi_0`, then

\[
C_{\chi_0}(X)
=
\sum_{\substack{n\le X\\(n,q_y)=1}}\mu(n)
=G_y(X),
\]

and `chi_0(a)=1` on every reduced residue class. Thus (6) is exactly a variance estimate around the mean `G_y(X)/phi(q_y)`. Summing the residuals gives zero identically. The theorem has projected out the quantity that `MC-185` and `MC-187` need to control.

If `chi_1` is nonprincipal, orthogonality gives

\[
\sum_a^{*}\chi_1(a)=0.
\]

Using (5),

\[
G_y(X)=\sum_a^{*}E_a.
\]

Cauchy--Schwarz and (6) therefore give

\[
|G_y(X)|^2
\le
\varphi(q_y)\sum_a^{*}|E_a|^2
\ll
\varepsilon\,\varphi(q_y)^2(X/q_y)^2.
\]

This proves (1). The standard Mertens product

\[
\frac{\varphi(q_y)}{q_y}
=
\prod_{p\le y}(1-1/p)
\asymp \frac1{\log y}
\]

shows explicitly that the gain obtained from transverse dispersion is only logarithmic unless the theorem parameter `epsilon` itself can be made polynomially small.

## 4. The theorem parameter cannot provide a hidden fixed power

There is a nontrivial rate constraint in the smoothness hypothesis. Because the largest prime factor of `q_y` is of order `y`, applicability requires

\[
y\le q_y^{\varepsilon'},
\qquad
\varepsilon'=e^{-\varepsilon^{-3}}.
\tag{7}
\]

Using `log q_y ~ c log X` and `log y ~ log log X`, (7) forces

\[
e^{-\varepsilon^{-3}}
\gtrsim
\frac{\log\log X}{\log X},
\]

hence

\[
\varepsilon^{-3}
\lesssim
\log\log X-\log\log\log X+O(1).
\tag{8}
\]

So the smallest admissible scale is of order `(log log X)^(-1/3)`, not `X^{-delta}`. Conversely, for example

\[
\varepsilon_X=(\tfrac12\log\log X)^{-1/3}
\]

gives `epsilon'_X=(log X)^(-1/2)`, for which

\[
q_y^{\varepsilon'_X}
=
\exp((c+o(1))\sqrt{\log X})
\gg y,
\]

while the theorem's lower bound on `epsilon` and the typicality condition remain satisfied. Thus the logarithmic threshold in (8) is genuinely the relevant rate scale for this primorial application.

In the nonprincipal branch, inserting `sqrt(epsilon_X)=(log log X)^(-1/6+o(1))` into (1), together with `log y=(1+o(1))log log X`, gives (2). No choice allowed by (7) turns the theorem into a fixed-power estimate.

## 5. Relation to the current rough-parity frontier

`MC-183` and `MC-184` show that the unsigned pre-sieved support can already be controlled strongly; the remaining hard variable is the Möbius parity sign on that support. The present result shows that a substantial piece of **signed** structure is also accessible: the distribution of rough Möbius mass across the reduced residue classes of its own primorial sieve modulus satisfies a strong smooth-modulus dispersion theorem.

But this information is transverse to the current bottleneck. `MC-185` shows that a fixed-power rough short-interval variance target forces a fixed-power estimate on the rough zero mode. `MC-187` gives the best immediate unconditional zero-mode transfer available from the classical Mertens bound,

\[
G_y(X)\ll X\exp(-a\Phi(X)),
\]

which is already asymptotically much smaller than (2), yet still subpower. Consequently the smooth-modulus theorem does not improve the present zero-mode bound even in its favorable character branch.

This rules out a natural shortcut: **equidistribution of the signed rough coefficients among reduced residue classes, by itself, is not the missing phase-sensitive theorem.** What is missing is a coupling that forces the principal character coefficient to inherit cancellation from the transverse character modes, or another statistic that controls both simultaneously.

## 6. Prior art and novelty assessment

`MC-S45` is the primary source. Its smooth-modulus theorem, pretentious-character main term, and typicality condition are established prior art; no novelty is claimed for them. The identities (4)--(6), character orthogonality, and the Mertens product are classical.

The durable Mathia contribution is the specialization and rate audit at the exact active sieve modulus `q_y=prod_{p<=c log X}p`: the theorem really does apply to that primorial, and its character-space geometry isolates precisely why it does not pay the rough zero mode. The additional calculation (7)--(8) closes the possible loophole that one could tune the theorem's small parameter to manufacture a fixed power while retaining the required smoothness hypothesis.

A targeted search of the source paper and neighboring literature found the general smooth-modulus theorem and related squarefree/smooth-number progression results, but no basis for treating this primorial Möbius specialization as an independent analytic-number-theory theorem. It is therefore recorded as a line-specific obstruction/frontier refinement rather than a novelty claim.

## 7. Boundaries and falsification tests

- The result concerns prefix sums distributed across residue classes, not the moving short-interval variance itself. The general hybrid theorem in `MC-S45` has an exceptional-modulus set and does not automatically guarantee the exact primorial `q_y`; no hybrid smooth-primorial theorem is asserted here.
- The character `chi_1` is not assumed principal or nonprincipal. The finding is deliberately a dichotomy valid in either case.
- The nonprincipal estimate (1) is a consequence of the published variance theorem plus Cauchy--Schwarz; it is not claimed to be competitive with known direct bounds for `G_y`.
- The Mertens product is used only to read the size of `phi(q_y)/q_y`; no zeta zero-free region is imported.
- Equation (8) audits the parameter regime of this theorem, not every possible smooth-modulus dispersion theorem. A different theorem with a better dependence on the smoothness parameter could evade this rate barrier.
- A future argument using correlations between character modes, several nested primorial moduli, or a source-specific bilinear identity would contain information absent from (3) and is not ruled out.

The decisive test for a continuation of this route is therefore: **exhibit a theorem or exact identity that couples the principal rough coefficient `G_y` to the controlled nonprincipal residue/character modes with a fixed-power gain.** Merely improving transverse equidistribution without such a coupling cannot cross the `MC-185` zero-mode budget.

## Consequences for the line

The current search for an intermediate phase-sensitive category should no longer treat primorial residue-class dispersion as an unexplored missing layer. It is already available in a strong unconditional form for the active logarithmic primorial, and its failure mode is now explicit: the global rough mass is the principal character coefficient.

This narrows the next useful targets to mechanisms that mix character modes rather than estimate them independently: parity-sensitive bilinear forms, cross-scale identities, or another arithmetic coupling in which the principal coefficient cannot remain free while the transverse dispersion is small.