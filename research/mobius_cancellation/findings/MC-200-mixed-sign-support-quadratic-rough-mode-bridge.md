# MC-200 — Mixed sign-support covariance gives a quadratic rough-mode bridge, but fixed-shift decorrelation has no power budget

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `BOUNDARY/CONDITIONAL-GAIN`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-190`--`MC-194` show that equivariant linear and same-field quadratic statistics of the logarithmic-primorial residue vector cannot transfer controlled transverse character information into its principal rough Möbius mode. `MC-196` finds a genuine cubic escape after residue aggregation, but its exact source expansion pays for signed pair and triple correlations on the polynomially sparse shift lattice `q\mathbb N`. `MC-199` then isolates the remaining identifiability requirement: a centered nonlinear statistic cannot recover the deleted principal coordinate without an additional source-side relation.

Retaining the **square-free support field together with the sign field** lowers the algebraic degree of such a source bridge. The cubic interaction of `MC-196` is not minimal in this two-field representation.

Let

\[
q=q_y=\prod_{p\le y}p,
\qquad y=c\log X,
\qquad 0<c<\tfrac12,
\tag{1}
\]

and define

\[
g(n)=\mu(n)\mathbf 1_{(n,q)=1}.
\tag{2}
\]

For `a\in G=(\mathbb Z/q\mathbb Z)^\times`, put

\[
A_a=\sum_{\substack{n\le X\\n\equiv a\pmod q}}g(n),
\qquad
B_a=\sum_{\substack{n\le X\\n\equiv a\pmod q}}g(n)^2,
\tag{3}
\]

with

\[
S=\sum_a A_a=G_y(X),
\qquad
Q=\sum_a B_a,
\qquad
\phi=\varphi(q),
\tag{4}
\]

and centered fields

\[
u_a=A_a-\frac S\phi,
\qquad
v_a=B_a-\frac Q\phi.
\tag{5}
\]

Define the centered mixed covariance

\[
C_{1,2}:=\sum_{a\in G}u_av_a
\tag{6}
\]

and the ordered distinct same-residue sign-support correlation

\[
E_{1,2}:=
\sum_{a\in G}
\sum_{\substack{n,m\le X\\n\ne m\\n\equiv m\equiv a\pmod q}}
g(n)g(m)^2.
\tag{7}
\]

Then the following identity is exact:

\[
\boxed{
E_{1,2}-C_{1,2}
=
S\left(\frac Q\phi-1\right).
}
\tag{8}
\]

Hence whenever `Q\ne\phi`, the rough principal mode has the quadratic source decoder

\[
\boxed{
S=
\frac{E_{1,2}-C_{1,2}}{Q/\phi-1}.
}
\tag{9}
\]

The denominator is not the active obstruction at the logarithmic primorial. Every prime `p` with `y<p\le X` contributes to `Q`, while `\phi\le q` and the prime number theorem gives `q=X^{c+o(1)}`. Therefore

\[
Q\ge \pi(X)-\pi(y),
\qquad
\frac Q\phi\ge X^{1-c-o(1)},
\tag{10}
\]

so in particular

\[
\boxed{
\frac Q\phi-1\ge X^{1-c-o(1)}.
}
\tag{11}
\]

The bridge is thus polynomially well-conditioned. It also genuinely uses transverse information: with normalized multiplicative Fourier coefficients,

\[
\widehat A(\chi)=\frac1\phi\sum_a A_a\overline{\chi(a)},
\qquad
\widehat B(\chi)=\frac1\phi\sum_a B_a\overline{\chi(a)},
\tag{12}
\]

one has

\[
\boxed{
\frac{C_{1,2}}\phi
=
\sum_{\chi\ne1}
\widehat A(\chi)\widehat B(\chi^{-1}).
}
\tag{13}
\]

So `C_{1,2}` is built entirely from nonprincipal sign/support character sectors, while `E_{1,2}` is the additional uncentered source statistic demanded by `MC-199`.

The gain over the cubic source relation is exact but limited. Writing

\[
H_{1,2}(r)
:=
\sum_{n\le X-r}
\left(
 g(n)g(n+r)^2+g(n)^2g(n+r)
\right),
\tag{14}
\]

same-residue pairs give

\[
\boxed{
E_{1,2}
=
\sum_{1\le h\le (X-1)/q}H_{1,2}(hq).
}
\tag{15}
\]

Thus the source bill has dropped from the pair-plus-triple family of `MC-196` to a **mixed two-point** family, but it still lies on the deterministic polynomially sparse lattice `q\mathbb N`, whose spacing is `X^{c+o(1)}`.

Moreover, the obvious attempt to exploit the square-free factor in `(14)` is circular at first order. For `r` divisible by `q`, the classical identity

\[
\mu(m)^2=\sum_{d^2\mid m}\mu(d)
\tag{16}
\]

gives

\[
\sum_{n\le X-r}g(n)g(n+r)^2
=
\sum_{\substack{d\ge1\\(d,q)=1}}
\mu(d)
\sum_{\substack{n\le X-r\\n\equiv-r\pmod{d^2}}}g(n),
\tag{17}
\]

and the `d=1` term is exactly

\[
G_y(X-r).
\tag{18}
\]

Similarly,

\[
\sum_{n\le X-r}g(n)^2g(n+r)
=
\sum_{\substack{d\ge1\\(d,q)=1}}
\mu(d)
\sum_{\substack{r<m\le X\\m\equiv r\pmod{d^2}}}g(m),
\tag{19}
\]

whose `d=1` term is

\[
G_y(X)-G_y(r).
\tag{20}
\]

Thus replacing a signed factor by square-free support does not by itself make the required source correlation cheap: the direct square-divisor expansion immediately reintroduces the same rough principal sums that the bridge is meant to control.

Finally, existing qualitative correlation theory cannot pay the missing quantitative bill. The exact-support multiplicative comparator `a_\ell=\mu^2\sigma_\ell` from `MC-005` and `MC-040`, for any fixed prime `\ell\ge5`, satisfies

\[
\sum_{n\le x}a_\ell(n)
\sim C_\ell\frac{x}{(\log x)^{2/(\ell-1)}}
\qquad(C_\ell>0),
\tag{21}
\]

while for every fixed distinct shifts `h_1,h_2`, Tao--Teräväinen's logarithmically averaged correlation theorem (`MC-S28`) applies to

\[
g_1=a_\ell,
\qquad
g_2=a_\ell^2=\mu^2,
\qquad
g_1g_2=a_\ell^3=a_\ell,
\tag{22}
\]

because `MC-040` proves that `a_\ell` does not weakly pretend to any Dirichlet character. Consequently

\[
\boxed{
\sum_{n\le x}
\frac{a_\ell(n+h_1)a_\ell(n+h_2)^2}{n}
=o(\log x),
}
\tag{23}
\]

and likewise with the signed and squared factors reversed. The comparator therefore has exact Möbius square-free support, multiplicativity, qualitative fixed-shift mixed sign-support decorrelation, and nevertheless only logarithmic-order mean cancellation.

The lower-degree bridge in `(8)` is therefore a real frontier improvement, not a solution. A successful route now has a sharper target: obtain a **polynomially quantitative, growing-shift, pre-sieved estimate for the specific aggregate `(15)`**, or another identity that cancels its principal contamination. Merely proving more fixed-shift or logarithmically averaged mixed correlations cannot imply a fixed-power Mertens bound.

No improved estimate for `G_y(X)`, `M(X)`, or the Riemann zero set is claimed.

## 1. Exact quadratic identity

For one residue class, abbreviate the values of `g` in that class by `x_i\in\{-1,0,1\}`. Then

\[
A=\sum_i x_i,
\qquad
B=\sum_i x_i^2.
\]

Expanding the product gives

\[
AB
=
\sum_i x_i^3
+
\sum_{i\ne j}x_ix_j^2.
\tag{24}
\]

Since `x_i^3=x_i`, the diagonal term is `A`. Therefore, after summing over classes,

\[
E_{1,2}
=
\sum_a A_aB_a-S.
\tag{25}
\]

Using `(5)` and `\sum_a u_a=\sum_a v_a=0`,

\[
\sum_a A_aB_a
=
\sum_a
\left(\frac S\phi+u_a\right)
\left(\frac Q\phi+v_a\right)
=
\frac{SQ}\phi+C_{1,2}.
\tag{26}
\]

Combining `(25)` and `(26)` proves `(8)`--`(9)`.

This is precisely the source datum missing from the quotient in `MC-199`. The centered pair `(u,v)` determines `C_{1,2}` but not `E_{1,2}`; the latter remembers how the signed source values sit against **other supported source sites in the same residue class**.

## 2. The denominator is polynomially conditioned

The rough support count is

\[
Q
=
\sum_{\substack{n\le X\\(n,q)=1}}\mu(n)^2.
\tag{27}
\]

Every prime in `(y,X]` occurs in this sum, so

\[
Q\ge\pi(X)-\pi(y).
\tag{28}
\]

The prime number theorem and `y=c\log X` give

\[
\pi(X)-\pi(y)=X^{1-o(1)},
\qquad
q=\exp(\vartheta(y))=X^{c+o(1)}.
\tag{29}
\]

Since `\phi\le q`, equations `(28)`--`(29)` imply `(10)`--`(11)`. No estimate for `M`, no zero-free continuation of `1/\zeta`, and no unproved square-free equidistribution statement enters this conditioning argument.

This matters because `MC-196` leaves conditioning of its cubic bracket as an independent requirement. In the present two-field decoder, the scalar coefficient multiplying `S` is already known to be polynomially large. The only unresolved arithmetic cost is the numerator.

## 3. Character-space meaning and relation to the previous no-go

Fourier inversion on the finite abelian group `G` gives

\[
u_a=\sum_{\chi\ne1}\widehat A(\chi)\chi(a),
\qquad
v_a=\sum_{\chi\ne1}\widehat B(\chi)\chi(a).
\tag{30}
\]

Character orthogonality proves `(13)`. Products of a nonprincipal sign character and the inverse support character can therefore land in the trivial representation at quadratic degree.

This does not contradict `MC-190` or `MC-194`. Those findings classify equivariant linear/Hermitian quadratic processing of the signed residue vector itself. Here there are **two source fields**, `A` and `B`, and their tensor product contains a trivial sector. Nor does it contradict `MC-199`: `C_{1,2}` remains a centered-only invariant and cannot decode `S` alone. Equation `(8)` works only because `E_{1,2}` imports an additional uncentered inter-site source relation.

The conclusion is a useful correction to the live nonlinear hierarchy: degree three is the first escape if one insists on nonlinear processing of the signed aggregate field alone, but **degree two already suffices once the exact square-free support field is retained as a second channel**.

## 4. The source bridge is a prescribed mixed-shift problem

Every distinct pair in one residue class differs by `hq` for a unique positive integer `h`; the two orientations contribute the two terms in `(14)`. This proves `(15)`.

At the active scale,

\[
q=X^{c+o(1)},
\qquad
\#\{h:hq<X\}=X^{1-c+o(1)}.
\tag{31}
\]

So the relevant source family is neither a fixed-shift correlation nor an average over all shifts. It is a deterministic polynomially sparse family whose modulus and coefficient `g` both vary with `X`.

The generic sparse-restriction problem from `MC-196` therefore survives at lower correlation order. A theorem giving only a logarithmic saving after averaging over all shifts can still concentrate its permitted mass on a subset of density `q^{-1}=X^{-c+o(1)}`. What has improved is the **type of correlation that must be controlled**: one signed Möbius factor against one square-free-support factor, rather than the signed triple family in `(18)` of `MC-196`.

## 5. Why the square-free expansion does not close the bridge

For `r=hq`, if `g(n)\ne0` then `(n,q)=1`, hence also `(n+r,q)=1`. Expanding the square-free indicator by `(16)`, any divisor `d` sharing a prime with `q` gives zero: `d^2\mid n+r` and `q\mid r` would force that prime to divide `n`, contradicting `g(n)\ne0`. This proves `(17)`.

The reverse orientation follows by expanding `g(n)^2` and then substituting `m=n+r`, giving `(19)`.

Equations `(18)` and `(20)` are the decisive audit. They show that the most immediate classical treatment of the squared factor has a principal `d=1` component. A proof that bounds `(17)`--`(19)` by first isolating this term and then inserts the known Korobov--Vinogradov bound for `G_y` has not created a new fixed-power mechanism; it has merely recycled the current zero-mode estimate.

This does **not** prove that `(15)` is as hard as Mertens. A bilinear, dispersion, spectral, or cancellation argument could in principle control the complete mixed correlation without estimating its square-divisor pieces absolutely. The finding only identifies the circularity of the naive expansion and the exact quantitative theorem that a successful alternative must supply.

## 6. Prior art and matched-control audit

The algebra `(24)`--`(26)`, character orthogonality in `(30)`, and the square-free identity `(16)` are classical/elementary mechanisms. No novelty is claimed for them as standalone mathematics.

Mixed sign/support correlations are also within established multiplicative-correlation theory. `MC-S28` treats general products of shifted `1`-bounded multiplicative functions and forces logarithmically averaged cancellation when their pointwise product does not weakly pretend to a Dirichlet character. Specializing to `g_1=\mu` and `g_2=\mu^2` places fixed-shift true-Möbius sign/support correlations inside that prior-art language; specializing to `(22)` gives the matched comparator statement `(23)`.

A targeted literature search over Möbius/square-free shifted correlations, logarithmically averaged multiplicative correlations, and square-free distribution found these established component languages but no theorem output matching the present need: a fixed-power ordinary estimate, uniform over the growing pre-sieved lattice `r=hq` with `q=X^{c+o(1)}`. This absence is **not** a novelty claim or a claim of impossibility; it fixes the current prior-art boundary for the route.

The exact-support comparator makes the information deficit explicit. Equations `(21)` and `(23)` can coexist, so a proposed implication from multiplicativity, exact square-free support, and qualitative fixed-shift mixed decorrelation to `S(x)=O(x^{1-\delta})` is false as a black-box principle. The new route must use quantitative strength, growing-shift uniformity, rational-prime-specific structure absent from the comparator, or another source identity.

## 7. Boundaries and falsification tests

- Equation `(8)` is exact for any finite ternary source partitioned into `\phi` classes; its arithmetic relevance comes from the primorial choice and the interpretation of `A,B`.
- The polynomial lower bound `(11)` uses only primes in the support and is deliberately crude. It establishes conditioning, not an asymptotic formula for `Q`.
- `C_{1,2}` is transverse, but no current result proves the fixed-power bound on it needed by a successful decoder. Its character expression does not make it automatically controlled by the same theorem as the signed-field variance.
- `E_{1,2}` is additional source information, not a function of the centered quotient. Estimating it by reconstructing `S` or by using `(8)` backwards is circular.
- The square-divisor expansions `(17)` and `(19)` expose one circular route but do not rule out cancellation across `d`, across `h`, or through a different representation of the complete mixed sum.
- The Tao--Teräväinen statement used in `(23)` is logarithmically averaged and fixed-shift. It supplies no polynomial rate uniform in shifts growing like `X^c` and no direct estimate for the pre-sieved aggregate `(15)`.
- The comparator `a_\ell` has the exact square-free support and multiplicativity of Möbius but different prime signs. A theorem using `\mu(p)=-1` for every rational prime, or another exact rational-prime input, is outside this control and remains viable.
- No claim is made that mixed two-point correlations are generally easier than signed triple correlations at the required polynomial uniformity. Only the algebraic source order has been reduced.

The core identity is falsified if `(25)` or `(26)` fails on any finite ternary residue array. The conditioning claim is falsified if primes `y<p\le X` fail to contribute to `(27)` or if `q=X^{c+o(1)}` fails for the primorial `(1)`. The matched-control boundary is falsified if `MC-S28` does not apply to `(22)` under the non-weak-pretence property already established in `MC-040`.

## Consequence for the active frontier

The principal-mode problem now has a lower-degree candidate bridge. The live search need not insist on cubic signed interactions: **signed residue mass coupled to the exact square-free support field already yields a polynomially conditioned quadratic decoder**.

But the gain is only useful if its source numerator is controlled independently. The next mathematically consequential target is therefore narrower than the generic `MC-196` pair/triple bill: determine whether the aggregate mixed correlation `(15)` admits fixed-power cancellation on the logarithmic-primorial shift lattice by methods that do not isolate the `d=1` rough Mertens term. A successful estimate would provide a genuinely new principal/transverse coupling channel; failure under a sharp matched multiplicative control would close this lower-degree escape and return the frontier to richer source structure.