# ANF-102 — twist-averaged diagonal barrier forces resonant bow cancellation

**Status:** `EXACT-DERIVED + CLASSICAL-MEAN-VALUE-BOUNDARY + PRIME-SECOND-MOMENT-BARRIER + BOW-VARIANCE-NO-GO + CLUE-NARROWING`. The proposed bow variance target from `CLUE-bow-multiplicative-gallagher-variance` cannot hold uniformly over the Archimedean regime `U asymp X^2`. For the exact Matomäki--Radziwiłł--Shao--Tao--Teräväinen prime approximant, averaging the moving short-interval square over any fixed multiplicative-scale `U` window of length `asymp X^2` diagonalizes the twist strongly enough that the prime second moment survives at full size. In the bow range `K=X^{1-2 epsilon+o(1)}`, `0<epsilon<1/4`, the averaged variance is `(1+o(1)) X K log X`. Hence at least one `U asymp X^2` has diagonal-scale variance, so no estimate `o(XK log X)` can be uniform in that regime. Any successful bow theorem at a distinguished twist must instead force a macroscopic **negative off-diagonal correlation** that cancels the prime diagonal at that special `U`.

Let

\[
R:=\exp((\log X)^{1/10}),\qquad
P(R):=\prod_{p<R}p,\qquad
c_R:=\frac{P(R)}{\varphi(P(R))},
\tag{1}
\]

and use the approximant from Matomäki--Radziwiłł--Shao--Tao--Teräväinen,

\[
\Lambda^\sharp(n)=c_R\,1_{(n,P(R))=1},
\qquad
a_X(n):=\Lambda(n)-\Lambda^\sharp(n).
\tag{2}
\]

For `1<=K<=X/4` and real `U`, define the moving twisted variance

\[
V_X(U;K)
:=
\int_X^{2X}
\left|
\sum_{x<n\le x+K}a_X(n)n^{-iU}
\right|^2dx.
\tag{3}
\]

Fix constants `0<A<B`. If

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\tag{4}
\]

then

\[
\boxed{
\frac{1}{(B-A)X^2}
\int_{AX^2}^{BX^2}V_X(U;K)\,dU
=(1+o(1))XK\log X.
}
\tag{5}
\]

In particular,

\[
\boxed{
\sup_{AX^2\le U\le BX^2}V_X(U;K)
\ge (1-o(1))XK\log X.
}
\tag{6}
\]

Thus the uniform target

\[
V_X(U;K)=o(XK\log X)
\quad\text{uniformly for }U\asymp X^2
\tag{7}
\]

is false as stated.

## 1. Exact overlap expansion separates the diagonal

Opening (3) gives

\[
V_X(U;K)
=
\sum_{m,n}a_X(m)a_X(n)
\left(\frac{n}{m}\right)^{-iU}
\omega_K(m,n),
\tag{8}
\]

where

\[
\omega_K(m,n)
:=
\operatorname{meas}\{x\in[X,2X]:x<m,n\le x+K\}.
\tag{9}
\]

The overlap is nonnegative, is supported on `m,n in (X,2X+K]` and `|m-n|<K`, and satisfies

\[
0\le\omega_K(m,n)\le K.
\tag{10}
\]

On the diagonal, every `n in (X+K,2X]` has the full weight

\[
\omega_K(n,n)=K.
\tag{11}
\]

Write

\[
D_X(K):=\sum_n |a_X(n)|^2\omega_K(n,n).
\tag{12}
\]

The issue is therefore whether the off-diagonal part can cancel this positive contribution uniformly in `U`.

## 2. Averaging a length-X-squared twist window kills the off-diagonal on average

Let `I=[U_0,U_0+L]`. For `m\ne n`, direct integration gives

\[
\left|
\frac1L\int_I
\left(\frac{n}{m}\right)^{-iU}dU
\right|
\le
\min\left\{1,\frac{2}{L|\log(n/m)|}\right\}.
\tag{13}
\]

On the support of (8), `m,n asymp X`. If `h=|n-m|>=1`, then

\[
|\log(n/m)|\gg \frac{h}{X},
\tag{14}
\]

so for the windows used below

\[
\left|
\frac1L\int_I
\left(\frac{n}{m}\right)^{-iU}dU
\right|
\ll \frac{X}{Lh}.
\tag{15}
\]

Put

\[
S_2(X,K):=\sum_{X<n\le2X+K}|a_X(n)|^2.
\tag{16}
\]

Cauchy--Schwarz gives, uniformly in `1<=h<K`,

\[
\sum_m|a_X(m)a_X(m+h)|\le S_2(X,K).
\tag{17}
\]

Using (10), (15), and (17) in the opened off-diagonal yields the general estimate

\[
\boxed{
\frac1L\int_I V_X(U;K)dU
=
D_X(K)
+O\left(
\frac{KX}{L}S_2(X,K)\log(2K)
\right).
}
\tag{18}
\]

This is the line-specific form of the classical Dirichlet-polynomial mean-value phenomenon. No prime-pair cancellation, large-value theorem, or zero-density input is used: averaging in the logarithmic twist already suppresses the off-diagonal kernel.

For `L=(B-A)X^2`, (18) becomes

\[
\frac1L\int_I V_X(U;K)dU
=
D_X(K)
+O\left(
\frac{K}{X}S_2(X,K)\log(2K)
\right).
\tag{19}
\]

## 3. The MRSTT residual has a full prime diagonal

Classical prime-number-theorem estimates give

\[
\sum_{X+K<n\le2X}\Lambda(n)^2
=(1+o(1))X\log X
\tag{20}
\]

