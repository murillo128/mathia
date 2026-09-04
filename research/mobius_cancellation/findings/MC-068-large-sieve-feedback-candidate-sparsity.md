# MC-068 — The multiplicative large sieve makes positive-feedback quadratic conductors logarithmically sparse below square-root scale

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the positive signed-feedback architecture of `MC-066` and the Page–Siegel obstruction of `MC-067`. For an odd prime `q`, let

\[
\chi_q(n)=\left(\frac{n}{q}\right),
\qquad
f_q(n)=\mu(n)^2\chi_q(n),
\qquad
h_q=1*f_q,
\]

and for `0<theta<1` put

\[
R_\theta(X;q)
:=
\sum_{2\le d\le X}\frac{h_q(d)}{d^\theta}.
\tag{1}
\]

Recall from `MC-066` that

\[
h_q(p^a)=1+\chi_q(p)
\qquad(a\ge1),
\tag{2}
\]

so every prime with `chi_q(p)=+1` contributes `2p^{-theta}` to `(1)`.

Fix `eta>0`. Uniformly for

\[
0<\theta\le1-\eta
\tag{3}
\]

and real parameters

\[
2\le Q\le X/2,
\tag{4}
\]

let

\[
\mathcal B_\theta(X,Q)
:=
\{q\le Q:\ q\text{ odd prime and }R_\theta(X;q)<1\}.
\tag{5}
\]

Then, for all sufficiently large `X` depending on `eta`,

\[
\boxed{
\#\mathcal B_\theta(X,Q)
\ll_\eta
\left(1+\frac{Q^2}{X}\right)\log X.
}
\tag{6}
\]

In particular, throughout the whole conductor range

\[
Q\le X^{1/2},
\tag{7}
\]

only

\[
\boxed{
\#\mathcal B_\theta(X,Q)\ll_\eta\log X
}
\tag{8}
\]

prime quadratic characters can even pass the **necessary positive-feedback test** `R_theta<1` at one scale.

The same bound applies to the union over all exponents `theta<=1-eta`: since `R_theta(X;q)` decreases as `theta` increases, existence of any such `theta` with `R_theta<1` implies

\[
R_{1-\eta}(X;q)<1.
\tag{9}
\]

This gives an unconditional family-level sharpening of the current residual corridor. `MC-067` excludes every prime quadratic conductor

\[
q\le \exp\!\bigl(b\sqrt{\log X}\bigr)
\]

from this positive triangle closure, while the Munsch/Burgess comparator certificate used in `MC-064`--`MC-067` requires `q=X^{o(1)}` in a near-critical implementation. Any such subpower cap is eventually below `X^{1/2}`, so `(8)` says that **at most logarithmically many** prime conductors under that cap can satisfy the remaining feedback condition at a given large scale.

This does not prove that those exceptional candidates do not exist, and it gives no improved bound for `M(X)`. It shows that a surviving moving-character scheme cannot rely on a plentiful family of acceptable quadratic comparators: positive feedback forces an extreme terminal prime bias, and the classical multiplicative large sieve permits that bias for only a very sparse family of primitive characters.

## 1. Feedback contraction forces almost every terminal prime to be a nonresidue

For `q<=Q<=X/2`, the conductor prime does not lie in the terminal interval `(X/2,X]`. Define

\[
\mathcal P_+(X;q)
:=
\{p:X/2<p\le X,\ \chi_q(p)=+1\}.
\tag{10}
\]

By positivity and `(2)`,

\[
R_\theta(X;q)
\ge
2\sum_{p\in\mathcal P_+(X;q)}p^{-\theta}
\ge
2X^{-\theta}\#\mathcal P_+(X;q).
\tag{11}
\]

Hence every `q in mathcal B_theta(X,Q)` satisfies

\[
\boxed{
\#\mathcal P_+(X;q)<\frac12X^\theta
\le\frac12X^{1-\eta}.
}
\tag{12}
\]

Thus the feedback condition is much stronger than a modest residue-class imbalance. In the final dyadic prime interval it demands that only `o(X/log X)` primes be quadratic residues.

Introduce the weighted terminal prime mass

\[
W(X)
:=
\sum_{X/2<p\le X}\log p
\tag{13}
\]

and the quadratic prime twist

\[
T_q(X)
:=
\sum_{X/2<p\le X}\chi_q(p)\log p.
\tag{14}
\]

Because `q` is outside the interval, every terminal prime has character value `+1` or `-1`. If

