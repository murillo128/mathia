# MC-082 — Liouville parity classes have the same divisor-density main terms; the discarded remainder is exactly the parity carrier

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
\lambda(n)=(-1)^{\Omega(n)},
\qquad
L(x)=\sum_{n\le x}\lambda(n),
\]

and split the positive integers into their two Liouville-parity classes

\[
w_+(n)=\frac{1+\lambda(n)}2,
\qquad
w_-(n)=\frac{1-\lambda(n)}2.
\tag{1}
\]

Thus `w_+` is the indicator of integers with an even number of prime factors counted with multiplicity, while `w_-` is the odd-parity indicator. For an integer `X>=2`, write

\[
A_\pm(X)=\sum_{n\le X}w_\pm(n)
\]

and, for `d>=1`,

\[
A_\pm(X;d)=\sum_{\substack{n\le X\\d\mid n}}w_\pm(n).
\]

Complete multiplicativity of `lambda` gives the exact identities

\[
\boxed{
A_\pm(X)=\frac{X\pm L(X)}2
}
\tag{2}
\]

and

\[
\boxed{
A_\pm(X;d)
=
\frac12\left\lfloor\frac Xd\right\rfloor
\pm
\frac{\lambda(d)}2
L\!\left(\left\lfloor\frac Xd\right\rfloor\right).
}
\tag{3}
\]

If the sieve main density is normalized as

\[
g(d)=\frac1d,
\]

then the exact remainder after using the actual total mass `A_\pm(X)` is

\[
\boxed{
\begin{aligned}
r_d^\pm(X)
&:=A_\pm(X;d)-\frac{A_\pm(X)}d\\
&=
\frac12\left(\left\lfloor\frac Xd\right\rfloor-\frac Xd\right)
\pm\frac12\left(
\lambda(d)L\!\left(\left\lfloor\frac Xd\right\rfloor\right)
-
\frac{L(X)}d
\right).
\end{aligned}}
\tag{4}
\]

Thus the two parity classes have **the same divisor-density main term** `g(d)=1/d`; their entire distinction at the Type-I/local-divisibility level is carried by signed Liouville remainders.

The classical unconditional Korobov–Vinogradov-shaped bound for `L` retained in `MC-S8` makes this indistinguishability uniform to every fixed polynomial depth. Define

\[
V(X)=(\log X)^{3/5}(\log\log X)^{-1/5}.
\]

For every fixed `delta in (0,1)` there is `c_delta>0` such that, uniformly for

\[
1\le d\le X^{1-\delta},
\]

one has

\[
\boxed{
r_d^\pm(X)
\ll_\delta
1+rac Xd\exp(-c_\delta V(X)).
}
\tag{5}
\]

In particular, throughout that polynomial range both sequences satisfy the same local density law with a relative error tending to zero faster than every fixed power of `1/log X`.

Yet their prime content is maximally different. For every prime `p`,

\[
\lambda(p)=-1,
\qquad
w_+(p)=0,
\qquad
w_-(p)=1.
\tag{6}
\]

So one parity class contains no primes at all, while the other contains every prime, despite the two classes having essentially identical divisor-density main terms and very small local remainders through polynomial level. This is precisely the information-loss mechanism behind the classical **parity phenomenon of sieve theory** (`MC-S39`).

For the Möbius line, the consequence is not that all sieve methods are useless. It is narrower: **a route that retains only Type-I/local divisor densities and then forgets the signed parity remainders has discarded the very observable that distinguishes even from odd prime-factor parity.** On square-free integers `mu=lambda`, and `MC-003` shows that the exact square-divisor bridge between Liouville and Möbius has its black-box transfer threshold at exponent `1/2`. Thus replacing the missing parity carrier by an RH-scale bound for `L` would merely reinsert an RH-equivalent input rather than explain Möbius cancellation.

