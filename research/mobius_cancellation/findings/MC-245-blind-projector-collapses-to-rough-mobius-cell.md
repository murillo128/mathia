# MC-245 — The blind source projector collapses exactly to one rough Möbius affine cell

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-244` reduced the complete quadratic-blind contribution of the first-shell source to the weighted projector

\[
B_S^{(K)}(X)
=
\frac{2^{\kappa}}{\varphi(q)}
\sum_{\substack{m\le T\\(m,q)=1\\\lambda(-m)\in W}}
\mu(m)\,\Psi(T/m,y),
\tag{1}
\]

where

\[
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\qquad
q=\prod_{r\in S}r^2,
\qquad r\in(y,2y],
\tag{2}
\]

and

\[
W=W_y(S)
=\operatorname{span}_{\mathbb F_2}\{\lambda(p):p\le y\text{ prime}\}
\subseteq\mathbb F_2^S.
\tag{3}
\]

Here `lambda(a)` is the vector of Legendre-symbol bits modulo the shell primes, `K=W^perp`, and `kappa=dim K`. At first sight the all-powers smooth weight `Psi(T/m,y)` in `(1)` looks like an additional source-specific analytic object beyond the rough Möbius block isolated in `MC-180`--`MC-187`.

It is not. The weight disappears **exactly** under the same smooth inverse already identified in `MC-181`.

Let

\[
s_y(d)=\mathbf 1_{P^+(d)\le y},
\qquad
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y}.
\tag{4}
\]

Then `MC-181` proved coefficientwise

\[
\boxed{g_y=\mu*s_y.}
\tag{5}
\]

Because every prime dividing a `y`-smooth `d` is below every shell prime dividing `q`, one has `(d,q)=1`. Moreover `lambda` is additive on multiplication in `F_2^S`, and by definition

\[
\lambda(d)\in W
\qquad(P^+(d)\le y).
\tag{6}
\]

Therefore multiplication by a smooth `d` preserves the affine blind-cell condition:

\[
\boxed{
\lambda(-m)\in W
\iff
\lambda(-md)\in W.
}
\tag{7}
\]

Expanding `Psi(T/m,y)=sum_{d\le T/m}s_y(d)`, regrouping by `n=md`, and using `(5)` gives the exact identity

\[
\boxed{
B_S^{(K)}(X)
=
\frac{2^{\kappa}}{\varphi(q)}
\sum_{\substack{n\le T\\(n,q)=1\\\lambda(-n)\in W}}
g_y(n).
}
\tag{8}
\]

Thus the complete blind source term is not a new smooth-weighted Möbius statistic. It is precisely a logarithmically **rough Möbius partial sum restricted to one affine Legendre cell**, with the same rough coefficient system already studied in `MC-180`--`MC-187`.

This changes the live interpretation of `MC-244`. The unresolved ingredient is no longer “signed cancellation against the source-forced `Psi` weight.” The `Psi` weight is an exact convolution coordinate which can be removed without loss. The remaining source-specific problem is signed rough Möbius cancellation inside the quotient condition

\[
\lambda(n)+\lambda(-1)\in W.
\tag{9}
\]

The reduction also sharpens the absolute support bound. Put

\[
h:=\frac{\varphi(q)}{2^{\kappa}},
\tag{10}
\]

the number of reduced residue classes modulo `q` satisfying `lambda(-a) in W`. Then

\[
A(U)
:=
\#\{m\le U:(m,q)=1,\ \lambda(-m)\in W\}
=
\frac{h}{q}U+O(h).
\tag{11}
\]

Since the blind-cell condition is invariant under multiplication by every divisor of `P`, exact Eratosthenes--Legendre inclusion-exclusion gives

\[
\begin{aligned}
C_y(T)
&:=
\#\{n\le T:(n,q)=1,\ \lambda(-n)\in W,\ (n,P)=1\}\\
&=
\sum_{d\mid P}\mu(d)A(T/d)\\
&=
\frac{hT}{q}\frac{\varphi(P)}P
+O\!\left(h\,2^{\pi(y)}\right).
\end{aligned}
\tag{12}
\]

The support of `g_y` is contained in the set counted by `C_y(T)`, so `(8)` implies

\[
\boxed{
|B_S^{(K)}(X)|
\le
\frac{T}{q}\frac{\varphi(P)}P
+O\!\left(2^{\pi(y)}\right).
}
\tag{13}
\]

At `y=c log X`, Mertens' product theorem and the prime number theorem give

\[
\frac{\varphi(P)}P
\asymp\frac1{\log y},
\qquad
2^{\pi(y)}=X^{o(1)}.
\tag{14}
\]

Hence, under the active shell scaling

\[
q=X^{2\alpha+o(1)},
\tag{15}
\]

one has

\[
\boxed{
|B_S^{(K)}(X)|
\ll
\frac{X^{1-2\alpha+o(1)}}{\log\log X}
+X^{o(1)}.
}
\tag{16}
\]

This recovers the genuine logarithmic rough-density saving that the triangle bound in `MC-244` obscured, but it does **not** change the fixed-power boundary: support alone still reaches `X^{1/2+o(1)}` only once `alpha>=1/4`. The gain from `(13)` over the previous absolute estimate is logarithmic, not a new power of `X`.

There is also an exact modewise analytic description. For `v in K`, let

\[
\chi_v(n)=\prod_{r\in S}\left(\frac nr\right)^{v_r}
\tag{17}
\]

with the usual extension by zero away from the units modulo `q`. Since `v in K`,

\[
\chi_v(p)=1
\qquad(p\le y\text{ prime}).
\tag{18}
\]

For `Re(s)>1`, the twisted rough Dirichlet series is therefore

\[
\begin{aligned}
D_{y,v}(s)
&:=
\sum_{n\ge1}\frac{g_y(n)\chi_v(n)}{n^s}\\
&=
\prod_{p>y}\left(1-\frac{\chi_v(p)}{p^s}\right)\\
&=
\boxed{
\frac{1}{L(s,\chi_v)}
\prod_{p\le y}\left(1-p^{-s}\right)^{-1}
}.
\end{aligned}
\tag{19}
\]

The finite small-prime Euler correction in `(19)` is holomorphic and nonzero throughout `Re(s)>0`. Thus if one attacks the blind sector **character by character**, the roughing operation does not remove the reciprocal-Dirichlet-`L` obstruction; it only deletes finitely many small-prime Euler factors. This is an analytic explanation for why the smooth inverse can change representation without manufacturing a fixed power of cancellation.

However, `(8)` is an affine-cell aggregate, not an individual character estimate. Character orthogonality gives

\[
\frac{2^{\kappa}}{\varphi(q)}
\mathbf 1_{\lambda(-n)\in W}
=
\frac1{\varphi(q)}
\sum_{v\in K}\chi_v(-1)\chi_v(n),
\tag{20}
\]

so the corresponding Dirichlet series is

\[
\boxed{
\frac1{\varphi(q)}
\left(\prod_{p\le y}(1-p^{-s})^{-1}\right)
\sum_{v\in K}\frac{\chi_v(-1)}{L(s,\chi_v)}.
}
\tag{21}
\]

A bound for the **single source-selected affine cell** does not invert `(20)` and therefore does not, by itself, imply comparable bounds for every individual `chi_v`. Cross-character cancellation remains a logically distinct possible source mechanism. Conversely, any strategy that estimates each blind mode separately must confront `(19)` rather than expecting the smooth `Psi` weight to regularize it.

## 1. Exact convolution collapse

Starting from `(1)`, write

\[
\Psi(T/m,y)
=
\sum_{\substack{d\le T/m\\P^+(d)\le y}}1
=
\sum_{d\le T/m}s_y(d).
\tag{22}
\]

The unnormalized weighted sum in `(1)` becomes

\[
\sum_{\substack{md\le T\\(m,q)=1\\\lambda(-m)\in W}}
\mu(m)s_y(d).
\tag{23}
\]

Every shell prime lies in `(y,2y]`, so `(d,q)=1`. For units modulo `q`, the Legendre-bit map satisfies

\[
\lambda(ab)=\lambda(a)+\lambda(b)
\quad\text{in }\mathbb F_2^S.
\tag{24}
\]

Because `lambda(d) in W`, equation `(24)` proves `(7)`. Hence after setting `n=md`, condition `(23)` depends on `n` but not on the particular smooth divisor `d`:

\[
\sum_{\substack{n\le T\\(n,q)=1\\\lambda(-n)\in W}}
\sum_{\substack{d\mid n\\P^+(d)\le y}}
\mu(n/d).
\tag{25}
\]

The inner divisor sum is exactly `(mu*s_y)(n)=g_y(n)` by `MC-181`, which proves `(8)`. No approximation, contour shift, density theorem, or zero-free input occurs in this step.

A small finite sanity check is useful but not evidential: choosing `y=2`, shell primes `{3,5,7}`, and summing through `T=500` gives the same integer for the weighted form `(1)` and the rough form before the common projector normalization. The proof above is coefficientwise and does not depend on this check.

## 2. The source projector retains only one quotient charge

Let

\[
V=\mathbb F_2^S/W
\tag{26}
\]

and write `[lambda(n)]` for the quotient class. Equation `(9)` says that the source selects exactly one charge

\[
[\lambda(n)]=[\lambda(-1)]
\quad\text{in }V.
\tag{27}
\]

Every `y`-smooth multiplier has zero charge in `V`, so the whole smooth semigroup acts trivially on this quotient. This is the quotient-language version of `(7)` and explains why the all-powers smooth inverse cannot spread the source over different blind charges.

This also separates two questions that should not be conflated:

- the **dimension question** asks how large `V` or `K` is;
- the **source-amplitude question** asks how much signed rough Möbius mass lies in the one fixed charge `(27)`.

`MC-243`--`MC-244` already show that dimension information alone does not pay for amplitude. Equation `(8)` makes the missing source quantity explicit without the auxiliary `Psi` weight.

## 3. Exact rough support count inside the affine cell

The absolute bound `(13)` is elementary but useful because it corrects the apparent direction of the smooth weight in `MC-244`.

The eligible reduced residues form exactly `h=phi(q)/2^kappa` classes modulo `q`, hence `(11)`. To impose `(n,P)=1`, use

\[
\mathbf 1_{(n,P)=1}
=
\sum_{d\mid(n,P)}\mu(d).
\tag{28}
\]

For every `d|P`, multiplication by `d` is invertible modulo `q` and `lambda(d) in W`, so

\[
\#\{n\le T:d\mid n,(n,q)=1,\lambda(-n)\in W\}
=A(T/d).
\tag{29}
\]

Substituting `(11)` into the resulting inclusion-exclusion gives `(12)`, because

\[
\sum_{d\mid P}\frac{\mu(d)}d
=
\frac{\varphi(P)}P,
\qquad
\sum_{d\mid P}1=2^{\pi(y)}.
\tag{30}
\]

Since `|g_y(n)|` additionally imposes square-freeness, it is bounded by the rough eligibility indicator. Equations `(8)` and `(12)` therefore give `(13)`.

The argument can be refined further by pricing square-free support, but that can improve only lower-order density factors here; it does not change the fixed-power support boundary `alpha=1/4`. The important point is structural: the `Psi` harmonic mass from the smooth inverse is exactly cancelled when the convolution is regrouped before absolute values.

## 4. Prior-art and novelty audit

Every algebraic ingredient is classical. The identity `g_y=mu*s_y` is the logarithmically rough smooth-inverse identity already persisted in `MC-181`; finite-group character orthogonality is the mechanism already used in `MC-238`--`MC-244`; `(28)` is the elementary Eratosthenes--Legendre sieve identity; and `(19)` is the Euler-product factorization of a rough Möbius character twist.

The closest external analytic literatures also treat the components rather than establishing a new theorem for this exact Mathia source cell. Yazan Alamoudi's 2026 preprint *On subradically sifted sums related to Alladi's higher order duality between prime factors* (arXiv:2601.10636) studies unconditioned rough Möbius sums and supplies the modern source audit used in `MC-186`. Shōta Inoue, *Some explicit formulas for partial sums of Möbius functions*, J. Théorie des Nombres de Bordeaux 33 (2021), 273--315, DOI `10.5802/jtnb.1162`, studies Möbius sums in arithmetic progressions and the associated finite Euler products. A targeted search did not locate a theorem combining the moving logarithmic rough cutoff with the particular shell-square Legendre quotient `(27)` in a way that supplies the missing fixed-power cancellation.

No novelty is claimed for the convolution, sieve, character decomposition, or Euler products. The mathematical delta is the **source specialization**: the apparently new weighted projector left by `MC-244` is exactly the old rough-parity coefficient system restricted to one source-forced affine charge. This rules out treating `Psi(T/m,y)` itself as the unresolved mechanism and reconnects the newest blind-sector frontier to the established rough-Möbius barrier.

## 5. Boundaries and falsification tests

- Equation `(8)` uses the strict separation between smooth primes `p<=y` and shell primes `r in (y,2y]`. If the modulus shares a prime with the smooth semigroup, `(d,q)=1` and the invariant regrouping require modification.
- The affine invariance uses only `lambda(d) in W`. It is exact for the quadratic blind quotient defined in `MC-244`; it does not automatically describe higher-order characters outside that quadratic quotient.
- The absolute bound `(13)` deliberately drops square-freeness and Möbius sign. It is an upper bound, not an asymptotic for the signed source term.
- The logarithmic density improvement in `(16)` does not cross the fixed-power boundary. Any claim that `(8)` solves the `alpha<1/4` range by support alone is false.
- Equation `(19)` is stated first in `Re(s)>1`, where Euler products converge absolutely. Analytic continuation beyond that region may be discussed only through legitimate `L`-function theory; the identity is not a license to assume a zero-free half-plane.
- The live family has `y`, `q`, and the characters themselves moving with `X`. A one-scale bound for `(8)` is **not automatically equivalent** to a fixed-character zero-free theorem. The reciprocal-`L` description is a modewise structural boundary, not an RH/GRH implication claimed here.
- A single affine-cell estimate does not recover every blind character by Fourier inversion. Cross-character cancellation in `(20)` is therefore not ruled out.
- No `X^{1/2+o(1)}` bound for `B_S^{(K)}`, no fixed-power cancellation for the rough affine cell, no elimination of the blind sector, no Mertens power bound, and no consequence for the zeta zero set is proved here.

## Consequence for the live frontier

The newest blind-sector route now lands on a cleaner object:

\[
\boxed{
\text{rough Möbius sign}
\quad+\quad
\text{one affine Legendre quotient charge}.
}
\]

The all-powers smooth weight in `MC-244` is representation, not an additional analytic obstruction. Absolute support gives only `(16)`, so the same `alpha=1/4` power boundary remains. Mode-by-mode analysis reduces to reciprocal Dirichlet `L`-functions with a finite small-prime correction, while the source aggregate still permits the logically distinct possibility of cancellation between blind modes.

A substantive next theorem must therefore do one of two things: prove source-specific signed cancellation for the rough affine cell `(8)`, or exploit cross-character coupling in `(20)` strongly enough to beat the dimension-free support bound. Further manipulation of the smooth `Psi` weight alone cannot provide a new fixed-power gain.