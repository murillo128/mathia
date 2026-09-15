# AF-370 — Hamburger rigidity makes the Riemann functional equation faithful only relative to its analytic source class

**Status:** `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `SOURCE-CLASS`, `RECOVERY`, `FUNCTIONAL-EQUATION`, `PRIOR-ART-REDIRECT`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be the class of ordinary Dirichlet series

\[
f(s)=\sum_{n\ge 1}a(n)n^{-s}
\]

that converge absolutely for `Re(s)>1` and for which `(s-1)f(s)` extends to an entire function of finite order. Consider the exact Riemann self-duality condition

\[
\pi^{-s/2}\Gamma(s/2)f(s)
=
\pi^{-(1-s)/2}\Gamma((1-s)/2)f(1-s).
\tag{1}
\]

Hamburger's classical converse theorem implies that the fiber of `(1)` inside `H` is one-dimensional:

\[
\boxed{f\in H\text{ and }(1)\quad\Longrightarrow\quad f=c\,\zeta}
\tag{2}
\]

for some constant `c`. Therefore adjoining the ordinary Dirichlet normalization

\[
a(1)=1
\tag{3}
\]

makes the retained analytic structure fully faithful to the distinguished function:

\[
\boxed{f\in H,\ (1),\ a(1)=1\quad\Longrightarrow\quad f=\zeta.}
\tag{4}
\]

In Arithmetic Fidelity terms, this is a clean positive example of **source-class-relative recovery**. The functional equation is not being treated as a magical standalone label. Its discriminatory power comes from coupling a rigid global reflection law to an admissible class carrying an ordinary integer Dirichlet expansion and strong whole-plane growth control. Inside that class the symmetry collapses the admissible fiber to scalar multiples of `zeta`; one scalar normalization then removes the remaining ambiguity.

This answers the specific boundary left open by AF-369 in a broader category than finite Euler modifications. AF-369 showed that, on integer-supported Delone Beurling systems, the zero divisor is non-faithful while pole residue `1` becomes faithful after the source class is narrowed. AF-370 gives a different coupling: within Hamburger's ordinary-Dirichlet finite-order class, the exact completed Riemann functional equation is already rigid up to scale, and the coefficient normalization `a(1)=1` completes recovery.

No novelty is claimed for Hamburger's theorem. The durable result here is the fidelity classification of which **jointly retained resources** make the symmetry discriminating, and the explicit failure boundary when those source hypotheses are removed.

## Derivation from Hamburger's converse theorem

A standard modern statement, recalled explicitly by Kaczorowski, Molteni and Perelli, is the following paired theorem. Suppose

\[
f(s)=\sum_{n\ge1}a(n)n^{-s},\qquad
 g(s)=\sum_{n\ge1}b(n)n^{-s}
\]

are absolutely convergent for `Re(s)>1`, `(s-1)f(s)` and `(s-1)g(s)` are entire functions of finite order, and

\[
\pi^{-s/2}\Gamma(s/2)f(s)
=
\pi^{-(1-s)/2}\Gamma((1-s)/2)g(1-s).
\tag{5}
\]

Then

\[
f(s)=g(s)=c\zeta(s).
\tag{6}
\]

Equation `(2)` is simply the self-dual specialization `g=f`. Since equality of absolutely convergent ordinary Dirichlet series is coefficientwise unique in `Re(s)>1`, the coefficient at `1^{-s}` of `c\zeta(s)` is `c`. Hence `(3)` forces `c=1`, proving `(4)`.

The important point is categorical. The same reflection formula is acting on a source representation that already remembers the integer frequency lattice `\{\log n\}` through an ordinary Dirichlet expansion. The finite-order meromorphic continuation prevents arbitrary extra symmetric entire factors from being inserted while staying in the admitted Hamburger class. The recovery theorem is therefore about the conjunction

\[
\text{ordinary Dirichlet source}
+
\text{finite-order global continuation}
+
\text{exact Riemann reflection}
+
\text{one scalar normalization},
\]

not about reflection symmetry in isolation.

## Why the source class is load-bearing

The hypotheses cannot be deleted and the conclusion retained as a general statement about functions satisfying a formal `s\leftrightarrow1-s` symmetry.

First, without the Dirichlet-series and finite-order restrictions, one can multiply a completed symmetric function by nonconstant symmetric zero-free factors. For example, if `\Lambda(s)=\Lambda(1-s)`, then formally

\[
\widetilde\Lambda(s)=e^{q(s(1-s))}\Lambda(s)
\]

has the same reflection symmetry for any entire `q`; such a factor need not correspond to an ordinary Dirichlet series in Hamburger's class. Reflection alone therefore leaves an enormous fiber.

Second, the literature contains non-zeta functions described as satisfying Riemann's functional equation once Hamburger's exact admissible category is relaxed. Nakamura, for example, constructs functions from shifted Dirichlet `L`-functions that obey the Riemann reflection law but are not `zeta`. This is not a contradiction to Hamburger: those objects do not satisfy the full ordinary-Dirichlet/finite-order hypothesis package used in `(5)`.

Third, even within neighboring `L`-function categories, functional equations need not determine a unique function. Kaczorowski, Molteni and Perelli emphasize that the Riemann-zeta one-dimensional phenomenon does not extend automatically to primitive Dirichlet `L`-functions; extra Euler-product or arithmetic structure may be needed. Thus the recovery statement is genuinely **category-relative** rather than a universal property of functional equations.

## Fidelity interpretation

Let `C` denote the coarse retained statement “the source satisfies the exact Riemann completed functional equation.” On an unrestricted function class the fiber `C^{-1}(true)` is large. On Hamburger's source class `H`, however, the same fiber is

\[
C^{-1}(true)\cap H=\{c\zeta:c\in\mathbb C\}.
\tag{7}
\]

The normalization map `N(f)=a(1)` then separates this residual one-dimensional gauge:

\[
(C,N)^{-1}(true,1)\cap H=\{\zeta\}.
\tag{8}
\]

This gives an exact instance of a general Arithmetic Fidelity principle suggested by AF-369: **the discriminatory content of retained data cannot be priced independently of the admissible source class**. A datum can be useless on a broad category and complete on a rigid one. Conversely, narrowing the category can be as information-bearing as adding another observable.

The distinction also prevents a misleading comparison of “how many scalars” are retained. AF-369's pole residue is one scalar and suffices for a binary prime/non-prime discriminator only after an integer-supported Delone classification has reduced the source freedom to finite arithmetic modifications. Here the functional equation is an infinite global relation and the source class itself contains strong analytic structure. Neither lift is intrinsically smaller or stronger without declaring the source category and target discriminator.

## Arithmetic consequence and limit

For a candidate prime-derived construction, recovering the exact Riemann functional equation inside Hamburger's ordinary Dirichlet class is therefore a legitimate arithmetic-specificity gate: a matched control cannot remain a distinct normalized member of the same class while preserving that entire retained structure.

But this does **not** advance the Riemann hypothesis by itself. Hamburger rigidity identifies the distinguished function; it does not force its nontrivial zeros onto `Re(s)=1/2`. The functional equation makes the critical line the reflection axis, but off-axis symmetric zero pairs remain compatible with it. A route to RH still needs an additional sign, positivity, unitarity, localization, or other mechanism acting on the already-identified `zeta` divisor.

Nor does `(4)` establish that the functional equation is a minimal lift. A smaller statistic may be sufficient on a narrower source class, as AF-369 already demonstrates. AF-370 establishes a **sufficient and classical global recovery package**, not a category-independent lower bound on retained information.

## Prior-art and novelty audit

- Hans Hamburger, **“Über die Riemannsche Funktionalgleichung der ζ-Funktion. (Erste Mitteilung),”** *Mathematische Zeitschrift* **10** (1921), 240–254. EuDML: https://eudml.org/doc/167643. This is the original converse theorem characterizing the Riemann zeta function under Dirichlet-series and analytic-growth hypotheses.
- Jerzy Kaczorowski, Giuseppe Molteni and Alberto Perelli, **“A converse theorem for Dirichlet L-functions,”** *Commentarii Mathematici Helvetici* **85**(2) (2010), 463–483. DOI: `10.4171/CMH/202`. Its introduction states the Hamburger theorem in the paired form `(5)`–`(6)` and stresses that analogous uniqueness fails in general for Dirichlet `L`-functional equations.
- Alberto Perelli, **“Converse theorems: from the Riemann zeta function to the Selberg class,”** *Bollettino dell'Unione Matematica Italiana* (2017), arXiv:`1605.02354`. Role: modern survey placing Hamburger's theorem at the start of the converse-theorem hierarchy and separating the zeta rigidity phenomenon from later Hecke/Weil/Selberg-class settings.
- Takashi Nakamura, **“L-functions with Riemann's functional equation and the Riemann hypothesis,”** Jxiv preprint (2023), DOI: `10.51094/jxiv.238`. Role: explicit evidence that functions outside the Hamburger hypothesis package can satisfy the Riemann reflection law without being `zeta`, so the source-class assumptions are load-bearing rather than technical decoration.

No novelty is claimed for the converse theorem, its proof, or the existence of broader functional-equation families. The Arithmetic Fidelity contribution is the exact **resource accounting**: the functional equation becomes faithful only after it is paired with the correct source category, and normalization removes the final scalar gauge.

## Decisive audit rule

When a proposed compression claims that a zeta-like functional equation preserves rational-prime provenance, do not ask only whether the destination has an `s\leftrightarrow1-s` symmetry. Audit the full pair:

1. does the source remain an ordinary Dirichlet series on the integer frequency lattice with the continuation/growth hypotheses needed by the converse theorem; and
2. is the retained relation the exact completed Riemann functional equation with a normalization fixing the scalar ambiguity?

If both gates hold, Hamburger gives exact recovery of `zeta`. If either gate fails, the symmetry alone is not a faithful discriminator and matched non-zeta controls must remain admissible.
