# MC-023 — The renormalized Huxley–Watt endpoint forms an infinite analytic jet hierarchy

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `NO-NOVELTY-CLAIM`.

## Claim

The analytic family suggested by the `g(n)=1/n` endpoint in `MC-021` can be derived exactly by specializing the Huxley–Watt scale-doubling identity to

\[
g_t(n)=n^{-1-t}.
\]

After centering at the reciprocal-zeta germ and applying one scale normalization, the entire family collapses to a compact exact recursion with no explicit `log N` terms. However, differentiating that recursion at `t=0` does **not** produce a finite closed system for the centered coefficients. The `k`-th differentiated equation necessarily introduces the `(k+1)`-st centered jet, together with the `k`-th derivative of the residual kernel. Thus finite differentiation alone generates an infinite triangular hierarchy rather than the finite multiscale closure proposed as a possible continuation in `MC-021`.

For `t` in a sufficiently small complex neighborhood of `0`, define

\[
F_N(t)=\sum_{n\le N}\frac{\mu(n)}{n^{1+t}},
\qquad
f(t)=\frac1{\zeta(1+t)},
\tag{1}
\]

where `f(0)=0` is the removable value at the simple pole of zeta. Set

\[
E_N(t)=F_N(t)-f(t),
\qquad
A_N(t)=N^tE_N(t).
\tag{2}
\]

Then

\[
A_N(0)=H(N):=\sum_{n\le N}\frac{\mu(n)}n.
\tag{3}
\]

For `y>=1`, write `q=floor(y)` and define the centered analytic kernel

\[
\kappa_t(y)
=
y^{1+t}\left(
\sum_{k\le q}k^{-1-t}
-\zeta(1+t)
+\frac{y^{-t}}t
\right),
\tag{4}
\]

with the removable value at `t=0`. Since

\[
\zeta(1+t)=\frac1t+\gamma+O(t),
\qquad
\frac{y^{-t}}t=\frac1t-\log y+O(t),
\]

one recovers exactly

\[
\kappa_0(y)
=y\bigl(H_{\lfloor y\rfloor}^{(1)}-\log y-\gamma\bigr),
\tag{5}
\]

the bounded harmonic endpoint kernel of `MC-021`. Define

\[
B_N(t)
=
\sum_{m,n\le N}
\mu(m)\mu(n)
\kappa_t\!\left(\frac{N^2}{mn}\right).
\tag{6}
\]

For every fixed `N`, this is holomorphic near `t=0`.

The exact renormalized scale-doubling identity is

\[
\boxed{
A_{N^2}(t)
=
\frac{H(N)^2}{t}
-
\frac{A_N(t)^2}{f(t)}
-
\frac{B_N(t)}{N^2}.
}
\tag{7}
\]

The first two terms in (7) have cancelling apparent poles at `t=0`, so their difference extends holomorphically there. Equation (7) therefore holds as an identity of holomorphic germs at `t=0`.

Now let

\[
a_j(N)=A_N^{(j)}(0),
\qquad
b_j(N)=B_N^{(j)}(0).
\tag{8}
\]

For every `k>=0`, differentiating (7) `k` times at `0` gives a triangular relation of the form

\[
\boxed{
a_k(N^2)
=
-\frac{2H(N)}{k+1}\,a_{k+1}(N)
+P_k\bigl(H(N),a_1(N),\ldots,a_k(N)\bigr)
-\frac{b_k(N)}{N^2},
}
\tag{9}
\]

where `P_k` is a universal polynomial determined by the Taylor coefficients of `1/f(t)=\zeta(1+t)` after its pole is separated. Crucially, `P_k` involves no `a_{k+1}`. Except at the special scale where `H(N)=0`, the highest new jet appears with the nonzero coefficient `-2H(N)/(k+1)`.

Consequently, for any fixed `K`, the equations of orders `0,...,K` do not close on the finite state

\[
(a_0(N),a_1(N),\ldots,a_K(N))
\]

without an additional arithmetic relation that controls or eliminates `a_{K+1}(N)`; simultaneously, each order introduces the new residual observable `b_k(N)`. The failure is algebraic and exact for this differentiated Huxley–Watt scheme. It does **not** prove that no other finite auxiliary identity could close the endpoint family.

The natural surviving formulation is therefore the full analytic germ `A_N(t)` together with the residual family `B_N(t)`, rather than any finite Taylor truncation.

## 1. Exact analytic specialization of the Huxley–Watt identity

Huxley and Watt prove, for an arbitrary totally multiplicative `g`, the square-scale identity

\[
M(g,N^2)=2M(g,N)-\mathbf m_g^{\rm T}A_g\mathbf m_g,
\tag{10}
\]