A surviving sieve-like route must therefore add information not contained in `(g(d),|r_d|)` alone—for example genuinely bilinear/Type-II, spectral, or other parity-sensitive structure that keeps signed relations between factors. The classical Friedlander–Iwaniec parity-sensitive sieve (`MC-S40`) is an important boundary: it shows that parity can be broken in special arithmetic sequences once additional harmonic information is supplied. The obstruction here is to **local-density-only inference**, not to every method containing a sieve step.

No improved estimate for `M(X)` or `L(X)` is claimed.

## 1. Exact divisor-density decomposition

From `(1)`,

\[
A_\pm(X;d)
=
\frac12\sum_{m\le X/d}1
\pm
\frac12\sum_{m\le X/d}\lambda(dm).
\]

Since Liouville is completely multiplicative,

\[
\lambda(dm)=\lambda(d)\lambda(m),
\]

and therefore

\[
\sum_{m\le X/d}\lambda(dm)
=
\lambda(d)L\!\left(\left\lfloor\frac Xd\right\rfloor\right).
\]

This proves `(3)`. Taking `d=1` gives `(2)`. Subtracting `A_\pm(X)/d` gives `(4)` exactly.

A particularly transparent equivalent identity is

\[
\boxed{
A_+(X;d)-A_-(X;d)
=
\lambda(d)L\!\left(\left\lfloor\frac Xd\right\rfloor\right).
}
\tag{7}
\]

The parity signal is therefore not a vague statistical defect hidden somewhere in the sieve data: it is exactly a rescaled Liouville summatory value at every divisor scale.

## 2. Uniform polynomial-depth indistinguishability

`MC-S8` records the unconditional estimate

\[
L(y)
\ll
 y\exp\!\left(-c(\log y)^{3/5}(\log\log y)^{-1/5}\right)
\tag{8}
\]

for sufficiently large `y` and some absolute `c>0`.

Fix `delta in (0,1)` and suppose `d<=X^{1-delta}`. Then

\[
y=\left\lfloor\frac Xd\right\rfloor
\ge \tfrac12 X^\delta
\]

for all sufficiently large `X`. Hence

\[
(\log y)^{3/5}(\log\log y)^{-1/5}
\ge c'_\delta V(X)
\]

for a positive constant `c'_delta`. Applying `(8)` at `y` and at `X`, and using the floor error in `(4)`, gives

\[
|r_d^\pm(X)|
\ll
1+rac Xd e^{-c_\delta V(X)},
\]

which is `(5)`.

This is much stronger than merely saying `A_\pm(X;d)~X/(2d)` for each fixed `d`. The same first-order divisor-density model remains valid uniformly while `d` ranges across any fixed polynomial sublevel. Nevertheless `(6)` shows that this local model cannot determine even the most basic parity-sensitive endpoint: whether the sequence contains primes.

The result should not be overread as a new theorem about the optimal level of distribution of a sieve. It is an explicit control pair showing that **very accurate one-divisor marginals can coexist with opposite prime-factor parity content**.

## 3. Möbius inherits the same parity carrier only after square-free projection

Liouville never vanishes, while Möbius is supported only on square-free integers, so the two sequences must not be identified globally. The relevant exact bridge was already audited in `MC-003`:

\[
\lambda(n)=\sum_{d^2\mid n}\mu\!\left(\frac{n}{d^2}\right),
\qquad
\mu(n)=\sum_{d^2\mid n}\mu(d)\lambda\!\left(\frac{n}{d^2}\right).
\tag{9}
\]

Consequently their summatory functions transfer through the square kernel with threshold `1/2`. For every `alpha>1/2`, an `O(x^alpha)` bound for one transfers by absolute summation to the other with the same exponent; at `alpha=1/2` the same black-box argument incurs a logarithm.

This supplies the exact dictionary needed for the present sieve control. On the square-free sector, where `mu(n)=lambda(n)`, Möbius sign is literally prime-factor parity. Passing from the all-integer Liouville witness to Möbius requires the square-free projection, and `MC-003` already proves that this projection does not create a cheaper route through the critical exponent.

