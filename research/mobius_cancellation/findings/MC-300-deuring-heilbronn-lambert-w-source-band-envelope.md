# MC-300 — Deuring–Heilbronn has a Lambert-W source-band envelope at fixed inverse-log accuracy

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`

## Claim

Continue the exceptional Page-shell setup of `MC-293` and the Deuring–Heilbronn refinement of `MC-299`. Write

\[
L_1=\log y,\qquad L_2=\log\log y,\qquad L_3=\log\log\log y,
\]

and let the exceptional primitive real character have zero

\[
\beta_*=1-\delta_*.
\]

Suppose a nonexceptional target shell character is embedded together with the exceptional character into a common modulus `q`, and put

\[
v=\log q.
\]

Take the truncated explicit formula at polylogarithmic height

\[
T=L_1^B
\]

for a fixed `B>0`. Benli–Goel–Twiss–Zaman's explicit Deuring–Heilbronn theorem gives every other zero `rho=beta+i gamma`, `|gamma|<=T`, the repulsion

\[
1-\beta
>
R(q,T,\delta_*)
:=
\frac{\log\!\bigl(1/(16\delta_*H)\bigr)}{H},
\qquad
H=10\log q+\log T+107,
\tag{1}
\]

whenever the logarithm is positive and the theorem's exceptional-zero hypothesis holds.

For every fixed desired shell accuracy `A>0`, the direct route

\[
\text{Deuring--Heilbronn }(1)
\quad+\quad
\text{standard truncated explicit formula}
\]

has the following quantitative envelope. Up to constants depending only on `A` and the fixed truncation choice, inverse-log shell cancellation

\[
|x_\lambda|\ll_A L_1^{-A}
\tag{2}
\]

is certified whenever

\[
\boxed{
 v
 \ \lesssim_A\ 
 \frac{L_1}{L_2}
 W\!\left(
 c_A\frac{L_2}{\delta_*L_1}
 \right),
}
\tag{3}
\]

where `W` is the principal Lambert function, `W(z)e^{W(z)}=z`, and `c_A>0` is a fixed constant.

Conversely, `(3)` describes the order of the **uniform certificate available from this particular black-box route**: if one knows only the coarse exceptional-zero input from `MC-293`,

\[
\delta_*\ll_a\frac1{L_1L_2},
\tag{4}
\]

then the worst admissible value on the right of `(4)` gives

\[
W\!\left(c\,L_2^2\right)
=
2L_3-\log(2L_3)+O(1).
\tag{5}
\]

Hence the largest common-modulus band that `(1)` can certify uniformly from **only** `(4)` at any prescribed fixed inverse-log accuracy has order

\[
\boxed{
\log q
=
O_A\!\left(\frac{L_1L_3}{L_2}\right).
}
\tag{6}
\]

In the Page-shell application, `q<=16D_y\mathcal Q(\lambda)` with

\[
\log D_y\asymp\frac{L_1}{L_2},
\]

so `(6)` yields exactly the source-cost scale of `MC-299`,

\[
\boxed{
\log \mathcal Q(\lambda)
=
O_A\!\left(\frac{L_1L_3}{L_2}\right).
}
\tag{7}
\]

Thus the `log log log y` enlargement in `MC-299` is not an arbitrary parameter choice. It is the natural Lambert-W scale obtained by balancing the logarithmic Deuring–Heilbronn repulsion numerator against the conductor appearing in its denominator.

This is a **certificate ceiling, not a mathematical impossibility theorem**. If the actual exceptional zero is substantially closer to `1` than `(4)` records, then `(3)` widens automatically. A stronger zero-repulsion theorem, a collective density/capacity argument, or new arithmetic information can also escape `(6)`. What is ruled out is the expectation that one can push the `MC-299` black-box argument to a parametrically larger source band merely by retuning its constants while retaining only `(4)`.

## 1. Fixed inverse-log shell accuracy requires a zero-free width of order `L_2/L_1`

The explicit-formula step in `MC-299` bounds the target prime sum by a zero contribution of the shape

\[
y^{1-R(q,T,\delta_*)}L_1^{O(1)}
\]

plus the truncation term. Choosing `B` sufficiently large in terms of `A`, the truncation term is harmless. After absorbing the fixed powers of `L_1` coming from zero counting and partial summation, it is enough that

\[
R(q,T,\delta_*)L_1
\ge K_A L_2
\tag{8}
\]

for a sufficiently large fixed `K_A>0`.

Substituting `(1)` into `(8)` gives

\[
\log\frac1{16\delta_*H}
\ge
K_A\frac{HL_2}{L_1}.
\tag{9}
\]

At the source bands relevant here, `v\gg L_2`, while `\log T=BL_2`; therefore

\[
H\asymp v
\tag{10}
\]

with absolute constants. Equation `(9)` is consequently equivalent up to fixed constants to

\[
\delta_*v
\exp\!\left(
C_A\frac{vL_2}{L_1}
\right)
\ll_A 1.
\tag{11}
\]

The appearance of Lambert `W` is now forced rather than chosen.

## 2. Solving the conductor/repulsion balance

Set

\[
z=C_A\frac{vL_2}{L_1}.
\]

Then `(11)` becomes, after absorbing fixed constants,

\[
z e^z
\ll_A
\frac{L_2}{\delta_*L_1}.
\tag{12}
\]

Because `z -> z e^z` is increasing on the positive axis, inversion gives

\[
z
\lesssim_A
W\!\left(c_A\frac{L_2}{\delta_*L_1}\right),
\]

which is `(3)`.

This formula also records exactly what extra information would buy a wider band. If a future argument improves the exceptional-zero closeness from `(4)` to some smaller explicit `\delta_*(y)`, the permitted logarithmic conductor grows according to

\[
\frac{L_1}{L_2}
W\!\left(
\frac{L_2}{\delta_*(y)L_1}
\right),
\tag{13}
\]

not linearly in `1/\delta_*`. The logarithm inside the Deuring–Heilbronn numerator is the bottleneck.

## 3. Why the `L_3` scale is forced by the current exceptional-zero input

Using only `(4)`, a uniform deduction must allow the least favorable zero closeness permitted by that estimate. Substitution into `(13)` gives the argument

\[
\frac{L_2}{\delta_*L_1}
\asymp_a L_2^2.
\]

For large `z`,

\[
W(z)=\log z-\log\log z+O\!\left(\frac{\log\log z}{\log z}\right),
\tag{14}
\]

so

\[
W(cL_2^2)
=
2L_3-\log(2L_3)+O(1).
\tag{15}
\]

This proves `(6)`.

The same calculation exposes the failure of a naive super-`L_3` enlargement. If

\[
v=h(y)\frac{L_1L_3}{L_2},
\qquad h(y)\to\infty,
\tag{16}
\]

and one substitutes only the worst-scale information `\delta_*\asymp1/(L_1L_2)`, then the repulsion supplied by `(1)` has

\[
R(q,T,\delta_*)L_1
=O\!\left(\frac{L_2}{h(y)}\right)
=o(L_2)
\tag{17}
\]

through the range where the numerator remains positive. Thus `(8)` cannot be certified for any prescribed fixed inverse-log power. This is precisely the sense in which `(6)` is the uniform black-box ceiling.

The quantifier is important: `(17)` does **not** assert that the actual exceptional zero has the least favorable allowed size, nor that the true nonexceptional zeros sit at the edge of the Deuring–Heilbronn bound. It says only that those stronger facts are absent from the input `(4)` and therefore cannot be recovered by retuning the same inequality.

## 4. Consequence for the current Page-spectrum frontier

`MC-299` showed that a near-negative Page exception is self-isolating over a source band larger than `MC-293` by an unbounded `L_3` factor in the logarithm. The present calculation identifies the exact resource behind that gain and its current limit.

There are now three genuinely different ways to move the source-cost frontier further:

1. **stronger exceptional-zero closeness:** improve the arithmetic deduction of `\delta_*` from the observed Page defect, which enlarges the Lambert-W argument in `(13)`;
2. **stronger family information:** use zero-density, collective character restrictions, or source-capacity information that controls many high-cost modes simultaneously rather than one target character through a common modulus;
3. **a different arithmetic carrier:** bypass the exceptional-zero/explicit-formula channel entirely.

By contrast, simply choosing a larger `E_y` in `MC-299`, increasing the fixed truncation exponent `B`, or optimizing constant factors in the same explicit Deuring–Heilbronn corollary cannot produce a parametrically super-`L_3` uniform band from `(4)`.

This sharpens the frontier exposed by `MC-298`: bounded overlap hierarchy is generically parity-blind, while the single-exception Deuring–Heilbronn repair has now been parameterized to its present information limit. The unresolved problem is therefore not another constant optimization; it is additional arithmetic information about exceptional-zero closeness or collective realizability of the high-source-cost Page modes.

## 5. Prior art and novelty audit

The zero-repulsion theorem is classical in mechanism and explicit in the form used here. Kübra Benli, Shivani Goel, Henry Twiss and Asif Zaman, *Explicit Deuring–Heilbronn phenomenon for Dirichlet L-functions*, Proceedings of the American Mathematical Society 154 (2026), 509–525, DOI `10.1090/proc/17450`, arXiv `2410.06082v3`, Corollary 1.1, supplies `(1)`. The paper's current arXiv version was revised 8 January 2026 and gives a uniform explicit repulsion estimate throughout the critical strip. Classical Deuring–Heilbronn bounds have the same qualitative `log(1/((1-beta_*)\times\text{conductor scale}))/\text{conductor scale}` structure; the recent result provides the constants already used in `MC-299`.

The truncated explicit-formula passage from a zero-free width to prime-sum cancellation is standard analytic number theory and was already audited in `MC-299`. Solving the resulting exponential inequality with Lambert `W` is elementary algebra. A targeted prior-art search did not identify this exact Page-source-cost packaging as a standard named result, but no novelty is claimed for the optimization itself. The durable content here is the explicit parameter envelope and the resulting no-go for a super-`L_3` **uniform certificate from the existing coarse input**, not a new Deuring–Heilbronn theorem.

## 6. Boundaries and falsification

The finding fails if the required fixed inverse-log shell accuracy can be obtained from the same inputs without a zero-free width of order `L_2/L_1`; any such argument would bypass the explicit-formula budget `(8)` and would be a genuinely different mechanism.

The envelope also changes if the actual `\delta_*` is independently shown to be much smaller than `(4)`. That is not a counterexample: equation `(13)` explicitly predicts the larger source band. Likewise, a zero-density argument can exploit scarcity rather than uniform exclusion and is not constrained by this single-character certificate.

No statement is made about the existence of a Landau–Siegel zero, the actual location of nonexceptional zeros, or `M(x)`. The result is a quantitative audit of one current proof channel. It rules out only a methodological shortcut: extending `MC-299` parametrically past the `L_3` scale without supplying new arithmetic information.