where

\[
M(g,X)=\sum_{n\le X}\mu(n)g(n),
\qquad
(\mathbf m_g)_n=\mu(n)g(n),
\]

and

\[
(A_g)_{mn}
=
\sum_{k\le N^2/(mn)}g(k).
\tag{11}
\]

Taking `g=g_t` gives `M(g_t,X)=F_X(t)`. For

\[
y=\frac{N^2}{mn},
\qquad q=\lfloor y\rfloor,
\]

the definition (4) is exactly equivalent to

\[
\sum_{k\le q}k^{-1-t}
=
\zeta(1+t)
-
\frac{y^{-t}}t
+
y^{-1-t}\kappa_t(y).
\tag{12}
\]

Substitution into the quadratic form in (10) separates three exact pieces. The zeta term gives

\[
\zeta(1+t)F_N(t)^2.
\tag{13}
\]

For the pole-cancelling term, the powers of `mn` simplify:

\[
\sum_{m,n\le N}
\frac{\mu(m)\mu(n)}{(mn)^{1+t}}
\frac{y^{-t}}t
=
\frac{N^{-2t}}tH(N)^2.
\tag{14}
\]

Finally,

\[
\sum_{m,n\le N}
\frac{\mu(m)\mu(n)}{(mn)^{1+t}}
y^{-1-t}\kappa_t(y)
=
N^{-2(1+t)}B_N(t).
\tag{15}
\]

Thus (10) becomes

\[
F_{N^2}(t)
=
2F_N(t)
-\zeta(1+t)F_N(t)^2
+rac{N^{-2t}}tH(N)^2
-N^{-2(1+t)}B_N(t).
\tag{16}
\]

No asymptotic expansion and no continuation toward the critical line is used here. The only analytic centering is local at the classical pole `s=1`.

## 2. Reciprocal-zeta centering removes the linear state

Write `F_N=f+E_N`. Since `f=1/zeta(1+t)`, on a punctured neighborhood of `t=0` one has the exact cancellation

\[
2F_N-\zeta(1+t)F_N^2-f
=-\frac{E_N^2}{f}.
\tag{17}
\]

Subtracting `f(t)` from (16) therefore gives

\[
E_{N^2}(t)
=
-\frac{E_N(t)^2}{f(t)}
+rac{N^{-2t}}tH(N)^2
-N^{-2(1+t)}B_N(t).
\tag{18}
\]

Multiplying by `N^{2t}` and using `A_N=N^tE_N` yields (7):

\[
A_{N^2}(t)
=
\frac{H(N)^2}{t}
-rac{A_N(t)^2}{f(t)}
-rac{B_N(t)}{N^2}.
\]

This normalization is structurally useful. The explicit `log N` terms seen after differentiating unnormalized weighted sums are absorbed into the state `A_N`; the scale transfer itself is represented by one universal nonlinear germ plus the normalized residual family.

The cancellation at `t=0` is unconditional. Since zeta has a simple pole of residue `1` at `1`,

\[
f(t)=t+O(t^2),
\tag{19}
\]

while `A_N(t)=H(N)+O(t)`. Hence

\[
\frac{H(N)^2}{t}-\frac{A_N(t)^2}{f(t)}
\]

has a removable singularity. No zero-free half-plane equivalent to RH has been imported; only a sufficiently small neighborhood of the pole is used.

## 3. Finite differentiation is triangular, not closed

Expand

\[
A_N(t)
=
H(N)+\sum_{j\ge1}\frac{a_j(N)}{j!}t^j
\tag{20}
\]

and

\[
\frac1{f(t)}
=
\zeta(1+t)
=
\frac1t+c_0+c_1t+c_2t^2+\cdots,
\qquad c_0=\gamma.
\tag{21}
\]

The pole term `H(N)^2/t` in (7) cancels the coefficient `H(N)^2/t` coming from `A_N(t)^2/f(t)`. To identify the highest jet entering the `k`-th regular coefficient, note that the coefficient of `t^{k+1}` in `A_N(t)^2` contains

\[
\frac{2H(N)a_{k+1}(N)}{(k+1)!}
\tag{22}
\]

and all its other terms involve only `a_1,...,a_k`. Multiplication by the `1/t` term in (21) is the **only** way for `a_{k+1}` to enter the coefficient of `t^k`; all regular terms `c_jt^j` multiply coefficients of `A_N^2` of order at most `k`.

Multiplying the `t^k` coefficient by `k!` therefore gives the contribution

\[
-\frac{2H(N)}{k+1}a_{k+1}(N),
\]

