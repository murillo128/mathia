# MC-070 — Siegel lower bounds push positive squarefree-character feedback beyond the square-root conductor horizon

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the signed square-free quadratic feedback architecture of `MC-066`. Let `q` be an odd prime,

\[
\chi(n)=\left(\frac{n}{q}\right),
\qquad
f_\chi(n)=\mu(n)^2\chi(n),
\qquad
h_\chi=1*f_\chi,
\]

and for `0<theta<1` define

\[
R_\theta(X;\chi)
:=
\sum_{2\le d\le X}\frac{h_\chi(d)}{d^\theta}.
\tag{1}
\]

Recall that `h_chi(n)>=0` and

\[
h_\chi(p^a)=1+\chi(p)
\quad(p\ne q),
\qquad
h_\chi(q^a)=1.
\tag{2}
\]

The positive-feedback obstruction is substantially stronger than `MC-067`--`MC-069` show pointwise from primes in progressions.

**For every fixed `eta>0` and every fixed `A<2`, uniformly for**

\[
q\le X^A,
\qquad
0<\theta\le1-\eta,
\tag{3}
\]

**one has, for all sufficiently large `X`,**

\[
\boxed{R_\theta(X;\chi)>1.}
\tag{4}
\]

The threshold in `(4)` is ineffective because the proof uses Siegel's lower bound for `L(1,chi)`. More quantitatively, the exact feedback coefficients satisfy

\[
\boxed{
\sum_{n\le X}h_\chi(n)
=
\frac{L(1,\chi)}{\zeta(2)(1-q^{-2})}X
+
O\!\left(
X^{1/2}q^{1/4}(\log(2q))^{1/2}\log(2Xq)
\right).
}
\tag{5}
\]

Consequently, for every fixed `A<2` and `eta>0`, Siegel's theorem implies an ineffective `c=c(A,eta)>0` and sufficiently large threshold such that throughout `(3)`

\[
R_\theta(X;\chi)
\ge X^{-\theta}\left(\sum_{n\le X}h_\chi(n)-1\right)
\gg_{A,\eta}X^c.
\tag{6}
\]

Thus a sequence of prime quadratic characters satisfying the positive triangle-contraction condition

\[
R_\theta(X;\chi)<1
\tag{7}
\]

at a fixed gap from `theta=1` must obey, at power-exponent level,

\[
\boxed{q\ge X^{2-o(1)}.}
\tag{8}
\]

This closes the residual subpower exceptional-character corridor left by `MC-069`: the possible Landau--Page exceptional character is not a surviving positive-feedback comparator merely because pointwise prime-number-theorem control loses uniformity. Its positive convolution kernel has mean density proportional to `L(1,chi)`, and Siegel's lower bound prevents that density from becoming polynomially small enough on any range `q<=X^A` with fixed `A<2`.

Coupled to the Munsch/Burgess squarefree-character certificate used in `MC-064`--`MC-069`, this produces a new method-specific floor. Munsch gives, for prime `q`,

\[
|F_\chi(X)|
\ll
X^{1/2}q^{3/16}(\log X)(\log q)^{1/2}.
\tag{9}
\]

To certify `|F_chi(X)|<=X^{theta+o(1)}` from `(9)` requires

\[
q\le X^{\frac{16}{3}(\theta-1/2)+o(1)}.
\tag{10}
\]

Combining `(8)` and `(10)` shows that the package consisting of **Munsch's comparator estimate plus the positive-kernel triangle closure of `MC-066` cannot certify any fixed power exponent below**

\[
\boxed{\theta=\frac78.}
\tag{11}
\]

This is only a certification floor for that exact package. It is not a bound on `M(X)`, not a lower bound on the true squarefree-character sum, and not an obstruction to an argument that keeps cancellation among the signed terms `h_chi(d)M(X/d)`.

## 1. The feedback kernel is a square-Möbius transform of `1*chi`

Put

\[
g_\chi:=1*\chi.
\tag{12}
\]

For a real quadratic character, `g_chi(n)>=0`. Its local factors are

\[
g_\chi(p^a)=
\begin{cases}
a+1,&\chi(p)=+1,\\
1_{2\mid a},&\chi(p)=-1,\\
1,&p=q.
\end{cases}
\tag{13}
\]

