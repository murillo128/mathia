# WI-187 — local bow normalization has a resolution--reservoir tradeoff

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding closes only the **naive black-box short-height escape** left open by WI-185--WI-186: localizing the Montgomery prime-side mean square to the vertical height occupied by a Maynard--Pratt bow and then invoking the classical Montgomery--Vaughan Dirichlet-polynomial mean-value theorem. It does **not** rule out a source-specific localized explicit formula with stronger cancellation, smoothing that changes the arithmetic remainder, non-principal bow--reservoir coupling, or new support/arithmetic information.

The new point is a quantitative dichotomy. For a mirror-closed bow with `m=T^epsilon` selected right-half labels and ordinate step `c/log T`, the source-compatible reciprocal frequency is

\[
\alpha_*=\frac{2\pi}{c}
\]

by WI-184. A local form-factor proof at that frequency naturally encounters Dirichlet-polynomial length `x=T^{\alpha_*}`. The bow itself occupies only height

\[
H_{\rm bow}\asymp \frac{cT^\varepsilon}{\log T}.
\]

The classical black-box mean-value error is of relative size `x/H_bow` on a dyadic length-`x` piece. Therefore local diagonal dominance requires, at exponent level,

\[
\boxed{\varepsilon>\alpha_*=\frac{2\pi}{c}.}
\]

At the count-saturating source-compatible spacing `c=4\pi`, this becomes `\varepsilon>1/2`, so every Maynard--Pratt bow with fixed `\varepsilon<1/2` remains below black-box arithmetic resolution even after normalization to its own height. Conversely, forcing `\varepsilon>2\pi/c` by taking larger `c` makes Riemann--von Mangoldt compel a complementary zero reservoir comprising asymptotically more than `1-2\varepsilon` of all zeros in the same bow interval. Thus the elementary local-normalization escape has an exact tradeoff: **arithmetic resolution can be bought only by making the selected bow a small minority of the local zero population.**

## 1. Geometry inherited from WI-184

Write

\[
L:=\log T,
\qquad
m=T^\varepsilon,
\qquad
\gamma_j=T_0+\frac{cj}{L},
\qquad 1\le j\le m,
\tag{1}
\]

with fixed `c>0` and fixed `0<\varepsilon<1/2`, as in the Maynard--Pratt schematic bow. The occupied vertical span is

\[
H_{\rm bow}
=\gamma_m-\gamma_1
=\frac{c(m-1)}{L}
=\left(c+o(1)\right)\frac{T^\varepsilon}{L}.
\tag{2}
\]

WI-184 adds the compulsory same-ordinate functional-equation mirror and compares the resulting `2m-O(1)` selected zeros with Riemann--von Mangoldt. It proves the source-compatibility gate

\[
\boxed{c\ge4\pi-o(1)}
\tag{3}
\]

and, for fixed `c`, the complementary-zero count in the same interval

\[
R_I
=\left(\frac{c}{2\pi}-2+o(1)\right)m.
\tag{4}
\]

The unfolded vertical step is `d=c/(2\pi)`, so the first reciprocal line is

\[
\boxed{\alpha_*=\frac1d=\frac{2\pi}{c}.}
\tag{5}
\]

At `c=4\pi`, one has `\alpha_*=1/2`; WI-184 shows that the selected mirror-pair amplitude is phase coherent there independently of horizontal bow drift.

## 2. Classical local Dirichlet-polynomial mean-value scale

Montgomery and Vaughan's generalized Hilbert inequality gives the classical mean-value theorem for a Dirichlet polynomial

\[
A(t)=\sum_{n\le N}a_n n^{-it}.
\]

On any interval `[U,U+H]`, phase-twisting the coefficients by `n^{-iU}` reduces to the interval `[0,H]`, and the theorem gives

\[
\boxed{
\int_U^{U+H}|A(t)|^2\,dt
=
H\sum_{n\le N}|a_n|^2
+O\!\left(\sum_{n\le N}n|a_n|^2\right).
}
\tag{6}
\]

The interval shift therefore costs nothing. On a dyadic piece `n\asymp x`, put

\[
\mathcal A:=\sum_{n\asymp x}|a_n|^2.
\]

Then (6) becomes

\[
\int_U^{U+H}|A(t)|^2\,dt
=H\mathcal A+O(x\mathcal A),
\tag{7}
\]