which proves (9). The same differentiation contributes `-b_k(N)/N^2` from the residual family.

This is the exact obstruction to the finite-derivative closure proposed in `MC-021`. At every finite cutoff there is one more centered derivative above the cutoff, plus one more kernel derivative. Merely differentiating again moves the boundary upward rather than eliminating it.

The conclusion should not be overstated. Equation (9) does not prove that the jets are algebraically independent, nor that no number-theoretic identity can relate them. It proves that **the Huxley–Watt analytic family by itself supplies a triangular hierarchy, not such a closing relation**.

## 4. Zeroth order recovers the harmonic endpoint exactly

The first centered derivative has a concrete interpretation. From (1)–(2),

\[
F_N'(0)
=-\sum_{n\le N}\frac{\mu(n)\log n}{n}
=-J(N),
\qquad
f'(0)=1,
\]

so

\[
a_1(N)
=A_N'(0)
=(\log N)H(N)-(1+J(N)).
\tag{23}
\]

Taking `k=0` in (9), or simply taking the removable value of (7), gives

\[
H(N^2)
=-2H(N)a_1(N)-\gamma H(N)^2-rac{B_N(0)}{N^2}.
\tag{24}
\]

Substituting (23) yields

\[
H(N^2)
=
2H(N)(1+J(N))
-(2\log N+\gamma)H(N)^2
-rac{B_N(0)}{N^2},
\tag{25}
\]

which is exactly the `MC-021` endpoint identity with `B_N(0)=B(N)`. Thus the analytic recursion is not a new wrapper disconnected from the existing line: its zeroth-order boundary is the previously audited harmonic mechanism, and its first missing state is precisely the centered coefficient that appeared there.

Higher derivatives package reciprocal-logarithmic Möbius moments together with the scale normalization. Under RH their expected fixed-order critical sizes are compatible with the same `N^{-1/2+epsilon}` boundary after logarithms are absorbed into epsilon, but no such estimate is assumed or derived here.

## 5. Prior art and novelty boundary

The parent identity is prior art: M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. Their theorem allows an arbitrary totally multiplicative `g`, so choosing `g_t(n)=n^{-1-t}` is an immediate specialization of their framework, not a Mathia discovery. The paper's detailed matrix and spectral sections then specialize to `g=1`.

The Laurent expansion of zeta at `1`, the reciprocal-zeta germ, finite differentiation, and generalized harmonic sums are classical. `MC-021` already derived the `t=0` harmonic endpoint; `MC-020` and `MC-022` audit neighboring coarse-mode obstructions.

A targeted search for the Huxley–Watt identity together with `g(n)=n^{-s}`, weighted Möbius sums, generalized harmonic kernels, and differentiated scale-doubling systems located the general 2018 identity and the later unweighted sawtooth-kernel program, but no authoritative source explicitly presenting the normalized recursion (7) or the triangular finite-jet audit (9). Absence from that search is **not** evidence of novelty, so no novelty claim is made for either formula.

The durable contribution is the exact mechanism audit within the active Mathia route: the obvious analytic-family continuation of `MC-021` can be written cleanly, and its finite Taylor hierarchy demonstrably fails to close by differentiation alone.

## 6. Boundaries and decisive continuation

This finding kills only one specific continuation: constructing a finite system by differentiating the `g_t=n^{-1-t}` Huxley–Watt identity a fixed number of times and expecting the resulting weighted Möbius moments to close among themselves.

It does **not** kill the full harmonic endpoint or the analytic family. Equation (7) points to two materially different surviving possibilities:

- control the complete analytic state `A_N(t)` on a fixed neighborhood of `t=0` in a norm strong enough that the nonlinear quotient and residual family propagate with a strict gain; or
- derive an independent arithmetic identity, inequality, or finite certificate that eliminates the top jet and residual observable at some finite order.

Either route must be audited for the same circularity that affected earlier coarse modes. A proposed functional norm fails if its critical bound is merely equivalent to zero-freeness after Mellin/Dirichlet continuation, and a finite closure fails if the auxiliary relation simply assumes the next RH-scale weighted moment. Likewise, derivatives `b_k(N)` of the residual kernel must be controlled with their actual logarithmic/product structure rather than declared harmless from the boundedness of `kappa_0`.

A decisive next test is therefore functional rather than merely differential: determine whether (7) admits any source-natural analytic norm or contraction whose hypotheses follow from independently weaker arithmetic information. A negative result showing that every natural candidate norm already contains an RH-equivalent boundary datum would close this endpoint more sharply; a positive result would have to exhibit a genuine quantitative gain while preserving the coupled Möbius signs.