The Dirichlet series of `h_chi` from `MC-066` is, in `Re(s)>1`,

\[
\sum_{n\ge1}\frac{h_\chi(n)}{n^s}
=
\frac{\zeta(s)L(s,\chi)}{L(2s,\chi^2)}.
\tag{14}
\]

Comparing local factors with

\[
\sum_{n\ge1}\frac{g_\chi(n)}{n^s}
=\zeta(s)L(s,\chi)
\tag{15}
\]

gives the exact coefficient identity

\[
\boxed{
g_\chi(n)
=
\sum_{\substack{m^2\mid n\\q\nmid m}}
h_\chi(n/m^2).
}
\tag{16}
\]

Indeed, away from `q` the quotient of the Euler factors in `(15)` and `(14)` is `(1-p^{-2s})^{-1}`, while the `q`-factor cancels. Möbius inversion on square divisors therefore gives

\[
\boxed{
h_\chi(n)
=
\sum_{\substack{m^2\mid n\\q\nmid m}}
\mu(m)g_\chi(n/m^2).
}
\tag{17}
\]

No analytic continuation is used in `(16)`--`(17)`; they are finite multiplicative identities.

## 2. Pólya--Vinogradov gives a uniform mean for `1*chi`

Let

\[
G_\chi(y):=\sum_{n\le y}g_\chi(n).
\tag{18}
\]

The classical Pólya--Vinogradov inequality gives

\[
\max_t\left|\sum_{n\le t}\chi(n)\right|
\ll \sqrt q\log(2q).
\tag{19}
\]

Write

\[
P:=C\sqrt q\log(2q)
\]

for a fixed absolute upper bound in `(19)`. If `y>=P`, choose

\[
B=(yP)^{1/2}.
\]

From

\[
G_\chi(y)=\sum_{b\le y}\chi(b)\left\lfloor\frac yb\right\rfloor,
\tag{20}
\]

split at `B`. On `b<=B`, replacing the floor by `y/b` costs `O(B)`. On `b>B`, either partial summation against the decreasing weight `floor(y/b)` or the identity

\[
\sum_{B<b\le y}\chi(b)\left\lfloor\frac yb\right\rfloor
=
\sum_{a\le y/B}\sum_{B<b\le y/a}\chi(b)
\]

shows that the tail is `O(Py/B)`. The same partial-summation bound gives

\[
L(1,\chi)-\sum_{b\le B}\frac{\chi(b)}b
=O(P/B).
\]

Hence

\[
\boxed{
G_\chi(y)=L(1,\chi)y+O\!\left(\sqrt{yP}\right)
\qquad(y\ge P).
}
\tag{21}
\]

For `y<P`, positivity and `g_chi(n)<=d(n)` give the elementary fallback

\[
G_\chi(y)\ll y\log(2y).
\tag{22}
\]

The exponent `q^{1/4}` that will appear below is therefore simply the square root of the Pólya--Vinogradov scale, not a new character-sum estimate.

## 3. Square inversion produces the feedback-density asymptotic

Summing `(17)` gives

\[
H_\chi(X)
:=\sum_{n\le X}h_\chi(n)
=
\sum_{\substack{m\le\sqrt X\\q\nmid m}}
\mu(m)G_\chi(X/m^2).
\tag{23}
\]

Take

\[
M=(X/P)^{1/2}.
\]

For `m<=M`, equation `(21)` yields

\[
G_\chi(X/m^2)
=
L(1,\chi)\frac{X}{m^2}
+O\!\left(\frac{\sqrt{XP}}m\right).
\tag{24}
\]

The main coefficient satisfies

\[
\sum_{\substack{m\ge1\\q\nmid m}}\frac{\mu(m)}{m^2}
=
\frac{1}{\zeta(2)(1-q^{-2})},
\tag{25}
\]

and truncating `(25)` at `M` costs `O(1/M)`. Summing the error in `(24)` costs

\[
O\!\left(\sqrt{XP}\log(2X)\right).
\tag{26}
\]

For `m>M`, use `(22)`. Since `X/m^2<P`,