In particular, equation `(7)` should not be advertised as a new Mertens formula. Its role is diagnostic: a local-divisibility representation that replaces the signed remainder by a magnitude bound or omits it entirely loses an arithmetic channel whose critical-scale control is already known to be zero-sensitive.

## 4. Prior art and novelty boundary

The parity obstruction itself is classical sieve theory. Friedlander and Iwaniec's expository note *What is ... the parity phenomenon?* (`MC-S39`) is a direct literature anchor for the fact that ordinary sieve information can fail to distinguish integers according to parity of the number of prime factors. The use of Liouville signs `(-1)^Omega` as the parity witness is standard; no novelty is claimed for that idea.

The formulas `(2)`--`(4)` are elementary consequences of complete multiplicativity, and the quantitative estimate `(5)` is an immediate specialization of the classical Liouville bound already retained in `MC-S8`. A targeted prior-art audit therefore gives no basis for a new analytic-number-theory theorem claim.

The useful Mathia contribution is the **exact information-budget dictionary for this research line**: the common local sieve density is `1/d`, while the data it forgets is explicitly `lambda(d)L(X/d)`. Combined with `MC-003`, this identifies the standard sieve parity barrier with the same square-root-sensitive cancellation carrier that the Möbius program is trying to control.

The boundary is equally important. Friedlander and Iwaniec's 1997 parity-sensitive sieve (`MC-S40`) proves that the parity barrier is not an absolute impossibility theorem. Their prime-producing application uses additional harmonic structure beyond generic local sieve marginals. Accordingly, the present finding does not justify rejecting Type-II/bilinear or parity-sensitive routes merely because they also use sieve language.

## 5. Boundaries and falsification tests

- The control sequences `w_+` and `w_-` live on **all positive integers**. They are not square-free-supported Möbius comparators. Their relevance to Möbius is through the exact square-divisor bridge in `MC-003`, not through equality of the full sequences.
- Equation `(5)` is stated only for every fixed polynomial level `d<=X^(1-delta)`. It does not claim a useful uniform estimate when `X/d` is bounded or subpolynomial.
- The Korobov–Vinogradov saving in `(5)` is subpower. It supplies strong local indistinguishability but not an RH-scale power estimate.
- The obstruction applies when a method retains local density data while losing the **signed** parity remainder. A method that controls the signed family in `(7)`, or a bilinear relation among such terms, is using strictly more information and is not ruled out.
- No conclusion is drawn about the full power of modern sieve methods. `MC-S40` is an explicit counterexample to any blanket claim that parity can never be broken.
- A bound on `L(X)` of size `O_epsilon(X^(1/2+epsilon))` is not an independently cheap repair: `MC-S8` records its equivalence to RH, and `MC-003` transfers that critical-scale information to Möbius.

The exact claim is falsified if `(3)` fails for some `X,d`, if subtracting the total-mass normalization does not give `(4)`, or if the unconditional Liouville estimate does not imply the uniform bound `(5)` on every fixed polynomial sublevel. The sieve interpretation is falsified as a claimed no-go if it is extended to a method that demonstrably retains additional parity-sensitive information; that extension is explicitly excluded.

## Consequence for the active frontier

The line already knows from `MC-001` that strong almost-all local cancellation does not aggregate to a global Mertens bound when signs and exceptional structure are discarded. The present finding isolates a complementary classical obstruction on the **multiplicative-divisibility axis**: even extremely accurate divisor marginals can be blind to prime-factor parity.

This gives a concrete filter for future Type-I/Type-II or sieve-flavored proposals. If the proposed input can be evaluated on `w_+` and `w_-` and sees only their common density `1/d` plus unsigned small errors, it has not yet retained the Möbius parity carrier. A viable continuation must identify the first genuinely parity-sensitive statistic—typically a signed bilinear or higher-order relation—show that it distinguishes the control pair, and then prove that its available arithmetic bound is independently weaker than the Mertens target.

That requirement narrows the search without closing it: local-density refinements alone are classical parity-blind information, while extra parity-sensitive coupling remains a legitimate research frontier.