so a proof that treats (6) only as a black box has guaranteed relative uncertainty

\[
\boxed{O(x/H).}
\tag{8}
\]

This statement is deliberately information-theoretic in the same sense as WI-186: it does not claim that the true off-diagonal term has size `x\mathcal A`; it says the standard theorem alone does not certify cancellation below that scale. Any improvement must use extra structure of the coefficients, smoothing, correlations, or a stronger localized arithmetic theorem.

The primary source for the generalized Hilbert inequality and its Dirichlet-series mean-value application is H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *J. London Math. Soc.* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`. The standard equivalent formulation `\int_0^H |A(t)|^2dt=\sum |a_n|^2(H+O(n))` is a classical corollary of that argument.

## 3. The reciprocal bow frequency fixes the Dirichlet length

The corrected unconditional Montgomery theorem used in WI-186 is naturally parametrized by

\[
x=T^\alpha,
\tag{9}
\]

with `0<=\alpha<=1`; its arithmetic side is a prime/Dirichlet-polynomial mean square at length `x`. This is the standard Montgomery frequency--length correspondence already present in the 1973 pair-correlation framework and retained in the Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh proof.

At the source-compatible bow's first reciprocal line (5), the relevant arithmetic length is therefore

\[
\boxed{
x_*=T^{\alpha_*}=T^{2\pi/c}.}
\tag{10}
\]

If one now attempts the most direct version of the short-height escape from WI-186 -- replace the global height average by an average over the bow's own interval (2), while otherwise invoking the standard mean-value theorem -- the black-box resolution ratio (8) is

\[
\frac{x_*}{H_{\rm bow}}
=
\left(\frac{1}{c}+o(1)\right)
L\,T^{2\pi/c-\varepsilon}.
\tag{11}
\]

Consequently

\[
\boxed{
\varepsilon<\frac{2\pi}{c}
\quad\Longrightarrow\quad
\frac{x_*}{H_{\rm bow}}\to\infty,
}
\tag{12}
\]

and even the exponent-equality case `\varepsilon=2\pi/c` has `x_*/H_bow\asymp L/c\to\infty`. A genuine black-box asymptotic requires

\[
\boxed{
\varepsilon>\frac{2\pi}{c}
}
\tag{13}
\]

(up to any additional logarithmic margins imposed by the concrete coefficient family).

For the count-saturating bow,

\[
c=4\pi,
\qquad
\alpha_*=\frac12,
\qquad
x_*=\sqrt T,
\qquad
H_{\rm bow}\asymp\frac{T^\varepsilon}{\log T}.
\tag{14}
\]

Thus for every fixed `\varepsilon<1/2`,

\[
\boxed{
\frac{x_*}{H_{\rm bow}}
\asymp
\sqrt T\,\frac{\log T}{T^\varepsilon}
\to\infty.
}
\tag{15}
\]

This closes the simplest interpretation of “normalize the form factor to the bow's own height”: at the unique spacing where the bow plus mirrors can asymptotically saturate the local zero count, the classical local Dirichlet-polynomial theorem loses diagonal dominance by a polynomial factor.

## 4. Buying arithmetic resolution forces a large cancellation reservoir

The more useful conclusion comes from combining the arithmetic gate (13) with WI-184's exact zero-count bookkeeping (4). Define the complementary-to-right-half-bow ratio

\[
q:=\frac{R_I}{m}.
\]

For fixed `c`, WI-184 gives

\[
q=\frac{c}{2\pi}-2+o(1).
\tag{16}
\]

Condition (13) is equivalent at exponent level to

\[
c>\frac{2\pi}{\varepsilon}.
\tag{17}
\]

Hence any spacing for which the **standard** local mean-value theorem can resolve the first reciprocal line must satisfy

\[
\boxed{
q>\frac1\varepsilon-2+o(1).
}
\tag{18}
\]

There is an even cleaner formulation in terms of the fraction of all local zeros represented by the selected bow plus its compulsory mirrors. Riemann--von Mangoldt gives total local count

\[
N_I=\left(\frac{c}{2\pi}+o(1)\right)m,
\tag{19}
\]

while the selected mirror-closed bow contributes `2m-O(1)`. Therefore its local fraction is

\[
\frac{2m}{N_I}
=\frac{4\pi}{c}+o(1).
\tag{20}
\]

Under the resolution gate (17),

\[
\boxed{
\frac{2m}{N_I}<2\varepsilon+o(1),
\qquad
\frac{R_I}{N_I}>1-2\varepsilon-o(1).
}
\tag{21}
\]

So for the small fixed `\varepsilon` relevant to the Maynard--Pratt obstruction, a naive local mean-square proof can enter its asymptotic regime only after the selected bow becomes a small minority of the zeros in its own interval. The complementary population that WI-184 left as a possible cancellation reservoir then occupies almost all of the local zero count.

This is a genuine two-sided obstruction rather than merely a restatement of (15):

- near count saturation (`c\approx4\pi`), there need be little local complement, but the arithmetic averaging interval is far too short relative to the required Dirichlet length `\sqrt T`;
- increasing `c` lowers the reciprocal frequency and shortens the Dirichlet polynomial, but once it is short enough for black-box local mean-value control, zero counting forces the unselected reservoir to have local fraction `>1-2\varepsilon`.

Thus the two obvious desiderata -- **small cancellation reservoir** and **black-box arithmetic resolvability** -- cannot hold simultaneously for a `T^\varepsilon`, `\varepsilon<1/2`, bow in this elementary localized architecture.

## 5. Scope, prior art, and escape routes

This finding is not a no-go theorem for all short-height form factors. The mean-value theorem (6) is deliberately used as a black box. Prime-supported coefficients can admit stronger estimates than arbitrary coefficients, smooth localizers can alter the dual arithmetic kernel, and a proof reopened at the explicit-formula level may obtain cancellation in the off-diagonal term that (6) discards. Any such result is **new arithmetic information** relative to this route and would evade the finding legitimately.

Nor does (21) prove that the complementary zeros actually cancel the bow. It says only that the source count forces enough unselected mass to exist whenever one buys the interval length needed by the standard arithmetic theorem. The type of those zeros remains exactly as in WI-184: critical-line zeros, multiple zeros, further off-line pairs, or a mixture. A successful non-principal argument might exploit bow--reservoir cross terms rather than regard the reservoir solely as an adversary.

A targeted prior-art audit checked the classical Montgomery--Vaughan mean-value theorem, Montgomery's frequency/Dirichlet-length correspondence, work on pair correlation and primes in short intervals, and modern short-interval Dirichlet-polynomial estimates. The standard estimate `\int |A|^2\ll(H+x)\sum|a_n|^2` is ubiquitous; specialized sparse/prime-coefficient refinements also exist. No located source supplies the specific unconditional complex-zero localized form-factor theorem needed to bypass (11) for the selected Maynard--Pratt bow. Absence from that search is not evidence of priority, and no priority claim is made.

The relevant established source anchors are:

- H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *J. London Math. Soc.* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`: generalized Hilbert inequality and classical Dirichlet-series mean-value application;
- H. L. Montgomery, **The pair correlation of zeros of the zeta function**, Proc. Sympos. Pure Math. 24 (1973), 181--193: original form-factor frequency/prime-length framework;
- Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, corrected unconditional Montgomery theorem as recorded in WI-186: the current unconditional complex-zero `x=T^alpha` interface;
- Maynard--Pratt, **Half-Isolated Zeros and Zero-Density Estimates**, IMRN 2024:19, 12978--13014, Section 8: the schematic `m=T^epsilon` bow geometry.

## 6. Research consequence

WI-186 left short-height normalization as a high-value escape because the global `T\sqrt{\log T}` pointwise error need not remain the natural uncertainty after localizing. WI-187 shows that the most immediate replacement does not work: the classical local Dirichlet-polynomial theorem introduces its own length barrier. At the count-saturating bow one needs length `\sqrt T` but has height only `T^\varepsilon/\log T`, while moving the reciprocal line low enough to make the classical theorem effective forces almost all local zeros into the unselected reservoir.

The next short-height attempt must therefore do at least one thing that the black-box Montgomery--Vaughan estimate does not: exploit the specific prime coefficients to beat the `x/H` barrier, use a smoother/local dual observable with genuinely shorter arithmetic length, or couple the compulsory reservoir to another sign/inertia invariant instead of trying to isolate the bow principal square. Merely replacing global normalization by the bow's own vertical height is now a closed weak route.