\[
\sum_{m>M}G_\chi(X/m^2)
\ll
X\log(2P)\sum_{m>M}\frac1{m^2}
\ll
\sqrt{XP}\log(2P).
\tag{27}
\]

The truncated-main-term error contributes at most

\[
O\!\left(L(1,\chi)\sqrt{XP}\right),
\]

and the elementary bound `L(1,chi)<<log(2q)` absorbs it into the displayed logarithmic envelope. Since `P<<q^{1/2}log(2q)`, equations `(23)`--`(27)` prove `(5)` whenever `X/P` tends to infinity; this is automatic uniformly in the power range `q<=X^A`, `A<2`.

The leading constant in `(5)` is also the residue at `s=1` of `(14)`, because for prime `q`

\[
L(2,\chi^2)=\zeta(2)(1-q^{-2}).
\]

The finite derivation above is retained because it makes the modulus dependence and the `q<X^2` horizon explicit without a Tauberian black box.

## 4. Siegel's lower bound makes the positive mass unavoidable

For every fixed `epsilon>0`, Siegel's theorem gives, ineffectively but uniformly over primitive real characters,

\[
L(1,\chi)\gg_\varepsilon q^{-\varepsilon}.
\tag{28}
\]

Fix `A<2` and `eta>0`. Choose `epsilon>0` so small that

\[
A\varepsilon<\frac\eta2
\qquad\text{and}\qquad
A\varepsilon<\frac{2-A}{8},
\tag{29}
\]

with the second condition omitted when `A=0`.

For `q<=X^A`, `(28)` makes the main term in `(5)` at least a constant times

\[
X^{1-A\varepsilon},
\tag{30}
\]

whereas its error is at most

\[
X^{1/2+A/4+o(1)}.
\tag{31}
\]

The second inequality in `(29)` gives a fixed positive exponent gap between `(30)` and `(31)`. Thus, after an ineffective sufficiently-large threshold,

\[
H_\chi(X)\gg_{A,\eta}X^{1-A\varepsilon}.
\tag{32}
\]

Since `h_chi(n)>=0`, every `n<=X` has `n^{-theta}>=X^{-theta}`, so

\[
R_\theta(X;\chi)
\ge
X^{-\theta}(H_\chi(X)-1)
\gg
X^{1-\theta-A\varepsilon}.
\tag{33}
\]

For `theta<=1-eta`, the first condition in `(29)` makes the final exponent at least `eta/2`. This proves `(4)`--`(6)`.

The argument is deliberately ineffective. It proves that no fixed power range below `q=X^2` can contain infinitely many positive-feedback contractions at a fixed gap from `theta=1`, but it does not supply a computable cutoff at which a particular conductor is eliminated.

## 5. The Munsch plus positive-feedback package has a 7/8 power floor

Suppose the exact positive triangle architecture of `MC-066` is used to certify a fixed exponent `theta<1`, and the comparator term is controlled only by Munsch's bound `(9)`.

At power level, `(9)` can fit under `X^{theta+o(1)}` only if `(10)` holds. If

\[
\theta<\frac78,
\]

then

\[
\frac{16}{3}(\theta-1/2)<2.
\]

Choose a fixed `A` strictly between those two numbers. The Munsch conductor requirement then puts every admissible conductor below `X^A` for all sufficiently large `X`, while `(4)` says every such conductor has `R_theta>1`. Hence the sufficient triangle closure cannot close.

At the endpoint `theta=7/8`, logarithms and the strict `A<2` horizon prevent a literal endpoint theorem here. The correct durable statement is the power-exponent floor `(11)` for this certificate package.

This sharply revises the residual frontier from `MC-067`--`MC-069`. Those findings used terminal split primes and uniform prime-number-theorem technology to squeeze the positive-feedback family from below. The mean-density route sees a different obstruction: before the conductor reaches the natural Pólya--Vinogradov transition `q about X^2`, the entire nonnegative convolution kernel has too much total mass for a fixed-gap power-weighted contraction. The possible exceptional character does not evade this aggregate constraint.

## 6. Prior art and novelty boundary