\[
W_+(X;q)
:=
\sum_{p\in\mathcal P_+(X;q)}\log p,
\]

then exactly

\[
T_q(X)=2W_+(X;q)-W(X).
\tag{15}
\]

Equation `(12)` gives

\[
W_+(X;q)
\le
\frac12X^\theta\log X
\le
\frac12X^{1-\eta}\log X.
\tag{16}
\]

The prime number theorem gives

\[
W(X)=\frac X2+o(X).
\tag{17}
\]

Since `X^{-eta}log X -> 0`, equations `(15)`--`(17)` imply, uniformly in `(3)`, that for all sufficiently large `X`,

\[
\boxed{
T_q(X)\le-\frac X4
}
\qquad(q\in\mathcal B_\theta(X,Q)).
\tag{18}
\]

The particular constant `1/4` is inessential. The structural point is that `R_theta<1` forces a **linear-size negative character correlation with the terminal primes**.

This deduction uses no zero-free region and no exceptional-zero dichotomy. It is purely the positive prime part of the feedback kernel plus the ordinary prime number theorem.

## 2. The multiplicative large sieve allows only few such extreme characters

Use the coefficient sequence supported on the same terminal interval,

\[
a_n
:=
\begin{cases}
\log n,&X/2<n\le X\text{ and }n\text{ prime},\\
0,&\text{otherwise}.
\end{cases}
\tag{19}
\]

The classical multiplicative large sieve for primitive Dirichlet characters states that for coefficients supported on an interval of length `N`,

\[
\sum_{r\le Q}\frac r{\varphi(r)}
\sum_{\chi\ (\mathrm{mod}\ r)}^{*}
\left|\sum_n a_n\chi(n)\right|^2
\le
(N+Q^2-1)\sum_n|a_n|^2.
\tag{20}
\]

Here the star denotes primitive characters. This is standard large-sieve prior art; a convenient authoritative reference is Iwaniec and Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53 (2004), Chapter 7, Theorem 7.13. The inequality goes back to the classical large-sieve theory of Montgomery and Vaughan; see also H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika 20 (1973), 119–134, DOI `10.1112/S0025579300004708`.

For `(19)` the interval length is at most `X`, while

\[
\sum_n|a_n|^2
=
\sum_{X/2<p\le X}(\log p)^2
\le
(\log X)W(X)
\ll X\log X.
\tag{21}
\]

For every odd prime `q`, the Legendre symbol `chi_q` is a primitive nonprincipal character modulo `q`, so its term is present on the left of `(20)`. Moreover `q/phi(q)>1`. Therefore `(18)` implies

\[
\sum_{q\in\mathcal B_\theta(X,Q)}
\frac q{\varphi(q)}|T_q(X)|^2
\gg
\#\mathcal B_\theta(X,Q)\,X^2.
\tag{22}
\]

On the other hand, `(20)` and `(21)` give

\[
\sum_{q\in\mathcal B_\theta(X,Q)}
\frac q{\varphi(q)}|T_q(X)|^2
\ll
(X+Q^2)X\log X.
\tag{23}
\]

Comparing `(22)` and `(23)` proves `(6)`.

Nothing quadratic-specific is needed on the sieve side beyond primitivity of the selected Legendre symbols. A quadratic large sieve could also be applied to this family, but the ordinary multiplicative large sieve is already stronger than necessary for the current `q=X^{o(1)}` corridor and keeps the obstruction independent of reciprocity conventions.

## 3. Coupling the count to the current comparator corridor

`MC-067` leaves the positive-triangle version of the quadratic comparator, at a near-critical exponent, only the method-specific conductor window

\[
\exp\!\bigl(b\sqrt{\log X}\bigr)<q<X^{o(1)}.
\tag{24}
\]

The lower boundary comes from Page–Siegel control of terminal split primes. The upper boundary comes from asking Munsch's squarefree-character estimate

\[
|F_q(X)|
\ll
X^{1/2}q^{3/16}\,\operatorname{polylog}(Xq)
\tag{25}
\]

to remain at `X^(1/2+o(1))` scale.

Let `Q(X)=X^{o(1)}` be any concrete conductor cap supplied by such an implementation. Eventually

\[
Q(X)\le X^{1/2}.
\]

Equation `(8)` then gives

\[
\boxed{
\#\{q\le Q(X):q\text{ prime},\ R_\theta(X;q)<1\}
\ll_\eta\log X.
}
\tag{26}
\]