throughout (4): removing the initial interval of length `K=o(X/log X)` costs only `O(K log^2 X)=o(X log X)`. Also the classical Mertens product bound gives

\[
c_R\ll\log R\ll(\log X)^{1/10}.
\tag{21}
\]

Consequently the model square and cross term are lower order:

\[
\sum_{X+K<n\le2X}(\Lambda^\sharp(n))^2
\le Xc_R^2
=o(X\log X),
\tag{22}
\]

and

\[
\sum_{X+K<n\le2X}\Lambda(n)\Lambda^\sharp(n)
\le c_R\sum_{X<n\le2X}\Lambda(n)
=o(X\log X).
\tag{23}
\]

Thus

\[
\boxed{
\sum_{X+K<n\le2X}|a_X(n)|^2
=(1+o(1))X\log X.
}
\tag{24}
\]

The same elementary estimates give

\[
S_2(X,K)\ll X\log X.
\tag{25}
\]

By (11), (24), and the fact that the two diagonal edge strips contain only `O(K)` integers with `|a_X(n)|\ll\log X`, one gets

\[
\boxed{D_X(K)=(1+o(1))XK\log X.}
\tag{26}
\]

Substituting (25)--(26) into (19), and using `log K=O(log X)`, gives

\[
\frac1L\int_I V_X(U;K)dU
=(1+o(1))XK\log X
+O(K\log X\log K).
\tag{27}
\]

The error in (27) is smaller than the main term by `O(log K/X)`, proving (5) and therefore (6).

## 4. What a special bow twist would now have to do

Equation (5) does not say that every `U asymp X^2` has diagonal-scale variance. It says something more useful for the proposed uniform route: **most importantly, the diagonal cannot be uniformly erased across the whole regime**. If a distinguished bow trajectory `U=U(X)` nevertheless satisfied

\[
V_X(U(X);K)=o(XK\log X),
\tag{28}
\]

then its off-diagonal contribution in (8) would necessarily obey

\[
\boxed{
2\operatorname{Re}
\sum_{\substack{m<n\\n-m<K}}
 a_X(m)a_X(n)
\left(\frac{n}{m}\right)^{-iU(X)}
\omega_K(m,n)
=-(1+o(1))XK\log X.
}
\tag{29}
\]

So the remaining source problem is not a generic variance saving. It is a **resonant sign problem**: the exact bow twist must create negative correlation of the same macroscopic size as the prime diagonal. Any proof architecture whose estimates take absolute values before exposing this sign cannot reach (28).

The obstruction is stable under fixed smooth bulk weights. If `w` is bounded and `|w(y)|>=c>0` on a fixed subinterval of `(1,2)`, replacing `a_X(n)` by `w(n/X)a_X(n)` leaves a positive `asymp XK log X` diagonal and the same twist-averaging estimate. A weighted bow normalization that vanishes or rescales the bulk may change the target and must be checked separately; (5) is a no-go for the unweighted target written in the clue and for ordinary nondegenerate smoothings of it.

## 5. Relation to the current almost-all major-arc theorem

The 2026 Matomäki--Radziwiłł--Shao--Tao--Teräväinen theorem is substantially stronger than a fixed-phase result in its quantifiers: for `H>=X^{1/3+delta}` it gives, outside a logarithmically small exceptional set, a maximal bound

\[
\left|
\sum_{x<n\le x+H}(\Lambda(n)-\Lambda^\sharp(n))n^{-iT}
\right|^*
\ll H\log^{-A}X
\tag{30}
\]

uniformly for polynomial-size `T`. The bow length (4) lies safely inside that interval range. But squaring (30) and integrating gives at best `XH^2 log^{-2A}X` on the good set, while the target is `XH log X`; for every fixed `A`, the polynomial factor `H` dominates the logarithmic saving. The exceptional set is likewise too large under trivial amplitude control.

That mismatch is therefore not merely a weakness of the published theorem. Equation (5) shows that a uniform diagonal-scale improvement of the exact form proposed in the clue is mathematically impossible. The almost-all result can still be relevant to a **specific** bow twist or to a differently normalized weighted form, but it cannot be upgraded to the false uniform statement by a sharper bookkeeping of the same target.

## 6. Prior-art boundary, adversarial audit, and research consequence

The external inputs have now been pinned precisely. Matomäki--Radziwiłł--Shao--Tao--Teräväinen supply the definition (2), their almost-all major-arc theorem, and a Parseval-type variance framework. Montgomery--Vaughan's Hilbert inequality is the classical neighboring mechanism behind diagonal/off-diagonal control in Dirichlet-polynomial mean values. The proof of (18) is nevertheless self-contained: it is just exact averaging of `exp(-iU log(n/m))`, the overlap identity, and Cauchy--Schwarz. The line-specific content is the specialization to the MRSTT residual and the resulting impossibility of the proposed **uniform bow** norm.

The main adversarial boundaries are explicit. Isolated or thin resonant sets of `U` are not ruled out by a twist average; indeed they are exactly where (29) could live. The argument does not inspect the cross-line bow identity and therefore does not assert that its actual `U(X)` is generic. It also does not prove that current arithmetic technology cannot establish (29) at that distinguished twist; it proves only that any successful proof must preserve and control the negative off-diagonal sign instead of seeking a uniform small variance.

Accordingly `CLUE-bow-multiplicative-gallagher-variance` is resolved as **narrowed**. The uniform target in its decisive test is false. A viable continuation must specify the exact bow twist and smooth normalization and then prove the resonant cancellation (29), or reformulate the transferred quantity so that the unavoidable diagonal is explicitly removed before asking for an `o(1)` gain.