Every analytic ingredient is classical. Pólya--Vinogradov, Siegel's lower bound for `L(1,chi)`, Dirichlet convolution, and the residue of `zeta(s)L(s,chi)/L(2s,chi^2)` are standard. `MC-S15` already anchors the classical Dirichlet-`L` exceptional-zero/Siegel machinery used by this line, and `MC-S38` anchors the squarefree-character comparator and the Pólya--Vinogradov/Burgess inputs.

A particularly close recent comparison is Mikko Jaskari and Stelios Sachpazis, *The Chowla conjecture and Landau--Siegel zeroes*, Mathematical Proceedings of the Cambridge Philosophical Society 179 (2025), 167--187, DOI `10.1017/S0305004125000271`, arXiv `2409.10663`. Their Lemma 3.1 quantitatively bounds

\[
\sum_{z<p\le x}\frac{1+\chi(p)}p
\]

when `chi` has a Landau--Siegel zero, and their proof strategy exploits the same classical positivity of `1*chi` to replace Liouville behavior by an exceptional quadratic character. This confirms that harmonic split-prime sparsity under an exceptional zero is established prior art. It does **not** supply the power-weighted contraction required by `(1)`: the present obstruction instead uses the total mean density of the squarefree feedback kernel and Siegel's lower bound to show that this stronger contraction cannot occur below the `q=X^{2-o(1)}` horizon.

A targeted search around squarefree-character sums, `1*chi`, exceptional-character Liouville approximations, and the Dirichlet series `(14)` found no basis for a standalone novelty claim. Formula `(5)` is an elementary modulus-uniform specialization of classical convolution/character-sum machinery, and `(11)` is retained only as the method-specific consequence for the exact Mathia feedback architecture.

## 7. Boundaries and falsification tests

- The conclusion applies only to the **positive-kernel triangle closure** of `MC-066`. It says nothing against a proof that retains signs and proves cancellation in `sum h_chi(d)M(X/d)`.
- The fixed gap `theta<=1-eta` is load-bearing. No uniform claim is made when `theta` approaches `1` with `X` so quickly that the power gain disappears.
- The conductor exponent `A<2` is load-bearing for this Pólya--Vinogradov proof. At the transition `q about X^2`, the error in `(5)` can be as large as the main term under the available lower bound. Better character-sum information may move this horizon.
- The sufficiently-large threshold is ineffective because `(28)` is ineffective. `MC-067`--`MC-069` retain value where effective or more explicit finite-level exceptional-character structure is required.
- The statement is written for prime `q`, matching `MC-066`. Primitive real quadratic composite conductors require the corresponding local factor `prod_{p|q}(1-p^{-2})` and bookkeeping at conductor primes; no such extension is claimed here.
- The `7/8` value is a floor for **certification by Munsch plus positive triangle feedback**, not for the true comparator sum and not for Möbius cancellation.
- The recent Landau--Siegel/Chowla literature does not contradict `(4)`: harmonic closeness of `chi(p)` to `-1` can coexist with a power-large number of feedback coefficients on sufficiently long prefixes.

The finding is falsified if `(16)`--`(17)` fail at a local Euler factor, if Pólya--Vinogradov does not imply `(21)`, if the square-inversion tail cannot be bounded as in `(27)`, or if Siegel's theorem does not provide `(28)` uniformly over primitive real characters. These are all standard finite or classical analytic steps and are independently checkable.

## Consequence for the active frontier

The positive quadratic-feedback branch no longer has a meaningful subpower exceptional-character corridor. `MC-069` reduced that corridor to at most the unique Landau--Page exceptional conductor in a quasi-subpower range; the aggregate feedback-density argument here eliminates **every** prime quadratic conductor below every fixed power `X^A`, `A<2`, after an ineffective threshold.

For the current Munsch/Burgess comparator certificate this is decisive: a conductor large enough even to have a chance of positive feedback is already so large that the displayed comparator theorem cannot certify an exponent below `7/8`. Therefore this exact positive-triangle signed escape from the `MC-065` absolute-transfer floor is worse, not better, at critical power scale.

The surviving signed question is now narrower: any useful quadratic-character feedback argument must exploit cancellation among the terms of the recurrence itself, or replace the comparator certificate/feedback carrier with information that does not become positive and dense at mean level. Searching for a special exceptional quadratic character while retaining `R_theta<1` as the closure condition is no longer a viable asymptotic route.