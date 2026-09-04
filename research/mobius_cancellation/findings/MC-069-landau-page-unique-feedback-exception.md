# MC-069 — Landau–Page uniqueness collapses the positive-feedback quadratic family to at most one conductor below a quasi-subpower threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the positive signed-feedback architecture of `MC-066` and the family sparsity result `MC-068`. For an odd prime `q`, write

\[
\chi_q(n)=\left(\frac{n}{q}\right),
\qquad
f_q(n)=\mu(n)^2\chi_q(n),
\qquad
h_q=1*f_q,
\]

and, for `0<theta<1`,

\[
R_\theta(X;q)
:=
\sum_{2\le d\le X}\frac{h_q(d)}{d^\theta}.
\tag{1}
\]

For `Q>=2` let

\[
\mathcal B_\theta(X,Q)
:=
\{q\le Q:q\text{ odd prime and }R_\theta(X;q)<1\}.
\tag{2}
\]

There is an absolute constant `kappa>0` with the following property. For every fixed `eta>0`, uniformly for

\[
0<\theta\le1-\eta
\tag{3}
\]

and, for all sufficiently large `X`,

\[
2\le Q\le
\exp\!\left(\kappa\frac{\log X}{\log\log X}\right),
\tag{4}
\]

one has

\[
\boxed{\#\mathcal B_\theta(X,Q)\le1.}
\tag{5}
\]

More precisely, take the exceptional-character notion at level `D=ceil(Q)` from Ruzsa–Sanders. If no exceptional primitive character exists at that level, then

\[
\boxed{\mathcal B_\theta(X,Q)=\varnothing.}
\tag{6}
\]

If an exceptional primitive character `chi_D` of conductor `q_D<=D` does exist, then every member of `mathcal B_theta(X,Q)` must be induced by `chi_D`. Since each Legendre symbol `chi_q` here is primitive of prime conductor, this forces

\[
\mathcal B_\theta(X,Q)
\subseteq
\begin{cases}
\{q_D\},&q_D\text{ is an odd prime and }\chi_D=\chi_{q_D},\\
\varnothing,&\text{otherwise}.
\end{cases}
\tag{7}
\]

The same conclusion holds for the union over every exponent in `(3)`:

\[
\boxed{
\#\bigcup_{0<\theta\le1-\eta}\mathcal B_\theta(X,Q)\le1.
}
\tag{8}
\]

Thus `MC-068`'s `O_eta(log X)` family bound can be sharpened to a **single possible conductor** throughout the explicit quasi-subpower range `(4)`. Combined with `MC-067`, the positive triangle-feedback branch has the following sharper structure: sufficiently small stretched-exponential conductors are excluded even in the exceptional-zero case, while above that range and through `(4)` the only possible survivor is the unique Landau–Page exceptional primitive character at the relevant level.

No such exceptional character is proved to exist, and no improved estimate for `M(X)` follows.

## 1. Small feedback forces a linear negative terminal-prime twist

The first step is the exact terminal-prime argument already isolated in `MC-068`, repeated here because it is the bridge to the exceptional-character theorem.

For all sufficiently large `X`, the upper bound in `(4)` is below `X/2`. Hence the conductor prime `q` does not lie in `(X/2,X]`. Define

\[
\mathcal P_+(X;q)
:=
\{p:X/2<p\le X,\ \chi_q(p)=+1\}.
\tag{9}
\]

By `MC-066`, every split prime has

\[
h_q(p)=2.
\]

Since the full feedback kernel is nonnegative,

\[
R_\theta(X;q)
\ge
2\sum_{p\in\mathcal P_+(X;q)}p^{-\theta}
\ge
2X^{-\theta}\#\mathcal P_+(X;q).
\tag{10}
\]

Therefore `q in mathcal B_theta(X,Q)` implies

\[
\#\mathcal P_+(X;q)<\frac12X^\theta
\le\frac12X^{1-\eta}.
\tag{11}
\]

Put

\[
W(X)=\sum_{X/2<p\le X}\log p,
\qquad
T_q(X)=\sum_{X/2<p\le X}\chi_q(p)\log p,
\tag{12}
\]

and

\[
W_+(X;q)=\sum_{p\in\mathcal P_+(X;q)}\log p.
\]

Because every terminal prime has character value `+1` or `-1`, exactly

\[
T_q(X)=2W_+(X;q)-W(X).
\tag{13}
\]

Equation `(11)` gives, uniformly in `(3)`,

\[
W_+(X;q)
\le\frac12X^{1-\eta}\log X=o(X).
\tag{14}
\]

The ordinary prime number theorem gives

\[
W(X)=\frac X2+o(X).
\tag{15}
\]

Consequently, for all sufficiently large `X`, every feedback-capable conductor satisfies the fixed linear bias

\[
\boxed{T_q(X)\le-\frac X4.}
\tag{16}
\]

As in `MC-068`, the constant `1/4` is arbitrary. What matters is that positive-feedback contraction requires a character whose terminal-prime correlation is of order `X`, uniformly away from `theta=1`.

## 2. Ruzsa–Sanders give one exceptional primitive character and uniform cancellation for all the others

Ruzsa and Sanders, *Difference sets and the primes*, Acta Arithmetica 131 (2008), 281–301, DOI `10.4064/aa131-3-5`, arXiv `0710.0644`, collect the classical Landau exceptional-character machinery in exactly the uniform form needed here.

Their Corollary 4.3 states that, at every level `D>=2`, there is **at most one** primitive Dirichlet character `chi_D`, of conductor at most `D`, possessing a zero in their exceptional region. Their Theorem 4.5 states that there is an absolute `c_3>0` such that every nonprincipal character `chi` modulo `q<=D` which is not induced by that exceptional character satisfies

\[
\psi(x,\chi)
\ll
x\exp\!\left(
-\frac{c_3\log x}{\sqrt{\log x}+\log D}
\right)(\log D)^2
\tag{17}
\]

for every real `x>=1`. Only a character induced by `chi_D` receives the exceptional main term `-x^{beta_D}/beta_D`.

This is classical prime-number-theorem technology, not a new character theorem. Its usefulness here is that the modulus level `D` is allowed to grow with `X`, while all nonexceptional primitive characters are controlled simultaneously.

## 3. The Ruzsa–Sanders error is `o(X)` up to `exp(kappa log X / log log X)`

Let

\[
L=\log X
\]

and take `D=ceil(Q)`. Choose an absolute `kappa>0` sufficiently small relative to the constant `c_3` in `(17)`. Under `(4)`,

\[
\log D
\le
\kappa\frac{L}{\log L}+O(1).
\tag{18}
\]

For sufficiently large `L`, the `sqrt(L)` term is smaller than the right side of `(18)`, so at `x=X` the denominator in `(17)` is at most

\[
2\kappa\frac{L}{\log L}
\]

up to an inessential enlargement of the constant. At `x=X/2` the same conclusion holds with another fixed factor. Hence, after reducing `kappa` once more if necessary,

\[
\exp\!\left(
-\frac{c_3\log x}{\sqrt{\log x}+\log D}
\right)(\log D)^2=o(1)
\tag{19}
\]

uniformly for `x in {X/2,X}`.

For example, once the denominator is bounded by `3 kappa L/log L`, the right side of `(19)` is at most a constant times

\[
L^{\,2-c_3/(3\kappa)},
\]

apart from powers of `log L`; choosing `kappa<c_3/9` gives a strict negative power of `L`. No optimization is intended.

Therefore every nonexceptional `chi_q` with `q<=Q` satisfies

\[
\psi(X,\chi_q)=o(X),
\qquad
\psi(X/2,\chi_q)=o(X)
\tag{20}
\]

uniformly in the range `(4)`.

Removing prime powers costs only

\[
O(\sqrt X\,\log^2X)=o(X),
\]

so `(20)` implies

\[
T_q(X)
=
\vartheta(X,\chi_q)-\vartheta(X/2,\chi_q)
=o(X).
\tag{21}
\]

Equation `(21)` contradicts the necessary feedback bias `(16)`. Thus **no nonexceptional primitive quadratic character can belong to `mathcal B_theta(X,Q)`** in the range `(4)`.

## 4. Primitivity turns the exceptional branch into a singleton

Suppose `q in mathcal B_theta(X,Q)`. By the preceding section, `chi_q` must be induced by the unique exceptional primitive character `chi_D`, if that character exists.

But `chi_q` is itself primitive modulo the odd prime `q`. The primitive character inducing a Dirichlet character is unique. Therefore

\[
\chi_q=\chi_D,
\qquad
q=q_D.
\tag{22}
\]

There can consequently be at most one prime conductor in the bad family, proving `(5)`--`(7)`.

Finally, `h_q(d)>=0` gives monotonicity in the exponent:

\[
\theta_1\le\theta_2
\quad\Longrightarrow\quad
R_{\theta_2}(X;q)\le R_{\theta_1}(X;q).
\tag{23}
\]

If `R_theta(X;q)<1` for any `theta<=1-eta`, then

\[
R_{1-\eta}(X;q)<1.
\]

Thus the union in `(8)` is contained in `mathcal B_{1-eta}(X,Q)`, and the same singleton bound applies simultaneously to all fixed-gap exponents.

## 5. Prior art and novelty boundary

All analytic input is classical. Landau's uniqueness of an exceptional primitive character, the exceptional-zero prime number theorem, and the uniform nonexceptional bound `(17)` are standard results; Ruzsa–Sanders package them as Corollary 4.3 and Theorem 4.5 in a growing-level form. Their paper cites Davenport's *Multiplicative Number Theory* for those ingredients. A modern open-access restatement with the same exceptional/nonexceptional dichotomy appears in Mengdi Wang, *A quantitative bound on Furstenberg–Sárközy patterns with shifted prime power common differences in primes*, Mathematische Annalen 391 (2025), Appendix A, Theorems A.1–A.2, DOI `10.1007/s00208-024-03015-3`.

No standalone novelty is claimed for `(17)`, exceptional-character uniqueness, or the deduction that nonexceptional characters cannot have a linear-size terminal prime twist in the stated uniformity range.

The durable line-specific contribution is the exact coupling to the feedback carrier of `MC-066`. `MC-068` used the multiplicative large sieve and allowed `O(log X)` extreme prime quadratic characters below square-root conductor scale. The present argument uses the stronger pointwise information available below the quasi-subpower threshold `(4)` and identifies the entire possible exceptional family there with the **single** Landau–Page exceptional primitive character.

A targeted audit of the closest exceptional-character PNT literature therefore classifies the mechanism as established mathematics specialized to the Mathia feedback condition, not as a new theorem about Dirichlet characters.

## 6. Boundaries and falsification tests

The statement is deliberately narrower than a general elimination of moving quadratic comparators.

- It applies only to the **positive-kernel triangle closure** `R_theta(X;q)<1` from `MC-066`. A proof that retains the signs of the terms `h_q(d)M(X/d)` rather than bounding them through `R_theta` lies outside this obstruction.
- The fixed gap `theta<=1-eta` is load-bearing. It converts `R_theta<1` into the linear terminal bias `(16)`. The proof does not address exponents approaching `1` so rapidly that `X^theta log X` is no longer `o(X)`.
- The conductor range `(4)` is also load-bearing. The direct Ruzsa–Sanders error contains `(log D)^2`; the argument only claims a sufficiently small absolute constant `kappa` for which the nonexceptional error is `o(X)`. It does **not** cover every abstract `Q=X^{o(1)}`.
- The result does not eliminate the one exceptional primitive character. Indeed an exceptional zero creates a negative prime-character bias, exactly the direction that can help suppress the positive split-prime feedback. `MC-067` separately eliminates that exceptional loophole only in the smaller fixed stretched-exponential range where the classical lower bound on `1-beta` still dominates the prime-number-theorem error.
- If the unique level-`D` exceptional conductor is composite, or its primitive real character is not one of the prime-conductor Legendre symbols in this family, then the set in `(2)` is empty. The theorem does not assert that the exceptional conductor is prime.
- No zero-density hypothesis, GRH, random-character model, or Riemann-zeta zero-free region is used. The zero information is solely the classical Dirichlet-`L` exceptional-character dichotomy.
- No estimate for `M(X)` follows from `(5)`. The theorem constrains only which quadratic comparators can satisfy the sufficient triangle-feedback architecture.

The argument would fail if `R_theta<1` did not force the terminal bias `(16)`, if the Ruzsa–Sanders bound were not uniform over all nonexceptional characters up to level `D`, if its error were not `o(X)` in `(4)`, or if a primitive `chi_q` could be induced by a distinct primitive exceptional character. Each of these points is explicit and independently auditable.

## Consequence for the active frontier

The surviving positive quadratic-feedback corridor is now stratified more sharply than after `MC-068`.

For sufficiently large `X`, `MC-067` rules out every prime quadratic conductor up to

\[
\exp\!\bigl(b\sqrt{\log X}\bigr).
\]

From there through

\[
\exp\!\left(\kappa\frac{\log X}{\log\log X}\right),
\]

the present finding says that **at most one** conductor can satisfy the necessary contraction condition, and that conductor must be the unique exceptional primitive character at the chosen level. Beyond this direct pointwise range, `MC-068` still supplies the coarser family-energy bound `O(log X)` for every conductor cap below `X^(1/2)`.

Therefore continuing this exact positive-feedback architecture requires confronting a much more specific object than an arbitrary sparse family of prime quadratic characters: either the possible moving Landau–Siegel exceptional character itself, or a conductor range beyond the present uniform pointwise theorem. The alternative is to abandon the positive triangle inequality and prove genuine signed cancellation in the feedback sum. Merely searching a broad family of ordinary nonexceptional quadratic comparators below `(4)` is now ruled out.