Combining `(24)` and `(26)`, every surviving positive-feedback comparator must be selected from a logarithmically sized exceptional set lying above the Page–Siegel range. The result is intentionally **not** an existence theorem: the large sieve bounds the number of possible extreme correlations but cannot exclude a single exceptional primitive character.

This also separates two distinct ways the present route could change. If a better squarefree-character theorem merely enlarges the permitted conductor cap while keeping `Q<=X^(1/2)`, the logarithmic sparsity `(8)` survives unchanged. If a new certificate pushes the useful conductor range above square-root scale, the general estimate `(6)` records exactly where the ordinary large-sieve counting argument starts to weaken.

## 4. Prior art and novelty boundary

The analytic input `(20)` is entirely classical. The multiplicative large sieve was designed precisely to prevent one coefficient sequence from having large correlation with too many primitive characters. Modern refinements for prime moduli, such as Henryk Iwaniec, *The large sieve with prime moduli*, Revista Matemática Iberoamericana 38 (2022), 2337–2354, DOI `10.4171/RMI/1381`, and work on distributions of large quadratic character sums provide a much richer surrounding theory, but none is needed for `(6)`.

The passage from a small positive feedback budget to the extreme terminal bias `(18)` is an exact specialization of the `MC-066` kernel and contains no new theorem about Dirichlet characters. Applying the standard family-energy inequality to that bias is likewise a direct classical mechanism. Accordingly **no standalone novelty claim is made**.

The durable line-specific contribution is the frontier synthesis: `MC-067` is pointwise and loses control beyond the Page range because a potential exceptional zero may suppress split primes; the large sieve does not resolve that pointwise exceptional case, but it remains effective **uniformly over the whole family**. It shows that the unresolved pointwise loophole cannot occur for more than a logarithmically sized set of sub-square-root prime conductors at one scale.

A targeted prior-art audit around multiplicative large-sieve inequalities, prime-modulus refinements, and distributions of large quadratic character sums found this family-energy mechanism to be established mathematics rather than a new character-sum theorem. The stored result is therefore an obstruction tailored to the exact Mathia feedback carrier.

## 5. Boundaries and falsification tests

The conclusion is deliberately narrow.

- It applies only to the positive-kernel triangle closure `R_theta(X;q)<1` isolated in `MC-066`. An argument that keeps the signs of the terms `h_q(d)M(X/d)` and proves cancellation among them is outside this obstruction.
- The fixed gap `theta<=1-eta` is load-bearing. It makes `X^theta log X=o(X)`, converting feedback sparsity into the linear character bias `(18)`. If `theta` approaches `1` too rapidly, this proof no longer gives a linear terminal correlation.
- The clean statement assumes `q<=Q<=X/2`, so the conductor prime is absent from `(X/2,X]`. Allowing a conductor inside the terminal interval changes `(15)` only by one `O(log X)` term, but that extension is not needed for the active subpower corridor and is not claimed here.
- The estimate is a **counting** theorem. It does not rule out one or several exceptional conductors, identify them, or prove they are Landau–Siegel exceptional.
- No independence, random-character model, GRH, zero-density theorem, or zeta zero-free region is used. The only asymptotic prime input outside the large sieve is the ordinary prime number theorem in `(17)`.
- The logarithmic count in `(8)` is not asserted to be sharp. Stronger quadratic-family or prime-modulus large-sieve technology may improve constants or ranges; such refinements would not change the present qualitative conclusion for `Q=X^{o(1)}`.
- No estimate for `M(X)` follows from `(6)` or `(8)`.

The claim would fail if `R_theta<1` did not force `(12)`, if the resulting terminal character sum were not linear in `X`, if the quadratic characters were not primitive, or if the multiplicative large sieve did not contain those character sums with total energy bounded by `(20)`. Each step is explicit and independently checkable.

## Consequence for the active frontier

The positive quadratic-feedback branch is now squeezed in three independent ways. `MC-066` requires simultaneous control of the squarefree comparator and of a power-weighted split-prime feedback budget. `MC-067` proves that every conductor up to a fixed stretched-exponential scale fails the feedback side, even in the presence of an exceptional zero. The present finding shows that beyond that range but below square-root conductor scale, **feedback-capable characters form at most a logarithmically sized exceptional family**.

Therefore a continuation of this exact architecture must do more than search a broad moving-conductor window. It must either isolate and control a very sparse sequence of extremely prime-biased quadratic characters, strengthen the pointwise arithmetic enough to eliminate that residual exceptional family, or abandon the positive triangle inequality and exploit signed cancellation inside the feedback recurrence itself.