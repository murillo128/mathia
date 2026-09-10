# MC-195 — The canonical cubic transverse Möbius triad is Mertens-complete

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-190`--`MC-194` show that for the logarithmic-primorial residue representation, unit-equivariant linear and Hermitian-quadratic operations cannot transfer cancellation from nonprincipal character sectors into the hard rough principal mode. `MC-194` therefore leaves genuinely nonlinear source-forced coupling as one possible escape category.

There is a canonical nonlinear coupling already forced by the Möbius source itself: pointwise,

\[
\mu(n)^3=\mu(n).
\tag{1}
\]

After a finite additive Fourier transform, `(1)` creates a cubic interaction among nonzero frequencies whose total is exactly tied to the Mertens mean. Thus **nonlinearity really can couple transverse Fourier modes back to a principal quantity**; the quadratic representation-theoretic no-go does not extend mechanically to cubic statistics.

However, the canonical cubic coupling gives no exponent gain. Let

\[
M(N)=\sum_{n\le N}\mu(n),
\qquad
Q(N)=\sum_{n\le N}\mu(n)^2,
\tag{2}
\]

and put

\[
m_N:=\frac{M(N)}N,
\qquad
s_N:=\frac{Q(N)}N.
\tag{3}
\]

Regard the first `N` Möbius values as a function `f_N` on the cyclic group `Z/NZ`, using the complete representatives `1,...,N`, and use normalized Fourier coefficients

\[
\widehat f_N(h)
:=
\frac1N\sum_{n=1}^N
\mu(n)e\!\left(-\frac{hn}{N}\right),
\qquad h\in\mathbb Z/N\mathbb Z.
\tag{4}
\]

Then `\widehat f_N(0)=m_N`. Define the purely nonzero-frequency cubic triad

\[
T_N
:=
\sum_{\substack{h_1+h_2+h_3\equiv0\pmod N\\
h_1,h_2,h_3\ne0}}
\widehat f_N(h_1)
\widehat f_N(h_2)
\widehat f_N(h_3).
\tag{5}
\]

The exact identity is

\[
\boxed{
T_N
=
m_N\bigl(1-3s_N+2m_N^2\bigr).
}
\tag{6}
\]

Since `s_N -> 6/pi^2` and `|m_N|<=s_N`, the factor in parentheses is bounded away from zero and infinity in absolute value for all sufficiently large `N`. More precisely, whenever `1/2<s_N<1`,

\[
\boxed{
(1-s_N)(2s_N-1)|m_N|
\le |T_N|
\le (3s_N-1)|m_N|.
}
\tag{7}
\]

Consequently

\[
\boxed{|T_N|\asymp |M(N)|/N}
\qquad(N\to\infty),
\tag{8}
\]

with absolute constants after a fixed finite threshold. In particular, for every fixed `epsilon>0`,

\[
M(N)=O_\varepsilon(N^{1/2+\varepsilon})
\quad\Longleftrightarrow\quad
T_N=O_\varepsilon(N^{-1/2+\varepsilon}).
\tag{9}
\]

So the first canonical source-forced cubic escape is **Mertens-complete rather than Mertens-improving**. It moves the hard mean into a nonlinear transverse Fourier interaction but does not make the required estimate cheaper.

There is a broader algebraic obstruction behind `(6)`. Because `mu` takes only the three values `-1,0,1`, every pointwise scalar function of `mu` is exactly a quadratic polynomial in `mu`. For arbitrary values `Phi(-1),Phi(0),Phi(1)`, there are unique constants `a,b,c` such that

\[
\boxed{
\Phi(\mu(n))=a+b\mu(n)+c\mu(n)^2
}
\tag{10}
\]

for every `n`. Explicitly,

\[
a=\Phi(0),
\qquad
b=\frac{\Phi(1)-\Phi(-1)}2,
\qquad
c=\frac{\Phi(1)+\Phi(-1)}2-\Phi(0).
\tag{11}
\]

Thus **no pointwise scalar nonlinearity of the raw Möbius value introduces an arithmetic degree of freedom beyond background mass, squarefree support, and Möbius orientation**. Odd powers reduce to `mu`; positive even powers reduce to `mu^2`. To escape this obstruction, a nonlinear route must use relations between distinct arithmetic sites, scales, divisor factorizations, residue aggregates, or another source structure not contained in the one-site ternary algebra.

This result does not close the full nonlinear escape left by `MC-194`, because the primorial residue vector `A_q(X;a)` is an aggregate and is not pointwise ternary. It closes only the natural subclass in which one returns to the raw Möbius sequence and hopes that a pointwise nonlinear transform, followed by Fourier mixing, creates an independently estimable principal carrier.

## 1. Centering removes every zero-frequency factor

Let

\[
g_N(n):=\mu(n)-m_N.
\tag{12}
\]

Its normalized Fourier coefficients satisfy

\[
\widehat g_N(0)=0,
\qquad
\widehat g_N(h)=\widehat f_N(h)
\quad(h\ne0).
\tag{13}
\]

Finite Fourier convolution on `Z/NZ` therefore gives

\[
\frac1N\sum_{n=1}^N g_N(n)^3
=
\sum_{h_1+h_2+h_3\equiv0}
\widehat g_N(h_1)
\widehat g_N(h_2)
\widehat g_N(h_3).
\tag{14}
\]

Every summand containing a zero frequency vanishes by `(13)`. Hence the right-hand side of `(14)` is exactly the transverse triad `(5)`:

\[
\boxed{
T_N=\frac1N\sum_{n=1}^N(\mu(n)-m_N)^3.
}
\tag{15}
\]

The statistic `(5)` can therefore be computed using only nonzero Fourier coefficients even though its source identity will recover the mean.

## 2. The ternary Möbius algebra forces the exact triad identity

Expand `(15)` and use

\[
\mu(n)^3=\mu(n),
\qquad
\frac1N\sum_{n\le N}\mu(n)=m_N,
\qquad
\frac1N\sum_{n\le N}\mu(n)^2=s_N.
\tag{16}
\]

Then

\[
\begin{aligned}
T_N
&=
\frac1N\sum_{n\le N}
\left(\mu(n)^3-3m_N\mu(n)^2+3m_N^2\mu(n)-m_N^3\right)\\
&=m_N-3m_Ns_N+3m_N^3-m_N^3\\
&=m_N(1-3s_N+2m_N^2),
\end{aligned}
\tag{17}
\]

which proves `(6)`.

This is the exact nonlinear source relation missing from a purely representation-theoretic quadratic analysis: the cubic convolution of nonzero additive modes lands in the mean because the source values satisfy a nontrivial polynomial identity.

But the same polynomial identity also explains why no new information has appeared. The quotient algebra

\[
\mathbb C[x]/(x^3-x)
\tag{18}
\]

has representatives of degree at most two. Evaluating at `x=mu(n)` therefore reduces every pointwise polynomial statistic to the span of

\[
1,\qquad \mu(n),\qquad \mu(n)^2.
\tag{19}
\]

The interpolation formula `(10)`--`(11)` extends that statement from polynomials to every scalar function on the three-point range of `mu`.

## 3. The cubic coefficient cannot mask the Mertens scale

Because `|mu|=mu^2`,

\[
|m_N|
=
\frac{|M(N)|}{N}
\le
\frac1N\sum_{n\le N}|\mu(n)|
=s_N.
\tag{20}
\]

Write

\[
D_N:=1-3s_N+2m_N^2.
\tag{21}
\]

If `1/2<s_N<1`, then `(20)` gives

\[
D_N
\le
1-3s_N+2s_N^2
=-(1-s_N)(2s_N-1)<0.
\tag{22}
\]

Also `m_N^2>=0`, so

\[
D_N\ge1-3s_N.
\tag{23}
\]

Combining `(22)`--`(23)` yields

\[
(1-s_N)(2s_N-1)
\le |D_N|
\le 3s_N-1,
\tag{24}
\]

which proves `(7)`.

For completeness, the needed squarefree density is elementary. The classical identity

\[
\mu(n)^2=\sum_{d^2\mid n}\mu(d)
\tag{25}
\]

gives

\[
\begin{aligned}
Q(N)
&=\sum_{d\le\sqrt N}\mu(d)\left\lfloor\frac{N}{d^2}\right\rfloor\\
&=N\sum_{d\le\sqrt N}\frac{\mu(d)}{d^2}+O(\sqrt N)\\
&=\frac{N}{\zeta(2)}+O(\sqrt N)
=\frac6{\pi^2}N+O(\sqrt N).
\end{aligned}
\tag{26}
\]

The last tail estimate uses absolute convergence of `sum d^{-2}`. This is the standard squarefree-counting argument already represented by `MC-S12` in `SOURCES.md`.

Hence

\[
s_N\longrightarrow\frac6{\pi^2}\in(1/2,1),
\tag{27}
\]

so both sides of `(24)` are bounded by positive absolute constants for all sufficiently large `N`. Equations `(6)` and `(24)` then imply `(8)` and `(9)`.

## 4. What nonlinear information remains genuinely open

The result separates two statements that should not be conflated.

First, **nonlinear transverse-to-principal coupling exists**. The statistic `T_N` contains no zero Fourier mode in its definition, yet `(6)` reconstructs a quantity of exactly the Mertens scale. So the multiplicity-free/Schur-type obstructions of `MC-190`--`MC-194` are genuinely bounded by their linear/quadratic hypotheses; they cannot simply be asserted for all nonlinear statistics.

Second, **one-site nonlinearity is insufficient**. The same ternary identity that creates the coupling forces it to remain algebraically equivalent to the original mean after the already-controlled squarefree density is inserted. Higher pointwise powers do not help:

\[
\mu^{2k+1}=\mu\quad(k\ge0),
\qquad
\mu^{2k}=\mu^2\quad(k\ge1).
\tag{28}
\]

A genuinely different nonlinear carrier must therefore introduce additional arithmetic relations. Natural classes not ruled out here include shifted products such as `mu(n)mu(n+h)`, divisor-factor interactions, cross-scale products, nonlinear functions of residue-class aggregates, and boundary-weighted interactions whose coefficients are forced by the cutoff rather than chosen to encode `M(N)`.

For any such candidate, the decisive question is quantitative: does an independently proved estimate for the nonlinear carrier transfer to `M` with a strict power gain after all reconstruction, exceptional-set, smoothing, and scale losses are restored? Equation `(6)` is a control showing what failure looks like when the nonlinear carrier is merely an algebraic re-encoding of one-site Möbius orientation.

## 5. Prior art and novelty audit

All ingredients used in the proof are classical: the three-valued definition of the Möbius function, the squarefree identity `(25)`, finite Fourier inversion/convolution on a cyclic group, polynomial interpolation on three points, and the asymptotic squarefree density `6/pi^2`. `MC-S12` already anchors the squarefree-counting input in the line bibliography.

A targeted literature search for Möbius additive Fourier transforms, higher moments, and cubic/third-moment formulations found the established literature on cancellation of Möbius against additive characters and on higher-order correlation questions, but no reason to treat `(6)` as a new theorem of analytic number theory. The identity is an elementary finite-Fourier consequence of `mu^3=mu`, and **no novelty is claimed for it or for the general three-point interpolation obstruction**.

The durable contribution is instead the frontier classification relative to the current Mathia corpus: after `MC-194` leaves nonlinear coupling open, `(5)`--`(9)` provide an explicit source-forced example showing that cubic transverse coupling is possible, while `(10)`--`(28)` show that the entire pointwise-scalar Möbius nonlinear class remains confined to background/support/orientation and cannot by itself supply a new cancellation degree of freedom.

## 6. Boundaries and falsification checks

- The cyclic encoding uses the raw prefix `mu(1),...,mu(N)`, not the aggregated primorial residue vector of `MC-188`--`MC-194`. Therefore this finding does **not** prove a no-go for nonlinear functions of `A_q(X;a)` or for cross-modulus aggregate data.
- The word `transverse` in `(5)` means only nonzero additive Fourier frequency relative to the raw-prefix cyclic encoding. It does not identify those modes with the nonprincipal Dirichlet-character sectors in `MC-188`--`MC-194`.
- Centering is not hiding the desired answer in the definition of `T_N`: equation `(5)` defines `T_N` directly from the nonzero Fourier coefficients of `f_N`. The mean appears only when the exact source identity `(1)` is used to evaluate that statistic.
- Conversely, `(6)` prevents `T_N` from being advertised as an independently easier Mertens statistic. Any proof of an RH-scale bound for `T_N` is already an RH-scale bound for `M(N)` once the elementary squarefree-density bounds are inserted.
- The argument is deterministic and finite. It uses no random-walk model, no zero-free continuation of `1/zeta(s)`, no contour shift, and no RH input.
- The reduction `(10)` concerns **pointwise scalar functions of one Möbius value**. Multisite correlations, divisor couplings, cross-scale interactions, and nonlinearities of aggregated fields are outside its hypotheses and remain live only if they carry independently estimable arithmetic information.
- Changing the complete set of cyclic representatives only multiplies individual Fourier coefficients by compatible phase factors; the zero-sum triad `(5)` and the real-space identity `(15)` are unchanged.
