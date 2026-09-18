# PL-359 — The conductor-one Riemann functional equation is incompatible with nonzero native `H^2`

**Evidence:** `CLASSICAL-CONVERSE-THEOREM+EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-358`.

`PL-357`--`PL-358` leave a sharp gap inside the standard Hardy space of Dirichlet series `\mathscr H^2`: complete multiplicativity is too rigid and gives zero-free reproducing kernels, while ordinary multiplicativity is too local and permits a critical-strip zero to be planted in one prime-power factor. A canonical way to couple all primes and degrees globally is to impose the completed Riemann functional equation itself.

Under the standard converse-theorem regularity needed to make that statement an `L`-function condition, this does not produce an intermediate family. It annihilates the native `\mathscr H^2` family.

Let

\[
h(s)=\sum_{n\ge1}a_n n^{-s},
\qquad
g(s)=\sum_{n\ge1}b_n n^{-s},
\tag{1}
\]

with `h,g in \mathscr H^2`, and suppose their meromorphic continuations satisfy

\[
(s-1)h(s),\ (s-1)g(s)
\quad\text{entire of finite order},
\tag{2}
\]

and the exact conductor-one Riemann functional equation

\[
\pi^{-s/2}\Gamma(s/2)h(s)
=
\pi^{-(1-s)/2}\Gamma((1-s)/2)g(1-s).
\tag{3}
\]

Then

\[
\boxed{h=g=0.}
\tag{4}
\]

In particular, a self-dual nonzero vector in the native Bohr/Dirichlet `\mathscr H^2` space cannot satisfy the genuine Riemann functional equation together with the usual Hamburger finite-order regularity. The obstruction is not RH and not a zero-location argument: the standard `H^2` completion has already excluded the unique nonzero conductor-one solution selected by the functional equation.

## 1. `\mathscr H^2` automatically satisfies Hamburger's convergence hypothesis

For `h in \mathscr H^2`,

\[
\sum_{n\ge1}|a_n|^2<\infty.
\tag{5}
\]

Hence for every `\sigma>1/2`, Cauchy--Schwarz gives

\[
\sum_{n\ge1}|a_n|n^{-\sigma}
\le
\left(\sum_n|a_n|^2\right)^{1/2}
\zeta(2\sigma)^{1/2}
<\infty.
\tag{6}
\]

The same holds for `g`. Thus both Dirichlet series are absolutely convergent, and therefore holomorphic, throughout `Re(s)>1/2`. In particular they satisfy the weaker absolute-convergence hypothesis `Re(s)>1` in Hamburger's converse theorem.

No analytic continuation of a formal Euler product is used here. Equation (6) is a native Hilbert-space estimate.

## 2. Hamburger uniqueness leaves only zeta

Hamburger's converse theorem, in the standard formulation recorded for example as Theorem 2.4 of Gelbart--Miller, states that if two ordinary Dirichlet series are absolutely convergent for `Re(s)>1`, `(s-1)h(s)` and `(s-1)g(s)` are entire of finite order, and (3) holds, then

\[
\boxed{h(s)=g(s)=a_1\zeta(s).}
\tag{7}
\]

The conclusion is classical prior art. What matters for the present line is its interaction with the native `\mathscr H^2` topology.

There are two independent ways to see that (7) forces `a_1=0` here.

First, (6) makes `h` holomorphic at `s=1`, whereas `a_1\zeta(s)` has a simple pole there unless `a_1=0`.

Second, uniqueness of ordinary Dirichlet coefficients in `Re(s)>1` gives

\[
a_n=a_1\qquad(n\ge1),
\tag{8}
\]

so the `\mathscr H^2` norm would be

\[
\sum_{n\ge1}|a_n|^2
=
\sum_{n\ge1}|a_1|^2,
\tag{9}
\]

which is finite only for `a_1=0`. Therefore (4) follows.

The same argument actually needs only one side of Hamburger's pair to lie in native `\mathscr H^2`; once the converse theorem identifies both sides with `c\zeta`, holomorphy at `1` or square summability forces `c=0`.

## 3. The failure is a topology/completion mismatch, not a critical-line mechanism

The nonzero solution selected by the conductor-one functional equation is precisely the coefficient vector

\[
(1,1,1,\ldots),
\tag{10}
\]

up to scale. That vector is not in `\ell^2(\mathbb N)`, and its Dirichlet series has the pole at `s=1` that native `\mathscr H^2` point evaluation forbids.

Thus adding the exact functional equation to the standard Bohr `H^2` completion does not interpolate between the two endpoints of `PL-357` and `PL-358`. It overshoots them: under ordinary `L`-function regularity the admissible family becomes `{0}`.

The familiar shifted example makes the same mismatch visible from another angle. For `\delta>1/2`,

\[
\zeta(s+\delta)=\sum_{n\ge1}n^{-\delta}n^{-s}
\in\mathscr H^2,
\tag{11}
\]

but its completed functional equation is

\[
\Lambda(s+\delta)=\Lambda(1-s-\delta),
\tag{12}
\]

whose reflection center in the `s` variable is `Re(s)=1/2-\delta`, not the Riemann critical line `Re(s)=1/2`. Moving zeta into `\mathscr H^2` by a square-summable weight simultaneously moves the functional-equation geometry away from the target line.

This is consistent with `PL-001`, `PL-021`, and `PL-357`: the standard coefficient Hilbert space naturally sees the half-plane beyond `1/2`, but the actual unshifted zeta coefficient vector sits on the wrong side of its norm boundary.

## 4. Prior-art and novelty audit

The theorem-level input is classical. Hamburger proved the converse theorem in 1921. Gelbart--Miller give the modern two-Dirichlet-series formulation used above: absolute convergence for `Re(s)>1`, finite order of `(s-1)h` and `(s-1)g`, plus (3), imply that both functions are the same constant multiple of `\zeta`. Kaczorowski--Molteni--Perelli restate the same theorem as the classical starting point for modern converse theorems.

A targeted literature audit on 18 September 2026 searched Hamburger's theorem together with Hardy spaces of Dirichlet series, square-summable coefficients, functional equations, and converse theorems. It recovered the classical converse-theorem literature and modern examples showing that altered conductor/frequency hypotheses can support other functions with Riemann-type functional equations, but no basis for claiming the elementary `\mathscr H^2` corollary (4) as a new theorem. **No theorem-level novelty is claimed.** The durable content is the exact route restriction after `PL-357`--`PL-358`: the most canonical global functional-equation repair is incompatible with the native completed source space.

Modern constructions are an important adversarial control against overstatement. Nakamura constructs functions with periodic coefficients or modified conductor normalizations satisfying Riemann-type functional equations and with non-zeta zero sets. They do not contradict (4): changing the conductor/frequency normalization or the exact ordinary-Dirichlet-series hypotheses leaves Hamburger's conductor-one uniqueness class. The slogan “the functional equation alone determines zeta” is therefore false without the precise analytic and Dirichlet-series hypotheses used above.

### Sources

1. H. Hamburger, “Über die Riemannsche Funktionalgleichung der Zeta-Funktion (Erste Mitteilung),” *Mathematische Zeitschrift* **10** (1921), 240--254. EuDML: https://eudml.org/doc/167643.
2. Stephen S. Gelbart, Stephen D. Miller, “Riemann's zeta function and beyond,” *Bulletin of the American Mathematical Society* **41**(1) (2004), 59--112, Theorem 2.4. DOI: https://doi.org/10.1090/S0273-0979-03-00995-9.
3. J. Kaczorowski, G. Molteni, A. Perelli, “A converse theorem for Dirichlet L-functions,” *Commentarii Mathematici Helvetici* **85**(2) (2010), 463--483. DOI: https://doi.org/10.4171/CMH/202.
4. Takashi Nakamura, “Dirichlet Series with Periodic Coefficients, Riemann's Functional Equation, and Real Zeros of Dirichlet L-Functions,” *Mathematica Slovaca* **73**(5) (2023), 1145--1152. DOI: https://doi.org/10.1515/ms-2023-0084. Used only as a boundary control on altered hypotheses.

## 5. Adversarial boundaries

1. **Finite-order/converse-theorem regularity is load-bearing.** Equation (3) as a bare meromorphic symmetry is not enough for Hamburger uniqueness. Dropping the growth/regularity hypotheses reopens a much larger solution space and supplies no automatic RH rigidity.

2. **The exact conductor-one gamma factor and ordinary integer Dirichlet spectrum are load-bearing.** Dirichlet `L`-functions, periodic-coefficient constructions, conductor changes, generalized Dirichlet series, and automorphic `L`-functions obey different converse-theorem classifications. They are not ruled out by (4).

3. **The result is about the native unweighted `\mathscr H^2` completion.** A weighted space large enough to contain `(1,1,...)`, a distributional completion, or a target-relative Nyman/Weil topology can behave differently.

4. **A dual partner outside `\mathscr H^2` is not classified by the two-sided formulation stated in (1)--(4).** The stronger observation after (9) applies if the other partner still satisfies Hamburger's ordinary Dirichlet-series and regularity assumptions, but no claim is made for arbitrary dual objects.

5. **No statement about RH follows.** The argument never studies nontrivial zeros. It proves that this proposed source-selection law destroys the candidate family before zero localization becomes a question.

## Research consequence

The live intermediate-family problem can now exclude another canonical endpoint. Within native `\mathscr H^2`, imposing ordinary multiplicativity is too weak, imposing complete multiplicativity is too local-kernel rigid, and imposing the exact conductor-one Riemann functional equation with standard converse-theorem regularity is stronger still: it leaves only zero.

A viable global coupling therefore cannot simply append the unmodified Riemann functional equation to an `\ell^2` coefficient family. It must change at least one load-bearing ingredient in a mathematically controlled way: the completion topology, the source/dual pairing, the conductor/gamma data, or the target-relative structure. Any such escape must then prove that its added freedom is not merely the well-known flexibility of generalized converse-theorem classes, and that it still supplies a destination theorem strong enough to constrain the Riemann zero divisor.